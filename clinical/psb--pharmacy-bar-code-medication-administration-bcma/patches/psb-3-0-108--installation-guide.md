---
title: BCMA V.3.0 Backup System (BCBU) Version 3 Installation Guide (updated PSB*3*108)
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Backup System (BCBU) Version 3  (updated PSB*3*108)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3.0
patch_id: PSB*3.0*108
group_key: "PSB:PSB:3.0"
file_numbers: []
security_keys: []
menu_options: 17
description: ![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/001.png)
audience: 
keywords: 
  - bcma
  - class
  - table
  - backup
  - workstation
  - bcbu
  - contents
  - orders
  - medication
  - vista
page_count: 0
word_count: 16922
section_count: 20
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_0_P108_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_0_P108_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/001.png)

BARCODE MEDICATION ADMINISTRATION (BCMA)

BCMA Backup System (BCBU)

INSTALLATION GUIDE

PSB\*3\*108

July 2021

Acknowledgments

The Bar Code Administration - Enterprise Tactical Support Team (National VistA Support Team) would like to extend the following acknowledgements to:

<span class="mark">REDACTED</span> and <span class="mark">REDACTED</span> of the New Jersey Health Care System.

The Bar Code Medication Administration Backup System (BCBU) has been based on their original conceptual model and retains many of the ideas implemented in the Class III plan. Their hard work and determination has led the way for us to provide all VA Medical Centers with a viable BCMA Contingency Plan.

<span class="mark">REDACTED</span> of VA Medical Center San Francisco, California.

His knowledge of the VistA HL7 package and work on the security portion of the Bar Code Medication Administration Backup System (BCBU) made it possible for the Class I acceptance of the package.

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [BCMA V. 3.0 and This Guide](#bcma-v-30-and-this-guide)
- [Security Information](#security-information)
- [Pre-Installation Information](#pre-installation-information)
- [Installation Information](#installation-information)
- [# Sample Installation](#sample-installation)
- [Sample PC Workstation Database Initialization](#sample-pc-workstation-database-initialization)
- [Technical Information](#technical-information)
  - [Option Descriptions](#option-descriptions)
  - [HL7 Parameters](#hl7-parameters)
    - [PSB BCBU CLIENT](#psb-bcbu-client)
    - [PSB BCBU SERVER](#psb-bcbu-server)
    - [PSB PMU SEND](#psb-pmu-send)
  - [HL7 Message Examples](#hl7-message-examples)
    - [Unit Dose Orders](#unit-dose-orders)
- [NTE^21^L^These are long word processing text special instructions that can be\\br\entered via CPRS as provider comments and then optionally included in the\\br\Pharmacists Special instructions as is or amended by the phrmamcists\\br\with more in](#nte21lthese-are-long-word-processing-text-special-instructions-that-can-bebrentered-via-cprs-as-provider-comments-and-then-optionally-included-in-thebrpharmacists-special-instructions-as-is-or-amended-by-the-phrmamcistsbrwith-more-in)
    - [IV Orders](#iv-orders)
    - [Med Log](#med-log)
  - [Parameter Definitions](#parameter-definitions)
    - [PSB BKUP DEFAULT](#psb-bkup-default)
    - [PSB BKUP MACHINES](#psb-bkup-machines)
    - [PSB BKUP ONLINE](#psb-bkup-online)
    - [PSB BKUP IPH](#psb-bkup-iph)
    - [PSB BKUP MEDLG](#psb-bkup-medlg)
    - [PSB BKUP DOM FILTER](#psb-bkup-dom-filter)
  - [List Templates](#list-templates)
    - [PSB ERROR LOG](#psb-error-log)
    - [PSB SELECT ORDERS](#psb-select-orders)
    - [PSB SELECT PATIENT](#psb-select-patient)
    - [PSB SHOW ORDERS](#psb-show-orders)
  - [HL Communication Server Parameters](#hl-communication-server-parameters)
  - [Files Associated with GT.M/Linux BCMA:](#files-associated-with-gtmlinux-bcma)
  - [Adding a BCMA printer to the Cache/NT Contingency system:](#adding-a-bcma-printer-to-the-cachent-contingency-system)
    - [Contingency Workstation (VistA) printer:](#contingency-workstation-vista-printer)
    - [From within Contingency Workstation (VistA) Printer](#from-within-contingency-workstation-vista-printer)
  - [Adding a BCMA printer to the GT.M/Linux Contingency system:](#adding-a-bcma-printer-to-the-gtmlinux-contingency-system)
    - [Contingency Workstation (VistA)](#contingency-workstation-vista)
    - [From within Contingency Workstation (VistA)](#from-within-contingency-workstation-vista)
    - [From within Contingency Workstation (VistA)](#from-within-contingency-workstation-vista-1)
  - [Workstation Queued Tasks](#workstation-queued-tasks)
- [Quick Reference Installation Checklist](#quick-reference-installation-checklist)
- [Contingency PC Workstation Reports](#contingency-pc-workstation-reports)
  - [List/Display Orders](#listdisplay-orders)
  - [## BCBU MAR (Medical Administration Record) Report](#bcbu-mar-medical-administration-record-report)
  - [Print MAR for All Wards](#print-mar-for-all-wards)
  - [Print MAR for Selected Patient](#print-mar-for-selected-patient)
  - [Print MAR for Selected Ward](#print-mar-for-selected-ward)
  - [Print MAR for All Clinics](#print-mar-for-all-clinics)
  - [## Print MAR for Selected Clinic](#print-mar-for-selected-clinic)
  - [## Print Blank MAR for Selected Patient](#print-blank-mar-for-selected-patient)
    - [Blank 3 Day MAR for Selected Patient](#blank-3-day-mar-for-selected-patient)
    - [Blank 7 Day MAR for Selected Patient](#blank-7-day-mar-for-selected-patient)
  - [List of Wards in BCMA Backup File](#list-of-wards-in-bcma-backup-file)
- [Trouble Shooting Guide](#trouble-shooting-guide)
<span id="pagei" class="anchor"></span>Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All”, replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 54%" />
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
<td>7/2021</td>
<td><p>i</p>
<p><a href="#P9_Hazrdous_Handle">9</a></p>
<p><a href="#P42_Hazardous_Handle">42</a></p></td>
<td>PSB*3*108</td>
<td>Added notifications to the Medication Administration Record (MAR) reports for hazardous to handle and hazardous to dispose drugs.</td>
</tr>
<tr class="even">
<td>9/2016</td>
<td><p><a href="#pagei">i</a>-<a href="#pageiv">iv</a></p>
<p><a href="#datadictionary_9">9</a></p>
<p><a href="#listdisplay-orders">39</a></p>
<p><a href="#bcbu-mar-medical-administration-record-report">42</a></p></td>
<td>PSB*3*87</td>
<td><p>Updated revision history, table of contents. Removed repeating headers.</p>
<p>Added data dictionary changes for Transdermal.</p>
<p>Added updates to the List/Display Orders section. Added BCBU MAR (Medical Administration Record) Report.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>1/2014</td>
<td>i-iv, <a href="#p73_5">5</a>, <a href="#p73_10">10-11</a>, <a href="#p73_12">12<strong>,</strong> 12a-12b</a>, <a href="#p73_13">13-14</a>, <a href="#p73_19">19-21, 21a-21b</a>, <a href="#p73_22">22-23</a>, <a href="#p73_25">25</a>, <a href="#adding-a-bcma-printer-to-the-cachent-contingency-system">31</a>, <a href="#p73_44">44-44a</a>, <a href="#p73_45">45-46</a>, <a href="#print-mar-for-all-clinics">48<strong>,</strong> 48a-48d</a></td>
<td>PSB*3*73</td>
<td><p>This patch will enhance the BCMA Backup System (BCBU) to support Clinic Orders. The Backup System will be able to store a Clinic name, per each order, for orders associated with clinic locations. The existing MAR reports will now print the clinic name along with the order under a heading label of "Location". The word "INPATIENT" will also print under the “Location” heading for Inpatient Medication orders, which are associated with the ward, of patients that are admitted. This patch will add two new menu options to support the printing of MAR reports for Selected Clinic or All Clinics.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/2013</td>
<td><a href="#bcbu-mar-medical-administration-record-report">44</a>-46</td>
<td>PSB*3*59</td>
<td><p>Patients with no current medication orders are now printed consistently on the three BCBU MAR reports (Print MAR for All Wards, Print MAR for Selected Patient, and Print MAR for Selected Ward). The patient’s information is followed by a message stating “No Active Medication Orders were reported to the Contingency at the time the MAR was printed”, followed by multiple blank lines and a footer. Also, a blank page is no longer used as a separator on the Print MAR for a Selected Ward (PW) and the Print MAR for All Wards (PA).</p>
<p>On both the Print MAR for a Selected Ward (PW) and the Print MAR for All Wards (PA) menus, after the question ‘Report [A]LL or [C]URRENT orders?’ has been answered ‘CURRENT’, a prompt appears, ‘Include Patients without Active Medications?’ (defaults to ‘Yes’). Answering ‘No’ prevents current patients without medications from printing on the report.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 56%" />
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
<td>09/2012</td>
<td>i, 44, 44a-44b</td>
<td>PSB*3*69</td>
<td><p>The Special Instructions and Other Print Info project changed these comment type fields to unlimited word processing text. This text is sent over in the same NTE segment as before. BCBU has been enhanced to receive and store the unlimited word processing text and print the word processing lines of text on the MAR reports as they were typed and stored in the Inpatient Order.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/2006</td>
<td>All</td>
<td>PSB*3*8</td>
<td><p>Document reissued for significant enhancements and issue resolution.</p>
<p>See patch description for details.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/2003</td>
<td></td>
<td></td>
<td>Original Released Bar Code Medication Administration Backup System (BCBU) Installation Guide.</td>
</tr>
</tbody>
</table>
Table of Contents
<span id="pageiv" class="anchor"></span>Department of Veterans Affairs [1](#_Toc76734832)
[Product Development [1](#_Toc76734833)](https://dvagov.sharepoint.com/sites/OITmpdu/Shared%20Documents/1_Pharmacy%20Safety%20Updates%20Project/IOC/Release%202/CD2_Release%20Readiness/PSB_3_108/AC%27s%20TM,%20UM,%20IG/PSB_IG.DOCX#_Toc76734833)

# BCMA V. 3.0 and This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="benefits-of-bcma" class="unnumbered">Benefits of BCMA </h2></td>
<td><p>The Veterans Health Information Systems and Technology Architecture (VistA) Bar Code Medication Administration Backup System (BCBU) software will provide a Class I solution to the BCMA Contingency IRA #20020403. This plan reflects the intent of VHA Directive #6210, the Automated Information Systems (AIS) Security, which states that all facilities are responsible for the development, maintenance, and annual testing of individual AIS contingency. This software maintains a current copy on the designated workstation, of all the inpatient pharmacy activities including the inpatient medication orders, medication administrations, and allergies that are included on a Pharmacy Medication Administration Record (MAR).</p>
<p>The Bar Code Medication Administration Backup System (BCBU) will interface with the BCMA VistA product to provide a real-time backup of all inpatient medication activities on a designated workstation(s). Designated workstation(s) will contain current information regarding inpatient medication orders (Unit Dose and IV), medication administration record (MAR), medication administration history (MAH), and patient allergies. Workstation(s) are updated using the VA Health Level Seven (HL7) package. These workstation(s) are available for use according to local policies concerning VistA<strong>,</strong> BCMA, or network outages.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="benefits-of-this-guide" class="unnumbered">Benefits of This Guide</h2></td>
<td>The Veterans Health Information Systems and Technology Architecture (VistA) Bar Code Medication Administration Backup System (BCBU) Installation provides detailed instructions required for installing and implementing this new software. Additional manuals are available with instructions for installing and implementing the new software on either a Linux or Caché workstation environment.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="our-target-audience" class="unnumbered">Our Target Audience</h2></td>
<td><p>This guide was developed for the following individuals, who are responsible for the installation, maintenance, support, and use of the package.</p>
<ul>
<li><p>Information Resources Management (IRM)</p></li>
<li><p>Clinical Application Coordinator (CAC) – called Applications Package Coordinator (ADPAC) at some sites</p></li>
<li><p>National VistA Support (NVS)</p></li>
<li><p>Independent Verification and Validation (IV&amp;V)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="this-manual-includes" class="unnumbered">This Manual Includes</h2></td>
<td><p><strong>Security Information</strong>: This section contains information regarding the mail group, alerts, and file security associated with the Bar Code Medication Administration Backup System (BCBU) software.</p>
<p><strong>Pre-Installation Information</strong>: This section provides information needed prior to installing the Bar Code Medication Administration Backup System (BCBU) software.</p>
<p><strong>Installation Information</strong>: This section contains instructions and examples of the Bar Code Medication Administration Backup System (BCBU) software.</p>
<p><strong>Technical Information</strong>: This section provides information on protocols involved in the Bar Code Medication Administration Backup System (BCBU) software.</p></td>
</tr>
<tr class="even">
<td><h2 id="section" class="unnumbered"></h2></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="other-sources-of-information" class="unnumbered">Other Sources of Information</h2>
<p>![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/002.png)</p></td>
<td><p>For more background and technical information about BCMA V. 3.0, refer to the Web sites listed below.</p>
<p>Background/Technical Information</p>
<p>To access the BCMA Home page, enter <mark>REDACTED</mark> in the Address field of your browser. The BCMA Backup System Installation Guide can be accessed from the VA Software Document Library (VDL) at <a href="http://www.va.gov/vdl/clinical.asp?appID=84"><u>http://www.va.gov/vdl</u></a>. The document is available in MS Word (.doc) format and Adobe Portable Document Format (.PDF).</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="conventions-used-in-this-guide" class="unnumbered">![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/003.png)![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/004.png)Conventions Used in This Guide</h2></td>
<td><p>Before installing BCBU patches, review this section to learn the many conventions used throughout this guide.</p>
<ul>
<li><p><strong>Keyboard Responses</strong>: Keys provided in boldface, within the steps, help you quickly identify what to press on your keyboard to perform an action. See the examples provided below.</p>
<ul>
<li><p><strong>Within the Steps:</strong> At the "Select Kernel Installation &amp; Distribution System Option" prompt, type <strong>INSTALL</strong>, and then press <span class="smallcaps"><strong>enter</strong>.</span></p></li>
<li><p><strong>Within Screen Captures:</strong> Text in <strong>boldface</strong>, centered between arrows on screen captures, identifies the key you must press for the system to capture your response or to move the cursor to the next field. See the following example.</p></li>
</ul></li>
</ul>
<p>DEVICE FOR QUEUED JOB OUTPUT: &lt;<strong>Enter</strong>&gt;</p>
<ul>
<li><p><strong>Mouse Responses:</strong> Buttons provided in <strong>boldface</strong>, within the steps, indicate what you should click on your computer screen using the mouse. For example, when you see <span class="smallcaps"><strong>next, yes/no,</strong></span> or <strong><span class="smallcaps">ok</span></strong> in the steps, click the appropriate button on your computer screen.</p></li>
<li><p><strong>User Responses:</strong> Information presented in <strong>boldface</strong>, within steps or shaded screen captures, indicate what you should “type” (enter) onto your computer screen. See the examples provided below.</p>
<ul>
<li><p><strong>Within the Steps</strong>: At the "Select OPTION NAME" prompt, type XPD MAIN and then press <strong><span class="smallcaps">enter</span></strong>.</p></li>
<li><p><strong>Within Screen Captures</strong>: See the following example.</p></li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Conventions Used in This Guide (cont.)</strong></td>
<td><p>RESCHEDULING FREQUENCY: <strong>1M</strong></p>
<ul>
<li><p><strong>Screen Captures</strong>: Provide "shaded" examples of what you will see on your computer screen, and possible user responses.</p></li>
<li><p><strong>Notes:</strong> Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our Staff, Developers, and Testers.</p></li>
<li><p><strong>Menu Options</strong>: When provided in italics, identifies a menu option. When provided in boldface, ALL CAPS, identifies the letters that you should type onto your computer screen, before pressing <span class="smallcaps">enter.</span> The system then goes directly to the menu option. (Note: The letters do not have to be entered as capital letters, even though they are provided within the steps in this format.) See the examples provided below.</p>
<ul>
<li><p><strong>Italicized:</strong> Use the Kernel <em>First Line Routine Print</em> option to print a list containing the first line of every PSB routine.</p></li>
<li><p><strong>Capitalized:</strong> At the "TaskMan Management Option:" prompt, type <strong>Schedule</strong>/Unscheduled Options, and then press <strong><span class="smallcaps">enter</span>.</strong></p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="locating-detailed-listings" class="unnumbered">Locating Detailed Listings</h2></td>
<td><p>You can obtain and print listings about routines and Data Dictionaries using the information provided below.</p>
<h3 id="routines">Routines</h3>
<p>Use the Kernel routine XINDEX to produce detailed listings of routines. Use the Kernel <em>First Line Routine Print</em> option to print a list containing the first line of every ALPB routine.</p>
<h3 id="data-dictionaries">Data Dictionaries</h3>
<p>The Data Dictionaries (DDs) are included in the on-line documentation for this software application. You can use the VA FileMan <em>List File Attributes</em> option, under <em>Data Dictionary Utilities</em> option, to print the Dictionaries. Journaling is not recommended for the ALPB global.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="interface-software" class="unnumbered">Interface Software</h2></td>
<td>The interface software is HL7. This will transmit the pharmacy data to the designated workstation.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="alerts" class="unnumbered">Alerts</h2></td>
<td>The mail group, PSB BCBU ERRORS, will receive all alerts.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="bcma-menus" class="unnumbered">BCMA Menus</h2></td>
<td><p>Bar Code Medication Administration Backup System (BCBU) software two main menus listed below. The options for each menu are listed in this section.</p>
<ul>
<li><p>BCMA Backup System (Wrkstn)<br />
[PSB BCBU WRKSTN MAIN]</p></li>
<li><p>BCMA Backup System (VistA)<br />
[PSB BCBU VistA MAIN]</p></li>
</ul>
<p>BCMA Backup System (Wrkstn)</p>
<p>This menu includes the following options:</p>
<ul>
<li><p>List/Display Orders</p></li>
<li><p>Print MAR for All Wards</p></li>
<li><p>Print MAR for Selected Patient</p></li>
<li><p>Print MAR for Selected Ward</p></li>
<li><p><span id="p73_5" class="anchor"></span>Print MAR for All Clinics</p></li>
<li><p>Print MAR for Selected Clinics</p></li>
<li><p>Print Blank MAR for Selected Patient</p></li>
<li><p>List of Wards in BCMA Backup File</p></li>
<li><p>BCMA Backup System Management Menu</p></li>
</ul>
<blockquote>
<p><em>BCMA Backup System Error Log</em></p>
<p><em>Edit Workstation Parameter Settings</em></p>
<p><em>Purge Orders Past X days old</em></p>
</blockquote>
<p>BCMA Backup System (VistA)</p>
<p>This menu includes the following options:</p>
<ul>
<li><p>Associate Backup Workstations with a Division</p></li>
<li><p>Default Workstation Initialize</p></li>
<li><p>Divisional Worstation Initialize</p></li>
<li><p>Initialize a Backup Workstation with BCMA Users</p></li>
<li><p>Single Patient Init</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="mail-group" class="unnumbered">Mail Group</h2></td>
<td>The PSB BCBU Errors Mail Group is used to notify responsible users of potential problems with sending information to the Contingency Workstation(s). Members of this group should include the staff that monitors the BCMA Backup System.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="remote-systems" class="unnumbered">Remote Systems</h2></td>
<td>The workstation where the software resides is the only remote system that will receive any data.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="archivingpurging" class="unnumbered">Archiving/Purging</h2></td>
<td>The product purges itself and only keeps active inpatient data. The journal files are flipped and purged nightly so disk space is not consumed by journaling.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="contingency-planning" class="unnumbered">Contingency Planning</h2></td>
<td>This contingency plan software can be used if there is a VistA outage. The sites can use the data stored on the workstations using the outputs on the menu supplied.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="menus" class="unnumbered">Menus</h2></td>
<td>There are two menus for use with this package, BCMA Backup System (Wrkstn) and BCMA Backup System (VistA). The BCMA Backup System Management Menu is under the first menu and requires a Security Key as described below.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="security-keys" class="unnumbered">Security Keys</h2></td>
<td>The BCMA Backup System Management Menu is secured by the security key, PSB BUMGR and MUST be assigned to the designated IRM personnel who currently manage the system for total access to the Bar Code Medication Administration Backup System.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="references" class="unnumbered">References</h2></td>
<td><p>Kernel Systems Manual V. 8.0</p>
<p>Kernel Toolkit V. 7.3</p>
<p>VA FileMan V. 22.0</p>
<p>MailMan V. 8.0</p>
<p>Health Level Seven (HL7) V. 1.6</p></td>
</tr>
</tbody>
</table>

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="recommended-users" class="unnumbered">Recommended Users</h2></td>
<td>Information Resource Management (IRM) Staff is recommended for installing, implementing and supporting the Bar Code Medication Administration Backup System (BCBU). IRM, Pharmacy, and Nursing staff must coordinate the implementation of the setup tasks after the package is installed.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="vista-operating-system-and-performance-capacity" class="unnumbered">VistA Operating System and Performance Capacity</h2></td>
<td>VistA Bar Code Medication Administration Backup System (BCBU) currently runs on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These hardware platforms consist of standard or upgraded Alpha 4100, ES40, or ES45 clusters, and run either DSM on VMS, Caché/VMS, Caché/NT, or CachéXP. There are no significant changes in the performance capacity of the VistA operating system once the VistA Bar Code Medication Administration Backup System (BCBU) has been installed. The software application should not create any appreciable global growth or network transmission problems. There are no memory constraints.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="central-processing-unit-cpu-requirements" class="unnumbered">Central Processing Unit (CPU) Requirements</h2></td>
<td><p>The following workstation configuration is recommended for installing and running the VistA Bar Code Medication Administration Backup System (BCBU).</p>
<p>Sites previously using the New Jersey Class III package should be able to use current workstations and Caché license.</p>
<p><u>Hardware</u></p>
<ul>
<li><p>1-2 Ghz CPU</p></li>
<li><p>256-512 Mb RAM</p></li>
<li><p>20 Gb hard drive</p></li>
<li><p>Monitor</p></li>
<li><p>Printer</p></li>
</ul></td>
</tr>
<tr class="even">
<td><h2 id="section-1" class="unnumbered"></h2></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Central Processing Unit (CPU) Requirements (cont.)</strong></td>
<td><p><u>Software</u></p>
<ul>
<li><p>Microsoft Windows XP, Windows 2000 or Windows NT with Intersystems Cache 5.x.x (4.1.4), (3.2.1) 20 user License</p></li>
</ul>
<p>or</p>
<ul>
<li><p>RedHat Linux 8.0 with Greystone GT.M</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="test-sites" class="unnumbered">Test Sites</h2></td>
<td><p>VistA BCBU software was tested at the following VA Sites and platforms prior to being released:</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="minimum-required-packages" class="unnumbered">Minimum Required Packages</h2></td>
<td>Before installing BCBU PSB*3*8, make sure that your VistA system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher):</td>
</tr>
</tbody>
</table>

|                                |                            |
|--------------------------------|----------------------------|
| Package                    | Minimum Version Needed |
| Kernel                         | 8.0                        |
| VA FileMan                     | 22.0                       |
| VA MailMan                     | 8.0                        |
| Health Level Seven (HL7)       | 1.6                        |
| Pharmacy Inpatient Medications | 5.0                        |
| Bar Code Med Admin (BCMA)      | 3.0                        |

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="installation-time-estimates" class="unnumbered">Installation Time Estimates</h2></td>
<td><p>VistA Bar Code Medication Administration Backup System (BCBU) patch installation time is less than 2 minutes during off peak hours. The time for workstation setup is approximately 30 minutes.</p>
<p><strong>Important!</strong> You should install and test BCBU patches in your test accounts BEFORE installing in your production accounts.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="required-patches" class="unnumbered">Required Patches</h2></td>
<td>Before installing BCBU patches, make sure that the required released patches listed in the Patch Descriptions are installed:</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="users-on-the-system" class="unnumbered">Users on the System</h2></td>
<td>Users may remain on the system; however, the VistA Bar Code Medication Administration Backup System (BCBU) installation should be done during off peak hours when minimal Pharmacy activity is occurring.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="options-out-of-order" class="unnumbered">Options Out of Order</h2></td>
<td>The options, <em>Inpatient Order Entry</em> [PSJ OE] and <em>Non-Verified/Pending Orders</em> [PSJU VBW] are to be placed out of order during installation.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="namespace" class="unnumbered">Namespace</h2></td>
<td>VistA Bar Code Medication Administration Backup System (BCBU) routine namespace is ALPB. The options/protocols/templates/parameters and keys use the PSB namespace. Files are distributed under the PSB namespace, but use ALPB global namespace.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="data-dictionary-changes" class="unnumbered">Data Dictionary Changes</h2></td>
<td><p>There are no changes made to the Data Dictionaries, but two new files have been added. These files are located on both the workstation and the VistA server, but are only populated on the workstation.</p>
<ul>
<li><p>^ALPB(53.7, BCMA Backup Data</p></li>
<li><p>^ALPB(53.71, BCMA Backup Parameters</p></li>
</ul>
<p>Journaling is not recommended for the ALPB global.</p>
<p><span id="p73_10" class="anchor"></span></p>
<p>There is one Data Dictionary change to support Clinic Orders in BCMA with the install of PSB*3*73.</p>
<ul>
<li><p>CLINIC NAME field (#3.5) was added to the ORDER NUMBER file multiple field (#9).</p></li>
</ul>
<p><span id="datadictionary_9" class="anchor"></span>There are three data dictionary changes to support Transdermal Medications in BCMA with the install of PSB*3*87.</p>
<ul>
<li><p>ASSOC. MED LOG GIVE DATE/TIME field (#4)</p></li>
<li><p>ASSOC. MED LOG GIVE ENTERED BY field (#5)</p></li>
<li><p>ASSOC. MED LOG GIVE STATUS MSG field (#6)</p></li>
</ul>
<p>The above fields were added to the MED LOG DATE/TIME field (#10).</p>
<p><span id="P9_Hazrdous_Handle" class="anchor"></span>There are two data dictionary changes to support Hazardous to Handle and Hazardous to Handle drugs in BCBU with the installation of PSB*3*108:</p>
<ul>
<li><p>The HAZARDOUS TO HANDLE field (#14) was added to the BCMA BACKUP DATA file (#53.7);</p></li>
<li><p>The HAZARDOUS TO DISPOSE field (#15) was added to the BCMA BACKUP DATA file (#53.7).</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="resource-requirements" class="unnumbered"><br />
Resource Requirements</h2></td>
<td><p>This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.</p>
<ul>
<li><p>Routines 29</p></li>
<li><p>Globals 1 (^ALPB)</p></li>
<li><p>Files 2 (53.7, 53.71)</p></li>
<li><p>^ALPB Size Backup data= 268,288 bytes<br />
(131 blocks) per order</p></li>
</ul>
<p><strong>Note:</strong> Population of the ALPB global will only occur on the workstation, there is no global growth on the VistA server. ALPB global size estimate was acquired by dividing the number of blocks consumed by the total number of orders in file 53.7. This results in the number of blocks per order, which is multiplied by 2048, which is the number of bytes per block in Cache.</p>
<ul>
<li><p>FTEE Support .2</p></li>
<li><p>FTEE Maintenance .2</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="printers" class="unnumbered">Printers</h2></td>
<td><p>Your site should provide dedicated printers for each of the contingency workstations, which would allow printing of the MAR or MAH if the network was down.</p>
<p><strong>Note:</strong> The printer must have the capability to print 132 characters per line.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="routines-installed" class="unnumbered">Routines Installed</h2></td>
<td><p>Review the listing below to learn the routines installed on your site's VistA Server during the installation of patch PSB*3*8. The first line of each routine briefly describes its general function.</p>
<p><strong>Note:</strong> You can use the Kernel <em>First Line Routine Print</em> option to print a list containing the first line of each ALPB routine.</p></td>
</tr>
<tr class="even">
<td><h2 id="section-2" class="unnumbered"></h2></td>
<td></td>
</tr>
</tbody>
</table>

> BCMA Routines Installed on VistA Server

> ALPB8

> ALPBBK

> ALPBCBU

> ALPBELOG

> ALPBFRM1

> ALPBFRM2

> ALPBFRMU

> ALPBGEN

> ALPBGEN1

> ALPBGEN2

> ALPBHL1

> ALPBHL1U

> ALPBIN

> ALPBIND

> ALPBINP

> ALPBOP

> ALPBPALL

> ALPBPARM

> ALPBPCLN

> ALPBPPAT

> ALPBPWRD

> ALPBSP1

> ALPBSP2

> ALPBSPAT

> ALPBSWRD

> ALPBUTL

> ALPBUTL1

> ALPBUTL2

> ALPBUTL3

# Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="vista-server-installation-instructions" class="unnumbered">VistA Server Installation Instructions</h2></td>
<td>VistA Bar Code Medication Administration Backup System (BCBU) patch distribution is done by using the VA KIDS package. An example of this installation is found at the end of this installation guide.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="pc-workstation-database-initialization" class="unnumbered">PC Workstation Database Initialization</h2></td>
<td><p>Once the PC Workstation(s) have been setup and assigned an IP address, proceed with setting up the workstation link.</p>
<p>Create a link (node) for the PC workstation. This will be the regular transmission node. Name it "BC" and the ward. For example, if the ward is 2A the link could be called "BC 2A". This will indicate that the link is tied to a BCBU package and where the contingency workstation is located. Use the <em>Link Edit</em> [HL EDIT LOGICAL LINK] option of the HL Interface menu. An example of this installation is found at the end of this installation guide in the Sample PC Workstation Database Initialization Section.</p>
<p><span id="p73_12" class="anchor"></span></p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="mar-reports" class="unnumbered">MAR Reports</h2></td>
<td>Various MAR reports are located at the end of this installation guide under the Contingency PC Workstation Reports Section.</td>
</tr>
</tbody>
</table>

Please refer to the following documents for additional Installation Information:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="bcma-backup-system-bcbu-intersystems-cache-installation-setup" class="unnumbered">BCMA Backup System (BCBU) InterSystems Cache Installation Setup</h2></td>
<td>Refer to "Bar Code Medication Administration Backup System (BCBU) InterSystems Caché Installation Setup" guide for a systematic installation of Caché install on a PC workstation.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="bcma-backup-system-bcbu-linux-installation-setup" class="unnumbered">BCMA Backup System (BCBU) Linux Installation Setup</h2></td>
<td><p>Refer to "Bar Code Medication Administration Backup System (BCBU) Linux Installation Setup" for systematic installation of Linux on a PC workstation.</p>
<p>This manual also includes step-by-step installation of GT/M, VistA, and the Bar Code Medication Administration Backup System (BCBU) on the Linux workstation.</p></td>
</tr>
</tbody>
</table>

# # Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p73_13" class="anchor"></span>Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: INSTall Package(s)

Select INSTALL NAME: PSB\*3.0\*73 12/6/13@14:30:01

=\> PSB\*3\*73 v10 ;Created on Dec 03, 2013@12:42:21

This Distribution was loaded on Dec 06, 2013@14:30:01 with header of

PSB\*3\*73 v10 ;Created on Dec 03, 2013@12:42:21

It consisted of the following Install(s):

PSB\*3.0\*73

Checking Install for Package PSB\*3.0\*73

Install Questions for PSB\*3.0\*73

Incoming Files:

53.7 BCMA BACKUP DATA (Partial Definition)

> **NOTE:** You already have the 'BCMA BACKUP DATA' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

PSB\*3.0\*73

­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­

Installing Data Dictionaries:

Dec 06, 2013@14:43:10

Installing PACKAGE COMPONENTS:

Installing OPTION

Dec 06, 2013@14:43:10

Updating Routine file...

Updating KIDS files...

PSB\*3.0\*73 Installed.

Dec 06, 2013@14:43:11

Install Message sent \#1327

­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­

+­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­+

100% \| 25 50 75 \|

Complete +­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­­+

Install Completed

# Sample PC Workstation Database Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When initializing the workstations, you add an entry at the HL Logical Link Node prompt for each pc workstation your site has. The name of each link should represent the actual workstation location. For example, if you have a workstation on Ward 2A, the name of the workstation should be BC 2A. Associating the name of the HL Logical Link Node with the ward where the workstation is located, will aid in locating specific workstations should a problem arise. Once you have initialized the workstation with the correct workstation location, you can update the workstation with the users from the VistA system that have the \[PSB GUI CONTEXT - USER\] option. This initialization process will queue the activity and when complete send an alert.

On new installations, check the Parameter Value. The parameter can be left off until the workstation is ready to be initialized. If the workstation is already running, <u>do not</u> turn the Parameter Value off. Use the *General Parameter Tools* \[XPAR MENU TOOLS\] option to edit the parameter values.

XPAR MENU TOOLS     General Parameter Tools

LV List Values for a Selected Parameter  
LE List Values for a Selected Entity  
LP List Values for a Selected Package  
LT List Values for a Selected Template  
EP Edit Parameter Values  
ET Edit Parameter Values with Template  
EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: ep Edit Parameter Values  
--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: PSB BKUP ONLINE

---------- Setting PSB BKUP ONLINE  for Package: BAR CODE MED ADMIN ----------

Value: YES//\<ENTER\>

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME: PSB BKUP IPH BCMA Contingency Active Pharm Order

----------- Setting PSB BKUP IPH  for Package: BAR CODE MED ADMIN -----------

Value: 7// \<ENTER\>

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME: PSB BKUP MEDLG BCMA Contingency MedLog DFT

---------- Setting PSB BKUP MEDLG  for Package: BAR CODE MED ADMIN ----------

Value: 15// \<ENTER\>

-------------------------------------------------------------------------------

Continue with the Workstation setup.

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: INTERFACE Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL Link Edit

Select HL LOGICAL LINK NODE: BC 2A

INSTITUTION:\<ENTER\> leave blank

DOMAIN: \<ENTER\> leave blank

AUTOSTART: Enabled

QUEUE SIZE: 10

LLP TYPE: TCP

TCP/IP SERVICE TYPE: CLIENT (SENDER)

TCP/IP ADDRESS: (workstation IP address)

TCP/IP PORT: (10000)

ACK TIMEOUT:10 RE-TRANSMISSION ATTEMPTS: 2

READ TIMEOUT:10 EXCEED RE-TRANSMIT ACTION: restart

BLOCK SIZE: 256

STARTUP NODE: leave blank PERSISTENT: NO

RETENTION: 120 UNI-DIRECTIONAL WAIT: leave blank

Save the link

Sign out and then sign back in by doing the following:

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: PSB BCBU VISTA MAIN BCMA Backup System (VISTA)

PSB BCBU VISTA MAIN BCMA Backup System (VISTA)

LNK Associate Backup Workstations with a Division  
DFT Default Workstation Initialize  
DIV Divisional Workstation Initialize  
USR Initialize a Backup Workstation with BCMA Users  
PAT Singe Patient Init

Select BCMA Backup System (VISTA) Option: LNK Associate Backup Workstations with a Division

Do you want all backup data to go to the same group of

backup devices regardless of the patient's division?

Enter Yes or No: YES// \<ENTER\>

Select one of the following:

A Add a Logical Link

D Delete a Logical Link

OPERATION: ADD// \<ENTER\> Add a Logical Link

The following DEFAULT links are associated with this package:

BC KEVC

BC SID

BC KEVINK

BC SFVA

Select HL LOGICAL LINK: BC 2A ...Added

Select HL LOGICAL LINK: ?

LNK Associate Backup Workstations with a Division  
DFT Default Workstation Initialize  
DIV Divisional Workstation Initialize  
USR Initialize a Backup Workstation with BCMA Users  
PAT Singe Patient Init

> **NOTE:** If you want to remove an HL7 Link from your system, make sure you use the *LNK Associate Backup Workstation with a Division* option to delete the logical link association prior to deleting the link in HL7. If this is not done, you will get undefined errors on the VistA system. It is recommended that the Workstation Initialize be queued to run during non-peak hours. These inits may run for several hours depending on the parameter settings.

Select BCMA Backup System (VISTA) Option: DFT \<RET\> Default Workstation Initialize

Include all workstations

Enter Yes or No? YES// NO

Select WorkStation Link : BC 2A

Selected Workstations

BC 2A

Select WorkStation Link :

Requested Start Time: NOW// \<RET\> (FEB 18, 2003@14:28:13)

2624847

LNK Associate Backup Workstations with a Division  
DFT Default Workstation Initialize  
DIV Divisional Workstation Initialize  
USR Initialize a Backup Workstation with BCMA Users  
PAT Singe Patient Init

Select BCMA Backup System (VISTA) Option: USR Initialize a Backup Workstation with BCMA Users

This option searches for users that hold the option, 'PSB GUI CONTEXT - USER'

and if they are active users, transmits the information to your BCMA Backup Workstations.

NOTE that you must have completed the step of assigning workstations to either a single default group or by division.

Do you wish to continue? YES// \<ENTER\>

Do you wish to queue this init? YES//\<ENTER\>

Requested Start Time: NOW// \<ENTER\> (FEB 20, 2003@17:17:02)

TASK \#: 2625005

LNK Associate Backup Workstations with a Division  
DFT Default Workstation Initialize  
DIV Divisional Workstation Initialize  
USR Initialize a Backup Workstation with BCMA Users  
PAT Singe Patient Init

You have PENDING ALERTS  
 Enter "VA to jump to VIEW ALERTS option

Select BCMA Backup System (VISTA) Option: "VA

1.I BCBU INIT Started Feb 20, 2003@17:17:04 and finished Feb 20, 2003@17:2  
Select from 1 to 1  
or enter ?, A, I, D, F, S, P, M, R, or ^ to exit: 1

Processed Alert Number 1  
BCBU INIT Started Feb 20, 2003@17:17:04 and finished Feb 20, 2003@17:27:57.  
556

Menu option from the BCBU Contingency Workstation for parameter settings

Select BCMA Backup System (Wrkstn) Option: MM BCMA Backup System Management Menu

EL BCMA Backup System Error Log

PE Edit Workstation Parameter Settings

PO Purge Orders Past X days old

Select BCMA Backup System Management Menu Option: PE Edit Workstation Parameter Settings

Workstation Parameter ONE

BCBU Workstation Parameter Setup

-----------------------------------------------------------------------------

DEFAULT DAYS FOR MAR: 7

DEFAULT MAR PRINTER: BCBU

PURGE ORDER DAYS:

PURGE PATIENT:

MED-LOG NUMBER:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSB BCBU MANAGEMENT MENU

BCMA Backup System Management Menu

This Menu contains all Management options for the BCMA Contingency (Workstation Menu)

TYPE: menu

ITEM: PSB BCBU ERROR LOG

ITEM: PSB BCBU WRKSTN PARAMETER EDIT

ITEM: PSB BCBU WRKSTN PURGE ORDERS

PSB BCBU ERROR LOG

BCMA Backup System Error Log

This option is used to view the Error Log. (Workstation Menu)

TYPE: run routine Routine: ALPBELOG

PSB BCBU WRKSTN PARAMETER EDIT

Edit Workstation Parameter Settings

This option will allow the user to edit Site definable parameter settings for the BCMA Contingency Workstation. (Workstation Menu)

TYPE: ScreenMan

DIC {DIC}: ALPB(53.71, DIC(0): A

DIC(A): Workstation Parameter: DR{DDS}: \[PSB BCBU PARAMETERS\]

DDSFILE: 53.71 DDSPAGE: 1

PSB BCBU WRKSTN PURGE ORDERS

Purge Orders Past X days old

This option purges order information based on stop date first. Purge is also based on parameter setting for number of days to hold patient orders (default is 7 days) and parameter setting for number of days to hold patient record (default is 30 days with no order information). (Workstation Menu)

TYPE: run routine Routine: ALPBOP

PSB BCBU WRKSTN MAIN

This is the main menu for the BCMA Backup system -- the ward workstation containing the BCMA backup/contingency data. (Workstation Menu)

TYPE: menu

<span id="p73_19" class="anchor"></span>ITEM: PSB BCBU SHOW PATIENT

ITEM: PSB BCBU PRINT MAR ALL

ITEM: PSB BCBU PRINT MAR PATIENT

ITEM: PSB BCBU PRINT MAR WARD

ITEM: PSB BCBU MANAGEMENT MENU

ITEM: PSB BCBU WARD LIST

ITEM: PSB BCBU PRINT BLK MAR

ITEM: PSB BCBU PRINT MAR ALL CLINICS

ITEM: PSB BCBU PRINT MAR CLINIC

PSB BCBU SHOW PATIENT

List/Display Orders

This option will display orders to the screen by individual patient. (Workstation Menu)

TYPE: run routine ROUTINE: ALPBSPAT

PSB BCBU SHOW WARD

Display Orders for Selected Ward

This option will display orders to the screen by Ward. (Workstation Menu)

TYPE: run routine ROUTINE: ALPBSWRD

PSB BCBU PRINT MAR ALL

Print MAR for All Wards

This option prints a MAR report for all wards. (Workstation Menu)

TYPE: run routine ROUTINE: ALPBPALL

PSB BCBU PRINT MAR PATIENT

Print MAR for Selected Patient

This option prints a MAR report by individual patients. (Workstation Menu)

TYPE: run routine ROUTINE: ALPBPPAT

PSB BCBU PRINT MAR WARD

Print MAR for Selected Ward

This option prints a MAR report by individual wards. (Workstation Menu)

TYPE: run routine ROUTINE: ALPBPWRD

PSB BCBU WARD LIST

List of Wards in BCMA Backup File

This option will display all the wards available on the workstation. (Workstation Menu)

TYPE: run routine ROUTINE: WARDLIST^ALPBUTL

PSB BCBU PRINT BLK MAR

Print Blank Mar for Selected Patient

This option allows the user to select a patient from the BCMA contingency and print a blank 3 or 7 day MAR. The MAR will only contain patient info.

TYPE: run routine ROUTINE: ALPBBK

PSB BCBU PRINT MAR ALL CLINICS

Print MAR for All Clinics

This option prints a MAR report for all the clinics available on the workstation. (Workstation Menu)

TYPE: run routine ROUTINE: EN^ALPBPCLN("ALL")

PSB BCBU PRINT MAR CLINIC

Print MAR for Selected Clinic

This option prints a MAR report for a selected clinic.

(Workstation Menu)

TYPE: run routine ROUTINE: EN^ALPBPCLN("CLN")

PSB BCBU VISTA MAIN

BCMA Backup System (VISTA)

This is the Primary Menu for the BCMA Backup Contingency. (VISTA Menu)

TYPE: menu

ITEM: PSB BCBU INIT WRKSTN DFT

ITEM: PSB BCBU INIT WRKSTN DIV

ITEM: PSB BCBU LINK ASSOCIATIONS

ITEM: PSB BCBU USER INIT

ITEM: PSB BCBU INIT SINGLE PT

PSB BCBU INIT WRKSTN DFT

Default Workstation Initialize

This option is used to initialize Workstations that are linked as default. This option will send inpatient and clinic orders to the BCMA Contingency to all or selected workstations. For non-divisional sites. (VISTA Option)

TYPE: run routine ROUTINE: OPT^ALPBIND

PSB BCBU INIT WRKSTN DIV

Divisional Workstation Initialize

This option is used to initialize Workstations that are linked by Division. This option will send inpatient and clinic orders to the BCMA Contingency workstation for all or selected divisions. For multi-divisional sites only. (VISTA Option)

TYPE: run routine ROUTINE: OPT^ALPBIN

PSB BCBU LINK ASSOCIATIONS

Associate Backup Workstations with a Division

For sites running the REAL-TIME BCMA BACKUP interface, use this option to assign your backup workstations to specific divisions. If you are not a multidivisional site, associate all backup workstations with a single division.

When HL7 events occur, the division associated with the patient will be used to determine which workstations will get the message. (VISTA Menu)

TYPE: run routine ROUTINE: ALPBPARM

PSB BCBU USER INIT

Initialize a Backup Workstation with BCMA Users

This option searches the VISTA New Person file for authorized BCMA users and generates a version 2.4 HL7 message. Messages are addressed dynamically based on the parameter definitions for BCMA Backup using divisions or the default group.

TYPE: run routine ROUTINE: INIT^ALPBGEN2

PSB BCBU INIT SINGLE PT

Single Patient Init

This option will send inpatient and clinic orders to the BCMA Contingency workstation for a single patient.

TYPE: run routine ROUTINE: SNDPT^ALPBIND

## HL7 Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSB BCBU CLIENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ~\|\\

### PSB BCBU SERVER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTIVE/INACTIVE: ACTIVE

HL7 ENCODING CHARACTERS: ~\|\\

PSB PMU RECV

ACTIVE/INACTIVE: ACTIVE

COUNTRY CODE: USA

HL7 ENCODING CHARACTERS: ~&^\\

HL7 FIELD SEPARATOR: \|

### PSB PMU SEND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTIVE/INACTIVE: ACTIVE

COUNTRY CODE: USA

HL7 ENCODING CHARACTERS: ~&^\\

HL7 FIELD SEPARATOR: \|

## HL7 Message Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unit Dose Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p73_22" class="anchor"></span>Conditionally sending (exclusively for clinic orders) the clinic name in the ORC segment for orders placed in a clinic:

PID^^000-00-0000\~~^10748~2~M10^^BCMAPATIENT~TWO~^^19350517^M^^^^^^^^^^^000002222  
PV1^1^I^4E M-KC~SE403~3^^^^5468~BCMAPROVIDER~ONE~^^^^^^^^^^^NSC VETERAN  
ORC^XX^~OR^1U~PS^^DC~discontinued^^^^199709191028-0400^33~BCMAPROVIDER,ONE^^7356~BCMAPHARMACIST,ONE^^^199709191028-0400^\~~99ORN\~\~~^^^^^SOUTH OUTPATIENT CLINIC

RXO^\~\~\~\~~99PSP^^^^^^^^^^^^^^^^  
RXE^&&2&~Q4H PRN&\~~199709191028-0400~19970920120402-0400\~\~~^326.2485~OXYCODONE HCL 5MG/ACETAMINOPHEN    

        325MG TAB~99NDF~7106~OXYCODONE 5MG/ACETAMINOPHEN 325MG TAB UD~99PSD^^^\~\~~0\~~99PSU^\~\~\~\~~99PSF^^^^^^^^24133~BCMAPROVIDER,TWO

      ~99NP^^^^^^^^^^^^\~\~\~\~~99PSU  
RXR^\~\~~1~ORAL~99PSR^^^^  
ZRX^^^^^24133~BCMAPROVIDER,TWO~99NP^

# NTE^21^L^These are long word processing text special instructions that can be\\br\entered via CPRS as provider comments and then optionally included in the\\br\Pharmacists Special instructions as is or amended by the phrmamcists\\br\with more in

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

formation optionally added.\\br\\

RXR^\~\~~1~ORAL~99PSR^^^^  
ZRX^^^^^24133~BCMAPROVIDER,TWO~99NP^

### IV Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Conditionally sending (exclusively for clinic orders) the clinic name in the ORC segment for orders placed in a clinic:

 PID^^000-00-0000\~~^10748~2~M10^^BCMAPATIENT~TWO~^^19350517^M^^^^^^^^^^^000002222  
 PV1^1^I^4E M-KC~SE403~3^^^^5468~BCMAPROVIDER~ONE~^^^^^^^^^^^NSC VETERAN  
 ORC^XX^8547404;1~OR^53V~PS^^CM~finished/verified by pharmacist(active)^^^^20021206135950-0400^24133~BCMAPROVIDER,TWO ^^24133~BCMAPROVIDER,TWO^^^200212061359-

         0400^\~~99ORN\~\~~^^^^^NORTH OUTPATIENT CLINIC

 RXO^\~\~~1062~MULTIVITAMIN INJ,SOLN~99PSP^^^^^^^^^^^^^^^^  
 RXE^~&\~~200212061359-0400~200212071400-0400^^^^^^^^^^^^^24133~BCMAPROVIDER,TWO~99NP^^^^^^^^^10^\~\~\~~ml/hr~PSU^^  
 NTE^21^L^I would like to enter these provider comments  
 RXC^A^\~\~~1062~MULTIVITAMIN~99PSP^10^\~\~~PSIV-1~ML~99OTH^^^^^^^^^^^^^^^^^^^^  
 RXC^A^\~\~~688~FOLIC ACID~99PSP^2^\~\~~PSIV-4~MG~99OTH^^^^^^^^^^^^^^^^^^^^  
 RXC^A^\~\~~1488~TRACE ELEMENTS~99PSP^2^\~\~~PSIV-1~ML~99OTH^^^^^^^^^^^^^^^^^^^^  
 RXC^B^\~\~~490~DEXTROSE 5%/WATER~99PSP^1000^\~\~~PSIV-1~ML~99OTH^^^^^^^^^^^^^^^^^^^^

 ZRX^^^N^^24133~BCMAPROVIDER,TWO~99NP^IV

### Med Log

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PID^^000-00-0000\~~^10748~2~M10^^BCMAPATIENT~TWO~^^19350517^M^^^^^^^^^^^000002222

 PV1^1^I^4E M-KC~SE403~3^^^^5468~BCMAPROVIDER~ONE~^^^^^^^^^^^NSC VETERAN  
 ORC^ML^^330U~PS^^G~GIVEN^^^^20010414131522-0400^15454~BCMAPROVIDER,THREE

## Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSB BKUP DEFAULT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: Package-specific 'default' Logical Links

MULTIPLE VALUED: Yes

INSTANCE TERM: Logical Link

VALUE DATA TYPE: pointer

VALUE DOMAIN: 870

VALUE HELP: Enter the HL7 logical link

INSTANCE DATA TYPE: pointer

INSTANCE DOMAIN: 870

INSTANCE HELP: Enter the HL7 logical link

DESCRIPTION: This parameter is used by the BCMA Backup system to route messages to a "default" group of HL7 Logical Links that are associated with the BCMA package rather than individual divisions. When the default group is defined, all messages will be routed to this group rather than using division-based grouping under the following conditions:

1.  If a call is made to the API, GET^ALPBPARM, and the division parameter is not present or null.
2.  If a call is made to the API, GET^ALPBPARM, and the division specified has no logical links associated with it.

PRECEDENCE: .5

> ENTITY FILE: PACKAGE

### PSB BKUP MACHINES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: Division-specific Logical Links

MULTIPLE VALUED: Yes

INSTANCE TERM: Logical Link

VALUE DATA TYPE: Pointer

VALUE DOMAIN: 870

VALUE HELP: Enter the HL7 Logical Link

INSTANCE DATA TYPE: pointer

INSTANCE DOMAIN: 870

INSTANCE HELP: Enter the HL7 Logical Link

DESCRIPTION: This parameter defines the BCMA Backup Logical Links that may be associated with a division when there are one or more divisions at a site.

PRECEDENCE: 1

ENTITY FILE: DIVISION

### PSB BKUP ONLINE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: BCMA Contingency Online

VALUE DATA TYPE: yes/no

DESCRIPTION: This parameter is used by the BCMA Backup system to activate the Contingency software. If the value is set to NO, then no HL7 messages will be sent to the Workstation. This does not affect the workstation initialization option.  
PRECEDENCE: 1

ENTITY FILE: PACKAGE

### PSB BKUP IPH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: BCMA Contingency Active Pharm Order

VALUE DATA TYPE: numeric

DESCRIPTION: The BCMA Backup Contingency software uses this parameter. During the Workstation initialization process, this tells the process how many days of historic Inpatient Medication <span id="p73_25" class="anchor"></span>and Clinic Orders to capture. It is based off the fact the order was active during that time.

PRECEDENCE: 1

ENTITY FILE: PACKAGE

### PSB BKUP MEDLG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: BCMA Contingency MedLog DFT

VALUE DATA TYPE: numeric

DESCRIPTION: The BCMA Backup Contingency software uses this parameter. During the Workstation initialization process, this tells the process how many days of historic Med Log entries of Inpatient Medication and Clinic Orders to capture.

PRECEDENCE: 1

ENTITY FILE: PACKAGE

### PSB BKUP DOM FILTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISPLAY TEXT: Filter out DOM patients

MULTIPLE VALUED: No

VALUE DATA TYPE: yes/no

VALUE HELP: Should the contingency backup filter out DOM patients?

DESCRIPTION: This parameter is used by the BCMA backup system to determine if DOM

 patients are included in the backup.  If the value is set to YES, DOM patients will be filtered out of the backup and will not be sent to the workstation.  If the value is NO or blank, DOM patients will be sent to the backup workstation.

PRECEDENCE: 1

ENTITY FILE: PACKAGE

## List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSB ERROR LOG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80

TOP MARGIN: 4

BOTTOM MARGIN: 20

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

PROTOCOL MENU: PSB ERROR LOG MENU

SCREEN TITLE: BCMAbu Error Log

ALLOWABLE NUMBER OF ACTIONS: 1

AUTOMATIC DEFAULTS: YES

HIDDEN ACTION MENU: VALM IDDEN ACTIONS

ARRAY NAME: ^TMP("ALPBELOG",\$J)

EXIT CODE: D EXIT^ALPBELOG

HEADER CODE: D HDR^ALPBELOG

HELP CODE: D HELP^ALPBELOG

ENTRY CODE: D INIT^ALPBELOG

### PSB SELECT ORDERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80

TOP MARGIN: 7

BOTTOM MARGIN: 19

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

PROTOCOL MENU: PSB ORDERS MENU

SCREEN TITLE: BCMAbu ACTIVE Orders List

ALLOWABLE NUMBER OF ACTIONS: 1

HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME: ^TMP("ALPBORDS",\$J)

ITEM NAME: OrderNum

COLUMN: 2

WIDTH: 10

DISPLAY TEXT: Order No.

ITEM NAME: OrderType

COLUMN: 22

WIDTH: 4

DISPLAY TEXT: Type

ITEM NAME: Status

COLUMN: 14

WIDTH: 7

DISPLAY TEXT: Status

ITEM NAME: Meds

COLUMN: 28

WIDTH: 45

DISPLAY TEXT: Medication(s)

ITEM NAME: SelNum

COLUMN: 2

WIDTH: 5

DISPLAY TEXT: Rec#

EXIT CODE: D EXIT^ALPBSP1

HEADER CODE: D HDR^ALPBSP1

HELP CODE: D HELP^ALPBSP1

ENTRY CODE: D INIT^ALPBSP1

### PSB SELECT PATIENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80

TOP MARGIN: 4

BOTTOM MARGIN: 15

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

PROTOCOL MENU: PSB PATIENT MENU

SCREEN TITLE: BCMAbu Patient List (All)

ALLOWABLE NUMBER OF ACTIONS: 1

HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME: ^TMP("ALPBPLIST",\$J)

ITEM NAME: RecNum

COLUMN: 2

WIDTH: 6

DISPLAY TEXT: Rec \#

ITEM NAME: Patient

COLUMN: 2

WIDTH: 30

DISPLAY TEXT: Patient

ITEM NAME: SSN

COLUMN: 33

WIDTH: 9

DISPLAY TEXT: SSN

ITEM NAME: WARD

COLUMN: 43

WIDTH: 15

DISPLAY TEXT: Ward

ITEM NAME: ROOM

COLUMN: 62

WIDTH: 5

DISPLAY TEXT: Room

ITEM NAME: BED

COLUMN: 72

WIDTH: 5

DISPLAY TEXT: Bed

EXIT CODE: D EXIT^ALPBSPAT

HEADER CODE: D HDR^ALPBSPAT

HELP CODE: D HELP^ALPBSPAT

ENTRY CODE: D INIT^ALPBSPAT

### PSB SHOW ORDERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF LIST: DISPLAY

RIGHT MARGIN: 80

TOP MARGIN: 7

BOTTOM MARGIN: 20

OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

SCREEN TITLE: BCMAbu Selected Order(s)

ALLOWABLE NUMBER OF ACTIONS: 1

AUTOMATIC DEFAULTS: YES

HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME:^TMP("ALPBFORM",\$J)

EXIT CODE: D EXIT^ALPBSP2

HEADER CODE: D HDR^ALPBSP2

HELP CODE: D HELP^ALPBSP2

ENTRY CODE: D INIT^ALPBSP2

## HL Communication Server Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These parameters exist only on the workstations and is included in the .dat file.

ONE: 1 DOMAIN: BCMABU.MED.VA.GOV

DEFAULT PROCESSING ID: training INSTITUTION: SOFTWARE SERVICE

DEFAULT NUMBER INCOMING FILERS: 2 DEFAULT NUMBER OUTGOING FILERS: 2

PURGE COMPLETED MESSAGES: 2 PURGE AWAITING ACK MESSAGES: 2

PURGE ALL MESSAGES: 4

Select HL LOGICAL LINK NODE: LISTNER

NODE: LISTNER LLP TYPE: TCP

DEVICE TYPE: Single-threaded Server

AUTOSTART: Enabled

SHUTDOWN LLP ?: NO

QUEUE SIZE: 10 RE-TRANSMISSION ATTEMPTS: 2

BLOCK SIZE: 256 READ TIMEOUT: 2

ACK TIMEOUT: 10 EXCEED RE-TRANSMIT ACTION: restart

TCP/IP PORT: 10000 TCP/IP SERVICE TYPE: SINGLE LISTENER

PERSISTENT: NO RETENTION: 120

## Files Associated with GT.M/Linux BCMA:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are provided with the GT.M version of Bar Code Medication Administration Backup System (BCBU) and are unpacked from the bcma_files.tar.gz file into \$HOME of the BCMA manager account.

.bashrc – this is the BCMA manager's *\$HOME*/*.bashrc* file. This file defines GT.M related global variables, sets convenient aliases and sets terminal characteristics. This file may be edited but all GT.M variable and terminal definitions should be retained to guarantee the proper functioning of the GT.M database.

bcmabashrc – *install_bcma* creates a generic "bcma" Linux account tied to VistA. *bcmabashrc* is renamed to */home/bcma/.bashrc* and is called with each “bcma” user login. The call to this file ties the user to VistA and prevents access to the Linux or GT.M level as well as defining GT.M related global variables.

bcma.gld – this is the GT.M global directory file which defines the location of the BCMAbu database. *install_bcma* edits this file automatically to account for the directory structure specified by the installer. The GT.M database utility, GDE, accesses this file.

cronjrnclean – this file is used to generate the crontab procedure (found in /var/spool/tar/bcma_manager_name) which runs nightly to flip the GT.M journal file, remove old journal files and remove temporary GT.M process related files in the manager’s \$HOME. This file is only used once during the BCMA install.

gcomp - run this file at your GT.M manager to recompile all M routines. At times, compiled objects may end up with the wrong user ownership (for example, if patches were installed and run as root). Run this script to correct such situations.

jrnclean – this file is called by /var/spool/tar/bcma_manager_name nightly at 1:00am to flip the GT.M journal file, remove old journal files and remove temporary GT.M process related files in the BCMA manager's \$HOME.

jrnoff - this file may be used to turn journaling off. Note that journaling is automatically enabled with every reboot of the system by *rc.local*.

jrnon – this file may be used to turn journaling on or flip the current journal file to a new one. It is called by *jrnclean*. Journal files are found in \$HOME/jrn of the bcma manager.

netmail_start – this file is called by *rc.local* during runlevel 5-system startup to start network mail on port 25. If netmail needs to be started manually, run this file as root (other users will not have the privileges to connect a process to port 25).

rc.local – this is a user-editable Linux file found in /etc/rc.d and is called during system startup and shutdown. This file calls *\$HOME/recoverall*, *\$HOME/jrnon*, *\$HOME/taskman_start* and *\$HOME/netmail_start* during system startup. It will call *\$HOME/zgstop* during system shutdown. If *rc.local* is successful in each of these calls, the following empty files will be created in \$HOME of the BCMA manager account: *recoverys, TaskMan, netmails*, and *rundowns*.

recoverall – this file is called by *rc.local* during system startup and attempts to recover the database should the system be shutdown uncleanly.

taskman_start – this file starts TaskMan automatically during system startup. If TaskMan needs to be started manually, run *taskman_start* as root (TaskMan automatically starts HL7 processes – the LISTNER link needs to connect with port 10000).

VistA– this script resides in the /home/bcma and /home/gtm manager directories and is called by the icon file \$HOME/.gnome-desktop/ VistA -icon for the respective users

\*-icon - these are the desktop icon files. The BCMA and GT.M manager users both have the VistA -icon, which will bring the user to the access/verify prompts. In addition to this, the GT.M manager user will also have the term-icon and editor-icon on its desktop to open a terminal session and gedit text editor, respectively.

zgstop - this file is called by *rc.local* during system shutdown to shutdown GT.M cleanly and performs a recovery if needed. Call this file as root if GT.M needs to be shutdown (only the root user will be permitted to stop ALL GT.M processes – if another user call zgstop, only its own processes will be shutdown). This file is derived from */usr/local/gtm/gstop*.

## Adding a BCMA printer to the Cache/NT Contingency system:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Contingency Workstation (VistA) printer:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Slave printers are defined in VistA as P22O/102 SLAVE CACHE/NT.

Test the printer through VistA.

DEVICE file entry:

NAME: P22O/102 SLAVE CACHE/NT \$I: 0

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: slave device for Cache/NT

MNEMONIC: SLAVE

SUBTYPE: C-VT220 TYPE: TERMINAL

<u>Network printer</u>:

<u>From the NT menu</u>:

1.  *Start/Settings/Printers/Add Printer*.
2.  Select the *My Computer* radio button then *Next* to continue.
3.  Click the *Add Port* button.
4.  Double click the *LPR Port* then fill in the IP address of the device and the name then *Close* to continue.
5.  Make sure the box for the newly created port is checked then *Next* to continue.
6.  Select the printer driver (note - you may need the NT install CD handy for this step) then *Next* to continue.
7.  Enter the printer name then *Next* to continue  
    Note: this is the value that will be used in the \$I below.
8.  Select shared or not shared then *Next* to continue.
9.  Try printing a test page; at this point, NT might start requesting the install CD for specific drivers.

<u>From the W2K menu</u>:

1.  *Start/Settings/Printers/Add Printer*.
2.  *Next* at the welcome add printer wizard box.
3.  Select the *Local Printer* radio button and uncheck the automatic detection for plug and play devices then *Next* to continue.
4.  Select the *Create a new port* radio button then select either *LPR* or *Standard TCPIP port* from the dropdown menu.

> \- For LPR:

- Fill in the IP address of the device and the name, then *Close* to continue.

> \- For TCP/IP:

- Click *Next* to continue in the welcome wizard window.
- Enter the printer name or IP address then *Next* to continue.
5.  Select the driver, then *Next* to continue.
6.  Enter the printer name, then *Next* to continue  
    Note: this is the value that will be used in the \$I below.
7.  Share or not, then *Next* to continue.
8.  Print a test page, then *Next* to continue.

### From within Contingency Workstation (VistA) Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  No special terminal types need to be used for Cache/NT network printing. Several HP-LASER terminal types are available in the TERMINAL TYPE file as installed.
2.  Create a new entry in the DEVICE file as per the example below. \$I syntax is \|PRN\|\\bcmaservername\LPR device defined above. In the example below, the A410 printer was defined as an LPR port through NT. The server name is VHAISADHC1
3.  Test the printer through VistA.

Examples:

DEVICE file entry:

NAME: A410 \$I: \|PRN\|\\VHAISADHC2\A410

LOCATION OF TERMINAL: A410 SUBTYPE: P-HP-P16

TYPE: TERMINAL

TERMINAL TYPE file entries:

NAME: P-HPLASER-P10 RIGHT MARGIN: 80

FORM FEED: \# PAGE LENGTH: 64

BACK SPACE: \$C(8) OPEN EXECUTE: W \*27,"E"

CLOSE EXECUTE: W \*27,"E" PROPORTIONAL SPACING: \$C(27)\_"(s1P"

DESCRIPTION: LASER PRINTER PORTRAIT MODE 10 CPI

NAME: P-HP-P16 RIGHT MARGIN: 132

FORM FEED: \$C(12,13) PAGE LENGTH: 58

BACK SPACE: \$C(8) OPEN EXECUTE: W \$C(27),"E",\$C(27),"&k2S”

CLOSE EXECUTE: W \$C(27),”E” DESCRIPTION: HP LASER JET 16 PITCH

## Adding a BCMA printer to the GT.M/Linux Contingency system:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Contingency Workstation (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>From the Linux menu</u>:

1.  Select *System Settings* then *Printing*.
2.  In the Red Hat printer config windows click *New* to create a new printer queue.
3.  Read the instructions then click *Forward* to continue.
4.  Specify 'local' or 'LOCAL' as the name for the new printer and select *local printer* radio button, then click *Forward* to continue.
5.  Accept */dev/lp0* as printer device to use, then click *Forward* to continue.
6.  Select the driver for your local printer, then click *Forward* to continue. *Postscript Printer* is usually acceptable for HP printers.
7.  Click *Apply* button to restart LPD.
8.  You may test the printer by selecting it in the Red Hat printer config window, then selecting *Test* from the horizontal menu.

### From within Contingency Workstation (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  P220/102 SLAVE GTM/LINUX entries are already pre-defined in VistA DEVICE file.
2.  Test the printer through VistA.

DEVICE file entries:

NAME: P220/102 SLAVE GTM/LINUX \$I: \$HOME/slave.dat

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: basic slave device for gtm/linux

ASK HOST FILE: NO SUPPRESS FORM FEED AT CLOSE: YES

OPEN PARAMETERS: newversion

MNEMONIC: SLAVE

SUBTYPE: P-SLAVE TEXT GTM/LINUX TYPE: HOST FILE SERVER

NAME: P220/102 HP 80 SLAVE GTM/LINUX \$I: \$HOME/slave.dat

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: HP 80 slave device for gtm/linux

ASK HOST FILE: NO SUPPRESS FORM FEED AT CLOSE: YES

OPEN PARAMETERS: newversion

MNEMONIC: SLAVE

SUBTYPE: P-SLAVE HP 80 GTM/LINUX TYPE: HOST FILE SERVER

NAME: P220/102 HP 132 SLAVE GTM/LINU \$I: \$HOME/slave.dat

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: HP 132 slave device for gtm/linux

ASK HOST FILE: NO SUPPRESS FORM FEED AT CLOSE: YES

OPEN PARAMETERS: newversion

MNEMONIC: SLAVE

SUBTYPE: P-SLAVE HP 80 GTM/LINUX TYPE: HOST FILE SERVER

TERMINAL TYPE file entries:

NAME: P-SLAVE HP 132 GTM/LINUX RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 60

BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"E",\*27,"(s16.7H",\*27,"&k3G"

CLOSE EXECUTE: W \*27,"E" U IO K IO(1,IO) C IO ZSYSTEM "lpr -lr "\_IO

NAME: P-SLAVE HP 80 GTM/LINUX RIGHT MARGIN: 80

FORM FEED: \# PAGE LENGTH: 60

BACK SPACE: \$C(8) OPEN EXECUTE: W \*27,"E",\*27,"&k3G"

CLOSE EXECUTE: W \*27,"E" U IO K IO(1,IO) C IO ZSYSTEM "lpr -lr "\_IO

NAME: P-SLAVE TEXT GTM/LINUX RIGHT MARGIN: 80

FORM FEED: \# PAGE LENGTH: 60

BACK SPACE: \$C(8)

CLOSE EXECUTE: U IO K IO(1,IO) C IO ZSYSTEM "lpr -r "\_IO

<u>Network printer</u>:

<u>From the Linux menu</u>:

1.  Select *System Settings* then *Printing*.
2.  In the Red Hat printer config windows click *New* to create a new printer queue
3.  Read the instructions then click *Forward* to continue.
4.  Specify the name of the new printer (example: A405) and select either the *Unix Printer* or *Jetdirect Printer* radio button as type (Note: Unix printer uses port 515 and Jetdirect uses port 9100), then click *Forward* to continue.
    1.  if Unix printer: Enter the printer hostname or IP in the *Server* box - no need to enter queue information.
    2.  if Jetdirect printer: Enter the printer hostname or IP in the *Printer IP* box - accept 9100 as the port value then click *Forward* to continue.
5.  Select the driver for your network printer, then click *Forward* to continue*.  
    *Note: *Postscript Printer is* usually acceptable for HP printers.
6.  Click *Apply* button to restart LPD.
7.  You may test the printer by selecting it in the Red Hat printer config window, then selecting *Test* from the horizontal menu.

### From within Contingency Workstation (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  P-TCP \* GTM/LINUX entries are already pre-defined in VistA TERMINAL TYPE file. You may use the VA FileMan *Transfer File Entries* option to create new terminal types using these as templates. Edit the OPEN EXECUTE fields accordingly to vary print characteristics.
2.  Create a new DEVICE file entry.
    1.  Note: The name of the new DEVICE must begin with the name of the Linux printer created above FOLLOWED BY A SPACE then a description (Example: "A405 - ADMIN 10/6/UP"). The CLOSE EXECUTE field of the TERMINAL TYPE being used parses the queue name from the first space backward)
    2.  I\$'s for network printers are normally /home/*Linux bcma mgr acct*/hfs/devicename.txt
    3.  Device TYPE - HFS
3.  Test the printer through VistA.

Examples:

DEVICE file entries:

NAME: A405 10/6/UP \$I: /home/gtmmgr/hfs/A405.dat

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: A405 ASK HOST FILE: NO

SUPPRESS FORM FEED AT CLOSE: YES OPEN PARAMETERS: newversion

SUBTYPE: P-TCP 10/6/UP GTM/LINUX TYPE: HOST FILE SERVER

NAME: A405 16/6/UP \$I: /home/gtmmgr/hfs/A405.dat

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: A405 ASK HOST FILE: NO

SUPPRESS FORM FEED AT CLOSE: YES OPEN PARAMETERS: newversion

SUBTYPE: P-TCP 16/6/UP GTM/LINUX TYPE: HOST FILE SERVER

TERMINAL TYPE file entries:

NAME: P-TCP 10/6/UP GTM/LINUX SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 60 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"E",\*27,"&k3G"

CLOSE EXECUTE: W \*27,"E" U IO K IO(1,IO) C IO ZSYSTEM "lpr -lrP "\_\$E(ION,1,\$F(ION," ")-1)\_" "\_IO

NAME: P-TCP 16/6/UP GTM/LINUX SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 60 BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"E",\*27,"(s16.7H",\*27,"&k3G"

CLOSE EXECUTE: W \*27,"E" U IO K IO(1,IO) C IO ZSYSTEM "lpr –lrP "\_\$E(ION,1,\$F(ION," ")-1)\_" "\_IO

## Workstation Queued Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tasks should be queued to run on the workstation. All except XMMGR-PURGE-AI-XREF (which has a rescheduling frequency of 7D) should have a rescheduling frequency of 1D. The GT.M and Cache dat files where released with these jobs scheduled properly but they should be checked, once TaskMan is started, to make sure they have run and are being rescheduled.

The following capture shows how to list the currently queued workstation tasks and verifies that the HL PURGE TRANSMISSIONS task has been rescheduled. Check the TaskMan error log should the jobs not appear to be run or scheduled properly.

Select Systems Manager Menu Option:

Core Applications ...

Device Management ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Management ...

HL7 Main Menu ...

Select Systems Manager Menu Option: TASKman Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: SCHEdule/Unschedule Options

Select OPTION to schedule or reschedule: ?

Answer with OPTION SCHEDULING NAME

Choose from:

XQBUILDTREEQUE (R)

XQ XUTL \$J NODES (R)

XUTM QCLEAN (R)

XUERTRP AUTO CLEAN (R)

XMCLEAN (R)

XMAUTOPURGE (R)

XMMGR-PURGE-AI-XREF (R)

HL PURGE TRANSMISSIONS (R)

HL TASK RESTART (R)

HL AUTOSTART LINK MANAGER (R)

PSB BCBU WRKSTN PURGE ORDERS (R)

You may enter a new OPTION SCHEDULING, if you wish

Enter OPTION to schedule.

Only allow Action, Print, and Run type options.

Answer with OPTION NAME

Do you want the entire OPTION List? N (No)

Select OPTION to schedule or reschedule: PSB BCBU WRKSTN PURGE ORDERS Purge Orders Past X days old

...OK? Yes// \<ENTER\> (Yes)

\(R\)

Edit Option Schedule

Option Name: PSB BCBU WRKSTN PURGE ORDERS

Menu Text: Purge Orders Past X days old TASK ID: 8709

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUN 3,2003@01:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Quick Reference Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 22%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action</strong></th>
<th><strong>Where</strong></th>
<th><strong>Completed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>Install patch PSB*3.0*8</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol type="A">
<li><p>FTP Software from an OI Field Office</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="2" type="A">
<li><p>Install using Kids</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><p>Workstation Setup</p></li>
</ol>
<p><strong>Note:</strong> Ensure that the workstation has a static IP Address.</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><ol type="A">
<li><p>Windows/Caché</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ol type="1">
<li><p>Setup Caché – InterSystems supplies software. Example of install can be found in the manual, "Bar Code Medication Administration Backup System (BCBU) InterSystems Cache Installation Setup".</p></li>
</ol></td>
<td>Workstation</td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>Shutdown Caché</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>Copy cache.dat file that was downloaded from the FTP site into C:\CACHESYS\folder. (If asked to replace file, answer yes.)</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>Remove the Read-Only attribute from the cache.dat file.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li><p>Ensure telnet is enabled in Caché Configuration.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li><p>Move ZSTU routine from VistA namespace to %SYS namespace.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li><p>Setup Telnet and Terminal users using Caché Control Panel.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li><p>Stop and Restart Caché.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="9" type="1">
<li><p>Create BCMA Backup shortcut.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol type="A">
<li><p>Linux/GT.M</p></li>
</ol></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ol type="1">
<li><p>Install Linux onto clean system</p></li>
<li><p>Example of install can be found in the manual, "Bar Code Medication Administration Backup System (BCBU) Linux Installation Setup. Make note of username entered and its password for future use. Also, remember the root password.</p></li>
</ol></td>
<td>Workstation</td>
<td><p>_________</p>
<p>_________</p></td>
</tr>
</tbody>
</table>

  
Action Where Completed

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 22%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ol start="3" type="1">
<li><p>Sign into Linux using the user created during the installation.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li><p>Enter super user mode ($ <u>su</u>)</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="5" type="1">
<li><p>Copy downloaded Linux files to an accessible location.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li><p>Ensure downloaded file has correct permissions.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="7" type="1">
<li><p>Run the install script. (./install_bcma)<br />
<strong>Note:</strong> BCMA manager account will be the user you created during the Linux install.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="8" type="1">
<li><p>Edit the TaskMan Site Parameters to enter the correct Box-Volume pair.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li><p>Restart TaskMan.</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>Workstation Database Initialization</p></li>
</ol></td>
<td></td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol type="A">
<li><p>On new installs check the parameter PSB BKUP ONLINE VALUE=yes</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="2" type="A">
<li><p>Add a new link using HL7 options.</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="3" type="A">
<li><p>Associate the new link to a division using PSB BCBU VistA MAIN option.</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="4" type="A">
<li><p>Start the new link using HL7 options.</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="5" type="A">
<li><p>Check the HL7 Site Parameter to make sure the field, "Is this a Production or Test Account", is set correctly. It must match the setting in the Vista account sending the messages</p></li>
</ol></td>
<td>Workstation</td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="6" type="A">
<li><p>Start the LISTNER link using HL7 options.</p></li>
</ol></td>
<td>Workstation</td>
<td>_________</td>
</tr>
<tr class="odd">
<td><ol start="7" type="A">
<li><p>Review the Parameter settings and verify that all task jobs have been queued properly. This is described in the Workstation Queued Tasks section of this documentation.</p></li>
</ol></td>
<td>Workstation</td>
<td>_________</td>
</tr>
<tr class="even">
<td><ol start="8" type="A">
<li><p>Initialize the workstation using Default or Divisional Workstation initialize option.</p></li>
</ol></td>
<td>VistA</td>
<td>_________</td>
</tr>
</tbody>
</table>

# Contingency PC Workstation Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## List/Display Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCBU <u>List/Display Orders</u> report will add Remove Times to Admin Times and will display both “Given” data and “Removed” data for medications requiring removal.

![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/005.png)

Select BCMA Backup System (Wrkstn) Option: SO\<ENTER\> List/Display Orders

BCMAbu Patient List (All) Mar 29, 2005@07:38:33 Page: 1 of 1

BCMA Backup System :: Patient Listing

Patient SSN Ward Room Bed

BCMAPATIENT1,ONE 000000001 4 MED M20 A

BCMAPATIENT2,TWO 000000002 3W GS NW304 2

Enter ?? for more actions

SP Select Patient LW List by Ward LA List All Patients

Select Item(s): Quit// SP \<ENTER\> Select Patient

Select PATIENT: BCMAPATIENT1,ONE \<ENTER\>

BCMAbu ACTIVE Orders List Mar 29, 2005@07:39 Page: 1 of 1

BCMAPATIENT1,ONE SSN: 000000001 Ward: 4 MED

This record last updated: Mar 29, 2005@07:29:43 Room: M20 Bed: A

Allergies: DYE,CATHETER; DILTIAZEM; SULFA; IBUPROFEN

-----------------------------------------------------------------------------

Order No. Status Type Medication(s)

16U Active UD SULFADIAZINE 500MG TAB (500MG ORAL QD)

Enter ?? for more actions

SO Select Order L1 List Active Orders L2 List All Orders

Select Action: Quit// SO \<ENTER\> Select Order

Select order number, more than one separated by a comma, or 'ALL':

Select ORDER#: ALL// 16U \<ENTER\>

BCMAbu Selected Order(s) Mar 29, 2005@07:39:36 Page: 1 of 1

BCMAPATIENT1,ONE SSN: 000000001 Ward: 4 MED

This record last updated: Mar 29, 2005@07:29:43 Room: M20 Bed: A

Allergies: DYE,CATHETER; DILTIAZEM; SULFA; IBUPROFEN

-----------------------------------------------------------------------------

Order Number: 16U Start: Mar 29, 2005@07:29:53

Type: UNIT DOSE Stop: Apr 11, 2005@14:00

Status: finished/verified by pharmacist(active)

Drug: SULFADIAZINE 500MG TAB

Give: 500MG ORAL QD

Provider: BCMAPROVIDER,ONE RPh/Entry by: BCMAPHARMACIST,ONE

Admin. Times: 0900

-----------------------------------------------------------------------------

Enter ?? for more actions

Select Action:Quit// \<ENTER\> QUIT

BCMAbu Patient List (All) Mar 29, 2005@07:40:28 Page: 1 of 1

BCMA Backup System :: Patient Listing

Patient SSN Ward Room Bed

BCMAPATIENT1,ONE 000000001 4 MED M20 A

BCMAPATIENT2,TWO 000000002 3W GS NW304 2

Enter ?? for more actions

SP Select Patient LW List by Ward LA List All Patients

Select Item(s): Quit// LW \<ENTER\> List by Ward

Wards with BCMA Backup Data on this workstation:

3W GS

4 MED

4 MED-CO

Select WARD: 3W \<ENTER\>

BCMAbu Patient List (Ward) Mar 29, 2005@07:41:03 Page: 1 of 1

BCMA Backup System :: Patient Listing

Patient SSN Ward Room Bed

BCMAPATIENT2,TWO 000000002 3W GS NW304 2

Enter ?? for more actions

SP Select Patient LW List by Ward LA List All Patients

Select Item(s): Quit// SP \<ENTER\> Select Patient

Select PATIENT: BCMAPATIENT2,TWO \<ENTER\>

BCMAbu ACTIVE Orders List Mar 29, 2005@07:41:20 Page: 1 of 1

BCMAPATIENT2,TWO SSN: 000000002 Ward: 3W GS

This record last updated: Mar 29, 2005@07:32:52 Room: NW304 Bed: 2

-----------------------------------------------------------------------------

Order No. Status Type Medication(s)

30U Active UD EPOETIN ALFA,RECOMBINANT 4000 UNT/ML INJ (4000UNT/1ML

Enter ?? for more actions

SO Select Order L1 List Active Orders L2 List All Orders

Select Action: Quit// \<ENTER\> QUIT

## ## BCBU MAR (Medical Administration Record) Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCBU MAR (Medical Administration Record) report will add Remove Times to Admin Times and will display both “Given” data and “Removed” data for medications requiring removal. The “Order \#:” field containing the letter “U” that previously printed on the same line as “Type:” and which could be mistaken for unit dose information, has been removed from the report.

In addition, notifications will be displayed on the MAR informing the medical professional of drugs that are <span id="P42_Hazardous_Handle" class="anchor"></span>hazardous to handle and/or hazardous to dispose.

![](bcma-v-3-0-backup-system-bcbu-version-3-installation-guide-updated-psb-3-108/006.png)

The hard-coded list of injection sites that prints as a legend at the end of the BCBU MAR reports has been removed. This report legend does not correspond with the medications requiring removal dermal sites or injectable medication injection sites.

BCBU MAR Report Prior to Report Legend Removal   Location                                        AdminStart                     Stop                     Times  01/16  01/17  01/18  01/19  01/20  01/21  01/22-----------------------------------------------------------------------------------------------------------   INPATIENT                                      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|May 07, 2015@15:38        Jun 06, 2015@23:59      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|\<\<*SELENIUM SULFIDE 2.5% LOTION/SHAMPOO\>\>          \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|Give:SMALL AMOUNT TOPICAL ON CALL PRN           \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|    Provider: TEAGUE,LYN D                  \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|RPh/Entry* by:                                  \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|   Order \#: 147U         Type: UNIT DOSE      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|   Status: finished/verified by pharmacist(active)\|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|BCMA MEDICATION LOG HISTORY                      PRN Effectiveness:\_\_\_\_\_\_\_\_\_\_\_<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>No Medication Log entries are on file for this order.                  Special Instructions:Give to patient as requested.-----------------------------------------------------------------------------------------------------------\|            SIGNATURE/TITLE            \| INIT  \|INJ SITES (Right or Left)       VA FORM  10-2970\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\_\_\_\_\_\_\_\| 1. DELTOID           4. MED (ANTERIOR) THIGH  7. ABDOMEN\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\_\_\_\_\_\_\_\| 2. VENTRAL GLUTEAL   5. VASTUS LATERALIS      8. THIGH\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\_\_\_\_\_\_\_\| 3. GLUTEUS MEDIUS    6. UPPER ARM             9. BUTTOCK\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \|\_\_\_\_\_\_\_\|10. UPPER BACK      PRN: E=Effective  N=Not Effective

> BCBU MAR Report After Report Legend Removal

>    Location                                        Admin

> Start                     Stop                     Times  01/16  01/17  01/18  01/19  01/20  01/21  01/22

> -----------------------------------------------------------------------------------------------------------

>    INPATIENT                                      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|

> May 07, 2015@15:38        Jun 06, 2015@23:59      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|

> \<\<*SELENIUM SULFIDE 2.5% LOTION/SHAMPOO\>\>          \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|*

> *Give:SMALL AMOUNT TOPICAL ON CALL PRN           \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|*

> *    Provider: TEAGUE,LYN D                     \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|*

> *RPh/Entry* by:                                  \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|

>    Order \#: 147U         Type: UNIT DOSE      \|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|

>    Status: finished/verified by pharmacist(active)\|      \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\|

> BCMA MEDICATION LOG HISTORY                      PRN Effectiveness:\_\_\_\_\_\_\_\_\_\_\_<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

> No Medication Log entries are on file for this order.                  

> Special Instructions:

> Give to patient as requested.

> -----------------------------------------------------------------------------------------------------------

## Print MAR for All Wards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: PA Print MAR for All Wards

Inpatient Pharmacy Orders for all wards

Report \[A\]LL or \[C\]URRENT orders? CURRENT// \<ENTER\>

Include Patients Without Active Medications? YES// \<ENTER\>

<span id="p73_44" class="anchor"></span>Sort Patients by \[N\]ame or \[R\]oom/Bed? Room/bed// \<ENTER\>

Print how many days MAR? 7// \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

DEVICE: HOME// DEC Windows \<ENTER\>

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT1,TEST SSN: 000000001 DOB: Sep 17, 1950 Sex: M

Ward: C MEDICINE Room: 320 Bed: 1

This record last updated: Mar 02, 2012@10:08:57

No allergies reported to the Contingency

No Active Medication Orders were reported to the Contingency at the time the MAR was printed

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT2,TEST SSN: 000000002 DOB: Jan 01, 1920 Sex: M

Ward: C MEDICINE Room: 320 Bed: 2

This record last updated: Jan 22, 2013@15:35:08

No allergies reported to the Contingency

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Jan 22, 2013@15:34 Feb 21, 2013@18:00 \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<BUSULFAN TAB\>\>

\<\<HAZ HANDLE\>\> \<\<HAZ DISPOSE\>

Give: 2MG ORAL (BY MOUTH)

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,ONE

Order \#: 3U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

-----------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

---------------------------------------------------------------------------------------------------------------------------------

INPATIENT \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Jan 27, 2013@09:00 Jan 29, 201@24:00 \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

\<\<NICOTINE 11MG/24HRS PATCH\>\> \| Remove \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Give: ONE PATCH TRANSDERMAL Q12H \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Provider: BCMAPROVIDER, ONE \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

RPh/Entry by: BCMAPHARMACIST, ONE

Order \#: 14U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

Log Date Message Log Entry Person

07/27/16@21:03 GIVEN BCMANURSE,ONE

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT3,TEST SSN: 000000003 DOB: Jan 01, 1930 Sex: F

Ward: C MEDICINE Room: 321 Bed: 1

This record last updated: Jan 18, 2013@11:54:28

No allergies reported to the Contingency

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Jan 18, 2013@11:51 Feb 17, 2013@18:00 \| 0600 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ALLOPURINOL 50MG (1/2 X 100MG) TAB\>\> \| 1200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 150mg ORAL (BY MOUTH) Q6H \| 1800 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER, ONE \| 2400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST, ONE

Order \#: 17U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

-----------------------------------------------------------------------------------------------------------------------------

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT4,TEST SSN: 000000004 DOB: Apr 23, 1966 Sex: M

Ward: C MEDICINE Room: 321 Bed: 2

This record last updated: Oct 23, 2012@13:34:56

Allergies: HALOTHANE; MALT BARLEY; PALMOLIVE SOAP; WATERMELONS; KELP; OLEPTRO; SARDINES;

MALTOSE; NICOTINAMIDE HYDRIODIDE/P; POLLEN; NAMENDA TITRATION PAK;

PINE NEEDLES; PINE PRODUCTS; IBUPROFEN/PSEUDOEPHEDRINE; TALBUTAL;

FARBITAL(NEW FORMULA); CARBONATED BEVERAGES; METHYLCELLULOSE;

CADEXOMER IODINE; ALUMINUM ACETATE/BENZETHO; HALAZEPAM;

\*\*ADR\*\* ALUMINUM HYDROXIDE/ASPIRI

No Active Medication Orders were reported to the Contingency at the time the MAR was printed

## Print MAR for Selected Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: PP Print MAR for Selected Patient

Inpatient Pharmacy Orders for a selected patient

Select PATIENT NAME: TESTPATIENT,ANOTHER \<ENTER\>

Report \[A\]LL or \[C\]URRENT orders? CURRENT// \<ENTER\>

Print how many days MAR? 7// \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

DEVICE: HOME// DEC Windows \<ENTER\>

MAR Ran: Jan 28, 2013@09:25:40 Inpatient Pharmacy Orders (Backup) Page: 1

TESTPATIENT,ANOTHER SSN: 000000006 DOB: May 04, 1960 Sex: M

Ward: C MEDICINE Room: 100 Bed: A

This record last updated: Jul 30, 2012@13:47:23

No allergies reported to the Contingency

No Active Medication Orders were reported to the Contingency at the time the MAR was printed

Select BCMA Backup System (Wrkstn) \<TEST ACCOUNT\> Option: PP Print MAR for Selected Patient

Inpatient Pharmacy Orders for a selected patient

Select PATIENT NAME: TESTPATIENT,ANOTHER\<ENTER\>

Report \[A\]LL or \[C\]URRENT orders? CURRENT// ALL\<ENTER\>

Print how many days MAR? 7// \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

DEVICE: HOME// DEC Windows\<ENTER\>

MAR Ran: Jan 28, 2013@09:31:05 Inpatient Pharmacy Orders (Backup) Page: 1

TESTPATIENT,ANOTHER SSN: 000000006 DOB: Apr 04, 1960 Sex: M

Ward: Room: 100 Bed: A

This record last updated: Oct 23, 2012@13:34:57

No allergies reported to the Contingency

<span id="p73_45" class="anchor"></span> Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Not on file Not on file \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

\<\<ALDESLEUKIN 22 MU/VIAL INJ\>\> \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Give: 22MILLION UNIT/1VIL IV PIGGYBACK Q5H \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Provider: BCMAPROVIDER, ONE \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

RPh/Entry by: BCMAPHARMACIST, ONE \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Order \#: 257468P Type: PENDING \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

Status: pending \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

BCMA MEDICATION LOG HISTORY \| \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

No Medication Log entries are on file for this order.

CAUTION! THIS IS A PENDING ORDER :: CHECK WITH PROVIDER OR PHARMACIST!

-----------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Jul 17, 2012@10:40 Jul 17, 2012@15:00 \| 1200 \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

\<\<FLUOROURACIL\>\> \| 1500 \|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|\*\*\*\*\*\*\|

\<\<HAZ Handle\>\> \<\<HAZ Dispose\>\>

Additive(s): \<\<FLUOROURACIL BOTTLE: A 10MG\>\>

Solution(s): \<\<DEXTROSE 50% INJ 1000ML\>\>

Give: IV PIGGYBACK BID S INFUSE OVER 60 Minutes

Provider: BCMAPROVIDER, ONE

RPh/Entry by: BCMAPHARMACIST, ONE

Order \#: 1V Type: IV

Status: expired

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

Special Instructions:

TEST

-----------------------------------------------------------------------------------------------------------------------------

## Print MAR for Selected Ward

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: PW Print MAR for Selected Ward

Inpatient Pharmacy Orders for a selected ward

Select WARD: C MED C MEDICINE

Report \[A\]LL or \[C\]URRENT orders? CURRENT// \<ENTER\>

Include Patients Without Active Medications? YES// \<ENTER\>

Sort Patients by \[N\]ame or \[R\]oom/Bed? Room/bed// Name\<ENTER\>

Print how many days MAR? 7// \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

DEVICE: HOME// DEC Windows \<ENTER\>

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT1,TEST SSN: 000000001 DOB: Sep 17, 1950 Sex: M

Ward: C MEDICINE Room: 320 Bed: 1

This record last updated: Mar 02, 2012@10:08:57

No allergies reported to the Contingency

No Active Medication Orders were reported to the Contingency at the time the MAR was printed

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT2,TEST SSN: 000000002 DOB: Jan 01, 1920 Sex: M

Ward: C MEDICINE Room: 320 Bed: 2

This record last updated: Jan 22, 2013@15:35:08

No allergies reported to the Contingency

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Jan 22, 2013@15:34 Feb 21, 2013@18:00 \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ASPIRIN 325MG BUFFERED TAB\>\>

Give: 325MG ORAL (BY MOUTH) QD-(EVERY DAY)%0900

Provider: BCMAPROVIDER, ONE

RPh/Entry by: BCMAPHARMACIST, ONE

Order \#: 3U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

-----------------------------------------------------------------------------------------------------------------------------

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT3,TEST SSN: 000000003 DOB: Jan 01, 1930 Sex: F

Ward: C MEDICINE Room: 321 Bed: 1

This record last updated: Jan 18, 2013@11:54:28

No allergies reported to the Contingency

Location Admin

Start Stop Times 01/28 01/29 01/30 01/31 02/01 02/02 02/03

-----------------------------------------------------------------------------------------------------------------------------

INPATIENT

Jan 18, 2013@11:51 Feb 17, 2013@18:00 \| 0600 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ALLOPURINOL 50MG (1/2 X 100MG) TAB\>\> \| 1200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 150mg ORAL (BY MOUTH) Q6H \| 1800 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER, ONE \| 2400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST, ONE

Order \#: 17U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

-----------------------------------------------------------------------------------------------------------------------------

MAR Ran: Jan 28, 2013@09:10:52 Inpatient Pharmacy Orders (Backup) Page: 1

PATIENT4,TEST SSN: 000000004 DOB: Apr 23, 1966 Sex: M

Ward: C MEDICINE Room: 321 Bed: 2

This record last updated: Oct 23, 2012@13:34:56

Allergies: HALOTHANE; MALT BARLEY; PALMOLIVE SOAP; WATERMELONS; KELP; OLEPTRO; SARDINES;

MALTOSE; NICOTINAMIDE HYDRIODIDE/P; POLLEN; NAMENDA TITRATION PAK;

PINE NEEDLES; PINE PRODUCTS; IBUPROFEN/PSEUDOEPHEDRINE; TALBUTAL;

FARBITAL(NEW FORMULA); CARBONATED BEVERAGES; METHYLCELLULOSE;

CADEXOMER IODINE; ALUMINUM ACETATE/BENZETHO; HALAZEPAM;

\*\*ADR\*\* ALUMINUM HYDROXIDE/ASPIRI

No Active Medication Orders were reported to the Contingency at the time the MAR was printed

## Print MAR for All Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: PAC \<ENTER\> Print MAR for All Clinics

Report \[A\]LL or \[C\]URRENT orders? CURRENT// \<ENTER\>

Include a Patient's Inpatient Medications on the Clinic report? YES// \<ENTER\>

Print how many days MAR? 7// \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

MAR Ran: Mar 05, 2013@11:11:05 Inpatient Pharmacy Orders (Backup) Page: 1

BCMACO,ELEVEN SSN: 666001111 DOB: Mar 10, 1900 Sex: M

Ward: Room: Bed:

This record last updated: Mar 01, 2013@00:16:06

Allergies: LATEX STRAP

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

INPATIENT \| 0100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Feb 25, 2013@19:26 Mar 17, 2013@24:00

\<\<BACLOFEN 10MG TABS\>\>

Give: 10 MG ORAL (BY MOUTH) BID-AM

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 13U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-CLINIC MED SOUTH \| 0100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Mar 01, 2013@00:16 Mar 21, 2013@23:00 \| 0500 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ACETAMINOPHEN 325MG C.T.\>\> \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 325 MG ORAL (BY MOUTH) Q4H \| 1300 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,ONE \| 1700 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST,TWO \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Order \#: 48U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

Special Instructions:

Test special instructions to show that they can extend out 80 characters before

Wrapping to next line. Print as was typed and saved by Pharmacy.

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-CLINIC MED SOUTH \| 0100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Feb 25, 2013@14:23 May 07, 2013@24:00 \| 0500 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ASPIRIN BUFFERED 325MG TAB\>\> \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 325MG ORAL (BY MOUTH) Q4H \| 1300 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,ONE \| 1700 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST,TWO \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Order \#: 11U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-CLINIC MED SOUTH \| 0100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Feb 25, 2013@14:26 May 07, 2013@24:00

\<\<OXYTOCIN 10 UNIT INJ\>\>

\<\<HAZ Handle\>\>

Give: 10 UNIT INJ TID

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 13U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

MAR Ran: Mar 05, 2013@11:11:05 Inpatient Pharmacy Orders (Backup) Page: 2

BCMACO,SEVEN SSN: 666007777 DOB: Sep 22, 1900 Sex: M

Ward: 7A GEN MED Room: "" Bed: ""

This record last updated: Feb 22, 2013@11:34:47

Allergies: LATEX STRAP

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-CLINIC MED SOUTH \| 0400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Feb 20, 2013@09:11 Mar 31, 2013@24:00 \| 0600 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<ACETAMINOPHEN 325MG C.T.\>\> \| 0800 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 325 MG ORAL (BY MOUTH) Q2H \| 1000 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,ONE \| 1200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST,TWO \| 1400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Order \#: 14U Type: UNIT DOSE \| 1600 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Status: finished/verified by pharmacist(active) \| 1800 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

BCMA MEDICATION LOG HISTORY \| 2000 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

No Medication Log entries are on file for this order. \| 2200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\| 2400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

---------------------------------------------------------------------------------------------------------------------------------

MAR Ran: Mar 05, 2013@11:11:05 Inpatient Pharmacy Orders (Backup) Page: 1

BCMACO,TWELVE SSN: 666001212 DOB: Apr 16, 1900 Sex: F

Ward: Room: Bed:

This record last updated: Mar 01, 2013@18:02:35

Allergies: LATEX STRAP

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-DERM \| 0200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Mar 01, 2013@18:00 Mar 15, 2013@24:00 \| 0700 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<UREA WITH HC 1% CREAM 30GM\>\> \| 1200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: SMALL AMOUNT TOPICAL 5XD \| 1700 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,TWO \| 2200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST,ONE

Order \#: 3U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

Log Date Message Log Entry Person

03/01/13@18:02 GIVEN BCMAPHARMACIST,ONE

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 03/08 03/09 03/10 03/11

---------------------------------------------------------------------------------------------------------------------------------

AL-DERM \| 0200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Mar 01, 2013@22:00 Mar 15, 2013@24:00 \| 0600 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<HYDROXYZINE 10MG TAB\>\> \| 1000 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 20 MG ORAL (BY MOUTH) Q4HPRN \| 1400 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,TWO \| 1800 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPHARMACIST,ONE \| 2200 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Order \#: 4U Type: UNIT DOSE PRN Effectiveness:\_\_\_\_\_\_\_\_\_\_\_\_\_

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

## ## Print MAR for Selected Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: PC \<ENTER\> Print MAR for Selected Clinic

Inpatient Pharmacy Orders for a selected Clinic

Select CLINIC: SY-CLINIC \<ENTER\> SY-CLINIC NORTH

Report \[A\]LL or \[C\]URRENT orders? CURRENT// \<ENTER\>

Include a Patient's Inpatient Medications on the Clinic report? YES// NO \<ENTER\>

Print how many days MAR? 7// 3 \<ENTER\>

Select how many BCMA Medication Log history: 1// \<ENTER\>

MAR Ran: Mar 05, 2013@09:00:29 Inpatient Pharmacy Orders (Backup) Page: 1

BCMACO,ELEVEN SSN: 666001111 DOB: Mar 10, 1900 Sex: M

Ward: Room: Bed:

This record last updated: Mar 01, 2013@00:16:06

Allergies: LATEX STRAP

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Feb 27, 2013@10:02 Mar 09, 2013@24:00 \| 0500 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<THIORIDAZINE 30MG/ML CONC.\>\> \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 10 MG ORAL (BY MOUTH) Q4H \| 1300 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,TWO \| 1700 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

RPh/Entry by: BCMAPROVIDER,ONE \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Order \#: 47U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

Special Instructions:

tst

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Jan 03, 2013@10:06 Jun 30, 2013@11:11 \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<CHLORAL HYDRATE 500MG CAP\>\>

Give: 500 MG ORAL (BY MOUTH) Q12H

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 29U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Jan 03, 2013@10:05 Jun 30, 2013@11:11 \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\<\<LIDOCAINE JELLY 2% \>\>

Give: 1 DOSE TOPICAL Q12H

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 30U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

MAR Ran: Mar 05, 2013@09:00:29 Inpatient Pharmacy Orders (Backup) Page: 2

BCMACOIM,ELEVEN SSN: 000009011 DOB: Mar 10, 1900 Sex: M

Ward: 7A GEN MED Room: 726 Bed: B

This record last updated: Mar 01, 2013@16:41:56

Allergies: STRAWBERRIES

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0300 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Jan 03, 2013@10:06 Jun 24, 2013@12:00 \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<LORAZEPAM 1MG TAB\>\> \| 1500 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 2 MG ORAL (BY MOUTH) Q6H \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 23U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

Log Date Message Log Entry Person

02/07/13@15:26 GIVEN WILSON,REMELA

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0500 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Jan 03, 2013@10:07 Jun 24, 2013@12:00 \| 1300 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<METHADONE 10MG TAB \>\> \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Give: 20 MG ORAL (BY MOUTH) Q8H

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 24U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

Location Admin

Start Stop Times 03/05 03/06 03/07 Notes

---------------------------------------------------------------------------------------------------------------------------------

SY-CLINIC NORTH \| 0900 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

Jan 03, 2013@10:07 Jun 24, 2013@12:00 \| 2100 \|\_\_\_\_\_\_\|\_\_\_\_\_\_\|\_\_\_\_\_\_\|

\<\<METHOTREXATE 2.5MG TAB\>\>

Give: 2.5 MG ORAL (BY MOUTH) Q12H

Provider: BCMAPROVIDER,ONE

RPh/Entry by: BCMAPHARMACIST,TWO

Order \#: 25U Type: UNIT DOSE

Status: finished/verified by pharmacist(active)

BCMA MEDICATION LOG HISTORY

No Medication Log entries are on file for this order.

---------------------------------------------------------------------------------------------------------------------------------

## ## Print Blank MAR for Selected Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Blank 3 Day MAR for Selected Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: BL \<ENTER\> Print Blank Mar for Selected Patient

Inpatient Pharmacy Orders for a selected patient

Select PATIENT NAME: BCMAPATIENT1,ONE \<ENTER\>

Print how many days MAR? 7// 3 \<ENTER\>

DEVICE: BCBU// \<ENTER\>

MAR Ran: Mar 29, 2005@07:49:18 Inpatient Pharmacy Orders (Backup) Page: 1

BCMAPATIENT1,ONE SSN: 000000001 DOB: Jul 29, 1915 Sex: M

Ward: 4 MED Room: M20 Bed: A

This record last updated: Mar 29, 2005@07:29:43

Allergies: DYE,CATHETER; DILTIAZEM; SULFA; IBUPROFEN

Admin MAR

Order Start Stop Times 29 30 31 Notes

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

### Blank 7 Day MAR for Selected Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: BL \<ENTER\> Print Blank Mar for Selected Patient

Inpatient Pharmacy Orders for a selected patient

Select PATIENT NAME: BCMAPATIENT1,ONE \<ENTER\>

Print how many days MAR? 7// \<ENTER\>

DEVICE: BCBU// \<ENTER\>

MAR Ran: Mar 29, 2005@07:50:10 Inpatient Pharmacy Orders (Backup) Page: 1

BCMAPATIENT1,ONE SSN: 000000001 DOB: Jul 29, 1915 Sex: M

Ward: 4 MED Room: M20 Bed: A

This record last updated: Mar 29, 2005@07:29:43

Allergies: DYE,CATHETER; DILTIAZEM; SULFA; IBUPROFEN

Admin MAR APR

Order Start Stop Times 29 30 31 1 2 3 4 Notes

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

\| \|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|\_\_\_\_\_\|

RPH Verify:\_\_\_\_\_\_\_\_\_\_\_ Nurse Verify:\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------------------

## List of Wards in BCMA Backup File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select BCMA Backup System (Wrkstn) Option: WL \<ENTER\> List of Wards in BCMA Backup File

Wards with BCMA Backup Data on this workstation:

10W

2B APCU

3E GEM

3E SUBACUTE

3W GS

3W ORTHO

4 MED

4 SURG

4E ENT

4E M

4E ON

MICU

TICU

# Trouble Shooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The messages are building on the VistA side, but I see an open fail in the link monitor.

Check the following areas:

- The IP address on both and make sure they match.
- The Port numbers on both and make sure they match.
- The Firewall on the workstation.
- The Filers on the workstation.
- The Link Manager on the workstation.

When logging into the Cache Terminal on the workstation I get a \<FILEFULL\> error.When looking at the HL7 System Link Monitor on VistAthe BCBU Workstation shows a READ ERROR state.

This may be caused by the BCBU workstation reaching its defined maximum allowed database size. To increase the size of the BCBU workstations database go into the Cache Cube / Control Panel / Local Databases. Right click on VISTA and select properties. If the database has reached the maximum defined the fields \# of MB and Max \# of MB will be equal. To increase the size edit only the Max \# of MB field. (Note: Make sure the physical hard drive has enough space available for the increase in the database size)

When logging into the Cache Terminal on the workstation I get a \<NOROUTINE\> error.

Verify that the two user accounts setup under the Cache Cube / Control Panel / Security / User Accounts are set to VISTA Namespace and ^ZU Routine.

The messages appear to be transmitting but no data is filing on the workstation.

Verify that the HL COMMUNICATION SERVER PARAMETERS field, "DEFAULT PROCESSING ID" is set correctly. This field must match the value of the sending VistA system. In addition, verify that INCOMING and OUTGOING HL7 filers are running on the workstation.

I don't see the message queue increase for my HL7 link when I run the 'Initialize Workstation" option or during activity on the VistA side?

The following two places need to be checked:

Make sure the Link is enabled on the VistA side. *HL7 Main Menu* \[HL MAIN MENU\] option.

Make sure the Workstation Link is associated to the correct division or Default parameter.  
\[PSB BCBU LINK ASSOCIATIONS\] option.

I'm able to start TaskMan up with the Taskman_start script, but I notice that the HL7 link jobs do not start. What could be the problem?

Linux requires root privs to start listener jobs on TCPIP ports. TaskMan needs to be started by the root user so its submanagers (which start the listener) can have those privs as well. To do this, login as the BCMA Manager the issue the command "su –m" and enter the root password. Once you're logged in as root, start TaskMan by issuing the command "./taskman_start". The HL7 link manager and the listener link should start automatically. Note: Netmail startup has root requirements as well.

Running the netmail_start script does not start netmail. What could be the problem?

Linux requires root privs to start listener jobs on TCPIP ports. To start up the network mail listener job, log in as the BCMA Manager, then issue the command "su –m" and enter the root password. Once you're logged in as root, start network mail by issuing the command "./netmail_start". Note: HL7 links have root requirements as well.

How can I verify the TCPIP listening jobs on Linux?

As root, issue the "netstat –tlp" command. This will provide information similar to the following:

Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name

tcp 0 0 \*:32768 \*:\* LISTEN 523/rpc.statd

tcp 0 0 BCMA.med.va.gov:32769 \*:\* LISTEN 628/xinetd

tcp 0 0 \*:printer \*:\* LISTEN 658/lpd Waiting

tcp 0 0 \*:sunrpc \*:\* LISTEN 504/portmap

tcp 0 0 \*:10000 \*:\* LISTEN 1174/mumps

tcp 0 0 \*:5904 \*:\* LISTEN 13884/Xvnc

tcp 0 0 \*:x11 \*:\* LISTEN 813/X

tcp 0 0 \*:ftp \*:\* LISTEN 628/xinetd

tcp 0 0 \*:ssh \*:\* LISTEN 614/sshd

tcp 0 0 \*:telnet \*:\* LISTEN 628/xinetd

tcp 0 0 \*:smtp \*:\* LISTEN 1390/mumps

Ports of primary interest are 10000 (HL7 listener link) and SMTP (port 25-netmail).

To see the numeric ports for common TCPIP protocols, issue the "netstat –tlp – numeric" command.

What is the best way to shut GT.M down?

\$HOME of the BCMA manager account contains the script zgstop. This script is customized to shut down the BCMA configuration cleanly and run the GT.M database down (to ensure database integrity). To use this script properly, it must be run as root (the BCMA manager will not be able to shutdown HL7 link, netmail, and TaskMan jobs started as root - this will prevent the database to rundown properly). To do this, login as the BCMA manager then issue the command "su -m" and enter the root password. Once you're logged in as root, issue the command './zgstop'.

How do I start GT.M up?

There is no single GT.M daemon. This means that each GT.M process 'starts' GT.M for itself. GT.M processes (TaskMan, netmail, HL7 jobs) should start automatically with a system reboot provided the /etc/init.d/gtm script was enabled when BCMA was installed using the install_bcma script.

From within GT.M, how can I view system status (like when I D ^%SS in Cache)?

GT.M does not provide a utility of its own to provide this functionality. However, SD&D have provided the ^ZSY routine to accomplish this. As with other BCMA tasks, it is best to run this as the root user; otherwise, not all process information will be accessible. To do this, login as the BCMA manager, then issue the command "su -m" and enter the root password. Drop into GT.M, issue the ZSY command as follows, and select the type of display desired.

GTM\>D ^ZSY

1 pid

2 cpu time

3 image/pid

4 image/cpu

1// 1

INTRPT issued to process 1409

INTRPT issued to process 1148

INTRPT issued to process 1390

INTRPT issued to process 1315

INTRPT issued to process 1307

INTRPT issued to process 1295

INTRPT issued to process 1291

INTRPT issued to process 1239

INTRPT issued to process 1229

INTRPT issued to process 1225

INTRPT issued to process 1222

INTRPT issued to process 1216

INTRPT issued to process 1213

INTRPT issued to process 1189

INTRPT issued to process 1179

INTRPT issued to process 1177

INTRPT issued to process 1174

INTRPT issued to process 1157

INTRPT issued to process 1145

System Status for GT/M

GT.M Mumps users on 18-Mar-03 11:11:10

Proc. id Proc. name PS Terminal Routine Mode CPU time

-------- --------------- --- -------- -------- ------

1145 TaskMan VISTA 1 S ? IDLE+1^%ZTM -direct

1148 S pts/2 -direct

1157 HLmgr:538 S ? LOOP+3^HLCSLM -direct

1174 HLSrv:182 S ? -direct

1177 S ? SUB+1^%ZTMS1 -direct

1179 BTask 546 S ? STARTIN+17^HLCSIN -direct

1189 BTask 545 S ? STARTIN+17^HLCSIN -direct

1213 BTask 547 S ? STARTOUT+16^HLCSOUT-direct

1216 BTask 548 S ? STARTOUT+16^HLCSOUT-direct

1222 BTask 550 S ? STARTIN+17^HLCSIN -direct

1225 BTask 551 S ? STARTIN+17^HLCSIN -direct

1229 BTask 552 S ? STARTOUT+16^HLCSOUT-direct

1239 BTask 553 S ? STARTOUT+16^HLCSOUT-direct

1291 Sub 1291 S ? GETTASK+3^%ZTMS1 -direct

1295 Sub 1295 S ? SUB+1^%ZTMS1 -direct

1307 Sub 1307 S ? GETTASK+3^%ZTMS1 -direct

1315 Sub 1315 S ? SUB+1^%ZTMS1 -direct

1390 S ? -direct

1409 S pts/3 jobset+4^ZSY -direct

I'm getting \<RECOMPILE\> errors when working on the Caché system.

If you are getting this error, the routines need to be recompiled on the workstation. There are two different methods you can use to accomplish this:

CHUI

1.  Get to the programmer prompt on the workstation.
2.  D ^%RCOMPIL
3.  At the routine selection prompt, select %\*, press Enter.
4.  Repeat the D ^%RCOMPIL command and select \* at the routine selection prompt.

GUI

1.  Right-click on the Cache cube and select Explorer.
2.  On the left side of the screen expand VistA under the Local Databases, select routines.
3.  In the routine selection box, enter %\*
4.  From the Edit menu, click on Select All.
5.  In the Contents screen on the right, right-click, then click Advanced/Compile.
6.  Repeat steps 3-5, selecting \* in the routine selection.