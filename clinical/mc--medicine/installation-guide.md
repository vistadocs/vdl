---
title: Medicine Version 2.3 Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes and
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
menu_options: 0
description: - [Release Notes](#release-notes) - [Installation Information](#installation-information) - [Environment Check Routine](#environment-check-routine) - [Pre Installation Routines](#pre-installation-routines) - [Post Installation Routines](#post-installation-routines) - [Prior to Installation](#prior-t
audience: 
keywords: 
  - blockquote
  - including
  - your
  - class
  - already
  - mine
  - overwrite
  - table
  - medicine
  - contents
page_count: 0
word_count: 5993
section_count: 11
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc2_3ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc2_3ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=77"
---

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
- [Installation Information](#installation-information)
  - [Environment Check Routine](#environment-check-routine)
  - [Pre Installation Routines](#pre-installation-routines)
  - [Post Installation Routines](#post-installation-routines)
  - [Prior to Installation](#prior-to-installation)
    - [\>D ^%PARTSIZ](#d-partsiz)
  - [Post Installation Check List](#post-installation-check-list)
  - [For all installations on top of version 2.0:](#for-all-installations-on-top-of-version-20)
  - [Health Summary Routines](#health-summary-routines)
  - [Name/Number Spacing](#namenumber-spacing)
  - [Journaling](#journaling)
  - [Routine Size](#routine-size)
- [Virgin Installation (Example)](#virgin-installation-example)
    - [D ^XUP](#d-xup)
- [Installation Over a Version Less Than 2.0 (Example)](#installation-over-a-version-less-than-20-example)
    - [D ^XUP](#d-xup-1)
- [Installation Over Version 2.0 (Example)](#installation-over-version-20-example)
    - [D ^XUP](#d-xup-2)
- [Installation Over Version 2.2 (Example)](#installation-over-version-22-example)
    - [D ^XUP](#d-xup-3)
- [Patch MC\2.2\33 (Copy)](#patch-mc2233-copy)
> This is a maintenance release. Its purpose is to provide a stable version to build upon for future functionality. Only those issues addressed here are implemented. Any other issues with Medicine V. 2.2 will be addressed with patches or in a future version.
1.  This maintenance release includes Medicine 2.2 and patches MC\*2.2\* 1, 2, 3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34.
> Additionally, this release addresses NOIS messages: NYN-0696-10330 NCH-0794-40611 GAI-0596-31465 TUC-0596-60896 PRO-0596-10681 WPB-0596-30187 NYN-0496-12113 WAS-0396-21347 ALT-0396-21236 SFC-0296-61898 LEX-0296-40682 CTX-0496-70134 FAR-0496-41748 WPB-0696-30917 POR-0496-50937 CLA-1295-21830 LOU-0796-42170
> and enhancements for E3Rs: 6984
> 8219
> It also covers Mop-up and Standards and Conventions issues:
> \$NEXT was changed to \$ORDER in the data dictionaries.
> The first and second lines of routines were cleaned up to meet standard formatting practices.
> Naked references were expanded to the full reference or documented.
> Any discrepancies to the use of system wide variables or variables set by Kernel or VA FileMan were documented.
> Locks were cleaned up.
> DD and Audit security (@) were added to all the files.
2.  Many data dictionaries and data that were distributed with V. 2.2 were corrected or updated:
    1.  Changed the input transform of the CARDIAC CATHETERIZATION file (#691.1) to use the PROVIDER key (instead of the VA PROVIDER key) for security check.
    2.  Changed the DIC("S") for all procedure files to use \$G(MCARCODE,U) instead of the local variable MCARCODE only.
    3.  Corrected the formulas for the PF field (#7) and the TLC,VC,FVC,FEV1 CORR.-ORIENTAL field (#11) in the PFT PREDICTED VALUES file (#700.1).
    4.  Deleted three DD nodes that contain no data, those nodes were for the Field Title.
    5.  Cleaned up the MEDICINE VIEW file (#690.2), the PROCEDURE
> /SUBSPECIALTY file (#697.2), the Symptom file (#695.5)(removed the inappropriate data in the Function Field (#1) that points to Laboratory's Function Field file (#61.3)), and the MEDICINE SCREEN (USER) file (#697.3).
6.  The data dictionary and the distributed data of the Symptom file (#695.5) were updated.
> Added the types ECHO, CATH, HOLTER, ETT to the Medical Use (#2) field.
> Added indications for ECHO, CATH, HOLTER, ETT procedures, and the screening of the Symptom field of the these procedure files were updated.
> Added a new KWIC cross reference for easy look up.
7.  Plus, read the information contained under Pre Installation Routines and Post Installation Routines.
3.  It includes NOIS fixes.
    1.  NOIS NCH-0794-40611 and CLA-1295-21830: Corrected the Race Correction for Blacks formula used in the fields 10, 12 and 13 of the PFT Predicated Values file (#700.1).
    2.  NOIS NYN-0696-10330: Renamed the PCE cross reference for 15 procedure files from PCC to APCE.
> c\. NOIS PRO-0596-10681, GAI-0596-31465, TUC-0596-60896, PRO-0596- 10681, WPB-0596-30187, NYN-0496-12113, FAR-0496-41748, WAS-
> 0396-21347: Resolved problems on MED components in Health Summary, problems in Problem Oriented Consult, Generalized Procedure, and Pacemaker.
6.  It includes enhancements proposed in the following E3Rs:
    1.  E3R 8219: Added procedure name to the Workload Reporting e-mail message.
    2.  E3R 6984: Changed the length of the PFT FORMULA field (#.01) in the PFT FORMULA file (# 700.2) from 30 to 50 characters.
7.  The Generalized Procedure Module was revised.
Release Notes
1.  Added two new options, Generalized Procedure Management \[MCGENERICMGR\] and Procedures/Subspecialties Definition Enter/Edit \[MCGENERICPREDT\]. This included the addition of a new routine MCPREDT and an update of the input template \[MCBUILDGENERIC\]. It allows users the ability to define procedures used locally along with the associated CPT codes.
2.  Updated the Generalized Procedure Enter/Edit options (\[MCFLGEN\] and \[MCFSGEN\]\]) by adding the fields Subjective and Objective for editing.
3.  Updated the Brief Generalized Procedure Enter/Edit options (\[MCBLGEN\] and \[MCBSGEN\]) by adding the fields Provider/Physician, Summary, and Procedure Summary for editing.
4.  Updated the Generalized Procedure Report \[MCFPGEN\] and the Brief Generalized Procedure Report \[MCBPGEN\]) to reflect the changes made to the enter/edit options.
8.  The Cardiology ECHO Module was revised.
    1.  Added STUDY TYPE field (#7.5) to the ECHO file (#691) to track/monitor different types of ECHO studies. The options Line Entry/Edit of ECHO test \[MCFLECHO\] and Enter/Edit Echo (Screen) \[MCFSECHO\] were updated and the new field was placed as field 16 on screen 1.
    2.  Added more symptoms to the Symptom file for selection at the Symptom prompt, Screen 1, field 13.
    3.  Provided deletion capability to ECHO reports. (NOIS CTX-0496-70134)
    4.  Added the field SUMMARY to the Brief ECHO Report \[MCBPECHO\].
    5.  Revised the ECHO Test Results \[MCFPECHO\]. (NOIS SFC-0296-61898, LEX-0296-40682 Status was Refer to EP).
9.  The Sphincterotome file (#699.65) was removed in a past version of Medicine and may not have been deleted at all sites. We are ensuring that it is deleted with this release.
10. Cardiology Module: The Atrial Study screen 2 of 2, field \#8 calculated the inverse of what the RP/PR ratio should be. Also fields \#1, \#2, and \#3 didn't show the description when "??" was entered. These items were fixed with this version. The report Results of EP Tests now contains page breaks when printing to the screen.
12. Pulmonary Module: Descriptions were added to the codes for field \#9, screen 2 of 2 for the Pulmonary Endoscopy entry options and fields \#16 and \#19, screen 1 of 2 for the Pulmonary Function entry options. Centigrade was added to the field \#22 name in the Blood Gas secondary screen. Field \#22 of the Special Studies (Exercise) Screen was expanded to accept a 4 digit number with 2 decimal places.
13. Echo Module: Descriptions when questioning a field were added to field \#16 of screen 1 of 4 and field \#1 of screen 3 of 4. The display of the data in Mitral Max Gradient, field \#14 of screen 3 of 4 was fixed (example: display would show 6.0 6 for 6.0). Field \#23 of screen 3 of 4 was expanded by one character.
14. Convert Old Records to Released Not Verified: This option was enhanced by adding the ability to select a date.
> Convert all records prior to: ?
> All records on or prior to this date will be converted. Any records after this date will be left as is.
> Enter an exact date less than or equal to today.

# Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This package was created using Kernel V. 8.0 and VA FileMan V. 21.0 and requires the following packages/versions installed:

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Package Name</u></p>
</blockquote></th>
<th><blockquote>
<p>Minimum <u>Required Version</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTPATIENT PHARMACY</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LAB SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DRG GROUPER</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OE/RR</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADVERSE REACTION TRACKING</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONSULT/REQUEST TRACKING</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Health Summary V. 2.7 and HL7 V. 1.5 need not be installed for Medicine to run, however any components that use Health Summary will not be available.

> Therefore, it is suggested that both Health Summary and HL7 be installed.

> If you are currently running Medicine V. 2.2, a New Person file conversion <u>will not</u> run. It is assumed that your conversion ran to completion andthat the data is clean. Therefore, it would be in your best interest to ensure that the data is correct. See a copy of patch MC\*2.2\*33, page 77, for information. If you have not installed this patch and are unsure of your data, install and run it prior to installation of this version of Medicine.

> A New Person file conversion will be performed if you are running version 2.0. A report of entries that cannot be converted will be produced. The report will contain the Medicine file, field \#, Internal Entry Number, an error message telling you whether it is a broken pointer to File \#6, \#16, or \#200, the pointer numbers if available, and an external form of the Provider Name from the Provider file and/or Person Name from the Person file if they are available. You will need to review this report and make the corrections. If you do not correct the broken pointers, it is possible that records in the Medicine database may point to wrong entries in the New Person file.

> This package can take several hours to install.

## Environment Check Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Checks for the version of Medicine that your site is running.
2.  Checks for required external files from the packages/versions listed above.

> September 1996 Medicine V. 2.3 5

3.  Since version 2.3 cannot be installed if your version of Medicine is <u>less than</u> 2.0, asks the following:

> Delete old Medicine files and Data: NO// Please answer YES or NO

> If you answer YES to this question, all Medicine files and data will be deleted. If you answer NO, the installation will abort. You will not see this question if your version is 2.0 or greater.

4.  Asks for a device (only if you are running V. 2.0) to print the New Person Exception Report for the conversion of data to the New Person file. If you do not enter a device name, the installation will abort.
5.  Checks for patch DI\*21\*25. It uses \$\$PATCH^XPDUTL (part of patch XU\*8\*28, seq. 20, released in April of this year) to check for the presence of the patch.

## Pre Installation Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Remove the 'Select a new patient' item from the 'Medicine/Consult Interface Menu' entry in the Protocol file (#101)
2.  Clean up data in the Procedure/Subspecialty file (#697.2).
3.  Remove the 'M' from the APPLICATION PACKAGES' USE field (#63) of the DRUG file (#50).
4.  If version 2.2 was installed, clean up an unneeded global (^MCNP) that was built during the New Person conversion.
5.  Clean up the data in the Indication file (#694.1).
6.  Clean up all the DDs. If the version is less than 2.0 and you answered "Yes" to "Delete old Medicine files and Data: NO//", they kill every file and the data. If the version is 2.0 or greater, they kill all the DDs leaving the data untouched, with the exception of deleting all the data in Files \#690.2 and \#697.3. (Note: At a test site running DEC Alphas, this routine ran for 1 hour 42 minutes.)
7.  Clean up the ICD Code multiple in the Medical Diagnosis/ICD Codes file (#697.5).
8.  Kill all records with no zero nodes for version 2.0 or better.
9.  Clean up the PFT Predicted Values file (#700.1).

## Post Installation Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Kill all the cross references in every file then rebuilds them. (Note: At a test site running DEC Alphas, this routine ran for 3 hours. This time will depend on the number of entries at your site.)
2.  For version 2.0 only, convert data to the New Person file (#200).
3.  For version 2.0 only, print the New Person Exception Report. This is a report of data that cannot be converted.
4.  For version 2.0 only, move data into the multiple from the flat Instrument field in Endoscopy/Consult file (#699).
5.  Move the Consult data from the Endoscopy/Consult file (#699) to the Generalized Procedure/Consult file (#699.5).
6.  Create the MC Messaging Server mail group.
7.  Fix a sub DD number in the data nodes in the Generalized Procedure/Consult file (#699.5).
8.  Delete all pointers to the Lab files.
9.  Add the cardiology code to the Medical Package Use multiple in the Medication file (#695).
10. For version 2.0 only, move Micro Description Remarks from a free text field to the word processing field in the Hematology file (#694).
11. Update pointers from the Procedure Term file (#694.8) to the Procedure/ Subspecialty file (#697.2).
12. Update Medicine package file level access security.
13. Restore locally defined procedures to the Medicine View file (#690.2) since the data in the Medicine View file is deleted in a pre-install routine.

## Prior to Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If you are installing over a previous version of Medicine, you must install patch DI\*21\*25 before installing the Medicine software.
- Medicine V. 2.3 is distributed in KIDS format.
- Do not delete any Medicine routines. The installation will delete them for you.
- The installation will kill all the Data Dictionaries for the package, so if you made any local changes to the DDs, you may want to save them off to another area.
- This package was exported using the Kernel Installation and Distribution System (KIDS). You will use KIDS to install this software. If you are not familiar with KIDS installations, please read your KIDS documentation before you install this software.
- Make sure you have the required external packages installed. See list on page 1.
- If you are running Medicine V. 2.2, make sure the New Person conversion ran to completion and that the data is accurate. See a copy of patch MC\*2.2\*33, page 77 of this manual.
- If your site is running a version less than 2.0, are you ready to delete the DDs and data for that version? You cannot install over a version less than 2.0.
- Queuing of the installation is not permitted due to the current limitations of KIDS and the distribution of large print templates.
- Make sure you have a device available to print conversion reports. You can queue to that device. The installation will abort if you cannot provide a device name.
- All users of the package should log off. All others may remain on-line.
- On MSM systems the installation process will prompt you to move the package's routines to other CPUs. If you inhibit logons to the CPUs receiving the routines you must shutdown TaskMan otherwise the routines will not be moved.

> If you are running a partition size of 40K or less on an MSM system, you must increase the partition size to 45K prior to installation. This is only necessary during installation. An example is shown here:

### \>D ^%PARTSIZ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MSM - Partition Size Utility 16-JUL-96 12:59 PM

> Enter partition size \<40\> 45

> Partition size changed from 40K to 45K

> \>

- Backup the system.
- Disable mapping if applicable.
- Disable journaling, if applicable (MC\* globals).
- Invoke the KIDS menu to load the Medicine V. 2.3 distribution global (MC2_3.KID). Use the KIDS Build File Print option if you wish to obtain a complete listing of package components (e.g., routines and options) sent with this Distribution file.
- Verify checksums in transport global.
- Run the Install Package(s) option.
- Installation examples are on Alpha systems and assume TaskMan is running.

> Note: 1. The installation example dialogues that follow may vary depending on the system you have (Alpha or MSM) and the additional work that must be done in the pre- and post- installation process. The installation examples shown are on an Alpha system.

> 2\. If during the installation process you receive the message

> \*\* ERROR IN POINTER RESOLUTION OF DATA \*\*

> Unable to find exact match and resolve pointer (^MCAR(697.2, Entry:XXX)

> where "XXX" is the name of a Procedure/Subspecialty, this most likely indicates duplicates in the Procedure/Subspecialty file (#697.2). This will not adversely affect the installation or the operation of the package. Customer Service can be contacted at a future time for cleanup and resolution of duplicate entries.

## Post Installation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Move the Medicine routines (MC\*) onto all your systems, if applicable.

## For all installations on top of version 2.0:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Review the Medicine New Person Exception Report that was generated during the installation. Fix any exceptions reported.
2.  Rerun the New Person conversion ( D ^MCPOS02 ) until the report returns no exceptions.
3.  Rerun the Consult conversion ( D ^MCPOS04 ).
4.  You may wish to run the Unique New Person Names in Medicine Provider Fields report (D ^MCNP2CHK). This report goes through all the Medicine files that have fields with pointers to the New Person file (#200) and prints a unique listing of persons for those fields, their IEN and whether or not they hold the Provider Key. This should help you clean up any inaccurate data. Here is an example of the report:

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 19%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CARDIOLOGY ATTENDING field (#39)</p>
</blockquote></th>
<th><blockquote>
<p>10000</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>KANSAS,HARVEY</p>
</blockquote></td>
<td><blockquote>
<p>1867</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CARDIOLOGY FELLOW field (#43)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CALI FORNI A,JUDY</p>
</blockquote></td>
<td><blockquote>
<p>4601</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KANSAS,HARVEY</p>
</blockquote></td>
<td><blockquote>
<p>1867</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PENNSYLVANI A,MISTER</p>
</blockquote></td>
<td><blockquote>
<p>4589</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>CARDIAC CATHETERIZATION file (#691.1)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CARDIOLOGY FELLOW field (#62)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ARKANSAS,WILLIAM A</p>
</blockquote></td>
<td><blockquote>
<p>151</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CARDIOLOGY STAFF field (#63)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ALABAMA,DARRYL</p>
</blockquote></td>
<td><blockquote>
<p>448</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Enable journaling, if applicable.
- For multiple CPUs, the ^MCAR global must be translated.
- Insure that the following fields of the Terminal Type file (#3.2) are defined for each terminal type at your site that is being used with the Medicine package. This is necessary to provide support for the screen edit driver routines.

> XY CRT

> Erase to End of Page High Intensity

> Low Intensity

- The installation killed all the Data Dictionaries for the package, so if you made any local changes to the DDs, you may want to add those changes to the DDs.
- Make sure all provider users of the medicine package have an electronic signature.
- Assign security keys to the appropriate users if this is a virgin install or an install over a version less than 2.0. (See Security Keys under the Security chapter in the Medicine Technical Manual.)
- Assign menu options to the appropriate users if this is a virgin install or an install over a version less than 2.0. (See Menu Option Assignment under the Security chapter in the Medicine Technical Manual.
- When a procedure for a patient is completed (results entered into the Medicine package) and the procedure has been signed and released, the Medicine package will send a message to a mail group and/or report to a device that contains the Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time. If your users want this capability, within the

> Workload Reporting Management \[MCWKLDM\] menu make sure following is done:

- Turn on the workload reporting toggle using the option Workload Reporting ON/OFF Toggle \[MCWKLDT\] option.

> WORKLOAD REPORTING: NO// Y YES

- Set up a list of devices for the users via the Workload Reporting Device \[MCWKLDD\] option. It provides a mechanism for the user to select a printing device or devices to receive message transmissions (Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time).

> and/or

- Make sure to define a mail group for them before using the Workload Reporting Mailgroup Selection \[MCWKLDG\] option. It provides a mechanism for the user to select a mail group to receive message transmissions (Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time). Example:

> Select WORKLOAD MAIL GROUP: CARDIOLOGY// Pulmonary

> Are you adding 'PULMONARY' as a new WORKLOAD MAIL GROUP (the 2ND for this MEDICINE PACKAGE PARAMETERS)? Y (YES)

> Select WORKLOAD MAIL GROUP: \<RET\>

- If your site is using OE/RR, make sure it is turned on using the option Enable/Disable OE/RR \[MCORHOOK\].

> Do you want to enable Order Entry/Results Reporting? y YES OE/RR enabled!

- The rest of the set-up can be done by your users. For more complete information on the user's portion of the set-up, refer to the Implementation and Maintenance chapter of the Medicine Technical Manual. They may need some guidance from you.
- Use the KIDS Install File Print option if you wish to print out the results of the installation process.

## Health Summary Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are upgrading from Medicine V. 2.2 to Medicine V. 2.3, you do not need to do anything with the Health Summary routines. For all other installations, see the

> September 1996 Medicine V. 2.3 11

> instructions for the Medicine package on page 44 of the Health Summary V. 2.7 Installation Guide.

## Name/Number Spacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The namespace assigned to the Medicine package is MC. All routines, globals, options, edit and print templates start with these characters. All routines generated from templates have the namespace MCARO, MCOB, MCOE, or MCOP. All files use the ^MCAR global namespace.

> The Medicine package number space is 690 through 704. The package currently uses 690 through 701. Number spaces 702 through 704 are reserved for future growth.

## Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is highly recommended that the ^MCAR global be journaled.

## Routine Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The compiled print routines occupy approximately 300 K bytes and the package routines occupy approximately 447 K bytes.

# Virgin Installation (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### D ^XUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: EVE Systems Manager Menu

> Core Applications ... Device Management ...

> FM VA FileMan ...

> Manage Mailman ... Menu Management ... Programmer Options ...

> Operations Management ... Spool Management ...

> System Security ... Taskman Management ... User Management ...

> Application Utilities ... Capacity Management ...

> MailMan Menu ...

> Select Systems Manager Menu Option: Programmer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options Option: KIDS Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System

> September 1996 Medicine V. 2.3 13

> Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Load a Distribution Enter a Host File: MC2_3.KID

> KIDS Distribution saved on Jun 03, 1996@10:48:08 Comment: Medicine 2.3

> This Distribution contains Transport Globals for the following Package(s): MEDICINE 2.3

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Medicine package not found.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Use MEDICINE 2.3 to install this Distribution.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: MEDICINE 2.3 Loaded from Distribution 6/3/96@13:36:34

> =\> Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> This Distribution was loaded on Jun 03, 1996@13:36:34 with header of Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> It consisted of the following Install(s): MEDICINE 2.3

> Will first run the Environment Check Routine, MCENV00 Checking for previous version of the medicine package. Medicine package not found.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Install Questions for MEDICINE 2.3

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 70%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>690</p>
</blockquote></th>
<th><blockquote>
<p>MEDICAL PATIENT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>690.1</p>
</blockquote></td>
<td><blockquote>
<p>MEDICINE PACKAGE PARAMETERS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.2</p>
</blockquote></td>
<td><blockquote>
<p>MEDICINE VIEW (including data)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.5</p>
</blockquote></td>
<td><blockquote>
<p>ASTM (including data)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.97</p>
</blockquote></td>
<td><blockquote>
<p>MCQ POLLING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.99</p>
</blockquote></td>
<td><blockquote>
<p>*NEW PERSON CONVERSION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691</p>
</blockquote></td>
<td><blockquote>
<p>ECHO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.1</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC CATHETERIZATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.5</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROCARDIOGRAM (EKG)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.6</p>
</blockquote></td>
<td><blockquote>
<p>HOLTER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.7</p>
</blockquote></td>
<td><blockquote>
<p>EXERCISE TOLERANCE TEST</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.8</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROPHYSIOLOGY (EP)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.9</p>
</blockquote></td>
<td><blockquote>
<p>ATRIAL STUDY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>692</p>
</blockquote></td>
<td><blockquote>
<p>VENTRICULAR STUDY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693</p>
</blockquote></td>
<td><blockquote>
<p>MEDICAL DESCRIPTION (including</p>
</blockquote></td>
<td><blockquote>
<p>data)</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  INTERPRETATION (including data)
3.  ECG INTERPRETATION (including data)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>693.5</p>
</blockquote></th>
<th><blockquote>
<p>RECORDING SITE (including data)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>693.6</p>
</blockquote></td>
<td><blockquote>
<p>EP INTERVENTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694</p>
</blockquote></td>
<td><blockquote>
<p>HEMATOLOGY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.1</p>
</blockquote></td>
<td><blockquote>
<p>INDICATION (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694.5</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC SURGERY RISK ASSESSMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.8</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE TERM (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695</p>
</blockquote></td>
<td><blockquote>
<p>MEDICATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.1</p>
</blockquote></td>
<td><blockquote>
<p>REGIONAL WALL MOTION (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.3</p>
</blockquote></td>
<td><blockquote>
<p>CATH PROCEDURE (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.4</p>
</blockquote></td>
<td><blockquote>
<p>PAST HISTORY AND RISK FACTOR (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.5</p>
</blockquote></td>
<td><blockquote>
<p>SYMPTOM (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.6</p>
</blockquote></td>
<td><blockquote>
<p>HEART CATHETER (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.8</p>
</blockquote></td>
<td><blockquote>
<p>REASON (MEDICINE) (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.9</p>
</blockquote></td>
<td><blockquote>
<p>NORMALITY OF CORONARY VESSEL (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696</p>
</blockquote></td>
<td><blockquote>
<p>SEGMENT OF CORONARY ARTERIES (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.1</p>
</blockquote></td>
<td><blockquote>
<p>PERCENTAGE LESION (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.2</p>
</blockquote></td>
<td><blockquote>
<p>LESION MORPHOLOGY (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.3</p>
</blockquote></td>
<td><blockquote>
<p>MORPHOLOGY OF DISTAL VESSEL (including data)</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  BYPASS GRAFT SEGMENT (including data)
5.  LEFT VENTRICULOGRAPHY (including data)

> 696.7 MITRAL REGURG ON LV GRAM (including data)

> 696.9 COMPLICATION (including data) 697 ANATOMY (including data)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>697.1</p>
</blockquote></th>
<th><blockquote>
<p>REFERRING PHYSICIAN/AGENCY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>697.2</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE/SUBSPECIALTY (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697.3</p>
</blockquote></td>
<td><blockquote>
<p>MEDICINE SCREEN (USER) (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.5</p>
</blockquote></td>
<td><blockquote>
<p>MEDICAL DIAGNOSIS/ICD CODES (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698</p>
</blockquote></td>
<td><blockquote>
<p>GENERATOR IMPLANT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.1</p>
</blockquote></td>
<td><blockquote>
<p>V LEAD IMPLANT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.2</p>
</blockquote></td>
<td><blockquote>
<p>A LEAD IMPLANT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.3</p>
</blockquote></td>
<td><blockquote>
<p>PACEMAKER SURVEILLANCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.4</p>
</blockquote></td>
<td><blockquote>
<p>PACEMAKER EQUIPMENT (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.6</p>
</blockquote></td>
<td><blockquote>
<p>PACEMAKER MANUFACTURER (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.9</p>
</blockquote></td>
<td><blockquote>
<p>NON-MAGNET ECG RHYTHM (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699</p>
</blockquote></td>
<td><blockquote>
<p>ENDOSCOPY/CONSULT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.48</p>
</blockquote></td>
<td><blockquote>
<p>INSTRUMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.5</p>
</blockquote></td>
<td><blockquote>
<p>GENERALIZED PROCEDURE/CONSULT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.55</p>
</blockquote></td>
<td><blockquote>
<p>GROSS (including data)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>699.57</p>
</blockquote></th>
<th><blockquote>
<p>MODIFIER (including data)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>699.6</p>
</blockquote></td>
<td><blockquote>
<p>DIAG/THERAP INTERVENT (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.7</p>
</blockquote></td>
<td><blockquote>
<p>ENDOSCOPIC DEVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.81</p>
</blockquote></td>
<td><blockquote>
<p>RESULTS (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.82</p>
</blockquote></td>
<td><blockquote>
<p>CONSULTATION TYPE (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.83</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION OF PAIN/PNEUMONIAS (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.84</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE EVALUATION (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.85</p>
</blockquote></td>
<td><blockquote>
<p>FOLLOWUP DEVICE/THERAPY (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.86</p>
</blockquote></td>
<td><blockquote>
<p>SURVEILLANCE (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.88</p>
</blockquote></td>
<td><blockquote>
<p>NON-ENDOSCOPIC PROCEDURE (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>700</p>
</blockquote></td>
<td><blockquote>
<p>PULMONARY FUNCTION TESTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>700.1</p>
</blockquote></td>
<td><blockquote>
<p>PFT PREDICTED VALUES (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>700.2</p>
</blockquote></td>
<td><blockquote>
<p>PFT FORMULA (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>700.5</p>
</blockquote></td>
<td><blockquote>
<p>MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>701</p>
</blockquote></td>
<td><blockquote>
<p>RHEUMATOLOGY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages. Enter a '^' to abort the install.

> DEVICE: HOME// (Enter a device name)

> MEDICINE 2.3

> Install Started for MEDICINE 2.3 :

> Jun 03, 1996@13:38:05

> Installing Routines:

> Jun 03, 1996@13:38:51

> Running Pre-Install Routine: ^MCPRE00 Installing Data Dictionaries:

> Jun 03, 1996@13:41:01

> Installing Data: ............................................................

> Jun 03, 1996@13:46:02

> Installing PACKAGE COMPONENTS:

> Installing SECURITY KEY Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE Installing OPTION

> Jun 03, 1996@13:49:45

> Running Post-Install Routine: ^MCPOS00 Updating Routine file...

> The following Routines were created during this install:

> MCOPRG

> MCOPRG1 MCOPRG2 MCAROC4 MCAROC41 MCAROC3 MCAROC31 MCAROC2 MCAROC21 MCAROC22 MCAROC1 MCAROT MCAROT1 MCAROK MCAROK1 MCAROEP MCAROEP1 MCAROV MCAROV1 MCAROH1 MCAROH11 MCAROH2

> MCAROGR MCAROGI MCAROGN MCAROG MCAROG1 MCAROHD MCAROHB MCAROHF MCAROPG MCAROPG1 MCAROPA MCAROPA1 MCAROPV MCAROPV1 MCAROPS MCAROPS1 MCAROE1 MCAROS0 MCAROS1 MCAROS2 MCAROS3 MCAROPF MCAROS4 MCARORB MCARORH MCARORH1 MCARORH2 MCAROGA MCAROGA1 MCAROP MCAROPE MCAROPE1 MCARORQ MCARORD MCARORN MCAROE2 MCARORP MCARORP1 MCARORL MCARORL1 MCARORL2 MCARORA MCARORE MCARORE1 MCAROGM MCARORF MCARORF1 MCARORF2 MCARORF3 MCAROGC MCAROGE MCOBC1 MCOBC11 MCOBE1 MCOBK MCOBEP MCOBH1 MCOBT MCOBGC MCOBGA

> MCOBGA1 MCOBGN MCOBPE MCOBPFT MCOBHEM MCOBPG MCOBPA MCOBPV MCOBPS MCOBPS1 MCOBGEN MCOBRH MCOBRH1 MCOBRHA MCOBRHA1 MCOBPF MCAROAT MCAROAT1 MCAROAT2

> Updating KIDS files... MEDICINE 2.3 Installed.

> Jun 03, 1996@13:50:11

> Not a production UCI

> NO Install Message sent

> September 1996 Medicine V. 2.3 21

> Install Completed

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global Select Installation Option:

# Installation Over a Version Less Than 2.0 (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### D ^XUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: EVE Systems Manager Menu

> Core Applications ... Device Management ...

> FM VA FileMan ...

> Manage Mailman ... Menu Management ... Programmer Options ...

> Operations Management ... Spool Management ...

> System Security ... Taskman Management ... User Management ...

> Application Utilities ... Capacity Management ...

> MailMan Menu ...

> Select Systems Manager Menu Option: Programmer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options Option: KIDS Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System

> September 1996 Medicine V. 2.3 23

> Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Load a Distribution Enter a Host File: MC2_3.KID

> KIDS Distribution saved on Jun 03, 1996@10:48:08 Comment: Medicine 2.3

> This Distribution contains Transport Globals for the following Package(s): MEDICINE 2.3

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 1.5.

> You are running a version of the Medicine package less than 2.0. Medicine 2.3 can only install over top of version 2.0, 2.2, or in a virgin account.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Use MEDICINE 2.3 to install this Distribution.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: MEDICINE 2.3 Loaded from Distribution 6/3/96@14:31:48

> =\> Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> This Distribution was loaded on Jun 03, 1996@14:31:48 with header of Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> It consisted of the following Install(s): MEDICINE 2.3

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 1.5.

> You are running a version of the Medicine package less than 2.0. Medicine 2.3 can only install over top of version 2.0, 2.2, or in a virgin account.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Cannot install over version 1.5.

> Delete old Medicine files and data? No// ?

> You are running a version of the Medicine package less than 2.0. Medicine 2.3 can only install over top of version 2.0, 2.2, or in a virgin account. If you answer YES to this question, ALL MEDICINE FILES AND DATA WILL BE DELETED. If you answer NO, the installation will abort.

> Please answer YES or NO

> Cannot install over version 1.5.

> Delete old Medicine files and data? No// YES

> All Medicine files and data will be deleted! Are you sure? No// ?

> Answering YES to this question will cause the deletion of all Medicine files and data.

> Please answer YES or NO

> All Medicine files and data will be deleted! Are you sure? No// YES

> Install Questions for MEDICINE 2.3

690. MEDICAL PATIENT

> Note: You already have the 'MEDICAL PATIENT' File.

1.  MEDICINE PACKAGE PARAMETERS
2.  MEDICINE VIEW (including data)

> 690.5 ASTM (including data)

> 690.97 MCQ POLLING

> 690.99 \*NEW PERSON CONVERSION 691 ECHO

> Note: You already have the 'ECHO' File.

> 691.1 CARDIAC CATHETERIZATION

> Note: You already have the 'CARDIAC CATHETERIZATION' File.

5.  ELECTROCARDIOGRAM (EKG)

> Note: You already have the 'ELECTROCARDIOGRAM (EKG)' File.

6.  HOLTER

> Note: You already have the 'HOLTER' File.

7.  EXERCISE TOLERANCE TEST

> Note: You already have the 'EXERCISE TOLERANCE TEST' File.

8.  ELECTROPHYSIOLOGY (EP)

> Note: You already have the 'ELECTROPHYSIOLOGY (EP)' File.

9.  ATRIAL STUDY

> Note: You already have the 'ATRIAL STUDY' File.

692. VENTRICULAR STUDY

> Note: You already have the 'VENTRICULAR STUDY' File.

693. MEDICAL DESCRIPTION (including data) Note: You already have the 'MEDICAL DESCRIPTION' File. I will OVERWRITE your data with mine.
     2.  INTERPRETATION (including data)

> \*BUT YOU ALREADY HAVE 'IMPRESSION POST CATHETERIZATION' AS FILE \#693.2!

> Shall I write over your IMPRESSION POST CATHETERIZATION File? YES// \<RET\>

> I will OVERWRITE your data with mine.

3.  ECG INTERPRETATION (including data) Note: You already have the 'ECG INTERPRETATION' File. I will OVERWRITE your data with mine.
5.  RECORDING SITE (including data)

> \*BUT YOU ALREADY HAVE 'CATHETER PLACEMENT SITE' AS FILE \#693.5!

> Shall I write over your CATHETER PLACEMENT SITE File? YES// \<RET\>

> I will OVERWRITE your data with mine.

6.  EP INTERVENTION

> Note: You already have the 'EP INTERVENTION' File.

694. HEMATOLOGY

> Note: You already have the 'HEMATOLOGY' File.

1.  INDICATION (including data) Note: You already have the 'INDICATION' File. I will OVERWRITE your data with mine.

> 694.5 CARDIAC SURGERY RISK ASSESSMENT

> Note: You already have the 'CARDIAC SURGERY RISK ASSESSMENT' File.

> 694.8 PROCEDURE TERM (including data) 695 MEDICATION

> Note: You already have the 'MEDICATION' File.

> 695.1 REGIONAL WALL MOTION (including data) Note: You already have the 'REGIONAL WALL MOTION' File. I will OVERWRITE your data with mine.

3.  CATH PROCEDURE (including data) Note: You already have the 'CATH PROCEDURE' File. I will OVERWRITE your data with mine.
4.  PAST HISTORY AND RISK FACTOR (including data) Note: You already have the 'PAST HISTORY AND RISK FACTOR' File. I will OVERWRITE your data with mine.
5.  SYMPTOM (including data) Note: You already have the 'SYMPTOM' File. I will OVERWRITE your data with mine.
6.  HEART CATHETER (including data) Note: You already have the 'HEART CATHETER' File. I will OVERWRITE your data with mine.
8.  REASON (MEDICINE) (including data) Note: You already have the 'REASON (MEDICINE)' File. I will OVERWRITE your data with mine.
9.  NORMALITY OF CORONARY VESSEL (including data) Note: You already have the 'NORMALITY OF CORONARY VESSEL' File. I will OVERWRITE your data with mine.
696. SEGMENT OF CORONARY ARTERIES (including data) Note: You already have the 'SEGMENT OF CORONARY ARTERIES' File. I will OVERWRITE your data with mine.
     1.  PERCENTAGE LESION (including data) Note: You already have the 'PERCENTAGE LESION' File. I will OVERWRITE your data with mine.
     2.  LESION MORPHOLOGY (including data) Note: You already have the 'LESION MORPHOLOGY' File. I will OVERWRITE your data with mine.
     3.  MORPHOLOGY OF DISTAL VESSEL (including data) Note: You already have the 'MORPHOLOGY OF DISTAL VESSEL' File. I will OVERWRITE your data with mine.
     4.  BYPASS GRAFT SEGMENT (including data) Note: You already have the 'BYPASS GRAFT SEGMENT' File. I will OVERWRITE your data with mine.
     5.  LEFT VENTRICULOGRAPHY (including data) Note: You already have the 'LEFT VENTRICULOGRAPHY' File. I will OVERWRITE your data with mine.

> 696.7 MITRAL REGURG ON LV GRAM (including data) Note: You already have the 'MITRAL REGURG ON LV GRAM' File. I will OVERWRITE your data with mine.

> 696.9 COMPLICATION (including data) Note: You already have the 'COMPLICATION' File. I will OVERWRITE your data with mine.

697. ANATOMY (including data) Note: You already have the 'ANATOMY' File. I will OVERWRITE your data with mine.
     1.  REFERRING PHYSICIAN/AGENCY

> Note: You already have the 'REFERRING PHYSICIAN/AGENCY' File.

2.  PROCEDURE/SUBSPECIALTY (including data)

> \*BUT YOU ALREADY HAVE 'PROCEDURE LOCATION' AS FILE \#697.2!

> Shall I write over your PROCEDURE LOCATION File? YES// \<RET\>

> I will MERGE your data with mine.

3.  MEDICINE SCREEN (USER) (including data)

> \*BUT YOU ALREADY HAVE 'CARDIOLOGY SCREEN (USER)' AS FILE \#697.3!

> Shall I write over your CARDIOLOGY SCREEN (USER) File? YES// \<RET\>

> I will OVERWRITE your data with mine.

> 697.5 MEDICAL DIAGNOSIS/ICD CODES (including data) Note: You already have the 'MEDICAL DIAGNOSIS/ICD CODES' File. I will OVERWRITE your data with mine.

698. GENERATOR IMPLANT

> Note: You already have the 'GENERATOR IMPLANT' File.

1.  V LEAD IMPLANT

> Note: You already have the 'V LEAD IMPLANT' File.

2.  A LEAD IMPLANT

> Note: You already have the 'A LEAD IMPLANT' File.

3.  PACEMAKER SURVEILLANCE

> Note: You already have the 'PACEMAKER SURVEILLANCE' File.

4.  PACEMAKER EQUIPMENT (including data) Note: You already have the 'PACEMAKER EQUIPMENT' File. I will OVERWRITE your data with mine.

> 698.6 PACEMAKER MANUFACTURER (including data) Note: You already have the 'PACEMAKER MANUFACTURER' File. I will OVERWRITE your data with mine.

> 698.9 NON-MAGNET ECG RHYTHM (including data) Note: You already have the 'NON-MAGNET ECG RHYTHM' File. I will OVERWRITE your data with mine.

699. ENDOSCOPY/CONSULT

> \*BUT YOU ALREADY HAVE 'ENDOSCOPY' AS FILE \#699!

> Shall I write over your ENDOSCOPY File? YES// \<RET\>

> 699.48 INSTRUMENT

> Note: You already have the 'INSTRUMENT' File.

> 699.5 GENERALIZED PROCEDURE/CONSULT

> 699.55 GROSS (including data) Note: You already have the 'GROSS' File. I will OVERWRITE your data with mine.

> 699.57 MODIFIER (including data) Note: You already have the 'MODIFIER' File. I will OVERWRITE your data with mine.

6.  DIAG/THERAP INTERVENT (including data) Note: You already have the 'DIAG/THERAP INTERVENT' File. I will OVERWRITE your data with mine.
7.  ENDOSCOPIC DEVICE

> \*BUT YOU ALREADY HAVE 'STENT' AS FILE \#699.7!

> Shall I write over your STENT File? YES// \<RET\>

81. RESULTS (including data) Note: You already have the 'RESULTS' File. I will OVERWRITE your data with mine.
82. CONSULTATION TYPE (including data) Note: You already have the 'CONSULTATION TYPE' File. I will OVERWRITE your data with mine.
83. LOCATION OF PAIN/PNEUMONIAS (including data) Note: You already have the 'LOCATION OF PAIN/PNEUMONIAS' File. I will OVERWRITE your data with mine.
84. DISEASE EVALUATION (including data) Note: You already have the 'DISEASE EVALUATION' File. I will OVERWRITE your data with mine.
85. FOLLOWUP DEVICE/THERAPY (including data) Note: You already have the 'FOLLOWUP DEVICE/THERAPY' File. I will OVERWRITE your data with mine.
86. SURVEILLANCE (including data) Note: You already have the 'SURVEILLANCE' File. I will OVERWRITE your data with mine.

> 699.88 NON-ENDOSCOPIC PROCEDURE (including data) Note: You already have the 'NON-ENDOSCOPIC PROCEDURE' File. I will OVERWRITE your data with mine.

700. PULMONARY FUNCTION TESTS
     1.  PFT PREDICTED VALUES (including data)
     2.  PFT FORMULA (including data)

> 700.5 MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY

> Note: You already have the 'MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY' File.

701. RHEUMATOLOGY

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages. Enter a '^' to abort the install.

> DEVICE: HOME// (Enter a device name)

> MEDICINE 2.3

> Install Started for MEDICINE 2.3 :

> Jun 03, 1996@14:33:18

> Installing Routines:

> Jun 03, 1996@14:33:36

> Running Pre-Install Routine: ^MCPRE00 Killing the Medicine data dictionaries.

> Note: At this point a number of blank lines will be printed as the files are deleted.

> Installing Data Dictionaries:

> Jun 03, 1996@14:36:21

> Installing Data: ............................................................

> Jun 03, 1996@14:41:27

> Installing PACKAGE COMPONENTS:

> Installing SECURITY KEY Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE Installing OPTION

> Jun 03, 1996@14:45:30

> Running Post-Install Routine: ^MCPOS00 Updating Routine file...

> The following Routines were created during this install:

> MCOPRG

> MCOPRG1 MCOPRG2 MCAROC4 MCAROC41 MCAROC3 MCAROC31 MCAROC2 MCAROC21 MCAROC22 MCAROC1 MCAROT MCAROT1 MCAROK MCAROK1 MCAROEP

> MCAROEP1 MCAROV MCAROV1 MCAROH1 MCAROH11 MCAROH2 MCAROGR MCAROGI MCAROGN MCAROG MCAROG1 MCAROHD MCAROHB MCAROHF MCAROPG MCAROPG1 MCAROPA MCAROPA1 MCAROPV MCAROPV1 MCAROPS MCAROPS1 MCAROE1 MCAROS0 MCAROS1 MCAROS2 MCAROS3 MCAROPF MCAROS4 MCARORB MCARORH MCARORH1 MCARORH2 MCAROGA MCAROGA1 MCAROP MCAROPE MCAROPE1 MCARORQ MCARORD MCARORN MCAROE2 MCARORP MCARORP1 MCARORL MCARORL1 MCARORL2 MCARORA MCARORE MCARORE1 MCAROGM MCARORF MCARORF1 MCARORF2 MCARORF3 MCAROGC MCAROGE MCOBC1 MCOBC11 MCOBE1

> MCOBK MCOBEP MCOBH1 MCOBT MCOBGC MCOBGA MCOBGA1 MCOBGN MCOBPE MCOBPFT MCOBHEM MCOBPG MCOBPA MCOBPV MCOBPS MCOBPS1 MCOBGEN MCOBRH MCOBRH1 MCOBRHA MCOBRHA1 MCOBPF MCAROAT MCAROAT1 MCAROAT2

> Updating KIDS files... MEDICINE 2.3 Installed.

> Jun 03, 1996@14:45:54

> Not a production UCI

> NO Install Message sent

> Install Completed

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global Select Installation Option:

> September 1996 Medicine V. 2.3 35

# Installation Over Version 2.0 (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### D ^XUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: EVE Systems Manager Menu

> Core Applications ... Device Management ...

> FM VA FileMan ...

> Manage Mailman ... Menu Management ... Programmer Options ...

> Operations Management ... Spool Management ...

> System Security ... Taskman Management ... User Management ...

> Application Utilities ... Capacity Management ...

> MailMan Menu ...

> Select Systems Manager Menu Option: Programmer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options Option: KIDS Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System

> September 1996 Medicine V. 2.3 37

> Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Load a Distribution Enter a Host File: MC2_3.KID

> KIDS Distribution saved on Jun 03, 1996@10:48:08 Comment: Medicine 2.3

> This Distribution contains Transport Globals for the following Package(s): MEDICINE 2.3

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 2.0.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Use MEDICINE 2.3 to install this Distribution.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: MEDICINE 2.3 Loaded from Distribution 6/3/96@10:56:16

> =\> Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> This Distribution was loaded on Jun 03, 1996@10:56:16 with header of Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> It consisted of the following Install(s):

> MEDICINE 2.3

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 2.0.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Device for conversion reports (required): \<Enter a Device Name\>

> Install Questions for MEDICINE 2.3

690. MEDICAL PATIENT

> Note: You already have the 'MEDICAL PATIENT' File.

1.  MEDICINE PACKAGE PARAMETERS
2.  MEDICINE VIEW (including data)

> 690.5 ASTM (including data)

> 690.97 MCQ POLLING

> 690.99 \*NEW PERSON CONVERSION 691 ECHO

> Note: You already have the 'ECHO' File.

> 691.1 CARDIAC CATHETERIZATION

> Note: You already have the 'CARDIAC CATHETERIZATION' File.

5.  ELECTROCARDIOGRAM (EKG)

> Note: You already have the 'ELECTROCARDIOGRAM (EKG)' File.

6.  HOLTER

> Note: You already have the 'HOLTER' File.

7.  EXERCISE TOLERANCE TEST

> Note: You already have the 'EXERCISE TOLERANCE TEST' File.

8.  ELECTROPHYSIOLOGY (EP)

> Note: You already have the 'ELECTROPHYSIOLOGY (EP)' File.

9.  ATRIAL STUDY

> Note: You already have the 'ATRIAL STUDY' File.

692. VENTRICULAR STUDY

> Note: You already have the 'VENTRICULAR STUDY' File.

693. MEDICAL DESCRIPTION (including data) Note: You already have the 'MEDICAL DESCRIPTION' File. I will OVERWRITE your data with mine.
     2.  INTERPRETATION (including data) Note: You already have the 'INTERPRETATION' File. I will OVERWRITE your data with mine.
     3.  ECG INTERPRETATION (including data) Note: You already have the 'ECG INTERPRETATION' File. I will OVERWRITE your data with mine.
     5.  RECORDING SITE (including data) Note: You already have the 'RECORDING SITE' File. I will OVERWRITE your data with mine.
     6.  EP INTERVENTION

> Note: You already have the 'EP INTERVENTION' File.

694. HEMATOLOGY

> Note: You already have the 'HEMATOLOGY' File.

1.  INDICATION (including data) Note: You already have the 'INDICATION' File. I will OVERWRITE your data with mine.

> 694.5 CARDIAC SURGERY RISK ASSESSMENT

> Note: You already have the 'CARDIAC SURGERY RISK ASSESSMENT' File.

> 694.8 PROCEDURE TERM (including data) 695 MEDICATION

> Note: You already have the 'MEDICATION' File.

> 695.1 REGIONAL WALL MOTION (including data) Note: You already have the 'REGIONAL WALL MOTION' File. I will OVERWRITE your data with mine.

3.  CATH PROCEDURE (including data) Note: You already have the 'CATH PROCEDURE' File. I will OVERWRITE your data with mine.
4.  PAST HISTORY AND RISK FACTOR (including data) Note: You already have the 'PAST HISTORY AND RISK FACTOR' File. I will OVERWRITE your data with mine.
5.  SYMPTOM (including data) Note: You already have the 'SYMPTOM' File. I will OVERWRITE your data with mine.
6.  HEART CATHETER (including data) Note: You already have the 'HEART CATHETER' File. I will OVERWRITE your data with mine.
8.  REASON (MEDICINE) (including data) Note: You already have the 'REASON (MEDICINE)' File. I will OVERWRITE your data with mine.
9.  NORMALITY OF CORONARY VESSEL (including data) Note: You already have the 'NORMALITY OF CORONARY VESSEL' File. I will OVERWRITE your data with mine.
696. SEGMENT OF CORONARY ARTERIES (including data) Note: You already have the 'SEGMENT OF CORONARY ARTERIES' File. I will OVERWRITE your data with mine.
     1.  PERCENTAGE LESION (including data) Note: You already have the 'PERCENTAGE LESION' File. I will OVERWRITE your data with mine.
     2.  LESION MORPHOLOGY (including data) Note: You already have the 'LESION MORPHOLOGY' File. I will OVERWRITE your data with mine.
     3.  MORPHOLOGY OF DISTAL VESSEL (including data) Note: You already have the 'MORPHOLOGY OF DISTAL VESSEL' File. I will OVERWRITE your data with mine.
     4.  BYPASS GRAFT SEGMENT (including data) Note: You already have the 'BYPASS GRAFT SEGMENT' File. I will OVERWRITE your data with mine.
     5.  LEFT VENTRICULOGRAPHY (including data) Note: You already have the 'LEFT VENTRICULOGRAPHY' File. I will OVERWRITE your data with mine.

> 696.7 MITRAL REGURG ON LV GRAM (including data) Note: You already have the 'MITRAL REGURG ON LV GRAM' File. I will OVERWRITE your data with mine.

> 696.9 COMPLICATION (including data) Note: You already have the 'COMPLICATION' File. I will OVERWRITE your data with mine.

697. ANATOMY (including data) I will OVERWRITE your data with mine.
     1.  REFERRING PHYSICIAN/AGENCY

> Note: You already have the 'REFERRING PHYSICIAN/AGENCY' File.

2.  PROCEDURE/SUBSPECIALTY (including data)

> \*BUT YOU ALREADY HAVE 'PROCEDURE LOCATION' AS FILE \#697.2!

> Shall I write over your PROCEDURE LOCATION File? YES// \<RET\>

> I will MERGE your data with mine.

3.  MEDICINE SCREEN (USER) (including data) Note: You already have the 'MEDICINE SCREEN (USER)' File. I will OVERWRITE your data with mine.

> 697.5 MEDICAL DIAGNOSIS/ICD CODES (including data) Note: You already have the 'MEDICAL DIAGNOSIS/ICD CODES' File. I will OVERWRITE your data with mine.

698. GENERATOR IMPLANT

> Note: You already have the 'GENERATOR IMPLANT' File.

1.  V LEAD IMPLANT

> Note: You already have the 'V LEAD IMPLANT' File.

2.  A LEAD IMPLANT

> Note: You already have the 'A LEAD IMPLANT' File.

3.  PACEMAKER SURVEILLANCE

> Note: You already have the 'PACEMAKER SURVEILLANCE' File.

4.  PACEMAKER EQUIPMENT (including data) Note: You already have the 'PACEMAKER EQUIPMENT' File. I will OVERWRITE your data with mine.

> 698.6 PACEMAKER MANUFACTURER (including data) Note: You already have the 'PACEMAKER MANUFACTURER' File. I will OVERWRITE your data with mine.

> 698.9 NON-MAGNET ECG RHYTHM (including data) Note: You already have the 'NON-MAGNET ECG RHYTHM' File. I will OVERWRITE your data with mine.

699. ENDOSCOPY/CONSULT

> Note: You already have the 'ENDOSCOPY/CONSULT' File.

> 699.48 INSTRUMENT

> Note: You already have the 'INSTRUMENT' File.

> 699.5 GENERALIZED PROCEDURE/CONSULT

> 699.55 GROSS (including data) Note: You already have the 'GROSS' File. I will OVERWRITE your data with mine.

> 699.57 MODIFIER (including data) Note: You already have the 'MODIFIER' File. I will OVERWRITE your data with mine.

6.  DIAG/THERAP INTERVENT (including data) I will OVERWRITE your data with mine.
7.  ENDOSCOPIC DEVICE

> Note: You already have the 'ENDOSCOPIC DEVICE' File.

81. RESULTS (including data) Note: You already have the 'RESULTS' File. I will OVERWRITE your data with mine.
82. CONSULTATION TYPE (including data) Note: You already have the 'CONSULTATION TYPE' File. I will OVERWRITE your data with mine.
83. LOCATION OF PAIN/PNEUMONIAS (including data) Note: You already have the 'LOCATION OF PAIN/PNEUMONIAS' File. I will OVERWRITE your data with mine.
84. DISEASE EVALUATION (including data) Note: You already have the 'DISEASE EVALUATION' File. I will OVERWRITE your data with mine.
85. FOLLOWUP DEVICE/THERAPY (including data) Note: You already have the 'FOLLOWUP DEVICE/THERAPY' File. I will OVERWRITE your data with mine.
86. SURVEILLANCE (including data) Note: You already have the 'SURVEILLANCE' File. I will OVERWRITE your data with mine.

> 699.88 NON-ENDOSCOPIC PROCEDURE (including data) Note: You already have the 'NON-ENDOSCOPIC PROCEDURE' File. I will OVERWRITE your data with mine.

700. PULMONARY FUNCTION TESTS

> Note: You already have the 'PULMONARY FUNCTION TESTS' File.

1.  PFT PREDICTED VALUES (including data) Note: You already have the 'PFT PREDICTED VALUES' File. I will MERGE your data with mine.
2.  PFT FORMULA (including data) Note: You already have the 'PFT FORMULA' File. I will OVERWRITE your data with mine.

> 700.5 MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY

> Note: You already have the 'MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY' File.

701. RHEUMATOLOGY

> Note: You already have the 'RHEUMATOLOGY' File.

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages. Enter a '^' to abort the install.

> DEVICE: HOME// (Enter a device name)

> MEDICINE 2.3

> Install Started for MEDICINE 2.3 :

> Jun 03, 1996@10:58:31

> Installing Routines:

> Jun 03, 1996@10:59:09

> Running Pre-Install Routine: ^MCPRE00

> Removing the 'Select a new patient' item from the 'Medicine

> /Consult Interface Menu' entry in the Protocol file (#101).

> Cleaning up data in the Procedure/Subspecialty file (#697.2).

> Removing the 'M's from the APPLICATION PACKAGES' USE field (#63) of the DRUG file (#50).

> The clean-up of the Medicine entries (M) in the APPLICATION PACKAGES' USE field (#63) in

> the DRUG file (#50) is finished. Entries cleaned-up: 0.

> Cleaning up the ^MCNP global.

> Correcting misspellings in the Indication file (#694.1).

> Cleaning up the data in the ICD Code multiple in the Medical Diagnosis/ICD Codes file (#697.5).

> Searching the medicine files for bad records, (missing zero nodes). If found, these records will be killed.

> Cleaning-up the PFT PREDICTED VALUES file (#700.1). Killing the Medicine data dictionaries.

> Note: At this point a number of blank lines will be printed as the files are deleted.

> Installing Data Dictionaries: 100

> Jun 03, 1996@11:03:04

> Installing Data: ............................................................

> Jun 03, 1996@11:08:30

> Installing PACKAGE COMPONENTS: Installing SECURITY KEY Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE Installing OPTION

> Jun 03, 1996@11:12:21

> Running Post-Install Routine: ^MCPOS00 File: MEDICAL PATIENT (690)

> Cross references for file MEDICAL PATIENT have been deleted.

> Re-indexing file MEDICAL PATIENT... Complete...

> File: MEDICINE PACKAGE PARAMETERS (690.1)

> Cross references for file MEDICINE PACKAGE PARAMETERS have been deleted.

> Re-indexing file MEDICINE PACKAGE PARAMETERS... Complete...

> File: MEDICINE VIEW (690.2)

> Cross references for file MEDICINE VIEW have been deleted.

> Re-indexing file MEDICINE VIEW... Complete...

> File: ASTM (690.5)

> Cross references for file ASTM have been deleted.

> Re-indexing file ASTM................

> Complete...

> File: MCQ POLLING (690.97)

> Cross references for file MCQ POLLING have been deleted.

> Re-indexing file MCQ POLLING...

> Complete...

> File: \*NEW PERSON CONVERSION (690.99)

> Cross references for file \*NEW PERSON CONVERSION have been deleted.

> Re-indexing file \*NEW PERSON CONVERSION...

> Complete...

> File: ECHO (691)

> Cross references for file ECHO have been deleted.

> Re-indexing file ECHO...

> Complete...

> File: CARDIAC CATHETERIZATION (691.1)

> Cross references for file CARDIAC CATHETERIZATION have been deleted.

> Re-indexing file CARDIAC CATHETERIZATION...

> Complete...

> File: ELECTROCARDIOGRAM (EKG) (691.5)

> Cross references for file ELECTROCARDIOGRAM (EKG) have been deleted.

> Re-indexing file ELECTROCARDIOGRAM (EKG)...

> Complete...

> File: HOLTER (691.6)

> Cross references for file HOLTER have been deleted.

> Re-indexing file HOLTER... Complete...

> File: EXERCISE TOLERANCE TEST (691.7)

> Cross references for file EXERCISE TOLERANCE TEST have been deleted.

> Re-indexing file EXERCISE TOLERANCE TEST... Complete...

> File: ELECTROPHYSIOLOGY (EP) (691.8)

> Cross references for file ELECTROPHYSIOLOGY (EP) have been deleted.

> Re-indexing file ELECTROPHYSIOLOGY (EP)... Complete...

> File: ATRIAL STUDY (691.9)

> Cross references for file ATRIAL STUDY have been deleted.

> Re-indexing file ATRIAL STUDY... Complete...

> File: VENTRICULAR STUDY (692)

> Cross references for file VENTRICULAR STUDY have been deleted.

> Re-indexing file VENTRICULAR STUDY... Complete...

> File: MEDICAL DESCRIPTION (693)

> Cross references for file MEDICAL DESCRIPTION have been deleted.

> Re-indexing file MEDICAL DESCRIPTION.....

> Complete...

> File: INTERPRETATION (693.2)

> Cross references for file INTERPRETATION have been deleted.

> Re-indexing file INTERPRETATION........

> Complete...

> File: ECG INTERPRETATION (693.3)

> Cross references for file ECG INTERPRETATION have been deleted.

> Re-indexing file ECG INTERPRETATION.....

> Complete...

> File: RECORDING SITE (693.5)

> Cross references for file RECORDING SITE have been deleted.

> Re-indexing file RECORDING SITE...

> Complete...

> File: EP INTERVENTION (693.6)

> Cross references for file EP INTERVENTION have been deleted.

> Re-indexing file EP INTERVENTION...

> Complete...

> File: HEMATOLOGY (694)

> Cross references for file HEMATOLOGY have been deleted.

> Re-indexing file HEMATOLOGY... Complete...

> File: INDICATION (694.1)

> Cross references for file INDICATION have been deleted.

> Re-indexing file INDICATION... Complete...

> File: CARDIAC SURGERY RISK ASSESSMENT (694.5)

> Cross references for file CARDIAC SURGERY RISK ASSESSMENT have been deleted.

> Re-indexing file CARDIAC SURGERY RISK ASSESSMENT...

> Complete...

> File: PROCEDURE TERM (694.8)

> Cross references for file PROCEDURE TERM have been deleted.

> Re-indexing file PROCEDURE TERM... Complete...

> File: MEDICATION (695)

> Cross references for file MEDICATION have been deleted.

> Re-indexing file MEDICATION... Complete...

> File: REGIONAL WALL MOTION (695.1)

> Cross references for file REGIONAL WALL MOTION have been deleted.

> Re-indexing file REGIONAL WALL MOTION... Complete...

> File: CATH PROCEDURE (695.3)

> Cross references for file CATH PROCEDURE have been deleted.

> Re-indexing file CATH PROCEDURE... Complete...

> File: PAST HISTORY AND RISK FACTOR (695.4)

> Cross references for file PAST HISTORY AND RISK FACTOR have been deleted.

> Re-indexing file PAST HISTORY AND RISK FACTOR... Complete...

> File: SYMPTOM (695.5)

> Cross references for file SYMPTOM have been deleted.

> Re-indexing file SYMPTOM....

> Complete...

> File: HEART CATHETER (695.6)

> Cross references for file HEART CATHETER have been deleted.

> Re-indexing file HEART CATHETER...

> Complete...

> File: REASON (MEDICINE) (695.8)

> Cross references for file REASON (MEDICINE) have been deleted.

> Re-indexing file REASON (MEDICINE)... Complete...

> File: NORMALITY OF CORONARY VESSEL (695.9)

> Cross references for file NORMALITY OF CORONARY VESSEL have been deleted.

> Re-indexing file NORMALITY OF CORONARY VESSEL... Complete...

> File: SEGMENT OF CORONARY ARTERIES (696)

> Cross references for file SEGMENT OF CORONARY ARTERIES have been deleted.

> Re-indexing file SEGMENT OF CORONARY ARTERIES... Complete...

> File: PERCENTAGE LESION (696.1)

> Cross references for file PERCENTAGE LESION have been deleted.

> Re-indexing file PERCENTAGE LESION... Complete...

> File: LESION MORPHOLOGY (696.2)

> Cross references for file LESION MORPHOLOGY have been deleted.

> Re-indexing file LESION MORPHOLOGY... Complete...

> File: MORPHOLOGY OF DISTAL VESSEL (696.3)

> Cross references for file MORPHOLOGY OF DISTAL VESSEL have been deleted.

> Re-indexing file MORPHOLOGY OF DISTAL VESSEL... Complete...

> File: BYPASS GRAFT SEGMENT (696.4)

> Cross references for file BYPASS GRAFT SEGMENT have been deleted.

> Re-indexing file BYPASS GRAFT SEGMENT... Complete...

> File: LEFT VENTRICULOGRAPHY (696.5)

> Cross references for file LEFT VENTRICULOGRAPHY have been deleted.

> Re-indexing file LEFT VENTRICULOGRAPHY... Complete...

> File: MITRAL REGURG ON LV GRAM (696.7)

> Cross references for file MITRAL REGURG ON LV GRAM have been deleted.

> Re-indexing file MITRAL REGURG ON LV GRAM... Complete...

> File: COMPLICATION (696.9)

> Cross references for file COMPLICATION have been deleted.

> Re-indexing file COMPLICATION... Complete...

> File: ANATOMY (697)

> Cross references for file ANATOMY have been deleted.

> Re-indexing file ANATOMY....

> Complete...

> File: REFERRING PHYSICIAN/AGENCY (697.1)

> Cross references for file REFERRING PHYSICIAN/AGENCY have been deleted.

> Re-indexing file REFERRING PHYSICIAN/AGENCY...

> Complete...

> File: PROCEDURE/SUBSPECIALTY (697.2)

> Cross references for file PROCEDURE/SUBSPECIALTY have been deleted.

> Re-indexing file PROCEDURE/SUBSPECIALTY...

> Complete...

> File: MEDICINE SCREEN (USER) (697.3)

> Cross references for file MEDICINE SCREEN (USER) have been deleted.

> Re-indexing file MEDICINE SCREEN (USER)......

> Complete...

> File: MEDICAL DIAGNOSIS/ICD CODES (697.5)

> Cross references for file MEDICAL DIAGNOSIS/ICD CODES have been deleted.

> Re-indexing file MEDICAL DIAGNOSIS/ICD CODES............

> Complete...

> File: GENERATOR IMPLANT (698)

> Cross references for file GENERATOR IMPLANT have been deleted.

> Re-indexing file GENERATOR IMPLANT...

> Complete...

> File: V LEAD IMPLANT (698.1)

> Cross references for file V LEAD IMPLANT have been deleted.

> Re-indexing file V LEAD IMPLANT...

> Complete...

> File: A LEAD IMPLANT (698.2)

> Cross references for file A LEAD IMPLANT have been deleted.

> Re-indexing file A LEAD IMPLANT...

> Complete...

> File: PACEMAKER SURVEILLANCE (698.3)

> Cross references for file PACEMAKER SURVEILLANCE have been deleted.

> Re-indexing file PACEMAKER SURVEILLANCE...

> Complete...

> File: PACEMAKER EQUIPMENT (698.4)

> Cross references for file PACEMAKER EQUIPMENT have been deleted.

> Re-indexing file PACEMAKER EQUIPMENT.........................

> Complete...

> File: PACEMAKER MANUFACTURER (698.6)

> Cross references for file PACEMAKER MANUFACTURER have been deleted.

> Re-indexing file PACEMAKER MANUFACTURER... Complete...

> File: NON-MAGNET ECG RHYTHM (698.9)

> Cross references for file NON-MAGNET ECG RHYTHM have been deleted.

> Re-indexing file NON-MAGNET ECG RHYTHM... Complete...

> File: ENDOSCOPY/CONSULT (699)

> Cross references for file ENDOSCOPY/CONSULT have been deleted.

> Re-indexing file ENDOSCOPY/CONSULT... Complete...

> File: INSTRUMENT (699.48)

> Cross references for file INSTRUMENT have been deleted.

> Re-indexing file INSTRUMENT... Complete...

> File: GENERALIZED PROCEDURE/CONSULT (699.5)

> Cross references for file GENERALIZED PROCEDURE/CONSULT have been deleted.

> Re-indexing file GENERALIZED PROCEDURE/CONSULT... Complete...

> File: GROSS (699.55)

> Cross references for file GROSS have been deleted.

> Re-indexing file GROSS... Complete...

> File: MODIFIER (699.57)

> Cross references for file MODIFIER have been deleted.

> Re-indexing file MODIFIER....

> Complete...

> File: DIAG/THERAP INTERVENT (699.6)

> Cross references for file DIAG/THERAP INTERVENT have been deleted.

> Re-indexing file DIAG/THERAP INTERVENT....

> Complete...

> File: ENDOSCOPIC DEVICE (699.7)

> Cross references for file ENDOSCOPIC DEVICE have been deleted.

> Re-indexing file ENDOSCOPIC DEVICE...

> Complete...

> File: RESULTS (699.81)

> Cross references for file RESULTS have been deleted.

> Re-indexing file RESULTS...

> Complete...

> File: CONSULTATION TYPE (699.82)

> Cross references for file CONSULTATION TYPE have been deleted.

> Re-indexing file CONSULTATION TYPE... Complete...

> File: LOCATION OF PAIN/PNEUMONIAS (699.83)

> Cross references for file LOCATION OF PAIN/PNEUMONIAS have been deleted.

> Re-indexing file LOCATION OF PAIN/PNEUMONIAS... Complete...

> File: DISEASE EVALUATION (699.84)

> Cross references for file DISEASE EVALUATION have been deleted.

> Re-indexing file DISEASE EVALUATION... Complete...

> File: FOLLOWUP DEVICE/THERAPY (699.85)

> Cross references for file FOLLOWUP DEVICE/THERAPY have been deleted.

> Re-indexing file FOLLOWUP DEVICE/THERAPY... Complete...

> File: SURVEILLANCE (699.86)

> Cross references for file SURVEILLANCE have been deleted.

> Re-indexing file SURVEILLANCE... Complete...

> File: NON-ENDOSCOPIC PROCEDURE (699.88)

> Cross references for file NON-ENDOSCOPIC PROCEDURE have been deleted.

> Re-indexing file NON-ENDOSCOPIC PROCEDURE... Complete...

> File: PULMONARY FUNCTION TESTS (700)

> Cross references for file PULMONARY FUNCTION TESTS have been deleted.

> Re-indexing file PULMONARY FUNCTION TESTS... Complete...

> File: PFT PREDICTED VALUES (700.1)

> Cross references for file PFT PREDICTED VALUES have been deleted.

> Re-indexing file PFT PREDICTED VALUES... Complete...

> File: PFT FORMULA (700.2)

> Cross references for file PFT FORMULA have been deleted.

> Re-indexing file PFT FORMULA... Complete...

> File: MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY (700.5)

> Cross references for file MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY have been

> .

> Re-indexing file MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY...

> Complete...

> File: RHEUMATOLOGY (701)

> Cross references for file RHEUMATOLOGY have been deleted.

> Re-indexing file RHEUMATOLOGY... Complete...

> Converting Provider file (#6) pointers to New Person file (#200) pointers.

> Moving instrument from flat field into multiple in the Endoscopy/Consult file (#699).

> Moving the Consult data from the Endoscopy/Consult file (#699) to the Generalized Procedure/Consult file (#699.5).

> Creating the MC MESSAGING SERVER mail group.

> Checking the sub-DD numbers in the Generalized Procedure/Consult file (#699.5).

> Deleting pointers to Lab files.

> Adding the cardiology code to the Medical Package Use multiple in the Medication file (#695)

> Moving Micro Description Remarks from a free text field to word processing field in the Hematology file (#694).

> Update the pointers from the Procedure Term file (#694.8) to the Procedure/Subspecialty file (#697.2).

> Update the pointers from the Medicine View file (#690.2) to the Procedure/Subspecialty file (#697.2).

> Update the pointers from the Medicine View file (#690.2) to the ASTM file (#690.5).

> Updating Medicine package file level access security. Restoring locally defined procedures to the

> Medicine View file (#690.2) Updating Routine file...

> The following Routines were created during this install:

> MCOPRG MCOPRG1 MCOPRG2 MCAROC4 MCAROC41 MCAROC3 MCAROC31 MCAROC2 MCAROC21 MCAROC22 MCAROC1 MCAROT

> MCAROT1 MCAROK MCAROK1 MCAROEP MCAROEP1 MCAROV MCAROV1 MCAROH1 MCAROH11 MCAROH2 MCAROGR MCAROGI MCAROGN MCAROG MCAROG1 MCAROHD MCAROHB MCAROHF MCAROPG MCAROPG1 MCAROPA MCAROPA1 MCAROPV MCAROPV1 MCAROPS MCAROPS1 MCAROE1 MCAROS0 MCAROS1 MCAROS2 MCAROS3 MCAROPF MCAROS4 MCARORB MCARORH MCARORH1 MCARORH2 MCAROGA MCAROGA1 MCAROP MCAROPE MCAROPE1 MCARORQ MCARORD MCARORN MCAROE2 MCARORP MCARORP1 MCARORL MCARORL1 MCARORL2 MCARORA MCARORE MCARORE1 MCAROGM MCARORF MCARORF1 MCARORF2 MCARORF3 MCAROGC

> MCAROGE MCOBC1 MCOBC11 MCOBE1 MCOBK MCOBEP MCOBH1 MCOBT MCOBGC MCOBGA MCOBGA1 MCOBGN MCOBPE MCOBPFT MCOBHEM MCOBPG MCOBPA MCOBPV MCOBPS MCOBPS1 MCOBGEN MCOBRH MCOBRH1 MCOBRHA MCOBRHA1 MCOBPF MCAROAT MCAROAT1 MCAROAT2

> Updating KIDS files... MEDICINE 2.3 Installed.

> Jun 03, 1996@11:15:18

> Not a production UCI

> NO Install Message sent

> September 1996 Medicine V. 2.3 55

> Install Completed

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global Select Installation Option:

# Installation Over Version 2.2 (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### D ^XUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: EVE Systems Manager Menu

> Core Applications ... Device Management ...

> FM VA FileMan ...

> Manage Mailman ... Menu Management ... Programmer Options ...

> Operations Management ... Spool Management ...

> System Security ... Taskman Management ... User Management ...

> Application Utilities ... Capacity Management ...

> MailMan Menu ...

> Select Systems Manager Menu Option: Programmer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options Option: Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global

> September 1996 Medicine V. 2.3 57

> Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Load a Distribution Enter a Host File: MC2_3.KID

> KIDS Distribution saved on Jun 03, 1996@10:48:08 Comment: Medicine 2.3

> This Distribution contains Transport Globals for the following Package(s): MEDICINE 2.3

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 2.2.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Use MEDICINE 2.3 to install this Distribution.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: MEDICINE 2.3 Loaded from Distribution 6/4/96@12:51:16

> =\> Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> This Distribution was loaded on Jun 04, 1996@12:51:16 with header of Medicine 2.3 ;Created on Jun 03, 1996@10:48:08

> It consisted of the following Install(s):

> MEDICINE 2.3

> Will first run the Environment Check Routine, MCENV00

> Checking for previous version of the medicine package. Found Medicine package version 2.2.

> Checking for minimum required package versions. All required files found.

> Checking for patch DI\*21\*25. Patch found.

> Install Questions for MEDICINE 2.3

690. MEDICAL PATIENT

> Note: You already have the 'MEDICAL PATIENT' File.

1.  MEDICINE PACKAGE PARAMETERS

> Note: You already have the 'MEDICINE PACKAGE PARAMETERS' File.

2.  MEDICINE VIEW (including data) Note: You already have the 'MEDICINE VIEW' File. I will OVERWRITE your data with mine.

> 690.5 ASTM (including data) Note: You already have the 'ASTM' File. I will OVERWRITE your data with mine.

> 690.97 MCQ POLLING

> 690.99 \*NEW PERSON CONVERSION 691 ECHO

> Note: You already have the 'ECHO' File.

> 691.1 CARDIAC CATHETERIZATION

> Note: You already have the 'CARDIAC CATHETERIZATION' File.

5.  ELECTROCARDIOGRAM (EKG)

> Note: You already have the 'ELECTROCARDIOGRAM (EKG)' File.

6.  HOLTER

> Note: You already have the 'HOLTER' File.

7.  EXERCISE TOLERANCE TEST

> Note: You already have the 'EXERCISE TOLERANCE TEST' File.

8.  ELECTROPHYSIOLOGY (EP)

> Note: You already have the 'ELECTROPHYSIOLOGY (EP)' File.

9.  ATRIAL STUDY

> Note: You already have the 'ATRIAL STUDY' File.

692. VENTRICULAR STUDY

> Note: You already have the 'VENTRICULAR STUDY' File.

693. MEDICAL DESCRIPTION (including data) Note: You already have the 'MEDICAL DESCRIPTION' File. I will OVERWRITE your data with mine.
     2.  INTERPRETATION (including data) Note: You already have the 'INTERPRETATION' File. I will OVERWRITE your data with mine.
     3.  ECG INTERPRETATION (including data) Note: You already have the 'ECG INTERPRETATION' File. I will OVERWRITE your data with mine.
     5.  RECORDING SITE (including data) Note: You already have the 'RECORDING SITE' File. I will OVERWRITE your data with mine.
     6.  EP INTERVENTION

> Note: You already have the 'EP INTERVENTION' File.

694. HEMATOLOGY

> Note: You already have the 'HEMATOLOGY' File.

1.  INDICATION (including data) Note: You already have the 'INDICATION' File. I will OVERWRITE your data with mine.

> 694.5 CARDIAC SURGERY RISK ASSESSMENT

> Note: You already have the 'CARDIAC SURGERY RISK ASSESSMENT' File.

> 694.8 PROCEDURE TERM (including data) Note: You already have the 'PROCEDURE TERM' File. I will OVERWRITE your data with mine.

695. MEDICATION

> Note: You already have the 'MEDICATION' File.

1.  REGIONAL WALL MOTION (including data) Note: You already have the 'REGIONAL WALL MOTION' File. I will OVERWRITE your data with mine.
3.  CATH PROCEDURE (including data) Note: You already have the 'CATH PROCEDURE' File. I will OVERWRITE your data with mine.
4.  PAST HISTORY AND RISK FACTOR (including data) Note: You already have the 'PAST HISTORY AND RISK FACTOR' File. I will OVERWRITE your data with mine.
5.  SYMPTOM (including data) Note: You already have the 'SYMPTOM' File. I will OVERWRITE your data with mine.
6.  HEART CATHETER (including data) Note: You already have the 'HEART CATHETER' File. I will OVERWRITE your data with mine.
8.  REASON (MEDICINE) (including data) Note: You already have the 'REASON (MEDICINE)' File. I will OVERWRITE your data with mine.
9.  NORMALITY OF CORONARY VESSEL (including data) Note: You already have the 'NORMALITY OF CORONARY VESSEL' File. I will OVERWRITE your data with mine.
696. SEGMENT OF CORONARY ARTERIES (including data) Note: You already have the 'SEGMENT OF CORONARY ARTERIES' File. I will OVERWRITE your data with mine.
     1.  PERCENTAGE LESION (including data) Note: You already have the 'PERCENTAGE LESION' File. I will OVERWRITE your data with mine.
     2.  LESION MORPHOLOGY (including data) Note: You already have the 'LESION MORPHOLOGY' File. I will OVERWRITE your data with mine.
     3.  MORPHOLOGY OF DISTAL VESSEL (including data) Note: You already have the 'MORPHOLOGY OF DISTAL VESSEL' File. I will OVERWRITE your data with mine.
     4.  BYPASS GRAFT SEGMENT (including data) Note: You already have the 'BYPASS GRAFT SEGMENT' File.

> I will OVERWRITE your data with mine.

5.  LEFT VENTRICULOGRAPHY (including data) Note: You already have the 'LEFT VENTRICULOGRAPHY' File. I will OVERWRITE your data with mine.

> 696.7 MITRAL REGURG ON LV GRAM (including data) Note: You already have the 'MITRAL REGURG ON LV GRAM' File. I will OVERWRITE your data with mine.

> 696.9 COMPLICATION (including data) Note: You already have the 'COMPLICATION' File. I will OVERWRITE your data with mine.

697. ANATOMY (including data) Note: You already have the 'ANATOMY' File. I will OVERWRITE your data with mine.
     1.  REFERRING PHYSICIAN/AGENCY

> Note: You already have the 'REFERRING PHYSICIAN/AGENCY' File.

2.  PROCEDURE/SUBSPECIALTY (including data) Note: You already have the 'PROCEDURE/SUBSPECIALTY' File. I will MERGE your data with mine.
3.  MEDICINE SCREEN (USER) (including data) Note: You already have the 'MEDICINE SCREEN (USER)' File. I will OVERWRITE your data with mine.

> 697.5 MEDICAL DIAGNOSIS/ICD CODES (including data) Note: You already have the 'MEDICAL DIAGNOSIS/ICD CODES' File. I will OVERWRITE your data with mine.

698. GENERATOR IMPLANT

> Note: You already have the 'GENERATOR IMPLANT' File.

1.  V LEAD IMPLANT

> Note: You already have the 'V LEAD IMPLANT' File.

2.  A LEAD IMPLANT

> Note: You already have the 'A LEAD IMPLANT' File.

3.  PACEMAKER SURVEILLANCE

> Note: You already have the 'PACEMAKER SURVEILLANCE' File.

4.  PACEMAKER EQUIPMENT (including data) Note: You already have the 'PACEMAKER EQUIPMENT' File.

> 62 Medicine V. 2.3 September 1996

> I will OVERWRITE your data with mine.

> 698.6 PACEMAKER MANUFACTURER (including data) Note: You already have the 'PACEMAKER MANUFACTURER' File. I will OVERWRITE your data with mine.

> 698.9 NON-MAGNET ECG RHYTHM (including data) Note: You already have the 'NON-MAGNET ECG RHYTHM' File. I will OVERWRITE your data with mine.

699. ENDOSCOPY/CONSULT

> Note: You already have the 'ENDOSCOPY/CONSULT' File.

> 699.48 INSTRUMENT

> Note: You already have the 'INSTRUMENT' File.

> 699.5 GENERALIZED PROCEDURE/CONSULT

> Note: You already have the 'GENERALIZED PROCEDURE/CONSULT' File.

> 699.55 GROSS (including data) Note: You already have the 'GROSS' File. I will OVERWRITE your data with mine.

> 699.57 MODIFIER (including data) Note: You already have the 'MODIFIER' File. I will OVERWRITE your data with mine.

6.  DIAG/THERAP INTERVENT (including data) Note: You already have the 'DIAG/THERAP INTERVENT' File. I will OVERWRITE your data with mine.
7.  ENDOSCOPIC DEVICE

> Note: You already have the 'ENDOSCOPIC DEVICE' File.

81. RESULTS (including data) Note: You already have the 'RESULTS' File. I will OVERWRITE your data with mine.
82. CONSULTATION TYPE (including data) Note: You already have the 'CONSULTATION TYPE' File. I will OVERWRITE your data with mine.
83. LOCATION OF PAIN/PNEUMONIAS (including data) Note: You already have the 'LOCATION OF PAIN/PNEUMONIAS' File. I will OVERWRITE your data with mine.
84. DISEASE EVALUATION (including data)

> Note: You already have the 'DISEASE EVALUATION' File. I will OVERWRITE your data with mine.

85. FOLLOWUP DEVICE/THERAPY (including data) Note: You already have the 'FOLLOWUP DEVICE/THERAPY' File. I will OVERWRITE your data with mine.
86. SURVEILLANCE (including data) Note: You already have the 'SURVEILLANCE' File. I will OVERWRITE your data with mine.

> 699.88 NON-ENDOSCOPIC PROCEDURE (including data) Note: You already have the 'NON-ENDOSCOPIC PROCEDURE' File. I will OVERWRITE your data with mine.

700. PULMONARY FUNCTION TESTS

> Note: You already have the 'PULMONARY FUNCTION TESTS' File.

1.  PFT PREDICTED VALUES (including data) Note: You already have the 'PFT PREDICTED VALUES' File. I will MERGE your data with mine.
2.  PFT FORMULA (including data) Note: You already have the 'PFT FORMULA' File. I will OVERWRITE your data with mine.

> 700.5 MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY

> Note: You already have the 'MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY' File.

701. RHEUMATOLOGY

> Note: You already have the 'RHEUMATOLOGY' File.

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages. Enter a '^' to abort the install.

> DEVICE: HOME// (Enter a Device Name)

> 64 Medicine V. 2.3 February 1997

> MEDICINE 2.3

> Install Started for MEDICINE 2.3 :

> Jun 04, 1996@12:53:23

> Installing Routines:

> Jun 04, 1996@12:53:50

> Running Pre-Install Routine: ^MCPRE00

> Removing the 'Select a new patient' item from the 'Medicine

> /Consult Interface Menu' entry in the Protocol file (#101).

> Cleaning up data in the Procedure/Subspecialty file (#697.2).

> Removing the 'M's from the APPLICATION PACKAGES' USE field (#63) of the DRUG file (#50).

> The clean-up of the Medicine entries (M) in the APPLICATION PACKAGES' USE field (#63) in

> the DRUG file (#50) is finished. Entries cleaned-up: 0.

> Cleaning up the ^MCNP global.

> Correcting misspellings in the Indication file (#694.1).

> Cleaning up the data in the ICD Code multiple in the Medical Diagnosis/ICD Codes file (#697.5).

> Searching the medicine files for bad records, (missing zero nodes). If found, these records will be killed.

> Cleaning-up the PFT PREDICTED VALUES file (#700.1). Killing the Medicine data dictionaries.

> Note: At this point a number of blank lines will be printed as the files are deleted.

> Installing Data Dictionaries:

> Jun 04, 1996@12:58:11

> Installing Data: ............................................................

> Jun 04, 1996@13:06:52

> Installing PACKAGE COMPONENTS: Installing SECURITY KEY Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE Installing OPTION

> Jun 04, 1996@13:10:09

> Running Post-Install Routine: ^MCPOS00 File: MEDICAL PATIENT (690)

> Cross references for file MEDICAL PATIENT have been deleted.

> Re-indexing file MEDICAL PATIENT... Complete...

> File: MEDICINE PACKAGE PARAMETERS (690.1)

> Cross references for file MEDICINE PACKAGE PARAMETERS have been deleted.

> Re-indexing file MEDICINE PACKAGE PARAMETERS... Complete...

> File: MEDICINE VIEW (690.2)

> Cross references for file MEDICINE VIEW have been deleted.

> Re-indexing file MEDICINE VIEW... Complete...

> File: ASTM (690.5)

> Cross references for file ASTM have been deleted.

> Re-indexing file ASTM................

> Complete...

> File: MCQ POLLING (690.97)

> Cross references for file MCQ POLLING have been deleted.

> Re-indexing file MCQ POLLING...

> Complete...

> File: \*NEW PERSON CONVERSION (690.99)

> Cross references for file \*NEW PERSON CONVERSION have been deleted.

> Re-indexing file \*NEW PERSON CONVERSION...

> Complete...

> File: ECHO (691)

> Cross references for file ECHO have been deleted.

> Re-indexing file ECHO...

> Complete...

> File: CARDIAC CATHETERIZATION (691.1)

> Cross references for file CARDIAC CATHETERIZATION have been deleted.

> Re-indexing file CARDIAC CATHETERIZATION...

> Complete...

> File: ELECTROCARDIOGRAM (EKG) (691.5)

> Cross references for file ELECTROCARDIOGRAM (EKG) have been deleted.

> Re-indexing file ELECTROCARDIOGRAM (EKG)...

> Complete...

> File: HOLTER (691.6)

> Cross references for file HOLTER have been deleted.

> Re-indexing file HOLTER...

> Complete...

> File: EXERCISE TOLERANCE TEST (691.7)

> Cross references for file EXERCISE TOLERANCE TEST have been deleted.

> Re-indexing file EXERCISE TOLERANCE TEST... Complete...

> File: ELECTROPHYSIOLOGY (EP) (691.8)

> Cross references for file ELECTROPHYSIOLOGY (EP) have been deleted.

> Re-indexing file ELECTROPHYSIOLOGY (EP)... Complete...

> File: ATRIAL STUDY (691.9)

> Cross references for file ATRIAL STUDY have been deleted.

> Re-indexing file ATRIAL STUDY... Complete...

> File: VENTRICULAR STUDY (692)

> Cross references for file VENTRICULAR STUDY have been deleted.

> Re-indexing file VENTRICULAR STUDY... Complete...

> File: MEDICAL DESCRIPTION (693)

> Cross references for file MEDICAL DESCRIPTION have been deleted.

> Re-indexing file MEDICAL DESCRIPTION.....

> Complete...

> File: INTERPRETATION (693.2)

> Cross references for file INTERPRETATION have been deleted.

> Re-indexing file INTERPRETATION........

> Complete...

> File: ECG INTERPRETATION (693.3)

> Cross references for file ECG INTERPRETATION have been deleted.

> Re-indexing file ECG INTERPRETATION.....

> Complete...

> File: RECORDING SITE (693.5)

> Cross references for file RECORDING SITE have been deleted.

> Re-indexing file RECORDING SITE...

> Complete...

> File: EP INTERVENTION (693.6)

> Cross references for file EP INTERVENTION have been deleted.

> Re-indexing file EP INTERVENTION...

> Complete...

> File: HEMATOLOGY (694)

> Cross references for file HEMATOLOGY have been deleted.

> Re-indexing file HEMATOLOGY...

> Complete...

> File: INDICATION (694.1)

> Cross references for file INDICATION have been deleted.

> Re-indexing file INDICATION... Complete...

> File: CARDIAC SURGERY RISK ASSESSMENT (694.5)

> Cross references for file CARDIAC SURGERY RISK ASSESSMENT have been deleted.

> Re-indexing file CARDIAC SURGERY RISK ASSESSMENT...

> Complete...

> File: PROCEDURE TERM (694.8)

> Cross references for file PROCEDURE TERM have been deleted.

> Re-indexing file PROCEDURE TERM... Complete...

> File: MEDICATION (695)

> Cross references for file MEDICATION have been deleted.

> Re-indexing file MEDICATION... Complete...

> File: REGIONAL WALL MOTION (695.1)

> Cross references for file REGIONAL WALL MOTION have been deleted.

> Re-indexing file REGIONAL WALL MOTION... Complete...

> File: CATH PROCEDURE (695.3)

> Cross references for file CATH PROCEDURE have been deleted.

> Re-indexing file CATH PROCEDURE... Complete...

> File: PAST HISTORY AND RISK FACTOR (695.4)

> Cross references for file PAST HISTORY AND RISK FACTOR have been deleted.

> Re-indexing file PAST HISTORY AND RISK FACTOR... Complete...

> File: SYMPTOM (695.5)

> Cross references for file SYMPTOM have been deleted.

> Re-indexing file SYMPTOM....

> Complete...

> File: HEART CATHETER (695.6)

> Cross references for file HEART CATHETER have been deleted.

> Re-indexing file HEART CATHETER...

> Complete...

> File: REASON (MEDICINE) (695.8)

> Cross references for file REASON (MEDICINE) have been deleted.

> Re-indexing file REASON (MEDICINE)...

> Complete...

> File: NORMALITY OF CORONARY VESSEL (695.9)

> Cross references for file NORMALITY OF CORONARY VESSEL have been deleted.

> Re-indexing file NORMALITY OF CORONARY VESSEL... Complete...

> File: SEGMENT OF CORONARY ARTERIES (696)

> Cross references for file SEGMENT OF CORONARY ARTERIES have been deleted.

> Re-indexing file SEGMENT OF CORONARY ARTERIES... Complete...

> File: PERCENTAGE LESION (696.1)

> Cross references for file PERCENTAGE LESION have been deleted.

> Re-indexing file PERCENTAGE LESION... Complete...

> File: LESION MORPHOLOGY (696.2)

> Cross references for file LESION MORPHOLOGY have been deleted.

> Re-indexing file LESION MORPHOLOGY... Complete...

> File: MORPHOLOGY OF DISTAL VESSEL (696.3)

> Cross references for file MORPHOLOGY OF DISTAL VESSEL have been deleted.

> Re-indexing file MORPHOLOGY OF DISTAL VESSEL... Complete...

> File: BYPASS GRAFT SEGMENT (696.4)

> Cross references for file BYPASS GRAFT SEGMENT have been deleted.

> Re-indexing file BYPASS GRAFT SEGMENT... Complete...

> File: LEFT VENTRICULOGRAPHY (696.5)

> Cross references for file LEFT VENTRICULOGRAPHY have been deleted.

> Re-indexing file LEFT VENTRICULOGRAPHY... Complete...

> File: MITRAL REGURG ON LV GRAM (696.7)

> Cross references for file MITRAL REGURG ON LV GRAM have been deleted.

> Re-indexing file MITRAL REGURG ON LV GRAM... Complete...

> File: COMPLICATION (696.9)

> Cross references for file COMPLICATION have been deleted.

> Re-indexing file COMPLICATION... Complete...

> File: ANATOMY (697)

> Cross references for file ANATOMY have been deleted.

> Re-indexing file ANATOMY....

> Complete...

> File: REFERRING PHYSICIAN/AGENCY (697.1)

> Cross references for file REFERRING PHYSICIAN/AGENCY have been deleted.

> Re-indexing file REFERRING PHYSICIAN/AGENCY... Complete...

> File: PROCEDURE/SUBSPECIALTY (697.2)

> Cross references for file PROCEDURE/SUBSPECIALTY have been deleted.

> Re-indexing file PROCEDURE/SUBSPECIALTY... Complete...

> File: MEDICINE SCREEN (USER) (697.3)

> Cross references for file MEDICINE SCREEN (USER) have been deleted.

> Re-indexing file MEDICINE SCREEN (USER)......

> Complete...

> File: MEDICAL DIAGNOSIS/ICD CODES (697.5)

> Cross references for file MEDICAL DIAGNOSIS/ICD CODES have been deleted.

> Re-indexing file MEDICAL DIAGNOSIS/ICD CODES............

> Complete...

> File: GENERATOR IMPLANT (698)

> Cross references for file GENERATOR IMPLANT have been deleted.

> Re-indexing file GENERATOR IMPLANT...

> Complete...

> File: V LEAD IMPLANT (698.1)

> Cross references for file V LEAD IMPLANT have been deleted.

> Re-indexing file V LEAD IMPLANT...

> Complete...

> File: A LEAD IMPLANT (698.2)

> Cross references for file A LEAD IMPLANT have been deleted.

> Re-indexing file A LEAD IMPLANT...

> Complete...

> File: PACEMAKER SURVEILLANCE (698.3)

> Cross references for file PACEMAKER SURVEILLANCE have been deleted.

> Re-indexing file PACEMAKER SURVEILLANCE...

> Complete...

> File: PACEMAKER EQUIPMENT (698.4)

> Cross references for file PACEMAKER EQUIPMENT have been deleted.

> Re-indexing file PACEMAKER EQUIPMENT.........................

> Complete...

> File: PACEMAKER MANUFACTURER (698.6)

> Cross references for file PACEMAKER MANUFACTURER have been deleted.

> Re-indexing file PACEMAKER MANUFACTURER...

> Complete...

> File: NON-MAGNET ECG RHYTHM (698.9)

> Cross references for file NON-MAGNET ECG RHYTHM have been deleted.

> Re-indexing file NON-MAGNET ECG RHYTHM... Complete...

> File: ENDOSCOPY/CONSULT (699)

> Cross references for file ENDOSCOPY/CONSULT have been deleted.

> Re-indexing file ENDOSCOPY/CONSULT... Complete...

> File: INSTRUMENT (699.48)

> Cross references for file INSTRUMENT have been deleted.

> Re-indexing file INSTRUMENT... Complete...

> File: GENERALIZED PROCEDURE/CONSULT (699.5)

> Cross references for file GENERALIZED PROCEDURE/CONSULT have been deleted.

> Re-indexing file GENERALIZED PROCEDURE/CONSULT... Complete...

> File: GROSS (699.55)

> Cross references for file GROSS have been deleted.

> Re-indexing file GROSS... Complete...

> File: MODIFIER (699.57)

> Cross references for file MODIFIER have been deleted.

> Re-indexing file MODIFIER....

> Complete...

> File: DIAG/THERAP INTERVENT (699.6)

> Cross references for file DIAG/THERAP INTERVENT have been deleted.

> Re-indexing file DIAG/THERAP INTERVENT....

> Complete...

> File: ENDOSCOPIC DEVICE (699.7)

> Cross references for file ENDOSCOPIC DEVICE have been deleted.

> Re-indexing file ENDOSCOPIC DEVICE...

> Complete...

> File: RESULTS (699.81)

> Cross references for file RESULTS have been deleted.

> Re-indexing file RESULTS...

> Complete...

> File: CONSULTATION TYPE (699.82)

> Cross references for file CONSULTATION TYPE have been deleted.

> Re-indexing file CONSULTATION TYPE...

> Complete...

> File: LOCATION OF PAIN/PNEUMONIAS (699.83)

> Cross references for file LOCATION OF PAIN/PNEUMONIAS have been deleted.

> Re-indexing file LOCATION OF PAIN/PNEUMONIAS... Complete...

> File: DISEASE EVALUATION (699.84)

> Cross references for file DISEASE EVALUATION have been deleted.

> Re-indexing file DISEASE EVALUATION... Complete...

> File: FOLLOWUP DEVICE/THERAPY (699.85)

> Cross references for file FOLLOWUP DEVICE/THERAPY have been deleted.

> Re-indexing file FOLLOWUP DEVICE/THERAPY... Complete...

> File: SURVEILLANCE (699.86)

> Cross references for file SURVEILLANCE have been deleted.

> Re-indexing file SURVEILLANCE... Complete...

> File: NON-ENDOSCOPIC PROCEDURE (699.88)

> Cross references for file NON-ENDOSCOPIC PROCEDURE have been deleted.

> Re-indexing file NON-ENDOSCOPIC PROCEDURE... Complete...

> File: PULMONARY FUNCTION TESTS (700)

> Cross references for file PULMONARY FUNCTION TESTS have been deleted.

> Re-indexing file PULMONARY FUNCTION TESTS... Complete...

> File: PFT PREDICTED VALUES (700.1)

> Cross references for file PFT PREDICTED VALUES have been deleted.

> Re-indexing file PFT PREDICTED VALUES... Complete...

> File: PFT FORMULA (700.2)

> Cross references for file PFT FORMULA have been deleted.

> Re-indexing file PFT FORMULA... Complete...

> File: MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY (700.5)

> Cross references for file MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY have been

> .

> Re-indexing file MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY...

> Complete...

> File: RHEUMATOLOGY (701)

> Cross references for file RHEUMATOLOGY have been deleted.

> Re-indexing file RHEUMATOLOGY... Complete...

> Moving the Consult data from the Endoscopy/Consult file (#699) to the Generalized Procedure/Consult file (#699.5).

> Creating the MC MESSAGING SERVER mail group.

> Checking the sub-DD numbers in the Generalized Procedure/Consult file (#699.5).

> Deleting pointers to Lab files.

> Adding the cardiology code to the Medical Package Use multiple in the Medication file (#695)

> Update the pointers from the Procedure Term file (#694.8) to the Procedure/Subspecialty file (#697.2).

> Update the pointers from the Medicine View file (#690.2) to the Procedure/Subspecialty file (#697.2).

> Update the pointers from the Medicine View file (#690.2) to the ASTM file (#690.5).

> Updating Medicine package file level access security. Restoring locally defined procedures to the

> Medicine View file (#690.2) Updating Routine file...

> The following Routines were created during this install:

> MCOPRG MCOPRG1 MCOPRG2 MCAROC4 MCAROC41 MCAROC3 MCAROC31 MCAROC2 MCAROC21 MCAROC22 MCAROC1 MCAROT MCAROT1 MCAROK MCAROK1 MCAROEP MCAROEP1 MCAROV MCAROV1 MCAROH1 MCAROH11 MCAROH2

> MCAROGR MCAROGI MCAROGN MCAROG MCAROG1 MCAROHD MCAROHB MCAROHF MCAROPG MCAROPG1 MCAROPA MCAROPA1 MCAROPV MCAROPV1 MCAROPS MCAROPS1 MCAROE1 MCAROS0 MCAROS1 MCAROS2 MCAROS3 MCAROPF MCAROS4 MCARORB MCARORH MCARORH1 MCARORH2 MCAROGA MCAROGA1 MCAROP MCAROPE MCAROPE1 MCARORQ MCARORD MCARORN MCAROE2 MCARORP MCARORP1 MCARORL MCARORL1 MCARORL2 MCARORA MCARORE MCARORE1 MCAROGM MCARORF MCARORF1 MCARORF2 MCARORF3 MCAROGC MCAROGE MCOBC1 MCOBC11 MCOBE1 MCOBK MCOBEP MCOBH1 MCOBT MCOBGC MCOBGA

> MCOBGA1 MCOBGN MCOBPE MCOBPFT MCOBHEM MCOBPG MCOBPA MCOBPV MCOBPS MCOBPS1 MCOBGEN MCOBRH MCOBRH1 MCOBRHA MCOBRHA1 MCOBPF MCAROAT MCAROAT1 MCAROAT2

> Updating KIDS files... MEDICINE 2.3 Installed.

> Jun 04, 1996@13:12:46

> Not a production UCI

> NO Install Message sent

> September 1996 Medicine V. 2.3 75

> Install Completed

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global Select Installation Option:

# Patch MC\*2.2\*33 (Copy)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> =============================================================================

> Run Date: MAY 16, 1996 Designation: MC\*2.2\*33

> Package : MC - MEDICINE Priority : MANDATORY

> Version : 2.2 SEQ \#30 Status : RELEASED

> =============================================================================

> Subject: New Person Conversion Report Category: ROUTINE

> Description:

> ===========

> This patch is being released to help identify those sites with Medicine 2.2 New Person conversion problems. During the installation of 2.2 the conversion will only convert the data if the old 2.0 data dictionaries are in place. If the conversion was queued to run and the inits completed before the conversion did, some or all data will not be converted.

> The routine included in this patch will examine all the provider fields in all the files that should have been converted. It will produce a list of unique providers in these fields broken out by file and field name. This report should then be reviewed by the appropriate Medicine package users for correctness of the provider names. If a problem is found with the entries in these fields, you should contact the Customer Service Clin2 Support Team for further assistance. To fix the conversion problem, a modified Medicine 2.2 New Person conversion will have to be run at your site.

> This routine only prints data from the Medicine files, it does not change any data. The report may be run multiple times. It is recommended that the report be queued.

> This patch may be installed and run with Medicine users on-line. No options need to be disabled. MCNP2CHK is a new routine, it does not need to be mapped. This patch has no other patch dependencies. The installation time for this patch is minimal. The time it will take to produce the report is dependent on the number of entries in your Medicine files.

> Installing and Running the Patch:

1)  Unpack the PackMan patch message into your production account.
2)  DO ^MCNP2CHK (See the sample run below)

> Unique New Person Names in Medicine Provider Fields Apr 18, 1996

> Page: 1

> File Name (Number)

> Field Name (Number)

New Person Name IEN Provider Key

=================================================================

> ECHO file (#691)

> CARDIOLOGY ATTENDING field (#39)

> I OWA,HARVEY 1867 YES

> PENNSYLVANI A,MISTER 4589 YES CARDIOLOGY FELLOW field (#43)

> DELAWARE,JON 1859 NO

> CARDIAC CATHETERIZATION file (#691.1) CARDIOLOGY FELLOW field (#62)

> September 1996 Medicine V. 2.3 77

> Patch MC\*2.2\*33

> ...

> DELAWARE,JON 1859 NO CARDIOLOGY STAFF field (#63)

> I OWA,HARVEY 1867 YES

> PENNSYLVANI A,MISTER 4589 YES CARDIOLOGY FELLOW-2ND field (#64)

> FLORI DA,SCOTT 1448 NO

> Routine Information:

> ====================

> Routine Name: MCNP2CHK Description of Changes:

> The second line looks like:

> ;;2.2;MEDICINE;\*\*33\*\*;Jun 08, 1995

> Routine Checksum:

> MCNP2CHK value = 4467177

> =============================================================================

> User Information:

> Entered By : DELAWARE,DON Date Entered : APR 18,1996 Completed By: ARKANSAS,TONY Date Completed: APR 22,1996 Released By : RHODEI SLAND,JERALD F Date Released : APR 26,1996

> =============================================================================

> ![](medicine-version-2-3-release-notes-and-installation-guide/001.png)

> MEDICINE

> RELEASE NOTES INSTALLATION GUIDE

> Version 2.3

> September 1996

> Department of Veterans Affairs Software Service

> Clinical Support Product Line

[Release Notes 1](#release-notes)

> [Installation Information 5](#installation-information)

Post Installation 9

> Check List 9

> [Health Summary Routines 11](#health-summary-routines)

> September 1996 Medicine V. 2.3 i Release Notes and Installation Guide