---
consolidated_title: "mocha release notes"
app_code: PSO
doc_type: release-note
master_source: "MOCHA Version 2 Release Notes"
master_pub_date: March 2014
consolidated_from: 2 versions
prior_versions:
  - "MOCHA Version 1 Release Notes"
---

<!-- image -->

Medication order check healthcare application (mocha) v2.0

Release Notes

PSJ*5*252, PSO*7*372, and OR*3*345
(MOCHA 2.0 Combined Build 1.0)

PSJ*5*257, PSO*7*416, OR*3*311, and GMRA*4*47
(MOCHA 2.0 FOLLOW UP Combined Build 1.0)

PSS*1*160, PSS*1*173, and OR*3*381 (Stand Alone)

PSJ*5*299 and PSO*7*431

(MOCHA 2.0 FAST TRACK BUILDS 1.0)

March 2014

<!-- image -->

Product Development

*(This page included for two-sided copying.)*

**Table of Contents**

1.	Introduction	1

2.	Enhancements	2

3.	Menu Changes	3

3.1.	New Options	3

3.2.	Changed Options	4

3.3.	Deleted Options	4

3.4.	New Files	4

3.5.	New Fields	4

3.6.	Modified Fields	5

3.7.	Security Key	5

3.8.	Modified Templates	5

4.	Other Functionality	6

4.1.	PSS*1.0*160	6

4.2.	OR*3*345	7

4.3.	OR*3*311	8

5.	Impacts to Other Package	9

6.	Known Anomalies	9

*(This page included for two-sided copying.)*

## Introduction

The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of Pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, Medication Order Check Healthcare Application (MOCHA) v1.0, implemented enhanced order checking functionality utilizing Health *e* Vet (H *e* V) compatible architecture and First Databank (FDB) MedKnowledge Framework (formerly DIF) Application Program Interfaces (APIs), and database for Drug Interaction and Duplicate Therapy order checks. MOCHA v2.0 implements one of two Dosing Order Checks, Maximum Single Dose Order Check for simple and complex medication orders.

This release notes document provides a brief description of the new features and functions of the MOCHA v2.0 patches listed in the table below. More detailed information on the functionality can be found in the application user and technical manuals found on the Virtual Documentation Library (VDL).

| Application                                | Patch                |
|--------------------------------------------|----------------------|
| Outpatient Pharmacy                        | PSO*7*372, PSO*7*416 |
| Inpatient Medications                      | PSJ*5*252, PSJ*7*257 |
| Pharmacy Data Management (PDM)             | PSS*1*160, PSS*1*173 |
| Computerized Patient Records System (CPRS) | OR*3*345, OR*3*311   |
| Adverse Reaction Tracking                  | GMRA*4*47            |

## Enhancements

MOCHA v2.0 will provide the following enhancements:

**Enhanced Order Checking Features:**

- Implement Maximum Single Dose Order Check for simple and complex orders in Outpatient Pharmacy, Inpatient Medications, and CPRS applications
- Provide error messages with reasons at the order level when a Maximum Single Dose Order Check cannot be performed for Pharmacy users
- Provide a generic error message at the order level when a Maximum Single Dose Order Check cannot be performed for CPRS users
- Add a check during installation to see if Pre-Release setup work – mapping of local medication routes and population of numeric dose and dose unit fields for local possible dosages has been completed
- Add new fields to the ADMINISTRATION SCHEDULE file (#51.1) to support the ability to exclude a schedule from all Dosing Checks or just from a Daily Dose Order Check
- Modify *Standard Schedule Edit* [PSS SCHEDULE EDIT] option to allow editing of the new dosing exclusion fields
- Modify *Administration Schedule File Report* [PSS SCHEDULE REPORT] option to display data entered in the new dosing exclusion fields
- Apply the ‘all Dosing Checks exclusion' for a schedule when processing outpatient and inpatient medication orders through Pharmacy and CPRS
- Create a new Pharmacy Data Management (PDM) option called *Lookup Dosing Check Info for Drug* [PSS DRUG DOSING LOOKUP] so that a user can view all data that can affect Dosing Order Checks for a drug
- Add new entries to the DOSE UNITS file (#51.24)
- Provide option (locked with security key) to enable/disable Dosing Order Checks
- Provide notification when Dosing Order Checks enabled/disabled (via email when disabled or enabled)
- Provide audit trail for enabling/disabling of Dosing Order Checks
- Creation and auto enabling of new DOSING\_INFO web service
- Provide option to identify drug names with trailing spaces called *Drug Names with Trailing Spaces* [PSS TRAILING SPACES REPORT]
- Modified option *Check Vendor Database Link* [PSS CHECK VENDOR DATABASE LINK] to show Domain Name Service name for the MOCHA server when displaying the connection status

## Menu Changes

Patch PSS*1*160 introduces a menu change to the *Pharmacy Data Management* menu. Details on the new options can also be found in the *Pharmacy Data Management (PDM) User Manual Version 1.0* and *Pharmacy Data Management (PDM) Technical Manual/Security Guide Version 1.0* .

**Restructured Pharmacy Data Management menu** (changes are bolded)

Select Pharmacy Data Management Option: ??

CMOP Mark/Unmark (Single drug) [PSSXX MARK]

**&gt; Locked with PSXCMOPMGR

**Dosages … [PSS DOSAGES MANAGEMENT]**

Dosage Form File Enter/Edit [PSS DOSAGE FORM EDIT]

Enter/Edit Dosages [PSS EDIT DOSAGES]

Most Common Dosages Report [PSS COMMON DOSAGES]

Noun/Dosage Form Report [PSS DOSE FORM/NOUN REPORT]

Review Dosages Report [PSS DOSAGE REVIEW REPORT]

Local Possible Dosages Report [PSS LOCAL POSSIBLE DOSAGES]

Request Change to Dose Unit [PSS DOSE UNIT REQUEST]

**Lookup Dosing Check Info for Drug [PSS DRUG DOSING LOOKUP]**

**Drug Names with Trailing Spaces Report [PSS TRAILING SPACES REPORT]**

Drug Enter/Edit [PSS DRUG ENTER/EDIT]

Order Check Management ... [PSS ORDER CHECK MANAGEMENT]

Electrolyte File (IV) [PSSJI ELECTROLYTE FILE]

Lookup into Dispense Drug File [PSS LOOK]

Medication Instruction Management ... [PSS MED INSTRUCTION MANAGEMENT]

Medication Routes Management ... [PSS MEDICATION ROUTES MGMT]

Orderable Item Management ... [PSS ORDERABLE ITEM MANAGEMENT]

Formulary Information Report [PSSNFI]

Drug Text Management ... [PSS DRUG TEXT MANAGEMENT]

Pharmacy System Parameters Edit [PSS SYS EDIT]

Standard Schedule Management ... [PSS SCHEDULE MANAGEMENT]

Synonym Enter/Edit [PSS SYNONYM EDIT]

Controlled Substances/PKI Reports ... [PSS CS/PKI REPORTS]

Send Entire Drug File to External Interface [PSS MASTER FILE ALL]

IV Additive/Solution ... [PSS ADDITIVE/SOLUTION]

Warning Builder [PSS WARNING BUILDER]

Warning Mapping [PSS WARNING MAPPING]

PEPS Services ... [PSS PEPS SERVICES]

Inpatient Drug Management ... [PSS INP MGR]

### New Options

The following items are the new options:

- *Lookup Dosing Check Info for Drug* [PSS DRUG DOSING LOOKUP] option displays all of the information related to Dosing Order Checks for the selected entry from the DRUG file (#50), VA PRODUCT file (#50.68), and vendor database. This option is found under the *Dosages* menu.
- *Drug Names with Trailing Spaces Report* [PSS TRAILING SPACES REPORT] option lists all active, multi-ingredient DRUG file (#50) entries with Local Possible Dosages defined, and whose drug name has trailing spaces. Drugs not matched to the National Drug file with trailing spaces in the name will also be listed. If the Drug Name is appended to the Local Possible Dosage and optional conjunction in the Computerized Patient Record System (CPRS) order dialogues, a selection of such a dosage could cause the conjunction + drug name to become part of the actual Dosage, instead of just a display enhancement. This can cause the Dosing Order Check to fail, and that extra text could come to Pharmacy as part of the Dosage in the order. These trailing spaces should be cleaned up if possible.
- *Enable/Disable Dosing Order Checks* [PSS DOSING ORDER CHECKS] option is used to enable or disable Dosing Order Checks for Inpatient Medications, Outpatient Pharmacy, and Computerized Patient Record System (CPRS). In order to use this option, the user must hold the new security key PSS ORDER CHECKS. It is NOT exported as part of the main Pharmacy Data Management [PSS MGR] menu option, and should only be assigned to a minimum number of users (usually limited to the Pharmacy Automated Data Processing Application Coordinator (ADPAC) and/or Pharmacy Manager). This option should only be used to disable the Dosing Order Checks upon direction from Pharmacy Benefits Management (PBM).
    - This option should only be used if authorized by PBM. PBM will only authorize if local approval has been granted by the Medical Center Patient Safety Office and the Medical Center Director. PBM should be notified of this decision by the Pharmacy Chief via email to the REDACTED Outlook mail group. In turn, PBM will notify Patient Care Services (PCS), the National Patient Safety Office (NPSO), and the Office of Information and Technology (OIT).

### Changed Options

The following options have been changed:

- The *Standard Schedule Edit* [PSS SCHEDULE EDIT] option has been modified to allow editing of the new dosing exclusion fields. A user will be able to exclude a schedule from either all Dosing Order Checks or just the Daily Dose Order Check.
- The *Administration Schedule File Report* [PSS SCHEDULE REPORT] option has been modified to allow display of the EXCLUDE FROM ALL DOSING CHECKS field (#9) and EXCLUDE FROM DAILY DOSE CHECK field (#10) from the ADMINISTRATION SCHEDULE file (#51.1) for a schedule.
- Modified option *Check Vendor Database Link* [PSS CHECK VENDOR DATABASE LINK] to show Domain Name Service name for the MOCHA server when displaying the connection status.

### Deleted Options

No options have been deleted.

### New Files

No new files have been added.

### New Fields

The following fields have been added:

- The EXCLUDE FROM ALL DOSING CHECKS field (#9) has been created in the ADMINISTRATION SCHEDULE file (#51.1). This field allows a user to exclude a standard schedule from all Dosing Order Checks. If a schedule is entered for a medication order that has this field set to ‘Yes’, no Dosing Order Checks will be performed on the drug within the order.
- The EXCLUDE FROM DAILY DOSE CHECK field (#10) has been created in the ADMINISTRATION SCHEDULE file (#51.1). This field allows a user to exclude a standard schedule from the Daily Dose Order Check. If a schedule is entered for a medication order that has this field set to ‘Yes’, no Daily Dose Order Check will be performed on the drug within the order. The Maximum Single Dose Order Check will still be performed. Please Note: The Daily Dose Order Check will be implemented in a future version of MOCHA. Only the Maximum Single Dose Order Check is introduced with MOCHA v2.0.
- The DOSING ON/OFF field (#95) has been created in the PHARMACY SYSTEM file (#59.7) to indicate if Dosing is On or Off. This field determines whether Dosing Order Checks will be part of the medication ordering process in Inpatient Medications, Outpatient Pharmacy, and Computerized Patient Record System (CPRS). A ‘1’ indicates that Dosing Order Checks will occur; a ‘0’ indicates that Dosing Order Checks will not occur. The DOSING ACTIVITY DATE AND TIME sub file (#82) has been created in the PHARMACY SYSTEM file (#59.7). The DOSING ACTIVITY DATE AND TIME field (#.01) stores the date and time the Dosing Order Checks were either enabled or disabled. It is set when the DOSING ON/OFF field (#95) is edited. The PERSON MAKING CHANGE field (#1) documents the person making the change to the DOSING ON/OFF field (#95). The ENABLE/DISABLE field (#2) indicates what change was made to the DOSING ON/OFF field (#95). A ‘0’ indicates the Dosing Order Checks were disabled, a ‘1’ indicates the Dosing Order Checks were enabled.
- The IMO DC/EXPIRED DAY LIMIT field (#6) has been created in the CLINIC DEFINITION file (#53.46) to allow entry of a number of days that discontinued/expired IMO orders will be included in Enhanced Order Checks (Drug Interactions and Therapeutic Duplications).

### Modified Fields

The DOSE WARNING field (#8) in the RX VERIFY file (#52.4) has been modified to add another code of ‘4’ to indicate when the ‘DOSAGE EXCEEDS MAX SINGLE DOSE’.

### Security Key

A new security key has been created called PSS ORDER CHECKS. This key will be used for functions related to medication order checks. It is used to lock the *Enable/Disable Dosing Order Checks* [PSS DOSING ORDER CHECKS] option.

### Modified Templates

The PSSJ SCHEDULE EDIT Input template has been modified to allow editing of the EXCLUDE FROM ALL DOSING CHECKS field (#9) and the EXCLUDE FROM DAILY DOSE CHECK field (#10) in the ADMINISTRATION SCHEDULE file (#51.1).

## Other Functionality

### PSS*1.0*160

The environment check routine will perform the following tasks:

- A check will be made to verify whether the MOCHA v1.0 Pre-Release setup work has been completed.
- Verification that all local medication routes have been mapped will be made.
- Verification will be made that all local possible dosage data (numeric dose and dose unit fields) have been populated.
- If either the local medication routes mapping and/or the local possible dosage data population has not been completed, the installer will be displayed a message informing them of this and then prompted with whether or not they want to continue. If all work has been completed, the user will be informed and the program will automatically continue on. The consequence of continuing installation if either of these tasks have not been completed is that dosage checks will not work for those orders that contain unmapped local medication routes and may not work for local possible dosages that have missing data.
- A Mailman message will also be generated with the same information to the installer and members of the PSS ORDER CHECKS mail group.

It should be noted that not all medication routes can be mapped at this time. For a few medication routes (Intrathoracic, Intrafollicular) it was recommended that they be left unmapped. Because of this, all sites will see a warning message that not all medication routes have been mapped during the install and the installer will be prompted to continue. Below is an example of the warning message:

*There are still local Medication Routes marked for 'ALL PACKAGES' not yet mapped. Any orders containing an unmapped medication route will not have dosage checks performed. Please refer to the 'Medication Route Mapping Report' option for more details.*

If the Pharmacy Automated Data Processing Application Coordinator (ADPAC) has completed the rest of the required mapping, then the installer should continue with the installation.

The POST-INIT routine PSS160PO will perform the following tasks:

- Add the new option, *Lookup Dosing Check Info for Drug* [PSS DRUG DOSING LOOKUP], to the *Pharmacy Data Management* menu structure.
- Attach the Drug Names with Trailing Spaces Report [PSS TRAILING SPACES  REPORT] option to the Dosages [PSS DOSAGES MANAGEMENT] Menu Option.
- Generate the mail message indicating the POST-INIT routine has run to completion.
- Add two new entries to the DOSE UNITS file (#51.24). They are FILM(S) and ELISA UNIT(S).
- Modify the MILLIONUNIT(S) entry in the DOSE UNITS file (#51.24) to add two new synonyms: MILLION UNIT and MILLION UNITS.
- Automatically add and enable the DOSING\_INFO web service to the Pharmacy Product Enterprise System (PEPS) Server so that FDB information can be retrieved for the Pharmacy Data Management (PDM) *Lookup Dosing Check Info for Drug* [PSS DRUG DOSING LOOKUP] option.
- Turn the Dosing Order Checks functionality on.

### OR*3*345

OR*3*345 is part of the MOCHA 2.0 COMBINED BUILD. This patch will address the following issues:

- On the copy/renew/change of an Infusion or Unit Dose order where the Dispense Drug was not matched to the National Drug File, there were multiple duplicative messages indicating the order checks could not be done. The duplicate messages will now only display once.
- When a pending order does not have a Dispense Drug assigned and all drugs associated with the Orderable Item are matched to National Drug File and another order is placed for the same drug, both a Duplicate Drug and Duplicate Therapy Order Check are displayed. This has been modified such that in this situation only the Duplicate Drug Order Check will display.
- The status of a Non-VA Medication order was occasionally showing as PENDING in the DRUG-DRUG Interaction Order Checks when it was in fact ACTIVE. Now the status will show as "ACTIVE NON-VA" when an active Non-VA Medication order is included in a Drug Interaction.
- CPRS was displaying duplicate exception messages when Order Checks could not be done for a drug. With this patch, only a single exception message is shown.
- For 2 unsigned medication orders that result in a Drug Interaction and both have Dispense Drugs, upon signing either one you get the order check showing the interaction with the other, which is correct. However, if one of them is entered as a Free Text Dose and the other has a Dispense Drug, then when signing the order that has a Dispense Drug the Drug-Drug Interaction Order Check was not firing. This has been addressed such that in all cases the correct Drug-Drug Interaction Order Check displays.
- Unit Dose Complex medication orders do not generate Duplicate Drug Order Check on Accept for Renewal. This now works as expected.
- CPRS can now handle displaying multiple messages relating to General Dosing Order Checks for a complex medication order.
- After the release of OR*3*294, Cache would log the following error in the error trap when Remote Data Interoperability could not connect to the Health Data Repository: &lt;FUNCTION&gt;zSend+2^%Net.HttpRequest. Since an InterSystems Fix would take too long to be released it was decided to preempt the error in the Order Entry code so that the error should no longer be displayed in the error trap.
- In certain scenarios, DRUG INTERACTION would be displayed as the status of a medication order in the DRUG-DRUG Interaction Order Check instead of PENDING or NON-VERIFIED. With this patch the correct status will be displayed.
- When a drug was entered that was not matched to National Drug File, two exception messages were returned as order checks that the order checks could not be done. Only one relevant message will now be displayed.
- When the First Databank (FDB) database was down or inaccessible, information from the message, that lists what order checks were not displayed, was being dropped when signing off or when the order check information became stored with the order. This has been fixed.
- When an Orderable Item was set up as both an Additive and a non-premix Solution, CPRS never performed Enhanced Order Checks on the Orderable Item when it was marked as an Additive in an infusion order. Additionally, for an infusion order with a non-premix Solution and an Additive, CPRS performed Enhanced Order Checks for both the non-premix Solution and the Additive. CPRS should never perform Enhanced Order Checks on non-premix Solutions. With this patch, CPRS will only perform Enhanced Order Checks on all Orderable Items in an infusion order that are either an Additive or a premix Solution.
- When an Infusion was being entered via CPRS the FDB database was being accessed for each of the components (Additives and Solutions) in the order and thus creating slowdowns for the user. This has been streamlined now to only access the database once for Dosing Order Checks and once for Enhanced Order Checks.
- If a Unit Dose or Outpatient drug is selected, a free text dose is entered and before the order is accepted all of the dispense drugs are inactivated in Outpatient Pharmacy Backdoor, no Order Checks will occur and no message will display indicating that Order Checks were not done. In this situation, CPRS will now let the user know that the Order Checks were not done and that they should do manual checks.
- Exception messages were not being displayed for Prospective (newly entered) drug orders when order checking. This has been fixed such that any exceptions on the new order being entered will show to the user.
- If an Orderable Item is marked as a supply in the scenario where there are a mixture of Dispense Drugs (marked as supply or not supply) tied to that Orderable Item, if a medication is entered through CPRS which would normally result in Duplicate Therapy Order Check, the Duplicate Therapy Order Checks are screened out and not displayed. It appears this only affects the prospective drug. Now CPRS will not screen out supply items that the Duplicate Therapy Order Checks are based on and the screening is done on the Pharmacy side for the specific Dispense Drug instead of at the Orderable Item level.
- Lab Result Order Checks will only fire on the first entry to the LOCAL TERM TEXT multiple (#860.91) in the ORDER CHECK NATIONAL TERM file (#860.9) if there is more than a single entry. This would cause only the first entry to be returned as an Order Check, when there may be other more recent results. Routine ORKPS has been modified to search through all entries in the LOCAL TERM TEXT multiple (#860.91) for matches, then return the most recent result.

### OR*3*311

OR*3*311 is part of the MOCHA 2.0 FOLLOW UP COMBINED BUILD. This patch will address the following issues identified by the MOCHA v2.0 test sites:

- When a medication quick order is created with a dosage that does not match any of the local possible dosages associated with that medication, the creator is not warned that Dosing Order Checks may not work when the quick order is used to create an order. This patch will enable the software to warn the quick order creator of the unmatched dosage.
- When a medication quick order is created for a drug using a local possible dosage and the drug name contains lowercase characters, the quick order will not have a dispense drug attached to it and Dosing Order Checks will not occur on orders created with this quick order. This patch will enable the software to warn the quick order creator that dosage order checks will not occur.
- When a prescription is entered through Outpatient Pharmacy Backdoor with a local possible dosage and the associated Computerized Patient Record System order is either transferred to inpatient or copied and then changed, the dosage is converted to free text preventing the software from executing the Dosing Order Check. This patch will prevent the software from converting the local possible dosage to free text.

## Impacts to Other Package

OR*3* 345 will be released in the MOCHA V. 2.0 combined build with PSO*7*372 and PSJ*5*252. It provides CPRS functionality for the Maximum Single Dose Order Check. OR*3*311 will be released in the MOCHA V. 2.0 follow up combined build with PSO*7*416 and PSJ*5*257.

Previously nationally released patch OR*3*366 has two new options that were added to the Order Menu Management [ORCM MGMT] menu option. They are:

- *Quick Order Mixed-Case Report* [OR QO CASE REPORT] identifies quick orders that potentially had the DRUG name edited such that when the quick order is loaded in CPRS the dosage that is saved with the quick order does not match any of the dosages available for selection in the list. This causes the Dosing Order Checks not to be able to be performed correctly. The edit to the drug that this specifically looks for is a case change to the DRUG name. If the name is changed so that it contains different characters that are not just case changes, this report will not identify them.
- *Quick Order Free-Text Report* [OR QO FREETEXT REPORT] identifies Medication Quick orders that have a free text dosage that does not match exactly one of the Local Possible Dosages from Pharmacy.

The above options were created to assist sites in identifying quick orders that require some cleanup for Dosing Order Checks to perform successfully.

## Known Anomalies

List of Outstanding Anomalies:

1. Problem Reporting System Number: **CCR6721**
    - 1.1. Charleston reported "Dc'ed due to Edit" orders for non-verified orders display in order checks in Inpatient Meds
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: Although there are additional orders included in the Order Check display, all orders that should be included are.
    - 1.5. Fixed in PSJ*5*299

1. Problem Reporting System Number: **CCR6704**
    - 1.1. Orders edited then immediately verified in Inpatient Meds do not kill the IMO cross reference
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: The IMO cross reference will take up some additional space, but Order Checks will not be slowed down because the system looks at a specified time frame for the clinic.
    - 1.5. Fixed in PSJ*5*299

1. Problem Reporting System Number: **CCR6682**
    - 1.1. Dose check in Outpatient Pharmacy scrolls off the screen.
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: The dosing warning or error message will only scroll off the screen for a patient that has a long list of disabilities. This should occur infrequently. The user has the ability to scroll back to view the dosing warning/error message.
    - 1.5. Fixed in PSO*7*431

1. Incorporate PSJ*5*285: **CCR6732**
    - 1.1. With v14 of MOCHA v2.0 FOLLOW UP COMBINED build the routine PSIVORFB was included in the last build for Inpatient, and this routine was missing nationally released PSJ*5*285 changes. PSJ*5*285 was a VistA Maintenance patch and did not have a patient safety. The missing line of code was restored and the 2nd line of the routine was changed to reflect PSJ*5*285.
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: In PSJ*5*299 fast track release patch, the missing line of code was restored and the 2nd line of the routine was changed to reflect PSJ*5*285.
    - 1.5. Fixed in PSJ*5*299

1. Post Install routine needs a re-start function: **CCR6710**
    - 1.1. CLIN 1 Support installed MOCHA 2.0 FOLLOW UP COMBINED build in their account and an error occurred during indexing of the PHARMACY PATIENT file (#55) within Inpatient Medications. The error was caused by an invalid entry in the file, which was subsequently removed. In order to complete the post install, it was necessary to reinstall the patch. To eliminate having to reinstall the build when such an error occurs, a restart function was added to allow IRM's to run the post install separately. From the programmers command prompt (&gt;), sites can restart the post install by typing: D RESTART^PSJ299PO
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: The post install routine will re-index the CIMO cross reference for NON-VERIFIED ORDERS file (#53.1) and the CIMOU, CIMOCLU, CIMOCLI, and CIMOI cross references for PHARMACY PATIENT file (#55). This will clean up any old IMO cross references created as a result of CCR6704 and CCR6721.
    - 1.5. Fixed in PSJ*5*299

1. Problem Reporting System Number: **CR6748**
    - 1.1. A Maximum Single Dose Order Check cannot be performed for complex orders that have a Drug Name in the Dosage/Instructions due to trailing spaces in the Drug Name because the dosage cannot be interpreted.
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: Sites can remove trailing spaces from all their drug names in the Drug file and continue to monitor. A national utility released with patches OR*3*378 and PSO*7*433 can be run periodically.
    - 1.5. Fixed in CPRS GUI v30.

1. Problem Reporting System Number: None (data clean-up)
    - 1.1. Orders have Drug Name part of Dosage/Instructions and/or Date part of Dosage/Instructions
    - 1.2. Risk/Impact: Low
    - 1.3. Workaround: N/A
    - 1.4. Comments: Sites will be required to  run the National Data-Cleanup Utility (OR*3*378 and PSO*7*433) which are currently under development and have not been released to sites yet. Utility was developed by CPRS and Pharmacy to clean-up existing orders. The utility will look at Outpatient free text orders that have a dispense drug assigned and
    5. Remove the date
    6. Remove the drug name
    7. Replace all sequences of consecutive spaces within the OR GTX INSTRUCTIONS dialog response with a single space
    8. An activity log entry is entered on the order when the instructions are modified noting old and new instructions
    9. A report is generated detailing the changes made by the utility for easy review by the sites If drug name found in instructions will remove
    - 1.5. Code is already fixed in OR*3.0*311 as part of MOCHA v2.0.
2. Dosing issue with CPRS 'Copy/Edits' and 'Changes: **CR6805** (PSPO #2495)
    - 2.1. An order was placed in CPRS by selecting from the Possible Dosage list. The Possible Dosage was deleted, and then the copy or change action was selected in CPRS. This action resulted in the dispense drug from the original order erroneously being used to perform the order checks. This issue has been resolved such that the new free text dosage is used to perform the dosing check in this scenario.
    - 2.2. Risk/Impact: Medium
    - 2.3. Workaround: None
    - 2.4. Comments: This issue has been resolved such that the new free text dosage is used to perform the dosing check in this scenario.
    - 2.5. Fixed in OR*3*384. Progressing to release soon after MOCHA v2.0 deployment.

- Remove leading and trailing spaces.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MOCHA Version 1 Release Notes

## *(This page included for two-sided copying.)*

## Impacts to Other Packages

OR*3* 272 will be released in the combined build with PSO*7*251 and PSJ*5*181.  It provides CPRS functionality for the enhanced drug interaction and duplicate therapy order checks.

OR*3*280 and GUI V28 provide CPRS functionality for the new dosage checks and the ability to display a detailed professional drug interaction monograph. The Dosage checks will not be activated until the release of PSS*1.0*160. PSJ*5.0*226 was released with the GUI V28 and OR*3.0*280 bundle. PSS*1*151 will be released as a host file with CPRS v.28.
