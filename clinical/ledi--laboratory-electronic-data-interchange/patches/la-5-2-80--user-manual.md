---
title: LA*5.2*80/LR*5.2*427 LDSI/LEDI IV Update User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*80
group_key: "LEDI:LA:5.2"
file_numbers: 
  - 4
  - 62
  - 64
security_keys: []
menu_options: 5
description: 
audience: 
keywords: 
  - span
  - class
  - mark
  - report
  - laboratory
  - table
  - test
  - ledi
  - accession
  - contents
page_count: 0
word_count: 42603
section_count: 23
table_count: 39
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iv_um_update.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iv_um_update.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

Laboratory Data Sharing and Interoperability (LDSI)

Laboratory Electronic Data Interchange IV  
(LEDI IV)

VA Shield

![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/001.png)

LDSI/LEDI IV User Manual

August 2013

(Revised June 2018)

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

<span id="_Toc510168817" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Toc510169020" class="anchor"></span>Table 1. Precedence of parameters</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 53%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6/2018</td>
<td>2.8</td>
<td><p>Changes for patch LA*5.2*95. This enhancement add a customizable parameter in VistA that allows Laboratory staff at each site to determine the default response when prompted to create a shipping manifest.</p>
<ul>
<li><p>Updated <u>Table 2. LEDI IV patch parameters</u> to include new parameter LR MANIFEST DEFLT CREATE.</p></li>
<li><p>Added the new parameter to the list in Section <u>5.2.2.</u></p></li>
<li><p>Updated <u>Figure 19. Package Level Parameter Edit [LR7O PAR PKG].</u></p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/2018</td>
<td>2.7</td>
<td><p>Changes for patch LR*5.2*495. The change affects how the SNOMED CT update for files 61, 61.2, and 62 is sent to the receiving facilities.</p>
<ul>
<li><p>Updated the title page.</p></li>
<li><p>Modified Section 4.1.2.</p></li>
<li><p>Modified Section 5.3.20, Figure 41. Load SNOMED SCT Mapping [LA7S LOAD MAPPING SCT]<u>.</u></p></li>
</ul></td>
<td><p>Mantech Mission, Solutions and Services</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>8/15/13</td>
<td>2.6</td>
<td><p>Sr. VA Leadership decision was made on 8/8/13 to remove the AP Results from the LEDI IV Update Patch, due to regulatory concerns.</p>
<p>Added a note to the Introduction section indicating that the AP Results would not be available in the LEDI IV Update Patch.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/29/13</td>
<td>2.5</td>
<td><p>Added input from CLIN 4:</p>
<ul>
<li><p><strong><u>Section 1.1.3:</u></strong></p></li>
</ul>
<p>Clarified the VA to DoD interface overview,</p>
<ul>
<li><p><strong><u>Section 2.2.1, Step 5:</u></strong></p></li>
</ul>
<p>Added two notes on the HL7 interface,</p>
<ul>
<li><p><strong><u>Section 2.2.2:</u></strong></p></li>
</ul>
<p>Modified steps 1-8 under LIM responsibilities,</p>
<ul>
<li><p><strong><u>Section 4.1.2, point 1:</u></strong></p></li>
</ul>
<p>Clarified SNOMED set ups,</p>
<ul>
<li><p><strong><u>Section 4.1.2, Note #3:</u></strong></p></li>
</ul>
<p>Provided more detail on the SNOMED CT</p>
<p>process,</p>
<ul>
<li><p><strong><u>Section 4.2.1, Reference B., Appendix B.</u></strong></p></li>
</ul>
<p>Added new reference “How Notifications</p>
<p>Work”.</p>
<ul>
<li><p><strong><u>Section 4.7.1, Figure 5:</u></strong></p></li>
</ul>
<p>Replaced “Enter/Edit Update Signature</p>
<p>Code with the “Person Class Edit Option”</p>
<p>screen,</p>
<ul>
<li><p><strong><u>Section 4.7.1, Figure 9:</u></strong></p></li>
</ul>
<p>Added examples of the use of a bar code UID with an AP Host and Collection facility,</p>
<ul>
<li><p><strong><u>Section 4.7.2, Figure 17:</u></strong></p></li>
</ul>
<p>Added note that the Techs may view an interim report verified using EA,</p>
<ul>
<li><p><strong><u>Section 5.2.1, Table 2:</u></strong></p></li>
</ul>
<p>Parameter Precedence Order: Modified logic for the method of assigning the AP Accession number,</p>
<ul>
<li><p><strong><u>Section 5.3.2: Manage MI/AP Test Mappings</u></strong></p></li>
</ul>
<p>Added example to the screen of when the mapping needs to be performed.</p>
<ul>
<li><p><strong><u>Section 5.4.13:</u></strong></p></li>
</ul>
<p>Designation of Performing Laboratory –added that a site requiring a performing Laboratory other than the default local Institution Name, must have that performing lab listed in File # 4.</p>
<ul>
<li><p><strong><u>Section 5.4.21:</u></strong></p></li>
</ul>
<p>On the Print Log Book, added example of selecting by UID and provided a more clear example of how the users can select by Accession number,</p>
<ul>
<li><p><strong><u>Glossary:</u></strong></p></li>
</ul>
<p>Updated the definitions of SNOMED CT and VDL.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/24/13</td>
<td>2.4</td>
<td><p>Input from CLIN 4 personnel includes:</p>
<p>Replacing the “MD” and “D.O.” abbreviations with updated PERSON CLASS names for e-signatures in Section 4.7.1,</p>
<p>Updating Enter/Edit File Entry – Update Signature Code screen</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/16/13</td>
<td>2.3</td>
<td><p>Made numerous revisions to make document more 508 compliant as follows:</p>
<p>Added “Editor Notes” to allow the visually impaired to see special hints and tips on the screen captures.</p>
<p>Added screen tips at the web links identified as warning markers by the 508 Compliance Checker. These screen tips allow the reader to see where the hyperlink will take them.</p>
<p>Ensured there were bookmarks at the left top corner of each table.</p>
<p>Took minus symbols out of the table of contents.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>4/22/13</td>
<td>2.2</td>
<td><p>Revisions to the LEDI IV User Manual that now includes the LEDI IV Update patch. This version will be used by the field test sites for the LEDI IV Update patch (LR*5.2*427/LA*5.2*80).</p>
<p>The Changes for the Update patch are listed below and are hyperlinked at the section numbers:</p>
<p><strong><u>Section 1.1:</u></strong></p>
<p>Added detail on the AP/MICRO Interface that now allows data interchange between VA, DoD and Commercial Reference Labs.</p>
<p><strong><u>Section 2.2.1:</u></strong></p>
<p>Added a step for the IRM to schedule the check of the SNOMED CT Mappings Against the Lexicon every two weeks.</p>
<p><strong><u>Section 4.1.2:</u></strong></p>
<p>Added in the <strong>LIM</strong> instructions for updating the SNOMED CT codes at a lab site. Also, Enable editing of the NAME (.01) fields in files 61, 61.2 and 62.</p>
<p>Last, added the message that displays to the Lab site when the SNOMED CT update sent by STS does not match the mappings done by the lab. The description of the code change is included.</p>
<p><strong><u>Section 4.2.2:</u></strong></p>
<p>Added method by which the LIMs can add 3 critical fields to a Stub Report on a MICRO organism result sent back by the Performing Site.</p>
<p><strong><u>Section 4.4.1:</u></strong></p>
<p>Modified AP reports to display the new acronym for Joint Pathology Center (JPC).</p>
<p><strong><u>Section 4.4.2:</u></strong></p>
<p>Listing of features added for the addition of Anatomic Pathology (AP) Orders and Results.</p>
<p><strong><u>Section 4.7.1 and 4.7.2, Figures 5 - 19:</u></strong></p>
<p>Enable AP/MICRO interface. Added signature update feature. Re-added functionality for AP/MICRO interface functionality that had been removed from the User Manual. The assumption that “LSRP” will be taking over AP/MICRO communications is no longer valid.</p>
<p><strong><u>Section 5.2.1 and 5.2.2:</u></strong></p>
<p>Added new Parameter “Method of Assigning AP Accession Number” to the Parameter lists as well as to Figure # 21.</p>
<p><strong><u>Section 5.2.3:</u></strong></p>
<p>Specified a setting of 132 on the Lab Parameters print report. This setting prevents line wrapping from occurring.</p>
<p><strong><u>Section 5.3.24:</u></strong></p>
<p>Added in new option to 'Check SNOMED CT Mappings Against the Lexicon'</p>
<p><strong><u>Section 5.4.12:</u></strong></p>
<p>Method of Assigning AP Accession Number parameter. Modified the way AP Accession Numbers are defaulted.</p>
<p><strong><u>Section 5.5.9:</u></strong></p>
<p>Move Pathologist signature on AP &amp; MICRO e-reports. See revised AP/MICRO e-report.</p>
<p><strong><u>Glossary Section:</u></strong></p>
<p>Corrected the definition of eGFR. The option [LRUCHGDIV] used by LIMs to change divisions (to assist with troubleshooting, data entry, information lookup, etc.) was deactivated with patches LA*5.2*74/LR*5.2*350. It is noted in this User Manual update Table of Contents for the first time.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/17/12</td>
<td>2.1</td>
<td><ul>
<li><blockquote>
<p>Added a reference to the Install Guide for the manual running of File 63 Remediation,</p>
</blockquote></li>
<li><blockquote>
<p>Added descriptive text by the screens that have “dialogue bubbles” to ensure 508 compliance.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/14/12</td>
<td>2.0</td>
<td><ul>
<li><blockquote>
<p>Added the words “Lab System” to the end of the page 1 Introduction sentence that describes the Future of Lab. Clerical fix only.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/10/12</td>
<td>2.0</td>
<td><ul>
<li><blockquote>
<p>Added a reference to the LEDI IV FAQs</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/05/12</td>
<td>1.9</td>
<td><ul>
<li><blockquote>
<p>Added a hyperlink that takes the reader directly to the LEDI IV Install Guide.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/04/12</td>
<td>1.8</td>
<td><ul>
<li><blockquote>
<p>Removed certain references to “Lab System” and replaced it with future LEDI patch since the AP/MICRO and LOINC features will be in a future LEDI patch.</p>
</blockquote></li>
<li><blockquote>
<p>Removed all references to LSRP and replaced it with “Lab System”.</p>
</blockquote></li>
<li><blockquote>
<p>Replaced the LSRP on the screen shots with LEDI.</p>
</blockquote></li>
<li><blockquote>
<p>Input from CLIN 4.</p>
</blockquote></li>
<li><blockquote>
<p>Copied over more detailed steps for the IRM and LIM to follow from the Install Guide (Section 2.2),</p>
</blockquote></li>
<li><blockquote>
<p>Reformatted Section 3.3 and reduced the white space in the screen shots, (Non-content changes.)</p>
</blockquote></li>
<li><blockquote>
<p>Reformatted the File 63 Remediation section to make the bullets consistent.</p>
</blockquote></li>
<li><blockquote>
<p>Modified User Manual to match CLIN 4 comments on the Installation Guide. That is, replaced several “Laboratory System” references with “Future LEDI patch” since there will be another LEDI patch that will include AP/MICRO prior to the implementation of the Laboratory System.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/23/12</td>
<td>1.7</td>
<td><ul>
<li><blockquote>
<p>Updates from the LEDI IV, Implementation team and CLIN 4 users’ review.</p>
</blockquote></li>
<li><blockquote>
<p>Updated File 63 Remediation section to reflect that when the Lab personnel run the remediation tool manually, the tool will repair the errors that were known at the time the tool was developed.</p>
</blockquote></li>
<li><blockquote>
<p>Specified that File 63 Remediation errors be handled by local site personnel with VistA Programmer access.</p>
</blockquote></li>
<li><blockquote>
<p>Added that the File 63 Analysis and Reporting process can be manually kicked off by the local site personnel. Also, that the File 63 Remediation errors be cleaned up prior to the site converting to the LSRP COTS system.</p>
</blockquote></li>
<li><blockquote>
<p>Input from Dev on section 5.3.1, 5.4.14 and 5.4.16.</p>
</blockquote></li>
<li><blockquote>
<p>Added in CR00008076. New Sort for ‘CH’ File 63 Remediation report. See section 5.5.</p>
</blockquote></li>
<li><blockquote>
<p>Added that the AP lab alerts are sent to the Primary Care Provider for outpatients.</p>
</blockquote></li>
<li><blockquote>
<p>Modified the File 63 Remediation functionality to reflect changes arising from testing. It now runs monthly, not nightly.</p>
</blockquote></li>
<li><blockquote>
<p>Renamed LR MANIFEST DEFLT ACCESSION from LA to LR. Also removed “7S” in the title.</p>
</blockquote></li>
<li><blockquote>
<p>Removed three duplicate entries from the General Lab Parameters table.</p>
</blockquote></li>
<li><blockquote>
<p>Renamed LR MANIFEST EXC PREV TEST from LA to LR. Also removed “7S” in the title.</p>
</blockquote></li>
<li><blockquote>
<p>Added a new Parameter to the LEDI IV Patch Parameters “Prompt CPRS Alert in CH Result Entry”.</p>
</blockquote></li>
<li><blockquote>
<p>Procedures for the Addition of Mycobacterium Antibiotics to File #62.06, per Field Input.</p>
</blockquote></li>
<li><blockquote>
<p>Added functionality to allow users to edit reference ranges. Now users who have the LRDATA key can enter a tilde (~) at the result prompt to edit units/reference ranges for lab tests.</p>
</blockquote></li>
<li><blockquote>
<p>Added that the SNOMED CT Codes must match between two sites.</p>
</blockquote></li>
<li><blockquote>
<p>Added the setting and sending of three lab result alert types to the Chemistry/Hematology section.</p>
</blockquote></li>
<li><blockquote>
<p>CCR 7961 CLOSED Shipping Manifest allows a site to add/remove tests from an Open or a Closed manifest. No longer from a “Canceled Manifest”.</p>
</blockquote></li>
<li><blockquote>
<p>Modified the File 63 Remediation mail group back to where it was before – the LMI group is notified of File 63 Remediation errors whether in test or in production.</p>
</blockquote></li>
<li><blockquote>
<p>Removed the references to the error messages for the entering of SNOMED CT IDs since they are listed in the Install Guide. Avoids duplication.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/13/12</td>
<td>1.6</td>
<td><ul>
<li><blockquote>
<p>Minor changes to section numbering to bring it up to date. No content changes.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/03/12</td>
<td>1.6</td>
<td><ul>
<li><blockquote>
<p>Updated per Feedback from CLIN 4:</p>
</blockquote></li>
<li><blockquote>
<p>Clarified in section 1.14 that the (CH) subscript is available prior to the LSRP COTS being implemented,</p>
</blockquote></li>
<li><blockquote>
<p>Clarified in the Scope section that the AP/MICRO interface is not enabled in LEDI IV until the release of the LSRP COTS system.</p>
</blockquote></li>
<li><blockquote>
<p>Removed an ambiguous line from section 2 pertaining to the use of LEDI IV.</p>
</blockquote></li>
<li><blockquote>
<p>Removed “For Government Use Only” from the footer since this document will be placed on the VDL.</p>
</blockquote></li>
<li><blockquote>
<p>Clarified that the LRAP VR option will only be used by those sites that have been part of the prior testing,</p>
</blockquote></li>
<li><blockquote>
<p>Clarified that the LA7VPFL option will not be used until a future date. (To support LSRP COTS.)</p>
</blockquote></li>
<li><blockquote>
<p>Clarified that the LA7V 62.47 ADD DOD option will not be used until a future date. (To support LSRP COTS.)</p>
</blockquote></li>
<li><blockquote>
<p>De-identified certain data elements (accession number, street name and patient name) per VHA standards.</p>
</blockquote></li>
<li><blockquote>
<p>Moved and aligned the text clouds with the sentences they pertained to – for 508 compliance.</p>
</blockquote></li>
<li><blockquote>
<p>Met with Internal Development team. Went over additional CLIN 4 comments.</p>
</blockquote></li>
<li><blockquote>
<p>Incorporated Team Input from 3/30 and 4/2 reviews. Also, clarified several points for CLIN 4.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/22/12</td>
<td>1.5</td>
<td><ul>
<li><blockquote>
<p>Minor updates: Added File #64 to two WKLD References.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Removed the second (duplicate) screen shot under the LRAPLG Log-In Anatomy Pathology Log in Section.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/20/12</td>
<td>1.5</td>
<td><p>Tech edit review:</p>
<p>Updated the document to follow the current national documentation standards and styles.</p>
<p>Updated the document for formatting and styles to conform to the LSRP document template.</p>
<p>Added section breaks before each major section/chapter.</p>
<p>Modified document for double-sided printing:</p>
<ul>
<li><p>Added Odd and Even pages.</p></li>
<li><p>Updated Headers and Footers in all sections.</p></li>
<li><p>Made sure all sections end on an even page.</p></li>
<li><p>Fixed all page numbering to be continuous.</p></li>
</ul>
<p>Added a "Figures and Tables" section.</p>
<p>Added an "Orientation" section; copy taken from current LSRP document modified to fit LDSI/LEDI IV.</p>
<p>Moved the "Blood Bank" section into the added "Orientation" section.</p>
<p>Promoted some bulleted items to Heading 3 style and reformatted other lists throughout the document.</p>
<p>Added file names to file number references throughout this document.</p>
<p>Added user entries in boldface and yellow highlights to screen capture figures throughout.</p>
<p>Added captions to all tables and figures throughout.</p>
<p>Corrected/Added organization acronyms and references for first occurrence in each chapter and as needed.</p>
<p>Made minor grammar, punctuation, and spelling updates as needed.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/16/12</td>
<td>1.4</td>
<td><p>Removed the Lexicon note under Section 4.12 – SNOMED CT. It was deemed irrelevant by the developers and STS.</p>
<p>Input from CLIN 4 to the document.</p>
<p>Added Dev Team modifications to the Manual post CLIN 4 Review Meeting.</p>
<p>Added Parameter list, options and screen captures.</p>
<p>Updated how Non-Performed "NP" tests are handled in the New LEDI IV Options section.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/29/12</td>
<td>1.3</td>
<td><p>Included the HDI*1.0*7 patch within the LEDI IV build.</p>
<p>Added the message that displays when the File 63 Remediation tool finds an error after the install or after completing the nightly data dictionary check.</p>
<p>Clarified that the LEDI IV Install Guide covers the Installation and not the configuration, aka Setup of LEDI IV in Section 6.2 below.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/02/12</td>
<td>1.2</td>
<td><p>Removed section on CCR 5519 and placed the setting up of lab names in to the Install manual.</p>
<p>Renamed Document as LEDI IV User Manual.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/27/12</td>
<td>1.1</td>
<td><p>Removed all references to "Cerner", "Pathnet" and "Millennium". Replaced said references with "LSRP COTS". This change will prevent any legal issues from arising since LSRP is not yet fully released to Production.</p>
<p>Removed the LEDI IV interface set-up instructions for both the VistA Host Facility Communicating with LSRP COTS Collecting Facility &amp; the VistA Collecting facility communicating with the LSRP COTS Host facility. The LSRP team will be documenting these steps.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/11/12</td>
<td>1.0</td>
<td>Base line version for ORR, removed Draft.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/09/12</td>
<td>0.16</td>
<td><p>Added details on eGFR per PM direction,</p>
<p>Accepted revision marks from ESE input,</p>
<p>Removed General Lab from Section 4 per Development input,</p>
<p>Updated the first new option for LEDI IV in section 5 with a screen shot. (Ask Performing Lab.)</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/22/11</td>
<td>0.15</td>
<td>Include VA to LSRP COTS set ups toward the end of the manual.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/14/11</td>
<td>0.14</td>
<td>Additional input from DEV: both technical as well as form and style.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/13/11</td>
<td>0.13</td>
<td><p>Combined Impl. Guide with the User Manual due to overlapping instructions.</p>
<p>Updated the CCRs with additional info from Development.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/07/11</td>
<td>0.12</td>
<td>Updates from Dev Team Meeting.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/16/11</td>
<td>0.11</td>
<td><p>Incorporated feedback from team members.</p>
<p>Added the 5 CCRs arising from the Alpha Test.</p>
<p>Removed Glossary Terms that are not used in the software or this manual.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/10/11</td>
<td>0.11</td>
<td>Removed References to LSRP as well as Micro/AP Electronic Ordering and Resulting for Use at the LEDI IV BETA Sites.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/27/2011</td>
<td>0.10</td>
<td>Updated section 2.4.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/1/11</td>
<td>0.9</td>
<td>Updated section 3.1.4.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/18/11</td>
<td>0.8</td>
<td><p>Section 3.1.2 added step 4</p>
<p>Section 2.3 added 2<sup>nd</sup> Bullet.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/18/11</td>
<td>0.7</td>
<td>Added section 2.6</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/17/11</td>
<td>0.6</td>
<td>Updated document content.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/06/11</td>
<td>0.5</td>
<td>Applied LSRP standard template to the guide.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/05/11</td>
<td>0.4</td>
<td>Cleaned up rough tech edit.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/04/11</td>
<td>0.3</td>
<td>Updated document content.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/01/11</td>
<td>0.2</td>
<td>Updates.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/01/11</td>
<td>0.1</td>
<td>Initial document:</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc510169020" class="anchor"></span>Table 1. Precedence of parameters

 

<span id="_Toc510168818" class="anchor"></span>Contents

<span id="_Toc318284260" class="anchor"></span>Figures and Tables

<span id="_Toc318284261" class="anchor"></span>Figures

<span id="_Toc318284262" class="anchor"></span>Tables

[Table 1. Precedence of parameters [9](#_Toc510169020)](#_Toc510169020)

[Table 2. LEDI IV patch parameters [53](#_Ref509818240)](#_Ref509818240)

<span id="_Toc510168822" class="anchor"></span>Orientation

<span id="how_to_use_this_manual" class="anchor"></span>How to Use this Manual

This manual is intended for use in conjunction with the Laboratory Data Sharing and Interoperability (LDSI) Laboratory Electronic Data Interchange IV (LEDI IV). This manual provides instructions for using LEDI IV.

There are two patches that provide an update to the LEDI IV functionality in this User Manual: LR\*5.2\*427 and LA\*5.2\*80. LR\*5.2\*427 and LA\*5.2\*80 consist of both maintenance fixes as well as an enhancement to allow AP/MICRO orders and results to be sent and received electronically. There is also a new set of manual procedures allowing a LIM to update the SNOMED CT codes at a Lab.

<span id="intended_audience" class="anchor"></span>Intended Audience

The intended audience of this manual includes the following stakeholders:

(Primary) Information Resource Management (IRM), system administrators, or other technical staff who are tasked with installation and implementation of LEDI IV related software in all VistA environments.

Laboratory Automated Data Processing Application Coordinators (ADPACS) and Laboratory Information Managers (LIM).

Product Support (PS).

<span id="legal_requirements" class="anchor"></span>Legal Requirements

There are no special legal requirements involved in the use of the LDSI LEDI IV software.

<span id="blood_bank_clearance" class="anchor"></span>Blood Bank Clearance

VistA Blood Bank Software V5.2 Device Product Labeling Statement

VistA Laboratory Package patches LA\*5.2\*74/LR\*5.2\*350 contain changes to software controlled by VHA Directive 2004-053, titled VistA Blood Bank Software.  
  
Changes involve two routines: LRU and LRX.  
  
These changes were reviewed by the VistA Blood Bank Developer and found to have no impact on the VistA Blood Bank Software control functions.

LEDI IV Updates for LA\*5.2\*80/LR\*5.2\*427:

VISTA Laboratory Package patches LA\*5.2\*80/LR\*5.2\*427 contain changes to software controlled by VHA DIRECTIVE 2004-058, titled VISTA BLOOD BANK SOFTWARE. The changes involve four files: LAB CODE MAPPING (#62.47), LA7 MESSAGE PARAMETER (#62.48), COLLECTION SAMPLE (#62) & LAB DATA (#63).

The changes also involve thirteen fields: SEQUENCE (#.001), CONCEPT (#.01), ALTERNATE CONCEPT (#.04), IDENTIFIER (#62.4701,.01), CODING SYSTEM (#62.4701,.02), NATIONAL STANDARD (#62.4701,.05), RELATED ENTRY (#62.4701,2.1), MESSAGE CONFIGURATION (#62.4701,2.2), SEQUENCE (#62.482,.001), VA FILE ENTRY (#62.482,.01), SNOMED CT ID (#62.482,.02) , NAME (#.01) and FUNGUS/YEAST (#63.37,.01).

All of the above changes for LA\*5.2\*80/LR\*5.2\*427 have been reviewed by the VISTA Blood Bank Developer and found to have no impact on the VISTA BLOOD BANK SOFTWARE control functions.

Risk Analysis

Changes made by patches LA\*5.2\*74/LR\*5.2\*350 have no effect on Blood Bank software functionality, therefore Risk is none.

LEDI IV Updates for LA\*5.2\*80/LR\*5.2\*427:

The changes made by patch LA\*5.2\*80/LR\*5.2\*427 have no effect on Blood Bank software functionality, therefore RISK is none.

Effect on Blood Bank Functional Requirements

Patches LA\*5.2\*74/LR\*5.2\*350 do not alter or modify any software design safeguards or safety critical elements functions.

LEDI IV Updates for LA\*5.2\*80/LR\*5.2\*427:

Patches LA\*5.2\*80//LR\*5.2\*427 does not alter or modify any software design safeguards or safety critical elements functions.

Potential Impact on Sites

These patches contain changes to two routines and 0 files identified in Veterans Health Administration (VHA) Directive 2004-053, group B listing. The changes have no effect on Blood Bank functionality or medical device control functions. There is no adverse potential to sites.

LEDI IV Updates for LA\*5.2\*80/LR\*5.2\*427:

These patches contain changes to 0 routines and 2 files identified in Veterans Health Administration (VHA) Directive 2004-058, group B listing. The changes have no effect on Blood Bank functionality or medical device control functions. There is no adverse potential to sites.

Validation Requirements by Option

There are no validation requirements by option for these patches.  
  
Minimal Test Case Scenarios by Option, Inclusive of All Control Functions: There are no test case scenarios for these patches.

LEDI IV Updates for LA\*5.2\*80/LR\*5.2\*427:

There are no validation requirements by option.

<span id="disclaimers" class="anchor"></span>Disclaimers

This manual provides an overall explanation of how to use the LEDI IV software options; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA websites on the Internet and VA Intranet for a general orientation to VistA. For example, go to the Office of Information and Technology (OIT) VistA Development VA Intranet website: http://vista.med.va.gov

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/002.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA. |

<span id="_Ref509818240" class="anchor"></span>Table 2. LEDI IV patch parameters

<span id="documentation_conventions" class="anchor"></span>Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

Table ii. Documentation symbol/term descriptions

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Symbol</td>
<td>Description</td>
</tr>
<tr class="even">
<td>![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/003.png)</td>
<td><p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
<p>In most cases, you will need this information, or at least it will make the installation smoother and more understandable. Please read each note <em>before</em> executing the steps that follow it!</p></td>
</tr>
<tr class="odd">
<td>![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/004.png)</td>
<td><strong>CAUTION, DISCLAIMER, or RECOMMENDATION:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
</tbody>
</table>

Descriptive text is presented in a proportional font (as represented by this font).

Some of these screen dialogue formats below have been modified from their original version.  They have been formatted to fit this document. 

"Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.

- User’s responses to online prompts will be bold yellow typeface.

  (e.g., \<<span class="mark">Enter</span>\>).
- Editor’s comments are displayed in *italics* preceded by the phrase “*Editor Note*”.

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/005.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

Besides established styles and conventions, the following additional text formatting will be used to further highlight or emphasize specific document content:

- Bold Typeface:
  - All computer keys when referenced with a command (e.g., "press Enter" or "click OK").
  - All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
  - All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
  - All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., "Enter the following command: CD xyz").
- Italicized Typeface:
  - Emphasis (e.g., do *not* proceed or you *must* do the following steps).
  - All reference to computer dialogue or screen titles (e.g., "in the *Add Entries* dialogue…").
  - All document or publication titles and references (e.g., "see the *ABC Installation Guide*").

Step-by-Step Instructions—For documentation purposes, explicit step-by-step instructions for repetitive tasks (e.g., "Open a Command-Line prompt") are generally only provided once. For subsequent steps that refer to that same procedure or task, please refer back to the initial step where those instructions were first described.

<span id="navigation" class="anchor"></span>Documentation Navigation

Document Navigation—This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

|                                                   |                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/006.png) | NOTE: This is a one-time setup and will automatically be available in any other Word document once you install it on the Toolbar. |

<span id="_Toc254604881" class="anchor"></span>Definitions, Acronyms, and Abbreviations

All LEDI IV definitions are included in the Glossary section at the end of this manual.

<span id="assumptions_about_the_reader" class="anchor"></span>Assumptions

This manual is written with the assumption that the reader is experienced or familiar with the following:

VistA computing environment:

- Laboratory—VistA M Server software.
  - Blood Bank.
  - Anatomic Pathology.
  - Microbiology.
  - Chemistry.
  - Previous versions of the LEDI software.
- Kernel—VistA M Server software.
- VA FileMan data structures and terminology—VistA M Server software.

Microsoft Windows

M programming language.

<span id="_Toc397138035" class="anchor"></span>Reference Materials

Readers who wish to learn more about LEDI installations should consult the *LEDI IV Installation Guide* available at the following link:

<http://www.va.gov/vdl/application.asp?appid=75>

VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at the following website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Documentation Library (VDL) website: <http://www.va.gov/vdl/>

There is a LEDI IV Frequently Asked Questions (FAQ) Guide available on the LEDI Lab Share Point.

Because LEDI IV is a controlled release, access to the software will be provided to sites on a case-by-case basis depending on the implementation schedule.  However, the VistA documentation can be downloaded from the Product Support (PS) anonymous directories.

Preferred Method download.vista.med.va.gov

|                                                   |                                                                                                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/007.png) | NOTE: This method transmits the files from the first available File Transfer Protocol (FTP) server. |

<span class="mark">REDACTED</span>

The LEDI IV Update patch will be released to all lab sites simultaneously after the LEDI IV phased national rollout is complete.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Communication Interfaces](#communication-interfaces)
    - [VA to VA](#va-to-va)
    - [VA to Commercial Reference Laboratories](#va-to-commercial-reference-laboratories)
    - [VA to Department of Defense (DoD)](#va-to-department-of-defense-dod)
  - [File \#63 Remediation Tool](#file-63-remediation-tool)
- [LEDI IV Requirements](#ledi-iv-requirements)
  - [Messaging Interface Implementation Requirements](#messaging-interface-implementation-requirements)
  - [Staffing Requirements for LEDI IV](#staffing-requirements-for-ledi-iv)
    - [Information Resource Management (IRM) staff is required for software installation, including:](#information-resource-management-irm-staff-is-required-for-software-installation-including)
    - [LIMS staff is needed for any software configurations including:](#lims-staff-is-needed-for-any-software-configurations-including)
  - [Disk Space Requirements](#disk-space-requirements)
  - [Performance/Capacity Impact](#performancecapacity-impact)
  - [Memory Constraints](#memory-constraints)
- [Implementation](#implementation)
  - [LEDI IV Implementation Instructions](#ledi-iv-implementation-instructions)
  - [Parameter Setup Level Descriptions](#parameter-setup-level-descriptions)
  - [Add Existing or Create New Mycobacterium Antibiotic Procedures](#add-existing-or-create-new-mycobacterium-antibiotic-procedures)
    - [Adding Existing Mycobacterium Antibiotics to the Antimicrobial Susceptibility File](#adding-existing-mycobacterium-antibiotics-to-the-antimicrobial-susceptibility-file)
    - [Creating New Mycobacterium Antibiotics](#creating-new-mycobacterium-antibiotics)
- [New Features for LEDI IV](#new-features-for-ledi-iv)
  - [SNOMED CT Functionality](#snomed-ct-functionality)
    - [Data Standardization of SNOMED CT Codes](#data-standardization-of-snomed-ct-codes)
    - [Manual Process for LIMs to Update SNOMED CT Files](#manual-process-for-lims-to-update-snomed-ct-files)
    - [All SNOMED CT Codes are Available in the Lexicon Utility](#all-snomed-ct-codes-are-available-in-the-lexicon-utility)
  - [LEDI IV Microbiology](#ledi-iv-microbiology)
    - [New Methods to Enter and Edit Microbiology Options](#new-methods-to-enter-and-edit-microbiology-options)
    - [Addition of Microbiology (MI) Orders and Results](#addition-of-microbiology-mi-orders-and-results)
  - [LAB CODE MAPPING](#lab-code-mapping)
    - [LAB CODE MAPPING File (#62.47)](#lab-code-mapping-file-6247)
  - [LEDI IV Anatomic Pathology](#ledi-iv-anatomic-pathology)
    - [New Options to Enter and Edit for AP Functionality](#new-options-to-enter-and-edit-for-ap-functionality)
    - [Addition of Anatomic Pathology (AP) Orders and Results](#addition-of-anatomic-pathology-ap-orders-and-results)
  - [LEDI IV LOINC Functionality](#ledi-iv-loinc-functionality)
  - [LEDI IV Chemistry/Hematology (CH)](#ledi-iv-chemistryhematology-ch)
  - [LEDI IV AP/MICRO INTERFACE](#ledi-iv-apmicro-interface)
    - [Orders and Results for Anatomic Pathology (AP) – Update Patch](#orders-and-results-for-anatomic-pathology-ap-update-patch)
    - [Orders and Results for Microbiology (MI) –Update Patch](#orders-and-results-for-microbiology-mi-update-patch)
- [Use of the LEDI IV Software](#use-of-the-ledi-iv-software)
  - [VistA Laboratory New Menus](#vista-laboratory-new-menus)
    - [New Laboratory Menu—Lab Code Mapping File Menu \[LA7V 62.47 MENU\]](#new-laboratory-menulab-code-mapping-file-menu-la7v-6247-menu)
  - [Parameters and Hierarchies with LEDI IV](#parameters-and-hierarchies-with-ledi-iv)
    - [Parameter Precedence Order](#parameter-precedence-order)
    - [Package Level Parameter Edit \[LR70 PAR PKG\]](#package-level-parameter-edit-lr70-par-pkg)
    - [General Lab User Parameters \[LR User Param\]](#general-lab-user-parameters-lr-user-param)
    - [Domain Level Parameter Edit \[LR70 PAR DOMAIN\]](#domain-level-parameter-edit-lr70-par-domain)
  - [New LEDI IV Options](#new-ledi-iv-options)
    - [Edit an Antibiotic \[LRWU7 EDIT\]](#edit-an-antibiotic-lrwu7-edit)
    - [Manage MI/AP Test Mappings \[LRCAPFF\]](#manage-miap-test-mappings-lrcapff)
    - [Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]](#addedit-local-identifier-la7v-6247-local-identifier)
    - [Clone a Message Configuration \[LA7V 62.47 CLONE MSG CONFIG\]](#clone-a-message-configuration-la7v-6247-clone-msg-config)
    - [Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]](#edit-susceptibility-la7v-6247-edit-susc)
    - [Find Identifier \[LA7V 62.47 FIND IDENTIFIER\]](#find-identifier-la7v-6247-find-identifier)
    - [Print by Msg Config \[LA7V 62.47 PRINT BY MSG CONFIG\]](#print-by-msg-config-la7v-6247-print-by-msg-config)
    - [Code/Set Mismatches \[LA7V 62.47 PRINT CS MISMATCHES\]](#codeset-mismatches-la7v-6247-print-cs-mismatches)
    - [Print Local Codes \[LA7V 62.47 PRINT LOCAL\]](#print-local-codes-la7v-6247-print-local)
    - [Print Susceptibilities \[LA7V 62.47 PRINT SUSC\]](#print-susceptibilities-la7v-6247-print-susc)
    - [Error Code Help \[LA7V 62.47 ERROR CODE HELP\]](#error-code-help-la7v-6247-error-code-help)
    - [Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\]](#map-all-susceptibilities-la7v-6247-map-suscs)
    - [Interim report for an accession \[LRRP1\]](#interim-report-for-an-accession-lrrp1)
    - [Move Cumulative Major/Minor Headers \[LRAC MOVE\]](#move-cumulative-majorminor-headers-lrac-move)
    - [AP LEDI Data Entry \[LRAP VR\]](#ap-ledi-data-entry-lrap-vr)
    - [Reprocess Lab HL7 Messages \[LA7 REPROCESS HL7 MESSAGES\]](#reprocess-lab-hl7-messages-la7-reprocess-hl7-messages)
    - [Display SCT Overrides \[LA7S 62.48 PRINT SCT OVERRIDE\]](#display-sct-overrides-la7s-6248-print-sct-override)
    - [Display a Shipping Configuration \[LA7S 62.9 PRINT\]](#display-a-shipping-configuration-la7s-629-print)
    - [Code Usage \[LA7S CODE USAGE\]](#code-usage-la7s-code-usage)
    - [Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\]](#load-snomed-sct-mapping-la7s-load-mapping-sct)
    - [Map Non-VA SNOMED CT codes \[LA7S MAP NON-VA SNOMED CODES\]](#map-non-va-snomed-ct-codes-la7s-map-non-va-snomed-codes)
    - [Print MI/AP Test Mappings \[LA7VPFL\]](#print-miap-test-mappings-la7vpfl)
    - [Initialize DOD Codes \[LA7V 62.47 ADD DOD\]](#initialize-dod-codes-la7v-6247-add-dod)
    - [Check SNOMED CT Mappings Against the Lexicon \[LA7TASK SCT MAPPINGS CHECK\]](#check-snomed-ct-mappings-against-the-lexicon-la7task-sct-mappings-check)
  - [Modified LEDI Options](#modified-ledi-options)
    - [Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\]](#display-lab-universal-interface-message-la7-print-lab-ui-message)
    - [Edit Shipping Configuration \[LA7S EDIT 62.9\]](#edit-shipping-configuration-la7s-edit-629)
    - [Print Shipping Manifest \[LA7S MANIFEST PRINT\]](#print-shipping-manifest-la7s-manifest-print)
    - [Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\]](#print-ledi-pending-orders-la7s-pending-print-ledi)
    - [Enter/verify/modify data (manual) \[LRENTER\]](#enterverifymodify-data-manual-lrenter)
    - [Referral Patient Multi-purpose Accession \[LRLEDI\]](#referral-patient-multi-purpose-accession-lrledi)
    - [Fast Bypass Data Entry/Verify \[LRFASTS\]](#fast-bypass-data-entryverify-lrfasts)
    - [Bypass normal data entry \[LRFAST\]](#bypass-normal-data-entry-lrfast)
    - [Results entry (batch) \[LRMISTUF\]](#results-entry-batch-lrmistuf)
    - [Microbiology Results Entry \[LRMIEDZ\]](#microbiology-results-entry-lrmiedz)
    - [Enter/verify data (auto instrument) \[LRVR\]](#enterverify-data-auto-instrument-lrvr)
    - [Log-in, anat path \[LRAPLG\]](#log-in-anat-path-lraplg)
    - [Anatomic Pathology Performing Laboratory](#anatomic-pathology-performing-laboratory)
    - [Add tests to a given accession \[LRADD TO ACC\]](#add-tests-to-a-given-accession-lradd-to-acc)
    - [Add a New Internal Name for an Antibiotic \[LRWU7\]](#add-a-new-internal-name-for-an-antibiotic-lrwu7)
    - [Delete entire order or individual tests \[LRCENDEL\]](#delete-entire-order-or-individual-tests-lrcendel)
    - [Microbiology Performing Laboratory](#microbiology-performing-laboratory)
    - [Microbiology Sending an Alert](#microbiology-sending-an-alert)
    - [The Add/Remove a Shipping Manifest Test’ \[LA7S MANIFEST TEST ADD/REMOVE\]](#the-addremove-a-shipping-manifest-test-la7s-manifest-test-addremove)
    - [Enter/verify/modify data (manual) \[LRENTER\]](#enterverifymodify-data-manual-lrenter-1)
    - [Print log book \[LRAPBK\]](#print-log-book-lrapbk)
    - [Change How Not-Performed ("NP") Tests Work in LEDI IV](#change-how-not-performed-np-tests-work-in-ledi-iv)
    - [Cumulative Report Modifications](#cumulative-report-modifications)
  - [Modified Report Options](#modified-report-options)
    - [Interim report by provider \[LRRD\]](#interim-report-by-provider-lrrd)
    - [Interim report for chosen tests \[LRRP3\]](#interim-report-for-chosen-tests-lrrp3)
    - [Interim report for selected tests as ordered \[LRRSP\]](#interim-report-for-selected-tests-as-ordered-lrrsp)
    - [Interim reports by location (manual queue) \[LRRS\]](#interim-reports-by-location-manual-queue-lrrs)
    - [Interim reports for 1 location (manual queue) \[LRRS BY LOC\]](#interim-reports-for-1-location-manual-queue-lrrs-by-loc)
    - [Interim reports for 1 provider (manual queue) \[LRRD BY MD\]](#interim-reports-for-1-provider-manual-queue-lrrd-by-md)
    - [File 63 Remediation Results MailMan Message for ‘CH’](#file-63-remediation-results-mailman-message-for-ch)
    - [File 63 Remediation Results MailMan Message for ‘Micro’](#file-63-remediation-results-mailman-message-for-micro)
    - [Modify AP& MICRO Report for Pathologist’s Signature](#modify-ap-micro-report-for-pathologists-signature)
Laboratory Electronic Data Interchange (LEDI) IV update software introduces enhancements to the bi-directional interface that allows Department of Veterans Affairs (VA) laboratories to communicate with other VA facilities, Commercial Reference Laboratories and DoD. The LEDI IV update software has the capacity and features necessary for sharing secure, encrypted data between the VA and DoD facilities.
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/008.png) | NOTE: The LEDI IV Update patch is enabling the micro interface for orders and results, as well as the AP orders interface.  However, the sending of AP results from VA Host Labs to other VA Labs, DoD Labs and Commercial Reference Labs will still be disabled.  The AP Host Labs will continue to use their existing processes to return the resulted sample to the Collecting Labs. |
The purpose of this Manual is two-fold:
Serve as the user manual.
Provide instructions to implement Laboratory Electronic Data Interchange version IV (LEDI IV) after installing the software.
The software has the capacity and features necessary for sharing secure, encrypted laboratory data between:
VA to VA.
VA to Commercial Reference Laboratories.
VA to Department of Defense (DoD).
The LEDI IV and LEDI IV update software are extensions of the LEDI III software. The software includes this new functionality:
SNOMED CT Mapping (collection samples, etiology, topography).
AP Orderable configuration.
Adding and editing antimicrobials & drugs.
File 63 Remediation.
New Parameters.
Recording of the performing laboratory for AP and Micro.
The LEDI IV update software patch allows AP/MICRO electronic ordering and resulting.
Intended Users
The intended users of LEDI IV include the laboratory personnel of the VA Medical Centers.

## Communication Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA to VA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV Update software enhances the general LEDI IV functionality. LEDI IV Update software enhances the current LEDI IV functionality.

It supports the sending and receiving of Microbiology and Anatomic Pathology (AP) orders and results between the associated Veterans Health Information Systems and Technology Architecture (VistA) Lab database and other VAs.

### VA to Commercial Reference Laboratories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV Update software enhances the general LEDI IV functionality. It adds the capability of transferring AP and Micro orders to commercial reference laboratories and the receipt of AP and Micro results from those laboratories

### VA to Department of Defense (DoD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV Update software enhances LEDI IV functionality. It supports the sending and receiving of Microbiology and Anatomic Pathology (AP) orders and results between the associated Veterans Health Information Systems and Technology Architecture (VistA) Lab database and DoD labs.

## File \#63 Remediation Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI IV software creates a tool to check the LAB DATA File (#63) for data dictionary issues.

Checks for the following issues:

- Errors that might have occurred when an antibiotic was added by the local site to the ORGANISM sub-field (#63.3) of the LAB DATA file (#63).
- Errors with data names in the LABORATORY TEST file (#60), for tests in the Clinical Chemistry (Chemistry and Hematology) section. It checks the CHEM, HEM, TOX, RIA, SER, etc. sub-file (#63.04) of the LAB DATA file (#63) looking for possible discrepancies in the data dictionary.
- File Remediation runs on three occasions:
  - Automatically during install in Analyze and Report mode.
  - Runs automatically once each month as part of the LR NIGHTY task in analyze mode after the successful installation of LEDI IV.
  - Manually under the direction of a LAB SME. See Install Guide for details.
- For errors in a Production (or test) database, the system generates an email message and sends it to the LMI Mail Group.
- For the remaining (unrepaired) File 63 issues, the site should then log a Remedy ticket and not try to fix the error(s) on its own.

The error message that displays to the users after the LR NIGHTY run, reads as follows:

"Contact the National Service Desk to request assistance from the Clin 4 Product Support team in resolving the following errors identified in the VistA Laboratory package:"

If you see this message, enter a Help Desk ticket or have the National Service Desk enter a ticket for you. CLIN 4 personnel will assist the site in correcting the reported errors.

> **NOTE:** It is very important to analyze and fix the critical errors to ensure accurate lab results.

# LEDI IV Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Messaging Interface Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation of the Laboratory Electronic Data Interchange (LEDI) IV Health Level Seven (HL7) messaging interface between VA to VA and VA to external reference laboratories consists of three parts:

VA to VA:

- Veterans Health Information Systems and Technology Architecture (VistA) Laboratory LEDI IV software.
- VistA HL7 application software.

VA to Commercial Reference Laboratory:

- VistA Laboratory LEDI IV software.
- VistA HL7 application software.
- Commercial Reference Laboratory non-VA information system capable of sending and receiving Laboratory HL7 order and result messages (i.e., LabCorp, Quest).

VA to Department of Defense (DoD):

- VistA Laboratory LEDI IV software.
- VistA HL7 application software.
- Vitria Interface Engine.

## Staffing Requirements for LEDI IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resource Management (IRM) staff is required for software installation, including:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Installing the LEDI IV bundle (HDI\*1.0\*7, LA\*5.2\*74 and LR\*5.2\*350), as well as the LEDI IV Update patches which include LR\*5.2\*427 and LA\*5.2\*80.
2.  Establishing mail groups and menu assignments.
3.  Loading the SNOMED CT mapping file, including updates sent by STS.
1.  Scheduling the Check SNOMED CT Mappings Against the Lexicon \[LA7TASK SCT MAPPINGS CHECK\] option to run every two weeks.
2.  If setting up VA to non-VA (DoD or commercial reference lab) then complete HL LOGICAL LINK file (#870) setup for LA7V xxx client logical link created by LEDI Setup option.  
      
    Note a: If this link has been created/setup for a previous existing interface then no action is required.  
      
    Note b: If VA to VA, then no action is required as the interface uses existing VAxxx logical links already established and configured.
3.  If an electronic link (HL7 interface) is used for Micro and/or AP, edit the Lab Messaging Link field (#.07) to link the shipping configuration to the HL7 interface.
4.  If an electronic link (HL7 interface) is used for Micro and/or AP, link, local Antimicrobial Susceptibility to the result codes used by the reference laboratory to report antibiotic susceptibilities.
5.  Map the LEDI Micro and AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] which establishes the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests.

### LIMS staff is needed for any software configurations including:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Setting up the File \#62 AP Collection Sample and File \#60 Test(s).
2.  Adding existing mycobacterium drugs to the Antimicrobial Susceptibility File \#62.06.
3.  Editing Package level Parameters if needed using the Package Level Parameter Edit \[LR7O PAR PKG\] option.
4.  Setting up the Lab Shipping Files for Micro and AP using the options on the Lab Shipping Management Menu \[LA7S MGR MENU\].
5.  If using the HL7 TCP/IP communication protocol for Micro and/or AP, complete the HL LOGICAL LINK file (#870) setup.
6.  If an electronic link (HL7 interface) is used for Micro and/or AP, edit the Lab Messaging Link field (#.07) to link the shipping configuration to the HL7 interface.
7.  If an electronic link (HL7 interface) is used for Micro and/or AP, the LIM should use the CFE option by selecting Edit Shipping Configuration \[LA7S EDIT 62.9\] (CFE) and then LAB MESSAGING LINK.
8.  Map the LEDI Micro and AP tests using menu option National Laboratory File \[LR70 60-64\]. Then select National Laboratory File \<NAME OF ACCOUNT\> Option. Manage MI/AP Test Mappings’ \[LRCAPFF\]. This establishes the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests.

The LEDI IV installation process *must* be performed in the sequence specified in the Veterans Health Information Systems and Technology Architecture (VistA) *LEDI IV Installation Guide.*

## Disk Space Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A 5-15% increase in disk space can be expected in the ^LR and ^LRO globals due to new fields. This 5-15% increase includes the AP data entered into the LAB ORDER ENTRY file (#69).

## Performance/Capacity Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performance estimates and capacity measures are difficult to obtain, because LEDI IV software has components in several applications. It is estimated that LAB SERVICE and AUTOMATED LAB INSTRUMENTS applications may impact the system by requiring more Central Processing Unit (CPU) cycles.

## Memory Constraints 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No memory constraints are associated with the release of the LEDI IV software.

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## LEDI IV Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Information Managers (LIMs) should refer to the Laboratory Electronic Data Interchange (LEDI) III implementation and user guides in the VA Software Document Library (VDL) for setting up the following LEDI interface types for CH subscript tests:

VA to VA—Host and Collection as well as Intra Division.

VA to Commercial Reference Labs—Collection.

VA to DOD Labs—Host and Collection.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/009.png)</td>
<td><p><strong>REF:</strong> The LIMs should follow the detailed setup instructions in the LEDI III Implementation Guide (patches LA*5.2*64/LR*5.2*286) at this link:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appid=75">http://www.va.gov/vdl/application.asp?appid=75</a></p>
<p>Users <em>must</em> also follow the LEDI IV configuration steps in the "Use of the LEDI IV Software" section in this manual. The AP/MICRO interface configuration processes are described in the AP/MICRO Configuration document.</p></td>
</tr>
<tr class="even">
<td>![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/010.png)</td>
<td><strong>NOTE:</strong> To assist with training end users, review this manual.</td>
</tr>
</tbody>
</table>

## Parameter Setup Level Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the three precedence levels that the user can use to set the parameter (listed in order of precedence):

1.  User
1.  Division
2.  Package

For example, if a site sets the "Ask Performing Lab Micro" parameter to "NO" on the division level, but a specific user sets that parameter to "YES" on the User level, then all users in the division will *not* get prompted for a performing lab, except the user who sets it to "YES".

The Lab User parameters only control what an *individual* user sees. Each parameter can have different precedence levels defined.

| Parameter | Level/Precedence | File              |
|-----------|------------------|-------------------|
| USR       | User             | NEW PERSON (#200) |
| DIV       | Division         | INSTITUTION (#4)  |
| PKG       | Package          | PACKAGE (#9.4)    |

For example, the "EGFR Patient's Age Cutoff" parameter is only configurable at the Package and Division levels. The Division level takes precedence over the Package level.

See Section 5.2 for more details on the LEDI IV Parameters.

## Add Existing or Create New Mycobacterium Antibiotic Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV changes the way Mycobacterium Antibiotics are handled. Mycobacterium Antibiotics are handled similar to Bacterial Antibiotics, and need to have an entry in the Antimicrobial Susceptibility File (#62.06).

### Adding Existing Mycobacterium Antibiotics to the Antimicrobial Susceptibility File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add existing Mycobacterium Antibiotics (that were created pre-LEDI IV) to the Antimicrobial Susceptibility File (#62.06), use the option ‘Edit an Antibiotic’ \[LRWU7 EDIT\]. However, first you will need a listing of your current Mycobacterium Antibiotics. There are two methods to obtain a listing of Mycobacterium Antibiotics that exist in the Lab Data File (#63). The first method requires FileMan Data Dictionary access to the Lab Data File (#63); the other method requires access to the option ‘Outline for one or more files’ \[LRUFILE\] under the ‘Lab liaison menu’ \[LRLIAISON\]. For both methods, it’s easiest if the output is captured in a text file, and then the user can search for ‘63.39’; the existing Mycobacterium Antibiotics will be displayed a few lines under ‘63.39’.

> **NOTE:** To capture or log the session for a text file, the LIM should follow the specific documentation of the Terminal Emulator that they use.

Method 1: Using the FileMan ‘Data Dictionary Utilities’ menu \[DI DDU\], select the option ‘List File Attributes’ \[DILIST\]. Enter ‘63’ for the ‘Start with what’ and ‘Go to what’ File, and then enter ‘Microbiology’ for the ‘Sub-File’.

(Note: The output below has been shortened; some text has been replaced with ‘…’)

<span id="_Toc510168942" class="anchor"></span>Figure 1. List File Attributes for File \#63 from Data Dictionary

VA FileMan 22.0

Select OPTION: <span class="mark">8\<ENTER\></span> DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: <span class="mark">LIST FILE ATTRIBUTES\<ENTER\></span>

START WITH WHAT FILE: LAB DATA// <span class="mark">\<ENTER\></span>

GO TO WHAT FILE: LAB DATA// <span class="mark">\<ENTER\></span>

Select SUB-FILE: <span class="mark">MICROBIOLOGY\<ENTER\></span>

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// <span class="mark">GLOBAL MAP\<ENTER\></span>

DEVICE: 0;80;999<span class="mark">\<ENTER\></span> VIRTUAL TELNET

GLOBAL MAP DATA DICTIONARY \#63.05 -- MICROBIOLOGY SUB-FILE

APR 30,2012@09:12:33 PAGE 1

STORED IN ^LR(D0,"MI", SITE: MHC DEVELOPMENT ACCOUNT UCI: MHCVSS,MHCVSS

-------------------------------------------------------------------------------

This is microbiology data associated with this patient.

CROSS

REFERENCED BY: MYCOBACTERIUM(AC), FUNGUS/YEAST(AD), PARASITE(AE), VIRUS(AF)

^LR(D0,"MI",D1,0)= (#.01) DATE/TIME SPECIMEN TAKEN \[1D\] ^ (#.02) DATE/TIME

==\>OBTAINED INEXACT \[2S\] ^ (#.03) DATE REPORT COMPLETED \[3D\]

==\>^ (#.04) VERIFY PERSON \[4P:200\] ^ (#.05) SITE/SPECIMEN

==\>\[5P:61\] ^ (#.06) MICROBIOLOGY ACCESSION \[6F\] ^ (#.07)

==\>PHYSICIAN \[7P:200\] ^ (#.08) WARD \[8F\] ^ (#.09) AMENDED

==\>REPORT \[9S\] ^ (#.1) DATE/TIME RECEIVED \[10D\] ^ (#.055)

==\>COLLECTION SAMPLE \[11P:62\] ^ (#.2) RESULTS ENTRY DATE

==\>\[12D\] ^ (#.111) REQUESTING LOC/DIV \[13V\] ^ (#.112)

==\>ACCESSIONING INSTITUTION \[14P:4\] ^

...

^LR(D0,"MI",D1,12,0)=^63.39PA^^ (#26) MYCOBACTERIUM

^LR(D0,"MI",D1,12,D2,0)= (#.01) MYCOBACTERIUM \[1P:61.2\] ^ (#1) QUANTITY \[2F\]

==\>^

^LR(D0,"MI",D1,12,D2,.1)= (#.1) ISOLATE ID \[1F\] ^

^LR(D0,"MI",D1,12,D2,1,0)=^63.4A^^ (#2) COMMENT

^LR(D0,"MI",D1,12,D2,1,D3,0)= (#.01) COMMENT \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0001)= (#5) STR \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0002)= (#10) PAS \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0003)= (#15) INH \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0004)= (#20) ETH \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0005)= (#25) RIF \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0006)= (#30) KANAMYCIN \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0007)= (#35) CAPREOMYCIN \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0008)= (#40) CYCLOSERINE \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0009)= (#45) ETHIONAMIDE \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.001)= (#50) PYRAZINAMIDE \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.0011)= (#55) MIOMYCIN \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.00170001)= (#2.00170001) NEWBIOTIC \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.00522001)= (#2.00522001) TEST2 \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.00522002)= (#2.00522002) TEST \[1F\] ^

^LR(D0,"MI",D1,12,D2,2.00636002)= (#65) STREPTOMYCIN 10.0 \[1F\] ^

^LR(D0,"MI",D1,13,0)=^63.41A^^ (#27) TB RPT REMARK

^LR(D0,"MI",D1,13,D2,0)= (#.01) TB RPT REMARK \[1F\] ^

...

Method 2: Alternatively, the option ‘Outline for one or more files’ \[LRUFILE\] under the ‘Lab liaison menu’ \[LRLIAISON\] can be used. When prompted to select a File, enter ‘63’.

(Note: The output below has been shortened; some text has been replaced with ‘…’)

<span id="_Toc510168943" class="anchor"></span>Figure 2. List File Attributes from \[LRUFILE\]

Select Lab liaison menu Option: Outline for one or more files <span class="mark">\<ENTER\></span>

Select FILE: <span class="mark">63 \<ENTER\></span> LAB DATA

Select FILE:

Brief listing: <span class="mark">? YES//</span> <span class="mark">\<ENTER\></span> (YES)

DEVICE: HOME// <span class="mark">0;80;99999 \<ENTER\></span> VIRTUAL TELNET

Apr 30, 2012 LAB DATA (63) Pg 1

-------------------------------------------------------------------------------

.01 LRDFN

.02 PARENT FILE

.03 NAME

.04 DO NOT TRANSFUSE

.05 ABO GROUP

.06 RH TYPE

...

22 TB RPT DATE APPROVED

22.1 TB RE DATE

23 TB RPT STATUS

24 ACID FAST STAIN

25 QUANTITY

25.5 TB ENTERING PERSON

26 MYCOBACTERIUM (Subfile 63.39)

.001 ISOLATE NUMBER

.01 MYCOBACTERIUM

.1 ISOLATE ID

1 QUANTITY

2 COMMENT (Subfile 63.4)

.01 COMMENT

2.00170001 NEWBIOTIC

2.00522001 TEST2

2.00522002 TEST

5 STR

10 PAS

15 INH

20 ETH

25 RIF

30 KANAMYCIN

35 CAPREOMYCIN

40 CYCLOSERINE

45 ETHIONAMIDE

50 PYRAZINAMIDE

55 MIOMYCIN

65 STREPTOMYCIN 10.0

26.4 TB TEST(S) (Subfile 63.181)

.01 TB TEST(S)

Once you have the list of existing Mycobacterium Antibiotics setup in the Lab Data File (#63), use the option ‘Edit an Antibiotic’ \[LRWU7 EDIT\] to add the desired Mycobacterium Antibiotics to the Antimicrobial Susceptibility File (#62.06).

> **NOTE:** For Mycobacterium Antibiotics, <u>do not</u> enter anything for the ‘ANTIMICROBIAL SUSCEPTIBILITY INTERNAL NAME’ prompt.

For the ‘AFB INTERNAL NAME’ prompt, the name must be entered exactly as seen in the Lab Data File (#63).

<span id="_Toc510168944" class="anchor"></span>Figure 3. Antibiotic’ Using the Edit an Antibiotic \[LRWU7 EDIT\] Option

Select Lab liaison menu Option: <span class="mark">ANTE\<ENTER\></span> Edit an Antibiotic

Select one of the following:

1 Bacterial Antibiotic

2 Mycobacterium Antibiotic

Select Antibiotic Type to Edit: 1// <span class="mark">2\<ENTER\></span> Mycobacterium Antibiotic

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: STREPTOMYCIN 10.0 <span class="mark">\<ENTER\></span>

Are you adding 'STREPTOMYCIN 10.0' as

a new ANTIMICROBIAL SUSCEPTIBILITY? No// <span class="mark">Y\<ENTER\></span> (Yes)

ANTIMICROBIAL SUSCEPTIBILITY NUMBER: 111// <span class="mark">\<ENTER\></span>

ANTIMICROBIAL SUSCEPTIBILITY INTERNAL NAME: <span class="mark">\<ENTER\></span> *Editor Note: For Mycobacterium Antibiotics, do not enter anything for this prompt.*

NAME: STREPTOMYCIN 10.0// <span class="mark">\<ENTER\></span>

AFB INTERNAL NAME: STREPTOMYCIN 10.0 <span class="mark">\<ENTER\></span> *Editor Note: This is the Field Name or Number from File \#63 (Subfile \#63.39).*

NATIONAL VA LAB CODE: STREPTOMYCIN 10 UG/ML AFB SUSC <span class="mark">\<ENTER\></span> 93690.0000 *Editor Note: Map the entry to an NLT Code.*

Select Lab liaison menu Option:

Note 1: For the ANTIMICROBIAL SUSCEPTIBILITY INTERNAL NAME: prompt do not enter anything for Mycobacterium Antibiotics,

Note 2: For AFB INTERNAL NAME: STREPTOMYCIN 10.0 prompt, the Field Name or Number is from File \#63 (Subfile \#63.39),

Note 3: At the NATIONAL VA LAB CODE: prompt, map the entry to the most appropriate and specific NLT Code, including the drug concentration in the procedure name when available.

### Creating New Mycobacterium Antibiotics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV also changes the method used for creating new Mycobacterium Antibiotics; it is now similar to how Bacterial Antibiotics are created. When creating new Mycobacterium Antibiotics (that did not exist pre-LEDI IV), you do not need to go into FileMan any more to add the new Drug Node. Instead, you use the option ‘Add a new internal name for an antibiotic’ \[LRWU7\]. This option now allows a user to create a new Mycobacterium Antibiotic; the option will automatically add the new drug to the Lab Data File (#63, Subfile \#63.39), as well as create a new entry in the Antimicrobial Susceptibility File (#62.06).

This option should only be used when creating new Mycobacterium Drugs that never existed before ((both in the Lab Data File (#63) and the Antimicrobial Susceptibility File (#62.06)). However, for Mycobacterium Drugs whose drug nodes already existed in the Lab Data File (#63), but now need to be added to the Antimicrobial Susceptibility File (#62.06), the option ‘Edit an Antibiotic’ \[LRWU7 EDIT\] should be used instead.

<span id="_Toc510168945" class="anchor"></span>Figure 4. Create New Mycobacterium Drugs for Files

Select Lab liaison menu Option: <span class="mark">ANT\<ENTER\></span> Add a new internal name for an antibiotic

Select one of the following:

1 Bacterial Antibiotic

2 Mycobacterium Antibiotic

Select Antibiotic Type to Add: 1// <span class="mark">2\<ENTER\></span> Mycobacterium Antibiotic

Enter the name of the new antibiotic you wish to create: KANAMYCIN 6.0

Checking if field exists...OK

(DRUG NODE will be 2.00500008)

Are you sure you wish to create KANAMYCIN 6.0? NO// <span class="mark">YES \<ENTER\></span>

KANAMYCIN 6.0 has now been created.

You must now add a new antibiotic in the ANTIMICROBIAL SUSCEPTIBILITY file

and use KANAMYCIN 6.0 as the entry for the AFB INTERNAL NAME field.

Do you want to setup KANAMYCIN 6.0 as a new Mycobacterium Antibiotic? NO// <span class="mark">YES \<ENTER\></span>

NAME: KANAMYCIN 6.0// <span class="mark">\<ENTER\></span>

AFB INTERNAL NAME: 2.00500008// <span class="mark">\<ENTER\></span> KANAMYCIN 6.0

NATIONAL VA LAB CODE: Kanamycin 6 ug/mL AFB Susc <span class="mark">\<ENTER\></span> 93697.0000

Select Lab liaison menu Option:

# New Features for LEDI IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory Electronic Data Interchange (LEDI) IV brings new features to the legacy Veterans Health Information Systems and Technology Architecture (VistA) Laboratory version 5.2 software.

## SNOMED CT Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV introduces new functionality for the SNOMED CT codes.

### Data Standardization of SNOMED CT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files will be mapped to SNOMED CT codes:

TOPOGRAPHY FIELD (#61).

ETIOLOGY FIELD (#61.2).

COLLECTION SAMPLE (#62).

In addition, the SNOMED CT codes are standardized for General Lab, Microbiology, and AP data in these files. Standards & Terminology Service (STS) will provide a SNOMED CT Mapping File for each site to load and apply the mappings. See the option Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\] under section 5 below for more information.

### Manual Process for LIMs to Update SNOMED CT Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The manual processes for updating the SNOMED CT files by a LIM are in this section.

- STS will deploy SNOMED CT updates for files 61, 61.2, and 62 via the Lab’s Server side MailMan function to the facilities.
- When the update file has been read in and saved in the LAB MAPPING TRANSPORT File (#95.4) a MailMan message will be sent to the facilities G.LMI group informing them that data has been saved on their system and is ready for processing.
- The LIM will process the mapping update during non-peak times. See detailed process below in the LEDI IV User Manual entitled Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\].
1.  The LIM uses a FileMan inquiry to look at the entries in any of the three monitored files.
2.  VA laboratory LIM creates a new entry to a monitored file. (See list of 3 files under i. below.)
    1.  Each new entry will automatically be assigned a unique NUMBER (IEN).
    2.  Each new entry will be given a NAME.
    3.  Each new entry must be given a SNOMED field.
        1.  Monitored Files that include a SNOMED CT field are the following:
- File 61 – Topography (required field).
- File 61.2 – Etiology (required field).
- File 62 – Collection Sample – Note: Does not have a SNOMED field.

Once the new entry has been completed, a message will be sent to STS, which will contain all the necessary information to provide a SNOMED CT mapping, if applicable.

NOTE 1: To prevent any data transfer errors, the SNOMED CT IDs (SCT IDs) for the specimen and the tests need to match between the collecting and the host sites.

NOTE 2: The NAME field (#.01) in the TOPOGRAPHY FIELD file (#61), COLLECTION SAMPLE file (#62), and ETIOLOGY FIELD file (#61.2) are once again editable with the LEDI IV Update patch.

NOTE 3: When a Systemized Nomenclature of Medicine Clinical Terms (SNOMED CT)

mapping file is loaded, the system validates each SNOMED CT ID against the Lexicon. If there is an exception found (e.g., the code is inactive) the system sends an alert to Standards & Terminology Services (STS) so that STS can send an updated mapping for this entry.

### All SNOMED CT Codes are Available in the Lexicon Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lexicon Utility provides the following functionality:

Legacy VistA Laboratory software can now access SNOMED CT data stored in the Lexicon database.

Provides Application Program Interfaces (APIs) to the legacy VistA Laboratory software to support SNOMED access by all VistA applications.

- VistA Laboratory uses the Lexicon APIs, \$\$CODE^LEXTRAN API, to retrieve SNOMED CT codes and use the established hierarchy to retrieve SNOMED CT codes for organisms.

Provides a mechanism for updating future SNOMED codes.

Provides new reports for mapped and unmapped SNOMED codes available through the VistA Laboratory application.

When the Lexicon Utility receives an unknown term, VistA Laboratory notifies members of the local LAB MAPPING mail group of exception handling instances and sends an exception handling notification to VA Standards and Terminology Services for resolution via an HDI LABXCPT^HDISVAP1 API.

The Laboratory package uses the API for three exceptions/events:

- Errors encountered while loading STS mapped SCT code into the target database.
- Loading new/additional terms received from another system via HL7 messaging.
- New terms entered locally.
- Unknown terms can originate within VA or a clinical partner. The Laboratory package can receive a patient care term (clinical term) that is from a non-VA information system not known to the VA clinical Lexicon.
- The term can be a clinical term stored and displayed in a report to the provider who interprets and/or acts on the term in the report.
- The term can be a valid national term not represented in the Lexicon, due to sequencing or database update lag.
- The term can be a valid clinical term not yet modeled or issued by the national code set provider.
- The term can be a local term originating with the clinical data provider partner that may or may not be included in the national code set.
- When a local lab performs a SNOMED CT update and an Exception error occurs, the Vista Lab application will display a message to the Installer that reads: “Due to a recent Lexicon patch that updated the SNOMED CT (SCT) code set at your facility, some of your Lab entries in files XXXXXXX are mapped to deprecated SCT codes. Standards & Terminology Services (STS) has received notification of these exceptions and will provide you with a new SCT mapping file within several weeks or less. The following SNOMED CT exceptions have been found at XXXXXXX VAMC.”. Where “X” represents either the File \# or the name of the VA Medical Center.

## LEDI IV Microbiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV introduces new enhancements for Microbiology.

### New Methods to Enter and Edit Microbiology Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Antibiotic \[LRWU7 EDIT\], located under the Lab Liaison Menu, allows the LIM to edit an antibiotic rather than going through VA FileMan. This option allows the entry of existing mycobacterial drugs to the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

The modification of the option Add a new internal name for an antibiotic \[LRWU7\] also located under the Lab Liaison Menu, now allows the creation of a new internal name for an antibiotic in LAB DATA file \#63 for mycobacterium drugs. This action needs to be done first before the LRWU7 option is run.

In Microbiology data entry options, the fields xxx RPT DATE APPROVED (e.g., BACT RPT DATE APPROVED, MYCOLOGY RPT DATE APPROVED, etc.) must now contain a date and time entry (i.e., "N" to designate "Now"; "T" can no longer be used).

Within Microbiology result entry options, the user can opt to send one of three alert types to the ordering provider and additional recipients and/or mail groups. Depending on how the parameter is set, will determine whether the user is prompted to send an alert. The three alert types are:

- Lab results available.
- Abnormal lab results.
- Critical lab results.

|                                                   |                                                                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/011.png) | NOTE: The type of alert generated either depends on whether the clinician has set the parameter for personal alerts in CPRS, or if the alert is mandatory at the system level. |
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/012.png) | REF: For additional details on these alerts, see the “APPENDIX B: HOW NOTIFICATIONS WORK - TECHNICAL OVERVIEW” section in the CPRS Technical Manual in the VDL.            |

Under the Microbiology Result entry option, the LIM can designate to:

- Set the performing laboratory for the entire report.
- Set the performing laboratory for specific sections of the report. If choosing to enter the performing laboratory for specific report sections, only those sections that have data entered will appear for selection.

### Addition of Microbiology (MI) Orders and Results 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- New codes are added to the LAB ELECTRONIC CODES file (#64.061) to support messaging via HL7 messaging.
- Additional information is added to the LABORATORY PENDING ORDER file (#69.6) for HL7 messaging.
- HL7 messaging is enhanced to process the following sections:
  - Bacteriology.
  - Mycobacteriology.
  - Mycology.
  - Virology.
  - Parasitology.
- The electronic messaging functionality of the LAB DATA file (#63) is enhanced to handle multiple isolates for any given culture.
- The LEDI software application is enhanced by triggering an event to notify and return results to the *collecting* facility laboratory, once an order is identified as LEDI associated and released.  
  A new API was created to generate the new LEDI messages.

<u>LEDI IV Update Patch:</u>

Should the Host site, using the LEDI IV interface, send back a Micro result with an organism that the Collecting Site does not have configured in their file, the system automatically creates a new stub entry for that organism. This patch allows the LIM at the Collecting Site to make manual updates to a stub entry. It then sends an email to the LAB MAPPING mail group letting them know that a new term was added to the file.

Since the new stub entry for that organism is missing some important fields the LIM needs to manually add them. The Collecting Site LIM should fill in the IDENTIFIER field (so that the organism will display on the micro trend report), ETIOLOGY WKLD CODE (so that the site can get workload credit, and the  SUSCEPTIBILITY EDIT TEMPLATE (if the site plans on entering susceptibility results locally for that organism). Editing of an entry is a relatively quick process for the LIM.

<u>A sample of the LAB MAPPING mail group message Subject line is below:</u>

> Subj: Term added to file ETIOLOGY FIELD (#61.2:4978)  \[#178806\] 04/10/12@17:24 14 lines

> From: LRLAB, HL  In 'IN' basket.   Page 1  \*New\*

> -----------------------------------------------------------------------

> New term added to file ETIOLOGY FIELD \#61.2 (entry \#4978)

> New Term: Alicyclobacillus

> -----------------------------------------------------------------------

## LAB CODE MAPPING 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/013.png) | NOTE: This functionality is reserved for future use with the Labs and Associated VistA databases once converted to Laboratory Systems (timeframe TBD). |

Modified the HL7 messaging structure to support SNOMED CT coding.

Added the option Manage MI/AP Test Mappings \[LRCAPFF\] to establish the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests.

### LAB CODE MAPPING File (#62.47)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LAB CODE MAPPING file (#62.47) is used to map standard code system concepts to the related area of the Laboratory package database, as well as support mapping codes used in the role identifying the result or expressing the answer. The LAB CODE MAPPING file (#62.47) was created to enhance the legacy VistA Laboratory software.

#### Examples of Result Codes

LOINC and VA NLT Test Result codes, such as LOINC code 11475-1 MICROORGANISM IDENTIFIED: PRID:PT:XXX:NOM:CULTURE, which represent the concept of the organism identified.

#### Examples of Answer Codes

SNOMED CT code 23506009, which is the term normal flora or SNOMED CT code 30334005 AEROMONAS SALMONICIDA (ORGANISM), which represents the name of the organism identified.

#### Fields

SEQUENCE field (#62.47,.001): This field is the Internal Entry Number (IEN) (sequence number).

CONCEPT field (#62.47,.01): This field contains the nature of the codes and the area of the laboratory to which the concept relates.

LR SUBSCRIPT field (#62.47,.02): This field is the LAB DATA file (#63) subscript for this entry.

DATABASE CODE field (#62.47,.03): For result type codes, this field indicates the related area of the Laboratory package database in which answers to the code are stored. The database code indicates the storage location within the Laboratory package.

ALTERNATE CONCEPT field (#62.47,.04): This field designates an alternate concept when the answer associated with the concept is not in a form that can be stored within the current VistA database. For example:

When VistA expects to store the answer as a pointer to a VistA file and the instance of an answer is free text, this field points to a concept that allows the answer to be stored in a field that can accept the answer.

IDENTIFIER field (#62.47,1): This field contains the codes/code sets associated with the concept.

- IDENTIFIER field (#62.4701,.01): This field is the code or ID associated with an instance of the concept. The identifier in conjunction with Coding System field (#.02) indicates use and source.
- CODING SYSTEM field (#62.4701,.02): This field contains the name of the coding system from which the code is derived.
- PURPOSE field (#62.4701,.03): This field classifies the code as a result or answer code.

|                                                   |                                                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/014.png) | NOTE: Codes from the HL7 OBX segment field OBX-3 must be classified as result codes. Codes from the HL7 OBX segment field OBX-5 must be classified as answer codes. |

- OVERRIDE CONCEPT field (#62.4701,.04): For answer type codes, this field indicates the related area of the Laboratory package database in which answers to the code are stored.  
    
  Use it when the answer associated with a result code cannot be stored in the usual VistA Laboratory LAB DATA file (#63) field. For example:

SNOMED CT code 23506009 is the term normal flora. This term is the answer used within the LAB DATA file (#63). If it is associated as the answer to a microorganism identified code, instead of stored as an entry in the ETIOLOGY FIELD file (#61.2), it is stored as a comment.

- NATIONAL STANDARD field (#62.4701,.05): This field flags an entry as nationally distributed or local.
- RELATED ENTRY field (#62.4701,2.1): This field links the code/code set to an entry in one of the pointed-to files, which allows the system to determine how to translate a code/code set to a file entry.
- MESSAGE CONFIGURATION field (#62.4701,2.2): When the related identifier (code) is from a local coding system, this field indicates the specific interface with which the code is associated. Local codes are interface-specific.

## LEDI IV Anatomic Pathology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI IV patch provides several enhancements for Anatomic Pathology.

### New Options to Enter and Edit for AP Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The functionality in the VistA Laboratory Anatomic Pathology section includes:

Populating the LAB DATA (#63), ACCESSION (#68), and LAB ORDER ENTRY (#69) files with:

- AP accession to be consistent with the rest of laboratory's accession process.
- The creation and storing of the UID, ordering data, and order number.

Creation of the ORDERED TEST sub-file (#63.53) for the SP, EM, and CY sections. This sub-file contains information about the ordered tests for this accession. The ORDERED TEST field (#.01) contains the ordered test NLT code requested by the clinical provider. This sub-file contains fifteen fields.

Enhanced the generation of the CPRS Anatomic Pathology alerts/notifications to the following recipients:

- Outpatient Primary Care Provider if patient is Outpatient – new feature.
  - If it is a related surgery case, then the following providers receive the alerts/notifications:
    - The current surgeon if different from surgeon used as ordering provider when specimen was logged in.
    - Attending surgeon.

The list of recipients is displayed to the releasing pathologist/user.

Modified the laboratory user login process for SP, CY, and EM. The process was modified to require an entry from the COLLECTION SAMPLE file (#62), an entry from the TOPOGRAPHY FIELD file (#61), and a selection of multiple orderable test code names from LABORATORY TEST file (#60), during AP login.

|                                                   |                                                                                               |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/015.png) | REF: For a sample of this AP login process, see Chapter 5, "Use of the LEDI IV Software." |

Modified Print log book \[LRAPBK\]:

- If the site has the Document Surgery Package Case Info Parameter set to Yes, then when copying surgical case information from the Surgery package during surgical pathology login a statement will be added to the copied information documenting the source of the copied information.
- The LIM may also set a prompt for printing a single accession. The accession number can be entered by using the \<ACCESSION AREA\> \<DATE\> \<NUMBER\> format or UID in the 10-15 character formats. The Log Book now displays the UID for all entries.

Within Anatomic Pathology result entry options, the user can designate the performing laboratory for the entire report or for specific sections of the report. If choosing to enter the performing laboratory for specific sections, only the sections that have data entered will appear.

Added the option AP LEDI Data Entry \[LRAP VR\]. This option allows data for Anatomic Pathology (LEDI results) to be reviewed and approved individually by accession or by UID. . Once approved, the data is not available for viewing with this option.

The AP reports have been modified to replace “AFIP” or Armed Forces Institute of Pathology with “JPC” or Joint Pathology Center.

![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/016.png) REF: For examples of new or modified options and prompts, see Chapter 5, "Use of the LEDI IV Software."

### Addition of Anatomic Pathology (AP) Orders and Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory is enhanced to handle AP data by storing incoming HL7 result (ORU) messages in the intermediate LAH global if the site is a Host VA that is receiving incoming orders for the three AP sections listed below.

- Cytology – CY.
- Electron Microscopy – EM.
- Surgical Pathology – SP.
- The AP verification process is modified to accept incoming results processed by personnel outside the VA from another VA, a commercial reference lab, or the DoD.
  - Incoming results are accepted or rejected by staff via the ‘AP LEDI Data Entry \[LRAP VR\]’ option.
  - This option moves the data from the LAH global for storage in LAB DATA file (#63).
- <u>The LEDI IV Update patch provides new features outlined below.  
  > </u>

  Upon verification of an AP report at the Host site, an outgoing HL7 result message to the Collection site is triggered via the ‘Verify/release reports, anat path \[LRAPRS\]’ option.

> **NOTE:** Because the outgoing HL7 result messages are for referral patients, these AP reports are not stored in TIU.

- The patches support the acceptance and processing of AP electronic orders and results via LEDI HL7 messaging.
- Determine the test order number, type of specimen and collection sample code for an outgoing order message.
- Generate HL7 messaging exceptions for incomplete LEDI orders located in LABORATORY PENDING ORDER file (#69.6).
- Generate HL7 messaging exceptions for LEDI results that cannot be processed.
- Process incoming HL7 order (ORM) messages from DoD facilities.
- Process messages and store the orders in the LABORATORY PENDING ORDER file (#69.6).

## LEDI IV LOINC Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/017.png) | NOTE: This functionality is reserved for future use with a subsequent release of the LEDI software (timeframe TBD). |

Several modifications are provided by the LEDI IV Patch for LOINC functionality.

The LAB CODE MAPPING file (#62.47) provides the ability to map the LOINC codes of external systems to corresponding Microbiology and Anatomic Pathology concepts.

This file is used to map standard code system concepts to the related area of the Laboratory package database, as well as to support mapping codes used in the roles of identifying the result or expressing the answer.

The VistA Laboratory LEDI software provides the ability to report Microbiology and AP results with pre-determined and site-configurable mapping of LOINC codes.

The VistA Laboratory LEDI software allows standardized reporting of Microbiology tests results and site-mapped antibiotics to LOINC.

SNOMED CT hierarchy concepts added to the LAB ELECTRONIC CODES file (#64.061) to support routing of SNOMED CT concepts to corresponding sections of the VistA Laboratory database.

LOINC codes received from external systems are accepted and mapped to corresponding VistA Laboratory database concepts via the .01 Concept field of the LAB CODE MAPPING file (#62.47).

## LEDI IV Chemistry/Hematology (CH) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI IV patch provides new enhancements for Chemistry and Hematology.  
  
Within Chemistry and Hematology result entry options, the user can opt to send one of three alert types to the ordering provider and additional recipients and/or mail groups. Depending on how the parameter is set, will determine whether the user is prompted to send an alert. The three alert types are:

- Lab results available.
- Abnormal lab results.
- Critical lab results.

|                                                   |                                                                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/018.png) | NOTE: The type of alert generated either depends on whether the clinician has set the parameter for personal alerts in CPRS, or if the alert is mandatory at the system level. |
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/019.png) | REF: For additional details on these alerts, see the the “APPENDIX B: HOW NOTIFICATIONS WORK - TECHNICAL OVERVIEW” section in the CPRS Technical Manual in the VDL.        |

## LEDI IV AP/MICRO INTERFACE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Orders and Results for Anatomic Pathology (AP) – Update Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To complete the verification process, a PROVIDER key, a provider class of PHYSICIAN, a person class of Pathology Allopathic or Osteopathic Physicians and a valid electronic signature code are needed. Below, are the instructions on how to add those (if not already entered) via VA FileMan edits. Make these edits for both the collection site and the host facility. The updated VHA PERSON CLASS code list of positions which can release AP reports is below:

<u>Specialization:</u>                          

Pathology, Anatomic & Clinical           

Pathology, Anatomic                      

Pathology, Anatomic & Laboratory Medicine

Pathology, Chemical                      

Pathology, Clinical                      

Dermatopathology                         

Hematology: Pathology                    

Neuropathology                           

Oral and Maxillofacial Pathology   

Cytotechnology

> **NOTE:** Cytotechnologists can release Negative Gynecological results as long as they are a Provider Class of CYTOTECHNOLOGIST, a PERSON CLASS \# of 430 Cytotechnology and have a LRVERIFY security key.

<span id="_Toc510168946" class="anchor"></span>Figure 5. Person Class Edit Option \[XU-PERSON CLASS EDIT\] <span class="mark"></span>

Select User Management \<TEST ACCOUNT\> Option: PERSON CLASS Edit

Select NEW PERSON NAME: <span class="mark">LRPROVIDER</span>

1 LRPROVIDER,ONE JR WGA

2 LRPROVIDER,TWO CKA

CHOOSE 1-2: <span class="mark">2</span> LRPROVIDER,TWO CKA

Edit of Person Class

NAME: LRPROVIDER,TWO\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Allopathic and Osteopathic Physicians (M.D. and D.O.) JUN 27, 2013

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: EXIT Press \<PF1\>H for help Insert

You’ve got PRIORITY mail!

1.  On the collection site, log in an AP accession and transmit the order to the host facility:

> <span id="_Toc510168947" class="anchor"></span>Figure 6. Log-in Anatomic Pathology Accession \[LRAPLG\]

Select Anatomic pathology \<TEST ACCOUNT\> Option: <span class="mark">l</span> Log-in menu, anat path

Select Log-in menu, anat path \<TEST ACCOUNT\> Option: <span class="mark">li</span> Log-in, anat path

Select ANATOMIC PATHOLOGY SECTION: SURGICAL PATHOLOGY

Log-In for 2012 ? // <span class="mark">\<ENTER\></span> (YES)

Select Patient Name: <span class="mark">hxx,pxxx,PXXXXXX HXX,PXXXXXX</span> 1-1-60 XXXXXXXXX

NO NSC VETERAN

Enrollment Priority: Category: IN PROCESS End Date:

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from NOV 17,2009

Enter \<RETURN\> to continue.

HXX,PXXXXXX ID: XXX-XX-XXXX Physician: LRUSER,ONE

AGE: 52 DATE OF BIRTH: JAN 1,1960

PATIENT LOCATION: UNK// <span class="mark">2E 2 EAST</span>

Accession number assigned for Nov 20, 2012 is: NSP 12 22

Checking surgical record for this patient...

No operations on record in the past 7 days for this patient.

Assign SURGICAL PATHOLOGY (NSP) accession \#: 23? YES// <span class="mark">\<ENTER\></span> (YES)

Date/time Specimen taken: NOW// (NOV 20, 2012@17:40)

SURGEON/PHYSICIAN: <span class="mark">lrprovider,ONE JR</span> LRPROVIDER,ONE JR WGA

SPECIMEN SUBMITTED BY: <span class="mark">lrprovider,one</span>

Select SPECIMEN: <span class="mark">skin</span>

SPECIMEN TOPOGRAPHY: skin

1 SKIN 01000

2 SKIN APPENDAGE 01300

3 SKIN BETWEEN FOURTH AND FIFTH TOES 02915

4 SKIN BETWEEN GREAT TOE AND SECOND TOE 02885

5 SKIN BETWEEN THIRD AND FOURTH TOES 02905

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">1</span> SKIN 01000

COLLECTION SAMPLE: skin

Select SPECIMEN:

DATE/TIME SPECIMEN RECEIVED: NOW// (NOV 20, 2012@17:41)

PATHOLOGIST: lrprovider,ONE JR LRPROVIDER,ONE JR WGA

Select COMMENT:

Select LABORATORY TEST: // <span class="mark">TISSUE EXAM</span> SP

Select Patient Name:

Select Log-in menu, anat path \<TEST ACCOUNT\> Option:

Select Anatomic pathology \<TEST ACCOUNT\> Option:

<span id="_Toc510168948" class="anchor"></span>Figure 7. Collection Site Builds AP Shipping Manifest \[LA7S MANIFEST BUILD\]

Select Laboratory DHCP Menu \<TEST ACCOUNT\> Option: <span class="mark">lsm</span> Lab Shipping Menu

Select Lab Shipping Menu \<TEST ACCOUNT\> Option: <span class="mark">smb</span> Build Shipping Manifest

Select Shipping Configuration: <span class="mark">mhc</span> TO VRR

There's no open shipping manifest for MHC TO VRR

Do you want to start one? NO// <span class="mark">y</span> YES

Use default accession dates? YES//

Exclude previously removed tests from building? YES//

Using shipping manifest# 522-20121120-2

Searching accession area: CHEMISTRY

Searching accession area: MICROBIOLOGY

Searching accession area: SURGICAL PATHOLOGY

Searching accession area: EM

Searching accession area: CYTOPATHOLOGY

There were 2 specimens added

Print Shipping Manifest? NO// <span class="mark">y</span> YES

DEVICE: HOME// 0;80;9999 VIRTUAL TELNET

\*\*\* DO NOT USE FOR SHIPPING DOCUMENT - WORK COPY ONLY \*\*\*

Shipping Manifest: 522-20121120-2 Page: 1

to Site: REGION 7 ISC,TX (FS) Printed: Nov 20, 2012@17:42

from Site: ZZ BONHAM E-Order: YES

Status: OPEN Ship via: COURIER

Shipping Condition: ROOM TEMPERATURE Container: BOX

Item Patient Name Patient ID Accession

Date of Birth Patient ICN Specimen UID

Requested By Sex Collect Date/Time

-------------------------------------------------------------------------------

1-1 HXX,PXXXXXX XXX-XX-XXXX NSP 12 23

Jan 01, 1960 2212000023

LRPROVIDER,ONE JR Male Nov 20, 2012@17:40

Specimen Container: PLASTIC TUBE

-----------------------------------------

SURGICAL PATHOLOGY LOG-IN SKIN

VA NLT Code \[Name\]: 93940.0000 \[Surgical Pathology Tissue Exam\]

-----------------------------------------

TISSUE EXAM SKIN

VA NLT Code \[Name\]: 93940.0000 \[Surgical Pathology Tissue Exam\]

-------------------------------------------------------------------------------

End of Shipping Manifest

<span id="_Toc510168949" class="anchor"></span>Figure 8. Close/Ship an AP Shipping Manifest \[LA7S MANIFEST CLOSE/SHIP\]

Select Lab Shipping Menu \<TEST ACCOUNT\> Option: <span class="mark">sms</span> Close/Ship a Shipping Manifest

Select Shipping Configuration: <span class="mark">mhc</span> TO VRR

Select Shipping Manifest: 522-20121120-2 MHC TO VRR Status: OPEN as of Nov 20,

2012@17:42

Select one of the following:

1 Close manifest

2 Ship manifest

Select action to perform: 1// <span class="mark">2</span> Ship manifest

Enter Manifest Shipping Date: NOW// (NOV 20, 2012@18:11)

Electronic Transmission of Shipping Manifest queued as task# 1465284

Print Shipping Manifest? NO//<span class="mark">\<ENTER\></span>

Select Lab Shipping Menu \<TEST ACCOUNT\> Option:

2.  On the host facility, accession the order via the ‘Referral Patient Multi-purpose Accession’ option and enter results. Note: There are two examples of the same screen shown below. The first example shows the Host using their own bar code UID. The second example shows how the screen looks when the lab uses the collection site UID.

> <span id="_Toc510168950" class="anchor"></span>Figure 9. Host Accessions AP Order Using Referral Patient Multi-purpose Accession Option \[LRLEDI\]

*Editor’s Note: First example when the lab uses their own bar code UID.*

Select Accessioning Menu Option: Referral Patient Multi-purpose Accession

Are you using a barcode reader? YES//

Scan Remote Site Barcode (SM): STX^SITE^500^3130620.1127^500-20130620-7^ETX110

Select ACCESSION TEST GROUP: <span class="mark">SEND OUTS</span>

Scan Patient/Accession Barcode (PD): STX^PD^000008888^500^1031710025^M^3130620.0

81517^ETX110

NAME: LABPATIENT,TEST SEX: MALE

DOB: 07/07/1920 RACE: UNKNOWN

IDENTIFIER: 000008888

LAB Order number: 272603

You have just selected the following tests for LABPATIENT,TEST 000-00-8888

entry no. Test Sample

1 CULTURE,SPUTUM SPUTUM

All satisfactory? Yes// <span class="mark">(Yes)</span>

LAB Order number: 272603

Print labels on: LABLABEL// SEND

~For Test: CULTURE,SPUTUM SPUTUM

Enter Comment (DO NOT ORDER TESTS HERE!):

ACCESSION: MICRO 13 99 \<7313000099\>

CULTURE,SPUTUM SPUTUM

Scan Patient/Accession Barcode (PD): <span class="mark">^</span>

*Editor’s Note: Second example in which the lab uses the Collection site UID*.

Select Accessioning Menu Option: Referral Patient Multi-purpose Accession

Are you using a barcode reader? YES//

Scan Remote Site Barcode (SM): STX^SITE^500^3130620.1127^500-20130620-7^ETX110

Select ACCESSION TEST GROUP: <span class="mark">SEND OUTS</span>

Scan Patient/Accession Barcode (PD): STX^PD^000008888^500^1031710025^M^3130620.0

81517^ETX110

NAME: LABPATIENT,TEST SEX: MALE

DOB: 07/07/1920 RACE: UNKNOWN

IDENTIFIER: 000008888

LAB Order number: 272603

You have just selected the following tests for LABPATIENT,TEST 000-00-8888

entry no. Test Sample

1 CULTURE,SPUTUM SPUTUM

All satisfactory? Yes// <span class="mark">(Yes)</span>

LAB Order number: 272603

Print labels on: LABLABEL// SEND

~For Test: CULTURE,SPUTUM SPUTUM

Enter Comment (DO NOT ORDER TESTS HERE!):

ACCESSION: MICRO 13 99 \<1031710025\>

CULTURE,SPUTUM SPUTUM

Scan Patient/Accession Barcode (PD): <span class="mark">^</span>

> <span id="_Toc510168951" class="anchor"></span>Figure 10. Host Site Enters A/P Results

ANATOMIC PATHOLOGY MENU

D Data entry, anat path ...

E Edit/modify data, anat path ...

I Inquiries, anat path ...

L Log-in menu, anat path ...

P Print, anat path ...

R SNOMED field references ...

S Supervisor, anat path ...

V Verify/release menu, anat path ...

C Clinician options, anat path ...

W Workload, anat path ...

Select Anatomic pathology Option: <span class="mark">d</span> Data entry, anat path

AU Data entry for autopsies ...

BS Blocks, Stains, Procedures, anat path

CO Coding, anat path ...

GD Clinical Hx/Gross Description/FS

GM FS/Gross/Micro/Dx

GS FS/Gross/Micro/Dx/SNOMED Coding

GI FS/Gross/Micro/Dx/ICD9CM Coding

OR Enter old anat path records

SR Supplementary Report, Anat Path

SS Spec Studies-EM;Immuno;Consult;Pic, Anat Path

LEDI AP LEDI Data Entry

Select Data entry, anat path Option: <span class="mark">gm</span> FS/Gross/Micro/Dx

Select ANATOMIC PATHOLOGY SECTION: SURGICAL PATHOLOGY

SURGICAL PATHOLOGY (NSP)

Data entry for 2012 ? YES// (YES)

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// Accession number

Enter Accession Number: <span class="mark">NSP 12 8</span>

Enter the year 2012 SURGICAL PATHOLOGY accession number to be updated.

Enter Accession Number: \[2212000023\] for 2012

HXX,PXXXXXX XXX-XX-XXXX DOB: Jan 01, 1960

Collection Date: Nov 20, 2012@17:40

Acc \#: NSP 12 8 \[2212000023\]

Tissue Specimen(s):

Skin structure (body structure)

Skin structure (body structure)

Test(s): SURGICAL PATHOLOGY LOG-IN

FROZEN SECTION:

No existing text

Edit? NO//<span class="mark">\<ENTER\></span>

GROSS DESCRIPTION:No existing text

Edit? NO//<span class="mark">\<ENTER\></span>

MICROSCOPIC DESCRIPTION:

No existing text

Edit? NO// <span class="mark">\<ENTER\></span>

SURGICAL PATH DIAGNOSIS:

No existing text

Edit? NO// <span class="mark">y</span> YES

PATHOLOGIST: lrprovider,o

1 LRPROVIDER,ONE MRY COMPUTER SPECIALIST

2 LRPROVIDER,ONE MD OLP IRM

CHOOSE 1-2: 1 LRPROVIDER,ONE MRY COMPUTER SPECIALIST

DATE REPORT COMPLETED: <span class="mark">T</span> (NOV 20, 2012)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// Entire report

Select Performing Laboratory: <span class="mark">ZZ BONHAM</span>// TX VAMC 522

Sure you want to add this record? NO// <span class="mark">y</span><span class="mark">\<ENTER\></span> YES

... assignment created.

Current performing lab assignments:

Surgical Pathology Report Performed By: <span class="mark">ZZ BONHAM</span> <span class="mark">\<ENTER\></span>

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

Enter CPT coding? NO//<span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// <span class="mark">^</span>

AU Data entry for autopsies ...

BS Blocks, Stains, Procedures, anat path

CO Coding, anat path ...

GD Clinical Hx/Gross Description/FS

GM FS/Gross/Micro/Dx

GS FS/Gross/Micro/Dx/SNOMED Coding

GI FS/Gross/Micro/Dx/ICD9CM Coding

OR Enter old anat path records

SR Supplementary Report, Anat Path

SS Spec Studies-EM;Immuno;Consult;Pic, Anat Path

LEDI AP LEDI Data Entry

Select Data entry, anat path Option:

3.  Next, verify and release the report. A message should appear indicating that results will be sent back to the collection site:

<span id="_Toc510168952" class="anchor"></span>Figure 11. Host Site Verifies and Releases Report \[LRAPVR\]

Select Anatomic pathology Option: <span class="mark">v</span> Verify/release menu, anat path

RR Verify/release reports, anat path

RS Supplementary report release, anat path

LU List of unverified pathology reports

CPT LAB CPT BILLING

SA Send an AP Alert

Select Verify/release menu, anat path Option \[LRAPR\]: <span class="mark">rr</span> Verify/release reports, anat path

Release/Electronically Sign Pathology Reports

Select one of the following:

C CPT Coding

E Electronically Sign Reports

V View SNOMED Codes

Selection: <span class="mark">e</span> Electronically Sign Reports

Select ANATOMIC PATHOLOGY SECTION: <span class="mark">SURGICAL PATHOLOGY</span>

SURGICAL PATHOLOGY (NSP)

Data entry for 2012 ? YES//<span class="mark">\<ENTER\></span> (YES)

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// <span class="mark">\<ENTER\></span> Accession number

Enter Accession Number: <span class="mark">8</span> for 2012

HXX,PXXXXXX XXX-XX-XXXX DOB: Jan 01, 1960

Collection Date: Nov 20, 2012@17:40

Acc \#: NSP 12 8 \[2212000023\]

Tissue Specimen(s):

Skin structure (body structure)

Skin structure (body structure)

Test(s): SURGICAL PATHOLOGY LOG-IN

View the report before signing? YES// <span class="mark">n</span><span class="mark">\<ENTER\></span> NO

Enter your Current Signature Code: SIGNATURE VERIFIED

\*\*\* Report is being processed. One moment please. \*\*\*

\*\*\* NOTE: This REFERRAL PATIENT report will not be stored in TIU and therefore does not have an electronic signature. A hardcopy signature will be required for this report.

\*\*\* Report released. \*\*\*

Sending report to LEDI collecting site

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// <span class="mark">^</span>

Select one of the following:

C CPT Coding

E Electronically Sign Reports

V View SNOMED Codes

Selection:

RR Verify/release reports, anat path

RS Supplementary report release, anat path

LU List of unverified pathology reports

CPT LAB CPT BILLING

SA Send an AP Alert

Select Verify/release menu, anat path Option:

4.  On the collection site end, accept the results from the host using the ‘AP LEDI Data Entry’ option:

<span id="_Toc510168953" class="anchor"></span>Figure 12. Collection Site approves results using the AP LEDI Data Entry option \[LRAPD\]

Select Anatomic pathology \<TEST ACCOUNT\> Option: <span class="mark">d</span> Data entry, anat path

Select Data entry, anat path \<TEST ACCOUNT\> Option: <span class="mark">?</span>

AU Data entry for autopsies ...

BS Blocks, Stains, Procedures, anat path

CO Coding, anat path ...

GD Clinical Hx/Gross Description/FS

GM FS/Gross/Micro/Dx

GS FS/Gross/Micro/Dx/SNOMED Coding

GI FS/Gross/Micro/Dx/ICD9CM Coding

OR Enter old anat path records

SR Supplementary Report, Anat Path

SS Spec Studies-EM;Immuno;Consult;Pic, Anat Path

LEDI AP LEDI Data Entry

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Data entry, anat path \<TEST ACCOUNT\> Option: <span class="mark">ledi</span> AP LEDI Data Entry

Select LOAD/WORK LIST NAME: <span class="mark">??</span>*Editor note: See AP/MICRO Config Guide for details*

Choose from:

AFB

ANCILLARY TESTING

ANTI-DS DNA AB

APO A

BLOOD CULTURE

BLOOD GAS

CHEM 7

COAG

COBAS

CYTOPATHOLOGY

DIFF

DRUGS

EM

HEMATOLOGY

HEPATITIS

KODAK

LAB POC

LDSI

MANUAL BENCH

MICROBIOLOGY

MYCOLOGY

RIA

SMAC

SURGICAL PATHOLOGY

UA

VDRL

VITEK

WK-BB

WK-CYTOLOGY

WK-LITHIUM

Select LOAD/WORK LIST NAME: <span class="mark">ldsi</span>

Select PROFILE: <span class="mark">??</span>

Choose from:

CHEMISTRY CHEMISTRY

CYTOPATHOLOGY CYTOPATHOLOGY

EM PATHOLOGY EM

MICROBIOLOGY MICROBIOLOGY

SURGICAL PATHOLOGY SURGICAL PATHOLOGY

Select PROFILE: <span class="mark">SURGICAL PATHOLOGY</span> SURGICAL PATHOLOGY

Select Performing Laboratory: <span class="mark">REGION 7 ISC,TX (FS)</span>// TX 170

Work Load Area: LDSI//<span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// <span class="mark">2</span> Unique Identifier (UID)

Unique Identifier: 2212000023

HXX,PXXXXXX XXX-XX-XXXX Age: 52yr

ORDER \#: 399 NSP 12 23 \[2212000023\]

Seq \#: 69 Accession: NSP 12 23 Results received: Nov 20, 2012@23:22

UID: 2212000023 Last updated: Nov 20, 2012@23:22

Enter RETURN to continue or '^' to exit:

DEVICE: HOME// 0;80;9999 VIRTUAL TELNET

Accession \#: NSP 12 23 UID: 2212000023

Name: HXX,PXXXXXX SSN: XXX-XX-XXXX DOB: Jan 01, 1960 Age: 52yr PAGE: 1

Collection Date: Nov 20, 2012@17:40

-------------------------------------------------------------------------------

Surgical Pathology Diagnosis

Surgical Pathology diagnosis text for CCR testing.

Do you want to ACCEPT these results? NO// <span class="mark">y</span><span class="mark">\<ENTER\></span> YES

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// TX VAMC 522 INACTIVE Jan 01, 1997

Sure you want to add this record? NO// <span class="mark">y</span><span class="mark">\<ENTER\></span> YES

... assignment created.

Current performing lab assignments:

Surgical Pathology Report Performed By: ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for:

Unique Identifier:

Select Data entry, anat path \<TEST ACCOUNT\> Option:

### Orders and Results for Microbiology (MI) –Update Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the collection site, accession a microbiology order and transmit the accessioned microbiology order to the host facility:

<span id="_Toc510168954" class="anchor"></span>Figure 13. Collecting Site Builds MICRO Shipping Manifest \[LA7S MANIFEST BUILD\]

Select Accessioning menu Option:

1 Phlebotomy menu ...

2 Accessioning menu ...

3 Process data in lab menu ...

4 Quality control menu ...

5 Results menu ...

6 Information-help menu ...

7 Ward lab menu ...

8 Anatomic pathology ...

9 Blood bank ...

10 Microbiology menu ...

11 Supervisor menu ...

LSM Lab Shipping Menu ...

Select Laboratory DHCP Menu Option: <span class="mark">lsm</span> Lab Shipping Menu

SMB Build Shipping Manifest

SSM Start a Shipping Manifest

SMS Close/Ship a Shipping Manifest

ART Add/Remove a Shipping Manifest Test

SMR Edit Required Test Information

SMI Edit Relevant Clinical Information

SMC Cancel a Shipping Manifest

PSM Print Shipping Manifest

STA Order Status Report

RSM Retransmit Shipping Manifest

RLR Retransmit LEDI Lab Results

SMP Print LEDI Pending Orders

Select Lab Shipping Menu Option: <span class="mark">smb</span> Build Shipping Manifest

Select Shipping Configuration: <span class="mark">BONHAM HOST</span>

There's no open shipping manifest for BONHAM HOST

Do you want to start one? NO// <span class="mark">y</span> YES

Use default accession dates? YES//

Exclude previously removed tests from building? YES// <span class="mark">\<ENTER\></span>

Using shipping manifest# 170-20121022-1

Searching accession area: CHEMISTRY

Searching accession area: MICROBIOLOGY

Searching accession area: SURGICAL PATHOLOGY

Searching accession area: CYTOPATHOLOGY

Searching accession area: TOXICOLOGY

There were 1 specimens added

Print Shipping Manifest? NO// <span class="mark">y</span> YES

DEVICE: HOME// 0;80;9999 VIRTUAL TELNET

\*\*\* DO NOT USE FOR SHIPPING DOCUMENT - WORK COPY ONLY \*\*\*

Shipping Manifest: 170-20121022-1 Page: 1

to Site: ZZ BONHAM Printed: Oct 22, 2012@10:12

from Site: DALLAS OI E-Order: YES

Status: OPEN Ship via: COURIER

Shipping Condition: ROOM TEMPERATURE Container: STYROFOAM BOX

Item Patient Name Patient ID Accession

Date of Birth Patient ICN Specimen UID

Requested By Sex Collect Date/Time

-------------------------------------------------------------------------------

1-1 XXX,PXXXXXX XXX-XX-XXXX MICRO 12 27

Jan 01, 1960 5000000423V938388 1412000027

LRPROVIDER,ONE Male Oct 22, 2012@10:09

Specimen Container: CULTURE

Collection sample: URINE

-----------------------------------------

URINE CULTURE URINE

VA NLT Code \[Name\]: 87553.0000 \[Urine Culture\]

-------------------------------------------------------------------------------

End of Shipping Manifest

<span id="_Toc510168955" class="anchor"></span>Figure 14. Close/Ship a MICRO Shipping Manifest \[LA7S MANIFEST CLOSE/SHIP\]

Select Shipping Configuration: BONHAM HOST

Select Shipping Manifest: 170-20121022-1 BONHAM HOST Status: OPEN as of Oct 22, 2012@10:12

Select one of the following:

1 Close manifest

2 Ship manifest

Select action to perform: 1// <span class="mark">2</span> Ship manifest

Enter Manifest Shipping Date: NOW// (OCT 22, 2012@10:13)

Electronic Transmission of Shipping Manifest queued as task# 3794701

Print Shipping Manifest? NO//

SMB Build Shipping Manifest

SSM Start a Shipping Manifest

SMS Close/Ship a Shipping Manifest

ART Add/Remove a Shipping Manifest Test

SMR Edit Required Test Information

SMI Edit Relevant Clinical Information

SMC Cancel a Shipping Manifest

PSM Print Shipping Manifest

STA Order Status Report

RSM Retransmit Shipping Manifest

RLR Retransmit LEDI Lab Results

SMP Print LEDI Pending Orders

2.  On the host facility, accession the order via the ‘Referral Patient Multi-purpose Accession’ option and enter results. A message indicating that results will be sent back to the collection site should appear:

<span id="_Toc510168956" class="anchor"></span>Figure 15. Host Accessions MICRO Order on Referral Multi-purpose Accession Option \[LRLEDI\]

Select Accessioning menu \<TEST ACCOUNT\> Option: referral Patient Multi-purpose

Accession

Are you using a barcode reader? YES// <span class="mark">n</span> NO

Select Shipping Configuration: <span class="mark">??</span>

Choose from:

CBOC TO MAIN

DOD-SAIC (COLLECTING SITE)

MILW

VRR COLLECTION

Select Shipping Configuration: <span class="mark">vrr</span> COLLECTION

SHIPPING MANIFEST: 170-20121022-1

Lookup orders using this manifest? YES//

Select ACCESSION TEST GROUP:

Select one or more tests from which you will be generating your entries.

Select LABORATORY TEST NAME: urine CULTURE URN CUL

Is URINE the correct sample to collect? Y//

Same specimen/source for the rest of the order? No// (No)

Select LABORATORY TEST NAME:

Enter UID of specimen: <span class="mark">??</span>

Choose from: 1412000027 HXX,PXXXXXX

Pat ID: XXXXXXXXX DOB: Jan 01, 1960 Sex: MALE

Spec ID: 1412000027 Manifest: 170-20121022-1 Site: REGION 7 ISC,TX (FS)

Collected D/T: Oct 22, 2012@11:09 Specimen: URINE Spec. Status: In-Transit

Enter UID of specimen: 1412000027 HXX,PXXXXXX

Pat ID: XXXXXXXXX DOB: Jan 01, 1960 Sex: MALE

Spec ID: 1412000027 Manifest: 170-20121022-1 Site: REGION 7 ISC,TX (FS)

Collected D/T: Oct 22, 2012@11:09 Specimen: URINE Spec. Status: In-Transit

...OK? // <span class="mark">\<ENTER\></span> (Yes)

LAB Order number: 375

Collecting site order comments:

For test URINE CULTURE

Specimen source: Urine (substance) \[78014005:SCT\] ; Urine \[UR:HL70070\]

Collection sample: Urine specimen (specimen) \[122575003:SCT\] ;URINE \[15:99VA62\]

You have just selected the following tests for HXX,PXXXXXX XXX-XX-XXXX

entry no. Test Sample 1 URINE CULTURE URINE SPECIMEN URINE

All satisfactory? Yes// <span class="mark">\<ENTER\></span> (Yes)

LAB Order number: 375

Print labels on: LABLABEL// null Bit Bucket

Do you wish to test the label printer: NO// <span class="mark">\<ENTER\></span>

ACCESSION: MICRO 12 30 \<1412000030\>

URINE CULTURE URINE SPECIMEN URINE

COMMENT ON SPECIMEN: Test for CCR_8693 (sending results back).

(Test for CCR_8693 (sending results back).)

Description OK? Y//

<span id="_Toc510168957" class="anchor"></span>Figure 16. Host Site Enters MICRO Results \[LRMIEDZ\]

Select Laboratory DHCP Menu \<TEST ACCOUNT\> Option: <span class="mark">10 \<ENTER\></span> Microbiology menu

Select Microbiology menu \<TEST ACCOUNT\> Option: <span class="mark">re\<ENTER\></span> Results entry

Select MICROBIOLOGY Accession or UID: <span class="mark">MICRO 12 30</span>

MICROBIOLOGY (2012) 30

Work Load Area: MICROBIOLOGY

Select TEST/PROCEDURE: URINE CULTURE URN CUL

HXX,PXXXXXX SSN: XXX-XX-XXXX

Pat Info: Sex: MALE Age: 52yr as of Oct 22, 2012

Edit this accession? YES// <span class="mark">\<ENTER\></span>

WARD COMMENTS ON SPECIMEN: For test URINE CULTURE

Specimen source: Urine (substance) \[78014005:SCT\] ; Urine \[UR:HL70070\]

Collection sample: Urine specimen (specimen) \[122575003:SCT\] ; URINE

\[15:99VA62\]

URINE CULTURE completed: <span class="mark">t</span> (OCT 23, 2012)

COLLECTION SAMPLE: URINE SPECIMEN//

SITE/SPECIMEN: URINE//

COMMENT ON SPECIMEN: <span class="mark">Test for CCR_8693</span> (sending results back).

Replace

Select GRAM STAIN: NR

(GRAM NEGATIVE RODS)

Select GRAM STAIN: NP

(NP)

Select GRAM STAIN:

BACT RPT STATUS: <span class="mark">f</span> FINAL REPORT

URINE SCREEN:

Select ORGANISM: ESCHERICHIA COLI 1571 112283007 SCT Organism

ORGANISM ISOLATE NUMBER: 1//

ORGANISM: ESCHERICHIA COLI//

QUANTITY: <span class="mark">2+</span>

(2+)

Select COMMENT:

COLISTIN:

GENTAMICIN: I (I)

CHLORAMPHENICOL: R (RESIS)

TETRACYCLINE: S (SUS)

AMPICILLIN: 32 (S)

CARBENICILLIN: I (I)

TOBRAMYCIN: R (RES)

TRIMETHAPRIM/SULFAMETHOXAZOLE: S (SUS)

AMIKACIN: \>256 (\>256)

CEFAMANDOLE: I (I)

CEFOXITIN: R (RESIS)

NITROFURANTOIN: S (SUS)

CEPHALOTHIN: I (I)

1 ESCHERICHIA COLI

Select ORGANISM:

Select BACT RPT REMARK:

BACT RPT DATE APPROVED: <span class="mark">n</span> (OCT 23, 2012@17:21)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// TX VAMC 522

Sure you want to add this record? NO// <span class="mark">y</span> YES

... assignment created.

Current performing lab assignments:

Bacteriology Report Performed By:

ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for:

URINE CULTURE completed: 10/23/2012 //

Sending report to LEDI collecting site

3.  On the collection site, a message will appear indicating that new Micro results were received from the host. Process the results via the ‘Enter/verify data (auto instrument)’ option:

<span id="_Toc510168958" class="anchor"></span>Figure 17. Collection Site Processes MICRO Results on ‘Enter/verify data (auto Instrument)’ \[LRVR\]

Select OPTION NAME: lrmenu Laboratory DHCP Menu

1 Phlebotomy menu ...

2 Accessioning menu ...

3 Process data in lab menu ...

4 Quality control menu ...

5 Results menu ...

6 Information-help menu ...

7 Ward lab menu ...

8 Anatomic pathology ...

9 Blood bank ...

10 Microbiology menu ...

11 Supervisor menu ...

LSM Lab Shipping Menu ...

Lab Msg - New Microbiology results received for LA7V HOST 522

Enter "VA to jump to VIEW ALERTS option

Select Laboratory DHCP Menu Option: <span class="mark">3</span> Process data in lab menu

EA Enter/verify data (auto instrument)

EL Enter/verify data (Load list)

EM Enter/verify/modify data (manual)

EW Enter/verify data (Work list)

GA Group verify (EA, EL, EW)

MP Misc. Processing Menu ...

Accession order then immediately enter data

Batch data entry (chem, hem, tox, etc.)

Build a load/work list

Bypass normal data entry

Fast Bypass Data Entry/Verify

Lookup accession

Order/test status

Print a load/work list

Std/QC/Reps Manual Workload count

Unload Load/Work List

Select Process data in lab menu Option: <span class="mark">ea</span> Enter/verify data (auto instrument)

Select LOAD/WORK LIST NAME: <span class="mark">??</span> *Editor note: See AP/MICRO Config Guide for details*

Choose from:

ABBOTT

ACA IV

AFB

ANTI-DS DNA AB

APO A

BLOOD CULTURE

BLOOD GAS

CHEM 7

CHEMISTRY

COAG

DIFF

DOD SAIC

DRUGS

FRANK TEST

HEMATOLOGY

HEPATITIS

KODAK

LA7V HOST ACH

LA7V REMOTE 170

LAB CORP

LAH38

MANUAL BENCH

MICROBIOLOGY

MYCOLOGY

POC

POC-NEW

RALSG

RIA

SMAC

UA

VDRL

VITEK

WK-BB

WK-CYTOLOGY

WK-LITHIUM

Select LOAD/WORK LIST NAME: LA7V REMOTE 170

Select PROFILE: <span class="mark">??</span>

Choose from:

VA AP/DALLAS OI-HOST SURGICAL PATHOLOGY

VA CH/DALLAS OI-HOST CHEMISTRY

VA MICRO/DALLAS OI-HOST MICROBIOLOGY

Select PROFILE: va MICRO/DALLAS OI-HOST MICROBIOLOGY

Select Performing Laboratory: DALLAS OI// TX 170

Work Load Area: LA7V REMOTE 170//

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// Accession Number

Accession Date: TODAY//10-23-2012 (OCT 23, 2012)

Enter Accession number part: 1// 27

Seq \#: 24 Accession: MICRO 12 27 Results received: Oct 23, 2012@17:22

UID: 1412000027 Last updated: Oct 23, 2012@17:22

HXX,PXXXXXX XXX-XX-XXXX Age: 52yr

ORDER \#: 682 MICRO 12 27 \[1412000027\]

Enter RETURN to continue or '^' to exit:

HXX,PXXXXXX XXX-XX-XXXX AGE: 52

Nov 20, 2012@16:21

----MICROBIOLOGY----

page 1

Accession \[UID\]: MICRO 12 27 \[1412000027\] Received: Oct 22, 2012@10:09

Collection sample: URINE Collection date: Oct 22, 2012 10:09

Provider: LRPROVIDER,ONE

Comment on specimen: <span class="mark">Test for CCR_8693</span> (sending results back).

Test(s) ordered: URINE CULTURE

\* BACTERIOLOGY FINAL REPORT =\> Nov 20, 2012 16:21 TECH CODE: 123456813

GRAM STAIN: GRAM NEGATIVE RODS

NP

CULTURE RESULTS: ESCHERICHIA COLI - Quantity: 2+

Comment: For AMPICLN: DISPLAY COMMENT

For NITROFURANTOIN REAL LONG NAME: DISPLAY COMMENT

ANTIBIOTIC SUSCEPTIBILITY TEST RESULTS:

ESCHERICHIA COLI

:

SUSC INTP

AMIKACN....................... \>256 TESTING DISPLAY COMMENT

HXX,PXXXXXX XXX-XX-XXXX ROUTING: MICU

HXX,PXXXXXX XXX-XX-XXXX AGE: 52

Nov 20, 2012@16:21

\>\> CONTINUATION OF MICRO 12 27 \<\<

page 2

Collection sample: URINE Collection date: Oct 22, 2012 10:09

ESCHERICHIA COLI

:

SUSC INTP

AMPICLN....................... 32 S

CARBCLN....................... I I TESTING DISPLAY COMMENT

CEFMAND....................... I I TESTING DISPLAY COMMENT

CEFOXITIN..................... R R TESTING DISPLAY COMMENT

CHLORAM....................... R R TESTING DISPLAY COMMENT

NITROFURANTOIN REAL LONG NAME. S S TESTING DISPLAY COMMENT MAX LENGTH

DISPL

TETRCLN....................... S S TESTING DISPLAY COMMENT

TOBRMCN....................... R R TESTING DISPLAY COMMENT

TRMSULF....................... S S TESTING DISPLAY COMMENT

GENTMCN....................... I I TESTING DISPLAY COMMENT

CEPHALOTHIN................... I I TESTING DISPLAY COMMENT

\+ + + + + + + + + + End of Report + + + + + + + + + + End of Report + + +

HXX,PXXXXXX XXX-XX-XXXX ROUTING: MICU

'^' TO STOP

Do you want to APPROVE these results? NO// <span class="mark">y</span> YES

Current performing lab assignments:

Bacteriology Report Performed By: ZZ BONHAM

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">1</span> Entire report

Select Performing Laboratory: ZZ BONHAM// TX VAMC 522 INACTIVE Jan 01, 1997

Sure you want to update this record? NO// <span class="mark">y</span> YES

... assignment updated.

Current performing lab assignments:

Bacteriology Report Performed By: <span class="mark">ZZ BONHAM</span>

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for:

Enter Accession number part: 29// <span class="mark">^</span>

EA Enter/verify data (auto instrument)

EL Enter/verify data (Load list)

EM Enter/verify/modify data (manual)

EW Enter/verify data (Work list)

GA Group verify (EA, EL, EW)

MP Misc. Processing Menu ...

Accession order then immediately enter data

Batch data entry (chem, hem, tox, etc.)

Build a load/work list

Bypass normal data entry

Fast Bypass Data Entry/Verify

Lookup accession

Order/test status

Print a load/work list

Std/QC/Reps Manual Workload count

Unload Load/Work List

Select Process data in lab menu Option:

> **NOTE:** Lab Techs. May view an interim report when the interim report is verified using EA. The results are then viewable via lab interim reports and CPRS.

# Use of the LEDI IV Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Laboratory New Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/020.png) | NOTE: For LIMs and IRM personnel, follow the Installation steps in the *LEDI IV Install Guide* prior to using this software: <http://www.va.gov/vdl/application.asp?appid=75> |

The following new menus accommodate the new LEDI IV functionality.

### New Laboratory Menu—Lab Code Mapping File Menu \[LA7V 62.47 MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Code Mapping File menu \[LA7V 62.47 MENU\] is the main menu that allows access to the LAB CODE MAPPING file (#62.47). This menu is located on the Lab Shipping Management Menu \[LA7S MGR MENU\]. This menu gets used for preparation for conversion to the Laboratory System.

<span id="_Toc510168959" class="anchor"></span>Figure 18. Lab Code Mapping File menu \[LA7V 62.47 MENU\] options Select Lab Shipping Management Menu Option: LAB CODE MAPPING FILE

AEL Add/Edit Local Identifier

CMC Clone a Message Configuration

CSM Code/Set Mismatches

DOD Initialize DOD Codes

ECH Error Code Help

ES Edit Susceptibility

FI Find Identifier

MAS Map All Susceptibilities

PL Print Local Codes

PMC Print by Message Configuration

PS Print Susceptibilities

## Parameters and Hierarchies with LEDI IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the parameters that are new with LEDI IV. These parameters can be edited using one of these three options:

Package Level Parameter Edit \[LR7O PAR PKG\] NOTE: There is a restriction on which user level at each site is allowed to edit Package Level Parameters.

Domain Level Parameter Edit, The Domain Level Option is used to modify Division Level Parameters \[LR7O PAR DOMAIN\].

General Lab User Parameters \[LR USER PARAM\].

### Parameter Precedence Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single parameter may be set for several different types of entities. The Precedence Order lists the order in which entities are searched for a defined value.

For example, if a parameter may be set for a Package, a Division, and a User and the respective precedents are 3, 2, 1, the value of the User parameter would be used. If it did not exist, then the value of the Division parameter would be used. If that did not exist, then the value of the Package parameter would be used.

The table below provides the Parameters that are new and accessible by the users with the LEDI IV patch. The display text, parameter name, description and precedence order are all included.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 47%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Display Text</th>
<th>Name</th>
<th>Description</th>
<th>Precedence Order</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Default manual verify method</td>
<td>LR VER EM VERIFY BY UID</td>
<td><p>Used to designate the default verification method presented to the user when verifying laboratory results in the "CH" subscript via options <strong>that do not use a load/work list</strong>. Parameter can be set at the package, division or user level. Division level takes precedence over the package level. User level takes precedence over division level. Site can also force verification by UID only.</p>
<p>The available values that can be selected are: Accession number, UID (Unique Identifier) and only UID.</p></td>
<td><ol type="1">
<li><p>User</p></li>
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Default load/work list verify method</td>
<td>LR VER EA VERIFY BY UID</td>
<td><p>Used to designate the default verification method presented to the user when verifying laboratory results in the "CH" subscript via options <strong>that use a load/work list.</strong> Parameter is associated with the accession area linked to the load/worklist profile selected by the user.</p>
<p>Parameter can be set at the package or user level. User level takes precedence over package level.</p>
<p>The available values that can be selected are: Accession number, UID (Unique Identifier) and only UID.</p></td>
<td><ol type="1">
<li><blockquote>
<p>User</p>
</blockquote></li>
</ol>
<ol start="4" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Display Provider in Micro Result Entry</td>
<td>LR MI VERIFY DISPLAY PROVIDER</td>
<td><p>This parameter allows the site/division/user to indicate if the ordering provider information should be displayed to the user during microbiology result data entry. The information displayed to the user is:</p>
<ul>
<li><p>Provider Name</p></li>
<li><p>Voice Pager</p></li>
<li><p>Office Phone</p></li>
<li><p>Digital Pager</p></li>
</ul></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="5" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Prompt CPRS Alert in Micro Result Entry</td>
<td>LR MI VERIFY CPRS ALERT</td>
<td><p>Used to allow the user to determine if they want to be prompted to send a CPRS alert after editing a microbiology accession.</p>
<p>The user can indicate:</p>
<p>They do not want to be asked</p>
<p>The user can request that they be asked and have the default prompt to be set to NO, or</p>
<p>The user can request to be asked and have the default prompt to be set to Yes.</p>
<p>The default Package level setting is ‘Don’t Ask’.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="7" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>EGFR Creatinine IDMS-traceable Method</td>
<td>LR EGFR METHOD</td>
<td>Used to designate if the EGFR calculation should calculate the EGFR based on an IDMS-traceable method. This parameter is configurable at both the package and division level.</td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="9" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>EGFR Patient's Age Cutoff</td>
<td>LR EGFR AGE CUTOFF</td>
<td>Used to designate if the EGFR calculation should not be performed on creatinine when executing the delta check EGFR when the patient's age is &lt;18 or &gt;70. This parameter is configurable at both the Package and division level and can be set for either or both age cutoffs</td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="10" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>EGFR Result Cutoff</td>
<td>LR EGFR RESULT SUPPRESS</td>
<td>Used to designate if the EGFR calculation should be suppressed when the value is &gt;60. If enabled then "&gt;60" is reported in lieu of the actual EGFR calculated value. This parameter is configurable at both the package and division level.</td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="11" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Send an alert after AP release</td>
<td>LRAPRES1 AP ALERT</td>
<td><p>After Anatomic Pathology report is released, this will be the default answer to the "Send an alert" message.</p>
<p>The default Package level setting is ‘NO’.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="12" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Default AP Report Selection Prompt</td>
<td>LR AP REPORT SELECTION</td>
<td>Allows the package/facility/user to set a default report selection method to present to the user.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="14" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Ask Performing Lab AP</td>
<td>LR ASK PERFORMING LAB AP</td>
<td><p>Enter YES to be prompted for Performing Lab.</p>
<p>Enter NO to <em>not</em> be prompted for Performing Lab.</p>
<p>If the user chooses not to be prompted for performing laboratory, the system will assign the performing laboratory based on the user's Default Performing Laboratory parameter and if the parameter is not set for the user, it defaults to the user's Institution (DUZ(2)).</p>
<p>The default Package level setting is ‘YES’.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="16" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Ask Performing Lab Micro</td>
<td>LR ASK PERFORMING LAB MICRO</td>
<td><p>Enter YES to be prompted for Performing Lab.</p>
<p>Enter NO to <em>not</em> be prompted for Performing Lab.</p>
<p>If the user chooses not to be prompted for performing laboratory, the system will assign the performing laboratory based on the user's 'Default Performing Laboratory' parameter and if the parameter is not set for the user, it defaults to the user's Institution (DUZ(2)).</p>
<p>The default Package level setting is ‘YES’.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="18" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Print SNOMED Code System</td>
<td>LR AP SNOMED SYSTEM PRINT</td>
<td><p>Parameter to allow the site/division to indicate which version of SNOMED to print or display on Anatomic Pathology reports.</p>
<p>The default Package level setting is ‘SNOMED I’.</p></td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="20" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Document Surgery Package Case Info</td>
<td>LR AP SURGERY REFERENCE</td>
<td><p>Allows site/division to indicate when copying surgical case information from the Surgery package during surgical pathology login if a statement is also added to the copied information documenting the source of the copied information.</p>
<p>The default Package level setting is ‘NO’.</p></td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="21" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Chemistry GUI Report Right Margin</td>
<td>LR CH GUI REPORT RIGHT MARGIN</td>
<td>This is the value to use for the right margin (column) when formatting chemistry/hematology type laboratory reports within a GUI display/client.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="22" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Microbiology GUI Report Right Margin</td>
<td>LR MI GUI REPORT RIGHT MARGIN</td>
<td>This is the value to use for the right margin (column) when formatting microbiology type laboratory reports within a GUI display/client.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="24" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>AP GUI Report Right Margin</td>
<td>LR AP GUI REPORT RIGHT MARGIN</td>
<td>This is the value to use for the right margin (column) when formatting anatomic pathology type laboratory reports within a GUI display/client.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="26" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Method of Assigning AP Accession Number</td>
<td>LR AP DEFAULT ACCESSION NUMBER</td>
<td>When an Anatomic Pathology (AP) case is accessioned, this parameter will control how the system should assign a default accession number to the case being logged in. (Note: The user will still be able to override the default, and select a different accession number, if they so choose). The user can select to keep the Accession default as it is. Or, they can set system to search from the beginning (#1). The first available accession number found in that accession area will be used as the default accession number for the new case being logged in.</td>
<td><ol type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Default Accessioning Specimen</td>
<td>LR ACCESSION DEFAULT SPECIMEN</td>
<td>Allows the package/facility/user to set a default topography presented to the user when accessioning specimens into the Laboratory system.</td>
<td><ol type="1">
<li><blockquote>
<p>User</p>
</blockquote></li>
</ol>
<ol start="28" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Default Accessioning Collection Sample</td>
<td>LR ACCESSION DEFAULT COL SAMP</td>
<td>Allows the package/facility/user to set a default collection sample presented to the user when accessioning specimens into the Laboratory system.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="30" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Default Accessioning Lab Test</td>
<td>LR ACCESSION DEFAULT LAB TEST</td>
<td>Allows the package/facility/user to set a default laboratory test presented to the user when accessioning specimens into the Laboratory system.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="32" type="1">
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Exclude removed tests from building</td>
<td>LR MANIFEST EXC PREV TEST</td>
<td>Allows package or user to select the default value presented to the user when building a shipping configuration to the prompt "Exclude previously removed tests from building?"</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="34" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Use default accession dates</td>
<td>LR MANIFEST DEFLT ACCESSION</td>
<td>Allows package or user to select the default value presented to the user when building a shipping configuration to the prompt "Use default accession dates?"</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="35" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Default to create new manifest</td>
<td>LR MANIFEST DEFLT CREATE</td>
<td>Allows package or user to determine the default response when prompted to create a shipping manifest at the "There is not an open shipping manifest for [shipping configuration] Do you want to start one?" prompt.</td>
<td><ol type="1">
<li><p>User</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Print Reporting/Printing Facility</td>
<td>LR REPORTS FACILITY PRINT</td>
<td><p>Determines if the name and address of the:</p>
<p>Laboratory that is responsible for the report display on the Laboratory report.</p>
<p>Facility where the report is printed display on the Laboratory report.</p>
<p>Both names display on the Laboratory report.</p>
<p>The default Package level setting is ‘None’.</p>
<p><strong>NOTE:</strong> Setting of the Print Reporting /Printing</p>
<p>Facility is not fully functional for Multi-Divisional</p>
<p>sites. It also has no impact on the Performing</p>
<p>Lab that displays in CPRS.</p></td>
<td><ol type="1">
<li><p>Division</p></li>
</ol>
<ol start="36" type="1">
<li><p>Package</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Lab STS Default Mapping Files Directory</td>
<td>LR MAPPING DEFAULT DIRECTORY</td>
<td><p>This parameter holds the name of the default directory, which contains the STS mapping of standard code sets to VistA Laboratory system files.</p>
<p>Should be expressed as a full directory specification.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="37" type="1">
<li><p>Package</p></li>
<li><p>System</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Lab STS Default Mapping Filespec</td>
<td>LR MAPPING DEFAULT FILESPEC</td>
<td><p>This parameter holds the file specification used to screen which files is a given directory are presented to the user for loading. These files contain the STS mapping of standard code sets to VistA Laboratory system files.</p>
<p>The default Package level setting is ‘*.TXT’.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="39" type="1">
<li><p>Package</p></li>
<li><p>System</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Default lab label printer</td>
<td>LR LABEL PRINTER DEFAULT</td>
<td>Allows selection of default lab label printer presented to the user when selecting the label device to use to print accession and order labels. User can specify default printer by division.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Default Performing Laboratory</td>
<td>LR VER DEFAULT PERFORMING LAB</td>
<td>Allows the user to designate a default performing lab that is presented to the user when specifying the performing lab. Normally the lab software defaults to the user's institution. This parameter allows the user to specify a different institution.</td>
<td><ol type="1">
<li><p>User</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Lab Messaging - Parse HL7 Messages</td>
<td>LA7UTILA PARSE</td>
<td><p>Allows the User to select the default setting for "Parse HL7 Message" prompt when using [LA7 PRINT LAB UI MESSAGE].</p>
<p>"LAST" means the user wants the system to keep track of their last response to this prompt and use that as their default.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="41" type="1">
<li><p>System</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Lab Messaging - Display using Browser</td>
<td>LA7UTILA USE BROWSER</td>
<td><p>Allows the User to select the default setting for the "Use Browser to display HL7 Message" prompt when using [LA7 PRINT LAB UI MESSAGE].</p>
<p>"LAST" means the User wants the system to keep track of their last response to this prompt and use that as their default.</p></td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="42" type="1">
<li><p>System</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Lab Messaging - Show Identifiers</td>
<td>LA7UTILA SHOIDS</td>
<td>Allows the user to select the default setting for the "Display identifiers during message selection?" prompt when using [LA7 PRINT LAB UI MESSAGE].</td>
<td><ol type="1">
<li><p>User</p></li>
</ol>
<ol start="43" type="1">
<li><p>System</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Prompt CPRS Alert in CH Result Entry</td>
<td>LR CH VERIFY CPRS ALERT</td>
<td><p>Used to allow the user to determine if they want to be prompted to send a CPRS alert after editing a Chem/Heme accession.</p>
<p> The user can indicate:</p>
<ul>
<li><blockquote>
<p>They do not want to be asked</p>
</blockquote></li>
<li><blockquote>
<p>The user can request that they be asked and have the default prompt to be set to NO,</p>
</blockquote></li>
<li><blockquote>
<p>The user can request to be asked and have the default prompt to be set to Yes.</p>
</blockquote></li>
</ul></td>
<td><ol type="1">
<li><p>User</p></li>
<li><p>Division</p></li>
<li><p>Package</p></li>
</ol></td>
</tr>
</tbody>
</table>

### Package Level Parameter Edit \[LR70 PAR PKG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Package Level Parameter Setup should be performed by the LIM. The option Package Level Parameter Edit \[LR7O PAR PKG\] specifies LAB package settings for the new parameters introduced with LEDI IV (see list below). The Lab LIM should configure these as appropriate for their package. The option is located on the Update CPRS Parameters menu \[LR7O PARAM MENU\].

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/021.png) | NOTE: During data entry, the LIM can enter two question marks next to a field and VistA provides a short explanation of the parameter. |

Default manual verify method.

Default load/work list verify method.

Display Provider in Micro Result Entry.

Prompt CPRS Alert in Micro Result Entry.

Prompt CPRS Alert in CH Result Entry.

EGFR Creatinine IDMS-traceable Method.

EGFR Patient's Age Cutoff.

EGFR Result Cutoff.

Send an alert after AP release.

Default AP Report Selection Prompt.

Ask Performing Lab AP.

Ask Performing Lab Micro.

Print SNOMED Code System.

Document Surgery Package Case Info.

Chemistry GUI Report Right Margin.

Microbiology GUI Report Right Margin.

AP GUI Report Right Margin.

Method of Assigning AP Accession Number.

Default Accessioning Specimen.

Default Accessioning Collection Sample.

Default Accessioning Lab Test.

Exclude removed tests from building.

Use default accession dates.

Default to create new manifest.

Print Reporting/Printing Facility.

Lab STS Default Mapping Files Directory.

Lab STS Default Mapping Filespec.

<span id="_Ref509818519" class="anchor"></span>Figure 19. Package Level Parameter Edit \[LR7O PAR PKG\]

Select Laboratory DHCP Menu Option: <span class="mark">SUPER \<ENTER\></span> visor menu

Select Supervisor menu Option: <span class="mark">LAB LIA \<ENTER\></span> ison menu

Select Lab liaison menu Option: <span class="mark">OE/RR \<ENTER\></span> interface parameters

Select OE/RR interface parameters Option: <span class="mark">CC \<ENTER\></span> Update CPRS Parameters

Select Update CPRS Parameters Option: <span class="mark">?</span>

   PA     Update CPRS with Lab order parameters

   SI     Update CPRS with Single Lab test

   UP     Update CPRS with all Lab test parameters

   DO     Domain Level Parameter Edit

   LO     Location Level Parameter Edit

   PP     Package Level Parameter Edit

   UL     Display Lab User Parameters

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Update CPRS Parameters Option: <span class="mark">PP\<ENTER\></span> Package Level Parameter Edit

Lab Package Level Parameters for Package: <span class="mark">LAB SERVICE</span>

------------------------------------------------------------------------------

Collect on Monday                                 YES

Collect on Tuesday                                YES

Collect on Wednesday                              YES

Collect on Thursday                               YES

Collect on Friday                                 YES

Collect on Saturday                               NO

Collect on Sunday                                 NO

Lab Collects on Holidays                          YES

Lab Collect Days Allowed in Future                365

Maximum Days for Continuous Orders                270

Default manual verify method                     

Default load/work list verify method

Display Provider in Micro Result Entry           

Prompt CPRS Alert in Micro Result Entry           Don't Ask

Prompt CPRS Alert in CH Result Entry             

EGFR Creatinine IDMS-traceable Method            

EGFR Patient's Age Cutoff                        

EGFR Result Cutoff                               

Send an alert after AP release                   

Default AP Report Selection Prompt               

Ask Performing Lab AP                             YES

Ask Performing Lab Micro                          YES

Print SNOMED Code System                          SNOMED I

Document Surgery Package Case Info               

Chemistry GUI Report Right Margin                

Microbiology GUI Report Right Margin             

AP GUI Report Right Margin

Method of Assigning AP Accession Number                       

Default Accessioning Specimen

Default Accessioning Collection Sample

Default Accessioning Lab Test

Exclude removed tests from building

Use default accession dates

Default to create new manifest

Print Reporting/Printing Facility                 None

Lab STS Default Mapping Files Directory          

Lab STS Default Mapping Filespec                  \*.TXT

------------------------------------------------------------------------------

COLLECT MONDAY: YES// <span class="mark">\<ENTER\></span>

COLLECT TUESDAY: YES// <span class="mark">\<ENTER\></span>

COLLECT WEDNESDAY: YES// <span class="mark">\<ENTER\></span>

COLLECT THURSDAY: YES// <span class="mark">\<ENTER\></span>

COLLECT FRIDAY: YES// <span class="mark">\<ENTER\></span>

COLLECT SATURDAY: NO// <span class="mark">\<ENTER\></span>

COLLECT SUNDAY: NO// <span class="mark">\<ENTER\></span>

IGNORE HOLIDAYS: YES// <span class="mark">\<ENTER\></span>

LAB COLLECT DAYS ALLOWED IN FUTURE: 365// <span class="mark">\<ENTER\></span>

MAXIMUM DAYS FOR CONTINUOUS ORDERS: 270// <span class="mark">\<ENTER\></span>

Default manual verify method: <span class="mark">\<ENTER\></span>

For Default load/work list verify method -

Select Accession Area: <span class="mark">\<ENTER\></span>

Display Provider in Micro Result Entry: <span class="mark">\<ENTER\></span>

Send CPRS Alert in Micro Result Entry: Don't Ask// <span class="mark">\<ENTER\></span>

Send CPRS Alert in CH Result Entry: <span class="mark">\<ENTER\></span>

Creatinine IDMS-traceable Method: <span class="mark">\<ENTER\></span>

Suppress EGFR When Patient's Age: <span class="mark">\<ENTER\></span>

Report EGFR as \>60: <span class="mark">\<ENTER\></span>

Send alert for released AP: <span class="mark">\<ENTER\></span>

AP Report Selection Default: <span class="mark">\<ENTER\></span>

Ask Performing Lab AP: YES// <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Anatomic Pathology tests.

Ask Performing Lab AP: YES// <span class="mark">\<ENTER\></span>

Ask Performing Lab for MICRO: YES// <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Microbiology tests.

Ask Performing Lab for MICRO: YES// <span class="mark">\<ENTER\></span>

Print SNOMED Version: SNOMED I// <span class="mark">\<ENTER\></span>

Document Surgery Case Info: <span class="mark">\<ENTER\></span>

Chemistry GUI Report Right Margin: <span class="mark">\<ENTER\></span>

Microbiology GUI Report Right Margin: <span class="mark">\<ENTER\></span>

AP GUI Report Right Margin: <span class="mark">\<ENTER\></span>

For Default Accessioning Specimen -

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Collection Sample -

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Lab Test -

Select Lab Section: <span class="mark">\<ENTER\></span>

For Exclude removed tests from building -

Select Shipping Configuration: <span class="mark">\<ENTER\></span>

For Use default accession dates -

Select Shipping Configuration: <span class="mark">\<ENTER\></span>

For Default to create new manifest -

Select Shipping Configuration: <span class="mark">\<ENTER\></span>

Print Reporting/Printing Facility: None// <span class="mark">\<ENTER\></span>

Default Directory: <span class="mark">?</span>

The directory that contains the STS mapping files.

Default Directory: <span class="mark">\<ENTER\></span>

Default FileSpec: \*.TXT// <span class="mark">\<ENTER\></span>

Select Update CPRS Parameters Option:

### General Lab User Parameters \[LR User Param\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General Lab user parameter setup should be performed by the Lab users. The General Lab User Parameters \[LR USER PARAM\] option specifies user level default settings that a user can set to override corresponding package or domain level parameters for these settings (see list below). This option is located on the Information-help menu \[LRHELP\].

|                                                   |                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/022.png) | NOTE: During data entry, the LIM can type in two question marks next to a field and VistA provides a short explanation of the parameter. |

Default lab label printer.

Display previous comments for test.

Default Performing Laboratory.

Ask Performing Lab AP.

Ask Performing Lab Micro.

Display Provider in Micro Result Entry.

Prompt CPRS Alert in CH Result Entry.

Prompt CPRS Alert in Micro Result Entry.

Default AP Report Selection Prompt.

Send an alert after AP release.

Default Accessioning Specimen.

Default Accessioning Collection Sample.

Default Accessioning Lab Test.

Exclude removed tests from building.

Use default accession dates.

Lab Messaging - Parse HL7 Messages.

Lab Messaging - Display using Browser.

Lab Messaging - Show Identifiers.

Chemistry GUI Report Right Margin.

Microbiology GUI Report Right Margin.

AP GUI Report Right Margin.

Lab STS Default Mapping Files Directory.

Lab STS Default Mapping Filespec.

<span id="_Toc510168961" class="anchor"></span>Figure 20. General Lab User Parameters \[LR USER PARAM\]

Select OPTION NAME: <span class="mark">LRMENU \<ENTER\></span> Laboratory DHCP Menu

Select Laboratory DHCP Menu Option: <span class="mark">?</span>

1 Phlebotomy menu ...

2 Accessioning menu ...

3 Process data in lab menu ...

4 Quality control menu ...

5 Results menu ...

6 Information-help menu ...

7 Ward lab menu ...

8 Anatomic pathology ...

9 Blood bank ...

10 Microbiology menu ...

11 Supervisor menu ...

LSM Lab Shipping Menu ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Laboratory DHCP Menu Option: <span class="mark">6 \<ENTER\></span> Information-help menu

Select Information-help menu Option: <span class="mark">PP \<ENTER\></span> General Lab User Parameters

Lab User Level Parameters for User: <span class="mark">LRUSER,TWO</span>

------------------------------------------------------------------------------

Default lab label printer

Display previous comments for test

Default Performing Laboratory

Ask Performing Lab AP

Ask Performing Lab Micro

Display Provider in Micro Result Entry

Prompt CPRS Alert in CH Result Entry

Prompt CPRS Alert in Micro Result Entry

Default AP Report Selection Prompt

Send an alert after AP release

Default Accessioning Specimen

Default Accessioning Collection Sample

Default Accessioning Lab Test

Exclude removed tests from building

Use default accession dates

Lab Messaging - Parse HL7 Messages

Lab Messaging - Display using Browser

Lab Messaging - Show Identifiers

Chemistry GUI Report Right Margin

Microbiology GUI Report Right Margin

AP GUI Report Right Margin

Lab STS Default Mapping Files Directory USER\$:\[LRUSERT\]

Lab STS Default Mapping Filespec

------------------------------------------------------------------------------

For Default lab label printer -

Select Division: <span class="mark">?</span>

There are currently no entries for Division.

Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

OFFICIAL VA NAME, or CURRENT LOCATION, or CODING SYSTEM/ID PAIR, or

NPI, or STATUS, or NAME (CHANGED FROM), or CODING SYSTEM

Do you want the entire INSTITUTION List? <span class="mark">Y \<ENTER\></span> (Yes)

Choose from: ... *Editor Note: List of Institutions displays.*

Select Division: <span class="mark">\<ENTER\></span>

For Display previous comments for test -

Select Laboratory Test: <span class="mark">?</span>

There are currently no entries for Laboratory Test.

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or

PRINT NAME

Do you want the entire LABORATORY TEST List? <span class="mark">Y \<ENTER\></span> (Yes)

Choose from:

1,25-DIHYDROXYVIT D3 1,25-DI

1/2HR LTT 1/2HR L

1/2Hr.GTT 1/2Hr.G

1/2Hr.GTT (URINE) 1/2Hr.G

11-DEOXYCORTISOL 11-DEOX

17-HYDROXYCORTICOSTEROIDS 17-HYDR

1HR LTT 1HR LTT

1Hr.GTT 1Hr.GTT

1Hr.GTT (URINE) 1Hr.GTT

25 OH VITAMIN D 25 OH V

2HR LTT 2HR LTT

2Hr.GTT 2Hr.GTT

2Hr.GTT (URINE) 2Hr.GTT

3HR LTT 3HR LTT

3Hr.GTT 3Hr.GTT

3Hr.GTT (URINE) 3Hr.GTT

4Hr.GTT 4Hr.GTT

4Hr.GTT (URINE) 4Hr.GTT

5' NUCLEOTIDASE 5' N

5Hr.GTT 5Hr.GTT

<span class="mark">^</span>

Select Laboratory Test: <span class="mark">\<ENTER\></span>

Default Performing Laboratory: <span class="mark">?</span>

Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

OFFICIAL VA NAME, or CURRENT LOCATION, or CODING SYSTEM/ID PAIR, or

NPI, or STATUS, or NAME (CHANGED FROM), or CODING SYSTEM

Do you want the entire INSTITUTION List? <span class="mark">Y \<ENTER\></span> (Yes)

Choose from:

DOD-SAIC CA

LAB RE-ENGINEERING - REGION 1 TX OTHER 200LR1

LABORATORY CORPORATION NC

MILWAUKEE VAMC WI VAMC 695

REGION 7 ISC,TX (FS) TX 170

TRIPLER ARMY MEDICAL CENTER HI USAH 459CN

ZZ BONHAM TX VAMC 522 INACTIVE Jan 01, 1997

Default Performing Laboratory: <span class="mark">\<ENTER\></span>

Ask Performing Lab AP: <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Anatomic Pathology tests.

Ask Performing Lab AP: <span class="mark">\<ENTER\></span>

Ask Performing Lab for MICRO: <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Microbiology tests.

Ask Performing Lab for MICRO: <span class="mark">\<ENTER\></span>

Display Provider in Micro Result Entry: <span class="mark">?</span>

Enter yes/no to display ordering provider information during micro

result entry.

Display Provider in Micro Result Entry: <span class="mark">\<ENTER\></span>

Send CPRS Alert in CH Result Entry: <span class="mark">?</span>

Specify if user should be prompted to send a CPRS Alert.

Select one of the following:

0 Don't Ask

1 Ask - Default NO

2 Ask - Default YES

Send CPRS Alert in CH Result Entry: <span class="mark">\<ENTER\></span>

Send CPRS Alert in Micro Result Entry: <span class="mark">?</span>

Specify if user should be prompted to send a CPRS Alert.

Select one of the following:

0 Don't Ask

1 Ask - Default NO

2 Ask - Default YES

Send CPRS Alert in Micro Result Entry: <span class="mark">\<ENTER\></span>

AP Report Selection Default: <span class="mark">?</span>

Specify the default report selection method presented to user.

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

3 Patient Name

AP Report Selection Default: <span class="mark">\<ENTER\></span>

Send alert for released AP: <span class="mark">?</span>

Enter either 'Y' or 'N'.

Send alert for released AP: <span class="mark">\<ENTER\></span>

For Default Accessioning Specimen -

Select Lab Section: <span class="mark">?</span>

There are currently no entries for Lab Section.

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire ACCESSION List? y (Yes)

Choose from:

CYTOPATHOLOGY

CYTOPATHOLOGY-GYN

EM

SURGICAL PATHOLOGY

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Collection Sample -

Select Lab Section: <span class="mark">?</span>

There are currently no entries for Lab Section.

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire ACCESSION List? <span class="mark">y</span> (Yes)

Choose from:

CYTOPATHOLOGY

CYTOPATHOLOGY-GYN

EM

SURGICAL PATHOLOGY

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Lab Test -

Select Lab Section: <span class="mark">?</span>

There are currently no entries for Lab Section.

Answer with ACCESSION AREA, or UID, or HOST UID

Do you want the entire ACCESSION List? y (Yes)

Choose from:

CYTOPATHOLOGY

CYTOPATHOLOGY-GYN

EM

SURGICAL PATHOLOGY

Select Lab Section: <span class="mark">\<ENTER\></span>

For Exclude removed tests from building -

Select Shipping Configuration: <span class="mark">?</span>

There are currently no entries for Shipping Configuration.

Answer with LAB SHIPPING CONFIGURATION NAME, or COLLECTING FACILITY, or

HOST FACILITY'S SYSTEM, or COLLECTING FACILITY'S SYSTEM

Do you want the entire LAB SHIPPING CONFIGURATION List? <span class="mark">y</span> (Yes)

Choose from:

CERNER \#1

DOD HOST

LABCORP

LEDI HOST LAB

MHC TO VRR

TRIPLER AMC

Select Shipping Configuration: <span class="mark">\<ENTER\></span>

For Use default accession dates -

Select Shipping Configuration: <span class="mark">?</span>

There are currently no entries for Shipping Configuration.

Answer with LAB SHIPPING CONFIGURATION NAME, or COLLECTING FACILITY, or

HOST FACILITY'S SYSTEM, or COLLECTING FACILITY'S SYSTEM

Do you want the entire LAB SHIPPING CONFIGURATION List? <span class="mark">y</span> (Yes)

Choose from:

CERNER \#1

DOD HOST

LABCORP

LEDI HOST LAB

MHC TO VRR

TRIPLER AMC

Select Shipping Configuration: <span class="mark">\<ENTER\></span>

Lab Messaging - Parse HL7 Messages: <span class="mark">?</span>

Enter a code from the list.

Select one of the following:

Y YES

N NO

L LAST

Lab Messaging - Parse HL7 Messages: <span class="mark">\<ENTER\></span>

Lab Messaging - Use Browser to display: <span class="mark">?</span>

Enter a code from the list.

Select one of the following:

Y YES

N NO

L LAST

Lab Messaging - Use Browser to display: <span class="mark">\<ENTER\></span>

Lab Messaging - Show Identifiers: <span class="mark">?</span>

Enter a code from the list.

Select one of the following:

Y YES

N NO

L LAST

Lab Messaging - Show Identifiers: <span class="mark">\<ENTER\></span>

Chemistry GUI Report Right Margin: <span class="mark">?</span>

Enter the value to be used (132) for the right margin when formatting lab

reports.

Chemistry GUI Report Right Margin: <span class="mark">\<ENTER\></span>

Microbiology GUI Report Right Margin: <span class="mark">?</span>

Enter the value to be used (132) for the right margin when formatting lab reports.

Microbiology GUI Report Right Margin: <span class="mark">\<ENTER\></span>

AP GUI Report Right Margin: <span class="mark">?</span>

Enter the value to be used (132) for the right margin when formatting lab reports.

AP GUI Report Right Margin: <span class="mark">\<ENTER\></span>

Default Directory: USER\$:\[LRUSERT\]// <span class="mark">?</span>

The directory that contains the STS mapping files.

Default Directory: USER\$:\[LRUSERT\]// <span class="mark">\<ENTER\></span>

Default FileSpec: <span class="mark">?</span>

The filespec to screen the display of files.

Default FileSpec: <span class="mark">\<ENTER\></span>

Select Information-help menu Option: Select Laboratory DHCP Menu Option:

### Domain Level Parameter Edit \[LR70 PAR DOMAIN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the option Domain Level Parameter Edit \[LR7O PAR DOMAIN\] to edit the parameters at the Division level. The LIM performs the Domain Level Parameter Edit to configure the parameters appropriately for their system. The Domain Level Parameter Edit \[LR7O PAR DOMAIN\] specifies Division level settings that can be set to override corresponding Package level settings for the following parameters.

|                                                   |                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/023.png) | NOTE: During data entry, the LIM can type in two question marks next to a field and VistA provides a short explanation of the parameter. |

- Lab Collect Days Allowed in Future.               
- Default manual verify method.                     
- Default load/work list verify method.
- EGFR Creatinine IDMS-traceable Method.            
- EGFR Patient's Age Cutoff.                        
- EGFR Result Cutoff.                                
- Default AP Report Selection Prompt.               
- Ask Performing Lab AP.                           
- Ask Performing Lab Micro.                         
- Print SNOMED Code System.                         
- Document Surgery Package Case Info.               
- Default Accessioning Specimen.
- Default Accessioning Collection Sample.
- Default Accessioning Lab Test.
- Display Provider in Micro Result Entry.           
- Prompt CPRS Alert in Micro Result Entry.          
- Prompt CPRS Alert in CH Result Entry.             
- Chemistry GUI Report Right Margin.                
- Microbiology GUI Report Right Margin.             
- AP GUI Report Right Margin.                       
- Print Reporting/Printing Facility.   

<span id="_Toc510168962" class="anchor"></span>Figure 21. Domain Level Parameter Edit \[LR7O PAR DOMAIN\]

Select Laboratory DHCP Menu Option: <span class="mark">SUPER \<ENTER\></span> visor menu

Select Supervisor menu Option: <span class="mark">LAB LIA \<ENTER\></span> ison menu

Select Lab liaison menu Option: <span class="mark">OE/RR \<ENTER\></span> interface parameters

Select OE/RR interface parameters Option: <span class="mark">CC \<ENTER\></span> Update CPRS Parameters

Select Update CPRS Parameters Option: <span class="mark">?</span>

   PA     Update CPRS with Lab order parameters

   SI     Update CPRS with Single Lab test

   UP     Update CPRS with all Lab test parameters

   DO     Domain Level Parameter Edit

   LO     Location Level Parameter Edit

   PP     Package Level Parameter Edit

   UL     Display Lab User Parameters

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Update CPRS Parameters Option: <span class="mark">DO \<ENTER\></span> Domain Level Parameter Edit

Select INSTITUTION NAME: <span class="mark">ZZ BONHAM \<ENTER\></span>       TX  VAMC      522      INACTIVE Jan 01, 1997

Lab Domain Level Parameters for Division: ZZ BONHAM

------------------------------------------------------------------------------

Phlebotomy Collection Time    27000               0800

                              54000               1530

                              55200               1530

Lab Collect Days Allowed in Future               

Default manual verify method                     

Default load/work list verify method

EGFR Creatinine IDMS-traceable Method            

EGFR Patient's Age Cutoff                        

EGFR Result Cutoff                               

Default AP Report Selection Prompt               

Ask Performing Lab AP                             YES

Ask Performing Lab Micro                          YES

Print SNOMED Code System                          SNOMED I

Document Surgery Package Case Info               

Default Accessioning Specimen

Default Accessioning Collection Sample

Default Accessioning Lab Test

Display Provider in Micro Result Entry           

Prompt CPRS Alert in Micro Result Entry          

Prompt CPRS Alert in CH Result Entry             

Chemistry GUI Report Right Margin                

Microbiology GUI Report Right Margin             

AP GUI Report Right Margin                       

Print Reporting/Printing Facility                

------------------------------------------------------------------------------

For Phlebotomy Collection Time -

Select Instance: <span class="mark">\<ENTER\></span>

LAB COLLECT DAYS ALLOWED IN FUTURE: <span class="mark">\<ENTER\></span>

Default manual verify method: <span class="mark">\<ENTER\></span>

For Default load/work list verify method -

Select Accession Area: <span class="mark">\<ENTER\></span>

Creatinine IDMS-traceable Method: <span class="mark">\<ENTER\></span>

Suppress EGFR When Patient's Age: <span class="mark">\<ENTER\></span>

Report EGFR as \>60: <span class="mark">\<ENTER\></span>

AP Report Selection Default: <span class="mark">\<ENTER\></span>

Ask Performing Lab AP: YES// <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Anatomic Pathology tests.

Ask Performing Lab AP: YES// <span class="mark">\<ENTER\></span>

Ask Performing Lab for MICRO: YES// <span class="mark">?</span>

Enter yes to be prompted for Performing Lab for Microbiology tests.

Ask Performing Lab for MICRO: YES// <span class="mark">\<ENTER\></span>

Print SNOMED Version: SNOMED I// <span class="mark">\<ENTER\></span>

Document Surgery Case Info: <span class="mark">\<ENTER\></span>

For Default Accessioning Specimen -

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Collection Sample -

Select Lab Section: <span class="mark">\<ENTER\></span>

For Default Accessioning Lab Test -

Select Lab Section: <span class="mark">\<ENTER\></span>

Display Provider in Micro Result Entry: <span class="mark">\<ENTER\></span>

Send CPRS Alert in Micro Result Entry: <span class="mark">\<ENTER\></span>

Send CPRS Alert in CH Result Entry: <span class="mark">\<ENTER\></span>

Chemistry GUI Report Right Margin: <span class="mark">\<ENTER\></span>

Microbiology GUI Report Right Margin: <span class="mark">\<ENTER\></span>

AP GUI Report Right Margin: <span class="mark">\<ENTER\></span>

Print Reporting/Printing Facility: <span class="mark">\<ENTER\></span>

Select Update CPRS Parameters Option:

## New LEDI IV Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit an Antibiotic \[LRWU7 EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Antibiotic \[LRWU7 EDIT\] allows the editing of an existing bacterial antibiotic or mycobacterium antibiotic.

<span id="_Toc510168963" class="anchor"></span>Figure 22. Edit an Antibiotic \[LRWU7 EDIT\]

Select Lab liaison menu Option: <span class="mark">?</span>

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

File list for lab

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">EDIT AN ANTIBIOTIC</span>

Select one of the following:

1 Bacterial Antibiotic

2 Mycobacterium Antibiotic

Select Antibiotic Type to Edit: 1// <span class="mark">\<ENTER\></span> Bacterial Antibiotic

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: <span class="mark">PENICILLIN</span><span class="mark">\<ENTER\></span> PENICILLIN

NAME: PENICILLIN// <span class="mark">\<ENTER\></span>

INTERNAL NAME: PENICILLIN// <span class="mark">\<ENTER\></span>

DISPLAY COMMENT: <span class="mark">\<ENTER\></span>

ABBREVIATION: PEN// <span class="mark">\<ENTER\></span>

DEFAULT SCREEN: ALWAYS DISPLAY// <span class="mark">\<ENTER\></span>

PRINT ORDER: 23// <span class="mark">\<ENTER\></span>

Select SUSCEPTIBILITY RESULT: <span class="mark">\<ENTER\></span>

NATIONAL VA LAB CODE: Penicillin//

### Manage MI/AP Test Mappings \[LRCAPFF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In preparation for converting to the next LEDI patch, the Manage MI/AP Test Mappings \[LRCAPFF\] establishes the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests.

<span id="_Toc510168964" class="anchor"></span>Figure 23. Manage MI/AP Test Mappings \[LRCAPFF\]

Select LIM workload menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

Select National Laboratory File Option: <span class="mark">?</span>

   1      Semi-automatic Linking of file 60 to 64

   2      Manual Linking of file 60 to 64

   3      Result NLT Auto Linker

   4      Link Result NLT Manual

   5      Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<ENTER\></span> Manage MI/AP Test Mappings

     Select one of the following:

          MI        Microbiology

          SP        Surgical Pathology

          CY        Cytopathology

          EM        Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<ENTER\></span> Microbiology

Enter Laboratory Test Name: <span class="mark">GRAM STAIN \<ENTER\></span> GRAM ST

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Gram Stain// <span class="mark">\<ENTER\></span>

60 = GRAM STAIN  \[362\]

64 = Gram Stain (87754.0000)  \[2851\]

Link the two entries? No// Y <span class="mark">\<ENTER\></span> (Yes)

No Database Code on file for this NLT code

Select an MI Database Code: ?

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? Y (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY R

PT DATE DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: 9194 MI Gram Stain Rpt Date GENERAL GRAM ST

AIN DATANAME

Update complete.

### Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\] allows the user to add and edit local codes.

<span id="_Toc510168965" class="anchor"></span>Figure 24. Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]

Select Lab Code Mapping File Option: <span class="mark">ADD/EDIT LOCAL IDENTIFIER</span>

Select LAB CODE MAPPING CONCEPT: GRAM STAIN<span class="mark">\<ENTER\></span> MI Gram Stain Rpt Date

Select IDENTIFIER:0410.3 <span class="mark">\<ENTER\></span>99LAB

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

IDENTIFIER: 0410.3// <span class="mark">\<ENTER\></span>

CODING SYSTEM: 99LAB// <span class="mark">\<ENTER\></span>

PURPOSE: RESULT// <span class="mark">\<ENTER\></span>

OVERRIDE CONCEPT: <span class="mark">\<ENTER\></span>

RELATED ENTRY: <span class="mark">\<ENTER\></span>

MESSAGE CONFIGURATION: LA7V HOST 170// <span class="mark">\<ENTER\></span>

Select IDENTIFIER: <span class="mark">\<ENTER\></span>

Select LAB CODE MAPPING CONCEPT:

### Clone a Message Configuration \[LA7V 62.47 CLONE MSG CONFIG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Clone a Message Configuration \[LA7V 62.47 CLONE MSG CONFIG\] copies the entries of the source Message Configuration into entries for the destination message configuration. When local identifiers (codes) are added (using the Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]) those local codes are interface specific. This option allows a user to clone the local identifiers added for one Message Configuration to another. This is useful when setting up a new interface that uses similar local codes to an existing interface.

> <span id="_Toc510168966" class="anchor"></span>Figure 25. Clone a Message Configuration \[LA7V 62.47 CLONE MSG CONFIG\]

Select Lab Code Mapping File Option: <span class="mark">CLONE A MESSAGE CONFIGURATION</span>

Source Message Configuration: <span class="mark">LA7V HOST 981</span>

Destination Message Configuration: <span class="mark">LA7V HOST 0109</span>

Continue with cloning? ? N// <span class="mark">YES</span>

Records found: 1

Records added: 1

### Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Edit Susceptibility \[LA7V 62.47 EDIT SUSC\] links Bacteriology and Mycobacteria susceptibilities to existing codes.

<span id="_Toc510168967" class="anchor"></span>Figure 26. Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]

Select Lab Code Mapping File Option: <span class="mark">EDIT SUSCEPTIBILITY</span>

Select LAB CODE MAPPING CONCEPT: <span class="mark">BACTERIOLOGY SUSCEPTIBILITY MI \<ENTER\></span> Bacteria Susceptibility

Select IDENTIFIER: <span class="mark">29-9\<ENTER\></span> LN

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

AMPICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION

RELATED ENTRY: <span class="mark">AMPICILLIN</span>

Searching for a Select ANTIBIOTIC

AMPICILLIN AMPICILLIN

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Select IDENTIFIER:

### Find Identifier \[LA7V 62.47 FIND IDENTIFIER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Find Identifier \[LA7V 62.47 FIND IDENTIFIER\] searches the entire file for a particular identifier.

<span id="_Toc510168968" class="anchor"></span>Figure 27. Find Identifier \[LA7V 62.47 FIND IDENTIFIER\]

Select Lab Code Mapping File Option: <span class="mark">FIND IDENTIFIER</span>

Select IDENTIFIER: <span class="mark">0430.3</span>

... OK Yes// <span class="mark">\<ENTER\></span> YES 0430.3

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

LAB CODE MAPPING (0430.3) Sep 19, 2008@11:09:42 Page: 1

SEQ ID SYSTEM PURPOSE NATL

============================================================================

CONCEPT:MYCOLOGY SMEAR/PREP (MI)

2 0430.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

Select Lab Code Mapping File Option:

### Print by Msg Config \[LA7V 62.47 PRINT BY MSG CONFIG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print by Msg Config \[LA7V 62.47 PRINT BY MSG CONFIG\] displays entries in File \#62.47 by CONCEPT, sorted by the MESSAGE CONFIGURATION field.

<span id="_Toc510168969" class="anchor"></span>Figure 28. Print by Msg Config \[LA7V 62.47 PRINT BY MSG CONFIG\]

Select Lab Code Mapping File Option: <span class="mark">PMC \<ENTER\></span> Print by Message Configuration

Print All Message Configurations? ? N// <span class="mark">Y \<ENTER\></span> YES

DEVICE: HOME// <span class="mark">;;1000\<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

LAB CODE MAPPING (BY MSG CONFIG) Sep 02, 2008@16:14:49 Page: 1

SEQ ID SYSTEM PURPOSE NATL

============================================================================

CONCEPT:GRAM STAIN (MI)

2 0410.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:BACTERIA (MI)

1000004 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V COLLECTION 9999

1000002 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V HOST 170

1000003 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V HOST 9999

CONCEPT:BACTERIOLOGY REPORT (MI)

1000004 0410.2 99LAB RESULT NO

Msg Config: LA7V COLLECTION 9999

1000001 0410.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

1000003 0410.2 99LAB RESULT NO

Msg Config: LA7V HOST 9999

CONCEPT:PARASITE (MI)

28 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V COLLECTION 9999

26 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V HOST 170

27 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V HOST 9999

CONCEPT:PARASITE REPORT REMARK (MI)

2 0440.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:FUNGAL REPORT REMARK (MI)

2 0430.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:MYCOBACTERIA REPORT (MI)

2 0420.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:VIROLOGY REPORT (MI)

34 0450.1 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:MYCOLOGY SMEAR/PREP (MI)

2 0430.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:ACID FAST STAIN (MI)

3 0420.1 99LAB RESULT NO

Override Concept: BACTERIOLOGY REPORT

Msg Config: LA7V HOST 0052

CONCEPT:ACID FAST STAIN QUANTITY (MI)

2 0420.1 99LAB RESULT NO

Msg Config: LA7V HOST 170

### Code/Set Mismatches \[LA7V 62.47 PRINT CS MISMATCHES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Code/Set Mismatches LA7V 62.47 PRINT CS MISMATCHES\] displays entries in File \#62.47, where the Identifier/Coding System pairs are mismatched. It searches for Identifier (Code)/Coding System pairs and validates that the Code is valid for that Coding System. This option validates the Codes from the three Coding Systems listed below.

LOINC

SNOMED CT

NLT WKLD CODES

<span id="_Toc510168970" class="anchor"></span>Figure 29. Code/Set Mismatches \[LA7V 62.47 PRINT CS MISMATCHES\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">LCM \<ENTER\></span> Lab Code Mapping File

Select Lab Code Mapping File Option: <span class="mark">CSM \<ENTER\></span> Code/Set Mismatches

DEVICE: HOME// <span class="mark">\<ENTER\></span> TELNET PORT Right Margin: 80// <span class="mark">\<ENTER\></span>

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

LAB CODE MAPPING (CODE/SET MISMATCHES) Mar 15, 2012@09:20 Page: 1

SEQ ID SYSTEM PURPOSE NATL

============================================================================

CONCEPT:BACTERIA (MI)

1000042 1111222 LN RESULT NO

Msg Config: LA7V HOST 981

Select Lab Code Mapping File Option:

### Print Local Codes \[LA7V 62.47 PRINT LOCAL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print Local Codes \[LA7V 62.47 PRINT LOCAL\] prints local codes from file (#62.47).

<span id="_Toc510168971" class="anchor"></span>Figure 30. Print Local Codes \[LA7V 62.47 PRINT LOCAL\]

Select Lab Code Mapping File Option: <span class="mark">PL \<ENTER\></span> Print Local Codes

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

LAB CODE MAPPING -- LOCAL CODES Sep 02, 2008@16:03:57 Page: 1

SEQ ID SYSTEM PURPOSE NATL

===========================================================================

CONCEPT:GRAM STAIN (MI)

2 0410.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:BACTERIA (MI)

249 2 99LRE ANSWER NO

Related Entry: \[#61.2:2\] STAPHYLOCOCCUS AUREUS

1000002 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V HOST 170

1000003 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V HOST 9999

1000004 4796 99VA61.2 ANSWER NO

Related Entry: \[#61.2:4796\] STREPTOCOCCUS ALPHA HEMOL.(NOT GP.D OR S.PNEU...

Msg Config: LA7V COLLECTION 9999

CONCEPT:BACTERIOLOGY REPORT (MI)

1000001 0410.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

1000003 0410.2 99LAB RESULT NO

Msg Config: LA7V HOST 9999

1000004 0410.2 99LAB RESULT NO

Msg Config: LA7V COLLECTION 9999

1000002 BOB 99LAB NO

CONCEPT:BACTERIOLOGY SUSCEPTIBILITY (MI)

1019 46 99LRA RESULT NO

CONCEPT:PARASITE (MI)

26 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V HOST 170

27 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V HOST 9999

28 486 99VA61.2 ANSWER NO

Related Entry: \[#61.2:486\] PABESIA, NOS

Msg Config: LA7V COLLECTION 9999

CONCEPT:PARASITE REPORT REMARK (MI)

1 0440.3 99LAB RESULT NO

2 0440.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:PARASITE STAGE (MI)

1 63.749 99LAB RESULT NO

CONCEPT:FUNGAL REPORT REMARK (MI)

2 0430.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:MYCOBACTERIA SUSCEPTIBILITY (MI)

1000001 TEST L NO

CONCEPT:MYCOBACTERIA REPORT (MI)

2 0420.2 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:VIROLOGY REPORT (MI)

34 0450.1 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:MYCOLOGY SMEAR/PREP (MI)

2 0430.3 99LAB RESULT NO

Msg Config: LA7V HOST 170

CONCEPT:ACID FAST STAIN (MI)

3 0420.1 99LAB RESULT NO

Override Concept: BACTERIOLOGY REPORT

Msg Config: LA7V HOST 0052

CONCEPT:ACID FAST STAIN QUANTITY (MI)

2 0420.1 99LAB RESULT NO

Msg Config: LA7V HOST 170

### Print Susceptibilities \[LA7V 62.47 PRINT SUSC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print Susceptibilities \[LA7V 62.47 PRINT SUSC\] prints File \#62.47 susceptibility codes.

<span id="_Toc510168972" class="anchor"></span>Figure 31. Print Susceptibilities \[LA7V 62.47 PRINT SUSC\]

Select Lab Code Mapping File Option: <span class="mark">PRINT SUSCEPTIBILITIES</span>

Print (A)ll, (M)apped, (U)nmapped: (A/M/U): A// <span class="mark">\<ENTER\></span> LL

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

LAB CODE MAPPING -- SUSCEPTIBILITIES Sep 02, 2008@16:06:19 Page: 1

SEQ ID SYSTEM PURPOSE NATL

===========================================================================

CONCEPT:BACTERIOLOGY SUSCEPTIBILITY (MI)

1019 46 99LRA RESULT NO

1 1-8 LN RESULT YES

LOINC: Acyclovir:Susc:Pt:Isolate:OrdQn

10 10-9 LN RESULT YES

LOINC: Amdinocillin:Susc:Pt:Isolate+Ser:Ord:SBT

100 100-8 LN RESULT YES

LOINC: Cefoperazone:Susc:Pt:Isolate:OrdQn:MIC

101 101-6 LN RESULT YES

LOINC: Cefoperazone:Susc:Pt:Isolate:OrdQn:Agar diffusion

102 102-4 LN RESULT YES

LOINC: Cefoperazone:Susc:Pt:Isolate+Ser:Ord:SBT

103 103-2 LN RESULT YES

LOINC: Ceforanide:Susc:Pt:Isolate:Qn:MLC

104 104-0 LN RESULT YES

LOINC: Ceforanide:Susc:Pt:Isolate:OrdQn:MIC

105 105-7 LN RESULT YES

LOINC: Ceforanide:Susc:Pt:Isolate:OrdQn:Agar diffusion

106 106-5 LN RESULT YES

LOINC: Ceforanide:Susc:Pt:Isolate+Ser:Ord:SBT

636 10653-4 LN RESULT YES

LOINC: Clotrimazole:Susc:Pt:Isolate:OrdQn:MIC

637 10654-2 LN RESULT YES

LOINC: Clotrimazole:Susc:Pt:Isolate:Qn:MLC

638 10697-1 LN RESULT YES

LOINC: Nystatin:Susc:Pt:Isolate:OrdQn:MIC

639 10698-9 LN RESULT YES

LOINC: Nystatin:Susc:Pt:Isolate:Qn:MLC

107 107-3 LN RESULT YES

LOINC: Cefotaxime:Susc:Pt:Isolate:Qn:MLC

### Error Code Help \[LA7V 62.47 ERROR CODE HELP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Error Code Help \[LA7V 62.47 ERROR CODE HELP\] adds extended help for error codes. Errors can be looked up in the LA7 MESSAGE LOG BULLETINS file (#62.485).

<span id="_Toc510168973" class="anchor"></span>Figure 32. Error Code Help \[LA7V 62.47 ERROR CODE HELP\]

Select Lab Code Mapping File Option: <span class="mark">ERROR CODE HELP</span>

LAB CODE MAPPING ERROR CODES

=========================================================================

Error \#200

No File \#62.47 mapping found for OBX-3

The code set in OBX-3 was not found in the LAB CODE MAPPING file (#62.47).

--------------------------------

Error \#201

No File \#63 field mapping found for OBX-3

Storage location unknown in LAB DATA file (#63). An organism,

parasite, or susceptibility doesn't have a mapping to or

storage location in the LAB DATA file (#63). This is usually

caused by an incorrect or missing RELATED ENTRY field (#2.1)

for that code in the LAB CODE MAPPING file (#62.47).

---------------------------------

Error \#202

No filing method for CONCEPT \# n found for OBX-3

Enter RETURN to continue or '^' to exit:

The Lab package does not have a routine to process the Concept.

---------------------------------

Error \#203

No Coding System found in OBX-5

OBX-5 does not have a coding system specified.

---------------------------------

Error \#204

Unknown entity in OBX-5

The organism, parasite, etc. being reported does not have

an entry in its associated file (i.e. ETIOLOGY FIELD file (#61.2)).

---------------------------------

Error \#205

Invalid SubId in OBX-4

Enter RETURN to continue or '^' to exit:

The SubId in OBX-4 is either empty or invalid. The processing logic expected a valid SubId here and cannot continue processing. Action must be taken by the sender of the HL7 message to correct the invalid SubId.

---------------------------------

Error \#206

Could not create new entry in file \#X (text)

The system needed to add a new entry "on-the-fly" to

the file specified to handle this incoming message but

failed to create the new entry. This may be a problem on

the sender's or the receiver's side.

Select HELP SYSTEM action or \<return\>:

### Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\] displays antibiotics from ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and suggests which entry from the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) to map to the LOINC code in the LAB CODE MAPPING file (#62.47).

<span id="_Toc510168974" class="anchor"></span>Figure 33. Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\]

Select Lab Code Mapping File Option: <span class="mark">MAP ALL SUSCEPTIBILITIES</span>

Report only? YES// <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">;;999 \<ENTER\></span> TELNET PORT Right Margin: 80// <span class="mark">\<ENTER\></span>

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...

---LOINC 3320-9 in \#64:27 not a susceptibility (#62.06:1)

-----AMIKACIN~RANDOM:MCNC:PT:SER/PLAS:QN

\#62.06:3 \#95.3:194 \#62.47:7,193

No RELATED ENTRY for LOINC 194-1

CLINDAMYCIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION

Use CLINDAM (CLINDAMYCIN) for this mapping?

\#62.06:19 \#95.3:13968 \#62.47:7,647

No RELATED ENTRY for LOINC 13968-3

PENICILLIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION

Use TOM' WONDER DRUG (PROVIDENCE \#8) for this mapping?

\#62.06:20 \#95.3:117 \#62.47:7,117

No RELATED ENTRY for LOINC 117-2

CEFOXITIN:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION

Use CEFOXITIN for this mapping?

\#62.06:21 \#95.3:109 \#62.47:7,109

No RELATED ENTRY for LOINC 109-9

CEFOTAXIME:SUSC:PT:ISLT:ORDQN:AGAR DIFFUSION

Use CEFOTAXIME for this mapping?

---No NLT code in \#62.06 for COMPUCILLIN (22)

\#62.06 records searched: 69 of 69

Total \#62.47 records searched: 32

Total NATL codes: 32

Total \#62.47 codes without mapping: 30

Total \#62.06 LOINC codes not in \#62.47: 2

### Interim report for an accession \[LRRP1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the option Interim report for an accession \[LRRP1\] to display an interim report for a selected accession. It will only print verified results. The report prints site codes for tests. The user will be asked if they would like to print an address page. The address page prints on a separate page(s) at the end of the report and lists the performing lab name, address and site code. This option is located on the Results menu \[LR OUT\], which is located on the Laboratory DHCP Menu \[LRMENU\].

<span id="_Toc510168975" class="anchor"></span>Figure 34. Interim report for an accession \[LRRP1\]

Select Laboratory DHCP Menu Option: <span class="mark">5 \<ENTER\></span> Results menu

Select Results menu Option: <span class="mark">INTERIM REPORT FOR AN ACCESSION</span>

Print address page? NO// <span class="mark">YES</span>

Select Accession or UID: <span class="mark">CH 0314 1</span>

CHEMISTRY (MAR 14, 2012) 1

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET

LRPATIENT,TWO Report date: Mar 14, 2012@13:23

Pat ID: 000-00-1234 SEX: F DOB: Jan 01, 1900 LOC: RC

Provider: LRUSER,ONE

Specimen: SERUM

Accession \[UID\]: CH 0526 1 \[0411460001\]

Report Released: Jul 14, 2011@13:09

Specimen Collection Date: May 26, 2011@14:10

Test name Result units Ref. range Site Code

GLUCOSE 100 mg/dL 60 - 123 \[522\]

CALCIUM 200 H\* mg/dL 9 - 11 \[522\]

Comment: TEST

===============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LRPATIENT,TWO 000-00-1234 Mar 14, 2012@13:23 PRESS '^' TO STOP

page 2

LRPATIENT,TWO 000-00-1234 Mar 14, 2012@13:23

Performing Lab Sites:

\[522\] ZZ BONHAM \[CLIA# 987654321\]

BONHAM, TX

Select Accession or UID: <span class="mark">\<ENTER\></span>

Select Results menu Option:

### Move Cumulative Major/Minor Headers \[LRAC MOVE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the option Move Cumulative Major/Minor Headers \[LRAC MOVE\] to move a cumulative major or minor header to another major header. After moving the header, it deletes the old header. This option is located on the Cumulative menu \[LRAC\], which is located on the Supervisor menu \[LRSUPERVISOR\].

<span id="_Toc510168976" class="anchor"></span>Figure 35. Move Cumulative Major/Minor Headers \[LRAC MOVE\]

Select Laboratory DHCP Menu Option: <span class="mark">11 \<ENTER\></span> Supervisor menu

Select Supervisor menu Option: <span class="mark">CUMULATIVE MENU</span>

Select Cumulative menu Option: <span class="mark">LACM \<ENTER\></span> Move Cumulative Major/Minor Headers

Select one of the following:

1 Major Header

2 Minor Header

Select type of header to move: 1// <span class="mark">MAJOR HEADER</span>

Select MAJOR HEADER: <span class="mark">RIA</span>

MAJOR HEADER ORDER: 19// <span class="mark">\<ENTER\></span>

MAJOR HEADER: NEW HEADER// <span class="mark">RIA NEW</span>

MAJOR HEADER MEDICAL CENTER: ALBANY ISC// <span class="mark">\<ENTER\></span>

Copying major header: RIA

to major header: RIA NEW

Re-indexing new major header: RIA NEW

Deleting major header: RIA

Re-indexing the LAB REPORTS file for:

Mumps "A" index of the LAB TEST subfield

(contains reference ranges, units, etc. from file 60)

Mumps "AC" index of the LAB TEST LOCATION subfield

(atomic test x-ref.)

Mumps "AR" index of the LAB TEST subfield

(site/specimen x-ref.)

HEMATOLOGY

CBC PROFILE..............................

DIFFERENTIAL COUNT

DIFFERENTIAL COUNTS..........................................................

.......................

COAG & MISC. HEM

COAG PROFILE..................

MISC. HEM..........

CHEMISTRY (SERUM)

CHEM PROFILE...............................................................

CHEMISTRY-MISC.

CARDIAC ENZYMES........................

MISC. CHEM....................................

HGB A1C...

AMMONIA...

CHEMISTRY-GLUCOSE TOL.

GLUCOSE TOL-(SERUM).....................

GLUCOSE TOL-(URINE).....................

TOXICOLOGY

TOXICOLOGY...................................................................

............................................

RIA-(PLASMA)

RIA-(PLASMA)............

SEROLOGY

SEROLOGY....................................

FLUIDS

CELL COUNT (CSF)..................

CELL COUNT (SYNOVIAL)..................

CELL COUNT (PLEURAL)..................

CELL COUNT (PERITONEAL)..................

CELL COUNT (PERICARD/THORACIC)..................

CSF CHEMS............

SYNOVIAL CHEMS...............

PLEURAL CHEMS...............

PERITONEAL CHEMS...............

PERICARD/THORACIC CHEMS...............

URINALYSIS

URINALYSIS...................................................................

...................................

URINE CHEMS

URINE CHEMS...................................................

LAB LONG TERM TESTS

LAB LONG TERM TESTS...

RIA NEW

RIA-(SERUM)...............................................................

Run Diagnostic Report for LAB REPORTS File

DEVICE: HOME// <span class="mark">\<ENTER\></span> TELNET PORT Right Margin: 80// <span class="mark">\<ENTER\></span>

Diagnostic Report for LAB REPORTS FILE (64.5)

HEMATOLOGY

CBC PROFILE

DIFFERENTIAL COUNT

DIFFERENTIAL COUNTS

COAG & MISC. HEM

COAG PROFILE

MISC. HEM.

CHEMISTRY (SERUM)

CHEM PROFILE

CHEMISTRY-MISC.

CARDIAC ENZYMES

MISC. CHEM

HGB A1C

AMMONIA

CHEMISTRY-GLUCOSE TOL.

GLUCOSE TOL-(SERUM)

GLUCOSE TOL-(URINE)

TOXICOLOGY

TOXICOLOGY

RIA-(PLASMA)

RIA-(PLASMA)

SEROLOGY

SEROLOGY

FLUIDS

CELL COUNT (CSF)

CELL COUNT (SYNOVIAL)

CELL COUNT (PLEURAL)

CELL COUNT (PERITONEAL)

CELL COUNT (PERICARD/THORACIC)

CSF CHEMS

SYNOVIAL CHEMS

PLEURAL CHEMS

PERITONEAL CHEMS

PERICARD/THORACIC CHEMS

URINALYSIS

URINALYSIS

URINE CHEMS

URINE CHEMS

LAB LONG TERM TESTS

LAB LONG TERM TESTS

RIA NEW

RIA-(SERUM)

Select Cumulative menu Option:

### AP LEDI Data Entry \[LRAP VR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the option AP LEDI Data Entry \[LRAP VR\] to review and accept AP results from a LEDI Host site. It is located on the Data entry, anat path menu \[LRAPD\], which is located on the Anatomic pathology menu \[LRAP\].

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/024.png) | NOTE:. The AP LEDI Data Entry option will only be used by the LEDI test sites who previously used the software to send and receive AP. |

<span id="_Toc510168977" class="anchor"></span>Figure 36. AP LEDI Data Entry \[LRAP VR\]

Select Anatomic pathology Option: <span class="mark">D \<ENTER\></span> Data entry, anat path

Select Data entry, anat path Option: <span class="mark">LEDI \<ENTER\></span> AP LEDI Data Entry

Select LOAD/WORK LIST NAME: <span class="mark">LDSI</span>

Select PROFILE: <span class="mark">SURGICAL PATHOLOGY \<Enter\></span> SURGICAL PATHOLOGY

Select Performing Laboratory: <span class="mark">REGION 7 ISC,TX (FS)</span>// <span class="mark">\<ENTER\></span> TX 170

Work Load Area: LDSI// <span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// <span class="mark">2 \<ENTER\></span> Unique Identifier (UID)

Unique Identifier: <span class="mark">2211000011</span>

TEST,PATIENT 000-00-1234 Age: 61yr

ORDER \#: 196 NSP 11 11 \[2211000011\]

Seq \#: 61 Accession: NSP 11 11 Results received: Oct 19, 2011@15:55

UID: 2211000011 Last updated: Oct 19, 2011@15:55

Enter RETURN to continue or '^' to exit: <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

Accession \#: NSP 11 11 UID: 2211000011

Name: TEST,PATIENT SSN: 000-00-1234 DOB: Jan 01, 1950 Age: 61yr PAGE: 1

Collection Date: Oct 19, 2011@15:31

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------

Surgical Pathology Diagnosis

TESTING

Do you want to ACCEPT these results? NO// <span class="mark">Y \<ENTER\></span> YES

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// <span class="mark">\<ENTER\></span> TX VAMC 522 INACTIVE Jan 01, 1997

Sure you want to add this record? NO// <span class="mark">Y \<ENTER\></span> YES

... assignment created.

Current performing lab assignments:

Surgical Pathology Report Performed By:

ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

Unique Identifier: <span class="mark">\<ENTER\></span>

Select Data entry, anat path Option:

### Reprocess Lab HL7 Messages \[LA7 REPROCESS HL7 MESSAGES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Reprocess Lab HL7 Messages \[LA7 REPROCESS HL7 MESSAGES\] allows reprocessing of selected incoming Lab HL7 messages. This option is located on the Lab Universal Interface Menu \[LA7 MAIN MENU\], which is located on the 'Lab interface menu' \[LA INTERFACE\].

Messages should be of type (I)ncoming, have a status of (X)purgable, (E)rror, or (Q)ueued for processing and be related to a message configuration type:

LAB UI

LEDI

Messages for other configuration types should not be reprocessed at this time.

<span id="_Toc510168978" class="anchor"></span>Figure 37. Reprocess Lab HL7 Messages \[LA7 REPROCESS HL7 MESSAGES\]

Select Laboratory DHCP Menu Option: <span class="mark">11 \<ENTER\></span> Supervisor menu

Select Supervisor menu Option: <span class="mark">LAB INTER \<ENTER\></span> face menu

Select Lab interface menu Option: <span class="mark">LAB UNIVERSAL INTERFACE MENU</span>

Select Lab Universal Interface Menu Option: <span class="mark">RLH \<ENTER\></span> Reprocess Lab HL7 Messages

Display identifiers during message selection? YES// <span class="mark">\<ENTER\></span>

Select Message: <span class="mark">LA7V HOST 981-I-L612790005</span>

Entered D/T: Oct 06, 2011@12:46 Type: INCOMING Status: PURGEABLE

Instrument Name: LA7V HOST 981-I-L612790005

Configuration: LA7V HOST 981

Select another Message: <span class="mark">\<ENTER\></span>

Reprocess these messages? YES// <span class="mark">\<ENTER\></span>

Queued processing routine for configuration LA7V HOST 981

Select Lab Universal Interface Menu Option:

### Display SCT Overrides \[LA7S 62.48 PRINT SCT OVERRIDE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Display SCT Overrides \[LA7S 62.48 PRINT SCT OVERRIDE\] displays the SCT Overrides on file for a MESSAGE PARAMETER (#62.48) file entry. It can also display all SCT Overrides on file for all MESSAGE PARAMETER (#62.48) entries. This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

<span id="_Toc510168979" class="anchor"></span>Figure 38. Display SCT Overrides \[LA7S 62.48 PRINT SCT OVERRIDE\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">DSO \<ENTER\></span> Display SCT Overrides

Select MESSAGE CONFIGURATION: ALL// <span class="mark">LA7V HOST 0052</span>

Select another MESSAGE CONFIGURATION: <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

MESSAGE CONFIGURATION SCT OVERRIDES Printed Mar 14, 2012@13:41 Page 1

===============================================================================

Message Configuration: LA7V HOST 0052

Specimen \[Topography file \#61\] VA SCT Non-VA SCT

SPUTUM \[360\] 45710003 416462003

URINE \[71\] 78014005 78014005

Sample \[Collection Sample file \#62\] VA SCT Non-VA SCT

SPUTUM \[18\] 119334006 49957000

URINE \[15\] 78014005 78014005

SCT Code SCT Preferred Term

119334006 Sputum specimen

416462003 Wound

45710003 Sputum

49957000 Spermatic cord structure

78014005 Urine

Select Lab Shipping Management Menu Option:

### Display a Shipping Configuration \[LA7S 62.9 PRINT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Display a Shipping Configuration \[LA7S 62.9 PRINT\] displays LAB SHIPPING CONFIGURATION file (#62.9) information for a Shipping Configuration (or a Message Parameter) file entry. This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

<span id="_Toc510168980" class="anchor"></span>Figure 39. Display a Shipping Configuration \[LA7S 62.9 PRINT\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">DSC \<ENTER\></span> Display a Shipping Configuration

Select LA7 MESSAGE PARAMETER CONFIGURATION: <span class="mark">LA7V HOST 170</span>

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Only show SCT overrides? ? N// <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">0;80;999</span>

SHIPPING CONFIGURATION DISPLAY Printed Mar 14, 2012@13:48 Page 1

===============================================================================

Shipping Configuration: LEDI HOST LAB

Test: GLUCOSE

Glucose Fasting (81352.0000)

Specimen: SERUM (67922002 Serum)

Test: LYTES

Electrolytes (81357.0000)

Test: CREATININE

Creatinine (82565.0000)

Select Lab Shipping Management Menu Option:

### Code Usage \[LA7S CODE USAGE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Code Usage \[LA7S CODE USAGE\] searches the system for a particular code and code system pair and reports in which files this pair is used. This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

<span id="_Toc510168981" class="anchor"></span>Figure 40. Code Usage \[LA7S CODE USAGE\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">CU \<ENTER\></span> Code Usage

Enter IDENTIFIER: <span class="mark">673-4</span>

Enter CODING SYSTEM: LN

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET Right Margin: 80//

Invalid LOINC code

Checking TOPOGRAPHY file (#61)

No matches

Checking ETIOLOGY FIELD (#61.2) file

No matches

Checking COLLECTION SAMPLE (#62) file

No matches

Checking ANTIMICROBIAL SUSCEPTIBILITY (#62.06) file

No matches

Checking LAB CODE MAPPING (#62.47) file

PARASITE (#62.47:8)

\#1: 673-4 (No Message Config)

\$\$HL2LAH:8^MI^63.34^.01^9318

Checking LA7 MESSAGE PARAMETER (#62.48) file

No matches

Checking LAB SHIPPING CONFIGURATION (#62.9) file

No matches

Select Lab Shipping Management Menu Option:

### Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\] allows the user to load SNOMED CT (SCT) mappings and term disposition into the target file entry. This mapping is usually provided by STS after they have extracted and mapped the site's local terms to the appropriate SCT code. If no mapping is provided then a disposition is stored with the reason. A SCT mapping can also be provided as part of the mediation process that occurs when a new term is added either by the site or via an HL7 interface with the new term. This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

The SCT mapping file is a text file that is sent by STS to the Facilities via Lab Server side MailMan function. This option prompts the user to specify whether to proceed to the processing of the loaded data and then allows the user to apply the mappings to the target entries.

<span id="_Ref501364182" class="anchor"></span>Figure 41. Load SNOMED SCT Mapping \[LA7S LOAD MAPPING SCT\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">LSCT \<ENTER\></span> Load SNOMED SCT Mapping

Select one of the following:

0 Quit - no action

2 Process previous loaded file

Enter response: 2// 2  Process previous loaded file    

Select one of the following:

0 Quit - no action

1 Process SNOMED CT mappings directly

2 Task processing SNOMED CT mappings

Processing Action: 0// <span class="mark">1 \<Enter\></span> Process SNOMED CT mappings directly

Loading files with National SNOMED CT Codes

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Loading file \#61 \[TOPOGRAPHY FIELD\]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.......

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent....

No such entry: File \#61 IEN:8830 STS alert sent...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Loading file \#61.2 \[ ETIOLOGY FIELD \]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Lexicon SCT lookup error STS alert sent.

Names do not match: \[CLOSTRIDIUM DIFFICILE TOXIN A/B POSITIVE \< - \> CLOSTRIDIUM DIFFICILE TOXIN B DNA DETECTED\] STS alert sent.

Lexicon SCT lookup error STS alert sent.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Loading file \#62 \[ COLLECTION SAMPLE \] \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

### Map Non-VA SNOMED CT codes \[LA7S MAP NON-VA SNOMED CODES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the option Map Non-VA SNOMED CT codes \[LA7S MAP NON-VA SNOMED CODES\] to map, for a specific HL7 interface, SNOMED CT (SCT) codes required by an external system to legacy VistA Laboratory files. This is used in cases where a site is communicating with a non-VA system, and the external system maps the same term using a SCT code that is different than the code assigned by the VA to the term, then the site can override the SCT code for that specific interface. Currently, this option is used to map the following legacy VistA Laboratory files:

TOPOGRAPHY (#61).

COLLECTION SAMPLE (#62).

This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

<span id="_Toc510168983" class="anchor"></span>Figure 42. Map Non-VA SNOMED CT codes \[LA7S MAP NON-VA SNOMED CODES\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">MSCT \<ENTER\></span> Map Non-VA SNOMED CT codes

Select MESSAGE CONFIGURATION: <span class="mark">LA7V HOST 981</span>

Select VA FILE ENTRY: <span class="mark">?</span>

You may enter a new NON-VA ORDER SNOMED CODES, if you wish

Select specimen or collection sample

Enter one of the following:

SP.EntryName to select a Specimen from TOPOGRAPHY file

CS.EntryName to select a Sample from COLLECTION SAMPLE

To see the entries in any particular file type \<Prefix.?\>

Select VA FILE ENTRY: <span class="mark">SP.SPUTUM</span>

Searching for a Specimen from TOPOGRAPHY file, (pointed-to by VA FILE ENTRY)

Searching for a Specimen from TOPOGRAPHY file

SPUTUM

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Are you adding 'SPUTUM \[SP \#61:360\]' as

a new NON-VA ORDER SNOMED CODES (the 1ST for this LA7 MESSAGE PARAMETER)? No// <span class="mark">Y \<ENTER\></span> (Yes)

NON-VA ORDER SNOMED CODES SEQUENCE: 1// <span class="mark">\<ENTER\></span>

SNOMED CT ID: <span class="mark">416462003 \<ENTER\></span> Wound (disorder)

Select VA FILE ENTRY: <span class="mark">\<ENTER\></span>

Select MESSAGE CONFIGURATION: <span class="mark">\<ENTER\></span>

Select Lab Shipping Management Menu Option:

### Print MI/AP Test Mappings \[LA7VPFL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print MI/AP Test Mappings \[LA7VPFL\] checks Lab Tests by subscript (MI, SP, or CY) for their mapped NLT and Electronic Codes. These codes are required for LEDI transmission of orders and reports. Provides Lists for correctly mapped tests or tests that are not mapped correctly. This option is located on the Lab Shipping Management Menu \[LA7S MGR MENU\], which is located on the Lab liaison menu \[LRLIAISON\].

|                                                   |                                                                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/025.png) | NOTE: The option Print MI/AP Test Mappings \[LA7VPFL\] is released with LEDI IV but will not be used until a future date. |

<span id="_Toc510168984" class="anchor"></span>Figure 43. Print MI/AP Test Mappings \[LA7VPFL\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">PTM \<ENTER\></span> Print MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

Enter Lab Area Subscript: <span class="mark">SP \<ENTER\></span> Surgical Pathology

Select one of the following:

C Correctly Mapped Tests

E Tests with Errors

Enter response: <span class="mark">E \<ENTER\></span> Tests with Errors

DEVICE: HOME// <span class="mark">\<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

Laboratory Tests for SP with mapping errors Mar 14, 2012@14:51:47

Page: 1

===============================================================================

\[5059\] AUTOPSY H & E

is mapped to: Autopsy Exam NOS \[88608.0000\]

Not Linked to File \#64.061

\[5060\] AUTOPSY UNSTAINED SLIDE Not Mapped to File \#64

\< \< \< End of report \> \> \>

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

Enter Lab Area Subscript: <span class="mark">\<ENTER\></span>

Select Lab Shipping Management Menu Option:

### Initialize DOD Codes \[LA7V 62.47 ADD DOD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Initialize DOD Codes \[LA7V 62.47 ADD DOD\] populates the Lab Code Mapping file with the standard DOD local codes for the message configuration selected by the user. This option is located on the Lab Code Mapping File menu \[LA7V 62.47 MENU\], which is located on the Lab Shipping Management Menu \[LA7S MGR MENU\].

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-update-user-manual/026.png) | NOTE: The LA7V 62.47 ADD DOD option is released with LEDI IV but will not be used until a future date. |

<span id="_Toc510168985" class="anchor"></span>Figure 44. Initialize DOD Codes \[LA7V 62.47 ADD DOD\]

Select Lab liaison menu Option: <span class="mark">SMGR \<ENTER\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">LCM \<ENTER\></span> Lab Code Mapping File

Select Lab Code Mapping File Option: <span class="mark">DOD \<ENTER\></span> Initialize DOD Codes

Select MESSAGE CONFIGURATION: <span class="mark">LA7V HOST 0109</span>

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Adding 0410.2 99LAB (okay)

Adding 0410.3 99LAB (okay)

Adding 0420.1 99LAB (okay)

Adding 0420.2 99LAB (okay)

Adding 0430.2 99LAB (okay)

Adding 0430.3 99LAB (okay)

Adding 0440.3 99LAB (okay)

Adding 0450.1 99LAB (okay)

Select Lab Code Mapping File Option:

### Check SNOMED CT Mappings Against the Lexicon \[LA7TASK SCT MAPPINGS CHECK\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option checks and validates each SNOMED CT ID mapping against the Lexicon when a SNOMED CT - (SCT Mapping) file is loaded. Schedule this option to run on a recurring basis. If an exception is found (e.g., the code is inactive) the system sends an alert to Standards & Terminology Services (STS) so that STS can send an updated mapping for this entry. Note: It is possible for a code to be active at the time of the load, but be deprecated when a Lexicon patch is installed that updates the SNOMED CT code set.

If this option finds any exceptions:  
  
a. The SCT CODE STATUS field (#21) of files \#61, \#61.2 and \#62 for the entry will be updated

to 'Error',  
b. An HDI exception alert will be sent to STS,  
c. A MailMan message will be sent to the G.LMI and G.LAB MESSAGING Mail Groups with a list of the exceptions found.

STS will review the exception alerts they receive, and if needed, will send an updated SCT  
mapping file to the site to load. The site does not need to do anything until STS notify the site that there is an updated mapping file to load.

## Modified LEDI Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\] allows large HL7 component fields to display correctly and print errors and events logged using the Lab Universal Interface system.

<span id="_Toc510168986" class="anchor"></span>Figure 45. Display Lab Universal Interface Message \[LA7 PRINT LAB UI MESSAGE\]

Select Lab Universal Interface Menu Option: <span class="mark">?</span>

1 Print Source of Specimen Table

2 Print Lab Universal Interface Log

Display Lab Universal Interface Message

Download to Universal Interface

Start/Stop Auto Download Background Job

UIS Lab Universal Interface Setup

PCS Lab Point of Care Setup

FIC Lab Messaging File Integrity Checker

PIC Print Lab Messaging Integrity Check Report

RLH Reprocess Lab HL7 Messages

Select Lab Universal Interface Menu Option: <span class="mark">DISPLAY LAB UNIVERSAL INTERFACE MESSAGE</span>

Display identifiers during message selection? YES// <span class="mark">\<ENTER\></span>

Select Message: <span class="mark">20</span>

Entered D/T: Mar 01, 2011@14:37 Type: INCOMING Status: PURGEABLE

Instrument Name: LA7V HOST 981-I-1311000001

Configuration: LA7V HOST 981

Select another Message: <span class="mark">\<ENTER\></span>

Parse message fields based on HL7 segments? YES// <span class="mark">\<ENTER\></span>

Suppress blank segments? YES// <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">\<ENTER\></span> TELNET PORT

Use Browser to display message(s)? YES// <span class="mark">\<ENTER\></span>

\[\*\*\*\*\*\*\*Message Statistics\*\*\*\*\*\*\*\*\*\*\*\*\*\*\]

CONFIGURATION: LA7V COLLECTION 200LR1 DATE/TIME ENTERED: MAY 06, 2011@13:15:

DATE/TIME OF MESSAGE: MAY 06, 2011@13:15:25

INSTRUMENT NAME: LA7V REMOTE 200LR1-I-581-20110506-2

MESSAGE CONTROL ID: Q2791607T2918296_3017639

MESSAGE NUMBER: 15287455 MESSAGE TYPE: ORM

PRIORITY: 3 PROCESSING ID: TRAINING

RECEIVING APPLICATION: LA7V HOST 596 RECEIVING FACILITY: 596

SENDING APPLICATION: LA7V REMOTE 200LR1 SENDING FACILITY: 200LR1

STATUS: ERROR TYPE: INCOMING

VERSION ID: 2.3

Error Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\]

Date: May 06, 2011@13:15:38

Text: Msg \#15287455 - Cannot identify an active entry in file SHIPPING CONFIGURA

Text of Message

MSH^~\|\\^LA7V REMOTE 200LR1^200LR1^LA7V HOST 596^596^20110506131525-0400^^ORM~O0

MSH-1 = ^

MSH-2 = ~\|\\

MSH-3 = LA7V REMOTE 200LR1

MSH-4 = 200LR1

MSH-5 = LA7V HOST 596

MSH-6 = 596

MSH-7 = 20110506131525-0400

MSH-9 = ORM~O01

MSH-9-1 = ORM

MSH-9-2 = O01

MSH-10 = Q2791607T2918296_3017639

MSH-11 = T

MSH-12 = 2.3

MSH-15 = AL

MSH-16 = AL

PID^1^^7220469\~\~~USVHA&&0363~PI~VA FACILITY ID&581&L\|101102237\~\~~USSSA&&0363~SS~

00)000-0000^^M^0^581:7220469:05052011^101102237^^^2186-5^^^0

PID-1 = 1

PID-3 = 7220469\~\~~USVHA&&0363~PI~VA FACILITY ID&581&L\|1111111111\~\~~USSSA&&0363~SS

PID-3.1-1 = 7220469

PID-3.1-4-1 = USVHA

PID-3.1-4-3 = 0363

PID-3.1-5 = PI

PID-3.1-6-1 = VA FACILITY ID

PID-3.1-6-2 = 581

PID-3.1-6-3 = L

PID-3.2-1 = 111111111

PID-3.2-4-1 = USSSA

PID-3.2-4-3 = 0363

PID-3.2-5 = SS

PID-3.2-6-1 = VA FACILITY ID

PID-3.2-6-2 = 581

PID-3.2-6-3 = L

PID-5 = LEDITEST,TEST

PID-5-1 = FLAB

PID-5-2 = BLUA

PID-5-3 = C

PID-6 = LEDITEST^LEDITEST^C^^^^M

PID-7 = 19490422

PID-8 = M

PID-10 = 2106-3

PID-11 = \~~ZULU~HI\~\~~N\|2645 ANYWHERE STREET\~~FARM HILL~DE~12345~USA~P\~~001

PID-11.1-3 = ZULU

PID-11.1-4 = HI

PID-11.1-7 = N

PID-11.2-1 = 2645 ANYWHERE STREET

PID-11.2-3 = FARM HILL

PID-11.2-4 = DE

PID-11.2-5 = 12345

PID-11.2-6 = USA

PID-11.2-7 = P

PID-11.2-9 = 001

PID-13 = (000)000-0000

PID-14 = (000)000-0000

PID-16 = M

PID-17 = 0

PID-18 = 581:7220469:05052011

PID-19 = 101102237

PID-22 = 2186-5

PID-25 = 0

PV1^1^O^1208^^^^^^^^^^^^^^^O^^^^^^^^^^^^^^^^^^CD:638671^^^^^^^^20110505000000-04

PV1-1 = 1

PV1-2 = O

PV1-3 = 1208

PV1-18 = O

PV1-36 = CD:638671

PV1-44 = 20110505000000-0400

PV1-45 = 20110505235959-0400

ORC^NW^5811112600001^^581-20110506-2^SC^^^^20110506081400-0400^99761-VA581~USER

ORC-1 = NW

ORC-2 = 5811112600001

ORC-4 = 581-20110506-2

ORC-5 = SC

ORC-9 = 20110506081400-0400

ORC-10 = 99761-VA581~USER~USER

ORC-10-1 = 99761-VA581

ORC-10-2 = USER

ORC-10-3 = USER

ORC-12 = REF:581\~\~~E

ORC-12-1 = REF:581

ORC-12-4 = E

ORC-13 = 1208

ORC-15 = 20110506081602-0400

ORC-17 = 581

ORC-18 = I~ESI Default

ORC-18-1 = I

ORC-18-2 = ESI Default

ORC-19 = 99761-VA581~USER~USER

ORC-19-1 = 99761-VA581

ORC-19-2 = USER

ORC-19-3 = USER

OBR^1^5811112600001^^89111.0000~Mumps Ab IgG~99VA64^^^20110506081400-0400^^^~YOU

2011_005812011126000001-3017639^3017639^005812011126000001^20110506081602-0400^^

OBR-1 = 1

OBR-2 = 5811112600001

OBR-4 = 89111.0000~Mumps Ab IgG~99VA64

OBR-4-1 = 89111.0000

OBR-4-2 = Mumps Ab IgG

OBR-4-3 = 99VA64

OBR-7 = 20110506081400-0400

OBR-10 = ~USER~USER

OBR-10-2 = USER

OBR-10-3 = USER

OBR-11 = O

OBR-14 = 20110506081400-0400

OBR-15-1 = 67922002

OBR-15-2 = Serum (substance)

OBR-15-3 = SCT

OBR-15-4 = 72

OBR-15-5 = Serum (substance)

OBR-15 = 67922002&Serum (substance)&SCT&72&Serum (substance)&99VA61\~\~~119297000&

OBR-15-6 = 99VA61

LA7 UI Message Display Msg \#15287455 - LA7V REMOTE 200LR1-I-581-20110506-2

OBR-15-4-1 = 119297000

OBR-15-4-2 = Blood

OBR-15-4-3 = SCT

OBR-15-4-4 = 20

OBR-15-4-5 = Blood

OBR-15-4-6 = 99VA62

OBR-16 = REF:581\~\~~E

OBR-16-1 = REF:581

OBR-16-4 = E

OBR-19 = 581:7220469:05052011_005812011126000001-3017639

OBR-20 = 3017639

OBR-21 = 005812011126000001

OBR-22 = 20110506081602-0400

OBR-24 = CH

OBR-27 = 1\~~0~20110506081400-0400\~~R\|\~\~\~\~~R

OBR-27.1-1 = 1

OBR-27.1-3 = 0

OBR-27.1-4 = 20110506081400-0400

OBR-27.1-6 = R

OBR-27.2-6 = R

OBR-36 = 20110506081400-0400

### Edit Shipping Configuration \[LA7S EDIT 62.9\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Edit Shipping Configuration \[LA7S EDIT 62.9\] adds fields to individual shipping configuration entries.

<span id="_Toc510168987" class="anchor"></span>Figure 46. Edit Shipping Configuration \[LA7S EDIT 62.9\]

Select Lab Shipping Management Menu Option: <span class="mark">EDIT SHIPPING CONFIGURATION</span>

Select SHIPPING CONFIGURATION: <span class="mark">MHC TO VRR</span>

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: <span class="mark">1 \<ENTER\></span> Collecting facility

NAME: MHC TO VRR// <span class="mark">\<ENTER\></span>

COLLECTING FACILITY: ZZ BONHAM// <span class="mark">\<ENTER\></span>

COLLECTING FACILITY'S SYSTEM: ZZ BONHAM// <span class="mark">\<ENTER\></span>

HOST FACILITY: REGION 7 ISC,TX (FS)// <span class="mark">\<ENTER\></span>

HOST FACILITY'S SYSTEM: REGION 7 ISC,TX (FS)// <span class="mark">\<ENTER\></span>

STATUS: ACTIVE// <span class="mark">\<ENTER\></span>

SHIPPING METHOD: COURIER// <span class="mark">\<ENTER\></span>

BARCODE MANIFEST: NO// <span class="mark">\<ENTER\></span>

MANIFEST RECEIPT: YES// INCLUDE UNCOLLECTED SPECIMENS: NO// <span class="mark">\<ENTER\></span>

Select ORDERING LOCATION: <span class="mark">\<ENTER\></span>

Select TEST/PROFILE: HEPATITIS B Ag// <span class="mark">\<ENTER\></span>

TEST/PROFILE: HEPATITIS B Ag// <span class="mark">\<ENTER\></span>

ACCESSION AREA: SEROLOGY// <span class="mark">\<ENTER\></span>

DIVISION: <span class="mark">\<ENTER\></span>

Select FEEDER SHIPPING CONFIGURATION: <span class="mark">\<ENTER\></span>

SPECIMEN: SERUM// <span class="mark">\<ENTER\></span>

URGENCY: <span class="mark">\<ENTER\></span>

SPECIMEN CONTAINER: RED TOP// <span class="mark">\<ENTER\></span>

SHIPPING CONDITION: REFRIGERATED// <span class="mark">\<ENTER\></span>

PACKAGING CONTAINER: <span class="mark">\<ENTER\></span>

REQUIRE PATIENT HEIGHT: YES// <span class="mark">\<ENTER\></span>

PATIENT HEIGHT UNITS: <span class="mark">\<ENTER\></span>

PATIENT HEIGHT CODE: <span class="mark">\<ENTER\></span>

REQUIRE PATIENT WEIGHT: YES// <span class="mark">\<ENTER\></span>

PATIENT WEIGHT UNITS: <span class="mark">\<ENTER\></span>

PATIENT WEIGHT CODE: <span class="mark">\<ENTER\></span>

REQUIRE COLLECTION VOLUME: <span class="mark">YES</span> *Editor Note:If you answer YES here, the system displays the next two prompts.*

COLLECTION VOLUME UNITS: <span class="mark">\<ENTER\></span>

COLLECTION VOLUME CODE: <span class="mark">\<ENTER\></span>

REQUIRE COLLECTION WEIGHT: <span class="mark">\<ENTER\></span>

REQUIRE COLLECTION END D/T: <span class="mark">\<ENTER\></span>

Select TEST/PROFILE: <span class="mark">\<ENTER\></span>

Select Lab Shipping Management Menu Option:

> **NOTE:** If the user answers YES to REQUIRE COLLECTION VOLUME, the following two prompts display: COLLECTION VOLUME UNITS, COLLECTION VOLUME CODE.

### Print Shipping Manifest \[LA7S MANIFEST PRINT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print Shipping Manifest \[LA7S MANIFEST PRINT\] prints additional information on the manifests:

Requesting provider's office phone, voice/digital pager numbers, and specimen container are printed on working copies of the shipping manifest.

Relevant clinical information is printed on manifests used for shipping documents.

Refer to the option Edit Relevant Clinical Information \[LA7S MANIFEST CLINICAL INFO\].<span id="_Toc78075628" class="anchor"></span>

Figure 47. Print Shipping Manifest \[LA7S MANIFEST PRINT\]

Select Lab Shipping Menu Option: <span class="mark">?</span>

SMB Build Shipping Manifest

SSM Start a Shipping Manifest

SMS Close/Ship a Shipping Manifest

ART Add/Remove a Shipping Manifest Test

SMR Edit Required Test Information

SMI Edit Relevant Clinical Information

SMC Cancel a Shipping Manifest

PSM Print Shipping Manifest

STA Order Status Report

RSM Retransmit Shipping Manifest

RLR Retransmit LEDI Lab Results

SMP Print LEDI Pending Orders

Select Lab Shipping Menu Option: <span class="mark">PRINT SHIPPING MANIFEST</span>

Print Shipping Manifest

Select Shipping Configuration: <span class="mark">LEDIB HOST</span>

Select Shipping Manifest: <span class="mark">980-20110218-1</span>

Print barcodes on manifest? YES// <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">\<ENTER\></span> TELNET PORT Right Margin: 80// <span class="mark">\<ENTER\></span>

Shipping Manifest: 980-20110218-1 Page: 1

to Site: LEDIB Printed: Apr 07, 2011@16:59

from Site: LEDIA E-Order: YES

Date Shipped: Feb 18, 2011@16:30 Ship via: FEDEX

Shipping Condition: ROOM TEMPERATURE Container: STYROFOAM BOX

Item Patient Name Patient ID Accession

Date of Birth Patient ICN Specimen UID

Requested By Sex Collect Date/Time

------------------------------------------------------------------------------

1-1 BCMA,ONE-PATIENT 000-00-0001 SOIM\* 11 1

Apr 07, 1935 8811000001

PROVIDER,ONE Male Feb 18, 2011@16:13

-----------------------------------------

VIRAL LOAD BLOOD

VA NLT Code \[Name\]: 89498.0000 \[HIV Viral Load\]

------------------------------------------------------------------------------

End of Shipping Manifest

### Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\] prints ordering provider and current test status.

<span id="_Toc510168989" class="anchor"></span>Figure 48. Print LEDI Pending Orders \[LA7S PENDING PRINT LEDI\]

Select Lab Shipping Menu Option: <span class="mark">?</span>

SMB Build Shipping Manifest

SSM Start a Shipping Manifest

SMS Close/Ship a Shipping Manifest

ART Add/Remove a Shipping Manifest Test

SMR Edit Required Test Information

SMI Edit Relevant Clinical Information

SMC Cancel a Shipping Manifest

PSM Print Shipping Manifest

STA Order Status Report

RSM Retransmit Shipping Manifest

RLR Retransmit LEDI Lab Results

SMP Print LEDI Pending Orders

Select Lab Shipping Menu Option: <span class="mark">PRINT LEDI PENDING ORDERS</span>

Select Shipping Manifest: <span class="mark">7 \<ENTER\></span> GOMERTOSE,HE BE

Pat ID: 000000000 DOB: Mar 02, 1955 Sex: MALE

Spec ID: 1409000002 Manifest: 522-20090721-1 Site: ZZ BONHAM

Collected D/T: Feb 27, 2009@15:13 Specimen: SERUM Spec. Status: In-Transit

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

DEVICE: HOME// <span class="mark">\<ENTER\></span> TELNET PORT Right Margin: 80// <span class="mark">\<ENTER\></span>

\*\*\* DO NOT USE FOR SHIPPING DOCUMENT - WORK COPY ONLY \*\*\*

Shipping Manifest: 522-20090721-1 Page: 1

to Site: DALLAS OI Printed: Apr 07, 2011@17:06

from Site: ZZ BONHAM E-Order: YES

Status: Electronic Manifest Ship via: Electronic manifest

Shipping Condition: None Specified Container: None Specified

Item Patient Name Patient ID Accession

Date of Birth Patient ICN Specimen UID

Requested By Sex Collect Date/Time

------------------------------------------------------------------------------

1-1 LEDITEST,TEST 000000000 SER 09 2

Mar 02, 1955 1409000002

LRUSER,TWO Male Feb 27, 2009@15:13

COMMENTS: HEPATITIS B Ag

Specimen source: Serum (substance) \[67922002:SCT\] ; Serum

\[SER:HL70070\]

Collection sample: Blood specimen (specimen) \[119297000:SCT\] ;

BLOOD \[20:99VA62\]

Host test status: In-Transit

-------------------------------

HEPATITIS B Ag SERUM

### Enter/verify/modify data (manual) \[LRENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Enter/verify/modify data (manual) \[LRENTER\] supports the editing of microbiology results by using either the Unique Identifier (UID) or the Accession Number.

<span id="_Toc510168990" class="anchor"></span>Figure 49. Enter/verify/modify data (manual) \[LRENTER\]

Enter/verify/modify data (manual)

Do you want to review the data before and after you edit? YES// <span class="mark">\<ENTER\></span>

Do you wish to see all previously verified results? NO// <span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// <span class="mark">2 \<ENTER\></span> Unique Identifier (UID)

Unique Identifier: <span class="mark">1411000010 \<ENTER\></span> (MICRO 11 10)

### Referral Patient Multi-purpose Accession \[LRLEDI\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Referral Patient Multi-purpose Accession \[LRLEDI\] includes three modifications to allow receipt of inter-divisional LEDI manifests from a facility within an existing VistA system.

<span id="_Toc510168991" class="anchor"></span>Figure 50. Referral Patient Multi-purpose Accession \[LRLEDI\]

Select OPTION NAME: <span class="mark">REFERRAL PATIENT MULTI-PURPOSE \<ENTER\></span> LRLEDI Referral Patient Multi-purpose Accession

Are you using a barcode reader? YES// <span class="mark">NO</span>

Select Shipping Configuration: <span class="mark">CBOC TO MAIN</span>

Select Shipping Manifest: <span class="mark">170-20080206-4 \<ENTER\></span> CBOC TO MAIN Status: RECEIVED as of Feb 06, 2008@18:10

Select one of the following:

0 Abort Manifest Acceptance

1 Accept Manifest

2 Accept Manifest with Exceptions

3 Accept Selected Accessions

4 Reject Manifest

Manifest Acceptance Action: <span class="mark">1 \<ENTER\></span> Accept Manifest

Manifest 170-20080206-4 status set to 'Manifest received by host facility'.

Test(s) on manifest 170-20080206-4 set to 'Test received' status.

### Fast Bypass Data Entry/Verify \[LRFASTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Fast Bypass Data Entry/Verify \[LRFASTS\] allows the selection of a performing laboratory for specific sections or the entire report.

<span id="_Toc510168992" class="anchor"></span>Figure 51. Fast Bypass Data Entry/Verify \[LRFASTS\]

Select OPTION NAME: <span class="mark">FAST BYPASS DATA ENTRY/VERIFY \<ENTER\></span> LRFASTS Fast Bypass Data Entry/Verify

Do you want to review the data before and after you edit? YES// <span class="mark">\<ENTER\></span>

Select Performing Laboratory: ZZ BONHAM// <span class="mark">\<ENTER\></span> TX VAMC 522 INACTIVE Jan 01,1997

WANT TO ENTER COLLECTION TIMES? Y// <span class="mark">\<ENTER\></span>

Select ACCESSION TEST GROUP: <span class="mark">MICROBIOLOGY</span>

Select Patient Name: <span class="mark">HXX,PXXXXXX \<ENTER\></span> HXX,PXXXXXX 1-1-60 XXXXXXXXX NO NSC VETERAN

Enrollment Priority: Category: IN PROCESS End Date:

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from NOV 17,2009

Enter \<RETURN\> to continue. <span class="mark">\<ENTER\></span>

Select one of the following:

LC LAB COLLECT(INPATIENTS-MORN. DRAW)

SP SEND PATIENT

WC WARD COLLECT

I Immed COLLECT

Specimen collected how ? : SP// <span class="mark">IMMED\<ENTER\></span> COLLECT

PATIENT LOCATION: 2E// <span class="mark">\<ENTER\></span> 2 EAST

PROVIDER: LRUSER,ONE// <span class="mark">\<ENTER\></span>

LAB Order number: <span class="mark">145</span>

Is there one sample for this patient's order? Yes// <span class="mark">\<ENTER\></span> (Yes)

Select COLLECTION SAMPLE NAME: <span class="mark">URINE \<ENTER\></span> URINE

Enter Order Comment:

Choose one (or more, separated by commas) ('\*' AFTER NUMBER TO CHANGE URGENCY)

1 CULTURE & SENSITIVITY 6 AFB SMEAR

2 ANAEROBIC CULTURE 7 MYCOLOGY CULTURE

3 GRAM STAIN 8 PARASITE EXAM

4 BLOOD CULTURE 9 FECAL LEUKOCYTES

5 AFB CULTURE & SMEAR 10 STERILITY TEST

TEST number(s): <span class="mark">1</span>

For CULTURE & SENSITIVITY

Other tests? N// <span class="mark">\<ENTER\></span>

Nature of Order/Change: <span class="mark">WRITTEN \<ENTER\></span> W

You have just selected the following tests for HXX,PXXXXXX XXX-XX-XXXX

entry no. Test Sample

1 CULTURE & SUSCEPTIBILITY URINE

All satisfactory? Yes// <span class="mark">\<ENTER\></span> (Yes)

LAB Order number: <span class="mark">145</span>

Collection Date@Time: NOW// <span class="mark">\<ENTER\></span> (APR 14, 2011@15:16:57)

Print labels on: LABLABEL// <span class="mark">NULL \<ENTER\></span> Bit Bucket

Do you wish to test the label printer: NO// <span class="mark">\<ENTER\></span>

~For Test: CULTURE & SUSCEPTIBILITY URINE

Enter Order Comment: <span class="mark">\<ENTER\></span>

ACCESSION: MICRO 11 11 \<1411000011\>

CULTURE & SUSCEPTIBILITY URINE

COMMENT ON SPECIMEN:

Work Load Area: MICROBIOLOGY

HXX,PXXXXXX SSN: XXX-XX-XXXX LOC: 2E

Pat Info: Sex: MALE Age: 51yr as of Apr 14, 2011

Edit this accession? YES// <span class="mark">\<ENTER\></span>

1 CULTURE & SUSCEPTIBILITY

CULTURE & SUSCEPTIBILITY completed: <span class="mark">T \<ENTER\></span> (APR 14, 2011)

COLLECTION SAMPLE: URINE// <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: URINE// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Select GRAM STAIN: <span class="mark">A</span>

(NO)

Select GRAM STAIN: <span class="mark">\<ENTER\></span>

BACT RPT STATUS: <span class="mark">F \<ENTER\></span> FINAL REPORT

URINE SCREEN: <span class="mark">N</span> NEGATIVE

Select ORGANISM: <span class="mark">ESCHERICHIA COLI \<ENTER\></span> 1571 112283007 SCT Organism

ORGANISM ISOLATE NUMBER: 1// <span class="mark">\<ENTER\></span>

ORGANISM: ESCHERICHIA COLI// <span class="mark">\<ENTER\></span>

QUANTITY: <span class="mark">\<10000</span>

(\<10000)

Select COMMENT: <span class="mark">\<ENTER\></span>

COLISTIN: <span class="mark">\<ENTER\></span>

GENTAMICIN: <span class="mark">R\<ENTER\></span> (R)

CHLORAMPHENICOL: <span class="mark">I \<ENTER\></span> (I)

TETRACYCLINE: <span class="mark">S \<ENTER\></span> (SUS)

AMPICILLIN: <span class="mark">R \<ENTER\></span> (RESIS)

CARBENICILLIN: <span class="mark">I \<ENTER\></span> (I)

TOBRAMYCIN: <span class="mark">S \<ENTER\></span> (SUS)

TRIMETHAPRIM/SULFAMETHOXAZOLE: <span class="mark">R \<ENTER\></span> (RESIS)

AMIKACIN: <span class="mark">I \<ENTER\></span> (I)

CEFAMANDOLE: <span class="mark">S \<ENTER\></span> (SUS)

CEFOXITIN: <span class="mark">R \<ENTER\></span> (RESIS)

NITROFURANTOIN: <span class="mark">I \<ENTER\></span> (I)

CEPHALOTHIN: <span class="mark">S \<ENTER\></span> (SUS)

1 ESCHERICHIA COLI

Select ORGANISM: <span class="mark">\<ENTER\></span>

Select BACT RPT REMARK: <span class="mark">\<ENTER\></span>

BACT RPT DATE APPROVED: <span class="mark">NOW \<ENTER\></span> (APR 14, 2011@15:21)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// <span class="mark">\<ENTER\></span> TX VAMC 522 INACTIVE Jan 01, 1997

Sure you want to add this record? NO// <span class="mark">YES</span>

... assignment created.

Current performing lab assignments:

Bacteriology Report Performed By:

ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for:

CULTURE & SUSCEPTIBILITY completed: 04/14/2011 // <span class="mark">\<ENTER\></span>

(D)isplay (A)dd Work Load D

CULTURE & SUSCEPTIBILITY

WKLD CODE: Micro Mycobacterium Culture TEST MULTIPLY FACTOR: 1

COMPLETION TIME: APR 14, 2011@15:16:57

USER: POSTMASTER INSTITUTION: ZZ BONHAM

MAJOR SECTION: MICROBIOLOGY LAB SUBSECTION: MICROBIOLOGY

(D)isplay (A)dd Work Load

Accession \#:

Select Patient Name:

### Bypass normal data entry \[LRFAST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Bypass normal data entry \[LRFAST\] allows the selection of a performing laboratory for specific sections or the entire report.

<span id="_Toc510168993" class="anchor"></span>Figure 52. Bypass normal data entry \[LRFAST\]

Select OPTION NAME: <span class="mark">BYPASS NORMAL DATA ENTRY \<ENTER\></span> LRFAST Bypass normal data entry

Select Performing Laboratory: ZZ BONHAM// <span class="mark">\<ENTER\></span> TX VAMC 522 INACTIVE Jan 01, 1997

Do you want to enter draw times? No// <span class="mark">\<ENTER\></span> (No)

Select Patient Name: <span class="mark">HXX,PXXXXXX \<ENTER\></span> 1-1-60 XXXXXXXXX NO NSC VETERAN

Enrollment Priority: Category: IN PROCESS End Date:

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from NOV 17,2009

Enter \<RETURN\> to continue. <span class="mark">\<ENTER\></span>

PATIENT LOCATION: 2E// <span class="mark">\<ENTER\></span> 2 EAST

Select one of the following:

LC LAB COLLECT(INPATIENTS-MORN. DRAW)

SP SEND PATIENT

WC WARD COLLECT

I Immed COLLECT

Specimen collected how ? : SP// <span class="mark">IMMED \<ENTER\></span> COLLECT

PROVIDER: LRUSER,ONE// <span class="mark">\<ENTER\></span>

Select URGENCY: ROUTINE// <span class="mark">\<ENTER\></span>

Select LABORATORY TEST NAME: <span class="mark">CULTURE & SUSCEPTIBILITY \<ENTER\></span> C & S

For CULTURE & SUSCEPTIBILITY

Select COLLECTION SAMPLE NAME: <span class="mark">URINE \<ENTER\></span> URINE

~For Test: CULTURE & SUSCEPTIBILITY URINE

Enter Order Comment: <span class="mark">\<ENTER\></span>

Nature of Order/Change: <span class="mark">WRITTEN \<ENTER\></span> W

LAB Order number: <span class="mark">144</span>

ACCESSION: MICRO 11 10 \<1411000010\>

CULTURE & SUSCEPTIBILITY URINE

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Description OK? Y// <span class="mark">\<ENTER\></span>

Work Load Area: MICROBIOLOGY

HXX,PXXXXXX SSN: XXX-XX-XXXX LOC: 2E

Pat Info: Sex: MALE Age: 51yr as of Apr 14, 2011

Edit this accession? YES// <span class="mark">\<ENTER\></span>

1 CULTURE & SUSCEPTIBILITY

CULTURE & SUSCEPTIBILITY completed: <span class="mark">T \<ENTER\></span> (APR 14, 2011)

COLLECTION SAMPLE: URINE// <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: URINE// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Select GRAM STAIN: <span class="mark">MODE</span>

(MODE)

Select GRAM STAIN: <span class="mark">\<ENTER\></span>

BACT RPT STATUS: <span class="mark">F \<ENTER\></span> FINAL REPORT

URINE SCREEN: <span class="mark">N \<ENTER\></span> NEGATIVE

Select ORGANISM: <span class="mark">ESCHERICHIA COLI \<ENTER\></span> 1571 112283007 SCT Organism

ORGANISM ISOLATE NUMBER: 1// <span class="mark">\<ENTER\></span>

ORGANISM: ESCHERICHIA COLI// <span class="mark">\<ENTER\></span>

QUANTITY: <span class="mark">\<10000</span>

(\<10000)

Select COMMENT: <span class="mark">\<ENTER\></span>

CHOOSE FROM:

COLISTIN:

GENTAMICIN: R (R)

CHLORAMPHENICOL: I (I)

TETRACYCLINE: S (SUS)

AMPICILLIN: R (RESIS)

CARBENICILLIN: I (I)

TOBRAMYCIN: S (SUS)

TRIMETHAPRIM/SULFAMETHOXAZOLE: R (RESIS)

AMIKACIN: I (I)

CEFAMANDOLE: S (SUS)

CEFOXITIN: R (RESIS)

NITROFURANTOIN: I (I)

CEPHALOTHIN: S (SUS)

1 ESCHERICHIA COLI

Select ORGANISM: <span class="mark">\<ENTER\></span>

Select BACT RPT REMARK: <span class="mark">\<ENTER\></span>

BACT RPT DATE APPROVED: <span class="mark">NOW \<ENTER\></span> (APR 14, 2011@14:37)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// <span class="mark">TX \<ENTER\></span> VAMC 522 INACTIVE Jan 01, 1997

Sure you want to add this record? NO// <span class="mark">YES</span>

...assignment created.

Current performing lab assignments:

Bacteriology Report Performed By: ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

CULTURE & SUSCEPTIBILITY completed: 04/14/2011 //

### Results entry (batch) \[LRMISTUF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Results entry (batch) \[LRMISTUF\] allows the selection of a performing lab for entire report or specific sections.

<span id="_Toc510168994" class="anchor"></span>Figure 53. Results entry (batch) \[LRMISTUF\]

Select OPTION NAME: <span class="mark">LRMISTUF \<ENTER\></span>       Results entry (batch)

Results entry (batch)

Select ACCESSION AREA: <span class="mark">MICRO \<ENTER\></span> MICROBIOLOGY CDD

Work Load Area: <span class="mark">M</span>

     1   MICROBIOLOGY 

     2   MISC HEMATOLOGY TESTS 

     3   MISC URINALYSIS TESTS 

     4   MYCOLOGY 

CHOOSE 1-4: <span class="mark">1 \<ENTER\></span> MICROBIOLOGY

Micro Accession Year: (11)// <span class="mark">\<ENTER\></span>

Select MICROBIOLOGY TEST: <span class="mark">CULT</span>

     1   CULTURE & SUSCEPTIBILITY

     2   CULTURE - AFB NON-RESPIRATORY  AFB NON-RESPIRATORY CULT & SMEAR

     3   CULTURE - AFB RESPIRATORY  AFB RESPIRATORY CULT & SMEAR

     4   CULTURE - BLOOD  BLOOD CULTURE

     5   CULTURE - FUNGUS  MYCOLOGY CULTURE

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">1 \<ENTER\></span> CULTURE & SUSCEPTIBILITY

Preliminary or Final: <span class="mark">F</span>

Enter the field to edit: <span class="mark">?</span>

Answer with MICROBIOLOGY SUB-FIELD NUMBER, or LABEL

Do you want the entire MICROBIOLOGY SUB-FIELD List? <span class="mark">Y \<ENTER\></span> (Yes)

   Choose from:

   11.57        URINE SCREEN

   11.58        SPUTUM SCREEN

   11.6         GRAM STAIN

   13           BACT RPT REMARK

   

Enter the field to edit: <span class="mark">13 \<ENTER\></span> BACT RPT REMARK

1  Automatically enter your entry.

2  Prompt with your entry.

3  Just Prompt.

Choice: <span class="mark">1</span>

What do you want entered?: <span class="mark">NO GROWTH 2 DAYS \<ENTER\></span> (NO GROWTH 2 DAYS)

I will automatically stuff BACT RPT REMARK

with NO GROWTH 2 DAYS

   ...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Verify all work automatically? Yes// <span class="mark">\<ENTER\></span> YES

Designate the individual test as complete? No// <span class="mark">YES</span>

Select Performing Laboratory: LEXINGTON-CDD VAMC// <span class="mark">\<ENTER\></span> KY  VAMC  596A4 

     Select one of the following:

          1         Entire report

          2         BACT RPT REMARK section of report

Designate performing laboratory for:

### Microbiology Results Entry \[LRMIEDZ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Microbiology Results Entry \[LRMIEDZ\] can display the ISOLATE ID as determined by the Execute code setup in the EDIT CODE field in LABORATORY TEST file (#60).

<span id="_Toc510168995" class="anchor"></span>Figure 54. Microbiology Results Entry \[LRMIEDZ\]

Select Laboratory DHCP Menu \<TEST ACCOUNT\> Option: <span class="mark">MICROBIOLOGY MENU</span>

Select Microbiology menu \<TEST ACCOUNT\> Option: <span class="mark">RE \<ENTER\></span> Results entry

Select MICROBIOLOGY Accession or UID: <span class="mark">MYCOLOGY</span>

Accession Date: TODAY// <span class="mark">\<ENTER\></span> (JUN 01, 2011)

Number part of Accession: (1-999999): <span class="mark">2</span>

Work Load Area: MYCOLOGY

Select TEST/PROCEDURE:

None Preselected

Accession \# 2

XXXXXXXXX SSN: XXX-XX-XXXXLOC: CBOC

Pat Info: Sex: MALE Age: 75yr as of Jun 01, 2011

Edit this accession? YES// <span class="mark">\<ENTER\></span>

1 MYCOLOGY CULTURE

MYCOLOGY CULTURE completed: <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: SPUTUM// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

MYCOLOGY RPT STATUS: <span class="mark">P \<ENTER\></span> PRELIMINARY REPORT

Select FUNGUS/YEAST: <span class="mark">CANDIDA GLABRATA</span>

FUNGUS/YEAST ISOLATE NUMBER: 1// <span class="mark">\<ENTER\></span>

ISOLATE ID: 99VA4:581:9-1// <span class="mark">\<ENTER\></span> (No Editing)

QUANTITY: <span class="mark">\<ENTER\></span>

Select COMMENT: <span class="mark">\<ENTER\></span>

Select FUNGUS/YEAST: <span class="mark">\<ENTER\></span>

Select MYCOLOGY RPT REMARK: <span class="mark">\<ENTER\></span>

MYCOLOGY RPT DATE APPROVED: <span class="mark">\<ENTER\></span>

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: HUNTINGTON VAMC// <span class="mark">\<ENTER\></span> WV VAMC 581

Sure you want to add this record? NO// <span class="mark">YES</span>

...assignment created.

Current performing lab assignments:

Mycology Report Performed By: HUNTINGTON VAMC \[CLIA# 51D0987909\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for:

MYCOLOGY CULTURE completed:

### Enter/verify data (auto instrument) \[LRVR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Enter/verify data (auto instrument) \[LRVR\] prompts the user to view results associated to each sequence display when verifying by accession number, where there are multiple results available for the accession number.

<span id="_Toc510168996" class="anchor"></span>Figure 55. Enter/verify data (auto instrument) \[LRVR\]

Select Process data in lab menu \<TEST ACCOUNT\> Option: <span class="mark">EA \<ENTER\></span> Enter/verify data (auto instrument)

Select LOAD/WORK LIST NAME: <span class="mark">VITROS</span>

Select Performing Laboratory: HUNTINGTON VAMC// <span class="mark">\<ENTER\></span> WV VAMC 581

Work Load Area: VITROS// <span class="mark">\<ENTER\></span>

Would you like to see the test list? No// <span class="mark">\<ENTER\></span> NO

Do you wish to modify the test list? NO// <span class="mark">\<ENTER\></span>

You have selected 128 tests to work with.

Do you want to review the data before and after you edit? YES// <span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// <span class="mark">\<ENTER\></span> Accession Number

Accession Date: TODAY// <span class="mark">\<ENTER\></span> (MAY 19, 2011)

Accession NUMBER: 488// <span class="mark">487</span>

ORDER \#: 100278

Seq \#: 78740 Accession: CH 0517 487  

Seq \#: 78740 Accession: CH 0517 487   Results received: May 14, 2011@11:27

                    UID: UNKNOWN            Last updated: May 14, 2011@11:27

 

  Seq \#: 78743 Accession: CH 0517 487   Results received: May 14, 2011@11:35

                    UID: UNKNOWN            Last updated: May 14, 2011@11:35

 

  Seq \#: 80124 Accession: CH 0517 487   Results received: May 17, 2011@20:20

                    UID: 4111370487         Last updated: May 17, 2011@20:20

Select one of the following:

          0         Skip Display

          78740     Seq \# 78740

          78743     Seq \# 78743

          80124     Seq \# 80124

  Display results associated with sequence \#: Skip Display//

### Log-in, anat path \[LRAPLG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Log-in, anat path \[LRAPLG\] requires the input for three new prompts:

Specimen Topography.

Collection Sample.

Laboratory Test.

> <u>LEDI IV Update:</u>

> The option 'Log-in, anat path' \[LRAPLG\] was modified to change the way the system assigns a default accession number when an AP case is accessioned. Previously, the system defaulted to the next available number that followed the last accession number that was used. This option was modified so that every time an AP accession is logged in, the system starts searching from the beginning (#1). The first available accession number that is found in that accession area will be used as the default accession number for the new case being logged in (note: the user will still be able to override the default, and select a different accession number, if they so choose).

> For sites that wish to keep the original method of assigning a default AP accession number, a new Parameter is being introduced that will let the site configure which method the system should use. This new parameter, 'Method of Assigning AP Accession Number', can be edited via the option 'Package Level Parameter Edit' \[LR7O PAR PKG\] on the 'Update CPRS Parameters' \[LR7O PARAM MENU\] menu. See Table 2 LEDI IV Patch Parameters for the values of the settings.

<span id="_Toc510168997" class="anchor"></span>Figure 56. Log-in, anat path \[LRAPLG\]

Select Anatomic pathology Option: <span class="mark">L \<ENTER\></span> Log-in menu, anat path

Select Log-in menu, anat path Option: <span class="mark">?</span>

LI Log-in, anat path

DA Delete accession \#, anat path

PB Print log book

HW Histopathology Worksheet

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Log-in menu, anat path Option: <span class="mark">LI \<ENTER\></span> Log-in, anat path

Select ANATOMIC PATHOLOGY SECTION: <span class="mark">SUR \<ENTER\></span> GICAL PATHOLOGY

Log-In for 2008 ? YES// <span class="mark">\<ENTER\></span> (YES)

Select Patient Name: <span class="mark">LDSI</span>

1 LDSIAP,ONE X-X-55 XXXXXXXXX NO EMPLOYEE

2 LDSIAP,PATIENT X-X-7XXXXXXXXX YES MILITARY RETIREE

3 LDSIAP,SALLY X-X-54 XXXXXXXX7 NO EMPLOYEE

CHOOSE 1-3: <span class="mark">1 \<ENTER\></span> LDSIAP,ONE X-X-55 XXXXXXXX NO EMPLOYEE

LDSIAP,ONE ID: XXXXXXXX

AGE: 53 DATE OF BIRTH: MAY 5,1955

PATIENT LOCATION: 3E// <span class="mark">\<ENTER\></span> 3 EAST

Checking surgical record for this patient...

No operations on record in the past 7 days for this patient.

Assign SURGICAL PATHOLOGY (NSP) accession \#: 13? YES// <span class="mark">\<ENTER\></span> (YES)

Date/time Specimen taken: NOW// <span class="mark">\<ENTER\></span> (SEP 15, 2008@15:17)

SURGEON/PHYSICIAN: <span class="mark">LRPROVIDER,ONE JR \<ENTER\></span> LRPROVIDER,ONE JR WGA

SPECIMEN SUBMITTED BY: <span class="mark">LRPROVIDER,ONE</span>

Select SPECIMEN: <span class="mark">TISSUE</span>

SPECIMEN TOPOGRAPHY: <span class="mark">TISSUE</span>

1 TISSUE 00001A

2 TISSUE EOSINOPHIL 05145

3 TISSUE NEUTROPHIL 05147

4 TISSUE, SUBCUTANEOUS SUBCUTANEOUS TISSUE 03000

CHOOSE 1-4: <span class="mark">1 \<ENTER\></span> TISSUE 00001A

COLLECTION SAMPLE: <span class="mark">TISSUE \<ENTER\></span> TISSUE

Select SPECIMEN: <span class="mark">\<ENTER\></span>

DATE/TIME SPECIMEN RECEIVED: NOW// <span class="mark">\<ENTER\></span> (SEP 15, 2008@15:18)

PATHOLOGIST: <span class="mark">LRPROVIDER,ONE \<ENTER\></span> JR LRPROVIDER,ONE JR WGA

Select COMMENT: <span class="mark">\<ENTER\></span>

FROZEN SECTION: <span class="mark">\<ENTER\></span>

1\>

Select LABORATORY TEST: <span class="mark">TISSUE EXAM \<ENTER\></span> SP

Select Patient Name: <span class="mark">\<ENTER\></span>

Select Log-in menu, anat path Option: <span class="mark">\<ENTER\></span>

Select Anatomic pathology Option: <span class="mark">\<ENTER\></span>

Select Laboratory DHCP Menu

<span id="_Toc510168998" class="anchor"></span>Figure 57. Sample of the AP Log Book where the display of related surgical information is enabled

Select OPTION NAME: <span class="mark">LRAPBK \<ENTER\></span> Print log book

Print log book

Select ANATOMIC PATHOLOGY SECTION: <span class="mark">SURGICAL PATHOLOGY</span>

SURGICAL PATHOLOGY LOG BOOK

Select one of the following:

0 No

1 Yes

2 Only Topography and Morphology Codes

Print SNOMED codes: No// <span class="mark">\<ENTER\></span>

Print Single Accession? NO// <span class="mark">Y \<ENTER\></span> YES

Select SURGICAL PATHOLOGY Accession or UID: <span class="mark">NSP 08 20</span>

SURGICAL PATHOLOGY (2008) 20

DEVICE: HOME// <span class="mark">;;9999</span><span class="mark">\<ENTER\></span> UCX/TELNET

Mar 14, 2012 18:00 ZZ BONHAM Pg: 1

LOG BOOK entry for accession NSP 08 20

\# =Demographic data in file other than PATIENT file

Date Num Patient ID LOC PHYSICIAN PATHOLOGIST

-------------------------------------------------------------------------------

Oct/07 20 LRPATIENT,ONE JR 1111 1T LRUSER,ONE LRUSER,ONE

Patient ID: 000-00-1111

InPatient Accession \[UID\]: NSP 08 20 \[0000000000\]

Date specimen taken: Oct 07, 2008@09:43 Entered by: LRUSER,ONE

FIFTH BIG TOE

OTHER BIG TOE

Related Surgery Case \#35

BRIEF CLINICAL HISTORY: Information automatically documented from SURGERY package case \#35 Field (#60) BRIEF CLIN HISTORY

PREOPERATIVE DIAGNOSIS: Information automatically documented from SURGERY package case \#35 Field (#32) PRINCIPAL PRE-OP DIAGNOSIS,

(#.72) OTHER PREOP DIAGNOSIS

POSTOPERATIVE DIAGNOSIS: Information automatically documented from SURGERY package case \#35 Field (#34) PRINCIPAL POST-OP DIAG,

(#.74) OTHER POSTOP DIAGS

-------------------------------------------------------------------------------

Select SURGICAL PATHOLOGY Accession or UID:

### Anatomic Pathology Performing Laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Anatomic Pathology data entry options, the user can designate the performing laboratory for the entire report or for specific sections of the report. If choosing to enter the performing laboratory for specific sections, only the sections that have data entered will appear. If the site requires a Performing Laboratory other than the default local Institution Name, then the Institution must be in File 4 as either a National or Local entry and the LIM must set up a Lab Shipping Configuration for the performing laboratory. See section 5.4.2 Edit Shipping Configuration \[LA7S EDIT 62.9\].

<span id="_Toc510168999" class="anchor"></span>Figure 58. Sample AP Designation of Performing Laboratory for Report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: *Editor Note: Enter the performing Institution Name here.*

Sure you want to add this record? NO// <span class="mark">YES</span>

...assignment created.

Current performing lab assignments:

Surgical Pathology Report Performed By:

*(#1 Institution Name)*

Select one of the following:

1 Entire report

2Specific sections of report

Designate performing laboratory for: 1// <span class="mark">2 \<ENTER\></span> Specific sections of report

1 - Brief Clinical History

2 - Preoperative Diagnosis

3 - Post-Operative Diagnosis

4 - Gross Description

5 - Frozen Section

Select the section to designate (1-5): <span class="mark">1</span>

Select Performing Laboratory: *Editor Note:Enter thedesignate Institution Name here.*

Sure you want to add this record? NO// <span class="mark">YES</span>

... assignment created.

Current performing lab assignments:

Brief Clinical History Performed By:

*(#2 Institution Name)*

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">2</span> <span class="mark">\<ENTER\></span> Specific sections of report

Note 1: Next to Select Performing Laboratory on line 2 of the view, Enter the performing Institution Name,

Note 2: Next to Select Performing Laboratory on line 20 of the view, Enter the designate Institution Name.

### Add tests to a given accession \[LRADD TO ACC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Add tests to a given accession \[LRADD TO ACC\] was modified to allow the selection of the type of test order added.

<span id="_Toc510169000" class="anchor"></span>Figure 59. Add tests to a given accession \[LRADD TO ACC\]

Select Accessioning menu \<TEST ACCOUNT\> Option: <span class="mark">ADD TESTS TO A GIVEN ACCESSION</span>

Select Accession or UID: <span class="mark">CHEMISTRY</span>

CHEMISTRY

  Accession Date: TODAY// <span class="mark">\<ENTER\></span> (MAY 17, 2011)

  Number part of Accession:  (1-999999): <span class="mark">1</span>

LEDITEST,PATIENTONE             000-00-1111

Nature of Order/Change: POLICY// <span class="mark">\<ENTER\></span>    I

TESTS ALREADY ON THE ACCESSION:

     CREATININE

     UREA NITROGEN

     GLUCOSE

     SODIUM

     POTASSIUM

     CHLORIDE

     CO2

     CALCIUM

     ANION GAP

     ELECTROLYTE 7

Select Original Ordered Test: ELECTROLYTE 7 

Add LABORATORY TEST: <span class="mark">TSH \<ENTER\></span> TSH (LAB)

  ...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

     Select one of the following:

          1         Add On

          2         Reflex

Type of test order being added: <span class="mark">1 \<ENTER\></span> Add On

TSH (LAB) ADDED

### Add a New Internal Name for an Antibiotic \[LRWU7\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This existing option was expanded to allow editing of mycobacterium antibiotics.

<span id="_Toc510169001" class="anchor"></span>Figure 60. Add a new internal name for an antibiotic \[LRWU7\]

Select Lab liaison menu Option: <span class="mark">?</span>

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

Edit Inactive Date - COLLECTION SAMPLE

Edit Inactive Date - TOPOGRAPHY FIELD

File list for lab

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits

Select Lab liaison menu Option: <span class="mark">ADD A NEW INTERNAL NAME FOR AN ANTIBIOTIC</span>

Select one of the following:

1 Bacterial Antibiotic

2 Mycobacterium Antibiotic

Select Antibiotic Type to Add: 1// <span class="mark">\<ENTER\></span> Bacterial Antibiotic

Enter the name of the new antibiotic you wish to create: <span class="mark">NEW ANTIOBIOTIC</span>

Checking if field exists...OK

(DRUG NODE will be 2.00581067)

Are you sure you wish to create NEW ANTIOBIOTIC? NO// <span class="mark">YES</span>

TEST ANTIOBIOTIC has now been created.

You must now add a new antibiotic in the ANTIMICROBIAL SUSCEPTIBILITY file

and use TEST ANTIOBIOTIC as the entry for the INTERNAL NAME field.

Do you want to setup NEW ANTIOBIOTIC as a new Bacterial Antibiotic? NO// <span class="mark">YES</span>

NAME: NEW ANTIOBIOTIC//

INTERNAL NAME: 2.00581067// NEW ANTIOBIOTIC

DISPLAY COMMENT:

ABBREVIATION:

DEFAULT SCREEN: ALWAYS DISPLAY

PRINT ORDER: 25

Select SUSCEPTIBILITY RESULT:

NATIONAL VA LAB CODE: NEW ANTIBIOTIC

### Delete entire order or individual tests \[LRCENDEL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Delete entire order or individual tests \[LRCENDEL\] was modified to prevent a user from "Not Performing" (NP) any tests that have results. This applies even if the results have not yet been verified. Note: Shortened the actual length of the screen to remove excess space and cut down on paper.

<span id="_Toc510169002" class="anchor"></span>Figure 61. Delete entire order or individual tests \[LRCENDEL\]

Select Accessioning menu Option: DELETE ENTIRE order or individual tests

ENTER ORDER NUMBER: : (1-9999999999): <span class="mark">361</span>

Order Test Urgency Status Accession

-Lab Order \# 361 Provider: LRUSER,TWO

BLOOD

CBC ROUTINE Collected 07/17/2012@12:08 HE 0717 1

LRPATIENT,TWO 000-00-9934

Test result(s) already entered for this order; cannot change order.

You must select individual test using the 'Delete test from accession' option.

Can't change status of test(s) on this order.

ENTER ORDER NUMBER: : (1-9999999999):

### Microbiology Performing Laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV adds the capability to designate the performing laboratory for the entire AP or Micro report or for specific sections of the report. For sites that do all their AP or Micro tests in house (and do not send them out), it can be cumbersome to assign a performing lab each time they enter an AP or Micro result.

Two new parameters were created that allow the site to skip the prompt for performing laboratory: 'Ask Performing Lab AP' and 'Ask Performing Lab Micro'. They can set the value to either 'Yes' or 'No'. If they set the parameter to 'No', the system will not prompt the user to designate a performing lab, and the system will automatically assign a performing lab (based on the algorithm explained below). Sites that send AP and Micro tests to another lab (some or all of the report; all the time, or only in certain scenarios) should maintain the ability to designate the performing lab when they verify the report, and should not choose to set the parameter to not ask for a performing lab.

If the user sets the parameter to not ask for a performing lab, the system automatically assigns a performing lab to the entire report based off these conditions:

If the user entering results has their 'Default Performing Laboratory' parameter set to a default Institution, that Institution will be used as the performing lab.

If that parameter is not set for the user, the system will use the DUZ(2) (the user's Institution) as the performing lab.

Within Microbiology result entry options, the user can designate the performing laboratory for the entire report or for specific sections of the report. If choosing to enter the performing laboratory for specific sections, only the sections that have data entered will appear for selection.

<span id="_Toc510169003" class="anchor"></span>Figure 62. Microbiology Assigning Performing Laboratory for Entire Report

CULTURE & SUSCEPTIBILITY completed: <span class="mark">N\<ENTER\></span> (JUL 17, 2012@12:54)

COLLECTION SAMPLE: BLOOD// <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: SERUM// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Select GRAM STAIN: <span class="mark">NEGATIVE</span> <span class="mark">\<ENTER\></span>

(NEGATIVE)

Select GRAM STAIN: <span class="mark">\<ENTER\></span>

BACT RPT STATUS: <span class="mark">F</span><span class="mark">\<ENTER\></span> FINAL REPORT

Select ORGANISM: <span class="mark">\<ENTER\></span>

Select BACT RPT REMARK: <span class="mark">\<ENTER\></span>

BACT RPT DATE APPROVED: <span class="mark">N\<ENTER\></span> (JUL 17, 2012@12:54)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: ZZ BONHAM// <span class="mark">\<ENTER\></span> TX VAMC 522 INACTIVE Jan 01, 1997

Sure you want to add this record? NO// <span class="mark">YES\<ENTER\></span>

...assignment created.

Current performing lab assignments:

Bacteriology Report Performed By: ZZ BONHAM \[CLIA# 987654321\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

CULTURE & SUSCEPTIBILITY completed: 07/17/2012 12:54 // <span class="mark">\<ENTER\></span>

Send a CPRS Alert/Notification? YES// <span class="mark">NO</span> <span class="mark">\<ENTER\></span>

(D)isplay (A)dd Work Load <span class="mark">\<ENTER\></span>

Accession \#: <span class="mark">\<ENTER\></span>

<span id="_Toc510169004" class="anchor"></span>Figure 63. Microbiology Assigning Performing Laboratory for Specific Sections of Report

CULTURE & SUSCEPTIBILITY completed: <span class="mark">N\<ENTER\></span> (JUL 17, 2012@12:21)

COLLECTION SAMPLE: BLOOD// <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: SERUM// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Select GRAM STAIN: <span class="mark">NEGATIVE</span> <span class="mark">\<ENTER\></span>

(NEGATIVE)

Select GRAM STAIN: <span class="mark">\<ENTER\></span>

BACT RPT STATUS: <span class="mark">F\<ENTER\></span> FINAL REPORT

Select ORGANISM: <span class="mark">STAPHYLOCOCCUS AUREUS</span><span class="mark">\<ENTER\></span> 2441 3092008 SCT Organism

ORGANISM ISOLATE NUMBER: 1// <span class="mark">\<ENTER\></span>

This entry is mapped in File \#62.47

ORGANISM: STAPHYLOCOCCUS AUREUS// <span class="mark">\<ENTER\></span>

QUANTITY: <span class="mark">\<ENTER\></span>

Select COMMENT: <span class="mark">\<ENTER\></span>

PENICILLIN: <span class="mark">\<ENTER\></span>

CLINDAMYCIN: <span class="mark">S</span><span class="mark">\<ENTER\></span> (SUS)

VANCOMYCIN: <span class="mark">S</span><span class="mark">\<ENTER\></span> (6)

GENTAMICIN: <span class="mark">S</span> <span class="mark">\<ENTER\></span> (S)

CHLORAMPHENICOL: <span class="mark">\<ENTER\></span>

TETRACYCLINE: <span class="mark">\<ENTER\></span>

AMPICILLIN: <span class="mark">\<ENTER\></span>

NITROFURANTOIN: <span class="mark">\<ENTER\></span>

ERYTHROMYCIN: <span class="mark">\<ENTER\></span>

OXACILLIN: <span class="mark">R\<ENTER\></span> (RESIS)

CEPHALOTHIN: <span class="mark">\<ENTER\></span>

1 STAPHYLOCOCCUS AUREUS

Select ORGANISM: <span class="mark">\<ENTER\></span>

Select BACT RPT REMARK: <span class="mark">\<ENTER\></span>

BACT RPT DATE APPROVED: <span class="mark">N\<ENTER\></span> (JUL 17, 2012@12:23)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">2\<ENTER\></span> Specific sections of report

1 - Bacteriology Report

2 - Gram Stain

3 - Organism Identification

4 - Comment On Specimen

Select the section to designate (1-4): <span class="mark">3\<ENTER\></span>

1 - STAPHYLOCOCCUS AUREUS including All Susceptibilities

1.1 - STAPHYLOCOCCUS AUREUS Specific Susceptibilities

2 - ALL items

Select the item to designate (1-2): <span class="mark">1.1\<ENTER\></span>

1 - Clindam

2 - Vancmcn

3 - Gentmcn

4 - Oxacillin

Select the item to designate (1-4): <span class="mark">4\<ENTER\></span>

Select Performing Laboratory: ZZ BONHAM// <span class="mark">REGION 7 ISC,TX (FS)</span><span class="mark">\<ENTER\></span> TX 170

Sure you want to add this record? NO// <span class="mark">Y\<ENTER\></span> YES

...assignment created.

Current performing lab assignments:

Staphylococcus Aureus Oxacillin Susceptibility Performed By:

Dallas Office of Information Field Office - Lab Development \[CLIA# 123445689\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

CULTURE & SUSCEPTIBILITY completed: 07/17/2012 12:21 // <span class="mark">\<ENTER\></span>

Send a CPRS Alert/Notification? YES// <span class="mark">NO \<ENTER\></span>

(D)isplay (A)dd Work Load

Accession \#: <span class="mark">\<ENTER\></span>

### Microbiology Sending an Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within Microbiology result entry options, the user can opt to send one of three alert types to the ordering provider and additional recipients and/or mail groups. Depending on how the ‘Prompt CPRS Alert in Micro Result Entry’ parameter is set, will determine whether the user is prompted to send an alert. The three alert types are:

- Lab results available.
- Abnormal lab results.
- Critical lab results.

|                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NOTE: The type of alert generated either depends on whether the clinician has set the parameter for personal alerts in CPRS, or if the alert is mandatory at the system level. |
| Reference: For additional details on these alerts, see the “APPENDIX B: HOW NOTIFICATIONS WORK - TECHNICAL OVERVIEW” section in the CPRS Technical Manual on the VDL.      |

<span id="_Toc510169005" class="anchor"></span>Figure 64. Sending an Alert - Microbiology

CULTURE & SUSCEPTIBILITY completed: <span class="mark">N \<ENTER\></span> (MAY 05, 2011@17:45)

COLLECTION SAMPLE: URINE// <span class="mark">\<ENTER\></span>

SITE/SPECIMEN: URINE// <span class="mark">\<ENTER\></span>

COMMENT ON SPECIMEN: <span class="mark">\<ENTER\></span>

Select GRAM STAIN: <span class="mark">NEGATIVE</span>

BACT RPT STATUS: <span class="mark">F \<ENTER\></span> FINAL REPORT

URINE SCREEN: <span class="mark">NEGATIVE \<ENTER\></span> NEGATIVE

Select ORGANISM: <span class="mark">\<ENTER\></span>

Select BACT RPT REMARK: <span class="mark">\<ENTER\></span>

BACT RPT DATE APPROVED: <span class="mark">N \<ENTER\></span> (MAY 05, 2011@17:45)

Current performing lab assignments: None Listed

Select one of the following:

1 Entire report

2 Specific sections of report

Designate performing laboratory for: 1// <span class="mark">\<ENTER\></span> Entire report

Select Performing Laboratory: LEXINGTON-LD VAMC// <span class="mark">\<ENTER\></span> KY VAMC 596

Sure you want to add this record? NO// <span class="mark">YES</span>

...assignment created.

Current performing lab assignments:

Bacteriology Report Performed By: LEXINGTON VA MEDICAL CENTER \[CLIA# 18D1086610\]

Select one of the following:

1 Entire report

2 Specific sections of report

3 Delete performing laboratory

Designate performing laboratory for: <span class="mark">\<ENTER\></span>

CULTURE & SUSCEPTIBILITY completed: 05/05/2011 17:45 //

Send a CPRS Alert/Notification? NO// <span class="mark">YES \<ENTER\></span>

Select TEST: <span class="mark">CULTURE & SUSCEPTIBILITY</span><span class="mark">\<ENTER\></span>

Select one of the following:

1 Lab results available

2 Abnormal lab results

3 Critical lab results

Enter response: <span class="mark">1 \<ENTER\></span> Lab results available

The current recipients will be:

LEDIIVPROVIDER.ONE \[Outpatient Primary Care Provider\]

LEDIIVPROVIDEER.TWO \[Ordering Provider\]

Send the alert to additional recipients and/or mail groups? NO// <span class="mark">\<ENTER\></span>

The current recipients will be:

LEDIIVPROVIDER.ONE \[Outpatient Primary Care Provider\]

LEDIIVPROVIDEER.TWO \[Ordering Provider\]

Send Alert? YES// <span class="mark">\<ENTER\></span> ...Alert Sent

(D)isplay (A)dd Work Load

Accession \#:

### The Add/Remove a Shipping Manifest Test’ \[LA7S MANIFEST TEST ADD/REMOVE\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option was modified to restrict adding/removing tests from a cancelled shipping manifest. The option will only allow a test to be added or removed from an “Open” or “Closed” shipping manifest.

### Enter/verify/modify data (manual) \[LRENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The option Enter/verify/modify data (manual) \[LRENTER\] was modified to allow holders of the LRDATA Security Key to change the Units and Reference Ranges for a result by entering a tilde (~) at the lab result prompt.

> See below for an example of this new feature.

<span id="_Toc510169006" class="anchor"></span>Figure 65. Enter/verify/modify data (manual) \[LRENTER\]

Select Process data in lab menu Option: <span class="mark">EM \<ENTER\></span> Enter/verify/modify data (manual)

Do you want to review the data before and after you edit? YES// <span class="mark">\<ENTER\></span>

Do you wish to see all previously verified results? NO// <span class="mark">\<ENTER\></span>

Select one of the following:

1 Accession Number

2 Unique Identifier (UID)

Verify by: 1// <span class="mark">2</span><span class="mark">\<ENTER\></span> Unique Identifier (UID)

Unique Identifier: L621350001 <span class="mark">\<ENTER\></span> (CH 0514 1)

Select Performing Laboratory: LEDIA// <span class="mark">\<ENTER\></span> 980

BCMA,SEVEN-PATIENT 111-11-1111 LOC:BCMA

Sample: BLOOD

These results have been approved by LRUSER,ONE on May 14, 2012@09:22:40

Specimen: SERUM

1 GLUCOSE verified

BCMA,SEVEN-PATIENT SSN: 111-11-1111 LOC: BCMA

Pat Info: Sex: MALE Age: 77yr as of May 14, 2012

Provider: LRUSER,ONE Voice pager:

Phone: 6655544 Digital pager:

ACCESSION: CH 0321 2 CH 0514 1 \[L621350001\]

3/21 14:01d 5/14 09:22d

GLUCOSE 90 120 H mg/dL

COMMENTS: <span class="mark">TEST EDITTING RANGES</span>

If you need to change something, enter your initials: <span class="mark">LU \<ENTER\></span>

SELECT ('E' to Edit, 'C' for Comments, 'W' Workload): <span class="mark">Edit</span><span class="mark">\<ENTER\></span>

GLUCOSE 120//~

Current Laboratory Test File Values

Current Ref Range: 60-110 Units: mg/dL

Critical Low: 50 Critical High: 300

Use these values? NO// <span class="mark">\<ENTER\></span>

For test GLUCOSE

UNITS: mg/dL// <span class="mark">\<ENTER\></span>mg/dL

REFERENCE LOW: 60// 70 <span class="mark">\<ENTER\></span>

REFERENCE HIGH: 110// 120 <span class="mark">\<ENTER\></span>

CRITICAL LOW: 50// <span class="mark">\<ENTER\></span> 50

CRITICAL HIGH: 300// <span class="mark">\<ENTER\></span> 300

Result's Abnormality: Abnormal High// <span class="mark">?</span><span class="mark">\<ENTER\></span>

Select the abnormality if it cannot be calculated from reference values.

Select one of the following:

0 Calculate from entered values

1 Abnormal Low

2 Critical Low

3 Abnormal High

4 Critical High

Result's Abnormality: Abnormal High// <span class="mark">0</span><span class="mark">\<ENTER\></span> Calculate from entered values

GLUCOSE 120// <span class="mark">\<ENTER\></span>

Select COMMENT: EDITTING REF RANGES // <span class="mark">\<ENTER\></span>

COMMENT: EDITTING REF RANGES Replace <span class="mark">\<ENTER\></span>

Select COMMENT: <span class="mark">\<ENTER\></span>

BCMA,SEVEN-PATIENT SSN: 111-11-1111 LOC: BCMA

Pat Info: Sex: MALE Age: 77yr as of May 14, 2012

Provider: LRUSER,ONE Voice pager:

Phone: 6655544 Digital pager:

ACCESSION: CH 0321 2 CH 0514 1 \[L621350001\]

3/21 14:01d 5/14 09:22d

GLUCOSE 90 120 mg/dL

COMMENTS: <span class="mark">EDITTING REF RANGES</span>

If you need to change something, enter your initials: <span class="mark">\<ENTER\></span>

Approve update of data by entering your initials: <span class="mark">LU</span><span class="mark">\<ENTER\></span>

GLUCOSE flagged incorrectly as H by \[18-VA980\].

Changed to normal on May 14, 2012@09:25 by \[18-VA980\].

GLUCOSE reference low reported incorrectly as 60 by \[18-VA980\].

Changed to 70 on May 14, 2012@09:25 by \[18-VA980\].

GLUCOSE reference high reported incorrectly as 110 by \[18-VA980\].

Changed to 120 on May 14, 2012@09:25 by \[18-VA980\].

Unique Identifier: <span class="mark">\<ENTER\></span>

### Print log book \[LRAPBK\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The accession number can be entered by using the \<ACCESSION AREA\> \<DATE\> \<NUMBER\> format or UID in the 10-15 character formats. The AP Log Book now displays the UID for all entries. Two samples of the same view are presented below. The first has the user selecting by Accession number. The second has the user selecting by UID.

<span id="_Toc510169007" class="anchor"></span>Figure 66. Print log book \[LRAPBK\] Select by Accession

Data entry for 2008 ? YES// <span class="mark">\<ENTER\></span> (YES)

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// 1 Accession number

Enter Accession Number: 1

Enter the year 2008 SURGICAL PATHOLOGY accession number to be updated.

Enter Accession Number: 1 for 2008

Second Sample of Print Log Book- Select by UID

Data entry for 2008 ? YES// <span class="mark">\<ENTER\></span> (YES)

Enter the year 2008 SURGICAL PATHOLOGY accession number to be updated.

Enter Accession Number: 1 for 2008

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1// 2 Unique Identifier (UID)

Unique Identifier: 1513000002 (SP-LX 13 1) for 2008

### Change How Not-Performed ("NP") Tests Work in LEDI IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV is made "NP aware" so that it will send a message back to the LEDI collecting site when the Host site NP's a test. When the Host site NP's a test, an HL7 message will be sent back to the Collecting site. At the Collecting site, a LA7 ORDER STATUS CHANGED bulletin and an alert will be sent out to the mail group specified in the Message Configuration to receive "New Results" alerts.

If the Host site NP'ed the entire ordered test (from a non-exploded panel), the HL7 message being sent back will not contain a result (in the OBX), but will just contain the Test result comments. The Collecting site will need to:

1.  Delete test from an accession \[LRTSTOUT\], or Delete Entire Order of Individual Test \[LRCENDEL\] if there are no results already verified on the order.
2.  Enter/verify/modify data (manual) \[LRENTER\].

However, if the Host site NP'ed individual tests from an exploded panel, then a result of "canc" will be sent back to the Collecting site for the individual tests from the panel that were Not Performed.

<span id="_Toc510169008" class="anchor"></span>Figure 67. Sample LA7 ORDER STATUS CHANGED

Subj: LAB ORDER STATUS CHANGED  \[#62133\] 10/03/11@12:44  24 lines

From: LAB PACKAGE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

An order status change has been received for a patient via a HL7 interface

that indicates the order has been changed. Please use the appropriate

laboratory option to update this order on this system.

  

 Action: No results available; Order canceled.

      Interface: LA7V HOST 123

    File \#62.49: 142

   Patient Name: LRPATIENT,ONE

     Patient ID: 000001234

    Specimen ID: L612760003

Collection D/T: Oct 03, 2011@12:42

   Test/analyte: Lipid Panel \[81132.0000\]

  Producer's ID: LRPRODUCER1

       Manifest: 123-20111003-3

Comments:

\*LIPID PROFILE Not Performed: Oct 03, 2011@12:43 by 123456

\*NP Reason: CONTAMINATED SAMPLE

Enter message action (in IN basket): Ignore//

### Cumulative Report Modifications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cumulative Report was modified so that when the ‘Date/Time Obtained Inexact’ field is set to ‘Yes’ for an Accession, the Cumulative Report will just display the Collection Date (without the time) for that accession.

<span id="_Toc510169009" class="anchor"></span>Figure 68. Cumulative Report

---- CHEM II Profile ----

PLASMA FBS

Ref range low 60

Ref range high 123

mg/dL

-------------------------------------------------------------------------------

\[a\] Jul 09, 2012 120

\[c\] Jun 26, 2012 10:20 145 H

\[d\] Jun 26, 2012 10:13 110

\[g\] May 31, 2012 16:06 130 H

\[i\] Feb 08, 2012 09:48 110

## Modified Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following report options are modified to display the facilities at which the laboratories are performed and reported, and the name/address of the facility at which the report is printed to comply with Federal CLIA regulations.

<span id="_Toc510169010" class="anchor"></span>Figure 69. Interim report \[LRRP2\]

Select Results menu Option: <span class="mark">INTERIM</span>

1 Interim report

2 Interim report by provider

3 Interim report for an accession

4 Interim report for chosen tests

5 Interim report for selected tests as ordered

6 Interim reports by location (manual queue)

7 Interim reports for 1 location (manual queue)

8 Interim reports for 1 provider (manual queue)

CHOOSE 1-8: <span class="mark">1 \<ENTER\></span> Interim report

Select Patient Name: <span class="mark">LEDIPATIENT,ONE JR \<ENTER\></span> LRPATIENT,ONE JR X-XX-20 000001111 NO NSC VETERAN

Date to START with: TODAY// <span class="mark">\<ENTER\></span> (SEP 05, 2008)

Date to END with: T-7// <span class="mark">\<ENTER\></span> (AUG 29, 2008)

Print address page? NO// <span class="mark">Y \<ENTER\></span> YES

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 05, 2008@11:23

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0482490012\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:23 PRESS '^' TO STOP

page 2

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:24

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Patient Name:

### Interim report by provider \[LRRD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169011" class="anchor"></span>Figure 70. Interim report by provider \[LRRD\]

Select Results menu Option: <span class="mark">INTERIM REPORT BY PROVIDER</span>

Date to START with: TODAY// <span class="mark">\<ENTER\></span> (SEP 05, 2008)

Date to END with: AUG 6,2008// <span class="mark">\<ENTER\></span> (AUG 06, 2008)

Print address page? NO// <span class="mark">Y \<ENTER\></span> YES

Do you want (A)ll providers, a (R)ange of providers,

or (S)elected providers? S// <span class="mark">\<ENTER\></span>

Select PROVIDER NAME: <span class="mark">LRPROVIDER,ONE JR \<ENTER\></span> WGA

Select PROVIDER NAME: <span class="mark">\<ENTER\></span>

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 05, 2008@11:29

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0482490012\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:29 PRESS '^' TO STOP

LEDIPATIENT,ONE JR 000-00-1111 AGE: 88 LOC: 1 TEST (NORTH)Sep 05, 2008@11:30

----MICROBIOLOGY---- page 1

Printed at:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Accession \[UID\]: MICRO 08 11 \[1408000011\]

Collection sample: THROAT SWAB Collection date: Aug 21, 2008 11:58

Provider: LRPROVIDER,ONE JR

=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=

\* BACTERIOLOGY PRELIMINARY REPORT =\> Aug 21, 2008 13:21 TECH CODE: 235

GRAM STAIN: TESTING STUFFING PL DURING LRMISTF

Bacteriology Remark(s):

TESTING PL ENTRY

=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--

Performing Laboratory:

Gram Stain Performed By:

TRIPLER ARMY MEDICAL CENTER

1 JARRETT WHITE ROAD HONOLULU, HI 96859-5000

Bact Report Remark Performed By:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

\+ + + End of Report + + + End of Report + + + End of Report + + +

LEDIPATIENT,ONE JR 000-00-1111 ROUTING: 1T '^' TO STOP

LEDIPATIENT,ONE JR 000-00-1111 AGE: 88 LOC: 1 TEST (NORTH)Sep 05, 2008@11:30

----MICROBIOLOGY---- page 1

Printed at:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Accession \[UID\]: MICRO 08 10 \[1408000010\]

Collection sample: THROAT SWAB Collection date: Aug 20, 2008 17:25

Provider: LRPROVIDER,ONE JR

Test(s) ordered: GRAM STAIN completed: Aug 20, 2008 17:26

\* BACTERIOLOGY PRELIMINARY REPORT =\> Aug 20, 2008 17:26 TECH CODE: 235

GRAM STAIN: TESTING GRAM STAIN BATCH ENTRY AND PL SAVING

Performing Laboratory:

Gram Stain Performed By:

TRIPLER ARMY MEDICAL CENTER

1 JARRETT WHITE ROAD HONOLULU, HI 96859-5000

\+ + + End of Report + + + End of Report + + + End of Report + + +

LEDIPATIENT,ONE JR 000-00-1111 ROUTING: 1T '^' TO STOP

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:30 PRESS '^' TO STOP

page 2

LRPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:30

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

page 3

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:30

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Results menu Option:

### Interim report for chosen tests \[LRRP3\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169012" class="anchor"></span>Figure 71. Interim report for chosen tests \[LRRP3\]

Select Results menu Option: <span class="mark">INT</span>

1 Interim report

2 Interim report by provider

3 Interim report for an accession

4 Interim report for chosen tests

5 Interim report for selected tests as ordered

6 Interim reports by location (manual queue)

7 Interim reports for 1 location (manual queue)

8 Interim reports for 1 provider (manual queue)

CHOOSE 1-8: <span class="mark">4 \<ENTER\></span> Interim report for chosen tests

GENERAL LAB DATA DISPLAY

Select Patient Name: LEDIPATIENT,ONE JR 2-12-20 000001111 NO

NSC VETERAN

Select LABORATORY TEST NAME: <span class="mark">GLUCOSE \<ENTER\></span> FBS

Select LABORATORY TEST NAME: <span class="mark">\<ENTER\></span>

Date to START with: TODAY// <span class="mark">\<ENTER\></span> (SEP 05, 2008)

Date to END with: T-7// <span class="mark">\<ENTER\></span> (AUG 29, 2008)

Print address page? NO// <span class="mark">Y \<ENTER\></span> YES

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 05, 2008@11:41

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0000000000\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:41 PRESS '^' TO STOP

page 2

LEDIPATIENT,ONE JR 000-00-1111 Sep 05, 2008@11:41

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

### Interim report for selected tests as ordered \[LRRSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169013" class="anchor"></span>Figure 72. Interim report for selected tests as ordered \[LRRSP\]

Select Results menu Option: <span class="mark">INTERIM REPORT FOR SELECTED TESTS AS ORDERED</span>

Select Patient Name: <span class="mark">LEDIPATIENT,ONE JR</span> <span class="mark">\<Enter\></span> 2-12-20 000001111

NO NSC VETERAN

WARNING : You may have selected a test patient.

Select ORDERED TEST: ANY// <span class="mark">GLUCOSE</span> <span class="mark">\<Enter\></span> FBS

Date to START with: TODAY// <span class="mark">\<Enter\></span> (SEP 12, 2008)

Date to END with: T-7// <span class="mark">\<Enter\></span> (SEP 05, 2008)

Print address page? NO// <span class="mark">Y \<Enter\></span> YES

DEVICE: HOME// <span class="mark">;;1000 \<Enter\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<Enter\></span>

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 12, 2008@11:48

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0000000000\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 12, 2008@11:48 PRESS '^' TO STOP

page 2

LEDIPATIENT,ONE JR 000-00-1111 Sep 12, 2008@11:48

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Patient Name: <span class="mark">\<Enter\></span>

Select Results menu Option:

### Interim reports by location (manual queue) \[LRRS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169014" class="anchor"></span>Figure 73. Interim reports by location (manual queue) \[LRRS\]

Select Results menu Option: <span class="mark">INTERIM REPORTS BY LOCATION (MANUAL QUEUE)</span>

Print address page? NO// <span class="mark">Y \<Enter\></span> YES

Date to START with: TODAY// <span class="mark">\<Enter\></span> (SEP 18, 2008)

Date to END with: T-7// <span class="mark">T-18 \<Enter\></span> (AUG 31, 2008)

Select one of the following:

S Selected Locations

R A Range of locations

A All locations

Please select one of the following: <span class="mark">A \<Enter\></span> All locations

DEVICE: HOME// <span class="mark">;;1000 \<Enter\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<Enter\></span>

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 18, 2008@12:16

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0000000000\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:16 PRESS '^' TO STOP

page 2

LRPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:16

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Results menu Option:

### Interim reports for 1 location (manual queue) \[LRRS BY LOC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169015" class="anchor"></span>Figure 74. Interim reports for 1 location (manual queue) \[LRRS BY LOC\]

Select Results menu Option: <span class="mark">INTER</span>

1 Interim report

2 Interim report by provider

3 Interim report for an accession

4 Interim report for chosen tests

5 Interim report for selected tests as ordered

6 Interim reports by location (manual queue)

7 Interim reports for 1 location (manual queue)

8 Interim reports for 1 provider (manual queue)

CHOOSE 1-8: <span class="mark">7 \<ENTER\></span> Interim reports for 1 location (manual queue)

DAILY REPORT FOR DAY: TODAY// <span class="mark">9/5/08 \<ENTER\></span> (SEP 05, 2008)

Print address page? NO// <span class="mark">Y \<ENTER\></span> YES

Select Report Location: <span class="mark">2 \<ENTER\></span> 1 TEST (NORTH)

...OK? Yes// <span class="mark">\<ENTER\></span> (Yes)

Select Report Location:

DEVICE: HOME// <span class="mark">;;100 \<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 18, 2008@12:10

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LRPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0000000000\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:10 PRESS '^' TO STOP

page 2

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:10

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Results menu Option:

### Interim reports for 1 provider (manual queue) \[LRRD BY MD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169016" class="anchor"></span>Figure 75. Interim reports for 1 provider (manual queue) \[LRRD BY MD\]

Select Results menu Option: <span class="mark">INTERIM</span>

1 Interim report

2 Interim report by provider

3 Interim report for an accession

4 Interim report for chosen tests

5 Interim report for selected tests as ordered

6 Interim reports by location (manual queue)

7 Interim reports for 1 location (manual queue)

8 Interim reports for 1 provider (manual queue)

CHOOSE 1-8: <span class="mark">8</span> Interim reports for 1 provider (manual queue)

Date to START with: TODAY// <span class="mark">\<ENTER\></span> (SEP 18, 2008)

Date to END with: AUG 19,2008// <span class="mark">\<ENTER\></span> (AUG 19, 2008)

Print address page? NO// <span class="mark">Y \<ENTER\></span> YES

Select PROVIDER NAME: <span class="mark">LRPROVIDER,ONE JR \<ENTER\></span> WGA

DEVICE: HOME// <span class="mark">;;1000 \<ENTER\></span> UCX/TELNET Right Margin: 80// <span class="mark">\<ENTER\></span>

Printed at: page 1

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

LEDIPATIENT,ONE JR Report date: Sep 18, 2008@12:25

Pat ID: 000-00-1111 SEX: M DOB: Feb 12, 1920 LOC: 1T

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Provider: LEDIPROVIDER,ONE JR

Specimen: SERUM

Accession \[UID\]: CH 0905 12 \[0000000000\]

Report Released: Sep 05, 2008@11:19

Specimen Collection Date: Sep 05, 2008@11:18

Test name Result units Ref. range Site Code

GLUCOSE 120 mg/dL 60 to 123 \[522\]

Eval: 70-99 mg/dL NORMAL

Eval: 100-125 mg/dL Impaired Fasting Glucose

Eval: \>/= 126 mg/dL Provisional Diagnosis of Diabetes

Eval:

Eval: \*\*5/17/04 Reference Range Changed, OLD RANGE 70-110\*\*

============================================================================

KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:25 PRESS '^' TO STOP

LEDIPATIENT,ONE JR 000-00-1111 AGE: 88 LOC: 1 TEST (NORTH)Sep 18, 2008@

12:25

----MICROBIOLOGY---- page 1

Printed at:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Accession \[UID\]: MICRO 08 11 \[0000000000\]

Collection sample: THROAT SWAB Collection date: Aug 21, 2008 11:58

Provider: LRPROVIDER,ONE JR

--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

\* BACTERIOLOGY PRELIMINARY REPORT =\> Aug 21, 2008 13:21 TECH CODE: 235

GRAM STAIN: TESTING STUFFING PL DURING LRMISTF

Bacteriology Remark(s):

TESTING PL ENTRY

--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

Performing Laboratory:

Gram Stain Performed By:

TRIPLER ARMY MEDICAL CENTER

1 JARRETT WHITE ROAD HONOLULU, HI 96859-5000

Bact Report Remark Performed By:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

\+ + + End of Report + + + End of Report + + + End of Report + + +

LEDIPATIENT,ONE JR 000-00-1111 ROUTING: 1T '^' TO STOP

LEDIPATIENT,ONE 000-00-1111 AGE: 88 LOC: 1 TEST (NORTH)Sep 18, 2008@

12:25

----MICROBIOLOGY---- page 1

Printed at:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue Building 456 VistA City, TX 99999

Reporting Lab:

Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Accession \[UID\]: MICRO 08 10 \[0000000000\]

Collection sample: THROAT SWAB Collection date: Aug 20, 2008 17:25

Provider: LRPROVIDER,ONE JR

Test(s) ordered: GRAM STAIN completed: Aug 20, 2008 17:26

\* BACTERIOLOGY PRELIMINARY REPORT =\> Aug 20, 2008 17:26 TECH CODE: 235

GRAM STAIN: TESTING GRAM STAIN BATCH ENTRY AND PL SAVING

Performing Laboratory:

Gram Stain Performed By:

TRIPLER ARMY MEDICAL CENTER

1 JARRETT WHITE ROAD HONOLULU, HI 96859-5000

\+ + + End of Report + + + End of Report + + + End of Report + + +

LEDIPATIENT,ONE JR 000-00-1111 ROUTING: 1T '^' TO STOP

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:25 PRESS '^' TO STOP

page 2

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:25

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

page 3

LEDIPATIENT,ONE JR 000-00-1111 Sep 18, 2008@12:25

Performing Lab Sites:

\[522\] Dallas Office of Information Field Office \[CLIA# 987654321\]

1234 Anyplace Avenue VistA City, TX 99999

Select Results menu Option:

### File 63 Remediation Results MailMan Message for ‘CH’ 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169017" class="anchor"></span>Figure 76. File 63 ‘CH’ Remediation Results MailMan

Subj: DATA DICTIONARY ^DD(63.04 CHECK REPORT Jun 18, 2012@09:57:14 \[#179854\]

06/18/12@09:57 124 lines

From: LRPROVIDER,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

ZZ BONHAM (MHCVSS.FO-ALBANY.MED.VA.GOV) Jun 18, 2012

Contact the National Service Desk to request assistance from the Clin 4

Product Support team in resolving the following errors identified in the

VistA Laboratory package:

\*WARNING\* THE DATA NAME 'POTASSIUM' (#6) IS LINKED TO MORE THAN ONE LAB TEST:

1\. POTASSIUM (#177)

2\. POTASSIUM,STAT (#1245)

\*WARNING\* THE DATA NAME 'MYELIN BASIC PROTEIN' (#61) IS LINKED TO MORE THAN ONE

LAB TEST:

1\. MYELIN BASIC (#947)

2\. MYELIN BASIC PROTEIN (#1124)

\*WARNING\* THE DATA NAME 'CATECHOLAMINES' (#88) IS LINKED TO MORE THAN ONE LAB TEST:

1\. CATECHOLAMINES (#253)

2\. CATECHOLAMINES, TOTAL (#494)

\*WARNING\* THE DATA NAME 'FRUCTOSE' (#254) IS LINKED TO MORE THAN ONE LAB TEST:

1\. FRUCTOSE (#827)

2\. YEAST (#1096)

\*WARNING\* THE DATA NAME '%METHB' (#448) IS LINKED TO MORE THAN ONE LAB TEST:

1\. METHB% (#50)

2\. METHEMOGLOBIN (#929)

\*WARNING\* THE DATA NAME 'NEUTROPHIL' (#468) IS LINKED TO MORE THAN ONE LAB TEST:

1\. PMN (#285)

2\. NEUTROPHIL % (#359)

\*WARNING\* THE DATA NAME 'UR BLOOD' (#687) IS LINKED TO MORE THAN ONE LAB TEST:

1\. OCCULT BLOOD (#145)

2\. URINE BLOOD (#1158)

\*WARNING\* THE DATA NAME 'PORPHOBILINOGEN' (#709) IS LINKED TO MORE THAN ONE LAB

TEST:

1\. URINE PORPHOBILINOGEN (#164)

2\. PORPHOBILINOGEN (#273)

\*WARNING\* THE DATA NAME 'CYCLIC AMP' (#759) IS LINKED TO MORE THAN ONE LAB TEST:

1\. ANTI MITOCHONDRIAL (#232)

2\. CYCLIC AMP (#338)

Results in Data Name NEUTROPHIL MATURITY, MEAN^NXJ3, without a test in file 60 at:

^LR(4,"CH",6939886.847758,478)

^LR(4,"CH",6948776.855053,478)

^LR(4,"CH",6948776.855341,478)

^LR(4,"CH",6948776.867499,478)

^LR(4,"CH",6948776.874264,478)

^LR(4,"CH",6948776.898199,478)

^LR(4,"CH",6948776.898963,478)

^LR(4,"CH",6948777.828758,478)

^LR(4,"CH",6948777.837167,478)

^LR(4,"CH",6948777.879579,478)

^LR(4,"CH",6948778.826191,478)

^LR(4,"CH",6948783.824546,478)

^LR(4,"CH",6948785.855445,478)

^LR(4,"CH",6948797.82579,478)

^LR(4,"CH",6948797.834446,478)

^LR(4,"CH",6948797.834552,478)

^LR(4,"CH",6948869.867963,478)

^LR(4,"CH",6948883.81608,478)

^LR(4,"CH",6948883.897299,478)

^LR(36,"CH",6939887.845793,478)

^LR(36,"CH",6939889.858144,478)

^LR(36,"CH",6939889.85915,478)

^LR(36,"CH",6939889.868949,478)

^LR(36,"CH",6939893.857267,478)

^LR(36,"CH",6939893.864653,478)

^LR(36,"CH",6939894.836083,478)

^LR(36,"CH",6939896.807283,478)

^LR(36,"CH",6939896.824992,478)

^LR(36,"CH",6939896.826294,478)

^LR(36,"CH",6948776.836472,478)

^LR(36,"CH",6948776.896077,478)

^LR(36,"CH",6948778.826089,478)

^LR(36,"CH",6948783.81525,478)

^LR(36,"CH",6948783.825054,478)

^LR(36,"CH",6948783.859268,478)

^LR(36,"CH",6948785.855585,478)

^LR(36,"CH",6948796.849575,478)

^LR(36,"CH",6948796.84985,478)

^LR(36,"CH",6948797.834646,478)

^LR(36,"CH",6948797.83479,478)

^LR(36,"CH",6948869.867448,478)

^LR(36,"CH",6948869.867875,478)

^LR(36,"CH",6948869.868061,478)

^LR(36,"CH",6948869.86839,478)

^LR(36,"CH",6948883.816168,478)

^LR(36,"CH",6948883.897492,478)

^LR(36,"CH",6948884.875662,478)

^LR(36,"CH",6948970.88607,478)

^LR(36,"CH",6948970.8962,478)

^LR(49,"CH",6939878.905758,478)

^LR(69,"CH",6948779.864789,478)

^LR(69,"CH",6948783.809956,478)

^LR(77,"CH",6948783.814046,478)

^LR(77,"CH",6948967.857279,478)

^LR(77,"CH",6948967.886849,478)

^LR(180,"CH",6939886.845649,478)

^LR(180,"CH",6939886.845786,478)

^LR(180,"CH",6939887.897374,478)

^LR(180,"CH",6939888.825054,478)

^LR(180,"CH",6939888.84596,478)

^LR(180,"CH",6939888.847075,478)

^LR(180,"CH",6939889.878051,478)

^LR(180,"CH",6939894.844685,478)

^LR(180,"CH",6939894.849984,478)

^LR(180,"CH",6939894.86407,478)

^LR(180,"CH",6939894.869481,478)

^LR(180,"CH",6939894.869951,478)

^LR(180,"CH",6939896.824143,478)

^LR(180,"CH",6939896.82845,478)

^LR(180,"CH",6948775.894965,478)

^LR(180,"CH",6948776.838141,478)

^LR(180,"CH",6948783.80986,478)

^LR(180,"CH",6948783.824451,478)

^LR(180,"CH",6948783.894368,478)

^LR(180,"CH",6948785.855486,478)

^LR(180,"CH",6948796.849486,478)

^LR(180,"CH",6948797.8257,478)

^LR(191,"CH",6948776.844296,478)

^LR(191,"CH",6948779.86469,478)

^LR(191,"CH",6948967.856876,478)

^LR(359,"CH",6939879.858091,478)

Enter message action (in IN basket): Ignore//

### File 63 Remediation Results MailMan Message for ‘Micro’ 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510169018" class="anchor"></span>Figure 77. File 63 ‘Micro’ Remediation Results MailMan

Subj: LAB DATA file (#63) Microbiology Antibiotic Fields Cleanup \[#179978\]

07/01/12 85 lines

From: LRPROVIDER,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Contact the National Service Desk to request assistance from the Clin 4

Product Support team in resolving the following errors identified in the

VistA Laboratory package:

The LAB DATA file (#63) cleanup process has completed.

Tool run in ANALYZE MODE for: ZZ BONHAM (MHCVSS.FO-ALBANY.MED.VA.GOV).

This process checked the Organism Sub-field (#63.3) of the LAB DATA file (#63)

to locate potential Data Dictionary discrepancies related to the definition and

setup of fields for reporting antibiotic sensitivities.

The following report lists any discrepancies found:

-------------------------------------------------------------------------------

ANALYZE - INCORRECT INPUT TRANSFORMS (IT)

-------------------------------------------------------------------------------

ANTIBIOTIC NAME CURRENT INPUT PROPOSED INPUT

(FIELD NUMBER) TRANSFORM TRANSFORM

------------------------------- ---------------------------- ---------------

AMPICILLIN B D ^XYZDEF D ^LRMISR

(2.00522799)

-------------------------------------------------------------------------------

TOTAL: 1

ANALYZE - INCORRECT HELP TEXT

-------------------------------------------------------------------------------

ANTIBIOTIC NAME CURRENT PROPOSED

(FIELD NUMBER) HELP HELP

------------------------------- ---------------------------- ---------------

AMPICILLIN B D ZEN^ZLRMISR D EN^LRMISR

(2.00522799)

-------------------------------------------------------------------------------

TOTAL: 1

ANALYZE - INCORRECT SET OF CODES

-------------------------------------------------------------------------------

ANTIBIOTIC NAME CURRENT PROPOSED

(FIELD NUMBER) SET OF CODES SET OF CODES

------------------------------- ------------------ -------------------------

AMPICILLIN X SCREEN M:MAYBE;N:NEVER; A:ALWAYS DISPLAY;N:NEVER

(2.00602) DISPLAY;R:RESTRICT

DISPLAY;

-------------------------------------------------------------------------------

TOTAL: 1

ANALYZE - MISSING INTERP and/or SCREEN

-------------------------------------------------------------------------------

ANTIBIOTIC NAME INTERP FIELD SCREEN FIELD

(FIELD NUMBER) NEEDED NEEDED

------------------------------- ---------------------------- ---------------

AMPICILLIN C 2.005225991 2.005225992

(2.00522599)

-------------------------------------------------------------------------------

TOTAL: 1

ANALYZE - BAD FIELD NUMBER and DEFINITION, LAB DATA NOT UPDATED

-------------------------------------------------------------------------------

ANTIBIOTIC NAME NEW FIELD \# NEW INTERP NEW SCREEN OCCURRENCES

(FIELD NUMBER) FOUND

-------------------------- ----------- ------------ ----------- -----------

CEFPODOXIME TBD TBD TBD 0

(2.0046)

TRIMETH/SULF2 TBD TBD TBD 1

\(199\)

-------------------------------------------------------------------------------

TOTAL: 2

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* END OF REPORT \*\*\*

Enter message action (in IN basket): Ignore//

### Modify AP& MICRO Report for Pathologist’s Signature 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performing Laboratory information should display after the e-signature but not before, so that the Pathologist’s signature is more visible.

<span id="_Toc510169019" class="anchor"></span>Figure 78. Move Pathologist Signature on AP e-Report

ONE, LABUSER,MD

CPT:88305(x2)

/es/ ONE, LABUSER,MD

PATHOLOGIST

Signed Jan 04, 2012@13:36

================================================================================

Performing Laboratory:

Surgical Pathology Report Performed By:

VA BOSTON HEALTHCARE SYSTEM - WEST ROXBURY DIVISION \[CLIA# 22D0989792\]

1400 VFW PARKWAY WEST ROXBURY, MA 02132-4927

<span id="_Toc211242892" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AP</td>
<td>Anatomic Pathology.</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Program Interface.</td>
</tr>
<tr class="odd">
<td>CAP</td>
<td>College of American Pathologists.</td>
</tr>
<tr class="even">
<td>Collecting Facility</td>
<td><p>The Collecting facility is the laboratory that collects the patient's specimen.</p>
<p>To use LEDI after the specimen is collected, the Collecting facility must:</p>
<p>Create an electronic Shipping Manifest, specifying the lab tests to be performed by the Host facility laboratory).</p>
<p>Transmit the Shipping Manifest List to the Host facility laboratory.</p>
<p>Transport the specimen by carrier to the Host facility laboratory.</p></td>
</tr>
<tr class="odd">
<td>Creatinine</td>
<td>Blood and urine tests, used to determine kidney function and for monitoring treatment for kidney disease.</td>
</tr>
<tr class="even">
<td>CY</td>
<td>Cytology</td>
</tr>
<tr class="odd">
<td>Data Fields</td>
<td>The information base associated with a segment.</td>
</tr>
<tr class="even">
<td>Data Type (DT)</td>
<td>Restrictions on the contents of the data field as defined by the HL7 Standard.</td>
</tr>
<tr class="odd">
<td>DoD</td>
<td>Department of Defense.</td>
</tr>
<tr class="even">
<td>eGFR</td>
<td>(eGFR) is Estimated Glomerular Filtration Rate test. A test for kidney function. Specifically, it estimates how much blood passes through the tiny filters in the kidneys, called glomeruli, each minute.</td>
</tr>
<tr class="odd">
<td>Electronic Catalog</td>
<td>The electronic catalog contains laboratory tests available for the Collecting facility to order.</td>
</tr>
<tr class="even">
<td>Element Name</td>
<td>Globally unique descriptive name for the field.</td>
</tr>
<tr class="odd">
<td>EM</td>
<td>Electron Microscopy.</td>
</tr>
<tr class="even">
<td>Feeder Configuration</td>
<td>A shipping configuration that allows the site to indicate certain tests are eligible for a manifest related to the shipping configuration, when the specimen/test is received via the designated feeder shipping configuration used to receive the specimen.</td>
</tr>
<tr class="odd">
<td>HDI</td>
<td>Health Data Informatics.</td>
</tr>
<tr class="even">
<td>HDR</td>
<td>Health Data Repository.</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level Seven. Standard for electronic data exchange/messaging protocol.</td>
</tr>
<tr class="even">
<td>Host facility</td>
<td>The Host facility is the laboratory that receives the patient's specimen and performs the requested testing and analysis on the specimen.</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Internal Entry Number.</td>
</tr>
<tr class="even">
<td>IP</td>
<td>Internet Protocol.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management.</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td>Kernel Installation and Distribution System.</td>
</tr>
<tr class="odd">
<td>LDSI</td>
<td>Laboratory Data Sharing and Interoperability.</td>
</tr>
<tr class="even">
<td>LEDI</td>
<td>Laboratory Electronic Data Interchange.</td>
</tr>
<tr class="odd">
<td>LEN<br />
(length)</td>
<td>Length is the maximum number of characters that one occurrence of the data field may occupy.</td>
</tr>
<tr class="even">
<td>LIM</td>
<td>Laboratory Information Manager.</td>
</tr>
<tr class="odd">
<td>MI</td>
<td>Microbiology.</td>
</tr>
<tr class="even">
<td>NLT</td>
<td>National Laboratory Test.</td>
</tr>
<tr class="odd">
<td>NLTS</td>
<td>VA National Laboratory Test File.</td>
</tr>
<tr class="even">
<td>OIFO</td>
<td>Office of Information Field Office.</td>
</tr>
<tr class="odd">
<td>P&amp;LMS</td>
<td>Pathology and Laboratory Medicine Service.</td>
</tr>
<tr class="even">
<td>PID</td>
<td>Patient Identifier.</td>
</tr>
<tr class="odd">
<td>R/O/C<br />
(optional)</td>
<td><p>R/O/C indicates whether the data field is required, optional, or conditional in a segment:</p>
<p>R—required</p>
<p>O (null) —optional</p>
<p>C—conditional on the trigger event</p></td>
</tr>
<tr class="even">
<td>RP/#<br />
(repetition)</td>
<td><p>Repetition indicates the number of times you can repeat a field:</p>
<p>N (null)—No repetition allowed.</p>
<p>Y—Field may repeat an indefinite or site-determined number of times.</p>
<p>(Integer)—You can repeat the field the number of times specified by the integer.</p></td>
</tr>
<tr class="odd">
<td>Segment</td>
<td>A logical grouping of data fields.</td>
</tr>
<tr class="even">
<td>SEQ<br />
(sequence number)</td>
<td><p>Sequence Number is the ordinal position of a data field within a segment.</p>
<p>This number refers to the data field in the comments text that follows the segment definition table.</p></td>
</tr>
<tr class="odd">
<td>Shipping Configuration</td>
<td><p>Shipping configuration is an entry in the LAB SHIPPING CONFIGURATION file (#62.9) that defines and describes a relationship between two facilities—a Collecting facility and a Host facility.</p>
<p>It is for the collecting, processing, receipting, and reporting of the laboratory testing of clinical specimens.</p>
<p>It controls the building of shipping manifests, which are used as shipping documents for the transport of clinical specimens between the facilities and make up the configuration.</p>
<p>It controls how the specimens are processed at both facilities, as well as, the means and methods used to communicate test orders and results for the two entities.</p></td>
</tr>
<tr class="even">
<td>Shipping Manifest</td>
<td>The shipping manifest is a document that lists the lab specimens sent outside the facility to a reference lab for processing.</td>
</tr>
<tr class="odd">
<td>SNOMED CT</td>
<td>Systemized Nomenclature of Medicine Clinical Terms.</td>
</tr>
<tr class="even">
<td>SP</td>
<td>Surgical Pathology.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Social Security Number.</td>
</tr>
<tr class="even">
<td>TBL#<br />
(table)</td>
<td><p>Table attribute of the data field defined by the HL7 standard (for a set of coded values) or negotiated between the VistA Laboratory application and the vendor system.</p>
<p>Local tables used by the VA begin with the prefix 99VA.</p></td>
</tr>
<tr class="odd">
<td>UI</td>
<td>Universal Interface.</td>
</tr>
<tr class="even">
<td>UID</td>
<td>Unique identifier assigned to each laboratory accession.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Veterans Affairs.</td>
</tr>
<tr class="even">
<td>VAMC</td>
<td>Veterans Affairs Medical Center.</td>
</tr>
<tr class="odd">
<td>VDL</td>
<td>VA Software Document Library.</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration.</td>
</tr>
<tr class="odd">
<td>VIE</td>
<td>Vitria Interface Engine.</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Service Network.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Information System and Technology Architecture.</td>
</tr>
</tbody>
</table>