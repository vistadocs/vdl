---
title: TBI Version 4.2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: TBI
app_name: "Registry: Traumatic Brain Injury"
section: CLI
app_status: active
pkg_ns: TBI
patch_ver: 4.2
patch_id: TBI*4.2
group_key: "TBI:TBI:4.2"
file_numbers: []
security_keys: []
menu_options: 0
description: The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the Global War on Terror (GWOT) report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic B
audience: 
keywords: 
  - table
  - contents
  - class
  - application
  - tools
  - injury
  - registry
  - access
  - strong
  - traumatic
page_count: 0
word_count: 1491
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2015
revision_count: 6
revision_newest: 7/7/2015
revision_oldest: 9/09/2011
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbiig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbiig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

Traumatic Brain Injury (TBI)

Installation Guide

![](tbi-version-4-2-installation-guide/001.png)

Increment 1

July 2015

Office of Information and Technology (OIT)

Product Development

Revision History

| Date      | Version | Description                                                         | Author                             |
|-----------|---------|---------------------------------------------------------------------|------------------------------------|
| 7/7/2015  | 4.2     | Reviewed for TBI Enhancements Increment 1. No updates necessary.    | <span class="mark">REDACTED</span> |
| 5/6/2014  | 4.1     | Updated for Increment 5. No major updates, minor formatting updates | <span class="mark">REDACTED</span> |
| 5/2/2012  | 4.0     | Final Version                                                       | <span class="mark">REDACTED</span> |
| 5/1/2012  | 2.1     | Document review                                                     | <span class="mark">REDACTED</span> |
| 4/25/2012 | 2.0     | Updated for Increment 4                                             | <span class="mark">REDACTED</span> |
| 9/09/2011 | 1.0     | Final Version                                                       | <span class="mark">REDACTED</span> |

<span id="_Toc303239520" class="anchor"></span>Table 1 - Typographical Conventions

Table of Contents

1\. Preface [1](#preface)

1.1. Typographical Conventions Used in the Manual [1](#typographical-conventions-used-in-the-manual)

1.2. The Traumatic Brain Injury Registry Application [2](#the-traumatic-brain-injury-registry-application)

1.3. Purpose of the Manual [2](#purpose-of-the-manual)

1.4. Recommended Users [2](#_Toc387158011)

2\. Background [3](#background)

3\. Access to TBI from CPRS [4](#access-to-tbi-from-cprs)

3.1. Providing Access to TBI from the Tools Menu [4](#providing-access-to-tbi-from-the-tools-menu)

3.2. Tools Menu – Example Configuration [5](#tools-menu-example-configuration)

Table of Tables

[Table 1 - Typographical Conventions [1](#_Toc303239520)](#_Toc303239520)

[Table 2 - Graphical Conventions [1](#_Toc303239521)](#_Toc303239521)

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [The Traumatic Brain Injury Registry Application](#the-traumatic-brain-injury-registry-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
- [Background](#background)
- [Access to TBI from CPRS](#access-to-tbi-from-cprs)
  - [Providing Access to TBI from the Tools Menu](#providing-access-to-tbi-from-the-tools-menu)
  - [Tools Menu – Example Configuration](#tools-menu-example-configuration)

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other conventions are used:

<table>
<caption><p><span id="_Toc303239521" class="anchor"></span>Table 2 - Graphical Conventions</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 33%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Font</strong></th>
<th><strong>Used for…</strong></th>
<th><strong>Examples:</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blue text, underlined</td>
<td>Hyperlink to another document or URL</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Green text, dotted underlining</td>
<td>Hyperlink within this document</td>
<td>See Release History for details.</td>
</tr>
<tr class="odd">
<td>Courier New</td>
<td>Patch names, VistA filenames</td>
<td>Patch names will be in this font</td>
</tr>
<tr class="even">
<td>Franklin Gothic Demi</td>
<td><p>Keyboard keys</p>
<p>Web application panel, pane, tab, and button names</p></td>
<td><p>&lt; F1 &gt;, &lt; Alt &gt;, &lt; L &gt;</p>
<p>Other Registries panel</p>
<p>[Delete] button</p></td>
</tr>
<tr class="odd">
<td>Microsoft Sans Serif</td>
<td>Software Application names</td>
<td>Traumatic Brain Injury (TBI)</td>
</tr>
<tr class="even">
<td rowspan="4">Microsoft Sans Serif bold</td>
<td>Registry names</td>
<td><strong>TBI</strong></td>
</tr>
<tr class="odd">
<td>Database field names</td>
<td><strong>Mode field</strong></td>
</tr>
<tr class="even">
<td>Report names</td>
<td><strong>National Summary Report</strong></td>
</tr>
<tr class="odd">
<td>Organization and Agency Names</td>
<td><strong>DoD, VA</strong></td>
</tr>
<tr class="even">
<td>Microsoft Sans Serif, 50% gray and italics</td>
<td>Read-only fields</td>
<td><em>Procedures</em></td>
</tr>
<tr class="odd">
<td>Times New Roman</td>
<td>Normal text</td>
<td>Information of particular interest</td>
</tr>
<tr class="even">
<td rowspan="3">Times New Roman Italic</td>
<td>Text emphasis</td>
<td>“It is <em>very</em> important . . .”</td>
</tr>
<tr class="odd">
<td>National and International Standard names</td>
<td><em>International Statistical Classification of Diseases and Related Health Problems</em></td>
</tr>
<tr class="even">
<td>Document names</td>
<td><em>Traumatic Brain Injury (TBI) Registry User Manual</em></td>
</tr>
</tbody>
</table>

<span id="_Toc303239521" class="anchor"></span>Table 2 - Graphical Conventions

| Graphic                                        | Used for…                                                                          |
|----------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](tbi-version-4-2-installation-guide/002.png) | Information of particular interest regarding the current subject matter.               |
| ![](tbi-version-4-2-installation-guide/003.png) | A tip or additional information that may be helpful to the user.                       |
| ![](tbi-version-4-2-installation-guide/004.png) | A warning concerning the current subject matter.                                       |
| ![](tbi-version-4-2-installation-guide/005.png) | Information about the history of a function or operation; provided for reference only. |
| ![](tbi-version-4-2-installation-guide/006.png)  | Indicates an action or process which is optional                                       |
| ![](tbi-version-4-2-installation-guide/007.png)  | Indicates a resource available either in this document or elsewhere                    |

## The Traumatic Brain Injury Registry Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Traumatic Brain Injury Registry application (TBI Registry) supports the maintenance of local and national registries for clinical and resource tracking of care for such Veterans. The TBI Registry software application allows case managers to identify Veterans who participated in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) and who sustained a head injury and thus are potential traumatic brain injury (TBI) patients. The TBI Registry permits the case manager to oversee and track the comprehensive evaluation of these patients. It also provides 17 types of reports used for tracking the evaluation and care of individuals identified as possible TBI candidates.

There are three TBI applications: the main application, TBI Instruments and the TBI Polytrauma application. There are two ways to access TBI information, depending upon the application. TBI Instruments can be made available by adding it to the CPRS Tools Menu.

The standalone version of TBI is not connected to CPRS. Non-Instrument TBI is accessed in a standalone mode by entering the uniform resource locator (URL) link in the Internet Explorer address bar. Refer to the *TBI User Manual* for a detailed description on access and use of TBI from CPRS and as a standalone application process.

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides the details for accessing and installing the TBI Registry, which has been developed for the Department of Veterans Affairs (VA) in support of Veterans who are potential TBI patients.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TBI Registry software is designed for use by designated case managers who are responsible for screening and overseeing the records of patients both seen and not seen for the comprehensive TBI evaluation.

This installation guide is intended for system administrators who are assumed to possess the technical knowledge of how to configure and interact with CPRS and VistA files.

TBI Instruments is not installed at each local site; it is installed on an application server. A link to the application may be incorporated into the existing CPRS Tools Menu at the local site. The instructions provided in this guide identify the required configuration settings for TBI Instruments use from the CPRS Tools Menu.

# Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) is charged with supporting the Presidential Task Force on Returning Global War on Terror Heroes. The Task Force has stated in the *Global War on Terror (GWOT)* report (recommendation P-7) that the Department of Veterans Affairs (VA) shall “create a ‘Traumatic Brain Injury’ Surveillance Center and Registry to monitor returning service members who have possibly sustained head injury and thus may potentially have a traumatic brain injury in order to provide early medical intervention.”

The Traumatic Brain Injury (TBI) Registry software application collects data on the population of Veterans who participated in Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF). These individuals need to be seen within 30 days for a comprehensive TBI evaluation. Each facility can produce local reports (information related to patients evaluated and treated in their system).

| ![](tbi-version-4-2-installation-guide/008.png) | Note: Access to TBI Instruments in a test account should not be made available to general users. Access should be made available in a production account. Data in VistA is linked to the Registries database via Social Security Numbers, and these would not match in a test environment. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Access to TBI from CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Providing Access to TBI from the Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A site will use the Tools Menu to give users access to other client software from within CPRS. The parameter, ORWT TOOLS MENU, is used to set up the list of software that appears on the menu. This parameter may be set up for the site, then overridden as appropriate at the division, service, and user levels.

Each item entered on the Tools Menu should have the form:

NAME=COMMAND

NAME represents what the user will see on the menu for that line item. An ampersand “&” may also be used in front of a letter to allow keyboard access to the menu item.

COMMAND may be an entry that is executable by Windows. It may be any file that has a Windows file association.

For example:

Name=Command: &CPRSInfo=http://vista.med.va.gov/cprs/index.html

For TBI:

Name=Command:

TBI Instruments=https://vaww.tbi.registries.aac.va.gov/TBI_Instruments/PatientInstruments.aspx?q9gtw0=931&xqi4z=%DFN&yiicf=%DUZ&jbPI0202=%SRV&27trp=%PORT

\[Note: The above is to be entered on one line, as shown in the example, with no line break\]

In the following example extracted from the CPRS GUI Technical Manual, note that CPRSInfo did not require an executable file to be identified. Since Windows understands hypertext transfer protocol (HTTP), it will launch the workstation’s default browser and navigate to the address. Also note the quotation marks in the VistA Terminal (VT) example. A path that contains space characters (like C:\Program Files\\..) must be surrounded by quotation marks. Entries on the command line may also contain parameters. The LOCALVAMC is the name of a KEA! session, which is passed as a command line parameter.

## Tools Menu – Example Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select General Parameter Tools Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: ORWT TOOLS MENU CPRS GUI Tools Menu

> ORWT TOOLS MENU may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

> 2 Location LOC \[choose from HOSPITAL LOCATION\]

> 2.5 Service SRV \[choose from SERVICE/SECTION\]

> 3 Division DIV \[REGION 5\]

> 4 System SYS \[OEC.ISC-SLC.VA.GOV\]

> Enter selection: 1 User NEW PERSON

> Select NEW PERSON NAME: CPRSPROVIDER,TEN TC

> -------------- Setting ORWT TOOLS MENU for User: CPRSPROVIDER,TEN -----

> Select Sequence: 1

> Are you adding 1 as a new Sequence? Yes// YES

> Sequence: 1// 1

> Name=Command: &Notepad=Notepad.exe

> Select Sequence: 2

> Are you adding 2 as a new Sequence? Yes// YES

> Sequence: 2// 2

> Name=Command: &CPRSInfo=http://vista.med.va.gov/cprs/index.html

> Select Sequence: 3

> Are you adding 3 as a new Sequence? Yes// YES

> Sequence: 3// 3

> Name=Command: &VistA=”C:\Program Files\Attachmate\KEA! VT\keavt.exe” LOCALVAMC

> Select Sequence:

It is also possible to pass context-sensitive parameters. These are parameters that are entered as placeholders and then converted to the appropriate values at runtime. These placeholder parameters are:

> %SRV = Server name for the current broker connection

> %PORT = Port number for the current broker connection

> %MREF = M code giving the global reference where the patient DFN is stored

> %DFN = The actual DFN of the currently selected patient

> %DUZ = Internal entry number of the current user

So, if you have another application that needs to know, for example, the identity of the current user and currently selected patient, you could list %DUZ and %DFN as parameters in the command that executes that program.