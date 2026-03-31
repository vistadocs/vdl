---
title: Mental Health Version 5.01 Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: 
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: "- [Preface](#preface) - [Package Security](#package-security) - [# Progress Notes](#progress-notes) - [Electronic Signature:](#electronic-signature) - [# Security Keys](#security-keys) - [# Menus](#menus) - [Option Assignment:](#option-assignment) - [Primary Menu Option:](#primary-menu-option) - [Se"
audience: 
keywords: 
  - mental
  - health
  - table
  - contents
  - security
  - access
  - progress
  - package
  - options
  - notes
page_count: 0
word_count: 1048
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/mh_sgv5.01.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/mh_sgv5.01.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

> ![](mental-health-version-5-01-security-guide/001.png)

> MENTAL HEALTH

> SECURITY GUIDE

> Version 5.01

> December 1994

> Department of Veterans Affairs

> Veterans Health Administration

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Package Security](#package-security)
- [# Progress Notes](#progress-notes)
  - [Electronic Signature:](#electronic-signature)
- [# Security Keys](#security-keys)
- [# Menus](#menus)
  - [Option Assignment:](#option-assignment)
  - [Primary Menu Option:](#primary-menu-option)
  - [Secondary Menu Option:](#secondary-menu-option)
- [# VA FileManager Access Codes](#va-filemanager-access-codes)
The Mental Health Package Security Guide Version 5.1 defines and discusses package security issues and the control of sensitive information related to this national software package. This document is not to be included in any Freedom of Information Act (FOIA) software releases.
Table of Contents
Preface [i](#preface)
Package Security [4](#package-security)
Progress Notes [5](#progress-notes)
Electronic Signature: [5](#electronic-signature)
Security Keys [6](#security-keys)
Menus [8](#menus)
Option Assignment: [8](#option-assignment)
Primary Menu Option: [8](#primary-menu-option)
Secondary Menu Option: [8](#secondary-menu-option)
VA FileManager Access Codes [10](#va-filemanager-access-codes)

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.0 security is provided through use of security keys, menu options, and Department of Veterans Affairs (VA) FileManager access codes.

The Mental Health package is designed to provide clinical and demographic patient information. Most options in the Mental Health package provide access to sensitive clinical information and are subject to the conditions of the Privacy Act of 1974. The chiefs of the clinical services (Psychiatry, Psychology, Social Work, and Nursing) in consultation with the application coordinator, should determine the user’s need to know and should assign security keys, options, and FileManager access codes appropriately.

The options that are not affected by the conditions of the Privacy Act are the options contained in the Vocational Rehabilitation menu and the Clerk-entered Tests option contained in the General Management menu.

# # Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Version 5.0 of the Mental Health package, the Progress Notes User menu option on the Clinical Record menu accesses the new Progress Notes package. PLEASE, reference the Progress Notes Package Security Guide V. 2.5 for instructions relating to Progress Note security.

\*WARNING: A signed progress note is considered a part of the Patient's legal record and MUST be safeguarded as such. A signed progress note must not be purged (deleted) except under unusual circumstances such as a court order and must be deleted by an authorized person.

Progress Notes cannot be viewed by clinicians until signed by the author. Then they are considered part of the patient's record and are treated as such.

## Electronic Signature:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Progress Notes users can electronically sign progress notes. Users have an electronic signature code and it is used interchangeably in Progress Notes, Order Entry, and IFCAP. The electronic signature code is similar to a user's access or verify code. It can be assigned by the Edit Electronic Signature Code option on the Progress Notes User Menu option that is in turn on the Clinical Record menu.

# # Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.0 uses security keys to enable access to specific options. Options that provide discipline specific functionality such as administration and interpretation of instruments or verification of diagnoses is restricted to qualified professionals through assignment of security keys.

Mental Health exports four (4) security keys: YSD, YSP, YSQ, and YSZ.

> YSD: YSD security key allows verification of the ICD9 diagnoses. Entry of a verified ICD9 diagnosis into the record requires the YSD key. The Chief of Psychiatry may authorize assignment of this key to clinicians. Note, although members of the Mental Health staff determine the existence of a medical problem, it is up to the clinician responsible for the medical care of the patient to verify the ICD9 diagnosis.

> YSP: YSP security key provides access to psychological test options and is required to receive computer psychology test results.

> The Chief of Psychology Service may authorize assignment of this key to the psychologists or authorized designee who meet the American Psychological Association guidelines for training in psychological tests.

> YSQ: YSQ security key allows verification of the DSM-III-R diagnoses. Entry of a verified DSM-III-R diagnosis into the record requires the YSQ key.

> The Chiefs of the Clinical Services may authorize assignment of this key to clinicians who are qualified to verify diagnoses.

> **NOTE:** Although many members of the Mental Health staff may recognize mental health symptoms and may know a patient's past psychiatric history and previous diagnoses, verification of DSM-III-R diagnoses is the responsibility of the patient's clinician.

> YSZ: YSZ security key allows technicians/aids to queue tests and/or interviews to be printed after the patient has completed the instrument.

> Chiefs of the Clinical Services may authorize assignment of this key to the appropriate personnel. Individual facilities may have a psychological laboratory or assessment area where a testing supervisor, who is not a psychologist, initiates administration of psychological tests and interviews. This key allows tests to be queued for printing at the time the test is completed. The testing supervisor has access to the printouts of test results only at the time the tests are initially administrated.

# # Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Option Assignment:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assignment of menus is very important. The Mental Health package includes options that provide managerial functionality, as well as options that are relevant to personnel with specific jobs. Care must be taken when assigning menus and security keys. The security has already been described. The Mental Health options are described below.

## Primary Menu Option: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary menu for Mental Health V. 5.0 is Mental Health \[YSUSER\] menu which is composed of five submenu options.

Menu Title

Clinical Record YSCLINRECORD

Patient-Administered Instruments YSPTINSTRU

Vocational Rehabilitation YSVOCATIONAL

General Management YSMANAGEMENT

Inpatient Features YSCENMAIN

## Secondary Menu Option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health package contains options that enable execution of managerial responsibilities. A secondary menu MHS Manager \[YSMANAGER\] has been created to restrict access to these managerial utilities. The MHS Manager \[YSMANAGER\] menu contains several utility options. This includes the Mental Health System Site Parameters \[YS SITE PARAMETERS\] option and the two new Instruments Restart Parameter options. The MHS Manager \[YSMANAGER\] menu should be used by the Mental Health Application Coordinator to define site-specific fields and to define teams, wards, and team rotation schedules for the Inpatient Features option of Mental Health.

> **NOTE:** Only individuals who are responsible for maintaining the Mental Health package should be assigned the MHS Manager \[YSMANAGER\] menu.

# # VA FileManager Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileManager Access Codes have been assigned to the Mental Health files. Every Mental Health employee who accesses a computer terminal will require the upper case “Y” code. This permits the recipient to read and update the Mental Health files. The lower case “y” allows deletion of data from the files; therefore, this access should be limited to supervisory personnel.

MENTAL HEALTH FILEMANAGER ACCESS CODES

DD RD WR DEL LAYGO

FILE NUMBER ACCESS ACCESS ACCESS ACCESS ACCESS

---------------------------------------------------------------------------------

MEDICAL RECORD 90 @ Y Y Y Y

PT. TEXT 99 @ Y Y Y Y

MH CLINICAL FILE 615 @ Y Y Y Y

MH WAIT LIST 617 @ Y Y Y Y

PROBLEM 620 @ Y y y y

INDICATOR 625 @ Y y y y

JOB BANK 624 @ Y Y Y Y

MH TEXT 605 @ Y Y @ Y

MENTAL HEALTH CENSUS 618 @ Y Y Y Y

MENTAL HEALTH TEAM 618.2. @ Y Y Y Y

COPYRIGHT HOLDER 601.3. @ Y y y y

INCOMPLETE PSYCH TEST PATIENT 601.4. @ Y Y Y Y

MH INSTRUMENT 601 @ Y y y y

PSYCH INSTRUMENT PATIENT 601.2. @ Y Y y Y

SECLUSION/RESTRAINT 615.2. @ Y Y y Y

S/R REASONS 615.5. @ Y y y y

S/R RELEASE CRITERIA 615.7. @ Y y y y

S/R ALTERNATIVES 615.8. @ Y y y y

S/R CATEGORY 615.6. @ Y y y y

S/R OBSERVATION CHECKLIST 615.9. @ Y y y y

DSM-III-R 627.5. @ Y y y y

DSM-III-R MODIFIERS 627.9. @ Y y y y

YSEXPERT 628 @ Y y y y

CRISIS NOTE DISPLAY 600.7. @ Y Y Y Y

MENTAL HEALTH SITE PARAMETERS 602 @ y y @ @

MENTAL HEALTH INPT 618.4. @ Y Y Y Y

DSM3 627 @ Y @ @ @

DIAGNOSTIC RESULTS - MENTAL HEALTH 627.8. @ Y Y Y Y

> **NOTE:** If the File Access Conversion Part 3 of Kernel has been run, the above FileManager Access Code scheme does not apply.