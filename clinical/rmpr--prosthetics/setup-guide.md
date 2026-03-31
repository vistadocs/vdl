---
title: Prosthetics Version 3 Security Guide
doc_type: SG
doc_label: Security Guide
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
menu_options: 7
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"overview\\">Overview</h5></td> <td><blockquote> <p>The Decentralized Hospital Computer Program (DHCP) Prosthetics package automates many functions for Prosthetics. The Record of Pr"
audience: 
keywords: 
  - blockquote
  - table
  - colgroup
  - style
  - width
  - tbody
  - prosthetics
  - module
  - rmpr
  - access
page_count: 0
word_count: 2508
section_count: 2
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmprsg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmprsg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [Prosthetics Security System](#prosthetics-security-system)
![](prosthetics-version-3-security-guide/001.png)
PROSTHETICSSECURITY GUIDE*Sensitive Information*
December 1995
V*IST*A Health System Design and Development (HSD&D)
Prosthetics Security Guide
Table of Contents
Prosthetics Security Guide [3](#prosthetics-security-guide)
Introduction [3](#introduction)
Prosthetic Security [7](#prosthetic-security)
Prosthetics Security System [9](#prosthetics-security-system)
VA FileMan Accessible Files [9](#va-fileman-accessible-files)
VA FileMan Access Codes [12](#va-fileman-access-codes)

#### ## Prosthetics Security Guide

#### Introduction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="overview">Overview</h5></td>
<td><blockquote>
<p>The Decentralized Hospital Computer Program (DHCP) Prosthetics package automates many functions for Prosthetics. The Record of Prosthetics Service (VA Form (VAF) 10-2319), and the appropriate VAF 4-1358 obligation, are updated at the time of purchase (entry into the computer) of the item or service provided to the veteran. This update is accomplished through direct links to IFCAP (Integrated Funds Distribution, Control Point Activity, Accounting and Procurement) and the Electronic Patient VAF 10-2319.</p>
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

#### Prosthetic Security

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rmpr-official-and-rmpr-clerk-menus">RMPR OFFICIAL and RMPR CLERK Menus</h5></td>
<td><blockquote>
<p>Prosthetic deals extensively with patient records information and accounting data. Normal security measures at your facility apply.</p>
<p>The Chief, Prosthetics Service should be assigned the RMPR OFFICIAL menu along with all the RMPR security keys that are discussed in greater detail below.</p>
<p>Other employees may also be assigned the RMPR OFFICIAL or RMPR CLERK menus, and the appropriate keys for the required level of access according to their job assignment.</p>
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
<td><h5 id="security-keys">5 Security Keys</h5></td>
<td><blockquote>
<p>Five security keys are exported with Prosthetics. The keys and what options or actions they control are as follows:</p>
<p><strong>1. RMPRSUPERVISOR:</strong></p>
</blockquote>
<ul>
<li><p>Close Out [RMPR CLOSE-OUT]</p></li>
<li><p>Enter/Edit Prosthetics Item Master [RMPR ADD ITEM MASTER]</p></li>
<li><p>IFCAP Utilities [RMPR VEN/ITEM]</p></li>
<li><p>Print All Prosthetic Items [RMPR PRINT ALL ITEMS]</p></li>
<li><p>Complete Form 2529-3 [RMPR 10-2937a]</p></li>
</ul>
<blockquote>
<p><strong>2. RMPRMANAGER:</strong></p>
</blockquote>
<ul>
<li><p>Enter/Edit Site Parameters [RMPR SITE MENU]</p></li>
<li><p>Enter/Edit Station Site Parameters [RMPR SITE PARA]</p></li>
<li><p>Purge Obsolete Data [RMPR PURGE MENU]</p></li>
<li><p>Add/Edit Correspondence Skeleton Letter [RMPR CORR EDIT]</p></li>
</ul>
<blockquote>
<p><strong>3. RMPR LAB ADMIN:</strong></p>
<p>This key is for the Prosthetic Treatment Center administrative users. The holder of this Key will receive vital e-mail messages when a purchasing transaction associated with the lab has been canceled, or closed by either the Lab or the Administrative Section. Since the receipt of this mail is so critical, the EP has decided to deliver it based on this key instead of relying on a Mail Group. The mail is mandatory, and is not up to the users to decide if they want it delivered or not.</p>
<p><strong>4. RMPR LAB MENU:</strong></p>
</blockquote>
<ul>
<li><p>Prosthetic Lab Menu [RMPR LAB MENU]</p></li>
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
<td><h5 id="security-keys-continued">5 Security Keys (continued)</h5></td>
<td><blockquote>
<p><strong>5. RMPR LAB SUPERVISOR:</strong></p>
</blockquote>
<ul>
<li><p>Assign 2429-3 to Technician [RMPR 2529-3 ASSIGN]</p></li>
<li><p>Generate Worksheet 10-2937a [RMPR 10-2937a]</p></li>
<li><p>Holders of the RMPR LAB ADMIN and RMPR LAB SUPERVISOR security keys will be sent a message when a 2421 Request for Work Order has been initiated, returned to the Lab, canceled, delivered, or is awaiting approval.</p></li>
<li><p>One security key from the IFCAP package is used with Prosthetics. The PRCHZ REV is a reverse lock for the <strong>Item File Edit</strong> option (PRCHPC ITEM EDIT).</p></li>
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
<td><h5 id="prosthetics-purchasing-agents">Prosthetics Purchasing Agents</h5></td>
<td><blockquote>
<p>Prosthetics Purchasing Agents can function fully as independent users of the Prosthetics package without the RMPRSUPERVISOR key, but they will not be able to complete a purchase if the vendor or item they select is not in the appropriate file.</p>
<p>RMPRSUPERVISOR enables users to add/edit entries in the IFCAP ITEM MASTER and VENDOR files. It is strongly urged that this key be given to Prosthetics users who frequently purchase equipment and supplies for patients. A&amp;MM Service should be notified that Prosthetic Service has access to these files, and local training for adding/editing these files may need to be provided.</p>
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
<td><h5 id="prosthetics-lab-personnel">Prosthetics Lab personnel</h5></td>
<td><blockquote>
<p>Prosthetics Laboratory personnel need the RMPR LAB MENU key in order to access the Prosthetic Lab menu. Assigning a VAF 10-2529-3 to a technician and generating AMIS worksheets are limited to users with the RMPR LAB SUPERVISOR key. VAF 10-2421s may be completed by users assigned the RMPR LAB ADMIN key.</p>
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
<td><h5 id="class-i-dhcp-software">Class I DHCP software</h5></td>
<td><blockquote>
<p>The modification of Class I DHCP software data dictionaries is restricted to the adding of new data elements (station number multiplied by 1000) and to the creation of input/output templates (namespace concatenated to a Z) necessary to meet the specific needs of the local facility.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Prosthetics Security System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VA FileMan Accessible Files

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="file-access">File Access</h5></td>
<td><blockquote>
<p>If your Medical Center has run Part 3 of the Kernel installation, assign your Prosthetics users the following file access:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                    |            |               |               |               |                |                  |
|--------------------|------------|---------------|---------------|---------------|----------------|------------------|
| File           | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| REC PROS APPL/REP  | 660        | N             | Y             | Y             | N              | Y                |
| PROS RTN CONDEMN   | 660.1      | N             | Y             | Y             | Y              | Y                |
| PROS ITEM MASTER   | 661        | N             | Y             | Y             | N              | Y                |
| PROS DISAB CODE    | 662        | N             | Y             | N             | N              | N                |
| PROS AMIS CODES    | 663        | N             | Y             | N             | N              | N                |
| ACT NEW/REP WS TOT | 663.2      | N             | Y             | Y             | N              | Y                |
| PROS DISAB W.S.    | 663.3      | N             | Y             | N             | N              | N                |
| PROS APPT W.S.     | 663.4      | N             | Y             | Y             | Y              | Y                |
| PROS 1358          | 664        | N             | Y             | Y             | Y              | Y                |
| PROS 2529-3        | 664.1      | N             | Y             | Y\`           | Y              | Y                |

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="file-access-continued">File Access (continued)</h5></td>
<td><blockquote>
<p>If your Medical Center has run Part 3 of the Kernel installation, assign your Prosthetics users the following file access:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                           |            |               |               |               |                |                  |
|---------------------------|------------|---------------|---------------|---------------|----------------|------------------|
| File                  | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| PROS WORK ORDER           | 664.2      | N             | Y             | Y             | Y              | Y                |
| PROS LAB HRS DATE         | 664.3      | N             | Y             | Y             | Y              | Y                |
| PROS LAB/REST WS          | 664.4      | N             | Y             | Y             | Y              | Y                |
| PROS PATIENT              | 665        | N             | Y             | Y             | N              | Y                |
| PROS HOME/ LIAISON VISITS | 665.1      | N             | Y             | Y             | Y              | Y                |
| PROS LETTER               | 665.2      | N             | Y             | Y             | N              | Y                |
| PROS LTR TRANS            | 665.4      | N             | Y             | Y             | Y              | Y                |
| VEH OF RECORD             | 667        | N             | Y             | Y             | N              | Y                |
| PROS AUTO AD EQUIP        | 667.1      | N             | Y             | Y             | N              | Y                |
| AUTO AD MANUFAC           | 667.2      | N             | Y             | Y             | N              | Y                |

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="file-access-continued-1">File Access (continued)</h5></td>
<td><blockquote>
<p>If your Medical Center has run Part 3 of the Kernel installation, assign your Prosthetics users the following file access:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                |            |               |               |               |                |                  |
|----------------|------------|---------------|---------------|---------------|----------------|------------------|
| File       | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| VOR TRANS      | 667.3      | N             | Y             | Y             | Y              | Y                |
| PROS SUS       | 668        | N             | Y             | Y             | Y              | Y                |
| PROS LAB WO#   | 669.1      | N             | Y             | Y             | N              | Y                |
| PROS SITE PARA | 669.9      | N             | Y             | Y             | Y              | Y                |

#### VA FileMan Access Codes

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="access-codes">Access Codes</h5></td>
<td><blockquote>
<p>VA FileMan Access Codes have been assigned to the Prosthetic files. The at-sign (@) code restricts action unless the user is assigned the programmer access code “@”.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                    |            |               |               |               |                |                  |
|--------------------|------------|---------------|---------------|---------------|----------------|------------------|
| File           | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| REC PROS APPL/REP  | 660        | @             |               |               | @              |                  |
| PROS RTN/ CONDEMN  | 660.1      | @             |               |               |                |                  |
| PROS ITEM MASTER   | 661        | @             |               |               | @              |                  |
| PROS DISAB CODE    | 662        | @             |               | @             | @              | @                |
| PROS AMIS CODES    | 663        | @             |               | @             | @              | @                |
| ACT NEW/REP WS TOT | 663.2      | @             |               |               | @              |                  |
| PROS DISAB W.S.    | 663.3      | @             |               |               | @              |                  |
| PROS APPT W.S.     | 663.4      | @             |               |               |                |                  |
| PROS 1358          | 664        | @             |               |               |                |                  |
| PROS 2529-3        | 664.1      | @             |               |               |                |                  |
| PROS WORK ORDER    | 664.2      | @             |               |               |                |                  |

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="access-codes-continued">Access Codes (continued)</h5></td>
<td><blockquote>
<p>VA FileMan Access Codes have been assigned to the Prosthetic files. The at-sign (@) code restricts action unless the user is assigned the programmer access code “@”.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                           |            |               |               |               |                |                  |
|---------------------------|------------|---------------|---------------|---------------|----------------|------------------|
| File                  | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| PROS LAB HRS DATE         | 664.3      | @             |               |               |                |                  |
| PROS LAB/REST WS          | 664.4      | @             | @             | @             | @              | @                |
| PROS PATIENT              | 665        | @             |               |               | @              |                  |
| PROS HOME/ LIAISON VISITS | 665.1      | @             |               |               |                |                  |
| PROS LETTER               | 665.2      | @             |               |               | @              |                  |
| PROS LTR TRANS            | 665.4      | @             |               |               |                |                  |
| VEH OF RECORD             | 667        | @             |               |               | @              |                  |
| PROS AUTO AD EQUIP        | 667.1      | @             |               |               | @              |                  |
| AUTO AD MANUFAC           | 667.2      | @             |               |               | @              |                  |

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="access-codes-continued-1">Access Codes (continued)</h5></td>
<td><blockquote>
<p>VA FileMan Access Codes have been assigned to the Prosthetic files. The at-sign (@) code restricts action unless the user is assigned the programmer access code “@”.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                |            |               |               |               |                |                  |
|----------------|------------|---------------|---------------|---------------|----------------|------------------|
| File       | Number | DD Access | RD Access | WR Access | DEL Access | LAYGO Access |
| VOR TRANS      | 667.3      | @             |               |               |                |                  |
| PROS SUS       | 668        | @             |               |               |                |                  |
| PROS LAB WO#   | 669.1      | @             |               | @             | @              | @                |
| PROS SITE PARA | 669.9      | @             |               |               |                |                  |