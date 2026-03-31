---
consolidated_title: "bcma technical manual/security guide change pages"
app_code: PSB
doc_type: TM
master_source: "PSB*3*42 BCMA Version 3 Technical Manual/Security Guide Change Pages"
master_pub_date: February 2004
consolidated_from: 5 versions
prior_versions:
  - "PSB*3*2 BCMA Version 3 Technical Manual/Security Guide Change Pages"
  - "PSB*3*28 BCMA Version 3 Technical Manual/Security Guide Change Pages"
  - "PSB*3*32 BCMA Version 3 Technical Manual/Security Guide Change Pages"
  - "PSB*3*47 BCMA Version 3 Technical Manual/Security Guide Change Pages"
---

> ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

> TECHNICAL MANUAL/SECURITY GUIDE

# Version 3.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Version 3.0](#version-30)
  - [![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/002.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/003.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/004.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/005.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/006.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/007.png)Example: Minimum Required Packages and Versions](#psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages002pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages003pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages004pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages005pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages006pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages007pngexample-minimum-required-packages-and-versions)
  - [Example: BCMA V. 3.0 Routines Installed onto VistA Server](#example-bcma-v-30-routines-installed-onto-vista-server)
  - [![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/066.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/067.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/068.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/069.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/070.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/071.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/072.png)Example: “RAS” Messages Created for the Administration of a Medication Order (cont.)](#psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages066pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages067pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages068pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages069pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages070pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages071pngpsb-3-42-bcma-version-3-technical-manual-security-guide-change-pages072pngexample-ras-messages-created-for-the-administration-of-a-medication-order-cont)
> February 2004
> (Revised January 2011)
> Department of Veterans Affairs Product Development
> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2011</td>
<td><blockquote>
<p>i-ii, 6, 7, 10,</p>
<p>15,</p>
<p>B-2, B-4</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*42</p>
</blockquote></td>
<td><blockquote>
<p>Added note and list of BCMA Reports that were added to GUI only. Added definition of data field change for Indian Health Service.</p>
<p>Added Indian Health Service terms to Glossary.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/2009</td>
<td><blockquote>
<p>i-ii, 7, 9, 17</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*47</p>
</blockquote></td>
<td><blockquote>
<p>Added PSBPXFL and PSBPXLP to the list of installed routines. Add Immunizations Documentation by BCMA Nightly Task [PSB PX BCMA2PCE TASK] option to the <em>Manager</em> [PSB MGR] menu. Added Patient Care Encounter to the External Relationships section.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td><blockquote>
<p>i-ii, iv, 6-7,</p>
<p>13-14,</p>
<p>18-19, 21</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*28</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p>Update Table of Contents to include Remote Procedure Calls. (p. iv)</p>
</blockquote></li>
<li><p>Increased the total for the BCMA V .3.0 routines to 85 and files to 6. (p.6-7)</p></li>
<li><p>Updated the files and “BCMA V.3.0 Routines Installed onto VistA Server” Example. (p.7)</p></li>
<li><p>Updated the Mail Group Types in BCMA V.3.0 to include scanning failures. (p. 13)</p></li>
<li><blockquote>
<p>Updated Security Keys to include PSB UNABLE TO SCAN. (p. 14)</p>
</blockquote></li>
<li><blockquote>
<p>Added list of Remote Procedure Calls (RPCs). (p. 18)</p>
</blockquote></li>
</ul>
<blockquote>
<p>-Added new Glossary entry for LIMITED ACCESS BCMA. (p. 19)</p>
</blockquote>
<ul>
<li><p>Added new Glossary entry for PSB UNABLE TO SCAN. (p. 21) <mark>REDACTED</mark></p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/2008</td>
<td><blockquote>
<p>6-7, 9-10,</p>
<p>C-1, C-2,</p>
<p>C-4, C-5,</p>
<p>C-7, C-9</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*2</p>
</blockquote></td>
<td><blockquote>
<p>Description of [PSBO BZ] functionality added, code strings updated (p. C-1.)</p>
</blockquote>
<ul>
<li><p>Updated Intermec Printer Team Type Codes Information, Intermec Barcode Label Field Position Map, Intermec printer Sample Terminal Type File code descriptions updated (pp. C-4, C-5, C-7.)</p></li>
<li><p>Barcode samples updated – references to “Dosage” changed to “Dose” and space between colon and dose measurement deleted (p. C-9.)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/2007</td>
<td><blockquote>
<p>6-7</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*32</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p>Increased the total for the BCMA V. 3.0. routines to 68. (p.6)</p>
</blockquote></li>
<li><p>Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routine: PSBO XA. (p. 7)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2006</td>
<td><blockquote>
<p>6-7,</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*13</p>
</blockquote></td>
<td><blockquote>
<p>– Increased the total for the BCMA V. 3.0. routines to 68. (p.6)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9, 13</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>– Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routine: PSBO XA. (p. 7)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>– Updated Manager Menu [PSB MGR] options list to include Missing Dose Follow-up (correction) and Unknown Action Status Report (new with this patch). (p. 9)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>– Added description of the “Unknown Actions” mail group parameter. (p. 13)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/2006</td>
<td><blockquote>
<p>iv,</p>
<p>6, C1-C10</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*2</p>
</blockquote></td>
<td><blockquote>
<p><strong><u>Note</u></strong>: The functionality listed below will be activated with the release of PSB*3*2.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Updated Table of Contents to include new Appendix C. (p. iv)</p>
</blockquote></li>
<li><p>Added reference to new Unit Dose label printing functionality and Appendix C. (p. 6)</p></li>
<li><p>Added Appendix C: Interfacing with the Bar Code Label Printer. (p. C1-C10)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/2005</td>
<td><blockquote>
<p>6-7</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*16</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p>Increased the total for the BCMA V. 3.0. routines to 67. (p.6)</p>
</blockquote></li>
<li><p>Updated the “BCMA V. 3.0 Routines Installed onto VistA Server” example to include the following routines: PSBCSUTL, PSBCSUTX, PSBCSUTY. (p. 7)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>01/2005</td>
<td><blockquote>
<p>6-7,</p>
<p>14,</p>
<p>20-21</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*4</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p>Increased the total for the BCMA V. 3.0. routines to 64. (p.6)</p>
</blockquote></li>
<li><p>Updated the “BCMA V. 3.0 Routines Installed on to VistA Server” example to include the PSBOPF routine. (p. 7).</p></li>
<li><blockquote>
<p>Added description for new PSB READ ONLY security key. (p.14)</p>
</blockquote></li>
<li><p>Added new Glossary entries for PSB READ ONLY and Read-Only BCMA. (p. 20-21)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/2004</td>
<td><blockquote>
<p>6-7</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*3</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p>Increased the total for the BCMA V. 3.0 routines to 63. (p. 6)</p>
</blockquote></li>
<li><p>Updated the “BCMA V. 3.0 Routines Installed on to VistA Server” example to reflect the inclusion of routines PSBML2, PSBML3, and PSBMLLKU to the VistA Server. (p. 7)</p></li>
</ul>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/2004</td>
<td></td>
<td></td>
<td><blockquote>
<p>Original Released BCMA V. 3.0 Technical Manual/Security Guide</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Minimum Required Packages</strong></p>
</blockquote></th>
<th><blockquote>
<p>Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/002.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/003.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/004.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/005.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/006.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/007.png)Example: Minimum Required Packages and Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Minimum Version Needed</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Inpatient Medications</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MailMan</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/008.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Nursing</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Order Entry/Results Reporting</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pharmacy Data Management</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RPC Broker (32-bit)</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Toolkit</p>
</blockquote></td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Vitals/Measurements</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Installation Time Estimates</strong></p>
<p><strong>IMPORTANT:</strong></p>
<p>You should install and test BCMA in your test accounts <em><strong>before</strong></em> installing in</p>
<p>your production</p>
</blockquote></th>
<th><blockquote>
<p>On average, it takes approximately two minutes to install BCMA</p>
<p>V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its’ system resources.</p>
<p>Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/009.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/010.png)accounts.

![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/011.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Resource Requirements</strong></p>
<p><strong>TIP:</strong></p>
<p>The approximate size for ^PSB was calculated using a “normal” medication pass for a Unit Dose and an IV medication order.</p>
<p>This is only an estimated number; it serves as the “mean.”</p>
</blockquote></th>
<th><blockquote>
<p>This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Routines 84</p>
</blockquote></li>
<li><blockquote>
<p>Globals 1 (^PSB)</p>
</blockquote></li>
<li><blockquote>
<p>Files 6 (53.66-53.79)</p>
</blockquote></li>
<li><p>^PSB Size Unit Dose = 300 x # of Medications (in bytes) Administered</p></li>
</ul>
<blockquote>
<p>IV = 2100 x # of IV Bags Administered</p>
</blockquote>
<ul>
<li><blockquote>
<p>FTEE Support .2</p>
</blockquote></li>
<li><blockquote>
<p>FTEE Maintenance .2</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Response Time Monitor</strong></p>
<p>BCMA V. 3.0 does not include Response Time Monitor hooks.</p>
<p><strong>Laptops and Bar Code Scanners</strong></p>
<p>The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas, at your site, that use BCMA</p>
<p>V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.</p>
<p><strong>Printers</strong></p>
<p>Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.</p>
<p><strong>Unit Dose Label Printer Devices</strong></p>
<p>BCMA V. 3.0 includes the <em>Label Print</em> [PSBO BL] option for printing individual or batch Unit Dose bar code labels. This option allows sites the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBL uses site-specific printers or terminals to produce labels. See Appendix C: “Interfacing with the Bar Code Label Printer” for detailed setup information.</p>
<p><strong>IV Label Printer Devices</strong></p>
<p>Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section “Interfacing with</p>
<p>the Bar Code Label Printer” in the <em>Inpatient Medications V. 5.0 Technical Manual/Security Guide</em> for detailed setup information.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/012.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Files Required to Run BCMA V. 3.0</strong></p>
<p><strong>TIP:</strong></p>
<p>The namespace for the BCMA package is PSB and the primary global</p>
<p>is ^PSB.</p>
</blockquote></th>
<th><blockquote>
<p>BCMA V. 3.0 uses the following files installed on the VistA Server. “Journaling” is recommended.</p>
</blockquote>
<ul>
<li><p>^PSB (53.66, BCMA IV Parameters</p></li>
<li><p>^PSB (53.68, BCMA Missing Dose Request</p></li>
<li><p>^PSB (53.69, BCMA Report Request</p></li>
<li><p>^PSB (53.77, BCMA Unable to Scan Log</p></li>
<li><p>^PSB (53.78, BCMA Medication Variance Log</p></li>
<li><p>^PSB (53.79, BCMA Medication Log</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> You can learn more about these files by generating a list with file attributes using VA FileMan.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Routines Installed</strong></p>
</blockquote></td>
<td><blockquote>
<p>Review the listing below to learn the routines installed on to your site’s VistA Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.</p>
<p><strong>Note:</strong> You can use the <em>Kernel First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of each PSB routine.</p>
<p><strong>Routine Mapping</strong></p>
<p>At this time, we do <em>not</em> offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it</p>
<p>to load the new routines into memory.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Example: BCMA V. 3.0 Routines Installed onto VistA Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSBALL</p>
</blockquote></th>
<th><blockquote>
<p>PSBAPIPM</p>
</blockquote></th>
<th><blockquote>
<p>PSBCHIVH</p>
</blockquote></th>
<th><blockquote>
<p>PSBCHKIV</p>
</blockquote></th>
<th><blockquote>
<p>PSBCSUTL</p>
</blockquote></th>
<th><blockquote>
<p>PSBCSUTX</p>
</blockquote></th>
<th><blockquote>
<p>PSBCSUTY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSBMD</p>
</blockquote></td>
<td><blockquote>
<p>PSBML</p>
</blockquote></td>
<td><blockquote>
<p>PSBML1</p>
</blockquote></td>
<td><blockquote>
<p>PSBML2</p>
</blockquote></td>
<td><blockquote>
<p>PSBML3</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLEN</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLEN1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBMLHS</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLLKU</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLTS</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLU</p>
</blockquote></td>
<td><blockquote>
<p>PSBMLVAL</p>
</blockquote></td>
<td><blockquote>
<p>PSBO</p>
</blockquote></td>
<td><blockquote>
<p>PSBO1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSBOAL</p>
</blockquote></td>
<td><blockquote>
<p>PSBOBL</p>
</blockquote></td>
<td><blockquote>
<p>PSBOBLU</p>
</blockquote></td>
<td><blockquote>
<p>PSBOBZ</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCE</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCE1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBOCI1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCM</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCM1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCP</p>
</blockquote></td>
<td><blockquote>
<p>PSBOCP1</p>
</blockquote></td>
<td><blockquote>
<p>PSBODL</p>
</blockquote></td>
<td><blockquote>
<p>PSBODL1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSBODO</p>
</blockquote></td>
<td><blockquote>
<p>PSBOHDR</p>
</blockquote></td>
<td><blockquote>
<p>PSBOIV</p>
</blockquote></td>
<td><blockquote>
<p>PSBOIV1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMD</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMH</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMH1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBOMH2</p>
</blockquote></td>
<td><blockquote>
<p>PSBOML</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMM</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMM2</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMT1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOMV</p>
</blockquote></td>
<td><blockquote>
<p>PSBOPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSBOPF</p>
</blockquote></td>
<td><blockquote>
<p>PSBOPI</p>
</blockquote></td>
<td><blockquote>
<p>PSBOPM</p>
</blockquote></td>
<td><blockquote>
<p>PSBOPM1</p>
</blockquote></td>
<td><blockquote>
<p>PSBOSF</p>
</blockquote></td>
<td><blockquote>
<p>PSBOST</p>
</blockquote></td>
<td><blockquote>
<p>PSBOVT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBOWA</p>
</blockquote></td>
<td><blockquote>
<p>PSBOXA</p>
</blockquote></td>
<td><blockquote>
<p>PSBPAR</p>
</blockquote></td>
<td><blockquote>
<p>PSBPARIV</p>
</blockquote></td>
<td><blockquote>
<p>PSBPOIV</p>
</blockquote></td>
<td><blockquote>
<p>PSBPRN</p>
</blockquote></td>
<td><blockquote>
<p>PSBPXFL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSBPXLP</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPC</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPC1</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPC2</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPC3</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPCMO</p>
</blockquote></td>
<td><blockquote>
<p>PSBRPCXM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBSAGG</p>
</blockquote></td>
<td><blockquote>
<p>PSBSVHL7</p>
</blockquote></td>
<td><blockquote>
<p>PSBUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSBVAR</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLIV</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLPA</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLPB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSBVDLTB</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLU1</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLU3</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLUD</p>
</blockquote></td>
<td><blockquote>
<p>PSBVDLVL</p>
</blockquote></td>
<td><blockquote>
<p>PSBVITFL</p>
</blockquote></td>
<td><blockquote>
<p>PSBVT1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>84</td>
<td><blockquote>
<p>routines</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
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
<thead>
<tr class="header">
<th><blockquote>
<p><strong>BCMA CHUI Menus</strong></p>
</blockquote></th>
<th><blockquote>
<p>BCMA V. 3.0 exports three main menus. They include those listed below, in the CHUI version of BCMA V. 3.0. The options for each menu are listed in this section.</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>Manager Menu:</strong> [PSB MGR] is assigned to managers</p>
</blockquote></li>
<li><p><strong>Pharmacist Menu:</strong> [PSB PHARMACY] is assigned to all inpatient Pharmacists</p></li>
<li><p><strong>Nurse Menu:</strong> [PSB NURSE] is assigned to all clinicians and other personnel who administer active medication orders</p></li>
</ul>
<blockquote>
<p><strong>Manager Menu [PSB MGR]</strong></p>
<p>This menu includes the following options:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Drug File Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Immunizations Documentation by BCMA Nightly Task</p>
</blockquote></li>
<li><blockquote>
<p>Medication Administration Menu Nursing</p>
</blockquote>
<ul>
<li><p>Medication Administration Log Report</p></li>
<li><p>Missed Medications Report</p></li>
<li><p>Ward Administration Times Report</p></li>
<li><p>Due List Report</p></li>
<li><p>PRN Effectiveness List Report</p></li>
<li><p>Enter PRN Effectiveness</p></li>
<li><p>Manual Medication Entry</p></li>
<li><p>Medication Administration History (MAH) Report</p></li>
<li><p>Missing Dose Request</p></li>
<li><blockquote>
<p>Medication Variance Log</p>
</blockquote></li>
<li><blockquote>
<p>Drug File Inquiry</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Medication Administration Menu Pharmacy</p>
</blockquote>
<ul>
<li><blockquote>
<p>Medication Administration Log Report</p>
</blockquote></li>
<li><blockquote>
<p>Missed Medications Report</p>
</blockquote></li>
<li><blockquote>
<p>Due List Report</p>
</blockquote></li>
<li><blockquote>
<p>Medication Administration History (MAH) Report</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Request</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Follow-up</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Report</p>
</blockquote></li>
<li><blockquote>
<p>Label Print</p>
</blockquote></li>
<li><blockquote>
<p>Drug File Inquiry</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Missing Dose Follow-up</p>
</blockquote></li>
<li><blockquote>
<p>Reset User Parameters</p>
</blockquote></li>
<li><blockquote>
<p>Trouble Shoot Med Log</p>
</blockquote></li>
<li><blockquote>
<p>Unknown Action Status Report</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>BCMA CHUI Menus (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Pharmacy Medication Administration Menu [PSB PHARMACY]</strong></p>
<p>This menu includes the following options:</p>
</blockquote>
<ul>
<li><p>Medication Administration Log Report</p></li>
<li><p>Missed Medications Report</p></li>
<li><blockquote>
<p>Due List Report</p>
</blockquote></li>
<li><blockquote>
<p>Medication Administration History (MAH) Report</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Request</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Follow-up</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Report</p>
</blockquote></li>
<li><blockquote>
<p>Label Print</p>
</blockquote></li>
<li><blockquote>
<p>Drug File Inquiry</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Nursing Medication Administration Menu [PSB NURSE]</strong></p>
<p>This menu includes the following options:</p>
</blockquote>
<ul>
<li><p>Medication Administration Log Report</p></li>
<li><p>Missed Medications Report</p></li>
<li><blockquote>
<p>Ward Administration Times Report</p>
</blockquote></li>
<li><blockquote>
<p>Due List Report</p>
</blockquote></li>
<li><blockquote>
<p>PRN Effectiveness List Report</p>
</blockquote></li>
<li><blockquote>
<p>Enter PRN Effectiveness</p>
</blockquote></li>
<li><blockquote>
<p>Manual Medication Entry</p>
</blockquote></li>
<li><blockquote>
<p>Medication Administration History (MAH) Report</p>
</blockquote></li>
<li><blockquote>
<p>Missing Dose Request</p>
</blockquote></li>
<li><blockquote>
<p>Medication Variance Log</p>
</blockquote></li>
<li><blockquote>
<p>Drug File Inquiry</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Note:</strong> The following reports have been added to BCMA and are available via GUI only, but have not been added to the CHUI menus.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Cover Sheet Reports:</p>
</blockquote>
<ul>
<li><p>Medication Overview</p></li>
<li><p>PRN Overview</p></li>
<li><p>IV Overview</p></li>
<li><p>Expired/DC’d/Expiring Orders</p></li>
</ul></li>
<li><blockquote>
<p>IV Bag Status Report</p>
</blockquote></li>
<li><blockquote>
<p>Medication Therapy Report</p>
</blockquote></li>
<li><blockquote>
<p>Unable to Scan Detailed Report</p>
</blockquote></li>
<li><blockquote>
<p>Unable to Scan Summary Report</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Developing a Contingency Plan</strong></p>
</blockquote></th>
<th><blockquote>
<p>In March 2006, patch PSB*3*8, the BCMA Backup System (BCBU), was reissued with significant enhancements to the field as a Class I solution for the BCMA Contingency Plan. This patch provides real- time backup of all inpatient medication activities on a designated workstation. Review the patch description to learn more about the benefits of this patch.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/013.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/014.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/015.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/016.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/017.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/018.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/019.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/020.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/021.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/022.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/023.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Sample HL7 Data Fields Broadcast to BCMA Subscribers</strong></p>
</blockquote></th>
<th><blockquote>
<p>BCMA includes the Standards from the HL7 V. 2.4 (VistA Messaging) package. For more information, refer to the VistA Messaging and Interface Services Web site at: <mark>REDACTED</mark> This section provides a list of sample Health Level Seven (HL7) data fields that BCMA broadcasts to BCMA HL7 subscribers. Review the information to learn the “RAS” messages created for the administration and/or update of a medication order. The activities, which cause the broadcast of BCMA HL7 messages, are called “trigger events.” BCMA HL7 trigger events are MEDPASS, UPDATE STATUS, PRN EFFECTIVENESS, and ADD COMMENT.</p>
<p><strong>Note:</strong> Every message will not use every data field and every segment provided. Some segments may repeat as necessary. Some segments</p>
<p>may not appear in the exact order depicted below for all trigger events, but they will be consistent for each specific trigger event.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/024.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/025.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/026.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/027.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/028.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/029.png)Example: “RAS” Messages Created for the Administration of a Medication Order

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEG</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SEQ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 Type</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/030.png) ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/031.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Field Separator</p>
</blockquote></td>
<td><blockquote>
<p>^</p>
</blockquote></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Encoding Characters</p>
</blockquote></td>
<td><blockquote>
<p>~|\&amp;</p>
</blockquote></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/032.png)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Sending Application</p>
</blockquote></td>
<td><blockquote>
<p>PSB HL7 SRV</p>
</blockquote></td>
<td><blockquote>
<p>hierarchic designator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Sending Facility</p>
</blockquote></td>
<td>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/033.png)</td>
<td><blockquote>
<p>hierarchic designator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/034.png)</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Application</p>
</blockquote></td>
<td><blockquote>
<p>PSB HL7 SUB</p>
</blockquote></td>
<td><blockquote>
<p>hierarchic designator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/035.png) ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/036.png)</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Facility</p>
</blockquote></td>
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/037.png)</p>
</blockquote></td>
<td><blockquote>
<p>hierarchic designator</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>D/T of Message</p>
</blockquote></td>
<td><blockquote>
<p>20030530075514-0600</p>
</blockquote></td>
<td><blockquote>
<p>HL7 format timestamp (yyyymmddhhnnss-0600)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/038.png)</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Security</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
<td><blockquote>
<p>RAS~O17</p>
</blockquote></td>
<td><blockquote>
<p>composite</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
<td><blockquote>
<p>5001457</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/039.png)</p></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/040.png)</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p>processing type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
<td><blockquote>
<p>2.4</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/041.png)</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>Sequence Number</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/042.png)</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Continuation Pointer</p>
</blockquote></td>
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/043.png)</p>
</blockquote></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Accept Acknowledgement Type</p>
</blockquote></td>
<td><blockquote>
<p>AL</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/044.png)</p></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/045.png)</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>Application</p>
<p>Acknowledgment Type</p>
</blockquote></td>
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>Country Code</p>
</blockquote></td>
<td><blockquote>
<p>USA</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/046.png)</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>Character Set</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/047.png)</p>
</blockquote></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>Principal Language of Message</p>
</blockquote></td>
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/048.png)</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/049.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/050.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/051.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/052.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/053.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/054.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/055.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/056.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/057.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/058.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/059.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/060.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/061.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/062.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/063.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/064.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/065.png)

## ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/066.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/067.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/068.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/069.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/070.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/071.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/072.png)Example: “RAS” Messages Created for the Administration of a Medication Order (cont.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEG</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SEQ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 Type</strong></p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/073.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/074.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PID</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Patient Identifier List</p>
</blockquote></td>
<td><blockquote>
<p>748</p>
</blockquote></td>
<td><blockquote>
<p>composite ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Alternate Patient ID</p>
</blockquote></td>
<td><blockquote>
<p>54~~~~AGE</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/075.png)</p></td>
<td><blockquote>
<p>extended composite ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name</p>
</blockquote></td>
<td><blockquote>
<p>BCMAPATIENT~TWO</p>
</blockquote></td>
<td><blockquote>
<p>patient name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time of Birth</p>
</blockquote></td>
<td><blockquote>
<p>19490101</p>
</blockquote></td>
<td><blockquote>
<p>HL7 format timestamp (yyyymmdd)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Administrative Sex</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/076.png)</p></td>
<td><blockquote>
<p>user table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>SSN Number (VA)</p>
<p>or HRN Number (IHS)– Patient</p>
</blockquote></td>
<td><blockquote>
<p>000001000 (VA)</p>
<p>or 123456 (IHS)</p>
</blockquote></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PV1</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class</p>
</blockquote></td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>table 0004</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Patient Location</p>
</blockquote></td>
<td><blockquote>
<p>7A GEN MED 724-A~~~500</p>
</blockquote></td>
<td><blockquote>
<p>user table</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Attending Doctor</p>
</blockquote></td>
<td><blockquote>
<p>BCMAPROVIDER~ONE</p>
</blockquote></td>
<td><blockquote>
<p>composite ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORC</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Order Control</p>
</blockquote></td>
<td><blockquote>
<p>XX</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/077.png)</p></td>
<td><blockquote>
<p>table 119</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Placer Order Number</p>
</blockquote></td>
<td><blockquote>
<p>1045~PSB~1045~IEN</p>
</blockquote></td>
<td><blockquote>
<p>entity identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Filler Order Number</p>
</blockquote></td>
<td><blockquote>
<p>13V</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/078.png)</p></td>
<td><blockquote>
<p>entity identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Quantity/Timing</p>
</blockquote></td>
<td><blockquote>
<p>~~~~~~~~~C</p>
</blockquote></td>
<td><blockquote>
<p>dosage, scheduled</p>
<p>administration time, schedule type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>Parent</p>
</blockquote></td>
<td><blockquote>
<p>~</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/079.png)</p></td>
<td><blockquote>
<p>composite</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>D/T of Transaction</p>
</blockquote></td>
<td><blockquote>
<p>20030530075514-0600</p>
</blockquote></td>
<td><blockquote>
<p>HL7 format timestamp</p>
<p>(yyyymmddhhnnss-0600)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Entered by</p>
</blockquote></td>
<td><blockquote>
<p>BCMANURSE~ONE</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/080.png)</p></td>
<td><blockquote>
<p>extended composite name</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Order Effective D/T</p>
</blockquote></td>
<td><blockquote>
<p>20030530075514-0600</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/081.png)</p></td>
<td><blockquote>
<p>HL7 format timestamp</p>
<p>(yyyymmddhhnnss-0600)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>Action By</p>
</blockquote></td>
<td><blockquote>
<p>BCMANURSE~ONE</p>
</blockquote></td>
<td><blockquote>
<p>extended composite name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RXR</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Route</p>
</blockquote></td>
<td><blockquote>
<p>IV</p>
</blockquote></td>
<td><blockquote>
<p>table 0162</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Administration Site</p>
</blockquote></td>
<td><blockquote>
<p>3 INJECTION SITE</p>
</blockquote></td>
<td><blockquote>
<p>table 0163</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RXO</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Requested Give Code</p>
</blockquote></td>
<td><blockquote>
<p>269~FLUOROURACIL</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Requested Give Amount</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="even">
<td>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/082.png) ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/083.png)</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Requested Dispense Code</p>
</blockquote></td>
<td><blockquote>
<p>748V52</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>Requested Give Rate Amount</p>
</blockquote></td>
<td><blockquote>
<p>~250 ml/hr</p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/084.png)</p>
</blockquote></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/085.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/086.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/087.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/088.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/089.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/090.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/091.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/092.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/093.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/094.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/095.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/096.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/097.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/098.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/099.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/100.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/101.png)

> ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/102.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/103.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/104.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/105.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/106.png)![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/107.png)Example: “RAS” Messages Created for the Administration of a Medication Order (cont.)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEG</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SEQ</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 Type</strong></p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/108.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/109.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RXC</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>RX Component Type</p>
</blockquote></td>
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>table 0166</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/110.png)</td>
<td><blockquote>
<p>2</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/111.png)</p></td>
<td><blockquote>
<p>Component Code</p>
</blockquote></td>
<td><blockquote>
<p>20~5-FLUOURACIL</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/112.png)</p></td>
<td><blockquote>
<p>coded element</p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/113.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Component Amount</p>
</blockquote></td>
<td><blockquote>
<p>5-FLUOURACIL</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/114.png)</p></td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Component Units</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RXC</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>RX Component Type</p>
</blockquote></td>
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>table 0166</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Component Code</p>
</blockquote></td>
<td><blockquote>
<p>8~AMINO ACID SOLUTION</p>
<p>8.5%</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/115.png)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Component Amount</p>
</blockquote></td>
<td><blockquote>
<p>AMINO ACID SOLUTION 8.5%</p>
</blockquote></td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/116.png)</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Component Units</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/117.png)</p></td>
<td>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/118.png)</td>
<td><blockquote>
<p>coded element</p>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/119.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RXA</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>Give Sub-ID Counter</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/120.png)</p></td>
<td><blockquote>
<p>number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/121.png)</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Administration Sub-ID</p>
<p>Counter</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>number</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Date/Time Start of Administration</p>
</blockquote></td>
<td><blockquote>
<p>20030530075514-0600</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/122.png)</p></td>
<td><blockquote>
<p>HL7 format timestamp (yyyymmddhhnnss-0600)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Administered Code</p>
</blockquote></td>
<td><blockquote>
<p>20~5-FLUOURACIL</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/123.png)</p></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Administered Amount</p>
</blockquote></td>
<td><blockquote>
<p>450 MG</p>
</blockquote></td>
<td><blockquote>
<p>number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/124.png)</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>Administered Unit</p>
</blockquote></td>
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/125.png)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/126.png)</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>Administration Notes</p>
</blockquote></td>
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/127.png)</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>Substance/Treatment Refusal Reason</p>
</blockquote></td>
<td><blockquote>
<p>~Elevated Blood Sugar</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/128.png)</p></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>Indication</p>
</blockquote></td>
<td><blockquote>
<p>~</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>Completion Status</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>user table</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NTE</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Source of Comment</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>table 105</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/129.png)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Comment</p>
</blockquote></td>
<td><blockquote>
<p>This is a comment …</p>
</blockquote></td>
<td><blockquote>
<p>free text</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/130.png) ![](psb-3-42-bcma-version-3-technical-manual-security-guide-change-pages/131.png)</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Comment Type</p>
</blockquote></td>
<td><blockquote>
<p>BCMANURSE~ONE~20030 530075514-0600~Date</p>
<p>Entered</p>
</blockquote></td>
<td><blockquote>
<p>coded element</p>
<p>(includes HL7 format timestamp [yyyymmddhhnnss-0600])</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Definitions of Data Fields Under FIELD NAME Column</strong></p>
</blockquote></th>
<th><blockquote>
<p>This section lists the definitions for some of the data fields provided under the FIELD NAME column, along with the location of the data field. The message header (i.e., the MSH segment) is constructed and supported by the VistA HL7 message development tool.</p>
<p><strong>Note:</strong> The MSH segment field names are <em>not</em> described below.</p>
</blockquote>
<ul>
<li><blockquote>
<p><strong>PATIENT ID:</strong> Field (#.01) of the BCMA MEDICATION LOG file (#53.79) and Internal Entry Number (IEN) pointer to the PATIENT file (#2).</p>
</blockquote></li>
<li><p><strong>PATIENT NAME:</strong> As returned by the Application Program Interface (API) VADPT.</p></li>
<li><blockquote>
<p><strong>DATE OF BIRTH:</strong> As returned by the API VADPT.</p>
</blockquote></li>
<li><p><strong>ADMINISTRATIVE SEX:</strong> As returned by the API VADPT.</p></li>
<li><p><strong>SSN NUMBER (VA) or HRN NUMBER (IHS):</strong> As returned by the API VADPT.</p></li>
<li><blockquote>
<p><strong>PATIENT LOCATION:</strong> Field (#.02) of the BCMA MEDICATION LOG file (#53.79), which contains the actual room-bed and ward location of the patient at the time the medication pass occurred. Also contains field (#.03) of the BCMA MEDICATION LOG file (#53.79), which contains the division number of the ward that the patient was on during the medication pass.</p>
</blockquote></li>
<li><p><strong>PLACER ORDER NUMBER:</strong> IEN for the BCMA MEDICATION LOG file (#53.79).</p></li>
<li><blockquote>
<p><strong>FILLER ORDER NUMBER:</strong> Contains the ORDER REFERENCE NUMBER field (#.11) of the BCMA MEDICATION LOG file (#53.79), which contains the IEN of the actual medication order from the PHARMACY PATIENT file (#55)PREVIOUS ORDER NUMBER as returned by the API PSJBCMA1.</p>
</blockquote></li>
<li><p><strong>QUANTITY/TIMING:</strong> Contains the order dosage, schedule type, and scheduled administration time data from the BCMA MEDICATION LOG file (#53.79), fields #.15, #.12, and #.13 respectively.</p></li>
<li><p><strong>PARENT:</strong> Contains the PREVIOUS ORDER NUMBER as returned by the PSB routine PSBVT.</p></li>
<li><blockquote>
<p><strong>DATE/TIME OF TRANSACTION:</strong> Contains the ACTION DATE/TIME field (#.06) of the BCMA MEDICATION LOG file (#53.79), which contains the FileMan date/time of the actual time that the action was taken.</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSB*3*28 BCMA Version 3 Technical Manual/Security Guide Change Pages

## BCMA V. 3.0 and This Guide 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Benefits of BCMA V. 3.0 1

> Benefits of This Guide 1

> Our Target Audience. 1

> Other Sources of Information 2

> Background/Technical Information 2

> This Manual and Related Documentation 2

> Conventions Used in This Guide 2

> Obtaining On-line Help 3

> Locating Detailed Listings 3

> Routines 3

> Data Dictionaries 3

## Implementation and Maintenance 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Minimum Required Packages 5

> Installation Time Estimates 5

> Resource Requirements 6

> Response Time Monitor 6

> Laptops and Bar Code Scanners 6

> Printers 6

> Unit Dose Label Printer Devices 6

> IV Label Printer Devices 6

> Files Required to Run BCMA V. 3.0 7

> Routines Installed 7

> Routine Mapping 7

## Exported Options 9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BCMA CHUI Menus 9

> Manager Menu \[PSB MGR\] 9

> Pharmacy Medication Administration Menu \[PSB PHARMACY\] 10

> Nursing Medication Administration Menu \[PSB NURSE\] 10

## Archiving and Purging 11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Archive and Purge Capabilities 11

## Security Features 13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Defining Mail Groups in BCMA 13

> Creating Mail Groups for BCMA V. 3.0 13

> Mail Group Types in BCMA V. 3.0 13

> Assigning Menus to Users 14

> CHUI Version 14

> GUI Version 14

> Allocating Security Keys to Users 14

> Establishing Electronic Signature Codes 14

> Developing a Contingency Plan 15

> February 2004 BCMA V. 3.0 Technical Manual/Security Guide iii

> Internal and External Relations 17

Internal Relations 17

Options 17

Package-Wide Variables 17

Templates 17

External Relations 17

Glossary 19

Learning BCMA V. 3.0 Lingo 19

> Appendix A: Processing of Schedule Information............................................. A-1

How BCMA Processes Schedule Information ............................................................................... A-1

Steps for Processing Schedule Information ................................................................................... A-1

Examples of Odd Schedules .......................................................................................................... A-4

Examples of Schedules That Are Not Odd Schedules ................................................................... A-4

## Appendix B: HL7 Messaging for BCMA .............................................................. B-1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sample HL7 Data Fields Broadcast to BCMA Subscribers............................................................B-1

> Definitions of Data Fields Under FIELD NAME Column .............................................................B-4

> Sample HL7 Data Fields Passed in Each Trigger Event .................................................................B-8

## Appendix C: Interfacing with the Bar Code Label Printer ................................. C-1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction .....................................................................................................................................C-1

Hardware Setup...............................................................................................................................C-1

Software Setup ................................................................................................................................C-1

Printer Control Codes .................................................................................................................... C-2

Control Code Set Up...................................................................................................................... C-2

Example Terminal Type Files........................................................................................................ C-6

Dot Matrix and Laser Printers........................................................................................................ C-8

Printed Bar Code Unit Dose Label Sample.....................................................................................C-9

JCAHO Standard for Medication Labeling\*.................................................................................C-10

> iv BCMA V. 3.0 Technical Manual/Security Guide January 2009 PSB\*3\*28

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Minimum Required Packages</strong></p>
</blockquote></th>
<th>Before installing BCMA V. 3.0, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/002.png)Example: Minimum Required Packages and Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Minimum Version Needed</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Inpatient Medications</td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Nursing</td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Pharmacy Data Management</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RPC Broker (32-bit)</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Toolkit</td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Vitals/Measurements</td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Installation Time Estimates</strong></p>
<p><strong>IMPORTANT:</strong></p>
<p>You should install and test BCMA in your test accounts <em><strong>before</strong></em> installing in your production</p>
</blockquote></th>
<th><p>On average, it takes approximately two minutes to install BCMA</p>
<p>V. 3.0. This estimate was provided by a few of our BCMA V. 3.0 Beta Test sites. Actual times may vary, depending on how your site is using its’ system resources.</p>
<p>Suggested time to install: non-peak requirement hours. During the install process, PC Client users should not be accessing the Client Software.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/003.png)accounts.

> February 2004 BCMA V. 3.0 Technical Manual/Security Guide 5

![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/004.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Resource Requirements</strong></p>
<p><strong>TIP:</strong></p>
<p>The approximate size for ^PSB was calculated using a “normal” medication pass for a Unit Dose and an IV medication order.</p>
<p>This is only an estimated number; it serves as the “mean.”</p>
</blockquote></th>
<th><p>This section summarizes the (approximate) number of resources required to install BCMA V. 3.0.</p>
<ul>
<li><p>Routines 85</p></li>
<li><p>Globals 1 (^PSB)</p></li>
<li><p>Files 6 (53.66-53.79)</p></li>
<li><p>^PSB Size Unit Dose = 300 x # of Medications (in bytes) Administered</p></li>
</ul>
<blockquote>
<p>IV = 2100 x # of IV Bags Administered</p>
</blockquote>
<ul>
<li><p>FTEE Support .2</p></li>
<li><p>FTEE Maintenance .2</p></li>
</ul>
<p><strong>Response Time Monitor</strong></p>
<p>BCMA V. 3.0 does not include Response Time Monitor hooks.</p>
<p><strong>Laptops and Bar Code Scanners</strong></p>
<p>The approximate requirements for laptops and bar code scanners depend on the number of Inpatient areas, at your site, that use BCMA</p>
<p>V. 3.0 for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward.</p>
<p><strong>Printers</strong></p>
<p>Your site should provide printers for creating patient wristbands and medication bar code labels, and for handling Missing Dose Requests sent from BCMA V. 3.0 to the Pharmacy.</p>
<p><strong>Unit Dose Label Printer Devices</strong></p>
<p>BCMA V. 3.0 includes the <em>Label Print</em> [PSBO BL] option for printing individual or batch Unit Dose bar code labels. This option allows sites the flexibility to use any printer that has bar code printing capabilities to produce BCMA bar code labels. Routine PSBOBL uses site-specific printers or terminals to produce labels. See Appendix C: “Interfacing with the Bar Code Label Printer” for detailed setup information.</p>
<p><strong>IV Label Printer Devices</strong></p>
<p>Inpatient Medications V. 5.0 provides a menu option for printing individual or batch IV bar code labels. See the section “Interfacing with the Bar Code Label Printer” in the <em>Inpatient Medications V. 5.0</em></p>
<p><em>Technical Manual/Security Guide</em> for detailed setup information.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 6 BCMA V. 3.0 Technical Manual/Security Guide January 2009 PSB\*3\*28

![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/005.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Files Required to Run BCMA V. 3.0</strong></p>
<p><strong>TIP:</strong></p>
<p>The namespace for the BCMA package is PSB and the primary global</p>
<p>is ^PSB.</p>
</blockquote></th>
<th><p>BCMA V. 3.0 uses the following files installed on the VistA Server. “Journaling” is recommended.</p>
<ul>
<li><p>^PSB (53.66, BCMA IV Parameters</p></li>
<li><p>^PSB (53.68, BCMA Missing Dose Request</p></li>
<li><p>^PSB (53.69, BCMA Report Request</p></li>
<li><p>^PSB (53.77, BCMA Unable to Scan Log</p></li>
<li><p>^PSB (53.78, BCMA Medication Variance Log</p></li>
<li><p>^PSB (53.79, BCMA Medication Log</p></li>
</ul>
<p><strong>Note:</strong> You can learn more about these files by generating a list with file attributes using VA FileMan.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Routines Installed</strong></p>
</blockquote></td>
<td><p>Review the listing below to learn the routines installed on to your site’s VistA Server during the installation of BCMA V. 3.0. The first line of each routine briefly describes its general function.</p>
<p><strong>Note:</strong> You can use the <em>Kernel First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of each PSB routine.</p>
<p><strong>Routine Mapping</strong></p>
<p>At this time, we do <em>not</em> offer any recommendations for routine mapping. However, if you choose to map the BCMA V. 3.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory.</p></td>
</tr>
</tbody>
</table>

## Callable Routines, Entry Points, and Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BCMA V. 3.0 includes two callable routines: PSBAPIPM and PSBMLHS. Each routine is described in this section, along with the entry points and variables information for each.

- PSBAPIPM: Provides information to Inpatient Medications

> V. 5.0 for determining the start date for a renewed order.

- PSBMLHS: Provides other software packages with the ability to call the BCMA Medication History Report. The report lists medications, that a patient has received, by orderable item.

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BCMA subscribes to Database Integration Agreements (DBIAs) with the Inpatient Medications, CPRS, Nursing, and Registration packages. BCMA V. 3.0 also offers DBIAs for other packages to subscribe to as well.

> For detailed information about these DBIAs, log in to FORUM and select the *Integration Agreements Menu* \[DBA IA ISC\] option located under the *DBA* \[DBA\] option (Data Base Administrator). Once in the Integration Agreements Menu Option, select “Inquire” and type BCMA at the “Select INTEGRATION REFERENCES:” prompt.

## Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Following is a list of Remote Procedure Calls associated with BCMA.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1 PSB ALLERGY</p>
</blockquote></th>
<th><blockquote>
<p>2 PSB BAG DETAIL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3 PSB CHECK IV</p>
</blockquote></td>
<td><blockquote>
<p>4 PSB CHECK SERVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5 PSB COVERSHEET1</p>
</blockquote></td>
<td><blockquote>
<p>6 PSB CPRS ORDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7 PSB DEVICE</p>
</blockquote></td>
<td><blockquote>
<p>8 PSB FMDATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9 PSB GETIVPAR</p>
</blockquote></td>
<td><blockquote>
<p>10 PSB GETORDERTAB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11 PSB GETPRNS</p>
</blockquote></td>
<td><blockquote>
<p>12 PSB GETPROVIDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13 PSB INSTRUCTOR</p>
</blockquote></td>
<td><blockquote>
<p>14 PSB IV ORDER HISTORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15 PSB LOCK</p>
</blockquote></td>
<td><blockquote>
<p>16 PSB MAIL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17 PSB MAN SCAN FAILURE</p>
</blockquote></td>
<td><blockquote>
<p>18 PSB MAXDAYS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19 PSB MED LOG LOOKUP</p>
</blockquote></td>
<td><blockquote>
<p>20 PSB MEDICATION HISTORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>21 PSB MOB DRUG LIST</p>
</blockquote></td>
<td><blockquote>
<p>22 PSB NURS WARDLIST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23 PSB PARAMETER</p>
</blockquote></td>
<td><blockquote>
<p>24 PSB PUTIVPAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>25 PSB REPORT</p>
</blockquote></td>
<td><blockquote>
<p>26 PSB SCANMED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27 PSB SCANPT</p>
</blockquote></td>
<td><blockquote>
<p>28 PSB SERVER CLOCK VARIANCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29 PSB SUBMIT MISSING DOSE</p>
</blockquote></td>
<td><blockquote>
<p>30 PSB TRANSACTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31 PSB USERLOAD</p>
</blockquote></td>
<td><blockquote>
<p>32 PSB USERSAVE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>33 PSB UTL XSTATUS SRCH</p>
</blockquote></td>
<td><blockquote>
<p>34 PSB VALIDATE ESIG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35 PSB VALIDATE ORDER</p>
</blockquote></td>
<td><blockquote>
<p>36 PSB VERSION CHECK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>37 PSB VITAL MEAS FILE</p>
</blockquote></td>
<td><blockquote>
<p>38 PSB VITALS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39 PSB WARDLIST</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 18 BCMA V. 3.0 Technical Manual/Security Guide January 2009 PSB\*3\*28

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA</strong></p>
<p><strong>V. 3.0 Lingo</strong></p>
</blockquote></th>
<th>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/006.png)Acronym/Term Definition

> Archive To transfer files from a computer onto long-term storage.

> BCMA Clinical Reminders A marquee located in the lower, right-hand corner of the VDL that

> identifies PRN medication orders needing effectiveness documentation. The setting is based on the “PRN Documentation” site parameter, and applies to current admissions or the site parameter timeframe (whichever is greater). A mouse-over list displays when the pointer is placed over the PRN Effectiveness Activity, or a full list is available by double clicking on the Activity.

> CHUI Character-based User Interface.

> Client An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.

> CPRS Computerized Patient Record System. A VistA software application that allows users to enter patient orders into different packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.

> Data Dictionary Also called “DD,” the dictionary that contains file attributes.

> DBIA Database Integration Agreement. A formal understanding between two or more application packages which describes how data is shared or how packages interact. This Agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.

> FileMan The VistA database management system.

> GUI Graphical User Interface. The type of interface chosen for BCMA V. 3.0.

> IV A medication given intravenously (within a vein) to a patient from an IV bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.

> Journaling A record of changes made in files and messages transmitted. It is quite

> useful when recovering previous versions of a file before updates were made, or to reconstruct updates if an updated file gets damaged.

> ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/007.png)LIMITED ACCESS BCMA A mode in which BCMA can be accessed that provides medication

> administering users the ability to access patient records for non- medication administration documentation, review and reporting purposes without being at the patient’s bedside.

January 2009 BCMA V. 3.0 Technical Manual/Security Guide 19

PSB\*3\*28

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA</strong></p>
<p><strong>V. 3.0 Lingo (cont.)</strong></p>
</blockquote></th>
<th>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/008.png)![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/009.png)Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Acronym/Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MAH</strong></td>
<td><blockquote>
<p><strong>M</strong>edication <strong>A</strong>dministration <strong>H</strong>istory. A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The date column lists three asterisks (*) if a medication was Discontinued.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>MAR</strong></td>
<td><blockquote>
<p><strong>M</strong>edication <strong>A</strong>dministration <strong>R</strong>ecord. The traditional, handwritten record used for noting when a patient received a medication. BCMA V. 3.0 replaces this record with an MAH.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>NOW Order</strong></td>
<td><blockquote>
<p>A medication order given ASAP to a patient, entered as a One-Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Patient Transfer Notification</strong></td>
<td><blockquote>
<p>A message that displays when a patient’s record is opened or the Unit Dose or IVP/IVPB Medication Tab is viewed for the first time. This message indicates that the patient has had a movement type (usually a transfer) within the site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PRN Order</strong></td>
<td><blockquote>
<p>The Latin abbreviation for <strong>P</strong>ro <strong>R</strong>e <strong>N</strong>ata. A medication dosage given to a patient on an “as needed” basis.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSB CPRS MED BUTTON</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and NOW (One-Time) medication orders using the CPRS Med Order Button on the BCMA VDL.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSB INSTRUCTOR</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSB MANAGER</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSB READ ONLY</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to users that can only access BCMA in Read-Only mode. Users who are assigned the PSB READ ONLY security key will never be able to administer medications or perform any actions against a patient’s medical record. The PSB READ ONLY security key overrides all other BCMA security keys.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 20 BCMA V. 3.0 Technical Manual/Security Guide February 2004

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA</strong></p>
<p><strong>V. 3.0 Lingo (cont.)</strong></p>
</blockquote></th>
<th>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this guide.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/010.png)Example: Alphabetical Listing of BCMA V. 3.0 Acronyms and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Acronym/Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PSB STUDENT</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options within BCMA V. 3.0. This key also requires that a nursing instructor sign on to BCMA.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSB UNABLE TO SCAN</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to allow the user to run the Unable to Scan (Detailed and Summary) reports.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Purge</strong></td>
<td><blockquote>
<p>To delete a set of data, and all references to the data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Read-Only BCMA</strong></td>
<td><blockquote>
<p>A mode in which BCMA can be accessed that provides non-medication administering users the ability to view a patient’s VDL and print reports, without performing any actions against a patient’s medical record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>RPC</strong></td>
<td><blockquote>
<p><strong>R</strong>emote <strong>P</strong>rocedure <strong>C</strong>all. A procedure stored on the VistA Server, which is executed to return data to the Client.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>RPC Broker</strong></td>
<td><blockquote>
<p>A Client/Server System within the VA’s Veterans Health Information Systems and Technology Architecture (VistA) environment. It enables client applications to communicate and exchange data with M Servers.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Security Keys</strong></td>
<td><blockquote>
<p>Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Server</strong></td>
<td><blockquote>
<p>An architecture in which one computer can get information from another. The Server, which can be anything from a personal computer to a mainframe, supplies the requested data or services to the Client.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>STAT Order</strong></td>
<td><blockquote>
<p>A medication order given immediately to a patient, entered as a One- Time order by Providers and Pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VDL</strong></td>
<td><blockquote>
<p><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</p>
<p><strong>Note:</strong> This is called BCMA VDL in this guide to eliminate confusion with the VistA Documentation Library (VDL) also mentioned in this guide.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td><blockquote>
<p><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Ward Stock</strong></td>
<td><blockquote>
<p>Unit Dose and IV medications that are “stocked” on an ongoing basis on wards and patient care areas. They are packaged in a ready-to-use form or compounded by the medication administrator.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ZPL</strong></td>
<td><blockquote>
<p><strong>Z</strong>ebra <strong>P</strong>rogramming <strong>L</strong>anguage.</p>
</blockquote></td>
</tr>
</tbody>
</table>

January 2009 BCMA V. 3.0 Technical Manual/Security Guide 21

![](psb-3-28-bcma-version-3-technical-manual-security-guide-change-pages/011.png)PSB\*3\*28

> 22 BCMA V. 3.0 Technical Manual/Security Guide February 2004
