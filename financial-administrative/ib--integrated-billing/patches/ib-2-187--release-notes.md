---
title: IB*2*187 Visit Copay Phase 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Visit Copay Phase 2
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*187
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - stop
  - routine
  - care
  - patch
  - billable
  - table
  - contents
  - description
  - code
  - codes
page_count: 0
word_count: 1143
section_count: 4
table_count: 17
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_187rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_187rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

![](ib-2-187-visit-copay-phase-2-release-notes/001.png)

VISIT COPAY PHASE 2RELEASE NOTESPatch IB\*2\*187September 2002

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Visit Co-pay Determination](#visit-co-pay-determination)
- [Functional Description](#functional-description)
  - [Stop codes for file \#352.5](#stop-codes-for-file-3525)
- [Technical Description](#technical-description)
  - [Data dictionary changes in file \#352.5](#data-dictionary-changes-in-file-3525)
- [Sample Installation](#sample-installation)
This software will modify the method for determining the outpatient visit copayment tiers as originally distributed in patches IB\*2\*167 and IB\*2\*177 effective October 1, 2002. The method for determining the outpatient medical care copayments will be based upon both Decision Support Services (DSS) primary and secondary stop codes instead of just the primary clinic stop code as implemented in Phase 1. The new approach still maintains the three tiered outpatient medical care copayment rates for non-exempt veterans. Refer to the patch descriptions of IB\*2.0\*167 and IB\*2.0\*177 to get more details regarding billable types and dollar amounts. This patch also renames "PRIMARY CARE" billable type to "BASIC CARE". Thus the rates for visit copayment are as follows:
> NON-BILLABLE \$0
> BASIC CARE \$15
> SPECIALTY CARE \$50

## Visit Co-pay Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior patches used only the clinic's primary stop code to determine billable type and rate for copayment. This patch will implement software to take into account the clinic's credit stop code as well. The clinic stop code and credit stop code (a.k.a. credit pair) defined for the clinic will constitute a 6-digit stop code that is used to determine the billable type for the visit. If the secondary stop code is not defined for the clinic, then the 3-digit primary code will be used to determine the billable type. This patch introduces override tables for BASIC, SPECIALTY and NON-BILLABLE stop codes to support new business rules to determine proper billable types and proper visit copayment amounts.

The effective date for implementation is October 1, 2002. Therefore, this patch MUST be installed at all sites by September 30, 2002.

# Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menu options were not changed with this patch; however, the functionality behind all outpatient encounters and the manual option "Cancel/Edit/Add Patient Charges \[IB CANCEL/EDIT/ADD CHARGES\]" is affected for determining copayment amounts.

## Stop codes for file \#352.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A. The following 6-digit stop codes and billable types will be added to the IB CLINIC STOP CODE BILLABLE TYPES (#352.5) file:

|          |                                |                   |
|----------|--------------------------------|-------------------|
| Code | Description                | Billable Type |
| 102101   | EMERGENCY UNIT WORK            | SPECIALTY CARE    |
| 103801   | IN-VISN PHONE TRIAGE-NOT VAMC  | NON-BILLABLE      |
| 103802   | OUT OF VISN, VA PHONE TRIAGE   | NON-BILLABLE      |
| 103803   | COMMERCIAL PHONE TRIAGE        | NON-BILLABLE      |
| 107473   | ECHOCARDIOGRAM                 | SPECIALTY CARE    |
| 116714   | RESPIRATORY THERAPY EDUCATION  | BASIC CARE        |
| 116329   | RESPIRATORY THERAPY PROCEDURES | SPECIALTY CARE    |
| 117473   | PPD CLINIC                     | NON-BILLABLE      |
| 117710   | FLU SHOT                       | NON-BILLABLE      |
| 147209   | TELEPHONE VIST                 | NON-BILLABLE      |
| 174202   | HBPC - RECREATION THERAPY (RT) | BASIC CARE        |
| 174205   | HBPC - PHYSICAL THERAPY (PT)   | BASIC CARE        |
| 174206   | HBPC - OT                      | BASIC CARE        |
| 177201   | HBPC - PM&RS                   | BASIC CARE        |
| 177210   | HBPC - SCI                     | BASIC CARE        |
| 208466   | DOMICILIARY (DOM) CWT          | NON-BILLABLE      |
| 209125   | VIST COORD BY SOCIAL WORKER    | NON-BILLABLE      |
| 210414   | SCI-CYSTOURO                   | BASIC CARE        |
| 210468   | SCI-RN PROCEDURE               | BASIC CARE        |
| 213466   | VETS ED/TRNG DOM               | NON-BILLABLE      |
| 216203   | TELEPHONE AUDIO REHAB SUP SVC  | NON-BILLABLE      |
| 216204   | TELEPHONE SPEECH REHAB SUP SVC | NON-BILLABLE      |
| 216210   | SCI TELEPHONE SUP              | NON-BILLABLE      |
| 303115   | ECHOCARDIOGRAM                 | SPECIALTY CARE    |
| 303201   | CARD REHAB                     | BASIC CARE        |
| 304416   | DERM PHOTO THERAPY             | SPECIALTY CARE    |
| 304715   | DERMATOLOGY ROUTINE AFTERCARE  | BASIC CARE        |
| 306117   | DIAB DM ED                     | BASIC CARE        |
| 306714   | DIABETIC EDUCATION             | BASIC CARE        |
| 307117   | ENTEROSTOMAL CLINIC            | BASIC CARE        |
| 307454   | LIVER                          | SPECIALTY CARE    |
| 310323   | CHRON INFX DSE PRIMARY CARE    | BASIC CARE        |
| 312104   | SLEEP STUDIES                  | SPECIALTY CARE    |
| 313457   | TRANSPLANT                     | SPECIALTY CARE    |
| 315456   | EPILEPSY                       | SPECIALTY CARE    |
| 315469   | MOVEMENT DISORDER              | SPECIALTY CARE    |

|          |                                |                   |
|----------|--------------------------------|-------------------|
| Code | Description                | Billable Type |
| 315470   | SLEEP DISORDER                 | SPECIALTY CARE    |
| 316149   | RAD RX W/ONC MED               | SPECIALTY CARE    |
| 316329   | ONCOLOGY/TUMOR PROCEDURES      | SPECIALTY CARE    |
| 322704   | PAP SMEAR ONLY WOMEN'S CLI     | NON-BILLABLE      |
| 323160   | PHARMACIST CONSULTS            | BASIC CARE        |
| 323473   | PPD CLINIC                     | NON-BILLABLE      |
| 323710   | FLU SHOT                       | NON-BILLABLE      |
| 402457   | HEART TRANSPLANT CLINIC        | SPECIALTY CARE    |
| 410210   | SCI PLASTIC                    | SPECIALTY CARE    |
| 414451   | IMPOTENCY                      | SPECIALTY CARE    |
| 414473   | URODYNAMICS                    | SPECIALTY CARE    |
| 415461   | ADAM CLINIC                    | SPECIALTY CARE    |
| 417201   | MAJOR MED                      | BASIC CARE        |
| 417451   | WHEEL CHAIR                    | BASIC CARE        |
| 417452   | CUSHION                        | BASIC CARE        |
| 417455   | SHOE/BRACE                     | BASIC CARE        |
| 417473   | ORTHOTIC LAB                   | BASIC CARE        |
| 417474   | PROSTHETICS LAB                | BASIC CARE        |
| 423461   | CAD CAM UNIT                   | NON-BILLABLE      |
| 510473   | NEURO PSYCHOLOGY LAB           | SPECIALTY CARE    |
| 510474   | PSYCHOLOGY RESEARCH            | NON-BILLABLE      |
| 510475   | RESEARCH (USE 510474)          | NON-BILLABLE      |
| 510509   | PSO - PSI                      | BASIC CARE        |
| 513461   | IND SUB ABUSE: ALCH DEP        | BASIC CARE        |
| 513469   | IND SUB ABUSE: DRUG DEP        | BASIC CARE        |
| 516726   | PTSD DOM - AFTERCARE GROUP     | BASIC CARE        |
| 527564   | TELEPHONE MH TEAM CASE MGT     | NON-BILLABLE      |
| 532713   | GAMBLING ADDICTION IND         | BASIC CARE        |
| 533707   | SMOKING CESSATION IND          | BASIC CARE        |
| 545461   | TELEPHONE/SUB ABUSE - ALC DEP  | NON-BILLABLE      |
| 545469   | TELEPHONE SUB ABUSE - DRUG DEP | NON-BILLABLE      |
| 547461   | INT SU ABUSE TRMT - ALCH DEP   | BASIC CARE        |
| 547469   | INT SUB ABUSE TRMT - DRUG DEP  | BASIC CARE        |
| 559713   | GAMBLING ADDICTION GRP         | BASIC CARE        |
| 560461   | GRP SUB ABUSE: ALCH DEP        | BASIC CARE        |
| 560469   | GRP SUB ABUSE: DRUG DEP        | BASIC CARE        |
| 566707   | SMOKING CESSATION GRP          | BASIC CARE        |
| 574513   | CWT/ SUBSTANCE ABUSE           | NON-BILLABLE      |
| 999510   | PSO - EAP - OPTIONAL           | NON-BILLABLE      |

B. The following new 3-digit stop codes and billable types will be added to the IB CLINIC STOP CODE BILLABLE TYPES (#352.5) file:

|          |                               |                   |
|----------|-------------------------------|-------------------|
| Code | Description               | Billable Type |
| 219      | TBI (TRAUMATIC BRAIN INJURY)  | SPECIALTY CARE    |
| 335      | PARKINSON'S DISEASE RECC      | SPECIALTY CARE    |
| 515      | CWT/TR - HCMI                 | NON-BILLABLE      |
| 567      | MH INTENSIVE CASE MGMT GRP    | BASIC CARE        |
| 653      | STATE HOSPITAL CARE           | NON-BILLABLE      |
| 654      | NON VA RESIDENTIAL CARE DAYS  | NON-BILLABLE      |
| 655      | COMMUNITY NON-VA CARE         | NON-BILLABLE      |
| 656      | DOD NON-VA CARE               | NON-BILLABLE      |
| 657      | ASSIST LIVING VENDOR WORK     | NON-BILLABLE      |
| 660      | CHIROPRACTIC CARE OUTSIDE VA  | NON-BILLABLE      |
| 670      | ASSIST LIVING VHA-PAID, STAFF | NON-BILLABLE      |

C. The following 3-digit stop codes and billable types will be updated in IB CLINIC STOP CODE BILLABLE TYPES (#352.5) file:

|          |                                |                       |                       |
|----------|--------------------------------|-----------------------|-----------------------|
| Code | Description                | Old Billable Type | New Billable Type |
| 117      | NURSING                        | NON-BILLABLE          | BASIC CARE            |
| 160      | CLINICAL PHARMACY              | NON-BILLABLE          | BASIC CARE            |
| 180      | DENTAL                         | BASIC CARE            | NON-BILLABLE          |
| 190      | ADULT DAY HEALTH CARE          | NON-BILLABLE          | BASIC CARE            |
| 210      | SPINAL CORD INJURY             | SPECIALTY CARE        | BASIC CARE            |
| 215      | SCI HOME CARE PROGRAM          | NON-BILLABLE          | BASIC CARE            |
| 217      | BROS (BLIND REHAB O/P SPEC)    | SPECIALTY CARE        | BASIC CARE            |
| 218      | CAT BLIND REHAB                | SPECIALTY CARE        | BASIC CARE            |
| 422      | CAST CLINIC                    | NON-BILLABLE          | BASIC CARE            |
| 430      | CYSTO ROOM UNIT FOR OUTPATIENT | NON-BILLABLE          | SPECIALTY CARE        |
| 509      | PSYCHIATRY - MD                | SPECIALTY CARE        | BASIC CARE            |
| 510      | PSYCHOLOGY - INDIVIDUAL        | SPECIALTY CARE        | BASIC CARE            |
| 512      | PSYCHIATRY CONSULTATION        | SPECIALTY CARE        | BASIC CARE            |
| 602      | CHRON ASSISTED HEMODIAL TREAT  | SPECIALTY CARE        | BASIC CARE            |
| 603      | LIM SELF CARE HEMODIAL TREAT   | SPECIALTY CARE        | BASIC CARE            |
| 604      | HOME/SELF HEMOD TRAIN TREAT    | SPECIALTY CARE        | BASIC CARE            |
| 606      | CHRON ASSISTED PERIT DIALYSIS  | SPECIALTY CARE        | BASIC CARE            |
| 607      | LIM SELF CARE PERIT DIALYSIS   | SPECIALTY CARE        | BASIC CARE            |
| 608      | HOME/SELF PERIT DIALYSIS TRAIN | NON-BILLABLE          | BASIC CARE            |

D. The following stop codes will be placed into a new NON-BILLABLE override table:

|          |                                     |
|----------|-------------------------------------|
| Code | Description                     |
| 103      | TELEPHONE TRIAGE                    |
| 147      | TELEPHONE/ANCILLARY                 |
| 148      | TELEPHONE/DIAGNOSTIC                |
| 163      | CHAPLAIN BILLABLE                   |
| 164      | CHAPLAIN BILLABLE                   |
| 165      | BEREAVEMENT COUNSELING              |
| 166      | CHAPLAIN SERVICE - INDIVIDUAL       |
| 167      | CHAPLAIN SERVICE - GROUP            |
| 168      | CHAPLAIN SERVICE - COLLATERAL       |
| 169      | TELEPHONE/CHAPLAIN                  |
| 178      | HBPC/TELEPHONE                      |
| 181      | TELEPHONE/DENTAL                    |
| 202      | RECREATION THERAPY SERVICE          |
| 216      | TELEPHONE/REHAB AND SUPPORT         |
| 324      | TELEPHONE/MEDICINE                  |
| 325      | TELEPHONE/NEUROLOGY                 |
| 326      | TELEPHONE/GERIATRICS                |
| 370      | LTC SCREENING/ASSESSMENT            |
| 424      | TELEPHONE/SURGERY                   |
| 425      | TELEPHONE/PROSTHETICS/ORTHO         |
| 428      | TELEPHONE/OPTOMETRY                 |
| 449      | FITTING & ADJUSTMENTS               |
| 450      | C&P EXAM                            |
| 474      | RESEARCH                            |
| 522      | HUD/VASH                            |
| 523      | OPIOID SUBSTITUTION                 |
| 524      | ACTIVE DUTY SEX TRAUMA              |
| 527      | TELEPHONE/GENERAL PSYCHIATRY        |
| 528      | TELE/HOMELESS MENTALLY ILL          |
| 529      | HCHV/HMI                            |
| 530      | TELEPHONE/HUD-VASH                  |
| 536      | TELEPHONE/ MH VOCATIONAL ASSISTANCE |
| 537      | TELEPHONE/PSYCHOSOCIAL REHAB        |
| 542      | TELEPHONE/PTSD                      |
| 545      | TELEPHONE/SUBSTANCE ABUSE           |
| 546      | TELEPHONE/MHICM                     |
| 579      | TELEPHONE/ PSYCHOGERIATRICS         |
| 589      | NON-ACTIVE DUTY SEX TRAUMA          |
| 611      | TELEPHONE/DIALYSIS                  |
| 640      | SEND-OUT PROCEDURES NOT FEE         |
| 641      | SEND-OUT PROC-DOD NOT PAID FEE      |
| 642      | SEND-OUT PROCEDURES FEE             |
| 650      | CONTRACT NURSING HOME DAYS          |
| 651      | STATE NURSING HOME DAYS             |
| 652      | STATE DOMICILIARY HOME DAYS         |
| 653      | STATE HOSPITAL CARE                 |
| 654      | NON VA RESIDENTIAL CARE DAYS        |

|          |                                        |
|----------|----------------------------------------|
| Code | Description                        |
| 655      | COMMUNITY NON-VA CARE                  |
| 656      | DOD NON-VA CARE                        |
| 657      | ASSIST LIVING VENDOR WORK              |
| 660      | CHIROPRACTIC CARE OUTSIDE VA           |
| 670      | ASSIST LIVING VHA-PAID, STAFF          |
| 680      | HOME/COMMUN HEALTHCARE ASSESSMENT      |
| 681      | VA-PAID HOME/COMMUN CARE PROVIDERS     |
| 682      | VA-REFER TO HOME/COMMUN CARE PROVIDERS |
| 691      | PRE-EMP PHYS MILITRY PERSONNEL         |
| 692      | TELEMED CONSULT SAME STATION           |
| 693      | TELEMED CONSULT OTHER STATION          |
| 701      | BLOOD PRESSURE CHECK                   |
| 702      | CHOLESTEROL SCREENING                  |
| 703      | MAMMOGRAM                              |
| 704      | PAP TEST                               |
| 705      | FOBT - GUIAC SCREENING                 |
| 706      | ALCOHOL SCREENING                      |
| 710      | INFLUENZA IMMUNIZATION                 |
| 711      | INJURY COUNSEL/SEAT BELT USAGE         |
| 712      | HEP C REGISTRY PATIENT                 |
| 729      | TELEPHONE/DOMICILIARY                  |
| 999      | EMPLOYEE HEALTH                        |

E. The following stop codes will be placed into a new SPECIALTY CARE override table:

|          |                                |
|----------|--------------------------------|
| Code | Description                |
| 104      | PULMONARY FUNCTION             |
| 106      | ELECTROENCEPHALOGRAM (EEG)     |
| 109      | NUCLEAR MEDICINE               |
| 115      | ULTRASOUND                     |
| 116      | RESPIRATORY THERAPY            |
| 126      | EVOKED POTENTIAL               |
| 127      | TOPOGRAPHICAL BRAIN MAPPING    |
| 128      | PROLONGED VIDEO-EEG MONITORING |
| 144      | RADIONUCLIDE THERAPY           |
| 145      | PHARM/PHYSIO NMP STUDIES       |
| 146      | PET                            |
| 149      | RADIATION THERAPY TREATMENT    |
| 150      | COMPUTERIZED TOMOGRAPHY (CT)   |
| 151      | MRI                            |
| 152      | ANGIOGRAM CATHETERIZATION      |
| 153      | INTERVENTIONAL RADIOGRAPHY     |
| 154      | MEG                            |
| 155      | INFO ASSISTS TECHNOLOGY        |
| 457      | TRANSPLANT                     |
| 480      | COMPREHENSIVE FUNDOSCOPY EXAM  |
| 481      | BRONCHOSCOPY                   |
| 538      | PSYCHOLOGICAL TESTING          |

F. The following stop codes will be placed into a new BASIC CARE override table:

|          |                                |
|----------|--------------------------------|
| Code | Description                |
|          |                                |
| 117      | NURSING SERVICES               |
| 123      | NUTRITION/DIETETICS/INDIVIDUAL |
| 124      | NUTRITION/DIETETICS/GROUP      |
| 125      | SOCIAL WORK SERVICE            |
| 160      | CLINICAL PHARMACY              |
| 205      | PHYSICAL THERAPY               |
| 206      | OCCUPATIONAL THERAPY           |
| 214      | KINESIOTHERAPY                 |
| 322      | WOMEN'S CLINIC                 |
| 323      | PRIMARY CARE/MEDICINE          |
| 350      | GERIATRIC PRIMARY CARE         |
| 509      | PSYCHIATRY - MD                |
| 510      | PSYCHOLOGY - INDIVIDUAL        |
| 512      | PSYCHIATRY CONSULTATION        |
| 707      | SMOKING CESSATION              |
| 708      | NUTRITION                      |
| 709      | PHY FIT/EXERCISE COUNSELING    |
| 713      | GAMBLING ADDICTION             |
| 714      | OTHER EDUCATION                |
| 715      | ONGOING TREATMENT (Non-MH)     |
| 716      | POST SURG ROUTINE AFTERCARE    |

# Technical Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB2P187A

This post init routine will populate file \#352.5 with new six and three digit codes (see listing above) and will edit "PRIMARY CARE" entry in file \#363.21 to change the name to "BASIC CARE".

IB2P187B:

This routine contains data to add and update items in file \#352.5.

IBAUTL2:

Billable type "PRIMARY CARE" has been changed to "BASIC CARE" in TYPE^IBAUTL2 subroutine.

IBCREQ:

Billable type "PRIMARY CARE" has been changed to "BASIC CARE" in MT^IBCREQ subroutine.

IBEMTSCR:

Billable type "Primary Care" has been changed to "Basic Care" in TYPE^IBEMTSCR subroutine.

IBEMTSCU

Existing logic has been updated to implement the new business rules to determine billable types for visit copayment.

## Data dictionary changes in file \#352.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The old name of "PRIMARY CARE" (code \#1) has been changed to "BASIC CARE".
- Technical description for the field (#.03) has been added. With patch IB\*2.0\*187 the name of the billable type code (1) has been changed from "PRIMARY CARE" to "BASIC CARE".
- "WRITE" node was edited to change "PRIMARY CARE" to "BASIC CARE".
- A new field (#.05) "OVERRIDE FLAG" has been added to file (#352.5) .

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Time - less than 5 minutes.

1\. LOAD TRANSPORT GLOBAL

---------------------

Choose the PackMan message containing this patch and invoke the

INSTALL/CHECK MESSAGE PackMan option.

2\. DISABLE ROUTINE MAPPING (DSM for Open VMS sites only)

-----------------------

Disable routine mapping on all systems for the routines listed

in step 3 below.

> **NOTE:** If the routines included in this patch are not currently

in your mapped routine set, please skip this step.

3\. ROUTINES SENT WITH PATCH

------------------------

The following is a list of the routines included in this patch.

The second line of each of these routines now looks like:

;;2.0;INTEGRATED BILLING;\*\*\[patch list\]\*\*;21-MAR-94

CHECK^XTSUMBLD results

Routine Before Patch After Patch Patch List

-------- ------------ ----------- ----------

IB2P187A n/a 8752864 187

IB2P187B n/a 8797954 187

IBAUTL2 4129248 4115995 52,153,167,187

IBCREQ 21870882 21862627 52,153,167,187

IBEMTSCR 5867019 5861220 167, 187

IBEMTSCU 8362803 10525057 167,177,187

Total number of routines - 6

4\. START UP KIDS

-------------

Start up the Kernel Installation and Distribution System Menu

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option:INS

tallation

---

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

5\. Select Installation Option:

--------------------------

> **NOTE:** The following are OPTIONAL - (When prompted for the

INSTALL NAME, enter IB\*2.0\*187):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of this

patch (routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

6\. Select Installation Option: Install Package(s)

----------------------------------------------

\*\*This is the step to start the installation of this KIDS patch:

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? YES//" answer NO

c\. When prompted "Want to DISABLE Scheduled Options, Menu

Options, and Protocols? YES//" answer NO

7\. REBUILD MAPPED ROUTINE(S) (DSM for Open VMS sites only)

-------------------------

Optional - Include the routines distributed with this patch in

the mapped routine set.

> **NOTE:** This step is only necessary if you performed step 2 or if

you wish to include the routines in your mapped set.

8\. Remove post-init routines IB2P187A and IB2P187B.

Routine Information:

====================

Routine Name: IBAUTL2

Description of Changes:

Routine Checksum:

Routine Name: IBCREQ

Description of Changes:

Routine Checksum:

Routine Name: IBEMTSCR

Description of Changes:

Routine Checksum:

Routine Name: IBEMTSCU

Description of Changes:

Routine Checksum:

Routine Name: IB2P187A

Description of Changes:

Routine Checksum:

Routine Name: IB2P187B

Description of Changes:

Routine Checksum: