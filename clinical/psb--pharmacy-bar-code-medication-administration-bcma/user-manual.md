---
consolidated_title: "bcma manager's user manual change pages"
app_code: PSB
doc_type: UM
master_source: "PSB*3*42 BCMA Version 3 Manager's User Manual Change Pages"
master_pub_date: February 2004
consolidated_from: 4 versions
prior_versions:
  - "PSB*3*47 BCMA Version 3 Manager's User Manual Change Pages"
  - "PSB*3*58 BCMA Version 3 Manager's User Manual Change Pages"
  - "PSB*3*68 BCMA Version 3 Manager's User Manual Change Pages"
---

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

> MANAGER’S USER MANUAL

## Version 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> February 2004

> (Revised January 2011)

> Department of Veterans Affairs Product Development

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
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
<p>i, iii-iv, 12-</p>
<p>13, 54, 57,</p>
<p>59-64</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*42</p>
</blockquote></td>
<td><blockquote>
<p>Removed field Scratch HFS Directory from the Parameters Tab, and replaced corresponding Site Parameters screen capture.</p>
<p>Added Appendix A describing the new parameter tab created for the Indian Health Service (IHS) project.</p>
<p>Updated Glossary and Index for Indian Health Service. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/2009</td>
<td><blockquote>
<p>i, iii-iv, 48a- 48b, 56</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*47</p>
</blockquote></td>
<td><blockquote>
<p>Added information for the new <em>Immunizations Documentation by BCMA Nightly Task</em> [PSB PX BCMA2PCE TASK] option that is added to the <em>Bar Code Medication Administration Manager</em> [PSB MGR] menu. PCE added to the glossary.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSB*3*28</p>
</blockquote></td>
<td><blockquote>
<p>Reissue of manual to add new functionality in patch PSB*3*28 including the addition of a new unable to scan option, email notification feature, mode of patient record access and five rights override administration.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

> ii BCMA V. 3.0 Manager’s User Manual January 2009

Introduction 1

Benefits of BCMA V. 3.0 1

Benefits of This Manual 1

Our Target Audience 1

Other Sources of Information 2

Background/Technical Information 2

Training Information 2

This Manual and Related Documentation 2

Conventions Used in This Manual 2

Obtaining On-line Help 4

[Setting Site Parameters for GUI BCMA 5](#setting-site-parameters-for-gui-bcma)

Signing on to GUI BCMA Site Parameters Application 5

Defining and Updating Site Parameters for Your Division 9

Working with the Facility Tab 11

Working with the Parameters Tab 12

Working with the Default Answer Lists Tab 17

Working with the IV Parameters Tab 25

Keyed Entry Timing Parameter 30

Accessing the CHUI BCMA Manager Menu 33

Accessing the CHUI BCMA Manager Menu 33

Checking the Drug IEN Code for Unit Dose Meds 35

Verifying the Drug IEN Code for a Unit Dose Medication 35

Responding to Missing Dose Requests 37

Creating a Follow-up Message for a Missing Dose Request 37

Resetting User Parameters 41

Resetting a User’s Default Parameter Settings 41

Using the Trouble Shoot Med Log 43

Identifying Scanning Problems 43

Running the Unknown Action Status Report 47

Creating a Listing of Unknown Actions 47

Using Immunizations Documentation by BCMA 48a

Validate the Immunizations Documentation by BCMA Nightly Task 48a

Customizing the BCMA GUI Tools Menu 49

Defining the Tools Menu in VistA 49

[Glossary 53](#glossary)

> Learning BCMA Lingo 53

### Appendix A: Setting Site Parameters for Indian Health Service (IHS) 59

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Defining and Setting Site Parameters for IHS 59

> *Working with the Parameters Tab 59*

### Index 61

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/002.png)Setting Site Parameters for GUI BCMA


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Version 3.0](#version-30)
  - [Revision History](#revision-history)
    - [Appendix A: Setting Site Parameters for Indian Health Service (IHS) 59](#appendix-a-setting-site-parameters-for-indian-health-service-ihs-59)
    - [Index 61](#index-61)
- [![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/002.png)Setting Site Parameters for GUI BCMA](#psb-3-42-bcma-version-3-manager-s-user-manual-change-pages002pngsetting-site-parameters-for-gui-bcma)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma)
- [![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/006.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/007.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/008.png)Glossary](#psb-3-42-bcma-version-3-manager-s-user-manual-change-pages006pngpsb-3-42-bcma-version-3-manager-s-user-manual-change-pages007pngpsb-3-42-bcma-version-3-manager-s-user-manual-change-pages008pngglossary)
- [Appendix A: Setting Site Parameters for Indian Health Service (IHS)](#appendix-a-setting-site-parameters-for-indian-health-service-ihs)
    - [A](#a)
    - [B](#b)
    - [C](#c)
    - [D](#d)
    - [E](#e)
    - [F](#f)
    - [G](#g)
    - [I](#i)
    - [K](#k)
- [Index](#index)
    - [L](#l)
    - [M](#m)
    - [N](#n)
    - [O](#o)
    - [P](#p)
    - [S](#s)
    - [T](#t)
- [Index](#index-1)
    - [U](#u)
    - [V](#v)
    - [W](#w)
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Defining and Updating Site Parameters for Your Division (cont.)</strong></p>
<p><strong>TIP:</strong></p>
<p>Modifying the “BCMA On-line” parameter affects <em>all</em> users signing on to your division.</p>
<p>Multi-division sites must disable access to each site.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Working with the Facility Tab</strong></p>
<p>The Facility Tab, on the BCMA Site Parameters Main Screen, provides the following functions:</p>
<p><strong>Facility Information (Read-Only):</strong> This area provides read-only information populated by the INSTITUTION</p>
<p>file (#4).</p>
<p><strong>BCMA On-Line:</strong> This option (check box) under the “BCMA Status for Division” section lets IRM personnel enable or disable all GUI BCMA options. It does not affect CHUI BCMA options.</p>
</blockquote>
<ul>
<li><p><strong>If the “BCMA On-Line” check box is checked,</strong> the system is on-line and all GUI BCMA options are available.</p></li>
<li><p><strong>If the “BCMA On-line” check box is <em>not c</em>hecked,</strong> all users currently logged on to GUI BCMA options will <em>not</em> be affected. However, when a user attempts to log on to the GUI options, the following Error message displays:</p></li>
</ul>
<blockquote>
<p><strong>Example: Error Message When BCMA Not Active for Your Site</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/003.png)</p>
</blockquote>
<ul>
<li><p>If the “BCMA On-Line” check box is checked and you try to take it off-line by deselecting the check box, the following Warning message displays:</p></li>
</ul>
<blockquote>
<p><strong>Example: Warning Message When All BCMA Users Are Being Disabled for Your Division</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/004.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
> Setting Site Parameters for GUI BCMA
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Defining and Updating Site Parameters for Your Division (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Working with the Parameters Tab</strong></p>
<p>You can activate the Parameters Tab by placing the cursor over the Tab, and then clicking once on it. Doing so activates the site parameters for this Tab.</p>
<p><strong>Keyboard Shortcut:</strong> Press <strong>ALT+P</strong> to display the Parameters Tab.</p>
<p>This section describes the fields and check boxes available on the Parameters Tab.</p>
<p><strong>Example: Site Parameters Available Parameters Tab</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/005.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Defining and Updating Site Parameters for Your Division (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Working with the Parameters Tab (cont.)</strong></p>
</blockquote>
<ul>
<li><p><strong>Output Devices Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Missing Dose Request Printer:</strong> This field identifies the default division printer for Missing Dose requests.</p>
</blockquote>
<ul>
<li><p><strong>Mail Groups Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Mail Groups:</strong> This area lists the mail groups that must be created using the <em>VistA Mail Group Edit</em> [XM EDIT MG] option, and by setting the TYPE field to PUBLIC. BCMA</p>
</blockquote>
<ol start="5" type="I">
<li><p>3.0 includes the following mail groups listed below:</p>
<ul>
<li><p><strong>Due List Error:</strong> This field generates an E-mail message for any medication order that BCMA cannot resolve for VDL placement, and sends it to the mail group members. An example might include no administration times entered for a Continuous order.</p></li>
<li><p><strong>Missing Dose Notification:</strong> This field generates an E-mail message for any Missing Dose Request</p></li>
</ul></li>
</ol>
<blockquote>
<p>entered using the BCMA CHUI or GUI menu options. The E-mail is sent to all members of the mail group, specifically Pharmacy, as a “fail safe” even if the designated Missing Dose printer is not functioning.</p>
</blockquote>
<ul>
<li><p><strong>Unknown Actions:</strong> This field generates an E-mail message for any administration with an “Unknown” status while processing administrations to display on the VDL.</p></li>
<li><p><strong>Unable to Scan:</strong> Generates an E-mail message to alert the mail group when a user creates an “Unable to Scan” entry and to assist in researching the reasons for a scanning failure.</p></li>
</ul>
<ul>
<li><p><strong>Reports Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Include Comments:</strong> This check box, when selected, will automatically check the “Include Comments” check box in the Report dialog box as the default setting for the Medication History Report and the Medication Log Report. If this is unchecked, the “Include Comments” check box will be unchecked, by default, in the related Report dialog box. Users can change the check box setting in the Printer dialog box as needed, depending on whether they wish to have the comments for the administration included on the report.</p>
<p><strong>Med Hist Days Back:</strong> This field lets you define the number of days in the past, from the current system date, that the Medication History Report should retrieve data. The allowable entry is 1 to 9999 days.</p>
<p>The default is 30 days.</p>
</blockquote>
<ul>
<li><p>A user can change the date range for the report, in the Report dialog box.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Setting Site Parameters for GUI BCMA

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Defining and Updating Site Parameters for Your Division (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Working with the Parameters Tab (cont.)</strong></p>
</blockquote>
<ul>
<li><p><strong>Bar Code Options Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Default Bar Code Format:</strong> This field lets you select the desired bar code format that you want to produce on the bar code label printer. The following options are available from a drop-down list box: C39, 128, and I25.</p>
<p><strong>Default Bar Code Prefix:</strong> This field lets you specify up to five alphanumeric characters of text that will print as a prefix on a bar code label printed on the bar code label printer.</p>
<p><strong>Using Robot RX:</strong> This check box should be checked only if your site is using the Robot RX product.</p>
</blockquote>
<ul>
<li><p><strong>Five Rights Override Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Unit Dose Administration:</strong> This field lets you control the Unable to Scan verification process by allowing the user to verify the Five Rights of medication administration and proceed with a unit dose administration without entering a Drug IEN or National Drug Code (NDC).</p>
<p><strong>IV Administration:</strong> This field lets you control the Unable to Scan verification process by allowing the user to verify the Five Rights of medication administration and proceed with an IV administration without entering a Drug IEN or National Drug Code (NDC).</p>
</blockquote>
<ul>
<li><p><strong>Administration Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Require ESig To Administer Medication:</strong> This check box requires that users enter the Access/Verify and Electronic Signature Code (ESig) before launching GUI BCMA. Otherwise, the clinician administering medications will be asked for Access/Verify codes only.</p>
<p><strong>Allow Multiple Admins for On-Call:</strong> When checked, your division allows multiple administrations for an On-Call order.</p>
</blockquote>
<ul>
<li><p><strong>Allowable Time Limits In Minutes Area</strong></p></li>
</ul>
<blockquote>
<p><strong>Before and After Scheduled Admin Time:</strong> This parameter defines the allowable medication administration timeframe. In the example provided, the allowable timeframe is set to one hour before through one hour after the scheduled administration time. Each window may be defined up to 240 minutes.</p>
<p><strong>PRN Effectiveness Entry:</strong> This parameter defines the allowable time for the PRN Effectiveness to be assessed, after a PRN medication is given, and before a variance is logged. If a medication administration is outside the allowable time, a variance will be logged when the effectiveness is entered. You can define this window up to 240 minutes.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/006.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/007.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/008.png)Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA Lingo</strong></p>
</blockquote></th>
<th><blockquote>
<p>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/009.png)Example: Alphabetical Listing of BCMA Acronyms and Terms

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/010.png)</p>
<blockquote>
<p><strong>Acronym/Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Active</strong></p>
</blockquote></td>
<td><blockquote>
<p>When a medication has been finished <em>and</em> verified, it becomes “active,” and displays on the VDL under the related Medication Tab. A nurse can then administer the medication to the patient. Under the IV Medication Tab, this information is listed in the Status column.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>BCMA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>B</strong>ar <strong>C</strong>ode <strong>M</strong>edication <strong>A</strong>dministration. A VistA software application used in VAMCs for validating patient information and medications against active medication orders <em>before</em> being administered to a patient.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/011.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>BCMA Clinical Reminders</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/012.png)</p>
</blockquote></td>
<td><blockquote>
<p>A marquee located in the lower, right-hand corner of the VDL that</p>
<p>identifies PRN medication orders needing effectiveness documentation. The setting is based on the “PRN Documentation” site parameter, and applies to current admissions or the site parameter timeframe (whichever is greater). A mouse-over list displays when the pointer is placed over the PRN Effectiveness Activity, or a full list is available by double clicking on the Activity.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CHUI</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Ch</strong>aracter-based <strong>U</strong>ser <strong>I</strong>nterface.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/013.png)</p>
<blockquote>
<p><strong>Client</strong></p>
</blockquote></td>
<td><blockquote>
<p>An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/014.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Clinician</strong></p>
</blockquote></td>
<td><blockquote>
<p>Nursing personnel who administer active medication orders to patients</p>
<p>on a ward. In a VAMC, a number of teams may be assigned to take care of one ward, with specific rooms and beds assigned to each team.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Continuous Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>A medication given continuously to a patient for the life of the order, as defined by the order Start and Stop Date/Time.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CPRS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>C</strong>omputerized <strong>P</strong>atient <strong>R</strong>ecord <strong>S</strong>ystem. A VistA software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/015.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ESig</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>E</strong>lectronic <strong>Sig</strong>nature Code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>FileMan</strong></p>
</blockquote></td>
<td><blockquote>
<p>The VistA database management system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/016.png)</p>
<blockquote>
<p><strong>Finish</strong></p>
</blockquote></td>
<td><blockquote>
<p>The process in which the Pharmacist adds the information necessary to make the order active. For example: dispense drug, and start/stop date.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/017.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/018.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/019.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/020.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/021.png)<u>Glossary</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA Lingo (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/022.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/023.png)Example: Alphabetical Listing of BCMA Acronyms and Terms

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/024.png)</p>
<blockquote>
<p><strong>Acronym/Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Given</strong></p>
</blockquote></td>
<td><blockquote>
<p>When a medication is administered to a patient, it is considered to be “Given” and marked as such (with a “G”) in the Status column of the VDL.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>GUI</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>G</strong>raphical <strong>U</strong>ser <strong>I</strong>nterface.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/025.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HRN</strong></p>
</blockquote></td>
<td><blockquote>
<p>Health Record Number – 6 digit patient identifier in IHS/Tribal facilities</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>IEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>I</strong>nternal <strong>E</strong>ntry <strong>N</strong>umber. The internal entry drug number entered by Pharmacy personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>IHS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Indian Health Service</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/026.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Internal Entry Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>Also called “IEN,” the internal entry drug number entered by Pharmacy</p>
<p>personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>IV</strong></p>
</blockquote></td>
<td><blockquote>
<p>A medication given intravenously (within a vein) to a patient from an IV Bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/027.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LIMITED ACCESS BCMA</strong></p>
</blockquote></td>
<td><blockquote>
<p>A mode in which BCMA can be accessed that provides medication</p>
<p>administering users the ability to access patient records for non- medication administration documentation, review and reporting purposes without being at the patient’s bedside.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>MAH</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/028.png)</p>
</blockquote></td>
<td><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/029.png)</p>
<blockquote>
<p><strong>M</strong>edication <strong>A</strong>dministration <strong>H</strong>istory. A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MAR</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>M</strong>edication <strong>A</strong>dministration <strong>R</strong>ecord. The traditional, handwritten record</p>
<p>used for noting when a patient received a medication. BCMA replaces this record with an MAH.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/030.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Medication Administration</strong></p>
<p><strong>History Report</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>M</strong>edication <strong>A</strong>dministration <strong>H</strong>istory. A patient report that lists a clinician’s</p>
<p>name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/031.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/032.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/033.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/034.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/035.png)![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/036.png)<u>Glossary</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Learning BCMA Lingo (cont.)</strong></p>
</blockquote></th>
<th><blockquote>
<p>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/037.png)Example: Alphabetical Listing of BCMA Acronyms and Terms

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/038.png)</p>
<blockquote>
<p><strong>Acronym/Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Refused</strong></p>
</blockquote></td>
<td><blockquote>
<p>The status for an IV bag or Unit Dose to indicate that the patient refused to take the dose.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/039.png)</p>
<blockquote>
<p><strong>RPMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Resource and Patient Management System – health information system for IHS, analogous to VistA</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/040.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Schedule Type</strong></p>
</blockquote></td>
<td><blockquote>
<p>Identifies the type of schedule (i.e., Continuous, PRN, On-Call, and</p>
<p>One-Time) for the medication being administered to a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Security Keys</strong></p>
</blockquote></td>
<td><blockquote>
<p>Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/041.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Solution</strong></p>
</blockquote></td>
<td><blockquote>
<p>A homogeneous mixture of two or more substances. For IVs, these</p>
<p>would be liquids.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Start Date/Time</strong></p>
</blockquote></td>
<td><p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/042.png)</p>
<blockquote>
<p>The date and time that a medication is scheduled for administration to a patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>STAT Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>A medication order given immediately to a patient, entered as a One- Time order by providers and pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/043.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Stop Date/Time</strong></p>
</blockquote></td>
<td><blockquote>
<p>The date and time that a medication order will expire, and should no</p>
<p>longer be administered to a patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Strength</strong></p>
</blockquote></td>
<td><blockquote>
<p>The degree of concentration, distillation, or saturation of a medication.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Unit Dose</strong></p>
</blockquote></td>
<td><blockquote>
<p>A medication given to a patient, such as tablets or capsules.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/044.png)</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VDL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line “list” used by clinicians when administering</p>
<p>active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Verify</strong></p>
</blockquote></td>
<td><blockquote>
<p>When a nurse or a Pharmacist confirms that a medication order is accurate and complete, according to the information supplied by the Provider.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Virtual Due List</strong></p>
</blockquote></td>
<td><blockquote>
<p>Also called “VDL,” an on-line list used by clinicians when administering active medication orders to a patient. This is the Main Screen in BCMA V. 3.0.</p>
</blockquote>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/045.png)</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VistA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/046.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix A: Setting Site Parameters for Indian Health Service (IHS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Defining and Setting Site Parameters for IHS</strong></p>
</blockquote></th>
<th><blockquote>
<p>The Indian Health Service (IHS) project requires the addition of a new parameter to the BCMA Parameters application. The IHS user- specified parameter entries are stored at the Division level and override corresponding System level values.</p>
<p><strong>Working with the Parameters Tab</strong></p>
<p>If the operating environment is Resource and Patient Management System (RPMS), the tab entitled “IHS” is added to the parameters application.</p>
<p>You can activate the IHS Tab by placing the cursor over the Tab and clicking once on it or by selecting Alt-H to access it directly. Doing so activates the site parameters for this Tab.</p>
<p>This section describes the field available on the IHS Tab.</p>
<p><strong>Example: Site Parameters Available IHS Tab</strong></p>
<p>![](psb-3-42-bcma-version-3-manager-s-user-manual-change-pages/047.png)</p>
<p><strong>IHS Patient ID Label:</strong> This text entry field allows you to enter a patient ID textual label of up to 5 characters if the operating environment is RPMS. The contents of this field are displayed throughout the BCMA GUI forms and reports.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Index

### A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Accessing

> Bar Code Medication Administration Manager Menu, 31

> CHUI BCMA Manager Menu Screen, 31 Administration Area, Parameters Tab, 14

### B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Background, technical information, 2

> Bar Code Medication Administration Manager Menu Screen, 31

> Bar Code Options Area, Parameters Tab, 14 BCMA V. 3.0

> Benefits, 1

> Clinical Reminders, 16

> Idle Timeout, 15

> Lingo, 45-49

> Site Parameters Main Screen with Facility Tab Selected, 10

> Site Parameters Opening Screen, 8 Target Audience, 1

> Benefits of This Manual, 1

### C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Checking Drug IEN Code for Unit Dose Medications, 33-34

> CHUI BCMA

> Manager Menu Screen, 31 On-line Help, 4

> Connect to Selection Dialog Box, 5 Conventions Used in This Manual

> Keyboard Responses, 2

> Menu Options, 3

> Mouse Responses, 2

> Notes, 3

> Screen Captures, 3

> Tips, 3

> User Responses, 3 Creating

> Default Answer List for Injection Sites, 24 Default Answer List for Reason Medication

> Given PRN, 19-21

> Default Answer List for Reason Medication Held, 22

> Default Answer List for Reason Medication Refused, 23

> Follow-up Message for a Missing Dose Request, 35-37

### D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Default

> Answer Lists Tab, 17-24

> Answer Lists Tab Selected and List Names Provided Screen, 17

> Parameter Settings, Resetting for a User, 39-40

> Defining and Setting Site Parameters for IHS, 59 Defining and Updating Site Parameters for

> Your Division, 9-29

> Division Selection Dialog Box, 9 Drug File Inquiry Screen, 33

> Drug IEN Code for Unit Dose Medications, Verifying, 33-34

### E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enable CPRS Med Order Button, Selecting, 16 Error Message When BCMA Not Active for

> Your Site, 11

### F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Facility Tab, 11

> Five Rights Override Parameters, 14 Follow-up Message

> Creating for a Missing Dose Request, 35-37

### G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> GUI BCMA Site Parameters Application Desktop Icon, 5

### I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Identifying Scanning Problems Using the Trouble shoot Med Log, 41-43

> Include Comments Parameter, 12-13 Information Message When Prompts Default

> Setting Changed, 29 Introducing

> BCMA V. 3.0, 1

> This Manual, 3 IV Parameters Tab

> IV Type Area, 27 Location Area, 26

> Prompts Area, 28-29

### K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Keyboard Response Conventions, 2 Keyed Entry Timing Parameter, 30

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Location Area, IV Parameters Tab, 26

### M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mail Groups Area, Parameters Tab, 13 Med Hist Days Back Parameter, 12-13 Med Log
> Identifying Scanning Problems, 41-43 Trouble Shooter Screens, 41-42
> Menu Option Conventions, 3
> Misc Options Area, Parameters Tab, 15 Missing Dose
> Creating a Followup Message, 35-37 Request Entry Screen, 36
> Request Selection Screen, 35 Mouse Response Conventions, 2

### N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notes Conventions, 3

### O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Online Help, CHUI, 4
> Order Validation Screen, Trouble Shoot Med Log, 43
> Other Sources of Information, 2
> Output Devices Area, Parameters Tab, 12-13

### P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Parameters Tab Administration Area, 14 Bar Code Options Area, 14 Mail Groups Area, 13 Misc Options Area, 15-16
> Output Devices Area, 12-13 Reports Area, 12-13
> Virtual Due List Setup Area, 15 Patient Transfer Notification, 15
> Pharmacy Reasons Needed Selection Table, 37 PRN Documentation, 16
> Prompts Area, IV Parameters Tab, 28-29 Prompts Drop-Down List Box for Additive
> Field, 28
> PSB CPRS MED BUTTON Security key, 16 PSB MANAGER Security Key, 1
> PSB Unable to Scan Security Key, 56
> R
> Related Documentation, 2
> Reports Area, Parameters Tab, 12-13
> Reset User Parameters Sequence Screen, 39 Resetting a User’s Default Parameter Settings,
> 39-40
> Responding to Missing Dose Requests, 35-37 Results of Drug File Inquiry Screen, 34

### S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Screen Capture Conventions, 3 Security Keys
> PSB CPRS MED BUTTON, 16 PSB MANAGER, 1
> Select Division Dialog Box, 7
> Selecting a Default Answer Lists Name Screen, 18
> Setting Site Parameters for GUI BCMA V. 3.0, 5
> Signing on to GUI BCMA Site Parameters Application, 5-8
> For VAMCs with Multiple Divisions, 7 Site Parameters
> Available Using Parameters Tab, 12-15 Available When IV Parameters Tab Selected
> Screen, 25
> Suggested Default Answer Lists For Injection Sites, 24
> For Reason Medication Given PRN, 20-21 For Reason Medication Held, 22
> For Reason Medication Refused, 23

### T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Tabs
> Facility, 11
> Default Answer Lists, 17-24 IV Parameters, 25-29
> Parameters, 12-16
> Target Audience for This Manual, 1 This Manual
> Benefits of, 1
> Conventions Used, 2-3
> Other Sources of Information, 2 Related Documentation, 2
> Target Audience, 1
> Tips Conventions, 3
> Trouble Shoot Med Log, Using, 41-43
> Type Drop-Down List Box for IV Type Area, 27

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unable to Scan Mail Group, 13 Unit Dose Medications
> Verifying the Drug IEN Code for, 33 Updating and Defining Site Parameters for
> Your Division, 9-29
> User Response Conventions, 3
> Using the Trouble Shoot Med Log, 41-43

### V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verifying the Drug IEN Code for Unit Dose Medications, 33-34
> Virtual Due List Setup Area, Parameters Tab, 15 VistA Sign-on Dialog Box, 5

### W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ward Drop-Down List Box for Location Area, 26
> Warning Message
> About Updates to Parameters Being Immediate, 8
> That Fields in Inpatient Medications V. 5.0 Changed, 29
> When All BCMA Users Are Being Disabled from Your Division, 11
> Working with
> Default Answer Lists Tab, 17-24 Facility Tab, 11
> IV Parameters Tab, 25-29 Parameters Tab, 12-16


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSB*3*47 BCMA Version 3 Manager's User Manual Change Pages

### ![](psb-3-47-bcma-version-3-manager-s-user-manual-change-pages/002.png)![](psb-3-47-bcma-version-3-manager-s-user-manual-change-pages/003.png)Example: Alphabetical Listing of BCMA Acronyms and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
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
<td><strong>Medication Route</strong></td>
<td><blockquote>
<p>Also called “Route” or “Med Route,” the method by which a patient receives medication (i.e., PO, IV, IM, ID, SQ, and SC). Each VAMC determines routes and associated abbreviations, which cannot exceed five characters in length. Otherwise they will <em>not</em> fit on bar code labels and the MAH.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Medication Tab</strong></td>
<td><blockquote>
<p>Used to separate and view a type of active medication order (i.e., Unit Dose IV Push, IV Piggyback, and large-volume IVs) that needs to be administered to a patient. The Tab under which an order displays depends on how it was entered. The “alert light” on a Tab turns <strong>GREEN</strong> <em>only</em> when a medication order exists for the Schedule Type selected within the respective start/stop date and time selected on the BCMA VDL. If grayed out, then none exist.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Missing Dose</strong></td>
<td><blockquote>
<p>A medication considered “Missing.” BCMA automatically marks this order type (with an “M”) in the Status column of the VDL after you submit a Missing Dose Request to the Pharmacy. If an IV bag displayed in the IV Bag Chronology display area of the VDL is <em>not</em> available for administration, you may mark the IV bag as a “Missing Dose” using the Missing Dose button or by right clicking the IV bag and selecting the Missing Dose command in the Right Click drop-down menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>National Drug Code</strong></td>
<td><blockquote>
<p>Also called “NDC,” the number assigned by a manufacturer to each item/medication administered to a patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>NDC</strong></td>
<td><blockquote>
<p><strong>N</strong>ational <strong>D</strong>rug <strong>C</strong>ode. The number assigned by a manufacturer to each item/medication administered to a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>On-Call Order</strong></td>
<td><blockquote>
<p>A specific order or action dependent upon another order or action taking place <em>before</em> it is carried out. For example, “Cefazolin 1gm IVPB On Call to Operating Room.” Since it may be unknown when the patient will be taken to the operating room, the administration of the On-Call Cefazolin is dependent upon that event.</p>
</blockquote></td>
</tr>
</tbody>
</table>
January 2009 BCMA V. 3.0 Manager’s User Manual 55

### ![](psb-3-47-bcma-version-3-manager-s-user-manual-change-pages/004.png)![](psb-3-47-bcma-version-3-manager-s-user-manual-change-pages/005.png)Example: Alphabetical Listing of BCMA Acronyms and Terms

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
<td><strong>One-Time Order</strong></td>
<td><blockquote>
<p>A medication order given one time to a patient such as a STAT or NOW order. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time or until it is Given.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Orderable Item</strong></td>
<td><blockquote>
<p>A drug whose name does NOT have the strength associated with it (e.g., Acetaminophen 325 mg). The name with a strength is called the “Dispensed Drug Name.”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Patient Transfer Notification</strong></td>
<td><blockquote>
<p>A message that displays when a patient’s record is opened or the Unit Dose or IVP/IVPB Medication Tab is viewed for the first time. It indicates that the patient has had a movement type (usually a transfer) within the site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PCE</strong></td>
<td><blockquote>
<p><strong>P</strong>atient <strong>C</strong>are <strong>E</strong>ncounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td><blockquote>
<p>An order entered by a provider through CPRS without Pharmacy personnel verifying the order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PRN Effectiveness List Report</strong></td>
<td><blockquote>
<p>A report that lists PRN medications administered to a patient that needs Effectiveness comments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PRN Order</strong></td>
<td><blockquote>
<p>The Latin abbreviation for <strong>P</strong>ro <strong>R</strong>e <strong>N</strong>ata. A medication dosage given to a patient on an “as needed” basis.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Provider</strong></td>
<td><blockquote>
<p>Another name for the “Physician” involved in the prescription of a medication (Unit Dose or IV) to a patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSB CPRS MED BUTTON</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and medication orders using the CPRS Med Order Button on the BCMA VDL.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSB INSTRUCTOR</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSB MANAGER</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>PSB STUDENT</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options with BCMA V. 3.0. This key requires that a nursing instructor sign on to BCMA V. 3.0.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSB UNABLE TO SCAN</strong></td>
<td><blockquote>
<p>The name of the security “key” that must be assigned to allow the user to run the Unable to Scan Detailed and Summary reports.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 56 BCMA V. 3.0 Manager’s User Manual October 2009 PSB\*3\*47
