---
title: PXRM*2*35 Life Sustaining Treatment Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Life Sustaining Treatment
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*35
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - strong
  - blockquote
  - life
  - treatment
  - sustaining
  - orders
  - class
  - order
  - table
  - template
page_count: 0
word_count: 10791
section_count: 11
table_count: 6
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_35_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_35_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/001.png)

> Life-Sustaining Treatment Reminder Dialog

> PXRM\*2.0\*35

> INSTALLATION and SETUP GUIDE

> August 25, 2016

> Product Development Department of Veterans Affairs

1.  Contents
2.  [Introduction 4](#introduction)
3.  [Pre-Installation 6](#pre-installation)
4.  [Installation 6](#installation)
5.  [Pre- or Post-Installation 9](#pre--or-post-installation)
    1.  [VistA/CPRS Preparation 9](#vistacprs-preparation)
    2.  [Life-Sustaining Treatment Display Group Creation in VistA FileMan 9](#life-sustaining-treatment-display-group-creation-in-vista-fileman)
        1.  [Initial Display Group Creation 10](#initial-display-group-creation)
        2.  [Add Display Group to “ALL SERVICES” 10](#add-display-group-to-all-services)
        3.  [Double Check – FileMan Inquiry (FileMan Menu) 10](#double-check-fileman-inquiry-fileman-menu)
    3.  [VistA CPRS Manager “Edit the Parameter Definition Entry” 11](#vista-cprs-manager-edit-the-parameter-definition-entry)
        1.  [Go Into CPRS Manager Menu 11](#go-into-cprs-manager-menu-1)
        2.  [Follow the Menu Path 12](#follow-the-menu-path)
        3.  [Edit the ORWOR CATEGORY SEQUENCE Parameter Definition 12](#edit-the-orwor-category-sequence-parameter-definition-1)
        4.  [Double Check the ORWOR CATEGORY SEQUENCE Parameter Definition 13](#double-check-the-orwor-category-sequence-parameter-definition)
    4.  [VistA Orders Set-Up 15](#vista-orders-set-up)
        1.  [Go into CPRS Configuration (Clinical Coordinator) Menu and Follow the Menu Path: CP \> MM \> GO (Note: Local menu paths may vary.) 15](#_bookmark15)
        2.  [Build new Life-Sustaining Treatment Generic Orders 17](#build-new-life-sustaining-treatment-generic-orders)
    5.  [Build an LST Menu and Place LST Orders on the LST Menu 51](#build-an-lst-menu-and-place-lst-orders-on-the-lst-menu)
        1.  [Go Into CPRS Configuration (Clinical Coordinator) Menu 53](#_bookmark18)
        2.  [Follow the Menu Path: Order Menu Management (MM) \> Enter/Edit Order Menus (MN) 53](#_bookmark19)
        3.  [Build the new LST Orders Menu 54](#_bookmark20)
        4.  [Add the New LST Orders Menu to Other Order Menus 60](#add-the-new-lst-orders-menu-to-other-order-menus)
    6.  [Editing Auto-Discontinue Rules to Make LST Orders Durable 61](#_bookmark22)
        1.  [Go Into CPRS Configuration (Clinical Coordinator) Menu 61](#go-into-cprs-configuration-clinical-coordinator-menu-3)
        2.  [Follow the Menu Path: DO \> DO \> Auto-DC Rules 62](#_bookmark24)
        3.  [Add/Edit Each Event 63](#_bookmark25)
        4.  [Double Check to make sure the action held 64](#_bookmark26)
    7.  [Set Up “NO COPY” for Orders in the “Life-Sustaining Treatment“ Display Group 64](#_bookmark27)
        1.  [Go Into CPRS Configuration (Clinical Coordinator) Menu and Follow the Menu Path: DO \> EP \> Exclude display groups from copy 65](#_bookmark28)
6.  [Post-Installation Setup Instructions 67](#post-installation-setup-instructions)
    1.  [Link the Life-Sustaining Treatment Orders or Orders Menu to the VA-LIFE-SUSTINING TREATMENT Reminder Dialog 67](#link-the-life-sustaining-treatment-orders-or-orders-menu-to-the-va-life-sustining-treatment-reminder-dialog)
        1.  [Linking Individual LST Orders to the LST Reminder Dialog Template 67](#linking-individual-lst-orders-to-the-lst-reminder-dialog-template)
        2.  [Linking LST Orders Menu and/or a Local Comfort Care Order Set/Consult Order Set to the LST Reminder Dialog Template 70](#linking-lst-orders-menu-andor-a-local-comfort-care-order-setconsult-order-set-to-the-lst-reminder-dialog-template)
    2.  [Set Up the Life-Sustaining Treatment Progress Note Title in the VistA Text Integration Utility (TIU) 72](#set-up-the-life-sustaining-treatment-progress-note-title-in-the-vista-text-integration-utility-tiu)
    3.  [Set Up the Life-Sustaining Treatment Progress Note Document Definition in the VistA Text Integration Utility (TIU) 75](#set-up-the-life-sustaining-treatment-progress-note-document-definition-in-the-vista-text-integration-utility-tiu)
    4.  [Set Up Life-Sustaining Treatment Progress Note Business Rules in TIU 77](#set-up-life-sustaining-treatment-progress-note-business-rules-in-tiu)
    5.  [Activate the Reminder Dialog for TIU Use 78](#activate-the-reminder-dialog-for-tiu-use)
    6.  [Adding the Life-Sustaining Treatment Reminder Dialog Template Into CPRS and Linking It to the Progress Note Title 80](#adding-the-life-sustaining-treatment-reminder-dialog-template-into-cprs-and-linking-it-to-the-progress-note-title)
    7.  [Editing the CPRS “Template Fields” Deployed With the Reminder Dialog 82](#_bookmark38)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
- [Installation](#installation)
- [Pre- or Post-Installation](#pre-or-post-installation)
  - [VistA/CPRS Preparation](#vistacprs-preparation)
  - [Life-Sustaining Treatment Display Group Creation in VistA FileMan](#life-sustaining-treatment-display-group-creation-in-vista-fileman)
    - [Initial Display Group Creation](#initial-display-group-creation)
    - [Add Display Group to “ALL SERVICES”](#add-display-group-to-all-services)
    - [Double Check – FileMan Inquiry (FileMan Menu)](#double-check-fileman-inquiry-fileman-menu)
  - [VistA CPRS Manager “Edit the Parameter Definition Entry”](#vista-cprs-manager-edit-the-parameter-definition-entry)
    - [Go Into CPRS Manager Menu](#go-into-cprs-manager-menu)
    - [Follow the Menu Path](#follow-the-menu-path)
    - [Edit the ORWOR CATEGORY SEQUENCE Parameter Definition](#edit-the-orwor-category-sequence-parameter-definition)
    - [Double Check the ORWOR CATEGORY SEQUENCE Parameter Definition](#double-check-the-orwor-category-sequence-parameter-definition)
  - [VistA Orders Set-Up](#vista-orders-set-up)
    - [Build new Life-Sustaining Treatment Generic Orders](#build-new-life-sustaining-treatment-generic-orders)
    - [Go Into CPRS Configuration (Clinical Coordinator) Menu](#go-into-cprs-configuration-clinical-coordinator-menu)
- [Post-Installation Setup Instructions](#post-installation-setup-instructions)
  - [Link the Life-Sustaining Treatment Orders or Orders Menu to the VA-LIFE-SUSTINING TREATMENT Reminder Dialog](#link-the-life-sustaining-treatment-orders-or-orders-menu-to-the-va-life-sustining-treatment-reminder-dialog)
    - [Linking Individual LST Orders to the LST Reminder Dialog Template](#linking-individual-lst-orders-to-the-lst-reminder-dialog-template)
    - [Linking LST Orders Menu and/or a Local Comfort Care Order Set/Consult Order Set to the LST Reminder Dialog Template](#linking-lst-orders-menu-andor-a-local-comfort-care-order-setconsult-order-set-to-the-lst-reminder-dialog-template)
  - [Set Up the Life-Sustaining Treatment Progress Note Title in the VistA Text Integration Utility (TIU)](#set-up-the-life-sustaining-treatment-progress-note-title-in-the-vista-text-integration-utility-tiu)
  - [Set Up the Life-Sustaining Treatment Progress Note Document Definition in the VistA Text Integration Utility (TIU)](#set-up-the-life-sustaining-treatment-progress-note-document-definition-in-the-vista-text-integration-utility-tiu)
  - [Set Up Life-Sustaining Treatment Progress Note Business Rules in TIU](#set-up-life-sustaining-treatment-progress-note-business-rules-in-tiu)
  - [Activate the Reminder Dialog for TIU Use](#activate-the-reminder-dialog-for-tiu-use)
  - [Adding the Life-Sustaining Treatment Reminder Dialog Template Into CPRS and Linking It to the Progress Note Title](#adding-the-life-sustaining-treatment-reminder-dialog-template-into-cprs-and-linking-it-to-the-progress-note-title)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B - Acronyms](#appendix-b-acronyms)
- [Appendix C – Health Factors and Reminder Dialog Linkage Points](#appendix-c-health-factors-and-reminder-dialog-linkage-points)
- [Appendix D – Life-Sustaining Treatment Orders in CPRS](#appendix-d-life-sustaining-treatment-orders-in-cprs)
- [Appendix E – Life-Sustaining Treatment Reminder Dialog Screenshots](#appendix-e-life-sustaining-treatment-reminder-dialog-screenshots)

#### Patch PXRM\*2.0\*35 releases a new reminder dialog template to the field, without any changes to routines, data dictionaries, or other package functions; it deals with content only. The new reminder dialog template is: VA-LIFE-SUSTAINING TREATMENT.

#### This reminder dialog template will be mandated for use upon release of Veterans Health Administration (VHA) Handbook 1004.03, “Life-Sustaining Treatment Decisions: Eliciting,

#### Documenting and Honoring Patients’ Values, Goals and Preferences.” This Handbook will

#### replace VHA Handbook 1004.3, “Do Not Resuscitate (DNR) Protocols within the Department of Veterans Affairs (VA).” The use of this reminder dialog template, the associated progress note title, and ancillary ordering processes, will introduce a significant practice change for most ordering providers in VHA.

#### Facilities will be required to install and test this template within normal installation timelines as established by OIT. However, the new Handbook will allow 18 months for site implementation of the policy and the associated processes. Clinical Informatics staffs are encouraged to work closely with their local Life-Sustaining Treatment Advisory/Implementation groups to complete post-installation steps in support of facility deployment.

#### The National Center for Ethics in Health Care (NCEHC) is the Program Office with oversight of this template and its associated processes. NCEHC will be available to help facilities meet the timelines to implement the associated practice changes and begin using this template with patients.

#### This patch will only import the reminder dialog template, associated health factors, and multiple CPRS template fields. In order to make this process function as required in VHA Handbook 1004.03, each site that installs this template will also need to complete the listed post- installation actions.

#### Multiple installation steps will be required, and some actions will be optional. These actions should to be accomplished in your VistA/CPRS test account and then transitioned to your live account after successful testing in accordance with your facility’s deployment strategy. These processes are outlined in the following guidance, but an overview is provided here:

#### Pre- or Post-Installation. These actions may be accomplished either before or after installation of the reminder dialog patch

#### Build and assign a new CPRS “orders display group”: Life-Sustaining Treatment

#### Build Life-Sustaining Treatment Generic Orders, using the new orders display group

#### Build and assign a Life-Sustaining Treatment order set menu

#### Add auto-discontinue rules to ensure that the Life-Sustaining Treatment orders DO NOT auto-discontinue upon patient movement or specialty change (e.g. admission, transfer, discharge, change from General Surgery to Neurology, etc.)

#### Add rules to ensure that no option to “copy” these orders is offered when delayed orders are written

#### Post-Installation. These actions may be accomplished only after installation of the reminder dialog patch

#### Build the CWAD progress note title, “Life-Sustaining Treatment”.

#### The local title and print name must be, “Life-Sustaining Treatment”.

#### The title must be linked to the national standard title, “Life-Sustaining Treatment Plan”.

#### Link the VA-LIFE-SUSTAINING TREATMENT reminder dialog template to the progress note title “Life-Sustaining Treatment”.

#### Edit the progress note title’s document definition and business rules.

#### Edit the reminder dialog to automatically launch the new individual generic orders or the new order set and/or local consults and comfort care order sets. (Linking and launching the LST orders from the template is a local option and is not required. However, the ability to launch the orders from the template was highly esteemed and encouraged as a strong practice from all of the *LST demonstration/test sites.*)

#### Create VistA business rules and user classes to restrict the entering of the progress note, “Life-Sustaining Treatment” to personnel as defined in VHA Handbook 1004.03.

#### Create business rules and user classes to restrict the adding of addenda to this progress note by additional personnel to only those persons as defined in VHA Handbook 1004.03.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Required Software for PXRM\*2.0\*35*

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package/Patch</strong></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><strong>Version</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>XU</p>
</blockquote></td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

> *Related Documentation*

| Documentation            | Documentation File name |
|------------------------------|-----------------------------|
| Installation and Setup Guide | PXRM\*2.0\*35_IG.PDF        |

> *Web Sites*

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 38%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td><p>Contains manuals, PowerPoint presentations, and other</p>
<p>information about Clinical Reminders</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td><p>This committee directs the development of new and revised</p>
<p>national reminders</p></td>
</tr>
<tr class="odd">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td>Contains manuals for Clinical Reminders</td>
</tr>
</tbody>
</table>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes.

#### The installation needs to be done by a person with DUZ(0) set to "@."

1.  Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 36%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

2.  Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

3.  Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

> Example

> From the Installation menu, you may elect to use the following options:

4.  Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> a. Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

5.  Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*35 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

> Installation Example

> See Appendix A.

6.  Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

7.  Build File Print

> Use the KIDS Build File Print option to print out the build components.

8.  Post-installation routines

> After successful installation, the following init routines may be deleted:

#### PXRMP35E PXRMP35I

# Pre- or Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA/CPRS Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Since this is a significant practice change, these actions should be well coordinated with all personnel that will be impacted.

#### The pre- or post-installation development of Life-Sustaining Treatment orders is needed in order to support new processes directed in forthcoming policy. These new orders and their associated processes will replace former Do Not Resuscitate (DNR) order processes.

#### Sites may decide to have their providers launch the orders and/or the associated orders menu by associating the orders/orders menu with the Life-Sustaining Treatment reminder dialog. The automatic launching of orders, via completion of the reminder dialog, was seen as a major 

#### advantage by test sites and was evaluated by practitioners as a “highly desirable” option. Alternatively, sites may develop processes that force providers to launch the orders menu separately. However, during usability testing, providers stated very strongly that they would want the orders to auto-populate when they clicked on the associated options within the reminder dialog template (e.g., clicking the option in the template for “DNAR/DNR: Do not

#### attempt CPR” automatically populates the associated, pre-built generic order in the orders tab). Sites will be required to build these specific orders and the associated orders menu, regardless of whether they are associated with the template. Sites are encouraged to associate the orders with the reminder dialog template during installation.

#### Your attention to detail during the building of these orders and the associated processes should make this implementation flow smoothly. Your work will be appreciated by the providers you support.

## Life-Sustaining Treatment Display Group Creation in VistA FileMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The new Life-Sustaining Treatment (LST) display group will help ensure that active LST orders default to the top of the orders tab in CPRS. This will be required in the forthcoming policy.

#### This will not prevent users from customizing the way that orders appear in CPRS, but the default setting will be at the top. This display group will also make it simpler to set “auto- discontinue” rules and “do not copy” rules to make these orders durable and remain in effect until they are manually changed or discontinued. You will need to have “LAYGO” access to accomplish this task. This may require coordination with your local OIT, or they may need to take these actions. It is crucial that this Display Group be built as shown below and in place prior to any attempts to build the associated orders.

#### Using VA FileMan add a New Display Group to file 100.98

#### Summary of actions:

1.  Add a new Display Group (file \#100.98) entry *(you must have LAYGO access to this file!)*

#### Add the new Display Group as a Member to the ALL SERVICES Display Group

#### Double-check! Do a FileMan Inquiry into the Display Group file

#### The following is an example of adding a LIFE-SUSTAINING TREATMENT member to the ALL SERVICES Display Group in VistA:

### Initial Display Group Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add Display Group to “ALL SERVICES”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Double Check – FileMan Inquiry (FileMan Menu)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA CPRS Manager “Edit the Parameter Definition Entry”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### In CPRS Manager, Edit the Parameter Definition Entry

#### Summary of actions:

#### Go into CPRS Manager Menu

#### Follow the following menu path: IR \> XX \> EP

#### Edit the ORWOR CATEGORY SEQUENCE Parameter Definition

#### Double-check!

#### The following example in VistA shows how this is done.

### Go Into CPRS Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Follow the Menu Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

### Edit the ORWOR CATEGORY SEQUENCE Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select General Parameter Tools Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders

####### Category Sequence

> ORWOR CATEGORY SEQUENCE may be set for the following:

> 8 System SYS \[XXX.XXX.VA.GOV\] (Note: This will vary by site.)

> 10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

####### Enter selection: 8 System XXXX.XXXXX (Note: Health Information Specialists/Clinical Application Coordinators may not have access to set this at the “Package” level and may need to set this to the “System” level. The level selected should ensure that all users of the system will be able to see orders assigned to this display group. If selecting the “System” level, some sites may have multiple systems and this setup will need to be set up for sites’ implementation for each system.)

####### Parameters set for 'Package' may be replaced if ORDER ENTRY/RESULTS REPORTING is installed in this account.

> Setting ORWOR CATEGORY SEQUENCE for System: XXX.XXX.VA.GOV

> Select Sequence: ?

### Double Check the ORWOR CATEGORY SEQUENCE Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 14%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>8 System</th>
<th>SYS</th>
<th><blockquote>
<p>[<strong>XXX.XXX.VA.GOV</strong>]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10 Package</td>
<td>PKG</td>
<td><blockquote>
<p>[ORDER ENTRY/RESULTS REPORTING]</p>
</blockquote></td>
</tr>
</tbody>
</table>

## VistA Orders Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The fourteen generic orders listed below should all populate into the Life-Sustaining Treatment display group, which was built in the previous step. Many of these orders are set to auto- populate (e.g., DNAR/DNR, no mechanical ventilation, etc.). Sites should not add orders to the Life-Sustaining Treatment display group unless they are listed below. Use of this standardized terminology will help standardize processes throughout VA. Terms such as “do not intubate” and “modified code status” are no longer authorized for use. <u>The only exception is the facility’s</u>

#### <u>choice in using either “Do Not Resuscitate” (DNR) or “Do Not Attempt Resuscitation”</u> <u>(DNAR) in the “text” that populates into the orders. Either of these two terms/acronyms is</u> <u>acceptable and understood to be interchangeable in the “text” of the order(s) and either may be</u> <u>used within the text of the generic order(s) when they are built</u>. The use of DNR or DNAR in the naming conventions for the orders and the orderable items should reflect what is presented below.

#### Please note that these generic orders do NOT have an associated “stop date/time.” They are designed to be durable and not automatically discontinue.

#### Some site VistA menus may omit some of the steps listed below. If the local menu you use does not show data that is listed below, look a bit further down the menu example and you will likely see where your menu continues the pattern displayed here.

#### In CPRS Configuration (Clinical Coordinator) Menu Create Generic Orders with Associated Orderable Items

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu and follow the menu path: CP \> MM \> GO

#### Build new Life-Sustaining Treatment Generic Orders The following examples in VistA show how this is done:

1.  <span id="_bookmark15" class="anchor"></span>Go into CPRS Configuration (Clinical Coordinator) Menu and Follow the

> Menu Path: CP \> MM \> GO (Note: Local menu paths may vary.)

> AL Allocate OE/RR Security Keys KK Check for Multiple Keys

> DC Edit DC Reasons

> GP GUI Parameters ...

> GA GUI Access - Tabs, RPL MI Miscellaneous Parameters

> NO Notification Mgmt Menu ... OC Order Checking Mgmt Menu ... MM Order Menu Management ...

> LI Patient List Mgmt Menu ... FP Print Formats

> PR Print/Report Parameters ... RE Release/Cancel Delayed Orders US Unsigned orders search

> EX Set Unsigned Orders View on Exit NA Search orders by Nature or Status CM Care Management Menu ...

> DO Event Delayed Orders Menu ... LO Lapsed Orders search

> PM Performance Monitor Report

> Select CPRS Configuration (Clin Coord) \<TEST ACCOUNT\> Option: MM Order Menu Management

> OI Manage orderable items ... PM Enter/edit prompts

> GO Enter/edit generic orders QO Enter/edit quick orders

> QU Edit personal quick orders by user ST Enter/edit order sets

> AC Enter/edit actions

> MN Enter/edit order menus

> AO Assign Primary Order Menu CP Convert protocols

> SR Search/replace components LM List Primary Order Menus

> DS Disable/Enable order dialogs

> CS Review Quick Orders for Inactive ICD9 Codes MR Medication Quick Order Report

> CV Convert IV Inpatient QO to Infusion QO FR IV Additive Frequency Utility

> Select Order Menu Management \<TEST ACCOUNT\> Option: GO Enter/edit generic orders

### Build new Life-Sustaining Treatment Generic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will need to build these orders exactly as displayed in the menu examples below. *(<u>NOTE:</u> <u>The orderable items are built during the building of the order itself. This allows for the</u> <u>addition of the orderable item to the orderable item table associated with the Life-Sustaining</u> <u>Treatment display group, which most Clinical Application Coordinators will not have direct</u> <u>access to for editing/viewing purposes</u>.)* These orders do NOT have a prompt for a “stop date/time,” which helps make them durable. Please ensure that you edit the “Display Text” as shown, so that the way the orders display on menus is consistent no matter which menu they are associated with.

#### Note: Where the acronym DNAR/DNR is shown as text that comes into the order, sites may use either: DNAR/DNR; DNAR; or DNR as locally determined. These are the only three acronyms authorized. Please use the naming conventions as shown for naming orderable items and generic orders. Sites may NOT use “DNI” (Do Not Intubate) and may not build DNI orders.

#### DNAR/DNR - Order Setup

> Select ORDER DIALOG NAME: OR LST DNR

> Are you adding 'OR LST DNR' as a new ORDER DIALOG? No// YES (Yes) DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST DNR - DO NOT RESUSCITATE

> Are you adding LST DNR - DO NOT RESUSCITATE' as a new ORDERABLE ITEMS (the 2466TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST DNR//

> *(Note: In the text string below, sites may use either “DNAR” or “DNR” and don’t have to use both. These acronyms are interchangeable.)* DISPLAY TEXT: DNAR/DNR: Do not attempt CPR in the event of cardiopulmonary arrest

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]==========\< DESCRIPTION \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> ====T=======T=======T=======TT=======T=======T=======T=======T\>====== ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2465// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? YES (Yes) *(This should be blank, so that the orderable item does NOT appear in the actual order on the orders tab in CPRS)*

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 DISPLAY TEXT: LST ORDER: // REQUIRED: YES//

> MULTIPLE VALUED: NO//

> ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

######## (Note: In the text string below, sites may use either “DNAR” or “DNR” and don’t have to use both. These acronyms are interchangeable.)

> ==\[ WRAP DEFAULT WORD-PROCESSING TEXT \>===\[ \<PF1\>H=Help

####### DNAR/DNR: Do not attempt CPR in the event of cardiopulmonary arrest

> ===T=======T=======T=======T=======T=======T=======T=======T=======T POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE:

> WORD-WRAP:

> Select PROMPT: 3

> SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

> HELP MESSAGE: Enter the date/time to begin this order.

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT: S Y=“NOW” *(NOTE: Local VistA setup may require simply entering the word NOW)*

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 2//@

> SURE YOU WANT TO DELETE? YES (Yes) *(This should be blank, so that the item does NOT appear in the order on the orders tab in CPRS)* FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE:

> Select PROMPT:

> Auto-accept this order? YES//

> Do you want to test this dialog now? YES

> Order: LST DNR - DO NOT RESUSCITATE LST ORDER: DNAR/DNR: Do not

> attempt CPR in the event ...

> START DATE/TIME: NOW (6/7/13@09:27)

#### DNAR/DNR Except - Order Setup

> Select ORDER DIALOG NAME: OR LST DNR EXCEPT

> Are you adding 'OR LST DNR' as a new ORDER DIALOG? No// YES (Yes) DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST DNR EXCEPT

> Are you adding 'LST DNR EXCEPT' as a new ORDERABLE ITEMS (the 2466TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST DNR EXCEPT//

> *(Note: In the text string below, sites may use either “DNAR” or “DNR” and don’t have to use both. These acronyms are interchangeable.)* DISPLAY TEXT: LST DNR EXCEPT Replace ... With DISPLAY TEXT: DNAR/DNR

####### with exception: ONLY attempt CPR during the following procedure:

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]==========\< DESCRIPTION \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> ====T=======T=======T=======TT=======T=======T=======T=======T\>======

> ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2465// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? YES (Yes) *(This should be blank, so that the orderable item does NOT appear in the actual order on the orders tab in CPRS)*

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1

####### DISPLAY TEXT: DNAR/DNR with exception: ONLY attempt CPR during the following procedure: //

> REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: NO NO ASK ON ACTION: RCW

####### HELP MESSAGE: Specific limitations on exceptions to DNAR/DNR (Note: After HELP MESSAGE – some local VistA systems skip several

####### prompts and automatically open the box for word-processing. Do NOT add text to the word-processing section for this prompt.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// NO

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

######## (Note: In the text string below, sites may use either “DNAR” or “DNR”.

######## These acronyms are interchangeable.)

####### LEADING TEXT: DNAR/DNR with exception: ONLY attempt CPR during the following procedure:

> TRAILING TEXT:

> START NEW LINE:

> WORD-WRAP: WRAP

> Select PROMPT: 3

> SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

> HELP MESSAGE: Enter the date/time to begin this order.

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT: S Y=“NOW” *(NOTE: Local VistA setup may require simply entering the word NOW)*

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 2//@

> SURE YOU WANT TO DELETE? YES (Yes) *(This should be blank, so that the item does NOT appear in the actual order on the orders tab in CPRS)*

> FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE:

> Select PROMPT:

> Auto-accept this order? NO//

> Do you want to test this dialog now? YES

> ==\[ WRAP \]==\[ INSERT \]=====\< DNAR/DNR EXCEPT \>=====\[ \<PF1\>H=Help \]==== TEST, TEST, TEST

> \<=======T===T=======T=======T=======T=======T=======T=======T\>======

> Order: LST DNR EXCEPT

> DNAR/DNR with exception: ONLY attempt CPR during the following procedure::TEST, TEST, TEST

> START DATE/TIME: NOW (12/16/13@06:24)

#### Do Not Use Life-Sustaining Treatments - Order Setup

> Select ORDER DIALOG NAME: OR LST DO NOT USE LST

> Are you adding 'OR LST DO NOT USE LST' as a new ORDER DIALOG? No// YES (Yes)

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST DO NOT USE LIFE SUSTAINING TREATMENT

> Are you adding 'LST DO NOT USE LIFE SUSTAINING TREATMENT' as a new ORDERABLE ITEMS (the 2476TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST DO NOT USE LST Replace

> DISPLAY TEXT: LST DO NOT USE LIFE SUSTAINING TREATMENT

####### Replace ... With No life sustaining treatment in circumstances other than cardiopulmonary arrest

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: NO NO

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word- processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]=\< DEFAULT WORD-PROCESSING TEXT \>===\[

####### No life-sustaining treatment in circumstances OTHER than cardiopulmonary arrest. DO NOT USE: artificial nutrition (enteral or parenteral), artificial hydration (enteral, IV or subcutaneous) except if needed for comfort, invasive or noninvasive mechanical ventilation, blood products, or dialysis. No transfers to hospital or ICU except if needed for comfort.

> =======T=======T=======T=======T=======T=======T=======T\>======

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE: YES YES WORD-WRAP: WRAP WRAP

> Select PROMPT: 3

> SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

> HELP MESSAGE: Enter the date/time to begin this order.

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT: S Y=“NOW” *(NOTE: Local VistA setup may require simply entering the word NOW)*

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 2// @

> SURE YOU WANT TO DELETE? YES (Yes)

> Select PROMPT:

> Auto-accept this order? NO// YES

#### No Artificial Nutrition - Order Setup

> Select ORDER DIALOG NAME: OR LST NO ARTIFICIAL NUTRITION

> Are you adding 'OR LST NO ARTIFICIAL NUTRITION as a new ORDER DIALOG? No// YES (Yes)

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT ORDERABLE ITEM: LST NO ART NUTRITION

> Are you adding 'LST NO ART NUTRITION' as

> a new ORDERABLE ITEMS (the 2468TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST NO ARTIFICIAL NUTRITION Replace

> DISPLAY TEXT: LST NO ARTIFICIAL NUTRITION

> Replace ... With No artificial nutrition (enteral or

####### parenteral)

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> \<====T=======T=======T=======T=======T=======T=======T=======T\>====== ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE: DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2470// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? YES (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: LST ORDER:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]==\< DEFAULT WORD-PROCESSING TEXT \>=\[ \<PF1\>H=Help

####### No artificial nutrition (enteral or parenteral).

> ====TT=======T=======T=======T=======T=======T=======T=======T\>======

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE:

> WORD-WRAP:

> Select PROMPT: 3 SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

#### Limit Artificial Nutrition as follows: - Order Setup

> ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2471// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? Yes (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: Limit artificial nutrition as follows: REQUIRED: YES YES

> MULTIPLE VALUED:

> ASK ON EDIT ONLY: NO NO ASK ON ACTION: RCW

> HELP MESSAGE: Add explanatory text.

####### (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word-processing. Do NOT add text to the word-processing section for this prompt.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO//

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT: Limit artificial nutrition as follows:

#### No Artificial Hydration - Order Setup

> DISPLAY TEXT: LST NO ARTIFICIAL HYDRATION

####### Replace ... With No artificial hydration (IV enteral or subcutaneous) unless needed for comfort

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> \<====T=======T=======T=======T=======T=======T=======T=======T\>====== ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2470// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? YES (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: LST ORDER:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

#### Limit Artificial Hydration as follows: - Order Setup

> Select ORDER DIALOG NAME: OR LST ARTIFICIAL HYDRATION AS SPECIFIED

> Are you adding 'OR LST ARTIFICIAL HYDRATION AS SPECIFIED' as a new ORDER DIALOG? No// YES (Yes)

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST ART HYDRATION AS SPECIFIED

> Are you adding 'LST ART HYDRATION AS SPECIFIED' as

> a new ORDERABLE ITEMS (the 2469TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST ARTIFICIAL HYDRATION AS SPECIFIED

> Replace

> DISPLAY TEXT: LST ARTIFICIAL HYDRATION AS SPECIFIED

> Replace ... With Limit artificial hydration as follows:

> SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: YES YES

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]=========\< DESCRIPTION \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> ===T=======T=======T=======T=======T=======T=======T=======T\>====== ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE: DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

#### No Invasive Mechanical Ventilation - Order Setup

> ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2468// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

####### SURE YOU WANT TO DELETE? YES (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: LST ORDER:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word- processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]=\< DEFAULT WORD-PROCESSING TEXT \>===\[

####### No invasive mechanical ventilation (e.g., endotracheal or tracheostomy tube) in circumstances other than cardiopulmonary arrest

> =====T=======T=======T=======T=======T=======T=======T=======T=======T

#### No Non-Invasive Mechanical Ventilation - Order Setup

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST NO NON-INVASIVE MECHANICAL VENTILATION Replace

> DISPLAY TEXT: LST NO NON-INVASIVE MECHANICAL VENTILATION Replace ...

####### With No noninvasive mechanical ventilation (e.g. BiPAP or CPAP)

> Replace

> No noninvasive mechanical ventilation (e.g. BiPAP or CPAP) SIGNATURE REQUIRED: ORES ORES

> VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> =====T=======T=======T=======T=======T=======T=======T=======T=======T ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2468// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

####### SURE YOU WANT TO DELETE? YES (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: LST ORDER:

> REQUIRED: YES YES

> MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word- processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]=\< DEFAULT WORD-PROCESSING TEXT \>===\[

####### No non-invasive mechanical ventilation (e.g., BiPAP, CPAP) in circumstances other than cardiopulmonary arrest

> =====T=======T=======T=======T=======T=======T=======T=======T=======T POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT:

> TRAILING TEXT:

> START NEW LINE:

> WORD-WRAP:

> Select PROMPT: 3

> SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

> HELP MESSAGE: Enter the date/time to begin this order.

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT: S Y=“NOW” *(NOTE: Local VistA setup may require simply entering the word NOW)*

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 2// @

> SURE YOU WANT TO DELETE? YES (Yes) *(This should be blank, so that the item does NOT appear in the actual order on the orders tab in CPRS)*

> Select PROMPT:

#### Limit Mechanical Ventilation As Follows - Order Setup

> Select ORDER DIALOG NAME: OR LST MECH VENT SPECIFIED

> Are you adding 'OR LST MECH VENT SPECIFIED' as a new ORDER DIALOG? No// YES (Yes)

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST MECHANICAL VENTILATION AS SPECIFIED

> Are you adding 'LST MECHANICAL VENTILATION AS SPECIFIED' as a new ORDERABLE ITEMS (the 2467TH)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST MECH VENT SPECIFIED Replace

> DISPLAY TEXT: LST MECHANICAL VENTILATION AS SPECIFIED

> Replace ... With Limit mechanical ventilation as follows:

> Replace

> Limit mechanical ventilation as follows: SIGNATURE REQUIRED: ORES ORES

> VERIFY ORDER: YES YES

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]=========\< DESCRIPTION \>=====\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> ====T=======T=======T=======T=======T=======T=======T=======T\>====== ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE: DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

#### No Transfers To ICU Except for Comfort - Order Setup

> ==\[ WRAP \]==\[ INSERT DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> =T=======T=======T=======T=======T=======T=======T=======T\>======

> ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2474// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? Yes (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: LST ORDER:

> REQUIRED: YES YES MULTIPLE VALUED: No NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word- processing.)

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO// YES

#### No Transfers To Hospital Except for Comfort - Order Setup

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST NO TRANSFERS TO HOSPITAL EXCEPT FOR COMFORT

> Are you adding 'LST NO TRANSFERS TO HOSPITAL EXCEPT FOR COMFORT' as a new ORDERABLE ITEMS (the 2472ND)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST NO TRANSFERS TO HOSPITAL EXCEPT FOR COMFORT Replace DISPLAY TEXT: LST NO TRANSFERS TO HOSPITAL EXCEPT FOR COMFORT

####### Replace ... With No transfers to the hospital except if needed for comfort

> Replace

> No transfers to the hospital except if needed for comfort SIGNATURE REQUIRED: ORES ORES

> VERIFY ORDER: NO NO

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> =T=======T=======T=======T=======T=======T=======T=======T\>======

> ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2474// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? Yes (Yes)

#### Limit Transfers as follows: - Order Setup

> Select ORDER DIALOG NAME: OR LST TRANSFERS WITH EXPLANATION

> Are you adding 'OR LST TRANSFERS WITH EXPLANATION' as

> a new ORDER DIALOG? No// YES (Yes) DISPLAY GROUP: LIFE-SUSTAINING TREATMENT

> ORDERABLE ITEM: LST TRANSFERS AS SPECIFIED

> Are you adding 'LST TRANSFERS AS SPECIFIED' as

> a new ORDERABLE ITEMS (the 2473RD)? No// YES (Yes)

> Do you wish to copy an existing order dialog? YES// NO

> NAME: OR LST TRANSFERS WITH EXPLANATION Replace

> DISPLAY TEXT: LST TRANSFERS AS SPECIFIED Replace ... With Limit

####### transfers as follows:

> Replace

> Limit transfers as follows: SIGNATURE REQUIRED: ORES ORES VERIFY ORDER: YES YES

> ASK FOR ANOTHER ORDER: NO NO DESCRIPTION:

> No existing text Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]======\< DESCRIPTION \>===========\[ \<PF1\>H=Help

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> \<=======T=======T=======T=======T=======T=======T=======T=======T ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

#### Limit Other Life-Sustaining Treatments (Specify) - Order Setup

> ==\[ WRAP \]==\[ INSERT \]=======\< DESCRIPTION \>===========\[ \<PF1\>H=Help

####### This order supports implementation of VHA Handbook 1004.03, Life Sustaining Treatment Decisions. This policy is managed by the National Center for Ethics in Health Care.

> ===T=======T=======T=======T=======T=======T=======T=======T=======T\>= ENTRY ACTION:

> EXIT ACTION:

> VALIDATION:

> ADDITIONAL TEXT:

> DISPLAY GROUP: LIFE-SUSTAINING TREATMENT// Select PROMPT: 1 OR GTX ORDERABLE ITEM SEQUENCE: 1//

> PROMPT: OR GTX ORDERABLE ITEM// pointer to a file INDEX: S.LST//

> SCREEN:

> SPECIAL LOOKUP ROUTINE:

> DISPLAY TEXT: Order: // REQUIRED: YES// MULTIPLE VALUED:

> ASK ON EDIT ONLY: YES// ASK ON ACTION:

> HELP MESSAGE:

> XECUTABLE HELP:

> ASK ON CONDITION: I 0 ;uneditable// INPUT TRANSFORM:

####### DEFAULT: S Y=2476// (Note: Local VistA systems may display this as the orderable item. Do NOT replace it.)

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// @

> SURE YOU WANT TO DELETE? Yes (Yes)

> Select PROMPT: 2

> SEQUENCE: 2//

> PROMPT: OR GTX WORD PROCESSING 1 word processing DISPLAY TEXT: Limit other life sustaining treatment as follows: REQUIRED: YES YES

> MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: NO NO ASK ON ACTION: RCW

####### HELP MESSAGE: (Note: After HELP MESSAGE – some local VistA systems skip several prompts and automatically open the box for word- processing. Do NOT add text to the word-processing section for this prompt.)

> XECUTABLE HELP: ASK ON CONDITION: INPUT TRANSFORM:

> DEFAULT WORD-PROCESSING TEXT:

> No existing text Edit? NO//

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 1// FORMAT:

> OMIT TEXT:

> LEADING TEXT: Limit other life-sustaining treatment as follows:

> TRAILING TEXT:

> START NEW LINE:

> WORD-WRAP: WRAP WRAP

> Select PROMPT: 3

> SEQUENCE: 3//

> PROMPT: OR GTX START DATE/TIME relative date/time DISPLAY TEXT: START DATE/TIME:

> REQUIRED: YES YES MULTIPLE VALUED: NO NO ASK ON EDIT ONLY: YES YES ASK ON ACTION: RCW

> HELP MESSAGE: Enter the date/time to begin this order.

> XECUTABLE HELP:

> ASK ON CONDITION:

> INPUT TRANSFORM:

> DEFAULT: S Y=“NOW” *(NOTE: Local VistA setup may require simply entering the word NOW)*

> POST-SELECTION ACTION:

> ENTRY ACTION:

> EXIT ACTION:

> ORDER TEXT SEQUENCE: 2// @

> SURE YOU WANT TO DELETE? Yes (Yes)

> Select PROMPT:

> Auto-accept this order? NO// NO

> Do you want to test this dialog now? YES

> ==\[ WRAP \]==\[ INSERT \]===\< Limit other life_sustaining tr \>==\[

> \<PF1\>H=Help=

####### TEST TEST TEST

> \<=======T=======T=======T=======T=======T=======T=======T=======T

> Order: LST LIMIT OTHER LST AS SPECIFIED

> Limit other life sustaining treatment as follows: TEST TEST TEST START DATE/TIME: NOW (9/30/13@10:59)

#### Build an LST Menu and Place LST Orders on the LST Menu

#### Sites will need to build an order menu for the new Life-Sustaining Treatment orders. This menu can then be assigned to providers who have the authority to input these orders, or it can be embedded in their other menus as appropriate.

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: MM \> MN

#### Build the new LST orders menu

#### Add text

#### Add LST orders to the menu

#### Add this order menu, as appropriate, to other order menus that providers use at your facility

#### When completed, the order menu should look like this:

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/002.png)

2.  <span id="_bookmark18" class="anchor"></span>Go Into CPRS Configuration (Clinical Coordinator) Menu

> PXRM Reminder Managers Menu ... TIU TIU Maintenance Menu ...

> GMTS Health Summary Overall Menu ... PCE PCE Coordinator Menu ...

> CPRS CPRS Configuration (Clin Coord) ...

> Select NATIONAL CONTENT DEVELOPMENT \<TEST ACCOUNT\> Option: CPRS CPRS

####### Configuration (Clin Coord)

> AL Allocate OE/RR Security Keys KK Check for Multiple Keys

> DC Edit DC Reasons

> GP GUI Parameters ...

> GA GUI Access - Tabs, RPL MI Miscellaneous Parameters

> NO Notification Mgmt Menu ... OC Order Checking Mgmt Menu ... MM Order Menu Management ...

> LI Patient List Mgmt Menu ... FP Print Formats

> PR Print/Report Parameters ... RE Release/Cancel Delayed Orders US Unsigned orders search

> EX Set Unsigned Orders View on Exit NA Search orders by Nature or Status CM Care Management Menu ...

> DO Event Delayed Orders Menu ... LO Lapsed Orders search

> PM Performance Monitor Report

3.  <span id="_bookmark19" class="anchor"></span>Follow the Menu Path: Order Menu Management (MM) \> Enter/Edit Order Menus (MN)
4.  <span id="_bookmark20" class="anchor"></span>Build the new LST Orders Menu

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/003.png)

#### Add Explanatory Text to the Menu

#### Add the Orders to the Menu

#### Add the New LST Orders Menu to Other Order Menus

#### Sites will need to determine locally which provider order menus should have the LST order menu added to them. Unless this order menu is added to existing assigned order menus, providers will not be able to access these orders when needed. Even if sites tie the orders into the LST reminder dialog template, providers will still need a way to access these orders from a menu. For example, the patient has an order for DNAR/DNR and wants it suspended during a dialysis. The attending could annotate this in an addendum to the LST progress note, discontinue the current DNR order, and write an order for DNAR/DNR EXCEPT… using the standalone menu.

#### Adding this menu to another order set is done as follows:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: MM \> MN

#### Select the order menu you wish to add the “Life-Sustaining Treatment Orders” menu to

#### Select “Add”

#### Choose: “Menu Items”

#### Add “OR LST ORDER MENU”

#### Define the Row and Column you want to add it to

#### Leave the “Display Text” option blank.

> <span id="_bookmark22" class="anchor"></span>5.5 Editing Auto-Discontinue Rules to Make LST Orders Durable

#### These orders must be durable, so that they do not auto-discontinue when patients move between levels of care (e.g. admission, discharge, transfer, change in treating specialties, etc.).

#### Sites will need to edit their CPRS/VistA “Auto-Discontinue” rules in VistA to make orders in the new Life-Sustaining Treatment display group durable. You will do this by excluding the

#### “Life-Sustaining Treatment” display group from being automatically discontinued when actions are taken on a patient’s record (e.g., admission, discharge, transfer, going into surgery, change in treating specialties, etc.).

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: DO \> DO \> Auto-DC Rules \> AE

#### Edit Each Event

#### Double-check!

### Go Into CPRS Configuration (Clinical Coordinator) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <span id="_bookmark24" class="anchor"></span>Follow the Menu Path: DO \> DO \> Auto-DC Rules
2.  <span id="_bookmark25" class="anchor"></span>Add/Edit Each Event

#### Note: Individual sites may have different “Event Names” set up to allow for Auto-DC actions. Each event must be edited to exclude the Life-Sustaining Treatment display group from being automatically discontinued.

![](pxrm-2-35-life-sustaining-treatment-installation-guide/004.png)

3.  <span id="_bookmark26" class="anchor"></span>Double Check to make sure the action held

> Next you should select “DD Detailed Display” to confirm the change took place.

![](pxrm-2-35-life-sustaining-treatment-installation-guide/005.png)

#### You should continue to “Add/Edit” for each available event to exclude the “Life-Sustaining Treatment” Display Group from each available event. Remember to double check each entry.

> <span id="_bookmark27" class="anchor"></span>5.6 Set Up “NO COPY” for Orders in the “Life-Sustaining Treatment“

> Display Group

#### Since orders in the “Life-Sustaining Treatment” display group are now durable and will not be auto-discontinued, you must ensure that they are not presented to be “copied” from the list of

#### currently active orders when “Event Delayed Orders” are input. If you do not take this step, the

#### durable orders may be duplicated when providers write Event Delayed Orders, which may lead to patient safety issues.

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: DO \> EP \> Exclude display groups from copy

1.  <span id="_bookmark28" class="anchor"></span>Go Into CPRS Configuration (Clinical Coordinator) Menu and Follow the Menu Path: DO \> EP \> Exclude display groups from copy

> PXRM Reminder Managers Menu ... TIU TIU Maintenance Menu ...

> GMTS Health Summary Overall Menu ... PCE PCE Coordinator Menu ...

> CPRS CPRS Configuration (Clin Coord) ...

> Select NATIONAL CONTENT DEVELOPMENT \<TEST ACCOUNT\> Option: CPRS CPRS

####### Configuration (Clin Coord)

> AL Allocate OE/RR Security Keys KK Check for Multiple Keys

> DC Edit DC Reasons

> GP GUI Parameters ...

> GA GUI Access - Tabs, RPL MI Miscellaneous Parameters

> NO Notification Mgmt Menu ... OC Order Checking Mgmt Menu ... MM Order Menu Management ...

> LI Patient List Mgmt Menu ... FP Print Formats

> PR Print/Report Parameters ... RE Release/Cancel Delayed Orders US Unsigned orders search

> EX Set Unsigned Orders View on Exit NA Search orders by Nature or Status CM Care Management Menu ...

> DO Event Delayed Orders Menu ... LO Lapsed Orders search

> PM Performance Monitor Report

> Select CPRS Configuration (Clin Coord) \<TEST ACCOUNT\> Option: DO Event Delayed Orders Menu

> DO Delayed Orders/Auto-DC Set-up

> EP Parameters for event delayed orders IN Inquire to OE/RR Patient Event File

> Select Event Delayed Orders Menu \<TEST ACCOUNT\> Option: EP Parameters for event delayed orders

> Select one of the following:

1.  Write orders list by event
2.  Default release event
3.  Common release event list
4.  Manual release controlled by
5.  Set manual release parameter
6.  Exclude display groups from copy

> Select parameter to edit: 6 Exclude display groups from copy

> Excluded groups for copy active order may be set for the following:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 57%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th><blockquote>
<p>Division</p>
</blockquote></th>
<th>DIV</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
</tr>
</tbody>
</table>

####### Enter selection: 1 Division (Note: Choose the appropriate level for excluding copy of orders in this display group within your VistA system. Select 1 “Division” prompt to select “Institution Name.”)

> NAME: ALL SERVICES MIXED NAME: All SHORT NAME: ALL

> SEQUENCE: 1 MEMBER: PHARMACY

> SEQUENCE: 2 MEMBER: LABORATORY

> SEQUENCE: 3 MEMBER: IMAGING

> SEQUENCE: 4 MEMBER: DIETETICS

> SEQUENCE: 5 MEMBER: CONSULTS

> SEQUENCE: 6 MEMBER: VITALS/MEASUREMENTS

> SEQUENCE: 7 MEMBER: NURSING

> SEQUENCE: 8 MEMBER: SURGERY

> SEQUENCE: 9 MEMBER: M.A.S.

> SEQUENCE: 10 MEMBER: OTHER HOSPITAL SERVICES

> SEQUENCE: 11 MEMBER: PROCEDURES

> SEQUENCE: 12 MEMBER: ALLERGIES

> SEQUENCE: 13 MEMBER: SUPPLIES/DEVICES

> SEQUENCE: 14 MEMBER: RESUSCITATION STATUS

> SEQUENCE: 15 MEMBER: LEGAL STATUS

> SEQUENCE: 16 MEMBER: SAFETY ALERTS

> SEQUENCE: 17 MEMBER: LIFE-SUSTAINING TREATMENT

> Select the display group that you wish to exclude from the *Copy Active Orders* dialog. (Note: Enter “LIFE-SUSTAINING TREATMENT.”)

# Post-Installation Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### There are still several steps necessary to bring the new LST orders into compliance with the forthcoming policy on documenting Life-Sustaining Treatment progress notes and orders. These should be taken after the patch is installed, making the associated VA-LIFE- SUSTAINING TREATMENT reminder dialog available.

#### Briefly, these steps include:

#### Linking the LST orders or LST orders menu to the reminder dialog (local option that is highly encouraged)

#### Setting up the Life-Sustaining Treatment progress note title in VistA

#### Setting up the Life-Sustaining Treatment progress note Document Definition in VistA

## Link the Life-Sustaining Treatment Orders or Orders Menu to the VA-LIFE-SUSTINING TREATMENT Reminder Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### If a site decides to launch LST orders <u>or</u> the LST Order Menu, the site should NOT set up the reminder dialog template to launch both the individual orders and the order menu. This could lead to duplicate order input. Either the LST orders should be associated with the template or the LST Order Menu, not both. (Note: This does not preclude adding the optional “Comfort Care Order Set” or “Local Consult Order Set” to the LST reminder dialog template.)

#### During extensive usability testing, providers STRONGLY requested that the individual orders be launched by selecting the related option in the reminder dialog template (e.g., selecting DNAR in the template automatically launches the associated DNAR order on the orders tab).

#### The input needed for linking and launching a local “Comfort Care Order Set” and/or a “Local Consult Menu” from the LST reminder dialog template is provided as well.

### Linking Individual LST Orders to the LST Reminder Dialog Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Summary of actions:

#### Go into PXRM Reminder Managers Menu ... \[PXRM MANAGERS MENU\]

#### Follow the menu path: DM \[PXRM DIALOG MANAGEMENT\] \> DI \[PXRM DIALOG/COMPONENT EDIT\] \> CV Change View

#### Select either “E - Dialog Elements” or “G - Dialog Groups”, as appropriate

#### Navigate to the appropriate group or element

#### Edit the group or element to add the quick order as a “Finding”, or “Additional Finding” if a “Finding” is already in place

#### Here is an example of linking the order for “Do Not Resuscitate” to the appropriate reminder dialog element, using the path shown above. 

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/006.png)

####### Select Item: Next Screen// 4393 (Note: This number will vary according to each site. Choose the item number associated with the element, “VA-LST DNR (E).

> You may proceed through the remainder of the dialog, then go back through it to ensure that your added “Finding” or “Additional Finding” is in place.

> Here is a table that lists the LST orders and their associated proper, tested VA-LIFE-SUSTAINING TREAMENT reminder dialog linkage locations. You should link these orders using the steps in the example above.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 30%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>LST Order</p>
</blockquote></th>
<th><blockquote>
<p>LST Reminder Dialog Template Placement</p>
</blockquote></th>
<th><blockquote>
<p>Group or Element</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OR LST DNR</strong></td>
<td><strong>VA-LST DNR (E)</strong></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST DNR EXCEPT</strong></td>
<td><strong>VA-LST DNR EXCEPT (G)</strong></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST DO NOT USE LST</strong></td>
<td><p><strong>VA-LST NO LIFE- SUSTAINING TREATMENT</strong></p>
<p><strong>(E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST NO ARTIFICIAL NUTRTION</strong></td>
<td><p><strong>VA-LST NO ART</strong></p>
<p><strong>NUTRITION (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST ARTIFICIAL NUTRITION AS SPECIFIED</strong></td>
<td><p><strong>VA-LST ART NUTRITION-</strong></p>
<p><strong>SPECIFIED (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST NO ARTIFICIAL HYDRATION</strong></td>
<td><p><strong>VA-LST NO ART</strong></p>
<p><strong>HYDRATION (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST ARTIFICIAL HYDRATION AS SPECIFIED</strong></td>
<td><p><strong>VA-LST ART HYDRATION-</strong></p>
<p><strong>SPECIFIED (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST NO INVASIVE MECHANICAL VENTILATION</strong></td>
<td><p><strong>VA-LST NO INVASIVE MECHANICAL</strong></p>
<p><strong>VENTILATION (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST NO NON-INVASIVE MECHANICAL VENTILATION</strong></td>
<td><p><strong>VA-LST NO NON-INVASIVE MECHANICAL</strong></p>
<p><strong>VENTILATION (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST MECH VENT SPECIFIED</strong></td>
<td><p><strong>VA-LST MECH VENT</strong></p>
<p><strong>SPECIFIED (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST NO TRANSFERS TO HOSPITAL EXCEPT FOR COMFORT</strong></td>
<td><p><strong>VA-LST NO TRANSFERS TO HOSPITAL EXCEPT FOR</strong></p>
<p><strong>COMFORT (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST NO TRANSFERS TO ICU EXCEPT FOR COMFORT</strong></td>
<td><p><strong>VA-LST NO TRANSFERS TO ICU EXCEPT FOR</strong></p>
<p><strong>COMFORT (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST TRANSFERS WITH EXPLANATION</strong></td>
<td><p><strong>VA-LST TRANSFERS-LIMIT</strong></p>
<p><strong>(G)</strong></p></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST LIMIT OTHER LST AS SPECIFIED</strong></td>
<td><p><strong>VA-LST LIMIT OTHER -</strong></p>
<p><strong>SPECIFIED GROUP (G)</strong></p></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Linking LST Orders Menu and/or a Local Comfort Care Order Set/Consult Order Set to the LST Reminder Dialog Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Launching LST Order Menus. If your site decides to use the LST reminder dialog template to launch the LST order menu instead of individual orders, these are the locations that are set up to launch the order set(s).

#### Please note that the launching of the LST Order Menu should be linked to the reminder dialog options for documenting “informed consent” by the patient/surrogate. If the patient/surrogate is not capable of giving informed consent, authorization to write life-sustaining orders needs to be obtained prior to writing the orders. Therefore, if launched from the reminder dialog, the order set should be linked to the groups and elements documenting informed consent being obtained from either the patient or the surrogate.

#### Summary of actions:

#### Go into PXRM Reminder Managers Menu ... \[PXRM MANAGERS MENU\]

#### Follow the menu path: DM \[PXRM DIALOG MANAGEMENT\] \> DI \[PXRM DIALOG/COMPONENT EDIT\] \> CV Change View

#### Select either “E - Dialog Elements” or “G - Dialog Groups”, as appropriate

#### Navigate to the appropriate group or element

#### Edit the group or element to add the link for the appropriate Order Set as a “Finding”, or “Additional Finding” if a “Finding” is already in place

#### Here is an example of linking the LST Order Menu one of the two appropriate reminder dialog elements, using the path shown above.

![](pxrm-2-35-life-sustaining-treatment-installation-guide/007.png)

#### You may proceed through the remainder of the dialog, then go back through it to ensure that your added “Finding” or “Additional Finding” is in place.

> Here is a table that lists the LST Order Menu linkage, and the Local Consult Order Menu and Local Comfort Care Order set linkage, along with their associated VA-LIFE-SUSTAINING TREAMENT reminder dialog linkage locations.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 49%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>LST Order Menu</p>
</blockquote></th>
<th><blockquote>
<p>LST Reminder Dialog Template Placement</p>
</blockquote></th>
<th><blockquote>
<p>Reminder Dialog Group or Element</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OR LST ORDER MENU</strong></td>
<td><strong>VA-LST INFORMED COSENT YES (G)</strong></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST ORDER MENU</strong></td>
<td><p><strong>VA-LST INFORMED CONSENT YES - SURR</strong></p>
<p><strong>(G)</strong></p></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>OR LST ORDER MENU</strong></td>
<td><p><strong>VA-LST INFORMED CONSENT-MDC-</strong></p>
<p><strong>FACILITY APPROVED (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>OR LST ORDER MENU</strong></td>
<td><p><strong>VA-LST INFORMED CONSENT - SAPO-</strong></p>
<p><strong>PENDING MDC (E)</strong></p></td>
<td><blockquote>
<p><strong>Element</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>* Locally built consult</p>
<p>menu</p></td>
<td><strong>VA-LST LOCAL CONSULT MENU OPTION (G)</strong></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>* Locally built “Comfort</p>
<p>Care Order Set”</p></td>
<td><strong>VA-LST LOCAL COMFORT CARE ORDERS MENU OPTION (G)</strong></td>
<td><blockquote>
<p><strong>Group</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \* Sites may build these optional menus to support local processes, using local naming conventions, and link them to the VA-LIFE-SUSTAINING TREATMENT reminder dialog template at the locations shown.

#### There is an example of a “Comfort Care Order Set” toolkit available on the NCEHC intranet web site, [<u>vaww.ethics.va.gov</u>.](http://vaww.ethics.va.gov/) Your site may wish to implement a similar order set to support your local processes. Please ensure that any orders built for “Comfort Care” are NOT built to display in the Life-Sustaining Treatment orders display group. They should display under the appropriate display group(s) for orders that are initiated or discontinued at the present time.

#### Also, DO NOT build orders into any local Comfort Care Order Set that duplicate or contradict orders in the Life-Sustaining Treatment order set (e.g. no “Do Not Intubate” orders, no orders that authorize Cardiopulmonary Resuscitation Except When….”, etc.).

#### Attaching a comfort care order set to the reminder dialog template at this location is optional.

#### However, this option was requested by multiple providers during several levels of template usability testing.

#### Building and linking a local consult order menu with a local consult order set will allow sites to link an associated consult order set in the template to support your local processes. Attaching an order set to the reminder dialog template at this location is optional. This option was requested by multiple providers during several levels of template usability testing.

## Set Up the Life-Sustaining Treatment Progress Note Title in the VistA Text Integration Utility (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Life-Sustaining Treatment Decisions progress note title must be built using the Text Integration Utility in VistA.

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: TIU Maintenance Menu \> Document Definitions (Manager)

#### Create Document Definitions \> Navigate to “Advance Directive” Document class

#### Title \> Life-Sustaining Treatment

> Select CPRS Configuration (Clin Coord) \<TEST ACCOUNT\> Option: ^ PXRM Reminder Managers Menu ... \[PXRM MANAGERS MENU\]

####### TIU TIU Maintenance Menu ... \[TIU IRM MAINTENANCE MENU\]

> GMTS Health Summary Overall Menu ... \[GMTS MANAGER\] PCE PCE Coordinator Menu ... \[PX PCE COORDINATOR MENU\]

> CPRS CPRS Configuration (Clin Coord) ... \[OR PARAM COORDINATOR MENU\]

> Select Option: TIU Maintenance Menu

1.  TIU Parameters Menu ... \[TIU SET-UP MENU\]

####### Document Definitions (Manager) ... \[TIUF DOCUMENT DEFINITION MGR\]

2.  User Class Management ... \[USR CLASS MANAGEMENT MENU\]
3.  TIU Template Mgmt Functions ... \[TIU IRM TEMPLATE MGMT\]
4.  TIU Alert Tools \[TIU ALERT TOOLS\]

> 7 TIUHL7 Message Manager \[TIUHL7 MSG MGR\]

> Title Mapping Utilities ... \[TIU MAP TITLES MENU\]

> 6 Active Title Cleanup Report \[TIU ACTIVE TITLE CLEANUP\]

> Select TIU Maintenance Menu \<TEST ACCOUNT\> Option: Document Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions

####### Create Document Definitions

3.  Create Objects

![](pxrm-2-35-life-sustaining-treatment-installation-guide/008.png)

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/009.png)

![](pxrm-2-35-life-sustaining-treatment-installation-guide/010.png)

![](pxrm-2-35-life-sustaining-treatment-installation-guide/011.png)

#### The Life-Sustaining Treatment progress note title has now been created. It is active and available for use. Progress notes with this title will be visible not only on the Progress Note tab of CPRS, but also on the CWAD Postings area of the CPRS Coversheet tab.

## Set Up the Life-Sustaining Treatment Progress Note Document Definition in the VistA Text Integration Utility (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Now that the CPRS progress note title has been built, you will need to add a Document Definition to ensure that the progress note operates appropriately. Sites may set up rules in the document definition to require cosignature of these notes by authors with specific User Classes as appropriate, in accordance with the requirements set forth in VHA Handbook 1004.03.

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu

#### Follow the menu path: TIU Maintenance Menu \> TIU Parameters Menu \> Document Parameter Edit \> Life-Sustaining Treatment

> Select CPRS Configuration (Clin Coord) \<TEST ACCOUNT\> Option: ^ PXRM Reminder Managers Menu ... \[PXRM MANAGERS MENU\]

####### TIU TIU Maintenance Menu ... \[TIU IRM MAINTENANCE MENU\]

> GMTS Health Summary Overall Menu ... \[GMTS MANAGER\] PCE PCE Coordinator Menu ... \[PX PCE COORDINATOR MENU\]

> CPRS CPRS Configuration (Clin Coord) ... \[OR PARAM COORDINATOR MENU\]

> Select Option: TIU Maintenance Menu

####### TIU Parameters Menu ... \[TIU SET-UP MENU\]

1.  Document Definitions (Manager) ... \[TIUF DOCUMENT DEFINITION MGR\]
2.  User Class Management ... \[USR CLASS MANAGEMENT MENU\]
3.  TIU Template Mgmt Functions ... \[TIU IRM TEMPLATE MGMT\]
4.  TIU Alert Tools \[TIU ALERT TOOLS\]

> 7 TIUHL7 Message Manager \[TIUHL7 MSG MGR\]

> Title Mapping Utilities ... \[TIU MAP TITLES MENU\]

> 6 Active Title Cleanup Report \[TIU ACTIVE TITLE CLEANUP\] Select TIU Maintenance Menu \<TEST ACCOUNT\> Option: TIU Parameters Menu

1.  Basic TIU Parameters \[TIU BASIC PARAMETER EDIT\]
2.  Modify Upload Parameters \[TIU UPLOAD PARAMETER EDIT\]

####### Document Parameter Edit \[TIU DOCUMENT PARAMETER EDIT\]

3.  Progress Notes Batch Print Locations \[TIU PRINT PN LOC PARAMS\]
4.  Division - Progress Notes Print Params \[TIU PRINT PN DIV PARAMS\]

> Select TIU Parameters Menu \<TEST ACCOUNT\> Option: Document Parameter Edit

> First edit Institution-wide parameters:

> Select DOCUMENT DEFINITION: LIFE-SUSTAINING TREATMENT TITLE Std Title: LIFE-SUSTAINING TREATMENT PLAN

> REQUIRE RELEASE: NO//

> REQUIRE MAS VERIFICATION:

> REQUIRE AUTHOR TO SIGN: YES// ROUTINE PRINT EVENT(S):

> STAT PRINT EVENT(S):

> MANUAL PRINT AFTER ENTRY: *(Note: Determined locally)*

> ALLOW CHART PRINT OUTSIDE MAS: YES// ALLOW \>1 RECORDS PER VISIT: YES

> ENABLE IRT INTERFACE: *(Note: Leave undefined or set to “NO”)*

> SUPPRESS DX/CPT ON ENTRY: // FORCE RESPONSE TO EXPOSURES:

> ASK DX/CPT ON ALL OPT VISITS: YES//

> SEND ALERTS ON ADDENDA: *(Note: Determined locally)*

> ORDER ID ENTRIES BY TITLE:

> SEND ALERTS ON NEW ID ENTRY:

> SEND COSIGNATURE ALERT: After Author has SIGNED// EDITOR SET-UP CODE:

> Now enter the USER CLASSES for which cosignature will be required:

> Select USERS REQUIRING COSIGNATURE: *(Note: specify user classes who must have co-signatures)*

> Now enter the DIVISIONAL parameters: *(Note: Determined locally)*

> Select DIVISION: *(Note: Determined locally)*

> If document is to be uploaded, specify Filing Alert Recipients: Select FILING ALERT RECIPIENT:

> Press RETURN to continue...

## Set Up Life-Sustaining Treatment Progress Note Business Rules in TIU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Per forthcoming policy, the LST Progress note and associated orders may only be completed by: attending physicians; Licensed Independent Practitioners (LIP) in charge of the patient’s care; or physician resident, Supervised Advanced Practice Registered Nurses, or Supervised Physician Assistants meeting additional qualifications spelled out in the policy. Your site may wish to associate business rules with this progress note title to limit who may enter and sign a Life-Sustaining Treatment progress note, based upon User Class(es).

#### Summary of actions:

#### Go into CPRS Configuration (Clinical Coordinator) Menu and follow the menu path: TIU \[TIU IRM MAINTENANCE MENU\] \> User Class Management ... \[USR CLASS MANAGEMENT MENU\] \> Manage Business Rules \[USR BUSINESS RULE MANAGEMENT\]

#### Add business rules to the progress note title: Life-Sustaining Treatment as appropriate

#### Below are some sample business rules for the User Class “ATTENDING PHYSICIAN,” allowing attending physicians to author these notes. It is understood that business rules require local coordination and the User Classes will vary from site to site. Please remember that locally developed business rules should meet the requirements of VHA Handbook 1004.03, which will restrict the authoring of the “LIFE-SUSTAINING TREATMENT” progress note to specific groups of providers (see Handbook for specific authorization criteria). It will also restrict who is authorized to add addenda to a completed “LIFE-SUSTAINING TREATMENT” progress note. Access restrictions should only to be placed on entering and adding addenda to these notes, not on viewing of notes. Uncosigned notes input should be viewable to all staff with access to see progress notes in CPRS.

#### An UNSIGNED (TITLE) LIFE-SUSTAINING TREATMENT may BE VIEWED by an ATTENDING PHYSICIAN who is also an AUTHOR/DICTATOR

#### An UNSIGNED (TITLE) LIFE-SUSTAINING TREATMENT may BE EDITED by an ATTENDING PHYSICIAN who is also an AUTHOR/DICTATOR

#### An UNTRANSCRIBED (TITLE) LIFE-SUSTAINING TREATMENT may BE ENTERED by an ATTENDING PHYSICIAN who is also a TRANSCRIBER

#### For Addenda:

#### A COMPLETED (TITLE) LIFE SUSTAINING TREATMENT PLAN may BE ADDENDED by an ATTENDING PHYSICIAN.

## Activate the Reminder Dialog for TIU Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### You will need to activate the Life-Sustaining Treatment reminder dialog template for TIU use prior to linking it to the progress note title.

#### Summary of actions:

#### In VistA go to the PCRM Reminder Managers Menu

#### Follow the menu path: CP – CPRS Reminders Configuration \> TIU - TIU Template Reminder Dialog Parameter \> System

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/012.png)INFO Reminder Information Only Menu ... DM Reminder Dialog Management ...

####### CP CPRS Reminder Configuration ...

> RP Reminder Reports ...

> MST Reminders MST Synchronization Management ... PL Reminder Patient List Menu ...

> PAR Reminder Parameters ...

> ROC Reminder Order Check Menu ... XM Reminder Extract Menu ...

> GEC GEC Referral Report

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

####### TIU TIU Template Reminder Dialog Parameter

> DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allowed as Templates may be set for the following:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose</th>
<th>from NEW PERSON]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td>[choose</td>
<td>from SERVICE/SECTION]</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td colspan="2"><blockquote>
<p>[SALT LAKE CITY]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td colspan="2"><blockquote>
<p>[NATREM.FO-SLC.MED.VA.GOV]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter selection: 5 System NATREM.FO-SLC.MED.VA.GOV

> Setting Reminder Dialogs allowed as Templates for System: NATREM.FO- SLC.MED.VA

> .GOV

> available Then select the next number available. Select Display Sequence: 99

> Are you adding 99 as a new Display Sequence? Yes// YES

> Display Sequence: 99// 99

> Clinical Reminder Dialog: VA-LIFE-SUSTAINING TREATMENT (D) Select Display Sequence:

## Adding the Life-Sustaining Treatment Reminder Dialog Template Into CPRS and Linking It to the Progress Note Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Once the Life-Sustaining Treatment reminder dialog template is imported via the patch and you have set up the appropriate progress note title, you will need to add the reminder dialog template to the notes tab in CPRS and link it to the Life-Sustaining Treatment progress note title.

#### You will need the ability to “Edit Shared Templates” in CPRS. Summary of actions:

#### Go into CPRS Notes tab

#### Follow the menu path: Options \> Edit Shared Templates \> Template Editor Window

#### In CPRS, from the Notes Tab

#### Select the drop down for “Options”

#### Select “Edit Shared Templates”

#### This will launch the “Template Editor” window.

#### Ensure that the box is checked for “Edit Shared Templates”

#### Select (single click) “Document Titles”

![](pxrm-2-35-life-sustaining-treatment-installation-guide/013.png)

#### While still in the “Template Editor” window:

#### Select “New Template”

#### Replace the name “New Template” with “LIFE-SUSTAINNG TREATMENT”

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/014.png)

#### While still in the “Template Editor” window:

#### Select “Reminder Dialog” on the drop down for “Template Type”

#### Select “VA-LIFE-SUSTAINING TREATMENT” on the drop down for “Reminder Dialog”

#### Select “LIFE-SUSTAINING TREATMENT” on the drop down for “Associated Title”

#### Click “OK”

> Here is an example of these actions. Please note that some options will be site-specific.

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/015.png)

#### The VA-LIFE-SUSTAINING TREATMENT reminder dialog should now be available in CPRS, linked to the CPRS progress note title “Life-Sustaining Treatment.” Test this by starting a new note with the title “Life-Sustaining Treatment.” The reminder dialog template should launch and display the reminder dialog wizard.

#### Test the wizard for functionality, launching of orders, and/or order menus (if linked).

1.  <span id="_bookmark38" class="anchor"></span>Editing the CPRS “Template Fields” Deployed With the Reminder

> Dialog

#### Several CPRS template fields were deployed with this reminder dialog. They all begin with the letters “VA-LST”. These should NOT be changed without approval from the VHA National Center for Ethics in Health Care, except as provided in the table below.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 44%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CPRS Template</p>
<p>Field</p>
</blockquote></th>
<th><blockquote>
<p>Function</p>
</blockquote></th>
<th><blockquote>
<p>Editing Allowed (yes/no)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VA-LST DNR OR DNAR</strong></td>
<td><blockquote>
<p><strong>Used to import either the acronym: DNAR/DNR or DNAR or DNR in the template.</strong></p>
</blockquote></td>
<td><strong>Sites may change this to display either "DNAR:" or "DNR:". Sites may not use any other verbiage in this field. These abbreviations are authorized in VHA Handbook 1004.03.</strong></td>
</tr>
<tr class="even">
<td><strong>VA-LST DNR OR DNAR WITH EXCEPTION</strong></td>
<td><blockquote>
<p><strong>Used to import: “DNAR/DNR with exception:” in the template.</strong></p>
</blockquote></td>
<td><strong>Sites may change this to display either "DNAR with exception:" or "DNR with exception:". Sites may not use any other verbiage in this field. These abbreviations are authorized in VHA Handbook 1004.03.</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-LST-MDC PROCESS</strong></td>
<td><blockquote>
<p><strong>Imports text to describe the process for initiating a multidisciplinary committee review of a proposed life-sustaining treatment plan for patients lacking a surrogate and lacking decision-making capacity. Text currently states: “If you do not know how to initiate the multidisciplinary committee review process, contact your supervisor or the</strong></p>
<p><strong>Chief of Staff's office.”</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>This text may be edited with a short statement to identify the local process for consulting the Multidisciplinary Committee, such as “Send a consult titled, XXX to the Multidisciplinary Committee”.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>VA-LST BLANK LINE FOR TEMPLATE</strong></p>
<p><strong>SPACING</strong></p></td>
<td><blockquote>
<p><strong>Provides spacing within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-LST POLICY LINK</strong></td>
<td><blockquote>
<p><strong>Provides URL to VHA Handbook 1004.01</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Do not edit unless directed by the National Center for Ethics in Health Care</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-LST MUST SELECT ONE</strong></td>
<td><blockquote>
<p><strong>Brings text into template that is excluded from the note.</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 44%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CPRS Template</p>
<p>Field</p>
</blockquote></th>
<th><blockquote>
<p>Function</p>
</blockquote></th>
<th><blockquote>
<p>Editing Allowed (yes/no)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VA-LST SURR LIST</strong></td>
<td><blockquote>
<p><strong>Provides drop down list of surrogate possibilities in the order required by</strong></p>
<p><strong>policy and US Code.</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>VA-LST WORD PROCESSING</strong></p>
<p><strong>SHORT</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>VA-LST WP 2</strong></p>
<p><strong>LINE</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-LST OPT COMMENT-DO</strong></td>
<td><blockquote>
<p><strong>Brings text into template that is excluded from the note.</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>VA-LST</strong></p>
<p><strong>ADDITIONAL COMMENTS</strong></p></td>
<td><blockquote>
<p><strong>Brings text into template that is excluded from the note.</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-LST WORD PROCESSING1</strong></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>VA-LST WORD PROCESS 2</strong></p>
<p><strong>LINES REQ</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>VA-LST WP MAND</strong></p>
<p><strong>2 LINE</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>VA-LST WP MAND</strong></p>
<p><strong>2 LINE</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>VA-LST TEXT</strong></p>
<p><strong>(45)</strong></p></td>
<td><blockquote>
<p><strong>Provides word processing field within the template</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>VA-LST</strong></p>
<p><strong>ADDITIONAL FINAL COMMENTS</strong></p></td>
<td><blockquote>
<p><strong>Brings text into template that is excluded from the note.</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>NO editing allowed.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<Your directory\>PXRM_2_0_35.KID

> KIDS Distribution saved on Sep 08, 2015@12:00:35 Comment: VA-LIFE-SUSTAINING DIALOG

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*35 has been loaded before, here is when:

> PXRM\*2.0\*35 Install Completed

> was loaded on Nov 25, 2014@13:27:42 PXRM\*2.0\*35 Install Completed

> was loaded on Apr 21, 2015@13:18:31 PXRM\*2.0\*35 Install Completed

> was loaded on Apr 21, 2015@14:13:47 PXRM\*2.0\*35 Install Completed

> was loaded on Sep 08, 2015@12:03:55 PXRM\*2.0\*35 Install Completed

> was loaded on Sep 08, 2015@12:11:47 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// YES Loading Distribution...

> PXRM\*2.0\*35

> Use INSTALL NAME: PXRM\*2.0\*35 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*35 9/8/15@12:18:19

> =\> VA-LIFE-SUSTAINING DIALOG ;Created on Sep 08, 2015@12:00:35

> This Distribution was loaded on Sep 08, 2015@12:18:19 with header of VA-LIFE-SUSTAINING DIALOG ;Created on Sep 08, 2015@12:00:35

> It consisted of the following Install(s):

> PXRM\*2.0\*35

> Checking Install for Package PXRM\*2.0\*35 Install Questions for PXRM\*2.0\*35 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// SSH Virtual Terminal

> --------------------------------------------------------------------------------

> Install Started for PXRM\*2.0\*35 : Sep 08, 2015@12:18:28

> Build Distribution Date: Sep 08, 2015 Installing Routines:

> Sep 08, 2015@12:18:28

> Running Pre-Install Routine: PRE^PXRMP35I Installing Data Dictionaries:

> Sep 08, 2015@12:18:28

> Installing Data:

> Sep 08, 2015@12:18:30

Running Post-Install Routine: POST^PXRMP35I

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry VA-LIFE-SUSTAINING TREATMENT PXRM\*2.0\*35 Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*35 Installed.

> Sep 08, 2015@12:19:06

> Not a production UCI

> PXRM\*2.0\*35

> Install Completed

# Appendix B - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The OIT Master Glossary is available at: [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

| Term | Definition                            |
|----------|-------------------------------------------|
| CPRS     | Computerized Patient Record System        |
| DNAR     | Do Not Attempt Resuscitation              |
| DNR      | Do Not Resuscitate                        |
| LST      | Life-Sustaining Treatment                 |
| NCEHC    | National Center for Ethics in Health Care |
| OIT/OI&T | Office of Information Technology          |
| TIU      | Text Integration Utility                  |
| VHA      | Veterans Health Administration            |
|          |                                           |
|          |                                           |
|          |                                           |
|          |                                           |

# Appendix C – Health Factors and Reminder Dialog Linkage Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Health Factor Category</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Health Factor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Life-Sustaining Treatment Template Location</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ETHICS-LST</strong></td>
<td>ETHICS-LIFE-SUSTAINING TREATMENT</td>
<td>VA-LST MAIN HEADER (G)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-DECISION- MAKING CAPACITY</strong></td>
<td><p>ETHICS-DECISION-MAKING</p>
<p>CAPACITY-YES</p></td>
<td><p>VA-LST DMC - PATIENT HAS</p>
<p>(E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-DECISION- MAKING CAPACITY</strong></td>
<td>ETHICS-DECISION-MAKING CAPACITY-NO</td>
<td>VA-LST DMC - PATIENT LACKS HAS SURR (E)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-DECISION- MAKING CAPACITY</strong></td>
<td>ETHICS-DECISION-MAKING CAPACITY-NO</td>
<td>VA-LST DMC - PATIENT LACKS - NO SURR-HF (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-SURROGATE</strong></td>
<td>ETHICS-SURROGATE-HAS</td>
<td><p>VA-LST SURROGATE SELECTION OPTIONS (E) &amp; VA-LST DMC - PATIENT</p>
<p>LACKS HAS SURR (E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-SURROGATE</strong></td>
<td>ETHICS-SURROGATE-DOES NOT HAVE</td>
<td><p>VA-LST SURROGATE SELECTION - NONE (E) &amp; VA-LST DMC - PATIENT</p>
<p>LACKS - NO SURR-HF (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-MED CONDITION UNDERSTANDING</strong></td>
<td><p>ETHICS-MED CONDITION</p>
<p>UNDERSTANDING-YES</p></td>
<td><p>VA-LST UNDERSTANDING-HAS</p>
<p>(E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-MED CONDITION UNDERSTANDING</strong></td>
<td><p>ETHICS-MED CONDITION</p>
<p>UNDERSTANDING-OTHER</p></td>
<td><p>VA-LST UNDERSTANDING-</p>
<p>OTHER (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-</p>
<p>OTHER-SPECIFIED</p></td>
<td>VA-LST GOAL OTHER (G)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-BE</p>
<p>CURED</p></td>
<td>VA-LST GOAL BE CURED (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-</p>
<p>PROLONG LIFE</p></td>
<td><p>VA-LST GOAL PROLONG LIFE</p>
<p>(E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td>ETHICS-PATIENT GOAL- FUNCTION-INDEP-QUAL</td>
<td>VA-LST GOAL MAINTAIN FUNCTION/INDEPEND/QOL (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-BE</p>
<p>COMFORTABLE</p></td>
<td><p>VA-LST GOAL BE</p>
<p>COMFORTABLE (E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-</p>
<p>FAMILY SUPPORT</p></td>
<td><p>VA-LST GOAL OBTAIN</p>
<p>SUPPORT (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-PATIENT GOALS OF CARE</strong></td>
<td><p>ETHICS-PATIENT GOAL-</p>
<p>ACHIEVE LIFE GOALS</p></td>
<td><p>VA-LST GOAL ACHIEVE LIFE</p>
<p>GOALS (E)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Health Factor Category</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Health Factor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Life-Sustaining Treatment Template Location</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>ETHICS-OTHER THAN ARREST</strong></td>
<td>ETHICS-FULL SCOPE OF TREATMENT</td>
<td>VA-LST FULL SCOPE OF TREATMENT (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-OTHER THAN ARREST</strong></td>
<td><p>ETHICS-LIMIT LIFE-</p>
<p>SUSTAINING TREATMENT</p></td>
<td>VA-LST LIMITED LST (G)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-OTHER THAN ARREST</strong></td>
<td><p>ETHICS-NO LIFE-</p>
<p>SUSTAINING TREATMENT</p></td>
<td><p>VA-LST NO LIFE-SUSTAINING</p>
<p>TREATMENT (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-ARTIFICIAL NUTRITION</strong></td>
<td><p>ETHICS-NO ARTIFICIAL</p>
<p>NUTRITION</p></td>
<td>VA-LST NO ART NUTRITION (E)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-ARTIFICIAL NUTRITION</strong></td>
<td><p>ETHICS-LIMIT ARTIFICIAL</p>
<p>NUTRITION</p></td>
<td><p>VA-LST ART NUTRITION-</p>
<p>SPECIFIED (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-ARTIFICIAL HYDRATION</strong></td>
<td><p>ETHICS-NO ARTIFICIAL</p>
<p>HYDRATION</p></td>
<td>VA-LST NO ART HYDRATION (E)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-ARTIFICIAL HYDRATION</strong></td>
<td><p>ETHICS-LIMIT ARTIFICIAL</p>
<p>HYDRATION</p></td>
<td><p>VA-LST ART HYDRATION-</p>
<p>SPECIFIED (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-MECHANICAL VENTILATION</strong></td>
<td><p>ETHICS-NO INVASIVE MECH</p>
<p>VENTILATION</p></td>
<td><p>VA-LST NO INVASIVE</p>
<p>MECHANICAL VENTILATION (E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-MECHANICAL VENTILATION</strong></td>
<td><p>ETHICS-NO NON-INVASIVE</p>
<p>MECH VENTILATION</p></td>
<td><p>VA-LST NO NON-INVASIVE</p>
<p>MECHANICAL VENTILATION (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-MECHANICAL VENTILATION</strong></td>
<td><p>ETHICS-LIMIT MECHANICAL</p>
<p>VENTILATION</p></td>
<td><p>VA-LST MECH VENT SPECIFIED</p>
<p>(E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-TRANSFERS</strong></td>
<td>ETHICS-LIMIT TRANSFERS- ICU</td>
<td><p>VA-LST NO TRANSFERS TO</p>
<p>ICU EXCEPT FOR COMFORT (E)</p></td>
</tr>
<tr class="odd">
<td><strong>ETHICS-TRANSFERS</strong></td>
<td>ETHICS-LIMIT TRANSFERS- HOSPITAL</td>
<td><p>VA-LST NO TRANSFERS TO</p>
<p>HOSPITAL EXCEPT FOR COMFORT (E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-TRANSFERS</strong></td>
<td><p>ETHICS-LIMIT TRANSFERS-</p>
<p>GENERAL</p></td>
<td>VA-LST TRANSFERS-LIMIT (G)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-LIMIT OTHER LST</strong></td>
<td><p>ETHICS-LIMIT OTHER LIFE-</p>
<p>SUSTAINING TX</p></td>
<td><p>VA-LST LIMIT OTHER -</p>
<p>SPECIFIED GROUP (G)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-RESUSCITATION</strong></td>
<td>ETHICS-CPR-FULL CODE</td>
<td>VA-LST FULL CODE (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-RESUSCITATION</strong></td>
<td>ETHICS-DNAR/DNR</td>
<td>VA-LST DNR (E)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-RESUSCITATION</strong></td>
<td>ETHICS-DNAR/DNR- EXCEPT</td>
<td>VA-LST DNR EXCEPT (G)</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Health Factor Category</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Health Factor</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Life-Sustaining Treatment Template Location</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ETHICS-LST CONSENT</strong></td>
<td>ETHICS-LST CONSENT- PATIENT</td>
<td>VA-LST INFORMED CONSENT YES (G)</td>
</tr>
<tr class="even">
<td><strong>ETHICS-LST CONSENT</strong></td>
<td>ETHICS-LST CONSENT- SURROGATE</td>
<td>VA-LST INFORMED CONSENT YES - SURR (G)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-LST CONSENT</strong></td>
<td><p>ETHICS-LST CONSENT-MDC-</p>
<p>FACILITY APPROVED</p></td>
<td><p>VA-LST INFORMED CONSENT-</p>
<p>MDC-FACILITY APPROVED (E)</p></td>
</tr>
<tr class="even">
<td><strong>ETHICS-LST CONSENT</strong></td>
<td>ETHICS-LST CONSENT-SAPO- PENDING MDC</td>
<td>VA-LST INFORMED CONSENT - SAPO-PENDING MDC (E)</td>
</tr>
<tr class="odd">
<td><strong>ETHICS-LST SUPERVISING PRACTITIONER</strong></td>
<td>ETHICS-SUPERVISING PRACTITIONER FOR LST</td>
<td>VA-LST SUPERVISING PRACT REVIEW (G)</td>
</tr>
</tbody>
</table>

# Appendix D – Life-Sustaining Treatment Orders in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Life-Sustaining Treatment orders should show up at the top of the orders tab under the

#### “Service” “Life-Sustaining Treatment”. When signed they should not have a stop date/time. Here are examples of the orders. When prompted for text input, the words “test text” were entered.

![](pxrm-2-35-life-sustaining-treatment-installation-guide/016.png)

# Appendix E – Life-Sustaining Treatment Reminder Dialog Screenshots

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Life-Sustaining Treatment reminder dialog template should open looking like this:

![](pxrm-2-35-life-sustaining-treatment-installation-guide/017.png)

> ![](pxrm-2-35-life-sustaining-treatment-installation-guide/018.png)