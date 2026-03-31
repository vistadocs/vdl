---
consolidated_title: "bcma release notes"
app_code: PSB
doc_type: RN
master_source: "PSB*3*68 BCMA Version 3 Release Notes"
master_pub_date: September 2012
consolidated_from: 4 versions
prior_versions:
  - "PSB*3*2 BCMA Version 3 Release Notes"
  - "PSB*3*42 BCMA Version 3 Release Notes"
  - "PSB*3*58 BCMA Version 3 Release Notes"
---

> ![](psb-3-68-bcma-version-3-release-notes/001.png)

Special Instructions / Other Print Info and Injection Sites for BCMA v3.0

####### RELEASE NOTES

PSB\*3\*68

September 2012

Product Development (PD)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Special Instructions/Other Print Info Enhancement](#special-instructionsother-print-info-enhancement)
  - [Virtual Due List (VDL) Modified](#virtual-due-list-vdl-modified)
  - [Three ways to display Special Instructions/Other Print Info on Each Medication Tab](#three-ways-to-display-special-instructionsother-print-info-on-each-medication-tab)
  - [Dialog Boxes Modified](#dialog-boxes-modified)
  - [Special Instructions/Other Print Info Pop-Up Boxes Modified](#special-instructionsother-print-info-pop-up-boxes-modified)
  - [BCMA Cover Sheet Modified](#bcma-cover-sheet-modified)
  - [BCMA Reports Modified](#bcma-reports-modified)
- [Injection Sites Enhancement](#injection-sites-enhancement)
  - [Conditions to enable Injection Site features](#conditions-to-enable-injection-site-features)
  - [“Last Site” column displayed on the BCMA VDL](#last-site-column-displayed-on-the-bcma-vdl)
  - [Options to Display Injection Site History](#options-to-display-injection-site-history)
  - [Injection Site History Dialog](#injection-site-history-dialog)
  - [Expanded Injection Site Needed Dialog](#expanded-injection-site-needed-dialog)
  - [Multiple Administrations](#multiple-administrations)
- [Patient Safety Issue Corrections](#patient-safety-issue-corrections)
- [Defect Fix for Remedy Tickets](#defect-fix-for-remedy-tickets)
- [New Service Requests (NSRs) Resolved](#new-service-requests-nsrs-resolved)
- [BCMA Online Help Update](#bcma-online-help-update)
- [Installation Details](#installation-details)
This document provides a feature summary of the Special Instructions and Other Print Info (SPECIAL INSTRUCTIONS/OTHER PRINT INFO) and Injection Sites functionality for Bar Code Medication Administration (BCMA) v3.0 project, patch PSB\*3\*68.
­­­­­­­­­­­­­
Installation instructions for PSB\*3\*68 are included in the patch description. See page [20](#installation-details) of these Release Notes for additional installation details.
- When installing PSB\*3\*68, a second part of the install will immediately begin running in the background and will create a new index for the injection site. This may take 20 to 30 hours to complete.
- After installing the patch, and upon opening BCMA, be sure to expand the last column which is entitled “Last Site.” The default is approximately 8 characters, depending on screen resolution, use of capitals or lower case, etc. After you expand the column, BCMA will remember the width each time you log in.
Patches PSB\*3\*58, PSB\*3\*61, PSB\*3\*62, PSS\*1\*171, PSJ\*5\*267 and PSB\*3\*67 must be installed prior to PSB\*3\*68.Highlights
- The following dialogs and popups that include Special Instructions/Other Print Info were widened and modified to accommodate unlimited text sent via Inpatient Medications.
  - Special Instructions/Other Print Info pop-up boxes
  - Medication Log
  - Unable to Scan
  - Multiple/Fractional Dose
  - PRN Medication Log
  - PRN Effectiveness Log
  - Scan IV
- Title bar for Special Instructions/Other Print Info modified.
- Three methods added to display Special Instructions/Other Print Info on demand for each medication tab.
- New methods added to display Special Instructions/Other Print Info from the Cover Sheet.
- Last Site Column added to the VDL showing the location of the last injection site for the orderable item.
- Expanded Injection Site Needed dialog displays during administration of applicable medications, showing injection site history to assist with injection site rotation.
- Injection Site History dialog added showing the previous injection sites, up to 4, for the orderable item and all injection sites for the patient within the time frame for the parameter selected.
BCMA Reports
- All reports that contain Special Instructions/Other Print Info were modified to accommodate unlimited text.
- The report dialog boxes of some of the BCMA reports were modified to allow the user to include/exclude Special Instructions/Other Print Info from the reports.
Patient Safety Issue Correction
- Patient Safety Issues, PSPO 42, 1466, and 2037 resolved with PSB\*3\*68.
BCMA Online Help System Update
- The Online Help system has been updated for BCMA.

# Special Instructions/Other Print Info Enhancement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications and BCMA Special Instructions/Other Print Info fields were modified to support an unlimited amount of text. This text is received from the Provider Comments that are entered in the Computerized Patient Record System (CPRS) order entry screen by the provider, and then optionally edited by the Pharmacist in Inpatient Medications. Previously, the Inpatient Medications character length for Special Instructions was 180 characters and for Other Print Info 60 characters.

## Virtual Due List (VDL) Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Special Instructions/Other Print Info will display on the VDL under the Active Medication. If the total height of the administration row including Special Instructions/Other Print Info is equal to or greater than 19 lines, the following message displays for all three med tabs in place of Special Instructions/Other Print Info (bold red text): “Too much information to display. Use right-click menu to display full text.”

Example: VDL Display

![](psb-3-68-bcma-version-3-release-notes/002.png)

## Three ways to display Special Instructions/Other Print Info on Each Medication Tab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three ways will display Special Instructions/Other Print Info for orders that contain them.

- Special Instructions/Other Print Info Right Click Menu

Example: Special Instructions/Other Print Info Right Click Menu

![](psb-3-68-bcma-version-3-release-notes/003.png)

- Special Instructions/Other Print Info Due List Menu

Example: Special Instructions/Other Print Info Due List Menu

![](psb-3-68-bcma-version-3-release-notes/004.png)

- Special Instructions/Other Print Info Shortcut Function Key (F6)

Example: Special Instructions/Other Print Info Shortcut (F6)

![](psb-3-68-bcma-version-3-release-notes/005.png)

- The above options will be disabled (grayed out) for orders that do not contain Special Instructions/Other Print Info.

Example: Special Instructions/Other Print Info Disabled

![](psb-3-68-bcma-version-3-release-notes/006.png)

## Dialog Boxes Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following dialog boxes were modified by allowing the Special Instructions/Other Print Info box to expand the full width of the dialog box. A conditional vertical scroll bar and word wrap were added. The vertical height of the Special Instructions/Other Print Info display within the dialog boxes is 6 lines.

- Unable to Scan DialogExample: Unable to Scan Dialog

![](psb-3-68-bcma-version-3-release-notes/007.png)

- Medication Log DialogExample: Medication Log Dialog

![](psb-3-68-bcma-version-3-release-notes/008.png)

- Multiple/Fractional Dose DialogExample: Multiple/Fractional Dose Dialog

![](psb-3-68-bcma-version-3-release-notes/009.png)

- PRN Medication Log DialogExample: PRN Medication Log Dialog

![](psb-3-68-bcma-version-3-release-notes/010.png)

- PRN Effectiveness Log DialogExample: PRN Effectiveness Log Dialog

![](psb-3-68-bcma-version-3-release-notes/011.png)

-   
  Scan IV DialogExample: Scan IV Dialog

![](psb-3-68-bcma-version-3-release-notes/012.png)

In all of the above dialog boxes, if Special Instructions/Other Print Info text exceeds 6 lines, a scroll bar and “Display Instructions” button appear. The following message displays in bold red text: “\<Scroll down or click ‘Display Instructions’ for full text\>.” When the “Display Instructions” button is clicked, Special Instructions/Other Print Info will display in the pop-up.

Following are examples of dialog boxes with Special Instructions/Other Print Info text that exceed 6 lines.

  
Example: Unable to Scan Dialog Box

![](psb-3-68-bcma-version-3-release-notes/013.png)

Example: Scan IV Dialog Box

![](psb-3-68-bcma-version-3-release-notes/014.png)

## Special Instructions/Other Print Info Pop-Up Boxes Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The title bar of the pop-up for Special Instructions/Other Print Info now reflects the type of information contained in the dialog, Special Instructions or Other Print Info. Special Instructions displays for Unit Dose and IV Push administrations, while Other Print Info display for IVPB and large volume IV medications.
- The default size of the Special Instructions pop-up box is approximately 80 characters wide with a minimum height of 6 lines. The width cannot be changed, and the height will automatically resize to accommodate the length of the message. If the vertical height of the message exceeds the size of the screen, a vertical scroll bar displays.

> If the total height of the administration row, including Special Instructions, is equal to or greater than 19 lines, the following message displays in place of Special Instructions (bold red text): “Too much information to display. Use right-click menu to display full text.”

Example: Special Instructions Pop-up Box

![](psb-3-68-bcma-version-3-release-notes/015.png)

Example: Other Print Info Pop-up Box

![](psb-3-68-bcma-version-3-release-notes/016.png)

## BCMA Cover Sheet Modified 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- For orders containing Special Instructions/Other Print Info that exceed 180 characters on the Cover Sheet, the message: “Too much information to display. Use right-click menu to display full text” will be displayed.

  
Example: BCMA Cover Sheet

![](psb-3-68-bcma-version-3-release-notes/017.png)

- For orders containing Special Instructions/Other Print Info that exceed 180 characters on the Cover Sheet, the hover text message: “Too much information to display. Use right-click menu to display full text” will be displayed while hovering over a Special Instructions/Other Print Info field exceeding 180 characters.

Example: BCMA Cover Sheet Hover Text

![](psb-3-68-bcma-version-3-release-notes/018.png)

- The following two methods will also display Special Instructions/Other Print Info on the Cover Sheet.
  - Special Instructions/Other Print Info Right Click Menu

Example: Special Instructions/Other Print Info Right Click Menu

![](psb-3-68-bcma-version-3-release-notes/019.png)

- Special Instructions/Other Print Info Shortcut Key (Alt+Ctrl+S)

Example: Special Instructions/Other Print Info Shortcut Key (Alt+Ctrl+S)

![](psb-3-68-bcma-version-3-release-notes/020.png)

- The above options will be disabled (grayed out) for orders that do not contain Special Instructions/Other Print Info.

Example: Special Instructions/Other Print Info Disabled

![](psb-3-68-bcma-version-3-release-notes/021.png)

## BCMA Reports Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following BCMA reports were modified to invoke a 74 character word wrap for Special Instructions/Other Print Info to accommodate unlimited text.

- Medication Administration History (MAH) Report
- Display Order Detail Report
- Due List Report
- IV Bag Status Report
- Cover Sheet Report – Medication Overview Report
- Cover Sheet Report – PRN Overview Report
- Cover Sheet Report – IV Overview
- Cover Sheet Report – Expired/DC’d/Expiring Report

When printing the MAH report to a printer, if Special Instructions/Other Print Info need to flow to another printed page, a blank line with the message: “CONTINUED ON NEXT PAGE\*\*\*” is printed before the page break. The message: “\*\*\*CONTINUED FROM PREVIOUS PAGE \*\*\*” and a blank line is printed on the subsequent page after the page headers.

Special Instructions was moved below the Initials field and starts on a separate line to allow for wrapping and unlimited text. The field is now entitled “Special Instructions.”

  
Example: MAH Report

![](psb-3-68-bcma-version-3-release-notes/022.png)

The report dialog boxes of the following BCMA reports were also modified to display a checkbox that allows the user to include/exclude SPI/OPI from the reports. The checkbox is unchecked by default, which excludes Special Instructions/Other Print Info from the reports.

- Due List Report
- IV Bag Status Report
- Cover Sheet Report – Medication Overview Report
- Cover Sheet Report – PRN Overview Report
- Cover Sheet Report – IV Overview
- Cover Sheet Report – Expired/DC’d/Expiring Report

# Injection Sites Enhancement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA now allows the nurse at the time of medication administration to see the location of up to the last four injection sites for the orderable item, displayed without time limits and all injection site entries for the patient within the time frame (nn) specified by the BCMA Site Parameter, “Injection Site History Max Hours.” The default is 72 hours.

## Conditions to enable Injection Site features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new injection site functionality applies to injectable administrations that participate in injection site rotation. When the following conditions are met, the Last Site column will be populated, Injection Site History options will be enabled, and the expanded Injection Site Needed dialog will display for applicable administrations.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Unit Dose Tab:</strong></td>
</tr>
<tr class="even">
<td><p>If the administration is on the Unit Dose Tab, and</p>
<p>“PROMPT FOR INJ SITE IN BCMA” = YES</p>
<p>in the Medication Routes file (#51.2).</p></td>
</tr>
<tr class="odd">
<td><strong>IVP/IVPB Tab:</strong></td>
</tr>
<tr class="even">
<td><p>If the administration is on the IVP/IVPB tab, and</p>
<p>IV TYPE = SYRINGE, subtype INTERMITTENT or</p>
<p>IV TYPE = CHEMOTHERAPY, subtype SYRINGE, subtype INTERMITTENT, and</p>
<p>MEDICATION ROUTE = Intramuscular, Subcutaneous, or Intradermal, and</p>
<p>“PROMPT FOR INJ SITE IN BCMA” = YES, and</p>
<p>“DISPLAY ON IVP/IVPB TAB IN BCMA?” = YES</p>
<p>in the Medication Routes file (#51.2).</p></td>
</tr>
</tbody>
</table>

## “Last Site” column displayed on the BCMA VDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new column, “Last Site”, was added to the VDL on the Unit Dose and IVP/IVPB tabs, displaying the last injection site that was indicated for the orderable item, for administrations that participate in injection site rotation. The column appears in the last position to the right of the “Last Action” column.

  
Example: Last Site Display

![](psb-3-68-bcma-version-3-release-notes/023.png)

## Options to Display Injection Site History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA provides multiple ways to display Injection Site History for administrations that participate in injection site rotation.

- Right-click menu option, “Injection Site History”.

Example: Right-Click Menu

![](psb-3-68-bcma-version-3-release-notes/024.png)

- Due List menu option, “Injection Site History”.

Example: Due List Menu

![](psb-3-68-bcma-version-3-release-notes/025.png)

- F7 shortcut option enabled.

## Injection Site History Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Injection Site History Dialog displays two tables:

- “Previous Injection Sites for this Medication (up to 4)” shown at the top, lists the last four injection sites for the orderable item displayed without time limits. The name of the Orderable Item and the route are shown above the top table.
- “All Injection Sites (within last nn hours)” shown at the bottom, lists all injection site entries for the patient within the time frame (nn) specified by the BCMA Site Parameter, “Injection Site History Max Hours.” The default is 72 hours.

> Note: If no data exists for the table, the message “\<\<No data to display\>\>” appears.

> The following fields are displayed in each table: Date Time, Medication (orderable item name), Dosage Given, Route, and Injection Site – sorted in reverse date/time order.

  
Example: Injection Site History Dialog

![](psb-3-68-bcma-version-3-release-notes/026.png)

## Expanded Injection Site Needed Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The expanded Injection Site Needed displays during administration of injectable medications when the conditions in section 3.1 are met. The information provided in the following tables will assist the nurse in deciding the location of the next injection site, to ensure proper injection site rotation.

- “Previous Injection Sites for this Medication (up to 4)” shown at the top, lists the last four injection sites for the orderable item displayed without time limits. The name of the Orderable Item and the route are shown above the top table.
- “All Injection Sites (within last nn hours)” shown at the bottom, lists all injection site entries for the patient within the time frame (nn) specified by the BCMA Site Parameter, “Injection Site History Max Hours.” The default is 72 hours.

> Note: If no data exists for the table, the message “\<\<No data to display\>\>” appears.

> The following fields are displayed in each table: Date Time, Medication (orderable item name), Dosage Given, Route, and Injection Site sorted in reverse date/time order.

  
On the Unit Dose tab:

1.  The user selects the location on the patient where the medication is to be injected from the Select Injection Site drop-down list.
2.  Click OK.

Example: Expanded Injection Site Needed Dialog on Unit Dose Tab

![](psb-3-68-bcma-version-3-release-notes/027.png)

  
On the IVP/IVPB tab:

1.  In the lower left of the following dialog, a checkbox is displayed with the statement: “I acknowledge this medication to be administered via route:\_\_\_\_\_\_\_\_\_\_\_.” The medication route is displayed in bold uppercase red text. The OK button remains disabled until the user confirms the acknowledgement statement by checking the checkbox and selecting an injection site.
2.  The user selects the location on the patient where the medication is to be injected from the Select Injection Site drop-down list.
3.  Click OK.

Example: Expanded Injection Site Needed Dialog on IVP/IVPB Tab

![](psb-3-68-bcma-version-3-release-notes/028.png)

## Multiple Administrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When multiple administrations are selected, the Injection Site History menu option and corresponding F7 hotkey are disabled (grayed out) on both the Right click menu and the Due List Menu.

# Patient Safety Issue Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Safety Issue corrections made with this patch:

- PSPO 42 – Special Instructions/Other Print Info too short corrected.
- PSPO 1466 – Provider Comments truncated when copying to Special Instructions corrected.
- PSPO 2037 – Unable to view all allergies/ADRs for patient on BCMA GUI corrected.

# Defect Fix for Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remedy Tickets were resolved with this patch:

- HD480879 – Multiple Dose Dialog Box “Invalid Medications” popup modified to display whenever an invalid dose is scanned.
- HD488494 – BCMA modified to display all Allergies and ADRs for patients with more than one line of Allergies and ADRs.
- HD506938 – BCMA modified to always display Patient Record flag in Red.
- HD419658 – Special Instructions modified to print in full on Med Overview and PRN Overview Reports

# New Service Requests (NSRs) Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following NSRs were resolved with this patch:

- 20031205 – Equalizing character limits
- 20081003 – BCMA Enhancement - Injection Sites

# BCMA Online Help Update 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA GUI Online Help system has been updated to include all released BCMA PSB\*3\*68 functionality.

# Installation Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post install routine will run to initialize the New Kernel variable, PSB INJECTION SITE MAX HOURS, used for the new Injection Site History functionality in BCMA.  This parameter may be changed, after this install, via the BCMA site parameters GUI client, per division, to match site policy.  This new parameter will be initialized for all divisions having the Parameter "PSB ONLINE" set to YES, as shown below in the Example Install Message.

 

A second part of the post install procedure, BCMA Injection Site Cross Ref Builder, will be tasked in the background and begin running immediately.  This process may take 20-30 hours to complete, depending on your sites BCMA MEDICATION LOG file size. BCMA can be used while this background job is running. 

 

The background job will process the most recent Medical Administration records and work its way back through the BCMA MEDICATION LOG file until complete.  The most recent records should be available for the Injection History Window in BCMA, in one to two hours.  A MailMan message will be sent to the installer when the background job has completed.

See below example.

The background job can be stopped by asking Taskman to stop. A MailMan message will be sent containing the progress of the Cross Ref Builder to that point. This procedure can be restarted later. It will resume where it left off. 

 

The status of this background job can be checked by typing the Mumps command in Programmer Mode, as shown below in the Example Status Check.

The Post Install routine, PSB3P68, should be deleted manually after the MailMan message is received indicating the Cross Ref Builder is complete. See “Post Installation” section in the patch description for instructions on deleting the routine.

 Example MailMan Message:

------------------------

Subj: BCMA Injection Site Cross Ref Builder Results  \[#141406\]

 02/23/12@15:42 6 lines

From: PSB3P68 POST INSTALL  In 'IN' basket.   Page 1

-------------------------------------------------------------------------

BCMA Injection Site Cross Ref Builder Status: COMPLETED Feb 23,2012@15:23

         Total Records in file:      21,180,999

             Records processed:      21,180,999

            Total elapsed time:       1 5:22:32

              Percent complete:            100%

  Example Status Check:

---------------------

   UCI\>D STATUS^PSB3P68

   BCMA Injection Site Cross Ref Builder

   Status: RUNNING since   Feb 23, 2012@15:42:47

   74% complete

 

 Example Install Message:

------------------------

 

  \*\*\* PSB\*3\*68 POST INSTALL NOW RUNNING \*\*\*

 

   Initialize BCMA parameter PSB INJECTION SITE MAX HOURS...

     DIV                              MAX HRS

   Before update

     ABC DIVISION                      

     XYZ DIVISION                      

 

   After update

     ABC DIVISION                       72

     XYZ DIVISION                       72

 

 

 

   BCMA Injection Site Cross Ref Builder

   This request queued as Task \# 4957178

   A MailMan message will be sent to you when the Cross Reference Builder

   completes.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSB*3*58 BCMA Version 3 Release Notes

## Site Parameter for Non-Nurse Verified orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the BCMA Site Parameters application Graphical User Interface (GUI), a new option group labeled “Non-Nurse Verified Orders” with three mutually exclusive options: “Allow Administration (No Warning)”, “Allow Administration with Warning”, “Prohibit Administration” was added.

“Allow Administration (No Warning)” is the default setting. Below are examples of the parameter screens.

Example: Parameter Screen

![](psb-3-58-bcma-version-3-release-notes/002.png)

## Administering Non-Nurse Verified medication orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When “Allow Administration (No Warning)” parameter option is selected:

> If nurse initials are <u>not</u> displayed in Verified “Ver” column of the BCMA VDL for a particular order/administration, BCMA will allow the medication to be administered with no warning to the user.

> Marking non-nurse verified administrations as Held, Refused, or Missing Dose will be unaffected by this parameter setting. Therefore, no warnings will be displayed.

- When “Allow Administration with Warning” parameter option is selected:

> If nurse initials are <u>not</u> displayed in Verified “Ver” column of the BCMA VDL for a particular order/administration, BCMA will display a warning dialog with the message: “Order NOT Nurse-Verified! Do you want to continue?” when user scans the medication (or uses Unable to Scan).

> The user has the choice of continuing the administration or cancelling the administration. Clicking OK will acknowledge that the order has not been nurse verified, and the user may continue the administration. All medication administration dialogs will display as appropriate to the workflow for the selected administration.

> Clicking Cancel will display the “Order Administration Cancelled” dialog. User must click OK to acknowledge the cancellation and return to the VDL.

Example: Warning Message

> ![](psb-3-58-bcma-version-3-release-notes/003.png)

- When “Prohibit Administration” parameter option is selected:

> If nurse initials are <u>not</u> displayed in Verified “Ver” column of the BCMA VDL for a particular order/administration, BCMA will display an error dialog with the message: “Order NOT Nurse-Verified! DO NOT GIVE!” when user scans the medication (or uses Unable to Scan).

> Clicking OK to acknowledge the “DO NOT GIVE” message and clicking OK at the “Order Administration Cancelled” dialog will acknowledge the cancellation and return the user to the VDL without administering the medication.

  
Example: Error Message

> ![](psb-3-58-bcma-version-3-release-notes/004.png)

- When the “Allow Administration with Warning” or “Prohibit Administration” parameter setting is selected, the resulting warning/error pop-up message will usually precede other BCMA pop-ups during the medication administration process. Exceptions to this are:
  - Ward Stock Bags: When the user scans bag components into the Ward stock dialog thus creating a ward stock bag, BCMA will not match the list of components to the order until the user selects OK. At that time, if the order is not nurse-verified, the Non-Nurse Verify pop-up will then display. (Applies to IVP/IVPB and IV)
  - Multiple Orders for Scanned Drugs: When the user scans a medication and there are multiple administrations available within the virtual due list parameters timeframe, the Multiple Orders for Scanned Drugs dialog displays before the Non-Nurse Verify pop-up. (Applies to Unit Dose and IVP/IVPB)
  - Currently Infusing IV Bags: When attempting to scan a new bag while an existing bag is currently infusing, the user must complete the infusing bag before the Non-Nurse Verify pop-up displays. (Applies to IV)
- Site parameters for non-nurse verified orders do not affect the CPRS med order button functionality.

## Submitting a Missing Dose Request for Non-Nurse Verified Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When submitting a Missing Dose request for non-nurse verified Unit Dose, IVP/IVPB, or IV orders, the user must perform one of the following actions:

- When “Allow Administration (No Warning)” parameter option is selected, no Warning message will display. The Missing Dose Request dialog box will display. The user may continue submitting the Missing Dose Request for the non-nurse verified order.
- When “Allow Administration with Warning” parameter option is selected, the pop-up dialog with the warning: “Order NOT Nurse-Verified! Do you want to continue?” will display.

> The user must click OK to acknowledge that the order has not been nurse verified. The Missing Dose Request dialog box will display. The user may continue submitting the Missing Dose Request for the non-nurse verified order.

> The user must click Cancel to cancel the request.

  
Example: Warning Message

> ![](psb-3-58-bcma-version-3-release-notes/005.png)

- When “Prohibit Administration” parameter option is selected, the pop-up dialog with the error message: “Order NOT Nurse-Verified. Action unavailable until verified.” will display.

> The user must click OK to cancel the selected action and return to the VDL.

Example: Error Message

![](psb-3-58-bcma-version-3-release-notes/006.png)

> Note: User’s site policy will determine the correct workflow for verifying the order in CPRS.

## Marking Multiple Non-Nurse Verified Administrations Held or Refused

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When “Allow Administration With Warning” parameter option is selected, if nurse initials are <u>not</u> displayed in the Verified “Ver” column of the BCMA VDL for a particular order/administration, when the user attempts to mark multiple administrations Held or Refused, BCMA will display a pop-up dialog with the warning: “You have selected one or more orders that are NOT Nurse Verified. Do you want to continue?”

User has the choice of continuing the administration or cancelling the administration.

- Clicking OK will acknowledge that the order has not been nurse verified, and the user may continue the administration. Held or Refused dialogs will display as appropriate to the workflow for the selected action. All of the selected administrations will be marked appropriately.
- Clicking Cancel will return the user to the VDL. No administrations will be marked.

  
Example: Warning Message

![](psb-3-58-bcma-version-3-release-notes/007.png)

- When “Prohibit Administration” parameter option is selected, if nurse initials are <u>not</u> displayed in the Verified “Ver” column of the BCMA VDL for a particular order/administration, when the user attempts to mark multiple administrations Held or Refused, BCMA will display a pop-up error dialog with the message:“You have selected one or more orders that are NOT Nurse Verified. Do you want to continue?”

User has the choice of continuing the administration or cancelling the administration.

- Clicking OK will acknowledge that the order has not been nurse verified, and the user may continue the administration. Held or Refused dialogs will display as appropriate to the workflow for the selected action. All of the selected administrations will be marked appropriately.
- Clicking Cancel will return the user to the VDL. No administrations will be marked.

Example: Warning Message

![](psb-3-58-bcma-version-3-release-notes/008.png)

- PRN orders are skipped when checking the non-nurse verify status for a selection of multiple orders to be marked Held or Refused. Only non-PRN orders will trigger a prompt for held or refused non-nurse verified orders.

## PRN Effectiveness Entry Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Allowable time for PRN Effectiveness Entry Parameter maximum has been expanded from 240 to 960 minutes.

- The drop down field has been changed to a spinner field.
- Numeric options in 10 minute increments are provided.

Below is an example of the parameter screen.

  
Example: Parameter Screen

> ![](psb-3-58-bcma-version-3-release-notes/009.png)

## BCMA GUI Visual Indicator to reflect Provider Overrides/Pharmacist Interventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A logical flag was created to pass from Inpatient Medications to BCMA, to indicate the existence of CPRS Provider override reasons and/or Pharmacist interventions associated with an order.

If the flag exists for an order, the cell in the Verified “Ver” column of the order/administration on the BCMA VDL is highlighted in yellow, to indicate the existence of CPRS Provider override reasons and/or Pharmacist interventions associated with the order.

- The highlighting of the Verified “Ver” cell is applicable to orders on all three medication tabs: Unit Dose, IVP/IVPB, and IV.
- The highlighting of the Verified “Ver” cell is applicable to orders on the Cover Sheet.

The Verified “Ver” column was added to the Cover Sheet tab to display either initials of the nurse who verified order, or three asterisks “\*\*\*” to indicate the order is non-nurse verified.

Example: VDL Screen Excerpt

> ![](psb-3-58-bcma-version-3-release-notes/010.png)

## BCMA Order Detail Report displays CPRS Provider Overrides/Pharmacist Interventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If CPRS Provider override reasons and/or Pharmacist interventions exist for an order, a summary of the order’s <u>current</u> CPRS Order Checks, Provider override reasons and Pharmacist intervention information will be included in the BCMA Order Detail report, below “Spec Inst”.

At the top of the summary, the following Provider Override information displays:

- Heading: \*\*Current Provider Overrides for this order \*\*
- “Overriding Provider:” (Provider Name and Title)
- “Override Entered By:” (User who entered justification and Title)
- “Date//Time Entered: ” (MM/DD/YY HH:MM)
- “Override Reason:” (Justification text)

Below the Provider Override information, the summary of current CPRS Order Checks will display in the following order:

- Allergies/Adverse Drug Reaction (ADR)s
- Critical drug-drug interactions
- All other interactions that were displayed in the CPRS Order Checks dialog at the time the order was signed.

BCMA Order Detail Report Variations:

- Both current CPRS Provider Overrides and current Pharmacist Interventions exist for a critical drug-drug interaction or an allergy/ADR associated with the order.

Example: BCMA Order Detail Report

![](psb-3-58-bcma-version-3-release-notes/011.png)

- A current CPRS Provider Override exists for a critical drug-drug interaction or an allergy/ADR associated with the order; No Pharmacist Intervention exists for the order.

Example: BCMA Order Detail Report

![](psb-3-58-bcma-version-3-release-notes/012.png)

- A current Pharmacist Intervention exists for a critical drug-drug interaction or an allergy/ADR associated with the order; no CPRS Provider Override exists for the order.

Example: BCMA Order Detail Report

![](psb-3-58-bcma-version-3-release-notes/013.png)

## Icon Legend Option Added to the View Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new menu option called “Icon Legend” was added to the View Menu so that when selected, a dialog will display showing icons used throughout BCMA, with their corresponding descriptions:

- Click on View then click on Icon Legend.
- Clicking OK will return the user to the VDL.

Example: Icon Legend

![](psb-3-58-bcma-version-3-release-notes/014.png)

## “Hover-Over” Capability Added to the VDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new hover-over feature was added to the BCMA VDL. When CPRS Provider Overrides and/or Pharmacist Interventions exist for an order, the user will be able to hover over the highlighted Verified “Ver” cell, and the following visual indicator will display: “Override/Intervention reasons.”

Example: Override/Intervention Indicator

![](psb-3-58-bcma-version-3-release-notes/015.png)

## Double Scan Detection and Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality was added to test for scanning of data into the Quantity and Units pop-up fields. The Double Scan routine tests for the following criteria and rejects input that matches:

- Integer only
- All–numeric string (out of range for integer)
- IV label: nnnVnn where n is a numeric digit
- Number and units: nnnnnU or nnnnn U where n is a numeric digit. A single U is also rejected.

Where double scanning occurs, e.g., a match is found for any of the first three conditions, above, BCMA will display a popup error dialog with the message: “Error. Incorrect or insufficient information entered. Please use the correct quantity and units. Examples: 5000 units, 2mg, 1 puff, small amount, 1 inch.”

  
Example: Error Message

![](psb-3-58-bcma-version-3-release-notes/016.png)

If ‘U’ or ‘u’ is entered, BCMA will display a popup error dialog with the message: “Error. ‘U’ or ‘u’ is not an acceptable abbreviation. Retype the entry using the word “units.”

Example: Error Message

![](psb-3-58-bcma-version-3-release-notes/017.png)

## Missed Medications Report Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missed Medications Report dialog was modified so that the “Include Admin Status: Held, Refused” and the “Include Detail: Comments/Reasons” checkboxes will be checked (selected) as a default when the report dialog initially displays.

These new default settings will always be in effect when the report is executed. The Comments/Reasons checkbox will be selected regardless of parameter settings for Reports-Include Comments. Upon display of the dialog, the user will be able to uncheck the boxes as desired.

Example: Missed Meds Report Dialog Box

![](psb-3-58-bcma-version-3-release-notes/018.png)

## Missed Medications Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA Missed Medications Report has been modified to add a Verified column showing nurse initials or asterisks in both By Patient and by Ward formats.

Example: Missed Medication Report by Patient

![](psb-3-58-bcma-version-3-release-notes/019.png)

### From: PSB*3*42 BCMA Version 3 Release Notes

### *(This page included for two-sided copying.)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Indian Health Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA application is now able to determine if it is operating in the Indian Health Service (IHS) or Veterans Health Administration (VHA) environment and recognize and display the appropriate patient identifier. This enables a single version of BCMA to be maintained by VHA and be installed and operate in a “plug and play” fashion in an IHS or Tribal facility running Resource and Patient Management System (RPMS).

BCMA principally interacts with the Patient Information Management System (PIMS), Inpatient Pharmacy, and Order Entry/Results Reporting (OE/RR) packages. Each of these has a native VistA version and a modified Resource and Patient Management system (RPMS) version maintained by IHS. With this enhancement, BCMA is able to work seamlessly alongside these packages regardless of the operating environment. In addition, the BCMA Graphical User Interface (GUI) displays vital measurements from the Veterans Administration (VA) VITALS/MEASUREMENTS package or the PCC V MEASUREMENT files, if operating in an RPMS system.

## Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 508 of the Rehabilitation Act of 1973 and Rehabilitation Act Amendments of 1998 mandates that all software developed by federal agencies allow access to and use of information and data by individuals with disabilities. The updated BCMA V. 3.0 GUI ensures compliance with the requirements of the Section 508 Checklist for Software Applications and Operating Systems. Section 508 enhancements to BCMA ensure accessibility for color-blind, mobility-impaired, and visually-impaired users, without impacting software usability for sighted staff administering medications to patients.

The Delphi Components for Section 508 Compliance functionality and screen reader compatibility to the BCMA GUI VDL are incorporated in this enhancement as required and specified by the VA Section 508 Compliance Office. Section 508 Compliance requirements for software applications can be accessed via the following link: <span class="mark">REDACTED</span>

## Indian Health Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Identifies Operational Environment

BCMA recognizes the operational environment (VistA or RPMS) by referencing the agency variable DUZ (“AG”).

Recognizes IHS Patient Identifier

When operating in the RPMS environment, BCMA reads the 12-digit bar code IHS patient identifier and splits the 12-digit identifier into its component parts, Area, Service Unit Facility ASUFAC (characters 1-6) and Health Record Number (HRN) (characters 7-12), to correctly identify and match patient identifiers associated with drug orders.

Provides IHS Site Parameter for Customizing IHS Patient ID Label

When operating in the RPMS environment, the application provides a Site Parameter to customize the IHS Patient ID label in BCMA. By default, the IHS Patient ID Label defaults to “HRN.” The features below are described using the default IHS Patient ID Label. Please note that the application will display the customized label, if applicable. See Section 3.3 below for details.

Displays IHS Patient Identifier on BCMA GUI Screens

When operating in the RPMS environment, the application displays the default IHS Patient ID Label of “HRN” instead of “SSN” on the following BCMA GUI screens that display a label for the patient identifier, as well as the patient’s 6-digit IHS HRN:

- BCMA Virtual Due List (VDL)
- Patient Confirmation form
- Edit Med Log Administration Select form
- Edit Med Log form
- Patient Select form

Displays IHS Patient Identifier on BCMA GUI Reports

When operating in the RPMS environment, the patient’s entire 6-digit HRN and corresponding IHS Patient ID Label, instead of the SSN, are displayed and printed on the following reports:

- Administration Times
- Cover Sheet Medication Overview
- Cover Sheet PRN Overview
- Cover Sheet IV Overview
- Cover Sheet Expired/DC’d/Expiring Orders
- Display Order
- Due List
- IV Bag Status
- Medication Admin History
- Medication History
- Medication Log
- Medication Therapy
- Medication Variance Log
- Missed Medications
- Patient Demographics/Inquiry
- PRN Effectiveness
- Unable to Scan Detailed Report
- Cumulative Vitals Report
- Patient Record Flag Report

Transmits HRN in HL7 Messages

The application transmits the patient’s entire 6-digit HRN and corresponding IHS Patient ID Label, instead of the SSN, in any Health Level Seven (HL7) messages that it generates.

Displays HRN in BCMA E-mail Notifications

When operating in the RPMS environment, the patient’s entire 6-digit HRN and corresponding IHS Patient ID Label, instead of the SSN, will be displayed and formatted appropriately in the following BCMA e‑mail notification messages:

- Due List Error
- Missing Dose Notification
- Unknown Actions
- Unable to Scan

Detects Vital Signs Application

BCMA determines which vital signs application is in use at the facility (VA VITALS/MEASUREMENTS or PCC V MEASUREMENTS) and retrieves, displays, and files vitals measurement data in the appropriate locations.

Whether a facility uses the VA VITALS/MEASUREMENTS (VHA origin) or the PCC V MEASUREMENTS (IHS origin) to record vital measurements, its use is determined independent of the agency variable, because some IHS facilities may ultimately adopt the VA VITALS/MEASUREMENTS package.

Provides IHS Output Device Support

If BCMA recognizes the RPMS operating environment, it adds the output device of OTH “OTHER” to support printing of reports in the IHS AIX operating system.

Sets System Level IHS Patient ID Label Default

Upon installation of the server package, the System level “IHS Patient ID Label” variable default value, PSB PATIENT ID LABEL, must be set.

- If the operating environment is RPMS, and the System level variable has no value, the script sets the System level “IHS Patient ID Label” variable to a default value of “HRN.”
- If the operating environment is VistA, the script sets the System level “IHS Patient ID Label” variable to a default value of “SSN.”
- A Division level “IHS Patient ID Label” variable having an assigned value takes precedence and overrides the value in the System level “IHS Patient ID Label” variable.

See the BCMA User Manual, Appendix E: IHS – Parameterization.

## Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recognizes JAWS Application

When launching BCMA, the application recognizes whether the JAWS screen reader is currently running. If the screen reader is detected, the BCMA title bar displays “s508”. An alternate interface is launched that runs Delphi components, providing a framework allowing keyboard navigation of the BCMA VDL that is compatible with the JAWS screen reader.

Implemented for BCMA GUI Tabs

Screen reader functionality is implemented for the following medication tabs on the BCMA VDL: Unit Dose, Intravenous Push (IVP)/Intravenous Piggy Back (IVPB), and Intravenous (IV). Note that the BCMA Cover Sheet tab is not compatible with the JAWS screen reader at this time.

Provides Compatible Drug Administration Dialogs

Drug administration dialogs are compatible with the JAWS screen reader.

Provides Enhanced Accessibility

Keyboard shortcuts, field focus, and modified tab order have been added, where necessary, to enhance accessibility.

See the BCMA User Manual, Appendix D: 508 Compliance.

## BCMA Site Parameters Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new parameter has been added to the BCMA Parameters application allowing IHS to customize the patient identifier label used in their environment.

New Tab Added to BCMA Site Parameters Application

If the operating environment is RPMS, a new tab entitled “IHS” is added to the Parameters application which can only be seen when operating in the RPMS environment.

Field Added to BCMA Site Parameters Application

If the operating environment is RPMS, the field entitled “IHS Patient ID Label” is added to the “IHS” tab. This text entry field allows the user to enter a patient ID textual label of up to 5 characters. The contents of this field are displayed throughout BCMA GUI forms, reports, and e-mail notifications.

Patient ID Label Displayed

If the operating environment is RPMS and the Division level “IHS Patient ID Label” variable has no value, the program displays the System level “IHS Patient ID Label” variable value in the “IHS Patient ID Label” field.

If the Division level “IHS Patient ID Label” variable has a value assigned to it, the program displays the Division level “IHS Patient ID Label” variable value in the “IHS Patient ID Label” field.

If the operating environment is RPMS and both Division and System level “IHS Patient ID Label” variables have no value, the program displays the “IHS Patient ID Label” field as blank and BCMA displays “PtID” as the default value for “IHS Patient ID Label.”

User Selected Patient ID Label Stored

If the operating environment is RPMS and the user entry for “IHS Patient ID Label” differs from the System level value, the program stores the user entry to the Division level variable.

See the BCMA Manager’s User Manual, Appendix A: Setting Site Parameters for IHS.

### From: PSB*3*2 BCMA Version 3 Release Notes

## New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list describes the new features provided by patch PSB\*3\*2.

The *Barcode Label Print* \[PSBO BZ\] option allows pharmacy personnel to create Unit Dose and Ward Stock medication labels with a barcode printer. This option gives sites the flexibility to add different types of barcode printers to their printing process and store their unique barcode printer control codes in their local Terminal Type file (#3.2) instead of the BCMA routine.

- The PSBO BZ option is very similar to the PSBO BL option with the exception that the controls codes for the barcode printer are stored in the Terminal Type file \#3.2 rather than being hard coded in a routine.

> Note: The Label Print \[PSBO BL\] option will still be accessible to users with the installation of the new Barcode Label Print \[PSBO BZ\] option.

The data input screens for both options are also the same. The following field lengths were modified:

- Lot number length was increased from 15 to 25 characters.
- Manufacturer length was decreased from 30 to 10 characters.
- Dosage length was decreased from 30 to 22 characters.
- The Barcode Label Print menu option appears at the end of the Medication Administration Menu Pharmacy \[PSB PHARMACY\] menu, as shown below.

> ![](psb-3-2-bcma-version-3-release-notes/002.png)

- Users can print bar code labels for medications that have an unknown or a future drug inactivation date.
- The Barcode *Label Print* \[PSBO BZ\] option will display all four digits of the calendar year for the expiration date on the bar code label.
- Users can also print a blank line for the Check By and Filled By fields if they want to manually record the proper information on the bar code label at a later time.

## Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications correct an error in previous versions of the application.

- The BCMA application no longer errors when accessing a patient who is assigned to a ward location having two entries with the same name (one active and one inactive) in the WARD LOCATION file (#42).

## Examples of Control Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Zebra 105 SL Printer Terminal Type Control Codes

|              |                         |                                                                                                                                                                                                                                           |
|--------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abbreviation | Full Name               | Control Code                                                                                                                                                                                                                              |
| ET           | End Text                | N/A                                                                                                                                                                                                                                       |
| ETF          | End Text Field          | N/A                                                                                                                                                                                                                                       |
| EB           | End Barcode             | N/A                                                                                                                                                                                                                                       |
| EBF          | End Barcode Field       | N/A                                                                                                                                                                                                                                       |
| EL           | End Label               | W !,"^XZ"                                                                                                                                                                                                                                 |
| FE           | Format End              | N/A                                                                                                                                                                                                                                       |
| FI           | Format Initialization   | N/A                                                                                                                                                                                                                                       |
| FI1          | Format Initialization 1 | N/A                                                                                                                                                                                                                                       |
| FI2          | Format Initialization 2 | N/A                                                                                                                                                                                                                                       |
| SB           | Start Barcode           | S PSBTYPE=\$S(PSBSYM="I25":"B2N",PSBSYM="128":"BCN",1:"B3N") S:PSBSYM="" PSBBAR="NO-CODE"  W !,"^BY2,3.0,80^FO20,100^"\_PSBTYPE\_",N,80,Y,N^FR^FD"\_PSBBAR\_"^FS"                                                                         |
| SBF          | Start Barcode Field     | N/A                                                                                                                                                                                                                                       |
| SL           | Start Label             | W !,"^XA",!,"^LH0,0^FS"                                                                                                                                                                                                                   |
| ST           | Start Text              | W !,"^FO"\_PSBTYPE\_"^A0N,30,20^CI13^FR^FD"\_TEXT\_"^FS"                                                                                                                                                                                  |
| STF          | Start Text Field        | S PSBTYPE=\$S(PSBTLE="PSBDRUG":"20,25",PSBTLE="PSBDOSE":"20,60", PSBTLE="PSBNAME":"350,60",PSBTLE="PSBWARD":"350,90", PSBTLE="PSBLOT":"350,120", PSBTLE="PSBEXP":"350,150", PSBTLE="PSBMFG":"500,150", PSBTLE="PSBFCB":"350,180",1:"0,0") |

Zebra Bar Code Label - Field Position Map

| Abbreviation | Control Code ( Field Coordinates) | Description              |
|--------------|-----------------------------------|--------------------------|
| EB           | FO20,150                          | “No – Code” statement    |
| SB           | FO20,100 "                        | Bar Code Graph           |
| STF          | PSBTLE="PSBDRUG":"20,25"          | Drug Name                |
|              | PSBTLE="PSBDOSE":"20,60",         | Dosage                   |
|              | PSBTLE="PSBNAME":"350,60"         | Patient Name and Quality |
|              | PSBTLE="PSBWARD":"350,90",        | Ward Location            |
|              | PSBTLE="PSBLOT":"350,120",        | Lot Number               |
|              | PSBTLE="PSBEXP":"350,150",        | Expiration Date          |
|              | PSBTLE="PSBMFG":"500,150",        | Manufacturer             |
|              | PSBTLE="PSBFCB":"350,180"         | Filled By/Checked By     |

Intermec 3400<sup>e</sup> Printer Terminal Type Control Codes

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Abbreviation</td>
<td>Full Name</td>
<td>Control Code</td>
</tr>
<tr class="even">
<td>ET</td>
<td>End Text</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>ETF</td>
<td>End Text Field</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>EB</td>
<td>End Barcode</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>EBF</td>
<td>End Barcode Field</td>
<td>W "&lt;STX&gt;H8;o50,40;f3;c0;h1;w1;d0,80;&lt;ETX&gt;",!</td>
</tr>
<tr class="even">
<td>EL</td>
<td>End Label</td>
<td>W "&lt;STX&gt;&lt;ETB&gt;&lt;ETX&gt;",!</td>
</tr>
<tr class="odd">
<td>FE</td>
<td>Format End</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>FI</td>
<td>Format Initialization</td>
<td><p>W "&lt;STX&gt;&lt;ESC&gt;C&lt;ETX&gt;",!,"&lt;STX&gt;&lt;ESC&gt;P&lt;ETX&gt;",!,"&lt;STX&gt;E2;F2&lt;ESC&gt;&lt;ETX</p>
<p>&gt;",!</p></td>
</tr>
<tr class="odd">
<td>FI1</td>
<td>Format Initialization 1</td>
<td><p>W "&lt;STX&gt;H7;o30,260;f3;c0;h1;w1;d0,80;&lt;ETX&gt;",!,"&lt;STX&gt;H6;o50,440;f</p>
<p>3;c0;h1;w1;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H5;o50,260;f3;c0;h1;w1;d0,20;&lt;ETX&gt;",!,"&lt;STX&gt;H4;o70,260;f3;c0;h1;w1;d0,35;&lt;ETX&gt;",!</p></td>
</tr>
<tr class="even">
<td>FI2</td>
<td>Format Initialization 2</td>
<td><p>W "&lt;STX&gt;H3;o90,260;f3;c0;h1;w1;d0,35;&lt;ETX&gt;",!,"&lt;STX&gt;H2;o110,260;</p>
<p>f3;c0;h1;w1;d0,35;&lt;ETX&gt;",!,"&lt;STX&gt;H1;o110,40;f3;c0;h1;w1;d0,30;&lt;ETX&gt;",!,"&lt;STX&gt;H0; o130,40;f3;c0;h1;w1;d0,60;&lt;ETX&gt;",!</p></td>
</tr>
<tr class="odd">
<td>SB</td>
<td>Start Barcode</td>
<td>W "&lt;STX&gt;"_TEXT_"&lt;ETX&gt;",!</td>
</tr>
<tr class="even">
<td>SBF</td>
<td>Start Barcode Field</td>
<td><p>S PSBTYPE=$S(PSBSYM="I25":"c2,0",PSBSYM="128":"c6,0",1:"c0,0") W</p>
<p> "&lt;STX&gt;B8;o85,40;f3;"_PSBTYPE_";h50;w1;i1;do,25;p@;&lt;ETX&gt;",!,"&lt;STX&gt;I8;h1;w1;&lt;ETX&gt;",!</p></td>
</tr>
<tr class="odd">
<td>SL</td>
<td>Start Label</td>
<td>W "&lt;STX&gt;R;&lt;EXT&gt;",!,"&lt;STX&gt;&lt;ESC&gt;E2&lt;EXT&gt;",!</td>
</tr>
<tr class="even">
<td>ST</td>
<td>Start Text</td>
<td>W "&lt;STX&gt;"_TEXT_"&lt;CR&gt;&lt;ETX&gt;",!</td>
</tr>
<tr class="odd">
<td>STF</td>
<td>Start Text Field</td>
<td>N/A</td>
</tr>
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
<td>&lt;STX&gt;H8;o50,40;f3;c0;h1;w1;d0,80;&lt;ETX&gt;</td>
<td>“No – Code” statement</td>
</tr>
<tr class="even">
<td rowspan="4">FI1</td>
<td>&lt;STX&gt;H7;o30,260;f3;c0;h1;w1;d0,80;&lt;ETX&gt;</td>
<td>Filled By/Checked By</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H6;o50,440;f3;c0;h1;w1;d0,20;&lt;ETX&gt;"</td>
<td>Manufacturer</td>
</tr>
<tr class="even">
<td>&lt;STX&gt;H5;o50,260;f3;c0;h1;w1;d0,20;&lt;ETX&gt;</td>
<td>Expiration Date</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H4;o70,260;f3;c0;h1;w1;d0,35;&lt;ETX&gt;</td>
<td>Lot Number</td>
</tr>
<tr class="even">
<td rowspan="4">FI2</td>
<td>&lt;STX&gt;H3;o90,260;f3;c0;h1;w1;d0,35;&lt;ETX&gt;</td>
<td>Ward Location</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H2;o110,260;f3;c0;h1;w1;d0,35;&lt;ETX&gt;</td>
<td>Patient Name and Quality</td>
</tr>
<tr class="even">
<td>&lt;STX&gt;H1;o110,40;f3;c0;h1;w1;d0,27;&lt;ETX&gt;</td>
<td>Dose</td>
</tr>
<tr class="odd">
<td>&lt;STX&gt;H0;o130,40;f3;c0;h1;w1;d0,60;&lt;ETX&gt;</td>
<td>Drug Name</td>
</tr>
<tr class="even">
<td>SBF</td>
<td><p>&lt;STX&gt;B8;o85,40;f3;"_PSBTYPE_";h50;wl;il;do;25;p@;</p>
<p>&lt;ETX&gt;&lt;STX&gt;I8;h1;w1;&lt;ETX&gt;"</p></td>
<td>Bar Code Graph</td>
</tr>
</tbody>
</table>
