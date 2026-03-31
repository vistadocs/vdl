---
title: PXRM*2*37 Caregiver Support Program Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Caregiver Support Program
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*37
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - colspan
  - blockquote
  - strong
  - style
  - width
  - table
  - caregiver
  - even
  - assessment
page_count: 0
word_count: 4808
section_count: 5
table_count: 37
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: October 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_37_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_37_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-37-caregiver-support-program-installation-guide/001.png)

> Caregiver Support Program

> PXRM\*2.0\*37

> Reminder Dialogs Installation Guide October 2015

[Changing Print Name to Follow Local Naming Convention](#_bookmark7) 16

[Associating the Reminder Dialogs with the Note Titles](#associating-the-reminder-dialogs-with-the-note-titles) 20

[Appendix A: Installation Example 26](#_bookmark9)

[Appendix B: Health Factors in each Reminder Dialog 29](#appendix-b-health-factors-in-each-reminder-dialog)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [The first release of these templates supporting the Caregiver Support Program (CSP) occurred in Spring and Fall 2011.](#the-first-release-of-these-templates-supporting-the-caregiver-support-program-csp-occurred-in-spring-and-fall-2011)
- [In response to feedback from Caregiver Support Coordinators, providers and others in the field regarding the CSP’s In-Home Assessment process, adjustments and modifications were made to improve the overall process, including these template changes.](#in-response-to-feedback-from-caregiver-support-coordinators-providers-and-others-in-the-field-regarding-the-csps-in-home-assessment-process-adjustments-and-modifications-were-made-to-improve-the-overall-process-including-these-template-changes)
- [We would like to thank the following sites for their participation in the testing of these templates:](#we-would-like-to-thank-the-following-sites-for-their-participation-in-the-testing-of-these-templates)
- [New Mexico VA HCS (Albuquerque) Alexandria HCS](#new-mexico-va-hcs-albuquerque-alexandria-hcs)
- [Amarillo VA HCS Butler VAMC](#amarillo-va-hcs-butler-vamc)
- [VA Eastern Kansas HCS](#va-eastern-kansas-hcs)
- [Michael E. DeBakey VAMC (Houston) Clement J. Zablocki VAMC (Milwaukee) VA Pittsburgh HCS](#michael-e-debakey-vamc-houston-clement-j-zablocki-vamc-milwaukee-va-pittsburgh-hcs)
- [VA St Louis HCS](#va-st-louis-hcs)
- [Southern Arizona VA HCS (Tucson)](#southern-arizona-va-hcs-tucson)
    - [After installation of this patch, you will find a total of eight reminder dialogs in your system.](#after-installation-of-this-patch-you-will-find-a-total-of-eight-reminder-dialogs-in-your-system)
  - [Creating Three New DOCUMENT DEFINITIONS for the Other Parent Notes](#creating-three-new-document-definitions-for-the-other-parent-notes)
  - [Associating the Reminder Dialogs with the Note Titles](#associating-the-reminder-dialogs-with-the-note-titles)
  - [Installing PXRM 2\0\37](#installing-pxrm-2037)
  - [APPENDIX B: Health Factors in each Reminder Dialog](#appendix-b-health-factors-in-each-reminder-dialog)

# The first release of these templates supporting the Caregiver Support Program (CSP) occurred in Spring and Fall 2011.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# In response to feedback from Caregiver Support Coordinators, providers and others in the field regarding the CSP’s In-Home Assessment process, adjustments and modifications were made to improve the overall process, including these template changes.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# We would like to thank the following sites for their participation in the testing of these templates:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# New Mexico VA HCS (Albuquerque) Alexandria HCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Amarillo VA HCS Butler VAMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# VA Eastern Kansas HCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Michael E. DeBakey VAMC (Houston) Clement J. Zablocki VAMC (Milwaukee) VA Pittsburgh HCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# VA St Louis HCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Southern Arizona VA HCS (Tucson)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### After installation of this patch, you will find a total of eight reminder dialogs in your system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### These dialogs are named as follows:

| VA-CSP | INITIAL | IN-HOME                          | ASSESSMENT | REV        |
|--------|---------|----------------------------------|------------|------------|
| VA-CSP | INITIAL | IN-HOME                          | ASSESSMENT | CHILD NOTE |
| VA-CSP | INTERIM | IN-HOME                          | ASSESSMENT | REV        |
| VA-CSP | INTERIM | IN-HOME                          | ASSESSMENT | CHILD NOTE |
| VA-CSP | ANNUAL  | IN-HOME ASSESSMENT REV           |            |            |
| VA-CSP | ANNUAL  | IN-HOME ASSESSMENT CHILD NOTE    |            |            |
| VA-CSP | 90 DAY  | MONITORING ASSESSMENT            |            |            |
| VA-CSP | 90 DAY  | MONITORING ASSESSMENT CHILD NOTE |            |            |

> <span id="_bookmark1" class="anchor"></span>Making the Dialogs Viewable in CPRS

#### From the Reminders Manager Menu:

> Select Reminder Managers Menu Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allowed as Templates may be set for the following:

| 1   | User     | USR | \[choose | from NEW PERSON\]      |
|-----|----------|-----|----------|------------------------|
| 3   | Service  | SRV | \[choose | from SERVICE/SECTION\] |
| 4   | Division | DIV | \[choose | from INSTITUTION\]     |

> 5 System SYS \[NORTH-FLORIDA.MED.VA.GOV\] Enter selection: 5 System NORTH-FLORIDA.MED.VA.GOV

> Setting Reminder Dialogs allowed as Templates

> for System: NORTH-FLORIDA.MED.VA.GOV

> Select Display Sequence: ?

> 150 MEDICINE PROGRESS NOTE ATTENDING

> 170 PATIENT DISCHARGE INSTRUCTIONS

> 180 TIU512 NAD ADMISSION/VITALS

> 190 TIU512 NAD PAIN

> 200 TIU512 NAD FUNCTIONAL

> 210 TIU512 NAD NUTRITION

> 220 TIU512 NAD SLP

#### When you type a question mark above, you will see the list of \#’s and dialogs that are already taken. Choose a number NOT on this list.

> For this example, looking above I see the number 160 is not in the list, so I will use 160.

> Select Display Sequence: 160

> Are you adding 160 as a new Display Sequence? Yes// Y YES Display Sequence: 160// (hit enter) 160

> Clinical Reminder Dialog: VA-CSP INITIAL IN-HOME ASSESSMENT REV reminder dialog LOCAL

> ...OK? Yes// (hit enter) (Yes)

> Select Display Sequence:

#### It takes you back to this prompt, at which point you can add the rest until you have sequenced all eight dialogs.

> Next, you will be setting up the note titles, which includes the use of Interdisciplinary Notes.

> <span id="_bookmark2" class="anchor"></span>Background on Interdisciplinary Notes Interdisciplinary Notes

> Interdisciplinary Notes are a feature of Text Integration Utilities (TIU) for expressing notes from different care givers as a single episode of care. They always start with a single note by the initial contact person (e.g., triage nurse, attending) and continue with separate notes created and signed by other providers and attached to the original note.

> The Parent Note

> You start any interdisciplinary note with a parent note. A parent is a note title that includes an ASU (Authorization/Subscription Utility) rule allowing attachments. Your facility should have set up these titles with unique names that allow you to easily identify them.

> Only certain members of your team should start Interdisciplinary Notes. To establish a parent note for a patient and a specific episode of care, all they do is create a note with the proper title, and sign it.

> The Child Note(s)

> *Continue an interdisciplinary note by attaching one or more child notes to the parent note. The intention is for each child note to be by a different provider involved in this episode of care. Again your facility has established a number of notes with unique titles to act as child notes.*

#### Above information taken from page 55 of the [<u>TIU Coordinator & User Manual</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuum-275.pdf)

> Side note about use of Interdisciplinary Notes:

#### While the parent notes will be entered by several disciplines, the child notes will be entered into CPRS only by the Caregiver Support Coordinators (CSCs). We understand this functionality may be unfamiliar for some sites. If this process is new to you and/or your facility, you will want to familiarize yourself with the process for attaching a child note to the parent note, in case end-users have questions related to this.

> Information related to entering and maintaining Parent/Child Interdisciplinary Notes can be found on pages 42-48 of the [<u>TIU Coordinator & User Manual</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuum.pdf).

> We also are providing the CSCs detailed guidance for this.

> <span id="_bookmark3" class="anchor"></span>Note Titles

> \* Comprehensive information on Creating Document Definitions and Moving Definitions from one Document Class to another can be found beginning on page 51 of the [<u>TIU/ASU Implementation Guide</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuim.pdf)

> With the eight dialogs, one note title is needed for each.

> *All note titles are to be mapped to the following VHA Enterprise Standard Title:*

#### CAREGIVER CERTIFICATE

> \*\*All of the templates are to be used as parent/child notes.

> The following gives instructions for each of the note titles assuming the existence of a parent document class and a child document class. If your site utilizes a different process for setting up Interdisciplinary notes (i.e. business rules), please disregard these instructions and *follow your established guidelines for setting up Interdisciplinary documents*. In the end, you will have 4 parent notes and 4 child notes.

1)  The following title should already exist and only needs to be modified to parent status: CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT
2)  The three \*new\*parent note titles that need to be created are: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT CAREGIVER PROGRAM ANNUAL IN-HOME MONITORING ASSESSMENT CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT
3)  The four \*new\*child note titles that need to be created are: CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM ANNUAL IN-HOME ASSESSMENT CHILD NOTE

> CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT CHILD NOTE

1.  <span id="_bookmark4" class="anchor"></span>Moving the Initial In-Home Assessment Note to the Parent Document Class

> \*\*Please note: Moving note titles from one document class to another can be taxing on system resources. If this note title has been used frequently at your facility, we advise you wait until the end of the day or other NON-PEAK usage times to move it, as this process may significantly affect your system’s performance.

> To move the existing note title to the parent document class, you will need to edit the Document Definition.

> From the TIU CLINICAL COORDINATOR MENU:

> USR User Class Management ...

> Document Definitions (Manager) ... Progress Notes Print Options ...

> Progress Notes/Discharge Summary \[TIU\] ... Text Integration Utilities (MIS Manager) ... Text Integration Utilities (MRT) ...

> Text Integration Utilities (Remote User) ... Text Integration Utilities (Transcriptionist) ... TIU Maintenance Menu ...

> Select TIU CLINICAL COORDINATOR MENU Option: DOCument Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) Option: 1 Edit Document Definitions.......

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Edit Document Definitions</strong></th>
<th><blockquote>
<p>Jul</p>
</blockquote></th>
<th>08, 2013@10:49:20</th>
<th colspan="2"><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>of</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>BASICS</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Name</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>Type</td>
</tr>
<tr class="odd">
<td colspan="2">1 CLINICAL DOCUMENTS</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>CL</td>
</tr>
<tr class="even">
<td colspan="2">2 +PROGRESS NOTES</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>CL</td>
</tr>
<tr class="odd">
<td colspan="2">3 +ADDENDUM</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>DC</td>
</tr>
<tr class="even">
<td colspan="2">4 +DISCHARGE SUMMARY</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>CL</td>
</tr>
<tr class="odd">
<td colspan="2">5 +CLINICAL PROCEDURES</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>CL</td>
</tr>
<tr class="even">
<td colspan="2">6 +LR LABORATORY REPORTS</td>
<td></td>
<td></td>
<td colspan="3"></td>
<td>CL</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>?Help &gt;ScrollRight PS/PL</p>
</blockquote></td>
<td>PrintScrn/List</td>
<td>+/-</td>
<td colspan="3">&gt;&gt;&gt;</td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 34%" />
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Expand/Collapse</th>
<th><blockquote>
<p>Detailed Display/Edit</p>
</blockquote></th>
<th>Items: Seq Mnem</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Jump to Document Def</td>
<td><blockquote>
<p>Status...</p>
</blockquote></td>
<td><blockquote>
<p>Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Boilerplate Text</td>
<td><blockquote>
<p>Name/Owner/PrintName...</p>
</blockquote></td>
<td>Copy/Move</td>
</tr>
</tbody>
</table>

> Select Action: Quit// J Jump to Document Def

> Select TIU DOCUMENT DEFINITION NAME: CAREGIVER PROGRAM INI

1.  CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT TITLE Std Title: CAREGIVER CERTIFICATE
2.  CAREGIVER PROGRAM INITIAL IN-HOME NOTE OBJECT

> CHOOSE 1-2: 1 CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT TITLE

> Std Title: CAREGIVER CERTIFICATE.......................................

> .............................................................................

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Edit</strong></th>
<th><strong>Document Definitions</strong></th>
<th colspan="2">Jul 08, 2013@10:49:46 Page:</th>
<th>5</th>
<th>of</th>
<th>6</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BASICS</p>
</blockquote></td>
<td></td>
<td></td>
<td>Type</td>
</tr>
<tr class="even">
<td>59</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">INITIAL IN-HOME ASSESSMENT</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>60</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">INTERIM IN-HOME ASSESSMENT</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>61</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">DISCONTINUED FOR CAUSE</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>62</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">ASSESSMENT AND APPLICATION PART II</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>63</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">MENTAL HEALTH IN-HOME ASSESSMENT</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>64</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">SUPPORT NOTE</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>65</td>
<td>CAREGIVER PROGRAM</td>
<td colspan="2">VETERAN'S ELIGIBILITY ASSESSMENT</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>66</td>
<td><blockquote>
<p>TBI NOTE</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td colspan="3">67 TBI SECOND LEVEL EVALUATION</td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td colspan="3">68 +SECURE MESSAGING DOCUMENTS</td>
<td></td>
<td colspan="3">DC</td>
</tr>
<tr class="even">
<td colspan="3">69 +ANTICOAGULATION</td>
<td></td>
<td colspan="3">DC</td>
</tr>
<tr class="odd">
<td colspan="3">70 +OEF</td>
<td></td>
<td colspan="3">DC</td>
</tr>
<tr class="even">
<td colspan="3">71 +STUDENT NOTES</td>
<td></td>
<td colspan="3">DC</td>
</tr>
<tr class="odd">
<td colspan="3"><p>72 +TBI/POLYTRAUMA DOCUMENTS</p>
<p>+ ?Help &gt;ScrollRight PS/PL PrintScrn/List</p></td>
<td>+/-</td>
<td colspan="3"><blockquote>
<p>DC</p>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Jump to Document Def Status...</p>
<p>Boilerplate Text Name/Owner/PrintName...</p>
</blockquote>
<p>Select Action: Next Screen// <strong>COP</strong> Copy/Move</p></td>
<td><blockquote>
<p>Delete Copy/Move</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
</tbody>
</table>

> Select Copy/Move Action: (MT/MD/C/U): MT// MOVE TITLE (hit enter)

> WARNING: This action affects inheritance and can CHANGE DOCUMENT BEHAVIOR.

> It DISREGARDS ownership. It may take awhile if the Title has many documents. Please use caution and DON'T TOUCH entries you are not responsible for.

> Press RETURN to continue or '^' or '^^' to exit:

> Select Title to Move: (59-72): 59

> Selecting target Document Class. Enter '??' for a list of selectable ones. You may not select PRF Flag Document Classes or Document Classes outside the original Class.

> Select TIU DOCUMENT CLASS NAME to Move Title to: INTERDIS

1.  INTERDISC CHILD DOCUMENT DOCUMENT CLASS
2.  INTERDISC PARENT DOCUMENT DOCUMENT CLASS

> CHOOSE 1-2: 2 INTERDISC PARENT DOCUMENT DOCUMENT CLASS

#### (be careful to choose your facility’s PARENT document class for this note, not the CHILD)

> ........................................................................

> ...Title Inactivated, Moved to INTERDISC PARENT DOCUMENT.

> Processing documents that use this Title.........................

> Done. All documents updated for selected Title.

> Press RETURN to continue or '^' or '^^' to exit:

> Since the Title is in a new Document Class, it now inherits from a new parent wherever it lacks its own values, and its behavior may differ from before.

> It may also differ from its new siblings wherever it HAS its own values and siblings INHERIT them.

> Please check Title thoroughly before reactivating. Check Business Rules, TIU Document Parameters, and Document Definition attributes including Basic, Technical, and Upload fields.

#### Notice above that moving the document to a different class also inactivates the title, so we need to re-activate the title. Shown below:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 21%" />
<col style="width: 7%" />
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Edit</strong></th>
<th colspan="5"><strong>Document Definitions</strong> Jul 08, 2013@10:50:40 Page:</th>
<th>4</th>
<th>of</th>
<th>7</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+</td>
<td colspan="5"><blockquote>
<p>BASICS</p>
<p>Name</p>
</blockquote></td>
<td></td>
<td></td>
<td>Type</td>
</tr>
<tr class="even">
<td>46</td>
<td colspan="5">CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>47</td>
<td colspan="5"><blockquote>
<p>DCFS 3008 PHYSICIAN TEAM NOTE</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>48</td>
<td colspan="5"><blockquote>
<p>GEC EXTENDED CARE REFERRAL</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>49</td>
<td colspan="5"><blockquote>
<p>INTERDISCIPLI</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>50</td>
<td colspan="5"><blockquote>
<p>INTERDISCIPLINARY PLAN OF CARE</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>51</td>
<td colspan="5"><blockquote>
<p>TEAM INTERDISCIPLINARY PLAN</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>52</td>
<td colspan="5"><blockquote>
<p>TEAM PREADMISSION NUR &amp; ANESTHESIA SCREEN &amp; ASSESS</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>53</td>
<td colspan="5"><blockquote>
<p>TEAM PREANESTHESIA NURSING SCREEN &amp; ASSESSMENT</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>54</td>
<td colspan="5"><blockquote>
<p>TEAM SOCIAL WORK DCFS 3008</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>55</td>
<td colspan="5"><blockquote>
<p>+TEST TITLES</p>
</blockquote></td>
<td></td>
<td></td>
<td>DC</td>
</tr>
<tr class="even">
<td>56</td>
<td colspan="5"><blockquote>
<p>+OPHTHALMOLOGY</p>
</blockquote></td>
<td></td>
<td></td>
<td>DC</td>
</tr>
<tr class="odd">
<td><p>57</p>
<p>+</p></td>
<td colspan="5"><blockquote>
<p>+PATIENT RECORD FLAG CAT I</p>
<p>?Help &gt;ScrollRight PS/PLPrintScrn/List +/-</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote>
<p>&gt;&gt;&gt;</p></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Expand/Collapse Jump to Document</p>
</blockquote></td>
<td>Def</td>
<td><blockquote>
<p>Detailed Display/Edit Status...</p>
</blockquote></td>
<td>Items: Delete</td>
<td>Seq</td>
<td>Mnem</td>
<td colspan="2">MenuTxt</td>
</tr>
</tbody>
</table>

> Boilerplate Text Name/Owner/PrintName. Copy/Move

> Select Action: Quit// ST Status...

> Select STATUS: (A/I/T): A

> Selecting Entries for Status ACTIVE. You may enter multiple entries at the same time.

> Select Entry(s): (46-59): 46

> Editing Status for Entry 46 ... Entry Activated. Entry and any (nonShared) Components Activated

## Creating Three New DOCUMENT DEFINITIONS for the Other Parent Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The following three note titles will need to be *created* as PARENT documents: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT CAREGIVER PROGRAM ANNUAL IN-HOME MONITORING ASSESSMENT

> CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT

> From the TIU CLINICAL COORDINATOR MENU: DOCument Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) Option: 3 Create Document Definitions.......

> Create Document Definitions Jul 08, 2013@11:42:27 Page: 1 of 1

> BASICS

> Name Type

#### CLINICAL DOCUMENTS CL

1.  PROGRESS NOTES CL
2.  ADDENDUM DC
3.  DISCHARGE SUMMARY CL
4.  CLINICAL PROCEDURES CL
5.  LR LABORATORY REPORTS CL
6.  SURGICAL REPORTS CL

> New Users, Please Enter '?NEW' for Help \>\>\> (Title) Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Level// Next Level (hit enter)

> Select CLINICAL DOCUMENTS Item (Line 2-7): 2................................

#### Once you are in the PROGRESS NOTES class, you will want to hit enter and go to the next screen until you get to your facility’s PARENT document class. At our facility, this is \#44 below.

> Then type NEXT LEVEL and type in the number for the PARENT document class. See below:

> Create Document Definitions Jul 08, 2013@11:42:38 Page: 3 of 5

> BASICS

> \+ Name Type

37. MULTI-DISCIPLINE/MULTI-USE DC
38. OCCUPATIONAL HEALTH NOTES DC
39. EMPLOYEE TB SKIN TEST DC
40. RESEARCH DC
41. HISTORY AND PHYSICAL DC
42. GI PROCEDURES DC
43. INTERDISC CHILD DOCUMENT DC
44. INTERDISC PARENT DOCUMENT DC
45. TEST TITLES DC
46. OPHTHALMOLOGY DC
47. PATIENT RECORD FLAG CAT I DC
48. PATIENT RECORD FLAG CAT II DC
49. IFC NOTE TITLES/TEMPLATES DC
50. WRII DC

> \+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> Class/DocumentClass Next Level Detailed Display/Edit

> (Title) Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Screen// NEXT L Next Level

> Select PROGRESS NOTES Item (Line 3-62): 44..................................

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 79%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Create</strong></th>
<th><strong>Document Definitions</strong> Jul 08, 2013@11:42:52 Page:</th>
<th>1</th>
<th>of</th>
<th>4</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BASICS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>+</td>
<td>Name</td>
<td></td>
<td></td>
<td>Type</td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></td>
<td></td>
<td></td>
<td>CL</td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p><strong>INTERDISC PARENT DOCUMENT</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td>DC</td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>DCFS 3008 PHYSICIAN TEAM NOTE (T)</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>GEC EXTENDED CARE REFERRAL</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>INTERDISCIPLI</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>INTERDISCIPLINARY PLAN OF CARE</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>TEAM INTERDISCIPLINARY PLAN</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>TEAM PREADMISSION NUR &amp; ANESTHESIA SCREEN &amp; ASSESS (T)</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>TEAM PREANESTHESIA NURSING SCREEN &amp; ASSESSMENT (T)</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>11</td>
<td><blockquote>
<p>TEAM SOCIAL WORK DCFS 3008 (T)</p>
</blockquote></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
</tbody>
</table>

> ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> (Class/DocumentClass) Next Level Detailed Display/Edit

> Title Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Screen// TI Title

> Enter the Name of a new INTERDISC PARENT DOCUMENT: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT

> CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR (hit enter)

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

> Direct Mapping to Enterprise Standard Title...

> Your LOCAL Title is: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT

> **NOTE:** Only ACTIVE Titles may be selected...

> Select VHA ENTERPRISE STANDARD TITLE: CAREGIVER CERTIFICATE

I found a match of: CAREGIVER CERTIFICATE

> ... OK? Yes// YES (hit enter)

> Ready to map LOCAL Title: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT to

> VHA Enterprise Standard Title: CAREGIVER CERTIFICATE.

> ... OK? Yes// YES (hit enter)

> Done.

> STATUS: (A/I/T): INACTIVE// A ACTIVE Entry Activated. SEQUENCE: (hit enter)

> MENU TEXT: Caregiver Program An Replace Caregiver... With CP Interim In-Home

> Replace

> CP Interim In-Home

#### (if needed, you can edit MENU TEXT above according to your facility’s policies)

> Entry Created

> If you wish, you may enter another INTERDISC PARENT DOCUMENT:

#### At the prompt above, you will create the next parent note document definition. As indicated above, you will create a total of three parent notes.

1.  <span id="_bookmark6" class="anchor"></span>Creating Four New DOCUMENT DEFINITIONS for the Child Notes

> From the TIU CLINICAL COORDINATOR MENU: DOCument Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) Option: 3 Create Document Definitions.......

> Create Document Definitions Jul 08, 2013@11:42:27 Page: 1 of 1

> BASICS

> Name Type

#### CLINICAL DOCUMENTS CL

1.  PROGRESS NOTES CL
2.  ADDENDUM DC
3.  DISCHARGE SUMMARY CL
4.  CLINICAL PROCEDURES CL
5.  LR LABORATORY REPORTS CL
6.  SURGICAL REPORTS CL

> New Users, Please Enter '?NEW' for Help \>\>\> (Title) Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Level// Next Level (hit enter)

> Select CLINICAL DOCUMENTS Item (Line 2-7): 2................................

#### Once you are in the PROGRESS NOTES class, you will want to hit enter and go to the next screen until you get to your facility’s CHILD document class. At our facility, this is \#43 below.

> Then type NEXT LEVEL and type in the number for the CHILD document class. See below:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 34%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><strong>Create Document Definitions</strong></th>
<th>Jul 08, 2013@11:42:38</th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th>of</th>
<th>5</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BASICS</p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td>+</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="4">Type</td>
</tr>
<tr class="odd">
<td>37</td>
<td></td>
<td colspan="2">MULTI-DISCIPLINE/MULTI-USE</td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>38</td>
<td></td>
<td colspan="2">OCCUPATIONAL HEALTH NOTES</td>
<td colspan="4">DC</td>
</tr>
<tr class="odd">
<td>39</td>
<td></td>
<td colspan="2">EMPLOYEE TB SKIN TEST</td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>40</td>
<td></td>
<td colspan="2">RESEARCH</td>
<td colspan="4">DC</td>
</tr>
<tr class="odd">
<td>41</td>
<td></td>
<td colspan="2">HISTORY AND PHYSICAL</td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>42</td>
<td></td>
<td colspan="2">GI PROCEDURES</td>
<td colspan="4">DC</td>
</tr>
<tr class="odd">
<td>43</td>
<td></td>
<td colspan="2">INTERDISC CHILD DOCUMENT</td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>44</td>
<td></td>
<td colspan="2">INTERDISC PARENT DOCUMENT</td>
<td colspan="4">DC</td>
</tr>
<tr class="odd">
<td>45</td>
<td></td>
<td colspan="2">TEST TITLES</td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>46</td>
<td></td>
<td colspan="2">OPHTHALMOLOGY</td>
<td colspan="4">DC</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>47</th>
<th><blockquote>
<p>PATIENT RECORD FLAG CAT I</p>
</blockquote></th>
<th></th>
<th></th>
<th>DC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>48</td>
<td><blockquote>
<p>PATIENT RECORD FLAG CAT II</p>
</blockquote></td>
<td></td>
<td></td>
<td>DC</td>
</tr>
<tr class="even">
<td>49</td>
<td><blockquote>
<p>IFC NOTE TITLES/TEMPLATES</p>
</blockquote></td>
<td></td>
<td></td>
<td>DC</td>
</tr>
<tr class="odd">
<td><p>50</p>
<p>+</p></td>
<td><blockquote>
<p>WRII</p>
<p>?Help &gt;ScrollRight PS/PL</p>
</blockquote></td>
<td>PrintScrn/List</td>
<td>+/-</td>
<td><blockquote>
<p>DC</p>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Class/DocumentClass Next Level Detailed Display/Edit

> (Title) Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Screen// NEXT L Next Level

> Select PROGRESS NOTES Item (Line 3-62): 43..................................

> Create Document Definitions Jul 08, 2013@11:42:52 Page: 1 of 4

> BASICS

> \+ Name Type

2.  PROGRESS NOTES CL

#### INTERDISC CHILD DOCUMENT DC

3.  DCFS 3008 NURS TEAM NOTE TL
4.  DCFS 3008 OT/SPEECH/RT TEAM NOTE TL
5.  DCFS 3008 PT TEAM NOTE TL
6.  DCFS 3008 SOCIAL WORK TEAM NOTE TL
7.  DCFS 3008 SPEECH TEAM NOTE TL
8.  GEC REFERRAL CARE COORDINATION 4 TL
9.  GEC REFERRAL CARE RECOMMENDATIONS PROVIDER 3 TL
10. GEC REFERRAL NURSING 2 TL
11. GEC REFERRAL SOCIAL SERVICES TL
12. NURS CARE PLAN: ACTIVITY INTOLERANCE (T) TL
13. NURS CARE PLAN: ANXIETY (T) TL
14. NURS CARE PLAN: ASPIRATION RISK (T) TL

> \+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> (Class/DocumentClass) Next Level Detailed Display/Edit

> Title Restart Status...

> (Component) Boilerplate Text Delete Select Action: Next Screen// TI Title

> Enter the Name of a new INTERDISC CHILD DOCUMENT: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR (hit enter)

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

> Direct Mapping to Enterprise Standard Title...

> Your LOCAL Title is: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> NOTE: Only ACTIVE Titles may be selected...

> Select VHA ENTERPRISE STANDARD TITLE: CAREGIVER CERTIFICATE

> I found a match of: CAREGIVER CERTIFICATE

> ... OK? Yes// YES (hit enter)

> Ready to map LOCAL Title: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE to

> VHA Enterprise Standard Title: CAREGIVER CERTIFICATE.

> ... OK? Yes// YES (hit enter)

> Done.

> STATUS: (A/I/T): INACTIVE// A ACTIVE Entry Activated. SEQUENCE: (hit enter)

> MENU TEXT: Caregiver Program In Replace Caregiver... With CP Interim Child

> Replace

> CP Interim Child

#### (if needed, you can edit MENU TEXT above according to your facility’s policies)

> Entry Created

> If you wish, you may enter another INTERDISC CHILD DOCUMENT:

#### At the prompt above, you can create the next child note document definition. A total of four child notes need to be created:

> CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM ANNUAL IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT CHILD NOTE

> <span id="_bookmark7" class="anchor"></span>Changing Print Name to Follow Local Naming Convention

> We understand many sites utilize existing naming conventions for document definitions, including Interdisciplinary notes. Facilities with these guidelines already in place are allowed to continue using local naming conventions.

> Although the NAME field for each title must remain as indicated in this document, sites may modify the Print Name of each title to follow local policy. This is done by editing the note title after it has been created.

#### If your site wishes to modify the Print Name, instructions are below (using the Interim Child Note as the example).

> First, the title must be in inactive status.

> This can be done through the Edit Document Definitions option.

> From the TIU CLINICAL COORDINATOR MENU: DOCument Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) Option: 1 Edit Document Definitions......

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 4%" />
<col style="width: 27%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Edit Document Definitions</strong></th>
<th>Oct</th>
<th>13, 2015@11:38:51</th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>of</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>BASICS</p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td colspan="2"></td>
<td colspan="4">Type</td>
</tr>
<tr class="odd">
<td>1 CLINICAL DOCUMENTS</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
<tr class="even">
<td>2 +PROGRESS NOTES</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
<tr class="odd">
<td>3 +ADDENDUM</td>
<td colspan="2"></td>
<td colspan="4">DC</td>
</tr>
<tr class="even">
<td>4 +DISCHARGE SUMMARY</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
<tr class="odd">
<td>5 +CLINICAL PROCEDURES</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
<tr class="even">
<td>6 +LR LABORATORY REPORTS</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
<tr class="odd">
<td>7 +SURGICAL REPORTS</td>
<td colspan="2"></td>
<td colspan="4">CL</td>
</tr>
</tbody>
</table>

> ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> Expand/Collapse Detailed Display/Edit Items: Seq Mnem MenuTxt Jump to Document Def Status... Delete

> Boilerplate Text Name/Owner/PrintName... Copy/Move Select Action: Quit// J Jump to Document Def

> Select TIU DOCUMENT DEFINITION NAME: CAREGIVER PROGRAM INTERIM

1.  CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT TITLE Std Title: CAREGIVER CERTIFICATE
2.  CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE TITLE Std Title: CAREGIVER CERTIFICATE
3.  CAREGIVER PROGRAM INTERIM IN-HOME NOTE OBJECT

> CHOOSE 1-3: 2 CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE TITLE

> Std Title: CAREGIVER CERTIFICATE.......................................

> .............................................................................

> .............................................................................

> Edit Document Definitions Oct 13, 2015@11:39:10 Page: 4 of 9

> BASICS

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 44%" />
<col style="width: 10%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>+</th>
<th>Name</th>
<th></th>
<th colspan="2"></th>
<th></th>
<th></th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>44</td>
<td></td>
<td>CAREGIVER PROGRAM INTERIM IN-HOME</td>
<td colspan="2">ASSESSMENT</td>
<td>CHILD</td>
<td>NOTE</td>
<td>TL</td>
</tr>
<tr class="even">
<td>45</td>
<td></td>
<td>DCFS 3008 NURSE TEAM NOTE</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>46</td>
<td></td>
<td>DCFS 3008 OT/SPEECH/RT TEAM NOTE</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>47</td>
<td></td>
<td>DCFS 3008 PT TEAM NOTE</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>48</td>
<td></td>
<td>DCFS 3008 SOCIAL WORK TEAM NOTE</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>49</td>
<td></td>
<td>DCFS 3008 SPEECH TEAM NOTE</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>50</td>
<td></td>
<td>GEC REFERRAL CARE COORDINATION 4</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>51</td>
<td></td>
<td>GEC REFERRAL CARE RECOMMENDATIONS</td>
<td colspan="2">PROVIDER 3</td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>52</td>
<td></td>
<td>GEC REFERRAL NURSING 2</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="even">
<td>53</td>
<td></td>
<td>GEC REFERRAL SOCIAL SERVICES</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td><p>+</p>
<p>Select</p></td>
<td colspan="3">?Help &gt;ScrollRight PS/PL PrintScrn/List STATUS: (A/I/T): <strong>I</strong> INACTIVE</td>
<td colspan="2">+/-</td>
<td colspan="2">&gt;&gt;&gt;</td>
</tr>
</tbody>
</table>

> Selecting Entry for Status INACTIVE. Please select ONE entry. You will be prompted for another.

> Select Entry: (44-57): 44

> Entry (& any nonShared Components) Inactivated

> Selecting Another Entry for Status INACTIVE:

> Select Entry: (44-57): (hit enter)

#### Next, you will go to the detailed display of the note to view and change the print name.

> Edit Document Definitions Oct 13, 2015@11:39:32 Page: 4 of 9

> BASICS

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>+</th>
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>44</td>
<td></td>
<td>CAREGIVER</td>
<td>PROGRAM INTERIM IN-HOME</td>
<td>ASSESSMENT</td>
<td>CHILD</td>
<td>NOTE</td>
<td>TL</td>
</tr>
<tr class="even">
<td>45</td>
<td></td>
<td>DCFS 3008</td>
<td>NURSE TEAM NOTE</td>
<td></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
<tr class="odd">
<td>46</td>
<td></td>
<td>DCFS 3008</td>
<td>OT/SPEECH/RT TEAM NOTE</td>
<td></td>
<td></td>
<td></td>
<td>TL</td>
</tr>
</tbody>
</table>

47. DCFS 3008 PT TEAM NOTE TL
48. DCFS 3008 SOCIAL WORK TEAM NOTE TL
49. DCFS 3008 SPEECH TEAM NOTE TL
50. GEC REFERRAL CARE COORDINATION 4 TL
51. GEC REFERRAL CARE RECOMMENDATIONS PROVIDER 3 TL
52. GEC REFERRAL NURSING 2 TL
53. GEC REFERRAL SOCIAL SERVICES TL

> \+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> Expand/Collapse Detailed Display/Edit Items: Seq Mnem MenuTxt Jump to Document Def Status... Delete

> Boilerplate Text Name/Owner/PrintName... Copy/Move Select Action: Next Screen// DET Detailed Display/Edit Select Entry: (44-57): 44

> Detailed Display Oct 13, 2015@11:39:49 Page: 1 of 3 Title CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> Basics Note: Values preceded by \* have been inherited

> Name: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> VHA Enterprise

> Standard Title: CAREGIVER CERTIFICATE Abbreviation:

> Print Name: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE Type: TITLE

> IFN: 3802

> National Standard: NO

> Status: INACTIVE

> Owner: CLINICAL COORDINATOR

> In Use: NO Suppress Visit

> Selection: NO

> \+ ? Help +, - Next, Previous Screen PS/PL Basics Technical Fields Find Items: Seq Mnem MenuTxt Edit Upload Quit Boilerplate Text Try

> Select Action: Next Screen// BAS Basics

> NAME: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> Replace (hit enter)

> ABBREVIATION: (hit enter)

> PRINT NAME: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE Replace ... With CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT (C)

> Replace (hit enter)

> CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT (C)

#### The Print Name above is the field where sites can alter the title to follow local nomenclature. In the example above, I chose to add (C) in place of the words CHILD NOTE. This will vary depending on local policy. After this, you can hit enter through the rest of the fields, re- activate the title, and return back to the Detailed Display.

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

> Direct Mapping to Enterprise Standard Title...

> Your LOCAL Title is: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> NOTE: Only ACTIVE Titles may be selected...

> The LOCAL Title: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> is already mapped to

> VHA Enterprise Title: CAREGIVER CERTIFICATE

> Do you want to RE-MAP it? NO// (hit enter)

> ... OK, No Harm Done!

> TYPE: (TL): TL// (hit enter) TITLE

> CLASS OWNER: CLINICAL COORDINATOR// (hit enter) CLINICAL COORDINATOR SUPPRESS VISIT SELECTION: NO// (hit enter)

> STATUS: (A/I/T): INACTIVE// A ACTIVE Entry Activated.

#### You will now see the Print Name reflects the changes made:

> Detailed Display Oct 13, 2015@11:42:21 Page: 1 of 3 Title CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> Basics Note: Values preceded by \* have been inherited

> Name: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE

> VHA Enterprise

> Standard Title: CAREGIVER CERTIFICATE Abbreviation:

> Print Name: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT (C) Type: TITLE

> IFN: 3802

> National Standard: NO

> Status: ACTIVE

> Owner: CLINICAL COORDINATOR

> In Use: NO Suppress Visit

> Selection: NO

> \+ ? Help +, - Next, Previous Screen PS/PL Basics Technical Fields Find Items: Seq Mnem MenuTxt Edit Upload Quit Boilerplate Text Try

> Select Action: Next Screen// Q Quit

## Associating the Reminder Dialogs with the Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### First, in Template Editor (CPRS) you will need to switch out the revised Initial In-Home Assessment Reminder Dialog in its corresponding note title.

> To do this, go into Template Editor, then to Document Titles, and find your current template that is linked to the note title.

> Below is our current set-up for the INITIAL In-Home Assessment:

![](pxrm-2-37-caregiver-support-program-installation-guide/002.png)

> As you see above, the current linked Reminder Dialog is: VA\*CG CAREGIVER INITIAL IN-HOME ASSESSMENT

> Switch this Reminder Dialog out with the new one: VA-CSP INITIAL IN-HOME ASSESSMENT REV

> ![](pxrm-2-37-caregiver-support-program-installation-guide/003.png)Make sure the Associated Title is still linked to the template, then Hit Apply.

|     |
|-----|

> Second, you will need to modify the Document Titles in Template Editor for two of the other parent notes. For this, you will be switching out the old Reminder Dialog for the new Reminder Dialog *as well as* associating the respective new Note Title.

> To do this, go into Document Titles and find your current template that is linked to the old note title.

> For this example, I will use the ANNUAL IN-HOME MONITORING ASSESSMENT note.

> Once you have found this template in Template Editor, on the right-hand side you will want to change out the old Reminder Dialog for the new Reminder Dialog and hit apply.

> OLD Reminder Dialog: VA\*CG CAREGIVER ANNUAL IN-HOME ASSESSMENT

> ![](pxrm-2-37-caregiver-support-program-installation-guide/004.png)*NEW Reminder Dialog*: VA-CSP ANNUAL IN-HOME ASSESSMENT REV

|     |
|-----|

#### After this is complete, you will need to disassociate the old Note Title for the new Note Title.

> To do this, position the cursor at the end of the “Associated Title” field and Backspace to beginning of the line. Then, type in the new title, ensuring you choose the correct one (the word MONITORING has been added to new title).

> OLD title: CAREGIVER PROGRAM ANNUAL IN-HOME ASSESSMENT

> ![](pxrm-2-37-caregiver-support-program-installation-guide/005.png)*NEW title*: CAREGIVER PROGRAM ANNUAL IN-HOME MONITORING ASSESSMENT

|     |
|-----|

> After ensuring the new Reminder Dialog is linked to the new Title, select Apply. You will then repeat this process for the INTERIM note.

> OLD Reminder Dialog: VA\*CG CAREGIVER INTERIM IN-HOME ASSESSMENT

> *NEW Reminder Dialog*: VA-CSP INTERIM IN-HOME ASSESSMENT REV OLD title: CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT

> *NEW title*: CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT

> Lastly, you will need to create the Document Titles in Template Editor to link the final parent note and all four child notes:

> CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT

> CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM ANNUAL IN-HOME ASSESSMENT CHILD NOTE CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT CHILD NOTE

> ![](pxrm-2-37-caregiver-support-program-installation-guide/006.png)To do this, go into Document Titles and select New Template (top right-hand corner).

|     |
|-----|

> Next, type in the Associated Title which, for this example, is CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT, and hit Apply:

![](pxrm-2-37-caregiver-support-program-installation-guide/007.png)

> You will follow this same process for each of the four child notes:

- Create a new template for each
- Type in the name of the appropriate Reminder Dialog
- Type in the appropriate Associated Title before hitting Apply

> After all parent and child templates have been linked to the appropriate note titles, you will need to inactivate all old titles and Reminder Dialogs.

> After this is complete, you are done setting up the Caregiver Program templates.

> Complete list of eight note titles with the respective Reminder Dialogs:

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 14%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>NOTE TITLE (NAME)</strong></th>
<th><p><strong>VHA ENTERPRISE</strong></p>
<p><strong>TITLE</strong></p></th>
<th><strong>REMINDER DIALOG NAME</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP INITIAL IN-HOME ASSESSMENT REV</strong></td>
</tr>
<tr class="even">
<td><strong>CAREGIVER PROGRAM INITIAL IN-HOME ASSESSMENT CHILD NOTE</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP INITIAL IN-HOME ASSESSMENT CHILD NOTE</strong></td>
</tr>
<tr class="odd">
<td><strong>CAREGIVER PROGRAM ANNUAL IN-HOME MONITORING ASSESSMENT</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP ANNUAL IN-HOME ASSESSMENT REV</strong></td>
</tr>
<tr class="even">
<td><strong>CAREGIVER PROGRAM ANNUAL IN-HOME ASSESSMENT CHILD NOTE</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP ANNUAL IN-HOME ASSESSMENT CHILD NOTE</strong></td>
</tr>
<tr class="odd">
<td><strong>CAREGIVER PROGRAM INTERIM IN-HOME MONITORING ASSESSMENT</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP INTERIM IN-HOME ASSESSMENT REV</strong></td>
</tr>
<tr class="even">
<td><strong>CAREGIVER PROGRAM INTERIM IN-HOME ASSESSMENT CHILD NOTE</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP INTERIM IN-HOME ASSESSMENT CHILD NOTE</strong></td>
</tr>
<tr class="odd">
<td><strong>CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP 90 DAY MONITORING ASSESSMENT</strong></td>
</tr>
<tr class="even">
<td><strong>CAREGIVER PROGRAM 90 DAY MONITORING ASSESSMENT CHILD NOTE</strong></td>
<td><strong>CAREGIVER CERTIFICATE</strong></td>
<td><strong>VA-CSP 90 DAY MONITORING ASSESSMENT CHILD NOTE</strong></td>
</tr>
</tbody>
</table>

> \*\*Note: The name spacing for the above Note Titles/VHA Enterprise Standard Titles is required *for all facilities*. Print Names for each title, however, may be modified to be consistent with local policy for Interdisciplinary documents. Sites may need to modify

> some of the existing Local Note Titles/VHA Enterprise Titles if different than what is listed above.

> If you have any questions throughout this process, please feel free to email: <span class="mark">REDACTED</span> We will respond to your email and/or set up a time to talk and dial-in to your desktop if needed.

> <span id="_bookmark9" class="anchor"></span>APPENDIX A: Installation Example

> Software & Documentation Retrieval Instructions:

> ================================================

> This patch is being distributed as a host file. The name of the host file is PXRM_2_0_37.KID. This file should be downloaded in ASCII format.

> The preferred method for obtaining these files is to use File Transfer Protocol (FTP) to download them from:

> ftp://download.vista.med.va.gov/.

> This transmits the files from the first available FTP server. Sites may also elect to retrieve the files directly from a specific server as follows:

> Albany ftp.fo-albany.med.va.gov

> Hines ftp.fo-hines.med.va.gov Salt Lake City ftp.fo-slc.med.va.gov

> The Install and Setup Guide and User Manuals are also available on the above servers. It is available as .pdf format. This file should be downloaded in BINARY format.

> File Name: Description: Protocol:

> ========== ============ =========

> PXRM_2_0_37_IG.PDF PXRM\*2.0\*37 Install BINARY

> and Setup Guide

> PXRM_2_0_37.KID PXRM\*2.0\*37 Host File ASCII

> Documentation can also be found on the VistA Documentation Library (VDL) at: <http://www.va.gov/vdl/>

## Installing PXRM 2\*0\*37

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System Edits and Distribution ...

> Utilities ... Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<your directory\>PXRM_2_0_37.KID

> KIDS Distribution saved on May 05, 2015@08:21:22 Comment: Caregiver Templates

> This Distribution contains Transport Globals for the following Package(s): PXRM\*2.0\*37

> Distribution OK!

> Want to continue with Load? YES// (hit enter)

> Loading Distribution...

> PXRM\*2.0\*37

> Use INSTALL NAME: PXRM\*2.0\*37 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INSTall Package(s)

> Select INSTALL NAME: PXRM\*2.0\*37 5/7/15@08:37:10

> =\> Caregiver Templates ;Created on May 05, 2015@08:21:22

> This Distribution was loaded on May 07, 2015@08:37:10 with header of Caregiver Templates ;Created on May 05, 2015@08:21:22

> It consisted of the following Install(s):

> PXRM\*2.0\*37

> Checking Install for Package PXRM\*2.0\*37 Install Questions for PXRM\*2.0\*37 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO// (hit enter)

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// (hit enter)

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// (hit enter) TELNET PORT

> \+

> \+

PXRM\*2.0\*37

> Install Started for PXRM\*2.0\*37 :

> May 07, 2015@08:37:21

> Build Distribution Date: May 05, 2015 Installing Routines:

> May 07, 2015@08:37:21

> Running Pre-Install Routine: PRE^PXRMP37I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> May 07, 2015@08:37:21

> Installing Data:

> May 07, 2015@08:37:24

> Running Post-Install Routine: POST^PXRMP37I ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry VA-CAREGIVER DIALOG TEMPLATES Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*37 Installed.

> May 07, 2015@08:44:08

> Not a production UCI

> PXRM\*2.0\*37

> Install Completed

## APPENDIX B: Health Factors in each Reminder Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Categories are displayed in BOLD font with associated Health Factors beneath.

> Dialog Name: VA-CSP INITIAL IN-HOME ASSESSMENT REV

| INITIAL ZARIT BURDEN INTERVIEW |
|------------------------------------|
| CGI ZBI SCORE = 0                  |
| CGI ZBI SCORE = 1                  |
| CGI ZBI SCORE = 10                 |
| CGI ZBI SCORE = 11                 |
| CGI ZBI SCORE = 12                 |
| CGI ZBI SCORE = 13                 |
| CGI ZBI SCORE = 14                 |
| CGI ZBI SCORE = 15                 |
| CGI ZBI SCORE = 16                 |
| CGI ZBI SCORE = 2                  |
| CGI ZBI SCORE = 3                  |
| CGI ZBI SCORE = 4                  |
| CGI ZBI SCORE = 5                  |
| CGI ZBI SCORE = 6                  |
| CGI ZBI SCORE = 7                  |
| CGI ZBI SCORE = 8                  |
| CGI ZBI SCORE = 9                  |
| CGI FOLLOWUP                   |
| CGI ACTIONS                        |
| CGI ADAPT BED                      |
| CGI ADAPT BENCH                    |
| CGI ADAPT BLIND                    |
| CGI ADAPT BOARD                    |
| CGI ADAPT CANE                     |
| CGI ADAPT CHAIR                    |
| CGI ADAPT COMMODE                  |
| CGI ADAPT CRUTCHES                 |
| CGI ADAPT CUSHION                  |
| CGI ADAPT DRIVING                  |
| CGI ADAPT GRBARS                   |
| CGI ADAPT HEARING                  |
| CGI ADAPT MOBILITY                 |
| CGI ADAPT OTHER                    |
| CGI ADAPT PC                       |

| CGI ADAPT REACH       |
|-----------------------|
| CGI ADAPT ROLLIN      |
| CGI ADAPT SEAT        |
| CGI ADAPT SHOEHORN    |
| CGI ADAPT STOCK       |
| CGI ADAPT TOILETFRAME |
| CGI ADAPT TRAPEZE     |
| CGI ADAPT UTENSIL     |
| CGI ADAPT WALKER      |
| CGI ADAPT WHEELCHAIR  |
| CGI ADAPTIVE NEEDED   |
| CGI CLINIC            |
| CGI FOLLOWNEEDED NO   |
| CGI HOME              |
| CGI REFERRALS         |
| CGI TELEHEALTH        |
| CGI VISITS            |
| CGI UNMET NEEDS   |
| CGI NEED ADLS         |
| CGI NEED BVMGMTSKILLS |
| CGI NEED COG          |
| CGI NEED IADLS        |
| CGI NEED INFECT       |
| CGI NEED MEDMGMT      |
| CGI NEED NUTRITION    |
| CGI NEED OTHER        |
| CGI NEED SELF         |
| CGI NEED SKIN         |
| CGI NEED VITAL/PAIN   |
| CGI NEEDS NO          |
| CGI NEEDS YES         |
| CGI ENVIRONMENT   |
| CGI BATHCHAIR NA      |
| CGI BATHCHAIR NO      |
| CGI BATHCHAIR YES     |
| CGI COOKING NO        |
| CGI COOKING YES       |
| CGI DETERIORATE YES   |
| CGI DETERIORIATE NO   |
| CGI EMERGPLAN NO      |
| CGI EMERGPLAN YES     |

| CGI FIREEXIT NO     |
|---------------------|
| CGI FIREEXIT YES    |
| CGI FLOOR1 NO       |
| CGI FLOOR1 YES      |
| CGI FOOD NO         |
| CGI FOOD YES        |
| CGI GRABBARS NA     |
| CGI GRABBARS NO     |
| CGI GRABBARS YES    |
| CGI HANDRAILS NA    |
| CGI HANDRAILS NO    |
| CGI HANDRAILS YES   |
| CGI HEATAC NO       |
| CGI HEATAC YES      |
| CGI OBVFALLRISK NO  |
| CGI OBVFALLRISK YES |
| CGI OXYGEN NA       |
| CGI OXYGEN NO       |
| CGI OXYGEN YES      |
| CGI PESTS NO        |
| CGI PESTS YES       |
| CGI SAFEMEDS NA     |
| CGI SAFEMEDS NO     |
| CGI SAFEMEDS YES    |
| CGI SAFETY NO       |
| CGI SAFETY YES      |
| CGI SECURITY NO     |
| CGI SECURITY YES    |
| CGI SMOKE NO        |
| CGI SMOKE YES       |
| CGI STORAGE NO      |
| CGI STORAGE YES     |
| CGI SUPPLIES NA     |
| CGI SUPPLIES NO     |
| CGI SUPPLIES YES    |
| CGI VENTI NO        |
| CGI VENTI YES       |
| CGI WATER NO        |
| CGI WATER YES       |

| CGI PHYSICAL ASSESS   |
|---------------------------|
| CGI ABUSE NO              |
| CGI ABUSE YES             |
| CGI CLEGAL NO             |
| CGI CLEGAL YES            |
| CGI DRIVING NO            |
| CGI DRIVING YES           |
| CGI DRUGABUSE NO          |
| CGI DRUGABUSE YES         |
| CGI FALL NO               |
| CGI FALL YES W/ INJURY    |
| CGI FALL YES W/OUT INJURY |
| CGI GUNS NO               |
| CGI GUNS YES              |
| CGI VLEGAL NO             |
| CGI VLEGAL YES            |
| CGI IADLS             |
| CGI FINANCE A             |
| CGI FINANCE D             |
| CGI FINANCE I             |
| CGI HOUSEWORK A           |
| CGI HOUSEWORK D           |
| CGI HOUSEWORK I           |
| CGI MEALPREP A            |
| CGI MEALPREP D            |
| CGI MEALPREP I            |
| CGI MEDMGMT A             |
| CGI MEDMGMT D             |
| CGI MEDMGMT I             |
| CGI SHOPPING A            |
| CGI SHOPPING D            |
| CGI SHOPPING I            |
| CGI TELEPHONE A           |
| CGI TELEPHONE D           |
| CGI TELEPHONE I           |
| CGI TRANSPORT A           |
| CGI TRANSPORT D           |
| CGI TRANSPORT I           |

| CGI ADLS            |
|-------------------------|
| CGI AMBULATION A        |
| CGI AMBULATION D        |
| CGI AMBULATION I        |
| CGI BATHING A           |
| CGI BATHING D           |
| CGI BATHING I           |
| CGI DRESSING A          |
| CGI DRESSING D          |
| CGI DRESSING I          |
| CGI EQUIP BRACES        |
| CGI EQUIP CANE          |
| CGI EQUIP CRUTCH        |
| CGI EQUIP NONE          |
| CGI EQUIP OTHER         |
| CGI EQUIP WALKER        |
| CGI EQUIP WHEEL         |
| CGI FEEDING A           |
| CGI FEEDING D           |
| CGI FEEDING I           |
| CGI TOILETING A         |
| CGI TOILETING D         |
| CGI TOILETING I         |
| CGI TRANSFER A          |
| CGI TRANSFER D          |
| CGI TRANSFER I          |
| CGI CONTINENT       |
| CGI BLADDER NO          |
| CGI BLADDER YES         |
| CGI BOWEL NO            |
| CGI BOWEL YES           |
| CGI SPECIAL NEEDS   |
| CGI COLOSTOMY           |
| CGI CPAP                |
| CGI FEEDING TUBE        |
| CGI FOLEY               |
| CGI OXYGEN              |
| CGI SKIN CARE           |
| CGI SPECIAL NEEDS OTHER |
| CGI TRACH               |

| CGI PRIMARYRELATIONSHIP |
|-----------------------------|
| CGI PRELATION BRO           |
| CGI PRELATION DAU           |
| CGI PRELATION FA            |
| CGI PRELATION FRD           |
| CGI PRELATION MO            |
| CGI PRELATION OTHER         |
| CGI PRELATION OTREL         |
| CGI PRELATION SIS           |
| CGI PRELATION SON           |
| CGI PRELATION SP            |
| CGI PVET NO                 |
| CGI PVET YES                |
| CGI VET CAPACITY        |
| CGI VETCAPACITY NO          |
| CGI VETCAPACITY YES         |
| CGI CG VERB ABILITY     |
| CGI ADLS TRAINING           |
| CGI CG BHVRMGMT             |
| CGI CG SELFCARE             |
| CGI CGABILITY NO            |
| CGI CGABILITY YES           |
| CGI COGNITIVE               |
| CGI IADLS TRAINING          |
| CGI INFECT CTRL             |
| CGI MED MANAGE              |
| CGI NUTRITION               |
| CGI SKINCARE ABILITY        |
| CGI VITALS PAIN             |
| CGI SECONDRELATIONSHIP  |
| CGI SRELATION BRO           |
| CGI SRELATION DAU           |
| CGI SRELATION FA            |
| CGI SRELATION FRD           |
| CGI SRELATION MO            |
| CGI SRELATION OTHER         |
| CGI SRELATION OTREL         |
| CGI SRELATION SIS           |
| CGI SRELATION SON           |
| CGI SRELATION SP            |

| CGI SVET NO           |
|-----------------------|
| CGI SVET YES          |
| CGI CG EDUCATION  |
| CGI CBARRIERS NO      |
| CGI CBARRIERS YES     |
| CGI CBELIEFS          |
| CGI CCOGNITIVE        |
| CGI CEMOTIONAL        |
| CGI CHEARING          |
| CGI CLANGUAGE         |
| CGI CLITERACY         |
| CGI COTHER            |
| CGI CPAIN             |
| CGI CPHYSICAL         |
| CGI CVISUAL           |
| CGI VET EDUCATION |
| CGI VBARRIERS NO      |
| CGI VBARRIERS YES     |
| CGI VBELIEFS          |
| CGI VCOGNITIVE        |
| CGI VEMOTIONAL        |
| CGI VHEARING          |
| CGI VLANGUAGE         |
| CGI VLITERACY         |
| CGI VMISSEDAPPT       |
| CGI VOTHER            |
| CGI VPAIN             |
| CGI VPHYSICAL         |
| CGI VVISUAL           |
| CGI ASSESS        |
| CGI ORDERMEDS NO      |
| CGI ORDERMEDS YES     |
| CGI PLAN NO           |
| CGI PLAN YES          |
| CGI RESPITEAWARE NO   |
| CGI RESPITEAWARE YES  |
| CGI VET MH        |
| CGI VETMH NO          |
| CGI VETMH YES         |

> Dialog Name: VA-CSP INITIAL IN-HOME ASSESSMENT CHILD NOTE

| CGI ZARITFOLLOWUP |
|-----------------------|
| CGI ZARIT\<8          |
| CGI ZARIT\<8 F1       |
| CGI ZARIT\<8 F2       |
| CGI ZARIT\<8 F3       |
| CGI ZARIT\<8 F4       |
| CGI ZARIT\<8 F5       |
| CGI ZARIT\<8 F6       |
| CGI ZARIT\>7          |
| CGI ZARIT\>7 F1       |
| CGI ZARIT\>7 F2       |
| CGI ZARIT\>7 F3       |
| CGI ZARIT\>7 F4       |
| CGI ZARIT\>7 F5       |
| CGI ZARIT\>7 F6       |

> Dialog Name: VA-CSP ANNUAL IN-HOME ASSESSMENT REV

| ANNUAL ZARIT BURDEN INTERVIEW |
|-----------------------------------|
| CGA ZBI SCORE = 0                 |
| CGA ZBI SCORE = 1                 |
| CGA ZBI SCORE = 10                |
| CGA ZBI SCORE = 11                |
| CGA ZBI SCORE = 12                |
| CGA ZBI SCORE = 13                |
| CGA ZBI SCORE = 14                |
| CGA ZBI SCORE = 15                |
| CGA ZBI SCORE = 16                |
| CGA ZBI SCORE = 2                 |
| CGA ZBI SCORE = 3                 |
| CGA ZBI SCORE = 4                 |
| CGA ZBI SCORE = 5                 |
| CGA ZBI SCORE = 6                 |
| CGA ZBI SCORE = 7                 |
| CGA ZBI SCORE = 8                 |
| CGA ZBI SCORE = 9                 |

| CGA FOLLOWUP      |
|-----------------------|
| CGA ACTIONS           |
| CGA ADAPT BED         |
| CGA ADAPT BENCH       |
| CGA ADAPT BLIND       |
| CGA ADAPT BOARD       |
| CGA ADAPT CANE        |
| CGA ADAPT CHAIR       |
| CGA ADAPT COMMODE     |
| CGA ADAPT CRUTCHES    |
| CGA ADAPT CUSHION     |
| CGA ADAPT DRIVING     |
| CGA ADAPT GRBARS      |
| CGA ADAPT HEARING     |
| CGA ADAPT MOBILITY    |
| CGA ADAPT OTHER       |
| CGA ADAPT PC          |
| CGA ADAPT REACH       |
| CGA ADAPT ROLLIN      |
| CGA ADAPT SEAT        |
| CGA ADAPT SHOEHORN    |
| CGA ADAPT STOCK       |
| CGA ADAPT TOILETFRAME |
| CGA ADAPT TRAPEZE     |
| CGA ADAPT UTENSIL     |
| CGA ADAPT WALKER      |
| CGA ADAPT WHEELCHAIR  |
| CGA ADAPTIVE NEEDED   |
| CGA CLINIC            |
| CGA FOLLOWNEEDED NO   |
| CGA HOME              |
| CGA REFERRALS         |
| CGA TELEHEALTH        |
| CGA VISITS            |
| CGA UNMET NEEDS   |
| CGA NEED ADLS         |
| CGA NEED BVMGMTSKILLS |
| CGA NEED COG          |
| CGA NEED IADLS        |
| CGA NEED INFECT       |
| CGA NEED MEDMGMT      |
| CGA NEED NUTRITION    |

| CGA NEED OTHER      |
|---------------------|
| CGA NEED SELF       |
| CGA NEED SKIN       |
| CGA NEED VITAL/PAIN |
| CGA NEEDS NO        |
| CGA NEEDS YES       |
| CGA ENVIRONMENT |
| CGA BATHCHAIR NA    |
| CGA BATHCHAIR NO    |
| CGA BATHCHAIR YES   |
| CGA COOKING NO      |
| CGA COOKING YES     |
| CGA DETERIORATE NO  |
| CGA DETERIORATE YES |
| CGA EMERGPLAN NO    |
| CGA EMERGPLAN YES   |
| CGA FIREEXIT NO     |
| CGA FIREEXIT YES    |
| CGA FLOOR1 NO       |
| CGA FLOOR2 YES      |
| CGA FOOD NO         |
| CGA FOOD YES        |
| CGA GRABBARS NA     |
| CGA GRABBARS NO     |
| CGA GRABBARS YES    |
| CGA HANDRAILS NA    |
| CGA HANDRAILS NO    |
| CGA HANDRAILS YES   |
| CGA HEATAC NO       |
| CGA HEATAC YES      |
| CGA OBVFALLRISK NO  |
| CGA OBVFALLRISK YES |
| CGA OXYGEN NA       |
| CGA OXYGEN NO       |
| CGA OXYGEN YES      |
| CGA PESTS NO        |
| CGA PESTS YES       |
| CGA SAFEMEDS NA     |
| CGA SAFEMEDS NO     |
| CGA SAFEMEDS YES    |
| CGA SAFETY NO       |
| CGA SAFETY YES      |

| CGA SECURITY NO           |
|---------------------------|
| CGA SECURITY YES          |
| CGA SMOKE NO              |
| CGA SMOKE YES             |
| CGA STORAGE NO            |
| CGA STORAGE YES           |
| CGA SUPPLIES NA           |
| CGA SUPPLIES NO           |
| CGA SUPPLIES YES          |
| CGA VENTI NO              |
| CGA VENTI YES             |
| CGA WATER NO              |
| CGA WATER YES             |
| CGA PHYSICAL ASSESS   |
| CGA ABUSE NO              |
| CGA ABUSE YES             |
| CGA CLEGAL NO             |
| CGA CLEGAL YES            |
| CGA DRIVING NO            |
| CGA DRIVING YES           |
| CGA DRUGABUSE NO          |
| CGA DRUGABUSE YES         |
| CGA FALL NO               |
| CGA FALL YES W/ INJURY    |
| CGA FALL YES W/OUT INJURY |
| CGA GUNS NO               |
| CGA GUNS YES              |
| CGA VLEGAL NO             |
| CGA VLEGAL YES            |
| CGA IADLS             |
| CGA FINANCE A             |
| CGA FINANCE D             |
| CGA FINANCE I             |
| CGA HOUSEWORK A           |
| CGA HOUSEWORK D           |
| CGA HOUSEWORK I           |
| CGA IADLS CHG NO          |
| CGA IADLS CHG YES         |
| CGA MEALPREP A            |
| CGA MEALPREP D            |
| CGA MEALPREP I            |

| CGA MEDMGMT A    |
|------------------|
| CGA MEDMGMT D    |
| CGA MEDMGMT I    |
| CGA SHOPPING A   |
| CGA SHOPPING D   |
| CGA SHOPPING I   |
| CGA TELEPHONE A  |
| CGA TELEPHONE D  |
| CGA TELEPHONE I  |
| CGA TRANSPORT A  |
| CGA TRANSPORT D  |
| CGA TRANSPORT I  |
| CGA ADLS     |
| CGA AMBULATION A |
| CGA AMBULATION D |
| CGA AMBULATION I |
| CGA BATHING A    |
| CGA BATHING D    |
| CGA BATHING I    |
| CGA DRESSING A   |
| CGA DRESSING D   |
| CGA DRESSING I   |
| CGA EQUIP BRACES |
| CGA EQUIP CANE   |
| CGA EQUIP CRUTCH |
| CGA EQUIP NONE   |
| CGA EQUIP OTHER  |
| CGA EQUIP WALKER |
| CGA EQUIP WHEEL  |
| CGA FEEDING A    |
| CGA FEEDING D    |
| CGA FEEDING I    |
| CGA TOILETING A  |
| CGA TOILETING D  |
| CGA TOILETING I  |
| CGA TRANSFER A   |
| CGA TRANSFER D   |
| CGA TRANSFER I   |

| CGA CONTINENT          |
|----------------------------|
| CGA BLADDER NO             |
| CGA BLADDER YES            |
| CGA BOWEL NO               |
| CGA BOWEL YES              |
| CGA SPECIAL NEEDS      |
| CGA COLOSTOMY              |
| CGA CPAP                   |
| CGA FEEDING TUBE           |
| CGA FOLEY                  |
| CGA OXYGEN                 |
| CGA SKIN CARE              |
| CGA SPECIAL NEEDS OTHER    |
| CGA TRACH                  |
| CGA VET MH             |
| CGA VETMH NO               |
| CGA VETMH YES              |
| CGA CG VERB ABILITY    |
| CGA ADLS TRAINING          |
| CGA CG BHVRMGMT            |
| CGA CG SELFCARE            |
| CGA CGABILITY NO           |
| CGA CGABILITY YES          |
| CGA COGNITIVE              |
| CGA IADLS TRAINING         |
| CGA INFECT CTRL            |
| CGA MED MANAGE             |
| CGA NUTRITION              |
| CGA SKINCARE ABILITY       |
| CGA VITALS PAIN            |
| CGA VET CAPACITY       |
| CGA VETCAPACITY NO         |
| CGA VETCAPACITY YES        |
| CGA SECONDRELATIONSHIP |
| CGA SRELATION BRO          |
| CGA SRELATION DAU          |
| CGA SRELATION FA           |
| CGA SRELATION FRD          |
| CGA SRELATION MO           |

| CGA SRELATION OTHER   |
|-----------------------|
| CGA SRELATION OTREL   |
| CGA SRELATION SIS     |
| CGA SRELATION SON     |
| CGA SRELATION SP      |
| CGA SVET NO           |
| CGA SVET YES          |
| CGA VETCHANGES    |
| CGA ENVIRONMENT NO    |
| CGA ENVIRONMENT YES   |
| CGA CG EDUCATION  |
| CGA CBARRIERS NO      |
| CGA CBARRIERS YES     |
| CGA CBELIEFS          |
| CGA CCOGNITIVE        |
| CGA CEMOTIONAL        |
| CGA CHEARING          |
| CGA CLANGUAGE         |
| CGA CLITERACY         |
| CGA COTHER            |
| CGA CPAIN             |
| CGA CPHYSICAL         |
| CGA CVISUAL           |
| CGA VET EDUCATION |
| CGA VBARRIERS NO      |
| CGA VBARRIERS YES     |
| CGA VBELIEFS          |
| CGA VCOGNITIVE        |
| CGA VEMOTIONAL        |
| CGA VHEARING          |
| CGA VLANGUAGE         |
| CGA VLITERACY         |
| CGA VMISSEDAPPT       |
| CGA VOTHER            |
| CGA VPAIN             |
| CGA VPHYSICAL         |
| CGA VVISUAL           |

| CGA ASSESS       |
|----------------------|
| CGA ORDERMEDS NO     |
| CGA ORDERMEDS YES    |
| CGA PLAN NO          |
| CGA PLAN YES         |
| CGA RESPITEAWARE NO  |
| CGA RESPITEAWARE YES |

> Dialog Name: VA-CSP ANNUAL IN-HOME ASSESSMENT CHILD NOTE

| CGA ZARITFOLLOWUP |
|-----------------------|
| CGA ZARIT\<8          |
| CGA ZARIT\<8 F1       |
| CGA ZARIT\<8 F2       |
| CGA ZARIT\<8 F3       |
| CGA ZARIT\<8 F4       |
| CGA ZARIT\<8 F5       |
| CGA ZARIT\<8 F6       |
| CGA ZARIT\>7          |
| CGA ZARIT\>7 F1       |
| CGA ZARIT\>7 F2       |
| CGA ZARIT\>7 F3       |
| CGA ZARIT\>7 F4       |
| CGA ZARIT\>7 F5       |
| CGA ZARIT\>7 F6       |

> Dialog Name: VA-CSP INTERIM IN-HOME ASSESSMENT REV

| INTERIM ZARIT BURDEN INTERVIEW |
|------------------------------------|
| CGINT ZBI SCORE = 0                |
| CGINT ZBI SCORE = 1                |
| CGINT ZBI SCORE = 10               |
| CGINT ZBI SCORE = 11               |
| CGINT ZBI SCORE = 12               |
| CGINT ZBI SCORE = 13               |
| CGINT ZBI SCORE = 14               |
| CGINT ZBI SCORE = 15               |
| CGINT ZBI SCORE = 16               |
| CGINT ZBI SCORE = 2                |
| CGINT ZBI SCORE = 3                |
| CGINT ZBI SCORE = 4                |
| CGINT ZBI SCORE = 5                |
| CGINT ZBI SCORE = 6                |
| CGINT ZBI SCORE = 7                |
| CGINT ZBI SCORE = 8                |
| CGINT ZBI SCORE = 9                |
| CGINT VET MH                   |
| CGINT VETMH NO                     |
| CGINT VETMH YES                    |
| CGINT FOLLOWUP                 |
| CGINT ACTIONS                      |
| CGINT ADAPT BED                    |
| CGINT ADAPT BENCH                  |
| CGINT ADAPT BLIND                  |
| CGINT ADAPT BOARD                  |
| CGINT ADAPT CANE                   |
| CGINT ADAPT CHAIR                  |
| CGINT ADAPT COMMODE                |
| CGINT ADAPT CRUTCHES               |
| CGINT ADAPT CUSHION                |
| CGINT ADAPT DRIVING                |
| CGINT ADAPT GRBARS                 |
| CGINT ADAPT HEARING                |
| CGINT ADAPT MOBILITY               |
| CGINT ADAPT OTHER                  |
| CGINT ADAPT PC                     |
| CGINT ADAPT REACH                  |

| CGINT ADAPT ROLLIN      |
|-------------------------|
| CGINT ADAPT SEAT        |
| CGINT ADAPT SHOEHORN    |
| CGINT ADAPT STOCK       |
| CGINT ADAPT TOILETFRAME |
| CGINT ADAPT TRAPEZE     |
| CGINT ADAPT UTENSIL     |
| CGINT ADAPT WALKER      |
| CGINT ADAPT WHEELCHAIR  |
| CGINT ADAPTIVE NEEDED   |
| CGINT CLINIC            |
| CGINT FOLLOWNEEDED NO   |
| CGINT HOME              |
| CGINT REFERRALS         |
| CGINT TELEHEALTH        |
| CGINT VISITS            |
| CGINT UNMET NEEDS   |
| CGINT NEED ADLS         |
| CGINT NEED BVMGMTSKILLS |
| CGINT NEED COG          |
| CGINT NEED IADLS        |
| CGINT NEED INFECT       |
| CGINT NEED MEDMGMT      |
| CGINT NEED NUTRITION    |
| CGINT NEED OTHER        |
| CGINT NEED SELF         |
| CGINT NEED SKIN         |
| CGINT NEED VITAL/PAIN   |
| CGINT NEEDS NO          |
| CGINT NEEDS YES         |
| CGINT CG EDUCATION  |
| CGINT CBARRIERS NO      |
| CGINT CBARRIERS YES     |
| CGINT CBELIEFS          |
| CGINT CCOGNITIVE        |
| CGINT CEMOTIONAL        |
| CGINT CHEARING          |
| CGINT CLANGUAGE         |
| CGINT CLITERACY         |
| CGINT COTHER            |
| CGINT CPAIN             |

| CGINT CPHYSICAL         |
|-------------------------|
| CGINT CVISUAL           |
| CGINT VET EDUCATION |
| CGINT VBARRIERS NO      |
| CGINT VBARRIERS YES     |
| CGINT VBELIEFS          |
| CGINT VCOGNITIVE        |
| CGINT VEMOTIONAL        |
| CGINT VHEARING          |
| CGINT VLANGUAGE         |
| CGINT VLITERACY         |
| CGINT VMISSEDAPPT       |
| CGINT VOTHER            |
| CGINT VPAIN             |
| CGINT VPHYSICAL         |
| CGINT VVISUAL           |
| CGINT ASSESS        |
| CGINT ORDERMEDS NO      |
| CGINT ORDERMEDS YES     |
| CGINT PLAN NO           |
| CGINT PLAN YES          |
| CGINT RESPITEAWARE NO   |
| CGINT RESPITEAWARE YES  |
| CGINT ENVIRONMENT   |
| CGINT BATHCHAIR NA      |
| CGINT BATHCHAIR NO      |
| CGINT BATHCHAIR YES     |
| CGINT COOKING NO        |
| CGINT COOKING YES       |
| CGINT DETERIORATE NO    |
| CGINT DETERIORATE YES   |
| CGINT EMERGPLAN NO      |
| CGINT EMERGPLAN YES     |
| CGINT FIREEXIT NO       |
| CGINT FIREEXIT YES      |
| CGINT FLOOR1 NO         |
| CGINT FLOOR1 YES        |
| CGINT FOOD NO           |
| CGINT FOOD YES          |
| CGINT GRABBARS NA       |

| CGINT GRABBARS NO         |
|---------------------------|
| CGINT GRABBARS YES        |
| CGINT HANDRAILS NA        |
| CGINT HANDRAILS NO        |
| CGINT HANDRAILS YES       |
| CGINT HEATAC NO           |
| CGINT HEATAC YES          |
| CGINT OBVFALLRISK NO      |
| CGINT OBVFALLRISK YES     |
| CGINT OXYGEN NA           |
| CGINT OXYGEN NO           |
| CGINT OXYGEN YES          |
| CGINT PESTS NO            |
| CGINT PESTS YES           |
| CGINT SAFEMEDS NA         |
| CGINT SAFEMEDS NO         |
| CGINT SAFEMEDS YES        |
| CGINT SAFETY NO           |
| CGINT SAFETY YES          |
| CGINT SECURITY NO         |
| CGINT SECURITY YES        |
| CGINT SMOKE NO            |
| CGINT SMOKE YES           |
| CGINT STORAGE NO          |
| CGINT STORAGE YES         |
| CGINT SUPPLIES NA         |
| CGINT SUPPLIES NO         |
| CGINT SUPPLIES YES        |
| CGINT VENTI NO            |
| CGINT VENTI YES           |
| CGINT WATER NO            |
| CGINT WATER YES           |
| CGINT VETCHANGES      |
| CGINT ENVIRONMENT NO      |
| CGINT ENVIRONMENT YES     |
| CGINT PHYSICAL ASSESS |
| CGINT ABUSE NO            |
| CGINT ABUSE YES           |
| CGINT CLEGAL NO           |
| CGINT CLEGAL YES          |
| CGINT DRIVING NO          |

| CGINT DRIVING YES           |
|-----------------------------|
| CGINT DRUGABUSE NO          |
| CGINT DRUGABUSE YES         |
| CGINT FALL NO               |
| CGINT FALL YES W/ INJURY    |
| CGINT FALL YES W/OUT INJURY |
| CGINT GUNS NO               |
| CGINT GUNS YES              |
| CGINT VLEGAL NO             |
| CGINT VLEGAL YES            |
| CGINT IADLS             |
| CGINT FINANCE A             |
| CGINT FINANCE D             |
| CGINT FINANCE I             |
| CGINT HOUSEWORK A           |
| CGINT HOUSEWORK D           |
| CGINT HOUSEWORK I           |
| CGINT IADLS CHG NO          |
| CGINT IADLS CHG YES         |
| CGINT MEALPREP A            |
| CGINT MEALPREP D            |
| CGINT MEALPREP I            |
| CGINT MEDMGMT A             |
| CGINT MEDMGMT D             |
| CGINT MEDMGMT I             |
| CGINT SHOPPING A            |
| CGINT SHOPPING D            |
| CGINT SHOPPING I            |
| CGINT TELEPHONE A           |
| CGINT TELEPHONE D           |
| CGINT TELEPHONE I           |
| CGINT TRANSPORT A           |
| CGINT TRANSPORT D           |
| CGINT TRANSPORT I           |
| CGINT ADLS              |
| CGINT ADLS CHG NO           |
| CGINT ADLS CHG YES          |
| CGINT AMBULATION A          |
| CGINT AMBULATION D          |
| CGINT AMBULATION I          |
| CGINT BATHING A             |

| CGINT BATHING D           |
|---------------------------|
| CGINT BATHING I           |
| CGINT DRESSING A          |
| CGINT DRESSING D          |
| CGINT DRESSING I          |
| CGINT EQUIP BRACES        |
| CGINT EQUIP CANE          |
| CGINT EQUIP CRUTCH        |
| CGINT EQUIP NONE          |
| CGINT EQUIP OTHER         |
| CGINT EQUIP WALKER        |
| CGINT EQUIP WHEEL         |
| CGINT FEEDING A           |
| CGINT FEEDING D           |
| CGINT FEEDING I           |
| CGINT TOILETING A         |
| CGINT TOILETING D         |
| CGINT TOILETING I         |
| CGINT TRANSFER A          |
| CGINT TRANSFER D          |
| CGINT TRANSFER I          |
| CGINT CONTINENT       |
| CGINT BLADDER NO          |
| CGINT BLADDER YES         |
| CGINT BOWEL NO            |
| CGINT BOWEL YES           |
| CGINT SPECIAL NEEDS   |
| CGINT COLOSTOMY           |
| CGINT CPAP                |
| CGINT FEEDING TUBE        |
| CGINT FOLEY               |
| CGINT OXYGEN              |
| CGINT SKIN CARE           |
| CGINT SPECIAL NEEDS OTHER |
| CGINT TRACH               |
| CGINT VET CAPACITY    |
| CGINT CAPACITY CHANGE NO  |
| CGINT CAPACITY CHANGE YES |
| CGINT VETCAPACITY NO      |
| CGINT VETCAPACITY YES     |

| CGINT CG VERB ABILITY    |
|------------------------------|
| CGINT ADLS TRAINING          |
| CGINT CG BHVRMGMT            |
| CGINT CG SELFCARE            |
| CGINT CGABILITY NO           |
| CGINT CGABILITY YES          |
| CGINT COGNITIVE              |
| CGINT IADLS TRAINING         |
| CGINT INFECT CTRL            |
| CGINT MED MANAGE             |
| CGINT NUTRITION              |
| CGINT SKINCARE ABILITY       |
| CGINT VITALS PAIN            |
| CGINT SECONDRELATIONSHIP |
| CGINT SRELATION BRO          |
| CGINT SRELATION DAU          |
| CGINT SRELATION FA           |
| CGINT SRELATION FRD          |
| CGINT SRELATION MO           |
| CGINT SRELATION OTHER        |
| CGINT SRELATION OTREL        |
| CGINT SRELATION SIS          |
| CGINT SRELATION SON          |
| CGINT SRELATION SP           |
| CGINT SVET NO                |
| CGINT SVET YES               |

> Dialog Name: VA-CSP INTERIM IN-HOME ASSESSMENT CHILD NOTE

| CGINT ZARITFOLLOWUP |
|-------------------------|
| CGINT ZARIT\<8          |
| CGINT ZARIT\<8 F1       |
| CGINT ZARIT\<8 F2       |
| CGINT ZARIT\<8 F3       |
| CGINT ZARIT\<8 F4       |
| CGINT ZARIT\<8 F5       |
| CGINT ZARIT\<8 F6       |
| CGINT ZARIT\>7          |
| CGINT ZARIT\>7 F1       |
| CGINT ZARIT\>7 F2       |
| CGINT ZARIT\>7 F3       |
| CGINT ZARIT\>7 F4       |
| CGINT ZARIT\>7 F5       |
| CGINT ZARIT\>7 F6       |

> Dialog Name: VA-CSP 90 DAY MONITORING ASSESSMENT

| 90 DAY MONITORING ZARIT BURDEN INTERVIEW |
|----------------------------------------------|
| CGF ZBI SCORE = 0                            |
| CGF ZBI SCORE = 1                            |
| CGF ZBI SCORE = 10                           |
| CGF ZBI SCORE = 11                           |
| CGF ZBI SCORE = 12                           |
| CGF ZBI SCORE = 13                           |
| CGF ZBI SCORE = 14                           |
| CGF ZBI SCORE = 15                           |
| CGF ZBI SCORE = 16                           |
| CGF ZBI SCORE = 2                            |
| CGF ZBI SCORE = 3                            |
| CGF ZBI SCORE = 4                            |
| CGF ZBI SCORE = 5                            |
| CGF ZBI SCORE = 6                            |
| CGF ZBI SCORE = 7                            |
| CGF ZBI SCORE = 8                            |
| CGF ZBI SCORE = 9                            |
| CGF INTERIMVISIT NEEDED                  |
| CGF NOT INDICATED                            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CGF CONTACT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CGF CONTACT CVT</p>
<p>CGF CONTACT IN-PERSON CGF CONTACT OTHER</p></td>
</tr>
<tr class="even">
<td>CGF CONTACT TELEPHONE</td>
</tr>
<tr class="odd">
<td><strong>CGF VETHEALTH</strong></td>
</tr>
<tr class="even">
<td>CGF ABUSE NO</td>
</tr>
<tr class="odd">
<td>CGF ABUSE YES</td>
</tr>
<tr class="even">
<td>CGF ADLCHANGE NO</td>
</tr>
<tr class="odd">
<td>CGF ADLCHANGE YES</td>
</tr>
<tr class="even">
<td>CGF MENTAL NO</td>
</tr>
<tr class="odd">
<td>CGF MENTAL YES</td>
</tr>
<tr class="even">
<td>CGF SUPERVISION NO</td>
</tr>
<tr class="odd">
<td>CGF SUPERVISION YES</td>
</tr>
<tr class="even">
<td><strong>CGF YEAR IN PROGRAM</strong></td>
</tr>
<tr class="odd">
<td>CGF 90CHANGE NO</td>
</tr>
<tr class="even">
<td>CGF 90CHANGE YES</td>
</tr>
</tbody>
</table>

> CGF VET MH CGF VETMH NO CGF VETMH YES

> Dialog Name: VA-CSP 90 DAY MONITORING ASSESSMENT CHILD NOTE

> CGF ZARITFOLLOWUP

| CGF ZARIT\<8    |
|-----------------|
| CGF ZARIT\<8 F1 |
| CGF ZARIT\<8 F2 |
| CGF ZARIT\<8 F3 |
| CGF ZARIT\<8 F4 |
| CGF ZARIT\<8 F5 |
| CGF ZARIT\<8 F6 |
| CGF ZARIT\>7    |
| CGF ZARIT\>7 F1 |
| CGF ZARIT\>7 F2 |
| CGF ZARIT\>7 F3 |
| CGF ZARIT\>7 F4 |
| CGF ZARIT\>7 F5 |
| CGF ZARIT\>7 F6 |