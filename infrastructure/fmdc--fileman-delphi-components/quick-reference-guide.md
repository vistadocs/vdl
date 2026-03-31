---
title: FMDC Getting Started Guide
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: plain
doc_subject: 
app_code: FMDC
app_name: FileMan Delphi Components
section: INF
app_status: active
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
  - strong
  - fmdc
  - table
  - fileman
  - property
  - component
  - record
  - guide
  - components
  - contents
page_count: 0
word_count: 7552
section_count: 5
table_count: 34
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0gs.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0gs.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=6"
---

![](fmdc-getting-started-guide/001.png)

FILEMAN DELPHI COMPONENTS(FMDC)GETTING STARTED GUIDE

March 1998

VistA Health Systems Design & Development (HSD&D)

Development and Infrastructure Support (DaIS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 41%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>03/1998</td>
<td>1.0</td>
<td>Initial FileMan Delphi Components (FMDC) V. 1.0 software documentation creation.</td>
<td>FMDC Development Team, Oakland, CA OIFO</td>
</tr>
<tr class="odd">
<td>12/14/04</td>
<td>2.0</td>
<td>Reformatted manual to follow ISS Style Guide. Also, updated outdated information (e.g., Web site references).<br />
<br />
In addition, recreated PDF document to meet 508 compliance requirements.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of FileMan Delphi Components (FMDC) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                   |                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                        | Description                                                                                       |
| ![](fmdc-getting-started-guide/002.png)    | Used to inform the reader of general information including references to additional reading material. |
| ![](fmdc-getting-started-guide/003.png) | Used to caution the reader to take special notice of critical information.                            |

<span id="_Ref345831418" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type. The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

> Select Primary Menu option: ??

- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/005.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. Please refer to the *FileMan Delphi Components (FMDC) Technical Manual* for further information. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, the user is immediately returned to the point from which he/she started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in any VistA character-based product:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/006.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

It provides an overall explanation of configuring the FileMan Delphi Components (FMDC) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about the FileMan Delphi Components (FMDC) software should consult the following:

- *FileMan Delphi Components Installation Guide*
- *FileMan Delphi Components Technical Manual and Security Guide*
- *FileMan Delphi Components Getting Started Guide* (this Manual)
- *FileMan Delphi Components Help File*—Provides complete information on the FileMan Delphi Components (FMDC), including full listings of each component's methods and properties.

|                                                                                                                |                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/007.png) | For more information, please refer to the "FMDC.HLP Help File" chapter in this manual. |

- The FileMan Delphi Components (FMDC) Home Page at the following Web address:

> <http://vista.med.va.gov/fmdc/index.asp>

> The FileMan Delphi Components (FMDC) Web site provides up-to-date information including Frequently Asked Questions (FAQs), troubleshooting tips, and any code or documentation links/updates.

- *VA FileMan Programmer Manual*—Provides complete information on the VA FileMan Database Server (DBS) API. The FMDC data access components are wrappers around calls in the VA FileMan Database Server (DBS) API. Thus, having a DBS reference can be handy when you're working with data access components. An online version of this documentation is available at the following Web address:

> <http://vista.med.va.gov/fileman/docs/pm/index.asp>

VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

VistA documentation can be downloaded from the Enterprise VistA Support (EVS) anonymous directories or from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](fmdc-getting-started-guide/008.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/009.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
    - [FMDC Data Access Components](#fmdc-data-access-components)
    - [FMDC Custom Dialogues](#fmdc-custom-dialogues)
    - [FMDC Data Control Components](#fmdc-data-control-components)
    - [FMDC Object Hierarchy](#fmdc-object-hierarchy)
- [Quick Start Guide](#quick-start-guide)
- [How To: By VA FileMan Field Type](#how-to-by-va-fileman-field-type)
- [How To: By Task](#how-to-by-task)
    - [Selecting a Record](#selecting-a-record)
    - [Retrieving a Record](#retrieving-a-record)
    - [Providing Automated OnExit Processing for Controls](#providing-automated-onexit-processing-for-controls)
    - [Saving a Record](#saving-a-record)
    - [Editing Records from Several Files Simultaneously](#editing-records-from-several-files-simultaneously)
    - [Other "How To" Tasks](#other-how-to-tasks)
- [Using Data Access Components Directly](#using-data-access-components-directly)
    - [TFMGets: Retrieving a Record](#tfmgets-retrieving-a-record)
    - [TFMLister: Retrieving a List of Records](#tfmlister-retrieving-a-list-of-records)
    - [TFMValidator: Validating a Standalone Value](#tfmvalidator-validating-a-standalone-value)
    - [TFMFiler: Filing Standalone Values](#tfmfiler-filing-standalone-values)
    - [TFMFiler: Adding a Record](#tfmfiler-adding-a-record)
- [FMDC.HLP Help File](#fmdchlp-help-file)
  - [Index](#index)
This Getting Started Guide introduces developers to the FileMan Delphi Components (FMDC) Version 1.0. It aims to quickly get you started building Delphi applications that access VA FileMan data.
The FileMan Delphi Components make it easy for developers to work with VA FileMan data in Delphi applications. The components encapsulate the details of retrieving, validating and updating VA FileMan data within a Delphi application. This saves you from creating your own custom remote procedure calls (RPCs) when you need to access VA FileMan data.
The FileMan Delphi Components also include special enhanced features such as complete server-side error checking and data dictionary help.
If you're already familiar with Delphi, the time needed to develop an application to edit a set of VA FileMan fields using the FileMan Delphi Components is comparable to the time needed to create the same application using VA FileMan's roll-and-scroll ScreenMan interface.
The FileMan Delphi Components provide three types of components:
- Data Access Components are invisible to the user, but contain the functionality for calling the server to find, retrieve, validate, and file data. Each of the data access components encapsulates the functionality of one or more VA FileMan Database Server (DBS) calls.
- Custom Dialogues are like mini-applications you can include in your own application. The TFMLookUp custom dialogue makes it easy to perform lookups in files with large numbers of records.
- Data Controls are visual controls users can interact with to change data values. For example, a TFMCheckBox control is good for editing "Boolean" two-value set of codes fields; a TFMMemo control is good for editing word-processing fields; and a TFMEdit control is good for editing free text fields. Data controls are directly populated by the data access components. Values are directly validated and filed from the controls by the data access components.

### FMDC Data Access Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Component    | Icon                                                                                                                    | Function                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TFMGets      | ![](fmdc-getting-started-guide/010.png)      | Encapsulates the Data Retriever (GETS^DIQ) DBS call. Retrieves a record from the server. Populates any associated data controls with field values of the retrieved record.                                                                                         |
| TFMValidator | ![](fmdc-getting-started-guide/011.png) | Encapsulates the Validator (VAL^DIE) DBS call. Validates a data value against the corresponding VA FileMan field on the server. If any associated data control's coValOnExit flag is True, the TFMValidator automatically validates values entered in the control. |
| TFMFiler     | ![](fmdc-getting-started-guide/012.png)     | Encapsulates the Filer (FILE^DIE) and Updater (UPDATE^DIE) DBS calls. Given a list of data controls with values to file, the TFMFiler collects those values from the controls and files them.                                                                      |
| TFMLister    | ![](fmdc-getting-started-guide/013.png)    | Encapsulates the Lister (LIST^DIC) DBS call. Retrieves a list of records from the server. Optionally populates listbox-type data controls with the retrieved list.                                                                                                 |
| TFMHelp      | ![](fmdc-getting-started-guide/014.png)      | Encapsulates the Helper (HELP^DIE) DBS call. Retrieves field-based help from the data dictionary on the server. Can automatically display help for a data control's field in a panel, whenever a user sets focus on a data control.                                |
| TFMFinder    | ![](fmdc-getting-started-guide/015.png)    | Encapsulates the Finder (FIND^DIC) DBS call. Finds one or more records in a file that match a lookup value. Also used for lookups by TFMComboBoxLookUp and the TFMLookup custom dialogue.                                                                          |
| TFMFindOne   | ![](fmdc-getting-started-guide/016.png)  | Encapsulates the Single Record Finder (\$\$FIND1^DIC) DBS call. Finds a unique record in a file based on a lookup value; not linked with data controls.                                                                                                            |
<span id="_Toc90780647" class="anchor"></span>Table 1‑1: FMDC data access components

### FMDC Custom Dialogues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>![](fmdc-getting-started-guide/017.png) <strong>TFMLookUp</strong></p>
<p>The TFMLookUp custom dialogue makes it easier to do lookups in files with large numbers of records.</p></td>
<td>![](fmdc-getting-started-guide/018.png)</td>
</tr>
</tbody>
</table>
<span id="_Toc90780648" class="anchor"></span>Table 1‑2: FMDC custom dialogues

### FMDC Data Control Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 7%" />
<col style="width: 33%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Icon</strong></th>
<th><strong>Example</strong></th>
<th><strong>Use For</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TFMCheckBox</strong></td>
<td>![](fmdc-getting-started-guide/019.png)</td>
<td>![](fmdc-getting-started-guide/020.png)</td>
<td>"Boolean" two-value yes/no set of codes fields.</td>
</tr>
<tr class="even">
<td><strong>TFMComboBox</strong></td>
<td>![](fmdc-getting-started-guide/021.png)</td>
<td>![](fmdc-getting-started-guide/022.png)</td>
<td>Pointer fields, record lookups.</td>
</tr>
<tr class="odd">
<td><strong>TFMComboBoxLookUp</strong></td>
<td>![](fmdc-getting-started-guide/023.png)</td>
<td>![](fmdc-getting-started-guide/024.png)</td>
<td>Pointer fields, record lookups.<br />
Does on-the-fly lookups of what the user types in; good for longer lists.</td>
</tr>
<tr class="even">
<td><strong>TFMEdit</strong></td>
<td>![](fmdc-getting-started-guide/025.png)</td>
<td>![](fmdc-getting-started-guide/026.png)</td>
<td>Free Text, Numeric, Date and MUMPS fields.</td>
</tr>
<tr class="odd">
<td><strong>TFMLabel</strong></td>
<td>![](fmdc-getting-started-guide/027.png)</td>
<td>![](fmdc-getting-started-guide/028.png)</td>
<td>Computed fields, Read-only field values.</td>
</tr>
<tr class="even">
<td><strong>TFMListBox</strong></td>
<td>![](fmdc-getting-started-guide/029.png)</td>
<td>![](fmdc-getting-started-guide/030.png)</td>
<td>Pointer fields, record lookups.</td>
</tr>
<tr class="odd">
<td><strong>TFMMemo</strong></td>
<td>![](fmdc-getting-started-guide/031.png)</td>
<td>![](fmdc-getting-started-guide/032.png)</td>
<td>Word-processing fields.</td>
</tr>
<tr class="even">
<td><strong>TFMRadioButton</strong></td>
<td>![](fmdc-getting-started-guide/033.png)</td>
<td>![](fmdc-getting-started-guide/034.png)</td>
<td>Set of codes fields.</td>
</tr>
<tr class="odd">
<td><strong>TFMRadioGroup</strong></td>
<td>![](fmdc-getting-started-guide/035.png)</td>
<td>![](fmdc-getting-started-guide/036.png)</td>
<td>Set of codes fields.</td>
</tr>
</tbody>
</table>
<span id="_Toc90780649" class="anchor"></span>Table 1‑3: FMDC data control components

### FMDC Object Hierarchy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](fmdc-getting-started-guide/037.png)
<span id="_Toc90780650" class="anchor"></span>Figure 1‑1: FMDC object hierarchy

# Quick Start Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Quick Start Guide demonstrates the basic approach to editing data with the FileMan Delphi Components. This approach only uses a subset of the properties, methods and components in the FileMan Delphi Components.

There are 17 FileMan Delphi Components, and each one has a variety of methods and properties that allow you to fine-tune its behavior. However, a basic approach to using them, involving only a subset of their properties and methods, is appropriate for most data editing situations.

To follow this basic approach: First, determine the set of fields you want to edit in your Delphi application. Then follow this Quick Start Guide to provide that access in your Delphi application.

To edit records in a given VA FileMan file with the FileMan Delphi Components:

> 1\. Establish an RPC Broker connection:

a\. Add a TRPCBroker component to your form.

b\. Set its properties and invoke its methods as necessary to connect to a server system.

> 2\. Add a TFMGets component to retrieve data:

a\. Add a TFMGets component to your form.

b\. Set its RPCBroker property to point to your form's TRPCBroker component.

c\. Set its FileNumber property to the file containing records to retrieve.

> 3\. Add a TFMFiler component to file changes:

a\. Add a TFMFiler component to your form.

b\. Set its RPCBroker property to point to your form's TRPCBroker component.

> 4\. Add a TFMValidator component to provide validation services:

a\. Add a TFMValidator component to your form:

b\. Set its RPCBroker property to point to your form's TRPCBroker component.

> 5\. Add VA FileMan data controls for each field:

a\. For each field to edit, add data control(s) and supporting data access components to your form as follows:

| For this Field Type:     | Add to Your Form:                                 |
|------------------------------|-------------------------------------------------------|
| Free Text, Numeric, Date | 1 TFMEdit                                             |
| "Boolean" Set of Codes   | 1 TFMCheckBox                                         |
| Set of Codes             | 1 TFMRadioGroup, or                                   |
|                              | 1 TPanel or TGroupBox, plus 1 TFMRadioButton per code |
| Word-processing          | 1 TFMMemo                                             |
| Pointer                  | 1 TFMLister and 1 TFMListBox, or                      |
|                              | 1 TFMLister and 1 TFMComboBox, or                     |
|                              | 1 TFMLister and 1 TFMComboBoxLookUp                   |
| Computed                 | 1 TFMLabel                                            |

<span id="_Toc90780651" class="anchor"></span>Table 2‑1: Field types and data controls on a form

b\. For each field that you add component(s) for, set the field-type-specific properties of the components according to the guidelines (listed by field type) in the "How To: By VA FileMan Field Type" chapter in this manual.

> 6\. Select and retrieve a record:

a\. To select a record, follow the procedure in the "Selecting a Record" section below in the "How To: By Task" chapter. You'll add a TFMLookUp and TFMLister component to your form, and add a button that calls TFMLookup's Execute method to perform the lookup.

b\. TFMLookUp.Execute returns a record number. Using it you can retrieve the record and populate your data controls with the record's field values. To retrieve the record, follow the procedure in the "Retrieving a Record" section below in the "How To: By Task" chapter. You'll call TFMGets' GetAndFill method to retrieve the record and populate data controls.

c\. The OnClick event handler for the button that executes the TFMLookup.Execute method (Step \#6a) can also perform the retrieval (Step \#6b). Code to do this would look like:

> procedure TForm1.Button1Click(Sender: TObject);

> var AddRecord:Boolean;

> begin

> if FMLookup1.Execute(AddRecord) then begin

> FMGets1.IENS:=FMLookUp1.RecordNumber+',';

> // Call any TFMListBox/TFMComboBox GetList methods

> // here, before calling GetAndFill.

> FMGets1.GetAndFill;

> end

> else

> ShowMessage('No record chosen.');

> end;

> <span id="_Toc90780652" class="anchor"></span>Figure 2‑1: TFMLookUp—Sample OnClick even handler code

|                                                                                                                          |                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| ![](fmdc-getting-started-guide/038.png) | *Compile your application. You can now retrieve records.* |

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 2%" />
<col style="width: 43%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7. Set Up Automated OnExit Processing:</p>
</blockquote>
<p>a. Your data controls should already be linked to a TFMFiler and a TFMValidator component, from following the "Data Control Property Settings for All Field Types" guidelines in the "How To: By VA FileMan Field Type" chapter in this manual.</p>
<p>b. Set every data control's <strong>coValOnExit</strong> value to True, in each control's <strong>FMCtrlOptions</strong> property.</p></td>
<td></td>
<td><p><strong>About Automated OnExit Processing</strong></p>
<p>This feature automatically validates a field value in a data control when a user changes it (this is the control's OnExit event). If the changed value is valid, automated OnExit processing adds the control to the associated TFMFiler's component's list of controls to file.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                          |                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/039.png) | *Compile your application. All changes to fields in VA FileMan data controls will be validated, and only accepted by the data controls if valid.* |

> 8\. Provide an event to save changes:

a\. To save changes the user makes to the record, follow the procedure in the "Saving a Record" section below in the "How To: By Task" chapter. You'll add a button whose caption is something like "Save Changes". You'll add code for this button's OnClick event handler that calls your TFMFiler's Update method to file changes.

|                                                                                                                          |                                                                    |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/040.png) | *Compile your application. You can now file changes to the record* |

> 9\. (optional) Provide context-sensitive field help.

> There are several ways you can provide context-sensitive help for the VA FileMan fields being edited:

- The first line of the DD help for a field can automatically be displayed in a display panel, whenever a user sets focus to a control.
- All DD help for a field can be displayed when, with a particular control selected, the user presses F1.
- Standalone help: you can retrieve DD help for any field and display it using your own methods.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/041.png) | For more information on providing context-sensitive help, please refer to the "FMDC.HLP Help File" chapter in this manual. |

<table>
<colgroup>
<col style="width: 74%" />
<col style="width: 2%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10. Register your application:</p>
</blockquote>
<p>a. Create a "B"-type option in the Option file for your application.</p>
<p>b. In the option's RPC multiple, include every Remote Procedure Call (RPC) your application calls.<br />
<br />
You need to include all RPCs invoked by methods of the FileMan Delphi Components called by your application, as well as RPCs you invoke yourself. The FMDC.HLP online help file details which FMDC RPCs are called by FMDC component methods.</p>
<p>c. In your application's OnCreate event, register the option name using the broker's CreateContext method. If registration fails, your application should probably terminate. For example:</p>
<blockquote>
<p><strong>if not</strong> RPCBroker1.CreateContext('A6A APP1')</p>
<p><strong>then</strong> Application.Terminate;</p>
</blockquote>
<p>d. Users must have the registered "B"-type option assigned to them in order to use your client application.</p></td>
<td></td>
<td><p>Bypass Security During Development.</p>
<p>Possessing the XUPROGMODE key allows you as a developer to bypass RPC Broker security.</p>
<p>Once you're ready to deploy your application to non-developer users, your application will need to register itself appropriately.</p>
<p>![](fmdc-getting-started-guide/042.png) For more information on RPC Broker security, please refer to the RPC Broker documentation.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                          |                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/043.png) | *Compile your application. Users without the XUPROGMODE key should now be able to run your application.* |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](fmdc-getting-started-guide/044.png)</td>
<td><p>The FMDC data access components are wrappers around calls in the VA FileMan Database Server (DBS) API. So having a DBS reference can be handy when you're working with data access components. For a complete DBS reference, please refer to the <em>VA FileMan Programmer Manual</em>. Online versions of this documentation are available on the VDL:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/Infrastructure.asp?appID=5">http://www.va.gov/vdl/Infrastructure.asp?appID=5</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

# How To: By VA FileMan Field Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter shows which VA FileMan data controls are compatible with which VA FileMan field types, and how to set the properties of the data controls.

For each VA FileMan data control you use on your form to edit a particular VA FileMan field type, follow the corresponding procedure in this chapter to set the control's properties.

VA FileMan Field Types and Compatible Controls

| Field Type   | Compatible Controls                                                        |
|------------------|--------------------------------------------------------------------------------|
| Computed         | TFMEdit, TFMLabel                                                              |
| Date             | TFMEdit, TFMLabel                                                              |
| Free Text        | TFMEdit, TFMLabel                                                              |
| MUMPS            | TFMEdit, TFMLabel                                                              |
| Numeric          | TFMEdit, TFMLabel                                                              |
| Pointer          | TFMComboBox, TFMComboBoxLookUp, TFMListBox, TFMEdit, TFMLookUp custom dialogue |
| Set of Codes     | TFMCheckBox, TFMRadioButton, TFMRadioGroup, TFMEdit                            |
| Variable Pointer | (must be done manually)                                                        |
| Word-processing  | TFMMemo                                                                        |

<span id="_Toc90780653" class="anchor"></span>Table 3‑1: VA FileMan field types and compatible controls

Data Control Property Settings for All Field Types

<table style="width:100%;">
<colgroup>
<col style="width: 69%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 22%" />
<col style="width: 0%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Set these properties for every VA FileMan data control you use.</p>
<blockquote>
<p>1. Set the <strong>FMField</strong> and <strong>FMFile</strong> properties to the field and file that the control is to edit.</p>
<p>2. Set the <strong>FMGets</strong> property to the TFMGets to use to retrieve values.</p>
<p>3. Set the <strong>FMValidator</strong> property to the TFMValidator to use to validate (except for TFMMemo controls, which do not require validation).</p>
<p>4. Set the <strong>FMFiler</strong> property to the TFMFiler to use to file changes.</p>
<p>5. (optional) Set the <strong>FMCtrlOptions</strong> coValOnExit flag to True to enable automated OnExit processing. For more information, please refer to the "Providing Automated OnExit Processing for Controls" topic.</p>
</blockquote></td>
<td></td>
<td colspan="2"><p><strong>Hint</strong></p>
<p>In Delphi, to set a property for a set of controls to the same value, select all of the components simultaneously (Hold down the Ctrl key and select each control).</p>
<p>Then, in Delphi's Object Inspector, in a single edit of that property you set the property value for all selected controls.</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><p>Free Text, Numeric, Date, MUMPS: TFMEdit</p>
<blockquote>
<p>1. Add a <strong>TFMEdit</strong> component to your form.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
</blockquote></td>
<td colspan="2"><p>TFMEdit:</p>
<p>![](fmdc-getting-started-guide/045.png)</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><p>"Boolean" Set of Codes (2 Yes/No Values): TFMCheckBox</p>
<blockquote>
<p>1. Add a <strong>TFMCheckBox</strong> component to your form.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Set its <strong>FMValueChecked</strong> and <strong>FMValueUnchecked</strong> properties to the two internal codes (from the VA FileMan data dictionary) that should be represented by the checked and unchecked states of the control.</p>
<p>4. Set the <strong>Caption</strong> property to the label to display to the end-user (typically the external value represented by the "True" internal code).</p>
</blockquote></td>
<td colspan="3"><p>TFMCheckBox:</p>
<p>![](fmdc-getting-started-guide/046.png)</p></td>
</tr>
<tr class="even">
<td colspan="3"><p>Multi-value Set of Codes: TFMRadioGroup</p>
<blockquote>
<p>1. Add a <strong>TFMRadioGroup</strong> component to your form.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Populate its <strong>Items</strong> property (an array of TStrings) with the values to display to the user for each code.</p>
<p>4. Populate its <strong>FMInternalCodes</strong> property with the <strong>internal</strong> values (from the VA FileMan data dictionary) of the codes in the set of codes field. Populate it in the same sequence, line-by-line and code-by-code, with which you populated the Items property.</p>
</blockquote></td>
<td colspan="3"><p>TFMRadioGroup:</p>
<p>![](fmdc-getting-started-guide/047.png)</p></td>
</tr>
<tr class="odd">
<td colspan="3"><p>Multi-value Set of Codes: TFMRadioButton</p>
<blockquote>
<p>1. Place a <strong>TPanel</strong> or <strong>TGroupBox</strong> panel component on your form.</p>
<p>2. Place one <strong>TFMRadioButton</strong> per code directly from the component palette onto the TPanel or TGroupBox. For example, for a 3-value set of codes field, place 3 TFMRadioButtons directly from the component palette onto the TPanel or TGroupBox.</p>
<p>3. Set each TFMRadioButton's properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>4. Set each TFMRadioButton's <strong>FMValueChecked</strong> property to the internal code (from the VA FileMan data dictionary) that should be represented by the checked state of the control.</p>
<p>5. Set each TFMRadioButton's <strong>Caption</strong> property to the label to display to the end-user (typically the external value represented by each code).</p>
</blockquote></td>
<td colspan="3"><p>TFMRadioButton:</p>
<p>![](fmdc-getting-started-guide/048.png)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 66%" />
<col style="width: 3%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p>Pointer: TFMComboBox, TFMListBox</p>
<blockquote>
<p>1. Add a <strong>TFMComboBox</strong> or <strong>TFMListBox</strong> to your form. These work best when the set of records is not huge.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Add a <strong>TFMLister</strong> component to your form. It must be dedicated entirely to servicing the pointer field.</p>
<p>4. Set the TFMLister's <strong>FileNumber</strong> property to that of the <strong>pointed-to</strong> file. Make sure its <strong>FieldNumbers</strong> property contains at least ".01". Set its <strong>RPCBroker</strong> property to your form's TRPCBroker.</p>
<p>5. Associate the TFMListBox or TFMComboBox with the TFMLister through the <strong>FMLister</strong> property.</p>
<p>6. To retrieve the current value of the pointer field: <strong>First</strong> use the control's GetList method to populate its Items property with pointed-to file's list of records. <strong>Then</strong> use the GetAndFill method of the associated TFMGets component to select the current pointer value from the list of possible values.</p>
</blockquote></td>
<td><p>TFMComboBox:</p>
<p>![](fmdc-getting-started-guide/049.png)</p>
<p>TFMListBox:</p>
<p>![](fmdc-getting-started-guide/050.png)</p></td>
</tr>
<tr class="even">
<td colspan="2"><p>Pointer: TFMComboBoxLookUp</p>
<blockquote>
<p>1. Add a <strong>TFMComboBoxLookUp</strong> to your form. This control performs lookups "on-the-fly" (the entire list of possible records does not have to be retrieved into the control).</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Add a <strong>TFMLister</strong> component to your form. It must be dedicated entirely to servicing the pointer field.</p>
<p>4. Set the TFMLister's <strong>FileNumber</strong> property to that of the <strong>pointed-to</strong> file. Make sure its <strong>FieldNumbers</strong> property contains at least ".01". Set its <strong>RPCBroker</strong> property to the TRPCBroker component on your form.</p>
<p>5. Optionally set the TFMLister's <strong>Number</strong> property to restrict the number of records returned in any one lookup when the user enters "<strong>?</strong>" or leaves the edit box null and presses the down-arrow. This enables a "&lt;&lt;&lt; More &gt;&gt;&gt;" item at the end of the Items list so the user can request more records if needed.</p>
<p>6. Associate the TFMComboBoxLookUp with the TFMLister through its <strong>FMLister</strong> property.</p>
<p>7. You don't need to populate the TFMComboBoxLookUp's Items property prior to calling GetAndFill, because lookups are performed on the fly.</p>
<p>8. Because TFMComboBoxLookUp performs server-side calls automatically you application will need to register the DDR LISTER and DDR FINDER RPCs.</p>
<p>![](fmdc-getting-started-guide/051.png) For more information on registering RPCs, please refer to the RPC Broker documentation on the VDL:</p>
<p><a href="http://www.va.gov/vdl/Infrastructure.asp?appID=23">http://www.va.gov/vdl/Infrastructure.asp?appID=23</a></p>
</blockquote></td>
<td><p>TFMComboBoxLookUp:</p>
<p>![](fmdc-getting-started-guide/052.png)</p></td>
</tr>
<tr class="odd">
<td colspan="3"><p>Pointer: TFMLookUp</p>
<p>You can also edit pointer fields with the TFMLookUp custom dialogue. This can be useful if the pointer field points to a file with a huge number of records; the TFMLookUp custom dialogue simplifies lookups in large files.<br />
<br />
Use a VA FileMan data control such as <strong>TFMLabel</strong> or <strong>TFMEdit</strong> to display the current value of the pointer field. If you use TFMEdit you should set its ReadOnly property set to True. Then a button you place next to the control could invoke the <strong>Execute</strong> method of <strong>TFMLookUp</strong> to edit the value of the pointer field.</p>
<p>![](fmdc-getting-started-guide/053.png) For a complete list of steps and a code sample, please refer to the online FMDC.HLP help file.</p></td>
</tr>
<tr class="even">
<td><p>Word-processing: TFMMemo</p>
<blockquote>
<p>1. Add a <strong>TFMMemo</strong> component to your form.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Make sure you set its <strong>FMFile</strong> property to the file number of the file containing the word-processing field, and <strong>FMField</strong> to the word-processing field number. Don't use the subfile number of the word-processing field.</p>
</blockquote></td>
<td colspan="2"><p>TFMMemo:</p>
<p>![](fmdc-getting-started-guide/054.png)</p></td>
</tr>
<tr class="odd">
<td><p>Computed: TFMLabel or TFMEdit</p>
<blockquote>
<p>1. Add a <strong>TFMLabel</strong> or <strong>TFMEdit</strong> component to your form.</p>
<p>2. Set its properties as described in the "Data Control Property Settings for All Field Types" topic above.</p>
<p>3. Unlike other field types, no automated OnExit processing or filing is needed for computed fields since they are read-only.</p>
<p>4. If you are using a TFMEdit control, set its <strong>ReadOnly</strong> property to True, so users don't think that they can edit the field (and so that filing is never attempted).</p>
</blockquote></td>
<td colspan="2"><p>TFMLabel:</p>
<p>![](fmdc-getting-started-guide/055.png)</p>
<p>TFMEdit:</p>
<p>![](fmdc-getting-started-guide/056.png)</p></td>
</tr>
</tbody>
</table>

# How To: By Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter demonstrates how to accomplish the most common VA FileMan record-editing tasks.

### Selecting a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The procedure below describes how to select a record with the TFMLookUp custom dialogue.

|                                                                                                                |                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/057.png) | For additional ways to select records, please refer to the FMDC.HLP help file. |

To select a record with a TFMLookUp component:

> 1\. Add a TFMLister component to your form.

> 2\. Set the TFMLister's RPCBroker property to point to your form's TRPCBroker component.

> 3\. Set the TFMLister's FileNumber property to the file to do the lookup in.

> 4\. Optionally set the TFMLister's Number property to restrict the number of records returned when the TFMLookUp window is first opened (particularly for files with large numbers of records). Setting this property enables the TFMLookUp More button so that the user can request more records if needed.

> 5\. Add a TFMLookUp component to your form.

> 6\. Set the TFMLookUp's FMLister property to the TFMLister.

> 7\. Add a button to your form so the user can do a lookup. Set the button's Caption to something the user will recognize, e.g. "Choose User" if you're doing a lookup in the NEW PERSON file (#200).  

> The button's OnClick event should call the Execute method of the TFMLookUp component to do the lookup. It can make the retrieved record number, if any, available to a TFMGets component so that the TFMGets is ready to retrieve the record (see the "Retrieving a Record" topic). For example:

procedure TForm1.Button1Click(Sender: TObject);  
var

AddRecord :Boolean;begin  
FMLookUp1.AllowNew:=False; // disallow adding records  
if FMLookUp1.Execute(AddRecord) then  
TFMGets1.IENS:=FMLookUp1.RecordNumber+','  
else  
ShowMessage('You did not select a record.');  
end;

> <span id="_Toc90780654" class="anchor"></span>Figure 4‑1: Sample of code from the TFMLookUp Execute method

### Retrieving a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To retrieve a record from the server, use the TFMGets component. Its GetAndFill method retrieves fields from a record on the server and populates a set of associated data controls with the retrieved values.

The following should be set prior to calling the code example below:

- TFMGets.FileNumber should be set to the file from which to retrieve the record.
- All data controls should be associated with the TFMGets component (through their FMGets properties).
- All data controls' FMFile and FMField properties should be set to reflect the file and field number that they should be editing.

The following code retrieves a record and populates the associated controls with appropriate field values:

// Set TFMGets.IENS to IENS (#+',' for top-level records)

// of the record to retrieve

FMGets.IENS:=TFMLookup1.RecordNumber+',';

// if you have TFMListBox or TFMComboBox controls to get lists for,

// get the lists here before calling GetAndFill.

FMListBox1.Getlist;

// Now you can call TFMGets.GetAndFill.

FMGets1.GetAndFill;

// Check for errors after the server call.

if FMGets1.ErrorList.Count\>0 then FMGets1.DisplayErrors;

> <span id="_Toc90780655" class="anchor"></span>Figure 4‑2: Sample code to retrieve a record and populate controls

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 2%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](fmdc-getting-started-guide/058.png) The Items property of TFMListBox and TFMComboBox controls must be populated <strong>before</strong> calling TFMGets.GetAndFill. Do this by calling the GetList method of the data control before calling GetAndFill. Then GetAndFill can retrieve the current field value, and select the corresponding value in the control's Items property as the control's current value.</td>
<td></td>
<td><p><strong>About Error Checking</strong></p>
<p>Error checking is provided for each of the data access components. Whenever the data access components make a server call (invoking an M routine on the server) there is the potential for an error to occur on the server side, due to a variety of conditions in the server environment.</p>
<p>You should check a data access component's ErrorList.Count property after making a server call to see if a server-side error occurred. If any did, you can call the component's DisplayErrors method to display those errors to the user (typically the error number and text from a DBS error is what is displayed), and then branch accordingly to gracefully handle the error condition.</p></td>
</tr>
</tbody>
</table>

### Providing Automated OnExit Processing for Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each time a user enters a data value in a data control, there is a set of tasks you would typically perform:

> 1\. Check if the user changed the data value.

> 2\. If the control's FMRequired property is True, and the user deleted the data value, warn the user that the value is required, and reset the control's value to its previous state.

> 3\. Otherwise, validate the changed value (usually needed only for TFMEdit controls):

> a\. If the value is invalid, return the control's value to the original and provide the user help on why the value was invalid.

> b\. If the value is valid, update the control's display value from what user typed to validated external form of field value, if necessary.

> 4\. If the value is valid, update the control's FMCtrlInternal and FMCtrlExternal properties to reflect the internal and external VA FileMan forms of the control's value (except for TFMMemo controls).

> 5\. Unless the changed value is invalid, tell the associated TFMFiler that the control has data to file (with the TFMFiler's AddChgdControl method).

A good place to perform these actions is in a control's OnExit event handler. Coding these actions by hand for each of your data controls would be laborious. Fortunately, the VA FileMan data controls have an Automated OnExit processing option you can turn on to perform each of these tasks automatically.

To turn on Automated OnExit Processing:

> 1\. Make sure each of your VA FileMan data controls is linked to a TFMFiler component through their FMFiler properties.

> 2\. Make sure each of your VA FileMan data controls is linked to a TFMValidator component through their FMValidator properties (except TFMMemo, which does not need validation).

> 3\. Set every data control's coValOnExit value in the FMCtrlOptions property to True.

When Control Values are changed by Code

If a control's value is changed by code (rather than through user interaction) the OnExit event of the control is not triggered. Automated OnExit processing is not triggered either. In this case, your code will need to perform any actions that you would ordinarily expect to be performed by automated OnExit processing.

### Saving a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save changes to the database, use the TFMFiler component. You can add filing requests with its AddFDA and AddChgdControl methods, and file all pending requests with its Update method.

To request filing:

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 2%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>Call a TFMFiler's AddFDA method to request filing a standalone field value (not attached to a control).</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Call a TFMFiler's AddChgdControl method to request filing a field value in a VA FileMan data control.</p>
</blockquote></li>
</ul></td>
<td></td>
<td><p><strong>Hint</strong></p>
<p>If you are using automated OnExit processing, the AddChgdControl method is automatically called when a user changes the value in a VA FileMan data control to a valid new value.</p></td>
</tr>
</tbody>
</table>

To file all accumulated filing requests to the database, call the TFMFiler's Update method.

To save accumulated filing requests:

> 1\. Provide some event that the user can trigger to save changes. The OnClick event of a "Save Changes" button is one good place.

> 2\. Provide code for this event that will save the changes to the server. This code should:

a\. (optional) Check if there are any data updates waiting to be filed (TFMFiler's AnythingToFile method). Because the Update method also calls AnythingToFile, your code only needs to call AnythingToFile if that code needs to know if changes are waiting to be filed.

b\. If you designated any controls as required with the FMRequired property, call the TFMFiler's DataProblemCheck method to check that all required controls have values.

c\. If no problems are found, call the TFMFiler's Update method to file the accumulated changes.

d\. If Update fails, call the TFMFiler's DisplayErrors method to display error information to the end-user.

> For example:

if FMFiler1.AnythingToFile then  
if FMFiler1.DataProblemCheck then  
FMFiler1.ProcessDataProblemList  
else  
if FMFiler1.Update then  
ShowMessage('Changes filed!')  
else  
 FMFiler1.DisplayErrors  
else  
ShowMessage('No changes to file!');

> <span id="_Toc90780656" class="anchor"></span>Figure 4‑3: TFMFiler—Sample code calling DisplayErrors method

### Editing Records from Several Files Simultaneously

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous chapters describe how to edit a set of fields from a single VA FileMan file. Often, however, you may need to edit sets of fields from several related records in different VA FileMan files simultaneously. To do this:

| Data Controls | Set each data control's FMFile and FMField property to reflect the file and field to edit.                                                                                                                                                                                                                                                                                     |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TFMGets       | Use one TFMGets component for each file you need to retrieve records for. Set the FMGets property of each data control to the TFMGets component you're using to retrieve records for that file.                                                                                                                                                                                |
| TFMValidator  | Use one TFMValidator component for all data controls, regardless of file and field being edited.                                                                                                                                                                                                                                                                               |
| TFMFiler      | If the set of fields from several files is to be filed simultaneously, and there are no dependencies between records, use a single TFMFiler to file all fields for one or more files. Otherwise, use a separate TFMFiler for each file you need to save records to. Set the FMFiler of each data control to the TFMFiler component you're using to save records for that file. |

### Other "How To" Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some other tasks within the scope of editing VA FileMan data in Delphi applications are not addressed in this Getting Started Guide. For help on these and other issues, please refer to the online FMDC.HLP help file:

- Selecting records with TFMListBox, TFMComboBox, TFMComboBoxLookUp, or TFMFindOne.
- Retrieving records with TFMFinder.
- Retrieving and filing data that is in multiples.
- Providing manual OnExit processing for VA FileMan data controls.
- Providing context-sensitive DD field help for data controls.
- Adding new records using VA FileMan controls or TFMLookUp.
- Deleting Records.

# Using Data Access Components Directly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous chapters in this guide demonstrate using the VA FileMan data access components in conjunction with the VA FileMan data controls.

You can also use the VA FileMan data access components directly to retrieve, validate and file VA FileMan data, without involving any VA FileMan data controls.

### TFMGets: Retrieving a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the TFMGets.GetData method to retrieve one or more field values from a specified record. The field values are returned in the TFMGets.Results property as follows:

![](fmdc-getting-started-guide/059.png)

<span id="_Toc90780657" class="anchor"></span>Figure 5‑1: TFMGets sample returned data

Each field is retrieved into a TFMFieldObj object, whose structure is:

| Object          | Description                                     |
|---------------------|-----------------------------------------------------|
| FldObj.IENS         | string (IENS of record).                            |
| FldObj.FMField      | string (field number)                               |
| FldObj.FMDBExternal | string (external field value if requested)          |
| FldObj.FMDBInternal | string (internal field value if requested)          |
| FldObj.FMWordProc   | boolean (if True, field is a word-processing field) |
| FldObj.FMWPTextLine | TStrings (Word-processing field lines)              |

<span id="_Toc90780658" class="anchor"></span>Table 5‑1: TFMFieldObj—Structure description

To retrieve a record without populating VA FileMan data controls:

> 1\. Add a TFMGets component to your form.

> 2\. Set its RPCBroker property to your form's TRPCBroker component.

> 3\. Set its FileNumber property to the file containing records to retrieve.

> 4\. Set its FieldNumbers property to contain all fields to retrieve. You can set the property directly or use the AddField method.

> 5\. Set its IENS property to the IENS of the record to retrieve.

> 6\. Call the GetData method to retrieve the record into the Results property.

> 7\. Access each field's retrieved TFMFieldObj object with the GetField method. For example:

> MyFldObj:=FMGets1.GetField('.01');

### TFMLister: Retrieving a List of Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the TFMLister.GetList method directly to retrieve a set of records. The set of records is returned in the TFMLister's Results property, which is a TStrings object. The format of returned data is as follows:

![](fmdc-getting-started-guide/060.png)

<span id="_Toc90780659" class="anchor"></span>Figure 5‑2: TFMLister—Sample returned data

The structure of each returned TFMRecordObj is:

| Object                | Description                                                 |
|---------------------------|-----------------------------------------------------------------|
| RecObj.IEN                | IEN of the record.                                              |
| RecObj.FMFldValues        | TFMFieldObj objects for fields requested in FieldNumbers.       |
| RecObj.FMIXExternalValues | external form of index value(s) (TFMLister only) if requested.  |
| RecObj.FMIXInternalValues | internal form of index value(s) (TFMLister only) if requested.  |
| RecObj.FMWIDValues        | Write Identifier of a file and the Identifier parameter result. |
| RecObj.Objects            | Place to associate your own object.                             |

<span id="_Toc90780660" class="anchor"></span>Table 5‑2: TFMRecordObj—Structure description

To retrieve a list of records with TFMLister:

> 1\. Add a TFMLister component to your form.

> 2\. Set its RPCBroker property to the TRPCBroker component your form is using.

> 3\. Set the TFMLister's FileNumber property to the file or subfile number to retrieve records from. If retrieving from a subfile, use the IENS property to indicate the full path to the subfile.

> 4\. Set the FieldNumbers property to the fields to retrieve with each record.

> 5\. To use any of the optional parameters for the LIST^DIC call that affect how records are retrieved, set the corresponding property in the TFMLister component (ListerFlags, FMIndex, Identifier, PartList, and Screen).

> 6\. Set any of the options controlling the TFMLister component with the ListerOptions property.

> 7\. You can limit the number of records returned in any one call with the Number property. If you need to retrieve more records, you'll need to use the TFMLister's GetMore method.

> 8\. Invoke the TFMLister component's GetList method to retrieve records. The list of records returned in the Results property of the TFMLister. If you pass a TStrings object as a parameter to the GetList method, that list is also populated.

> 9\. You can access the TFMRecordObj object and TFMFieldObj objects returned for a particular record (based on IEN) with the GetRecord and GetField functions as follows:

> MyRecordObj:=TFMLister1.GetRecord(IEN);

> MyFieldObj:=MyRecordObj.GetField('.01');

> MyFieldExternal:=MyFieldObj.FMDBExternal;

### TFMValidator: Validating a Standalone Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the TFMValidator directly to validate any given value in the context of a given file, field number and IENS.

To validate a standalone value:

> 1\. Add a TFMValidator component to your form.

> 2\. Set its RPCBroker property to the TRPCBroker component your form is using.

> 3\. Set the TFMValidator component's FieldNumber, FileNumber, IENS, and Value properties directly to reflect the value to validate, and the context in which to validate it. Value should be in the form as would be input by a user (not internal form!). Alternatively you can call the TFMValidator's Setup method to set these properties.

> 4\. Call the Validate method of the TFMValidator. Results of the validation are returned in TFMValidator's Results property, in the format:

> Results\[0\]: Internal VA FileMan form of value if input Value was valid, otherwise "^".  
> Results\[1\]: External VA FileMan form of value if input Value is valid.

### TFMFiler: Filing Standalone Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the TFMFiler directly to file any given value to a specified VA FileMan file, field and record.

To file standalone values:

> 1\. If you want to pre-validate the value to file, follow the steps in the "Validating a Standalone Value" section above.

> 2\. Use the TFMFiler's AddFDA method to request filing for a given value. You pass as parameters to this method the values that would comprise a VA FileMan Database Server (DBS) FDA: FileNumber, IENS, FieldNumber and Value (internal). For example:

FMFiler1.AddFDA('49','+1,','.01',NewName);

<span id="_Toc90780661" class="anchor"></span>Figure 5‑3: TFMFiler—AddFDA method

> Call the Update method of the TFMFiler to file the value. This method returns True if filing was successful, or False if one or more errors were encountered on the server. You can use the return value as follows in code to branch to an error handler:

if FMFiler1.Update then

ShowMessage('Changes filed!')

else

FMFiler1.DisplayErrors;

> <span id="_Toc90780662" class="anchor"></span>Figure 5‑4: TFMFiler—Sample code branching to error handler

### TFMFiler: Adding a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several ways you can add a new record to a file. This section describes how to add a record using the TFMFiler.AddFDA method.

|                                                                                                                |                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/061.png) | For information on other ways to add records, please refer to the online FMDC.HLP help file. |

To add a new record to a file using TFMFiler.AddFDA:

> 1\. Get values from the user for the record's .01 field, and for any required identifier fields.

> 2\. Pre-validate each field value. To do this, set the FieldNumber, FileNumber, and Value properties of a TFMValidator component for each field directly (or use its Setup method). For validation, Value should be in the form it would be input as a user (not internal form!) Set the IENS property to the IENS including placeholder (e.g.,'+1,') for the new record. Call the TFMValidator 's Validate method. This gives you the external and internal VA FileMan forms of each field value. Ask for the value again if it fails validation.

> 3\. Use a TFMFiler component's AddFDA method to add VA FileMan Data Arrays (FDAs) (File, record number, field and value) for these fields to the TFMFiler component's list of fields to be updated. Value should be in internal VA FileMan format (obtained from the validation step above). For the record number for each field, use an identical placeholder (e.g. '+1,').

> 4\. When you're ready to file the new record, call the TFMFiler component's Update method. This adds the new record.

> 5\. To find the actual IEN assigned to the new record, call the TFMFiler component's FindIEN method using the new record's placeholder. If the return value is null, the record was not created (and an error would have been returned by the Update call).

The following example adds a new record and displays the IEN of the added record:

procedure TForm1.AddRecord(Sender: TObject);

var NewName, IEN: String;

begin

NewName:= InputBox('Add a New Service', 'Service Name: ', '');

FMValidator1.Setup('49','+1,','.01',NewName);

Ifnot FMValidator1.Validate then

FMValidator1.DisplayErrors

elsebegin {file}

FMFiler1.AddFDA('49','+1,','.01',NewName);

if not FMFiler1.Update then FMFiler1.DisplayErrors;

//get IEN of new record}

IEN:=FMFiler1.FindIEN('+1,');

if IEN \<\> '' then FMGets1.IENS:=IEN+',';

end; {file}

end;

<span id="_Toc90780663" class="anchor"></span>Figure 5‑5: Adding a new record

Once you have the IEN for the new record you've created, you could use a TFMGets component to populate a set of VA FileMan data controls with the new record's values.

# FMDC.HLP Help File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For complete information on the FileMan Delphi Components, including full listings of each component's methods and properties, please refer to the FMDC.HLP help file provided with the FileMan Delphi Components.

![](fmdc-getting-started-guide/062.png)

<span id="_Toc90780664" class="anchor"></span>Figure 6‑1: FMDC online help file directory tree

FMDC.HLP Help File as Context-Sensitive Help

You can integrate the FMDC.HLP help file with Delphi's help. This means that you can select a FileMan Delphi Component on a Delphi form, or a FileMan Delphi Component property in Delphi's Object Browser, press F1, and automatically access the corresponding help file topic from FMDC.HLP.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](fmdc-getting-started-guide/063.png) | For more information integrating the FMDC help file with Delphi, please refer to the *FileMan Delphi Components Installation Guide*. |

Accessing the FMDC.HLP Help File Directly

You can invoke the FMDC.HLP file directly by making a Windows shortcut or desktop icon for it. Your shortcut or icon should load the copy of the FMDC.HLP file that you place in your DELPHI\HELP directory during installation.

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$
\$\$FIND1^DIC, 1-2
A
Accessing the FMDC.HLP Help File Directly, 6-2
Add a New Record to a File Using TFMFiler.AddFDA, 5-5
AddChgdControl Method, 4-3, 4-4
AddFDA Method, 4-4, 5-4, 5-5
AddField Method, 5-2
Adding a Record
TFMFiler Component, 5-5
Adobe
Home Page Web Address, xii
Adobe Acrobat Quick Guide
Home Page Web Address, xii
AnythingToFile Method, 4-4
APIs
\$\$FIND1^DIC, 1-2
Database Server (DBS), xi, 1-1, 1-2, 2-4, 4-2, 5-4
FIND^DIC, 1-2
GETS^DIQ, 1-1
HELP^DIE, 1-2
UPDATE^DIE, 1-1
VAL^DIE, 1-1
Assumptions About the Reader, xi
C
Caption Property, 3-3, 3-4
Compatible Controls and Field Types, 3-1
Component componentTRPCBroker, 3-5
Components
TFMCheckBox, 1-1, 1-3, 2-2, 3-1, 3-3
TFMComboBox, 1-3, 2-2, 3-1, 3-5, 4-2, 4-5
TFMComboBoxLookUp, 1-2, 1-3, 2-2, 3-1, 3-5, 3-6, 3-5, 4-5
TFMEdit, 1-1, 1-3, 2-2, 3-1, 3-2, 3-7, 4-3
TFMFiler, 4-5, 5-4, 5-5
TFMFinder, 1-2, 4-5
TFMFindOne, 1-2, 4-5
TFMGets, 1-1, 2-1, 2-2, 3-2, 3-5, 4-1, 4-2, 4-5, 5-1, 5-6
TFMHelp, 1-2
TFMLabel, 1-3, 2-2, 3-1, 3-7
TFMListBox, 1-3, 2-2, 3-1, 3-5, 4-2, 4-5
TFMLister, 1-2, 2-2, 3-5, 3-6, 4-1, 5-2, 5-3
TFMLookUp, 1-1, 1-2, 2-2, 2-3, 3-1, 3-7, 4-1, 4-5
TFMMemo, 1-1, 1-3, 2-2, 3-1, 3-2, 3-7, 4-3
TFMRadioButton, 1-3, 2-2, 3-1, 3-4
TFMRadioGroup, 1-3, 2-2, 3-1, 3-3
TFMValidator, 1-1, 2-1, 3-2, 4-3, 4-5, 5-3, 5-5
TGroupBox, 2-2, 3-4
TPanel, 2-2, 3-4
TRPCBroker, 2-1, 3-6, 4-1, 5-3
TRPCBroker Component, 5-1
ComponentTFMFiler, 4-4
Contents, v
coValOnExit Value, 2-3, 4-3
CreateContext Method, 2-4
Custom Dialogues, 1-1, 1-2
D
Data Access Components, 1-1
Data Arrays, 5-5
Data Control Property Settings for All Field Types, 3-2
Data Controls, 1-1, 1-2, 1-3, 2-2, 2-3, 3-1, 3-7, 4-2, 4-3, 4-4, 4-5, 5-1, 5-6
Setting Properties, 3-2
Database Server (DBS) API, xi, 1-1, 1-2, 2-4, 4-2, 5-4
DataProblemCheck Method, 4-4
DisplayErrors Method, 4-2, 4-4
Documentation
Revisions, iii
E
Edit Pointer Fields
TFMLookUp, 3-7
Edit Records in a Given VA FileMan File with the FMDC, 2-1
Editing Records from Several Files Simultaneously, 4-5
Execute Method, 2-2, 2-3, 3-7, 4-1
F
Field Types and Compatible Controls, 3-1
FieldNumber Property, 5-5
FieldNumbers Property, 3-5, 3-6, 5-2, 5-3
Figures and Tables, vii
File Standalone Values, 5-4
FileNumber Property, 2-1, 3-5, 3-6, 4-1, 5-1, 5-3, 5-5
Files
FMDC.HLP, 2-4, 4-1, 4-5, 5-5, 6-1, 6-2
Context Sensitive Help, 6-1
Filing Standalone Values
TFMFiler Component, 5-4
FIND^DIC, 1-2
FindIEN Method, 5-5
FMCtrlOptions Property, 2-3, 4-3
FMDC
Custom Dialogues, 1-2
Data Access Components, 1-1
Data Control Components, 1-3
Home Page Web Address, xi
Introduction, 1-1
Object Hierarchy, 1-4
FMDC.HLP File, 2-4, 4-1, 4-5, 5-5, 6-1, 6-2
Context Sensitive Help, 6-1
FMField Property, 3-2, 3-7, 4-2, 4-5
FMFile Property, 3-2, 3-7, 4-2, 4-5
FMFiler Property, 3-2, 4-5
FMGets Property, 3-2, 4-5
FMInternalCodes Property, 3-3
FMLister Property, 3-5, 3-6, 4-1
FMRequired Property, 4-3, 4-4
FMValidator Property, 3-2
FMValueChecked Property, 3-3, 3-4
FMValueUnchecked Property, 3-3
G
GetAndFill Method, 2-2, 3-5, 4-2
GetData Method, 5-1, 5-2
GetField Method, 5-2
GetList Method, 3-5, 4-2, 5-2, 5-3
GetMore Method, 5-3
GETS^DIQ, 1-1
H
Help at Prompts, x
HELP^DIE, 1-2
Home Page
Adobe Acrobat Quick Guide Home Page Web Address, xii
Adobe Home Page Web Address, xii
FMDC Home Page Web Address, xi
HSD&D Home Page Web Address, xi
VA FileMan Programmer Manual Home Page Web Address, xi
VistA Documentation Library (VDL) Home Page Web Address, xii
How to
Add a New Record to a File Using TFMFiler.AddFDA, 5-5
By Task, 4-1
By VA FileMan Field Type, 3-1
Edit Pointer Fields
TFMLookUp, 3-7
Edit Records in a Given VA FileMan File with the FMDC, 2-1
File Standalone Values, 5-4
Obtain Technical Information Online, x
Other Tasks, 4-5
Retrieve a List of Records with TFMLister, 5-2
Retrieve a Record Without Populating VA FileMan Data Controls, 5-1
Save Accumulated Filing Requests, 4-4
Select a Record with a TFMLookUp Component, 4-1
Turn on Automated OnExit Processing, 4-3
Use this Manual, ix
Using
Boolean Set of Code Fields
TFMCheckBox, 3-3
Computed Fields
TFMEdit, 3-7
TFMLabel, 3-7
Free Text, Numeric, MUMPS Fields
TFMEdit, 3-2
Multi-value Set of Code Fields
TFMRadioButton, 3-4
TFMRadioGroup, 3-3
Pointer Fields
TFMComboBox, 3-5
TFMComboBoxLookUp, 3-5
TFMListBox, 3-5
Word-processing Fields
TFMMemo, 3-7
Validate a Standalone Value, 5-3
HSD&D
Home Page Web Address, xi
I
IENS Property, 5-2, 5-3, 5-5
Introduction, 1-1
Items Property, 3-3, 3-5, 3-6, 4-2
L
ListerOptions Property, 5-3
M
Methods
AddChgdControl, 4-3, 4-4
AddFDA, 4-4, 5-4, 5-5
AddField, 5-2
AnythingToFile, 4-4
CreateContext, 2-4
DataProblemCheck, 4-4
DisplayErrors, 4-2, 4-4
Execute, 2-2, 2-3, 3-7, 4-1
FindIEN, 5-5
GetAndFill, 2-2, 3-5, 4-2
GetData, 5-1, 5-2
GetField, 5-2
GetList, 3-5, 4-2, 5-2, 5-3
GetMore, 5-3
Setup, 5-3, 5-5
Update, 2-3, 4-4, 5-4, 5-5
Validate, 5-3, 5-5
N
Number Property, 3-6, 4-1, 5-3
O
Object Hierarchy, 1-4
Objects
TFMFieldObj, 5-1, 5-2
TFMRecordObj, 5-2
Obtaining
Data Dictionary Listings, x
Technical Information Online, How to, x
OnExit Event Handler, 4-3
OnExit Processing, 2-3, 3-2, 3-7, 4-3, 4-4, 4-5
Orientation, ix
Other "How To" Tasks, 4-5
P
Patches
Revisions, iii
Properties
Caption, 3-3, 3-4
FieldNumber, 5-5
FieldNumbers, 3-5, 3-6, 5-2, 5-3
FileNumber, 2-1, 3-5, 3-6, 4-1, 5-1, 5-3, 5-5
FMCtrlOptions, 2-3, 4-3
FMField, 3-2, 3-7, 4-2, 4-5
FMFile, 3-2, 3-7, 4-2, 4-5
FMFiler, 3-2, 4-5
FMGets, 3-2, 4-5
FMInternalCodes, 3-3
FMLister, 3-5, 3-6, 4-1
FMRequired, 4-3, 4-4
FMValidator, 3-2
FMValueChecked, 3-3, 3-4
FMValueUnchecked, 3-3
IENS, 5-2, 5-3, 5-5
Items, 3-3, 3-5, 3-6, 4-2
ListerOptions, 5-3
Number, 3-6, 4-1, 5-3
ReadOnly, 3-7
Results, 5-1, 5-2, 5-3
RPCBroker, 2-1, 3-5, 3-6, 4-1, 5-1, 5-3
Value, 5-3, 5-5
Providing Automated OnExit Processing for Controls, 4-3
Q
Quick Start Guide, 2-1
R
Reader, Assumptions About the, xi
ReadOnly Property, 3-7
Reference Materials, xi
Results Property, 5-1, 5-2, 5-3
Retrieve a List of Records with TFMLister, 5-2
Retrieve a Record Without Populating VA FileMan Data Controls, 5-1
Retrieving a List of Records
TFMLister Component, 5-2
Retrieving a Record, 4-2
TFMGets Component, 5-1
Revision History, iii
Documentation, iii
Patches, iii
RPCBroker Property, 2-1, 3-5, 3-6, 4-1, 5-1, 5-3
S
Save Accumulated Filing Requests, 4-4
Saving a Record, 4-4
Select a Record with a TFMLookUp Component, 4-1
Selecting a Record, 4-1
Setup Method, 5-3, 5-5
T
Table of Contents, v
Tables and Figures, vii
TFMCheckBox Component, 1-1, 1-3, 2-2, 3-1, 3-3
TFMComboBox Component, 1-3, 2-2, 3-1, 3-5, 4-2, 4-5
TFMComboBoxLookUp Component, 1-2, 1-3, 2-2, 3-1, 3-5, 3-6, 3-5, 4-5
TFMEdit Component, 1-1, 1-3, 2-2, 3-1, 3-2, 3-7, 4-3
TFMFieldObj Object, 5-1, 5-2
TFMFiler Component, 4-4, 4-5, 5-4, 5-5
Adding a Record, 5-5
Filing Standalone Values, 5-4
TFMFinder Component, 1-2, 4-5
TFMFindOne Component, 1-2, 4-5
TFMGets Component, 1-1, 2-1, 2-2, 3-2, 3-5, 4-1, 4-2, 4-5, 5-1, 5-6
Retrieving a Record, 5-1
TFMHelp Component, 1-2
TFMLabel Component, 1-3, 2-2, 3-1, 3-7
TFMListBox Component, 1-3, 2-2, 3-1, 3-5, 4-2, 4-5
TFMLister Component, 1-2, 2-2, 3-5, 3-6, 4-1, 5-2, 5-3
Retrieving a List of Records, 5-2
TFMLookUp Component, 1-1, 1-2, 2-2, 2-3, 3-1, 3-7, 4-1, 4-5
TFMMemo Component, 1-1, 1-3, 2-2, 3-1, 3-2, 3-7, 4-3
TFMRadioButton Component, 1-3, 2-2, 3-1, 3-4
TFMRadioGroup Component, 1-3, 2-2, 3-1, 3-3
TFMRecordObj Object, 5-2
TFMValidator Component, 1-1, 2-1, 3-2, 4-3, 4-5, 5-3, 5-5
Validating a Standalone Value, 5-3
TGroupBox Component, 2-2, 3-4
TPanel Component, 2-2, 3-4
TRPCBroker Component, 2-1, 3-5, 3-6, 4-1, 5-1, 5-3
Turn on Automated OnExit Processing, 4-3
U
Update Method, 2-3, 4-4, 5-4, 5-5
UPDATE^DIE, 1-1
Using
Boolean Set of Code Fields
TFMCheckBox, 3-3
Computed Fields
TFMEdit, 3-7
TFMLabel, 3-7
Data Access Components Directly, 5-1
Free Text, Numeric, MUMPS Fields
TFMEdit, 3-2
Multi-value Set of Code Fields
TFMRadioButton, 3-4
TFMRadioGroup, 3-3
Pointer Fields
TFMComboBox, 3-5
TFMComboBoxLookUp, 3-5
TFMListBox, 3-5
Word-processing Fields
TFMMemo, 3-7
V
VA FileMan Field Types and Compatible Controls, 3-1
VA FileMan Programmer Manual
Home Page Web Address, xi
VAL^DIE, 1-1
Validate a Standalone Value, 5-3
Validate Method, 5-3, 5-5
Validating a Standalone Value
TFMValidator Component, 5-3
Value Property, 5-3, 5-5
Values
coValOnExit, 2-3, 4-3
VistA Documentation Library (VDL)
Home Page Web Address, xii
W
Web Page
Adobe Acrobat Quick Guide Home Page Web Address, xii
Adobe Home Page Web Address, xii
FMDC Home Page Web Address, xi
HSD&D Home Page Web Address, xi
VA FileMan Programmer Manual Home Page Web Address, xi
VistA Documentation Library (VDL) Home Page Web Address, xii
When Control Values are changed by Code, 4-3
