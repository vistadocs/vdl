---
consolidated_title: "inbound eprescribing mbm class 3 to class 1 conversion release notes"
app_code: PSO
doc_type: RN
master_source: "PSO*7.0*770 Inbound ePrescribing MbM Class 3 to Class 1 Conversion Release Notes"
master_pub_date: revision_count: 0
consolidated_from: 2 versions
prior_versions:
  - "PSO*7*700 Inbound ePrescribing MbM Class 3 to Class 1 Conversion Release Notes"
---

Outpatient Pharmacy

Inbound ePrescribing (IEP)Meds-by-Mail (MbM) Class 3 to Class 1 ConversionVistA Patch \# PSO\*7.0\*770

Release Notes

![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/001.png)

July 2025Version 1.0

Office of Information and Technology (OI&T)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Patches](#related-patches)
  - [Summary of Changes](#summary-of-changes)
    - [Patient Progress Note Update](#patient-progress-note-update)
    - [Patient address, primary phone and SSN displayed on the Single eRx View screen](#patient-address-primary-phone-and-ssn-displayed-on-the-single-erx-view-screen)
    - [Patient Pharmacy Narrative displayed on the Single eRx View screen](#patient-pharmacy-narrative-displayed-on-the-single-erx-view-screen)
    - [Provider phone displayed on the Single eRx View screen](#provider-phone-displayed-on-the-single-erx-view-screen)
    - [Missing Patient Instruction alert](#missing-patient-instruction-alert)
    - [RxChangeRequest 'Script Clarification' reason message templates](#rxchangerequest-script-clarification-reason-message-templates)
    - [Option to Edit RxChangeRequest Reason Template Text](#option-to-edit-rxchangerequest-reason-template-text)
    - [Full drug name display when user selects the DET hidden action](#full-drug-name-display-when-user-selects-the-det-hidden-action)
    - [VistA Drug Search](#vista-drug-search)
    - [RxRenewalResponse Message Types under SQ](#rxrenewalresponse-message-types-under-sq)
    - [Search by Remove Reason codes](#search-by-remove-reason-codes)
    - [Provider Auto-Validation for CS Drugs](#provider-auto-validation-for-cs-drugs)
    - [Ability to Un-Process VistA Rx with a DELETED status](#ability-to-un-process-vista-rx-with-a-deleted-status)
    - [Allow Un-Accept and Re-Accept of Approved eRx Renewals](#allow-un-accept-and-re-accept-of-approved-erx-renewals)
    - [Park Functionality in the eRx Holding Queue](#park-functionality-in-the-erx-holding-queue)
    - [No auto-match if Provider is inactive](#no-auto-match-if-provider-is-inactive)
    - [Patient, Provider and Drug/SIG auto-matching based on suggestions](#patient-provider-and-drugsig-auto-matching-based-on-suggestions)
    - [Updates to existing Accept(AC) action in Single eRx View/Display screen](#updates-to-existing-acceptac-action-in-single-erx-viewdisplay-screen)
    - [Ability to change the Hold code w/out Un-holding an eRx](#ability-to-change-the-hold-code-wout-un-holding-an-erx)
    - [First-In-First-Out (FIFO) processing for Complete Orders from OERR \[PSO LMOE FINISH\] option](#first-in-first-out-fifo-processing-for-complete-orders-from-oerr-pso-lmoe-finish-option)
    - [eRx Prescriber Order Number in the Print](#erx-prescriber-order-number-in-the-print)
    - [Page breaking in the Print](#page-breaking-in-the-print)
    - [Allow Change Requests for eRx currently on Hold and Responses](#allow-change-requests-for-erx-currently-on-hold-and-responses)
    - [RxChangeRequest 'Therapeutic Interchange/Subst.' reason message templates](#rxchangerequest-therapeutic-interchangesubst-reason-message-templates)
    - [MbM Only: Auto-Holds for Pt. Eligibility and Non-Allergy Assessment](#mbm-only-auto-holds-for-pt-eligibility-and-non-allergy-assessment)
    - [Menu changes to the Single eRx View/Display Screen](#menu-changes-to-the-single-erx-viewdisplay-screen)
    - [New View Suggested Rx (VSR) action](#new-view-suggested-rx-vsr-action)
    - [New value for ACTION on SUGGESTION prompt: (V) VIEW RX](#new-value-for-action-on-suggestion-prompt-v-view-rx)
    - [VistA Prescriber Class displayed on Single eRx and Pending Order](#vista-prescriber-class-displayed-on-single-erx-and-pending-order)
    - [New Next Drug (ND) hidden action](#new-next-drug-nd-hidden-action)
    - [Indication functionality added to eRx Holding Queue](#indication-functionality-added-to-erx-holding-queue)
    - [Added RRE and CRE error codes under CCR Filter](#added-rre-and-cre-error-codes-under-ccr-filter)
    - [Patient DOB check on Edit and Accept Validation warning](#patient-dob-check-on-edit-and-accept-validation-warning)
    - [Memorize the VistA patient when eRx is selected (\<SPACE BAR\>)](#memorize-the-vista-patient-when-erx-is-selected-space-bar)
    - [HFF for Un-Accept and Un-Remove will now ask for Future Fill Date](#hff-for-un-accept-and-un-remove-will-now-ask-for-future-fill-date)
    - [IAS (Include All Statuses) action extended to Rx Medication Queue as well](#ias-include-all-statuses-action-extended-to-rx-medication-queue-as-well)
    - [eRx Prescriber Phone \# displayed on Pending Order and Active Rx](#erx-prescriber-phone-displayed-on-pending-order-and-active-rx)
    - [VistA Drug Edit capability on the Single eRx View/Display screen](#vista-drug-edit-capability-on-the-single-erx-viewdisplay-screen)
    - [After AV it will go back to Single eRx View/Display (VAMC's only)](#after-av-it-will-go-back-to-single-erx-viewdisplay-vamcs-only)
    - [Default for Copy PATIENT INSTRUCTIONS from Rx#12345? Y// changed to 'NO'](#default-for-copy-patient-instructions-from-rx12345-y-changed-to-no)
    - [Jump to eRx (JE) action modification at the Patient level](#jump-to-erx-je-action-modification-at-the-patient-level)
    - [DEA Nightly Update Job w/ Data from DEA/DOJ](#dea-nightly-update-job-w-data-from-deadoj)
    - [Patient address will ignore differences between similar words](#patient-address-will-ignore-differences-between-similar-words)
    - [Conversion issue with Patient Weight when prescriber sent in g (grams)](#conversion-issue-with-patient-weight-when-prescriber-sent-in-g-grams)
    - [HFF (Hold for Future Fill) will now set the Effective Date if none](#hff-hold-for-future-fill-will-now-set-the-effective-date-if-none)
    - [MbM Only: CAO status will automatically be set with CAA](#mbm-only-cao-status-will-automatically-be-set-with-caa)
    - [Cancelations of RxRenewal and RxChange were not DCing Pending/Active Order](#cancelations-of-rxrenewal-and-rxchange-were-not-dcing-pendingactive-order)
    - [Allergies compare between eRx and VistA were Case Sensitive](#allergies-compare-between-erx-and-vista-were-case-sensitive)
    - [Update to the Pharmacist Enter/Edit \[PSO RPH\] option](#update-to-the-pharmacist-enteredit-pso-rph-option)
    - [New option for Batch Change Request and VistA Drug Replacement](#new-option-for-batch-change-request-and-vista-drug-replacement)
    - [eRx Pending Order Suggested FILL DATE auto calculation](#erx-pending-order-suggested-fill-date-auto-calculation)
- [Reflection Terminal Display Settings](#reflection-terminal-display-settings)
- [Product Documentation](#product-documentation)
The Inbound Electronic Prescribing (eRx) Phase 3 Enhancements delivered in this patch is a continuation effort to convert all of the MbM Class 3 modifications into Class 1. Below is a summary of the changes being delivered in this patch. For a more comprehensive description of the changes please refer to the documents listed in the Documentation section of this description. A summary of the changes can be found below.

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This functionality enhancement is being released via a single VistA patch:

APPLICATION/VERSION PATCH

----------------------------------------------------------

OUTPATIENT PHARMACY (PSO) V. 7.0 PSO\*7\*770

## Summary of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of the changes made to the existing Outpatient Pharmacy eRx functionality. Please, refer to the patch description and documentation for more detailed information.

### Patient Progress Note Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the user sends the eRx Change Request to the prescriber, a Patient Progress Note will be automatically generated for the patient. Depending on the site's configuration of its CPRS Progress Note Title, the RxChangeRequest CPRS Progress Note Title could fall under either the PHARMACY ERX RX CHANGE REQUEST NOTE or the ERX RX CHANGE REQUEST NOTE. The text in the Progress Note generated will mirror the content from the eRx Change Request Display VistA record.  
  
If the user initiating the eRx Change Request has a designated cosigner linked to their profile, the software will ask (refer to sample below) the user to provide the expected cosigner. This area must be completed. Kindly note that if the user fails to input the required cosigner, the eRx Change Request will still be generated, but the CPRS Progress Note will not be created.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>. . .</strong></p>
<p>Would you like to edit this Rx Change Request before sending it? NO//</p>
<p>Would you like to send this Rx Change Request? YES//</p>
<p>Sending Request to Provider...Done.</p>
<p>Creating a new Progress Note...</p>
<p>EXPECTED COSIGNER:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Patient address, primary phone and SSN displayed on the Single eRx View screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To easily confirm the patient's identity, the patient's address, phone number and SSN are included on both the eRx and VistA sides of the Single eRx View/Display landing page, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Patient Pharmacy Narrative displayed on the Single eRx View screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the VistA patient is matched and it contains text in the Pharmacy Narrative field, it will be displayed in the eRx Single View/Display Screen across the screen at the bottom of the Patient section and just above the Provider section, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<p>VistA Narrative: <strong>ALLEGRA, LANSOPRAZOLE CRITERIA MET-2-23-01 NFDR FAMOTIDINE 8/0</strong></p>
<p><strong>1 ; RABEPRAZOLE OK 8/02; FINASTERIDE; ZOSTAVAX; WARFARIN CITC 8/21</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Provider phone displayed on the Single eRx View screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To quickly verify the Provider, the provider's phone number is included and shown on both the eRx and VistA portions of the Single eRx View/Display landing page alongside the NPI, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<p>VistA Narrative: <strong>ALLEGRA, LANSOPRAZOLE CRITERIA MET-2-23-01 NFDR FAMOTIDINE 8/0</strong></p>
<p><strong>1 ; RABEPRAZOLE OK 8/02; FINASTERIDE; ZOSTAVAX; WARFARIN CITC 8/21</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Missing Patient Instruction alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After accepting the suggested Rx on the eRx Drug Validation Edit action screen, the user will be prompted whether they want to copy the patient instructions from the suggested Rx into the eRx, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// e Edit</p>
<p>|Sugg. <strong>1</strong> of <strong>2</strong> - <strong>03/11/25</strong>|</p>
<p>ERX MED VISTA MED |From Rx#: <strong>3059546</strong> |</p>
<p>_______________________________________________________________________________</p>
<p>Drug: LEVOTHYROXINE NA (SYNTHROID) 50MC |Drug: LEVOTHYROXINE NA (SYNTHROID) 50M</p>
<p>G TAB | CG TAB</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; VA STND DRUG</strong></p>
<p>________________________________________|______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET MOUTH EVERY DAY</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>| <strong>BEFORE MEAL FOR THYROID HORMONE</strong></p>
<p>| <strong>REPLACEMENT - TAKE AT LEAST AN HOUR</strong></p>
<p>| <strong>BEFORE FOOD OR OTHER MEDICATIONS</strong></p>
<p>________________________________________|______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p><strong>TESTING FOR ERX BATCH CHANGE REQUEST.</strong> | <strong>TESTING FOR ERX BATCH CHANGE REQUEST.</strong></p>
<p>________________________________________|______________________________________</p>
<p>Quantity: <strong>30</strong> |Quantity: <strong>30</strong></p>
<p>Dispense Unit: |Dispense Unit: <strong>TAB</strong></p>
<p>________________________________________|______________________________________</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>3</strong> |Days Supply: <strong>30</strong> Refills: <strong>3</strong></p>
<p>________________________________________|______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (N)EXT (F)ORGET (E)XIT: NEXT// ACCEPT</p>
<p>Rx #<strong>3059546</strong> PATIENT INSTRUCTIONS:</p>
<p><strong>FOR THYROID HORMONE REPLACEMENT - TAKE AT LEAST AN HOUR BEFORE FOOD OR OTHER</strong></p>
<p><strong>MEDICATIONS</strong></p>
<p>Copy PATIENT INSTRUCTIONS from Rx #<strong>3059546</strong>? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1)  If YES is chosen by the user, all fields on the eRx Drug Validation screen will have its fields updated with any available data.
2)  If NO is chosen by the user, all fields on the eRx Drug Validation screen will have its fields updated with any available data, with the exception of the Patient Instruction field. The user can manually edit the field as they currently do.
3)  When the user inputs the up-caret symbol (^), no changes are made.

### RxChangeRequest 'Script Clarification' reason message templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CHANGE REQUEST CODE for 'Script Clarification' has been updated to allow the pharmacist/technician to choose a reason code linked to a pre-populated question template in the \<RxChangeRequest\> \<ReasonText\> field. The user will be prompted to choose a CHANGE REQUEST SUB-CODE from the options provided, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<p>VistA Narrative: <strong>ALLEGRA, LANSOPRAZOLE CRITERIA MET-2-23-01 NFDR FAMOTIDINE 8/0</strong></p>
<p><strong>1 ; RABEPRAZOLE OK 8/02; FINASTERIDE; ZOSTAVAX; WARFARIN CITC 8/21</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// EC EC</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>IBUPROFEN 200MG TAB</strong></p>
<p>eRx SIG : <strong>TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</strong></p>
<p>eRx Notes: <strong>This is a TEST NOTE.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>20</strong> Days Supply: <strong>30</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: Script Clarification</p>
<p>Select one of the following:</p>
<p>PRN - PRN Directions</p>
<p>UDD - As Directed Directions</p>
<p>COD - Conflicting Directions</p>
<p>MSD - Missing Directions</p>
<p>RIJ - Route of Injection</p>
<p>VEF - Verify Formulation</p>
<p>VLQ - Verify Low Quantity</p>
<p>VPQ - Verify Package Quantity</p>
<p>AUT - Prescriber Not Authorized</p>
<p>CHANGE REQUEST SUB-CODE: COD Conflicting Directions</p>
<p>NOTE TO PROVIDER:....</p>
<p>==[ WRAP ]==[INSERT ]===========&lt; NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]====</p>
<p>This prescription contains conflicting directions. Please verify which</p>
<p>directions are to be followed.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Option to Edit RxChangeRequest Reason Template Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the eRx Patient Centric Queue screen, a new hidden action called 'CRT CR Default Text Edit' has been added to enable users who hold the PSDMGR security key to modify the default RxChangeRequest Reason template text for their own division. Please, refer to the user documentation for more information about this new option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Jun 02, 2025@15:27:51 Page: 1 of 2</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB SSN ED<strong>v</strong> NW WT IP HD CCR OTH TOT</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. MBMONE,TESTONE TEST 02/02/9999 666-12-1234 336 0 0 3 2 0 0 5</p>
<p>2. MBMONE,TESTONE TEST 02/02/9999 666-12-1234 272 0 0 1 0 0 0 1</p>
<p>3. TESTONE,MBMONE 02/23/9999 252 0 0 0 0 1 0 1</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>RX Rx List View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// CRT CRT</p>
<p><strong>Updates will apply for the CHEYENNE VAH&amp;ROC division only.</strong></p>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: Therapeutic Interchange/Substitution</p>
<p>DEFAULT NOTE TO PROVIDER:......</p>
<p><strong>You are about to edit Therapeutic Interchange/Substitution Template:</strong></p>
<p>==[ WRAP ]==[INSERT ]=======&lt; DEFAULT NOTE TO PROVIDE[Press &lt;PF1&gt;H for help]====</p>
<p>Pharmacy is unable to supply medication as prescribed; however, alternative</p>
<p>options may exist. Please approve an option below or Cancel Rx and send a</p>
<p>replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Full drug name display when user selects the DET hidden action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the eRx Single Patient Queue and the eRx Medication Queue when the user selects the DET (Show/Hide Details) action it will display the complete eRx Drug name as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Patient Centric Queue</strong> Jun 02, 2025@15:27:51 Page: 1 of 2</u></p>
<p>Rx PATIENT: <strong>MBMONE,TESTONE TEST</strong> SEX: <strong>M</strong> DOB: <strong>02/02/75(50)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>666-13-4567</strong> MATCHING</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID DRUG NAME PROVIDER NAME REC.DATE<strong>^</strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 2024070000001 IBUPROFEN 200MG TAB PROVIDER,TST1 07/01/24 HC <strong>M</strong>V A <strong>M</strong>V</p>
<p>2. 2024070000002 ROSUVASTATIN CA 10MG PROVIDER,TST1 07/01/24 I <strong>M</strong>V AV A</p>
<p>3. 2024070000003 HYDROCODONE 5MG/ACETAM PROVIDER,TST1 07/01/24 I <strong>M</strong>V A A</p>
<p>4. 2024070000004 TETRACYCLINE HCL 250MG PROVIDER,TST1 07/01/24 I <strong>M</strong> A A</p>
<p>5. 2024070000006 LISINOPRIL 40MG TAB PROVIDER,TST2 07/02/24 HC AV A<strong>V</strong> AV</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>DET Show/Hide Details IAS Include All Statuses LBD Change Look Back Days</p>
<p>Select: Quit// DET Show/Hide Details</p>
<p><u><strong>eRx Patient Centric Queue</strong> Jun 02, 2025@15:27:51 Page: 1 of 2</u></p>
<p>Rx PATIENT: <strong>MBMONE,TESTONE TEST</strong> SEX: <strong>M</strong> DOB: <strong>02/02/75(50)</strong></p>
<p>LOOK BACK DAYS: <strong>365</strong> STATUS: <strong>ACTIONABLE</strong> SSN: <strong>666-13-4567</strong> MATCHING</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># ERX ID PROVIDER NAME REC.DATE<strong>^</strong>STA PT PR DR</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. 2024070000001 PROVIDER,TST1 07/01/24 HC <strong>M</strong>V A <strong>M</strong>V</p>
<p><strong>eRx Drug: IBUPROFEN 200MG TAB</strong></p>
<p><strong>eRx Qty: 20 eRx # of Refills: 3 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</strong></p>
<p>2. 2024070000002 PROVIDER,TST1 07/01/24 I <strong>M</strong>V AV A</p>
<p><strong>eRx Drug: ROSUVASTATIN CA 10MG</strong></p>
<p><strong>eRx Qty: 20 eRx # of Refills: 3 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</strong></p>
<p>3. 2024070000003 PROVIDER,TST1 07/01/24 I <strong>M</strong>V A A</p>
<p><strong>eRx Drug: HYDROCODONE 5MG/ACETAMINOPHEN 325MG TAB</strong></p>
<p><strong>eRx Qty: 20 eRx # of Refills: 3 eRx Days Supply: 30</strong></p>
<p><strong>SIG: Take 1 tablet by mouth every 8 hours as needed for Acute Pain.</strong></p>
<p>4. 2024070000004 PROVIDER,TST1 07/01/24 I <strong>M</strong> A A</p>
<p><strong>eRx Drug: TETRACYCLINE HCL 250MG CAP</strong></p>
<p><strong>eRx Qty: 20 eRx # of Refills: 3 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE ONE CAPSULE BY MOUTH FOUR TIMES A DAY (BEFORE MEALS AND AT</strong></p>
<p><strong>BEDTIME) FOR 10 DAYS FOR INFECTION.</strong></p>
<p>5. 2024070000006 PROVIDER,TST2 07/02/24 HC AV A<strong>V</strong> AV</p>
<p><strong>eRx Drug: LISINOPRIL 40MG TAB</strong></p>
<p><strong>eRx Qty: 20 eRx # of Refills: 3 eRx Days Supply: 30</strong></p>
<p><strong>SIG: TAKE YOUR FIRST DOSE BEFORE BEDTIME. AFTER THE FIRST DOSE, TAKE</strong></p>
<p><strong>LISINOPRIL AT ANY TIME OF DAY.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>DET Show/Hide Details IAS Include All Statuses LBD Change Look Back Days</p>
<p>Select: Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### VistA Drug Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new search option called 'VISTA DRUG' has been added in the SQ Search Queue action, enabling users to search for eRx's by VistA Drug already matched/linked to the eRx drug as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Jun 03, 2025@10:16:05 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DAT<strong>^</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. MBMONE,TESTONE TEST 02/02/75 IBUPROFEN 200MG TAB PROVIDR,TST I 09/03/24</p>
<p>2. TESTONE,MBMONE 02/23/46 CHOLECALCIF 25MCG (D3 PROVIDR,TST HC 09/23/24</p>
<p>3. PATIENT,TESTER 09/10/45 Spiriva with HandiHal PROVIDR,TST N 09/24/24</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// SQ Search Queue</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### RxRenewalResponse Message Types under SQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The search query option MESSAGE TYPE has been modified. Upon entering certain message types (RE and CX) as listed below, the user will be prompted to enter the corresponding RESPONSE TYPE as indicated. In this prompt, users have the option to choose ALL to view all response types for the message type selected or select a specific response type as shown below. For additional details on this new change, please refer to the user manual documentation.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Jun 03, 2025@10:16:05 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DAT<strong>^</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. MBMONE,TESTONE TEST 02/02/75 IBUPROFEN 200MG TAB PROVIDR,TST I 09/03/24</p>
<p>2. TESTONE,MBMONE 02/23/46 CHOLECALCIF 25MCG (D3 PROVIDR,TST HC 09/23/24</p>
<p>3. PATIENT,TESTER 09/10/45 Spiriva with HandiHal PROVIDR,TST N 09/24/24</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// SQ Search Queue</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY: 7 MESSAGE TYPE</p>
<p>MESSAGE TYPE: RXRENEWALRESPONSE</p>
<p>RESPONSE TYPE: ALL// ?</p>
<p>Enter a response type from the list.</p>
<p>Select one of the following:</p>
<p>ALL ALL</p>
<p>A APPROVED</p>
<p>AWC APPROVED WITH CHANGES</p>
<p>D DENIED</p>
<p>DNP DENIED, NEW RX TO FOLLOW</p>
<p>R REPLACE</p>
<p>RESPONSE TYPE: ALL//</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE <strong>(RXRENEWALRESPONSE/ALL)</strong></p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Furthermore, the RXCHANGEREQUEST MESSAGE TYPE search has been altered. When the user inputs CR (RXCHANGEREQUEST) in the message type prompt, they will be prompted to enter the CHANGE REQUEST CODE. In this prompt, users can choose to either view all CHANGE REQUEST CODE or pick a specific CHANGE REQUEST CODE as shown below. Please refer the user manual documentation for further information regarding this new change.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item(s): Next Screen// SQ Search Queue</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY: 7 MESSAGE TYPE</p>
<p>MESSAGE TYPE: CR RXCHANGEREQUEST</p>
<p>Select one of the following:</p>
<p>ALL ALL</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: ALL//</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE <strong>(RXCHANGEREQUEST/ALL)</strong></p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Search by Remove Reason codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The search query option ERX STATUS has been modified. Upon entering certain eRx Status (RM and RJ) as listed below, the user will be prompted to enter the corresponding REMOVAL or REJECT REASON CODE as indicated. In this prompt, users have the option to choose ALL to view all REMOVAL or REJECT REASON CODE or select a specific response type as shown below. For additional details on this new change, please refer to the user manual documentation.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Jun 03, 2025@10:16:05 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DAT<strong>^</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. MBMONE,TESTONE TEST 02/02/75 IBUPROFEN 200MG TAB PROVIDR,TST I 09/03/24</p>
<p>2. TESTONE,MBMONE 02/23/46 CHOLECALCIF 25MCG (D3 PROVIDR,TST HC 09/23/24</p>
<p>3. PATIENT,TESTER 09/10/45 Spiriva with HandiHal PROVIDR,TST N 09/24/24</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// SQ Search Queue</p>
<p>Select one of the following:</p>
<p>1 ERX PATIENT</p>
<p>2 ERX DATE OF BIRTH</p>
<p>3 RECEIVED DATE RANGE</p>
<p>4 ERX PROVIDER</p>
<p>5 ERX STATUS</p>
<p>6 ERX DRUG NAME</p>
<p>7 MESSAGE TYPE</p>
<p>8 ERX REFERENCE NUMBER</p>
<p>9 VISTA RX #</p>
<p>10 VISTA PATIENT</p>
<p>11 VISTA PROVIDER</p>
<p>12 MATCH STATUS</p>
<p>13 VISTA DRUG</p>
<p>SEARCH BY: 5 ERX STATUS</p>
<p>ERX STATUS: RM REMOVED</p>
<p>REMOVAL REASON CODE: ALL// ?</p>
<p>Enter the code associated with this action. Answer must be 1-10</p>
<p>characters in length.</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>216 REM01 Drug out of stock or on backorder and unavailable for</p>
<p>processing</p>
<p>217 REM02 Patient was not able to pick up</p>
<p>218 REM03 Prescription canceled by Provider</p>
<p>219 REM04 Prescription processed manually</p>
<p>220 REM05 Provider will cancel this eRx and submit another</p>
<p>221 REM06 Unable to mail prescription and patient unable to pick</p>
<p>up</p>
<p>222 REM07 Unable to contact patient</p>
<p>223 REM08 Unable to contact provider</p>
<p>224 REM91 Undefined system error</p>
<p>225 REM92 OCAND9080;@VFQH828!rrm6018bah!ther</p>
<p>1556 REM09 ERX Issue not resolved-Provider contacted</p>
<p>1586 REM81 Prior Authorization Denied</p>
<p>1587 REM82 No Community Care Authorization for this Prescription</p>
<p>1588 REM83 Patient Not Found in Local VA Database</p>
<p>REMOVAL REASON CODE: ALL//</p>
<p><strong>. . .</strong></p>
<p>SEARCH BY: 5 ERX STATUS</p>
<p>ERX STATUS: RJ REJECTED</p>
<p>REJECT REASON CODE: ALL// ?</p>
<p>Enter the code associated with this action. Answer must be 1-10</p>
<p>characters in length.</p>
<p>Answer with ERX SERVICE REASON CODES, or NUMBER</p>
<p>Do you want the entire ERX SERVICE REASON CODES List? Y (Yes)</p>
<p>Choose from:</p>
<p>203 PTT01 Patient not eligible</p>
<p>204 PTT02 Cannot resolve Patient</p>
<p>205 PVD01 Provider not eligible</p>
<p>206 PVD02 Cannot resolve Provider</p>
<p>207 DRU01 Not eligible for refills</p>
<p>208 DRU02 Non-formulary drug</p>
<p>209 DRU03 Duplicate Prescription found for this Patient</p>
<p>210 DRU04 Invalid Quantity</p>
<p>211 DRU05 Duplicate therapeutic class</p>
<p>212 DRU06 CS prescription written/issue date has problems</p>
<p>213 ERR01 Multiple errors, please contact the Pharmacy</p>
<p>214 ERR02 Incorrect Pharmacy</p>
<p>215 ERR03 Issues with prescription, please contact the pharmacy</p>
<p>1557 PVD03 Missing/bad digital signature on inbound CS ERX</p>
<p>1558 PVD04 Prescriber's CS credential is not appropriate</p>
<p>1559 PTT03 Patient's mailing address is missing/mismatched</p>
<p>1560 ERR99 Other</p>
<p>REJECT REASON CODE: ALL//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Provider Auto-Validation for CS Drugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Auto-Validation functionality released with patch PSO\*7\*700 (see item \#5 of the patch description) will now be extended to digitally signed (indicating Controlled Substance) eRx's as well. The only additional check performed for auto-validating is that the VA provider must have a valid DEA# on file that matches the DEA# sent with the eRx.

### Ability to Un-Process VistA Rx with a DELETED status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sometimes an eRx prescription that has already been transmitted to CMOP must be un-processed so it can go back to the eRx Holding Queue. Therefore, an exception was implemented in the software to allow non-CS eRx prescriptions with a DELETED status to be un-processed even after they have been transmitted to CMOP.

### Allow Un-Accept and Re-Accept of Approved eRx Renewals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a Renewal request is Approved by the outside prescriber the eRx will go straight to the Pending Order file without stopping at the eRx Holding Queue first. The software will now allow the user to Un-Accept such records and send them back to the eRx Holding Queue so an issue (e.g., Eligibility verification, etc.) can be worked on there. Once the issue has been resolved the user will be able to re-accept the record without having to perform any matches or validations.

### Park Functionality in the eRx Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Park functionality released by the patch PSO\*7\*441, released back in September of 2022 has now been implemented in the eRx Holding Queue. If the site has the Park functionality turned ON the user will be able to select PARK as an option for the PICKUP ROUTING besides MAIL or WINDOW, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>. . .</strong></p>
<p>VA PATIENT INSTRUCTIONS: WITH FOOD FOR PAIN/INFLAMMATION</p>
<p>Replace</p>
<p>VA PROVIDER COMMENTS: THIS IS A TEST NOTE. Replace</p>
<p>PATIENT STATUS: CHAMPVA// CHAMPVA</p>
<p>eRx Quantity: 20</p>
<p>QTY ( ML ) ML (120/BT): 30// 30</p>
<p>eRx Days Supply: 30</p>
<p>DAYS SUPPLY: (1-90): 30//</p>
<p>eRx Refills: 3</p>
<p># OF REFILLS: (0-11): 1//</p>
<p>Select one of the following:</p>
<p>M MAIL</p>
<p>W WINDOW</p>
<p>P PARK</p>
<p>PICKUP ROUTING: M//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### No auto-match if Provider is inactive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A check was added to prevent an inactive VistA provider from being auto-matched to the eRx even if the NPI matches. Furthermore, if the inactive VistA Provider is a suggestion it will be automatically forgotten.

### Patient, Provider and Drug/SIG auto-matching based on suggestions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The auto-matching functionality is being further enhanced to utilize current VistA suggestions for Patient, Provider and Drug/SIG. For Patient and Provider if no auto-match was found the software will look for any existing suggestion and will auto-match to the latest VistA suggestion on file. In the case of Drug/SIG it will be greatly improved by matching not only the dispense drug but all fields from the suggested VistA Rx (if one exists), exactly as if the user accepted the suggestion manually.

### Updates to existing Accept(AC) action in Single eRx View/Display screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing Accept(AC) action in the Single eRx View/Display screen was renamed to Validate & Accept eRx and will automatically try to perform the validation (AV) for Patient (except for MbM), Provider and Drug as well, if needed, before accepting the eRx. This action will still perform all the checks necessary by each individual record match and will display the result for validating each match separately.

Please, refer to the user documentation for more detailed information about this new functionality.

### Ability to change the Hold code w/out Un-holding an eRx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users will now be able to switch the Hold code for an eRx on Hold for a different Hold code without having to un-hold the eRx. Once the user selects the Hold (H) action to hold an eRx already on software will inform them the eRx is already on hold and will ask if they want to change the Hold code, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// H Hold</p>
<p>This eRx is already in a 'HOLD' status.</p>
<p>Would you like to change the hold status and comments? NO// YES</p>
<p>Select HOLD reason code: HAL NO PATIENT ALLERGY ASSESSMENT</p>
<p>Additional Comments (Optional): ASSIGNING CORRECT HOLD CODE</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### First-In-First-Out (FIFO) processing for Complete Orders from OERR \[PSO LMOE FINISH\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A FIFO order algorithm has been implemented for this option for users that hold the newly created PSO ERX WORKLOAD RPH security key. Once the user holding this key enters the option they will be prompted for the Clinic they want to finish Pending Orders for and then if they want to process Flagged orders only. After answering these two prompts the option will automatically select the patient with the oldest record for the user to work on. The user will not be able to move to the next patient unless all the current patient's pending orders are either finished or flagged by themselves.

Please, refer to the user documentation for more detailed information about this new functionality.

### eRx Prescriber Order Number in the Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The incoming prescriber order number will be displayed in Print (P) under the PRESCRIPTION INFORMATION section, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>. . .</strong></p>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// P P</p>
<p>DEVICE: ;P-OTHER;80;999999999999999 HOME (CRT)</p>
<p>*PHARMACY INFORMATION*</p>
<p>TEST BUSINESS NAME</p>
<p>Address:</p>
<p>,</p>
<p>Primary Phone: NCPDP:</p>
<p>.</p>
<p>.</p>
<p>.</p>
<p>.</p>
<p>*PRESCRIPTION INFORMATION*</p>
<p>Prescriber Order #: ECWIA-9382026-211005-828</p>
<p>eRx Drug: LISINOPRIL 40MG TAB</p>
<p>NDC: 1472583693 Written Date: JUL 02, 2024 Issue Date:</p>
<p>Qty: 20 Days Supply: 30 Refills: 3</p>
<p>Code List Qualifier: Original Quantity</p>
<p>Drug Form:</p>
<p>Strength:</p>
<p>Substitutions?: YES Prohibit Renewals: No</p>
<p>eRx Sig:</p>
<p>TAKE YOUR FIRST DOSE BEFORE BEDTIME. AFTER THE FIRST DOSE, TAKE LISINOPRIL AT</p>
<p>ANY TIME OF DAY.</p>
<p>Provider Comments: TEST.</p>
<p>.</p>
<p>.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Page breaking in the Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print (P) action will now page break one page at time instead of displaying the entire information, which forced the user to scroll up using the terminal scrolling capability.

### Allow Change Requests for eRx currently on Hold and Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two changes are being made to the Change Request (EC Action) functionality:

1)  The Change Request (EC) action will be allowed to be run on eRx's that are currently on Hold.
2)  The Change Request (EC) action will be allowed to be run Response eRx's. Before, the EC action was restricted to the NewRx records only.

### RxChangeRequest 'Therapeutic Interchange/Subst.' reason message templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CHANGE REQUEST CODE for 'Therapeutic Interchange/Substitution' has been updated to allow the pharmacist/technician to choose a reason code linked to a pre-populated question template in the \<RxChangeRequest\> \<ReasonText\> field. The user will be prompted to choose a CHANGE REQUEST SUB-CODE from the options provided, as shown below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p>Name: <strong>MBMONE,TESTONE TEST</strong> |Name: <strong>MBMONE,TESTONE TEST</strong></p>
<p>DOB : <strong>FEB 02, 9999</strong> SSN : <strong>666123456</strong> |DOB : <strong>FEB 2,9999</strong> SSN : <strong>666-12-3456</strong></p>
<p>Phone: <strong>5551112222</strong> |Phone: <strong>5551112222</strong></p>
<p>ADDRESS LINE 1 ARLINGTON,TX 76017 | 1234 THIS REAL NOT REALLY 1234...76017</p>
<p>VistA Narrative: <strong>ALLEGRA, LANSOPRAZOLE CRITERIA MET-2-23-01 NFDR FAMOTIDINE 8/0</strong></p>
<p><strong>1 ; RABEPRAZOLE OK 8/02; FINASTERIDE; ZOSTAVAX; WARFARIN CITC 8/21</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PROVIDER AUTO-MATCHED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Name: <strong>PROVIDER,TESTONE</strong> |Name: <strong>PROVIDER,TESTONE</strong></p>
<p>NPI : <mark>1366412157</mark> Phone: |NPI : <mark>1932288248</mark> Phone: <mark>(888) 888-8888</mark></p>
<p>DEA : <mark>FB5656802</mark> |DEA :</p>
<p>Clinic: |Class:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED/EDITED | VALIDATED by USER,USERONE Z on 5/27/25@15:49</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: <strong><mark>IBUPROFEN 200MG TAB</mark></strong> |<u>1)</u>Drug: <mark>IBUPROFEN 100MG/5ML SUSP</mark></p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; 120 ML/BT</strong></p>
<p>SIG: |SIG:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// EC EC</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ORIGINAL ERX</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>eRx Drug : <strong>IBUPROFEN 200MG TAB</strong></p>
<p>eRx SIG : <strong>TAKE ONE TABLET A DAY ON AN EMPTY STOMACH</strong></p>
<p>eRx Notes: <strong>This is a TEST NOTE.</strong></p>
<p>Drug Form: Strength:</p>
<p>Qty Qualifier: <strong>Original Quantity</strong> Qty Unit of Measure:</p>
<p>Qty: <strong>20</strong> Days Supply: <strong>30</strong> Refills: <strong>3</strong> Substitutions: <strong>YES</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Select one of the following:</p>
<p>D DUE (Drug Use Evaluation)</p>
<p>G Generic Substitution</p>
<p>OS Out of Stock</p>
<p>P Prior Authorization Required</p>
<p>S Script Clarification</p>
<p>T Therapeutic Interchange/Substitution</p>
<p>U Prescriber Authorization</p>
<p>CHANGE REQUEST CODE: Therapeutic Interchange/Substitution</p>
<p>Select one of the following:</p>
<p>DSC - Days Supply Change</p>
<p>FMC - Formulary Change</p>
<p>CHANGE REQUEST SUB-CODE: FMC Formulary Change</p>
<p>NOTE TO PROVIDER:......</p>
<p>==[ WRAP ]==[INSERT ]===========&lt; NOTE TO PROVIDER &gt;=[Press &lt;PF1&gt;H for help]====</p>
<p>Pharmacy is unable to supply medication as prescribed; however, alternative</p>
<p>options may exist. Please approve an option below or Cancel Rx and send a</p>
<p>replacement.</p>
<p>&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MbM Only: Auto-Holds for Pt. Eligibility and Non-Allergy Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon arrival from the eRx Hub the eRx will be checked whether the VistA Patient was auto-matched or not. If it was successfully matched, the software will then check if the patient is eligible for ChampVA Rx benefit, if not, the software will automatically hold the eRx with an HEL (PATIENT ELIGIBILITY ISSUE). If eligible, the software will then check if the patient has an Allergy Assessment on file, if not, the software will automatically hold the eRx with an HAL (NO PATIENT ALLERGY ASSESSMENT).

### Menu changes to the Single eRx View/Display Screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bottom menu for the eRx Single eRx View/Display Screen was modified to increase the listing area by 2 lines. Only 6 actions will be available in the main menu: VP-VALIDATE PATIENT, VM-VALIDATE PROVIDER, VD-VALIDATE DRUG/SIG, H-Hold, RM-Remove and AC-Validate & Accept eRx. The actions P-Print and UH-Un Hold have been moved to the Hidden actions section, as seen below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Main actions menu:</u></strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen//</p>
<p><strong><u>Hidden actions menu:</u></strong></p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>+ Next Screen AD Add Comment AU View Audit Log</p>
<p>- Previous Screen ACK Acknowledge VO View Original eRx</p>
<p>UP Up a Line SH Status History VRQ View Request eRx</p>
<p>DN Down a Line HL View History Log VRE View Response eRx</p>
<p>FS First Screen EC eRx Change Request REC Resend Change Request</p>
<p>GO Go to Page PA Patient Allergies P Print</p>
<p>PS Print Screen UR Un Remove eRx UH Un Hold</p>
<p>PL Print List JO Jump to OP VSR View Suggested Rx</p>
<p>SL Search List UX Un Process eRx</p>
<p>Q Quit PN Patient Progress Note</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### New View Suggested Rx (VSR) action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new hidden action VSR was added to the eRx Single eRx View/Display hidden menu. This option will allow the user to view the VistA Rx that was used to suggest populate the prescription information for the current eRx. It will invoke the same layout from the View Prescription \[PSO VIEW\] option. Once the user selects VSR and there's a Suggested VistA Rx that was used to populate the eRx, the user will receive the following notice before they are taken to viewing the suggested VistA Rx:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>VP VALIDATE PATIENT VM VALIDATE PROVIDER VD VALIDATE DRUG/SIG</p>
<p>H Hold RM Remove eRx AC (Validate &amp; Accept eRx)</p>
<p>Select Item(s): Next Screen// VSR VSR</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>NOTICE</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>You will be taken to the VistA prescription that was used to pre-populate the</p>
<p>Drug fields (Product/SIG/Qty/Days Supply/# of Refills/Substitution) for this</p>
<p>eRx (aka,'Suggested VistA Rx'). This VistA Rx may or may not be for the same</p>
<p>patient in this eRx being processed.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
</tbody>
</table>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### New value for ACTION on SUGGESTION prompt: (V) VIEW RX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The suggestion prompt for the Drug/Sig will now offer a new option VIEW RX (V) to allow the user to view the VistA Rx information before accepting it. If the user select V a notice will be displayed before taking the user to view the Suggested VistA Rx detail, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>|Sugg. <strong>1</strong> of <strong>2</strong> - <strong>03/11/25</strong>|</p>
<p>ERX MED VISTA MED |From Rx#: <strong>3059546</strong> |</p>
<p>_______________________________________________________________________________</p>
<p>Drug: LEVOTHYROXINE NA (SYNTHROID) 50MC |Drug: LEVOTHYROXINE NA (SYNTHROID) 300</p>
<p>G TAB | MCG TAB</p>
<p>Substitution? <strong>YES</strong> Renewals? <strong>YES</strong> |Drug Message:</p>
<p>| <strong>NATL FORM; VA STND DRUG</strong></p>
<p>________________________________________|______________________________________</p>
<p>SIG: |SIG:</p>
<p><strong>TAKE ONE TABLET MOUTH EVERY DAY</strong> | <strong>TAKE ONE TABLET BY MOUTH ONCE DAILY</strong></p>
<p>| <strong>BEFORE MEAL FOR THYROID HORMONE</strong></p>
<p>| <strong>REPLACEMENT - TAKE AT LEAST AN HOUR</strong></p>
<p>| <strong>BEFORE FOOD OR OTHER MEDICATIONS</strong></p>
<p>________________________________________|______________________________________</p>
<p>Provider Notes/Comments: |Provider Comments:</p>
<p><strong>THIS IS ONLY A TEST FOR ERX BATCH</strong> | <strong>THIS IS ONLY A TEST FOR ERX BATCH</strong></p>
<p><strong>CHANGE REQUEST.</strong> | <strong>CHANGE REQUEST.</strong></p>
<p>________________________________________|______________________________________</p>
<p>Quantity: <strong>30</strong> |Quantity: <strong>30</strong></p>
<p>Dispense Unit: |Dispense Unit: <strong>TAB</strong></p>
<p>________________________________________|______________________________________</p>
<p>Days Supply: <strong>30</strong> Refills: <strong>3</strong> |Days Supply: <strong>30</strong> Refills: <strong>3</strong></p>
<p>________________________________________|______________________________________</p>
<p>ACTION on SUGGESTION: (V)IEW RX (A)CCEPT (N)EXT (F)ORGET (E)XIT: NEXT// V</p>
<p>_____________________________NOTICE______________________________________</p>
<p>You will be taken to the VistA Rx#9999999 that was entered in the past</p>
<p>for the same Product (NDC/SIG/Qty/Days Supply/# of Refills/Substitution)</p>
<p>for a different eRx. This VistA Rx may or may not be for the same patient</p>
<p>in this eRx being processed.</p>
<p>_________________________________________________________________________</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### VistA Prescriber Class displayed on Single eRx and Pending Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Provider Class will now be displayed in the eRx Holding Queue as well as when viewing an eRx Pending Order, as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name: TEST,PROVIDER MD |Name: TEST,PROVIDER</p>
<p>NPI : 123456789 Phone: 9999999999 |NPI : 123456789 Phone: 9999999999</p>
<p>DEA : XX9999999 |DEA :</p>
<p>Clinic: Wellness Clinic Inc. |Class: PHYSICIAN</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### New Next Drug (ND) hidden action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Next Drug (ND) hidden action was introduced to facilitate the user navigation to the Drug Validation screen for the actionable eRx from a single patient. This new action will work from two different screens in the eRx Holding Queue:

1)  eRx Single Patient Queue: If the user types "ND" in this screen it will take the user to the Drug Validation directly for the first actionable eRx for the current patient.
2)  Drug Validation: If the user types "ND" in this screen it will take the user to the Drug Validation screen for the next (based on eRx Received Date/Time) actionable eRx for the patient. If the patient has only one actionable eRx it will stay in the same eRx. If they current eRx is the last eRx on file for the patient it will loop back to the first eRx.

### Indication functionality added to eRx Holding Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When matching the VistA Drug the user will now be prompted to also enter the Indication. This functionality was only available in CPRS, Complete Orders from OERR \[PSO LMOE FINISH\] and Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] options and it is now being extended to the eRx Holding Queue Processing \[PSO ERX QUEUE PROCESSING\] option as well. If the patient record includes Indication, the user will now see the Indication shown on the Single eRx View/Display landing page. The Indication field will be displayed in the Single eRx View/Display screen as well as in the Drug Validation screen, where it can be edited.

Please, refer to the user documentation for more detailed information about this new functionality.

### Added RRE and CRE error codes under CCR Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The two error codes listed below have been added under CCR Filter. This will enable technicians to monitor and examine the RxChangeRequest/RxRenewalRequest sent either by the VA eRx hub software or by the outside prescribers.

CRE RxChangeRequest Inbound Error

RRE RxRenewalRequest Inbound Error

### Patient DOB check on Edit and Accept Validation warning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When editing or accepting validating the VistA patient, if there the DOB of the eRx Patient does not match the DOB of the VistA Patient, the warning below will be displayed:

<u>Editing:</u>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* WARNING(S) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patient DOB mismatch (eRx: 01/01/1950 \| VistA: 06/16/1936)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Would you like to use this patient? NO//

<u>Validating:</u>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* WARNING(S) \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Patient DOB mismatch (eRx: 01/01/1950 \| VistA: 06/16/1936)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Would you like to mark this patient as VALIDATED?

### Memorize the VistA patient when eRx is selected (\<SPACE BAR\>)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user selects an eRx that has a VistA Patient matched to it, the VistA patient will now be memorized as the last patient accessed by the user, therefore when the user type \<SPACE BAR\> at a VistA PATIENT prompt, it will automatically select the VistA Patient matched to the eRx.

### HFF for Un-Accept and Un-Remove will now ask for Future Fill Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Un-Accepting or Un-Removing an eRx and selecting the hold code HFF (HOLD FOR FUTURE FILL) the software was not prompting the user to select a 'Future Fill Hold Date', which indicates when the eRx should be automatically be un-held. This was causing the eRx to be unheld immediately after being put on hold. This will be fixed with this patch.

### IAS (Include All Statuses) action extended to Rx Medication Queue as well

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IAS action that was only available at the eRx Single Patient Queue will now be available in the Rx Medication Queue as well. This action is used to indicate that all eRx statuses should be included in the list and it will behave as such for the Rx Medication Queue as well.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>eRx Medication Queue</strong> Jun 03, 2025@10:16:05 Page: 1 of 3</u></p>
<p>LOOK BACK DAYS: <strong>365</strong> CS/NON-CS: <strong>BOTH (II-V)</strong> MAX. QUEUE SIZE: <strong>999</strong></p>
<p>ERX STATUS: <strong>ALL</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th># PATIENT DOB DRUG PROVIDER STA REC.DAT<strong>^</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>1. MBMONE,TESTONE TEST 02/02/75 IBUPROFEN 200MG TAB PROVIDR,TST I 09/03/24</p>
<p>2. TESTONE,MBMONE 02/23/46 CHOLECALCIF 25MCG (D3 PROVIDR,TST HC 09/23/24</p>
<p>3. PATIENT,TESTER 09/10/45 Spiriva with HandiHal PROVIDR,TST N 09/24/24</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>+ Enter ?? for more actions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>SPAT Sort By Patient SQ Search Queue LBD Change Look Back Days</p>
<p>PC Patient Centric View RAF Remove All Filters REF Refresh List</p>
<p>Select Item(s): Next Screen// ??</p>
<p>The following actions are also available:</p>
<p>CS Group By CS RXF Rx Refill Only FS First Screen</p>
<p>SDOB Sort By DOB IE Inbound Errors Only LS Last Screen</p>
<p>SDRU Sort By Drug OE Outbound Errors Only GO Go to Page</p>
<p>SPRO Sort By Provider CA Cancel Rx's Only PS Print Screen</p>
<p>SSTA Sort By Status CN Cancel Response Only PT Print List</p>
<p>SREC Sort By Received DateCX Change Response Only PT Print List</p>
<p>CV Change View DET Show/Hide Details SL Search List</p>
<p>RRQ Renewal Request Only + Next Screen QU Quit</p>
<p>RRP Renewal Response Only- Previous Screen IAS Include All Statuses</p>
<p>NEW New Rx's Only UP Up a Line</p>
<p>CR Change Request Only DN Down a Line</p>
<p>Type &lt;Enter&gt; to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### eRx Prescriber Phone \# displayed on Pending Order and Active Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eRx Prescriber Phone \# will now be displayed for the eRx Pending Order as well as for an ACTIVE eRx prescription.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Pending order:</u></strong></p>
<p>Name: TEST,PROVIDER MD |Name: TEST,PROVIDER</p>
<p>NPI : xxxxxxxxxx Phone: 9999999999 |NPI : xxxxxxxxxxx Phone: 9999999999</p>
<p>DEA : XX9999999 |DEA :</p>
<p>Clinic: BFS - Gastroenterology |Class: NURSE PRACTITIONER</p>
<p><strong><u>Active order:</u></strong></p>
<p>eRx HT: (cm)() eRx WT: (kg)()</p>
<p>eRx Provider: xxxxxxxxxxxxxx DEA: xxxxxxxxxx</p>
<p>eRx Phone: xxxxxxxxxx NPI: xxxxxxxxxx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### VistA Drug Edit capability on the Single eRx View/Display screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When viewing the eRx int he Single eRx View/Display screen the users will now be able to edit the drug fields. Before, this capability was only available in the Validate Drug (VD action) screen. This will allow users to do quick edits such as Indication or Patient Instructions field without having to go into the Validate Drug screen. The edit can be done exclusively by typing the \# of the field the user intends to edit, if \#1 (Drug) is selected the user will be prompt to edit all other fields as well. This sample shows \#'s before each editable field:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Single eRx View/Display</strong> Jun 02, 2025@14:40:52 Page: 1 of 4</u></p>
<p>eRx Patient: <strong>MBMONE,TESTONE TEST</strong> eRx Reference #: <strong>2024070000001</strong></p>
<p>eRx Msg Type: <strong>NEWRX</strong> Written: <strong>07/01/24</strong></p>
<p>eRx Status: <strong>HC - HOLD DUE TO CHANGE</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ERX | VISTA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT AUTO-MATCHED/EDITED | VALIDATED by USER,USERONE Z on 7/1/24@17:34</td>
</tr>
</tbody>
</table>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>DRUG/SIG SUGGESTED | VALIDATED by USER,USERONE Z on 11/2/24@14:55:54</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>Drug: Suprep Bowel Prep Kit 1.6 g-17 |1)Drug: COLON ELECTROLYTE LAVAGE ORAL</p>
<p>g-17.5 g/177 mL liquid | SOLN KIT</p>
<p>Drug Form: LIQUID DOSAGE FORM | * NON-FORMULARY *</p>
<p>Substitution? YES Renewals? YES |</p>
<p>SIG: |SIG:</p>
<p>354 ml orally 177 ml evening before| TAKE 1 KIT BY MOUTH EVERY MORNING</p>
<p>and 177 morning of colonoscopy |</p>
<p>Prescriber Drug Use Evaluation: | Verb: TAKE</p>
<p>None |2) Dosage: 1 KIT</p>
<p>| Route: ORAL</p>
<p>| Schedule: QAM</p>
<p>|</p>
<p>|3)Patient Instructions:</p>
<p>|</p>
<p>Provider Notes/Comments: |4)Provider Comments:</p>
<p>|</p>
<p>|5)Pat. Status: SC</p>
<p>|</p>
<p>Quantity: 354 |6)Quantity: 33</p>
<p>Dispense Unit: MILLILITER | Dispense Unit: TAB</p>
<p>Qty Qualifier: Original Quantity |</p>
<p>Days Supply: 1 Refills: 0 |7)Days Supply: 33 8)Refills: 11</p>
<p>|9)Routing: MAIL</p>
<p>|10)Clinic: CWM/NO/PHARM/INBOUND ERX</p>
<p>Written: 07/23/24 Effective: |</p>
<p>Primary Dx: |11)Indications:</p>
<p>...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### After AV it will go back to Single eRx View/Display (VAMC's only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A small change was made to streamline the processing of eRx's. Once the user accepts validation (AV action) for a patient, provider or drug, the software will take them automatically to the Single eRx View/Display screen. This ways they don't have to type "^" or \<ENTER\>'s in order to go back to the Single eRx View/Display screen.

### Default for Copy PATIENT INSTRUCTIONS from Rx#12345? Y// changed to 'NO'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When accepting a VistA Drug suggestion for an eRx, the software prompts the user if they also want to copy the Patient Instructions from the suggested VistA Rx if it has this field populated. The default for this prompt was 'YES' and it is being changed to 'NO'.

### Jump to eRx (JE) action modification at the Patient level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Jump to eRx (JE) action used to jump from Backdoor Pharmacy back to the eRx Holding Queue is being modified to included all variations of the eRx Patient that are matched to the same VistA Patient. Instead of jumping to the eRx Single Patient Queue the user will now be taken to the eRx Medication Queue with the VistA Patient filter automatically set with the patient that was selected in Backdoor Pharmacy. Therefore, the list items will include all eRx's from all eRx Patients that have been matched to the VistA Patient.

### DEA Nightly Update Job w/ Data from DEA/DOJ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new menu option called DEA Number Nightly Update with DEA/DOJ Data \[PSO DEA/DOJ NIGHTLY DATA UPD\] is being created by this patch. This option is used for automatically updating the Kernel DEA NUMBERS file (#8991.9) with the latest prescriber DEA information from DEA/DOJ database. It will run nightly and it will update DEA data for entries that are 30 days or less from expiring. This new option will be added to the list of options that can be edited via the existing Queue Background Jobs \[PSO AUTOQUEUE JOBS\] option.

### Patient address will ignore differences between similar words

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient address comparison between eRx and VistA patients is being enhanced to recognize and ignore these differences listed below by not reversing the video if these are the only difference between the addresses:

| DR = DRIVE       | APT = APARTMENT | STE = SUITE    |
|------------------|-----------------|----------------|
| AVE = AVENUE     | W = WEST        | S = SOUTH      |
| ST = STREET      | NW = NORTHWEST  | SW = SOUTHWEST |
| HGWY = HIGHWAY   | NE = NORTHEAST  | SE = SOUTHEAST |
| BLVD = BOULEVARD | CT = COURT      | RD = ROAD      |
| TER = TERRACE    | PKY = PARKWAY   |                |

### Conversion issue with Patient Weight when prescriber sent in g (grams)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the outside prescriber sent in a patient weight in grams (g) the software was not making the proper conversion to kilograms and it was displaying the value in grams with a 'kg' indication in the Patient Validation scree, as shown below:

...

Weight(kg): 107161.2 \|Weight(kg): 107.95

...

After fix:

...

Weight(kg): 107.16 \|Weight(kg): 107.95

...

### HFF (Hold for Future Fill) will now set the Effective Date if none

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an eRx is received without an Effective Date value and No Refills and the user decides to hold it with a future fill date (HFF), if the date entered by the user is more than 30 days from the eRx Written Date the software will set the Effective Date on the eRx with the future date entered by the user when placing the eRx on Hold with the HFF code.

### MbM Only: CAO status will automatically be set with CAA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a cancelation is received from the outside prescriber and the eRx status is set to CAO (CANCEL PROCESS COMPLETE) the software will automatically set it to CAA (CANCEL REQUEST ACKNOWLEDGED) for Meds-by-Mail sites. The reason is because the volume of CAO records at Meds-by-Mail makes it impossible to acknowledge them manually one by one.

### Cancelations of RxRenewal and RxChange were not DCing Pending/Active Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a RxRenewal or Rx Change response had been processed from the eRx Holding queue and were either on the Pending or Active order queue and the outside prescriber sent in a cancellation for the renewal or accepted change request the software was failing to properly cancel (DC) the pending or active order for the corresponding medication. This issue is being addressed by this patch.

### Allergies compare between eRx and VistA were Case Sensitive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When comparing incoming list of allergies from the external prescriber with the list of VistA allergies the software was performing a case sensitive comparison. In other words, if the outside prescriber sent in 'Tomato' and in VistA we had 'TOMATO' it would reverse the video on both because it assumed them to be different. This issue is being addressed by this patch.

### Update to the Pharmacist Enter/Edit \[PSO RPH\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously this option was used to allocated and de-allocate the PSORPH key that identifies a user as a pharmacist on the system. It is now being modified to allow allocation and de-allocation of the following eRx keys:

PSO ERX WORKLOAD TECH

PSO ERX WORKLOAD RPH

These keys are mostly used by MbM to flag a user as a workload processing technician or pharmacist, which prevents them from skipping orders, effectively imposing a FIFO (First-In-First-Out) processing of incoming eRx and Pending orders.

### New option for Batch Change Request and VistA Drug Replacement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option Batch eRx Change Request/VistA Drug Replacement \[PSO ERX BATCH CH REQ/DRUG SWAP\] placed under the Supervisor Functions \[PSO SUPERVISOR\] menu option. It is used to perform two distinct tasks:

Submission of Multiple eRx Change Requests

Replacement of the Vista Dispense Drug on finished prescriptions (MbM only)

The user will respond few prompts, specifically to the task they want to perform, a list will be presented before the user actually perform the update. The Replacement of the VistA Dispense Drug is available to MbM (Meds-by-Mail) only users. For more information about this option please review the user documentation released along with this patch.

### eRx Pending Order Suggested FILL DATE auto calculation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, the Fill Date field for an eRx Pending Order is always set to the current date. In some cases this is not ideal because the patient might still have enough medication to last a few more days and a future fill date, based on the last fill for the medication might be more appropriate.

The algorithm will auto calculate the suggested Fill Date using the

following logic:

Requirement:

\- A previous prescription for the exact same drug must be found on the

patient's profile

\- The SIG from the previous prescription must match exactly with the

SIG for the new eRx Pending Order

Suggested Future Fill Date:

\- If the Last Fill in the in the existing prescription is released and the Release Date + Days Supply results in a future date, this future date will be suggested as the Fill Date for the eRx Pending Order.

\- If the CMOP Transmission status for the Last Fill is TRANSMITTED or

RE-TRANSMITTED, the Fill Date for the eRx Pending Order will be

today's date + Days Supply for the Suspended fill.

\- If Last Fill is Suspended with a future Fill Date this future date

will be suggested as the Fill Date for the eRx Pending Order.

# Reflection Terminal Display Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Although not required to use the new *eRx Holding Queue Processing* \[PSO ERX QUEUE PROCESSING\] option, for you to have a better user interface experience it’s important that you adjust a few settings on your Reflection Terminal application. Below you will find a step-by-step on how to set the colors on your terminal display that works best for you.

> STEP 1 – Click on Display below to open the Terminal Display Settings on your Reflection application. Some Reflection applications may have a different top menu layout, which you will have to find this “Display” menu item via a different path.

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/002.png)

> STEP 2 – When the window below opens, click on <u>Modify the currently selected theme file.</u>

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/003.png)

> STEP 3 – Scroll down until you find the “Text Color Mapping” section. Here is where you will be able to set the color scheme that works best for you.

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/004.png)

Once you reach this color mapping you can adjust the colors by clicking on the “Change” button specific to each text feature supported by the terminal. See below for a few examples on where each setting is used in the new option:

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/005.png)

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/006.png)

> ![](pso-7-0-770-inbound-eprescribing-mbm-class-3-to-class-1-conversion-release-notes/007.png)

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites Software and Documentation Retrieval Instructions:

Upon National Release the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

https://www.va.gov/vdl/

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 40%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>File Name</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Installation Guide - Inbound ePrescribing (PSO*7.0*770)</td>
<td><p>PSO_7_0_P770_DIBRG.docx</p>
<p>PSO_7_0_P770_ DIBRG.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>User Manual – Inbound ePrescribing – Unit 7 Part 1 (PSO*7.0*770)</p>
<p>User Manual – Inbound ePrescribing – Unit 7 Part 2 (PSO*7.0*770)</p></td>
<td><p>PSO_7_0_P770_UM_71.docx</p>
<p>PSO_7_0_P770_UM_71.pdf</p>
<p>PSO_7_0_P770_UM_72.docx</p>
<p>PSO_7_0_P770_UM_72.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>Technical Manual/Security Guide - Outpatient Pharmacy V.7.0 (PSO*7.0*770)</td>
<td><p>PSO_7_0_P770_TM.docx</p>
<p>PSO_7_0_P770_TM.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>Release Notes – Inbound ePrescribing (PSO*7.0*770)</td>
<td><p>PSO_7_0_P770_RN.docx</p>
<p>PSO_7_0_P770_RN.pdf</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>