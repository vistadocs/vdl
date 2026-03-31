---
title: Radiology Version 5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer
audience: 
keywords: 
  - table
  - contents
  - fields
  - added
  - removed
  - order
  - status
  - imaging
  - supervisor
  - changed
page_count: 0
word_count: 1595
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

> ![](radiology-version-5-release-notes/001.png)

RADIOLOGY / NUCLEAR MEDICINE RELEASE NOTES

> Version 5.0

> April 1998

> Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer

> <span id="_bookmark0" class="anchor"></span>Release Notes

> PARENT/DESCENDENT EXAM AND PRINTSETS

> The major change with this release is the ability to enter a single report for a Parent/Descendent set of exams. An exam set or printset contains a Parent procedure and its Detailed or Series descendent procedures. Requesting a Parent will automatically cause each descendent to be presented for registration as separate cases under a single visit date and time. If the parent is defined to be a printset, the collection and printing of all common report related data between the descendants is seen as one entity. (E3R 7142 and 8021)

> This change affects case edits, reporting, displays, the HL7 and CPRS interfaces, labels/headers/footers, and output from VA FileMan Inquire and Print options. It is described in full in the ADPAC manual chapter on Parent/Descendent Exam and Printsets.

> NUCLEAR MEDICINE COMPONENT

> The other main change to this release is the addition of a Nuclear Medicine Component that manages data regarding the use of Radiopharmaceuticals. See New Options below for more information. To support this feature, changes have also been made to the options Examination Status Enter/Edit, Procedure Enter/Edit, Register Patient for Exams, Status Tracking of Exams, Case No. Exam Edit, Edit Exam by Patient, View Exam by Case No., Display a Rad/Nuc Med Report, Draft Report (Reprint), On-line Verifying of Reports, Report Entry/Edit, Resident On-line Pre-verification, Select Report to Print by Patient, Exam Profile (Selected Sort), and Profile of Rad/Nuc Med Exams.

> <span id="Changed_Options" class="anchor"></span>CHANGED OPTIONS

# Global Changes Affecting Many Options


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Global Changes Affecting Many Options](#global-changes-affecting-many-options)
- [IRM Menu \[RA SITEMANAGER\]](#irm-menu-ra-sitemanager)
- [Supervisor Menu \[RA SUPERVISOR\]](#supervisor-menu-ra-supervisor)
- [Exam Entry/Edit Menu \[RA EXAMEDIT\]](#exam-entryedit-menu-ra-examedit)
- [Films Reporting Menu \[RA RPT\]](#films-reporting-menu-ra-rpt)
- [Management Reports Menu \[RA MGTRPTS\]](#management-reports-menu-ra-mgtrpts)
- [Patient Profile Menu \[RA PROFILES\]](#patient-profile-menu-ra-profiles)
- [Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]](#radiologynuclear-med-order-entry-menu-ra-order)
- [IRM Menu \[RA SITEMANAGER\]](#irm-menu-ra-sitemanager-1)
- [Supervisor Menu \[RA SUPERVISOR\]](#supervisor-menu-ra-supervisor-1)
- [Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]](#radiologynuclear-med-order-entry-menu-ra-order-1)
- [Management Reports](#management-reports)
- [User Utility Menu \[RA USERUTL\]](#user-utility-menu-ra-userutl)
- [Rad/Nuc Med Patient file \#70 Fields Removed:](#radnuc-med-patient-file-70-fields-removed)
- [Fields Added:](#fields-added)
- [Nuc/Med Exam Data file \#70.2](#nucmed-exam-data-file-702)
- [Fields:](#fields)
- [Rad/Nuc Med Procedures file \# 71 Fields Removed:](#radnuc-med-procedures-file-71-fields-removed)
- [Fields Added:](#fields-added-1)
- [Major Rad/Nuc Med AMIS Codes file \#71.1 Fields Removed:](#major-radnuc-med-amis-codes-file-711-fields-removed)
- [Rad/Nuc Med Common Procedure file \#71.3 Fields Removed:](#radnuc-med-common-procedure-file-713-fields-removed)
- [Route of Administration file \#71.6](#route-of-administration-file-716)
- [Fields Added:](#fields-added-2)
- [Site of Administration file \#71.7](#site-of-administration-file-717)
- [Fields Added:](#fields-added-3)
- [Radiopharmaceutical Source file \#71.8](#radiopharmaceutical-source-file-718)
- [Fields Added:](#fields-added-4)
- [Radiopharmaceutical Lot file \#71.9](#radiopharmaceutical-lot-file-719)
- [Fields Added:](#fields-added-5)
- [Examination Status file \#72 Fields Added:](#examination-status-file-72-fields-added)
- [Rad/Nuc Med Reports file \#74 Field Name Changed:](#radnuc-med-reports-file-74-field-name-changed)
- [Fields Added:](#fields-added-6)
- [Field Changed:](#field-changed)
- [Report Distribution file \#74.4 Fields Removed:](#report-distribution-file-744-fields-removed)
- [Fields Added:](#fields-added-7)
- [Lbl/Hdr/Ftr Formats file \#78.2](#lblhdrftr-formats-file-782)
- [Diagnostic Codes file \#78.3 Fields Added:](#diagnostic-codes-file-783-fields-added)
- [Label Print Fields file \#78.7 Fields Added:](#label-print-fields-file-787-fields-added)
- [Rad/Nuc Med Division file \#79 Field Name Changed:](#radnuc-med-division-file-79-field-name-changed)
- [Fields Removed:](#fields-removed)
- [Fields Added:](#fields-added-8)
- [Imaging Locations file \#79.1 Fields Removed:](#imaging-locations-file-791-fields-removed)
- [Fields Added:](#fields-added-9)
- [Imaging Type file \#79.2 Fields Removed:](#imaging-type-file-792-fields-removed)
- [Fields Added:](#fields-added-10)
> All reports that can consume a significant amount of CPU/print time are now stoppable through the Stop Task action of the Taskman User \[XUTM USER\] option under the User's Toolbox \[XUSERTOOLS\] menu. The enhanced report logic checks for a stop flag during processing that is done before printing actually begins as well as during printing.
> All Imaging Location lookups will now display not only the imaging type of the location, but also the station number of the division to which it is assigned. If it is not assigned to a division, no station number will display. This was done to assist integration sites where users may not be familiar with the division of each Imaging Location.
> On all case lookup and patient profile screens that display a list of cases for a selected patient, a lowercase "i" will be displayed to the right of the case number if the site is running the V*IST*A Imaging package and if our interface with that package has filed image Ids on a "skeleton" radiology/nuclear medicine report record. The "i" is a visual indicator that images have been collected for that case.
> When an active, non-unique case number is entered at case number prompts, the system will now display a secondary selection list that includes the Long Case number for all active instances of that case number. For example, if a user enters case 100 at the Case No. prompt, and there are two active case 100s, a list will display both cases with additional information including long case number.
> Ordering and edit programs were changed to allow all but the special modifiers (portable, bilateral, operating room) for Series procedures in order to maintain the accuracy of AMIS reports. (E3R 8974)
> If a user accidentally enters blank lines at the end of word processing fields containing clinical history, report text, and impression text, the system will now delete the blank lines before storing the data, so that they won't be displayed on terminals and reports.
> The online help message for the one-many-all selector utility now includes the phrase, "Wildcard is case sensitive".
> <span id="_bookmark2" class="anchor"></span>Mammography was added as an additional Imaging Type.

# IRM Menu \[RA SITEMANAGER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Device Specifications for Imaging Locations \[RA DEVICE\] option now includes a prompt for DOSAGE TICKET PRINTER that will appear only if the Imaging Location's type of imaging is Nuclear Medicine or Cardiology Studies. There is also a new device specification, CANCELLED REQUEST PRINTER. The request cancellation logic was modified so that cancelled requests trigger the software to look for the Imaging Location to which the request was submitted, then print a cancellation notice on the CANCELLED REQUEST PRINTER for that location. If there is no Imaging Location associated with the request, nothing will print. If there is an Imaging Location associated with the request, but no CANCELLED REQUEST PRINTER entered for it, the system will make one last attempt to print if a CANCELLED REQUEST PRINTER is entered for the first location in the file; if none, nothing will print. If set up properly, the printing will happen regardless of whether the cancellation was done through the Rad/Nuc Med Cancel a Request option or OE/RR V. 2.5 or V. 3.0. (E3R 8255)

# Supervisor Menu \[RA SUPERVISOR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The option Unverify a Report \[RA UNVERIFY\] was changed to Unverify a Report for Amendment.

> The prompt "Select RAD/NUC MED Reports DAY/CASE#" was changed to "Select RAD/NUC MED REPORTS DAY-CASE#" to aid the user in remembering to use a dash instead of a slash when responding. (E3R 8761)

> Patch RA\*4.5\*2 enhanced the option by providing for the retention of reports for historical/legal purposes at the time they are Unverified. The uncorrected report and the date unverified is saved in a new subfile in the Error Reports field \#1000 of the Rad/Nuc Med Report file \#74. This subfile supports multiple occurrences of un-verification of the same report. All fields related to the report are rolled into a word processing field in the subfile: report text, impression, clinical history, diagnostic codes, primary and secondary interpreting staff and residents, verifier name/date/esig, pre-verifier name/date/esig, and un-verifier. The report purge logic was modified so that no report data for amended reports will ever be purged. The Rad/Nuc Med Report Unverified bulletin now includes primary staff and primary resident

> (E3R 7901). The new option Access Uncorrected Reports \[RA UNCORRECTED REPORTS\] can be used to view the retained records.

> The Delete Printed Batches By Date \[RA BTCHDEL DATE\] option now allows deletion of batches that have not yet been printed.

> System Definition Menu \[RA SYSDEF\] Division Parameter Set-up \[RA SYSDIV\]

1.  The prompt ALLOW 'RELEASED/UNVERIFIED' is now a Location

> parameter and can be found under the option Location Parameter Set- up. (E3R 7742)

> The prompt WARNING ON UNVERIFIED REPORTS was changed to WARNING ON RPTS NOT YET VERIF. If this field is set to YES results reports in any status except Verified will print the status surrounded by asterisks under the body of the report. If this field is set to NO or left unanswered, the status box will not print on reports not yet verified. This can be used to make sure that hard copies of unverified results reports are not accidentally placed in patient charts or interpreted as the final results.

2.  AUTO E-MAIL TO REQ. PHYS is a new prompt. Entering YES will turn on a feature that automatically sends the Radiology/Nuclear Medicine findings report to the Requesting Physician via e-mail at the time it is verified.

> Print Division Parameter List \[RA SYSDIVLIST\]

> All changes to Division Parameter Set-up are reflected in this listing. Also the Resource Device for the Division is displayed. Resource Device is a new field and is entered/edited via the IRM Menu \[RA SITEMANAGER\], Resource Device Specifications for Division \[RA RESOURCE DEVICE\] option.

> List of Cameras/Equip/Rms \[RA SYSEXLIST\]

> Unassigned cameras, equipment, or rooms will appear at the end of the listing.

> Location Parameter Set-up \[RA SYSLOC\]

1.  The prompt ALLOW 'RELEASED/UNVERIFIED' that used to be a Division parameter is now a Location parameter. (E3R 7742)
2.  There is a new field, STAT REQUEST ALERT RECIPIENTS. Recipients must have a Radiology/Nuclear Medicine personnel classification. They will receive an alert whenever a STAT request is submitted to the Imaging Location. (E3R 6880) Prerequisite for this feature are CPRS (OE/RR V. 3.0) and your site must have the "Ask Imaging Location" Division parameter turned on.
3.  A new field, URGENT REQUEST ALERTS, will determine if alerts will be sent to the Imaging Personnel defined in the Stat Request Alert Recipients field. If this field is set to YES, then all the users in the Stat Request Alert Recipients field will be sent an alert for urgent requests. (E3R 6880) Prerequisite for this feature is the same as \#2 above.
4.  A new field, VOICE DICTATION AUTO-PRINT, if set to YES and voice dictation is used to enter a report, will automatically print a copy of the report on the device defined in the field Report Printer Name.
5.  The new fields, CREDIT METHOD and DSS ID are used in connection with crediting the exam. These were added with patch RA\*4.5\*4.
6.  The field, PRINCIPAL CLINIC was removed from this option.
7.  The description has been changed for the PRINT DX CODES IN REPORT field. It clarifies the printing of primary and secondary diagnostic codes in the body of reports and headers and footers.
8.  REPORT RIGHT MARGIN was changed so that the entry in this field indicates the absolute column at which the text for Clinical History, Report and Impression should end when printing.

> Location Parameter List \[RA SYSLOCLIST\]

> This option now permits eliminating Inactive locations and you may select all, many, or a few locations for printing. The Principal Clinic, Input Devices at this Location, and User Code Entry Required were removed and the following data added to the Location Parameter List:

> Inactivation Date Credit Method DSS ID

> Allow 'Released/Unverified'

> Cancelation Ptr under Order Parameters

> April 1998 Radiology/Nuclear Medicine V. 5.0 5

> Health Summary under Reporting Parameters Radiopharmaceutical Dosage Ticket Parameters 'Stat' Alert Recipients For This Location

> Urgent Request Alerts?

> The flash card printing mechanism will now honor the Division/Location parameters specifying that a selected number of flash cards will print per visit. (NOIS FTL-0496-50985)

> Utility Files Maintenance Menu \[RA MAINTENANCE\] Diagnostic Code Enter/Edit \[RA DIAGEDIT\]

> INACTIVE was added as a new field so diagnostic codes could be

> inactivated (removed from selection lists). (E3R 8906) Examination Status Entry/Edit \[RA EXAMSTATUS\]

1.  The prompt "Default next status for exam" no longer allows statuses without order numbers. The Inconsistency report that runs after the Examination Status Entry/Edit will print a warning if any status record has a default next status without an order number. The Status Tracking of Exams no longer allows an exam to go to a status without an order number. During Status Tracking, if the default next status of the current status is detected to have no order number, the system will find the next higher status with an order number and present that as the next status to progress to.
2.  The wording on many of the prompts was changed to provide a clearer description of what is being asked of the user.
3.  New fields for all Imaging Types:

> GENERATE EXAMINED HL7 MESSAGE allows an HL7

> message to be sent when a patient has been examined.

> ASK MEDICATIONS & DOSAGES will ask the user to enter medications and dosages given for the exam.

> ASK MEDICATION ADMIN DT/TIME & PERSON will ask the

> user to enter the medication administration date/time and person who gave the dose.

4.  The following are new fields for Imaging Types that use Radiopharmaceuticals (Cardiology Studies and Nuclear Medicine). They fall into two types, those that require data to move the case to the status being defined and those that ask for data when the case is moving to the status being defined.

> <u>Required for the status being defined</u>

> RADIOPHARMS & DOSAGES REQUIRED ACTIVITY DRAWN REQUIRED (RADIOPHARM)

> DRAWN DT/TIME AND PERSON REQUIRED (RADIOPHARM) ADMIN DT/TIME/PERSON REQUIRED (RADIOPHARM) ROUTE/SITE REQUIRED (RADIOPHARM ADMINISTERED) LOT NO. REQUIRED (RADIOPHARM)

> VOLUME/FORM REQUIRED (RADIOPHARM)

> <u>Asked while attempting to progress to the status being</u> <u>defined</u>

> ASK RADIOPHARMACEUTICALS & DOSAGES

> ASK ACTIVITY DRAWN (RADIOPHARMACEUTICAL)

> ASK DRAWN DT/TIME & PERSON (RADIOPHARMACEUTICAL) ASK ADMIN DT/TIME & PERSON (RADIOPHARMACEUTICAL) ASK ROUTE/SITE OF ADMIN (RADIOPHARM)

> ASK LOT NO. (RADIOPHARM)

> ASK VOLUME/FORM (RADIOPHARM)

5.  PRINT DOSAGE TICKET WHEN EXAM REACHES THIS STATUS is also asked for only Imaging Types that use radiopharmaceuticals.

> Flash Card/Label Formatter \[RA FLASHFORM\]

> The name of the option was changed to Label/Header/Footer Formatter.

> The following Label Print Fields were added: Resident Signature Name

> Staff Signature Name Verifying Signature Name Verifying Signature Title Long Case Number Barcode Patient Address Line 1 Patient Address Line 2 Patient Address Line 3

> Common Procedure Enter/Edit \[RA COMMON PROCEDURE\] and Display Common Procedure List \[RA DISPLAY COMMON PROCEDURES\] in the Order Entry Procedure Display menu begin by allowing the selection of Imaging Types.

> Procedure Enter/Edit \[RA PROCEDURE\] has a number of new fields:

> SINGLE REPORT appears when a Parent procedure is being edited. It combines the reporting of the common data of the procedure's descendants (report text, impression, verifier, pre-verifier, staff (primary and secondary), residents (primary and secondary), diagnoses, and all other report-related fields) into one report.

> PROMPT FOR MEDS only appears for procedures that are Detailed or Series. If this field is set to YES, case edits will prompt for medications administered for this procedure and Status Tracking will ask for meds if the Ask Medications and Dosages parameter is set to YES for the next status.

> DEFAULT MEDICATION only appears for procedures that are Detailed or Series. This field is used to enter any medications which are usually used for the procedure.

> DEFAULT MED DOSE only appears if a Default Medication is entered. If a default dose is entered, it will be the default response for med dose on the patient's exam record when the case is edited.

> SUPPRESS RADIOPHARM PROMPT only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (nuclear medicine or cardiology studies). If the exam status setup for the affected Imaging Types specifies that radiopharmaceutical data should be asked and/or required to progress to various statuses, this field can be used to over-ride that requirement.

> PROMPT FOR RADIOPHARM RX only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (nuclear medicine or cardiology studies). It controls whether case edit and status tracking options prompt for prescribing physician and prescribed radiopharmaceutical dose. If this field is set to YES, prescriber prompts will appear for any radiopharmaceuticals entered for this procedure. If this field is left blank, prescriber prompts will not appear. If this field is set to YES, Status Tracking will prompt

> during each edit session until the data is entered; case edits will always prompt, even if prescriber data has already been entered.

> DEFAULT RADIOPHARMACEUTICAL only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (nuclear medicine or cardiology studies). It will be automatically entered as a radiopharmaceutical on patients' nuclear medicine exam records during registration. If a Default Radiopharmaceutical is defined for a procedure, then the following fields appear for editing:

> LOW ADULT DOSE HIGH ADULT DOSE USUAL DOSE

> DFLT ROUTE OF ADMINISTRATION DEFAULT FORM

> EDUCATIONAL DESCRIPTION is used to describe the procedure and give information about its purpose in confirming or eliminating various diagnoses. It may be used for educational purposes by clinicians who are trying to familiarize themselves with imaging procedures that are available. If an educational description is entered, the system asks if the user wants to DISPLAY EDUCATIONAL DESCRIPTION WHEN

> ORDERED. Entering YES at that field displays the description along with any Procedure Message during the ordering process. The Educational Description is included on the Active Procedure List. (E3R 6112)

> Also, if a procedure is changed from a Detailed or Series procedure to a Parent during Procedure Enter/Edit, the system will automatically delete the CPT on that procedure.

> Reason Edit \[RA REASON EDIT\]

> NATURE OF ORDER ACTIVITY determines actions that OE/RR will take when it is notified that an order was held or canceled by the imaging service. This prompt will not appear until CPRS (OE/RR V. 3.0) is installed.

> Reports Distribution Edit \[RA DISTEDIT\]

> There are two new features for sending reports to the requesting physician:

> <span id="_bookmark3" class="anchor"></span>A new queue, Requesting Physician, was added to this option that will give results reports sorted by requesting physician. As with the other queues, reports are automatically placed in the queue at the time they are verified. (E3R 5154)

> This is not related to the new Division parameter, AUTO E- MAIL TO REQ. PHYS, which controls whether an e-mail message containing the results report will be automatically generated and sent to the requesting physician.

> Maintenance Files Print Menu \[RA MAINTENANCEP\]

> These print options reflect changes made in the Utility Files Maintenance Menu options.

> Flash Card/Label List \[RA FLASHFORMP\] was renamed Label/Header/Footer Format List.

> All Procedure File Listings \[RA PROCLISTS\] begin by allowing the user to select an Imaging Type.

> Active Procedure List (Long) \[RA PROCLONG\], Series of Procedures List \[RA PROCSERIES\], and Inactive Procedure List (Long) \[RA INACPRCLONG\] now include the name of the Health Summary type to be printed with requests.

# Exam Entry/Edit Menu \[RA EXAMEDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Register Patient for Exams \[RA REG\] now allows the user to register a parent procedure set for a detailed procedure order. At the time of registration, at the "Select a request" prompt, the software will allow replacement of a single selected Detailed, Series, or Broad procedure request with a parent-printset procedure by doing the following:

1.  Enter "Pn" at the prompt, where "P" indicates that you want to trigger the parent-printset registration feature and "n" is the request number. The request must NOT be a parent. Only one "n" value is allowed. You will then see a prompt for a parent procedure.
2.  Enter a parent procedure of the same imaging type as the requested procedure. The parent must be predefined as a printset.

> 10 Radiology/Nuclear Medicine V. 5.0 April 1998

3.  Then proceed to register the predefined descendant(s) OR, discard (^) its descendant(s) and register any descendants you choose when it asks you for more procedures to add on.

> The list of requests displayed will have a "+" in front of procedures that are printset parents. (A "+" will not display in front of non-printset parents.) After the replacement printset parent is registered, all outstanding orders that have matching procedures to any just registered will be displayed as a reminder that these may be duplicates and might have to be cancelled.

> Diagnostic Code Entry by Case No. \[RA DIAGCN\] was renamed to Diagnostic Code and Interpreter Edit by Case No.

> View Exam by Case No. now includes a secondary screen that displays all additional personnel involved in the case (the main screen will only display one technologist even if there are several). The secondary screen displays requesting physician, primary and secondary staff and residents, transcriptionist, pre-verifier, verifier, and technologists if these fields contain data. (E3R 5885)

> The Indicate No Purging of an Exam/Report \[RA NOPURGE\] option will now prompt for and store reason(s) for not purging.

> The warning message that appears during registration, Register Patient for Exams \[RA REG\], when a procedure is rejected by the user has been changed to include the possibility of contrast media as the rejection reason. (E3R 4110)

> The new message states:

> Only active procedures allowed, imaging type of exam should be same as procedure, contrast media use must be OK'd if previous adverse reaction on record.

> The Status Tracking edit functionality was changed (E3R 9509):

> It informs the user if the exam meets criteria for a higher status than the status reached after editing.

> If the "default next status" is invalid (i.e., no order number on the status) the Status Tracking functionality will detect this and search for the next valid status to use instead.

> Status Tracking will now cycle to screens with inactive statuses (i.e., no order number on the status) if the status' "Appears on Status Tracking?" field is set to YES. Previously, there was no way, through case edit options, to get prompts for fields necessary to process cases in an inactive status to complete.

# Films Reporting Menu \[RA RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Primary and Secondary Staff and Resident fields will now screen out interpreting physicians who do not have access to at least one Imaging Location of the imaging type that matches the exam. (E3R 8467)

> Remove/Add Report From Batch \[RA BTCHREMOVE\] in the Batch Reports Menu \[RA BTCH\] was changed to Add/Remove Report From Batch.

> Display a Report \[RA RPTDISP\] was changed to Display a Rad/Nuc Med Report.

> Select Report to Print by Patient \[RA RPTPAT\] now allows selection of multiple reports rather than just one at a time. (E3R 6732)

> During On-line Verification, if two concurrent users choose categories that include the same report, then user A changes the status of the report making it inconsistent with the report category chosen by User B, user B will now see a message notifying him of the change. The message displayed will be one of the following:

> Since the time you selected this group of reports, another user has deleted this report for RADPATIENT,ONE case \#256.

> Since the time you selected this group of reports, another user has changed this report's status to XXXXX.

> Since the time you selected this group of reports, DR. SMITH has verified the report for RADPATIENT,ONE case \#289.

> On-Line Verifying of Reports \[RA RPTONLINEVERIFY\] and Resident On-Line Pre- Verification \[RA RESIDENT PRE-VERIFY\] were modified to include transcriptionist and secondary staff and residents in the header. Patch RA\*4.5\*2 also changed the default printer of HOME to display the sign-on Imaging Location report printer if one has been entered by IRM. (E3R 7957) Rad/Nuc Med Residents and Staff will now see a message when they log on telling them how many imaging cases are awaiting their pre-verification and verification respectively (E3R 6619).

> The option On-Line Verifying of Reports now returns to the list of report categories left to verify (if any exist for the user whose reports were verified) after choosing a category and verifying the reports. (E3R 8905) A new category, \*STAT\*, was added. A report associated with a STAT order will only be counted under the STAT category if the order for the exam still exists on the system. The procedure name is now included in the message displayed when a user changes the status of a report in another user's verify queue. (E3R 9003)

> <span id="_bookmark5" class="anchor"></span>Report Entry/Edit \[RA RPTENTRY\] now warns the user that the standard report will completely overwrite the existing report when a standard report is selected and the impression and/or report text already exists. In this case, the option gives the user a chance to cancel their standard selection. Also, the default response to the "Do you want to print batch now?" prompt was changed from YES to NO. (E3R 8833)

> The Report Entry/Edit \[RA RPTENTRY\] option will now detect, at the beginning, if the sign-on user has an electronic signature (e-sig), Staff or Resident Rad/Nuc Med Classification, and the RA VERIFY key. If these requirements are met, the user will be prompted for his or her e-sig, and reports verified while using this option will contain the verifier's e-sig.

> The options that allow changing report status to Verified will now capture the user who is signed on and changing the status. This will be reflected in the report printout. If the verifying physician is the same person as the sign-on user who moved the status to Verified, but this was not done via the On-Line Verifying of Reports \[RA RPTONLINEVERIFY\] option or the Report Entry/Edit \[RA RPTENTRY\] option, wording next to the verifier's name will read "(Verifier, no e- sig)". If a transcriptionist or resident (i.e., someone other than the name entered as the Verifying Physician) verified the report, the wording will state "Verified by transcriptionist for Dr. xxx". If an electronic signature is affixed to the report (i.e., it was verified via on-line verification) the wording will be "(Verifier)". (E3R 8270)

> The On-Line Verifying of Reports option now displays different prompts at the end of a report page versus the end of an entire report display. The prompt at the end of a report display has been changed to:

> ("nn" left to review) type '?' for action list, 'Enter' to continue//

> This change was designed to give users a visual cue that the end of report display is the time to select an action (especially Status and Print if they want the report to print after assigning a status). (E3R 8835)

> Clinic Distribution List \[RA RPTDISTLISTCLINIC\] and Ward Distribution List \[RA RPTDISTLISTWARD\] in the Distribution Queue Menu \[RA RPTDIST\] now allow one-many-all and wildcard selection of clinics/wards.

> Report pre-verification date/time and user was added to the Report Activity Log. It is populated via the Resident Pre-verify option.

# Management Reports Menu \[RA MGTRPTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unverified Reports \[RA DAIUVR\] within Daily Management Reports \[RA DAILYRPTS\] can now be generated in either a Brief or Detailed version or by Exam Date, Itemized List or Staff, Itemized List. They can be sorted by Division, Imaging Type and Exam Date range. The first two include a default breakout of 24, 48, 96, and \>96 hours for the age of the reports or the user can select hour cutoffs. Report aging totals are displayed by category (staff, resident) and individual physician.

> The detailed version includes extra report and exam data to help in tracking down reports: transcription date, patient ID, report status, pre-verification date exam date/time, desired date entered by the ordering clinician, procedure, and other attending and resident radiologists entered as primary/secondary interpreting physicians. In addition, the report now has Division summaries. The Division summary is suppressed to prevent redundancy if only one Imaging Type prints for the Division. (E3R 7220) The Exam Date, Itemized List and Staff, Itemized List provide the same output format with one line per report. The report by exam date is sorted by division, exam date/time, patient, and case. It is useful for case turn- around and completion since the oldest cases appear first. The staff list is sorted by staff, exam date/time, patient, and case. If a report exists, but no staff is entered, it will appear as staff UNKNOWN. Separate pages print for each staff member, so it can be handed out to the staff for their review and follow-up.

> Abnormal Exam Report \[RA ABNORMAL\] within Daily Management Reports now prompts for a selection of one-many-all Diagnostic codes to be included on the report. (E3R 9184)

> Daily Log Report \[RA LOG\] within Daily Management Reports now prompts for Imaging Locations to be included on the report. Each Imaging Location prints separately within Imaging Type. The report header includes the location. (E3R 9025)

> The name of the Interpreting Physician now appears on the Delinquent Status Report \[RA DELINQUENT\] and Incomplete Exam Report \[RA INCOMPLETE\] within the Daily Management Reports menu. If both the Primary Interpreting Staff and Resident are entered, the report will show Staff. If only Resident is entered, it will show the Resident. If neither are entered, no name will be printed on the report. The name of one technologist (the first entered) also appears. (E3R 8539) Also, Outpatient and Inpatient were added as subheadings to the reports.

> Within Division and Imaging Type, first the inpatient data is printed then the outpatient data. (E3R 9563)

> The Staff and Resident Reports \[RA WKLSTAFF and RA WKLRES\] under Personnel Workload Reports \[RA WKL\] now prompt for inclusion/exclusion of secondary staff and resident. These reports can now be generated for Primary Staff or Primary Residents only, or primary and secondary.

> <span id="_bookmark6" class="anchor"></span>The Staff, Physician, Resident and Technologist reports within Personnel Workload Reports menu now display the CPT code for each procedure. (E3R 9613)

> The Procedure/CPT Statistics Report \[RA CPTSTATS\] in the Special Reports menu now prompts for inclusion/exclusion of cancelled cases. The header now has an added notation telling whether cancelled cases were included or excluded. (E3R 8846) The report also has additional columns displaying the percentage of total cases and cost per procedure. Number of procedures done and cost are totaled for each imaging type. (beta test enhancement)

# Patient Profile Menu \[RA PROFILES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> and

# Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Request displays and request reprints now show the Clinical History (E3R 7694) and procedure(s) registered (if it has been registered). Detailed exam profiles show the procedure requested (unless the request has been purged from the system). If a Parent procedure is requested, the request form will show all procedures registered. The request form will no longer print the exam status of the first exam it finds in the set; only the request status (usually Active) will print. This change affects Detailed Request Display \[RA ORDERDISPLAY\], Exam Profile (selected sort) \[RA PROFSORT\], and Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]. (E3R 8458)

> When a cancelled request is printed, the name of the person who cancelled the request and the cancel transaction date/time are now included on the printout.

> The Procedure selection prompt that appears when using Request an Exam \[RA ORDEREXAM\] was changed to let users know that they can get online help by entering a "?". The online help was changed to tell users that they can see a list of all selectable procedures by entering "??". (E3R 9611)

> The default response of "NO" to the pregnancy question during order entry has been removed, so that users are forced to enter an answer if the woman is of child bearing age. If the patient is under 12 or over 50 years of age, the default response remains "NO". (E3R 6911)

> If CPRS (OE/RR V. 3.0) is installed, an alert may be sent to predefined Imaging personnel when a STAT or URGENT request is entered. A prerequisite is that the Division parameter "Ask Imaging Location" that triggers the "Submit Request To" prompt must be turned on.

> <span id="New_Options" class="anchor"></span>NEW OPTIONS

# IRM Menu \[RA SITEMANAGER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Resource Device Specifications for Division \[RA RESOURCE DEVICE\]

> This is a new option under the IRM Menu. The device controls the rate at which tasked exam status updates are released to be processed. This is advised if the facility is experiencing drastic system slowdowns due to periodic heavy use of the online report verification and batch verification of reports options, which can queue a large number of tasks at once.

# Supervisor Menu \[RA SUPERVISOR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access Uncorrected Reports \[RA UNCORRECTED REPORTS\] was added to the Supervisor Menu that displays or prints uncorrected reports. See Unverify a Report for Amendment \[RA UNVERIFY\] above for more detail.

> Nuclear Medicine Setup Menu \[RA NM EDIT MENU\] contains four menu options to build and manage the Nuclear Medicine radiopharmaceutical lot numbers, routes and sites of administration, and vendor source.

> Lot (Radiopharmaceutical) Number Enter/Edit \[RA NM EDIT LOT\] allows the entry and edit of lot numbers in the Radiopharmaceutical Lot file \#71.9.

> Route of Administration Enter/Edit \[RA NM EDIT ROUTE\] allows the entry and edit of routes in the Route of Administration file \#71.6.

> Site of Administration Enter/Edit \[RA NM EDIT SITE\] allows the entry and edit of sites in the Site of Administration file \#71.7.

> Vendor/Source (Radiopharmaceutical) Enter/Edit \[RA NM EDIT SOURCE\] allows the entry and edit of vendors and sources in the Radiopharmaceutical Source file \#71.8.

> Nuclear Medicine List Menu \[RA NM PRINT MENU\] compliments the Nuclear Medicine Setup Menu by printing the contents of the four files using the following new options.

> Lot (Radiopharmaceutical) Number List \[RA NM PRINT LOT\]

> <span id="_bookmark8" class="anchor"></span>Route of Administration List \[RA NM PRINT ROUTE\] Site of Administration List \[RA NM PRINT SITE\]

> Vendor/Source (Radiopharmaceutical) List \[RA NM PRINT SOURCE\]

> Procedure Edit Menu \[RA PROCEDURE EDIT MENU\] is a new menu under Utility Files Maintenance Menu \[RA MAINTENANCE\]. It contains the options Procedure Enter/Edit, Procedure Message Entry/Edit, Procedure Modifier Entry, and a new option Cost of Procedure Enter/Edit \[RA PROCOSTEDIT\].

> Cost of Procedure Enter/Edit supports the entry of a cost for each procedure. The Unit cost and Total cost appear on the Procedure/CPT Statistics Report \[RA CPTSTATS\].

> Barcoded Procedure List \[RA BARPROCPRINT\] found under the Maintenance Files Print Menu, Procedure File Listings produces a list of barcoded procedures with or without barcoded CPTs. The list is selectable by Imaging Type. (E3R 6125)

> Parent Procedure List \[RA PARENT PROCEDURE LIST\] found under the Maintenance Files Print Menu, Procedure File Listings produces a list of parent procedures, selectable by Imaging Type and Active and/or Inactive. It can be printed in 80-column format. The list includes only parent type procedures and all fields applicable to parent procedures that are included on the Active Procedure Long listing. It shows whether they are printsets (i.e., Single Report = Yes), whether a health summary is associated with it for printing with the request, whether Radiology/Nuclear Medicine approval is required to order it, its imaging type, all descendants and their CPT codes, and the educational description.

# Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rad/Nuc Med Procedure Information Look-Up \[RA DISPLAY IMAGPROCINFO\] allows the user to select active procedures by Imaging Type (only Imaging Types already assigned to at least one procedure are allowed). The user can select one, many or all procedures of the chosen Imaging type(s) and direct the output to the screen or any available output device. The option will provide the procedure, type of procedure, imaging type abbreviation and the CPT code of the procedure. The CPT code for Parent procedures will state "See Descendants". If any Educational Description exists, it will also be shown. (E3R 6112)

# Management Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Two new management reports are now available for Nuclear Medicine. The Radiopharmaceutical Usage Report \[RA NM RADIOPHARM USAGE\] can be found under the Daily Reports menu. The Radiopharmaceutical Administration

> Report \[RA NM RADIOPHARM ADMIN\] can be found under the Personnel Workload Reports menu. The reports show the case number, patient, radiopharmaceutical, activity drawn and administered, radiopharmaceutical low/high ranges, procedure and the person who administered the dose.

# User Utility Menu \[RA USERUTL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Duplicate Dosage Ticket \[RA DOSAGE TICKET\] allows the user to print additional dosage tickets for those exams which are associated with radiopharmaceuticals.

> OUTPATIENT WORKLOAD CREDITING

> Since the release of patch RA\*4.5\*4, outpatient workload crediting is handled differently. For more complete information, see the ADPAC Guide, Outpatient Workload Crediting chapter.

> INTERFACES

> Patch RA\*4.5\*2 made the following changes to the interface with the V*IST*A

> Imaging package.

> Imaging/Multi-Media Interface Changes

> The program that enters a skeleton report to store image pointers will no longer populate the Impression field. It will store a single line in the report text field if images have been collected.

> Images captured for this report.

> A new transaction type, Images Collected, was added to the Type of Action field \#2, of the Activity Log field \#100, of the Rad/Nuc Med Reports file \#74. This will be recorded in the log if the imaging package stores an image ID on the report.

> The status of a newly created skeleton report will remain blank instead of changing to DRAFT. This was done to prevent report selection displays from showing a misleading draft status for cases whose image pointers have been recorded in a skeleton report with no other report data entered.

> The subroutine that performs a test to determine if the Imaging package is installed before proceeding to call the Imaging side of the interface was moved to a new routine by itself to reduce the sites' downtime impact when installing future patches to the rest of the Rad/Nuc Med side of the interface.

> Voice Recognition Interface Changes

> When a voice recognition system was used to overwrite an existing Draft or Problem Draft report in which Secondary diagnostic code(s) existed, the program did not delete the existing diagnostic code(s). The voice recognition system interface is only capable of entering a single diagnostic code(s) which is entered as the primary diagnosis. In keeping with the philosophy that the interpreting physician on the voice recognition system believes that what he is entering is the total report, the secondary diagnostic code(s) are now deleted if the voice recognition system report replaces the existing report.

> HL7 Messaging

> The HL7 Messaging for Imaging and PACS subscribers was enhanced to use V*IST*A HL6 V. 1.6 features. A new message is triggered at the point where a patient's images have been collected (i.e., patient examined). In the Examination Status setup, a new field Generate Examined HL7 Message was added so that ADPACs can flag the status where this message should be triggered. As soon as an exam has reached the selected status, the HL7 message will be sent. Once the message has been sent, another new field, HL7 Examined message Sent?, on the Rad/Nuc Med Patient file \#70 exam subfile will be set to YES to act as a log of the message event. The software checks this log at every status change. If the new status is equal or greater to the flagged status the message will be sent, if and only if the log field is blank.

> Reports

> Routines in the RAHLO\* namespace that process transmitted reports have been rewritten to open the door to accept report data from potentially any source within or outside of V*IST*A, with or without the use of HL7 messages.

> <span id="Bulletins" class="anchor"></span>BULLETINS

> Primary Interpreting Staff and Primary Interpreting Resident data were added to the Rad/Nuc Med Report Unverified bulletin. (E3R 7901)

> FILE CHANGES

# Rad/Nuc Med Patient file \#70 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Transfer Comment \#150

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Dosage Ticket Printed \#29 Reason for not Purging \#46 Medications \#200

> Med Administered Med Dose

> Date/Time Med Administered Person who Administered Med

# Nuc/Med Exam Data file \#70.2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new file that contains information specific to nuclear medicine studies in which radiopharmaceuticals are used.

# Fields:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient \#.01

> Exam Date/Time \#2

> Case Number \#3

> Radiopharmaceuticals \#100 Radiopharmaceutical

> Prescribed Dose by MD Override Prescribing Physician

> Activity Drawn (in mCi) Date/Time Drawn

> Person Who Measured Dose Dose Administered

> Date/Time Dose Administered Person Who Administered Dose Witness to Dose Administration Route of Administration

> Site of Administration Site of Admin Text Lot No.

> Volume (in ml or caplets) Form

# Rad/Nuc Med Procedures file \# 71 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Stop Codes \#160

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Suppress Radiopharm Prompt \#2 Prompt for Meds \#5

> Cost of Procedure \#10

> Default Camera/Equip/Rm \#14 Print Procedure Barcode \#15 Print CPT Barcode \#16

> Display Ed Desc when Ordered \#17 Single Report \#18

> Prompt for Radiopharm RX \#19 Default Radiopharmaceuticals \#50

> Default Radiopharmaceutical Usual Dose

> Dflt Route of Administration Default Site of Administration High Adult Dose

> Low Adult Dose Default Form

> Default Medications Default Medication Default Med Dose

> New Procedure Message \#400 Educational Description \#500

# Major Rad/Nuc Med AMIS Codes file \#71.1 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Credit Clinic Stop \#3

# Rad/Nuc Med Common Procedure file \#71.3 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Common Procedure Group \#2

# Route of Administration file \#71.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new file for routes of administration for radiopharmaceuticals.

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Name \#.01

> Valid Sites of Administration \#2 Prompt for Free Text Site? \#3 Synonyms \#100

# Site of Administration file \#71.7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new file for sites of administration for radiopharmaceuticals.

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Name \#.01

> Synonym \#100

# Radiopharmaceutical Source file \#71.8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new file for sources for radiopharmaceuticals.

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vendor/Pharmacy \#.01

# Radiopharmaceutical Lot file \#71.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a new file for lot numbers for radiopharmaceuticals.

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Number/ID \#.01

> Source \#2

> Expiration Date \#3

> Kit \# \#4

> Radiopharm \#5

> Inactive \#6

# Examination Status file \#72 Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ask Medications & Dosages? \#.27 Ask Med Adm Dt/Time/Person? \#.28 Radiopharms/Dosages Required? \#.51 Activity Drawn Required? \#.53

> Drawn Dt/Time/Person Required? \#.54

> 22 Radiology/Nuclear Medicine V. 5.0 April 1998

> Adm Dt/Time/Person Required? \#.55 Route/Site Required? \#.57

> Lot No. required? \#.58 Volume/Form Required? \#.59

> Ask Radiopharms and Dosages? \#.61 Print Dosage Ticket? \#.611

> Ask Activity Drawn? \#.63

> Ask Drawn Dt/Time/Person? \#.64 Ask Adm Dt/Time/Person? \#.65 Ask Route/Site of Adm? \#.67

> Ask Lot No.? \#.68

> Ask Volume/Form? \#.69

# Rad/Nuc Med Reports file \#74 Field Name Changed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pre-Verification Elect Sign is now Pre-Verification E-Sig

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Other Case \# \#4.5

> Status Changed to Verified By \#17

# Field Changed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> P:PRE-VERIFIED was added as a new code to the Type of Action subfile of the Activity Log field \#100.

# Report Distribution file \#74.4 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hospital Division \#5

> Imaging Location \#7

> Patient \#9

> SSN \#10

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requesting Physician \#12

# Lbl/Hdr/Ftr Formats file \#78.2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The name of this file was changed from Flash Card Formats to Lbl/Hdr/Ftr Formats.

# Diagnostic Codes file \#78.3 Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> April 1998 Radiology/Nuclear Medicine V. 5.0 23

> Inactive \#5

# Label Print Fields file \#78.7 Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unique \#6

# Rad/Nuc Med Division file \#79 Field Name Changed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Warning on Unverified Reports? was changed to Warning on Rpts Not Yet Verif? \#.125

# Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Allow 'Released/Unverified (moved to Imaging Locations file \#79.1) Allow 'VA' Patient Entry \#.13

> Allow 'Non-VA' Patient Entry \#.14 Ask 'Requesting Physician' \#.15

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Auto E-Mail to Req. Phys? \#.126 Rpharm Dose Warning Message \#125

# Imaging Locations file \#79.1 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Input Devices \#50

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Allow 'Released/Unverified (moved from Rad/Nuc Med Division file \#79) Urgent Request Alerts? \#20

> Dosage Ticket Printer \#23 Cancelled Request Printer \#24 Stat Request Alert Recipients \#150

# Imaging Type file \#79.2 Fields Removed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Device Assignment Explanation \#75

# Fields Added:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Radiopharmaceuticals Used? \#5

> All free text pointer fields to the Device file were converted during installation to regular VA FileMan pointer fields that allow choices from lists by entering only the first few characters. (E3R 3894)

> This affects the following fields:

> Rad/Nuc Med Procedure file \#71 Required Flash Card Printer Name (#3) Imaging Locations file \#79.1 Flash Card Printer Name (#3)

> Jacket Label Printer Name (#5) Report Printer Name (#10) Request Printer Name (#16)

> All obsolete fields have been removed from the Rad/Nuc Med data dictionaries and references to them in code have been taken out.