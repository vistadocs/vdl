---
title: EAS Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Revision History](#revision-history) - [# Introduction](#introduction) - [Process Overview](#process-overview) - [# Using the Software](#using-the-software) - [1010EZ Processing via List Manager](#1010ez-processing-via-list-manager) - [VA Form 1010EZ Application Status](#va-form-1010ez-applicat
audience: 
keywords: 
  - application
  - patient
  - form
  - easpatient
  - applicant
  - enrollment
  - action
  - processing
  - clerk
  - status
page_count: 0
word_count: 19157
section_count: 22
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-version-1-user-manual/001.png)

enrollment application system

user manual

September 2021

V*IST*A System Design & Development

# # Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# Introduction](#introduction)
  - [Process Overview](#process-overview)
- [# Using the Software](#using-the-software)
  - [1010EZ Processing via List Manager](#1010ez-processing-via-list-manager)
  - [VA Form 1010EZ Application Status](#va-form-1010ez-application-status)
- [Processing a VA Form 10-10EZ Application](#processing-a-va-form-10-10ez-application)
  - [![](eas-version-1-user-manual/002.png)What to do with a signed form …](#eas-version-1-user-manual002pngwhat-to-do-with-a-signed-form)
  - [What to do without a signed form…](#what-to-do-without-a-signed-form)
  - [Linking Applicant to PATIENT File (#2)](#linking-applicant-to-patient-file-2)
    - [New Patient](#new-patient)
    - [Existing Patient](#existing-patient)
  - [In Review](#in-review)
    - [Data Comparison – Existing Patient](#data-comparison-existing-patient)
    - [Data Comparison – New Patient](#data-comparison-new-patient)
    - [Notice a few 1010EZ data elements appearing in the example above are not highlighted, which indicates they are not ‘accepted’. Those particular data elements cannot be ‘accepted” because they are basic patient identifiers, and should only be modified under special circumstances. The data appearing under the column header VistA Data are the answers the enrollment clerk provided when entering the new patient data for this applicant through the standard Registration interface. (Refer to the Linking Applicant to PATIENT File \[#2\] section of this manual for further information.) This set of basic patient identifiers and other 1010EZ data elements, which cannot be accepted, are discussed in more detail in the Data Elements Not Filed section of this manual.](#notice-a-few-1010ez-data-elements-appearing-in-the-example-above-are-not-highlighted-which-indicates-they-are-not-accepted-those-particular-data-elements-cannot-be-accepted-because-they-are-basic-patient-identifiers-and-should-only-be-modified-under-special-circumstances-the-data-appearing-under-the-column-header-vista-data-are-the-answers-the-enrollment-clerk-provided-when-entering-the-new-patient-data-for-this-applicant-through-the-standard-registration-interface-refer-to-the-linking-applicant-to-patient-file-2-section-of-this-manual-for-further-information-this-set-of-basic-patient-identifiers-and-other-1010ez-data-elements-which-cannot-be-accepted-are-discussed-in-more-detail-in-the-data-elements-not-filed-section-of-this-manual)
  - [Using Action Commands](#using-action-commands)
    - [Accept All](#accept-all)
    - [Clear All](#clear-all)
    - [Accept Field](#accept-field)
    - [Special Cases of Data Acceptance](#special-cases-of-data-acceptance)
    - [Update Field](#update-field)
    - [Reset to New](#reset-to-new)
  - [Printed, Pending Signature](#printed-pending-signature)
  - [Signed](#signed)
    - [After Receiving a Signed Application](#after-receiving-a-signed-application)
  - [Filed](#filed)
    - [Filing 1010EZ Data into VISTA](#filing-1010ez-data-into-vista)
  - [Data Elements Not Filed](#data-elements-not-filed)
    - [Validity Checks](#validity-checks)
  - [Inactivated](#inactivated)
    - [Closing an Application](#closing-an-application)
- [Other 1010EZ Menu Options](#other-1010ez-menu-options)
  - [10-10EZ Quick Lookup \[EAS EZ QUICK LOOKUP\]](#10-10ez-quick-lookup-eas-ez-quick-lookup)
  - [Remove Signature Verification \[EAS EZ REMOVE SIGNATURE\]](#remove-signature-verification-eas-ez-remove-signature)
- [Help, Hints, & Frequently Asked Questions (FAQs)](#help-hints-frequently-asked-questions-faqs)
  - [Help](#help)
  - [FAQs](#faqs)
  - [Overall Process Schematic](#overall-process-schematic)
  - [EAS\1.0\190 in Host File DG53P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.](#eas10190-in-host-file-dg53p993kid-disables-the-link-to-patient-file-lz-action-in-the-electronic-10-10ez-processing-option)
  - [## # Appendix A-Sample Letter for VA Form 10-10EZ Mailing](#appendix-a-sample-letter-for-va-form-10-10ez-mailing)
  - [# Appendix B-Sample VA MailMan Message](#appendix-b-sample-va-mailman-message)
- [Glossary](#glossary)
- [Index](#index)
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 48%" />
<col style="width: 18%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision Date</th>
<th>Brief Description</th>
<th>Project Manager</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>June, 2001</td>
<td><p>Updated for patches EAS*1*1 and EAS*1*2.</p>
<p>Eliminated “training guide” aspect of the original User Manual. This resulted from combining some sections, rearranging the order of some sections, and eliminating others from the original version entirely.</p>
<p>New material was added to explain:</p>
<p>the enhanced behavior of the Accept Field (AF) action command</p>
<p>the new Remove Signature Verification menu option</p>
<p>the availability of online Help</p></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/14/2004</td>
<td><p>Update for Patch EAS*1*51:</p>
<p>Updated Process Overview section</p>
<p>Added sample VA MailMan message</p>
<p>Updated 10-10EA Processing section</p>
<p>Miscellaneous formatting and grammar corrections</p></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/15/2004</td>
<td>Updated list of data elements not filed (Patch EAS*1*51)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/20/2004</td>
<td>Updates to data elements not filed (Patch EAS*1*51)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/22/2003</td>
<td>Updates to data elements not filed (Patch EAS*1*51)</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/23/2004</td>
<td>Updated manual to reflect fictitious patient-specific data</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/30/2004</td>
<td>Updated to comply with new patient name and SSN standards set forth in SOP 192-352, Displaying Sensitive Data</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/29/2005</td>
<td>Updates to data elements not filed (Patch EAS*1*57) as well as screen samples</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/2/2005</td>
<td>Updates to data elements not filed (Patch EAS*1*66) on pg. 51 <u>(Test Director Defect #125)</u></td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/9/06</td>
<td>EAS*1*62 – Enrollment VistA Changes Early Release – removed military disability from the table that lists data elements not accessible via VistA screen interfaces</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/23/08</td>
<td>EAS*1*70 – Enrollment VistA Changes, Release 2 – added printing information in support of the addition of accepting foreign address information via the 10-10EZ and 10-10EZR forms.<br />
Also added new features in the Introduction section that were implemented in the effort to align the EAS data comparison display and processing with the Feb 2005 data collection format.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/25/08</td>
<td>Updated footers to reflect September 2008 Release date for patch EAS*1*70 – Enrollment VistA Changes, Release 2.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/17/09</td>
<td>Updated footers to reflect March 2009 Release date for patch EAS*1*70 – Enrollment VistA Changes, Release 2. Removed “Draft” indicators.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/30/09</td>
<td>Updated cover page to reflect new VistA LOGO, posted doc in new VES VDL site</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/11/09</td>
<td>Updated cover page to reflect old VistA LOGO, posted doc back into the EAS VDL site</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/10/09</td>
<td><p>Update for Patch EAS*1*81:</p>
<p>Added new user prompt information display to distinguish new patient from existing patient that has the same name.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/9/11</td>
<td>Update for Patch EAS*1*92: Added notes regarding military service not uploading if already verified and locked by ESR</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/5/2011</td>
<td>Update for Patch EAS*1*92: TW review. Updated footers to reflect release date and patch number.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/27/2012</td>
<td>Update for Patch EAS*1*92 – Changed footer date from January to March.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/13/2015</td>
<td>Update for Patch EAS*1*107 – Updated 10-10EZ form Data Element Names, Section and Item #s, and footer date and patch number.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/24/2020</td>
<td>Update for Patch EAS*1.0*190 in Host File DG_53_P993.KID – Updated Process Overview, Using the Software, 1010EZ Processing via List Manager, VA Form 1010EZ Application Status, Processing a VA Form 10-10EZ Application, Linking Applicant to PATIENT File (#2), and Overall Process Schematic sections to reflect that Patch EAS*1.0*190 disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/23/2021</td>
<td>Changed “Permanent Mailing Address” to “Mailing Address” throughout document (Patch EAS*1*203)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# # Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Process Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 1010EZ process begins when the veteran completes a VA Form 10-10EZ on the web application and indicates his or her preferred treatment facility. The online VA Form 10-10EZ is located at <https://www.1010ez.med.va.gov/sec/vha/1010ez/>.

IMPORTANT!  
ALL NEW ONLINE VA-FORM 10-10EZs ARE TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

When a veteran submits the online VA Form 10-10EZ, an email is sent to members of the G.VA1010EZ@\[LOCAL SITE\].VA.GOV mail group at the veteran’s preferred treating facility, via its parent facility, if appropriate. VAMC staff will print the email for immediate data input. For a faster turnaround time, the veteran is encouraged to print the completed VA Form 10-10EZ, sign it, and mail or fax the form to the parent facility of the preferred treatment facility. The web site provides the correct address and fax number for the parent facilities.

The ENROLLMENT APPLICATION SYSTEM (EAS) V. 1.0 contains the VA Form 10-10EZ Enrollment Application Processor module. Once locally installed, the EAS module will receive e-mail transmissions from the web server via GATEWAY.FORUM. It places all data from the VA Form 10-10EZ into the 1010EZ HOLDING File (#712) so staff responsible for enrollment and registration functions can further process the data.

Use of the 1010EZ Enrollment Application Processor module allows site personnel to view VA Form 10-10EZ data and manage the application without committing the data to the V*IST*A patient database. Enrollment staff may now review information submitted by the applicant, correspond with the applicant, and verify receipt of a signed VA Form 10-10EZ before loading data into the patient database. If the enrollment clerk decides to accept the submitted information, the EAS module makes all necessary updates to the PATIENT File (#2) and other relevant files. This uploaded information is then available to all V*IST*A users at the site, and the veteran’s data can be accessed through Registration, Enrollment, Scheduling, Integrated Billing, etc., as needed.

In support of the technology and business changes that are occurring with the implementation of the Enrollment System Redesign (ESR), ESR introduces some new and modified business functionality that required changes to the V*IST*A software via the release of EVC R2 (Enrollment VistA Changes Release 2).

- One of the required changes in the V*IST*A software was in support for adding foreign addresses in patient Mailing, Temporary and Confidential addresses. Currently there is no provision on the online 10-10EZ for beneficiaries to enter a foreign permanent address. However, to collect this information in V*IST*A for eventual use, staff can enter foreign address information via the Registration options. V*IST*A will require staff to enter a country before completing or updating a mailing address. In order for the EAS data filing system and V*IST*A to communicate, V*IST*A will default the Country field with United States for any mailing address downloaded, in process, or filed. Likewise, V*IST*A will use the default United States for any application received at the VA medical facility that does not have the Applicant Country field completed.

> For those instances where the applicant specified a country other than United States, (e.g., the veteran mails back a foreign address) staff can enter or edit the address in the Registration option once the application has been downloaded from EAS.

> V*IST*A will suppress the display of the Applicant Country field on the data comparison screens.

> V*IST*A will print the appropriate field headings when printing a 10-10EZ and 10-10EZR form. If the Country field equals United States, County, State, and Zip fields will print. Note that when the Country field equals United States, V*IST*A will not print the Country field.

> If the Country field is anything other than United States, V*IST*A will print the Province, Postal Code, and Country fields.

To improve usability and to promote standardization with other V*IST*A Registration, Enrollment and Financial Assessment options, the EAS application has aligned its data comparison display and processing with the Feb 2005 data collection format by implementing the following changes via EVC R2.

- The collection of Previous Calendar Year Gross Annual Income with the Feb 2005 Data Format was changed to collect 3 data elements rather than the 10 data elements collected with the pre Feb. 2005 format.
- The collection of Previous Calendar Year Net Worth with the Feb 2005 Data Format was changed to collect 3 data elements rather than the 5 data elements collected with the pre Feb. 2005 format.
- The marital status and dependents’ means test data items of Child Has Income and Income Available expanded to Child Has Income/Net Worth and Income/Net Worth Available to identify that these responses will apply to both dependent children’s gross annual income dollar amounts and the dependent children’s net worth dollar amounts.
- The Deductible Expenses money category for Gross Medical Expense has been renamed to Total Non-Reimbursed Medical Expenses.
- The constraints have been removed for entry and edit of the Deductible Expenses money category for Funeral And Burial Expenses – specifically, V*IST*A no longer requires the constraint that requires the veteran to have a spouse or dependent child.

It is important to understand that 1010EZ processing does *not* accomplish Registration, Enrollment, or Means Testing. Those functions must still be executed, when deemed necessary, through the established V*IST*A Patient Information Management System (PIMS) menu options. The 1010EZ module simply provides a method of managing electronically submitted applications for VA healthcare, which includes viewing and editing application data, printing the VA Form 10-10EZ with data, quick lookup of application status, and committing application data to the patient database.

# # Using the Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL ONLINE VA-FORM 10-10EZs ARE NOW TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

Enrollment clerks may process the VA Form 10-10EZ application through the following processing statuses before the data is committed to the site’s patient database via the Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\] menu option:

New

In Review

Printed, Pending Signature

Signed

Once the enrollment clerk decides to allow upload of the data to the patient database, the processing status becomes:

Filed

Another processing status exists, which can be used in cases where further, normal processing cannot or should not be done:

Inactivated

Each processing status is achieved as the enrollment clerk performs certain actions on the VA Form 10-10EZ application. The actions available to the enrollment clerk depend on the current processing status of the application. The enrollment clerk interface for the 1010EZ module is the V*IST*A List Manager interface.

The following is an example of the 10-10EZ Status List screen (a List Manager screen) displayed when using the 1010EZ Processing menu option.

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: IN REVIEW

Applicant SSN Vet. Type Rec'd Print To App#

1 EASPATIENT,ONE 000-14-9999 SC \<50% 11/02/00 Vet 473GB 000

2 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

3 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

4 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

5 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

7 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

8 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

9 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit// <u>EZ=4</u> 1010EZ Processing

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

There are eight actions available for this In Review application. They appear in the bottom portion of the 10-10EZ Processing screen; each has a two-letter code, which can be used to select and initiate the action.

Screen 1

For example, if the enrollment clerk wants to accept the data appearing on Line 5 (i.e., the Sex), then s/he would type AF for Accept Field and indicate the field location by typing =5 as follows:

Select Action: Next Screen// <u>AF=5</u>

The Accept Field action requires a line number to be specified because it is an action that pertains to a particular data item. Update Field is another action that requires a line number to be specified.

All the remaining actions listed on this screen example are actions that pertain to the VA Form 10-10EZ application as a whole; therefore, no line number needs to be specified.

For example, if the enrollment clerk wants to accept all data elements contained on the application, then s/he would enter AZ for the Accept All action, as demonstrated below.

Select Action: Next Screen// <u>AZ</u>

## 1010EZ Processing via List Manager 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A number of List Manager action items will be available to the enrollment clerk for 1010EZ processing. Use of any particular action depends upon the processing status of the application.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th>List Manager Action Item</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accept All (AZ)</td>
<td><p>The enrollment clerk accepts all VA Form 10-10EZ data. Every non-null data field on the data display appears highlighted on the List Manager screen.</p>
<p>If the applicant is an existing patient in <strong>V</strong><em>IST</em><strong>A</strong>, then existing data is over-written with data when the File 1010EZ (FZ) action is performed. Data fields that appear blank (i.e., null) do not overwrite existing patient database fields. If authoritative military service data has already been received from ESR, the filing of MSE data from the electrconic 10-10EZ will be blocked. This will be indicated by the MSE data not being highlighted.</p>
<p>Accept All (AZ) action can only be done when in processing status of In Review.</p></td>
</tr>
<tr class="even">
<td>Accept Field (AF)</td>
<td><p>The enrollment clerk may accept data items on a field-by-field basis. When a data item is accepted, it appears highlighted on the List Manager screen. If authoritative military service data has already been received from ESR, the filing of MSE data from the electrconic 10-10EZ will be blocked and a message will be displayed to the user. The message reads “Sorry, that data element cannot be ‘Accepted for ‘Filing’. Authoritative ESR data for military service exists. After filing this Application to VistA, use Register a Patient or Patient Enrollment to enter/upate data as needed”</p>
<p>If the enrollment clerk performs a second Accept Field (AF) action on a data item that has already been accepted, the data item is set back to a non-accepted state.</p>
<p>Accept Field (AF) action can only be done when in processing status of In Review.</p></td>
</tr>
<tr class="odd">
<td>Clear All (CZ)</td>
<td><p>The enrollment clerk resets all accepted data elements to non-accepted, and removes any direct edits done through the Update Field (UF) action.</p>
<p>Clear All (CZ) action can only be done when in a processing status of In Review.</p></td>
</tr>
<tr class="even">
<td>File 1010EZ (FZ)</td>
<td><p>The enrollment clerk commits all accepted data items to the <strong>V</strong><em>IST</em><strong>A</strong> patient database. Date of action and identity of user are recorded.</p>
<p>File 1010EZ (FZ) action can only be done when in processing status of Signed.</p>
<p>File 1010EZ (FZ) action changes the processing status of the electronic VA Form 10-10EZ to Filed.</p>
<p>Once Filed, the data is available for normal patient processing, e.g., full Registration, Means Testing, etc. After filing, the electronic VA Form 10-10EZ application is no longer available for processing, but can be viewed onscreen or printed.</p>
<p>Any health insurance-related information filed will be immediately available only to Integrated Billing users through the INSURANCE BUFFER File (#355.33). As with all new insurance data entered through the Registration menu options, this information must be verified and accepted by IB before it becomes available to other <strong>V</strong><em>IST</em><strong>A</strong> applications.</p></td>
</tr>
<tr class="odd">
<td>Inactivate 1010EZ (IZ)</td>
<td><p>If further processing cannot or should not be undertaken on a particular application, it may be inactivated. If problems arise during processing, the decision to Inactivate (IZ) an application must be made before the Verify Signature (VZ) action is performed.</p>
<p>Inactivate 1010EZ (IZ) action can be done when in processing statuses of New, In Review or Printed, Pending Signature. Date of action and identity of the enrollment clerk are recorded.</p>
<p>After executing the Inactivate 1010EZ (IZ) action, the processing status of the electronic VA Form 10-10EZ application becomes Inactivated.</p>
<p>Once Inactivated, no action can be taken on the application beyond simple viewing on the List Manager screen. Should it be later determined that the inactivated application should be processed, all data would need to be re-submitted via the web-based online VA Form 10-10EZ application.</p></td>
</tr>
<tr class="even">
<td>Link to Patient File (LZ)</td>
<td><p><strong>EAS*1.0*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.</strong></p>
<p><strong>ALL ONLINE VA-FORM 10-10EZs ARE NOW TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.</strong></p></td>
</tr>
<tr class="odd">
<td>Print 1010EZ (PZ)</td>
<td><p>The enrollment clerk prints a system-generated version of the VA Form 10-10EZ application with data. The data used will be all accepted data items. Any form field that does not have accepted data will be filled-in with existing <strong>V</strong><em>IST</em><strong>A</strong> patient data, whenever such data is available. The printed form may be sent to the applicant for signature.</p>
<p><strong>Note</strong>: Now that <strong>V</strong><em>IST</em><strong>A</strong> accepts a Foreign Address, it will print the appropriate field headings when printing a 10-10EZ and 10-10EZR form. If the Country field equals United States, County, State, and Zip fields will print. Note that when the Country field equals United States, <strong>V</strong><em>IST</em><strong>A</strong> will not print the Country field.</p>
<p>If the Country field is anything other than United States, <strong>V</strong><em>IST</em><strong>A</strong> will print the Province, Postal Code, and Country fields.</p>
<p>Print 1010EZ (PZ) action can be done for applications in processing statuses of In Review, Printed, Pending Signature, Signed, or Filed.</p>
<p>The first time the Print 1010EZ (PZ) action is performed on an In Review application, its status is changed to Printed, Pending Signature. Date of action and identity of the enrollment clerk are recorded.</p></td>
</tr>
<tr class="even">
<td>Reset to New (RZ)</td>
<td><p>The enrollment clerk may break the linkage to the <strong>V</strong><em>IST</em><strong>A</strong> patient database, set all previously accepted data items to non-accepted status, remove any direct edits of data, and erase all audit information recorded about the application to date by executing the Reset to New (RZ) action.</p>
<p>Reset to New (RZ) can be performed on applications with processing status of In Review or Printed, Pending Signature.</p>
<p>Reset to New (RZ) action places the electronic VA Form 10-10EZ application back to the New processing status.</p></td>
</tr>
<tr class="odd">
<td>Update Field (UF)</td>
<td><p>The Update Field (UF) action allows the enrollment clerk to overwrite a VA Form 10-10EZ application data item. This would normally be done to correct obvious typographical errors or to update the electronic VA Form 10-10EZ with hand-written insertions made by the applicant when signing a paper-copy of the form. VA FileMan editing functionality is used to perform each update.</p>
<p>Update Field (UF) action can be executed on applications with a processing status of In Review or Signed. Date of action and identity of user are recorded for each field updated.</p>
<p>After data has been filed to <strong>V</strong><em>IST</em><strong>A</strong>, the enrollment clerk can make any further updates needed by using the appropriate Registration or Means Test menu option.</p></td>
</tr>
<tr class="even">
<td>Verify Signature (VZ)</td>
<td><p>The enrollment clerk is able to verify that the applicant has signed and dated the printed VA Form 10-10EZ application.</p>
<p>Verify Signature (VZ) can be done on electronic VA Form 10-10EZ applications in a processing status of In Review or Printed, Pending Signature. Date of action and identity of user are recorded.</p>
<p>Verify Signature (VZ) changes the status of the application to Signed. Data on a VA Form 10-10EZ cannot be placed into the <strong>V</strong><em>IST</em><strong>A</strong> patient database until after signature verification.</p></td>
</tr>
</tbody>
</table>

## VA Form 1010EZ Application Status 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL ONLINE VA-FORM 10-10EZs ARE NOW TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

The following table provides an overview of each processing status and the valid action commands associated with it. Specific instructions and guidance regarding each status and action are included in the subsequent sections of this manual.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 30%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Processing Status</th>
<th>Definition</th>
<th>Available Actions</th>
<th>Next Expected Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>New</td>
<td><p>These are VA Form 10-10EZs that have been received by the VAMC electronically after being completed on-line by veteran applicants. Its data has been filed in the 1010EZ HOLDING File (#712) record.</p>
<p>The enrollment clerk may view and print New application data.</p></td>
<td><p>Link to Patient File (LZ) action – <strong>Disabled with EAS*1.0*190</strong></p>
<p>IZ Inactivate 1010EZ</p>
<p>To print a simple listing of all the data, use the List Manager hidden command of PS Print Screen. The PS command can always be used, regardless of processing status.</p></td>
<td><p>Link to Patient File (LZ) action – <strong>Disabled with</strong></p>
<p><strong>EAS*1.0*190</strong></p></td>
</tr>
<tr class="even">
<td>In Review</td>
<td><p>For an application In Review, the link to the VistA database is established. If the applicant is linked to an existing patient, the data from that patient record is displayed on the screen along side the VA Form 10-10EZ data for comparison. If the applicant cannot be matched to an existing patient record, then a new patient record is created. Of course, in this case, no comparison data is displayed.</p>
<p>If the linkage is found to be incorrect, the enrollment clerk will need to reset the status of the application back to New and restart the process.</p></td>
<td><p>AF Accept Field</p>
<p>AZ Accept All</p>
<p>CZ Clear All</p>
<p>RZ Reset to New</p>
<p>PZ Print 1010EZ</p>
<p>VZ Verify Signature</p>
<p>UF Update Field</p>
<p>IZ Inactivate 1010EZ</p></td>
<td><p>AF Accept Field</p>
<p>AZ Accept All</p>
<p>Continue to review application data, as needed. During this process, the enrollment clerk may accept all or selected data elements from the application for eventual upload to V<em>IST</em>A.</p></td>
</tr>
<tr class="odd">
<td><p>Printed,</p>
<p>Pending Signature</p></td>
<td><p>The application must be In Review before the VA Form 10-10EZ can be printed. Once the application has been printed, its status becomes Printed, Pending Signature.</p>
<p>The printed form will contain accepted data elements from the VA Form 10-10EZ. Data elements that were not accepted cannot be filed. If the applicant was matched to an existing <strong>V</strong><em>IST</em><strong>A</strong> patient, then data from that patient record will be used on the printed form in place of not-accepted or blank VA Form 10-10EZ data.</p></td>
<td><p>RZ Reset to New</p>
<p>PZ Print 1010EZ</p>
<p>VZ Verify Signature</p>
<p>IZ Inactivate 1010EZ</p>
<p>The form can be printed as often as necessary. But once printed, data review and edit commands (i.e., AF) cannot be used.</p>
<p>The usual reason for printing the VA Form 10-10EZ is to obtain the applicant’s signature whenever</p>
<p>the applicant never mailed in a signed form</p>
<p>the user has made changes to the original VA Form 10-10EZ data.</p></td>
<td><p>VZ Verify Signature</p>
<p>The printed form is sent to the applicant for signature. When returned, the enrollment clerk can verify receipt of the signed form.</p></td>
</tr>
<tr class="even">
<td>Signed</td>
<td><p>After the enrollment clerk verifies that a VA Form 10-10EZ has been received with the applicant’s signature, its status is Signed.</p>
<p>It is not necessary to use Print 1010EZ before using Verify Signature. If the enrollment clerk has not made any significant change to the original VA Form 10-10EZ data, and if the applicant sent a signed VA Form 10-10EZ to the site, then the enrollment clerk can issue the VZ command when the application is In Review.</p></td>
<td><p>PZ Print 1010EZ</p>
<p>FZ File 1010EZ</p>
<p>UF Update Field</p>
<p>Once Signed, the application may not be Inactivated. If some problem exists that prevents further processing, the application should be Inactivated before the signature is verified.</p></td>
<td><p>FZ File 1010EZ</p>
<p>The application data may be immediately Filed to <strong>V</strong><em>IST</em><strong>A</strong>.</p>
<p>It is possible that the Signed form has had data elements further modified by the applicant. The enrollment clerk may edit data through the UF Update Field action. Any data element which is directly edited by the enrollment clerk is automatically accepted.</p></td>
</tr>
<tr class="odd">
<td>Filed</td>
<td><p>Only data from a Signed form may be Filed to <strong>V</strong><em>IST</em><strong>A</strong>.</p>
<p>Only accepted data will be placed in the patient record.</p>
<p>After filing, the applicant’s data, now in a patient record, can be viewed and modified via the <strong>V</strong><em>IST</em><strong>A</strong> registration and means test screens.</p></td>
<td><p>PZ Print 1010EZ</p>
<p>The VA Form 10-10EZ may still be printed; the dates on which the applicant signature was verified and on which the data was filed will appear on the form.</p></td>
<td><p>Processing for this VA Form 10-10EZ application has been completed.</p>
<p>Once filed to the <strong>V</strong><em>IST</em><strong>A</strong> database, no further processing action can be taken on a VA Form 10-10EZ application.</p></td>
</tr>
<tr class="even">
<td>Inactivated</td>
<td>It may happen that an application is determined to be invalid, unacceptable, unnecessary, or for some reason cannot be processed further. The enrollment clerk may inactivate (i.e., close) the application to prevent inadvertent filing of the data.</td>
<td><p>Processing of a VA Form 10-10EZ application may be Inactivated at any time before the application has been Signed.</p>
<p>After it has been Inactivated<em>,</em> application data may only be viewed on screen.</p></td>
<td><p>The application is no longer available for processing.</p>
<p>Should there be a need to resume processing the application, it would need to be re-submitted via online VA Form 10-10EZ.</p></td>
</tr>
</tbody>
</table>

> *<u>Note</u>*

> The status can remain Signed indefinitely--the enrollment clerk must intentionally perform a File 1010EZ (FZ) action to store the data to V*IST*A.

> A VA Form 10-10EZ application cannot be inactivated once it moves to the Signed status; the Inactivate 1010EZ (IZ) action can only be done to a form with status of New, In Review or Printed, Pending Signature.

# Processing a VA Form 10-10EZ Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL ONLINE VA-FORM 10-10EZs ARE NOW TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

## ![](eas-version-1-user-manual/002.png)What to do with a signed form …

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*… mailed by the veteran at the time of submission of the electronic VA Form 10-10EZ*

Enrollment clerks should set time aside on a daily or other routine basis to check the V*IST*A system for New applications. Some veterans will complete the online form, print it, sign it, and mail it to the preferred medical treatment facility. The form, however, may take several days to reach the enrollment clerk. The enrollment clerk will know if there are applications signed and in the mail by viewing the list of New applications within the 1010EZ module.

To view the New applications, the enrollment clerk types New or *1* at the prompt, as shown in the following screen.

10-10EZ Application Processing --

Select one of the following:

1 New

2 In Review

3 Printed, Pending Signature

4 Signed

5 Filed

6 Inactivated

Select Applications to View: <u>1 New</u>

Please wait while processing...

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: NEW

Applicant SSN Vet. Type Rec'd Print To App#

1 EASPATIENT,ONE 000-14-9999 SC \<50% 11/02/00 Vet 473GB 000

2 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

3 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

4 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

5 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

7 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

8 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

9 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit//

After the enrollment clerk selects New applications to be viewed, the initial List Manager screen displays. Notice the column with the header “Print”. Applications that show “Vet” in this column are those for which the veteran has indicated that he/she will print a copy, sign it, and send to the Enrollment Coordinator at their selected facility.

As with other List Manager applications, the enrollment clerk enters the command and the line number of interest at the Select Action: prompt.

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: NEW

Applicant SSN Vet. Type Rec'd Print To App#

1 EASPATIENT,ONE 000-14-9999 SC \<50% 11/02/00 Vet 473GB 000

2 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

3 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

4 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

5 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

7 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

8 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

9 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit//<u>EZ=1</u> 1010EZ Processing

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

In this example, the next List Manager screen displays data for Application \#000, which is the application on Line 1. The current date and time and the List Manager page number are displayed at the top of the screen. The page number indicates the enrollment clerk’s current viewing location, as well as the total number of data screens available for display.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 0000-223110-2000 Vet Sending Signed Form?: YES

The next three lines show basic application data, such as the application number, applicant name, and status. The Web ID \# field is important because this is the unique identifying number assigned to this application by the web application software. Applicants are instructed to refer to the Web Submission ID when contacting a facility with questions about the VA Form 10-10EZ application. The Web Submission ID is the same as the web identification number listed on this screen and is viewable only in the 10-10EZ processing menus. The Application \# is an internal identifying number used by EAS v1.0.

Notice in the following example that at the Vet Sending Signed Form?: field, the response is YES. Here, the veteran has indicated that s/he printed, signed, and mailed the VA Form 10-10EZ application to the preferred medical treatment facility.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 0000-223110-2000 Vet Sending Signed Form?: YES

Further down on this screen, the right-hand column VistA Data is blank. This is because this is a New application and the applicant has not been matched to the site’s patient database.

Screen 2

The previous screen is the first of nine screens of data for Application \#000, EASPATIENT,ONE. The enrollment clerk can view each subsequent screen by hitting Enter at the Select Action: Next Screen// prompt. The enrollment clerk can also print the data screens in their entirety by entering the hidden List Manager action PS (Print Screen).

![](eas-version-1-user-manual/003.png)If the enrollment clerk wishes to continue processing of Application \# 000, the data must first be linked to the site’s patient database through the Link to Patient File (LZ) action. This action has been disabled with EAS\*1.0\*190 in Host File DG_53_P993.KID. The 10-10EZ processing is now implemented via the Enrollment System. This action invokes the standard patient lookup functionality associated with V*IST*A Registration. There are only two possible scenarios for patient lookup: the applicant cannot be matched to any patient record and a new patient record is created, or the applicant is matched to an existing patient record. (See later sections on *New Patient* and *Existing Patient*.)

Because the applicant has printed the VA Form 10-10EZ from his web browser and mailed a signed copy to the parent facility, the enrollment clerk can suspend any further action on the application until receipt of the signed form.

## What to do without a signed form…

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL ONLINE VA-FORM 10-10EZs ARE NOW TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

![](eas-version-1-user-manual/004.png)*… not mailed by the veteran at the time of VA Form 10-10EZ Electronic submission*

As indicated in the previous section, enrollment clerks should set time aside on a daily or other routine basis to check the V*IST*A system for New applications. Many veterans will complete the online VA Form 10-10EZ, but leave it up to the preferred medical treatment facility to print and mail the VA Form 10-10EZ for signature. These procedures outline actions the enrollment clerk needs to take in processing an application when a signed copy cannot be expected via surface mail from the veteran.

As with other List Manager applications, the enrollment clerk enters the command and the line number of interest at the Select Action: prompt.

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: NEW

<u>Applicant SSN Vet. Type Rec'd Print To App#</u>

1 EASPATIENT,ONE 000-14-9999 SC \<50% 11/02/00 Vet 473GB 000

2 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

3 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

4 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

5 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

7 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

8 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

9 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit// <u>EZ=9</u> 1010EZ Processing

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

In this example, the next List Manager screen displays data for Application \#000. The current date and time and the List Manager page number are displayed at the top of the screen. The page number indicates the enrollment clerk’s current viewing location, as well as the total number of data screens available for display.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-534310-2000 Vet Sending Signed Form?: NO

The next three lines show basic application data, such as the application number, applicant name, and status. The Web ID \# field is important because this is the unique identifying number assigned to this application by the web application software. Applicants are instructed to refer to the Web Submission ID when contacting a facility with questions about the VA Form 10-10EZ application. The Web Submission ID is the same as the web identification number listed on this screen. The Application \# is an internal identifying number used by EAS V. 1.0.

Notice in the following example that at the Vet Sending Signed Form?: field, the response is NO. This indicates that the veteran did not mail a signed VA Form 10-10EZ to the preferred medical treatment facility when the electronic VA Form 10-10EZ was submitted. Therefore, it is the responsibility of the facility to print out the VA Form 10-10EZ and mail it to the veteran for signature.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-534310-2000 Vet Sending Signed Form?: NO

Further down on this screen, the right-hand column VistA Data is blank. This is because this is a new application and the applicant has not been matched to the site’s patient database.

10-10EZ ProcessingNov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-534310-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE

5 Sex MALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-14-9999

10 Claim \# 36366333

11 DOB 12/10/1921

12 Religion BAPTIST

13 Place of Birth City MYTOWN

+ Enter ?? for more actions

LZ Link to Patient File IZ Inactivate 1010EZ

Select Action: Next Screen// <u>LZ</u> Link to Patient File

The previous screen is the first of nine screens of data for Application \#000, EASPATIENT,ONE. The enrollment clerk can view each subsequent screen by hitting Enter at the Select Action: Next Screen// prompt. The enrollment clerk can also print the data screens in their entirety by entering the hidden List Manager action PS (Print Screen).

The enrollment clerk will need to continue processing the application by first executing the Link to Patient File (LZ) action. This action invokes the standard patient lookup functionality associated with V*IST*A Registration. There are only two possible scenarios for patient lookup: the applicant cannot be matched to any patient record and a new patient record is created, or the applicant is matched to an existing patient record. (See later section on *Linking Applicant to Patient File.)*

In this example, let’s assume the applicant did not exist in the facility’s patient database. At the conclusion of the Link to Patient File (LZ) action, the 10-10EZ applicant will be linked to a newly created patient record. The status of the 10-10EZ application will have changed from New to In Review.

Notice the expanded list of actions (in the command section at the lower part screen), which are available to In Review applications.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-534310-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-54-8111 000-54-8111

10 Claim \# 36366333

11 DOB 04/04/1949 04/04/1949

12 Religion UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

Because the applicant is new to this site, the enrollment clerk created a new record in the PATIENT File (#2) with minimal data. That data is shown on the right side of the screen as VistA Data. Most of the data elements shown in the center 10-10EZ Data portion of the screen appear highlighted. Highlighting indicates that the data has been “accepted”. All 10-10EZ data is automatically “accepted” for applicants who are new patients. (Refer to the Data Comparison section of this manual for further information.) Only “accepted”10-10EZ data appears on a printed VA Form 10-10EZ application. (Refer to the Printed, Pending Signature section of this manual for further information.)

![](eas-version-1-user-manual/005.png)At this point the enrollment clerk must print this application using the Print 1010EZ (PZ) action. The status of the application will have changed from In Review to Printed, Pending Signature.

The printed application is then sent to the veteran for signature. The enrollment clerk must suspend any further action on the application until receipt of the signed form.

## Linking Applicant to PATIENT File (#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL NEW ONLINE VA-FORM 10-10EZs ARE TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option.

If the enrollment clerk wishes to complete processing of the VA Form 10-10EZ application, the applicant must first be linked to the site’s patient database through the Link to Patient File (LZ) action. This action invokes the standard patient lookup functionality associated with V*IST*A Registration. There are only two possible scenarios for patient lookup: the applicant cannot be matched to any patient record and a new patient record is created, or the applicant is matched to an existing patient record.

Enrollment clerks familiar with V*IST*A Registration functionality will know that the way in which they respond to the Select PATIENT NAME: prompt will greatly affect the system’s response. Enrollment clerks should follow the lookup method approved at their site. This may include one or more of the following:

- Initial of last name plus the last four digits of the SSN
- First few letters of last name
- Full last name
- Full SSN
- Full name (e.g., Last,First MI)

For example, the enrollment clerk queried the patient database by entering the first few letters of the last name, which in this case provided no possible match.

Select PATIENT NAME: TEST

1 EASPATIENT,ONE 11-23-66 000112222 NON-VETERAN (OTHER)

2 EASPATIENT,ONE 12-12-12 000000123 NSC VETERAN

3 EASPATIENT,ONE 10-05-28 000998888 NSC VETERAN

4 EASPATIENT,ONE D 02-10-50 000000456 NSC VETERAN

The enrollment clerk then entered the initial of the last name plus the last four digits of the SSN, which also produced no match.

CHOOSE 1-4:

Select PATIENT NAME: E9999 ??

Then the enrollment clerk tried the last name without the first name to be sure no match existed before entering the applicant’s full name.

Select PATIENT NAME: EASPATIENT ??

Select PATIENT NAME: EASPATIENT,ONE

ARE YOU ADDING ' EASPATIENT,ONE ' AS A NEW PATIENT (THE 3032ND)? No// YES (Yes)

At the conclusion of the Link to Patient File (LZ) action, the 10-10EZ applicant will be linked to either an existing patient in the facility’s V*IST*A database, or to a newly created patient record.

For example, the enrollment clerk queried the patient database by entering the first few letters of last name, which in this case provided no possible match.

Select PATIENT NAME: EASPATIENT

1 EASPATIENT,ONE 12-13-71 000112222 NON-VETERAN (OTHER)

2 EASPATIENT,ONE 10-18-21 000000123 NSC VETERAN

The enrollment clerk then entered the initial of last name plus the last four digits of the SSN, which also produced no match.

CHOOSE 1-4:

Select PATIENT NAME: P8111 ??

Then the enrollment clerk tried last name with first name to be sure of no match before entering the applicant’s full name.

A 10-10EZ applicant who *is not* a patient at a given facility may have the same name as a person who *is* a patient there and hence has a record in the facility’s patient database.  In this scenario, if the enrollment clerk enters the 10-10EZ applicant’s name but not SSN, an erroneous match will result.  To help prevent inappropriate linkages, whenever the applicant is matched to an existing patient record, a new user prompt inquiring whether this is the correct patient will automatically display.  If the clerk replies ‘NO’, a new instruction will appear to enter the name of the 10-10EZ patient in double quotation marks.  After the enrollment clerk has complied, processing continues as described in the section entitled “New Patient.”

If the 10-10EZ applicant already *is* a patient at the facility and is thus represented in its database, the enrollment clerk should respond ‘YES’ to the ‘Is this is the correct patient?’ prompt, provided that the lookup has made the proper match.  In this scenario, where the reply to the prompt is ‘YES’, processing immediately continues as described in the section entitled “Existing Patient."

*‘IS THIS THE CORRECT PATIENT? YES//’ Prompt Is Answered ‘NO’:*

Select OPTION NAME: EAS EZ MENU 10-10EZ Menu

QL 10-10EZ Quick Lookup

EZ Electronic 10-10EZ Processing

RS Remove Signature Verification

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select 10-10EZ Menu Option: EZ Electronic 10-10EZ Processing

10-10EZ Application Processing --

Select one of the following:

1 New

2 In Review

3 Printed, Pending Signature

4 Signed

5 Filed

6 Inactivated

Select Applications to View: 1 New

Please wait while processing...

<u>10-10EZ Status List Jul 14, 2009@13:56:40 Page: 1 of 1</u>

Application Status: NEW

<u>Applicant SSN Vet. Type Rec'd Print To App.#</u>

1 EASPatient, One 000-00-0000 NSC 02/16/07 VA 325

2 EASPatient, Two 000-00-0000 SC \<50% 09/01/04 Vet 442GC 309

3 EASPatient, Three 000-00-0000 NSC 09/22/04 Vet 442GC 312

4 EASPatient, Four 000-00-0000 NSC 09/22/04 Vet 442GC 313

5 EASPatient, Five 000-00-0000 NSC 02/21/07 VA 999 327

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit// EZ 1010EZ ProcessingSelect 1010EZ(s): (1-5): 1

<u>10-10EZ Processing Jul 14, 2009@13:56:51 Page: 2 of 13</u>

Application \#: 327 (999 ) Status: NEW

Applicant: EASPATIENT,One Date Rec'd: 02/16/07

Web ID \#: XXXX-XXXXX-XXXX Vet Sending Signed Form?: NO

<u>+ Data Item 10-10EZ Data VistA Data</u>

13 Street Address 1 MAIN ST

14 City ALBANY

15 State NEW YORK

16 Zipcode 12208

17 County ALBANY (001)

18 Home Phone (518)343-9883

19 Email EXAMPLE@HOTMAIL.COM

20 Cell Phone (518)333-8888

21 Pager \# (518)333-8888

22 Appointment Request YES

23 Seen at VA Med. Fac NO

24 Marital Status MARRIED

\+ Enter ?? for more actions

LZ Link to Patient File IZ Inactivate 1010EZ

Select Action: Next Screen// LZ Link to Patient File

Applicant Data Application \#: 325 Received: FEB 16, 2007

Name: EASPATIENT,One

SSN: 000-00-0000 DOB: 03/05/1948 Sex: Male

Veteran Type: NSC

Enter Applicant data as prompted --

Select PATIENT NAME: EASPATIENT,OneEASPATIENT,One 1-15-80 555041212

NO NSC VETERAN

WARNING : \*\* This patient has been flagged with a Bad Address Indicator.

Enrollment Priority: Category: IN PROCESS End Date:

Combat Vet Status: ELIGIBLE End Date: 12/31/2009

Press ENTER to continue

IS THIS THE CORRECT PATIENT? YES// NO \<*<u>Note: ‘No’ triggers new user instruction\></u>*If there are already one or more patients with the same name,re-enter the name in double quotes, for example, "DOE,JOHN".Select PATIENT NAME: "EASPATIENT,One"ARE YOU ADDING EASPATIENT,OneAS A NEW PATIENT (THE 61985TH)? No// Y (Yes)

### New Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example uses the scenario where the applicant cannot successfully be matched to the facility patient database and a new patient record must be created.

As explained earlier, the enrollment clerk uses several patient lookup methods in trying to find a match with the applicant. Since there is no match, the enrollment clerk eventually enters the applicant’s full name and responds YES to the ARE YOU ADDING A NEW PATIENT? question.

There are several pieces of basic demographic data required to establish the patient record. To help the enrollment clerk answer the prompts correctly, the applicant’s basic identifying data is displayed at the top of the screen. The screen display below shows the additional prompts answered by the enrollment clerk.

Applicant Data Application \#: 000 Received: 10/01/2000

Name: EASPATIENT,ONE

SSN: 000-14-9999 DOB: 12/10/1921

Veteran Type: SC \<50%

Enter Applicant data as prompted --

Select PATIENT NAME: EAS

1 EASPATIENT,ONE 11-23-66 000112222 NON-VETERAN (OTHER)

2 EASPATIENT,ONE 12-12-12 000000123 NSC VETERAN

3 EASPATIENT,ONE 10-05-28 000998888 NSC VETERAN

4 EASPATIENT,ONE 02-10-50 000000456 NSC VETERAN

CHOOSE 1-4:

Select PATIENT NAME: E9999 ??

Select PATIENT NAME: EASPATIENT,ONE

ARE YOU ADDING ' EASPATIENT,ONE ' AS A NEW PATIENT (THE 3032ND)? No// N (No)

Select PATIENT NAME: EASPATIENT,ONE

ARE YOU ADDING ' EASPATIENT,ONE ' AS A NEW PATIENT (THE 3032ND)? No// Y (Yes)

PATIENT SEX: <u>M</u> MALE

PATIENT DATE OF BIRTH: <u>12/10/1921</u> (DEC 10, 1921)

PATIENT SOCIAL SECURITY NUMBER: <u>000-14-9999</u>

PATIENT TYPE: <u>SC</u> VETERAN

PATIENT VETERAN (Y/N)?: <u>Y</u> YES

\[additional system responses may appear here for MPI inquiry\]

Attempting to connect to the Master Patient Index in Austin...

If no or inexact DOB or common name, this request

may take some time, please be patient...

Patient was not found in the MPI...

Could not connect to MPI, Assigning Local ICN...

One moment please...

Preparing for data comparison to VistA Patient database...

....

Please wait while processing...

The application is again opened in the main screen, the review has begun and the system has automatically changed the processing status from New to In Review.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 0000-223110-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-14-9999 000M-14-9999

10 Claim \# 36366333

10 DOB 12/10/1921 12/10/1921

11 Religion BAPTIST

12 Place of Birth City MYTOWN+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

Because the applicant is new to this site’s PATIENT File (#2), the enrollment clerk created a new record in the PATIENT File (#2) with minimal data. That data is also shown on the right side of the screen as VistA Data.

Notice the center portion of the screen where 10-10EZ Data is displayed. On this initial page of data, as well as on all the following pages (there are 9 pages for this applicant), most of the data elements in the 10-10EZ Data column will be highlighted in reverse video. Highlighting of a data element indicates that it is ‘accepted’. The 1010EZ module automatically ‘accepts’ data for an applicant who is associated with a new patient record. (Refer to the Data Comparison section of this manual for further information.)

### Existing Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the next example, the screens display a patient lookup scenario when the applicant is matched to an existing patient record. First, a New application is selected from the initial List Manager screen.

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: NEW

<u>Applicant SSN Vet. Type Rec'd Print To App#</u>

1 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

2 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

3 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

4 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

5 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

7 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

8 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit// <u>EZ=3</u> 1010EZ Processing

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

Next, the enrollment clerk selects the LZ action:

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE

5 Sex MALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-84-3111

10 Claim \# 00000000

11 DOB 04/19/1948

12 Religion UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN

+ Enter ?? for more actions

LZ Link to Patient File IZ Inactivate 1010EZ

Select Action: Next Screen// <u>LZ</u> Link to Patient File

Basic application data is displayed at the top of the next screen so the patient lookup process can begin. The enrollment clerk enters the first few letters of applicant’s last name, and in this example, is presented with four possible matches.

Applicant Data Application \#: 000 Received: 11/02/2000

Name: EASPATIENT,ONE SSN: 000-84-3111 DOB: 04/19/1948

Veteran Type: SC \<50%

Enter Applicant data as prompted --

Select PATIENT NAME: <u>TEST</u>

1 EASPATIENT,ONE 4-19-48 000834111 SC VETERAN

2 EASPATIENT,ONE 11-21-49 000040449 NSC VETERAN

3 EASPATIENT,ONE 4-14-31 000994949 NSC VETERAN

4 EASPATIENT,ONE 3-13-48 000355300 NSC VETERAN

CHOOSE 1-4: <u>1</u> EASPATIENT,ONE 4-19-48 000843111 SC VETERAN

One moment please...

Preparing for data comparison to VistA Patient database...

....

Please wait while processing...

To continue with this example, the enrollment clerk has decided that the first choice among the four possibilities listed is likely to be a match. Data from the selected patient’s record is displayed on the right side of the main data comparison screen, which now appears.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-83-4111

10 Claim \# 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

Notice that the processing status has changed from New to In Review.

Unlike the previous example in which a new patient record was created, notice that this screen display does not show highlighted data elements in the 10-10EZ Data column. When the applicant has been matched to an existing patient record, the 10-10EZ data must be accepted by the enrollment clerk field-by-field. An accepted 10-10EZ data element will eventually overwrite data in the V*IST*A patient record; data that is not accepted will not be filed into the patient record. If authoritative military service data has already been received from ESR, the filing of MSE data from the electrconic 10-10EZ will be blocked and a message will be displayed to the user. The message reads “Sorry, that data element cannot be ‘Accepted for ‘Filing’. Authoritative ESR data for military service exists. After filing this Application to VistA, use Register a Patient or Patient Enrollment to enter/upate data as needed”

(Refer to the Data Comparison section of this manual for further information.)

The enrollment clerk should review all pages of data available to be sure that the applicant and the selected patient are indeed a match. The enrollment clerk may decide after further review that the 1010EZ applicant and the V*IST*A patient selected are not, in fact, the same person. The Reset to New (RZ) action command should then be used to break the linkage between the applicant and the patient record, and the application will be reset to a status of New. (See the *Reset to New* section later in this manual.)

> *<u>Note</u>*

> Establishing the PATIENT File (#2) link avoids the need for the enrollment clerk to re-process the applicant through V*IST*A’s patient lookup, duplicate checking, name standardization, Master Patient lookup, etc., functions each time the data comparison screen is entered.

## In Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Comparison – Existing Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data comparison is done whenever the applicant has been matched to an existing patient record.

The In Review application is displayed in the middle column with data from the site’s patient database in the right-hand column.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

In this example, the enrollment clerk should carefully inspect all the data elements presented on the nine List Manager screens, which show comparison between applicant EASPATIENT,ONE and V*IST*A patient EASPATIENT,ONE. The enrollment clerk may also wish to inspect other information for the patient available in the V*IST*A database by using other menu options, e.g., Patient Inquiry, View Registration Data, and View a Past Means Test. If it is determined that the applicant and the patient are not the same person, then the Reset to New (RZ) action is used to break the linkage with the V*IST*A database record and start over.

The basic intent of data comparison is for the enrollment clerk to determine which 10-10EZ data elements are to be accepted for eventual upload to the site’s V*IST*A database. Any data element which is not accepted will not appear on the printed VA Form 10-10EZ; nor will it ever be filed to the patient database. Each data element that is accepted will overwrite existing data when the enrollment clerk performs the File 1010EZ (FZ) action.

There are five commands available that initiate actions relevant to data comparison and to the In Review application in general. They are:

> AF Accept Field – mark a single or range of 10-10EZ data elements as accepted

> AZ Accept All – mark all 10-10EZ data elements as accepted

> UF Update Field – directly edit a single 10-10EZ data element

> CZ Clear All – resets all 10-10EZ data elements to non-accepted

> RZ Reset to New – break the link to the V*IST*A patient database and start over

### Data Comparison – New Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AF and AZ actions are particularly useful in data comparison situations where the 10-10EZ applicant data is being compared to existing V*IST*A patient data. However, all five actions mentioned above can be used when the applicant has been linked to a new patient record as well. Applicants that are *new* to the site’s patient database will have all possible10-10EZ data elements *automatically* accepted so there is generally no need to use the Accept All (AZ) action.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-534310-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-54-8111 000-54-8111

10 Claim \# 36366333

11 DOB 04/04/1949 04/04/1949

12 Religion UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

### Notice a few 1010EZ data elements appearing in the example above are not highlighted, which indicates they are not ‘accepted’. Those particular data elements cannot be ‘accepted” because they are basic patient identifiers, and should only be modified under special circumstances. The data appearing under the column header VistA Data are the answers the enrollment clerk provided when entering the new patient data for this applicant through the standard Registration interface. (Refer to the Linking Applicant to PATIENT File \[#2\] section of this manual for further information.) This set of basic patient identifiers and other 1010EZ data elements, which cannot be accepted, are discussed in more detail in the Data Elements Not Filed section of this manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accept Field (AF) action command can be used to toggle acceptance of most 1010EZ data elements from “accepted” to “not accepted” or vice versa. In the example above, for instance, the enrollment clerk could use an AF=7 command to toggle Religion data element to “not accepted”. A second use of the AF=7 command would toggle the Religion data element back to “accepted”. (Refer to the Accept Field section of this manual for further information.).

## Using Action Commands 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Accept All 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A quick way to mark all the 10-10EZ data as accepted is by use of the Accept All (AZ) command. The following example uses the AZ action in the case of an applicant matched to an existing patient record.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 52361-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// AZ10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

Data on all nine display screens for this VA Form 10-10EZ are accepted using the Accept All (AZ) action.

> *<u>Note</u>*

> Any question contained in the On-Line 10-10EZ application, which was not answered by the applicant, will not appear on the data comparison screens of the 1010EZ module. So in the preceding example, if the applicant had not provided a home telephone number when filling out the on-line form, then a line for Home Telephone would not appear on the data comparison screen. Therefore, the Home Telephone for the existing V*IST*A patient would not be displayed.

### Clear All 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clear All (CZ) action can be used to reset all 10-10EZ data elements to a non-accepted condition. Note, though, that this action is not an option for a new patient. The enrollment coordinator can, however, employ the Accept Field (AF) action to toggle-off accept, one field at a time.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// CZ Clear All

When this action is selected, the system will remove all highlighting in the 10-10EZ Data column and 10-10EZ data elements that have been accepted will be reset to non-accepted. After using the Clear All (CZ) action, the Accept Field (AF) and Accept All (AZ) actions can be used again as needed to accept the desired 10-10EZ data elements.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

### Accept Field 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another way for the enrollment clerk to accept 10-10EZ data is with the Accept Field (AF) action. The Accept Field action allows the enrollment clerk to accept a single 10-10EZ data element. This action is useful when the enrollment clerk wants to select a limited number of 10-10EZ data elements for eventual filing to the V*IST*A patient record. Accepted data appears highlighted on the screen.

When using the Accept Field (AF) action, the enrollment clerk will also need to specify a data element line or a range of data element lines.

> Select Action: Next Screen//<u>AF=13</u>

> or

> Select Action: Next Screen//<u>AF=5,11,13</u>

> or

> Select Action: Next Screen//<u>AF=5,7-13</u>

In the following example, the enrollment clerk typed AF=20 to accept the applicant’s Home Phone.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

14 Place of Birth State MYSTATE MYSTATE

15 Street Address 123 ANYWHERE ST. 123 ANYWHERE ST.

16 City MYTOWN MYTOWN

17 State MYSTATE MYSTATE

18 Zip 99999 99999

19 County MYCOUNTY MYCOUNTY

20 Home Phone (999) 999-9998 (999) 999-9999

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// <u>AF=20</u>10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

14 Place of Birth State MYSTATE MYSTATE

15 Street Address 123 ANYWHERE ST. 123 ANYWHERE ST.

16 City MYTOWN MYTOWN

17 State MYSTATE MYSTATE

18 Zip 99999 99999

19 County MYCOUNTY MYCOUNTY

20 Home Phone (999)999-9998 (999) 999-9999

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

> *<u>Note</u>*

> Once accepted, any data element can be placed back into a non*-*accepted condition by performing another Accept Field (AF) action on the same data element. This can occur reiteratively until the enrollment clerk is satisfied with the result.

### Special Cases of Data Acceptance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are some 10-10EZ data elements which the system automatically accepts (pre-accepted) without any action by the enrollment clerk.

This is true for data related to health insurance and Medicare coverage. If the VA Form 10-10EZ application is filed eventually to the V*IST*A database, then health insurance and Medicare information always will be filed, so acceptance cannot be toggled-off for those data elements. The data is passed to Integrated Billing for further review.

Another case of pre-acceptance relates to spouse and dependent data that is stored in files associated with income testing; it cannot be toggled-off. Because of the inter-dependencies involved and the need to preserve database integrity, the filing of data to these income-related files must be complete and consistent. All income-related data elements will be filed as long as the applicant does not have an income test for the current income-reporting year at the preferred medical treatment facility that received the VA Form 10-10EZ application. Note that the current income-reporting year is the year immediately preceding the current year, i.e., 2000 is the current income-reporting year for applications received in 2001.

However, the enrollment clerk may use the Update Field (UF) action to edit any pre-accepted 10-10EZ data element, if needed. All the data filed into the V*IST*A patient database by the 1010EZ module can be edited when using V*IST*A Registration, Enrollment, and/or Means Test menu options.

### Update Field 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Update Field (UF) action allows the enrollment clerk to directly edit a selected field. The editing is done through FileMan.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

14 Place of Birth State MYSTATE MYSTATE

15 Street Address 123 ANYWHERE ST. 123 ANYWHERE ST.

16 City MYTOWN MYTOWN

17 State MYSTATE MYSTATE

18 Zip 99999 99999

19 County MYCOUNTY MYCOUNTY

20 Home Phone (999)999-9998 (999) 999-9999

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// <u>UF=15</u> Update Field

APPLICANT STREET ADDRESS: <u>123 ANYWHERE ST.</u>

When the enrollment clerk selects UF, an updated data element is automatically accepted, as seen in the next screen display where the data for Street Line 1 is highlighted to indicate acceptance.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

14 Place of Birth State MYSTATE MYSTATE

15 Street Address 1234 ANYWHERE ST. 123 ANYWHERE ST.

16 City MYTOWN MYTOWN

17 State MYSTATE MYSTATE

18 Zip 99999 99999

19 County MYCOUNTY MYCOUNTY

20 Home Phone (999) 999-9998 (999) 999-9999

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//

> *<u>Note</u>*

> The Update Field (UF) action should be used judiciously to correct obvious typographical errors, or to amend data to comply with official sources or as directed by the applicant.

> Any 10-10EZ data element directly edited via Update Field (UF) is automatically accepted for eventual filing into the V*IST*A database. This acceptance cannot be toggled off by executing an Accept Field (AF) command on the data element. To reinstate the original data values to updated fields requires the enrollment clerk to Reset to New (RZ).

### Reset to New 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reset to New (RZ) allows the enrollment clerk to scrap everything done to a VA Form 10-10EZ application and to start over again. Reset to New is only available for applications in the status of In Review or Printed, Pending Signature.

This Reset to New action sets the processing status of the application back to New. When this occurs:

1)  Any accepted data items are placed back in their original state, i.e., all Accept Field (AF) actions are reversed.
2)  Original data is restored to any data element that was edited through Update Field (UF).
3)  The link (i.e., match-up) to the PATIENT File (#2) established through the Link to Patient File (LZ) action is broken.
4)  The application is placed back on the New application list.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE MAIDEN,ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

14 Place of Birth State MYSTATE MYSTATE

15 Street Address 1234 ANYWHERE ST. 123 ANYWHERE ST.

16 City MYTOWN MYTOWN

17 State MYSTATE MYSTATE

18 Zip 99999 99999

19 County MYCOUNTY MYCOUNTY

20 Home Phone (999) 999-9998 (999) 999-9999

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// RZ Reset to New

Notice on the following screen, the street address now reads as it was originally received and the application Status is New.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: NEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN,ONE

5 Sex MALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-84-3111

10 Claim \# 36366333

11 DOB 04/19/1948

12 Religion UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN

14 Place of Birth State MYSTATE

15 Street Address 123 ANYWHERE ST.

16 City MYTOWN

17 State MYSTATE

18 Zip 99999

19 County MYCOUNTY

20 Home Phone (999) 999-9999

+ Enter ?? for more actions

LZ Link to Patient File IZ Inactivate 1010EZ

Select Action: Next Screen//

## Printed, Pending Signature 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-version-1-user-manual/006.png)

If the applicant indicated that a signed copy of the VA Form 10-10EZ submission would be mailed to the facility, and if the signed copy is not received within 30 days, then the enrollment clerk should use the Print 1010EZ (PZ) action to print the form and mail it to the veteran for signature. Another 30 days should be allowed for the applicant to return the signed form.

If the applicant indicated that he would not print the VA Form 10-10EZ, and expects the facility to print and send a copy to him for signature, then the enrollment clerk should use the Print 1010EZ (PZ) action as soon as possible to generate the form. If it is not returned by the applicant within 30 days, another copy should be generated and sent for signature. As above, if the first 30-day period passes without receiving the signed form from the veteran, then it should be printed and mailed again, allowing an additional 30 days for a returned signature.

When the enrollment clerk selects the Print 1010EZ (PZ) action, the accepted data will be printed on a VA Form 10-10EZ. Any data element that has not been marked as accepted will not appear on the printed form. If V*IST*A data exists for a non-accepted 10-10EZ data element, then the V*IST*A data will appear on the printed form.

In the screen below, the enrollment clerk selects the Print 1010EZ (PZ) action to print the form. The form requires 132 columns. It cannot be displayed on the screen and must be sent to a valid system print device; it cannot be sent to a printer connected to a personal computer system.

The VA Form 10-10EZ printed from V*IST*A has been implemented to follow the format of the VA Form 10-10EZ seen in the web application to the greatest degree possible. It includes the Privacy Act, Paperwork Reduction Act, medical release consent, and signature blocks.

The enrollment clerk will see that the processing status, seen in the upper right portion of the screen, has changed from In Review to Printed, Pending Signature.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE MAIDEN, ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen//<u>PZ</u> Print 1010EZ

This output requires a 132 column output printer.

Output to SCREEN will be unreadable.

DEVICE: HOME// <u>P-HP132</u>

Requested Start Time: NOW// <u>\<Enter\></u> (NOV 19, 2000@20:22:53)

Please wait while processing...

Enter RETURN to continue or '^' to exit:

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: PRINTED,PENDING SIG

Applicant: EASPATIENT,ONE Date Rec'd: 11/02/2000

Web ID \#: 00000-545845-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE MAIDEN, ONE

5 Sex MALE MALE

6 Span/Hisp/Latino? NO (S) NO (S)

7 Black/African Am.? YES (S) YES (S)

8 Asian? YES (S) YES (S)

9 SSN 000-84-3111 000-84-3111

10 Claim \# 36366333 36366333

11 DOB 04/19/1948 04/19/1948

12 Religion UNKNOWN/NO PREFERENC UNKNOWN/NO PREFERENC

13 Place of Birth City MYTOWN MYTOWN

+ Enter ?? for more actions

RZ Reset to New VZ Verify Signature

PZ Print 1010EZ IZ Inactivate 1010EZ

Select Action: Next Screen//

> *<u>Note</u>*

> The enrollment clerk may obtain a printed copy of all 1010EZ data along with any existing V*IST*A patient data by using the hidden List Manager of Print Screen (PS) which prints all the data comparison screens. This printed output is for internal use only and should not be sent to the veteran.

## Signed 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### After Receiving a Signed Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-version-1-user-manual/007.png)It is not until the enrollment clerk receives a signed application from the veteran that data can actually be stored in V*IST*A. When the enrollment clerk receives a signed application from a veteran, the veteran's electronic VA Form 10-10EZ should be located and retrieved for viewing. The enrollment clerk may receive the signed form at the start of the application processing in V*IST*A, or may have to wait up to 30 days for the signed application. Or, if the veteran requested the printed VA Form 10-10EZ to be sent to him/her for signature, a wait time of 60 days is recommended.

The electronic VA Form 10-10EZ application will most likely be in either a New or Printed, Pending Signature status, although some may be in an In Review status as well.

Applications still in the New status will be those where the applicant indicated he has printed his VA Form 10-10EZ and intends to sign and send it to the medical facility.

Those applications in the Printed, Pending Signature status will generally be those where the applicant has indicated he wants the VA facility to print and send the completed form for signature.

Regardless of which category the signed application falls into, the enrollment clerk may face a situation where the veteran has made hand-written changes to data on the printed (i.e., paper) form. In other words, the enrollment clerk may need to edit the electronic VA Form 10-10EZ data with the veteran’s hand-written changes on the printed VA Form 10-10EZ. Direct edits to 10-10EZ data are accomplished through the Update Field (UF) action. Update Field is available only for applications in either the In Review or the Signed processing status.

If the application is still New, then in order to use the Update Field (UF) action, the enrollment clerk must first place the application into the In Review status by using the Link to Patient File (LZ) command. The Update Field (UF) action can be seen in the command section at the lower part of the List Manager screen for the In Review application.

If the application is Printed, Pending Signature, the enrollment clerk must first place the application into the Signed status in order to use the Update Field (UF) action; this is done by using the Verify Signature (VZ) command. The Update Field (UF) action can be seen in the command section at the lower part of the List Manager screen for the Signed application.

For example, the enrollment clerk has received a signed, printed application, returned by veteran ONE, EASPATIENT (SSN 000-45-6789) via surface mail. The enrollment clerk can clearly see that this paper VA Form 10-10EZ was printed from the VistA 10-10EZ module, and not from the online VA Form 10-10EZ web site. Therefore, the status of this application must be Printed, Pending Signature.

First, the enrollment clerk locates the application from the list of applications in the Printing, Pending Signature status.

10-10EZ Status List Nov 09, 2000 13:29:56 Page: 1 of 1

Application Status: PENDING SIGNATURE

Applicant SSN Vet. Type Rec'd Print To App#

1 EASPATIENT,ONE 000-14-8111 NSC 11/02/00 VA 473GB 000

2 EASPATIENT,ONE 000-77-9111 SC \<50% 10/27/00 VA 473GB 000

3 EASPATIENT,ONE 000-84-3111 SC \<50% 11/02/00 VA 473GB 000

4 EASPATIENT,ONE 000-67-3111 NSC 11/02/00 Vet 473GB 000

5 EASPATIENT,ONE 000-46-9111 NSC 11/02/00 Vet 473GB 000

6 EASPATIENT,ONE 000-77-4111 NSC 11/02/00 VA 473GB 000

7 EASPATIENT,ONE 000-78-5111 NSC 10/27/00 VA 473GB 000

8 EASPATIENT,ONE 000-54-8111 SC 50-100% 11/02/00 VA 473GB 000

9 EASPATIENT,ONE 000-45-6789 NSC 11/12/00 Vet 473GB 000

Select an Application to view.

EZ 1010EZ Processing

Select Action: Quit// <u>EZ=9</u> 1010EZ Processing

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

This brings up the data comparison screens for Application \#000.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: PRINTED,PENDING SIG

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN+ Enter ?? for more actions

RZ Reset to New VZ Verify Signature

PZ Print 1010EZ IZ Inactivate 1010EZ

Select Action: Next Screen//

To continue with our example, the enrollment clerk notices on the paper VA Form 10-10EZ that the veteran has changed data in question block 10. Religion. Ms. Smith crossed out her previous answer of BAPTIST and wrote in PRESBYTERIAN. To make this same change on the electronic VA Form 10-10EZ, the enrollment clerk must first place the application in the Signed status. The enrollment clerk will type VZ at the prompt.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: PRINTED,PENDING SIG

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN+ Enter ?? for more actions

RZ Reset to New VZ Verify Signature

PZ Print 1010EZ IZ Inactivate 1010EZ

Select Action: Next Screen// <u>VZ</u> Verify Signature

Applicant signature is verified...

Please wait while processing...

After execution of the VZ function, the application's status changes from Printed, Pending Signature to Signed, as shown below. Now, the Update Field (UF) action can be seen in the command section of the List Manager screen and the Inactivate 1010EZ (IZ) action is no longer available.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: SIGNED

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN+ Enter ?? for more actions

PZ Print 1010EZ UF Update Field FZ File 1010EZ

Select Action: Next Screen//

The enrollment clerk can now select the Update Field (UF) action if necessary to update any 1010EZ data element that may have been manually edited by the applicant. This may occur when a printed VA Form 10-10EZ is sent to the veteran for signature, and the veteran decides to change certain information or to fill-in missing information as requested by the enrollment clerk.

In this case, the enrollment clerk specifies command UF=12 in order to update the religion data element appearing on Line 12 of the List Manager screen. The UF command initiates a FileMan edit dialog, and the enrollment clerk may select a new religion from the valid selections.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: SIGNED

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN+ Enter ?? for more actions

PZ Print 1010EZ UF Update Field FZ File 1010EZ

Select Action: Next Screen// UF=12 Update Field

RELIGION: ??

Choose from:

ADVENTIST 9

ASSEMBLY OF GOD 10

BAPTIST 3

BRETHREN 11

BUDDHIST 31

CATHOLIC 0

CHRISTIAN SCIENTIST 12

CHURCH OF CHRIST 13

CHURCH OF GOD 14

DISCIPLES OF CHRIST 15

EASTERN ORTHODOX 2

EPISCOPALIAN 8

EVANGELICAL COVENANT 16

FRIENDS 17

ISLAM 20

JEHOVAH'S WITNESS 18

JEWISH 1

LATTER-DAY SAINTS 19

LUTHERAN 5

^

RELIGION: 14 CHURCH OF GOD 14

The next screen displays the updated data element.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: SIGNED

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion CHURCH OF GOD

13 Place of Birth City MYTOWN+ Enter ?? for more actions

PZ Print 1010EZ UF Update Field FZ File 1010EZ

Select Action: Next Screen//

> *<u>Note</u>*

> Once the signature has been verified with the Verify Signature (VZ) command, the application is in a Signed status. The enrollment clerk can then update (i.e., directly edit) a data element on the VA Form 10-10EZ through the Update Field (UF) action.

> The reason for not allowing the Update Field (UF) for an application in the Printed, Pending Signature status is to prevent inadvertent changes to 10-10EZ data. An application in the Printed, Pending Signature is assumed to have been mailed to the veteran for signature. Changes should not be made to the data or to the form while awaiting receipt of the signed VA Form 10-10EZ.

## Filed 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Filing 1010EZ Data into VISTA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After receipt of a signed form has been verified, the enrollment clerk can file the data into the V*IST*A patient database by selecting the File 1010EZ (FZ) action at the Select Action: prompt, as shown below. By doing so, the application's status is set to Filed.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: SIGNED

Applicant: EASPATIENT,ONE Date Rec'd: 11/12/2000

Web ID \#: 00000-338900-2000 Vet Sending Signed Form?: YES

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion CHURCH OF GOD

13 Place of Birth City MYTOWN+ Enter ?? for more actions

PZ Print 1010EZ UF Update Field FZ File 1010EZ

Select Action: Quit// <u>FZ</u> File 1010EZ

Requested Start Time: NOW// (NOV 09, 2000@21:02:17)

10-10EZ data is being filed as a background job.

Task \#: 9280

Enter RETURN to continue or '^' to exit:

The actual process of filing data to the patient database can be rather lengthy. The filing process is tasked as a background job.

When the File 1010EZ (FZ) action is performed, processing of the electronic VA Form 10-10EZ is complete. The data comparison screen is closed and the enrollment clerk is returned to the application selection screen. If the enrollment clerk needs to view this VA Form 10-10EZ again, it may be selected from the list of Filed applications for up to 30 days after filing. The entire VA Form 10-10EZ remains in the 1010EZ HOLDING file (#712), but can only be viewed by using the 10-10EZ Quick Lookup menu option.

Once Filed, the majority of the 10-10EZ data is available for normal patient processing within VISTA (e.g., registration, means testing, and enrollment) and can be viewed onscreen. After the majority of the 10-10EZ data is Filed, the electronic VA Form 10-10EZ application can be printed, but cannot be processed further. Should the enrollment clerk need to make any further updates, s/he can do so via the appropriate V*IST*A Registration menu option.

There is a subset of 10-10EZ data that is filed into the V*IST*A patient database, but is not accessible via any V*IST*A screen interface. The following table outlines the specific 10-10EZ data that is filed and stored in V*IST*A, but cannot be accessed for any further updates.

| 10-10EZ Data Element Name                 | Section – Item \# on VA Form 10-10EZ | Displayed on VISTA screens? |
|-------------------------------------------|--------------------------------------|-----------------------------|
| MEDICARE CLAIM NUMBER                     | II – 9                               | NO                          |
| DID YOU SERVE IN COMBAT AFTER 11/11/1998? | IV – 2C                              | NO                          |

## Data Elements Not Filed 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain 10-10EZ data elements cannot be filed in the patient database. There are three possible reasons why filing is not done for a given data element:

1.  Filing of the data element cannot be done without initiating further patient processing (e.g., full Registration and/or Enrollment).
2.  A storage location for the data element does not exist in the current patient database.
3.  Filing of the data element cannot be done because other data is required that is not collected on the VA Form 10-10EZ.

The following table outlines the 10-10EZ data elements that are *not* filed in the V*IST*A patient database, and the corresponding reason number from the list above.

| 10-10EZ Data Element Name                                                | Section – Item \# on VA Form 10-10EZ | Reason for not filing |
|--------------------------------------------------------------------------|--------------------------------------|-----------------------|
| VETERAN NAME                                                             | I - 1                                | 1                     |
| SOCIAL SECURITY NUMBER                                                   | I - 7                                | 1                     |
| DATE OF BIRTH                                                            | I - 9                                | 1                     |
| TYPE OF BENEFIT(S) APPLYING FOR                                          | I - 12                               | 1                     |
| WHICH VA MEDICAL CENTER OR OUTPATIENT CLINIC DO YOU PREFER?              | I - 13                               | 1                     |
| ARE YOU A PURPLE HEART AWARD RECIPIENT?                                  | IV – 2A                              | 3                     |
| DID YOU RECEIVE NOSE AND THROAT RADIUM TREATMENTS WHILE IN THE MILITARY? | IV-2H                                | 3                     |
| DO YOU HAVE A SPINAL CORD INJURY?                                        | IV-I                                 | 1                     |

Since these data items cannot be filed into the patient database, they are not available to the enrollment clerk for the Accept Field (AF) or to the Update Field (UF) actions. If any one of these fields is selected for the AF or UF actions, the screen will display an informational message indicating that the action cannot be completed.

### Validity Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the filing process, the system employs FileMan validity checks. Any data element that does not pass the validity checks will not be filed into the patient record, even though the VA Form 10-10EZ itself indicates a status of Filed.

For example, if the enrollment clerk decides not to accept the applicant’s employment status data element, but does accept the employer name, employer address and employer telephone number. After the FZ action is completed, the enrollment clerk will find that none of the employer data was filed with the patient record. The FileMan validity checks will not allow employer data without an employment status. In other words, data cannot be filed into the patient record through the 10-10EZ module that would not have been accepted through V*IST*A Registration.

The Registration menu options (e.g., *Register a Patient*, *Load/Edit Patient Data*) operate interactively and give the user immediate feedback on invalid data. The File 1010EZ (FZ) action results in an update to the patient record that occurs as a queued background job. Therefore, the user who filed the data is provided with an informational message concerning any validity checks that produced errors and prevented update of the patient record. The following is an example message:

Subj: EAS 1010EZ Error Report for APP \#000 \[#3249\] 27 Mar 01 17:17

From: POSTMASTER In 'IN' basket. Page 1

------------------------------------------------------------------

Errors were returned by the FileMan validator when filing 1010EZ

data for --

Applicant: EASPATIENT,ONE

Application \#: 120

Filing Date: MAR 27, 2001

1010EZ data for APPLICANT was not filed to

Field \#.117 of File \#2 because:

The value 'BUXBY' for field COUNTY in file PATIENT is not

valid.

1010EZ data for APPLICANT was not filed to

Field \#.07 of File \#408.22 because:

The value '0' for field AMOUNT CONTRIBUTED TO SPOUSE in file

INCOME RELATION is not valid.

1010EZ data for CHILD \#3 was not filed to

Field \#.09 of File \#408.13 because:

The value '777777777' for field SOCIAL SECURITY NUMBER in file

INCOME PERSON is not valid.

The enrollment clerk may wish to follow-up immediately on this informational message by correcting the data through the Load/Edit Patient Data menu option*.* In other cases, it may be sufficient to edit the data during normal registration, enrollment and/or means testing.

## Inactivated 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Closing an Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-version-1-user-manual/008.png)Any time prior to verifying the signature of an application, an enrollment clerk may determine that a VA Form 10-10EZ application cannot be processed further. One circumstance may be that the applicant did not return a signed application to the facility in the maximum 60-day time period allotted. Changing the status of the electronic VA Form 10-10EZ to Inactivated allows the application to be viewed at any time if needed, but it will not be available for normal application processing. Note, however, that an inactivated application will remain viewable for up to 30 days after inactivation. The entire VA Form 10-10EZ application remains in the 1010EZ HOLDING File (#712), and its basic information can be viewed only through using the 10-10EZ Quick Lookup menu option.

In the screen below, the enrollment clerk enters Inactivate 1010EZ (IZ) at the Select Action: prompt.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/14/2000

Web ID \#: 00000-897880-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

-------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion CHURCH OF GOD

13 Place of Birth City MYTOWN+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// IZ Inactivate 1010EZ

Application has been closed/inactivated...

Please wait while processing...

When the application is viewed again, its processing status is Inactivated, all accepted fields are reset to non-accepted, any updated data elements have been replaced with original data, and the linkage to the site’s patient database has been removed.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: INACTIVATED

Applicant: EASPATIENT,ONE Date Rec'd: 11/14/2000

Web ID \#: 00000-897880-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789

10 Claim \# 00000000

11 DOB 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN

+ Enter ?? for more actions

QZ Quit

Select Action: Next Screen//

> *<u>Note</u>*

> An application cannot be inactivated once the Verify Signature (VZ) action has been performed. An application that is Inactivated cannot be processed further. If it is determined that the application should be processed, then all 10-10EZ data would need to be re-entered at the Online VA Form 10-10EZ web site as a new application.

# Other 1010EZ Menu Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## 10-10EZ Quick Lookup \[EAS EZ QUICK LOOKUP\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As indicated in previous sections, enrollment coordinators who need to review 10-10EZ data for those applications already dropped from Filed or Inactivated lists, may do so through the 10-10EZ Quick Lookup menu option. At the Select 10-10EZ Menu Option: prompt, select QL.

Select 10-10EZ Menu Option: <u>?</u>

QL 10-10EZ Quick Lookup

EZ Electronic 10-10EZ Processing

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select 10-10EZ Menu Option: <u>QL</u> 10-10EZ Quick Lookup

When prompted, the enrollment coordinator can enter any one of the following types of information.

10-10EZ Application Quick Lookup --

At the prompt, you may enter any one of the following:

\(1\) Application ID

Example: 120

\(2\) Web Submission ID

Example: 0000-122010-2000

Hyphens must appear just as received from

the On-Line 1010-EZ application.

\(3\) Applicant Name

Examples: EASPATIENT,ONE

EASPATIENT,O

No space between last and first name.

\(4\) Applicant SSN

Example: 000-12-0000

Must be entered as nnn-nn-nnnn.

Or enter "^" to exit.

Select 1010EZ HOLDING APPLICATION \#: 000 *This is the Application \#.*

At the next screen, the enrollment clerk will notice that the application Status is highlighted.

App \#: 000 Web ID: 0000-122010-2000

To: 473GB Date Rec'd: OCT 20, 2000

Status: FILED

Applicant: EASPATIENT,ONE SSN: 000-12-0000 DOB: 03/03/1948

Vet Type: NSC Veteran new to Vista?: NO

Financial Disclosure: YES Expect copy from veteran?: YES

Review start date: OCT 27,2000 Print date:

Sign date: NOV 10,2000 File date: NOV 10,2000

Inactivate date:

Services Requested: outpatient visits and prescriptions

Appt. Requested: NO

e-mail Address: jclover@aol.com

Enter RETURN to continue or '^' to exit: *Screen pauses*

If the enrollment clerk enters ^, the main menu will display. If the enrollment clerk hits the Enter key, the second screen of information will appear.

App \#: 000 Web ID: 0000-122010-2000

Status: FILED

Applicant: EASPATIENT,ONE

Comments –-

This is comment Line 1.

This is comment Line 2.

This is comment Line 3.

Enter RETURN to continue or '^' to exit: *The screen pauses*

The enrollment clerk is returned to the Select prompt and may query another application. When the enrollment clerk enters ^ at this prompt, the menu displays.

Select 1010EZ HOLDING APPLICATION \#: <u>^</u>

Select 10-10EZ Menu Option: <u>?</u>

QL 10-10EZ Quick Lookup

EZ ELECTRONIC 10-10EZ PROCESSING

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select 10-10EZ Menu Option:

As explained in the opening screen, other ways to lookup an application are by using the web submission ID, applicant name, or applicant SSN. The applicant name method is the only one of the four lookup methods that uses alphabetic characters. But if web submission ID or applicant SSN methods are used, they must be entered exactly as they appear on the VA Form 10-10EZ, i.e., exactly as provided by the On-Line VA Form 10-10EZ application.

An applicant SSN must be entered as nnn-nn-nnnn. Likewise, the Web Submission ID must be entered as all numeric with hyphens inserted as needed.

Select 1010EZ HOLDING APPLICATION \#: <u>000121812001</u> ??

Select 1010EZ HOLDING APPLICATION \#: <u>000-12181-2001</u> 132

App \#: 000 Web ID: 000-12181-2001

To: Date Rec'd: FEB 28, 2001

Status: IN REVIEW

Applicant: EASPATIENT,ONE SSN: 000-44-5555 DOB: 01/14/1957

Vet Type: SC 50-100% Veteran new to Vista?: YES

Financial Disclosure: NO Expect copy from veteran?: YES

Review start date: FEB 28,2001 Print date:

Sign date: File date:

Inactivate date:

Services Requested: testing

Appt. Requested: NO

e-mail Address:

Enter RETURN to continue or '^' to exit: ^

Entering a partial number is also acceptable, such as 000-12. Since this could possibly be the beginning of an applicant SSN, as well as a web submission ID number, the user may need to select one of several matches.

Select 10-10EZ Menu Option: QL 10-10EZ Quick Lookup

10-10EZ Application Quick Lookup --

At the prompt, you may enter any one of the following:

\(1\) Application ID

Example: 000

\(2\) Web Submission ID

Example: 0000-15222-2001

Hyphens must appear just as received from

the On-Line 1010-EZ application.

\(3\) Applicant Name

Examples: EASPATIENT,ONE

EASPATIENT,O

No space between last and first name.

\(4\) Applicant SSN

Example: 000-22-3333

Must be entered as nnn-nn-nnnn.

Or enter "^" to exit.

Select 1010EZ HOLDING APPLICATION \#: <u>000-12</u>

1 000-12-7677&03/21/1930 000 *This is an SSN match*

2 000-12181-2001 000 *This is the Web Submission ID match*

CHOOSE 1-2:

## Remove Signature Verification \[EAS EZ REMOVE SIGNATURE\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the Verify Signature (VZ) action is performed on the 1010EZ application data, it must be filed into the patient database. It is no longer possible to break the linkage to the PATIENT File (#2) (i.e., Reset to New) or to discard the application (i.e., Inactivate 1010EZ) through the normal List Manager processing tool.

However, a separate menu option has been provided to allow enrollment staff to remove signature verification. The Enrollment Coordinator at each facility can decide how this menu option should be used, and if local option locking should be enforced to prevent wider distribution. (Menu option locking should be discussed with IRM support staff at the local facility.)

Signature verification may be removed only on those 1010EZ applications which are in a status of Signed, and which have not yet been Filed to the patient database.

In the example, user responses are bolded and underlined:

Select 10-10EZ Menu Option: <u>?</u>

EZ Electronic 10-10EZ Processing

QL 10-10EZ Quick Lookup

RS Remove Signature Verification

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select 10-10EZ Menu Option: <u>RS</u> Remove Signature Verification

Lookup and selection for Signature Verification Removal

is by Application \# only.

Only Applications with a Signature Verification Date, but no

Filing Date may be selected.

Select 1010EZ HOLDING APPLICATION \#: <u>?</u>

Answer with 1010EZ HOLDING NUMBER, or APPLICATION \#

Do you want the entire 1010EZ HOLDING List? Y (Yes)

Choose from:

000 000

000 000

Select 1010EZ HOLDING APPLICATION \#: <u>000</u>

Are you sure Signature Verification should be removed? (Y/N): <u>YES</u>

One moment please...

Signature Verification removed...

Application \#000 STATUS -- Printed, Pending Signature

The record in File \#712 for Application \#000 will contain the date and user identity associated with the signature verification removal.

# Help, Hints, & Frequently Asked Questions (FAQs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Help 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 1010EZ module contains two Help features. A system of Help Frames is tied to the opening prompt of the Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\] menu option.

In the following example, user responses are bolded and underlined:

EZ Electronic 10-10EZ Processing

QL 10-10EZ Quick Lookup

RS Remove Signature Verification

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select 10-10EZ Menu Option: <u>EZ</u> Electronic 10-10EZ Processing

10-10EZ Application Processing --

Select one of the following:

1 New

2 In Review

3 Printed, Pending Signature

4 Signed

5 Filed

6 Inactivated

Select Applications to View: <u>??</u>

Enter RETURN to continue or '^' to exit: <u>\<Enter\></u>

10-10EZ PROCESSING

There are six Processing Status categories used to organize interaction

with the 10-10EZ module:

NEWIN REVIEWPRINTED, PENDING SIGNATURESIGNEDFILEDINACTIVATED

A given Application can be in only one Processing Status at any point

in time.

Basic information about a VA Form 10-10EZ Application, including its

current Processing Status, can be obtained by using the 1010EZ

Quick Lookup option on the main 10-10EZ Menu.

Further information is also available on the initial List Manager

display screen.

Select HELP SYSTEM action or \<return\>:

The Help Frames can only be entered using the double question mark in response to the initial Electronic 10-10EZ Processing prompt.

> Select Applications to View: <u>??</u>

Within the Kernel Help Frame system, the enrollment clerk can type-in any term appearing in highlighted text (i.e., reverse video) at the

> Select HELP SYSTEM action or \<return\>:

prompt for additional Help Frame help. In the example above, the terms “NEW”, “IN REVIEW”, “PRINTED”, “SIGNED”, “FILED”, “INACTIVATED”, “Quick Lookup”, or “screen” could be used to link to further Help Frames.

In addition to the Help Frames, help is provided within the List Manager presentation screens. The help returned to the user within List Manager pertains to the actions available at the bottom of the List Manager screen.

10-10EZ Processing Nov 09, 2000 13:33:54 Page: 1 of 9

Application \#: 000 (473GB) Status: IN REVIEW

Applicant: EASPATIENT,ONE Date Rec'd: 11/14/2000

Web ID \#: 00000-897880-2000 Vet Sending Signed Form?: NO

Data Item 10-10EZ Data VistA Data

------------------------------------------------------------------------------

1 Applying for Health YES

2 Facility Applying To YOUR VAMC

3 Applicant Name EASPATIENT,ONE EASPATIENT,ONE

4 Mother’s Maiden Name MAIDEN, ONE

5 Sex FEMALE FEMALE

6 Span/Hisp/Latino? NO (S)

7 Black/African Am.? YES (S)

8 Asian? YES (S)

9 SSN 000-45-6789 000456789

10 Claim \# 00000000

11 DOB 04/09/1967 04/09/1967

12 Religion BAPTIST

13 Place of Birth City MYTOWN+ Enter ?? for more actions

AF Accept Field RZ Reset to New UF Update Field

AZ Accept All PZ Print 1010EZ IZ Inactivate 1010EZ

CZ Clear All VZ Verify Signature

Select Action: Next Screen// <u>??</u>

AF Accept Field --\> Enter AF=n to act on the field shown in Line \#n.

OR

AF Accept Field --\> Enter AF to act on multiple fields.

At the next prompt enter line numbers using '-' and/or ',' --

Select Line Item(s): (1-12): 5-9,11

'Accept' means the 10-10EZ data element is 'accepted' for later filing

into the VistA Patient database when the File 1010EZ action is performed.

Using this action on a previously accepted data element, removes the

'accepted' indicator.

AZ Accept All

All 10-10EZ data element are 'accepted' for later filing into

the VistA Patient database.

UF Update Field --\> Enter UF=n to act on the field shown in Line \#n.

Only one line number can be selected within the Update Field action.

The 10-10EZ data element on Line \#n can be overwritten by the user for

later filing into VistA.

This action should be used to enter the Applicant's hand-written

changes to the signed VA Form 10-10EZ.

Enter RETURN to continue or '^' to exit: <u>\<Enter\></u>

CZ Clear All

The 'accepted' indicator is removed from any fields previously

'accepted'.

RZ Reset to New

The Application is returned to the 'New' processing status.

It can be re-matched to the VistA database.

PZ Print 1010EZ

Once the VA Form 10-10EZ is Printed, actions of Accept Field, Accept All,

Clear All, and Update Field can no longer be used.

The VA Form 10-10EZ is printed using all 'accepted' data.

VistA Patient data is used for any fields not 'accepted'.

Printing must be queued to a valid print device.

Enter RETURN to continue or '^' to exit: <u>\<Enter\></u>

VZ Verify Signature

The user verifies that the Applicant's signature appears on a

printed VA Form 10-10EZ.

IZ Inactivate 1010EZ

Once the Application is inactivated, it will no longer be available

for processing.

Use this action only if the Application is deemed invalid or is being

replaced by a new Application.

Enter RETURN to continue or '^' to exit: <u>\<Enter\></u>

The following actions are also available:

\+ Next Screen \< Shift View to Left PS Print Screen

\- Previous Screen FS First Screen PL Print List

UP Up a Line LS Last Screen SL Search List

DN Down a Line GO Go to Page ADPL Auto Display(On/Off)

\> Shift View to Right RD Re Display Screen Q Quit

Enter RETURN to continue or '^' to exit:

Notice in the example above that the enrollment clerk is viewing an application with the status of In Review. Therefore the response to the help request (i.e., the double question mark), describes those actions that are valid for an In Review application.

After guidance is provided for actions specific to the 1010EZ module, information is displayed that pertains to general List Manager action commands and cursor movement.

## FAQs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*What happens when the facility receives an out of area request for services?*

The facility should attempt to verify where the veteran prefers to receive medical treatment. This could be accomplished through the normal processing of the VA Form 10-10EZ, i.e., the veteran can verify the location when he/she reviews the printed form.

*What happens when a facility receives a request that is not a true enrollment, such as a request for payment of a bill?*

The facility should route any non-related correspondence to the most appropriate service for resolution, as with any request for services.

*What should the facility do when the Application for Health Care is obviously fictitious, e.g., from Mickey Mouse?*

The facility should follow local procedures for any request that cannot be processed, to include marking the transmission as Inactivated.

*When I print the VA Form 10-10EZ application using the VistA PZ function, why does a data value from the previous V<span class="smallcaps">ist</span>A record for the veteran appear when no value existed in the form submitted by the veteran?*

During data comparison and acceptance, blank values in the application are not automatically accepted if data for that veteran already exists in V*IST*A. If the user does not use the Accept Field (AF) function to accept the application's blank data field, then the value for that field already in V*IST*A gets pulled into the new application.

*Can facilities correspond directly with veterans via email?*

Facilities may correspond directly with veterans. The VA Form 10-10EZ does provide the veteran with the opportunity to supply an email address. Remember, any correspondence to veterans should be general in nature, and must not contain any personal information, information subject to the Privacy Act, or any other information, which could be sensitive in nature. Facilities should invite veterans to call or visit to discuss or inquire about anything personal in nature.

*How would a veteran or the facility know when a transmission did not take place?*

Veterans are supplied with a transaction ID number (Submit ID \#) if and when a transmission takes place. At that time, the veteran is instructed to write this number down and safeguard in case of a missing form. Veterans are also instructed to contact the facility enrollment coordinator for questions or concerns with the VA Form 10-10EZ. If a veteran calls and indicates that a VA Form 10-10EZ was sent, and has a transaction ID number handy, but the facility cannot locate the transmitted form, the facility can contact the HEC at (404) 235-1295.

*  
Once the Purple Heart software has been installed, will the response to the Purple Heart prompt from the web remain non-uploadable or will it change to one that we will have to nonselect?*

The Purple Heart project development team has stipulated that VA Form 10-10EZ application not file any Purple Heart data. The Purple Heart data element on the 10-10EZ screen cannot be accepted or updated by the user. That data will have to be manually entered during the registration process using the Registration application.

## Overall Process Schematic 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!  
ALL NEW ONLINE VA-FORM 10-10EZs ARE TRANSMITTED TO THE ENROLLMENT SYSTEM AND THIS OPTION IS NO LONGER USED TO PROCESS VA FORM 10-10EZ.

## EAS\*1.0\*190 in Host File DG_53_P993.KID disables the Link to Patient File (LZ) action in the Electronic 10-10EZ Processing option. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## # Appendix A-Sample Letter for VA Form 10-10EZ Mailing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the VA Form 10-10EZ must be sent to the veteran for signature, the enrollment clerk should attach a letter similar to this one. The letter should instruct the veteran to carefully review the information on the form, make any needed changes, and sign and mail/fax the form back to the medical facility. The letter should include any deadlines and should inform the veteran that the facility may dispose of the original application if the veteran does not return the signed form within the specified time period. Facilities should modify this letter for second mailings of the VA Form 10-10EZ to indicate a second attempt at trying to obtain a signed VA Form 10-10EZ from the veteran.

![](eas-version-1-user-manual/009.png)

## # Appendix B-Sample VA MailMan Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a partial sample of a VA MailMan message that gets sent to members of the G.1010EZ… mail group when a veteran submits a completed VA Form 10-10EZ. The appropriate VAMC staff must use the Load/Edit Patient Data menu option on the PIMS Registration Menu to enter data for all new data elements (fields displaying a description in upper case, enclosed in parentheses).

Subj: 999 : VA ToPrint: EASPATIENT,ONE : SID 5618-11204-2004 \[#4294279\]

Tue, 20 Apr 2004 11:32:38 -0400 222 lines

From: \<G.1010EZADMIN@FORUM.VA.GOV\> In ‘IN’ basket. Page 1

--------------------------------------------------------------------------------

SECTION I - VISTA AUTOMATION

2.1^EASPATIENT^

2.2^ONE^

2.3^TWO^

2.4^JR^ (SUFFIX)

1B.^Bay Pines Test Lab OIFO^

1A.1^Y^

1A.2^Y^

1A.3^^

1A.4^^

3.^OTHERNAMEUSED^

3A.^ABCPATIENT^ (MOM'S MAIDEN)

4.^M^

4A.^N^ (ETHNICITY-'HISPANIC OR LATINO')

4B.^^ (RACE-- 'AMERICAN INDIAN OR ALASKA NATIVE')

4C.^^ (RACE--'BLACK OR AFRICAN AMERICAN')

4D.^^ (RACE--'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER')

4E.^^ (RACE--'ASIAN')

4F.^Y^ (RACE--'WHITE')

4G.^^ (RACE--UNKNOWN BY PATIENT)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                              |                                                                                                                                                                                           |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA Form 10-10EZ                          | A VA form used by veterans to apply for VHA health benefits                                                                                                                               |
| 10-10EZ Enrollment Application Processor | A menu option that allows local V*IST*A systems to electronically process applications for enrollment and healthcare benefits filled out by veterans via a web-based application. |
| EAS                                      | Enrollment Application System                                                                                                                                                             |
| ESR                                      | Enrollment System Redesign                                                                                                                                                                |
| EVC R2                                   | Enrollment VistA Changes Release Two                                                                                                                                                      |
| VA                                       | Department of Veterans Affairs                                                                                                                                                            |
| VHA                                      | Veterans Health Administration                                                                                                                                                            |
| V*IST*A                              | VHA Information Systems and Technology Architecture                                                                                                                                       |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1
1010EZ Processing via List Manager 7
10-10EZ Quick Lookup \[EAS EZ QUICK LOOKUP\] 61
A
Accept All 33
Accept Field 36
Addresses
Confidential 2
foreign 2
Mailing 2
Temporary 2
After Receiving a Signed Application 47
Appendix B-Sample VA MailMan Message 78
C
Clear All 35
Closing an Application 58
Country
field 2
D
Data Comparison – Existing Patient 31
Data Comparison – New Patient 32
Data Elements Not Filed 56
E
Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\] 4
Existing Patient 28
F
*FAQs* 70
Feb 2005 Data Format 2
Filed 54
Filing 1010EZ Data into VistA 54
G
Glossary 79
H
*Help* 65
Help, Hints, & Frequently Asked Questions (FAQs) 65
I
*In Review* 31
Inactivated 58
Introduction 1
L
Linking Applicant to PATIENT File (#2) 21
N
New Patient 25
O
Other 1010EZ Options 61
*Overall Process Schematic* 73
P
Printed, Pending Signature 44
*Process Overview* 1
Processing a VA Form 10-10EZ Application 13
R
*Remove Signature Verification \[EAS EZ REMOVE SIGNATURE\]* 64
Reset to New 41
Revision History iii
S
Sample Letter for VA Form 10-10EZ Mailing 76
Signed 47
Special Cases of Data Acceptance 39
U
Update Field 40
Using Action Commands 33
Using the Software 4
V
VA Form 1010EZ Application Status 10
Validity Checks 57
W
What to do with a signed form 13
What to do without a signed form 17
