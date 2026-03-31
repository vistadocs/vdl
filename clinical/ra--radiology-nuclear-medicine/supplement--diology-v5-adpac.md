---
title: Radiology Version 5 ADPAC Supplement
doc_type: SUP
doc_label: Supplement
doc_layer: anchor
doc_subject: ADPAC Supplement
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Documentation Conventions](#documentation-conventions) - [Assumptions](#assumptions) - [Radiology/Nuclear Medicine VAMC Annual Code Changes](#radiologynuclear-medicine-vamc-annual-code-changes) - [Radiology/Nuclear Medicine Code Change Process](#radiologynuclear-medicine-code-change-process) - [R
audience: 
keywords: 
  - span
  - procedure
  - class
  - radiology
  - mark
  - conscious
  - adpac
  - procedures
  - sedation
  - code
page_count: 0
word_count: 2929
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 8
revision_newest: 4/4/2017
revision_oldest: 3/15/2017
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra_5_aa_s_1.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra_5_aa_s_1.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

---
title: |
  Collaborative Terminology Tooling & Data Management (CTT & DM)

  Native Domain Standardization (NDS)
---

Radiology Reports

Automated Data Processing Application Coordinator

(ADPAC)

Manual Code Change Supplement

![](radiology-version-5-adpac-supplement/001.png)

April 2017

Department of Veterans Affairs (VA)

Revision History

| Date      | Revision | Description                                                                              | Author                             |
|-----------|----------|------------------------------------------------------------------------------------------|------------------------------------|
| 4/4/2017  | 1.0      | Delivery to VA                                                                           | <span class="mark">REDACTED</span> |
| 4/4/2017  | 0.7      | Technical Writer review                                                                  | <span class="mark">REDACTED</span> |
| 4/3/2017  | 0.6      | Update for Parent Procedure Inactivation Date.                                           | <span class="mark">REDACTED</span> |
| 3/30/2017 | 0.5      | Update use of forward slashes                                                            | <span class="mark">REDACTED</span> |
| 3/20/2017 | 0.4      | Technical Writer review                                                                  | <span class="mark">REDACTED</span> |
| 3/20/2017 | 0.3      | Update feedback within Document.                                                         | <span class="mark">REDACTED</span> |
| 3/20/2017 | 0.2      | Stakeholder review and feedback                                                          | <span class="mark">REDACTED</span> |
| 3/15/2017 | 0.1      | Initial draft – Provided process & content for Manual Code Change Updates to Procedures. | <span class="mark">REDACTED</span> |

Document revision history.

Table of Content

Table of Figures

# Documentation Conventions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Documentation Conventions](#documentation-conventions)
- [Assumptions](#assumptions)
- [Radiology/Nuclear Medicine VAMC Annual Code Changes](#radiologynuclear-medicine-vamc-annual-code-changes)
- [Radiology/Nuclear Medicine Code Change Process](#radiologynuclear-medicine-code-change-process)
  - [Radiology Procedure - Before RA\5\127 Patch](#radiology-procedure-before-ra5127-patch)
  - [Procedure File Code Update Process after RA\5\127](#procedure-file-code-update-process-after-ra5127)
- [Parent Procedures and Inactivation Date](#parent-procedures-and-inactivation-date)
- [Conclusion](#conclusion)
- [Appendix A](#appendix-a)
  - [Radiology Informational Patch RA\5\134](#radiology-informational-patch-ra5134)
This manual uses several methods to highlight different aspects of the material:
- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a non-proportional font and enclosed within a box.
- User’s responses to online prompts are bold typeface, underlined and highlighted in yellow (e.g., <span class="mark">\<<u>Enter</u>\></span>).
- Emphasis within a dialogue box is bold typeface, underlined and highlighted in blue and in all capital letters (e.g., <span class="mark"><u>STANDARD LISTENER: RUNNING</u></span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.
> **NOTE:** Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., DIEXTRACT).
> **NOTE:** Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

# Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Access to Radiology Supervisor Menu functions

  <u><span class="mark">Important Note:</span> <span class="mark">PLEASE READ</span></u>
1.  *The ADPAC* will not have the ability to key the double question marks ‘??’ for a procedure list.  
    There will be need for the ADPAC to enter at least 3 characters of the procedure name in order to obtain the partial list of related procedures.
2.  *Informational Patch* - (See Appendix A) This is in reference to NTRT Seeding, please read.  
    <span class="mark">*<u>ADPAC</u>*:</span>  
    Do not continue until ‘The system installer has verified that the MASTER RADIOLOGY PROCEDURE file (#71.99) (MRPF) content has been deployed to your facility”.
3.  *<span class="mark">Duplicate Error: When doing a direct match on a procedure name</span>*, if there are multiple procedures with the same name being entered. If the user is entering the procedure name with double quotes (“ “) due to an existing procedure having the same name. If an error is issued as a result of duplicate records. To avoid this issue, the user will need to put in the procedure name omitting the last few characters to avoid a duplication error.  
    >   
    > Example: RAD NUC/MED PROCEDURES NAME: “WRIST 2 VIEWS”  
    > Enter as: “WRIST 2 VIEW”
4.  <span class="mark">Procedure Name with Forward Slashes (‘/’)</span>, May not create Procedures with forward slashes (‘/’) in the Procedure name. May not edit Procedures with a forward slash (‘/’) in the Procedure Name.

# Radiology/Nuclear Medicine VAMC Annual Code Changes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In January of each year VAMC provides new CPT codes that impact the Radiology Procedures depending on the site the number of code changes.

As an example in January, 2017 one of the VA facilities had an estimated 25 -30 procedures that needed to be updated as a result of the annual VAMA code changes as follows:

New CPT Codes requiring procedure changes for a specific VA Sites are as follows:

- 20 - Interventional Rad
- 4 - Mammography
- 6 - Conscious Sedation.

During the analysis phase of the NDS Radiology Domain decisions were made by the stakeholders resulting in a difference in the appearance and the Procedure data reflected. The impact of these changes is apparent with the VAMA annual code changes.

Information being displayed for the procedure has been truncated due to size restriction and the request by VA stakeholders to have the Procedure Name more descriptive has resulted in less information associated with the procedure names. Within the ‘RAD/NUC MED PROCEDURES NAME’, the ADPAC will not be able to see the Type of Imaging, nor will they see ‘Detailed’ reflected. The CPT code is no longer reflected on the resulting procedure list displayed.

# Radiology/Nuclear Medicine Code Change Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the annual VAMC code changes are distributed to the VA facilities, the ADPAC will need to update each individual procedure impacted by the new CPT codes provided to the medical centers.

## Radiology Procedure - Before RA\*5\*127 Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the ADPAC executes the PROCEDURE Entry/Edit, they then select to process a partial procedure list of all related procedures.

When entering a partial procedure name prior to the deployment of the NDS patch RA\*5\*127 install, the ‘Procedure Enter/Edit Display would have appeared with the abbreviated ‘Type of Imaging (CT Detailed) and the CPT code (CPT: 99145) was also reflected as seen in Figure 1.

DISPLAY of Radiology Procedure List BEFORE RA\*5\*127 Patch:

<span id="_Toc479074042" class="anchor"></span>Figure : Radiology/Nuclear Medicine Partial Procedure List BEFORE RA\*5\*127 patch

CHOOSE 1-2: 1  RA PROCEDURE     Procedure Enter/Edit

Procedure Enter/Edit

Select RAD/NUC MED PROCEDURES NAME: CONSCIOUS

     1   CONSCIOUS SED (+15 MIN)             <span class="mark">(CT   Detailed) CPT:99145</span>

     2   CONSCIOUS SED. (1ST 30 MIN)         (CT   Detailed) CPT:99144

     3   CONSCIOUS SEDATION (+15 MIN)        (ANI  Detailed) CPT:99145

     4   CONSCIOUS SEDATION (15 MIN)         (ANI  Detailed) CPT:99150

     5   CONSCIOUS SEDATION (1ST 30 MIN)     (ANI  Detailed) CPT:99149

     6   CONSCIOUS SEDATION (1ST 30 MIN)     (ANI  Detailed) CPT:99144

     7   CONSCIOUS SEDATION (30 MIN)         (CT   Detailed) CPT:99149

<u>IMPORTANT NOTE:</u> This is reflected within the NDS Radiology ADPAC Addendum.

Upon Enter/Edit of a procedure, the lookup of a procedure with the capability of utilizing the CPT Code is no longer applicable. The ADPAC is required to enter the Procedure or partial Procedure name for this function.

## Procedure File Code Update Process after RA\*5\*127

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the NDS Radiology Patch RA\*5\*127 is installed the ADPAC will not have visibility to the Type of Imaging, Detailed nor the CPT Code.

As a result of the new patch, the Radiology Procedure List display will have a different appearance.

When the VAMC annual code changes are provided, the Radiology ADPAC will be responsible for updating each impacted radiology procedure title identify the type of imaging in an abbreviated format to identify the imaging location.

ADPAC enters a partial procedure name as “conscious” to execute a Partial Procedure List:

RAD/NUC MED PROCEDURES NAME: conscious

Procedure Entry/Edit

Resulting Partial Procedure List AFTER RA\*5\*127 patch installation and BEFORE the ADPAC updates the procedures impacted by code changes.

<span id="_Toc479074043" class="anchor"></span>Figure : Radiology/Nuclear Medicine Partial Procedure List “AFTER” the NDS RA\*5\* 127 patch

Select one of the following:

1 CONSCIOUS SED, EACH ADDITIONAL 15 MIN INTRA-SERVICE TIME/1935

<span class="mark">2 CONSCIOUS SEDATION -P/2475</span>

3 CONSCIOUS SEDATION 1ST 30 MIN/2473

4 CONSCIOUS SEDATION, FIRST 30 MIN INTRA-SERVICE TIME/1934

5 CONSCIOUS SED, EACH ADDITIONAL 15 MIN INTRA-SERVICE TIME/1933

<span class="mark">6 CONSCIOUS SEDATION -P/2321</span>

7 CONSCIOUS SEDATION EACH ADDIT 15 MIN/2474

<span class="mark">8 CONSCIOUS SEDATION -P/2324</span>

9 CONSCIOUS SEDATION, 1ST 30 MIN/2388

10 CONSCIOUS SEDATION, FIRST 30 MIN INTRA-SERVICE TIME/1932

11 CONSCIOUS SEDATION-P/2762

12 New Procedure

13 None of the above

Per the above display, when a procedure has a ‘Type of Imaging’, it is not visible within the RAD/NUC MED PROCEDURES LISTED.

The Radiology ADPAC executes ‘Procedure Entry Edit’ to make a new descendent with the new code and then update the parent for specific procedures impacted as a result of the VAMA annual new codes provided in January each year.

- ADPAC changes the descendants in the parents. Imaging location is important, with only the – P (parent).
- The ADPAC will go into the individual procedure in order to determine the actual ‘Type of Imaging’ for the Procedure.
- The ADPAC will update the individual procedures title with the ‘Type of Imaging’ in order for this imaging location to be visible on the display of impacted procedures within the resulting partial list going forward.
- An abbreviation of the Type of Imaging will be updated in the title.
- Example: ‘CT’ indicates CT Scan
- There are restrictions on the size of the Procedure name being displayed.

These updates made to the procedures will exist throughout the life cycle of the procedure.

With the Imaging Location updates, the ADPAC may update an existing procedure or determine they should add another procedure to support the change.

The ADPAC Process updates the procedure utilizing the following process:

The ADPAC named the <u>descendants moderate sedation</u> and set the <u>imaging locations</u>.

<span id="_Toc479074044" class="anchor"></span>Figure : Radiology/Nuclear Medicine ADPAC Updated Process After the NDS RA 127 patch

Enter a number from the list above: 8

NAME: CONSCIOUS SEDATION -P Replace

TYPE OF IMAGING: CT SCAN//

…………………………………………………………………………………………………………………………………………………………………………………………………………

Adpac viewed the procedure to determine that \#8 corresponded with

CT SCAN and therefore renamed the parent as follows:

CONSCIOUS SEDATION (CT) –P

The partial Procedure List now reflects the updated Type of Imaging when displayed.

Below are <span class="mark">three Procedures updated by the Radiology ADPAC</span> based on the new VAMC codes. (See lines 2, 6 and 8).

This list is the workable display of the parents updated after the new patch installation.

<span id="_Toc479074045" class="anchor"></span>Figure : Radiology/Nuclear Med Partial Procedure List “AFTER” the ADPAC UPDATES  
Post RA\*5\*127

CHOOSE 1-5: 3  RA PROCEDURE          Procedure Enter/Edit

Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: CONSCIOUS

Select one of the following:

 1  <span class="mark">CONSCIOUS  SED, EACH ADDITIONAL 15 MIN INTRA-SERVICE TIME/1935</span>

2  <span class="mark">CONSCIOUS  SEDATION (GEN RAD) -P/2475</span>

3  <span class="mark">CONSCIOUS  SEDATION 1ST 30 MIN/2473</span>

 4  <span class="mark">CONSCIOUS  SEDATION, FIRST 30 MIN INTRA-SERVICE TIME/1934</span>

 5  <span class="mark">CONSCIOUS SED, EACH ADDITIONAL 15 MIN INTRA-SERVICE TIME/1933</span>

 6  <span class="mark">CONSCIOUS SEDATION  (ANGIO)-P/2321</span>

 7  <span class="mark">CONSCIOUS SEDATION  EACH ADDIT 15 MIN/2474</span>

 8  <span class="mark">CONSCIOUS SEDATION (CT) -P/2324</span>

9  <span class="mark">CONSCIOUS SEDATION, 1ST 30 MIN/2388</span>

10  <span class="mark">CONSCIOUS SEDATION, FIRST 30 MIN INTRA-SERVICE TIME/1932</span>

11  <span class="mark">CONSCIOUS SEDATION-P/2762</span>

12  New Procedure

13  None of the above

# Parent Procedures and Inactivation Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not able to associate a Parent Procedure to a Descendent Procedure when creating a Parent Procedure.

Since a Parent Procedure cannot be associated to a Descendent Procedure when the ADPAC is adding/creating a Parent Procedure for the first time the Inactivation date will default to Todays Date.

In order to associate a Parent Procedure to a Descendent Procedure the ADPAC will have to edit the Parent Procedure. In the edit session of the Parent Procedure the ADPAC will be able to associate Descendent Procedures to the Parent Procedure.

Once the Descendent Procedures have been associated to the Parent Procedure the ADPAC will have to delete the Inactivation date. This is done by entering an ‘@’ sign at the Inactivation Date prompt.

<span id="_Toc479074046" class="anchor"></span>Figure : Creating a Parent Procedure

RAD/NUC MED PROCEDURES NAME: <span class="mark">TEST PARENT 1</span>

Select one of the following:

1 New Procedure

2 None of the above

Enter a number from the list above: 1 New Procedure

TYPE OF PROCEDURE: P PARENT

NAME: TEST PARENT 1//

TYPE OF IMAGING: CT SCAN

TYPE OF PROCEDURE: PARENT//

SINGLE REPORT: Y YES

HEALTH SUMMARY WITH REQUEST:

Select SYNONYM:

RAD/NM PHYS APPROVAL REQUIRED: NO// NO

Select MESSAGE:

EDUCATIONAL DESCRIPTION:

1\>

INACTIVATION DATE: APR 3,2017// (APR 03, 2017)

This procedure was not created as a DETAILED exam and will not be matched

to the MASTER RADIOLOGY PROCEDURE FILE.

Temporary new procedure entry has been moved to the permanent

RAD/NUC MED PROCEDURE file.

Inactivating this parent procedure - no descendents.

Updating ORDERABLE ITEMS file

Deleting temporary entry in file 71.11

Want to run a validity check on CPT and stop codes? NO//

<span id="_Toc479074047" class="anchor"></span>Figure : Editing a Parent Procedure, adding a Descendent Procedure, and removing the Inactivation Date

RAD/NUC MED PROCEDURES NAME: <span class="mark">TEST PARENT 1</span>

NAME: TEST PARENT 1//

TYPE OF IMAGING: CT SCAN//

TYPE OF PROCEDURE: PARENT//

SINGLE REPORT: YES//

HEALTH SUMMARY WITH REQUEST:

Select SYNONYM:

RAD/NM PHYS APPROVAL REQUIRED: NO//

Select MESSAGE:

Select DESCENDENTS: <span class="mark">CT</span>

1 CT ABDOMEN W&W/O CONT (CT Detailed) CPT:74170

2 CT ABDOMEN W/CONT (CT Detailed) CPT:74160

3 CT ABDOMEN W/O CONT (CT Detailed) CPT:74150

4 CT ABDOMINAL PARACENTESIS (SURGICAL CODE) (CT Detailed) CPT:49080

5 CT ANGIO CHEST W&W/O CONT (CT Detailed) CPT:71275

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 2 <span class="mark">CT ABDOMEN W/CONT</span> (CT Detailed) CPT:74160

Are you adding 'CT ABDOMEN W/CONT' as a new DESCENDENTS? No// Y (Yes)

Select DESCENDENTS:

EDUCATIONAL DESCRIPTION:

1\>

INACTIVATION DATE: APR 3,2017// <span class="mark">@</span>

SURE YOU WANT TO DELETE? Y (Yes)

Running validity check on CPT and stop codes.

This option prints a list of Radiology/Nuclear Medicine Procedures

with missing or invalid CPT's and DSS ID's, and Imaging Locations

pointing to Hospital Locations with inappropriate set-up parameters.

Broad, parent and inactive procedures are not required to have codes.

To be valid, DSS ID's must be in the Imaging Stop Codes file 71.5;

CPT's must be nationally active.

Include Inactive Procedures? NO// ^

# Conclusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The look and feel of the Procedures List when displayed has been altered.

The RA\*5\*127 patch is a Radiology application patch. This patch contains Data Definition and routine updates needed for managing the association of in the RAD/NUC MED PROCEDURES file (# 71).

The Display of the Procedure List appears differently from the display prior to this new radiology patch. This change is due to the VA Business Owners decisions to provide more of the procedure name on the display, resulting in removing the imaging type and CPT codes from being display within the Procedure List. There are a limited number of characters to display information on the screen.

In order for the Radiology ADPAC to have visibility to the Image Type, it is required that each procedure impacted by the annual code changes be manually updated to reflect an abbreviated version of the Image Type within the title of the procedure.

<u>IMPORTANT NOTE:</u> VAMC Annual update of CPT Codes is a once a year work effort. After these procedures are updated, the added information will be visible going forward.

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Radiology Informational Patch RA\*5\*134

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: FEB 12, 2017 Designation: RA\*5\*134 TEST v1

Package : RADIOLOGY/NUCLEAR MEDICINE Priority : MANDATORY

Version : 5 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (u)RA\*5\*127 \<\<= must be installed BEFORE \`RA\*5\*134'

Subject: RADIOLOGY INFORMATIONAL UPDATE PATCH FOR NTRT

Category: INFORMATIONAL

Description:

===========

This is an INFORMATIONAL patch that is a follow on to patch

RA\*5.0\*127. This patch includes instructions to manually change

field \#9 SEEDING COMPLETE in the Radiology MASTER RADIOLOGY SITE

File (71.98) from N to Y.

<span class="mark">This patch should not be exercised until the content of the</span>

<span class="mark">MASTER RADIOLOGY PROCEDURE file (#71.99) has been deployed.</span>

<span class="mark">When the content of the MASTER RADIOLOGY PROCEDURE file (#71.99)</span>

<span class="mark">has been deployed the NTRT group sends a message to the</span>

<span class="mark">NTRT_NOTIFICATION-L listserv.</span>

<span class="mark"></span>

<span class="mark">The ADPAC for the facility shall subscribe to this list using the</span>

<span class="mark">following web site: http://vaww.listserv.va.gov/scripts/wa.exe. The</span>

<span class="mark">NTRT group does not own the List Serve application. The List Serve</span>

<span class="mark">is a VA service. The ADPAC will need to create an account using a</span>

<span class="mark">username and password that does NOT synchronize with the ADPAC's</span>

<span class="mark">VA network account.</span>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DO NOT CHANGE ANY VALUES EXCEPT FOR field \#9 SEEDING COMPLETE.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CHANGE INSTRUCTIONS:

==========================

Systems Installer (OI&T):

Verify that the MASTER RADIOLOGY PROCEDURE file (#71.99) (MRPF)

has been populated with data. The pre-deployment MASTER RADIOLOGY

PROCEDURE file (#71.99) will contain nine (9) entries.

<span class="mark">ADPAC:</span>

<span class="mark">Do not continue until The system installer has verified that the</span>

<span class="mark">MASTER RADIOLOGY PROCEDURE file (#71.99) (MRPF) content has been</span>

<span class="mark">deployed to your facility</span>.

Navigate to the Radiology Supervisor menu.

Suggested method is:

Menu Path: Core Applications -\> Rad/Nuc Med Total System Menu

-\> Press "Enter Key" to select a "Sign on Imaging Location"

-\> Supervisor menu.

Select SEED Master Procedure file seeding Complete.

At the prompt SEEDING COMPLETE: NO// enter 'Y' to change the

value from NO to YES. This will allow request messages to

be sent when a new Radiology Procedure is created and has not

been associated to the MASTER RADIOLOGY PROCEDURE file (#71.99).

Press \<ENTER\> to return to the Supervisors menu.

You may exit the Supervisors menu at this time.

Routine Information:

====================

No routines included.

=============================================================================

User Information:

Entered By : <span class="mark">REDACTED</span> Date Entered : JAN 25,2017

Completed By: Date Completed:

Released By : Date Released :

=============================================================================