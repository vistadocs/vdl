---
title: Radiology Version 5 ADPAC Guide Addendum
doc_type: UG
doc_label: Manager/ADPAC Guide
doc_layer: anchor
doc_subject: ADPAC Guide Addendum
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
description: "<table> <caption><p>Table . Radiology Supervisor Menu Options and Descriptions</p></caption> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 12%\\" /> <col style=\\"width: 38%\\" /> <col style=\\"width: 35%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Revision</th> <th>Description<"
audience: 
keywords: 
  - procedure
  - span
  - procedures
  - edit
  - patch
  - radiology
  - mrpf
  - mark
  - class
  - table
page_count: 0
word_count: 7697
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra_5_aa_1.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra_5_aa_1.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

---
title: |
  Collaborative Terminology Tooling & Data Management (CTT & DM)

  Native Domain Standardization (NDS)
---

Radiology Reports

Automated Data Processing Application Coordinator (ADPAC) Addendum

![](radiology-version-5-adpac-guide-addendum/001.png)

May 2017

Department of Veterans Affairs (VA)

Revision History

<table>
<caption><p>Table . Radiology Supervisor Menu Options and Descriptions</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 38%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5/31/2017</td>
<td>1.1</td>
<td>Delivery to VA</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/31/2017</td>
<td>1.02</td>
<td>Technical Writer Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>4/13/2017</td>
<td>1.01</td>
<td><p>Update Content to support :</p>
<p>MRPF selection screen the display needs to be changed from ‘/’ to ‘~’. This is to accommodate the potential usage of forward slashes in the MRPF name. Added Appendix with Patch Desc 139 and 140.</p>
<p>(Accepted changes and added Appendix A - Patch descriptions )</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/24/2017</td>
<td>1.0</td>
<td>Delivery to VA</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/21/2017</td>
<td>0.95</td>
<td>Technical Writer Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/15/2017</td>
<td>0.9</td>
<td>Updated Content to support MRPF Association; included patches released, added content related to Mailman Messages.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/11/2016</td>
<td>0.8</td>
<td>Minor mods of screen content</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/27/2016</td>
<td>0.7</td>
<td>Stakeholder Feedback Incorporated</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/25/2016</td>
<td>0.6</td>
<td>Distribution for Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/7/2016</td>
<td>0.5</td>
<td>Technical Writer Review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/6/2016</td>
<td>0.4</td>
<td>Tester Review - updates</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/6/2016</td>
<td>0.3</td>
<td>Developer Review - updates</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/28/2016</td>
<td>0.2</td>
<td>Added screen scrapes</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/1/2016</td>
<td>0.1</td>
<td>Initial draft – Provided process &amp; content.</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table . Radiology Supervisor Menu Options and Descriptions

Table of Contents

Table of Figures

# Documentation Conventions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Documentation Conventions](#documentation-conventions)
- [Assumptions](#assumptions)
- [Radiology/Nuclear Medicine New Procedure Process Workflow](#radiologynuclear-medicine-new-procedure-process-workflow)
  - [Master Radiology Procedure File (MRPF) Update Process – Adding new Radiology Procedures](#master-radiology-procedure-file-mrpf-update-process-adding-new-radiology-procedures)
  - [Related Patches](#related-patches)
    - [XU\8\666](#xu8666)
    - [HDI\1.0\16](#hdi1016)
    - [RA\5\127](#ra5127)
    - [RA\5\134](#ra5134)
    - [RA\5.0\140](#ra50140)
    - [RA\5.0\138](#ra50138)
  - [NTRT Process](#ntrt-process)
  - [Radiology Menu Options and Descriptions](#radiology-menu-options-and-descriptions)
- [ADPAC Procedures](#adpac-procedures)
  - [AON - Edit MRPF Association on One Procedure](#aon-edit-mrpf-association-on-one-procedure)
  - [ASC - Associating a Local Procedures to MRPF File](#asc-associating-a-local-procedures-to-mrpf-file)
  - [LNC - Enter/Edit LOINC for One Procedure](#lnc-enteredit-loinc-for-one-procedure)
  - [PIN - Print Active Procedures with inactive CPT/LOINC](#pin-print-active-procedures-with-inactive-cptloinc)
  - [SEED - Master Procedure File Seeding Complete](#seed-master-procedure-file-seeding-complete)
- [On Demand Report](#on-demand-report)
- [APPENDIX A – PATCH DESCRIPTIONS](#appendix-a-patch-descriptions)
  - [Patch RA\5\138](#patch-ra5138)
  - [Patch RA\5\140](#patch-ra5140)
This manual uses several methods to highlight different aspects of the material:
- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a non-proportional font and enclosed within a box.
- User’s responses to online prompts are bold typeface, underlined and highlighted in yellow (e.g., <span class="mark">\<<u>Enter</u>\></span>).
- Emphasis within a dialogue box is bold typeface, underlined and highlighted in blue (e.g., <span class="mark"><u>STANDARD LISTENER: RUNNING</u></span>).
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
- Radiology Information Manager functions

# Radiology/Nuclear Medicine New Procedure Process Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process for adding a new procedure to the MRPF file is described below in the process flow diagram.

<span id="_Toc484003454" class="anchor"></span>Figure : Radiology/Nuclear Medicine New Procedure Process Workflow

![](radiology-version-5-adpac-guide-addendum/002.png)

## Master Radiology Procedure File (MRPF) Update Process – Adding new Radiology Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Until all of the patches listed in the ‘Related Patches’ section are installed and the ‘Master Radiology Procedure file (MRPF) (#71.99)’ data content has been deployed to your facility, the ADPAC will not have the ability to interact with the MRPF and the following options should not be exercised.

The Master Radiology Procedure file (MRPF) (#71.99) will need to be populated by a terminology team under the direction of the VHA Radiology Program Office before deployment, and will be done independently of the development effort. It is recommended that the initial seeding include the most common procedures based on frequency of use as all undefined procedures will be pushed through the New Term Rapid Turnaround (NTRT) process.

1.  Initial association of procedures in the RAD/NUC MED Procedure file (#71) to the Master Radiology Procedure file (MRPF) (#71.99) will need to be done by the Automated Data Processing Application Coordinator (ADPAC) managers at each facility.
2.  Upon the entry of a new procedure an NTRT request will be automatically launched if an MRPF is not chosen for the given procedure CPT code. The ADPAC will be able to use the procedure in the interim while the NTRT team evaluates the new MRPF term that will be used for the procedure.
3.  An NTRT Exception flag will be set and added to the given procedure in RAD/NUC MED Procedure File (#71) when a new procedure has been submitted to NTRT for processing.
4.  The Creation Date of the new procedure shall be captured and added to the RAD/NUC MED Procedure File (#71) when a new procedure is added.
5.  Upon completion of the NTRT evaluation for the given new procedure entered by ADPAC that requires an MRPF entry, this procedure will be added to the Master Radiology Procedure file (MRPF) (#71.99) and pushed out to the individual facilities.
6.  If the search result identifies that an equivalent procedure already exists within the Master Radiology Procedure file (MRPF) (#71.99), the creation request will be rejected and a notification is displayed to the requesting ADPAC including the specific MRPF term and the procedure it is associated with.
7.  On demand reports will be made available to VHA Radiology Program Office for providing beneficial views of procedures and MRPF associations.
8.  The local site’s Read Mail (RML) mail group will be utilized for email notifications relating to NTRT and the creation of new procedures.

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The related patches for this effort are as follows:

### XU\*8\*666

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XU\*8\*666 patch is a required Kernel system patch. This patch is used by the STS group when deploying content for the MASTER RADIOLOGY PROCEDURE FILE (#71.99)

### HDI\*1.0\*16

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEALTH DATA & INFORMATICS (HDI) patch HDI\*1.0\*16 is a required HDI patch. This patch registers the MASTER RADIOLOGY PROCEDURE FILE (71.99) into the HDI system. The HDI system manages the VA Unique Identifier (VUID) numbering and is invoked during the STS content deployment.

### RA\*5\*127

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA\*5\*127 patch is a Radiology application patch. This patch contains Data Definition and routine updates needed for managing the association of in the RAD/NUC MED PROCEDURES file (# 71).

### RA\*5\*134

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA\*5\*134 is an INFORMATIONAL patch and contains information for after installing patch RA\*5\*127 and after the MASTER RADIOLOGY PROCEDURE file (#71.99) is deployed to your facility this associated follow on informational patch (RA\*5.0\*134) should be installed. The informational patch provides instructions for turning on the sending of NTRT messages to the NTRT group.

### RA\*5.0\*140

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA\*5.0\*140 is an INFORMATIONAL Patch and contains work around information for defects identified with the release of RA\*5\*127. If you are using RA\*5\*127 please review the patch description for RA\*5.0\*140. Once patch RA\*5.0\*138 is installed the defects will be resolved.

### RA\*5.0\*138

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA\*5.0\*138 patch resolves the deficiencies identified from patch RA\*5\*127. Please review the patch description for RA\*5.0\*138.

## NTRT Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The items below describe the NTRT process for newly added local facility procedures that were not associated with the MRPF when a procedure is created.

This process will be activated after the MASTER RADIOLOGY PROCEDURE FILE (#71.99) content has been deployed, and the sending of NTRT messages is activated.

NTRT messages will not be sent for procedures that were created prior to the MRPF content deployment and the sending of NTRT messages being activated.

An NTRT message will be sent if a procedure is not associated to the MRPF during the Enter / Edit of a RAD/NUC MED Procedure file (#71).

A mailman message is sent to the Radiology NTRT mail group.

- An STS analysts passes this information on to the Radiology SME group who will decide whether to:
1.  Add a new PROCEDURE NAME entry to the MRPF to the national radiology standard; or
2.  Suggest a mapping to an existing radiology procedure name entry in the MRPF.
- Once the SMEs have made a decision, an STS analyst will reply to the email address that was included in the auto email. The email address is the facilities RADNTRT mailman address. The email will describe the Radiology SME decision.
- If the SME’s decision was to suggest a mapping to an existing procedure, already part of the national standard, this is the end of the process. Otherwise
- If the SMEs authorize a new procedure, that work goes to an STS analyst to create the procedure in the STS database. The new procedure goes through several layers of validation, acquires SQA approval, and is deployed to all national production sites. This process takes between 1-2 weeks.
- When a deployment is complete, STS sends a message to the NTRT_NOTIFICATION-L listserv.
- The ADPAC for the facility shall subscribe to this list using the following web site: <span class="mark">REDACTED</span>. (STS does not own this application; it's a VA service. The ADPAC will need to create an account using a username and password that does NOT synchronize with the ADPAC's VA network account.)

## Radiology Menu Options and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Table 1. Radiology Supervisor Menu Options contain the Radiology Supervisor MENU option name, option letter, and a brief description of the option functions.

| Menu Option Name                                | Option Synonym | Description                                                                                                                                                                                                                                               |
|-------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Edit MRPF Association on One Procedure          | AON            | Edit MRPF Association on One Procedure.                                                                                                                                                                                                                   |
| Associate Local Procedures to MRPF              | ASC            | This option allows you to associate the local procedures to the Master Radiology Procedure File.                                                                                                                                                          |
| Enter/Edit LOINC for one procedure              | LNC            | Enter/Edit LOINC for one procedure                                                                                                                                                                                                                        |
| Print Active Procedures with Inactive CPT/LOINC | PIN            | Report. This report option prints the active procedures with inactive CPT/LOINC codes                                                                                                                                                                     |
| Master Procedure file seeding Complete          | SEED           | The populating of the Master Radiology Procedure (MRPF) file is called seeding. This option indicates if the seeding is complete. Note: Seeding pertains to the STS effort to send the MRPF to a facility. This is not associated to the matching process |

Radiology Supervisor Menu Options and Descriptions.

[<u>IMPORTANT NOTE (1):</u>](#asc---associating-a-local-procedures-to-mrpf-file) The MASTER RADIOLOGY PROCEDURE FILE (#71.99), will not be populated prior to the application patch installation. Therefore, the functions related to menu option ‘ACS’ Associate Local Procedures to MRPF will not be functional until content of the MRPF is provided.  In the future, the NTRT team will populate and deploy the MRPF file for all sites.

Prior to the population of the MRPF, creation of a new procedure in file (# 71) will generate a Read Mail (RML) mailman message to the Radiology ADPAC entering a new procedure. Because the functionality to forward that message on to the NTRT team has not yet been turned on, sites should ignore these messages.

IMPORTANT NOTE (2):

Upon Enter/Edit of a procedure, the lookup of a procedure with the capability of utilizing the CPT Code is no longer applicable. The ADPAC is required to enter the Procedure or partial Procedure name for this function.

# ADPAC Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [AON – Edit MRPF Association on One Procedure](#_AON_-_Edit)
- [ASC – Associating a Local Procedures to MRPF File](#asc---associating-a-local-procedures-to-mrpf-file)
- [LNC – Enter/Edit LOINC for One Procedure](#lnc---enteredit-loinc-for-one-procedure)
- [PIN – Print Active Procedures with inactive CPT/LOINC](#_PIN_-_Print)
- [SEED – Master Procedure File Seeding Complete](#_SEED_-_Master)

## AON - Edit MRPF Association on One Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type AON – to select the Edit MRPF Association on One Procedure option; press \<Enter\>, as shown in Figure 2. Radiology Supervisor Menu – AON Option.

<span id="_Ref455573476" class="anchor"></span>Figure . Radiology Supervisor Menu – AON Option

HL7 Radiology HL7 Menu...

<span class="mark">AON</span> Edit MRPF Association on One Procedure <span class="mark"><u>\<Enter\></u></span>

ASC Associate Local Procedures to MRPF

LNC Enter/Edit LOINC for one procedure

PIN Print Active Procedures with inactive CPT/LOINC

SEED Master Procedure file seeding Complete

9.  Enter the procedure to be edited, press \<Enter\>, as shown in [Figure 3. OAN – Edit MRPF Association on One Procedure](#_Ref455573605) .

<span id="_Ref455573605" class="anchor"></span>Figure . AON - Edit MRPF Association on One Procedure

<span class="mark">CLT TEST4 (RAD Detailed) CPT:74000</span>, <span class="mark">\<Enter\></span>

Enter the MRPF to Associate with the Selected Procedure: ??

Choose from:

KNEE 3 VIEWS

Enter the MRPF to Associate with the Selected Procedure: Knee 3 VIEWS

10. Procedure CLT TEST4 is now associated to MRPF KNEE 3 VIEWS. If additional local procedures are to be mapped to MRPF, the User can continue to with the entry of procedures. If there are no more procedures to be mapped, User will PRESS ENTER.

## ASC - Associating a Local Procedures to MRPF File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type ASC to select the Supervisor Menu Option: ASC -Associate Local Procedures to MRPF, press \<Enter\>, as shown in Figure 4. Radiology Supervisor Menu – ASC Option

<span id="_Ref455573554" class="anchor"></span>Figure . Radiology Supervisor Menu – ASC Option

HL7 Radiology HL7 Menu...

AON Edit MRPF Association on One Procedure

<span class="mark">ASC</span> Associate Local Procedures to MRPF <span class="mark"><u>\<Enter\></u></span>

LNC Enter/Edit LOINC for one procedure

PIN Print Active Procedures with inactive CPT/LOINC

SEED Master Procedure file seeding Complete

11. Select the number of the Master Procedure that best matches, or enter a number followed by 'C' for the long name. e.g.: 1C: 1 US GUIDANCE FOR THORACENTESIS/ECHO GUIDE FOR BIOPSY, as shown in Figure 5. ASC - Associate Local Procedures to MRPF File – Step 1.
12. Press \<ENTER\> to continue or '^' to quit.: Continue//.

<span id="_Ref455574334" class="anchor"></span>Figure . ASC - Associate Local Procedures to MRPF File – Step 1 Single Choice

PROCEDURE NAME: ANGIO, EXTERNAL CAROTID, UNILAT SELECTIVE Replace

CPT CODE: 76942

Select one of the following:

1 US GUIDANCE FOR THORACENTESIS~ECHO GUIDE FOR BIOPSY

2 NONE LISTED

13. Select the number of the Master Procedure that best matches, or enter a number followed by 'C' for the long name. e.g. 1C: 2 NONE LISTED, as shown in. <u>Figure 6. ASC - Associate Local Procedures to MRPF File – Step 2</u>. (If a new CPT code is not entered the default code (75660) will be the selection.)
14. Press \<ENTER \> to continue or '^' to quit.: Continue//

<span id="_Ref455575627" class="anchor"></span>Figure . ASC - Associate Local Procedures to MRPF File – Step 2 No Choices

NAME: ANGIO, VERTEBRAL, CERVICAL &/OR INTRACRANIAL

CPT CODE: 78215

Select one of the following:

1 NONE LISTED

15. Select the number of the Master Procedure that best matches, or enter a number followed by 'C' for the long name. e.g. 1C: 1 NONE LISTED, as shown in <u>Figure 7. ASC - Associate Local Procedures to MRPF File – Step 3</u>.

<span id="_Ref455576018" class="anchor"></span>Figure . ASC - Associate Local Procedures to MRPF File – Step 3 Multiple Choices

NAME: ANGIOGRAM CONSULTATION

CPT CODE: 76705

Select one of the following:

1 US RUQ~ECHO EXAM OF ABDOMEN

2 US SPLEEN~ECHO EXAM OF ABDOMEN

3 US AORTA~ECHO EXAM OF ABDOMEN

4 NONE LISTED

16. Select the number of the Master Procedure that best matches or enter a number followed by 'C' for the long name. e.g. 1C: 2 US SPLEEN/ECHO E XAM OF ABDOMEN, as shown in Figure 8. ASC - Associate Local Procedures to MRPF File – Step 4.

<span id="_Ref455576617" class="anchor"></span>Figure . ASC - Associate Local Procedures to MRPF File – Step 4

The MRPF procedure US SPLEEN~ECHO E XAM OF ABDOMEN is already mapped to your procedure TRANS CATH PLACEMENT OF INTRAVASCULAR STENT, OPEN, INITIA

17. L.Press \<RETURN\> to continue or '^' to quit.: Continue//
18. The user should write down the procedure that was rejected (US SPLEEN~ECHO E XAM OF ABDOMEN) so they can use AON to match it.

A successful selection should be shown and also the display when the ‘C’ is in the selection (i.e. 2C)

## LNC - Enter/Edit LOINC for One Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type LNC to select the Supervisor Menu Option: LNC Enter/Edit LOINC for one procedure, press \<Enter\>, as shown in Figure 9. Radiology Supervisor Menu – LNC Option.

<span id="_Ref455576669" class="anchor"></span>Figure . Radiology Supervisor Menu – LNC Option

HL7 Radiology HL7 Menu...

AON Edit MRPF Association on One Procedure

ASC Associate Local Procedures to MRPF

<span class="mark">LNC</span>Enter/Edit LOINC for one procedure <span class="mark">\<<u>Enter</u>\></span>

PIN Print Active Procedures with inactive CPT/LOINC

SEED Master Procedure file seeding Complete

2.  Select the RAD/NUC Procedure Name, press \<Enter\>, as shown in <u>Figure 10. LNC - Enter/Edit LOINC for One Procedure</u>

> **NOTE:** The entry of a LOINC code in file 71 will not update the associated MRPF entry.

Only STS makes changes to the MRPF. Quality control is a local facility function.

<span id="_Ref455576724" class="anchor"></span>Figure . LNC - Enter/Edit LOINC for One Procedure

Select RAD/NUC MED PROCEDURES NAME: CLT TEST4 (RAD Detailed) CPT:74000

LOINC: 123456-7

## PIN - Print Active Procedures with inactive CPT/LOINC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type PIN to select the Supervisor Menu Option: PIN Print Active Procedures with inactive CPT/LOINC, as shown in <u>Figure 11. Radiology Supervisor Menu – PIN Option.</u>

<span id="_Ref455576791" class="anchor"></span>Figure . Radiology Supervisor Menu – PIN Option

HL7 Radiology HL7 Menu...

AON Edit MRPF Association on One Procedure

ASC Associate Local Procedures to MRPF

LNC Enter/Edit LOINC for one procedure \<Enter\>

<span class="mark">PIN</span> Print Active Procedures with inactive CPT/LOINC <span class="mark">\<<u>Enter</u>\></span>

SEED Master Procedure file seeding Complete

The Active Procedures with inactive CPT/LOINC report displays, as shown in <u>Figure 12. Active Procedures with inactive CPT/LOINC</u>.

19. Press \<ENTER\> to continue or '^' to quit.

<span id="_Ref455566268" class="anchor"></span>Figure . Active Procedures with inactive CPT/LOINC Report

QUEUE ON DEVICE(80 COLUMN): HOME// DEC Windows Right Margin: 80//

ACTIVE RADIOLOGY PROCEDURES PAGE 1

WITH INACTIVE CPT CODE OR MRPF LOINC

PROCEDURE NAME CPT CODE INAC DT MRPF NAME INAC DT

ABDOMEN 1 VIEW 74022 6/9/16

ABDOMEN 2 + PA & LAT 74022 6/9/16

ABDOMEN 2 + PA & LAT UNPROCEDURE 5/1/16@10:00

ABDOMEN 2 + PA CHEST 74022 6/9/16

ABDOMEN 2 VIEWS 74022 6/9/16

ABDOMEN 3 OR MORE VI 74022 6/9/16

ABDOMEN MIN 3 VIEWS+ 74022 6/9/16

ABDOMEN-KUB 74022 6/9/16

ABSCESS LOCALIZATION 74022 6/9/16

ADRENAL IMAGING, COR 74022 6/9/16

ADRENAL IMAGING, COR UNPROCEDURE 5/1/16@10:00

ANGIO ADRENAL BILAT 74022 6/9/16

ANGIO ADRENAL UNILAT 74022 6/9/16

<span class="mark">Enter \<RETURN\></span> to continue or '<span class="mark">^</span>' to quit:

## SEED - Master Procedure File Seeding Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type SEED to select the Supervisor Menu Option: SEED - Master Procedure file seeding Complete, as shown in <u>Figure 13. Radiology Supervisor Menu – SEED Option</u>
20. Press \<Enter\>.

<span id="_Ref455576206" class="anchor"></span>Figure . Radiology Supervisor Menu – SEED Option

HL7 Radiology HL7 Menu...

AON Edit MRPF Association on One Procedure

ASC Associate Local Procedures to MRPF

LNC Enter/Edit LOINC for one procedure \<Enter\>

PIN Print Active Procedures with inactive CPT/LOINC

<span class="mark">SEED</span> Master Procedure file seeding Complete <span class="mark">\<<u>Enter</u>\></span>

21. Type \<No\> or \<Yes\> to indicate if seeding is complete, as shown in <u>Figure 14. Radiology Seeding</u>.

<span id="_Ref455576383" class="anchor"></span>Figure . Radiology Seeding

The populating of the MASTER RADIOLOGY PROCEDURE file is called seeding.

SEEDING COMPLETE: NO// YES

22. When the seeding is complete the system will now begin to notify NTRT when a new procedure is entered.

# On Demand Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is intended for use by the program office. This on demand report allows for monitoring the individual site changes within file RAD/NUC MED PROCEDURE file (#71) per usable selectable date range. When inputting the date range, provide a date range that will included relevant new procedures made while testing this patch.

The report is requested by sending a Mailman message using the following menu path:

Menu Path: Mailman Menu SML Send Mailman message

<span class="mark">Include Subject: RADIOLOGY ON DEMAND</span>

<span class="mark">Include Line 1: BEGIN DATE:1/1/2016</span>

<span class="mark">Include Line 2: END DATE:1/18/2016</span> “(Use Current Date)”

<span class="mark">Include Line 3: RESPOND TO:YOUR EMAIL ADDRESS (FORUM or VA OUTLOOK)</span>

For Example:

RESPOND TO:Recipient@STLVETSDEV.FO-BAYPINES.MED.VA.GOV or Recipient@VA.GOV

<span class="mark">SEND MAIL TO:S.RADIOLOGY ON DEMAND@(Site location)</span>

For Example:

S.RADIOLOGY ON <DEMAND@STLVETSDEV.FO->BAYPINES.MED.VA.GOV

View the requested report in your VA Outlook or in Mailman using the following path:

Menu Path: Mailman Menu RML Read/Manage Messages Input the number of the last message received in your inbox (The message may take some time to compile and populate into your Mailman inbox)

<span class="mark">Subj: ON DEMAND REPORT \[#451195\] 12/08/16@16:15 89 lines</span>

<span class="mark">From: POSTMASTER In 'IN' basket. Page 1</span>

<span class="mark">-------------------------------------------------------------------------------</span>

<span class="mark">On demand report for 01/01/2016 through 11/11/2016</span>

<span class="mark">For ST. LOUIS MO VAMC-JC DIVISION</span>

<span class="mark">PROCEDURE CREATED MATCHED</span>

<span class="mark">========= ========== =======</span>

<span class="mark">CLT TEST4 Yes</span>

<span class="mark">CLT TEST5 No</span>

<span class="mark">NEWTEST7-7-2016 No</span>

<span class="mark">SEEDOFFTEST7-13 Yes</span>

<span class="mark">SEEDOFFTEST7-13 3 No</span>

<span class="mark">SEEDONTEST7-13 07/13/2016 No</span>

# APPENDIX A – PATCH DESCRIPTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch RA\*5\*138

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: APR 12, 2017 Designation: RA\*5\*138 TEST v1

Package : RADIOLOGY/NUCLEAR MEDICINE Priority : MANDATORY

Version : 5 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)RA\*5\*127 \<\<= must be installed BEFORE \`RA\*5\*138'

Subject: NDS FOLLOWUP TO RA\*5.0\*127

Category: DATA DICTIONARY

ROUTINE

INPUT TEMPLATE

Description:

===========

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\* Please install/re-install released patch RA\*5.0\*127 \*\*

\*\* immediately prior to installing this patch to ensure \*\*

\*\* all routine and data dictionary dependencies exist, and \*\*

\*\* have not been backed out or modified. \*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patch RA\*5.0\*138 corrects defects introduced by patch RA\*5.0\*127 that

adversely affect the Procedure Enter/Edit \[RA PROCEDURE\] option.

Issues with the Procedure Enter/Edit \[RA PROCEDURE\] option that are

addressed by this patch:

\* An undefined error, "\<UNDEFINED\>DIRB+3^DIR \*X", may occur if a

user attempts to add a duplicate procedure name surrounded by

double quotes at the 'RAD/NUC MED PROCEDURE NAME:' prompt.

\* Missing question mark ("?" and "??") lookup/help functionality

at the 'RAD/NUC MED PROCEDURE NAME:' prompt.

\* Procedures can no longer be looked up by CPT code at the 'RAD/NUC

MED PROCEDURE:' prompt.

\* An undefined error, "\<UNDEFINED\>BR+1^DIE0 \*RANEW", may occur

when editing a procedure with a forward slash ("/") in its name.

\* When performing a procedure lookup at the 'RAD/NUC MED PROCEDURE

NAME:' prompt, the TYPE OF IMAGING value no longer displays next to

each entry.

\* An undefined error, "\<UNDEFINED\>21+12^RAMAIN2 ^RAMIS(71,-1,0)"

may occur when a procedure lookup is done at the 'RAD/NUC MED

PROCEDURE NAME:' prompt and two or more matching entries with the same

name exist in the RAD/NUC MED PROCEDURE (#71) file.

\* Incorrect entries are returned at the 'DESCENDENTS:' prompt when

a user performs a lookup by entering a partial procedure name or

question mark.

Related Patches

---------------

RA\*5.0\*127

Bulletins

---------

N/A

Files & Fields Associated:

--------------------------

New/Modified

File Name (#) Field Name (#) /Deleted

--------------------------------- ------------------ -------------

NEW RAD PROCEDURE WORKUP (#71.11) DESCENDENTS (#300) Modified

Forms Associated:

-----------------

N/A

Mail Groups Associated:

-----------------------

N/A

Options Associated:

-------------------

N/A

Protocols Associated:

---------------------

N/A

Security Keys Associated:

-------------------------

N/A

Templates Associated:

---------------------

Template Name Type File Name (Number) New/Modified/Deleted

------------- ----- ------------------ --------------------

NEW RAD PROCEDURE INPUT NEW RAD PROCEDURE Modified

WORKUP (#71.11)

RA PROCEDURE EDIT INPUT RAD/NUC MED Modified

PROCEDURES (#71)

New Service Requests (NSRs):

----------------------------

N/A

Patient Safety Issues (PSIs):

-----------------------------

None

Defect Tracking & Overview:

=============================

Associated Defect(s):

----------------------

Defect \#492278 - When trying to enter an additional duplicate procedure

name to the RAD/NUC MED PROCEDURES (#71) file using quotes, an M error

occurs.

Defect \#492546 - An M error occurs during procedure lookup when procedure

has two or more exact matches in the RAD/NUC MED PROCEDURES (#71) file.

Defects \#492274, \#492272, \#492270 - When doing a partial name lookup at

the DESCENDENTS prompt, entries matching the wrong Imaging Type are

returned, resulting in an inability to add the correct Descendent to

Parent procedure, and an Inactivation Date to incorrectly default into new

Parent procedures.

Defect \#486891 - As a result of Patch RA\*5.0\*127 Native Domain

Standardization Radiology Reporting imaging locations no longer show next

to procedures in procedure entry/edit.

Defect \#493698 - An M error occurs when running the Invalid Procedure

List.

Defect \#492268 - When using the Procedures Enter/Edit \[RA PROCEDURE\]

option, procedures lookup by CPT code is no longer available.

Defect 487927 - At the RAD/NUC MED PROCEDURES NAME prompt, entering

question marks returns "?? Answer must be 1-60 characters in length." In

the past, entering question marks returned an alphabetical list of

procedures.

Test Sites:

----------

TBD

Overview:

===============

Issue 1

==========================================================================

Defect \#492278 - When trying to enter an additional duplicate procedure

name to the RAD/NUC MED PROCEDURES (#71) file using quotes, an M error

occurs.

Problem:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a procedure name that exactly or

partially matches an existing entry in the RAD/NUC MED PROCEDURES

(#71) file may no longer be added by surrounding the procedure name with

double quotes. Instead of a prompt to add the new entry, the following M

error occurs: "\<UNDEFINED\>DIRB+3^DIR \*X".

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: "MANDIBLE"

K:X\[""""!(\$A(X)=45) X S:\$D(X) X=\$\$UP^XLFSTR(X) Q:(X="^")!\$D(DTOUT)

K:\$L(X)\>60!( \$L(X)\<3) X I \$D(X) K:'+\$\$UNI30^RAUTL14(+\$G(DA),X) X

\<UNDEFINED\>DIRB+3^DIR \*X

Resolution:

--------------

When entering a procedure name surrounded by quotes at the RAD/NUC MED

PROCEDURE Procedure Enter/Edit \[RA PROCEDURE\] option, display a prompt

asking the user if they wish the procedure name (inside the quotes) to be

added as a new procedure.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: "MANDIBLE"

Are you adding MANDIBLE as a new Radiology Procedure? YES//

Issue 2

==========================================================================

Defect \#492546 - An M error occurs during procedure lookup when procedure

has two or more exact matches in the RAD/NUC MED PROCEDURES (#71) file.

Problem:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a procedure name that exactly matches two

or more existing entries in the RAD/NUC MED PROCEDURES (#71) file

results in the following M error: "\<UNDEFINED\>21+12^RAMAIN2

^RAMIS(71,-1,0)".

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: MRI

. S RACPT=\$P(^RAMIS(71,RADA,0),U,9)

^

\<UNDEFINED\>21+12^RAMAIN2 ^RAMIS(71,-1,0)

Resolution:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a procedure name that exactly matches

two or more existing entries in the RAD/NUC MED PROCEDURES (#71) file

results in the display of a numbered, selectable list containing all

exact and partial matches to the user input.

Example:

RAD/NUC MED PROCEDURE NAME: MRI

1 MRI (RAD Detailed) CPT:76499

2 MRI (MRI Inactive) CPT:76499

3 MRI (MRI Inactive) CPT:76499

4 MRI (VAS Detailed) CPT:10121

5 MRI (US Broad )

CHOOSE 1-5:

Issue 3

==========================================================================

Defects \#492274, \#492272, \#492270 - The "DESCENDENTS:" prompt does not

allow eligible procedures to be entered, resulting in a Parent procedure

with no Descendent.

Problem:

--------------

During the process of adding a new Parent procedure in the Procedure

Enter/Edit \[RA PROCEDURE\] option, the "DESCENDENTS:" prompt

searches for and returns descendants with an Imaging Type different than

the Parent procedure, resulting in an inability to add the correct

Descendent to the Parent procedure. An incorrect Inactivation Date is

then automatically stored into the new Parent procedure, because the

Parent has no descendent.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: NEWPAR1

Select one of the following:

1 New Procedure

2 None of the above

Enter a number from the list above: 1 New Procedure

TYPE OF PROCEDURE: P PARENT

NAME: NEWPARENT1//

TYPE OF IMAGING: MRI MAGNETIC RESONANCE IMAGING

TYPE OF PROCEDURE: PARENT//

SINGLE REPORT: ^DESCENDENTS

Select DESCENDENTS: MA

1 MANDIBLE 4 /OR/MORE VIEWS (RAD Detailed) CPT:70110

2 MANDIBLE LESS THAN 4 VIEWS (RAD Detailed) CPT:70100

3 MASTOIDS 3 OR MORE VIEWS/SIDE (RAD Detailed) CPT:70130

4 MASTOIDS LESS THAN 3 VIEWS/SIDE (RAD Detailed) CPT:70120

CHOOSE 1-4:

Resolution:

--------------

During the process of adding a new Parent procedure in the Procedure

Enter/Edit \[RA PROCEDURE\] option , the "DESCENDENTS:" prompt searches

for and returns descendants with the same Imaging Type as the Parent

procedure, resulting in the ability to add the correct Descendent to the

Parent procedure, and no Inactivation Date automatically stored into the

new Parent procedure, because the Parent has an appropriate descendent.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: NEWPAR1

Are you adding NEWPAR1 as a new Radiology Procedure? YES// YES

TYPE OF PROCEDURE: P PARENT

NAME: NEWPAR1//

TYPE OF IMAGING: MRI MAGNETIC RESONANCE IMAGING

TYPE OF PROCEDURE: PARENT//

SINGLE REPORT: ^DESCENDENTS

Select DESCENDENTS: MAG

1 MAGNETIC IMAGE, LUMBAR SPINE (MRI Detailed) CPT:72148

2 MAGNETIC IMAGE,ABDOMEN (MRI Detailed) CPT:74181

3 MAGNETIC IMAGE,BRAIN (MRI Detailed) CPT:70551

4 MAGNETIC IMAGE,BRAIN STEM (MRI Detailed) CPT:70551

5 MAGNETIC IMAGE,LOWER EXTREMITY (MRI Detailed) CPT:73720

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

Issue 4

==========================================================================

Defect \#486891 - As a result of Patch RA\*5.0\*127 Native Domain

Standardization Radiology Reporting imaging locations no longer show next

to procedures in procedure entry/edit.

Problem:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a procedure name partially matching more

than one entry results in a numbered, selectable list that is missing

the TYPE OF IMAGING value next to the procedure name.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: VENOGRAM REN

Select one of the following:

1 VENOGRAM RENAL BILAT SELECT /369

2 VENOGRAM RENAL BILAT SELECT CP/370

3 VENOGRAM RENAL BILAT SELECT S&I/1244

4 VENOGRAM RENAL UNILAT SELECT CP/368

5 VENOGRAM RENAL UNILAT SELECT S&I/1243

6 New Procedure

7 None of the above

Enter a number from the list above:

Resolution:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a procedure name partially matching more

than one entry results in a numbered, selectable list that displays the

TYPE OF IMAGING value next to the procedure name.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: VENOGRAM REN

1 VENOGRAM RENAL BILAT SELECT CP (RAD Inactive) CPT:75834

2 VENOGRAM RENAL BILAT SELECT S&I (RAD Inactive) CPT:75833

3 VENOGRAM RENAL UNILAT SELECT CP (RAD Inactive) CPT:75832

4 VENOGRAM RENAL UNILAT SELECT S&I (RAD Inactive) CPT:75831

CHOOSE 1-4:

Issue 5

==========================================================================

Defect \#493698 - An M error occurs when running the Invalid Procedure

List.

Problem:

--------------

Selection of a procedure name containing a forward slash ("/") at the

"RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit \[RA

PROCEDURE\] option later results in the undefined M error

"\<UNDEFINED\>BR+1^DIE0 \*RANEW" after the "AMIS CODE:" prompt, before the

"CPT:" prompt.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: NEW W

Select one of the following:

1 NEW W/2+/VIEWS/2132

2 New Procedure

3 None of the above

Enter a number from the list above: 1 NEW W/2+/VIEWS/2132

TYPE OF PROCEDURE: D DETAILED

NAME: NEW W//

TYPE OF IMAGING: VASCULAR LAB

TYPE OF PROCEDURE: DETAILED//

CONTRAST MEDIA USED: NO// NO

Select MODALITY:

HEALTH SUMMARY WITH REQUEST:

Select SYNONYM:

PROMPT FOR MEDS:

Select DEFAULT MEDICATION:

Select AMIS CODE:

S:'RANEW Y="@15"

^

\<UNDEFINED\>BR+1^DIE0 \*RANEW

ISRA09:STLVETSDEV 7x2\>

Resolution:

--------------

Selection of a procedure name containing a forward slash ("/") at the

"RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit \[RA

PROCEDURE\] option later does not result in any M errors after the

"AMIS:" prompt.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: NEW

1 NEW W/2+/VIEWS (VAS Broad )

2 NEW W/3+/VIEWS (MRI Detailed) CPT:72159

3 NEWNATETEST4-14 1 (UNKN Unknown )

4 NEWNATETEST5-11 1 (RAD Detailed) CPT:74022

5 NEWPAR TEST1 (VAS Parent )

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 2 NEW W/3+/VIEWS (MRI Detailed) CPT:72159

NAME: NEW W/3+/VIEWS//

TYPE OF IMAGING: MAGNETIC RESONANCE IMAGING//

TYPE OF PROCEDURE: DETAILED//

CONTRAST MEDIA USED: No//

Select MODALITY: AS//

HEALTH SUMMARY WITH REQUEST:

Select SYNONYM:

PROMPT FOR MEDS:

Select DEFAULT MEDICATION:

Select AMIS CODE:

CPT CODE// 72159 (no editing)

Select DEFAULT CPT MODIFIERS(PROC):

STAFF REVIEW REQUIRED: NO//

RAD/NM PHYS APPROVAL REQUIRED: NO//

REQUIRED FLASH CARD PRINTER:

REQUIRED FLASH CARD FORMAT:

Select FILM TYPE:

Select MESSAGE:

EDUCATIONAL DESCRIPTION:

THERE ARE NO LINES!

Edit? NO//

INACTIVATION DATE:

RAD/NUC MED PROCEDURE NAME:

Issue 6

==========================================================================

Defect \#492268 - Procedure lookup by CPT code is no longer available.

Problem:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a CPT code no longer returns any

results, even if there are procedures with matching CPT codes in the

RAD/NUC MED PROCEDURES (#71) file.

Example, lookup CPT 72159 in the Procedure Enter/Edit \[RA PROCEDURE\]

option:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: 72159

Select one of the following:

1 New Procedure

2 None of the above

Enter a number from the list above: ^

Want to run a validity check on CPT and stop codes? NO// ^

Example, FileMan lookup of CPT code 72159:

VA FileMan 22.2

Select OPTION: INQUIRE TO FILE ENTRIES

Output from what File: RAD/NUC MED PROCEDURES// (2010 entries)

Select RAD/NUC MED PROCEDURES NAME: 72159 MR ANGIO SPINE

W/O&W/DYE

1 72159 MAGNETIC ANGIOGRAPHY, SPINAL CANAL (MRI Inactive) CPT:72159

2 72159 CERVICAL CANAL, W & W/O CONTRAST (MRI Inactive) CPT:72159

3 72159 THORACIC CANAL, W & W/O CONTRAST (MRI Inactive) CPT:72159

4 72159 LUMBAR CANAL, W & W/O CONTRAST (MRI Inactive) CPT:72159

5 72159 MRA CERVICAL CANAL W/CONTENTS (MRI Inactive) CPT:72159

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

Resolution:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, entry of a CPT code returns all eligible

procedures with matching CPT codes in the RAD/NUC MED PROCEDURES (#71)

file.

Example, lookup CPT 71015 in the Procedure Enter/Edit \[RA PROCEDURE\]

option:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: 71015 CHEST X-RAY STEREO FRONTAL

1 71015 CHEST STEREO PA (RAD Detailed) CPT:71015

2 71015 CHEST TUBE PLACEMENT (RAD Detailed) CPT:71015

CHOOSE 1-2:

Example, FileMan lookup of CPT 71015:

Select RAD/NUC MED PROCEDURES NAME: 71015 CHEST X-RAY STEREO FRONTAL

1 71015 CHEST STEREO PA (RAD Detailed) CPT:71015

2 71015 CHEST TUBE PLACEMENT (RAD Detailed) CPT:71015

CHOOSE 1-2:

Issue 7

==========================================================================

Defect \#487927 - Question mark lookup of procedures no longer works at

Procedure Enter/Edit.

Problem:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, the entry of question marks returns the error

message "?? Answer must be 1-60 characters in length." In the past,

entering question marks returned an alphabetical list of procedures.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURES NAME: ?

Answer must be 1-60 characters in length. First 30 must be unique.

RAD/NUC MED PROCEDURES NAME: ??

Answer must be 1-60 characters in length. First 30 must be unique.

Resolution:

--------------

At the "RAD/NUC MED PROCEDURE NAME:" prompt in the Procedure Enter/Edit

\[RA PROCEDURE\] option, the entry of question marks returns an

alphabetical list of procedures in the RAD/NUC MED PROCEDURES (#71)

file.

Example:

Select Procedure Edit Menu Option: Procedure Enter/Edit

RAD/NUC MED PROCEDURE NAME: ?

Answer with RAD/NUC MED PROCEDURES NAME, or CPT CODE, or

CONTRAST MEDIA USED, or MRPF NAME, or ENTRY CREATION DATE, or

SYNONYM

Do you want the entire 901-Entry RAD/NUC MED PROCEDURES List? Y (Yes)

Choose from:

A9150 (NM Parent )

ABDOMEN 1 VIEW (RAD Detailed) CPT:74022

ABDOMEN 2 + PA & LAT CHEST (RAD Detailed) CPT:74022

Type \<Enter\> to continue or '^' to exit:

^

RAD/NUC MED PROCEDURE NAME: ??

Answer with RAD/NUC MED PROCEDURES NAME, or CPT CODE, or

CONTRAST MEDIA USED, or MRPF NAME, or ENTRY CREATION DATE, or

SYNONYM

Do you want the entire 901-Entry RAD/NUC MED PROCEDURES List? Y (Yes)

Choose from:

A9150 (NM Parent )

ABDOMEN 1 VIEW (RAD Detailed) CPT:74022

ABDOMEN 2 + PA & LAT CHEST (RAD Detailed) CPT:74022

Type \<Enter\> to continue or '^' to exit:

Software and Documentation Retrieval Instructions:

----------------------------------------------------

Software being released as a host file and/or documentation describing

the new functionality introduced by this patch are available.

The preferred method is to retrieve files from download.vista.med.va.gov.

This transmits the files from the first available server. Sites may

also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using

Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE

directory at the following OI Field Offices:

Albany: fo-albany.med.va.gov

Hines: fo-hines.med.va.gov

Salt Lake City: fo-slc.med.va.gov

Documentation can also be found on the VA Software Documentation Library

at: http://www4.va.gov/vdl/

Title File Name FTP Mode

------------------------------------------------------------------------

N/A

Patch Installation:

Pre/Post Installation Overview:

There are no pre-installation actions.

Pre-Installation Instructions:

==============================

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\* Please install/re-install released patch RA\*5.0\*127 \*\*

\*\* immediately prior to installing this patch to ensure \*\*

\*\* all routine and data dictionary dependencies exist, and \*\*

\*\* have not been backed out or modified. \*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Prior to installing this patch, create a backup of both the routines

and the updated Data Definition by creating a 'backup' patch containing

all the routines and data definitions exported with this patch.

From the Kernel Installation and Distribution System Menu, select the

Edit a Build option. When prompted for the BUILD NAME, enter backup patch

name ZRA\*5.0\*138.

a\. Add the following Data Definitions to the patch:

1\. At the File List page, enter the NEW RAD PROCEDURE WORKUP (#71.11)

file, with the following settings:

A. Send Full or Partial DD: PARTIAL
B. Update the Data Dictionary: YES
C. Send Security Code: YES
D. Data Comes With File: NO

2\. At the Data Dictionary Number page, enter the following:

A. The DESCENDENTS sub-file (#71.1105).

b\. Add the following 7 routines to the patch:

RAMAIN2

RAMAIN4

RAMAIN5

RANPRO

RANPRO1

RANPRO4

RANPRO5

b\. Add the following Input Templates to the Build Components section

of the patch:

1\. NEW RAD PROCEDURE (#71.11)

2\. RA PROCEDURE EDIT (#71)

After creating the backup patch, printing the build using the Build

File Print \[XPD PRINT BUILD\] in the Utilities \[XPD UTILITY\] menu

should produce output similar to the following:

PACKAGE: ZRA\*5.0\*138 Apr 11, 2017 12:22 pm PAGE 1

---------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ALPHA/BETA TESTING: NO

DESCRIPTION:

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

--------------------------------------------------------------------------

71.11 NEW RAD PROCEDURE

WORKUP YES YES NO NO

Partial DD: subDD: 71.11

subDD: 71.1105

INPUT TEMPLATE: ACTION:

NEW RAD PROCEDURE FILE \#71.11 SEND TO SITE

RA PROCEDURE EDIT FILE \#71 SEND TO SITE

ROUTINE: ACTION:

RAMAIN2 SEND TO SITE

RAMAIN4 SEND TO SITE

RAMAIN5 SEND TO SITE

RANPRO SEND TO SITE

RANPRO1 SEND TO SITE

RANPRO4 SEND TO SITE

RANPRO5 SEND TO SITE

After creating the backup patch build, transport the backup to all

appropriate recipients using the Transport a Distribution \[XPD

TRANSPORT PACKAGE\] option in the Edit a Build \[XPD INSTALLATION MENU\]

menu in the Kernel Installation & Distribution System \[XPD MAIN\] menu.

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than

5 minutes to install. It is not necessary to disable any options.

Installation Instructions:

--------------------------

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the

patch RA\*5.0\*138.

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

(allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch routines,

DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow you

to ensure the integrity of the routines that are in the transport

global.

4\. From the Installation Menu, select the Install Package(s) option

and choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//', respond NO.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', respond NO.

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

Post-Installation Instructions:

===============================

N/A

Patch Backout Plan

==================

If patch RA\*5.0\*138 needs to backed out, please contact Health Product

Support to back the patch out by re-installing the patch backup created

prior to installation.

The rollback/back-out procedure for this patch requires installation of

the backup patch ZRA\*5.0\*138 created during the pre-installation process.

Please contact Health Product Support for assistance if a determination

is made that the patch should be backed out.

ROUTINE INFORMATION

-------------------

Routine Information:

====================

The second line of each of these routines now looks like:

;;5.0;Radiology/Nuclear Medicine;\*\*\[Patch List\]\*\*;Mar 16, 1998;Build 16

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: RAMAIN2

Before: B63613910 After: B63318644 \*\*45,62,71,65,127,138\*\*

Routine Name: RAMAIN4

Before: B30460135 After: B31310933 \*\*127,138\*\*

Routine Name: RAMAIN5

Before: B38646269 After: B36683496 \*\*127,138\*\*

Routine Name: RANPRO

Before: B93138436 After:B105341617 \*\*127,138\*\*

Routine Name: RANPRO1

Before: n/a After: B1214199 \*\*138\*\*

Routine Name: RANPRO4

Before: B38023574 After: B38438908 \*\*127,138\*\*

Routine Name: RANPRO5

Before: B42155834 After: B39057526 \*\*127,138\*\*

Routine list of preceding patches: 127

=============================================================================

User Information:

Entered By : HARRIS,JAMES C Date Entered : MAR 30,2017

Completed By: Date Completed:

Released By : Date Released :

## Patch RA\*5\*140 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: APR 11, 2017 Designation: RA\*5\*140 TEST v1

Package : RADIOLOGY/NUCLEAR MEDICINE Priority : EMERGENCY

Version : 5 Status : UNDER DEVELOPMENT

=============================================================================

Subject: INFORMATIONAL PATCH FOR RA\*5.0\*127 SUPPLEMENT

Category: INFORMATIONAL

Description:

===========

\*\*\*\* This Patch Only Applies to Facilities that have \*\*\*\*

\*\*\*\* Installed Patch RA\*5.0\*127. \*\*\*\*

This patch describes supplemental actions that the Radiology

ADPAC's may take while using the Radiology Procedure Enter/Edit

option post the RA\*5.0\*127 install.

With the release of RA\*5.0\*127 certain functionality in the selection

and creation of Procedures was changed. This Informational Patch is

notating the changes that have been reported and work arounds for

those changes where appropriate.

These items are also addressed in the 'ADPAC Supplement RA 5.0' file

name: ra_5_aa_s_1.PDF.

1\. Use of double question marks ('??').

The ADPAC will not have the ability to use '??' for a Procedure List.

The work around is: The ADPAC will need to enter at least the first 3

characters of the Procedure Name. This will list those Procedures

whose name starts with the characters entered.

2\. VistA error when selecting a direct match on a Procedure Name.

This error is generated as the result of multiple procedures having

the same name.

The work around is: If the ADPAC encounters this error when entering

an exact match on the Procedure Name the ADPAC should re-enter the

Procedure Name omitting the last few characters.

Example:

RAD NUC/MED PROCEDURES NAME: "WRIST 2 VIEWS"

Enter as: "WRIST 2 VIEW"

3\. Procedure Names that contain forward slashes ('/').

The ADPAC should refrain from creating Procedures with forward

slashes ('/') in the Procedure name.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The ADPAC may not edit Procedures with a forward slash ('/') in

the Procedure Name.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4\. Radiology/Nuclear Medicine Code Change Process

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Detailed instructions are in section 2 of the:

ADPAC Supplement RA 5.0 (ra_5_aa_s_1.pdf)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

When the annual VAMC code changes are distributed to the VA

facilities, the ADPAC will need to update each individual procedure

impacted by the new CPT codes provided to the medical centers.

After the NDS Radiology Patch RA\*5\*127 is installed the ADPAC will

not have visibility to the Type of Imaging, Detailed nor the CPT Code.

As a result of the new patch, the Radiology Procedure List display will

have a different appearance.

The ADPAC will only be able to look up Procedures based on a partial

match To the Procedure Name.

When working with the Procedure the ADPAC would include the Imaging

Type in the Procedure Name.

Software and Documentation Retrieval Instructions:

----------------------------------------------------

Software being released as a host file and/or documentation describing

the new functionality introduced by this patch are available.

The preferred method is to retrieve files from download.vista.med.va.gov.

This transmits the files from the first available server. Sites may

also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using

Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE

directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library

at: http://www4.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

ADPAC Supplement RA 5.0 ra_5_aa_s_1.PDF Binary

Routine Information:

====================

No routines included.

=============================================================================

User Information:

Entered By : <span class="mark">REDACTED</span> Date Entered : APR 11,2017

Completed By: Date Completed:

Released By : Date Released :

=============================================================================