---
title: NUMI User Guide Version 15.15
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: NUMI
app_name: National Utilization Management Integration
section: GUI
app_status: archive
pkg_ns: NUMI
patch_ver: 15.15
patch_id: NUMI*15.15
group_key: NUMI:NUMI:15.15
file_numbers: []
security_keys: []
menu_options: 0
description: '''- User Guide for National Utilization Management Integration (NUMI) - Introduction - Purpose - Scope - Audience - Overview - [User Instructions: Getting...'''
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 43081
section_count: 20
table_count: 12
figure_count: 16
appendix_count: 8
has_toc: false
is_stub: false
pub_date: ''
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_15_15_ug_r.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_15_15_ug_r.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=285
audit_applied: '2026-05-31'
master_source: NUMI User Guide Version 15.15
master_pub_date: ''
consolidated_from: 5 versions
prior_versions:
- NUMI User Guide Version 15.10
- NUMI User Guide Version 15.11
- NUMI User Guide Version 15.9
- NUMI User Guide
consolidated_title: numi user guide
---

# User Guide for National Utilization Management Integration (NUMI)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [User Guide for National Utilization Management Integration (NUMI)](#user-guide-for-national-utilization-management-integration-numi)
  - [Introduction](#introduction)
    - [Purpose](#purpose)
    - [Scope](#scope)
    - [Audience](#audience)
    - [Overview](#overview)
  - [User Instructions: Getting Started](#user-instructions-getting-started)
    - [Allowing Pop-Ups for the Site](#allowing-pop-ups-for-the-site)
    - [Making NUMI a Trusted Site](#making-numi-a-trusted-site)
    - [Allowing ActiveX Controls for the Site](#allowing-activex-controls-for-the-site)
    - [Setting Your Screen Resolution to 1024 x 768 or higher](#setting-your-screen-resolution-to-1024-x-768-or-higher)
    - [Making Sure You Have a VistA Account](#making-sure-you-have-a-vista-account)
    - [Setting Up Your Internet Browser](#setting-up-your-internet-browser)
    - [Creating a NUMI Icon on Your Desktop](#creating-a-numi-icon-on-your-desktop)
    - [Launching NUMI from Your Internet Browser](#launching-numi-from-your-internet-browser)
    - [Locating Your NUMI Point of Contact (POC)](#locating-your-numi-point-of-contact-poc)
    - [Using NUMI Search Filters](#using-numi-search-filters)
    - [Using NUMI Hyperlinks](#using-numi-hyperlinks)
    - [Displaying Information in NUMI](#displaying-information-in-numi)
    - [Adobe Flash Player for CERMe](#adobe-flash-player-for-cerme)
  - [National Utilization Management Integration (NUMI) Login](#national-utilization-management-integration-numi-login)
    - [VA Single Sign-On Login](#va-single-sign-on-login)
    - [NUMI Login](#numi-login)
    - [Application Problem Notification](#application-problem-notification)
  - [Patient Selection / Worklist](#patient-selection-worklist)
    - [Accessing Patient Information](#accessing-patient-information)
    - [General Navigation](#general-navigation)
    - [Include Observations](#include-observations)
    - [Using Filters and Paging Features](#using-filters-and-paging-features)
    - [Dismissing a Patient Stay](#dismissing-a-patient-stay)
    - [Selecting Patients for Review](#selecting-patients-for-review)
    - [Viewing Patient Information for Different Sites](#viewing-patient-information-for-different-sites)
    - [Assigning and Reassigning Reviewers to Stays](#assigning-and-reassigning-reviewers-to-stays)
    - [Assigning / Reassigning a Reviewer](#assigning-reassigning-a-reviewer)
  - [Patient Stay History](#patient-stay-history)
    - [Patient Stay List](#patient-stay-list)
    - [Currently Selected Stay Information](#currently-selected-stay-information)
    - [Reviews for Currently Selected Stays List](#reviews-for-currently-selected-stays-list)
    - [Table of Stay Movements and Table of Reviews](#table-of-stay-movements-and-table-of-reviews)
    - [Dismiss a Patient](#dismiss-a-patient)
    - [Selecting a Review from the Reviews Table](#selecting-a-review-from-the-reviews-table)
    - [Viewing Patient Insurance Information](#viewing-patient-insurance-information)
    - [Printing out a Patient Worksheet](#printing-out-a-patient-worksheet)
    - [Invalidating a Patient Stay](#invalidating-a-patient-stay)
  - [InterQual<sup>®</sup> Criteria](#interqualsupsup-criteria)
    - [Selecting a Review Type](#selecting-a-review-type)
    - [CERMe Help, Navigation and Font Size](#cerme-help-navigation-and-font-size)
    - [Selecting the Product, Category and Subsets](#selecting-the-product-category-and-subsets)
    - [Keyword/Medical Code Search and Instruction Notes](#keywordmedical-code-search-and-instruction-notes)
    - [Criteria Organization](#criteria-organization)
    - [Level of Care (LOC) Options: Acute Adult Product](#level-of-care-loc-options-acute-adult-product)
    - [Working with InterQual® Notes](#working-with-interqual-notes)
    - [Create a Review with CERMe](#create-a-review-with-cerme)
    - [Create a Review with CERMe](#create-a-review-with-cerme-1)
    - [Additional Features in CERMe](#additional-features-in-cerme)
  - [Primary Review Summary](#primary-review-summary)
    - [Selecting the Day Being Reviewed Date](#selecting-the-day-being-reviewed-date)
    - [Selecting Admission Review Type](#selecting-admission-review-type)
    - [Selecting or Changing Current Level of Care](#selecting-or-changing-current-level-of-care)
    - [Enter Criteria Not Met Elaboration](#enter-criteria-not-met-elaboration)
    - [Adding Reviewer Comments](#adding-reviewer-comments)
    - [Selecting a Stay Reason](#selecting-a-stay-reason)
    - [Selecting or Changing Recommended Level of Care](#selecting-or-changing-recommended-level-of-care)
    - [Assigning a Physician Advisor to a Review that has Not Met Criteria](#assigning-a-physician-advisor-to-a-review-that-has-not-met-criteria)
    - [Changing the Next Review Reminder Date](#changing-the-next-review-reminder-date)
    - [Indicating No More Reviews on a Stay](#indicating-no-more-reviews-on-a-stay)
    - [Admitting Physician](#admitting-physician)
    - [Working with Admission Sources](#working-with-admission-sources)
    - [Selecting or Changing Treating Specialty](#selecting-or-changing-treating-specialty)
    - [Selecting or Changing Service Section](#selecting-or-changing-service-section)
    - [Selecting or Changing Ward](#selecting-or-changing-ward)
    - [Adding Custom Notes](#adding-custom-notes)
    - [Indicating an Unscheduled Readmit within 30 Days](#indicating-an-unscheduled-readmit-within-30-days)
    - [Working with Admission Review Types](#working-with-admission-review-types)
    - [Showing a Patient's Reviews](#showing-a-patients-reviews)
    - [Copying a Review from the Primary Review Screen](#copying-a-review-from-the-primary-review-screen)
    - [Viewing CERMe Review Text](#viewing-cerme-review-text)
    - [Saving and Locking a Final Review](#saving-and-locking-a-final-review)
    - [Days Since Last VA Acute Care Discharge Calculation](#days-since-last-va-acute-care-discharge-calculation)
  - [Primary Review Summary](#primary-review-summary-1)
  - [Physician Advisor Review](#physician-advisor-review)
    - [Physician Advisor Review](#physician-advisor-review-1)
    - [Selecting a Physician Advisor Review](#selecting-a-physician-advisor-review)
    - [Agreeing / Disagreeing with Current Level of Care](#agreeing-disagreeing-with-current-level-of-care)
    - [Entering Physician Advisor Comments](#entering-physician-advisor-comments)
    - [Saving and Locking a Final Review](#saving-and-locking-a-final-review-1)
  - [Tools Menu](#tools-menu)
    - [Patient Selection/Worklist Option](#patient-selectionworklist-option)
    - [Utilization Management Review Listing Option](#utilization-management-review-listing-option)
    - [Dismissed Patient Stays](#dismissed-patient-stays)
    - [Free Text Search Option](#free-text-search-option)
    - [Physician Advisor Review Option](#physician-advisor-review-option)
    - [Manual VistA Synchronization Option](#manual-vista-synchronization-option)
    - [Patient Stay Administration Option](#patient-stay-administration-option)
    - [Logout Option](#logout-option)
  - [Reports Menu](#reports-menu)
  - [Unlocking and Deleting Reviews](#unlocking-and-deleting-reviews)
    - [Unlocking a Locked Primary Review](#unlocking-a-locked-primary-review)
    - [Unlocking the Physician Advisor Portion of a Locked Review](#unlocking-the-physician-advisor-portion-of-a-locked-review)
    - [Deleting a Review](#deleting-a-review)
  - [Copying Reviews](#copying-reviews)
    - [To copy a review from the Patient Stay History Screen](#to-copy-a-review-from-the-patient-stay-history-screen)
    - [To copy a review from the Primary Review screen](#to-copy-a-review-from-the-primary-review-screen)
    - [To copy a review from the Review Summary screen](#to-copy-a-review-from-the-review-summary-screen)
  - [Admin Menu](#admin-menu)
    - [Accessing the NUMI Users Feature](#accessing-the-numi-users-feature)
    - [Accessing the NUMI Site Admin Feature](#accessing-the-numi-site-admin-feature)
    - [Accessing the NUMI Treating Specialty Configuration Feature](#accessing-the-numi-treating-specialty-configuration-feature)
  - [Logging Out of the NUMI Application](#logging-out-of-the-numi-application)
    - [To logout of the NUMI application](#to-logout-of-the-numi-application)
  - [Online Help Menu](#online-help-menu)
  - [Primary Reviewer and Primary Reviews](#primary-reviewer-and-primary-reviews)
  - [Physician Advisors and Medical Reviews](#physician-advisors-and-medical-reviews)
  - [CERMe vs. CERME vs. CERM](#cerme-vs-cerme-vs-cerm)
- [Index](#index)
![](numi-user-guide-version-15-15/001.png)
Department of Veteran Affairs
October 2024
Version 1.1.15.15
Revision History
<table>
<caption><p><span id="_bookmark44" class="anchor"></span>Table 1: NUMI Login Screen Features</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Document Version No.</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/7/2024</td>
<td>2.8</td>
<td>Updated link to Enhanced Reports in <a href="#reports-menu-1">Reports Menu</a> section</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/16/2024</td>
<td>2.7</td>
<td>Updated application version to 15.15<br />
updated footer month</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>01/24/2024</td>
<td>2.6</td>
<td><p>Updated application version to 15.14</p>
<p>Updated Footer month and year</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>10/26/2023</td>
<td>2.5</td>
<td><p>Added references to Enhanced Reports link on NUMI application Reports Menu</p>
<p>Provided a definition of full VistA username format that explains it is always LASTNAME,FIRSTNAME</p>
<p>Updated User guide based on VHA review process SOP update</p>
<p>Updated Physician Advisor Review Selections</p>
<p>Updated application version to 15.13</p>
<p>Updated Footer month and year</p>
<p>Updated figures for 508 compliance</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>1/9/2023</td>
<td>2.4</td>
<td><p>Removed references to Enhanced Reports</p>
<p>Updated application version to 15.11</p>
<p>Updated Footer month and year</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/15/2021</td>
<td>2.33</td>
<td>Updated application version to 15.10</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/8/2021</td>
<td>2.32</td>
<td>Updated 15 days to 7 as per INC17430279</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/23/2020</td>
<td>2.31</td>
<td>Updated Enhanced Reports link on page 117. Version number has been updated to 15.9.1 in title. Footer month and year have been updated.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/30/2019</td>
<td>2.30</td>
<td>Updated version number to 15.9. Functionality change for PUMA reviews from 15 days to 7, Chapter 12 updated. Appendix E, added additional questions. Appendix relabeling, updated TOC and index</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>08/24/2019</td>
<td>2.29</td>
<td>SSOI NUMI Login added under Section 3.1. Updated figures for Section 3.1 and added Appendix H, Access/Verify Alternate Login</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>06/11/2019</td>
<td>2.28</td>
<td>Super user note added for Admin Sites Section.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>04/16/2019</td>
<td>2.27</td>
<td>Updating to version five and changing dates on footer and title.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>03/21/2019</td>
<td>2.26</td>
<td>Update/Remove language concerning the removal of print preview and export buttons.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>03/05/2019</td>
<td>2.25</td>
<td>Updated Section 9.3.1 with updated language and added figure for the default selection of the radio button change made for Sec.508 compliance.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>04/17/2018</td>
<td>2.21</td>
<td>Updates to document for version 15.5</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>02/21/2018</td>
<td>2.23</td>
<td>Updated section 14.1 : Added a note for Super Users</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>02/21/2018</td>
<td>2.24</td>
<td>Updated section 4.3: Added a note for how reviews are handled when an observation stay spans for two calendar days.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>2/13/2018</td>
<td>2.22</td>
<td>508 Updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/27/2017</td>
<td>2.20</td>
<td>Updated documents per HPS review and updated Care Management Information section.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/15/2017</td>
<td>2.19</td>
<td>Updated version (15.4) information and CERME screen shots.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>5/25/2017</td>
<td>2.18</td>
<td>Document reviewed</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/14/2017</td>
<td>2.17</td>
<td>Updates to document per HPS review</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>3/3/2017</td>
<td>2.16</td>
<td>Changes for IAM SSO Integration</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/7/2016</td>
<td>2.14</td>
<td>Updated reference to MDWS with VIA.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/7/2016</td>
<td>2.15</td>
<td>Updated section 4.6.3: Sensitive Patients. Added few more scenarios where user can see Sensitive Patient Warning screen.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/7/2016</td>
<td>2.15</td>
<td>Updated NUMI VISN, and Site screen</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/7/2016</td>
<td>2.13</td>
<td>Updated InterQual copyright, TOC, Index and completed edits.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/4/2016</td>
<td>2.12</td>
<td>Updates to List of Figures, edits, section and sub-section levels with feedback received from HPS team.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/3/2016</td>
<td>2.11</td>
<td>Minor updates to List of Figures, edits, section and sub-section levels with feedback received from HPS team.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/2/2016</td>
<td>2.10</td>
<td>Created Index for the document from a new template.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>10/28/2016</td>
<td>2.9</td>
<td>Moved document to new template to fix issues with TOC, Table of Tables and List of Figures. Fixed issues with page numbers in the document by updating document footer.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>9/20/2016</td>
<td>2.8</td>
<td>Updated document with feedback from HPS team review. Replaced Chapter 7 entirely with new content and screen shots.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/25/2016</td>
<td>2.7</td>
<td>Removed old text-highlights from NUMI 14.3 version User Guide updates. Updated Appendix B section to reflect reporting link changes and updated training resource website to OQSV. Deleted/updated Appendix F to remove non-relevant sections to NUMI 14.4 application.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>6/28/2016</td>
<td>2.6</td>
<td>Updated Reports Section to reflect NUMI Enhanced Report link changes</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/12/2015</td>
<td>2.5</td>
<td><p>Updated the help link menu.</p>
<p>Added the copyright menu item. Updated the message of the Review save dialog box. Added error message when VistA is down for any unknown reason, instead of invalidating a stay. Updated information on copying an admission review. Added a warning message if reason code is not saved along with review. Removed the old labels for the review types and Admission review types and changed the screenshots accordingly. Removed the section which stated that Report #7 was not capable of doing patient search using initial +4.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/6/2015</td>
<td>2.4</td>
<td>Updated Appendix D and Appendix E. -Provided more clarification for Reports #8 and #9.-Replaced the current Enhanced Reports section entirely with the document provided by Kenneth Monroe.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>5/6/2014</td>
<td>2.3</td>
<td><p>Removed Table of Document Changes to comply with the documentation standards. The Revision table remains as is.</p>
<p>Updated Section 5.6.3 Sensitive Patients. Changed the wording to be more explicit, defining the screen (Utilization Management Review Listing) on which the specific sensitive patient pop-up message appears.</p>
<p>Updated Figure 63 to match changes introduced with v14.1 Criteria Met/Not Met wording.</p>
<p>Updated Figure 192: OQSV Web Page</p>
<p>Updated screen shot to match most recent version of the web page.</p>
<p>Updated Section 17 Online Help Menu. Description wording is changed. Link to VDL turned into a hyperlink.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>8/16/2013</td>
<td>2.2</td>
<td>Updated invalidated stay information in Case 1 in section 5.2.1, removed invalidated stay deletion text from section 5.2.1 and 5.5, removed truncated footnote from section 2.1.12, added paragraph explaining Stay ID, Movement ID and Check-in ID to section 6, changed reference to Chapter 0 to Section 7 in section 6.1.9, changed figure caption for Figure 84, changed footnote 2 to reference the Movement ID field in Section 11.6, removed highlighting section 5.5 and 11.3, removed delete patient stay sentence from section 11.7, removed Invalidated stay removal / delete note from section 11.7, removed section 11.7.2, relabeled section 11.7.3 to 11.7.2</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/14/2013</td>
<td>2.1</td>
<td>Changed invalidated stay note in section 5.6.1.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>7/31/2013</td>
<td>2.0</td>
<td>Added new section 5.1.2 Cell Tooltips, added explanation of source for columns in the last paragraph of section 5.2, added clarification to the patient status in section 5.4.9, changed Days Since Admission explanation in section 5.4.10, added new section 6.1.12 Invalidating a Patient Stay, added explanation and examples of Free Text Searches in section 11.4. Added alt text to figures.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/24/2013</td>
<td>1.9</td>
<td><p>Per VA Feedback from initial submission of Increment 6 User Guide, made the following revisions:</p>
<p>Revised last paragraph of section 5.4.5 for clarity based on VA suggested text. Revised section 5.5 for clarity, regarding automatic dismissal of Initial Treating Specialties.</p>
<p>Added note to beginning of section 6.1.7 indicating that both sections 6.1.7 and 6.1.9 are valid methods of selecting stays for reviews, but instructions in section 6.1.7 are preferred. Updated Figure 97. Updated instruction for printing from the Report Print Preview page for Reports Sections 12.2- 12.11.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/03/2013</td>
<td>1.8</td>
<td><p>Highlighted changes reflect updates per customer feedback:</p>
<p>Deleted section 2.1.3 and Fig 2, deleted the paragraph describing ellipses operation and original Fig 19, updated figure 23 (now Fig 21), changed Figure 26 (now Fig 24) to have an "All" option and changed text correspondingly, section 2.1.22 – Updated all incorrect uses of "CERMe, deleted step 4 of section 5.4.5 and original Fig 28, added text to section 5.4.5 to clarify Filter selection criteria "All" Fig 68 (now Fig 65), corrected capitalization of figure title, moved Fig 63 to section 8.3 and changed Fig 63 to 65 (now Fig 62), updated Fig 70 (now Fig 73), updated Fig 79 (now Fig 76), updated Fig 104 (now Fig 101), updated text in section 12 for all the reports where the manual has PRINT REPORT preview whereas the application only has Print Preview as a choice and added text where needed such that if a user wants to print it they need to right click on the report and click print, updated Fig 120 (now Fig 117) and text referencing this figure in sections 12.2 – 12.10, section 15, changed to Admin Site to Admin Sites, updated Fig 193, (now Fig 190) updated text for step 2 and deleted 3.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>3/28/2013</td>
<td>1.7</td>
<td><p>Highlighted changes reflect updates per customer feedback:</p>
<p>Made changes to cover page to denote v1.1.14.0, Increment 6 added to cover page, Increment 6 removed from footers, Updated section 5.3 to clarify initial default when the new user first logs in to NUMI, updated Fig. 63 to keep the caption with the figure, Section 12.2 updated to explain that CERMe Review Types display inside selection box, updated link for OQSV home page on p. 17.1, added link to VistA Software Documentation Library as a source for user documentation, updated section 2.1.22 to reflect 2012.2, added text to steps in Section 7.8, Updated section 8.11.1, Adm/Atten MD to include parameter on name entry/format, text about duplicate names entry/no titles/characters limit, updated reason codes in Appendix D and E. Also updated Fig. 21 to add Modify button, updated Fig. 23 to no longer show cancel button, updated Fig. 51, updated 53 to show new criteria, updated Figs. 58 &amp; 59 to reflect current 2012.2 criteria, updated Fig. 68 to show reason code example, updated Fig.75 to include physician's name and format guidelines, updated Fig. 105 to no longer show cancel button, updated Fig. 176 to keep the caption with the figure.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>03/06/2013</td>
<td></td>
<td><p>Highlighted changes reflect updated functionality in Increment 6: Section 1.4, added/corrected three features; section 5.2, added/corrected general list of Patient Selection/Worklist features; section 5.5, added/corrected content related to automatic stay dismissal and Dismissal Admission screen, corrected overriding of automatic dismissal job by Dismissal Administration; section 12 (throughout Reports), inserted details re: sorting order with observation reviews.</p>
<p>To support changes in screens related to Section 508 compliance, a note and a new Fig. 62 were added to section 8.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>10/22/2012</td>
<td>1.5</td>
<td><p>Highlighted changes to document in response to addition of the Review Type Dropdown, IOC testing and customer feedback from 10/26/2012:</p>
<p>Review Type Dropdown Updates:</p>
<p>Updated Figure 48, 51, 53, and 55-57 in</p>
<p>section 7 and step #5 of sections 7.11 .1 and 7.11.2 IOC:</p>
<p>IOC Testing Updates:</p>
<p>Added notes re: making the Continue Primary Review button active in section</p>
<p>7.11.1 step #10, section 7.11.2, step #9, bottom of section 7.11.2 and section 7.12, step #1; added details to section 5.4.9 in the third to last and last paragraph to support changes to the Observation calculation.</p>
<p>Customer Feedback Updates:</p>
<p>Added reference to Fig. 23 in section 5.3; added reference to Fig. 34 in section 5.5.1, step #5 of Dismiss Type subsection; updated Fig. 41 in section 6; added reference to Fig. 43 in section in 6.1.6, step #2; Added reference to Fig. 62 in section 8.3; added reference to Fig. 65 in section 8.4; added reference to Fig. 69 in Section 8.8; added references to Fig. 74 and 75 in section 8.11.1; added references to Fig. 88 and 89 in section 8.22; updated Fig. 123 in section 12.2; deleted "Copy Review" erroneously included in list of buttons in step #5 of section 13.3; added reference to Fig. 189 in step #2 of section 15.2; added reference to Fig. 190 in section 15.3, page 15-14 and to Fig. 191 in step #1.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>07/19/2012</td>
<td>1.4</td>
<td>Updated doc for re-release of 14.0 and highlighted changes; per Harris PM, kept highlighting from original 14.0 release: revised Primary Review Screen (Fig. 62) for new Admitting Physician dropdown</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>06/19/2012</td>
<td></td>
<td><p>Updated document per customer feedback/questions from today:</p>
<p>The Version No. column label in the Revision History table should change to Document Version No. per discussion with Stacey Alfieri.</p>
<p>On p. 1-2, there is a reference to OQP, but I believe their name changed to OQSV. Same for Figure 191, pp. 2-10, 17-1, and Glossary.</p>
<p>p. 5-2, first complete sentence on the page describes the possibility where ". . . the page number which the user previously selected no longer exists . . ." but does not explain why that might happen. Please add some explanation.</p>
<p>On p. 5-14, Section 5.5, the first paragraph refers to Section 7.3, but I think it should refer to section 11.3.</p>
<p>p. 5-15 has a sentence "NUMI transmits/sends everything except the above to VSSC." Then there is a list of items that are not counted. Someone with better familiarity with VSSC processing needs to take a look at this. My guess is that the word "above" should be changed to "following," and/or the first bullet point needs to be separated into a description of the bullet points as things that VSSC screens out.</p>
<p>On p. 5-16 the first bullet point under Figure 31 talks about auto dismissal not catching non-reviewable stays because of the naming convention of the treating specialty. Is the auto-dismiss program still dismissing by naming convention as well as treating specialty configuration? (The note on page 5-17 seems to be saying that it is, with configuration over-riding naming convention.)</p>
<p>In various places, Section 5.6.1 refers to colorized patient links on the UM Review Listing and Figure 36 illustrates them but I'm not seeing this feature in v.1.1.14 any longer on any screen. Am I missing something, or is this section outdated?</p>
<p>Section 5.6, at the top of p. 5-21 there is a message text for sensitive patients that does not seem to appear when I click on the patient link for patients with #### in the SSN column in any of the screens. The brief warning in the corresponding figure and another full screen with a similarly worded short warning (warning, restricted record) appear after various actions, but not the longer wording. Please either describe accurately what action on which screen will cause this text to be displayed, or remove it from the manual.</p>
<p>The second sentence in Chapter 6 refers to the Patient Stay History screen as "read-only." Actions like dismissing a stay and initiating a review can be taken from this screen, so please remove the "read-only" phrase so that the sentence begins with "The <em><strong>Patient Stay History</strong></em> screen displays information . . . "</p>
<p>Two bullet items on p. 6-1 refer to RSD items, which is not appropriate for a User Guide. Please remove.</p>
<p>p. 6-5 refers to Chapter 12 for details about Unlocking and Deleting reviews, but that is now in Chapter 6 and 13, and Chapter 12 is for Reports.</p>
<p>Section 5.3 states ("The default is for the 'Include Observations' checkbox to not be selected,") but it was checked most of the time when I brought up the Patient Selection/Worklist screen, including when I had just logged in and the screen came up on p. 7-13, the following sentence refers to section 8.15 for admission information, but admission review types are now described in section 8.18. I think this sentence should be reworded:</p>
<p>FROM: "Please see <u>Chapter 12</u> for more information about reporting and <u>Section 8.15</u> for information about the different types of admissions."</p>
<p>TO: "Please see <u>Chapter 12</u> for more information about reporting and <u>Section</u> <u>8.18</u> for information about the different types of admission reviews."</p>
<p>Also on p. 7-13, a note needs the word "now" removed because this User Guide should not be specific to v.1.1.14:</p>
<p>FROM: At the time a review is created, NUMI will now save three additional data fields captured from CERMe: Criteria Subset, Episode Day of Care, and CERMe version.</p>
<p>TO: At the time a review is created, NUMI will now save three additional data fields captured from CERMe: Criteria Subset, Episode Day of Care, and CERMe version.</p>
<p>I'm not sure what this sentence on p. 7-15 is trying to say. Please reword and correct: "On the <em>Primary Review Summary</em> screen you will complete the review by entering the Day Being Reviewed, the Current Level of Care, entering the Criteria Not Met Elaboration details, and Reviewer Comments, selecting the Selected Reason Description and, if the review does not meet criteria, selecting a Recommended Level of Care and Stay Reason, and selecting a Physician Advisor Reviewer and setting the Next Review Reminder Date Verify that Admitting Physician, Attending Physician, Treating Specialty, Service Selection, Hardware correct."</p>
<p>The following sentence on p. 8-1 is unclear. Why would only "first time reviewers" select an admitting Physician? This same sentence appears again at the beginning of Section</p>
<p>8.11 On p. 8-11. Was the intent that the admission review is where an admitting physician should be selected?</p>
<p>"First time reviewers should select the Admitting Physician from the Admitting Physician dropdown in the stay information section of the Primary Review Summary screen."</p>
<p>The 3rd paragraph in section 8 says "A read-only edit box near Criteria Subset is labeled "Episode Day of Care" and displays the information captured from CERMe." The only place I can find an illustration is in Chapter 9 which has a saved review display but it has "n/a" in that field. Figure 62 does not include the field label because it is not a condition-specific review. A sample review with condition-specific criteria that has Episode Day of Care data would be helpful.</p>
<p>Add to the first paragraph of Chapter 9 that the saved review summary is also accessible from the UM Review Listing screen.</p>
<p>The 2nd paragraph of Section 11.2 refers to Section 12 for information about unlocking, deleting, and copying reviews, but Section 12 is now the Reports Menu. It should refer to Section 13 for unlocking and deleting and 14 for copying.</p>
<p>Please search the manual for references to chapter 12 for Unlocking a review; this is now primarily in Chapter 13.</p>
<p>Section 11.3 says "<u>Section 3.1</u> and <u>Section</u></p>
<p><u>2.1.11</u> describes the use of these filters." However, Section 3 now describes part of the login process.</p>
<p>FAQ section of User Guide:</p>
<p>p. 18-18 refers to Chapter 7 for deleting patient stays, but I think it should be Chapter 11.</p>
<p>p. 18-18 refers to Chapter 4 [Table 7] for unsupported criteria, but this table is now in Chapter 7.</p>
<p>p. 18-18, the first sentence and the next to last FAQ refer to Chapter 7 for info on Manual Synchronization, but that is now in Chapter 11.</p>
<p>p. 18-19 refers to Chapter 5 for changing Attending Physician on a review, but this is now in Chapter 8.</p>
<p>p. 18-20 refers to Chapter 7 for Dismissed Patient Stay info, but his is now in Chapter 11.</p>
<p>p. 1-20 describes a process for dismissing DOM, NH, REHAB and OUTPATIENT stays, and should be replaced by something describing how to use the Treating Specialty configuration so that they are auto-dismissed.</p>
<p>On p. 18-21, the first FAQ under the Working with Reviews section describes functionality that works differently in 14.0. There is no "view" hyperlink any more. You have to click on the patient hyperlink to get to the review display. Also, this paragraph refers to Chapter 9 for info on unlocking a review, and that info is now in Chapter 13.</p>
<p>p. 18-21 has an FAQ on copying reviews ("... complete more than one review at a time . . .") that refers to Chapter 10, but that info is now in Chapters 8, 11 and 14.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>06/18/2012</td>
<td>1.2</td>
<td>Per Harris PM, highlighted changes between release 13.2 and 14.0 in this User Guide for the customer.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/14/2012</td>
<td>1.2</td>
<td>Updated section 5.1.1 to reflect the Modify Filter button and functionality; updated section 15 to list revised Treating Specialties features and updated section 15.3 with revised Treating Specialties details</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/29/2011</td>
<td>1.1</td>
<td>Updated for Release 1.1.14.0: Made general edits, updated screen names, dispersed contents from former section 13 Additional NUMI Information, added functionality updates per SDD, added Document Change Table to document specific changes</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/31/2011</td>
<td>1.0</td>
<td>Removed references to green "Please wait….page is loading" message in Section 3.2.1, as that has been removed from NUMI</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>8/30/2011</td>
<td></td>
<td>Revised Section 7.3 and 13.8 to reflect the 6 month default change to 1 week per revised requirements</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>7/29/2011</td>
<td></td>
<td>Removed some FAQs per Product Support comments</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>7/29/2011 –</p>
<p>8/12/2011</p></td>
<td></td>
<td>Updated document with v1.1.13.1 requirement functionality</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>6/6/2011</td>
<td></td>
<td>Updated Section 8.13.2 with steps for exporting Enhanced Reporting artifacts. Inserted figure depicting Format type selection and Export hyperlink</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>6/2/2011</td>
<td></td>
<td>Updated the document with input from the 6/1 formal peer review discussion</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>5/25/2011</td>
<td></td>
<td><p>Updated document sections 2.1.18, 2.1.19,</p>
<p>Figure 11, 2.3.1.1, 2.1.12, 2.1.13, Table 3,</p>
<p>3.2.1, 7.3 with input from 5/25 formal peer review discussion</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>5/9/2011 –</p>
<p>5/11/2011</p></td>
<td></td>
<td>Updates made to sections 3.3.3, 7.3, 3.2. Replaced various screenshots in the document.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td><p>4/8/2011 –</p>
<p>5/3/2011</p></td>
<td></td>
<td>Made additional updates per 1.1.13 RSD requirements</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/4/2011</td>
<td></td>
<td>Began making updates per requirements in the 1.1.13 RSD</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/1/2011</td>
<td></td>
<td>Updated document with input from the formal peer review discussion.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>3/21/2011 –</p>
<p>3/22/2011</p></td>
<td></td>
<td>Updated per release 1.1.12.1 enhancements</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>3/2/2011</td>
<td></td>
<td><p>Updated sections 8.1 thru 8.10 with updated screenshots and verbiage that reflects the addition of bulletined instructional text on the report filter screens screen. Updated sections</p>
<p>8.11 and 8.12 with updated screenshots</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>2/15/2011</td>
<td></td>
<td>Rewrote section 8.11 and 8.12 and updated screenshots per client requested requirement changes and RSD</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>2/9/2011</td>
<td></td>
<td>Updated document per Formal peer review meeting</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>1/20/2011 –</p>
<p>2/8/2011</p></td>
<td></td>
<td>Updates made per Requirements Specification Document (RSD)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>1/19/2011</td>
<td></td>
<td>Updated Section 3.2 per conference call with C. Heuer and G. Johnson</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>1/13/2011 –</p>
<p>1/18/2011</p></td>
<td></td>
<td>Updated document per 1/12/2011 baseline peer review discussion</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td><p>12/24/2010;</p>
<p>12/28/2010</p></td>
<td></td>
<td>Additional 1.1.12 updates added to the document.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/6/2010</td>
<td></td>
<td>Began inserting information related to release 1.1.12 thru out the document.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>10/19/2010</td>
<td></td>
<td>Inserted verbiage related to Flash Player requirement for CERMe 2010 to Chapters 2 and 4. Inserted Figure of Flash Player message into Chapter 2.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>10/8/2010</td>
<td></td>
<td>Updated document per PIMS feedback</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>10/5/2010</td>
<td></td>
<td><p>Per patch 1.1.11, updated sections 3, 4, 4.2,</p>
<p>4.6, 8.7, 9.1, 9.3, 11.1.6, and 14. Added new sections 4.9 and 4.10.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>8/30/2010 –</p>
<p>8/31/2020</p></td>
<td></td>
<td>Updated Ch. 3, Section 3.1.1 and Figures 16 and 17 to reflect 34 day default date range modification.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td><p>8/24/2010 –</p>
<p>8/26/2010</p></td>
<td></td>
<td>Updated per PIMS input.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>8/9/2010 -</p>
<p>8/13/2010</p></td>
<td></td>
<td>V1.1.10 – modified Chapter 3 to reflect new behavior; removed images of Save For Review Later button; updated Dismissed Stay verbiage to reflect new automated dismissal of "non-reviewable" specialties; updated Chapter 5 to reflect new validation check for blank Review Type.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td><p>5/12/2010 –</p>
<p>5/14/2010</p></td>
<td></td>
<td>V1.1.9 – incorporated information about new 'red text' user messages</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/30/2010</td>
<td></td>
<td>Feedback – added subsection for Paging features to chapter 2. Updated TOC to include changes retroactive to prior iterations of this artifact.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/29/2010</td>
<td></td>
<td>V1.1.9 – updated document per PIMS</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/27/2010</td>
<td></td>
<td>V1.1.9 – updated user tip in section 5.7 related to identification of hospital admission reviews; updated section 6.1 with new screenshots for Physician UM Advisor worklist screen; updated section 7.2 with updated screenshots and descriptive text</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/26/2010</td>
<td></td>
<td>v1.1.9 – Replaced screenshots for screens containing Paging features, History screen Stay Movement and Reviews tables; updated text description information for Reports 1 and 5</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/23/2010</td>
<td></td>
<td>v1.1.9 – updated section 2.1.11 to include behavior change to filter reset functionality</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/22/2010</td>
<td></td>
<td><p>v1.1.9 – updated sections related to modified Paging functionality for Patient Selection, Dismissed Patient Selection and Review Selection screens; updated 3.1.9 with additional screenshot and indication paging links are now within the table grid; updated</p>
<p>3.1.11 to reflect replacement of Go button with Reset Page Size button</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/20/2010</td>
<td></td>
<td>v1.1.9 – added text to Chapter 3 intro and section 7.3 regarding new error message text that will replace the yellow Server Error in '/' Application messages</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/13/2010</td>
<td></td>
<td>v1.1.9 – removed references to Save For Review Later button - has been removed from NUMI; updated Chapter 5 with new required field info on Primary Review screen; added screenshot of new error messages for required fields left blank</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>4/9/2010</td>
<td></td>
<td>v1.1.9 – Updated 31. Text and tip related to new column sort feature and behavior of the Reset button for filters</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>4/1/2010</td>
<td></td>
<td>v1.1.9 – initial document updates begun</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>2/17/2010</td>
<td></td>
<td>v1.1.8 – Update section 7.6; added subsections for new 'paging' functionality on the Patient Selection screen</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>2/16/2010</td>
<td></td>
<td>v1.1.8 - Added instructions for 'Enabling 3rd Party Browsing Extensions to Chapter 2</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>1/25/2010</td>
<td></td>
<td>Revised write-up in section 3.2</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>1/19/2010</td>
<td></td>
<td>Updated Chapter 10 to indicate that Admission reviews are not to be copied</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>10/27/2009</td>
<td></td>
<td>Corrected clinical to chemical sec 13.4</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>9/24/2009</td>
<td></td>
<td>Removed Acute Level of Care Review Process per Heidi Martin.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>9/21/2009-</p>
<p>9/22/2009</p></td>
<td></td>
<td>Updated section 2.2. Removed NUMI Workflow Diagrams</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td><p>9/8/2009-</p>
<p>9/14/2009</p></td>
<td></td>
<td>Updated per EPS and Medora feedback/comments</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>8/24/2009</td>
<td></td>
<td>Incorporated OQP and field test trainee review feedback into the draft. Added Appendix G. Submitted for EPS team review.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/11/2009</td>
<td></td>
<td>Added alternate text to newly added and enhanced screenshots.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>8/7/2009</td>
<td></td>
<td>Finished adding functional, navigation and screenshots information for requirements in the Track tickets. Generated new Index.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/4/2009</td>
<td></td>
<td>Updated document name and footers to reflect reversion to "Release 1.0" identifier</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td><p>7/29/2009;</p>
<p>7/31/2009</p></td>
<td></td>
<td><p>Updated Reports chapter to include revised screenshots. Updated navigation steps and refined some functionality write-ups.</p>
<p>Updated index markers.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>7/24/2009</td>
<td></td>
<td>Updated Patient Selection, History, Primary Review, Reports and Tools screens to reflect new and enhanced functionality in "sweet 16" Track tickets. Updated Section 7.6.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>7/22/2009</td>
<td></td>
<td>Updated Reports chapter to include new reports, screenshots and navigation steps. Updated Section 7.3.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>7/21/2009</td>
<td></td>
<td>Updated screenshots</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>7/20/2009</td>
<td></td>
<td>Modified Reports chapter with 3 new reports and updates to 1 existing report</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>7/13/2009</td>
<td></td>
<td>Updated with placeholders for 16 new requirements; will subsequently update this guide with functionality, navigation steps and screenshots</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>6/1/2009</td>
<td></td>
<td>Initial draft delivered to VA</td>
<td><mark>Redacted</mark></td>
</tr>
</tbody>
</table>
<span id="_bookmark44" class="anchor"></span>Table 1: NUMI Login Screen Features
Table of Contents
[2.12.18 Using the Row Results Display Paging Feature [18](#using-the-row-results-display-paging-feature)](\l)
[2.13 Adobe Flash Player for CERMe [19](#adobe-flash-player-for-cerme)](\l)
[4.7 Viewing Patient Information for Different Sites [48](#viewing-patient-information-for-different-sites)](\l)
[4.7.1 Switching to a Different Site [48](#switching-to-a-different-site)](\l)
[6.6.3 Criteria Met Check Mark [81](#criteria-met-check-mark)](\l)
[6.7 Working with InterQual® Notes [83](#working-with-interqual-notes)](\l)
[7.11.3 To add an Admitting/Attending Physician [109](#to-add-an-admittingattending-physician)](\l)
[7.12 Working with Admission Sources [110](#working-with-admission-sources)](\l)
[10.1 Patient Selection/Worklist Option [128](#patient-selectionworklist-option)](\l)
[10.1.1 To work with the Patient Selection/Worklist [128](#to-work-with-the-patient-selectionworklist)](\l)
[14.1.1 To access the NUMI 'Users' feature [157](#to-access-the-numi-users-feature)](\l)
[14.1.2 Finding VistA Users by Name [158](#finding-vista-users-by-name)](\l)
[Glossary of Terms [179](#_Toc465421563)](\l)
[Appendix A – NUMI Screen Flow [184](#_Toc479676271)](\l)
List of Tables
List of Figures
[Figure 6: Select a Title for the Program window [10](#_Hlk169013752)](\l)
[Figure 7: Windows Security Alert dialog box [11](#_Hlk169013767)](\l)
[Figure 28: Data Management for UM Review Process - NUMI / VSSC [41](#_Hlk169014121)](\l)
[Figure 29: Dismiss Type Dropdown/Dismiss Stay Button [43](#_Hlk169014140)](\l)
[Figure 50: Initial InterQual<sup>®</sup> Criteria screen surrounded by NUMI banner [61](#_Hlk169014362)](\l)
[Figure 51: NUMI Banner above InterQual<sup>®</sup> Criteria screen [61](#_Hlk169014365)](\l)
[Figure 72: Surgical Subset Operative Day Menu [74](#_Hlk169014531)](\l)
[Figure 73: Behavioral Health Level of Care menu [75](#_Hlk169014536)](\l)
[Figure 94: Example of note for Chronic Obstructive Lung Disease [85](#_Hlk169014641)](\l)
[Figure 95: Care Management Information Note Field [86](#_Hlk169014648)](\l)
[Figure 116: Criteria Not Met Elaboration [103](#_Hlk169014857)](\l)
[Figure 117: Reviewer Comments [103](#_Hlk169014866)](\l)
[Figure 138 : Observation Review warning message [116](#_Hlk169015074)](\l)
[Figure 139: Show Reviews table display [116](#_bookmark221)](\l)
[Figure 160: NUMI Patient Stay Administration Screen [142](#_Hlk169015431)](\l)
[Figure 161: Stay retrieval advisory message [142](#_Hlk169015446)](\l)
[Figure 182: NUMI Treating Specialty Configuration Feature [171](#_Hlk169015820)](\l)
[Figure 183: Select Treatment Dismissal Behavior list box [172](#_Hlk169015830)](\l)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide National Utilization Management Integration (NUMI) users with a comprehensive overview of the application, as well as navigation steps for using the various features of each screen. Throughout the guide are tips and additional information for the reader. This information appears in gray highlighted text with the ![](numi-user-guide-version-15-15/002.png) icon.

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document represents a guided tour of the NUMI application. Users are presented with step- by-step navigation instructions and comprehensive information about the many features of the NUMI application, its options and its screens in a 'one stop shopping' format.

### Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is intended for users of different degrees of knowledge and experience with the NUMI application. It is particularly geared towards:

- Veterans Health Administration (VHA) Utilization Management (UM) Staff
- VHA Utilization Review Staff
- NUMI Site Point of Contact (POC)/Administrators (these are UM staff members)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application is a web-based solution that automates utilization review assessment and outcomes. The UM process is a tool used to help ensure that patients are receiving the right care, at the right time, and in the right place.

UM is both a quality and efficiency tool, as it is used to move patients efficiently through the VA system to maximize use of resources. UM reviewers assess patient admissions and hospital stay days using standardized objective evidence-based clinical criteria to determine whether patients meet criteria for acute hospital care.

The NUMI project was established to meet a specific business need. The Office of Quality Safety and Value (OQSV) have a need to provide automation support to field UM nurses that perform reviews of clinical care activities.

These reviews are considered core procedures to support both quality improvement and business/compliance functions central to VA's mission. National UM policy includes review of all admissions and all hospital bed days of care, with a mandate that all review information be entered into the NUMI application.

The NUMI application standardizes UM review methodology and documentation at the facility level and creates a national VHA utilization information database.

In NUMI, patient movement data is obtained from read-only Veterans Health Information Systems and Technology Architecture (VistA) access to pre-populate a patient stay database, eliminating redundancy and errors from manually re-entering patient data.

A Commercial Off-the-Shelf (COTS) product, Change Healthcare Care Enhanced Review Management Enterprise (CERMe), is integrated into NUMI to provide access to the InterQual® standardized clinical appropriateness criteria and algorithms.

The CERMe functionality is used to determine whether patient admissions and hospital days meet clinical appropriateness criteria for acute care hospital care. The national NUMI database is built in Structured Query Language (SQL) and will enable facility, VISN, and national reporting of UM review outcomes.

The NUMI system provides critical functionality to help UM reviewers to organize UM review workload, document UM review outcomes, and generate reports to help identify system constraints and barriers to providing the appropriate services at the appropriate level of care.

NUMI users can perform the following functions:

- Pre-populate patient stay information from VistA into a NUMI SQL database which records patient stay information. UM reviewed outcomes, reasons, and recommended levels of care are saved in the NUMI database.
- Generate a list of patient admissions and hospital days that need to be reviewed to assist UM reviewers in organizing their workload.
- For newly admitted patients, collect patient and treatment information to determine whether patients meet clinical criteria for inpatient admission.
- Following admission, collect treatment information for each hospital day to determine whether patients meet continued stay criteria.
- Standardize documentation of a) reasons for inpatient admissions or continued stays that do not meet clinical criteria for inpatient care, and b) recommended levels of care for admissions and continued stay days not meeting criteria.
- Provide Physician Advisors with an automated UM review list to access reviews, document agreement or disagreement with current levels of care, and add comments and recommendations regarding patients not meeting criteria.
- Generate summary reports of UM outcomes to provide insight into system constraints and barriers and identify quality improvement opportunities.
- Assign specific reason codes for reviews that do not meet criteria. The VA-specific reason code structure will enable UM staff to aggregate and analyze the most prevalent reasons why patients are not meeting criteria at their current level of care. This information provides insight to help identify quality and access improvement opportunities.
- Display a list of patient stays and review information, with filters and search features to assist in organizing individual reviewer workloads.
- Allow the reviewer to filter the display of patients based upon observation status in both Worklists and Reports.
- Allow the Administrator to select the Automatic Dismissal Filter criteria on a per site basis.
- Upon any synchronization, the program shall automatically check the Treating Specialty and other filter parameters for compliance with Automatic Dismissal Filter criteria and if the patient's clinical parameters lie within the boundaries of the filter criteria, that patient shall be dismissed.

The importance of implementing a national automated Utilization Management Program is specifically addressed in The Office of Inspector General (OIG) Report: Healthcare Inspection: Evaluation of Quality Management, VHA Facilities Fiscal Year 2006 (Project No. 2006-00014-HI-0003, WebCIMS 371342).

NUMI was developed to address the Utilization Management data needs of the VHA and to provide the UM staff with a web-based solution for capturing patient information in compliance with VHA DIRECTIVE 2010-021 (Utilization Management Policy).

## User Instructions: Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have been authorized to use the NUMI application and completed the end of the NUMI training session you will be given the NUMI uniform resource locator (URL) address.

This chapter discusses some things to consider before you login for the first time. Subsequent chapters (please see the breakdown in Section [1.2](\l)) will explain the NUMI screens and provide step-by-step navigation instructions for using the various features.

> **NOTE:** If you are unable to change the settings on your computer, please contact your local Information Resource Management (IT) support team for assistance. Tips to help you make the most out of using the NUMI application can be found in Appendix B.

### Allowing Pop-Ups for the Site 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application uses pop-up windows, so it is important that your computer is set up appropriately. If your computer currently has a pop-up blocker, this must be disabled in order to use NUMI effectively (Symptoms you may see that indicate pop-ups are blocked may include: a pop-up blocker bar displaying and indicating pop-ups are blocked; or the

InterQual® Criteria does not open properly; clicking on a review hyperlink in a reviews table does not display the review screen). If you do not have permission to change your pop-up blocker settings, please contact your local IT for assistance. If you do have permission, here is how to double check your pop-up window settings:

1.  Open a new browser (if you have several browser windows open, close all but one).
2.  Select Tools\>Pop-Up Blocker\>Turn Off Pop-up Blocker. NOTE: If the pop up blocker is turned off, Steps 3 and 4 are irrelevant. In order to execute those steps, select Tools\>Pop-Up Blocker\>Pop-Up Blocker Settings and then you can proceed to Step 3).
3.  When the *Pop-Up Blocker Settings* screen displays, *type* the address of the web site into the Address of Web site to allow field.
4.  *Click* the \<Add\> button.
5.  *Click* \<Close\> to exit the screen.
6.  To apply the changes you just made, close your browser and then reopen it.

![](numi-user-guide-version-15-15/003.png)

<span id="_Hlk169013700" class="anchor"></span>Figure 1: Pop-up Blocker Settings

### Making NUMI a Trusted Site 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From your internet browser, select *Tools\>Internet Options*
2.  *Click* the Security tab.
3.  *Click* on Trusted Sites
4.  *Type* in the NUMI URL (The URL will be provided to you after you have completed NUMI training)
5.  Click the \<Add\> button
6.  Click the Apply button
7.  Click the OK button

### Allowing ActiveX Controls for the Site 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to install ActiveX controls, you will see the message bar: "This site might require the following ActiveX control" right below the address line of your browser window. Follow these steps to install ActiveX controls:

1.  *Click* on the message bar to reveal the dropdown menu.
2.  *Click* on "Install ActiveX Control".
3.  When the *Security Warning* window displays, as illustrated in the figure below, click the \<Install\> button. NOTE: You will only need to install ActiveX controls once.

> ![](numi-user-guide-version-15-15/004.png)<span id="_Toc479683256" class="anchor"></span>

Figure 2: Install ActiveX Control dropdown

![](numi-user-guide-version-15-15/005.png)

<span id="_Hlk169013718" class="anchor"></span>Figure 3: Internet Explorer Security Warning Window

### Setting Your Screen Resolution to 1024 x 768 or higher

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To minimize the need for scrolling while doing your reviews, the recommended screen solution when using NUMI is1024 x 768. The screen resolution is changed on the Settings screen. Here are some different ways to navigate to the Setting screen:

1.  From your desktop, *select* Start\>Control Panel\>Display\>Settings OR
2.  From your desktop, *select* Start\>Control Panel\>Appearances & Themes\>Display\>Settings OR
3.  From your desktop, *right-click* and select Properties\>Settings.
4.  *Click and drag* the Screen Resolution bar to 1024x768 or higher.
5.  *Click* the \<OK\> button.

> ![](numi-user-guide-version-15-15/006.png) Depending on which operating system your computer uses, your Settings screen may look different than Figure 4.

![](numi-user-guide-version-15-15/007.png)<span id="_Toc479683258" class="anchor"></span>

Figure 4: Screen Resolution settings

### Making Sure You Have a VistA Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must have a VistA account in order to login to NUMI. If you are using Computerized Patient Record System (CPRS), you already have an active VistA account. Your IT contact at your facility will be able to assist with VistA account issues, or your NUMI POC may be able to help. (Please see Section 2.1.9 for more information about finding out who the NUMI POC at your facility is).

Once you have a VistA account, your access to sites within NUMI will be set up by a NUMI Administrator. (If you will have multi-site access in NUMI, please be aware that the access is completely independent from access to other applications at other facilities including: CPRS, VistA and VistaWeb. Please follow your usual procedure for requesting access to applications outside of NUMI).

### Setting Up Your Internet Browser

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure that the browser you are using is the browser and version currently approved for use in the VA. This is the only browser that will let you access the NUMI application.

If you do not have it installed on your computer, please contact your local IT Support Team for assistance or enable compatibility views under the Tools menu.

### Creating a NUMI Icon on Your Desktop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that you create an icon for the NUMI application on your desktop so that you can access it quickly.

#### To create a desktop icon for NUMI

You can create an icon for NUMI using the Create Shortcut Wizard. Just follow these steps:

1.  Right-click on your desktop and select \<New\>.
2.  Select \<Shortcut\>.
3.  The Create Shortcut Wizard window will open.
4.  *Type* the NUMI URL address into the Type the location of the item field. Click the \<Next\> button.
5.  The Select a Title for the Program window will open.
6.  Enter a name for the shortcut in the Type a name for this shortcut field.
7.  *Click* the \<Finish\> button.
8.  The wizard will close and the icon you just created will appear on your desktop. You should now be able to access NUMI by double-clicking on the icon, or by right-clicking it and selecting the "Open" option.

![](numi-user-guide-version-15-15/008.png)

<span id="_Hlk169013749" class="anchor"></span>Figure 5: Create Shortcut Wizard with NUMI URL

![](numi-user-guide-version-15-15/009.png)

<span id="_Hlk169013752" class="anchor"></span>Figure 6: Select a Title for the Program window

### Launching NUMI from Your Internet Browser

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to being able to access NUMI through an icon on your desktop, you can also launch the application through your internet browser.

#### To launch NUMI using your internet browser

1.  Open your internet browser.
2.  Type the NUMI URL into your browser's address line.
3.  Enter PIV credentials to access NUMI
4.  Select VISN, then Site, Enter Access/Verify Codes, then screen will display.

![](numi-user-guide-version-15-15/010.png) You can have other VistA applications and NUMI open at the same time.

Please note, however, that NUMI will not follow the active patient in other applications such as CPRS, and vice versa. So please be sure you are looking at the same patient for whom you are performing a review.

![](numi-user-guide-version-15-15/011.png) After launching NUMI for the first time, it is recommended that you add the site to your list of browser Favorites.

![](numi-user-guide-version-15-15/012.png) NUMI uses a secured website, identified by the prefix https:// in your browser's address line. It is likely you will see a dialog box, similar to the one illustrated in [the](\l) figure below, the first time you use the site. If you do, click the \<Yes\> button to proceed.

![](numi-user-guide-version-15-15/013.png)

<span id="_Hlk169013767" class="anchor"></span>Figure 7: Windows Security Alert dialog box

### Locating Your NUMI Point of Contact (POC) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As mentioned earlier in this chapter, you will be given the URL to the NUMI application after you have completed NUMI training. You will also be given information about your NUMI Facility Site POC/Administrator. That individual is a member of the UM staff and should be contacted if you need assistance while using the NUMI application (NOTE: The NUMI POC/Administrator is not the same as an IT representative. The NUMI POC/Administrator manages the NUMI account, while IT takes care of VistA and other software and hardware issues). Additional NUMI assistance may be found through NUMI Online Help.

To access NUMI Online Help, click the Help dropdown (located across the top bar of the NUMI screens) to go the OQSV website and select the User Guide option from the Quick Links list.

### Using NUMI Search Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many NUMI screens offer a variety of filters that you can use to search for patients and other information. You can select multiple filters if you wish to refine your search to a more detailed level. Here are general instructions for using filters:

1.  First, activate the filter you wish to use by clicking on the checkbox in the filter header. Then…
2.  If the filter is for a beginning and ending date range (e.g., Reminder Date), or for other date fields such as Admission, Discharge, or Review, choose a date by *clicking* on the calendar icon, or by manually *typing* a date in. When manually *typing* a date in, be sure to use the format mm/dd/yyyy.
3.  If the filter is for a Dropdown box, choose an option from the dropdown by *clicking* on it
4.  If the filter is for List of items, single *click* on an item in the list. In some cases you may be able to *control-click* to select or deselect multiple independent items, or *shift-click* to select a range of items. This will depend on the particular field.
5.  If the filter is for a Text Entry field, *type* the information you wish to search for into the text entry field. The format in which you can enter data in these fields will depend on the field.
6.  If the filter contains other checkboxes, *click* on one or more checkboxes.
7.  If the filter contains radio buttons you may select one of the options.
8.  In most cases, at the bottom of the filter bank you will need to *click* the \<Find\> button to see any changes in the information that is displayed – although in some cases the page will be updated immediately.

> NOTE: After performing a search (on the *Patient Selection/Worklist*), if you click on the \<Reset\> button, your filter selections will be set to their initial default state and when the screen is re-loaded, the Reminder Date checkbox will once again be selected and display default information. For more information about NUMI filters, see Section 4.4.

### Using NUMI Hyperlinks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI offers a variety of hyperlinks1 that will quickly redirect you to other screens and information. Hyperlinks can be found in NUMI data displayed in table format. Some tables will be closed when the screen first displays, and must be opened (e.g., the Show Reviews button on the *Patient Stay History* screen will open the Reviews table). Here are general instructions for using hyperlinks:

1.  While viewing a table, *click* on the hyperlink beside the desired patient or information. For example, clicking on this hyperlink would automatically take you to the *Patient Selection/Worklist*.
2.  The link will take you to another location in the NUMI application (e.g., clicking on the patient's name in the *Patient Selection/Worklist* will take you to the *Patient Stay History* screen).
3.  Depending on the hyperlink, it may perform different functions depending on the status of a patient or review, and on your user access privileges.

### Displaying Information in NUMI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI offers the ability to sort information in the tables on the application. If the content of the page is changed by resetting the page size or clicking the <u>Next</u>, <u>Previous</u>, <u>Last Page</u> or <u>First Page</u> hyperlinks, the sort does not need to be re-done. [^1]

Here are general instructions for using the sort feature:

1.  Click on an underscored column header in the table (e.g., Patient Name on the *Patient Selection/Worklist*).
2.  The screen will refresh and the information will be sorted in ascending order.
3.  Click on the header again to refresh the screen and change the display to descending order.

#### Using NUMI Buttons

NUMI displays a series of buttons that, when clicked, will display additional information. Here are the different ways in which clicking a button feature works:

1.  Takes you to another screen (e.g., on the Patient Stay History screen, the Patient Selection, CERMe and Primary Review buttons navigate to other screens).
2.  Displays a pop-up window (the Patient Worksheet button on the *Patient Stay History* screen opens a window containing a worksheet with Stay information for a patient).
3.  Displays informational text (e.g., the Notes icon button ![](numi-user-guide-version-15-15/014.png) on the *InterQual*® *Criteria* displays read-only InterQual® Notes information).
4.  Expands and collapses fields (e.g., the + and – Stay 'toggle' buttons on the *Patient Stay History* and *Primary Review Summary* screens, expand and collapse the list of Stay Reasons).

#### Using NUMI Radio Buttons

Some NUMI screens contain 'radio' button ![](numi-user-guide-version-15-15/015.png)

Here are general instructions for using those:

1.  *Click* on the desired radio button to select that option.

#### NUMI Screen 'Tabs'

> ![](numi-user-guide-version-15-15/016.png)

Some NUMI screens contain tabs when clicked, will take you to other NUMI screens. Certain buttons may be grayed out, depending on which screen you are working on. Here are general instructions for using tabs:

1.  While on a screen that displays tabs (e.g., the *Patient Stay History* screen) click on a tab.
2.  You will be redirected to the tab of the corresponding screen.

#### NUMI Menus

NUMI provides menus, which are accessible from the major NUMI screens. These menus provide access to various features of the NUMI application.

#### Administrator (Admin) Menu

The Admin Menu is only available to NUMI Administrator users.

Non-administrator users will see this menu option on the Graphical User Interface (GUI); however, its dropdown menus will be disabled. If Administrator users have problems using this menu or its features, validate that their profile indicates they have the appropriate access privileges. Please see Chapter 14 for more information about this menu.

#### Reports Menu

The Reports Menu is available to all NUMI users and links to the separate Enhanced Reports system which includes its own help options. These reports are generated on-demand. Please see Chapter 11 for more information about this menu.

#### Tools Menu

The Tools Menu is accessible to all NUMI users. However, the accessibility of certain options is based on individual access privileges. Please see Chapter 10 for more information about this menu.

#### Help Menu

Online help for NUMI functionality consists of a Help Menu option on the major NUMI screens. The only option under this menu is *User Guide*. Selecting the option opens a new webpage to the main OQSV web page, where they will have hyperlinked access to view the latest version of the *NUMI User Guide.* Please see Chapter 16 for more information about this menu.

#### Using Screen 'Bars'

Some NUMI screens contain gold-trimmed bars ![](numi-user-guide-version-15-15/017.png) that, when clicked, will display or hide the information in the NUMI tables on that screen. Here are general instructions for using bars:

1.  While on a screen that displays bars (e.g., *Patient Stay History* screen), *click* on a bar.
2.  The corresponding table for that bar will either display or be hidden, depending on whether the "Show" or "Hide" bar was selected.

#### Using Sidebars

Some screens contain sidebars. The sidebar on the *InterQual* ®*Criteria* in NUMI is a good example of one.

A sidebar is an auxiliary box of information, appearing next to the main information on a screen that may contain functional rows or items that can be clicked or selected.

> ![](numi-user-guide-version-15-15/018.png)

<span id="_Hlk169013831" class="anchor"></span>Figure 8: Sidebar

#### Using Scrollbars

Throughout the NUMI application, you will find scrollbars (the figure below shows an image of the scrollbar that appears on the right-hand side of the *InterQual*® *Criteria*). A scrollbar is a long rectangular area containing a bar that can be dragged to scroll up, down, left or right. Depending on the screen, the scrollbar can be horizontal or vertical.

![](numi-user-guide-version-15-15/019.png)

<span id="_bookmark34" class="anchor"></span>Figure 9: Scrollbar

![](numi-user-guide-version-15-15/020.png) While working in NUMI, if you use the BACK button on your browser instead of one of the screen tabs or the Tools menu, you may get an error message. Always navigate around NUMI using the tabs or the Tools menu and you will avoid error messages and delays.

#### Using NUMI Dropdown Boxes

Some NUMI screens display dropdown boxes that contain selectable options, similar to this example: ![](numi-user-guide-version-15-15/021.png)

To choose an option from a dropdown, c*lick* on the down arrow to display the list of options. Select the desired option by *clicking* on it.

#### Using NUMI Paging Features

The *Patient Selection/Worklist*, *Dismissed Patient Stays* and *Utilization Management Review Listing* screens contain paging features that allow you to navigate thru lists of information in the tables. When these screens first open and you use NUMI's filters to search for information, the results table will display the first 30 rows of results. You can navigate thru each screen of results by selecting the <u>Next</u>, <u>Last Page</u>, <u>Previous</u> and <u>First Page</u> pagination hyperlinks. If you wish to see more than 30 rows of results at a time, just type in a different value and click the reset page size button.

As long as the screen remains open, the system will continue to display the number of rows in the result table that you specified. However, once you close the screen and reopen it, your search results will once again default back to display the first 30 rows of results. The sections below explain how to use each paging feature.

#### Using the Next and Previous Page Paging Features

When you open a screen that contains paging features, <u>Next</u> and <u>Last Page</u> hyperlinks will display within the table grid. If you are already on the first page, you will not see a <u>Previous</u> link. Similarly, if you are already on the last page, you will not see a <u>Next</u> link (the figure below illustrates the screen with all paging links displayed).

![](numi-user-guide-version-15-15/022.png)

<span id="_Hlk169013848" class="anchor"></span>Figure 10: NUMI Paging Hyperlinks

#### To use the Next and Previous Page features

1.  From any page but the last page, *click* the Next hyperlink.
2.  The next page of results will display and a Previous hyperlink will become visible at the top and bottom of the table.
3.  *Click* the Previous hyperlink.
4.  The previous page of results will display.

#### Using the First and Last Page Paging Features

If you are already on the first page, the Next and Last Page links will display. Likewise, if you are already on the last page, the First Page and Previous links will display.

#### To use the First Page and Last Page features

1.  From any page but the first page, *click* the First Page hyperlink.
2.  The first page of results will display OR
3.  *Click* the Last Page hyperlink.
4.  The last page of results will display.

#### Using the Row Results Display Paging Feature

To specify how many result rows you want to see in the table

1.  Type the number of result rows you want to see in the Page Size field (NOTE: The default is 30.)
2.  Click the \<Reset Page size\> button.
3.  The screen will refresh and display the number of rows you specified for each page in the table, and the total number of pages in the listing will change according to the change size you specified.

### Adobe Flash Player for CERMe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CERMe InterQual® Criteria are loaded into NUMI. CERMe requires the use of a Flash Player and expects that your desktop has Flash Player installed (It is likely that you already have Flash Player installed, because it is part of the standard desktop package for VA employees. If you are not certain whether you have Flash Player, please contact your local IT representative or your NUMI POC for assistance). If your desktop does not have Flash Player, a reminder screen will display when you try to access CERMe.

This message cannot be disabled, as it is part of the Change Healthcare CERMe core package. Just click the OK button to close this message and proceed into CERMe to complete your review (Flash Player is used for a CERMe insurance screen that NUMI does not utilize, so you will be able to use CERMe).

![](numi-user-guide-version-15-15/023.png)

<span id="_Hlk169013870" class="anchor"></span>Figure 11: Adobe Flash Player Dialog Box Select

## National Utilization Management Integration (NUMI) Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the *NUMI Login* process. This is where you sign-in with your VA PIV Card and pin number.

### VA Single Sign-On Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first page that you will see when you open the NUMI application in a browser is the VA Single Sign-On (SSO) login screen, shown in the figure below.

Click on, "Sign-In with VA PIV Card." You will be presented with a certificate selection screen.

![](numi-user-guide-version-15-15/024.png)  
<span id="_Hlk169013877" class="anchor"></span>Figure 12: VA SSO Login

Select the correct certificate (same as you use to login to your VA computer) and click on OK. Then you will be prompted to enter the PINFigure 14.

![](numi-user-guide-version-15-15/025.png)

<span id="_Hlk169013882" class="anchor"></span>Figure 13: SSO PIV Certificate selection

Enter your PIN and click on OK to complete the Identity and Access Management (IAM) login. On successful authentication of the PIV card the user will be directed to "*Patient Selection/Worklist"* screen.

![](numi-user-guide-version-15-15/026.png)

<span id="_Hlk169013885" class="anchor"></span>Figure 14: SSO PIN Entry

### NUMI Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|  FEATURES                           |
|-----------------------------------------|
| Select Sign-In with VA PIV Card         |
| Enter PIV Pin Code                      |
| Secure Token Service Integration        |
| Access/Verify Code Login See Appendix H |

<span id="_Hlk169013966" class="anchor"></span>Table 2: Patient Selection/Worklist Features

#### Secure Token Service Login Integration

Users must link their PIV cards with their local facility VistA account before logging in to NUMI.  To set up your account, please follow the directions in the [ServiceNow Knowledge Document (KB0013359 v10.0](https://yourit.va.gov/nav_to.do?uri=%2Fkb_view.do%3Fsys_kb_id%3D1ba32049dbe7b704a885362f7c9619fe)).  The Knowledge Document will direct you to go to this link, [IAM Provisioning Services](https://mvitkssoi.iam.va.gov/imdquiWeb/login.do), and select the left hand navigation link that says "Link VistA User."

#### Login Issues

Users who have not linked their PIV cards with their home site in NUMI will be redirected to the fallback login process via ACCESS/VERIFY codes. The full instructions are listed in Appendix H of this document.

The following STS-related error messages may appear on the ACCESS/VERIFY screen and can help troubleshoot common NUMI Secure Token Service related issues.

- User has no sites linked to their PIV. Provision the site with link above.

*User not provisioned in STS.  Please provision your site to bypass ACCESS/VERIFY login*

- User has at least one site, but not the site they're set up for in the NUMI application. The site code shown needs to be provisioned with the link above.

  *Users homesite: NNN in NUMI not a provisioned site in STS.*
- User hasn't been set up in NUMI yet, or their VHA username has changed and needs updating inside NUMI.

  *User network credentials not found in NUMI*.

#### Session Timeout

#### Timeout due to Inactivity

After 15 minutes of inactivity, a dialog box with an audible "beep… beep… beep… beep… beep" will display at the top of the screen with a countdown timer set for 5 minutes and the message. If the OK button is clicked within the 5 minutes, you will be returned to the last screen you were on in NUMI. NOTE: If the OK button is not clicked before the 5 minutes elapse, the system will log you out of NUMI, but your browser will remain open.

![](numi-user-guide-version-15-15/027.png)

<span id="_Hlk169013911" class="anchor"></span>Figure 15: Session Idle Message

### Application Problem Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA will lock your Access and Verify Codes after the maximum number of permitted login attempts is exceeded. VistA will automatically unlock your Access and Verify Codes after 20 minutes and you may try to login again. See Section 3.2 for more information.

![](numi-user-guide-version-15-15/028.png) While working in NUMI, if you use the BACK button on your browser instead of one of the screen tabs or the *Tools* menu, you may get an error message. Always navigate around NUMI using the tabs or the *Tools* menu and you will avoid error messages and delays.

![](numi-user-guide-version-15-15/029.png)

<span id="_Hlk169013917" class="anchor"></span>Figure 16: Generic Error Message

## Patient Selection / Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the *Patient Selection/Worklist.*

If you have rights to create and conduct primary reviews or are a super user, this is the first screen that will appear after you successfully complete the login process. The top section of the screen will show a drop-down list of sites to which you have access.

This screen is where UM Reviewers will search for patient stays, select patients for review, assign and reassign reviewers, and view patient information for different sites (if they have permission to visit multiple sites). The features of this screen are listed in Table 2.

When the screen first opens you will see the search filters, but no patient data rows will automatically display. You will see instructions for using the filters to obtain search results, and the Date filter will be pre-selected and pre-populated with a 34-day default date range (You may click the \<Find\> button to display the last 34 days of stays in the table, or enter different or additional filtering criteria, then click the \<Find\> button).

### Accessing Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### General Search Information 

After you select the search criteria and perform a search on the Patient Selection/Worklist, the resulting screen will not display the original select criteria controls. Instead, an unmodifiable summary of the search criteria will display. This summary includes the date and time of the last synchronization with VistA for this site, and the date and time of the most recent generation of this worklist.

A button called "Modify Filter" can be used to display your last search criteria controls and select different search criteria. If the Reset button is clicked, the default search filters are displayed.

Upon performing a search, the resulting worklist will display one row per patient with at least one stay matching the search criteria.

Displayed row details will represent the most recent stay that meets the search criteria of one or more patient stays, displayed in the format illustrated in the figure below. Search criteria that are different from the default criteria will remain effective when you leave the Patient Selection/Worklist and return to it as long as you remain logged in.

To select a patient for review, click on their hyperlinked name in the Patient Name column.

#### Cell Tooltips 

Sometimes the information for a given cell in the Patient Selection/Worklist will not entirely fit into the cell. When this happens ellipses (…) will appear in the cell. Hover the mouse over the cell to show the complete value for the cell.

### General Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Links</u>: When an active link is selected (e.g., a <u>Patient Name</u> hyperlink is clicked) and you leave the *Patient Selection/Worklist* and then return to it, the original sort order will be retained and you will be returned to the original page display of the worklist.
- <u>Other Pages in NUMI</u>: When you leave the *Patient Selection/Worklist* to view another screen, link or report (e.g., Dismissed Patient Stays is clicked) and you return to the *Patient Selection/Worklist*, the sort order will be retained on the worklist and you will be returned to the original page displayed in the worklist.
-  Additionally, the sort order will be applied when searching on new criteria. After navigating to different pages in the worklist, when you return to the first page (i.e., Page 1) the sort order will be retained and displayed. If other users discharge patients in the interim between visits to the *Patient Selection/Worklist*, this will affect your existing search results and cause a re-sort which may invalidate the current page number. If this is the case, the page number previously shown will be set to the final page in the *Patient Selection/Worklist*. If the user re-searches with new criteria, the page number will be set to the first page.
- <u>Pagination</u>: When the filter selections are made and displayed on the worklist and multiple pages exist, you will still be able to click on the <u>First Page</u>, <u>Next</u>, <u>Previous</u> and <u>Last Page</u> hyperlinks to navigate through the results.

Depending on how refined your search is it may take a few seconds for the bottom part of this screen to load, showing the patient stays for the site. Please be patient to allow this screen to load completely before changing sites or clicking on filters.

The Patient Selection/Worklist displays an "X" column and clicking any boxes in the column will flag those stays for dismissal. The Patient Selection/Worklist includes functionality that lets you distinguish dismissed stays for patients in non-reviewable specialties. Please see Section [4.5.2](\l) for more information. The Patient Selection/Worklist also includes the dismissal and review assignment controls available at the top and bottom of the worklist.

> **IMPORTANT:** Each row in the Patient Selection/Worklist represents a patient/admission. The patient stay row will have several information fields including: Patient Name, SSN, Specialty, Ward, Attending, Admitting Diagnosis, Admit Date, Date of Last Review, Met (i.e. whether that review met criteria), Reason Code, Reason Description, Criteria Subset, Episode Day of Care, Next Review Date, D/C (i.e., discharge date), Reviewer and Status.

To make it easier to see the individual rows in the table, the background of each row alternates in color between white and shaded. The table will also show you last Specialty, Ward and Attending for each patient, taken from the patient stay record.

#### Information Feeds from VistA

NUMI obtains Admissions, Ward transfers, and Discharge movements from VistA on an hourly basis during the daytime (i.e., at the top of each hour) and resynchronizes other movements at Midnight (local time) each night. Therefore, it is possible that some stays may not be in NUMI yet, or have not been updated yet.

Reviewers may also see stays that have Transfers and Discharges, even though they have not had a chance to do an Admission review yet. After the midnight synchronizer information feed occurs, most stays that were dismissed the previous day will not display again in the worklist. Certain stays can be undismissed using the *Dismissed Patient Stays* screen by clicking on the patient name hyperlink and entering a review.

Stays will be updated by the synchronizer when it detects that a stay has changed. This includes stays that have been dismissed or that have had continuing stay reminders set by the reviewer (The purpose of this is to alert a reviewer that there has been a movement. Whether or not it is of sufficient clinical significance to warrant a review before the scheduled reminder is at the discretion of the reviewer).

For situations where a patient is not in the NUMI database and needs to be loaded manually, please see <u>Section 10.6</u>, which describes how to use the Manual VistA Synchronization feature to manually synchronize information from VistA into the NUMI *Patient Selection/Worklist*.

The NUMI system detects:

- Case 1: Stays deleted in VistA but still in NUMI

When a stay is invalidated - meaning it is not in VistA but is still in NUMI - and the stay is selected for review, the system will move it to the *Dismissed Patient Stays* screen and the *Patient Stay Administration* screen. If you select the stay from the *Dismissed Patient Stays* screen it will not be restored. It will only be restored if the stay was an unintentional dismissal by a NUMI reviewer.

For the Case 1 scenario, this is the message that will display when a user selects a stay that has been deleted in VistA but is still in NUMI: "The patient stay you have selected appears to have been deleted from VistA. Stay ID: \<stay number\>. This patient stay has been moved to the Patient Stay Administration screen."

- Case 2: Stays not retrieved from VistA for one of the 4 reasons below. Should you get one of these messages, you may need to contact your local IT to find out if there is a problem with VistA connectivity or local network issues.
  - VistA Integration Adapter (VIA) timed out before it returned the stays from VistA
  - VIA service is unavailable
  - VIA could not connect to VistA because the VistA node is unavailable
  - VIA could not connect to VistA because VistA is down for unknown reasons

For the Case 2 scenario, a notification with the following message will be displayed: "Stay \<stay number\> for patient \<patient name\> cannot be retrieved from VistA as the server is busy at this time. Please try again." On clicking OK on the message, the following message will be displayed on the NUMI UI.

<span id="_Hlk169013960" class="anchor"></span>

Figure 17: VistA is unreachable

![](numi-user-guide-version-15-15/030.png) While working on the screen, you may see a message in red text advising there was a problem loading the web page. Refreshing your browser will reload the web page and display the NUMI screen.

![](numi-user-guide-version-15-15/031.png)

<span id="_Hlk169013964" class="anchor"></span>Figure 18: Page load error message

| FEATURES                                     |
|----------------------------------------------|
| Include Observation Stays                    |
| Use Filters and Paging Features              |
| Find Patients By Category                    |
| Dismiss a Reminder for a Patient Stay        |
| Select a Patient for Review                  |
| View Patient Information for Different Sites |
| Assign/Reassign Reviewers to Patient Stays   |
| Distinguish Stay Dismissals                  |

<span id="_Hlk169014263" class="anchor"></span>Table 3: Patient Stay History Features

![](numi-user-guide-version-15-15/032.png)

<span id="_Hlk169013978" class="anchor"></span>Figure 19: Patient Selection/Worklist with 34-day default

![](numi-user-guide-version-15-15/033.png)

<span id="_Hlk169013980" class="anchor"></span>Figure 20: Patient Selection/Worklist with search results

### Include Observations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stays or reviews can be listed with or without Observation stays or reviews depending on whether you select the "Include Observations" checkbox (The default for a new user is for the "Include Observations" checkbox to not be selected. The OBS checkbox will remember the last setting even after logging out and back into NUMI. If at any time you choose to include observations, this selection will be your new default the next time you log in.

![](numi-user-guide-version-15-15/034.png)<span id="_Toc479683278" class="anchor"></span>

Figure 21: Patient Selection/Worklist including Observations checkbox

> If you select the "Include Observations" checkbox, any Observation stays or reviews will always precede any non-observation reviews or stays, regardless of other sorting selections you make.

> Once selected, the Include Observations checkbox will remain effective when you leave the *Patient Selection/Worklist* or other screens and return to them, and when you log back in. The "Include Observations" checkbox can be found on the following screens:

- Patient Select Screen
- Review Select Screen
- Dismissed Stay Patient Select Screen
- Free Text Search
- Patient Stay Admin

![](numi-user-guide-version-15-15/035.png) An observation stay of 48 hours or less may span two calendar days; however, only one review is required for the observation stay. The 2nd day will not be counted in the VISN Support Services Center (VSSC) data due to a business rule that only counts one.

### Using Filters and Paging Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI offers filters and paging features so you can navigate thru the list of patients quickly and conveniently. Additionally, all columns in the list can be sorted in ascending or descending order by clicking on the column headers.

![](numi-user-guide-version-15-15/036.png) The filters on NUMI screens are additive. This means you can select several filters in order to get very specific search results. After performing a search, if you click on the \<Reset\> button, your filter selections will be cleared and when the screen is re-loaded the Reminder Date checkbox selected and default information redisplayed. While additive filters can be helpful if you need to, for example, look at a specific set of Reminder Dates for a specific Ward in a specific Date range, it is possible to create such precise (and even mutually exclusive) criteria that no records will be found in NUMI. This is something to be aware of when using multiple filters. For more information about using NUMI filters.

#### Finding Patients by Patient Category

You can specify which types of patients will be displayed in your search by selecting the following radio button options from the Patient Category filter:

- Patients Pending a Review: Includes patients with undismissed stays that still have an un- reviewed admission or bed day of care.
- Patients Currently in Beds: Include patients with dismissed and undismissed stays, but not discharged patients.
- Patients with undismissed Stays: Includes patients with undismissed stays.

![](numi-user-guide-version-15-15/037.png)

<span id="_Hlk169014002" class="anchor"></span>Figure 22: Patient Category Filter

#### Finding Patients Using the Reminder Date Filter

As mentioned in the Patient Selection/Worklist introduction, when the *Patient Selection/Worklist* first opens the Reminder Date checkbox will be pre-selected, as will the Start Date and End Date checkboxes, and a 34 day range will be pre-populated. The default Start and End dates will always appear as the last 34 days, but each time they appear on the screen, you can edit them as desired (See Section 7.9 for more information about Review Reminder Dates). Use this filter to search for patients based on review reminder dates.

#### To find patients by reminder date

1.  *Click* on the Reminder Date checkbox to activate the filter, if it is not already selected.
2.  *Click* on the Start Date checkbox.
3.  *Click* in the Start Date textbox and type the desired Start Date in mm/dd/yyyy format, or scroll through the calendar and click the desired Start Date in the calendar.
4.  *Click* on the End Date checkbox.
5.  *Click* in the End Date textbox and type the desired End Date in mm/dd/yyyy format, or scroll through the calendar and click the desired End Date in the calendar.
6.  *Click* the \<Find\> button. A list of patients for the date range you specified will display. The results will include <u>all</u> movement types (e.g. Admissions, Discharges, etc.).

![](numi-user-guide-version-15-15/038.png)

<span id="_Hlk169014013" class="anchor"></span>Figure 23: Reminder Date filter

#### Filtering by Reviewer

When the reviewer checkbox is selected, the *Patient Selection/Worklist* will populate the reviewer filter with the current user's login name in the Reviewer drop-down section of the screen. You can also use this filter to search for patients by another specific reviewer name, by "all" reviewers, and sorting by the Reviewer column when the results appear will list those with no assigned reviewer on top.

#### To filter by Reviewer

1.  *Click* on the Reviewer checkbox to activate the filter.
2.  Select the defaulted reviewer name and *click* the \<Find\> button. OR
3.  Select another reviewer in the dropdown by *clicking* on their name, and click \<Find\>. OR
4.  *Click* on \<All\> in the dropdown and then \<Find\>, to view stays that have been assigned to all reviewers.

![](numi-user-guide-version-15-15/039.png)

<span id="_Hlk169014023" class="anchor"></span>Figure 24: Reviewer filter with "All" option selected

![](numi-user-guide-version-15-15/040.png) To select multiple reviewer dropdown options, click on the first option, then press and hold the Ctrl key down on your keyboard and click on the other options you are interested in. You may also press and hold the Shift key down and select a block of options.

#### Finding Patients Using the Ward Filter

Use this filter to search for patients by specific Ward location.

![](numi-user-guide-version-15-15/041.png)

<span id="_Hlk169014028" class="anchor"></span>Figure 25: Ward Filter

#### To find patients by single Ward

1.  *Click* the Ward checkbox to activate the filter.
2.  *Click* on the desired Ward.
3.  *Click* the \<Find\> button.

#### To find patients by multiple Wards

1.  *Click* the Ward checkbox to activate the filter.
2.  *Click* on the first Ward. *Press and hold* the \<Ctrl\> key down on your keyboard and *click* on the other Wards you are interested in. You may also *press and hold* the \<Shift\> key down and select a block of Wards, or *click* \<All\> to choose all Wards.
3.  *Click* the \<Find\> button.

![](numi-user-guide-version-15-15/042.png) There may be instances where you may expect to see a particular ward in the Ward dropdown, but it does not display. Ward lists are populated as movements for those wards occur. For example, for a patient that requires a ward not listed in the dropdown, you can use the Manual VistA Synchronization feature (see Section 10.6 for more information) to search for a patient that you know is in a particular ward. Once their information has been synchronized and pulled into NUMI, that ward will display in the Wards dropdown.

#### Filtering by Service or Treating Specialty

Use this filter to search for patients by a particular Service or Treating Specialty, or a combination of both (e.g., Service = *Medicine* and Treating Specialty = *NHCU \[ECU\]*).

#### To filter by Service or Treating Specialty

1.  *Click* on the Treating Specialty and Service checkbox to activate the filter.
2.  Select options from the Treating Specialty window by *clicking* on them, and then click the \<Find\> button. OR
3.  *Click* the \<All\> option, then \<Find\>, to search by all Treating Specialties).
4.  Select options from the Service dropdown by *clicking* on them.
5.  Click the \<Find\> button.

![](numi-user-guide-version-15-15/043.png) To select multiple specialty dropdown options, click on the first option, then press and hold the Ctrl key down on your keyboard and click on the other options you are interested in. You may also press and hold the Shift key down and select a block of options.

![](numi-user-guide-version-15-15/044.png) If you select filters that are contradictory, it could result in partial or zero results found. For example, if you choose a Psychiatry Service and a General Surgery Treating Specialty, you will probably not get any results back. So, to filter by a specific Service, select the service but leave the Treating Specialty set to "All." Or, if you want to filter by a specific Treating Specialty only, select the specialty but leave the Service filter set to "All."

#### Filtering by Movement

Use this filter to search for patients by Movement type. This refers to any movement that the patient has undergone while at the hospital and includes Admissions, Continued Stays, Discharges and Transfers.

#### To filter by Movement Type

1.  *Click* on the Movement checkbox to activate the filter on the *Patient Selection/Worklist*).
2.  *Click* on the desired Movement checkboxes.
3.  *Click* the \<Find\> button.

![](numi-user-guide-version-15-15/045.png)

<span id="_Hlk169014056" class="anchor"></span>Figure 26: Movement filter

![](numi-user-guide-version-15-15/046.png) NOTE: If you wish to find missing hospital admission review records (i.e., stays with no reviews) you can sort by the Date of Last Review column by clicking on the column title.

#### Finding Patients Using the Patient Search Filter

The Patient Search selection filter is illustrated in the figure below. NUMI uses VistA's search capabilities to look for a patient. A list of possible matches will be shown in the lower window. The reviewer selects one of those patients and NUMI searches its database to see if there are any stays for that site/selection combination. Use this filter to search for patients by Name or Social Security Number.

![](numi-user-guide-version-15-15/047.png) Because twins and other patients can have the same or similar names, it is strongly recommended that you search for patients using their full Social Security Number. This will confirm the identity of the patient.

![](numi-user-guide-version-15-15/048.png)

<span id="_Hlk169014063" class="anchor"></span>Figure 27: Patient Search Filter

#### To find patients by Full Social Security Number (SSN)

1.  *Click* the Patient Search checkbox to activate the filter.
2.  Type the patient's full SSN in the Find Patient field (in xxx-xx-xxxx OR Xxxxxxxxx format).
3.  *Click* the \<Find Patient\> button.
4.  When the patient whose SSN matches your search criteria displays in the result window, *click* on the patient's name and the stays stored in NUMI for that patient will be displayed in the table, unless they have been dismissed or other filtering criteria selected has filtered them out. Dismissed stays can be found on the *Dismissed Patient Stays* screen (See Section 10.3 for more information).

#### To find patients by Last Name

1.  *Click* the Patient Search checkbox to activate the filter.
2.  Type the patient's Last Name in the Find Patient field (You can further refine your search by entering the patient's First and Last Name).
3.  *Click* the \<Find Patient\> button.
4.  When the list of patients displays in the result window, *click* on a patient name and their information will be populated in the table on the screen.

#### To find patients by First Letter of Last Name and Last four digits of the patient SSN

1.  *Click* the Patient Search checkbox to activate the filter.
2.  Type the first initial of the patient's last name, followed by the last 4 digits of their SSN (e.g. *W0000*) in the Find Patient field.
3.  *Click* the \<Find Patient\> button and the patient information will display in a table. Finding patients this way may initially bring back a list of names because this lookup method is not necessarily unique.

#### Reset Button

After obtaining search results on the Patient Selection/Worklist), when you click on the Reset button the system will restore all fields to their default values. The fields and default values are:

- Patient Category – Patients with undismissed Stays
- Reminder Date – Checkbox selected and defaults with a 34-day range
- Reviewer – Checkbox not selected and will display the logged in user's name
- Ward – Checkbox not selected and defaults to All
- Treating Specialty and Service – Checkbox not selected and defaults to All
- Movement – Checkbox not selected and no default values display
- Patient Search – Checkbox not selected and no default values display
- Include Observation checkbox – selected if selected in user's last filtering criteria

#### Patient Status Column

In cases where the most recent stay for a patient is a non-observation stay, the Status column on the right side of the *Patient Selection/Worklist* may provide some combination of the following:

- Green text appears if the patient is up-to-date on reviews and no new movement information has been detected since the last review.
- Blue text appears if the patient is behind on reviews (i.e., there are bed days of care, for which there are no saved reviews), or a review has been performed on the patient's discharge date.
- Red text appears if the patient has more than one undismissed stay.

When the Status column is sorted, patients with a recent non-observation stay will show the following descending order (reversed for ascending order) as applicable:

- Blue Status Text
- Blue and Red Status Text
- Green and Red Status Text
- Green Status Text

Patients that have not been discharged and have a 48 hour or longer stay since admission will display a red "48+" indicator.

For observation patients, the Status column will contain the total time in hours and minutes that the patient has been on observation status ("Observation patients" refers to patients whose most recent stay meets the search criteria of an observation stay.).

The total time on observation will be calculated by subtracting the current date and time from the admission date and time. If the patient has been discharged, the total time will reflect the admission time less the discharge time. The Total Time in the Status column will increment every sixty seconds without refreshing the screen for patients that have not been discharged. For patients that have not been discharged with a Total Time exceeding eighteen hours, the time will be displayed in red, providing a visual means of identifying patients whose observation period is winding down.

#### Days Since Admission

The number of days since admission for a particular patient will be displayed as a tooltip when hovering over the Admit Date for that patient's row. This will be the days since admission for the most recent stay that meets the search criteria (There may be a more recent admission that does not meet the search criteria, because that stay may have been dismissed. Days Since Admission will not be in reference to that admission).

> **NOTE:** If the patient is known to have been discharged, either from a patient movement or from a dismissal type, the tooltip shall read "Days Since Admission: Discharged."

### Dismissing a Patient Stay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to dismiss a patient stay movement. When you dismiss a stay from the *Patient Selection/Worklist*, it will move to the *Dismissed Patient Stays* screen under the *Tools* menu (This screen is described in more detail in Section 10.3). It is important to note that although the selected stay movement will be dismissed, the entry of a new movement or discharge in VistA will refresh the patient's entry again on the *Patient Selection/Worklist* with updated information.

The system allows you to distinguish patient stay dismissal types. Having this ability will assist with reporting and identifying patients in non-reviewable specialties. This is explained in Section 4.5.1.

The *Patient Selection/Worklist* is patient-based; therefore, a dismissal of a given row in the Worklist will result in the dismissal of the stay that is currently being represented by that patient in the Worklist (i.e., the most recent stay that meets the current search criteria). If the stay represented by the patient is already dismissed, then the dismissal will have no effect, except potentially informing the user via dialog box.

This action is also available on Patient History Stays. See Section 5.

#### NUMI /VISN Support Services Center (VSSC) Processes

> NUMI will automatically place stays into the Dismissed Patient Stays screen based on the following two conditions:

1.  The Stay has an initial treating specialty that is configured in the Dismissed Patient Stays screen.
2.  The initial treating specialty is not listed at all in the Dismissed Patient Stays screen, but contains one of the following character patterns: '%DOM%', '%NH%', '%OUTPATIENT%', '%REHAB%', Representing the treating specialties categories of DOMICILIARY, NURSING HOME, OUTPATIENT, and REHAB and their derivatives.

(Example: "NURSING HOME" would cover treating specialties NHCU, NH Hospice, NH Long Term Dementia Care, NH Long Stay Maintenance Care, etc.)

NUMI shall automatically un-dismiss a stay if movement into a reviewable treating specialty (as determined by the Dismissed Patient Stays) is detected. Subsequent moves into auto- dismissible treating specialties after the initial treatment specialty will not result in an auto- dismissal. This process happens whenever a new stay is synchronized with VistA.

<u>Scenario \#1</u>:

A VistA nightly synchronization runs on Tuesday at 4:30am Eastern Time (ET) and hourly synchronization runs during the day: Patient was admitted to a Rehab treating specialty Tuesday at 12:30am ET. If any NUMI users are on the system Tuesday between 12:30am ET and 4:30am ET they will not see the patient stay on the *Patient Selection/Worklist* or Dismissed Patient Stays list until the VistA nightly synchronization runs. NUMI users who log in after 4:30am ET on Tuesday will see the patient stay on the Dismissed Patient Stays list. However, if the site has the Rehab treating specialty configured as reviewable, it would override the default dismissal and the stay would appear on the *Patient Selection/Worklist*. However, if a patient is admitted to a non-reviewable treating specialty (ex: Rehab), they will appear on the Patient Selection/Worklist if they are transferred to a reviewable treating specialty (ex: Surgery).

<u>Scenario \#2</u>:

VistA synchronization runs on Tuesday at 4:30am ET and hourly synchronization runs during the day: Patient is admitted to a reviewable treating specialty Tuesday at 10:50am and an hourly synchronization runs at 11:30am. The admission should appear on the *Patient Selection/Worklist* a minute or so after 11:30am. However, if the patient is discharged Tuesday at 7:00am ET, users will not see the discharge on the *Patient Selection/Worklist* until 4:30am ET <u>Wednesday</u> because the hourly synchronization does not bring discharges into NUMI. If a user clicks on the patient name link NUMI link before 4:30am ET, NUMI will retrieve the discharge data and the user will see it on the *Patient Stay History* screen and when they return to the *Patient Selection/Worklist*.

A data management process flow for the UM Review Process for NUMI / VSSC is illustrated in the figure below.

![](numi-user-guide-version-15-15/049.png)

<span id="_Hlk169014121" class="anchor"></span>Figure 28: Data Management for UM Review Process - NUMI / VSSC

Any reviewer can dismiss a patient from the Patient Selection/Worklist There are several reasons that you may wish to dismiss a patient stay:

- A patient stay is in a treating specialty that does not require review and automatic dismissal has not been configured to automatically dismiss the stay. (It is important to note that the nightly screening job does not screen out stays where the treating specialty has changed).
- A patient has been discharged and has all reviews for their stay entered in NUMI.
- A patient is not going to be reviewed in NUMI. Perhaps you are not reviewing 100% of patients yet, and the patient is not in your review sample.
- A patient's admission was cancelled (invalidated) in VistA. For example, perhaps a patient was admitted to acute care. The actual stay was very short, and the written admission orders are cancelled and the stay is reclassified in VistA. When the reviewer selects the patient stay for review, they would see a message indicating that the stay for the patient cannot be retrieved because it may be invalid (This is not an error, but an occurrence in clinical decision making with change of status of a patient).

> **NOTE:** It is advisable to check CPRS or VistA to confirm that a stay has changed or has been deleted. It may be important to compare the exact date/timestamps of the patient movements to determine if NUMI matches VistA, or if something was changed in VistA.You can generate a report showing all patient stays that have been dismissed. If you dismiss a patient stay in error, you can retrieve that patient and get them to reappear on the *Patient Selection/Worklist* screen by going to the *Dismissed Patient Stays* screen, locating the patient stay, and performing a review.

#### Dismissing / Distinguishing Stays

#### To dismiss / distinguish a stay

1.  Perform a search for patients using the desired filters.
2.  When the results display, the Dismiss Type dropdown and Dismiss Stays button are disabled. After selecting at least one stay checkbox on the screen, the Dismiss Type dropdown will be enabled. After choosing an option from the Dismiss Type dropdown, the Dismiss Stays button will be enabled.
3.  *Click* the checkbox in the X column in the far left hand column beside the name of the patient stay you wish to dismiss NOTE: Tool Tip: Hover the mouse over the X and a display appears: "Use the checkboxes to select stays to be dismissed"0.
4.  *Click* on the Dismiss Type dropdown and select an option by *clicking* on it. You may choose Dismiss Non Reviewable Treating Specialty, Dismiss No Further Reviews, or Patient Discharged, no further reviews needed (If you select multiple checkboxes, whatever Dismiss Type dropdown option you choose will be applied to <u>all</u> checked stays. If you wish to categorize the stays individually, select a single checkbox and then choose the desired Dismiss Type option).
5.  Click on the \<Dismiss Stays\> button next to the dropdown. If you hover your mouse over the "Dismiss Stays button" this tool tip displays "Click this button to dismiss selected stays with the selected Dismiss Type."
6.  The stay you chose will be dismissed and moved to the *Dismissed Patient Stays* screen with the reason you selected.

![](numi-user-guide-version-15-15/050.png)If you click the Dismiss Stay button without selecting an option from the dropdown first you will see a message in red text advising you to select a Dismiss Type.

![](numi-user-guide-version-15-15/051.png)

<span id="_Hlk169014140" class="anchor"></span>Figure 29: Dismiss Type Dropdown/Dismiss Stay Button

#### To change the Dismiss Type

If you select an option from the Dismiss Type dropdown and dismiss the stay, and you wish to go back and change the dismiss type to something else, you can do that by following these steps.

1.  Navigate to the Dismissed Patient Stays screen.
2.  Click the hyperlinked patient name for the stay you wish to make the change to.
3.  Perform a review on the patient.
4.  Navigate to the *Patient Selection/Worklist* screen.
5.  Perform a search for the patient.
6.  When the patient displays in the results, click the "x" checkbox beside their name.
7.  Click on the Dismiss Type dropdown and select the new value.
8.  Click the \<Dismiss Stays\> button.
9.  The stay will be dismissed with the new Dismiss Type value.

![](numi-user-guide-version-15-15/052.png)

<span id="_Hlk169014153" class="anchor"></span>Figure 30: Selected Dismiss Stay option

![](numi-user-guide-version-15-15/053.png)

<span id="_Hlk169014156" class="anchor"></span>Figure 31: Enabled Dismiss Type and Dismiss Stays features

![](numi-user-guide-version-15-15/054.png)

<span id="_Hlk169014158" class="anchor"></span>Figure 32: Select Dismiss Type advisory message

![](numi-user-guide-version-15-15/055.png) Only a checked patient stay row is dismissed and will reappear if there is another movement or new hospital admission for the patient, to make UM reviewers aware of new admissions and continued stays requiring reviews. The stay will also reappear on the Patient Selection/Worklist if the stay is selected from the Dismissed Patient Stays list and a new review is added.

### Selecting Patients for Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Selecting a Patient from the Patient Movements List

Use this feature to select a patient stay to enter a review.

#### To select a patient movement for review

1.  Conduct a search for patients using the desired filters.
2.  When the results display, *click* on a hyperlinked name in the Patient Name column worklist.
3.  The *Patient Stay History* screen will display.

![](numi-user-guide-version-15-15/056.png) When search results display on the *Utilization Management Review Listing* page, locked reviews will display a blue Patient Name hyperlink, while reviews that have been unlocked for editing will display a red Patient Name hyperlink. A tooltip "Review Saved" will be displayed on blue Patient Name hyperlink and "Review not saved" on red Patient Name hyperlink.

If a locked review is unlocked for editing, the blue link will turn red. Similarly, if a review that was unlocked for editing is save/locked back to the database, the red link will turn blue. Figure 37 depicts these colorized links:

![](numi-user-guide-version-15-15/057.png)

<span id="_Hlk169014173" class="anchor"></span>Figure 33: Utilization Management Review Listing Patient Selection/Worklist Colorized Hyperlinks

![](numi-user-guide-version-15-15/058.png) If you select a stay and the record no longer exists in VistA, the stay will be automatically invalidated. A dialogue box will open and display the message: "The patient stay you have selected appears to have been deleted from VistA. Stay ID: \<stay id\>. This patient stay has been moved to the Patient Stay Administration screen." *Click* the \<OK\> button to dismiss the dialogue. This warning may occur because an invalid patient admission was entered into VistA, and the record was deleted from the hospital database – but not before the NUMI synchronizer came in and read the information. See Section 4.2.1 for more information about admission feeds from VistA to NUMI and Section 10.7 for more information about reviews that are in NUMI but the associated stay can no longer be found in VistA.

![](numi-user-guide-version-15-15/059.png)If you search for a stay that has been invalidated because of missing data, or never synchronized into NUMI, a "No Records Found" message will appear. Please see Figure 38.

![](numi-user-guide-version-15-15/060.png)

<span id="_Hlk169014180" class="anchor"></span>Figure 34: Invalid/Missing data or never Synchronized into NUMI

![](numi-user-guide-version-15-15/061.png) When a patient is selected for review, (depending on reminder dates or dismissals and the filters used), the name will remain in the patient stay list on the *Patient Selection/Worklist* and you will be able to perform a second review right away, if you wish.

#### Deceased Patients 

A review may be performed for a now-deceased patient for the purpose of documenting information related to their final stay in the hospital. If you select a deceased patient from the movement list, this message will display: "Warning – Patient is deceased! Warning! This patient is deceased as of mm/dd/yyyy. Do you wish to continue?" along with \<Continue\> and \<Cancel\> buttons. Click the \<Continue\> button to proceed. After all reviews are entered on deceased patients, do not forget to dismiss their final hospital stay from the Patient Selection/Worklist.

![](numi-user-guide-version-15-15/062.png)

<span id="_Hlk169014186" class="anchor"></span>Figure 35: <span class="smallcaps">Deceased Patient Warning</span>

#### Sensitive Patients 

Sensitive patient records will display \#### in the SSN column.

(NOTE: Throughout NUMI, except on the *Patient Stay History* screen, if you know a sensitive patient's SSN you can still search for them by partial or full SSN).

If you are on the Utilization Management Review Listing option and select a Sensitive patient review that has been locked to the database (indicated by a blue hyperlink), you will see the pop-up in the figure below:

![](numi-user-guide-version-15-15/063.png)  
<span id="_Hlk169014194" class="anchor"></span>Figure 36: Sensitive Patient Warning for unlocked review

If you are on the Utilization Management Review Listing option and select a sensitive patient review that has been unlocked for editing (indicated by a red hyperlink), you will see the Sensitive Patient Warning screen shown in the figure below.

![](numi-user-guide-version-15-15/064.png)

<span id="_Hlk169014197" class="anchor"></span>Figure 37: Sensitive Patient Warning Screen for Unlocked Review

1.  ![](numi-user-guide-version-15-15/065.png) If you are on the Patient Selection / Worklist screen option and click on a sensitive Patient Name, you will see the Sensitive Patient Warning screen.

![](numi-user-guide-version-15-15/066.png)

<span id="_Hlk169014202" class="anchor"></span>Figure 38: Sensitive Patient Warning for Patient Stays

2.  ![](numi-user-guide-version-15-15/067.png) Once you select the \<Continue\> button, a Sensitive Patient Bulletin will be sent to the Information Security Officer at your site for justification.

### Viewing Patient Information for Different Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will be able to use this feature if you have permission to view patient information for different sites. Please note that you may only view patient information for one site at a time.

#### Switching to a Different Site 

#### To select a different site

1.  *Click* the Current Lookup Site dropdown
2.  Select a site by *clicking* on it.
3.  *Click* the \<Go\> button to view patient information for that site.

![](numi-user-guide-version-15-15/068.png)

<span id="_Hlk169014213" class="anchor"></span>Figure 39: Current Lookup Site Dropdown

![](numi-user-guide-version-15-15/069.png) You can switch to a site where you do not have a particular set of permissions and you can still navigate to the desired web page, but you will not be able to see any patient data. For example: if you get access to a site where you do not have Primary Review rights and you navigate to the *Patient Selection/Worklist* you will not see patient data there.

### Assigning and Reassigning Reviewers to Stays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select a stay from the *Patient Reviews* screen and complete a review on that patient, NUMI will automatically assign this stay to you. However, NUMI gives you the flexibility to manually assign and reassign stays to yourself or to others, as described in Section 4.9.

### Assigning / Reassigning a Reviewer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To assign a reviewer to a patient stay

1.  Conduct a search for patients using the desired filters.
2.  *Click* on the Assign Reviewer dropdown for each patient stay that you wish to assign a reviewer to.
3.  Select a reviewer from each dropdown by *clicking* on their name.
4.  *Click* the \<Assign Reviewers\> button. If you hover your mouse over the \<Assign Reviewers\> button a tooltip will display.
5.  The review will be assigned and the reviewer you selected will see the patient information in their worklist.

#### To reassign a reviewer for a patient stay

1.  *Click* on the Assign Reviewer dropdown for a patient that has already been assigned to a reviewer.
2.  Select another reviewer from the list by *clicking* on their name.
3.  *Click* the \<Assign Reviewers\> button. The review will be reassigned and the name of the new reviewer you selected will display in the table.

![](numi-user-guide-version-15-15/070.png)

<span id="_Toc479683295" class="anchor"></span>

Figure 40: Assign Reviewer Dropdown Illustration

![](numi-user-guide-version-15-15/071.png) If you complete a review on a stay, you become the assigned reviewer regardless of whether or not the review was previously assigned to someone else.

![](numi-user-guide-version-15-15/072.png)<span id="_Toc479683296" class="anchor"></span>

Figure 41: Assign Reviewers Button with Tooltip

## Patient Stay History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the *Patient Stay History* screen. The *Patient Stay History* screen displays information from VistA once you select a stay from the "Patient Selection/Worklist". Patient Stay History is related to the most recent status of a patient's stay in in the hospital.

Any reviewer can view prior movements and reviews for the stay, print out a worksheet for the patient stay for use when out on rounds, and begin a review by clicking a hyperlink, and copy an existing review. Upon initial display, the CERMe and Primary Review buttons are grayed out. A list box displays a list of all known stays for the selected patient in reverse chronological order.

The Patient Stay History screen contains a Patient Stays list and a Stay Movements grid. The Patient Stays list contains a column for the Stay ID, which is the internal NUMI database ID for the patient stay record and is also shown in the Selected Stay field on the screen.

The Stay Movements grid contains a column for the Movement ID, which is an internal Vista ID for stay movements associated with the patient stay record in NUMI. The Movement ID is synonymous with the Check in ID which is mentioned elsewhere in this guide.

So, to recap, the Stay ID is the internal NUMI database ID for the patient stay record, the Movement ID and Check in ID are synonymous and are the internal Vista ID for the stay movements that are associated with the patient stay record.

The most recent undismissed stay is selected by default, and the information in the 'Selected Stay Information' Panel on the screen is set based upon that stay. Upon selecting a new stay in the Stay List, the information in the 'Selected Stay Information' Panel on the Stay History screen is updated to reflect the information for the newly selected stay.

Details from the Patient Stay History Screen include:

- Admitting Physician: The Admitting Physician details are derived from the information entered by a reviewer on the Primary Review Screen, as described in Section 7.
- Admission Sources: The Admission Source details are derived from information entered by a reviewer on the Primary Review Screen, as described in Section 7.

![](numi-user-guide-version-15-15/073.png) If NUMI is unable to connect to VistA to obtain information associated with a stay, an error message stating that NUMI is unreachable, or NUMI cannot access VistA will be displayed. If you can access VistA through CPRS, please contact the National Service Desk. If you cannot access VistA or CPRS, then please wait to use this feature in NUMI until VistA at your facility comes back online.

![](numi-user-guide-version-15-15/074.png) If NUMI's connection to VistA does not quickly return data upon selecting a new stay, the following error message "NUMI is requesting movement records from VistA." will display and remain there until data is returned from VistA or an actual timeout occurs.

![](numi-user-guide-version-15-15/075.png) If transitioning from CERME to Primary Review screens and the VIA/VistA connection is lost, the following error will appear. "VIA service is unable to pull Patient Stay information from VISTA for Admission Movement :\< Admission Movement number\> during this time. Please submit a National Service help desk ticket. We apologize for the inconvenience." See Figure: 46.

![](numi-user-guide-version-15-15/076.png)

<span id="_Hlk169014256" class="anchor"></span>Figure 42: VIA/VistA Connection Error

![](numi-user-guide-version-15-15/077.png) If NUMI finds that a given stay is not reflected in VistA, the following error message "This stay cannot be found in VistA. Do you want to invalidate the stay?" will display.

The features on this screen are listed [in Table 3](\l).

| FEATURES                                        |
|-------------------------------------------------|
| Show / Hide Reviews Table                       |
| Dismiss a Patient Stay                          |
| Select a Review from the Reviews Table          |
| Select Review links from Movement History Table |
| View Patient Insurance Information              |
| Print out a Patient Worksheet                   |

<span id="_Hlk169014368" class="anchor"></span>Table 4: InterQual® Criteria Screen – Change Healthcare CERMe Features

![](numi-user-guide-version-15-15/078.png)

<span id="_Hlk169014273" class="anchor"></span>Figure 43: Patient Stay History

### Patient Stay List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patient stays that are synchronized into NUMI are displayed in the Patient Stay List in the upper left hand portion of the screen. The most recent undismissed stay is always displayed first in the list and is the stay upon which the "Selected Stay Information and "Reviews for Selected Stays" lists are based. Selecting a different Patient stay will re-populate the screen with new data for that newly selected stay.

### Currently Selected Stay Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "Selected Stay Information" list includes most patient information for the currently selected patient stay.

### Reviews for Currently Selected Stays List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The reviews for selected stays list is also based on the currently selected patient stay. It displays all reviewable dates for the selected patient stay. In addition, a hyperlink next to each date allows the user to conduct a review or view an existing review for that date.

### Table of Stay Movements and Table of Reviews 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stay Movements table is displayed when the *Patient Stay History* screen first opens. This table cannot be hidden. The Reviews table, however, is hidden when the screen first opens. Instructions for displaying that table are described in Section 5.4.1.

#### Showing and Hiding the Table of Reviews for a Patient 

1.  *Click* the gold colored \<Show Reviews\> bar to display the table containing the patient's reviews since they were admitted. While the table is open, the text on the bar will display \<Hide Reviews\> (For more information about NUMI bars, please see Section 2.1.2).

![](numi-user-guide-version-15-15/079.png)

<span id="_Hlk169014289" class="anchor"></span>Figure 44: Patient Stay History screen tabs and buttons

### Dismiss a Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient stays can be dismissed from the *Patient Stay History*.

![](numi-user-guide-version-15-15/080.png)  
<span id="_Hlk169014293" class="anchor"></span>Figure 45: Dismiss Stay from Patient Stay History.

#### To dismiss a patient stay:

1.  Select the stay you wish to dismiss.
2.  Choose the reason from the Select a Dismiss Type for Current Stay dropdown menu. The Dismissal Type dropdown will have the same options listed on the Patient Selection/Worklist.
3.  Click the Dismiss Currently Selected Stay.
4.  The Patient Stays column will reflect "Dismissed" in the D/U detail column

> ![](numi-user-guide-version-15-15/081.png)On the Patient History Screen, it is possible to select other stays for thatpatient for dismissal. This is in contrast to the *Patient Selection/Worklist* where the dismissal action defaults to the most recent stay with no abilities to select other stays for that patient.

### Selecting a Review from the Reviews Table 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** There are two methods for selecting stays for reviews, *"Selecting a Review from the Reviews Table"* and "*Selecting a Patient Movement from the Stay Movements Table" (Section 5.6.2)*. While both are valid methods of selecting reviews, Section 5.6, "*Selecting a Review from the Reviews Table"* provides instructions for the preferred method. Patient reviews that have not been locked into the database may require further review and completion, and will display a <u>Review</u> hyperlink in the Reviews table.

Clicking the hyperlink will open the *Review Summary* screen and you can continue working on the review from there. You will also have the option to copy the review – just click the \<Copy This Review\> button.

Reviews that have been locked to the database will display a <u>View</u> hyperlink in the Reviews table. Clicking the hyperlink will open the *Review Summary* screen, and you can look at the review and, depending on the review state and your NUMI privileges, you can edit the review, delete the review, or copy the review and save it with another date. When you open the review, you may see some or all of the following buttons: \<Close\>, \<Copy This Review\>, \<Unlock\>, \<Delete\> and \<Print\>. If the review included an admission or day that did not meet criteria, depending on the state of the review you will also see the \<Unlock Physician Advisor Review\> button (See Section 12 for more information).

#### Selecting a Review from the Review for Currently Selected Stays List 

The Review/View functionality is also available from the "Reviews for Currently Selected Stays" list on the upper right side of the screen. This functions exactly the same as selecting from the Reviews Table, with the added feature of being able to see exactly which days in the Patient Stay are available for review or have already been reviewed. Additionally, selecting a review from the "Reviews for Currently Selected Stays" list automatically pre-populates the review date in the review.

![](numi-user-guide-version-15-15/082.png)When unlocking a Primary Review Summary with no Admission Review Type displayed, you will not be able to save the review until a valid option from the Admission Review Type dropdown is selected. The valid dropdown options are discussed in Section 7.18.

There are some restrictions imposed when copying reviews. You are prohibited from copying a review and applying it to a different patient. Copying an admission review is not allowed. You are also prohibited from copying a review and using a stay date related to a different hospital admission. From this versatile screen you can Unlock, Delete, Print and Copy a review with the click of a button (See Chapter 12 for more details about Unlocking and Deleting reviews, and Chapter 13 for more details about Copying reviews).

#### To select a review from the Reviews table

1.  *Click* the blue \<Show Reviews\> bar to display the Reviews table.
2.  *Click* on the View or Review hyperlink for the review you want to see.
3.  A separate window will open and display the *Review Summary* screen.

![](numi-user-guide-version-15-15/083.png)

<span id="_Hlk169014321" class="anchor"></span>Figure 46: Review Summary screen with Unlock, Delete, Print and Copy options

#### Selecting a Patient Movement from the Stay Movements Table

Each patient will receive one review per day. If you select a patient movement from the table as a starting point for reviewing a day of a stay the Attending, Ward, and Treating Specialty are already populated. Any of these aspects related to the movement, as well as the date, can be corrected later on the *Primary Review* screen (See Chapter 7 for detailed information about the *Primary Review* screen). The caption for Figure 49 is "Review Summary screen with Unlock, Delete, Print and Copy options" but the screen shot only has Print, Close, Review and Delete. Need a new screen shot that has everything.

> **NOTE:** The Attending Physician from VistA may need to be updated in NUMI if it has been entered inaccurately on the unit, or in Admissions.

This does not update it in VistA or on the *Patient Selection/Worklist*, but NUMI reports will display the corrected Attending information.

![](numi-user-guide-version-15-15/084.png) To get to the *InterQual*® *Criteria* screen, you must click on a Review link from the Stay Movements table. The review link that you select determines the ward, treating specialty and attending physician that will be populated on the review.

#### To select a patient movement from the Stay Movements table

1.  *Click* the Review hyperlink in the Stay Movements table for the movement you want to see.
2.  Remember that the Attending Physician, Ward, Treating Specialty from that movement will pre-populate on the *Primary Review* screen.
3.  The *InterQual*® *Criteria* screen will display (See Section 6 for information about the *InterQual*® *Criteria* screen and its use in NUMI).

![](numi-user-guide-version-15-15/085.png)

<span id="_Hlk169014335" class="anchor"></span>Figure 47: Patient Movements and Reviews tables

### Viewing Patient Insurance Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The display of patient insurance is for informational purposes only and does not impact the review process (Insurance review data can be entered into the VistA Claims Tracking application or another facility/VISN-designated program for tracking of this information). The Insurance field will be collapsed when the *Patient Stay History* screen first opens.

#### To display Insurance information

1.  *Click* the \<+\> button, beside the Insurance field and the patient's insurance information will display. If the patient does not have insurance, a "0" will display in the field.

### Printing out a Patient Worksheet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI offers a convenient feature that allows you to print out a hardcopy worksheet with admission information for a patient and use it to take notes to assist you in entering reviews into NUMI. This can be helpful if you like to do all your CPRS research first and then enter reviews, or if you need to take notes when out on the units. Worksheets can be valuable tools if a reviewer needs to pick up patients from another reviewer.

#### To print a patient worksheet

1.  *Click* the \<Patient Worksheet\> button.
2.  A worksheet with information for the patient will display in a new window. *Right-click* and select the \<Print\> option to print it out on your local printer.

![](numi-user-guide-version-15-15/086.png)

<span id="_Hlk169014351" class="anchor"></span>Figure 48: Patient Worksheet example

### Invalidating a Patient Stay 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you click on a patient stay ID and the stay cannot be found in VistA, or no longer exists in VistA, then the Invalid Stay dialog will appear. When this occurs the user has the option of invalidating the stay. Choose Invalidate to invalidate the stay, or choose Do Not Invalidate to leave the stay in its current state.

If you choose "Do Not Invalidate" then whatever stay was selected will remain selected. You can invalidate the stay at a later time if you wish.

![](numi-user-guide-version-15-15/087.png)

<span id="_Hlk169014356" class="anchor"></span>Figure 49: Invalidating a Patient Stay

## InterQual<sup>®</sup> Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The InterQual<sup>®</sup> Criteria screens within NUMI contain the electronic version of Change Healthcare's CERMe product. This interactive electronic version contains the same criteria found in the online Book View version available on the OQSV website.

![](numi-user-guide-version-15-15/088.png)

<span id="_Hlk169014362" class="anchor"></span>Figure 50: Initial InterQual<sup>®</sup> Criteria screen surrounded by NUMI banner

![](numi-user-guide-version-15-15/089.png)

<span id="_Hlk169014365" class="anchor"></span>Figure 51: NUMI Banner above InterQual<sup>®</sup> Criteria screen

Below the gray navigation buttons, the patient name, age, and admission diagnosis are pre-populated from VistA. The Continue Primary Review button located in the upper right will be grayed out and disabled when the InterQual<sup>®</sup> Criteria screen first opens.

| CERMe FEATURES                              |
|---------------------------------------------|
| Selecting NUMI Review Type                  |
| CERMe Help, Navigation Pane, Font size      |
| InterQual® Products, Categories and Subsets |
| Keyword and Medical Code Search             |
| Criteria Organization                       |
| Criteria Met or Not Met                     |
| Working with InterQual® Notes               |
| Create a Review in CERMe                    |
| Additional Features in CERMe                |

<span id="_Hlk169014435" class="anchor"></span>Table 5: InterQual® Criteria Subsets not implemented in NUMI

### Selecting a Review Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Review Type field contains a dropdown list where you select the type of review being completed. This field is VA specific and not part of the CERMe product.

![](numi-user-guide-version-15-15/090.png)

<span id="_Hlk169014385" class="anchor"></span>Figure 52: Review Type Dropdown Box

A Review Type should be selected prior to moving through the InterQual<sup>®</sup> Criteria screens.

![](numi-user-guide-version-15-15/091.png)

<span id="_Hlk169014391" class="anchor"></span>Figure 53: Review Type Dropdown box

Current selections available include:

- Admission
- Continued Stay

It is helpful to select the review type *before* making any other selections.

### CERMe Help, Navigation and Font Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the Help button to display the CERMe help menu.

![](numi-user-guide-version-15-15/092.png)

<span id="_Toc168998282" class="anchor"></span>Figure 54: Change Healthcare Help Button for CERMe

![](numi-user-guide-version-15-15/093.png)

<span id="_Hlk169014404" class="anchor"></span>Figure 55: Change Healthcare Help Menu for CERMe

The Help dropdown menu contains a variety of Change Healthcare CERMe help topics. These help topics are specific to the Change Healthcare products and users are encouraged to seek reference material from the UM Website for guidance specific to NUMI and/or the VHA UM Review Process. Available Change Healthcare Help topics are:

- CareEnhance Review Manager Help
- Guide to Conducting Reviews
- InterQual® Clinical Reference
- Historical InterQual® Clinical Reference
- About CareEnhance Review Manager

> **CAUTION:** NUMI users should refer to the VHA Review Process SOPs available on the VHA UM Website. Contact your InterQual® Certified Instructor or supervisor for assistance in VHA specific reference documents.

The area outlined below is called the navigation pane. The navigation pane will not display content until a subset is selected. Once populated, the navigation pane can be used to select criteria that will display in the center of the screen.

![](numi-user-guide-version-15-15/094.png)

<span id="_Toc479683310" class="anchor"></span>

Figure 56: Navigation pane highlighted

#### Changing the Size of the Font 

A plus (+) and a minus (-) button can be seen to the right of the Criteria Not Met tab – that can be used to modify the size of the font displayed in the center section of the screen. This option is available after the subset has been selected.

![](numi-user-guide-version-15-15/095.png)

<span id="_Hlk169014420" class="anchor"></span>Figure 57: Font size indicator buttons

Following selection of a subset, the navigation pane is populated (See next Figure).

![](numi-user-guide-version-15-15/096.png)<span id="_Toc479683312" class="anchor"></span>

Figure 58: Product, Subset, and Criteria Version

### Selecting the Product, Category and Subsets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on any of the products in the list to open the categories.

![](numi-user-guide-version-15-15/097.png)

<span id="_Hlk169014430" class="anchor"></span>Figure 59: InterQual® Products and Categories

![](numi-user-guide-version-15-15/098.png)NOTE: After selecting LOC: Acute Adult, selections are available in the Categories list for the *Quality Indicator Checklist* and the *Transition Plan*. These screens are available to view and use for reference. No data entered on these screens will be saved in the NUMI database. Behavioral Health Procedure Review Subsets are not supported in NUMI. CERMe will let you choose the Transition Plan Review subsets below and do a review, but you should not save Transition Plan reviews.

| InterQual® Product | Category                    | Unsupported Subsets |
|--------------------|-----------------------------|---------------------|
| LOC: Acute Adult   | Transition Plan             | All                 |
| LOC: Acute Adult   | Quality Indicator Checklist | All                 |
| BH: Procedures     | Procedure Review            | All                 |

<span id="_Hlk169014791" class="anchor"></span>Table 6: Primary Review Summary Screen Features

No reviews need to be performed for non-implemented subsets (i.e., procedures within Behavioral Health and transition plans), and they should not be saved.

Procedure Review is not a selectable product in current CERMe versions.

#### Finding Subsets 

After selecting the product, then the category, a list of subsets will display:

![](numi-user-guide-version-15-15/099.png)

<span id="_Hlk169014454" class="anchor"></span>Figure 60: LOC: Acute Adult subsets

#### Changing a Subset Selection

To change a Subset selection, *click* the Change Subset button in the center of the LOC note:

![](numi-user-guide-version-15-15/100.png)

![](numi-user-guide-version-15-15/101.png)

<span id="_Hlk169014461" class="anchor"></span>Figure 61: Change Subset Button

The following message displays, "Changing subsets will erase all criteria point selections, reviewer notes, and the review outcome. Would you like to change subsets?"

![](numi-user-guide-version-15-15/102.png)

<span id="_Hlk169014466" class="anchor"></span>Figure 62: Change Subset pop-up confirmation box

*Click*ing the Yes button returns you to the screen containing the list of subsets where you may select a different subset.

Use your mouse to highlight and select a different subset from the list (such as Chronic Obstructive Pulmonary Disease (COPD). Doing this will change the screen content and allow you to either select an episode day for the new subset or view the corresponding subset note.

![](numi-user-guide-version-15-15/103.png)<span id="_Toc479683318" class="anchor"></span>

Figure 63: Return to Subset list

Clicking on the COPD subset updates the content to display the episode days available for the COPD subset. The subset description at the top of the navigation pane also updates to the newly selected subset.

![](numi-user-guide-version-15-15/104.png)

<span id="_Hlk169014479" class="anchor"></span>Figure 64: Changed to COPD subset

When the new subset is selected, you can open the subset review note for the new subset to determine if it appropriate to use by clicking on the version box at the top of the navigation pane.

The Episode Day Menu will update to reflect appropriate days of review for the new subset.

![](numi-user-guide-version-15-15/105.png)

<span id="_Hlk169014485" class="anchor"></span>Figure 65: Episode Day Menu reflects days of review for new subset

You can begin a review with the new subset by selecting an episode day from the navigation pane. The change subset function may be repeated until the most appropriate subset for the clinical review is found.

### Keyword/Medical Code Search and Instruction Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to search for InterQual<sup>®</sup> Medical Criteria Product subsets using Keywords and Medical Codes. The Keyword search feature is handy when users are not sure which subset to use for an admitting diagnosis. The Medical Code search feature is handy in cases where concurrent coding has been done (i.e., a patient stay gets an ICD code upon admission, and that code is changed concurrently as the diagnosis changes).

Type the desired Keyword or Medical code into the field and click Find Subsets to generate a list of subsets relative to your entry. If a Keyword or Medical Code search produces no results, the message "No Subsets Found" displays. Use commas between multiple Keywords and Medical Codes to receive the best results.

Subset notes provide guidance on subset selection. Depending on the subset chosen, information on evaluation, standard treatment options, and level of care (LOC) are found.

![](numi-user-guide-version-15-15/106.png)

<span id="_Hlk169014495" class="anchor"></span>Figure 66: Subset note icons

View the notes by *clicking* on the ![](numi-user-guide-version-15-15/107.png) button beside any of the listed subsets. A dialog box will display the contents of the LOC Instruction note.

![](numi-user-guide-version-15-15/108.png)<span id="_Toc479683322" class="anchor"></span>

Figure 67: Viewing Notes

Close the dialog box by clicking on the in the right corner.

![](numi-user-guide-version-15-15/109.png)

<span id="_Hlk169014509" class="anchor"></span>Figure 68: Subset list

From the subset list, use your mouse to highlight the subset you want to open. Click on the underlined subset description to access the criteria and begin the clinical review.

![](numi-user-guide-version-15-15/110.png)

<span id="_Hlk169014514" class="anchor"></span>Figure 69: Selecting a subset

#### LOC Instruction Note

Clicking on the box identifying the product, subset, and criteria version will allow users to view the LOC Instruction Note. The LOC Instruction Note provides an overview of the subset contents. This feature is available in both LOC Acute Adult and BH Products.

![](numi-user-guide-version-15-15/111.png)<span id="_Hlk169014520" class="anchor"></span>Figure 70: LOC Instruction Note

### Criteria Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Menu of Review Days

Many subsets within the LOC: Acute Adult products are organized by Episode or Operative Days. When the subset is selected, a menu of days will display in both the navigation pane on the left and also in the center of the screen. Behavioral Health products are organized by LOC.

![](numi-user-guide-version-15-15/112.png)NOTE: Initial review under Criteria selection is designed for use in screening patients PRIOR to admission therefore users should not select this to complete reviews in NUMI.

![](numi-user-guide-version-15-15/113.png)

<span id="_Hlk169014529" class="anchor"></span>Figure 71: Acute Adult criteria: Episode Day Menu

![](numi-user-guide-version-15-15/114.png)

<span id="_Hlk169014531" class="anchor"></span>Figure 72: Surgical Subset Operative Day Menu

![](numi-user-guide-version-15-15/115.png)

<span id="_Hlk169014536" class="anchor"></span>Figure 73: Behavioral Health Level of Care menu

### Level of Care (LOC) Options: Acute Adult Product

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the LOC: Acute Adult product, when an Episode Day or Operative Day is selected from the navigation pane, LOC options display in the center of the screen. LOC options and criteria are evidence based. Only levels of care considered clinically appropriate will be displayed.

Below you see the LOC Options: Observation, Intermediate, and Critical. No Acute level is available to select.

![](numi-user-guide-version-15-15/116.png)

<span id="_Hlk169014541" class="anchor"></span>Figure 74: Episode Day 1: Levels of Care

![](numi-user-guide-version-15-15/117.png)

<span id="_Hlk169014546" class="anchor"></span>Figure 75: Operative Day: Levels of Care

Select the LOC for your review. Click the \<+\> to access the selectable criteria appropriate for any of the listed levels of care.

You may open one or all levels of care using the \<+\> button.

![](numi-user-guide-version-15-15/118.png)

<span id="_Hlk169014550" class="anchor"></span>Figure 76: Expanding Acute Level of Care

When multiple criteria lists are opened, you may need to use the scroll bar to view all of the criteria.

![](numi-user-guide-version-15-15/119.png)

<span id="_Hlk169014555" class="anchor"></span>Figure 77: Scroll bar used to view multiple expanded criteria lists

The organization of the Behavioral Health Product criteria is different than LOC: Acute Adult. After selecting a level of care option from the navigation pane, a menu of Episode Days appears in the center of the screen as shown below. The selectable criteria are available within each Episode Day.

![](numi-user-guide-version-15-15/120.png)

<span id="_Hlk169014559" class="anchor"></span>Figure 78: Episode Days in BH Products

![](numi-user-guide-version-15-15/121.png)

<span id="_Hlk169014563" class="anchor"></span>Figure 79: Selectable Criteria in BH

Selectable criteria points are contained within each level of care. Clicking on the button will open the list of clinical criteria appropriate for the subset, day, and level of care.

![](numi-user-guide-version-15-15/122.png)

<span id="_Hlk169014566" class="anchor"></span>Figure 80: Selectable Criteria for Observation

Use the checkboxes to indicate which criteria points are valid for the patient and episode of care you are reviewing.

![](numi-user-guide-version-15-15/123.png)

<span id="_Hlk169014570" class="anchor"></span>Figure 81: Selected criteria using checkboxes

Click on the box to place a check mark inside the box. To remove check marks, click the check mark again.

Many criteria points contain additional "nested" criteria. Click on the plus sign \<+\> to expand, or open the list of criteria.

![](numi-user-guide-version-15-15/124.png)

<span id="_Hlk169014574" class="anchor"></span>Figure 82: Expanding and Collapsing Criteria Lists

Use the \<+\> beside each criteria set or point to open additional nested criteria. The screen can become full quickly when all lists are expanded.

![](numi-user-guide-version-15-15/125.png)

<span id="_Hlk169014578" class="anchor"></span>Figure 83: Using \<+\> to expand nested criteria

As you work through the nested criteria it may be helpful to collapse the list when the checkmark indicates the criteria point is met or if criteria do not apply:

![](numi-user-guide-version-15-15/126.png)

<span id="_Hlk169014584" class="anchor"></span>Figure 84: Use \<-\> to collapse nested criteria

Collapse the list to allow for easier viewing by clicking on the - beside the criteria point.

![](numi-user-guide-version-15-15/127.png)

<span id="_Hlk169014587" class="anchor"></span>Figure 85: View of collapsed list of selected criteria

This will make it easier for you to work through criteria points containing multiple qualifying criteria.

#### Criteria Met/ Not Met Indicator

In the header bar across the screen, the selected product and subset will display. On the right side of the header bar is a red 'Criteria Not Met" indicator.

When the selection of criteria fulfills the requirement for the selected LOC, the indicator will change from red "Criteria Not Met" to a green box indicating the LOC "Met."

![](numi-user-guide-version-15-15/128.png)

<span id="_Hlk169014596" class="anchor"></span>Figure 86: Criteria Not Met Indicator is RED

#### Observation Met Indicator

![](numi-user-guide-version-15-15/129.png)

<span id="_Hlk169014599" class="anchor"></span>Figure 87: Criteria Met Indicator is GREEN

#### Criteria Met Check Mark

In addition to the colored "Criteria met/not met" indicator, users can use the navigation pane to determine when criteria are met. A check mark will appear to the left of the Episode Day, or Operative Day in the navigation pane for another reference when criteria are met (or not met). The check mark functions in all CERMe products.

![](numi-user-guide-version-15-15/130.png)

<span id="_Hlk169014605" class="anchor"></span>Figure 88: Criteria appear checked in left (navigation) pane

The Next Step arrow at the bottom of each navigation pane under the InterQual<sup>®</sup> Clinical Reference bar is non-functional, but part of the CERMe software that cannot be removed.

![](numi-user-guide-version-15-15/131.png)

<span id="_Hlk169014609" class="anchor"></span>Figure 89: Non-functional Next Step arrow

![](numi-user-guide-version-15-15/132.png)NOTE: Clicking on the next arrow during reviews may result in an error message.

### Working with InterQual® Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](numi-user-guide-version-15-15/133.png)

<span id="_Hlk169014615" class="anchor"></span>Figure 90: Notes and Transition

Several note types are available within the criteria. The InterQual<sup>®</sup> Notes that display will depend on the criteria you have selected and are specific to that criteria. Not all criteria points have associated information notes or other icons. Criteria Information Notes and Transition Plan note icons are used to identify specific types of notes contained within the criteria. Criteria Information Notes are identified by the Note Icon at the end of the criteria point. Notes will display on the right side of the associated criteria point as seen below:

![](numi-user-guide-version-15-15/134.png)

<span id="_Hlk169014619" class="anchor"></span>Figure 91: Criteria Note Icons

#### Viewing Notes

Notes can be viewed individually by clicking on a specific icon. The selected note will be displayed as a web pop-up box that displays over the CERMe screen and is easily read. Additionally, notes will display in the in the lower left hand window of the sidebar as seen below, even if the user does not select the icon.

![](numi-user-guide-version-15-15/135.png)

![](numi-user-guide-version-15-15/136.png)

<span id="_Hlk169014626" class="anchor"></span>Figure 92: View Notes icon enlarged

Use the view notes icon in the right upper corner to enhance the view of notes displayed at the bottom of the screen. This is helpful when more than one note is associated with a particular criteria point.

![](numi-user-guide-version-15-15/137.png)

<span id="_Hlk169014629" class="anchor"></span>Figure 93: Informational Notes

#### Criteria Information Notes 

Informational notes are available for many criteria points within each subset. These notes provide explanations of criteria, definitions of medical terminology, information about a clinical condition, and specific instructions on how to apply criteria. Reviewers are highly encouraged to use the criteria information notes during the review process.

To view Informational Notes, Click on the Note icon. A dialog box opens to display the note:

![](numi-user-guide-version-15-15/138.png)

<span id="_Hlk169014641" class="anchor"></span>Figure 94: Example of note for Chronic Obstructive Lung Disease

Close the note by clicking on the Red in the upper right corner of the dialog box. The notes will continue to display at the bottom of the CERMe screen for easy reference. ![](numi-user-guide-version-15-15/139.png)

#### Care Management Information Note Field

This is a tool to assist the care manager and not part of a review. These notes are derived from content, EBM literature, discharge screens, and consultant consensus. Barriers are based on clinical guidelines.  This information is displayed to the right in the software.

![](numi-user-guide-version-15-15/140.png)

<span id="_Hlk169014648" class="anchor"></span>Figure 95: Care Management Information Note Field

![](numi-user-guide-version-15-15/141.png)

<span id="_Hlk169014652" class="anchor"></span>Figure 96: Expected Progress Note

![](numi-user-guide-version-15-15/142.png)

<span id="_Hlk169014657" class="anchor"></span>Figure 97: Care Facilitation Note

Expected progress: Provides a holistic picture of what the care manager should expect in response to treatment, potential barriers, and suggested interventions.

Care Facilitation: Identifies when a plateau has been reached and provides direction to appropriate post-acute levels of care.

#### Transition Plan Notes

Within the criteria, certain criteria points are flagged with a green ![](numi-user-guide-version-15-15/143.png) icon indicating that the patient may be at risk for readmission and could benefit from comprehensive discharge planning. The Transition Plan is a comprehensive discharge planning guideline intended to provide reviewers with a means to document, track and report on the discharge plan throughout the episode of care.

It provides a framework for identifying discharge needs and outlines the interventions necessary to ensure continuity of quality patient care. Evidence has demonstrated that attention to transitioning care from one setting to another can significantly improve outcomes, impact quality of care and reduce readmissions.

To view Transition Notes, click on the green Transition Note icon. A dialog box opens to display the note:

![](numi-user-guide-version-15-15/144.png)

<span id="_Hlk169014670" class="anchor"></span>Figure 98: Example of a Transition Plan note displayed in NUMI

Close the note by clicking on the black in the upper right corner of the dialog box. The notes will continue to display at the bottom of the CERMe screen for easy reference.

### Create a Review with CERMe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps used in NUMI to complete Behavioral Health (BH) reviews are different because the criteria organization of the BH products differs.

You will first select the BH review type: Admission or Continued Stay Review. Next, select the BH product, category, and subset for review.

![](numi-user-guide-version-15-15/145.png)

<span id="_Hlk169014678" class="anchor"></span>Figure 99: Screen displaying BH Review Type, Product, Category, and Subset

After the subset is selected for any BH Initial Review, levels of care will display in the navigation pane.

![](numi-user-guide-version-15-15/146.png)

<span id="_Hlk169014683" class="anchor"></span>Figure 100: BH Levels of care display

Selecting the patient's current LOC will create a list of Episode days in the center of the screen.

![](numi-user-guide-version-15-15/147.png)

<span id="_Hlk169014689" class="anchor"></span>Figure 101: Episode Days displayed under level of care

Selecting the Episode Day will open the list of selectable criteria points relative to each episode day.

![](numi-user-guide-version-15-15/148.png)

<span id="_Hlk169014692" class="anchor"></span>Figure 102: BH Selectable Criteria

Click on the check boxes to select the appropriate criteria points.

Click on the \<+\> sign to the left or by selecting them individually using the navigation pane.

> **NOTE:** The center of the screen may become cluttered and difficult to read if you open the criteria using the \<+\> signs.

When the criteria points selected support the level of care being reviewed the criteria met indicator will turn green. Additionally, the reviewer will see a check mark in the navigation pane to the left of the level of care met.  
  
![](numi-user-guide-version-15-15/149.png)<span id="_Toc479683356" class="anchor"></span>

Figure 103: BH Criteria selected using check boxes

### Create a Review with CERMe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When all applicable criteria points have been selected the reviewer will move to the next portion of the application to record and save the review outcome.

This step is the same regardless of the "criteria met" or "not met" status. In either situation, the reviewer will select the Continue Primary Review Button to complete the next step of the review process.

![](numi-user-guide-version-15-15/150.png)

<span id="_Hlk169014706" class="anchor"></span>Figure 104: Intermediate Met indicator

![](numi-user-guide-version-15-15/151.png)

<span id="_Hlk169014709" class="anchor"></span>Figure 105: Criteria Not Met indicator

#### Continue Primary Review Button

![](numi-user-guide-version-15-15/152.png)

<span id="_Hlk169014714" class="anchor"></span>Figure 106: Continue Primary Review Button

Select this button to leave the Criteria screen in the NUMI application and proceed to the Primary Review Summary Screen where you will record your review outcome and lock and save the review into the NUMI database.

### Additional Features in CERMe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The lower portion of the navigation pane contains menu options with usable additional features. Depending on the product one or more of the selections below are available:

- Review Summary
- Export
- Reference (Non-Functional-Grayed Out!)
- View Discharge Screens
- InterQual<sup>®</sup> Clinical Reference

Refer to the next Figure to see the navigation pane showing additional features in CERMe.

![](numi-user-guide-version-15-15/153.png)![](numi-user-guide-version-15-15/154.png)

<span id="_Hlk169014728" class="anchor"></span>Figure 107: Additional Features in CERMe

Clicking on any of these will open them for viewing. Note that the Reference Section is grayed out and non-functional.

#### Printing a Review Summary

While there is a feature for printing a review summary, it should be noted that this summarizes <u>CERMe data selected only</u>, and does not include any VA specific review outcome data. To print a CERMe review summary, *click* the Review Summary button on the sidebar.

The summary information will display in the right side. Use your browser's print feature to print out the information noting that only the criteria selections will be available for printing.

![](numi-user-guide-version-15-15/155.png)

<span id="_Hlk169014738" class="anchor"></span>Figure 108: CERMe Review Summary

#### Export 

The Export function is a CERMe feature that does not function in NUMI. Clicking on this selection is possible but users will not be able to export data from this screen.

![](numi-user-guide-version-15-15/156.png)

<span id="_Toc168998337" class="anchor"></span>Figure 109: Export Feature

#### Reference Section

The reference section of CERMe was disabled by Change Healthcare. Content previously included in this section is now available in the InterQual<sup>®</sup> Clinical Reference section.

#### Viewing Discharge Screens 

Discharge screens allow users to select a post-acute LOC for determination of patient stability for a proposed LOC. These screens and criteria are for reference only and Discharge reviews are not currently completed in NUMI. Discharge screens are available only for the LOC: Acute Adult product.

![](numi-user-guide-version-15-15/157.png)

<span id="_Hlk169014752" class="anchor"></span>Figure 110: Discharge Screens

Select a potential discharge LOC and click on the \<+\> to display criteria points for each discharge LOC. Criteria points are not selectable within the discharge screens.

![](numi-user-guide-version-15-15/158.png)

<span id="_Hlk169014757" class="anchor"></span>Figure 111: Discharge level of care expanded view

> **NOTE:** The discharge screen information is used for reference purposes only. Discharge reviews are not currently required in NUMI.

## Primary Review Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the Primary Review Summary screen. The Primary Review Summary screen is where you will select a day to be reviewed during the patient stay and add and update patient review information such as review and reminder dates, levels of care, Attending's, and stay reasons.

During the initial patient review, if the Admitting Physician field is not already populated by VistA, the reviewer should select an Admitting Physician from the Admitting Physician dropdown in the stay information section of the Primary Review Summary screen.

The IQ Criteria Met and Subset captured from CERMe are displayed on the review screen.

To flag an unscheduled re-admission within 30 days of discharge, the reviewer can select the "Check if Unscheduled Readmit within 30 Days" checkbox. This appears when the CERMe review type is "Continued Stay" and the day being reviewed is the same as the admission date.

The Primary Review Summary screen also displays the following text near the "Check if Unscheduled Readmit within 30 Days" checkbox: "You are a conducting a "Continued Stay" Review for the day of admission. This should only be done when patients are inter-ward transfers within your facility. This is not their first day of admission."

This message will only appear when the CERMe review type is "Continued Stay" and the day reviewed is the same as the admission date.

In the IQ Criteria Met field, a visible Met / Not Met indicator is displayed for your convenience. The value that displays in the field (Yes/No) will be determined by the criteria checkboxes that were selected on the InterQual® Criteria screen (The IQ Criteria Met field value will also display in the Met? column on the Patient Selection/Worklist screen).

A "Criteria Not Met Elaboration" box will appear when the reviewer is creating a review that has not met criteria. A "Custom" text box will appear on the Primary Review Screen. You can type up to 25 characters in this box. The full content of the Custom text will appear as you hover over this area with your mouse.

On this screen you can also select the Admission Review Type, see if the IQ Criteria is met, select the Current LOC and Day Being Reviewed, enter any Reviewer Comments and, if the review does not meet criteria, select a Recommended Level of Care, a Reason Description, and enter Criteria Not Met Elaboration details. If the review does not meet criteria and you did not select the "Check here if criteria are NOT MET and formal hospital policy does NOT require physician review" check box, select a Physician Advisor Reviewer.

The "Check this box if you will not be doing further views on this stay" checkbox can be selected or you can set a reminder that is different than the default of tomorrow's date by selecting the Next Review Reminder date.

Other actions that can be taken on the Primary Review screen are: Select the Admitting Physician from the dropdown, select the Admission Source the dropdown, select the Attending Physician from the dropdown, select the Treating Specialty from the dropdown, and select the Service Section from the dropdown. Verify the Ward, identify unscheduled readmissions, copy a review (via a link in the Reviews table), and save/lock reviews to the database.

The bottom half of the screen displays read-only review text information from Change Healthcare CERMe (The information that displays in the Attending, Treating Specialty and Ward fields will depend on which <u>Review</u> hyperlink you selected on the *Patient StayHistory* screen). When the screen first displays, the Patient Selection/Worklist, Patient Stay History, CERMe, and Primary Review buttons will be available for selection. The features on this screen are listed in Table 6.

If a user creates Admission or Initial Review type reviews, the system will display an Admission Review Type dropdown, a Number of Days Since Last VA Acute Care Discharge field, and a Check if Unscheduled Readmit Within 30 Days checkbox on the *Primary Review Summary* screen.

![](numi-user-guide-version-15-15/159.png) All fields on the *Primary Review Summary* screen (except Custom and Reviewer Comments) are required and must be populated before a review can be saved and locked to the database. If the review "Meets" you must select Review Date, Attending Physician, Current Level of Care, Treating Specialty, Ward, and Service Section. If the review "Does Not Meet" you must select options from the above mentioned fields as well as options for Recommended Level of Care and Physician Advisor, and enter Criteria Not Met Elaboration text. If the review is an Admission type you must select an Admission Review Type. If you do not select something from these dropdowns you will see one or more messages in red text.

![](numi-user-guide-version-15-15/160.png)

<span id="_Hlk169014784" class="anchor"></span>Figure 112: Example required field messages on Primary Review Screen

> NOTE: The red text error messages depicted in the various figures within this document may vary from their appearance to the actual application. This is due to on-going section 508 compliance changes.

> ![](numi-user-guide-version-15-15/161.png)

<span id="_Hlk169014789" class="anchor"></span>Figure 113: Red text example

| FEATURES                                                         |
|------------------------------------------------------------------|
| Select Day Being Reviewed Date                                   |
| Select/Change Current Level of Care                              |
| Select/Change Attending Physician                                |
| Select/Change Treating Specialty                                 |
| Select/Change Ward                                               |
| Select/Change Service Section                                    |
| Working with Admission Review Types                              |
| Working with Admission Sources                                   |
| Add Reviewer Comments                                            |
| Select Stay Reasons                                              |
| Assign a Physician Advisor to a Review that has Not Met Criteria |
| Change Next Review Reminder Date                                 |
| Indicate no more Reviews on a Stay                               |
| Select/Change Recommended Level of Care                          |
| Indicate an Unscheduled Readmission within 30 days               |
| Show a Patient's Reviews                                         |
| Copy a Review                                                    |
| View CERMe Review Text                                           |
| Add Custom Notes                                                 |
| Save and Lock a Final Review                                     |
| Add an Admitting Physician                                       |
| Days Since Last VA Acute Care Discharge Calculation              |
| Enter Criteria Not Met Elaboration                               |

<span id="_Hlk169015158" class="anchor"></span>Table 7: Physician Advisor Screen Features

### Selecting the Day Being Reviewed Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Primary Review Summary screen opens, you will need to select a Day Being Reviewed date. This calendar feature is located below the Admit Date field and above the Review Type field. If you selected the review from the "Reviews from Currently Selected Stays" list on the Patient History page, the review date will be pre-populated.

#### To select the Day Being Reviewed date

> *Click* on the dropdown box beside the Calendar icon and select the stay date you are reviewing. This should not be the discharge date since reviews should not be entered for the discharge date.

![](numi-user-guide-version-15-15/162.png)

<span id="_bookmark171" class="anchor"></span>Figure 114: Calendar

![](numi-user-guide-version-15-15/163.png) The calendar only lets you select a date between Admission and Discharge dates (or current day's date if the patient is still in the hospital). If you manually enter a date, it must be within that range or it will change the date to mm/dd/yyyy format but, may not keep the entered value.

Once you select the Review Date, the Day of Stay populates with a number representing the difference between the Admission Date and the Review Date plus one. e.g., if the Review Date and Admission Date are the same, the Day of Stay is "1."

If you selected the review from the "Reviews from Currently Selected Stays" list on the Patient History page, the review date will be pre-populated as will be the Day of Stay.

#### Calendar and 508 Compliance

The calendar popup that appears next to the text box for all the dates in the NUMI application is not Section 508 compliant. NUMI uses a third-party tool (Excentrics World) for calendar popup, and hence, cannot be made Section 508 compliant. The non-sighted users have an alternative mean of entering the date directly in the text box, in the format of MM/DD/YYYY. Any incorrect date entered will be autocorrected by the system, and the corrected date will be read back to the non-sighted user with a screen reader.

### Selecting Admission Review Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to select the Admission Review Type for a patient. You must select an Admission Review Type or you will not be able to save the review.

#### To select the Admission Review Type

1.  *Click* on the Admission Review Type dropdown.
2.  Select an Admission Review Type by *clicking* on an option in the list.

### Selecting or Changing Current Level of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to select or change the Current Level of Care for a patient. You must select a Current Level of Care or you will not be able to save the review.

![](numi-user-guide-version-15-15/164.png)

<span id="_bookmark175" class="anchor"></span>Figure 115: Primary Review screen

#### To select or change the Current Level of Care

1.  *Click* on the Current Level of Care dropdown.
2.  Select a Current Level of Care by *clicking* on an option in the list, OR
3.  Change the Current Level of Care to another value by *clicking* on a different one.

### Enter Criteria Not Met Elaboration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to elaborate on criteria not met.

#### To enter Criteria Not Met Elaboration

1.  *Type* up to 100 characters directly into the Criteria Not Met Elaboration field

![](numi-user-guide-version-15-15/165.png)  
<span id="_Hlk169014857" class="anchor"></span>Figure 116: Criteria Not Met Elaboration

### Adding Reviewer Comments 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Comments that you enter here will also display in the Comments window on the Physician Advisor Worklist screen for reviews not meeting criteria. Your comments may be up to 4,000 characters in length. It is helpful to enter information, which will explain why the patient does not meet criteria. For reviews meeting criteria, use this field to document information that will be helpful to you for future reference (Please see Section 10.5 for more information about this screen).

#### To add reviewer comments

1.  *Type* your comments directly into the Reviewer Comments field

![](numi-user-guide-version-15-15/166.png)

<span id="_Hlk169014866" class="anchor"></span>Figure 117: Reviewer Comments

### Selecting a Stay Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stay reasons will only be required on the *Primary Review Summary* for reviews that have <u>not</u> met criteria. The Stay Reason categories are collapsed when the screen first opens. To expand the categories and view the list of Stay subcategories, click the \<+\> buttons.

![](numi-user-guide-version-15-15/167.png) You must choose a Stay Reason if the stay does not meet criteria or you will not be able to save the review and the message "Please Select a Reason" will display.

![](numi-user-guide-version-15-15/168.png)

<span id="_Hlk169014873" class="anchor"></span>Figure 118: Expanded Stay Reason Categories

To select a stay reason

1.  Click on the \<+\> button beside the desired stay reason category.
2.  Choose a stay reason by clicking on it

### Selecting or Changing Recommended Level of Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recommended Level of Care dropdown will only display for reviews that have <u>not</u> met criteria.

#### To select or change Recommended Level of Care

1.  *Click* the Recommended Level of Care dropdown.
2.  Select an option from the dropdown by *clicking* on it.

![](numi-user-guide-version-15-15/169.png)

<span id="_Hlk169014886" class="anchor"></span>Figure 119: Recommended Level of Care Options

### Assigning a Physician Advisor to a Review that has Not Met Criteria 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to assign a review that did not meet criteria to a Physician Advisor. You must choose a Physician Advisor or you will not be able to save the review and the message "Please Select a Physician Advisor" will display.

#### To select a Physician Advisor to receive a review that has not met criteria

1.  Select the Physician Advisor Review dropdown and select a name by *clicking* on it.
2.  Once you *click* the \<FINAL SAVE/Lock to Database\> button, the review will be assigned to that individual and it will display the next time they open their *Physician Advisor Worklist* screen.

![](numi-user-guide-version-15-15/170.png)

<span id="_Hlk169014896" class="anchor"></span>Figure 120: Physician Utilization Management Advisor dropdown

#### Physician Advisor Review Not Required

There is an overarching rule that all unmet reviews are sent to a Physician Advisor. NUMI gives you an option to indicate that a Physician Advisor Reviewer review is <u>not</u> required.

![](numi-user-guide-version-15-15/171.png) In order to check the box indicating that the Physician Advisor review is not required, a local facility policy must be in place defining the specific cases not requiring Physician Advisor review. If this box is checked and the unmet review is not sent for physician review, the review will still be stored in the NUMI database as an unmet review, and included in the unmet review reporting.

To indicate that a Physician Advisor Reviewer is not required

1.  *Click* the \<Check here if criteria is NOT MET and formal hospital policy does NOT require physician review\> checkbox beside the Physician Advisor Reviewer dropdown list for the desired patient.
2.  Click the \<FINAL SAVE/Lock to Database\> button.
3.  A Physician Advisor Reviewer review will not be created.

![](numi-user-guide-version-15-15/172.png)

<span id="_bookmark187" class="anchor"></span>Figure 121: Physician Advisor Reviewer review not required checkbox indicator

![](numi-user-guide-version-15-15/173.png) If the checkbox is selected, you do not have to choose a Physician Advisor (and no Physician Advisor review will be created). If a Physician Advisor had been selected from the dropdown and the checkbox was then selected, you will see a warning when you try to save the review: A PUMA name and the box indicating no PUMA review needed cannot be selected at the same time. Please either remove the PUMA name or uncheck the box.

![](numi-user-guide-version-15-15/174.png) If your facility policy does not require Physician Advisor review, the reviews that do not meet criteria will be included in reports and treated the same as all other reviews (including the requirement to select a Stay Reason and Recommended Level of Care), except that there is no Physician Advisor Review attached to the primary review.

### Changing the Next Review Reminder Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this feature to indicate when the next review should be performed. The default is the next day's date. This feature can also be used to defer reviews.

> For example, if a patient is going to be in the ICU for the next 3 days, you might choose to defer the next review and use the time to review other higher priority stays, then catch up with the deferred reviews later.

#### To change the next review reminder date

1.  *Click* on the dropdown box beside the Calendar icon.
2.  Scroll through the calendar screens and select the desired date by *clicking* on it (date field and calendar are shown the figure below) OR
3.  *Type* the desired date into the Next Review Reminder field.

![](numi-user-guide-version-15-15/175.png)

<span id="_bookmark190" class="anchor"></span>Figure 122: Next Review Reminder Date field with calendar displayed

![](numi-user-guide-version-15-15/176.png) When a patient review reminder is set to a day outside of a date filter range, then the patient stay will disappear from the list. If you would like to use the "Patient Selection/Worklist" in such a way that when a review is performed, the patient disappears from the list, set the reminder date on the *Primary ReviewSummary* to an appropriate future reminder date (e.g., the next day), and then set the date filters to have an End Date prior to that day. If you do not want the reviews to disappear from your "Patient Selection/Worklist", then leave the End Date filter blank.

### Indicating No More Reviews on a Stay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this feature to indicate that no more reviews will be performed on a stay. For example, you might use this in a situation where a patient is discharged on Sunday, and a Continued Stay review was performed for Saturday. The patient is now discharged and the review no longer meets criteria. Selecting this option will ensure that the review no longer appears on the Patient Selection/Worklist unless a subsequent VistA movement brings the patient back to the list.

#### To indicate that you will not be doing further reviews on a stay

1.  *Click* the \<Check this box if you will not be doing further reviews on this stay\> checkbox.
2.  *Click* the \<FINAL SAVE/Lock to Database\> buttons to dismiss the reminder.

![](numi-user-guide-version-15-15/177.png)  
<span id="_Hlk169014933" class="anchor"></span>Figure 123: Further Review on Stay checkbox

![](numi-user-guide-version-15-15/178.png) Once you indicate that you will not be doing any further reviews on a stay, it will be removed from the table on the *Patient Selection/Worklist*. It will display on the screen again *only* after someone goes to the *Dismissed Patient Stays* and performs another review on it (See Section 10.3 for more information about the *Dismissed Patient Select* screen).

> **NOTE:** Another movement may cause a stay to re-display on the *Patient Selection/Worklist*.

### Admitting Physician

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the initial patient review, if the Admitting Physician field is not already populated by VistA, the reviewer should select an Admitting Physician.

#### To select the Admitting Physician

1.  *Click* on the Admitting Physician dropdown.
2.  Select an option from the dropdown by clicking on it.

![](numi-user-guide-version-15-15/179.png)  
<span id="_Hlk169014945" class="anchor"></span>Figure 124: Admitting Physician dropdown

#### Adding an Admitting/Attending Physician

If you cannot find your doctor in the Admitting Physician/Attending Physician dropdowns, you can add him/her to the dropdown using the "Add Physician" text box. The new physician name along with the current site ID will be added to the Physician table.

#### To add an Admitting/Attending Physician

1.  *Click* on the Add Physician button.
2.  In the pop-up window, type the Physician's name.
3.  *Click* the Submit button.
4.  The new physician and current site ID are added to the Physician table.

![](numi-user-guide-version-15-15/180.png) As long as the physician's name and the site ID are unique, they will be added and available for selection from the dropdown. Every attempt should be made by the user to carefully examine the list to avoid duplicate name entry. The new Physician name should be entered in the format "*LastName, FirstName (space) OptionalMiddleInitial*." Entries should not include titles (Dr. RN, etc.) and are limited to 100 characters in length. If you attempt to enter a duplicate physician, you will receive a warning: "The entered Physician Name already exists for your site. Please choose the Physician from the existing Physician drop down list(s)."

![](numi-user-guide-version-15-15/181.png)

<span id="_bookmark197" class="anchor"></span>Figure 125: Warning for Duplicate Physician Name

![](numi-user-guide-version-15-15/182.png) Attempts to enter a blank physician name in the Admitting Physician dropdown will not be accepted.

![](numi-user-guide-version-15-15/183.png)

<span id="_Hlk169014964" class="anchor"></span>Figure 126: Warning for Blank Physician Name

### Working with Admission Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select a patient for an Admission review and navigate to the *Primary Review* screen, the system will display the following list of options in the Admission Sources dropdown:

- Scheduled Admission
- Unscheduled Admission – ED
- Unscheduled Admission – Clinic
- Unscheduled Admission – Other
- Transfer in – from VA Facility
- Transfer in – from non-VA Facility
- Other

![](numi-user-guide-version-15-15/184.png)

<span id="_bookmark200" class="anchor"></span>Figure 127: Admission Source Options

#### Select /Change Admission Sources

#### To select or change the Admission Sources

1.  *Click* on the Admission Source dropdown.
2.  Select an option from the dropdown by clicking on it.

#### Selecting or Changing Attending Physician

> NUMI gives you a convenient way to select or change the Attending Physician information for a review, and associate the review with the correct Attending. This feature is especially handy in cases where the Attending information from VistA is not provided or is incorrect.

#### To select or change Attending Physician

1.  *Click* on the Attending Physician dropdown.
2.  Select a new Attending by *clicking* on the name OR
3.  Change the Attending by *clicking* on the dropdown and selecting another name.

![](numi-user-guide-version-15-15/185.png)

<span id="_bookmark203" class="anchor"></span>Figure 128: Attending Physician dropdown

### Selecting or Changing Treating Specialty

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To select or change the Treating Specialty

1.  *Click* on the Treating Specialty dropdown.
2.  Select a Treating Specialty by *clicking* on it. OR
3.  Change the Treating Specialty by *clicking* on the dropdown and selecting another one.

![](numi-user-guide-version-15-15/186.png)

<span id="_Hlk169014999" class="anchor"></span>Figure 129: Treating Specialty dropdown

### Selecting or Changing Service Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To select or change the Service Section

1.  *Click* on the Service Section dropdown.
2.  Select a Service Section by *clicking* on it. OR
3.  Change the Service Section by *clicking* on the dropdown and selecting another one.

![](numi-user-guide-version-15-15/187.png)

<span id="_Hlk169015008" class="anchor"></span>Figure 130: Service Section Dropdown

![](numi-user-guide-version-15-15/188.png) There may be instances where you may expect to see a particular Ward, Treating Specialty, Service Section or Admitting Physician, but the information does not display. The NUMI database will not include this information until NUMI first finds it in a patient movement record from VistA.

![](numi-user-guide-version-15-15/189.png)

<span id="_Hlk169015012" class="anchor"></span>Figure 131: No Records Found

![](numi-user-guide-version-15-15/190.png)While you cannot manually add this information to the dropdowns, you can use the Manual VistA Synchronization feature (please see Section 10.6 for more information). Once the information has been synchronized and pulled into NUMI, the information will display in the dropdowns.

### Selecting or Changing Ward

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To select or change the Ward

1.  *Click* on the Ward dropdown.
2.  Select a Ward by *clicking* on it. OR
3.  Change the Ward by *clicking* on the dropdown and selecting another one.

![](numi-user-guide-version-15-15/191.png)<span id="_bookmark209" class="anchor"></span>

Figure 132: Ward dropdown

### Adding Custom Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may wish to enter special notes, to be used when you are doing a focused study or doing special tracking of some issue. NUMI provides you with a field specifically for that purpose. Some examples of when this feature would be used are:

- Tracking diabetic-related admissions
- Tracking Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF) patients
- Entering the Admitting Physician
- Flagging this review for special studies

#### To add a custom note

1.  *Click* in the Custom field and type in up to 25 characters.
2.  Click the \<FINAL SAVE/Lock to Database\> button and your notes will be saved.

![](numi-user-guide-version-15-15/192.png)

<span id="_bookmark211" class="anchor"></span>Figure 133: Custom field text example

![](numi-user-guide-version-15-15/193.png)The Enhanced Reports let you generate a report showing notes that were typed into the Custom field. Enhanced Reports are available through a link on the NUMI Reports Menu.

### Indicating an Unscheduled Readmit within 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This checkbox feature will only display on the screen if you are doing an admission or initial review. Use this feature to indicate that a patient was an unscheduled readmit to the hospital within the past 30 days.

![](numi-user-guide-version-15-15/194.png)

<span id="_bookmark213" class="anchor"></span>Figure 134: Unscheduled Readmit within 30 Days checkbox

#### To indicate an unscheduled readmit within 30 days

1.  *Click* on the Check if Unscheduled Readmit Within 30 Days checkbox to select.
2.  ![](numi-user-guide-version-15-15/195.png) The Enhanced Reports let you generate a report showing reviews performed on unscheduled readmissions. Enhanced Reports are available through a link on NUMI Reports Menu.

### Working with Admission Review Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review Type information comes over to NUMI in a separate field from CERMe. The Admission Review Type dropdown list will <u>only</u> be displayed if the review type is an Admission review. If the review type is Continued Stay, the dropdown will not be displayed.

![](numi-user-guide-version-15-15/196.png)

<span id="_bookmark215" class="anchor"></span>Figure 135: Admission Review Type dropdown

#### Admission Review Types for Admission Reviews

When you select a patient for an Admission review and navigate to the *Primary Review* screen, the system will display the following list of options in the Admission Review Type dropdown:

- Admission
- Continued Stay

![](numi-user-guide-version-15-15/197.png)

<span id="_Hlk169015060" class="anchor"></span>Figure 136: Review Type Options

#### Select / Change Admission Review Type

#### To select or change the Admission Review Type

1.  *Click* on the Admission Review Type dropdown.
2.  Select an option from the dropdown by *clicking* on it. Hover the mouse pointer over the dropdown option to see a tooltip on a selection of multiple choices.

![](numi-user-guide-version-15-15/198.png) If you create an Admission Review and do not select an Admission Review Type and then try to save/lock the review, a red error message will display and advise that you must select one of the valid types.

![](numi-user-guide-version-15-15/199.png)

<span id="_Hlk169015068" class="anchor"></span>Figure 137: Admission Review Type error message

![](numi-user-guide-version-15-15/200.png)If you select an "Observation Review" under Admission Review Type for a non-observation Treating Specialty and the day being reviewed is same as the Admission day you will see a warning message as below. This will prevent users from making a selection that will cause a stay to accumulate observation hours for a non-observation Treating Specialty.

![](numi-user-guide-version-15-15/201.png)

<span id="_Hlk169015074" class="anchor"></span>Figure 138 : Observation Review warning message

![](numi-user-guide-version-15-15/202.png)The information that displays on the Enhanced reports will depend on the Admission Review Type that is selected on the Primary Review Summary screen.

### Showing a Patient's Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To show reviews for a patient

1.  *Click* on the \<Show Reviews\> button.
2.  Reviews for the patient will display in a table.

> (NOTE: The button display changes to \<Hide Reviews\>.)

![](numi-user-guide-version-15-15/203.png)

<span id="_bookmark221" class="anchor"></span>Figure 139: Show Reviews table display

### Copying a Review from the Primary Review Screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To copy a review from the Primary Review Summary screen

1.  *Click* on the \<Show Reviews\> button.
2.  Reviews for the patient will display in a table.
3.  *Clicking* a <u>View</u> hyperlink in the table will display the \<Copy This Review\> button, and you can make a copy of the review from there.

### Viewing CERMe Review Text 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The lower half of the *Primary Review Summary* screen displays CERMe Review Text. What displays depends on the criteria that have been selected, and is read-only. An example is shown in the figure below. All possible subset criteria are displayed with an \[X\] to the left of the selected criteria.

![](numi-user-guide-version-15-15/204.png)

<span id="_bookmark225" class="anchor"></span>Figure 140: CERMe Review Text example

### Saving and Locking a Final Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This feature will save and lock a review to the database. In order to be included in NUMI reports, a review must be locked into the database. If you lock a review and then later need to amend it, you can do this by clicking on the <u>View</u> link in the Reviews Table on the *Patient Stay History*...

> Clicking on <u>View</u> for a locked review will produce the saved review with boxes that allow you to unlock and edit, delete, or copy the review.

#### To save changes to the database and lock the review

1.  The message "This review will now lock into the NUMI Database. Are you sure you are ready to lock this review?" will display with \<OK\> and \<Cancel\> buttons.
2.  *Click* the \<OK\> button.
3.  While this period of saving and checking is occurring, all buttons and links on the page will be disabled, and an on-screen textual legend will appear, reading "Saving review. Please wait" this legend will disappear when the saving and checking are complete.

![](numi-user-guide-version-15-15/205.png)

<span id="_Hlk169015105" class="anchor"></span>Figure 141: Saving review legend

> Additionally, if users attempt to leave the *Primary Review Summary* screen without saving their work, they will be informed of this fact via a dialog box, and be prompted as to whether they really wish to abandon their changes.

![](numi-user-guide-version-15-15/206.png)

<span id="_Hlk169015111" class="anchor"></span>Figure 142: Unsaved review message

4.  The review will be locked and saved to the database and can then be accessed from the *Utilization Management Review Listing* screen in view-only format. (Please see Section 10.2 for more information about the *Utilization Management Review Listing* screen).
5.  Rarely, NUMI may save a "not met" review without the reason code. If that happens, a message will appear asking you to open and re-save the review: ("The review reason did not save correctly, you must unlock this review and re-enter the reason.") This is a timing issue with NUMI, and opening and re-saving is a work-around to make sure both the review and the reason code are saved permanently.

If NUMI cannot confirm that the data has been saved, it will not proceed to the next screen. It will instead display an error message, "An error occurred during commit…" and leave the review data previously entered on the screen. The reviewer may again attempt to save the data.

![](numi-user-guide-version-15-15/207.png)

<span id="_Hlk169015116" class="anchor"></span>Figure 143: Commit error

![](numi-user-guide-version-15-15/208.png) Only reviews with 'Do not Meet Criteria' status will go to the *Physician Advisor Review screen* from the *Primary Review Summary* screen.

All reviews that are locked (both 'Meets Criteria' and 'Do not Meet Criteria' statuses) will automatically be reported in the Date of Last Review field on the *Patient Selection/Worklist.*

![](numi-user-guide-version-15-15/209.png) If you would like to perform another review on the same patient stay, you can do this by selecting a saved review from the Reviews table and copying it. There is a gold button on the Patient Stay History and Primary Review Summary screens that you can click on to see a listing of the saved reviews on a patient stay and make a copy from there, as well. (See Chapter 13 for more information). Reminder: the system will only permit you to save one continued stay review per day.

![](numi-user-guide-version-15-15/210.png) When you create a review, the Review Type comes pre-populated from CERMe. In some instances, CERMe does not do this and the Review Type field is blank.

NUMI will not let you save a review without the review type information. If the review you are working on has no review type information and you try to save it, you will now see the message: "Review Type cannot be blank. Please return to CERMe to select a Review Type and re-enter criteria." To continue with your review, click the CERMe tab at the top of the Primary Review Summary screen, reselect your CERMe criteria, and you will be able to complete your review and save it.

### Days Since Last VA Acute Care Discharge Calculation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI system calculates the number of days since a patient's last discharge from a VA facility. It displays the number in the Days Since Last VA Acute Care Discharge field. The field is above the Check if Unscheduled Readmit Within 30 Days checkbox field.

> If the value in the field is over 30 days, the reviewer will know that it is not possible for the stay to be an unscheduled readmission in less than 30 days. If the value in the field is less than 30 days, the reviewer would then consider whether the stay is unscheduled.

![](numi-user-guide-version-15-15/211.png)<span id="_bookmark231" class="anchor"></span>

Figure 144: Days Since Last VA Acute Care Discharge field

#### Calculation Rules

The NUMI system shall display an error message, "The last VA discharge date is not available" in the Days Since Last VA Acute Discharge field when a prior stay does not have a discharge date.

The NUMI system shall display "n/a" in the Days Since Last VA Acute Discharge field when there is no VA facility discharge.

The NUMI system shall display the number of days between the last VA facility discharge date and the current VA facility admission date in the Days Since Last VA Acute Discharge field when there has been a prior VA facility discharge.

## Primary Review Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Saved Review Summary* screen offers a synopsis of information saved from the *Primary Review* screen. This is accessed through the *Utilization Management Review Listing* screen, the Stay History screen and by clicking the <u>View</u> hyperlink.

![](numi-user-guide-version-15-15/212.png)

<span id="_Hlk169015142" class="anchor"></span>Figure 145: Saved Review Summary

Fields of interest include the following Primary Review Screen data available on the Review Summary screen:

- Review ID The review ID number is displayed on the summary page title.
- Admitting Physician: The Admitting Physician will display if selected on the Primary Review screen.
- Admission Source: The Admission Source will display if selected on the Primary Review screen.
- Reason Code: The Reason Code will be viewable on the Saved Review Summary Screen for reviews where the criteria were not met.
- Reason Description: The Reason Description will be viewable on the Saved Review Summary Screen for reviews where the criteria were not met.

## Physician Advisor Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the *Physician Advisor Review* screen. Physician Advisors access this screen by selecting the Physician Advisor Review option from the *Tools* menu.

> This screen lets Physician Advisors see the reviews that have been sent to them (including the name of the sender). The features of this screen are listed in Table 7.

![](numi-user-guide-version-15-15/213.png) If you do not have Physician Advisor permissions, you will not see the Physician Advisor Review option in the *Tools* menu dropdown.

| FEATURES                                    |
|---------------------------------------------|
| The Physician Advisor Review                |
| Select a Physician Advisor Review           |
| Agree / Disagree with Current Level of Care |
| Enter Physician Advisor Review Comments     |
| FINAL SAVE/Lock To Database                 |

<span id="_Hlk169015218" class="anchor"></span>Table 8: Tools Menu features

![](numi-user-guide-version-15-15/214.png) All reviews that are locked (both 'Meets Criteria' and 'Do not Meet Criteria') will automatically go to the *Patient Selection/Worklist* screen from the *Physician Advisor Review* screen.

### Physician Advisor Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When this screen first opens, Physician Advisors will see a table with reviews that did not meet criteria and have been sent to them from a UM reviewer. If there are no reviews assigned, their list will be empty and "No Records Found" will display. By default, the "Current Lookup Site" selection is set to "All". This list can be narrowed down by selecting a different site from the "Current Lookup Site" dropdown and clicking the "Go" button.

> ![](numi-user-guide-version-15-15/215.png)

<span id="_Hlk169015173" class="anchor"></span>Figure 146: Physician Advisor Review with no reviews assigned

![](numi-user-guide-version-15-15/216.png)The Review Date column on the screen will always display the date with a time of 00:00:00 underneath. This is not an error. The time will always display as 00:00:00 (Midnight) because reviews are for the CALENDAR DAY.

![](numi-user-guide-version-15-15/217.png)

<span id="_Hlk169015177" class="anchor"></span>Figure 147: Physician Advisor list of reviews sent by Reviewers

### Selecting a Physician Advisor Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To select a review from the list

1.  On the *Physician Advisor Review* screen, *click* on the Review hyperlink on the far-right side of the row of the review you wish to access.
2.  The Physician Advisor Review summary for that patient will display below the *Physician Advisor Review* screen.
3.  Immediately below the review list, you will see Care is Clinically indicated and clinically not indicated selections and a Comments box. This is where the Physician Advisor enters information. Selection about care is required from the Physician Advisor but, comments are optional.
4.  Below *Physician Advisor Review* section, the entire review is available for review.

> ![](numi-user-guide-version-15-15/218.png)

<span id="_Hlk169015189" class="anchor"></span>Figure 148: Physician Advisor Review Screen

### Agreeing / Disagreeing with Current Level of Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this feature to show concurrence or non-concurrence with the indicated Current Level of Care.

#### To Agree with the Current Level of Care

1.  Select Care IS clinically indicated.

#### To Disagree with the Current LOC

1.  Select Care is NOT clinically indicated.

![](numi-user-guide-version-15-15/219.png)

<span id="_Hlk169015199" class="anchor"></span>Figure 149: Physician Advisor Review Selection

### Entering Physician Advisor Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter Physician Advisor comments

1.  *Type* the desired comments into the Comments window. (You may type up to 4,000 characters).
2.  When you *click* the \<FINAL SAVE/Lock to Database\> button, your comments will be saved.

### Saving and Locking a Final Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This feature will save and lock a review to the database.

#### To save changes to the database and lock the review

1.  *Click* the \<FINAL SAVE/Lock to Database\> button.
2.  The message "This review will now lock into the NUMI Database. Further changes require an administrator. Are you sure you are ready to lock this review?" will display, with \<OK\> and \<Cancel\> buttons.
3.  *Click* the \<OK\> button. The review will be locked and saved to the database and can then be accessed from the *Utilization Management Review Listing* screen in read-only format. (Please see Section 10.2 for more information about the *Utilization Management Review Listing* screen).

## Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the *Tools* Menu, which offers you different options that can be selected by clicking on them. It is a navigation menu that includes some features that are accessible through other screens and other features only accessible here. The *Tools* Menu dropdown is located at the top of several NUMI screens.

> You can choose options related to selecting patients and reviews, unlocking and deleting reviews (see Chapter 13 for more information), locating dismissed patient movements, accessing the Physician Advisor Worklist (if you are designated as a Physician Advisor on NUMI), and on-demand synchronization of stay information between VistA and NUMI.

> NOTE: The features you see in the dropdown will depend on your NUMI privileges (e.g., Physician Advisors will not see the Patient Selection/Worklist option; Primary Reviewers will not see the Physician Advisor Review, etc.). The features on the *Tools* Menu are listed in Table 8.

<table>
<caption><p><span id="_Hlk169015596" class="anchor"></span>Table 9: Admin Users features</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>FEATURES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient Selection/Worklist Option</td>
</tr>
<tr class="even">
<td><p>Utilization Management Review Listing Option</p>
<p>(includes Unlock/Copy/Delete options)</p></td>
</tr>
<tr class="odd">
<td>Dismissed Patient Stays Option</td>
</tr>
<tr class="even">
<td>Free Text Search Option</td>
</tr>
<tr class="odd">
<td>Physician Advisor Review Option</td>
</tr>
<tr class="even">
<td>Manual VistA Synchronization Option</td>
</tr>
<tr class="odd">
<td>Patient Stay Administration Option</td>
</tr>
<tr class="even">
<td>Logout Option</td>
</tr>
</tbody>
</table>

<span id="_Hlk169015596" class="anchor"></span>Table 9: Admin Users features

![](numi-user-guide-version-15-15/220.png)

  
<span id="_Toc168998378" class="anchor"></span>Figure 150: NUMI Tools Menu

### Patient Selection/Worklist Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select this option to work with the *Patient Selection/Worklist* screen, where you can select stays to perform primary reviews. This screen also contains paging features that allow you to navigate thru the information in the table on the screen. Use of the paging features is explained in Section 2.12.7. The Find and Reset buttons are available on the right side of the screen. Please see Chapter 5 for more information about the *Patient Selection/Worklist*.

#### To work with the Patient Selection/Worklist

1.  *Click* on the *Tools* dropdown.
2.  Select the \< Patient Selection/Worklist\> option by *clicking* on it and the *Patient Selection/Worklist* will display.

![](numi-user-guide-version-15-15/221.png)

<span id="_Hlk169015242" class="anchor"></span>Figure 151: Patient Selection/Worklist Screen

### Utilization Management Review Listing Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select this feature to work with the *Utilization Management Review Listing* screen, where you can see reviews that have been saved or unlocked for editing. Section 2.10 explains how to use the filters at the top of the screen, and use of the paging features is covered in Section 2.12.13.

> Observation stays can be included in results. Please see Section 4.3 for more information.

> NUMI reviewers will be able to Unlock, Copy, and Delete reviews (See Chapter 12 for details about NUMI's Unlock and Delete features and Chapter 13 for details on copying.) The hyperlinked patient name brings you to the Review Summary and CERMe Review Text screen for that particular patient.

> To work with the Utilization Management Review Listing

1.  Click on the Tools dropdown.
2.  Select the \<Utilization Management Review Listing\> option by *clicking* on it.
3.  The Utilization Management Review Listing screen will display.
4.  Selecting filters to search by and *clicking* the \<Find\> button will display a list of patients based on your search criteria.

![](numi-user-guide-version-15-15/222.png) Locked reviews will display a blue hyperlink with a tooltip "Review saved". Clicking on these will open the *Review Summary* screen. Reviews that have been unlocked for editing will display a red hyperlink with a tooltip "Review not saved". Clicking on these will open the *Primary Review* screen. An example of the screen with red and blue links is shown below.

#### Filtering Reviews by Free Text

To filter by Free Text

1.  Type directly in the Free Text field.
2.  Click the \<Find\> button and the results will display in a table. To select a patient, *click* on their hyperlinked name in the Patient Name column.

![](numi-user-guide-version-15-15/223.png) Using Free Text, you can search for an exact word or phrase, for synonymous words, for partial words, or for a specific word, and the system will check the database for certain information.

![](numi-user-guide-version-15-15/224.png) (The system searches the following to try to match what you've entered: treating specialty, ward, patient name and SSN, movement, reviewer name, attending physician name, comments, custom notes, and admitting diagnosis.

If the admitting physician name has been manually entered in the custom notes or comments fields, the search will find it).

#### Filtering Reviews by Date

To filter by Date

1.  *Click* on the Date filter checkbox to activate it.
2.  Select a date from the Start Date dropdown by *clicking* on it. (Start Date is from 12:00 a.m. that day)
3.  Select a date from the End Date dropdown by *clicking* on it. (End Date is until 11:59 p.m. that day)
4.  *Click* the \<Find\> button and the results will display in a table.

![](numi-user-guide-version-15-15/225.png) To select only one day, select the same date for the Start and End Date fields. Entering the Start Date only will give you the start date and everything after. Entering the End Date only will retrieve everything up to, and including, the end date.

#### Filtering Reviews by Reviewer

To filter by Reviewer

1.  *Click* on the Reviewer filter checkbox to activate it.
2.  Select another option from the dropdown by *clicking* on it OR
3.  Select "All" to see all (regardless of whether a reviewer has been assigned or not) OR
4.  *Click* the \<Find\> button and the results will display in a table.

#### Filtering Reviews by Attending

To filter by Attending

1.  *Click* on the Attending filter checkbox or activate it.
2.  Select an Attending from the dropdown list by clicking on it OR
3.  Select "All" to see the Attending's for all reviews OR
4.  Click the From VistA checkbox to see Attending's from VistA OR
5.  Click the Corrected checkbox to see all Attending's that were corrected after coming across to NUMI from VistA.
6.  Click the \<Find\> button and the results will display in a table

#### Filtering Reviews by Ward

To filter by Ward

1.  *Click* on the Ward filter checkbox to activate it.
2.  Select a Ward from the list by *clicking* on it. To select multiple Wards, *click* on one, then hold the \<Ctrl\> key down and *click* on others. You can also press and hold the \<Shift\> key down to select a block of Wards OR
3.  Select "All" to see the Wards for all reviews.
4.  *Click* the \<Find\> button and the results will display in a table.

![](numi-user-guide-version-15-15/226.png) There may be instances where you may expect to see a particular ward in the Ward dropdown, but it does not display. Ward lists are populated as movements for those wards occur. For example, a patient you are looking for has been in a bed for a while and has not had any movements. Their information has not been picked up by the overnight synchronizer yet because there were not any qualifying movements. While you cannot manually add a ward to the dropdown, you can use the Manual VistA Synchronization feature (please see Section 10.6 for more information) to search for a patient that you know is in a particular ward. Once their information has been synchronized and pulled into NUMI, that ward will display in the Wards dropdown.

#### Filtering Reviews by Treating Specialty and Service

To filter by Treating Specialty and Service

1.  *Click* on the Treating Specialty and Service filter checkbox to activate it.
2.  Select options from the Treating Specialty and/or Service dropdowns by *clicking* on them.
3.  *Click* the \<Find\> button and the results will display in a table.

#### Filtering Reviews by Review Type

To filter by Review Type

1.  *Click* the Review Type filter checkbox to activate it.
2.  Select an option from the dropdown by *clicking* on it.
3.  *Click* the \<Find\> button and the results will display in a table.

### Dismissed Patient Stays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This feature opens the Dismissed Patient Stays screen. This is where patient stays that were dismissed from the Patient Selection/Worklist screen will display. The screen contains the same filters that appear on the Patient Selection/Worklist screen. Section 2.10 describes the use of these filters. Observation stays can be included in results.

Please see Section 4.3 for more information. The hyperlinked patient name brings you to the NUMI Patient Stay History screen for that particular patient. The Dismiss Stays button is also available for dismissing selected stays with the selected Dismiss Type. For more information about dismissing patient stays, please see Section 4.5.

> When the screen opens, a series of filters will display. The Date checkbox will be pre-selected, as will the Start Date and End Date checkboxes. Also pre-populated is a 1 week date range, to include the last day of the week.

The default Start and End dates will appear as the last week, even after clicking the Reset button, but each time they appear on the screen, these dates can be changed.

After obtaining search results, this screen could potentially display several thousand stays, so paging features have been built into it so you can view next, previous, first and last pages, and indicate how many rows of results you would like to see in each page of the table.

The following informational message displays on the screen under the Find and Reset buttons: "Click FIND to list all dismissed stays meeting the filters specified above. To create a different stay list, click RESET, select your filter criteria and click FIND."

A Dismissal Type checkbox below the Reviewer criteria allows you to select Dismissal Type search criteria from the dropdown. When you initiate a search, these criteria will be applied to your search. After a search, the Dismissed Patient Stays Screen presents three related columns: Dismissed By, Dismissed On, and Dismissal Type.

![](numi-user-guide-version-15-15/227.png) "Non-reviewable" Treating Specialties (i.e., Domiciliary, Nursing Home, Outpatient and Rehab) and Treating Specialties configured as non-reviewable will be intercepted as they come from VistA into NUMI, and automatically moved to the *Dismissed Patient Stays* screen during nightly, hourly and manual Synchronization. ("Inactivated" stays will not appear on the *Patient Selection/Worklist* screen unless a review is performed on them). To identify stays that are not reviewable, the system looks for treating specialties that are configured as non-reviewable. It also looks for one of the following character sequences in the Treating Specialty description: DOM, NH, OUTPATIENT, and REHAB. The system then sets the stays to 'dismissed' and moves them to the *Dismissed Patient Stays* screen. If one of the special character sequences is configured as reviewable it will appear on the worklist because configuration overrides the character sequence search.

![](numi-user-guide-version-15-15/228.png) While working on the screen, you may see a message, "Error Occurred Loading the Page. Please click your browser's Refresh button and try again" advising there was a problem loading the webpage. Refreshing your browser will reload the webpage and display the NUMI screen. You may also want to 1.) Check to see if you have a blank Start Date and/or End Date field and 2.) Check to see if the date range you have selected produces too many stays in the results. Narrow your date range to produce a smaller number of stays.

#### To work with the Dismissed Patient Stays

1.  *Click* on the *Tools* dropdown.
2.  Select the \< Dismissed Patient Stays \> option by *clicking* on it and the *Dismissed Patient Stays* screen will display.
3.  Select the desired search filters and *click* the \<Find\> button (If there are no dismissed movements, 'No Records Found' will display on the screen).
4.  After the results display, to see a particular patient stay, *click* on the hyperlinked patient name in the Patient Name column.

![](numi-user-guide-version-15-15/229.png) Once a patient review has been performed, the patient's name will be removed from the *Dismissed Patient Stays* screen and will re-display on the *Patient Selection/Worklist* screen.

![](numi-user-guide-version-15-15/230.png)

<span id="_Hlk169015335" class="anchor"></span>Figure 152: Dismissed Stays screen with 1-week default date range

> After obtaining search results on the *Dismissed Patient Stays* screen, when you click on the Reset button the system will restore all fields to their default values, except the 1-week default date range. The fields and default values are:

- Date – Checkbox selected and defaults with a 1-week range (this timeframe keys off the Next Review Date)
- Reviewer – Checkbox not selected and will display the logged in user's name
- Ward – Checkbox not selected and defaults to "All"
- Treating Specialty and Service – Checkbox not selected and defaults to "All"
- Movement– Checkbox not selected and no default values display
- Patient Search – Checkbox not selected and no default values display

### Free Text Search Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This feature lets you type information in and search by exact words, similar words, partial words or specific words. Observation stays can be included in results. You can filter by Date, Reviewer, Ward, Treating Specialty and Service, Movement and Patient Search. When you search using free text, the system will check for certain types of information.

To work with the Free Text Search option

1.  *Click* on the *Tools* dropdown.
2.  Select the \<Free Text Search \> option by *clicking* on it and the *Free Text Search* screen will display. (See Section 2.10 for more information about how to use NUMI filters and Section 10.2.4 for more information about using the free text search options).
3.  To select a patient for review from the *Free Text Search* screen, just click on the hyperlinked name of the patient.

### Physician Advisor Review Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This feature opens the *Physician Advisor Review* screen. This option is where

> Physician Advisors will be able to access and work on the reviews that have been assigned to them.

To work with the Physician Advisor Review

1.  *Click* on the *Tools* dropdown.
2.  Select the \<Physician Advisor Worklist\> option by *clicking* on it.
3.  The *Physician Advisor Review* screen will open. If a Physician Advisor has reviews assigned to them, the reviews will display in a table.

![](numi-user-guide-version-15-15/231.png) Only reviews with 'Do not Meet Criteria' status will go to the *Physician Advisor Review*.

![](numi-user-guide-version-15-15/232.png)

<span id="_Hlk169015363" class="anchor"></span>Figure 153: Physician Advisor Review screen

### Manual VistA Synchronization Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This feature lets you synchronize stay information between VistA and NUMI. An automatic feed containing admissions, ward transfers, discharges and provider and specialty changes is sent to NUMI from VistA at the top of each hour during the day, and at midnight. Stays that were dismissed the previous day will not redisplay in the *Patient Selection/Worklist* after the midnight synchronizer information feed occurs (NOTE: If information changes in VistA, the information in NUMI will be overwritten / overlaid in the next feed. It should also be noted that resynching with VistA will always update the stay data, but the review data will not be overwritten).

When you synchronize a patient or several patients, you are bringing VistA information on those patients into NUMI and placing those patient stays in your *Patient Selection/Worklist*.

With the Manual VistA Synchronization feature, you do not need to wait for a feed. You can retrieve and synchronize information on-demand. This feature comes in handy when you know a patient has been admitted to the hospital (or transferred to another Ward – a frequent occurrence during the day) and is in VistA, but you do not see them in NUMI yet.

As an added convenience, the table on the screen includes Ward, Specialty and Admitting Diagnosis information to help you identify which patients need to be "synched" onto the *Patient Selection/Worklist*.

![](numi-user-guide-version-15-15/233.png) You can only synchronize by Date OR by Check-in ID OR by Patient on this screen. In addition, please note that if you only enter a date without a patient name, everything for that date will be displayed and can be selected and synchronized.

![](numi-user-guide-version-15-15/234.png) You must click on the Date, Check-in ID or Patient Search radio buttons in order to activate the search filters on the Manual VistA Synchronization screen. For more information about using the filters in NUMI, please see Section 4.4 in this guide.

![](numi-user-guide-version-15-15/235.png) While working on the Manual VistA Synchronization screen, you may see a message in red text advising that the server is busy. Perform your last action (e.g., re- click a button; re-select a hyperlink) to retry.

![](numi-user-guide-version-15-15/236.png)

<span id="_bookmark273" class="anchor"></span>Figure 154: Server Busy Error Message

#### To work with the Manual VistA Synchronization

1.  Click on the Tools dropdown.
2.  Select the \<Manual VistA Synchronization\> option by *clicking* on it and the *Manual VistA Synchronization* screen will display.
3.  *Click* the Date radio button, and select or *type* the desired date in the Movement Start Range field. If you type in the date, use the format mm/dd/yyyy.
4.  Select a specific time range, if desired, by *clicking* in the Hour fields and entering the desired hours (e.g., 06:00 thru 11:00) OR
5.  *Click* the Patient Search radio button, *type* in a Patient name (in \<Lastname, Firstname\> format) and *click* the \<Find Patient\> button. Then *single-click* on a patient name in the result window to select it. If you do not select a patient, the message "You must select a patient" will display OR
6.  *Click* the Check-in ID radio button and *type* in a Check-in ID, if you know it.[^2] (You can always search by Date or Name and the Check-in ID will be displayed in the search results. If the patient is not in NUMI but has an inpatient stay in VistA, you can add them to NUMI by searching for them by date range or patient name. If the patient does not have any inpatient stays in VistA, they will display in the search by patient list but no stays will be returned. If the patient's admission is not in NUMI, you can synchronize with VistA by entering the Admission date, which will add the Admission movement to NUMI.

![](numi-user-guide-version-15-15/237.png) If NUMI still cannot find the admission, you may need to get the VistA Patient Movement file admission movement's internal entry number (IEN) from your local IT and enter it as the Check In ID, then click \<Find Stays in VistA\> and, when the list appears, click on the box to the left of the ones you want to add to NUMI and press \<Synchronize Stays\>. If you cannot find the stay anywhere in NUMI after synchronizing, key data such as ward or treating specialty may be missing from Vista, which can prevent the stay from being included in the NUMI database.

If you have the VistA 'Detailed Inpatient Inquiry' option you can check the stay and you may need to contact an admissions supervisor in your facility if there is a problem. NOTE: The number displayed as the Movement ID on the Patient Stay History screen corresponds to the VistA Patient Movement IEN if the movement already appears in NUMI.

1.  *Click* the \<Find Stays in VistA\> button.
2.  When the search results display, *click* on the checkboxes in the far left column in the row for each patient stay you wish to synchronize into NUMI and display on the Patient Selection/Worklist.
3.  Click the \<Synchronize Stays\> button. The message: "Synchronized \<number\> stays for site \<site number\>" will display on the screen.

![](numi-user-guide-version-15-15/238.png)<span id="_Toc479683409" class="anchor"></span>

Figure 155: Manual VistA Synchronization Search Results Screen

![](numi-user-guide-version-15-15/239.png)

<span id="_Hlk169015404" class="anchor"></span>Figure 156: Stays selected for Synchronizing

![](numi-user-guide-version-15-15/240.png)

<span id="_bookmark276" class="anchor"></span>Figure 157: Synchronized Stays confirmation message

![](numi-user-guide-version-15-15/241.png)

<span id="_bookmark277" class="anchor"></span>Figure 158: Patient Search Message

![](numi-user-guide-version-15-15/242.png) If the stays selected before the \<Synchronize Stay\> button is clicked do not sync properly due to missing fields, the following error message will appear. "The following stays did not sync due to missing fields in the patient data. Please check data in VistA and sync manually again. Stay Id :\< stay id\>

![](numi-user-guide-version-15-15/243.png)

<span id="_Hlk169015414" class="anchor"></span>Figure 159: Patient Sync Error

### Patient Stay Administration Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option can <u>only</u> be used by NUMI Administrators. While non-Administrator users will see this option displayed in the *Tools* menu, selecting it will display an error message (i.e., "You are not authorized to administer patient stays at this site").

> If a VistA patient stay is entered in the NUMI database and VistA subsequently deletes the stay, NUMI will display an "invalid stay" message when the NUMI user clicks the review link for the deleted stay.

> Additionally, NUMI will move the NUMI patient stay record to the *Patient Stay Administration* screen. NUMI Administrators can use the *Patient Stay Administration* screen to verify the status of the stay in VistA and delete NUMI patient stay records that are no longer in VistA.

> Here is some background information about how this process works:

> Patient Stay Movements are entered into VistA and then synchronized into the NUMI database. Every time a stay is touched in NUMI, NUMI goes back to VistA to update the stay record with any changes in VistA. If nothing is returned from VistA when the record is requested, then NUMI marks its record of the stay as "invalid," and removes it from the *Patient Selection/Worklist*. It is put in an indeterminate state, but not deleted.

> NUMI Administrators then review the invalid stays using this screen. Selecting them from the table will cause NUMI to again try to retrieve them from VistA. If NUMI can retrieve the stay, then the Administrator has the option of selecting the Restore button to reactivate the stay.

#### To access the Patient Stay Administration feature

1.  Click on the Tools dropdown.
2.  Select the \<Patient Stay Administration\> option.
3.  The *Patient Stay Administration* screen displays with a list of invalidated stays.

![](numi-user-guide-version-15-15/244.png)

<span id="_Hlk169015431" class="anchor"></span>Figure 160: NUMI Patient Stay Administration Screen

> **NOTE:** Observations can be included in results. Please see Section 4.3 for more information.

#### Finding Patient Stays that were removed from VistA

To find patient stays that were removed from VistA

1.  Choose search filters by *clicking* on the checkboxes in the filter headers. This will activate the options in each filter. (For more information about NUMI filters, please see Section 2.10).
2.  Choose the desired options from each filter and click the \<Find\> button.
3.  A list of patient stay matching your search criteria will display in a table. If your search produces no results, No Records Found will display.

#### Restoring a Patient Stay

To restore a patient stay

1.  *Click* the <u>Validate</u> hyperlink beside the stay you wish to restore.
2.  *Click* the \<OK\> button when this message displays: "Stay \<number\> for patient \<patient name\> has been retrieved from VistA. Please click on the Restore button to set it as valid in NUMI."

![](numi-user-guide-version-15-15/245.png)

<span id="_Hlk169015446" class="anchor"></span>Figure 161: Stay retrieval advisory message

3.  *Click* the Restore button in the center of the screen.
4.  The screen will refresh and the patient record will no longer display in the table.
5.  The patient will display in the table on the *Patient Selection/Worklist* screen.

![](numi-user-guide-version-15-15/246.png)

<span id="_Hlk169015454" class="anchor"></span>Figure 162: Patient Stay Administration with Restore button displayed

#### Accessibility Feature

> Keyboard only users may optionally navigate directly to the Stay Summary the most recently validated stay an entry by pressing alt+x. This must be done after closing the message box for the stay validation but before validating the next stay.

> ![](numi-user-guide-version-15-15/247.png)

<span id="_Hlk169015458" class="anchor"></span>Figure 163: Stay Summary

### Logout Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This feature will take you to the logout screen.

To access the Logout option

1.  *Click* on the *Tools* dropdown.
2.  Select the \<Logout\> option by *clicking* on it.
3.  The *Logout* screen opens.

## Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Reports* Menu dropdown is on the menu bar located along the top of most NUMI screens.

![](numi-user-guide-version-15-15/248.png)

<span id="_Hlk169015473" class="anchor"></span>Figure 164: Reports Menu

NUMI Enhanced reports are available to all registered VA network users with access to NUMI and a NUMI profile that allows report access. The below link will take you there:

https://dvagov.sharepoint.com/sites/vhaum/SitePages/Enhanced-Reports-2.0.aspx

> **NOTE:** You must have logged in to NUMI at least once in order to get your facility list to appear in the Enhanced Reports facility dropdown.

## Unlocking and Deleting Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The features for unlocking Primary and Physician Advisor Reviews, and Deleting reviews are accessed from the *Utilization Management Review Listing* screen, which is located on the *Tools* menu.

- Primary Reviewers have the ability to Unlock and Delete their own reviews.
- Administrators have the ability to Unlock and Delete any reviews as long as they do not have an expired Physician Advisor review.
- Administrators can Unlock or Delete reviews, on behalf of Physician Advisors as long as they are not expired.

### Unlocking a Locked Primary Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMI offers the ability for a local NUMI Admin to unlock any Primary Review that was locked to the database at their site. This would be handy in cases where a reviewer might be covering for someone else in the VISN. (NOTE: If there is a Physician Advisor review associated with the Primary Review, unlocking the Primary Review will automatically unlock the Physician Advisor review portion, as well. However, if a PA review was not entered within 7 business days of the review, only a super user will be able to unlock the review.)

![](numi-user-guide-version-15-15/249.png) If a Primary Review that "Did Not Meet" criteria is unlocked and its status changes to "Meets" criteria, the associated Physician Advisor review will be deleted.

#### To unlock a Primary Review that was locked to the database

1.  *Click* on the Utilization Management Review Listing on the *Tools* menu to open the *Utilization Management Review Listing* screen.
2.  Select the desired filter options by *clicking* on them.
3.  *Click* the \<Find\> button and the results will display in a table.
4.  *Click* on the desired <u>Patient Name</u> hyperlink to open the *Review Summary* screen. (You can also get to the *Review Summary* screen from the Reviews table on the *Patient Stay History screen* and the *Primary Review* screen).
5.  The *Review Summary* screen will display with \<Close\>, \<Unlock\> and \<Delete\> buttons.

![](numi-user-guide-version-15-15/250.png)

<span id="_Hlk169015498" class="anchor"></span>Figure 165: Review Summary Window

1.  Click the \<Unlock\> button.
2.  A dialog box displays with the message: "Are you sure you want to Unlock this Review?"
3.  Click the \<OK\> button and the screen will refresh and display: "Successfully unlocked the record" and the \<Unlock\> button on the *Review Summary* screen will now display as \<Review\>.
4.  *Click* the \<Review\> button.
5.  The message "Are you sure you want to review?" displays.
6.  *Click* the \<OK\> button to be redirected to the *Primary Review Summary Screen* where you can continue working on the review.

### Unlocking the Physician Advisor Portion of a Locked Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI offers the ability to unlock <u>just</u> the Physician Advisor portion of a review that has been locked to the database.

Certain events must occur before the \<Unlock Physician Advisor Review\> button will display on the *Utilization Management Review Listing* screen.

A Primary Review that "Does Not Meet" is assigned to a Physician Advisor and locked to the database; the Physician Advisor opens the review from their Worklist, performs a review, and locks the Physician Advisor portion of the review back to the database.

#### To unlock the Physician Advisor portion of a review that was locked to the database

1.  *Click* on the Utilization Management Review Listing on the *Tools* menu.
2.  *Click* on the Patient Name hyperlink for the review.
3.  The Utilization Management Review Listing screen will display with \<Close\>, \<Unlock\>, \<Delete\> and \<Unlock Physician Advisor Review\> buttons.
4.  *Click* the \<Unlock Physician Advisor Review\> button.
5.  Next, the Physician Advisor can open the review from their Worklist, perform a review and lock the Physician Advisor portion of the review back to the database (NOTE: The Primary Review portion of the review remains locked to the database).

![](numi-user-guide-version-15-15/251.png)

<span id="_Hlk169015522" class="anchor"></span>Figure 166: Review Summary with Unlock Physician Advisor Review Button

![](numi-user-guide-version-15-15/252.png) NOTE: If an Advisor Review was not completed in the allotted 7 days and you are not a Super User, trying to unlock the advisor review will result in the following error message: "This Physician Advisor Patient Review is expired and can only be unlocked by a Super User. Current user does not have these privileges."  
  
![](numi-user-guide-version-15-15/253.png)

<span id="_Hlk169015528" class="anchor"></span>Figure 167: Review Summary with Unlock Physician Advisor Review Button Error

### Deleting a Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMI Administrators will use this feature to delete reviews. Primary Reviewers will be able to delete their own reviews. Administrators can delete reviews on behalf of Physician Advisors.

> A review that has been performed on a patient stay might be deleted if that stay has been deleted from VistA. Deleting the review from NUMI will ensure that no 'orphan' stays are on the application.

![](numi-user-guide-version-15-15/254.png) If a Primary Review is deleted, the associated Physician Advisor review will NOT be deleted. There is no way to directly delete a Physician Advisor review. You may, however, unlock it and reassign to another Physician Advisor and even change it completely.

#### To delete a review

1.  *Click* on the Utilization Management Review Listing on the *Tools* menu to open the *Utilization Management Review Listing* screen.
2.  Select the desired filter options by *clicking* on them.
3.  *Click* the \<Find\> button and the results will display in a table.
4.  *Click* on the desired Patient Name hyperlink to open the *Review Summary* screen in a different window.

![](numi-user-guide-version-15-15/255.png) If you select the Review hyperlink, you will not be able to delete the review. You will be taken to the *Primary Review* page where you can continue working on it. If another review is in process, then all changes will be lost unless it has been saved or locked.

1.  The screen will display \<Close\>, \<Unlock\> and \<Delete\> buttons.
2.  Type a Deletion Reason into the text box. (NOTE: You will not be able to delete the review unless you do this first).
3.  *Click* the \<Delete\> button.
4.  A dialog box will display with this message: "Are you sure you want to Delete this Review?"
5.  Click the \<OK\> button, and the screen will refresh and display: "Successfully Deleted the record" and the \<Delete\> button will be grayed out.
6.  Click \<Close\> to return to the Utilization Management Review Listing Screen.

![](numi-user-guide-version-15-15/256.png) Be very careful when using the Delete option. Once a review has been deleted, it cannot be restored.

## Copying Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI simplifies the process of creating multiple reviews for the same patient/stay. You can easily create and save a review by copying another review. This will save you considerable time and effort, especially for weekend stay days and patients awaiting long term care beds and procedures. A review can be copied from the *Patient Stay History* screen, the *Primary Review* screen, or the *Review Summary* screen.

![](numi-user-guide-version-15-15/257.png) IMPORTANT: Do not copy an Admission review. Since Admission reviews are only done once, there is no reason to copy them. (If your intent is to copy the criteria and use it for the following day, note that CERMe will not permit you to do that, and will require you to select the type of review before you select the criteria. If you are doing a Continued Stay review, you will want to be using Continued Stay criteria - not Admission criteria. So, there would not normally be any scenario in which you would copy an Admission review).

### To copy a review from the Patient Stay History Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the *Patient Stay History* screen, *click* the gold Show Reviews tab to display all the reviews.
2.  The Reviews table will open and display all reviews for the patient.
3.  *Click* on a <u>View</u> hyperlink in the table.
4.  The *Review Summary* screen will open and the \<Copy This Review\> button will display.
5.  *Click* the button and an identical copy of the review will be created. You can change anything you need to on the copy, and then save it.

### To copy a review from the Primary Review screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the *Primary Review* screen, *click* the gold Show Reviews tab to display all the reviews.
2.  The Reviews table will open and display all reviews for the patient.
3.  *Click* on a <u>View</u> hyperlink in the table.
4.  The \<Copy This Review\> button will display.
5.  *Click* the button and an identical copy of the review will be created.

![](numi-user-guide-version-15-15/258.png) It is only appropriate to copy a review if the criteria and met/not met outcome have not changed. You can copy a review as many times as you wish.

![](numi-user-guide-version-15-15/259.png)

<span id="_Hlk169015575" class="anchor"></span>Figure 168: Primary Review Summary screen with Copy This Review Button

### To copy a review from the Review Summary screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the *Primary Review* screen, *click* the gold Show Reviews tab to expand the Reviews table.
2.  The original review and all its copies will display.
3.  To see the summary for any review, *click* its <u>View</u> hyperlink.
4.  The *Review Summary* screen will display.
5.  *Click* the \<Copy This Review\> button and an identical copy of the review will be created.

![](numi-user-guide-version-15-15/260.png)

<span id="_Hlk169015586" class="anchor"></span>Figure 169: Review Summary Screen with Print and Copy This Review Buttons

## Admin Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the Admin menu. The menu is located in the Admin dropdown on the Main Navigation Toolbar. Only users with the NUMI Administrator role can use these features.

> On this screen, Administrator users can search for VistA users, add them as NUMI users, add and edit NUMI user information and assign privileges, deactivate user sites, and add/remove users from the Physician Advisor, Primary Reviewer and Site Administrator panels.

> There are 3 Admin options: Users, Admin Site and Treating Specialty Configuration.

> The administrative features of the *Users* screens are listed in Table 9, and the features of the *Admin Sites* screens are listed in Table 10. The Treating Specialty Configuration features are listed in Table 11.

| FEATURES                                                         |
|------------------------------------------------------------------|
| National Utilization Management Integration (NUMI) Users Feature |
| Find VistA Users by Name                                         |
| Find VistA Users by Site                                         |
| Find VistA Users by Status                                       |
| Add NUMI User / Assign Privileges                                |
| View NUMI User information / Privileges                          |
| Edit NUMI User information                                       |
| Deactivate a User's Site                                         |

<span id="_Hlk169015608" class="anchor"></span>Table 10: Admin Site features

| FEATURES                                                                                 |
|------------------------------------------------------------------------------------------|
| National Utilization Management Integration (NUMI)Admin Sites Feature (find VistA Users) |
| Find VistA Users                                                                         |
| Add Users to the Physician Advisor Panel                                                 |
| Add Users to the Primary Reviewer Panel                                                  |
| Add users to the Site Administrators Panel                                               |
| Remove Users from the Physician Advisor Panel                                            |
| Remove Users from the Primary Reviewer Panel                                             |
| Remove Users from the Site Administrators Panel                                          |

<span id="_Hlk169015621" class="anchor"></span>Table 11: Treating Specialty Configuration features

| FEATURES                              |
|---------------------------------------|
| Assign or Update Treating Specialties |

<span id="_Hlk169015888" class="anchor"></span>Table 12: Glossary of Terms

![](numi-user-guide-version-15-15/261.png)

<span id="_Hlk169015625" class="anchor"></span>Figure 170: Admin Menu

### Accessing the NUMI Users Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMI Administrators will use this feature to find VistA users, add/edit NUMI user information including the assignment of user privileges, and deactivate user sites.

![](numi-user-guide-version-15-15/262.png) Note: Administrators that are not "Super Users" cannot edit privileges of "Super Users".

#### To access the NUMI 'Users' feature

1.  *Select* the Admin dropdown and *click* on the Users option. A list of existing NUMI users displays on the NUMI User List screen, as illustrated in the figure below.

![](numi-user-guide-version-15-15/263.png)

<span id="_Hlk169015636" class="anchor"></span>Figure 171: NUMI User List Screen

#### Finding VistA Users by Name

The list of NUMI users can be very long. But you do not have to scroll thru the entire list. NUMI saves you time by letting you search for specific VistA users using a Find feature.

You can search by the user's full name using *lastname, firstname* format (e.g., Smith, John) or you can search by a partial name (e.g., Smi).

Please note that if you search by partial name you may receive a long list of results (e.g., Smi will retrieve all instances of 'smi' in user names (e.g., Goldsmith, Smit, Smith, Smithfield, etc.).

#### To find VistA users by name

1.  Type the user's name into the VISTA User Name field.
2.  Click the \<Find\> button.

![](numi-user-guide-version-15-15/264.png)

<span id="_Hlk169015649" class="anchor"></span>Figure 172: Find VistA Users search fields

#### Finding VistA Users by Site

To find VistA users by Site

1.  *Click* the Site dropdown and select a site by *clicking* on it.
2.  *Click* the \<Find\> button.

#### Finding VistA Users by Status

To find VistA users by Status (Active / Inactive)

1.  *Click* the Status dropdown, and select an option.
2.  *Click* the \<Find\> button.

#### Assigning Privileges to a NUMI User

To add a NUMI user and assign privileges

1.  *Click* the \<Add New User\> button.
2.  When the *Add New User/Privileges* screen displays, enter the user's name into the VISTA User Name field.
1.  VISTA User Name is always in LASTNAME,FIRSTNAME format with no space after the comma. Use this format for exact VISTA username search.
2.  You can also enter partial names (e.g., instead of Smith,John you can search by Smith or Smi).
    1.  Select the VISTA User Login Site dropdown and choose a site by *clicking* on *it.*
    2.  Click the \<Find VISTA User\> button.

![](numi-user-guide-version-15-15/265.png)

<span id="_Hlk169015671" class="anchor"></span>Figure 173: Add NUMI User

3.  When the results display on the screen, click the <u>Select</u> Hyperlink in the Select One column for the user you wish to add.

![](numi-user-guide-version-15-15/266.png)

<span id="_Hlk169015674" class="anchor"></span>Figure 174: Find VistA User results

4.  When the screen with user privilege checkboxes displays, choose a site in the NUMI Access Site dropdown by *clicking* on it.

![](numi-user-guide-version-15-15/267.png)Multiple sites can be chosen from the Select Site for Granting Access dropdown on the *Add User* screen, if the user has permission to visit more than one site. However, only one site can be selected and viewed at a time.

![](numi-user-guide-version-15-15/268.png)

<span id="_Hlk169015683" class="anchor"></span>Figure 175: Add User Permissions

5.  Choose NUMI privileges by *clicking* on the User Privileges checkboxes.
6.  *Type* a reason into the Reason field.
7.  *Type* the users full VHA Username into the corresponding field.  The full VHA Username includes the user's Domain and the VHA Username, such as 'DOMAIN\vhaistmabyys'. If the user is unaware of their domain and VHA Username, they can click on the NUMI link and attempt a sign in, and the full Domain and VHA Username is displayed at the top of the NUMI login page under the Welcome banner. The user can optionally log in with their ACCESS/VERIFY code, as described in Appendix H, and the system will save their full VHA Username for the next login attempt.
8.  *Click* the \<Save\> button and the message: "Successfully updated user site. Site: \<location\> privileges" will display, as illustrated in the figure below.

#### Viewing NUMI User Information and Privileges

To view a NUMI user's information and privileges

1.  *Click* the <u>Select</u> hyperlink for the desired user on the *NUMI User List* screen.
2.  Each accessible site will display either a <u>View</u> or an <u>Edit hyperlink.</u>

![](numi-user-guide-version-15-15/269.png)

<span id="_Hlk169015697" class="anchor"></span>Figure 176: View User Privileges

3.  To view privileges for a particular site, *click* the <u>View</u> hyperlink for that site.
4.  The information will display and the <u>View</u> hyperlink will change to grayed out text displaying Selected Site.
5.  While on this screen, if the user has privileges at multiple sites, you can *click* on the NUMI Access Site dropdown and then *click* on the desired site in the dropdown to see them.
6.  Click the \<Cancel\> button to return to the *NUMI User List* screen.

![](numi-user-guide-version-15-15/270.png)

<span id="_Hlk169015706" class="anchor"></span>Figure 177: View NUMI User Information

#### Editing NUMI User Information

To edit NUMI user information

1.  Click the <u>Select</u> hyperlink for the desired user on the *NUMI User List Screen.*
2.  Each site that they have access to will display either a <u>View</u> or an <u>Edit hyperlink.</u>
3.  To edit privileges for a particular site, *click* the <u>Edit</u> hyperlink for that site.
4.  The information will display and the <u>Edit</u> hyperlink will change to grayed out text displaying Selected Site.
5.  *Type* a reason for the change(s) into the Reason field.
6.  *Type* the updated VHA Username into the Full VHA Username field.
7.  Add or change the user's privileges by selecting/deselecting the User Privileges checkboxes.
8.  Select and click on the site that the privileges will apply to from the NUMI Access Site dropdown.
9.  *Click* the \<Save\> button. The message "Successfully Updated User: \<user name\>" will display, as well as the reason you entered.

![](numi-user-guide-version-15-15/271.png) While multiple sites can be selected from the NUMI Access Site dropdown if the user has permission to visit more than one site, only one site's privileges can be viewed at a time.

![](numi-user-guide-version-15-15/272.png)

<span id="_Hlk169015724" class="anchor"></span>Figure 178: Edit NUMI User Screen

![](numi-user-guide-version-15-15/273.png) If someone tries to edit a NUMI user record and they do not have the proper administrator privileges, an error message will display: "You do not have admin access to modify user privileges for: \<user name\>."

![](numi-user-guide-version-15-15/274.png) If a user's privileges are changed, they will need to logout and log back in for the changes to take effect.

#### Deactivating a User's Site

A user's permission to visit and view site information for a particular facility can be deactivated using this feature (NUMI does not allow you to deactivate a <u>user</u>, but you can accomplish that general goal by deactivating all of their site permissions).

#### To deactivate a user site

1.  Click the <u>Select</u> hyperlink for the desired user on the *NUMI User List screen.*
2.  Click the <u>Edit</u> hyperlink to display the user's privileges
3.  Select the desired site from the NUMI Access Site dropdown by *clicking* on it.
4.  *Click* the <u>Deactivate</u> button.
5.  When the prompt "Are you sure you want to deactivate user site \<City, State\>" displays.
6.  Click the \<OK\> button to deactivate the site.

### Accessing the NUMI Site Admin Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators will use this feature to find VistA users, and add or remove users from the NUMI Physician Advisor, NUMI Primary Reviewer and NUMI Site Administrators lists. The examples below illustrate adding HARRIS to several Admin lists.

#### To access the NUMI 'Admin Site' feature

1.  *Select* the Admin dropdown and *click* on the Admin Sites option.
2.  The *Site Admin Panel* screen displays the names of existing users in the NUMI Physician Utilization Management Advisor List, NUMI Primary Reviewer List and NUMI Site Administrator List panels.

![](numi-user-guide-version-15-15/275.png)

<span id="_Hlk169015748" class="anchor"></span>Figure 179: Site Admin Screen (top section)

![](numi-user-guide-version-15-15/276.png)

<span id="_Hlk169015752" class="anchor"></span>Figure 180: Site Admin Screen (middle section)

![](numi-user-guide-version-15-15/277.png)

<span id="_Hlk169015757" class="anchor"></span>Figure 181: Site Admin screen (bottom section)

#### Finding a VistA User

To find a VistA User

1.  *Type* the user's name into the VISTA User Name field.
2.  Select a site from the VISTA User Login Site dropdown by *clicking* on it.
3.  Select a site from the NUMI Access Site dropdown by *clicking* on it.
4.  *Click* the \<Find VISTA User\> button. A list of names matching your search criteria will display in the Physician Advisor, Primary Reviewer and Site Administrators VistA User List panels

![](numi-user-guide-version-15-15/278.png) When searching for a VistA user, the user name is required. If you try to search for a user without providing this information, the message 'Please enter VISTA User ID' will display.

#### Adding a User to NUMI Physician Advisor Panel

To add a user to the list

1.  In the Physician Advisor Panel portion of the screen, *click* on a name in the VISTA User List.
2.  Click the "Add User" button, and the name will populate to the NUMI Physician Advisor List.
3.  When the message 'Are you sure you want to add \<name(s)\> to the Physician Advisor panel?' displays, *click* the \<OK\> button.

#### Adding a User to NUMI Primary Reviewer Panel

To add a user to the list

1.  In the Primary Reviewer Panel portion of the screen, *click* on a name in the VISTA User List.
2.  *Click* the "Add User" button, and the name will populate to the NUMI Primary Reviewer List portion of the panel.
3.  When the message 'Are you sure you want to add \<name(s)\> to the Primary Reviewer panel?' displays, *click* the \<OK\> button

#### Adding a User to NUMI Site Administrators Panel

To add a user to the list

1.  In the Site Administrators Panel portion of the screen, *click* on a name in the VISTA User List.
2.  *Click* the "Add User" button, and the name will populate to the NUMI Site Administrators List portion of the panel.
3.  When the message 'Are you sure you want to add \<name(s)\> to the Site Administrators panel?' displays, *click* the \<OK\> button

#### Adding a User to NUMI Report Access Panel

You can assign the "Report Access" role for a user when editing an individual user under Admin/ Users, and when viewing roles and their members under Admin/Admin Sites. Only users that have this role will be able to run and view reports.

#### To add a user to the list

1.  In the Report Access portion of the screen, *click* on a name in the VISTA User List.
2.  *Click* the "Add User" button, and the name will populate to the NUMI Report Access portion of the panel.
3.  When the message 'Are you sure you want to add \<name(s)\> to the Report Access panel?' displays, *click* the \<OK\> button.

#### Removing a User from the NUMI Physician Advisor Panel

![](numi-user-guide-version-15-15/279.png) Note: A non-super user will not be able to remove a super user. If this is attempted you will receive a message saying "User does not have permissions to remove a NUMI Superuser".

#### To remove a user from the list

1.  *Click* on a name in the NUMI Physician Advisor List.
2.  *Click* the "Remove User" button, and the name will be moved from the list to the VISTA User List of the panel.
3.  When the message 'Are you sure you want to remove \<name(s)\> from the Physician Advisor panel?' displays, *click* the \<OK\> button.

#### Removing a User from the NUMI Primary Reviewer Panel

To remove a user from the list

1.  *Click* on a name in the NUMI Primary Reviewer List.
2.  *Click* the "Remove User" button, and the name will be moved from the list to the VISTA User List portion of the panel.
3.  When the message 'Are you sure you want to remove \<name(s)\> from the Primary Reviewer panel?' displays, *click* the \<OK\> button.

#### Removing a User from the NUMI Site Administrators Panel

To remove a user from the list

1.  *Click* on a name in the NUMI Site Administrators List.
2.  *Click* the "Remove User" button, and the name will be moved from the list to the VISTA User List of the panel.
3.  When the message 'Are you sure you want to remove \<name(s)\> from the Site Administrators panel?' displays, *click* the \<OK\> button.

#### Removing a User from the NUMI Report Access Panel

To remove a user from the list

1.  *Click* on a name in the NUMI Report Access List.
2.  *Click* the "Remove User" button, and the name will be moved from the list to the VISTA User List of the panel.
3.  When the message 'Are you sure you want to remove \<name(s)\> from the Report Access panel?' displays, *click* the \<OK\> button.

### Accessing the NUMI Treating Specialty Configuration Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](numi-user-guide-version-15-15/280.png)

<span id="_Hlk169015820" class="anchor"></span>Figure 182: NUMI Treating Specialty Configuration Feature

Under the Admin menu, the "Treating Specialty Configuration" option is available. You must have Site Administrator rights to view this screen. Information viewable on the screen will apply facility-wide.

The Treating Specialty Configuration screen explains, "You may use this utility to let NUMI know which treating specialties from your facility are reviewable and whether or not they will be reviewed. NUMI will use this information to determine which patient stays should be included in your work list. NUMI will also use this information to determine which patient stays should be included in performance score calculations. If your facility is part of an integrated site or integrated health system, you only need to configure treating specialties that are (or have been) used by your specific facility." and offers a list of Treating Specialties with accompanying Dismissal Behavior list boxes.

The list boxes are pre-populated with the following choices for Dismissal Behaviors: Not Configurable, Acute Reviewable, Obs Reviewable, Acute Non Reviewable, Obs Not Reviewable, Non-Acute Not Reviewable, and Opting Not to Review. More than one Treatment Specialty can be updated with a new Dismissal Behavior. You may scroll through the current Treatment Specialties/Dismissal Behaviors by clicking the <u>Next</u>, <u>Previous</u>, <u>Last Page</u> or <u>First</u> <u>Page</u> hyperlinks.

#### To update a Treatment Specialty with a new Dismissal Behavior

1.  Select new behavior(s) from the Treatment Dismissal Behavior dropdown for the corresponding Treatment Specialty.

![](numi-user-guide-version-15-15/281.png)

<span id="_Hlk169015830" class="anchor"></span>Figure 183: Select Treatment Dismissal Behavior list box

2.  *Press* \<Save\>.
3.  The choice(s) selected in the dropdowns are accepted.

## Logging Out of the NUMI Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "Logout option" is located on the *Tools* menu.

### To logout of the NUMI application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  *Click* on the Tools dropdown.
2.  *Click* on \<Logout from NUMI\> option.
3.  User will be logged out of the NUMI application and the *NUMI Screen* will display.
4.  If user wants to log out of the VA IAM SSO as well, which will log the user out of all other VA applications (e.g. Training Management System, etc.) that use VA IAM SSO login, *Click* the \<Logout of IAM SSO\> button. Otherwise close the browser or click on the '<u>here</u>' link to go to NUMI login page
5.  The IAM SSO logout page will be displayed with the message "You have been logged out of VA Single Sign-On"
6.  Close the browser.

## Online Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All NUMI users can access the most current version of this User Guide and other NUMI system documentation on the National VistA Software Documentation Library at: http://www.va.gov/vdl/application.asp?appid=184

or through links on the OQSV website.

The Office of Quality Safety and Value (OQSV) website can be accessed from the online NUMI Help menu. If the online help information does not answer your question, first contact your NUMI site POC/Administrator for assistance. If the question is still unresolved, you may log a Service Now ticket.

You may also go to the OQSV web page directly by typing this URL in your browser's address line: <http://vaww.oqsv.med.va.gov/functions/integrity/um/numi/numi.aspx>  
<span id="_Toc479676269" class="anchor"></span>To access the online Help feature

1.  *Click* on the Help menu dropdown

> ![](numi-user-guide-version-15-15/282.png)

<span id="_Hlk169015857" class="anchor"></span>Figure 184: Help Menu dropdown

2.  Select the On-Line Help option by *clicking* on it and you will be redirected to the OQSV web page.
3.  Click on the NUMI User Guide option in the web page (Here you will be able to click on a link that will open an electronic copy of this User Guide in its entirety. Or, if you prefer, you can click on individual links to each chapter in the document.)
4.  Select the Copyright option by *clicking* on it and you will be redirected to the Change Healthcare CERMe Proprietary Notice page.

![](numi-user-guide-version-15-15/283.png)

<span id="_Hlk169015865" class="anchor"></span>Figure 185: OQSV Web Page

![](numi-user-guide-version-15-15/284.png)

<span id="_Hlk169015868" class="anchor"></span>Figure 186: Change Healthcare CERMe Proprietary Notice

## Primary Reviewer and Primary Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Primary Reviewers may also be known as Nurse Reviewers or UM Reviewers. Whichever descriptor is utilized, this refers to the individual looking at the patient stay and performing the review that determines whether or not the stay meets InterQual® Criteria. In general, NUMI attempts to use the terms Primary Reviewer and Primary Review.

## Physician Advisors and Medical Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In cases where the Primary Review does not meet InterQual® Criteria as determined by the CERMe component of NUMI, the Primary Reviewer will be asked to assign a Physician Advisor to perform a medical review of the primary review.

InterQual® and some UM programs make use of a Secondary Reviewer who lies between the Primary Reviewer and the Physician Advisor. In NUMI there is no discreet Secondary Reviewer step -- this is best done by saving a review, and then having the Secondary Reviewer look at it.

## CERMe vs. CERME vs. CERM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CERMe stands for Care Enhanced Review Manager, Change Healthcare's automation of their InterQual® Criteria -- an industry standard. Per Change Healthcare, it is pronounced "Kermie." The 'E' or 'e' on the end technically refers to the standalone version of CERM, which has its own administrative and reporting tools.

Regardless of how you see it in the application, this refers to the Change Healthcare software embedded within NUMI. References to a "standalone CERMe" refer to the correct usage of the CERMe (or CERME) name. There are sites in the VA that have been using their own standalone instances of CERMe without the VistA integration.

<span id="_Toc465421563" class="anchor"></span>Glossary of Terms

> A glossary of UM terms that are relevant to the NUMI application are defined in Table 12.

<table>
<caption><p><span id="_Hlk169016080" class="anchor"></span>Table 13: UM Admission Reason Codes</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Acute</td>
<td colspan="2">A level of health care in which the patient's severity of illness and intensity of service can only be performed in an in-patient setting.</td>
</tr>
<tr class="even">
<td>Admission Review</td>
<td colspan="2"><p>An assessment of medical necessity and appropriateness of a hospital admission after the hospitalization has occurred and the patient has been moved to a higher level of care (e.g., from a Ward to MICU). This review is typically performed on admission, within 24 hours following admission or no later than the first business day following the admission.</p>
<p>Standardized review criteria must be used to determine the appropriateness of care.</p></td>
</tr>
<tr class="odd">
<td>ALOC</td>
<td colspan="2">Acronym for Alternate Level of Care</td>
</tr>
<tr class="even">
<td>Behavioral Health</td>
<td colspan="2">Assists in determining initial and successive level of care decisions for psychiatric conditions, chemical dependency and dual diagnosis for individuals at each stage of life, e.g., InterQual® Behavioral Health Criteria.</td>
</tr>
<tr class="odd">
<td>BH</td>
<td colspan="2">Acronym for Behavioral Health</td>
</tr>
<tr class="even">
<td>CERMe</td>
<td colspan="2">Acronym for Care Enhance Review Manager enterprise. A web-based application, made available by Change Healthcare that provides computerized InterQual® templates to field Utilization Management staff.</td>
</tr>
<tr class="odd">
<td>Concurrent Review</td>
<td colspan="2">A Behavioral Health review for a patient who has already received an initial review.</td>
</tr>
<tr class="even">
<td>Concurrent Review Process</td>
<td colspan="2">An assessment of medical necessity or appropriateness of services that covers the time period throughout the time of review and the previous 24 hours.</td>
</tr>
<tr class="odd">
<td>COTS</td>
<td colspan="2">Acronym for Commercial Off-the-Shelf</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td colspan="2">Acronym for Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>CS</td>
<td>Acronym for Continued Stay</td>
<td></td>
</tr>
<tr class="even">
<td>DoD</td>
<td>Acronym for Department of Defense</td>
<td></td>
</tr>
<tr class="odd">
<td>ECT</td>
<td>Acronym for Electroconvulsive Therapy</td>
<td></td>
</tr>
<tr class="even">
<td>Episode Day of Care</td>
<td>A term commonly used to measure the duration of a single episode of hospitalization. Inpatient days are calculated by subtracting day of admission from day of discharge. However, persons entering and leaving a hospital on the same day have a length of stay of one.</td>
<td></td>
</tr>
<tr class="odd">
<td>ET</td>
<td>Acronym for Eastern Time</td>
<td></td>
</tr>
<tr class="even">
<td>FAQ</td>
<td>Acronym for Frequently Asked Questions</td>
<td></td>
</tr>
<tr class="odd">
<td>G&amp;L</td>
<td>Acronym for Gains and Losses</td>
<td></td>
</tr>
<tr class="even">
<td>HIPPA</td>
<td>Acronym for Health Insurance Portability and Accountability Act of 1996</td>
<td></td>
</tr>
<tr class="odd">
<td>Hospital Admission Review</td>
<td>A review that is performed when a patient first comes into the hospital. All admission reviews should be dated with the actual admission date, regardless of when the review is performed.</td>
<td></td>
</tr>
<tr class="even">
<td>HTTP</td>
<td>Acronym for Hypertext Transfer Protocol</td>
<td></td>
</tr>
<tr class="odd">
<td>IAM</td>
<td>Identity and Access Management</td>
<td></td>
</tr>
<tr class="even">
<td>IE</td>
<td>Acronym for Internet Explorer</td>
<td></td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Acronym for Internal Entry Number</td>
<td></td>
</tr>
<tr class="even">
<td>InterQual® Clinical Evidence Summaries</td>
<td>Collection of current white papers that synthesize medical research to support controversial diagnoses, which support second- level medical review recommendations and promote evidence-based standards of care.</td>
<td></td>
</tr>
<tr class="odd">
<td>InterQual® Criteria</td>
<td>InterQual® is a product of the InterQual® division of Change Healthcare Corporation. InterQual® criteria are used to determine if a patient's hospital length of stay is appropriate. The criteria are based on the diagnoses and any treatments involved in the patient's care.</td>
<td></td>
</tr>
<tr class="even">
<td>InterQual® Level of Care Criteria</td>
<td>InterQual Level of Care Criteria addresses admissions and continued stays across the continuum of care, from acute settings through homecare and outpatient treatment.</td>
<td></td>
</tr>
<tr class="odd">
<td>IT</td>
<td>Acronym for Information Resource Management</td>
<td></td>
</tr>
<tr class="even">
<td>Level of Care</td>
<td>Refers to the continuum of care, which includes various intensities of service levels such as acute, rehabilitation, sub-acute, home care and outpatient rehabilitation. See also InterQual® Level of Care Criteria.</td>
<td></td>
</tr>
<tr class="odd">
<td>LOC</td>
<td>Acronym for Level Of Care</td>
<td></td>
</tr>
<tr class="even">
<td>MDWS</td>
<td>Acronym for Medical Domain Web Services</td>
<td></td>
</tr>
<tr class="odd">
<td>Movement Types</td>
<td>A movement refers to the act or process of moving a sick, injured, wounded, or other person to obtain medical care or treatment. Movement types in NUMI include Admission, Continued Stay, Discharge and Transfer.</td>
<td></td>
</tr>
<tr class="even">
<td>National Utilization Management Integration</td>
<td>A Web-based application that automates documentation of clinical features relevant to each patient's condition and the associated clinical services provided as part of VHA's medical benefits package.</td>
<td></td>
</tr>
<tr class="odd">
<td>NQF</td>
<td>Acronym for National Quality Forum</td>
<td></td>
</tr>
<tr class="even">
<td>NUMI</td>
<td>Acronym for National Utilization Management Integration</td>
<td></td>
</tr>
<tr class="odd">
<td>Observation(s)</td>
<td>An alternative level of health care comprising short-stay encounters for patients who require close nursing observation or medical management.</td>
<td></td>
</tr>
<tr class="even">
<td>OEF</td>
<td>Acronym for Operation Enduring Freedom</td>
<td></td>
</tr>
<tr class="odd">
<td>OIF</td>
<td>Acronym for Operation Iraqi Freedom</td>
<td></td>
</tr>
<tr class="even">
<td>OIG</td>
<td>Acronym for Office of Inspector General</td>
<td></td>
</tr>
<tr class="odd">
<td>OQSV</td>
<td>Acronym for Office of Quality Safety and Value</td>
<td></td>
</tr>
<tr class="even">
<td>PC</td>
<td>Acronym for Personal Computer</td>
<td></td>
</tr>
<tr class="odd">
<td>POC</td>
<td>Acronym for Point of Contact</td>
<td></td>
</tr>
<tr class="even">
<td>RLOC</td>
<td>Acronym for Recommended Level Of Care</td>
<td></td>
</tr>
<tr class="odd">
<td>Term</td>
<td>Description</td>
<td></td>
</tr>
<tr class="even">
<td>Severity of Illness</td>
<td>The extent of organ system derangement or physiologic de-compensation for a patient. Classified into minor, moderate, major, and extreme. Meant to provide a basis for evaluating hospital resource use or to establish patient care guidelines.</td>
<td></td>
</tr>
<tr class="odd">
<td>SQL</td>
<td>Acronym for Structured Query Language</td>
<td></td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Acronym for Social Security Number</td>
<td></td>
</tr>
<tr class="odd">
<td>SSO</td>
<td>Single Sign-On</td>
<td></td>
</tr>
<tr class="even">
<td>UM</td>
<td>Acronym for Utilization Management</td>
<td></td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Acronym for uniform Resource Locator</td>
<td></td>
</tr>
<tr class="even">
<td>Utilization Management</td>
<td>The process of evaluating and determining the coverage and the appropriateness of medical care services across the patient health care continuum to ensure the proper use of resources.</td>
<td></td>
</tr>
<tr class="odd">
<td>Utilization Review</td>
<td>A formal evaluation or the coverage, medical necessity, efficiency or appropriateness of health care services and treatment plans for an individual patient</td>
<td></td>
</tr>
<tr class="even">
<td>VA</td>
<td>Acronym for Department of Veterans Affairs</td>
<td></td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Acronym for Veterans Health Administration</td>
<td></td>
</tr>
<tr class="even">
<td>VIA</td>
<td>VistA Integration Adapter</td>
<td></td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Acronym for Veterans Integrated Service Network.</td>
<td></td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Acronym for Veterans Health Information Systems and Technology Architecture</td>
<td></td>
</tr>
<tr class="odd">
<td>VSSC</td>
<td>Acronym for VISN Support Services Center</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Hlk169016080" class="anchor"></span>Table 13: UM Admission Reason Codes

<span id="_Toc479676271" class="anchor"></span>Appendix A – NUMI Screen Flow

The figure below illustrates the *basic flow* of the major NUMI screens

![](numi-user-guide-version-15-15/285.png)

<span id="_Hlk169016037" class="anchor"></span>Figure 187: Basic Flow of NUMI Screens

NOTES:

On the *Primary Review* Screen, only reviews with Do not Meet Criteria status will go to the Physician Advisor Worklist.

<span id="_Toc479676272" class="anchor"></span>Appendix B – NUMI TIPS for Success

This Appendix contains tips that will help you make the most of working with NUMI.

Remember that each row on the Patient Selection/Worklist is a patient stay. Use the Patient Selection/Worklist to identify your patient stays and the reviews needed. This screen will tell you:

- Time and date of admission
- If the patient is discharged
- When the last review was done
- Whether criteria were met on the last review

Use the Assign Reviewer function. This will make it easier for you to locate your patients on the Patient Selection/Worklist.

When you do a review, NUMI automatically assigns you as the reviewer. If you assign yourself to new admissions in your area of responsibility every day, then you can filter your facility Patient Selection/Worklist by your name, and you will have a complete listing of your active patient stays.

Use your Gains and Losses (G&L) or Ward Roster reports to confirm that all admissions are appearing in NUMI.

Occasionally patient admissions are not picked up by the NUMI synchronizer. When this happens, you can add that patient through the Manual VistA Synchronization feature. If you make certain that all admissions are captured every day, your patient stay list will be complete.

Use short cuts and best practices whenever possible.

As you work with NUMI, you will find the workflow that is best for you. Here are some things that are time-savers:

Navigate around the system using the 4 tabs

Filter your Patient Selection/Worklist– make sure everyone gets an admission review. They will then be in your list daily until you dismiss them.

Use the Copy Review function as much as possible…especially after weekends.

Some people make brief written notes while in CPRS or on the units and enter reviews all at once. Others prefer to toggle back and forth between NUMI and CPRS while doing reviews.

Use Clinical Comments fields strategically.

Enter information in the Clinical Comments boxes that will assist you in identifying critical issues with this stay and jog your memory for future reviews. This is an optional field, if there is nothing notable, leave it blank. For reviews not meeting criteria that will be sent to the Physician Advisor, enter Criteria Not Met Elaboration and Clinical comments that can provide information to help the Physician Advisor understand the Not Met status.

Meet with your Physician Advisor to develop policy and guidelines for reviews. Discuss which types of Not Met reviews should go to the Physician Advisor for review.

If there are categories of Not Meeting reviews that the Physician Advisor would consider "Automatic Agree," consider establishing a formal local policy to not send those to the Physician Advisor. Find out what types of clinical comments are helpful to the Physician Advisor.

Use reporting

The reports are available through the link on the NUMI Report menu, which takes you to reports provided by OQSV. Some are facility aggregates, and some are patient level detail. At day's end, use the patient detail report to print out a summary of your reviews. This is a helpful tool for the following day.

Use the training and help resources available. Ask for help when needed.

The OQSV website will have a NUMI section with helpful tools and resources listed under Quick Links. Call on the NUMI Trainers for assistance as needed.

Be patient with yourself and the NUMI system

It takes time to learn how to apply a new tool like NUMI. NUMI upgrades roll out regularly with new capabilities and changes.

<span id="_Toc146202592" class="anchor"></span>Appendix C – UM Admission Reason Codes

Table 13 provides a list of UM Admission Reason Codes and their definitions.

| UM Code | Code Description for Admission Reviews  | Definition for Reason                                                                                              |
|---------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 8.1     | Outpatient Care                         | Admitted to the inpatient setting for care or services that could be safely provided in the outpatient setting.    |
| 8.11    | Work-up                                 | Admitted with unclear diagnosis, vague symptoms, or to confirm a suspected diagnosis.                              |
| 8.12    | Pre-op                                  | Admitted prior to an elective surgical procedure appropriate for the inpatient setting, excluding transplantation. |
| 8.13    | Ambulatory surgery                      | Admitted for a procedure that is not included on the Inpatient List.                                               |
| 8.14    | Diagnostic study                        | Admission for a diagnostic study to determine the cause of symptoms.                                               |
| 8.1401  | Ablation/EPS                            | Diagnostic study                                                                                                   |
| 8.1402  | Bronchoscopy                            | Diagnostic study                                                                                                   |
| 8.1403  | Cardiac Cath Diagnostic                 | Diagnostic study                                                                                                   |
| 8.1404  | Colonoscopy/EGD                         | Diagnostic study                                                                                                   |
| 8.1405  | CT Scan                                 | Diagnostic study                                                                                                   |
| 8.1406  | Echo-cardiac                            | Diagnostic study                                                                                                   |
| 8.1407  | EEG                                     | Diagnostic study                                                                                                   |
| 8.1408  | ERCP                                    | Diagnostic study                                                                                                   |
| 8.1409  | Interventional Radiology                | Diagnostic study                                                                                                   |
| 8.141   | MPI                                     | Diagnostic study                                                                                                   |
| 8.1411  | MRA/MRV                                 | Diagnostic study                                                                                                   |
| 8.1412  | MRI                                     | Diagnostic study                                                                                                   |
| 8.1413  | Nuclear Med Cardiac                     | Diagnostic study                                                                                                   |
| 8.1414  | Nuclear Med Non-cardiac                 | Diagnostic study                                                                                                   |
| 8.1415  | PET Scan                                | Diagnostic study                                                                                                   |
| 8.1416  | Sleep Study                             | Diagnostic study                                                                                                   |
| 8.1417  | Stress Test                             | Diagnostic study                                                                                                   |
| 8.1419  | Trans-esophageal Echo                   | Diagnostic study                                                                                                   |
| 8.142   | Transthoracic Echo                      | Diagnostic study                                                                                                   |
| 8.1421  | Ultrasound (non-cardiac)                | Diagnostic study                                                                                                   |
| 8.1422  | US/CT Guided Procedure                  | Diagnostic study                                                                                                   |
| 8.1423  | Vascular Studies                        | Diagnostic study                                                                                                   |
| 8.15    | Therapeutic procedure                   | Admitted for a therapeutic procedure indicated as treatment                                                        |
| 8.1501  | Infusions                               | Therapeutic procedure                                                                                              |
| 8.1502  | Transfusions                            | Therapeutic procedure                                                                                              |
| 8.1503  | Chemotherapy                            | Therapeutic procedure                                                                                              |
| 8.1504  | Radiation Therapy                       | Therapeutic procedure                                                                                              |
| 8.1505  | Cardioversion                           | Therapeutic procedure                                                                                              |
| 8.1506  | Cardiac Cath w/Intervention             | Therapeutic procedure                                                                                              |
| 8.1507  | Pacemaker/ICD Implantation              | Therapeutic procedure                                                                                              |
| 8.1508  | Enteral Feeding Tube                    | Therapeutic procedure                                                                                              |
| 8.1509  | ECT                                     | Therapeutic procedure                                                                                              |
| 8.151   | PICC Line Insertion                     | Therapeutic procedure                                                                                              |
| 8.1511  | Paracentesis                            | Therapeutic procedure                                                                                              |
| 8.1512  | Thoracentesis                           | Therapeutic procedure                                                                                              |
| 8.2     | Clinical                                | Clinical factors and/or physician judgment are the basis for admission.                                            |
| 8.21    | Inappropriate LOC                       | Meets criteria for a higher or lower level of care delivered in a hospital; includes observation.                  |
| 8.22    | Lack of Medical Necessity               | Care in a hospital bed not required.                                                                               |
| 8.23    | Comorbid conditions                     | Secondary condition affecting the clinical decision to admit.                                                      |
| 8.24    | BH patient with medical care needs      | Acute BH patient requiring medical/surgical intervention not available on BH unit.                                 |
| 8.25    | Premature Obs. Order                    | Observation ordered prior to the recovery period being completed.                                                  |
| 8.26    | Clinical Variance                       | Requires inpatient hospitalization but does not meet all specific criteria points.                                 |
| 8.3     | Regulatory                              | Admitted for legal not medical reasons.                                                                            |
| 8.31    | Court ordered                           | Court ordered inpatient care.                                                                                      |
| 8.32    | CMS 3 day rule                          | CMS qualifying hospital stay requirement.                                                                          |
| 8.33    | Adult Protective Services               | APS directed admission.                                                                                            |
| 8.4     | Social                                  | Social issues are the primary reason for admission.                                                                |
| 8.41    | Self-Care Deficit                       | Unable to care for basic or medical needs and no family/caregiver                                                  |
| 8.42    | Transportation                          | No timely transport plan in place                                                                                  |
| 8.43    | Planned respite                         | Scheduled respite care requiring hospital setting                                                                  |
| 8.44    | Homeless                                | Requires intervention by Homeless Program.                                                                         |
| 8.5     | Inpatient LOC Availability              | Not in the correct setting due to inpatient bed capacity or lack of an inpatient level of care                     |
| 8.51    | Inpatient RLOC not provided at facility | Facility lacks inpatient level of care.                                                                            |
| 8.6     | Environmental                           | Environmental conditions create public safety risks and limit access to medical care.                              |
| 8.61    | Adverse Conditions                      | Inclement weather, natural disasters, and/or power outage                                                          |

<span id="_Hlk169016300" class="anchor"></span>Table 14: UM Continued Stay Reason Codes

<span id="_Toc479676285" class="anchor"></span>Appendix D – UM Continued Stay Reason Codes

Table 14 provides a list of UM Continued Stay Reason Codes and their definitions.

| UM Code | Code Description for Cont'd Stay Reviews | Definition for Reason                                                                                                                                                                                                                                                                                                                      |
|---------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 18.1    | Outpatient Care                          | Awaiting care appropriate for the outpatient setting.                                                                                                                                                                                                                                                                                      |
| 18.11   | Diagnostic                               | Awaiting testing that does not require hospitalization.                                                                                                                                                                                                                                                                                    |
| 18.1101 | Ablation/EPS                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1102 | Bronchoscopy                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1103 | Cardiac Cath Diagnostic                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1104 | Colonoscopy/EGD                          | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1105 | CT Scan                                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1106 | Echo-cardiac                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1107 | EEG                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1108 | ERCP                                     | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1109 | Interventional Radiology                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.111  | MPI                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1111 | MRA/MRV                                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1112 | MRI                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1113 | Nuclear Med Cardiac                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1114 | Nuclear Med Non-cardiac                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1115 | PET Scan                                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1116 | Sleep Study                              | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1117 | Stress Test                              | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1119 | TEE                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.112  | TTE                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1121 | Ultrasound (non-cardiac)                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1122 | US/CT Guided Procedure                   | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1123 | Vascular Studies                         | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.12   | Procedures                               | Awaiting procedure appropriate for the ambulatory setting.                                                                                                                                                                                                                                                                                 |
| 18.1201 | Infusions                                | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1202 | Transfusions                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1203 | Chemotherapy                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1204 | Radiation Therapy                        | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1205 | Cardioversion                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1206 | Cardiac Cath w/Intervention              | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1207 | Pacemaker/ICD                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1208 | Enteral Feeding Tube                     | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1209 | ECT                                      | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.121  | PICC Line Insertion                      | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1211 | Paracentesis                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1212 | Thoracentesis                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1213 | Surgical Procedure                       | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.13   | Consults                                 | Awaiting consult appropriate for the ambulatory setting and not necessary for transition to the next level of care.                                                                                                                                                                                                                        |
| 18.131  | Medicine subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.132  | Surgical subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.133  | Psychiatry/Psychology                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.134  | Rehabilitation Medicine                  |                                                                                                                                                                                                                                                                                                                                            |
| 18.135  | Extended Care                            |                                                                                                                                                                                                                                                                                                                                            |
| 18.136  | Neurology                                |                                                                                                                                                                                                                                                                                                                                            |
| 18.137  | Speech & Audiology                       |                                                                                                                                                                                                                                                                                                                                            |
| 18.2    | Clinical                                 | Clinical presentation and/or physician judgment.                                                                                                                                                                                                                                                                                           |
| 18.21   | Lack of medical necessity                | Care could be safely rendered in the home or outpatient setting.                                                                                                                                                                                                                                                                           |
| 18.22   | Clinical instability                     | Patient falls outside of the criteria but does not meet discharge screens.                                                                                                                                                                                                                                                                 |
| 18.23   | Comorbid conditions                      | Documentation of secondary or tertiary conditions that are currently delaying patient response to treatment, or creating a deviation in standard evidence-based treatment.                                                                                                                                                                 |
| 18.24   | BH Patient with medical care needs       | BH patient requiring medical/surgical intervention not available on BH unit.                                                                                                                                                                                                                                                               |
| 18.25   | Inappropriate LOC                        | Patient remains in current level of care when care and services could be provided safely in a lower level or more appropriately in a higher level of care. This includes inpatient and post-acute settings available at the facility, CLC, or in the community. Not to be used for patients appropriate for discharge home see code 18.21. |
| 18.26   | No documented plan or evaluation         | Documentation absent or lacking specificity.                                                                                                                                                                                                                                                                                               |
| 18.3    | Regulatory                               | Legal not medical needs.                                                                                                                                                                                                                                                                                                                   |
| 18.31   | Court ordered stay                       | Court order for specified duration of time.                                                                                                                                                                                                                                                                                                |
| 18.32   | CMS 3 day rule                           | Post-acute placement required by CMS.                                                                                                                                                                                                                                                                                                      |
| 18.33   | APS                                      | Adult Protective Services investigation and recommendations pending.                                                                                                                                                                                                                                                                       |
| 18.34   | Guardianship                             | Awaiting guardianship procedures.                                                                                                                                                                                                                                                                                                          |
| 18.4    | Social                                   | Unresolved social issues.                                                                                                                                                                                                                                                                                                                  |
| 18.41   | Lack of caregiver                        | Self-care deficit and no support for home management.                                                                                                                                                                                                                                                                                      |
| 18.42   | Transportation                           | Lack of transportation to home or next level of care.                                                                                                                                                                                                                                                                                      |
| 18.43   | Planned respite                          | Scheduled respite requiring hospital setting                                                                                                                                                                                                                                                                                               |
| 18.44   | Homeless                                 | Requires arrangements for temporary housing and/or intervention by Homeless Program                                                                                                                                                                                                                                                        |
| 18.45   | Resistance to discharge plan             | Patient or the family resists plan for next level of care.                                                                                                                                                                                                                                                                                 |
| 18.5    | Inpatient LOC Availability               | Not in the correct inpatient setting due to capacity or lack of the appropriate inpatient level of care.                                                                                                                                                                                                                                   |
| 18.51   | Inpatient RLOC not provided at facility  | The needed level of Inpatient care is not available at the facility. Does not include post-acute levels of care.                                                                                                                                                                                                                           |
| 18.52   | Inpatient Transfer Delay                 | Patients requiring transfer for continued inpatient care needs at another facility. Not to be used for patients awaiting NG, CLC, or other post-acute settings.                                                                                                                                                                            |
| 18.521  | VA Facility                              | Transfer Delay                                                                                                                                                                                                                                                                                                                             |
| 18.522  | Non-VA Facility                          | Transfer Delay                                                                                                                                                                                                                                                                                                                             |
| 18.6    | Environmental                            | Environmental conditions create public safety risks and limit access to medical care                                                                                                                                                                                                                                                       |
| 18.61   | Adverse Conditions                       | Inclement weather, natural disasters, and/or power outage                                                                                                                                                                                                                                                                                  |
| 18.7    | Post-Acute Transition                    | Awaiting transition to post-acute setting                                                                                                                                                                                                                                                                                                  |
| 18.71   | Placement Issues                         | Post-acute placement delays                                                                                                                                                                                                                                                                                                                |
| 18.711  | Financial                                | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.712  | Administrative                           | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.713  | Clinical                                 | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.714  | Behavioral                               | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.72   | Awaiting CLC acceptance                  | Pending CLC Consult, screening or acceptance                                                                                                                                                                                                                                                                                               |
| 18.73   | Awaiting CLC bed                         | CLC without bed or ability to receive patients                                                                                                                                                                                                                                                                                             |
| 18.74   | Awaiting community placement             | Delay in transitioning patient to community nursing home                                                                                                                                                                                                                                                                                   |
| 18.741  | VA paid                                  | Awaiting community placement                                                                                                                                                                                                                                                                                                               |
| 18.742  | Non-VA paid                              | Awaiting community placement                                                                                                                                                                                                                                                                                                               |
| 18.75   | Ineffective discharge planning/process   | DC planning/interventions delay                                                                                                                                                                                                                                                                                                            |
| 18.76   | Awaiting VA Post-Acute Bed               | Patient requires post-acute care following hospital stay other than CLC/Nursing home care but no beds in appropriate LOC due to capacity issues.                                                                                                                                                                                           |
| 18.8    | Scheduling delays/cancellations          | Test, procedure, or surgery is cancelled or delayed                                                                                                                                                                                                                                                                                        |
| 18.81   | Delayed diagnostic test                  | Diagnostic test cancelled or delayed                                                                                                                                                                                                                                                                                                       |
| 18.8101 | Ablation/EPS                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8102 | Bronchoscopy                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8103 | Cardiac Cath Diagnostic                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8104 | Colonoscopy/EGD                          | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8105 | CT Scan                                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8106 | Echo-cardiac                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8107 | EEG                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8108 | ERCP                                     | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8109 | Interventional Radiology                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.811  | MPI                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8111 | MRA/MRV                                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8112 | MRI                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8113 | Nuclear Med Cardiac                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8114 | Nuclear Med Non-cardiac                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8115 | PET Scan                                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8116 | Sleep Study                              | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8117 | Stress Test                              | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8118 | Swallow Study                            | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8119 | TEE                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.812  | TTE                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8121 | Ultrasound (non-cardiac)                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8122 | US/CT Guided Procedure                   | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8123 | Vascular Studies                         | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.82   | Delayed Surgery/procedure                | Surgery or procedure cancelled or delayed                                                                                                                                                                                                                                                                                                  |
| 18.8201 | Infusions                                | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8202 | Transfusions                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8203 | Chemotherapy                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8204 | Radiation Therapy                        | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8205 | Cardioversion                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8206 | Cardiac Cath w/Intervention              | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8207 | Pacemaker/ICD                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8208 | Enteral Feeding Tube                     | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8209 | ECT                                      | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.821  | PICC Line Insertion                      | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8211 | Paracentesis                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8212 | Thoracentesis                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8213 | Surgical Procedure                       | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.83   | Consults                                 | Awaiting completion of consultation appropriate and necessary for transition to the next level of care. Consults are needed prior to discharge or transfer to a lower level of care.                                                                                                                                                       |
| 18.8301 | Medicine subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8302 | Surgical subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8303 | Psychiatry/Psychology                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8304 | Rehabilitation Medicine                  |                                                                                                                                                                                                                                                                                                                                            |
| 18.8305 | Extended Care                            |                                                                                                                                                                                                                                                                                                                                            |
| 18.8306 | Neurology                                |                                                                                                                                                                                                                                                                                                                                            |
| 18.8307 | Speech & Audiology                       |                                                                                                                                                                                                                                                                                                                                            |
| 18.8308 | Interventional Radiology                 |                                                                                                                                                                                                                                                                                                                                            |

UM Continued Stay Reason Codes TableTable listing the UM Continued Stay Reason Codes.

<span id="_Toc465421571" class="anchor"></span>Appendix E – Frequently Asked Questions (FAQ)

This Appendix contains a list of Frequently Asked Questions about NUMI:

*Getting Started:*

Q: What do I need before I start using NUMI?

> A: This is what you will need:

- a Windows PC on the VA intranet, running the version of Microsoft Edge currently approved and in use in the VA
  - While it is expected that NUMI will run on your PC without any difficulty, should you experience problems please contact your local IT for assistance. Many issues can be resolved by changing some settings on the PC (*See <u>Section 2</u> in the User Guide for more information*). If you are not permitted to change settings yourself due to restrictions at your particular VA site, your local IT can help you.
- a Personal Identity Verification (PIV) card
  - A PIV card is needed for Single Sign-on access.
- a production VistA account at one site that has CPRS access to that site
  - You only need one "home" login site. Please note that NUMI access is completely separate from access for CPRS and VistAWeb - you will need to arrange for those rights separately. Performing reviews in NUMI without proper additional clinical informatics tools such as CPRS and VistAWeb is strongly discouraged.
- to have your account set up by a NUMI Administrator
  - The rights you will need will depend on whether you are a Primary Reviewer, a Physician Advisor or an Administrator.
- the URL for the NUMI application
  - This will be provided to you after you have attended NUMI training.

Login Error Messages:

Q: I'm unable to login to VistA. I'm getting this message: "Unable to login to VistA. The error was: Device IP address is locked due to too many invalid sign on attempts." What should I do?

> A: This error means you have exceeded the maximum number of login attempts permitted by your local VistA. When this happens, VistA will lock you out of the NUMI application for 20 minutes. After 20 minutes, VistA will clear your login restriction and you can try to login again. You can also call your IT support person and ask them to zero out your login attempt count so you can login without waiting for 20 minutes.

Q: During login, after selecting my VISN and site and entering my access and verify codes, a mostly blank screen appears with the site I selected towards the upper left and a "GO" button next to it. Do I need to click the button to proceed?

> A: No. In fact, if you click the button you will get an error and have to start the login process over again. Just wait for the screen to paint fully.

Q: I'm unable to login. I'm getting this message: "Verify code must be changed before continued use." What should I do?

> A: Your VistA site Verify code has expired and you need to log into VistA. After you enter your Verify code VistA will ask you to re-enter it and enter a new Verify code, then re-enter it to confirm. After you have successfully logged into VistA you should be able to log in to NUMI.

Q: Admin user added a new employee to NUMI and user is now receiving the "User not found in NUMI, Contact your local NUMI site administrator for assistance."

> A: The site ADMIN user with privileges needs to check to make sure the user has been added and assigned a role and that the Field called VHA Username is populated with the Doman and VHA username in the following format: "DOMAIN\vhaxxxxxxxx". The Admin Point of Contact can do a screenshare with the user and the login page with the error message will display the full Domain and VHA username next to the Welcome banner.

Warning / Advisory Messages:

Q: I selected a patient stay from the Stay Movement table, but got a warning message telling me that the stay cannot be retrieved from VistA and may be invalid. Why would this happen?

> A: This warning may occur because an invalid patient admission was entered, and the record was deleted from the hospital database – but not before it was sent to NUMI. The stay can be deleted from NUMI using the Patient Stay Administration option. However, before deleting anything in NUMI, check CPRS or VistA to verify that the admission or movement is no longer in VistA. *(See Chapter 10 in the User Guide for more information about deleting invalid patient stays).*

Working with the NUMI Screens:

Q: Sometimes clicking on the Patient Stay History screen View link does not cause the expected screen to pop up.

> A: It is likely that the screen is already up but hidden in back of another screen. You can use alt-tab to move between screens that are already up, or minimize each screen until you see the hidden screen.

Q: The "typing memory" feature seems to have disappeared. Previously, when I typed in something, NUMI would often complete the text and save me from typing the whole thing.

> A: This happens if your web browser is upgraded to a new version. The auto-populate feature is wiped out when updates are applied, but will return gradually as you use the browser and NUMI (If your local IT policy controls the browser's auto-complete function, this may never be available).

Working with Patient / Attending Information:

Q: I know a patient has been admitted to the hospital and they are in VistA, but I do not see them listed on the Patient Selection/Worklist in NUMI. How can I get them to display?

> A: You can manually synchronize NUMI with what is in VistA. Select Manual VistA Synchronization from the Tools Menu. Choose the desired search options and click the 8

> Find Stays in VistA button. When the results display, click the checkboxes beside the stays you wish to synchronize and select the Synchronize Stays button. NUMI will now show what is in VistA *(See Chapter 11 in the User Guide for more information about using the Manual VistA Synchronization option)*.

Q: I have a patient on the list whose listed Attending Physician is different than the actual Attending. Is this supposed to be so?

> A: When that happens, it is because it was entered inaccurately on the unit or in Admissions. When you put in your review, you can correct this by selecting the correct Attending from the drop-down box on the Primary Review screen *(See Chapter 8 in the User Guide for more information about how to change the Attending Physician)*.

Q: While waiting for a patient's information to load after selecting a stay, if I click on another button, I get an error message and have to start over again.

> A: Please be patient and wait until NUMI responds to a click or other command. Clicking multiple times before the system responds will produce an error.

Q: I changed the Attending on the Primary Review Summary screen - so why does my change not show up on the Patient Selection/Worklist?

> A: That is because it is showing you the values from VistA.

Q: On the patient list under Wards, there is no option to select surgical patients. I have various areas that are not showing up on that list (i.e., one of my CLC units; 3B Observation). How can I get this information?

> A: The Ward list will be populated as movements for those wards occur. It may be that no surgical patients had been picked up yet, and that existing patients had not been picked up by the overnight synchronizer because there were not any qualifying movements. This will be a common phenomenon when NUMI is first up and running. If you know you're missing someone, use the manual synchronizer (Manual VistA Synchronization) feature of NUMI, to get that patient's information. If they are on the missing ward, that ward will also be added to the database (*See Chapter 11 in the User Guide for more information about using the Manual VistA Synchronization option)*. This is not a problem that you need to contact your Help Desk team about. It is just a one-time initial condition that can cause some confusion. It is very similar to the example of a long-term care patient who has not had a movement since NUMI started running, and does not show up in the database.

Q: Patient stays seem to be either disappearing from the Patient Selection/Worklist or never appear. What should I do?

> A: You can always use the Manual VistA Synchronization option to restore them. You might also want to check with other UM reviewers to find out what when and how they dismiss patient stays. It is important to use filtering on the Patient Selection/Worklist to make sure no one dismisses another reviewer's stays.

> A: It is also important to regularly dismiss stays that will not be reviewed to clear up screen clutter and keep NUMI response time reasonable, so UM reviewers should have a procedure for regularly dismissing stays. If you are not seeing patients that you expect to see, check to see which filters are currently applied to your Patient Selection/Worklist. To see a complete list of the patient stays on the List, uncheck all of the filter boxes and click on the GO button at the top of the screen. This will generate a complete list of the patient stays at your facility. Another way to check for patient stays is to look at the *Patient Stay Administration* screen and see if the stay was invalidated because it \[temporarily\] could not be found in VistA (*Follow the instructions for restoring a stay, as described in Section 10.7.2 of the User Guide*).

Q: A patient was admitted and has been in the hospital for a while, but does not appear on the Patient Selection/Worklist. Why does this happen and what can I do?

> A: The automatic midnight and hourly synchronization occasionally may not synchronize a patient movement, due to timing and network problems. Check CPRS, the G&L report, and ward rosters to identify any missing patients. Use the Manual VistA Synchronization feature to add a patient. Also, some patients may have been admitted prior to, and have not had a movement since, the inception of NUMI.

Q: Does resynching with VistA overwrite NUMI data?

> A: Resynching with VistA will always update the stay data, but review data will not be overwritten.

Q: A patient admission was on the G&L but does not appear in VistA as an inpatient.

> A: The admission may have been removed from VistA or the hospital's PIMS staff may be editing the movement record at the same time you are trying to access it. Use the Manual VistA Synchronization option to select the patient and bring the data to NUMI.

Q: Is there a way to pull up data for Admitting Physician?

> A: VistA patient movement data does not include Admitting Physician. In NUMI, you can select the Admitting's name in the Admitting's name on the Primary Review screen.

Working with Patient Stays:

Q: How can I tell who dismissed a patient?

> A: The information will come up on the Dismissed Patient Stays screen. You can get to this screen by selecting Dismissed Patient Stays from the Tools Menu.

(See Chapter 10 in the User Guide for more information about using the Dismissed Patient Stays option).

Q: Do you have any suggestions for how to go about finding and dismissing Discharged, Nursing Home, and Domiciliary patients?

> A: If you have Administrative privileges, you can set up the Treating Specialty Configuration to automatically dismiss these treating specialties. See Section 14.3 for further instructions.

Q: Physicians report receiving several notifications on the same stay for patients admitted Friday night.

> A: It is not that the patient is showing up multiple times, it's a notification for each day. Every review that does not meet criteria will go on the physician's list. It should be explained to the physicians that they do have to review them.

Q: I need to take over reviewing a patient stay that another reviewer had been working on and this involves changing a review previously saved.

> A: If it is appropriate to change a saved review, you can ask your site NUMI POC/Administrator to unlock it. Any reviewer can unlock their own saved reviews, but not a review saved by another reviewer.

Working with Reviews:

Q: If one of my reviews is locked and I need to edit it, do I need to delete and restart everything?

> A: No. You can unlock the review by selecting the Utilization Management Review Listing from the Tools Menu. Click the Reviewer dropdown and your name will appear in the list, by default. Click the Find button and a list of your reviews will display. Click the patient's hyperlink name beside the review you wish to edit to open the review summary. Click the Unlock button. You now have the option to re-review this day again. Remember to select the Final Save button when you are finished with the review *(See Chapter 12 in the User Guide for more information about Unlocking reviews)*.

Q: Is there a way to complete more than one review at a time in NUMI?

> A: No. Only 1 review can be completed at a time. However, you can create *consecutive* reviews by using the Copy Review feature to copy a completed review multiple times \[versus creating a new one from scratch each time\] *(See Chapter 13 and other references in the User Guide for more information about copying a Review*).

Q: Can you clarify the Reason Codes? What are my options?

> A: You will find the list of Admission and Continued Stay Reason Codes in Appendices C and D of the User Guide, respectively.

Q: I'm having trouble when trying to do a retrospective review because it's hard to remember which days have been reviewed and which is next to be reviewed.

> A: On the Primary Review screen, use the gold "Show Reviews" bar that you can click to show the reviews already done for that patient/stay. You can also click on the "View" link for each completed review to see its details in a pop-up window.

Q: Physician reviewers are saying they are spending too much time finding the review information.

> A: The more descriptive the UM reviewer can be in their Reviewer Comment field, the easier it is for the physician. You can enter up to 4000 characters that will appear on the physician review screen, and then the physician only needs to agree or disagree and do a final save to remove the patient from the worklist (Physicians may find it useful to look at the CERMe criteria decision tree at the bottom of the screen).

Q: How long does a Physician Reviewer have to do the reviews? Physician

> A: Utilization Management Advisor (PUMA) reviews expire after 7 business days. The reviews then become locked into the database. A superuser will have to unlock the reviews after the 7 day limit. The limit was 15 days and a change in policy occurred in May of 2020.

Q: What can I do to decrease the time I spend entering reviews into NUMI?

> A: First, stays that do not need reviews should always be dismissed each morning, if they have not been automatically dismissed by the system. Reviewers can use the Reviewer filter, whenever possible. When doing multiple reviews for the same patient, when not copying an existing review, go back to the Patient Stay History page rather than the Patient Selection/Worklist to save some of the longer load times in NUMI.

> You may prefer to use filters versus sorting. One recommendation is that you first check to see that you have all your patients on the Patient Selection/Worklist. If you are missing a patient or two, go to the Tools Menu, select Manual VistA Synchronization, and synchronize any missing patients before beginning your reviews for that day. This will cut down on the disruption of your workflow and ensure that you have all of your assigned patient stays.

Working with Reports:

Q: On those reviews not meeting criteria AND not needing to be sent to a Physician Advisor (e.g., patient is in ICU, awaiting an acute care bed; or a placement problem), do they ultimately get recorded as "approved" or "not approved" if the box is checked? For reporting purposes, how will they break out?

> A: In NUMI, there is no "approved" or "not approved" category. All reviews that go to the Physician Advisor are returned as "Agree with the current level of care" OR "Disagree with the current level of care." A patient review can be exempted from the physician review process through formal hospital policy. All patient reviews not meeting criteria that are automatically exempt are recorded in the NUMI database as Agree with the current level of care. These reviews will be included in all NUMI reports.

Q: If data, such as Attending Physician, is corrected within NUMI, will the corrected value be used on NUMI reports?

> A: Yes. The next time you generate the reports they will reflect the correct Attending Physician's name. These changes are NOT reflected in VistA, because NUMI has READ-ONLY access to VistA.

Working with Text Boxes:

Q: How many characters can I type in the various text boxes in the NUMI application?

> A: The maximum characters that can be typed into the various text boxes are listed below.

- Primary Review Screen
  - Criteria Not Met Elaboration Box is 100 characters
  - The maximum number of characters allowed in the Comments field is 4,000
  - The maximum number of characters allowed in the Custom field is 25

<span id="_Toc465421572" class="anchor"></span>Appendix F – NUMI Review – Screens Encountered

The figure below illustrates the major screens that are encountered doing a review in NUMI.

![](numi-user-guide-version-15-15/286.png)

<span id="_Hlk169016899" class="anchor"></span>Figure 188: Screens Encountered during NUMI Reviews

<span id="_Toc146202596" class="anchor"></span>Appendix G – ACCESS/VERIFY Alternate Login Method

Your domain and network ID will be displayed next to "Welcome" in the blacked-out part of the screenshot displayed in Error! Not a valid bookmark self-reference..

![](numi-user-guide-version-15-15/287.png)

<span id="_Hlk169016907" class="anchor"></span>Figure 189: NUMI Login

1.   Select VISN and Site and Enter Access and Verify Codes

As with other VistA applications, you must select VISN, VistA Site and enter valid access and verify codes to login to NUMI.

2.   To login into NUMI
    1.  *Click* on the Select VISN dropdown. Choose a VISN from the list by *clicking* on it. NOTE: Depending on your UM role, you may have access to several sites. However, you must always log onto NUMI using your home VISN and the facility associated with your VistA Access and Verify Codes. After you are logged into NUMI with your home location, you can then select a different site.
    2.  *Click* the Select Site dropdown. Choose a Site from the list by *clicking* on it.
    3.  Type your VistA access code into the Access Code field and press the \<Tab\> key on your keyboard.
    4.  Type your VistA verify code into the Verify Code field.
    5.  *Click* the \<Access NUMI System\> button and the *Patient Selection/Worklist* screen will display if your credentials match. If not, see Section [3.2.2](\l).
3.  ![](numi-user-guide-version-15-15/288.png) If VISN and/or Site information is not selected from the dropdowns, you will see the messages: "Please select a VISN" and/or "Please select a site".
4.  ![](numi-user-guide-version-15-15/289.png) If you enter an invalid access or verify code, the messages, "You must enter a valid access code," or "You must enter a valid verify code," will display.
5.  ![](numi-user-guide-version-15-15/290.png) If you receive an error message like this one, "This account does not exist in NUMI," ask your local NUMI POC/Administrator to set up a NUMI profile for you.
6.  ![](numi-user-guide-version-15-15/291.png) If you receive an error message like this one, "Unable to login to VistA. The error was: Not a valid ACCESS CODE/VERIFY CODE pair," recheck your Access Verify Code or verify you're logging in to the correct site. You should also verify that you're set up on the VistA side of the site you need to access

![](numi-user-guide-version-15-15/292.png)<span id="_Toc478556900" class="anchor"></span>

Figure 190: Access/Verify code not valid

![](numi-user-guide-version-15-15/293.png) The maximum number of login attempts permitted is determined by the local VistA site. If you exceed the maximum number, VistA will lock you out of the application for 20 minutes. You may see an error message similar to: "Unable to login to VistA. The error was: Device IP address is locked due to too many invalid sign-on attempts". After 20 minutes, VistA will clear your login restriction, and you can try to login again.![](numi-user-guide-version-15-15/294.png) Occasionally, after you've entered your correct access and verify codes you may see an error message similar to the one shown in Error! Not a valid bookmark self-reference.. If this happens, close down your Internet browser and restart the login process. Doing this resets your browser and you will then be able to log in successfully.

7.  

![](numi-user-guide-version-15-15/295.png)<span id="_Toc479683271" class="anchor"></span>

Figure 191: VistA Login Error Message

3.   How your login credentials are authenticated

When you login to NUMI, your NUMI credentials will be compared against your Windows credentials.

(NOTE: The purpose of this comparison is to control the Enhanced Reporting content - not to authenticate your access to the NUMI application. For more information about Enhanced Reporting, please see Section 11).

The system authenticates and tracks users when communication to the system is first established. You must prove your identity to the NUMI web site by supplying a valid VistA Access and Verify Code combination in order to establish this communication. Rather than passing your confidential credentials back and forth with each transaction, the system generates a unique "Session ID" (i.e., Windows session credentials) to identify your session as authenticated.

Subsequent communication between you and the web site will be tagged with the Session ID as "proof" of the authenticated session. For example, when you visit a retailer's website you want to collect articles in a 'shopping cart' and then go to the checkout page to place your order. A Session ID enables the system to keep track of your cart's status.

There are 3 possible credential comparison scenarios, 3.2.2.1, 3.2.2.2 and 3.2.2.3:

4.   The Login Credentials Match

If your NUMI login credentials match your Windows credentials, you will be logged in without seeing any dialog or pop-up boxes.

5.   The Login Credentials are Blank

If your NUMI login credentials are blank (e.g., new NUMI user), the system will apply the current credentials you are using and proceed with logging you in.

6.   The Login Credentials Do Not Match

When you login to NUMI, if your Windows credentials do not match the credentials saved in NUMI, you will see a Security Warning message like the one illustrated in the figure below (One reason for a credential mismatch would be if you logged in to NUMI from someone else's computer). You will be given the opportunity to either update your network account name or logout of NUMI and log back in using your own credentials, as described in Section 3.2.

![](numi-user-guide-version-15-15/296.png)

<span id="_Hlk169016956" class="anchor"></span>Figure 192: Login Security Warning

7.  Updating Your Network Account Name (at Login)
8.  If you wish to update your network account name
    1.  With the Security Warning message displayed, *click* on the <u>Update My</u> <u>Network Account name in NUMI hyperlink</u>.
    2.  The system will update your network account name in the NUMI User table. This update will not be visible to you.
    3.  The *Patient Selection/Worklist* will display.
9.   If you wish to logout without updating your network account name
1)  With the Security Warning message displayed, *click* on the <u>Logout</u> hyperlink.
2)  The system will not update your network account name in the NUMI User table and you will be logged out. You will then be able to login to NUMI as normal using your own credentials.
10. If you wish to continue
1)  With the Security Warning message displayed, *click* on the <u>Click here to</u> <u>continue.</u>
2)  The Patient Selection/Worklist will display.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access and Verify Codes 20, 21, 206
Accessing Patient Information 23
Adding Reviewer Comments *101*
Additional Features in CERMe *90*
Admin Menu 13
Admission Review 96, 97, 99, 100, 112, 113, 174
Admission Sources *48*, *108*, *109*
Admitting Physician *48*, *95*, *96*, *106*, *107*, *110*, *111*
Agreeing / Disagreeing with Current Level of *122*
Agreeing with Current Level of *122*
Allowing ActiveX Controls 5
Allowing Pop-Ups *4*
Assigning a Physician Advisor to a Review *103*
Buttons *12*, *150*
Calculation Rules 117
CERME Review Text *114*, *115*
Changing a Subset Selection *64*
Changing Current Level of Care *100*
Changing Recommended Level of Care *102*
Changing the Size of the Font *61*
Changing Treating Specialty *109*
Changing Ward *111*
Continue Primary Review Button *89*, *90*
Copying a Review from the Primary Review Screen *114*
Copying Reviews *148*
Create a Review with CERMe *86*, *89*
Creating a NUMI Icon on Your Desktop *7*
Criteria Information Notes *81*
Criteria Not Met Elaboration *96*, *100*, *101*, *181*
Criteria Organization *71*
Currently Selected Stay Information *50*
Day Being Reviewed Date *98*
Days Since Admission *36*
Days Since Last VA Acute Care Discharge Calculation *117*
Deactivating a User's Site *159*
Deceased Patients *43*
Deleting a Review *146*
Disagreeing with Current Level of *122*
Dismiss a Patient Stay *49*
Dismissing a Patient Stay *36*
Dropdown Boxes *15*
Editing NUMI User Information 158
Enhanced Reporting 208
Export 90, 92
Filtering by Movement 32
Filtering by Reviewer 30
Filtering Reviews by Date 126
Finding a VistA User 162
Finding Subsets 63
Getting Started 4, 196
Hyperlinks 11
Information Feeds from VistA 25
InterQual Criteria 4, 12, 14, 55, 58, 95
Keyword and Medical Code Search and Instruction Notes 67
Launching NUMI from Your Internet Browser 8
LOC Instruction Note 70
Logout Option 124, 140
Making Sure You Have a VistA Account 7
Manual VistA Synchronization 25, 32, 111, 124, 128, 132, 133
Menu of Review Days 71
Menus 13
Next Review Reminder Date 105
NUMI Physician Advisor Panel 163, 164
NUMI Point of Contact (POC) 10
NUMI Primary Reviewer Panel 163, 164
NUMI Report Access Panel 163, 165
NUMI Review – Screens Encountered 205, 206
NUMI Screen Flow 179
NUMI Site Administrators Panel 163, 164
NUMI User Information and Privileges 156
NUMI Users 152
Observation Met Indicator 79
Overview 1
Patient Selection/Worklist 11, 12, 15, 23, 24, 25, 28, 29, 30, 32, 34, 36, 37, 40, 43, 52, 55, 96, 106, 120, 124, 125, 129, 130, 132, 133, 134, 138, 139, 180, 209
Patient Stay Administration 124, 137, 138
Patient Stay History 11, 12, 13, 14, 41, 44, 48, 49, 51, 52, 55, 96, 115, 129, 134, 142, 148
Patient Stay List 50
Physician Advisor Comments 123
Physician Advisor Review 52, 103, 104, 120, 121, 124, 125, 131, 132, 144
Physician Advisor Worklist 101, 103, 124, 132
Primary Review Screen 48, 96
Primary Review Summary 12, 53, 90, 95, 96, 97, 98, 101, 105, 114, 115, 118
Printing out a Patient Worksheet 56
Products 63, 70, 75
Saving and Locking a Final Review 115, 123
Screen 'Bars' 14
Screen 'Tabs' 13
Search Filters 10
Select Site 155, 206
Selecting a Patient Movement from the Stay Movements Table 52
Selecting a Review Type 59
Selecting a Stay Reason 101
Selecting Patients for Review 41
Selecting the Product, Category and Subsets 62
Sensitive Patients 43
Session Timeout / Lost Sessions 21
Setting Up Your Internet Browser 7
Setting Your Screen Resolution 6
Showing and Hiding the Table of Reviews for a Patient 51
Single Sign-On Login 18, 19
Sorting Information 11
Switching to a Different Site 45
Tools Menu 13, 124
Transition Plan Notes 85
UM Admission Reason Codes 182
UM Continued Stay Reason Codes 187
Unlocking a Locked Primary Review 142
Unlocking and Deleting Reviews 142
Unlocking the Physician Advisor Portion of a Locked Review 143
Unscheduled Readmit 95, 112, 117
Updating Your Network Account Name (at Login) 209
User Instructions 4
[^1]: A hyperlink is a reference to a document or object that the reader can directly access by clicking on it.
[^2]: The NUMI Check-in ID (or "Movement ID" field in the Stay Movements grid on the Patient Stay History screen) is the internal record number in the VistA Patient Movement file \#405, which is not visible to end users.


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: NUMI User Guide Version 15.11

### The Enhanced Reports let you generate a report showing notes that were typed into the Custom field. Enhanced Reports are available through a link on the NUMI Enhanced Reports SharePoint site. Indicating an Unscheduled Readmit within 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This checkbox feature will only display on the screen if you are doing an admission or initial review. Use this feature to indicate that a patient was an unscheduled readmit to the hospital within the past 30 days.

![](numi-user-guide-version-15-11/195.png)

<span id="_bookmark213" class="anchor"></span>Figure 134: Unscheduled Readmit within 30 Days checkbox

#### To indicate an unscheduled readmit within 30 days

1.  *Click* on the Check if Unscheduled Readmit Within 30 Days checkbox to select.
2.  ![](numi-user-guide-version-15-11/196.png) The Enhanced Reports let you generate a report showing reviews performed on unscheduled readmissions. Enhanced Reports are available through the NUMI Enhanced Reports SharePoint site.

### ![](numi-user-guide-version-15-11/203.png) The information that displays on the Enhanced reports will depend on the Admission Review Type that is selected on the *Primary Review Summary* screen. Showing a Patient's Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To show reviews for a patient

1.  *Click* on the \<Show Reviews\> button.
2.  Reviews for the patient will display in a table.

> (NOTE: The button display changes to \<Hide Reviews\>.)

> ![](numi-user-guide-version-15-11/204.png)

<span id="_bookmark221" class="anchor"></span>Figure 139: Show Reviews table display

## To access the online Help feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  *Click* on the Help menu dropdown

> ![](numi-user-guide-version-15-11/284.png)

<span id="_Toc129959101" class="anchor"></span>Figure 185: Help Menu dropdown

2.  Select the On-Line Help option by *clicking* on it and you will be redirected to the OQSV web page.
3.  Click on the NUMI User Guide option in the web page (Here you will be able to click on a link that will open an electronic copy of this User Guide in its entirety. Or, if you prefer, you can click on individual links to each chapter in the document.)
4.  Select the Copyright option by *clicking* on it and you will be redirected to the Change Healthcare CERMe Proprietary Notice page.

![](numi-user-guide-version-15-11/285.png)

<span id="_Toc129959102" class="anchor"></span>Figure 186: OQSV Web Page

![](numi-user-guide-version-15-11/286.png)

<span id="_Toc129959103" class="anchor"></span>Figure 187: Change Healthcare CERMe Proprietary Notice

## Glossary of Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A glossary of UM terms that are relevant to the NUMI application are defined in Table 12.

<table>
<caption><p><span id="_Toc479676301" class="anchor"></span>Table 13: UM Admission Reason Codes</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Acute</p>
</blockquote></td>
<td><blockquote>
<p>A level of health care in which the patient's severity of illness and intensity of service can only be performed in an in-patient setting.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admission Review</p>
</blockquote></td>
<td><blockquote>
<p>An assessment of medical necessity and appropriateness of a hospital admission after the hospitalization has occurred and the patient has been moved to a higher level of care (e.g., from a Ward to MICU). This review is typically performed on admission, within 24 hours following admission or no later than the first business day following the admission.</p>
<p>Standardized review criteria must be used to determine the appropriateness of care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALOC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Alternate Level of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Behavioral Health</p>
</blockquote></td>
<td><blockquote>
<p>Assists in determining initial and successive level of care decisions for psychiatric conditions, chemical dependency and dual diagnosis for individuals at each stage of life, e.g., InterQual® Behavioral Health Criteria.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BH</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Behavioral Health</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CERMe</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Care Enhance Review Manager enterprise. A web-based application, made available by Change Healthcare that provides computerized InterQual® templates to field Utilization Management staff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Concurrent Review</p>
</blockquote></td>
<td><blockquote>
<p>A Behavioral Health review for a patient who has already received an initial review.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Concurrent Review Process</p>
</blockquote></td>
<td><blockquote>
<p>An assessment of medical necessity or appropriateness of services that covers the time period throughout the time of review and the previous 24 hours.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COTS</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Commercial Off-the-Shelf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Computerized Patient Record System</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc479676301" class="anchor"></span>Table 13: UM Admission Reason Codes

<table>
<caption><p><span id="_Toc479676302" class="anchor"></span>Table 14: UM Continued Stay Reason Codes</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CS</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Continued Stay</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DoD</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Department of Defense</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ECT</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Electroconvulsive Therapy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Episode Day of Care</p>
</blockquote></td>
<td><blockquote>
<p>A term commonly used to measure the duration of a single episode of hospitalization. Inpatient days are calculated by subtracting day of admission from day of discharge. However, persons entering and leaving a hospital on the same day have a length of stay of one.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ET</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Eastern Time</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FAQ</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Frequently Asked Questions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>G&amp;L</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Gains and Losses</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIPPA</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Health Insurance Portability and Accountability Act of 1996</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hospital Admission Review</p>
</blockquote></td>
<td><blockquote>
<p>A review that is performed when a patient first comes into the hospital. All admission reviews should be dated with the actual admission date, regardless of when the review is performed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HTTP</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Hypertext Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IAM</p>
</blockquote></td>
<td><blockquote>
<p>Identity and Access Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Internet Explorer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Internal Entry Number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InterQual® Clinical Evidence Summaries</p>
</blockquote></td>
<td><blockquote>
<p>Collection of current white papers that synthesize medical research to support controversial diagnoses, which support second- level medical review recommendations and promote evidence-based standards of care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InterQual® Criteria</p>
</blockquote></td>
<td><blockquote>
<p>InterQual® is a product of the InterQual® division of Change Healthcare Corporation. InterQual® criteria are used to determine if a patient's hospital length of stay is appropriate. The criteria are based on the diagnoses and any treatments involved in the patient's care.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InterQual® Level of Care Criteria</p>
</blockquote></td>
<td><blockquote>
<p>InterQual Level of Care Criteria addresses admissions and continued stays across the continuum of care, from acute settings through homecare</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Term</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Home care and outpatient treatment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IT</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Information Resource Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Level of Care</p>
</blockquote></td>
<td><blockquote>
<p>Refers to the continuum of care, which includes various intensities of service levels such as acute, rehabilitation, sub-acute, home care and outpatient rehabilitation. See also InterQual® Level of Care Criteria.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LOC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Level Of Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDWS</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Medical Domain Web Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Movement Types</p>
</blockquote></td>
<td><blockquote>
<p>A movement refers to the act or process of moving a sick, injured, wounded, or other person to obtain medical care or treatment. Movement types in NUMI include Admission, Continued Stay, Discharge and Transfer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Utilization Management Integration</p>
</blockquote></td>
<td><blockquote>
<p>A Web-based application that automates documentation of clinical features relevant to each patient's condition and the associated clinical services provided as part of VHA's medical benefits package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NQF</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for National Quality Forum</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUMI</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for National Utilization Management Integration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Observation(s)</p>
</blockquote></td>
<td><blockquote>
<p>An alternative level of health care comprising short-stay encounters for patients who require close nursing observation or medical management.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OEF</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Operation Enduring Freedom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OIF</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Operation Iraqi Freedom</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OIG</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Office of Inspector General</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OQSV</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Office of Quality Safety and Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Personal Computer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Point of Contact</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RLOC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Recommended Level Of Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Term</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Severity of Illness</p>
</blockquote></td>
<td><blockquote>
<p>The extent of organ system derangement or physiologic de-compensation for a patient. Classified into minor, moderate, major, and extreme. Meant to provide a basis for evaluating hospital resource use or to establish patient care guidelines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQL</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Structured Query Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Social Security Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SSO</p>
</blockquote></td>
<td><blockquote>
<p>Single Sign-On</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UM</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Utilization Management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>URL</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Utilization Management</p>
</blockquote></td>
<td><blockquote>
<p>The process of evaluating and determining the coverage and the appropriateness of medical care services across the patient health care continuum to ensure the proper use of resources.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Utilization Review</p>
</blockquote></td>
<td><blockquote>
<p>A formal evaluation or the coverage, medical necessity, efficiency or appropriateness of health care services and treatment plans for an individual patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VIA</p>
</blockquote></td>
<td><blockquote>
<p>VistA Integration Adapter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Veterans Integrated Service Network.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VSSC</p>
</blockquote></td>
<td><blockquote>
<p>Acronym for VISN Support Services Center</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc479676302" class="anchor"></span>Table 14: UM Continued Stay Reason Codes

## Appendix A – NUMI Screen Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The figure below illustrates the *basic flow* of the major NUMI screens

![](numi-user-guide-version-15-11/287.png)

<span id="_Toc129959104" class="anchor"></span>Figure 188: Basic Flow of NUMI Screens

> <u>NOTES</u>:

> On the *Primary Review* Screen, only reviews with Do not Meet Criteria status will go to the Physician Advisor Worklist.

## Appendix B – NUMI TIPS for Success

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix contains tips that will help you make the most of working with NUMI.

Remember that each row on the Patient Selection/Worklist is a patient stay. Use the Patient Selection/Worklist to identify your patient stays and the reviews needed. This screen will tell you:

- Time and date of admission
- If the patient is discharged
- When the last review was done
- Whether criteria were met on the last review

Use the Assign Reviewer function. This will make it easier for you to locate your patients on the Patient Selection/Worklist.

When you do a review, NUMI automatically assigns you as the reviewer. If you assign yourself to new admissions in your area of responsibility every day, then you can filter your facility Patient Selection/Worklist by your name, and you will have a complete listing of your active patient stays.

Use your Gains and Losses (G&L) or Ward Roster reports to confirm that all admissions are appearing in NUMI.

Occasionally patient admissions are not picked up by the NUMI synchronizer. When this happens, you can add that patient through the Manual VistA Synchronization feature. If you make certain that all admissions are captured every day, your patient stay list will be complete.

Use short cuts and best practices whenever possible.

As you work with NUMI, you will find the workflow that is best for you. Here are some things that are time-savers:

Navigate around the system using the 4 tabs

Filter your Patient Selection/Worklist– make sure everyone gets an admission review. They will then be in your list daily until you dismiss them.

Use the Copy Review function as much as possible…especially after weekends.

Some people make brief written notes while in CPRS or on the units and enter reviews all at once. Others prefer to toggle back and forth between NUMI and CPRS while doing reviews.

Use Clinical Comments fields strategically.

Enter information in the Clinical Comments boxes that will assist you in identifying critical issues with this stay and jog your memory for future reviews. This is an optional field, if there is nothing notable, leave it blank. For reviews not meeting criteria that will be sent to the Physician Advisor, enter Criteria Not Met Elaboration and Clinical comments that can provide information to help the Physician Advisor understand the Not Met status.

Meet with your Physician Advisor to develop policy and guidelines for reviews. Discuss which types of Not Met reviews should go to the Physician Advisor for review.

If there are categories of Not Meeting reviews that the Physician Advisor would consider "Automatic Agree," consider establishing a formal local policy to not send those to the Physician Advisor. Find out what types of clinical comments are helpful to the Physician Advisor.

Use reporting

The reports are available through the link on the NUMI Report menu, which takes you to reports provided by OQSV. Some are facility aggregates, and some are patient level detail. At day's end, use the patient detail report to print out a summary of your reviews. This is a helpful tool for the following day.

Use the training and help resources available. Ask for help when needed.

The OQSV website will have a NUMI section with helpful tools and resources listed under Quick Links. Call on the NUMI Trainers for assistance as needed.

Be patient with yourself and the NUMI system

It takes time to learn how to apply a new tool like NUMI. NUMI upgrades roll out regularly with new capabilities and changes.

## Appendix C – UM Admission Reason Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 13 provides a list of UM Admission Reason Codes and their definitions.

| UM Code | Code Description for Admission Reviews  | Definition for Reason                                                                                               |
|---------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 8.1 | Outpatient Care                     | Admitted to the inpatient setting for care or services that could be safely provided in the outpatient setting. |
| 8.11    | Work-up                                 | Admitted with unclear diagnosis, vague symptoms, or to confirm a suspected diagnosis.                               |
| 8.12    | Pre-op                                  | Admitted prior to an elective surgical procedure appropriate for the inpatient setting, excluding transplantation.  |
| 8.13    | Ambulatory surgery                      | Admitted for a procedure that is not included on the Inpatient List.                                                |
| 8.14    | Diagnostic study                        | Admission for a diagnostic study to determine the cause of symptoms.                                                |
| 8.1401  | Ablation/EPS                            | Diagnostic study                                                                                                    |
| 8.1402  | Bronchoscopy                            | Diagnostic study                                                                                                    |
| 8.1403  | Cardiac Cath Diagnostic                 | Diagnostic study                                                                                                    |
| 8.1404  | Colonoscopy/EGD                         | Diagnostic study                                                                                                    |
| 8.1405  | CT Scan                                 | Diagnostic study                                                                                                    |
| 8.1406  | Echo-cardiac                            | Diagnostic study                                                                                                    |
| 8.1407  | EEG                                     | Diagnostic study                                                                                                    |
| 8.1408  | ERCP                                    | Diagnostic study                                                                                                    |
| 8.1409  | Interventional Radiology                | Diagnostic study                                                                                                    |
| 8.141   | MPI                                     | Diagnostic study                                                                                                    |
| 8.1411  | MRA/MRV                                 | Diagnostic study                                                                                                    |
| 8.1412  | MRI                                     | Diagnostic study                                                                                                    |
| 8.1413  | Nuclear Med Cardiac                     | Diagnostic study                                                                                                    |
| 8.1414  | Nuclear Med Non-cardiac                 | Diagnostic study                                                                                                    |
| 8.1415  | PET Scan                                | Diagnostic study                                                                                                    |
| 8.1416  | Sleep Study                             | Diagnostic study                                                                                                    |
| 8.1417  | Stress Test                             | Diagnostic study                                                                                                    |
| 8.1419  | Trans-esophageal Echo                   | Diagnostic study                                                                                                    |
| 8.142   | Transthoracic Echo                      | Diagnostic study                                                                                                    |
| 8.1421  | Ultrasound (non-cardiac)                | Diagnostic study                                                                                                    |
| 8.1422  | US/CT Guided Procedure                  | Diagnostic study                                                                                                    |
| 8.1423  | Vascular Studies                        | Diagnostic study                                                                                                    |
| 8.15    | Therapeutic procedure                   | Admitted for a therapeutic procedure indicated as treatment                                                         |
| 8.1501  | Infusions                               | Therapeutic procedure                                                                                               |
| 8.1502  | Transfusions                            | Therapeutic procedure                                                                                               |
| 8.1503  | Chemotherapy                            | Therapeutic procedure                                                                                               |
| 8.1504  | Radiation Therapy                       | Therapeutic procedure                                                                                               |
| 8.1505  | Cardioversion                           | Therapeutic procedure                                                                                               |
| 8.1506  | Cardiac Cath w/Intervention             | Therapeutic procedure                                                                                               |
| 8.1507  | Pacemaker/ICD Implantation              | Therapeutic procedure                                                                                               |
| 8.1508  | Enteral Feeding Tube                    | Therapeutic procedure                                                                                               |
| 8.1509  | ECT                                     | Therapeutic procedure                                                                                               |
| 8.151   | PICC Line Insertion                     | Therapeutic procedure                                                                                               |
| 8.1511  | Paracentesis                            | Therapeutic procedure                                                                                               |
| 8.1512  | Thoracentesis                           | Therapeutic procedure                                                                                               |
| 8.2 | Clinical                            | Clinical factors and/or physician judgment are the basis for admission.                                             |
| 8.21    | Inappropriate LOC                       | Meets criteria for a higher or lower level of care delivered in a hospital; includes observation.                   |
| 8.22    | Lack of Medical Necessity               | Care in a hospital bed not required.                                                                                |
| 8.23    | Comorbid conditions                     | Secondary condition affecting the clinical decision to admit.                                                       |
| 8.24    | BH patient with medical care needs      | Acute BH patient requiring medical/surgical intervention not available on BH unit.                                  |
| 8.25    | Premature Obs. Order                    | Observation ordered prior to the recovery period being completed.                                                   |
| 8.26    | Clinical Variance                       | Requires inpatient hospitalization but does not meet all specific criteria points.                                  |
| 8.3 | Regulatory                          | Admitted for legal not medical reasons.                                                                             |
| 8.31    | Court ordered                           | Court ordered inpatient care.                                                                                       |
| 8.32    | CMS 3 day rule                          | CMS qualifying hospital stay requirement.                                                                           |
| 8.33    | Adult Protective Services               | APS directed admission.                                                                                             |
| 8.4 | Social                              | Social issues are the primary reason for admission.                                                                 |
| 8.41    | Self-Care Deficit                       | Unable to care for basic or medical needs and no family/caregiver                                                   |
| 8.42    | Transportation                          | No timely transport plan in place                                                                                   |
| 8.43    | Planned respite                         | Scheduled respite care requiring hospital setting                                                                   |
| 8.44    | Homeless                                | Requires intervention by Homeless Program.                                                                          |
| 8.5 | Inpatient LOC Availability          | Not in the correct setting due to inpatient bed capacity or lack of an inpatient level of care                      |
| 8.51    | No Inpatient bed available in RLOC      | No bed available in the level of care required                                                                      |
| 8.52    | Inpatient RLOC not provided at facility | Facility lacks inpatient level of care.                                                                             |
| 8.6 | Environmental                       | Environmental conditions create public safety risks and limit access to medical care.                               |
| 8.61    | Adverse Conditions                      | Inclement weather, natural disasters, and/or power outage                                                           |

UM Admission Reason CodesUM Admission Reason Codes

## Appendix D – UM Continued Stay Reason Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 14 provides a list of UM Continued Stay Reason Codes and their definitions.

| UM Code   | Code Description for Cont'd Stay Reviews | Definition for Reason                                                                                                                                                                                                                                                                                                                      |
|-----------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 18.1  | Outpatient Care                      | Awaiting care appropriate for the outpatient setting.                                                                                                                                                                                                                                                                                      |
| 18.11     | Diagnostic                               | Awaiting testing that does not require hospitalization.                                                                                                                                                                                                                                                                                    |
| 18.1101   | Ablation/EPS                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1102   | Bronchoscopy                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1103   | Cardiac Cath Diagnostic                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1104   | Colonoscopy/EGD                          | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1105   | CT Scan                                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1106   | Echo-cardiac                             | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1107   | EEG                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1108   | ERCP                                     | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1109   | Interventional Radiology                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.111    | MPI                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1111   | MRA/MRV                                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1112   | MRI                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1113   | Nuclear Med Cardiac                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1114   | Nuclear Med Non-cardiac                  | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1115   | PET Scan                                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1116   | Sleep Study                              | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1117   | Stress Test                              | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1119   | TEE                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.112    | TTE                                      | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1121   | Ultrasound (non-cardiac)                 | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1122   | US/CT Guided Procedure                   | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.1123   | Vascular Studies                         | Diagnostic                                                                                                                                                                                                                                                                                                                                 |
| 18.12 | Procedures                           | Awaiting procedure appropriate for the ambulatory setting.                                                                                                                                                                                                                                                                                 |
| 18.1201   | Infusions                                | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1202   | Transfusions                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1203   | Chemotherapy                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1204   | Radiation Therapy                        | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1205   | Cardioversion                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1206   | Cardiac Cath w/Intervention              | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1207   | Pacemaker/ICD                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1208   | Enteral Feeding Tube                     | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1209   | ECT                                      | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.121    | PICC Line Insertion                      | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1211   | Paracentesis                             | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1212   | Thoracentesis                            | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.1213   | Surgical Procedure                       | Procedures                                                                                                                                                                                                                                                                                                                                 |
| 18.13 | Consults                             | Awaiting consult appropriate for the ambulatory setting and not necessary for transition to the next level of care.                                                                                                                                                                                                                        |
| 18.131    | Medicine subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.132    | Surgical subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.133    | Psychiatry/Psychology                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.134    | Rehabilitation Medicine                  |                                                                                                                                                                                                                                                                                                                                            |
| 18.135    | Extended Care                            |                                                                                                                                                                                                                                                                                                                                            |
| 18.136    | Neurology                                |                                                                                                                                                                                                                                                                                                                                            |
| 18.137    | Speech & Audiology                       |                                                                                                                                                                                                                                                                                                                                            |
| 18.2  | Clinical                             | Clinical presentation and/or physician judgment.                                                                                                                                                                                                                                                                                           |
| 18.21     | Lack of medical necessity                | Care could be safely rendered in the home or outpatient setting.                                                                                                                                                                                                                                                                           |
| 18.22     | Clinical instability                     | Patient falls outside of the criteria but does not meet discharge screens.                                                                                                                                                                                                                                                                 |
| 18.23     | Comorbid conditions                      | Documentation of secondary or tertiary conditions that are currently delaying patient response to treatment, or creating a deviation in standard evidence-based treatment.                                                                                                                                                                 |
| 18.24     | BH Patient with medical care needs       | BH patient requiring medical/surgical intervention not available on BH unit.                                                                                                                                                                                                                                                               |
| 18.25     | Inappropriate LOC                        | Patient remains in current level of care when care and services could be provided safely in a lower level or more appropriately in a higher level of care. This includes inpatient and post-acute settings available at the facility, CLC, or in the community. Not to be used for patients appropriate for discharge home see code 18.21. |
| 18.26     | No documented plan or evaluation         | Documentation absent or lacking specificity.                                                                                                                                                                                                                                                                                               |
| 18.3  | Regulatory                           | Legal not medical needs.                                                                                                                                                                                                                                                                                                                   |
| 18.31     | Court ordered stay                       | Court order for specified duration of time.                                                                                                                                                                                                                                                                                                |
| 18.32     | CMS 3 day rule                           | Post-acute placement required by CMS.                                                                                                                                                                                                                                                                                                      |
| 18.33     | APS                                      | Adult Protective Services investigation and recommendations pending.                                                                                                                                                                                                                                                                       |
| 18.34     | Guardianship                             | Awaiting guardianship procedures.                                                                                                                                                                                                                                                                                                          |
| 18.4  | Social                               | Unresolved social issues.                                                                                                                                                                                                                                                                                                                  |
| 18.41     | Lack of caregiver                        | Self-care deficit and no support for home management.                                                                                                                                                                                                                                                                                      |
| 18.42     | Transportation                           | Lack of transportation to home or next level of care.                                                                                                                                                                                                                                                                                      |
| 18.43     | Planned respite                          | Scheduled respite requiring hospital setting                                                                                                                                                                                                                                                                                               |
| 18.44     | Homeless                                 | Requires arrangements for temporary housing and/or intervention by Homeless Program                                                                                                                                                                                                                                                        |
| 18.45     | Resistance to discharge plan             | Patient or the family resists plan for next level of care.                                                                                                                                                                                                                                                                                 |
| 18.5  | Inpatient LOC Availability               | Not in the correct inpatient setting due to capacity or lack of the appropriate inpatient level of care.                                                                                                                                                                                                                                   |
| 18.51     | No bed available in Inpatient RLOC       | Insufficient capacity in the level of care requires the patient to remain in a higher or lower level of care than needed.                                                                                                                                                                                                                  |
| 18.52     | Inpatient RLOC not provided at facility  | The needed level of Inpatient care is not available at the facility. Does not include post-acute levels of care.                                                                                                                                                                                                                           |
| 18.53     | Inpatient Transfer Delay                 | Patients requiring transfer for continued inpatient care needs at another facility. Not to be used for patients awaiting NG, CLC, or other post-acute settings.                                                                                                                                                                            |
| 18.531    | VA Facility                              | Transfer Delay                                                                                                                                                                                                                                                                                                                             |
| 18.532    | Non-VA Facility                          | Transfer Delay                                                                                                                                                                                                                                                                                                                             |
| 18.6  | Environmental                        | Environmental conditions create public safety risks and limit access to medical care                                                                                                                                                                                                                                                       |
| 18.61     | Adverse Conditions                       | Inclement weather, natural disasters, and/or power outage                                                                                                                                                                                                                                                                                  |
| 18.7  | Post-Acute Transition                | Awaiting transition to post-acute setting                                                                                                                                                                                                                                                                                                  |
| 18.71     | Placement Issues                         | Post-acute placement delays                                                                                                                                                                                                                                                                                                                |
| 18.711    | Financial                                | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.712    | Administrative                           | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.713    | Clinical                                 | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.714    | Behavioral                               | Placement Issues                                                                                                                                                                                                                                                                                                                           |
| 18.72     | Awaiting CLC acceptance                  | Pending CLC Consult, screening or acceptance                                                                                                                                                                                                                                                                                               |
| 18.73     | Awaiting CLC bed                         | CLC without bed or ability to receive patients                                                                                                                                                                                                                                                                                             |
| 18.74     | Awaiting community placement             | Delay in transitioning patient to community nursing home                                                                                                                                                                                                                                                                                   |
| 18.741    | VA paid                                  | Awaiting community placement                                                                                                                                                                                                                                                                                                               |
| 18.742    | Non-VA paid                              | Awaiting community placement                                                                                                                                                                                                                                                                                                               |
| 18.75     | Ineffective discharge planning/process   | DC planning/interventions delay                                                                                                                                                                                                                                                                                                            |
| 18.76 | Awaiting VA Post-Acute Bed               | Patient requires post-acute care following hospital stay other than CLC/Nursing home care but no beds in appropriate LOC due to capacity issues.                                                                                                                                                                                           |
| 18.8  | Scheduling delays/cancellations          | Test, procedure, or surgery is cancelled or delayed                                                                                                                                                                                                                                                                                        |
| 18.81     | Delayed diagnostic test                  | Diagnostic test cancelled or delayed                                                                                                                                                                                                                                                                                                       |
| 18.8101   | Ablation/EPS                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8102   | Bronchoscopy                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8103   | Cardiac Cath Diagnostic                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8104   | Colonoscopy/EGD                          | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8105   | CT Scan                                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8106   | Echo-cardiac                             | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8107   | EEG                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8108   | ERCP                                     | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8109   | Interventional Radiology                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.811    | MPI                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8111   | MRA/MRV                                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8112   | MRI                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8113   | Nuclear Med Cardiac                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8114   | Nuclear Med Non-cardiac                  | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8115   | PET Scan                                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8116   | Sleep Study                              | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8117   | Stress Test                              | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8118   | Swallow Study                            | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8119   | TEE                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.812    | TTE                                      | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8121   | Ultrasound (non-cardiac)                 | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8122   | US/CT Guided Procedure                   | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.8123   | Vascular Studies                         | Delayed diagnostic test                                                                                                                                                                                                                                                                                                                    |
| 18.82     | Delayed Surgery/procedure                | Surgery or procedure cancelled or delayed                                                                                                                                                                                                                                                                                                  |
| 18.8201   | Infusions                                | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8202   | Transfusions                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8203   | Chemotherapy                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8204   | Radiation Therapy                        | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8205   | Cardioversion                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8206   | Cardiac Cath w/Intervention              | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8207   | Pacemaker/ICD                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8208   | Enteral Feeding Tube                     | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8209   | ECT                                      | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.821    | PICC Line Insertion                      | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8211   | Paracentesis                             | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8212   | Thoracentesis                            | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.8213   | Surgical Procedure                       | Delayed Surgery/procedure                                                                                                                                                                                                                                                                                                                  |
| 18.83     | Consults                                 | Awaiting completion of consultation appropriate and necessary for transition to the next level of care. Consults are needed prior to discharge or transfer to a lower level of care.                                                                                                                                                       |
| 18.8301   | Medicine subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8302   | Surgical subspecialty                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8303   | Psychiatry/Psychology                    |                                                                                                                                                                                                                                                                                                                                            |
| 18.8304   | Rehabilitation Medicine                  |                                                                                                                                                                                                                                                                                                                                            |
| 18.8305   | Extended Care                            |                                                                                                                                                                                                                                                                                                                                            |
| 18.8306   | Neurology                                |                                                                                                                                                                                                                                                                                                                                            |
| 18.8307   | Speech & Audiology                       |                                                                                                                                                                                                                                                                                                                                            |
| 18.8308   | Interventional Radiology                 |                                                                                                                                                                                                                                                                                                                                            |

UM Continued Stay Reason Codes TableTable listing the UM Continued Stay Reason Codes.

## Appendix E – Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix contains a list of Frequently Asked Questions about NUMI:

*Getting Started:*

> Q: What do I need before I start using NUMI?

> A: This is what you will need:

- a Windows PC on the VA intranet, running the version of Microsoft Internet Explorer currently approved and in use in the VA
  - While it is expected that NUMI will run on your PC without any difficulty, should you experience problems please contact your local IT for assistance. Many issues can be resolved by changing some settings on the PC (*See <u>Section 2</u> in the User Guide for more information*). If you are not permitted to change settings yourself due to restrictions at your particular VA site, your local IT can help you.
- a Personal Identity Verification (PIV) card
  - A PIV card is needed for Single Sign-on access.
- a production VistA account at one site that has CPRS access to that site
  - You only need one "home" login site. Please note that NUMI access is completely separate from access for CPRS and VistAWeb - you will need to arrange for those rights separately. Performing reviews in NUMI without proper additional clinical informatics tools such as CPRS and VistAWeb is strongly discouraged.
- to have your account set up by a NUMI Administrator
  - The rights you will need will depend on whether you are a Primary Reviewer, a Physician Advisor or an Administrator.
- the URL for the NUMI application
  - This will be provided to you after you have attended NUMI training.

> *Login Error Messages:*

> Q: I'm unable to login to VistA. I'm getting this message: "Unable to login to VistA. The error was: Device IP address is locked due to too many invalid sign on attempts." What should I do?

> A: This error means you have exceeded the maximum number of login attempts permitted by your local VistA. When this happens, VistA will lock you out of the NUMI application for 20 minutes. After 20 minutes, VistA will clear your login restriction and you can try to login again. You can also call your IT support person and ask them to zero out your login attempt count so you can login without waiting for 20 minutes.

> Q: During login, after selecting my VISN and site and entering my access and verify codes, a mostly blank screen appears with the site I selected towards the upper left and a "GO" button next to it. Do I need to click the button to proceed?

> A: No. In fact, if you click the button you will get an error and have to start the login process over again. Just wait for the screen to paint fully.

> Q: I'm unable to login. I'm getting this message: "Verify code must be changed before continued use." What should I do?

> A: Your VistA site Verify code has expired and you need to log into VistA. After you enter your Verify code VistA will ask you to re-enter it and enter a new Verify code, then re-enter it to confirm. After you have successfully logged into VistA you should be able to log in to NUMI.

> Q: Admin user added a new employee to NUMI and user is now receiving the "User not found in NUMI, Contact your local NUMI site administrator for assistance."

> A: The site ADMIN user with privileges needs to check to make sure the user has been added and assigned a role and that the Field called VHA Username is populated with the Doman and VHA username in the following format: "DOMAIN\vhaxxxxxxxx". The Admin Point of Contact can do a screenshare with the user and the login page with the error message will display the full Domain and VHA username next to the Welcome banner.

> *Warning / Advisory Messages:*

> Q: I selected a patient stay from the Stay Movement table, but got a warning message telling me that the stay cannot be retrieved from VistA and may be invalid. Why would this happen?

> A: This warning may occur because an invalid patient admission was entered, and the record was deleted from the hospital database – but not before it was sent to NUMI. The stay can be deleted from NUMI using the Patient Stay Administration option. However, before deleting anything in NUMI, check CPRS or VistA to verify that the admission or movement is no longer in VistA. *(See Chapter 10 in the User Guide for more information about deleting invalid patient stays).*

> *Working with the NUMI Screens:*

> Q: Sometimes clicking on the Patient Stay History screen View link does not cause the expected screen to pop up.

> A: It is likely that the screen is already up but hidden in back of another screen. You can use alt-tab to move between screens that are already up, or minimize each screen until you see the hidden screen.

> Q: The "typing memory" feature seems to have disappeared. Previously, when I typed in something, NUMI would often complete the text and save me from typing the whole thing.

> A: This happens if your web browser is upgraded to a new version. The auto-populate feature is wiped out when updates are applied, but will return gradually as you use the browser and NUMI (If your local IT policy controls the browser's auto-complete function, this may never be available).

> *Working with Patient / Attending Information:*

> Q: I know a patient has been admitted to the hospital and they are in VistA, but I do not see them listed on the Patient Selection/Worklist in NUMI. How can I get them to display?

> A: You can manually synchronize NUMI with what is in VistA. Select Manual VistA Synchronization from the Tools Menu. Choose the desired search options and click the 8

> Find Stays in VistA button. When the results display, click the checkboxes beside the stays you wish to synchronize and select the Synchronize Stays button. NUMI will now show what is in VistA *(See Chapter 11 in the User Guide for more information about using the Manual VistA Synchronization option)*.

> Q: I have a patient on the list whose listed Attending Physician is different than the actual Attending. Is this supposed to be so?

> A: When that happens, it is because it was entered inaccurately on the unit or in Admissions. When you put in your review, you can correct this by selecting the correct Attending from the drop-down box on the Primary Review screen *(See Chapter 8 in the User Guide for more information about how to change the Attending Physician)*.

> Q: While waiting for a patient's information to load after selecting a stay, if I click on another button, I get an error message and have to start over again.

> A: Please be patient and wait until NUMI responds to a click or other command. Clicking multiple times before the system responds will produce an error.

> Q: I changed the Attending on the Primary Review Summary screen - so why does my change not show up on the Patient Selection/Worklist?

> A: That is because it is showing you the values from VistA.

> Q: On the patient list under Wards, there is no option to select surgical patients. I have various areas that are not showing up on that list (i.e., one of my CLC units; 3B Observation). How can I get this information?

> A: The Ward list will be populated as movements for those wards occur. It may be that no surgical patients had been picked up yet, and that existing patients had not been picked up by the overnight synchronizer because there were not any qualifying movements. This will be a common phenomenon when NUMI is first up and running. If you know you're missing someone, use the manual synchronizer (Manual VistA Synchronization) feature of NUMI, to get that patient's information. If they are on the missing ward, that ward will also be added to the database (*See Chapter 11 in the User Guide for more information about using the Manual VistA Synchronization option)*. This is not a problem that you need to contact your Help Desk team about. It is just a one-time initial condition that can cause some confusion. It is very similar to the example of a long-term care patient who has not had a movement since NUMI started running, and does not show up in the database.

> Q: Patient stays seem to be either disappearing from the Patient Selection/Worklist or never appear. What should I do?

> A: You can always use the Manual VistA Synchronization option to restore them. You might also want to check with other UM reviewers to find out what when and how they dismiss patient stays. It is important to use filtering on the Patient Selection/Worklist to make sure no one dismisses another reviewer's stays.

> A: It is also important to regularly dismiss stays that will not be reviewed to clear up screen clutter and keep NUMI response time reasonable, so UM reviewers should have a procedure for regularly dismissing stays. If you are not seeing patients that you expect to see, check to see which filters are currently applied to your Patient Selection/Worklist. To see a complete list of the patient stays on the List, uncheck all of the filter boxes and click on the GO button at the top of the screen. This will generate a complete list of the patient stays at your facility. Another way to check for patient stays is to look at the *Patient Stay Administration* screen and see if the stay was invalidated because it \[temporarily\] could not be found in VistA (*Follow the instructions for restoring a stay, as described in Section 10.7.2 of the User Guide*).

> Q: A patient was admitted and has been in the hospital for a while, but does not appear on the Patient Selection/Worklist. Why does this happen and what can I do?

> A: The automatic midnight and hourly synchronization occasionally may not synchronize a patient movement, due to timing and network problems. Check CPRS, the G&L report, and ward rosters to identify any missing patients. Use the Manual VistA Synchronization feature to add a patient. Also, some patients may have been admitted prior to, and have not had a movement since, the inception of NUMI.

> Q: Does resynching with VistA overwrite NUMI data?

> A: Resynching with VistA will always update the stay data, but review data will not be overwritten.

> Q: A patient admission was on the G&L but does not appear in VistA as an inpatient.

> A: The admission may have been removed from VistA or the hospital's PIMS staff may be editing the movement record at the same time you are trying to access it. Use the Manual VistA Synchronization option to select the patient and bring the data to NUMI.

> Q: Is there a way to pull up data for Admitting Physician?

> A: VistA patient movement data does not include Admitting Physician. In NUMI, you can select the Admitting's name in the Admitting's name on the Primary Review screen.

> *Working with Patient Stays:*

> Q: How can I tell who dismissed a patient?

> A: The information will come up on the Dismissed Patient Stays screen. You can get to this screen by selecting Dismissed Patient Stays from the Tools Menu.

> *(See Chapter 10 in the User Guide for more information about using the Dismissed Patient Stays option)*.

> Q: Do you have any suggestions for how to go about finding and dismissing Discharged, Nursing Home, and Domiciliary patients?

> A: If you have Administrative privileges, you can set up the Treating Specialty Configuration to automatically dismiss these treating specialties. See Section 14.3 for further instructions.

> Q: Physicians report receiving several notifications on the same stay for patients admitted Friday night.

> A: It is not that the patient is showing up multiple times, it's a notification for each day. Every review that does not meet criteria will go on the physician's list. It should be explained to the physicians that they do have to review them.

> Q: I need to take over reviewing a patient stay that another reviewer had been working on and this involves changing a review previously saved.

> A: If it is appropriate to change a saved review, you can ask your site NUMI POC/Administrator to unlock it. Any reviewer can unlock their own saved reviews, but not a review saved by another reviewer.

> *Working with Reviews:*

> Q: If one of my reviews is locked and I need to edit it, do I need to delete and restart everything?

> A: No. You can unlock the review by selecting the Utilization Management Review Listing from the Tools Menu. Click the Reviewer dropdown and your name will appear in the list, by default. Click the Find button and a list of your reviews will display. Click the patient's hyperlink name beside the review you wish to edit to open the review summary. Click the Unlock button. You now have the option to re-review this day again. Remember to select the Final Save button when you are finished with the review *(See Chapter 12 in the User Guide for more information about Unlocking reviews)*.

> Q: Is there a way to complete more than one review at a time in NUMI?

> A: No. Only 1 review can be completed at a time. However, you can create *consecutive* reviews by using the Copy Review feature to copy a completed review multiple times \[versus creating a new one from scratch each time\] *(See Chapter 13 and other references in the User Guide for more information about copying a Review*).

> Q: Can you clarify the Reason Codes? What are my options?

> A: You will find the list of Admission and Continued Stay Reason Codes in Appendices D and E of the User Guide, respectively.

> Q: I'm having trouble when trying to do a retrospective review because it's hard to remember which days have been reviewed and which is next to be reviewed.

> A: On the Primary Review screen, use the gold "Show Reviews" bar that you can click to show the reviews already done for that patient/stay. You can also click on the "View" link for each completed review to see its details in a pop-up window.

> Q: Physician reviewers are saying they are spending too much time finding the review information.

> A: The more descriptive the UM reviewer can be in their Reviewer Comment field, the easier it is for the physician. You can enter up to 4000 characters that will appear on the physician review screen, and then the physician only needs to agree or disagree and do a final save to remove the patient from the worklist (Physicians may find it useful to look at the CERMe criteria decision tree at the bottom of the screen).

> Q: How long does a Physician Reviewer have to do the reviews? Physician Utilization Management Advisor (PUMA) reviews expire after 7 business days. The reviews then become locked into the database. A superuser will have to unlock the reviews after the 7 day limit. The limit was 15 days and a change in policy occurred in May of 2020.

> Q: What can I do to decrease the time I spend entering reviews into NUMI?

> A: First, stays that do not need reviews should always be dismissed each morning, if they have not been automatically dismissed by the system. Reviewers can use the Reviewer filter, whenever possible. When doing multiple reviews for the same patient, when not copying an existing review, go back to the Patient Stay History page rather than the Patient Selection/Worklist to save some of the longer load times in NUMI.

> You may prefer to use filters versus sorting. One recommendation is that you first check to see that you have all your patients on the Patient Selection/Worklist. If you are missing a patient or two, go to the Tools Menu, select Manual VistA Synchronization, and synchronize any missing patients before beginning your reviews for that day. This will cut down on the disruption of your workflow and ensure that you have all of your assigned patient stays.

> *Working with Reports:*

> Q: On those reviews not meeting criteria AND not needing to be sent to a Physician Advisor (e.g., patient is in ICU, awaiting an acute care bed; or a placement problem), do they ultimately get recorded as "approved" or "not approved" if the box is checked? For reporting purposes, how will they break out?

> A: In NUMI, there is no "approved" or "not approved" category. All reviews that go to the Physician Advisor are returned as "Agree with the current level of care" OR "Disagree with the current level of care." A patient review can be exempted from the physician review process through formal hospital policy. All patient reviews not meeting criteria that are automatically exempt are recorded in the NUMI database as Agree with the current level of care. These reviews will be included in all NUMI reports.

> Q: If data, such as Attending Physician, is corrected within NUMI, will the corrected value be used on NUMI reports?

> A: Yes. The next time you generate the reports they will reflect the correct Attending Physician's name. These changes are NOT reflected in VistA, because NUMI has READ-ONLY access to VistA.

> *Working with Text Boxes:*

> Q: How many characters can I type in the various text boxes in the NUMI application?

> A: The maximum characters that can be typed into the various text boxes are listed below.

- Primary Review Screen
  - Criteria Not Met Elaboration Box is 100 characters
  - The maximum number of characters allowed in the Comments field is 4,000
  - The maximum number of characters allowed in the Custom field is 25

## Appendix F – NUMI Review – Screens Encountered

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The figure below illustrates the major screens that are encountered doing a review in NUMI.

![](numi-user-guide-version-15-11/288.png)

<span id="_Toc129959105" class="anchor"></span>Figure 189: Screens Encountered during NUMI Reviews

## Appendix G – ACCESS/VERIFY Alternate Login Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your domain and network ID will be displayed next to "Welcome" in the blacked-out part of the screenshot displayed in Error! Reference source not found..

![](numi-user-guide-version-15-11/289.png)

<span id="_Toc129959106" class="anchor"></span>Figure 190: NUMI Login

1.   Select VISN and Site and Enter Access and Verify Codes

As with other VistA applications, you must select VISN, VistA Site and enter valid access and verify codes to login to NUMI.

2.   To login into NUMI
1.  *Click* on the Select VISN dropdown. Choose a VISN from the list by *clicking* on it. NOTE: Depending on your UM role, you may have access to several sites. However, you must always log onto NUMI using your home VISN and the facility associated with your VistA Access and Verify Codes. After you are logged into NUMI with your home location, you can then select a different site.
2.  *Click* the Select Site dropdown. Choose a Site from the list by *clicking* on it.
3.  Type your VistA access code into the Access Code field and press the \<Tab\> key on your keyboard.
4.  Type your VistA verify code into the Verify Code field.
5.  *Click* the \<Access NUMI System\> button and the *Patient Selection/Worklist* screen will display if your credentials match. If not, see Section [3.2.2](#_bookmark51).
3.  ![](numi-user-guide-version-15-11/290.png) If VISN and/or Site information is not selected from the dropdowns, you will see the messages: "Please select a VISN" and/or "Please select a site".
4.  ![](numi-user-guide-version-15-11/291.png) If you enter an invalid access or verify code, the messages, "You must enter a valid access code," or "You must enter a valid verify code," will display.
5.  ![](numi-user-guide-version-15-11/292.png) If you receive an error message like this one, "This account does not exist in NUMI," ask your local NUMI POC/Administrator to set up a NUMI profile for you.
6.  ![](numi-user-guide-version-15-11/293.png) If you receive an error message like this one, "Unable to login to VistA. The error was: Not a valid ACCESS CODE/VERIFY CODE pair," recheck your Access Verify Code or verify you're logging in to the correct site. You should also verify that you're set up on the VistA side of the site you need to access

![](numi-user-guide-version-15-11/294.png)<span id="_Toc478556900" class="anchor"></span>

Figure 191: Access/Verify code not valid

![](numi-user-guide-version-15-11/295.png) The maximum number of login attempts permitted is determined by the local VistA site. If you exceed the maximum number, VistA will lock you out of the application for 20 minutes. You may see an error message similar to: "Unable to login to VistA. The error was: Device IP address is locked due to too many invalid sign-on attempts". After 20 minutes, VistA will clear your login restriction, and you can try to login again.![](numi-user-guide-version-15-11/296.png) Occasionally, after you've entered your correct access and verify codes you may see an error message similar to the one shown in Error! Reference source not found.. If this happens, close down your Internet browser and restart the login process. Doing this resets your browser and you will then be able to log in successfully.

7.  

![](numi-user-guide-version-15-11/297.png)<span id="_Toc479683271" class="anchor"></span>

Figure 192: VistA Login Error Message

3.   How your login credentials are authenticated

When you login to NUMI, your NUMI credentials will be compared against your Windows credentials.

(NOTE: The purpose of this comparison is to control the Enhanced Reporting content - not to authenticate your access to the NUMI application. For more information about Enhanced Reporting, please see Section 11).

The system authenticates and tracks users when communication to the system is first established. You must prove your identity to the NUMI web site by supplying a valid VistA Access and Verify Code combination in order to establish this communication. Rather than passing your confidential credentials back and forth with each transaction, the system generates a unique "Session ID" (i.e., Windows session credentials) to identify your session as authenticated.

Subsequent communication between you and the web site will be tagged with the Session ID as "proof" of the authenticated session. For example, when you visit a retailer's website you want to collect articles in a 'shopping cart' and then go to the checkout page to place your order. A Session ID enables the system to keep track of your cart's status.

There are 3 possible credential comparison scenarios, 3.2.2.1, 3.2.2.2 and 3.2.2.3:

4.   The Login Credentials Match

If your NUMI login credentials match your Windows credentials, you will be logged in without seeing any dialog or pop-up boxes.

5.   The Login Credentials are Blank

If your NUMI login credentials are blank (e.g., new NUMI user), the system will apply the current credentials you are using and proceed with logging you in.

6.   The Login Credentials Do Not Match

When you login to NUMI, if your Windows credentials do not match the credentials saved in NUMI, you will see a Security Warning message like the one illustrated in the figure below (One reason for a credential mismatch would be if you logged in to NUMI from someone else's computer). You will be given the opportunity to either update your network account name or logout of NUMI and log back in using your own credentials, as described in Section 3.2.

![](numi-user-guide-version-15-11/298.png)

<span id="_Toc129959109" class="anchor"></span>Figure 193: Login Security Warning

7.  Updating Your Network Account Name (at Login)
8.  If you wish to update your network account name
    1.  With the Security Warning message displayed, *click* on the <u>Update My</u> <u>Network Account name in NUMI hyperlink</u>.
    2.  The system will update your network account name in the NUMI User table. This update will not be visible to you.
    3.  The *Patient Selection/Worklist* will display.
9.   If you wish to logout without updating your network account name
1.  With the Security Warning message displayed, *click* on the <u>Logout</u> hyperlink.
2.  The system will not update your network account name in the NUMI User table and you will be logged out. You will then be able to login to NUMI as normal using your own credentials.
10. If you wish to continue
1.  With the Security Warning message displayed, *click* on the <u>Click here to</u> <u>continue.</u>
2.  The *Patient Selection/Worklist* will display.

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access and Verify Codes 19, 20, 192
Accessing Patient Information 21
Adding Reviewer Comments *96*
Additional Features in CERMe *86*
Admin Menu 12
Admission Review 91, 92, 95, 107, 108, 162
Admission Sources *45*, *103*, *104*
Admitting Physician *44*, *90*, *92*, *101*, *102*, *105*, *106*
Agreeing / Disagreeing with Current Level of *115*
Agreeing with Current Level of *115*
Allowing ActiveX Controls 5
Allowing Pop-Ups *4*
Assigning a Physician Advisor to a Review *98*
Buttons *11*, *12*, *141*
Calculation Rules 111
CERME Review Text *109*
Changing a Subset Selection *59*
Changing Current Level of Care *95*
Changing Recommended Level of Care *98*
Changing the Size of the Font *57*
Changing Treating Specialty *104*
Changing Ward *106*
Continue Primary Review Button *85*, *86*
Copying a Review from the Primary Review Screen *109*
Copying Reviews *139*
Create a Review with CERMe *82*, *85*
Creating a NUMI Icon on Your Desktop *7*
Criteria Information Notes *76*
Criteria Not Met Elaboration *91*, *96*, *169*
Criteria Organization *66*
Currently Selected Stay Information *47*
Day Being Reviewed Date *94*
Days Since Admission *33*
Days Since Last VA Acute Care Discharge Calculation *111*
Deactivating a User's Site *150*
Deceased Patients *40*
Deleting a Review *137*
Disagreeing with Current Level of *115*
Dismiss a Patient Stay *46*
Dismissing a Patient Stay *34*
Dropdown Boxes *14*
Editing NUMI User Information 149
Export 86, 88
Filtering by Movement 30
Filtering by Reviewer 28
Filtering Reviews by Date 119
Finding a VistA User 153
Finding Subsets 59
Getting Started 3, 182
Hyperlinks 10
Information Feeds from VistA 23
InterQual Criteria 4, 11, 13, 51, 53, 91
Keyword and Medical Code Search and Instruction Notes 63
Launching NUMI from Your Internet Browser 8
LOC Instruction Note 66
Logout Option 117, 132
Making Sure You Have a VistA Account 6
Manual VistA Synchronization 23, 29, 106, 117, 120, 124, 125
Menu of Review Days 66
Menus 12
Next Review Reminder Date 100, 101
NUMI Physician Advisor Panel 154, 156
NUMI Point of Contact (POC) 9
NUMI Primary Reviewer Panel 154, 156
NUMI Report Access Panel 154, 156
NUMI Review – Screens Encountered 190, 192
NUMI Screen Flow 167
NUMI Site Administrators Panel 154, 156
NUMI User Information and Privileges 147
NUMI Users 143
Observation Met Indicator 74
Overview 1
Patient Selection/Worklist 10, 11, 14, 20, 21, 22, 23, 26, 27, 28, 30, 32, 34, 35, 38, 41, 48, 51, 92, 101, 113, 117, 118, 121, 122, 124, 125, 126, 130, 131, 168, 195
Patient Stay Administration 117, 129, 130
Patient Stay History 10, 11, 12, 13, 39, 41, 44, 46, 47, 48, 51, 92, 109, 121, 126, 133, 139
Patient Stay List 46
Physician Advisor Comments 116
Physician Advisor Review 48, 98, 99, 113, 114, 117, 118, 124, 135
Physician Advisor Worklist 96, 99, 116, 124
Primary Review Screen 44, 45, 91
Primary Review Summary 11, 49, 86, 90, 91, 92, 94, 97, 101, 109, 110, 112
Printing out a Patient Worksheet 52
Products 58, 66, 70
Saving and Locking a Final Review 109, 116
Screen 'Bars' 13
Screen 'Tabs' 12
Search Filters 9
Select Site 146, 192
Selecting a Patient Movement from the Stay Movements Table 48
Selecting a Review Type 54
Selecting a Stay Reason 97
Selecting Patients for Review 39
Selecting the Product, Category and Subsets 58
Sensitive Patients 41
Session Timeout / Lost Sessions 19, 20
Setting Up Your Internet Browser 7
Setting Your Screen Resolution 5
Showing and Hiding the Table of Reviews for a Patient 47
Single Sign-On Login 16, 17
Sorting Information 11
Switching to a Different Site 42
Table of Contents xxiii
Tools Menu 12, 116, 117
Transition Plan Notes 81
UM Admission Reason Codes 169
UM Continued Stay Reason Codes 174
Unlocking a Locked Primary Review 132
Unlocking and Deleting Reviews 132
Unlocking the Physician Advisor Portion of a Locked Review 135
Unscheduled Readmit 91, 107, 111
Updating Your Network Account Name (at Login) 195
User Instructions 3
[^1]: A hyperlink is a reference to a document or object that the reader can directly access by clicking on it.
[^2]: The NUMI Check-in ID (or "Movement ID" field in the Stay Movements grid on the Patient Stay History screen) is the internal record number in the VistA Patient Movement file \#405, which is not visible to end users.

### From: NUMI User Guide

### VA Microsoft EntraId Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first page that you will see when you open the NUMI application in a browser if your browser is not automatically authenticated with Microsoft EntraId is the VA Microsoft login screen, shown in the figure below.

Type in your VA email or select your email account if its listed. You will be presented with a certificate selection screen.

<span id="_Hlk169013877" class="anchor"></span>Figure 12: VA Microsoft Login

![](numi-user-guide/024.png)

Select the correct certificate (same as you use to login to your VA computer) and click on OK. Then you will be prompted to enter the PIN as shown in Figure 14.

<span id="_Hlk169013882" class="anchor"></span>Figure 13: PIV Certificate selection

![](numi-user-guide/025.png)

Enter your PIN and click on OK to complete the EntraId login. On successful authentication of the PIV card the user will be directed to "*Patient Selection/Worklist"* screen.

<span id="_Hlk169013885" class="anchor"></span>Figure 14: PIN Entry

![](numi-user-guide/026.png)

### Agreeing or Disagreeing Whether Care is Clinically Indicated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this feature to show whether or not the PUMA agrees that the care is clinically indicated or not.

#### To Agree with the Current Care

1.  Select Care IS clinically indicated.

#### To Disagree with the Current Care

1.  Select Care is NOT clinically indicated.

<span id="_Hlk169015199" class="anchor"></span>Figure 149: Physician Advisor Review Selection

![](numi-user-guide/220.png)
