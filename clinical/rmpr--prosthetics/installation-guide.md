---
title: Prosthetics Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"preface\\">Preface</h5></td> <td><blockquote> <p>This guide is for use by Information Resources Management Services and Information Systems Center personnel to install the DHCP Pro"
audience: 
keywords: 
  - table
  - style
  - width
  - colgroup
  - tbody
  - blockquote
  - prosthetics
  - class
  - module
  - installation
page_count: 0
word_count: 2757
section_count: 0
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr3ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr3ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

![](prosthetics-version-3-installation-guide/001.png)

PROSTHETICSINSTALLATION GUIDE

December 1995

V*IST*A System Design and Development

Prosthetics Installation Guide

Table of Contents

Prosthetics Installation Guide [3](#prosthetics-installation-guide)

Introduction [3](#introduction)

Installation Instructions [7](#installation-instructions)

Pre-Installation – Required Resources [8](#pre-installation-required-resources)

Prosthetics Installation [10](#prosthetics-installation)

Installation Over a Previous Release [12](#installation-over-a-previous-release)

#### ## Prosthetics Installation Guide

#### Introduction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="preface">Preface</h5></td>
<td><blockquote>
<p>This guide is for use by Information Resources Management Services and Information Systems Center personnel to install the DHCP Prosthetics package. Prosthetics automates the Record of Prosthetics Services (VA Form 10-2319) and purchasing functions within Prosthetics Service. Prosthetics also integrates individual purchasing transactions with IFCAP (Integrated Funds Distribution, Control Point Activity, Accounting and Procurement) and Generic Inventory.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="package-overview">Package Overview</h5></td>
<td><blockquote>
<p>The Decentralized Hospital Computer Program (DHCP) Prosthetics package automates many functions for Prosthetics. The Record of Prosthetics Service (VA Form (VAF) 10-2319), and the appropriate VAF 4-1358 obligation, are updated at the time of purchase (entry into the computer) of the item or service provided to the veteran. This update is accomplished through direct links to IFCAP and the Electronic Patient VAF 10-2319.</p>
<p>Purchasing is simplified by entering the information only once into the computer and letting it update your 1358 account balances and VAF 10-2319. The Prosthetics package automates the tracking of appliances and services issued, suspense records, correspondence to veterans and vendors, and scheduled meetings and home/liaison visits.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="purchasing-module">Purchasing Module</h5></td>
<td><blockquote>
<p>Purchasing interfaces with IFCAP into IFCAP 1358 module. Forms printed include Prosthetics Authorization and Invoice (VAF 10-2421), and Authority to Exceed Amount on Service Card (Form Letter (FL) 10-55).</p>
<p>For tracking transactions associated with purchasing, Prosthetics will accommodate Prosthetic Service Card Invoice (VAF 10-2520), No Form, Pickup/Delivery Charges, Request for Estimate (FL 10-55), and Patient Notification Letter.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="electronic-record-of-prosthetic-services-module">Electronic Record of Prosthetic Services Module</h5></td>
<td><blockquote>
<p>The Record of Prosthetic Services, VAF 10-2319, is fully incorporated into DHCP, displayed in multiple terminal screens. Appliances and services issued are automatically recorded to the electronic VAF 10-2319 when purchases are obligated or issued from stock. In addition, Prosthetic Service Card (PSC), Clothing Allowance, Auto-Adaptive Equipment, Patient Correspondence, and other patient data, are recorded and displayed within the electronic VAF 10-2319 module.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="inventory-module">Inventory Module</h5></td>
<td><blockquote>
<p>The Inventory module helps you track quantities of items in the Prosthetics Sensory and Aids Service (PSAS) inventory by automating the creation of VA Form 10-1210 Issue and Stock Control Record - Prosthetics Stock Items. It provides the means to:</p>
</blockquote>
<ul>
<li><p>Manage the inventory data</p></li>
<li><p>Track lab employee time and salary for dispensing stock</p></li>
<li><p>Send a mail message when stock is low</p></li>
<li><p>Automatically calculate stock quantities when stock is ordered or issued.</p></li>
</ul>
<blockquote>
<p>A release of Prosthetics includes four new Inventory Reports. These usage reports are available for the sites and also for PSAS Headquarters personnel. Each report shows stock usage and is sorted first by site and then by a date range. Values for used and new inventory are shown on these reports.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="correspon-dence-module">Correspon-dence Module</h5></td>
<td><blockquote>
<p>Letters to patients are generated from this module.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scheduled-meetings-and-homeliaison-visits-module">Scheduled Meetings and Home/Liaison Visits Module</h5></td>
<td><blockquote>
<p>Appointment information for Prosthetics Clinics may be pulled over into VAF 10-2527 to be printed as Appointment Roster and Action Sheets. Home/liaison visits may also be entered and printed in this module.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="nppd-module">NPPD Module</h5></td>
<td><blockquote>
<p>The NPPD (National Prosthetics Patient Database) module is used to routinely view, analyze, and validate the medical center PSAS (Prosthetic Sensory Aids Service) patient transaction data and resides at the medical center level. The mission of this module is to provide a clinical review, to increase quality, reduce costs, and improve efficiencies of the Prosthetics program.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="prosthetic-lab-module">Prosthetic Lab Module</h5></td>
<td><blockquote>
<p>The Prosthetic Lab module automates the Request and Receipt for Prosthetic Appliances or Services (VAF 10-2529-3) which is used to maintain a consolidated record of prosthetic services furnished to eligible veterans. This includes activities at the following:</p>
</blockquote>
<ul>
<li><p>Orthotic Laboratories</p></li>
<li><p>Restoration Laboratories</p></li>
<li><p>Shoe Last Clinics</p></li>
<li><p>Wheelchair Repair Shops</p></li>
<li><p>National Foot Centers</p></li>
<li><p>Denver Distribution Center.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="entitlement-module">Entitlement Module</h5></td>
<td><blockquote>
<p>Information collected by Medical Administration Service (MAS) to determine eligibility of benefits to the veteran is displayed in this module. Patient data includes the following:</p>
</blockquote>
<ul>
<li><p>Name</p></li>
<li><p>Social security number</p></li>
<li><p>Date of birth</p></li>
<li><p>Address</p></li>
<li><p>Remarks</p></li>
<li><p>Temporary address</p></li>
<li><p>Phone</p></li>
<li><p>Sex</p></li>
<li><p>Next of kin</p></li>
<li><p>Military service</p></li>
<li><p>Eligibility status</p></li>
<li><p>Verification of eligibility</p></li>
<li><p>Disability ratings</p></li>
<li><p>Diagnostic codes</p></li>
<li><p>Admission date</p></li>
<li><p>Discharge date</p></li>
<li><p>Type of discharge</p></li>
<li><p>Clinic enrollment</p></li>
<li><p>Pending appointments.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="suspense-module">Suspense Module</h5></td>
<td><blockquote>
<p>The Suspense module tracks patient requests for prosthetic appliances or services. The user can add new suspense records, close, edit, inquire, and print suspense records. This module provides a method for any Prosthetics service request or items request to be made either manually through the Prosthetics system or electronically through CPRS (Computerized Patient Record System).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="administrative-home-oxygen-module">Administrative Home Oxygen Module</h5></td>
<td><blockquote>
<p>The Administrative Home Oxygen module is used to manage billing from the vendor, providing several benefits, including saving money by suspending erroneous charges and saving time through the elimination of a manual review of the records.</p>
<p>The Home Oxygen module provides for the recording of patient information for reporting and invoice billing which can be used as a check against bills received from the contractor for each patient. The module facilitates the coordination of services when contractors change at the end of a contract cycle.</p>
<p>It also provides correspondence support to remind patients when they need to renew their Home Oxygen prescriptions and flags patients with special problems.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Installation Instructions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="the-process">The process</h5></td>
<td><blockquote>
<p>The installation instructions include a detailed description of pre-installation, installation and post-installation instructions. Examples of the installation process over a previous release or into a virgin account are included.</p>
<p>An Installation Checklist has been provided to aid in installing Prosthetics. It is recommended that you install Prosthetics in a test account prior to installing it in a production account, and for reference purposes, you may want to slave print the initialization process.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="ifcap-options">IFCAP options</h5></td>
<td><blockquote>
<p>Two IFCAP options are used by Prosthetics. They are <strong>Item File Edit</strong> (PRCHPC ITEM EDIT) and <strong>Vendor File Edit</strong> (PRCHPC VEN EDIT). These two options are under the <strong>IFCAP Utilities menu</strong> (RMPR VEN/ITEM) which is locked with the RMPRSUPERVISOR key.</p>
<p>One security key from the IFCAP package is used with Prosthetics. The PRCHZ REV is a reverse lock for the <strong>Item File Edit</strong> option (PRCHPC ITEM EDIT).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="note">Note</h5></td>
<td><blockquote>
<p>File 663 – All AMIS calculations are accomplished according to codes stored in the file. DO NOT add, edit or delete data stored in this file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Pre-Installation – Required Resources

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="software">1. Software</h5></td>
<td><blockquote>
<p>The minimal hardware requirements for Prosthetics are three CRTs to one printer. The alpha and beta sites (Phoenix and Atlanta) compiled the following statistics regarding the disk storage requirements for Prosthetics after running the software for about one year.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Globals</td>
<td>Data Type</td>
<td>Size</td>
</tr>
<tr class="even">
<td>RMPR</td>
<td>Prosthetic data</td>
<td><p>10,000 VMS blocks</p>
<p>5,000 DSM blocks</p></td>
</tr>
<tr class="odd">
<td>RMPRA</td>
<td>Temporary global</td>
<td></td>
</tr>
<tr class="even">
<td>DDs</td>
<td></td>
<td><p>90 VMS blocks</p>
<p>45 DSM blocks</p></td>
</tr>
<tr class="odd">
<td>Routines 120 (not including inits and onits)</td>
<td></td>
<td><p>478 VMS blocks</p>
<p>238 DMS blocks</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="global-description-and-placement">2. Global Description and Placement</h5></td>
<td><blockquote>
<p>Two globals are created when Prosthetics is installed into a virgin account. The first global, ^RMPR, is the main global. All routines, options and templates are namespaced RMPR.</p>
<p>The second global, ^RMPRA, is a storage global for AMIS data. The data in this global is updated each time AMIS worksheets are run. If you are installing Prosthetics into a virgin account, place and define access privileges (RWD for System, World, Group, and UCI) for ^RMPR and ^RMPRA using ^%GLOMAN (DSM) or ^%GCH (MSM).</p>
<p>Journaling is recommended for the ^RMPR global.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="required-packages">3. Required Packages</h5></td>
<td><blockquote>
<p><strong><u>Application</u> <u>Minimum Version Number</u></strong></p>
<p>FileMan 21</p>
<p>IFCAP 5.0</p>
<p>Kernel 8.0</p>
<p>PIMS 5.3</p>
<p>Integrated Billing 2.0</p>
<p>OE/RR 2.5</p>
<p>Generic Code Sheet 2.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="hardware">4. Hardware</h5></td>
<td><blockquote>
<p>Disk space (expected growth) = 3 MB per 20,000 patient visits.</p>
<p>Number of CRTs = number of Prosthetics Service FTEEs (Full-Time Employment Equivalent) that utilize the package.</p>
<p>Number of Printers (PRTs) depends on the CRT ratio below:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|         |         |
|---------|---------|
| \# CRTs | \# PRTs |
| 1-4     | 1       |
| 5-6     | 2       |
| 7-8     | 3       |
| 9-10    | 4       |
| 11-12   | 5       |
| 13-14   | 6       |
| 15      | 7       |

#### Prosthetics Installation

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="stepactions">Step/Actions</h5></td>
<td><blockquote>
<p>Below are the steps for a Prosthetics installation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>1</td>
<td>Get Prosthetic Users off the system(s).</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Backup system(s).</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Load RMPR* and RMPT* routines. Have a slaved printer copy a listing of the exported routines.</p>
<p>&gt;D^%RR</p>
<p><strong>NOTE:</strong> Do NOT Delete RMPR* routines prior to loading RMPR*</p></td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>Define Programmer Variables.</p>
<p>D^XUP to define DUZ, DT, DTIME and U</p>
<p>S DUZ(0)=”@”</p>
<p>RMPT* routines.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Run RMPRNTEG to a printer. Make sure the exported routines have correct checkfile sums.</td>
</tr>
<tr class="odd">
<td>6</td>
<td><p>Initialize Prosthetics.</p>
<p>Accept all default prompts (see examples with previous version installed, or installation into a virgin account). For a virgin install, the RMPRTINITs will be run first, then the RMPRINITs. If installing over a previous version of Prosthetics, the RMPRINITs must be run first, then the RMPTINITs.</p></td>
</tr>
<tr class="even">
<td>7</td>
<td><p>Pre-Inits</p>
<p>The RMPRPRE checks the system to insure that the software applications required for Prosthetics have been installed.</p></td>
</tr>
<tr class="odd">
<td>8</td>
<td><strong>NOTE:</strong> When running the inits, be sure to run RMPRINIT <u>prior</u> to running RMPTINIT if installing over a previous version of Prosthetics.</td>
</tr>
<tr class="even">
<td>9</td>
<td>Make sure the RMPRINITs and RMPTINITs completed correctly, and in the correct order. If one of the inits fails to complete, determine why, and rerun the init before continuing.</td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="stepactions-1">Step/Actions</h5>
<p>(continued)</p></td>
<td><blockquote>
<p>Below are the steps for a Prosthetics installation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>Post-init</p>
<p>If this is a Virgin Install, this step will not apply, as you will not have a prior Loan Program to be concerned with. This information is solely for those sites installing this Prosthetics Package over a previous version of the Prosthetics Package.</p>
<p>LOAN^RMPRPOST removes the Loan Program. If your site has made a local decision to use the Loan Program option, then do not run this routine. The Prosthetic Expert Panel is not recommending the support of the Loan Program.</p>
<p>LOAN^RMPRPOST will delete the following options: RMPR LOAN DEL, RMPR LOAN CREATE, RMPR LOAN RET, RMPR LOAN DISP, RMPR LOAN FOLLOW-UP, RMPR LOAN PRINT ALL, RMPR LOAN EDIT, RMPR LOAN STAT, and RMPR LOAN MENU.</p>
<p><strong>NOTE:</strong> Do NOT delete this routine once the Loan Program has been deleted. It does more than delete the Loan Program.</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Delete RMPRI* and RMPTI* routines, if desired.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Move RMPR* routines to all systems.</td>
</tr>
</tbody>
</table>

#### Installation Over a Previous Release

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="example">Example</h5></td>
<td><blockquote>
<p>The following is an example of the installation of Prosthetics Version 3.0 with Version 2.0 installed.</p>
<p><strong>NOTE:</strong> Make sure you D ^RMPRINIT before you D ^RMPTINIT.</p>
</blockquote></td>
</tr>
</tbody>
</table>