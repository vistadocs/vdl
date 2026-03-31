---
title: Adverse Reaction Tracking Installation Manual
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: 
app_code: GMRA
app_name: "CPRS: Adverse Reaction Tracking (ART)"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > Adverse Reaction Tracking (ART) requires an estimated minimum of 0.7 megabytes of disk space to install.
audience: 
keywords: 
  - blockquote
  - gmrai
  - table
  - class
  - installation
  - contents
  - style
  - width
  - site
  - gmra
page_count: 0
word_count: 2028
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/gmra_allr4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/gmra_allr4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=57"
---

> General Installation Information

### GMRA Namespace: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All components of this software begin with the letters GMRA.

### Resource Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Adverse Reaction Tracking (ART) requires an estimated minimum of 0.7 megabytes of disk space to install.

> There should be at least one terminal and one printer at each location where ART will be used.

> The disk requirements are estimated as follows:

> <u>Globals</u> <u>Type of Data</u> <u>Size</u> GMRD(120.82,

> GMRD(120.83, Static data for ART 40K GMRD(120.84,

> GMRD(120.87,

> GMRD(120.8, Patient data for ART 0.4K per Allergy entry GMRD(120.85, Observed, FDA 0.4K per Reaction

> GMRD(120.86, Patient NKA data 0.01K per Patient

### Soft ware Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following packages must be installed before installing Adverse Reaction Tracking:

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Name</u></strong></th>
<th><blockquote>
<p><strong><u>Min. Ver.</u></strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><blockquote>
<p>7.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td><blockquote>
<p>21</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAS/PIMS</td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>National Drug File</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> If this is not a virgin installation, the GMRA\*3\*13 patch must be installed. The patch portion of the version line of the GMRARAD1 routine must contain “13”.

> If your site is using the Progress Notes (v2.5) package, then GMRP\*2.5\*32 must be installed. This Progress Notes patch provides ART with a new interface to

> create progress notes.

### Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Adverse Reaction Tracking package contains the following 7 files .

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 37%" />
<col style="width: 23%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data</strong></p>
<p><strong>Exported with</strong></p>
<p><strong>Installation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>120.8</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ALLERGIES</p>
</blockquote></td>
<td><blockquote>
<p>^ GMR(120.8,</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>120.82</p>
</blockquote></td>
<td><blockquote>
<p>GMR ALLERGIES</p>
</blockquote></td>
<td><blockquote>
<p>^ GMRD(120.82,</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>120.83</p>
</blockquote></td>
<td><blockquote>
<p>SIGN/SYMPTOMS</p>
</blockquote></td>
<td><blockquote>
<p>^ GMRD(120.83,</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>120.84</p>
</blockquote></td>
<td><blockquote>
<p>GMR ALLERGY SITE PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>^ GMRD(120.84,</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>120.85</p>
</blockquote></td>
<td><blockquote>
<p>ADVERSE REACTION REPORTING</p>
</blockquote></td>
<td><blockquote>
<p>^ GMR(120.85,</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>120.86</p>
</blockquote></td>
<td><blockquote>
<p>ADVERSE REACTION ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>^ GMR(120.86,</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>120.87</p>
</blockquote></td>
<td><blockquote>
<p>GMRA DOCUMENT</p>
</blockquote></td>
<td><blockquote>
<p>^ GMRD(120.87,</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Files \#120.82, \#120.83 and \#120.84 will add their data to the local system

> only when the file does not exist (Virgin Installation) or no data exists in the file. Appendix 1 of the Adverse Reaction Tracking User Manual contains a list of data entries exported with this version for File \#120.82. Appendix 2 of the user manual contains a list of data entries exported with this version for File \#120.83. File \#120.87 is a new file and its data will be added to the

> system.

3.  Other DHCP files used by Adverse Reaction Tracking :

> New Person

> Generic Progress Note

> Generic Progress Note Type Generic Progress Note Title Drug Ingredient

> VA Drug Class Protocol

> Title

> Patient

> National Drug File

> 200 Required 121

> 121.1

> 121.2

> 50.416 Required

> 50.605 Required

> 101 Required

> 3.1 Required

> 2 Required

> 50.6 Required

> Drug 50 Required

### Installation Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version of the software uses the Kernel Installation and Distribution System (KIDS) to install the package. An environment check routine

> (GMRAXENV) is used by Adverse Reaction Tracking to verify that all the

> needed packages have been installed. If the checks in the environment routine are satisfied, the package name in the PACKAGE (#9.4) file will change from GEN. MED. REC. -ALLERGIE S to ADVERSE REACTION TRACKING. Also,

> the SHORT DESCRIPTION (#2) and DESCRIPTION (#3) fields of File \#9.4 will be updated.

> Adverse Reaction Tracking uses a Pre- installation routine (GMRAXPRE) to delete the ANKA cross reference which is no longer needed.

> Adverse Reaction Tracking also uses post installation routines (GMRAXPST and GMRAXNKA) to update the Adverse Reaction Tracking database after the

> installation is completed by KIDS. Specifically, the post-installation does the following:

4.  Deletes the NO KNOWN ALLERGIES field (#.03) in the Patient Allergies file (#120.8),
5.  Moves those records which represent whether a patient has been asked about allergies (NKA nodes) from the Patient Allergies file (#120.8) to the Adverse Reaction Assessment file (#120.86),
6.  Converts the set of codes of the COMMENT TYPE sub-field (#1.5) of the COMMENTS multiple (#26) of the Patient Allergies file (#120.8) from old values to new values, and
7.  Creates the following mail groups if they do not already exist:
    1.  GMRA MARK CHART
    2.  GMRA VERIFY DRUG ALLERGY
    3.  GMRA VERIFY FOOD ALLERGY
    4.  GMRA VERIFY OTHER ALLERGY
    5.  GMRA P&T COMMITTEE FDA
8.  Loops through File \#121.2 and changes the ALLERGY/ADVERSE REACTION entry value to ADVERSE REACTION/ALLERGY.
9.  Checks the file level security codes for Files \#120.8-120.87 and changes the site's values to match what is in the KIDS Build.

### Test Site Installation Time s:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 43%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Type of System</u></p>
</blockquote></th>
<th><blockquote>
<p><u># of records converted</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Install Time</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Site #1 (Alpha)</p>
</blockquote></td>
<td><blockquote>
<p>16,309</p>
</blockquote></td>
<td><blockquote>
<p>55 minutes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Site #2 (Alpha)</p>
</blockquote></td>
<td><blockquote>
<p>11,957</p>
</blockquote></td>
<td><blockquote>
<p>25 minutes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Site #3 (Alpha)</p>
</blockquote></td>
<td><blockquote>
<p>5,464</p>
</blockquote></td>
<td><blockquote>
<p>20 minutes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Site #4 (Alpha)</p>
</blockquote></td>
<td><blockquote>
<p>13,069</p>
</blockquote></td>
<td><blockquote>
<p>51 minutes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Site #5 (MSM)</p>
</blockquote></td>
<td><blockquote>
<p>2,047</p>
</blockquote></td>
<td><blockquote>
<p>14 minutes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Site #6 (Alpha)</p>
</blockquote></td>
<td><blockquote>
<p>11,150</p>
</blockquote></td>
<td><blockquote>
<p>34 minutes</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Installation Instructions

1.  Preparation:
- We encourage you to back up your system before you install.
- Coordinate the installation with the package ADPAC.
- Schedule downtime with the users of the ART package. The installation will put the GMRA namespace options out-of-service for the duration of the install. The system does not have to be down during the installation.
- Make certain that patch GMRA\*3\*13 is installed. This is required by the environment check routine. The patch portion of the version line of the GMRARAD1 routine should contain a ‘13’.
- Disable mapping if applicable.
- Disable journaling if applicable.
- On MSM systems, the installation process will prompt you to move the package’s routines to the other CPUs. If you inhibit logons to the CPUs receiving the

> routines you must shutdown TaskMan, otherwise the routines will not be moved.

### Pre-Installation Tasks:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> D ^XUP to establish programmer variables and set DUZ(0) for Programmer

> access. You will want to delete the old Adverse Reaction Tracking init routines.

> Select the routines with the GMA and GMRAI namespace. The following is an example:

> \>D ^%RDELETE

> ROUTINE DELETE

> routine(s) ? \> GMA\* searching directory ... routine(s) ? \> GMRAI\* searching directory ... routine(s) ? \> \<RET\>

> 89 routines to DELETE, OK: NO// Y

> GMAAI001 GMAAI002 GMAAI003 GMAAI004 GMAAI005 GMAAI006 GMAAI007 GMAAI008 GMAAI009 GMAAI00A GMAAIENV GMAAINI1 GMAAINI2 GMAAINI3 GMAAINI4 GMAAINI5 GMAAINIS GMAAINIT GMAAIPRE GMAAIPST GMABO001 GMABONI1 GMABONI2 GMABONI3

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GMABONIT</p>
</blockquote></th>
<th>GMACI001</th>
<th>GMACINI1</th>
<th><blockquote>
<p>GMACINI2</p>
</blockquote></th>
<th>GMACINI3</th>
<th>GMACINI4</th>
<th>GMACINI5</th>
<th><blockquote>
<p>GMACINIS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GMACINIT</p>
</blockquote></td>
<td>GMRAI001</td>
<td>GMRAI002</td>
<td><blockquote>
<p>GMRAI003</p>
</blockquote></td>
<td>GMRAI004</td>
<td>GMRAI005</td>
<td>GMRAI006</td>
<td><blockquote>
<p>GMRAI007</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRAI008</p>
</blockquote></td>
<td>GMRAI009</td>
<td>GMRAI010</td>
<td><blockquote>
<p>GMRAI011</p>
</blockquote></td>
<td>GMRAI012</td>
<td>GMRAI013</td>
<td>GMRAI014</td>
<td><blockquote>
<p>GMRAI015</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRAI016</p>
</blockquote></td>
<td>GMRAI017</td>
<td>GMRAI018</td>
<td><blockquote>
<p>GMRAI019</p>
</blockquote></td>
<td>GMRAI020</td>
<td>GMRAI021</td>
<td>GMRAI022</td>
<td><blockquote>
<p>GMRAI023</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRAI024</p>
</blockquote></td>
<td>GMRAI025</td>
<td>GMRAI026</td>
<td><blockquote>
<p>GMRAI027</p>
</blockquote></td>
<td>GMRAI028</td>
<td>GMRAI029</td>
<td>GMRAI030</td>
<td><blockquote>
<p>GMRAI031</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRAI032</p>
</blockquote></td>
<td>GMRAI033</td>
<td>GMRAI034</td>
<td><blockquote>
<p>GMRAI035</p>
</blockquote></td>
<td>GMRAI036</td>
<td>GMRAI037</td>
<td>GMRAI038</td>
<td><blockquote>
<p>GMRAI039</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRAI040</p>
</blockquote></td>
<td>GMRAI041</td>
<td>GMRAI042</td>
<td><blockquote>
<p>GMRAI043</p>
</blockquote></td>
<td>GMRAI044</td>
<td>GMRAI045</td>
<td>GMRAI046</td>
<td><blockquote>
<p>GMRAI047</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRAI048</p>
</blockquote></td>
<td>GMRAI049</td>
<td>GMRAINI0</td>
<td><blockquote>
<p>GMRAINI1</p>
</blockquote></td>
<td>GMRAINI2</td>
<td>GMRAINI3</td>
<td>GMRAINI4</td>
<td><blockquote>
<p>GMRAINIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRAINIT</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Done.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> The installation process updates the remaining GMRA routines and deletes some obsolete GMRA routines.

### Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  This version of Adverse Reaction Tracking does <u>not</u> use DIFROM inits.

> Instead Adverse Reaction Tracking uses the KIDS utility. KIDS can install the package immediately or task it to run at a later time. You will again

> want to Do ^XUP and select the Kernel Installation & Distribution System option.

> NOTE: The installation example dialogue that follows may vary depending on the system you have (Alpha or MSM) and the additional work that must be done in the pre and post installation process.

> \> D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: KERNEL INSTALLATION & DISTRIBUTION XPD MAIN Kernel

> Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option:

2.  Select the Installation menu option. Within the Installation menu you will select the Load a Distribution option. At the prompt “Enter a Host File:”

> enter the filename ALLR4.KID. ALLR4.KID is the Adverse Reaction

> Tracking KIDS Build. The following is an example of loading a distribution.

> Select Kernel Installation & Distribution System Option: INSTALLATION

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: LOAD A DISTRIBUTION

> Enter a Host File: ALLR4.KID

> KIDS Distribution saved on JAN 08, 1996@9:44:57 Comment: ADVERSE REACTION TRACKING V4.0

> This Distribution contains Transport Globals for the following Package(s): ADVERSE REACTION TRACKING 4.0

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> Will first run the Environment Check Routine, GMRAXENV

> Use ADVERSE REACTION TRACKING 4.0 to install this Distribution.

3.  You may wish to run the Verify Checksums in the Transport Global option at this point as a precaution. If there are any discrepancies, do not run the

> Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.

4.  Select the Install Package(s) option from the menu. The system will ask you the name of the package to be installed and the device to display the

> information as the installation progresses.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: INSTALL PACKAGES(S)

> Select INSTALL NAME: ?

> Answer with INSTALL NAME Choose from:

> ADVERSE REACTION TRACKING 4.0 Loaded from Distribution

> Select INSTALL NAME: ADVERSE REACTION TRACKING 4.0 Loaded from

> Distribution

> This Distribution was loaded on Jan 08, 1996@11:58:43 with header of

> ADVERSE REACTION TRACKING V4.0 ;Created on Jan 08, 1996@09:44:57

> It consisted of the following Install(s):

> ADVERSE REACTION TRACKING 4.0

> Will first run the Environment Check Routine, GMRAXENV Install Questions for ADVERSE REACTION TRACKING 4.0

> 120.8 PATIENT ALLERGIES

> Note: You already have the 'PATIENT ALLERGIES' File.

82. GMR ALLERGIES (including data) Note: You already have the 'GMR ALLERGIES' File. Data will NOT be added.
83. SIGN/SYMPTOMS (including data) Note: You already have the 'SIGN/SYMPTOMS' File. Data will NOT be added.
84. GMR ALLERGY SITE PARAMETERS (including data) Note: You already have the 'GMR ALLERGY SITE PARAMETERS' File. Data will NOT be added.
85. ADVERSE REACTION REPORTING

> Note: You already have the 'ADVERSE REACTION REPORTING' File.

86. ADVERSE REACTION ASSESSMENT
87. GMRA DOCUMENT (including data)

> Want to DISABLE Scheduled Options and Options? YES// \<RET\>

> Enter options you wish to mark as 'Out Of Order': \<RET\>

> Delay Install (Minutes): (0-60): 0// \<RET\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// HOME

> Install Started for ADVERSE REACTION TRACKING 4.0 : Jan 08, 1996@15:30:04

> Installing

> Routines:...............................................................

> ..

> Jan 08, 1996@15:30:13

> Running Pre-Install Routine: ^GMRAXPRE. Installing Data Dictionaries: .......

> Jan 08, 1996@15:30:22

> Installing Data:

> Jan 08, 1996@15:30:22

> Installing PACKAGE COMPONENTS:

> Installing BULLETIN.........

> Installing SECURITY KEY...

> Installing PRINT TEMPLATE...

> Installing SORT TEMPLATE.. Installing PROTOCOL...

> Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace..

> Installing OPTION..........................................

> Jan 08, 1996@15:30:39

> Running Post-Install Routine: ^GRMAXPST.

> Move 120.8 NKA Cross Reference to 120.86......

> The GMRA MARK CHART mail group has been added.

> The GMRA VERIFY DRUG ALLERGY mail group has been added. The GMRA VERIFY FOOD ALLERGY mail group has been added. The GMRA VERIFY OTHER ALLERGY mail group has been added. The GMRA P&T COMMITTEE FDA mail group has been added.

> Updating File security on file 120.8. Updating File security on file 120.82. Updating File security on file 120.83. Updating File security on file 120.84. Updating File security on file 120.85. Updating File security on file 120.86. Updating File security on file 120.87.

> The Progress Note Title of ALLERGY/ADVERSE REACTION with a note type of GENERAL NOTE has been changed to ADVERSE REACTION/ALLERGY.

> Updating Routine file......

> Updating KIDS files.......

> ADVERSE REACTION TRACKING 4.0 Installed.

> Jan 08, 1996@15:30:52

> Install Message sent \#1234

> Waiting for job on VOLUME SET CSA to start. Note: You will see this text

> Waiting for mob on VOLUME SET CSA to complete. only if you are installing the

> software on an MSM system

> Job on VOLUME SET CSA Completed. and have told KIDS to move the routines to other CPUs.

### Implementation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Move the GMRA\* namespaced routines onto all your systems, if applicable.
- Enable journaling, if applicable.
- The following global is recommended for journaling:

> ^ GMR

- For multiple CPUs the following globals must be translated:

> ^ GMR

> ^ GMRD

- Enable routine mapping if applicable.
- Use the KIDS Build File Print option if you wish to obtain a complete listing of package components (e.g., routines and options) sent with this software.
- Use the KIDS Install File Print option if you wish to print out the results of the installation process.
- The following are new protocols which are distributed with this version:

> GMRA RECEIVE - Will be used by CPRS (ORDER ENTRY) V3.0 to send an Allergy/Adverse Reaction entry in an HL7 message format to the ART

> database.

- Other packages can ‘hang’ their protocols off the following protocols to perform necessary tasks when these events occur.

> GMRA ENTER IN ERROR - When a user marks a reaction as ‘entered-in- error’, this extended action protocol is invoked.

> GMRA MEDWATCH DATA COMPLETE - When the P&T Committee completes and indicates that an FDA MEDWatch Form has been sent for a reaction, this extended action protocol is invoked.

> GMRA SIGN-OFF DATA - When a user signs off on (i.e., completes) a reaction(s) for a patient, this extended action protocol is invoked.

> GMRA VERIFY DATA - When a user verifies a patient reaction, this extended action protocol is invoked.

- Use the Enter/Edit Site Parameters \[GMRA SITE FILE\] option to update two new parameters in the GMR ALLERGY SITE PARAMETERS file (#120.84):

> NEW ADMISSION CHART MARK (#7.3) - A YES/NO response to indicate if the site wants to send a chart mark bulletin for a new admission.

> E/E DESCRIPTION ACTIVE (#10.1) - A YES/NO response which permits the user to indicate why a reaction was entered in error.

- Refer to the Adverse Reaction Tracking Technical Manual for instructions on implementing and maintaining Adverse Reaction Tracking .
- Note: The SACC has granted several exemptions. If you run the %INDEX

> utility on the GMRA\* routines, you will see many fatal type errors which are not really a cause for concern. See the SACC Exemptions chapter in the Adverse

> Reaction Tracking Technical Manual for a list of the exemptions.

## Virgin Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Preparation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- We encourage you to back up your system before you install. The system does not have to be down during the installation.
- Coordinate the installation with the package ADPAC.
- Disable mapping if applicable.
- Disable journaling if applicable.
- On MSM systems, the installation process will prompt you to move the package’s routines to the other CPUs. If you inhibit logons to the CPUs receiving the

> routines you must shutdown TaskMan, otherwise the routines will not be moved.

### Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version of Adverse Reaction Tracking does <u>not</u> use DIFROM inits. Instead Adverse Reaction Tracking uses the KIDS utility. KIDS can install the package immediately or task it to run at a later time. You will want to Do ^XUP and

> select the Kernel Installation & Distribution System option.

> NOTE: The installation example dialogue that follows may vary depending on the system you have (Alpha or MSM) and the additional work that must be done in the pre and post installation process.

> This section contains an example of a virgin installation of the software. This example assumes TaskMan is running.

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INSTALLATION

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: LOAD A DISTRIBUTION

> Enter a Host File: ALLR4.KID

> KIDS Distribution saved on Jan 12, 1996@09:42:08 Comment: ADVERSE REACTION TRACKING V4.0

> This Distribution contains Transport Globals for the following Package(s): ADVERSE REACTION TRACKING 4.0

> Want to Continue with Load? YES// \<ret\>

> Loading Distribution...

> Will first run the Environment Check Routine, GMRAXENV

> Use ADVERSE REACTION TRACKING 4.0 to install this Distribution.

> You may wish to run the Verify Checksums in the Transport Global option at this point as a precaution. If there are any discrepancies, do not run the Install

> Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.

> Load a Distribution Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Backup a Transport Global

> Select Installation Option: INSTALL PACKAGES(S)

> Select INSTALL NAME: ADVERSE REACTION TRACKING 4.0 Loaded from

> Distribution

> This Distribution was loaded on Jan 31, 1996@09:07:08 with header of ADVERSE REACTION TRACKING V4.0 ;Created on Jan 31, 1996@09:05:59

> It consisted of the following Install(s): ADVERSE REACTION TRACKING 4.0

> Will first run the Environment Check Routine, GMRAXENV Install Questions for ADVERSE REACTION TRACKING 4.0

> 120.8 PATIENT ALLERGIES

82. GMR ALLERGIES (including data)
83. SIGN/SYMPTOMS (including data)
84. GMR ALLERGY SITE PARAMETERS (including data)
85. ADVERSE REACTION REPORTING
86. ADVERSE REACTION ASSESSMENT
87. GMRA DOCUMENT (including data)

> Want to DISABLE Scheduled Options and Options? YES// \<ret\> Enter options you wish to mark as 'Out Of Order': \<ret\> Delay Install (Minutes): (0-60): 0// \<ret\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<ret\> HOME

> Install Started for ADVERSE REACTION TRACKING 4.0 : Jan 31, 1996@09:07:46

> Installing Routines

> ..............................................................................

> ..............

> Jan 31, 1996@09:07:51

> Running Pre-Install Routine: ^GMRAXPRE

> Installing Data Dictionaries: ........................

> Jan 31, 1996@09:08

> Installing Data: ....

> Jan 31, 1996@09:08:07

> Installing PACKAGE COMPONENTS:

> Installing BULLETIN..........

> Installing SECURITY KEY...

> Installing PRINT TEMPLATE...

> Installing SORT TEMPLATE.. Installing PROTOCOL...

> Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace..

> Located in the GMRA (ADVERSE REACTION TRACKING) namespace.. Located in the GMRA (ADVERSE REACTION TRACKING) namespace..

> Installing OPTION...............................................................

> Jan 31, 1996@09:08:23

> Running Post-Install Routine: ^GRMAXPST.

> The GMRA MARK CHART mail group has been added.

> The GMRA VERIFY DRUG ALLERGY mail group has been added. The GMRA VERIFY FOOD ALLERGY mail group has been added. The GMRA VERIFY OTHER ALLERGY mail group has been added. The GMRA P&T COMMITTEE FDA mail group has been added.

> Updating File security on file 120.8. Updating File security on file 120.82. Updating File security on file 120.83. Updating File security on file 120.84. Updating File security on file 120.85. Updating File security on file 120.86. Updating File security on file 120.87.

> The Progress Note Title of ALLERGY/ADVERSE REACTION with a note type of GENERAL NOTE has been changed to ADVERSE REACTION/ALLERGY.

> Updating Routine file......

> Updating KIDS files.......

> ADVERSE REACTION TRACKING 4.0 Installed.

> Jan 31, 1996@09:08:36

> Install Completed

### Implementation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Move the GMRA\* namespaced routines onto all your systems, if applicable.
- Enable journaling, if applicable.
- The following global is recommended for journaling:

> ^ GMR

- For multiple CPUs the following globals must be translated:

> ^ GMR

> ^ GMRD

- Enable routine mapping if applicable.
- Use the KIDS Build File Print option if you wish to obtain a complete listing of package components (e.g., routines and options) sent with this software.
- Use the KIDS Install File Print option if you wish to print out the results of the installation process.
- The following are new protocols which are distributed with this version:

> GMRA RECEIVE - Will be used by CPRS (ORDER ENTRY) V3.0 to send an Allergy/Adverse Reaction entry in an HL7 message format to the ART

> database.

- Other packages can ‘hang’ their protocols off the following protocols to perform necessary tasks when these events occur.

> GMRA ENTER IN ERROR - When a user marks a reaction as ‘entered-in- error’, this extended action protocol is invoked.

> GMRA MEDWATCH DATA COMPLETE - When the P&T Committee completes and indicates that an FDA MEDWatch Form has been sent for a reaction, this extended action protocol is invoked.

> GMRA SIGN-OFF DATA - When a user signs off (i.e., completes) on a reaction(s) for a patient, this extended action protocol is invoked.

> GMRA VERIFY DATA - When a user verifies a patient reaction, this extended action protocol is invoked.

- Refer to the Adverse Reaction Tracking Technical Manual for instructions on

> implementing and maintaining Adverse Reaction Tracking . You will definitely want to run the Enter/Edit Site Parameters option to customize the software to your site's needs.

> Department of Veterans Affairs Decentralized Hospital Computer Program

> ADVERSE REACTION TRACKING INSTALLATION GUIDE

# Version 4.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [GMRA Namespace:](#gmra-namespace)
    - [Resource Requirements:](#resource-requirements)
    - [Soft ware Requirements:](#soft-ware-requirements)
    - [Files:](#files)
    - [Installation Routines:](#installation-routines)
    - [Test Site Installation Time s:](#test-site-installation-time-s)
    - [Pre-Installation Tasks:](#pre-installation-tasks)
    - [Installation:](#installation)
    - [Implementation:](#implementation)
  - [Virgin Installation](#virgin-installation)
    - [Preparation:](#preparation)
    - [Installation:](#installation-1)
    - [Implementation:](#implementation-1)
- [Version 4.0](#version-40)
> March 1996
> Information Resource Management Field Office Hines, Illinois
