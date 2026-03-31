---
title: One Consult - Order to Consult - Admin Key Reporting Technical Training Guide
doc_type: TRG
doc_label: Training Guide
doc_layer: plain
doc_subject: One Consult - Order to Consult - Admin Key Reporting Technical
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - consult
  - admin
  - prompt
  - order
  - table
  - community
  - care
  - contents
  - administrative
  - security
page_count: 0
word_count: 685
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2018
revision_count: 1
revision_newest: 12/07/2018
revision_oldest: 12/07/2018
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/oc_adminkey_tech_tg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/oc_adminkey_tech_tg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>One Consult - Order to Consult – Admin Key Reporting

  Software Version 1.0.03

  Technical Training Guide
---

![](one-consult-order-to-consult-admin-key-reporting-technical-training-guide/001.png)

December 2018

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description              | Author   |
|------------|----------|--------------------------|----------|
| 12/07/2018 | 1.0      | Initial Document Release | AbleVets |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Assigning the OR ADMIN RPB TO CC Key to a User](#assigning-the-or-admin-rpb-to-cc-key-to-a-user)
  - [Provide Access to the Consult](#provide-access-to-the-consult)
<span id="_Toc526948464" class="anchor"></span>This guide provides instructions on how to set up OR ADMIN RBP TO CC CPRS users so that they can use the Administratively Released by Policy functionality for COMMUNITY CARE -ADMIN and -DS consults. Setup requires assignment of the OR ADMIN RBP TO CC security key to CPRS users as well as assigning the ADMINISTRATIVE UPDATE USER role to applicable COMMUNITY CARE -ADMIN and -DS consults as determined by the users role. The OR ADMIN RBP TO CC key is not exclusive and may be assigned as the sole key for a user or in conjunction with another security key (usually the OREMAS key).
CPRS users who hold the security key OR ADMIN RBP TO CC are able to create and release a Community Care direct schedule or administrative consult orders without possessing the ORES provider security key. The consults service order will start with Community Care (case-insensitive), and contain either –DS or –ADMIN (case insensitive). The consult order will be auto-signed as "Administratively Released by Policy" and released to the service as soon as the order has been accepted. The consult order will appear on the Orders tab with status "pending".

## Assigning the OR ADMIN RPB TO CC Key to a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions are required for any CPRS user needing the Administratively Released by Policy functionality for Community Care administrative or direct schedule consults. The users need to have the OR ADMIN RBP TO CC security key assigned in order to create an administrative or direct schedule consult to be released to Community Care without the need to have a provider sign the order. In order to assign the OR ADMIN RPB TO CC key to a user, the user must update File \#200 (New Person) with the key as follows:

1.  At the Select OPTION NAME: prompt, enter XUKEYMGMT.

> Select OPTION NAME: XUKEYMGMT Key Management

> Allocation of Security Keys

> De-allocation of Security Keys

> Enter/Edit of Security Keys

> All the Keys a User Needs

> Allocate/De-Allocate Exclusive Key(s)

> Change user's allocated keys to delegated keys

> Delegate keys

> Keys For a Given Menu Tree

> List users holding a certain key

> Remove delegated keys

> Show the keys of a particular user

2.  At the Select Key Management \<Account\> Option: prompt, enter ALL.

> Select Key Management \<TEST ACCOUNT\> Option: ALL

> 1 All the Keys a User Needs

> 2 Allocate/De-Allocate Exclusive Key(s)

> 3 Allocation of Security Keys

3.  At the CHOOSE 1-3: prompt, enter 3.

> CHOOSE 1-3: 3 Allocation of Security Keys

4.  At the Allocate Key: prompt, enter OR ADMIN RBP TO CC.

> Allocate key: OR ADMIN RBP TO CC

> Another key:

5.  At the Holder of key: prompt, enter \<USER NAME\>.

> Holder of key: TESTUSER,ADMINKEY TUAK

> Another holder:

> You've selected the following keys:

> OR ADMIN RBP TO CC

> You've selected the following holders:

> TESTUSER,ADMINKEY

6.  After confirming the Key and the User, at the Do you wish to proceed? prompt, enter YES.

> You are allocating keys. Do you wish to proceed? YES//

> OR ADMIN RBP TO CC being assigned to:

> TESTUSER,ADMINKEY

1.  The Admin Key is not an exclusive security key and may be assigned in conjunction with other security keys. It is expected that the Admin Key will often be required in conjunction with the OREMAS key.

## Provide Access to the Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to assigning the OR ADMIN RBP TO CC key to the user, each user will need to be added as an ADMINISTRATIVE UPDATE USER for each applicable Community Care Admin and DS consult as required for their role. Note that applicable consult types meet both of the following criteria:

- The Consult title contains Community Care (not case sensitive) -and- the Consult title contains -ADMIN (case sensitive).
- The consult title contains Community Care (not case sensitive) -and- the consult title contains -DS (case sensitive).

The Administrative user must update each applicable consult as follows:

1.  At the OPTION NAME: prompt, enter GMRC MGR.

> Select OPTION NAME: GMRC MGR       Consult Management

>    RPT    Consult Tracking Reports ...

>    SS     Set up Consult Services

>    SU     Service User Management

>    CS     Consult Service Tracking

>    RX     Pharmacy TPN Consults

>    GU     Group update of consult/procedure requests

>    UA     Determine users' update authority

>    UN     Determine if user is notification recipient

>    NR     Determine notification recipients for a service

>    TD     Test Default Reason for Request

>    LH     List Consult Service Hierarchy

>    PR     Setup procedures

>    CP     Copy Prosthetics services

>    CCT    Menu for Closure Tools ...

>    DS     Duplicate Sub-Service

>    FS     Define Fee Services

>    IFC    IFC Management Menu ...

>    TP     Print Test Page

> You have PENDING ALERTS

>           Enter  "VA to jump to VIEW ALERTS option

> You've got PRIORITY mail!

7.  At the Select Consult Management \<ACCOUNT\> Option: prompt, enter SS (setup consult services).

> Select Consult Management \<TEST ACCOUNT\> Option: SS  Set up Consult Services

8.  At the Select Service/Specialty: prompt, enter \<CONSULT NAME\>.

> Select Service/Specialty: COMMUNITY CARE-ADMIN-CARDIAC      

> SERVICE NAME: COMMUNITY CARE-ADMIN-CARDIAC  Replace

> ABBREVIATED PRINT NAME (Optional): CCAC//

> INTERNAL NAME:

> Select SYNONYM: ADMIN RELEASE TO CARDIAC//

> SERVICE USAGE:

> SERVICE PRINTER:

> SECONDARY PRINTER:

> NOTIFY SERVICE ON DC:

> REPRINT 513 ON DC:

> PREREQUISITE:

9.  At the Edit? prompt, enter NO.

> Edit? NO//

> PROVISIONAL DX PROMPT:

> PROVISIONAL DX INPUT:

> DEFAULT REASON FOR REQUEST:

10. At the Edit? prompt, enter NO.

>   Edit? NO//

> RESTRICT DEFAULT REASON EDIT:

> Inter-facility information

> IFC ROUTING SITE:

> IFC REMOTE NAME:

> Select IFC SENDING FACILITY:

> SERVICE INDIVIDUAL TO NOTIFY:

> Select SERVICE TEAM TO NOTIFY:

> Select NOTIFICATION BY PT LOCATION:

> PROCESS PARENTS FOR NOTIFS:

> Select UPDATE USERS W/O NOTIFICATIONS:

> Select ADMINISTRATIVE UPDATE USER:

11. At the Select ADMINISTRATIVE UPDATE USER: prompt, enter \<User Name\>.

Select ADMINISTRATIVE UPDATE USER: CPRSADMINUSER,ONE