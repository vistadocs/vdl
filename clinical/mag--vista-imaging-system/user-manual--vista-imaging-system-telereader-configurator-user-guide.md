---
title: VistA Imaging System TeleReader Configurator User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VistA Imaging System TeleReader Configurator
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - telereader
  - configurator
  - vista
  - imaging
  - strong
  - configuring
  - guide
  - consult
page_count: 0
word_count: 1589
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag_telereader_configurator_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag_telereader_configurator_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=413"
---

> ![](vista-imaging-system-telereader-configurator-user-guide/001.png)

VistA Imaging System TeleReader Configurator User Guide

> July 2013 – Revision 2

> Department of Veterans Affairs Office of Enterprise Development (OED)

> Office of Information and Technology (OI&T)

> MAG\*3.0\*127 TeleReader Configurator User Guide July 2013

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development office.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

> Revision History

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 50%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Rev</strong></th>
<th><strong>Date</strong></th>
<th><strong>Notes</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0.9a</td>
<td>07-20-2010</td>
<td>Initial draft.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>0.9b</td>
<td>08-04-2010</td>
<td>2<sup>nd</sup> iteration based on 1<sup>st</sup> product review comments</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>0.9c</td>
<td>08-10-2010</td>
<td>Made some additional formatting changes.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>0.9d</td>
<td>08-11-2010</td>
<td>Updated for Release.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>0.9e</td>
<td>08-18-2010</td>
<td>Replaced Reader Page Screen Shot with correct spelling of Privilege.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>0.9f</td>
<td>08-19-2010</td>
<td>Updated Unread List Page.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1.0</td>
<td>08-26-2010</td>
<td>Updated for National Release.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1.1</td>
<td>05-11-2011</td>
<td>Updated for National Release P106, new section added called “Configuring TeleReader with a Thin Client”.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2</td>
<td>07-15-2013</td>
<td><p>Updated for national release of Patch 127. Revised sections Adding a Consult Type to the TeleReader Unread List; Editing a Consult Type; Configuring TeleReader Readers. Added section Cloning</p>
<p>TeleReader Profiles.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
- [VistA Imaging Configuration for TeleReader](#vista-imaging-configuration-for-telereader)
- [Using TeleReader Configurator](#using-telereader-configurator)
  - [Menus](#menus)
  - [System Help File](#system-help-file)
    - [Field Help Text](#field-help-text)
  - [TeleReader Configurator Main Screen](#telereader-configurator-main-screen)
    - [System Message Log](#system-message-log)
    - [![](vista-imaging-system-telereader-configurator-user-guide/008.png)About Box](#vista-imaging-system-telereader-configurator-user-guide008pngabout-box)
  - [Configuring an Acquisition Site](#configuring-an-acquisition-site)
    - [Configuring the TeleReader Unread List](#configuring-the-telereader-unread-list)
    - [Adding a Consult Type to the TeleReader Unread List](#adding-a-consult-type-to-the-telereader-unread-list)
    - [Editing a Consult Type](#editing-a-consult-type)
    - [Deleting a Consult Type from the Unread List](#deleting-a-consult-type-from-the-unread-list)
    - [Configuring the Modality Worklist](#configuring-the-modality-worklist)
    - [Adding a Consult Type to the Modality Worklist](#adding-a-consult-type-to-the-modality-worklist)
    - [Adding Clinics to a Modality Worklist Consult Type](#adding-clinics-to-a-modality-worklist-consult-type)
    - [Editing a Modality Worklist Consult Type](#editing-a-modality-worklist-consult-type)
    - [Deleting a Modality Worklist Consult Type](#deleting-a-modality-worklist-consult-type)
  - [Configuring a Reading Site](#configuring-a-reading-site)
    - [Configuring Rights to Acquisition Sites](#configuring-rights-to-acquisition-sites)
    - [Adding an Acquisition Site](#adding-an-acquisition-site)
    - [Editing, Activating/Deactivating an Acquisition Site](#editing-activatingdeactivating-an-acquisition-site)
    - [Delete an Acquisition Site](#delete-an-acquisition-site)
    - [Configuring TeleReader Readers](#configuring-telereader-readers)
    - [Adding New TeleReader Readers](#adding-new-telereader-readers)
    - [Adding Additional Privileges to a Reader](#adding-additional-privileges-to-a-reader)
    - [Activate/Deactivate Privileges](#activatedeactivate-privileges)
    - [Deleting a Reader or Reader Privilege](#deleting-a-reader-or-reader-privilege)
    - [Cloning TeleReader Profiles](#cloning-telereader-profiles)
    - [Configuring TeleReader Global Settings](#configuring-telereader-global-settings)
  - [Configuring TeleReader with a Thin Client](#configuring-telereader-with-a-thin-client)
> This document explains how to configure the VistA Imaging TeleReader application using the TeleReader Configurator application. Configuration for both the acquisition and reading sites are described.
> This document is meant for site administrators to assist in configuring the TeleReader. This document does not contain information for users of the TeleReader.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FDA regulations require that each Imaging software distribution is documented and tracked by the VistA Imaging project.

# VistA Imaging Configuration for TeleReader 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader works in conjunction with the Consult Request Tracking package (GMRC) to enable a user to obtain a list of imaging studies that are ready to be interpreted. Configuration work is required at both the Acquisition Site and the Reading Site.

> The TeleReader was first introduced in MAG\*3.0\*46 and included instructions for configuration using VA FileMan. The TeleReader Configurator was developed to replace VA FileMan as the preferred method for configurating the TeleReader.

> TeleReader Configurator is a windows-based application that eliminates the need for a site administrator to access VistA files and fields directly. The TeleReader Configurator will ensure data integrity.

> VistA Imaging Configuration for TeleReader

> This page intentionally left blank.

# Using TeleReader Configurator 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Menus are available on several screens within the application that consist of:

> File: The File Menu contains items that are equivalent to buttons on that screen and an option to close the screen, or in the case of the main screen, exit the application.

> Help: The Help Menu contains an item ‘Contents’ which opens the system help file. On the TeleReader Main Screen, the Help Menu also contains Message Log and About Box.

## System Help File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As mentioned in the Menus section, the system help file can be accessed from the Contents menu item under Help on any screen that contains a menu. In addition, the system help file can be accessed from any screen by pressing the F1 key

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/002.png)</p>
</blockquote></th>
<th><p><strong>NOTE: On screens that add or edit configuration settings, when focus is on a control that is tied to a specific field, for example, combo box, the F1 will invoke help text for that field instead of the</strong></p>
<p><strong>system help file. This is explained in the Field Help Text section.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Field Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any screen that adds or edits configuration settings will have text available for each field on that screen. To invoke the help text for that field either press the F1 key while focus is on that control (combo box, edit box) or click on the ![](vista-imaging-system-telereader-configurator-user-guide/003.png) icon above it to the right.

![](vista-imaging-system-telereader-configurator-user-guide/004.png)

> Figure 1: Field Text Help

## TeleReader Configurator Main Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the TeleReader Configurator Main Screen, the user has the option to configure Acquisition Site Settings, Reading Site Settings, and Global Settings.

> ![](vista-imaging-system-telereader-configurator-user-guide/005.png)

> Figure 2: TeleReader Configurator Main Screen

> The Acquisition Site Setup button opens the Acquisition Site Consult Setup Screen. The Reading Site Setup button opens the Reader Setup Screen. The Global Settings button opens the TeleReader Global System Settings Screen.

> In addition to the standard ‘Contents’ menu item, The TeleReader Configurator Main Screen Help Menu contains selections to view the System Message Log and Application About Box. The Main Screen title bar displays the login server in parentheses.

### System Message Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the TeleReader Configurator, under the Help Menu, click Message Log. The View Log File Screen opens.

![](vista-imaging-system-telereader-configurator-user-guide/006.png)

> Figure 3: View Log File Screen

> The System Log tracks application activity and can be used to troubleshoot problems in the system. The TeleReader Configurator adds information to the log from start up to close. After the user closes the application, the Log is saved to a .log file in C:\Program Files\VistA\Imaging with a timestamp. One Log file is created per session.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/007.png)</p>
</blockquote></th>
<th><strong>NOTE: As the number of files in the directory grows, the administrator can delete the older files as necessary.</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ![](vista-imaging-system-telereader-configurator-user-guide/008.png)About Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 4: About Box

> The About Box shows information about the application, such as version number.

## Configuring an Acquisition Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure an Acquisition Site, from the TeleReader Configurator Main Screen page click the Acquisition Site Setup button. This opens the Acquisition Site Consult Setup Screen.

![](vista-imaging-system-telereader-configurator-user-guide/009.png)

> <span id="_bookmark11" class="anchor"></span>Figure 5: Acquisition Site Consult Setup Screen

> The Acquisition Site Consult Setup Screen has two pages. The TeleReader Unread List page configures which Consult Types VistA Imaging will add to the TeleReader Unread List when a Consult is ordered. This is the default page when the screen is opened.

> The Modality Worklist Screen configures which Consult Types will be added to the DICOM Modality Worklist when a Consult is ordered.

### Configuring the TeleReader Unread List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader Unread List page (see [Figure 5: Acquisition Site Consult Setup Screen](#_bookmark11)) displays all Consult Types currently configured to appear on the TeleReader Unread List. Only Consults listed are configured for use with the TeleReader. The bottom panel shows the detail of the selected Service Name. The display is updated as Consult Types are added to /edited/deleted from the TeleReader Unread List.

### Adding a Consult Type to the TeleReader Unread List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new Consult Type to the TeleReader Unread List, click the Add button on the TeleReader Unread List page.

> The Add TeleReader Consult Type Dialog ([Figure 6: Add TeleReader Consult Type](#_bookmark14) [Dialog](#_bookmark14)) appears.

![](vista-imaging-system-telereader-configurator-user-guide/010.png)

> <span id="_bookmark14" class="anchor"></span>Figure 6: Add TeleReader Consult Type Dialog

> The Add TeleReader Consult Type Dialog has six required fields and one optional field. The fields are:

> Service Name: Service Name of the Consult Type to be added to the Unread List.

> Procedure: This field is optional. Some services do not have associated procedures. If you select a service that has no associated procedures, the Procedure field is disabled.

> Specialty Index: Specialty Index of the Consult Type to be added to the Unread List.

> Procedure/Event Index: The drop-down list is a subset of the selected Specialty Index.

> Acquisition Site: The Acquisition Site defaults to the Login site.

> Unread List Trigger: The Unread List Trigger field defaults to ‘(I) – CREATE/UPDATE WITH EVERY ACQUIRED IMAGE’.

![](vista-imaging-system-telereader-configurator-user-guide/011.png)

> Figure 7: Select UNREAD LIST TRIGGER Field

> TIU Note Title: The TIU note to be associated with the consult.

> When a selection is made for all required fields, the Save button is enabled.

### Editing a Consult Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-imaging-system-telereader-configurator-user-guide/012.png)

> <span id="_bookmark16" class="anchor"></span>Figure 8: Consult Types to be added to the TeleReader Unread List

> To edit the values of a Consult Type from the TeleReader Unread List page, highlight the Service Name row on the Consult Types to be added to the TeleReader Unread List ([Figure 8: Consult Types to be added to the TeleReader Unread List](#_bookmark16)) and click Edit.

> The Edit TeleReader Consult Type Dialog appears (see [Figure 9: Edit TeleReader](#_bookmark17) [Consult Type Dialog](#_bookmark17)).

> ![](vista-imaging-system-telereader-configurator-user-guide/013.png)

> <span id="_bookmark17" class="anchor"></span>Figure 9: Edit TeleReader Consult Type Dialog

> The Edit TeleReader Consult Type Dialog populates with current values of the selected Consult Type.

> The Service Name field displays the Service Name originally selected for the consult type. The field is disabled and cannot be changed.

> The Procedure: Optional field displays the procedure originally associated with the Service Name for this consult type. The field is disabled and cannot be changed.

> The remaining fields on the screen are enabled and can be edited.

> Once a change has been made to the screen, the Save button is enabled.

### Deleting a Consult Type from the Unread List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To delete a Consult Type, from the TeleReader Unread List page (see Figure 5) select the Service Name and click the Delete button. A dialog appears, asking the user for confirmation. The user can either Cancel the action or click OK to confirm the deletion of the Consult Type.

### Configuring the Modality Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure Consult Types to the Modality Worklist, from the Acquisition Site Consult Setup Screen page click the Modailty Worklist tab.

> ![](vista-imaging-system-telereader-configurator-user-guide/014.png)

> <span id="_bookmark20" class="anchor"></span>Figure 10: Modality Worklist Screen

> The Modality Worklist Screen (see [Figure 10: Modality Worklist Screen](#_bookmark20)) displays all Consult Types currently configured to appear on the DICOM Modality Worklist when a Consult of that type is ordered. The display is updated as Consult Types are added to

> /edited/deleted from the Modality Worklist.

### Adding a Consult Type to the Modality Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new Consult Type to the Modality Worklist, click the Add button on the Modality Worklist Screen and the Add Modality Worklist Consult Type Screen appears.

![](vista-imaging-system-telereader-configurator-user-guide/015.png)

> Figure 11: Add Modality Worklist Consult Type Dialog

> The Add Modality Worklist Consult Type Dialog has the following three required fields and one optional field:

> Service Name: Service Name of the Consult Type to be added to the Modality Worklist.

> Specialty Index: Specialty Index of the Consult Type to be added to the Unread List.

> Acquisition Site: The Acquisition Site defaults to the login site.

> Clinic(s): The Clinic(s) list box can have one or more selections and is optional. For more instruction on how to add clinics read the section below.

> When a selection is made for all required fields, the Save button is enabled.

### Adding Clinics to a Modality Worklist Consult Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Adding Clinics to a Consult Type means that the information for an appointment scheduled at that clinic of that Consult Type will appear on the Modality Worklist. To add clinics to the Consult Type, click the Clinic List button and the Select Clinic(s) Dialog opens.

![](vista-imaging-system-telereader-configurator-user-guide/016.png)

> Figure 12: Select Clinic(s) Dialog

> The Select Clinic(s) Dialog has two list boxes. Available Clinics displays the list of Clinics that can be associated with the Consult Type. Selected Clinics will display Clinics as they are selected by the user to add to the Consult type.

> To select a Clinic to add to the Consult Type, from the Available Clinics listbox either double click on an item or select the item and click the ![](vista-imaging-system-telereader-configurator-user-guide/017.png) button. Those items will move from Available Clinics to Selected Clinics. To remove a Selected Clinic back to the Available Clinics list either double click the item in the Selected Clinics listbox or select it and click the ![](vista-imaging-system-telereader-configurator-user-guide/018.png) button.

> To save the selections click OK. The Select Clinic(s) dialog closes and the Clinic(s) listbox on the Add Modality Worklist Consult Type Dialog displays the selected Clinics.

### Editing a Modality Worklist Consult Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To edit the values of a Modality Worklist Consult Type, from the Modality Worklist Screen, select the Service Name then click the Edit button and the Edit Modality Worklist Consult Type Screen appears.

![](vista-imaging-system-telereader-configurator-user-guide/019.png)

> Figure 13: Edit Modality Worklist Consult Type Dialog

> The Edit Modality Worklist Consult Type Dialog populates with current values of the selected Consult Type. The Service Name combo box is disabled and cannot be changed. Once a change is made to the screen the Save button is enabled.

### Deleting a Modality Worklist Consult Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To delete a Modality Worklist Consult Type, on the Modality Worklist Screen, select the Service Name and click the Delete button. A dialog appears, asking the user for confirmation. The user can either Cancel the action or click OK to confirm the deletion of the Consult Type.

## Configuring a Reading Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure a Reading Site, from the TeleReader Configurator Main Screen page, click the Reading Site Setup button. This opens the Reader Setup Screen.

![](vista-imaging-system-telereader-configurator-user-guide/020.png)

> <span id="_bookmark26" class="anchor"></span>Figure 14: Reader Setup Screen

> The Reader Setup Screen has two pages. The Acquisition Sites page configures which Acquisition Sites’ Unread List local Readers have rights too. This is the default page when the screen is opened.

> The Readers page configures user level rights to Acquisition Sites’ Unread List.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/021.png)</p>
</blockquote></th>
<th><strong>NOTE: At the user level, rights are referred to as Privileges.</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Configuring Rights to Acquisition Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Acquisition Sites page displays all Acquisition Site Unread Lists for which local Readers have rights. The display is updated as Acquisition Site rights are added

> /edited/deleted for local Readers.

### Adding an Acquisition Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new Acquisition Site, click the Add button on the Acquisition Site page and the Add Acquisition Site Dialog appears.

> ![](vista-imaging-system-telereader-configurator-user-guide/022.png)

> Figure 15: Add Acquisition Site Dialog

> The Acquisition Site Dialog has the following four required fields:

> Acquisition Site: The acquisition site where the Unread List Consults were ordered.

> Acquisition Primary Site: The primary site of the acquisition site.

> Active: Status of the acquisition site. If the status is not active, local Readers will not be able to result Consults from that sites Unread List through TeleReader. The Active checkbox defaults to checked (the Rights to that site are active).

> Lock Timeout: Lock Timeout configures the amount of time (in minutes) a consult will remain locked on the Unread List before automatically unlocking.

> When all fields are completed, the Save button is enabled.

### Editing, Activating/Deactivating an Acquisition Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To edit the values or change the Active Status of an Acquisition Site, from the Acquisition Site page select the Site then click the Edit button and the Edit Acquisition Site Dialog appears.

> ![](vista-imaging-system-telereader-configurator-user-guide/023.png)

> Figure 16: Edit Acquisition Site Dialog

> The Edit Acquisition Site Dialog populates with the current values of the selected Acquisition Site. The Acquisition Site combo box is disabled and cannot be changed. Once a change is made to the screen the Save button is enabled. To deactivate the site to local Readers uncheck the Active check box. To reactivate the site at a later time, open the Edit Acquisition Site Dialog for the site and check to Active check box.

### Delete an Acquisition Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To delete an Acquisition Site, on the Acquisition Site page, select the Site and click the Delete button. A dialog appears, asking the user for confirmation. The user can either Cancel the action or click OK to confirm the deletion of the Acquisition Site.

### Configuring TeleReader Readers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure a reader for TeleReader from the Reader Setup screen (see [Figure 14:](#_bookmark26) [Reader Setup Screen](#_bookmark26)), click the Readers tab. The Readers/Privileges screen opens.

> ![](vista-imaging-system-telereader-configurator-user-guide/024.png)

> Figure 17: Reader Setup (Readers/Privileges Screen)

> The Readers/Privileges screen displays the list of readers configured to use TeleReader to review consults and the specialties/procedures assigned to them. Any reader who needs to use the TeleReader application must be configured on this page to have access to the unread list.

> The view can be collapsed by clicking the (-) button and by the clicking the (+) button. The screen opens with an expanded view by default.

> As readers and reader privileges are added/deleted/activated/inactivated the view is updated.

### Adding New TeleReader Readers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new Reader, from the Reader page, click the New Reader button and the Add New Reader Dialog appears.

> ![](vista-imaging-system-telereader-configurator-user-guide/025.png)

> Figure 18: Add New Reader Dialog

> The Add New Reader Dialog has the following four required fields and a Reader lookup edit box:

> Reader: When adding a new Reader, enter a partial last name (at least first 2 characters) in the first edit box and press ENTER. The Reader combo box drop down will be the populated with the list of matches against the last name string. The first match in the list (alphabetically) will default as the selection.

> Acquisition Site: The drop down list of sites will be those added to the Acquisition Site page.

> Specialty Index: Specialty Index of the that Acquisition sites Unread List Consult Type.

> Procedure/Event Index: The drop down list from the Procedure/Event Index combo box will be a subset of the selected Specialty Index.

> When all fields are completed, the Save button is enabled.

### Adding Additional Privileges to a Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To Add Privileges to an existing Reader select the appropriate Privilege from the screen view and click the Add Privileges button. The Add to Dialog opens.

> For example, to add a new Acquisition Site for a Reader, select the Reader on the view and click the Add Privilege button. To a new Specialty one of the Reader’s Acquisition Site, select the Acquisition Site then click the Add Privilege button. To Add a new Procedure to an Exiting Reader/Acquisition Site/Specialty select that Specialty.

> ![](vista-imaging-system-telereader-configurator-user-guide/026.png)

> <span id="_bookmark34" class="anchor"></span>Figure 19: Add to (Reader Privileges) Dialog

> In [Figure 19,](#_bookmark34) the user is adding a new Specialty to the Salt Lake City Acquisition Site for Reader Eye, Imager. That Privilege (Acquisition Site) and all higher level Privileges (Reader) are disabled and cannot be changed. Because the Reader cannot be changed, the Reader lookup edit box is disabled as well. When all required selections on the dialog are completed the Save button is enabled.

### Activate/Deactivate Privileges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To activate/deactivate a Privilege on the Readers/Privileges view, select the appropriate Privilege and click the Activate/Deactivate button. The button’s text will display Activate when the selected Privilege is inactive, and will display Deactivate when on an Active Privilege.

> Readers do not have an active status. When a Reader is selected, the Activate/Deactivate button will be disabled.

> <u>Explicit/Implicit Deactivation</u>

> When Deactivating an Active Privilege, then all Child Privileges will be deactivated as well. All Deactivated Privileges will have an icon change for their given node (Grayed out globe for Acquisition Site, Gray Pause button for Specialty Index, Procedure index). The explicitly Deactivated Privilege will have the text ‘\[INACTIVE\]’ appended to it. To Activate the Privilege and its Child Privileges select the appropriate node and click Activate. The Privilege and all Child Privilege will become Active with the icon

> changing (colored in globe, green play button) and the ‘\[INACTIVE\]’ text removed.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/027.png)</p>
</blockquote></th>
<th><p><strong>NOTE: If a Child Privilege had been explicitly deactivated at an earlier time, it will remain so, even after the Parent Privilege is activated until the</strong></p>
<p><strong>Child Privilege is explicitly activated.</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Deleting a Reader or Reader Privilege

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To Delete a Reader or Reader Privilege from the Reader Setup page, select that Reader/Reader Privilege and click the Delete button. A dialog appears, asking the user for confirmation. The user can either Cancel the action or click OK to confirm the deletion.

> If a Reader or Privilege is deleted, all sub Privileges are deleted as well. <u>Complete Privilege Set</u>

> Each Reader must have at least one Acquisition Site. Each Acquisition Site must have at least one Specialty. Each Specialty must have at least one Procedure. If deleting a Privilege makes a Reader or Parent Privilege incomplete, it will be deleted as well and the confirmation dialog message will state this. For example, if an Acquisition Site Privilege is deleted and is the only Site that Reader has then reader will be deleted as well.

![](vista-imaging-system-telereader-configurator-user-guide/028.png)

> <span id="_bookmark37" class="anchor"></span>Figure 20: Reader Privileges Delete Confirmation Dialog

### Cloning TeleReader Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once a reader profile is set up, a site administrator can clone the profile to provide consistent profiles for other readers who perform the same function.

> To clone a reader profile, from the TeleReader Configurator main screen, click the Reading Site Setup button.

> ![](vista-imaging-system-telereader-configurator-user-guide/029.png)

> Figure 21: TeleReader Configurator Main Screen

> The Reader Setup screen opens.

![](vista-imaging-system-telereader-configurator-user-guide/030.png)

> Figure 22: Reader Setup (Readers/Privileges Screen)

> From the Readers/Privileges tree view, select the reader whose privileges you want to clone. The reader is highlighted in blue. Click the Clone Reader button. The Select Readers to be Cloned screen opens.

> ![](vista-imaging-system-telereader-configurator-user-guide/031.png)

> Figure 23: Select Reader(s) to be Cloned Screen

> The Privileges to be cloned panel displays the site name and lists the privileges that will be cloned to new readers. In the Enter part of last name field, enter at least the first two characters of the last name of the reader to which you want to clone the selected privileges. The list of readers with no assigned privileges whose names match the search string populates in the Available Readers panel. Use the add arrow ( ![](vista-imaging-system-telereader-configurator-user-guide/032.png)) and the delete arrow ( ![](vista-imaging-system-telereader-configurator-user-guide/033.png)) to move readers from the Available Readers panel to the Selected Readers panel and vice versa. You can also move readers back and forth by double-clicking on the reader name, or selecting the name and pressing Ctrl + Enter.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/034.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE: If TeleReader Configurator does not find readers whose names match the search string you enter into the Enter Part of Last Name field, a No Matches Found dialog displays. To return to the previous screen and enter another search string, click the OK</strong></p>
<p><strong>button.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](vista-imaging-system-telereader-configurator-user-guide/035.png)Figure 24: No Matches Were Found Dialog

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-telereader-configurator-user-guide/036.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE: You cannot clone privileges to a reader with an existing TeleReader profile. You must delete that reader’s privileges first. For instructions about deleting a reader’s</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> privileges, see the section titled Deleting a Reader or a Reader Privilege.

> Complete the selection of readers to whom you want to clone the privileges. When the Selected Readers panel is populated, the OK button activates.

> Click OK to confirm the cloning. Click Cancel to cancel the cloning.

> A confirmation of cloning action dialog opens, listing the users for whom profiles will be created with the cloned profile.

![](vista-imaging-system-telereader-configurator-user-guide/037.png)

> Figure 25: Confirmation of Cloning Dialog

> Click OK to confirm the cloning. Click Cancel to cancel the cloning.

### Configuring TeleReader Global Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure Global Settings, from the TeleReader Configurator Main Screen (see Figure 2) click the Global Settings button. This opens the TeleReader Global System Settings Screen.

![](vista-imaging-system-telereader-configurator-user-guide/038.png)

> Figure 26: TeleReader Global System Settings Dialog

> At the time of this document, the only setting is TeleReader Timeout in minutes. This setting specifies how long the TeleReader application can stand idle on a desktop before it closes.

## Configuring TeleReader with a Thin Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> By default, the TeleReader application is restricted from running on a Thin Client workstation. This restriction can be overridden at various levels with the use of the MAG TR ALLOW THIN CLIENT parameter.

> To configure this parameter:

> 1\. In the VistA menu system, select Kernel menu option XPAR EDIT PARAMETER and parameter MAG TR ALLOW THIN CLIENT.

![](vista-imaging-system-telereader-configurator-user-guide/039.png)