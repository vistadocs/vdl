---
title: "Kernel 8.0 Systems Management: Device Handler User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: Device Handler"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - device
  - span
  - class
  - table
  - terminal
  - spool
  - contents
  - figure
  - anchor
  - devices
page_count: 0
word_count: 17324
section_count: 24
table_count: 15
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Device Handler User Guide
---

![](kernel-8-0-systems-management-device-handler-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-device-handler-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref26361187" class="anchor"></span>Table 1: Sample Semicolon-delimited Pieces at the “DEVICE:” Prompt</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/31/2025</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>07/23/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<p>Updated external document links to open documents in a new window.</p></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Device Handler User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref26361187" class="anchor"></span>Table 1: Sample Semicolon-delimited Pieces at the “DEVICE:” Prompt

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="List_of_Figures" class="anchor"></span>List of Figures

<span id="List_of_Tables" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-systems-management-device-handler-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Device Handler: User Interface](#device-handler-user-interface)
  - [Printing to Devices](#printing-to-devices)
    - [Specifying Right Margin and Page Length](#specifying-right-margin-and-page-length)
  - [Queuing](#queuing)
  - [Specifying a Special Subtype](#specifying-a-special-subtype)
    - [Spool Document Names—An Exception](#spool-document-namesan-exception)
  - [Alternate Syntax for Device Specification](#alternate-syntax-for-device-specification)
  - [Summary](#summary)
- [Device Handler: System Management](#device-handler-system-management)
  - [DEVICE (#3.5) File](#device-35-file)
    - [DEVICE File Fields](#device-file-fields)
    - [Device Edit Menu](#device-edit-menu)
    - [Sample Device File Entries](#sample-device-file-entries)
  - [Mixed OS Environment Fields](#mixed-os-environment-fields)
    - [Edit Logical/Physical Mapping Option](#edit-logicalphysical-mapping-option)
    - [Enter/Edit Kernel Site Parameters Option](#enteredit-kernel-site-parameters-option)
  - [Device Security](#device-security)
  - [TERMINAL TYPE (#3.2) File](#terminal-type-32-file)
    - [Terminal Type Naming Conventions](#terminal-type-naming-conventions)
    - [How Shared Device and Terminal Type Attributes are Used](#how-shared-device-and-terminal-type-attributes-are-used)
    - [Terminal Type Information Retained by User](#terminal-type-information-retained-by-user)
  - [Devices and Signon](#devices-and-signon)
    - [Device Selection at Signon and Virtual Terminal Devices](#device-selection-at-signon-and-virtual-terminal-devices)
    - [Terminal Type Selection at Signon](#terminal-type-selection-at-signon)
  - [Troubleshooting](#troubleshooting)
    - [Loopback Test of Device Port Option](#loopback-test-of-device-port-option)
    - [Send Test Pattern to Terminal Option](#send-test-pattern-to-terminal-option)
    - [Out of Service Set/Clear Option](#out-of-service-setclear-option)
    - [Verify HFS and NULL Device Setup (required)](#verify-hfs-and-null-device-setup-required)
  - [Device Identification and Cross-References](#device-identification-and-cross-references)
- [Host Files](#host-files)
  - [Host Files: User Interface](#host-files-user-interface)
  - [Host Files: System Management](#host-files-system-management)
    - [Host File Server Device Edit Option](#host-file-server-device-edit-option)
    - [Caché and GT.M HFS Device Setup](#caché-and-gtm-hfs-device-setup)
- [Spooling](#spooling)
  - [Spooling: User Interface](#spooling-user-interface)
    - [Sending Output to the Spooler](#sending-output-to-the-spooler)
    - [Retrieving Spooled Documents](#retrieving-spooled-documents)
    - [Browsing a Spool Document](#browsing-a-spool-document)
    - [Printing Spool Documents](#printing-spool-documents)
    - [Making Spool Documents into Mail Messages](#making-spool-documents-into-mail-messages)
  - [Spooling: System Management](#spooling-system-management)
    - [Spool Document Storage](#spool-document-storage)
    - [Overflowing Spool Document Storage](#overflowing-spool-document-storage)
    - [Granting Spooling Privileges](#granting-spooling-privileges)
    - [Managing Spool Documents](#managing-spool-documents)
    - [Spooler Site Parameters Edit Option](#spooler-site-parameters-edit-option)
    - [Purge old Spool documents Option](#purge-old-spool-documents-option)
    - [Defining Spool Device Types](#defining-spool-device-types)
    - [Spool Device Edit Option](#spool-device-edit-option)
    - [Auto-Despooling](#auto-despooling)
    - [Generating Spool Document Names](#generating-spool-document-names)
- [Special Devices](#special-devices)
  - [Browser Device](#browser-device)
    - [Browser User Interface](#browser-user-interface)
    - [Browser System Management](#browser-system-management)
  - [Form Feeds](#form-feeds)
    - [Form Feeds User Interface](#form-feeds-user-interface)
    - [Form Feeds System Management](#form-feeds-system-management)
  - [Magtape](#magtape)
    - [Magtape System Management](#magtape-system-management)
  - [Network Channel Devices](#network-channel-devices)
    - [Network Channel Devices System Management](#network-channel-devices-system-management)
  - [Resources](#resources)
    - [Resources System Management](#resources-system-management)
  - [Sequential Disk Processors (Obsolete)](#sequential-disk-processors-obsolete)
  - [Slaved Printers](#slaved-printers)
    - [Slaved Printers User Interface](#slaved-printers-user-interface)
    - [Slaved Printers System Management](#slaved-printers-system-management)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Device Handler User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. Device Handler is a Kernel module that provides a mechanism for accessing peripherals and using them in controlled ways (e.g., user access to printers or other output devices).

# Device Handler: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications that are designed for the Kernel environment perform output in a consistent manner, using Kernel’s Device Handler. This ensures consistency on how you are asked to select devices for output and how the output is performed.

When you respond to the “DEVICE:” prompt, you are using the Device Handler.

## Printing to Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “DEVICE:” prompt, to send output to your terminal, you can simply press the \<Enter\> key. This tells the Device Handler to display the report on the home device (that is, on your terminal), as shown in <u>Figure 1</u>:

<span id="_Ref29371825" class="anchor"></span>Figure 1: Choosing the Home Device

DEVICE: <span class="mark">\<Enter\></span>

To send output to a printer, enter the name of the printer at the “DEVICE:” prompt, as shown in <u>Figure 2</u>:

<span id="_Ref29371990" class="anchor"></span>Figure 2: Choosing a Printer Device

DEVICE: <span class="mark">DVNM5 \<Enter\></span>

To select the closest printer, if one is defined (unlikely), you can simply enter P and press \<Enter\>, as shown in <u>Figure 3</u>:

<span id="_Ref29372009" class="anchor"></span>Figure 3: Choosing the Closest Printer Device

DEVICE: <span class="mark">P \<Enter\></span>

You can enter a question mark (?) to display help about the syntax of the response, as shown in <u>Figure 4</u>:

<span id="_Ref29372035" class="anchor"></span>Figure 4: Device Syntax Help—One Question Mark (?)

DEVICE: <span class="mark">? \<Enter\></span>

Specify a device with optional parameters in the format

Device Name;Right Margin;Page Length

or

Device Name;Subtype;Right Margin;Page Length

You can enter two question marks (??) to display available printers and other devices connected to the current Volume Set or “reachable from” the current Volume Set. You can also ask for a series of help frames under extended help, as shown in <u>Figure 5</u>:

<span id="_Ref29372125" class="anchor"></span>Figure 5: Displaying Devices Help—Two Question Marks (??)

DEVICE: <span class="mark">?? \<Enter\></span>

The following information is available:

All Printers

Printers only on 'ROU'

Complete Device Listing

Devices only on 'ROU'

Extended Help

Select one (A,P,C,D, or E):

You can list all devices. In addition to printers, this list shows other types of devices you can use to handle output. An example of a partial printer listing is shown in <u>Figure 6</u>:

<span id="_Ref29372144" class="anchor"></span>Figure 6: Sample Printer Listing

Select one (A,P,C,D, or E): <span class="mark">P \<Enter\></span>

GENICOM10P 6th Floor 301 GENICOM16P 6th Floor 301

HP LASER DEV-10P HP LASER DEV-12P

![](kernel-8-0-systems-management-device-handler-user-guide/004.png) REF: Unusual device types (such as Resource devices) are discussed in “<u>Special Devices</u>.”

### Specifying Right Margin and Page Length

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ordinarily, when choosing an output device, you only need to specify the device name. There can be times, however, when you may find it useful to specify the right margin or the page length for your output. The syntax to specify margin and page length uses semicolon delimiters. The format is:

DEVICE: Device Name ; Right Margin ; Page Length

The examples in <u>Table 1</u> show how to use the additional semicolon-delimited pieces at the “DEVICE:” prompt:

| Semicolon-delimited Piece | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| DEVICE: DVNM5;80;66   | Use the DVNM5 device with a right margin of 80 columns and page length of 66 lines.             |
| DEVICE: ;132          | Use the home device, right margin of 132.                                                       |
| DEVICE: ;;66          | Use the home device and format the output with page breaks at 66 lines.                         |
| DEVICE: ;;9999        | Scroll output on the home device without needing to press the \<Enter\> key at page breaks. |

<span id="_Ref26361243" class="anchor"></span>Table 2: Alternate Device Attribute Codes

## Queuing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “DEVICE:” prompt, if you enter a device’s name, the output goes directly to that device. If the output you’re sending is, for example, a long report, this ties your terminal up until the report finishes printing to that device.

You can print output and yet keep your terminal free for other processing by queuing your jobs rather than running them directly. As described in the “TaskMan: User Interface” section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf#TaskMan_User_Interface), you can queue output by entering Q at the “Device:” prompt. The device prompt is then presented a second time so that you can specify the output device.

<span id="_Ref85864823" class="anchor"></span>Figure 7: Specifying a Device and Queuing a Print Job—Sample User Dialog (1 of 2)

DEVICE: <span class="mark">Q \<Enter\></span>

DEVICE: <span class="mark">DVNM5 \<Enter\></span>

REQUESTED TIME TO PRINT: NOW// <span class="mark">\<Enter\></span>

REQUEST QUEUED!

Task number: 856103

Alternatively, you can still specify the device first. The Device Handler checks to see if the device is available and, if so, asks you if you want to queue your output. If the device *cannot* be reached at the current time, Device Handler indicates that the device is busy or unavailable. You can avoid the preliminary availability check by entering Q at the first prompt (see <u>Figure 7</u>).

<span id="_Toc193181743" class="anchor"></span>Figure 8: Specifying a Device and Queuing a Print Job—Sample User Dialog (2 of 2)

DEVICE: <span class="mark">DVNM5 \<Enter\></span>

DO YOU WANT YOUR OUTPUT QUEUED? NO// <span class="mark">YES \<Enter\></span>

REQUESTED TIME TO PRINT: NOW// <span class="mark">T@18:00 \<Enter\></span> (JUL 11, 2004@18:00)

REQUEST QUEUED!

Task number: 856109

Whether you request queuing before or after naming a device, Device Handler then asks you to specify a time for the queued job to run. You can accept the default (NOW) or indicate a later time in the usual format. Queuing sends output to TaskMan for scheduling. Meanwhile, you can continue working on the computer system without a delay.

<span id="_Toc193181744" class="anchor"></span>Figure 9: Queuing a Print Job—Sample User Dialog

REQUESTED TIME TO PRINT: NOW// <span class="mark">T@18:00 \<Enter\></span> (JUL 11, 2004@18:00)

REQUEST QUEUED!

Task number: 856109

![](kernel-8-0-systems-management-device-handler-user-guide/005.png) REF: For more information about queuing output, see the “TaskMan: User Interface” section in the [*Kernel Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf#TaskMan_User_Interface).

## Specifying a Special Subtype

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an exception to using numbers in the second semicolon piece to indicate a right margin setting. If, instead of a number, you use a letter and then a hyphen in a device specification (such as P-DEC), the second semicolon piece specifies a terminal type entry from the TERMINAL TYPE (#3.2) file to use for the output. A terminal type entry specifies information about what commands to use with specific printers (such as escape codes).

<span id="_Toc193181745" class="anchor"></span>Figure 10: Terminal-Type Device Entry—*Without* Pauses

DEVICE: <span class="mark">;P-DEC \<Enter\></span>

One form of the subtype request made possible by VA FileMan’s print routines is the use of the word SINGLE along with P- or PK-. Appending -SINGLE indicates that a pause should occur after the display of each page. If using a slaved device to print the screen display, for example, the next page is displayed only after the user has pressed \<Enter\>:

<span id="_Toc193181746" class="anchor"></span>Figure 11: Terminal-Type Device Entry—*With* Pauses

DEVICE: <span class="mark">;P-DEC-SINGLE \<Enter\></span>

If you are *not* sure which subtype to use, you can enter a partial specification of the subtype in the second piece, and the Device Handler lets you choose from all matching subtypes. For example, if a dozen subtypes begin with “P-LASER...,” you can list them by entering only the beginning of the subtype name (such as P-LASER):

<span id="_Toc193181747" class="anchor"></span>Figure 12: Partial Device Specification—Unknown Subtype

DEVICE: <span class="mark">LASER;P-LASER \<Enter\></span>

All subtypes beginning with P-LASER are listed; you can then choose a subtype from this list.

When using a subtype as the second semicolon piece of a device specification, you can still specify a right margin and page length to use, but you then do so with the 3rd and 4th semicolon pieces:

<span id="_Toc193181748" class="anchor"></span>Figure 13: Device Specification—Four-Semicolon Piece: Sample

DEVICE: <span class="mark">LASER;P-LASER-NEW;132;100 \<Enter\></span>

The syntax for the four-semicolon piece form of the device specification is:

<span id="_Toc193181749" class="anchor"></span>Figure 14: Device Specification—Four-Semicolon Piece: Syntax

DEVICE: Device Name ; Subtype ; Right Margin ; Page Length

### Spool Document Names—An Exception

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you request the spool device at the device prompt, you can use the formats in <u>Figure 15</u> and <u>Figure 16</u> to specify the spool document name:

<span id="_Ref29291277" class="anchor"></span>Figure 15: Device Syntax—Specifying a Spool Document Name: Sample Formats (1 of 2)

DEVICE: Spooler ; Spool Document Name ; Right Margin ; Page Length

<span id="_Ref29291299" class="anchor"></span>Figure 16: Device Syntax—Specifying a Spool Document Name: Sample Formats (2 of 2)

DEVICE: Spooler ; Subtype ; Spool Document Name

Although neither right margin nor page length can be specified when including a subtype as the second piece and spool document name as the third, no functionality is lost. The explanation is simple; the spooler only responds to these two terminal type specifications. In other words, identifying a subtype for the spooler does no more than define a margin and page length.

Spool document entries in the SPOOL DOCUMENT (#3.51) file *cannot* have names beginning with: P-, PK-, C-, and so on (that is one or two letters followed by a hyphen, see Section <u>3.4.1</u>). Because this syntax is the required naming convention for subtypes, you are allowed to specify the document name and the subtype in any order.

![](kernel-8-0-systems-management-device-handler-user-guide/006.png) REF: For more information about Spool Devices, see the “<u>Spooling</u>” section.

## Alternate Syntax for Device Specification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An alternate syntax is available for specifying right margin and page length when responding to the device prompt. Using the alternate format, you can specify pitch, intensity, and quality. The success of specifying these additional attributes, however, depends on whether the corresponding fields have been defined by system administrators at your site.

The syntax requires the use of a slash (“/”) after the last semicolon (see <u>Figure 17</u>).

You can use the codes in <u>Table 2</u> to specify special device attributes (in any order), without separating punctuation to delimit the pieces:

| Code  | Description                               |
|-------|-------------------------------------------|
| B | Boldface                                  |
| L | Page length                               |
| M | Margin                                    |
| P | Pitch                                     |
| Q | Quality (can be Q, Q1, or Q2) |

<span id="_Ref29375394" class="anchor"></span>Table 3: Device-related Files Global Locations

For example, you could specify:

<span id="_Ref85866098" class="anchor"></span>Figure 17: Specifying a Device—Using Alternate Syntax

DEVICE: <span class="mark">LASER;P-LASER-LANDSCAPE;/M132L100P16BQ2 \<Enter\></span>

In this example (<u>Figure 17</u>), the following attributes are set:

- Margin (“M”) is set to 132 (M132)
- Page length (“L”) is set to 100 lines (L100)
- Pitch (“P”) is set to 16 (P16)
- Intensity to boldface (“B”)
- Quality (“Q”) set to letter quality (Q2).

An absence of the B would indicate normal intensity. The quality settings are Q, Q1, and Q2.

Your system administrators need to confirm that the appropriate code to set the specified printer attributes is set up for the device that you are using. Then, when the Device Handler closes the device, system administrators need to be sure that appropriate reset code is in the CLOSE EXECUTE field, so that the characteristics do *not* stay in effect. If, for example, someone requests a small pitch, subsequent reports also use the small pitch unless reset in the CLOSE EXECUTE statement for that device (or altered by the OPEN EXECUTE statement of the next device called).

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device Handler is a common interface used by all VistA applications to send output to devices (usually, printers). Once you become familiar with the Device Handler, you can enhance your productivity by making use of some of the Device Handler’s special features, including queuing, selecting a specific right margin or page length, and selecting a special subtype.

# Device Handler: System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device Handler makes use of two primary Files:

- DEVICE (#3.5) File
- TERMINAL TYPE (#3.2) File

Together, these two files control most of the characteristics of devices in Kernel.

The global locations of the device-related files are listed in <u>Table 3</u>:

| Device-related File Name | Global Location |
|--------------------------|-----------------|
| DEVICE (#3.5)            | ^%ZIS(1,    |
| TERMINAL TYPE (#3.2)     | ^%ZIS(2,    |
| DA RETURN CODES (#3.22)  | ^%ZIS(3.22, |

<span id="_Ref29375618" class="anchor"></span>Table 4: DEVICE File Fields

## DEVICE (#3.5) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel’s DEVICE (#3.5) file stores information about devices on the system. All connected volume Sets/CPUs should make use of a single DEVICE (#3.5) file. Then all information concerning a particular device is stored in just one place, which facilitates device management.

Sometimes, a CPU has an attachment point to which a device can be connected, for example, physical ports. The \$I field in the DEVICE (#3.5) file entry identifies this attachment point.

Most devices (such as printers) are connected to the network and \$I points to the name used by the underlying OS to point to the device. When using such a device, Kernel’s Device Handler allows the creation and use of multiple DEVICE (#3.5) file entries for the same physical device. Each DEVICE (#3.5) file entry can contain different specifications (font, margin, page length, and so on) to format output. Each entry in the DEVICE (#3.5) file, then, uniquely identifies a set of instructions to send to a particular device on the network.

Each device that Kernel Device Handler needs to communicate with should be set up as an entry in the DEVICE (#3.5) file. The DEVICE (#3.5) file supports a variety of devices, including video display terminals (VDTs), commonly called cathode ray tube devices (CRTs); printers; tape drives; and operating system files (such as Host File Server \[HFS\] devices).

The DEVICE (#3.5) file is in the Manager’s account for common reference from all associated accounts. With TaskMan’s help, this information is also available to all associated processors (CPUs) in the local area network.

### DEVICE File Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The most essential fields in the DEVICE (#3.5) file to populate or consider populating for device entries are listed in <u>Table 4</u>:

<table>
<caption><p><span id="_Ref237145013" class="anchor"></span>Table 5: Device Types in the TYPE Field in the DEVICE (#3.5) File</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td>This is the name of the device. It is used at the “DEVICE” prompt to select this device. It should <em>not</em> be the internal name for the device but a logical one. It <em>must</em> start with one uppercase character and <em>not</em> contain lowercase characters.</td>
</tr>
<tr class="even">
<td>$I (#1)</td>
<td>This field holds the hardware port name that the operating system (OS) can identify when referencing a port on a CPU. On layered systems where opening of host files is supported, this field can hold the host file name.</td>
</tr>
<tr class="odd">
<td>VOLUME SET(CPU) (#1.9)</td>
<td><p>(Optional) This field holds the name of the CPU to which this device belongs. It holds the name of the CPU where the physical port resides.</p>
<p>If entered, the device is assumed to be accessible only from the specified CPU.</p>
<p>If the field is left blank, this device is assumed to be accessible from all CPUs in the network. In other words, when this device is referenced, the Device Handler operates as if this device is resident on the local CPU. For example, if there is a device that uses the same <strong>$I</strong> on each CPU, one entry can be made in the DEVICE (#3.5) file by leaving this field set to <strong>NULL</strong>. This shortcut works only if the same <strong>$I</strong> has been associated with this device on every CPU. The Device Handler still maintains the CPU cross-reference to support queuing and other activities. The cross-reference format involves use of periods as delimiters. If the VOLUME SET(CPU) value were “<strong>BBB</strong>,” the cross-reference for the device with a <strong>$I</strong> of <strong>75</strong> would be “<strong>BBB.75</strong>”. If the VOLUME SET(CPU) value were <strong>NULL</strong>, then “<strong>.75</strong>” would be the CPU cross-reference.</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/007.png) <strong>NOTE:</strong> In the Caché environment, where cluster mounting is used and most devices are set up on all CPUs, all such devices do <em>not</em> need a value for this field.</p></td>
</tr>
<tr class="even">
<td>SIGN-ON/SYSTEM DEVICE (#1.95)</td>
<td>If set to <strong>YES</strong>, this field identifies that this entry is the primary device among those device entries that have the same <strong>$I</strong> with the same VOLUME SET(CPU). Among those device entries that have a common <strong>$I</strong> and CPU, only one of these entries can have this field set to <strong>YES</strong>. If none of the common device entries is set to <strong>YES</strong>, the default device is identified by the first device on the CPU cross-reference. The default device is used when the Device Handler is invoked with <strong>$I</strong> as the device to be selected.</td>
</tr>
<tr class="odd">
<td>TYPE (#2)</td>
<td><p>This field contains the general type of device on the CPU.</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/008.png) <strong>REF:</strong> For a list of device types, see <u>Table 5</u>.</p></td>
</tr>
<tr class="even">
<td>SUBTYPE (#3)</td>
<td><p>Use this field to select a default terminal type for the device. This field points to the TERMINAL TYPE (#3.2) file to retrieve a standard set of characteristics that have been defined for vendor devices (such as Laser printers or VT320 CRTs).</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/009.png) <strong>REF:</strong> For a discussion of the TERMINAL TYPE (#3.2) file, see the “<u>TERMINAL TYPE (#3.2) File</u>” section.</p></td>
</tr>
<tr class="odd">
<td>QUEUING (#5.5)</td>
<td><p>You can control the degree of queuing allowed for a device with the QUEUING field.</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/010.png) <strong>REF:</strong> For a list of settings to control queuing for a device, see <u>Table 6</u>.</p></td>
</tr>
<tr class="even">
<td>PRE-OPEN EXECUTE (#7)</td>
<td><p>This is the executable M code that is used by <strong>%ZIS</strong> before opening the device.</p>
<p>If you define the <strong>%ZISQUIT</strong> variable, the device open fails. Setting <strong>%ZISQUIT=1</strong> in the PRE-OPEN EXECUTE code signals <strong>%ZIS</strong> to reject the selected device. With this variable, you can use the PRE-OPEN EXECUTE as a screen on whether the device should be opened or not.</p></td>
</tr>
<tr class="odd">
<td>POST-CLOSE EXECUTE (#8)</td>
<td>This is the executable M code that is used by <strong>%ZISC</strong> after closing the device.</td>
</tr>
<tr class="even">
<td>OPEN PARAMETERS (#19)</td>
<td><p>These parameters are used to open a device with specified characteristics/addresses. This field is primarily used with non-terminal devices (such as Magtape and Sequential Disk Processor).</p>
<p>Magtape (MT), SDP (obsolete), and Host File Server (HFS device types use the value in this field as the default if the ASK PARAMETERS (#5 flag is set. Users would then be prompted for address/parameters. If the <strong>ASK PARAMETERS</strong> flag is <em>not</em> set and if there is a value in the OPEN PARAMETERS (#19) field, this value is used when opening the device (or file).</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/011.png) <strong>NOTE:</strong> Each operating system has its own way of specifying parameters. For example, under Caché, margins are set with both the <strong>OPEN</strong> and <strong>USE</strong> command.</p></td>
</tr>
<tr class="odd">
<td>USE PARAMETERS (#19.5)</td>
<td><p>This field holds the parameters to be used in an M <strong>USE</strong> statement.</p>
<p>The Device Handler takes information from this field when opening and using such devices as the Magtape (MT) drive.</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/012.png) <strong>NOTE:</strong> Each operating system has its own way of specifying parameters. For example, under Caché, margins are set with both the <strong>OPEN</strong> and <strong>USE</strong> command.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref237145013" class="anchor"></span>Table 5: Device Types in the TYPE Field in the DEVICE (#3.5) File

| Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BAR  | Identifies the device as a bar code reader.                                                                                                                                                                                                                                                                                                                                                                            |
| CHAN | Network Channels are high speed devices that use network protocols (such as TCP/IP).                                                                                                                                                                                                                                                                                                                                   |
| HFS  | The Host File Server (HFS) type and the associated functionality provides the vehicle to READ and WRITE to host level files. Instead of directing reports to a printer, the results could be placed into an OpenVMS or UNIX/Linux file. This would allow non-M-based statistical software or spreadsheet to use data produced by the M-based application by simply extracting data from the host file. |
| IMPC | Imaging work station device (reserved for VistA Imaging).                                                                                                                                                                                                                                                                                                                                                              |
| MT   | Magtape (MT) devices.                                                                                                                                                                                                                                                                                                                                                                                          |
| OTH  | Other (OTH) devices that do *not* fit a particular category.                                                                                                                                                                                                                                                                                                                                                   |
| RES  | Resources (RES) is a type used for special sequencing of tasks that do *not* require a particular device.                                                                                                                                                                                                                                                                                                      |
| SDP  | (Obsolete) Sequential Disk Processor (SDP) is a predefined allocated disk space used for sequential processing; use HFS.                                                                                                                                                                                                                                                                                       |
| SPL  | Spool (SPL) device is a predefined allocated disk space. It is like SDP; however, access to the spool device can be achieved from multiple users simultaneously.                                                                                                                                                                                                                                           |
| TRM  | Terminal devices (such as most CRTs and printers) should be associated with a corresponding device entry with a type of TRM.                                                                                                                                                                                                                                                                                       |
| VTRM | Virtual Terminal Server devices are those that are associated with a dynamically created M port identification (\$I). A generic device entry with a device type of VTRM can be established for users who log into the system through terminal servers or other network protocols.                                                                                                                              |

<span id="_Ref237145563" class="anchor"></span>Table 6: Queuing Settings

![](kernel-8-0-systems-management-device-handler-user-guide/013.png) NOTE: Device type descriptions can also be obtained by entering two question marks (??) at the TYPE field while editing a device.

![](kernel-8-0-systems-management-device-handler-user-guide/014.png) REF: For more information on these device types, see “<u>Special Devices</u>.”  
  
Also, for more information on Host File Server (HFS) devices, see “<u>Host Files</u>.

| Setting | Queuing     | Description                                          |
|---------|-------------|------------------------------------------------------|
| 0   | ALLOWED     | Jobs can be queued or run directly (default).        |
| 1   | FORCED      | Queuing is forced, unless disallowed by application. |
| 2   | NOT ALLOWED | Queuing to device is *not* allowed.                  |

<span id="_Ref29375915" class="anchor"></span>Table 7: Mixed OS Environment Fields in the DEVICE (#3.5) File

#### OpenVMS-Specific DEVICE Fields

![](kernel-8-0-systems-management-device-handler-user-guide/015.png) NOTE: These fields are used by VMS and *not* Caché.

The DEVICE (#3.5) file can store operating system-specific information. For example, several fields are included in the DEVICE (#3.5) file to configure terminals and ports on Terminal Servers as part of an OpenVMS start-up command file. These operating system-specific fields in the DEVICE (#3.5) file are listed in <u>Table 7</u>:

| Field                              | Description                                                                                                                                                                                                                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LAT SERVER NODE (#61)              | This is the DECserver/terminal server node name that the device is on. It is used by the XTLATSET routine to build data files for VMS startup.                                                                                                                              |
| LAT SERVER PORT (#62)              | This is the port on the DECserver/terminal server to which this device is connected. It can be entered in the LC-2-5 form or 31 form. On EQUINOX it is in the PORT_31 form. This field is used by the XTLATSET routine to build VMS data files for startup. |
| VMS DEVICE TYPE (#63)              | This is a flag that is passed into the LT_PTR.DAT file by the XTLATSET routine to select how this port should be set up in VMS by the SYS\$MANAGER:SYSPRINT.COM file when it runs.                                                                                      |
| LAT PORT SPEED (#64)               | This field holds the value that is passed to the TSC_LOAD.COM file for loading the DECserver permanent database.                                                                                                                                                            |
| PRINT SERVER NAME OR ADDRESS (#65) | This field contains the fully qualified domain name (FQDN) or specific TCP/IP address of a remote server (such as LPD/LPR printing) or device (such as Telnet printer).                                                                                                             |
| TELNET PORT (#66)                  | This field contains the Telnet port of a remote device (such as Telnet printer). The allowable range is a number between 2000 and 65534.                                                                                                                                    |
| REMOTE PRINTER NAME (#67)          | This is the name of the remote printer that is referenced by the PRINT SERVER NAME OR ADDRESS (#65) and TELNET PORT (#66) fields.                                                                                                                                                   |

<span id="_Ref26361441" class="anchor"></span>Table 8: Mixed OS Environment Fields in the KERNEL SYSTEM PARAMETERS (#8989.3) File

Kernel Toolkit software distributes the XTLATSET and NVSTNSET routines that makes use of these fields.

### Device Edit Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEVICE (#3.5) file has many more fields where additional specific information for devices can be entered. Kernel provides several options to facilitate creating and editing device types on the Device Edit \[XUDEVEDIT\] menu, which is located on the Device Management \[XUTIO\] menu:

<span id="_Toc193181755" class="anchor"></span>Figure 18: Device Edit Options

Device Management ... \[XUTIO\]

Device Edit \[XUDEVEDIT\]

ALL Edit All Device Fields \[XUDEVEDITALL\]

CHAN Network Channel Device Edit \[XUDEVEDITCHAN\]

HFS Host File Server Device Edit \[XUDEVEDITHFS\]

LPD LPD/VMS Device Edit \[XUDEVEDITLPD\]

MT Magtape Device Edit \[XUDEVEDITMT\]

RES Resource Device Edit \[XUDEVEDITRES\]

SPL Spool Device Edit \[XUDEVEDITSPL\]

TRM TRM or VTRM Device Edit \[XUDEVEDITTRM\]

![](kernel-8-0-systems-management-device-handler-user-guide/016.png) AUTHOR’S NOTE: The SDP Device Edit \[XUDEVEDITSDP\] option is purposely *not* displayed in this menu list, because it is obsolete.

### Sample Device File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patch XU\*8.0\*440 also included the addition of the SECONDARY \$I (#52) field in the DEVICE (#3.5) file.

#### HFS Devices

<u>Figure 19</u> and <u>Figure 20</u> show an HFS device using the Host File Server Device Edit \[XUDEVEDITHFS\] option to update the SECONDARY \$I (#52) field in the DEVICE (#3.5) file:

<span id="_Ref458515014" class="anchor"></span>Figure 19: HFS Device—Sample Data Entry Screen

--------------------------------------------------------------------------

EDIT A HOST FILE SERVER DEVICE

NAME: HFS <u>LOCATION</u>: Host Disk File

\$I: USER\$:\[TEMP\]MIXED.TXT

<span class="mark">ALT \$I: /TMP/MIXED.TXT</span>

SUBTYPE: P-OTHER

ASK PARAMETERS: YES MARGIN WIDTH:

ASK HOST FILE: YES PAGE LENGTH:

ASK HFS I/O OPERATION: NO VOLUME SET(CPU):

OPEN PARAMETERS: ("NWS")

CLOSE PARAMETERS:

PRE-OPEN EXECUTE:

POST-CLOSE EXECUTE:

QUEUING: ALLOWED SUPPRESS FORM FEED: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref458515026" class="anchor"></span>Figure 20: HFS Device—Sample DEVICE File Entry

NAME: <span class="mark">HFS</span> \$I: USER\$:\[TEMP\]MIXED.TXT

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: Disk ASK HOST FILE: NO

ASK HFS I/O OPERATION: YES SECONDARY \$I: /tmp/mixed.txt

OPEN COUNT: 5 SUBTYPE: P-OTHER

TYPE: HOST FILE SERVER

OPEN PARAMETERS: ("NWS")

<u>Figure 21</u> shows a printer set up as an HFS device with the Terminal Type CLOSE EXECUTE, which submits the file to the OS print queue:

<span id="_Ref458514956" class="anchor"></span>Figure 21: HFS Device—Sample Data Entry Screen with the Terminal Type CLOSE EXECUTE

EDIT A HOST FILE SERVER DEVICE

NAME: SDD P10 LOCATION: Printer next to One Xuuser

\$I: USER\$:\[TEMP\]SDD_DN2\$PRT.TXT

Alt \$I:

SUBTYPE: P-HP8000 TCP/S

ASK PARAMETERS: NO MARGIN WIDTH:

ASK HOST FILE: NO PAGE LENGTH:

ASK HFS I/O OPERATION: NO VOLUME SET(CPU):

OPEN PARAMETERS: "NWS"

CLOSE PARAMETERS:

PRE-OPEN EXECUTE:

POST-CLOSE EXECUTE:

QUEUING: SUPPRESS FORM FEED: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

#### NULL Devices

<u>Figure 22</u> and <u>Figure 23</u> shows a NULL device entry for a mixed operating system, VMS (Primary) and Linux (Secondary), using the TRM or VTRM Device Edit \[XUDEVEDITTRM\] option to update the SECONDARY \$I (#52) field in the DEVICE (#3.5) file:

<span id="_Ref458496233" class="anchor"></span>Figure 22: Mixed Operating System: VMS (Primary) and Linux (Secondary) NULL Device—Sample Data Entry Screen

Edit a TRM or VTRM device

NAME: NULL <u>LOCATION</u>: Bit Bucket

\$I: \_NLA0:

<span class="mark">ALT \$I:</span> <span class="mark">/dev/null</span>

TYPE: TERMINAL

SUBTYPE: P-OTHER

SIGN-ON/SYSTEM DEVICE: NO

VOLUME SET(CPU):

ASK DEVICE: NO MARGIN WIDTH:

ASK PARAMETERS: NO PAGE LENGTH:

QUEUING: SUPPRESS FORM FEED:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref458496293" class="anchor"></span>Figure 23: Mixed Operating System: VMS (Primary) and Linux (Secondary) NULL Device—Sample DEVICE File Entries

NAME: NULL \$I: <span class="mark">\_NLA0:</span>

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: Bit Bucket

SECONDARY \$I: <span class="mark">/dev/null</span> OPEN COUNT: 8523

SUBTYPE: P-OTHER TYPE: TERMINAL

![](kernel-8-0-systems-management-device-handler-user-guide/017.png) REF: For additional sample NULL device entries, see Section <u>3.6.4.2</u>, “[NULL Device](#null-device).”

#### BROWSER Devices

<u>Figure 24</u> shows DEVICE (#3.5) file entries for a BROWSER device:

<span id="_Ref26361291" class="anchor"></span>Figure 24: BROWSER Device—Sample DEVICE File Entry

NAME: <span class="mark">BROWSER</span> \$I: USER\$:\[BROWSER\]DDBR.TXT

ASK DEVICE: YES ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO QUEUING: NOT ALLOWED

LOCATION OF TERMINAL: BROWSER ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO SECONDARY \$I: /tmp/ddbr.txt

OPEN COUNT: 1 OPEN PARAMETERS: ("NWS")

POST-CLOSE EXECUTE: D POST^DDBRZIS I \$G(IO("CLOSE"))'="" N % S %=\$\$DEL1^%ZISH(

IO("CLOSE"))

PRE-OPEN EXECUTE: N X S X=\$\$TEST^DDBRT S:X IO=\$\$UNIQUE^%ZISUTL(IO) I 'X S %ZIS

QUIT=1,X="Browser not selectable from current terminal." W \$C(7),!,X

SUBTYPE: P-BROWSER TYPE: HOST FILE SERVER

#### P-MESSAGE Devices

<u>Figure 25</u> shows DEVICE (#3.5) file entries for a P-MESSAGE device:

<span id="_Ref507509194" class="anchor"></span>Figure 25: P-MESSAGE Device—Sample DEVICE File Entry

NAME: <span class="mark">P-MESSAGE-HFS-ONT</span> \$I: USER\$:\[TEMP\]XMHFS.TMP

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO QUEUING: ALLOWED

LOCATION OF TERMINAL: HFS FILE==\> MESSAGE

ASK HOST FILE: NO ASK HFS I/O OPERATION: NO

SECONDARY \$I: /tmp/xmhfs.tmp OPEN PARAMETERS: ("NWS")

PRE-OPEN EXECUTE: D EN^XMAPHOST Q:\$G(POP) S IO=\$\$UNIQUE^%ZISUTL(IO)

SUBTYPE: P-MESSAGE-HFS-ONT TYPE: HOST FILE SERVER

#### TELNET Devices

<u>Figure 26</u> and <u>Figure 27</u> show DEVICE (#3.5) file entries for TELNET devices:

<span id="_Ref26361340" class="anchor"></span>Figure 26: TELNET Device—Sample DEVICE File Entry (1 of 2)

NAME: <span class="mark">TELNET/LINUX</span> \$I: /dev/pts/

ASK DEVICE: YES SIGN-ON/SYSTEM DEVICE: YES

LOCATION OF TERMINAL: Telnet Terminal

OPEN COUNT: 101 SUBTYPE: C-VT320

TYPE: VIRTUAL TERMINAL

<span id="_Ref26361402" class="anchor"></span>Figure 27: TELNET Device—Sample DEVICE File Entry (2 of 2)

NAME: <span class="mark">TELNET/VMS</span> \$I: TNA

ASK DEVICE: YES ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: YES LOCATION OF TERMINAL: Telnet terminal

OPEN COUNT: 8657 SUBTYPE: C-VT320

TYPE: VIRTUAL TERMINAL

## Mixed OS Environment Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-systems-management-device-handler-user-guide/018.png) NOTE: This is for Caché only.

With the advent of remote data centers (RDCs), the VA may use mixed OS environments with a Caché Extended Caché Protocol (ECP) App/Data server configuration. In this environment output devices need different \$IO values depending on where the job is running. Kernel patch XU\*8.0\*440 added support to allow the Device Handler to work in a mixed operating system (OS) environment. The fields in <u>Table 8</u> were added to the KERNEL SYSTEM PARAMETERS (#8989.3) file to provide this support:

<table>
<caption><p><span id="_Ref29376058" class="anchor"></span>Table 9: Common Fields in the TERMINAL TYPE (#3.2) File</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MIXED OS (#.05)</td>
<td><p>This is used to select which field to use when selecting operating system (OS)-specific data fields in a mixed OS environment. The support is for Caché in an ECP client/server configuration with only two operating systems at a time. In a mixed environment the primary OS is always VMS, and the secondary OS is <em>not</em> VMS (that is Linux or NT). Some of the fields that need mixed values are:</p>
<ul>
<li><p>PRIMARY HFS DIRECTORY (#320) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file</p></li>
<li><p>SECONDARY HFS DIRECTORY (#320.2) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file</p></li>
<li><p>SECONDARY $I (#52) field in the DEVICE (#3.5) file</p></li>
</ul></td>
</tr>
<tr class="even">
<td>SECONDARY HFS DIRECTORY (#320.2)</td>
<td>This field holds the secondary HFS directory path.</td>
</tr>
<tr class="odd">
<td>LOGICAL DISK NAME (#504)</td>
<td>This field holds a logical disk name that is stored in the Caché CPF file for client system in an ECP client/server configuration.</td>
</tr>
<tr class="even">
<td>PHYSICAL DISK (#505)</td>
<td>This field holds the physical disk name to which Cache VMS converts the LOGICAL DISK NAME (#504).</td>
</tr>
<tr class="odd">
<td>SECONDARY $I (#52)</td>
<td>This field holds the <strong>$IO</strong> value to be used if this is the secondary system in a mixed OS environment. It is <em>not</em> used otherwise. It is only used for output devices.</td>
</tr>
</tbody>
</table>

<span id="_Ref29376058" class="anchor"></span>Table 9: Common Fields in the TERMINAL TYPE (#3.2) File

### Edit Logical/Physical Mapping Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Logical/Physical Mapping option \[XU SID EDIT\] option, which is located on the Kernel Management Menu \[XUKERNEL\] menu, allows you to edit the fields that support the LOGICAL to PHYSICAL translation for the System ID. This is only valid in a Caché 5.2 client/server configuration.

![](kernel-8-0-systems-management-device-handler-user-guide/019.png) NOTE: This option was released with Kernel Patch XU\*8.0\*440.

### Enter/Edit Kernel Site Parameters Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option’s Screen 3 (<u>Figure 28</u>) displays the following fields that were added to the KERNEL SYSTEM PARAMETERS (#8989.3) file:

- MIXED OS (#.05)
- SECONDARY HFS DIRECTORY (#320.2)

<span id="_Ref511302552" class="anchor"></span>

Figure 28: Enter/Edit Kernel Site Parameters Option—ScreenMan Form 3: MIXED OS (#.05) and SECONDARY HFS DIRECTORY (#320.2) Fields

--------------------------------------------------------------------------

Kernel Site Parameter edit

DOMAIN:*\<REDACTED\>*.VA.GOV

MAX SPOOL LINES PER USER: 99999

MAX SPOOL DOCUMENTS PER USER: 99

MAX SPOOL DOCUMENT LIFE-SPAN: 60

<span class="mark">MIXED OS</span>: <span class="mark">VMS/LINUX \<Enter\></span>

<u>DEFAULT DIRECTORY FOR HFS</u>: USER\$:\[TEMP\]

<span class="mark">SECONDARY HFS DIRECTORY</span>: <span class="mark">/VAR/TMP/ \<Enter\></span>

<u>DNS IP</u>: 99.9.99.99,99.8.99.999

NEW PERSON IDENTIFIERS:

--------------------------------------------------------------------------

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

![](kernel-8-0-systems-management-device-handler-user-guide/020.png) NOTE: This option was updated with Kernel Patch XU\*8.0\*440.

## Device Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To regulate who can use a particular device, you can use the PASSWORD and SECURITY fields.

The SECURITY field, if populated, should contain a string of characters to compare with a user’s FILE MANAGER ACCESS CODE (#3) field, DUZ(0), when the device is selected. Access is denied to anyone whose DUZ(0) does *not* contain one of the specified characters. As with other uses of DUZ(0), the at-sign (@; Programmer access) overrides this restriction.

The PASSWORD field, if populated, forces all users trying to log on to the device to be prompted for the matching password, before entering their Access Code.

## TERMINAL TYPE (#3.2) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TERMINAL TYPE (#3.2) file holds device vendor-specific code to characterize a terminal type. For example, escape sequences can be entered in the OPEN EXECUTE (#6) and CLOSE EXECUTE (#7) fields to set pitch or font. Every device in the DEVICE (#3.5) file *must* be assigned a terminal type, in the SUBTYPE (#3) field.

The most common fields to populate for TERMINAL TYPE (#3.2) file entries are listed in <u>Table 9</u>:

<table>
<caption><p><span id="_Ref237223209" class="anchor"></span>Table 10: Terminal Type Naming Conventions</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td><p>The name of the terminal type.</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/021.png) <strong>REF:</strong> For a description and list of acceptable terminal type name formats, see the “<a href="#terminal-type-naming-conventions">Terminal Type Naming Conventions</a>” section and <u>Table 10</u>.</p></td>
</tr>
<tr class="even">
<td>SELECTABLE AT SIGN-ON (#.02)</td>
<td>This field is used to screen the choices that can be made at the “DEVICE TYPE” prompt during signon.</td>
</tr>
<tr class="odd">
<td>RIGHT MARGIN (#1)</td>
<td>This field is the number of characters wide for this device.</td>
</tr>
<tr class="even">
<td>FORM FEED (#2)</td>
<td>The argument of an M <strong>WRITE</strong> statement that sets the top-of-form for the use of tractor-feed paper on a printer or clears the screen of a video display terminal.</td>
</tr>
<tr class="odd">
<td>PAGE LENGTH (#3)</td>
<td>This field is the number of usable lines on the output device.</td>
</tr>
<tr class="even">
<td>BACK SPACE (#4)</td>
<td>The argument of an M <strong>WRITE</strong> statement that causes the cursor to back space.</td>
</tr>
<tr class="odd">
<td>OPEN EXECUTE (#6)</td>
<td>This is the executable M code that is used by <strong>%ZIS</strong> to <strong>OPEN</strong> the terminal.</td>
</tr>
<tr class="even">
<td>CLOSE EXECUTE (#7)</td>
<td>This is the executable M code that is used by <strong>%ZIS</strong> to <strong>CLOSE</strong> the terminal [that is <strong>X ^%ZIS(“C”)</strong>].</td>
</tr>
</tbody>
</table>

<span id="_Ref237223209" class="anchor"></span>Table 10: Terminal Type Naming Conventions

The TERMINAL TYPE (#3.2) file has many more fields where additional specific information for terminal types can be entered. Kernel provides the options shown in <u>Figure 29</u> to facilitate creating and editing terminal types:

<span id="_Ref511302806" class="anchor"></span>Figure 29: Terminal Type Edit Options

Device Management ... \[XUTIO\]

Terminal Type Edit \[XUTERM\]

Change Device’s Terminal Type \[XUCHANGE\]

List Terminal Types \[XULIST\]

### Terminal Type Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The convention for naming terminal types is shown in <u>Table 10</u>:

| Terminal Type | Description                                       |
|---------------|---------------------------------------------------|
| C-        | Video terminals (such as C-VT320).            |
| PK-       | Printers with keyboards.                          |
| P-        | Printers without keyboards (such as P-LASER). |
| M-        | Modems.                                           |

<span id="_Ref29304560" class="anchor"></span>Table 11: Sample Period-delimited Pieces Used for Device Lookup

The general format is limited to two alphabetic character prefix, followed by a hyphen, and followed by alphanumeric characters.

As mentioned previously (see Section <u>2.3.1</u>), a spool document name *cannot* use this format; this is so that it can be distinguished from a device subtype in a call to the Device Handler. Confusion could arise since either can be used as the second piece of the device specification. The SPOOL DOCUMENT (#3.51) file has an input transform pattern match that guards against creation of document names in the format of device subtypes.

### How Shared Device and Terminal Type Attributes are Used

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEVICE (#3.5) and TERMINAL TYPE (#3.2) files share attribute fields for RIGHT MARGIN and PAGE LENGTH. If a value is entered for RIGHT MARGIN or PAGE LENGTH in the DEVICE (#3.5) file, it overrides the value from the TERMINAL TYPE \[#3.2\] file.

When a user selects a device by responding to the device prompt with only the first required piece of information, the device identification, Device Handler retrieves parameters to characterize the device (such as RIGHT MARGIN) from the DEVICE (#3.5) file. Furthermore, the Device Handler checks the ASK PARAMETERS (#5) flag for the selected device and, if the flag is set, prompts the user for associated parameters, presenting DEVICE (#3.5) file characteristics as the default. For terminals and virtual terminals (types TRM and VTRM, respectively), the user is prompted for the right margin. For magtape (MT), Sequential Disk Processor (SDP; obsolete), and Host File Server (HFS) devices, they can be prompted for address/parameters with the value of the OPEN PARAMETERS (#19) field (in the DEVICE \[#3.5\] file) as the default.

![](kernel-8-0-systems-management-device-handler-user-guide/022.png) REF: For more information on Magtape (MT) devices, see “<u>Special Devices</u>.”  
  
For more information on Host File Server (HFS) devices, see Section <u>4</u>, “<u>Host Files</u>.”

### Terminal Type Information Retained by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User can change some terminal type attributes of their signon device by doing either of the following:

- Changing the terminal type during the session with the Edit User Characteristics \[XUSEREDITSELF\] option.
- Selecting a device for direct output.

Kernel uses the ^XUTL global to hold information about changes made to device characteristics of the home device during a session.

![](kernel-8-0-systems-management-device-handler-user-guide/023.png) REF: For more information the ^XUTL global, see the “Menu Manager: System Management” section in the [*Kernel Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf#Menu_Manager_System_Management).

The terminal type established for users at each signon is stored in their NEW PERSON (#200) file entries so that, if necessary, it can be used as a default for the next signon.

## Devices and Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Device Selection at Signon and Virtual Terminal Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every interactive user *must* be associated with a device by the Device Handler when they sign onto the VistA system. The device association is done by matching the incoming user’s \$I (#1) field value with the \$I value of an entry in the DEVICE (#3.5) file.

Historically, it was practical to set up one device entry with a matching \$I for each physical port. With the move to OpenVMS, however, the \$I of the user was dynamic, with many thousands of \$I values possible. The Virtual Terminal device type (VTRM; see <u>Table 5</u>) was created to have one device entry to be used for signon for multiple incoming \$I values. The Device Handler still checks to see if it can assign a device to an incoming process based on an exact match of \$I values. If there is no direct match, however, Device Handler checks to see if the first part of the user’s \$I value matches the \$I value of a virtual device entry. This way, a virtual device with a \$I value of \_TNA can service all incoming processes whose \$I values start with the string TNA.

Virtual devices do *not* need a value in the VOLUME SET(CPU) (#1.9) field; they should have the SIGN-ON/SYSTEM DEVICE (#1.95) field set to YES, however, to speed up the signon device selection process.

Common device prefixes on VMS systems that could be used for virtual terminal device entries include:

- TNA—Telnet devices
- RTA—Remote processes using the SET HOST command
- FTA—Secure Shell devices

Processes on VMS systems that use Telnet usually have \$I values beginning with the prefix TNA, concatenated with an integer value and a colon (such as “TNA8456:”). A single virtual terminal device entry whose \$I value is TNA services all such processes.

### Terminal Type Selection at Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides needing a device assigned at signon, users also need a terminal type. As described in the “Signon/Security: System Management” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_System_Management), Kernel can usually determine the correct subtype without needing to prompt the user by querying the terminal and matching the returned string (if any) with return codes for terminals stored in the DA RETURN CODES (#3.22) file.

If the user is prompted to enter a terminal type, they need to choose one. The list of terminal types from which they can choose is screened by the SELECTABLE AT SIGN-ON (#.02) field in the TERMINAL TYPE (#3.2) file. Users can only choose from entries with this field set to YES. This stops users from choosing inappropriate terminal types. The setting of this field does *not* prevent terminal types from being chosen by the DA return code method, however. Make sure that all terminal types appropriate for signon have SELECTABLE AT SIGN-ON (#.02 set to YES.

If the Signon/Security system *cannot* supply even a default, the Device Handler selects according to the signon device’s subtype.

#### Managing Display Attributes (DA) Return Codes

<span id="_Toc193181760" class="anchor"></span>Figure 30: DA Return Code Edit Option

Device Management ... \[XUTIO\]

DA Return Code Edit \[XU DA EDIT\]

The DA RETURN CODES (#3.22) file stores entries for the codes returned by different terminals after Kernel prompts for their display attributes at signon. This file then maps Kernel terminal types to the terminal’s return codes. This mapping allows sites to set up mappings for new terminals or to map different terminals to a common type. For example, a site could map all codes returned by all DEC VT type terminals to a single C-VT102 type terminal type.

The DA RETURN CODES (#3.22) file is a small static file managed by the DA Return Code Edit option \[XU DA EDIT\]. You can use the DA Return Code Edit option \[XU DA EDIT\] option to automate the population of the DA RETURN CODES (#3.22) file. When you select this option, the terminal you are using is queried and you are shown the terminal’s DA code response. You are then prompted for the terminal type and description for this return code. Enter the terminal type name for the terminal you are using. The option updates the DA RETURN CODES (#3.22) file, and all terminals responding with this code are recognized at signon. You can quickly populate the DA RETURN CODES (#3.22) file by using this option from several different types of terminals.

Kernel pre-populates the DA RETURN CODES (#3.22) file with a set of standard terminal type entries. You may need to add more entries as needed to handle all terminals at your site.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181761" class="anchor"></span>Figure 31: Device Management—Troubleshooting Options

SYSTEM MANAGER MENU \[EVE\]

Device Management... \[XUTIO\]

Loopback Test of Device Port \[XUTLOOPBACK\]

Send Test Pattern to Terminal \[XUTTEST\]

Out of Service Set/Clear \[XUOUT\]

Kernel provides several options on the Device Management \[XUTIO\] menu to aid with troubleshooting device problems, which are described in the sections that follow.

### Loopback Test of Device Port Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Loopback Test of Device Port \[XUTLOOPBACK\] option to test an RS-232 serial data line when using a loopback connection on the line. First, disconnect the data line from the device it is attached to (if any). Then, tie pins 2 and 3 of the RS-232 serial data line together. This is a loopback connection; data sent down pin 2 (transmit) loops back up pin 3 (receive). The Loopback Test of Device Port \[XUTLOOPBACK\] option sends the letters of the alphabet down the data line one at a time, and it attempts to READ them back. If both lines are intact, you should see “ABCDEFGHIJKLMNOPQRSTUVWXYZ” print on the terminal from which you are testing the data line.

### Send Test Pattern to Terminal Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Send Test Pattern to Terminal \[XUTTEST\] option to send a simple test pattern to a device. This is an easy way to verify whether a device is connected to the system. It lets you choose how many lines of the test pattern to send and then sends that number of lines to the device. You can confirm on the device end exactly how many lines of the test pattern you receive, which can be useful when troubleshooting printer handshaking problems.

### Out of Service Set/Clear Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Out of Service Set/Clear \[XUOUT\] option to set a device out of order. It asks you the date on which to put the device out of order. From that date forward, the Device Handler does *not* allow any jobs to use the device (users get a message that the device is out of order). To clear the out of order status, use this option again and delete the out of order date.

### Verify HFS and NULL Device Setup *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HFS Device

Verify you have a Host File Server (HFS) device in the DEVICE (#3.5) file named HFS. If you have performed KIDS installations on your server before, you probably already have an appropriate HFS device set up. If you do *not* have an entry for this device, you *must* create one.

![](kernel-8-0-systems-management-device-handler-user-guide/024.png) REF: For information on how to create an HFS device, see “<u>Host Files</u>.”

#### NULL Device

Verify you have a NULL device in the DEVICE (#3.5) file named NULL (or whose mnemonic is named NULL). You can have other devices with similar names, but one device is needed whose name or mnemonic is NULL. The subtype should be a “P-” subtype (such as P-OTHER), the margin should be a minimum of 80, and the page length should be a minimum of 60. Sample setups:

<span id="_Toc207534522" class="anchor"></span>Figure 32: VMS NULL Device—Sample DEVICE File Entry

NAME: NULL \$I: <span class="mark">\_NLA0:</span>

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: BIT BUCKIT

SUBTYPE: P-OTHER TYPE: TERMINAL

<span id="_Toc207534523" class="anchor"></span>Figure 33: Mixed Operating System: VMS (Primary) and Linux (Secondary) NULL Device—Sample DEVICE File Entry

NAME: NULL \$I: <span class="mark">\_NLA0:</span>

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: Bit Bucket

SECONDARY \$I: <span class="mark">/dev/null</span>

SUBTYPE: P-OTHER TYPE: TERMINAL

<span id="_Toc207534524" class="anchor"></span>Figure 34: Linux NULL Device Example—Caché NULL Device Setup

NAME: NULL \$I: <span class="mark">/dev/null</span>

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: BIT BUCKIT

SUBTYPE: P-OTHER TYPE: TERMINAL

<span id="_Toc207534525" class="anchor"></span>Figure 35: Windows NULL Device Example—Caché NULL Device Setup

NAME: NULL <span class="mark">\$I: //./nul</span>

ASK DEVICE: NO ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: BIT BUCKIT

SUBTYPE: P-OTHER TYPE: TERMINAL

<u>Figure 36</u> is the TERMINAL TYPE (#3.2) file entry that is used by all NULL device configurations.

<span id="_Ref458576042" class="anchor"></span>Figure 36: NULL Device Example—P-OTHER Terminal Type Setup

NAME: P-OTHER RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 64

BACK SPACE: \$C(8) DESCRIPTION: General prntr (132)

## Device Identification and Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Devices can be selected in several ways from the “DEVICE:” prompt. Besides the NAME (#.01) field, three other attributes: MNEMONIC, LOCAL SYNONYM, and \$I can also be used to select devices. When LOCAL SYNONYM is used, the Device Handler searches the local CPU for a match. Thus, the same LOCAL SYNONYM value (such as PRINTER) can be used to identify several devices, one per CPU.

When editing devices through VA FileMan, two additional fields can be used for lookup:

- VOLUME SET(CPU) (#1.9)
- SIGN-ON/SYSTEM DEVICE (#1.95)

You can separate these values with a period delimiter, as shown in <u>Table 11</u>:

| Period-delimited Piece | Description                                   |
|------------------------|-----------------------------------------------|
| CPU                    | All devices matching CPU.                     |
| CPU.\$I                | All devices matching the CPU and \$I.     |
| SYS                    | All SIGN-ON DEVICES.                          |
| SYS.CPU                | All SIGN-ON DEVICES matching CPU.             |
| SYS.\$I                | All SIGN-ON DEVICES matching \$I.         |
| SYS.CPU.\$I            | All SIGN-ON devices matching CPU and \$I. |

<span id="_Ref29304663" class="anchor"></span>Table 12: HFS Input/Output Modes of Operation

For example, to display all signon devices on CPU “BBB”, you could do:

<span id="_Toc193181763" class="anchor"></span>Figure 37: Displaying Signon Devices on a Specific CPU—Sample User Dialog

Select DEVICE NAME: <span class="mark">SYS.BBB \<Enter\></span>

To display all signon devices whose \$I begins with \_TNA you could do:

<span id="_Toc193181764" class="anchor"></span>Figure 38: Displaying Signon Devices with a Specific \$I—Sample User Dialog

Select DEVICE NAME: <span class="mark">SYS..\_TNA \<Enter\></span>

The ^%ZIS global listing in <u>Figure 39</u> shows the cross-references for a device with a \$I value of 99 and an internal entry number (IEN) of 251. It is a SIGN-ON/SYSTEM DEVICE (#1.95) and has a VOLUME SET(CPU) (#1.9) value of AAA.

<span id="_Ref237226577" class="anchor"></span>Figure 39: Global Listing for Device Cross-references—\$I Value = 99 and IEN = 251

^%ZIS(1,"G","SYS.AAA.99",251) = ""

^%ZIS(1,"CPU","AAA.99",251) = ""

^%ZIS(1,"C","99",251) = ""

If this device is a virtual terminal with a \$I of \_TNA and established as a SIGN-ON/SYSTEM DEVICE (#1.95) but *not* given a VOLUME SET(CPU) (#1.9) value, the cross-reference structure would be as shown in <u>Figure 40</u>:

<span id="_Ref33081822" class="anchor"></span>Figure 40: Global Listing for Virtual Terminal Device Cross-references—\$I Value = \_TNA and IEN = 251

^%ZIS(1,"G","SYS..\_TNA",251) = ""

^%ZIS(1,"CPU",".\_TNA",251) = ""

^%ZIS(1,"C","\_TNA",251) = ""

# Host Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Host Files: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Host File Server (HFS) devices allow you to send output to a file maintained by your computer’s operating system, rather than to a printer. You can send your output to an HFS device, if such a device type has been established on the system. Depending upon how system administrators define the HFS device, you may be prompted for a host file name and for an input/output operation:

<span id="_Toc193181767" class="anchor"></span>Figure 41: Choosing a Host File Server (HFS) Device—Sample User Dialog

DEVICE: <span class="mark">HFS \<Enter\></span> DISK FILE

HOST FILE NAME: TMP.TMP// <span class="mark">\<Enter\></span> INPUT/OUTPUT OPERATION: <span class="mark">? \<Enter\></span>

Enter one of the following host file input/output operation:

R = READONLY

N = NEWVERSION

RW = READ/WRITE

Not all input/output modes are available on all systems. The possible modes for input/output operation work are shown in <u>Table 12</u>:

| Input/Output Mode | Description                                                                                                                              |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| APPEND        | Data from a WRITE operation is appended to the file.                                                                                 |
| MIXED         | Both READs and WRITEs are allowed for the specified file.                                                                        |
| NEWVERSION    | A new file is created with a higher version number; this file can be used for WRITEs only.                                           |
| READ          | READs are allowed from the specified file; WRITEs are *not* allowed.                                                             |
| READONLY      | READs are allowed from the specified file; WRITEs are *not* allowed.                                                             |
| READ/WRITE    | Both READs and WRITEs are allowed for the specified file; if a WRITE operation is performed, output is appended to the file. |
| WRITE         | WRITEs are allowed; output can be sent to the specified file.                                                                        |

<span id="_Ref29376214" class="anchor"></span>Table 13: HFS-related Fields in the DEVICE (#3.5) File

## Host Files: System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To provide access to host files through the Device Handler, set up device entries of type HFS.

<u>Table 13</u> lists the three fields in an HFS device entry that act as flags for what a user *must* enter when they use an HFS device:

| Field                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASK PARAMETERS (#5)          | If this field is set to YES, the user *must* enter the correct M open parameters to open the device. This field should be set to NO if the device is accessible to *non*-system administrator users. If it is set to YES, the default value is the current value of the OPEN PARAMETERS (#19) field.                                                                                                                                                        |
| ASK HOST FILE (#5.1)         | When this field is set to YES, the user can choose what file is opened. If it is set to NO, the default file name built into the device entry is always used. This field should be set to NO if the HFS device is accessible to *non*- system administrator users. Host files can proliferate if too many users are able to create many files. Also, an HFS device opens access to the host operating system and the potential for overwriting vital files. |
| ASK HFS I/O OPERATION (#5.2) | If this field is set to YES, the user can choose in what mode the file should be opened (such as READ or WRITE). If it is set to NO, files are opened in WRITE mode. This should be set to NO if the device is accessible to *non*-system administrator users, if all such users would only need to WRITE host files.                                                                                                                       |

<span id="_Toc193181770" class="anchor"></span>Table 14: HFS I/O Operation Modes for Caché and GT.M

### Host File Server Device Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181769" class="anchor"></span>Figure 42: Host File Server Device Edit Option

Device Management... \[XUTIO\]

Edit Devices by Specific Types... \[XUDEVEDIT\]

Host File Server Device Edit \[XUDEVEDITHFS\]

The Host File Server Device Edit \[XUDEVEDITHFS\] option lets you to edit Host File Server device attributes using a ScreenMan form.

### Caché and GT.M HFS Device Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Caché and GT.M require the name of the host file to be part of the device \$I and *not* part of the parameter list.

| I/O Operation Mode | Description                                                                                                                              |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| NEWVERSION     | A new file is created (on VMS with a higher version number); this file can be used for WRITEs only.                                  |
| READONLY       | READs are allowed from the specified file; WRITEs are *not* allowed.                                                             |
| READ/WRITE     | Both READs and WRITEs are allowed for the specified file; if a WRITE operation is performed, output is appended to the file. |

<span id="_Ref511308373" class="anchor"></span>Table 15: User Spooler-related Fields in the NEW PERSON (#200) File

<span id="_Toc193181771" class="anchor"></span>Figure 43: Host File Server Device for Caché and GT.M—Sample Settings

Name: HFS

\$I: TMP.TMP

Type: HFS

Ask Parameters: NO

Ask Host File: NO

Ask HFS I/O Operation: NO

Open Parameters: ("NWS")

# Spooling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Spooling: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Spooling privileges can be granted by system administrators to users who prepare and manage reports. By sending your output to the spooler, rather than to a printer, you can benefit in several ways. Since spooling saves the output online in a holding area, you can easily print multiple copies of the report later. Spooling is also a good way to store the results of a time-consuming calculation (such as a complex VA FileMan report). By queuing to the spooler, a report involving intensive processing can be done at night or off hours when the system is relatively free. Output can then be printed during the day when the printer can be attended. Finally, when using the spooler, report processing can run to completion without printer problems interfering.

### Sending Output to the Spooler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have been given the authority to spool, you can send output to the spooler by responding to the “DEVICE:” prompt with the name of the spool device. Devices used for spooling are commonly named SPOOL or SPOOLER.

If you do *not* have spooling privileges and you try to use the spool device, the spooler issues a message that authority has *not* been granted, as shown in <u>Figure 44</u>:

<span id="_Ref26361585" class="anchor"></span>Figure 44: Unable to Send Output to a Spool Device—Sample Message

DEVICE: <span class="mark">SPOOL \<Enter\></span>

You aren't an authorized SPOOLER user.

To send output to the spooler with a customized right margin of 96 and page length of 66, you can use the syntax in <u>Figure 45</u>:

<span id="_Ref26361554" class="anchor"></span>Figure 45: Specifying Spooled Output Margin and Length

DEVICE: <span class="mark">SPOOL;96;66 \<Enter\></span>

After requesting the spool device, you are usually prompted for a spool document name, as shown in <u>Figure 46</u>. The prompt is *not* issued, however, if the spool device has been set up to generate the spool document name itself.

<span id="_Ref86567834" class="anchor"></span>Figure 46: Spool Document Name Prompt

DEVICE: <span class="mark">SPOOL \<Enter\></span>

Select SPOOL DOCUMENT NAME:

To skip the “Select SPOOL DOCUMENT NAME:” prompt, you can specify the spool document name at the “DEVICE:” prompt by entering the name in the second semicolon piece. A name entered here is *not* used if the spooler is set up to generate names itself, however. Because of the format used, the Device Handler knows that a spool document name, rather than a device subtype, is being specified. Subtypes begin with one or two letters followed by a hyphen (such as P-DEC), while spool document names *cannot* (see Section <u>2.3.1</u>).

<span id="_Toc193181775" class="anchor"></span>Figure 47: Specifying Spool Device and Document Name

DEVICE: <span class="mark">SPOOL;MYDOC \<Enter\></span>

DEVICE: <span class="mark">SPOOL;P-OTHER80;MYDOC \<Enter\></span>

If the computing environment is composed of several networked processors, you may need to specify where spooling should take place. The spooler on the current CPU should be chosen unless the output is queued.

<span id="_Toc193181776" class="anchor"></span>Figure 48: Spooling Output to a Spool Device on the Same CPU

DEVICE: <span class="mark">SPOOL \<Enter\></span>

1 SPOOL AAA

2 SPOOL BBB

Choose 1-2\>

If the output is queued, you can choose a spooler on another CPU and a time to schedule the job to run.

<span id="_Toc193181777" class="anchor"></span>Figure 49: Queuing Output to a Spool Device

DEVICE: <span class="mark">Q \<Enter\></span>

DEVICE: <span class="mark">SPOOL BBB \<Enter\></span>

<span id="_Toc193181778" class="anchor"></span>Figure 50: Spooler Parameters at the Device Prompt (Summary)

DEVICE: Spooler

DEVICE: Spooler;Right Margin;Page Length

DEVICE: Spooler;Subtype

DEVICE: Spooler;Spool Document Name

DEVICE: Spooler;Subtype;Spool Document Name

### Retrieving Spooled Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a spool document has been created, you can retrieve the output by using options on the Spooler Menu \[XU-SPL-MENU\] menu. This menu is distributed as part of Kernel’s SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu), a menu available to all users. Specifically, the Spooler Menu \[XU-SPL-MENU\] is in your User’s Toolbox \[XUSERTOOLS\] menu.

To quickly reach the Toolbox or any other option on the Common menu, you can enter a quotation mark plus the menu text or synonym, as shown in <u>Figure 51</u>:

<span id="_Ref455484942" class="anchor"></span>Figure 51: Spooler Menu Options

Select Primary Menu Option: <span class="mark">"TBOX \<Enter\></span>

Select User’s Toolbox Option: <span class="mark">SPOOLER MENU \<Enter\></span>

Select Spooler Menu Option: <span class="mark">?</span><span class="mark">\<Enter\></span>

Allow other users access to spool documents \[XU-SPL-ALLOW\]

Browse a Spool Document \[XU-SPL-BROWSE\]

Delete A Spool Document \[XU-SPL-DELETE\]

List Spool Documents \[XU-SPL-LIST\]

Make spool document into a mail message \[XU-SPL-MAIL\]

Print A Spool Document \[XU-SPL-PRINT\]

#### List Spool Documents Option

The List Spool Documents \[XU-SPL-LIST\] option lists any documents that you have created. Other users *cannot* read or print these documents unless you have authorized them to do so with the Allow other users access to spool documents \[XU-SPL-ALLOW\] option, also on the Spooler Menu \[XU-SPL-MENU\].

#### Delete A Spool Document Option

Use the Delete A Spool Document \[XU-SPL-DELETE\] option to delete spool documents. Since there is a limit on the amount of spool space that any one user can consume, you may need to delete old spool documents to free up space for new ones. If you attempt to create a new document when the space limits have been exceeded, the spooler issues a message about the need to delete some documents.

Old documents are deleted automatically, on a schedule as determined by system administrators. System administrators set the “life span” of a spool document through the MAX SPOOL DOCUMENT LIFE-SPAN (#31.3) field in the KERNEL SYSTEM PARAMETERS (#8989.3) File. System administrators should inform you of the life span of spooled documents, so that you are *not* surprised when old documents are purged.

### Browsing a Spool Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Browse a Spool Document Option

With the Browse a Spool Document \[XU-SPL-BROWSE\] option, you can view spool documents with VA FileMan’s Browser.

The Browser allows you to:

- View spool documents on your terminal screen.
- Scroll backward and forward through the report.
- Perform simple searches within the report.

![](kernel-8-0-systems-management-device-handler-user-guide/025.png) REF: For more information on using the Browser, see the *VA FileMan User Manual*.

### Printing Spool Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Print A Spool Document Option

Use the Print A Spool Document \[XU-SPL-PRINT\] option to print spool documents. Before selecting an output device, you are prompted for the number of copies to print. If you have been granted the ability to print to multiple devices, you can send your output to several devices for simultaneous printing. If this privilege has been granted to you, the device prompt is displayed again after you choose the first printer. Entering a NULL response to the second device prompt tells the spooler *not* to use any more additional printers.

To save users the time and trouble of despooling their documents, system administrators can set up a spool device for auto-despooling. If you invoke such a spool device, the spool document is sent to one or more printers when the spooling process has completed. After automatic printing, the spool document remains available for reprinting as necessary (it is *not* automatically deleted upon despooling).

### Making Spool Documents into Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Make spool document into a mail message Option

If you have been granted the ability to make spool documents into mail messages, the Make spool document into a mail message \[XU-SPL-MAIL\] option on the Spooler Menu \[XU-SPL-MENU\] is available. You can use it to make documents into regular mail messages that can then be edited, copied, or forwarded just like other VistA MailMan messages. After the text has been moved into a mail message, the spool document is deleted. The deletion is to allow space for new spool documents.

If you plan to make a document into a message, you should do the original output to the spool device with an appropriate margin and page length for a MailMan message. Since MailMan breaks incoming text lines at about the 75th character, a right margin of 75 may be desirable. Indicating that page breaks should *not* be inserted during the spooling process may also be desirable. Otherwise, the VA FileMan window command \|TOP\| is inserted into the text at the beginning of each page. While this automatic formatting is an advantage when printing spool documents, it is a disadvantage when creating a mail message. Page breaks are *not* inserted when indicating a page length of 99999 lines or a number greater than the document’s total.

Therefore, when you know your spool document is to be a MailMan message, a suitable margin and page length request might be what is shown in <u>Figure 52</u>:

<span id="_Ref33081955" class="anchor"></span>Figure 52: Formatting/Sending a Document to a Spool Device to Print as a MailMan Message—Sample User Dialog

DEVICE: <span class="mark">SPOOL;75;99999 \<Enter\></span>

To turn the spool document into a MailMan message, once your spool document completes, go to the Spooler Menu \[XU-SPL-MENU\] and select the appropriate option, as shown in <u>Figure 53</u>:

<span id="_Ref511308169" class="anchor"></span>Figure 53: Make Spool Document into a Mail Message Option

Select Primary Menu Option: <span class="mark">^SPOOLER MENU \<Enter\></span>

Select Spooler Menu Option: <span class="mark">MAKE SPOOL DOCUMENT INTO A MAIL MESSAGE \<Enter\></span>

If the number of lines in the document exceeds 500, you are asked whether the transfer process should be queued. This prompt is provided for your convenience since queuing of a time-consuming process is usually preferred. After using the option, you can find your messages by reviewing recently delivered mail in your MailMan IN basket.

## Spooling: System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Spool Document Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Spool document identification is stored in the SPOOL DOCUMENT (#3.51) file in the ^XMB global. This file is for internal use by Kernel’s spooler and should *not* be directly manipulated by system administrators. It holds identifying information, such as the name of the spool document and the line count totals. The document’s text is stored in the SPOOL DATA (#3.519) file in the ^XMBS global. If the spool document is made into a mail message, the text is moved into the MESSAGE (#3.9) file, the ^XMB global, and the corresponding entry in the SPOOL DOCUMENT (#3.51) file is deleted.

When initially creating a spooled document, output is sent to the operating system’s spooling area (as defined in the spool device). Kernel’s spooler moves the output into the ^XMBS global when the operating system’s spooling process is complete. The status of the document (a field in the SPOOL DOCUMENT \[#3.51\] file) is then changed from Active to Ready and the document can be accessed by the user. Thus, except during spooling, the operating system’s spool area should be empty.

### Overflowing Spool Document Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the output is moved from the operating system’s spool area into the ^XMBS global, the lines are counted. If during the count the user’s maximum line limit is reached (as defined in the MAX SPOOL LINES PER USER \[#31.1\] field in the KERNEL SYSTEM PARAMETERS \[#8989.3\] file), the transfer process is halted, and a notification message is appended to the transferred text. The entry in the SPOOL DOCUMENT (#3.51) file is also marked as incomplete. Thus, the ^XMBS global is protected from growth expansion that could overflow the disk storage area.

The Kernel spooler *cannot*, however, count the lines of output as they are sent to the operating system’s spool area. If the user’s line limit is *not* exceeded before initiating the report, Kernel permits sending of an unlimited amount of output to the operating system’s spooler. System administrators should consider this when granting spooling privileges. Users who are allowed to spool should be trained accordingly.

Users need to anticipate the results of a process they send to the spooler. If they are *not* sure what to expect, they should be instructed to test the process by sending it directly to an output device. If unexpected results should occur (such as an endless loop or meaningless sort), they can interrupt and cancel the process. Users should also be advised about appropriate use of processing time. Methods of efficient VA FileMan searching and sorting should be used when invoking the spooler (just as when printing directly). For example, as described in the VA FileMan documentation, the first sort-by field should be a cross-referenced field when possible and search criteria should be specified with the most likely conditions first.

### Granting Spooling Privileges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Options on the Spool Management \[XU-SPL-MGR\] menu can be used to grant spooling privileges to users.

<span id="_Toc193181782" class="anchor"></span>Figure 54: Edit User’s Spooler Access Option

SYSTEMS MANAGER MENU ... \[EVE\]

Spool Management ... \[XU-SPL-MGR\]

Edit User’s Spooler Access \[XU-SPL-USER\]

<u>Table 15</u> lists the spooler-related fields that are user-specific and are stored in the NEW PERSON (#200) file:

| Field                                | Description                                                                                                                                                                                                                                                                                                            |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALLOWED TO USE SPOOLER (#41)         | If set to YES it gives the user the ability to invoke the spooler at the device prompt.                                                                                                                                                                                                                            |
| MULTI-DEVICE DESPOOLING (#41.1)      | If set to YES it enable the user to despool a spooled document to more than one device simultaneously.                                                                                                                                                                                                             |
| CAN MAKE INTO A MAIL MESSAGE (#41.2) | If set to YES it permits the conversion of a spool document into a MailMan mail message. The user can use all MailMan functions, such as copying and forwarding. As a mail message, the document can no longer be manipulated with the spooler since its flag in the SPOOL DOCUMENT (#3.51) file has been deleted. |

<span id="_Ref511308533" class="anchor"></span>Table 16: Spooler Site Parameter Fields in the KERNEL SYSTEM PARAMETERS (#8989.3) File

As mentioned earlier, the user-oriented spooler options are distributed as part of the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu), a menu available to all users. If system administrators have chosen to lock the Spooler Menu \[XU-SPL-MENU\] or removed it from the Common menu, access to the options needs to be re-established for users who are allowed to spool using the Edit User’s Spooler Access \[XU-SPL-USER\] option, as shown in <u>Figure 55</u>:

<span id="_Ref511308225" class="anchor"></span>Figure 55: Edit User’s Spooler Access—Sample User Dialog

Select Spool Management Option: <span class="mark">EDIT USER'S SPOOLER ACCESS \<Enter\></span>

Select NEW PERSON NAME: <span class="mark">XUUSER,SIX \<Enter\></span>

ALLOWED TO USE SPOOLER: YES// <span class="mark">\<Enter\></span>

MULTI-DEVICE DESPOOLING: YES// <span class="mark">\<Enter\></span>

CAN MAKE INTO A MAIL MESSAGE: YES// <span class="mark">\<Enter\></span>

### Managing Spool Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The remaining options on the Spool Management \[XU-SPL-MGR\] menu (<u>Figure 56</u>) are also found on the user-oriented Spooler Menu \[XU-SPL-MENU\]. They are provided on the Spool Management \[XU-SPL-MGR\] menu simply for convenience to system administrators to access any spool document on the system. Users *must* hold the XUMGR security key to access all spool documents. Together, these options along with the XUMGR security key permit system administrators to view, print, or delete anyone’s spooled documents.

<span id="_Ref67467220" class="anchor"></span>Figure 56: Spool Management Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Spool Management ... \[XU-SPL-MGR\]

Delete A Spool Document \[XU-SPL-DELETE\]

List Spool Documents \[XU-SPL-LIST\]

Print A Spool Document \[XU-SPL-PRINT\]

### Spooler Site Parameters Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181785" class="anchor"></span>Figure 57: Spooler Site Parameters Option

SYSTEMS MANAGER MENU ... \[EVE\]

Spool Management ... \[XU-SPL-MGR\]

Spooler Site Parameters Edit \[XU-SPL-SITE\]

The Spool Management \[XU-SPL-MGR\] menu also has the Spooler Site Parameters Edit \[XU-SPL-SITE\] option for setting the spooler site parameters (system-wide defaults for the spooler). The initial settings are defined when installing Kernel but can be edited afterwards.

The spooler site parameters control the total number of documents a user can create and the total number of lines for all documents. When the limits are reached, the user *cannot* create new spooled documents.

<u>Table 16</u> lists the effects of the three spooler site parameter fields:

| Spooler Site Parameter Field         | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAX SPOOL LINES PER USER (#31.1)     | This field holds the MAX number of lines of spooled output a user is allowed. If the user has more than this number, then they are *not* permitted to spool any more until some of their spool documents are deleted. This only controls allowing the creation of new spool documents and does *not* terminate a job that is running that has gone over the limit. Recommended value 9999. |
| MAX SPOOL DOCUMENTS PER USER (#31.2) | This field limits the number of spool documents that any user can have on the system. Recommended value 10-100.                                                                                                                                                                                                                                                                            |
| MAX SPOOL DOCUMENT LIFE-SPAN (#31.3) | This field controls the number of days that a spooled document is allowed to remain in the spooler before deletion by the Purge old spool documents \[XU-SPL-PURGE\] option that needs to be setup to run in the background.                                                                                                                                                                   |

<span id="_Ref237246232" class="anchor"></span>Table 17: Fields in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) Files that May Not be Relevant for Certain Devices

### Purge old Spool documents Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181787" class="anchor"></span>Figure 58: Purge old Spool documents Option

PARENT OF QUEUABLE OPTIONS \[ZTMQUEUABLE OPTIONS\]

Purge old spool documents \[XU-SPL-PURGE\]

A spool document is automatically deleted when its life span (in days) is reached. The purge is carried out by the Purge old spool documents \[XU-SPL-PURGE\] option. This option is listed on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu along with others that should *not* be invoked interactively but should be scheduled to run through TaskMan.

### Defining Spool Device Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEVICE (#3.5) file entries for spooler device types make use of information about the underlying operating system’s spooling mechanism. Examples for several operating systems are provided in the topics that follow.

#### Caché and GT.M

Caché and GT.M use an OpenVMS directory for spooling. As indicated in the VistA Cookbook for VAX sites, the directory should be established with full privileges for System, Owner, Group, and World. The directory specifications are used as the \$I value.

<span id="_Toc193181788" class="anchor"></span>Figure 59: Spool Device for Caché and GT.M

Name: SPOOL

\$I: VA1\$:\[SPOOLER\]

Type: SPOOL

Subtype: P-OTHER

### Spool Device Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Spool Device Edit \[XUDEVEDITSPL\] option lets you edit spool device attributes using a ScreenMan form.

<span id="_Toc193181789" class="anchor"></span>Figure 60: Spool Device Edit Option

Device Management... \[XUTIO\]

Edit Devices by Specific Types... \[XUDEVEDIT\]

Spool Device Edit \[XUDEVEDITSPL\]

![](kernel-8-0-systems-management-device-handler-user-guide/026.png) NOTE: The type of data entered in the \$I (#1) and OPEN PARAMETERS (#19) fields depends on the type of M system you are using and the mode of access.

![](kernel-8-0-systems-management-device-handler-user-guide/027.png) REF: For further details, see your M system manuals.  
  
REF: Examples are provided in the “[Defining Spool Device Types](#defining-spool-device-types)” section.

### Auto-Despooling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For convenience, spool devices can be defined to ensure that despooling takes place automatically, without user interaction. If the AUTO DESPOOL (#31) field in the DEVICE (#3.5) file is set to YES, one copy of the spooled output is sent to each device named in the DESPOOL DEVICES (#32) Multiple field. Having the output automatically despooled saves users the time and trouble of logging on and printing a spool document that may have been created the previous evening. Documents are *not* deleted upon despooling; they remain available to the user for subsequent printing.

<span id="_Toc193181790" class="anchor"></span>Figure 61: Device Edit Option—Sample User Dialog

Select Device Handler Option: <span class="mark">DEVICE EDIT \<Enter\></span>

Select DEVICE NAME: <span class="mark">SPOOL \<Enter\></span>

NAME: SPOOL// <span class="mark">^AUTO D \<Enter\></span> ESPOOL

AUTO DESPOOL: <span class="mark">1 \<Enter\></span> YES

Select DESPOOL DEVICES:

### Generating Spool Document Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Spool devices can be set up to automatically generate the name that identifies the spool document. If the GENERATE SPL DOC NAME (#33) field in the DEVICE (#3.5) file is set to YES, users of that device are *not* prompted to enter the spool document name. Also, if the flag is set, any user- or developer-defined name \[in IO(“DOC”)\] is ignored. The generated name consists of the first 15 characters of the spool device’s name, followed by an underscore (\_), and followed by the internal entry number (IEN) of the spool document in the SPOOL DOCUMENT (#3.51) file.

<span id="_Toc193181791" class="anchor"></span>Figure 62: Generating Spool Document Name—Sample User Dialog

NAME: SPOOL// <span class="mark">^GENERATE SPL DOC NAME \<Enter\></span>

GENERATE SPL DOC NAME: <span class="mark">YES \<Enter\></span>

# Special Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the following special devices and device issues:

- [Browser Device](#_Toc236534747)
- [Form Feeds](#form-feeds)
- [Magtape](#magtape) (MT)
- [Network Channel Devices](#network-channel-devices)
- [Resources](#resources)
- [Sequential Disk Processors (Obsolete)](#sequential-disk-processors-obsolete)
- [Slaved Printers](#slaved-printers)

<span id="_Toc236534747" class="anchor"></span>

## Browser Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Browser User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan’s Browser allows you to:

- View reports on your terminal screen.
- Scroll backward and forward through the report.
- Perform simple searches within the report.

If the Browser has been installed at your site and set up as a device, you can use the Browser to view any report that asks you for an output device.

To send a report to the BROWSER device, at any device prompt, enter BROWSER as the device. You may *not* want to send huge reports to the BROWSER, however, since the report *must* complete before you can view its output in the Browser.

![](kernel-8-0-systems-management-device-handler-user-guide/028.png) REF: For information on using the Browser and on Browser commands, see the *VA FileMan User Manual*.

<span id="_Toc193181792" class="anchor"></span>Figure 63: Print File Entries Option—Sample User Dialog when Sending a Report to the Browser Device

Select VA FileMan Option: <span class="mark">PRINT FILE ENTRIES \<Enter\></span>

OUTPUT FROM WHAT FILE: NEW PERSON// <span class="mark">DOMAIN \<Enter\></span> (314 entries)

SORT BY: NAME// <span class="mark">\<Enter\></span>

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">NAME \<Enter\></span>

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

HEADING (S/C): DOMAIN LIST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">BROWSER \<Enter\></span> BROWSER

BROWSER TITLE (optional): VA FileMan Browser// <span class="mark">\<Enter\></span>

...one moment...

<span id="_Toc193181793" class="anchor"></span>Figure 64: Print File Entries Option—Sample Domain List report, as Displayed in the Browser Device

VA FileMan Browser

DOMAIN LIST JUL 28,2009 12:44 PAGE 1

NAME

--------------------------------------------------------------------------

*\<REDACTED01\>*.VA.GOV

*\<REDACTED02\>*.VA.GOV

*\<REDACTED03\>*.VA.GOV

*\<REDACTED04\>*.VA.GOV

*\<REDACTED05\>*.VA.GOV

*\<REDACTED06\>*.VA.GOV

*\<REDACTED07\>*.VA.GOV

*\<REDACTED08\>*.VA.GOV

*\<REDACTED09\>*.VA.GOV

*\<REDACTED10\>*.VA.GOV

*\<REDACTED11\>*.VA.GOV

*\<REDACTED12\>*.VA.GOV

*\<REDACTED13\>*.VA.GOV

*\<REDACTED14\>*.VA.GOV

*\<REDACTED15\>*.VA.GOV

*\<REDACTED16\>*.VA.GOV

*\<REDACTED17\>*.VA.GOV

*\<REDACTED18\>*.VA.GOV

Col\> 1 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 22 of 320 Screen\> 1 of 15

### Browser System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can set up VA FileMan’s Browser as a device to which users can send their output.

When a user sends output to a Browser device, the Browser device performs the following steps:

1.  Output is sent to a host file.
2.  When the output completes, the host file is closed.
3.  The contents of the host file are read back into a scratch global.
4.  The host file is deleted.
5.  The Browser is called, which displays the data in the global to the user, through the Browser interface.
6.  When the user exits the Browser, the scratch global is deleted.

This provides a quick way to generate a report and view the report through the scrollable Browser, potentially saving paper and wear and tear on printers.

To support the Browser device, you need to set up a special terminal type (P-BROWSER) and a special device type (BROWSER).

![](kernel-8-0-systems-management-device-handler-user-guide/029.png) REF: For sample entries of the special Browser terminal type and device entries for the Caché and GT.M operating systems, see <u>Figure 65</u> and <u>Figure 66</u>.

The Browser device tests the current terminal to see whether it supports:

- A scrolling region.
- Reverse indexing.

If the terminal does *not* support these features, the Browser device issues a message saying that it is *not* selectable from the current terminal. Also, for the check (\$\$TEST^DDBRT) to work properly, the user *must* already be in the Kernel menu system or *must* have set up developer variables through the ^XUP entry point. Otherwise, the test always fails.

#### Storing Host Files in a Specific Directory

By default, the temporary host files created by the Browser device are stored in the current default directory. You can optionally specify a path to a specific directory to store the temporary host files. Make sure the directory you specify exists on all nodes/CPUs where users can sign on. On DOS systems, do *not* specify the root directory, since there is a limit on the number of files a DOS root directory can hold. Finally, make sure you change both the OPEN PARAMETERS (#19), and POST-CLOSE EXECUTE (#19.8 fields in the Browser DEVICE (#3.5) file entry to specify the directory (replace DD with, for example, D:\BROW\DD).

<span id="_Ref85879477" class="anchor"></span>Figure 65: Caché and GT.M Browser Device—TERMINAL TYPE (#3.2) File Entry

NAME: P-BROWSER SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 99999 BACK SPACE: \$C(8)

OPEN EXECUTE: D OPEN^DDBRZIS

CLOSE EXECUTE: D CLOSE^DDBRZIS

DESCRIPTION: Browser Device

<span id="_Ref178063517" class="anchor"></span>Figure 66: Caché and GT.M Browser Device—DEVICE (#3.5) File Entry

NAME: BROWSER \$I: DDBR.TXT

ASK DEVICE: YES ASK PARAMETERS: NO

SIGN-ON/SYSTEM DEVICE: NO QUEUING: NOT ALLOWED

LOCATION OF TERMINAL: HFS/CRT ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO MARGIN WIDTH: 80

FORM FEED: \# PAGE LENGTH: 99999

BACK SPACE: \$C(8) OPEN PARAMETERS: NEW:DELETE

POST-CLOSE EXECUTE: D POST^DDBRZIS

SUBTYPE: P-BROWSER TYPE: HOST FILE SERVER

PRE-OPEN EXECUTE: I '\$\$TEST^DDBRT S %ZISQUIT=1 W \$C(7),!,"Browser not selectable from current terminal.",!

## Form Feeds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Form Feeds User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most users would prefer to see their printouts without any extra blank pages before or after the content. Most prefer to see their reports printed on a fresh page instead of starting in the middle of the previous printout. The printing of labels should also be accomplished without unnecessary form feeds. If a printer is generating extra pages, you should contact the system administrators to remedy the problem.

### Form Feeds System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a particular device does *not* need a form feed between reports, system administrators should set the SUPPRESS FORM FEED AT CLOSE (#11.2) field to YES in the device’s DEVICE (#3.5) file entry. Label printers, for example, should have this flag set. This procedure prevents the Device Handler from issuing a form feed, as shown in <u>Figure 67</u>:

<span id="_Ref33082162" class="anchor"></span>Figure 67: Device Edit Option—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">DEVICE HANDLER \<Enter\></span>

Select Device Handler Option: <span class="mark">DEVICE EDIT \<Enter\></span>

Select DEVICE NAME: <span class="mark">LABEL PRINTER \<Enter\></span>

NAME: LABEL PRINTER// <span class="mark">^SUP \<Enter\></span> PRESS FORM FEED AT CLOSE

SUPPRESS FORM FEED AT CLOSE: <span class="mark">YES \<Enter\></span>

The Device Handler also checks the TERMINAL TYPE (#3.2) file to see if form feeds have been suppressed for that terminal type. It checks for the existence of the IONOFF variable. Thus, for certain terminal types (such as laser printers), system administrators can set this “no form feed” variable in the corresponding terminal type’s CLOSE EXECUTE (#7) field.

![](kernel-8-0-systems-management-device-handler-user-guide/030.png) NOTE: The IONOFF variable can also be set by the calling application to suppress form feeds.

<span id="_Toc193181797" class="anchor"></span>Figure 68: Terminal Type Edit Option—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">DEVICE HANDLER \<Enter\></span>

Select Device Handler Option: <span class="mark">TERMINAL TYPE EDIT \<Enter\></span>

Select TERMINAL TYPE NAME: <span class="mark">P-DEC-LABEL \<Enter\></span>

NAME: P-ZPK80// <span class="mark">^CLOSE EXECUTE \<Enter\></span>

CLOSE EXECUTE: <span class="mark">S IONOFF="" \<Enter\></span>

## Magtape

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Magtape System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181800" class="anchor"></span>Figure 69: Edit Devices by Specific Types Option

Device Management... \[XUTIO\]

<span class="mark">Edit Devices by Specific Types...</span> \[XUDEVEDIT\]

Magtape Device Edit \[XUDEVEDITMT\]

The Edit Devices by Specific Types \[XUDEVEDIT\] option lets you edit specific types of devices using ScreenMan.

Values entered in a Magtape (MT) device for the fields in <u>Table 17</u> may *not* be relevant to a given application:

<table>
<caption><p><span id="_Ref26361678" class="anchor"></span>Table 18: Escape Sequences Used to Toggle the Slaved Printing Modes for DEC VT220/VT320 Terminals</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 26%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DEVICE (#3.5)</td>
<td>SUBTYPE (#3)</td>
<td><p>Use this field to select a default terminal type for the device. This field points to the TERMINAL TYPE (#3.2) file to retrieve a standard set of characteristics that have been defined for vendor devices (such as Laser printers or <strong>VT320</strong> CRTs).</p>
<p>![](kernel-8-0-systems-management-device-handler-user-guide/031.png) <strong>REF:</strong> For a discussion of the TERMINAL TYPE (#3.2) file, see the “<u>TERMINAL TYPE (#3.2) File</u>” section.</p></td>
</tr>
<tr class="even">
<td></td>
<td>MARGIN WIDTH (#9)</td>
<td>Data in this field overrides the RIGHT MARGIN field value from the TERMINAL TYPE (#3.2) file. Leave this field blank unless you are sure that you need to have a different RIGHT MARGIN than what is in the TERMINAL TYPE (#3.2) file.</td>
</tr>
<tr class="odd">
<td>TERMINAL TYPE (#3.2)</td>
<td>FORM FEED (#2)</td>
<td>The argument of an M <strong>WRITE</strong> statement that sets the top-of-form for the use of tractor-feed paper on a printer or clears the screen of a video display terminal.</td>
</tr>
<tr class="even">
<td></td>
<td>PAGE LENGTH (#3)</td>
<td>This field is the number of usable lines on the output device.</td>
</tr>
<tr class="odd">
<td></td>
<td>BACK SPACE (#4)</td>
<td>The argument of an M <strong>WRITE</strong> statement that causes the cursor to back space.</td>
</tr>
</tbody>
</table>

<span id="_Ref26361678" class="anchor"></span>Table 18: Escape Sequences Used to Toggle the Slaved Printing Modes for DEC VT220/VT320 Terminals

The data values entered in these fields may be arbitrary for Magtape devices. However, if the application plans to copy the output to a printer, the characteristics may need to be like that of the printer.

If an application intends to use these fields, be cautious about the type of data that is entered. When sent to the tape unit, some control codes initiate tape movement or cause tape markers to be written to the mounted tape.

Data entered in the \$I and OPEN PARAMETERS fields depends on the following:

- Type of M system you are running.
- Type of tape unit.
- Desired format.

![](kernel-8-0-systems-management-device-handler-user-guide/032.png) REF: For examples of the type of data required in these fields, see the “<u>Device Handler: System Management</u>” section.

![](kernel-8-0-systems-management-device-handler-user-guide/033.png) REF: For further details on Magtape devices, see your specific M implementation manuals.

## Network Channel Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Network Channel Devices System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network channel devices are typically high-speed channel devices (such as TCP/IP). Currently, this network channel device support exists under the Caché and GT.M operating system. In most cases, these devices are used for specialized purposes rather than for general output. For example, network mail could use such devices to move enormous amounts of email through high speed communication channels.

The use of network channel devices requires at least two processes on each end of the communication channel, a server and a client, which can then exchange information:

- Server Process—One process *must* always be available. It can be actively running or triggered to run at a given moment. This process is commonly known as a server. The server waits until another process makes a request to exchange information.
- Client Process—The other process is known as the client.

The two processes can be hosted by two CPUs using network protocols.

#### Network Channel Device Edit

<span id="_Toc193181801" class="anchor"></span>Figure 70: Network Channel Device Edit Option

Device Management... \[XUTIO\]

Edit Devices by Specific Types... \[XUDEVEDIT\]

<span class="mark">Network Channel Device Edit</span> \[XUDEVEDITCHAN\]

The Network Channel Device Edit \[XUDEVEDITCHAN\] option allows you to edit network channel device attributes.

When editing Network Channel devices, the contents of the fields listed in <u>Table 17</u> are *not* necessarily relevant for using network Channel devices. However, these fields are provided in case the application calling the Device Handler is *not* able to distinguish between a printer and a Network Channel device when sending output.

The timeout on the M OPEN command may *not* be applicable with Network Channel devices. Therefore, it may be necessary to answer NO to the USE TIMEOUT ON OPENS (#2009.5) field in the DEVICE (#3.5) file.

![](kernel-8-0-systems-management-device-handler-user-guide/034.png) REF: For more information regarding device timeout applicability, see the appropriate Caché manual.

For Network Channel devices that use TCP/IP, data is required for the OPEN PARAMETERS (#19) field in the DEVICE (#3.5) file. For the client device setup, this field stores the remote Internet address to which the host connects.

<span id="_Toc193181802" class="anchor"></span>Figure 71: Network Channel Device Edit Option—Sample Output

EDIT A NETWORK CHANNEL DEVICE

NAME: SDD-DIRECT PAGE 1 OF 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME: SDD-DIRECT LOCATION OF TERMINAL: HP-8000 near Raul

\$I: \|TCP\|9100 VOLUME SET(CPU):

TYPE: NETWORK CHANNEL SIGN-ON/SYSTEM DEVICE: NO

SUBTYPE: P-HP8000 TCP/S MARGIN WIDTH:

PAGE LENGTH:

ASK DEVICE: NO USE TIMEOUT ON OPENS:

ASK PARAMETERS: NO OPEN TIMEOUT:

OPEN PARAMETERS: ("10.6.21.138":9100:"M")

USE LOCK:

The GLOBAL LOCK (#36) field in the DEVICE (#3.5) file stores a YES/NO Set of Codes. This is important, especially if the application expects that only one client at a given time can open the device. If this field is set to YES an M lock on ^%ZIS(“lock”,IO) is obtained before the device is opened. It remains until a call to ^%ZISC to close the device. It can be used with any type of device.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Resources System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Resource device is a type of device that can only be used by tasks. They *cannot* be used for input or output (I/O). As such, they are *not* available for user selection at the device prompt. The purpose of a resource is to provide a mechanism of limiting the number of concurrent jobs that can run at any one time.

When creating a task, a task can request the resource as an input variable for the ^%ZTLOAD call. The resource itself, as defined in the DEVICE (#3.5) file, has a field called RESOURCE SLOTS (#35) that determines how many jobs can simultaneously own it as a resource.

The Device Handler and TaskMan work together to provide resource device functionality. The RESOURCE (#3.54) file, stored in the translated ^%ZISL global, regulates processing and is for internal use only. The NAME (#.01) field holds the \$I of the resource device. Other fields hold information on jobs currently using the resource, information that is cleared when the resource is closed.

The RESOURCE (#3.54) file supports processing by maintaining a count of the number of available “slots.” The ability to open and close resources is accomplished by decrementing and incrementing this count.

#### Limiting Simultaneous Running of a Particular Task

Resources make it possible for you to control the number of a particular kind of non-I/O task that runs at any one time. If you have a particular job and you want no more than three running versions of it at any one time, you can queue the job (through the ^%ZTLOAD interface) to a resource that had a RESOURCE SLOTS (#35) setting of 3.

#### Running Sequences of Tasks

Resources also make it possible to run non-I/O tasks in sequential order. Non-I/O tasks can run simultaneously because they do *not* compete for the ownership of I/O devices. If you instead queue such tasks to the same resource, and the resource has a RESOURCE SLOTS (#35) setting of 1, TaskMan runs the tasks one at a time and in the order queued. In this way, the results of one process can be used by another. This sequential processing might be appropriate, for example, for the processing of physician orders or other nested tasks involving code execution.

An additional enhancement to resource devices are SYNC FLAGs, which are stored in the SYNC FLAG (#87) field in the TASKS (#14.4) file, allows TaskMan to run the next task waiting for a resource only if the previous task using that resource has completed successfully. You can use SYNC FLAGs to ensure that subsequent jobs run only if previous jobs have completed successfully.

#### Creating Resource Devices

<span id="_Toc193181803" class="anchor"></span>Figure 72: Resource Device Edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Device Management ... \[XUTIO\]

<span class="mark">Resource Device Edit</span> \[XUDEVEDITRES\]

The Resource Device Edit \[XUDEVEDITRES\] option provides a facility for editing resource devices. Software that uses a resource should include in its installation instructions the way the new resource should be defined in the DEVICE (#3.5) file. System administrators can then create one or more resource-type (RES) entries.

<span id="_Toc193181804" class="anchor"></span>Figure 73: Resource Device—Sample Output

NAME: ZZRES \$I: ZZRES

LOCATION OF TERMINAL: NA RESOURCE SLOTS: 1

TYPE: RESOURCE

The installation instructions should indicate the number of resource slots. Sequential processing should use a value of 1. The NAME and \$I should probably use the same value and be namespaced according to VistA conventions.

## Sequential Disk Processors (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Though the Sequential Disk Processors (SDP) entry is still found in the DEVICE (#3.5) file, it is obsolete, and users should now use Host File Server (HFS) devices.

![](kernel-8-0-systems-management-device-handler-user-guide/035.png) REF: For more information on HFS devices, see “<u>Host Files</u>.”

## Slaved Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Slaved Printers User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your terminal has an auxiliary printer port with a printer directly attached, you can send output normally destined for the CRT terminal directly to a printer. Output for the terminal is redirected from the host computer through the terminal’s auxiliary port to the printer. Such printers are commonly called slaved printers or slaved devices.

If slaved printing is available from your terminal, you can send a printed report to your slaved printer, by entering the device name that corresponds to your slaved printer, as shown in <u>Figure 74</u>:

<span id="_Ref33082263" class="anchor"></span>Figure 74: Slaved Printer—Sample User Dialog

DEVICE: <span class="mark">SLAVELA50 \<Enter\></span>

![](kernel-8-0-systems-management-device-handler-user-guide/036.png) NOTE: Consult your local system administrators to find out if slaved printing devices are available.

### Slaved Printers System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two modes of slaved printing:

- Auto Print Mode (aka Copy Print Mode)—When Auto Print Mode is toggled on, output is displayed on the terminal as well as printed on the printer. Special escape sequences and control characters, such as those that are normally used to adjust fonts/pitches, are *not* passed to the printer; however, those used for actions like carriage return, line feed, and form feed are passed on to the printer.
- Printer Controller Mode (aka Transparent Print Mode)—When Printer Controller Mode is toggled on, output is only printed on the printer; nothing is displayed on the terminal. All escape sequences and control characters are passed to the printer. This mode is preferable to Auto Print Mode, especially when compressed mode printing is desired.

<u>Table 18</u> lists the escape sequences used to toggle the slaved printing modes for DEC VT220/VT320 terminals:

| Mode                         | Escape Sequence |
|------------------------------|-----------------|
| Auto print mode on.          | ESC \[?5i   |
| Auto print mode off.         | ESC \[?4i   |
| Printer controller mode on.  | ESC \[5i    |
| Printer controller mode off. | ESC \[4i    |

#### Device and Terminal Type File Entries

To use a slaved printer through the Device Handler, two DEVICE (#3.5) file entries along with corresponding TERMINAL TYPE (#3.2) file entries *must* be made for the following:

- Home Device
- Slaved Printer

One pair of DEVICE/TERMINAL TYPE entries is needed to describe the home (that is CRT) terminal attributes including the codes to open and close the printer port. The OPEN PRINTER PORT (#110 and CLOSE PRINTER PORT (#111) fields of the TERMINAL TYPE (#3.2) file can be used to store the appropriate codes.

Another pair of DEVICE/TERMINAL TYPE entries is needed to describe the attributes of the slaved printer including escape codes to adjust fonts/pitches. The OPEN EXECUTE (#6) and CLOSE EXECUTE (#7) fields of the TERMINAL TYPE (#3.2) file can be used to hold such codes. Additionally, the device entry for the slaved printer *must* have a value of 0 (Zero) entered into the \$I field. This \$I value identifies the DEVICE (#3.5) file entry as one for a slaved device.

The examples in <u>Figure 75</u> through <u>Figure 80</u> show the setup for a home device, and the setup for slaved printers.

<span id="_Ref29294228" class="anchor"></span>Figure 75: Home Device Example (VT320)—DEVICE (#3.5) File Entry

NAME: TELNET DEVICE \$I: \_TNA

ASK DEVICE: YES ASK PARAMETERS: NO

VOLUME SET(CPU): KDE SIGN-ON/SYSTEM DEVICE: YES

LOCATION OF TERMINAL: Network MARGIN WIDTH: 80

FORM FEED: \#,\$C(27,91,50,74,27,91,72) PAGE LENGTH: 24

BACK SPACE: \$C(8) SUBTYPE: C-VT320

TYPE: VIRTUAL TERMINAL

TIMED READ (# OF SECONDS): 400

<span id="_Toc193181808" class="anchor"></span>Figure 76: Home Device Example (VT320)—TERMINAL TYPE (#3.2) File Entry

NAME: C-VT320 SELECTABLE AT SIGN-ON: YES

FORM FEED: \#,\$C(27,91,50,74,27,91,72) RIGHT MARGIN: 80

PAGE LENGTH: 24 BACK SPACE: \$C(8)

DESCRIPTION: Digital Equipment Corporation VT-320 video

OPEN PRINTER PORT: W \*27," \[5i"

CLOSE PRINTER PORT: W \*27," \[4i"

<span id="_Toc193181809" class="anchor"></span>Figure 77: Slaved Printer Example: DEC LA50—DEVICE (#3.5) File Entry

NAME: SLAVELA50 \$I: 0

ASK DEVICE: YES ASK PARAMETERS: YES

SLAVED FROM DEVICE: TRM

LOCATION OF TERMINAL: SLAVE DEVICE FOR LA50

MARGIN WIDTH: 132 FORM FEED: \#

PAGE LENGTH: 64 SUBTYPE: P-LA50

TYPE: TERMINAL

<span id="_Toc193181810" class="anchor"></span>Figure 78: Slaved Printer Example: DEC LA50—TERMINAL TYPE (#3.2) File Entry

NAME: P-LA50 RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 64

OPEN EXECUTE: W \*27,"\[4w" CLOSE EXECUTE: W \*27,"\[0w"

DESCRIPTION: LA50 132 COL/16.5 CPI

<span id="_Toc193181811" class="anchor"></span>Figure 79: Slaved Printer Example: Epson LQ870—DEVICE (#3.5) File Entry

NAME: SLAVELQ870 \$I: 0

ASK DEVICE: YES ASK PARAMETERS: YES

SLAVED FROM DEVICE: TRM

LOCATION OF TERMINAL: SLAVE DEVICE FOR LQ870

MARGIN WIDTH: 132 FORM FEED: \#

PAGE LENGTH: 64 SUBTYPE: P-LQ870

TYPE: TERMINAL

<span id="_Ref29294240" class="anchor"></span>Figure 80: Slaved Printer Example: Epson LQ870—TERMINAL TYPE (#3.2) File Entry

NAME: P-LQ870 RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 64

OPEN EXECUTE: W \*15 CLOSE EXECUTE: W \*18

DESCRIPTION: EPSON LQ870 PRINTER--CONDENSED

#### Use of Slaved Printer: Processing Steps

The Device Handler manages output to slaved printers using the following steps:

1.  Execute the OPEN PRINTER PORT (#110) code of the home device’s terminal type.
2.  Execute the OPEN EXECUTE (#6) code of the slaved printer’s terminal type.
3.  When the application closes the device, execute the CLOSE EXECUTE (#7) code of the slaved printer’s terminal type.
4.  Execute the CLOSE PRINTER PORT (#111) code of the home device’s terminal type.

#### Queuing to Slaved Printers

If queuing to a slaved device is desired, then the SLAVE FROM DEVICE field of the DEVICE (#3.5) file *must* be used. This field is a pointer to the DEVICE (#3.5) file. Data *must* be entered in this field for the entry for the slaved printer. This data should point to the home device entry unless the slaved printer is attached to a terminal on a Terminal Server (that is a virtual terminal).

If queuing to a slaved device is being performed from a virtual terminal, then a third device entry *must* be established that fully describes the home device with a type of TRM. This device should be entered into the SLAVE FROM DEVICE field.

![](kernel-8-0-systems-management-device-handler-user-guide/037.png) NOTE: When queuing to a slaved device from a terminal on a Terminal Server, the user *must* be fully logged off the computer system and logged off the port by the time the queued task is scheduled to run.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-device-handler-user-guide/038.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-device-handler-user-guide/039.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-device-handler-user-guide/040.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.