---
title: BCMA Version 3 GUI User Manual - Appendix A (FAQs)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: GUI  - Appendix A (FAQs)
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
menu_options: 7
description: - [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs) - [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-1) - [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-2) - [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-3) - [Fre
audience: 
keywords: 
  - bcma
  - order
  - questions
  - medication
  - table
  - frequently
  - asked
  - faqs
  - orders
  - patient
page_count: 0
word_count: 7242
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
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_UM_APPENDIX_A_FAQS.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_UM_APPENDIX_A_FAQS.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

Appendix A: Frequently Asked Questions

Appendix A: Frequently Asked Questions

Nursing-Related Questions and Answers (cont.)

[IRM-Related Questions and Answers A-1](#irm-related-questions-and-answers)8

# Frequently Asked Questions (FAQs)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-1)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-2)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-3)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-4)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-5)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-6)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-7)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-8)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-9)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-10)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-11)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-12)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-13)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-14)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-15)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-16)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs-17)
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="benefits-of-this-chapter">Benefits of this Chapter</h2></td>
<td><p>This chapter seeks to answer the questions asked most frequently by BCMA users. The questions and answers in this chapter are organized by Pharmacy, Nursing, and then IRM (Information Resource Management).</p>
<p>Within each section, we have provided the FAQ topic so you can quickly locate what you need immediately in the Table of Contents. The topics are not listed in any particular order.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers">Pharmacy-Related Questions and Answers </h2></td>
<td><h3 id="recognizing-synonyms">Recognizing Synonyms</h3>
<p>When I used the <em>DRUG File Inquiry</em> option, I was unable to view an IV Piggyback medication by synonym. Doesn’t this option recognize synonyms from the DRUG file (#50)?</p>
<p>Yes, the <em>Drug File Inquiry</em> [PSB DRUG INQUIRY] option does recognize synonyms from the DRUG file (#50), including any of the following entry formats: drug IEN code, generic name, Federal Supply Number (FSN), VA product name, National Drug Code (NDC), and ATC mnemonic. However, it does not recognize synonyms from the IV ADDITIVES file (#52.6).</p>
<h3 id="reading-bar-codes-into-synonym-field">Reading Bar Codes into SYNONYM Field</h3>
<p>How are bar codes scanned into the SYNONYM field (#.01) of the DRUG file (#50)? Is this information transferred just as a number?</p>
<p>Use the <em>Drug Enter/Edit</em> [PSS DRUG ENTER/EDIT] option under the <em>Pharmacy Data Management</em> menu to scan the synonyms into DRUG file (#50), plus trade names and quick codes for drug item look-up.</p>
<p>In BCMA, the SYNONYM field (#.01) is used when you scan a manufacturer’s National Drug Code (NDC) or Universal Product Code (UPC) on the bar code label to create a quick code look-up for a drug product. You should not enter bar codes into this field manually. You can also use the <em>Synonym Enter/Edit</em> [PSS SYNONYM EDIT] option under the <em>Pharmacy Data Management</em> menu to scan a manufacturer’s bar code into the SYNONYM field (#.01) of the DRUG file (#50).</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers-cont.">Pharmacy-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="tools-available-for-drug-file-50-clean-up">Tools Available for DRUG file (#50) Clean up</h3>
<p>Are tools available for the Pharmacy to use when cleaning up DRUG file (#50)?</p>
<p>Yes, the Pharmacy can use VA FileMan, in conjunction with Microsoft<sup></sup> Excel, to clean up DRUG file (#50). DRUG file maintenance is extremely important for all Pharmacy packages. This process is especially important in CPRS, and should be ongoing. BCMA does not provide options to identify duplicate drug entries or similarities. This is solely a function of the <em>Pharmacy Data Management</em> menu.</p>
<h3 id="displaying-message-field-on-vdl">Displaying MESSAGE Field on VDL</h3>
<p>Is there a way to make the MESSAGE field from the IV package (as it currently prints on the IV labels) display on the VDL?</p>
<p>Information entered into the OTHER PRINT INFORMATION field, during IV Order Entry, automatically displays in <strong>RED</strong> on the Medication Order Display Area of the BCMA VDL, and prints on the CHUI BCMA Due List Report.</p>
<h3 id="entering-information-into-the-quantity-prompt">Entering Information into the “Quantity:” Prompt</h3>
<p>What should I put into the “Quantity:” prompt for an order with Lorazepam 1-2 mg Q6H PRN? Should I put 1 mg, 2 mg, or 1 tab?</p>
<p>You can enter dosage ranges in the “DOSAGE ORDERED:” prompt of Inpatient Medications V. 5.0. In this example, you could enter the dosage ordered as 1-2 mg. The “UNITS PER DOSE:” prompt should contain a “2” for this example order (i.e., the maximum allowable units per dose). This allows you to administer either 1 mg or 2 mg of the medication to the patient. All BCMA reports will then include an accurate reflection of the actual dosages administered to patients.</p>
<h3 id="entering-dosage-amount-given-to-patient">Entering Dosage Amount Given to Patient</h3>
<p>When will the nurse be prompted to enter the Dosage amount given to the patient?</p>
<p>Anytime a medication is administered under the Unit Dose Medication Tab, but not entered as a TAB or CAP in the “DOSAGE ORDERED:” prompt of Inpatient Medications V. 5.0, a nurse will be prompted to enter the amount given to the patient.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers-cont.-1">Pharmacy-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="handling-liquid-doses">Handling Liquid Doses</h3>
<p>How do I handle liquid doses?</p>
<p>You can draw up oral syringes for all liquid dosages, and then label them with the bar code, but this may be too labor intensive for some Pharmacies. Most liquid dosages have the manufacturer’s bar-coded NDC number on them, so they can be scanned as synonyms into the DRUG file (#50) to eliminate the need for additional labeling.</p>
<p>If liquids are kept as bulk stock on wards, and you actually pour the amount of medication to be administered, the Pharmacy could enter the liquid dosage (i.e., 4 mg = 2 ml) into the “DOSAGE ORDERED:” prompt, in Inpatient Medications V. 5.0, during Order Entry. Then you would know how much liquid to administer to a patient. When you scan the bar code on a liquid dosage, a dialog box displays in BCMA, requiring you to enter the amount given. You should review the order on the BCMA VDL, and then enter the corresponding amount administered into the DOSAGE field of the dialog box.</p>
<h3 id="handling-fill-on-request-orders">Handling Fill-on-Request Orders</h3>
<p>How does the BCMA software handle the Fill-on-Request order types used for narcotics and for multi-dose packages such as inhalers?</p>
<p>Fill-on-Request orders are compatible with BCMA V. 3.0. These order types are grouped, based on whether their Schedule Type is Continuous or PRN. BCMA looks at the order and tries to find the characters “PRN” in the schedule. If it does not find these characters, it then looks for administration times, and places the order accordingly on the BCMA VDL.</p>
<h3 id="handling-self-administer-medications">Handling Self-Administer Medications</h3>
<p>How do I order and dispense medications that patients self-administer?</p>
<p>This is a local policy decision. One way to handle self-administered medications is to order and dispense medications using the Outpatient Pharmacy package, and to enter the medications into the Inpatient Medications V. 5.0 package. When patients self-administer their medications, they must put their initials next to their dosage amounts on a seven-day MAR. Medications are not scanned unless a nurse administers them.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers-cont.-2">Pharmacy-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="managing-sliding-scale-insulin">Managing Sliding Scale Insulin</h3>
<p>How is Sliding Scale insulin managed?</p>
<p>When an order for insulin is entered into Inpatient Medications V. 5.0, the “DOSAGE ORDERED:” prompt should include the words "sliding scale." BCMA then provides a dialog box for you to enter the amount of medication given to the patient. The “SPECIAL INSTRUCTIONS:” prompt should also include the sliding scale range written by the provider. For example, the instructions could specify the number of units drawn and the vial to use for administering the insulin.</p>
<h3 id="configuring-the-window-of-administration">Configuring the Window of Administration</h3>
<p>Is the window of administration configurable by drug?</p>
<p>If the drug orderable item (not the medication) has a specific schedule in the default schedule, the medication order will display on the BCMA VDL. If this is currently being done in the Inpatient Medications V. 5.0 package, and the order displays properly on the 7- or 14-Day MAR from this package, the order should display properly on the BCMA VDL.</p>
<h3 id="how-last-action-displays-on-vdl">How “Last Action” Displays on VDL </h3>
<p>How will the “Last Action” display on the VDL if the dispensed drug has changed since the last administration?</p>
<p>The information in the Last Action column of the VDL is based on the orderable item (not the medication). If the orderable item is the same, it will list the last administration action.</p>
<p>If the patient has two different orders for the same orderable item, the last administration of either of these orders will display in the Last Action column for both orders. You can view the Medication History Report to determine which order the medication was given from on the BCMA VDL.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers-cont.-3">Pharmacy-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="last-action-field-on-medication-order-entry-screen">“LAST ACTION” Field on Medication Order Entry Screen</h3>
<p>What is the “BCMA ORDER LAST ACTION:” prompt on the Medication Order Entry screen that I receive when I edit an order, or renew an order that has already been administered?</p>
<p>This data comes from BCMA and displays the Date/Time and Last Action taken on this order. For example: BCMA ORDER LAST ACTION: 07/12/02 09:31 Held. The data in this field is order specific, not orderable item specific; therefore, it differs from the Last Action column on the BCMA VDL.</p>
<h3 id="when-an-order-displays-on-the-vdl">When an Order Displays on the VDL</h3>
<p>When will a medication order display on the VDL?</p>
<p>A pharmacist or nurse must verify an order (and the order must be active) before it will display on the BCMA VDL. BCMA determines when to display an order on the BCMA VDL by subtracting the information in the “Before Scheduled Admin Time” site parameter field from the Start Date/Time of the medication order. You can define this parameter using the Parameters Tab in the GUI BCMA Site Parameters application.</p>
<h3 id="orders-that-display-on-the-vdl">Orders that Display on the VDL</h3>
<p>What types of medication orders display on the VDL?</p>
<p>All orders entered using CPRS or Inpatient Medications V. 5.0 display on the BCMA VDL once the orders have been finished and verified (and are active) including orders on “Hold,” and any orders entered through the Unit Dose or IV package — as long as the patient is an inpatient. Orders “On Hold” display grayed out on the BCMA VDL. You can mark these order types as “Held,” although it is not necessary for you to do so.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="pharmacy-related-questions-and-answers-cont.-4">Pharmacy-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="orders-that-display-under-each-medication-tab">Orders that Display Under Each Medication Tab</h3>
<p>What type of orders display under each Medication Tab on the VDL?</p>
<p>BCMA provides three Medication Tabs for separating and viewing active Unit Dose, IV Push, IV Piggyback, and large-volume IV medication orders. Medications that need to be administered will correspond to one of these tabs. This will depend on how the order was entered.</p>
<p>Each Medication Tab is described below.</p>
<ul>
<li><p><strong>Unit Dose Medication Tab:</strong> Displays all active Unit Dose orders for the Start and Stop Date/Time and Schedule Types selected on the BCMA VDL, except for orders entered with a Medication Route of IVP or IV PUSH. (These order types display under the IVP/IVPB Medication Tab.)</p></li>
<li><p><strong>IVP/IVPB Medication Tab:</strong> Displays all active Unit Dose orders with a Medication Route of IVP or IV PUSH. The following IV order types display on the BCMA VDL when you click this Tab:</p></li>
</ul>
<ul>
<li><p>“Piggyback”</p></li>
<li><p>“Syringe,” with the “INTERMITTENT SYRINGE?” prompt set to “YES”</p></li>
<li><p>“Chemotherapy,” with the “CHEMOTHERAPY TYPE:” prompt set to “Piggyback” or “Syringe” and the “INTERMITTENT SYRINGE?” prompt set to “YES”</p></li>
</ul>
<ul>
<li><p><strong>IV Medication Tab:</strong> Displays all active IV orders, as defined by the order Start and Stop Date/Time. The following IV order types display on the BCMA VDL when you click this Tab:</p></li>
</ul>
<ul>
<li><p>“Hyperal”</p></li>
<li><p>“Admixture”</p></li>
<li><p>“Syringe,” with the “INTERMITTENT SYRINGE?” prompt set to “NO”</p></li>
<li><p>“Chemotherapy,” with the “CHEMOTHERAPY TYPE:” prompt set to “Admixture” or “Syringe” and the “INTERMITTENT SYRINGE?” prompt set to “NO”</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers">Nursing-Related Questions and Answers</h2></td>
<td><h3 id="how-last-action-column-functions">How “Last Action” Column Functions</h3>
<p>How does the “Last Action” column function on the VDL?</p>
<p>The Last Action column, on the BCMA VDL, is based on the orderable item (not the medication), so you will know when the patient last received any dose of a medication regardless of the Schedule Type selected. This information is to prevent the same medication from being given to the patient from another order or schedule type.</p>
<p>If the patient has two different orders for the same orderable item, the last administration of either of these orders will display in the Last Action column for both orders. You can view the Medication Log Report to determine which order the medication was given from on the BCMA VDL.</p>
<h3 id="how-new-patch-functionality-works">How New Patch Functionality Works</h3>
<p>How does the new Patch functionality work in BCMA V. 3.0?</p>
<p>Any orderable item with “PATCH” in the DOSE FORM field, and a status of “Given,” must be marked as “Removed” in the BCMA VDL before you can administer another patch to a patient on the same order. You can use the Due List menu or the Right Click drop-down menu to document this action. The BCMA VDL then displays the letters “RM” (for “Removed”) in the Status column of the BCMA VDL. A patch will continue to display on the BCMA VDL each time BCMA is opened, until the patch is marked “Removed” — even if the order is discontinued or expires, or the patient is discharged and re-admitted.</p>
<h3 id="iv-orders-that-display-on-the-vdl">IV Orders that Display on the VDL</h3>
<p>How long does an IV order display on the VDL?</p>
<p>An IV order will display on the BCMA VDL until the Stop Date/Time of the order. If an order becomes expired or is discontinued while an IV bag is infusing, both the order and the bag will display on the BCMA VDL until the bag is marked “Completed” for up to 72 hours after expiration or discontinued date. The order will have a status of Expired or Discontinued.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="viewing-the-patients-order">Viewing the Patient’s Order</h3>
<p>How can I see the patient’s complete order when I am working in their VDL?</p>
<p>Double-click on a patient’s medication order on the BCMA VDL to display the Display Order dialog box. It provides a detailed display of the order from Inpatient Medications V. 5.0. You can also select an order, and then press <strong><span class="smallcaps">f4</span></strong>, <em>or</em> select an order then select the Display Order command from the Due List menu to display order information.</p>
<h3 id="understanding-the-log-in-message">Understanding the Log-in Message</h3>
<p>When I tried logging into BCMA, I received the message “The BCMA application is not active for this site!” Why am I getting this message?</p>
<p>Most likely, you received this Information message because you tried to log on while BCMA was temporarily offline. When BCMA is offline, users that are <em>currently</em> logged into GUI BCMA will not be affected.</p>
<p>You can select the “BCMA Online” check box using the GUI BCMA Site Parameters application (typically used by IRM Staff) to take BCMA offline for a particular division. This setting is located under the Facility Tab of this application.</p>
<h3 id="selecting-a-medication-before-scanning">Selecting a Medication Before Scanning </h3>
<p>Do I have to select a drug (by selecting it on the VDL) before I can scan the bar code for that medication?</p>
<p>No, you do not have to select the drug on the BCMA VDL. After you scan the medication bar code, BCMA verifies whether an order exists for the medication displayed on the patient’s VDL. If BCMA does not find a match, it displays an Error message informing you that the scanned drug was not found.</p>
<h3 id="orders-with-a-non-standard-administration-time">Orders with a Non-Standard Administration Time</h3>
<p>How does an order appear on the VDL if the provider selects a non-standard administration time?</p>
<p>An order will display correctly on the BCMA VDL if the Order Entry method is compatible with, and appears correctly on the electronic MAR provided within the Inpatient Medications V. 5.0 package.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-1">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="entering-an-ointment-quantity">Entering an Ointment Quantity</h3>
<p>How should an ointment quantity be entered into BCMA?</p>
<p>For example, enter “small amount,” “quantity sufficient,” or the area where the ointment is applied on the patient. This is a free-text field limited to 150 characters.</p>
<h3 id="scanning-two-tablet-doses">Scanning Two-Tablet Doses</h3>
<p>Why do I have to scan twice for a two-tablet dose?</p>
<p>So you specify the actual dosage given to the patient at the time that the medication is scanned. BCMA also verifies and documents the correct dosage administered to the patient.</p>
<h3 id="documenting-a-half-tablet-dosage">Documenting a Half-Tablet Dosage</h3>
<p>How do I document the administration of a half-tablet dosage?</p>
<p>The Fractional Dose functionality is designed to alert you when dispensed drug dosages need to be administered to a patient in “fractional” doses, and to allow you to provide comments about this order type once administered. In short, the related dialog boxes let you document the units and the fractional portion of a dose administered to a patient.</p>
<p><strong>Note:</strong> The Fractional Dose dialog box displays when the units per dose is fractional and <em>less than</em> 1.0. The Multiple/Fractional Dose dialog box displays when the units per dose is <em>greater than</em> 1.0. If you do not scan once for each unit listed in the Multiple/Fractional Dose dialog box, the Confirmation dialog box displays, requesting that you confirm the actual total units administered to the patient.</p>
<p>See the section “Documenting a Fractional Dose Order” in chapter 3 for more information.</p>
<h3 id="recording-the-contents-of-code-carts-or-emergency-meds">Recording the Contents of Code Carts or Emergency Meds</h3>
<p>How do I record the contents of code carts or other emergency meds?</p>
<p>The CPRS Med Order Button (or “Hot Button”) links you to CPRS for electronically ordering, documenting, reviewing, and signing verbal- and phone-type STAT and (One-Time) medication orders that you have administered to patients. This feature can help streamline the workflow in busy settings such as ICU-type environments. See chapter 6, “Using the CPRS Med Order Button” for more information.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-2">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="sorting-capabilities-on-the-vdl">Sorting Capabilities on the VDL</h3>
<p>What sorting capabilities are available to me on the VDL?</p>
<p>Yes, the route is passed to the BCMA VDL from the “MED ROUTE:” prompt of the Inpatient Medications V. 5.0 package. You can use the Sort By command in the Due List menu or simply click on the “Route” Column Header to sort a patient’s VDL by route. You can sort this column by ascending or descending order.</p>
<h3 id="notifying-nurses-about-orders-on-hold">Notifying Nurses About Orders on “Hold”</h3>
<p>What notification will I receive when a provider places a medication order on “Hold”?</p>
<p>Medications placed on or taken off “Hold,” in CPRS or Inpatient Medications V. 5.0, display on the Missed Medications Report with the Hold information below the medication. The Hold information applies only to administrations due within the Hold timeframe. The “Order Num” column on the report lists the actual order number and order type (i.e., Unit Dose or IV). This information is quite helpful when troubleshooting problems with BCMA.</p>
<h3 id="printing-mah-and-prn-reports">Printing MAH and PRN Reports</h3>
<p>Are the MAH and PRN Reports available for printing when a patient is discharged?</p>
<p>Yes, using CHUI BCMA, you can print these reports by patient or by ward for specific date/time ranges.</p>
<h3 id="printing-ward-specific-reports">Printing Ward-Specific Reports</h3>
<p>Is it possible to run reports for the nursing ward without logging into a specific patient?</p>
<p>Yes, simply click <strong><span class="smallcaps">cancel</span></strong> at the Patient Lookup dialog box to access the Menu Bar — without opening a patient record. This applies to all ward-specific reports, except for the Cumulative Vitals/Measurement Report. A patient’s file must be opened to access patient-specific reports such as this one.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-3">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="entering-prn-effectiveness-comments">Entering PRN Effectiveness Comments</h3>
<p>How can I tell which PRN medications need an effectiveness documented?</p>
<p>The BCMA Clinical Reminders marquee, located in the lower, right-hand corner of the BCMA VDL, identifies PRN medications needing documentation.</p>
<h3 id="entering-effectiveness-comments-for-medications-other-than-prns">Entering Effectiveness Comments for Medications<br />
Other Than PRNs</h3>
<p>How can I enter an Effectiveness Comment for medications other than PRNs?</p>
<p>You can enter Effectiveness comments for active orders on the BCMA VDL. Simply select an order, and then select the Add Comment command from the Due List menu or the Right Click drop-down menu. This command is only available if the order status is “Given,” “Held,” “Refused,” “Missing,” and “Removed.” At the dialog box that displays, enter an Effectiveness comment for the patient’s medication, and then click <strong><span class="smallcaps">ok</span></strong> to save your comments and close the dialog box.</p>
<h3 id="prn-medications-allow-multiple-administrations">PRN Medications Allow Multiple Administrations</h3>
<p>I was able to document a PRN medication although it was not within the time frame of the order. Why does BCMA allow this to happen?</p>
<p>BCMA allows the nurse to administer PRNs on an “as needed” basis. There are no checks and balances to alert the nurse that the patient is not due the medication since PRNs have no administration times associated with the order. Information related to the last administration displays within the Last Action column. The PRN Reason list box displays up to the last four administrations created against that orderable item for the nurse to review.</p>
<h3 id="on-call-orders-displayed-on-vdl">On-Call Orders Displayed on VDL</h3>
<p>I administered all of the On-Call medications for my ward, but they still display on the VDL. When do they drop off the VDL?</p>
<p>After On-Calls are marked as Given, they will remain on the BCMA VDL until the expiration Date/Time of the order is reached. You can select the “Allow Multiple Admins for On-Call” checkbox using the Parameters Tab in the GUI BCMA Site Parameters application. This site parameter allows On-Call orders to be scanned multiple times. If you set the site parameter to “multiple,” an On-Call order will continue to display on the BCMA VDL until the order expires.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-4"><br />
Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="access-by-nursing-assistants">Access By Nursing Assistants</h3>
<p>Do Nursing Assistants have access to BCMA?</p>
<p>This is a local policy decision. Some facilities assign the BCMA options and menus (or portions of them) to Nursing Assistants so they can document treatments within their scope of practice.</p>
<h3 id="access-by-nursing-respiratory-students">Access By Nursing (Respiratory) Students</h3>
<p>Do Nursing (Respiratory) Students have access to BCMA?</p>
<p>Nursing (Respiratory) students can be given access to BCMA and identified as students. Along with the <em>Medication Administration Menu Nursing</em> [PSB NURSE] option in CHUI BCMA, the students are assigned the PSB STUDENT security key. The instructor assigned to the student will need to be assigned the PSB INSTRUCTOR security key as well. When the student initially logs into BCMA, a dialog box will prompt the instructor to enter the assigned VistA sign on credentials. The BCMA VDL will display both the student and instructor names as the medication administrators, and both names will also display on the BCMA reports. Staff acting as a preceptor to the student can be assigned the PSB INSTRUCTOR security key to log on with the student.</p>
<h3 id="documenting-non-administration-nursing-activities">Documenting Non-Administration Nursing Activities</h3>
<p>What method of documentation is available in BCMA for Nursing activities that are not associated with administering medications?</p>
<p>BCMA is designed <em>only</em> for electronically documenting medication administration activities performed on inpatients. Whatever system your site currently has in place (i.e., Accuchecks, free-text orders) for documenting non-medication treatments — such as intake/output, vital signs, and activity status — will remain in place.</p>
<h3 id="nursing-contraindications-and-drug-interactions">Nursing Contraindications and Drug Interactions</h3>
<p>Will BCMA provide nurses with any nursing contraindications and drug interactions that are needed before administering medications to patients?</p>
<p>No, this version of BCMA does not have this capability.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-5">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="borrowing-meds-from-another-patients-drawer">Borrowing Meds from Another Patient’s Drawer</h3>
<p>Can nurses still “borrow” meds from another patient's drawer?</p>
<p>BCMA software does not prevent this from happening for Unit Dose medications. However, you will not be able to borrow IV bags from another patient’s drawer since each IV bag is labeled with a Unique Identifier Number assigned specifically to a patient. This number displays on a patient’s VDL under the IVP/IVPB Medication Tab for IV Piggyback orders, and the IV Medication Tab for large-volume IV orders.</p>
<h3 id="defining-order-num-on-missed-meds-report">Defining “Order Num” on Missed Meds Report</h3>
<p>What does “Order Num” on the Missed Medications Report mean?</p>
<p>This is the actual order number of the medication from Inpatient Medications V. 5.0. It is quite useful to have when troubleshooting problems with BCMA.</p>
<h3 id="documenting-narcotic-waste">Documenting Narcotic Waste</h3>
<p>How can I document narcotic waste by the Anesthesia Provider?</p>
<p>There is no drug accountability available in BCMA V. 3.0. This is a local policy decision and your site should continue its current method for documenting this type of waste.</p>
<h3 id="documenting-blood-products">Documenting Blood Products</h3>
<p>How can I document the administration of blood products?</p>
<p>BCMA does not document the administration of blood products. It is designed for electronically documenting the administration of active medication orders only.</p>
<h3 id="documenting-inhalation-treatments">Documenting Inhalation Treatments</h3>
<p>How do Respiratory Therapists document inhalation treatments?</p>
<p>They document inhalation treatments by scanning the patient’s wristband and inhalation medication — just like they would any active medication displayed on the BCMA VDL.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nursing-related-questions-and-answers-cont.-6">Nursing-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="locating-bcma-information-in-cprs">Locating BCMA Information in CPRS</h3>
<p>Where can a Provider see BCMA information in CPRS?</p>
<p>In CPRS, the provider can access the BCMA MAH Report and the Medication Log Report using the Reports Tab. They can also access<br />
the Administration History Report (called Medication History Report<br />
in BCMA) in CPRS by right clicking on a medication under the Meds or Orders Tab.</p>
<h3 id="changes-to-order-entry-process">Changes to Order Entry Process</h3>
<p>How does BCMA V. 3.0 change the Order Entry process?</p>
<p>Implementing BCMA places extra pressure on the Order Entry process. There is a certain amount of flexibility, because humans can understand several different entries to mean the same thing. However, software is not as flexible. Providers, nurses, and pharmacists will need to agree on Order Entry procedures. With BCMA, Order Entry standardization is imperative. If the medication order is compatible with the electronic MAR available in Inpatient Medications V. 5.0, it will be compatible with the BCMA VDL.</p>
<h3 id="handling-inpatients-in-outpatient-areas">Handling Inpatients in Outpatient Areas</h3>
<p>How do you handle areas that treat inpatients, but are considered “outpatient”?</p>
<p>BCMA does not recognize orders that have an outpatient status and location. The patient must have a status and location of “inpatient.” You can use BCMA software if patients are seen in an outpatient clinic with an inpatient status and location, and any medications that need to be administered to them are entered using the Inpatient Medications V. 5.0 package.</p>
<h3 id="handling-patients-in-the-or-and-pacu">Handling Patients in the OR and PACU</h3>
<p>How does BCMA handle patients seen in the OR and the PACU?</p>
<p>If these areas are considered inpatient locations and their medication orders are entered through the Inpatient Medications V. 5.0 package or CPRS, you can use BCMA in these settings. Remember, the patient status and location must be “inpatient,” and the order must be active to display on the BCMA VDL.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="nurse-related-questions-and-answers-cont.">Nurse-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="handling-evening-coverage-when-pharmacy-closed">Handling Evening Coverage When Pharmacy Closed</h3>
<p>For sites that do not have evening Pharmacy coverage, will nurses need to be trained in, and given access to, the Inpatient Medications V. 5.0 package so they can manage needed changes in medication orders for BCMA?</p>
<p>This is a local policy decision. Some sites have Nursing Officers of the Day (NODs) who are permanently assigned to nights. They are on duty during the hours that the Pharmacy is not open. Besides the PSJ RNURSE security key, NODs are also assigned the PSJ RPHARM security key so they can enter and verify Unit Dose and IV medication orders.</p>
<p>You can set the user parameters for a NOD using the <em>Inpatient User Parameters Edit</em> [PSJ SEUP] option in Inpatient Medications V. 5.0:</p>
<ul>
<li><p>Allow Auto Verify: NO</p></li>
<li><p>Type of Order Entry: REGULAR</p></li>
</ul>
<p>These settings allow a NOD to finish — but not verify — an order in Inpatient Medications V. 5.0. The next morning, the nurse on the ward then verifies the order in Inpatient Medications V. 5.0, and the pharmacist verifies the order against a copy of the order. Once the order is verified, it then displays on the BCMA VDL. Your site may decide to train a NOD to enter orders into Inpatient Medications V. 5.0 that are written after hours, but need to be administered before the Pharmacy reopens the next day.</p>
<p>Another option is to assign nurses the PSJ RNFINISH and PSJ RNIVFINISH security keys so they can verify Unit Dose and IV medication orders. Once verified, these orders then display on the BCMA VDL for administration. The Pharmacy security key PSJ PHARM TECH designates the user as a Pharmacy Technician and gives them access to enter/finish, but not verify Unit Dose orders. The PSJI PHARM TECH security key allows Pharmacy Technicians to enter/finish, but not verify IV medication orders.</p>
<h3 id="handling-patient-transfers">Handling Patient Transfers</h3>
<p>How can I be sure that a medication is not given twice when a patient transfers a ward?</p>
<p>BCMA displays the Patient Transfer Notification message if the patient has transferred to another area within a specified time range, and the last action for the medication occurred before the transfer within the same time frame. This message displays only when you open the patient’s record and as you change tabs within BCMA.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="irm-related-questions-and-answers">IRM-Related Questions and Answers </h2></td>
<td><h3 id="contingency-plan-for-facilities">Contingency Plan for Facilities</h3>
<p>What is the Contingency Plan if the computer goes down?</p>
<p>In August 2003, patch PSB*2*17, the BCMA Backup System, was released to the field as a Class I solution for the BCMA Contingency Plan. This patch provides real-time backup of all inpatient medication activities on a designated workstation. Review the patch description to learn more about the benefits of this patch.</p>
<h3 id="bcma-wont-run-after-installation">BCMA Won’t Run After Installation</h3>
<p>I installed the BCMA software, but I can’t get the application to run. What else do I need to install?</p>
<p>Check the <em>BCMA V. 3.0 Installation Guide</em> for installation requirements. This guide includes a list of package version requirements and patches that are required for the installation of BCMA. It is available on the BCMA Project Notebook at:</p>
<ul>
<li><p><mark>REDACTED</mark></p></li>
</ul>
<h3 id="medication-not-displaying-on-the-vdl">Medication Not Displaying on the VDL</h3>
<p>How can I determine why a medication is not displaying on the VDL?</p>
<p>BCMA sends the Pharmacy a Due List Error Notification e-mail message to mail group members when it cannot resolve placement of a medication order on the VDL. An example might include no administration times entered for a Continuous order.</p>
<h3 id="setting-parameters-for-the-broker-server">Setting Parameters for the Broker Server</h3>
<p>I tried setting up the Optional Command Line Parameter for the Broker Server, but it was being ignored. Why?</p>
<p>Both parameters “S” (Broker Server) and “P” (Server Port) must be set, or they will be ignored. See the <em>BCMA V. 3.0 Installation Guide</em> for more information about these parameters settings.</p></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="irm-related-questions-and-answers-cont.">IRM-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="directing-error-log-to-another-directory">Directing Error Log to Another Directory</h3>
<p>How can I direct the BCMA Error Log for the GUI application to another directory?</p>
<p>Use the Optional Command Line Parameter “L” (DOS path location) to redirect the BCMA Error Log file to an alternate directory. The default directory is C:\Temp. There is also an Optional Command Line Parameter “/nologfile” that you can use to disable the Error Log.</p>
<h3 id="clock-used-for-displaying-administration-times">Clock Used for Displaying Administration Times</h3>
<p>What clock is the BCMA application using for administration times?</p>
<p>BCMA compares the Client clock (date/time) with the Server clock (date/time) at application start-up. If there is a difference greater than the “Max Client/Server Clock Variance” parameter value, a Warning message displays. All Client date/time calculations are based on the Client clock, plus a Client-Server increment. You can set this parameter value/setting using the Parameters Tab in the GUI BCMA Site Parameters application.</p>
<h3 id="requirements-for-laptops-and-scanners">Requirements for Laptops and Scanners</h3>
<p>What are the requirements for laptops and scanners? What additional equipment is needed on each ward?</p>
<p>The approximate requirements for laptops and scanners depend upon the number of Inpatient areas, at your site, that use BCMA for administering active medication orders. The BCMA Development Team recommends that your site have a minimum of three laptops and three scanners for each ward. Each site also needs printers for wristbands, bar code labels, and Missing Dose Requests notifications. For more information, see the <em>BCMA V. 3.0 Installation Guide</em> or locate information on the BCMA Project Notebook at:</p>
<ul>
<li><p><mark>REDACTED</mark></p></li>
</ul></td>
</tr>
</tbody>
</table>

# Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="irm-related-questions-and-answers-cont.-1">IRM-Related Questions and Answers (cont.)</h2></td>
<td><h3 id="locating-durable-wristbands">Locating Durable Wristbands</h3>
<p>Are durable wristbands available for printing on existing bar code printers?</p>
<p>The Phoenix beta site tested a wristband printed on a Zebra printer that seemed to be more durable than most. Check out the BCMA Web page listed below that provides a contact at Interface System, Inc. for more information.</p>
<p><mark>REDACTED</mark></p>
<h3 id="establishing-electronic-signature-codes">Establishing Electronic Signature Codes</h3>
<p>How do I set up the requirement for Electronic Signatures?</p>
<p>You can establish Electronic Signatures using the Kernel V. 8.0 <em>Electronic Signature code Edit</em> [XUSESIG] option. This option is tied to the Common Options under the <em>User’s Toolbox</em> [XUSERTOOLS] submenu to make access easy for all users.</p>
<h3 id="vdl-parameters-different-than-default-site-defined-parameters">VDL Parameters Different Than Default Site-Defined Parameters</h3>
<p>Why are the parameters on the VDL different than the default site-defined parameters?</p>
<p>Because the BCMA VDL parameters are the user’s (i.e., nurse’s) default settings. For example, when a nurse alters the default setting for certain fields (i.e., Start and Stop Times, and Column Sort Selection) on the BCMA VDL, these settings are retained in the user parameters and become the default setting each time the nurse logs on to BCMA.</p>
<p>The <em>Reset User Parameters</em> [PSB USER PARAM RESET] option in CHUI BCMA lets you reset user-selected parameters to site-defined parameters. See the <em>BCMA V. 3.0 Manager Manual</em> for more information.</p>
<h3 id="obtaining-centralized-funding">Obtaining Centralized Funding</h3>
<p>Is there a centralized funding plan available to help all facilities obtain up-to-date hardware for BCMA V. 3.0?</p>
<p>No, there is no centralized funding plan available at this time.</p></td>
</tr>
</tbody>
</table>