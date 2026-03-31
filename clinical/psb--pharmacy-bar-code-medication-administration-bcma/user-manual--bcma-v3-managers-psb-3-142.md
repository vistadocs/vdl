---
title: BCMA Version 3 Manager's User Manual (PSB*3*142)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Manager's  (PSB*3*142)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 13
description: "<table> <colgroup> <col style=\\"width: 30%\\" /> <col style=\\"width: 69%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h2 id=\\"benefits-of-bcma-v.-3.0\\">![](bcma-version-3-manager-s-user-manual-psb-3-142/002.png)Benefits of<br /> BCMA V. 3.0 </h2></td> <td><p>The Bar Code Medication Administration (BCMA) "
audience: 
keywords: 
  - strong
  - bcma
  - parameters
  - table
  - site
  - class
  - cont
  - style
  - width
  - contents
page_count: 0
word_count: 19343
section_count: 1
table_count: 17
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_man_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_man_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

![](bcma-version-3-manager-s-user-manual-psb-3-142/001.png)

BAR CODE MEDICATION ADMINISTRATION (BCMA)

MANAGER’S USER MANUAL

February 2004

(Revised August 2023)

# Department of Veterans Affairs


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Product Development](#product-development)
- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Introduction](#introduction-1)
- [Introduction](#introduction-2)
- [Introduction](#introduction-3)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-1)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-2)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-3)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-4)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-5)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-6)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-7)
- [# Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-8)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-9)
- [# Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-10)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-11)
- [# Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-12)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-13)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-14)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-15)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-16)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-17)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-18)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-19)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-20)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-21)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-22)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-23)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-24)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-25)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-26)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-27)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-28)
- [Setting Site Parameters for GUI BCMA](#setting-site-parameters-for-gui-bcma-29)
- [Accessing the CHUI BCMA Manager Menu](#accessing-the-chui-bcma-manager-menu)
- [Checking the Drug IEN Code for Unit Dose Meds](#checking-the-drug-ien-code-for-unit-dose-meds)
- [Checking the Drug IEN Code for Unit Dose Meds](#checking-the-drug-ien-code-for-unit-dose-meds-1)
- [Responding to Missing Dose Requests](#responding-to-missing-dose-requests)
- [Responding to Missing Dose Requests](#responding-to-missing-dose-requests-1)
- [Responding to Missing Dose Requests](#responding-to-missing-dose-requests-2)
- [Resetting User Parameters](#resetting-user-parameters)
- [Resetting User Parameters](#resetting-user-parameters-1)
- [Using the Trouble Shoot Med Log](#using-the-trouble-shoot-med-log)
- [Using the Trouble Shoot Med Log](#using-the-trouble-shoot-med-log-1)
- [Using the Trouble Shoot Med Log](#using-the-trouble-shoot-med-log-2)
- [Running the Unknown Action Status Report](#running-the-unknown-action-status-report)
- [Running the Unknown Action Status Report](#running-the-unknown-action-status-report-1)
- [Using Immunizations Documentation by BCMA](#using-immunizations-documentation-by-bcma)
- [Using Immunizations Documentation by BCMA](#using-immunizations-documentation-by-bcma-1)
- [Customizing the BCMA GUI Tools Menu](#customizing-the-bcma-gui-tools-menu)
- [Customizing the BCMA GUI Tools Menu](#customizing-the-bcma-gui-tools-menu-1)
- [Customizing the BCMA GUI Tools Menu](#customizing-the-bcma-gui-tools-menu-2)
- [Glossary](#glossary)
- [Glossary](#glossary-1)
- [Glossary](#glossary-2)
- [Glossary](#glossary-3)
- [Glossary](#glossary-4)
- [Appendix A: Setting Site Parameters for Indian Health Service (IHS)](#appendix-a-setting-site-parameters-for-indian-health-service-ihs)
- [Index](#index)
- [Index](#index-1)
- [Index](#index-2)

# Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revised Pages</td>
<td>Patch Number</td>
<td>Description</td>
</tr>
<tr class="even">
<td>08/2023</td>
<td><a href="#revision_historyi">i</a>, <a href="#pg59_P142"><u>59</u></a></td>
<td>PSB*3*142</td>
<td>The Immunizations Documentation by BCMA application is sunset.</td>
</tr>
<tr class="odd">
<td>12/2018<span id="revision_historyi2" class="anchor"></span></td>
<td><a href="#revision_historyi2">i</a>, <a href="#p5">5-7</a></td>
<td>PSB*3*96</td>
<td><p>Two-factor authentication (2FA).</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>06/2018</td>
<td><a href="#psb_3_100"><u>46</u></a></td>
<td>PSB*3*100</td>
<td><p>Added note on selecting divisions at a multidivisional site for Missing Dose Follow-up.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td><span id="revision_historyi" class="anchor"></span>11/2016</td>
<td><p><a href="#revision_historyi">i</a>-<a href="#tociii">iii</a></p>
<p><a href="#p42_12">12</a></p>
<p><a href="#mail-groups-area">13a</a></p>
<p><a href="#p16_Dermal">16</a></p>
<p><a href="#default_answer_listtab">17</a>-<a href="#default_answer_listname18">18</a></p>
<p><a href="#documenting-and-displaying-anatomic-location-for-medication-administrations">24</a>-<a href="#list_of_recommendedbodysites33">33</a></p></td>
<td>PSB*3*83</td>
<td><p>Updated Revision History and Table of Contents.</p>
<p>Updated BCMA Site Parameter screenshot.</p>
<p>Changed verbiage from BCMA CHUI to BCMA GUI for Missing Dose notification.</p>
<p>Added explanation of Dermal Site History Max Days.</p>
<p>Updated Default Answer List Tab screen. Updated Selecting Default Answer List Name screen</p>
<p>Added Documenting and Displaying Anatomic Location for Medication Administrations, XPAR EDIT BY TEMPLATE with new PSB DERMAL SITE MAX DAYS site parameter, and Body Sites List information.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>12/2013</td>
<td>i-ii, 2, 12, 13, 13a-13b, 14a</td>
<td>PSB*3*70</td>
<td><p>Updated BCRO address link.</p>
<p>Added site parameter to allow sites to be able to assign a <strong>specific</strong> clinic order missing dose request printer to a specific clinic, so that all missing dose requests for that clinic will print at that defined clinic location. Sites will also be able to assign a <strong>division</strong> clinic order missing dose request printer, so that all clinic order missing dose requests in the division will print on that printer.</p>
<p>Renamed “Missing Dose Request Printer” parameter in BCMA Parameters to “Inpatient Missing Dose Request Printer.”</p>
<p>Parameters for Allowable Time Limits ignored for Clinic Orders.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>09/2012</td>
<td>i, 12, 16</td>
<td>PSB*3*68</td>
<td><p>Added site parameter to allow sites to select the maximum number of hours that new BCMA site parameter, Injection Site History, will display on the VDL during the administration of injectable medications.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>01/2012</td>
<td>i, 8, 12, 14, 14a-14b</td>
<td>PSB*3*58</td>
<td><p>Added site parameter to allow sites to administer non-nurse verified medication orders with no warnings displayed, to display a warning before administering non-nurse verified medication orders, or to prohibit administration of non-nurse verified medication orders.</p>
<p>PRN Effectiveness Entry Parameter maximum increased from 240 to 960 minutes.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>01/2011</td>
<td>i, iii-iv, 12-13, 54, 57, 59-64</td>
<td>PSB*3*42</td>
<td><p>Removed field Scratch HFS Directory from the Parameters Tab, and replaced corresponding Site Parameters screen capture.</p>
<p>Added Appendix A describing the new parameter tab created for the Indian Health Service (IHS) project.</p>
<p>Updated Glossary and Index for Indian Health Service.</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revised Pages</td>
<td>Patch Number</td>
<td>Description</td>
</tr>
<tr class="even">
<td>10/2009</td>
<td>i, iii-iv, 48a-48b, 56</td>
<td>PSB*3*47</td>
<td><p>Added information for the new <em>Immunizations Documentation by BCMA Nightly Task</em> [PSB PX BCMA2PCE TASK] option that is added to the <em>Bar Code Medication Administration Manager</em> [PSB MGR] menu. PCE added to the glossary.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td>All</td>
<td>PSB*3*28</td>
<td><p>Reissue of manual to add new functionality in patch PSB*3*28 including the addition of a new unable to scan option, email notification feature, mode of patient record access and five rights override administration.</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

Table of Contents

Introduction [1](#introduction)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="benefits-of-bcma-v.-3.0">![](bcma-version-3-manager-s-user-manual-psb-3-142/002.png)Benefits of<br />
BCMA V. 3.0 </h2></td>
<td><p>The Bar Code Medication Administration (BCMA) V. 3.0 software includes routines, files, enhancements, maintenance fixes, and Phase Release changes for BCMA V. 2.0. The enhancements are a direct result of feedback from the BCMA Workgroup and our many end users.</p>
<p>BCMA V. 3.0 software is designed to improve the accuracy of the medication administration process. By automating this process, Department of Veterans Affairs Medical Centers (VAMCS) can expect enhanced patient safety and patient care.</p>
<p>The electronic information that BCMA V. 3.0 provides clinicians improves their ability to administer medications safely and effectively to patients on wards during their medication passes. It also helps to improve the daily communication that occurs between Nursing and Pharmacy staffs.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="benefits-of-this-manual">![](bcma-version-3-manager-s-user-manual-psb-3-142/003.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/004.png)Benefits of This Manual</h2></td>
<td><p>This manual provides detailed instructions for setting the Graphical User Interface (GUI) BCMA site parameters; using the BCMA Character-based User Interface (CHUI) Manager Option; checking the Drug Internal Entry Number (IEN) Code on Unit Dose medications; entering a reason for a Missing Dose Request; resetting user parameters; and using the Trouble Shoot Med Log.</p>
<h3 id="our-target-audience">Our Target Audience</h3>
<p>We have developed this manual for individuals within the following groups, who are responsible for managing the site parameter settings for your VAMC.</p>
<p>Information Resources Management (IRM)</p>
<p>Clinical Applications Coordinator (CAC) — called Applications Package Coordinator (ADPAC) at some VAMCs</p>
<p>BCMA Coordinators</p></td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="other-sources-of-information">![](bcma-version-3-manager-s-user-manual-psb-3-142/005.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/006.png)Other Sources of Information</h2></td>
<td><p>Refer to the Web sites listed below when you want to receive more background and technical information about BCMA V. 3.0, and to download this manual and related documentation.</p>
<h3 id="backgroundtechnical-information">Background/Technical Information</h3>
<p>To access the BCMA Bar Code Resource Office (BCRO) home page, access the following link from your Intranet: REDACTED</p>
<h3 id="training-information">Training Information</h3>
<p>To access BCMA training modules on the National Training and Education Office web site, access the following link from your Intranet: REDACTED</p>
<h3 id="this-manual-and-related-documentation">This Manual and Related Documentation</h3>
<p>To access this manual, and those listed below, from the VHA Software Document Library, access the following link from your Intranet:<br />
<a href="http://www.va.gov/vdl/application.asp?appid=84">http://www.va.gov/vdl/application.asp?appid=84</a></p>
<p>Release Notes</p>
<p>Installation Guide</p>
<p>Technical Manual/Security Guide</p>
<p>BCMA GUI User Manual</p>
<p>Nursing CHUI User Manual</p>
<p>Pharmacy CHUI User Manual</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="conventions-used-in-this-manual">![](bcma-version-3-manager-s-user-manual-psb-3-142/007.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/008.png)Conventions Used in This Manual</h2></td>
<td><p>Throughout this manual, you will find a variety of elements designed to help you work more efficiently with BCMA 3.0. They include the many conventions listed below.</p>
<p><strong>Keyboard Responses:</strong> Keys provided in <strong>boldface</strong>, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see <strong>ENTER</strong> or &lt;<strong>Enter</strong>&gt; in the copy, press this key on your keyboard.</p>
<ul>
<li><p><strong>Within the GUI Steps:</strong> Use the <strong><span class="smallcaps">arrow</span></strong> keys to Select your division name, and then press <span class="smallcaps"><strong>enter</strong>.</span></p></li>
<li><p><strong>Within the CHUI Steps</strong>: At the “Select User to Reset:” prompt, enter the user’s name and then press <strong>&lt;Enter&gt;</strong>.</p></li>
</ul>
<p><strong>Mouse Responses:</strong> Buttons provided in <strong>boldface</strong>, within the steps, indicate what you should select on your computer screen using the mouse. For example, when you see <strong>NEXT</strong>, <strong>YES/NO</strong>, or <strong>OK</strong> in the steps, click or select the appropriate button on your computer screen.</p></td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="conventions-used-in-this-manual-cont." class="H2-Continued">Conventions Used in This Manual (cont.)</h2></td>
<td><p><strong>User Responses:</strong> Information presented in <strong>boldface</strong>, within the steps, indicate what you should “type” (enter) onto your computer screen. For example, At the “Select OPTION NAME:” prompt, type <strong>XPD MAIN</strong> and then press <strong>&lt;Enter&gt;</strong>.</p>
<p><strong>Screen Captures:</strong> Provide “shaded” examples of what<br />
you will see on your computer screen, and possible user responses.</p>
<p><strong>Notes:</strong> Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our Staff, Developers, and Testers.</p>
<p><strong>Tips:</strong> Located in the left margin, these helpful hints are designed to help you work more efficiently with BCMA<br />
V. 3.0.</p>
<p><strong>Menu Options:</strong> When provided in italics, identifies a menu option. When provided in <strong>boldface</strong>, ALL CAPS, identifies the letters that you should type onto your computer screen, before pressing &lt;<strong>Enter</strong>&gt;. The system then goes directly to the menu option or field. (<strong>Note</strong>: The letters do not have to be entered as capital letters, even though they are provided within the steps in this format.) See the example provided below.</p>
<ul>
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>T</strong>, and then press <strong>&lt;Enter&gt;</strong> to access the <em>Trouble Shoot Med Log</em> [PSB MED LOG TROUBLE SHOOTER] option.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="obtaining-on-line-help">Obtaining On-line Help</h2></td>
<td><p>On-line help is designed right into the CHUI version of BCMA V. 3.0, making it quick and easy for you to get answers to your questions. Here’s how to access help in CHUI BCMA:</p>
<p><strong>CHUI BCMA:</strong> Lets you enter up to three question marks at any prompt to receive on-line help.</p>
<ul>
<li><p><strong>One Question Mark:</strong> Provides a brief statement related to the prompt.</p></li>
<li><p><strong>Two Question Marks:</strong> Displays more detailed information about the prompt, plus any hidden actions.</p></li>
<li><p><strong>Three Question Marks:</strong> Provides more detailed help, including a list of possible answers.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](bcma-version-3-manager-s-user-manual-psb-3-142/009.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/010.png)Signing on to<br />
GUI BCMA Site Parameters Application</td>
<td><p>Use this section to sign on (log on) to the GUI BCMA Site Parameters application.</p>
<p><strong>Note:</strong> The initial process of signing on to the GUI BCMA Site Parameters application is the same for each site.</p>
<p>To sign on to GUI BCMA Site Parameters application</p>
<ol type="1">
<li><p>Double-click on the BCMA icon on your desktop. The Connect To Selection dialog box may display. This will depend on your system set-up.</p></li>
</ol>
<p>Example: Connect To Selection Dialog Box</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/011.png)</p>
<ol start="2" type="1">
<li><p>Select the Server connection for your site, and then click OK.</p></li>
<li><p><span id="p5" class="anchor"></span>To sign in using two-factor authentication (2FA) you will select the appropriate PIV credentials.</p></li>
</ol>
<p>Example: Select PIV Credentials</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/012.png)</p>
<ol start="4" type="1">
<li><p>Enter your PIV PIN.</p></li>
</ol>
<p>Example: Enter PIV PIN</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/013.png)</p>
<ol start="5" type="1">
<li><p>If you are prompted for your Access and Verify Codes, enter those here.</p></li>
</ol>
<p>Example: VistA Sign-on Dialog Box</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/014.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="signing-on-to-gui-bcma-site-parameters-application-cont." class="H2-Continued">Signing on to<br />
GUI BCMA Site ![](bcma-version-3-manager-s-user-manual-psb-3-142/015.png)Parameters Application (cont.) ![](bcma-version-3-manager-s-user-manual-psb-3-142/016.png)</h2></td>
<td><p>To sign on to GUI BCMA Site Parameters application (cont.)</p>
<ol start="6" type="1">
<li><p>In the Access Code field, type your Access Code, and then press <span class="smallcaps"><strong>tab</strong>.</span></p></li>
</ol>
<p>If the “blinking” cursor does not display in this field, click once in the field to activate it.</p>
<p><strong>Keyboard Shortcut:</strong> Press <strong><span class="smallcaps">tab</span></strong> to move among the fields and buttons on the dialog box.</p>
<ol start="7" type="1">
<li><p>In the Verify Code field, type your Verify Code, and then<br />
click <span class="smallcaps"><strong>ok</strong>.</span> A Warning message displays.</p></li>
</ol>
<p>If the “blinking” cursor does not display in this field, click once in the field to activate it.</p>
<p><strong>Keyboard Shortcut:</strong> Press <strong><span class="smallcaps">enter</span></strong> after typing the codes to display a Warning message.</p></td>
</tr>
<tr class="even">
<td><h2 id="section" class="H2-Continued"></h2></td>
<td></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="signing-on-to-gui-bcma-site-parameters-application-cont.-1" class="H2-Continued">Signing on to<br />
GUI BCMA Site Parameters Application (cont.)</h2></td>
<td><h3 id="if-your-vamc-has-multiple-divisions">If Your VAMC Has Multiple Divisions</h3>
<p>The Select Division dialog box, provided below, displays if your VAMC has multiple divisions.</p>
<p>To Select a Division:</p>
<ol type="1">
<li><p>Select a division that corresponds to your VAMC, and then click <strong><span class="smallcaps">ok</span></strong>.</p></li>
</ol>
<p><strong>Keyboard Shortcut:</strong> Use the <strong><span class="smallcaps">arrow</span></strong> keys to Select your division name, and then press <span class="smallcaps"><strong>enter</strong>.</span></p>
<p>Example: Select Division Dialog Box</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/017.png)</p>
<ol start="2" type="1">
<li><p>Continue with the sign-on process.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="signing-on-to-gui-bcma-site-parameters-application-cont.-2" class="H2-Continued">Signing on to<br />
GUI BCMA Site Parameters Application (cont.)</h2></td>
<td><p>To sign on to GUI BCMA Site Parameters application (cont.)</p>
<p>Example: Warning Message About Updates to Parameters Being Immediate</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/018.png)</p>
<ol start="8" type="1">
<li><p>Review the Warning message, and then click <strong><span class="smallcaps">ok</span></strong>. The BCMA Site Parameters Opening Screen displays.</p></li>
</ol>
<p>Example: BCMA Site Parameters Opening Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/019.png)</p>
<p><strong>Note:</strong> The BCMA Site Parameters Opening Screen will display the Facility Division Number, as shown above, upon opening.</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division">Defining and Updating Site Parameters for Your Division</h2></td>
<td><p>You are now ready to update existing GUI BCMA site parameters for your VAMC.</p>
<p>To define and update site parameters for your division</p>
<ol type="1">
<li><p>Select the Open command from the File menu. The Division Selection dialog box displays.</p></li>
</ol>
<p><strong>Keyboard Shortcut:</strong> Press <span class="smallcaps"><strong>alt+f</strong></span> to display the File menu, and then press <strong><span class="smallcaps">o</span></strong> to select the Open command.</p>
<p>Example: Division Selection Dialog Box</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/020.png)</p>
<ol start="2" type="1">
<li><p>Enter the <strong>number of the division</strong> that corresponds to your VAMC, and then click <strong><span class="smallcaps">ok</span></strong>. The BCMA Site Parameters Main Screen displays, with the Facility Tab selected.</p></li>
</ol>
<p><strong>Keyboard Shortcut:</strong> Press <strong><span class="smallcaps">tab</span></strong> to activate the <strong><span class="smallcaps">ok</span></strong> button, and then press <strong><span class="smallcaps">enter</span></strong> to continue with the defining and updating process.</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont." class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><p>To define and update site parameters for your division (cont.)</p>
<p>Example: BCMA Site Parameters Main Screen with Facility Tab Selected</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/021.png)</p>
<ol start="3" type="1">
<li><p>Review the sections that follow to acquaint yourself with each Tab and the options available to your VAMC.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-1" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/022.png)</h2></td>
<td><h3 id="working-with-the-facility-tab">Working with the Facility Tab</h3>
<p>The Facility Tab, on the BCMA Site Parameters Main Screen, provides the following functions:</p>
<p><strong>Facility Information (Read-Only):</strong> This area provides read-only information populated by the INSTITUTION<br />
file (#4).</p>
<p><strong>BCMA On-Line:</strong> This option (check box) under the “BCMA Status for Division” section lets IRM personnel enable or disable all GUI BCMA options. It does not affect CHUI BCMA options.</p>
<ul>
<li><p><strong>If the “BCMA On-Line” check box is checked,</strong> the system is on-line and all GUI BCMA options are available.</p></li>
<li><p><strong>If the “BCMA On-line” check box is <em>not c</em>hecked,</strong> all users currently logged on to GUI BCMA options will <em>not</em> be affected. However, when a user attempts to log on to the GUI options, the following Error message displays:</p></li>
</ul>
<p>Example: Error Message When BCMA</p>
<p>Not Active for Your Site</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/023.png)</p>
<ul>
<li><p>If the “BCMA On-Line” check box is checked and you try to take it off-line by deselecting the check box, the following Warning message displays:</p></li>
</ul>
<p>Example: Warning Message When All BCMA Users<br />
Are Being Disabled for Your Division</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/024.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-2" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab">Working with the Parameters Tab</h3>
<p>You can activate the Parameters Tab by placing the cursor over the Tab, and then clicking once on it. Doing so activates the site parameters for this Tab.</p>
<p><strong>Keyboard Shortcut:</strong> Press <span class="smallcaps"><strong>alt+P</strong></span> to display the Parameters Tab.</p>
<p>This section describes the fields and check boxes available on the Parameters Tab.</p>
<p><span id="p42_12" class="anchor"></span>Example: Site Parameters Available<br />
Parameters Tab</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/025.png)</p></td>
</tr>
</tbody>
</table>

# # Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-3" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont." class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<h3 id="output-devices-area">Output Devices Area</h3>
<p><strong>Inpatient Missing Dose Request Printer:</strong> This field identifies the default division printer for Inpatient Missing Dose requests.</p>
<p><strong>Clinic Missing Dose Request Printer:</strong> This field identifies a specific clinic printer for Clinic Missing Dose requests.</p>
<p>You may set the MISSING DOSE PRINTER field in the CLINIC DEFINITION (#53.46) file according to the following 3-tiered approach to defining a clinic missing dose request printer.</p>
<ul>
<li><p>This field allows you to specify a printer device that is located at a particular clinic in order to send all missing dose requests for this clinic to the specified printer.</p></li>
</ul>
<p>Example: Specifying a Printer Device for the Clinic</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/026.png)</p>
<ul>
<li><p>If no specific Clinic Missing Dose Request Printer device is defined above for this particular clinic, missing dose requests will print on a general Clinic Missing Dose Request Printer that is defined for the division in the BCMA Parameters Tab Output Devices.</p></li>
</ul>
<p>Example: BCMA Parameters Tab Output Devices</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/027.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-4" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-1" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<ul>
<li><p>If no specific Clinic Missing Dose Request Printer device is defined above for this particular clinic, AND no general Clinic Missing Dose Request Printer is defined for a division in the BCMA Parameters Tab Output Devices, then all missing dose requests for both clinic and inpatient orders will print on the Inpatient Missing Dose Request Printer defined for the division in the BCMA Parameters Tab Output Devices.</p></li>
</ul>
<p>Example: BCMA Parameters Tab Output Devices</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/028.png)</p>
<h3 id="mail-groups-area">Mail Groups Area</h3>
<p><strong>Mail Groups:</strong> This area lists the mail groups that must be created using the <em>VistA Mail Group Edit</em> [XM EDIT MG] option, and by setting the TYPE field to PUBLIC. BCMA<br />
V. 3.0 includes the following mail groups listed below:</p>
<ul>
<li><p><strong>Due List Error:</strong> This field generates an E-mail message for any medication order that BCMA cannot resolve for VDL placement, and sends it to the mail group members. An example might include no administration times entered for a Continuous order.</p></li>
<li><p><strong>Missing Dose Notification:</strong> This field generates an E-mail message for any Missing Dose Request</p>
<p>entered using the BCMA GUI menu option. The E-mail is sent to all members of the mail group, specifically Pharmacy, as a “fail safe” even if the designated Missing Dose printer is not functioning.</p></li>
<li><p><strong>Unknown Actions:</strong> This field generates an E-mail message for any administration with an “Unknown” status while processing administrations to display on the VDL.</p></li>
<li><p><strong>Unable to Scan:</strong> Generates an E‑mail message to alert the mail group when a user creates an “Unable to Scan” entry and to assist in researching the reasons for a scanning failure.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# # Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-5" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-2" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<h3 id="reports-area">Reports Area</h3>
<p><strong>Include Comments:</strong> This check box, when selected, will automatically check the “Include Comments” check box in the Report dialog box as the default setting for the Medication History Report and the Medication Log Report. If this is unchecked, the “Include Comments” check box will be unchecked, by default, in the related Report dialog box. Users can change the check box setting in the Printer dialog box as needed, depending on whether they wish to have the comments for the administration included on the report.</p>
<p><strong>Med Hist Days Back:</strong> This field lets you define the number of days in the past, from the current system date, that the Medication History Report should retrieve data. The allowable entry is 1 to 9999 days. The default is 30 days.</p>
<ul>
<li><p>A user can change the date range for the report,<br />
in the Report dialog box.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-6" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-3" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<h3 id="bar-code-options-area">Bar Code Options Area</h3>
<p><strong>Default Bar Code Format:</strong> This field lets you select the desired bar code format that you want to produce on the bar code label printer. The following options are available from a drop-down list box: C39, 128, and I25.</p>
<p><strong>Default Bar Code Prefix:</strong> This field lets you specify up to five alphanumeric characters of text that will print as a prefix on a bar code label printed on the bar code label printer.</p>
<p><strong>Using Robot RX:</strong> This check box should be checked only if your site is using the Robot RX product.</p>
<h3 id="five-rights-override-area">Five Rights Override Area</h3>
<p><strong>Unit Dose Administration:</strong> This field lets you control the Unable to Scan verification process by allowing the user to verify the Five Rights of medication administration and proceed with a unit dose administration without entering a Drug IEN or National Drug Code (NDC).</p>
<p><strong>IV Administration:</strong> This field lets you control the Unable to Scan verification process by allowing the user to verify the Five Rights of medication administration and proceed with an IV administration without entering a Drug IEN or National Drug Code (NDC).</p>
<h3 id="administration-area">Administration Area</h3>
<p><strong>Require ESig To Administer Medication:</strong> This check box requires that users enter their VistA signon credentials and Electronic Signature Code (ESig) before launching GUI BCMA. Otherwise, the clinician administering medications will be asked for their VistA signon credentials.</p>
<p><strong>Allow Multiple Admins for On-Call:</strong> When checked, your division allows multiple administrations for an On-Call order.</p>
<h3 id="non-nurse-verified-orders-area">Non-Nurse Verified Orders Area</h3>
<p>This parameter allows sites to administer non-nurse verified medication orders with no warnings displayed, to display a warning before administering non-nurse verified medication orders, or to prohibit administration of non-nurse verified medication orders. Facilities will be able to set this option by division.</p>
<p><strong>Allow Administration (No Warning):</strong> When checked, your site allows administration of non-nurse veriied medication orders with no warnings displayed.</p>
<p><strong>Allow Administration with Warning:</strong> When checked, your site will display a warning before administering non-nurse verified medication orders. Marking as Held or Refused and Missing Dose requests will be allowed with warning.</p></td>
</tr>
</tbody>
</table>

# # Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-7" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-4" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<p><strong>Prohibit Administration:</strong> When checked, your site will prohibit administration of non-nurse verified medication orders and missing dose requests. Marking as Held or Refused will be allowed with warning.</p>
<h3 id="allowable-time-limits-in-minutes-area">Allowable Time Limits In Minutes Area</h3>
<p><strong>Before and After Scheduled Admin Time:</strong> This parameter defines the allowable medication administration timeframe. In the example provided, the allowable timeframe is set to one hour before through one hour after the scheduled administra­tion time. Each window may be defined up to 240 minutes.</p>
<p><strong>Note:</strong> The parameters for Allowable Time Limits (Before Scheduled Admin Time and After Scheduled Admin Time) are ignored when displaying clinic orders on the Cover Sheet and displaying and administering clinic orders on the VDL.</p>
<p><strong>PRN Effectiveness Entry:</strong> This parameter defines the allowable time for the PRN Effectiveness to be assessed, after a PRN medication is given, and before a variance is logged. If a medication administration is outside the allowable time, a variance will be logged when the effectiveness is entered. You can define this window up to 960 minutes (equivalent to 16 hours.) Numeric options in 10 minute increments are provided in the spinner field.</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-8" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/029.png)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-5" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<h3 id="virtual-due-list-default-times-area">Virtual Due List Default Times Area</h3>
<p><strong>Start Time and Stop Time:</strong> This option lets you enter the number of hours before and after NOW that GUI BCMA will initally display orders on a patient’s VDL (i.e., patient record).</p>
<h3 id="include-schedule-types-area">Include Schedule Types Area </h3>
<p>These check boxes let you select the default display for the CHUI Menu Option Due List [PSBO DL] and the BCMA VDL. The PRN check box controls the default display of PRN medications on the VDL. Your VAMC can choose to have the PRN Schedule Types display on the VDL by default, or to display PRN medications once the clinician selects the PRN Schedule Type check box on the VDL. All other Schedule Types will display by default and cannot be changed.</p>
<ul>
<li><p>Individual client settings are not allowed.</p></li>
</ul>
<h3 id="misc-options-area">Misc Options Area</h3>
<p><strong>Max Client/Server Clock Variance:</strong> This field lets you specify the number of minutes allowed for a variance, between the Client clock and the Server clock time.</p>
<ul>
<li><p><strong>If outside the range,</strong> a Warning message displays.</p></li>
</ul>
<p><strong>Patient Transfer Notification Timeframe In Hours:</strong> This field lets you define the number of hours, before the current system time, that a patient movement must be less than for the movement type (usually a transfer) to display on the BCMA VDL. The allowable entry for this parameter is a minimum value of 2 and a maximum value of 99. The default is 72 hours.</p>
<ul>
<li><p>Individual client settings are not allowed.</p></li>
</ul>
<p><strong>BCMA Idle Timeout In Minutes:</strong> This field lets you define the number of minutes before BCMA becomes inactive. The default is 1 minute.</p>
<p><strong>PRN Documentation In Hours:</strong> This field lets you define the minimum number of hours from NOW that BCMA V. 3.0 will search for PRN medication orders needing effectiveness comments. The four most recent PRN orders that need documentation display within the PRN Effectiveness mouse-over list in the “BCMA Clinical Reminders” marquee, which is located in the lower, right-hand corner of the VDL. BCMA displays PRN medications based on the current admission or the site parameter timeframe (whichever is greater). The allowable entry for this parameter is a minimum value of 1 and a maximum value of 999. The default is 72 hours.</p>
<ul>
<li><p>Individual client settings are not allowed.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-9" class="H2-Continued">![](bcma-version-3-manager-s-user-manual-psb-3-142/030.png)Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-parameters-tab-cont.-6" class="H3-Continued">Working with the Parameters Tab (cont.)</h3>
<h3 id="misc-options-area-cont.">Misc Options Area (cont.)</h3>
<p><strong>Max Date Range:</strong> This field lets you specify the maximum number of days allowed for the IV Bag Status and Medication Therapy reports. A warning message will display if the user attempts to run these reports beyond the number of days allowed by this site parameter. No default.</p>
<p><strong>Patch Display Duration:</strong> This field lets you specify the number of days after an order’s Stop Date that a “Given” patch will continue to display on the VDL and Cover Sheet. The allowed values are: Always Display and 7‑14 days. The display date will be calculated by adding the number of days defined in the site parameter to the Stop Date of the order. If the value of the site parameter is Always Display, then the patch will continue to display on the VDL until it is marked as removed using the Due List–regardless of the order Stop Date. The default is Always Display.</p>
<p><strong>Injection Site History Max Hours:</strong> This field lets you specify the maximum number of hours that previous injection sites will display on the VDL, during the administration of injectable medications for the current patient. The allowable entry for this parameter is a miniumum value of 1 and a maximum value and default of 72 hours.</p>
<p><span id="p16_Dermal" class="anchor"></span><strong>Dermal Site History Max Days:</strong> This field lets you specify the maximum number of days that previous dermal sites will display on the VDL, during the administration of medications requiring removal for the current patient. The allowable entry for this parameter is a maximum value of 2 digits and the maximum value allowed is 99 days.</p>
<p><strong>Enable CPRS Med Order Button:</strong> Selecting this button allows clinicians to use the CPRS Med Order Button in BCMA V. 3.0 to electronically order, document, review, and sign verbal- and phone-type STAT and NOW (One-Time) medication orders that they are administering to patients.</p>
<ul>
<li><p>Clinicians can access the CPRS Med Order Button functionality only if they hold the PSB CPRS MED BUTTON security key.</p></li>
<li><p>Clinicans must be able to accept <em>and</em> sign orders in CPRS to use the CPRS Med Order Button functionality in BCMA V. 3.0.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-10" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/031.png)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab">Working with the Default Answer Lists Tab</h3>
<p>You can activate the Default Answer Lists Tab by placing the cursor over the Tab, and then clicking once on it. Doing so activates the site parameters for the Default Answer Lists Tab.</p>
<p><span id="default_answer_listtab" class="anchor"></span>Example: Default Answer Lists Tab Selected<br />
and List Names Provided</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/032.png)</p>
<p>You can use the Default Answer Lists Tab to define the Selection Lists for the following options. These lists are free-text and definable on a divisional basis.</p>
<p>Reason Medication Given PRN</p>
<p>Reason Medication Held</p>
<p>Reason Medication Refused</p>
<p>Injection Sites</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-11" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont." class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>You can display Default Answer Lists Names by clicking once on the down arrow on the List Name drop-down list box. To select a list, highlight a selection in the list box. Then you are ready to create each list within the text box provided. See the example provided below.</p>
<p><strong>Note:</strong> The Attribute column is available only when you choose the Default Answer Lists for “Reason Medication Given PRN.”</p>
<p><span id="default_answer_listname18" class="anchor"></span>Example: Selecting a Default Answer Lists Name</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/033.png)</p>
<p><strong>Note:</strong> This section provides examples of suggested Default Answer Lists for the List Names shown above in the drop-down list.</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-12" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/034.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/035.png)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-1" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>You can create a list by pointing inside the text box associated with a list item, and then clicking the right mouse button. You may Add, Rename, or Delete any item within the box by highlighting the option within the List Items box, and then clicking on the right mouse button to make your selection. To activate the Rename or Delete functions for one of the listings, highlight the listing, and then click on the related command in the list box.</p>
<p>After you complete a list, click on the Save List button to store your list before exiting the Default Answer Lists Tab.</p>
<p><strong>Note:</strong> A warning message displays if you attempt to enter more than 100 entries in a Default Answer Lists.</p>
<p>Example: Creating a Default Answer List for</p>
<p>“Reason Medication Given PRN”</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/036.png)</p>
<p>— THEN —</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/037.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/038.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/039.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/040.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/041.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/042.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-13" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-2" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>This section provides suggested entries for the Default Answers Lists for GUI BCMA V. 3.0.</p></td>
</tr>
</tbody>
</table>

Example: Suggested Default Answer List for  
”Reason Medication Given PRN”

|            |                         |
|------------|-------------------------|
| Reason \#: | Value                   |
| 1          | Agitation               |
| 2          | Anxiety                 |
| 3          | Arrhythmia              |
| 4          | Chest Pain              |
| 5          | Congestion              |
| 6          | Constipation            |
| 7          | Cough                   |
| 8          | Cramps                  |
| 9          | Diarrhea                |
| 10         | Discomfort              |
| 11         | Dizziness               |
| 12         | Dyspepsia               |
| 13         | Dysuria                 |
| 14         | Elevated Blood Pressure |
| 15         | Elevated Blood Sugar    |
| 16         | Extrapyramidal Symptoms |
| 17         | Fever                   |
| 18         | Gastritis               |
| 19         | Headache                |
| 20         | Hiccups                 |
| 21         | Indigestion             |
| 22         | Insomnia                |

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-14" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-3" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>This section provides suggested entries for the Default Answers Lists for GUI BCMA V. 3.0.</p></td>
</tr>
</tbody>
</table>

Example: Suggested Default Answer List for

“Reason Medication Given PRN” (cont.)

|            |                     |
|------------|---------------------|
| Reason \#: | Value               |
| 23         | Irritation          |
| 24         | Itching             |
| 25         | Low Blood Pressure  |
| 26         | Low Blood Sugar     |
| 27         | Muscle Spasm        |
| 28         | Nausea              |
| 29         | Nervousness         |
| 30         | Nightmares          |
| 31         | Nocturia            |
| 32         | Oliguria            |
| 33         | Pain                |
| 34         | Psychosis           |
| 35         | Seizures            |
| 36         | Shortness of Breath |
| 37         | Sore Throat         |
| 38         | Tremors             |
| 39         | Vertigo             |
| 40         | Vomiting            |
| 41         | Wheezing            |
| 42         | Withdrawals         |

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-15" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-4" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>This section provides suggested entries for the Default Answers Lists for GUI BCMA V. 3.0.</p></td>
</tr>
</tbody>
</table>

Example: Suggested Default Answer List for

“Reason Medication Held”

|            |                             |
|------------|-----------------------------|
| Reason \#: | Value                       |
| 1          | Agitation                   |
| 2          | Apical Pulse Out of Range   |
| 3          | Authorized Absence          |
| 4          | Blood Pressure Out of Range |
| 5          | Blood Sugar Out of Range    |
| 6          | Constipation                |
| 7          | Diarrhea                    |
| 8          | NPO                         |
| 9          | Obtunded                    |
| 10         | Off Ward                    |
| 11         | On Pass                     |
| 12         | Provider Ordered            |
| 13         | Respirations Out of Range   |
| 14         | Sleeping                    |
| 15         | Somnolent                   |
| 16         | Temperature Out of Range    |
| 17         | HEALED                      |

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-16" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-5" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>This section provides suggested entries for the Default Answers Lists for GUI BCMA V. 3.0.</p></td>
</tr>
</tbody>
</table>

Example: Suggested Default Answer List for

“Reason Medication Refused”

|            |                  |
|------------|------------------|
| Reason \#: | Value            |
| 1          | Diarrhea         |
| 2          | Emesis           |
| 3          | Nausea           |
| 4          | Patient Request  |
| 5          | Patient Spit Out |

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-17" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-default-answer-lists-tab-cont.-6" class="H3-Continued">Working with the Default Answer Lists Tab (cont.)</h3>
<p>This section provides suggested entries for the Default Answers Lists for GUI BCMA V. 3.0.</p>
<h3 id="documenting-and-displaying-anatomic-location-for-medication-administrations">Documenting and Displaying Anatomic Location for Medication Administrations </h3>
<p>In the BCMA Site Parameters application, on the Parameters tab, in the Misc. Options section, a new site parameter is available, called “Dermal Site History Max Days”. It displays directly below the existing “Injection Site History Max Hours” site parameter.</p>
<p>See example below:</p></td>
</tr>
</tbody>
</table>

Example of new Dermal Site History Max Days site parameter on Parameters tab:

![](bcma-version-3-manager-s-user-manual-psb-3-142/043.png)

In the following BCMA CHUI, you can view and edit the new PSB DERMAL SITE MAX DAYS site parameter , as in the examples provided below. This includes the following options:

1.  XPAR EDIT BY TEMPLATE Edit Parameter Values with Template
2.  XPAR EDIT KEYWORD Edit Parameter Definition Keyword
3.  XPAR EDIT PARAMETER Edit Parameter Values

Example of XPAR EDIT BY TEMPLATE with new PSB DERMAL SITE MAX DAYS site parameter:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: XPAR ED</p>
<p>1 XPAR EDIT BY TEMPLATE Edit Parameter Values with Template</p>
<p>2 XPAR EDIT KEYWORD Edit Parameter Definition Keyword</p>
<p>3 XPAR EDIT PARAMETER Edit Parameter Values</p>
<p>CHOOSE 1-3: 1 XPAR EDIT BY TEMPLATE Edit Parameter Values with Template</p>
<p>Edit Parameter Values with Template</p>
<p>Select PARAMETER TEMPLATE NAME: PSB DIVISION BCMA Divisional Parameters</p>
<p>Select INSTITUTION NAME: XXXXXX NY VAMC 500</p>
<p>BCMA Divisional Parameters for Division: XXXXXX</p>
<p>------------------------------------------------------------------------------</p>
<p>Is BCMA System On-Line YES</p>
<p>Default Bar Code Format C39</p>
<p>Default Barcode Prefix</p>
<p>Using Robot RX NO</p>
<p>Allowed Mins After Sched Admin 60</p>
<p>Allowed Mins Before Sched Admin 60</p>
<p>Require E-Sig to Administer NO</p>
<p>Allow Multi Admin On-Call YES</p>
<p>Allowed Mins to Enter PRN Effect 80</p>
<p>Scratch HFS Directory USER$:[SPOOLER]</p>
<p>Due List Error Notification Mail Group BCMA DUE LIST ERROR</p>
<p>Missing Dose Notification Mail Group BCMA MISSING DOSE</p>
<p>System Error Notification Mail Group</p>
<p>Missing Dose Printer ZZFIDO</p>
<p>Clinic Order Missing Dose Printer</p>
<p>Allowable client-server time variance 30</p>
<p>Include Blank Addendums at end YES</p>
<p>Include Continuous Meds YES</p>
<p>Include IV Med Orders YES</p>
<p>Include On Call Meds NO</p>
<p>Include One-Time Meds YES</p>
<p>Include PRN Meds YES</p>
<p>Include Unit Dose Med Orders</p>
<p>Default hours prior to NOW for the VDL 1</p>
<p>Default hours after NOW for the VDL 1</p>
<p>The UNC of the Auto-update Server \\vhaisdfpc3\bcma$\BCMA_AutoUp</p>
<p>date_Files</p>
<p>Autoupdate Notification Mail Group</p>
<p>IV Provider Comments A W-Display Warning Message</p>
<p>P I-Invalid IV Bag</p>
<p>H W-Display Warning Message</p>
<p>S I-Invalid IV Bag</p>
<p>C W-Display Warning Message</p>
<p>Patient ID Display Label SSN</p>
<p>Non-Nurse Verified Prompt action N-Allow Admin (No Warning)</p>
<p>Last Injection Site Max Hours 72</p>
<p>Last Dermal Site Max Days 14</p>
<p>------------------------------------------------------------------------------</p>
<p>IS BCMA ON-LINE: YES//</p>
<p>DEFAULT BARCODE FORMAT: C39//</p>
<p>DEFAULT BARCODE PREFIX:</p>
<p>USING ROBOT RX: NO//</p>
<p>ALLOWED MINS AFTER SCHED TIME: 60//</p>
<p>ALLOWED MINS BEFORE SCHED TIME: 60//</p>
<p>REQUIRE ESIG TO ADMINISTER: NO//</p>
<p>ALLOW MULTIPLE ON CALL ADMINS: YES//</p>
<p>ALLOWED MINS FOR PRN EFFECT: 80//</p>
<p>SCRATCH HFS DIRECTORY: USER$:[SPOOLER]//</p>
<p>DUE LIST ERRORS MAIL GROUP: BCMA DUE LIST ERROR// BCMA DUE LIST ERROR</p>
<p>MISSING DOSE MAIL GROUP: BCMA MISSING DOSE// BCMA MISSING DOSE</p>
<p>SYSTEM ERRORS MAIL GROUP:</p>
<p>MISSING DOSE PRINTER: ZZFIDO// ZZFIDO PRINTERS CORNER _NLA0:</p>
<p>CO MISSING DOSE PRINTER:</p>
<p>ALLOWABLE SERVER CLOCK VARIANCE: 30//</p>
<p>INCLUDE BLANKS ADDENDUMS ON DUE LIST: YES//</p>
<p>INCLUDE CONTINUOUS MEDS ON DUE LIST: YES//</p>
<p>INCLUDE IV MEDS ON DUE LIST: YES//</p>
<p>INCLUDE ON CALL MEDS ON DUE LIST: NO//</p>
<p>INCLUDE ONE-TIME MEDS ON DUE LIST: YES//</p>
<p>INCLUDE PRN MEDS ON DUE LIST: YES//</p>
<p>INCLUDE UNIT DOSE MEDS ON DUE LIST:</p>
<p>HOURS PRIOR TO NOW FOR VDL: 1//</p>
<p>HOURS AFTER NOW FOR VDL: 1//</p>
<p>UNC OF THE AUTOUPDATE SERVER: \\vhaisdfpc3\bcma$\BCMA_AutoUpdate_Files</p>
<p>Replace</p>
<p>AUTOUPDATE NOTIFICATION MAIL GROUP:</p>
<p>For IV Provider Comments -</p>
<p>Select IV Type:</p>
<p>PSB PATIENT ID LABEL: SSN//</p>
<p>PSB NON-NURSE VERIFIED PROMPT: N-Allow Admin (No Warning)//</p>
<p>PSB INJECTION SITE MAX HOURS: 72//</p>
<p>PSB DERMAL SITE MAX DAYS: 14// ?</p>
<p>Enter a number of days (1-30).</p>
<p>PSB DERMAL SITE MAX DAYS: 14//</p>
<p>BCMA Divisional Parameters for Division: XXXXXX is now:</p>
<p>------------------------------------------------------------------------------</p>
<p>Is BCMA System On-Line YES</p>
<p>Default Bar Code Format C39</p>
<p>Default Barcode Prefix</p>
<p>Using Robot RX NO</p>
<p>Allowed Mins After Sched Admin 60</p>
<p>Allowed Mins Before Sched Admin 60</p>
<p>Require E-Sig to Administer NO</p>
<p>Allow Multi Admin On-Call YES</p>
<p>Allowed Mins to Enter PRN Effect 80</p>
<p>Scratch HFS Directory USER$:[SPOOLER]</p>
<p>Due List Error Notification Mail Group BCMA DUE LIST ERROR</p>
<p>Missing Dose Notification Mail Group BCMA MISSING DOSE</p>
<p>System Error Notification Mail Group</p>
<p>Missing Dose Printer ZZFIDO</p>
<p>Clinic Order Missing Dose Printer</p>
<p>Allowable client-server time variance 30</p>
<p>Include Blank Addendums at end YES</p>
<p>Include Continuous Meds YES</p>
<p>Include IV Med Orders YES</p>
<p>Include On Call Meds NO</p>
<p>Include One-Time Meds YES</p>
<p>Include PRN Meds YES</p>
<p>Include Unit Dose Med Orders</p>
<p>Default hours prior to NOW for the VDL 1</p>
<p>Default hours after NOW for the VDL 1</p>
<p>The UNC of the Auto-update Server \\vhaisdfpc3\bcma$\BCMA_AutoUp</p>
<p>date_Files</p>
<p>Autoupdate Notification Mail Group</p>
<p>IV Provider Comments A W-Display Warning Message</p>
<p>P I-Invalid IV Bag</p>
<p>H W-Display Warning Message</p>
<p>S I-Invalid IV Bag</p>
<p>C W-Display Warning Message</p>
<p>Patient ID Display Label SSN</p>
<p>Non-Nurse Verified Prompt action N-Allow Admin (No Warning)</p>
<p>Last Injection Site Max Hours 72</p>
<p>Last Dermal Site Max Days 14</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example of XPAR EDIT KEYWORD with new PSB DERMAL SITE MAX DAYS site parameter:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CHOOSE 1-5: 3  XPAR EDIT PARAMETER     Edit Parameter Values</p>
<p>Edit Parameter Values</p>
<p>                         --- Edit Parameter Values ---</p>
<p>Select PARAMETER DEFINITION NAME: psb dermAL SITE MAX DAYS     Last Dermal Site</p>
<p>Max Days</p>
<p>Select INSTITUTION NAME: alb</p>
<p>     1   ALB-PRRTP             NY  MC(M)     500PA </p>
<p>     2   XXXXXX                NY  VAMC      500 </p>
<p>     3   XXXXXX OPC            NY  OCMC      500A4 </p>
<p>     4   ALBUQUERQUE, NM                     501 </p>
<p>     5   ALBUQUERQUE-RO        NM            340 </p>
<p>CHOOSE 1-5: 2  XXXXXX          NY  VAMC      500 </p>
<p>----------- Setting PSB DERMAL SITE MAX DAYS  for Division: XXXXXX -----------</p>
<p>PSB DERMAL SITE MAX DAYS: 14//</p>
<p>Select INSTITUTION NAME:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example of XPAR EDIT PARAMETER with new PSB DERMAL SITE MAX DAYS site parameter:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CHOOSE 1-5: 1  XPAR EDIT KEYWORD     Edit Parameter Definition Keyword</p>
<p>Edit Parameter Definition Keyword</p>
<p>Select PARAMETER DEFINITION NAME: psb dermAL SITE MAX DAYS    Last Dermal Site Max Days</p>
<p>Select KEYWORD:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

From the BCMA Site Parameters application, on the Default Answer Lists tab, you can now access a new default answer list with list name “Body Sites.” This list allows both Injection Sites (for injection type medications) and Dermal Sites (for medications requiring removal) to be defined in a single list.

Example of Body Sites list on Default Answer Lists tab:

![](bcma-version-3-manager-s-user-manual-psb-3-142/044.png)

> **NOTE:** All items that are currently in the facility’s existing Injection Sites default answer list will be copied over to the new Body Sites default answer list, with the Item name for each one the same, and with the Injection Site attribute automatically selected for each.

If the new item name matches that of an existing item’s name, when the OK button is clicked in the Add New Item window, the following message displays indicating that duplicates cannot be created. When you click the OK button, the Body Sites default answer list tab displays with the new item not added.

![](bcma-version-3-manager-s-user-manual-psb-3-142/045.png)

When a new item is added to the Body Sites list, the Item name and at least one checkbox must be selected in order for the OK button to be enabled, so the new item can be added to the list.

Example of Add New Item window, with OK button disabled (neither checkbox is checked):

![](bcma-version-3-manager-s-user-manual-psb-3-142/046.png)

When an existing item in the list is selected, selection of Edit option from right-click menu will allow the existing item to be edited in the Edit Item window.

If the new item name matches that of an existing item’s name, when the OK button is clicked in the Edit Item window, a message displays indicating that the item is already in the list. When the OK button is clicked, the Body Sites default answer list tab displays with the new item not added.

![](bcma-version-3-manager-s-user-manual-psb-3-142/047.png)

When you are editing an existing item in the Body Sites list, you must select the Item name and at least one checkbox in order for the OK button to be enabled, so that you can edit the item in the list.

Example of Edit Item window when it first opens:

![](bcma-version-3-manager-s-user-manual-psb-3-142/048.png)

If you want to delete an existing item, select Delete from the right-click menu.

The system will then display a message asking you to confirm deletion of the selected item. For example:

![](bcma-version-3-manager-s-user-manual-psb-3-142/049.png)

Select Yes to delete the selected item from the list and select No if you do NOT wish to delete the selected item from the list.

To access the Body Site Editor, click the Edit Layout button above the body diagram image (see below for example).

The Body Site Editor displays the following items:

- Item, Injection Site and Dermal Site columns , with the Item name listed, and “Y” in the Injection Site and/or Dermal Site columns, based on the definition of the item in the list.
- When the Body Site list is selected, the right-click menu options are available (i.e., Add New, Edit, Delete).
- If the item in the list has a position defined on the body diagram image, a checkmark displays to the left of the Item name. The left side of the Body Site Editor window displays a body diagram image which indicates the positions on the body that have been associated with items in the Body Sites list.
- Dots (or circles) display on the body diagram indicating the positions (coordinates) on the body that have been associated with items in the Body Sites list.
- When an item in the list on the body diagram is selected, the dot on the body diagram image that corresponds to that item on the list displays in a darker color, to indicate that is the position on the body diagram.

To associate a position on the body diagram image to a given item in the list, select and drag the item in the list (using your mouse) to the desired position on the body diagram.

To display the Item name, coordinates, and internal sequence number, hover your cursor over a dot on the body diagram image.

The bottom of the Body Site Editor window contains two buttons:

- OK: click to save changes to the list, and display the main Default Answer List tab with Body Sites list.
- Cancel: click to cancel changes to the list.

Example of Body Site Editor window for Body Sites default answer list:

![](bcma-version-3-manager-s-user-manual-psb-3-142/050.png)

The following is an example of a list of Body Sites, so that you can accurately depict and record the location of product administration (i.e., transdermal medications that require removal as well as injections).

<span id="list_of_recommendedbodysites33" class="anchor"></span>Example: List of Recommended Body Sites

| Item                  | Injection site | Dermal site |
|---------------------------|--------------------|-----------------|
| Abdomen, Left Lower Quad  | Y                  | Y               |
| Abdomen, Left Upper Quad  | Y                  | Y               |
| Abdomen, Right Lower Quad | Y                  | Y               |
| Abdomen, Right Upper Quad | Y                  | Y               |
| Arm, Left Upper           | Y                  | Y               |
| Arm, Right Upper          | Y                  | Y               |
| Back, Lower Left          |                    | Y               |
| Back, Lower Right         |                    | Y               |
| Back, Middle              |                    | Y               |
| Back, Upper Left          |                    | Y               |
| Back, Upper Right         |                    | Y               |
| Behind Ear, Left          |                    | Y               |
| Behind Ear, Right         |                    | Y               |
| Bicep, Left               |                    | Y               |
| Bicep, Right              |                    | Y               |
| Buttock, Left             | Y                  |                 |
| Buttock, Right            | Y                  |                 |
| Deltoid, Left             | Y                  |                 |
| Deltoid, Right            | Y                  |                 |
| Flank, Left               |                    | Y               |
| Flank, Right              |                    | Y               |
| Forearm, Left Lower       | Y                  | Y               |
| Forearm, Left Upper       | Y                  | Y               |
| Forearm, Right Lower      | Y                  | Y               |
| Forearm, Right Upper      | Y                  | Y               |
| Gluteal, Left             | Y                  |                 |
| Gluteal, Right            | Y                  |                 |
| Hip, Left                 |                    | Y               |
| Hip, Right                |                    | Y               |
| Intravenous/Central       | Y                  |                 |
| Intravenous/Midline       | Y                  |                 |
| Intravenous/Peripheral    | Y                  |                 |
| Intravenous/PICC          | Y                  |                 |
| Irrigation                | Y                  |                 |
| Knee, Left                |                    | Y               |
| Knee, Right               |                    | Y               |
| Other (Add Comment)       | Y                  | Y               |
| Scapula, Left             |                    | Y               |
| Scapula, Right            |                    | Y               |
| Shoulder, Left            |                    | Y               |
| Shoulder, Right           |                    | Y               |
| Thigh, Left               | Y                  |                 |
| Thigh, Right              | Y                  |                 |

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-18" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-iv-parameters-tab">Working with the IV Parameters Tab</h3>
<p>You can activate the IV Parameters Tab by placing the cursor over the Tab, and then clicking once on it. Doing so activates the site parameters for this Tab.</p>
<p>The IV Parameters Tab lets you configure the business logic that BCMA V. 3.0 will use when processing an IV order that has been changed. You can configure this option using the following hierarchy: Division and Ward.</p>
<p>When BCMA V. 3.0 is first installed, it automatically sets up the recommended default settings for the division and all IV types.</p>
<p><strong>Note:</strong> Although the default settings are highly recommended by the BCMA Workgroup, you can still change them for your site.</p>
<p>Example: Site Parameters Available<br />
When IV Parameters Tab Selected</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/051.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-19" class="H2-Continued">![](bcma-version-3-manager-s-user-manual-psb-3-142/052.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/053.png)Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-iv-parameters-tab-cont." class="H3-Continued">Working with the IV Parameters Tab (cont.)</h3>
<p>This section describes each field that is available when you select the IV Parameters Tab.</p>
<h3 id="location-area">Location Area</h3>
<p><strong>Ward:</strong> This field lets you configure the IV parameter by division (ALL) or by an individual ward. “ALL” is the default setting for a division. This setting includes all wards.</p>
<ul>
<li><p>A ward provided in <strong>boldface</strong>, in the drop-down list box, indicates that an IV parameter has been set up.</p></li>
<li><p>You may change the configuration on an individual ward basis by selecting a ward from the Ward drop-down list box, making selections from the Prompts section, and then clicking <strong><span class="smallcaps">ok</span></strong> to accept the changes.</p></li>
</ul>
<p>Example: Ward Drop-Down List Box<br />
for Location Area</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/054.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-20" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/055.png)</h2></td>
<td><h3 id="working-with-the-iv-parameters-tab-cont.-1" class="H3-Continued">Working with the IV Parameters Tab (cont.)</h3>
<p>This section describes each field that is available when you select the IV Parameters Tab.</p>
<h3 id="iv-type-area">IV Type Area</h3>
<p><strong>Type:</strong> This field lets you configure the IV parameter by<br />
IV Type. They include: Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</p>
<ul>
<li><p>An IV Type listed in <strong>boldface</strong>, in the list box, is set up for the selected ward.</p></li>
</ul>
<p>Example: Type Drop-Down List Box<br />
for IV Type Area</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/056.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-21" class="H2-Continued"><br />
Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-iv-parameters-tab-cont.-2" class="H3-Continued">Working with the IV Parameters Tab (cont.)</h3>
<p>This section describes each field that is available when you select the IV Parameters Tab.</p>
<h3 id="prompts-area">Prompts Area</h3>
<p>Includes fields from the Inpatient Medications V. 5.0<br />
IV Order Entry screen. They include the following: Additive, Strength, Bottle, Solution, Volume, Infusion Rate, Med Route, Schedule, Admin Time, Remarks, Other Print Info, Provider, Start Date/Time, Stop Date/Time, and Provider Comments.</p>
<ul>
<li><p>Each field offers a selection of Warning, Non-Verify, and Invalid Bag.</p></li>
</ul>
<p>Example: Prompts Drop-Down List Box<br />
for Additive Field</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/057.png)</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-22" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="working-with-the-iv-parameters-tab-cont.-3" class="H3-Continued">Working with the IV Parameters Tab (cont.)</h3>
<h3 id="prompts-area-cont.">Prompts Area (cont.)</h3>
<p>Should you determine that you need to change the Prompts default settings, you will receive an Information message notifying you that your selection is not recommended for that particular option.</p>
<p>Example: Information Message<br />
When Prompts Default Settings Changed</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/058.png)</p>
<p><strong>If a field is set to Warning,</strong> and an order is changed, the<br />
IV bags from the old order are carried to the new order and display on the BCMA VDL. When you scan the bar code on an IV bag, a Warning message alerts you about fields that have changed. GUI BCMA would then display the Scan IV dialog box so you can begin infusing the IV bag.</p>
<p>Example: Warning Message That Fields<br />
in Inpatient Medications V. 5.0 Changed</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/059.png)</p>
<p><strong>If a field is set to Non-Verify,</strong> and an order is changed, the<br />
IV bags from the old order are carried to the new order and display on the BCMA VDL. When you scan a bar code on an IV bag, NO warning message displays. The Scan IV dialog box automatically displays so you can begin infusing the<br />
IV bag.</p>
<p><strong>If a field is set to Invalid Bag,</strong> and an order is changed, the IV bags from the old order do not carry to the new order or display on the BCMA VDL.</p></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-23" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="keyed-entry-timing-parameter">Keyed Entry Timing Parameter</h3>
<p>In order to determine which entries are scanned versus which entries are keyed-in for the Unable to Scan Summary report, BCMA incorporated a default, hard-coded timing threshold value of 400 milliseconds (ms). This mechanism sets the time limit by which BCMA distinguishes whether an IEN/NDC bar code number entry was scanned or keyed in manually. This feature is not absolute. However, it is intended to give a very close approximation. Entries that take less than the threshold value are logged as scanned, while entries taking longer than the threshold value are logged as scanner-bypass keyed entries.</p>
<p>The default value works for most sites without any changes. However, there may be variations across sites, due to various factors, including scanner models and speed settings that render the default timing parameter ineffective in determining whether an entry was scanned versus keyed. This may result in an inflated value for your keyed entries total on the Unable to Scan Summary report, especially for very long bar code numbers (e.g., 16-digit NDC numbers). It was found that network speed and distance from scanner base station have no effect on this feature.</p>
<p>Together, the local BCMA Coordinator and IRM/ADPAC can choose to override the default parameter by adding a command line parameter to the desktop shortcut for all BCMA workstations where the problem is encountered. Note that this is an optional parameter. If no parameter is entered, the default value of 400ms is used.</p>
<p>An optional command line parameter (/K for “keyboard”) overrides the default timer value in the BCMA desktop shortcut as follows:</p>
<ul>
<li><p>In desktop icon target properties, you can add /K= and a time value in milliseconds, for example: <strong>/K=500.</strong></p></li>
<li><p>The value must be positive and a whole number.</p></li>
<li><p>The value must be in the range of 250 to 1500.</p></li>
<li><p>If you don’t enter a parameter at all, or if you enter a value outside of 250 to 1500, it will default to 400.</p></li>
<li><p>The /K= parameter can be anywhere in the parameter string. (See example)</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Setting Site Parameters for GUI BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-and-updating-site-parameters-for-your-division-cont.-24" class="H2-Continued">Defining and Updating Site Parameters for Your Division (cont.)</h2></td>
<td><h3 id="keyed-entry-timing-parameter-cont." class="H3-Continued">Keyed Entry Timing Parameter (cont.)</h3>
<p>Example: Selecting an Optional Timer Value</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/060.png)</p>
<p>Timer value conversion:</p>
<p>250 (ms) = 0.25 second</p>
<p>400 (ms) = 0.4 second</p>
<p>1000 (ms)= 1.0 second</p>
<p>1500 (ms)= 1.5 seconds</p>
<p>Changes to this parameter will only impact the Keyed Entries total on the Unable to Scan Summary report. Values that are too low may result in an excessive and erroneous number of keyed entries reported. Values that are too high may result in the underreporting of actual keyed entries. It may take some trial and error before you find the threshold that works for your site, or even particular units within your site. Please note that the use of this parameter must be done according to your site policy.</p>
<p>If you choose to use this parameter to override the default keyed entry timing value, it must be added to each BCMA GUI desktop shortcut on the workstations where it is needed. In addition, each time the BCMA GUI client is reinstalled, this parameter must be added to all workstations that need it.</p></td>
</tr>
</tbody>
</table>

# Accessing the CHUI BCMA Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="accessing-the-chui-bcma-manager-menu-1">![](bcma-version-3-manager-s-user-manual-psb-3-142/061.png)<br />
Accessing the<br />
CHUI BCMA Manager Menu</h2></td>
<td><p>You can use the <em>Bar Code Medication Administration Manager</em> menu to access information entered by clinicians via the BCMA VDL within CHUI BCMA V. 3.0. You can access this menu option from any VistA-enabled terminal within your VAMC.</p>
<p>Because BCMA operates in real time, scanned patient and medication information is available as soon as the “scan” is successfully completed using GUI BCMA.</p>
<p>To access the CHUI BCMA Manager Menu</p>
<ol type="1">
<li><p>At a VistA-enabled terminal, enter your <strong>Access and Verify Codes</strong> when prompted by the system. The menus available to you will then display.</p></li>
</ol>
<p>Example: Accessing the CHUI BCMA Manager Menu</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/062.png)</p>
<ol start="9" type="1">
<li><p>At the “Select BCMA NURSING MENU Option:” prompt,<br />
type <strong>BAR</strong>, and then press <strong>&lt;Enter&gt;</strong> to access the <em>Bar Code Medication Administration Manager</em> menu. The options available to you then display.</p></li>
<li><p>At the “Select Bar Code Medication Administration Manager Option:” prompt, enter the <strong>text of the desired option</strong>, and then press <strong>&lt;Enter&gt;</strong>. The Main Screen for the associated option then displays.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Checking the Drug IEN Code for Unit Dose Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="verifying-the-drug-ien-code-for-a-unit-dose-medication">Verifying the Drug IEN Code for a Unit Dose Medication</h2></td>
<td><p>You can use the <em>Drug File Inquiry</em> [PSB DRUG INQUIRY] option from the <em>Bar Code Medication Administration</em> menu to verify the Drug IEN Code for Unit Dose medications. This option is particularly useful when you need to resolve a discrepancy with an IEN Code for a medication.</p>
<p>To verify the drug IEN code for a Unit Dose medication</p>
<ol type="1">
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>D</strong> to access the <em>Drug File Inquiry</em> [PSB DRUG INQUIRY] option. The associated screen displays.</p></li>
</ol>
<p>Example: Drug File Inquiry Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/063.png)</p>
<ol start="11" type="1">
<li><p>At the “Select DRUG:” prompt, type the <strong>name and dosage of the drug</strong> <strong>that you want an IEN Code</strong>, and then press <strong>&lt;Enter&gt;</strong>. The associated drug file information, or other IEN information, then displays. See the next page for an example.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Checking the Drug IEN Code for Unit Dose Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="verifing-the-drug-ien-code-for-a-unit-dose-medication-cont." class="H2-Continued">Verifing the Drug IEN Code for a Unit Dose Medication (cont.)</h2></td>
<td><p>To verify the drug IEN code for a Unit Dose medication</p>
<p>(cont.)</p>
<p>Example: Results of Drug File Inquiry</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/064.png)</p>
<p><strong>Note:</strong> The IEN Code appears on the first line, to the right of the Drug Name. Typically, this is the bar code number on the Unit Dose package prepared by the Pharmacy. Manufacturers’ National Drug Code (NDC) bar codes may appear in the SYNONYMS field within this screen. If the drug is non-formulary, the NON-FORMULARY field will be set to N/F.</p></td>
</tr>
</tbody>
</table>

# Responding to Missing Dose Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="creating-a-follow-up-message-for-a-missing-dose-request">Creating a Follow-up Message for a Missing Dose Request</h2></td>
<td><p>The <em>Missing Dose Followup</em> [PSB MISSING DOSE FOLLOWUP] option from the <em>Bar Code Medication Administration</em> <em>Manager</em> menu lets the Pharmacy electronically respond to a Missing Dose Request submitted by a clinician from BCMA V. 3.0. The Pharmacy can enter a reason that the dose was missing, the time the dose was delivered, and the name of the individual who delivered the dose.</p>
<p>To create a follow-up message for a Missing Dose Request</p>
<ol type="1">
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>MI</strong>, and then press <strong>&lt;Enter&gt;</strong> to access the <em>Missing Dose Followup</em> [PSB MISSING DOSE FOLLOWUP] option. The associated screen then displays.</p></li>
</ol>
<p><strong>Note</strong>: <span id="psb_3_100" class="anchor"></span>If your site is defined as multidivisional in the MAS PARAMETER (#43) file, then you will be prompted to select one or all divisions at your site. If you enter “O” (One) at the “Do you want ‘A’ll Divisions or just ‘O’ne Division:” prompt, then VistA displays the “Select Division:” prompt with your login division as the default. You can accept the default or enter “?” to choose from a list of site divisions. After you select a division, the system displays missing dose requests for that division on the screen below, and the division name is shown in the screen heading. If you select all divisions, then requests will be shown for all divisions at your site.</p>
<p>Example: Missing Dose Request Selection Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/065.png)</p>
<ol start="2" type="1">
<li><p>At the “Select Missing Dose Request # (&lt;RET&gt; to continue,<br />
‘^’ to quit): (1-7):” prompt, type the <strong>number opposite the Missing Dose that you want to create a follow-up message for</strong>, and then press <strong>&lt;Enter&gt;</strong>. The Missing Dose Request Pharmacy Follow-up Information screen, provided on the following page, then displays.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Responding to Missing Dose Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="creating-a-follow-up-message-for-a-missing-dose-request-cont." class="H2-Continued">Creating a Follow-up Message for a Missing Dose Request (cont.)</h2></td>
<td><p>To create a follow-up message for a Missing Dose Request (cont.)</p>
<p>Example: Missing Dose Request Entry Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/066.png)</p>
<ol start="12" type="1">
<li><p>At the DOSE DELIVERED field, type <strong>Yes</strong>, and then press <strong>&lt;Enter&gt;</strong>.</p></li>
</ol>
<p>If a medication is no longer active or will not be delivered, type No in this field.</p>
<ol start="13" type="1">
<li><p>At the DELIVERY DATE/TIME field, type <strong>N</strong> (for Now) or the <strong>date and time</strong> <strong>that the dose was delivered</strong>, and then press <strong>&lt;Enter&gt;</strong>.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Responding to Missing Dose Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="creating-a-follow-up-message-for-a-missing-dose-request-cont.-1" class="H2-Continued">Creating a Follow-up Message for a Missing Dose Request (cont.)![](bcma-version-3-manager-s-user-manual-psb-3-142/067.png)</h2></td>
<td><p>To create a follow-up message for a Missing Dose Request (cont.)</p>
<ol start="14" type="1">
<li><p>At the PHARMACY REASON NEEDED field, type the <strong>number that corresponds to your selection</strong> from the Pharmacy Reasons Needed Selection Table provided below.</p></li>
<li><p>At the COMMAND field, perform one of the following actions:</p></li>
</ol>
<p>Type <strong>S</strong>, and then press <strong>&lt;Enter&gt;</strong> to save the information that you entered for the Missing Dose Request selected.</p>
<p>Type <strong>E</strong>, and then press <strong>&lt;Enter&gt;</strong> to exit the Followup Information Screen.</p>
<ul>
<li><p><strong>If you try to exit the screen without saving the data,</strong> the system displays the message: “Save changes before leaving form (Y/N)?” Type <strong>N</strong> (for No), or <strong>Y</strong> (for Yes), and then press <strong>&lt;Enter&gt;</strong>. The system confirms that the data has been saved, and returns you to the “Select Bar Code Medication Administration Manager Option:” prompt.</p></li>
</ul>
<p>Type <strong>R</strong>, and then press <strong>&lt;Enter&gt;</strong> to refresh the Followup Information Screen.</p></td>
</tr>
</tbody>
</table>

Example: Pharmacy Reasons Needed Selection Table

|            |                             |
|------------|-----------------------------|
| Number | Pharmacy Reasons Needed |
| 1          | WS/FILL ON REQUEST          |
| 2          | FOUND IN DRAWER             |
| 3          | PHARMACIST ERROR            |
| 4          | EXPIRED/NO ORDER            |
| 5          | ATC ERROR                   |
| 6          | NOT ENOUGH PRNS             |
| 7          | TECHNICIAN ERROR            |
| 8          | ON PRE-EXCHANGE/PICK LIST   |
| 9          | PATIENT TRANSFERRED         |
| 10         | NURSE ADMIN ERROR           |

# Resetting User Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="resetting-a-users-default-parameter-settings">![](bcma-version-3-manager-s-user-manual-psb-3-142/068.png)Resetting a<br />
User’s Default Parameter Settings</h2></td>
<td><p>Once a clinician uses BCMA V. 3.0, the parameters become their default settings. For example, when they change the default settings for certain fields (i.e., Start and Stop Times, and Column Sort Selection) on the BCMA VDL, these settings are retained in their user parameters — and become the default settings each time they log on to BCMA V. 3.0. This does <em>not</em> apply to the Unit Dose Tab, which is the default view or to Schedule Types, which are all selected each time you open a VDL (i.e., patient record).</p>
<p>You can reset these user-selected parameters to site-defined parameters using the <em>Reset User Parameters</em> [PSB USER PARAM RESET] option in BCMAV. 3.0.</p>
<p>To reset a user’s default parameter settings</p>
<ol type="1">
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>RE</strong> to access the <em>Reset User Parameters</em> [PSB USER PARAM RESET] option. The associated screen then displays.</p></li>
</ol>
<p>Example: Reset User Parameters Sequence Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/069.png)</p>
<ol start="16" type="1">
<li><p>At the “Select User to Reset:” prompt, enter the <strong>user’s name</strong>, and then press &lt;<strong>Enter</strong>&gt;. A prompt displays.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Resetting User Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="resetting-a-users-default-parameter-settings-cont." class="H2-Continued">Resetting a<br />
User’s Default Parameter Settings (cont.)</h2></td>
<td><p>To reset a user’s default parameter settings (cont.)</p>
<ol start="17" type="1">
<li><p>At the “Are you sure you want to reset all parameters for this user? No//” prompt, perform one of the following actions:</p></li>
</ol>
<p><strong>To accept the default answer of No</strong>, press &lt;<strong>Enter</strong>&gt;. The system will <em>not</em> reset the user’s parameters. You will be returned to the Bar Code Medication Administration Manager Menu.</p>
<p><strong>To reset the user parameters,</strong> type <strong>Y</strong> at the prompt, and then press &lt;<strong>Enter</strong>&gt;. The system then provides a message of “Resetting…Done” to indicate that the user parameters have been reset. See the Example on the previous page for more details.</p></td>
</tr>
</tbody>
</table>

# Using the Trouble Shoot Med Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="identifying-scanning-problems">Identifying Scanning Problems</h2></td>
<td><p>You can use the <em>Trouble Shoot Med Log</em> [PSB MED LOG TROUBLE SHOOTER] option from the <em>Bar Code Medication Administration</em> <em>Manager</em> menu to determine the reason that a medication is <em>not</em> being marked on the BCMA VDL within BCMA V. 3.0 as “Given,” even though it is being scanned during a medication pass.</p>
<p>To identify scanning problems using the Trouble Shoot<br />
Med Log</p>
<ol type="1">
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>T</strong> to access the <em>Trouble Shoot Med Log</em> [PSB MED LOG TROUBLE SHOOTER] option. The associated screen then displays.</p></li>
</ol>
<p>Example: Medication Log Trouble Shooter Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/070.png)</p>
<ol start="18" type="1">
<li><p>At the “Select PATIENT:” prompt, enter the <strong>patient’s name,</strong> and then press &lt;<strong>Enter</strong>&gt;. CHUI BCMA provides data related to the patient name that you entered.</p></li>
</ol>
<p><strong>For a list of standard name and date formats,</strong> type <strong>?</strong> in the “Select PATIENT:” and Select Date To Validate:” prompts, and then press &lt;<strong>Enter</strong>&gt;.</p>
<ol start="19" type="1">
<li><p>At the “Select Date To Validate:” prompt, enter the <strong>desired date</strong>, and then press &lt;<strong>Enter</strong>&gt;. CHUI BCMA searches the database for every order for the selected patient and date you entered, and then displays a list of related orders. See the Example on the next page for more details.</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Using the Trouble Shoot Med Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="identifying-scanning-problems-cont." class="H2-Continued">Identifying Scanning Problems (cont.)</h2></td>
<td><p>To identify scanning problems using the Trouble Shoot<br />
Med Log (cont.)</p>
<p>Example: Medication Log Trouble Shooter Screen (cont.)</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/071.png)</p>
<ol start="20" type="1">
<li><p>At the “Enter a number (###):” prompt, enter the <strong>number that corresponds to the desired order in the selection list</strong>, and then press &lt;<strong>Enter</strong>&gt;. The selected order will display with the prompt “Is this the correct Order? Yes//”</p></li>
</ol>
<p><strong>If the list is longer than one screen,</strong> you will receive the prompt “Enter RETURN to continue or ‘^’ to exit.” Press &lt;<strong>Enter</strong>&gt; to display the rest of the list.</p></td>
</tr>
</tbody>
</table>

# Using the Trouble Shoot Med Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="identifying-scanning-problems-cont.-1" class="H2-Continued">![](bcma-version-3-manager-s-user-manual-psb-3-142/072.png)Identifying Scanning Problems (cont.)</h2></td>
<td><p>To identify scanning problems using the Trouble Shoot<br />
Med Log (cont.)</p>
<p>Example: Order Validation Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/073.png)</p>
<ol start="21" type="1">
<li><p>At the “Is this the correct Order? Yes//” prompt, press &lt;<strong>Enter</strong>&gt; to accept the default answer of Yes, and to display information about the order that you selected. The Order Validation Screen displays.</p></li>
<li><p>At the “Enter the DATE of Administration: Today//” prompt, press &lt;<strong>Enter</strong>&gt; to select today’s date. Otherwise, enter another date, and then press &lt;<strong>Enter</strong>&gt;. A variance reason displays, related to the order that you selected.</p></li>
</ol>
<p>If there is more than one administration time for the order, the system will list the times.</p>
<ol start="23" type="1">
<li><p>At the “Select Administration Time:” prompt, type the <strong>number corresponding to the desired administration time listed</strong>, and then press &lt;<strong>Enter</strong>&gt;. The system lists information related to the order’s administration time.</p></li>
<li><p>Perform one of the following actions:</p></li>
</ol>
<p>Press &lt;<strong>Enter</strong>&gt; to return to the list of medications for the selected patient and administration date.</p>
<p>Press <strong>^</strong> to exit the option.</p></td>
</tr>
</tbody>
</table>

# Running the Unknown Action Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="creating-a-listing-of-unknown-actions">![](bcma-version-3-manager-s-user-manual-psb-3-142/074.png)![](bcma-version-3-manager-s-user-manual-psb-3-142/075.png)Creating a Listing of Unknown Actions</h2></td>
<td><p>You can use the <em>Unknown Action Status Report</em> [PSBO XA] option from the <em>Bar Code Medication Administration</em> <em>Manager</em> menu to print a listing of administrations that have an unknown action status. When a user is in the process of documenting an administration in <em>Manual Medication Entry</em> [PSB MED LOG NEW ENTRY], the administration status initially defaults to blank (null). If the order is not completed with a valid administration status, the Admin Status will be listed as unknown, and appear on the Unknown Action Status Report.</p>
<p>The unknown (null) status can occur during <em>Manual Medication Entry</em> when the user’s network connection is broken, their terminal emulator software malfunctions, or if the user improperly exits out of the application.</p>
<p>Use the BCMA GUI Edit Med Log to correct the administration status of any entries found on this report.</p>
<p><strong>Note:</strong> This report is only accessible to users with the PSB MANAGER security key.</p>
<p>To run the Unknown Action Status Report</p>
<ol type="1">
<li><p>At the <em>Bar Code Medication Administration Manager</em> menu, type <strong>U</strong>, and then press <strong>&lt;Enter&gt;</strong> to access the <em>Unknown Action Status Report</em> [PSBO XA] option. The associated screen then displays.</p></li>
</ol>
<p>Example: Unknown Action Status Report<br />
Report Criteria Screen</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/076.png)</p></td>
</tr>
</tbody>
</table>

# Running the Unknown Action Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="creating-a-listing-of-unknown-actions-cont." class="H2-Continued">Creating a listing of Unknown Actions (cont.)</h2>
<h2 id="section-4" class="H2-Continued"></h2></td>
<td><ol start="25" type="1">
<li><p>At the “Report Criteria” screen, enter the desired Start Date, Stop Date, Division, and Print to DEVICE fields. Note the Start Date defaults to Today minus 7 days, and the Stop Date defaults to today.</p></li>
<li><p>Press &lt;PF1&gt; E to run the report. A sample report is shown below.</p></li>
</ol>
<p>Example: Unknown Action Status Report</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/077.png)</p></td>
</tr>
</tbody>
</table>

# Using Immunizations Documentation by BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="pg59_P142" class="anchor"></span>\*\* With the release of patch PSB\*3.0\*142, BCMA2PCE Sunset, the Immunizations Documentation by BCMA application no longer documents BCMA immunization administrations in Patient Care Encounter (PCE).\*\*

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="validate-the-immunizations-documentation-by-bcma-nightly-task">Validate the Immunizations Documentation by BCMA Nightly Task</h2></td>
<td><p>The Immunizations Documentation by BCMA application is introduced with patches PSS*1*141 and PSB*3*47. Patch PSS*1*141 adds the ASSOCIATED IMMUNIZATION field (#9) to the PHARMACY ORDERABLE ITEM file (#50.7). A mapping relationship is created between the PHARMACY ORDERABLE ITEM file (#50.7) and the pointed-to immunization so that a record can be created in the V IMMUNIZATION file (#9000010.11) corresponding to the BCMA administration of an immunization.</p>
<p>Patch PSB*3*47 adds <em>Immunizations Documentation by BCMA Nightly Task</em> [PSB PX BCMA2PCE TASK] option to the <em>Bar Code Medication Administration Manager</em> [PSB MGR] menu. You can use this option to run a task which will create a record within Patient Care Encounter (PCE) for medications marked as given in BCMA that have been identified as immunizations.  The primary intended use of this option is to queue it as a nightly background task, which will process the previous day’s BCMA administrations of immunizations.</p>
<p>See the Immunizations Documentation by BCMA Release Notes for additional detail.</p>
<p>For each orderable item that is found in which there is an associated immunization, the program will display the patient name, immunization name, date of entry and the person who recorded the BCMA administration.</p>
<p>Once an immunization is found, the next line will display a result code.</p>
<ul>
<li><p>Result code 1 indicates a successful transmission of data to PCE.</p></li>
<li><p>Result codes -1, -2 and -3 indicate a problem filing the data to PCE.</p>
<ul>
<li><p>-1 is returned if there were errors in PCE but the data was filed as completely as possible. For example, error code -1 can occur if the nurse who recorded the administration in BCMA does not have a valid and current entry in the PERSON CLASS field (#8932.1).</p></li>
<li><p>-2 is returned if PCE could not find or create an entry in the VISIT file (#9000010).</p></li>
<li><p>-3 is returned if PCE was called incorrectly, which is indicative of a problem with this BCMA application.</p></li>
</ul></li>
</ul>
<p>If the task generates an error code, file a Remedy ticket.  If you don’t have access to Remedy please call the VA Service Desk at 1-888-596-4357 and they will file a ticket on your behalf.</p></td>
</tr>
</tbody>
</table>

# Using Immunizations Documentation by BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="validate-the-immunizations-documentation-by-bcma-nightly-task-cont." class="H2-Continued">Validate the Immunizations Documentation by BCMA Nightly Task (cont.)</h2>
<h2 id="section-5" class="H2-Continued"></h2></td>
<td><p>A message will be displayed if there is already a record on file for the combination of patient, entry date, and immunization type. Duplicate data will not be filed.</p>
<p>Example: Immunizations Documentation by BCMA Nightly Task [PSB PX BCMA2PCE TASK] Option</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/078.png)</p></td>
</tr>
</tbody>
</table>

# Customizing the BCMA GUI Tools Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-the-tools-menu-in-vista">Defining the Tools Menu in VistA</h2></td>
<td><p>BCMA provides a feature to define custom tools menus in VistA for use in the BCMA GUI. This allows users a convenient way to launch frequently used applications directly from within the BCMA GUI. Applications can be added to menus that correspond to the following levels: User, Location, Service, Division, System, and Package. The following is an example of a customized menu displayed in the BCMA GUI.</p>
<p>Example: Customized Tools Menu</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/079.png)</p>
<p>To define a custom tools menu for use in BCMA GUI</p>
<ol type="1">
<li><p>In VistA, select the <em>BCMA GUI Tool Menu Items</em> [PSB TOOL MENU ITEMS] option. The following menu appears:</p>
<p>1   User     USR  [choose from NEW PERSON]<br />
2   Location  LOC  [choose from HOSPITAL LOCATION]<br />
2.5 Service   SRV  [choose from SERVICE/SECTION]<br />
3   Division  DIV  [choose from INSTITUTION]<br />
4   System    SYS  [CTST.FO-XXXX.MED.VA.GOV]<br />
9   Package   PKG  [BAR CODE MED ADMIN]</p></li>
</ol>
<ol start="27" type="1">
<li><p>Enter a menu level (above) to customize, then press &lt;<strong>Enter</strong>&gt;. For example, 1 for User, 2 for Location, etc. When prompted, type the specific New Person, Hospital Location, etc., to which the custom menu will be assigned then press &lt;<strong>Enter</strong>&gt;.</p></li>
</ol>
<p><strong>Note:</strong> The lowest menu level defined here determines which menu level is loaded when the BCMA GUI is executed. For example, if the User and Division menu levels are both defined, the User menu displays in BCMA. When all menu items in the User level menu are deleted (using @ symbol), then the Division menu will display in BCMA.</p></td>
</tr>
</tbody>
</table>

# Customizing the BCMA GUI Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-the-tools-menu-in-vista-cont." class="H2-Continued">Defining the Tools Menu in VistA (cont.)</h2></td>
<td><p>To define a custom tools menu for use in BCMA GUI (cont.)</p>
<ol start="28" type="1">
<li><p>At the “Select Sequence” prompt, enter a sequence number for the menu item you want to add or edit, then press &lt;<strong>Enter</strong>&gt;. This number controls the order in the menu items are displayed in BCMA. 1 is the first item, 2 is the second item, etc. If adding a new menu item, answer <strong>Yes</strong> at the “Are you adding # as a new Sequence?” prompt. If editing an existing sequence, press &lt;<strong>Enter</strong>&gt; to confirm the sequence number shown.</p></li>
</ol>
<p><strong>Note</strong>: At the Select Sequence prompt, type <strong>?</strong> &lt;<strong>Enter</strong>&gt; to see a list of existing menu definitions for the selected level, or type <strong>??</strong> &lt;<strong>Enter</strong>&gt; to get extended help for this option.</p>
<ol start="29" type="1">
<li><p>At the “Name=Command:” prompt, enter the name of the menu option as you want it to display in the BCMA Tools menu, then an equal sign, then the command string used to run the application or web page, then press &lt;<strong>Enter</strong>&gt;. For example, Calculator=C:\WINDOWS\SYSTEM32\CALC.EXE.</p></li>
</ol>
<p><strong>Note</strong>: Be sure to specify the complete path or web address, including any parameters that must be passed to the executable.</p>
<p><strong>Note</strong>: In each menu item, you can place an ampersand character “&amp;” before the letter you want to designate as a keyboard shortcut. For example, &amp;Calculator would assign the letter C to be the keyboard shortcut for this menu item. The ampersand can be assigned to any letter in the menu option name.</p>
<ol start="30" type="1">
<li><p>Repeat steps 3 and 4 above for each menu option you want to add or edit at the selected menu level.</p></li>
</ol></td>
</tr>
</tbody>
</table>

Example: Command Strings for Customized Tools Menu

# Customizing the BCMA GUI Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="defining-the-tools-menu-in-vista-cont.-1" class="H2-Continued">Defining the Tools Menu in VistA (cont.)</h2></td>
<td><p>To define a custom tools menu for use in BCMA GUI (cont.)</p>
<ol start="31" type="1">
<li><p>When you have defined all desired menu options for a selected level, run the BCMA GUI and select the Tools menu and confirm the following:</p></li>
</ol>
<ul>
<li><p>All menu options are displayed in the order you want.</p></li>
<li><p>All menu options can be executed by clicking the mouse or using keyboard navigation, and any defined shortcut keys work as expected.</p></li>
<li><p>All menu options launch the correct application or web page.</p></li>
</ul></td>
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
<td><h2 id="learning-bcma-lingo">Learning BCMA Lingo</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA Acronyms and Terms
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Acronym/Term            | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Active                  | When a medication has been finished *and* verified, it becomes “active,” and displays on the VDL under the related Medication Tab. A nurse can then administer the medication to the patient. Under the IV Medication Tab, this information is listed in the Status column.                                                                                                                                                                                  |     |
| BCMA                    | Bar Code Medication Administration. A VistA software application used in VAMCs for validating patient information and medications against active medication orders *before* being administered to a patient.                                                                                                                                                                                                                                 |     |
| BCMA Clinical Reminders | A marquee located in the lower, right-hand corner of the VDL that identifies PRN medication orders needing effectiveness documentation. The setting is based on the “PRN Documentation” site parameter, and applies to current admissions or the site parameter timeframe (whichever is greater). A mouse-over list displays when the pointer is placed over the PRN Effectiveness Activity, or a full list is available by double clicking on the Activity. |     |
| CHUI                    | Character-based User Interface.                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| Client                  | An architecture in which one computer can get information from another. The Client is the computer that asks for access to data, software, or services.                                                                                                                                                                                                                                                                                                      |     |
| Clinician               | Nursing personnel who administer active medication orders to patients on a ward. In a VAMC, a number of teams may be assigned to take care of one ward, with specific rooms and beds assigned to each team.                                                                                                                                                                                                                                                  |     |
| Continuous Order        | A medication given continuously to a patient for the life of the order, as defined by the order Start and Stop Date/Time.                                                                                                                                                                                                                                                                                                                                    |     |
| CPRS                    | Computerized Patient Record System. A VistA software application that allows users to enter patient orders into different software packages from a single application. All pending orders that appear in the Unit Dose and IV packages are initially entered through the CPRS package. Clinicians, Managers, Quality Assurance Staff, and Researchers use this integrated record system.                                                     |     |
| ESig                    | Electronic Signature Code.                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
| FileMan                 | The VistA database management system.                                                                                                                                                                                                                                                                                                                                                                                                                        |     |
| Finish                  | The process in which the Pharmacist adds the information necessary to make the order active. For example: dispense drug, and start/stop date.                                                                                                                                                                                                                                                                                                                |     |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-lingo-cont." class="H2-Continued">Learning BCMA Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td>Definition</td>
<td></td>
</tr>
<tr class="even">
<td>Given</td>
<td colspan="2">When a medication is administered to a patient, it is considered to be “Given” and marked as such (with a “G”) in the Status column of the VDL.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td colspan="2"><strong>G</strong>raphical <strong>U</strong>ser <strong>I</strong>nterface.</td>
</tr>
<tr class="even">
<td>HRN</td>
<td colspan="2">Health Record Number – 6 digit patient identifier in IHS/Tribal facilities</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td colspan="2"><strong>I</strong>nternal <strong>E</strong>ntry <strong>N</strong>umber. The internal entry drug number entered by Pharmacy personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</td>
</tr>
<tr class="even">
<td>IHS</td>
<td colspan="2">Indian Health Service</td>
</tr>
<tr class="odd">
<td>Internal Entry Number</td>
<td colspan="2">Also called “IEN,” the internal entry drug number entered by Pharmacy personnel into the DRUG file (#50) to identify Unit Dose and IV medications.</td>
</tr>
<tr class="even">
<td>IV</td>
<td colspan="2">A medication given intravenously (within a vein) to a patient from an<br />
IV Bag. IV types include Admixture, Chemotherapy, Hyperal, Piggyback, and Syringe.</td>
</tr>
<tr class="odd">
<td>LIMITED ACCESS BCMA</td>
<td colspan="2">A mode in which BCMA can be accessed that provides medication administering users the ability to access patient records for non-medication administration documentation, review and reporting purposes without being at the patient’s bedside.</td>
</tr>
<tr class="even">
<td>MAH</td>
<td colspan="2"><strong>M</strong>edication <strong>A</strong>dministration <strong>H</strong>istory. A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</td>
</tr>
<tr class="odd">
<td>MAR</td>
<td colspan="2"><strong>M</strong>edication <strong>A</strong>dministration <strong>R</strong>ecord. The traditional, handwritten record used for noting when a patient received a medication. BCMA replaces this record with an MAH.</td>
</tr>
<tr class="even">
<td>Medication Administration History Report</td>
<td colspan="2"><strong>M</strong>edication <strong>A</strong>dministration <strong>H</strong>istory. A patient report that lists a clinician’s name and initials, and the exact time that an action was taken on an order (in a conventional MAR format). Each order is listed alphabetically by the orderable item. The Date column lists three asterisks (*) to indicate that a medication is not due. The report also lists information about when an order is placed “On Hold” and taken “Off Hold” by a provider, and the order Start and Stop Date/Time for the medication.</td>
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
<td><h2 id="learning-bcma-lingo-cont.-1" class="H2-Continued">Learning BCMA Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA Acronyms and Terms
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Acronym/Term       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |     |
| Medication Route   | Also called “Route” or “Med Route,” the method by which a patient receives medication (i.e., PO, IV, IM, ID, SQ, and SC). Each VAMC determines routes and associated abbreviations, which cannot exceed five characters in length. Otherwise they will *not* fit on bar code labels and the MAH.                                                                                                                                                                                      |     |
| Medication Tab     | Used to separate and view a type of active medication order (i.e., Unit Dose IV Push, IV Piggyback, and large-volume IVs) that needs to be adminstered to a patient. The Tab under which an order displays depends on how it was entered. The “alert light” on a Tab turns GREEN *only* when a medication order exists for the Schedule Type selected within the respective start/stop date and time selected on the BCMA VDL. If grayed out, then none exist.                    |     |
| Missing Dose       | A medication considered “Missing.” BCMA automatically marks this order type (with an “M”) in the Status column of the VDL after you submit a Missing Dose Request to the Pharmacy. If an IV bag displayed in the IV Bag Chronology display area of the VDL is *not* available for administration, you may mark the IV bag as a “Missing Dose” using the Missing Dose button or by right clicking the IV bag and selecting the Missing Dose command in the Right Click drop-down menu. |     |
| National Drug Code | Also called “NDC,” the number assigned by a manufacturer to each item/medication administered to a patient.                                                                                                                                                                                                                                                                                                                                                                           |     |
| NDC                | National Drug Code. The number assigned by a manufacturer to each item/medication administered to a patient.                                                                                                                                                                                                                                                                                                                                                              |     |
| On-Call Order      | A specific order or action dependent upon another order or action taking place *before* it is carried out. For example, “Cefazolin 1gm IVPB On Call to Operating Room.” Since it may be unknown when the patient will be taken to the operating room, the administration of the On-Call Cefazolin is dependent upon that event.                                                                                                                                                       |     |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-lingo-cont.-2" class="H2-Continued">Learning BCMA Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA Acronyms and Terms
|                               |                                                                                                                                                                                                                                                                                                                                                                  |     |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Acronym/Term                  | Definition                                                                                                                                                                                                                                                                                                                                                       |     |
| One-Time Order                | A medication order given one time to a patient such as a STAT or NOW a order. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time or until it is Given.                                                                                                                                             |     |
| Orderable Item                | A drug whose name does NOT have the strength associated with it (e.g., Acetaminophen 325 mg). The name with a strength is called the “Dispensed Drug Name.”                                                                                                                                                                                                      |     |
| Patient Transfer Notification | A message that displays when a patient’s record is opened or the Unit Dose or IVP/IVPB Medication Tab is viewed for the first time. It indicates that the patient has had a movement type (usually a transfer) within the site-definable parameter, and the last action for the medication occurred before the movement, but still within the defined timeframe. |     |
| PCE                           | Patient Care Encounter                                                                                                                                                                                                                                                                                                                               |     |
| Pending Order                 | An order entered by a provider through CPRS without Pharmacy personnel verifying the order.                                                                                                                                                                                                                                                                      |     |
| PRN Effectiveness List Report | A report that lists PRN medications administered to a patient that needs Effectiveness comments.                                                                                                                                                                                                                                                                 |     |
| PRN Order                     | The Latin abbreviation for Pro Re Nata. A medication dosage given to a patient on an “as needed” basis.                                                                                                                                                                                                                                              |     |
| Provider                      | Another name for the “Physician” involved in the prescription of a medication (Unit Dose or IV) to a patient.                                                                                                                                                                                                                                                    |     |
| PSB CPRS MED BUTTON           | The name of the security “key” that must be assigned to nurses who document verbal- and phone-type STAT and medication orders using the CPRS Med Order Button on the BCMA VDL.                                                                                                                                                                                   |     |
| PSB INSTRUCTOR                | The name of the security “key” that must be assigned to nursing instructors, supervising nursing students, so they can access user options within BCMA V. 3.0.                                                                                                                                                                                                   |     |
| PSB MANAGER                   | The name of the security “key” that must be assigned to managers so they can access the PSB Manager options within BCMA V. 3.0.                                                                                                                                                                                                                                  |     |
| PSB STUDENT                   | The name of the security “key” that must be assigned to nursing students, supervised by nursing instructors, so they can access user options with BCMA V. 3.0. This key requires that a nursing instructor sign on to BCMA V. 3.0.                                                                                                                               |     |
| PSB UNABLE TO SCAN            | The name of the security “key” that must be assigned to allow the user to run the Unable to Scan Detailed and Summary reports.                                                                                                                                                                                                                                   |     |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="learning-bcma-lingo-cont.-3" class="H2-Continued">Learning BCMA Lingo (cont.)</h2></td>
<td>The alphabetical listing, in this section, is designed to familiarize you with the many acronyms and terms used throughout this manual.</td>
</tr>
</tbody>
</table>
Example: Alphabetical Listing of BCMA Acronyms and Terms
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Acronym/Term</td>
<td>Definition</td>
<td></td>
</tr>
<tr class="even">
<td>Refused</td>
<td colspan="2">The status for an IV bag or Unit Dose to indicate that the patient refused to take the dose.</td>
</tr>
<tr class="odd">
<td>RPMS</td>
<td colspan="2">Resource and Patient Management System – health information system for IHS, analogous to VistA</td>
</tr>
<tr class="even">
<td>Schedule Type</td>
<td colspan="2">Identifies the type of schedule (i.e., Continuous, PRN, On-Call, and One-Time) for the medication being administered to a patient.</td>
</tr>
<tr class="odd">
<td>Security Keys</td>
<td colspan="2">Used to access specific options within BCMA V. 3.0 that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="even">
<td>Solution</td>
<td colspan="2">A homogeneous mixture of two or more substances. For IVs, these would be liquids.</td>
</tr>
<tr class="odd">
<td>Start Date/Time</td>
<td colspan="2">The date and time that a medication is scheduled for administration to a patient.</td>
</tr>
<tr class="even">
<td>STAT Order</td>
<td colspan="2">A medication order given immediately to a patient, entered as a One-Time order by providers and pharmacists. This order type displays for a fixed length of time on the VDL, as defined by the order Start and Stop Date/Time.</td>
</tr>
<tr class="odd">
<td>Stop Date/Time</td>
<td colspan="2">The date and time that a medication order will expire, and should no longer be administered to a patient.</td>
</tr>
<tr class="even">
<td>Strength</td>
<td colspan="2">The degree of concentration, distillation, or saturation of a medication.</td>
</tr>
<tr class="odd">
<td>Unit Dose</td>
<td colspan="2">A medication given to a patient, such as tablets or capsules.</td>
</tr>
<tr class="even">
<td>VDL</td>
<td colspan="2"><strong>V</strong>irtual <strong>D</strong>ue <strong>L</strong>ist. An on-line “list” used by clinicians when administering active medication orders (i.e., Unit Dose, IV Push, IV Piggyback, and large-volume IVs) to a patient. This is the Main Screen in BCMA V. 3.0.</td>
</tr>
<tr class="odd">
<td>Verify</td>
<td colspan="2">When a nurse or a Pharmacist confirms that a medication order is accurate and complete, according to the information supplied by the Provider.</td>
</tr>
<tr class="even">
<td>Virtual Due List</td>
<td colspan="2">Also called “VDL,” an on-line list used by clinicians when administering active medication orders to a patient. This is the Main Screen in<br />
BCMA V. 3.0.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td colspan="2"><strong>V</strong>eterans Health <strong>I</strong>nformation <strong>S</strong>ystems and <strong>T</strong>echnology <strong>A</strong>rchitecture.</td>
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
<tbody>
<tr class="odd">
<td><h2 id="defining-and-setting-site-parameters-for-ihs">Defining and Setting Site Parameters for IHS</h2></td>
<td><p>The Indian Health Service (IHS) project requires the addition of a new parameter to the BCMA Parameters application. The IHS user-specified parameter entries are stored at the Division level and override corresponding System level values.</p>
<h3 id="working-with-the-parameters-tab-1">Working with the Parameters Tab</h3>
<p>If the operating environment is Resource and Patient Management System (RPMS), the tab entitled “IHS” is added to the parameters application.</p>
<p>You can activate the IHS Tab by placing the cursor over the Tab and clicking once on it or by selecting Alt-H to access it directly. Doing so activates the site parameters for this Tab.</p>
<p>This section describes the field available on the IHS Tab.</p>
<p>Example: Site Parameters Available<br />
IHS Tab</p>
<p>![](bcma-version-3-manager-s-user-manual-psb-3-142/080.png)</p>
<p><strong>IHS Patient ID Label:</strong> This text entry field allows you to enter a patient ID textual label of up to 5 characters if the operating environment is RPMS. The contents of this field are displayed throughout the BCMA GUI forms and reports.</p></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Accessing
Bar Code Medication Administration
Manager Menu, 31
CHUI BCMA Manager Menu Screen, 31
Administration Area, Parameters Tab, 14
B
Background, technical information, 2
Bar Code Medication Administration Manager
Menu Screen, 31
Bar Code Options Area, Parameters Tab, 14
BCMA V. 3.0
Benefits, 1
Clinical Reminders, 16
Idle Timeout, 15
Lingo, 45-49
Site Parameters Main Screen with  
Facility Tab Selected, 10
Site Parameters Opening Screen, 8
Target Audience, 1
Benefits of This Manual, 1
C
Checking Drug IEN Code for Unit Dose
Medications, 33-34
CHUI BCMA
Manager Menu Screen, 31
On-line Help, 4
Connect to Selection Dialog Box, 5
Conventions Used in This Manual
Keyboard Responses, 2
Menu Options, 3
Mouse Responses, 2
Notes, 3
Screen Captures, 3
Tips, 3
User Responses, 3
Creating
Default Answer List for Injection Sites, 24
Default Answer List for Reason Medication  
Given PRN, 19-21
Default Answer List for Reason Medication  
Held, 22
Default Answer List for Reason Medication  
Refused, 23
Follow-up Message for a Missing Dose  
Request, 46-48
D
Default
Answer Lists Tab, 17-24
Answer Lists Tab Selected and List Names  
Provided Screen, 17
Parameter Settings, Resetting for a User,  
39-40
Defining and Setting Site Parameters for IHS, 59
Defining and Updating Site Parameters for
Your Division, 9-29
Dermal Site History Max Days, 16
Division Selection Dialog Box, 9
Documenting and Displaying Anatomic Location, 24
Drug File Inquiry Screen, 33
Drug IEN Code for Unit Dose Medications,
Verifying, 33-34
E
Enable CPRS Med Order Button, Selecting, 16
Error Message When BCMA Not Active for
Your Site, 11
F
Facility Tab, 11
Five Rights Override Parameters, 14
Follow-up Message
Creating for a Missing Dose Request, 46-48
G
GUI BCMA Site Parameters Application
Desktop Icon, 5
I
Identifying Scanning Problems Using the
Trouble shoot Med Log, 41-43
Include Comments Parameter, 12-13
Information Message When Prompts Default
Setting Changed, 29
Introducing
BCMA V. 3.0, 1
This Manual, 3
IV Parameters Tab
IV Type Area, 27
Location Area, 26
Prompts Area, 28-29
K
Keyboard Response Conventions, 2
Keyed Entry Timing Parameter, 30

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

L
Location Area, IV Parameters Tab, 26
M
Mail Groups Area, Parameters Tab, 13
Med Hist Days Back Parameter, 12-13
Med Log
Identifying Scanning Problems, 41-43
Trouble Shooter Screens, 41-42
Menu Option Conventions, 3
Misc. Options Area, Parameters Tab, 15
Missing Dose
Notification, 13a
Creating a Follow-up Message, 46-48
Request Entry Screen, 47
Request Selection Screen, 46
Mouse Response Conventions, 2
N
Notes Conventions, 3
O
Online Help, CHUI, 4
Order Validation Screen, Trouble Shoot Med
Log, 43
Other Sources of Information, 2
Output Devices Area, Parameters Tab, 12-13
P
Parameters Tab
Administration Area, 14
Bar Code Options Area, 14
Mail Groups Area, 13
Misc. Options Area, 15-16
Output Devices Area, 12-13
Reports Area, 12-13
Virtual Due List Setup Area, 15
Patient Transfer Notification, 15
Pharmacy Reasons Needed Selection Table, 37
PRN Documentation, 16
Prompts Area, IV Parameters Tab, 28-29
Prompts Drop-Down List Box for Additive
Field, 28
PSB CPRS MED BUTTON Security key, 16
PSB MANAGER Security Key, 1
PSB Unable to Scan Security Key, 56
R
Related Documentation, 2
Reports Area, Parameters Tab, 12-13
Reset User Parameters Sequence Screen, 39
Resetting a User’s Default Parameter Settings,
39-40
Responding to Missing Dose Requests, 46-48
Results of Drug File Inquiry Screen, 34
S
Screen Capture Conventions, 3
Security Keys
PSB CPRS MED BUTTON, 16
PSB MANAGER, 1
Select Division Dialog Box, 7
Selecting a Default Answer Lists Name Screen,
18
Setting Site Parameters for GUI BCMA V. 3.0,
5
Signing on to GUI BCMA Site Parameters  
Application, 5-8
For VAMCs with Multiple Divisions, 7
Site Parameters
Available Using Parameters Tab, 12-15
Available When IV Parameters Tab Selected  
Screen, 25
Suggested Default Answer Lists
For Injection Sites, 24
For Reason Medication Given PRN, 20-21
For Reason Medication Held, 22
For Reason Medication Refused, 23
T
Tabs
Facility, 11
Default Answer Lists, 17-24
IV Parameters, 25-29
Parameters, 12-16
Target Audience for This Manual, 1
This Manual
Benefits of, 1
Conventions Used, 2-3
Other Sources of Information, 2
Related Documentation, 2
Target Audience, 1
Tips Conventions, 3
Trouble Shoot Med Log, Using, 41-43  
Type Drop-Down List Box for IV Type Area, 27

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

U
Unable to Scan Mail Group, 13
Unit Dose Medications
Verifying the Drug IEN Code for, 33
Updating and Defining Site Parameters for  
Your Division, 9-29
User Response Conventions, 3
Using the Trouble Shoot Med Log, 41-43
V
Verifying the Drug IEN Code for Unit Dose
Medications, 33-34
Virtual Due List Setup Area, Parameters Tab, 15
VistA Sign-on Dialog Box, 5
W
Ward Drop-Down List Box for Location Area,
26
Warning Message
About Updates to Parameters Being  
Immediate, 8
That Fields in Inpatient Medications V. 5.0  
Changed, 29
When All BCMA Users Are Being Disabled  
from Your Division, 11
Working with
Default Answer Lists Tab, 17-24
Facility Tab, 11
IV Parameters Tab, 25-29
Parameters Tab, 12-16
