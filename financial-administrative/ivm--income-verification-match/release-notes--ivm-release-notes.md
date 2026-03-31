---
consolidated_title: "ivm release notes"
app_code: IVM
doc_type: release-note
master_source: "IVM Version 2 Release Notes"
master_pub_date: October 1994
consolidated_from: 2 versions
prior_versions:
  - "IVM Version 4.2.5 Release Notes"
---

<!-- image -->

**inCOME VERIFICATION MATCH**

**(IVM)**

**release notes**


October 1994

Information Systems Center

Albany, New York

Table of Contents

Introduction	1

Executive Summary	3

Background	4

Functional Description	5

I.	Introduction	5

II.	Overview	5

III.	Noninteractive Processing	6

IV.	Interactive Processing	11

V.	PIMS and IB Enhancements	17

Introduction

This release of Income Verification Match (IVM) V. 2.0 provides software which will impact the Registration, Medical Care Cost Recovery (MCCR), and Information Resource Management (IRM) staffs at your facility.  There is a significant increase in functionality from the previous version of IVM.

Increased data transmissions between the facility and the

Several on-line options for reporting and data upload purposes

Significant enhancements to the Patient Information Management System (PIMS) Means Test module

Enhancements to the Integrated Billing (IB) package

The previous version of IVM did not include any user options.  IVM V. 2.0 contains an on-line module targeted primarily for two individuals.

Each site should appoint an IVM Coordinator to monitor incoming data transmissions from the .  This individual would receive notices of data transmissions and coordinate the upload of that data into the site's database.  An output menu includes inquiries and reports which may be used to chart overall activity of the IVM program.

An IRM menu provides the IRM staff with the means of monitoring data transmissions leaving the facility.  A purge option allows transmission log entries from inactive cases to be deleted from the database.

IVM V. 2.0 is highly integrated with other Decentralized Hospital Computer Program (DHCP) packages.

PIMS is the feeder of demographic, Means Test, and income information to the .  Means Test and demographic information which has been verified by IVM will be filed back into the PIMS package.

Patient insurance information is extracted from the IB package and transmitted to the .  Means Test charges will be created in IB for patients who become Category C when a verified Means Test from IVM is transmitted to the facility.  Insurance information identified by IVM will be filed into IB.  IB will provide billing and collections information, for billings resulting from IVM activity, which will be transmitted back to the .

The Health Level 7 (HL7) package is used extensively and provides the foundation for all communications between the facility and the .

These release notes contain an Executive Summary which provides a concise statement that describes the impact of this software at your facility.  A background of the IVM process is provided along with a functional description of the software.  These release notes will concentrate on user functionality and not provide technical documentation.  Descriptions of the files, fields, templates, routines, and security keys will be provided in the IVM V. 2.0 Technical Manual.

**Please ensure that copies of these release notes are distributed to the appropriate users.**

Executive Summary

This release of IVM will substantially impact the patient workload at your facility.  The software will automatically refile into DHCP, for veterans who were previously Category A, Means Tests which have been verified by the .  The facility will see a shift of workload from the mandatory to discretionary category.  The automatic change of Means Test category will have several implications beyond placing the veteran in the discretionary category.

Means Test charges will be created for care received by veterans while they were Category A, and then billed to the veteran pending a review by MCCR.  Current or subsequent episodes of care will automatically be billed.

Veterans who were previously exempt from the medication copayment requirement may become nonexempt.  Copayment billing for these veterans will resume when the veteran receives a new prescription.

Patient insurance information which has been identified by the  will be transmitted back to your facility for potential filing into DHCP.  These policies will provide opportunities for the back-billing or subsequent billing of care to third party insurance carriers.  All billing information which has resulted from IVM activity will be compiled nightly for transmission to the .

New SSNs and demographics information will be transmitted to your facility for potential filing into DHCP.  Uploading of a new SSN for a veteran, in particular, will have a significant impact at your site.  Not only will this patient's identifier in DHCP have changed for all DHCP modules, but all paper records which contain the previous SSN will need to be updated.  Guidance from Medical Administration Service (MAS) Department of Veterans Affairs Central Office (VACO) will be forthcoming to provide assistance to sites who choose to change a veteran's SSN.

This version of IVM provides all of the functionality required by the  to return verified Means Test, insurance, and demographic information to the affected VA Medical Center(s).  This package also forms the foundation for the Centralized Means Test (CMT) initiative which is currently in the planning stages at the .  The CMT initiative would centralize the administration of Means Tests at the  and send the results to the VA Medical Center(s) where the patient has recently been seen.  This will alleviate the VAMCs of much of the administrative overhead associated with the Means Test process.Background

Public Law 101-508 permits VA to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income.  The IVM process for Veterans Health Administration (VHA) medical facilities is centralized and performed at the   in .

DHCP IVM V. 1.0, released in August 1993, provided the functionality to transmit patient demographic and income information from the field facilities to the .  All Means Tests completed since January 1, 1993 which meet the following criteria have been transmitted.

Veteran is Category A, but was neither adjudicated nor given a hardship exemption.

Veteran is Category C, but has no active health insurance on file.

The IVM*1*2 patch, mandated for installation in the field in January 1994, augmented this data stream with the total number of inpatient and outpatient days of care received by the veteran since the Means Test date.  All of this information combined will provide the  the ability to compare the income reported to VHA by the veteran with records maintained by SSA and IRS, and then to prioritize the cases which need to be verified, based on the following.

Whether the veteran has active insurance

The total days of care received by the veteran (the inpatient and outpatient days are combined and converted to points)

Whether the veteran's income reported to IRS/SSA exceeds the Means Test threshold (when the income reported by the veteran did not exceed the threshold)

Contact representatives at the  may then begin verification of cases with the highest priority.  Once the Means Test has been updated as a result of verification and the veteran has signed the revised VA Form 10-10F, the new Means Test will then be electronically returned to the field facility for automatic filing into DHCP.

Functional Description

I.  INTRODUCTION

This section will provide a general overview to IVM V. 2.0, followed by a detailed description of both the non-interactive and interactive modules of IVM.  The section will conclude with a description of the PIMS and IB enhancements which accompany the package.

II.  OVERVIEW

DHCP IVM V. 2.0 provides the capability to electronically receive the revised       10-10F and automatically file the updated test in the DHCP Means Test module.  No user interaction will be required.  The original Means Test conducted by the facility will be inactivated, and the IVM test will become the primary (active) test for the test date.  The original test will no longer be editable, but may be viewed and printed.

The automatic filing of the IVM verified Means Test may change the patient's current Means Test status.  If the patient's Means Test status changes from Category A to Category C and the patient received medical care after the Means Test date, Means Test copayment charges for these episodes of care will automatically be created.  The charges will be placed in a "hold" status so that they may be reviewed by MCCR before being passed to Accounts Receivable to be included on the patient's Statement of Charges.

Filing of the verified Means Test may also change the patient's current pharmacy copay exemption status from exempt to non-exempt.  All new prescriptions dispensed to the patient will then be subject to the prescription copayment.

When VHA records are matched by SSA with their records (by SSN and name), some VHA records may be rejected because they could not be matched with any SSA record.  In some cases, SSA will return to VA a recommended SSN for a veteran or spouse.  These SSNs will be transmitted electronically to the field facilities after validation by the .  An upload utility will be available to allow users to review and verify these SSNs, and then either upload or reject the data.  If the SSNs are uploaded, the veteran's Means Test will be retransmitted to the .

The IVM verification process may also result in the discovery of updated demographic or eligibility information.  This information will also be transmitted electronically to the field facilities for review and potential uploading into DHCP.

The IVM verification process also includes sending an inquiry to patients' employers for health insurance information if the patient did not report active health insurance.  Health insurance information which is identified by the  will be electronically transmitted to the field facilities for review and uploading into DHCP.  Sites may optionally upload this information.  After the sites take definitive action on the policy (upload or reject the policy) a confirmation message will be sent to the  to report the decision that was made.

The uploading of IVM Means Tests and health insurance policies may eventually result in additional copayment and third party billings.  The  will perform a statistical analysis on the resultant billing and collections data.  When this information is generated at the field sites, it will be electronically transmitted back to the  during the nightly transmissions.

III.  Noninteractive Processing

With this version of IVM, there are several exchanges of data between the  and the facility.  These exchanges may take place on a scheduled basis, such as when the IVM Nightly job is run, or on an ad-hoc basis when an unsolicited message is received from the .

There are several circumstances which may arise during communications between the two systems where the DHCP user will need to be notified of any problems or results that occur.  The IVM MESSAGES mail group is established with this version and is used to alert DHCP personnel of all results.  Your IVM Coordinator and IRM support personnel should be members of this group.

A.  DHCP Server Functionality

This section describes all of the messages received on an ad-hoc basis from the  and processed.

**SSN Data Transmission**

When the  submits VHA demographic and income data to SSA for matching, SSA may reject the VHA record because it could not be matched with a record of its own.  The rejected records are sent back to the , sometimes with a recommended SSN for the veteran or spouse.  After the  has verified that the SSNs are valid, they need to be transmitted to the field facilities for verification and possible uploading into DHCP.

When this message is received by DHCP, the patient identifier, income year, and social security numbers are checked for validity.  An application error message is returned to IVM if an error is found.  Otherwise, the SSNs are stored in the veteran's case record to await upload by the DHCP user.  A mail message is then sent as a notice of the receipt of the SSNs.  The generation of this notification is controlled by a parameter and may be suppressed.

**Insurance Data Transmission**

As part of the IVM verification process, requests for insurance information are sent to the employers of veterans who do not report active health insurance information in DHCP.  If a health insurance policy is identified by the , the patient policy information may be transmitted to the facility with the Insurance Data Transmission message.  DHCP users would then be able to review the information and either upload or reject the policy.

When this message is received by DHCP, the patient identifier and message segment sequence are verified.  An application error message is returned to IVM if an error is found.  Otherwise, the message segments are stored in the veteran's case record to await upload by the DHCP user.  A mail message is then sent as a notice of the receipt of the insurance information.  The generation of this notification is controlled by a parameter and may be suppressed.

**Demographic Data Transmission**

During the course of verifying a Means Test, contact representatives at the  may determine that certain patient demographic and eligibility information has changed.  The  may electronically transmit these changes to the facility with the Demographic Data Transmission message.  These elements are classified as either uploadable or non-uploadable.  Uploadable elements may be automatically loaded into DHCP; non-uploadable may only be viewed but not loaded into DHCP.  Users may review this data and either load (automatically or manually, depending upon whether the field is uploadable or non-uploadable) or reject the data.

When this message is received by DHCP, the patient identifier and message segment sequence are verified.  An application error message is returned to IVM if an error is found.  If there are no errors, each message element is compared with the corresponding element already on file for the patient in the DHCP database.  Any elements transmitted from the  which differ from what is already on file is stored in the veteran's case record to await upload by the DHCP user.  A mail message is then sent as a notice of the receipt of the demographic and eligibility information.  The generation of this notification is controlled by a parameter and may be suppressed.

**Means Test Data Transmission**

After the IVM verified Means Test is signed by the veteran, the entire 10-10F is electronically transmitted to the field facility in the Means Test Data Transmission message.  The verified Means Test is automatically uploaded into the DHCP database upon receipt.

When a Means Test Data Transmission message is received by DHCP, the new Means Test is filed automatically.  All corresponding annual income and income relation records will also be filed.  Filing of the  verified Means Test results in a mail message being generated.  If the veteran's Means Test category changes to C and the veteran had episodes of care subsequent to the date that the original Means Test was completed, the Integrated Billing package will automatically create copayment charges for those episodes of care.  The charges will be placed in a review status where they may be reviewed by MCCR personnel and then passed to the Accounts Receivables package.

Please note that while the  is verifying the income of the veteran, they will also be verifying the dependent information.  The dependents claimed by the veteran on the IVM-administered Means Test will be considered accurate.  Because dependents are associated with a veteran and not just a single Means Test, it is possible for the addition or removal of a dependent to affect other Means Tests administered for the same patient.  IVM Means Tests which contain changes to the veteran's dependents will be referred back to the  until such time as changes are made in DHCP to associate changes in dependents to the IVM Means Test only.  This functionality is expected to be released to the field as a patch shortly after the release of this version of IVM.

**Case Status Data Transmission**

If neither the income reported to VHA by the veteran nor the income reported to SSA exceed the Means Test threshold, then the Means Test does not need to be verified and the case may be closed.  The  will then inactivate the case in the DHCP database by transmitting a Case Status Transmission message.  The case will automatically be closed upon receipt by DHCP.

This message will be processed immediately upon receipt by DHCP.  If the patient identifiers and income year cannot be verified, an application error message will be sent to the .  Otherwise, the case record will be closed, and further transmissions for that income year for the patient will not occur.  Upon closing the case record, the closure source (IVM), closure reason (Means Test will not be verified), and the closure date/time will be recorded.

**Single Patient Query**

While verifying a Means Test, the  may require the most up-to-date demographic, eligibility, and income information for a veteran.  This information may be obtained by sending a Single Patient Query to the DHCP database to request the data.

The Full Data Transmission is compiled for the veteran and transmitted back to the  upon receipt of the Single Patient Query.  This message is described further under IVM Nightly Background Job in this section.  The Query Date/Time in the patient's case record will also be updated, if it has not been previously, indicating that all future transmissions for this patient for the income year should be Full Transmissions.

**Master Query**

After the  has conducted a match of income data reported to VHA with both SSA and IRS, other demographic and income information is needed for all income cases prior to comparing VHA income to SSA/IRS income and prioritizing the cases.  The  may request a complete information profile for all open cases for an income year by submitting a Master Query to the DHCP database.  Typically, this will occur once per year.

When the Master Query is received by DHCP, the query request is logged in the IVM PARAMETER (#301.9) file.  The request is handled at night when the IVM Background Job is run.  After the response to the Master Query has been transmitted to the , all transmissions for that income year shall be Full Transmissions as opposed to Initial Transmissions.

**Acknowledgments**

The  will respond to all messages generated from the field facilities with an HL7 acknowledgment message which indicates to the transmitting facility whether the original transmission was received with or without error.  All Full and Initial Transmissions generated from the field during nightly processing will be internally logged in the IVM TRANSMISSIONS (#301.6) file.  When an acknowledgment is received, the original transmission being acknowledged will be located in this file.  If no error is reported, the transmission will be flagged as having been successfully received by the .  If an error is reported, the transmission record will be flagged as having an error, and a mail message will be sent to record the error.

B.  IVM Nightly Background Job

The IVM Nightly Background was the sole piece of functionality delivered with IVM V. 1.0.  The purpose of the job was to transmit to the  all Means Tests which meet the IVM criteria.  The prioritization patch to IVM V. 1.0, IVM*1*2, further enhanced this transmission by adding additional data elements to the messages that were sent to IVM.

With this version of IVM, this job has been greatly enhanced and includes four separate jobs.

**Response to Master Query**

The first task during the Nightly Job is to determine the status of the Master Query.  A status of the Master Query request for the income year two years in the past is performed first.  If the request from two years previous has not been satisfied, then the Full Transmission messages for all active cases for that income year are compiled and transmitted.

Otherwise, the status of the previous income year's request is determined.  If the request has not been logged, then the Initial Transmission message is compiled and transmitted for all active cases which have been updated since the job was last run.  If the request has been logged but not satisfied, the Full Transmission message for all active cases for that income year are compiled and transmitted.  If the request has been logged and previously satisfied, then a Full Transmission message is compiled and transmitted for all active cases which have been updated since the job was last run.  Note that if either Master Query is responded to during the Nightly Job, then no other processing takes place.

**"Regular" Nightly Processing**

If a response to the Master Query is not going to be transmitted, then data is only transmitted for those cases which were added or updated since the job was last run.  This functionality currently exists with IVM V. 1.0.  If the Master Query for the previous year had already been satisfied, the Full Transmission message is used for each case; otherwise, the Initial Transmission message is used.  These messages are further described below.

**Initial Transmission**

The initial transmission will be sent to the  for a specific patient if the Master Query for the current income year has not been received, and if a Single Patient query has not been received for the patient.  The initial transmission message will also be transmitted when the patient's Means Test or demographic information changes.  The purpose of the initial transmission is to provide the  with sufficient information to perform a match for the veteran and spouse with SSA.  Once the match is made, the  will send a Master Query to the facilities to collect income and additional Means Test information in order to prioritize the cases for that income year.

**Full Transmission**

Once the  has completed the match with SSA and has retrieved patient earned and unearned income from SSA/IRS, a complete profile of patient Means Test and demographic information from DHCP is needed by IVM to prioritize the case.  The  may solicit a full profile for all patients by issuing a Master Query.  IVM may also request a full profile for a particular veteran at any time by sending a Single Patient Query to a facility.  The complete information profile is transmitted to the  using the Full Transmission message.  The Full Transmission contains all the patient demographic, eligibility, Means Test, income, and episode of care information required by the  to prioritize and verify the case.

**"Retransmission" Processing**

All transmissions three days or older which were not successfully received by the   are examined each evening.  If the transmission is "Awaiting Transmission" by the VA MailMan, a mail message is sent to alert the IRM Staff of this problem so that they can attempt to "push" the message out of their facility by playing a script to IVM.  If there was an error in the transmission, the data is rebundled and retransmitted to the .  The same scheme for using either Full or Initial Transmission messages is employed as for regular nightly processing.

**Billing Transmission Processing**

All Means Test and Third Party Billing data which has resulted from an IVM verified Means Test or an IVM identified insurance policy is compiled and stored in the DHCP IVM database.  Any changes to these bills are then transmitted to the .  These transmissions are date/time stamped so that the last transmission date is known.  Billing activity will only be transmitted to the  when a change in the bill status, amount billed, or amount collected is identified.

IV.  Interactive Processing

This version of IVM contains three menus, each containing three options.

A.  IVM Upload Menu

This menu is used to upload demographic and insurance information which has been received from the .  This menu is locked with the IVM UPLOAD security key.  All of the upload options employ the List Manager and allow the sites to review a list of all veterans for whom data is to be uploaded prior to reviewing the data for a single veteran.

**Demographics Upload**

The Demographics Upload option will allow the DHCP user to review and then upload or reject demographic and eligibility data which has been transmitted to DHCP from the .  This information, compiled by IVM while verifying a Means Test, is sent back to the site if it is found to be different from what is on file at the .  IVM may send "uploadable" data which the site may wish to automatically upload into DHCP after review.  IVM may also send "non-uploadable" data for the purpose of review only (although sites may choose to use DHCP Registration options to load this data after review).  Eligibility (and some demographics) data must be sent as non-uploadable because IVM cannot send all of the required data elements required to process certain transactions in DHCP.

Following is a list of all demographic fields for the Patient file (#2) which may be transmitted to DHCP from the .

|   **Field #** | **DHCP Field Name**          | **Uploadable?**   |
|---------------|------------------------------|-------------------|
|        0.02   | SEX                          | YES               |
|        0.03   | DATE OF BIRTH                | YES               |
|        0.111  | STREET ADDRESS [LINE 1]      | YES               |
|        0.112  | STREET ADDRESS [LINE 2]      | YES               |
|        0.114  | CITY                         | YES               |
|        0.115  | STATE                        | YES               |
|        0.1112 | ZIP+4                        | YES               |
|        0.117  | COUNTY                       | YES               |
|        0.131  | PHONE NUMBER [RESIDENCE]     | YES               |
|        0.291  | DATE RULED INCOMPETENT (VA)  | NO                |
|        0.293  | RATED INCOMPETENT?           | NO                |
|        0.313  | CLAIM FOLDER NUMBER          | NO                |
|        0.314  | CLAIM FOLDER LOCATION        | NO                |
|        0.351  | DATE OF DEATH                | YES               |
|        0.361  | PRIMARY ELIGIBILITY CODE     | NO                |
|        0.381  | ELIGIBLE FOR MEDICAID?       | NO                |
|        0.382  | DATE MEDICAID LAST ASKED?    | NO                |
|        0.2911 | INSTITUTION (VA)             | NO                |
|        0.2912 | GUARDIAN (VA)                | NO                |
|        0.2913 | RELATIONSHIP (VA)            | NO                |
|        0.2914 | STREET ADDRESS [LINE 1] (VA) | NO                |
|        0.2915 | STREET ADDRESS [LINE 2] (VA) | NO                |
|        0.2916 | CITY (VA)                    | NO                |
|        0.2917 | STATE (VA)                   | NO                |
|        0.2918 | ZIP (VA)                     | NO                |
|        0.2919 | PHONE (VA)                   | NO                |
|        0.3611 | ELIGIBILITY STATUS           | NO                |
|        0.3612 | ELIGIBILITY STATUS DATE      | NO                |
|        0.3615 | ELIGIBILITY VERIF. METHOD    | NO                |

**Insurance Upload**

When the  contacts veterans' employers to verify income information, the employer is also asked to supply insurance information for policies to which the veteran subscribed through the employer.  This information is transferred back to DHCP in the Insurance Data Transmission message.

The Insurance Upload option is used to review the policy information identified by IVM and either upload or reject the policy.  Once the user either loads or rejects the policy, a confirmation message is immediately sent back to the  which identifies the decision that was made.

If the policy is rejected, the user will be asked for a reason for not uploading the policy.  Following is a list of the reasons for not uploading insurance information.

ALREADY HAVE INSURANCE POLICY

DATA APPEARS TO BE INCORRECT

INSURANCE COMPANY CLOSED

POLICY BENEFITS FULLY USED

POLICY COVERAGE EXPIRED

POLICY PLAN TYPE IS HMO

POLICY PLAN TYPE IS PPO

BENEFITS NOT AVAILABLE

COVERAGE FOR SPOUSE ONLY

The reason for not uploading the policy will be transmitted in the Insurance Confirmation Transmission to the .

If the policy is to be loaded, the user must select an insurance company (in file #36) which matches the carrier transmitted from the .  If the user wishes to add the IVM carrier as a new insurance company, the carrier will be added to file #36.  Once the carrier is selected, the user may commit to adding the policy to the database.  This action will also cause the confirmation message to be transmitted to the .  The Source of Information of the added policy will be set to IVM.  This field will flag the policy as having been identified by IVM, and will subsequently be used to send billing and collections information back to the  in the Billing/Collection Data Transmission.  Adding the new policy for the patient will also cause a mail message to be sent to MCCR personnel.  This message will list all of the patient's potentially billable episodes of care since the effective date of the policy.

**SSN Upload**

The SSN Upload option will allow the DHCP user to review and then upload or reject social security numbers that have been transmitted to DHCP from the .  The SSNs were received as "recommended SSNs" from SSA by the  after a match of DHCP data with SSA data failed to produce a match.  The SSNs are validated by the  and returned to DHCP for the veteran and spouse only.  Dependent SSNs are not submitted to SSA for matching purposes.

If the site has verified the SSN and wishes to automatically upload the SSN for either the veteran or spouse into the database, the veteran SSN will be filed in the PATIENT (#2) file and the Spouse SSN will be filed in the INCOME PERSON (#408.13) file.  Filing of either of these new SSNs will trigger either a Full or Initial Transmission for the veteran back to the .  IVM may then again attempt to match the veteran with SSA.

If the site does not wish to accept the SSN, the SSN may be rejected.  This action will remove the IVM recommended value from the IVM database where it is being temporarily stored.

B.  IVM Output Menu

This menu contains inquiries and reports which will assist the user in monitoring activity with the IVM program.

**Billing Transmission Report**

This option will generate a report of all IVM-related billing and collections activity which has been transmitted to the .  Information for each third party claim or Means Test charge is listed along with the date that the last transmission was sent to IVM.  The report will also indicate whether any further transmissions will be sent to IVM.

**IVM Case Inquiry**

This option allows the user to review the status of any Means Test which has been submitted to the  for verification.  The user will enter a patient name and income year, and then review the status of the case.  If the case has been closed, the closure reason, source, and date will be displayed.  All Means Test and Billing/Collection transmissions for the case will be displayed.  Additionally, the inquiry will indicate whether there is any uploadable data associated with the case which needs to be uploaded.

**Means Test Comparison Report**

This management report provides a summary of all Means Tests for two consecutive years for veterans who are Category A or C.  The report lists the total numbers of veterans in each Category, the number of veterans who have changed Means Test category over the two year period, the number of new Means Tests (veterans Means Tested in the second year only) and the number of "non-returns" (veterans Means Tested in the first year only).  A detailed report, which lists each veteran with both year's Means Test category, is also available.  This report may be run regularly to judge the shift of veterans from the mandatory to discretionary category, and to estimate the number of potential cases which will be referred for verification to the .

C.  IVM System Manager's Menu

This menu contains options that will assist the IRM specialist who supports IVM to monitor and configure system-related features within the package.  This menu is locked with the IVM SYS security key.

**IVM Parameter Enter/Edit**

There are only three parameters included with this package to be configured.  These parameters control whether notification messages will be sent to the IVM MESSAGES mail group when SSN, demographics, and insurance information is received from IVM.  The default action is to generate the messages.  This option may be used to inactivate the messages.

**Purge IVM Transmissions**

This option allows IRM to purge entries from the IVM TRANSMISSION LOG (#301.6) file which are associated with closed cases (entries in the IVM PATIENT [#301.5] file) from the previous Means Test year.

**IVM Transmission Report**

This report may be used to list the number of Initial and Full Data Transmissions which have been transmitted to IVM.  Summary statistics for the number of Category A and C veterans, and the number of veterans with and without active insurance, are also provided.

V.  PIMS and IB Enhancements

Substantial changes and enhancements to the DHCP Means Test module and the Integrated Billing package accompany IVM V. 2.0.

A.  PIMS Changes

The Means Test module has been designed on the premise that a veteran may only have on file one Means Test within a 365 day period.  However, in order to file the IVM verified Means Test and not lose the original Means Test conducted by the site, the software was reconfigured to accommodate 2 or more Means Tests for a veteran with the same date of test.  The following three fields were added to the ANNUAL MEANS TEST (#408.31) file to allow for this change.

#.23  Source of Income Test

#.24  Date Veteran Signed Test

#.25  DATE IVM VERIFIED MT COMPLETED

#.26  REFUSED TO SIGN

#2     Primary Income Test for Year?

The Source of Income Test field indicates whether the Means Test was conducted by the site or IVM.  The Date Veteran Signed Test field stores the date that the veteran signed the Means Test conducted by the  (the date that the patient signed the original Means Test remains in the Date/Time Completed [#.07] field).  The DATE IVM VERIFIED MT COMPLETED field contains the date returned from the  that the Means Test was verified and completed.  The REFUSED TO SIGN field returns an indicator from the  that the veteran refused to sign the Means Test.  The Primary Income Test for Year field indicates whether the Means Test is the active test for that date of test.  When an IVM Means Test is filed, the DHCP test is inactivated and the IVM test becomes the primary test.  The initialization of IVM V. 2.0 will flag all current Means Tests on file as the primary test.

Associated with each Source of Income Test is an indicator which is used to determine whether the test is editable.  IVM verified Means Tests are not editable, nor are tests which are not the primary test.  Inactivated DHCP Means Tests thus may not be edited, but they may be viewed and printed.

A patient may only have one test per calendar year from any given source.  Currently, the only sources allowed are VAMC and IVM, meaning the maximum number of Means Tests a patient can have for a calendar year is two.  Only one test per patient per year will be considered primary and will affect eligibility for care and patient billing.

When choosing a Means Test to act on (edit, view, delete, etc.), the source of the test and the primary indicator will be displayed to assist in picking the correct test.

B.  IB Changes

Several enhancements have been made to the Integrated Billing package to augment IVM V. 2.0.

Pharmacy copay exemption software was modified so that an IVM verified Means Test may potentially be used to update the veteran's copay exemption status.

When an IVM verified Means Test changes a veteran's Means Test category from A to C, IB will create all of the Means Test charges for the veteran's previous billable episodes of care.  These charges will be placed in a "hold" status in billing so that they may be reviewed before being passed to the Accounts Receivable module.  The new IB option, Release Charges 'Pending Review', will allow MCCR to review all charges which have been created and placed on hold, and either pass the charge to AR(Accounts Receivable) or cancel it.  When a charge is passed to AR, IB passes the billing information back to the IVM package so that it may be used for transmission to the .

Each night, when all billing activity is transmitted to IVM, a call is made to IB to compile all billing and collections activity related to IVM.  This information is then compared by the IVM package to billing data which has already been transmitted.  If there are changes in the bill which warrant the retransmission of the billing data, the record is queued for transmission and subsequently sent to the .

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IVM Version 4.2.5 Release Notes

## Introduction

The mission of the Income Verification (IV) Division of the Health Eligibility Center (HEC) is to collect and verify a Veteran’s income to determine medical care eligibility assignments.

This mission is accomplished through the verification process of the Veterans’ means tests conducted at VA healthcare facilities. Household income information of non-compensable 0% Service Connected (SC) and non-service-connected Veterans without special eligibility is matched with the person’s income records maintained by the Internal Revenue Service (IRS) and Social Security Administration (SSA). The IV staff verifies total household annual income and bases a Veteran’s eligibility or care on income from the previous year. When the total income exceeds an established means test threshold, the Veteran may be responsible for health care copayments.

The Income Verification Match (IVM) has undergone modification to their business process to assist in reaching a goal of processing all potential IVM cases available for each income year. To assist in these process changes, existing functionality of the IVM/EDB software was enhanced to further improve productivity and meet the needs of the business.

## Purpose

The purpose of this Release Notes document is to support the release of IVM 4.2.5. This document is intended to describe the functionality enhancements delivered with IVM 4.2.5 software.

## Audience

This document targets users and administrators of IVM 4.2.5 and applies to the changes made between this release and any previous release for this software.

## This Release

IVM will be upgraded from Version 4.2.4 to Version 4.2.5 and hosted at the Austin Information Technology Center (AITC). This upgrade will improve the user experience and the performance of IVM.

The following sections provide a summary of the enhancements and modifications to the existing software and any known issues for IVM 4.2.5.

### Enhancements and Modifications

Table 1 lists the enhancements and modifications included in the IVM 4.2.5 release. Enhancements and modifications are tracked in Rational Team Concert (RTC) Requirements Management (RM).

Table : Enhancements and Modifications in IVM 4.2.5

|   **RTC RM #** | **Title**                                                   | **Description**                                                                                                                                                           |
|----------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         948314 | IVM Sustainment work                                        | IVM Sustainment work                                                                                                                                                      |
|         948293 | The IVM/EDB system shall support Two Factor Authentication. | As the IVM/EDB product owner, the IVM/EDB application must require the Two Factor Authentication (2FA), so that the IVM/EDB application conforms to VA security policies. |

Table 2 lists the defects and fixes and corresponding RTC Change and Configuration Management (CM) numbers included in IVM 4.2.5.

Table : Defects and Fixes in IVM 4.2.5

|   **RTC CM #** | **Summary**                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         599291 | **Defect:**  Income not in initial letter and not included in gross income  **Fix:**  Made code changes to include income in the initial letter and in the gross income.                                                                        |
|         615370 | **Defect:**  Inactive users are able to login to IVM  **Fix:**  Made code changes to prevent inactive users to be able to login into the IVM application.                                                                                       |
|         615373 | **Defect:**  Unauthorized users “login” to main IVM screen  **Fix:**  Made code changes to prevent unauthorized users to be able to login into the IVM main screen.                                                                             |
|         615667 | **Defect:**  Unauthorized users able to access EnrollmentAdmin page  **Fix:**  Made code changes to prevent unauthorized users to be able to access the EnrollmentAdmin page.                                                                   |
|         618947 | **Defect:**  IVM application is not logging out users after period of inactivity (timeout)  **Fix:**  Updated code in files EnrollmentWeb\login.aspx.cs and EnrollmentWeb\Global.asax.cs to implement the user session timeout of 15 mins.      |
|         646239 | **Defect:**  EDB primary key values too large for Int32 data type in IVM  **Fix:**  Updated IVM Web application, EnrollmentAdmin, LetterCreator and IVM Bidirectional service code to support Int64 values as identifier across all IVM tables. |

### Known Issues

No defects remain open in this release.

## Product Documentation

The following documents apply to this release:

IVM 4.2.5 Release Notes are uploaded to the [VA Software Document Library](http://www.va.gov/vdl/) (VDL).

Additional reference documentation related to this release is stored in RTC.
