---
title: Radiology Version 5 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: active
pkg_ns: RA
patch_ver: 5
patch_id: RA*5
group_key: "RA:RA:5"
file_numbers: 
  - 2
  - 4
  - 40
  - 42
  - 44
  - 49
  - 71
  - 72
  - 74
  - 78
  - 79
  - 81
  - 200
security_keys: []
menu_options: 32
description: "<table> <caption><p>Table 1 - Summary Counts</p></caption> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 65%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong>Date</strong></th> <th><strong>Page</strong></th> <th><strong>Change</strong></th> </tr> </thead>"
audience: 
keywords: 
  - class
  - report
  - exam
  - table
  - even
  - imaging
  - contents
  - radiology
  - reports
  - added
page_count: 0
word_count: 28883
section_count: 27
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=98"
---

![](radiology-version-5-technical-manual/001.png)

RADIOLOGY/NUCLEAR MEDICINETECHNICAL MANUAL

January 2026

<span id="_Toc185253625" class="anchor"></span>Department of Veterans Affairs

Health System Design and Development

Provider Systems

This Page is intentionally left blank

Revision History

<table>
<caption><p>Table 1 - Summary Counts</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Page</strong></th>
<th><strong>Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>January 2026</td>
<td>64, 40-41</td>
<td><p>RA*5.0*226</p>
<p>Add new option ‘Activate/Inactivate Standard Procedures’ [RA PROCEDURE ACTIVATE]</p>
<p>Updated routine list: RACTCERN, RAIPS226</p></td>
</tr>
<tr class="even">
<td>May 2025</td>
<td>38, 43</td>
<td><p>RA*5.0*223</p>
<p>Add new file RADIOLOGY PROCEDURE MAP TO CC CONSULT (#71.1235)</p></td>
</tr>
<tr class="odd">
<td>January 2025</td>
<td>15,16,73</td>
<td><p>RA*5.0*220</p>
<p>Add new menu option ‘Reprocess locked study accession error’ [RA REPROC].</p>
<p>Add new option ‘Site Accession Number Set-up’ [RA SITEACCNUM] to the ‘IRM Menu’ [RA SITEMANGER]</p></td>
</tr>
<tr class="even">
<td>May 2023</td>
<td>7, 13, 32, 46, 51, 59, 61, 64, 67, 81, 84</td>
<td>Status of options impacted by patch RA*5.0*198.</td>
</tr>
<tr class="odd">
<td>January 2022</td>
<td>5-6</td>
<td><p>RA*5.0*185</p>
<p>‘Device Specifications for Imaging Locations’ [RA DEVICE] menu includes new “Alternate Request Printer” and associated parameters.</p></td>
</tr>
<tr class="even">
<td>September 2021</td>
<td>57</td>
<td><p>RA*5.0*184</p>
<p>New option ‘Inactivate a Location’ [RA SYSINACT] added to the ‘System Definition’ [RA SYSDEF] parent menu.</p></td>
</tr>
<tr class="odd">
<td>June 2021</td>
<td>31,54,55</td>
<td><p>RA*5*179</p>
<p>New option ‘Log of Discontinued Requests’ [RA ORDER DISCONTINUE] added to the ‘Menu of Request Log Options’ [RA ORDERLOG MENU]</p>
<p>New sub-menu ‘Rad/Nuc Med Report Management’ [RA REPORT MANAGEMENT] added to the ‘Supervisor Menu’ [RA SUPERVISOR]. Options to unverify/delete/restore a deleted report menus moved under this sub-menu.</p>
<p>New RA RPTMGR security key for the report manangement options. Previously locked with RA MGR and RA UNVERIFY.</p></td>
</tr>
<tr class="even">
<td>March 2021</td>
<td>43, 48, 49, 54, 74, 76, 85</td>
<td>RA*5.0*175: Clarification of the ‘Discontinued’ and ‘Cancelled’ REQUEST STATUS values. Update the menu structure of the [RA ORDER] menu and ITS new [RA ORDERLOG MENU] sub-menu.</td>
</tr>
<tr class="odd">
<td>March 2021</td>
<td>55</td>
<td><p>MAG*3.0*231</p>
<p>New ‘Radiology Study Tracker Menu’ added to the Supervisor Menu [RA SUPERVISOR].</p></td>
</tr>
<tr class="even">
<td>Feb 2021</td>
<td>44</td>
<td><p>RA*5.0*170</p>
<p>Added new filed COMMUNITY CARE JUSTIFICATIONS (#75.3)</p></td>
</tr>
<tr class="odd">
<td>Feb 2021</td>
<td>58</td>
<td><p>RA*5.0*178</p>
<p>Added new ‘Outside Location Order Suppression’ [RA SYSUPLOC] to the RA SYSDEF menu.</p></td>
</tr>
<tr class="even">
<td>July 2019</td>
<td>31, 85</td>
<td><p>RA*5.0*157</p>
<p>Added the ‘RA SWITCHLOC’ security key</p></td>
</tr>
<tr class="odd">
<td>June 2019</td>
<td>34, 42, 58</td>
<td><p>RA*5.0*158</p>
<p>VA FileMan file security update to RAD/NUC MED REASON file (#75.2)</p>
<p>Remove ‘Reason Edit’ [RA REASON EDIT] menu</p></td>
</tr>
<tr class="even">
<td>March 2019</td>
<td>36, 55, 59</td>
<td><p>RA*5*148</p>
<p>Routine List updated</p>
<p>New Radiology menu item ‘Refer Selected Requests to COMMUNITY CARE Provider [RA ORDERREF]’ added to Radiology/Nuclear Med Order Entry Menu [RA ORDER]</p></td>
</tr>
<tr class="odd">
<td>March 2019</td>
<td>52-54,62, 71</td>
<td><p>RA*5.0*153: Remove references to scaled wRVUs.</p>
<p>Change the upper file number values for Rad Nuc Med files from 79.2 to 79.7.</p></td>
</tr>
<tr class="even">
<td>August 2018</td>
<td>31, 45, 58, 85</td>
<td><p>RA*5.0*124: The reference to the RA CANCEL input template has been removed.</p>
<p>Added the ‘RA UNVERIFY’ security key.</p></td>
</tr>
<tr class="odd">
<td>June 2017</td>
<td>5, 56</td>
<td><p>RA*5*137</p>
<p>‘Device Specifications for Imaging Locations’ [RA DEVICE] menu includes new “Registered Request Printer” parameter.</p>
<p>Removed RA EXAMSTATUS MASS OVERRIDE</p></td>
</tr>
<tr class="even">
<td>March 2017</td>
<td>31, 36, 39, 41, 46, 47, 55, 91</td>
<td><p>RA*5*127</p>
<p>Added RADNTRT to the Mail Group section.</p>
<p>Added routines to the Routine List section for the NDS Radiology Reports patch.</p>
<p>Amended file #71 to state there are four new fields incorporated within the file for interoperability purposes</p>
<p>Added new files #71.11, #71.98, and #71.99 and their related information</p>
<p>Added RA PRO MAP template to the templates section.</p>
<p>Ammended the RA PROCEDURE EDIT template to state that there is a section to assocaite a “DETAILED” Type procedure with a cpt code to the MRPF.</p>
<p>Ammended the RA SUPERVISOR MENU option to include the new options: RALOINC ENTER, RA MAP TO MRPF, RA MAP ONE, and RA SEEDING DONE.</p>
<p>Added RA*5.0*127 patch description</p></td>
</tr>
<tr class="odd">
<td>December 2016</td>
<td>58,61</td>
<td><p>RA*5*133</p>
<p>‘Radiology/Nuclear Med Order Entry Menu’ [RA ORDER] includes new ‘Update a Hold Request’ [RA ORDERREASON UPDATE]</p></td>
</tr>
<tr class="even">
<td>November 2013</td>
<td>19, 34, 36-37, 52, 53, 87</td>
<td><p>RA*5*113</p>
<p>Definition of ^RAD global Radiation Absorbed Dose file (#70.3)</p>
<p>VA FileMan File Protection on Radiation Absorbed Dose file (#70.3)</p>
<p>Routine List included; shows core Radiology routines (compiled routines may differ from site to site)</p>
<p>Special Reports’ [RA SPECRPTS] Menu update: includes new ‘Radiation Dose Summary Report’ [RA RAD DOSE SUMMARY] menu item</p>
<p>‘Patient Profile Menu’ [RA PROFILES] includes new Exam Profile with Radiation Dosage Data [RA PROFRAD DOSE] menu item.</p>
<p>Software / Documentation Notes and Patch descriptions</p></td>
</tr>
<tr class="odd">
<td>September 2013</td>
<td>43, 71</td>
<td><ul>
<li><p>RA*5*97: Added BI-RADS and AAA codes to DIAGNOSTIC CODES file (#78.3)</p></li>
<li><p>RA*5*97: Added definition for Abdominal Aortic Aneurysm (AAA)</p></li>
</ul>
<p>RA*5*97: Added definition for Breast Imaging Reporting and Data System (BI-RADS<sup>™</sup>)</p></td>
</tr>
<tr class="even">
<td>August 2011</td>
<td>13, 34, 51, 65, Glossary</td>
<td><p>Patch RA*5.0*47:</p>
<ul>
<li><blockquote>
<p>Added a new option to turn on the site-specific accession number: Site Accession Number Set-up.</p>
</blockquote></li>
<li><blockquote>
<p>Replaced the example with an updated version.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the names of the Rad/Nuc Med HL7 manuals.</p>
</blockquote></li>
<li><blockquote>
<p>Added a new option to the IRM Menu [RA SITEMANAGER]:<br />
Site Accession Number Set-up.</p>
</blockquote></li>
<li><blockquote>
<p>Added four new protocols:<br />
RA CANCEL 2.4<br />
RA EXAMINED 2.4<br />
RA REG 2.4<br />
RA RPT 2.4</p>
</blockquote></li>
<li><p>Added Site Specific Accession Number (SSAN) to the Glossary.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>February 2010</td>
<td>15</td>
<td><p>RA*5*99:</p>
<ul>
<li><p>Updated the section heading to reflect change in reporting periods; "Schedule Perf. Indic. Summary for Fifteenth of Month Following the Quarter End."</p></li>
<li><p>Updated “RA PERFORMIN SCHEDULE” to run quarterly vs. monthly.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>May 2009</td>
<td>1, 32, 32, 69, 71</td>
<td><ul>
<li><p>RA*5*78: Added a phrase to the description of the interface in the Introduction</p></li>
<li><p>RA*5*78: Added the new mail group name and description, RAD HL7 MESSAGE</p></li>
<li><p>RA*5*78 :Added information about querying the VistA Radiology application for results</p></li>
<li><p>RA*5*78: Updated the screen capture of the DBIAs section</p></li>
<li><p>RA*5*78: Changed UCI to development environment in the note regarding XINDEX</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>July 2008</td>
<td>52, 71, 84</td>
<td><ul>
<li><p>RA*5*56: Added new option, Outside Report Entry/Edit.</p></li>
<li><p>RA*5*56: Added a new option, Restore a Deleted Report.</p></li>
<li><p>RA*5*56: Added a definition for the ‘Deleted’ status.</p></li>
<li><p>RA*5*56: Added a definition for the ‘Electronically Filed’ status.</p></li>
<li><p>RA*5*56: Added two new valid report statuses to the definition.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>June 2008</td>
<td>63</td>
<td>RA*5*84: Added four new protocols</td>
</tr>
<tr class="odd">
<td>September 2007</td>
<td>56</td>
<td>RA*5*80: Added new option to RA HL7 MENU.</td>
</tr>
<tr class="even">
<td>June 2007</td>
<td><a href="#_Ref163373573">35</a>, 36, 46, 56</td>
<td><ul>
<li><p>Updated sections to reflect current functionality. (These updates are not associated with any particular patch.)</p></li>
<li><p>RA*5*81: Added file #79.7 to VA FileMan File Protection list.</p></li>
<li><p>RA*5*81: Added file #79.7 to the detailed list of files.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>February 2007</td>
<td>19, Glossary</td>
<td><ul>
<li><p>RA*5*79: Added file to RA Global</p></li>
<li><p>RA*5*79: Added new file - #73.2 Radiology CPT By Procedure Type.</p></li>
<li><p>RA*5*79: Updated glossary entry for Procedure Type.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>July 2006</td>
<td>51, 53, 54, Glossary</td>
<td><ul>
<li><p>RA*5*64: Added scaling factor description to File #79.2.</p></li>
<li><p>RA*5*64: Added five reports to [RA WKL] menu: Physician CPT Report by I-Type, and four Physician wRVU reports.</p></li>
<li><p>RA*5*64: Added two Procedure wRVU reports to [RA SPECRPTS] menu.</p></li>
<li><p>RA*5*64: Added glossary entries for RVU, wRVU.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>April 2006</td>
<td>54</td>
<td>RA*5*67: Renamed Performance Indicator menu to Timeliness Reports. Added Outpatient Procedure Wait Time menu and report to Timeliness Reports menu. Renamed Performance Indicator reports to Verification Timeliness reports (menu options unchanged).</td>
</tr>
<tr class="even">
<td>March 2006</td>
<td><a href="#_Ref220156552">20</a>, Glossary</td>
<td><ul>
<li><p>RA*5*57: Added Key Variable RACCOUNT.</p></li>
<li><p>RA*5*57: Added glossary entries for PFSS, PFSS Account Reference, and PFSS Department Code.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>August 2005</td>
<td>6</td>
<td><ul>
<li><p>Miscellaneous formatting corrections throughout</p></li>
<li><p>RA*5*41: Text was deleted - On the Rad/Nuc Med patient file (#70), the activity log, clinical history, and exam status times are deleted. The entire request entry in the Rad/Nuc Med Orders file (#75.1) is deleted.</p></li>
<li><p>RA*5*41: Text deletion. – Item 5 - Order data (ORDER DATA CUT-OFF). Purges the record (entire procedure request) from File (#75.1)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>August 2005</td>
<td>8, 9, 12, 10</td>
<td><ul>
<li><p>RA*5*41: The following text was deleted - The default number of days for the Order Data Cut-Off is 90 and, if changed, must be a whole number between 30 and 99999. The orders which will be purged include those whose last activity date is greater than the number of default days and whose order status is Discontinued, Hold, Complete, or Pending. Order purges can also be initiated by OE/RR.</p></li>
<li><p>RA*5*41: Additional text description - This number should 0, as the option no longer allows purging of orders.</p></li>
<li><p>RA*5*41: Text change and deletion - ^RAO - …but not data from ^RAO (order data) - …order data and changed 5 items to 4.</p></li>
<li><p>RA*5*41: Deletion of prompt and response " ORDER DATA CUT-OFF: 90// 99999".</p></li>
<li><p>RA*5*41: Deleted O - Orders only and A - All three.</p></li>
<li><p>RA*5*41: Purging orders/requests was deleted.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>May 2005</td>
<td>31, 34, 57, 57, 68, 70, 71, Glossary</td>
<td><ul>
<li><p>RA*5.0*45: Reference to template compilation option has been updated to state that different sites may have different templates compiled.</p></li>
<li><p>RA*5.0*45: Reference to non-existent HL7 specific appendices in the Technical Manual removed. HL7 specific documents have been created to: 1) describe interfaces with COTS applications 2) general HL7 message definition</p></li>
<li><p>RA*5.0*45: The Procedure File Listings menu has two new items; ‘RA CMAUDIT HISTORY’ &amp; RA PROCMEDIA</p></li>
<li><p>RA*5*45: Included the CPT MODIFIER (#81.3) file in the External Relations section.</p></li>
<li><p>RA*5.0*45 changed the screen capture; the Version label erroneously displayed the version of the application as being 4.5, not version 5.</p></li>
<li><p>RA*5.0*45: Removed all references to %INDEX, issues with using XINDEX regarding RAUTL8 have been addressed by the Kernel development team.</p></li>
<li><p>RA*5.0*45: Updated definition of AMIS code. Removed references to contrast media.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>January 2004</td>
<td>30</td>
<td>RA*5*44: Added Schedule Perf. Indic. Summary for the fifteenth of the month.</td>
</tr>
<tr class="odd">
<td>May 2003</td>
<td>8, 10, 54</td>
<td><ul>
<li><p>RA*5*34: Changed 9999 to 99999</p></li>
<li><p>RA*5*34: Replaced example</p></li>
<li><p>RA*5*34: Added data recovery text</p></li>
<li><p>RA*5*37: Added RAD PERFORMANCE INDICATOR mail group.</p></li>
<li><p>RA*5*37: Performance Indicator Menu Options added</p></li>
</ul></td>
</tr>
<tr class="even">
<td>December 2002</td>
<td>59</td>
<td>RA*5*35: Added new option to the User Utility Menu – Set preference for Long Display of Procedures [RA SET PREFERENCE LONG DISPLAY]</td>
</tr>
<tr class="odd">
<td>September 2002</td>
<td>12, 49, 57, 58</td>
<td><ul>
<li><p>RA*5*31: Added new option - Credit Completed Exams for an Imaging Location</p></li>
<li><p>RA*5*31: Added new option to Exported Menus</p></li>
<li><p>RA*5*31: Added new option to [RA OVERALL]</p></li>
<li><p>RA*5*31: Added new option to [RA OVERALL]</p></li>
</ul></td>
</tr>
<tr class="even">
<td>July 2002</td>
<td>52, 51</td>
<td><ul>
<li><p>RA*5*25: Added Radiology HL7 Menu</p></li>
<li><p>RA*5*25: A number of new protocols added</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>April 2002</td>
<td>7, TOC</td>
<td><ul>
<li><p>RA*5*27: Added the word Additional to the Clinical</p></li>
<li><p>istory subfile from File (#74)</p></li>
<li><p>RA*5*27: Updated Table of Contents</p></li>
</ul></td>
</tr>
</tbody>
</table>

Table 1 - Summary Counts

Table of Contents

![](radiology-version-5-technical-manual/002.png)[Credit completed exams for an Imaging Location [15](#credit-completed-exams-for-an-imaging-location)](#credit-completed-exams-for-an-imaging-location)

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [# Implementation](#implementation)
  - [Implementation of a Virgin Installation](#implementation-of-a-virgin-installation)
  - [Implementation of an Installation over V. 4.5](#implementation-of-an-installation-over-v-45)
  - [Informational Messages](#informational-messages)
- [# Maintenance](#maintenance)
  - [Imaging Type Mismatch Report](#imaging-type-mismatch-report)
  - [IRM Menu](#irm-menu)
    - [Device Specifications for Imaging Locations](#device-specifications-for-imaging-locations)
    - [Distribution Queue Purge](#distribution-queue-purge)
    - [Failsoft Parameters](#failsoft-parameters)
    - [Imaging Type Activity Log](#imaging-type-activity-log)
    - [Purge Data Function](#purge-data-function)
    - [Rebuild Distribution Queues](#rebuild-distribution-queues)
    - [Report File x-ref Clean-up Utility [^16]](#report-file-x-ref-clean-up-utility-16)
    - [Site Accession Number Set-up [^17]](#site-accession-number-set-up-17)
    - [Credit completed exams for an Imaging Location [^19]](#credit-completed-exams-for-an-imaging-location-19)
    - [Enable HL7 reprocessing for locked studies](#enable-hl7-reprocessing-for-locked-studies)
    - [Resource Device Specifications for Division](#resource-device-specifications-for-division)
    - [Schedule Perf. Indic. Summary for Fifteenth of Month [^20]Following the Quarter End [^21]](#schedule-perf-indic-summary-for-fifteenth-of-month-20following-the-quarter-end-21)
    - [Template Compilation](#template-compilation)
- [# Globals](#globals)
- [Key Variables](#key-variables)
  - [Function](#function)
  - [Bulletins](#bulletins)
  - [Mail Groups](#mail-groups)
- [# Security](#security)
  - [Keys](#keys)
    - [RA ALLOC](#ra-alloc)
    - [RA MGR](#ra-mgr)
    - [RA VERIFY](#ra-verify)
    - [RA RPTMGR](#ra-rptmgr)
    - [RA SWITCHLOC](#ra-switchloc)
  - [Sign-on Security](#sign-on-security)
  - [Electronic Signature [^26]](#electronic-signature-26)
    - [VistA Options](#vista-options)
    - [COTS HL7 Interfaces](#cots-hl7-interfaces)
  - [VA FileMan File Protection](#va-fileman-file-protection)
  - [Legal Requirements](#legal-requirements)
- [# Routine List](#routine-list)
- [File List](#file-list)
  - [Templates](#templates)
    - [Input Templates](#input-templates)
    - [Sort Templates](#sort-templates)
    - [Print Templates](#print-templates)
    - [List Templates](#list-templates)
- [# Exported Options](#exported-options)
  - [Exported Menus](#exported-menus)
    - [IRM Menu \[RA SITEMANAGER\]](#irm-menu-ra-sitemanager)
    - [Rad/Nuc Med Total System Menu \[RA OVERALL\]](#radnuc-med-total-system-menu-ra-overall)
    - [Rad/Nuc Med Clerk Menu \[RA CLERKMENU\]](#radnuc-med-clerk-menu-ra-clerkmenu)
    - [Rad/Nuc Med Ward Clerk Menu \[RA WARD\]](#radnuc-med-ward-clerk-menu-ra-ward)
    - [Rad/Nuc Med File Room Clerk Menu \[RA FILERM\]](#radnuc-med-file-room-clerk-menu-ra-filerm)
    - [Interpreting Physician Menu \[RA RADIOLOGIST\]](#interpreting-physician-menu-ra-radiologist)
    - [Reports Menu \[RA REPORTS\]](#reports-menu-ra-reports)
    - [Rad/Nuc Med Secretary Menu \[RA SECRETARY\]](#radnuc-med-secretary-menu-ra-secretary)
    - [Rad/Nuc Med Technologist Menu \[RA TECHMENU\]](#radnuc-med-technologist-menu-ra-techmenu)
    - [Rad/Nuc Med Transcriptionist Menu \[RA TRANSCRIPTIONIST\]](#radnuc-med-transcriptionist-menu-ra-transcriptionist)
  - [Single Options](#single-options)
  - [Menu/Option Assignment](#menuoption-assignment)
  - [Protocols [^56]](#protocols-56)
  - [FileMan Options](#fileman-options)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
  - [DBIAs](#dbias)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
  - [Build File Print](#build-file-print)
  - [Question Marks](#question-marks)
  - [XINDEX](#xindex)
  - [Inquire to File Entries](#inquire-to-file-entries)
  - [Print Options File](#print-options-file)
  - [List File Attributes](#list-file-attributes)
- [Glossary](#glossary)
- [SOFTWARE AND DOCUMENTATION NOTES](#software-and-documentation-notes)
The Radiology/Nuclear Medicine package is a comprehensive software package designed to assist with the functions related to processing patients for imaging examinations.
The package automates a range of Radiology/Nuclear Medicine functions, including order entry of requests for exams by clinical staff, registration of patients for exams, processing of exams, recording reports/results, verification of reports on-line, displaying/printing results for clinical staff, automatic tracking of requests/exams/reports, and generation of management statistics/reports, both recurring and ad hoc.
The package automates many tedious tasks providing faster, more efficient and accurate data entry and more timely results reporting.
The package interfaces with the Record Tracking package for the purpose of tracking Radiology/Nuclear Medicine records and creating pull lists for those records needed for scheduled clinic appointments.
- It interfaces with and through the Health Level Seven (HL7) package for the exchange of exam and report information with other VistA applications as well as Commercial Off The Shelf (COTS) applications.[^1]
- It interfaces with the Health Summary package to allow users to see patient histories and test results which may influence the nature of the examination.
- It interfaces with the Computerized Patient Record System (CPRS) package to allow requesting of exams and viewing of reports.
- It interfaces with the Adverse Reaction Tracking (ART) package for the exchange of data concerning a patient's allergies.
- It interfaces with Patient Care Encounter (PCE) for crediting outpatient imaging procedures.
- It also interfaces with the AMIE package to display exam results.

# # Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation of a Virgin Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter at least one division into the Rad/Nuc Med Division file \#79 to activate the system. The division can be further defined by the ADPAC.

Give the ADPAC access to at least one Imaging Location (field \#74) in the New Person file (#200). Without this, no one will be able to sign onto the system. Once the ADPAC has access, s/he must give each package user (technologist, interpreting resident physician, interpreting staff physician, or clerk) location access so they can sign on. The ADPAC can give users access with the Classification Enter/Edit \[RA PNLCLASS\] option. Without an assigned imaging location, a user simply cannot access the package.

Along with the ADPAC, determine the devices needed for each Imaging Location that will be defined. Use the option Device Specifications for Imaging Locations \[RA DEVICE\] in the IRM Menu \[RA SITEMANAGER\] to assign them.

Associate an existing or new mail group with each of the exported bulletins (see page 32) so users can receive these Radiology/Nuclear Medicine messages. The bulletins are generated when an important action has taken place, such as the deletion of a report. Consult with the package ADPAC to determine how many mail groups to create, what mail group(s) to associate with each bulletin and who should be the mail group coordinator. It is strongly recommended that a mail group with the ADPAC and possibly an IRM support person as recipients be established and associated with the RAD/NUC MED CREDIT FAILURE bulletin. This is the only way users can be notified of credit failure due to lack of data or wrong data in Radiology/Nuclear Medicine.

Verifying reports [^2]  
VistA reports: Give the RA VERIFY key to staff that will be verifying reports and make sure they have an electronic signature.

COTS Voice Recognition Systems: In addition to the above, assign verifying privileges to staff that will be verifying reports on a COTS Voice Recognition system. Also, assign an ID to each physician that matches his/her IEN in the New Person file \#200.

The IRM Menu \[RA SITEMANAGER\] and the standalone option Imaging Type Mismatch Report \[RA EXAM/STATUS ITYPE\] covered in this chapter will help with the continued maintenance of the software. Further implementation and maintenance can be done by the ADPAC and is described in full in the *Radiology/Nuclear Medicine ADPAC Guide*.

## Implementation of an Installation over V. 4.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verifying reports [^3]  
    VistA reports: Give the RA VERIFY key to staff that will be verifying reports and make sure they have an electronic signature.  
    COTS Voice Recognition Systems: In addition to the above, assign verifying privileges to staff that will be verifying reports on a COTS Voice Recognition system. Also, assign an ID to each physician that matches his/her IEN in the New Person file \#200.
2.  The burden of Implementation falls mainly on the ADPAC and is fully discussed in the *ADPAC Guide* with a checklist of steps to use in the implementation process.

## Informational Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two main messages that users may receive that concern IRM particularly during implementation after a virgin installation:

3.  Radiology/Nuclear Medicine Division definition error. Call your site manager.  
    When a user calls about this message, it means there is insufficient information in the imaging location that was selected by the user. Make sure the ADPAC has assigned that location to a division in the Division Parameter Set-up option Rad/Nuc Med Division file (#79), field \#50.
1.  No default "ABC" printer has been assigned. Contact IRM.  
    This message appears when the ADPAC is editing an imaging location in the Location Parameter Set-up option and as yet, a printer has not been assigned for that activity (jacket labels, flash cards, or exam labels). Use the option Device Specifications for Imaging Locations \[RA DEVICE\] to assign them.

# # Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information throughout this manual is meant to help IRM in the maintenance of the software. The discussion that follows here covers the options available to assist IRM in that maintenance.

## Imaging Type Mismatch Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA EXAM/STATUS ITYPE\]

This option is not assigned to any menu. It generates a report listing each case where the imaging type of the visit does not match the imaging type of the current exam status. These cases should be edited to Complete as soon as possible to correct the exam status. This mismatch condition may have happened around the time a previous version was installed, but new mismatches should not occur.

The report requires 132 column output and displays the patient name, SSN, exam date/time, case number, imaging type of the visit, exam status and imaging type of the exam status for each discrepancy. Radiology/Nuclear Medicine personnel can use the case edit options to move these exams to a Complete status which automatically resolves the mismatch.

## IRM Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA SITEMANAGER\]

### Device Specifications for Imaging Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA DEVICE\]

This function allows you to assign device names for printers to which the software will direct various outputs. Each imaging location can be assigned its own set of printers.

When a user signs on the system and tries to access the module, the first action by the module will be to determine which division and location with which the user is associated. During the entire session, the system automatically uses the parameters that the coordinator has specified for that division and location. For example, the user need never be asked how many flash cards to print or what flash card format if the parameters contain that information.

Once parameters are entered for default printers (flash card, jacket label, radio-pharmaceutical dose ticket, report, request and request cancellation) and the printer names have been assigned to the location, output is automatically routed to these devices.

If a default printer is not entered, the user will be prompted to select a printer at the time they initially access the Radiology/Nuclear Medicine package. If a default printer is not selected at the time of initial access to the package, the user will be prompted for a printer each time they elect to print a flash card, jacket label, request, or report.

> **NOTE:** When an exam is requested via the Request an Exam option, the prompt, "Submit Request To:" is screened. Therefore, if a Request Printer is malfunctioning, it will have to be changed for that location until the printer is fixed. This is an option that you may wish to assign to the package ADPAC.

One of the new fields, Dosage Ticket Printer, only appears if the Imaging Location you select is an Imaging Type of Nuclear Medicine or Cardiology Studies.

The option requests the Imaging Location name, and then default printer names for:

- Flash Cards
- Jacket Labels
- Requests
- Reports
- Dosage Tickets
- Cancelled Requests
- Registered Request Printer
- Alternate Request Printer

> The Alternate Request Printer has additional parameters associated with it. These parameters are as follows:

ALTERNATE PRINTER USAGE – This parameter designates how the alternate request printer will be used. It is a set of codes: 1:After Hours Printer or 2:Alternate Printer

AFTER HOURS BEGIN TIME - This is the time of day that radiology requests will be routed to the alternate request printer you selected (i.e., 7:00PM)

AFTER HOURS END TIME - This is the time of day that radiology requests will revert to printing to your normal default request printer.(i.e., 7:00AM)

AFTER HOURS WEEKEND - This parameter allows the user to define weekends (Saturday/Sunday) as after hours. If set to YES, all requests will be routed to the alternate printer for the duration of the weekend.

AFTER HOURS HOLIDAY - This parameter allows the user to define holidays as after hours. If set to YES, all requests will be routed to the alternate printer on that day. \*\*\*Note that this parameter relies on the HOLIDAY file (#40.5) being populated correctly with the Federal holidays.\*\*\*

ARP CATEGORY OF EXAM - This allows you to send ONLY outpatient or inpatient requests to the alternate printer (all other categories would print to the original request printer), or ALL exam categories (INP/OPT etc) to the after hours printer during the specified time frame.

ALTERNATE PRT REQUESTING LOC – This parameter can be used to identify requesting locations that will cause the request to be routed to the alternate request printer. This parameter <u>cannot</u> be used in conjunction with the after hours parameters.

### Distribution Queue Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA RPTDISTPURGE\]

The Distribution Queue Purge option allows you to purge the distribution files. This can be done to eliminate old reports that have already been printed or reprinted.

The information purged includes the Activity Log in the Reports Distribution Queue file (#74.3) and the reports in the Report Distribution file (#74.4).

You are prompted for a purge date and a device. Any reports printed prior to that specified date are purged from the distribution files.

A mail message will be sent to you with the results of the purge which includes the date/time the purge begins and ends.

Subj: Distribution Queue Purge \[#12256\] 09 Feb 97 11:34 4 Lines

From: Radiology Package in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------

Purge distribution files of reports printed before JAN 1,1997

Distribution files purge process begun at FEB 9,1997 11:34

Distribution files purge process completed at FEB 9,1997 11:34

> **NOTE:** Occasionally, a facility has kept the Distribution Queues active, but reports have not been printed for a long time causing a high volume of unprinted reports to sit in the queue. This purge option is not designed to purge unprinted reports. To delete unprinted, historical reports that you do not want to print from the queues, use the Rebuild Distribution Queues \[RA RPTDISTREBUILD\] option. Rebuilding also supports populating the queues with reports verified on or after a date, you choose.

### Failsoft Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA FAILSOFT\]

The Failsoft Parameters option allows you to specify the Operating Conditions parameter. This feature will be obsolete in the future. It previously ignored imaging location devices if in emergency mode, but it no longer completely supports that.

### Imaging Type Activity Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA IMGLOG\]

The Imaging Type Activity Log option enables you to acquire a hardcopy log of certain activities.

The log includes the following information by Imaging Type: the date on which the activity occurred, the type of activity, the user who initiated the activity, the number of exams affected (if any) and the number of reports affected (if any).

The types of activities listed are:

- Changes in imaging type parameters
- Scheduled data purges
- Completion of data purges
- Modification of on-line data criteria (changes made through the Purge Data Function option)

### Purge Data Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA PURGE\]

RA\*5.0\*198 set out of order both the ‘Purge Data Function’ \[RA PURGE\] & ‘Indicate No Purging of an Exam/report’ \[RA PURGE\] options. The information for the RA PURGE option has been retained for historical reference.

The Purge Data Function option enables you to purge specific data from the system without affecting the integrity of the patient records.[^4] The data purge deletes the report text, clinical history, and activity log entries from the Rad/Nuc Med Report file \#74. However, if the report was amended, nothing is deleted.[^5]

You must enter cut off dates (or accept the default) for the following types of data which may be purged using this option:

1.  Activity logs (ACTIVITY LOG CUT-OFF)  
    Purges the ACTIVITY LOG subfile from File \#74  
    and Purges the ACTIVITY LOG subfile from File \#70
2.  Reports (REPORT CUT-OFF)  
    Purges the REPORT TEXT (not the impressions) subfile from File \# 74
3.  Clinical histories (CLINICAL HISTORY CUT-OFF)  
    Purges the ADDITIONAL CLINICAL HISTORY [^6] subfile from File \#74  
    and  
    Purges the CLINICAL HISTORY FOR EXAM subfile from File \#70
4.  Status tracking times (TRACKING TIME CUT-OFF)  
    Purges the EXAM STATUS TIMES subfile from File \#70

[^7]At each prompt concerning one of the above data types, you will be setting the imaging type parameter for the number of days to keep the various activity logs on-line. The number of days for each should be determined by the coordinator and the IRM site manager.

The number of days must be a whole number between 90 and 99999 [^8] for Activity Logs, Report, Clinical History, and Tracking Time. The report impressions will remain on-line even after purging.[^9]

This operation should be run during off-hours. A system backup should be completed prior to execution of the purge routine.

Output [^10]

The output will include the date/time the purge starts and finishes, and all purge statistics compiled for records processed, reports processed and requests processed. Entries are made to the imaging type activity log showing any changes to on-line criteria, purge routine scheduling, and a record of completion.

The following describes how to interpret the summary counts in the output.

<table>
<caption><p>Table 2 - Globals</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Count</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PURGE COUNTS</td>
<td>COUNT EVEN IF ONLY 1 OF 3 IS WITHIN CUT-OFF DAYS</td>
</tr>
<tr class="even">
<td>No. of exam records processed</td>
<td>ACTIVITY LOG CUT-OFF<br />
and/or<br />
CLINICAL HISTORY CUT-OFF<br />
and/or<br />
TRACKING TIME CUT-OFF</td>
</tr>
<tr class="odd">
<td>No. of reports processed</td>
<td>ACTIVITY LOG CUT-OFF<br />
and/or<br />
CLINICAL HISTORY CUT-OFF<br />
and/or<br />
REPORT CUT-OFF</td>
</tr>
<tr class="even">
<td></td>
<td>Count only if order was purged within cut-off day<br />
AND other criteria</td>
</tr>
<tr class="odd">
<td>No. of requests processed</td>
<td><p>ORDER DATA CUT-OFF</p>
<p>This number should be 0, as the option no longer allows purging of orders.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch RA*5*41 August 2005: Additional text description – “This number should be 0, …”.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Table 2 - Globals

By purging information that is unnecessary for the maintenance of the system and associated patient records, you will extend your disk space and possibly speed up processing time.

> **NOTE:** Be sure to do a system backup before you choose to purge data.

The following is an example:

Select IRM Menu Option: Purge Data Function [^11]

+--------------------------------------------------------+

\| This option is used to remove data from one or all of \|

\| these globals: ^RADPT, ^RARPT[^12] \|

\| \|

\| Make sure IRM keeps the backup that was made prior to \|

\| running this option, and NOT overwrite that backup for \|

\| at least 6 months. Data from ^RADPT and ^RARPT can be \|

\| recovered. \|

\| \|

\| The cut-off dates for the 4 items (activity log, \|

\| report, clinical history, tracking time) \|

\| are compared to the exam date of those items. If the \|

\| exam date for an item is older than the cut-off date \|

\| for that item, then that item would be purged. \|

+--------------------------------------------------------+

Do you want to edit the Imaging Type purge parameters? Yes// \<RET\>

Select IMAGING TYPE: ULTRASOUND

Please indicate how many days each type of data should remain on-line:

----------------------------------------------------------------------

ACTIVITY LOG CUT-OFF: 90// ?

Enter a number between 90 and 99999, to indicate the number of

days to keep the various activity logs on-line.

ACTIVITY LOG CUT-OFF: 90// 99999

REPORT CUT-OFF: 90// 99999

CLINICAL HISTORY CUT-OFF: 90// 99999

TRACKING TIME CUT-OFF: 90// 99999

Select IMAGING TYPE:

Do you wish to schedule the data purge? No// YES

Select one of the following:

[^13] E Exams only

R Reports only

B Both exams & reports

Enter type of data to purge: Reports only// Both exams & reports

IMAGING TYPES

-------------

1\) ANGIO/NEURO/INTERVENTIONAL

2\) CARDIOLOGY STUDIES (NUC MED)

3\) CT SCAN

4\) GENERAL RADIOLOGY

5\) MAGNETIC RESONANCE IMAGING

6\) MAMMOGRAPHY

7\) NUCLEAR MEDICINE

8\) ULTRASOUND

9\) VASCULAR LAB

Select Imaging Type(s) to Purge: (1-9): 8

Do you wish to re-purge records that have been purged in the past? No// \<RET\>

You have chosen to purge Exam & Report records from ULTRASOUND

Do you wish to proceed with the purge? No// YES

DEVICE: HOME// QUEUE TO PRINT ON

DEVICE: HOME// printer name

Requested Start Time: NOW// \<RET\>

Request Queued. Task \#: 10157

Purge data routine started at MAR 1,1997 01:05.

Purging exams/reports.[^14]

Data purge completed at MAR 1,1997 01:18.

The following purge statistics were compiled:

No. of exam records processed : 863

No. of reports processed : 620

No. of requests processed : 796

If purged data needs to be recovered, IRM can start the data recovery by running routine RARECOV from the backup volume, and later the RARESTOR routine from production.

There are no options assigned to this recovery operation.

The instructions for recovering purged data are displayed when routine RARECOV is run.[^15]

The following is an example from the backup volume.

D ^RARECOV

Instructions for recovering purged exam and/or report data

Step 0.

Find out:

1 - the DATE that the purge was done

2 - how many DAYS back from that date was used as cut-off

i.e., what was entered as "ddd" in "T-ddd" ?

Step 1. From the Backup Volume:

D ^RARECOV

enter cut-off dates that you had used in the purge function

Step 2. From the Backup Volume:

D ^%GTO (or your system's global copy out utility)

enter output file name

enter ^XTMP("RARECOV"

Step 3. From the Production volume that holds ^XTMP:

D ^%GTI (or your system's global restore utility)

enter the file name from step 2

Step 4. From the Production volume:

D ^RARESTOR

routine will automatically read from ^XTMP("RARECOV"

and copy data back into ^RADPT and/or ^RARPT

IMAGING TYPES

-------------

1\) ANGIO/NEURO/INTERVENTIONAL

2\) CARDIOLOGY STUDIES (NUC MED)

3\) CT SCAN

4\) GENERAL RADIOLOGY

5\) MAGNETIC RESONANCE IMAGING

6\) MAMMOGRAPHY

7\) NUCLEAR MEDICINE

8\) ULTRASOUND

9\) VASCULAR LAB

Select Imaging Type(s) to recover purged data: (1-9): 9

Select one of the following:

E Exam data

R Report data

B Both

Enter type of data to recover: Report data// EXAM Exam data

Cut-off Date Selection \*\*\*\* VASCULAR LAB \*\*\*\*

Enter date that the Radiology Purge was done : 3/1/02 (MAR 01, 2002)

Enter number of days subtracted from that date as cut-off : 90

The default value can be changed as needed.

Cut-off Date for ACTIVITY LOG CUT-OFF : DEC 01, 2001// \<RET\>

Cut-off Date for REPORT CUT-OFF : DEC 01, 2001// \<RET\>

Cut-off Date for CLINICAL HISTORY CUT-OFF : DEC 01, 2001// \<RET\>

Cut-off Date for TRACKING TIME CUT-OFF : DEC 01, 2001// \<RET\>

Do you want to proceed ? NO// \<RET\>

-- Nothing Done --

### Rebuild Distribution Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA RPTDISTREBUILD\]

The Rebuild Distribution Queue option allows you to rebuild distribution files with reports verified on or after a selected date.

Rebuilding the distribution queues allows the user to reprint reports that have been printed through the Distribution Queue Menu and then purged through the Distribution Queue Purge option. This might be necessary if the original reports were misplaced, if a printer has jammed, etc.

This option can also be used if a facility which has not been using Distribution Queues wants to clean out the queues completely and rebuild with only the reports verified after a chosen date. In this way, the queues can be cleared without printing any reports.

Depending on the category of the report and the requirements of the distribution queue, there will be an entry made in the Report Distribution file (#74.4) for each report and the corresponding queue. In other words, if a report has a category of Outpatient and both the Clinic Reports Queue and the File Room Queue include outpatient reports, two entries will be made in the Report Distribution file (#74.4).

The output from this option will show the number of reports used to rebuild the distribution files.

This report should be queued to a printer.

### Report File x-ref Clean-up Utility [^16]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA XREF CLEANUP\]

This option can be used to clean-up left-over "ASTF" and "ARES" x-refs from the RAD/NUC MED REPORTS file (#74). It will list and optionally delete the left-over "ASTF" and "ARES" cross-references.

This option is locked by the RA MGR key.

Here is an example:

RAD/NUC MED UTILITY TO LIST/DELETE LEFT-OVER REPORT X-REFS

Do you want to print a list of left-over x-refs?? YES// \<RET\>

Select Device: HOME// \<RET\> TELNET Right Margin: 80// \<RET\>

LEFT-OVER ^RARPT("ARES") X-REFS

===============================

RESIDENT PHYSICIAN CASE \# OF LEFT-OVER X-REF

------------------ -------------------------

RAPROVIDER, ONE Unknown report \#99999992

LEFT-OVER ^RARPT("ASTF") X-REFS

===============================

STAFF PHYSICIAN CASE \# OF LEFT-OVER X-REF

--------------- -------------------------

RAPROVIDER, TWO Unknown report \#7852353

Do you want to clean up these 2 left-over x-refs?? NO// YES

^RARPT("ARES",4570,99999992) deleted

^RARPT("ASTF",6738,7852353) deleted

Press RETURN to continue...

Select IRM Menu Option: Report File x-ref Clean-up Utility

RAD/NUC MED UTILITY TO LIST/DELETE LEFT-OVER REPORT X-REFS

Do you want to print a list of left-over x-refs?? YES// \<RET\>

Select Device: HOME// \<RET\> TELNET Right Margin: 80// \<RET\>

LEFT-OVER ^RARPT("ARES") X-REFS

===============================

RESIDENT PHYSICIAN CASE \# OF LEFT-OVER X-REF

------------------ -------------------------

\< There are no left-over "ARES" x-refs found. \>

LEFT-OVER ^RARPT("ASTF") X-REFS

===============================

STAFF PHYSICIAN CASE \# OF LEFT-OVER X-REF

--------------- -------------------------

\< There are no left-over "ASTF" x-refs found. \>

Press RETURN to continue.. \<RET\>.

### Site Accession Number Set-up [^17] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA SITEACCNUM\]

This option is used to turn on use of the Site Specific Accession Number when registering new cases in the Radiology/Nuc Med package for the facility selected.

The user is asked to select a facility and then is allowed to edit the “USE SITE ACCESSION NUMBER?” division parameter for the selected facility. Until this field is set to ‘YES,’ the system will not use the Site Specific Accession Number during registration of a new case.

Only when all devices are able to handle the Site Specific Accession Number, should this field be set to ‘YES’, at which point the system will begin to use the Site Specific Accession Number.

Here is an example:

Select OPTION NAME: RA SITEMANAGER IRM Menu

Device Specifications for Imaging Locations

Distribution Queue Purge

Failsoft Parameters

Imaging Type Activity Log

Rebuild Distribution Queues

Report File x-ref Clean-up Utility

Site Accession Number Set-up

Credit completed exams for an Imaging Location

Resource Device Specifications for Division

Schedule Perf. Indic. Summary for 15th of month

Template Compilation

Select IRM Menu Option: Site Accession Number Set-up

> **WARNING:** Turning on the Site Specific Accession Number should only

be done in conjunction with using the RA v2.4 messaging protocols.

> **NOTE:** Changing the Site Specific Accession Number parameter at a

multidivisional site will change the parameter for ALL divisions.

Current value of Site Specific Accession Number parameter: NO

Use Site Specific Accession Number? YES [^18]

### Credit completed exams for an Imaging Location [^19]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA CREDIT IMAGING LOCATION\]

This option is used to assign "REGULAR CREDIT" to completed exams that have all required data, but did not receive credit because their Imaging Location was incorrectly assigned as "NO CREDIT".

Before this option can be used, the incorrectly defined Imaging Location must have its CREDIT METHOD field changed from "NO CREDIT" to "REGULAR CREDIT".

Then this option will change the exams for the specified Imaging Location and date range from "NO CREDIT" to "REGULAR CREDIT", and pass the information to the PCE package for crediting.

This option should \*not\* be used to credit exams that were completed by overriding the exam status to "COMPLETE", because the overridden exams probably do not have all required data and would be rejected by the PCE package resulting in many credit failure mail messages.

The option will prompt for the Imaging Location, then the starting and ending exam dates. The user should choose no more than a month's worth of data to process each time, because of the background tasks involved in crediting an exam.

Here is an example:

Select an Imaging Location from the IMAGING LOCATIONS (#79.1) file that is active, receives regular credit, and has a valid DSS ID.

Enter the Imaging Location that you wish to credit: RADIOLOGY LAB

Enter the starting date: : (1/1/1911 - 7/19/2002): 2/1/2002 (FEB 01, 2002)

Enter the ending date: : (2/1/2002 - 7/19/2002): 2/28/2002 (FEB 28, 2002)

Requested Start Time: NOW// \<RET\> (JUL 19, 2002@16:40:32)

Request queued: 362160 @ Jul 19, 2002@16:40:32

### Enable HL7 reprocessing for locked studies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RASAN ENABLE REPROCESSING\]

This option This option enables a sending application for reprocessing of HL7

result messages that were rejected due to a locked study error. Additionally,

it includes a flag that, when set, overrides the radiology NOSEND flag and sends the reprocessed result message back to the sending application.

Select RAD/NUC MED HL7 APPLICATION EXCEPTION HL7 APPLICATION NAME: RA-PSCRIBE-TCP ACTIVE

Are you adding 'RA-PSCRIBE-TCP' as

a new RAD/NUC MED HL7 APPLICATION EXCEPTION (the 3RD)? No// y (Yes)

ENABLE LOCK STUDY REPROCESSING: Y YES

REPROCESS RETURN TO SENDER: Y YES

### Resource Device Specifications for Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA RESOURCE DEVICE\]

If your facility wishes to control the rate at which tasked exam status updates are released to be processed, use this option to enter resource device specifications. This is advised if the facility is experiencing drastic system slowdowns due to periodic heavy use of the online report verification and batch verification of reports options, which can queue a large number of tasks at once.

However, if you choose to enter a Resource Device in this field, you should be careful to completely follow all directions in Kernel documentation after a system crash to bring this Resource Device back up.

Failure to follow those directions could result in Rad/Nuc Med tasks being severely delayed and data corruption.

When you select the option, you are asked to enter a Division and the Device.

### Schedule Perf. Indic. Summary for Fifteenth of Month [^20]Following the Quarter End [^21]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA PERFORMIN SCHEDULE\]

Normally, the Taskman Task List should show:

nnnnnn: RA PERFORMIN TASKLM - Run Previous Quarter's Summary Report. No device.

sss,ttt. From mm/dd/yyyy at hh:mm, By anananan. Scheduled for mm/15/yyyy at hh:mm

This task was submitted to Taskman by patch RA\*5\*44. The task is supposed to run on the fifteenth of each month following the quarter-end. The quarters are calendar quarters (i.e., Jan, Feb, Mar = 1st quarter).

However, if this task is lost from the Taskman queue, this option should be used to put the option, RA PERFORMIN TASKLM, back on the Taskman queue to run on the fifteenth of the current month following the quarter-end or the next month following the quarter-end,[^22] whichever is the closest date in the future.

### Template Compilation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[RA COMPILE TEMPLATES\]

This option recompiles Radiology/Nuclear Medicine input and print templates that are currently compiled. It is advised that all Radiology/Nuclear Medicine users be off the system while the templates are being recompiled.

The user may select compiled templates from any or all of the Radiology/Nuclear Medicine package files that have compiled templates. Also, the user will select the maximum size of the compiled routines.

Here is an example (Note: sites may have compiled templates other than those listed in this example): [^23]

Template Compilation

This option will compile all Radiology/Nuclear Medicine input

and print templates (within the defined file number range) which

are currently compiled on your system. Since these templates

are critical to the operation of the software, it is strongly

advised that all Radiology/Nuclear Medicine users be off the

system. It is also strongly advised that the compilation of

templates be done when system activity is at a minimum.

Is it ok to continue? No// YES

Maximum routine size on this computer in bytes. (2400-5000) : 5000// \<RET\>

Select Rad/Nuc Med Input Template: ??

Select a INPUT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g. -NAME.

To get all NAMES type ALL.

Use an asterisk (\*) to do a wildcard selection, e.g.,

enter NAME\* to select all entries that begin

with the text 'NAME".

Choose from:

RA ORDER EXAM File \#: 75.1

RA QUICK EXAM ORDER File \#: 75.1

RA REGISTER File \#: 70

RA REPORT EDIT File \#: 74

RA VERIFY REPORT ONLY File \#: 74

Select Rad/Nuc Med Input Template: ALL

Another one (Select/De-Select): -RA REPORT EDIT File \#: 74

Another one (Select/De-Select): ??

Select a INPUT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g., -NAME.

To get all NAMES type ALL.

Use an asterisk (\*) to do a wildcard selection, e.g.,

enter NAME\* to select all entries that begin

with the text 'NAME'. Wildcard selection is

case sensitive.

You have already selected:

RA ORDER EXAM File \#: 75.1

RA QUICK EXAM ORDER File \#: 75.1

RA REGISTER File \#: 70

RA VERIFY REPORT ONLY File \#: 74

Choose from:

RA REPORT EDIT File \#: 74

Another one (Select/De-Select): \<RET\>

Select Rad/Nuc Med Print Template: ALL

Another one (Select/De-Select): ??

Select a PRINT TEMPLATE NAME from the displayed list.

To deselect a NAME type a minus sign (-)

in front of it, e.g., -NAME.

To get all NAMES type ALL.

Use an asterisk (\*) to do a wildcard selection, e.g.,

enter NAME\* to select all entries that begin

with the text 'NAME'. Wildcard selection is

case sensitive.

You have already selected:

RA REPORT PRINT STATUS File \#: 74

Choose from:

Another one (Select/De-Select): \<RET\>

Are you sure you wish to compile the selected templates? No// YES

Input template to be compiled: RA ORDER EXAM

For file \#75.1: RAD/NUC MED ORDERS

Routines filed under the following namespace: 'RACTOE'.

Compiling RA ORDER EXAM Input Template of File 75.1...

'RACTOE' ROUTINE FILED.....

'RACTOE1' ROUTINE FILED......

'RACTOE4' ROUTINE FILED......

'RACTOE5' ROUTINE FILED.....

'RACTOE6' ROUTINE FILED.......

'RACTOE8' ROUTINE FILED..

'RACTOE2' ROUTINE FILED..

'RACTOE3' ROUTINE FILED...

'RACTOE7' ROUTINE FILED.

Done!

Input template to be compiled: RA QUICK EXAM ORDER

For file \#75.1: RAD/NUC MED ORDERS

Routines filed under the following namespace: 'RACTQE'.

Compiling RA QUICK EXAM ORDER Input Template of File 75.1....

'RACTQE' ROUTINE FILED......

'RACTQE1' ROUTINE FILED......

'RACTQE3' ROUTINE FILED.......

'RACTQE4' ROUTINE FILED...

'RACTQE6' ROUTINE FILED..

'RACTQE2' ROUTINE FILED...

'RACTQE5' ROUTINE FILED.

Done!

Input template to be compiled: RA REGISTER

For file \#70: RAD/NUC MED PATIENT

Routines filed under the following namespace: 'RACTRG'.

Compiling RA REGISTER Input Template of File 70..

'RACTRG' ROUTINE FILED.....

'RACTRG1' ROUTINE FILED....

'RACTRG2' ROUTINE FILED....

'RACTRG3' ROUTINE FILED.......

'RACTRG6' ROUTINE FILED.......

'RACTRG7' ROUTINE FILED......

'RACTRG8' ROUTINE FILED...

'RACTRG11' ROUTINE FILED..

'RACTRG4' ROUTINE FILED..

'RACTRG5' ROUTINE FILED..

'RACTRG9' ROUTINE FILED...

'RACTRG10' ROUTINE FILED...

'RACTRG12' ROUTINE FILED.

Done!

Input template to be compiled: RA VERIFY REPORT ONLY

For file \#74: RAD/NUC MED REPORTS

Routines filed under the following namespace: 'RACTVR'.

Compiling RA VERIFY REPORT ONLY Input Template of File 74...

'RACTVR' ROUTINE FILED....

'RACTVR1' ROUTINE FILED.....

'RACTVR2' ROUTINE FILED.....

'RACTVR3' ROUTINE FILED...

'RACTVR4' ROUTINE FILED.

Done!

Print template to be compiled: RA REPORT PRINT STATUS

For file \#74: RAD/NUC MED REPORTS

Routines filed under the following namespace: 'RACTRT'.

Compiling RA REPORT PRINT STATUS Print Template of File 74......................

...

'RACTRT' ROUTINE FILED........

Done!

# # Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table 3 - Key Variables</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>NAME</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RA</td>
<td><p>Description: This global contains all of the general table type files used by the Radiology/Nuclear Medicine package. These files are pointed to by other files and contain various types of parameters that may be set up at each site to customize the package to meet that site's needs. The files contained in this global are:</p>
<p>Contract/Sharing Agreements (#34)</p>
<p>Route of Administration (#71.6)</p>
<p>Site of Administration (#71.7)</p>
<p>Radiopharmaceutical Source (#71.8)</p>
<p>Radiopharmaceutical Lot (#71.9)</p>
<p>Examination Status (#72)</p>
<p>Radiology CPT By Procedure Type (#73.2) <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>Standard Reports (#74.1)</p>
<p>Rad/Nuc Med Reason (#75.2)</p>
<p>Complication Types (#78.1)</p>
<p>LBL/HDR/FTR Formats (#78.2)</p>
<p>Diagnostic Codes (#78.3)</p>
<p>Film Sizes (#78.4)</p>
<p>Camera/Equip/Rm (#78.6)</p>
<p>Label Print Fields (#78.7)</p>
<p>Rad/Nuc Med Division (#79)</p>
<p>Imaging Locations (#79.1)</p>
<p>Imaging Type (#79.2)</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="even">
<td>RAD</td>
<td>Description: This RAD global contains data for the Radiation Absorbed Dose file (#70.3). Journalling is mandatory for this global.</td>
</tr>
<tr class="odd">
<td>RADPT</td>
<td><p>Description: This global contains data for the Rad/Nuc Med Patient file (#70).</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="even">
<td>RADPTN</td>
<td><p>Description: This global contains patient exam data specific to radiopharmaceuticals for the Nuc Med Exam Data file (#70.2).</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="odd">
<td>RAMIS</td>
<td><p>Description: This global contains all the files related to Rad/Nuc Med AMIS reporting. The files contained in this global are:</p>
<p>Rad/Nuc Med Procedures (#71)</p>
<p>Major Rad/Nuc Med AMIS Codes (#71.1)</p>
<p>Procedure Modifiers (#71.2)</p>
<p>Rad/Nuc Med Common Procedure (#71.3)</p>
<p>Rad/Nuc Med Procedure Message (#71.4)</p>
<p>Imaging Stop Codes (#71.5)</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="even">
<td>RABTCH</td>
<td><p>Description: This global contains data for:</p>
<p>Report Batches (#74.2)</p>
<p>Report Distribution Queue (#74.3)</p>
<p>Report Distribution (#74.4)</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="odd">
<td>RAO</td>
<td><p>Description: This global contains the data for Rad/Nuc Med Orders file (#75.1).</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
<tr class="even">
<td>RARPT</td>
<td><p>Description: This global contains only data for Rad/Nuc Med Reports file (#74).</p>
<p>The global should be journaled and translated if the operating system supports these functions.</p>
<p>Journaling: Mandatory</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p><span id="_Ref220156552" class="anchor"></span> Patch RA*5*79 February 2007: Added new file to RA global.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Table 3 - Key Variables

# Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table 4 - Function</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>NAME</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RACCESS</td>
<td><p>This local array identifies the user's division, imaging type and imaging location access. This variable, along with RAIMGTY, RAMLC, RAMDV, and RAMDIV are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist.</p>
<p>The routine series RAPSET* sets these variables.</p>
<p>For any initial menu for the Radiology/Nuclear Medicine package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.</p>
<p>The array elements that identify the user's division access look like the following:<br />
RACCESS(DUZ,"DIV",File #79 IEN,File #79.1 IEN)=File #4 IEN^Division name</p>
<p>The array elements that identify the user's imaging type access look like the following:<br />
RACCESS(DUZ,"IMG",File #79.2 IEN,File #79.1 IEN) =null^Imaging Type name</p>
<p>The array elements that identify the user's location access look like the following:<br />
RACCESS(DUZ,"LOC",File #79.1 IEN)=File #44 IEN^Hospital Location name</p></td>
</tr>
<tr class="even">
<td>RABED</td>
<td>Bedsection name. First piece of the zeroth-node for an entry in File #42.4 [Specialty - ^DIC(42.4,]</td>
</tr>
<tr class="odd">
<td>RABTCH</td>
<td>Internal entry number to File #74.2 [Report Batches - ^RABTCH( ] that is used during various batch processing functions.</td>
</tr>
<tr class="even">
<td>RACCOUNTPFSS <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>Account Reference Returned from calling GETACCT^IBBAPI</td>
</tr>
<tr class="odd">
<td>RACLNC</td>
<td>Default clinic name used in the initial exam entry process. First piece of the zeroth-node of an entry in File #44 [Hospital Location - ^SC( ]</td>
</tr>
<tr class="even">
<td>RACN</td>
<td><p>Case Number for an exam;</p>
<p>^RADPT(RADFN,"DT",RADTI,"P",RACNI,0)=RACN^...</p></td>
</tr>
<tr class="odd">
<td>RACNI</td>
<td><p>Internal entry number for an exam;</p>
<p>^RADPT(RADFN,"DT",RADTI,"P",RACNI,0)</p></td>
</tr>
<tr class="even">
<td>RACRT</td>
<td><p>This variable is used by the various workload report routines and it contains either a 'y' for 'yes' or an 'n' for 'no' to indicate to the routine whether the exam being processed should be used in the compilation of the report.</p>
<p>The value of RACRT is obtained from the Examination Status file (#72) entry for which the exam being processed points to. In the Examination Status file there is a field for each workload report.</p>
<p>The variable name RACRT comes from 'CRiTeria'</p></td>
</tr>
<tr class="odd">
<td>RACS</td>
<td>RACS="Y" if the crediting has already been given to PCE (Patient Care Encounter) for the exam currently being processed</td>
</tr>
<tr class="even">
<td>RACT</td>
<td>Internal set value for the various activity logs through out the system; for example, in the exam activity log 'E' means 'Exam Entry'</td>
</tr>
<tr class="odd">
<td>RADATE</td>
<td>Date of registered exam expanded to a user readable format. (i.e., Jun 17,1984)</td>
</tr>
<tr class="even">
<td>RADFN</td>
<td>Internal entry number to Files #2 and #70 [Patient - ^DPT( ]; [Rad/Nuc Med Patient - ^RADPT( ]</td>
</tr>
<tr class="odd">
<td>RADIV</td>
<td>Used in the various workload reports, such as RAWKL*, RAPRC*, RALWKL*, RAMIS*, RAFLM*, to indicate the division currently being processed</td>
</tr>
<tr class="even">
<td>RADOB</td>
<td>Patient's date of birth. Third piece of the zeroth node of an entry in File #2 [Patient - ^DPT( ]</td>
</tr>
<tr class="odd">
<td>RADTE</td>
<td>Exam registration date/time; ^RADPT(RADFN,"DT",RADTI,0)=RADTE^....</td>
</tr>
<tr class="even">
<td>RADTI</td>
<td>Internal entry number of exam registration date/time; also the inverse exam registration date/time; ^RADPT(RADFN,"DT",RADTI,0)</td>
</tr>
<tr class="odd">
<td>RADUZ</td>
<td>Most of the time this is the same as DUZ variable. However, the Radiology/Nuclear Medicine package has the 'feature' to require the user to input their access code during certain processes. RADUZ is equal to that access code's DUZ number.</td>
</tr>
<tr class="even">
<td>RAEXFM</td>
<td>Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the 'exam' label</td>
</tr>
<tr class="odd">
<td>RAEXLBLS</td>
<td>Number of exam labels to be produced by RAFLH* routines</td>
</tr>
<tr class="even">
<td>RAF5</td>
<td>RAF5=IEN of the ward for the patient if the exam being processed was done while the patient was an Inpatient. RAF5's value is taken from the Ward field of the exam subfile of the Rad/Nuc Med Patient file.</td>
</tr>
<tr class="odd">
<td>RAFIN</td>
<td><p>This variable is a flag that is set inside the RA REGISTER input template. If defined after the template is exited, then the system knows that the registration process went to normal completion.</p>
<p>If it is not defined, then the system will automatically delete that current exam because not all questions were answered during the registration process.</p></td>
</tr>
<tr class="even">
<td>RAFLH</td>
<td><p>This variable can take on two different meanings depending on the routine that is being executed.</p>
<p>When you first log on to the package, the routine RAPSET is executed. This routine computes various parameters for the current logon session. One of the parameters set is the printer where all the flash cards requested by the user are printed. The variable RAFLH is used to store this printer information temporarily until it is set in the third piece of the variable RAMLC. (See RAMLC description for more information.)</p>
<p>The variable RAFLH, throughout the rest of the system, is used to specify which LBL/HDR/FTR Formats file (#78.2) entry to use when printing a flash card.</p></td>
</tr>
<tr class="odd">
<td>RAFMT</td>
<td><p>Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2 ] used to produce one of the following:</p>
<p>flash card (RAFLH)</p>
<p>exam label (RAEXFM)</p>
<p>film jacket label (RAJAC)</p>
<p>report header (RAHDFM)</p>
<p>report footer (RAFTFM)</p>
<p>Before each of the above is produced, their respective routine sets RAFMT to their associated format entry and then PRT^RAFLH is called.</p></td>
</tr>
<tr class="even">
<td>RAFTFM</td>
<td>Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the report footer</td>
</tr>
<tr class="odd">
<td>RAGE</td>
<td>Patient's age</td>
</tr>
<tr class="even">
<td>RAHDFM</td>
<td>Internal entry number to File #78.2 [LBL/HDR/FTR Formats - ^RA(78.2, ] that is used for the report header</td>
</tr>
<tr class="odd">
<td>RAHEAD</td>
<td>This is the header used when executing the utility routine RAPTLU. This routine displays the current exams on file for a patient. Depending on what the user is currently doing, the header is different.</td>
</tr>
<tr class="even">
<td>RAIMGTY</td>
<td><p>This variable, along with RACCESS, RAMLC, RAMDV, and RAMDIV are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.</p>
<p>For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.</p>
<p>This variable tracks the Imaging Type for each user based on the location determined at sign-on.</p></td>
</tr>
<tr class="odd">
<td>RAJAC</td>
<td>Default jacket label printer information. (Used only in RAPSET*, the parameter setting routine executed upon logging into the program.)</td>
</tr>
<tr class="even">
<td>RAKEY</td>
<td>During various processes in the Radiology/Nuclear Medicine system, the user must have a certain key. By setting RAKEY equal to this key and then calling USER^RAUTL the system uses one common set of code to check and verify if the user is qualified to do the current process and asks for an access code if required.</td>
</tr>
<tr class="odd">
<td>RAMDIV</td>
<td><p>This variable, along with RACCESS, RAMLC, RAMDV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.</p>
<p>For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.</p>
<p>The variable RAMDIV is the internal entry number to File #79 [Rad/Nuc Med Division - ^RA(79, ]. This is the division that the current location is associated with.</p>
<p><strong>Note:</strong> An imaging location can only be associated with one division.</p></td>
</tr>
<tr class="even">
<td>RAMDV</td>
<td><p>This variable, along with RACCESS, RAMLC, RAMDIV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.</p>
<p>For any initial menu for the package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.</p>
<p>The variable RAMDV has 26 pieces. Each piece contains parameter information pertaining to the current 'division' the user is signed on under. All values are '1' for 'yes' or '0' for 'no'.</p>
<p>The following is a description of each piece:</p>
<table>
<caption><p>Table 5 - Bulletins</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>[not used]</td>
</tr>
<tr class="even">
<td></td>
<td>should a flash card be printed for each exam</td>
</tr>
<tr class="odd">
<td></td>
<td>[no longer used]</td>
</tr>
<tr class="even">
<td></td>
<td>[no longer used]</td>
</tr>
<tr class="odd">
<td></td>
<td>[no longer used]</td>
</tr>
<tr class="even">
<td></td>
<td>various activity logs are kept during the processing of exams and their reports. This piece indicates whether the user should be asked for their access code during each process or should the system automatically use the user code associated with the initial logon. If 'yes' then system assumes the logon user code (DUZ).</td>
</tr>
<tr class="odd">
<td></td>
<td>should entry of a 'Detailed' or 'Series' procedure be required during initial exam registration. If '0' then user can enter a 'Broad' code. However, before the exam can be placed in a 'Complete' status the procedure must be changed to a 'Detailed' or 'Series' procedure.</td>
</tr>
<tr class="even">
<td></td>
<td>should a jacket label be printed automatically during each visit</td>
</tr>
<tr class="odd">
<td></td>
<td>should 'camera/equipment/room' be asked during exam editing</td>
</tr>
<tr class="even">
<td></td>
<td>should the system automatically collect the time when the exam status changes</td>
</tr>
<tr class="odd">
<td></td>
<td>If piece 10 is set to '1', collect status change time data, then should the user be asked the time of the status change or should the system automatically use the current date and time. (If you are batch filing the changes then this parameter would be '1' so that the user can put in the actual change time.)</td>
</tr>
<tr class="even">
<td></td>
<td>should the transcriptionist be given the opportunity to select a standard report during initial report entry</td>
</tr>
<tr class="odd">
<td></td>
<td>should the transcriptionist be given the opportunity to place reports in a batch during report entry</td>
</tr>
<tr class="even">
<td></td>
<td>should the transcriptionist be given the opportunity to copy the contents of one report into another</td>
</tr>
<tr class="odd">
<td></td>
<td>[not used]</td>
</tr>
<tr class="even">
<td></td>
<td>require that an impression be given on a report before the report can be verified and the exam to be considered 'complete'</td>
</tr>
<tr class="odd">
<td></td>
<td>should the transcriptionist be prompted for the date the exam was requested</td>
</tr>
<tr class="even">
<td></td>
<td>allow interpreting residents to verify other interpreting physicians' reports while using the On-line Verifying of Reports option</td>
</tr>
<tr class="odd">
<td></td>
<td>collect the date and the time of request status changes</td>
</tr>
<tr class="even">
<td></td>
<td>[not used]</td>
</tr>
<tr class="odd">
<td></td>
<td>indicate that the user should be asked when requesting an exam, which Imaging Location the request should be forwarded to</td>
</tr>
<tr class="even">
<td></td>
<td>if a user without the RA MGR key can enter a report on a cancelled case</td>
</tr>
<tr class="odd">
<td></td>
<td>[not used]</td>
</tr>
<tr class="even">
<td></td>
<td>the number of hours in the future (0-168) that a user may register a patient for an exam</td>
</tr>
<tr class="odd">
<td></td>
<td>should the report status appear on unverified reports</td>
</tr>
<tr class="even">
<td></td>
<td>should an e-mail of the radiology/nuclear medicine report findings be automatically sent to the requesting physician</td>
</tr>
</tbody>
</table>
<p><strong>Note:</strong> These parameters are permanently stored in the .1 node of the appropriate entry in File #79 [Rad/Nuc Med Division - ^RA(79,]. The Division Parameter Set-up option under the System Definition Menu is used to set this node.</p></td>
</tr>
<tr class="odd">
<td>RAMLC</td>
<td><p>This variable, along with RACCESS, RAMDIV, RAMDV, and RAIMGTY are package-wide variables set by the system. They are all normally computed during the login process. They are also set by the individual options of the package if they do not already exist. The routine series RAPSET* sets these variables.</p>
<p>For any initial menu for the Radiology/Nuclear Medicine package created at the local site level, these variables must be killed. Do this by making D KILL^RAPSET1 the exit action for the menu.</p>
<p>The variable RAMLC has thirteen pieces. Each piece contains parameter information pertaining to the current imaging location the user is signed on under.</p>
<p>The following is a description of each piece: (IEN ==&gt; internal entry number)</p>
<table>
<caption><p>Table 6 - Mail Groups</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>IEN to File #79.1 [Imaging Location] - used to stuff proper location in registration record</td>
</tr>
<tr class="even">
<td></td>
<td>how many flash cards to produce per patient visit</td>
</tr>
<tr class="odd">
<td></td>
<td>flash card printer name - used to automatically queue flash cards and exam labels without having to ask the user the device question</td>
</tr>
<tr class="even">
<td></td>
<td>how many jacket labels to print per visit</td>
</tr>
<tr class="odd">
<td></td>
<td>jacket label printer name - used to automatically queue jacket labels without having to ask the user the device question</td>
</tr>
<tr class="even">
<td></td>
<td>IEN to File #79.2 [Imaging Type] - used to stuff proper imaging type in registration record (always Rad/Nuc Med's internal number)</td>
</tr>
<tr class="odd">
<td></td>
<td><p>default flash card format</p>
<p>IEN to File #78.2 [LBL/HDR/FTR Formats]</p>
<p>used when queuing a flash card to print; this format is the default flash card for the current location</p></td>
</tr>
<tr class="even">
<td></td>
<td>how many exam labels to produce for each exam - when flash cards are queued to print, the system must also be told how many exam labels to print.</td>
</tr>
<tr class="odd">
<td></td>
<td><p>default exam label format</p>
<p>IEN to File #78.2 [LBL/HDR/FTR Formats]</p>
<p>used when queuing an exam label to print; this format is the default 'exam label' for the current location</p>
<p><strong>Note:</strong> Exam labels always print after flash card labels are printed.</p></td>
</tr>
<tr class="even">
<td></td>
<td>report printer name - used to automatically queue reports without having to ask the user the device question</td>
</tr>
<tr class="odd">
<td></td>
<td><p>default jacket label format</p>
<p>IEN to File #78.2 [LBL/HDR/FTR Formats]</p>
<p>used when queuing a jacket label to print; this format is the default jacket label for the current location</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>default report header format</p>
<p>IEN to File #78.2 [LBL/HDR/FTR Formats]</p>
<p>used when queuing a report to print; this format is the default 'header' for the current location</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>default report footer format</p>
<p>IEN to File #78.2 [LBL/HDR/FTR Formats]</p>
<p>used when queuing a report to print; this format is the default footer for the current location</p></td>
</tr>
</tbody>
</table>
<p><strong>Note</strong>: These parameters are permanently stored in the zeroth node of the appropriate entry in File #79.1 [Imaging Location - ^RA(79.1,]<br />
The Location Parameter Set-up option under the System Definition Menu is used to set this no.</p></td>
</tr>
<tr class="even">
<td>RAMUL</td>
<td>Internal entry number to File #71.2 [Procedure Modifiers - ^RAMIS(71.2, ]</td>
</tr>
<tr class="odd">
<td>RANME</td>
<td>Patient's name. First piece of the zeroth-node of File #2 [Patient - ^DPT( ]</td>
</tr>
<tr class="even">
<td>RANUM</td>
<td>Number of flash cards, exam labels or jacket labels to produce when there is a call to PRT^RAFLH. RANUM is always one for report header and footer production.</td>
</tr>
<tr class="odd">
<td>RAPHY</td>
<td>Default provider name used in the initial exam entry process. First piece of the zeroth-node of an entry in File #200 [New Person - ^VA(200, ]</td>
</tr>
<tr class="even">
<td>RAPRC</td>
<td>Exam Procedure name. First piece of the zeroth-node of an entry in File #71 [Rad/Nuc Med Procedures - ^RAMIS(71, ]</td>
</tr>
<tr class="odd">
<td>RAPRI</td>
<td>Internal entry number to File #71 [Rad/Nuc Med Procedures - ^RAMIS(71, ]</td>
</tr>
<tr class="even">
<td>RAQUICK</td>
<td>This variable is used inside the 'Edit Exam' template to properly log an entry into the exam's activity log. The variable is set before going into the template. If set to '1' then the template knows that the editing is occurring through the case number edit routine and if set to '0' then it means the editing is occurring from the edit by patient routine.</td>
</tr>
<tr class="odd">
<td>RARPT</td>
<td>Internal entry number to File #74 [Rad/Nuc Med Reports - ^RARPT( ]</td>
</tr>
<tr class="even">
<td>RASER</td>
<td>Service name. First piece of the zeroth-node of an entry in File #49 [Service/Section - ^DIC(49, ]</td>
</tr>
<tr class="odd">
<td>RASSN</td>
<td>Patient's SSN. Ninth piece of the zeroth-node of an entry in File #2 (Patient - ^DPT( )</td>
</tr>
<tr class="even">
<td>RAST</td>
<td><p>This variable can have three meanings depending on where it is used.</p>
<p>In routine RADEM1, the patient demographic display routine, it is equal to the first piece of the zeroth node of an entry in File #72 [Examination Status - ^RA(72, ]</p>
<p>In routine RARTR, the report print routine, it is equal to the set code for the report status.</p>
<p>Otherwise, this variable is normally equal to the internal entry number of an entry in File #72 [Examination Status - ^RA(72, ]</p></td>
</tr>
<tr class="odd">
<td>RASTI</td>
<td>Internal entry number to File #72 [Examination Status - ^RA(72, ]</td>
</tr>
<tr class="even">
<td>RAWARD</td>
<td>Ward Name. First piece of the zeroth-node of an entry in File #42 [Ward Location - ^DIC(42, ]</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch RA*5*57 March 2006: Added key variable RACCOUNT PFSS.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Table 4 - Function

## Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME | DESCRIPTION                                                                                                                                                                                                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RACAT    | Uses the RAUTL1 routine to compute the location (inpatient, outpatient, contract/sharing agreement, research) and convert time of day to external format. It computes the exam status and updates the status log and OE/RR. It sends alert/notification to OE/RR after the patient is examined. |

Table 7 - VA FileMan File Protection

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend that when setting up mail groups for each of the following bulletins, you name the mail group something similar to the bulletin.

| BULLETIN NAME             | DESCRIPTION                                                                                                                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RAD/NUC MED CREDIT FAILURE    | Bulletin will notify users in the selected mailgroup(s) that a crediting failure occurred.                                                                                                 |
| RAD/NUC MED EXAM DELETED      | Bulletin used to notify the radiology supervisor that a radiology exam has been deleted and the computer user who did deletion.                                                            |
| RAD/NUC MED REPORT DELETION   | Bulletin used to notify a mail group that a radiology report has been deleted.                                                                                                             |
| RAD/NUC MED REPORT UNVERIFIED | Bulletin used to notify the radiology supervisor, ADPAC and other selected recipients that a 'verified' radiology report was 'unverified' and the computer user who did the 'unverifying'. |
| RAD/NUC MED REQUEST CANCELLED | Bulletin used to notify the recipient mail group (usually named 'RA REQUEST CANCELLED') that a radiology request has been cancelled.                                                       |
| RAD/NUC MED REQUEST HELD      | Bulletin used to notify the 'RA REQUEST HELD' mail group thatradiology request has been held.                                                                                              |

Table 8: File Numbers and Description

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| MAIL GROUP NAME               | DESCRIPTION                                                                                                                                                                                           |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RADPERFORMANCEINDICATOR [^24] | Mail group containing names of local users who are to receive a copy of the Radiology Performance Indicator Summary Report in their VistA mail basket.                                                |
| RADHL7MESSAGE [^25]           | This mail group is used to inform radiology users about issues regarding the HL7 interface between the VistA Radiology/Nuclear Medicine application and Commercial Off The Shelf (COTS) applications. |
| RADNTRT                       | This mail group will be used in communication with the NTRT team for new radiology procedures.                                                                                                        |

Table 9 - Input Templates

# # Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RA ALLOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ownership of the RA ALLOC key overrides the location access security given to personnel through Classification Enter/Edit. Owners of the RA ALLOC key have expanded access to Imaging Locations, Imaging Types, and Divisions. In the case of most workload reports, this means they can select from a list of all Divisions and Imaging Types to include on the report. In the case of various edit and ordering functions, it means they can select from all locations within the Imaging Type to which they are currently signed on through the "Select sign-on location prompt.

### RA MGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA MGR key gives the user access to supervisor-type functions. Those functions are the following:

1.  Editing Completed Exams
2.  Adding An Exam To A Visit That Is Older Than Yesterday
3.  Showing The User All Non-Completed Exams, Not Just Those Associated With The User's Current Division, During Execution Of The "Status Tracking" Function.
4.  Updating The Exam Status Of An Exam To Complete
5.  Deleting Exams
6.  Deleting Reports
7.  Entering A Report On A Cancelled Exam If Site Parameters Don't Allow It
8.  Deleting Printed Batches By Date
9.  Synching Up Exams With CPRS & Radiology Orders

### RA VERIFY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA VERIFY key allows users to verify reports.

### RA RPTMGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA RPTMGR key gives the user supervisor-type privilege to unverify a report, delete a report, and restore a deleted report.

### RA SWITCHLOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA SWITCHLOC key gives the user the ability to register an exam under a different modality than the order.

## Sign-on Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon entering a Radiology/Nuclear Medicine menu, the user is prompted to select a "sign-on Imaging Location". The set of locations the user is privileged to access is controlled by the ADPAC or IRM through the Classification Enter/Edit option. Most options are screened by a combination of Imaging Type, Division and Location. Others are screened by ownership. For a thorough discussion of how users are allowed into the Radiology/Nuclear Medicine package options, see the Screening Methods section of the Radiology/Nuclear Medicine ADPAC Guide.

## Electronic Signature [^26]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an Interpreting Staff physician wants to verify a report via VistA’s On-line Verifying of Reports or Resident On-Line Pre-Verification option, he must hold the RA VERIFY key and enter an electronic signature code before he can verify the report. This electronic signature code is encrypted.

### COTS HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an Interpreting Staff physician verifies a report on a COTS Voice Recognition system (such as TalkStation or PowerScribe [^27]) interfaced to VistA*,* the electronic signature processing is not the same as with the VistA options.

The system administrator for the COTS system assigns verifying privileges, similar to the RA VERIFY key, to each physician. An ID that matches the IEN of the physician in the New Person file \#200 is also assigned to the physician. When the physician logs on to the COTS application, an ID and secure password are entered to identify the physician.

When a report has been signed and released on the COTS system, it is transmitted over the TCP/IP interface and is received by the Radiology HL7 "bridge" routine RAHLTCPB. Based on the HL7 status of the report, the processing logic will determine if the report has been verified on the COTS system.

This routine will get the verifying physician from the OBR segment's Principal Result Interpreter field (OBR-32) in the HL7 Unsolicited Observation (ORU) report message.[^28] If this physician holds the RA VERIFY key, and the physician has a valid electronic signature defined in File \#200, the report is filed in the Rad/Nuc Med Report file as VERIFIED with the electronic signature printed block name attached. This process does not currently use any encryption technology, and the processing routine assumes that the verifying physician ID in the OBR segment of the HL7 message belongs to the physician that signed the report on the COTS system.

Even though the VistA routine RAHLTCPB uses certain data items to validate the report sent from the COTS system before it assigns a signature to the report, it can not prevent a renegade software application from sending bogus HL7 messages to the Radiology/Nuclear Medicine system.

While the sending of bogus HL7 messages is not a likely occurrence, it must be recognized as a real and potential breach that could have an impact on Rad/Nuc Med Reports.

Technical Services is considering the use of Public Key Encryption schemes. When an encryption scheme such as this is implemented as a standard, the Radiology developers will issue a patch for COTS interfaces that use the Public Key Encryption schemes for electronic signatures.

Patch RA\*5.0\*78 - *Query the VistA Radiology/Nuclear Medicine application for results* allows the VistA Radiology/Nuclear Medicine application to accept an inbound query from ScImage and return radiology results back to ScImage. This historical information serves as a reference for the teleradiologists working for the National Teleradiology Project.

> **NOTE:** ScImage is a specific vendor. The query was developed to be vendor independent. There are two different sort criteria for the query. The client (ScImage) can request results based on:

- A single accession number (one patient/one result)
- A patient record number, within a patient care event date/time window, and maximum number of results to be returned on that patient.

The following components are exported with RA\*5.0\*78:

File Number File Name Record Name

779.2 HLO APPLICATION REGISTRY RA-NTP-QUERY

RA-NTP-RSP

3.8 MAIL GROUP RAD HL7 MESSAGES [^29]

> **NOTE:** The Electronic Signature for COTS HL7 interfaces can be enabled or disabled in the VistA Radiology/Nuclear Medicine application for each division record in the RAD/NUC MED DIVISION (#79) file.[^30] For information on setting up the COTS HL7 interface electronic signature feature, please refer to the following Radiology/Nuclear Medicine v5.0 manuals:[^31]

- Radiology/Nuclear Medicine 5.0 HL7 Setup/Implementation Manual
- Radiology/Nuclear Medicine 5.0 HL7 Interface Specification [^32]

## VA FileMan File Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#    | Name                               | DD | RD | WR | DEL | LAYGO |
|-----------|----------------------------------------|--------|--------|--------|---------|-----------|
| 34        | Contract/Sharing Agreements            | @      |        |        |         |           |
| 70        | Rad/Nuc Med Patient                    | @      |        |        |         |           |
| 70.2      | Nuc Med Exam Data                      | @      |        |        |         |           |
| 70.3      | Radiation Absorbed Dose                | @      |        |        |         |           |
| 71        | Rad/Nuc Med Procedures                 | @      |        |        |         |           |
| 71.1      | Major Rad/Nuc Med AMIS Codes           | @      |        |        |         |           |
| 71.1235   | Radiology Procedure Map to CC Consult  | @      | @      | @      | @       | @         |
| 71.2      | Procedure Modifiers                    | @      |        |        |         |           |
| 71.3      | Rad/Nuc Med Common Procedure           | @      |        |        |         |           |
| 71.4      | Rad/Nuc Med Procedure Message          | @      |        |        |         |           |
| 71.5      | Imaging Stop Codes                     | @      |        |        |         |           |
| 71.6      | Route of Administration                | @      |        |        |         |           |
| 71.7      | Site of Administration                 | @      |        |        |         |           |
| 71.8      | Radiopharmaceutical Source             | @      |        |        |         |           |
| 71.9      | Radiopharmaceutical Lot                | @      |        |        |         |           |
| 71.98     | Master Radiology Site File             | @      |        |        |         |           |
| 71.99     | Master Radiology Procedure File (MRPF) | @      |        |        |         |           |
| 72        | Examination Status                     | @      |        |        |         |           |
| 74        | Rad/Nuc Med Reports                    | @      |        |        |         |           |
| 74.1      | Standard Reports                       | @      |        |        |         |           |
| 74.2      | Report Batches                         | @      |        |        |         |           |
| 74.3      | Report Distribution Queue              | @      |        |        |         |           |
| 74.4      | Report Distribution                    | @      |        |        |         |           |
| 75.1      | Rad/Nuc Med Orders                     | @      |        |        |         |           |
| 75.2      | Rad/Nuc Med Reason                     | @      |        | @      | @       | @         |
| 78.1      | Complication Types                     | @      |        |        |         |           |
| 78.2      | LBL/HDR/FTR Formats                    | @      |        |        |         |           |
| 78.3      | Diagnostic Codes                       | @      |        |        |         |           |
| 78.4      | Film Sizes                             | @      |        |        |         |           |
| 78.6      | Camera/Equip/Rm                        | @      |        |        |         |           |
| 78.7      | Label Print Fields                     | @      |        |        |         |           |
| 79        | Rad/Nuc Med Division                   | @      |        |        |         |           |
| 79.1      | Imaging Locations                      | @      |        |        |         |           |
| 79.2      | Imaging Type                           | @      |        |        |         |           |
| 79.3[^33] | HL7 Message Exceptions                 | @      | @      | @      | @       | @         |
| 79.7[^34] | Rad/Nuc Med HL7 Application Exceptions | @      |        |        |         |           |

Table 10 - Sort Templates

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Radiology/Nuclear Medicine package uses the Current Procedural Terminology (CPT) coding system which is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA.

# # Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines exported in the VistA Radiology/Nuclear Medicine application are namespaced ‘RA’. Routine names are alphanumeric characters (uppercase letters only) with a maximum length of eight characters.

Excludes in the list of routines are the following namespaces: ‘RAI’ (Radiology initialization routines), ‘RACT\*’ (Radiology routines compiled by VA FileMan) and ‘RAZ\*’ (locally developed Radiology routines).

Short Listing of Selected Routine/Include Files

Namespace: DEVRAD

19 May 2025 11:59 AM Page 1

-- .INT --

RA RA01 RAAPI RABAR RABAR1 RABIRAD RABTCH RABTCH1

RABTCH2 RABTCH3 RABUL RABUL1 RABUL2 RABUL3 RABWIBB RABWIBB2

RABWORD RABWORD1 RABWORD2 RABWPCE RABWRTE RABWUTL RACDR RACDR1

RACMHIS RACMP RACMP1 RACMP2 RACMPLE RACNLU RACNVRT3 RACOMDEL

RACPT RACPT1 RACPTCSV RACPTMSC RACTCERN RACTRG RACTRG1 RACTRG2

RADD1 RADD2 RADD3 RADD4 RADELSVR RADEM RADEM1 RADEM2

RADLQ1 RADLQ2 RADLQ3 RADLY RADLY1 RADOSTIK RADPA RADRPT1

RADRPT1A RADRPT2 RADRPT2A RADTICK RADUTL RAEDCN RAEDCN1 RAEDPT

RAERR RAERR01 RAERRPT RAESO RAESR RAESR1 RAESR2 RAESR3

RAFLH RAFLH1 RAFLH2 RAFLM RAFLM1 RAFLM2 RAFLM3 RAHL7C

RAHL7L RAHL7O RAHL7Q RAHL7Q1 RAHLACK RAHLBKVQ RAHLBKVR RAHLBMS

RAHLCV RAHLCV1 RAHLEX RAHLEX1 RAHLEXF RAHLNTEG RAHLO RAHLO1

RAHLO2 RAHLO3 RAHLO4 RAHLOPT RAHLQ RAHLQ1 RAHLR RAHLR1

RAHLR1A RAHLROUT RAHLRPC RAHLRPRO RAHLRPT RAHLRPT1 RAHLRPT2 RAHLRPTT

RAHLRS RAHLRS1 RAHLRU RAHLRU1 RAHLTCPB RAHLTCPU RAHLTCPX RAIPS226

RAJAC RAKRDIT RALIST RALIST1 RALOCK RALOCK01 RALWKL RALWKL1 RALWKL2

RALWKL3 RALWKL4 RAMAG RAMAG02 RAMAG02A RAMAG03 RAMAG03A RAMAG03C

RAMAG03D RAMAG04 RAMAG05 RAMAG06 RAMAG06A RAMAG07 RAMAGHL RAMAGRP1

RAMAGRP2 RAMAGU01 RAMAGU02 RAMAGU03 RAMAGU04 RAMAGU05 RAMAGU06 RAMAGU07

RAMAGU08 RAMAGU09 RAMAGU10 RAMAGU11 RAMAGU12 RAMAGU13 RAMAGU14 RAMAIN

RAMAIN1 RAMAIN2 RAMAIN3 RAMAIN4 RAMAIN5 RAMAINP RAMAINP1 RAMAINU

RAMAINU1 RAMAORPT RAMGI001 RAMGI002 RAMGI003 RAMGI004 RAMGINI0 RAMGINI1

RAMGINI2 RAMGINI3 RAMGINIT RAMIS RAMIS1 RAMIS2 RAMRPIN RANEWPRO

RANMED1 RANMPRT1 RANMPT1 RANMUSE1 RANMUSE2 RANMUSE3 RANMUTL1 RANPRO

RANPRO1 RANPRO4 RANPRO5 RANPROU RANPROU2 RANTEG RAO7CH RAO7CMP

RAO7MFN RAO7NEW RAO7OKR RAO7OKS RAO7PC1 RAO7PC1A RAO7PC2 RAO7PC3

RAO7PC4 RAO7PURG RAO7RCH RAO7RO RAO7RO1 RAO7ROCN RAO7RON RAO7RON1

RAO7SCH RAO7UTL RAO7UTL1 RAO7VLD RAO7XX RAONDEM RAONI001 RAONIT

RAONIT1 RAONIT2 RAONIT3 RAORD RAORD1 RAORD1A RAORD2 RAORD3

RAORD4 RAORD5 RAORD6 RAORD61 RAORD7 RAORD7A RAORD8 RAORDC

RAORDC1 RAORDCP RAORDP RAORDQ RAORDR RAORDR1 RAORDR2 RAORDS

RAORDU RAORDU1 RAORR RAORR1 RAORR2 RAORR3 RAOUT RAPAST

RAPAT23 RAPAT23A RAPCE RAPCE1 RAPCE2 RAPERR RAPERR1 RAPINFO

RAPM RAPM1 RAPM2 RAPM3 RAPM4 RAPMW RAPMW1 RAPMW2

RAPMW3 RAPNL RAPRC RAPRC1 RAPRE4 RAPRI RAPRINT RAPRINT1

RAPROD RAPROD1 RAPROD2 RAPROQ RAPROS RAPSAPI RAPSAPI2 RAPSAPI3

RAPSET RAPSET1 RAPTLU RAPURGE RAPURGE1 RAPXRM RARD RARECOV

RAREG RAREG1 RAREG2 RAREG3 RAREG4 RARESTOR RARIC RARIC1

RARPTUT RART RART1 RART2 RART3 RARTE RARTE1 RARTE2

RARTE3 RARTE4 RARTE5 RARTE6 RARTE7 RARTFLDS RARTR RARTR0

RARTR1 RARTR2 RARTR3 RARTRPV RARTRPV1 RARTST RARTST1 RARTST2

RARTST2A RARTST3 RARTUTL RARTUTL1 RARTUVR RARTUVR1 RARTUVR2 RARTUVR3

RARTVER RARTVER1 RARTVER2 RASELCT RASERV RASETU RASIGU RASITE

RASTAT RASTED RASTEXT RASTEXT1 RASTREQ RASTREQ1 RASTREQN RASTRPT

RASTRPT1 RASTRPT2 RASYNCH RASYNCHLU RASYS RASYS1 RATIMBUL RATRAN

RAUTL RAUTL0 RAUTL00 RAUTL1 RAUTL10 RAUTL11 RAUTL12 RAUTL13

RAUTL14 RAUTL15 RAUTL16 RAUTL16A RAUTL17 RAUTL18 RAUTL19 RAUTL19A

RAUTL19B RAUTL19C RAUTL2 RAUTL20 RAUTL21 RAUTL22 RAUTL23 RAUTL3

RAUTL4 RAUTL5 RAUTL6 RAUTL7 RAUTL7A RAUTL8 RAUTL9 RAUTODC

RAWFR1 RAWFR2 RAWFR3 RAWFR4 RAWKL RAWKL1 RAWKL2 RAWKL3

RAWKLU RAWKLU1 RAWKLU2 RAWKLU3 RAWORK RAWRVUP RAXMLSND RAXREF

RAXSTAT

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table 11 - Print Templates</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE NUMBER</th>
<th>GLOBAL FILE DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>34</p>
<p>Contract/Sharing Agreements</p></td>
<td><p>^DIC(34</p>
<p>This file contains the Contract and Sharing agreements used in Radiology.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>70</p>
<p>Rad/Nuc Med Patient</p></td>
<td><p>^RADPT(</p>
<p>This file contains imaging information for patients. It is the focal point of the package.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="odd">
<td><p>70.2</p>
<p>Nuc Med Exam Data</p></td>
<td><p>^RADPTN(</p>
<p>This file contains information specific to nuclear medicine studies in which radiopharmaceuticals are used.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>70.3</p>
<p>Radiation Absorbed Dose</p></td>
<td><p>^RAD(</p>
<p>This file is used to measure the amount of radiation absorbed by a person, known as the “absorbed dose,” this tallies the amount (quantity) of radioactive energy that radioactive sources deposit in patients. Occurs on a study by study, case by case basis that the subject patient is involved in.</p></td>
</tr>
<tr class="odd">
<td><p>71</p>
<p>Rad/Nuc Med Procedures</p></td>
<td><p>^RAMIS(71</p>
<p>This file contains all the procedures that may be associated with an imaging exam. If the procedure has an inactivation date less than the current date then it is not a valid choice and will not appear as a selection to the user. Entries should be deactivated rather than deleted.</p></td>
</tr>
<tr class="even">
<td><p>71.1</p>
<p>Major Rad/Nuc Med AMIS Codes</p></td>
<td><p>^RAMIS(71.1</p>
<p>This file contains the valid AMIS codes, descriptions and weighted work units as assigned by VACO. The data in this file is used in the compilation of various workload reports.</p>
<p>Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.</p></td>
</tr>
<tr class="odd">
<td><p>71.11</p>
<p>New Rad Procedure Workup</p></td>
<td><p>^RAMIS(71.11</p>
<p>This file houses the new procedures being created in file 71 with a “Detailed” Type temporarily while the procedure is being created and will be removed from thos location once the procedure has been completed.</p></td>
</tr>
<tr class="even">
<td><p>71.1235</p>
<p>Radiology Procedure Map to CC Consult</p></td>
<td><p>^RA(71.1235</p>
<p>This file is added with radiology patch RA*5.0*223 and contains</p>
<p>radiology procedures that are associated with a consult service for the purpose of community care referrals of radiology orders. The entries in this file are used by the radiology option 'Refer Selected Requests to COMMUNITY CARE Provider' [RA ORDERREF] to determine if a special consult title should be used for the community care consult order. The entries in this file are maintained nationally and should not be modified.</p></td>
</tr>
<tr class="odd">
<td><p>71.2</p>
<p>Procedure Modifiers</p></td>
<td><p>^RAMIS(71.2</p>
<p>This file contains the modifiers that can be associated with an imaging exam. These modifiers are used to further describe the procedure associated with the exam.</p>
<p>Data comes with the file. It is ADDed ONLY IF NEW to the site's existing entries. Only modifiers with an internal entry number of less than 6 are exported with this version.</p></td>
</tr>
<tr class="even">
<td><p>71.3</p>
<p>Rad/Nuc Med Common Procedure</p></td>
<td><p>^RAMIS(71.3</p>
<p>This file contains the procedures used in the display of the common procedures when requesting a procedure. Forty active procedures are allowed per imaging type.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="odd">
<td><p>71.4</p>
<p>Rad/Nuc Med Procedure Message</p></td>
<td><p>^RAMIS(71.4</p>
<p>This file contains messages concerning special requirements when ordering a procedure. One or more of these messages can be tied to a procedure in the Rad/Nuc Med Procedures file (#71) so that they are displayed to a requestor at the time an order is placed.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="even">
<td><p>71.5</p>
<p>Imaging Stop Codes</p></td>
<td><p>^RAMIS(71.5</p>
<p>This file contains valid imaging stop codes. It is not pointed to by any other file. The Rad/Nuc Med ADPAC should make sure this file is updated. Obsolete or unused entries should be deleted. This file should contain all stop codes that can be assigned to imaging locations at the facility.</p>
<p>No data comes with the file.</p></td>
</tr>
<tr class="odd">
<td><p>71.6</p>
<p>Route of Administration</p></td>
<td><p>^RAMIS(71.6</p>
<p>This file contains possible routes of radiopharmaceutical administration used in imaging exams.</p>
<p>Data comes with this file. Routes may be added/edited.</p></td>
</tr>
<tr class="even">
<td><p>71.7</p>
<p>Site of Administration</p></td>
<td><p>^RAMIS(71.7</p>
<p>This file contains frequently-used sites of radiopharmaceutical administration for imaging exams.</p>
<p>Data comes with this file. Sites may be added/edited.</p></td>
</tr>
<tr class="odd">
<td><p>71.8</p>
<p>Radiopharmaceutical Source</p></td>
<td><p>^RAMIS(71.8</p>
<p>This file contains the names of vendors, pharmacies, and other sources of radiopharmaceuticals.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>71.9</p>
<p>Radiopharmaceutical Lot</p></td>
<td><p>^RAMIS(71.9</p>
<p>This file is used to record names of radiopharmaceutical lots, batches, vials, syringes, or kits at the discretion of the facility.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>71.98</p>
<p>Master Radiology Site File</p></td>
<td>This VistA file is a national file used by all VA VistA sites that includes a configurable parameter that will indicate whether ISAAC is active or not, a field named “SEEDING COMPLETE” that controls whether messages are sent to NTRT when a new procedure is created, and monitors the mapping of radiology procedures to the Master Radiology Procedure File (MRPF) and allows the user to stop and restart the mapping process without losing their place in the RAD/NUC MED PROCEDURE file (#71).</td>
</tr>
<tr class="even">
<td><p>71.99</p>
<p>Master Radiology Procedure File (MRPF)</p></td>
<td>This VistA file is a national file used by all VA VistA sites with the following fields: reflecting the standardized procedure the GOLD NAME field which points to the MRPF NAME field in file 71, the VUID NUMBER, the CPT Code, the LOINC Code, LOINC Long description, LOINC Short description, and MRPF LONG NAME for the purposes of interoperability between VA offices and external entities.</td>
</tr>
<tr class="odd">
<td><p>72</p>
<p>Examination Status</p></td>
<td><p>^RA(72</p>
<p>This file contains the statuses an imaging exam may be in, as it is processed. Each status has a set of parameters that drives exam processing and management report logic.</p>
<p>Data comes with the file. It is MERGE'd with existing entries. Statuses can be edited.</p></td>
</tr>
<tr class="even">
<td><p>73.1</p>
<p>Rad Modality Defined Terms <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></td>
<td><p>VistA Imaging software will build a modality work list using this file and the Rad/Nuc Med Procedure file (#71) entries. The work list identifies the scheduled radiology cases to be performed on the individual modality (equipment). Entries in this file are as defined in the DICOM Standards PS 3.3 - 1998 under section General Series Attribute Descriptions (C.7.3.1.1).</p>
<p>Data comes with this file. Do not change/add/delete any records in this file.</p></td>
</tr>
<tr class="odd">
<td><p>73.2</p>
<p>Radiology CPT By Procedure Type</p></td>
<td><p>^RA(73.2</p>
<p>This file contains Procedure Types and CPT Codes supplied by the Office of Patient Care Services.</p>
<p>Data comes with this file. The data cannot be edited locally. Records may be added by the Office of Patient Care Services via a new Radiology patch; existing records may be updated but never deleted.</p></td>
</tr>
<tr class="even">
<td><p>74</p>
<p>Rad/Nuc Med Reports</p></td>
<td><p>^RARPT(</p>
<p>This file contains the reports for registered exams.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>74.1</p>
<p>Standard Reports</p></td>
<td><p>^RA(74.1</p>
<p>This file contains the standard report text the interpreting physician can choose from when dictating a report.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>74.2</p>
<p>Report Batches</p></td>
<td><p>^RABTCH(74.2</p>
<p>This file provides the mechanism to group draft reports into logical categories to help in the efficient processing of these reports.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>74.3</p>
<p>Report Distribution Queue</p></td>
<td><p>^RABTCH(74.3</p>
<p>This file contains the names of the distribution queues and the category of reports for each queue.</p>
<p>Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.</p></td>
</tr>
<tr class="even">
<td><p>74.4</p>
<p>Report Distribution</p></td>
<td><p>^RABTCH(74.4</p>
<p>This file points to the Rad/Nuc Med Reports file (#74). It contains the only verified reports associated with the various active distribution queues.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>75.1</p>
<p>Rad/Nuc Med Orders</p></td>
<td><p>^RAO(75.1</p>
<p>This file contains all information pertaining to an imaging order entered for a patient.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>75.2</p>
<p>Rad/Nuc Med Reason</p></td>
<td><p>^RA(75.2</p>
<p>This file contains the reasons a user may select from when placing an order in the Hold or Cancelled status.</p>
<p>Data comes with this file. Changing or adding data to this file is prohibited.</p></td>
</tr>
<tr class="odd">
<td><p>75.3</p>
<p>Community Care Justifications</p></td>
<td><p>^RA(75.3</p>
<p>WARNING: ENTRIES SHOULD NOT BE ADDED/DELETED/CHANGED FROM THIS FILE.</p>
<p>This file contains only data supplied by the Office of Community</p>
<p>Care. The data are sent to the Radiology development and</p>
<p>maintenance teams.</p>
<p>This file contains the justifications a user may select from when</p>
<p>referring an order to Community Care.</p></td>
</tr>
<tr class="even">
<td><p>78.1</p>
<p>Complication Types</p></td>
<td><p>^RA(78.1</p>
<p>This file contains the types of complications that may occur while a procedure is being performed.</p>
<p>Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.</p></td>
</tr>
<tr class="odd">
<td><p>78.2</p>
<p>Lbl/Hdr/Ftr Formats</p></td>
<td><p>^RA(78.2</p>
<p>This file contains the print formats for flash cards, exam labels, jacket labels, report headers and report footers.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>78.3</p>
<p>Diagnostic Codes</p></td>
<td><p>^RA(78.3</p>
<p>This file contains the diagnostic codes that can be associated with an exam. The diagnostic code represents a quick overall summary of what the interpreting physician wrote in the report concerning the exam. The diagnostic code is not the impression. The impression is stored in the Impression field (#300) of the Rad/Nuc Med Reports file (#74).</p>
<p>Data comes with this file. It is ADDed ONLY IF NEW to the site's existing entries.</p>
<p>Patch RA*5.0*97 added the following Diagnostic Codes to this file:<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></p>
<blockquote>
<p>1100 BI-RADS CATEGORY 0</p>
<p>1101 BI-RADS CATEGORY 1</p>
<p>1102 BI-RADS CATEGORY 2</p>
<p>1103 BI-RADS CATEGORY 3</p>
<p>1104 BI-RADS CATEGORY 4</p>
<p>1105 BI-RADS CATEGORY 5</p>
<p>1106 BI-RADS CATEGORY 6</p>
<p>1200 ABDOMINAL AORTIC ANEURYSM NOT PRESENT</p>
<p>1201 ABDOMINAL AORTIC ANEURYSM PRESENT</p>
<p>1202 DOES NOT SATISFY SCREEN FOR AAA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>78.4</p>
<p>Film Sizes</p></td>
<td><p>^RA(78.4</p>
<p>This file contains the allowable film sizes that the technologist can choose from when entering the film data for an exam.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>78.6</p>
<p>Camera/Equip/Rm</p></td>
<td><p>^RA(78.6</p>
<p>This file contains all the rooms that may be used to perform imaging examinations. The Imaging Locations file (#79.1) uses this file to indicate which rooms are allowable choices when the technologist attaches a camera/equipment/room to an exam that is performed.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>78.7</p>
<p>Label Print Fields</p></td>
<td><p>^RA(78.7</p>
<p>This file contains the names of the data fields that can be printed on a flash card, exam label, jacket label, report header and report footer. The formats indicating which fields to print are stored in the Lbl/Hdr/Ftr Formats file (#78.2).</p>
<p>Data comes with this file. It OVERWRITE's existing entries in the site's data.</p></td>
</tr>
<tr class="even">
<td><p>79</p>
<p>Rad/Nuc Med Division</p></td>
<td><p>^RA(79</p>
<p>The package is designed to handle multiple divisions within a medical center. This file contains, for each division entry, parameters that the package uses during various stages of exam and report processing.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="odd">
<td><p>79.1</p>
<p>Imaging Locations</p></td>
<td><p>^RA(79.1</p>
<p>Within an imaging division there may be a number of physical locations where an imaging procedure can be performed. This file contains for each imaging location entry, parameters that the module uses during various stages of exam and report processing and inquiring.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>79.2</p>
<p>Imaging Type</p></td>
<td><p>^RA(79.2</p>
<p>This file contains for each imaging type entry parameters that the package uses during various stages of exam and report processing.</p>
<p>Data comes with the file. It is MERGE'd with existing entries.<a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></p></td>
</tr>
<tr class="odd">
<td><p>79.3</p>
<p>HL7 Message Exceptions <a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></p></td>
<td><p>^RA(79.3</p>
<p>This file contains details of HL7 messages from Sending Applications that have been rejected by Rad/Nuc Med.</p>
<p>No data comes with this file.</p></td>
</tr>
<tr class="even">
<td><p>79.7</p>
<p>Rad/Nuc Med HL7 Application Exceptions <a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a></p></td>
<td><p>^RA(79.7</p>
<p>This file contains parameters related to application exceptions in processing of HL7 Radiology messages.</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch RA*5*3 April 1999<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>PatchRA*5*97 August 2009: Added BI-RADS and AAA codes to DIAGNOSTIC CODES file (#78.3).<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Patch RA*5*64 July 2006: Added scaling factor description to File #79.2<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>Patch RA*5*12 December 1999<a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5"><p> Patch RA*5*81 June 2007: Added File #79.7 – Rad/Nuc Med HL7 Application Exceptions<a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Table 11 - Print Templates

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p>Table 12 - List Templates</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 37%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FILE</strong></th>
<th><strong>NAME</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>70</td>
<td>RA DIAGNOSTIC BY CASE</td>
<td>This template is used by the Diagnostic Code Entry by Case No. option.</td>
</tr>
<tr class="even">
<td>70</td>
<td>RA EXAM EDIT</td>
<td>This template is used to edit exams.</td>
</tr>
<tr class="odd">
<td>70</td>
<td>RA LAST PAST VISIT</td>
<td>This template is used when adding the last visit prior to implementing the VistA Radiology/Nuclear Medicine package.</td>
</tr>
<tr class="even">
<td>70</td>
<td>RA NO PURGE SPECIFICATION</td>
<td>This template is used to set the no purge flag for an exam in the Indicate No Purging of an Exam/report option. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] &amp; ‘Indicate No Purging of an Exam/report’ [RA PURGE] options.</td>
</tr>
<tr class="odd">
<td>70</td>
<td>RA OUTSIDE ADD</td>
<td>This template is used to enter outside films for tracking purposes.</td>
</tr>
<tr class="even">
<td>70</td>
<td>RA OUTSIDE EDIT</td>
<td>This template is used to edit information on outside film tracking.</td>
</tr>
<tr class="odd">
<td>70</td>
<td>RA OUTSIDE SUPEROK</td>
<td>This template is used to flag an outside film as needing a supervisor's concurrence in order to be released.</td>
</tr>
<tr class="even">
<td>70</td>
<td>RA OVERRIDE</td>
<td>This template is used to override the status of an exam and set it to Complete.</td>
</tr>
<tr class="odd">
<td>70</td>
<td>RA REGISTER</td>
<td>This template is used to register patients for exams. It is compiled into the RACTRG* routines.</td>
</tr>
<tr class="even">
<td>70</td>
<td>RA STATUS CHANGE</td>
<td>This template is used for the Status Tracking of Exams option.</td>
</tr>
<tr class="odd">
<td>71</td>
<td>RA PRO MAP</td>
<td>Used in mapping the file 71 to file 71.99</td>
</tr>
<tr class="even">
<td>71</td>
<td>RA PROCEDURE EDIT</td>
<td><p>This template is used to enter and edit procedures.</p>
<p>There is an option to select a Master Radiology Procedure File (MRPF) entry when a CPT code is associated with a “DETAILED” Type procedure.</p></td>
</tr>
<tr class="odd">
<td>71.3</td>
<td>RA COMMON PROCEDURE EDIT</td>
<td>This template is used to set up and change the common procedure display used when requesting an exam.</td>
</tr>
<tr class="even">
<td>72</td>
<td>RA STATUS ENTRY</td>
<td>This template is used to enter and edit a status for an exam.</td>
</tr>
<tr class="odd">
<td>74</td>
<td>RA PRE-VERIFY REPORT EDIT</td>
<td>This template is used by interpreting resident physicians to edit and pre-verify their reports.</td>
</tr>
<tr class="even">
<td>74</td>
<td>RA PRE-VERIFY REPORT ONLY</td>
<td>This template is used by interpreting resident physicians to pre-verify their reports only.</td>
</tr>
<tr class="odd">
<td>74</td>
<td>RA REPORT EDIT</td>
<td>This template is used to enter and edit reports in File #74. It is compiled into the RACTWR* routines.</td>
</tr>
<tr class="even">
<td>74</td>
<td>RA VERIFY REPORT ONLY</td>
<td>This template is used to verify reports in File #74. It is compiled into the RACTVR* routines.</td>
</tr>
<tr class="odd">
<td>74.1</td>
<td>RA STANDARD REPORT ENTRY</td>
<td>This template is used to enter standard reports into File #74.</td>
</tr>
<tr class="even">
<td>74.3</td>
<td>RA DISTRIBUTION EDIT</td>
<td>This template is used in the Reports Distribution Edit option.</td>
</tr>
<tr class="odd">
<td>74.3</td>
<td>RA DISTRIBUTION LOG</td>
<td>This template is used to enter data in the activity log of File #74.3.</td>
</tr>
<tr class="even">
<td>75.1</td>
<td>RA OERR EDIT</td>
<td>This template is to edit requests by OE/RR V. 2.5 users. It is compiled into the RACTOE* routines.</td>
</tr>
<tr class="odd">
<td>75.1</td>
<td>RA ORDER EXAM</td>
<td>This template is used to request an exam.</td>
</tr>
<tr class="even">
<td>75.1</td>
<td>RA QUICK EXAM ORDER</td>
<td>This template is used by OE/RR V. 2.5 users for ordering an exam. It is compiled into the RACTQE* routines.</td>
</tr>
<tr class="odd">
<td>78.2</td>
<td>RA FLASH CARD EDIT</td>
<td>This template is used to enter and edit flash cards, jacket labels, exam labels, report headers and report footers.</td>
</tr>
<tr class="even">
<td>79</td>
<td>RA DIVISION PARAMETERS</td>
<td>This template is used to enter division parameters for the package.</td>
</tr>
<tr class="odd">
<td>79.1</td>
<td>RA LOCATION PARAMETERS</td>
<td>This template is used to enter the location parameters for the package.</td>
</tr>
<tr class="even">
<td>79.1</td>
<td>RA SITE MANAGER</td>
<td>This template is used by the IRM Service to define input and printing devices for the package.</td>
</tr>
<tr class="odd">
<td>79.2</td>
<td>RA IMAGE PARAMETERS</td>
<td>This template is used to enter parameters for an imaging type.</td>
</tr>
<tr class="even">
<td>79.2</td>
<td>RA ON-LINE CRITERIA</td>
<td>This template is used to enter data associated with the storing of on-line data for an imaging location.</td>
</tr>
<tr class="odd">
<td>200</td>
<td>RA PERSONNEL</td>
<td>This template is used to enter Radiology/ Nuclear Medicine personnel into the package.</td>
</tr>
</tbody>
</table>

Table 12 - List Templates

### Sort Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE | NAME                    | DESCRIPTION                                                                                        |
|----------|-----------------------------|--------------------------------------------------------------------------------------------------------|
| 70       | RA DAILY LOG                | This template is used to sort exams by exam date and hospital division.                                |
| 70       | RA OUTSIDE LIST             | This template is used to sort the outside film registry.                                               |
| 71       | RA ALPHA LIST OF ACTIVES    | This template is used to determine which procedures are active and put them in alphabetical order.     |
| 71       | RA PROCEDURES BY AMIS       | This template is used to sort procedures by major AMIS code.                                           |
| 71       | RA PROCEDURES BY AMIS CODES | This template sorts procedures by AMIS code and then by CPT code.                                      |
| 71       | RA SERIES ONLY              | This template is used to sort procedures by "Series" type only.                                        |
| 74.4     | RA ALL UNPRINTED            | This template is used to sort the Unprinted Reports List for the report distribution queue.            |
| 74.4     | RA CLINIC BY PRINT DATE     | This template sorts the distribution queue by clinic location. Also, it sorts reports by print status. |
| 74.4     | RA WARD BY PRINT DATE       | This template sorts reports in the ward distribution queue by print date.                              |
| 75.1     | RA REQ REJECTED SORT        | This template sorts orders by date desired.                                                            |
| 78.2     | RA FLASH PRINT              | This template sorts the print formats by name for printing label set-ups.                              |
| 79.1     | RA EXAM ROOM LIST           | This template sorts examination rooms by Radiology/Nuclear Medicine location.                          |
| 79.1     | RA IMAGE LOC LIST           | This template is used to sort location parameters by imaging location.                                 |
| 200      | RA PERSONNEL LIST           | This template sorts Radiology/Nuclear Medicine personnel by classification (e.g., technologist).       |

Table 13 - External Relations

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| FILE | NAME                 | DESCRIPTION                                                                                                                                                             |
|----------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 70       | RA DAILY LOG             | This template is used to print a daily log of registered examinations.                                                                                                      |
| 70       | RA OUTSIDE LIST          | This template is used to generate the Delinquent Outside Film Report for outpatients.                                                                                       |
| 71       | RA ALPHA LIST OF ACTIVES | This template produces an alphabetic listing of all active Radiology/Nuclear Medicine procedures.                                                                           |
| 71       | RA PROCEDURE BY AMIS     | This template is used to generate the Short Active Procedure List.                                                                                                          |
| 71       | RA PROCEDURE LIST        | This template is used to generate the Long Procedure List.                                                                                                                  |
| 71       | RA PROCEDURE SHORT LIST  | This template is used to generate the Inactive Short Procedure List.                                                                                                        |
| 74.1     | RA STANDARD REPORTS LIST | This template is used in the Standard Reports Print option.                                                                                                                 |
| 74.3     | RA DISTRIBUTION          | This template is used in the Report Distribution List.                                                                                                                      |
| 74.4     | RA ALL UNPRINTED REPORTS | This template is used to generate a list of reports in the distribution queue that have not been printed.                                                                   |
| 74.4     | RA PRINTED REPORTS       | This template is used in the List Reports in a Batch option.                                                                                                                |
| 74.4     | RA UNPRINTED REPORTS     | This template is used to generate reports in the distribution queue that have not yet been printed                                                                          |
| 75.1     | RA REQ REJECTED PRINT    | This template generates reports that identify orders rejected by CPRS within a date range determined by the date desired.                                                   |
| 78.2     | RA FLASH PRINT           | This template is used to generate the Flash Card/Label List.                                                                                                                |
| 78.3     | RA DIAGNOSTIC CODE PRINT | This template is used to print the Diagnostic Code List.                                                                                                                    |
| 78.4     | RA FILM SIZE             | This template is used to provide information about types of film (e.g., inactivation date).                                                                                 |
| 79       | RA IMAGE DIV LIST        | This template is used to generate a list of divisions.                                                                                                                      |
| 79.1     | RA EXAM ROOM LIST        | This template is used to generate an exam room list.                                                                                                                        |
| 79.1     | IMAGE LOC LIST           | This template is used to generate a list of imaging locations.                                                                                                              |
| 79.2     | RA ACTIVITY LOG          | This template is used to print the activity log from File \#79.2.                                                                                                           |
| 200      | RA PERSONNEL LIST        | This template is used to generate a list of personnel who have a Radiology/Nuclear Medicine classification and their inactivation date, if applicable.                      |
| 200      | RA RESIDENT RADIOLOGIST  | This template is used to generate a list of personnel who have a Radiology/Nuclear Medicine classification, their inactivation date and whether a staff review is required. |

Table 14 - Package-Wide Variables

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|           |                   |                                                                                                                       |
|-----------|-------------------|-----------------------------------------------------------------------------------------------------------------------|
| FILE  | NAME          | DESCRIPTION                                                                                                       |
| 79.3[^35] | RA HL7 EXCEPTIONS | This template is used to display and print HL7 messages which have been rejected by VistA Radiology/Nuclear Medicine. |

Table 15 - Glosary Terms

# # Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Exported Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM Menu \[RA SITEMANAGER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Device Specifications for Imaging Locations \[RA DEVICE\]

Distribution Queue Purge \[RA RPTDISTPURGE\]

Failsoft Parameters \[RA FAILSOFT\]

Imaging Type Activity Log \[RA IMGLOG\]

Rebuild Distribution Queues \[RA RPTDISTREBUILD\]

Report File x-ref Clean-up Utility \[RA RPTDISTREBUILD\] [^36]

Site Accession Number Set-up \[RA SITEACCNUM\][^37]

Credit Completed Exams for an Imaging Location [^38]

Enable HL7 reprocessing for locked studies \[RASAN ENABLE REPROCESSING\]

Resource Device Specifications for Division \[RA RESOURCE DEVICE\]

Schedule Perf Indic Summary for 15<sup>th</sup> of month \[RA PERFORMIN SCHEDULE\] [^39]

Template Compilation \[RA COMPILE TEMPLATES\]

### Rad/Nuc Med Total System Menu \[RA OVERALL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam Entry/Edit Menu \[RA EXAMEDIT\]

> Add Exams to Last Visit \[RA ADDEXAM\]

> Cancel an Exam \[RA CANCEL\]

> Case No. Exam Edit \[RA EDITCN\]

> Diagnostic Code and Interpreter Edit by Case No. \[RA DIAGCN\]

> Edit Exam by Patient \[RA EDITPT\]

> Enter Last Past Visit Before DHCP \[RA PAST\]

> Exam Status Display \[RA STATLOOK\]

> Register Patient for Exams \[RA REG\]

> Status Tracking of Exams \[RA STATRACK\]

> Switch Locations \[RA LOC SWITCH\]

> View Exam by Case No. \[RA VIEWCN\]

Films Reporting Menu \[RA RPT\]

Batch Reports Menu \[RA BTCH\]

> Add/Remove Report From Batch \[RA BTCHREMOVE\]

> Create a Batch \[RA BTCHNEW\]

> Delete Printed Batches \[RABTCHDEL\]

> List Reports in a Batch \[RA BTCHLIST\]

> Print a Batch of Reports \[RA BTCHPRINT\]

> Verify Batch \[RA BTCHVERIFY\] \*\*LOCKED: RA VERIFY\*\*

> Display a Rad/Nuc Med Report \[RA RPTDISP\]

> Distribution Queue Menu \[RA RPTDIST\]

> Activity Logs \[RA RPTDISTACTIVITY\]

> Clinic Distribution List \[RA RPTDISTLISTCLINIC\]

> Individual Ward \[RA RPTDISTSINGLEWARD\]

> Print By Routing Queue \[RA RPTDISTQUE\]

> Report's Print Status \[RA RPTDISTPRINTSTATUS\]

> Single Clinic \[RA RPTDISTSINGLECLINIC\]

> Unprinted Reports List \[RA RPTDISTLISTUNPRINTED\]

> Ward Distribution List \[RA RPTDISTLISTWARD\]

Draft Report (Reprint) \[RA REPRINT\]

On-line Verifying of Reports \[RA RPTONLINEVERIFY\] \*\*LOCKED: RA VERIFY\*\*

Outside Report Entry/Edit \[RA OUTSIDE RPTENTRY\] [^40]

Report Entry/Edit \[RA RPTENTRY\]

Resident On-Line Pre-Verification \[RA RESIDENT PRE-VERIFY\]

Select Report to Print by Patient \[RA RPTPAT\]

Switch Locations \[RA LOC SWITCH\]

Verify Report Only \[RA RPTVERIFY\] \*\*LOCKED: RA VERIFY\*\*

Management Reports Menu \[RA MGTRPTS\]

> Daily Management Reports \[RA DAILYRPTS\]

> Abnormal Exam Report \[RA ABNORMAL\]

> Complication Report \[RA COMPLICATION\]

> Daily Log Report \[RA LOG\]

> Delinquent Outside Film Report for Outpatients \[RA OUTSIDERPT\]

> Delinquent Status Report \[RA DELINQUENT\]

> Examination Statistics \[RA DAISTATS\]

> Incomplete Exam Report \[RA INCOMPLETE\]

> Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

> Radiopharmaceutical Usage Report \[RA RADIOPHARM USAGE\]

> Unverified Reports \[RA DAIUVR\]

Functional Area Workload Reports \[RA LWKL\]

> Clinic Report \[RA LWKLCLINIC\]

> PTF Bedsection Report \[RA LWKLBEDSEC\]

> Service Report \[RA LWKLSERVICE\]

> Sharing Agreement/Contract Report \[RA LWKLSHARING\]

> Ward Report \[RA LWKLWARD\]

Personnel Workload Reports \[RA WKL\] [^41]

> Physician CPT Report by Imaging Type \[RA WKLIPHY CPT ITYPE\]

> Physician Report \[RA WKLPHY\]

> Physician scaled wRVU Report by Imaging Type \[RA WKLIPHY SWRVU ITYPE\]

> Physician scaled wRVU Report by CPT \[RA WKLIPHY SWRVU CPT\]

> Physician wRVU Report by CPT \[RA WKLIPHY WRVU CPT\]

> Physician wRVU Report by Imaging Type \[RA WKLIPHY WRVU ITYPE\]

> Radiopharmaceutical Administration Report \[RA RADIOPHARM ADMIN\]

> Resident Report \[RA WKLRES\]

> Staff Report \[RA WKLSTAFF\]

> Technologist Report \[RA WKLTECH\]

> Transcription Report \[RA TRANSRIP REPORT\]

Special Reports \[RA SPECRPTS\] [^42]

> AMIS Code Dump by Patient \[RA AMISDUMP\]

> AMIS Report \[RA AMIS\]

> Camera/Equip/Rm Report \[RA WKLROOM\]

> Cost Distribution Report \[RA CDR REPORT\]

> Detailed Procedure Report \[RA WKLPROCEDURE\]

> Film Usage Report \[RA FILMUSE\]

> Procedure Scaled wRVU/CPT Report \[RA PROC CPTSWRVU\]

> Procedure wRVU/CPT Report \[RA PROC CPTWRVU\]

> Procedure/CPT Statistics Report \[RA CPTSTATS\]

> Radiation Dose Summary Report \[RA RAD DOSE SUMMARY\]

> Status Time Report \[RA STATRPT\]

> Wasted Film Report \[RA WASTED FILM RPT\]

Timeliness Reports \[RA TIMELINESS MENU\] [^43]<sup>,</sup>[^44]

> Outpatient Procedure Wait Time \[RA TIMELINESS OUTPATIENT MENU\]

> Summary/Detail report \[RA TIMELINESS REPORT\]

Verification Timeliness \[RA TIMELINESS VER MENU\] [^45]

> Enter/Edit OUTLOOK mail group \[RA PERFORMIN MAIL GROUP ENTRY\]

> Run Previous Month's Summary Report \[RA PERFORMIN TASKLM\] [^46]

> Summary/Detail report \[RA PERFORMIN RPTS\]

Outside Films Registry Menu \[RA OUTSIDE\]

> Add Films to Registry \[RA OUTADD\]

> Delinquent Outside Film Report for Outpatients \[RA OUTSIDERPT\]

> Edit Registry \[RA OUTEDIT\]

> Flag Film to Need 'OK' Before Return \[RA OUTFLAG\]

> Outside Films Profile \[RA OUTPROF\]

Patient Profile Menu \[RA PROFILES\]

> Detailed Request Display \[RA ORDERDISPLAY\]

> Display Patient Demographics \[RA PROFDEMOS\]

> Exam Profile (selected sort) \[RA PROFSORT\]

> Exam Profile with Radiation Dosage Data \[RA PROFRAD DOSE\]

> Outside Films Profile \[RA OUTPROF\]

> Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]

Menu of Request Log Options ... \[RA ORDERLOG MENU\]

> Log of Discontinued Requests \[RA ORDER DISCONTINUED\]

> Log of CPRS Rejected Requests by Date Desired \[RA ORDERLOG REJECTED\]

> Pending/Hold Rad/Nuc Med Request Log \[RA ORDERPENDING\]

> Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

> Ward/Clinic Scheduled Request Log \[RA ORDERLOGLOC\]

Refer Selected Requests to COMMUNITY CARE Provider \[RA ORDERREF\]

Cancel a Request \[RA ORDERCANCEL\]

Detailed Request Display \[RA ORDERDISPLAY\]

Hold a Request \[RA ORDERHOLD\]

Print Rad/Nuc Med Requests by Date \[RA ORDERPRINTS\]

Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

Rad/Nuc Med Procedure Information Look-Up \[RA DISPLAY IMAGPROCINFO\]

Request an Exam \[RA ORDEREXAM\]

Schedule a Request \[RA ORDERSCHEDULE\]

> Update a Hold Request \[RA ORDERREASON UPDATE\]

Supervisor Menu \[RA SUPERVISOR\]

> Radiology HL7 Menu \[RA HL7 MENU\] [^47]

> Rad/Nuc Med HL7 Voice Reporting Errors \[RA HL7 VOICE REPORTING ERRORS\]

> Resend Radiology HL7 Message \[RA HL7 MESSAGE RESEND\] \*\*LOCKED: RA MGR\*\*

> Resend Radiology HL7 Message by Date Range \[RA HL7 RESEND BY DATE RANGE\] [^48]

> Radiology Study Tracker Menu \[MAGD RAD STUDY TRACKER\]

> Check a Radiology or Consult Study for Images \[MAGD ACN CHECK\]

> Report Radiology Studies without Images \[MAGD RAD RANGE CHECK\]

> \*\*Locked with MAGD QR REPORT

> DICOM Query Client \[MAGD QUERY\]

> DICOM Query/Retrieve Client \[MAGD QUERY/RETRIEVE\]

> \*\*\> Locked with MAGD QR MANUAL RETRIEVE

> Compare Radiology Image Count on PACS with VistA \[MAGD RAD COUNT COMPARE\] \*\*Locked with MAGD QR REPORT

> Retrieve Missing Radiology Images from PACS \[MAGD RAD AUTO RETRIEVE\] \*\*Locked with MAGD QR AUTO RETRIEVE

> Display stats for automatic radiology Q/R runs \[MAGD Q/R RAD RUN STATI

> STICS\]

> Delete the stats for automatic radiology Q/R runs \[MAGD RAD STATISTICS

> DELETE\] \*\*Locked with MAG SYSTEM

> Stop automatic Q/R processes \[MAGD STOP AUTOMATIC PROCESSES\]

> \*\*Locked with MAGD QR REPORT

> Rad/Nuc Med Report Management \[RA REPORT MANAGEMENT\]

> Delete a Report \[RA DELETERPT\] \*\*Locked with RA RPTMGR

> Restore a Deleted Report \[RA RESTORE REPORT\] \*\*Locked with RA RPTMGR

> Unverify a Report for Amendment \[RA UNVERIFY\] \*\*Locked with RA RPTMGR

> Access Uncorrected Reports \[RA UNCORRECTED REPORTS\]

> Delete Printed Batches By Date \[RA BTCHDELDATE\]\*\* LOCKED: RA MGR\*\*

> Exam Deletion \[RA DELETEXAM\] \*\*LOCKED: RA MGR\*\*

> Inquire to File Entries \[DIINQUIRE\]

> List Exams with Inactive/Invalid Statuses \[RA INVALID EXAM STATUSES}

> Maintenance Files Print Menu \[RA MAINTENANCEP\]

> Complication Type List \[RA COMPRINT\]

> Diagnostic Code List \[RA DIAGP\]

> Examination Status List \[RA EXAMSTATUSP\]

> Film Sizes List \[RA FILMP\]

> Label/Header/Footer Format List \[RA FLASHFORMP\]

> Major AMIS Code List \[RA MAJORAMISP\]

> Modifier List \[RA MODIFIERP\]

> Nuclear Medicine List Menu \[RA NM PRINT MENU\]

> Lot (Radiopharmaceutical) Number List \[RA NM PRINT LOT\]

> Route of Administration List \[RA NM PRINT ROUTE\]

> Site of Administration List \[RA NM PRINT SITE\]

> Vendor/Source (Radiopharmaceutical) List \[RA NM PRINT SOURCE\]

Procedure File Listings \[RA PROCLISTS\]

> Display Rad/NM Procedure Contrast Media History \[RA CMAUDIT HISTORY\] [^49]

> Active Procedure List (Long) \[RA PROCLONG\]

> Active Procedure List (Short) \[RA PROCSHORT\]

> Alpha Listing of Active Procedures \[RA ALPHALIST\]

> Barcoded Procedure List \[RA BARPROCPRINT\]

> Inactive Procedure List (Long) \[RA INACPRCLONG\]

> Invalid CPT/Stop Code List \[RA INVALID CPT/STOP\]

> List of Inactive Procedures (Short) \[RA INACPRCSHORT\]

> List of Procedures with Contrast \[RA PROCMEDIA\] [^50]

> Parent Procedure List \[RA PROCPARENT\]

> Procedure Message List \[RA PROCMSGPRINT\]

> Series of Procedures List \[RA PROCSERIES\]

> Report Distribution Lists \[RA DISTP\]

> Sharing Agreement/Contract List \[RA SHARINGP\]

> Standard Reports Print \[RA STANDPRINT\]

> VistaRad Category Print \[RA VISTARAD CATEGORY P\] [^51]

Override a Single Exam Status to 'complete' \[RA OVERRIDE\]\*\*LOCKED: RA MGR\*\*

Print File Entries \[DIPRINT\]

Rad/Nuc Med Personnel Menu \[RA PNL\]

> Classification Enter/Edit \[RA PNLCLASS\]

> Clerical List \[RA PNLCLERK\]

> Interpreting Resident List \[RA PNLRES\]

> Interpreting Staff List \[RA PNLSTAFF\]

> Technologist List \[RA PNLTECH\]

Search File Entries \[DISEARCH\]

Switch Locations \[RA LOC SWITCH\]

System Definition Menu \[RA SYSDEF\]

> Camera/Equip/Rm Entry/Edit \[RA SYSEXROOM\]

> Division Parameter Set-up \[RA SYSDIV\]

> Inactivate a Location \[RA SYSINACT\]

> List of Cameras/Equip/Rms \[RA SYSEXLIST\]

> Location Parameter List \[RA SYSLOCLIST\]

> Location Parameter Set-up \[RA SYSLOC\]

> Outside Location Order Suppression \[RA SYSUPLOC\]

> Print Division Parameter List \[RA SYSDIVLIST\]

Update Exam Status \[RA UPDATEXAM\]

Utility Files Maintenance Menu \[RA MAINTENANCE\]

> Complication Type Entry/Edit \[RA COMPEDIT\]

> Diagnostic Code Enter/Edit \[RA DIAGEDIT\]

> Examination Status Entry/Edit \[RA EXAMSTATUS\]

> Film Type Entry/Edit \[RA FILMEDIT\]

> HL7 Interface Exceptions List \[RA HL7 EXCEPTIONS\] [^52]

> Label/Header/Footer Formatter \[RA FLASHFORM\]

> Major AMIS Code Entry/Edit \[RA MAJORAMIS\]

> Nuclear Medicine Setup Menu \[RA NM EDIT MENU\]

> Lot (Radiopharmaceutical) Number Enter/Edit \[RA NM EDIT LOT\]

> Route of Administration Enter/Edit \[RA NM EDIT ROUTE\]

> Site of Administration Enter/Edit \[RA NM EDIT SITE\]

> Vendor/Source (Radiopharmaceutical) Enter/Edit \[RA NM EDIT SOURCE\]

> Order Entry Procedure Display Menu \[RA ORDERDISPLAY MENU\]

> Common Procedure Enter/Edit \[RA COMMON PROCEDURE\]

> Create OE/RR Protocol from Common Procedure \[RA CREATE OE/RR PROTOCOL\]

> Display Common Procedure List \[RA DISPLAY COMMON PROCEDURES\]

> Procedure Edit Menu \[RA PROCEDURE EDIT MENU\]

> Activate/Inactivate Standard Procedures \[RA PROCEDURE ACTIVATE\]

> Cost of Procedure Enter/Edit \[RA PROCOSTEDIT\]

> Procedure Enter/Edit \[RA PROCEDURE\]

> Procedure Message Entry/Edit \[RA PROCMSGEDIT\]

> Procedure Modifier Entry \[RA MODIFIER\]

> Reports Distribution Edit \[RA DISTEDIT\]

> Sharing Agreement/Contract Entry/Edit \[RA SHARING\]

> Standard Reports Entry/Edit \[RA STANDRPTS\]

> Valid Imaging Stop Codes Edit \[RA VALID STOP CODES\] \*\*LOCKED: RA MGR\*\*

VistaRad Category Entry/Edit \[RA VISTARAD CATEGORY E\] [^53]

Update Patient Record \[RA PTEDIT\]

User Utility Menu \[RA USERUTL\]

SYN Synch Exams with CPRS & RIS Orders \[RA EXAM ORDER SYNCH\]

\*\*\>Locked with RA MGR

> Duplicate Dosage Ticket \[RA DOSAGE TICKET\]

> Duplicate Flash Card \[RA FLASH\]

> Jacket Labels \[RA LABELS\]

> Print Worksheets \[RA WORKSHEETS\]

> Set preference for Long Display of Procedures \[RA SET PREFERENCE LONG DISPLAY\] [^54]

> Switch Locations \[RA LOC SWITCH\]

> Test Label Printer \[RA LABELTEST\]

### Rad/Nuc Med Clerk Menu \[RA CLERKMENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add Exams to Last Visit \[RA ADDEXAM\]

Cancel an Exam \[RA CANCEL\]

Case No. Exam Edit \[RA EDITCN\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Display Patient Demographics \[RA PROFDEMOS\]

Duplicate Flash Card \[RA FLASH\]

Exam Status Display \[RA STATLOOK\]

Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]

> Refer Selected Requests to COMMUNITY CARE Provider \[RA ORDERREF\]

> Cancel a Request \[RA ORDERCANCEL\]

> Detailed Request Display \[RA ORDERDISPLAY\]

> Hold a Request \[RA ORDERHOLD\]

> Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

> Pending/Hold Rad/Nuc Med Request Log \[RA ORDERPENDING\]

> Print Rad/Nuc Med Requests by Date \[RA ORDERPRINTS\]

> Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

> Rad/Nuc Med Procedure Information Look-Up \[RA DISPLAY IMAGPROCINFO\]

> Request an Exam \[RA ORDEREXAM\]

> Schedule a Request \[RA ORDERSCHEDULE\]

> Update a Hold Request \[RA ORDERREASON UPDATE\]

> Ward/Clinic Scheduled Request Log \[RA ORDERLOGLOC\]

Register Patient for Exams \[RA REG\]

Switch Locations \[RA LOC SWITCH\]

View Exam by Case No. \[RA VIEWCN\]

### Rad/Nuc Med Ward Clerk Menu \[RA WARD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cancel a Request \[RA ORDERCANCEL\]

Detailed Request Display \[RA ORDERDISPLAY\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Request an Exam \[RA ORDEREXAM\]

Ward/Clinic Scheduled Request Log \[RA ORDERLOGLOC\]

### Rad/Nuc Med File Room Clerk Menu \[RA FILERM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed Request Display \[RA ORDERDISPLAY\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Display Patient Demographics \[RA PROFDEMOS\]

Outside Films Registry Menu \[RA OUTSIDE\]

> Add Films to Registry \[RA OUTADD\]

> Delinquent Outside Film Report for Outpatients \[RA OUTSIDERPT\]

> Edit Registry \[RA OUTEDIT\]

> Flag Film To Need 'OK' Before Return \[RA OUTFLAG\]

> Outside Films Profile \[RA OUTPROF\]

Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Select Report to Print by Patient \[RA RPTPAT\]

User Utility Menu \[RA USERUTL\]

SYN Synch Exams with CPRS & RIS Orders \[RA EXAM ORDER SYNCH\]

\*\*\> Locked with RA MGR

> Duplicate Dosage Ticket \[RA DOSAGE TICKET\]

> Duplicate Flash Card \[RA FLASH\]

> Jacket Labels \[RA LABELS\]

> Print Worksheets \[RA WORKSHEETS\]

> Switch Locations \[RA LOC SWITCH\]

> Test Label Printer \[RA LABELTEST\]

View Exam by Case No. \[RA VIEWCN\]

Ward/Clinic Scheduled Request Log \[RA ORDERLOGLOC\]

### Interpreting Physician Menu \[RA RADIOLOGIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed Request Display \[RA ORDERDISPLAY\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Draft Report (Reprint) \[RA REPRINT\]

On-line Verifying of Reports \[RA RPTONLINEVERIFY\] \*\*LOCKED: RA VERIFY\*\*

Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Resident On-Line Pre-Verification \[RA RESIDENT PRE-VERIFY\]

Select Report to Print by Patient \[RA RPTPAT\]

Switch Locations \[RA LOC SWITCH\]

View Exam by Case No. \[RA VIEWCN\]

### Reports Menu \[RA REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Abnormal Exam Report \[RA ABNORMAL\]

Complication Report \[RA COMPLICATION\]

Daily Log Report \[RA LOG\]

Delinquent Outside Film Report for Outpatients \[RA OUTSIDERPT\]

Delinquent Status Report \[RA DELINQUENT\]

Duplicate Flash Card \[RA FLASH\]

Film Usage Report \[RA FILMUSE\]

Functional Area Workload Reports \[RA LWKL\]

> Clinic Report \[RA LWKLCLINIC\]

> PTF Bedsection Report \[RA LWKLBEDSEC\]

> Service Report \[RA LWKLSERVICE\]

> Sharing Agreement/Contract Report \[RA LWKLSHARING\]

> Ward Report \[RA LWKLWARD\]

Jacket Labels \[RA LABELS\]

Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

Personnel Workload Reports \[RA WKL\] [^55]

> Physician CPT Report by Imaging Type \[RA WKLIPHY CPT ITYPE\]

> Physician Report \[RA WKLPHY\]

> Physician scaled wRVU Report by Imaging Type \[RA WKLIPHY SWRVU ITYPE\]

> Physician scaled wRVU Report by CPT \[RA WKLIPHY SWRVU CPT\]

> Physician wRVU Report by CPT \[RA WKLIPHY WRVU CPT\]

> Physician wRVU Report by Imaging Type \[RA WKLIPHY WRVU ITYPE\]

> Radiopharmaceutical Administration Report \[RA RADIOPHARM ADMIN\]

> Resident Report \[RA WKLRES\]

> Staff Report \[RA WKLSTAFF\]

> Technologist Report \[RA WKLTECH\]

> Transcription Report \[RA TRANSCRIP REPORT\]

Print Worksheets \[RA WORKSHEETS\]

Status Time Report \[RA STATRPT\]

Test Label Printer \[RA LABELTEST\]

### Rad/Nuc Med Secretary Menu \[RA SECRETARY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Draft Report (Reprint) \[RA REPRINT\]

Rad/Nuc Med Personnel Menu \[RA PNL\]

> Classification Enter/Edit \[RA PNLCLASS\]

> Clerical List \[RA PNLCLERK\]

> Interpreting Resident List \[RA PNLRES\]

> Interpreting Staff List \[RA PNLSTAFF\]

> Technologist List \[RA PNLTECH\]

Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]

> Cancel a Request \[RA ORDERCANCEL\]

> Detailed Request Display \[RA ORDERDISPLAY\]

> Hold a Request \[RA ORDERHOLD\]

> Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

> Pending/Hold Rad/Nuc Med Request Log \[RA ORDERPENDING\]

> Print Rad/Nuc Med Requests by Date \[RA ORDERPRINTS\]

> Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

> Rad/Nuc Med Procedure Information Look-Up \[RA DISPLAY IMAGPROCINFO\]

> Request an Exam \[RA ORDEREXAM\]

> Schedule a Request \[RA ORDERSCHEDULE\]

> Update a Hold Request \[RA ORDERREASON UPDATE\]

> Ward/Clinic Scheduled Request Log \[RA ORDERLOGLOC\]

Report Entry/Edit \[RA RPTENTRY\]

Select Report to Print by Patient \[RA RPTPAT\]

Switch Locations \[RA LOC SWITCH\]

Verify Batch \[RA BTCHVERIFY\] \*\*LOCKED: RA VERIFY\*\*

Verify Report Only \[RA RPTVERIFY\] \*\*LOCKED: RA VERIFY\*\*

View Exam by Case No. \[RA VIEWCN\]

### Rad/Nuc Med Technologist Menu \[RA TECHMENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add Exams to Last Visit \[RA ADDEXAM\]

Cancel an Exam \[RA CANCEL\]

Case No. Exam Edit \[RA EDITCN\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Duplicate Flash Card \[RA FLASH\]

Log of Scheduled Requests by Procedure \[RA ORDERLOG\]

Patient Profile Menu \[RA PROFILES\]

> Detailed Request Display \[RA ORDERDISPLAY\]

> Display Patient Demographics \[RA PROFDEMOS\]

> Exam Profile (selected sort) \[RA PROFSORT\]

> Outside Films Profile \[RA OUTPROF\]

> Profile of Rad/Nuc Med Exams \[RA PROFQUICK\]

Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

Register Patient for Exams \[RA REG\]

Status Tracking of Exams \[RA STATRACK\]

Switch Locations \[RA LOC SWITCH\]

View Exam by Case No. \[RA VIEWCN\]

### Rad/Nuc Med Transcriptionist Menu \[RA TRANSCRIPTIONIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Batch Reports Menu \[RA BTCH\]

> Add/Remove Report From Batch \[RA BTCHREMOVE\]

> Create a Batch \[RA BTCHNEW\]

> Delete Printed Batches \[RA BTCHDEL\]

> List Reports in a Batch \[RA BTCHLIST\]

> Print a Batch of Reports \[RA BTCHPRINT\]

> Verify Batch \[RA BTCHVERIFY\] \*\*LOCKED: RA VERIFY\*\*

Diagnostic Code and Interpreter Edit by Case No. \[RA DIAGCN\]

Display a Rad/Nuc Med Report \[RA RPTDISP\]

Draft Report (Reprint) \[RA REPRINT\]

Report Entry/Edit \[RA RPTENTRY\]

Select Report to Print by Patient \[RA RPTPAT\]

Standard Reports Entry/Edit \[RA STANDRPTS\]

## Single Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options do not appear on any menu:

- Rad/Nuc Med \[RA OERR EXAM\]
- Imaging Type Mismatch Report \[RA EXAM/STATUS ITYPE MISMATCH\]
- Autopurge of Distribution Queues \[RA RPTDISTAUTOPURGE\]
- Reprocess locked study accession error \[RA REPROC\] – This option should be scheduled to run and it will reprocess HL7 result messages that are rejected due to LOCK errors.

## Menu/Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RA SITEMANAGER menu may be assigned to the IRM staff member who supports this package. Descriptions of the RA SITEMANAGER options are in the Implementation and Maintenance section of this manual.

The RA OVERALL menu is the most extensive menu and may be assigned to the ADPAC.

All other menu and option assignments should be decided upon by the ADPAC. Descriptions of non-RA SITEMANAGER options may be found in the *ADPAC Guide* or *User Manual*.

## Protocols [^56]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are exported with this version:

RA CANCEL

RA CANCEL 2.3

RA CANCEL 2.4 [^57]

RA EVSEND OR

RA EXAMINED

RA EXAMINED 2.3

RA EXAMINED 2.4 [^58]

RA HL7 EXCEPTIONS DELETE [^59]

RA HL7 EXCEPTIONS MENU

RA HL7 EXCEPTIONS NEXT

RA HL7 EXCEPTIONS PREVIOUS

RA HL7 EXCEPTIONS PRINT

RA HL7 EXCEPTIONS RESEND

RA OERR DEFAULT PROTOCOL

RA OERR EXAM

RA OERR PROFILE

RA ORDERABLE ITEM UPDATE

RA PSCRIBE ORM

RA PSCRIBE ORU

RA PSCRIBE TCP REPORT

RA PSCRIBE TCP SERVER RPT

RA RECEIVE

RA REG

RA REG 2.3

RA REG 2.4 [^60]

RA RPT

RA RPT 2.3

RA RPT 2.4 [^61]

RA SCIMAGE ORM

RA SCIMAGE ORU

RA SCIMAGE TCP REPORT

RA SCIMAGE TCP SERVER RPT [^62]

RA SEND ORM

RA SEND ORU

RA TALKLINK ORM

RA TALKLINK ORU

RA TALKLINK TCP REPORT

RA TALKLINK TCP SERVER RPT

RA TCP ORM

RA TCP ORU

RA VOICE TCP REPORT

RA VOICE TCP SERVER RPT

## FileMan Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three FileMan namespaced options are exported with this software to allow users to inquire, print or search Radiology/Nuclear Medicine package files. They are:

- DIINQUIRE
- DIPRINT
- DISEARCH

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Radiology/Nuclear Medicine package does not provide for the archiving of its data.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the latest information on active supported references, use the Custodial Package menu under the DBA's Integration Agreement menu on FORUM.

Select DBA Option: integration Agreements Menu

O Instructions for Entering IA's

1 Get New Integration \#'s

2 Add/Edit

3 Inquire

4 Roll-up into Mail Message

5 File Agreements Menu ...

6 Routine Agreements Menu ...

7 Subscriber Package Menu ...

8 Custodial Package Menu ...

9 Print Other

10 Print Pending

11 Print Active

12 Print All

13 Supported References Menu ...

14 Private References Menu ...

15 Controlled Subscription References Menu ...

16 Agreement Lookup by Variable

Select Integration Agreements Menu Option: 8 Custodial Package Menu

1 ACTIVE by Custodial Package

2 Print ALL by Custodial Package

3 Supported References Print All

Select Custodial Package Menu Option: 1 ACTIVE by Custodial Package

Select PACKAGE NAME: RADIOLOGY/NUCLEAR MEDICINE RA

DEVICE: (Enter a device)

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Radiology/Nuclear Medicine package relies on the following external packages to run effectively:

| PACKAGE                     | MINIMUM VERSION NEEDED |
|---------------------------------|----------------------------|
| Kernel                          | 8.0                        |
| VA FileMan                      | 21.0                       |
| MailMan                         | 7.1                        |
| PIMS                            | 5.3                        |
| Health Level Seven              | 1.6                        |
| Adverse Reaction Tracking (ART) | 4.0                        |
| OE/RR                           | 2.5                        |
| PCE                             | 1.0                        |
| Visit Tracking                  | 2.0                        |

Table 16 - Patches

The following external files are expected to be present, with data:

- CPT (#81)
- CPT Categories (#81.1)
- CPT Modifier (#81.3) [^63]
- Hospital Location (#44)
- Medical Center Division (#40.8)
- New Person (#200)
- Patient (#2)
- Ward Location (#42)

Also, the Electronic Signature fields in the New Person file (#200) are used by this package to verify reports.

## DBIAs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the latest information on active supported references, use the Subscriber Package Menu under the DBA's Integration Agreement Menu on FORUM.

Select Software Services Primary Menu Option: DBA MENU

Select DBA MENU Option: integration CONTROL REGISTRATIONS

Select INTEGRATION CONTROL REGISTRATIONS Option: ?

HELP Instructions for Entering ICRs

GET# GET NEW Integration Control Registration \#(s)

ADD ADD/EDIT Pending Integration Control Registration

ROLL Roll up ICR into Mail Message

FILE File-type Integration Control Registrations Menu ...

ROU Routine-type ICRs Menu ...

RPC Remote Procedure Call-type ICRs Menu ...

OTH Print 'Other'-type ICRs

SUPP Supported References Menu ...

CONT Controlled Subscription ICRs Menu ...

PRIV Private ICRs Menu ...

CUST Custodial Package Menu ...

INQ Inquire to an Integration Control Registration

SUBS Subscriber Package Menu ...

APIS Supported API Report

VBLE Lookup ICRs by Variable

PEND Print ICRs in Pending Status

ACTV Print Active ICRs

ALL Print ALL ICRs

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select INTEGRATION CONTROL REGISTRATIONS Option: SUBS Subscriber Package Menu

Select Subscriber Package Menu Option: ?

1 Print ACTIVE by Subscribing Package

2 Print ALL by Subscribing Package

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Subscriber Package Menu Option: 1 Print ACTIVE by Subscribing Package

\* Previous selection: SUBSCRIBING PACKAGE equals INTEGRATED BILLING

START WITH SUBSCRIBING PACKAGE: INTEGRATED BILLING// RADIOLOGY/NUCLEAR MEDICINE

GO TO SUBSCRIBING PACKAGE: LAST// RADIOLOGY/NUCLEAR MEDICINE

DEVICE: (Enter a device) [^64]

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All options in the Radiology/Nuclear Medicine 5.0 package can function independently. Most options require the use of the following package-wide variables: RACCESS, RAMDV, RAMLC, RAMDIV and RAIMGTY. Descriptions of these variables can be found under Package-wide Variables and under Key Variables of the Implementation and Maintenance section of this manual.

If they do not already exist, these variables are set at the time the option is invoked. They are only killed by the exit action of the user's main Radiology/Nuclear Medicine menu (e.g., Rad/Nuc Med Transcriptionist Menu). If other options are invoked independently, these variables should be killed by adding 'D KILL^RAPSET1' to the exit action of the option.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME    | DESCRIPTION                                                                                                                                                    |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RACCESS | This array identifies the user's division, imaging location and imaging type access.                                                                           |
| RAIMGTY | This is the name of imaging type (File \#79.2 entry) of the user based on the imaging location selected.                                                       |
| RAMDIV  | The internal entry number of the division (File \#79) the user has signed-on to.                                                                               |
| RAMDV   | The division parameters for a File \#79 entry. The parameters that make up this variable are identified in the Key Variables portion, page 23, of this manual. |
| RAMLC   | The imaging location parameters for a File \#79.1 entry. The parameters that make up this variable are identified in the Key Variables portion of this manual. |

These variables are created or changed when the user selects a sign-on imaging location usually during the log-in process or in the Switch Locations option.

The variables are also set by the individual options if they do not already exist. The routine series RAPSET\* sets these variables.

Example of when the package-wide variables are created or changed:

Please select a sign-on Imaging Location: X-RAY// \<RET\> (GENERAL RADIOLOGY)

--------------------------------------------------------------------------

Welcome, you are signed on with the following parameters:

Printer Defaults

Version [^65] : 5.0 ----------------

Division : HINES Flash Card : RAD/NM FLASH CARDS

Location : X-RAY 1 card/exam

Img. Type: GENERAL RADIOLOGY Jacket Label: RAD/NM JACKET LBLS

User : RADUSER,ONE 1 labels/visit

Report : RAD/NM REPORT PTR

--------------------------------------------------------------------------

These variables are killed when the user exits the package menu they logged in under. The variables are killed by calling KILL^RAPSET1.

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes various methods by which users may generate Radiology/ Nuclear Medicine technical documentation.

## Build File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Build File Print option, found under the KIDS Utilities menu, lists the complete definition of the package, including all files, components, install questions, and the environment, pre-install, and post-install routines

## Question Marks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering question marks at the "Select Option:" prompt provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option.

Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock (if applicable) for each.

Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for the option.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility analyzes routines to determine if they adhere to VistA Programming Standards. The XINDEX output may include the following components: Compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Global References, Label References and External References.

To run XINDEX for the Radiology/Nuclear Medicine package, specify the following namespace at the "routine(s) ?\>" prompt: RA\*.

RACT\* routines are compiled template routines, which you may not wish to examine (i.e., -RACT\*).

> **NOTE:** If you run an XINDEX [^66] you may run into several errors caused by references to routines not in the development environment[^67] if the imaging package and/or OE/RR V. 3.0 (CPRS) are not yet installed or released. These errors are benign and do not affect the operation of the Radiology/Nuclear Medicine package.

Routines involved are:

MAGRIC MAGSET3 ORMFN ORXP ORERR

## Inquire to File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the following information about a specified option: option name, menu text, option description, type of option. All fields that have a value will be displayed (e.g., Entry Action).

To secure information about the Radiology/Nuclear Medicine options, the user must specify the name of the options desired (File \#19). The options exported with this package begin with the letters RA.

## Print Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to generate ad hoc reports about options from the Option file (#19). The user may choose one, many or all Radiology/Nuclear Medicine options. The options exported with this package begin with the letters RA.

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to generate documentation pertaining to files and file structure. The Radiology/Nuclear Medicine file numbers are 34 and 70-79.7. See the File List section page [41](#file-list), of this manual for a specific listing.

Select the Standard format to get the following data dictionary information for a specified file: file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates and sort templates.

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-references, input transform, and date last edited.

Select the Global Map format to generate an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates and sort templates.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the *VistA Kernel Systems Manual*.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TERM</strong></th>
<th><strong>MEANING</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abdominal Aortic Aneurysm <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> (AAA)</td>
<td>A weakness in the body’s main artery for that portion of the aorta located in the abdomen. If untreated, it can lead to serious internal bleeding.</td>
</tr>
<tr class="even">
<td>Active</td>
<td>An order status that occurs when a request to perform a procedure on a patient has been registered as an exam, but before it has reached a status of Complete.</td>
</tr>
<tr class="odd">
<td>Activity log</td>
<td>A log of dates and times data was entered and/or changed. The Radiology/Nuclear Medicine system is capable of maintaining activity logs for reports, exam status changes, imaging type parameter changes, purge dates, outside film registry activity, and order status changes.</td>
</tr>
<tr class="even">
<td>Alert</td>
<td>Alerts consist of information displayed to specific users triggered by an event. For example, alerts pertaining to Rad/Nuc Med include the Stat Imaging Request alert, an Imaging Results Amended alert, and an Abnormal Imaging Results alert. The purpose of an alert is to make a user aware that something has happened that may need attention. Refer to Kernel and CPRS documentation.</td>
</tr>
<tr class="odd">
<td>AMIS code <a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td>For imaging, one of 27 codes used to categorize procedures, calculate workload crediting, and weighted work units. AMIS codes are determined by VA Central Office and should not be changed at the medical centers.</td>
</tr>
<tr class="even">
<td>AMIS weight multiplier</td>
<td>A number associated with a procedure-AMIS code pair that is multiplied by the AMIS code weighted work units. If the multiplier is greater than 1, a single exam receives multiple exam credits.</td>
</tr>
<tr class="odd">
<td>Attending physician</td>
<td>The Radiology/Nuclear Medicine software obtains this data from the PIMS package, which is responsible for its entry and validity. Refer to PIMS documentation for more information and a description of the meaning of this term as it applies to VistA.</td>
</tr>
<tr class="even">
<td>Batch</td>
<td>In the Radiology/Nuclear Medicine system, a batch is a set of results reports. Transcriptionists may create batches to keep similar reports together and cause them to print together. One possible purpose might be to print all reports dictated by the same physician together.</td>
</tr>
<tr class="odd">
<td>Bedsection</td>
<td>See PTF Bedsection.</td>
</tr>
<tr class="even">
<td>Bilateral</td>
<td>A special type of modifier that can be associated with an exam, a procedure, or an AMIS code. When an exam is bilateral due to one of the aforementioned associations, workload credit and exam counts are doubled for that exam on most workload and AMIS reports.</td>
</tr>
<tr class="odd">
<td>BI-RADS<sup>™</sup> <a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></td>
<td>Breast Imaging Reporting and Data System: A system created by the American College of Radiology (ACR) to standardize assessment and categorization of breast imaging results and reports.</td>
</tr>
<tr class="even">
<td>Broad procedure</td>
<td>A non-specific procedure that is useful for ordering when the ordering party is not familiar enough with imaging procedures to be able to specify the exact procedure that is to be performed. Before an exam status can progress to Complete, the imaging service must determine a more specific procedure and change the exam procedure to reflect the actual Detailed or Series procedure done. Depending on site parameters, broad procedures may or may not be used at a given facility. Also see Detailed and Series procedure.</td>
</tr>
<tr class="odd">
<td>Bulletin</td>
<td>A special type of mail message that is computer-generated and sent to a designated user or members of a mail group. Bulletins are usually created to inform someone of an event triggered by another user's data entry, or exam and request updates that require some action on the part of the bulletin recipient.</td>
</tr>
<tr class="even">
<td>Camera/Equipment/Room</td>
<td>The specific room or piece of equipment used for a patient's imaging exam. Each is associated with one or more imaging locations. The Radiology/Nuclear Medicine system supports, but does not require users to record the camera/equipment/room used for each exam.</td>
</tr>
<tr class="odd">
<td>Cancelled</td>
<td>A general status that can be associated with a radiology exam or order. A radiology order is cancelled when the order is rejected on the CPRS side. It is important to note that history shows that ‘discontinued’ and ‘cancelled’ were used synonymously when discussing the status of a CPRS or Radiology order prior to the release of RA*5.0*169. Post patch 169 ‘discontinued’ and ‘cancelled’ have distinct meanings.</td>
</tr>
<tr class="even">
<td>Case number</td>
<td><p>A computer-generated number assigned to the record generated when one patient is registered for one procedure at a given date/time.</p>
<p>When multiple procedures are registered for a patient at the same date/time, each procedure will be given a different case number. Case numbers will be recycled and reused by a new patient/procedure/date instance when the exam attains a Complete status.</p></td>
</tr>
<tr class="odd">
<td>Category of exam</td>
<td>For the purposes of this system, category of exam must be Outpatient, Inpatient, Contract, Sharing, Employee, or Research. Several workload and statistical reports print exam counts by category. Others use the category to determine whether exams should be included on the report.</td>
</tr>
<tr class="even">
<td>Clinic</td>
<td>Hospital locations where outpatients are cared for. In VistA, clinics are represented by entries in the Hospital Location file (#44). Radiology/Nuclear Medicine Imaging Locations, represented by entries in the Imaging Location file (#79.1), are a subset of the Hospital Location file.</td>
</tr>
<tr class="odd">
<td>Clinical history</td>
<td>Data entered in the Radiology/Nuclear Medicine system during exam ordering and exam edit. Usually entered by the requesting party to inform the imaging service why the exam needs to be done and what they hope to find out by doing the exam.</td>
</tr>
<tr class="even">
<td>Clinical history message</td>
<td>Text that, if entered in system parameter setup, will always display when the user is prompted for clinical history. Generally used to instruct the user on what they should enter for clinical history.</td>
</tr>
<tr class="odd">
<td>Common Procedure</td>
<td>A frequently ordered procedure that will appear on the order screen. Up to 40 per imaging type are allowed by the system. Other active Rad/Nuc Med procedures are selectable for ordering, but only the ones designated as common procedures and given a display sequence number will be displayed prior to selection.</td>
</tr>
<tr class="even">
<td>Complete</td>
<td>A status that can be attained by an order or an exam.</td>
</tr>
<tr class="odd">
<td>Complication</td>
<td>A problem that occurs during or resulting from an exam, commonly a contrast medium reaction.</td>
</tr>
<tr class="even">
<td>Contract</td>
<td>A possible category of exam when imaging services are contracted out.</td>
</tr>
<tr class="odd">
<td>Contrast medium</td>
<td>A radio-opaque injectable or ingestible substance that appears on radiographic images and is helpful in image interpretation. It is used in many imaging procedures.</td>
</tr>
<tr class="even">
<td>Contrast reaction message</td>
<td>A warning message that will display when a patient who has had a previous contrast medium reaction is registered for a procedure that uses contrast media. The message text is entered during Rad/Nuc Med division parameter setup.</td>
</tr>
<tr class="odd">
<td>CPT code</td>
<td>See Current Procedural Terminology</td>
</tr>
<tr class="even">
<td>Credit stop code</td>
<td>See Stop Code. Also see PIMS documentation.</td>
</tr>
<tr class="odd">
<td>Current Procedural Terminology (CPT)</td>
<td>A set of codes published annually by the American Medical Association which include Radiology/Nuclear Medicine procedures. Each active detailed or series procedure must be assigned a valid, active CPT code to facilitate proper workload crediting. In VistA, CPT's are represented by entries in the CPT file #81.</td>
</tr>
<tr class="even">
<td>Deleted (X) <a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></td>
<td>A report status that refers to a report deleted from a case but remains in the database. The deleted report status is seen on the Report Activity Log after the deleted report is restored. A deleted report is not viewable from any Radiology options.</td>
</tr>
<tr class="odd">
<td>Descendent</td>
<td>A type of Rad/Nuc Med procedure. One of several associated with a 'Parent' type of procedure. The descendent procedures are actually registered and performed. Also see Parent.</td>
</tr>
<tr class="even">
<td>Desired date (of an order)</td>
<td>The date the ordering party would like for the exam to be performed. Not an appointment date. The imaging service is at liberty to change the date depending on their availability.</td>
</tr>
<tr class="odd">
<td>Detailed procedure</td>
<td>A procedure that represents the exact exam performed, and is associated with a CPT code and an AMIS code.</td>
</tr>
<tr class="even">
<td>Diagnostic code</td>
<td>Represented, for the purposes of this system, by entries in the Diagnostic Codes file (#78.3). Diagnostic codes describe the outcome of an exam, such as normal, abnormal. A case may be given one or more (or no) diagnostic code(s).</td>
</tr>
<tr class="odd">
<td>Discontinued</td>
<td><p>An order status that occurs when a user cancels an order. CPRS’ order field and the Radiology order request status get updated to ‘Discontinued’.</p>
<p>Post patch RA*5.0*169 ‘Discontinued’ and ‘Cancelled’ have distinct meanings.</p></td>
</tr>
<tr class="even">
<td>Distribution queue</td>
<td>A mechanism within the Radiology/Nuclear Medicine system that facilitates printing results reports at various hospital locations, such as the patient's current ward or clinic, the file room, and medical records.</td>
</tr>
<tr class="odd">
<td>Division, Rad/Nuc Med</td>
<td>A subset of the VistA Institution file (#4). Multi-divisional sites are usually sites responsible for imaging at more than one facility.</td>
</tr>
<tr class="even">
<td>Draft</td>
<td>A report status that is assigned to all Rad/Nuc Med results reports as soon as they are initially entered into the system, but before they are changed to a status of Verified or (if allowed) Released/Not Verified.</td>
</tr>
<tr class="odd">
<td>DSS ID</td>
<td>Formerly Stop Code associated with each procedure, now DSS ID associated with each Imaging Location.</td>
</tr>
<tr class="even">
<td>Electronic signature code</td>
<td>A security code that the user must enter to identify him/herself to the system. This is required before the user is allowed to electronically verify Rad/Nuc Med reports. This is not the same as the Access/Verify codes.</td>
</tr>
<tr class="odd">
<td>Electronically Filed (EF) <a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a></td>
<td>A report status that refers to a report interpreted outside the Rad/Nuc Med Department. The content is not the actual interpreted report, but canned or manually entered text referring to the outside interpreted report.</td>
</tr>
<tr class="even">
<td>Exam label</td>
<td>One of 3 types of labels that can be printed at the time exam registration is done for a patient. Also see jacket label, flash card.</td>
</tr>
<tr class="odd">
<td>Exam set</td>
<td>An exam set contains a Parent procedure and its Detailed or Series descendent procedures. Requesting a Parent will automatically cause each descendent to be presented for registration as separate cases under a single visit date and time.</td>
</tr>
<tr class="even">
<td>Exam status</td>
<td>The state of an exam that describes its level of progress. Valid exam statuses are represented in this system by entries in the Examination Status file (#72). Examples are ordered, cancelled, complete, waiting for exam, called for exam, and transcribed. The valid set of exam statuses can, to a degree, be tailored by the site. There are many parameters controlling required data fields, status tracking and report contents that are determined when the parameters of this file are set up. There are separate and different set of statuses for requests and reports.</td>
</tr>
<tr class="odd">
<td>Exam status parameter setup</td>
<td>See Exam status.</td>
</tr>
<tr class="even">
<td>Exam status time</td>
<td>The date/time when an exam's status changes, triggered by exam data entry that can be done through over a dozen different options.</td>
</tr>
<tr class="odd">
<td>Film size</td>
<td>Represented by entries in the Film Sizes file (#78.4) in this system. Used to facilitate film use/waste tracking.</td>
</tr>
<tr class="even">
<td>Flash card</td>
<td>One of 3 labels that can be generated at the time an exam is registered for a patient. The flash card was named because it can be photographed along with an x-ray, and its image will appear on the finished x-ray. Helpful in marking x-ray images with the patient's name, SSN, etc. to insure that x-rays are not mixed up.</td>
</tr>
<tr class="odd">
<td>Footer</td>
<td>The last lines of the results report, the format of which can be specified using the Label/Header/Footer Formatter.</td>
</tr>
<tr class="even">
<td>Format</td>
<td>The specification for print locations of fields on a printed page. In this system, print formats can be specified using the Label/Header/Footer Formatter.</td>
</tr>
<tr class="odd">
<td>Header</td>
<td>The top lines of the results report, the format of which can be specified using the Label/Header/Footer Formatter.</td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td>Refers to a report or VistA software package that produces a report showing historical patient data. Can be configured to meet various requirements. Refer to the Health Summary documentation for more information.</td>
</tr>
<tr class="odd">
<td>Hold</td>
<td>An order status occurring when a users puts an order on hold, indicating that a study should not yet be done or scheduled, but that it will likely be needed in the future.</td>
</tr>
<tr class="even">
<td>Hospital location</td>
<td>Represented in VistA by entries in the Hospital Location file (#44). Rad/Nuc Med locations are a subset of the Hospital Location file.</td>
</tr>
<tr class="odd">
<td>Imaging location</td>
<td>One of a subset of Hospital Locations (See Hospital location) that is represented in the Imaging Location file #79.1, and is a location where imaging exams are performed.</td>
</tr>
<tr class="even">
<td>Imaging type</td>
<td><p>For the Rad/Nuc Med software, the set of valid imaging types is:</p>
<ul>
<li><p>ANGIO/NEURO/INTERVENTIONAL</p></li>
<li><p>GENERAL RADIOLOGY</p></li>
<li><p>MAMMOGRAPHY</p></li>
<li><p>NUCLEAR MEDICINE</p></li>
<li><p>ULTRASOUND</p></li>
<li><p>VASCULAR LAB</p></li>
<li><p>CARDIOLOGY STUDIES (NUC MED)</p></li>
<li><p>CT SCAN</p></li>
<li><p>MAGNETIC RESONANCE IMAGING</p></li>
</ul>
<p>These are the imaging types that are supported by this version of the software. Each imaging location and procedure may be associated with only one imaging type.</p></td>
</tr>
<tr class="odd">
<td>Impression</td>
<td>A short description or summary of a patient's exam results report. Usually mandatory data to complete an exam. The impression is not purged from older reports even though the lengthier report text is.</td>
</tr>
<tr class="even">
<td>Inactivate</td>
<td>The process of making a record in a file inactive, usually by entering an inactive date on that record or deleting a field that is necessary to keep it active. When a record is inactive, it becomes essentially "invisible" to users. Procedures, common procedures, modifiers, and exam statuses can be inactivated.</td>
</tr>
<tr class="odd">
<td>Inactivation date</td>
<td>A date entered on a record to make it inactive. See Inactivate.</td>
</tr>
<tr class="even">
<td>Information Resources Management</td>
<td>The service within VA hospitals that supports the installation, maintenance, troubleshooting, and sometimes local modification of VistA software packages and the hardware that they run on.</td>
</tr>
<tr class="odd">
<td><p>Interpreting physician</p>
<p>(also Interpreting Resident, Interpreting Staff)</p></td>
<td>The resident or staff physician who interprets exam images.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td>See Information Resources Management.</td>
</tr>
<tr class="odd">
<td>Jacket label</td>
<td>One of the 3 types of labels that can be generated at the time an exam is registered for a patient. Usually affixed to the x-ray film jacket. (See also exam label, flash card.)</td>
</tr>
<tr class="even">
<td>Key</td>
<td>See security key.</td>
</tr>
<tr class="odd">
<td>Label print fields</td>
<td>Fields that are selectable for printing on a label, report header, or report footer on formats that are designed using the Label/Header/Footer Formatter.</td>
</tr>
<tr class="even">
<td>Label/Header/Footer Formatter</td>
<td>The name given to the option/mechanism that allows users to define formats for labels and for headers and footers on results reports. Users can specify which fields to print at various columns and lines on the label or report header/footer.</td>
</tr>
<tr class="odd">
<td>LOINC</td>
<td>Logical Observation Identifiers Names and Codes (LOINC) is a database and universal standard for identifying medical laboratory observations. LOINC Codes exist within File 71.99 for the purposes of interoperability and standardization.</td>
</tr>
<tr class="even">
<td>Mode of transport</td>
<td>The patient's method of moving within the hospital, (ambulatory, wheelchair, portable, stretcher) designated at the exam is ordered.</td>
</tr>
<tr class="odd">
<td>Modifier</td>
<td>Additional information about the characteristics of an exam or procedure (such as bilateral, operating room, portable, left, right). Also see bilateral, operating room, portable.</td>
</tr>
<tr class="even">
<td>No purge indicator</td>
<td>A flag that can be set on the exam record to force the purge process to bypass the record. Guarantees that the record will not be purged when a historic data purge is scheduled by IRM. Also see Purge. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] &amp; ‘Indicate No Purging of an Exam/report’ [RA PURGE] options.</td>
</tr>
<tr class="odd">
<td>Non-credit stop code</td>
<td>Certain stop codes, usually for health screening, that do not count toward workload credit. If a non-credit stop code is assigned to a procedure, another credit stop code must also be assigned. Also see Stop code.</td>
</tr>
<tr class="even">
<td>On-line verification</td>
<td>The option within the Radiology/Nuclear Medicine package that allows physicians to review, modify, and electronically sign patient result reports.</td>
</tr>
<tr class="odd">
<td>Operating room</td>
<td>A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Operating Room.</td>
</tr>
<tr class="even">
<td>Order</td>
<td>The paper or electronic request for an imaging exam to be performed.</td>
</tr>
<tr class="odd">
<td>Order Entry</td>
<td>The process of requesting that one or more exams be performed for a patient. Order entry for Radiology / Nuclear Medicine procedures can be accomplished through a Rad/Nuc Med software option or through a separate VistA package, CPRS.</td>
</tr>
<tr class="even">
<td>Order Entry/Results Reporting</td>
<td>A VistA package that performs that functions of ordering for many clinical packages, including Radiology/Nuclear Medicine. This package has been replaced by CPRS.</td>
</tr>
<tr class="odd">
<td>Outside films registry</td>
<td>A mechanism in this system that allows users to track films done outside of the medical center. This can also be accomplished through the VistA Record Tracking package. Refer to Record Tracking documentation for more information.</td>
</tr>
<tr class="even">
<td>Parent procedure</td>
<td><p>A type of Rad/Nuc Med procedure that is used for ordering purposes. It must be associated with Descendent procedures that are of procedure type Detailed and/or Series.</p>
<p>At the time of registration the descendent procedures are actually registered. Setting up a parent procedure provides a convenient way to order multiple related procedures on one order.</p>
<p>Parent/descendent procedure relationships must be set up ahead of time during system definition and file tailoring by the ADPAC.</p></td>
</tr>
<tr class="odd">
<td>Pending</td>
<td>An order status that every Rad/Nuc Med order is placed in as soon as it is ordered through this system's ordering option. This system also receives orders from CPRS and places them in a pending status.</td>
</tr>
<tr class="even">
<td>PFSS / Patient Financial Services System <a href="#fn6" class="footnote-ref" id="fnref6" role="doc-noteref"><sup>6</sup></a></td>
<td><p>The PFSS project will prepare the VistA environment for implementation of a commercial off-the-shelf (COTS) billing replacement system.</p>
<p>The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system.</p></td>
</tr>
<tr class="odd">
<td>PFSS Account Reference <a href="#fn7" class="footnote-ref" id="fnref7" role="doc-noteref"><sup>7</sup></a></td>
<td>A PFSS reference to the Account Number entry (external billing visit number) in the VistA Integrated Billing subsystem (IBB) account file. Other VistA applications use this to point to the account number in IBB.</td>
</tr>
<tr class="even">
<td>PFSS Department Code</td>
<td><p>A 3-character numeric code representing the</p>
<p>Department Code for Radiology used by PFSS.</p></td>
</tr>
<tr class="odd">
<td>Portable</td>
<td>A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Portable.</td>
</tr>
<tr class="even">
<td>Pre-verification</td>
<td>The process whereby a resident reviews a report and affixes his/her electronic signature to indicate that the report is ready for staff (attending) review, facilitated through an option in this system for Resident Pre-verification.</td>
</tr>
<tr class="odd">
<td>Primary Interpreting Staff/ Resident</td>
<td>The attending or resident primarily responsible for the interpretation of the case. (See also Secondary Interpreting Staff/Resident.)</td>
</tr>
<tr class="even">
<td>Primary physician</td>
<td>The Radiology/Nuclear Medicine software obtains this data from PIMS, which is responsible for its entry and validity. Refer to the PIMS documentation for more information and a description of the meaning of this term as it applies to VistA.</td>
</tr>
<tr class="odd">
<td>Principal clinic</td>
<td>For the purposes of the Radiology/Nuclear Medicine system, this term is usually synonymous with 'referring clinic'. However, for the purposes of crediting, it is defined as the DSS (clinic/stop) code that is associated with the imaging location where the exam was performed.</td>
</tr>
<tr class="even">
<td>Printset</td>
<td>A printset contains a Parent procedure and its Detailed or Series descendent procedures. If the parent is defined to be a printset, the collection and printing of all common report related data between the descendents is seen as one entity.</td>
</tr>
<tr class="odd">
<td>Problem draft</td>
<td>A report status that occurs when a physician identifies a results report as having unresolved problems, and designates the status to be Problem Draft. Depending on site parameters, a report may be designated as a Problem Draft due to lack of an impression. Also see Problem statement.</td>
</tr>
<tr class="even">
<td>Problem statement</td>
<td>When a results report is in the Problem Draft status, the physician or transcriptionist is required to enter a brief statement of the problem. This problem statement appears on report displays and printouts.</td>
</tr>
<tr class="odd">
<td>Procedure</td>
<td>For the purposes of this system, a medical procedure done with imaging technology for diagnostic purposes.</td>
</tr>
<tr class="even">
<td>Procedure message</td>
<td><p>Represented in this system by entries in the Rad/Nuc Med Procedure Message file (#71.4). If one or more procedure messages are associated with a procedure, the text of the messages will be displayed when the procedures is ordered, registered, and printed on the request form.</p>
<p>Useful in alerting ordering clinicians and imaging personnel of special precautions, procedures, or requirements of a given procedure.</p></td>
</tr>
<tr class="odd">
<td>Procedure type <a href="#fn8" class="footnote-ref" id="fnref8" role="doc-noteref"><sup>8</sup></a></td>
<td><p>A characteristic of a Rad/Nuc Med procedure that affects exam processing and workload crediting. See Detailed, Series, Broad, and Parent.</p>
<p>Also used in Outpatient Procedure Wait Time reports to standardize the reporting of performance monitors throughout VA. Procedure Type categories have been assigned by the Office of Patient Care Services.</p></td>
</tr>
<tr class="even">
<td>PTF Bedsection</td>
<td>See PIMS documentation.</td>
</tr>
<tr class="odd">
<td>Purge</td>
<td>The process that is scheduled at some interval by IRM to purge historic computer data. In this system, purges are done on results report text, orders, activity logs, and clinical history. Patch RA*5.0*198 set out of order both the ‘Purge Data Function’ [RA PURGE] &amp; ‘Indicate No Purging of an Exam/report’ [RA PURGE] options.</td>
</tr>
<tr class="even">
<td>Registration (of an exam)</td>
<td>The process of creating a computer record for one or more patient/procedure/visit date-time instances. Usually done when the patient arrives at the imaging service for an exam.</td>
</tr>
<tr class="odd">
<td>Relative Value Unit (RVU) <a href="#fn9" class="footnote-ref" id="fnref9" role="doc-noteref"><sup>9</sup></a></td>
<td><p>This is a "unit of work" assigned to a CPT code. RVUs are based on the cost of providing a particular service to a patient and are broken down into three components: the Work RVU is the provider time, the Practice Expense RVU is what that time is costing in overhead, and the Malpractice RVU is the liability cost (likelihood of complications).</p>
<p>Each RVU is a weight based on complexity, and is used as a multiplier to calculate Medicare and other fee schedules.</p></td>
</tr>
<tr class="even">
<td>Released/not verified</td>
<td>A results report status that may or may not be implemented at a given medical center. Reports in this status may be viewed or printed by hospital staff outside of the imaging service.</td>
</tr>
<tr class="odd">
<td>Report batch</td>
<td>See Batch.</td>
</tr>
<tr class="even">
<td>Report status <a href="#fn10" class="footnote-ref" id="fnref10" role="doc-noteref"><sup>10</sup></a></td>
<td><p>The state of a report that describes its progress level. Valid report statuses in this system are Draft, Problem Draft, Released/Not Verified (if the site allows this status), Verified, Electronically Filed, and Deleted.</p>
<p>The status of a report may affect the status of an exam. Also see Exam status. Exams and requests each have a separate and different set of statuses.</p></td>
</tr>
<tr class="odd">
<td>Request</td>
<td>Synonymous with order. See Order.</td>
</tr>
<tr class="even">
<td>Request status</td>
<td><p>The state of a request (order) that describes its progress level. Valid request statuses in this system are Unreleased(only if created through CPRS), Pending, Hold, Scheduled, Active, Discontinued, Cancelled and Complete.</p>
<p>Reports and exams each have a separate and different set of statuses.</p></td>
</tr>
<tr class="odd">
<td>Request urgency</td>
<td>Data entered at the time an exam is ordered to describe the priority/criticality of completing the exam quickly (i.e. Stat, Urgent, Routine).</td>
</tr>
<tr class="even">
<td>Requesting location</td>
<td><p>Usually the location where the patient was last seen or treated (an inpatient's ward, or an outpatient's clinic). All requesting locations are represented by an entry in the VistA Hospital Location file (#44).</p>
<p>The requesting location may be, but is usually not an imaging location.</p></td>
</tr>
<tr class="odd">
<td>Requesting physician</td>
<td>The physician who requested the exam.</td>
</tr>
<tr class="even">
<td>Research source</td>
<td>A research project or institution that refers a patient for a Radiology/Nuclear Medicine exam.</td>
</tr>
<tr class="odd">
<td>Scheduled</td>
<td>An order status that occurs when imaging personnel enter a date when the exam is expected to be performed.</td>
</tr>
<tr class="even">
<td>Secondary Interpreting Staff/Resident</td>
<td><p>This generally refers to an attending/resident who assisted or sat in on review of the case, but is not primarily responsible for it.</p>
<p>It may also be used to indicate a second reviewer of the case, for quality control or peer review purposes.</p></td>
</tr>
<tr class="odd">
<td>Security key</td>
<td>Represented by an entry in the VistA Security Key file. Radiology/Nuclear Medicine keys include RA MGR, RA ALLOC, RA UNVERIFY, RA VERIFY and RA SWITCHLOC. Various options and functions within options require that the user "own" a security key.</td>
</tr>
<tr class="even">
<td>Site Specific Accession Number (SSAN) <a href="#fn11" class="footnote-ref" id="fnref11" role="doc-noteref"><sup>11</sup></a></td>
<td><p>This is a case number with the 3-digit Site ID and the Date appended at the beginning of it in the format of ‘SSS-MMDDYY-CASE#’.</p>
<p>An example is 141-052709-23457, where 141 is the site ID, 052709 is the date and 23457 is the case number.</p>
<p>(see also, Case Number above)</p></td>
</tr>
<tr class="odd">
<td>Staff</td>
<td>Imaging Attending.</td>
</tr>
<tr class="even">
<td>Staff review (of reports)</td>
<td>The requirement where an attending imaging physician is required to review the reports written by a resident imaging physician.</td>
</tr>
<tr class="odd">
<td>Standard report</td>
<td>Represented in this system by entries in the Standard Reports file (#74.1). Standard reports can be created by the ADPAC during system definition and set-up. If the division setup specifies that they are allowed, transcriptionists will be offered a selection of standard report text and impressions to minimize data entry effort.</td>
</tr>
<tr class="even">
<td>Status tracking</td>
<td>The mechanism within this system that facilitates exam tracking from initial states to the complete state. ADPACs must specify during exam status parameter setup which statuses will be used, which data fields will be required to progress to each status, which data fields will be prompted, and exams of which statuses will be included on various management reports.</td>
</tr>
<tr class="odd">
<td>Stop code</td>
<td><p>Member of a coding system designed by VA Central Office to aid in determining workload and reimbursement of the medical centers. Stop codes are controlled by VA Central Office. The set of valid stop codes is revised October 1 of each year.</p>
<p>At this time, the PIMS developers issue a maintenance patch to the Vist<em>A</em> software updating the file containing stop codes. Imaging stop codes are represented by entries in the Valid Imaging Stop Code file #71.5.</p>
<p>Imaging stop codes are a subset of the Vist<em>A</em> Clinic Stop file #40.7. See PIMS documentation for more information. (Also see DSS ID.)</p></td>
</tr>
<tr class="even">
<td>Synonym</td>
<td><p>In the Radiology/Nuclear Medicine package, synonyms are alternate terms that can be associated with procedures for the purposes of convenient look-up/retrieval.</p>
<p>A given procedure may have more than one synonym, and a given synonym may be used for more than one procedure.</p></td>
</tr>
<tr class="odd">
<td>Technologist</td>
<td>Radiology/Nuclear Medicine personnel who usually are responsible for performing imaging exams and entering exam data into the system.</td>
</tr>
<tr class="even">
<td>Time-out</td>
<td>The amount of time allowed before a user is automatically logged out of the system if no keystrokes are entered. This is a security feature, to help prevent unauthorized users from accessing your VistA account in case you forget to log off the system or leave your terminal unattended.</td>
</tr>
<tr class="odd">
<td>Transcribed</td>
<td>An exam status that may occur when a results report is initially entered into the system for an exam. If this status is not activated at the site, it will not occur.</td>
</tr>
<tr class="even">
<td>Unreleased</td>
<td>An order status that occurs when an exam order is created, but no authorization to carry out the order has been given. This is possible only if the order is created through the PIMS software.</td>
</tr>
<tr class="odd">
<td>Verification</td>
<td><p>For the purposes of this system, the process of causing a results report to progress to the status of Verified. This happens when a physician affixes his/her electronic signature to the report, or when a transcriptionist, with the proper authorization, enters the name of a physician who has reviewed and approved a report.</p>
<p>This is analogous to a physician signing a paper report.</p>
<p>Verification Timeliness reports are available to show the amount of time elapsed between registration of an exam and its transcription and/or verification.<a href="#fn12" class="footnote-ref" id="fnref12" role="doc-noteref"><sup>12</sup></a></p></td>
</tr>
<tr class="even">
<td>Verified</td>
<td>A results report status that occurs at the time of verification. A report is verified when the interpreting physician electronically signs the report or gives his/her authorization that the report is complete and correct. Also see Verification.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture. Formerly known as DHCP.</td>
</tr>
<tr class="even">
<td>VUID</td>
<td>Veterans Health Administration Unique Identifiers.</td>
</tr>
<tr class="odd">
<td>Waiting for exam</td>
<td>An exam status that occurs as soon as the exam is first registered. The system automatically places all exams in this status upon registration.</td>
</tr>
<tr class="even">
<td>Ward</td>
<td>The hospital location where an inpatient resides. In VistA, wards are a subset of the Hospital Location file (#44).</td>
</tr>
<tr class="odd">
<td>Weighted work unit</td>
<td><p>The number that results from multiplying the weight of a procedure's AMIS code with the procedure's AMIS weight multiplier for that AMIS code.</p>
<p>If a procedure has more than one AMIS code, the multiplication is done for each and the results are summed.</p></td>
</tr>
<tr class="even">
<td>Work Relative Value Unit (wRVU) <a href="#fn13" class="footnote-ref" id="fnref13" role="doc-noteref"><sup>13</sup></a></td>
<td>The work RVU correlates time, intensity, and difficulty of service. For example, a service with a work RVU of "2" would be considered to involve twice as much physician work as a service with a work RVU of "1".</td>
</tr>
<tr class="odd">
<td>Workload credit</td>
<td>A general term that refers to the CPT type of workload credit that is used in the VA to calculate reimbursement to medical centers for work done.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch RA*5*97 August 2009: Added definition for Abdominal Aortic Aneurysm (AAA).<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p> Patch RA*5*45 May 2005: Definition of AMIS code has been changed.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Patch RA*5*97 August 2009: Added definition for Breast Imaging Reporting and Data System (BI-RADS<sup>™</sup>).<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>: Added a definition for the ‘Deleted’ status.<a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5"><p>: Added a definition for the ‘Electronically Filed’ status.<a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn6"><p>Patch RA*5*57 March 2006: Added glossary entry for PFSS.<a href="#fnref6" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn7"><p>Patch RA*5*57 March 2006: Added glossary entry for PFSS Account Reference.<a href="#fnref7" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn8"><p>Patch RA*5*79 February 2007: Updated definition of Procedure Type.<a href="#fnref8" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn9"><p> Patch RA*5*64 July 2006: Added glossary entry for RVU.<a href="#fnref9" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn10"><p>: Added two new valid report statuses to the definition.<a href="#fnref10" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn11"><p> Patch RA*5*47 August 2011: Added Site Specific Accession Number (SSAN) to the Glossary.<a href="#fnref11" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn12"><p>Patch RA*5*67 April 2006: Added Verification Timeliness report description.<a href="#fnref12" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn13"><p>Patch RA*5*64 July 2006: Added glossary entry for wRVU. Updated “Workload credit” definition.<a href="#fnref13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

# SOFTWARE AND DOCUMENTATION NOTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RADIOLOGY/NUCLEAR MEDICINE TECHNICAL MANUAL VERSION 6.0 contains the Rad/Nuc Med Patch RA\*5.0\*113 and RA\*5.0\*116. These manuals are available in MS Word (.doc) format and the Portable Document Format (.pdf) on the VA Software Documentation Library in the Clinical Section http://www4.va.gov/vdl/

RADIOLOGY / NUCLEAR MEDICINE USER MANUAL VERSION 6.0 contains the Rad/Nuc Med Patch RA\*5.0\*113 and RA\*5.0\*116 software and documentation files and it is available in MS Word (.doc) format and the Portable Document Format (.pdf) on the VA Software Documentation Library in the Clinical Section <http://www4.va.gov/vdl/>

To download these files the preferred method is to FTP the files from ftp://download.vista.med.va.gov/. This transmits the files from the first available FTP server.

PATCHES

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Patch RA*5.0*113</u></strong></p>
<p>The Patient Specific Radiation Dose Aggregation patch collects patient radiation information and how many Rankin’s study patients were exposed to</p>
<p>Patient Radiation dose data is available in two report options; Exam Profile with Radiation Dosage Data and a Radiation Dose Summary Report.</p>
<p>The Radiation Dose Summary Report lists completed exams performed within the selected date range for which dose data has been collected. Users must select the type of report format and which filters should apply.</p>
<p>Studies for which dose parameters are captured are currently limited to Computed Tomography and Fluoroscopy. These two modalities are directly related to the CT Scan and General Radiology imaging type records found in the IMAGING TYPE (#79.2) file.</p>
<p>The data returned from the application program interface (API) will be filed in the new RADIATION ABSORBED DOSE (#70.3) file. As long as the study exists and is tied to an active radiation dose record, the radiation dose data will be available to radiology users in the form of report options.</p>
<p>Exported in this patch are new options:</p>
<p>Exam Profile with Radiation Dosage Data - RA PROFRAD DOSE allows the user to select the type of report and the filters applied to the report.</p>
<p>Radiation Dose Summary Report - RA RAD DOSE SUMMARY behaves just as the current patient profile options but the reports may be printed.</p>
<p>When an exam is deleted using the 'Exam Deletion' RA DELETEXAM option, all radiation dosage information associated with that study will be deleted in the RADIATION ABSORBED DOSE file.</p></th>
<th><p><strong><u>Patch RA*5.0*116</u></strong></p>
<p>The VistA Imaging Importer III (for the Radiology Information System Support (RIS)), is a DICOM Image Gateway application for transfering DICOM objects from PAC studies performed outside of the VA, into VistA Imaging.</p>
<p>DICOM objects may be electronically transferred or directly from portable media (such as CDs, DVDs, Flash Drives). Portable media must conform to:</p>
<p>• DICOM Standards</p>
<p>• IHE Portable Data for Imaging PDI profiles</p>
<p>CDs and DVDs saved in proprietary formats usually cannot be transferred by (and used) by VistA Imaging nor can saved Report files (future release).</p>
<p>The VistA Imaging Importer III can correct patient and/or study identification information mismatchs previously processed by older utility software.</p>
<p>Diagnostic codes may be used to generate alerts to the requesting clinician whenever an examination has an abnormal result.</p>
<p>Exported Components (ex-routines), Component Type</p>
<p>RAMAG EXAM COMPLETE, Remote Procedure Call (RPC)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><u>Patch RA</u></strong><strong><u>*5.0*127</u></strong></p>
<p>The Department of Veterans Affairs (VA) Interagency Program Office (IPO)and the Department of Defense (DoD) is tasked by its charter withleading the Departments’ efforts “to implement national health datastandards for interoperability and [be] responsible for establishing,monitoring, and approving the clinical and technical standards profileand processes to ensure a seamless [exchange] of health data.” This task of Native Domain standardization is aligned with achieving the goalsoutlined in the 2014 National Defense Authorization Act (NDAA) requiringthat the Departments’ “healthcare data [are] computable in real-time and[comply] with existing national data standards” and that the “data [are]standardized as national standards continue to evolve.”</p>
<p>VA clinicians historically used non-standardized clinical terminologies which are inconsistent within the VA user community as well as within the currently accepted data standards as established by Office of the National Coordinator for Health Information Technology (ONC). Implementation of Native Standardization will allow a streamlined method for data sharing, performing clinical decision support and engaging in national data reporting and analysis. The VA has recently established a process for implementing standard terminology/terminologies within individual clinical domains for the exchange of data. The intent of this effort is to provide the detailed groundwork necessary for industry-wide interoperability. By providing a detailed analysis of the current state of the applicable domains and recommendations regarding the path forward, the Native Domain Standardization supports VA’s efforts toremain at the forefront of healthcare data exchange.</p>
<p>The system will include the addition of a new field to the RAD/NUC MED PROCEDURE file (#71) and creation of the Master Radiology Procedure File (MRPF) Gold File (#71.99).</p>
<p>The local facility Automated Data Processing Application Coordinator (ADPAC) will need to associate the local procedure names in file #71 to Gold Names in file #71.99.</p>
<p>It will be necessary to develop a national standard of radiology procedures and map to their respective Current Procedural Terminology (CPT) code and Logical Observation Identifiers Names and Codes (LOINC) will be populated under the direction of the VHA Radiology Program Office prior to implementation of any of the data within these files. The objective of this process is to enable the most user friendly interface as possible in the implementation of the native standardization along with all of the activities required to operationalize the change within the VistA environment and the associated terminology consuming applications. The Radiology ADPAC will match each active entry in the RAD/NUC MED PROCEDURES file (# 71) to an entry in the MASTER RADIOLOGY PROCEDURES file (#71.99) (MRPF). This is all that is required outside the normal day-to-day operations. When a new procedure is entered into the RAD/NUC MED PROCEDURES file (# 71) an email is automatically sent to the NEW TERMINOLOGY RAPID TURNAROUND (NTRT) team for the creation of a new entry in the MRPF. The results of the NTRT process will be one of three possible results. 1) A new entry will be created in the MRPF and will be in he next file release. 2) A match was found in the MRPF and the facility should use that entry for a match. 3) There is no LOINC that matches this procedure and a request for a new LOINC has been submitted.</p>
<p>An On Demand report is available to the VHA Radiology Program Office that will allow them to monitor new procedure creation activity. A bulletin will be sent to a local mail group, the VHA Radiology Program Office, and NTRT whan a new procedure reaches a specified number of days from creation and it has not been matched to a MASTER RADIOLOGY PROCEDURES file (# 71.99) entry. While the MASTER RADIOLOGY PROCEDURES file (# 71.99) is locked down and cannot be changed at the local facility, the RAD/NUC MED PROCEDURES file (# 71) will remain accessable to the local facility.</p></td>
<td></td>
</tr>
</tbody>
</table>

[^1]:  Patch RA\*5\*78 May 2009: Added a phrase to the description of the interface in the Introduction

[^2]: Patch RA\*5\*12 December 1999

[^3]: Patch RA\*5\*12 December 1999

[^4]: Patch RA\*5\*26 July 2001: Additional text description.

[^5]: Patch RA\*5\*41 August 2005: Text deletion – Please see revision history.

[^6]:  Patch RA\*5\*27 April 2002: Added the word Additional to the CLINICAL HISTORY subfile from File (#74).

[^7]: Patch RA\*5\*41 August 2005: Text deletion – Item 5 - Order data (ORDER DATA CUT-OFF).

[^8]:  Patch RA\*5\*34 May 2003: Changed 9999 to 99999

[^9]:  Patch RA\*5\*41 August 2005: Text deletion – Please see revision history.

[^10]:  Patch RA\*5\*41 August 2005: Text deletion – Please see revision history.

[^11]: Patch RA\*5\*34 May 2003: Updated example

[^12]:  Patch RA\*5\*41 August 2005: Text deletion ^RAO - …but not data from ^RAO (order data) …order data changed 5 items to 4.

[^13]:  Patch RA\*5\*41 August 2005: Deleted “O Orders only” and “A All three"

[^14]:  Patch RA\*5\*41 August 2005: Purging orders/requests was deleted

[^15]:  Patch RA\*5\*34 May 2003: Inserted section on data recovery.

[^16]:  Patch RA\*5\*26 July 2001: Added new option \[RA XREF CLEANUP\].

[^17]:  Patch RA\*5\*47 August 2011: Added a new option to turn on the site-specific accession number: Site Accession Number Set-up.

[^18]: Patch RA\*5\*47 August 2011: Replaced the example with an updated version.

[^19]: Patch RA\*5\*31 November 2002: Added new option \[RA CREDIT IMAGING LOCATION\].

[^20]: Patch RA\*5\*44 March 2004: Added Scheduled Perf. Indic. Summary for fifteenth of the month.

[^21]:  Patch RA\*5\*99 February 2010: Added “Following the Quarter End” to reflect change in reporting periods.

[^22]:  Patch RA\*5\*99 February 2010: The date the task executes was changed to quarterly to reflect new quarterly reporting periods. Previously, the reporting periods were monthly.

[^23]: Patch RA\*5\*45 May 2005: Added “Note: sites may have compiled templates …”

[^24]: Patch RA\*5\*37 June 2003: Added local mail group name and definition.

[^25]:  Patch RA\*5\*78 May 2009: Added the new mail group name and description, RAD HL7 MESSAGE

[^26]: Patch RA\*5\*12 December 1999

[^27]: <span id="_Ref163373573" class="anchor"></span> June 2007: Edited paragraph to remove Interpreting Resident; removed MedSpeak from list of VR systems.

[^28]: June 2007: Added OBR-32 segment information to the RAHLTCPB routine description.

[^29]: Patch RA\*5\*78 May 2009: Added information about querying the VistA Radiology application for results

[^30]: June 2007: Edited the note to include a reference to File \#79.

[^31]:  Patch RA\*5\*45 May 2005: Added reference to HL7 specific documents to: 1) describe interfaces with COTS applications 2) general HL7 message definition. Removed reference to deleted Appendix.

[^32]:  Patch RA\*5.0\*47 August 2011: Updated the names of the Rad/Nuc Med HL7 manuals.

[^33]: Patch RA\*5\*12 December 1999: Added new file \#79.3

[^34]:  Patch RA\*5\*81 June 2007: Added new file: \#79.7

[^35]: Patch RA\*5\*12 December 1999

[^36]: Patch RA\*5\*26 August 2001: Added new option \[RA RPTDISTREBUILD\]

[^37]:  Patch RA\*5\*47 August 2011: Added a new option to the IRM Menu \[RA SITEMANAGER\]: Site Accession Number Set-up.

[^38]: Patch RA\*5\*31 November 2002: Added new option to \[RA SITEMANAGER\]

[^39]: Patch RA\*5\*44 March 2004: Added new option \[RA PERFORMIN SCHEDULE\].

[^40]: : Added new option, Outside Report Entry/Edit.

[^41]:  Patch RA\*5\*64 July 2006: Added five reports to \[RA WKL\] menu: Physician CPT Report by ImagingType, and four Physician wRVU reports.

[^42]:  Patch RA\*5\*64 July 2006: Added two Procedure wRVU reports to \[RA SPECRPTS\] menu.

[^43]:  Patch RA\*5\*37 June 2003: Added Performance Indicator menu options.

[^44]:  Patch RA\*5\*67 April 2006: Renamed Performance Indicator menu to Timeliness Reports. The Performance Indicator \[RA PERFORMIN MENU\] option is automatically deleted and replaced during this patch installation.

[^45]: Patch RA\*5\*67 April 2006: Renamed Performance Indicator to Verification Timeliness; menu options unchanged.

[^46]: Patch RA\*5\*44 March 2004: Added new option \[RA PERFORMIN TASKLM\].

[^47]: Patch RA\*5\*25 August 2002: Added Radiology HL7 Menu.

[^48]:  Patch RA\*5\*80 September 2007: Added new option \[RA HL7 RESEND BY DATE RANGE\].

[^49]:  Patch RA\*5\*45 May 2005: Added new option to Procedure File Listings menu \[RA CMAUDIT HISTORY\].

[^50]:  Patch RA\*5\*45 May 2005: Added new option to Procedure File Listings menu \[RA PROCMEDIA\].

[^51]:  Patch RA\*5\*31 November 2002: Added new option \[RA VISTARAD CATEGORY P\].

[^52]:  Patch RA\*5\*12 December 1999

[^53]:  Patch RA\*5\*31 November 2002: Added new option \[RA VISTARAD CATEGORY E\].

[^54]:  Patch RA\*5\*35 January 2003: Added new option to \[RA USERUTL\]

[^55]: Patch RA\*5\*64 July 2006: Added five reports to \[RA WKL\] menu: Physician CPT Report by I-Type, and four Physician wRVU reports.

[^56]: Patch RA\*5\*25 August 2002: A number of new protocols added.

[^57]:  Patch RA\*5\*47 August 2011: Added new protocol: RA CANCEL 2.4.

[^58]: Patch RA\*5\*47 August 2011: Added new protocol: RA EXAMINED 2.4.

[^59]: Patch RA\*5\*12 December 1999

[^60]:  Patch RA\*5\*47August 2011: Added new protocol: RA REG 2.4.

[^61]: Patch RA\*5\*47 August 2011: Added new protocol: RA RPT 2.4.

[^62]: Added four new protocols for ScImage.

[^63]: Patch RA\*5\*45 May 2005: Added the CPT MODIFIER (#81.3) file to the External Relations section.

[^64]:  Patch RA\*5\*78 May 2009: Updated the screen capture of the DBIAs section

[^65]:  Patch RA\*5\*45 May 2005: Changed the screen capture; the Version label erroneously displayed the version of the application as being 4.5, not version 5.

[^66]:  Patch RA\*5\*45 May 2005: All reference to %INDEX removed.

[^67]:  Patch RA\*5\*78 May 2009: Changed UCI to development environment in the note regarding XINDEX