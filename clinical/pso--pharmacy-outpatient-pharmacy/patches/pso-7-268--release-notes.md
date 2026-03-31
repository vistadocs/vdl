---
title: PSO*7*268 FY07 Qtr 3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: FY07 Qtr 3
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*268
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - order
  - allergy
  - status
  - table
  - contents
  - drug
  - update
  - assessment
  - mail
page_count: 0
word_count: 2436
section_count: 9
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p268_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p268_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-268-fy07-qtr-3-release-notes/001.png)

Pharmacy FY07 Q3

Release Notes

PSO\*7\*268

July 2007

VistA Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
- [Patient Safety Issues](#patient-safety-issues)
  - [PSI-06-186 – Changing Dispense Drug and SIG](#psi-06-186-changing-dispense-drug-and-sig)
  - [PSI-06-184 - Enhancements for No Allergy Assessment](#psi-06-184-enhancements-for-no-allergy-assessment)
- [Miscellaneous Enhancements](#miscellaneous-enhancements)
  - [Service Reject Selection (HD172344)](#service-reject-selection-hd172344)
  - [Patient Eligibility Update (HD67512)](#patient-eligibility-update-hd67512)
  - [## Patient Status Update (HD188707)](#patient-status-update-hd188707)
  - [Patient Lookup Update (Enhancement)](#patient-lookup-update-enhancement)
  - [Mail Status Expiration Date Displayed (HD68535)](#mail-status-expiration-date-displayed-hd68535)
  - [## ## ## Cache Locking Issue (Enhancement)](#cache-locking-issue-enhancement)
The Pharmacy Fiscal Year 2007 Quarter 3 (FY07 Q3) release includes updates in PSO\*7\*268. Installation instructions are included in the PSO\*7\*268 patch description.
*(This page included for two-sided copying.)*

# Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FY07 Q3 release includes updates for Patient Safety Issues (PSIs) and miscellaneous enhancements.

# Patient Safety Issues 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following PSIs were addressed by patch PSO\*7\*268:

- PSI-06-186 - Changing dispense drug and SIG
- PSI-06-184 - Enhancements for No Allergy Assessment

## PSI-06-186 – Changing Dispense Drug and SIG 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When entering a new order using the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option, and answering “NO” to the prompt "Is this correct? YES//", the software allows the option to edit the dispense drug. It allows you to select any active drug from the DRUG file (#50) and accept the order even though the entered SIG is incorrect. This patch will not list all the active drugs for selection during dispense drug edit, but will list only those drugs that are tied to that orderable item in the DRUG file (#50). Changing the dispense drug and Sig should not change the medical treatment intent of the order. VHA Pharmacies must have local polices that address pharmacist changing Dispense Drug and SIG.

Previously, when the dispense drug is changed the software prompts "Do You want to Edit the SIG? NO//." To read the current SIG you may have to scroll the screen up. This patch will now display the current SIG along with the prompt "Do You want to Edit the SIG? YES//".

If the Outpatient Pharmacy site parameter “EDIT DRUG” is set to YES and the dispense drug is changed on an existing prescription, then the current Sig is displayed along with the prompt "Do You want to Edit the SIG? YES//."

Example:

You have changed the dispense drug from

AMOXAPINE 150MG TAB to AMOXAPINE 50MG TAB.

Current SIG: TAKE ONE TABLET BY MOUTH THREE TIMES A DAY FOR 10 DAYS WITH FOOD

Do You want to Edit the SIG? YES//

When finishing a pending order through the Outpatient Pharmacy application, the software allows the option to edit the orderable item and select a different dispense drug, but does not prompt you to change the SIG. This can lead to an incorrect SIG. This patch will now prompt "Do You want to Edit the SIG? YES//".

## PSI-06-184 - Enhancements for No Allergy Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes are included to make the pharmacist aware/act on prescriptions if they’re being entered/finished for a patient with no allergy assessment:

- At the same spot where checking for bad address, add a check for no allergy assessment and provide a message to the user. (When the user continues on, he could choose EA to enter allergy information, stop with that patient, or continue on with ordering or finishing). See example 1.
- Within the profile information, display “No Assessment Made” next to the allergy header (like “NKA” currently shows) – see Example 2.
- On the profile header, on the right side of the line with patient name where \<A\> currently shows in reverse video if the patient has any allergy/adverse reaction information on file, show \<NO ALLERGY ASSESSMENT\> in reverse video if no assessment has been done. See example 3.
- If the pharmacist proceeds with drug entry for a patient with no allergy assessment, prompt to intervene just as if there had been an allergy reaction and treat this like a critical interaction (e.g., require the user to choose to continue processing and if so, prompt for an intervention).  
  See Example 4.

> **NOTE:** When flagging is available in backdoor Outpatient Pharmacy for pending orders, procedurally sites can choose to flag pending orders for patients awaiting an allergy assessment.

Example 1 – *Patient Prescription Processing* option update:

Select Rx (Prescriptions) Option: PATient Prescription Processing

Select PATIENT NAME: OPPATIENT16,ONE OPPATIENT16,ONE 4-3-41 000246802

YES SC VETERAN

OPPATIENT16,ONE (000-24-6802)

No Allergy Assessment!

Press Return to continue:

Eligibility: SC

RX PATIENT STATUS: SERVICE CONNECTED// \<Enter\>

Example 2 – *Patient Prescription Processing* option update (Patient Information screen):

Patient Information May 01, 2007@12:12:12 Page: 1 of 1

OPPATIENT16,ONE <span class="mark">\<NO ALLERGY ASSESSMENT\></span>

PID: 000-24-6802 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: SEP 7,1952 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

--------------------------------------------------------------------------------

Eligibility: SC LESS THAN 50% SC%: 30

Disabilities:

101 ANYPLACE ST

OZONE PARK, NY

12345

PHONE:

Prescription Mail Delivery: Regular Mail

Allergies: No Allergy Assessment

+---------Enter ?? for more actions---------------------------------------------

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Next Screen//

  
Example 3 – *Patient Prescription Processing* option update (Medication Profile screen):

Medication Profile May 01, 2007@12:12:12 Page: 1 of 1

OPPATIENT16,ONE <span class="mark">\<NO ALLERGY ASSESSMENT\></span>

PID: 000-24-6802 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: SEP 7,1952 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

------------------------------------ACTIVE----------------------------------

*------ --------------------screen continues but is not shown--------------------------*Example 4 – *Patient Prescription Processing* option update (No Allergy Assessment – Intervention Created):

There is no allergy assessment on file for this patient.

You will be prompted to intervene if you continue with this prescription

Do you want to Continue?: N// YES

Now creating Pharmacy Intervention

for POTASSIUM CHLORIDE 325MG ENSEAL

PROVIDER: OPPROVIDER4,TWO

RECOMMENDATION: ?

Answer with APSP INTERVENTION RECOMMENDATION, or NUMBER

Choose from:

1 CHANGE DRUG

2 CHANGE FORM OR ROUTE OF ADMINISTRATION

3 ORDER LAB TEST

4 ORDER SERUM DRUG LEVEL

5 CHANGE DOSE

6 START OR DISCONTINUE A DRUG

7 CHANGE DOSING INTERVAL

8 NO CHANGE

9 OTHER

RECOMMENDATION: 2 CHANGE FORM OR ROUTE OF ADMINISTRATION

See 'Pharmacy Intervention Menu' if you want to delete this

intervention or for more options.

Would you like to edit this intervention ? N// \<Enter\> O

# Miscellaneous Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are miscellaneous enhancements to the Outpatient Pharmacy V. 7.0 software.

- Service Reject selection for Nature of Order prompt
- Patient eligibility status displayed
- Patient Status refreshed when changed with the PU action
- Patient lookup updated for remote data for order checks
- Mail status expiration date displayed
- CACHE locking issue

## Service Reject Selection (HD172344)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds the SERVICE REJECT choice from the CPRS NATURE OF ORDER file (#100.02) to the current list of selections for the “Nature of Order:” prompt.

When chosen, SERVICE REJECT will generate an alert to the provider to electronically sign the prescription. Sites should ensure their operational policies include clear guidance on when the pharmacist would use the service reject option.

Example:

Nature of Order: WRITTEN// ?

Choose from:

1 WRITTEN W

2 VERBAL V

3 TELEPHONED P

4 SERVICE CORRECTION S

5 POLICY I

6 DUPLICATE D

12 SERVICE REJECT R

Nature of Order: WRITTEN//

The “Nature Of Order” prompt is shown when entering new orders, discontinuing orders or making edits to critical fields. The following chart lists a description of each of the choices (new selection highlighted):

Require Print Print on

<u>Nature of Order Activity E.Signature Chart Copy Summary</u>

WRITTEN x

VERBAL x x x

TELEPHONED x x x

SERVICE CORRECTION

POLICY x x

DUPLICATE

<span class="mark">SERVICE REJECT x x</span>

There may be several instances where the usage of Service Reject for the Nature of Order field may be used in conjunction with local policy. Several sites have been using the service reject choice during order processing and have provided the following scenarios:

\(1\) When the pharmacist is processing pending outpatient pharmacy orders, if either the intent of provider is not clear or is not appropriate (i.e., dose out of range, provider not authorized to write for restricted/NF med, etc), then the pharmacy has the option of discontinuing the order and assigning SERVICE REJECT to the Nature of Order field. The pharmacist is first prompted to enter a justification of the discontinuation in the Comments section, and then enter a selection for Nature of Order. This nature of order generates a view alert in CPRS and requires the provider to electronically sign the order, acknowledging that the order has been discontinued and requires appropriate follow-up, based on the comments sent by the pharmacist.

\(2\) When finishing orders from OERR where the Pharmacy edit/intervention changes the intent of the order, the service may reject the original order. This may be due to lack of significant reason to hold the medication from the patient. The original order is discontinued, and a new unsigned order is generated, and reflects the changes for the physician’s signature.

## Patient Eligibility Update (HD67512)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient’s eligibility will be displayed before prompting for patient status when finishing prescriptions or entering new orders. This ensures that the proper entry from the RX PATIENT STATUS file (#53) is being selected. This is stored in the PATIENT STATUS field (#3) of the PHARMACY PATIENT file (#55).

- In the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] and the *Complete Orders from OERR* \[PSO LMOE FINISH\] options, after displaying the patient name, the patient's eligibility is displayed and the user is prompted for Rx Patient Status. If "NO" for New Order is entered, the eligibility is displayed again before the prompt for Rx Patient Status.
- For both of these options, the Patient Status prompt is updated to include “RX” in the prompt.

Example 1 - *Patient Prescription Processing* option update:  

Select Rx (Prescriptions) Option: PATient Prescription Processing

Select PATIENT NAME: OPPATIENT10 OPPATIENT10,ONE 06-03-41 000246810

YES SC VETERAN

Eligibility: SC

RX PATIENT STATUS: SERVICE CONNECTED// \<Enter\>

------------------------------example continues------------------------------------  
Example 1 *Patient Prescription Processing* option update (continued):

<u>Patient Information May 22, 2007 10:44:38 Page: 1 of 2</u>

OPPATIENT10,ONE

PID: 000-24-6810 Ht(cm): 177.80 (02/08/2006)

DOB: JUN 3,1941 (67) Wt(kg): 90.45 (02/08/2006)

SEX: MALE

<u>+</u>

Eligibility: SC

Disabilities:

1B STREET

CHAT PHONE:

NEW YORK 12345

Prescription Mail Delivery: DO NOT MAIL Expire Date: JUN 01, 2008

Outpatient Narrative: N

Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Next Screen// \<Enter\> NEXT SCREEN

Quit// \<Enter\>

<u>Patient Information May 22, 2007 10:44:38 Page: 2 of 2</u>

OPPATIENT10,ONE

PID: 000-24-6810 Ht(cm): 177.80 (02/08/2006)

DOB: JUN 3,1941 (67) Wt(kg): 90.45 (02/08/2006)

SEX: MALE

\+

Allergies:

Remote: ASPIRIN, NON-OPIOID ANALGESICS

Adverse Reactions:

Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Quit// \<Enter\>

Medication Profile May 22, 2007 10:44:56 Page: 1 of 1

OPPATIENT10,ONE

PID: 000-24-6810 Ht(cm): 177.80 (02/08/2006)

DOB: JUN 3,1941 (67) Wt(kg): 90.45 (02/08/2006)

AGE: 60

Last entry on 01/13/03

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

------------------------------------ACTIVE----------------------------------

1 503902 ACETAMINOPHEN 500MG TAB 60 A\> 05-22 05-22 3 30

2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

------------------------------------PENDING------------------------------------

3 AMPICILLIN 250MG CAP QTY: 40 ISDT: 05-29 REF: 0

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// NO New Order

Eligibility: SC

RX PATIENT STATUS: SERVICE CONNECTED// \<Enter\>

  
Example 2 - *Complete Orders from OERR* option update:  

Select By: (PA/RT/PR/CL/E): PATIENT// ROUTE

Route: (W/M/C/E): WINDOW// MAIL

Do you want to see Medication Profile? Yes// \<Enter\>

OPPATIENT,ONE (000-23-0777)

No Allergy Assessment!

Press Return to continue: \<Enter\>

Eligibility: NSC

RX PATIENT STATUS: OPT NSC//

## ## Patient Status Update (HD188707)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option, if the Patient Update “PU” action is chosen and the PATIENT STATUS is changed to a new one, when returning to the option and choosing “NO” for New Order, the default PATIENT STATUS displayed is the one before the PU change was done. Patch PSO\*7\*268 makes a correction to refresh the PATIENT STATUS before displaying the default.

## Patient Lookup Update (Enhancement)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient lookup for Outpatient Pharmacy V. 7.0 will be modified to include a check for the availability of remote data for order checks. This was requested to improve the performance of order checks. Once Remote Data Interoperability (RDI) is turned on at a site, if a problem has been detected with accessing remote data, the patient lookup will report that to the user when selecting a patient, rather than displaying “Remote data not available - Only local order checks processed.” for each individual order.

Example - Health Data Repository Unavailable  

Select PATIENT NAME: OPPATIENT16,ONE OPPATIENT16,ONE 4-3-41 000246802

YES SC VETERAN

OPPATIENT16,ONE (000-24-6802)

No Allergy Assessment!

Press Return to continue: \<Enter\>

Remote data not available - Only local order checks processed.

Press Return to continue... \<Enter\>

Eligibility: SC

RX PATIENT STATUS: SERVICE CONNECTED//

## Mail Status Expiration Date Displayed (HD68535)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the MAIL STATUS EXPIRATION DATE field (#.05) in the PHARMACY PATIENT file (#55) is less than today, the MAIL field (#.03) displays on the patient profile as if it is still active. This patch adds the display of the MAIL STATUS EXPIRATION DATE field next to the MAIL field on the patient profile for MAIL settings of Do Not Mail, Local - Regular Mail and Local - Certified Mail if the mail status is expired.

Example (Patient Information screen):

Patient Information May 11, 2007@12:40:08 Page: 1 of 1

OPPATIENT16,ONE <span class="mark">\<NO ALLERGY ASSESSMENT\></span>

PID: 000-24-6802 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: SEP 7,1952 (55) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

--------------------------------------------------------------------------------

Eligibility: SC LESS THAN 50% SC%: 30

Disabilities:

1B STREET

CHAT PHONE:

NEW YORK 12345

Prescription Mail Delivery: DO NOT MAIL Expire Date: MAY 01, 2007

Cannot use safety caps.

Allergies: No Allergy Assessment

Adverse Reactions:

----------Enter ?? for more actions---------------------------------------------

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Quit//

## ## ## ## Cache Locking Issue (Enhancement)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the deployment of Cache Version 5, it was discovered that the short lock timeout values could generate a lock failure. Patch DI\*22\*147, which has already been released, provided a solution to resolve this issue and future lock issues. This patch instituted a new default lock timeout of three seconds based on a global node setting of ^DD("DILOCKTM")=3.

In order to avoid the lock issue, all routines that currently uses a lock timeout value less than 3 seconds is modified in this patch to check for the node ^DD("DILOCKTM") and to use the value defined otherwise, default the lock timeout value to 3 seconds.

The following patches contain the fix for the locking issue:

- PSA\*3\*64
- PSD\*3\*66
- PSO\*7\*268
- PSS\*1\*125