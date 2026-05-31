---
title: BCMA Version 3 Technical Manual / Security Guide (PSB*3*142)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: null
app_code: PSB
app_name: 'Pharmacy: Bar Code Medication Administration (BCMA)'
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3
group_key: PSB:PSB:3
file_numbers:
- '2'
- '3.2'
- '3.5'
- '7'
- '26'
- '41'
- '42'
- '50.7'
- '53.79'
- '55'
- '62'
- '100'
- '200'
security_keys:
- PSB MGR
- PSB READ ONLY
menu_options: 14
description: '- Revision History - BCMA V. 3.0 and This Guide - BCMA V. 3.0 and This Guide - BCMA V. 3.0 and This Guide - Implementation and Maintenance -...'
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 15302
section_count: 1
table_count: 9
figure_count: 0
appendix_count: 3
has_toc: false
is_stub: false
pub_date: February 2004
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_tm.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_tm.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=84
audit_applied: '2026-05-31'
master_source: BCMA Version 3 Technical Manual / Security Guide (PSB*3*142)
master_pub_date: February 2004
consolidated_from: 2 versions
prior_versions:
- BCMA Version 3 Technical Manual / Security Guide ( PSB*3*131)
consolidated_title: bcma technical manual / security guide
---

![](bcma-version-3-technical-manual-security-guide-psb-3-142/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

TECHNICAL MANUAL/SECURITY GUIDE

February 2004

(Revised August 2023)

Office of Information and Technology

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [BCMA V. 3.0 and This Guide](#bcma-v-30-and-this-guide)
- [BCMA V. 3.0 and This Guide](#bcma-v-30-and-this-guide-1)
- [BCMA V. 3.0 and This Guide](#bcma-v-30-and-this-guide-2)
- [Implementation and Maintenance](#implementation-and-maintenance)
- [Implementation and Maintenance](#implementation-and-maintenance-1)
- [Implementation and Maintenance](#implementation-and-maintenance-2)
- [Exported Options](#exported-options)
- [Exported Options](#exported-options-1)
- [Exported Options](#exported-options-2)
- [Archiving and Purging](#archiving-and-purging)
- [Security Features](#security-features)
- [Security Features](#security-features-1)
- [Security Features](#security-features-2)
- [Internal and External Relations](#internal-and-external-relations)
- [Internal and External Relations](#internal-and-external-relations-1)
- [# Internal and External Relations](#internal-and-external-relations-2)
- [Glossary](#glossary)
- [Glossary](#glossary-1)
- [Glossary](#glossary-2)
- [Appendix A: Processing of Schedule Information](#appendix-a-processing-of-schedule-information)
- [Appendix A: Processing of Schedule Information](#appendix-a-processing-of-schedule-information-1)
- [Appendix A: Processing of Schedule Information](#appendix-a-processing-of-schedule-information-2)
- [Appendix A: Processing of Schedule Information](#appendix-a-processing-of-schedule-information-3)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-1)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-2)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-3)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-4)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-5)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-6)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-7)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-8)
- [Appendix B: HL7 Messaging for BCMA](#appendix-b-hl7-messaging-for-bcma-9)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-1)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-2)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-3)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-4)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-5)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-6)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-7)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-8)
- [Appendix C: Interfacing with the Bar Code Label Printer](#appendix-c-interfacing-with-the-bar-code-label-printer-9)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2023</td>
<td><a href="#p8_patch142"><u>8</u></a></td>
<td>PSB*3*142</td>
<td>The Immunizations Documentation by BCMA Nightly Task [PSB PX BCMA2PCE TASK] option has been placed Out of Order.</td>
</tr>
<tr class="even">
<td>10/2021</td>
<td><a href="#P_C6">C-6</a>,<a href="#P_C7">C-7</a></td>
<td>PSB*3*131</td>
<td>Added an example of a Zebra Printer Sample Terminal Type File with HAZ Control Code.</td>
</tr>
<tr class="odd">
<td>07/2021</td>
<td><a href="#C2_Printer">C-2</a><u>,</u> <a href="#C3_Printer">C-3</a><u>,</u> <a href="#C6">C‑6</a><u>,</u> <a href="#C9_Bar_Code_Label">C-9</a></td>
<td>PSB*3*106</td>
<td>Updated the tables to include the parameters for Hazardous to Handle and Hazardous to Dispose data and added a sample label containing that information.</td>
</tr>
<tr class="even">
<td>01/2019</td>
<td><a href="#Routine_table"><u>7</u></a>, <a href="#MissedMedRespExportedOption1"><u>8</u></a>, <a href="#MissedMedRespExportedOption2"><u>9</u></a></td>
<td>PSB*3*103</td>
<td><p>Added new routine names to the Routines Installed table. Added "Report for Respiratory Therapy Medications" option to the Medication Administration Menu Pharmacy.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td>i, 8, 9</td>
<td>PSB*3*88</td>
<td>Add "BCMA Drug IEN Synonym Check" option to Pharmacy Medication Administration Menu</td>
</tr>
<tr class="even">
<td>12/2016</td>
<td><p>All</p>
<p>6</p>
<p>7</p>
<p>9</p>
<p>19</p></td>
<td>PSB*3*83</td>
<td><p>Renumbered pages to remove sub-pages a, b, etc.</p>
<p>Updated number of routines in list.</p>
<p>Added new Routine "PSBVDLRM".</p>
<p>Spelled out first use of acronym CHUI.</p>
<p>Added new RPC "PSB GETSETWP" to table and included RPC "PSB GETINJECTIONSITE" from previous patch.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>12/2013</td>
<td><p>i-ii, 9, 10, 10a-10b, 14,</p>
<p>18a</p></td>
<td>PSB*3*70</td>
<td><p>Added "Documenting Backlog PRNs" to Manager's Menu. Added note that Missed Medications, Ward Administration Times, and Due List BCMA CHUI reports are Inpatient, only. Added PSB NO WITNESS Security Key. Missing Dose Request option removed from CHUI menus. Added "VHIC 4.0 Card Bar Code Scanning Support" to External Relations section.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>01/2011</td>
<td><p>i-ii, 6, 7, 10, 15,</p>
<p>B-2, B-4</p></td>
<td>PSB*3*42</td>
<td><p>Added note and list of BCMA Reports that were added to GUI only.</p>
<p>Added definition of data field change for Indian Health Service.</p>
<p>Added Indian Health Service terms to Glossary.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/2009</td>
<td>i-ii, 7, 9, 17</td>
<td>PSB*3*47</td>
<td><p>Added PSBPXFL and PSBPXLP to the list of installed routines. Add Immunizations Documentation by BCMA Nightly Task [PSB PX BCMA2PCE TASK] option to the <em>Manager</em> [PSB MGR] menu. Added Patient Care Encounter to the External Relationships section.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>01/2009</td>
<td><p>i-ii, iv, 6-7,</p>
<p>13-14,</p>
<p>18-19, 21</p></td>
<td>PSB*3*28</td>
<td><p>- Update Table of Contents to include Remote Procedure Calls. (p. iv)</p>
<p>- Increased the total for the BCMA V .3.0 routines to 85 and files to 6. (p.6-7)</p>
<p>- Updated the files and "BCMA V.3.0 Routines Installed onto VistA Server" Example. (p.7)</p>
<p>- Updated the Mail Group Types in BCMA V.3.0 to include scanning</p>
<p>failures. (p. 13)</p>
<p>- Updated Security Keys to include PSB UNABLE TO SCAN. (p. 14)</p>
<p>- Added list of Remote Procedure Calls (RPCs). (p. 18)</p>
<p>-Added new Glossary entry for LIMITED ACCESS BCMA. (p. 19)</p>
<p>- Added new Glossary entry for PSB UNABLE TO SCAN. (p. 21)</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>03/2008</td>
<td><p>6-7, 9-10,</p>
<p>C-1, C-2,</p>
<p>C-4, C-5,</p>
<p>C-7, C-9</p></td>
<td>PSB*3*2</td>
<td><p>Description of [PSBO BZ] functionality added, code strings updated (p. C-1.)</p>
<p>- Updated Intermec Printer Team Type Codes Information, Intermec Barcode Label Field Position Map, Intermec printer Sample Terminal Type File code descriptions updated (pp. C-4, C-5, C-7.)</p>
<p>- Barcode samples updated – references to "Dosage" changed to "Dose" and space between colon and dose measurement deleted (p. C-9.)</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>09/2007</td>
<td>6-7</td>
<td>PSB*3*32</td>
<td><p>– Increased the total for the BCMA V. 3.0. routines to 68. (p.6)</p>
<p>– Updated the "BCMA V. 3.0 Routines Installed onto VistA Server" example to include the following routine: PSBO XA. (p. 7)</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>08/2006</td>
<td><p>6-7,</p>
<p>9, 13</p></td>
<td>PSB*3*13</td>
<td><p>– Increased the total for the BCMA V. 3.0. routines to 68. (p.6)</p>
<p>– Updated the "BCMA V. 3.0 Routines Installed onto VistA Server" example to include the following routine: PSBO XA. (p. 7)</p>
<p>– Updated Manager Menu [PSB MGR] options list to include Missing Dose Follow-up (correction) and Unknown Action Status Report (new with this patch). (p. 9)</p>
<p>– Added description of the "Unknown Actions" mail group parameter. (p. 13)</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>08/2006</td>
<td><p>iv,</p>
<p>6,</p>
<p>C1-C10</p></td>
<td>PSB*3*2</td>
<td><p><strong><u>Note</u></strong>: The functionality listed below will be activated with the release of PSB*3*2.</p>
<p>– Updated Table of Contents to include new Appendix C. (p. iv)</p>
<p>– Added reference to new Unit Dose label printing functionality and Appendix C. (p. 6)</p>
<p>– Added Appendix C: Interfacing with the Bar Code Label Printer. (p. C1-C10)</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>12/2005</td>
<td>6-7</td>
<td>PSB*3*16</td>
<td><p>– Increased the total for the BCMA V. 3.0. routines to 67. (p.6)</p>
<p>– Updated the "BCMA V. 3.0 Routines Installed onto VistA Server" example to include the following routines: PSBCSUTL, PSBCSUTX, PSBCSUTY. (p. 7)</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>01/2005</td>
<td><p>6-7,</p>
<p>14,</p>
<p>20-21</p></td>
<td>PSB*3*4</td>
<td><p>– Increased the total for the BCMA V. 3.0. routines to 64. (p.6)</p>
<p>– Updated the "BCMA V. 3.0 Routines Installed on to VistA Server" example to include the PSBOPF routine. (p. 7).</p>
<p>– Added description for new PSB READ ONLY security key. (p.14)</p>
<p>– Added new Glossary entries for PSB READ ONLY and Read-Only BCMA. (p. 20-21)</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/2004</td>
<td>6-7</td>
<td>PSB*3*3</td>
<td><p>– Increased the total for the BCMA V. 3.0 routines to 63. (p. 6)</p>
<p>– Updated the "BCMA V. 3.0 Routines Installed on to VistA Server" example to reflect the inclusion of routines PSBML2, PSBML3, and PSBMLLKU to the VistA Server. (p. 7)</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>02/2004</td>
<td></td>
<td></td>
<td><p>Original Released BCMA V. 3.0 Technical Manual/Security Guide</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>
Table of Contents

# BCMA V. 3.0 and This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="benefits-of-bcma-v.-3.0">![](bcma-version-3-technical-manual-security-guide-psb-3-142/002.png)Benefits of BCMA<br />
V. 3.0</h2></td>
<td><p>The Bar Code Medication Administration (BCMA) V. 3.0 software includes new routines and files, Phase Release changes, and maintenance fixes. This version also includes enhancements, which are a direct result of feedback from the BCMA Workgroup and our many end users.</p>
<p>The patch description for BCMA V. 2.0 includes more detailed information about the maintenance fixes and enhancements for Phase Releases I through IV, which were provided in patches PSB*2*20, *24, *31, and *36.</p>
<p>BCMA software is designed to improve the accuracy of the medication administration process. By automating this process, Department of Veterans Affairs Medical Centers (VAMCs) can expect enhanced patient safety and patient care.</p>
<p>The electronic information that BCMA V. 3.0 provides clinicians improves their ability to administer medications safely and effectively to patients on wards during their medication passes. It also helps to improve the daily communication that occurs between Nursing and Pharmacy staffs.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="benefits-of-this-guide">![](bcma-version-3-technical-manual-security-guide-psb-3-142/003.png)Benefits of This Guide</h2></td>
<td><p>This guide will help you discover the many technical and security aspects of BCMA V. 3.0. It describes implementation and maintenance features; interfaces, variables, and relationships; and security management.</p>
<h3 id="our-target-audience">Our Target Audience</h3>
<p>We have developed this guide for members of the Automated Data Processing (ADP) group and the Information Resources Management (IRM) group who are responsible for maintaining and supporting this package.</p>
<p>We assume that individuals within these groups have the following experience or skills.</p>
<p>Experienced with other Veterans Health Information Systems and Technology Architecture (VistA) software</p>
<p>Have worked with or will work with an Applications Package Coordinator (ADPAC) or Clinical Applications Coordinator (CAC) familiar with the medication administration process in a VAMC</p></td>
</tr>
</tbody>
</table>

# BCMA V. 3.0 and This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 67%" />
<col style="width: 2%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="other-sources-of-information">![](bcma-version-3-technical-manual-security-guide-psb-3-142/004.png)![](bcma-version-3-technical-manual-security-guide-psb-3-142/005.png)Other Sources of Information</h2></td>
<td><p>Refer to the Web sites listed below when you want to receive more background and technical information about BCMA V. 3.0, and to download this manual and related documentation.</p>
<h3 id="backgroundtechnical-information">Background/Technical Information</h3>
<p>From your Intranet, enter REDACTED in the Address field to access the BCMA Main Web page.</p>
<h3 id="this-manual-and-related-documentation">This Manual and Related Documentation</h3>
<p>From your Intranet, enter <a href="http://www.va.gov/vdl">http://www.va.gov/vdl</a> in the Address field to access this manual, and those listed below, from the VA Software Document Library (VDL).</p>
<p>Installation Guide</p>
<p>GUI User Manual</p>
<p>Nursing CHUI User Manual</p>
<p>Pharmacy CHUI User Manual</p>
<p>Manager's User Manual</p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="conventions-used-in-this-guidee">![](bcma-version-3-technical-manual-security-guide-psb-3-142/006.png)Conventions Used in This Guidee</h2></td>
<td colspan="2"><p>![](bcma-version-3-technical-manual-security-guide-psb-3-142/007.png)Before installing BCMA V. 3.0, review this section to learn the many conventions used throughout this guide.</p>
<p><strong>Keyboard Responses:</strong> Keys provided in <strong>boldface</strong>, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see <strong><span class="smallcaps">enter</span></strong> in the copy, press this key on your keyboard.</p>
<p><strong>Mouse Responses:</strong> Buttons provided in <strong>boldface</strong>, within the steps, indicate what you should click on your computer screen using the mouse. For example, when you see <strong><span class="smallcaps">next, yes/no,</span></strong> or <strong><span class="smallcaps">ok</span></strong> in the steps, click the appropriate button on your screen.</p>
<p><strong>Screen Captures:</strong> Provide "shaded" examples of what you will see on your computer screen, and possible user responses.</p>
<p><strong>Notes:</strong> Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our Staff, Developers, and Testers.</p>
<p><strong>Tips:</strong> Located in the left margin, these helpful hints are designed to help you work more efficiently with BCMA V. 3.0.</p>
<p><strong>Menu Options:</strong> Provided in italics. For example, You may establish Electronic Signatures Codes using the Kernel <em>Electronic Signature code Edit</em> [XUSESIG] option.</p></td>
</tr>
</tbody>
</table>

# BCMA V. 3.0 and This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="obtaining-on-line-help">![](bcma-version-3-technical-manual-security-guide-psb-3-142/008.png)Obtaining On-line Help</h2></td>
<td><p>On-line help is designed right into the Graphical User Interface (GUI) and Character-based User Interface (CHUI) versions of BCMA V. 3.0, making it quick and easy for you to get answers to your questions. Here's how to access help in both versions of BCMA V. 3.0:</p>
<p><strong>GUI BCMA:</strong> Provides context-sensitive, on-line help and the Help menu.</p>
<ul>
<li><p><strong>Context-Sensitive Help:</strong> Place your "focus" on a feature, button, or Tab on the BCMA Virtual Due List (VDL) using the <strong><span class="smallcaps">tab</span></strong> key, and then press <strong><span class="smallcaps">f1</span></strong> to receive help specific to that area of the BCMA VDL. In the case of a command, first highlight it in the Menu Bar or Right Click drop-down menu, and then press <strong><span class="smallcaps">f1.</span></strong></p></li>
<li><p><strong>Help Menu:</strong> Open the Help menu, and then choose the Contents and Index command to receive help for every feature in GUI BCMA V. 3.0.</p></li>
</ul>
<p><strong>CHUI BCMA:</strong> Lets you enter up to two question marks at any prompt to receive on-line help.</p>
<ul>
<li><p><strong>One Question Mark:</strong> Provides a brief statement related to the prompt.</p></li>
<li><p><strong>Two Question Marks:</strong> Displays more detailed information about the prompt, plus any hidden actions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="locating-detailed-listings">Locating Detailed Listings</h2></td>
<td><p>You can obtain <em>and</em> print listings about BCMA V. 3.0 routines, and Data Dictionaries using the information provided below.</p>
<h3 id="routines">Routines</h3>
<p>Use the Kernel routine XINDEX to produce detailed listings of routines. Use the Kernel <em>First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of every PSB routine.</p>
<h3 id="data-dictionaries">Data Dictionaries</h3>
<p>You can use the VA FileMan <em>List File Attributes</em> [DILIST] option, under the <em>Data Dictionary Utilities</em> [DI DDU] option, to print the Dictionaries.</p></td>
</tr>
</tbody>
</table>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="minimum-required-packages">Minimum Required Packages</h2></td>
<td>Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).</td>
</tr>
</tbody>
</table>

Example: Minimum Required Packages and Versions

| Package                       | Minimum Version Needed |
|-------------------------------|------------------------|
| Inpatient Medications         | 5.0                    |
| Kernel                        | 8.0                    |
| MailMan                       | 8.0                    |
| Nursing                       | 4.0                    |
| Order Entry/Results Reporting | 3.0                    |
| Pharmacy Data Management      | 1.0                    |
| RPC Broker (32-bit)           | 1.1                    |
| Toolkit                       | 7.3                    |
| VA FileMan                    | 22.0                   |
| Vitals/Measurements           | 5.0                    |

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="installation-time-estimates">Installation Time Estimates</h2>
<p>![](bcma-version-3-technical-manual-security-guide-psb-3-142/009.png)</p></td>
<td><p>On average, it takes approximately two minutes to install BCMA<br />
V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its system resources.</p>
<p>Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.</p></td>
</tr>
</tbody>
</table>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="resource-requirements">![](bcma-version-3-technical-manual-security-guide-psb-3-142/010.png)![](bcma-version-3-technical-manual-security-guide-psb-3-142/011.png)<br />
Resource Requirements</h2></td>
<td><p>This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.</p>
<p>Routines 97</p>
<p>Globals 1 (^PSB)</p>
<p>Files 6 (53.66-53.79)</p>
<p>^PSB Size Unit Dose = 300 x # of Medications<br />
(in bytes) Administered<br />
IV = 2100 x # of IV Bags<br />
Administered</p>
<p>FTEE Support .2</p>
<p>FTEE Maintenance .2</p>
<h3 id="response-time-monitor">Response Time Monitor</h3>
<p>BCMA V. 3.0 does not include Response Time Monitor hooks.</p>
<h3 id="laptops-and-bar-code-scanners">Laptops and Bar Code Scanners</h3>
<p>The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas at your site that use BCMA<br />
V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.</p>
<h3 id="printers">Printers</h3>
<p>Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.</p>
<h3 id="unit-dose-label-printer-devices">Unit Dose Label Printer Devices</h3>
<p>BCMA V. 3.0 includes the <em>Label Print</em> [PSBO BL] option for printing individual or batch Unit Dose bar code labels. This option allows sites the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBL uses site-specific printers or terminals to produce labels. See Appendix C: "Interfacing with the Bar Code Label Printer" for detailed setup information.</p>
<h3 id="iv-label-printer-devices">IV Label Printer Devices</h3>
<p>Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section "Interfacing with the Bar Code Label Printer" in the <em>Inpatient Medications V. 5.0 Technical Manual/Security Guide</em> for detailed setup information.</p></td>
</tr>
</tbody>
</table>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="files-required-to-run-bcma-v.-3.0">![](bcma-version-3-technical-manual-security-guide-psb-3-142/012.png)Files Required to Run BCMA V. 3.0</h2></td>
<td><p>BCMA V. 3.0 uses the following files installed on the VistA Server. "Journaling" is recommended.</p>
<p>^PSB (53.66, BCMA IV Parameters</p>
<p>^PSB (53.68, BCMA Missing Dose Request</p>
<p>^PSB (53.69, BCMA Report Request</p>
<p>^PSB (53.77, BCMA Unable to Scan Log</p>
<p>^PSB (53.78, BCMA Medication Variance Log</p>
<p>^PSB (53.79, BCMA Medication Log</p>
<p>Note: You can learn more about these files by generating a list with file attributes using VA FileMan.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="routines-installed">Routines Installed</h2></td>
<td><p>Review the listing below to learn the routines installed on your site's VistA Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.</p>
<p><strong>Note:</strong> You can use the <em>Kernel First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of each PSB routine.</p>
<h3 id="routine-mapping">Routine Mapping</h3>
<p>At this time, we do <em>not</em> offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory.</p></td>
</tr>
</tbody>
</table>

Example: BCMA V. 3.0 Routines Installed onto VistA Server

| <span id="Routine_table" class="anchor"></span>PSB3P103 | PSBALL   | PSBAPIPM | PSBCHIVH | PSBCHKIV | PSBCSUTL | PSBCSUTX | PSBCSUTY |
|---------------------------------------------------------|----------|----------|----------|----------|----------|----------|----------|
| PSBINJEC                                                | PSBMD    | PSBML    | PSBML1   | PSBML2   | PSBML3   | PSBMLEN  | PSBMLEN1 |
| PSBMLHS                                                 | PSBMLLKU | PSBMLTS  | PSBMLU   | PSBMLVAL | PSBMMRB  | PSBO     | PSBO1    |
| PSBOAL                                                  | PSBOBL   | PSBOBLU  | PSBOBZ   | PSBOCE   | PSBOCE1  | PSBOCI   | PSBOCI1  |
| PSBOCM                                                  | PSBOCM1  | PSBOCP   | PSBOCP1  | PSBODL   | PSBODL1  | PSBODO   | PSBOHDR  |
| PSBOHDR1                                                | PSBOIV   | PSBOIV1  | PSBOMD   | PSBOMH   | PSBOMH1  | PSBOMH2  | PSBOMH3  |
| PSBOML                                                  | PSBOMM   | PSBOMM2  | PSBOMT   | PSBOMT1  | PSBOMV   | PSBOPE   | PSBOPF   |
| PSBOPI                                                  | PSBOPM   | PSBOPM1  | PSBORT   | PSBOSF   | PSBOST   | PSBOVT   | PSBOWA   |
| PSBOXA                                                  | PSBPAR   | PSBPARIV | PSBPOIV  | PSBPRN   | PSBPRND  | PSBPXFL  | PSBPXLP  |
| PSBRPC                                                  | PSBRPC1  | PSBRPC2  | PSBRPC3  | PSBRPCMO | PSBRPCXM | PSBSAGG  | PSBSVHL7 |
| PSBUTL                                                  | PSBVAR   | PSBVDLIV | PSBVDLPA | PSBVDLPB | PSBVDLRM | PSBVDLTB | PSBVDLU1 |
| PSBVDLU2                                                | PSBVDLU3 | PSBVDLUD | PSBVDLVL | PSBVITFL | PSBVPR   | PSBVT    | PSBVT1   |
| PSBXMRG                                                 |          |          |          |          |          |          |          |

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="bcma-chui-menus"><br />
BCMA CHUI Menus</h2></td>
<td><p>BCMA V. 3.0 exports three main menus. They include those listed below, in the Character-based User Interface (CHUI) version of BCMA V. 3.0. The options for each menu are listed in this section.</p>
<p><strong>Manager Menu:</strong> [PSB MGR] is assigned to managers</p>
<p><strong>Pharmacist Menu:</strong> [PSB PHARMACY] is assigned to all inpatient Pharmacists</p>
<p><strong>Nurse Menu:</strong> [PSB NURSE] is assigned to all clinicans and other personnel who administer active medication orders</p>
<h3 id="manager-menu-psb-mgr">Manager Menu [PSB MGR]</h3>
<p>This menu includes the following options:</p>
<p>Documenting Backlog PRNs</p>
<p>Drug File Inquiry</p>
<p>Immunizations Documentation by BCMA Nightly Task</p>
<p>&gt; <span id="p8_patch142" class="anchor"></span>Out of order: Obsolete; Use CPRS Immunization Documentation</p>
<p>Medication Administration Menu Nursing</p>
<ul>
<li><p>Medication Administration Log Report</p></li>
<li><p>Missed Medications Report (INPATIENT ONLY)</p></li>
<li><p>Ward Administration Times Report (INPATIENT ONLY)</p></li>
<li><p>Due List Report (INPATIENT ONLY)</p></li>
<li><p>PRN Effectiveness List Report</p></li>
<li><p>Enter PRN Effectiveness</p></li>
<li><p>Manual Medication Entry</p></li>
<li><p>Medication Administration History (MAH) Report</p></li>
<li><p>Medication Variance Log</p></li>
<li><p>Drug File Inquiry</p></li>
</ul>
<p>Medication Administration Menu Pharmacy</p>
<ul>
<li><p>Medication Administration Log Report</p></li>
<li><p>Missed Medications Report (INPATIENT ONLY)</p></li>
<li><p>Due List Report (INPATIENT ONLY)</p></li>
<li><p>Medication Administration History (MAH) Report</p></li>
<li><p>Missing Dose Followup</p></li>
<li><p>Missing Dose Report</p></li>
<li><p>Label Print</p></li>
<li><p>Drug File Inquiry</p></li>
<li><p>Barcode Label Print</p></li>
<li><p>BCMA Drug IEN Synonym Check</p></li>
<li><p><span id="MissedMedRespExportedOption1" class="anchor"></span>Report for Respiratory Therapy Medications</p></li>
</ul>
<p>Missing Dose Followup</p>
<p>Reset User Parameters</p>
<p>Trouble Shoot Med Log</p>
<p>Unknown Action Status Report</p></td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="bcma-chui-menus-cont." class="H2-Continued">BCMA CHUI Menus (cont.)</h2></td>
<td><h3 id="medication-administration-menu-pharmacy-psb-pharmacy">Medication Administration Menu Pharmacy<br />
[PSB PHARMACY]</h3>
<p>This menu includes the following options:</p>
<p>Medication Administration Log Report</p>
<p>Missed Medications Report (INPATIENT ONLY)</p>
<p>Due List Report (INPATIENT ONLY)</p>
<p>Medication Administration History (MAH) Report</p>
<p>Missing Dose Followup</p>
<p>Missing Dose Report</p>
<p>Label Print</p>
<p>Drug File Inquiry</p>
<p>Barcode Label Print</p>
<p>BCMA Drug IEN Synonym Check<span id="MissedMedRespExportedOption2" class="anchor"></span></p>
<p>Report for Respiratory Therapy Medications</p>
<h3 id="nursing-medication-administration-menu-psb-nurse">Nursing Medication Administration Menu<br />
[PSB NURSE]</h3>
<p>This menu includes the following options:</p>
<p>Medication Administration Log Report</p>
<p>Missed Medications Report (INPATIENT ONLY)</p>
<p>Ward Administration Times Report (INPATIENT ONLY)</p>
<p>Due List Report (INPATIENT ONLY)</p>
<p>PRN Effectiveness List Report</p>
<p>Enter PRN Effectiveness</p>
<p>Manual Medication Entry</p>
<p>Medication Administration History (MAH) Report</p>
<p>Medication Variance Log</p>
<p>Drug File Inquiry</p>
<p><strong>Note:</strong> The Missed Medications, Ward Administration Times, and Due List BCMA CHUI reports will only include Inpatient orders in the report.  The menus containing these options will be updated to include "(INPATIENT ONLY)" in the report label/description.  To run these reports for Clinic orders and updated report selection options, the reports must be generated in the BCMA GUI.</p>
<p><strong>Note:</strong> The following reports have been added to BCMA and are available via GUI only, but have not been added to the CHUI menus.</p>
<p>Cover Sheet Reports</p>
<p>Medication Overview</p>
<p>PRN Overview</p>
<p>IV Overview</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="bcma-chui-menus-cont.-1" class="H2-Continued">BCMA CHUI Menus (cont.)</h2></td>
<td><p>Expired/DC'd/Expiring Orders</p>
<p>IV Bag Status Report</p>
<p>Medication Therapy Report</p>
<p>Unable to Scan Detailed Report</p>
<p>Unable to Scan Summary Report</p></td>
</tr>
</tbody>
</table>

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="archive-and-purge-capabilities">![](bcma-version-3-technical-manual-security-guide-psb-3-142/013.png)![](bcma-version-3-technical-manual-security-guide-psb-3-142/014.png)Archive and Purge Capabilities</h2></td>
<td><p>BCMA V. 3.0 stores detailed information about each inpatient at your VAMC, including medications administered to them and the PRN Effectiveness (when applicable).</p>
<p><strong>Average Unit Dose Administration</strong>: Requires about 300 bytes of disk space</p>
<p><strong>Average IV Administration:</strong> Requires about 2100 bytes<br />
of disk space</p>
<p><strong>Note:</strong> Although archive and purge capabilities are <em>not</em> currently available in BCMA V. 3.0, when they are, they will be consistent with the Computerized Patient Record System (CPRS) package. BCMA<br />
V. 3.0 will offer this feature once it is made available in CPRS.</p></td>
</tr>
</tbody>
</table>

# Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-mail-groups-in-bcma">Defining Mail Groups in BCMA</h2></td>
<td><p>In BCMA V. 3.0, you can define two "Mail Groups" for notifying Pharmacy, IRM, and other internal staff about errors and Missing Dose Requests. This section describes how you can create mail groups, and the purpose of each group.</p>
<h3 id="creating-mail-groups-for-bcma-v.-3.0">Creating Mail Groups for BCMA V. 3.0</h3>
<p>Creating mail groups for BCMA V. 3.0 involves using the VistA Mail Group <em>Enter/Edit</em> [XMUSER] option to set the TYPE field to PUBLIC. Once this task is accomplished, you can then use the Parameters Tab of the GUI BCMA Site Parameters application to define the mail groups that you created.</p>
<h3 id="mail-group-types-in-bcma-v.-3.0">Mail Group Types in BCMA V. 3.0</h3>
<p>This section describes the mail groups that you can define using the Parameters Tab of the GUI BCMA Site Parameters application.</p>
<p><strong>Due List Error:</strong> Generates an E-mail message for any medication order that BCMA V. 3.0 cannot resolve for the BCMA VDL placement, and sends it to the mail group members. An example might include no administration times entered for a Continuous order.</p>
<p><strong>Missing Dose Notification:</strong> Generates an E-mail message for any Missing Dose Request entered using the BCMA<br />
V. 3.0 GUI menu option. The E-mail is sent to all members of the mail group, specifically Pharmacy, as a "fail safe" even if the designated Missing Dose printer is not functioning.</p>
<p><strong>Unknown Actions:</strong> This field generates an E-mail message for any administration with an "Unknown" status while processing administrations to display on the BCMA VDL.</p>
<p><strong>Unable to Scan:</strong> Generates an E-mail message to alert the mail group when a user creates a scanning failure entry, and to assist in researching the reasons for a scanning failure.</p></td>
</tr>
</tbody>
</table>

# Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="assigning-menus-to-users">Assigning Menus<br />
to Users</h2></td>
<td><p>Use this section to assign menus to BCMA V. 3.0 CHUI and GUI users, if they have not already been assigned.</p>
<h3 id="chui-version">CHUI Version</h3>
<p>Refer to this section for BCMA V. 3.0 CHUI menu assignments.</p>
<p><strong>PSB MGR:</strong> assign to a manager</p>
<p><strong>PSB PHARMACY:</strong> assign to all Inpatient Pharmacists</p>
<p><strong>PSB NURSE:</strong> assign to all clinicians and other personnel who administer active medication orders</p>
<h3 id="gui-version">GUI Version</h3>
<p>Refer to this section for BCMA V. 3.0 GUI menu assignments.</p>
<p><strong>PSB GUI CONTEXT – USER:</strong> assign to all clinicians and other personnel who administer active medication orders</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="allocating-security-keys-to-users">Allocating Security Keys to Users</h2></td>
<td><p>Refer to this section to allocate the following security keys to appropriate site personnel.</p>
<p><strong>PSB MANAGER:</strong> designates the holder as a manager</p>
<p><strong>PSB INSTRUCTOR:</strong> designates the holder as a nursing instructor supervising student nurses</p>
<p><strong>PSB STUDENT:</strong> designates the holder as a student nurse, requiring that an instructor also sign on to BCMA V. 3.0 at the same time</p>
<p><strong>PSB CPRS MED BUTTON:</strong> designates the holder as a nurse who can document administered verbal- and phone-type STAT and NOW (One-Time) orders using the CPRS Med Order Button on the BCMA VDL</p>
<p><strong>PSB READ ONLY:</strong> designates the holder as a user that only has Read-Only access to BCMA. Note that users with Read-Only access will also be required to have the PSB GUI CONTEXT – USER secondary menu option.</p>
<p><strong>PSB UNABLE TO SCAN:</strong> designates the holder as a user that can run the Unable to Scan (Detailed and Summary) reports.</p>
<p><strong>PSB NO WITNESS:</strong> designates the holder as a BCMA user not authorized to witness high risk/high alert administrations, such as Unlicensed Assistive Personnel and Respiratory Therapists.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="establishing-electronic-signature-codes">Establishing Electronic Signature Codes</h2></td>
<td><p>You may establish Electronic Signatures Codes using the Kernel <em>Electronic Signature code Edit</em> [XUSESIG] option.</p>
<p><strong>Note:</strong> For easier access by all users, this option is tied to the Common Options, under the <em>User's Toolbox</em> [XUSERTOOLS] submenu.</p></td>
</tr>
</tbody>
</table>

# Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="developing-a-contingency-plan">Developing a Contingency Plan</h2></td>
<td>In March 2006, patch PSB*3*8, the BCMA Backup System (BCBU), was reissued with significant enhancements to the field as a Class I solution for the BCMA Contingency Plan. This patch provides real-time backup of all inpatient medication activities on a designated workstation. Review the patch description to learn more about the benefits of this patch.</td>
</tr>
</tbody>
</table>

# Internal and External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="internal-relations"><br />
Internal Relations</h2></td>
<td><p>This section describes options, package-wide variables, and templates within BCMA V. 3.0.</p>
<h3 id="options">Options</h3>
<p>You can invoke ALL options in BCMA V. 3.0 independently.</p>
<h3 id="package-wide-variables">Package-Wide Variables</h3>
<p>BCMA V. 3.0 does <em>not</em> include package-wide variables.</p>
<h3 id="templates">Templates</h3>
<p>BCMA V. 3.0 does <em>not</em> include any templates for Sort, Input, or Print.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="external-relations">![](bcma-version-3-technical-manual-security-guide-psb-3-142/015.png)External Relations</h2></td>
<td><p>BCMA V. 3.0 can only be run in an environment that already has several existing features, such as a standard MUMPS operating system.</p>
<p>It also requires the following Department of Veterans Affairs (VA) software packages (versions listed or higher) — and all current patches. Otherwise, BCMA V. 3.0 will <em>not</em> be fully functional for your users.</p>
<p>Inpatient Medications 5.0</p>
<p>Kernel 8.0</p>
<p>MailMan 8.0</p>
<p>Nursing 4.0</p>
<p>Order Entry/Results 3.0<br />
Reporting</p>
<p>Patient Care Encounter 1.0</p>
<p>Pharmacy Data 1.0<br />
Management</p>
<p>RPC Broker (32-bit) 1.1</p>
<p>Toolkit 7.3</p>
<p>VA FileMan 22.0</p>
<p>Vitals/Measurements 5.0</p></td>
</tr>
<tr class="even">
<td><h2 id="section"></h2></td>
<td></td>
</tr>
</tbody>
</table>

# Internal and External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="external-relations-1" class="H2-Continued">External Relations </h2>
<h2 id="cont." class="H2-Continued">(cont.)</h2></td>
<td><h3 id="callable-routines-entry-points-and-variables">Callable Routines, Entry Points, and Variables</h3>
<p>BCMA V. 3.0 includes two callable routines: PSBAPIPM and PSBMLHS. Each routine is described in this section, along with the entry points and variables information for each.</p>
<p><strong>PSBAPIPM:</strong> Provides information to Inpatient Medications<br />
V. 5.0 for determining the start date for a renewed order.</p>
<p><strong>PSBMLHS:</strong> Provides other software packages with the ability to call the BCMA Medication History Report. The report lists medications, that a patient has received, by orderable item.</p>
<h3 id="database-integration-agreements-dbias">Database Integration Agreements (DBIAs)</h3>
<p>BCMA subscribes to Database Integration Agreements (DBIAs) with the Inpatient Medications, CPRS, Nursing, and Registration packages. BCMA V. 3.0 also offers DBIAs for other packages to subscribe to as well.</p>
<p>For detailed information about these DBIAs, log in to FORUM and select the <em>Integration Agreements Menu</em> [DBA IA ISC] option located under the <em>DBA</em> [DBA] option (Data Base Administrator). Once in the Integration Agreements Menu Option, select "Inquire" and type <strong>BCMA</strong> at the "Select INTEGRATION REFERENCES:" prompt.</p>
<h3 id="remote-procedure-calls-rpcs">Remote Procedure Calls (RPCs)</h3>
<p>Following is a list of Remote Procedure Calls associated with BCMA.</p>
<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th>1   PSB ALLERGY</th>
<th>2   PSB BAG DETAIL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3   PSB CHECK IV</td>
<td>4   PSB CHECK SERVER</td>
</tr>
<tr class="even">
<td>5   PSB COVERSHEET1</td>
<td>6   PSB CPRS ORDER</td>
</tr>
<tr class="odd">
<td>7   PSB DEVICE</td>
<td>8   PSB FMDATE</td>
</tr>
<tr class="even">
<td>9 PSB GETINJECTIONSITE</td>
<td>10   PSB GETIVPAR</td>
</tr>
<tr class="odd">
<td>11  PSB GETORDERTAB</td>
<td>12  PSB GETPRNS</td>
</tr>
<tr class="even">
<td>13  PSB GETPROVIDER</td>
<td>14 PSB GETSETWP</td>
</tr>
<tr class="odd">
<td>15  PSB INSTRUCTOR</td>
<td>16  PSB IV ORDER HISTORY</td>
</tr>
<tr class="even">
<td>17  PSB LOCK</td>
<td>18  PSB MAIL</td>
</tr>
<tr class="odd">
<td>19  PSB MAN SCAN FAILURE</td>
<td>20  PSB MAXDAYS</td>
</tr>
<tr class="even">
<td>21  PSB MED LOG LOOKUP</td>
<td>22  PSB MEDICATION HISTORY</td>
</tr>
<tr class="odd">
<td>23  PSB MOB DRUG LIST</td>
<td>24  PSB NURS WARDLIST</td>
</tr>
<tr class="even">
<td>25  PSB PARAMETER</td>
<td>26  PSB PUTIVPAR</td>
</tr>
<tr class="odd">
<td>27  PSB REPORT</td>
<td>28  PSB SCANMED</td>
</tr>
<tr class="even">
<td>29  PSB SCANPT</td>
<td>30  PSB SERVER CLOCK VARIANCE</td>
</tr>
<tr class="odd">
<td>31  PSB SUBMIT MISSING DOSE</td>
<td>32  PSB TRANSACTION</td>
</tr>
<tr class="even">
<td>33  PSB USERLOAD</td>
<td>34  PSB USERSAVE</td>
</tr>
<tr class="odd">
<td>35  PSB UTL XSTATUS SRCH</td>
<td>36  PSB VALIDATE ESIG</td>
</tr>
<tr class="even">
<td>37  PSB VALIDATE ORDER</td>
<td>38  PSB VERSION CHECK</td>
</tr>
<tr class="odd">
<td>39  PSB VITAL MEAS FILE</td>
<td>40  PSB VITALS</td>
</tr>
<tr class="even">
<td>41 PSB WARDLIST</td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

# # Internal and External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="external-relations-cont." class="H2-Continued">External Relations (cont.)</h2></td>
<td><h3 id="vhic-4.0-card-bar-code-scanning-support">VHIC 4.0 Card Bar Code Scanning Support</h3>
<p>To incorporate lookup of patients by scanning the bar code on the new VIC 4.0 card or a DoD CAC card, a new supported API (RPCVIC^DPTLK) from dependent patch DG*5.3*857 has been incorporated into PSB SCANPT, which returns a patient DFN for lookup in BCMA.</p></td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-v.-3.0-lingo">Learning BCMA<br />
V. 3.0 Lingo</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
| Acronym/Term            | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Archive                 | To transfer files from a computer onto long-term storage.                                                                                                                                                                                                                                                                                                                                                                                                         |
| BCMA Clinical Reminders | A marquee located in the lower, right-hand corner of the BCMA VDL that identifies PRN medication orders needing effectiveness documentation. The setting is based on the "PRN Documentation" site parameter, and applies to current admissions or the site parameter timeframe (whichever is greater). A mouse-over list displays when the pointer is placed over the PRN Effectiveness Activity, or a full list is available by double clicking on the Activity. |
| CHUI                    | Character-based User Interface.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Client                  | An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.                                                                                                                                                                                                                                                                                                           |
| CPRS                    | Computerized Patient Record System. A VistA software application that allows users to enter patient orders into different packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.                                                                   |
| Data Dictionary         | Also called "DD," the dictionary that contains file attributes.                                                                                                                                                                                                                                                                                                                                                                                                   |
| DBIA                    | Database Integration Agreement. A formal understanding between two or more application packages which describes how data is shared or how packages interact. This Agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.                                                                                                                                       |
| FileMan                 | The VistA database management system.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| GUI                     | Graphical User Interface. The type of interface chosen for BCMA V. 3.0.                                                                                                                                                                                                                                                                                                                                                                               |
| IV                      | A medication given intravenously (within a vein) to a patient from an IV bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.                                                                                                                                                                                                                                                                                                          |
| Journaling              | A record of changes made in files and messages transmitted. It is quite useful when recovering previous versions of a file before updates were made, or to reconstruct updates if an updated file gets damaged.                                                                                                                                                                                                                                                   |
| LIMITED ACCESS BCMA     | A mode in which BCMA can be accessed that provides medication administering users the ability to access patient records for non-medication administration documentation, review and reporting purposes without being at the patient's bedside.                                                                                                                                                                                                                    |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-v.-3.0-lingo-cont." class="H2-Continued">Learning BCMA<br />
V. 3.0 Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
| Acronym/Term                  | Definition                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAH                           | Medication Administration History. A patient report that lists a clinician's name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The date column lists three asterisks (\*\*\*) if a medication was Discontinued.                            |
| MAR                           | Medication Administration Record. The traditional, handwritten record used for noting when a patient received a medication. BCMA V. 3.0 replaces this record with an MAH.                                                                                                                                                                                      |
| NOW Order                     | A medication order given ASAP to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the BCMA VDL, as defined by the order Start and Stop Date/Time.                                                                                                                                               |
| Patient Transfer Notification | A message that displays when a patient's record is opened or the Unit Dose or IVP/IVPB Medication Tab is viewed for the first time. This message indicates that the patient has had a movement type (usually a transfer) within the site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe. |
| PRN Order                     | The Latin abbreviation for Pro Re Nata. A medication dosage given to a patient on an "as needed" basis.                                                                                                                                                                                                                                                        |
| PSB CPRS MED BUTTON           | The name of the security "key" that must be assigned to nurses who document verbal- and phone-type STAT and NOW (One-Time) medication orders using the CPRS Med Order Button on the BCMA VDL.                                                                                                                                                                              |
| PSB INSTRUCTOR                | The name of the security "key" that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.                                                                                                                                                                                                             |
| PSB MANAGER                   | The name of the security "key" that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.                                                                                                                                                                                                                                            |
| PSB READ ONLY                 | The name of the security "key" that must be assigned to users that can only access BCMA in Read-Only mode. Users who are assigned the PSB READ ONLY security key will never be able to administer medications or perform any actions against a patient's medical record. The PSB READ ONLY security key overrides all other BCMA security keys.                            |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-v.-3.0-lingo-cont.-1" class="H2-Continued">Learning BCMA<br />
V. 3.0 Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym/Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSB STUDENT</td>
<td>The name of the security "key" that must be assigned to nursing students, supervised by nursing instructors, so they can access user options within BCMA V. 3.0. This key also requires that a nursing instructor sign on to BCMA.</td>
</tr>
<tr class="even">
<td>PSB UNABLE TO SCAN</td>
<td>The name of the security "key" that must be assigned to allow the user to run the Unable to Scan (Detailed and Summary) reports.</td>
</tr>
<tr class="odd">
<td>Purge</td>
<td>To delete a set of data, and all references to the data.</td>
</tr>
<tr class="even">
<td>Read-Only BCMA</td>
<td>A mode in which BCMA can be accessed that provides non-medication administering users the ability to view a patient's BCMA VDL and print reports, without performing any actions against a patient's medical record.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td><strong>R</strong>emote <strong>P</strong>rocedure <strong>C</strong>all. A procedure stored on the VistA Server, which is executed to return data to the Client.</td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td>A Client/Server System within the VA's Veterans Health Information Systems and Technology Architecture (VistA) environment. It enables client applications to communicate and exchange data with M Servers.</td>
</tr>
<tr class="odd">
<td>Security Keys</td>
<td>Used to access specific options within BCMA V. 3.0 that are otherwise "locked" without the security key. Only users designated as "Holders" may access these options.</td>
</tr>
<tr class="even">
<td>Server</td>
<td>An architecture in which one computer can get information from another. The Server, which can be anything from a personal computer to a mainframe, supplies the requested data or services to the Client.</td>
</tr>
<tr class="odd">
<td>STAT Order</td>
<td>A medication order given immediately to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the BCMA VDL, as defined by the order Start and Stop Date/Time.</td>
</tr>
<tr class="even">
<td>VDL</td>
<td><p><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line "list" used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</p>
<p><strong>Note:</strong> This is called BCMA VDL in this guide to eliminate confusion with the VA Software Document Library (VDL) also mentioned in this guide.</p></td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</td>
</tr>
<tr class="even">
<td>Ward Stock</td>
<td>Unit Dose and IV medications that are "stocked" on an ongoing basis on wards and patient care areas. They are packaged in a ready-to-use form or compounded by the medication administrator.</td>
</tr>
<tr class="odd">
<td>ZPL</td>
<td><strong>Z</strong>ebra <strong>P</strong>rogramming <strong>L</strong>anguage.</td>
</tr>
</tbody>
</table>

# Appendix A: Processing of Schedule Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="how-bcma-processes-schedule-information">How BCMA Processes Schedule Information</h2></td>
<td><p>This section describes how BCMA V. 3.0 processes Schedule information from Inpatient Medications V. 5.0, and how it determines when to display a Continuous medication order on the BCMA VDL. Keep in mind that BCMA displays medication orders on the BCMA VDL between the order Start and Stop Date and Time.</p>
<p>The information provided below defines term used in this section:</p>
<p><strong>Admin Time:</strong> The ADMIN TIMES field (#41) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the ADMINISTRATION TIMES field (#.12) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).</p>
<p><strong>Frequency:</strong> The FREQUENCY field (#42) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the SCHEDULE INTERVAL field (#.17) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).</p>
<p><strong>Schedule:</strong> The SCHEDULE field (#26) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55), and the SCHEDULE field (#.09) of the IV multiple (#100) of the PHARMACY PATIENT file (#55).</p>
<p><strong>Schedule Type:</strong> The SCHEDULE TYPE field (#7) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55). For IV orders, it refers to the pseudo-type determined by Inpatient Medications that is sent to BCMA.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="steps-for-processing-schedule-information">Steps for Processing Schedule Information</h2></td>
<td><p>This section describes the steps for processing schedule information from Inpatient Medications to BCMA.</p>
<ol type="1">
<li><p>BCMA checks the Inpatient Medications order for a Schedule Type of "Continuous."</p></li>
</ol>
<p>If a Schedule Type other than "Continuous" is listed, BCMA quits processing the order, and proceeds to the correct processing method for that order's Schedule Type.</p></td>
</tr>
</tbody>
</table>

# Appendix A: Processing of Schedule Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="steps-for-processing-schedule-information-cont." class="H2-Continued">Steps for Processing Schedule Information (cont.)</h2></td>
<td><ol start="2" type="1">
<li><p>BCMA verifies information provided in the Schedule of the Inpatient Medications order.</p></li>
</ol>
<p>If the Schedule is blank, BCMA quits processing the order and sends a Due List Error Notification message. (<strong>Note:</strong> A blank indicates that no Schedule was specified.)</p>
<p>If the Schedule lists a Day of the Week (i.e., <a href="mailto:MO-WE@1200">MO-WE@1200</a>), BCMA checks the Admin Time(s) for the correct two- or four-digit format (i.e., 12-14, 1200, 1400).</p>
<ul>
<li><p>If an Admin Time is listed, BCMA displays the order on the BCMA VDL, on specified days, using the Admin Time.</p></li>
<li><p>If no Admin Time is listed, BCMA quits processing the order and sends a Due List Error Notification message.</p></li>
</ul>
<p>If the Schedule lists an Admin Time (i.e., 12-14, 1200, 1400), BCMA checks the Admin Time in the Inpatient Medications order.</p>
<ul>
<li><p>If the Admin Time is blank, BCMA quits processing the order and sends a Due List Error Notification message.</p></li>
<li><p>If an Admin Time is listed, BCMA verifies for the correct two- or four-digit format (i.e., 12-14, 1200, 1400). If <strong>valid</strong>, BCMA displays the order on the BCMA VDL every day using the Admin Time provided. If <strong>invalid</strong>, BCMA quits processing the order and sends a Due List Error Notification message.</p></li>
</ul>
<ol start="3" type="1">
<li><p>BCMA verifies information provided in the Frequency of the Inpatient Medications order. <strong>(Note:</strong> The Frequency is the amount of time between medication administrations.)</p></li>
</ol>
<p>If the Frequency is blank, contains a letter other than "O" (the letter), or lists a Frequency less than one minute, BCMA quits processing the order and sends a Due List Error Notification message. (<strong>Note:</strong> A blank indicates that no Frequency was specified.)</p>
<p>If the Frequency lists "O" (the letter), BCMA converts the Frequency to 1440 minutes (one day) and proceeds to Step #4.</p></td>
</tr>
</tbody>
</table>

# Appendix A: Processing of Schedule Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="steps-for-processing-schedule-information-cont.-1" class="H2-Continued">Steps for Processing Schedule Information (cont.)</h2></td>
<td><ol start="4" type="1">
<li><p>BCMA verifies whether the order contains an Odd Schedule by determining that data in the order Frequency is not divisible by 1440 minutes (one day), and that 1440 minutes is not divisible by the data in the order Frequency. See the examples provided below.</p></li>
</ol>
<p>If the order contains an Odd Schedule and times in the Admin Time, BCMA quits processing the order and sends a Due List Error Notification message.</p>
<p>If the order contains an Odd Schedule, but no times in the Admin Time, BCMA displays the medication order on the BCMA VDL using the Frequency and order Start Date/Time provided by Inpatient Medications to calculate the Admin Times.</p>
<p>If the order does <em>not</em> contain an Odd Schedule and no times are listed in the Admin Time, BCMA displays the medication order on the BCMA VDL using the Frequency and order Start Date/Time provided by Inpatient Medications to calculate the Admin Times.</p>
<p>If the order does <em>not</em> contain an Odd Schedule, but times are listed in the Admin Time, BCMA verifies the Frequency listed in the order.</p>
<ul>
<li><p>If the Frequency is <em>less than</em> 1440 minutes (or one day), BCMA displays the medication order on the BCMA VDL every day, based on the Admin Times provided in the order.</p></li>
<li><p>If the Frequency is <em>greater than</em> 1440 minutes (or one day), BCMA uses the Frequency information from Inpatient Medications to determine which day to display the medication order on the BCMA VDL, based on the Admin Time provided in the order.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Appendix A: Processing of Schedule Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="steps-for-processing-schedule-information-cont.-2" class="H2-Continued">Steps for Processing Schedule Information (cont.)</h2></td>
<td><p>This section provides examples showing Schedule Types that are processed as Odd Schedules and those that are not.</p>
<p><strong>Note:</strong> For an Odd Schedule to occur, both statements for a Schedule Type must be False.</p>
<h3 id="examples-of-odd-schedules">Examples of Odd Schedules</h3>
<p>Schedule Type: Q5H (300 minutes)</p>
<p>300 minutes divided by 1440 minutes = fraction, not a whole number = False</p>
<p>1440 divided by 300 minutes = 4.8 (fraction, not a whole number) = False</p>
<p>Schedule Type: Q3XM (13440 minutes)</p>
<p>13440 minutes divided by 1440 minutes = 9.3 (fraction, not a whole number) = False</p>
<p>1440 divided by 13440 minutes = fraction, not a whole number = False</p>
<h3 id="examples-of-schedules-that-are-not-odd-schedules">Examples of Schedules That Are Not Odd Schedules</h3>
<p>Schedule Type: Q2H (120 minutes)</p>
<p>120 minutes divided by 1440 minutes = 8.3 (fraction, not a whole number) = False</p>
<p>1440 minutes divided by 120 = 12 (whole number) = True</p>
<p>Schedule Type: QOD (2880 minutes)</p>
<p>2880 minutes divided by 1440 minutes = 2 (whole number) = True</p>
<p>1440 minutes divided by 2880 = 0.5 (fraction, not a whole number) = False</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="sample-hl7-data-fields-broadcast-to-bcma-subscribers">Sample HL7 Data Fields Broadcast to BCMA Subscribers</h2></td>
<td><p>BCMA includes the Standards from the HL7 V. 2.4 (VistA Messaging) package. For more information, refer to the VistA Messaging and Interface Services Web site at: REDACTED.</p>
<p>This section provides a list of sample Health Level Seven (HL7) data fields that BCMA broadcasts to BCMA HL7 subscribers. Review the information to learn the "RAS" messages created for the administration and/or update of a medication order. The activities, which cause the broadcast of BCMA HL7 messages, are called "trigger events." BCMA HL7 trigger events are MEDPASS, UPDATE STATUS, PRN EFFECTIVENESS, and ADD COMMENT.</p>
<p><strong>Note:</strong> Every message will not use every data field and every segment provided. Some segments may repeat as necessary. Some segments may not appear in the exact order depicted below for all trigger events, but they will be consistent for each specific trigger event.</p></td>
</tr>
</tbody>
</table>

Example: "RAS" Messages Created for the Administration of a Medication Order

| SEG | SEQ | Field Name                      | Example             | HL7 Type                                   |
|-----|-----|---------------------------------|---------------------|--------------------------------------------|
|     |     |                                 |                     |                                            |
| MSH | 1   | Field Separator                 | ^                   | string                                     |
|     | 2   | Encoding Characters             | ~\|\\               | string                                     |
|     | 3   | Sending Application             | PSB HL7 SRV         | hierarchic designator                      |
|     | 4   | Sending Facility                |                     | hierarchic designator                      |
|     | 5   | Receiving Application           | PSB HL7 SUB         | hierarchic designator                      |
|     | 6   | Receiving Facility              |                     | hierarchic designator                      |
|     | 7   | D/T of Message                  | 20030530075514-0600 | HL7 format timestamp (yyyymmddhhnnss-0600) |
|     | 8   | Security                        |                     | string                                     |
|     | 9   | Message Type                    | RAS~O17             | composite                                  |
|     | 10  | Message Control ID              | 5001457             | string                                     |
|     | 11  | Processing ID                   | P                   | processing type                            |
|     | 12  | Version ID                      | 2.4                 | ID                                         |
|     | 13  | Sequence Number                 |                     | numeric                                    |
|     | 14  | Continuation Pointer            |                     | string                                     |
|     | 15  | Accept Acknowledgement Type     | AL                  | ID                                         |
|     | 16  | Application Acknowledgment Type | NE                  | ID                                         |
|     | 17  | Country Code                    | USA                 | ID                                         |
|     | 18  | Character Set                   |                     | ID                                         |
|     | 19  | Principal Language of Message   |                     | coded element                              |

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: "RAS" Messages Created for the Administration of a Medication Order  
(cont.)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>SEQ</th>
<th>Field Name</th>
<th>Example</th>
<th>HL7 Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PID</td>
<td>3</td>
<td>Patient Identifier List</td>
<td>748</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Alternate Patient ID</td>
<td>54~~~~AGE</td>
<td>extended composite ID</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Patient Name</td>
<td>BCMAPATIENT~TWO</td>
<td>patient name</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>Date/Time of Birth</td>
<td>19490101</td>
<td>HL7 format timestamp (yyyymmdd)</td>
</tr>
<tr class="even">
<td></td>
<td>8</td>
<td>Administrative Sex</td>
<td>M</td>
<td>user table</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td><p>SSN Number (VA)</p>
<p>or HRN Number (IHS)– Patient</p></td>
<td><p>000001000 (VA)</p>
<p>or 123456 (IHS)</p></td>
<td>string</td>
</tr>
<tr class="even">
<td>PV1</td>
<td>2</td>
<td>Patient Class</td>
<td>U</td>
<td>table 0004</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Patient Location</td>
<td>7A GEN MED 724-A~~~500</td>
<td>user table</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>Attending Doctor</td>
<td>BCMAPROVIDER~ONE</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>1</td>
<td>Order Control</td>
<td>XX</td>
<td>table 119</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Placer Order Number</td>
<td>1045~PSB~1045~IEN</td>
<td>entity identifier</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Filler Order Number</td>
<td>13V</td>
<td>entity identifier</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>Quantity/Timing</td>
<td>~~~~~~~~~C</td>
<td>dosage, scheduled administration time, schedule type</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>Parent</td>
<td>~</td>
<td>composite</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>D/T of Transaction</td>
<td>20030530075514-0600</td>
<td>HL7 format timestamp (yyyymmddhhnnss-0600)</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Entered by</td>
<td>BCMANURSE~ONE</td>
<td>extended composite name</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>Order Effective D/T</td>
<td>20030530075514-0600</td>
<td>HL7 format timestamp (yyyymmddhhnnss-0600)</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td>Action By</td>
<td>BCMANURSE~ONE</td>
<td>extended composite name</td>
</tr>
<tr class="even">
<td>RXR</td>
<td>1</td>
<td>Route</td>
<td>IV</td>
<td>table 0162</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Administration Site</td>
<td>3 INJECTION SITE</td>
<td>table 0163</td>
</tr>
<tr class="even">
<td>RXO</td>
<td>1</td>
<td>Requested Give Code</td>
<td>269~FLUOROURACIL</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Requested Give Amount</td>
<td></td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>Requested Dispense Code</td>
<td>748V52</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>21</td>
<td>Requested Give Rate Amount</td>
<td>~250 ml/hr</td>
<td>string</td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: "RAS" Messages Created for the Administration of a Medication Order  
(cont.)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>SEQ</th>
<th>Field Name</th>
<th>Example</th>
<th>HL7 Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>RXC</td>
<td>1</td>
<td>RX Component Type</td>
<td>A</td>
<td>table 0166</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Component Code</td>
<td>20~5-FLUOURACIL</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Component Amount</td>
<td>5-FLUOURACIL</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Component Units</td>
<td></td>
<td>coded element</td>
</tr>
<tr class="even">
<td>RXC</td>
<td>1</td>
<td>RX Component Type</td>
<td>B</td>
<td>table 0166</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Component Code</td>
<td>8~AMINO ACID SOLUTION 8.5%</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Component Amount</td>
<td>AMINO ACID SOLUTION 8.5%</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Component Units</td>
<td></td>
<td>coded element</td>
</tr>
<tr class="even">
<td>RXA</td>
<td>1</td>
<td>Give Sub-ID Counter</td>
<td>0</td>
<td>number</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Administration Sub-ID Counter</td>
<td>1</td>
<td>number</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Date/Time Start of Administration</td>
<td>20030530075514-0600</td>
<td>HL7 format timestamp (yyyymmddhhnnss-0600)</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Administered Code</td>
<td>20~5-FLUOURACIL</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>Administered Amount</td>
<td>450 MG</td>
<td>number</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>Administered Unit</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>Administration Notes</td>
<td></td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>18</td>
<td>Substance/Treatment Refusal Reason</td>
<td>~Elevated Blood Sugar</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td>Indication</td>
<td>~</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>20</td>
<td>Completion Status</td>
<td>C</td>
<td>user table</td>
</tr>
<tr class="even">
<td>NTE</td>
<td>2</td>
<td>Source of Comment</td>
<td></td>
<td>table 105</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Comment</td>
<td>This is a comment …</td>
<td>free text</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Comment Type</td>
<td>BCMANURSE~ONE~20030530075514-0600~Date Entered</td>
<td><p>coded element</p>
<p>(includes HL7 format timestamp [yyyymmddhhnnss-0600])</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="definitions-of-data-fields-under-field-name-column">Definitions of Data Fields Under FIELD NAME Column</h2></td>
<td><p>This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field. The message header (i.e., the MSH segment) is constructed and supported by the VistA HL7 message development tool.</p>
<p><strong>Note:</strong> The MSH segment field names are <em>not</em> described below.</p>
<p><strong>PATIENT ID:</strong> Field (#.01) of the BCMA MEDICATION LOG file (#53.79) and Internal Entry Number (IEN) pointer to the PATIENT file (#2).</p>
<p><strong>PATIENT NAME:</strong> As returned by the Application Program Interface (API) VADPT.</p>
<p><strong>DATE OF BIRTH:</strong> As returned by the API VADPT.</p>
<p><strong>ADMINISTRATIVE SEX:</strong> As returned by the API VADPT.</p>
<p>SSN NUMBER (VA) or HRN NUMBER (IHS): As returned by the API VADPT.</p>
<p><strong>PATIENT LOCATION:</strong> Field (#.02) of the BCMA MEDICATION LOG file (#53.79), which contains the actual room-bed and ward location of the patient at the time the medication pass occurred. Also contains field (#.03) of the BCMA MEDICATION LOG file (#53.79), which contains the division number of the ward that the patient was on during the medication pass.</p>
<p><strong>PLACER ORDER NUMBER:</strong> IEN for the BCMA MEDICATION LOG file (#53.79).</p>
<p><strong>FILLER ORDER NUMBER:</strong> Contains the ORDER REFERENCE NUMBER field (#.11) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN of the actual medication order from the PHARMACY PATIENT file (#55)PREVIOUS ORDER NUMBER as returned by the API PSJBCMA1.</p>
<p><strong>QUANTITY/TIMING:</strong> Contains the order dosage, schedule type, and scheduled administration time data from the BCMA MEDICATION LOG file (#53.79), fields #.15, #.12, and #.13 respectively.</p>
<p><strong>PARENT:</strong> Contains the PREVIOUS ORDER NUMBER as returned by the PSB routine PSBVT.</p>
<p><strong>DATE/TIME OF TRANSACTION:</strong> Contains the ACTION DATE/TIME field (#.06) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time of the actual time that the action was taken.</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="definitions-of-data-fields-under-field-name-column-cont." class="H2-Continued">Definitions of Data Fields Under FIELD NAME Column (cont.)</h2></td>
<td><p>This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.</p>
<p><strong>ENTERED BY:</strong> Field (#.05) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN pointer to the NEW PERSON file (#200) for the user who entered the data, along with the actual name of that person as returned by FileMan.</p>
<p><strong>ORDER EFFECTIVE DATE/TIME:</strong> Provides data from the ENTERED DATE/TIME field (#.04) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time that the action was taken.</p>
<p><strong>ACTION BY:</strong> Field (#.07) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN pointer to the NEW PERSON file (#200) for the user who took the action.</p>
<p><strong>ROUTE:</strong> Contains MEDICATION ROUTE data as returned by the PSB routine PSBVT. The ROUTE data is required for the RXR message segment.</p>
<p><strong>ADMINISTRATION SITE:</strong> Presents the INJECTION SITE field (#.16) of the BCMA MEDICATION LOG file (#53.79), which lists the injection site where the medication was administered.</p>
<p><strong>REQUESTED GIVE CODE:</strong> Presents the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), containing a pointer to the ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.</p>
<p><strong>REQUESTED GIVE AMOUNT:</strong> Provides the ORDER DOSAGE field (#.15) of the BCMA MEDICATION LOG file (#53.79), which contains the dosage from the original medication order.</p>
<p><strong>REQUESTED DISPENSE CODE:</strong> Presents the IV UNIQUE ID field (#.26) of the BCMA MEDICATION LOG file (#53.79), which contains the unique ID number for an<br />
IV bag.</p>
<p><strong>REQUESTED GIVE RATE AMOUNT:</strong> Presents the INFUSION RATE field (#.35) of the BCMA MEDICATION LOG file (#53.79), which contains the infusion rate for an<br />
IV bag.</p>
<p><strong>RX COMPONENT TYPE:</strong> Contains data specifying the "type" of item/component processed. Within the HL7 standard table, "A" signifies additive and "B" signifies base.</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="definitions-of-data-fields-under-field-name-column-cont.-1" class="H2-Continued">![](bcma-version-3-technical-manual-security-guide-psb-3-142/016.png)Definitions of Data Fields Under FIELD NAME Column (cont.)</h2></td>
<td><p>This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.</p>
<p><strong>COMPONENT CODE:</strong> Presents the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), containing a pointer to the ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.</p>
<p><strong>COMPONENT AMOUNT:</strong>Presents the DOSES ORDERED field (#.02) within the DISPENSE DRUG multiple (#.5) within the BCMA MEDICATION LOG file (#53.79), which contains the number of units.</p>
<p><strong>COMPONENT UNITS:</strong> Consists of the UNIT OF ADMINISTRATION field (#.04) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the unit(s) for the medication administered.</p>
<p><strong>GIVE SUB-ID COUNTER:</strong> A required field with a value<br />
of "00."</p>
<p><strong>ADMINISTRATION SUB-ID COUNTER:</strong> A required field with a numeric value.</p>
<p><strong>DATE/TIME START OF ADMINISTRATION:</strong> Presents the ACTION DATE/TIME field (#.06) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time that the action was taken.</p>
<p><strong>ADMINISTERED CODE:</strong> Composed of the ADMINISTRATION MEDICATION field (#.08) of the BCMA MEDICATION LOG file (#53.79), which contains a pointer to ORDERABLE ITEM file (#50.7), which provides the medication entered for the order, as well as the actual orderable item name as returned by FileMan.</p>
<p><strong>ADMINISTERED AMOUNT:</strong> Consists of the DOSES GIVEN field (#.03) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the actual number of units administered to the patient.</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="definitions-of-data-fields-under-field-name-column-cont.-2" class="H2-Continued">Definitions of Data Fields Under FIELD NAME Column (cont.)</h2></td>
<td><p>This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field.</p>
<p><strong>ADMINISTERED UNIT:</strong> UNIT OF ADMINISTRATION field (#.04) of the respective file multiple (i.e., DISPENSE DRUG [#.5], ADDITIVES [#.6], or SOLUTIONS [.7]) within the BCMA MEDICATION LOG file (#53.79), which contains the unit(s) for the medication administered.</p>
<p><strong>ADMINISTRATION NOTES:</strong> Consists of the AUDIT LOG field (#.9) and the AUDIT LOG field (#.01) of the AUDIT LOG multiple (#.9) within the BCMA MEDICATION LOG file (#53.79).</p>
<p><strong>SUBSTANCE/TREATMENT REFUSAL REASON:</strong> Field (#.21) of the BCMA MEDICATION LOG file (#53.79), which contains the PRN reason for administering a PRN medication.</p>
<p><strong>INDICATION:</strong> Consists of the ORDER ADMINISTRATION VARIANCE field (#.14), of the BCMA MEDICATION LOG file (#53.79), which if a Continuous medication order, will contain the minutes early (&lt;1) or late (&gt;1) that the medication was administered.</p>
<p><strong>COMPLETION STATUS:</strong> Consists of the ACTION STATUS field (#.09) of the BCMA MEDICATION LOG file (#53.79), which contains the status of the medication pass. Values in this field will equal an ACTION STATUS value.</p>
<p><strong>SOURCE OF COMMENTS:</strong> "O" source of the subsequent message.</p>
<p><strong>COMMENT:</strong> Contains the PRN EFFECTIVENESS field (#.22) of the BCMA MEDICATION LOG file (#53.79). When appropriate, contains a composite of the COMMENT field (#.3) and the COMMENT field (#.01) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the comments entered.</p>
<p><strong>COMMENT TYPE:</strong> Contains a composite of the ENTERED BY field (#.02) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the pointer to the NEW PERSON file (#200) for the user that entered the comment; along with the actual name of the user as returned by FileMan; as well as the ENTERED DATE/TIME field (#.03) of the COMMENT multiple (#.3) within the BCMA MEDICATION LOG file (#53.79), which contains the date and time that the entry was filed and the string "Date Entered."</p></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="sample-hl7-data-fields-passed-in-each-trigger-event">Sample HL7 Data Fields Passed in Each Trigger Event</h2></td>
<td><p>This section identifies the HL7 data fields that are passed in each of the four "trigger events" associated with BCMA, and examples of medication administrations. The processed trigger events are MEDPASS, UPDATE STATUS, PRN EFFECTIVENESS, and ADD COMMENT. For each event, there is an order control code and a set of data fields listed. For any given event; however, some of the data fields may be empty. Administration Notes is such an example.</p>
<p>The protocols provided in the table, use the BCMA name spacing convention ("PSB"), as do the messages sent by BCMA. The BCMA HL7 messages are unsolicited; therefore, acknowledgment messages are unnecessary and not recognized by the PSB protocol.</p>
<p><strong>Note:</strong> Word wrapping is in effect for the example Medications Administrations on the following pages.</p></td>
</tr>
</tbody>
</table>

Example: Data Fields Passed in Each Trigger Event Associated with BCMA HL7

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 38%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Broadcast from BCMA</th>
<th>Subscribing Application</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>MEDPASS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Protocol</td>
<td>PSB RAS O17 SRV</td>
<td>PSB RAS O17 SUB</td>
</tr>
<tr class="even">
<td>Order Control</td>
<td>XX (Order/service changed)</td>
<td></td>
</tr>
<tr class="odd">
<td>HL7 Fields</td>
<td><p>MSH (as prepared by HL7 tool)</p>
<p>PID: 3,4,5,7,8,19</p>
<p>PV1: 2,3,7</p>
<p>ORC: 1,2,3,7,8,9,10,15,19</p>
<p>RXO: 1,2,10,21</p>
<p>NTE: 2,3,4</p>
<p>RXR: 1,2</p>
<p>RXC: 1,2,3,4</p>
<p>RXA: 1,2,3,4,5,6,7,9,18,19,20</p></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Medication Administrations

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="medpass">MEDPASS</h5>
<p>Message:</p>
<p>MESSAGE HEADER:</p>
<p>MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530075514-0600^^RAS~O17^5001559^P^2.4^^^AL^NE^USA</p>
<p>MESSAGE TEXT:</p>
<p>PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000</p>
<p>PV1^^U^7A GEN MED 724-A~~~500^^^^BCMANURSE~ONE</p>
<p>ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^200305300755140-600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE</p>
<p>RXO^269~FLUOROURACIL^^^^^^^^^748V52^^^^^^^^^^^~250 ml/hr</p>
<p>NTE^^O^1~This is a comment...^BCMANURSE~ONE~20030530075514-0600~Date Entered</p>
<p>RXR^IV^3 INJECTION SITE</p>
<p>RXC^A^20~5-FLUOURACIL^5-FLUOURACIL^</p>
<p>RXC^B^8~AMINO ACID SOLUTION 8.5%^AMINO ACID SOLUTION 8.5%^</p>
<p>RXA^0^1^20030530075514-0600^ ^20~5-FLUOURACIL^450 MG^^^^^^^^^^^^^~^I</p>
<p>RXA^0^2^20030530075514-0600^ ^8~AMINO ACID SOLUTION 8.5%^500 ML^^^^^^^^^^^^^~^I</p>
<h5 id="update-status">UPDATE STATUS</h5>
<p>Message:</p>
<p>MESSAGE HEADER:</p>
<p>MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530090340-0600^^RAS~O17^5001561^P^2.4^^^AL^NE^USA</p>
<p>MESSAGE TEXT:</p>
<p>PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000</p>
<p>PV1^^U^7A GEN MED 724-A~~~500^^^^BCMANURSE~ONE</p>
<p>ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^200305300903400-600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE</p>
<p>RXO^269~FLUOROURACIL^^^^^^^^^748V52^^^^^^^^^^^~250 ml/hr</p>
<p>NTE^^O^2~Add this comment to the administration...^BCMANURSE~ONE~20030530082444-0600~Date Entered</p>
<p>RXR^IV^3 INJECTION SITE</p>
<p>RXC^A^20~5-FLUOURACIL^5-FLUOURACIL^</p>
<p>RXC^B^8~AMINO ACID SOLUTION 8.5%^AMINO ACID SOLUTION 8.5%^</p>
<p>RXA^0^1^20030530090340-0600^ ^20~5-FLUOURACIL^450 MG^^^4~20030530090340-0600^^^^^^^^^^~^C</p>
<p>RXA^0^2^20030530090340-0600^ ^8~AMINO ACID SOLUTION 8.5%^500 ML^^^4~20030530090340-0600^^^^^^^^^^~^C</p></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

# Appendix B: HL7 Messaging for BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Medication Administrations (cont.)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prn-effectiveness">PRN EFFECTIVENESS</h5>
<p>Message:</p>
<p>MESSAGE HEADER:</p>
<p>MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530110049-0600^^RAS~O17^5001562^P^2.4^^^AL^NE^USA</p>
<p>MESSAGE TEXT:</p>
<p>PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000</p>
<p>ORC^XX^1040~PSB~1040~IEN^28U^^^^13oz~Q6H~~~~~~~~P^~^20030529132246-0600^BCMANURSE~ONE^^^^^20030529132246-0600^^^^BCMANURSE~ONE</p>
<p>NTE^^O^ Effectiveness comment for 5/29/2003 1:22PM admin...^BCMANURSE~ONE~20030530110049-0600~Date Entered~~1298~PRN Minutes</p>
<h5 id="add-comment">ADD COMMENT</h5>
<p>Message:</p>
<p>MESSAGE HEADER:</p>
<p>MSH^~|\&amp;^PSB HL7 SRV^^PSB HL7 SUB^^20030530082444-0600^^RAS~O17^5001560^P^2.4^^^AL^NE^USA</p>
<p>MESSAGE TEXT:</p>
<p>PID^^^748^54~~~~AGE^BCMAPATIENT~TWO^^19490101^M^^^^^^^^^^^000001000</p>
<p>ORC^XX^1045~PSB~1045~IEN^13V^^^^~~~~~~~~~C^~^20030530075514-0600^BCMANURSE~ONE^^^^^20030530075514-0600^^^^BCMANURSE~ONE</p>
<p>NTE^^O^2~Add this comment to the administration...^BCMANURSE~ONE~20030530082444-0600~Date Entered</p></td>
</tr>
</tbody>
</table>

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="introduction">Introduction</h2></th>
<th><p>The Bar Code Medication Administration (BCMA) Medication package includes an interface between the <em>Label Print</em> [PSBO BL] option and the bar code label printer. The <em>Label Print</em> [PSBO BL] option currently prints Unit Dose labels on a label printer. This interface allows a unique bar code to be printed on the first line of the Unit Dose label.</p>
<p>Since users can now customize their own label formats using control codes, it is important to note that all Unit Dose and Ward Stock medication labels must conform to the JCAHO Standard for Medication Labeling (Standard MM.4.30). Please refer to the excerpt of the standard and references at the end of this Appendix.</p>
<p>Any printer that supports bar code printing can be used for the Unit Dose labels. However, the scan success rate will probably be lower if anything other than direct thermal transfer on synthetic labels is used. Labels from dot matrix printers, laser printers, or even bar code printers using other types of transfer, wipe off more easily. The label could become unreadable, especially in areas where the bag might become wet. With a direct thermal transfer onto a synthetic label, the print actually bonds to the label material. Essentially, the label would have to be ripped to damage the print.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><h2 id="hardware-setup">Hardware Setup</h2></td>
<td>The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.</td>
</tr>
<tr class="odd">
<td><h2 id="section-2"></h2></td>
<td></td>
</tr>
<tr class="even">
<td><h2 id="software-setup">Software Setup</h2></td>
<td><p>The type of printer will determine the next step. The Zebra and Intermec printers require control codes, where the dot matrix or laser printers do not require these codes. The Unit Does print routine checks the existence of the control codes before attempting to execute. It is not required for all control codes to be defined; just build the necessary control codes for the selected printer.</p>
<p>When setting up the Terminal Type file for the Zebra bar code printer device, the Terminal Type file entry must contains the word "ZEBRA" as part of the file name.</p>
<p>For example: P-ZEBRA</p>
<p>When setting up the Terminal Type file for the Intermec bar code printer device, the Terminal Type file entry must contains the word "INTERMEC" as part of the file name.</p>
<p>For example: P-INTERMEC</p></td>
</tr>
</tbody>
</table>

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th><p>The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.</p>
<h3 id="printer-control-codes">Printer Control Codes</h3>
<p>For this type of printer to print a unique bar code on the Unit Dose labels, IRMs must build control codes. The CONTROL CODES fields [#55] are added to the TERMINAL TYPE file (#3.2) in the Kernel patch XU*8*205. <strong>This patch must be installed before proceeding</strong>.</p>
<h3 id="control-code-set-up">Control Code Set Up</h3>
<p>The Unit Dose label print routine currently uses printer control codes and code names that are built within FileMan. The following table illustrates the control codes and corresponding names for the Zebra printer.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Zebra Printer Terminal Type Control Codes

| Abbreviation | Full Name               | Control Code                                                                                                                                                                                                                     |
|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ET           | End Text                | N/A                                                                                                                                                                                                                              |
| ETF          | End Text Field          | N/A                                                                                                                                                                                                                              |
| EB           | End Barcode             | W !,"^FO20,150^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"                                                                                                                                                                                |
| EBF          | End Barcode Field       | N/A                                                                                                                                                                                                                              |
| EL           | End Label               | W !,"^XZ"                                                                                                                                                                                                                        |
| FE           | Format End              | N/A                                                                                                                                                                                                                              |
| FI           | Format Initialization   | N/A                                                                                                                                                                                                                              |
| FI1          | Format Initialization 1 | N/A                                                                                                                                                                                                                              |
| FI2          | Format Initialization 2 | N/A                                                                                                                                                                                                                              |
| HAZ          | Hazardous Text          | S PSBTYPE=\$S(PSBTLE="HAZTEXT":"20,60",1:"0,0")                                                                                                                                                                                  |
| SB           | Start Barcode           | S PSBTYPE=\$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N") S:PSBSYM="" PSBBAR="NO-CODE"  W !,"^BY2,3.0^FO20,100^"\_PSBTYPE\_",N,80,Y,N^FR^FD"\_PSBBAR\_"^FS"                                                                   |
| SBF          | Start Barcode Field     | N/A                                                                                                                                                                                                                              |
| SL           | Start Label             | W !,"^XA",!,"^LH0,0^FS"                                                                                                                                                                                                          |
| ST           | Start Text              | W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"                                                                                                                                                                         |
| STF          | Start Text Field        | S PSBTYPE=\$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60", PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90", PSBTLE="PSBLOT":"350,120", PSBTLE="PSBEXP":"350,150", PSBTLE="PSBMFG":"500,150", PSBTLE="PSBFCB":"350,180" |

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-1" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th>The field position map below identifies the specific control codes for the Zebra printer that direct the exact position in which the fields are printed on the bar code label.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: <span id="C3_Printer" class="anchor"></span>Zebra Bar Code Label - Field Position Map

| Abbreviation | Control Code ( Field Coordinates) | Description                        |
|--------------|-----------------------------------|------------------------------------|
| EB           | FO20,150                          | "No – Code" statement              |
| HAZ          | PSBTLE="HAZTEXT":"20,60"          | Hazardous to Handle and/or Dispose |
| SB           | FO20,100 "                        | Bar Code Graph                     |
| STF          | PSBTLE="PSBDRUG":"20,25"          | Drug Name                          |
|              | PSBTLE="PSBDOSE":"20,60",         | Dosage                             |
|              | PSBTLE="PSBNAME":"350,60"         | Patient Name and Quality           |
|              | PSBTLE="PSBWARD":"350,90",        | Ward Location                      |
|              | PSBTLE="PSBLOT":"350,120",        | Lot Number                         |
|              | PSBTLE="PSBEXP":"350,150",        | Expiration Date                    |
|              | PSBTLE="PSBMFG":"500,150",        | Manufacturer                       |
|              | PSBTLE="PSBFCB":350,180",         | Filled By/Checked By               |

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-2" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th>The following table illustrates the control codes and corresponding names for the Intermec printer.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Intermec Printer Terminal Type Control Codes

| Abbreviation | Full Name               | Control Code                                                                                                                                                                                       |
|--------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ET           | End Text                | N/A                                                                                                                                                                                                |
| ETF          | End Text Field          | N/A                                                                                                                                                                                                |
| EB           | End Barcode             | W "\<STX\>H8;o50,40;f3;c7;h2;w2;d0,80;\<ETX\>",!                                                                                                                                                   |
| EBF          | End Barcode Field       | N/A                                                                                                                                                                                                |
| EL           | End Label               | W "\<STX\>\<ETB\>\<ETX\>",!                                                                                                                                                                        |
| FE           | Format End              | N/A                                                                                                                                                                                                |
| FI           | Format Initialization   | W "\<STX\>\<ESC\>C\<ETX\>",!,"\<STX\>\<ESC\>P\<ETX\>",!,"\<STX\>E2;F2\<ESC\>\<ETX\>",!                                                                                                             |
| FI1          | Format Initialization 1 | W "\<STX\>H7;o30,260;f3;c7;h2;w2;d0,80;\<ETX\>",!,"\<STX\>H6;o50,440;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H5;o50,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H4;o70,260;f3;c7;h2;w2;d0,20;\<ETX\>",!  |
| FI2          | Format Initialization 2 | W "\<STX\>H3;o90,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H2;o110,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H1;o110,40;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H0;o130,40;f3;c7;h2;w2;d0,40;\<ETX\>",! |
| SB           | Start Barcode           | W "\<STX\>"\_TEXT\_"\<ETX\>",!                                                                                                                                                                     |
| SBF          | Start Barcode Field     | S PSBTYPE=\$S(PSBSYM="I25":"c2,0",PSBSYM="128":"c6,0",1:"c0,0") W "\<STX\>B8;o85,40;f3;"\_PSBTYPE\_";i1;do,25;p@;\<ETX\>",!,"\<STX\>I8;h1;w1;\<ETX\>",!                                            |
| SL           | Start Label             | W "\<STX\>R;\<EXT\>",!,"\<STX\>\<ESC\>E2\<EXT\>",!                                                                                                                                                 |
| ST           | Start Text              | W "\<STX\>"\_TEXT\_"\<CR\>\<ETX\>",!                                                                                                                                                               |
| STF          | Start Text Field        | N/A                                                                                                                                                                                                |

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-3" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th>The field position map below identifies the specific control codes for the Intermec printer that direct the exact position in which the fields are printed on the bar code label.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Intermec Bar Code Label - Field Position Map

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 53%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Abbreviation</th>
<th>Control Code ( Field Coordinates)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EB</td>
<td>&lt;STX&gt;H8;o50,40;f3;c7;h2;w2;d0,80;&lt;ETX&gt;</td>
<td>"No – Code" statement</td>
</tr>
<tr class="even">
<td rowspan="4">FI1</td>
<td>&lt;STX&gt;H7;o30,260;f3;c7;h2;w2;d0,80;&lt;ETX&gt;</td>
<td>Filled By/Checked By</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H6;o50,440;f3;c7;h2;w2;d0,20;&lt;ETX&gt;"</td>
<td>Manufacturer</td>
</tr>
<tr class="even">
<td>&lt;STX&gt;H5;o50,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;</td>
<td>Expiration Date</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H4;o70,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;</td>
<td>Lot Number</td>
</tr>
<tr class="even">
<td rowspan="4">FI2</td>
<td>&lt;STX&gt;H3;o90,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;</td>
<td>Ward Location</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H2;o110,260;f3;c7;h2;w2;d0,20;&lt;ETX&gt;</td>
<td>Patient Name and Quality</td>
</tr>
<tr class="even">
<td>&lt;STX&gt;H1;o110,40;f3;c7;h2;w2;d0,20;&lt;ETX&gt;</td>
<td>Dosage</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H0;o130,40;f3;c7;h2;w2;d0,40;&lt;ETX&gt;</td>
<td>Drug Name</td>
</tr>
<tr class="even">
<td>SBF</td>
<td><p>&lt;STX&gt;B8;o85,40;f3;"_PSBTYPE_";i1;do,25;p@;&lt;ETX&gt;</p>
<p>&lt;STX&gt;I8;h1;w1;&lt;ETX&gt;"</p></td>
<td>Bar code Graph</td>
</tr>
</tbody>
</table>

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-4" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th><h3 id="example-terminal-type-files">Example Terminal Type Files </h3>
<p>The following are examples of terminal type file setups that were used in the development process. These examples are provided to guide the user in the setup process. Please note that they are only examples, and may not be appropriate for your configuration.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="C6" class="anchor"></span>Example: Zebra Printer Sample Terminal Type File

NUMBER: 1 ABBREVIATION: SL

FULL NAME: Start Label CONTROL CODE: W !,"^XA",!,"^LH0,0^FS"

NUMBER: 2 ABBREVIATION: EL

FULL NAME: End Label CONTROL CODE: W !,"^XZ"

NUMBER: 3 ABBREVIATION: SB

FULL NAME: Start Barcode

CONTROL CODE: S PSBTYPE=\$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N") S:PSBSYM="" PSBBAR="NO-CODE" W !,"^BY2,3.0^FO20,100^"\_PSBTYPE\_",N,80,Y,N^FR^FD"\_PSBBAR\_"^FS"

NUMBER: 4 ABBREVIATION: EB

FULL NAME: End Barcode

CONTROL CODE: W !,"^FO20,150^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 5 ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 6 ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S PSBTYPE=\$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60", PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90", PSBTLE="PSBLOT":"350,120", PSBTLE="PSBEXP":"350,150", PSBTLE="PSBMFG":"500,150", PSBTLE="PSBFCB":"350,180",1:"0,0")

<span id="P_C6" class="anchor"></span>Example: Zebra Printer Sample Terminal Type File with HAZ Control Code

NAME: P-TCP-ZEB-UD-HAZ 200DPI

NUMBER: 1 CTRL CODE ABBREVIATION: SL

FULL NAME: Start Label CONTROL CODE: W !,"^XA",!,"^LH0,0^FS"

NUMBER: 2 CTRL CODE ABBREVIATION: EL

FULL NAME: End Label CONTROL CODE: W !,"^XZ"

NUMBER: 3 CTRL CODE ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 4 CTRL CODE ABBREVIATION: SB

FULL NAME: Start Barcode

CONTROL CODE: S PSBTYPE=\$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N,N")

S:PSBSYM="" PSBBAR="NO-CODE" W !,"^BY2,3.0,80^FO20,115^"\_ PSBTYPE\_",60,Y,N^FR^FD"\_PSBBAR\_"^FS"

<span id="P_C7" class="anchor"></span>NUMBER: 5 CTRL CODE ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S SBTYPE=SPSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,85",

PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90",

PSBTLE="PSBLOT":"350,120",PSBTLE="PSBEXP":"350,150",

PSBTLE="PSBMFG":"500,150",PSBTLE="PSBFCB":"350,180",1:"0,0")

NUMBER: 6 CTRL CODE ABBREVIATION: HAZ

FULL NAME: Hazardous Text Field

CONTROL CODE: S PSBTYPE=\$S(PSBTLE="HAZTEXT":"20,60",1:"0,0") CONTROL CODE: W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"

NUMBER: 6 ABBREVIATION: STF

FULL NAME: Start Text Field

CONTROL CODE: S PSBTYPE=\$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60",1:"0,0")

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-5" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th>The following shows a sample Intermec printer terminal type file.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Intermec Printer Sample Terminal Type File

NUMBER: 1 ABBREVIATION: SL

FULL NAME: Start Label

CONTROL CODE: W "\<STX\>R;\<EXT\>",!,"\<STX\>\<ESC\>E2\<EXT\>",!

NUMBER: 2 ABBREVIATION: EL

FULL NAME: End Label CONTROL CODE: W "\<STX\>\<ETB\>\<ETX\>",!

NUMBER: 3 ABBREVIATION: FI1

FULL NAME: Format Initialization 1

CONTROL CODE: W "\<STX\>H7;o30,260;f3;c7;h2;w2;d0,80;\<ETX\>",!,"\<STX\>H6;o50,440;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H5;o50,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H4;o70,260;f3;c7;h2;w2;d0,20;\<ETX\>",!

NUMBER: 4 ABBREVIATION: FI2

FULL NAME: Format Initialization 2

CONTROL CODE: W "\<STX\>H3;o90,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H2;o110,260;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H1;o110,40;f3;c7;h2;w2;d0,20;\<ETX\>",!,"\<STX\>H0;o130,40;f3;c7;h2;w2;d0,40;\<ETX\>",!

NUMBER: 5 ABBREVIATION: SBF

FULL NAME: Start Barcode Field

CONTROL CODE: S PSBTYPE=\$S(PSBSYM="I25":"c2,0",PSBSYM="128":"c6,0",1:"c0,0") W "\<STX\>B8;o85,40;f3;"\_PSBTYPE\_";i1;do,25;p@;\<ETX\>",!,"\<STX\>I8;h1;w1;\<ETX\>",!

NUMBER: 6 ABBREVIATION: SB

FULL NAME: Start Barcode CONTROL CODE: W "\<STX\>"\_TEXT\_"\<ETX\>",!

NUMBER: 7 ABBREVIATION: EB

FULL NAME: End Barcode

CONTROL CODE: W "\<STX\>H8;o50,40;f3;c7;h2;w2;d0,80;\<ETX\>",!

NUMBER: 8 ABBREVIATION: FI

FULL NAME: Format Initialization

CONTROL CODE: W "\<STX\>\<ESC\>C\<ETX\>",!,"\<STX\>\<ESC\>P\<ETX\>",!,"\<STX\>E2;F2\<ESC\>\<ETX\>",!

NUMBER: 9 ABBREVIATION: ST

FULL NAME: Start Text

CONTROL CODE: W "\<STX\>"\_TEXT\_"\<CR\>\<ETX\>",!

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="software-setup-contd-6" class="H2-Continued">Software Setup (cont'd)</h2></th>
<th><h3 id="dot-matrix-and-laser-printers">Dot Matrix and Laser Printers</h3>
<p>The control codes in the TERMINAL TYPE file (#3.2) are not required for dot matrix and laser printers. However, the BAR CODE ON field [#60] and BAR CODE OFF field [#61] in the TERMINAL TYPE file (#3.2) are needed.</p>
<p>An example of each field is shown below for the Output Technology Corporation (OTC) printers. Please note that it is only an example and may not be appropriate for your configuration.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: OTC Printer Example

BAR CODE OFF: \$C(27),"\[0t",!

BAR CODE ON: \$C(27),"\[4;4;0;2;4;2;4;2}",\$C(27),"\[3t"

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="printed-bar-code-unit-dose-label-sample">Printed Bar Code Unit Dose Label Sample</h2></th>
<th>With this interface, a unique bar code will be printed on the first line of the Unit Dose label with the label number printed below it. Depending upon the type of printer used, the asterisks (*) may or may not be printed on either side of the label number.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: Sample Unit Dose Bar Code Label

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Drug: BACLOFEN 10MG TABS (Qty: 1)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Dosage: 25MG</td>
<td rowspan="2"><p>Patient: BCMAPATIENT,ONE</p>
<p>Ward: GEN MED</p>
<p>Lot: 123141</p>
<p>Exp: 4/5/2006 Mfg: UPJOHN</p>
<p>Filled/Checked By: XX/XX</p></td>
</tr>
<tr class="even">
<td><p>![](bcma-version-3-technical-manual-security-guide-psb-3-142/017.png)</p>
<p>*500-2564*</p></td>
</tr>
</tbody>
</table>

Example: Sample Ward Stock Bar Code Label

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Drug: BACLOFEN 10MG TABS (Qty: 1)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Dosage: 25MG</td>
<td rowspan="2"><p>Patient:</p>
<p>Ward:</p>
<p>Lot: 123141</p>
<p>Exp: 4/5/2006 Mfg: UPJOHN</p>
<p>Filled/Checked By:_______/_______</p></td>
</tr>
<tr class="even">
<td><p>![](bcma-version-3-technical-manual-security-guide-psb-3-142/018.png)</p>
<p>*500-2564*</p></td>
</tr>
</tbody>
</table>

<span id="C9_Bar_Code_Label" class="anchor"></span>Example: Sample Unit Dose Bar Code Label with HAZ Information

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>Drug: FLUOROURACIL 500MG/10ML (Qty: 1)</p>
<p>&lt;&lt;HAZ Handle&gt;&gt; &lt;&lt;HAZ Dispose&gt;&gt;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Dosage: 500MG</td>
<td rowspan="2"><p>BCMAPATIENT,ONE</p>
<p>Ward: GEN MED</p>
<p>Lot#: 123987 Exp: MAY 4,2022</p>
<p>Mfg: PHARMCO</p>
<p>Filled/Checked By: ABC/ZYX</p></td>
</tr>
<tr class="even">
<td><p>![](bcma-version-3-technical-manual-security-guide-psb-3-142/019.png)</p>
<p>*500-2564*</p></td>
</tr>
</tbody>
</table>

# Appendix C: Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="jcaho-standard-for-medication-labeling">JCAHO Standard for Medication Labeling*</h2></th>
<th>The following is an excerpt from <em>The Comprehensive Accreditation Manual for Hospitals: The Official Handbook (CAMH)</em> that lists the JCAHO standard for medication labeling. All printed medication labels must adhere to this standard.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Standard MM.4.30</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Medications are labeled.</td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><strong>Rationale for MM.4.30</strong></td>
</tr>
<tr class="even">
<td>A standardized method for labeling all medications will minimize errors.</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><strong>Elements of Performance for MM.4.30</strong></td>
</tr>
<tr class="odd">
<td><ol type="1">
<li><p>Medications are labeled in a standardized manner according to law or regulation and standards of practice.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><p>Any time one or more medications or solutions are prepared but are not administered immediately, the medication container* must be labeled.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li><p>At a minimum, all medications prepared in the hospital are labeled with the following:</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Drug name, strength, amount (if not apparent from the container)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Expiration date† when not used within 24 hours</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Expiration time when expiration occurs in less than 24 hours</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>The date prepared and the diluent for all compounded IV admixtures and parenteral nutrition solutions</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li><p>When preparing individualized medications for multiple specific patients, or when the person preparing the individualized medications is not the person administering the medication, the label also includes the following:</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Patient name</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Patient location</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Directions for use and any applicable cautionary statements either on the label or attached as an accessory label (for example, "requires refrigeration," "for IM use only")</p></li>
</ul></td>
</tr>
</tbody>
</table>

\*<u>Source</u>: Joint Commission on Accreditation of Hospital Organizations (JCAHO). (January, 2006). *The Comprehensive Accreditation Manual for Hospitals: The Official Handbook (CAMH)*  
(pp. MM-11-MM‑12). Oakbrook Terrace, Il: Joint Commission Resources, Inc. Web link:  
[<u>http://vaww.oqp.med.va.gov/oqp_services/accreditation/uploads/JCAHO2006/2006%20CAMH%20Core.pdf</u>](http://vaww.oqp.med.va.gov/oqp_services/accreditation/uploads/JCAHO2006/2006%20CAMH%20Core.pdf)