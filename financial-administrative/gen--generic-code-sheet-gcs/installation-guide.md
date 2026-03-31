---
title: GCS Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: GEN
app_name: Generic Code Sheet (GCS)
section: FIN
app_status: active
pkg_ns: GEN
patch_ver: 2
patch_id: GEN*2
group_key: "GEN:GEN:2"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Installation](#installation) - [Step 1. Print local modifications (optional)](#step-1-print-local-modifications-optional) - [Step 2. Users off the system (optional)](#step-2-users-off-the-system-optional) - [Step 3. Remove version 1.5 routines (mandatory)](#step-3-remove-version-15-routines-manda
audience: 
keywords: 
  - mail
  - filed
  - domain
  - router
  - batch
  - step
  - gecs
  - code
  - error
  - checking
page_count: 0
word_count: 2548
section_count: 11
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 2
revision_newest: 12/22/04
revision_oldest: 12/22/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2inst.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2inst.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=7"
---

Decentralized Hospital Computer Program

GENERIC CODE SHEETINSTALLATION GUIDE

March 1995

Information Systems Center

Washington, D.C.

Table of Contents

Installation

Step 1. Print local modifications (optional)

Step 2. Users off the system (optional)

Step 3. Remove version 1.5 routines (mandatory)

Step 4. Load version 2.0 routines (mandatory)

Step 5. Set up programming environment (mandatory)

Step 6. Initialize version 2.0 (mandatory)

Step 7. Move version 2.0 routines to all systems (mandatory)

Step 8. Fix any mail group errors (mandatory)

Step 9. Remove initialization routines (optional)

Step 10. Remake local modifications (optional)

Revision History

Initiated on 12/22/04

|          |                                                                  |                 |                  |
|----------|------------------------------------------------------------------|-----------------|------------------|
| Date     | Description (Patch \# if applic.)                                | Project Manager | Technical Writer |
| 12/22/04 | Updated to comply with SOP 192-352 Displaying Sensitive Data.    |                 | REDACTED         |
| 12/22/04 | Pdf file checked for accessibility to readers with disabilities. |                 | REDACTED         |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |

# Installation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation](#installation)
  - [Step 1. Print local modifications (optional)](#step-1-print-local-modifications-optional)
  - [Step 2. Users off the system (optional)](#step-2-users-off-the-system-optional)
  - [Step 3. Remove version 1.5 routines (mandatory)](#step-3-remove-version-15-routines-mandatory)
  - [Step 4. Load version 2.0 routines (mandatory)](#step-4-load-version-20-routines-mandatory)
  - [Step 5. Set up programming environment (mandatory)](#step-5-set-up-programming-environment-mandatory)
  - [Step 6. Initialize Version 2.0 (mandatory)](#step-6-initialize-version-20-mandatory)
  - [Step 7. Move version 2.0 routines to all systems (mandatory)](#step-7-move-version-20-routines-to-all-systems-mandatory)
  - [Step 8. Fix any mail group errors (mandatory)](#step-8-fix-any-mail-group-errors-mandatory)
  - [Step 9. Remove initialization routines (optional)](#step-9-remove-initialization-routines-optional)
  - [Step 10. Remake local modifications (optional)](#step-10-remake-local-modifications-optional)
*The SF CIO Field Office added hard page breaks to this document to keep the paging the same when the document was transferred and converted to a different version of MS Word. The TOC was also adjusted to coincide with the original version of this document. No other text/content changes were made.*
The following installation instructions and examples should be used for installing Generic Code Sheet Version 2.0. In order to ensure proper installation, follow each step carefully and in the order as they appear below.

## Step 1. Print local modifications (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post initialization routine will move the code sheets under the correct batch types as distributed by the Generic Code Sheet package. If your site has made any local modifications placing code sheets under different batch types, it will be necessary to print a listing of the code sheets and batch types using VA FileMan in order to remake the local modifications after installation.

Below is an example of printing the code sheets under the batch types:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>VA FileMan 20.0</p>
<p>Select OPTION: <strong>PRINT FILE ENTRIES</strong></p>
<p>OUTPUT FROM WHAT FILE: GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT// <strong>&lt;RET&gt;</strong></p>
<p>SORT BY: NAME// <strong>BATCH TYPE;S1</strong></p>
<p>START WITH BATCH TYPE: FIRST// <strong>&lt;RET&gt;</strong></p>
<p>WITHIN BATCH TYPE, SORT BY: <strong>&lt;RET&gt;</strong></p>
<p>FIRST PRINT FIELD: <strong>.01</strong> NAME</p>
<p>THEN PRINT FIELD: <strong>2</strong> GENERAL PURPOSE</p>
<p>THEN PRINT FIELD: <strong>&lt;RET&gt;</strong></p>
<p>HEADING: GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT LIST</p>
<p>Replace <strong>&lt;RET&gt;</strong></p>
<p>DEVICE: LAT RIGHT MARGIN: 80//<strong>&lt;RET&gt;</strong></p>
<p>...HMMM, JUST A MOMENT PLEASE...</p>
<p>GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT LIST JAN 4,1995 11:10 PAGE 1</p>
<p>NAME GENERAL PURPOSE</p>
<p>-------------------------------------------------------------------------------</p>
<p>BATCH TYPE: ACCOUNTS RECEIVABLE</p>
<p>243 CAT C - NSC VET NHC</p>
<p>244 CAT C - NSC OUTPATIENT CARE</p>
<p>245 CAT C - NSC HOSPITAL CARE</p>
<p>246 WORKMAN'S COMPENSATION CARE</p>
<p>247 NO FAULT MOTOR VEHICLE ACCIDENT CARE</p>
<p>248 CRIME OF PERSONAL VIOLENCE</p>
<p>249 NSC W/HEALTH INSURANCE (OPT)</p>
<p>251 INELIGIBLE HOSPITALIZATION AND TREATMENT</p>
<p>252 EMERGENCY HOSPITALIZATION</p>
<p>253 BREACHED CAREER RESIDENCY CONTRACTS</p>
<p>254 BREECHED OBLIGATED SERVICE AGREEMENT</p>
<p>292 SC VET TREAT NSC CON (INPT)</p>
<p>293 SC VET TREAT NSC CON (OPT)</p>
<p>294 MEDS FURNISHED OPT CARE, RX CO-PAY (NSC)</p>
<p>295 $10 PER DAY HOSPITAL CARE</p>
<p>296 $5 PER DAY NHCU CARE</p>
<p>297 NSC VET W/HEALTH INSURANCE (INPT)</p>
<p>298 MEDS FURNISHED OPT CARE, RX CO-PAY (SC)</p>
<p>BATCH TYPE: BUILDING MANAGEMENT</p>
<p>220 BMS Contracted Hours</p>
<p>217 BMS Staff Hours Worked</p>
<p>218 BMS Environmental Care Operations</p>
<p>219 BMS Textile Care Operations</p>
<p>BATCH TYPE: CHAPLAIN</p>
<p>141 Chaplain Service Monthly Code Sheet</p>
<p>142 Chaplain's Fund</p></td>
</tr>
</tbody>
</table>

## Step 2. Users off the system (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure no Generic Code Sheet users are on the system. This is not critical and will not cause damage to the database. This will only be a nuisance to the users if they are using the package during the installation of Version 2.0. If users are in the Generic Code Sheet package during installation, they will error out with no program or line errors. After installation, the user will be able to continue with the option they were using when they received the error.

## Step 3. Remove version 1.5 routines (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delete all GEC\* routines from all systems.

## Step 4. Load version 2.0 routines (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load the Version 2.0 Generic Code Sheet GEC\* routines onto the system containing the ^DD global. It is not necessary for the routines to be loaded on the system containing the ^DD global, but the initialization will run faster.

## Step 5. Set up programming environment (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From programmer mode, kill all variables and run the routine XUP to set up your DUZ variables.

\>K

\>D ^XUP

Setting up programmer environment

Access Code:

Terminal Type set to: C-VT100

Select OPTION NAME: ^

\>

## Step 6. Initialize Version 2.0 (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From programmer mode, run the Generic Code Sheet Version 2.0 initialization routine GECINIT. While the initialization routine is running, step 7 can be performed.

\>D ^GECINIT

This version (#2.0) of 'GECINIT' was created on 09-DEC-1994

(at IFA, by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

2100 GENERIC CODE SHEET

> **NOTE:** You already have the 'GENERIC CODE SHEET' File.

2100.1 GENERIC CODE SHEET STACK

> **NOTE:** You already have the 'GENERIC CODE SHEET STACK' File.

2101.1 GENERIC CODE SHEET BATCH TYPE (including data)

> **NOTE:** You already have the 'GENERIC CODE SHEET BATCH TYPE' File.

I will OVERWRITE your data with mine.

2101.2 GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT (including data)

> **NOTE:** You already have the 'GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT' File.

I will OVERWRITE your data with mine.

2101.3 GENERIC CODE SHEET TRANSMISSION RECORD

> **NOTE:** You already have the 'GENERIC CODE SHEET TRANSMISSION RECORD' File.

2101.4 GENERIC CODE SHEET TEMPLATE MAPS (not used)

> **NOTE:** You already have the 'GENERIC CODE SHEET TEMPLATE MAPS (not used)' File.

2101.5 GENERIC CODE SHEET COUNTER

> **NOTE:** You already have the 'GENERIC CODE SHEET COUNTER' File.

2101.6 GENERIC CODE SHEET LOCK

> **NOTE:** You already have the 'GENERIC CODE SHEET LOCK' File.

2101.7 GENERIC CODE SHEET SITE

> **NOTE:** You already have the 'GENERIC CODE SHEET SITE' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// YES (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// YES

ARE YOU SURE EVERYTHING'S OK? NO// YES

...HMMM, THIS MAY TAKE A FEW MOMENTS.........................................

.............................................................................

.............................................................................

.............................................................................

.............................................................................

.............................................................................

.............................................................................

.............................................................................

.............................................................................

........................................................

'GECQ 1-DAY PICKUP CODES' Help Frame filed.

'GECQ 2-DAY PICKUP CODES' Help Frame filed.

'GECQ 3-DAY PICKUP CODES' Help Frame filed.

'GECQ 4-DAY PICKUP CODES' Help Frame filed.

'GECQ 5-DAY PICKUP CODES' Help Frame filed.

'GECQ 6-DAY PICKUP CODES' Help Frame filed.

'GECQ 7-DAY PICKUP CODES' Help Frame filed.

'GECQ PICKUP CODES' Help Frame filed.........................................

..........

'GECO GECS BATCH' Option Filed

'GECO GECS BATCH EDIT' Option Filed

'GECO GECS BATCHES STATUS' Option Filed

'GECO GECS BATCHES WAITING TRAN' Option Filed

'GECO GECS CODE EDIT' Option Filed

'GECO GECS CREATE' Option Filed

'GECO GECS DELETE' Option Filed

'GECO GECS KEYPUNCH' Option Filed

'GECO GECS MAIN MENU' Option Filed

'GECO GECS MAINTENANCE USER MEN' Option Filed

'GECO GECS PURGE' Option Filed

'GECO GECS READY FOR BATCHING L' Option Filed

'GECO GECS REBATCH' Option Filed

'GECO GECS REPORTS MENU' Option Filed

'GECO GECS RETRANSMIT' Option Filed

'GECO GECS REVIEW CODE SHEET' Option Filed

'GECO GECS TRANSMIT' Option Filed

'GECO GECS TRANSMIT USER' Option Filed

'GECO GECS USER MENU' Option Filed

'GECS BATCH' Option Filed

'GECS BATCH EDIT' Option Filed

'GECS BATCHES STATUS' Option Filed

'GECS BATCHES WAITING TRANS' Option Filed

'GECS CODE EDIT' Option Filed

'GECS CREATE' Option Filed

'GECS DELETE' Option Filed

'GECS KEYPUNCH' Option Filed

'GECS MAIN MENU' Option Filed

'GECS MAINTENANCE MENU' Option Filed

'GECS MAINTENANCE USER MENU' Option Filed

'GECS PURGE' Option Filed

'GECS READY FOR BATCHING LIST' Option Filed

'GECS REBATCH' Option Filed

'GECS REPORTS MENU' Option Filed

'GECS RETRANSMIT' Option Filed

'GECS REVIEW CODE SHEET' Option Filed

'GECS SETUP' Option Filed

'GECS STACK MENU' Option Filed

'GECS STACK REPORT' Option Filed

'GECS STACK RETRANSMIT' Option Filed

'GECS STACK TRANSMIT TASKMAN' Option Filed

'GECS STACK USER COMMENTS’ Option Filed

‘GECS TRANSMIT' Option Filed

'GECS TRANSMIT USER' Option Filed

'GECS USER MENU' Option Filed..................................................

...............................................................................

...............................................................................

....................................

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

\[The Post-Initialization Routine Starts Here\]

-----------------------------------------------------------------------

checking batch type: ACCOUNTS RECEIVABLE

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: BUILDING MANAGEMENT

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: CHAPLAIN

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: CONSULTING/ATTENDING

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-CAA.VA.GOV'

\[NOT 'Q-AMD.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: DDCSS - MENTAL HEALTH

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-NPF.VA.GOV'

\[NOT 'Q-CEN.MED.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: DENTAL

-------------------------------------------------------------------------------

checking batch type: DIETETICS

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: FEE BASIS

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: FEE BASIS - GECO

-------------------------------------------------------------------------------

checking batch type: FEE BASIS - IFCAP

-------------------------------------------------------------------------------

checking batch type: FINANCIAL MANAGEMENT

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-FMS.VA.GOV' \[NOT ''\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: FORM REQUISITION - GECO

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-LOG.VA.GOV'

\[NOT 'Q-CAA.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: HOSPITAL BASED HOME CARE- GECO

-------------------------------------------------------------------------------

checking batch type: LAB

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: MAS

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: MEDICAL MEDIA

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: MEDICINE

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: MENTAL HEALTH

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: NURSING

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: PERSONNEL

-------------------------------------------------------------------------------

checking batch type: PERSONNEL:VACANT

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-PFV.VA.GOV'

\[NOT 'Q-RCV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: PHARMACY

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: PHYSICIAN RECRUIT/STAFF - GECO

-------------------------------------------------------------------------------

checking batch type: PROSTHETICS

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: RADIOLOGY

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: RECREATION

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: SECURITY/POLICE

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: SOCIAL WORK

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: STAFFING MANAGEMENT - GECO

-------------------------------------------------------------------------------

checking batch type: SURGERY

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-AMD.VA.GOV'

\[NOT 'Q-PFV.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: SWS (FOR VAF10-7946) - GECO

-------------------------------------------------------------------------------

checking batch type: SWS - GECO

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-RHC.VA.GOV'

\[NOT 'Q-NPF.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: VOLUNTARY

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-NST.VA.GOV'

\[NOT 'Q-LOG.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

-------------------------------------------------------------------------------

checking batch type: WAGE SURVEY - GECO

1\. ERROR -- DOMAIN MAIL ROUTER SHOULD EQUAL 'Q-WGE.VA.GOV'

\[NOT 'Q-NST.VA.GOV'\]

... FIXING DOMAIN MAIL ROUTER.

2\. ERROR -- THE MAIL GROUP 'WGE' NEEDS TO BE SET UP.

==================== \*\*\* INSTALLING PIMS 5.3 PATCH 47 \*\*\* ==================

Installing PIMS Patch DG\*5.3\*47, routine DGGECSB ... OK, DONE.

SPECIAL NOTE: If the Post-Initialization does not run to completion you may restart the Post-Initialization by running ^GECSVFY from programmer mode. If the Initialization does not get to the Post-Initialization routine, the INITs must be started over from the beginning.

## Step 7. Move version 2.0 routines to all systems (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the initialization routine is running, load the GECS\* routines onto all systems. The GECI\* initialization routines should not be loaded on all systems.

If you are running PIMS version 5.3 and receive the message "Installing PIMS patch DG\*5.3\*47 Routine DGGECSB" as shown at the end of the post-init in step 6 (the words "OK, DONE" will appear), the routine DGGECSB should be moved to all systems.

## Step 8. Fix any mail group errors (mandatory)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post initialization routine (which runs after the initialization routine in step 6) fixes any problems with the Generic Code Sheet package files. The only error which will not be fixed is the error showing which mail groups need to be set up. This error is shown on the last line of the initialization in step 6 above. It will be necessary to set up these mail groups shown in error if the code sheet relating to the mail group is being used by the station. If you are running a prior version of Generic Code Sheet, most of the mail groups are probably already set up.

You may run the post initialization as many times as you would like by running the routine GECSVFY. The routine GECSVFY will ask if you would like to check the  
batch types for errors, answer YES. Next it will ask you if you would like to fix any errors found. A NO response will print the report, a YES response will print the report and fix the error (except for the setting up of mail groups).

## Step 9. Remove initialization routines (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the initialization routine GECINIT has completed (step 6), delete the GECI\* routines from the system.

## Step 10. Remake local modifications (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has made any local modifications per step 1, reprint the code sheets under the batch types as shown in step 1 and remake the local modifications.