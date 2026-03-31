---
title: "Kernel 8.0 Developerâ€™s Guide: Device Handler User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Device Handler"
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
  - variables
  - handler
  - guide
  - table
  - devices
  - contents
  - span
  - output
  - variable
page_count: 0
word_count: 9971
section_count: 26
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259265" class="anchor"></span>Device Handler Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-device-handler-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-device-handler-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
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
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Device Handler Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207253254" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-device-handler-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [DEVICE^XUDHGUI(): GUI Device Lookup](#devicexudhgui-gui-device-lookup)
    - [Examples](#examples)
  - [\$\$RES^XUDHSET(): Set Up Resource Device](#resxudhset-set-up-resource-device)
  - [^%ZIS: Standard Device Call](#zis-standard-device-call)
    - [Examples](#examples-1)
    - [Multiple Devices and ^%ZIS](#multiple-devices-and-zis)
    - [Host Files and ^%ZIS](#host-files-and-zis)
  - [HLP1^%ZIS: Display Brief Device Help](#hlp1zis-display-brief-device-help)
  - [HLP2^%ZIS: Display Device Help Frames](#hlp2zis-display-device-help-frames)
  - [HOME^%ZIS: Reset Home Device IO Variables](#homezis-reset-home-device-io-variables)
  - [\$\$REWIND^%ZIS(): Rewind Devices](#rewindzis-rewind-devices)
    - [Example](#example)
  - [^%ZISC: Close Device](#zisc-close-device)
    - [Example](#example-1)
  - [PKILL^%ZISP: Kill Special Printer Variables](#pkillzisp-kill-special-printer-variables)
  - [PSET^%ZISP: Set Up Special Printer Variables](#psetzisp-set-up-special-printer-variables)
    - [Example](#example-2)
  - [ENDR^%ZISS: Set Up Specific Screen Handling Variables](#endrziss-set-up-specific-screen-handling-variables)
  - [ENS^%ZISS: Set Up Screen-handling Variables](#ensziss-set-up-screen-handling-variables)
  - [GKILL^%ZISS: KILL Graphic Variables](#gkillziss-kill-graphic-variables)
  - [GSET^%ZISS: Set Up Graphic Variables](#gsetziss-set-up-graphic-variables)
    - [Example](#example-3)
  - [KILL^%ZISS: KILL Screen Handling Variables](#killziss-kill-screen-handling-variables)
  - [CALL^%ZISTCP: Make TCP/IP Connection (Remote System)](#callzistcp-make-tcpip-connection-remote-system)
  - [CLOSE^%ZISTCP: Close TCP/IP Connection (Remote System)](#closezistcp-close-tcpip-connection-remote-system)
  - [CLOSE^%ZISUTL(): Close Device with Handle](#closezisutl-close-device-with-handle)
  - [OPEN^%ZISUTL(): Open Device with Handle](#openzisutl-open-device-with-handle)
    - [Example](#example-4)
  - [RMDEV^%ZISUTL(): Delete Data Given a Handle](#rmdevzisutl-delete-data-given-a-handle)
  - [SAVDEV^%ZISUTL(): Save Data Given a Handle](#savdevzisutl-save-data-given-a-handle)
  - [USE^%ZISUTL(): Use Device Given a Handle](#usezisutl-use-device-given-a-handle)
- [Special Device Issues](#special-device-issues)
  - [Form Feeds](#form-feeds)
    - [How to Check if Current Device is a CRT](#how-to-check-if-current-device-is-a-crt)
    - [Guidelines for Form Issuing Form Feeds](#guidelines-for-form-issuing-form-feeds)
  - [Resources](#resources)
    - [Queuing to a Resource](#queuing-to-a-resource)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Device Handler Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device Handler provides a common user interface and developer API for using output devices. This section describes the Device Handler’s developer API.

The ZIS\* series of routines becomes the Device Handler when the Kernel installation process (the ZTMGRSET routine) saves them in the Manager’s account as %ZIS\* routines. A separate set of ZIS\* routines is distributed for each operating system.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/004.png) NOTE: As of Kernel Patch XU\*8.0\*546 (and Informational Patch XU\*8.0\*556), Class 3 routines that are *not* written to permit queuing no longer output to devices where the QUEUING (#5.5) field in the DEVICE (#3.5) file is set to FORCED. Sites that have completed the Linux upgrade checklist should have already addressed this issue.  
  
REF: For more specific details, see Kernel Patches XU\*8.0\*546 and 556.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Device Handler APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## DEVICE^XUDHGUI(): GUI Device Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 3771

Description: The DEVICE^XUDHGUI API allows VistA Graphical User Interface (GUI)-based applications to look up devices. This API retrieves the first 20 devices that meet the specifications passed.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*220.

Format: DEVICE^XUDHGUI(.list,starting_point\[,direction\]  
\[,right_margin_range\])

Input Parameters: .list: (required) Named array to store output.

starting_point: (required) This parameter indicates where to start the \$ORDERing of the Global:

- P—Returns devices whose name starts with P.
- P\*—Returns up to 20 devices the first starting with P.

direction: (optional) This parameter indicates whether to \$ORDER up or down from the starting_point parameter. The acceptable values are:

- 1—Up.
- -1—Down.

right_margin_range: (optional) This parameter specifies a width range of devices:

- Exact Width (such as “132-132”)
- At Least Width (such as “132”)
- Range (such as “80-132”)

Output Parameters: .list: The data is returned in this named array. Data is returned in the following format:

IEN^NAME^DISPLAY NAME^LOCATION^RIGHT MARGIN^PAGE LENGTH

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

This example stores/displays a list of all devices that begin with P in an array (such as DEVICES), without passing a direction or right_margin_range parameter:

<span id="_Toc199950547" class="anchor"></span>Figure 1: DEVICE^XUDHGUI API—Example 1: Store Devices

\><span class="mark">K DEVICES</span>

\><span class="mark">D DEVICE^XUDHGUI(.DEVICES,"P")</span>

The DEVICES array displays the following results:

<span id="_Toc199950548" class="anchor"></span>Figure 2: DEVICE^XUDHGUI API—Example 1: Display Sample Results

\><span class="mark">ZW DEVICES</span>

DEVICES(1)=358^P-MESSAGE-HFS^P-MESSAGE-HFS^HFS FILE=\>MESSAGE^255^256

DEVICES(2)=348^P-MESSAGE-HFS-ONT^P-MESSAGE-HFS-ONT^HFS FILE==\> MESSAGE^80^999

DEVICES(3)=274^P-MESSAGE-HFS-VXD^P-MESSAGE-HFS-VXD^HFS FILE==\> MESSAGE^80^256

DEVICES(4)=292^P-RESMON^P-RESMON^IRM^132^64

DEVICES(5)=310^P-WINDOC^P-WINDOC^MWI WINDOW DOCUMENT BOX^80^256

#### Example 2

This example stores/displays a list of all devices that begin with P in an array (such as DEVICES), without passing a direction parameter but including those devices with a right margin of an exact width of 80:

<span id="_Toc199950549" class="anchor"></span>Figure 3: DEVICE^XUDHGUI API—Example 2: Store Devices

\><span class="mark">K DEVICES</span>

\><span class="mark">D DEVICE^XUDHGUI(.DEVICES,"P",,"80-80")</span>

The DEVICES array displays the following results:

<span id="_Toc199950550" class="anchor"></span>Figure 4: DEVICE^XUDHGUI API—Example 2: Display Sample Results

\><span class="mark">ZW DEVICES</span>

DEVICES(1)=348^P-MESSAGE-HFS-ONT^P-MESSAGE-HFS-ONT^HFS FILE==\> MESSAGE^80^999

DEVICES(2)=274^P-MESSAGE-HFS-VXD^P-MESSAGE-HFS-VXD^HFS FILE==\> MESSAGE^80^256

DEVICES(3)=310^P-WINDOC^P-WINDOC^MWI WINDOW DOCUMENT BOX^80^256

#### Example 3

This example stores/displays a list of all devices that begin with P in an array (such as DEVICES), without passing a direction parameter but including those devices with a right margin width range of 80-132:

<span id="_Toc199950551" class="anchor"></span>Figure 5: DEVICE^XUDHGUI API—Example 3: Store Devices

\><span class="mark">K DEVICES</span>

\><span class="mark">D DEVICE^XUDHGUI(.DEVICES,"P",,"80-132")</span>

The DEVICES array displays the following results:

<span id="_Toc199950552" class="anchor"></span>Figure 6: DEVICE^XUDHGUI API—Example 3: Display Sample Results

\><span class="mark">ZW DEVICES</span>

DEVICES(1)=348^P-MESSAGE-HFS-ONT^P-MESSAGE-HFS-ONT^HFS FILE==\> MESSAGE^80^999

DEVICES(2)=274^P-MESSAGE-HFS-VXD^P-MESSAGE-HFS-VXD^HFS FILE==\> MESSAGE^80^256

DEVICES(3)=292^P-RESMON^P-RESMON^IRM^132^64

DEVICES(4)=310^P-WINDOC^P-WINDOC^MWI WINDOW DOCUMENT BOX^80^256

#### Example 4

This example stores/displays a list of up to 20 devices, the first of which starts with P, in an array (such as DEVICES), without passing a direction or right_margin_range parameter:

<span id="_Toc199950553" class="anchor"></span>Figure 7: DEVICE^XUDHGUI API—Example 4: Store Devices

\><span class="mark">K DEVICES</span>

\><span class="mark">D DEVICE^XUDHGUI(.DEVICES,"P\*")</span>

The DEVICES array displays the following results:

<span id="_Toc199950554" class="anchor"></span>Figure 8: DEVICE^XUDHGUI API—Example 4: Display Sample Results

\><span class="mark">ZW DEVICES</span>

DEVICES(1)=358^P-MESSAGE-HFS^P-MESSAGE-HFS^HFS FILE=\>MESSAGE^255^256

DEVICES(2)=348^P-MESSAGE-HFS-ONT^P-MESSAGE-HFS-ONT^HFS FILE==\> MESSAGE^80^999

DEVICES(3)=274^P-MESSAGE-HFS-VXD^P-MESSAGE-HFS-VXD^HFS FILE==\> MESSAGE^80^256

DEVICES(4)=292^P-RESMON^P-RESMON^IRM^132^64

DEVICES(5)=310^P-WINDOC^P-WINDOC^MWI WINDOW DOCUMENT BOX^80^256

DEVICES(6)=202^C6_SDD_MX3 ROUTINE^ROUTINE \<C6_SDD_MX3 ROUTINE\>^Next to Jean's Office^80^59

DEVICES(7)=428^SDD DUPLEX P10^SDD DUPLEX P10^SSD DUPLEX PRINTER NEXT TO JACK^80^60

DEVICES(8)=429^SDD P10^SDD P10^Printer next to Jack.^80^60

DEVICES(9)=329^C6_SDD_MX3 P10^SS10 \<C6_SDD_MX3 P10\>^Near Jean's Office^80^59

DEVICES(10)=330^C6_SDD_MX3 P12^SS12 \<C6_SDD_MX3 P12\>^Near Jean's Office^96^57

DEVICES(11)=331^C6_SDD_MX3 P16^SS16 \<C6_SDD_MX3 P16\>^Near Jean's Office^255^58

DEVICES(12)=349^C6_SDD_MX3 P16P8L^SS16P8L \<C6_SDD_MX3 P16P8L\>^Near Jean's Office^117^79

DEVICES(13)=202^C6_SDD_MX3 ROUTINE^SSR \<C6_SDD_MX3 ROUTINE\>^Next to Jean's Office^80^59

DEVICES(14)=427^SUP\$PRT TEST^SUP\$PRT TEST^DISK FILE^132^58

DEVICES(15)=283^SYS\$INPUT^SYS\$INPUT^SYS\$INPUT;^132^64

DEVICES(16)=198^VMS FILE^VMS FILE^DISK^80^64

DEVICES(17)=349^C6_SDD_MX3 P16P8L^VPM \<C6_SDD_MX3 P16P8L\>^Near Jean's Office^117^79

DEVICES(18)=291^VTB255^VTB255^RMS FILE^255^99999

DEVICES(19)=288^ZBROWSE^ZBROWSE^RMS FILE^255^99999

## \$\$RES^XUDHSET(): Set Up Resource Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2232

Description: The \$\$RES^XUDHSET extrinsic function sets up a Resource device. It returns:

- Error:-1^text
- Successful:IEN^device nameFormat: \$\$RES^XUDHSET(device_name\[,resource_name\],slot_count,description,subtype)

Input Parameters: device_name: (required) The name of the resource device.

resource_name: (optional) The resource name if *not* the same as the device name.

slot_count: (required) The number of concurrent jobs that can use this device. It defaults to 1.

description: (required) The device description. It defaults to “Resource Device”.

subtype: (required) The subtype to use. It defaults to P-OTHER.

Output: returns: Returns:

- Error:-1^text
- Successful:IEN^device name

## ^%ZIS: Standard Device Call

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10086

Description: The ^%ZIS API allows you to select a device.

All input variables are optional. *Non*-namespaced variables that are defined and later KILLed by ^%ZIS include: %A, %E, %H, %X, and %Y.

If device selection is successful, characteristics of the output device are returned in several different variables. If selection is unsuccessful, ^%ZIS returns the POP output variable with a positive number. So, it checks for an unsuccessful device selection should be based on the POP input variable as a positive number.

Device selection can be done as shown in the example that follows.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/006.png) REF: For a discussion of form feeds, see the “<u>Form Feeds</u>” section in the “[Special Device Issues](#special-device-issues)” section.

Format: ^%ZIS

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variable: %ZIS: (optional) The %ZIS input variable is defined as a string containing one or more single-character flags that act as input specifications. The functions of each of the flags that can be included in the string are described below. If the %ZIS input variable contains:

- M—RIGHT MARGIN: The user is prompted with the right margin query.
- N—NO OPENING: The Device Handler returns the characteristics of the selected device *without* issuing the OPEN command to open the device.
- P (obsolete)—CLOSEST PRINTER: The closest printer, if one has been defined in the DEVICE (#3.5) file, is presented at the default response to the device prompt.
- Q—QUEUING ALLOWED: The job can be queued to run later. There is no automatic link between the Device Handler and TaskMan. If queuing is allowed, just before the Device Handler is called, the application routine *must* set the %ZIS input variable to a string that includes the letter Q. For example:

\>S %ZIS="MQ" D ^%ZIS

If the user selects queuing, the Device Handler defines the IO(“Q”) variable as an output variable, to indicate that queuing was selected. If queuing is selected, the application should set the needed TaskMan variables and call the TaskMan interface routine [^%ZTLOAD](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf#ztload).

![](kernel-8-0-developer-s-guide-device-handler-user-guide/007.png) REF: For further details on how to call the TaskMan interface, see the [*Kernel 8.0 Developer’s Guide: TaskMan Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf).

- 0—DON’T USE IO(0): The Device Handler does *not* attempt to use IO(0), the home device at the time of the call to ^%ZIS.
- D—DIRECT PRINTING: If the selected device is unavailable, it returns a positive number in POP.
- L—RESET IO(“ZIO”): If %ZIS contains L, the IO(“ZIO”) output variable is reset with the static physical port name (such as the port name from a Terminal Server). It is useful when the \$I of the M implementation does *not* represent a physical port name.

%ZIS(“A”): (optional) Use to replace the default device prompt.

%ZIS(“B”): (optional) If %ZIS is defined, HOME is presented as the default response to the device prompt. Use %ZIS(“B”) to replace this default with another response.

\>S %ZIS("B")=""

(If you do *not* want to display any default response.)

%ZIS(“HFSMODE”): (optional) Use to pass the Host file access mode to %ZIS. The possible values are:

- RW (which may *not* work in all environments)—READ/WRITE access.
- R—READ Only access.
- W—WRITE access.
- A—Append mode.

> For example:

\>S %ZIS("HFSMODE")="R"%ZIS(“HFSNAME”): (optional) Use to pass the name of a Host file to %ZIS. For example:

\>S %ZIS("HFSNAME")="MYFILE.DAT"%ZIS(“IOPAR”): (optional) Use this input variable to pass OPEN command variables to the Device Handler. If defined, the value of this input variable is used instead of any value specified in the OPEN PARAMETERS field of the DEVICE (#3.5) file. The Device Handler uses the data from either this input variable or from the OPEN PARAMETERS field whether the device type is TRM.

On some M systems, Right Margin is an OPEN PARAMETERS. Therefore, any value for Right Margin in the DEVICE (#3.5) file, TERMINAL TYPE (#3.2) file, or user response can be ignored when this input variable is used.

To set OPEN PARAMETERS for the tape drive device, a device with \$I=47 and device name of MAGTAPE, the following code could be used:

\>S %ZIS("IOPAR")="(""VAL4"":0:2048)"

\>S IOP="MAGTAPE" D ^%ZIS

![](kernel-8-0-developer-s-guide-device-handler-user-guide/008.png) NOTE: The specific variables you pass may *not* be functional for all operating systems. Use of this feature should be limited to local development efforts.

%ZIS(“IOUPAR”): (optional) Use this input variable in the same way as %ZIS(“IOPAR”), but for variables to the USE (rather than OPEN) command. Any USE PARAMETERS specified in the DEVICE (#3.5) file is overridden. For example:

\>S %ZIS("IOUPAR")="NOECHO"

\>S IOP="C72" D ^%ZIS%ZIS(“S”): (optional) Use this input variable to specify a device selection screen. The string of M code this input variable is set to should contain an IF statement to set the value of \$T. Those entries that the IF sets as \$T=0 are *not* displayed or selectable. Like comparable VA FileMan screens, %ZIS(“S”) should be set to sort on nodes and pieces, without using input variables like ION or IOT. As with VA FileMan, the variable Y can be used in the screen to refer to the Internal Entry Number (IEN) of the device. Also, the M naked indicator is at the global level ^%ZIS(1,Y,0).

> An example to limit device selection to spool device types (SPL) only might be coded as follows:

\>S %ZIS("S")="I \$G(^(""TYPE""))=""SPL"""IOP: (optional) Use IOP to specify the output device. There is no user interaction when IOP is defined to specify an output device; the device NAME (#.01) field is the usual value of IOP. You can also set IOP to Q and P. (The value of IOP *must not* be \$I.).\\

![](kernel-8-0-developer-s-guide-device-handler-user-guide/009.png) NOTE: If IOP is set to NULL, the device handler defaults to the HOME device.

You can request queuing by setting IOP=“Q”. The user is then asked to specify a device for queuing. To pre-select the device, set IOP=“Q;device”; the device specified after the semicolon is selected and IO(“Q”) is set.

You can request the closest printer, as specified in the DEVICE (#3.5) file, by setting IOP=“P” or IOP=“p”. If there is *not* a closest printer associated with the home device at the time of the call, device selection fails, and POP is returned with a positive value.

> You can also pass the Internal Entry Number (IEN) of the desired device through IOP. For instance, to select a device with an IEN of 202, you can set IOP to an accent grave character (\`) followed by the IEN value of 202 before the call to ^%ZIS. The following example illustrates the above call:

\>S IOP="\`202" D ^%ZIS

Using the IEN rather than device name can be useful when applications have the desired device stored as a POINTER to the DEVICE (#3.5) file rather than as FREE TEXT.

Output Variables: IO: If a device is successfully opened, IO is returned with the device \$I value of the selected device. If an abnormal exit occurs, POP is returned with a positive numeric value, and IO is returned as NULL.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/010.png) CAUTION: Because the returned value of IO can be changed, since December 1990, developers have been advised to check for a positive value in POP rather for IO equal to NULL when determining if an abnormal exit occurred.

IO(0):HOME DEVICE—Contains the \$I value of the home device at the time of the call to the Device Handler. Since it is defined at the time of the call, there is obviously no restoration after the call.

IO(1,\$I):OPENED DEVICES—This array contains a list of devices opened for the current job by the Device Handler. The first subscript of this array is 1. The second subscript is the \$I value of the device opened. The data value is NULL. The Device Handler sets, KILLs, and checks the existence of IO(1,IO).

![](kernel-8-0-developer-s-guide-device-handler-user-guide/011.png) NOTE: This array should *not* be altered by applications outside of Kernel.

IO(“CLNM”): This variable holds the name of the remote system. It is defined by the RPC Broker.

IO(“CLOSE”): Device closed.

IO(“DOC”):SPOOL DOCUMENT NAME—If output has been sent to the spool device, this output variable holds the name of the spool document that was selected.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/012.png) NOTE: This variable is KILLed when a call is made to ^%ZIS or <u>HOME^%ZIS: Reset Home Device IO Variables</u> APIs.

IO(“HFSIO”):HOST FILE DEVICE IO—This is defined by the Device Handler when a user queues to a file at the host operating system level (of a layered system) and selects a file name other than the default. This Host file system device input variable should have the same value as that stored in the IO output variable. If IO(“HFSIO”) exists when the TaskMan interface is called, the interface saves IO(“HFSIO”) and IOPAR so that the scheduled task opens the appropriate Host file.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/013.png) NOTE: This variable is KILLed when a call is made to ^%ZIS or <u>HOME^%ZIS: Reset Home Device IO Variables</u> APIs.

IO(“IP”): This variable holds the Internet Protocol (IP) of the remote system.

IO(“P”): This variable holds data about the new syntax requested.

IO(“Q”): OUTPUT WAS QUEUED—If queuing is allowed (%ZIS\[“Q”) and an output device for queuing is selected, this output variable is returned with a value of 1: IO(“Q”)=1. Otherwise, it is undefined.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/014.png) NOTE: This variable is KILLed when a call is made to ^%ZIS or <u>HOME^%ZIS: Reset Home Device IO Variables</u> APIs.

IO(“S”):SLAVED DEVICE—When a slaved printer is selected, the Device Handler uses this output variable to save the subtype specification for the home device so that the appropriate close printer logic can be executed with X ^%ZIS(“C”).

IO(“SPOOL”):SPOOLER WAS USED—The existence of this output variable indicates that output was sent to the spool device. It exists temporarily, during spooling, and is KILLed upon normal exit.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/015.png) NOTE: This variable is KILLed when a call is made to ^%ZIS or <u>HOME^%ZIS: Reset Home Device IO Variables</u> APIs.

IO(“T”): TaskMan call.

IO(“ZIO”):TERMINAL SERVER PORT—If %ZIS\[“L”, both physical port and server names are returned in IO(“ZIO”) under Caché. This information is useful on M implementations where the value of \$I does *not* represent a port on a Terminal Server.

IOBS:BACKSPACE—The code for backspace, usually \$C(8), is returned in this output variable. This code WRITEs a backspace with W @IOBS.

IOCPU:CPU INDICATOR—If the selected device is on another CPU, this output variable is returned with the other CPU reference, obtained from the VOLUME SET (CPU) field in the DEVICE (#3.5) file. TaskMan uses the IOCPU input variable as an indicator of where the job should ultimately be run.

IOF:FORM FEED—This output variable issues a form feed when writing its value with indirection; that is, W @IOF.

IOM:RIGHT MARGIN—The right margin is commonly set to either 80 or 132 columns.

ION:DEVICE NAME—This variable returns the device NAME (#.01) field as recorded in the DEVICE (#3.5) file.

IOPAR:OPEN PARAMETERS—This variable returns any OPEN PARAMETERS that may have been defined for the selected device, for example, a magnetic tape drive. If the OPEN PARAMETERS input variable has *not* been defined, IOPAR is returned as NULL.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/016.png) NOTE: When a device is closed, this variable gets set to NULL.

IOUPAR:USE PARAMETERS—This variable returns any USE PARAMETERS that may have been defined for the selected device. If the USE PARAMETERS input variable has *not* been defined, IOUPAR is returned as NULL.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/017.png) NOTE: When a device is closed, this variable gets set to NULL.

IOS:DEVICE NUMBER—The DEVICE (#3.5) file Internal Entry Number (IEN) for the selected device.

IOSL:SCREEN/PAGE LENGTH—The number of lines per screen or page is defined with this variable. The page length of a printing device is usually 66 lines. The screen length of a display terminal is usually 24 lines.

IOST:SUBTYPE NAME—This variable returns the NAME (#.01) field of the selected device’s subtype as recorded in the TERMINAL TYPE (#3.2) file.

IOST(0):SUBTYPE NUMBER—This variable returns the Internal Entry Number (IEN) of the selected device’s subtype as recorded in the TERMINAL TYPE (#3.2) file.

IOT:TYPE OF DEVICE—The DEVICE (#3.5) file holds an indication of Type for all devices. IOT returns the value of the device type (such as TRM for terminal, VTRM for virtual terminal, and HFS for Host File Server).

IOXY:CURSOR POSITIONING—This output variable returns the executable M code that allows cursor positioning, given the input variables DX and DY. The column position is passed in DX, and the row position is passed in DY.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/018.png) NOTE: The system special variables \$X and \$Y are *not* necessarily updated.

POP:EXIT STATUS—When the Device Handler is called, POP is the output variable that indicates the outcome status. If device selection is successful, POP is returned with a value of Zero (POP=0). Abnormal exit returns a positive number in the POP variable.

There are three general conditions for abnormal exit upon which the POP output variable is returned as positive:

- The first case is one in which a device is *not* selected.
- The second concerns unavailable devices.
- The third situation arises when a device is identified but is unknown to the system.

The first condition of no device selection is met if the user types a caret (^) or times out at the device prompt. Exceeding the TIMED READ at the right margin or address/variables prompts has the same result.

The second condition, unavailability, is met if the Device Handler *cannot* open the selected device. The selected device may also have existed on another computer, but queuing was *not* requested or perhaps *not* permitted (%ZIS had *not* contained Q).

Finally, the selected device may *not* exist in the DEVICE (#3.5) file. A device name may have been used that is *not* found as a .01 field entry. If the device is selected with P for the closest printer, the CLOSEST PRINTER field in the DEVICE (#3.5) file may be NULL.

If the exit is abnormal, returning POP with a positive value, the following output variables are restored with their values before the call to the Device Handler (before D ^%ZIS): ION, IOF, IOSL, IOBS, IOST(0), IOST, IOPAR, IOUPAR, IOS, and IOCPU.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/019.png) NOTE: If IOF had been NULL before the call, it is returned with the pound sign as its value (IOF=“#”). For backward compatibility, IO is currently returned as NULL (IO=“”). However, the returned value of IO may change in future Kernel versions.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 9</u> is a simplified example; the process of issuing form feeds is *not* shown.

<span id="_Ref499819448" class="anchor"></span>Figure 9: ^%ZIS API—Example

SAMPLE ;SAMPLE ROUTINE

;

S %ZIS="QM" D ^%ZIS G EXIT:POP

I \$D(IO("Q")) D Q

.S ZTRTN="DQ^SAMPLE",ZTDESC="Sample Test routine"

.D ^%ZTLOAD D HOME^%ZIS K IO("Q") Q

DQ U IO W !,"THIS IS YOUR REPORT"

W !,"LINE 2"

W !,"LINE 3"

D ^%ZISC

EXIT S:\$D(ZTQUEUED) ZTREQ="@" K VAR1,VAR2,VAR3 Q

#### Example 2

The IOP variable can be defined to pass a string to the Device Handler so that no user interaction is required for device selection information. The following is the general format for defining IOP:

\>S IOP=\[Q\[;\]\]\[DEVICE NAME\]\[;SUBTYPE\]\[;SPOOL DOCUMENT NAME\]\[;RIGHT MARGIN\[;PAGE LENGTH\]\]

#### Example 3

If the SPOOL DOCUMENT NAME is included, then the RIGHT MARGIN and PAGE LENGTH are ignored. Therefore, use the following format if a spool device is desired:

\>S IOP=\[Q\[;\]\]\[DEVICE NAME\]\[;SUBTYPE\]\[;SPOOL DOCUMENT NAME\]

#### Example 4

The following shows how a device named “RXPRINTER” in the DEVICE (#3.5) file can be opened *without user interaction*:

\>S IOP="RXPRINTER" D ^%ZIS Q:POP

#### Example 5

When setting the IOP variable, you can include the right margin:

\>S IOP=ION\_";"\_IOM or S IOP=";120"

Or:

\>S IOP="RXPRINTER;120"

In this example, ION is the local variable that contains the name of the device to be opened, and the IOM variable contains the value of the desired right margin.

#### Example 6

The IOP variable can be set to FORCED queuing by starting the string with Q:

\>SET IOP="Q;"\_ION\_";"\_IOM ... and so on

To force queuing and prompt the user for a device:

\>SET IOP="Q" D ^%ZIS Q:POP

#### Example 7

A *spool document name* can be passed to the Device Handler:

\>S IOP=DEVNAM\_";"\_IO("DOC") D ^%ZIS Q:POP

Or:

\>S IOP="SPOOL;"\_IO("DOC")

Or:

\>S IOP=DEVNAM\_";"\_IOST\_";"\_IO("DOC")

Or:

\>S IOP="SPOOL;P-OTHER;MYDOC"

![](kernel-8-0-developer-s-guide-device-handler-user-guide/020.png) REF: For more information, see the “Spooling” section in the *Kernel 8.0 Systems Management: Device Handler User Guide*.

In this example:

- DEVNAM contains the name of the device to be opened.
- IO(“DOC”) contains the spool document name.
- IOST contains the name of the desired subtype.
- “SPOOL” is the actual name of a device entry that corresponds to the spool device.
- “P-OTHER” is the desired subtype.
- “MYDOC” is the name of the spool document.

#### Example 8

Finally, the IOP variable can be used to select a device by the device’s Internal Entry Number (IEN). To select a device with an IEN of 202, set IOP to a grave accent character (\`) followed by the IEN value of 202:

\>S IOP="\`202" D ^%ZIS

### Multiple Devices and ^%ZIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beyond the home device, the ^%ZIS API is *not* designed to open more than one additional device at a time.

For interactive users, the home device should already be open and defined in the Kernel environment. ^%ZIS should only be used to open one additional device at a time for interactive users. For a task, you can use ^%ZIS to open one additional device beyond the task’s assigned device.

Beginning with Kernel 8.0, there are three APIs to support using more than one additional device simultaneously:

- <u>OPEN^%ZISUTL(): Open Device with Handle</u>
- <u>USE^%ZISUTL(): Use Device Given a Handle</u>
- <u>CLOSE^%ZISUTL(): Close Device with Handle</u>

These “multiple device” APIs are described later in this section.

### Host Files and ^%ZIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it is possible to use the ^%ZIS API to manipulate Host files, the Host file API (in ^%ZISH) offers more robust Host file functionality.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/021.png) REF: For more information on using the Host file API, see the “[Kernel 8.0 Developer’s Guide: Host Files Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_host_files_ug.pdf)” section.

## HLP1^%ZIS: Display Brief Device Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10086

Description: The HLP1^%ZIS API displays brief help about device selection. There are no input parameters.

While invoking the Help Processor involves a straightforward call in the production account (the [EN^XQH](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf#en_xqh) or [EN1^XQH](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf#en1_xqh) calls), it is a more complex matter in the Manager account where ^%ZIS resides. Hence, this call is provided.

Format: hlp1^%zis

Input Parameters: none.

Output: none.

## HLP2^%ZIS: Display Device Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10086

Description: The HLP2^%ZIS API allows you to display extended help about device selection. The Help Processor is invoked to display a series of help frames. There are no input parameters.

While invoking the Help Processor involves a straightforward call in the production account (the [ACTION^XQH4](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf#action_xqh4) or [EN1^XQH](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf#en1_xqh) APIs), it is a more complex matter in the Manager account where ^%ZIS resides. Hence, this call is provided.

Format: HLP2^%ZIS

Input Parameters: none.

Output: none.

## HOME^%ZIS: Reset Home Device IO Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10086

Description: The HOME^%ZIS API sets the key IO variables to match the characteristics of the home device. The HOME^%ZIS API performs the same function as the *obsolete*CURRENT^%ZIS API.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/022.png) NOTE: Developers have been advised that Kernel 8.0 is the last version of Kernel to support the *obsolete*CURRENT^%ZIS.

HOME^%ZIS, beyond updating the set of variables for the home device, also updates the active right margin system setting for the home device by executing ^%ZOSF(“RM”) based on the home device’s IOM value.

Format: HOME^%ZIS

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Variables: none.

Output Variables: IO: Device \$I.

IO(0): Home device at the time of the call to [^%ZIS](#zis).

IOBS: Backspace code.

IOF: Form Feed code.

IOM: Right Margin length.

ION: Name of last selected input/output device from the DEVICE (#3.5) file.

IOS: Internal Entry Number (IEN) of last selected input/output device from the DEVICE (#3.5) file.

IOSL: Screen or page length.

IOST: Subtype of the selected device.

IOST(0): Subtype Internal Entry Number (IEN).

IOT: Type of device, such as TRM for terminal.

IOXY: Executable M code for cursor control.

## \$\$REWIND^%ZIS(): Rewind Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10086

Description: The \$\$REWIND^%ZIS extrinsic function rewinds special devices. These devices may be of the following types:

- Magtape
- Sequential Disk Processor
- Host File Server

Format: \$\$REWIND^%ZIS(io,iot,iopar)

Input Parameters: io: (required) The \$IO representation of the device to be rewound, in the same format as the IO variable, which is returned by [^%ZIS](#zis).

iot: (required) The “Type” of device to be rewound, in the same format as the IOT variable, which is returned by [^%ZIS](#zis).

iopar: (required) The “Open Parameters” for the selected device, in the same format as the IOPAR variable, which is returned by [^%ZIS](#zis).

Output: returns: Returns:

- 1—Device was rewound successfully.
- 0—Device was *not* rewound successfully.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950556" class="anchor"></span>Figure 10: \$\$REWIND^%ZIS API—Example

\><span class="mark">S Y=\$\$REWIND^%ZIS(IO,IOT,IOPAR)</span>

## ^%ZISC: Close Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10089

Description: The \$\$XMLHDR^MXMLUTL API closes a device opened with a call to the ^%ZIS API and restores the home device.

Do *not* issue a form feed when calling ^%ZISC. The Device Handler takes care of issuing a form feed if necessary (that is if \$Y\>0, indicating the cursor or print head is *not* at the top of form). To prevent the Device Handler from issuing this form feed, as appropriate for continuous printing of labels, for example, define the IONOFF input variable before calling ^%ZISC.

Before the ^%ZISC API existed, close logic was executed with the command X ^%ZIS(“C”). Developers have been advised that X ^%ZIS(“C”) is no longer supported and that the ^%ZISC API should be used instead. In the current version of Kernel, the ^%ZIS(“C”) node only holds a call to the ^%ZISC routine. Kernel versions beyond Kernel 8.0 will *not* export ^%ZIS(“C”).

Format: ^%ZISC

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
6.  Set all input variables.
7.  Call the API.

Input Variables: See [^%ZIS](#zis): For a list of input variables, see the normal device output variables from the [^%ZIS Standard Device Call](#zis) API.

Output Variables: See [^%ZIS](#zis): For a list of output variables, see the normal device output variables from the [^%ZIS Standard Device Call](#zis) API.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950557" class="anchor"></span>Figure 11: ^%ZISC API—Example

\><span class="mark">D ^%ZISC</span>

## PKILL^%ZISP: Kill Special Printer Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 3172

Description: The PKILL^%ZISP API KILLs printer-specific Device Handler variables. All output parameters defined by the <u>PSET^%ZISP: Set Up Special Printer Variables</u> API are KILLed.

Format: PKILL^%ZISP

Input Parameters: none.

Output: none.

## PSET^%ZISP: Set Up Special Printer Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 3172

Description: The PSET^%ZISP API defines a set of variables that toggle special printer modes. The corresponding fields in the TERMINAL TYPE (#3.2) file entry for the terminal type in question *must* be correctly set up, however; that is where PSET^%ZISP retrieves its output values.

Format: PSET^%ZISP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
8.  Set all input variables.
9.  Call the API.

Input Variables: IOST(0): (required) POINTER to the TERMINAL TYPE entry for the printer in question, as set up by the Device Handler.

Output Variables:IOBAROFF: Bar code off.

IOBARON: Bar code on.

IOCLROFF: Color off.

IOCLRON: Color on.

IODPLXL: Duplex, long edge binding.

IODPLXS: Duplex, short edge binding.

IOITLOFF: Italics off.

IOITLON: Italics on.

IOSMPLX: Simplex.

IOSPROFF: Superscript off.

IOSPRON: Superscript on.

IOSUBOFF: Subscript off.

IOSUBON: Subscript on.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To toggle a printer mode with one of PSET^%ZISP’s output variables, WRITE the variable to the printer using indirection, as follows:

<span id="_Toc199950558" class="anchor"></span>Figure 12: PSET^%ZISP API—Example

\><span class="mark">D PSET^%ZISP</span>

\><span class="mark">W @IOBARON</span>

## ENDR^%ZISS: Set Up Specific Screen Handling Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10088

Description: The ENDR^%ZISS API sets up specific screen-handling variables and other terminal type attributes. Unlike the <u>ENS^%ZISS: Set Up Screen-handling Variables</u> API, which sets up all screen-handling variables, you specify which ones to set up with ENDR^%ZISS.

Format: ENDR^%ZISS

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
10. Set all input variables.
11. Call the API.

Input Variables:IOST(0): (required) Internal entry number (IEN) of the selected device’s subtype as recorded in the TERMINAL TYPE (#3.2) file.

X: (required) Use this input variable to select the [ENS^%ZISS](#ensziss-set-up-screen-handling-variables) screen-handling variables to define. It should be a semicolon-delimited list of the variables to define. For example:

\>S X="IORVON;IORVOFF;IOUON;IOUOFF"

If more than 255 characters are needed to define the X variable, make two or more calls to ENDR^%ZISS, each with a partial list of the variable settings for X.

%ZIS: (optional) If you define %ZIS=“I”, the output array IOIS is created. The format of IOIS is as follows:

IOIS(ASCII value of first character followed by remaining characters)=output variable

For example:

IOIS("27\[C")=IOCUF

Not every screen-handling variable has a corresponding IOIS node. Also, only the nodes in the IOIS array that correspond to screen-handling variables specified in the X input variable are created.

Output Variables: See [ENS^%ZISS](#ensziss-set-up-screen-handling-variables): A subset of the output variables returned by <u>ENS^%ZISS: Set Up Screen-handling Variables</u> API are returned by ENDR^%ZISS, depending on what screen-handling variables are requested in the X input variable.

## ENS^%ZISS: Set Up Screen-handling Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10088

Description: The ENS^%ZISS API is used for screen management. It sets up screen handling variables and other terminal type attributes.

Format: ENS^%ZISS

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
12. Set all input variables.
13. Call the API.

Input Variables: IOST(0): (required) Internal entry number of the selected device’s subtype as recorded in the TERMINAL TYPE (#3.2) file.

%ZIS: (optional) If you define %ZIS = “I”, the output array IOIS (mapping escape codes sent by input keys to input keys) is created.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/023.png) REF: For a description of the IOIS nodes created, see the “[Output Variables](#ens_ziss_output_variables)” section.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/024.png) NOTE: Not all characteristics are possible on all terminal types for all output variables. The IOEFLD and IOSTBM variables are used with indirection. Also, IOSTBM requires the setting of IOTM and IOBM as input variables for the top and bottom margins.

<span id="ens_ziss_output_variables" class="anchor"></span>Output Variables:IOARM0: Auto repeat mode off.

IOARM1: Auto repeat mode on.

IOAWM0: Auto wrap mode off.

IOAWM1: Auto wrap mode on.

IOBOFF: Blink off.

IOBON: Blink on.

IOCOMMA: Keypad’s comma.

IOCUB: Cursor backward.

IOCUD: Cursor down.

IOCUF: Cursor forward.

IOCUON: Cursor on.

IOCUOFF: Cursor off.

IOCUU: Cursor up.

IODCH: Delete character.

IODHLB: Double-high/wide bottom.

IODHLT: Double-high/wide top.

IODL: Delete line.

IODWl: Doublewide length.

IOECH: Erase character.

IOEDALL: Erase in display entire page.

IOEDBOP: Erase in display from beginning of page to cursor.

IOEDEOP: Erase in display from cursor to end of page.

IOEFLD: Erase field (<sup>\*</sup>use through indirection, such as, W @IOEFLD).

IOELALL: Erase in line entire line.

IOELBOL: Erase in line from beginning of line to cursor.

IOELEOL: Erase in line from cursor to end of line.

IOENTER: Keypad’s Enter.

IOFIND: Find key.

IOHDWN: Half down.

IOHOME: Home cursor.

IOHTS: Horizontal tab set.

IOHUP: Half up.

IOICH: Insert character.

IOIL: Insert line.

IOIND: Index.

IOINHI: High intensity.

IOINLOW: Low intensity.

IOINORM: Normal intensity.

IOINSERT: Insert key.

IOKP0: Keypad 0.

IOKP1: Keypad 1.

IOKP2: Keypad 2.

IOKP3: Keypad 3.

IOKP4: Keypad 4.

IOKP5: Keypad 5.

IOKP6: Keypad 6.

IOKP7: Keypad 7.

IOKP8: Keypad 8.

IOKP9: Keypad 9.

IOIRM0: Replace mode.

IOIRM1: Insert mode.

IOKPAM: Keypad application mode on.

IOKPNM: Keypad numeric mode on.

IOMC: Print screen.

IOMINUS: Keypad’s minus.

IONEL: Next line.

IONEXTSC: Next screen.

IOPERIOD: Keypad’s period.

IOPF1: Function key 1.

IOPF2: Function key 2.

IOPF3: Function key 3.

IOPF4: Function key 4.

IOPREVSC: Previous screen.

IOPROP: Proportional spacing.

IOPTCH10:10 Pitch.

IOPTCH12:12 Pitch.

IOPTCH16:16 Pitch.

IORC: Restore cursor.

IOREMOVE: Keypad’s Remove.

IORESET: Reset.

IORI: Reverse index.

IORLF: Reverse line feed.

IORVOFF: Reverse video off.

IORVON: Reverse video on.

IOSC: Save cursor.

IOSGR0: Turn off select graphic rendition attributes.

IOSELECT: Keypad’s Select.

IOSTBM: Set top and bottom margins (<sup>\*</sup>use through indirection, such as, W @IOSTBM; IOTM and IOBM *must* be defined as the top and bottom margins).

IOSWL: Singlewide length.

IOTBC: Tab clear.

IOTBCALL: Clear all tabs.

IOUOFF: Underline off.

IOUON: Underline on.

IOIS: This array is created as follows:

IOIS(escape_code)=KEYNAME

Where escape_code is the escape code generated by pressing the key KEYNAME on the selected terminal, and KEYNAME can be one of the following:

- COMMA
- DO
- ENTER
- FIND
- HELP
- INSERT
- IOCUB
- IOCUD
- IOCUF
- IOCUU
- KP0
- KP1
- KP2
- KP3
- KP4
- KP5
- KP6
- KP7
- KP8
- KP9
- MINUS
- NEXTSCRN
- PERIOD
- PF1
- PF2
- PF3
- PF4
- PREVSCRN
- REMOVE
- SELECT

## GKILL^%ZISS: KILL Graphic Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10088

Description: The GKILL^%ZISS API is used for screen management. It KILLs graphic variables used in screen handling. All output parameters set up by the <u>GSET^%ZISS: Set Up Graphic Variables</u> API are KILLed.

Format: GKILL^%ZISS

Input Parameters: none.

Output: none.

## GSET^%ZISS: Set Up Graphic Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10088

Description: The GSET^%ZISS API is used for screen management. It sets up graphic variables for screen handling. Graphics on/off is a toggle that remaps characters for use as graphics. Not all terminals need remapping, since they already have the high range of ASCII codes.

Format: GSET^%ZISS

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
14. Set all input variables.
15. Call the API.

Input Variables: IOST(0): (required) Terminal Type.

Output Variables: IOBLC: Bottom left corner.

IOBRC: Bottom right corner.

IOBT: Bottom “T”.

IOG1: Graphics on.

IOG0: Graphics off.

IOHL: Horizontal line.

IOLT: Left “T”.

IOMT: Middle “T”, or cross hair (“+”).

IORT: Right “T”.

IOTLC: Top left corner.

IOTRC: Top right corner.

IOTT: Top “T”.

IOVL: Vertical line.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269962" class="anchor"></span>Figure 13: GSET^%ZISS API—Example

; write a horizontal line

D GSET^%ZISS

W IOG1

F I=1:1:20 W IOHL

W IOG0

D GKILL^%ZISS

## KILL^%ZISS: KILL Screen Handling Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 10088

Description: The KILL^%ZISS API is used for screen management. It KILLs graphic variables used in screen handling. Only the output parameters set up by the <u>ENS^%ZISS: Set Up Screen-handling Variables</u> and <u>ENDR^%ZISS: Set Up Specific Screen Handling Variables</u> APIs are KILLed by this call.

Format: KILL^%ZISS

Input Parameters: none.

Output: none.

## CALL^%ZISTCP: Make TCP/IP Connection (Remote System)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2118

Description: The CALL^%ZISTCP API makes a TCP/IP connection to a remote system.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/025.png) NOTE: This API is IPv6 compliant.

Format: CALL^%ZISTCP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
16. Set all input variables.
17. Call the API.

Input Variables: IPADDRESS: (required) This is the Internet Protocol (IP) address of the Host system to which it connects. It *must* be in either of the following formats:

- IPv4—Format of four numbers separated by dots (such as 99.99.9.999)
- IPv6—Format of six numbers separated by colons (such as fe80::206a:b21b:fbd5:c93).

SOCKET: (required) This is the socket to connect to on the remote host. It is an integer from 1-65535. Values below 5000 are reserved for standard Internet services (such as SMTP mail).

TIMEOUT: (optional) This is the timeout to apply to the Open.

Output Variables: IO: If the connection is made then the IO variable holds the implementation value that references the connection.

POP: This output variable reports the connection status:

- Successful—A value of Zero (0) means the connection was successful.
- Unsuccessful—A positive value means the connection failed.

It works the same as a call to the <u>^%ZIS: Standard Device Call</u> API.

## CLOSE^%ZISTCP: Close TCP/IP Connection (Remote System)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2118

Description: The CLOSE^%ZISTCP API closes the connection opened with the <u>CALL^%ZISTCP: Make TCP/IP Connection (Remote System)</u> API. It works like a call to the <u>^%ZISC: Close Device</u> API.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/026.png) NOTE: This API is IPv6 compliant.

Format: CLOSE^%ZISTCP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
18. Set all input variables.
19. Call the API.

Input Variables: See [CALL^%ZISTCP](#callzistcp-make-tcpip-connection-remote-system): For a list of input variables, see <u>CALL^%ZISTCP: Make TCP/IP Connection (Remote System</u> API.

Output Variables: For a list of output variables, see <u>CALL^%ZISTCP: Make TCP/IP Connection (Remote System</u> API.

## CLOSE^%ZISUTL(): Close Device with Handle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2119

Description: The CLOSE^%ZISUTL API closes a device opened with the <u>OPEN^%ZISUTL(): Open Device with Handle</u> API. When you close a device with CLOSE^%ZISUTL, the IO variables are set back to the home device’s and the home device is made the current device. One of three functions that support using multiple devices at the same time.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/027.png) REF: See also <u>OPEN^%ZISUTL(): Open Device with Handle</u> and <u>USE^%ZISUTL(): Use Device Given a Handle</u> APIs.

Format: CLOSE^%ZISUTL(handle)

Input Parameters: handle: (required) The handle of a device opened with the <u>OPEN^%ZISUTL(): Open Device with Handle</u> API.

Output: none.

## OPEN^%ZISUTL(): Open Device with Handle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2119

Description: Use the OPEN^%ZISUTL API when you expect to be using multiple output devices. This API, as well as its two companion APIs: <u>RMDEV^%ZISUTL(): Delete Data Given a Handle</u> and <u>CLOSE^%ZISUTL(): Close Device with Handle</u>, makes use of handles to refer to a device. A handle is a unique string identifying the device.

The three ^%ZISUTL APIs are essentially wrappers around the [^%ZIS](#zis) API. They provide enhanced management of IO variables and the current device, especially when working with multiple open devices. One of three functions that support using multiple devices at the same time.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/028.png) REF: See also <u>RMDEV^%ZISUTL(): Delete Data Given a Handle</u> and <u>CLOSE^%ZISUTL(): Close Device with Handle</u> APIs.

Format: OPEN^%ZISUTL(handle\[,valiop\]\[,.valzis\])

Input Parameters: handle: (required) A unique FREE TEXT name to associate with a device you want to open.

valiop: (optional) Output device specification, in the same format as the IOP input variable for the <u>^%ZIS: Standard Device Call</u> API. The one exception to this is passing a value of NULL; this is like leaving IOP undefined. With [^%ZIS](#zis), on the other hand, setting IOP to NULL specifies the home device. To request the home device, pass a value of “HOME” instead.

.valzis: (optional) Input specification array, in the same format (and with the same meanings) as the %ZIS input specification array for the <u>^%ZIS: Standard Device Call</u> API. *Must* be passed by reference.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/029.png) REF: For more information, see the [^%ZIS](#zis) API documentation.

Output Variables:IOF:OPEN^%ZISUTL returns all the same output variables as the <u>^%ZIS: Standard Device Call</u> API. OPEN^%ZISUTL serves as a “wrapper” around the <u>^%ZIS: Standard Device Call</u> API, providing additional management of IO output variables that ^%ZIS does *not* (principally to support opening multiple devices simultaneously).

![](kernel-8-0-developer-s-guide-device-handler-user-guide/030.png) REF: For more information on these variables, see the [^%ZIS](#zis) documentation.

IOMIOSLIOIO(0)IO(“Q”)IO(“S”)IO(“DOC”)IO(“SPOOL”)IO(“ZIO”)IO(“HFSIO”)IO(1,\$I)IOSTIOST(0)IOTIONIOBSIOPARIOUPARIOSIOHGIOXYPOP

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269963" class="anchor"></span>Figure 14: OPEN^%ZISUTL API—Example

ZXGTMP ; ISC-SF/doc %ZISUTL sample ;11-oct-94

;;1.0;;

EN ;

K A6AZIS S A6AZIS("A")="Enter the printer to output first 40 chars in each line: "

D OPEN^%ZISUTL("PRT1","",.A6AZIS) Q:POP

K A6AZIS S A6AZIS("A")="Enter the printer to output chars 41

to end of line: "

D OPEN^%ZISUTL("PRT2","",.A6AZIS) I POP D CLOSE^%ZISUTL("PRT1") Q

S I="" F S I=\$O(^TMP(\$J,"DOC",I)) Q:I'\]"" S X=^(I) D

.D USE^%ZISUTL("PRT1") U IO W \$E(X,1,40),!

.D USE^%ZISUTL("PRT2") U IO W \$E(X,41,\$L(X)),!

D CLOSE^%ZISUTL("PRT1"),CLOSE^%ZISUTL("PRT2")

Q

## RMDEV^%ZISUTL(): Delete Data Given a Handle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2119

Description: The RMDEV^%ZISUTL API deletes the data associated with the handle. It does *not* change any of the IO\* variables.

Format: RMDEV^%ZISUTL(handle)

Input Parameters: handle: (required) A unique FREE TEXT name to associate with a device that you want to delete.

Output: none.

## SAVDEV^%ZISUTL(): Save Data Given a Handle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2119

Description: The SAVDEV^%ZISUTL API saves the current device IO\* variables under the handle name.

Format: SAVDEV^%ZISUTL(handle)

Input Parameters: handle: (required) A unique FREE TEXT name to associate with a device that you want to save.

Output: none.

## USE^%ZISUTL(): Use Device Given a Handle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Device Handler

ICR \#: 2119

Description: The USE^%ZISUTL API restores the IO variables for a device saved with the <u>OPEN^%ZISUTL(): Open Device with Handle</u> or <u>SAVDEV^%ZISUTL(): Save Data Given a Handle</u> APIs. It then does a USE of the device if it is open. The same as:

\>DO USE^%ZISUTL(handle) U IO

![](kernel-8-0-developer-s-guide-device-handler-user-guide/031.png) REF: See also <u>OPEN^%ZISUTL(): Open Device with Handle</u> and <u>CALL^%ZISTCP: Make TCP/IP Connection (Remote System)</u> APIs.

Format: USE^%ZISUTL(handle)

Input Parameters: handle: (required) A unique FREE TEXT name to associate with the device that was opened with the <u>OPEN^%ZISUTL(): Open Device with Handle</u> API.

Output Variables:IO\*: Standard IO variables.

# Special Device Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the following special devices and device issues:

- <u>Form Feeds</u>
- <u>Resources</u>

## Form Feeds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device Handler has a method for issuing a form feed at the point when it closes the device. The purpose for this utility is to eliminate unnecessary page feeds at the beginning or end of a report. Extra page feeds result when an application issues its own form feed at the beginning of a report and then VA FileMan issues another pair, one at the beginning and one at the end. An additional problem is laser printers that also generate an extra form feed to clear the print buffer.

When closing a device, [^%ZISC](#zisc-close-device) checks the value of \$Y to determine the cursor or print head’s vertical line location. If \$Y is greater than Zero, the Device Handler WRITEs a form feed (W @IOF) to reset the value of \$Y to Zero. Therefore, applications should *not* issue any form feeds when calling the Device Handler to open or close a device.

VA FileMan has already removed its initial form feed. For the benefit of those who use VA FileMan without Kernel and its Device Handler, VA FileMan continues to issue a form feed at the end when the device is closed. Since this procedure resets the \$Y special variable to Zero, the Device Handler does *not* send an additional form feed when VA FileMan is used with Kernel.

Device Handler also checks for the existence of the IONOFF variable when closing the device. Thus, application developers can use the IONOFF variable to suppress form feeds by setting it just before calling <u>^%ZISC: Close Device</u> API to close the device.

### How to Check if Current Device is a CRT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should use the following code to test if the current device is a CRT:

\>I \$E(IOST,1,2)'="C-"

If it returns:

- False—Current device is a CRT.
- True—Assume that the current device is a printer.

### Guidelines for Form Issuing Form Feeds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In most cases, a form feed before the first page is only needed for reports to CRTs. When directing reports to a printer, do *not* issue an initial form feed before the first page; it is *not* needed. However, you should print the heading (if used) on the first page. You do need to issue a form feed between pages, regardless of whether the report is directed to a CRT or to a printer.

The following summarizes the current guidelines for issuing form feeds for CRTs and printers:

#### CRTs

1.  Issue the initial form feed before the first page of a report as before.
20. Print a heading on the first page if headings are used.
21. Print the lines of the report while checking the value of the vertical position (\$Y).
22. If there is no more data to process, then GO TO STEP 9.
23. If the value of the vertical position plus a predetermined number to serve as a buffer exceeds the screen length, prompt the user to press \<Enter\> to continue.
24. A time-out at the READ or a caret (^) response to the continue prompt represents a request to terminate the display. GO TO STEP 9.
25. If the user presses \<Enter\> in response to the prompt, issue a form feed followed by a heading (if used).
26. GO TO STEP 3.
27. The application should terminate the display of the report.
28. END.

#### Printers

1.  Do *not* issue a form feed before the first page of a report.
29. Print a heading on the first page if headings are used.
30. Print the lines of the report while checking the value of the vertical position (\$Y).
31. If there is no more data to process, then GO TO STEP 7.
32. If the value of the vertical position plus a predetermined number to serve as a buffer exceeds the page line limit, issue a form feed.
33. GO TO STEP 3.
34. The application should terminate the printout of the report.
35. END.

The sample routines <u>Figure 15</u> and <u>Figure 16</u> provide two examples of how to output a report following current guidelines for form feeds. In the examples, a series of three vertical dots indicates omitted information.

<span id="_Ref410971290" class="anchor"></span>Figure 15: Device Handler—Issuing Form Feeds following Current Guidelines

ROU ;SAMPLE ROUTINE

S IOP="DEVNAM" D ^%ZIS G EXIT:POP

I \$D(IO("Q")) S ZTRTN="DQ^ROU",ZTDESC="SAMPLE REPORT" D ^%ZTLOAD,HOME^%ZIS Q

.

.

.

DQ ;SAMPLE REPORT

S (END,PAGE)=0

U IO D @("HDR"\_(2-(\$E(IOST,1,2)="C-"))) F Q:END D

.W !,....

.W !,...

.D HDR:\$Y+5\>IOSL Q

.

.

.

D ^%ZISC Q

HDR ;SAMPLE HEADER

I \$E(IOST,1,2)="C-" W !,"Press RETURN to continue or '^' to exit: " R X:DTIME S END='\$T!(X="^") Q:END

HDR1 W @IOF

HDR2 S PAGE=PAGE+1 W ?20,"SAMPLE HEADING",?(IOM-10),"PAGE: ",\$J(PAGE,3)

<span id="_Ref410971301" class="anchor"></span>Figure 16: Device Handler—Alternate Approach following Current Guidelines

ROU ;SAMPLE ROUTINE

S IOP="DEVNAM" D ^%ZIS G EXIT:POP

I \$D(IO("Q")) S ZTRTN="DQ^ROU",ZTDESC="SAMPLE REPORT" D ^%ZTLOAD,HOME^%ZIS Q

.

.

.

DQ ;SAMPLE REPORT

S (END,PAGE)=0

U IO F Q:END D

.D HDR:\$Y+5\>IOSL Q

.W !,....

.W !,...

.

.

.

D ^%ZISC Q

HDR ;SAMPLE HEADER

I PAGE,\$E(IOST,1,2)="C-" W !,"Press RETURN to continue or '^' to exit: " R X:DTIME S END='\$T!(X="^") Q:END

HDR1 W:'(\$E(IOST,1,2)'="C-"&'PAGE) @IOF

HDR2 S PAGE=PAGE+1 W ?20,"SAMPLE HEADING",?(IOM-10),"PAGE: ",\$J(PAGE,3)

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Queuing to a Resource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can only use resources through calls to [^%ZTLOAD](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf#ztload). They *cannot* be directly manipulated (except by TaskMan). To use a resource, you need to set the ZTIO input variable to the name of the resource. For example:

\>S ZTIO="ZZRES",ZTRTN="tag^routine",ZTDTH=\$H

\>S ZTDESC="First task in a series"

\>D ^%ZTLOAD

Since the name of the resource is part of the call, application developers *must* include installation procedures so that system administrators are able to create the resources using the correct names and other attributes.

You can optionally use a SYNC FLAG when queuing to a Resource type device. Using a SYNC FLAG helps to ensure that sequential tasks queued to a resource only run if the preceding task in the series has completed successfully.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/032.png) REF: For more information on using SYNC FLAGs, see the [*Kernel 8.0 Developer’s Guide: TaskMan Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf).

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-device-handler-user-guide/033.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-device-handler-user-guide/034.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-device-handler-user-guide/035.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.