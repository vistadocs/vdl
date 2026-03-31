---
title: BCMA Version 3 GUI User Manual - Appendix D (508 Compliance)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: GUI  - Appendix D (508 Compliance)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*508
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "- [Appendix D: 508 Compliance](#appendix-d-508-compliance) - [Appendix D: 508 Compliance](#appendix-d-508-compliance-1) - [Appendix D: 508 Compliance](#appendix-d-508-compliance-2) - [Appendix D: 508 Compliance](#appendix-d-508-compliance-3) - [Appendix D: 508 Compliance](#appendix-d-508-compliance-"
audience: 
keywords: 
  - strong
  - table
  - compliance
  - appendix
  - bcma
  - class
  - style
  - width
  - contents
  - cancel
page_count: 0
word_count: 4902
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_appendixd_508_compliance_r0111.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_appendixd_508_compliance_r0111.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

# Appendix D: 508 Compliance


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Appendix D: 508 Compliance](#appendix-d-508-compliance)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-1)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-2)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-3)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-4)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-5)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-6)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-7)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-8)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-9)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-10)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-11)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-12)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-13)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-14)
- [Appendix D: 508 Compliance](#appendix-d-508-compliance-15)
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 67%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="what-is-508-compliance">What Is 508 Compliance?</h2></th>
<th><p>Section 508 of the Rehabilitation Act of 1973 and Rehabilitation Act Amendments of 1998 mandates that all software developed by federal agencies allow access to and use of information and data by individuals with disabilities. The Bar Code Medication Administration (BCMA) V. 3.0 graphical user interface (GUI) is updated to ensure 508 Compliance with respect to the requirements of the Section 508 Checklist for Software Applications and Operating Systems (see<br />
<mark>REDACTED</mark>.</p>
<p>Section 508 enhancements to BCMA ensure accessibility for color-blind, mobility-impaired, and visually-impaired users, without impacting software usability for our primary audience of users—sighted nurses who administer medications to patients.</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"></td>
</tr>
<tr class="even">
<td><h2 id="definitions-used-in-508-compliance">Definitions Used in 508 Compliance </h2></td>
<td><p>The following definitions are used in the 508 Compliance project:</p>
<ul>
<li><p><strong>508 Compliant User</strong> — A user with one or more of the following disabilities (color-blind, mobility‑impaired, visually-impaired) who requires access to software applications through the use of adaptive technology and tools.</p></li>
<li><p><strong>Adaptive technology</strong> — Products that help people who cannot use regular versions of products; primarily people with physical disabilities such as limitations to vision and mobility. Such products include alternate pointing devices, screen readers, screen magnifiers, voice recognition technology, etc.</p></li>
<li><p><strong>Clear Focus</strong> — A well-defined on-screen indication of the current application focus so that keyboard users and adaptive technology can track focus and focus changes.</p></li>
<li><p><strong>Color-blind</strong> — A color vision deficiency in humans, resulting in the inability to perceive differences between some or all colors that other people can distinguish.</p></li>
<li><p><strong>Mobility-impaired</strong> — A user with a physical impairment or limitation, such that they require alternative pointing devices, limited keyboard access, keyboard-only access, voice recognition technology, or a combination of the above, in order to use a computer.</p></li>
<li><p><strong>Primary User</strong> — Refers to the primary user of BCMA, a sighted nurse that administers medications to patients at bedside.</p></li>
<li><p><strong>Visually-impaired</strong> — A user that has vision loss or impairment such that they require adaptive technologies such as screen readers or magnifiers in order to read a computer screen. Includes partially sighted, low vision, legally blind, or totally blind users.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 68%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="hardware-and-software-interfaces-for-508-compliance">Hardware and Software Interfaces for 508 Compliance </h2></th>
<th><p>Section 508 Compliance standards do not specifically mention the use of screen readers; however, the reference to a clear on-screen focus allows assistive technology, such as screen readers, to track focus and focus changes in order to read the screen.</p>
<p>The 508 standard states that sufficient information about a user interface element, including the identity, operation, and state of the element, be available to assistive technology. The screen reader must be able to distinguish and read all controls such as checkboxes, menus, and toolbars to the user. When electronic forms are used, the form must allow people using assistive technology to access the information, field elements, and functionality required for completion and submission of the form, including all directions and cues.</p>
<p>No specific brand of screen reader software is specified or standardized for Veterans Administration (VA) users. For development purposes, the popular Job Access With Speech (JAWS) software (by Freedom Scientific) was used to test screen reader compatibility. Other screen readers may perform differently. Since screen reader software is designed to verbalize data out loud, headphones must be used in conjunction with any screen reader, in order to protect confidential VA patient data—in accordance with the Health Insurance Portability &amp; Accountability Act of 1996 (HIPAA) laws that guarantee security and privacy of health information.</p>
<p>BCMA supports Microsoft<sup>®</sup> Active Accessibility<sup>®</sup> (MSAA), which is built into the Windows operating system. MSAA provides a standard, consistent mechanism for exchanging information between applications and assistive technologies, such as allowing applications to expose screen readers to the type, name, location, and current state of all objects, and notifying screen readers of Windows events that lead to user interface changes.</p>
<p>Any adaptive technology used in conjunction with BCMA must be installed and configured separately from BCMA. Users utilizing adaptive technology must have sufficient RAM and disk space required by their individual hardware and software configurations.</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="how-it-works-in-bcma"><br />
<br />
<br />
<br />
How It Works in BCMA </h2></td>
<td><p>Functionality for 508 Compliance is added to BCMA, including audible signals, keyboard navigation, clear focus, consistent use of color, images, and text, and screen reader compatibility as appropriate.</p>
<p>There are two types of users for BCMA: those who administer medications and those who do not administer medications.</p>
<ul>
<li><p><strong>Users who administer medications</strong> are assumed to be not visually-impaired but may be mobility-impaired and/or color-blind. Those users may use keyboard navigation, alternative pointing devices, or voice input technology.</p></li>
<li><p><strong>Users who do not administer medications</strong> may be color-blind, visually-impaired, or mobility-impaired. Those users may use screen readers, screen magnifiers, keyboard input, alternative pointing devices, or voice input technology.</p></li>
</ul>
<p>The following features are included in BCMA Section 508 Compliance functionality.</p>
<h3 id="keyboard-navigation-and-clear-focus">Keyboard Navigation and Clear Focus</h3>
<p>Section 508 Compliance standards require that all product functions be executable from the keyboard, and that a well-defined indication of current on-screen focus be provided. Keyboard navigation and clear focus work together to assist mobility-impaired users.</p>
<h3 id="reports">Reports</h3>
<p>Currently, all BCMA reports are text-based and screen reader compatible, but the reports may not read in a logical order for comprehension by visually-impaired users.</p>
<h3 id="use-of-color">Use of Color</h3>
<p>User-selected contrast and color selections and other individual display attributes are not overridden.</p>
<p>Color is used to enhance, but color coding is not used as the only means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. If color is used to convey information, the information is also displayed in another format.</p>
<h3 id="use-of-images">Use of Images</h3>
<p>Images are not used alone to convey information; the information is also available in text format. When images are used to identify controls, status indicators, or other programmatic elements, the meaning assigned to those images is used consistently throughout BCMA.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 67%" />
<col style="width: 2%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="how-it-works-in-bcma-continued" class="H2-Continued"><br />
<br />
<br />
<br />
How It Works in BCMA (Continued)</h2></td>
<td><h3 id="use-of-text">Use of Text</h3>
<p>All textual information on the screen is readable by assistive technologies. Note that this is implemented only in the areas designated for screen reader support.</p>
<h3 id="use-of-sounds">Use of Sounds</h3>
<p>Along with an informational message, an audible “beep” will sound 30 seconds, 20 seconds, and 10 seconds prior to timeout of BCMA because the application is idle. This time limit is set in the “BCMA Idle Timeout In Minutes” field on the Parameters Tab of the BCMA Site Parameters screen.</p>
<h3 id="alternate-methods-for-accessing-information">Alternate Methods for Accessing Information</h3>
<p>For features that are not screen reader compatible, an alternate method to access the same information is provided.</p>
<ul>
<li><p>For example, the Cover Sheet is not screen reader compatible, but all information is accessible via Cover Sheet reports.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><strong>Keyboard Navigation and Clear Focus</strong></td>
<td><p>508 Compliance features include keyboard navigation and clear focus for the features and elements listed below. At a minimum, navigation via use of arrow keys and Tab and Shift+Tab is provided.</p>
<ul>
<li><p>All Menus</p></li>
<li><p>All Dialogs</p></li>
<li><p>All Reports</p></li>
<li><p>Virtual Due List (VDL)</p></li>
<li><p>Cover Sheet</p></li>
<li><p>Read-Only mode</p></li>
<li><p>BCMA Site Parameter Application</p></li>
</ul>
<p>Although keyboard shortcuts (hotkeys) are not a Section 508 Compliance requirement, they are included, where possible, to assist both mobility-impaired and visually-impaired users, depending on the complexity of the window/object and level of difficulty to implement.</p>
<p>Since focus cannot be set on the Flag button on the VDL, the Patient Flag option is added to the View menu. This is in addition to the current documented keyboard shortcut of Ctrl+F.</p>
<p>The Cover Sheet and medication tabs (Unit Dose, IVP/IVPB, IV) do not get focus via keyboard navigation; however, there are two alternate methods to access them, through menu options (View, Med Tab) and function keys (F9, F10, F11, F12).</p></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="screen-reader-support"><br />
<br />
<br />
<br />
Screen Reader Support</h2></td>
<td><h3 id="features-supported">Features Supported</h3>
<p>Screen reader support is implemented in the functional areas listed below. BCMA can now recognize whether the JAWS software is running and loads special code components that enhance screen reader compatibility. The following features were implemented in order to facilitate JAWS screen reader support:</p>
<ul>
<li><p>Focus to all fields (edit and read-only) to provide screen reader support for all textual information on the dialog.</p></li>
<li><p>Tab order adjusted in order to provide focus on read-only information.</p></li>
<li><p>Labels are linked to fields so that the screen reader reads the field label and data pair each time the field is accessed.</p></li>
<li><p>Check box and radio button controls are placed into logical groups where necessary, so that the screen reader reads the group/field name, control, state of the control, and data.</p></li>
<li><p>Hot keys are provided for menu options, buttons, and groups.</p></li>
<li><p>On the BCMA Patient Lookup dialog, a dual mode is provided for JAWS users, such that a special grid is displayed that allows the screen reader to recognize and verbalize the Patient Name when moving horizontally across data in the Patient Lookup grid.</p></li>
<li><p>On the BCMA VDL, a dual mode is provided for JAWS users, such that a special grid is displayed that allows the screen reader to recognize and verbalize the Dispense Drug when moving horizontally across data in the VDL.</p></li>
</ul>
<h6 id="bcma-gui-client-application">BCMA GUI Client Application:</h6>
<ul>
<li><p>All Menus and options in Read-Only mode</p></li>
<li><p>All Menus and options in Limited Access mode</p></li>
<li><p>Patient Lookup dialog</p></li>
<li><p>Patient Confirmation dialog</p></li>
<li><p>All Report criteria dialog boxes</p></li>
<li><p>All Reports displayed on the screen</p></li>
<li><p>Scan Patient Wristband dialog</p></li>
<li><p>Scan Medication dialog</p></li>
<li><p>VDL and Medication tabs (Unit Dose, IVP/IVPB, IV)</p></li>
</ul>
<ul>
<li><p>Unable to Scan dialog</p></li>
<li><p>PRN Effectiveness log</p></li>
</ul>
<ul>
<li><p>Online Help</p></li>
</ul>
<p><strong>Note:</strong> The Cover Sheet is not screen reader compatible at this time.</p></td>
</tr>
<tr class="even">
<td></td>
<td><h6 id="bcma-site-parameters-application">BCMA Site Parameters Application</h6>
<ul>
<li><p>Facility tab</p></li>
<li><p>Parameters tab</p></li>
<li><p>Default Answers List tab</p></li>
<li><p>IV Parameters tab</p></li>
<li><p>Online Help</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section"><br />
</h2></td>
<td><h3 id="features-not-supported">Features Not Supported</h3>
<p>The following feature does <u>not</u> provide screen reader support:</p>
<ul>
<li><p>CPRS Med Order Button</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys"><br />
Hot Keys</h2></td>
<td><p>The following keyboard shortcuts (hot keys) are included to assist both mobility-impaired and visually-impaired users. The table below lists all hot keys available for BCMA.</p>
<p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>File Alt+F</p>
<p>Open Patient Record Alt<strong>+</strong>F+O</p>
<p>BCMA-Patient Select</p>
<p>Ok Alt+O</p>
<p>Cancel Alt+C</p>
<p>BCMA-Patient Confirmation</p>
<p>Yes Alt+Y</p>
<p>Cancel Alt+C</p>
<blockquote>
<p>Open (Limited Access) Alt+F+L</p>
</blockquote>
<p>BCMA-Patient Select</p>
<p>Ok Alt+O</p>
<p>Cancel Alt+C</p>
<p>BCMA-Patient Confirmation</p>
<p>Yes Alt+Y</p>
<p>Cancel Alt+C</p>
<p>Open (Read Only) Alt+F+R</p>
<p>BCMA-Patient Select</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>BCMA-Patient Confirmation</p>
<p>Yes Alt+Y</p>
<p>Cancel Alt+C</p>
<blockquote>
<p>Close Patient Record Alt+F+C</p>
<p>Edit Med Log Alt+F+E</p>
<p>Ok Alt+O</p>
<p>Cancel Alt+C</p>
<p>Exit Alt+F+X</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>View Alt+V</p>
<p>Med Tab Alt+V+M</p>
<p>Coversheet Alt+V+M+C F9</p>
<p>Unit Dose Alt+V+M+U F10</p>
<p>IVP/IVPB Alt+V+M+I F11</p>
<p>IV Alt+V+M+V F12</p>
<p>Allergies Alt+V+G</p>
<p>Print Alt+V+G+P</p>
<p>Next Alt+V+G+N</p>
<p>Cancel Alt+V+G+C</p>
<p>Patient Demographics Alt+V+P</p>
<p>Print Alt+V+P+P</p>
<p>Next Alt+V+P+N</p>
<p>Cancel Alt+V+P+C</p>
<p>Flag Ctrl+F</p>
<p>Reports Alt+R</p>
<blockquote>
<p>Administration Times Alt+R+A</p>
<p>Cover Sheet Alt+R+C</p>
<p>Medication Overview Alt+R+C+E</p>
<p>PRN Overview Alt+R+C+R</p>
<p>IV Overview Alt+R+C+O</p>
</blockquote>
<p>Expired/DC’d/Expiring</p>
<p>Orders Alt+R+C+X</p>
<p>Due List Alt+R+D</p>
<p>IV Bag Status Alt+R+B</p>
<p>Medication Admin History Alt+R+H</p>
<p>Medication Log Alt+R+L</p>
<p>Medication Therapy Alt+R+T</p>
<p>Medication Variance Log Alt+R+V</p>
<p>Missed Medications Alt+R+M</p>
<p>PRN Effectiveness List Alt+R+P</p>
<p>Unable to Scan (Detailed) Alt+R+N</p>
<p>Unable to Scan (Summary) Alt+R+S</p>
<p>Unknown Actions Alt+R+U</p>
<p>Vitals Cumulative Alt+R+I</p>
<p>On All Reports</p>
<p>Preview Alt+V</p>
<p>Print Alt+P</p>
<p>Cancel Alt+C</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-1" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>Due List Alt+D</p>
<p>Add Comment Alt+D+A</p>
<p>Display Order Alt+D+O F4</p>
<p>Mark Alt+D+M</p>
<p>Held Alt+D+M+H</p>
<p>Undo Alt+D+M+U</p>
<p>Refused Alt+D+M+R</p>
<p>Removed Alt+D+M+E</p>
<p>Med History Alt+D+E</p>
<p>Preview Alt+D+E+V</p>
<p>Print Alt+D+E+P</p>
<p>Cancel Alt+D+E+C</p>
<p>Missing Dose Alt+D+I</p>
<p>Submit Alt+D+I+S</p>
<p>Cancel Alt+D+I+C</p>
<p>PRN Effectiveness Alt+D+P</p>
<p>Unable To Scan Alt+D+U</p>
<p>OK Alt+D+U+O</p>
<p>Cancel Alt+D+U+C</p>
<p>Unable To Scan-Create WS Alt+D+W</p>
<p>Take Action on Bag Alt+D+T</p>
<p>Sort By Alt+D+S</p>
<p>Status Alt+D+S+S</p>
<p>Verifying Nurse Alt+D+S+V</p>
<p>Hospital Self Med Alt+D+S+H (Unit Dose only)</p>
<p>Type Alt+D+S+T</p>
<p>Active Medication Alt+D+S+A (Unit Dose only)</p>
<p>Medication/Solution Alt+D+S+A (IVP/IVPB and IV)</p>
<p>Dosage Alt+D+S+D (Unit Dose only)</p>
<p>Infusion Rate Alt+D+S+I (IVP/IVPB and IV)</p>
<p>Route Alt+D+S+R</p>
<p>Administration Time Alt+D+S+M (Unit Dose and IVP/IVPB)</p>
<p>Last Action Alt+D+S+L (Unit Dose and</p>
<p>IVP/IVPB)</p>
<p>Bag Information Alt+D+S+B (IV only)</p>
<p>Refresh Alt+D+R F5</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-2" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>Tools Alt+S</p>
<p>Notepad Alt+S+N</p>
<p>Options Alt+S+O</p>
<p>OK Alt+S+O+O</p>
<p>Cancel Alt+S+O+C</p>
<p>Help Alt+H</p>
<p>Contents and Index Alt+H+C F1</p>
<p>Index Alt+H+I</p>
<p>About BCMA Alt+H+A</p>
<p><strong><u>Tool Bar Hot Key (Alt)</u></strong></p>
<p>Missing Dose Alt+I</p>
<p>Submit Alt+I+S</p>
<p>Cancel Alt+I+C</p>
<p>Medication Log Alt+L</p>
<p>Medication Admin History Alt+E</p>
<p>Allergies Alt+G</p>
<p>Print Alt+G+P</p>
<p>Next Alt+G+N</p>
<p>Cancel Alt+G+C</p>
<p>CPRS Med Order Alt+M</p>
<p>Review/Sign Alt+M+R</p>
<p>Order Alt+M+O</p>
<p>Cancel Alt+M+C</p>
<p>Flag Ctrl+F</p>
<p><strong><u>Group Box Hot Key (Alt)</u></strong></p>
<p>Virtual Due List Parameters: Start Time Alt+A</p>
<p>Virtual Due List Parameters: Stop Time Alt+O</p>
<p>Schedule Types Continuous Alt+C</p>
<p>Schedule Types PRN Alt+P</p>
<p>Schedule Types On Call Alt+N</p>
<p>Schedule Types One-Time Alt+T</p>
<p><strong><u>Edit Box on VDL Hot Key (Alt)</u></strong></p>
<p>Enable Scanner Alt+B</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-3" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong>Note:</strong> The right-click option is simulated by selecting the Context Menu Key followed by the corresponding hot key listed below for each option.</p>
<p><strong>Right</strong></p>
<p><strong>Click</strong></p>
<p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>Add Comment A</p>
<p>Display Order +O F4</p>
<p>Print +O+P</p>
<p>Next +O+N</p>
<p>Cancel +O+C</p>
<p>Unable to Scan +U</p>
<p>OK +O</p>
<p>Cancel +C</p>
<p>Unable to Scan - Create WS +W</p>
<p>OK W+O</p>
<p>Cancel W+C</p>
<p>Mark +M</p>
<p>Held +M+H</p>
<p>Undo +M+U</p>
<p>Refused +M+R</p>
<p>Removed +M+E</p>
<p>Med History +E</p>
<p>Preview +E+V</p>
<p>Print +E+P</p>
<p>Cancel +E+C</p>
<p>Missing Dose +I</p>
<p>Submit +S</p>
<p>Cancel +C</p>
<p>PRN Effectiveness +P</p>
<p>Ok +O</p>
<p>Cancel +C</p>
<p>Med History +M</p>
<p>Exit +E</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-4" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong>Popup</strong></p>
<p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>BCMA-Unable to Scan</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Confirmation</p>
<p>Yes Alt+Y</p>
<p>No Alt+N</p>
<p>Error</p>
<p>OK Alt+O</p>
<p>Information</p>
<p>OK Alt+O</p>
<p>Injection Site Selection Dialog</p>
<p>Cancel Alt+C</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-5" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong>Popup</strong></p>
<p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>Medication Log</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Med History Alt+E</p>
<p>Adding a Comment Alt+T</p>
<p>Medication Verification</p>
<p>Verify Medication</p>
<p>Submit Alt+S</p>
<p>Verify Five Rights</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Medication Verification</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Medication Verification</p>
<p>Submit Alt+S</p>
<p>Multiple Dose</p>
<p>Done Alt+D</p>
<p>Cancel Alt+C</p>
<p>Multiple/Fractional Dose</p>
<p>Done Alt+D</p>
<p>Cancel Alt+C</p>
<p>Multiple Orders for Scanned Drug</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-6" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong>Popup</strong></p>
<p><strong><u>Menu Sub Menu Hot Key (Alt) Function Key</u></strong></p>
<p>Order Administration Cancelled</p>
<p>OK Alt+O</p>
<p>Quantity/Units Dialog</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Scan IV</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p>
<p>Ward Stock Dialog</p>
<p>OK Alt+O</p>
<p>Cancel Alt+C</p></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="hot-keys-continued-7" class="H2-Continued"><br />
Hot Keys<br />
(Continued)</h2></td>
<td><p><strong>BCMA Site Parameters</strong></p>
<p><strong>Main Tab Hot Keys</strong></p>
<p><strong><u>Action Hot Key</u></strong></p>
<p>Facility Alt+A</p>
<p>Parameters Alt+P</p>
<p>Default Answer Lists Alt+D</p>
<p>IV Parameters Alt+V</p>
<p><strong>BCMA Site Parameters</strong></p>
<p><strong>Facility Tab Hot Keys</strong></p>
<p><strong><u>Action Hot Key</u></strong></p>
<p>BCMA On-Line Alt+O</p>
<p>Navigate through Read-Only fields Shift+Tab and Tab</p>
<p><strong>BCMA Site Parameters</strong></p>
<p><strong>Parameters Tab Hot Keys</strong></p>
<p><strong><u>Action Hot Key</u></strong></p>
<p>Output Devices <strong>Alt+</strong>E</p>
<p>Mail Groups Alt+M</p>
<p>Reports Alt+R</p>
<p>Bar Code Options Alt+B</p>
<p>5 Rights Override Alt +G</p>
<p>Administration Alt<strong>+</strong>N</p>
<p>Allowable Time Limits (In Minutes) Alt+L</p>
<p>Virtual Due List Default Times Alt+T</p>
<p>Include Schedule Types Alt<strong>+</strong>S</p>
<p>Misc Options Alt+O</p>
<p><strong>BCMA Site Parameters</strong></p>
<p><strong>Default Answer Lists Tab Hot Keys</strong></p>
<p><strong><u>Action Hot Key</u></strong></p>
<p>List Name Alt+N</p>
<p>Save List Alt+S</p>
<p><strong>BCMA Site Parameters</strong></p>
<p><strong>IV Parameters Tab Hot Keys</strong></p>
<p><strong><u>Action Hot Key</u></strong></p>
<p>Location Alt+L</p>
<p>IV Type Alt+T</p>
<p>Prompts Alt+R</p></td>
</tr>
<tr class="even">
<td><h2 id="section-1" class="H2-Continued"></h2></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix D: 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="jaws-configuration-files"><br />
JAWS Configuration Files</h2></td>
<td><p>JAWS is a screen reader application that enables a computer to verbally describe the controls and content of computer applications. JAWS enables the visually-challenged user to navigate BCMA to complete necessary tasks.</p>
<p>Developers have created specialized scripts and software components that enable JAWS to work more effectively with BCMA. As part of the BCMA PSB*3*42 release, Common_Files.zip is needed to support JAWS communication with BCMA. The zip file is found at</p>
<p><mark>REDACTED</mark>. VA508Runtimes.zip contains VA508Runtimes.exe. Run VA508Runtimes.exe to put the following files in \Program Files\Vista\ Common Files. JAWS 9.0 or later is recommended.</p>
<p>It is best for JAWS users stay up to date with the latest releases of the product.</p>
<p>The following files are installed by the va508runtimes.exe file:</p>
<ul>
<li><p>JAWS.SR - DLL used for communication between JAWS and BCMA</p></li>
<li><p>VA508Access2006.bpl</p></li>
<li><p>VA508APP.jcf - JAWS configuration file</p></li>
<li><p>VA508APP.JKM - JAWS keyboard mapping file</p></li>
<li><p>VA508app.jsb</p></li>
<li><p>VA508APP.JSS - JAWS script file</p></li>
<li><p>VA508jaws.jsb</p></li>
<li><p>VA508JAWS.jsd - Documentation companion file to the VA508JAWS.jss script file</p></li>
<li><p>VA508JAWS.jss - JAWS script file</p></li>
<li><p>VA508JAWSDispatcher.exe - Application used for communication between JAWS and multiple applications using the JAWS.SR DLL</p></li>
<li><p>VA508Uninstall.exe</p></li>
<li><p>VAShared2006.bpl</p></li>
</ul>
<p>This version of BCMA has been tested against JAWS, version 11.</p></td>
</tr>
</tbody>
</table>