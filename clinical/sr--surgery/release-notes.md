---
consolidated_title: "surgery release notes"
app_code: SR
doc_type: RN
master_source: "SR*3.0*205 Surgery Release Notes"
master_pub_date: July 2024
consolidated_from: 4 versions
prior_versions:
  - "SR*3*182 Surgery Release Notes"
  - "SR*3*184 Surgery Release Notes"
  - "SR*3*200 Surgery Release Notes"
---

# VistA Surgery


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VistA Surgery](#vista-surgery)
- [SR\3.0\205](#sr30205)
- [Release Notes](#release-notes)
  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Patch Information](#patch-information)
    - [Surgery Menu Input Template Modifications, Including POSSIBLE ITEM RETENTION Field Removal](#surgery-menu-input-template-modifications-including-possible-item-retention-field-removal)
    - [POSSIBLE ITEM RETENTION Field Deactivation](#possible-item-retention-field-deactivation)
    - [DONOR VESSEL DISPOSITION Field Update](#donor-vessel-disposition-field-update)
    - [Spelling Correction of GLASSES/GOOGLES to GLASSES/GOGGLES](#spelling-correction-of-glassesgoogles-to-glassesgoggles)

# SR\*3.0\*205

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](sr-3-0-205-surgery-release-notes/001.png)

July 2024

Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement to the VistA Surgery package:

1\. Adds fields to, removes fields from, and modifies the order of fields displayed in the SRONRPT, SRONRPT1 and SRONRPT2 input templates. These input templates are executed when the Nurse Intraoperative Report option \[SRONRPT\] is selected. All 3 input templates now display the order of fields requested by the National Surgery Office (NSO).

2\. Deactivates the POSSIBLE ITEM RETENTION (#630) field in the SURGERY (#130) file and removes it from the SRONRPT, SRONRPT1, SRONRPT2, SROMEN-OPER and SROMEN-OUT input templates for entry/editing. The POSSIBLEITEMRETENTION (#630) field is no longer required to sign the Nurse Intraoperative Report but will continue to display when viewing completed Nurse Intraoperative Reports for historical cases.

3\. Adds ‘NA’ FOR NOT APPLICABLE to the SET OF CODES for the DONOR VESSEL DISPOSITION (#665) field in the SURGERY (#130) file. Surgery Risk Assessments have been modified to accommodate the new 2-character code.

4\. Corrects the spelling of GLASSES/GOOGLES to GLASSES/GOGGLES in the SRONRPT4 routine for display/print in the Nurse Intraoperative Report.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA Surgery and applies to the changes made between this release and any previous release for this software.

## Patch Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Surgery Menu Input Template Modifications, Including POSSIBLE ITEM RETENTION Field Removal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Menu has multiple entry points to access the input templates modified by this patch.

The Nurse Intraoperative Report option \[SRONRPT\] executes the SRONRPT, SRONRPT1, and SRONRPT2 input templates. This patch adds fields to, removes fields (including POSSIBLE ITEM RETENTION) from, and modifies the order of fields displayed in these input templates. The POSSIBLE ITEM RETENTION (#630) field is no longer a required field to sign the Nurse Intraoperative Report, but it will continue to display when viewing/printing completed Nurse Intraoperative Reports for historical cases.

The Operation option \[SROMEN-OP\] executes the SROMEN-OPER input template. This patch removes the POSSIBLE ITEM RETENTION (#630) field from this input template, so all fields following the removed POSSIBLE ITEM RETENTION field have moved up a position in the display.

The Operation (Short Screen) option \[SROMEN-OUT\] executes the SROMEN-OUT input template. This patch removes the POSSIBLE ITEM RETENTION (#630) field from this input template, so all fields following the removed POSSIBLE ITEM RETENTION field have moved up a position in the display.

#### Executing the SRONRPT Input Template

To execute the SRONRPT input template, prior to selecting the Nurse Intraoperative Report option \[SRONRPT\], the user must enter a new or select an existing surgical case that contains a Planned Principal Procedure Code (displayed as PLANNED PRIN PROCEDURE CODE) that references general surgeries.

Example: Entering a Planned Principal Procedure Code that references general surgeries

Select Surgery Menu \<TEST ACCOUNT\> Option: <u>Operation Menu</u>

Select Patient: <u>TEST,PATIENT</u>

*\<screen clears\>*

TEST,PATIENT XXX-XX-XXXX

1\. ENTER NEW SURGICAL CASE

Select Operation: <u>1</u>

Select the Date of Operation: <u>T</u> (JAN 25, 2024)

Desired Procedure Date: <u>T</u> (JAN 25, 2024)

Enter the Principal Operative Procedure: <u>SRONRPT CASE</u>

Principal Preoperative Diagnosis: <u>TEST</u>

The information entered into the Principal Preoperative Diagnosis field

has been transferred into the Indications for Operation field.

The Indications for Operation field can be updated later if necessary.

Select Primary Surgeon: <u>TEST,PROVIDER</u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Select Surgical Specialty: <u>GENERAL(OR WHEN NOT DEFINED BELOW)</u> GENERAL(OR WHEN N

OT DEFINED BELOW) 50

Planned Principal Procedure Code: <span class="mark"><u>10010</u></span> FNA BX W/CT GDN EA ADDL

FINE NEEDLE ASPIRATION BIOPSY, INCLUDING CT GUIDANCE; EACH ADDITIONAL LESION

(LIST SEPARATELY IN ADDITION TO CODE FOR PRIMARY PROCEDURE)

Modifier: <u>\<enter\></u>

Brief Clinical History:

1\><u>\<enter\></u>

Request Blood Availability (Y/N): N// <u>\<enter\></u>

Principal Preoperative Diagnosis: TEST// <u>\<enter\></u>

Prin Pre-OP ICD Diagnosis Code (ICD10): <u>\<enter\></u>

Hospital Admission Status: <u>\<enter\></u>

Case Schedule Type: <u>\<enter\></u>

First Assistant: <u>\<enter\></u>

Second Assistant: <u>\<enter\></u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Planned Postop Care: <u>\<enter\></u>

Case Schedule Order: <u>\<enter\></u>

Select SURGERY POSITION: SUPINE// <u>\<enter\></u>

Surgery Position: SUPINE// <u>\<enter\></u>

Requested Anesthesia Technique: <u>\<enter\></u>

Request Frozen Section Tests (Y/N): <u>\<enter\></u>

Requested Preoperative X-Rays: <u>\<enter\></u>

Intraoperative X-Rays (Y/N/C): <u>\<enter\></u>

Request Medical Media (Y/N): <u>\<enter\></u>

Preoperative Infection: <u>\<enter\></u>

Select REFERRING PHYSICIAN: <u>\<enter\></u>

General Comments:

1\><u>\<enter\></u>

SPD Comments:

1\><u>\<enter\></u>

*\<screen clears\>*\*\* NEW SURGERY \*\* CASE \#000 TEST,PATIENT PAGE 1 OF 3

1 PRINCIPAL PROCEDURE: SRONRPT CASE2 OTHER PROCEDURES: (MULTIPLE)3 PLANNED PRIN PROCEDURE CODE : <span class="mark">10010</span>4 LATERALITY OF PROCEDURE:

5 PRINCIPAL PRE-OP DIAGNOSIS: TEST6 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

7 OTHER PREOP DIAGNOSIS: (MULTIPLE)8 PALLIATION:

9 PLANNED ADMISSION STATUS:

10 PRE-ADMISSION TESTING:

11 CASE SCHEDULE TYPE:

12 SURGERY SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)13 PRIMARY SURGEON: TEST,PROVIDER14 FIRST ASST:

15 SECOND ASST:

Enter Screen Server Function:

The SRONRPT input template now follows the order of fields requested by the National Surgery Office and no longer contains POSSIBLE ITEM RETENTION:

\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 1 OF 7

1 DATE OF OPERATION: JAN 25, 20242 OP ROOM PROCEDURE PERFORMED:

3 CASE SCHEDULE TYPE:

4 TIME PAT IN HOLD AREA:

5 PATIENT EDUCATION/ASSESSMENT:

6 TRANS TO OR BY:

7 TIME PAT IN OR:

8 DELAY CAUSE: (MULTIPLE)9 PREOP MOOD:

10 PREOP CONSCIOUS:

11 PREOP SKIN INTEG:

12 SURG PRESENT TIME:

13 PRIMARY SURGEON: TEST,PROVIDER14 PGY OF PRIMARY SURGEON:

15 ATTENDING SURGEON: TEST,PROVIDER

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 2 OF 7

1 FIRST ASST:

2 SECOND ASST:

3 OTHER SCRUBBED ASSISTANTS: (MULTIPLE)4 PRINC ANESTHETIST:

5 ASST ANESTHETIST:

6 ANESTHESIOLOGIST SUPVR:

7 RELIEF ANESTHETIST:

8 ANESTHESIA TECHNIQUE: (MULTIPLE)9 ASA CLASS:

10 PERFUSIONIST:

11 ASST PERFUSIONIST:

12 OR CIRC SUPPORT: (MULTIPLE)13 OR SCRUB SUPPORT: (MULTIPLE)14 OTHER PERSONS IN OR: (MULTIPLE)15 SURGERY POSITION: (MULTIPLE)(DATA)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 3 OF 7

1 RESTR & POSITION AIDS: (MULTIPLE)(DATA)2 HAIR REMOVAL BY:

3 HAIR REMOVAL METHOD:

4 HAIR REMOVAL COMMENTS: (WORD PROCESSING)5 SKIN PREPPED BY (1):

6 SKIN PREPPED BY (2):

7 SKIN PREP AGENTS:

8 SECOND SKIN PREP AGENT:

9 ELECTROCAUTERY UNIT:

10 ESU COAG RANGE:

11 ESU CUTTING RANGE:

12 ELECTROGROUND POSITION:

13 ELECTROGROUND POSITION (2):

14 SEQUENTIAL COMPRESSION DEVICE:

15 THERMAL UNIT: (MULTIPLE)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 4 OF 7

1 FOLEY CATHETER INSERTED BY:

2 CONFIRM PATIENT IDENTITY:

3 PROCEDURE TO BE PERFORMED:

4 SITE OF PROCEDURE:

5 CONFIRM VALID CONSENT:

6 CONFIRM PATIENT POSITION:

7 MARKED SITE CONFIRMED:

8 PREOPERATIVE IMAGES CONFIRMED:

9 CORRECT MEDICAL IMPLANTS:

10 AVAILABILITY OF SPECIAL EQUIP:

11 ANTIBIOTIC PROPHYLAXIS:

12 APPROPRIATE DVT PROPHYLAXIS:

13 BLOOD AVAILABILITY:

14 CHECKLIST COMMENT: (WORD PROCESSING)15 TIME-OUT DOCUMENT COMPLETED BY:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 5 OF 7

1 TIME-OUT COMPLETED:

2 TIME OPERATION BEGAN:

3 DEVICE(S):

4 IRRIGATION: (MULTIPLE)5 MEDICATIONS: (MULTIPLE)6 TIME TOURNIQUET APPLIED: (MULTIPLE)7 CELL SAVER: (MULTIPLE)8 PROSTHESIS INSTALLED: (MULTIPLE)9 LASER PERFORMED: (MULTIPLE)10 SPECIMENS: (WORD PROCESSING)11 CULTURES: (WORD PROCESSING)12 SPONGE FINAL COUNT CORRECT:

13 SHARPS FINAL COUNT CORRECT:

14 INSTRUMENT FINAL COUNT CORRECT:

15 SPONGE, SHARPS, & INST COUNTER:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 6 OF 7

1 COUNT VERIFIER:

2 WOUND SWEEP:

3 WOUND SWEEP COMMENTS: (WORD PROCESSING)4 INTRA-OPERATIVE X-RAY:

5 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)6 NURSING CARE COMMENTS: (WORD PROCESSING)7 SURGERY SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)8 PRINCIPAL PROCEDURE: SRONRPT CASE9 LATERALITY OF PROCEDURE:

10 OTHER PROCEDURES: (MULTIPLE)11 ROBOTIC ASSISTANCE (Y/N):

12 WOUND CLASSIFICATION:

13 ATTENDING/RES SUP CODE:

14 PACKING:

15 DRESSING:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#000 TEST,PATIENT PAGE 7 OF 7

1 TUBES AND DRAINS:

2 TIME OPERATION ENDS:

3 POSTOP SKIN INTEG:

4 DISCHARGED VIA:

5 OP DISPOSITION:

6 REPORT GIVEN TO:

7 TIME PAT OUT OR:

Enter Screen Server Function:

#### Executing the SRONRPT1 Input Template

To execute the SRONRPT1 input template, prior to selecting the Nurse Intraoperative Report option \[SRONRPT\], the user must enter a new or select an existing surgical case that contains a Planned Principal Procedure Code (displayed as PLANNED PRIN PROCEDURE CODE) that references transplant surgeries. Transplant surgeries use the following CPT codes: 32851, 32852, 32853, 32854, 33935, 33945, 44135, 44136, 47135, 47136, 48160, 48554, 50360, 50365.

Example: Entering a Planned Principal Procedure Code that references transplant surgeries

Select Surgery Menu \<TEST ACCOUNT\> Option: <u>Operation Menu</u>

Select Patient: <u>TEST,PATIENT</u>

*\<screen clears\>*

TEST,PATIENT XXX-XX-XXXX

1\. 01-25-24 SRONRPT CASE (NOT COMPLETE)

2\. ENTER NEW SURGICAL CASE

Select Operation: <u>2</u>

Select the Date of Operation: <u>T</u> (JAN 25, 2024)

Desired Procedure Date: <u>T</u> (JAN 25, 2024)

Enter the Principal Operative Procedure: <u>SRONRPT1 CASE</u>

Principal Preoperative Diagnosis: <u>TEST</u>

The information entered into the Principal Preoperative Diagnosis field

has been transferred into the Indications for Operation field.

The Indications for Operation field can be updated later if necessary.

Select Primary Surgeon: <u>TEST,PROVIDER</u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Select Surgical Specialty: <u>TRANSPLANTATION</u> TRANSPLANTATION 49

Planned Principal Procedure Code: <span class="mark"><u>32853</u></span> LUNG TRANSPLANT DOUBLE

LUNG TRANSPLANT, DOUBLE (BILATERAL SEQUENTIAL OR EN BLOC); WITHOUT

CARDIOPULMONARY BYPASS

Modifier: <u>\<enter\></u>

Brief Clinical History:

1\><u>\<enter\></u>

Request Blood Availability (Y/N): N// <u>\<enter\></u>

Principal Preoperative Diagnosis: TEST// <u>\<enter\></u>

Prin Pre-OP ICD Diagnosis Code (ICD10): <u>\<enter\></u>

Hospital Admission Status: <u>\<enter\></u>

Case Schedule Type: <u>\<enter\></u>

First Assistant: <u>\<enter\></u>

Second Assistant: <u>\<enter\></u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Planned Postop Care: <u>\<enter\></u>

Case Schedule Order: <u>\<enter\></u>

Select SURGERY POSITION: SUPINE// <u>\<enter\></u>

Surgery Position: SUPINE// <u>\<enter\></u>

Requested Anesthesia Technique: <u>\<enter\></u>

Request Frozen Section Tests (Y/N): <u>\<enter\></u>

Requested Preoperative X-Rays: <u>\<enter\></u>

Intraoperative X-Rays (Y/N/C): <u>\<enter\></u>

Request Medical Media (Y/N): <u>\<enter\></u>

Preoperative Infection: <u>\<enter\></u>

Select REFERRING PHYSICIAN: <u>\<enter\></u>

General Comments:

1\><u>\<enter\></u>

SPD Comments:

1\><u>\<enter\></u>

*\<screen clears\>*\*\* NEW SURGERY \*\* CASE \#001 TEST,PATIENT PAGE 1 OF 3

1 PRINCIPAL PROCEDURE: SRONRPT1 CASE2 OTHER PROCEDURES: (MULTIPLE)3 PLANNED PRIN PROCEDURE CODE : <span class="mark">32853</span>4 LATERALITY OF PROCEDURE:

5 PRINCIPAL PRE-OP DIAGNOSIS: TEST6 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

7 OTHER PREOP DIAGNOSIS: (MULTIPLE)8 PALLIATION:

9 PLANNED ADMISSION STATUS:

10 PRE-ADMISSION TESTING:

11 CASE SCHEDULE TYPE:

12 SURGERY SPECIALTY: TRANSPLANTATION13 PRIMARY SURGEON: TEST,PROVIDER14 FIRST ASST:

15 SECOND ASST:

Enter Screen Server Function:

The SRONRPT1 input template now follows the order of fields requested by the National Surgery Office and no longer contains POSSIBLE ITEM RETENTION:

\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 1 OF 9

1 DATE OF OPERATION: JAN 25, 20242 OP ROOM PROCEDURE PERFORMED:

3 CASE SCHEDULE TYPE:

4 TIME PAT IN HOLD AREA:

5 PATIENT EDUCATION/ASSESSMENT:

6 TRANS TO OR BY:

7 TIME PAT IN OR:

8 DELAY CAUSE: (MULTIPLE)9 PREOP MOOD:

10 PREOP CONSCIOUS:

11 PREOP SKIN INTEG:

12 SURG PRESENT TIME:

13 PRIMARY SURGEON: TEST,PROVIDER14 PGY OF PRIMARY SURGEON:

15 ATTENDING SURGEON: TEST,PROVIDER

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 2 OF 9

1 FIRST ASST:

2 SECOND ASST:

3 OTHER SCRUBBED ASSISTANTS: (MULTIPLE)4 PRINC ANESTHETIST:

5 ASST ANESTHETIST:

6 ANESTHESIOLOGIST SUPVR:

7 RELIEF ANESTHETIST:

8 ANESTHESIA TECHNIQUE: (MULTIPLE)9 ASA CLASS:

10 PERFUSIONIST:

11 ASST PERFUSIONIST:

12 OR CIRC SUPPORT: (MULTIPLE)13 OR SCRUB SUPPORT: (MULTIPLE)14 OTHER PERSONS IN OR: (MULTIPLE)15 SURGERY POSITION: (MULTIPLE)(DATA)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 3 OF 9

1 RESTR & POSITION AIDS: (MULTIPLE)(DATA)2 HAIR REMOVAL BY:

3 HAIR REMOVAL METHOD:

4 HAIR REMOVAL COMMENTS: (WORD PROCESSING)5 SKIN PREPPED BY (1):

6 SKIN PREPPED BY (2):

7 SKIN PREP AGENTS:

8 SECOND SKIN PREP AGENT:

9 ELECTROCAUTERY UNIT:

10 ESU COAG RANGE:

11 ESU CUTTING RANGE:

12 ELECTROGROUND POSITION:

13 ELECTROGROUND POSITION (2):

14 SEQUENTIAL COMPRESSION DEVICE:

15 THERMAL UNIT: (MULTIPLE)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 4 OF 9

1 FOLEY CATHETER INSERTED BY:

2 CONFIRM PATIENT IDENTITY:

3 PROCEDURE TO BE PERFORMED:

4 SITE OF PROCEDURE:

5 CONFIRM VALID CONSENT:

6 CONFIRM PATIENT POSITION:

7 MARKED SITE CONFIRMED:

8 PREOPERATIVE IMAGES CONFIRMED:

9 CORRECT MEDICAL IMPLANTS:

10 AVAILABILITY OF SPECIAL EQUIP:

11 ANTIBIOTIC PROPHYLAXIS:

12 APPROPRIATE DVT PROPHYLAXIS:

13 BLOOD AVAILABILITY:

14 CHECKLIST COMMENT: (WORD PROCESSING)15 TIME-OUT DOCUMENT COMPLETED BY:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 5 OF 9

1 TIME-OUT COMPLETED:

2 TIME OPERATION BEGAN:

3 DEVICE(S):

4 IRRIGATION: (MULTIPLE)5 MEDICATIONS: (MULTIPLE)6 TIME TOURNIQUET APPLIED: (MULTIPLE)7 CELL SAVER: (MULTIPLE)8 PROSTHESIS INSTALLED: (MULTIPLE)9 LASER PERFORMED: (MULTIPLE)10 SPECIMENS: (WORD PROCESSING)11 CULTURES: (WORD PROCESSING)12 SPONGE FINAL COUNT CORRECT:

13 SHARPS FINAL COUNT CORRECT:

14 INSTRUMENT FINAL COUNT CORRECT:

15 SPONGE, SHARPS, & INST COUNTER:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 6 OF 9

1 COUNT VERIFIER:

2 WOUND SWEEP:

3 WOUND SWEEP COMMENTS: (WORD PROCESSING)4 INTRA-OPERATIVE X-RAY:

5 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)6 NURSING CARE COMMENTS: (WORD PROCESSING)7 SURGERY SPECIALTY: TRANSPLANTATION8 PRINCIPAL PROCEDURE: SRONRPT1 CASE9 LATERALITY OF PROCEDURE:

10 OTHER PROCEDURES: (MULTIPLE)11 ROBOTIC ASSISTANCE (Y/N):

12 WOUND CLASSIFICATION:

13 ATTENDING/RES SUP CODE:

14 PACKING:

15 DRESSING:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 7 OF 9

1 TUBES AND DRAINS:

2 TIME OPERATION ENDS:

3 POSTOP SKIN INTEG:

4 DISCHARGED VIA:

5 OP DISPOSITION:

6 REPORT GIVEN TO:

7 TIME PAT OUT OR:

8 ORGANS TO BE TRANSPLANTED: (MULTIPLE)9 UNOS NUMBER:

10 DONOR SEROLOGY HCV:

11 DONOR SEROLOGY HBV:

12 DONOR SEROLOGY CMV:

13 DONOR SEROLOGY HIV:

14 DONOR ABO TYPE:

15 RECIPIENT ABO TYPE:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 8 OF 9

1 BLOOD BANK ABO VERIFICATION:

2 BLOOD BANK ABO VER COMMENTS:

3 D/T BLOOD BANK ABO VERIF:

4 OR ABO VERIFICATION (Y/N):

5 OR ABO VER COMMENTS:

6 D/T OR ABO VERIF:

7 SURGEON VERIFYING UNET:

8 UNET VERIF BY SURGEON (Y/N):

9 ORGAN VER PRE-ANESTHESIA:

10 SURGEON VER ORGAN PRE-ANES:

11 SURGEON VER DONOR ORG PRE-ANES:

12 DONOR ORG VER PRE-ANES:

13 ORGAN VER PRE-TRANSPLANT:

14 SURGEON VER ORG PRE-TRANSPLANT:

15 DONOR VESSEL UNOS ID: (MULTIPLE)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 9 OF 9

1 DONOR VESSEL USAGE:

2 DONOR VESSEL DISPOSITION:

Enter Screen Server Function:

#### Executing the SRONRPT2 Input Template

To execute the SRONRPT2 input template, prior to selecting the Nurse Intraoperative Report option, the user must enter a new or select an existing surgical case that contains a Planned Principal Procedure Code (displayed as PLANNED PRIN PROCEDURE CODE) that references donor surgeries. Donor surgeries use the following CPT codes: 44133, 47140, 47141, 47142, 48550, 50320, 50547.

Example: Entering a Planned Principal Procedure Code that references general surgeries

Select Surgery Menu \<TEST ACCOUNT\> Option: <u>Operation Menu</u>

Select Patient: <u>TEST,PATIENT</u>

*\<screen clears\>*

TEST,PATIENT XXX-XX-XXXX

1\. 01-25-24 SRONRPT CASE (NOT COMPLETE)

2\. 01-25-24 SRONRPT1 CASE (NOT COMPLETE)

3\. ENTER NEW SURGICAL CASE

Select Operation: <u>3</u>

Select the Date of Operation: <u>T</u> (JAN 25, 2024)

Desired Procedure Date: <u>T</u> (JAN 25, 2024)

Enter the Principal Operative Procedure: <u>SRONRPT2 CASE</u>

Principal Preoperative Diagnosis: <u>TEST</u>

The information entered into the Principal Preoperative Diagnosis field

has been transferred into the Indications for Operation field.

The Indications for Operation field can be updated later if necessary.

Select Primary Surgeon: <u>TEST,PROVIDER</u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Select Surgical Specialty: <u>TRANSPLANTATION</u> TRANSPLANTATION 49

Planned Principal Procedure Code: <span class="mark"><u>44133</u></span> ENTERECTOMY LIVE DONOR

DONOR ENTERECTOMY (INCLUDING COLD PRESERVATION), OPEN; PARTIAL,

FROM LIVING DONOR

Modifier: <u>\<enter\></u>

Brief Clinical History:

1\><u>\<enter\></u>

Request Blood Availability (Y/N): N// <u>\<enter\></u>

Principal Preoperative Diagnosis: TEST// <u>\<enter\></u>

Prin Pre-OP ICD Diagnosis Code (ICD10): <u>\<enter\></u>

Hospital Admission Status: <u>\<enter\></u>

Case Schedule Type: <u>\<enter\></u>

First Assistant: <u>\<enter\></u>

Second Assistant: <u>\<enter\></u>

Attending Surgeon: TEST,PROVIDER// <u>\<enter\></u>

Planned Postop Care: <u>\<enter\></u>

Case Schedule Order: <u>\<enter\></u>

Select SURGERY POSITION: SUPINE// <u>\<enter\></u>

Surgery Position: SUPINE// <u>\<enter\></u>

Requested Anesthesia Technique: <u>\<enter\></u>

Request Frozen Section Tests (Y/N): <u>\<enter\></u>

Requested Preoperative X-Rays: <u>\<enter\></u>

Intraoperative X-Rays (Y/N/C): <u>\<enter\></u>

Request Medical Media (Y/N): <u>\<enter\></u>

Preoperative Infection: <u>\<enter\></u>

Select REFERRING PHYSICIAN: <u>\<enter\></u>

General Comments:

1\><u>\<enter\></u>

SPD Comments:

1\><u>\<enter\></u>

*\<screen clears\>*\*\* NEW SURGERY \*\* CASE \#002 TEST,PATIENT PAGE 1 OF 3

1 PRINCIPAL PROCEDURE: SRONRPT2 CASE2 OTHER PROCEDURES: (MULTIPLE)3 PLANNED PRIN PROCEDURE CODE : <span class="mark">44133</span>4 LATERALITY OF PROCEDURE:

5 PRINCIPAL PRE-OP DIAGNOSIS: TEST6 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

7 OTHER PREOP DIAGNOSIS: (MULTIPLE)8 PALLIATION:

9 PLANNED ADMISSION STATUS:

10 PRE-ADMISSION TESTING:

11 CASE SCHEDULE TYPE:

12 SURGERY SPECIALTY: TRANSPLANTATION13 PRIMARY SURGEON: TEST,PROVIDER14 FIRST ASST:

15 SECOND ASST:

Enter Screen Server Function:

The SRONRPT2 input template now follows the order of fields requested by the National Surgery Office and no longer contains POSSIBLE ITEM RETENTION:

\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 1 OF 7

1 DATE OF OPERATION: JAN 25, 20242 OP ROOM PROCEDURE PERFORMED:

3 CASE SCHEDULE TYPE:

4 TIME PAT IN HOLD AREA:

5 PATIENT EDUCATION/ASSESSMENT:

6 TRANS TO OR BY:

7 TIME PAT IN OR:

8 DELAY CAUSE: (MULTIPLE)9 PREOP MOOD:

10 PREOP CONSCIOUS:

11 PREOP SKIN INTEG:

12 SURG PRESENT TIME:

13 PRIMARY SURGEON: TEST,PROVIDER14 PGY OF PRIMARY SURGEON:

15 ATTENDING SURGEON: TEST,PROVIDER

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 2 OF 7

1 FIRST ASST:

2 SECOND ASST:

3 OTHER SCRUBBED ASSISTANTS: (MULTIPLE)4 PRINC ANESTHETIST:

5 ASST ANESTHETIST:

6 ANESTHESIOLOGIST SUPVR:

7 RELIEF ANESTHETIST:

8 ANESTHESIA TECHNIQUE: (MULTIPLE)9 ASA CLASS:

10 PERFUSIONIST:

11 ASST PERFUSIONIST:

12 OR CIRC SUPPORT: (MULTIPLE)13 OR SCRUB SUPPORT: (MULTIPLE)14 OTHER PERSONS IN OR: (MULTIPLE)15 SURGERY POSITION: (MULTIPLE)(DATA)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 3 OF 7

1 RESTR & POSITION AIDS: (MULTIPLE)(DATA)2 HAIR REMOVAL BY:

3 HAIR REMOVAL METHOD:

4 HAIR REMOVAL COMMENTS: (WORD PROCESSING)5 SKIN PREPPED BY (1):

6 SKIN PREPPED BY (2):

7 SKIN PREP AGENTS:

8 SECOND SKIN PREP AGENT:

9 ELECTROCAUTERY UNIT:

10 ESU COAG RANGE:

11 ESU CUTTING RANGE:

12 ELECTROGROUND POSITION:

13 ELECTROGROUND POSITION (2):

14 SEQUENTIAL COMPRESSION DEVICE:

15 THERMAL UNIT: (MULTIPLE)

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 4 OF 7

1 FOLEY CATHETER INSERTED BY:

2 CONFIRM PATIENT IDENTITY:

3 PROCEDURE TO BE PERFORMED:

4 SITE OF PROCEDURE:

5 CONFIRM VALID CONSENT:

6 CONFIRM PATIENT POSITION:

7 MARKED SITE CONFIRMED:

8 PREOPERATIVE IMAGES CONFIRMED:

9 CORRECT MEDICAL IMPLANTS:

10 AVAILABILITY OF SPECIAL EQUIP:

11 ANTIBIOTIC PROPHYLAXIS:

12 APPROPRIATE DVT PROPHYLAXIS:

13 BLOOD AVAILABILITY:

14 CHECKLIST COMMENT: (WORD PROCESSING)15 TIME-OUT DOCUMENT COMPLETED BY:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 5 OF 7

1 TIME-OUT COMPLETED:

2 TIME OPERATION BEGAN:

3 DEVICE(S):

4 IRRIGATION: (MULTIPLE)5 MEDICATIONS: (MULTIPLE)6 TIME TOURNIQUET APPLIED: (MULTIPLE)7 CELL SAVER: (MULTIPLE)8 PROSTHESIS INSTALLED: (MULTIPLE)9 LASER PERFORMED: (MULTIPLE)10 SPECIMENS: (WORD PROCESSING)11 CULTURES: (WORD PROCESSING)12 SPONGE FINAL COUNT CORRECT:

13 SHARPS FINAL COUNT CORRECT:

14 INSTRUMENT FINAL COUNT CORRECT:

15 SPONGE, SHARPS, & INST COUNTER:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 6 OF 7

1 COUNT VERIFIER:

2 WOUND SWEEP:

3 WOUND SWEEP COMMENTS: (WORD PROCESSING)4 INTRA-OPERATIVE X-RAY:

5 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)6 NURSING CARE COMMENTS: (WORD PROCESSING)7 SURGERY SPECIALTY: TRANSPLANTATION8 PRINCIPAL PROCEDURE: SRONRPT2 CASE9 LATERALITY OF PROCEDURE:

10 OTHER PROCEDURES: (MULTIPLE)11 ROBOTIC ASSISTANCE (Y/N):

12 WOUND CLASSIFICATION:

13 ATTENDING/RES SUP CODE:

14 PACKING:

15 DRESSING:

Enter Screen Server Function: <u>\<enter\></u>

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#002 TEST,PATIENT PAGE 7 OF 7

1 TUBES AND DRAINS:

2 TIME OPERATION ENDS:

3 POSTOP SKIN INTEG:

4 DISCHARGED VIA:

5 OP DISPOSITION:

6 REPORT GIVEN TO:

7 TIME PAT OUT OR:

8 SURGEON VER DONOR ORG PRE-ANES:

Enter Screen Server Function:

#### Executing the SROMEN-OPER Input Template

To execute the SROMEN-OPER input template, the user must select the Operation option \[SROMEN-OP\].

The SROMEN-OPER input template no longer contains POSSIBLE ITEM RETENTION so all fields following the removed POSSIBLE ITEM RETENTION field have moved up a position in the display:

\*\* OPERATION \*\* CASE \#000 TEST,PATIENT PAGE 1 OF 3

1 TIME PAT IN HOLD AREA:

2 TIME PAT IN OR:

3 ANES CARE TIME BLOCK: (MULTIPLE)4 TIME OPERATION BEGAN:

5 SPECIMENS: (WORD PROCESSING)6 CULTURES: (WORD PROCESSING)7 THERMAL UNIT: (MULTIPLE)8 ELECTROCAUTERY UNIT:

9 ESU COAG RANGE:

10 ESU CUTTING RANGE:

11 TIME TOURNIQUET APPLIED: (MULTIPLE)12 PROSTHESIS INSTALLED: (MULTIPLE)13 REPLACEMENT FLUID TYPE: (MULTIPLE)14 IRRIGATION: (MULTIPLE)15 MEDICATIONS: (MULTIPLE)

Enter Screen Server Function:

*\<screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,PATIENT PAGE 2 OF 3

1 SPONGE FINAL COUNT CORRECT:

2 SHARPS FINAL COUNT CORRECT:

3 INSTRUMENT FINAL COUNT CORRECT:

4 WOUND SWEEP:

5 WOUND SWEEP COMMENTS: (WORD PROCESSING)6 INTRA-OPERATIVE X-RAY:

7 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)8 SPONGE, SHARPS, & INST COUNTER:

9 COUNT VERIFIER:

10 SEQUENTIAL COMPRESSION DEVICE:

11 LASER PERFORMED: (MULTIPLE)12 CELL SAVER: (MULTIPLE)13 NURSING CARE COMMENTS: (WORD PROCESSING)14 PRINCIPAL PRE-OP DIAGNOSIS: TEST15 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

Enter Screen Server Function:

*\<screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,PATIENT PAGE 3 OF 3

1 PRINCIPAL PROCEDURE: SRONRPT CASE2 PLANNED PRIN PROCEDURE CODE : 100103 ROBOTIC ASSISTANCE (Y/N):

4 OTHER PROCEDURES: (MULTIPLE)5 INDICATIONS FOR OPERATIONS: (WORD PROCESSING)(DATA)6 BRIEF CLIN HISTORY: (WORD PROCESSING)

Enter Screen Server Function:

#### Executing the SROMEN-OUT Input Template

To execute the SROMEN-OUT input template, the user must select the Operation (Short Screen) option \[SROMEN-OUT\].

The SROMEN-OUT input template no longer contains POSSIBLE ITEM RETENTION so all fields following the removed POSSIBLE ITEM RETENTION field have moved up a position in the display:

\*\* SHORT SCREEN \*\* CASE \#000 TEST,PATIENT PAGE 1 OF 3

1 DATE OF OPERATION: JAN 25, 20242 HOSPITAL ADMISSION STATUS:

3 PRIMARY SURGEON: TEST,PROVIDER4 PRINCIPAL PRE-OP DIAGNOSIS: TEST5 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

6 OTHER PREOP DIAGNOSIS: (MULTIPLE)7 PRINCIPAL PROCEDURE: SRONRPT CASE8 PLANNED PRIN PROCEDURE CODE : 100109 ROBOTIC ASSISTANCE (Y/N):

10 OTHER PROCEDURES: (MULTIPLE)11 HAIR REMOVAL BY:

12 HAIR REMOVAL METHOD:

13 HAIR REMOVAL COMMENTS: (WORD PROCESSING)14 TIME PAT IN OR:

15 TIME OPERATION BEGAN:

Enter Screen Server Function:

*\<screen clears\>*\*\* SHORT SCREEN \*\* CASE \#000 TEST,PATIENT PAGE 2 OF 3

1 TIME OPERATION ENDS:

2 TIME PAT OUT OR:

3 IV STARTED BY:

4 OR CIRC SUPPORT: (MULTIPLE)5 OR SCRUB SUPPORT: (MULTIPLE)6 OP ROOM PROCEDURE PERFORMED:

7 FIRST ASST:

8 SPONGE FINAL COUNT CORRECT:

9 SHARPS FINAL COUNT CORRECT:

10 INSTRUMENT FINAL COUNT CORRECT:

11 WOUND SWEEP:

12 WOUND SWEEP COMMENTS: (WORD PROCESSING)13 INTRA-OPERATIVE X-RAY:

14 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)15 SPONGE, SHARPS, & INST COUNTER:

Enter Screen Server Function:

*\<screen clears\>*\*\* SHORT SCREEN \*\* CASE \#000 TEST,PATIENT PAGE 3 OF 3

1 COUNT VERIFIER:

2 SURGERY SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)3 WOUND CLASSIFICATION:

4 ATTENDING SURGEON: TEST,PROVIDER5 ATTENDING/RES SUP CODE:

6 SPECIMENS: (WORD PROCESSING)7 CULTURES: (WORD PROCESSING)8 NURSING CARE COMMENTS: (WORD PROCESSING)9 ASA CLASS:

10 PRINC ANESTHETIST:

11 ANESTHESIA TECHNIQUE: (MULTIPLE)12 ANES CARE TIME BLOCK: (MULTIPLE)13 DELAY CAUSE: (MULTIPLE)

Enter Screen Server Function:

### POSSIBLE ITEM RETENTION Field Deactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch deactivates the POSSIBLE ITEM RETENTION (#630) field in the SURGERY (#130) file by marking it as “UNEDITABLE” in VA FileMan and removing it from all VistA Surgery input templates for entry/editing.

STANDARD DATA DICTIONARY \#130 -- SURGERY FILE 1/25/24 PAGE 1

STORED IN ^SRF( (### ENTRIES) SITE: XXX.XXX.VA.GOV UCI: XXX,XXX (VERSION 3)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

130,630 POSSIBLE ITEM RETENTION 25;6 SET

Possible Item Retention

'Y' FOR YES;

'N' FOR NO;

LAST EDITED: AUG 18, 2022

HELP-PROMPT: <span class="mark">\*\*THIS FIELD IS NO LONGER USED\*\*</span> Answer YES if

the surgical field has the potential for

leaving behind a sponge, sharp, or instrument.

DESCRIPTION: VASQIP Definition (2015): This field is

intended to capture whether the surgical field

has the potential for leaving a retained

surgical item, including sponge, sharp, or

instrument behind. A retained surgical item

includes instruments, sharps, sponges or any

materials used by the surgical team performing

the operative procedure. Sharps include

surgical needles, aspirating needles, blunt

needles, scalpel blades or any items with a

sharp or pointed edge posing a risk for skin

puncture by the surgical team. Sponges include

cotton gauze sponges, laparotomy pads, surgical

towels or any absorbent materials not intended

to remain in the patient's body after the

surgical procedure is completed.

> **NOTE:** This field does not identify that a

retained surgical item actually was found or

occurred.

<span class="mark">UNEDITABLE</span>

### DONOR VESSEL DISPOSITION Field Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds ‘NA’ FOR NOT APPLICABLE to the SET OF CODES for the DONOR VESSEL DISPOSITION (#665) field in the SURGERY (#130) file.

STANDARD DATA DICTIONARY \#130 -- SURGERY FILE 1/25/24 PAGE 1

STORED IN ^SRF( (### ENTRIES) SITE: XXX.XXX.VA.GOV UCI: XXX,XXX (VERSION 3

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

130,665 DONOR VESSEL DISPOSITION VER1;16 SET

Donor Vessel Disposition if not used

'N' FOR NO DONOR VESSELS RECEIVED;

'D' FOR DISCARDED;

'R' FOR RETURNED TO OPO;

'S' FOR STORED;

<span class="mark">'NA' FOR NOT APPLICABLE;</span>

LAST EDITED: MAY 18, 2022

HELP-PROMPT: Enter disposition of donor vessels.

DESCRIPTION:

Document disposition of donor vessels.

The DONOR VESSEL DISPOSITION (#665) field is included in the Nurse Intraoperative Report option’s SRONRPT1 input template.

Example: Setting Donor Vessel Disposition to ‘NA’ using the Nurse Intraoperative Report option

\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 9 OF 9

1 DONOR VESSEL USAGE:

2 DONOR VESSEL DISPOSITION:

Enter Screen Server Function: <u>2</u>Donor Vessel Disposition if not used: <u>?</u>Enter disposition of donor vessels.Choose from:N NO DONOR VESSELS RECEIVEDD DISCARDEDR RETURNED TO OPOS STORED<span class="mark">NA NOT APPLICABLE</span>Donor Vessel Disposition if not used: <u>??</u>Document disposition of donor vessels.Choose from:N NO DONOR VESSELS RECEIVEDD DISCARDEDR RETURNED TO OPOS STORED<span class="mark">NA NOT APPLICABLE</span>Donor Vessel Disposition if not used: <u>NA</u> NOT APPLICABLE

*\<screen clears\>*\*\* NURSE INTRAOP \*\* CASE \#001 TEST,PATIENT PAGE 9 OF 9

1 DONOR VESSEL USAGE:

2 DONOR VESSEL DISPOSITION: <span class="mark">NOT APPLICABLE</span>

Enter Screen Server Function:

The DONOR VESSEL DISPOSITION (#665) field is transmitted to Veterans Affairs Surgery Quality Improvement Program (VASQIP) centralized database for Non-Cardiac & Cardiac Transplant surgery cases. Surgery Risk Assessment transmissions have been modified to accommodate the new 2-character code. Other than entering a new value for the field, you will see no other visible change related to transmissions.

### Spelling Correction of GLASSES/GOOGLES to GLASSES/GOGGLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch corrects the spelling for GLASSES/GOOGLES to GLASSES/GOGGLES in the SRONRPT4 routine for display/print in the Nurse Intraoperative Report.

Example: GLASSES/GOGGLES in the Nurse Intraoperative Report

MEDICAL RECORD NURSE INTRAOPERATIVE REPORT - CASE \#000 PAGE 4

Laser Performed:

TEST LASER Laser Type: N/A

Laser Start Time: N/A Laser End Date: N/A

Laser Test Fire: N/A Laser Delivery System: N/A

Pulse Mode: N/A Power/Average Power: N/A

Interval/Repetition Rate: N/A Total Joules Delivered: N/A

Watts Delivered: N/A Wave Form: N/A

Pulse Width: N/A Energy Joules: N/A

Duration: N/A

Laser On Standby: N/A Laser Off and Key Secured : N/A

Patient Precautions: SAFETY <span class="mark">GLASSES/GOGGLES</span>

Personnel Precautions: N/A

Immediate Use Steam Sterilization Episodes:

Contamination: 0

SPS Processing/OR Management Issues: 0

Emergency Case: 0

No Better Option: 0

Loaner or Short Notice Instrument: 0

Decontamination of Instruments Contaminated During the Case: 0

Press \<return\> to continue, 'A' to access Nurse Intraoperative Report

functions, or '^' to exit:

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: SR*3*182 Surgery Release Notes

### Department of Veterans Affairs Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *(This page included for two-sided copying.)*

### TIME-OUT COMPLETED field to accept time entry and stuff the current date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SR\*3\*182 V7:

- Bug fix to the non-cardiac transmission which was generating error messages in the Hines database
- New mechanical circulatory support occurrence definitions update
- The update cardiac transmission that includes the INTRAOP DEVICE TYPE and POSTOP DEVICE TYPE fields in line \#24 positions 68 and 69
- TIME-OUT COMPLETED & TIME-OUT DOCUMENT COMPLETED BY fields will no longer be required to sign the NIR report if the surgical case has a status of "Aborted"

> Each new version deployed to National Patch Module (NPM) in FORUM.

> <span id="_bookmark3" class="anchor"></span>Release Inventory

> The following version of Patch 182 is available for review and implementation by the VA Release Manager and has been forwarded via FORUM to the VA Release Manager for Surgery-Annual Surgery Updates.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Deliverable</strong></th>
<th><strong>Method</strong></th>
<th><strong>Location</strong></th>
<th><strong>Receiver</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SR*3*182 V7</td>
<td><p>FORUM</p>
<p>Mail</p></td>
<td>FORUM</td>
<td><mark>REDACTED</mark></td>
<td>MUMPS Build</td>
</tr>
</tbody>
</table>

> <span id="_bookmark4" class="anchor"></span>ASU Known Issues included in the Milestone 2 Issues Brief:

## Aborted cases – Reported by Tennessee Valley:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Tennessee Valley has raised an issue related to signing the NIR for aborted cases where the software required the data of the TIME-OUT COMPLETED field to be entered and the time out does not have to occur prior to aborting the case because the final time out takes place immediately before incision. This is after anesthesia induces the patient, which was what happened in this case. Anesthesia induction can cause systemic reactions in patients that may result in the surgery being aborted. The problem is that the case in the chart cannot be signed without the time out field being filled in.

> The recommended work around solution for this is to enter a time between lies between TIME PAT IN OR and TIME PAT OUT OR and sign the NIR report and then delete~~s~~ this data which will force addendum for the NIR and record the reason for the change in the comment for the addendum.

#### This issue is resolved in Version 7 of the patch.

## DSS items – Reported by Cleveland:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Item \#1: The VISIN Surgery Workgroup report is generating an error since patch 182 was installed that is due to MAJOR/MINOR filed has been removed from data entry screens and will no longer be populated. This report comes from DSS data that originates in the Surgery package. Team was informed by Valerie Pettigrew that DSS is consulting with the VISINs to redesign the whole report.

> Recommended solution: DSS is updating its report to comply with ASU Patch 182 data changes. No change to Patch 182 is needed.

> Item \#2: Date is not flowing to and from the DSS Inc live data package. This does not seem to be an error with the ASU Patch but an error with DSS. The reporter of this issue, <span class="mark">REDACTED</span>, has informed that the DSS Inc is aware of this and they require access to place a fix in their software and the reason for this is the new changes to the selection options made by ASU patch to the VALID CONSENT FORM.

> Recommended solution: DSS is fixing their software to comply with the changes made by ASU Patch 182 on the VALID CONSENT FORM. No change to Patch 182 is needed.

> (This page included for two-sided copying.)

## Update CPT EXCLUSIONS file (#137)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CPT EXCLUSIONS file (#137) is updated with the excluded CPT codes for Fiscal Year 2014. This file is used internally by the software to identify surgical cases eligible for assessment.

## Standard SURGERY CANCELLATION REASON file (#135)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Existing entries in the SURGERY CANCELLATION REASON file (#135) were made inactive so that they can no longer be selected when entering a cancellation reason. A new standard set of cancellation reasons was added to the file and will be the only reasons that may be selected when cancelling a surgical case. The CANCEL REASON field (#18) description was updated to further describe the new standard list. The cancellation reason was added to the list of transmitted data items transmitted to Denver.

> The cancellation comment field will no longer be prompted to the user during the cancellation process. This is the standard list of cancellation reasons:

1.  PATIENT RELATED ISSUE
2.  ENVIRONMENTAL ISSUE
3.  STAFF ISSUE
4.  PATIENT HEALTH STATUS
5.  CLIN URGENT/EMERGENT CASE
6.  SCHED ISSUES NON EMERGENT CASE
7.  UNAVAILABLE BED
8.  UNAVAILABLE EQUIP EXCLUDE RME
9.  UNAVAILABLE REUSABLE EQUP-RME
10. CASE MOVED TO EARLIER DATE

#### Cancellation Field – SURGERY File (#130)

| Field Name and Number   | Description of Change                                         |
|-----------------------------|-------------------------------------------------------------------|
| PRIMARY CANCEL REASON (#18) | Name change as well as Field Description and Functionality Update |

#### Standard Cancellation Reasons – Modified Option

| Option Name                         | Description of Change |
|-----------------------------------------|---------------------------|
| *Cancel Scheduled Operation* \[SRSCAN\] | Functionality Update      |
| *Update Cancellation Reason* \[SRSUPC\] | Functionality Update      |

## Time Out Verified Utilizing Checklist Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CHECKLIST CONFIRMED BY field (#.69) is renamed to "TIME-OUT DOCUMENT COMPLETED BY".

> The TIME-OUT COMPLETED field (#74) has been added as new field and will be auto-populated with military formatted timestamp when the user enter the TIME-OUT DOCUMENT COMPLETED BY field.

#### SURGERY File (#130)

| Field Name and Number     | Description of Change |
|-------------------------------|---------------------------|
| TIME-OUT COMPLETED (#74)      | New field                 |
| CHECKLIST CONFIRMED BY (#.69) | Field Label rename        |

#### Modified Option

| Option Name                                         | Description of Change |
|---------------------------------------------------------|---------------------------|
| *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\] | Functionality Update      |

## Operation Screen Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The POSSIBLE ITEM RETENTION field (#630), WOUND SWEEP field (#633), WOUND SWEEP COMMENTS field (#635), INTRAOPERATIVE X-RAY field (#636), and the INTRAOPERATIVE X-

> RAY COMMENTS field (#637) have been added as new fields to the data entry screen.

> The listed above new fields are added to the transmissions for cardiac assessments, non-cardiac assessments, and 1-liner (non-assessed) transmissions. Field \#630, \#633, and \#636 are made required to sign the NIR report.

#### SURGERY File (#130)

| Field Name and Number                  | Description of Change |
|--------------------------------------------|---------------------------|
| POSSIBLE ITEM RETENTION field (#630)       | New field                 |
| WOUND SWEEP field (#633)                   | New field                 |
| WOUND SWEEP COMMENTS field (#635)          | New field                 |
| INTRAOPERATIVE X-RAY field (#636)          | New field                 |
| INTRAOPERATIVE X-RAY COMMENTS field (#637) | New field                 |

#### Modified Option

| Option Name                           | Description of Change |
|-------------------------------------------|---------------------------|
| *Operation* \[SROMEN-OP\]                 | Functionality Update      |
| *Operation (Short Screen)* \[SROMEN-OUT\] | Functionality Update      |
| *Nurse Intraoperative Report* \[SRONRPT\] | Functionality Update      |

### The ANGINA TIMEFRAME field (#643) has been added as new field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The HYPERTENSION field (#463) has been replace with new field, HYPERTENSION field (#641)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The PCI field (#640) has been replaced by existing field, PCI (#351)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The new fields have been added to the Print Risk Assessment, and the cardiac data transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The data definition of the PRIOR HEART SURGERIES field (#485) has been updates.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The data detention of the POSITIVE DRUG SCREENING field (#618) has been updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Existing field, PREOPERATIVE SLEEP APNEA (#237.1) has been added to the data entry screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The following fields have been removed from the Cardiac Procedures Operative Data (Enter/Edit) \[SROA CARDIAC PROCEDURES\] option and are removed from the print assessment report, from missing cardiac items, and be replaced with blanks in cardiac data transmission:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Number with Vein o Number with IMA
- Number with Radial Artery o Number with Other Artery
- Number with Other Conduit o LV Aneurysmectomy
- Aortic Valve Procedure o Mitral Valve Procedure
- Bridge to transplant/Device/Destination Therapy
- TMR (Transmyocardial laser revascularization)
- Tricuspid Valve Procedure o Pulmonary Valve Procedure
- Maze procedure o ASD repair
- VSD repair o Myectomy
- Myxoma resection o Other tumor resection
- Cardiac transplant o Great Vessel repair
- Endovascular repair of aorta o Other cardiac procedure(s)
- Foreign Body Removal o Pericardectomy
- Other cardiac procedure(s)
- The OPERATIVE DEATH field (#384) has been removed from the Outcome Information (Enter/Edit) \[SROA CARDIAC-OUTCOMES\] option.
- The CARDIAC SURG PERFORMED NON-VA field (#472) has been removed from the SROA Resource Data \[CARDIAC RESOURCE\] option.
- The HOSPITAL DISCHARGE DATE field (#419) has been added to the 1-liner transmission data.
- The "N/A" selection option has been inactivated in all listed below fields and replaced with new selection "NA".
- SPONGE COUNT CORRECT (Y/N) field (#44)
- SHARPS COUNT CORRECT (Y/N) field (#45)
- INSTRUMENT COUNT CORRECT (Y/N) field (#46)
- CONVERT FROM OFF PUMP TO CPB field (#469)
- POSITIVE DRUG SCREENING field (#618)
- The following fields have been renamed as follows:
- SURGEON field (#.14) to PRIMARY SURGEON
- ATTEND SURG field (#.164) to ATTENDING SURGEON
- ATTENDING CODE field (#.166) to ATTENDING/RES SUP CODE
- OPERATING ROOM field (#.02) to OPROOM PROCEDURE PERFORMED
- IN/OUT-PATIENT STATUS field (#.011) to HOSPITAL ADMISSION STATUS

### From: SR*3*184 Surgery Release Notes

### The “SCNR WAS ON A/L” criteria has been changed to “10% RULE"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The "STUDY CRITERIA" criteria has been changed to "INCLSN CRTA NOT MET"
- Option \#4 and \#5 under the List of Surgery Risk Assessments \[SROA ASSESMENT LIST\] options are placed out of order and are not selectable after this enhancement.
- Default the DC/REL DESTINATION field (#685) to “1-HOME” when capturing the information from PIMS records using the Resource Data \[SROA CARDIAC RESOURCE\] option.

> SR\*3\*184 V3:

### The title field of the HX RAD RX PLANNED SURG FIELD (#674) has been updated to capitalize each word.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Fix a bug discovered while investigating of Upstate NY error related to the Schedule of Operations report.
- Implementation of Cleveland recommendation related to the deactivated items of the List of Surgery Risk Assessments option so that software goes back to option list instead of Risk menu when deactivated options (#4 or \#5) are selected.

> SR\*3\*184 v4:

- Fix defect reported by Minneapolis related to the Hospital Admission Status field printing blank while printing the Non-Cardiac assessment.
- Fix defect reported by Upstate NY related to printing of the BLOOD AVAILABILITY field (#610) when “NI” is selected.
- Change the “Unplanned Intub W/In 30 Days“ occurrence label to be “OUT- OF- OR UNPLANNED INTUBATION” (#422)in cardiac and non-cardiac print assessment.
- Enhance the Request Operation/Schedule Operation options to accept additional 90000 CPT codes for the PLANNED PRIN PROCEDURE CODE field. Allowed 90000 codes are as follows: 90865, 90870, 91040, 91120, 91122, 92502, 92504, 92511, 92611, 92612, 92613, 92614, 92615, 92616, 92617, 92960, 92961, 92970, 92986, 92987, 92990, 93312, 93313, 93314, 93315, 93316, 93317, 93318, 93355, 93505, 93580, 93581, 93582, 93583, 93631, 93650, 95940, 95955, 95958, 95961, 95990, 95991, 96420, 96422, 96425, 96440, 96450, 96521, 96522, 97597, 97598, 97602, 97605, 97606, 97607, 97608, 99144, 99149

> SR\*3\*184 v5:

### Include a missing routine which was modified for v4 but not included in the build of v4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each new version deployed to National Patch Module (NPM) in FORUM.

> <span id="_bookmark3" class="anchor"></span>Release Inventory

> The following version of Patch 184 is available for review and implementation by the VA Release Manager and has been forwarded via FORUM to the VA Release Manager for Surgery-Annual Surgery Updates.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Deliverable</strong></th>
<th><strong>Method</strong></th>
<th><strong>Location</strong></th>
<th><strong>Receiver</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SR*3*184 V5</td>
<td><p>FORUM</p>
<p>Mail</p></td>
<td>FORUM</td>
<td>VHA Release Manager</td>
<td>MUMPS Build</td>
</tr>
</tbody>
</table>

## Request Operation Screen Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The PALLIATION field (#661) has been added as new field.
- This patch adds the SPECIAL EQUIPMENT, PLANNED IMPLANTS, PHARMACY ITEMS, SPECIAL INSTRUMENTS, and SPECIAL SUPPLIES as new multiples in the SURGERY file (#130). The new multiples are added to the Operation Request options, the Operation Scheduling options, and the Schedule of Operations report option.
- This patch adds the SPINAL LEVEL field (#136) under the Operation Request

> options, the Operation Scheduling options, and the Schedule of Operations report option. This field will be available for edit only if the PLANNED PRIN PROCEDURE CODE (CPT) of the case matches one of the CPTs listed in the CPT-SPINAL LEVEL file (#131.4) which is introduced by this patch.

- The PLANNED ADMISSION STATUS field (#.013) has been added as new field and it has been made required for case creation using the

> request operation options and replaced the HOSPITAL ADMISSION STATUS field (#.011) in the Request Operation screen. The HOSPITAL ADMISSION STATUS (#.011) will be initially auto populated from the new field.

#### SURGERY File (#130)

| Field Name and Number                                | Description of Change |
|----------------------------------------------------------|---------------------------|
| PALLIATION (#661)                                        | New field                 |
| PLANNED ADMISSION STATUS (#.013)                         | New field                 |
| SPECIAL EQUIPMENT (#680), Multiple \#130.25              | New field                 |
| PLANNED IMPLANTS Multiple (#681), Multiple \#130.0681    | New field                 |
| PHARMACY ITEMS Multiple (#684), Multiple \#130.0684      | New field                 |
| SPECIAL INSTRUMENTS Multiple (#683), Multiple \#130.0683 | New field                 |
| SPECIAL SUPPLIES Multiple (#682), Multiple \#130.0682    | New field                 |

- The following files and their fields have been added to the Surgery package by this enhancement:

#### SPECIAL EQUIPMENT File (#131.3)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| NAME (#.01)               | New Field                 |
| NUMBER (#2)               | New Field                 |
| INACTIVE? (#3)            | New Field                 |
| SURGICAL SPECIALTIES (#4) | New Field                 |

#### PLANNED IMPLANT File (#131.5)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| NAME (#.01)               | New Field                 |
| SIZE (#1)                 | New Field                 |
| INACTIVE? (#2)            | New Field                 |

| MODEL (#3)                | New Field |
|---------------------------|-----------|
| VENDOR (#4)               | New Field |
| SURGICAL SPECIALTIES (#6) | New Field |

#### PHARMACY ITEMS File (#131.06)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| DRUG NAME (#.01)          | New Field                 |
| DOSE (#1)                 | New Field                 |
| INACTIVE? (#2)            | New Field                 |
| DRUG COMMENTS (#3)        | New Field                 |
| SURGICAL SPECIALTIES (#4) | New Field                 |

#### SPECIAL INSTRUMENTS File (#131.02)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| NAME (#.01)               | New Field                 |
| NUMBER (#1)               | New Field                 |
| INACTIVE? (#2)            | New Field                 |
| SURGICAL SPECIALTIES (#3) | New Field                 |

#### SPECIAL SUPPLIES File (#131.04)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| NAME (#.01)               | New Field                 |
| SIZE (#1)                 | New Field                 |
| INACTIVE? (#2)            | New Field                 |
| MODEL (#3)                | New Field                 |
| VENDOR (#4)               | New Field                 |
| SURGICAL SPECIALTIES (#5) | New Field                 |

#### CPT-SPINAL LEVEL File (#131.4)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| CPT CODE (#.01)           | New Field                 |

#### Modified Options

| Option Name                                      | Description of Change |
|------------------------------------------------------|---------------------------|
| *Schedule of Operations* \[SROSCH\]                  | Functionality change      |
| *Update Site Configurable Files* \[SR UPDATE FILES\] | Functionality change      |

## Time-Out Verified checklist Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new fields listed below were added to:

- SURGERY file (#130)
- This patch adds the new fields to the Time Out Verified Utilizing Checklist \[SROMEN-VERF\] and the Nurse Intraoperative Report \[SRONRPT\] data entry screens if the PLANNED PRIN PROCEDURE CODE field (#27) is set to a value that lies within a given range of CPT codes
- The new fields will be required to sign the NIR report if the PLANNED PRIN PROCEDURE CODE field (#27) is set to a value that lies within a given range of CPT codes
- Cardiac, Non-Cardiac, and 1-liner data transmissions

#### SURGERY File (#130)

| Field Name and Number                             | Description of Change |
|-------------------------------------------------------|---------------------------|
| UNOS NUMBER (#648)                                    | New field                 |
| DONOR SEROLOGY HCV (#649)                             | New field                 |
| DONOR SEROLOGY HBV (#650)                             | New field                 |
| DONOR SEROLOGY CMV (#651)                             | New field                 |
| DONOR SEROLOGY HIV (#652)                             | New field                 |
| DONOR ABO TYPE (#653)                                 | New field                 |
| RECIPIENT ABO TYPE (#654)                             | New field                 |
| BLOOD BANK ABO VERIFICATION (#655)                    | New field                 |
| BLOOD BANK ABO VER COMMENTS (#746)                    | New field                 |
| D/T BLOOD BANK ABO VERIF (#747)                       | New field                 |
| OR ABO VERIFICATION (Y/N)(#656)                       | New field                 |
| OR ABO VER COMMENTS (#748)                            | New field                 |
| D/T OR ABO VERIF (#749)                               | New field                 |
| SURGEON VERIFYING UNET (#657)                         | New field                 |
| UNET VERIF BY SURGEON (Y/N)(#750)                     | New field                 |
| ORGAN VER PRE-ANESTHESIA (#658)                       | New field                 |
| SURGEON VER ORGAN PRE-ANES (#751)                     | New field                 |
| SURGEON VER DONOR ORG PRE-ANES (#659)                 | New field                 |
| DONOR ORG VER PRE-ANES (#752)                         | New field                 |
| ORGAN VER PRE-TRANSPLANT (#660)                       | New field                 |
| SURGEON VER ORG PRE-TRANSPLANT (#753)                 | New field                 |
| DONOR VESSEL USAGE (#663)                             | New field                 |
| DONOR VESSEL UNOS ID (#664) , Multiple \#130.0664     | New field                 |
| DONOR VESSEL DISPOSITION (#665)                       | New field                 |
| ORGANS TO BE TRANSPLANTED (#647), Multiple \#130.0647 | New field                 |

#### Modified Option

| Option Name                                         | Description of Change |
|---------------------------------------------------------|---------------------------|
| *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\] | New Fields added          |
| *Nurse Intraoperative Report* \[SRONRPT\]               | New Fields added          |

## Cardiac/Non-Cardiac Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following changes were made to the *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\] option:

- CONGESTIVE HEART FAILURE PREOP (#423) field is used instead of the CONGESTIVE HEART FAILURE (#207) field which has been marked as obsolete
- The data definition of the “PREOP FUNCT. HEALTH STATUS” field (#492) has been updated and will be used under this option instead of the “FUNCTIONAL HEALTH STATUS” field (#240) which has been marked as obsolete
- The following fields were added:
- IMPAIRED COGNITIVE FUNCTION (#662)
- SLEEP APNEA-COMPLIANCE (#667)
- The following fields were removed from the data entry screen, missing items, and from Cardiac transmission data:
- PULMONARY RALES (#348)
- CURRENT DIGOXIN USE (#354)
- RESTING ST DEPRESSION (#350)

> The following field was added under the *Cardiac Procedures Operative Data* (Enter/Edit) \[SROA CARDIAC PROCEDURES\] option:

- BRIDGE TO TRANSPLANT/DEVICE (#481)

### The following updates were made to the *Resource Data* \[SROA CARDIAC RESOURCE\] screen as follows:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added the following fields:
- TRANSFER STATUS (#413)
- DATE OF DEATH (#342) and the "30 DAY DEATH" (#342.1)
- HISTORY OF CANCER DIAGNOSIS (#673)
- HX RAD RX PLANNED SURG FIELD (#674)
- PRIOR SURG SAME OP FIELD (#677)
- RESIDENCE 30 DAYS PREOP (#670)
- AMBULATION DEVICE PREOP (#671)
- DC/REL DESTINATION (#685)
- Removed the CARDIAC RESOURCE DATA COMMENTS (#431)
- The HOSPITAL DISCHARGE DATE (#419) will no longer be checked against the missing items for Cardiac assessment.

> The following fields were added to the *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\] option:

- IMPAIRED COGNITIVE FUNCTION (#662)
- SLEEP APNEA-COMPLIANCE (#667)
- CHEMO FOR MALIG LAST 90 DAYS (#338.3)
- RESIDENCE 30 DAYS PREOP (#670)
- AMBULATION DEVICE PREOP (#671)
- HISTORY OF CANCER DIAGNOSIS (#673)
- HX RAD RX PLANNED SURG FIELD (#674)
- PRIOR SURG SAME OP FIELD (#677)

> This patch removes the following fields under the *Operative Risk Summary Data* (Enter/Edit) \[SROA CLINICAL INFORMATION\] option:

- ESTIMATE OF MORTALITY (#364)
- CARDIAC RISK PREOP COMMENTS (#430)

> The *Outcome Information (Enter/Edit)* \[SROA CARDIAC-OUTCOMES\] option has been set out of order.

> This patch adds the DC/REL DESTINATION field (#685) to the *Patient Demographics (Enter/Edit)* \[SROA DEMOGRAPHICS\] screen.

#### SURGERY File (#130)

| Field Name and Number               | Description of Change |
|-----------------------------------------|---------------------------|
| \*CONGESTIVE HEART FAILURE (#207)       | Field Marked as Obsolete  |
| \*FUNCTIONAL HEALTH STATUS (#240)       | Field Marked as Obsolete  |
| \*CHEMOTHERAPY IN LAST 30 DAYS (#338.1) | Field Marked as Obsolete  |
| CHEMO FOR MALIG LAST 90 DAYS (#338.3)   | New field                 |
| \*PULMONARY RALES (#348)                | Field Marked as Obsolete  |
| \*CURRENT DIGOXIN USE (#354)            | Field Marked as Obsolete  |
| \*RESTING ST DEPRESSION (#350)          | Field Marked as Obsolete  |
| CONGESTIVE HEART FAILURE PREOP (#423)   | New field                 |
| PREOP FUNCT. HEALTH STATUS (#492)       | Field description update  |
| IMPAIRED COGNITIVE FUNCTION (#662)      | New field                 |
| SLEEP APNEA-COMPLIANCE (#667)           | New field                 |
| RESIDENCE 30 DAYS PREOP (#670)          | New field                 |
| AMBULATION DEVICE PREOP (#671)          | New field                 |
| HISTORY OF CANCER DIAGNOSIS (#673)      | New field                 |
| HX RAD RX PLANNED SURG FIELD (#674)     | New field                 |
| PRIOR SURG SAME OP FIELD (#677)         | New field                 |
| DC/REL DESTINATION (#685)               | New field                 |

#### Modified Options

| Option Name                                                              | Description of Change                           |
|------------------------------------------------------------------------------|-----------------------------------------------------|
| *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]            | New fields added, fields updated and fields removed |
| *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\]                  | New fields added                                    |
| *Cardiac Procedures Operative Data* (Enter/Edit) \[SROA CARDIAC PROCEDURES\] | New field added                                     |

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><em>Resource Data</em> [SROA CARDIAC RESOURCE]</th>
<th><p>New fields added and</p>
<p>removed a field</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Operative Risk Summary Data</em> (Enter/Edit) [SROA CARDIAC OPERATIVE RISK]</td>
<td>Fields removed</td>
</tr>
<tr class="even">
<td><em>Outcome Information (Enter/Edit)</em> [SROA CARDIAC-OUTCOMES]</td>
<td>Placed out of order</td>
</tr>
<tr class="odd">
<td><em>Patient Demographics (Enter/Edit)</em> [SROA DEMOPGRAPHICS]</td>
<td>New field added</td>
</tr>
</tbody>
</table>

## Case Aborted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Abort/Cancel Operation \[SROABRT\] option has been added as a new option under the Operation Menu \[SROPER\]. This menu should only be used if the patient has been taken to the operating room and no incision has been made. If an incision is made, the case should be completed and the discontinued procedure indicated in the record. Cancellation of future surgical cases should not use this option. This new option will prompt the user for CASE ABORTED field (#18.5) (“NO” default) and the cancellation information fields (CANCEL DATE, CANCELLATION TIMEFRAME and PRIMARY CANCEL REASON). The user will also be prompted to enter the TIME PAT IN OR and/or TIME PAT OUT OR if these fields were not previously entered, they will be required in order to proceed with aborting the case. The cancellation information fields (CANCEL DATE, CANCELLATION TIMEFRAME and PRIMARY CANCEL REASON) have been removed from all other data entry screens under the Operation Menu. If a surgical case is aborted the CANCELLATION TIMEFRAME field (#17.5) will be auto populated with

> “1-SURGERY CANCELLED \<48 HRS BEFORE SCHEDULED SURGERY”. This new field will be

> included in the 1-liner data transmission.

> \*\*\*

> There are known defects in Vista patch SR\*3\*184 with this new option. These will be addressed in a future patch.

> Defect 1) PRIMARY CANCEL REASON is not properly saved to the Surgery package.

> Defect 2) User is prompted for “Cancellation Avoidable” instead of “Cancellation Timeframe”

#### SURGERY File (#130)

| Field Name and Number | Description of Change |
|---------------------------|---------------------------|
| CASE ABORTED (#18.5)      | New field                 |

#### Operation Menu \[SROPER\]

| Option Name                      | Description of Change |
|--------------------------------------|---------------------------|
| *Abort/Cancel Operation* \[SROABRT\] | Added new option          |

## Height and Weight Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HEIGHT (#236) and the WEIGHT (#237) fields have been added to the first page of the Operation Startup \[SROMEN-START\] screen and will be auto populated using available data from the Vitals Package.

#### Modified Option

| Option Name                      | Description of Change |
|--------------------------------------|---------------------------|
| *Operation Startup* \[SROMEN-START\] | Added two fields          |

## Miscellaneous

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch updates the fields below in the SURGERY file (#130), the occurrence category descriptions listed below in the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5). This patch also replaced fields with new fields in order to enhance and refine certain data elements that are in common with Cardiac and Non-Cardiac Risk Assessments. All the associated data entry options, assessment printouts, missing items report, and transmissions are updated accordingly.

#### SURGERY File (#130)

| Field Name and Number            | Description of Change |
|--------------------------------------|---------------------------|
| DIABETES MELLITUS CHRONIC (#519)     | Definition update         |
| DIABETES MELLITUS PREOP MGMT (#520)  | Definition update         |
| ESOPHAGEAL VARICES (#213)            | Definition update         |
| FEV1 (#347)                          | Definition update         |
| ON VENTILATOR \>48 HOURS (#285)      | Definition update         |
| HISTORY OF COPD (#203)               | Definition update         |
| IMPAIRED SENSORIUM (#332)            | Definition update         |
| OBSERVATION ADMISSION DATE (#452)    | Definition update         |
| POSITIVE DRUG SCREENING (#618)       | Definition update         |
| GRAFT/PROSTHESIS/FLAP FAILURE (#261) | Definition update         |
| PERIPHERAL ARTERIAL DISEASE (#265)   | Definition update         |
| PRIOR MI (#205)                      | Definition update         |
| DEEP INCISIONAL SSI (#249)           | Definition update         |
| STEROID USE FOR CHRONIC COND. (#339) | Definition update         |
| REOPERATION FOR BLEEDING (#389)      | Definition update         |
| HOSPITAL ADMISSION STATUS (#.011)    | Definition update         |
| REPEAT CARDIAC SURG PROCEDURE (#391) | Definition update         |
| ORGAN/SPACE SSI (#488)               | Definition update         |
| BLOOD AVAILABILITY (#610)            | Definition update         |
| WOUND SWEEP (#633)                   | Definition update         |
| BLEEDING RISK DUE TO MED (#642)      | Definition update         |
| REASON FOR NO ASSESSMENT (#102)      | Definition update         |

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>PREOPERATIVE INFECTION (#.05)</th>
<th>Definition update</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>INTRAOP DEVICE TYPE field (#5) of the INTRAOPERATIVE</p>
<p>OCCURRENCES multiple (#1.14)</p></td>
<td>Definition update</td>
</tr>
<tr class="even">
<td><p>POSTOP DEVICE TYPE field (#15) of the POSTOP</p>
<p>OCCURRENCE multiple (#1.16)</p></td>
<td>Definition update</td>
</tr>
<tr class="odd">
<td>LIVER DISEASE/CIRRHOSIS (#666)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>IMMUNOCOMPROMISED STATE PREOP (#668)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>PULMONARY HTN (#669)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>NUTRITIONAL SUPPLEMENT PREOP (#672)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>PRIOR INFEC/INFLAM SURG FIELD (#675)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>HX DEEP VEIN THROMBOSIS (#676)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>AORTIC REGURGITATION (#686)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>INJURY TO ADJACENT ORGAN (#687)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>STOMA COMPLICATIONS (#688)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>NON-UNION (#689)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>IMPLANT INFECTIONS (#690)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>CHYLE/LYMPH LEAK (#691)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>ANASTOMOTIC LEAK (#692)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>FISTULA (#693)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>NECROTIZING SOFT TISS INFECT (#694)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>OTHER BLOOD PRODUCT UNITS (#695)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>PRESSORS USED INTRAOP (#696)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>MITRAL STENOSIS (#697)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>PCI INTERVENTION (#698)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>ATRIAL ARRHYTHMIAS (#699)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>HEAD OR NECK CANCER (#700)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>MACULAR DEGENERATION (#701)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>GLAUCOMA (#702)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>HX RETINAL DETACHMENT (#704)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>AXIAL LEN/ANTERIOR CHAM DEP (#705)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>CORNEAL GUTTAE/FUCHS ENDO (#706)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>DIABETIC RETINOPATHY (#707)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>COMPLEX CATARACT (#708)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>STATIN 30 DAYS PREOP (#709)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>IPSILAT CORTICAL EVENT PREOP (#710)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>PREOP MODIFIED RANKIN SCORE (#711)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>CAROTID SUR ANATOMIC HIGH RISK (#712)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>BYPASS CRITICAL LIMB ISCHEMIA (#713)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>ENDOLEAK AT COMPLETION (#715)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>HIGH HEART RATE 6HRS PREOP (#716)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>HIGH HEART RATE INTRAOP (#717)</td>
<td>New field</td>
</tr>
<tr class="odd">
<td>LOW ARTERIAL PRESS 6HRS PREOP (#718)</td>
<td>New field</td>
</tr>
<tr class="even">
<td>HIGH LACTIC ACID 6HRS PREOP (#719)</td>
<td>New field</td>
</tr>
</tbody>
</table>

| HIGH LACTIC ACID INTRAOP (#720)        | New field         |
|----------------------------------------|-------------------|
| LOWEST PH 6HRS PREOP (#721)            | New field         |
| LOWEST PH INTRAOP (#722)               | New field         |
| LOW ARTERIAL PRESS INTRAOP (#723)      | New field         |
| OLIGURIA \<60CC/2HRS 6HRS PREOP (#724) | New field         |
| OLIGURIA URINE OUTPUT INTRAOP (#725)   | New field         |
| LOWEST BICARBONATE 6HRS PREOP (#726)   | New field         |
| LOWEST BICARBONATE INTRAOP (#727)      | New field         |
| UNITS TRANSFUSED 6HRS PREOP (#728)     | New field         |
| VASOPRESSOR USAGE AT OR ENTRY (#729)   | New field         |
| CARDIAC ARREST 24HRS PREOP (#730)      | New field         |
| DIC 6HRS PREOP (#731)                  | New field         |
| HYPOXEMIA W/IN 6HRS PREOP (#732)       | New field         |
| ENDOLEAK AT FOLLOW-UP (#733)           | New field         |
| CARDIAC ARREST INTRAOP (#734)          | New field         |
| FLOPPY IRIS INTRAOP (#735)             | New field         |
| PREOP VISUAL ACUITY (#736)             | New field         |
| POSTOP VISUAL ACUITY (#737)            | New field         |
| ENDOPHTHALMITIS TYPE (#738)            | New field         |
| CYSTOID MACULAR EDEMA (#739)           | New field         |
| DISLOCATION OF OPERATIVE JOINT (#740)  | New field         |
| PERIPROSTHETIC FRACTURES (#741)        | New field         |
| D/T PAT ARRIVES HOSP DAY SURG (#742)   | New field         |
| D/T PAT LEAVES HOSP DAY SURG (#743)    | New field         |
| KIDNEY DONOR PROFILE INDEX (#744)      | New field         |
| EXPECTED POST TRANSPLANT INDEX (#745)  | New field         |
| SYMPTOMATIC UTI (#644)                 | Definition update |
| OUT-OF-OR UNPLANNED INTUBATION (#422)  | New field         |
| \*MECHANICAL VENT W/N 30 DAYS (#645)   | Inactivated       |

#### PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5)

| Occurrence Name - Number                     | Description of Change |
|--------------------------------------------------|---------------------------|
| DEEP INCISIONAL SSI - 2                          | Definition update         |
| ON VENTILATOR \> 48 HOURS - 6                    | Definition update         |
| GRAFT/PROSTHESIS/FLAP FAILURE – 19               | Definition update         |
| ORGAN/SPACE SSI - 35                             | Definition update         |
| SYMPTOMATIC UTI-CULTURE PLUS SIGN/SYMPTOM – 40   | Definition update         |
| MECHANICAL VENTILATION WITHIN 30 DAYS – 41       | Inactivated               |
| OUT-OF-OR UNPLANNED INTUBATION W/IN 30 DAYS – 42 | New                       |

## PLANNED PRIN PROCEDURE CODE Field (#27)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PLANNED PRIN PROCEDURE CODE field (#27) was changed to be a mandated field when creating Surgery cases and limits the selection of CPT codes to the following ranges: 10000-69999; 00100-01999; 70000-79999; allowed 90000 codes; D0000-D9999; xxxxT.

> <u>Allowed 90000 CPT codes:</u>

> 90865, 90870, 91040, 91120, 91122, 92502, 92504, 92511, 92611, 92612, 92613, 92614,

> 92615, 92616, 92617, 92960, 92961, 92970, 92986, 92987, 92990, 93312, 93313, 93314,

> 93315, 93316, 93317, 93318, 93355, 93505, 93580, 93581, 93582, 93583, 93631, 93650,

> 95940, 95955, 95958, 95961, 95990, 95991, 96420, 96422, 96425, 96440, 96450, 96521,

> 96522, 97597, 97598, 97602, 97605, 97606, 97607, 97608, 99144, 99149

> There is a known defect in VistA patch SR\*3\*184 where, in certain instances, active CPT codes D0000- D9999 and xxxxT will not be selectable. A correction for this will be addressed in a future patch.

## CPT Exclusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CPT Exclusions File (#137) was updated with data for fiscal year 2015.

## Transplant Assessment Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Transplant Assessment Menu* \[SR TRANSPLANT ASSESSMENT\] menu has been placed out of order.

#### Modified Option

| Option Name                                           | Description of Change |
|-----------------------------------------------------------|---------------------------|
| *Transplant Assessment Menu* \[SR TRANSPLANT ASSESSMENT\] | Placed out of order       |

## Major/Minor Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Remove missing data screening for MAJOR/MINOR field (#.03) which was removed by Patch 182. This impacts Lists 7 and 8 in the List of Surgery Risk Assessments \[SROA ASSESMENT LIST\] option.

> Option \#4 and \#5 under the List of Surgery Risk Assessments \[SROA ASSESMENT LIST\] options are placed out of order and are not selectable after this enhancement.

#### Modified Option

| Option Name                                            | Description of Change |
|------------------------------------------------------------|---------------------------|
| *List of Surgery Risk Assessments* \[SROA ASSESMENT LIST\] | Functionality Update      |

## Monthly Surgical Case Workload Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The listed exclusion criteria’s are updated as follows:

- The “SCNR WAS ON A/L” criteria has been changed to “10% RULE"
- The "STUDY CRITERIA" criteria has been changed to "INCLSN CRTA NOT MET"
- The “ABORTED” criteria have been added as new exclusion criteria.

#### Modified Option

| Option Name                                                          | Description of Change |
|--------------------------------------------------------------------------|---------------------------|
| *Monthly Surgical Case Workload Report* \[SROA MONTHLY WORKLOAD REPORT\] | Functionality Update      |
| *Exclusion Criteria (Enter/Edit)* \[SR NO ASSESSMENT REASON\]            | Functionality update      |

## Wound Classification Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The WOUND CLASSIFICATION field (#1.09) prevents the selection of “CLEAN” if the principal procedure code (CPT) matches one of the CPT’s that cannot be classified as clean. However, if data has already been populated for this field and the user tries to update it again, then the “CLEAN’ option will be displayed.

> The CPT codes are: 43108,43113,43118,43123,43361,43645,43845,43847,44020,44021,44110,44111,44120,44121,44125,44126,44127,

> 44128,44139,44140,44141,44143,44144,44145,44146,44147,44150,44151,44155,44156,44157,44157,44158,44158,

> 44160,44202,44203,44204,44205,44206,44207,44208,44210,44211,44212,44213,44227,44322,44602,44603,44620,

> 44625,44625,44626,44626,44701,44900,44950,44955,44960,44970,45000,45005,45020,45108,45111,45113,45119,

> 45120,45121,45126,45130,45135,45160,45171,45172,45190,45355,45390,45397,45562,45563,45910,46040,46060,

> 46288,46707,47010,47120,47122,47125,47130,47133,47140,47141,47142,47143,47144,47145,47361,47400,47420,

> 47425,47480,47490,47510,47511,47525,47530,47550,47552,47560,47561,47562,47563,47564,47570,47600,47605,

> 47610,47612,47620,47700,47700,47711,47712,47720,47721,47740,47741,47760,47765,47780,47785,47800,47802,

> 47900,48001,48001,48020,48105,48140,48145,48146,48150,48152,48153,48154,48155,48160,48500,48510,48520,

> 48540,48545,48547,48548,48550,48551,48551,48552,48554,48556,49020,49407,49442,49450,50815,50825,50845,

> 51596,51597,51597,58200,58240,58260,58262,58263,58267,58270,58275,58280,58285,58290,58291,58292,58293,

> 58294,58550,58552,58553,58554,59857,0184T

#### SURGERY File (#130)

| Field Name and Number    | Description of Change                 |
|------------------------------|-------------------------------------------|
| WOUND CLASSIFICATION (#1.09) | Field description and set of code updates |

### From: SR*3*200 Surgery Release Notes

## Before Getting Started: Update Site Configurable Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing this enhancement, the VistA Surgery application can be configured to auto-populate the value NO for surgical specialties that never use robotic assistance. When a Surgery case is created, the Robotic Assistance (Y/N) field will be auto populated with NO if the Local Surgical Specialty has been designated not to use robotics.

This is done using the Update Site Configurable Files option found on the Surgery Package Management Menu.

Example: Updating the Local Specialty File to include a default for Robotic Assistance

Select Surgery Menu \<TEST ACCOUNT\> Option: <u>Surgery Package Management Menu</u>

*\<screen clears\>*

Select Surgery Package Management Menu \<TEST ACCOUNT\> Option: <u>Update Site</u><u>Configurable Files</u>

*\<screen clears\>*

================================================================================

Update Site Configurable Surgery Files

================================================================================

1\. Surgery Transportation Devices

2\. Prosthesis

3\. Surgery Positions

4\. Restraints and Positional Aids

5\. Surgical Delay

6\. Monitors

7\. Irrigations

8\. Surgery Replacement Fluids

9\. Skin Prep Agents

10\. Skin Integrity

11\. Patient Mood

12\. Patient Consciousness

13\. Local Surgical Specialty

14\. Electroground Positions

15\. Special Equipment

16\. Planned Implant

17\. Pharmacy Items

18\. Special Instruments

19\. Special Supplies

================================================================================

Update Information for which File ? <u>13</u>

*\<screen clears\>*

Update Information in the Local Surgical Specialty file.

================================================================================

Select LOCAL SURGICAL SPECIALTY NAME: <u>PODIATRY</u> 61

NAME: PODIATRY// <u>\<enter\></u>

NATIONAL SURGICAL SPECIALTY: PODIATRY// <u>\<enter\></u>

ASSOCIATED CLINIC: <u>\<enter\></u>

INACTIVE?: <u>\<enter\></u>

CODE: <u>\<enter\></u>

ROBOTIC DEFAULT: <u>N</u> NO - ROBOTICS NOT USED

Select LOCAL SURGICAL SPECIALTY NAME: <u>\<enter\>  
</u>

## Entering the new Robotic Assistance (Y/N) field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several data entry options within the Surgery package have been updated to include the new Robotic Assistance (Y/N) field.

This new field is included on the Operation \[SROMEN-OP\], Operation (Short Screen) \[SROMEN-OUT\], and Nurse Intraoperative Report \[SRONRPT\] options within the Operation Menu \[SROPER\] and is required to be entered prior to signing the Nurse Intraoperative Report.

This field is also included on the Non-Cardiac and Cardiac Risk Assessment data entry options. This indicator is transmitted to Veterans Affairs Surgery Quality Improvement Program (VASQIP) for all cases.

Example: Editing Robotic Assistance (Y/N) using the Operation optionTEST,TEST (XXX-XX-XXXX) Case \#000 - JUL 1,2021Select Operation Menu \<TEST ACCOUNT\> Option: O Operation*\<Screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,TEST PAGE 1 OF 3

1 TIME PAT IN HOLD AREA:

2 TIME PAT IN OR:

3 ANES CARE TIME BLOCK: (MULTIPLE)4 TIME OPERATION BEGAN:

5 SPECIMENS: (WORD PROCESSING)6 CULTURES: (WORD PROCESSING)7 THERMAL UNIT: (MULTIPLE)8 ELECTROCAUTERY UNIT:

9 ESU COAG RANGE:

10 ESU CUTTING RANGE:

11 TIME TOURNIQUET APPLIED: (MULTIPLE)12 PROSTHESIS INSTALLED: (MULTIPLE)13 REPLACEMENT FLUID TYPE: (MULTIPLE)14 IRRIGATION: (MULTIPLE)15 MEDICATIONS: (MULTIPLE)

Enter Screen Server Function: \<Enter\>

*\<Screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,TEST PAGE 2 OF 3

1 POSSIBLE ITEM RETENTION: YES2 SPONGE FINAL COUNT CORRECT:

3 SHARPS FINAL COUNT CORRECT:

4 INSTRUMENT FINAL COUNT CORRECT:

5 WOUND SWEEP:

6 WOUND SWEEP COMMENTS: (WORD PROCESSING)7 INTRA-OPERATIVE X-RAY:

8 INTRA-OPERATIVE X-RAY COMMENTS: (WORD PROCESSING)9 SPONGE, SHARPS, & INST COUNTER:

10 COUNT VERIFIER:

11 SEQUENTIAL COMPRESSION DEVICE:

12 LASER PERFORMED: (MULTIPLE)13 CELL SAVER: (MULTIPLE)14 NURSING CARE COMMENTS: (WORD PROCESSING)15 PRINCIPAL PRE-OP DIAGNOSIS: EAR CONTUSION

Enter Screen Server Function: \<Enter\>

*\<Screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,TEST PAGE 3 OF 3

1 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

2 PRINCIPAL PROCEDURE: REPAIR TORN EAR3 PLANNED PRIN PROCEDURE CODE : 693994 ROBOTIC ASSISTANCE (Y/N):

5 OTHER PROCEDURES: (MULTIPLE)6 INDICATIONS FOR OPERATIONS: (WORD PROCESSING)(DATA)7 BRIEF CLIN HISTORY: (WORD PROCESSING)

Enter Screen Server Function: 4

Robotic Assistance (Y/N): ?Enter YES if robotic assistance was used for any part of the procedure.Choose from:Y YESN NORobotic Assistance (Y/N): ??This field indicates whether robotic assistance was used for any portionof the procedure. It must be entered prior to signing the NurseIntraoperative Report. Enter YES if robotic assistance was used duringthe procedure. Otherwise, enter NO.Choose from:Y YESN NORobotic Assistance (Y/N): N NO*\<Screen clears\>*\*\* OPERATION \*\* CASE \#000 TEST,TEST PAGE 3 OF 3

1 PRIN PRE-OP ICD DIAGNOSIS CODE (ICD10):

2 PRINCIPAL PROCEDURE: REPAIR TORN EAR3 PLANNED PRIN PROCEDURE CODE : 693994 ROBOTIC ASSISTANCE (Y/N): NO5 OTHER PROCEDURES: (MULTIPLE)6 INDICATIONS FOR OPERATIONS: (WORD PROCESSING)(DATA)7 BRIEF CLIN HISTORY: (WORD PROCESSING)

Enter Screen Server Function: ^

## Displaying the new Robotic Assistance (Y/N) field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Robotic Assistance (Y/N) field will display on the Nurse Intraoperative Report and must be entered prior to signing the report.

Example: Robotic Assistance (Y/N) on Nurse Intraoperative ReportTEST,TEST (XXX-XX-XXXX)MEDICAL RECORD NURSE INTRAOPERATIVE REPORT - CASE \#000 PAGE 1Operating Room: NOT ENTERED Surgical Priority: NOT ENTEREDPatient in Hold: NOT ENTERED Patient in OR: \* NOT ENTERED \*Operation Begin: NOT ENTERED Operation End: NOT ENTEREDPatient Out OR: \* NOT ENTERED \*Major Operations Performed:Primary: REPAIR TORN EARRobotic Assistance (Y/N): NOWound Classification: NOT ENTEREDPrimary Surgeon: SURGEON,ONE First Assist: N/AAttending Surgeon: SURGEON,TWO Second Assist: N/AOR Support Personnel:Scrubbed CirculatingN/A N/APress \<return\> to continue, 'A' to access Nurse Intraoperative Reportfunctions, or '^' to exit:

## Surgery Risk Assessment – Transmitting the Robotic Assistance (Y/N) field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Robotic Assistance (Y/N) field is transmitted to the Surgery Risk Assessment Database for Non-Cardiac and One-Liner Assessments. It is also transmitted as part of the Cardiac Assessments. Other than entering a value for the new field, you will see no other visible change related to transmissions.

## Surgery Risk Assessment – Workload Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The workload reports transmitted to the Surgery Risk Assessment Database have been updated to include the count of cases done using Robotic Assistance.

## Defect Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes the following defect fixes unrelated to this enhancement:

1.  An update to Risk Assessment transmissions to strip seconds from the D/T OF DESIRED PROCEDURE DATE field (#613). This allows the date/time to be stored properly at the Surgery Risk Assessment Database.
2.  A correction of the display of the Laser Duration on the Nurse Intraoperative Report. It changes mins. to seconds.
3.  A correction of the auto-population of the patient's height when using the Operation Startup \[SROMEN-START\] option, allowing the software to pull the measurement regardless of date taken. It also stores the date of the measurement.
4.  An update to the checks that determine whether a Risk Assessment transmission is generated from a Production account or Test account to use a supported Kernel Utility.
5.  Spelling corrections to the words inotropic and immediate in a help prompt.
