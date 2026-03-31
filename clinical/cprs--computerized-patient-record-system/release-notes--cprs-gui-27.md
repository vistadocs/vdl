---
consolidated_title: "release notes cprs gui 27"
app_code: CPRS
doc_type: RN
master_source: "OR*3*243 Release Notes CPRS GUI 27"
master_pub_date: February 2009
consolidated_from: 3 versions
prior_versions:
  - "OR*3*277 Release Notes CPRS GUI 27"
  - "OR*3*304 Release Notes CPRS GUI 27"
---

![](or-3-243-release-notes-cprs-gui-27/001.png)

<span class="smallcaps">CPRS GUI version 27</span><span class="smallcaps">(Patch# OR\*3.0\*243)</span><span class="smallcaps">Release Notes</span><span class="smallcaps">February 2009</span>

<span id="_Toc221409085" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Version/<br />
Patch</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>9/3/08</td>
<td>OR*3.0*301</td>
<td><a href="#team_lists">33</a></td>
<td><blockquote>
<p><a href="#team_lists">Corrected an error that team lists would be set by default to Owner when CPRS GUI v.27 was installed.</a></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/3/08</td>
<td>OR*3.0*300 (This is an informational patch only.)</td>
<td><a href="#related_patches">6</a></td>
<td><blockquote>
<p><a href="#related_patches">Removed patch RA*5.0*70 from list of related patches.</a></p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/4/08</td>
<td>OR*3.0*300 (This is an informational patch only.)</td>
<td><a href="#no_continuous_default">12</a></td>
<td><blockquote>
<p><a href="#no_continuous_default">Corrected the release notes to reflect that the Infusion dialog does not come up with a default route of “continuous”. The user must choose a route.</a></p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/15/08</td>
<td>OR*3.0*300 (This is an informational patch only.)</td>
<td><a href="#sensitive_patient_check_no_access">54</a></td>
<td><blockquote>
<p><a href="#sensitive_patient_check_no_access">Clarified the entry about sensitive patient checks to include the fact that users cannot access their own record and that is when this scenario might occur.</a></p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc221409086" class="anchor"></span>Table of Contents

<span id="_Toc221409087" class="anchor"></span>Installation Requirements

<span id="_Toc221409088" class="anchor"></span>Required Delphi Dynamic Link Library

Because CPRS GUI v.27 was compiled with Delphi 2006, CPRS requires a new version of the dynamic link library (DLL) BORLNDMM.DLL. This new DLL will be distributed with the CPRS executable. BORLNDMM.DLL must be installed in the same directory as CPRSChart.exe or in the system path so that it can be found.

If sites use CPRSUpdate.exe and have installed the new version with patch OR\*3.0\*252, CPRSUpdate will copy BORLNDMM.DLL into the same directory as the new CPRSChart.exe as part of the version update.

> **NOTE:** CPRS GUI v.27 will not run unless the BORLNDMM.DLL is installed in the correct location.

<span id="_Toc221409089" class="anchor"></span>Required Patches

The CPRS GUI v.27 patch is OR\*3.0\*243. It is included in the OR_PSJ_PSO_27.KID build. OR_PSJ_PSO_27.KID also contains two required pharmacy patches: PSJ\*5\*134, and PSO\*7\*225. Because CPRS interacts with so many packages, a significant number of patches must be installed before OR\*3.0\*243 can be installed. Below is a comprehensive list; some patches are part of the CPRS installation and other patches have already been nationally released:

- GMPL\*2.0\*35 (part of the CPRS v.27 installation sequence)
- LR\*5.2\*365 (part of the CPRS v.27 installation sequence)
- OR\*3.0\*232
- OR\*3.0\*245
- OR\*3.0\*246
- OR\*3.0\*254
- OR\*3.0\*255
- OR\*3.0\*256
- OR\*3.0\*258
- OR\*3.0\*265
- OR\*3.0\*275
- OR\*3.0\*277
- PSJ\*5.0\*134 (part of the CPRS v.27 installation sequence)
- PSO\*7.0\*225 (part of the CPRS v.27 installation sequence)
- PSS\*1.0\*94 (part of the CPRS v.27 installation sequence)
- PSS\*1.0\*112
- PSS\*1.0\*118
- TIU\*1.0\*219 (part of the CPRS v.27 installation sequence)
- WV\*1.0\*23 (part of the CPRS v.27 installation sequence)
- XU\*8.0\*498  
- YS\*5.01\*92

<span id="_Toc221409090" class="anchor"></span>Related <span id="related_patches" class="anchor"></span>Patches

The following patches are required for functionality but are not required for installation:

- DG\*5.3\*703
- GMRA\*4.0\*38 (part of the CPRS v.27 installation sequence)
- GMRC\*3.0\*55
- GMTS\*2.7\*80 (part of the CPRS v.27 installation sequence)
- GMTS\*2.7\*84 (part of the CPRS v.27 installation sequence)
- GMTS\*2.7\*85
- IB\*2.0\*339
- LR\*5.2\*364
- OR\*3.0\*281 (part of the CPRS v.27 installation sequence)
- OR\*3.0\*299 (part of the CPRS v.27 installation sequence)
- PSJ\*5.0\*120
- PSJ\*5.0\*180
- PSO\*7.0\*292
- PSS\*1.0\*108
- PSS\*1.0\*123 (part of the CPRS v.27 installation sequence)
- PXRM\*2.0\*6
- RA\*5.0\*86
- RA\*5.0\*92
- YS\*5.01\*85

> **NOTE:** CPRS GUI version 27 requires Internet Explorer 4.0 (IE4) or later. However, PKI functionality requires IE 5.5 or later with 128-bit encryption.

<span id="_Toc221409091" class="anchor"></span>Patient Safety Issues

- PSI-04-012: Consults Completed without Viewing Reason for Request

Resolution: Developers added a right-click option to the note editing popup menu to display details of the consult being completed while a consult title is being entered or edited. The new keyboard shortcut is Shift-Ctrl-U.

HDS software involved in resolving PSI-04-012: OR\*3.0\*243.

- PSI-04-057: Provider Selecting Wrong Patient with Same First/Last Name (NOIS BHH-1104-40049, Remedy \#71065) – On the patient selection screen, if a user typed in some letters of a patient’s name, CPRS would try to match the selection, go to that part of the patient list, and highlight the first entry that matched the text entered—even if there was more than one possible match. If the user pressed \<Enter\> without ensuring that the correct patient was selected, the user might be looking at the wrong record.

Resolution: To address this problem, developers changed the patient selection list to implement the same auto-unique selection behavior that the mediation order dialog dosage, route, and schedule implements. Specifically, an item in the list will not be selected unless the text typed uniquely identifies the item. If there are multiple items that could match what the user entered, CPRS requires the user to explicitly select the patient.

- PSI-05-001, PSI-06-068, PSI-06-134, PSI-07-014 and PSI-07-031: Make Anatomic Pathology Notifications Action Alerts

Resolution: Anatomic Pathology Results, Mammogram Results, and Pap Smear Results alerts are now action alerts that send the user to the Reports tab, selecting and displaying the report that triggered the alert.

This new feature requires patches WV\*1.0\*23 and LR\*5.2\*365.

WV\*1.0\*23 contains changes to support the pap smear & mammogram action alert generation.

LR\*5.2\*365 contains changes to the Anatomic Pathology reports display and to the alert message text of electronically signed pathology reports. A detailed report for an individual Anatomic Pathology specimen will now be retrieved and presented to the user. The alert message text is modified so that it includes additional patient identifiers in the notification to precisely identify the patient.

- PSI-05-006: When Discontinuing a Pending Renewal Order the Original Order Became Active Again (Remedy \#71193) – Previously in CPRS, if a user renewed an order, and then discontinued the renewed order while it was still in a pending state, the renewed order was discontinued, but the original order became active again.

Resolution: In this situation, CPRS now has a new option that lets the user pick if they want to discontinue the pending renewal order, or discontinue both the pending renewal order and the original order together.

- PSI-05-007: Invalid Pharmacy Order Number (Remedy \#71197) – Sometimes, for unknown reasons, the Pharmacy number stored in the ORDERS file (#100) does not match a valid Pharmacy number in the Pharmacy package. This mismatch of numbers caused a problem that did not allow users in CPRS to take actions these orders.

Resolution: When a mismatch occurs, developers modified CPRS to display an error message that tells the user that the order could not be saved and that the user should contact Pharmacy to complete the changes on the order.

HDS software involved in resolving PSI-05-007: OR\*3.0\*243.

- PSI-05-026: Changes to When CPRS Displays an Expected First Dose for Inpatient Medications – Previously, CPRS was displaying an expected first dose for on-call schedules and at other inappropriate times.

Resolution: Developers changed the inpatient order dialog for display of the expected first dose:

- If the schedule is an On Call schedule, CPRS does not display an expected first dose.
- On the Complex tab, if CPRS finds a PRN schedule, it will not display an expected first dose.
- On the Complex tab, if CPRS finds a Then conjunction, it will not review any of the lines following that entry.

HDS software involved in resolving PSI-05-026: OR\*3.0\*243.

- PSI-05-027 (CQ 14252 ) and PSI-07-135 (CQ 15176) Viewing Multiple Anatomic Pathology (AP) Reports in CPRS – Previously, anatomic pathology reports were text reports and users had to scroll through the report to find the wanted information.

Resolution: Developers changed the report format to a grid reports. Users can now select a date to view the information from that time.

-   
  PSI-05-048: System Changes Order from Lab Collect to Ward Collect (Remedy \#97102) ­– Previously, for inpatient lab orders that are of type “lab collect” or “immediate collect”, if a continuous schedule was selected (such as QD or QWEEKLY) and a child order falls on a day when the lab cannot perform the collection (for example, weekends or holidays), the collection type was automatically changed to “ward collect”, but CPRS did not warn the user.

Resolution: Developers added an advisory window that initially appears when the user selects “Accept” for that order, advising of any such changes to child orders. If these orders are left unsigned, the same advisory window will also appear at the point when they are signed or released at some future date.

HDS software involved in resolving PSI-05-048: OR\*3.0\*243.

- PSI-05-063: Incorrect data on Patient Inquiry Report (from CPRS) (Remedy \#102307)– To get patient demographics, a user can click once on the Patient Inquiry button. Previously, if a user double-clicked on the Patient Inquiry button and was changing patients, it was possible to get incorrect information. This happened infrequently.

Resolution: Developers changed CPRS so that double-clicking on the Patient Info button (located on the patient bar) will no longer open multiple dialogs. As a result, users will not see incorrect patient data in this box, due to double-clicking, and switching patients.

- PSI-05-065: When Ordering Fluid Bolus, Infusion Rate Does Not Display in Detailed Order Display when Finished as an IVPB (Remedy \#103019) – Previously, if a provider entered an order for an infusion bolus and entered a rate at which the fluid should be administered, such as 250 ml/hour, and the pharmacist saw the rate and finished the order as an intravenous piggyback (IVPB), the infusion rate information that the clinician entered when ordering a fluid bolus did not display in the CPRS Detailed Order Display. The inability of users on the ward, especially nurses, to see the rate might lead to patients being infused at an incorrect rate.

Resolution: CPRS displays IVPB infusion rate in CPRS Orders tab detailed display.

- PSI-05-093: Saving Patient Information in Personal Quick Orders Based on Resolved TIU Objects (Remedy \#69864) – Previously, it was possible to save personal quick orders with TIU objects in them. This caused a problem because when the quick order was saved, it had the information specific to the patient, and when a new patient was selected, the information from the TIU objects was not updated.

Resolution: This issue was mostly corrected in CPRS v26. But one uncorrected loophole remained: If a template dialog linked to a consult Reason for Request contained TIU objects, CPRS did not detect the TIU objects, and the order could still be inappropriately saved. CPRS now detects these objects and does not allow the user to save the personal quick order.

HDS software involved in resolving PSI-05-093: OR\*3.0\*243.

- PSI-05-103 Parts 1, 3, and 4: Order Check Overrides Not Transmitted to Ancillary Service – When a provider receives an order check with a danger level that the site has set as critical, CPRS requires that the provider enter a free-text reason for override. This reason for override text is kept only in the Orders file (file \#100), but the text is not transmitted along with the order to ancillary services, such as Pharmacy, Radiology, Laboratory, etc., that would act on the order. However, the provider may assume that the text is being sent.

Resolution: This PSI will be addressed in several parts. In CPRS v.27, these items have been changed:

- The “Return to Orders” button has been implemented on the order checks dialog. This does not cancel the order, but it does cancel the signature process. The provider could then return to the ordering dialog to rework the order.
- Developers created several reports that sites can run to review the critical order check override reasons. Reports can be extracted and sorted by division, display group, and other appropriate fields.
- Developers added a new note to critical order checks that reads “NOTE: The override justification is for tracking purposes and does not change or place new order(s).”

HDS software involved in resolving PSI-05-103: OR\*3.0\*243.

- PSI-05-106: Change the Review/Sign Items Form to Break the Orders Signature List into Three Different Groups – In CPRS, there is a parameter that enables sites to have some control of what orders are displayed on the Review/Sign Changes dialog. The parameter OR UNSIGNED ORDERS ON EXIT could be set to include NEW ORDERS ONLY, MY UNSIGNED ORDERS, or ALL UNSIGNED ORDERS. If sites used ALL UNSIGNED ORDERS, CPRS might display orders that were quite old, but had never been signed and the provider might sign orders that should not be signed.

Resolution: To address this issue, the CPRS Clinical workgroup and the Patient Safety Workgroup, made some recommendations. One of the recommendations was that if sites used the ALL UNSIGNED ORDERS options, the orders on the Review/Sign Changes dialog should be separated into three sections:

- My Unsigned Orders - This Session: This list contains all orders written by the current user in the current session.
- My Unsigned Orders - Previous Sessions: This list contains all orders written in previous sessions by the current user.
- Others’ Unsigned Orders - All Sessions: This list contains all orders written by other users.

This should enable providers to better identify which orders belong to them and which do not.

Another change was that when the user discontinues an unsigned/unreleased order, if the order was placed in the current ordering session the order is DELETED. If the order was placed in a different ordering session, then the order is CANCELLED. Deleted orders do not appear in the chart because other users never saw them, but it is possible that other clinicians saw the order placed in a different session so that information is retained in the chart and the order is given a CANCELLED status.

> **NOTE:** Note on Ordering Session—With CPRS 27, how CPRS behaves when a user discontinues (DC) an order is affected by the ordering session. If the order is DC’ed in the same ordering session in which it was created, then it is deleted and no longer remains in the database. If the order is DC’ed in a different ordering session, then the order is given a status of CANCELLED and is still in the database in file 100. Special attention should be given to when an ordering session actually ends. It ends in one of the following 4 ways:

- The user switches patients
- The user closes CPRS
- The user performs a Review/Sign changes Action
- The user performs a Refresh Patient Information

HDS software involved in resolving PSI-05-106: OR\*3.0\*243.

- PSI-05-116: Synonym Not Displayed beyond Initial Selection (Remedy \#123287) – In the medication ordering dialog, providers can select a medication by its generic name or by a synonym (usually the brand name). When the provider selects the medication, the second ordering dialog displayed the generic medication name without the synonym. If the provider selected the wrong medication and was not familiar with the generic name, the provider might not recognize that it was the wrong medication.

Resolution: To address this issue, the CPRS Clinical Workgroup recommended changing the Inpatient and Outpatient order dialogs to display both the generic name and the synonym in the order dialog, instead of the only displaying the generic name in the order dialog. Only the generic name is saved in the order. Therefore, the Orders tab display and the detailed display were not changed. The second order dialog, where the provider enters the rest of the order information, such as dosage, route, and schedule is the only dialog that developers changed.

HDS software involved in resolving PSI-05-116: OR\*3.0\*243.

- PSI-05-118: Caption on the Most Recent Labs Shows 00:00 when No Time Is Entered (Remedy \#123277) – For the caption on the Labs tab for the “Most Recent Labs” grid and Worksheet, if a lab result had a date but no associated specific time, CPRS was displaying “00:00” if no time was present for those results.

Resolution: If no specific time is entered (“T@U” for an unknown time), CPRS will display only the date. This change applies to the Most Recent Labs and Worksheet views and will not be visible to users until Lab patch LR\*5.2\*364 is also installed.

HDS software involved in resolving PSI-05-118: OR\*3.0\*243.

- PSI-06-014: How Epidural Routes Appear on the IV Tab in BCMA and Appear in CPRS Under IV Fluids Is Contributing To Medication Errors (Remedy \#128909, 178478)Note: Full resolution of this PSI will require changes in BCMA, Pharmacy Data Management, and Inpatient Medications

A site reported confusion on the part of a nurse because the medication was displayed on the IV tab in BCMA.

Resolution:

- CPRS now includes the medication route for solutions displayed in the Infusions group and on the detailed display.
- CPRS added three new fields to the IV Order dialog: Type, Route and Schedule.
- The new “<span id="no_continuous_default" class="anchor"></span>Type” field does not have a default. Users must select either “continuous” or “intermittent”.
- If the “Type” is “Continuous”, the Route defaults based on the Solution/Additive unless there was a conflict or none was selected. Then, the user must explicitly select a Route. An “Infusion Rate (ml/hr)” would need to be entered. The Schedule field would be unavailable.
- If “Type” is “Intermittent”, the Route defaults based on the Solution/Additive unless there is a conflict or none was selected. In that case, the user must explicitly select a Route. An “Infuse Over Time” value would need to be entered with a “Unit of time” designated, and a “Schedule” would need to be entered.
- New quick orders can be built using the new fields. A utility will be provided to “identify” quick orders that were done with an IV Dialog and lack data relevant to the new fields. IV quick orders that do not lack data for the new fields will be treated as continuous orders.
- When a user writes an intermittent infusion order with a schedule of ONCE, the following will happen in CPRS:
- Disable the display of DURATION
- Only VOLUME should be displayed
- Disable the doses, hrs, and days choices for VOLUME
- PSI-06-015: Dosage with an Initial Decimal Point Disallowed (Remedy \#129134) – Previously, a provider could enter a free-text dosage that began with a decimal point, such as .5MG, in an order dialog. This dosage could be misread as 5MG rather the .5MG. In addition, the provider could edit a dosage and the sig might not be updated if the provider made the change and immediately used the close (X) button of the dialog and accepted the order. In this case, a provider might have entered a dosage such as 5.5MG and then noticed the error and removed the initial number leaving a .5 dosage. But if the provider made the change and clicked the close button, the sig was not updated properly and the sig was saved as 5.5MG.

Resolution: Developers added a check to the dosage field so that if a provider enters a dosage with an initial decimal point, CPRS displays an error message stating that the dosage must begin with a numeric value. The provider will not be able to complete the order until the dosage has a numeric value before the decimal point. For example, if the provider enters a dosage of .5MG, CPRS will display the error message, and the provider would need to change the dosage to 0.5MG to avoid confusion. The order could then be accepted. The problem with editing a value and the sig not being updated was also corrected.

HDS software involved in resolving PSI-06-015: OR\*3.0\*243.

- PSI-06-023: (Remedy \#132020) – (Duplicate of PSI-05-006)
- PSI-06-041: Flag Does Not Display in VistA Outpatient Pharmacy (Remedy \#133716) – Previously, users could flag a pending order in CPRS, Inpatient Medications, or Outpatient Pharmacy, and the flag would display in CPRS and Inpatient Medications, but not in Outpatient Pharmacy. If one Pharmacist was working on an order and flagged it so that is was not acted upon by another Outpatient Pharmacist, the flag did not display in the Outpatient Pharmacy package, and another pharmacist could finish the order thereby creating a potential danger for the patient.

Resolution: The user may flag outpatient order and have the update sent to outpatient pharmacy.

HDS software involved in resolving PSI-06-041: PSO\*7\*225.

- PSI-06-045: (E3R \#18904) – (Duplicate of PSI-06-014)
- PSI-06-066: IV Fluid Order in CPRS with a Duration or Total Volume of a Fractional Dose (e.g., 0.5L) Causes Problem in Pharmacy Finishing (Remedy \#144913) – Previously, if a user entered an IV Fluid order in CPRS and used a fractional dose such as “0.5L” in the Duration or Total Volume window, the leading zero caused a problem when finishing the order in pharmacy.

For the pharmacy application, in field \#2, Solutions, instead of displaying IV Limit with the proper information, it displayed Duration: without a value. Also, in the display for START DATE/TIME and STOP DATE/TIME, the time span is only 6 minutes. Unless changed, the order would have only a 6-minute ACTIVE status and could easily be missed in BCMA because it could expire before the RN sees it.

Resolution: OR\*3.0\*254 addresses the PSI. Developers also changed CPRS (OR\*3.0\*243) to consistently manage entry of leading zeros at the user interface level. CPRS v.27 forces the provider to add a leading numeric value when entering a fractional duration for ml and L. This change also applies to the volume/strength field on the Infusion dialog.

- PSI-06-068: See PSI-05-001
- PSI-06-088: Consults Alert Changes (Remedy \#151414) – When sending alerts on addition of a comment to a consult request, no distinction was made between service update users defined at the service level and update users defined as “unrestricted access” for that service. Alerts were being sent incorrectly or not sent at all as a result of this.

Resolution: CPRS developers made the necessary changes to support patch GMRC\*3.0\*55 that will correct the issues when installed.

- PSI-06-104: RDV Health Summaries via CPRS (Remedy \#139560) – Previously, when using the CPRS Reports tab, if a patient had remote Department of Defense (DOD) data available and the user attempted to retrieve a Health Summary report via the DOD tab (with Dept. of Defense checked in the Remote Data button), the report did not populate.

Resolution: This problem goes beyond Health Summary reports and what is displayed when using or not using DOD/FHIE sites/Reports. All reports will experience this problem depending on what the user has selected and which remote sites are in an active query. The same issue will exist when the HDR comes online for CPRS.

Developers provided “cognitive” information when data is excluded on a report query. For text reports only, CPRS adds a comment that describes the problem where the report would normally be. For ‘grid’ type reports, the error comment is put in the first column (after the facility name) of the report. Here are some examples of the comments that could show up, depending on the type of query and what the user has selected:

- \<No HDR Data Included\> - Use “HDR Reports” menu for HDR Data.
- \<No HDR Data\> - This site is not a source for HDR Data.
- \<No DOD Data\> - Use “Dept. of Defense Reports” Menu to retrieve data from DOD.
- \<ERROR\> - Unable to communicate with Remote site

In addition to this text, error messages will also be shown after each remote site listed under the (blue) Remote Data View button, when appropriate.

Also, additional data has been added to the OE/RR REPORTS file (#101.24) to resolve this problem, which means that this file will be re-exported, with data, in patch OR\*3.0\*243. As part of the installation (pre-init) process, entries in this file with internal numbers greater than 999 will be deleted and re-installed.

- PSI-06-126: Duration Not Always Sent from CPRS to Inpatient Medications (Remedy \#158989) – When an IV Quick Order with a duration defined the duration field was auto-accepted, the duration was populating the Order File, but it was not sent to the Pharmacy package.

Resolution: CPRS now passes the duration to the Pharmacy package. In addition, CPRS now has additional validation that the entry is appropriate to be passed. If the user enters a value, such as 3, and a unit, such as days, but the user then changes the unit to hours, CPRS will remove the 3 and force the user to reenter the value. This is to prevent duration errors. If the user writes an order that has a duration type, but the user does not enter a duration, CPRS will not accept the order, but will display a warning message.

- PSI-06-134: See PSI-05-001
- PSI-06-145: Demographic Button and Tab Information for Different Patients

Resolution: Developers corrected this problem.

-   
  PSI-06-167: Auto-DC Rule Does Not DC the Meds when Medication Order Has an Outpatient Location (Inpatient Status) as the Ordering Location (Remedy \#167203) – Previously, if an inpatient went for an outpatient visit (or appointment) and the provider changed the location in CPRS from the inpatient location to the outpatient location and entered medication orders, the result was that the order filed under the outpatient order location and under Inpatient Meds display group. If at a later date, the patient has a treating specialty change, CPRS discontinues all medication orders EXCEPT those entered with the outpatient location. In discontinuing the medication orders, the software checked the patient location where the order was entered, and if the location was an outpatient location, the order did NOT get discontinued. 

Resolution: Developers changed the CPRS Auto-DC rules to DC the order if it is an inpatient order no matter if the ordering location is an outpatient location.

- PSI-06-170: Default Value in TIU Template Dialog Can Be Set to Incorrectly Checked (Remedy \#166177) – Previously on TIU template dialogs that had nested check box lists (where selecting the first level activated the second level of check boxes) and one of the second-level check boxes was a default, it was possible when the user unchecked the default and went to another nested check box item that the default item was once again checked when it should not have been.

Resolution: Developers corrected the behavior where the check box could automatically become checked again, and the check boxes should now function correctly.

- PSI-06-172: Custom Order View Does Not Display Unverified by Nursing Orders Correctly after CPRS v. 26 (Remedy \#168472)

Resolution: Developer changed the routine used to retrieve orders based on date and time to properly handle date and time.

- PSI-06-173: Providers without DEA Number Can Place IV Quick Orders (Remedy \#167843) – Previously, providers who did not have a DEA number, and therefore were not authorized to place some orders, could place these orders through the IV quick order features.

Resolution: Developers changed CPRS to cancel out of an IV Quick Order when the provider does not pass the pharmacy DEA check. The same check now occurs when the user is signing the order to catch auto-accept quick orders.

- PSI-06-192: User May Give Additional Dose Now in the Inpatient Medication Dialog Box with a Medication Schedule of ONCE or ONE-TIME (Remedy \#172339) – Previously, CPRS allowed the user to select the “Give additional dose now” checkbox in the inpatient medication dialog box with medication schedules of ONCE or ONE-TIME if the user was changing the medication order, transferring outpatient medications to inpatient medications, or copying to a new order. The checkbox was NOT selectable when the user was entering the medication the first time. The checkbox being selectable allowed the user to place two orders for the same medication, but CPRS did NOT alert the physician by displaying a pop-up warning dialog box as did the other schedules that told the physician two orders for the medication had been created.

Resolution: Developers modified CPRS to not display the “Give additional dose now” checkbox for any ONCE or ONE-TIME schedule.

- PSI-07-013: Orders Are Not Discontinuing as Expected--Error Message States “Invalid Pharmacy Order” (Remedy \#175403) – Duplicate of PSI-05-007.
- PSI-07-014: See PSI-05-001
- PSI-07-025: Update Provider/Location--Primary Focus Is Not on Encounter Provider (Remedy \#166051) – In CPRS v.25, when the user went to “Update Provider/Location”, the primary focus when the dialog opened was on the encounter provider, but with CPRS v.26, the focus was changed and the primary focus was on the bottom portion of the screen — Visit Location for outpatient medication orders, Clinic Appointments for inpatient medications, etc.

Resolution: Developers modified CPRS GUI v.27 so that the focus defaults to the Provider list box for non-provider users.

- PSI-07-031: See PSI-05-001
- PSI-07-036: Epidural QO with Default of IV Route May Result in Epidural Given via IV Port (Remedy \#178478) – Duplicate of PSI-06-045.
- PSI-07-046: Delayed Orders Entered for Transfer to Surgery Cancelled on Discharge from Observation (Remedy \#180390, E3R \#20065) – When an inpatient was in a ward with an observation treating specialty and the patient was transferred, the delayed orders were inappropriately cancelled.

Resolution: Developers changed CPRS so that transfer events will no longer be selectable from the delayed orders event selection list for patients in an observation treating specialty.

- PSI-07-057: Potential for Inappropriate or Misleading Provider Comments to Be Automatically Included on New Medication Orders (Remedy \# 151112, 173739, 182047) – For outpatient medications, a patient safety issue arose because a provider could inadvertently include the comments for an outpatient medication when doing a renew, copy, or change action on an existing order.

Previously, when placing an outpatient medication order in CPRS, the provider could include the default Patient Instructions (if any exist) for the medication and could include additional instructions to the pharmacist in the Provider Comments. When finishing the order, the pharmacist could copy the Provider Comments into the Patient Instructions to create one set of instructions for the patient; the final sig returned from OP contains only this one instruction, and the order is changed in the Orders file to reflect the update if necessary.

CPRS keeps both the original Provider Comments and the updated Patient Instructions with the order. If the order text was rebuilt as a result of a copy, renewal, change, or transfer, CPRS included both in the dialog.

Resolution:

- CPRS does not bring the Provider Comments forward for the Copy to New, Renewal, and Change actions.
- CPRS DOES bring forward Provider Comments when transferring medications from outpatient to inpatient.
- Both items are still retained in the detailed display.
- PSI-07-063: Schedule Missing from Two CPRS Reports on the Reports Tab / Clinical Reports / Pharmacy – Previously, the schedule did not display on two reports, those dealing with active IV medications and all IV medications.

Resolution: Developers added the schedule to both of these reports.

- PSI-07-177: Display on “Medication Nearing Expiration” Alert Does Not Match Status of Order – An expiring medication may not get renewed or there may be a delay in renewal since what is displayed on the CPRS Orders tab upon processing the “Medications nearing expiration” alert doesn't appear to match the status of the order. The user is routed to the correct order, but the status displays as “dc/edit”. The reporting site stated they had to use CPRS Orders tab “Custom View” for a Date Range to find the "expired" orders to renew.  
    
  Resolution: CPRS GUI v27 has been modified to include an indirect fix for PSI-07-177. Currently when a user processes a “Medication Nearing Expiration” alert (after the expiration date/time) on a changed inpatient meds order (order with an ACTION of change), the user will be directed to the list of “expired” (status) orders under the Recently Expired Orders view of the Orders tab. Only those orders that have “expired” will be displayed in the corresponding view and not those that have been “Discontinued/Edit” or “dc/edit”. If the alert was processed before the expiration date/time, CPRS directs the user to the list of orders (with a status of ACTIVE) that are going to expire soon under the Medications, Expiring view on the Orders tab.
- PSI-07-212: Upon Patient Movement, the Event-Delayed NPO Order Was Discontinued, Causing the Activation of a Regular Diet

Resolution: This is not easily corrected, if possible at all, but the user is now prompted about the possible conflict, and instructed on how to prevent it from happening by entering explicit start and stop date/times for any diet orders defined for that same release event. Developers also added code to check for auto-accept diet quick orders, immediate and delayed, that would auto-DC because of overlapping start/stop times. For event-delayed, auto-accept diet quick orders, CPRS checks for conflicting orders for the same release event, and if the user answers NO to the prompt about having adjusted the start/stop dates, CPRS displays the diet order dialog with that quick order pre-loaded so date adjustments can be made.

- PSI-08-019: CPRS Freezes When Users Double-Click Reminders – Previously, providers using reminders would sometimes double-click on a reminder and it would freeze CPRS.

Resolution: Developers corrected the problem—inadvertent double-clicking on reminders no longer freezes CPRS.

- PSI-08-066: Cannot See Notes in Remote Data
- PSI-08-079: An Alert Will Not Be Forwarded to a Recipient if the User Types in a Name Then Presses the ENTER Key when Forwarding an Alert from the CPRS GUI Patient Selection Screen – An alert will not be forwarded to a recipient if the user types in a name then presses the \<ENTER\> key when forwarding an alert from the CPRS GUI Patient Selection screen. The user may think they are forwarding the alert but they are not. (To forward to the named entry, the user must use the mouse.)

This is a patient safety concern in that patient care may be delayed or missed since the alert is not sent.

Resolution:  CPRS was modified to include an ‘ADD’ and ‘REMOVE’ buttons so that someone can add/remove recipients without having to use the mouse. They can ‘enter’ to select, but there are also the buttons.

<span id="_Toc221409092" class="anchor"></span>Known Issues

<span id="_Toc221409093" class="anchor"></span>Bidirectional Health Information Exchange (BHIE)

- BHIE-Inconsistency in Display of DoD Vitals, Cytology, Anatomic Path DataDescription:

In CPRS 27, the Lab Anatomic Pathology report (CY, SP) formats were changed in response to a PSI. The same changes could not be made to the reports used for Bidirectional Health information Exchange/Department of Defense (BHIE/DOD) until the changes were coordinated with similar changes on the BHIE/DOD side of things. Until the BHIE/DOD versions of these reports are made consistent with the VA versions of these reports, they cannot include a mix of both VA and DOD data in a single report, which is the way it was prior to CPRS 27.

Risk/Impact: Low Risk/Low Impact.

Workaround: Data is available but not co-mingled

Comments: As soon as the BHIE/DOD version of these reports can be changed to be consistent with the new formats found in CPRS 27, the changes necessary to re-integrate VA and DOD data into these reports will be made in CPRS. Software requirements to implement the report format modifications were provided to DOD in January 2008.

- BHIE-Graphing on VA pt,-\>changed to DoD pt-\>went to DoD- Vitals -\> clicked on REMOTE DATE-\>selected DoD, graph opensDescription: This problem occurs when a user selects a patient and graphs blood pressure (BP) for local data, then selects new patient and changes the view to the Cover Sheet tab. When the user clicks on the Reports tab, the BP graph reappears for about 0.5 seconds and then disappears immediately.

Risk/Impact: Low Risk/Low Impact

Workaround: None

Comments: This is considered a minor annoyance and has been resolved in CPRS GUI v27.n

<span id="_Toc221409094" class="anchor"></span>Notes/Note Tools

- Template Editor: Problem with ASSOCIATED CONSULT SERVICE FieldDescription: When the user types in the name of the *Associated Consult Service* field to associate this template with Consult a message box displays indicating this service is already assigned to another template. If I type in only M then I am allowed to scroll through the list of consult titles that begin with M to find the one I want to use. This happens with all consults; not just this one

Risk/Impact: Low Risk/Low Impact

Work Around: If the user types in the first character, they may scroll through the list of consult titles and select the desired entry.

Comments: Only Clinical Application Coordinators use this functionality. The problem is considered an annoyance and resolution has been deferred to CPRS GUI v27.n

- CPRS Will Not Find or Highlight a Key Word that Is Being SearchedDescription: This problem occurs occasionally when the user selects View, Search for Text, Find, types a key word in to search for in the progress notes, and CPRS will not find or highlight the word that is being searched for.

Risk/Impact: Low Risk/Low Impact

Work Around: The problem occurs occasionally. When the user re-attempts the search, the search is successful.

Comments: The problem was reported and then fixed. After t77 was created, the site reported that the problem continues to occur occasionally. It has been deferred for resolution in CPRS GUI v27.n

> Orders

- Cannot Create a Unit Dose Quick Order Using the Format Available in the Quick Order EditorDescription: When creating the Quick Order (QO) in VistA, if a dosage is not selected as part of QO creation, then the QO dialog does not present Route or Schedule for selection (these options are bypassed).

Risk/Impact: Low Risk/Low Impact

Work Around: On GUI, the QO can be selected, but user must then fill-in the route and the schedule along with the DOSAGE.

Comments: This is viewed as an annoyance and has been deferred for resolution in v28.

- Order Displays under Inpatient Meds on Meds Tab but Not on the Orders TabDescription: In the reported issue, both orders captured were still active, and the discontinue (DC) action was unsigned, which was correct; the only problem was with the Out Patient display group on the inpatient med order released after admission.

The new order was created by copying and delaying the original order, so the new order was tied to a release event. Because it was a manual event and the patient was not yet admitted, the Out Patient meds display group was assigned and that prevented the order from displaying in the Active view on the Orders Tab after release since the patient had been admitted by then.

Risk/Impact: Low Risk/Low Impact

Work Around: None

Comments: This scenario will be reevaluated in CPRS GUI v29 when delayed events and locking will be reevaluated in conjunction with Inpatient Medication, Outpatient Pharmacy, and Registration. There are several PSIs documenting similar issues that will be addressed in CPRS GUI v29.

- Error Message on Nurse Verification of IV Order—\<UNDEFINED\>LIMSTOP+7^PSIVORFBDescription: An \<UNDEFINED\>LIMSTOP+7^PSIVORFB error occurs when Nurse Verification of an IV Order is initiated. This problem occurs in Inpatient Medications code.

Risk/Impact: Low Risk/Low Impact

Work Around: None

Comments: This is a known issue that will be addressed in PSJ\*5\*207, which is in the queue for national release immediately after CPRS GUI v27. The problem is documented in Remedy tickets 230800 and 233925.

- Can’t Change, Renew, or Copy To New Order an IVPB Solution—Must Rewrite Entire Order and DC Soon To Expire OrderDescription: This problem has been reported by one provider at Hudson Valley Health Care (HVHC). It cannot be duplicated by development staff. No other CPRS GUI v27 test site has experienced this problem. It is believed that this may be a set-up issue at the site.

Risk/Impact: Low Risk/Low Impact

Work Around: User would need to enter a new order.

Comments: This is believed to be a set-up issue. The ticket has been left open in case another site reports this problem. Since the development team cannot duplicate the problem, it is not possible to fix it.

- Incorrect Location Displayed on Visit Location Switch FormDescription: Northern California Health Care System reported a single incident where a NHCU patient was seen in an outpatient clinic and when orders were entered, the Visit Location Switch Form displayed the incorrect location.

Risk/Impact: Low Risk/Low Impact

Work Around: Select the correct location.

Comments: This issue has only been reported once. The development team has not been able to duplicate the problem but believes that a specific sequence of steps may prevent a variable from being killed (cleared). This ticket has been left open for further evaluation in CPRS GUI v28.

- "CPRS - Patient Chart" Error Dialog" Reappears No Matter Which Signing Method Is UsedDescription: This problem has existed since CPRS GUI v27.2 when a correction was made to address: CQ: 10073 - PSI-05-106 Accidental Signing of Old Orders in CPRS. The occurrence of this problem is very, very rare and occurs only when the steps to duplicate it are explicitly followed. Only Charleston reported the problem, and Steve produced the problem when testing another PSI. In order to test that PSI, he had to set up the environment that created this problem.

One must initiate delayed orders for two patients during the same ordering session, the delayed event must occur before the orders are signed; the problem occurs on the second patient.

Risk/Impact: Low Risk/Low Impact

Work Around: Shut down CPRS and log-back in. The order is available for signing.

Comments: This problem has not been reported by any site even though the issue has existed since testing began in April 2007. It was reported when the specific environment was set-up to test another PSI. This has been deferred for resolution in CPRS GUI 27.n

<span id="_Toc221409095" class="anchor"></span>Other

- Name of Patient Changes, But The Chart Does NotDescription: One provider at Hudson Valley Health Care has reported this problem. No other users at any site have experienced this issue. The problem occurred when the provider started following-up on her patient at her office workstation and left her office to do rounds. She locked her workstation, but did not log-out of CPRS. She then did rounds and access several other workstations on the wards. Finally, when she returned to her office and selected a new patient, she noticed that the Notes tab and the Orders tab included data from the previous patient.

Risk/Impact: High Risk/High Impact

Work Around: Completely log-out of CPRS and log back in. All tabs are refreshed appropriately.

Comments: This problem was reported by one provider in February and has occurred multiple times but cannot be duplicated. No other providers have reported the problem. Several measures have been taken to prevent this from happening for this provider; CCOW has been disabled; CPRS timeout has been implemented; activation of multiple concurrent CPRS sessions has been prevented. Despite multiple attempts to shadow the provider and attempt to duplicate the problem, it cannot be duplicated.

The development team continues work on this problem and will resolve it as soon as the problem can be duplicated.

- Sign Order Box Never DisplaysDescription: This problem only occurs when the previously described issue occurs. A provider signs onto CPRS enters an order and goes through the steps of signing the order but is unable to sign the order because the sign order box never displays.

The provider then switches to a different patient and the order written on the original patient appears in the new pt's order display as an unsigned order.

Risk/Impact: High Risk/High Impact

Work Around: Completely log-out of CPRS and log back in. All tabs are refreshed appropriately and this problem does not occur.

Comments: This problem was reported by one provider in February and has occurred multiple times but cannot be duplicated. No other providers have reported the problem. Several measures have been taken to prevent this from happening for this provider; CCOW has been disabled; CPRS timeout has been implemented; activation of multiple concurrent CPRS sessions has been prevented. Despite multiple attempts to shadow the provider and attempt to duplicate the problem, it cannot be duplicated.

The development team is continues work on this problem and will resolve it as soon as the problem can be duplicated.

- MH DLL Active Screen behind CPRSDescription: When a user attempts it execute the Mental Health DLL from within CPRS (typically using a Clinical Reminder that executes a Mental Health testing instrument), the MH DLL form is partially hidden by CPRS.

Risk/Impact: Low Risk/Low Impact

Work Around: The user can click on the Mental Health DLL and give it focus.

Comments: CPRS GUI v27 resolves numerous problems where forms were inaccessible because they were hidden; however, use of the MH DLL was introduced with CPRS GUI v27. This form is partially hidden, but accessible. This will be addressed in CPRS GUI v28.

-   
  RDV Reports from v.26 Displayed in a v.27 AccountDescription: In CPRS v.27, developers added a new field called “Reason for Study” to accommodate the need of third-party radiology products. As a result, the Radiology reports in CPRS v.27 also changed. This created a problem with the display of reports created in v.26, but displayed in v.27. The new field created a mismatch between the headings in the report, and the data that followed as shown below in the following two captures.

A v.26 Report as Shown in a v.26 Account

Exam Date/Time

10/15/2005 10:51

Procedure Name

CHEST 2 VIEWS PA&LAT

Clinical History

increased hypoxia over last several days

Impression

1\. Left basilar consolidation most likely an infective process.

2\. Somewhat improved right basilar infiltrate since August, but not yet clear and extensive underlying chronic changes.

3\. Atherosclerosis without frank congestive heart failure.

D: 10/15/2005 1133 T: 10/15/2005 1134 msk3

Signing Radiologist: Contributing Radiologist(s):

Radiologist Physician Assistant:

Addenda

Report Status: Final This report has been electronically signed on: Saturday, October 15, 2005

Report

CHEST, SINGLE VIEW

COMPARISON: AP upright chest examination with the patient sitting in a

wheelchair was compared with a study from 8/24/05.

FINDINGS: An infiltrate has developed in the left base along with a small amount of pleural fluid. There are chronic changes throughout the lungs and patchy infiltrate at the right base although this area has improved since the previous examination. The heart size is normal. There is atherosclerotic disease in the aorta. Pulmonary vasculature is normal. There is an old fracture of the right clavicle and several right ribs.

Facility: CHEYENNE HDR SQA

  
A v.26 Report as Shown in a v.27 Account

Exam Date/Time

10/15/2005 10:51

Procedure Name

CHEST 2 VIEWS PA&LAT

Reason for Study

increased hypoxia over last several days

Clinical History

1\. Left basilar consolidation most likely an infective process.

2\. Somewhat improved right basilar infiltrate since August, but not yet clear and extensive underlying chronic changes.

3\. Atherosclerosis without frank congestive heart failure.

D: 10/15/2005 1133 T: 10/15/2005 1134 msk3

Signing Radiologist: Contributing Radiologist(s):

Radiologist Physician Assistant:

Addenda

Report Status: Final This report has been electronically signed on: Saturday, October 15, 2005

Impression

CHEST, SINGLE VIEW

COMPARISON: AP upright chest examination with the patient sitting in a

wheelchair was compared with a study from 8/24/05.

FINDINGS: An infiltrate has developed in the left base along with a small amount of pleural fluid. There are chronic changes throughout the lungs and patchy infiltrate at the right base although this area has improved since the previous examination. The heart size is normal. There is atherosclerotic disease in the aorta. Pulmonary vasculature is normal. There is an old fracture of the right clavicle and several right ribs.

Report

\[+\]

Facility: CHEYENNE HDR SQA

In these examples, the new field moves the data up one level. The Clinical History now displays under the Reason for Study, the Impression moves up to display under Clinical History, etc.

Risk/Impact: Low risk/Low impact

Work Around: None

Comments: This issue should be resolved when all sites have installed CPRS v.27.

<span id="_Toc221409096" class="anchor"></span>Parameter Description – OR CLOZ INPT MSG

The parameter description for OR CLOZ INPT MSG is somewhat unclear. Because it is only the description, it does affect how the parameter works. The current description is:

This parameter allows sites to set what text they would like for users to see when an inpatient order of Clozapine is made. This drug is generally ordered in an outpatient setting and thus is subject to the special order appropriateness checks. However, when ordered in an inpatient setting these checks are not done. Thus sites should determine a policy to handle this and provide instructions to users based on that policy.

The correct description, which is included in the CPRS Technical Manual: GUI Version and will be included in the next build of CPRS, is the following:

Clozapine is usually prescribed in an outpatient setting, but it can be ordered for inpatients. However, the special appropriateness order checks that occur when finishing in the backdoor Outpatient Pharmacy setting do not occur in the finishing process in backdoor Inpatient Pharmacy. In addition, backdoor Outpatient Pharmacy sends the clozapine information to the National Clozapine Coordinating Center (NCCC) database. Some sites have directed the ordering provider to place a corresponding outpatient order when placing an inpatient clozapine order. The sites that have this policy can use the new OR CLOZ INPT MSG parameter to help reinforce this policy to the ordering providers.

<span id="_Toc221409097" class="anchor"></span>VBECS—Blood Product Management

All the VBECS issues listed below will be considered for resolution in CPRS GUI v27.n. Only two sites, Philadelphia and St. Louis, have implemented VBECS in production. San Diego is scheduled for production installation of VBECS on August 9, 2008. All of these issues have been discussed with the CPRS/VBECS test sites.

Reports of CPRS/VBECS issues have been delayed due to the limited production testing of CPRS/VBECS ordering functionality. Philadelphia installed VBECS into production initially, and then St. Louis installed on July 19. The problems listed below were reported after CPRS GUI v27.77 was created. In conjunction with the CPRS/VBECS test sites, a decision was made to proceed forward with national release and address these issues in either CPRS GUI v27.n or CPRS GUI v28.

- VBECS-San Diego-Quick Orders: Labs linked to Whole Blood and RED BLOOD CELLS Do Not Display in “Lab Results” of DialogDescription: Lab results are being displayed properly when they are available and are supposed to be displayed; however, the tab changes from “Lab Results” to “Lab Results Available”, even when there are no results available. This is misleading. The tab should remain “Lab Results” if there are no results to be displayed.

Risk/Impact: Low Risk/Low Impact

Work Around: N/A

Comments: This has been resolved in CPRS GUI v27.n

- VBECS: “Date/Time Wanted” Does Not Display in the Printed/Displayed Lab Order in CPRSDescription: “Date/Time Wanted” Does Not Display in the Printed/Displayed Lab Order in CPRS

Risk/Impact: Low Risk/Low Impact

Work Around: Date/Time Wanted is displayed on Detailed Display of the order.

Comments: This issue was discussed with the test sites on 6/12. There was unanimous agreement that displaying the “Date/Time Wanted” in the order detailed display was sufficient for this version.

- VBECS-Non-Quick Order VBECS Dialog: System Thinks that ‘Now’ Is a Time in the PastDescription: In a Quick Order and a “Non-Quick Order”, when the user creates an order and adds a Diagnostic test, clicks to open the Change Date/Time for the Collection Date/Time and clicks the "NOW" button, clicks OK and then clicks Accept Order, CPRS displays a message stating that “Collection times in the past are not allowed”.

Risk/Impact: Low Risk/Low Impact

Work Around: User may enter a date/time.

Comments: Current functionality is consistent with the Lab dialog. If a change is made, it should be done to both the Lab order dialog as well as the Blood Bank order dialog. This will be reviewed by CPRS Clinical Work Group and evaluated whether it should go in V28.

- VBECS Date/Time, Urgency Elements Need to Be Consolidated or Cross ExaminedDescription: St. Louis surgeons reported June 19, 2008, that The Date/Time’s and Urgency elements need to be consolidated or cross examined. Blood Component, Diagnostic Tests, and Urgency can each have its own time. Blood Component can be set to NOW, TYPE AND SCREEN can be set to Next scheduled lab collection, and Urgency can be set to Routine.

Risk/Impact: Low Risk/Low Impact

Work Around: N/A

Comments: This was reported with CPRS GUI v27 t77. The site agreed that it could wait for resolution until CPRS GUI v27.n

-   
  VBECS Input Validation; Blood Component Field Allows Free TextDescription: Blood Component field allows free text. It doesn’t validate the entry until the Accept Order button is pressed. Validation should be triggered as soon as the focus changes the user down-clicks another field.

Risk/Impact: Low Risk/Low Impact

Work Around: N/A

Comments: This was reported with CPRS GUI v27.76, but was considered a low priority by the site. It will be evaluated for resolution in CPRS GUI v27.n

<span id="_Toc221409098" class="anchor"></span>New Parameters

CPRS v.27 (OR\*3.0\*243) adds several new parameters. These parameters should be set by the person at your site that normally controls the parameter settings. Some parameters can be set by the user while some must be set by a Clinical Applications Coordinator (CAC) or Information Resource Management (IRM) personnel. A CAC or IRM staff should set the parameters below.

- OR ADMIN TIME HELP TEXT
- OR CLOZ INPT MSG
- OR DC REASON LIST
- OR FLAGGED ORD REASONS
- OR LAPSE ORDERS
- OR LAPSE ORDERS DFLT
- OR MEDS TAB SORT
- OR RA RFS CARRY ON
- OR USE MH DLL
- ORWDXVB VBECS TNS CHECK
- ORWLR LC CHANGED TO WC

For more information on these parameters, please consult the *CPRS Technical Manual: GUI Version*.

<span id="_Toc221409099" class="anchor"></span>New Functionality

<span id="_Toc221409100" class="anchor"></span>About Box

- About CPRS Dialog Has Incorrect Email Address

Resolution: Developers changed the email address to the correct email address.

<span id="_Toc198000111" class="anchor"></span>Encounter Form and Signature Forms

- New Environmental Indicator: SHD (Shipboard Hazard And Defense) – Developers added a new Environmental Indicator to Co-pay and CIDC Review and Sign Orders dialogs—SHD. The encounter form has also been modified to prompt for the new option (SHD). The SHD definition will display as a hint when the provider hovers over “SHD” in the co-pay portion of the Order Signature dialogs or uses the keyboard combination Alt + h.

The Health Frame information is as follows:

Veterans with conditions recognized by VA as associated with Project 112/ SHAD, shipboard and land-based biological and chemical testing conducted by the United States (U.S.) military between 1962 and 1973 are eligible for enrollment in priority group 6, unless eligible for enrollment in a higher priority. In addition, veterans receive care at no charge for care and medications provided for treatment of conditions related to exposure.

<span id="_Toc221409102" class="anchor"></span>Meds

- New Sorting Capabilities on the Meds Tab – Developers added the capability to sort the medications on the Meds tab in the following ways:
- Sort by Status/Exp Date (IMO first on Inpt)
- Sort by Status Group/Status/Location/Drug Name
- Sort by Drug (alphabetically)/status active/status recent expired

<span id="_Toc221409103" class="anchor"></span>Orders

- New Blood Bank (VBECS) Ordering Dialog – With CPRS v.27 and OR\*3.0\*212, CPRS adds a new dialog that will enable clinicians to electronically order blood products using the VistA Blood Establishment Computer System (VBECS). This new dialog has three tabs: Patient Information, Orders, and Lab Results.

The Patient Information tab shows blood product information, such as available units, those that are autologous, directed, and allogenic. It gives information such as lab accession number for units and what their status is, such as are they just available, have they been cross-matched, or have they been assigned.

The Orders tab is where clinicians place orders for various blood products, for units of blood, plasma, red blood cells, platelets, for example. The dialog will prompt the user for needed information, such as ordering a type and screen for some units. Users can also place the order and put a desired date when the blood product is needed, such as for a future surgery.

The Lab Results tab shows the results of lab tests the may have been ordered related to the blood products. The lab results are displayed in this tab for the user’s convenience so that they do not have to go to the Labs tab for information when ordering blood products.

- Radiology “Reason for Study” Prompt – The Radiology package is implementing a PACS messaging and Voice Recognition interface that needs “Reason for Study” split out from “Clinical History”. Prior to this version, “Clinical History” had been a catch-all; it collected unlimited text which the users have been accustomed to entering both the clinical history of the patient and the reason for the study.

Resolution: Developers added a new “Reason for Study” prompt to the Radiology ordering dialog. CPRS still prompts for “Clinical History”, but it is no longer required, while “Reason for Study” is a required entry. Until Radiology patch RA\*5.0\*75 is released, both items will still appear in “Clinical History” in that package, but will appear separately in the ORDERS file.

Developers also added validity checking to CPRS for the optional “Clinical History” field. Following Radiology’s validation rules, CPRS will validate that this field contains at least one occurrence of two consecutive alphanumeric non-space characters. If it does not find them, CPRS will display a warning message and will not accept the order.

> **NOTE:** Radiology patch RA\*5.0\*75 will correct the issue where a user enters no Clinical History at all, and the order is rejected by Radiology on signature/release.

Also, to aid sites that have radiology quick orders that may need to be edited, developers created patch OR\*3.0\*281, which will search for VistA and personal radiology quick orders that have text defined in the existing History and Reason for Exam field. The patch will create a mail message with a list of quick orders—including disabled quick orders—that will need to be reviewed to see if the text should be edited. Part of the text now in the History and Reason for Exam field may need to be moved to the new Reason for Study field. The new field has a size limit of 64 characters so the change must be made by a person who can review what, if any, portion of the text should be moved into the new field.

IRM or CAC personnel can run the report after OR\*3.0\*281 is installed by using the ORCM RA STUDY option.

- New Clozapine Requirements

With the Food and Drug Administration required changes for administering Clozapine, the following criteria must be met for a provider to order Clozapine:

- The patient is part of the treatment program.
- The patient has proper WBC (White Blood Count) and ANC (Absolute Neutrophil Count) lab tests within the past 7 days.
- The ordering provider has the YSCL AUTHORIZED key.
- The ordering provider has a valid Drug Enforcement Agency number or Veterans Administration number (DEA/VA#).

The other order checks related to Clozapine will continue to work as they have prior to these changes.

Additionally, the values of the Days Supply, Quantity, and Refills fields are restricted based on the type of patient that Mental Health designates in their files when the provider is ordering Clozapine.

CPRS now prevents the user from renewing outpatient and inpatient Clozapine orders.

- Inpatient Clozapine Order Checks – Developers added inpatient Clozapine checks to the ordering process. CPRS now performs an order check when processing a Clozapine order for an inpatient. If the patient fails the check, the user will not be able to enter the Clozapine order. If the patient passes the check, the user will see a message if text has been defined in the OR CLOZ INPT MSG parameter.
- If an Inpatient Order Is DC’d at an Outpatient Location, Print the Order at the Inpatient Location

Resolution: Developers changed CPRS to automatically print to the inpatient ward for discontinued (DC) orders if the Nature Order allows printing. Because this is done automatically, the user should not see discontinued orders on the new print form.

<span id="_Toc221409104" class="anchor"></span>Parameter Description Changes

- Parameter Description Text Expanded – Developers updated descriptions for ORCH CONTEXT MEDS and ORWOR EXPIRED ORDERS in the PARAMETER DEFINITION file, 8989.51, to clarify that ORCH CONTEXT MEDS affects the Meds tab display, but ORWOR EXPIRED ORDERS affects the Orders tab. These parameters function exclusive of each other; changing one does not affect the other.

<span id="_Toc221409105" class="anchor"></span>Patient Record Flags

- Distinguish the Difference between Category I and Category II Flags – The Patient Record Flag (PRF) Advisory Board requested that CPRS developers enhance the PRF Category I flag display so that it is more distinct than Category II flags.

Resolution: On the PRF pop-up, developers separated Category I and Category II flag into different lists. Developers made Category I flags more distinct in following ways:

- Display in a separate section above Category II flags
- Are first in the tab order
- Display in larger fonts
- Background is bright orange
- The font color is white
- The Category I title flashes between white and black text

<span id="_Toc221409106" class="anchor"></span>Reports

- Supplemental Data for Pulse Ox Values on the Reports Tab

Four new fields have been added including:

- Flow Rate (l/min)
- O2 Concentration (%)
- Qualifiers
- Methods

BMI has also been added to the detailed display for weight values, when looking at non-HDR data. This new information will be displayed in the details when the values are clicked on in the grid display of the vitals.

A correction has also been made to the HDR All Outpatient Pharmacy report. Any set of results that has a SIG with a length greater than 60 characters will show “\[+\]” in the corresponding column.

- Bidirectional Health Information Exchange (BHIE) Only Sends Head Circumference/Girth Measure in Inches – The only circumference/girth that CPRS receives from the Department of Defense is the head measurement and it is only measured in inches. Because the measurement is not listed as a head measurement, providers must be aware that the circumference/girth measurement from a DoD location is a head measurement and it is in inches.

<span id="_Toc221409107" class="anchor"></span>Team Lists

- Exclude Personal <span id="team_lists" class="anchor"></span>Team Lists from GUI Applications – Previously, when a personal team list was created, it was visible to all users. This created clutter and could cause a breach of confidentiality if all patients on the list had HIV or some similar disease. Simply seeing the list might allow users to know more than they should about a patient.

Resolution: Developers added a new option to the ORLP TEAM MENU named ORLP TEAM LIST VISIBILITY. Personal Team lists can be updated singly or in batch. Visibility options are: OWNER or ALLUSERS. All new lists will be set to OWNER unless designated for ALLUSERS. Owners will need to set those that should be changed to ALLUSERS so that they can be seen.

<span id="_Toc221409108" class="anchor"></span>Defect Fixes

<span id="_Toc221409109" class="anchor"></span>Allergies

- Automatic Removal of Spaces Causing Mismatched Allergy Items – In some cases, a matching causative agent returned by the allergy search may legitimately contain a trailing space character. CPRS had been stripping any trailing spaces, in which case the causative agent was being stored without the space, causing a failure to match the correct value on file. The mismatch resulted in a free-text entry, and the failure of order checks to fire for these items.

Resolution: Developers corrected this problem.

- Remove Default for Value for Observed/Historical (E3R 19668) – Previously, the allergy dialog had a default for whether an allergy was observed or historical. User might not check to ensure that the correct value was selected.

Resolution: Developers removed the default value for the “Observed/Historical” radio button group, and the user will need to select one or the other to complete the entry of the allergy or adverse reaction.

- Users Can No Longer Change the “Originator” on Allergy Entry Dialog – Previously, on the Allergy Entry dialog, the “Originator” defaulted to the user who was logged in, but the user could change the “Originator” to another user. This was not consistent with the List Manager version of the Adverse Reaction Tracking package.

Resolution: Developers changed CPRS so that the “Originator” selection continues to default to current user, but is no longer editable.

<span id="_Toc221409110" class="anchor"></span>CCOW

- CPRS Menu Items Inappropriately Enabled - CCOW menu items for BREAK and REJOIN were being inappropriately re-enabled on every patient change, even if a previous CCOW error had occurred.

Resolution: Developers corrected this problem. If a CCOW error occurs, the Break and Rejoin menu items will remain disabled for the duration of the session.

<span id="_Toc221409111" class="anchor"></span>Consults

- Consult Selection Not Holding as User Navigates Other Tabs – If a user selected a consult in the consult treeview, and then the user navigated to the Orders tab and placed a new order, the prior consult was no longer selected when the user returned to the Consults tab. The detailed display window was blank as well.

Resolution: Developers corrected this problem.

- Text Wrapping Problem in Consult/Procedure Reason for Request – When a user entered a consult or procedure, the text for the consult/procedure Reason for Request was correctly wrapping at 74 characters, as required to maintain List Manager and File Manager editor compatibility, but hard returns were being inappropriately inserted. This caused the text to break up and have a choppy appearance when saved.

Resolution: Developers corrected the problem so that the text correctly flows into paragraphs that are still 74 characters wide.

- Users Could Directly Edit or Skip Reason for Request Field When Using Templates – Previously, when a user was ordering a consult, cancelling a template dialog linked to a Reason for Request allowed this field to be edited directly, instead of requiring the entries on the template.

Resolution: In this version, cancelling out of a template dialog will also abort that order, following user confirmation.

- Canceling Reason for Request Dialog Template Does Not Abort Order

Resolution: Developers corrected two additional scenarios where cancelling a dialog template for a consults reason for request did not correctly abort the order as well.

- REQCOS+7^TIUSRVA Errors (Remedy# 157898, 154177, 155727) – When a user signs a Clinical Procedures class document from the Consults tab, CPRS first checks that all CP-required fields are present. Beginning with CPRS v.26, another check determines whether the expected cosigner is valid as of the date of the document. In this case, the Delphi variable containing the date was not yet defined, causing the above error on the server.

Resolution: This has been corrected.

- Access Violation on Consult Copy, Edit, or Quick Order – If a consult copy, edit, or quick order action attempted to load an entry that contained no consult service, an access violation would result.

Resolution: This has been corrected, displaying instructions to the user that tell them that the order or quick order chosen does not define a consult service and that they should contact their IRM or support staff.

<span id="_Toc221409112" class="anchor"></span>Date/Time Selection

- Users Can Select an Invalid Time (Remedy \#153432) – From the CPRS date/time chooser dialog, the user can choose 00:00 from the time columns. Since it’s unclear what that means in terms of a date, CPRS currently changes it to 00:00:01. (Similarly, clicking “midnight” enters a time of 23:59.) But then, back on whatever form called this dialog, those seconds are stripped from the time, leaving the time at 00:00, and that’s the time that gets used.

Resolution: Developers changed CPRS so that selecting an hour of “00” will cause the minutes of “00” to change to “01”, making the selection of a “00:00” time impossible. Typing in a “00:00” will result in a value of “00:01” being returned to the calling date box when OK is selected.

<span id="_Toc221409113" class="anchor"></span>Delphi 2006

CPRS v.27 was coded using Delphi 2006 rather than Delphi 6. That is a change of several versions. As a result, there were changes in CPRS that were related to Delphi changes. The corrections in this section show the problems that developers found in making the change from one version of Delphi to another.

- Delphi 2006 Space Bar Does Not Toggle the Checkbox in Checklist Boxes

Resolution: Developers made the Space bar once again toggle the checked state in a checklist box.

- Delphi 2006 Drop-down List Items Disappears – When developers placed a drop-down combo box with hints on a form that stayed on top, the drop-down list would quickly disappear after it was opened.

Resolution: The problem has been resolved.

- Delphi 2006 Problem Deleting CIDC Diagnosis – Users would get an access violation when attempting to remove a diagnosis from the “Assign Diagnoses to Order(s)” dialog.

Resolution: Developers corrected the issue by coding separate delete function.

<span id="_Toc221409114" class="anchor"></span>Discharge Summary

- Problems with Users Allowed to Cosign Discharge Summaries – Previously, it was possible for some users who should not have been allowed to cosign discharge summaries to do so.

Resolution: The complete solution to this problem will probably need to be addressed by role-based user classes, but this will be at a later date. For now, developers reinstated a check for “requires cosignature” document parameter for Discharge Summaries. The check was removed in 2001, CPRS v15.7. For the discharge summary user/title, the check looks at the user class of the author and if the author’s user class requires cosignature, the author cannot be selected as an expected cosigner.

<span id="_Toc221409115" class="anchor"></span>Encounters

- Resizing Encounter Form Mistakenly Clears Checkboxes (Remedy \#70150) – On the Encounter form, if some of the checkboxes were filled in and the user resized the dialog, CPRS would mistakenly clear the checkboxes.

Resolution: Developers corrected this problem.

- Hover Hint Gives Incorrect Information – A hover hint that said, “To sort, click on column headers", was included on the Encounter form. However, clicking on the column headers does not sort the columns.

Resolution: The columns in this dialog are not designed to sort. The hover hint has been removed.

- Replace “Environmental Contaminants” Label with “SW Asia Conditions”

Resolution: As requested, developers changed the term Environmental Contaminants to Southwest Asia Conditions on the Order Signature dialogs. The change was to the display only, no other changes made regarding SW Asia Conditions.

- Provider/Location Dialog: Cursor Does Not Default to Location Field - Remedy ticket 97390 originally reported an issue on this provider/location selection screen. After fixing that issue, the field requested that for inpatients the cursor should continue to default to provider rather than location.

Resolution: Developers have changed CPRS and the cursor location for inpatients now defaults to the provider.

- Cursor Defaults to Incorrect Location on Current Activities Dialog (same as Remedy \#97390) – In the Current Activities dialog, the cursor does not default to Visit Location field—requiring an additional click from the user to get to the right location.

Resolution: Developers changed CPRS so that the cursor now defaults to the Visit Location field for outpatients if the user is a provider.

<span id="_Toc221409116" class="anchor"></span>Graphing

- Items and Views Now on Separate Tabs

Resolution: Developers changed the graphing display to create two tabs: one for Items that users can select, and one for predefined views.

- Changes to Display of Non-Numerical (Free-Text) Results and Comments

Resolution: Developers improved the display of non-numerical results or data by placing them closest to the graph’s top or bottom margin. Values that begin with “\>” are displayed at the top of the graph, others are down at the bottom of the graph. By default, free-text values display. This can be toggled by clicking on the label that reads “free-text labels:”. Comments are shown with a label that reads “\*\*comment”. Clicking on this label will display details of all items on the graph.

- Views Definitions Can Be Displayed

Resolution: Developers added areas on the graphing windows that can show the definitions of views—detailing the items included in the view.

- Users Can Select Lab Groups for a View

Resolution: Users can now select lab groups to graph the items in them.

- Users Can View the Views and Lab Groups of Others

Resolution: Developers added the ability of users to see and use the views and lab groups of other users.

<span id="_Toc221409117" class="anchor"></span>Imaging

- Image Flag Added to Windows Messages

Resolution: Users will not see any changes as a result to this internal change. As requested by the Imaging team, developers added a 1/0 flag to piece 13 of certain Windows messages to indicate the presence/absence of images attached to the report or document. This is in addition to the display of the “image” icon for these items. Other CPRS messages will require API changes by an ancillary application before the flag can be included. The places that include the NEW messages are as follows. All other places in CPRS will continue to send the OLD messages, without piece 13 set to reflect the presence/absence of images:

- Consults tab – “Related documents” and med results in the lower treeview.
- Notes, Discharge Summary tabs - click on any note.
- Surgery tab - Click on a TIU document. Clicking on a case will still send the existing messages until an API is updated by Surgery.
- Reports tab - Imaging (local only), Clinical Reports/Progress Notes. All others will still be the old messages.

<span id="_Toc221409118" class="anchor"></span>Labs

- Display of Lab Time Could Be Misleading (PSI-05-118) – On the Most Recent Labs and Worksheet views, developers changes CPRS to not display a time of “00:00” if Lab entered a result date/time of “T@U”, representing an unknown time.

Resolution: In this version, the same correction has been applied to the dates/times in the “Worksheet” display. Neither change will be visible to users until associated Lab patch LR\*5.2\*364 is installed.

<span id="_Toc221409119" class="anchor"></span>Launching CPRS

- Borland .DLL Check Prevents Access Violations – Previously, if a user launched CPRS and an incorrect version of the BORLNDMM.DLL was present, problems such as access violations and other Windows errors could occur.

Resolution: Developers added code to CPRS to check for the correct version of BORLNDMM.DLL. If the correct version is present, CPRS runs as it should. If the correct version is not present, CPRS displays an error message informing the user and CPRS does not run.

<span id="_Toc221409120" class="anchor"></span>Lexicon Lookup

- Identical Searches Return Different Number of Results (Remedy# 153968) – If the user did consecutive searches for the identical term in the Lexicon lookup dialog (Problems Tab, Consults/Procedures Ordering, Encounter Form, etc.), the search returned a different numbers of results.

Resolution: Developers changed CPRS so that a temporary Lexicon global node that was not being cleared after each search is now cleared.

<span id="_Toc221409121" class="anchor"></span>Non-VA Meds

- Non-VA Meds Quick Orders Not Storing the Default Route – When the user created an order and saved it as a Quick Order, the user had defined a route, but when the user then tried to use the quick order, the route was not defined.

Resolution: Developers corrected this so that the quick order will retain the route.

- Non-VA Meds Synonym Not Displayed beyond Initial Selection – In the Non-VA Meds dialog, providers can select a medication by its generic name or by a synonym (usually the brand name). When the provider selects the medication, the second ordering dialog displayed the generic medication name without the synonym. If the provider selected the wrong medication and was not familiar with the generic name, the provider might not recognize that it was the wrong medication.

Resolution: To address this issue, the Non-VA Meds dialog will display both the generic name and the synonym, instead of the only displaying the generic name. Only the generic name is saved in the order. Therefore, the Orders tab and detailed display were not changed. The second dialog, where the provider enters the rest of the order information, such as dosage, route, and schedule is the only dialog that developers changed.

<span id="_Toc221409122" class="anchor"></span>Notes

- Text Search “List Index Out of Bounds” Error – If a user did a text search in a notes view other than Signed Notes (All), CPRS gave a “list index out of bounds” error.

Resolution: Developers corrected this problem. There will no longer be an out of bounds error, when doing a text search in other views.

- Problem with Selecting Cosigner and Additional Cosigner (Remedy \#129322) – If a user first changed the cosigner, and then added that same individual as an additional signer, the document would be saved with that user as both a cosigner and additional signer. The selected user would then never be able to complete the signature as an additional signer.

Resolution: Developers changed CPRS so that the currently selected cosigner cannot be selected as an additional signer.

- User Able to Add Disallowed Author or Cosigner – When a user clicked on the disallowed user from the selection list for either the current author or cosigner, or for an already selected additional signer, CPRS correctly displayed an error message that the selection was not allowed. However, if the user then clicked the “Add” button immediately after the error message, CPRS would still add the disallowed selection to the list.

Resolution: Developers corrected this problem; CPRS will not add the inappropriate selection.

<span id="_Toc221409123" class="anchor"></span>Notifications

- Fixing Which Providers Should See “Orders Needing Clarification” Alert (Remedy \#69990) – Frequently, the alert for “Orders needing Clarification” was going to providers who were not interested in the alert or could take no action on the alert.

Resolution: When the user processes the “Orders needing Clarification” alert in CPRS, the list of orders will only include orders where the user is either stored in the Orders file (File 100) as the person identified to see the flagged order or where the user is identified as needing to see the order because of provider recipient rules for the Flagged Order for Clarification Notification.

- Orders Needing Clarification Default Reasons

Resolution: Developers added to the post install routine the default reasons for flagging orders that were identified by the CPRS Clinical Workgroup. The list contains some default reasons, and users can add some free-text to the existing text.

- Improved Surrogate Validation and Show Comments Button for Notifications – Previously, the comments were only displayed in a hover hint.

Resolution: Developers changed the surrogate validation code (Tools/Options/Notifications) to use a new supported Kernel API. Developers also added a Show Comments button to patient selection screen that allows users to display comments added by forwarder when forwarding an alert.

<span id="_Toc221409124" class="anchor"></span>Orders

- Orders Custom View Settings Not Being Retained
- The Orders Custom View selection screen has always opened with all values set to the most generic defaults, instead of to the user’s current view settings. A small change to the settings then requires starting from scratch.
- The Status and Service treeviews only highlighted the selected item when the treeview had focus.
- There was also an obvious copy/paste error in the code that may have also caused incorrect behavior.

Resolution: Developers changed CPRS so that the Custom Order View dialog now opens with the current view settings shown.

- Diet Quick Orders Do Not Prompt for Late Tray (Remedy \#69260) - Diet orders, both inpatient and outpatient, prompt for a late tray if the cutoff time has passed for the meal being ordered. If needed, this prompt appears when the user selects the Accept button. For diet quick orders that are designated as “auto-accept”, this prompt has never appeared as it should (reported in 2000), resulting in missing late trays for patients.

Resolution: Developers corrected this so that the late tray prompt will display when it should.

- Sequence Problem with Delayed NPO at Midnight and Other Diet Orders (related to PSI-07-212) – For inpatient delayed diet orders, if an “NPO at Midnight” were ordered, followed by any other diet with a start date prior to midnight and no expiration date, the NPO order will be discontinued on release and replaced by the second order. If placed in the reverse sequence, both orders are released correctly and remain in effect.

Resolution: This is not easily corrected, if possible at all, but the user is now prompted about the possible conflict, and instructed on how to prevent it from happening by entering explicit start and stop date/times for any diet orders defined for that same release event. Developers also added code to check for auto-accept diet quick orders, immediate and delayed, that would auto-DC because of overlapping start/stop times. For event-delayed, auto-accept diet quick orders, CPRS checks for conflicting orders for the same release event, and if the user answers NO to the prompt about having adjusted the start/stop dates, CPRS displays the diet order dialog with that quick order pre-loaded so date adjustments can be made.

- Provide a Way to Sort the DC List Sequence (This item is also under “New Parameters”)

Resolution: The new parameter OR DC REASON LIST enables someone at a site to define the sequence in which the list of reasons for DC appears in CPRS. The user configuring this list can define the entire list, but does not need to set the entire sequence for every DC reason. For example, if the user wants to have one item listed first, the user can define that item as the first sequence, causing CPRS to load the specified reason first and then load the rest of the DC reasons in alphabetical order.

- Error Message When Attempting to Copy to New Order – In the Recently Expired medications view, some medications that had a status of DC/EDIT were displayed because CPRS had not yet been refreshed. This could cause problems with a provider attempting to copy orders.

Resolution: Developers made changes to the Orders tab to review the order status and the order action status when determining if the Order Status in CPRS is out-of-sync with the Order Status in VistA. This should correct the problem with CPRS refreshing automatically when trying to copy an order with a status of DC/EDIT. Most likely, the user will receive another message not allowing the copy to happen, with a reason “Orders that have been DC’d due to editing may not be copied.”

- Change the Recently Expired Orders View

Resolution: To prevent duplicate orders—one with a status Expired and one with a status of DC/EDIT from appearing in the Recently Expired Orders view—developers changed this view to look only at the order status and not the order action status.

- Order Text Cut Off or Missing (Remedy \#135126) – Signed On Chart, Discontinue, and Order Verify dialogs could truncate text, or even hide orders on the list, if the maximum number of pixels needed to display the order, in height, exceeded 255. While more of a problem when using larger fonts, this could also occur for orders with an excessive amount of comments.

Resolution: Developers changed a setting in CPRS that should help alleviate this problem.

- Complex Tab Displays Incorrect Default Schedule – The default schedule loaded from the Pharmacy Orderable Item file was not carrying over to Complex tab.

Resolution: Developers corrected this problem. The default schedule should carry over correctly.

- Changes to PRN Usage on Complex Order Tab – Previously, the complex orders tab did not display PRN when the schedule field did not have focus. Also, PRN did not display for orderable items when the schedule was a standard schedule with PRN added to it.

Resolution: Developers changed the Complex order tab to display PRN in the schedule field when the schedule field is not in focus if the PRN checkbox is checked, and fixed the problem with orderable items not checking the PRN checkbox when the schedule is a standard schedule with PRN added to it.

- IMO Order Schedule Expanding Inappropriately – When copying an IMO order to a new IMO order, the schedule was expanding.

Resolution: Developers changed this because IMO orders should not expand the schedule.

- “Give Additional Dose Now” Checkbox Disappearing – When selecting a schedule in a Complex Inpatient Order dialog, the “Give Additional Dose Now” checkbox disappearing.

Resolution: Developers corrected this problem.

- Limitations Field Shown as Optional

Resolution: Developers added a message to the Limitations field, stating that the field is optional. (The Limitations field is seen when setting up a Quick Order in VistA.)

- New Parameter for Help Text for Administration Times

Resolution: CPRS has added the ability to display information describing how to change the administration times. The new parameter OR ADMIN TIME HELP TEXT enables sites to enter text that displays as a Hover Hint on the order dialog’s Dosage tab and as an Information Box on the Complex tab. To access this box on the Complex tab, the user must either click or press \<Enter\> in the administration schedule cells.

- Sig Not Updating after Dosage Edit – Previously, when deleting the first character in the dosage field and closing out of the Order dialog, the sig field did not update to the new dosage. For Example the user enter a dosage of 55 MG by accident they then deleted the first 5 out of the dosage field. The sig field will still show as 55 MG.

Resolution: Developers corrected this problem. The sig field should now update correctly.

- REASON FOR FLAG to Display When Processing Flagged Order Alert – When a user is processing a flagged order alert, the REASON FOR FLAG did not display in the order text on the Orders tab.

Resolution: When a user processes the Flagged Order alert, the REASON FOR FLAG will now display on the Orders tab. It will not display there when not processing notifications. In both cases, the reason will still be included in the order details as it currently is. This functionality now matches CPRS List Manager.

- REASON FOR FLAG Field Changed from Free-Text to Drop-Down List with Free-text Allowed

Resolution: When a user flags an order, the REASON FOR FLAG field has been changed from a free-text entry to a selection of standard reasons defined by the site in parameter (OR FLAGGED ORD REASONS). Users can append additional free-text to the selected reason, or enter a free-text reason of their own instead of selecting from the list. The field limit is 80 characters.

- Selected Orders Inappropriately Deselected when Right-Clicking (Remedy \#70286) – Previously, if a user selected several orders (so that they were highlighted) and then right-clicked on an unselected order, CPRS would deselect the other orders. If the user did not recognize that the selection had changed, the user might take an inappropriate action on an order.

Resolution: If a user selects (highlights) one or more orders and then right-clicks on a different order, CPRS keeps the orders selected and brings up the pop-up menu. This behavior is now consistent with other CPRS tabs.

- Duplicate Personal Quick Order Names – It was possible for a user to enter a new personal quick order name that is a duplicate of an existing quick order name in the same display group type.

Resolution: Developers corrected this problem. Users can no longer enter a duplicated quick order name for a quick order in the same display group type. CPRS will also prohibit renaming an existing personal quick order to a name that matches an existing entry.

- Dietetics Additional Order Quick Order Error – When using roll and scroll (List Manager) options to create or edit a Dietetics Additional Order quick order, an \<UNDEF\> error would occur.

Resolution: Developers corrected the Additional orders quick order problem.

- Remove Default Radiology Order Desired Date Default (E3R 19834) – Previously, when a user placed a radiology order, the prompt for Date Desired defaulted to TODAY.

Resolution: Developers removed this default as requested. This field remains required, but is now displayed with no default. Developers also created patch OR\*3.0\*281 to identify orders that may need to be changed as a result of new features in some patches. One feature of patch OR\*3.0\*281 is to identify radiology quick orders with a desired date of TODAY. The patch creates a list of the quick orders with a date of today that will be mailed to the user who runs the report. It can also be set to remove the default of TODAY from the quick orders, and can be set to disregard STAT orders.

-   
  New Clozapine Requirements

Resolution: There are some additional requirements for Clozapine ordering. When the user picks an orderable item that points to a Clozapine Pharmacy Orderable Item, the CPRS GUI checks to see if the patient is allowed to get the order based on:

- registration with the NCCC
- WBC and ANC lab tests (including the lab values and if the test was within the last 7 days)
- possibly an override permit from the NCCC.

If the order can be placed, the user sees nothing new.

If the order cannot be placed, then a dialog box pops up to show the user the reason.

CPRS now prevents Clozapine orders from being renewed for both Outpatient and Inpatient orders.

- Discontinuing an Unsigned/Unreleased Delayed Order Required DC Reason – If a user was discontinuing an unsigned/unreleased delayed order, CPRS was asking for a DC reason.

Resolution: Developers changed CPRS to no longer ask for a DC reason for these types of orders when a user discontinues them.

- IMO Order Assigned to Incorrect Location – Previously, when was signing IMO orders for a patient who was admitted while the CPRS session was open, the user was prompted to determine where the order should be given. This would cause the order to change the ordering location and the display group. If multiple orders were selected, but the user unchecks some of the IMO orders from the signature list, these orders were inappropriately updating the display group and the ordering location.

Resolution: Developers created a new dialog that CPRS displays when the patient location has changed between inpatient and outpatient, such as when a patient is admitted. The dialog lists the orders and enables the user to pick a location where each order should be administered, such as a clinic location or a ward location.

- Order Marked as Obsolete Still Showing on Active Orders List – In CPRS v.26 (OR\*30\*215), developers required a signature for discontinued orders that created an order action. In doing so, these orders did not drop off the active orders list as they previously done; the orders remained on the list until the length of time defined in the Context Hrs.

Resolution: At the recommendation of the CPRS Clinical Workgroup, developers changed CPRS so that discontinued orders now respect the value of the field “INCLUDE IN ACTIVE ORDERS” located in the NATURE OF ORDER file for the order’s NATURE OF DC. Orders marked appropriately will now behave as they did before CPRS v.26.

-   
  Truncated or Hidden Labels on Radiology Ordering Dialog – Previously, the “Imaging Type” and “Imaging Procedure” labels were sometimes being truncated or partially hidden on the Radiology ordering dialog, especially on resizing form.

Resolution: Developers corrected this problem and the labels should appear correctly.

- Schedule Field Behaves Differently when Setting-Up a Quick Order for IV and Unit Dose (Remedy \#162977)

Resolution: The schedule field now behaves the same for IV and Unit Dose Orders.

- Quick Order Prompt “Include Patient Instructions in SIG?” Not Functioning Properly (Remedy \#69829) – In VistA, when defining a Quick Order, one prompt is the question “Include Patient Instructions in SIG?”. The default response is “yes”. However, if the user changed the response to “no”, closed the dialog, and then began to edit the quick order, the value of this prompt was automatically changed back to “yes”. If the user presses \<Enter\> through the question without changing it, a value of “yes” will be stored.

Resolution: Developers changed the code to now retain the value as it has been entered by the user.

- Leading Zero in CPRS Orders and Quick Orders (Remedy \#85193) – Previously, when a user entered or edited an order or quick order in CPRS, the VOLUME field stripped off the leading zero. Also, when a user created or edited quick orders in the VistA roll-and-scroll, CPRS would accept a leading zero in the STRENGTH or VOLUME fields before the decimal (0.523), but when the order was placed the leading zero was stripped (.523). In fact, when creating an order or entering or editing a Quick Order in CPRS, the Strength field does no formatting of the entered strength.  For example, if the user enters 00.25 then the value is stored as 00.25.  If they enter .25 then the value is stored as .25. JCAHO compliance states that the volume should have the leading zero.

Resolution: Developers have changed CPRS to not accept orders that begin with a decimal point. Also, if the order is entered with a single leading zero (0.5), the zero will be retained.

- Dose Not Maintained when Placing an Order from Quick Order Menu in VistA (Remedy \#137019) – In VistA, when a user was viewing quick orders through Enter/Edit Quick Orders \[ORCM QUICK ORDERS\], the text-based dose was deleted if the user chose to place the order instead of cancel.

Resolution: The dose is maintained when the user has not changed the text dose.

- Problem When Provider Deletes Comments from Copied or Changed Order (Remedy \#160310, 160113) – When a provider copied or changed an order and deleted the comments from the original order, the order was sent to Inpatient Medications with a null entry in ^OR(100—causing Inpatient Medications issues because it tries to send comments to BCMA, but the comments are not there.

Resolution: CPRS no longer sends a null entry.

- Display of Unsigned Verbal Orders Confusing – Previously, verbal orders that were unsigned displayed on the active orders list, but when a pharmacist changed the order, the changed order replaced the original order. This could cause confusion because the second order showed as needing to be signed, but it was not what was originally entered as a verbal order.

Resolution: Developers changed CPRS so that the original unsigned verbal order remains visible to the ordering provider when the order is edited in backdoor pharmacy while in an active status. The action by the pharmacist creates a new order that should display on the Active orders display in CPRS. However, the original order should remain on the Unsigned orders display in CPRS.

- New Parameters Created for Old Unsigned Orders – Instances have occurred where providers have signed old orders accidentally.

Resolution: To help address the signing of old unsigned orders, developers added two new parameters to the OR namespace: OR LAPSE ORDERS and OR LAPSE ORDERS DFLT. OR LAPSE ORDERS is a numeric parameter that stores the number of days to keep unsigned orders before setting them to the Lapsed status. This parameter is set up such that the instance term is a display group so that different display groups can lapse at different times. OR LAPSE ORDERS DFLT is also a numeric parameter. This parameter stores the number of days before lapsing unsigned orders that are part of a display group that does not have a value set for parameter OR LAPSE ORDERS.

There is now a nightly process that looks at overdue delayed events and lapses orders associated with these events.  Previously, this lapsing only took place during a user session for that event.

- CPRS/Pharmacy HL7 Message Escaping – Prior to these changes, when certain characters were entered in order word processing fields, errors and/or corrupted data could result.

Resolution: CPRS now escapes the HL7 delimiter characters that may be placed in the word processing fields of an order. The escaping is done before the order is handed to Pharmacy so that Pharmacy can parse it and use the data. Pharmacy must in turn un-escape these characters so that they display correctly to the users. Pharmacy also escapes the same characters before sending HL7 messages to CPRS and CPRS un-escapes these before use.

- Lack of Control in Display of Obsolete Orders – Previously, the INCLUDE IN ACTIVE ORDERS attribute in the NATURE OF ORDER file applied to discontinued orders that did not create an order action (i.e., required a signature). Developers assumed that users would always want to see any discontinued order that had to be signed. At that time, housekeeping types of discontinues (DC’s) such as Obsolete did not create an action or get signed, so it was up to the sites to decide if they wanted those DC’s to display or not (according to the Context Hrs parameter, as noted) using this Nature attribute. With the change that all front-door DC’s create an action, there was no way for sites to make DC’s such as obsolete fall off the Orders display right away unless they have their Context Hrs set to 0.

Resolution: Discontinued orders now respect the value for INCLUDE IN ACTIVE ORDERS set in the NATURE OF ORDER file for the nature that was chosen when DCing the order in CPRS, which determines whether the orders will display or not.

- Accidental Signing of Old Orders: Lapsed Report – Previously, there was no way to get a report of orders that had gone into a lapsed status.

Resolution: This new report provides a way for users to view a list of orders that have been lapsed by the process that determines if orders have been in an unsigned state for too long. The option for this new report is OR LAPSED ORDERS which is an item under the menu option OR PARAM COORDINATOR MENU.

- Days Supply Not Calculating Correctly

Resolution: Developers changed CPRS to take into account the conjunctions used on the Complex tab of the Outpatient Meds ordering form when calculating the Days Supply.

- CPRS Needs to Check for Keys for Clozapine Ordering

Resolution: Developers changed CPRS to pass the user DUZ to the M system to run a check to see if the provider holds the YSCL Authorized Key.

- Cannot Focus on a Disabled or Invisible Window Message Received when Exiting Medication Order Menus after Order Checks – Previously, if a provider created a complex medication order against an allergy, the Order Check is received, and the provider canceled the order. Then, instead of exiting the order menu via the Quit button, the provider attempted to exit the dialog using the X in top right corner. This action generated an error message.

Resolution: Developers added code to correct the problem and the user can now exit by clicking the “X” from in the upper right corner of the dialog.

- Access Violation on Time Out When Day-of-Week Schedule Builder Is Open – Previously, when the Day-Of-Week schedule builder window was open and CPRS timed out, CPRS did not shut down following the countdown to “0” seconds. Instead, an access violation occurred.

Resolution: CPRS closes correctly as expected when the timeout is executed while the Day-of-Week form is open.

- Cannot Add the New Allergy Entry/Edit Dialog to the Writer Orders List (Remedy \#189377)

Resolution: User can now add the new allergy entry/edit dialog because developers changed the parameter ORWOR WRITE ORDERS LIST to accept entries of type ACTION in file 101.41.

- Error When Placing Diet Order for Hospital Location with Null Ward Location (Remedy \#187024) – When ordering an inpatient diet, if the current HOSPITAL LOCATION file entry has a null value for WARD LOCATION, an error would result at EN1^FHWOR8.

Resolution: This is a site data issue. Developers changed CPRS so that the error no longer occurs.

- Personal Quick Orders with Duplicate Names Can Be Saved If the Case Is Different

Resolution: Developers corrected this problem.

- Problem with Order Status Synchronization in VistA and CPRS – When the user tried to copy an order with a status of DC/EDIT, CPRS would automatically refresh.

Resolution: Developers changed the Orders tab to review the order status and the order action status when determining if the Order Status in CPRS is out-of-sync with the Order Status in VistA. Generally, CPRS will not allow the copy to happen, and will display a message to the user stating “Orders that have been DC’d due to editing may not be copied.” CPRS should not refresh if the order status in the GUI is DC/EDIT.

- Delayed A/D/T Orders Show Global Value in Location Field – When placing an A/D/T delayed order for an outpatient and a location is not selected before writing a delayed order, CPRS currently displays "0;sc(" in the location column for the order.

Resolution: Developers changed CPRS to display "Unknown" instead of "0;sc(" in the location column.

- Duplicate Order Forms Opening in CPRS – If a user double-clicked on an item in the Write Orders list, two of the same order dialog would open.

Resolution: Speedy double-clicking should no longer open multiple order forms.

- IMO Clinic Determination

Resolution: To help determine if a location is an authorized IMO location, CPRS calls to a scheduling database when the user begins writing orders. However, if for some reason, the database cannot be reached, the new RSA returns a -3 value (which tells CPRS it could not be reached). CPRS then checks the Hospital Location entry to see if that entry is marked as an IMO location. If the location is marked as an IMO location, then CPRS allows the user to place IMO orders.

- Detailed Order Display Change

Resolution: Developers changed the Order Detail display to read “Released:” and the date instead of “Released by: on” and the Date if the Signed on Chart field is not checked.

- Changed the Sequence Button on the Complex Order Dialog to a Drop-Down List

Resolution: Developers changed the Then/And button to a drop-down list. This should improve how the information is entered.

- Refill Field Allows Inappropriate Numbers, Letters and Characters – Previously, users could enter inappropriate numbers, letters, and character into the Refill field and then CPRS sent them to pharmacy

Resolution: The order dialog now performs a check when accepting an order. If the refill value is anything other then a number, then CPRS displays an error message, and the user will not be able to complete the order.

- Refills to Days Supply Are Not Checked when an Order Is Changed (Remedy 185499) – This Remedy ticket had two problems. When placing an outpatient order with refills, if the user changed the order before signing the order, the refill value would display as zero in the order dialog, and the user was not able to change the refill value until something else was changed in the order.

Resolution: Developers corrected these issues. When the user is placing an order, CPRS performs a more detailed check to stop order from being placed with a refill value greater then the max possible refills.

- Admin Times Display as NOT DEFINED on Personal QO Created from a VistA QO – When the user created the QO from one containing a Day-of-Week schedule built from the hours and minutes list instead of the schedule combo box, the administration times did not come through on the personal quick order.

Resolution: Developers corrected this and the administration times come through as they should.

- Personal Quick Order Not Saved When Created from an Existing VistA QO – When a user created a personal quick order (QO) from an existing Inpatient mediation quick order created in VistA, the personal quick order did not display in the Unit Dose list.

Resolution: Developers corrected this problem.

- IV Medication Order Dialog Clicking Off Solution or Additive List Automatically Adds Med To Order

Resolution: Developers addressed this problem and clicking someplace else or tabbing out of the solution or additives lists no longer automatically adds the Medication to the order.

- Text Box Not Read-Only when It Should Be – Previously, on the Inpatient and Outpatient Meds order dialogs, after the user selected a medication, and the complete dialog is displayed, the user could clear part of the medication name from the text box at the top of the screen, using the backspace or delete keys, or by selecting part of the text and typing other characters. The result would be a change that should not be allowed.

Resolution: Developers changed the text box to be read-only. Only the navigation keys are recognized in the edit box. To change the medication name, the user must select the Change button.

- Newly Created Personal Quick Order Are NOT Accessible - A problem was found with saving Inpatient quick order (QO) to a personal QO. This was caused by a difference with the display groups the QO were being saved to. Developers found that quick orders with the display group Inpatient Medications were not being displayed in the list of quick orders on the Inpatient Medications dialog where users were accustomed to seeing them.

Resolution: To correct this problem, developers removed the default dialog from the Inpatient Medication Display Group. This display group will now only be used as a grouper for Custom Order Views for Inpatient Medications. Sites will no longer be able to use the Inpatient Medication as a Type of Quick Order when creating a QO in VistA. Sites will need to use the Unit Dose Medication value for the Type of Quick Order when setting up a QO in VistA. A post install routine will change any existing quick orders that are defined with a Type of Quick Order of Inpatient Medications to a Type of Quick Order of Unit Dose. Doing this will keep the interface the same for CPRS users.

<span id="_Toc221409125" class="anchor"></span>Order Checks

- Order Checks and Reason for Override Not Sent to Ancillary Packages

Resolution: Developers added an API to communicate order checks and reason for override to ancillary packages.

- Order Check Consistency

Resolution: Developers changed the Inpatient Order dialog to do the same look-up for the Common Drug information as the outpatient dialog. This should allow for the same order check information to appear as an outpatient order, when accepting an inpatient order.

- Order Checking Screen Cannot be Resized

Resolution: Developers corrected this: the order checking screen (dialog) can now be resized.

<span id="_Toc221409126" class="anchor"></span>Parameter Description Changes

- Parameter Description Text Expanded

Resolution: Developers updated descriptions for ORCH CONTEXT MEDS and ORWOR EXPIRED ORDERS in the PARAMETER DEFINITION file, 8989.51, to clarify that ORCH CONTEXT MEDS affects the Meds tab display, but ORWOR EXPIRED ORDERS affects the Orders tab. These parameters function exclusive of each other; changing one does not affect the other.

<span id="_Toc221409127" class="anchor"></span>Patient Demographics

- Incorrect data on Patient Inquiry Report (from CPRS) (PSI-05-063, Remedy \#102307)– To get patient demographics, a user can click once on the Patient Inquiry button. Previously, if a user double-clicked on the Patient Inquiry button and was changing patients, it was possible to get incorrect information. This happened infrequently.

Resolution: Developers changed CPRS so that double-clicking on the Patient Info button (located on the patient bar) will no longer open multiple dialogs. As a result, users will not see incorrect patient data in this box, due to double-clicking, and switching patients.

- Display of Added Demographic Information

Resolution: When the user selects the Patient Inquiry button, developers enhanced CPRS to display the secondary Next of Kin information, the Emergency contact, and the patient’s cell phone number. This data comes from a registration (DG) Application Programming Interface (API).

<span id="_Toc221409128" class="anchor"></span>Patient Insurance Dialog

- Patient Insurance Dialog Formatting Problem – Previously, the patient name next to the dialog title might not be viewable.

Resolution: Developers made a change in CPRS on the dialog title to eliminate leading spaces between the title and the patients name to ensure that the patient’s name is viewable.

<span id="_Toc221409129" class="anchor"></span>Patient Record Flags

- Difficulty Changing PRF Note Title, Date, Author, Etc. – With unsigned PRF progress notes, users could not change the note characteristics: title, author, date.

Resolution: Developers fixed this problem and users can now change the date, author, etc. of an unsigned PRF progress note.

> **NOTE:** If the user attempts to change the characteristics of a PRF note and has highlighted an action that reads Yes under note, CPRS assumes that the user is trying to link to an already linked action and will not allow the change to continue. However, if the user removes the highlight from the Yes action, the changes can occur.

<span id="_Toc221409130" class="anchor"></span>Patient Selection

- Provider Selecting Wrong Patient with Same First/Last Name (PSI-04-057, NOIS BHH-1104-40049, Remedy \#71065) – On the patient selection screen, if a user typed in some letters of a patient’s name, CPRS would try to match the selection, go to that part of the patient list, and highlight the first entry that matched the text entered—even if there was more than one possible match. If the user pressed \<Enter\> without ensuring that the correct patient was selected, the user might be looking at the wrong record.

Resolution: To address this problem, developers changed the patient selection list to implement the same auto-unique selection behavior that the mediation order dialog dosage, route, and schedule implements. Specifically, an item in the list will not be selected unless the text typed uniquely identifies the item. If there are multiple items that could match what the user entered, CPRS requires the user to explicitly select the patient.

- Button Display Issue on the Patient Selection Dialog

Resolution: Developers changed the code so that the Save Patient List Settings button should no longer get cut off.

<span id="_Toc221409131" class="anchor"></span>Problem List

- New Problem Dialog: Manual Resizing Breaks Up Part of Display

Resolution: Manual resizing does not break up the display.

<span id="_Toc221409132" class="anchor"></span>Reminder Dialogs

- All Items in a Group Can Now Be Required (Remedy \#128569)

Resolution: Along with patch PXRM\*2.0\*4 and the changes in CPRS GUI v.27, users can now force all the items in a Reminder Dialog Group to be required.

- Additional Text in Progress Notes for Inexact Date Entered in Reminder Dialog (Remedy \#141382)

Resolution: When the user enters a vague historical date in a Reminder Dialog, the progress note text will append “exact date unknown” next to the date.

<span id="_Toc221409133" class="anchor"></span>Remote Data Views (RDV)

- RDV Not Displaying Units Consistently – Previously, the RDV reports did not display units in the comment section for site-to-site items, but HDR items did have units.

Resolution: RDV displays units consistently for both data from the HDR and the site-to-site data.

<span id="_Toc221409134" class="anchor"></span>Reports

- Missing Image Icons and Incorrect Messages on Radiology Reports – Previously on the Reports tab, radiology reports listed under “Clinical Reports/Radiology/Imaging” were not displaying an image icon if images were attached, as they did for the identical reports under “Imaging (local only)”. Additionally, if a report did have linked images, CPRS displayed the incorrect message “Imaging links are not active at this site” at the top of the report text when the user clicked on that report in the list. Behind the scenes, Windows messaging used by VistA Imaging was also not behaving correctly for these reports.

Resolution: Developers corrected all of these issues.

- Two Reports Missing Schedule Data – Two reports in CPRS, All IV and Active IV were missing schedule data.

Resolution: Developers added a new Schedule column to the reports and changed the column order. The order is now: Additives, Solutions, Rate, Schedule, Start Date/Time, Stop Date/Time, \[+\]Flag.

<span id="_Toc221409135" class="anchor"></span>Sensitive Patient Checks

- Sensitive Record <span id="sensitive_patient_check_no_access" class="anchor"></span>Check Bypassed when Using CPRS GUI to Process Alerts (Remedy \#215189, NSOC Ticket \#VA08853) – Previously, if a user was processing alerts, CPRS did not perform a sensitive record check before going to the patient chart. This has never worked correctly. The user was taken to the chart without receiving the sensitive patient warning.

Access to a record would be denied, for example, if a user tries to access his or her own patient record while processing alerts. An example message is shown below.

![](or-3-243-release-notes-cprs-gui-27/002.png)

There are two known issues remaining, both occur only when an alert cannot be processed at all because viewing that patient is denied:

1.  If that alert is the first in the list to be processed, then following the “access denied” message, the patient selection screen will open, and any subsequent alerts that the user had previously selected will need to be selected again.
2.  In any other sequence, alerts up to and including the “access denied” message will process correctly. At that point, the user cannot continue processing alerts using the NEXT button or menu, and must go back to the patient selection screen to continue, or reselect additional alerts.

<span id="_Toc221409136" class="anchor"></span>Signature

- Review/Sign Changes Dialog Incorrectly Identifying Some Orders as “Non-VA” Orders – CPRS was treating generic text orders containing the text of “Non-VA Meds” as Non-VA Meds orders on the Review/Sign Changes form. As a result, the checkbox on the Review/Sign Changes was grayed out for this order, and the user could not uncheck the order so that it would not be signed.

Resolution: For signature, CPRS now checks the display group of the order instead of the order text.

- Redundant Display of “Review/Sign Orders Dialog – Previously, if a patient had unsigned items, and the user selected "File/Select" to open a different patient’s chart, and then processes an alert from the patient selection screen, CPRS displayed the Review/Sign Changes dialog. The second instance, after selecting the alert, was redundant.

Resolution: Developers prevented the dialog from displaying the second time.

- Other Users’ Orders Appearing under the Current User’s Signature List – When a user was exiting a patient record that contained unreleased orders written by other users and the current user did not write any orders, CPRS was inappropriately placing the other users’ orders in the current user’s signature list.

Resolution: Developers corrected this problem. The order will now appear in the correct section of the signature list.

- Users Not Prompted to Sign Allergy Entered in Error Note when Exiting

Resolution: All allergies entered in error and allergies that create progress notes will require a signature and be listed on the signature form along with orders.

- Associating Orders with a Clinic or Ward when Patient Location Changes during Ordering Session – Previously, if a user began writing orders for an outpatient and during the ordering session, the patient was admitted, CPRS enabled the user to decide where the group of orders should be sent—the ward or the clinic. However, this choice seemed to limit the users to only moving all orders to a single location even though the user might want some orders given in one location and others in the other location.

Resolution: To add more flexibility, developers changed the dialog to enable the user to send all orders to either the ward or the clinic or to individually associate some orders with the ward and others with the clinic.

<span id="_Toc221409137" class="anchor"></span>Templates

- Refresh Button Allows All Patient Data Objects to Appear – When users create or edit a template, selecting Edit \| Insert Patient Data (Object) brings up a list of patient data objects (TIU Objects) that the user can put into the template. This list can be restricted by the TIU TEMPLATE PERSONAL OBJECTS parameter by specifying which patient data objects will appear in this list. The Refresh button on this form bypasses this parameter restriction and adds all patient data objects to the list.

Resolution: Developers corrected this problem; the parameter value will be respected.

- Template Searches Seem to Make CPRS Freeze – Previously, when users searched for a template with the Find Template feature, either in the template editor or in the templates drawer, the search could take an inordinate amount of time and make it appear that CPRS was frozen.

Resolution: CPRS developers added a dialog that displays when a search takes longer than a second or two. The dialog has a search animation (a moving flashlight) to show the user that CPRS is still searching. From this form, the user can also cancel the search using the Cancel button if the search is taking too long. Also, searches for templates higher up in the template tree should be considerably faster.

<span id="_Toc221409138" class="anchor"></span>User Interface

- Double-Clicking on Controls Creating Problems – Previously, if a user double-clicked on controls of some mental health tests, CPRS was experiencing problems, such as access violations. The problem appeared to be a latency problem, where the clicks were viewed as two separate clicks rather than a double-click. The problem appeared to be related to system response, and possibly the use of regional data processing centers.

Resolution: Developers made changes to CPRS to disable the Mental Health Test buttons, Clear, Cancel, and Finish buttons in reminder dialogs to disable after the first click and it will not become enable until the code is finished processing.

<span id="_Toc221409139" class="anchor"></span>508 and Sizing Issues

- Consults Reason for Request Box Not Expanding Vertically

Resolution: The Reason for Request field on the Consult dialog now expands vertically when the dialog increases in size.

- “Transfer Medication Orders" Pop-Up Window Does Not Display OK and Cancel Buttons with Fonts \>10 Pt

Resolution: The OK and Cancel buttons will now display with 10 point and larger font sizes.

- Notes Tab - JAWS Not Reading Text Correctly in the Custom View Dialog

Resolution: Developers changed the text on the Note Tree View and Sort Note List above the Sort Order radio buttons so that they display the same information as the group box above them. Now JAWS will read the same information.

- Assign Diagnoses Dialog – Difficult Keyboard Navigation

Resolution: The Assign Diagnoses to Orders(s) dialog has been changed to improve accessibility.

- The focus will no longer land on the labels above each of the controls, and the labels will still be read by screen readers.
- The initial focus on the form is now obviously in the top list control.
- Notes Change Button Causes Problems with Larger Fonts (Remedy \#135118) – When using larger fonts, and editing a note, the Change button used to change the note title, author, etc., moves to the left, covering up the note title or other relevant data, or the Change button could completely disappear.

Resolution: Developers corrected this problem so that the Change button remains on the right side of the screen regardless of the font size.

- Dialog Display Problems in Windows XP Style (Remedy \#71192) – When the workstation desktop is in Windows XP Style or when using Large or Extra Large fonts on the desktop, Windows expands the title bar of all windows. This expansion may cause scroll bars to appear on some dialogs, hiding or even making some components inaccessible. These scroll bars would not appear when Windows Classic Style and Normal Font Size are used.

Resolution: Developers added checks in CPRS to detect an enlarged title bar and lengthen the height of the dialog accordingly, to prevent these scroll bars from appearing on these dialogs.

- Large Font Sizes Create Problems in Dialogs (Remedy \# 70821) – When using larger fonts on some dialogs, the components on those dialogs would grow larger than the dialog itself, making them unusable. Some dialogs affects included the signature box when completing orders, and the lookup of other immunizations, skin tests, patient education topics, and exams on the encounter form. It is likely that there are other dialogs that were corrected as a result of this fix as well.

Resolution: Developers corrected this problem.

- CPRS Display Problems with Alternate Color Schemes (Remedy \# 119059) – When Windows is set to display in alternate color schemes, particularly when windows and buttons are black, many locations throughout CPRS do not accommodate the color change, making it difficult to use.

Resolution: CPRS will now automatically adjust text colors and black button images when windows are black, when using alternate color schemes.

> **NOTE:** Graphing colors are not adjusted. Also, CPRS will not adjust well to color scheme changes made while CPRS is running.

- Provider Selection Using Keyboard Difficult on the Encounter Form’s Procedure Tab (Remedy \# 70301) – Using the keyboard to select a provider on the Procedures tab of the Encounter Form was extremely difficult. After only a half second of typing, typed text was used to select the provider, with additional typed text restarting the provider selection.

Resolution: Developers changed this so that when the user types some text, CPRS searches for a possible match. If it finds a partial match (names that contain part of what was typed), the text remains in the field and the user can continue to type or use the down arrow to find the correct name. If there is no partial match, the field returns to blank or the previous name.

- Focus Should Remain on Tab When Navigating using the Keyboard – When navigating the tabs on the Encounter form, the focus would go to the first control on each tab. This made it difficult for sight-impaired users to know which tab they were on.

Resolution: The focus now stays on the tab rather than jumping to the first control on the tab’s page.

- Problem Selecting Items from List Boxes – When users attempted to check the selected diagnosis code using the keyboard, the cursor does not check the item, but goes somewhere else. A list box that allowed a user to type some text to go to the portion of the list where needed items were located (such as typing “m” to go to the first m item in the list, “macular degeneration” for example) did not keep the focus on the “macular degeneration” item if the user pressed the Up arrow, Down arrow, or Space bar on the item.

Resolution: Now the focus will activate (check for check list boxes) the correct item when pressing the Space bar or move to the correct item when pressing the Up or Down arrow keys.

- Screen reader Does Not Read Contents of Service Connection and Rated Disabilities Box

Resolution: The focus now starts at the beginning of the Service Connection and Rated Disabilities box, enabling the user of the screen reader to easily arrow down or instruct their screen reader to read the text.

- Encounter Form--Service Connection and Rated Disabilities Box Should Be Made Uneditable

Resolution: The Service Connection & Rated Disabilities box is no longer editable.

- Text Only Order Dialog OK/Cancel Buttons Hidden at 18 pt Font

Resolution: The OK & Cancel buttons should no longer be hidden at 18 pt font.

- Hover Hints on the Other Examinations Window Now Left Justified at Fonts Sizes 18 and 24 – The Other Examinations dialog (accessed from the encounter forms “exams” tab.) contains a list box. The list box hover hints are now left justified at font sizes 18 and 24.

Resolution: The upgrade to Delphi 2006 caused this improvement.

- Fix Sorting of Alerts on Patient Selection Screen with Keyboard (Remedy \#70891) – Previously CPRS supported only ascending sorting of alerts on the Patient Selection screen when using the keyboard.

Resolution: Developers corrected the problem and users can now toggle between ascending and descending sorts on alerts, using the keyboard, on the Patient Selection screen.

- 508: Difficulty in Accessing Unique Problem List Entries from Encounter Form – If a list contained an item beginning with a space, when the user pressed the Space bar, CPRS would move to the first item that began with a space and immediately select the item also (when using the keyboard, user press the Space bar to select items in a list). This meant that it was impossible for keyboard users to select any other item than the one beginning with the space.

Resolution: Now pressing the Space bar will not jump to items that begin with a space. The Space bar is reserved for selecting items so that the user will now be able to select other items in the list when using a keyboard.

- 508: Inconsistency in Checking Diagnosis Code – Previously, on the Encounter form’s Diagnoses tab, it was sometimes necessary for the user to arrow down off a specific code and then and back up to the code before the code could be checked.

Resolution: Developers corrected this problem. CPRS now functions correctly. Using the Up Arrow and Down Arrow keys and pressing the Space key keeps the user on the correct item in the list.

- 508: Notes Tab—Add Encounter to Action Menu

Developers added the Encounter menu item to the Action Menu on the Notes tab and included a short cut: Shift+Ctrl+R.

-   
  508: Encounter Form—Need short-cut to Get to the CANCEL Button

Resolution: “ALT+C” activates the CANCEL button.

- 508: Encounter Form—Need short-cut to Get to the OK Button

Resolution: “ALT+O” on the encounter form activates the OK button.

- 508: Put Add and Remove Buttons on the Consults Send Alert Dialog

Resolution: Developers put Add and Remove on the Consult Actions Send Alert dialog.

- 508: When Shift-Tabbing Out of the Encounter Information, a “Cannot Focus Error” Occurs

Resolution: Developers corrected the “Cannot focus” error that occurred when a user shift-tabbed out of the Encounter read-only text field on the Notes tab.

- 508: Encounter Form Navigation—Tab Should List Selected Section Entries – Previously, the tab order for moving the focus in the dialog was confusing to those using screen readers.

Resolution: Developers changed the tab order on the following Encounter form tabs: Diagnoses, Procedures, Immunizations, Skin Tests, Patient Ed, Health Factors, and Exams. Each of these tabs contains an Other button; the Other button has been put in the tab order after the section name list (after the Modifiers list on the Procedures tab).

- 508: When Reviewing/Checking Questions in the Classification Questions, Screen Readers Do Not Read Cursor Location

Resolution: Each check box will now read the group box title: “Visit Related To” and then the value it is related to like “Agent Orange Exposure” and then if the check box is a yes check box it will read: “- Yes”, and for no it will read: “- No”.

- 508: Consults Tab – Change Cursor Location for Action Menu - Alt-A-C-T – JAWS

Resolution: When activating the menu option: Actions \| Consult Tracking \| Display Details (Alt-A-C-T), CPRS now places the focus into the text field containing the details, the screen reader reads that it is in a text field, and the user can review the details.

- 508: Location for Current Activities Tab – JAWS – The Location for Current Activities dialog has 3 tabs within it. When a user Alt-tabbed or arrow-keyed through the tabs, sometimes focus is thrown onto a control within the tab area, making it difficult to navigate.

Resolution: Now when the user navigates using the keyboard (with the Tab or arrow keys), the focus will remain on tab name, so that the screen reader will read the tab name, making navigation easier.

- 508: Blind Users Can Only Select One Order at a Time – Previously, visually impaired users and those who use the keyboard exclusively could not select more than one order unless the orders were next to each other in a list.

Resolution: Multiple orders that are not in a row (not contiguous) can now be selected using the keyboard only. The functionality mimics Outlook’s email list. To move the focus without selecting an order, the user should press and hold the Ctrl key and then use the arrow keys. To select an order when the focus is on it, press the Space bar. To select another order, continue to hold the Ctrl key and press the arrow key to move focus to the next order you want to select, then still holding the Ctrl key, press Space bar—the new and the previous order will be selected.

- 508 : Notes Tab - Action Menu (Alt-A-G) Sign Order Dialog Text Now Accessible

Resolution: The notes sign orders dialog (Alt-A-G) has been modified so that the text displayed above the signature code box can be accessed via the keyboard. JAWS will be able to read the text when the user tabs into the text.

- 508: Consults - Press \<Enter\> Key to Begin a New Consult

The New Consult button is now the default button on the Consults tab. When the user first gets to the Consults tab and presses \<Enter\> the button will be “clicked” (the Order a Consult dialog displays).

- 508: Tabbing Access to Patient Inquiry from Notes Tab Is Problematic and Inconsistent

Resolution: Developers changed the tab order on the Notes tab. The Patient Inquiry can now be accessed consistently on the Notes tab by tabbing and shift-tabbing.

- 508: Treatment Factor Definition Pop-Ups Not Read by Screen Readers

Resolution: When a screen reader is running, the treatment factor labels now appear as read only edit fields. The read only fields contain the text displayed by the pop-up. The user can use their “read in” keys to read the text; this makes the data available for screen reader users.

- 508: Create Standardized Shortcuts for Use Throughout CPRS

Resolution: Developers changed CPRS so that now as a general rule “Ctrl + Enter” will activate (click) the default button on a dialog. Default buttons are typically labeled “Ok”, “Done”, or “Accept” Not all dialogs and windows have default buttons assigned. If no default exists for the dialog or window, “Ctrl + Enter” will not activate any button on those forms.

- 508: Orders Tab ‑ Would Like to Press the \<Enter\> key to “Accept Order” – Pressing the \<Enter\> key on most order dialogs moves the focus from one control to the next. So \<Enter\> had conflicting functionality.

Resolution: Developers changed CPRS so that if the user presses "Ctrl + Enter" on an order dialog it will activate the Accept button.

- 508: Encounter Form Inaccessible: CPRS Does Not Track Focus and Focus Changes – Specifically, users reported that on the Encounter form’s Visit Type tab, there were two places where the focus would get “lost”. The first instance occurred when the user tabbed or shift-tabbed between SC & Rated Disabilities box and the Visit Related To groupbox. The other instance of “lost” focus occurred only when the user shift-tabbed from the Available providers combo box.

Resolution: The focus will no longer be “lost” to adaptive technologies on the Encounter form.

- 508: Problems Tab - Default OK so that Pressing \<Enter\> Key Selects Term

Resolution: Now pressing the \<Enter\> key on the New Problem dialog will activate the OK button.

- 508: Notifications - Create Keystrokes for “Go to the Next Notification”, Continue, Forward and Renew - When processing multiple notifications in CPRS, there is a small hand pointing to the right in the lower right hand section of CPRS. Clicking on the hand means “go to the next notification” automatically. There was no keystroke for this option. Neither are there keystrokes for the pop-up menu items Continue, Forward, and Renew.

Resolution: Developers changed CPRS so that the user can now tab to the “Next Hand” or “go to the next notification” button, or the user can access it by pressing ALT+ N. All of the pop-up menu options are now available using short-cut keys: Continue = CTRL+C, Forward = CTRL+F, and Renew = CTLR+R.

- Splash Screen--Fix the Email Address on the Splash Screen

Resolution: Changed to email address from med.va.gov to va.gov.

- 508: Can't Tab Through Multi-Tab Screens

Resolution: The user can now move to the next tab using the left and right arrow keys.

- 508: At Fonts 12, 14, 18 Display of Problem List Items under Diagnosis Section Are Unreadable

Resolution: All font sizes are now readable.

-   
  508 Consults--Splitter Bar Doesn't Retain Size

Resolution: Developers removed code that was resizing left panel to the same size— overriding the user set size.

- Patient Selection Screen: Sizing Issues – Previously, when the user resized the Patient Selection Screen some buttons did not resize properly.

Resolution: Developers changed the dialog so that the Save Patient Listing Settings button width and height correctly adjust based on form text length and height.

- 508: Scroll Bar Disappears on Notes/Consults and DC Summary Tabs with Larger Fonts (Remedy \#70539)

Resolution: The scroll bars remain visible when using larger fonts.

- 508: Create a Custom Component to Read a Label that the User Can Tab To

A component has been created that will allow Delphi developers to place a label that can gain focus when a screen reader is running. This will allow free standing single line labels to be read.

- 508: Some Labs Grids Not Reading Correctly – Previously, the labs grid that CPRS displays after the user selects “Most Recent Results” or “Worksheet” does not read the data correctly.

Resolution: Developers worked on the labs grid for the “Most Recent Results” and “Worksheet” displays so that it reads the whole row, including headers, as the user arrows around in the grid.

- 508: Clinical Reminders and Reminder Categories on Cover Sheet Dialog

Resolution: The dialog “Clinical Reminders and Reminder Categories Displayed on Cover Sheet” now is accessible through a screen reader, with the exception of reading the graphics. The graphics are going to be handled globally with another correction.

- 508: JAWS Does Not Speak the State of Template and Reminder Drawers – Previously, the Templates and Reminders drawer buttons would speak their names, but they did not speak whether they were opened or closed.

Resolution: On the Notes, D/C Summ, or Consults tabs, or any other tab where they are found, when the Templates and Reminders buttons are pressed or receive focus, the screen reader will now indicate the state of the drawer. For example, when a closed templates drawer button receives focus, the screen reader will say “Templates Drawer, drawer closed”. When the button is pressed, the screen reader will say “drawer open”.

-   
  508: Users Not Told that Text Was Inserted into Documents

Resolution: When a user is working with any kind of document (note, consult, etc.) and a boilerplate, template, or reminder dialog inserts text into that document, the screen reader will say “text inserted”.

- 508: Dialogs Not Identified

Resolution: When a dialog appears, the screen reader will say the word “Dialog” following the title of the dialog.

- 508: JAWS Does Not Read Day of Week (DOW) Schedule

Resolution: If JAWS is running, the user should be able to read the DOW schedule at the end of the DOW schedule form.

- 508: JAWS Not Reading Order Dialog Fields

Resolution: If JAWS is running, the user should be able to read the Administration Times and the Expected First Dose time on the Unit Dose Order dialog and the Infusion Order dialog.

- 508: Add Keyboard Combination for OK Button

Resolution: Developers set the OK button as the default for when the user presses the keyboard combination \<Ctrl\> + \<Enter\>. When the user presses \<Ctrl\> + \<Enter\>, the OK button is activated.

- 508: Notifications Headings Not Displayed Correctly at Higher Font Sizes

Resolution: Developers adjusted the Notification heading sizes to accommodate 14pt font.

- 508: Template Field Combo Boxes Do Not Retain Their Values (Remedy \#70463) – Previously in Reminder dialogs, if the user entered values with keystrokes without the list dropping down, the values were not retained.

Resolution: Values chosen using key strokes are being selected and saved.

- 508: Notifications Selecting Provider to Forward Does Not Work with Keyboard – Previously, if the user was forwarding a notification to another provider, the user could not type the name in the search box and press \<Enter\> to have the name moved to the recipient list. Pressing \<Enter\> closed the dialog, and if a name was not selected, no action was taken.

Resolution: Developers changed CPRS so that the keystrokes now work as they should. The user can type a name, press \<Enter\>, and the name will go to the recipient list.

- 508: Encounter Area under Note Text Pane Does Not Have a Label

Resolution: Developers added the following label for JAWS: “Encounter Information” to the Encounter text area under the Note text pane. (This change can only be listened for.)

- 508: Focus Always Returns to Upper Left Item in Page – Previously on several CPRS tabs, when a used navigated CPRS with the keyboard and performed certain actions, the focus would return to the upper left item on the tab. The upper left item was not always the most useful place and at times required a lot of tabbing and navigation to return to the cursor or focus to the appropriate item.

Resolution: After opening a dialog and closing it - as a general rule - the focus will return to where it was.

- 508: Orders Tab - Order Selection Does Not Keep Its Focus

Resolution: The focus will stay on the order list after performing an action on an order.

- 508: Cancel Button on Patient Selection Screen Lower Border Is Not Displaying

Resolution: The bottom of the Cancel button is no longer cut off.

- 508: Charleston Issue \#2: OK and Cancel Button Disappear on Discontinue / Cancel Orders Form (PSI-05-006)

Resolution: The buttons will no longer be inaccessible by shrinking the size of the dialog.

- 508: Encounter Form Inaccessible: CPRS Does Not Track Focus and Focus Changes – Previously, CPRS providers who used adaptive technologies, such as screen readers had trouble navigating some areas of CPRS. On the Encounter form, for example, the focus would be “lost” when tabbing through the controls—meaning that the focus was on items, but the screen reader did not speak anything. This “lost” focus made the controls almost impossible to use effectively.

Resolution: The focus will no longer be "lost" to adaptive technologies on the encounter form—specifically on the Visit Type tab on the Encounter form.

- 508: Header Bar – Screen Reader Not Reading RDV Listbox Checkbox State

Resolution: JAWS will now read the RDV listbox checkbox state. If the checkbox is checked JAWS will tell the user it is a check box and then announce that it is checked.

-   
  508: Screen Reader Should State whether Checkboxes Are Checked/Unchecked under Historical Visit (Current Activities)

Resolution: The Historical Visit check box on the New Visit Tab in the Provider and Location for Current Activities dialog will now read the state of the check box.

- 508: Available Reminders Dialog – Treeview/listbox Combo Data Not Accessible with a Screen Reader

Resolution: The data in the list to the right of the treeview will now be read with each treeview item.

- 508: JAWS Did Not Read the Day-of-Week (DOW) Schedule at the end of the DOW Schedule Form

Resolution: Developers corrected this problem.

- 508: JAWS Not Reading Items on the Infusion Order Dialog Correctly

Resolution: Developers corrected this problem. JAWS now reads the Administration Times and the Expected First Dose time on the Unit Dose Order dialog and the IV Order Dialog.

- Template Preview Buttons Disappear with Large Fonts (Remedy \#110715)

Resolution: Developers corrected the font problem, and the Template Preview and Consult Order Pre-Requisites forms display their buttons appropriately regardless of the font size the user has selected.

- Font Size and Upper Case and Lower Case Affecting Printing (Remedy \#70295)

Resolution: Developers fixed the problems affecting printed items. They should print correctly regardless of font size and/or use of upper/lower case characters. Printouts with changes:

- Reports from Reports tab
- Progress Note Print
- Consult Pre-Requisite Print
- Consult SF513 Print
- Lab Results Print
- Patient Inquiry (Demographics) Print (Changed to maintain consistency)
- Template Preview Print (Changed to maintain consistency)
- 508: Read Only Edit Fields – Previously, when a screen reader got to certain fields, it would read each line by starting with "Read Only Edit" then the text with each arrow down.

Resolution: Developers changed CPRS and replaced the read only edits with a label component. When a screen reader is running, the label caption changes to match the text in the hint

- 508: CPRS Does Not Enable Screen Readers to Differentiate between Auto-Accept Quick Orders and Non-Auto-Accept Quick Orders

Resolution: Auto-accept quick orders will now speak “Auto Accept” before the order menu text is spoken.

- 508: Progress Notes: Screen Reader says “Procedure date/time” instead of “Date/Time of Note”

Resolution: Developers changed CPRS, and the note field date/time should read “Date/Time of Note:”.

- 508: Medication Order Dialog—Medication Field and Quick Order Field Need Labels

Resolution: Developers placed JAWS labels on the Medication field (“Medication”) and the Quick order field (“Quick Orders”).

- 508: Notifications—Forward aNotification—New Buttons Are Not in the Correct Tab Order

Resolution: Developers improved the tab order of the buttons—placing the Add button after the source list, the Remove and Remove all....

- 508: Clinical Reminders—Edit Reminders on Coversheet—Extra Tabs in the Tab Order

Resolution: Developers removed the extra tabs for the images and hidden drop down list.

- 508: Print Dialog on Reports Tab, with Larger Font Sizes, Loses Buttons and Is Unusable – The select device print dialog that appears when you print a report from the reports tab is not resizing properly for font changes.

Developers corrected this problem. .

- 508 Splitter Bar Can Be Lost with Resizing and Font Size Change – 508 testers reported a problem on the Reports tab. If a user selected a report that caused the right side of the screen to display two screens (Top/bottom), such as the Clinical Reports/Patient Information/Demographics report, and the user moved the splitter bar to the bottom of the screen, and then changed to a larger font (8 to 18), then the bottom data screen could be moved off the bottom of the screen—and in some cases cannot be retrieved.

Resolution: Developers corrected this problem.