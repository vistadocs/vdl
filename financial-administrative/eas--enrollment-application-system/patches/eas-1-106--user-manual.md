---
title: EAS*1*106 LOCAL Signed Means Test Application (ROSSIO 22) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: LOCAL Signed Means Test Application (ROSSIO 22)
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1*106
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](eas-1-106-local-signed-means-test-application-rossio-22-user-manual/001.png)
audience: 
keywords: 
  - letters
  - date
  - letter
  - test
  - print
  - report
  - means
  - appendix
  - table
  - contents
page_count: 0
word_count: 10142
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 17
has_toc: False
is_stub: False
pub_date: March 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p106_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p106_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-1-106-local-signed-means-test-application-rossio-22-user-manual/001.png)

local signed mEANS TEST application (Rossio 22)

enrollment application system (eas)

USER Manual

Patch EAS\*1\*106

March 2014

V*IST*A System Design & Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [<table>](#table)
- [# Introduction](#introduction)
- [Using the Software](#using-the-software)
    - [Search for MT Anniversary Dates Option](#search-for-mt-anniversary-dates-option)
    - [This option searches for 60-day MT anniversary dates by scanning the Annual Means Test File (#408.31) and adds the letter candidates to the EAS MT Letter Status File (#713.2). The use of this option will not actually cause the letters to print. Printing of the letters will be handled through the Letters Print Menu Option discussed elsewhere in this document.](#this-option-searches-for-60-day-mt-anniversary-dates-by-scanning-the-annual-means-test-file-40831-and-adds-the-letter-candidates-to-the-eas-mt-letter-status-file-7132-the-use-of-this-option-will-not-actually-cause-the-letters-to-print-printing-of-the-letters-will-be-handled-through-the-letters-print-menu-option-discussed-elsewhere-in-this-document)
    - [Veteran MT Return Edit Option](#veteran-mt-return-edit-option)
    - [Letters Print Menu](#letters-print-menu)
    - [Report Menu](#report-menu)
    - [EAS MT Parameter Menu](#eas-mt-parameter-menu)
- [Appointment Blocking](#appointment-blocking)
- [# Glossary](#glossary)
- [# Appendix A – Test Letter](#appendix-a-test-letter)
- [Appendix B – 60 Day Letter](#appendix-b-60-day-letter)
- [Appendix C – 30-Day Letter](#appendix-c-30-day-letter)
- [Appendix D – Report of Contact Form](#appendix-d-report-of-contact-form)
- [Appendix E – 0-Day Letter](#appendix-e-0-day-letter)
- [Appendix F – Count of Pending Letters to be Printed](#appendix-f-count-of-pending-letters-to-be-printed)
- [<table>](#table-1)
- [Appendix G – Auto-MT Letters Summary Report](#appendix-g-auto-mt-letters-summary-report)
- [Appendix H – Means Test Letters Statistics Report](#appendix-h-means-test-letters-statistics-report)
- [Appendix I – Summary of Unreturned Means Test Letters](#appendix-i-summary-of-unreturned-means-test-letters)
- [Appendix J – Means Test Expiration by Appt Date](#appendix-j-means-test-expiration-by-appt-date)
- [Appendix K – Means Test Expiration Report](#appendix-k-means-test-expiration-report)
- [Appendix L – Flowchart of Search Process](#appendix-l-flowchart-of-search-process)
- [Appendix M – Flowchart of Letters Option Process](#appendix-m-flowchart-of-letters-option-process)
- [Appendix N– Flowchart of Process of Making an Appointment](#appendix-n-flowchart-of-process-of-making-an-appointment)
- [Appendix O – FAQ (Desk Reference)](#appendix-o-faq-desk-reference)
- [Appendix P – FAQ (Post-Release Field Call Edition – May 2002)](#appendix-p-faq-post-release-field-call-edition-may-2002)
- [# Appendix Q – FAQ (Post-Release – Patch EAS\1\15 – Aug. 2002)](#appendix-q-faq-post-release-patch-eas115-aug-2002)
- [Index](#index)

# <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 21%" />
<col style="width: 58%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision Date</th>
<th>Brief Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/24/14</td>
<td><p>Added note to inform user EAS*1*106 disabled the means test letter options and associated jobs after contents and before the Automated Means Test Letters section.</p>
<p>Updated footer date to March 2014.</p></td>
<td>Darlene Morris</td>
</tr>
<tr class="even">
<td>08/14/02</td>
<td>Revised Section on Related Manuals/Documentation. Added Appendices P and Q.</td>
<td>Debbie Myers</td>
</tr>
<tr class="odd">
<td>07/26/02</td>
<td>Revisions due to release of Patch EAS*1*15; additions made to Appendix O (Desk Reference)</td>
<td>Debbie Myers</td>
</tr>
<tr class="even">
<td>04/11/02</td>
<td>Initial Version based on release of Patch EAS*1*3</td>
<td>Debbie Myers</td>
</tr>
<tr class="odd">
<td></td>
<td>Deployment of the VFA software (DG_53_P858.KID) deactivated the Means Test Letters and associated software.</td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

> **NOTE:** The Veterans Financial Assessment project removed the requirement for Veterans to renew their means test each year. EAS\*1\*106 deployed with DG_53_P858.KID disabled the means test letter options. Sites were requested to remove the associated scheduled jobs.

The MTCHK^EASMTCHK API shall return a MT Not Required result if a current

Means Test is less than 1 year old as of the Veterans Financial

Assessment (VFA), January 1, 2013.

The following menu options were disabled.

Automated Means Test Letter Menu \[EAS MT AUTO LETTERS MENU\]

Search For MT Anniversary Dates \[EAS MT LETTERS SEARCH\]

Veteran MT Return Edit \[EAS MT RETURNED\]

Letters Print Menu \[EAS MT PRINT MENU\]

Sixty Day Letters Print \[EAS MT 60 DAY LETTER PRINT\]

Thirty Day Letters Print \[EAS MT 30 DAY LETTER PRINT\]

Zero Day Letters Print \[EAS MT 0 DAY LETTER PRINT\]

Reprint Letters by Processing Date \[EAS MT REPRINT LETTERS\]

Reprint Single Letter \[EAS MT REPRINT SINGLE LETTER\]

Print Report of Contact \[EAS MT REPORT OF CONTACT\]

User Enrollee Site Print Override \[EAS MT UES OVERRIDE\]

Report Menu \[EAS MT REPORT MENU\]

Count of pending letters to be printed \[EAS MT PENDING LETTERS\]

Automated MT Letters Summary Report \[EAS MT SUMMARY REPORT\]

Means Test Letters Statistic Report \[EAS MT STATISTICS SUMMARY\]

Unreturned Letter Statistic Report \[EAS MT UNRETURNED LETTERS\]

Means Test Expiration by Appt Date \[EAS MT APPT EXPIRATION RPT\]

Means Test Expiration Report \[EAS MT EXPIRATIONS\]

User Enrollee Status for MT Letters \[EAS MT UE STATUS\]

EAS MT Parameter Menu \[EAS MT SETUP MENU\]

EAS MT Parameter Entry/Edit \[EAS MT PARAMETERS\]

Prohibit MT Letters Add/Edit \[EAS MT PROHIBIT EDIT\]

Edit Final Section of Letters \[EAS MT LETTERS EDIT\]

Print a Test Letter (EAS MT) \[EAS MT TEST LETTER\]

Clear Letter Search In-Use flag \[EAS MT CLEAR IN USE FLAG\]

The following background jobs should no longer be scheduled:

Background print job for EAS MT Letters \[EAS MT LETTER BG PRINT\]

Background search for MT Anniversary dates \[EAS MT LETTERS BG SEARCH\]

Daily Means Test Expiration Report \[EAS MT EXPIRATION BG PRINT\]

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Overview

This project was initially undertaken in response to Item \#22 in the "Report of Task Force to Review Enrollment, Means Testing and Income Verification" (a.k.a. Rossio Report) dated December 15, 2000. In the area of Means Test (MT) Deficiencies, Item \#22 required that the Veterans Health Administration (VHA) identify best practices for means testing and acquiring veterans’ signatures at the local level and explore the promulgation of these best practices throughout the system. Until Patch EAS\*1\*3 was released in April 2002, there were no provisions within Veterans Information System & Technology Architecture (V*IST*A) functionality that prevented the scheduling of future appointments for patients who required a MT. Additionally, there was no mechanism present to provide the patient adequate notification of the need to provide a current MT prior to the annual anniversary date. In response to the Rossio Report, the Enrollment Task Force recommended the national implementation of functionality similar to that developed locally at several sites in order to manage scheduling activities for veterans who require the completion of a MT. Sites that had developed and implemented local software (Class III) provided copies of their routines and supporting documentation to the Enrollment Systems Group (ESG) to assist in this endeavor.

Patch EAS\*1\*3 (April 2002) provided a national patch release to the Enrollment Application Systems (EAS) software of locally implemented software that had been converted from Class III to Class I.

Patch EAS\*1\*15 is in response to requests for enhancements and changes to the way MT reminder letters are printed and to correct issues with letter printing as reported by several sites.

##################### Functionality

This project addresses two major issues of functionality for the V*IST*A sites defined as MT deficiencies by the Enrollment Task Force:

- Generation of letters to veterans at designated times prior to the expiration of a veteran's MT and the tracking of letter status.
- Prevention of scheduling future appointments or the check-in/check-out of appointments for patients requiring a MT.

#####################  Related Manuals/Documentation

In addition to this User Manual, a Technical Manual and PIMS User Manual change pages will be released with the Local Signed MT Application software.

You can download the Local Signed MT Application User and Technical Manuals as follows:

From the Anonymous Directory:

- Go to the anonymous.software directory.
- Ftp the files listed in the following table. Remember to use binary format.

|                  |                             |
|------------------|-----------------------------|
| File Name    | Documentation Component |
| EAS_1_P15_UM.pdf | User Manual                 |
| EAS_1_P15_TM.pdf | Technical Manual            |

From the Project Notebook Web Page:

REDACTED

From VistA University, listed within the Enrollment Training Initiatives under Local Means Test ~ Appointment Blocking:

REDACTED

You may obtain a .pdf version of the PIMS v5.3 User Manual – Scheduling Module through the V*IST*A Documentation Library REDACTED. References to the functionality included in the Local Signed MT Application software may be found in the Appointment Menu under the Make Appointment and Check-in/Unsched. Visit options.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Veterans Financial Assessment project removed the requirement for Veterans to renew their means test each year. EAS\*1\*106 deployed with DG_53_P858.KID disabled the means test letter options. Site were requested to remove the associated scheduled jobs.

##################### Automated Means Test Letter Menu

The automated MT letter functionality provides the V*IST*A site with the ability to notify the patient in advance of the need to provide a MT via the use of a letter generated 60 days prior to the MT anniversary date and following up with additional letters at the 30 and 0-day marks if a response is not received. An option to generate a Report of Contact for telephone follow-up with the veteran is also provided. As specified by the Health Eligibility Center (HEC), these letters are Means Test date-based and are not linked to Appointments or Scheduled Activities of the veteran.

This new functionality adds a top-level menu option (Automated Means Test Letter Menu) to the EAS software. This new option contains three sub-menus and several options.

> Select OPTION NAME: Automated Means Test Letter Menu

> Search For MT Anniversary Dates

> Veteran MT Return Edit

> Letters Print Menu ...

> Report Menu ...

EAS MT Parameter Menu ...

> Select Automated Means Test Letter Menu Option:

### Search for MT Anniversary Dates Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This option searches for 60-day MT anniversary dates by scanning the Annual Means Test File (#408.31) and adds the letter candidates to the EAS MT Letter Status File (#713.2). The use of this option will not actually cause the letters to print. Printing of the letters will be handled through the Letters Print Menu Option discussed elsewhere in this document.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that the process handled by the Search for MT Anniversary Dates Option may be scheduled by your site’s Information Resources Management (IRM) Service as a background job to run automatically at specified intervals. If your site chooses to go with this method, it will not generally be necessary to run the Search for MT Anniversary Dates Option interactively; however, you can choose to run this option interactively at any time. From the Select Automated Means Test Letter Menu Option, choose the Search for MT Anniversary Dates Option.

Once you activate the option, the search will automatically process from the last date it was run to the current date. The only time you will be allowed to select a specific date will be the first time it is run after installation. At that time, the default will be set at T-30 (i.e., today minus 30 or 30 days in the past), but you will be allowed to change the date if desired. To specify an alternate starting date, answer “No” at the “Ok to continue? YES//” prompt. You will be asked to enter a different starting date, “Select new start date: Dec 15, 2001//”.

> Select Automated Means Test Letter Menu Option: Search For MT Anniversary Dates

> \>\> Processing date Aug 13, 2001 in progress \<\<

> \>\> Processing date Aug 14, 2001 in progress \<\<

> \>\> Processing date Aug 15, 2001 in progress \<\<

> \>\> Processing date Aug 16, 2001 in progress \<\<

> \>\> Processing date Aug 17, 2001 in progress \<\<

See Appendix L for details on the search process. Note that there are several checks that must be passed before a letter entry will be created. The search process will only search for “new” 60-day candidates. When an entry is created, 30- and 0-day dates are established in the MT Letter Status File (#713.2). All processing for 30- and 0-day letters occurs in the MT Letter Status File. No additional scans of the Annual Means Test File (#408.31) are performed for 30- and 0-day letters.

For DCD Sites only: If you are a DCD site, when the letter search functionality runs, only the 0-day letters will be flagged to print. Although entries will be made for 60- and 30-day letters, they will not be flagged to print. Therefore, after running this option, it will be 60 days (0-day threshold) before any letters actually print as result of this search.

### Veteran MT Return Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to update the veteran’s MT letter status in the EAS MT Letter Status File (#713.2) when a current VHA Form 10-10EZ, Application for Health Benefits, is returned to the facility as the result of a mailing. A positive (“Yes”) entry in the “Means Test Returned?” field will eliminate the further generation of MT reminder letters for the specific patient.

When prompted to select the letter status entry to be updated, you may answer with the patient name, the processing date, or the EAS MT letter status entry number. At the following prompt, answer “Yes” to “Means Test Returned?” to indicate that the veteran has returned a MT. Next, enter the date the MT was returned. You will then be given the opportunity to enter any additional comments you may have related to the return of the MT.

> Select Automated Means Test Letter Menu Option: Veteran MT Return Edit

> Select the Letter Status entry to update: HAYNES, LISA

> MEANS TEST RETURNED?: NO// YES

> DATE MEANS TEST RETURNED: 8/17/01 (AUG 17, 2001)

> COMMENTS:

> 1\>

Please note that there is no direct interaction between this option and the MT functionality. If a new MT is entered for a veteran, users should still use this option to update the MT Letter Status entry. If this option is NOT used, it is possible that a follow-up letter will still be generated, despite the fact that a MT has been entered. Conversely, this option could shut down the letters and indicate a response has been received without a MT actually being entered into the Annual Means Test file. Facilities should monitor this closely.

When printing letters, there is a check that attempts to determine whether the veteran’s MT status has changed. If this check determines that a MT status has changed, it will set this flag to “Yes” and enter a comment of “Auto-Generated”. Since there is not a direct linkage between this option and the MT menu options, this process should not be relied on exclusively.

### Letters Print Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sub-menu contains six different options that are detailed individually below. The letters and Report of Contact are formatted to print on an 80-column printer. The letters are additionally formatted for the patient’s address to appear in a standard 9-1/2” x 4-1/8” window envelope.

Note that the process handled by the Letters Print Menu Option may be scheduled by your site’s IRM Service as a background job to run automatically at specified intervals and print all auto-generated MT letters/forms. The background job will print all letters to a previously specified print device. (You may find further information pertaining to print parameters in the EAS MT Parameter Entry/Edit Option section elsewhere in this manual.) If your site chooses to utilize this method, it may not be necessary to run the Letters Print Menu Option interactively; however, you can choose to run the option interactively at any time to print/reprint specific MT reminder letters as indicated below.

> Select Automated Means Test Letter Menu Option: Letters Print Menu

> Sixty Day Letters Print

> Thirty Day Letters Print

> Zero Day Letters Print

> Reprint Letters By Processing Date

> Reprint Single Letter

> Print Report of Contact

The letters/forms will print to the user-specified print device. If filtering letters by preferred facility is enabled, when you select a letter type from the Letters Print Menu, you will be asked the following prompt(s):

> Filter letters by Preferred Facility? NO// Yes

> Select INSTITUTION: xxxxx

For the 60/30/0-Day Letters Print options, if you answer “YES” to the prompt “Filter letters by Preferred Facility?”, you will also be prompted to enter an institution to filter on. The location can be any entry in the Institution File (#4). Letters for those veterans who have specified that particular institution as their Preferred Facility (Field \#27.02) in the Patient File (#2), will be printed. After selecting a location to filter the letters by, you will be asked for a print device.

<span class="mark">  
</span>When any one of the first three Letters Print Menu options (Sixty/Thirty/Zero Day Letters Print) is selected and the “Allow Filtering by Location?” parameter is active, the possibility exists to miss printing letters for those veterans who have not specified a preferred facility. If you are allowing filtering, it is recommended that as a final step, letters be printed where “Filter letters by Preferred Facility?” is answered “NO” to ensure any remaining letters are printed.

The checks that occur when the print process runs could change the status of a letter and prevent the letter from printing. If a complete address for a veteran is not on file, the letter will not print, and a Mailman notification will be sent to the EAS MT LETTERS mail group. Also, the letter functionality will check whether the current MT is owned by the facility. It checks this by examining the Source of Income Test (Field \#.23) in the Annual Means Test File (#408.31). If this field is VAMC, this MT is considered "owned" by the current facility and may be edited. If this field is IVM or Other Facility, the MT is not considered "owned" by the current facility and a MT letter will not be printed. In this situation, the MT Returned flag will be updated to “yes” and a comment of “MT owned by another facility” will be entered. If the source of income test is DCD and the site is a DCD site, the 0-day letter will still be printed. See Appendix M for details.

Examples of each of the various letters (60/30/0-day) may be found in Appendices B, C, and E of this document as noted individually below. Each letter indicates with \[brackets\] those areas where the system would automatically insert data based on what is in the local files. The portion of the letter that is in *italics* (last paragraph and signature block) would be free text as entered by the site. This will be discussed further in the Edit Final Section of Letter option elsewhere in this manual.

Before printing letters, if you want to get an idea of what letters are flagged to print, you can run the Automated MT Letters Summary on the Report Menu. (See Report descriptions elsewhere in this manual.)

See the diagram in Appendix M for the process flow that occurs when the Sixty/Thirty/Zero Day Letters Print options are used.

#### Sixty Day Letters Print

Prints the 60-day anniversary letters pending in the EAS MT Letter Status File (#713.2). An example of a 60-day letter may be found in Appendix B of this document.

> Select Letters Print Menu Option: Sixty Day Letters Print

> Filter letters by Preferred Facility? NO// YES

> Select INSTITUTION: xxxxx

<u>  
</u>

#### Thirty Day Letters Print

Prints the 30-day anniversary letters pending in the EAS MT Letter Status File (#713.2). An example of a 30-day letter may be found in Appendix C of this document.

> Select Letters Print Menu Option: Thirty Day Letters Print

> Filter letters by Preferred Facility? NO// Yes

> Select INSTITUTION: xxxxx

#### Zero Day Letters Print

Prints the 0-day anniversary letters pending in the EAS MT Letter Status File (#713.2). An example of a 0-day letter may be found in Appendix E of this document.

> Select Letters Print Menu Option: Zero Day Letters Print

> Filter letters by Preferred Facility? NO// Yes

> Select INSTITUTION: xxxxx

#### Reprint Letters by Processing Date

Reprints 60, 30, and 0-day MT letters for a specific processing date. (Note: “Processing date” refers to the date the initial 60-day letter search was accomplished.) As soon as the option is selected, a list of available processing dates will be displayed and you will be prompted to select a date. Once the desired date is entered, you will be required to select a letter type (60-day, 30-day, or 0-day).

> Select Letters Print Menu Option: Reprint Letters By Processing Date

> Filter letters by Preferred Facility? NO// NO

> Available Processing Dates:

> 8/2/01

> 8/28/01

> 8/31/01

> Enter processing date to re-run letters: 8/28 (AUG 28, 2001)

> Select one of the following:

> 1 60-Day

> 2 30-Day

4 0-Day

> Select letter type: 2 30-Day

> . . . EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT . . .

> DEVICE: HOME//

#### Reprint Single Letter

Reprints a single MT letter for a selected veteran and processing date. You will first be asked to enter a patient name. A notification will be displayed regarding the patient’s MT status (if applicable), and you will be prompted to enter \<RETURN\> to continue. Next, you will need to enter the specific processing date for the letter that you want to have reprinted. If the date that you enter was not a processing date, you will be given a list of processing dates from which to choose. Once you have selected the appropriate date, you will be prompted to select a specific letter type (60-day, 30-day, 0-day).

> Select Letters Print Menu Option: Single Letter Reprint

> Select PATIENT: SMITH, JONATHAN SMITH, JONATHAN 8-14-22 206081422P NO

> NSC VETERAN KOPECKY,STEPHEN

> Enrollment Priority: Category: IN PROCESS End Date:

> \*\*\* Patient Requires a Means Test \*\*\*

> Primary Means Test Required from SEP 5,2000

> Enter \<RETURN\> to continue.

> Select the letter processing date for this patient: 8/4/01 AUG 04, 2001

Answer with EAS MT LETTER STATUS ENTRY NUMBER, or PROCESSING DATE, or

> RECIPIENT

> Choose from:

> 1 AUG 02, 2001 SMITH,JONATHAN Sep 5,2000

Select the letter processing date for this patient: 1 8-2-2001 SMITH,JONATHAN

> R Sep 5,2000

> Select one of the following:

> 1 60-Day

> 2 30-Day

> 4 0-Day

> Select letter type: 2 30-Day

> Select DEVICE: HOME//

After the patient has been selected, two checks are made: one for the Prohibit Flag and another for Date of Death. If either condition is met, no further processing will occur. After the processing date has been selected, checks are made to see if a MT has been returned or if the MT is no longer required. No further processing will occur if either condition is met. Only previously printed letters will appear in the selection list. If the 0-Day letter has not yet printed, it will not appear as a selection in the list. If no letters have yet been printed, you will be informed of that fact and no further processing will occur. All rules for printing to the primary or alternate print locations apply.

#### Print Report of Contact

Prints a Report of Contact (ROC) for a selected veteran(s). You will first be asked to enter a patient name. You may answer with the patient name, the processing date, or the EAS MT letter status entry number. You will next be prompted to enter \<RETURN\> to continue, followed by an opportunity to enter another patient name. Once you have entered the name for all veterans for which an ROC is desired, you will be prompted to select a print device. An example of a Report of Contact may be found in Appendix D of this document.

> Select Letters Print Menu Option: Single Letter Reprint

Select PATIENT: McCoy,Leonard

Enter \<RETURN\> to continue. 3-11-2002 MCCOY,LEONARD Apr 19,1999

Select Patient:

DEVICE: HOME//

### Report Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sub-menu contains six different options that are detailed individually below.

> Select Automated Means Test Letter Menu Option: Report Menu

> Count of pending letters to be printed

> Automated MT Letters Summary Report

> Means Test Letters Statistic Report

> Unreturned Letter Statistic Report

> AP Means Test Expiration by Appt Date

> EX Means Test Expiration Report

> Select Report Menu Option:

#### Count of Pending Letters to be Printed

Used after MT letters have been initiated to obtain a count of how many letters are pending and have not yet printed. You will be prompted for “Print Summary Only? YES//”. If you take the default, a summary of letters currently flagged to print will be displayed. If you answer "NO" at the prompt, after the summary is displayed, you will be prompted to display the detailed listing of letters flagged to print:

> Select Report Menu Option: Count of pending letters to be printed

> Print Summary Only? YES//

> DEVICE: HOME// UCX/TELNET

The following data will display or print on the summary report:

- Report title
- Print date
- Number of letters flagged to print for each letter type

The following data will display or print on the detailed list:

- Report title
- Print date
- Page number
- Column heading for originally scheduled print date\*
- Column headings per letter type
- Column heading for total
- Number of pending letters to be printed for each listed scheduled print date by letter type and total

\*Note: The Sched. Date is the date on which the flagged letter is currently scheduled to print. If the date is prior to the current date, the letter may have an incomplete address that is preventing it from printing. If the date is in the future, the print date has not yet been reached.

An example of the summary report and detailed list generated may be found in Appendix F of this document.

#### #### Automated MT Letters Summary Report

Provides a statistical report for a given processing date range. Once this option is selected, you will be prompted to enter both a start and end processing date. Only those actions that processed, i.e., 60-day search and initial entry into the EAS MT Letter Status File (#713.2), during the date range of the report will be included in the report. The start date entered must be either the default processing date or another date; it may not be a future date. The end date must be either the default of the current date or a prior date; it may not be a future date. Once the date range has been entered, you will be prompted to enter a print device.

> Select Report Menu Option: Summary by Processing date/s Report

> Start with Processing date: OCT 1, 1998// 7/15/01 (JUL 15, 2000)

> Ending Processing date: TODAY// 8/10/01 (AUG 10, 2001)

> A 132-column printer is required for this report.

> DEVICE: HOME//

The following data will display or print on the report:

- Report title
- Date range
- Print date
- Page number
- Entry number
- Patient name (Last 4)
- MT anniversary date
- Letter type
- Date of letter
- Flagged status
- Printed status
- Letter print date
- Prohibit status
- Means Test return date (if available)
- Comments (if available) – Note: Only the first 30 characters on the first comment line will be displayed.

Any patient who died in between letters will be flagged with a \*D\*. If a MT has been returned and is no longer required, the MT returned date will be shown below the veteran’s name.

An example of the report generated may be found in Appendix G of this document.

#### Means Test Letters Statistics Report

Provides a count of the total MT letters printed for a particular date range. Also provides a total of the letters during that processing date range for which the MT returned flag was turned on, broken down by reasons for the return as entered in the Comments field in the EAS MT Letter Status File (#713.2). You will be prompted to enter both a start and ending processing date and a print device.

> Select Report Menu Option: Means Test Letters Statistic Report

> Start with Processing date: OCT 1, 1998// (OCT 01, 1998)

> Ending Processing date: TODAY// (JUL 10, 2002)

> DEVICE: HOME// UCX/TELNET

The following data will display or print on each report:

- Report title
- Letter processing date range
- Print date
- Column headings per letter type
- Column heading for total
- Number of letters printed per letter type and total
- MT returned totals for:
  - Auto-Generated
  - Future MT
  - Owned by other site
  - Returned by Veteran
  - Total
- Number of patient records with prohibit flag during date range

An example of the report generated may be found in Appendix H of this document.

#### Unreturned Letter Statistic Report 

Provides statistics for those letters that have been printed and mailed and that do not have a MT returned. This report scans the letters printed for which no MT has been returned. Means Test Returned? (Field \#4) in the EAS MT Letter Status File (#713.2) is the determinant. The report scans in reverse order; i.e., 0-day letters, then 30-day letters, then 60-day letters. If a letter has been printed, no earlier letters are checked. This report will show only the most current letters printed. Once the option is selected, the report will display to the screen.

> Select Report Menu Option: Unreturned Letter Statistic Report

The following data shall display on the report:

- Report title
- Number of 60-Day letters printed with no MT returned
- Number of 30-Day letters printed with no MT returned
- Number of 0-Day letters printed with no MT returned
- Total number of letters for all letter types printed with no MT returned

An example of the report generated may be found in Appendix I of this document.

#### Means Test Expiration by Appt Date

Provides a list of veterans by clinic whose MT anniversary date will fall on their appointment date. Once this option is selected, you will be prompted to enter a date for which to run the report. The date selected may be the current or a future date. Once the date has been entered, you will be prompted to enter a print device. The report will display by clinic and will print information from each clinic where appointments are found for patients who have a MT due on the date selected.

> Select Report Menu Option: Means Test Expiration by Appt Date

> Run report for date: TODAY// (JUL 10, 2002)

> DEVICE: HOME//

The following data shall display or print on the report:

- Report title, including name of clinic
- Appointment date selected
- Print date
- Page number
- Patient name
- Last four digits of Social Security Number
- Anniversary date
- Appointment time

If there are no MT anniversary dates found for the selected appointment date, a message to that affect will be displayed.

Examples of the reports generated may be found in Appendix J of this document.

#### #### Means Test Expiration Report

Provides a list of patients with a MT expiration date within a specified date range. Note that this report may be scheduled by your site’s IRM Service as a background job to run automatically at specified intervals. If your site chooses to go with this method, the generated report will be for a one-day period, today minus 1. If the report is set to run after midnight, it will list the previous day’s MT expirations.

Once this option is selected, you will be prompted to enter both a start and end search date. Only those MTs that expire during the date range of the report will be included in the report. The start date entered may be either the default processing date or any past or future date. The end date may be either the default of the current date or a past or future date. The date range may be for a single date (same start and end date). Once the date range has been entered, you will be prompted to enter a print device.

> Select Report Menu Option: Means Test Expiration Report

> Enter date range for anniversary date search

> Start Date: Nov 15, 2001//11/01/00 (NOV 01, 2000)

End Date: Nov 15, 2001// (NOV 15, 2001)

> DEVICE: HOME//

The following data will display or print on the report:

- Report title
- Date range
- Print date/time
- Page number
- Patient name
- Social Security Number
- MT expiration date
- Current MT status
- Future appointments

If there are no MT expirations for the selected date range, a message to that affect will be displayed.

Examples of the reports generated may be found in Appendix K of this document.

### EAS MT Parameter Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

- You must have the EAS MTSUPV key to use the EAS MT Parameter Menu option.

This sub-menu contains five different options that are detailed individually below.

> Select Automated Means Test Letter Menu Option: EAS MT Parameter Menu

> EAS MT Parameter Entry/Edit

> Prohibit MT Letters Add/Edit

> Edit Final Section of Letters

> Print a Test Letter (EAS MT)

> Clear Letter Search In-Use flag

> Select EAS MT Parameter Menu Option:

#### EAS MT Parameter Entry/Edit

The EAS MT Parameter Entry/Edit option will display the current parameters for MT letters and allow for editing of the individual parameters as desired.

EAS MEANS TEST LETTERS PARAMETER ENTRY/EDIT

=============================================================================

\[1\] Parameters

Primary Print Device: : DEV\$PRT 10/6/UP

Allow Filtering by Location? : YES

Send Means Test Completion Notice? : NO

Envelope Offset : 0

Allow Alternate Return Address? : YES

Edit Parameters? YES//

Hit \<Enter\> at the “Edit Parameters? YES//” prompt to edit any of the parameters listed below:

- Primary Print Device
- Allow Filtering by Location?
- Send Means Test Completion Notice?
- Envelope Offset
- Allow Alternate Return Address?

*Primary Print Device*: A primary print device for the printing of MT letters may be specified. This device must be set up in the Device File (#3.5) in order to be selected. If entered, this device will be used as the default prompt when using the Letters Print options.

*Allow Filtering by Location?*: Enabling this allows the facility to filter the printing of the MT letters by preferred location. If this parameter is enabled, the software will query the Preferred Facility Field (#27.02) in the Patient File (#2) for the veteran. Only the MT letters where the veteran’s preferred facility matches will be printed. (Note: Installed default is “No”.)

*Send Means Test Completion Notice?*: Enabling this will result in a bulletin being generated upon completion of data entry of a veteran’s MT information through the option, Complete a Required Means Test. This bulletin will be sent to all users identified in the mail group EAS MT LETTERS to provide notification that a MT has been received and completed. (Note: Installed default is “No”.)

*Envelope Offset*: You should not have to set this UNLESS you need to move the veteran’s address to the right a few spaces in order to line it up properly in a window envelope. This parameter will only allow you 0 to 6 spaces. (Note: Installed default is “0”.)

*Allow Alternate Return Address?:* This allows sites to specify whether the primary facility's return address or the return address for the preferred facility will print on the MT reminder letters. The parameter will allow either a "YES" or a "NO". If set to "YES", when the MT reminder letter is printed, if a valid facility address is available, that address will print as the return address on the letter. If a valid address is not available, or the parameter is set to "NO", the facility address for the primary site will print as the return address.

#### Prohibit MT Letters Add/Edit

Certain circumstances warrant that a patient not receive a reminder letter to submit a MT. For these individuals, the patient should be flagged through the option Prohibit MT Letters Add/Edit that will prohibit the generation of a letter. Any patient from the Patient File (#2) may have a prohibit flag set or removed. If a patient is flagged, a MT letter will not be generated or mailed.

This option sets or removes the Prohibit flag in the EAS MT Patient Status File (#713.1). You will be given the choice of setting (S) or removing (R) the Prohibit Flag. Once you have entered the desired action, you will be prompted for the patient name. Once the patient name has been entered, the prompts will vary depending on whether you choose to set or remove the flag.

If you choose to SET the Prohibit Flag, you will be required to select a patient, confirm that you wish the patient added to the Patient Status File (if he is not already in that file), indicate the effective date for prohibiting printing of the letters, and state the reason for prohibiting the printing of the letters (3-60 characters).

> Select EAS MT Parameter Menu Option: Prohibit MT Letters Add/Edit

> Select one of the following:

> S Set Prohibit Flag

> R Remove Prohibit Flag

> Set or remove the MT Prohibit flag: Set Prohibit Flag

> Select Patient: ROSSIO,FIVE 3-16-24 206031624P NO NSC VETERAN KOPECKY,STEPHEN

> Enrollment Priority: GROUP 3 Category: IN PROCESS End Date:

Add patient to the Patient Status File? YES//

> PROHIBIT LETTER EFFECTIVE DATE: T (NOV 19, 2001)

> PROHIBIT LETTER REASON: \<enter appropriate reason; answer must be 3-60 characters in length\>

If you choose to REMOVE the Prohibit Flag, you will simply be required to select a patient.

> Select EAS MT Parameter Menu Option: Prohibit MT Letters Add/Edit

> Select one of the following:

> S Set Prohibit Flag

> R Remove Prohibit Flag

> Set or remove the MT Prohibit flag: Remove Prohibit Flag

> Select Patient: ROSSIO,FIVE ROSSIO,FIVE 3-16-24 206031624P NO

> NSC VETERAN KOPECKY,STEPHEN

Enrollment Priority: GROUP 3 Category: IN PROCESS End Date:

#### Edit Final Section of Letter

Each of the 60-, 30-, and 0-day MT reminder letters will be formatted in three separate sections – the header, the initial section and the final section. The Report Of Contact form is also formatted in three separate sections – the header, the initial section and the footer section.

The header for the 60/30/0-day letters includes the return address, date, patient name and address, and MT anniversary date. The primary institution address will serve as the return address for the facility. The header for the ROC form includes patient name, Social Security Number (SSN), address, telephone number, and VA Office. See the Technical Manual Installation Instructions for additional details on the return address.

For the 60/30/0-day letters, the Health Administration Services (HAS) Office has specified the contents of the initial section of the letter, and this field may not be modified by the V*IST*A facilities. This section contains the text informing the patient of the purpose of the letter.

The final section of the 60-, 30- and 0-day letters will be set up through a multiple field allowing for the selection of a preferred location and then drilling down to the text insertion that best fits the needs of the local facility and their associated patients. This information may include site-specific points of contact, hours of operation and signature blocks. Those facilities with integrated sites will have the capability of setting up this portion of the letter to provide information unique to their remote sites, using the preferred facility specified by the veteran. If a facility is not determined, a generic final section and signature block will be printed.

To edit the final section of any of the three letter types or the free text portion of the ROC form, you will need to access the Edit Final Section of Letter option. Once selected, you will be prompted to select one of the four letter/form types: 0-day letter, 30-day letter, 60-day letter, and Report of Contact. A prompt to select a preferred location for the final portion of the letter will follow. This field will allow for the selection of a location from within the Institution File (#4). The last field, Final Section, will be free text where you may enter the information relevant to the location and the 60-, 30- or 0-day letter type selected (such as where to call with questions or where to report for a MT, followed by an appropriate signature block) or details pertaining to personal or telephone contact with the veteran (ROC). Note: At a minimum, the final section for the primary facility must be entered. This section will be used for any additional locations for printing where a final section has not been defined.

Select Setup EAS MT Parameters Option: Edit Final Section of Letter

> Select EAS MT LETTERS NAME: ?

> Answer with EAS MT LETTERS NAME, or TYPE

Choose from:

> 0-DAY

> 30-DAY LETTER

> 60-DAY LETTER

> REPORT OF CONTACT

> Select EAS MT LETTERS NAME: 60-DAY

> Select LOCATION: MANCHESTER

> 1 MANCHESTER, NH 608

> 2 MANCHESTER-RO NH 373

> CHOOSE 1-2: 1 MANCHESTER, NH 608

> Are you adding 'MANCHESTER, NH' as

> a new PREFERRED LOCATION (the 1ST for this EAS MT LETTERS)? No// Y (Yes)

> FINAL SECTION:

> 1\>If you have any questions about the Financial Worksheet, please

2\>call the Manchester Veterans Assistance Office at (603) 890-4567

> 3\>between noon and 4 PM weekdays.

> 4\>

> 5\>Sincerely,

> 6\>

> 7\>

> 8\>

> 9\>JOHN DOE

> 10\>Medical Administrative Service

> 11\>

> EDIT Option:

#### Print a Test Letter (EAS MT)

Prints a generic test letter with the following header:

\[Facility Address\]

\[Facility Address\]

\[Facility Address\]

Jul 03, 2002

TEST LETTER (DO NOT MAIL!) (6789)

THIS IS A TEST LETTER STREET ADDRESS

ANYTOWN NY 11111-0000

\[Body\]

You will be asked to select the type of letter to print in a test format and to select a print device. An example of a 60-day test letter may be found in Appendix A of this document.

> Select EAS MT Parameter Menu Option: PRINT a Test Letter (EAS MT)

> Select one of the following:

> 1 60-Day

> 2 30-Day

> 4 0-Day

> Select letter type to test: 1

> DEVICE: HOME// UCX/TELNET

#### #### #### Clear Letter Search In-Use Flag

If, after selecting the Search for MT Anniversary Date option, the message "This process is already running, please try again later" appears and you have confirmed that no one else has actually started another search, then the "In-Use" flag may have been left in the set status due to an error or the task being incorrectly shut down on a previous search. This option may be used to reset the flag. As soon as this option is selected, the flag will be reset and a message indicating “Lock cleared” will appear on the screen. You may then rerun the search option.

> Select EAS MT Parameter Menu Option: Clear Letter Search In-Use flag

> \>\> Lock cleared

> **NOTE:** If running the tasked background option, EAS MT LETTERS BG SEARCH, an alert will be sent to the EAS MTLETTERS mail group members with the message "Auto MT Letters: This process is already running" in place of the user message.

# Appointment Blocking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional functionality included in the Local Signed MT Application software enables facilities to prohibit the scheduling of future appointments and the processing of certain unscheduled appointments for patients requiring a current MT. This determination is made through the use of computed fields currently residing in V*IST*A software and does not require user interaction. When accessing a patient in the Appointment Menu who is determined to require a completed MT, you will receive a screen alert notifying you of the requirement and prohibiting you from proceeding with scheduling of the appointment unless you are a holder of the EAS MTOVERRIDE security key. See Appendix L for a process flow of making an appointment.

See the *Related Manuals/Documentation* section of this document for the location of further information pertaining to this particular functionality.

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Acronyms 

| Acronym     | Description                                       |
|-----------------|-------------------------------------------------------|
| EAS             | Enrollment Application System                         |
| ESG             | Enrollment Systems Group                              |
| HAS             | Health Administration Services                        |
| HEC             | Health Eligibility Center                             |
| IRM             | Information Resources Management                      |
| MT              | Means Test                                            |
| ROC             | Report of Contact                                     |
| SSN             | Social Security Number                                |
| VAMC            | Veterans Affairs Medical Center                       |
| VHA             | Veterans Health Administration                        |
| VISN            | Veterans Integrated Service Network                   |
| V*IST*A | Veterans Information System & Technology Architecture |

# # Appendix A – Test Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA MEDICAL CENTER

123 ALBANY ST

ALBANY NY 12000

Jul 10, 2002

TEST LETTER (DO NOT MAIL!) (6789)

THIS IS A TEST LETTER STREET ADDRESS

ANYTOWN NY 11111-0000

MEANS TEST ANNIVERSARY DATE:

Dear Mr. TEST:

Each year the VA requires non-service-connected veterans and 0% service-connected veterans to complete a financial assessment (means test). Our records show that your annual means test is due.

What Does This Mean To You?

- The means test you completed last year exempted you from copayments for health care provided for your non-service-connected conditions.
- Failure to complete the means test by the anniversary date will prevent us from being able to schedule you for any future care for your non-service-connected conditions.

What Do You Need To Do?

- Complete and sign the Financial Assessment portion of the enclosed VA Form 10-10EZ reporting income and assets for the previous calendar year.
- Return the completed and signed form in the enclosed envelope before your means test anniversary date.
- When you report to your next health care appointment, bring your health insurance card so we may update your health insurance information.
- Notify us if you feel you received this letter in error.

What If You Have Questions?

Thank you for your assistance and cooperation. If you have any questions or need assistance in the completion of the information requested, please contact the VA Medical Center Business Office between 8:00am and 4:00pm Monday through Friday.

Sincerely,

Enclosure

# Appendix B – 60 Day Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[Facility Name\]

\[Address Line 1\]

\[City, State, Zip\]

\[Current Date\]

\[Veteran’s Name\] \[Last 4 of SSN\]

\[Street Address\]

\[City, State, Zip\]

MEANS TEST ANNIVERSARY DATE: \[Anniversary Date\]

Dear \[Title\] \[Veteran’s Last Name\]:

Each year the VA requires non-service-connected veterans and 0% service-connected veterans to complete a financial assessment (means test). Our records show that your annual means test is due \[Anniversary Date\].

What Does This Mean To You?

- The means test you completed last year exempted you from copayments for health care provided for your non-service-connected conditions.
- Failure to complete the means test by the anniversary date will prevent us from being able to schedule you for any future care for your non-service-connected conditions.

What Do You Need To Do?

- Complete and sign the Financial Assessment portion of the enclosed VA Form 10-10EZ reporting income and assets for the previous calendar year.
- Return the completed and signed form in the enclosed envelope before your means test anniversary date.
- When you report to your next health care appointment, bring your health insurance card so we may update your health insurance information.
- Notify us if you feel you received this letter in error.

What If You Have Questions?

*Thank you for your assistance and cooperation. If you have any questions or need assistance in the completion of the information requested, please contact the \[Facility Name\] Business Office at (XXX) XXX-XXXX between 8:00 a.m. and 4:00 p.m. Monday through Friday.Sincerely,Chief HAS or equivalentEnclosures*

# Appendix C – 30-Day Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[Facility Name\]

\[Address Line 1\]

\[City, State, Zip\]

\[Current Date\]

\[Veteran’s Name\] \[Last four of SSN\]

\[Street Address\]

\[City, State, Zip\]

MEANS TEST ANNIVERSARY DATE: \[Anniversary Date\]

Dear \[Title\] \[Veteran’s Last Name\]:

Each year the VA requires non-service-connected veterans and 0% service-connected veterans to complete a financial assessment (means test). Our records show that your annual means test is due \[Anniversary Date\].

As of this date we have not received the updated financial income information we requested in a previous letter.

What Does This Mean To You?

- The means test you completed last year exempted you from copayments for health care provided for your non-service-connected conditions.
- Failure to complete the means test by the anniversary date will prevent us from being able to schedule you for any future care for your non-service-connected conditions.

What Do You Need To Do?

- Complete and sign the enclosed Financial Assessment portion of the enclosed VA Form 10-10EZ reporting income and assets for the previous calendar year.
- Return the completed and signed form in the enclosed envelope before your means test anniversary date.
- When you report to your next health care appointment, bring your health insurance card so we may update your health insurance information.
- Notify us if you feel you received this letter in error.

What If You Have Questions?

*Thank you for your assistance and cooperation. If you have any questions or need assistance in the completion of the information requested, please contact the \[Facility Name\] Business Officeat (XXX) XXX-XXXX between 8:00 a.m. and 4:00 p.m. Monday through Friday.Sincerely,Chief HAS or equivalentEnclosures*

# Appendix D – Report of Contact Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

D E P A R T M E N T O F V E T E R A N S A F F A I R S

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

\| REPORT OF CONTACT \| VA Office \| Identification

> No.

\| Note: This form must be filled out in \| \| \|

\| ink or on typewriter as it becomes a \| \| 123-45-6789 \|

\| permanent record in veterans’ folders. \| \| \|

-------------------------------------------------------------------------------

\| Last Name-First Name-Middle Name (Type or print) \| Date of Contact \|

\| \| \|

\| BREYAR, TED \| 3/11/02 \|

-------------------------------------------------------------------------------

\| Address of Veteran \| Telephone \|

\| 123 THIRD STREET \| (518) 345-6678 \|

\| TROY, NEW YORK 12180 \| \|

-------------------------------------------------------------------------------

\| Person Contacted \| Type of Contact

\| \|

\| \| Personal/Phone \| \|

-------------------------------------------------------------------------------

\| Address of Person Contacted \| Telephone \|

\| \| \|

\| \| \|

-------------------------------------------------------------------------------

Brief statement of information requested and given

Means Test Anniversary Date: Feb 21, 2001

-------------------------------------------------------------------------------

\| Division or Section \| Executed By (signature

> and title)

\| \| \|

\| \| \|

-------------------------------------------------------------------------------

# Appendix E – 0-Day Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[Facility Name\]

\[Address Line 1\]

\[City State Zip\]

\[Current Date\]

\[Veteran’s Name\] \[Last four of SSN\]

\[Street Address\]

\[City, State, Zip\]

MEANS TEST ANNIVERSARY DATE: \[Anniversary Date\]

Dear \[Title\] \[Veteran’s Last Name\]:

According to our records you have not responded to our previous requests to complete the financial section of VA Form 10-10EZ. This is to inform you that your current financial assessment (means test) has expired.

How Does This Affect Your Eligibility for Cost Free Care?

- We do not have a current means test for you on file as is required to determine your eligibility for cost-free care.
- We are unable to schedule you for future care of your non-service-connected conditions.

How Does This Affect Your Enrollment?

- We are unable to determine your priority for enrollment in the VA health care system.

What Do You Need to Do?

- Complete, sign and return a new VA Form 10-10EZ, including the financial section.
- Read the enclosed VA Form 4107, Notice of Procedural and Appellate Rights. If you disagree with our decision, you or your representative may complete a Notice of Disagreement and return it to the Enrollment Coordinator or Health Benefits Advisor at your local VA health care facility.

What If You Have Questions?

*If you have any questions or feel that receipt of this letter is in error, please contact (insert name) at (insert telephone number)* or call the VA Health Benefits Service Center toll free 1-877-222-VETS.

*Sincerely,Chief, Health Administration Service, or equivalentEnclosure*

# Appendix F – Count of Pending Letters to be Printed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Count of Letters Pending to Print (Flag to Print marked 'YES')</p>
<p>Printed: Jul 03, 2002@14:00:48</p>
<p>=================================================================</p>
<p>60-Day letters flagged to print: 32</p>
<p>30-Day letters flagged to print: 4</p>
<p>0-Day letters flagged to print: 10</p>
<p>Press any key to continue...</p>
<p>Detailed List of Letters Flagged to Print</p>
<p>Printed: Jul 03, 2002@14:03:53 PAGE: 1</p>
<p>Sched. Date 60-Day 30-Day 0-day TOTAL</p>
<p>=======================================================================</p>
<p>Jul 24, 1989 1 0 0 1</p>
<p>Jan 13, 1992 0 0 2 2</p>
<p>Feb 17, 1993 0 0 1 1</p>
<h1 id="section-11"></h1></td>
</tr>
</tbody>
</table>

# Appendix G – Auto-MT Letters Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Appendix H – Means Test Letters Statistics Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MEANS TEST LETTERS STATISTIC REPORT

Letter Processing Date Range: Oct 01, 1998 thru Jul 05, 2002

Print Date: Jul 05, 2002@11:22:43

Letter type: 60-day 30-day 0-day Totals

==========================================================================

Letters printed: 18 0 0 18

Means Test returned Totals

AUTO-GENERATED: 1

Future MT: 0

Owned by Other Site: 1

Returned by Veteran: 1

Total: 3

Count of patient records set to prohibit letter during date range: 0

Press any key to continue...

# Appendix I – Summary of Unreturned Means Test Letters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Summary of Most Recent Unreturned Means Test Letters

60-day letters printed: 6

30-day letters printed: 0

0-day letters printed: 0

==============================

Total: 6

Press any key to continue...

# Appendix J – Means Test Expiration by Appt Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example 1:

Means Test Expiration Report by Appt Date for MEDICAL CLINIC

For Appointment Date: Jul 03, 2002

Print Date: Jul 03, 2002@10:07:13

Page 1

Last Anniversary Appointment

Name Four Date Time

==========================================================================

FLOCK,FRED 3642 Jul 03, 2002 7/3/02 2:20 pm

EGG,PATRICK 4521 Jul 03, 2002 7/3/02 11:00 am

Example 2:

Means Test Expiration Report by Appt Date

For Appointment Date: Jul 10, 2002

Print Date: Jul 10, 2002@14:40:58 Page 1

Last Anniversary Appointment

Name Four Date Time

=============================================================================

No MT Anniversary dates found for this appointment date.

# Appendix K – Means Test Expiration Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example 1:

Means Test Expiration Report

Anniversary Date(s): 11/1/2000 - 11/15/2001

Printed: Nov 15, 2001@14:05:30 Page 1

Patient SSN MT Expired Status Future Appts

===============================================================================

WILSON,FRED 429-56-9110 12/13/00 REQD

WILSON,LEE 374-50-1882 12/14/00 REQD

WILSON,EMPLOYEE 208-12-2350P 12/15/00 REQD

PHELPS,ROBERT JR 001-33-2211 12/15/00 REQD

GARIBALDI,THOMAS 345-22-0000 01/05/01 CAT A

JEANS,BLUE 782-34-5679 01/13/01 REQD

HORGAN,M 503-07-0253P 04/22/01 REQD

BEAR,TEDDY 543-43-2233 08/10/01 CAT C ROSSIO WALK-IN 1/18/02

ROSSIO,DOM 706-09-1223P 10/02/01 CAT C

ROSSIO,MTEXPIRED 206-08-1422P 10/18/01 CAT A STEVE'S-1 11/30/01

ROSSIO 22 12/4/01

Example 2:

Means Test Expiration Report

Anniversary Date(s): 11/13/2001 - 11/13/2001

Printed: Nov 15, 2001@14:05:30 Page 1

Patient SSN MT Expired Status Future Appts

==============================================================================

\>\>No Means Test expirations for the selected date range.

# Appendix L – Flowchart of Search Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-1-106-local-signed-means-test-application-rossio-22-user-manual/002.png)

# Appendix M – Flowchart of Letters Option Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-1-106-local-signed-means-test-application-rossio-22-user-manual/003.png)

# Appendix N– Flowchart of Process of Making an Appointment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-1-106-local-signed-means-test-application-rossio-22-user-manual/004.png)

# Appendix O – FAQ (Desk Reference)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: Will appointment blocking have an impact on CPRS? If so, what is that impact?

A: There is no impact on CPRS. While you can create a NEW VISIT in CPRS, there is not a place to make an appointment.

Q: Will the patch work in PCE?

A: From within the PCE Appointment List View, when Check Out Interview for an appointment encounter is selected, it will check for a MT block. The decision was made not to make major modifications to PCE.

Q: Does this replace the MT letter we currently send out? The letter thatautomatically prints now also includes all copays.

A: No. This is a completely different letter and basically acts as a reminder letter to the veteran.

Q: Are these letters automatically loaded into the computer system and generated?

A: Letter generation is not a 100% system automated activity. There are options to both prepare and print the jobs.

Q: Can telephone triage schedule an appointment if the veteran is MT status required?

A: If they are scheduling a regular appointment, then no.

Q: Will a pre-printed 10-10EZ accompany the letters?

A: No. Sites must manually stuff envelopes with the Form 10-10EZ.

Q: What type of documentation will be accompanying the release of this software?

A: Along with the FAQ, sites will also receive a User Manual and a Technical Manual.

Q: Is there an easy way to understand the requirements for appointment blocking and the generation of letters?

A: Yes, we have developed flowcharts that allow you to follow an example through and see why an appointment was blocked or why a letter was (or wasn’t) printed.

Q: Where does the header information come from for the letters?

A: The software looks at the Institution File and pulls the name and address from the Site’s record. The First line is retrieved from the Official VA Name, Field \#100. If this field is empty, a default of VA MEDICAL CENTER is used. Street Address 1, and optionally Street Address 2 (if populated), are printed along with the City, State, and Zip as entered in the facility’s Institution file. The Institution used is determined by a standard API call which returns the current Primary Facility.

Q: Can I send output to something other than an actual printer?

A: Yes. The output can be directed to any device that is defined in the Site’s device file.

Q: Should I send out Zero-Day letters right at the beginning since they won’t have received either a 60-day or 30-day letter?

A: If you have been communicating with veterans about an upcoming MT anniversary, you might choose to use the Zero-Day letter; if not, it may not be appropriate due to the wording and reference to “previous requests.” Also, when the software is installed, a date is set and the system starts counting down from that point forward to issue 60-day and 30-day letters. You may choose to wait until the system has completed a full ‘cycle’ before using the Zero-Day letters. Mailing these letters is, of course, a site-by-site decision.

Q: What do I need to do in order to print reminder letters at multiple locations or in a multi-divisional site?

> A: After the patches are installed, you’ll need to do two things. First, enter all of the locations in the Parameter file installed as part of the patch. Second, specify a print device for each of the locations entered into the Parameter file. See specific details on accomplishing this in the EAS MT Parameters Entry/Edit section of the Local Signed Means Test Application User Manual. Without the print device, the letters will be lost.

Q: After a print job is complete, I still see letters flagged for printing. What causes this and what does it mean?

> A: If certain required veteran information fields are blank (street, city, state or zip), the software sends a mailman message that it cannot print this letter. As soon as the field is complete, the letter will print in the next job.

Q: The system shows that it’s printed letters, but I can’t find all of them. What’s up?

> A: It appears that when the letters are printed to a network printer that is not spooled or does not have a large enough buffer, some letters are ”lost" because the letters are simply coming faster than the print device can print them. When the buffer is full, incoming letters are ignored until the buffer is able to accept new incoming data. A spooled network printer is required to print these letters. If you are using such a printer and the letters are still failing to print, check the device setup in the Device file. It has been determined that if Queuing, Field \#5.5, is set to FORCED, letters will not print correctly, but they will be displayed as “Printed” in the status reports.

Q: Lots of veterans don’t complete a MT in advance and wait until they come in for their next appointment. If they do that, do they have to complete the MT before they can be seen?

A: Yes. One of the early adopters of this product customized their local software to display a message that read, “Send patient to see \_\_\_\_\_\_\_\_\_ in Room XXXX” to make sure the process went as smoothly as possible. You may want to look into a uniform approach at your facility as well. Remember that once this software is loaded, you absolutely will not be able to check-in a veteran who is in MT Status Required.

Q: Is there an override key?

A: Yes, there is an override key. The key can only be used for making appointments, not for check-in/out. MT is still required!

Q: How far back does the system go for MT?

A: 365 days

Q: How will appointment blocking affect clinic cancellations?

A: Clinic cancellations are not affected.

Q: Does the letter look to see if the veteran has an appointment to update MT?

A: No. The letter is more of a reminder, and the software doesn’t look at appointments. There is an area of the letter that you can customize, and you might want to create something to encourage MT update appointments.

Q: Is there a check for the last facility that did a MT, or will the veteran get multiple letters from multiple facilities?

A: If a veteran has been seen in facilities that are not integrated, there is a real possibility that multiple letters will go out to that veteran. Of course, this situation will change in the future with HEC managing centralized means testing.

Q: Does the software just ignore Cat C veterans?

A: There are a series of tests to determine letter recipients. For example, we look at deceased status and last MT – is it required or expiring within 60 days. You can also manually flag patients so that they never get a letter. Currently, a Cat C veteran with a MT date after Oct 5, 1999, and with the Agreed to Pay Deductible answered “Yes” will be ignored for the purposes of the MT blocking.

Q: Will I be blocked from making C&P appointments?

> A: No, only Regular type appointments are affected since a veteran does not have to be means tested for the C&P exam.

Q: How do I process an urgent walk-in patient who required a MT and is unable to do one at the time?

> A: A walk-in patient may be <u>checked-out</u> using the Check-in/Unsched Visit option. A warning message will be displayed reminding you to enter Check-Out (CO) at the Appointment Check In or Check Out prompt. Make sure you answer “CO”. Process the check-out as you would any other appointment.

Q: Diagnosis and CPT codes could be pertinent clinical information -- how do I input them if I’m blocked from doing a check-out on a patient that isn’t available to do an MT?

> A: As a result of the decision that no major modifications would be made to the Patient Care Encounter (PCE) software, it is possible to use the Update Encounter option on the PCE Encounter list to update DX and CPT information for an existing appointment.

  
Q: Are there exceptions for scheduling appointments for veterans that require a MT?

> A: There are no exceptions; however, an override key is available for selected users that will allow the booking of appointments for these veterans. This key has no effect on check-in/out actions. If you feel you need this key, contact your local MT or Enrollment Coordinator.

Q: Will CPRS allow check-out data to be entered (CPT, ICD, provider, etc.) if a MT isrequired?

> A: CPRS does not currently support Appointment Management or Scheduling activities. As indicated in a question above, certain encounter information may be entered through Patient Care Encounter hooks between CPRS and PCE.

Q: How are the return address and patient address formatted?

> A: Both addresses are formatted to meet the standardized address as specified in Postal Addressing Standards, Pub 28, November 2000, section 21. The delivery address is formatted to display in a 9 ½ by 4-inch window envelope.

> Q: What happens with a veteran that hasn’t been seen in quite some time, for example, 18 months?

> A: In situations like this one, the software doesn’t trigger until the appointment is made. So the veteran can check-in but can’t check-out until a MT is completed.

# Appendix P – FAQ (Post-Release Field Call Edition – May 2002)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: Is it possible to order business reply envelopes that we don’t have to fold and stuff?

> A: A No. 9 business reply envelope should fit easily into the standard mail out envelopes.

Q: When do we use the Prohibit Flag?

> A: One use is to block out patients with no return address. The Prohibit Flag is accessed via the EAS MT Parameters Menu and requires the Supervisor Key (Prohibit MT Letters, add/edit allows you to turn the Prohibit Flag on or off.).

Q: If a veteran file is marked with the Prohibit Flag for the 60-day letter, must that veteran also be marked for the 30- and 0-day letters?

> A: No. Once the flag is set, it is set for all communications with that veteran from the MT software.

Q: When entering a future means test, the system doesn’t allow entry of a future date.

A: You enter today’s date, and the system handles all future dates.

Q: How does the future MT patch work?

A: As an example, let’s use an August anniversary date: The veteran completes a MT and you enter that using today’s date. Information is transmitted to the HEC for calculation and update. If the submitted MT improves the veteran’s status, it becomes effective immediately. If the submitted MT maintains or downgrades the veteran’s status, it is held (by the system) and not activated until the anniversary date. Either way, this is all handled by the software and requires no manual intervention.

Q: We entered a future MT and the anniversary date passed. Now we seem to have two MTs on file for this veteran. Is this right?

> A: The system maintains the information entered for the future MT with the original date of entry. You may not edit this information; however, it is available to you as a history file.

Q: When do you use complete vs. add for a MT?

A: *Complete* = a new test, first test or past anniversary date

*Add* = updating within the anniversary year

> **NOTE:** If MT not required, use Add not Complete.

Q: If there’s a 15-month lag, what do you do? For example, a veteran completed a MT in January ’01 and now it’s March ’02…..

A: This would require a *Complete* since the test is outside the anniversary period.

Q: What if a patient refuses to complete a MT and then needs emergency care?

> A: A veteran that refuses MT is considered ineligible. Emergency care will be rendered as humanitarian aid and billed at the full rate!

Q: When a MT is done at another facility, how does it affect us? What if it needs a correction?

> A: When a MT is completed at another facility, the HEC system shares this information. If you need a correction to a MT completed at another facility, you must call that facility. You can only edit a MT if you are the primary facility; otherwise, you really can’t touch it and must contact the other facility.

Q: We’ve been using the Class III software. Can we continue to use the Class III and use the national release at the same time?

> A: Yes, you may. The two systems have no interaction. You may choose to run the Class III until your last 0-day letters are out.

Q: When do you print the 30-day letters? We ran the 60-day, and it shows the exact same number in the 30-day queue.

> A: Even though all of the letters may queue up, no letter will print until it reaches its threshold – that date which makes it valid.

Q: We ran the background job this morning with the 60-day option. No letters printed!

> A: Make sure that your flags are set at: Print to Printer=YES, Allow Queuing=NO. You must also verify that you are printing to a spooled printer, or the letters fill the buffer too quickly, and the result is no printing.

Q: If a PSA calls me and needs override, do I have to make the appointment rather than the PSA?

> A: EAS MT Override Key allows anyone with that key to make an appointment; however, it still cannot be checked out until the MT is updated.

Q: Does the software store which appointments were made using the override key?

A: No. There is currently no way to track appointments made with the override key.

Q: How are things affected if the HEC rejects a MT?

> A: If the MT is completed, you can then make appointments as well as check-in and out. The only time this will be affected by a HEC rejection is if you go back to edit that appointment.

Q: What happens if the MT expires after the appointment, but before the check-out is entered into the system (a check-out clearly wasn’t handled properly)?

A: You’ll need to go through PCE to update the encounter.

Q: If we show a veteran as Cat A and another facility shows that veteran as Cat C, does Cat C override?

> A: Not necessarily. It is driven by date and primary facility. This is another example of a situation where sites must work together – the HEC cannot resolve this for you.

Q: If we choose to run the letter print jobs interactively, how often should those be run?

A: Software developers recommend running the interactive jobs at least every two (2) days.

Q: How can we avoid a situation where lack of MT becomes a hindrance to care?

> A: There are three main options: 1) use the MT Override Key; and 2) check out as an unscheduled appointment – it must also be unscheduled at the front end, or 3) in an emergency situation, you can check the patient in to get the system ready to process necessary labs, x-rays, etc.

Q: What about a patient who comes in and all is in order, then at midnight they become MT required. What’s the solution?

> A: First and foremost, get the MT! Hopefully, facilities are working up patients before their appointment. In any case, we must be aware of when a patient is set to be MT required.

Q: Is there a report that will support forward planning on our part?

> A: Yes. By selecting the MT Expiration Report, you can enter a date or date range to generate a report of MT tagged to expire.

Q: What happens when a clinic is cancelled and a patient is MT required?

> A: The only way to continue to make appointments for a MT required patient is to use the auto-rebook feature.

Q: Will patients continue to get letters until they update their MT?

A: No. A patient will receive a maximum of three letters – 60-, 30-, and 0-day.

Q: How do we get patient names off of the “Unreturned Letter Stat Report?”

> A: Marking a patient file with the Prohibit Flag will remove that patient from the “Unreturned Letter Stat Report.”

Q: Our system is generating letters on our ZZ (test) patients. How can we stop this?

A: You must set the Prohibit Flag for each of your ZZ patients.

Q: When should we see the override key message when making an appointment?

A: The only time the override message displays is after you set a *regular* appointment.

Q: Should we not print/mail letters for those veterans that don’t have upcoming appointments?

> A: Letters should be printed for ALL VETERANS with expiring MTs. The critical path for this effort is the status of a veteran’s eligibility, and that requires a current MT.

Q: We have veterans who receive care in several states. Won’t their primary facility handle the mail-out of those letters?

> A: All veterans in your system with a valid address should receive MT letters from your facility. In the long run, it’s better that veterans receive too many letters than none at all. The value of this service to the veteran outweighs the postage and material costs.

Q: If we ask a veteran to come in and complete a MT, aren’t we going to get into problems with travel?

> A: The letters should go out with a VA Form 10-10EZ and business return envelope so that the veteran can complete the MT and mail it back to you. Certainly, if you’re making an appointment for the MT completion, you are at risk of beneficiary travel.

Q: When a future MT is entered and determined to benefit the veteran, it becomes effective immediately. Is that date now the new anniversary date?

> A: Yes, when the new MT is determined to be beneficial to the veteran, the effective date (date entered into the system) becomes the new MT anniversary date.

# # Appendix Q – FAQ (Post-Release – Patch EAS\*1\*15 – Aug. 2002)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: What happens when you use…REGISTER?

> A: If the REGISTER A PATIENT option is used, it triggers a “real time” Financial and Enrollment/Eligibility query to upload information from the HEC during the actual registration process. It will also schedule a full data transmission on that veteran to be sent during the nightly IVM BACKGROUND JOB.

LOAD/EDIT?

> A: If the LOAD/EDIT option is used, the financial query will be triggered only IF financial data is required. A full data transmission will only be sent IF certain fields are edited.

Q: What about veterans with temporary addresses?

> A: If a temporary address is active at the time the letters are generated, that address will be used as the mailing address for that veteran.

Q: How do we handle test patients to avoid printing false letters?

> A: When the Search for MT Anniversary Dates is run, any test patients found will be excluded from being added to the EAS MT Patient Status file.

Q: What does the software look for to identify a test patient?

> A: A test patient is defined as any patient with 5 leading zeros in their social security number (i.e., 000-00-123).

Q: Our 0-day letters have not been correctly setting Flag-to-Print. Has this been resolved?

> A: EAS\*1\*15 corrects this flagging issue. You may also choose to use a post-installation routine that can be run from programmer mode to check for any 0-day letters to update the flag-to-print field appropriately.

Q: What about the “undefined errors” that we’ve been getting?

> A: This patch fixes those occurring under the following conditions: when jumping from the Letters sub-menu to the DG LOAD/EDIT menu item and when answering NO to the ‘Add patient to the Patient Status File’ prompt when setting a letter prohibit flag.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Acronyms 23
Appendix A – Test Letter 24
Appendix B – 60 Day Letter 25
Appendix C – 40-Day Letter 26
Appendix D – Report of Contact Form 27
Appendix E – 0-Day Letter 28
Appendix F – Count of Pending Letters to be Printed 29
Appendix G – Auto-MT Letters Summary Report 30
Appendix H – Means Test Letters Statistics Report 31
Appendix I – Summary of Unreturned Means Test Letters 32
Appendix J – Means Test Expiration by Appt Date 33
Appendix K – Means Test Expiration Report 34
Appendix L – Flowchart of Search Process 35
Appendix M – Flowchart of Letters Option Process 36
Appendix N – Flowchart of Process of Making an Appointment 37
Appendix O – FAQ (Desk Reference) 38
Appendix P – FAQ (Post-Release Field Call Edition – May 2002) 42
Appendix Q – FAQ (Post-Release – Patch EAS\*1\*15 – Aug. 2002) 46
Appointment Blocking 22
Automated Means Test Letter Menu 3
Automated MT Letters Summary Report 12
C
Clear Letter Search In-Use Flag 21
Count of Pending Letters to be Printed 11
E
EAS MT Parameter Entry/Edit 16
EAS MT Parameter Menu 16
Edit Final Section of Letter 19
F
Functionality 1
G
Glossary 23
I
Index 47
Introduction 1
L
Letters Print Menu 6
M
Means Test Expiration Report 14
Means Test Letters Statistics Report 13
O
Overview 1
P
Print a Test Letter (EAS MT) 21
Print Report of Contact 10
Prohibit MT Letters Add/Edit 18
R
Related Manuals/Documentation 2
Report Menu 11
Reprint Letters by Processing Date 8
Reprint Single Letter 9
Revision History i
S
Search for MT Anniversary Dates Option 4
Sixty Day Letters Print 7
T
Table of Contents ii
Thirty Day Letters Print 8
U
Unreturned Letter Statistic Report 13
Using the Software 3
V
Veteran MT Return Edit Option 5
Z
Zero Day Letters Print 8
