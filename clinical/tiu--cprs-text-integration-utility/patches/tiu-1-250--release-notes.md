---
title: TIU*1*250 TIU Line Count Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: TIU Line Count
app_code: TIU
app_name: "CPRS: Text Integration Utility"
section: CLI
app_status: active
pkg_ns: TIU
patch_ver: 1
patch_id: TIU*1*250
group_key: "TIU:TIU:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
audience: 
keywords: 
  - class
  - span
  - line
  - transcription
  - report
  - count
  - document
  - anchor
  - upload
  - transcriptionist
page_count: 0
word_count: 3653
section_count: 0
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_1_250rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_1_250rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=65"
---

![](tiu-1-250-tiu-line-count-release-notes/001.png)

Text Integration Utilities (TIU) Line Count(TIU\*1\*250) Release Notes

June 2010

September 2010 Modifications

Office of Enterprise Development

Computerized Patient Record System Product Line

<span id="_Toc107371093" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>September 2010</td>
<td><a href="#Page_12"><u>13</u></a>, <a href="#Page_16"><u>16</u></a></td>
<td><blockquote>
<p>Modified text to conform with VA Handbook 6500, Information Security Program</p>
</blockquote></td>
<td><blockquote>
<p>T Downing</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>June 2010</td>
<td>All</td>
<td><blockquote>
<p>Initial Release</p>
</blockquote></td>
<td><blockquote>
<p>T Downing</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc272239484" class="anchor"></span>Table of Contents

<span id="_Toc198350348" class="anchor"></span>Preface

<span id="_Toc272239486" class="anchor"></span>Scope of Manual

This manual provides an introduction to TIU Line Count (patch TIU\*1\*250) and recommendations on how the line count can be used to measure productivity for both internal and outsourced transcription.

<span id="_Toc272239487" class="anchor"></span>Audience

Information in this manual is intended for Clinical Coordinators, Automated Data Processing Application Coordinators (ADPACs), and end users: clinicians, Health Information Management (HIM) Managers, Medical Record Technicians, Transcription Contracting Officer Technical Representatives (COTRs), and transcriptionists.

<span id="_Toc272239488" class="anchor"></span>Related Manuals

The following manuals are available on the VA Software Document Library ([<u>http://www.va.gov/vdl/</u>).](http://www.va.gov/vdl/).)

> *Text Integration Utilities (TIU) Technical Manual*

> *Text Integration Utilities (TIU) Clinical Coordinator User Manual*

> *Text Integration Utilities (TIU) Generic HL7 Interface Handbook*

<span id="_Toc272239489" class="anchor"></span>Introduction

<span id="_Toc272239490" class="anchor"></span>Purpose of Text Integration Utilities Line Count

The purpose of the Text Integration Utilities (TIU) Line Count program is to provide a management tool for VA sites to determine the number of transcribed lines produced in all TIU document types, whether they be transcribed by VA staff transcriptionists or by contract transcription companies. Accurate line counts are used to:

- Validate billed transcription invoices and prevent overbilling by transcription services,
- Calculate the number of transcriptionists needed to assure accurate, rapid turnaround of dictated documents, and
- Quantitatively describe the total output of HIM transcription within a specified time frame.

A major limitation of this application is that anything stored outside of TIU—Radiology, C & P, and Medicine Procedure Reports depending on how Automated Medical Information Exchange (AMIE) and Clinical Procedures are implemented—is not counted by this utility. This limitation can be minimized by taking full advantage of the text integration capabilities of TIU.

<span id="_Toc272239491" class="anchor"></span>Background

In response to Inspector General (OIG) report No. 04-00018-155, *Audit of the Veterans Health Administration’s Acquisition of Medical Transcription Services* (Jun 2006), Veterans Health Administration (VHA) issued VHA DIRECTIVE 2008-042, PROVISIONS REQUIRED IN ALL MEDICAL TRANSCRIPTION CONTRACTS (August 7, 2008). This patch, TIU\*1\*250 TIU Line Count, fulfills the requirements of these two documents.

OIG report No. 04-00018-155 is available on the Internet at [<u>http://www.va.gov/oig/publications/reports-list.asp?year=2006</u>](http://www.va.gov/oig/publications/reports-list.asp?year=2006).

VHA DIRECTIVE 2008-042 is available on the Internet at [<u>http://www1.va.gov/vhapublications/publications.cfm?pub=1&order=desc&orderby=title</u>](http://www1.va.gov/vhapublications/publications.cfm?pub=1&order=desc&orderby=title)

Changes in this patch do not affect the existing line count functionality. It is anticipated that, as the VA converts to the new line count standards in transcription contracts, the present functionality will eventually be phased out. The legacy line count allows the site to specify the number of characters per line in a site parameter (defaulting to 60 characters per line) and counts a string of white space as one single character.

<span id="_Toc272239492" class="anchor"></span>What the OIG Says about Line Count

Inspector General (OIG) report No. 04-00018-155, *Audit of the Veterans Health Administration’s Acquisition of Medical Transcription Services* (Jun 2006) found overbilling by contract transcription services in the tens of thousands of dollars. Inconsistency in the way contract line counts were made and verified, including criminal misconduct, were cited in the report.

<span id="_Toc272239493" class="anchor"></span>What the VHA Directive Says

VHA DIRECTIVE 2008-042, PROVISIONS REQUIRED IN ALL MEDICAL TRANSCRIPTION CONTRACTS lays out the following specifications:

(Note: The following two paragraphs and figure are directly quoted from VHA DIRECTIVE 2008-042.)

1)  Visible Black Character. A Visible Black Character is defined strike-able and visible characters and includes any printed letter, number, symbol, and/or punctuation mark excluding any or all formatting (e.g., bold, underline, italics, table structure, formatting codes). All visible black characters can be seen with the naked eye as a mark, regardless of whether viewed electronically or on a printed page.

![](tiu-1-250-tiu-line-count-release-notes/002.png)

2)  Visual Black Character (VBC) Line or ASCII no Spaces Line. A VBC Line is defined as the total number of characters you can see with the naked eye, divided by 65. It includes any character contained within a header or footer. Spaces, carriage returns, and hidden format instructions, such as bold, underline, text boxes, printer configurations, spell check, etc., which are not counted in the total character count. A VBC Line is calculated by counting all visual characters and simply dividing the total number of characters by 65 to arrive at the number of defined lines.

<span id="OurInterpretation" class="anchor"></span>Our Interpretation

The table and guidance in this directive are based on AHIMA Foundation’s white paper: *A Standard Unit of Measure for Transcribed Reports* (available at: [<u>http://perspectives.ahima.org/index.php?option=com_content&view=category&id=57&Itemid=109</u>](http://perspectives.ahima.org/index.php?option=com_content&view=category&id=57&Itemid=109)). In formulating our own approach to Visible Black Character (VBC) counting, we have drawn from industry experience with this standard.

In order to facilitate auditing of transcription bills, we have created a report that lists the information needed for such an audit.

The table of VBC given in VHA DIRECTIVE 2008-042 is used by the program in determining what is a VBC. This table has an error that we have corrected in the coded routine: That is, there are two upper-case Ks. We replace the second upper-case K with a lower case k.

Many characters in common use, such as so-called smart quotes (“”) and apostrophes (‘’) used in many text entry programs, are excluded from the AHIMA specification and ignored by TIU\*1\*250. These are not consistently represented in computer systems and character sets. A work-around for transcriptionists is to turn off the use of smart quotes in their programs. (The way to turn off the feature varies even among Microsoft Word<sup>®</sup> versions, so to find out how to do this consult the tool's online help or user manual.)

| Note:                                             | Transcriptionists should turn off the use of smart quotes in the text entry program they are using. Additionally, transcriptionists with non-standard keyboards should avoid characters that are not in the VHA DIRECTIVE 2008-042 table. |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-250-tiu-line-count-release-notes/003.png) |                                                                                                                                                                                                                                           |

Most other characters that are not in the table have the same problem. Specifically, transcriptionist with non-standard keyboards should avoid characters that are not in the table. Transcriptionists should especially avoid character forms such as é, ü, and ñ because the software ignores these as well.

<span id="_Toc272239495" class="anchor"></span>TIU\*1\*250 Patch

The patch includes:

- Code to implement the Visible Black Character (VBC) Line Count as defined in VHA DIRECTIVE 2008-042.
- A new field in the TIU DOCUMENT FILE \[#8925\] to record the VBC Line Count for each document.
- Addition of the VBC Line Count to the Detailed Display views of TIU documents when it applies.
- A parameter for specifying a User Class of people for whom a VBC is reported.
- A Transcription Billing Verification Report that lists and summarizes VBC Line Counts for transcribed documents.

<span id="_Toc272239496" class="anchor"></span>Line Count Code

After this patch is installed, line counts conforming to VHA DIRECTIVE 2008-042 are made on each transcription entered.

There are four ways to enter transcribed documents into TIU:

1.  Transcriptionist menu entry option \[TIU MAIN MENU TRANSCRIPTION\]
2.  Background transcription upload utility \[TIU UPLOAD MENU\]
3.  CPRS Notes tab
4.  The Generic HL7 Interface

If the person entering the note is different from the author or expected cosigner, then the note is considered to be a transcription and a VBC Line Count is recorded. Additionally, if the site specifies a User Class in the parameter TIU USER CLASS FOR VBC, and the person who entered the document is a member of this User Class, a VBC Line Count for the document is reported in the Transcription Billing verification report.

The optional parameter, TIU USER CLASS FOR VBC, was implemented in response to large numbers of cases where a person whose work was not included in a transcription bill had entered documents in behalf of another person (e.g., secretaries, students, etc.), in addition to cases where documents were generated by automated processes (e.g., iMed Consent, etc.).

This VBC Line Count is saved in the TIU DOCUMENT FILE \[#8925\].

<span id="_Toc272239497" class="anchor"></span>TIU DOCUMENT FILE \[#8925\]

Patch TIU\*1\*250 adds a field and cross-reference to the TIU DOCUMENT FILE \[#8925\]. The field records the VBC Line Count as defined above. The cross-reference, VBC, by Entry Date/Time, is used to optimize reporting of VBC Line Counts by date range.

| Caution:                                          | If a transcribed document has not gone through the release process or is stored outside of TIU, there is no line count recorded. Documents that may miss the regular release process include: Radiology Notes, Anatomic Pathology Notes, Compensation and Pension (C & P) Notes, and Medicine Notes. |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-250-tiu-line-count-release-notes/004.png) |                                                                                                                                                                                                                                                                                                      |

<span id="_Toc272239498" class="anchor"></span>Addition of the Visible Black Character Line Count to Note Headers

If TIU has identified a released document as being a transcription, it adds the Visible Black Character (VBC) line count to the displayed header. This takes slightly different forms in different presentations. Presented here is an example of a header from an upload running in foreground:

K E R M I T U P L O A D

Now start a KERMIT send from your system.

Starting \[REMOTE\] KERMIT receive.

Done with \[REMOTE\] receive, File transfer was successful. (4523 bytes)

Bytes: 4523 Sec: 23 cps: 196.7

File Transfer Complete--Now Filing Records...

\>\>\> HEADER IDENTIFIED:

\$HDR: DISCHARGE SUMMARY

SOCIAL SECURITY NUMBER: 666-22-9999

DATE OF ADMISSION: APR 28, 1994

DICTATED BY: CPRSPHYSICIAN,ONE

DICTATION DATE: 09/17/2009

ATTENDING PHYSICIAN: CPRSPHYSICIAN,ONE

URGENCY: PRIORITY

TRANSCRIPTIONIST: CPRSCLERK,NINETY SEVEN

\$TXT

\>\>\> Document Filed Successfully.

LINES TYPED: 64

VBC LINES: 55.91

Discharge Summary Released.

TOTALS FOR CURRENT BATCH:

TOTAL Document(s) RECEIVED: 1

Document(s) NOT FILED: 0

Document(s) FILED with MISSING FIELDS: 0

Press RETURN to continue...

Below is an example of VBC Line Count from the Detailed Display view on the Notes tab in CPRS:

![](tiu-1-250-tiu-line-count-release-notes/005.png)

  
<span id="_Toc272239499" class="anchor"></span>TIU USER CLASS FOR VBC Parameter

This patch will work without filling in this parameter. The software compares the TRANSCRIPTIONIST ID and DICTATED BY field. If these two fields are different, and they are both present in the Upload Header, then a VBC is calculated and recorded. You will learn quickly that the accuracy of any reports generated from this data depends on the accuracy of the transcriptionist identification.

If the parameter is set to identify a specific user class, then only the work produced by members of that class will be included in the Transcription Billing Verification Report. The VBC line count will still be calculated and recorded for non-members of the class, but their work will be omitted from the report. This is to allow for cases where you inadvertently delay including a person in the User Class whose work will be billed. If you recognize such a case, and add the person to the User Class, subsequent reprints of the report for the same time period will include their work.

| Note: ![](tiu-1-250-tiu-line-count-release-notes/006.png) | If you choose to leave this parameter blank, you should still follow the directions in the [<u>TIU Upload Header</u>](#TIUUploadHeader) section below. |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|

This parameter identifies a locally defined User Class for transcriptionists. Using this parameter requires three things:

1.  You must set up and populate a TIU User Class for transcriptionists.
2.  You must check and correct each TIU upload header to identify the Author and Entered By.
3.  You must use XPAR to assign the transcriptionist User Class to the TIU USER CLASS FOR VBC parameter.

<span id="_Toc272239500" class="anchor"></span>Transcriptionist User Class

In the event that your Transcription Billing Verification Report includes a large number of cases where the documents entered by non-transcriptionists (i.e., persons whose work will never result in a bill), then implementing the User Class for VBC, and populating it with the appropriate people should help to improve the accuracy of your report.

Since the TIU USER CLASS FOR VBC parameter can be set up on either the Division or the System level, and there are so many different organizational structures within the VA, we did not include a User Class to meet this requirement. You must set one up to conform to your own local requirements. You must populate this User Class with transcriptionists for your organization.

<span id="Page_12" class="anchor"></span>  
All transcriptionists must have a New Person File \[#200\] entry because this patch keeps track of transcribed notes through a pointer to this file. This should not pose a problem because contract transcriptionists are not be VA employees—there are many contractors working for any medical center who also have VistA accounts. High turnover among transcriptionists should likewise not be a problem—handle transcriptionist turnover in a manner similar to that used for interns and other training positions.

| Note:                                             | According to VA Handbook 6500, Information Security Program, the use of shared or generic accounts in VA computer systems is prohibited. You must have a unique entry for each transcriptionist. |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-250-tiu-line-count-release-notes/007.png) |                                                                                                                                                                                                  |

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Reminder:</th>
<th rowspan="2"><p>Uploaded transcriptions can be linked to <em>inactive</em> New Person File entries, thus establishing an extra layer of security. An entry can be set to inactive by:</p>
<ul>
<li><p>Set the DISUSER field to YES.</p></li>
</ul></th>
</tr>
<tr class="odd">
<th>![](tiu-1-250-tiu-line-count-release-notes/008.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A simple work-around in the New Person File makes the Transcription Billing Verification Report more effective. That is to make the initials for each transcriptionist match the initials of the contracted company. The report sorts entries by the New Person File INITIALS field.

<span id="_Toc272239501" class="anchor"></span>TIU <span id="TIUUploadHeader" class="anchor"></span>Upload Header

This patch requires two fields in the TIU Upload Header to be filled in and accurate. They are: TRANSCRIPTIONIST ID (field \#1302) and DICTATED BY (field \#1202). Most upload headers already have DICTATED BY because this field is used by the electronic signature routines to determine who should sign the note. However, TRANSCRIPTIONIST ID is not consistently implemented.

You must be sure that the TIU upload header for each document type your vendor(s) transcribed includes the AUTHOR and ENTERED BY fields (the captions that coincide with these fields may be DICTATED BY and TRANSCRIPTIONIST, etc. as long as your vendor uses the captions you've specified in the Upload set-up.)

The following example checks the local definition of PROGRESS NOTE to make sure it still fulfills our minimum requirements:

1.  Using the TIU IRM MAINTENANCE MENU, choose the TIU Parameters Menu:

   1      TIU Parameters Menu ...

   2      Document Definitions (Manager) ...

   3      User Class Management ...

   4      TIU Template Mgmt Functions ...

   5      TIU Alert Tools

   7      TIUHL7 Message Manager

          Title Mapping Utilities ...

   6      Active Title Cleanup Report

\<CPM\> Select TIU Maintenance Menu Option: 1  TIU Parameters Menu

2.  Choose Modify Upload Parameters:

   1      Basic TIU Parameters

   2      Modify Upload Parameters

   3      Document Parameter Edit

   4      Progress Notes Batch Print Locations

   5      Division - Progress Notes Print Params

\<CPM\> Select TIU Parameters Menu Option: 2  Modify Upload Parameters

3.  Return past the Institution-wide parameters (e.g., source, protocol, format, header signal, etc.), and at the DOCUMENT DEFINITION prompt, choose PROGRESS NOTES, then continue pressing \<Enter\> until you get to the CAPTION prompt, and type “AUTHOR”:

First edit Institution-wide upload parameters:

Select INSTITUTION: MEMPHIS

ASCII UPLOAD SOURCE: remote computer// \<Enter\>

UPLOAD PROTOCOL: KERMIT// \<Enter\>

UPLOAD HEADER FORMAT: captioned// \<Enter\>

RECORD HEADER SIGNAL: \$HDR// \<Enter\>

BEGIN REPORT TEXT SIGNAL: \$TXT// \<Enter\>

RUN UPLOAD FILER IN FOREGROUND: YES// \<Enter\>

Now Select upload error alert recipients:

Select ALERT RECIPIENT: CPRSCLERK,TWO// \<Enter\>

Now edit the DOCUMENT DEFINITION file:

DOCUMENT DEFINITION: PROGRESS NOTES       CLASS 

         ...OK? Yes// \<Enter\>  (Yes)

ABBREVIATION: PN// \<Enter\>

LAYGO ALLOWED: YES// \<Enter\>

UPLOAD TARGET FILE: TIU DOCUMENT// \<Enter\>

Select TARGET TEXT FIELD: REPORT TEXT// \<Enter\> 

UPLOAD LOOK-UP METHOD: D LOOKUP^TIUPUTPN// \<Enter\>

UPLOAD POST-FILING CODE: D FOLLOWUP^TIUPUTPN(TIUREC("#"))

           Replace \<Enter\>

UPLOAD FILING ERROR CODE: D GETPN^TIUCHLP// \<Enter\>

Select CAPTION: NAME// AUTHOR

4.  Check that the Author Caption is mapped to field 1202 and that REQUIRED FIELD is set to YES:

Select CAPTION: NAME// AUTHOR

  CAPTION: AUTHOR// \<Enter\>

  ITEM NAME: DICTATING PROVIDER// \<Enter\>

  FIELD NUMBER: 1202// \<Enter\>

  LOOKUP LOCAL VARIABLE NAME: \<Enter\>

  TRANSFORM CODE: \<Enter\>

  EXAMPLE ENTRY: WELBY,MARCUS// \<Enter\>

  CLINICIAN MUST DICTATE: YES// \<Enter\>

  REQUIRED FIELD?: YES// \<Enter\>

Select CAPTION:

5.  At the Select CAPTION: prompt, choose TRANSCRIBER, and check the values of each of the fields (in particular, the FIELD NUMBER should be set to 1302, and REQUIRED FIELD set to YES):

Select CAPTION: TRANSCRIBER 

  CAPTION: TRANSCRIBER// \<Enter\>

  ITEM NAME: TRANSCRIBER// \<Enter\>

  FIELD NUMBER: 1302// \<Enter\>

  LOOKUP LOCAL VARIABLE NAME: \<Enter\>

  TRANSFORM CODE: \<Enter\>

  EXAMPLE ENTRY: MEDTRAN// \<Enter\>

  CLINICIAN MUST DICTATE: NO// \<Enter\>

  REQUIRED FIELD?: NO// Y \<Enter\>

  Select CAPTION: \<Enter\>
6.  Check the header. It should look something like this:

The header for the Progress Notes CLASS is now defined as:

\$HDR: PROGRESS NOTES

TITLE: ORTHOPEDICS NOTE

SSN: 555-12-4444

VISIT/EVENT DATE: 06/03/2010@13:00

AUTHOR: CPRSPROVIDER,SEVEN

TRANSCRIBER: MEDTRAN

DATE/TIME OF DICT: 06/04/2010@08:15

LOCATION: MEMPHIS ORTHOPEDIC CLINIC

NAME: CPRSPROVIDER,NINE

\$TXT

  PROGRESS NOTES Text

\*\*\* File should be ASCII with width no greater than 80 columns.

\*\*\* Use "@@@" for "BLANKS" (word or phrase in dictation that isn't understood).

DOCUMENT DEFINITION:

7.  Be sure that your Transcription Vendor knows the header format that you’re expecting, and that they understand that the captions and data types which they’re sending need to be *identical* to what you’re set up to receive. You may need to exchange e-mails, or have the vendor exchange samples with you several times, to work out any differences. If they have many transcribers who work from home etc., they may need to make special efforts to communicate any changes with their remote staff.

<span id="_Toc272239502" class="anchor"></span>TIU USER CLASS FOR VBC

The sole purpose of the TIU USER CLASS FOR VBC is to improve the accuracy of your Transcription Billing Verification Report. If you decide to implement this, use the option XPAR EDIT PARAMETER to identify the User Class for which VBC Line Counts will be reported. Note that you can set the parameter at either the System or Division level, in the event that you'd like to identify different User Classes to accommodate different needs at Multi-divisional facilities.

User Class inheritance can be used to your advantage to tailor the behavior of the report to meet your site's needs. For example if Contract Transcriptionist is set up as a sub-class of Transcriptionist, all members of the sub-class are recognized as members of the parent class.

<span id="_Toc272239503" class="anchor"></span>Transcription Billing Verification Report

This report can be run by division and provide information on all transcriptionists or one or more selected transcriptionist. It reports based on an entered date range. Since the VBC Line Count is only calculated for uploaded reports, it does not report on any document uploaded before the patch was installed.

The accuracy of this report depends on the accuracy of the data. Specifically, it depends on whether transcriptionists are reliably recorded in the header of each document.

| Note: ![](tiu-1-250-tiu-line-count-release-notes/009.png) | If you choose to use this report, you must follow the directions in the [<u>TIU Upload Header</u>](#TIUUploadHeader) section above to insure that each uploaded document has the needed data. |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="Page_16" class="anchor"></span>A simple work-around in the New Person File makes the Transcription Billing Verification Report more effective. That is to make the initials for each transcriptionist match the initials of the contracted company. The report sorts entries by the New Person File INITIALS field. So in our test system we have entered two transcriptionists with the initials ATI to stand for Ascott Transcription Incorporated. This makes all entries by either transcriptionist come out under a single heading in the report

This example is a complete report for all facilities on the local VistA system for the month of August:

                          --- MIS Managers Menu ---

   1      Individual Patient Document

   2      Multiple Patient Documents

   3      Print Document Menu ...

   4      Search for Selected Documents

   5      Statistical Reports ...

   6      Unsigned/Uncosigned Report

   7      Missing Text Report

   8      Missing Text Cleanup

   9      Signed/unsigned PN report and update

   10     UNKNOWN Addenda Cleanup

   11     Missing Expected Cosigner Report

   12     Mark Document as 'Signed by Surrogate'

   13     Mismatched ID Notes

   14     TIU 215 ANALYSIS ...

   15     Transcription Billing Verification Report

\<CPM\> Select Text Integration Utilities (MIS Manager) Option: 15  Transcription Billing Verification Report

              --- Transcription Billing Verification Report ---

Select division: ALL// \<Enter\>

Specific Transcriptionist(s)? NO// Y YES

Select Transcriptionist(s):

1\) ATI

1 ATI CPRSTRANSCRIPTIONIST,FIVE ATI

TRANSCRIPTIST

2 ATI CPRSTRANSCRIPTIONIST,ONE ATI TRANSCRIPTIST

CHOOSE 1-2: 1 CPRSTRANSCRIPTIONIST,FIVE ATI

TRANSCRIPTION SERVICE

2\) ATI CPRSTRANSCRIPTIONIST,ONE ATI TRANSCRIPTIST

3\) \<Enter\>

Print Summary Page Only? NO// \<Enter\>

Start Transcription Date \[Time\]: Jan 01, 2010// 1/1/09  (JAN 01, 2009)

Ending Transcription Date \[Time\]: Jan 31, 2010@23:59// \<Enter\>  (JAN 31, 2010@23:59)

DEVICE: HOME// \<Enter\>  TELNET PORT

                                                                          Page 1

================================================================================

T R A N S C R I P T I O N B I L L I N G R E P O R T

CAMP MASTER

for Documents Transcribed: 01/01/2009 to 09/03/2010 Printed: 09/03/2010 10:22

Tran Date Title Patient Aut VBC Lines

================================================================================

ati 07/23/09 Discharge Summary EIGHTY,INPATIENT (0880) JER 55.91

07/23/09 Discharge Summary BCMA,FIFTEEN-PATIEN (0015) JER 57.31

07/31/09 Discharge Summary BCMA,ELEVEN-PATIENT (0011) JER 56.25

07/31/09 Discharge Summary BCMA,ONE-PATIENT (0001) JER 56.31

----------

Total for Transcriber ati = 225.78

----------

Total for Division = 225.78

Press RETURN to continue or '^' to exit: \<Enter\>

Page 2

================================================================================

T R A N S C R I P T I O N B I L L I N G R E P O R T

SUMMARY for ZZ ALBANY-PRRTP

for Documents Transcribed: 01/01/2009 to 09/03/2010 Printed: 09/03/2010 10:22

================================================================================

Category Documents VBC Lines

================================================================================

Division Totals

CAMP MASTER 4 225.78

Transcriber Totals

ati 4 225.78

Station Totals

ZZ ALBANY-PRRTP 4 225.78

Press RETURN to continue or '^' to exit: \<Enter\>

<span id="_Toc272239504" class="anchor"></span>Future Requested Work

> <span id="_Toc272239505" class="anchor"></span>Radiology

Requirements Analysis & Engineering Management New Service Request (NSR) number 20100206: Update Radiology Line Count Software.

> The OIG has already made formal recommendation for action to VA for us to validate work that we are paying for from contractors. The TIU line counting software is in the process of being updated to meet this requirement, however, the radiology package was also found to have line counting software and does not produce accurate information per VHA Directive 2008-042, Provisions Required for all Medical Transcription Contracts.