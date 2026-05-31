---
title: DG*5.3*1067 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*1067
group_key: ADT:DG:5.3
file_numbers:
- '1'
- '2'
- '2.02'
- '2.06'
- '2.1'
- '10'
- '10.2'
- '11'
- '12.11'
- '13'
- '25.11'
- '172'
- '301.92'
- '374'
- '375'
- '391.71'
- '408.43'
- '597'
- '598'
- '599'
- '600'
- '601'
- '8989.5'
- '8989.51'
security_keys: []
menu_options: 0
description: '''[Table 1: DG_53_P1067.KID Enhancements and Modifications'''
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 8598
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: February 2022
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_p1067_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_p1067_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=55
audit_applied: '2026-05-31'
master_source: DG*5.3*1067 Release Notes
master_pub_date: February 2022
consolidated_from: 67 versions
prior_versions:
- DG*5.3*1006 Release Notes
- DG*5.3*1008 Release Notes
- DG*5.3*1012 Release Notes
- DG*5.3*1014 Release Notes
- DG*5.3*1015 Release Notes
- DG*5.3*1016 Release Notes
- DG*5.3*1018 Release Notes
- DG*5.3*1025 Release Notes
- DG*5.3*1027 Release Notes
- DG*5.3*1029 Release Notes
- DG*5.3*1031 Release Notes
- DG*5.3*1034 Release Notes
- DG*5.3*1035 Release Notes
- DG*5.3*1040 Release Notes
- DG*5.3*1041 Release Notes
- DG*5.3*1044 Release Notes
- DG*5.3*1045 Release Notes
- DG*5.3*1047 Release Notes
- DG*5.3*1048 Release Notes
- DG*5.3*1049 Release Notes
- DG*5.3*1056 Release Notes
- DG*5.3*1061 Release Notes
- DG*5.3*1064 Release Notes
- DG*5.3*1065 Release Notes
- DG*5.3*1075 Release Notes
- DG*5.3*1081 Release Notes
- DG*5.3*1082 Release Notes
- DG*5.3*1085 Release Notes
- DG*5.3*1090 Release Notes
- DG*5.3*1093 Release Notes
- DG*5.3*1098 Release Notes
- DG*5.3*1103 Release Notes
- DG*5.3*1104 Release Notes
- DG*5.3*1106 Release Notes
- DG*5.3*1108 Release Notes
- DG*5.3*1109 Release Notes
- DG*5.3*1111 Release Notes
- DG*5.3*1118 Release Notes
- DG*5.3*1120 Release Notes
- DG*5.3*1121 Release Notes
- DG*5.3*1127 Release Notes
- DG*5.3*1140 Release Notes
- DG*5.3*1149 Release Notes
- DG*5.3*850 Release Notes
- DG*5.3*867 Release Notes
- DG*5.3*903 Release Notes
- DG*5.3*925 Release Notes
- DG*5.3*935 Release Notes
- DG*5.3*936 Release Notes
- DG*5.3*939 Release Notes
- DG*5.3*940 Release Notes
- DG*5.3*941 Release Notes
- DG*5.3*947 Release Notes
- DG*5.3*952 Release Notes
- DG*5.3*964 Release Notes
- DG*5.3*966 Release Notes
- DG*5.3*972 Release Notes
- DG*5.3*976 Release Notes
- DG*5.3*977 Release Notes
- DG*5.3*978 Release Notes
- DG*5.3*985 Release Notes
- DG*5.3*987 Release Notes
- DG*5.3*993 Release Notes
- DG*5.3*996 Release Notes
- DG*5.3*997 Release Notes
- DG*5.3*998 Release Notes
consolidated_title: release notes
---

![](dg-5-3-1067-release-notes/001.png)

February 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Table of Contents

List of Tables

[Table 1: DG_53_P1067.KID Enhancements and Modifications [2](#_Ref533696768)](#_Ref533696768)

[Table 2: Defects and Fixes in DG_53_P1067.KID [36](#_Ref524346485)](#_Ref524346485)

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications](#enhancements-and-modifications)
  - [Defects and Fixes](#defects-and-fixes)
  - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
The release of VistA REE Host File DG_53_P1067.KID, which includes Registration (DG) patch DG\*5.3\*1067 and Income Verification Match (IVM) patch IVM\*2.0\*204, supports the enhancements for the Eligibility and Enrollment program. This patch focuses on updates for the ESM Phase 3 project.
Patch DG\*5.3\*1067 is also being released in support of the Veterans Health Administration (VHA) Enrollment System (VES) 6.0 release. Refer to Informational Patch EAS\*1\*208 (Enrollment Application System) for additional details regarding the VES release.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Notes cover the changes to VistA REE DG and IVM systems for this release.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA REE and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This multi-package build is distributed as a Host File. Refer to the Software and Documentation Retrieval Instructions section of the patch descriptions for information on obtaining the Host File DG_53_P1067.KID and related documentation.

The following sections provide a summary of the enhancements and modifications to the existing software for VistA REE with the release of patches DG\*5.3\*1067 and IVM\*2.0\*204.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new features or functions added to VistA REE for DG\*5.3\*1067 and IVM\*2.0\*204.

## Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1067 includes the following enhancements, with details provided below:

- Standardizes Next of Kin (NOK), Emergency Contact (EC) and Designee Relationship to Patient.
- Adds new Self-Reported Registration Reasons for Clinical Evaluations, Housing and Urban Development – VA Supportive Housing (HUD-VASH), 4<sup>th</sup> Mission and Immunizations.
- Adds FileMan field cross-references to support VES/VA Profile Demographic Integration.
- Adds two and modifies four VHA Profiles (VHAPs) to support Cerner billing.
  - New VHA Profiles:

NAME : ACTIVE DUTY PLAN CODE: 303

NAME : JOINT INCENTIVE FUND PLAN CODE: 304

- Modified VHA Profiles:

NAME: VA DOD SHARING MEDICAL RESOURCES PLAN CODE: 295

NAME: TRICARE PLAN CODE: 229

NAME: VETERAN PLAN CCP RESTRICTED CARE PLAN CODE: 300

NAME: APPLICANT IN PROCESS PLAN CODE: 226

- Adds and modifies VHAP information related to Veteran Family Member Programs (VFMPs) summarized below. These will be assigned to patients by the VES only after a future VES release.
  - New VHA Profile:

NAME: CHAMPVA CAREGIVER PLAN CODE: 305

- Modified VHA Profiles:

(The plan below replaces VETERAN BENEFICIARY PLAN - CAMP LEJEUNE

FAMILY, Plan Code 139.)

NAME: CAMP LEJEUNE FAMILY PLAN CODE: 306

(The plan below is renamed from BENEFICIARY CHAMPVA.)

NAME: CHAMPVA STANDARD PLAN CODE: 108

NAME: BENEFICIARY SPINA BIFIDA PLAN CODE: 109

NAME: BENEFICIARY CHILDREN OF WOMEN PLAN CODE: 110

OF VIETNAM VETERANS

NAME: VETERAN FOREIGN MEDICAL PROGRAM PLAN CODE: 122

Table 1 shows the enhancements and modifications included in the DG_53_P1067.KID release as tracked in Atlassian Jira.

| Jira Epic \# | Summary                                                                                  |
|------------------|----------------------------------------------------------------------------------------------|
| VES-2442         | NOK/EC Relationship Dropdown - VistA                                                         |
| VES-8332         | Rename ADTSA VHAP (VistA)                                                                    |
| VES-13552        | Demographics Integration with VA Profile (VistA)                                             |
| VES-14969        | HUD-VASH Program Enhancement (VistA)                                                         |
| VES-17483        | Add Self-Reported Registration Only Reasons - Clinical Evaluation and Immunizations (VistA)  |
| VES-18176        | Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) Standard |
| VES-18177        | CHAMPVA Foreign                                                                              |
| VES-18178        | CHAMPVA Caregiver                                                                            |

<span id="_Ref533696768" class="anchor"></span>Table 1: DG_53_P1067.KID Enhancements and Modifications

List of UpdatesDG\*5.3\*1067 makes the following enhancements to VistA REE:

SECTION 1: DATA DICTIONARY UPDATES

1.  A new PATIENT CONTACT RELATION file (#12.11) is added to VistA.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

This file contains all acceptable relationships for persons named as

Primary Next of Kin, Secondary Next of Kin, Primary Emergency Contact,

Secondary Emergency Contact, and Designee. These relationships are

consistent with the values used by Defense Manpower Data Center (DMDC) and

Cerner for these relationships. Additions or modifications to entries in

this file should only be done through a national patch release. Records in

this file should not be added, edited, or deleted locally. Doing so would

likely cause database corruption.

DD ACCESS: @

RD ACCESS: @

WR ACCESS: @

DEL ACCESS: @

LAYGO ACCESS: @

AUDIT ACCESS: @

IDENTIFIED BY: NAME (#.02)

POINTED TO BY: K2-RELATIONSHIP TYPE field (#.2104) of the PATIENT File

(#2)

K-RELATIONSHIP TYPE field (#.224) of the PATIENT File (#2)

E-RELATIONSHIP TYPE field (#.3309) of the PATIENT File

(#2)

E2-RELATIONSHIP TYPE field (#.331015) of the PATIENT File

(#2)

D-RELATIONSHIP TYPE field (#.34015) of the PATIENT File

(#2)

CROSS

REFERENCED BY: NUMBER(B), NAME(C)

CREATED ON: NOV 29, 2021 BY DGAdmin,One LAST MODIFIED: DEC

6,2021@15:11:25

12.11,.01 NUMBER 0;1 NUMBER (Required)

INPUT TRANSFORM: K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."4N.N) X

LAST EDITED: NOV 29, 2021

HELP-PROMPT: Type a whole number between 1 and 999.

DESCRIPTION: This field contains the number of the

Patient Contact Relation.

CROSS-REFERENCE: 12.11^B

1)= S ^DG(12.11,"B",\$E(X,1,30),DA)=""

2)= K ^DG(12.11,"B",\$E(X,1,30),DA)

This cross-reference allows the user to

lookup an entry by the NUMBER field.

12.11,.02 NAME 0;2 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<3) X

MAXIMUM LENGTH: 30

LAST EDITED: DEC 06, 2021

HELP-PROMPT: Enter a name for the Patient Contact

Relation between 3 and 30 characters.

DESCRIPTION: This field contains Standardized Name of

the Patient Contact Relation.

CROSS-REFERENCE: 12.11^C

1)= S ^DG(12.11,"C",\$E(X,1,30),DA)=""

2)= K ^DG(12.11,"C",\$E(X,1,30),DA)

This cross-reference allows the user to

lookup an entry by the NAME field.

12.11,.03 ACTIVE? 0;3 SET (BOOLEAN Data Type)

LAST EDITED: NOV 30, 2021

HELP-PROMPT: Enter 1 if the Patient Contact Relation is

active. Enter 0 if the Patient Contact is

no longer active.

DESCRIPTION: This field indicates whether the Patient

Contact Relation may be selected by the

user.

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

2.  The PATIENT CONTACT RELATION file (#12.11) is populated with the following data. Only active entries are allowed to be entered.

NUMBER NAME ACTIVE?

------ ---------------- -------

1 BROTHER YES

2 CHILD-IN-LAW YES

3 DAUGHTER YES

4 EXTENDED FAMILY MEMBER YES

5 FATHER YES

6 GRANDCHILD YES

7 HUSBAND YES

8 MOTHER YES

9 NIECE/NEPHEW YES

10 SISTER YES

11 SON YES

12 STEPCHILD YES

13 UNRELATED FRIEND/OTHER YES

14 WARD YES

15 WIFE YES

3.  The PATIENT file (#2) has the following new fields added.

\- K-RELATIONSHIP TYPE field (#.224)

\- K2-RELATIONSHIP TYPE field (#.2104)

\- E-RELATIONSHIP TYPE field (#.3309)

\- E2-RELATIONSHIP TYPE field (#.331015)

\- D-RELATIONSHIP TYPE field (#.34015)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.224 K-RELATIONSHIP TYPE .21;15 POINTER TO PATIENT CONTACT

RELATION FILE (#12.11)

(audited)

INPUT TRANSFORM: S DIC("S")="I

\$\$GET1^DIQ(12.11,Y,.03,""I"")" D ^DIC K

DIC S DIC=DIE,X=+Y K:Y\<0 X I \$D(X) S DFN

=DA D K1^DGLOCK2

LAST EDITED: JAN 06, 2022

HELP-PROMPT: Enter the relationship of the primary NOK

to the patient.

DESCRIPTION: If a primary next-of-kin is specified,

enter the relationship of that person to

the applicant. This field cannot be

deleted as long as a 'next of kin' name is

on file.

SCREEN: S DIC("S")="I

\$\$GET1^DIQ(12.11,Y,.03,""I"")"

EXPLANATION: Enter active relation types only.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D K1D^DGLOCK2 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM3 (#597) MUMPS ACTION

Short Descr: PRIMARY NOK Cross-Reference

Description: This cross-reference will update the

PRIMARY NOK CHANGE DATE/TIME field when

the Primary Next of Kin data changes for a

patient.

Set Logic: D PNOK^DGDDDTTM

Kill Logic: D PNOK^DGDDDTTM

X(1): K-NAME OF PRIMARY NOK (2,.211)

(forwards)

X(2): K-RELATIONSHIP TO PATIENT (2,.212)

(forwards)

X(3): K-STREET ADDRESS \[LINE 1\] (2,.213)

(forwards)

X(4): K-STREET ADDRESS \[LINE 2\] (2,.214)

(forwards)

X(5): K-STREET ADDRESS \[LINE 3\] (2,.215)

(forwards)

X(6): K-CITY (2,.216) (forwards)

X(7): K-STATE (2,.217) (forwards)

X(8): K-ZIP CODE (2,.218) (forwards)

X(9): K-ADDRESS SAME AS PATIENT'S? (2,.2125)

(forwards)

X(10): K-ZIP+4 (2,.2207) (forwards)

X(11): K-PHONE NUMBER (2,.219) (forwards)

X(12): K-WORK PHONE NUMBER (2,.21011)

(forwards)

X(13): K-COUNTRY (2,.221) (forwards)

X(14): K-PROVINCE (2,.222) (forwards)

X(15): K-POSTAL CODE (2,.223) (forwards)

X(16): K-RELATIONSHIP TYPE (2,.224) (forwards)

FILES POINTED TO FIELDS

PATIENT CONTACT RELATION

(#12.11) K-RELATIONSHIP TYPE (#.224)

2,.2104 K2-RELATIONSHIP TYPE .211;15 POINTER TO PATIENT CONTACT

RELATION FILE (#12.11)

(audited)

INPUT TRANSFORM: S DIC("S")="I

\$\$GET1^DIQ(12.11,Y,.03,""I"")" D ^DIC K

DIC S DIC=DIE,X=+Y K:Y\<0 X I \$D(X) S

DFN=DA D K2^DGLOCK2

LAST EDITED: JAN 05, 2022

HELP-PROMPT: Enter the relationship of the secondary

NOK to the patient.

DESCRIPTION: If a secondary next-of-kin is specified,

enter the relationship of that person to

the applicant. This field cannot be

deleted as long as a secondary NOK is on

file.

SCREEN: S DIC("S")="I

\$\$GET1^DIQ(12.11,Y,.03,""I"")"

EXPLANATION: Enter active relation types only.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D K2D^DGLOCK2 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM4 (#598) MUMPS ACTION

Short Descr: SECONDARY NOK Cross-Reference

Description: This cross-reference will update the

SECONDARY NOK CHANGE DATE/TIME field when

the Secondary Next of Kin data changes for

a patient.

Set Logic: D SNOK^DGDDDTTM

Kill Logic: D SNOK^DGDDDTTM

X(1): K2-NAME OF SECONDARY NOK (2,.2191)

(forwards)

X(2): K2-RELATIONSHIP TO PATIENT (2,.2192)

(forwards)

X(3): K2-STREET ADDRESS \[LINE 1\] (2,.2193)

(forwards)

X(4): K2-STREET ADDRESS \[LINE 2\] (2,.2194)

(forwards)

X(5): K2-STREET ADDRESS \[LINE 3\] (2,.2195)

(forwards)

X(6): K2-CITY (2,.2196) (forwards)

X(7): K2-STATE (2,.2197) (forwards)

X(8): K2-ZIP CODE (2,.2198) (forwards)

X(9): K2-ADDRESS SAME AS PATIENT'S? (2,.21925)

(forwards)

X(10): K2-ZIP+4 (2,.2203) (forwards)

X(11): K2-PHONE NUMBER (2,.2199) (forwards)

X(12): K2-WORK PHONE NUMBER (2,.211011)

(forwards)

X(13): K2-COUNTRY (2,.2101) (forwards)

X(14): K2-PROVINCE (2,.2102) (forwards)

X(15): K2-POSTAL CODE (2,.2103) (forwards)

X(16): K2-RELATIONSHIP TYPE (2,.2104)

(forwards)

FILES POINTED TO FIELDS

PATIENT CONTACT RELATION

(#12.11) K2-RELATIONSHIP TYPE (#.2104)

2,.3309 E-RELATIONSHIP TYPE .33;15 POINTER TO PATIENT CONTACT REL

ATION FILE (#12.11) (audited)

INPUT TRANSFORM: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)" D ^DIC K DIC S DIC=DIE,X=+Y K:Y\<0 X I \$

D(X) S DFN=DA D E1^DGLOCK2

LAST EDITED: JAN 05, 2022

HELP-PROMPT: Enter the relationship of the emergency

contact to the patient.

DESCRIPTION: If a primary emergency contact is

specified, enter the relationship of that

person to the applicant. This field cannot

be deleted as long as a primary emergency

contact is on file.

SCREEN: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)"

EXPLANATION: Enter active relation types only.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D E1D^DGLOCK2 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM5 (#599) MUMPS ACTION

Short Descr: E-CONTACT Cross-Reference

Description: This cross-reference will update the

E-CONTACT CHANGE DATE/TIME field when the

Emergency Contact data changes for a

patient.

Set Logic: D ECON^DGDDDTTM

Kill Logic: D ECON^DGDDDTTM

X(1): E-NAME (2,.331) (forwards)

X(2): E-RELATIONSHIP TO PATIENT (2,.332)

(forwards)

X(3): E-STREET ADDRESS \[LINE 1\] (2,.333)

(forwards)

X(4): E-STREET ADDRESS \[LINE 2\] (2,.334)

(forwards)

X(5): E-STREET ADDRESS \[LINE 3\] (2,.335)

(forwards)

X(6): E-CITY (2,.336) (forwards)

X(7): E-STATE (2,.337) (forwards)

X(8): E-ZIP CODE (2,.338) (forwards)

X(9): E-EMER. CONTACT SAME AS NOK? (2,.3305)

(forwards)

X(10): E-ZIP+4 (2,.2201) (forwards)

X(11): E-PHONE NUMBER (2,.339) (forwards)

X(12): E-WORK PHONE NUMBER (2,.33011)

(forwards)

X(13): E-COUNTRY (2,.3306) (forwards)

X(14): E-PROVINCE (2,.3307) (forwards)

X(15): E-POSTAL CODE (2,.3308) (forwards)

X(16): E-RELATIONSHIP TYPE (2,.3309) (forwards)

FILES POINTED TO FIELDS

PATIENT CONTACT RELATION

(#12.11) E-RELATIONSHIP TYPE (#.3309)

2,.331015 E2-RELATIONSHIP TYPE .331;15 POINTER TO PATIENT CONTACT RE

LATION FILE (#12.11) (audited)

INPUT TRANSFORM: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)" D ^DIC K DIC S DIC=DIE,X=+Y K:Y\<0 X I \$

D(X) S DFN=DA D E2^DGLOCK2

LAST EDITED: JAN 05, 2022

HELP-PROMPT: Enter the relationship of the secondary

emergency contact to the patient.

DESCRIPTION: If a secondary emergency contact is

specified, enter the relationship of that

person to the applicant. This field cannot

be deleted as long as a secondary

emergency contact is on file.

SCREEN: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)"

EXPLANATION: Enter active relation types only.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D E2D^DGLOCK2 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM6 (#600) MUMPS ACTION

Short Descr: E2-CONTACT Cross-Reference

Description: This cross-reference will update the

E2-CONTACT CHANGE DATE/TIME field when the

Secondary Emergency Contact data changes

for a patient.

Set Logic: D ECON2^DGDDDTTM

Kill Logic: D ECON2^DGDDDTTM

X(1): E2-NAME OF SECONDARY CONTACT (2,.3311)

(forwards)

X(2): E2-RELATIONSHIP TO PATIENT (2,.3312)

(forwards)

X(3): E2-STREET ADDRESS \[LINE 1\] (2,.3313)

(forwards)

X(4): E2-STREET ADDRESS \[LINE 2\] (2,.3314)

(forwards)

X(5): E2-STREET ADDRESS \[LINE 3\] (2,.3315)

(forwards)

X(6): E2-CITY (2,.3316) (forwards)

X(7): E2-STATE (2,.3317) (forwards)

X(8): E2-ZIP CODE (2,.3318) (forwards)

X(9): E2-ZIP+4 (2,.2204) (forwards)

X(10): E2-PHONE NUMBER (2,.3319) (forwards)

X(11): E2-WORK PHONE NUMBER (2,.331011)

(forwards)

X(12): E2-COUNTRY (2,.331012) (forwards)

X(13): E2-PROVINCE (2,.331013) (forwards)

X(14): E2-POSTAL CODE (2,.331014) (forwards)

X(15): E2-RELATIONSHIP TYPE (2,.331015)

(forwards)

FILES POINTED TO FIELDS

PATIENT CONTACT RELATION

(#12.11) E2-RELATIONSHIP TYPE (#.331015)

2,.34015 D-RELATIONSHIP TYPE .34;15 POINTER TO PATIENT CONTACT REL

ATION FILE (#12.11) (audited)

INPUT TRANSFORM: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)" D ^DIC K DIC S DIC=DIE,X=+Y K:Y\<0 X I \$

D(X) S DFN=DA D D^DGLOCK2

LAST EDITED: JAN 05, 2022

HELP-PROMPT: Enter the relationship of the designee to

the patient.

DESCRIPTION: If a designee is specified, enter the

relationship of that person to the

applicant. This field cannot be deleted as

long as a designee is on file.

SCREEN: S DIC("S")="I \$\$GET1^DIQ(12.11,Y,.03,""I""

)"

EXPLANATION: Enter active relation types only.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D DD^DGLOCK2 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM7 (#601) MUMPS ACTION

Short Descr: DESIGNEE Cross-Reference

Description: This cross-reference will update the

DESIGNEE CHANGE DATE/TIME field when the

Designee data changes for a patient.

Set Logic: D DESIG^DGDDDTTM

Kill Logic: D DESIG^DGDDDTTM

X(1): D-NAME OF DESIGNEE (2,.341) (forwards)

X(2): D-RELATIONSHIP TO PATIENT (2,.342)

(forwards)

X(3): D-STREET ADDRESS \[LINE 1\] (2,.343)

(forwards)

X(4): D-STREET ADDRESS \[LINE 2\] (2,.344)

(forwards)

X(5): D-STREET ADDRESS \[LINE 3\] (2,.345)

(forwards)

X(6): D-CITY (2,.346) (forwards)

X(7): D-STATE (2,.347) (forwards)

X(8): D-ZIP CODE (2,.348) (forwards)

X(9): D-DESIGNEE SAME AS NOK? (2,.3405)

(forwards)

X(10): D-ZIP+4 (2,.2202) (forwards)

X(11): D-PHONE NUMBER (2,.349) (forwards)

X(12): D-WORK PHONE NUMBER (2,.34011)

(forwards)

X(13): D-COUNTRY (2,.34012) (forwards)

X(14): D-PROVINCE (2,.34013) (forwards)

X(15): D-POSTAL CODE (2,.34014) (forwards)

X(16): D-RELATIONSHIP TYPE (2,.34015)

(forwards)

FILES POINTED TO FIELDS

PATIENT CONTACT RELATION

(#12.11) D-RELATIONSHIP TYPE (#.34015)

4.  The Help Text and Descriptions for the K-RELATIONSHIP TO PATIENT field (#.212), K2-RELATIONSHIP TO PATIENT field (#.2192), E-RELATIONSHIP TO PATIENT field (#.332), E2-RELATIONSHIP TO PATIENT field (#.3312) and D-RELATIONSHIP TO PATIENT field (#.342) of the PATIENT file (#2), shown below, are modified.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.212 K-RELATIONSHIP TO PATIENT .21;2 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<1) X I \$D(X) S DFN=DA D

K1^DGLOCK2

LAST EDITED: DEC 14, 2021

HELP-PROMPT: Enter any notes related to the

relationship of the primary NOK to the

patient \[1-30 characters\].

DESCRIPTION: If a primary next-of-kin is specified,

enter any additional information regarding

the relationship of that person to the

applicant \[1-30 characters\]. This field

cannot be deleted as long as a 'next of

kin' name is on file.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D K1D^DGLOCK2 I '\$D(X)

GROUP: NK1

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: 2^ADGRU212^MUMPS

1)= D:(\$T(ADGRU^DGRUDD01)'="")

ADGRU^DGRUDD01(DA)

2)= D:(\$T(ADGRU^DGRUDD01)'="")

ADGRU^DGRUDD01(DA)

This cross reference is used to remember

that changes were made to a monitored data

field in the PATIENT File (#2) required

for a vendor RAI/MDS COTS system.

Execution of this cross reference will

create an entry in the ADT/HL7 PIVOT file

(#391.71) and mark it as requiring

transmission of an HL7 demographic A08

update message to the COTS interface.

The local variable DGRUGA08 will be set

to 1 if the cross reference is not to be

executed as part of a re-indexing.

RECORD INDEX: ADTTM3 (#597) MUMPS ACTION

Short Descr: PRIMARY NOK Cross-Reference

Description: This cross-reference will update the

PRIMARY NOK CHANGE DATE/TIME field when

the Primary Next of Kin data changes for a

patient.

Set Logic: D PNOK^DGDDDTTM

Kill Logic: D PNOK^DGDDDTTM

X(1): K-NAME OF PRIMARY NOK (2,.211)

(forwards)

X(2): K-RELATIONSHIP TO PATIENT (2,.212)

(forwards)

X(3): K-STREET ADDRESS \[LINE 1\] (2,.213)

(forwards)

X(4): K-STREET ADDRESS \[LINE 2\] (2,.214)

(forwards)

X(5): K-STREET ADDRESS \[LINE 3\] (2,.215)

(forwards)

X(6): K-CITY (2,.216) (forwards)

X(7): K-STATE (2,.217) (forwards)

X(8): K-ZIP CODE (2,.218) (forwards)

X(9): K-ADDRESS SAME AS PATIENT'S? (2,.2125)

(forwards)

X(10): K-ZIP+4 (2,.2207) (forwards)

X(11): K-PHONE NUMBER (2,.219) (forwards)

X(12): K-WORK PHONE NUMBER (2,.21011)

(forwards)

X(13): K-COUNTRY (2,.221) (forwards)

X(14): K-PROVINCE (2,.222) (forwards)

X(15): K-POSTAL CODE (2,.223) (forwards)

X(16): K-RELATIONSHIP TYPE (2,.224) (forwards)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.2192 K2-RELATIONSHIP TO PATIENT .211;2 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<1) X I \$D(X) S DFN=DA D

K2^DGLOCK2

LAST EDITED: DEC 13, 2021

HELP-PROMPT: Enter any notes related to the

relationship of the secondary NOK to the

patient \[1-30 characters\].

DESCRIPTION: If a secondary next-of-kin is specified,

enter any additional information regarding

the relationship of that person to the

applicant \[1-30 characters\]. This field

cannot be deleted as long as a secondary

NOK is on file.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D K2D^DGLOCK2 I '\$D(X)

GROUP: NK2

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM4 (#598) MUMPS ACTION

Short Descr: SECONDARY NOK Cross-Reference

Description: This cross-reference will update the

SECONDARY NOK CHANGE DATE/TIME field when

the Secondary Next of Kin data changes for

a patient.

Set Logic: D SNOK^DGDDDTTM

Kill Logic: D SNOK^DGDDDTTM

X(1): K2-NAME OF SECONDARY NOK (2,.2191)

(forwards)

X(2): K2-RELATIONSHIP TO PATIENT (2,.2192)

(forwards)

X(3): K2-STREET ADDRESS \[LINE 1\] (2,.2193)

(forwards)

X(4): K2-STREET ADDRESS \[LINE 2\] (2,.2194)

(forwards)

X(5): K2-STREET ADDRESS \[LINE 3\] (2,.2195)

(forwards)

X(6): K2-CITY (2,.2196) (forwards)

X(7): K2-STATE (2,.2197) (forwards)

X(8): K2-ZIP CODE (2,.2198) (forwards)

X(9): K2-ADDRESS SAME AS PATIENT'S? (2,.21925)

(forwards)

X(10): K2-ZIP+4 (2,.2203) (forwards)

X(11): K2-PHONE NUMBER (2,.2199) (forwards)

X(12): K2-WORK PHONE NUMBER (2,.211011)

(forwards)

X(13): K2-COUNTRY (2,.2101) (forwards)

X(14): K2-PROVINCE (2,.2102) (forwards)

X(15): K2-POSTAL CODE (2,.2103) (forwards)

X(16): K2-RELATIONSHIP TYPE (2,.2104)

(forwards)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.332 E-RELATIONSHIP TO PATIENT .33;2 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<2) X I \$D(X) S DFN=DA D

E1^DGLOCK2

LAST EDITED: DEC 13, 2021

HELP-PROMPT: Enter any notes related to the

relationship of the emergency contact to

the patient \[3-35 characters\].

DESCRIPTION: If a primary emergency contact is

specified, enter any additional

information regarding the relationship of

that person to the applicant \[3-35

characters\]. This field cannot be deleted

as long as a primary emergency contact is

on file.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D E1D^DGLOCK2 I '\$D(X)

GROUP: EC1

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM5 (#599) MUMPS ACTION

Short Descr: E-CONTACT Cross-Reference

Description: This cross-reference will update the

E-CONTACT CHANGE DATE/TIME field when the

Emergency Contact data changes for a

patient.

Set Logic: D ECON^DGDDDTTM

Kill Logic: D ECON^DGDDDTTM

X(1): E-NAME (2,.331) (forwards)

X(2): E-RELATIONSHIP TO PATIENT (2,.332)

(forwards)

X(3): E-STREET ADDRESS \[LINE 1\] (2,.333)

(forwards)

X(4): E-STREET ADDRESS \[LINE 2\] (2,.334)

(forwards)

X(5): E-STREET ADDRESS \[LINE 3\] (2,.335)

(forwards)

X(6): E-CITY (2,.336) (forwards)

X(7): E-STATE (2,.337) (forwards)

X(8): E-ZIP CODE (2,.338) (forwards)

X(9): E-EMER. CONTACT SAME AS NOK? (2,.3305)

(forwards)

X(10): E-ZIP+4 (2,.2201) (forwards)

X(11): E-PHONE NUMBER (2,.339) (forwards)

X(12): E-WORK PHONE NUMBER (2,.33011)

(forwards)

X(13): E-COUNTRY (2,.3306) (forwards)

X(14): E-PROVINCE (2,.3307) (forwards)

X(15): E-POSTAL CODE (2,.3308) (forwards)

X(16): E-RELATIONSHIP TYPE (2,.3309) (forwards)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.3312 E2-RELATIONSHIP TO PATIENT .331;2 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<2) X I \$D(X) S DFN=DA D

E2^DGLOCK2

LAST EDITED: DEC 13, 2021

HELP-PROMPT: Enter any notes related to the

relationship of the secondary emergency

contact to the patient \[2-30 characters\].

DESCRIPTION: If a secondary emergency contact is

specified, enter any additional

information regarding the relationship of

that person to the applicant \[2-30

characters\]. This field cannot be deleted

as long as a secondary emergency contact

is on file.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D E2D^DGLOCK2 I '\$D(X)

GROUP: EC2

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM6 (#600) MUMPS ACTION

Short Descr: E2-CONTACT Cross-Reference

Description: This cross-reference will update the

E2-CONTACT CHANGE DATE/TIME field when the

Secondary Emergency Contact data changes

for a patient.

Set Logic: D ECON2^DGDDDTTM

Kill Logic: D ECON2^DGDDDTTM

X(1): E2-NAME OF SECONDARY CONTACT (2,.3311)

(forwards)

X(2): E2-RELATIONSHIP TO PATIENT (2,.3312)

(forwards)

X(3): E2-STREET ADDRESS \[LINE 1\] (2,.3313)

(forwards)

X(4): E2-STREET ADDRESS \[LINE 2\] (2,.3314)

(forwards)

X(5): E2-STREET ADDRESS \[LINE 3\] (2,.3315)

(forwards)

X(6): E2-CITY (2,.3316) (forwards)

X(7): E2-STATE (2,.3317) (forwards)

X(8): E2-ZIP CODE (2,.3318) (forwards)

X(9): E2-ZIP+4 (2,.2204) (forwards)

X(10): E2-PHONE NUMBER (2,.3319) (forwards)

X(11): E2-WORK PHONE NUMBER (2,.331011)

(forwards)

X(12): E2-COUNTRY (2,.331012) (forwards)

X(13): E2-PROVINCE (2,.331013) (forwards)

X(14): E2-POSTAL CODE (2,.331014) (forwards)

X(15): E2-RELATIONSHIP TYPE (2,.331015)

(forwards)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.342 D-RELATIONSHIP TO PATIENT .34;2 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<3) X I \$D(X) S DFN=DA D

D^DGLOCK2

LAST EDITED: DEC 13, 2021

HELP-PROMPT: Enter any notes related to the

relationship of the designee to the

patient \[3-30 characters\].

DESCRIPTION: If a designee is specified, enter any

additional information regarding the

relationship of that person to the

applicant \[3-30 characters\]. This field

cannot be deleted as long as a designee is

on file.

AUDIT: YES, ALWAYS

DELETE TEST: 1,0)= S DFN=DA D DD^DGLOCK2 I '\$D(X)

GROUP: D1

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

RECORD INDEX: ADTTM7 (#601) MUMPS ACTION

Short Descr: DESIGNEE Cross-Reference

Description: This cross-reference will update the

DESIGNEE CHANGE DATE/TIME field when the

Designee data changes for a patient.

Set Logic: D DESIG^DGDDDTTM

Kill Logic: D DESIG^DGDDDTTM

X(1): D-NAME OF DESIGNEE (2,.341) (forwards)

X(2): D-RELATIONSHIP TO PATIENT (2,.342)

(forwards)

X(3): D-STREET ADDRESS \[LINE 1\] (2,.343)

(forwards)

X(4): D-STREET ADDRESS \[LINE 2\] (2,.344)

(forwards)

X(5): D-STREET ADDRESS \[LINE 3\] (2,.345)

(forwards)

X(6): D-CITY (2,.346) (forwards)

X(7): D-STATE (2,.347) (forwards)

X(8): D-ZIP CODE (2,.348) (forwards)

X(9): D-DESIGNEE SAME AS NOK? (2,.3405)

(forwards)

X(10): D-ZIP+4 (2,.2202) (forwards)

X(11): D-PHONE NUMBER (2,.349) (forwards)

X(12): D-WORK PHONE NUMBER (2,.34011)

(forwards)

X(13): D-COUNTRY (2,.34012) (forwards)

X(14): D-PROVINCE (2,.34013) (forwards)

X(15): D-POSTAL CODE (2,.34014) (forwards)

X(16): D-RELATIONSHIP TYPE (2,.34015)

(forwards)

5.  Four entries are added to the PATIENT REGISTRATION ONLY REASON file (#408.43). The field values for each are listed below.  
    NOTE: These entries are not available for selection by the user during registration until the current date/time is greater than or equal to the "DG PATCH DG\*5.3\*1067 ACTIVE" parameter date/time value. See item 9 below for information on this parameter.

REASON (#.01) AVAILABILITY (#.02) CODE (#.03)

------------- ------------------- -----------

4TH MISSION COLLATERAL OF PATIENT 20

CLINICAL EVALUATION REGISTER A PATIENT 21

HUD-VASH REGISTER A PATIENT 22

IMMUNIZATIONS COLLATERAL OF PATIENT 23

6.  A new cross-reference is added to the RELIGIOUS PREFERENCE field (#.08) of the PATIENT file (#2). This cross-reference is used to notify HEC of changes that may affect enrollment.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.08 RELIGIOUS PREFERENCE 0;8 POINTER TO RELIGION FILE (#13)

(audited)

RELIGION

LAST EDITED: DEC 07, 2021

HELP-PROMPT: Select from the available list this

patients religious preference.

DESCRIPTION: Select from the available listing the

religious preference of this applicant.

AUDIT: YES, ALWAYS

GROUP: DEMOG

CROSS-REFERENCE: 2^AVAFC08^MUMPS

1)= I (\$T(AVAFC^VAFCDD01)'="") S

VAFCF=".08;" D AVAFC^VAFCDD01(DA)

2)= I (\$T(AVAFC^VAFCDD01)'="") S

VAFCF=".08;" D AVAFC^VAFCDD01(DA)

This cross reference is used to remember

that changes were made to the PATIENT file

(#2) outside of the Registration process.

Execution of this cross reference will

create an entry in the ADT/HL7 PIVOT file

(#391.71) and mark it as requiring

transmission of an HL7 ADT-A08 message.

The local variable VAFCFLG will be set to

1 if the cross reference is not executed

because the change is being made from

within the Registration process.

Execution of this cross reference can be

prevented by setting the local variable

VAFCA08 equal to 1.

The local variable VAFCF is used to

identify the field edited. This data is

stored in the FIELD(S) EDITED (#2.1) field

in the ADT/HL7 PIVOT file (#391.71).

CROSS-REFERENCE: 2^ADGRU08^MUMPS

1)= D:(\$T(ADGRU^DGRUDD01)'="")

ADGRU^DGRUDD01(DA)

2)= D:(\$T(ADGRU^DGRUDD01)'="")

ADGRU^DGRUDD01(DA)

This cross reference is used to remember

that changes were made to a monitored data

field in the PATIENT File (#2) required

for a vendor RAI/MDS COTS system.

Execution of this cross reference will

create an entry in the ADT/HL7 PIVOT file

(#391.71) and mark it as requiring

transmission of an HL7 demographic A08

update message to the COTS interface.

The local variable DGRUGA08 will be set

to 1 if the cross reference is not to be

executed as part of a re-indexing.

CROSS-REFERENCE: 2^AENR08^MUMPS

1)= D EVENT^IVMPLOG(DA)

2)= D EVENT^IVMPLOG(DA)

3)= DO NOT DELETE

This cross-reference is used to notify

HEC of changes that may affect enrollment.

FILES POINTED TO FIELDS

RELIGION (#13) RELIGIOUS PREFERENCE (#.08)

7.  A new cross-reference is added to the RACE INFORMATION field (#.01) of the RACE INFORMATION subfile (#2.02) of the PATIENT file (#2). This cross-reference is used to notify HEC of changes that may affect enrollment.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

---------------------------------------------------------------------

2.02,.01 RACE INFORMATION 0;1 POINTER TO RACE FILE (#10)

(Multiply asked)

INPUT TRANSFORM: S DIC("S")="I '\$G(^(.02))" D ^DIC K D

IC S DIC=\$G(DIE),X=+Y K:Y\<0 X S:\$D(X)

DINUM=X

LAST EDITED: DEC 05, 2021

HELP-PROMPT: Select from the available listing all

races which best identify this patient

DESCRIPTION: Patient's race

SCREEN: S DIC("S")="I '\$G(^(.02))"

EXPLANATION: Inactive values are not selectable

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: 2.02^B

1)= S ^DPT(DA(1),.02,"B",\$E(X,1,30),DA)=""

2)= K ^DPT(DA(1),.02,"B",\$E(X,1,30),DA)

CROSS-REFERENCE: ^^TRIGGER^2.02^.02

1)= X ^DD(2.02,.01,1,2,1.3) I X S X=D

IV S Y(1)=\$S(\$D(^DPT(D0,.02,D1,0)):^(

0),1:"") S X=\$P(Y(1),U,2),X=X S DIU=X

K Y S X=DIV S X=+\$O(^DIC(10.3,"C","S

",0)) S:X=0 X="" X ^DD(2.02,.01,1,2,1

.4)

1.3)= K DIV S DIV=X,D0=DA(1),DIV(0)=D

0,D1=DA,DIV(1)=D1 S Y(0)=X S Y(1)=\$S(

\$D(^DPT(D0,.02,D1,0)):^(0),1:"") S X=

\$S('\$D(^DIC(10.3,+\$P(Y(1),U,2),0)):""

,1:\$P(^(0),U,1))=""

1.4)= S DIH=\$G(^DPT(DIV(0),.02,DIV(1)

,0)),DIV=X S \$P(^(0),U,2)=DIV,DIH=2.0

2,DIG=.02 D ^DICR

2)= Q

CREATE CONDITION)= METHOD OF COLLECTION=""

CREATE VALUE)= S X=+\$O(^DIC(10.3,"C",

"S",0)) S:X=0 X=""

DELETE VALUE)= NO EFFECT

FIELD)= METHOD

SELF IDENTIFICATION is the default

value for collection method

CROSS-REFERENCE: 2^AENR20201^MUMPS

1)= D EVENT^IVMPLOG(\$G(DA(1)))

2)= D EVENT^IVMPLOG(\$G(DA(1)))

3)= DO NOT DELETE

This cross-reference is used to notify

HEC of changes that may affect enrollment.

FIELD INDEX: AVAFC20201 (#374) MUMPS I

ACTION

Short Descr: This x-ref calls the DG FIELD MONITOR

event point.

Description: This cross reference activates the DG

FIELD MONITOR event point.

Applications that wish to monitor

edit activity related to this field

may subscribe to that event point and

take action as indicated by the

changes that occur. Refer to the DG

FIELD MONITOR protocol for a

description of the information

available at the time of the event.

Set Logic: D FC^DGFCPROT(.DA,2.02,.01,"SET",\$H,\$

G(DUZ),.X,.X1,.X2,\$G(XQY0)) Q

Kill Logic: D FC^DGFCPROT(.DA,2.02,.01,"KILL",\$H,

\$G(DUZ),.X,.X1,.X2,\$G(XQY0)) Q

X(1): RACE INFORMATION (2.02,.01)

(forwards)

FILES POINTED TO FIELDS

RACE (#10) RACE INFORMATION (#.01)

8.  A new cross-reference is added to the ETHNICITY INFORMATION field (#.01) of the ETHNICITY INFORMATION subfile (#2.06) of the PATIENT file (#2). This cross-reference is used to notify HEC of changes that may affect enrollment.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2.06,.01 ETHNICITY INFORMATION 0;1 POINTER TO ETHNICITY FILE (#10.2)

INPUT TRANSFORM: S DIC("S")="I '\$G(^(.02))" D ^DIC K DIC S

DIC=DIE,X=+Y K:Y\<0 X S:\$D(X) DINUM=X

LAST EDITED: DEC 05, 2021

HELP-PROMPT: Select from the available listing the

ethnicity which best identifies this

patient

DESCRIPTION: Patient's ethnicity

TECHNICAL DESCR: Although this field is defined to be

multi-valued, the AONLYONE cross reference

prevents multiple values from being

stored. This is because the current

business definition for ethnicity only

accounts for a single value.

SCREEN: S DIC("S")="I '\$G(^(.02))"

EXPLANATION: Inactive values are not selectable

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: 2.06^B

1)= S ^DPT(DA(1),.06,"B",\$E(X,1,30),DA)=""

2)= K ^DPT(DA(1),.06,"B",\$E(X,1,30),DA)

CROSS-REFERENCE: ^^TRIGGER^2.06^.02

1)= X ^DD(2.06,.01,1,2,1.3) I X S X=DIV S

Y(1)=\$S(\$D(^DPT(D0,.06,D1,0)):^(0),1:"") S

X=\$P(Y(1),U,2),X=X S DIU=X K Y S X=DIV S

X=+\$O(^DIC(10.3,"C","S",0)) S:X=0 X="" X ^

DD(2.06,.01,1,2,1.4)

1.3)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=

DA,DIV(1)=D1 S Y(0)=X S Y(1)=\$S(\$D(^DPT(D0

,.06,D1,0)):^(0),1:"") S X=\$S('\$D(^DIC(10.

3,+\$P(Y(1),U,2),0)):"",1:\$P(^(0),U,1))=""

1.4)= S DIH=\$G(^DPT(DIV(0),.06,DIV(1),0)),

DIV=X S \$P(^(0),U,2)=DIV,DIH=2.06,DIG=.02

D ^DICR

2)= Q

CREATE CONDITION)= METHOD OF COLLECTION=""

CREATE VALUE)= S X=+\$O(^DIC(10.3,"C","S",0

)) S:X=0 X=""

DELETE VALUE)= NO EFFECT

FIELD)= METHOD

SELF IDENTIFICATION is the default value

for collection method

CROSS-REFERENCE: 2^AENR20601^MUMPS

1)= D EVENT^IVMPLOG(\$G(DA(1)))

2)= D EVENT^IVMPLOG(\$G(DA(1)))

3)= DO NOT DELETE

This cross-reference is used to notify

HEC of changes that may affect enrollment.

FIELD INDEX: AONLYONE (#172) MUMPS ACTION

Short Descr: Only one entry allowed in multiple

Description: Cross reference deletes all entries in the

multiple EXCEPT the one just added. This

has the net affect of only allowing one

entry to exist in the multiple.

Set Logic: N DGFDA,DGMSG,DGD0,DGD1,DGLOOP S DGD0=DA(1

),DGD1=DA S DGLOOP=0 F S DGLOOP=\$O(^DPT(D

GD0,.06,DGLOOP)) Q:'DGLOOP I DGLOOP'=DGD1

S DGFDA(2.06,DGLOOP\_","\_DGD0\_",",.01)="@"

D FILE^DIE("","DGFDA","DGMSG") K DGFDA,DG

MSG

Kill Logic: Q

X(1): ETHNICITY INFORMATION (2.06,.01)

(forwards)

FIELD INDEX: AVAFC20601 (#375) MUMPS I ACTION

Short Descr: This x-ref calls the DG FIELD MONITOR

event point.

Description: This cross reference activates the DG

FIELD MONITOR event point. Applications

that wish to monitor edit activity related

to this field may subscribe to that event

point and take action as indicated by the

changes that occur. Refer to the DG FIELD

MONITOR protocol for a description of the

information available at the time of the

event.

Set Logic: D FC^DGFCPROT(.DA,2.06,.01,"SET",\$H,\$G(DUZ

),.X,.X1,.X2,\$G(XQY0)) Q

Kill Logic: D FC^DGFCPROT(.DA,2.06,.01,"KILL",\$H,\$G(DU

Z),.X,.X1,.X2,\$G(XQY0)) Q

X(1): ETHNICITY INFORMATION (2.06,.01)

(forwards)

FILES POINTED TO FIELDS

ETHNICITY (#10.2) ETHNICITY INFORMATION (#.01)

9.  A new parameter DG PATCH DG\*5.3\*1067 ACTIVE is added to the PARAMETER DEFINITION file (#8989.51). A timestamp value of Feb 26, 2022@1700 is stored in this parameter indicating when the new Registration Only Reasons (see item 5 above) will be active. The timestamp value is set via post-install routine POST^DG531067P.

NUMBER: 1055 NAME: DG PATCH DG\*5.3\*1067 ACTIVE

DISPLAY TEXT: Active date/time for patch DG\*5.3\*1067

MULTIPLE VALUED: No PROHIBIT EDITING: No

VALUE DATA TYPE: date/time VALUE DOMAIN: ::T

VALUE HELP: Enter the date/time when patch DG\*5.3\*1067 becomes active.

DESCRIPTION:

This parameter contains the date/time when the functionality in patch

DG\*5.3\*1067 becomes active.

PRECEDENCE: 1 ENTITY FILE: PACKAGE

> An instance of this parameter is created in the PARAMETER file (#8989.5) with a timestamp value of Feb 26, 2022@1700. This parameter indicates when the new Registration Only Reasons (see item 5 above) will be active. The parameter is created and the timestamp value is set via post-install routine POST^DG531067P.

ENTITY (PKG): REGISTRATION PARAMETER: DG PATCH DG\*5.3\*1067

ACTIVE

INSTANCE: 1 VALUE: FEB 26, 2022@17:00

SECTION 2: VHAP UPDATES

1.  Two new VHA Profiles are added to the VistA HEALTH BENEFIT PLAN file (#25.11), shown below.

NUMBER: 94 NAME : ACTIVE DUTY

PLAN CODE: 303 COVERAGE CODE: AD01001

SHORT DESCRIPTION:

AD

LONG DESCRIPTION:

Active Duty (AD) and AD Family Prime

------------------------------------

Patient receiving care at a VAMC as AD of the Department of Defense:

\*TRICARE Authorization:

\- Required for TRICARE Prime patients - AD and AD Family Prime

\*If patient has a Veteran status and on Active Duty Orders, then all

Active Duty rules apply

\- Even if treatment is Service Connected - Patient considered TRICARE

Prime enrollee

\- Includes active Reserve and National Guard - Federal orders must

exceed 30 days

NUMBER: 95 NAME : JOINT INCENTIVE FUND

PLAN CODE: 304 COVERAGE CODE: JF01001

SHORT DESCRIPTION:

JIF

LONG DESCRIPTION:

VA/DoD Joint Incentive Fund (JIF)

---------------------------------

Patient receiving care at either VA Medical Center or Department of

Defense (DoD) facility under an active JIF project in which

bi-directional billing for shared resources will not occur:

\* Eligible Veteran referred to DoD for health care treatment / (ref.

VHA OCC DoD Referral Management SOP)

\* Eligible DoD beneficiaries (including TRICARE beneficiaries) referred

to VA for health care treatment

\* TRICARE authorization not applicable (services are not billed to

TRICARE)

2.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 295 field values for NAME field (#.01), SHORT DESCRIPTION field (#.03) and LONG DESCRIPTION field (#.04) are modified as shown below. The plan was originally named VA DOD DIRECT RESOURCE SHARING AGREEMENTS.

NAME : VA DOD SHARING MEDICAL RESOURCES

PLAN CODE: 295 COVERAGE CODE: DR01001

SHORT DESCRIPTION:

SHAGR

LONG DESCRIPTION:

VA/DoD Health Care Resource Sharing Agreements (38 USC 8111)

------------------------------------------------------------

Patient receiving care at Department of Defense (DoD) under a Health

Care Resource Sharing Agreement:

\* Eligible Veteran referred to DoD for health care treatment / (ref.

VHA OCC DoD Referral Management SOP)

\* TRICARE authorization not applicable (ref. TRICARE Health Plan) /

(e.g., dual eligible Veteran elects TRICARE Health Plan vs Veteran

benefit

\* Inactive Reserve and National Guard / Patients potentially enrolled

at VAMC (ref VHA Directive 1601A.02)(e.g., VAMC provides annual health

screenings or fitness for duty screenings)

\* If patient has a Veteran status and on Active Duty Orders (ref.

Active Duty Health Plan) / Includes active Reserve and National Guard

\- Federal orders must exceed 30 days

3.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 229 field values for NAME field (#.01), SHORT DESCRIPTION field (#.03) and LONG DESCRIPTION field (#.04) are modified as shown below. The plan was originally named ACTIVE DUTY AND TRICARE SHARING AGREEMENT.

NAME : TRICARE

PLAN CODE: 229 COVERAGE CODE: AC01001

SHORT DESCRIPTION:

TRI

LONG DESCRIPTION:

TRICARE Health Plan

-------------------

Patient receiving care at a VAMC as a TRICARE patient of the Department

of Defense:

\* TRICARE Authorization:

\- Required for TRICARE Prime patients - Retiree and Retiree Family

enrollees

\- NOT required for TRICARE Select patients - AD Family, Retiree,

Retiree Family and Reserve Select enrollees

\* VA/DoD Health Care Resource Sharing Agreements not applicable (ref.

VA/DoD Direct Resource Sharing Agreements)

\- (e.g., dual eligible Veteran elects Veteran benefit vs TRICARE

Health Plan)

\* If patient has a Veteran status and on Active Duty Orders, then all

Active Duty rules apply

\- Even if treatment is Service Connected - Patient considered TRICARE

Prime enrollee

\- Includes active Reserve and National Guard - Federal orders must

exceed 30 days

4.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 300, the field value for the LONG DESCRIPTION field (#.04) is modified as shown below.

NAME : VETERAN PLAN CCP RESTRICTED CARE

PLAN CODE: 300 COVERAGE CODE: CR01001

SHORT DESCRIPTION:

CCP R

LONG DESCRIPTION:

VHA Profile Veteran Plan CCP Restricted Care is assigned if one of the

following eligibilities is met:

Not enrolled Covered Veterans who are otherwise entitled to hospital

care, medical services, extended care services and community care

services; however, they are only eligible for care related to their

service connected conditions (less than 50% SC, and 0% non-compensable);

was discharged or released from active military service for a disability

incurred or aggravated in the line of duty for that disability for the

12-month period following discharge or release; Military Sexual Trauma

(MST); or Mental Health Other Than Honorable (OTH); as otherwise

documented in their record.

For COMPACT Act 2020, eligible Individuals are ones who served in the

active military service, regardless of length of service, and who were

discharged, excluding anyone who received a dishonorable discharge or was

discharged or dismissed by reason; are not enrolled in the health care

system established by section 1705 of this title; and served in the Armed

Forces for a period of more than 100 cumulative days: and was deployed in

a theater of combat operations, or while serving in the Armed Forces, was

the victim of a physical assault of a sexual nature, a battery of a

sexual nature, or sexual harassment.

5.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 226, the field value for the LONG DESCRIPTION field (#.04) is modified as shown below. The wording is corrected in the "Pending; Eligibility Unverified" bulleted item.

NAME : APPLICANT IN PROCESS PLAN CODE: 226

COVERAGE CODE: AN01001

SHORT DESCRIPTION:

INC

LONG DESCRIPTION:

Veterans who applied for VA healthcare benefits, but eligibility has not

been verified or a final enrollment determination could not be made.

. Pending; Means Test Required - Veterans whose Veterans Status has

been verified and who have not provided initial Means Test to

determine enrollment.

. Pending; Purple Heart Unconfirmed - A temporary eligibility for 14

days.

. Pending; Other - Enrollment System cannot determine enrollment

status.

. Pending; No Eligibility Code - Enrollment System cannot determine

enrollment status.

. Pending - Enrollment System cannot determine enrollment status.

. Unverified - Enrollment System cannot determine enrollment status.

. Pending; Eligibility Unverified - Veterans who do not have a prior

period of enrollment and are still within the 365-day period who

have not provided evidence of Veteran status.

For Eligible Individuals, under Veterans Comprehensive Prevention,

Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will

furnish, reimburse, pay for emergent suicide care, make referrals, as

appropriate, for care following the period of emergent suicide care.

Eligible Individuals are ones who served in the active military service,

regardless of length of service, and who were discharged, excluding

anyone who received a dishonorable discharge or was discharged or

dismissed by reason or while serving in the Armed Forces, was the victim

of a physical assault of a sexual nature, a battery of a sexual nature,

or sexual harassment.

> **NOTE:** The following VHAP modifications are for the Claims Processing and Eligibility (CP&E) project:

6.  In the HEALTH BENEFIT PLAN file (#25.11) plan code 139, VETERAN BENEFICIARY PLAN - CAMP LEJEUNE FAMILY, is replaced by the plan shown below.

NUMBER: 40 NAME : CAMP LEJEUNE FAMILY

PLAN CODE: 306 COVERAGE CODE: CL01001

SHORT DESCRIPTION:

CLF

LONG DESCRIPTION:

The Camp Lejeune Family Member Program (CLFMP) is for family members of

Veterans that lived or served at U.S. Marine Corps Base Camp Lejeune,

North Carolina, between August 1, 1953, and December 31, 1987, and were

potentially exposed to drinking water contaminated with industrial

solvents, benzene, and other chemicals.

On August 6, 2012, the Honoring America's Veterans and Caring for Camp

Lejeune Families Act of 2012 was signed into law. This law (H.R. 1627,

now Public Law 112-154) requires the Department of Veterans Affairs (VA)

to provide health care to Veterans who served on active duty at Camp

Lejeune and to reimburse eligible Camp Lejeune family members for health

care costs related to one or more of 15 specified illnesses or medical

conditions listed in the law.

For more information:

https://www.va.gov/COMMUNITYCARE/programs/dependents/CLFMP.asp

7.  Plan code 305, CHAMPVA CAREGIVER is added to the VistA HEALTH BENEFIT PLAN file (#25.11).

NUMBER: 96 NAME : CHAMPVA CAREGIVER

PLAN CODE: 305 COVERAGE CODE: CV01002

SHORT DESCRIPTION:

CHAMPVACG

LONG DESCRIPTION:

The VHA Office of Community Care (VHA OCC) is responsible for enrolling

the eligible Primary Family Caregiver into the Civilian Health and

Medical Program of the Department of Veterans Affairs (CHAMPVA) when

there is no other health insurance (OHI) coverage, to include TRICARE,

Medicare, Medicaid, commercial health plans through employment and

individual plans.

VHA Office of Community Care is also responsible for processing health

care claims for eligible Primary Family Caregivers under CHAMPVA,

processing reconsiderations, and providing customer service support to

Primary Family Caregivers for questions related to stipend payment and

CHAMPVA benefits.

For more information:

https://www.va.gov/COMMUNITYCARE/programs/caregiver/index.asp

8.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 108 field values for the NAME field (#.01), SHORT DESCRIPTION field (#.03) and LONG DESCRIPTION field (#.04) are modified as shown below. The plan was originally named BENEFICIARY CHAMPVA.

NAME : CHAMPVA STANDARD

PLAN CODE: 108 COVERAGE CODE: CV01001

SHORT DESCRIPTION:

CHAMPVA

LONG DESCRIPTION:

The Civilian Health and Medical Program of the Department of Veterans

Affairs (CHAMPVA) is a comprehensive health care program in which the VA

shares the cost of covered health care services and supplies with

eligible beneficiaries. The program is administered by the Veterans

Health Administration Office of Community Care (VHA OCC) in Denver,

Colorado.

CHAMPVA plan provides health care to dependents who may qualify for VA's

Civilian Health and Medical Program of the Department of Veteran Affairs

(CHAMPVA). They must not have eligibility under TRICARE and must be

dependents of a:

. Veteran who is rated Permanently and Totally (P&T) disabled due to a

Service-connected condition.

. Veteran who died from VA rated Service-connected condition, or who,

at the time of death, was rated Permanently and Totally disabled.

. Veteran who died on active duty and in the line of duty (not due to

misconduct).

For more information, call 1-800-733-8387 or go to:

https://www.va.gov/COMMUNITYCARE/programs/dependents/champva/index.asp

9.  In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 109, the field value for the LONG DESCRIPTION field (#.04) is modified as shown below.

NAME : BENEFICIARY SPINA BIFIDA

PLAN CODE: 109 COVERAGE CODE: SB01001

SHORT DESCRIPTION:

SB

LONG DESCRIPTION:

Spina Bifida (SB) Plan provides monetary allowances, vocational training

and rehabilitation, and VA-financed health care benefits to certain

Korean and Vietnam Veterans' birth children who have been diagnosed with

spina bifida. For the purpose of the program, spina bifida is defined

as all forms or manifestations of spina bifida (except spina bifida

occulta).

The Veterans Health Administration Office of Community Care (VHA OCC) in

Denver, CO, manages the SB Health Care Benefits Program, including

authorization of benefits and the subsequent processing and payment of

health care claims after a determination of eligibility has been made by

the Denver VA Regional Office (VARO).

For more information, call 1-888-820-1756 or go to:

https://www.va.gov/COMMUNITYCARE/programs/dependents/spinabifida/index.asp

10. In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 110, the field value for the LONG DESCRIPTION field (#.04) is modified as shown below.

NAME : BENEFICIARY CHILDREN OF WOMEN OF VIETNAM VETERANS

PLAN CODE: 110 COVERAGE CODE: CW01001

SHORT DESCRIPTION:

CWVV

LONG DESCRIPTION:

Children of Women Vietnam Veterans (CWVV) Plan provides "NEEDED CARE" to

an eligible child such health care as the Secretary determines is needed

by the child for that child's covered birth defects or any disability

that is associated with those birth defects. (38 USC 1811-1816)

For more information:

https://www.va.gov/COMMUNITYCARE/programs/dependents/cwvv/index.asp

11. In the HEALTH BENEFIT PLAN file (#25.11), VHAP plan code 122, the field value for the LONG DESCRIPTION field (#.04) is modified as shown below.

NAME : VETERAN FOREIGN MEDICAL PROGRAM PLAN CODE: 122

COVERAGE CODE: FM01001 INACTIVE: NO

SHORT DESCRIPTION:

FMP

LONG DESCRIPTION:

Foreign Medical Program Plan provides pay for medical services for

treating your service-connected disabilities, or any disability that is

associated with and aggravates a service-connected disability if you live

or travel outside the United States. This program will also reimburse you

for certain treatment of medical services while you are outside the

United States, if needed as part of your VA-approved vocational

rehabilitation program. If you are living or planning to travel outside

the U.S. (other than in the Philippines), you need to register with VA's

Foreign Medical Program office, P.O. Box 469061, Denver, CO 80246-9061,

USA: telephone 303-331-7590.

For information, visit:

https://www.va.gov/COMMUNITYCARE/programs/veterans/fmp/index.asp

SECTION 3: REGISTRATION SCREEN UPDATES

1.  At the SELF-REPORTED REGISTRATION ONLY REASON: prompt, the following new reasons are available when registering a new Veteran in Register A Patient \[DG REGISTER PATIENT\] and Enter A Request/Notification \[FBCH ENTER REQUEST\] options: 4TH MISSION, CLINICAL EVALUATION, HUD-VASH and IMMUNIZATIONS.
2.  At the SELF-REPORTED REGISTRATION ONLY REASON: prompt, the following new reasons are available when registering a new non-veteran in Register A Patient \[DG REGISTER PATIENT\] and Enter A Request/Notification \[FBCH ENTER REQUEST\] options: 4TH MISSION, HUD-VASH and IMMUNIZATIONS.
3.  At the SELF-REPORTED REGISTRATION ONLY REASON: prompt, the following new reasons are available in the Collateral Patient Register \[DG COLLATERAL PATIENT\] option: 4TH MISSION and IMMUNIZATIONS.
4.  The EMERGENCY CONTACT DATA, SCREEN \<3\> screen is updated to add the Relation Type prompts and to rename the RELATIONSHIP TO PATIENT prompts to Relation Note:

EMERGENCY CONTACT DATA, SCREEN \<3\>

DGPatient,ONE (PREFERRED NAME) MON DD,YYYY

\###-##-#### NSC VETERAN

==========================================================================

\[1\] NOK: DGNOK,ONE \[2\] NOK-2: DGNOK,TWO

Relation Type: STEPCHILD Relation Type: GRANDCHILD

Relation Note: PRIMARY NOK Relation Note: DEPLOYED

200 S ANY ST 200 S ANY ST

ANY CITY,MI \##### 211

UNITED STATES ANY CITY,MI \#####

UNITED STATES

Phone: \########## Phone: UNANSWERED

Work Phone: UNANSWERED Work Phone: UNANSWERED

\[3\] E-Cont.: DGEC,ONE \[4\] E2-Cont.: DGEC,TWO

Relation Type: STEPCHILD Relation Type: GRANDCHILD

Relation Note: LIVES OVERSEAS Relation Note: GRANDCHILD

100 S ANY ST 300 S ANY ST

100 S ANY ST 300 S ANY ST

ANY CITY,ST \##### 322

UNITED STATES ANY CITY,ST \#####

UNITED STATES

Phone: UNANSWERED Phone: UNANSWERED

Work Phone: UNANSWERED Work Phone: UNANSWERED

\[5\] Designee: DGDESIGNEE,ONE Relation Type: CHILD-IN-LAW

342 ANY ST Relation Note: POWER OF ATTORNEY

ANY CITY,ST \#####

UNITED STATES

Phone: \########## Work Phone: UNANSWERED

\<RET\> to CONTINUE, 1-5 or ALL to EDIT, ^N for screen N or '^' to QUIT:

<span id="_Toc95829180" class="anchor"></span>Figure : EMERGENCY CONTACT DATA, SCREEN \<3\>

5.  When the Emergency Contact Name is changed, the RELATION NOTE field is updated to match what is in RELATIONSHIP TYPE field:

E2-NAME OF SECONDARY CONTACT: DGEC,TWO//

E2-RELATION TYPE: GRANDCHILD// 3 DAUGHTER

\*\*The E2-RELATION NOTE field is changed from DEPLOYED to DAUGHTER\*\*

E2-RELATION NOTE: DAUGHTER//

<span id="_Toc95829181" class="anchor"></span>Figure : RELATION NOTE

6.  The DG PATIENT INQUIRY option is updated to add the "Relation Type:" and change the Emergency Contact labels to "Relation Note:"

DGPatient,ONE;(PREFERRED NAME) \###-##-#### MON DD,YYYY

==========================================================================

Emergency Contact Information:

E-Cont.: RELATED,PERSON E2-Cont.: WIFE,SECONDARY

Relation Type: NIECE/NEPHEW Relation Type: WIFE

Relation Note: OVERSEAS Relation Note: HEALTHCARE PROXY

100 S ANY ST 300 S ANY ST

322

ANY CITY, ST \##### ANY CITY, ST \#####

UNITED STATES UNITED STATES

Phone: UNSPECIFIED Phone: UNSPECIFIED

Work Phone: UNSPECIFIED Work Phone: UNSPECIFIED

VHA Profiles Currently Assigned to Veteran:

None

<span id="_Toc95829182" class="anchor"></span>Figure : DG PATIENT INQUIRY Option

SECTION 4: HL7 ZCT SEGMENT UPDATE

The HL7 VA Specific Emergency Contact Segment (ZCT) is updated with a new sequence (#11) CONTACT RELATIONSHIP TYPE.

There are five possible contacts in a patient record. Each contact has a Relationship Type field. The five Relationship Type fields for each contact are listed below. (See section 1 item 3 above for details on these five fields.)

Any contact defined in the patient record has a corresponding ZCT segment in the HL7-ORF/ORU Z07 message. Sequence \#11 contains the Relationship Type value for that contact. Refer to the IVM\*2.0\*204 patch description for information on the modifications to the Z07 message.

- K-RELATIONSHIP TYPE field (#.224)
- K2-RELATIONSHIP TYPE field (#.2104)
- E-RELATIONSHIP TYPE field (#.3309)
- E2-RELATIONSHIP TYPE field (#.331015)
- D-RELATIONSHIP TYPE field (#.34015)

SECTION 5: VADPT API & ICR MODIFICATIONS

1.  The DGRR GET PATIENT SERVICES DATA Remote Procedure Call (RPC) is modified with the addition of the field "RelationshipType" to the ContactInfo structure. This field contains, for each contact type, the corresponding relationship type field (K-RELATIONSHIP TYPE field (#.224), or K2-RELATIONSHIP TYPE field (#.2104), or E-RELATIONSHIP TYPE field (#.3309), or E2-RELATIONSHIP TYPE field (#.331015), or D-RELATIONSHIP TYPE field (#.34015)). The external value of the field is returned.
2.  The VADPT ICR#10061 is modified to add the new RELATION TYPE field to the OAD component. It replaces the RELATIONSHIP TO PATIENT in the tenth (10th) node of the output array. RELATIONSHIP TO PATIENT is moved from the 10th node to the new twelfth (12th) node of the output array. Please see the PIMS Technical Manual for details.

IVM\*2.0\*204 makes the following modification to VistA REE:

1.  VistA is updated to send a new sequence (#11) in the existing ZCT segment of the Health Level 7 (HL7) ORU/ORF-Z07 message if the current date/time is greater than or equal to the "DG PATCH DG\*5.3\*1067 ACTIVE" parameter date/time value. The new sequence (#11) transmits the following fields from the PATIENT file (#2) for each Contact Type:

\- K-RELATIONSHIP TYPE field (#.224)

\- K2-RELATIONSHIP TYPE field (#.2104)

\- E-RELATIONSHIP TYPE field (#.3309)

\- E2-RELATIONSHIP TYPE field (#.331015)

\- D-RELATIONSHIP TYPE field (#.34015)

2.  The HL7 ORU/ORF-Z05 message processing is updated to parse and store the new sequence (#11) values from the existing ZCT segment into the PATIENT file (#2). The new sequence (#11) values are stored in the corresponding fields in the PATIENT file (#2):

\- K-RELATIONSHIP TYPE field (#.224)

\- K2-RELATIONSHIP TYPE field (#.2104)

\- E-RELATIONSHIP TYPE field (#.3309)

\- E2-RELATIONSHIP TYPE field (#.331015)

\- D-RELATIONSHIP TYPE field (#.34015)

3.  The IVM DEMOGRAPHIC UPLOAD FIELDS file (#301.92) is updated with five new entries to automatically upload the relationship type code to the PATIENT file (#2):

DHCP FIELD NAME: K-RELATIONSHIP TYPE HL7 LOCATION: ZCT11K1

UPLOADABLE DEMOGRAPHIC FIELD: YES DHCP FILE: PATIENT

DHCP FIELD NUMBER: .224 TRANSFORM IVM DATA: YES

TRANSFORM DHCP DATA: YES ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.224 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.224 D LOOK^IVMPREC9

DHCP FIELD NAME: K2-RELATIONSHIP TYPE HL7 LOCATION: ZCT11K2

UPLOADABLE DEMOGRAPHIC FIELD: YES DHCP FILE: PATIENT

DHCP FIELD NUMBER: .2104 TRANSFORM IVM DATA: YES

TRANSFORM DHCP DATA: YES ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.2104 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.2104 D LOOK^IVMPREC9

DHCP FIELD NAME: E-RELATIONSHIP TYPE HL7 LOCATION: ZCT11E1

UPLOADABLE DEMOGRAPHIC FIELD: YES DHCP FILE: PATIENT

DHCP FIELD NUMBER: .3309 TRANSFORM IVM DATA: YES

TRANSFORM DHCP DATA: YES ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.3309 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.3309 D LOOK^IVMPREC9

DHCP FIELD NAME: E2-RELATIONSHIP TYPE HL7 LOCATION: ZCT11E2

UPLOADABLE DEMOGRAPHIC FIELD: YES DHCP FILE: PATIENT

DHCP FIELD NUMBER: .331015 TRANSFORM IVM DATA: YES

TRANSFORM DHCP DATA: YES ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.331015 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.331015 D LOOK^IVMPREC9

DHCP FIELD NAME: D-RELATIONSHIP TYPE HL7 LOCATION: ZCT11D1

UPLOADABLE DEMOGRAPHIC FIELD: YES DHCP FILE: PATIENT

DHCP FIELD NUMBER: .34015 TRANSFORM IVM DATA: YES

TRANSFORM DHCP DATA: YES ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.34015 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.34015 D LOOK^IVMPREC9

4.  See patch DG\*5.3\*1067 for information regarding the addition of individual triggers to flag transmission of an ORU-Z07 message to the Health Eligibility Center (HEC) when religious preference, race, or ethnicity is updated. These triggers are documented in the IVM Technical Manual.

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the defects and fixes and corresponding Jira identification numbers included in DG_53_P1067.KID.

<table>
<caption><p><span id="_Ref524346485" class="anchor"></span>Table 2: Defects and Fixes in DG_53_P1067.KID</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Jira ID</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-17777</td>
<td><p><strong>Defect</strong>: The LONG DESCRIPTION field (#.04) of the APPLICANT IN PROCESS VHAP in the HEALTH BENEFIT PLAN file (#25.11) is incorrectly worded.</p>
<p><strong>Fix</strong>: The wording "and have provided" in the description is corrected to "who have not provided" as shown below:</p>
<p>Pending; Eligibility Unverified - Veterans who do not have a prior period of enrollment and are still within the 365-day period who have not provided evidence of Veteran status.</p></td>
</tr>
<tr class="even">
<td>VES-18014</td>
<td><p><strong>Defect</strong>: The DG UAM API KEY parameter stored in the PARAMETER DEFINITION file (#8989.51) can be edited in FileMan.</p>
<p><strong>Fix</strong>: The PROHIBIT EDITING field in the DG UAM API KEY parameter stored in the PARAMETER DEFINITION file (#8989.51) is set to "Yes" to prevent a user from modifying the value stored in this parameter.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref524346485" class="anchor"></span>Table 2: Defects and Fixes in DG_53_P1067.KID

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

<u>Documentation Title</u> <u>File Name</u>

DG_53_P1067.KID Release Notes DG_5_3_P1067_RN.PDF  
User Manual Version 5.3 – Registration Menu PIMS_REG_UM.PDF  
PIMS Version 5.3 Technical Manual PIMS_TM.PDF  
IVM Version 2 Technical Manual IVM_2_TM.PDF

Refer to the Software and Documentation Retrieval Instructions section of the patch descriptions for information on obtaining the Host File DG_53_P1067.KID and related documentation.

Documentation can be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DG*5.3*850 Release Notes

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Admission Discharge Transfer (ADT) package related to the ICD-10 Follow On Class 1 Software Remediation Project contained in patch DG\*5.3\*850.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service, or dates of discharge, for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

This patch updates the Admission Discharge Transfer (ADT) package for ICD-10 remediation. Patch DG\*5.3\*850 makes the following changes to the ADT application:

- The Patient Treatment File (PTF) has been updated to allow ICD-10 Diagnosis and Procedure codes to be assigned an episode of care after the ICD-10 activation date, for the computation of the Diagnosis Related Group (DRG) and for the transmission of ICD-10 codes to the Austin Information Technology Center (AITC).
- ICD-10 Diagnosis and Procedure codes are now used to specify a Catastrophic Disability (CD) for a patient if the Date of Decision is on or after the ICD-10 activation date.
- The PTF Expanded Code List has been updated so that users can choose to view either ICD-9 or ICD-10 code sets.
- The Third Party Insurance Report has been updated to display both ICD-9 and/or ICD-10-CM/ICD-10-PCS codes.
- The Comprehensive Report by Admission and the Comprehensive Census Report have been updated to include an ICD-9 or ICD-10 indicator.
- New file fields, print templates, and routines have been added to support ICD-10 implementation.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT manuals are posted on the VistA Documentation Library (VDL) page <https://www.va.gov/vdl/>

The following ADT user manuals are updated with changes for DG\*5.3\*850:

- PIMS V. 5.3 ADT Module User Manual
- PIMS V. 5.3 ADT Module User Manual: PTF Menu

The following manual does not exist for this package:

- Security Guide

> **NOTE:** Security information is contained within the *PIMS Technical Manual*.

The following ADT documentation is present on the VDL, but does not require updates:

- ADT Outputs Menu User Manual
- Bed Control Menu User Manual
- Contract Nursing Home RUG Menu User Manual
- Copay Exemption Test Supervisor Menu User Manual
- High Risk Mental Health Patient: National Reminder and Flag Installation and Setup Guide
- Scheduling and Registration
- Means Test Supervisor Menu User Manual
- PIMS Installation Guide
- PIMS Release Notes
- PIMS Technical Manual
- PIMS User Manual – Menus, Intro & Orientation
- Registration Menu User Manual
- RUG-II Menu User Manual
- Security Officer Menu User Manual
- Supervisor ADT Menu User Manual
- Veteran ID Card Menu User Manual

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and display its description. The ADT user interface prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user.

This search method provides a "decision tree" type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes.

ICD-10-CM diagnosis code search highlights include:

- Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.
- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.
- The user is presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, the user is prompted to refine the search.
- The user can "drill down" through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

Example of ICD-10 Diagnosis Code Entry

Enter PRINCIPAL diagnosis (ICD 10): T3

9 matches found

1\. T30.- Burn and corrosion, body region unspecified (2)

2\. T31.- Burns classified accord extent body involv (55)

3\. T32.- Corrosions classified accord extent body involv

\(55\)

4\. T33.- Superficial frostbite (111)

If a user enters fewer than two characters during a DIAGNOSIS code search, the system will respond with a prompt to explain the issue and provide a resolution:

Please enter at least the first two characters of the ICD-10 code or code description to start the search.

### Sample ICD-10 Diagnostic Code PTF Record Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PTF file has been modified to prompt the user for either ICD-9 or ICD-10 data, based on whether the Discharge date or the current system date are before or after the ICD-10 activation date. PTF searches can be performed for either the ICD-9 or ICD-10 code set, but not for both during the same search.

Example of Diagnostic Code PTF Record Search with ICD-10 Codes

Admissions without an Associated PTF Record

Comprehensive Report by Admission

Diagnostic Code PTF Record Search

DRG Information Report

DRG Reports Menu ...

Inquire PTF Record

Listing of Records by Completion Status

Means Test Indicator of 'U' Report

MPCR INQUIRY

Open PTF Record Listing

Patient Summary by Admission

Pro Fee Coding Not Sent to PCE

Productivity Report by Clerk

PTF Records Transmitted with MT Indicator of U

Surgical Code PTF Record Search

Transmitted Records List

Unreleased PTF Record Output

Select PTF Output Menu Option: D

1 Diagnostic Code PTF Record Search

2 DRG Information Report

3 DRG Reports Menu

CHOOSE 1-3: 1 Diagnostic Code PTF Record Search

Select ICD Code Set (9,10): 10// ICD-10

Search by Range or Exact match: E// RANGE

Start with Diagnosis code: F10

46 matches found

1 Alcohol Abuse, Uncomplicated (ICD-10-CM F10.10)

2 Alcohol Abuse with Intoxication, Uncomplicated (ICD-10-CM F10.120)

3 Alcohol Abuse with Intoxication Delirium (ICD-10-CM F10.121)

4 Alcohol Abuse with Intoxication, unspecified (ICD-10-CM F10.129)

5 Alcohol Abuse with Alcohol-Induced Mood Disorder (ICD-10-CM F10.14)

Type "^" to STOP or Select 1-5: 1

\>\>\> ICD-10-CM Code: F10.10

Go to Diagnosis code: T53

108 matches found

1 Toxic effect of Carbon Tetrachloride, Accidental (Unintentional),

Initial Encounter (ICD-10-CM T53.0X1A)

2 Toxic effect of Carbon Tetrachloride, Accidental (Unintentional),

Subsequent Encounter (ICD-10-CM T53.0X1D)

3 Toxic effect of Carbon Tetrachloride, Accidental (Unintentional),

Sequela (ICD-10-CM T53.0X1S)

## ICD-10-PCS Procedure Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADT ICD-10 procedure code search functionality allows the end user to select a single, valid ICD-10 procedure code and display its description. The procedure code selection is based on the individual characters of ICD-10-PCS codes. The user must enter at least one character of a code. The system displays the possible values for the next digit, so the user can build the procedure code dynamically. The ADT ICD-10 procedure code search utility provides the user interface, which prompts the user for input and invokes the Lexicon utility to get data and then presents that data to the end user for selecting either a single, valid ICD-10 procedure code character or ICD-10 procedure code.

This search method provides a "decision tree" type presentation which makes use of the specific ICD-10-PCS code format and structure, where all codes consist of seven characters, with each position in the code having a specific meaning, as shown in the following table:

| Position | 1       | 2           | 3                     | 4         | 5        | 6      | 7         |
|----------|---------|-------------|-----------------------|-----------|----------|--------|-----------|
| Aspect   | Section | Body System | Root Operation / Type | Body Part | Approach | Device | Qualifier |

ICD-10-PCS procedure code search highlights include:

- This is a completely code-based search (i.e., not text-based). The user essentially "builds" the ICD-10 procedure code as they go, character by character.
- The user is presented with the list of possible values, with their descriptions, for each character (position) in the code, as they enter/select a value for each character.
- The list of options presented for each character is based on the values selected for each previous character up to that point. Initially, the user is presented with the list of possible values for character 1 (Section). Then, as the value for each character is entered/selected, the list of possible values for each subsequent character displays.
- Additional information (i.e. Definitions, Explanations, and/or Includes Examples) is provided along with the values and descriptions for each character, if applicable, to assist with the selection of the correct value.
- If part of the full ICD-10-PCS code is known, the user can enter the initial characters and the system displays the list of possible values for the subsequent character. Full code entry is also possible, if the full ICD-10-PCS code is known.
- When values for all seven characters have been entered/selected, the code and full description display for user verification. Short descriptions for the ICD-10-PCS codes display.

Example of ICD-10 Procedure Code Entry

Name: PTFPATIENT,TEST MALE SSN: 000001234 Dt of Adm: NOV 9,2014 08:00\<601-1\>

\[1\] Date of Proc: NOV 10,2014

Specialty:

\[2\] Procedures: (ICD-10-PCS)

ALTERATION OF RIGHT SHOULDER REGION WITH AUTOLOGOUS TISSUE SUBS(0X0247Z)

Enter \<RET\> to continue, 1-2 to edit,

'T' to add a Procedure Segment, '^N' for screen N, or '^' to abort: \<MAS\>//2

PROCEDURE CODE 1: 0X0247Z//

PROCEDURE CODE 2: 5a1

ICD-10 Procedure code:5A1

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 matches found for character 4.

1\. 2 Cardiac

2\. 5 Circulatory

3\. 9 Respiratory

4\. C Biliary

5\. D Urinary

Select 1-5: 2

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

Press '\*' to display available choices for next character or '^' to exit.

ICD-10 Procedure code:5A15\*

ICD-10 Procedure code:5A15

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

One code found for character 5.

2 Continuous

OK? (Yes/No) Yes// YES

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

Press '\*' to display available choices for next character or '^' to exit.

ICD-10 Procedure code:5A152\*

ICD-10 Procedure code:5A152

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

One code found for character 6.

2 Oxygenation

OK? (Yes/No) Yes// YES

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

2 - Oxygenation

Press '\*' to display available choices for next character or '^' to exit.

ICD-10 Procedure code:5A1522\*

ICD-10 Procedure code:5A1522

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

2 - Oxygenation

One code found for character 7.

3 Membrane

OK? (Yes/No) Yes// YES

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

2 - Oxygenation

3 - Membrane

Press '\*' to display available choices for next character or '^' to exit.

ICD-10 Procedure code:5A15223

ICD-10 Procedure code:5A15223

5 - Extracorporeal Assistance and Performance

A - Physiological Systems

1 - Performance

5 - Circulatory

2 - Continuous

2 - Oxygenation

3 - Membrane

EXTRACORPOREAL MEMBRANE OXYGENATION, CONTINUOUS

PROCEDURE CODE 3:

PROCEDURE CODE 4:

PROCEDURE CODE 5:

## PTF Expanded Code Listing Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *PTF Expanded Code Listing* option has been updated so that users can choose to view either ICD-9 or ICD-10 code sets.

Example of PTF Expanded Code List Prompt

099 099 Transmission

RPO Record Print-Out (RPO)

Delete PTF Record

Establish PTF Record from Past Admission

Print Special Transaction Request Log

PTF Expanded Code Listing

Purge Special Transaction Request Log

Set Transmit Flag on Movements

Validity Check of PTF Record

Select Utility Menu Option: PTF Expanded Code Listing

PTF Expanded Code List

Select ICD Code Set (9,10): 10// ICD-10

## Third Party Insurance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Third Party Insurance report has been updated to display both ICD-9 and/or ICD-10-CM/ICD-10-PCS codes.

Example of Third Party Insurance Report

Veteran Patient Insurance Information

Sort by Discharge or Admission: D// DISCHARGE

START DATE: 7 11 (JUL 11, 2011)

END DATE: t (JAN 25, 2014)

DEVICE: HOME// ;132;9999 UCX/TELNET

THIRD PARTY REIMBURSEMENT PRINTED: JAN 25,2014@13:29:25

PTFPATIENT,TEST FEMALE EMPLOYMENT STATUS: EMPLOYED FULL TIME

(PT ID: 000-00-1236) EMPLOYER: VA

111 PTF LANE OCCUPATION: COMPUTER PROGRAMMER

ANYTOWN, NEW YORK 11111

INSURANCE TYPE INSURANCE \# GROUP \# EXPIRES HOLDER

--------- ---- --------- - ----- - ------ ------

INSURER SSN 123456 SPOUSE

Admitted: AUG 1,2011@08:00 Discharged: AUG 30,2011@08:00

PTF Record not closed

DATE LOS BEDSECTION LOS DIAGNOSES (ICD-9-CM)

---- --------------- ---- --------------------

AUG 15,2011@08:00 POLYTRAUMA REHAB 14 452. (PORTAL VEIN THROMBOSIS)

389.00 (CONDUCT HEARING LOSS NOS)

330.3 (CERB DEG CHLD IN OTH DIS)

330.8 (CEREB DEGEN IN CHILD NEC)

330.9 (CEREB DEGEN IN CHILD NOS)

AUG 30,2011@08:00 CARDIAC SURGERY 15 331.0 (ALZHEIMER'S DISEASE)

---- ----------

TOTAL LOS: 29 DXLS: 428.0 (CONGEST HEART FAIL UNSPECIFIED)

SURGERY DATE SPECIALTY OP CODES (ICD-9-CM)

------------ ---------- --------------------

AUG 4,2011 CARDIAC SURGERY 02.92 (BRAIN REPAIR)

02.03 (SKULL FLAP FORMATION)

35.95 (HEART REPAIR REVISION)

AUG 8,2011 CARDIAC SURGERY 44.11 (TRANSABDOMIN GASTROSCOPY)

88.03 (ABDOMINAL WALL SINOGRAM)

THIRD PARTY REIMBURSEMENT PRINTED: JAN 25,2014@13:29:26

PTFPATIENT,TEST FEMALE EMPLOYMENT STATUS: EMPLOYED FULL TIME

(PT ID: 000-00-1236) EMPLOYER: VA

111 PTF LANE OCCUPATION: COMPUTER PROGRAMMER

ANYTOWN, NEW YORK 11111

INSURANCE TYPE INSURANCE \# GROUP \# EXPIRES HOLDER

--------- ---- --------- - ----- - ------- ------

INSURER SSN 123456 SPOUSE

Admitted: DEC 1,2011@08:00 Discharged: DEC 10,2011@08:00

PTF Record not closed

DATE LOS BEDSECTION LOS DIAGNOSES (ICD-10-CM)

---- --------------- ---- --------------------

DEC 5,2011@08:00 CARDIAC SURGERY 4 F12.150 (Cannabis abuse with psychotic disorder with delusions)

G44.221 (Chronic tension-type headache, intractable)

G71.3 (Mitochondrial myopathy, not elsewhere classified)

B42.9 (Sporotrichosis, unspecified)

G72.9 (Myopathy, unspecified)

DEC 10,2011@08:00 PSYCHIATRIC OBSE 5 I69.992 (Facial weakness following unsp cerebrovascular disease)

G44.229 (Chronic tension-type headache, not intractable)

F14.10 (Cocaine abuse, uncomplicated)

---- ----------

TOTAL LOS: 9 DXLS: S54.00XA (Injury of ulnar nerve at forearm level, unsp arm, init)

SURGERY DATE SPECIALTY OP CODES (ICD-10-PCS)

------------ ---------- --------------------

DEC 6,2011 CARDIAC SURGERY 8E0W3CZ (Robotic Assisted Procedure of Trunk Region, Perc Approach)

8E0W0CZ (Robotic Assisted Procedure of Trunk Region, Open Approach)

Patient Review Document

Review Document by Admission Range

Veteran Patient Insurance Information

Select ADT Third Party Output Menu Option:

10-10 Print

ADT Third Party Output Menu ...

AMIS Reports Menu ...

Bed Availability

Disposition Outputs Menu ...

Enrollment Reports ...

Gains and Losses (G&L) Sheet

Inconsistent Data Elements Report

Inpatient/Lodger Report Menu ...

Means Test Outputs ...

N/T Radium Treatment Pending Verification List

Pending/Open Disposition List

Print Patient Label

Scheduled Admission Statistics

Scheduled Admissions List

Treating Specialty Print

VBC Form By Admission Date

VBC Form for Specific Patient

Waiting List Output

Z07 Build Consistency Check

Select ADT Outputs Menu Option:

## ## Comprehensive Report by Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Comprehensive Report by Admission has been updated to include an ICD-9 or ICD-10 indicator for the following fields:

- DX
- Surg/Pro
- Procedure Date
- Principal Diagnosis

Example of Comprehensive Report by Admission

Admissions without an Associated PTF Record

Comprehensive Report by Admission

Diagnostic Code PTF Record Search

DRG Information Report

DRG Reports Menu ...

Inquire PTF Record

Listing of Records by Completion Status

Means Test Indicator of 'U' Report

MPCR INQUIRY

Open PTF Record Listing

Patient Summary by Admission

Pro Fee Coding Not Sent to PCE

Productivity Report by Clerk

PTF Records Transmitted with MT Indicator of U

Surgical Code PTF Record Search

Transmitted Records List

Unreleased PTF Record Output

Select PTF Output Menu Option: Comprehensive Report by Admission

\* Previous selection: PATIENT from PTFPATIENT,T to PTFPATIENT,TZ

START WITH PATIENT: PTFPATIENT,T//

GO TO PATIENT: PTFPATIENT,TZ//

START WITH ADMISSION DATE: FIRST//

START WITH STATUS: FIRST//

DEVICE: ;80;999999 UCX/TELNET

PTF RECORD JAN 20,2014 13:26 PAGE 1

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

-----------------------------------------------------------------------------

PTFPATIENT,TEST FEMALE AUG 30,2011 08:00 AUG 1,2011 08:00

000001236 13 Open

Facility: 499 Marit Stat: MARRIED

Source of Adm: SELF-WALKIN Ethnic: NS Race: BS

Source of Pay: Sex: FEMALE

Trans Facility: Date of Birth: JAN 1,1942

Admit Elig: SC LESS THAN 50% SCI: NOT APPLICABLE

Vietnam SRV: UNKNOWN State: NEW YORK

POW: YES Zip Code: 12208

POW SRV: YUGOSLAVIA CONFLICT County: ALBANY

Ion Rad Exp: NO

AO Exp/Loc: NO PROJ 112/SHAD: NO

Claims MST: UNKNOWN N/T Radium: UNKNOWN

Combat Veteran: YES End Date: DEC 31,2010

Date of Disch: AUG 30,2011 08:00 Disch Specialty: CARDIAC SURGERY

Type of Disch: REGULAR Disch Status: BED OCCUPANT

Place of Disp: Out Treat:

Means Test: SERVICE CONNECTED VA Auspices:

Receiv facil:

C&P Status: Income: \$15,000

ASIH Days: SC Percentage: 40%

Period Of Serv: OTHER OR NONE

Movement Date: AUG 15,2011 08:00 Losing Specialty: POLYTRAUMA REHAB UNIT

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

DX: (ICD-9-CM)

PORTAL VEIN THROMBOSIS (452.)

CONDUCT HEARING LOSS NOS (389.00)

CERB DEG CHLD IN OTH DIS (330.3)

CEREB DEGEN IN CHILD NEC (330.8)

CEREB DEGEN IN CHILD NOS (330.9)

TRANSFER DRG: 421 -

HEPATOBILIARY DIAGNOSTIC PROCEDURES W CC

Movement Date: AUG 30,2011 08:00 Losing Specialty: CARDIAC SURGERY

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

Discharge

DX: (ICD-9-CM)

ALZHEIMER'S DISEASE (331.0)

TRANSFER DRG: 57 -

DEGENERATIVE NERVOUS SYSTEM DISORDERS W/O MCC

Date of Surg: AUG 4,2011 Chief Surg: VA TEAM

Anesth Tech: INTRAVENOUS First Asst: STAFF, FT

Source of pay: Surg spec: CARDIAC SURGERY

Surg/pro: (ICD-9-CM)

BRAIN REPAIR (02.92)

SKULL FLAP FORMATION (02.03)

HEART REPAIR REVISION (35.95)

Date of Surg: AUG 8,2011 Chief Surg: VA TEAM

Anesth Tech: INTRAVENOUS First Asst: STAFF, FT

Source of pay: Surg spec: CARDIAC SURGERY

Surg/pro: (ICD-9-CM)

TRANSABDOMIN GASTROSCOPY (44.11)

ABDOMINAL WALL SINOGRAM (88.03)

Procedure Date: AUG 2,2011 (ICD-9-CM)

INTESTINAL INCISION NOS (45.00)

PRINCIPAL DIAGNOSIS: (ICD-9-CM)

CONGEST HEART FAIL UNSPECIFIED (428.0)

BENIGN NEOPLASM OVARY(220.)

MAL NEO PYLORIC ANTRUM(151.2)

MAL NEO CERVICAL ESOPHAG(150.0)

MAL NEO THORACIC ESOPHAG(150.1)

MAL NEO ABDOMIN ESOPHAG(150.2)

MAL NEO UPPER 3RD ESOPH(150.3)

MAL NEO LOWER 3RD ESOPH(150.5)

MAL NEO ESOPHAGUS NEC(150.8)

MAL NEO ESOPHAGUS NOS(150.9)

CEREBRAL EDEMA(348.5)

ALLERGY TO PEANUTS(V15.01)

ALLERGY TO MILK PRODUCTS(V15.02)

Effective Date: AUG 30, 2011@08:00

Diagnosis Related Group: 229 Average Length of Stay(ALOS): 7.2

Weight: 4.7745

Low Day(s): 1

High Days: 99

DRG: 229- OTHER CARDIOTHORACIC PROCEDURES W CC

1 AUG 15,2011@08:00 501 TESTWARD 1151.00 1113.00 0/ 0/ 14

421 NEU OBSERVATION POLYTRAUMA REH

2 AUG 30,2011@08:00 501 TESTWARD 1151.00 1210.00 0/ 0/ 15

57 NEU OBSERVATION CARDIAC SURGER

1-CPT Capture Date/Time: AUG 2,2011 08:00

Referring or Ordering Provider: LASTNAME,FIRSTNAME

Rendering Provider: LASTNAME, FIRSTNAME

Rendering Location: ZTEST

1 50120 EXPLORATION OF KIDNEY

Quantity: 1

-------------------- Related Diagnosis (ICD-9-CM) --------------------

331.0 ALZHEIMER'S DISEASE Treated for SC Condition: NO

304.23 COCAINE DEPEND-REMISS Treated for SC Condition: NO

542\. OTHER APPENDICITIS Treated for SC Condition: NO

098.41 GONOCOCCAL IRIDOCYCLITIS Treated for SC Condition: NO

353.8 NERV ROOT/PLEXUS DIS NEC Treated for SC Condition: NO

353.4 LUMBSACRAL ROOT LES NEC Treated for SC Condition: NO

102.0 INITIAL LESIONS YAWS Treated for SC Condition: NO

PTF RECORD JAN 20,2014 13:26 PAGE 5

PATIENT DISCHARGE DATE ADMISSION DATE

SSN PTF \# STATUS

-----------------------------------------------------------------------------

PTFPATIENT,TEST FEMALE DEC 10,2011 08:00 DEC 1,2011 08:00

000001236 14 Open

Facility: 999 Marit Stat: MARRIED

Source of Adm: SELF-WALKIN Ethnic: NS Race: BS

Source of Pay: Sex: FEMALE

Trans Facility: Date of Birth: JAN 1,1942

Admit Elig: SC LESS THAN 50% SCI: NOT APPLICABLE

Vietnam SRV: UNKNOWN State: NEW YORK

POW: YES Zip Code: 12208

POW SRV: YUGOSLAVIA CONFLICT County: ALBANY

Ion Rad Exp: NO

AO Exp/Loc: NO PROJ 112/SHAD: NO

Claims MST: UNKNOWN N/T Radium: UNKNOWN

Combat Veteran: YES End Date: DEC 31,2010

Date of Disch: DEC 10,2014 08:00 Disch Specialty: PSYCHIATRIC OBSERVATION

Type of Disch: REGULAR Disch Status: BED OCCUPANT

Place of Disp: VA MEDICAL CENTER Out Treat: NO

Means Test: SERVICE CONNECTED VA Auspices: YES

Receiv facil:

C&P Status: Income: \$15,000

ASIH Days: SC Percentage: 40%

Period Of Serv: OTHER OR NONE

Movement Date: DEC 5,2014 08:00 Losing Specialty: CARDIAC SURGERY

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

DX: (ICD-10-CM)

Cannabis abuse with psychotic disorder with delusions (F12.150)

Chronic tension-type headache, intractable (G44.221)

Mitochondrial myopathy, not elsewhere classified (G71.3)

Sporotrichosis, unspecified (B42.9)

Myopathy, unspecified (G72.9)

Movement Date: DEC 10,2014 08:00 Losing Specialty: PSYCHIATRIC OBSERVATIO

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

Discharge

DX: (ICD-10-CM)

Facial weakness following unsp cerebrovascular disease (I69.992)

Chronic tension-type headache, not intractable (G44.229)

Cocaine abuse, uncomplicated (F14.10)

TRANSFER DRG: 999 -

UNGROUPABLE

Date of Surg: DEC 6,2014 Chief Surg: VA TEAM

Anesth Tech: INTRAVENOUS First Asst: STAFF, FT

Source of pay: Surg spec: CARDIAC SURGERY

Surg/pro: (ICD-10-PCS)

Robotic Assisted Procedure of Trunk Region, Perc Approach (8E0W3CZ)

Robotic Assisted Procedure of Trunk Region, Open Approach (8E0W0CZ)

Procedure Date: DEC 4,2014 (ICD-10-PCS)

Acupuncture using Anesthesia (8E0H300)

PRINCIPAL DIAGNOSIS: (ICD-10-CM)

Injury of ulnar nerve at forearm level, unsp arm, init (S54.00XA)

Cannabis abuse with intoxication, unspecified(F12.129)

Cannabis abuse with cannabis-induced anxiety disorder(F12.180)

Cannabis abuse with psychotic disorder, unspecified(F12.159)

Gonococcal infection of anus and rectum(A54.6)

Effective Date: DEC 10, 2014@08:00

Diagnosis Related Group: 999 Average Length of Stay(ALOS): 0.0

Weight: 0.0000

Low Day(s): 0

High Days: 0

DRG: 999- UNGROUPABLE

1 DEC 5,2011@08:00 501 TESTWARD 1151.00 1210.00 0/ 0/ 4

NEU OBSERVATION CARDIAC SURGER

2 DEC 10,2011@08:00 501 TESTWARD 1151.00 1350.00 0/ 0/ 5

999 NEU OBSERVATION PSY OBSERVATIO

1-CPT Capture Date/Time: DEC 2,2014 08:00

Referring or Ordering Provider: LASTNAME, FIRSTNAME

Rendering Provider: LASTNAME, FIRSTNAME

Rendering Location: ZTEST

1 50120 EXPLORATION OF KIDNEY

Quantity: 1

-------------------- Related Diagnosis (ICD-10-PCS) --------------------

G44.219 Episodic tension-type headache, not intractable

Treated for SC Condition: YES

F12.150 Cannabis abuse with psychotic disorder with delusions

Treated for SC Condition: YES

G80.2 Spastic hemiplegic cerebral palsy

Treated for SC Condition: NO

A54.6 Gonococcal infection of anus and rectum

Treated for SC Condition: NO

B42.9 Sporotrichosis, unspecified Treated for SC Condition: NO

G40.A19 Absence epileptic syndrome, intractable, w/o stat epi

Treated for SC Condition: NO

B42.89 Other forms of sporotrichosisTreated for SC Condition: NO

D23.61 Oth benign neoplasm skin/ right upper limb, inc shoulder

Treated for SC Condition: NO

Admissions without an Associated PTF Record

Comprehensive Report by Admission

Diagnostic Code PTF Record Search

DRG Information Report

DRG Reports Menu ...

Inquire PTF Record

Listing of Records by Completion Status

Means Test Indicator of 'U' Report

MPCR INQUIRY

Open PTF Record Listing

Patient Summary by Admission

Pro Fee Coding Not Sent to PCE

Productivity Report by Clerk

PTF Records Transmitted with MT Indicator of U

Surgical Code PTF Record Search

Transmitted Records List

Unreleased PTF Record Output

Select PTF Output Menu Option:

## Comprehensive Census Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Comprehensive Census Report by Admission has been updated to include an ICD-9 or ICD-10 indicator for the following fields:

- DX
- Surg/Pro
- Procedure Date
- Principal Diagnosis

Example of Comprehensive Census Report

Other Census Outputs

Comprehensive Census Report

Productivity Report by Clerk (Census Only)

Records By Completion Status (Census Only)

Transmitted Census Records List

UnReleased Census Records Report

Select Other Census Outputs Option: Comprehensive Census Report

START WITH PATIENT: FIRST//

START WITH ADMISSION DATE: FIRST//

START WITH STATUS: FIRST//

DEVICE: ;80;99999 UCX/TELNET

CENSUS RECORD JAN 20,2011 13:25 PAGE 1

PATIENT

CENSUS DATE ADMISSION DATE

SSN PTF \# CENSUS \#

-----------------------------------------------------------------------------

STATUS: Open

PTFPATIENT,MST TWO AUG 30,2011 10:00 AUG 1,2011 08:00

000001238 15 Census Status: Open

Facility: 499 Marit Stat: SEPARATED

Source of Adm: SELF-WALKIN Ethnic: Race:

Source of Pay: Sex: MALE

Trans Facility: Date of Birth: JAN 1,1951

Admit Elig: UNKNOWN SCI:

Vietnam SRV: UNKNOWN State:

POW: UNKNOWN Zip Code:

POW SRV: County:

Ion Rad Exp: UNKNOWN

AO Exp/Loc: UNKNOWN PROJ 112/SHAD: NO

Claims MST: YES N/T Radium: UNKNOWN

Combat Veteran: NO

Census Date : AUG 30,2011 10:00 Disch Specialty: CARDIAC SURGERY

Type of Disch: REGULAR Disch Status: BED OCCUPANT

Place of Disp: Out Treat:

Means Test: SERVICE CONNECTED VA Auspices:

Receiv facil:

C&P Status: Income: \$0

ASIH Days: SC Percentage: % Transmitted: \[0%\]

Period Of Serv:

Movement Date: AUG 5,2011 09:00 Losing Specialty: PSYCHIATRIC OBSERVATIO

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

Treated for MST condition: No

DX: (ICD-9-CM)

LEUKODYSTROPHY (330.0)

WERDNIG-HOFFMANN DISEASE (335.0)

TRANSFER DRG: 999 -

UNGROUPABLE

Movement Date: AUG 30,2011 10:00 Losing Specialty: CARDIAC SURGERY

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

Discharge

PRINCIPAL DIAGNOSIS: (ICD-9-CM)

WERDNIG-HOFFMANN DISEASE (335.0)

AORTIC ATHEROSCLEROSIS(440.0)

ATHERO, NAT ART OF EXTR W/PAIN(440.22)

CENSUS RECORD JAN 20,2014 13:25 PAGE 2

PATIENT

CENSUS DATE ADMISSION DATE

SSN PTF \# CENSUS \#

-----------------------------------------------------------------------------

STATUS: Open

PTFPATIENT,MST TWO DEC 31,2011 10:00 DEC 1,2014 08:00

000001238 16 Census Status: Open

Facility: 499 Marit Stat: SEPARATED

Source of Adm: SELF-WALKIN Ethnic: Race:

Source of Pay: Sex: MALE

Trans Facility: Date of Birth: JAN 1,1951

Admit Elig: UNKNOWN SCI:

Vietnam SRV: UNKNOWN State:

POW: UNKNOWN Zip Code:

POW SRV: County:

Ion Rad Exp: UNKNOWN

AO Exp/Loc: UNKNOWN PROJ 112/SHAD: NO

Claims MST: YES N/T Radium: UNKNOWN

Combat Veteran: NO

Census Date : DEC 31,2014 10:00 Disch Specialty: CARDIAC SURGERY

Type of Disch: REGULAR Disch Status: BED OCCUPANT

Place of Disp: Out Treat:

Means Test: SERVICE CONNECTED VA Auspices:

Receiv facil:

C&P Status: Income: \$0

ASIH Days: SC Percentage: % Transmitted: \[0%\]

Period Of Serv:

Movement Date: DEC 31,2014 10:00 Losing Specialty: CARDIAC SURGERY

Leave Days: 0 Pass Days: 0

Treated for SC condition: No

Treated for MST condition: No

Discharge

DX: (ICD-10-CM)

Corrosion of internal genitourinary organs, sequela (T28.8XXS)

Frostbite with tissue necrosis of right foot, init encntr (T34.821A)

PRINCIPAL DIAGNOSIS (ICD-10-CM)

Corrosion of internal genitourinary organs, sequela (T28.8XXS)

Frostbite with tissue necrosis of right foot, sequela(T34.821S)

Gonococcal infection of anus and rectum(A54.6)

Juvenile myoclonic epilepsy, not intractable, w stat epi(G40.B01)

Expsr to rdct in atmos pressr wh surfc fr dp-watr div, sqla(W94.21XS)

Lac w fb of unsp bk wl of thorax w penet thor cavity, subs(S21.429D)

Corrosions of unspecified internal organs, subs encntr(T28.90XD)

Comprehensive Census Report

Productivity Report by Clerk (Census Only)

Records By Completion Status (Census Only)

Transmitted Census Records List

UnReleased Census Records Report

Select Other Census Outputs Option:

## Integration Control Registration (ICR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes have been made to Integration Control Registration (ICR) \#3157 to accommodate both ICD-9 and ICD-10 codes, and to include a new Data Element that contains a Present on Admission (POA) indicator for Principal Diagnosis, and the first nine Secondary Diagnoses.

Complete information is available on the Database Administrator (DBA) menu on FORUM.

## New File Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below table lists new fields that have been added to the CATASTROPHIC DISABILITY REASONS (#27.17), PTF (#45), and PTF EXPANDED CODE (#45.89) files.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>New Fields</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CATASTROPHIC DISABILITY REASONS (#27.17)</td>
<td><p>ICD VERSION (#9)</p>
<p>LONG DESCRIPTION (#10)</p></td>
</tr>
<tr class="even">
<td>PTF (#45)</td>
<td><p>POA PRINCIPAL DIAGNOSIS (#82.01) POA SECONDARY DIAGNOSIS 1 (#82.02) POA SECONDARY DIAGNOSIS 2 (#82.03) POA SECONDARY DIAGNOSIS 3 (#82.04) POA SECONDARY DIAGNOSIS 4 (#82.05) POA SECONDARY DIAGNOSIS 5 (#82.06) POA SECONDARY DIAGNOSIS 6 (#82.07) POA SECONDARY DIAGNOSIS 7 (#82.08)</p>
<p>POA SECONDARY DIAGNOSIS 8 (#82.09)</p>
<p>POA SECONDARY DIAGNOSIS 9 (#82.1)</p>
<p>POA SECONDARY DIAGNOSIS 10 (#82.11)</p>
<p>POA SECONDARY DIAGNOSIS 11 (#82.12)</p>
<p>POA SECONDARY DIAGNOSIS 12 (#82.13)</p>
<p>POA SECONDARY DIAGNOSIS 13 (#82.14)</p>
<p>Added Present On Admission (POA) in the 501 movement for each ICD diagnosis field on the ^DGPT(ptf,"M",entry,82) noded.</p>
<p>POA FOR ICD 1 (#82.01)</p>
<p>POA FOR ICD 2 (#82.02)</p>
<p>POA FOR ICD 3 (#82.03)</p>
<p>POA FOR ICD 4 (#82.04)</p>
<p>POA FOR ICD 5 (#82.05)</p>
<p>POA FOR ICD 6 (#82.06)</p>
<p>POA FOR ICD 7 (#82.07)</p>
<p>POA FOR ICD 8 (#82.08)</p>
<p>POA FOR ICD 9 (#82.09)</p>
<p>POA FOR ICD 10 (#82.1)</p></td>
</tr>
<tr class="odd">
<td>PTF EXPANDED CODE (#45.89)</td>
<td>ICD VERSION (#.05)</td>
</tr>
</tbody>
</table>

## New Associated Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below table lists new templates that have been added to the PTF file.

| Template Name | File Name/Number |
|---------------|------------------|
| DGICD-9       | PTF (#45)        |
| DGICD-10      | PTF (#45)        |

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some ADT routines were added to replace direct global reads and old Application Program Interfaces (APIs) with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible.

The following table contains a list of new routines:

| Routine Name | Function                |
|--------------|-------------------------|
| DG53C850     | Post Install            |
| DG53P850     | Pre Install             |
| DGICD        | ICD Diagnosis Lookup    |
| DGICDGT      | ICD Diagnosis Lookup    |
| DGICDL       | ICD Diagnosis Lookup    |
| DGICP        | ICD Procedure Lookup    |
| DGICPL       | ICD Procedure Lookup    |
| DGPTIC10     | ICD-10 Utility          |
| DGPTRI0      | PTF Transmission ICD-10 |
| DGPTRI1      | PTF Transmission ICD-10 |
| DGPTRI2      | PTF Transmission ICD-10 |
| DGPTRI3      | PTF Transmission ICD-10 |
| DGPTRI4      | PTF Transmission ICD-10 |

## Help for ICD-10 Code Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text (?) and extended help text (??, ???) are included for prompts related to ICD-10 codes.

When entering ?:

Enter code or "text" for more information.

When entering ??:

Enter a "free text" term or part of a term such as "femur fracture".

Or

Enter a "classification code" (ICD/CPT etc) to find the single term associated with the code.

Or

Enter a "partial code". Include the decimal when a search criterion includes 3 characters or more for code searches.

When entering ???:

Number of Code Matches

----------------------

The ICD-10 Diagnosis Code search will show the user the number of matches found, indicate if additional characters in ICD code exist, and the number of codes within the category or subcategory that are available for selection.

14 matches found

M91. - Juvenile osteochondrosis of hip and pelvis (19)

This indicates that 14 unique matches or matching groups have been found and will be displayed.

M91. - the "-" indicates that there are additional characters that specify unique ICD-10 codes available.

\(19\) Indicates that there are 19 additional ICD-10 codes in the M91 "family" that are possible selections.

### From: DG*5.3*1075 Release Notes

### Section 1: Data Dictionary Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The HUD-VASH eligibility code is added to the Medical Administration Service (MAS) ELIGIBILITY CODE (#8.1) file. This entry is provided in the build file and installed with the patch.

NUMBER: 26 NAME: HUD-VASH

CARD COLOR: RED ABBREVIATION: HUDV

VA CODE NUMBER: 13 TYPE: NON-VETERAN

PRINT NAME: HUD-VASH SELECT AS ADDITIONAL: YES

2.  The HUD-VASH eligibility code is added to the ELIGIBILITY CODE (#8) file. This entry is added to the file by the post install routine POST^DG531075P.

NAME: HUD-VASH CARD COLOR: RED

ABBREVIATION: HUDV VA CODE NUMBER: 13

TYPE: NON-VETERAN PRINT NAME: HUD-VASH

SELECT AS ADDITIONAL: YES MAS ELIGIBILITY CODE: HUD-VASH

ID FORMAT: VA STANDARD AGENCY: VA

> **NOTE:** Eligibility data is entered in ELIGIBILITY STATUS DATA, SCREEN \<7\> screen. VistA Registration options that display the ELIGIBILITY STATUS DATA, SCREEN \<7\> screen include:

> Register a Patient \[DG REGISTER PATIENT\]  
> Load/Edit Patient Data \[DG LOAD PATIENT DATA\]  
> Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]  
> View Registration Data \[DG REGISTRATION VIEW\]  
> Enter A Request/Notification \[FBCH ENTER REQUEST\]

1.  Users cannot add the new HUD-VASH eligibility in Group \[3\] at the PRIMARY ELIGIBILITY CODE prompt.
2.  The new HUD-VASH eligibility code is not available for selection by the user until the current date/time is greater than or equal to the "DG PATCH DG\*5.3\*1075 ACTIVE" parameter date/time value. See item 8 below for information on this parameter.
3.  The Help Text ("?", "??") for the PRIMARY ELIGIBILITY CODE prompt does not list HUD-VASH in the selection list.
4.  While VistA users are not prohibited from entering the new HUD-VASH eligibility code as a secondary eligibility, VES calculates eligibility and returns the authoritative eligibilities on ORU/ORF-Z11 messages.
3.  A new VHAP is added to the HEALTH BENEFIT PLAN (#25.11) file:

NUMBER: 97 NAME : HUD-VASH RESTRICTED CARE

PLAN CODE: 307 COVERAGE CODE: HUD1001

SHORT DESCRIPTION:

HUDVASH

LONG DESCRIPTION:

Veterans who are enrolled and not enrolled Veterans and former service

members can be seen for services related to their enrollment in the

Housing and Urban Development-Veterans Affairs Supportive Housing

(HUD-VASH) program. These Veterans and former service members are not

subject to copayment requirements and are exempt from copayments for

inpatient services and medications related to their HUD-VASH services.

Veterans and former service members assigned this VHAP meet one of the

following conditions:

\* Cancelled/Declined - Receive medical benefits for HUD-VASH conditions

only

\* Rejected - Receive medical benefits for HUD-VASH and SC conditions

only

\* Ineligible and SC 0% - Receive medical benefits for HUD-VASH and SC

conditions only

\* Ineligible and MST - Receive medical benefits for HUD-VASH and MST

conditions only

\* Ineligible with a bar to benefits (excluding Dishonorable, Bad Conduct

General Court Martial and Fugitive Felon Program (FFP)) - Receive

medical benefits for HUD-VASH conditions only

\* Former Service members with Other Than Honorable (OTH) discharges who

present for certain services

\* Presumptive (38 USC 1702- 38 CFR 17.109)

For eligible individuals, under Veterans Comprehensive Prevention,

Access to Care, and Treatment Act of 2020 (COMPACT), Section 201, VA will

furnish, reimburse, pay for emergent suicide care, make referrals, as

appropriate, for care following the period of emergent suicide care.

Eligible individuals are Veterans who served in the active military

service, regardless of length of service, and who were discharged,

excluding anyone who received a dishonorable discharge or was discharged

or dismissed by reason

4.  The DESCRIPTION of the RADIATION EXPOSURE INDICATED? (#.32103) field of the PATIENT (#2) file is modified as shown below.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.32103 RADIATION EXPOSURE INDICATED? .321;3 SET (Required)

WERE YOU EXPOSED TO RADIATION

'Y' FOR YES;

'N' FOR NO;

'U' FOR UNKNOWN;

INPUT TRANSFORM: S DFN=DA D SV^DGLOCK

LAST EDITED: FEB 10, 2022

HELP-PROMPT: Enter the RADIATION EXPOSURE INDICATED

associated with the enrollment priority

determination

DESCRIPTION: Enter 'Y' if the Veteran was exposed to

ionizing radiation:

2\) Nagasaki/Hiroshima - Veteran was

exposed to ionizing radiation as a POW or

while serving in Hiroshima and/or

Nagasaki, Japan from August 6, 1945

through July 1, 1946.

3\) Atmospheric Nuclear Testing - exposure

occurred at an atmospheric nuclear device

test site (e.g. the Pacific Islands, NM or

NV).

4\) H/N and Atmospheric Testing - exposure

occurred as a POW in Hiroshima or Nagasaki

AND at an atmospheric nuclear device test

site.

5\) Underground Nuclear Testing - exposure

occurred while at Longshot, Milrow, or

Cannikin underground nuclear tests at

Amchitka Island, AK prior to January 1,

1974\.

6\) Exposure at Nuclear Facility - exposure

occurred while at Department of Energy

plants at Paducah, KY, Portsmouth, OH or

the K25 area at Oak Ridge, TN for at least

250 days before February 1, 1992.

7\) Other - a method that does not fit any

of the other categories

Only Veterans exposed by methods \#2, 3 or

4 are eligible for copayment exemption or

enrollment in priority 6 based on their IR

exposure.

Enter 'N' if not exposed or 'U' if

unknown.

Once the record has been verified in VES

only VES users may enter/edit this field.

GROUP: IRD

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: ^^TRIGGER^2^.3212

1)= X ^DD(2,.32103,1,1,1.3) I X S X=DIV S

Y(2)=";"\_\$S(\$D(^DD(2,.3212,0)):\$P(^(0),U,3

),1:""),Y(1)=\$S(\$D(^DPT(D0,.321)):^(.321),

1:"") S X=\$P(\$P(Y(2),";"\_\$P(Y(1),U,12)\_":"

,2),";",1) S DIU=X K Y S X=DIV S X="" X ^D

D(2,.32103,1,1,1.4)

1.3)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)

=X S Y(1)=\$C(59)\_\$S(\$D(^DD(2,.32103,0)):\$P

(^(0),U,3),1:"") S X=\$P(\$P(Y(1),\$C(59)\_Y(0

)\_":",2),\$C(59),1)="NO"

1.4)= S DIH=\$S(\$D(^DPT(DIV(0),.321)):^(.32

1),1:""),DIV=X X "F %=0:0 Q:\$L(\$P(DIH,U,11

,99)) S DIH=DIH_U" S %=\$P(DIH,U,13,999),D

IU=\$P(DIH,U,12),^(.321)=\$P(DIH,U,1,11)\_U_D

IV\_\$S(%\]"":U\_%,1:""),DIH=2,DIG=.3212 D ^DI

CR:\$O(^DD(DIH,DIG,1,0))\>0

2)= Q

CREATE CONDITION)= \#.32103="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.3212

CROSS-REFERENCE: ^^TRIGGER^2^.32111

1)= X ^DD(2,.32103,1,2,1.3) I X S X=DIV S

Y(1)=\$S(\$D(^DPT(D0,.321)):^(.321),1:"") S

X=\$P(Y(1),U,11) S DIU=X K Y S X=DIV S X=""

X ^DD(2,.32103,1,2,1.4)

1.3)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)

=X S Y(1)=\$C(59)\_\$S(\$D(^DD(2,.32103,0)):\$P

(^(0),U,3),1:"") S X=\$P(\$P(Y(1),\$C(59)\_Y(0

)\_":",2),\$C(59),1)="NO"

1.4)= S DIH=\$S(\$D(^DPT(DIV(0),.321)):^(.32

1),1:""),DIV=X X "F %=0:0 Q:\$L(\$P(DIH,U,10

,99)) S DIH=DIH_U" S %=\$P(DIH,U,12,999),D

IU=\$P(DIH,U,11),^(.321)=\$P(DIH,U,1,10)\_U_D

IV\_\$S(%\]"":U\_%,1:""),DIH=2,DIG=.32111 D ^D

ICR:\$O(^DD(DIH,DIG,1,0))\>0

2)= Q

CREATE CONDITION)= \#.32103="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.32111

CROSS-REFERENCE: 2^AENR32103^MUMPS

1)= D AUTOUPD^DGENA2(DA)

2)= D AUTOUPD^DGENA2(DA)

3)= DO NOT DELETE

This cross-reference is used to update the

patient's current Patient Enrollment

record.

5.  The DESCRIPTION of the RADIATION EXPOSURE METHOD (#.3212) field in the PATIENT (#2) file is modified as shown below.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.3212 RADIATION EXPOSURE METHOD .321;12 SET

'2' FOR HIROSHIMA/NAGASAKI;

'3' FOR ATMOSPHERIC NUCLEAR TESTING;

'4' FOR H/N AND ATMOSPHERIC TESTING;

'5' FOR UNDERGROUND NUCLEAR TESTING;

'6' FOR EXPOSURE AT NUCLEAR FACILITY;

'7' FOR OTHER;

INPUT TRANSFORM: S DFN=DA D IR^DGLOCK Q

LAST EDITED: FEB 10, 2022

HELP-PROMPT: Select from the listing available the

method by which this patient was exposed

to ionizing radiation.

DESCRIPTION: This field represents the method by which

the exposure to ionizing radiation

occurred.

2\) Nagasaki/Hiroshima - if the Veteran was

exposed to ionizing radiation as a POW or

while serving in Hiroshima and/or

Nagasaki, Japan from August 6, 1945

through July 1, 1946.

3\) Atmospheric Nuclear Testing - if

exposure occurred at an atmospheric

nuclear device test site (e.g. the Pacific

Islands, NM or NV).

4\) H/N and Atmospheric Testing - if

exposure occurred as a POW in Hiroshima or

Nagasaki AND at an atmospheric nuclear

device test site.

5\) Underground Nuclear Testing - if

exposure occurred while at Longshot,

Milrow, or Cannikin underground nuclear

tests at Amchitka Island, AK prior to

January 1, 1974.

6\) Exposure at Nuclear Facility - if

exposure occurred while at Department of

Energy plants at Paducah, KY, Portsmouth,

OH or the K25 area at Oak Ridge, TN for at

least 250 days before February 1, 1992.

7\) Other - a method that does not fit any

of the other categories.

Only Veterans exposed by methods \#2, 3 or

4 are eligible for copayment exemption or

enrollment in priority 6 based on their IR

exposure.

Once the record has been verified in VES

only VES users may enter/edit this field.

DELETE TEST: 1,0)= S DFN=DA D IRD^DGLOCK1 I '\$D(X)

GROUP: IRD

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

TRIGGERED by the RADIATION EXPOSURE

INDICATED? field of the PATIENT File

CROSS-REFERENCE: 2^AENR3212^MUMPS

1)= D AUTOUPD^DGENA2(DA)

2)= D AUTOUPD^DGENA2(DA)

3)= DO NOT DELETE

This cross-reference is used to update the

patient's current Patient Enrollment

record.

6.  The DESCRIPTION of the AGENT ORANGE EXPOS. INDICATED? (#.32102) field in the PATIENT (#2) file is updated as shown below.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.32102 AGENT ORANGE EXPOS. INDICATED? .321;2 SET (Required)

EXPOSED TO AGENT ORANGE

'Y' FOR YES;

'N' FOR NO;

'U' FOR UNKNOWN;

INPUT TRANSFORM: S DFN=DA D SV^DGLOCK

LAST EDITED: DEC 09, 2020

HELP-PROMPT: Enter 'Y' if this patient claims exposure

to agent orange, 'N' if not, 'U' if

unknown.

DESCRIPTION: For this Veteran applicant enter 'Y' if

s/he was exposed to the chemical agent

orange, 'N' if not, or 'U' if unknown.

Exposure can be claimed by those serving

in the KOREAN DMZ between January 1, 1968

and December 31, 1969; or served in

country in Vietnam or the offshore waters

of Vietnam during Jan 9, 1962 to May 7,

1975\.

When Consistency Check \# 25 is active

(AGENT ORANGE EXPOSURE INDICATED WITHOUT

VIETNAM ERA PERIOD OF SERVICE), exposure

cannot be claimed unless the Period of

Service (#.323) field in the Patient (#2)

file is answered VIETNAM ERA, which

entails those serving in the Korean DMZ

between January 1, 1968 and December 31,

1969 or served in country in Vietnam or

the offshore waters of Vietnam during Jan

9, 1962 to May 7, 1975.

Once eligibility is verified in VES only

VES users with edit capability may

enter/edit this field.

GROUP: AO

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: ^^TRIGGER^2^.32107

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)=X

S Y(1)=\$C(59)\_\$P(\$G(^DD(2,.32102,0)),U,3)

S X=\$P(\$P(Y(1),\$C(59)\_Y(0)\_":",2),\$C(59))

="NO" I X S X=DIV S Y(1)=\$S(\$D(^DPT(D0,.32

1)):^(.321),1:"") S X=\$P(Y(1),U,7),X=X S D

IU=X K Y S X="" X ^DD(2,.32102,1,1,1.4)

1.4)= S DIH=\$G(^DPT(DIV(0),.321)),DIV=X S

\$P(^(.321),U,7)=DIV,DIH=2,DIG=.32107 D ^DI

CR

2)= Q

CREATE CONDITION)= \#.32102="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.32107

CROSS-REFERENCE: ^^TRIGGER^2^.3211

1)= X ^DD(2,.32102,1,2,1.3) I X S X=DIV S

Y(1)=\$S(\$D(^DPT(D0,.321)):^(.321),1:"") S

X=\$P(Y(1),U,10),X=X S DIU=X K Y S X="" S D

IH=\$G(^DPT(DIV(0),.321)),DIV=X S \$P(^(.321

),U,10)=DIV,DIH=2,DIG=.3211 D ^DICR

1.3)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)

=X S Y(1)=\$C(59)\_\$P(\$G(^DD(2,.32102,0)),U,

3\) S X=\$P(\$P(Y(1),\$C(59)\_Y(0)\_":",2),\$C(59

))="NO"

2)= Q

CREATE CONDITION)= \#.32102="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.3211

CROSS-REFERENCE: ^^TRIGGER^2^.32109

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)=X

S Y(1)=\$C(59)\_\$P(\$G(^DD(2,.32102,0)),U,3)

S X=\$P(\$P(Y(1),\$C(59)\_Y(0)\_":",2),\$C(59))

="NO" I X S X=DIV S Y(1)=\$S(\$D(^DPT(D0,.32

1)):^(.321),1:"") S X=\$P(Y(1),U,9),X=X S D

IU=X K Y S X="" X ^DD(2,.32102,1,3,1.4)

1.4)= S DIH=\$G(^DPT(DIV(0),.321)),DIV=X S

\$P(^(.321),U,9)=DIV,DIH=2,DIG=.32109 D ^DI

CR

2)= Q

CREATE CONDITION)= \#.32102="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.32109

CROSS-REFERENCE: 2^AENR32102^MUMPS

1)= D AUTOUPD^DGENA2(DA)

2)= D AUTOUPD^DGENA2(DA)

3)= DO NOT DELETE

This cross-reference is used to update the

patient's current Patient Enrollment

record.

CROSS-REFERENCE: ^^TRIGGER^2^.3213

1)= X ^DD(2,.32102,1,5,1.3) I X S X=DIV S

Y(1)=\$S(\$D(^DPT(D0,.321)):^(.321),1:"") S

X=\$P(Y(1),U,13),X=X S DIU=X K Y S X="" S D

IH=\$G(^DPT(DIV(0),.321)),DIV=X S \$P(^(.321

),U,13)=DIV,DIH=2,DIG=.3213 D ^DICR

1.3)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)

=X S Y(1)=\$C(59)\_\$P(\$G(^DD(2,.32102,0)),U,

3\) S X=\$P(\$P(Y(1),\$C(59)\_Y(0)\_":",2),\$C(59

),1)="NO"

2)= Q

CREATE CONDITION)= \#.32102="NO"

CREATE VALUE)= @

DELETE VALUE)= NO EFFECT

FIELD)= \#.3213

7.  The DESCRIPTION of the AGENT ORANGE EXPOSURE LOCATION (#.3213) field in the PATIENT (#2) file is updated as shown below.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.3213 AGENT ORANGE EXPOSURE LOCATION .321;13 SET (Required)

Agent Orange Exposure Location

'B' FOR BLUE WATER NAVY;

'K' FOR KOREAN DMZ;

'V' FOR VIETNAM;

'O' FOR OTHER;

LAST EDITED: DEC 29, 2020

HELP-PROMPT: Enter where the patient was exposed to

agent orange.

DESCRIPTION: For this Veteran applicant who was exposed

to agent orange (EXPOSED TO AGENT ORANGE

prompt must be answered YES) enter the

location where the exposure occurred. Once

eligibility is verified in VES only VES

users may enter/edit this field. This

field cannot be deleted as long as agent

orange exposure is indicated.

SCREEN: S DIC("S")="I \$\$CHKAOEL^DGRP6EF(Y)"

EXPLANATION: Available locations are shown.

DELETE TEST: 1,0)= S DFN=DA D AOD^DGLOCK1 I '\$D(X)

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

TRIGGERED by the AGENT ORANGE EXPOS.

INDICATED? field of the PATIENT File

CROSS-REFERENCE: 2^AENR3213^MUMPS

1)= D AUTOUPD^DGENA2(DA)

2)= D AUTOUPD^DGENA2(DA)

3)= DO NOT DELETE

This MUMPS cross-reference is used to

update the patient's current Patient

Enrollment record.

8.  A new parameter DG PATCH DG\*5.3\*1075 ACTIVE is added to the PARAMETER DEFINITION (#8989.51) file. The parameter value is a timestamp.

NAME: DG PATCH DG\*5.3\*1075 ACTIVE

DISPLAY TEXT: Active date/time for patch DG\*5.3\*1075

VALUE DATA TYPE: date/time VALUE DOMAIN: ::T

VALUE HELP: Enter the date/time when patch DG\*5.3\*1075 becomes active.

DESCRIPTION:

This parameter contains the date/time when the functionality in patch

DG\*5.3\*1075 becomes active.

PRECEDENCE: 1 ENTITY FILE: PACKAGE

An instance of this parameter is created in the PARAMETER file (#8989.5) with a timestamp value of Aug 03, 2022@1700 indicating when the new HUD-VASH eligibility code will be active. The timestamp value is set via post-install routine POST^DG531075P.

ENTITY (PKG): REGISTRATION PARAMETER: DG PATCH DG\*5.3\*1075

ACTIVE

INSTANCE: 1 VALUE: AUG 03, 2022@17:00

9.  The ELIGIBILITY (#.01) field of the PATIENT ELIGIBILITIES (#361) subfile of the PATIENT (#2) file is modified. The SCREEN logic is modified to add the routine invocation \$\$HUDCK^DGLOCK1(Y).

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2.0361,.01 ELIGIBILITY 0;1 POINTER TO ELIGIBILITY CODE FILE

(#8) (Multiply asked)

INPUT TRANSFORM: S DIC("S")="I '\$P(^(0),U,7),\$S(\$P(^(0),U,8

):1,'\$D(^DPT(D0,.36)):0,1:Y=+^(.36)),\$\$ELG

CHK^DGRPTU(D0),\$\$HUDCK^DGLOCK1(Y)" D ^DIC

K DIC S DIC=DIE,X=+Y K:Y\<0 X I \$D(X) S DIN

UM=X

LAST EDITED: MAR 25, 2022

HELP-PROMPT: Select other eligibilities to which this

patient may be entitled.

DESCRIPTION: Enter all eligibilities under which this

patient may receive care. The patients

primary eligibility as well as all other

eligibilities he is entitled to is stored

in this multiple.

TECHNICAL DESCR: Unlike previous versions of the PATIENT

file, in this version ALL the patient's

eligibilities are stored in this

multiple.

When the user enters/edits that patient's

PRIMARY ELIGIBILITY CODE, that code is

automatically stored in the multiple as

well as in the PRIMARY ELIGIBILITY CODE

field.

This change was necessary to accommodate

the VA/DOD sharing

SCREEN: S DIC("S")="I '\$P(^(0),U,7),\$S(\$P(^(0),U,8

):1,'\$D(^DPT(D0,.36)):0,1:Y=+^(.36)),\$\$ELG

CHK^DGRPTU(D0),\$\$HUDCK^DGLOCK1(Y)"

EXPLANATION: Select other eligibilities for the patient

. The primary may be selected but it must

already exist.

DELETE TEST: 1,0)= S DFN=DA(1) D EV^DGLOCK D:\$D(X) COV^

DGLOCK3(DA) I '\$D(X)!(+\$G(^DPT(DA(1),.36))

=DA) W:\$D(X) !?5,"Deleting primary eligibi

lity is not allowed"

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY

PROGRAMMER

CROSS-REFERENCE: 2.0361^B

1)= S ^DPT(DA(1),"E","B",\$E(X,1,30),DA)=""

2)= K ^DPT(DA(1),"E","B",\$E(X,1,30),DA)

CROSS-REFERENCE: 2^AEL1^MUMPS

1)= S ^DPT("AEL",DA(1),+X)=""

2)= K ^DPT("AEL",DA(1),+X) I X=\$\$FIND1^DIC

(8,"","B","COLLATERAL OF VET") D ARCHALL^D

GRP1152U(DA(1))

When an eligibility is deleted, the KILL

logic will remove the item from the "AEL"

cross reference and then check if

"COLLATERAL OF VET" eligibility is being

removed. If so, code is called to archive

all CCP entries in the COMMUNITY CARE

PROGRAM sub-file (#2.191) of the PATIENT

file (#2). The ARCHIVE (#.04) field of the

CCP entry is set to 1.

CROSS-REFERENCE: ^^TRIGGER^2.0361^.03

1)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA

,DIV(1)=D1 S Y(1)=\$S(\$D(^DPT(D0,"E",D1,0))

:^(0),1:"") S X=\$P(Y(1),U,3),X=X S DIU=X K

Y X ^DD(2.0361,.01,1,3,1.1) X ^DD(2.0361,

.01,1,3,1.4)

1.1)= S X=DIV S X="" I \$D(^DIC(8,DA,0)),\$D

(^DIC(8.2,+\$P(^(0),U,10),"LONG")) X ^("LON

G")

1.4)= S DIH=\$G(^DPT(DIV(0),"E",DIV(1),0)),

DIV=X S \$P(^(0),U,3)=DIV,DIH=2.0361,DIG=.0

3 D ^DICR

2)= K DIV S DIV=X,D0=DA(1),DIV(0)=D0,D1=DA

,DIV(1)=D1 S Y(1)=\$S(\$D(^DPT(D0,"E",D1,0))

:^(0),1:"") S X=\$P(Y(1),U,3),X=X S DIU=X K

Y S X="" S DIH=\$G(^DPT(DIV(0),"E",DIV(1),

0)),DIV=X S \$P(^(0),U,3)=DIV,DIH=2.0361,DI

G=.03 D ^DICR

CREATE VALUE)= S X="" I \$D(^DIC(8,DA,0)),\$

D(^DIC(8.2,+\$P(^(0),U,10),"LONG")) X ^("LO

NG")

DELETE VALUE)= @

FIELD)= LONG

CROSS-REFERENCE: 2^AO^MUMPS

1)= S DFN=DA(1) D EN^DGMTR K DGREQF

2)= S DFN=DA(1) D EN^DGMTR K DGREQF

This cross-reference is used to determine

whether or not a means test or co-pay test

is required.

CROSS-REFERENCE: 2^AENR01^MUMPS

1)= D AUTOUPD^DGENA2(DA(1))

2)= D AUTOUPD^DGENA2(DA(1))

3)= DO NOT DELETE

This cross-reference is used to update the

patient's current Patient Enrollment

record.

When deleting an eligibility, at the point

the kill logic of this x-ref is executed

the data still exists in the global. To

determine whether an eligibility still

exists the "B" x-ref is checked - if not

there, the eligibility is ignored.

FILES POINTED TO FIELDS

ELIGIBILITY CODE (#8) ELIGIBILITY (#.01)

10. The INPUT TRANSFORM of the NUMBER (#.01) field of the PATIENT CONTACT RELATION (#12.11) file is modified to only allow whole numbers.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

12.11,.01 NUMBER 0;1 NUMBER (Required)

INPUT TRANSFORM: K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."1N.N) X

LAST EDITED: FEB 04, 2022

HELP-PROMPT: Type a whole number between 1 and 999.

DESCRIPTION: This field contains the number of the

Patient

Contact Relation.

CROSS-REFERENCE: 12.11^B

1)= S ^DG(12.11,"B",\$E(X,1,30),DA)=""

2)= K ^DG(12.11,"B",\$E(X,1,30),DA)

This cross-reference allows the user to

lookup an entry by the NUMBER field.

### Section 2: Registration Screen Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Patient Inquiry \[DG PATIENT INQUIRY\] option displays the new HUD-VASH eligibility with Other Eligibilities: when HUD-VASH eligibility is assigned to the patient.

DGPATIENTONE,TEST ONE; \########## \###-##-### MMM, DD, YYYY

==========================================================================

Combat Vet Status: NOT ELIGIBLE End Date: 08/31/2025

COMPACT Act Status: ELIGIBLE

Primary Eligibility: HUMANITARIAN EMERGENCY (VERIFIED)

Other Eligibilities: HUD-VASH

Unemployable: NO

Permanent & Total Disabled: NO

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Type \<Enter\> to continue or '^' to exit: ^

<span id="_Toc101351258" class="anchor"></span>Figure : Patient Inquiry Option

2.  VistA Registration options that display the ELIGIBILITY STATUS DATA, SCREEN \<7\> screen include:

> Register a Patient \[DG REGISTER PATIENT\]  
> Load/Edit Patient Data \[DG LOAD PATIENT DATA\]  
> Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]  
> View Registration Data \[DG REGISTRATION VIEW\]  
> Enter a Request/Notification \[FBCH ENTER REQUEST\]

1.  Users cannot add the new HUD-VASH in Group \[3\] at the PRIMARY ELIGIBILITY CODE prompt on the ELIGIBILITY STATUS DATA, SCREEN \<7\>.
2.  The Help Text ("?", "??") for the PRIMARY ELIGIBILITY CODE prompt does not list HUD-VASH in the selection list.
3.  The FEE BASIS (FB) package also displays the ELIGIBILITY STATUS DATA, SCREEN \<7\> screen in the Enter a Request/Notification \[FBCH ENTER REQUEST\] option.
4.  The ENVIRONMENTAL FACTORS screen is updated as follows:
    1.  If the patient's eligibility has been verified by VES, the user is prevented from entering or editing data in Group \[1\] (Agent Orange Exposure) and Group \[2\] (ION Radiation Exposure). The informational message "Eligibility is Verified. Only VES users may enter/edit Agent Orange or ION Radiation Exposure." is displayed as well.

> NOTE: "Eligibility verified by VES" is defined as the ELIGIBILITY STATUS ENTERED BY (#.3616) field = POSTMASTER and the ELIGIBILITY STATUS (#.3611) field in the PATIENT (#2) file equal to "V" (VERIFIED).

DGPAIENT,ONE XXX XX, XXXX

XXX-XX-XXX NSC VETERAN

==========================================================================

\*\*\*\* ENVIRONMENTAL FACTORS \*\*\*\*

\<1\> A/O Exp.: NO Reg: Exam:

\<2\> ION Rad.: NO Reg: Method:

\[3\] SW Asia Cond: Reg: Exam:

\[4\] N/T Radium:

\<5\> Camp Lejeune:

Eligibility is Verified in VES. Only VES users may enter/edit Agent Orange

or ION Radiation Exposure.

SELECT AN ENVIRONMENTAL FACTOR (3-4) OR (Q)UIT: QUIT//

<span id="_Toc101351259" class="anchor"></span>Figure : ENVIRONMENTAL FACTORS Screen

2.  When editing ION Radiation Exposure data, the RADIATION EXPOSURE METHOD: prompt only displays if the user answered YES to Radiation Exposure Indicated?.
    1.  If the user answers YES to RADIATION EXPOSURE INDICATED? and leaves the RADIATION EXPOSURE METHOD: blank, the screen requires the user to respond. The system displays "??", the Help Prompt text, and then redisplays the prompt.

DGPATIENT,ONE XXX XX, XXXX

XXX-XX-XXXX NSC VETERAN

==========================================================================

\*\*\*\* ENVIRONMENTAL FACTORS \*\*\*\*

\[1\] A/O Exp.: NO Reg: Exam:

\[2\] ION Rad.: NO Reg: Method:

\[3\] SW Asia Cond: Reg: Exam:

\[4\] N/T Radium:

\<5\> Camp Lejeune:

SELECT AN ENVIRONMENTAL FACTOR (1-4) OR (Q)UIT: QUIT// 2 ION Rad

RADIATION EXPOSURE INDICATED?: NO// Y YES

RADIATION EXPOSURE METHOD: ??

Select from the listing available the method by which this patient was

exposed to ionizing radiation.

Choose from:

2 HIROSHIMA/NAGASAKI

3 ATMOSPHERIC NUCLEAR TESTING

4 H/N AND ATMOSPHERIC TESTING

5 UNDERGROUND NUCLEAR TESTING

6 EXPOSURE AT NUCLEAR FACILITY

7 OTHER

RADIATION EXPOSURE METHOD:

<span id="_Toc101351260" class="anchor"></span>Figure : RADIATION EXPOSURE INDICATED? Prompt

2.  If the user enters caret (^) at the RADIATION EXPOSURE METHOD: prompt, the action is aborted.
    1.  The value of the RADIATION EXPOSURE METHOD (#.3212) field is left unchanged.
    2.  If the RADIATION EXPOSURE INDICATED (#.32103) field was changed from NO to YES, it is reverted to NO.
    3.  If the RADIATION EXPOSURE INDICATED (#.32103) field was changed from UNK to YES, it is reverted to UNK.
    4.  If the RADIATION EXPOSURE INDICATED (#.32103) field was changed from NULL to YES, it is set to NO.
    5.  The user is returned to the ENVIRONMENTAL FACTORS screen.

DGPATIENT,ONE XXX XX, XXXX

XXX-XX-XXXX NSC VETERAN

==========================================================================

\*\*\*\* ENVIRONMENTAL FACTORS \*\*\*\*

\[1\] A/O Exp.: NO Reg: Exam:

\[2\] ION Rad.: NO Reg: Method:

\[3\] SW Asia Cond: Reg: Exam:

\[4\] N/T Radium:

\<5\> Camp Lejeune:

SELECT AN ENVIRONMENTAL FACTOR (1-4) OR (Q)UIT: QUIT// 2 ION Rad

RADIATION EXPOSURE INDICATED?: NO// Y YES

RADIATION EXPOSURE METHOD: ^

DGPATIENT,ONE XXX XX, XXXX

XXX-XX-XXXX NSC VETERAN

==========================================================================

\*\*\*\* ENVIRONMENTAL FACTORS \*\*\*\*

\[1\] A/O Exp.: NO Reg: Exam:

\[2\] ION Rad.: NO Reg: Method:

\[3\] SW Asia Cond: Reg: Exam:

\[4\] N/T Radium:

\<5\> Camp Lejeune:

SELECT AN ENVIRONMENTAL FACTOR (1-4) OR (Q)UIT: QUIT//

<span id="_Toc101351261" class="anchor"></span>Figure : RADIATION EXPOSURE METHOD: Prompt

2.  When editing Agent Orange Exposure data, the behavior of the AGENT ORANGE EXPOSURE LOCATION: prompt is updated if the user aborts by entering a caret (^).
    - The value stored in the AGENT ORANGE EXPOSURE LOCATION (#.321) field is left unchanged.
    - If the AGENT ORANGE EXPOS. INDICATED? (#.32102) field was changed from NO to YES, it is reverted to NO.
    - If the AGENT ORANGE EXPOS. INDICATED? (#.32102) field was changed from UNK to YES, it is reverted to UNK.
    - If the AGENT ORANGE EXPOS. INDICATED? (#.32102) field was changed from NULL to YES, it is set to NO.
    - The user is returned to the ENVIRONMENTAL FACTORS screen.
4.  The ELIGIBILITY STATUS DATA, SCREEN \<7\> screen is modified. The following prompts display a default value of "NO" if the patient is a non-Veteran and display a default value of "UNANSWERED" if the patient is a Veteran.
    1.  "Aid & Attendance:"
    2.  "Housebound:"
    3.  "VA Pension:"

ELIGIBILITY STATUS DATA, SCREEN \<7\>

DGPATIENTTWO,TWO XXX XX,XXXX

XXX-XX-XXXX NON-VETERAN (OTHER)

==========================================================================

\[1\] Patient Type: NON-VETERAN (OTHER) Veteran: NO

Svc Connected: N/A SC Percent: N/A

Rated Incomp.: UNANSWERED

Claim Number: UNANSWERED

Folder Loc.: UNANSWERED

\[2\] Aid & Attendance: NO Housebound: NO

VA Pension: NO

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED Amount: UNANSWERED

\[3\] Primary Elig Code: HUMANITARIAN EMERGENCY

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: OTHER NON-VETERAN

\[4\] Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT:

<span id="_Toc101351262" class="anchor"></span>Figure : ELIGIBILITY STATUS DATA, SCREEN \<7\>

5.  The COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION screen is modified as follows.
    1.  The following labels display a default value of "NO" if the patient is a non-Veteran and initially display "UNANSWERED" if the patient is a Veteran.
        1.  "Aid & Attendance:"
        2.  "Housebound:"
        3.  "VA Pension:"
    2.  The following prompts display a default of NO if the patient is a non-Veteran and no default value if the patient is a Veteran.
        1.  RECEIVING A&A BENEFITS?:
        2.  RECEIVING HOUSEBOUND BENEFITS?:
        3.  RECEIVING A VA PENSION?:

COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

DGPATIENTTWO,TWO; XXX-XX-XXXX NON-VETERAN (OTHER)

==========================================================================

Aid & Attendance: NO

Housebound: NO

VA Pension: NO

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?: NO// NO

RECEIVING HOUSEBOUND BENEFITS?: NO// NO

RECEIVING A VA PENSION?: NO// NO

RECEIVING VA DISABILITY?:

GI INSURANCE POLICY?:

<span id="_Toc101351263" class="anchor"></span>Figure : COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

6.  During consistency check processing the following prompts are updated.
    1.  The prompts display a default of NO if the patient is a non-Veteran and no default value if the patient is a Veteran.
        1.  RECEIVING A&A BENEFITS?:
        2.  RECEIVING HOUSEBOUND BENEFITS?
        3.  RECEIVING A VA PENSION?:
    2.  The above prompts are updated in the following options during consistency check processing:

> Preregister a Patient \[DGPRE PRE-REGISTER OPTION\]  
> Load/Edit Patient Data \[DG LOAD PATIENT DATA\]  
> Register a Patient \[DG REGISTER PATIENT\]  
> Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]  
> Edit Inconsistent Data for a Patient \[DG CONSISTENCY PATIENT\]  
> Fee Basis: Enter a Request/Notification \[FBCH ENTER REQUEST\]

DGPATIENTTWO,TWO MON DD,YYYY

\###-##-#### NON-VETERAN (OTHER)

==========================================================================

13 - POS UNSPECIFIED+ 14 - ELIG CODE UNSPECIFIED

62 - EMERGENCY CONTACT NAME MISSING 99 - CAN'T PROCESS FURTHER

Inconsistencies followed by \[+\] will prevent a Z07

DO YOU WANT TO UPDATE THESE INCONSISTENCIES NOW? Yes// (Yes)

E-NAME:

TYPE: NON-VETERAN (OTHER)//

VETERAN (Y/N)?: NO//

RECEIVING A&A BENEFITS?: NO// NO

RECEIVING HOUSEBOUND BENEFITS?: NO// NO

RECEIVING A VA PENSION?: NO// NO

POW STATUS INDICATED?: U UNKNOWN

PRIMARY ELIGIBILITY CODE:

PERIOD OF SERVICE:

Checking data for consistency...

<span id="_Toc101351264" class="anchor"></span>Figure : Check for Inconsistencies Screen

### Section 3: DG EE Summary Server Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server host and port number is updated for the DG EE SUMMARY SERVER web server. The post-install routine POST^DG531075P updates the server with the appropriate host and port number based on the type of system in which the patch is installed: Production, Pre-Production (Mirror), Software Quality Assurance (SQA) or Development.

### From: DG*5.3*1121 Release Notes

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA REE Host File DG_53_P1121.KID, which includes Registration (DG) patch DG\*5.3\*1121 and Income Verification Match (IVM) patch IVM\*2.0\*215, is being released to support enhancements for the Eligibility and Enrollment (E&E) program.

Host File DG_53_P1121.KID is also being released in support of the Veterans Health Administration (VHA) Enrollment System (VES) 6.11 release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA REE and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This multi-package build is distributed as a Host File. Refer to the Software and Documentation Retrieval Instructions section of the patch descriptions for information on obtaining the Host File DG_53_P1121.KID and related documentation.

The following sections provide a summary of the enhancements and modifications to the existing software for VistA REE with the release of patches DG\*5.3\*1121 and IVM\*2.0\*215.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new features or functions added to VistA REE for DG\*5.3\*1121 and IVM\*2.0\*215.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1121 modifies the APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\> to make the screen not editable.

Patch DG\*5.3\*1121 adds Data Dictionary TELEPHONE COUNTRY CODE file (#12.12).

Patch DG\*5.3\*1121 adds TEMPORARY COUNTRY CODE field (#.12116), COUNTRY CODE \[RESIDENCE\] field (#.1327), COUNTRY CODE \[CELLULAR\] field (#.1328), COUNTRY CODE \[WORK\] field (#.1329), and CONFIDENTIAL COUNTRY CODE field (#.13201) to the PATIENT file (#2).

Patch DG\*5.3\*1121 adds TEMPORARY EXTENSION field (#.12117), EXTENSION \[RESIDENCE\] field (#.13211), EXTENSION \[CELLULAR\] field (#.13212), EXTENSION \[WORK\] field (#.13213) and CONFIDENTIAL EXTENSION field (#.13214) to the PATIENT file (#2).

Patch DG\*5.3\*1121 adds the PERSIAN GULF INDICATOR field (#.32117) and PERSIAN GULF LAST CHANGE DATE field (#.32118) to the PATIENT file (#2).

Patch DG\*5.3\*1121 modifies the Integration Control Registration (ICR) \#10061 SVC^VADPT to return the new value PERSIAN GULF INDICATOR (#2.32117) and the PERSIAN GULF LAST CHANGE DATE (#2.32118).

Patch DG\*5.3\*1121 adds two new triggers to the PHONE NUMBER \[WORK\] field (#.132) of the PATIENT file (#2).

The ZEL segment of the Health Level 7 (HL7) ORU/ORF-Z11 message is modified. Sequences 49 and 50 are added for PERSIAN GULF INDICATOR and PERSIAN GULF LAST CHANGE DATE. The values for these sequences are stored in the PERSIAN GULF INDICATOR field (#.32117) and PERSIAN GULF LAST CHANGE DATE field (#.32118) of the PATIENT file (#2).

The ZTA segment of the HL7 ORU/ORF-Z07 message is modified. Sequence 10 is added for TEMPORARY INTERNATIONAL PHONE NUMBER. Also, the 13th sequence of the PID segment of the HL7 ORU/ORF-Z07 message is modified. Components 5 through 8 are added in Sequence 13 for COUNTRY CODE, AREA CODE, PHONE NUMBER, and EXTENSION.

Patch IVM\*2.0\*215 modifies the ZEL segment of the HL7 ORU/ORF Z11 message. Sequences 49 and 50 are added for PERSIAN GULF INDICATOR and PERSIAN GULF LAST CHANGE DATE. The values from these sequences are stored in the PERSIAN GULF INDICATOR field (#.32117) and PERSIAN GULF LAST CHANGE DATE field (#.32118) of the PATIENT file (#2).

Patch IVM\*2\*215 modifies the ZTA segment of the HL7 ORU/ORF Z05 message. Sequence 10 is added for TEMPORARY INTERNATIONAL PHONE NUMBER. Also, the 13th sequence of the PID segment of the HL7 ORU/ORF Z05 message is modified. Components 5 thru 8 are added in Sequence 13 for COUNTRY CODE, AREA CODE, PHONE NUMBER, and EXTENSION.

Patch IVM\*2.0\*215 fixes a defect with sending Confidential Address change site information in the ORU/ORF-Z07 HL7 message.

Table 1 shows the enhancements and modifications included in the DG_53_P1121.KID release as tracked in Atlassian Jira.

| Jira Epic \# | Summary                                                                      |
|--------------|------------------------------------------------------------------------------|
| VES-7052     | VistA, VES, Vet360 and Corp Display Phone Numbers 4-Digit Area Codes (VistA) |
| VES-41109    | VES Site Correlation (VistA)                                                 |
| VES-41501    | Ability to Edit All Employer details on Personal Subtab - Phase 2 (VistA)    |
| VES-45133    | PACT Act 405 Persian Gulf Deployed Cohort Identifier (VistA)                 |

Table 1: DG_53_P1121.KID Enhancements and Modifications

List of Updates

Patch DG\*5.3\*1121 makes the following enhancements to VistA REE:

<u>SECTION 1: DATA DICTIONARY UPDATES</u>

1.  DG\*5.3\*1121 adds a new Data Dictionary entry. TELEPHONE COUNTRY CODE File (#12.12) is installed and populated with 245 records containing the international dialing code, the country name, and the country's short display name.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

This file contains the list of telephone country codes using the

International Telecommunications Union (ITU) Standard. This list is

necessary to accurately store, transmit, and receive patient phone

numbers that are outside the United States.

> **NOTE:** This file is controlled by the MAS Health Eligibility Center, Member

Services. Records in this file should not be added, edited, or deleted.

Any changes to this file's structure or its records should only be done

through a national patch release. Performing local modifications would

likely cause database corruption.

POINTED TO BY: TEMPORARY COUNTRY CODE field (#.12116) of the PATIENT File

(#2)

CONFIDENTIAL COUNTRY CODE field (#.13201) of the PATIENT

File (#2)

COUNTRY CODE \[RESIDENCE\] field (#.1327) of the PATIENT

File (#2)

COUNTRY CODE \[CELLULAR\] field (#.1328) of the PATIENT File

(#2)

COUNTRY CODE \[WORK\] field (#.1329) of the PATIENT File

(#2)

CROSS

REFERENCED BY: NAME(B)

LAST MODIFIED: JUL 25,2024@14:52:54

12.12,.01 NAME 0;1 FREE TEXT (Required)

COUNTRY NAME

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<3)!'(X'?1P.E) X

MAXIMUM LENGTH: 30

LAST EDITED: JUL 22, 2024

HELP-PROMPT: Enter the country of origin for this phone

number.

DESCRIPTION: This field contains the name of the

country. This name will not appear on the

screen at data entry.

CROSS-REFERENCE: 12.12^B

1)= S ^DG(12.12,"B",\$E(X,1,30),DA)=""

2)= K ^DG(12.12,"B",\$E(X,1,30),DA)

12.12,.02 COUNTRY DIALING CODE 0;2 NUMBER (Required)

INPUT TRANSFORM: K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."1N.N) X

LAST EDITED: JUL 22, 2024

HELP-PROMPT: Enter the international dialing code.

DESCRIPTION: This value is the dialing code required to

call this country.

12.12,.03 COUNTRY DISPLAY NAME 0;3 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>12!(\$L(X)\<1) X

MAXIMUM LENGTH: 12

LAST EDITED: JUL 25, 2024

HELP-PROMPT: Enter the country display name.

DESCRIPTION: This value is the display name for the

country and is a shorter version of the

full country name. This value will

display on screen after selecting a

TELEPHONE COUNTRY CODE.

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

2.  DG\*5.3\*1121 adds 5 new fields in the PATIENT File (#2) to accommodate storing the country code.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.12116 TEMPORARY COUNTRY CODE .121;16 POINTER TO TELEPHONE COUNTRY

CODE FILE (#12.12)

LAST EDITED: JUL 22, 2024

HELP-PROMPT: Enter the country dialing code for

TEMPORARY PHONE NUMBER.

DESCRIPTION: TEMPORARY COUNTRY CODE is the

international dialing code for TEMPORARY

PHONE NUMBER, Field (#.1219) from the

PATIENT File (#2).

FILES POINTED TO FIELDS

TELEPHONE COUNTRY CODE (#12.12) TEMPORARY COUNTRY CODE (#.12116)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.1327 COUNTRY CODE \[RESIDENCE\] .132;7 POINTER TO TELEPHONE

COUNTRY CODE FILE (#12.12)

LAST EDITED: JUL 22, 2024

HELP-PROMPT: Enter the country dialing code for PHONE

NUMBER \[RESIDENCE\].

DESCRIPTION: COUNTRY CODE \[RESIDENCE\] is the

international dialing code for PHONE

NUMBER \[RESIDENCE\], Field (#.131) from the

PATIENT File (#2).

FILES POINTED TO FIELDS

TELEPHONE COUNTRY CODE (#12.12) COUNTRY CODE \[RESIDENCE\] (#.1327)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.1328 COUNTRY CODE \[CELLULAR\] .132;8 POINTER TO TELEPHONE COUNTRY

CODE FILE (#12.12)

LAST EDITED: JUL 26, 2024

HELP-PROMPT: Enter the country dialing code for PHONE

NUMBER \[CELLULAR\].

DESCRIPTION: COUNTRY CODE \[CELLULAR\] is the

international dialing code for PHONE

NUMBER \[CELLULAR\], Field (#.134) from the

PATIENT File (#2).

FILES POINTED TO FIELDS

TELEPHONE COUNTRY CODE (#12.12) COUNTRY CODE \[CELLULAR\] (#.1328)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.1329 COUNTRY CODE \[WORK\] .132;9 POINTER TO TELEPHONE COUNTRY

CODE FILE (#12.12)

LAST EDITED: JUL 22, 2024

HELP-PROMPT: Enter the country dialing code for PHONE

NUMBER \[WORK\].

DESCRIPTION: COUNTRY CODE \[WORK\] is the international

dialing code for PHONE NUMBER \[WORK\],

Field (#.132) from the PATIENT File (#2).

NOTES: TRIGGERED by the PHONE NUMBER \[WORK\]

field of the PATIENT File

FILES POINTED TO FIELDS

TELEPHONE COUNTRY CODE (#12.12) COUNTRY CODE \[WORK\] (#.1329)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.13201 CONFIDENTIAL COUNTRY CODE .132;10 POINTER TO TELEPHONE

COUNTRY CODE FILE (#12.12)

LAST EDITED: JUL 26, 2024

HELP-PROMPT: Enter the country dialing code for

CONFIDENTIAL PHONE NUMBER.

DESCRIPTION: CONFIDENTIAL COUNTRY CODE is the

international dialing code for

CONFIDENTIAL PHONE NUMBER, Field (#.1315)

from the PATIENT File (#2).

FILES POINTED TO FIELDS

TELEPHONE COUNTRY CODE (#12.12) CONFIDENTIAL COUNTRY CODE (#.13201)

3.  DG\*5.3\*1121 adds 5 new fields in the PATIENT file (#2) to accommodate storing the telephone number extensions.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.12117 TEMPORARY EXTENSION .121;17 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<1)!'(X?.N) X

MAXIMUM LENGTH: 6

LAST EDITED: AUG 29, 2024

HELP-PROMPT: Answer must be 1-6 digits in length.

DESCRIPTION: TEMPORARY EXTENSION is the telephone

extension for TEMPORARY PHONE NUMBER,

Field (#.1219) from the PATIENT File (#2).

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.13211 EXTENSION \[RESIDENCE\] .132;11 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<1)!'(X?.N) X

MAXIMUM LENGTH: 6

LAST EDITED: AUG 29, 2024

HELP-PROMPT: Answer must be 1-6 digits in length.

DESCRIPTION: EXTENSION \[RESIDENCE\] is the telephone

extension for PHONE NUMBER \[RESIDENCE\],

Field (#.131) from the PATIENT File (#2).

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.13212 EXTENSION \[CELLULAR\] .132;12 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<1)!'(X?.N) X

MAXIMUM LENGTH: 6

LAST EDITED: AUG 29, 2024

HELP-PROMPT: Answer must be 1-6 digits in length.

DESCRIPTION: EXTENSION \[CELLULAR\] is the telephone

extension for PHONE NUMBER \[CELLULAR\],

Field (#.134) from the PATIENT File (#2).

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.13213 EXTENSION \[WORK\] .132;13 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<1)!'(X?.N) X

MAXIMUM LENGTH: 6

LAST EDITED: AUG 29, 2024

HELP-PROMPT: Answer must be 1-6 digits in length.

DESCRIPTION: EXTENSION \[WORK\] is the telephone

extension for PHONE NUMBER \[WORK\] Field,

(#.132) from the PATIENT File (#2).

NOTES: TRIGGERED by the PHONE NUMBER \[WORK\]

field of the PATIENT File

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.13214 CONFIDENTIAL EXTENSION .132;14 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<1)!'(X?.N) X

MAXIMUM LENGTH: 6

LAST EDITED: AUG 29, 2024

HELP-PROMPT: Answer must be 1-6 digits in length.

DESCRIPTION: CONFIDENTIAL EXTENSION is the

telephone extension for the CONFIDENTIAL

PHONE NUMBER, Field (#.1315) from the

PATIENT File (#2).

4.  Patch DG\*5.3\*1121 adds the PERSIAN GULF INDICATOR field (#.32117) and the PERSIAN GULF LAST CHANGE DATE field (#.32118) to the PATIENT file (#2). Both fields are not editable. The PERSIAN GULF LAST CHANGE DATE field is not displayed to the user and is for internal use only.

PERSIAN GULF INDICATOR (#.32117)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.32117 PERSIAN GULF INDICATOR .321;17 SET (BOOLEAN Data Type)

LAST EDITED: AUG 19, 2024

HELP-PROMPT: If the patient indicates deployment to

the Persian Gulf, enter "YES". If the

patient indicates there was no deployment

to the Persian Gulf, enter "NO". Enter no

response if deployment is unknown.

DESCRIPTION: This field should be set to YES if the

patient deployed to the Persian Gulf, NO

if the patient did not deploy to the

Persian Gulf or left blank if it is

unknown. The Persian Gulf Indicator is

entered and maintained by the VHA

Enrollment System and shared with VistA

via HL7 messaging. The field is not

editable in VistA and is only shared so

that it may be displayed to a VistA user

along with the patient's other

Environmental Factors.

The Persian Gulf Indicator is stored

internally as 1 for YES, 0 for NO and NULL

for UNKNOWN.

TECHNICAL DESCR: The Persian Gulf Indicator is stored

internally as 1 for YES, 0 for No and NULL

for UNKNOWN. It is entered and maintained

by the VHA Enrollment System and shared

with VistA via HL7 messaging.

This field is UNEDITABLE.

WRITE AUTHORITY: ^

PERSIAN GULF LAST CHANGE DATE (#.32118)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.32118 PERSIAN GULF LAST CHANGE DATE .321;18 DATE

INPUT TRANSFORM: S %DT="E" D ^%DT S X=Y

K:3991231\<X!(2990802\>X) X

LAST EDITED: AUG 08, 2024

HELP-PROMPT: Type a date between 8/2/1999 and

12/31/2099.

DESCRIPTION: This is the date that the Persian Gulf

Indicator was last changed.

TECHNICAL DESCR: The Persian Gulf Last Change Date is a

record of when the Persian Gulf Indicator

was last changed in the system. It is

stored in the internal FileMan format.

This field is not displayed on any VistA

screens and is for internal reference

only. It is maintained by the VHA

Enrollment System and is shard with VistA

via HL7 messaging.

WRITE AUTHORITY: ^

<u>  
</u>

5.  DG\*5.3\*1121 adds two new triggers to PHONE NUMBER \[WORK\] field (#.132) of the PATIENT file (#2). These triggers delete the values in the EXTENSION \[WORK\] field (#.13213) and COUNTRY CODE \[WORK\] field (#.1329) of the PATIENT file (#2) when PHONE NUMBER \[WORK\] field is deleted.

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

--------------------------------------------------------------------------

2,.132 PHONE NUMBER \[WORK\] .13;2 FREE TEXT (audited)

OFFICE PHONE

INPUT TRANSFORM: K:\$L(X)\>20!(\$L(X)\<4) X

LAST EDITED: SEP 10, 2024

HELP-PROMPT: If employed, enter the telephone number of

this applicants place of employment \[4-20

characters\].

DESCRIPTION: Enter the office phone number \[4-20

characters\] where this applicant can be

reached while employed, if employed.

AUDIT: YES, ALWAYS

GROUP: PEMP

CROSS-REFERENCE: 2^AENR132^MUMPS

1)= D EVENT^IVMPLOG(DA)

2)= D EVENT^IVMPLOG(DA)

3)= DO NOT DELETE

This cross-reference is used to notify HEC

of changes that may affect enrollment.

CROSS-REFERENCE: ^^TRIGGER^2^.1325

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$

S(\$D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y

(1),U,5),X=X S DIU=X K Y S X=DIV S X=\$G(DU

Z\) S DIH=\$G(^DPT(DIV(0),.132)),DIV=X S \$P(

^(.132),U,5)=DIV,DIH=2,DIG=.1325 D ^DICR

2)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$

S(\$D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y

(1),U,5),X=X S DIU=X K Y S X=DIV S X=\$G(DU

Z\) S DIH=\$G(^DPT(DIV(0),.132)),DIV=X S \$P(

^(.132),U,5)=DIV,DIH=2,DIG=.1325 D ^DICR

CREATE VALUE)= S X=\$G(DUZ)

DELETE VALUE)= S X=\$G(DUZ)

FIELD)= PHONE \[WORK\] CHANGE USER

This cross-reference will record the user

who has just changed the patient's work

phone number.

CROSS-REFERENCE: ^^TRIGGER^2^.1326

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$

S(\$D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y

(1),U,6),X=X S DIU=X K Y S X=DIV S X=\$\$NOW

^XLFDT() S DIH=\$G(^DPT(DIV(0),.132)),DIV=X

S \$P(^(.132),U,6)=DIV,DIH=2,DIG=.1326 D ^

DICR

2)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(1)=\$

S(\$D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y

(1),U,6),X=X S DIU=X K Y S X=DIV S X=\$\$NOW

^XLFDT() S DIH=\$G(^DPT(DIV(0),.132)),DIV=X

S \$P(^(.132),U,6)=DIV,DIH=2,DIG=.1326 D ^

DICR

CREATE VALUE)= S X=\$\$NOW^XLFDT()

DELETE VALUE)= S X=\$\$NOW^XLFDT()

FIELD)= PHONE \[WORK\] CHANGE DT/TM

This cross reference will update the PHONE

\[WORK\] CHANGE DT/TM field with the current

date and time stamp each time this field

is changed.

CROSS-REFERENCE: ^^TRIGGER^2^.1329

1)= Q

2)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)=X

S Y(1)=\$S(\$D(^DPT(D0,.13)):^(.13),1:"") S

X=\$P(Y(1),U,2)="" I X S X=DIV S Y(1)=\$S(\$

D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y(1)

,U,9),X=X S DIU=X K Y S X="" X ^DD(2,.132,

1,4,2.4)

2.4)= S DIH=\$G(^DPT(DIV(0),.132)),DIV=X S

\$P(^(.132),U,9)=DIV,DIH=2,DIG=.1329 D ^DIC

R

CREATE VALUE)= NO EFFECT

DELETE CONDITION)= PHONE NUMBER \[WORK\]=""

DELETE VALUE)= @

FIELD)= COUNTRY CODE \[WORK\]

Trigger the deletion of COUNTRY CODE

\[WORK\] whenever this field is deleted.

CROSS-REFERENCE: ^^TRIGGER^2^.13213

1)= Q

2)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S Y(0)=X

S Y(1)=\$S(\$D(^DPT(D0,.13)):^(.13),1:"") S

X=\$P(Y(1),U,2)="" I X S X=DIV S Y(1)=\$S(\$

D(^DPT(D0,.132)):^(.132),1:"") S X=\$P(Y(1)

,U,13),X=X S DIU=X K Y S X="" X ^DD(2,.132

,1,5,2.4)

2.4)= S DIH=\$G(^DPT(DIV(0),.132)),DIV=X S

\$P(^(.132),U,13)=DIV,DIH=2,DIG=.13213 D ^D

ICR

CREATE VALUE)= NO EFFECT

DELETE CONDITION)= PHONE NUMBER \[WORK\]=""

DELETE VALUE)= @

FIELD)= EXTENSION \[WORK\]

Trigger the deletion of EXTENSION \[WORK\]

whenver this field is deleted.

CROSS-REFERENCE: 2^IVM132^MUMPS

1)= S IVMX=X,X="IVMPXFR" X ^%ZOSF("TEST")

D:\$T DPT^IVMPXFR S X=IVMX K IVMX

2)= S IVMX=X,X="IVMPXFR" X ^%ZOSF("TEST")

D:\$T DPT^IVMPXFR S X=IVMX K IVMX

This cross-reference will check the IVM

PATIENT file to see if a change to this

field will require transmission to the IVM

Center. If it does, the IVM PATIENT file

entry's TRANSMISSION STATUS will be set to

0 and the nightly background job will

transmit the updated information.

CROSS-REFERENCE: 2^AVAFC132^MUMPS

1)= I (\$T(AVAFC^VAFCDD01)'="") S VAFCF=".1

32;" D AVAFC^VAFCDD01(DA)

2)= I (\$T(AVAFC^VAFCDD01)'="") S VAFCF=".1

32;" D AVAFC^VAFCDD01(DA)

This cross reference is used to remember

that changes were made to the PATIENT file

(#2) outside of the Registration process.

Execution of this cross reference will

create an entry in the ADT/HL7 PIVOT file

(#391.71) and mark it as requiring

transmission of an HL7 ADT-A08 message.

The local variable VAFCFLG will be set to

1 if the cross reference is not executed

because the change is being made from

within the Registration process.

Execution of this cross reference can be

prevented by setting the local variable

VAFCA08 equal to 1.

The local variable VAFCF is used to

identify the field edited. This data is

stored in the FIELD(S) EDITED (#2.1) field

in the ADT/HL7 PIVOT file (#391.71).

CROSS-REFERENCE: 2^ADGRU132^MUMPS

1)= D:(\$T(ADGRU^DGRUDD01)'="") ADGRU^DGRUD

D01(DA)

2)= D:(\$T(ADGRU^DGRUDD01)'="") ADGRU^DGRUD

D01(DA)

This cross reference is used to remember

that changes were made to a monitored data

field in the PATIENT File (#2) required

for a vendor RAI/MDS COTS system.

Execution of this cross reference will

create an entry in the ADT/HL7 PIVOT file

(#391.71) and mark it as requiring

transmission of an HL7 demographic A08

update message to the COTS interface.

The local variable DGRUGA08 will be set to

1 if the cross reference is not to be

executed as part of a re-indexing.

<u>SECTION 2: REGISTRATION SCREEN UPDATES</u>

1.  Editing is no longer allowed on the APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\> screen:

APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\>

DGPATIENT,ONE MMM DD,YYYY

\###-##-#### NSC VETERAN

==========================================================================

\<1\> Employer: ANY EMPLOYER I \<2\> Spouse's: ANY EMPLOYER II

111 ANY STREET 333 ANY STREET

ANN ARBOR,MI 48104 ANN ARBOR,MI 48104

Phone: 555-222-1111 Phone: 555-222-3333

Occupation: SECRETARY Occupation: SOFTWARE ENGINEER

\<RET\> to CONTINUE, ^N for screen N or '^' to QUIT:

Figure 1: APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\>

2.  The Persian Gulf Data Group \<7\> is added as an uneditable field to the ENVIRONMENTAL FACTORS screen of the Environmental Factors Data Group \<3\> on the MILITARY SERVICE DATA SCREEN \<6\>. This field displays the PERSIAN GULF INDICATOR field (#.32117) of the PATIENT file (#2). If the field has no value, the default value of "UNKNOWN" is displayed.

DGPATIENT,ONE MMM DD, YYYY

\###-##-#### NSC VETERAN

==========================================================================

\*\*\*\* ENVIRONMENTAL FACTORS \*\*\*\*

\<1\> A/O Exp.: Reg: Exam:

\<2\> ION Rad.: Reg: Method:

\[3\] SW Asia Cond: NO Reg: Exam:

\[4\] N/T Radium:

\<5\> Camp Lejeune:

\<6\> TERA: NO

\<7\> Persian Gulf: UNKNOWN

Only VES users may enter/edit Agent Orange, ION Radiation Exposure,

Toxic Exposure Risk Activity (TERA), or Persian Gulf.

SELECT AN ENVIRONMENTAL FACTOR (3-4) OR (Q)UIT: QUIT//

Figure 2: ENVIRONMENTAL FACTORS Screen

<u>  
</u><u>SECTION 3: HL7 ORU/ORF-Z11 PROCESSING</u>

The fields below are added to the ZEL segment in the ORU/ORF Z11 HL7 message received from VES. The data from these fields is stored in the PERSIAN GULF DEPLOYMENT COHORT field (#.32117) and PERSIAN GULF LAST CHANGE DATE field (#.32118) of the PATIENT file (#2).

SEQ FIELD

--- -----

49 PERSIAN GULF INDICATOR

50 PERSIAN GULF LAST CHANGE DATE

<u>SECTION 4: HL7 ORU/ORF-Z07 PROCESSING</u>

1.  The field below is added to the ZTA segment in the ORU/ORF-Z07 HL7 message. The data from the TEMPORARY COUNTRY CODE field (#.12116), TEMPORARY PHONE NUMBER field (#.1219), the TEMPORARY EXTENSION field (#.12117) of the PATIENT file (#2) is populated in the TEMPORARY ADDRESS INTERNATIONAL PHONE (Seq 10) of the ZTA segment of ORU/ORF-Z07 in the format of COUNTRY CODE~AREA CODE~PHONE NUMBER ~EXTENSION.

SEQ FIELD

--- -----

10 TEMPORARY ADDRESS INTERNATIONAL PHONE

(COUNTRY CODE~AREA CODE~PHONE NUMBER~EXTENSION)

2.  The 13th sequence of the PID segment in the ORU/ORF-Z07 HL7 message is modified to include components 5 through 8 to accommodate international phone numbers. These component values are retrieved from the PATIENT file (#2) and populated in Sequence 13 of the PID segment in the ORU/ORF-Z07 message. Below is the list of the 13th sequence components and their corresponding PATIENT file (#2) fields.

CATEGORY COMPONENT PATIENT file (#2) field

Confidential Country Code CONFIDENTIAL COUNTRY CODE field (#.13201)

Phone Area Code CONFIDENTIAL PHONE NUMBER field (#.1315)

Phone Number CONFIDENTIAL PHONE NUMBER field (#.1315)

Extension CONFIDENTIAL EXTENSION field (#.13214)

Residential Country Code COUNTRY CODE \[RESIDENCE\] field (#.1327)

Phone Area Code PHONE NUMBER \[RESIDENCE\] field (#.131)

Phone Number PHONE NUMBER \[RESIDENCE\] field (#.131)

Extension EXTENSION \[RESIDENCE\] field (#.13211)

Cellular Country Code COUNTRY CODE \[CELLULAR\] field (#.1328)

Phone Area Code PHONE NUMBER \[CELLULAR\] field (#.134)

Phone Number PHONE NUMBER \[CELLULAR\] field (#.134)

Extension EXTENSION \[CELLULAR\] field (#.13212)

Work Phone Country Code COUNTRY CODE \[WORK\] field (#.1329)

Area Code PHONE NUMBER \[WORK\] field (#.132)

Phone Number PHONE NUMBER \[WORK\] field (#.132)

Extension EXTENSION \[WORK\] field (#.13213)

<u>SECTION 5: VADPT API & ICR MODIFICATIONS</u>

In support of external systems requiring access to the new PERSIAN GULF INDICATOR field (#.32117) and the PERSIAN GULF LAST CHANGE DATE field (#.32118) of the PATIENT file (#2), patch DG\*5.3\*1121 modifies the supported Integration Control Registration (ICR) \#10061 for the Service data Application Programming Interface (API) in SVC^VADPT. The new PERSIAN GULF INDICATOR field (#.32117) is accessible in the (16) node of the array created by SVC^VADPT. The format of this field will be the internal and external values separated by a "^" character. The data in node 16 will be either "1^YES", "0^NO", or NULL. For example: VASV(16)="1^YES". The new PERSIAN GULF LAST CHANGE DATE field (#.32118) is accessible in the (17) node of the array created by SVC^VADPT, The format of the data will be null if there has been no change to the PERSIAN GULF INDICATOR with the internal and external values separated by a "^". For example: VASV(17)="3230629^JUN 29,2023"

The optional input variable VAHOW can be set to return the data in alpha subscripts. The PERSIAN GULF INDICATOR is returned in the "PGI" subscript. For example: VASV("PGI")="0^NO". The PERSIAN GULF LAST CHANGE DATE is returned in the "LCD" subscript. For example: VASV("LCD")="3230629^JUN 29,2023"

> **NOTE:** For additional information on the SVC^VAPDT API, see the Patient Information Management System (PIMS) Technical Manual located on the Veterans Affairs (VA) Software Document Library.

Patch IVM\*2.0\*215 makes the following modifications to VistA REE:

<u>SECTION 1: HL7 ORU/ORF-Z11 PROCESSING</u>

The fields below are added to the ZEL segment in the ORU/ORF Z11 HL7 message received from VES. The data from these fields are stored in the PERSIAN GULF INDICATOR field (#.32117) and PERSIAN GULF LAST CHANGE DATE field (#.32118) of the PATIENT file (#2).

SEQ FIELD

--- -----

49 PERSIAN GULF INDICATOR

50 PERSIAN GULF LAST CHANGE DATE

<u>  
</u><u>SECTION 2: HL7 ORU/ORF-Z05 PROCESSING</u>

1.  The field below is added to the ZTA segment in the ORU/ORF Z05 HL7 message received from VES. The data from this field are parsed and COUNTRY CODE is stored in the TEMPORARY COUNTRY CODE field (#.12116), AREA CODE and PHONE NUMBER are stored in the TEMPORARY PHONE NUMBER field (#.1219), and EXTENSION is stored in the TEMPORARY EXTENSION field (#.12117) of the PATIENT file (#2).

SEQ FIELD

--- -----

10 TEMPORARY ADDRESS INTERNATIONAL PHONE

(COUNTRY CODE~AREA CODE~PHONE NUMBER~EXTENSION)

2.  The 13th sequence of the PID segment in the ORU/ORF Z05 HL7 message is modified to include components 5 through 8 to accommodate international phone numbers. These components are parsed and stored in the below fields of the PATIENT file (#2).

CATEGORY COMPONENT PATIENT file (#2) field

-------- --------- -----------------------

Confidential Country Code CONFIDENTIAL COUNTRY CODE field (#.13201)

Phone Area Code CONFIDENTIAL PHONE NUMBER field (#.1315)

Phone Number CONFIDENTIAL PHONE NUMBER field (#.1315)

Extension CONFIDENTIAL EXTENSION field (#.13214)

Residential Country Code COUNTRY CODE \[RESIDENCE\] field (#.1327)

Phone Area Code PHONE NUMBER \[RESIDENCE\] field (#.131)

Phone Number PHONE NUMBER \[RESIDENCE\] field (#.131)

Extension EXTENSION \[RESIDENCE\] field (#.13211)

Cellular Country Code COUNTRY CODE \[CELLULAR\] field (#.1328)

Phone Area Code PHONE NUMBER \[CELLULAR\] field (#.134)

Phone Number PHONE NUMBER \[CELLULAR\] field (#.134)

Extension EXTENSION \[CELLULAR\] field (#.13212)

Work Phone Country Code COUNTRY CODE \[WORK\] field (#.1329)

Area Code PHONE NUMBER \[WORK\] field (#.132)

Phone Number PHONE NUMBER \[WORK\] field (#.132)

Extension EXTENSION \[WORK\] field (#.13213)

<u>  
</u><u>SECTION 3: Add Records in IVM DEMOGRAPHIC UPLOAD FIELDS File (#301.92)</u>

Patch IVM\*2\*215 adds three new records to the IVM DEMOGRAPHIC UPLOAD FIELDS file (#301.92). New records will contain the following data:

NUMBER: 232 DHCP FIELD NAME: TEMPORARY COUNTRY CODE

HL7 LOCATION: ZTA101 UPLOADABLE DEMOGRAPHIC FIELD: YES

DHCP FILE: PATIENT DHCP FIELD NUMBER: .12116

ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.12116 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.12116 D LOOK^IVMPREC9

NUMBER: 233 DHCP FIELD NAME: TEMPORARY TELEPHONE

HL7 LOCATION: ZTA102 UPLOADABLE DEMOGRAPHIC FIELD: YES

DHCP FILE: PATIENT DHCP FIELD NUMBER: .1219

TRANSFORM IVM DATA: NO ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.1219 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.1219 D LOOK^IVMPREC9

NUMBER: 234 DHCP FIELD NAME: TEMPORARY EXTENSION

HL7 LOCATION: ZTA104 UPLOADABLE DEMOGRAPHIC FIELD: YES

DHCP FILE: PATIENT DHCP FIELD NUMBER: .12117

ADDRESS FIELD?: NO

DHCP LOCATION LOGIC: S DR=.12117 D LOOK^IVMPREC9

DHCP OUTPUT LOGIC: S DR=.12117 D LOOK^IVMPREC9

### Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the defects and fixes and corresponding Jira identification numbers included in DG_53_P1121.KID.

<table>
<caption><p>Table 2: Defects and Fixes in DG_53_P1121.KID</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Jira ID</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-44003</td>
<td><p><strong>Defect</strong>: Currently, VistA transmits the CONFIDENTIAL ADDRESS CHANGE USER field (#.14118) in the PATIENT file (#2) value in the RF1 segment of the ORU/ORF-Z07 HL7 message for change site to VES.</p>
<p><strong>Fix</strong>: IVM*2.0*215 updates VistA to transmit the CONFIDENTIAL ADDR CHANGE SITE field (#.14113) in the PATIENT file (#2) value in the RF1 segment of the ORU/ORF-Z07 HL7 message.</p></td>
</tr>
</tbody>
</table>

Table 2: Defects and Fixes in DG_53_P1121.KID

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

### From: DG*5.3*941 Release Notes

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the installation of patch DG\*5.3\*941, a new address type of Residential Address can be viewed, added or updated in VistA REE. This address is used by Enrollment and Eligibility to retain the geographic residence of an applicant or patient. It supports the ESCC program's need to determine geographic distance from a treatment facility. A Residential Address street address cannot include a P.O. Box. A new field "Coding Accuracy Support System (CASS) Certified" was added to all address types to store whether postal addresses meet United States Postal Service (USPS) format standards. The CASS Certified field will not be displayed or shared in Address Application Programming Interfaces (APIs). The Residential Address is available for viewing in other VistA packages via Integration Control Registration (ICR) 2041 and 10037. This patch also includes a Health Benefit Plan name change.

VistA can receive from the Enrollment System a new value for the Change Source associated with the Residential Address, Permanent Address, Residential Phone Number, Cellular Phone Number and Email Address. The new value is "VET360" and VistA will accept and store it in the corresponding PATIENT file (#2) field. The value of "VET360" refers to a central repository for patient contact information, which is also used for address validation.

A defect was resolved by revising address type labels on the Patient Address Update \[DG ADDRESS UPDATE\] Option to be consistent with the changes made with Patch DG\*5.3\*925.

Patch IVM\*2.0\*164 modifies the VistA Health Level 7 (HL7) messaging.

VistA Registration will send and receive a new address type of Residential Address to and from the Enrollment System (ES). This address is used by Enrollment and Eligibility to retain the geographic residence of an applicant or patient. It supports the ESCC program's need to determine geographic distance from a treatment facility.

For each address type, VistA Registration will also send and receive the new "Coding Accuracy Support System (CASS) Certified" data element, which is used to indicate whether or not the format of the address was verified by third party software.

The Income Verification Match (IVM) Demographic Upload Utility will include the Permanent Mailing Address CASS Certified field.

Patch EAS\*1.0\*151 enhances the VistA screen available from menu option View Patient Address \[EAS VIEW PATIENT ADDRESS\].

A new address type of Residential Address can be viewed. This address is used by Enrollment and Eligibility to retain the geographic residence of an applicant or patient. It supports the ESCC program's need to determine geographic distance from a treatment facility. In addition, the screen labels and prompts are modified.

Enhancements and modifications are tracked in Rational Requirements Management (RM) and Change and Configuration Management (CM) as follows:

RM \# 788099 – Add and/or Edit Residential Address in VistA for the following menu options:

> Load/Edit Patient Data \[DG LOAD PATIENT DATA\]

> Patient Inquiry \[DG PATIENT INQUIRY\]

> Preregister A Patient \[DGPRE PRE-REGISTER OPTION\]

> Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]

> View Registration Data \[DG REGISTRATION VIEW\]

> Register A Patient \[DG REGISTER PATIENT\]

> Admit A Patient \[DG ADMIT PATIENT\]

RM \# 788101 – Real Time Validation of the Addresses in VistA. The validation and consistency rules are consistent with those used for the Permanent Mailing Address in VistA.

RM \# 788103 – Determine Non-Residential Address in VistA by validating if the Residential Address violates the defined Non-Residential Address rules.

RM \# 788126 – Communicate Address Changes to VistA Sites: The PATIENT file (#2) includes a new address type of Residential Address and a new CASS Certified field was added for Residential Address (RESIDENTIAL ADDR CASS IND field .1159), Confidential Mailing (CONFIDENTIAL ADDR CASS IND field .14117), Temporary Mailing (TEMPORARY ADDR CASS IND field .12115) and Permanent Mailing (STREET ADDRESS CASS IND field .1118) address types.

RM \# 933596 – CR 584192 Modify Health Benefit Plan Name - In the HEALTH BENEFIT PLAN file (#25.11) the name of a Health Benefit Plan (HBP) is corrected. "Veteran Plan - VC Unusual and Excessive Burden" is changed to "Veteran Plan - VC Unusual or Excessive Burden."

RM \# 949766 – Maintain VistA by incorporating the following change: In the HEALTH BENEFIT PLAN file (#25.11) the name of a Health Benefit Plan (HBP) is corrected. "Veteran Plan - VC Unusual and Excessive Burden" is changed to "Veteran Plan - VC Unusual or Excessive Burden."

CM \# 840104 – During testing a defect was found in which Add/Update Confidential Address from Vista Site1 did not display the correct county name/code in Vista Site2 for County Name = Fairfax and Code = 059. The defect was resolved in version 17 of the IVM\*2.0\*164 patch, which modifies the code to separate the Confidential Address state pointer from the Residential Address state pointer.

List of Updates

### DG\*5.3\*941

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Part 1: New Address Type of Residential

1.  The PATIENT file (#2) includes a new address type of Residential Address consisting of the following fields:
    1.  CASS Certified (system-generated and not displayed)

> RESIDENTIAL ADDR CASS IND

2.  Country

> RESIDENTIAL COUNTRY

3.  Address Line 1

> RESIDENTIAL ADDRESS \[LINE 1\]

4.  Address Line 2

> RESIDENTIAL ADDRESS \[LINE 2\]

5.  Address Line 3

> RESIDENTIAL ADDRESS \[LINE 3\]

6.  Zip Code (4-Digit Extension)

> RESIDENTIAL ZIP+4

7.  City

> RESIDENTIAL CITY

8.  State

> RESIDENTIAL STATE

9.  County

> RESIDENTIAL COUNTY

10. Postal Code

> RESIDENTIAL POSTAL CODE

11. Province

> RESIDENTIAL PROVINCE

12. Source of Change

> RESIDENTIAL ADDR CHANGE SOURCE

13. Site of Change

> RESIDENTIAL ADDR CHANGE SITE

14. Last Update (system-generated, view only)

> RESIDENTIAL ADDR CHANGE DT/TM

2.  The following menu options incorporate the Address changes listed below:

Load/Edit Patient Data \[DG LOAD PATIENT DATA\]

Patient Inquiry \[DG PATIENT INQUIRY\]

Preregister A Patient \[DGPRE PRE-REGISTER OPTION\]

Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]

View Registration Data \[DG REGISTRATION VIEW\]

Register A Patient \[DG REGISTER PATIENT\]

Admit A Patient \[DG ADMIT PATIENT\]

3.  Validation and consistency rules are consistent with those used for the Permanent Mailing Address unless specified herein.
4.  When creating or modifying the Residential Address, the fields and prompts are as shown.
    1.  Country - Required. Defaults to UNITED STATES. Selection limited to the list of countries from the COUNTRY CODE file (#779.004). For an existing address, the Country on-file is displayed.
    2.  Address Line 1 – Optional, but required for saving. Free Text 3-35 characters.
    3.  Address Line 2 - Optional. Free Text 3-30 characters.
    4.  Address Line 3 - Optional. Free Text 3-30 characters.
5.  VistA uses the selected Country to determine the following fields presented to the user.
    1.  If Country = UNITED STATES:
        1.  Zip Code – Optional, but required for saving. Selection must be a valid zip code from ZIP CODE file (#5.11). Once a Zip Code is entered, the State and County will be populated automatically.
        2.  City – Optional, but required for saving. Selection is derived from the zip code and user may be presented with more than one choice.
    2.  If Country is not UNITED STATES:
        1.  City – Optional, but required for saving. Free Text 2-15 characters.
        2.  Province - Optional. Free Text 1-20 characters.
        3.  Postal Code - Optional. Free Text 1-10 characters.
6.  VistA then prompts for the two phone number fields below.
    1.  Phone Number \[RESIDENCE\] - Optional. Free Text 4-20 characters.
    2.  Phone Number \[WORK\] - Optional. Free Text 4-20 characters.
7.  VistA then prompts for confirmation to save the changes to the Address fields. The previous residential address fields are displayed along with the updated fields.

![](dg-5-3-941-release-notes/002.png)

<span id="_Toc531616765" class="anchor"></span>Figure 1: DG\*5.3\*941 Updates to Address Change Confirmation Prompts

8.  If the user answers "N", the changes are discarded.
9.  If the user answers "Y", VistA validates the address entered. If the address passes validation, the changes are saved. If the validation fails, VistA rejects the changes, informs the user, and presents the user with a message indicating the validation failure. The validation consists of two steps.
    1.  The following fields are required and may not be empty.
        1.  Address Line 1
        2.  City
        3.  State (for domestic address only)
        4.  Zip Code (for domestic address only)
    2.  The address must be a valid residential address. See Section 4.2.1.2 Part 2: Determine Non-Residential Address.

![](dg-5-3-941-release-notes/003.png)

<span id="_Toc531616766" class="anchor"></span>Figure 2: DG\*5.3\*941 Updates to Address Validation Step 1

![](dg-5-3-941-release-notes/004.png)

<span id="_Toc531616767" class="anchor"></span>Figure 3: DG\*5.3\*941 Updates to Address Validation Step 2

10. VistA then prompts for confirmation to save the changes to the Phone Number fields. The previous phone number fields are displayed along with the updated phone numbers.

![](dg-5-3-941-release-notes/005.png)

<span id="_Toc531616768" class="anchor"></span>Figure 4: DG\*5.3\*941 Updates to Phone Number Change Prompts

11. If the user answers "Y", the changes are saved. If the user answers "N", the changes are discarded.
12. After the phone numbers are processed, if the address validation described above had failed, the user is returned to the RESIDENTIAL COUNTRY prompt.
13. When the user has completed editing a Residential Address and Phone Number, VistA prompts the user "Copy the Residential Address to the Permanent Mailing Address? NO//".
    1.  If the user selects "Yes", VistA copies the Residential Address fields to the Permanent Mailing Address, displays the Permanent Mailing Address fields, and requests confirmation to update.
    2.  If the user selects "No", the copy is cancelled and VistA returns to SCREEN \<1.1\>.

![](dg-5-3-941-release-notes/006.png)

<span id="_Toc531616769" class="anchor"></span>Figure 5: DG\*5.3\*941 Updates to Copy Residential Address to Permanent Mailing Address Prompts

14. The user cannot exit the Residential Address prompts by entering an up carat "^".
15. The Last Update field is system-generated and displayed as view only.
16. VistA PATIENT DEMOGRAPHIC DATA, SCREEN \<1\> is updated as follows:
    1.  Group \[1\]: The Phone Number \[Residence\] and Phone Number \[Work\] are no longer presented to the user with the Permanent Mailing Address on Registration screens.
    2.  Group \[4\]: The Permanent Mailing Address group of fields are removed. The fields 'Cell Phone', 'Pager \#' and 'Email Address' are added.
    3.  Group \[5\]: The fields 'Language Date/Time' and 'Preferred Language' are added. Temporary Mailing Address fields are removed.

![](dg-5-3-941-release-notes/007.png)

<span id="_Toc531616770" class="anchor"></span>Figure 6: DG\*5.3\*941 Updates to VistA PATIENT DEMOGRAPHIC DATA,  
SCREEN \<1\> Groups \[1\], \[4\], and \[5\]

17. VistA ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN \<1.1\> is redesigned as follows:
    1.  Group \[1\] Residential Address is added with the following fields:

> Address Line 1

> Address Line 2

> Address Line 3

> City

> State, Zip Code, County - for UNITED STATES address

> Province, Postal Code - for foreign address

> Country (default equals "United States" for a new address

> Phone (Phone Number \[Residence\])

> Office (Phone Number \[Work\])

2.  Group \[2\] 'Cell Phone', 'Pager \#', and 'Email Address' are removed.
3.  Group \[2\] Permanent Mailing Address - is added with the same group of fields as originally presented in SCREEN \<1\>, group \[4\], with the removal of the 'Phone:' and 'Office:' fields.
4.  Group \[3\] 'Language Date/Time' and 'Preferred Language' are removed.
5.  Group \[3\] Temporary Mailing Address is added with the same group of fields as originally presented in SCREEN \<1\>, group \[5\].
6.  Group \[4\] Confidential Mailing Address is added - same group of fields as originally presented in ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN \<1.1\>, group \[1\].

![](dg-5-3-941-release-notes/008.png)

<span id="_Toc531616771" class="anchor"></span>Figure 7: DG\*5.3\*941 Updates to ADDITIONAL PATIENT DEMOGRAPHIC DATA,  
SCREEN \<1.1\> Groups \[1\] – \[4\]

18. The Demographic Help Screens for SCREEN \<1\> and SCREEN \<1.1\> reflect the changes described above in \#16 and \#17.
19. On the ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN \<1.1\>, when the user is adding a Permanent Mailing Address that is currently blank and a Residential Address was entered, VistA prompts the user "Copy the Residential Address to the Permanent Mailing Address? NO//".
    1.  If the user selects "Yes", VistA copies the Residential Address fields to the Permanent Mailing Address, and displays the Permanent Mailing Address fields and requests confirmation to add.
    2.  If the user selects "No", VistA proceeds by prompting for each Permanent Mailing Address field.

![](dg-5-3-941-release-notes/009.png)

<span id="_Toc531616772" class="anchor"></span>Figure 8: DG\*5.3\*941 Updates to Copy Residential Address to Permanent Mailing Address Prompts

20. On the ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN \<1.1\>, when the user has edited and saved a Permanent Mailing address and the Permanent Mailing address is an allowable Residential Address (not a P.O. Box or General Delivery and has the required fields) VistA prompts the user "Copy the Permanent Mailing Address to the Residential Address?"  
    If the user selects "Yes", VistA copies the Permanent Mailing Address fields to the Residential Address, displays the Residential Address fields, and requests confirmation to update.

![](dg-5-3-941-release-notes/010.png)

<span id="_Toc531616773" class="anchor"></span>Figure 9: DG\*5.3\*941 Updates to Copy Permanent Mailing Address to Residential Address Prompts

21. A history of Residential address changes is maintained by VistA via VA FileMan auditing.

#### Part 2: Determine Non-Residential Address

1.  VistA prevents a user from saving a Residential Address that is in a non-residential format with General Delivery or P.O. Box. A non-residential address is defined as Address Line 1 starting with any of the following in upper case, lower case, or mixed case (with or without a period):

> "Post Office"

> "P.O." or "PO"

> "General Delivery"

> "Box" when immediately followed by a number.

1.  The user can enter a non-residential address format when:
    1.  The Veteran's Residential address is Alaska or Hawaii
    2.  The Veteran resides in one of the United States territories (Guam, American Samoa, CNMI (Mariana Islands), U.S. Virgin Islands, or Philippines)
2.  If the user attempts to save a Residential Address that violates the non-residential address rules defined above, saving the record is not allowed. The following error message is displayed: "You cannot enter 'P.O. Box' or 'General Delivery' for a Residential Address".

#### Part 3: Patient Address Updates

1.  When editing the Temporary Mailing Address, the prompts for these fields are renamed as follows:
    1.  TEMP MAILING ADDRESS ACTIVE?:
1.  TEMP MAILING ADDRESS START DATE:
2.  TEMP MAILING ADDRESS END DATE:

![](dg-5-3-941-release-notes/011.png)

<span id="_Toc531616774" class="anchor"></span>Figure 10: DG\*5.3\*941 Updates to Temporary Mailing Address Field Prompts

1.  In the Patient Address Update \[DG ADDRESS UPDATE\] option, on the screen for editing the Permanent Mailing Address, the 'PHONE NUMBER \[RESIDENCE\]' and 'PHONE NUMBER \[OFFICE\]' fields are removed.
2.  The Patient Inquiry Screen \[DG PATIENT INQUIRY\] is modified so the first screen mimics the format of SCREEN \<1.1\>.
    1.  Residential Address group of fields is added.
    2.  Permanent Mailing Address, Temporary Mailing Address, and Confidential Mailing Address groups of field are shifted on the screen to mimic the same positions as in SCREEN \<1.1\>.
    3.  The Cell phone number and email remain displayed with the Permanent Mailing Address.
3.  A new CASS Certified field was added for Residential Address (RESIDENTIAL ADDR CASS IND field .1159), Confidential Mailing (CONFIDENTIAL ADDR CASS IND field .14117), Temporary Mailing (TEMPORARY ADDR CASS IND field .12115) and Permanent Mailing (STREET ADDRESS CASS IND field .1118) address types. This new field will be set to "NC" Not Checked when a user enters a new address or edits an existing address.

#### Part 4: Add Residential Address to Address Sharing APIs

The VADPT routine includes the Residential Address. It now returns the Residential Address with the Patient Address data. This applies to ICR 10061 at entry point "ADD^VADPT". This provides other VistA packages with the ability to edit the Residential Address, which is planned for a future release.

#### Part 5: Address Change Source Fields Updates

The Z05 received from the Enrollment System can include any of the following: Residential or Permanent Address, a Residence or Cellular Phone Number or an Email Address. If VistA accepts the update, now the Change Source can contain the value "VET360" and VistA will store "VET360" in the corresponding PATIENT file (#2) Change Source field. The change source fields are:

> ADDRESS CHANGE SOURCE (Permanent Address)  
> RESIDENTIAL ADDR CHANGE SOURCE  
> RESIDENCE NUMBER CHANGE SOURCE  
> CELLULAR NUMBER CHANGE SOURCE  
> EMAIL ADDRESS CHANGE SOURCE

#### Part 6: Defect – DG Address Update Prompt Labels

On the screen in Registration menu option Patient Address Update \[DG ADDRESS UPDATE\]:  
The labels in the prompt are modified from "Do you want to update the (P)ermanent Address, (T)emporary Address, or (B)oth?" to "Do you want to update the (P)ermanent Mailing Address, (T)emporary Mailing Address, or (B)oth?".

![](dg-5-3-941-release-notes/012.png)

<span id="_Toc531616775" class="anchor"></span>Figure 11: DG\*5.3\*941 Updates to Patient Address Update Menu Option

#### Part 7: Health Benefit Plan Name Corrected

In the HEALTH BENEFIT PLAN file (#25.11) the name of a Health Benefit Plan (HBP) is corrected. "Veteran Plan - VC - Unusual and Excessive Burden" is changed to "Veteran Plan - VC - Unusual or Excessive Burden."

#### Part 8: PATIENT File (#2) Address Trigger ADTTM8

1.  When any Residential Address field is changed (see list below), it modifies the Residential Address Change Date and Time field.

RESIDENTIAL ADDR CHANGE DT/TM (#.1158)

> RESIDENTIAL ADDRESS \[LINE 1\]  
> (#.1151) New  
> RESIDENTIAL ADDRESS \[LINE 2\]  
> (#.1152) New  
> RESIDENTIAL ADDRESS \[LINE 3\]  
> (#.1153) New  
> RESIDENTIAL CITY  
> (#.1154) New  
> RESIDENTIAL STATE  
> (#.1155) New  
> RESIDENTIAL ZIP+4  
> (#.1156) New  
> RESIDENTIAL COUNTY  
> (#.1157) New  
> RESIDENTIAL PROVINCE  
> (#.11571) New  
> RESIDENTIAL POSTAL CODE  
> (#.11572) New  
> RESIDENTIAL COUNTRY  
> (#.11573) New

2.  Any modification of the Residential Address Change Date and Time field RESIDENTIAL ADDR CHANGE DT/TM (#.1158) triggers the update of the Residential Address Source of Change field RESIDENTIAL ADDR CHANGE SOURCE (#.11582).

#### Part 9: Address Fields Converted to Uppercase

All address text fields on SCREEN \<1.1\> are modified to automatically convert the text entered to uppercase. This applies to address lines 1, 2, and 3, City, Province, Postal Code for Residential Address, Permanent Mailing Address, Temporary Mailing Address, and Confidential Mailing Address.

### IVM\*2.0\*164

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  With installation of this patch, VistA receives, stores, and displays Residential Addresses sent by ES.
    1.  Address changes are received from ES via Z05 HL7 messages, which now include the Residential Address in the PID segment.
1.  Logic for Confidential Mailing Address now allows VistA to process Confidential Mailing Address updates when ES is ready to send them. Previously, when a Confidential Mailing Address was updated in ES, a Z05 was sent to VistA, but "site number" logic prevented the address changes from being processed on VistA. The impact of this change will not be apparent until ES begins to send the Confidential Mailing Addresses to VistA.
1.  When VistA receives a Residential Address type on the Z05 HL7 message from ES, VistA checks the Date/Time last updated:
    1.  If, and only if, the incoming address is newer, the address is stored in VistA.
    2.  If the incoming address on the Z05 is older, it is not stored.
    3.  No other validation is applicable to Residential Address types during the Z05 upload.
2.  The HL7 message from ES to VistA includes the new CASS Certified field for Permanent Mailing, Temporary Mailing, Confidential Mailing, and Residential Address types in the new ZAV Segment.
    1.  The new ZAV, Address Verification, segment will be included for each address type included in the Z05 message.
    2.  The new ZAV, Address Verification, segment will be included for each address type included in the Z07 message.
3.  The IVM Demographic Upload Utility is modified to include the Permanent Mailing Address CASS Certified field.  
    When a Permanent Mailing Address is received from ES on the Z05, the associated CASS Certified field will either be uploaded to the IVM Demographic Upload Utility or directly to the PATIENT file (#2) based on the existing rules for processing a Permanent Mailing Address.
4.  The following menu options allow a Registration user to view, add, or update the Residential Address. If any Residential address field is added or updated, VistA will send the change to ES via the Z07 HL7 message. The new ZAV, Address Verification, segment will be included for each address type included in the Z05 message.

Load/Edit Patient Data \[DG LOAD PATIENT DATA\]

Patient Inquiry \[DG PATIENT INQUIRY\]

Preregister A Patient \[DGPRE PRE-REGISTER OPTION\]

Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]

Register A Patient \[DG REGISTER PATIENT\]

Patient Address Update \[DG ADDRESS UPDATE\]

Admit A Patient \[DG ADMIT PATIENT\]

### EAS\*1.0\*151

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new address type "Residential Address" can be viewed via the VistA option "View Patient Address" (EAS VIEW PATIENT ADDRESS). This address is used by Enrollment and Eligibility to retain the geographic residence of an applicant or patient. It supports the Enrollment System Community Care (ESCC) program's need to determine geographic distance from a treatment facility.

In addition the screen labels and prompts are modified as follows.

1.  The field label for the patient address is modified from "Patient Address" to "Permanent Mailing Address".
1.  The field label for the date of the patient address change is modified from "Patient Add Change Date" to "Permanent Mailing Add Change Date".
2.  The field label for the site of the patient address change is modified from "Patient Add Change Site" to "Permanent Mailing Add Change Site".
3.  The field label for the source of the patient address change is modified from "Patient Add Change Source" to "Permanent Mailing Add Change Source".

REDACTED

<span id="_Toc531616776" class="anchor"></span>Figure 12: EAS\*1.0\*151 Updates to Patient Address Field Labels

4.  After displaying the Permanent Mailing Address, the user is prompted for displaying the Confidential Mailing, Temporary Mailing and Residential addresses if they exist in the patient record. This prompt is modified from: "Would you like to see the Confidential and Temporary Addresses? Yes//" to "Would you like to view the Conf Mailing, TempMailing and Residential Addresses? Yes//"

REDACTED

<span id="_Toc531616777" class="anchor"></span>Figure 13: EAS\*1.0\*151 Updates to View Patient Address Prompts

5.  The display of the Confidential Address is modified as follows:
    1.  The field label for the Confidential Address is modified from "Confid Address" to "Confid Mailing Address".
    2.  The field label for the date of the Confidential Address change is modified from "Confid Add Change Date" to "Confid Mailing Add Change Date".
    3.  The field label for the site of the Confidential Address change is modified from "Confid Add Change Site" to "Confid Mailing Add Change Site".
    4.  The field label for the start date of the Confidential Address is modified from "Confid Add Start Date" to "Confid Mailing Add Start Date".
    5.  The field label for the end date of the Confidential Address is modified from "Confid Add End Date" to "Confid Mailing Add End Date".
6.  The display of the Temporary Address is modified as follows:
    1.  The field label for the Temporary Address is modified from "Temp Address" to "Temp Mailing Address".
    2.  The field label for the date of the Temporary Address change is modified from "Temp Add Change Date" to "Temp Mailing Add Change Date".
    3.  The field label for the site of the Temporary Address change is modified from "Temp Add Change Site" to "Temp Mailing Add Change Site".
    4.  The field label for the start date of the Temporary Address is modified from "Temp Add Start Date" to "Temp Mailing Add Start Date".
    5.  The field label for the end date of the Temporary Address is modified from "Temp Add End Date" to "Temp Mailing Add End Date".

REDACTED

<span id="_Toc531616778" class="anchor"></span>Figure 14: EAS\*1.0\*151 Updates to Temporary Address Display

7.  The Residential Address is added to the display if it exists in the patient record. The display of the Residential Address contains the following fields from the PATIENT file (#2):
1.  RESIDENTIAL ADDRESS LINE 1 (#.1151)
2.  RESIDENTIAL ADDRESS LINE 2 (#.1152)
3.  RESIDENTIAL ADDRESS LINE 3 (#.1153)
4.  RESIDENTIAL ADDRESS CITY (#.1154)
5.  For United States addresses:
- RESIDENTIAL STATE (#.1155)
- RESIDENTIAL ZIP+4 (#.1156)
6.  For foreign addresses:
- RESIDENTIAL PROVINCE (#.11571)
- RESIDENTIAL POSTAL CODE (#.11572)
7.  RESIDENTIAL COUNTRY (#.1153)
8.  RESIDENTIAL ADDRESS CHANGE SITE (#.11581)
9.  RESIDENTIAL ADDRESS CHANGE SOURCE (#.11582)
10. RESIDENTIAL ADDRESS CHANGE DT/TM (#.1158)

REDACTED

<span id="_Toc531616779" class="anchor"></span>Figure 15: EAS\*1.0\*151 Updates to Residential Address Display

### From: DG*5.3*1031 Release Notes

## List of Incidents and Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### INC12252768

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After Patch DG\*5.3\*993 installation, the system shows the message "Use Register a Patient option to add a new person.".

<u>Problem:</u>

In the Admit a Patient \[DG ADMIT PATIENT\] option, when admitting or editing an existing patient, an incorrect message may display. A message added with DG\*5.3\*993, "Use Register a Patient to add a new patient." displays after the "PRIMARY PHYSICIAN:" prompt. The user may press RETURN a few times to continue the admission.

Admit PATIENT: SEPPATIENTONE,VETERANONE MM-DD-YY 000011111 NO

NSC VETERAN

Enrollment Priority: 4 Category: VERIFIED End Date:

Select ADMISSION DATE: AUG 27,2020@07:38:31//

ADMISSION DATE: AUG 27,2020@07:38:31//

DOES THE PATIENT WISH TO BE EXCLUDED FROM THE FACILITY DIRECTORY?: NO

//

ADMITTING REGULATION:

NSC// 6

TYPE OF ADMISSION: DIRECT//

DIAGNOSIS \[SHORT\]: TESTING//

WARD LOCATION: 82-1A//

ROOM-BED:

FACILITY TREATING SPECIALTY: GENERAL MEDICAL(ACUTE MED)

//

PRIMARY PHYSICIAN: PROVIDERONE,TESTPROVIDER//providerone,te

PROVIDERONE,TESTPROVIDER A MAB 111 MEDICAL SERVICE PHYSICIAN

Use Register a Patient option to add a new person.

Press RETURN to continue...

ATTENDING PHYSICIAN: //providertwo,te PROVIDERtwo,TESTPROVIDER B

MAB 111 MEDICAL SERVICE PHYSICIAN

<span id="_Toc51762415" class="anchor"></span>Figure : Incorrect Message Display

This behavior may also be observed in the Extended Bed Control \[DG BED CONTROL EXTENDED\] options. This issue has only been reported at the Battle Creek VA Medical Center site. With DG\*5.3\*993, the new message "Use Register a Patient to add a new patient." should display only at the "ADMIT Patient:" prompt if the user attempts to do a patient lookup and admit a new patient. It incorrectly appears after the "PRIMARY PHYSICIAN:" prompt because the patient lookup routine did not prevent the message from displaying if the routine was called for a different purpose during the admission.

<u>  
</u>

<u>Resolution:</u>

The patient lookup logic for the Admit a Patient \[DG Admit Patient\] option is modified to only display the "Use Register a Patient to add a new patient." message when the patient cannot be found at the site. The message is no longer displayed at other admission prompts when the routine is called for a different purpose in the Admit a Patient \[DG Admit Patient\] or Extended Bed Control \[DG BED CONTROL EXTENDED\] options.

### INC12223437

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG DISPOSITION APPLICATION error.

<u>Problem:</u>

When using the Disposition an Application \[DG DISPOSITION APPLICATION\] option for a REGISTRATION ONLY patient, an undefined error occurs and terminates the user's connection to VistA.

Disposition PATIENT: SEPPATIENTSIX,VETERANSIX MM-DD-YY 000011116

NO

NSC VETERAN

No Patient Warnings on file for SEPPATIENTSIX,VETERANSIX.

Press RETURN to continue...

Enrollment Priority: 4 Category: VERIFIED End Date:

LOG DATE TYPE OF BENEFIT APPLIED FOR

-----------------------------------------------

04/17/2020@14:23 OUTPATIENT MEDICAL

RECORDING THAT AN ERROR OCCURRED ---

Sorry 'bout that

\$ZERROR=

Logged out at Sep 16, 2020 5:41 pm

<span id="_Toc51762416" class="anchor"></span>Figure : Disposition an Application Error

<u>Resolution:</u>

The logic is updated to handle a blank value in the EXAMINED IN MEDICAL CENTER field (#7) in the DISPOSITION LOG-IN DATE/TIME SUBFILE (#2.101) file of the PATIENT (#2) file. The default values for prompts in the Disposition an Application \[DG DISPOSITION APPLICATION\] option are set if the field is blank, so an undefined error will not occur.

### INC12223327

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(Duplicate of Incident INC12223437)  
DG DISPOSITION APPLICATION error.

<u>Problem:</u>

When using the Disposition an Application \[DG DISPOSITION APPLICATION\] option for a REGISTRATION ONLY patient, an undefined error occurs and terminates the user's connection to VistA.

<u>Resolution:</u>

The logic is updated to handle a blank value in the EXAMINED IN MEDICAL CENTER field (#7) in the DISPOSITION LOG-IN DATE/TIME SUBFILE (#2.101) file of the PATIENT (#2) file. The default values for prompts in the Disposition an Application \[DG DISPOSITION APPLICATION\] option are set if the field is blank, so an undefined error will not occur.

### INC12226257

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(Duplicate of Incident INC12223437)  
DG DISPOSITION APPLICATION error.

<u>Problem:</u>

When using the Disposition an Application \[DG DISPOSITION APPLICATION\] option for a REGISTRATION ONLY patient, an undefined error occurs and terminates the user's connection to VistA.

<u>Resolution:</u>

The logic is updated to handle a blank value in the EXAMINED IN MEDICAL CENTER field (#7) in the DISPOSITION LOG-IN DATE/TIME SUBFILE (#2.101) file of the PATIENT (#2) file. The default values for prompts in Disposition an Application \[DG DISPOSITION APPLICATION\] option are set if the field is blank, so an undefined error will not occur.

### INC12449251

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error during patient admission process caused by patch DG\*5.3\*993.

<u>Problem:</u>

In the Admit a Patient \[DG ADMIT PATIENT\] option, when admitting or editing an existing patient, an incorrect message may display. A message added with DG\*5.3\*993, "Use Register a Patient to add a new patient." displays either after the Admission Date confirmation, or after the "Patient admitted." message. The incorrect message repeats and the user cannot exit except by closing the session.

Admit PATIENT: SEPPATIENTTWO,VETERANTWO MM-DD-YY 000011112 NO

NSC VETERAN

Enrollment Priority: 4 Category: VERIFIED End Date:

Select ADMISSION DATE: NOW//

ARE YOU SURE YOU WANT TO ADD 'SEP 22,2020@12:01:01' AS A NEW ADMISSION DATE?// Y

(Yes)

Use Register a Patient option to add a new person.

Press RETURN to continue...

Use Register a Patient option to add a new person

Press RETURN to continue...^

Use Register a Patient option to add a new person

Press RETURN to continue...

<span id="_Toc51762417" class="anchor"></span>Figure : Admit a Patient Error

This behavior may also be observed in the Detailed Inpatient Inquiry \[DG INPATIENT INQUIRY EXTENDED\] and the Extended Bed Control \[DG BED CONTROL EXTENDED\] options. This issue has been reported at Ann Arbor, Lexington, and Louisville sites. With DG\*5.3\*993, the new message "Use Register a Patient to add a new Patient. Press RETURN to continue." should only display at the "ADMIT Patient:" prompt if the user attempts to do a patient lookup and admit a new patient. It incorrectly appears after the Admission Date confirmation and "Patient admitted" message because the patient lookup routine did not prevent the message from displaying if the routine was called for a different purpose during the admission.

<u>Resolution:</u>

The patient lookup logic for the Admit a Patient \[DG Admit Patient\] option is modified to only display the "Use Register a Patient to add a new patient. Press RETURN to continue." message when the patient cannot be found at the site. The message is no longer displayed at other admission prompts when the routine is called for a different purpose in the Admit a Patient \[DG Admit Patient\] option.

### From: DG*5.3*1006 Release Notes

## Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dg-5-3-1006-release-notes/001.png)

March 2020Department of Veterans AffairsOffice of Information and Technology (OIT)

Table of Contents

List of Figures

List of Tables

[Table 1: DG\*5.3\*1006 Enhancements and Modifications [2](#_Ref533696768)](#_Ref533696768)

[Table 2: Defects and Fixes in DG\*5.3\*1006 [3](#_Ref524346485)](#_Ref524346485)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release of Veterans Health Information System and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) Registration (DG) patch DG\*5.3\*1006 supports the enhancements for the Enterprise Health Benefits Determination (EHBD) program that focuses on updates for the Enrollment System Modernization (ESM) Phase 2 project, which supports Enrollment System Community Care (ESCC) and Enrollment System (ES) Sustainment.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Notes cover the changes to VistA REE for this release. Patch DG\*5.3\*1006 is also being released in support of the ES 5.10 release. Refer to Informational Patch EAS\*1\*186 (Enrollment Application System) for additional details regarding the ES release.

### Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA REE and applies to the changes made between this release and any previous release for this software.

### This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is being released as a patch (PackMan) message. The PackMan message includes the DG\*5.3\*1006 patch, which also supports the ES 5.10 release.

The following sections provide a summary of the enhancements and modifications to the existing software for VistA REE with the release of patch DG\*5.3\*1006.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new features or functions added to VistA REE for DG\*5.3\*1006.

### Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA REE patch DG\*5.3\*1006 renames Veteran Medical Benefit Plans (VMBPs) as VHA Profiles (VHAPs) to support the Electronic Health Record (EHR) in Cerner's Millennium application. VistA REE ELIGIBILITY VERIFICATION DATA SCREEN \<11\> and list templates associated with VHAP Screens \<11.1\>, \<11.3\>, \<11.3.1\>, and \<11.4\> are updated to refer to the plans as "VHA Profiles".

VistA REE Patch DG\*5.3\*1006 modifies the NAME (#.01) field of the HEALTH BENEFIT PLAN file (#25.11) of 24 VHA Profiles, eliminating non-alphanumeric characters, to allow the profiles to be successfully sent to the Cerner application. The affected VHAPs are detailed in the "Listing of Updates" section of this patch description.

Patch DG\*5.3\*1006 loads the HEALTH BENEFIT PLAN file (#25.11) to store seven new core VHA Profile names, codes, and short and long descriptions. VistA will accept the new profiles from ES via Health Level Seven (HL7) ORF-Z11/ORU-Z11 messages.

Patch DG\*5.3\*1006 modifies the VHAP \<11.3\> and VHAP \<11.3.1\> screens to display the ASSIGNED DATE AND TIME field (#1) of the CURRENT HEALTH BENEFIT PLAN subfile (#25.01) of the PATIENT file (#2) with both the date and time.

Patch DG\*5.3\*1006 modifies the help text for the VHAP \<11.1\> screen so that the response to an entry of "?" displays "Profile name preceded by 'zz' indicates the profile is inactive."

The Patient Inquiry \[DG PATIENT INQUIRY\] option and Patient Inquiry application program interface (API) (DGRPD) is updated to display "VHA Profiles" instead of "Veteran Medical Benefit Plan". The API DGRPD is called from VistA REE menu options, subscribers to API DGRPD, and other VistA packages.

Integration Control Registration (ICR) 10037 (DGRPD) is updated to display "VHA Profiles" instead of "Veteran Medical Benefit Plan".

ICR 10037 NAME: DGRPD

CUSTODIAL PACKAGE: REGISTRATION

SUBSCRIBING PACKAGE:

USAGE: Supported

Patch DG\*5.3\*1006 corrects VHAP long descriptions for the following profiles: COMPREHENSIVE EXTENDED CARE SERVICES COPAY EXEMPT, VETERAN EXTENDED CARE SERVICES COPAY EXEMPT, and VETERAN EXTENDED CARE SERVICES COPAY REQ.

Table 1 shows the enhancements and modifications included in the DG\*5.3\*1006 release as tracked in Rational Team Concert (RTC) Requirements Management (RM).

<table>
<caption><p><span id="_Ref533696768" class="anchor"></span>Table 1: DG*5.3*1006 Enhancements and Modifications</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RTC<br />
RM #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1158673</td>
<td>Assign VMBP to Individuals with no Veteran Eligibility Code (associated with Employee)</td>
</tr>
<tr class="even">
<td>1159224</td>
<td>VMBP: Plan Name Changes</td>
</tr>
<tr class="odd">
<td>1162280</td>
<td>VMBP: Add new and update existing manual plans</td>
</tr>
<tr class="even">
<td>1165388</td>
<td>ES 5.10 Maintain the Enrollment System - VistA View History Date/Time Display Change</td>
</tr>
</tbody>
</table>

<span id="_Ref533696768" class="anchor"></span>Table 1: DG\*5.3\*1006 Enhancements and Modifications

### Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the defects and fixes and corresponding Rational Team Concert (RTC) Change and Configuration Management (CM) numbers included in DG\*5.3\*1006.

<table>
<caption><p><span id="_Ref524346485" class="anchor"></span>Table 2: Defects and Fixes in DG*5.3*1006</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
CM #</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1221614</td>
<td><p><strong>Defect</strong>: VHAP long descriptions are displaying "=70%" instead of "&gt;=70%" for the following profiles: COMPREHENSIVE EXTENDED CARE SERVICES COPAY EXEMPT, VETERAN EXTENDED CARE SERVICES COPAY EXEMPT, and VETERAN EXTENDED CARE SERVICES COPAY REQ.</p>
<p><strong>Fix</strong>: The three VHAP long descriptions are corrected to display "&gt;=70%".</p></td>
</tr>
</tbody>
</table>

<span id="_Ref524346485" class="anchor"></span>Table 2: Defects and Fixes in DG\*5.3\*1006

### List of Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch makes the following enhancements to VistA REE:

1.  Twenty-four existing profiles have been updated to the HEALTH BENEFIT PLAN file (#25.11), eliminating non-alphanumeric characters, in order to support the EHR in Cerner's Millennium application. A pre-install routine included in the build executes the logic to accomplish the profile renames.
    1.  VETERAN FULL MED BENEFITS TX AND RX COPAY EXMT
    2.  VETERAN FULL MED BENEFITS TX AND RX COPAY EXMT 6
    3.  VETERAN FULL MED BENEFITS TX COPAY EXMT AND RX COPAY REQ
    4.  VETERAN FULL MED BENEFITS TX COPAY EXMT AND RX COPAY REQ 6
    5.  VETERAN FULL MED BENEFITS TX COPAY REQ AND RX COPAY EXMT 6
    6.  VETERAN FULL MED BENEFITS TX COPAY REQ AND RX COPAY EXMT 7
    7.  VETERAN FULL MED BENEFITS TX COPAY REQ AND RX COPAY EXMT 8
    8.  VETERAN FULL MED BENEFITS TX AND RX COPAY REQ 6
    9.  VETERAN FULL MED BENEFITS TX AND RX COPAY REQ 8
    10. VETERAN FULL MED BENEFITS TX GMT COPAY REQ AND RX COPAY EXMT
    11. VETERAN FULL MED BENEFITS TX GMT COPAY REQ AND COPAY EXMT 6
    12. VETERAN FULL MED BENEFITS TX GMT COPAY REQ AND RX COPAY REQ
    13. VETERAN FULL MED BENEFITS TX GMT AND RX COPAY REQ 6
    14. VETERAN RESTRICTED MED BENEFITS
    15. NONVETERAN OTHER RESTRICTED MED BENEFITS
    16. ACTIVE DUTY AND SHARING AGREEMENTS
    17. BENEFICIARY NEWBORN
    18. BENEFICIARY CHAMPVA
    19. BENEFICIARY SPINA BIFIDA
    20. BENEFICIARY CHILDREN OF WOMEN OF VIETNAM VETERANS
    21. VETERAN FOREIGN MEDICAL PROGRAM
    22. CAREGIVER PRIMARY FAMILY
    23. CAREGIVER SECONDARY FAMILY
    24. CAREGIVER GENERAL
2.  Seven new profiles have been added to the HEALTH BENEFIT PLAN file (#25.11). The data is provided in the build with the full data dictionary of the HEALTH BENEFIT PLAN file (#25.11).
    1.  EMPLOYEE ONLY
    2.  COMPREHENSIVE EXTENDED CARE SERVICES COPAY EXEMPT
    3.  VETERAN EXTENDED CARE SERVICES COPAY EXEMPT
    4.  VETERAN EXTENDED CARE SERVICES COPAY REQ
    5.  EXTENDED CARE SERVICES HUMANITARIAN
    6.  ASSISTED REPRODUCTIVE TECHNOLOGY
    7.  HIGH RISK VETERAN
3.  Nine existing profiles have been updated in the HEALTH BENEFIT PLAN file (#25.11) so that they are properly displayed based on the profile code being passed to VistA. The data is provided in the build with the full data dictionary of the HEALTH BENEFIT PLAN file (#25.11).
    1.  VETERAN FOREIGN MEDICAL PROGRAM
    2.  CAREGIVER GENERAL
    3.  CAREGIVER PRIMARY FAMILY
    4.  CAREGIVER SECONDARY FAMILY
    5.  BENEFICIARY NEWBORN
    6.  BENEFICIARY CHAMPVA
    7.  BENEFICIARY CHILDREN OF WOMEN OF VIETNAM VETERANS
    8.  BENEFICIARY SPINA BIFIDA
    9.  VETERAN FULL MED BENEFITS TX COPAY EXMT AND RX COPAY REQ 6
4.  The ELIGIBILITY VERIFICATION DATA SCREEN \<11\> screen is updated to display "VHA Profiles (VHAP):" instead of "Veteran Medical Benefit Plan (VMBP):".

![](dg-5-3-1006-release-notes/002.png)

<span id="_Toc33187911" class="anchor"></span>Figure 1: Eligibility Verification Data, Screen \<11\>

5.  The list template DGEN HBP PATIENT for the VHAP \<11.1\> screen is updated so that the header text of the screen reads "VHAP" instead of "VMBP". The profiles are now labeled "Current VHAP" and the VD option is updated to read "View All VHAP Detail".

![](dg-5-3-1006-release-notes/003.png)

<span id="_Toc33187912" class="anchor"></span>Figure 2: VHAP \<11.1\> Screen

6.  The list templates DGEN HBP VIEW for the VHAP \<11.3\> screen and DGEN HBP VIEWEXP for the VHAP \<11.3.1\> screen are updated to display the ASSIGNED DATE AND TIME field (#1) of the CURRENT HEALTH BENEFIT PLAN subfile (#25.01) of the PATIENT file (#2) with date and time that will display "VHAP" instead of "VMBP" on the header text of the screens. The column header for the profile name is modified to display "Profile" instead of "Plan Name". In screen \<11.3\> the prompt when selecting "EP Expand Entry" is modified to display "Select Profile:" instead of "Select Plan:".

![](dg-5-3-1006-release-notes/004.png)

<span id="_Toc33187913" class="anchor"></span>Figure 3: VHAP \<11.3\> Screen

![](dg-5-3-1006-release-notes/005.png)

<span id="_Toc33187914" class="anchor"></span>Figure 4: VHAP \<11.3.1\> Screen

7.  The list template DGEN HBP DETIAL for the VHAP \<11.4\> screen is updated so that the header text of the screen reads "VHAP" instead of "VMBP" and the label "VMBP View All Detail" is updated to display "VHAP View All Detail".

![](dg-5-3-1006-release-notes/006.png)

<span id="_Toc33187915" class="anchor"></span>Figure 5: VHAP \<11.4\> Screen

8.  In the Patient Inquiry \[DG PATIENT INQUIRY\] option, the label "Veteran Medical Benefit Plan Currently Assigned to Veteran:" is updated to display "VHA Profiles Currently Assigned to Veteran".

![](dg-5-3-1006-release-notes/007.png)

<span id="_Toc33187916" class="anchor"></span>Figure 6: Patient Inquiry Option

> **NOTE:** The label change is also displayed in external applications and packages that make use of the Patient Inquiry API and Integration Control Registrations (ICRs) \#2041, \#10037, and \#740.

The applications include:

Women's Health (WV)  
Barcode Medication Administration (BCMA)  
VISTA IMAGING - CLINICAL DISPLAY  
Order Entry Results Reporting  
Outpatient Pharmacy Manager (PSO MANAGER)  
Computerized Patient Record System (CPRS)  
Clinical Information Resource Network (CIRN)  
Automated Medical Information Exchange (AMIE)  
Regional Office Patient Inquiry (DVBA REG OFF PATIENT INQ)

The following VistA REE menu options also make use of the Patient Inquiry API and reflect the label change:

Collateral Patient Register \[DG COLLATERAL PATIENT\] option  
Load/Edit Patient \[DG LOAD PATIENT DATA\] option  
Register A Patient \[DG REGISTER PATIENT\] option

9.  The help text for the VHAP \<11.1\> screen is updated so that the response to an entry of "?" displays "Profile name preceded by 'zz' indicates the profile is inactive."

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

### Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

| Title                           | File Name          | FTP Mode |
|---------------------------------|--------------------|----------|
| DG\*5.3\*1006 Release Notes     | DG_5_3_P996_RN.PDF | (binary) |
| User Manual - Registration Menu | PIMS_REG_UM.PDF    | (binary) |

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from <span class="mark">redacted.</span>

Documentation can also be found on the VA Software Documentation Library at: <https://www.va.gov/vdl/>.

### From: DG*5.3*977 Release Notes

### Registration Screen 7 - EXPANDED MH CARE TYPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the primary eligibility is EXPANDED MH CARE NON-ENROLLEE, the new value "OTH-EXT EXTENDED MH OTH" for the EXPANDED MH CARE TYPE field will be displayed after the primary eligibility as follows:

PRIMARY ELIGIBILITY CODE: EXPANDED MH CARE NON-ENROLLEE 11 11 NON-VETERAN

This code is used ONLY for Other Than Honorable veterans

seeking mental healthcare prior to VBA ADJUDICATION.

EXPANDED MH CARE TYPE: ?

Enter the expanded mental health care type justifying the EXPANDED MH

CARE eligibility selection.

Choose from:

OTH-90 EMERGENT MH OTH

OTH-EXT EXTENDED MH OTH

### Registration Screen 7 - PRESUMPTIVE PSYCHOSIS Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new question "PRESUMPTIVE PSYCHOSIS?" will be asked at the end of input in Section 3 (ELIGIBILITY) of Screen 7.

If answered YES, the user can then select the category as follows:

REJ REJECTED DUE TO INCOME

LES LESS THAN 24 MONTHS SERVICE

OTH FSM WITH OTH (PP ONLY)

DEC VETERAN DECLINES ENROLLMENT

Here is an example: User should follow the current VA workaround as follows on Section 1:

Patient Type : SC Veteran

Veteran(Y/N) : Yes

Service Connected : Yes

Service Connected % : 0

User should follow the current VA workaround as follows on Section 3.

PRIMARY ELIGIBILITY CODE: SC LESS THAN 50% 3 3 VETERAN

Select PATIENT ELIGIBILITIES: SC LESS THAN 50%

//

ELIGIBILITY: SC LESS THAN 50%//

Select PATIENT ELIGIBILITIES:

PERIOD OF SERVICE:Persian Gulf War or Post-Vietnam (This depends on the date of birth of the patient and available system options.)

User will now be prompted with Presumptive Psychosis indicator

PRESUMPTIVE PSYCHOSIS? N// YES

PRESUMPTIVE PSYCHOSIS CATEGORY: // ?

Please select the Presumptive Psychosis category

Choose from:

REJ REJECTED DUE TO INCOME

LES LESS THAN 24 MONTHS SERVICE

OTH FSM WITH OTH (PP ONLY)

DEC VETERAN DECLINES ENROLLMENT

Screen 7 now contains a new line at the end of Section 3 (ELIGIBILITY) to show the Presumptive Psychosis category if the patient record contains this field.

### PRESUMPTIVE PSYCHOSIS CATEGORY - Five New Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: Presumptive Psychosis Reports \[DG PRESUMP. PSYCHOSIS REPORTS\]

PF Presumptive Psychosis Fiscal Year Report

PG Presumptive Psychosis Gender Report

PP Presumptive Psychosis Patient Profile Report

PS Presumptive Psychosis Status Report

PST Presumptive Psychosis Statistical Report

In order to make these new reports available to users, the menu Presumptive Psychosis Reports \[DG PRESUMP. PSYCHOSIS REPORTS\] needs to be added as the user's either primary or secondary menu. If it was added to the secondary menu, then the user needs to enter the word "PRESUMPTIVE" to access the menu above.

### OTH-EXT - EXTENDED MH OTH - CPRS OTH Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new version of the routine DGOTHBTN will supply CPRS with lines of text for the new OTH-EXT EXTENDED MH OTH care type to be displayed on the OTH button, hover over, and pop-up screen.

> **NOTE:** This functionality is available with CPRS version v31b and higher.

### OTH-EXT – MST Related Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new functionality provided by the patch will change the care type of the OTH patient with OTH-90 EMERGENT MH OTH to OTH-EXT EXTENDED MH OTH automatically if the Veteran's MST screening result is positive, and a MailMan notification about the change will be sent to DGEN ELIGIBILITY ALERT mail group members.

> **NOTE:** The care type will not be changed automatically for EXT EXTENDED MH OTH patients if their MST screening result is negative or "declined." The mailman message "Eligibility re-evaluation" will be sent to DGEN ELIGIBILITY ALERT mail group members in this case.

The following pre-existing menu option and reports have been disabled:

\[DGMST ENTER NEW MST\] MST Status Add/Edit

\[DGMST HISTORY REPORT\] MST History Report by Patient

\[DGMST SUMMARY REPORT\] MST Summary Report

\[DGMST DETAILED REPORT\] Detailed Demographic Report

\[DGMST STATISTICAL PRINT\] Print Statistical Report

### Back out of the Expanded MH Care Type Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Code and input template (DG LOAD EDIT SCREEN 7) changes will allow a user to enter ^ to back out of the Expanded MH Care Type field. If they do this, it will take them back to ELIGIBILITY STATUS DATA, SCREEN \<7\>.

### OTH Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several OTH reports have been updated so the user can select division(s) for sorting and filtering report data. They are:

- Tracking Report (OTH-90) \[DG OTH 90-DAY PERIOD\]
- Authorization Reports (OTH-90) \[DG OTH OTH90 AUTH REPORTS\]
- Other Than Honorable MH Status Report \[DG OTH MH STATUS REPORT\]

> **NOTE:** The OTH Statistical Report (OTH-90) is introduced for the first time in patch DG\*5.3\*977.

## Other Than Honorable MH Status Report - Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Changes to Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File Name (Number) Field Name (Number) New/Modified/Deleted

---------------------------- --------------------- --------------------

PATIENT (#2) EXPANDED MH CARE TYPE Modified

(#.5501)

PRESUMPTIVE PSYCHOSIS New

CATEGORY (#.5601)

PATIENT ENROLLMENT (#27.11) EXPANDED MH CARE TYPE Modified

(#50.31)

MST HISTORY (#29.11) MST CHANGE STATUS Modified

DATE (#.01)

NAME (#2) Modified

MST STATUS (#3) Modified

PROVIDER DETERMINING

STATUS (#4) Modified

OTH ELIGIBILITY PATIENT (#33) ELIGIBILITY FACTOR New

TYPE (#.03) of the

ELIGIBILITY CHANGES

SUB-FILE (#33.02) of

the OTH ELIGIBILITY

PATIENT FILE (#33)

PRESUMPTIVE PSYCHOSIS CATEGORY Full Data Dictionary New

CHANGES (#33.1)

### Input Template Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New/Modified/

Template Name Type Deleted

------------- ---- -------------

DG LOAD EDIT SCREEN 7 FILE \#2 INPUT Modified

### Indices New or Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File Name (Number) Field Name(Number) Name New/Modified

/Deleted

---------------------------- -------------------- -------- ---------

PATIENT (#2) PRIMARY ELIGIBILITY

CODE (#.361) AG Modified

PATIENT (#2) EXPANDED MH CARE TYPE AENR5501 New

(#.5501)

PATIENT (#2) PRESUMPTIVE PSYCHOSIS

CATEGORY (#.5601) AX New

### From: DG*5.3*867 Release Notes

## New Features and Fixed Previous Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement encompasses modifications to Fee Basis, Registration, and Integrated Billing to facilitate the registration and authorization of newborns. Table 1 lists all of the New Features added by this enhancement.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">FB*3.5*146</td>
</tr>
<tr class="even">
<td>1</td>
<td>Removes restrictions preventing the entry of a patient less than one year of age.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Internal checks use the date of birth instead of age</td>
</tr>
<tr class="even">
<td>3</td>
<td>Adds reject code C166 to deny claims exceeding the 7 day authorization</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>"NON-VA FOR FEMALE VET+NEWBORN 17.38" was added to the</p>
<p>VA ADMITTING REGULATION file (#43.4). This new Admitting Regulation is available when editing the 7078.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Fee Authorization dates associated with Newborns have checks in place to not allow Authorization dates that fall outside the accepted range of Newborn Authorization. The range is DOB to DOB+7; the system will warn the user and not accept an Authorization date that falls outside the appropriate range for a Newborn.</td>
</tr>
<tr class="odd">
<td colspan="2">DG*5.3*867</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>A new Patient Type of NEWBORN OF VET has been added to the</p>
<p>TYPE OF PATIENT file (#391). This new selection will be available on Registration screen &lt;7&gt;.</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>A sponsor is required for all Newborns determined by having the DOB less than one (1) year from the present date. An inconsistency check has been added to check the presence of a sponsor. If an inconsistency is found, the inconsistency check will prompt the user to return to Screen &lt;15&gt; in registration to enter a Sponsor.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>All Sponsors for Newborns must be listed as eligible for care. An inconsistency check will check the status of the Sponsors Eligibility. The check will trigger if the Sponsor has no Eligibility status. The inconsistency check will return error <strong>313 Newborn Requires Sponsor</strong> (if you try to enter a newborn without a sponsor, you will get a 313 check message at the end of the registration) or error <strong>314 Newborn Needs Eligible Sponsor</strong> (adds ability to issue a standard authorization for pre-authorized medical care for newborn coverage through midnight of the 7th day past date of birth).</p>
<p>All other statuses (i.e. Pending Verification, Verified, and Pending Re-verification) are acceptable.</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>The following default values were added when entering a Newborn:</p>
<p>PATIENT DATA, SCREEN &lt;2&gt; – "Marital" field is defaulted to "NEVER MARRIED."</p>
<p>APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN &lt;4&gt; - "Status" field is defaulted to "NOT EMPLOYED."</p>
<p>FAMILY DEMOGRAPHIC DATA, SCREEN &lt;8&gt; - "Married Last Year" field is defaulted to "NO."</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>When a Veteran Mother of a Sponsored Newborn is reviewed in the Registration screens, Screen &lt;15&gt; will display the Newborn(s), with the additional header of "Sponsored Newborn".</td>
</tr>
<tr class="odd">
<td colspan="2">IB*2.0*499</td>
</tr>
<tr class="even">
<td>11</td>
<td>The FAMILY PREFIX "NB Newborn of Vet" has been added to the Help text in the Family Prefix field (#.03) in the SPONSOR RELATIONSHIP file (#355.81).</td>
</tr>
</tbody>
</table>

## Operation Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although sites are required to use FBCS to process claims, Newborn claim can ONLY be processed by VistA at this time. FBCS can NOT be used to process Newborn claims.

## Security Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new security changes.

## Database Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle required the following modifications to Central Fee's system:

- 29 defined as the new Purpose of Visit (POV) Code for Inpatient Newborn Care
- 66 defined as the new POV Code for Outpatient Newborn Care
- Acceptance of short term authorization for Newborn patients with POV codes 29 and 66
- The inclusion of the new POV codes for Newborn Care on the following Central Fee reports:
  - Report 60002 -- Fee Basis Payment Analysis
  - Report 70001 -- Cost Analysis of Fee Basis Vouchers by Veterans and by Average Monthly Cost Range
  - Report 70007 -- Fee Veterans -- Costs By Facility, State, County, and POV
  - Report 70008 -- Fee Veterans -- Costs By VISN, Nation, and POV

## Infrastructure Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new hardware or the interfacing of any hardware.

## Other Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other dependencies for this enhancement.

## Documentation Updated/Created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle updated the Fee Basis User Manual (fb3_5_um) and PIMS ADT Registration User Manual (dg_5_3_reg_um).

## Existing Issues and Workarounds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA MUST BE USED for this process. DO NOT use FBCS. Until FBCS can process Newborn claims, follow your local facility's VistA procedures.

### From: DG*5.3*952 Release Notes

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new OTH ELIGIBILITY PATIENT file (#33) was created. This file contains data required for tracking the status of the eligibility for emergency mental health care for patients with Other Than Honorable (OTH) discharge type.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Other Than Honorable (OTH) software provides new VISTA options. The OTH options are in the Other Than Honorable Patient's Menu \[DG OTH MENU\] found in the Registration menu \[DG REGISTRATION MENU\]. The Other Than Honorable Patient's Menu \[DG OTH MENU\] contains the following options:

- OTH Management \[DG OTH MANAGEMENT\]
- This option is used to perform various action related to OTH patients.

> Screen Actions

| Synonym | Action Name          | Description                                                                        |
|---------|----------------------|------------------------------------------------------------------------------------|
| AP      | Add 90 day period    | Allow user to enter approved/pending/denied 90-Day period on a single OTH patient. |
| VD      | View denied requests | Display the 90-Day period denied request history for the selected patient.         |
| SD      | Show request details | Display the 90-Day period request details history for the selected patient.        |
| VA      | View appr. requests  | Display the 90-Day period approved request for the selected patient.               |
| PI      | Patient inquiry      | Allow user to do an inquiry on a single OTH patient.                               |
| PR      | Show pending request | Display the 90-Day period pending request for the selected patient.                |

- Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\]
- This option is used to do an inquiry on a single OTH patient.
- Other Than Honorable Reports \[DG OTH REPORTS MENU\]
- This option manages Other Than Honorable patient reports. The Other Than Honorable Reports available to run are:
- Tracking Report (OTH-90) \[DG OTH 90-DAY PERIOD\]
- This option is used to print a listing of all OTH-90 patients with ACTIVE or EXPIRED 90-Day period of care for a user-specified selected date range. Those OTH-90 patients that have been adjudicated, entered in error, or the Expanded MH Care Type is changed from OTH-90 to a different factor type, will not be displayed in this report.
- Statistical Report (OTH-90) \[DG OTH STATISTICAL REPORT\]
- This option used to print a listing of all OTH-90 patients with ACTIVE or EXPIRED 90-Day periods of care, have been adjudicated, entered in error, or the Expanded MH Care Type is changed from OTH-90 to a different Expanded MH Care Type.
- Authorization Reports (OTH-90) \[DG OTH OTH90 AUTH REPORTS\]
- This option is used to display Authorizations that were approved, denied, and pending.
- Other Than Honorable MH Status Report \[DG OTH MH STATUS REPORT\]
- This option is used to display the status and history of the OTH patient.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new routine DGOTHBTN will supply CPRS with lines of text to be displayed on the EMERGENT MH OTH (OTH-90) button, hover over, and pop-up screen.

### Integration Control Registry \[ICRs\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new ICR# 6873 was created to facilitate the retrieval of the Other Than Honorable (OTH) eligibility status for a selected patient to display the information in the CPRS header. There are two OTH categories (EMERGENT MH OTH and EXTENDED MH OTH). The OTH status is calculated based on the date stored in the PATIENT file (#2) and OTH ELIGIBILITY PATIENT file (#33).

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The PATIENT file (#2) has a new field \#.5501 "EXPANDED MH CARE TYPE" which indicates the expanded mental health care authority under which the patient should be treated.
- New set of code "OTH-90 (EMERGENT OTH) " has been added to PATIENT file (#2) field \#.5501 to be used as expanded mental health care type justifying the EXPANDED MH CARE eligibility.
- The new "EXPANDED MH CARE NON-ENROLLEE" eligibility has been added to MAS ELIGIBILITY CODE file (#8.1) and ELIGIBILITY CODE file (#8) to be used as primary eligibility for OTH patients.
- The number range in the VA CODE NUMBER field \#3 in MAS ELIGIBILITY CODE file (#8.1) and ELIGIBILITY CODE file (#8) has been updated from 1-10 to 1-99. This is to accommodate the primary eligibility EXPANDED MH CARE NON-ENROLLEE.
- The PATIENT ENROLLMENT file (#27.11) has a new field to record the EXPANDED MH CARE TYPE associated with the enrollment priority determination.
- The INCONSISTENT DATA ELEMENTS file (#38.6) has been updated to add new inconsistency checks on Patient Type. If Patient Type is incompatible with the Primary Eligibility of EXPANDED MH CARE NON-ENROLLEE, then inconsistency \#89 is displayed in the inconsistency checks screen.
- The PERIOD OF SERVICE file (#21) has been updated to add the EXPANDED MH CARE NON-ENROLLEE eligibility.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VISTA Registration Screen 7 option was updated. The OTH patients will be registered (in VISTA Registration Screen 7) using the new Primary Eligibility of EXPANDED MH CARE NON-ENROLLEE.  Once that Primary Eligibility EXPANDED MH CARE NON-ENROLLEE is selected, the system will prompt the EXPANDED MH CARE TYPE that allow the registration specialist to select which of the OTH eligibilities the patient qualifies for.

- EXPANDED MH CARE TYPE.  This entry is the descriptor for the primary eligibility code for Other Than Honorable (OTH) patients seeking mental health care services while awaiting VBA adjudication.
  a.  EMERGENT MH OTH

  Note: This prompt will only display when the user enters EXPANDED MH CARE NON-

                  VETERANS as the patient's primary eligibility.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines that handle that VISTA Registration Screen 7 was updated to prompt the EXPANDED MH CARE TYPE if primary eligibility is EXPANDED MH CARE NON-ENROLLEE.

### Input Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DG LOAD SCREEN 7 FILE \#2 has been updated to prompt the EXPANDED MH CARE TYPE if primary eligibility is EXPANDED MH CARE NON-ENROLLEE.

### From: DG*5.3*1008 Release Notes

### List of Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch makes the following enhancements to VistA REE:

1.  One existing profile has been renamed and updated in the HEALTH BENEFIT PLAN file (#25.11): ACTIVE DUTY AND TRICARE SHARING AGREEMENT
2.  Seven new profiles have been added to the HEALTH BENEFIT PLAN file (#25.11). The data is provided in the build with the full data dictionary of the HEALTH BENEFIT PLAN file (#25.11).
    - VA DOD DIRECT RESOURCE SHARING AGREEMENTS
    - STATE VETERAN HOME
    - EMPLOYEE VETERAN
    - OWCP
    - VETERAN PLAN CCP RESTRICTED CARE
    - VETERAN PLAN CCP ENTITLED CARE
    - COLLATERAL OF VETERAN OTHER
3.  Description updates have been corrected for the VHAP long descriptions. The errors were discovered internally by development and SQA.
- BENEFICIARY NEWBORN
  - The indentation has been removed for "Newborn:"
- BENEFICIARY CHAMPVA
  - Capitalization has been added:
  - "Permanently and Totally disabled (P&T)"
  - "CHAMPVA pays secondary to any Other Health Insurance (OHI)"
- CAREGIVER SECONDARY FAMILY
  - The quotation mark has been removed:
  - "is an individual approved as a provider of"
- APPLICANT IN PROCESS
  - The verb "are" has been added: "enrollment and are still within"
- OTHER FEDERAL AGENCY
  - The acronym has been corrected: "Sharing Agreement (excludes DoD)"
- VETERAN FULL MED BENEFITS TX GMT COPAY REQ AND COPAY EXMT 6
  - The plural noun has been changed to singular: "following condition:"
- VETERAN FULL MED BENEFITS TX GMT AND RX COPAY REQ 6
  - The plural noun has been changed to singular: "following condition:"
- VETERAN FULL MED BENEFITS TX AND RX COPAY EXMT 6
  - The plural noun has been changed to singular: "following condition:"
  - A blank line has been added at line number 15.
- VETERAN FULL MED BENEFITS TX COPAY EXMT AND RX COPAY REQ 6
  - The plural noun has been changed to singular: "following condition:"
- DENTAL FOCUSED EMERGENT CARE: The indentation now matches the RSD.
- INELIGIBLE: "no" has been changed to "non": "to non receipt"
- ASSISTED REPRODUCTIVE TECHNOLOGY: The short description has been changed from "FMP" to "ART"
- VETERAN PLAN CCP RESTRICTED CARE
  - Long description text added beginning with: "or Veteran who was discharged or released from active"

### From: DG*5.3*903 Release Notes

## Installation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must verify that Registration patches, DG\*5.3\*343, DG\*5.3\*574, DG\*5.3\*855, and DG\*5.3\*867 are properly installed on your system before you install DG\*5.3\*903.

### Minimum Package Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following minimum package versions are required to install VistA Registration V.5.3:

| MINIMUM VERSION BASELINE |          |
|------------------------------|----------|
| VA FileMan                   | V.21.0   |
| Kernel                       | V.8.0    |
| Kernel Toolkit               | V.7.3    |
| VA MailMan                   | V.7.1    |
| CPRS                         | V.28     |
| PXRM                         | V.2.0.18 |
| PCE                          | V.1.0    |
| IB                           | V.2.0    |
| IFCAP                        | V.3.0    |
| DRG Grouper                  | V.13.0   |
| HL7                          | V.1.6    |
| Generic Code Sheet           | V.1.5    |

> For more information, please see the PIMS Installation Guide on the VistA Document Library at: <http://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/pimsig.pdf>

### Release Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Increase Engagement in My HealtheVet enhancement patch, DG\*5.3\*903, is released in FORUM.

## Fields Added to the PATIENT (#2) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new fields were added to the PATIENT (#2) file. The increased size of the Patient file, due to these new fields, should not be significant, but the file will increase as more Veterans register in My HealtheVet.

- MHV SOCIALIZATION (#537026)
- MHV REGISTERED (#537027)
- MHV AUTHENTICATED (#537028)
- MHV SECURE MESSAGING (#537029)
- MHVREG UPDATE DATE/TIME (#537030)
- MHVAUTH UPDATE DATE/TIME (#537031)
- MHVSM UPDATE DATE/TIME (#537032)
- MHV REGISTER DECLINED TEXT (#537033)
- MHV AUTH DECLINED TEXT (#537034)
- MHV MSG DECLINED TEXT (#537035)
- MHV REGISTER DECLINED REASON (#537036)
- MHV AUTH DECLINED REASON (#537037)
- MHV MSG DECLINED REASON (#537038)
- MHV MSG ACTIONS (#537041)
- MHV AUTH ACTIONS (537042)

## Fields Added to the MHV SOCIALIZATION Multiple of the PATIENT (#2) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new fields were added to the MHV SOCIALIZATION multiple of the PATIENT (#2) file:

- SOCIALIZATION DATE (#.01)
- SOCIALIZATION RESPONSE (#1)
- SOCIALIZATION ACTIONS (#2)

## Fields Added to the MHV SOCIALIZATION (#390.01) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new fields were added to the MHV SOCIALIZATION (#390.01) file:

- NAME (#.01)
- DISPLAY SEQUENCE (#1)
- DISPLAY TEXT (#1.5)
- PATIENT TEXT (#2)
- FOLLOWUP ACTION (#3)

## Fields Added to the MHV SOCIALIZATION ACTIONS (#390.02) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new fields were added to the MHV SOCIALIZATION ACTIONS (#390.02) file:

- ACTION (#.01)
- SELECTABLE LOCATIONS (#1)
- DISPLAY TEXT (#3)

## Fields Added to the MHV DECLINED REASONS (390.03) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new fields were added to the MHV DECLINED REASONS (#390.03) file:

- NAME (#.01)
- SELECTABLE AT (#1)

## Fields Added to the MHV ACTION SELECTION (#390.04) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields were added to the MHV ACTION SELECTION (#390.04) file:

- NAME (#.01)
- DESCRIPTION (#1)

## Fields Added to the MAS PARAMETERS (#43) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new field was added to the MAS PARAMETERS (#43) file:

- ENABLE MY HEALTHEVET PROMPTS? (#1100.07)

### From: DG*5.3*1104 Release Notes

## Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Those with questions should reach out to their local COMPACT Act Coordinator.

Template Revision History

| Date          | Version | Description                                                                                                                             | Author                                |
|---------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| August 2019   | 2.0     | Updated to align with current OIT Documentation Standards and to conform with current Section 508 guidelines; revised to show new links | OIT Documentation Standards Committee |
| July 2016     | 1.1     | Updated instructional text to simplify content.                                                                                         | OIT Documentation Standards Committee |
| November 2015 | 1.0     | Initial draft                                                                                                                           | OIT Documentation Standards Committee |

Template Revision History showing date template was created or revised, version number, description, and author.

### From: DG*5.3*1012 Release Notes

## Technical Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch makes the following enhancements to VistA REE:

1.  A new HISTORIC KATRINA ERI (#.182) field is added in the PATIENT (#2) file. This field will be used to store the historic Hurricane Katrina Emergency Response Indicator for a patient.

> DATA NAME GLOBAL DATA

> ELEMENT TITLE LOCATION TYPE

> ---------------------------------------------------------------

> 2,.182 HISTORIC KATRINA ERI KATR;1 SET

> 'K' FOR HURRICANE KATRINA;

> LAST EDITED: APR 01, 2020

> HELP-PROMPT: Enter the appropriate ER Indicator to

> identify patients from impacted zip

> code areas designated by FEMA.

> DESCRIPTION: This is the historic Hurricane Katrina

> Emergency Response Indicator for a

> patient.

> CROSS-REFERENCE: 2^KATRI

> 1)= S ^DPT("KATRI",\$E(X,1,30),DA)=""

> 2)= K ^DPT("KATRI",\$E(X,1,30),DA)

> KATRI cross reference is used for look

> up of historic Hurricane Katrina

> Emergency Response Indicator

> patients.

2.  Patients (DFNs) temporarily stored in the ^XTMP("DG531011P") global by patch DG\*5.3\*1011 had an Emergency Response Indicator (ERI) of 'HURRICANE KATRINA'. For historical purposes, the post-install of this patch will automatically task off a job to now file this data back into the patient's record. It will be stored in the new HISTORIC KATRINA ERI (#.182) field of the PATIENT (#2) file.

Once the job is complete, a MailMan message will be sent to the patch installer containing the results.

3.  Note: Post-Installation routine DG531012P is included in the DG\*5.3\*1012 build. No other routines are included in the build.

### From: DG*5.3*1016 Release Notes

## Enhancement and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch DG\*5.3\*1016 makes the following enhancements and fixes to the code released by its predecessors DG\*5.3\*952 and DG\*5.3\*977:

- Provides a fix to ensure 'Reevaluate Eligibility' Mailman messages sent to DGEN ELIGIBILITY ALERT group are sent only for patients registered as 'OTH' patients, per the defined business scenario.
- Provides enhancement to the 'Reevaluate Eligibility' Mailman message to be sent to DGEN ELIGIBILITY ALERT group for patients first registered as NON-OTH patients and screened positively for MST, but whose registration then changed to OTH and subsequent MST re-screening resulting in an MST STATUS (#3) value in the MST HISTORY FILE (#29.11) of "No, Screened does not report MST" or "Screened Declines to answer".

  Note: the patch adds a new field AUTOMATIC CHANGE DATE field (#.5502) in the PATIENT file (#2) to capture the time when date/time of automatic change of Mental Health (MH) care type.
- Provides a fix to ensure that the Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\] option displays an ACTIVE OTH status if the patient transitions from OTH Emergent to OTH Extended.
- Provides a fix to ensure that the Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\] option displays the correct current Primary Eligibility.

### From: DG*5.3*976 Release Notes

### May 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Department of Veterans Affairs Office of Information and Technology (OIT)
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
