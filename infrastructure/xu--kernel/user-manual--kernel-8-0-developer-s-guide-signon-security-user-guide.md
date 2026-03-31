---
title: "Kernel 8.0 Developerâ€™s Guide: Signon/Security User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Signon/Security"
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
  - application
  - signon
  - table
  - contents
  - proxy
  - span
  - kernel
  - security
  - class
  - guide
page_count: 0
word_count: 7703
section_count: 35
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259528" class="anchor"></span>Signon/Security Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-signon-security-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-signon-security-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Signon/Security Developer Tools User Guide</em>.</p>
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

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-signon-security-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Direct Mode Utilities](#direct-mode-utilities)
  - [^XUP: Programmer Signon](#xup-programmer-signon)
  - [^XUS: User Signon: No Error Trapping](#xus-user-signon-no-error-trapping)
  - [H^XUS: Programmer Halt](#hxus-programmer-halt)
  - [^XUSCLEAN: Programmer Halt](#xusclean-programmer-halt)
  - [^ZU: User Signon](#zu-user-signon)
- [Developer Tools](#developer-tools)
  - [XU USER SIGN-ON Option](#xu-user-sign-on-option)
    - [XU USER SIGN-ON: Package-Specific Signon Actions](#xu-user-sign-on-package-specific-signon-actions)
    - [Example](#example)
  - [XU USER START-UP Option](#xu-user-start-up-option)
    - [XU USER START-UP: Application-specific Signon Actions](#xu-user-start-up-application-specific-signon-actions)
    - [Example:](#example-1)
  - [XU USER TERMINATE Option](#xu-user-terminate-option)
    - [Discontinuation of USER TERMINATE ROUTINE](#discontinuation-of-user-terminate-routine)
    - [Creating a Package-Specific User Termination Action](#creating-a-package-specific-user-termination-action)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$GET^XUPARAM(): Get Parameters](#getxuparam-get-parameters)
  - [\$\$KSP^XUPARAM(): Return Kernel Site Parameter](#kspxuparam-return-kernel-site-parameter)
    - [Examples](#examples)
  - [\$\$LKUP^XUPARAM(): Look Up Parameters](#lkupxuparam-look-up-parameters)
  - [SET^XUPARAM(): Set Parameters](#setxuparam-set-parameters)
  - [\$\$PROD^XUPROD(): Production or Test Account](#prodxuprod-production-or-test-account)
  - [H^XUS: Programmer Halt](#hxus-programmer-halt-1)
  - [SET^XUS1A(): Output Message During Signon](#setxus1a-output-message-during-signon)
    - [Details](#details)
  - [AVHLPTXT^XUS2: Get Help Text](#avhlptxtxus2-get-help-text)
  - [\$\$CREATE^XUSAP: Create Application Proxy User](#createxusap-create-application-proxy-user)
    - [Examples](#examples-1)
  - [KILL^XUSCLEAN: Clear all but Kernel Variables](#killxusclean-clear-all-but-kernel-variables)
  - [\$\$ADD^XUSERNEW(): Add New Users](#addxusernew-add-new-users)
    - [Examples](#examples-2)
  - [\$\$CHECKAV^XUSRB(): Check Access/Verify Codes](#checkavxusrb-check-accessverify-codes)
    - [Example](#example-2)
  - [CVC^XUSRB: VistALink—Change User’s Verify Code](#cvcxusrb-vistalinkchange-users-verify-code)
  - [\$\$INHIBIT^XUSRB: Check if Logons Inhibited](#inhibitxusrb-check-if-logons-inhibited)
  - [INTRO^XUSRB: VistALink—Get Introductory Text](#introxusrb-vistalinkget-introductory-text)
  - [LOGOUT^XUSRB: VistALink—Log Out User from M](#logoutxusrb-vistalinklog-out-user-from-m)
  - [SETUP^XUSRB(): VistALink—Set Up User’s Partition in M](#setupxusrb-vistalinkset-up-users-partition-in-m)
  - [VALIDAV^XUSRB(): VistALink—Validate User Credentials](#validavxusrb-vistalinkvalidate-user-credentials)
  - [\$\$DECRYP^XUSRB1(): Decrypt String](#decrypxusrb1-decrypt-string)
  - [\$\$ENCRYP^XUSRB1(): Encrypt String](#encrypxusrb1-encrypt-string)
  - [\$\$HANDLE^XUSRB4(): Return Unique Session ID String](#handlexusrb4-return-unique-session-id-string)
    - [Example](#example-3)
  - [^XUVERIFY: Verify Access and Verify Codes](#xuverify-verify-access-and-verify-codes)
  - [\$\$CHECKAV^XUVERIFY(): Check Access/Verify Codes](#checkavxuverify-check-accessverify-codes)
    - [Example](#example-4)
  - [WITNESS^XUVERIFY(): Return IEN of Users with A/V Codes and Security Keys](#witnessxuverify-return-ien-of-users-with-av-codes-and-security-keys)
    - [Example](#example-5)
  - [GETPEER^%ZOSV: VistALink—Get IP Address for Current Session](#getpeerzosv-vistalinkget-ip-address-for-current-session)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Signon/Security Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel’s Signon/Security module sets up a standard VistA programming environment as a foundation for software applications. Once a signon session has been created, applications can assume that system-wide variables exist for common reference. For example, key variables defined through Signon/Security include the user’s institution and agency (respectively):

- DUZ(2)
- DUZ(“AG”)

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Signon/Security direct mode utilities are available for developers to use at the M prompt. They are *not* APIs and *cannot* be used in software application routines. These utilities allow developers to simulate ordinary user signon and yet work from Programmer mode to test code and diagnose errors. These direct mode utilities are described below.

## ^XUP: Programmer Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^XUP routine can be called as a quick way to enter Kernel and set up a standard environment:

\>D ^XUP: Programmer Signon

It does the following:

- Sets up DT.
- Calls [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis).
- Prompts for Access Code if DUZ is Zero or undefined.
- KILLs and rebuilds ^XUTL(“XQ”,\$J).
- KILLs ^UTILITY(\$J).
- Calls ^XQ1 to prompt for an option if one should be run.

If a *non*-menu-type option is specified, returning from the option displays the “Select:” prompt as though the option was a menu-type. Although this construction may at first appear misleading, restricting option selection to menu-type only would be a functional limitation to the call.

## ^XUS: User Signon: No Error Trapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^XUS determines whether access to the computer is allowed, and then sets up the user with the proper environment:

\>D ^XUS

This routine can be called to establish the signon environment. A *recommended* alternative for developers is to call ^XUP, which establishes signon conditions as well as calling ^XQ1 for an option name. Neither ^XUP nor ^XUS sets the Error Trap. Entering through ^ZU sets the Error Trap and then calls the ^XUS routine.

## H^XUS: Programmer Halt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an obsolete utility:

\>D H^XUS

It simply transfers control to [^XUSCLEAN](#xusclean-programmer-halt).

## ^XUSCLEAN: Programmer Halt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Developers are advised to call the ^XUSCLEAN routine when signing off:

\>D ^XUSCLEAN

It is the same code that Kernel uses when a user signs off or restarts. It notes the signoff time in the SIGN-ON LOG (#3.081) file and KILLs the \$J nodes in ^XUTL and ^UTILITY. It then performs a normal halt.

## ^ZU: User Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZU routine sets the Error Trap and then calls ^XUS:

\>D ^ZU

User signons should be tied to ^ZU.

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## XU USER SIGN-ON Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some software applications asked for the means to execute an action at user signon, but *not* through the alert system. Kernel provides the XU USER SIGN-ON protocol option that software applications can attach to and perform software application-specific tasks on user signon.

### XU USER SIGN-ON: Package-Specific Signon Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0 introduced a method to support software application-specific signon actions. Kernel exports an extended-action option called XU USER SIGN-ON. Packages that want Kernel to execute a software application-specific user signon routine can accomplish this by attaching their own option, of type action, to Kernel’s XU USER SIGN-ON protocol option. Your action-type option should call your software application-specific user signon routine.

To attach your option to the XU USER SIGN-ON protocol option, make your option an item of the XU USER SIGN-ON protocol; then, export your option with a KIDS action of SEND, and export the XU USER SIGN-ON option with a KIDS action of USE AS LINK FOR MENU ITEMS.

During signon, Kernel executes the XU USER SIGN-ON protocol option, which in turn executes any options that software applications have attached to XU USER SIGN-ON. No database Integration Control Registrations are required to attach to the XU USER SIGN-ON protocol option.

If you need to perform any output during your action, you should use the [SET^XUS1A](#setxus1a-output-message-during-signon) function to perform the output. Output is *not* immediate but occurs once all software application-specific signon actions have completed. Also, you should *not* perform any tasks requiring interaction in an action attached to the XU USER SIGN-ON protocol option.

The DUZ variable is defined at the time the signon actions are executed; DUZ is set as it normally is to the person’s Internal Entry Number (IEN) in the NEW PERSON (#200) file.

Take care to make code efficient, since executed by every signon. A few examples of tasks you might want to accomplish during signon are:

- Alert the user to a software application status.
- Issue a reminder.
- Notify the software application of the signon of a software application user.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option in <u>Figure 1</u>, when attached to the XU USER SIGN-ON protocol, outputs one line during signon:

<span id="_Ref502896187" class="anchor"></span>Figure 1: XU USER SIGN-ON—Sample ZZTALK Protocol

NAME: ZZTALK PROTOCOL MENU TEXT: TALKING PROTOCOL

TYPE: action E ACTION PRESENT: YES

DESCRIPTION: USE TO TEST EXTENDED ACTION PROTOCOLS

ENTRY ACTION: D SET^XUS1A("!This line is from the ZZTALK option.")

UPPERCASE MENU TEXT: TALKING PROTOCOL

## XU USER START-UP Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA software developers asked for the means to execute an action at VistA user signon, but *not* through the alert system. Added with Kernel Patch XU\*8.0\*593, the XU USER START-UP protocol option is used exclusively during a VistA user signon event. Items attached to this option are “TYPE: action” options in the OPTION (#19) file, which can be used for software-specific actions that prompt users for input upon VistA signon before their Primary Menu Option is displayed. Unlike the XU USER SIGN-ON protocol option, it can provide interactive prompting to users. It is *not* used for GUI signon. It is called from the XQ12 routine.

### XU USER START-UP: Application-specific Signon Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0 introduced a method to support application-specific VistA (*non*-GUI) signon actions. Kernel Patch XU\*8.0\*593 exports the XU USER START-UP extended-action option. VistA applications that want Kernel to execute an application-specific user signon routine can do this by attaching their own option, of TYPE: action, to Kernel’s XU USER START-UP protocol option. The action-type option should call the application-specific user signon routine.

To attach your option to the XU USER START-UP protocol option, perform the following procedure:

Make your option an item of the XU USER START-UP protocol.

1.  Export your option with a KIDS action of SEND.
2.  Export the XU USER START-UP option with a KIDS action of USE AS LINK FOR MENU ITEMS.

During signon, Kernel executes the XU USER START-UP protocol option before the user’s Primary Menu Option is displayed, which in turn executes any options that applications have attached to XU USER START-UP. No database Integration Control Registrations are required to attach to the XU USER START-UP protocol option.

Since this option is only used for VistA signon sessions and *not* GUI signon, tasks requiring interaction are permitted. If you want a task to prevent a user from signing on, then the task should set the variable XUSQUIT=1.

The DUZ variable is defined at the time the signon actions are executed; DUZ is set as it normally is to the person’s Internal Entry Number (IEN) in the NEW PERSON (#200) file.

Take care to make code efficient, since it is executed at every VistA signon. The following are examples of tasks you might want to accomplish during a VistA signon:

- Prompt the user to update their phone number in the NEW PERSON (#200) file.
- Block a user’s access unless they electronically sign a security agreement.

### Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option in <u>Figure 2</u>, when attached to the XU USER SIGN-ON protocol, outputs one line during signon:

<span id="_Ref502896342" class="anchor"></span>Figure 2: XU USER START-UP Option—Sample Signon Action-type Option

NAME: ZZXU593 SAMPLE OPTION

<span class="mark">TYPE: action</span> E ACTION PRESENT: YES

DESCRIPTION: PROMPT USER TO EDIT SIGNATURE BLOCK

ENTRY ACTION: D SAMPLE^XQ12

UPPERCASE MENU TEXT: SAMPLE OPTION

## XU USER TERMINATE Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 8.0 introduced a method to support software application-specific user termination actions. Kernel 8.0 exports an extended-action option called XU USER TERMINATE. Packages that want Kernel to execute a software application-specific user termination action can accomplish this by attaching their own option, of type action, to Kernel’s XU USER TERMINATE extended action.

### Discontinuation of USER TERMINATE ROUTINE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel 7.1 introduced a method for software applications to have Kernel execute a software application-specific routine when Kernel terminated a user. The method was for the software application to have a routine tag and name in the following fields of the software application’s PACKAGE (#9.4) file entry:

- USER TERMINATE TAG (#200.1) field
- USER TERMINATE ROUTINE (#200.2) field

When Kernel 7.1 terminated a user, it executed the TAG^ROUTINE API stored in these fields, if any.

Kernel 8.0 continues to execute the API, if any, stored in a software application’s PACKAGE (#9.4) file entry. However, Kernel 8.0 is the last version to support that method of software application-specific user termination routines.

### Creating a Package-Specific User Termination Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beginning with Kernel 8.0, you should create an action-type option that calls your software application-specific user termination routine. To attach it to the XU USER TERMINATE protocol option, do the following:

Export your option with a KIDS action of SEND.

3.  Export the XU USER TERMINATE option with a KIDS action of USE AS LINK FOR MENU ITEMS.

Kernel defines the XUIFN variable at the time your action executes; it is defined as the Internal Entry Number (IEN) in the NEW PERSON (#200) file of the user being terminated.

When terminating a user, Kernel executes the XU USER TERMINATE protocol option, which in turn executes any options attached to XU USER TERMINATE. No database Integration Control Registrations are required to attach to the XU USER TERMINATE protocol option.

A few examples of user clean up you might want to accomplish when Kernel terminates users are as follows:

- Removal of HINQ access.
- Removal of Control Point access.
- Removal from health care teams.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Signon/Security APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$GET^XUPARAM(): Get Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2542

Description: The \$\$GET^XUPARAM extrinsic function gets simple parameters from the KERNEL PARAMETERS (#8989.2) file that the site can edit.

Format: \$\$GET^XUPARAM(parameter_name\[,style\])

Input Parameters: parameter_name: (required) This is the namespaced name of the parameter to look up in the KERNEL PARAMETERS (#8989.2) file and return the REPLACEMENT value or DEFAULT.

style: (optional) This input parameter controls the return value if the REPLACEMENT value or DEFAULT is empty.

Output: returns: Returns the REPLACEMENT value or DEFAULT.

## \$\$KSP^XUPARAM(): Return Kernel Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2541

Description: The \$\$KSP^XUPARAM extrinsic function retrieves a Kernel site parameter. The following parameters are currently supported:

- INST
- SPOOL DOC
- SPOOL LIFE
- SPOOL LINE
- WHERE

Format: \$\$KSP^XUPARAM(param)

Input Parameters: param: (required) Site parameter to retrieve. Currently, the following values for param are supported:

- INST—Internal Entry Number (IEN) of the site’s institution, in the site’s INSTITUTION (#4) file.
- SPOOL DOC—MAX SPOOL DOCUMENTS PER USER (internal value) from the site’s KERNEL SYSTEM PARAMETERS (#8989.3) file.
- SPOOL LIFE—MAX SPOOL DOCUMENT LIFE-SPAN (internal value) from the site’s KERNEL SYSTEM PARAMETERS (#8989.3) file.
- SPOOL LINE—MAX SPOOL LINES PER USER (internal value) from site’s KERNEL SYSTEM PARAMETERS (#8989.3) file.
- WHERE—Site’s domain name (FREE TEXT value), from the site’s DOMAIN (#4.2) file.

Output: returns: Returns the requested site parameter value.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950700" class="anchor"></span>Figure 3: \$\$KSP^XUPARAM API—Example 1

\><span class="mark">S A6ASITE=\$\$KSP^XUPARAM("WHERE")</span>

#### Example 2

<span id="_Toc199950701" class="anchor"></span>Figure 4: \$\$KSP^XUPARAM API—Example 2

\><span class="mark">S A6ASPLLF=\$\$KSP^XUPARAM("SPOOL LIFE")</span>

## \$\$LKUP^XUPARAM(): Look Up Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2542

Description: The \$\$LKUP^XUPARAM extrinsic function looks up simple parameters from the KERNEL PARAMETERS (#8989.2) file that the site can edit.

Format: \$\$LKUP^XUPARAM(parameter_name\[,style\])

Input Parameters: parameter_name: (required) This is the namespaced name of the parameter to look up in the KERNEL PARAMETERS (#8989.2) file and return the REPLACEMENT value or DEFAULT.

style: (optional) This input parameter controls the return value if the REPLACEMENT value or DEFAULT is empty.

Output: returns: Returns the REPLACEMENT value or DEFAULT.

## SET^XUPARAM(): Set Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2542

Description: The SET^XUPARAM API sets simple parameters in the KERNEL PARAMETERS (#8989.2) file.

Format: SET^XUPARAM(parameter_name\[,style\])

Input Parameters: parameter_name: (required) This is the namespaced name of the parameter to set in the KERNEL PARAMETERS (#8989.2) file.

style: (optional) This input parameter controls the return value if the REPLACEMENT (#4) field value or DEFAULT (#3) field is empty.

Output: none.

## \$\$PROD^XUPROD(): Production or Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 4440

Description: The \$\$PROD^XUPROD extrinsic function is called by applications to check and see if the application is running in a Production or a Test account.

The Ask if Production Account \[XU SID ASK\] option on the Kernel Management Menu \[XUKERNEL\], asks if the current account is the Production account. It returns the following values:

- True (1 or *non*-Zero)—If the answer is YES, the account is the Production account, so the current system ID (SID) is set as the Production SID.
- False (Zero)—If the answer is NO, the account is *not* the Production account, so a fake value is stored.

The Startup PROD check \[XU SID STARTUP\] option can be scheduled for startup so that when TaskMan starts the SID is checked. The first check each day gets the current SID and compares it with the stored SID to see if they match.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/004.png) NOTE: This API was released with Kernel Patch XU\*8.0\*284.

Format: \$\$PROD^XUPROD(\[force\])

Input Parameters: force: (optional) The parameter value of 1 allows an application to force a full test.

Output: returns: Returns a Boolean value:

- True (1 or *non*-Zero)—Production account, current SID is set as the Production SID.
- False (Zero)—Test account.

## H^XUS: Programmer Halt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 10044

Description: The H^XUS API is the ProgrammerHalt.

Format: H^XUS

Input Parameters: none.

Output: none.

## SET^XUS1A(): Output Message During Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 3057

Description: The SET^XUS1A API performs any output during a software application-specific action executed at signon. This function should *only* be used by action-type options attached to and executed by Kernel’s XU USER SIGN-ON extended action.

Display of the string is *not* immediate; instead, every call to SET^XUS1A appends a node to an array containing the post signon text. When all software application-specific signon actions have completed, the signon process then displays the post signon text array, which also contains any strings registered with the SET^XUS1A function, appended at the end.

Format: SET^XUS1A(string)

Input Parameters: string: (required) String to output. First character is stripped from string; if the first character is an exclamation point, a line feed is issued before the string is displayed; otherwise, no line feed is issued.

Output: none.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Kernel 8.0, software applications can attach an action-type option to a Kernel extended action-type option called XU USER SIGN-ON. This option, and all attached action-types, are executed during every signon.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/005.png) REF: For more information on software application-specific action executed at signon, see the “<u>XU USER SIGN-ON: Package-Specific Signon Actions</u>” section.

## AVHLPTXT^XUS2: Get Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4057

Description: The AVHLPTXT^XUS2 API retrieves help text to display to the user when they change their Verify Code.

Format: AVHLPTXT^XUS2

Input Parameters: none.

Output: returns: Returns the help text for a user to use when entering a new Verify Code.

## \$\$CREATE^XUSAP: Create Application Proxy User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4677

Description: The \$\$CREATE^XUSAP extrinsic function is a *non*-interactive API to create an Application Proxy User to support J2EE middle-tier applications. The Application Proxy User represents an application and *not* an end-user.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/006.png) ATTENTION: If a new Application Proxy name is being added to the NEW PERSON (#200) file, then the new Application Proxy information *<u>must be added to ICR \#4677 with the specifics</u>*. The developer needs to do the following:

1.  Make an ICR request at: [ICR Request Intake Form](https://dvagov.sharepoint.com/sites/OITEPMOVistAOffice/SitePages/Integration%20Control%20Registration%20(ICR)%20Request%20Intake%20Form.aspx) (or enter an email) to request subscribing to ICR 4677.
2.  Include in the request specific information that will be added to the NEW PERSON (#200) file entry to represent the Proxy User, Name, Secondary Menu Option associated with the user, and justification for the design that needs an Application Proxy.
3.  Send a message to the OIT PD Integration Control Registrations (\<REDACTED\>@va.gov) team. That team adds subject matter experts (SMEs) to the message string to solicit review and approval.

Upon approval, the summary information will be added to the SUBSCRIBER details in ICR 4677.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/007.png) CAUTION: If the user running this extrinsic function does *not* hold the XUMGR security key, it returns an error upon the filing of the Application Proxy as the User Class.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*361.

Overview

The Application Proxy User is a special category of user account that is created in the NEW PERSON (#200) file and can run internal tasks or execute authorized Remote Procedure Calls (RPCs). The Application Proxy represents an application and *not* an end-user. The Application Proxy user account *must* adhere to the following criteria:

- The name added to the NEW PERSON (#200) file *must* be unique and *must* be namespaced in accordance with M Programming Standards and Conventions (SAC) Section 2.6, “Name Requirements.”
- It *must* have a user class of “Application Proxy,” as defined in the USER CLASS (#201) file and pointed to by the USER CLASS (#9.5) field in the NEW PERSON (#200) file.
- It *mustnot* have an Access or Verify Code assigned to it.
- It *mustnot* have a Primary menu assigned to it.
- It *must* have one or more Secondary menu options assigned to it. The Secondary menu option *must* be owned by the application that the Application Proxy represents, or the application *must* have an Integration Control Registration (ICR) with the option owner. The Secondary menu option contains a list of RPCs that the Application Proxy is authorized to call, as described in the “RPC Security” section in the *RPC Broker User Guide*.
- The RPCs that the menu options reference *must* have the APP PROXY ALLOWED (#.11) field in the REMOTE PROCEDURE (#8994) file set to YES. The RPCs *must* be owned by the application that the Application Proxy represents, or the application *must* have an ICR with the RPC owner.
- The use of an Application Proxy *must* be restricted to accessing *non*-protected data. Federal laws specify when an actual end-user *must* be represented when accessing Personally Identifiable Information (PII) and Protected Health Information (PHI). Information regarding user authentication, identity, auditing, and authorization can be found in:
- *VA Information Security Handbook 6500 Appendix F*
- National Institute of Standards and Technology (NIST) e-Authentication Guidelines (800-63-2)
- Health Insurance Portability and Accountability Act of 1996 (HIPAA) federal law 45 CFR § 160 & § 164

Application Proxy Privacy and Auditing

Many VistA data interactions by human end-users *must* be represented with accurate and unambiguous user identity information, so that VistA audit mechanisms function as intended. Application Proxy user accounts do *not* identify the user and should be avoided, especially where the interaction is with PHI/PII data (regulated by federal law). The use of Application Proxy user accounts should be limited to background processes and machine-to-machine interactions.

Application Proxy Permission

Permission to use the \$\$CREATE^XUSAP API should be done early in the development process; as use of Application Proxy user accounts are reviewed by VA management due to security concerns.

Format: \$\$CREATE^XUSAP(proxyusername\[,filemanaccesscode\]\[,options\])

Input Parameters: proxyusername: (required) This is the name of the Application Proxy User (such as VPR,APPLICATION PROXY). This name *must* be unique and should be namespaced.

filemanaccesscode: (optional) This is the VA FileMan Access Code. It *cannot* be an at-sign (@).

![](kernel-8-0-developer-s-guide-signon-security-user-guide/009.png) REF: For more information, see the *VA FileMan Advanced User Manual*.

options: (optional) This is the name of a single option name (such as VPR APPLICATION PROXY) or an array of options, such as XUOPT(“XMUSER”)=1. Applications can only access the Remote Procedure Calls (RPCs) contained in the options provided in this input parameter. RPCs are tied to “B”-type options.

Output: returns: Returns:

- IEN of entry created in the NEW PERSON (#200) file—Successful; writes new Application Proxy User to the NEW PERSON (#200) file.
- “0^Name In Use”—Unsuccessful; Application Proxy User of that name already exists in the NEW PERSON (#200) file.
- -1—Unsuccessful due to either of the following:
- Could *not* create Application Proxy User.
- Error in call to UPDATE^DIE.

> ![](kernel-8-0-developer-s-guide-signon-security-user-guide/010.png) NOTE: For more information on the UPDATE^DIE-related error, users should check ^TMP(“DIERR”,\$J).

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Application Proxy Example—Good

<u>Figure 5</u> shows the successful creation of an Application Proxy User:

<span id="_Ref502135850" class="anchor"></span>Figure 5: \$\$CREATE^XUSAP API—Example

\>IF \$\$CREATE^XUSAP("VPR,APPLICATION PROXY","","VPR APPLICATION PROXY")\>0 W !,"Proxy Created"

Proxy Created

<u>Figure 6</u> is an example of an Application Proxy user account that is provisioned correctly:

<span id="_Ref442255647" class="anchor"></span>Figure 6: Application Proxy—Example: Good

NAME: <span class="mark">VPR,APPLICATION PROXY</span> DATE ENTERED: SEP 01, 2011

CREATOR: XUUSER,ONE

SECONDARY MENU OPTIONS: VPR APPLICATION PROXY

TIMESTAMP: 62335,62903

User Class: APPLICATION PROXY ISPRIMARY: Yes

The Proxy User List \[XUSAP PROXY LIST\] option lists the current Application Proxy user accounts, as shown in <u>Figure 7</u>:

<span id="_Ref442255614" class="anchor"></span>Figure 7: Application Proxy—Example: Good; Displayed Using Proxy User List Option

PROXY USER LIST JAN 28,2016 09:44 PAGE 1

NAME User Class IsPrimary Active

--------------------------------------------------------------------------

XOBVTESTER,APPLICATION PROXY APPLICATION PROXY Yes

ANRVAPPLICATION,PROXY USER APPLICATION PROXY Yes

VPFS,APPLICATION PROXY APPLICATION PROXY Yes

RADIOLOGY,OUTSIDE SERVICE APPLICATION PROXY Yes

LRLAB,HL APPLICATION PROXY Yes

LRLAB,POC APPLICATION PROXY Yes

TASKMAN,PROXY USER APPLICATION PROXY Yes

CLINICAL,DEVICE PROXY SERVICE APPLICATION PROXY Yes

NHIN,APPLICATION PROXY APPLICATION PROXY Yes

EDPTRACKING,PROXY APPLICATION PROXY Yes

KAAJEE,PROXY APPLICATION PROXY Yes

<span class="mark">VPR,APPLICATION PROXY APPLICATION PROXY Yes</span>

AUTHORIZER,IB REG APPLICATION PROXY Yes

HOWDY,BOT APPLICATION PROXY Yes

LRLAB,TASKMAN APPLICATION PROXY Yes

VIABAPPLICATIONPROXY,VIAB APPLICATION PROXY Yes

![](kernel-8-0-developer-s-guide-signon-security-user-guide/011.png) CAUTION: Some of the listed Application Proxy user accounts do *not* follow the rules for namespacing. There are other serious infractions in current applications using Application Proxy user accounts, which puts the VA in the position of violating federal privacy laws by accessing PHI/PII information. *VA Handbook 6500 Appendix F* lists VA System Security Controls that are applicable to Application Proxy user accounts as well as human end-users. An Application Proxy should *never* be used to circumvent VA System Security Controls.

#### Application Proxy Example—Bad

<u>Figure 8</u> is an example of an Application Proxy user account that is *not* provisioned correctly:

<span id="_Ref442255705" class="anchor"></span>Figure 8: Application Proxy Example (Bad) (1 of 2)

NAME: TASKMAN,PROXY USER FILE MANAGER ACCESS CODE: \#

DATE ENTERED: JUN 9,2009 CREATOR: LABTECH,FORTYEIGHT

NAME COMPONENTS: 200

SIGNATURE BLOCK PRINTED NAME: PROXY USER TASKMAN

TIMESTAMP: 62362,53550

User Class: APPLICATION PROXY ISPRIMARY: Yes

If provisioned correctly, the name “TASKMAN,PROXY USER” would be identified by the Kernel (XU) namespace, such as “XUTASKMAN,PROXY USER”. This Application Proxy does *not* require access to any menu options or RPCs, so it does *not* contain a SECONDARY MENU OPTION.

<u>Figure 9</u> is another example of an Application Proxy user account that is *not* provisioned correctly:

<span id="_Ref442255721" class="anchor"></span>Figure 9: Application Proxy Example (Bad) (2 of 2)

NAME: CLINICAL,DEVICE PROXY SERVICE DATE ENTERED: JUN 30,2010

CREATOR: XUUSER,ONE

SECONDARY MENU OPTIONS: MD GUI MANAGER

SECONDARY MENU OPTIONS: MD GUI USER

TIMESTAMP: 61907,71682

User Class: APPLICATION PROXY ISPRIMARY: Yes

In this example, the SECONDARY MENU OPTIONs are in the Clinical Procedures (MD) namespace, so that if provisioned correctly, “CLINICAL,DEVICE PROXY SERVICE” would be more appropriately named “MDCLINICAL,DEVICE PROXY SERVICE”.

## KILL^XUSCLEAN: Clear all but Kernel Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 10052

Description: The KILL^XUSCLEAN API clears the partition of all but key variables essential to Kernel. Application developers are allowed to use this call to clean up application variables and leave the local symbol table unchanged when returning from an option or as otherwise required by SAC Standards.

In the past, options that have called KILL^XUSCLEAN have occasionally created problems for other options that had defined software-wide variables. For example, a user might enter the top-level menu for a software application, which could have an entry action that retrieved site parameters into a local variable that is supposed to remain defined while in any menu of that software application, between options. But if the user could then reach a secondary menu option that happened to call KILL^XUSCLEAN, a side effect would be the KILLing off the previously defined software-wide variable.

KILL^XUSCLEAN now provides a way for sites and developers to work around this problem. For any menu-type option, the PROTECTED VARIABLES (#1840) field in the OPTION (#19) file allows you to enter a comma-delimited list of variables to protect from being KILLed by KILL^XUSCLEAN. Once a user enters a menu subtree descendent from the protected menu, the variables are protected until the menu subtree is exited.

So, for example, to protect a software-wide variable for an entire software application, you can enter that variable in the PROTECTED VARIABLES (#1840) field for the top-level menu in the software application. If a user does *not* exit the top-level menu of the software application’s menu tree, the software-wide variable is protected from all calls to KILL^XUSCLEAN. “Up-arrow Jumps” (using a caret; ^) into a menu tree also work fine, if the menu that has been protected is in the menu path made by the jump.

Format: KILL^XUSCLEAN

Input Parameters: none.

Output: none.

## \$\$ADD^XUSERNEW(): Add New Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 10053

Description: The \$\$ADD^XUSERNEW extrinsic function adds new entries to the NEW PERSON (#200) file. After prompting for the user’s name, it parses the input into its component parts, and then prompts for each name component separately, presenting the parsed input as defaults. It then prompts for the default identifiers for the NEW PERSON (#200) file entry in the following order:

1.  INITIAL (#1)
2.  SSN (#9)
3.  SEX (#4)

If the user of this function has the XUSPF200 security key, entry of the SSN is *not* required. The default identifiers can be locally modified by modifying the NEW PERSON IDENTIFIERS field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/012.png) NOTE: This API was modified with Kernel Patch XU\*8.0\*134.

To prompt for additional fields during this call, you pass a DR string containing the fields for which you wish to prompt as a parameter to this function. If the person adding the entry enters a caret (^) to exit out before filling in all the identifiers and requested fields, the entry is removed from the NEW PERSON (#200) file, and -1 is returned.

Format: \$\$ADD^XUSERNEW(\[dr_string\]\[,keys\])

Input Parameters: dr_string: (optional) Additional fields to ask when adding the new user, in the format for a DR string as used in a standard DIC call.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/013.png) REF: For information about DIC, see the VA FileMan Developer’s Guide.

keys: (optional) A comma-delimited string of keys to assign to the newly created user.

Output: returns: Returns a value similar in format to the value of Y returned from a standard DIC call:

- -1—User neither existed nor could be added.
- N^S—User already exists in the file; N is the internal number of the entry in the file, and S is the value of the .01 field for that entry.
- N^S^1—N and S are defined as above, and the 1 indicates the user has just been added to the file.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/014.png) REF: For information about DIC, see the VA FileMan Developer’s Guide.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

To add a new user, asking default fields for new entry:

<span id="_Toc200270032" class="anchor"></span>Figure 10: \$\$ADD^XUSERNEW API—Example 1: Adding a New User

\><span class="mark">S X=\$\$ADD^XUSERNEW \<Enter\></span>

Enter NEW PERSON's name (Family,Given Middle Suffix): <span class="mark">XUUSER,TWO E \<Enter\></span>

Are you adding 'XUUSER,TWO E' as a new NEW PERSON (the 1602ND)? No// <span class="mark">Y \<Enter\></span> (Yes)

Checking SOUNDEX for matches.

No matches found.

Name components.

FAMILY (LAST) NAME: XUUSER// <span class="mark">\<Enter\></span>

GIVEN (FIRST) NAME: TWO// <span class="mark">\<Enter\></span>

MIDDLE NAME: E// <span class="mark">\<Enter\></span>

SUFFIX: <span class="mark">\<Enter\></span>

Now for the Identifiers.

INITIAL: <span class="mark">TE</span>X

SSN: <span class="mark">000222222 \<Enter\></span>

SEX: <span class="mark">M \<Enter\></span> MALE

\><span class="mark">W X \<Enter\></span>

1000118^XUUSER,TWO E^1

\>

#### Example 2

To add a new user, specifying a key to add:

<span id="_Toc199950708" class="anchor"></span>Figure 11: \$\$ADD^XUSERNEW API—Example 2

\><span class="mark">S X=\$\$ADD^XUSERNEW("","PROVIDER")</span>

#### Example 3

To add a new user, specifying additional fields to ask, plus two keys to add:

<span id="_Toc199950709" class="anchor"></span>Figure 12: \$\$ADD^XUSERNEW API—Example 3

\><span class="mark">S X=\$\$ADD^XUSERNEW("5;13;53","PSMGR,PSNARC")</span>

## \$\$CHECKAV^XUSRB(): Check Access/Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 2882

Description: The \$\$CHECKAV^XUSRB extrinsic function checks an Access/Verify Code pair (delimited by a semi-colon) and returns whether it is a valid pair.

Format: \$\$CHECKAV^XUSRB(access_verify)

Input Parameters: access_verify: (required) This is a string containing the Access and Verify Code pair delimited by a semi-colon (that is Access Code;Verify Code).

Output: returns: Returns:

- Internal Entry Number (IEN)—Codes are OK.
- Zero (0)—Codes are *not* OK.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950710" class="anchor"></span>Figure 13: \$\$CHECKAV^XUSRB API—Example

\><span class="mark">S X=\$CHECKAV^XUSRB(*\<string\>*)</span>

String = Access Code;Verify Code

## CVC^XUSRB: VistALink—Change User’s Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4054

Description: The CVC^XUSRB API changes a VistALink user’s Verify Code.

Format: CVC^XUSRB

Input Parameters: none.

Output Variables: DUZ: If DUZ is defined, you can consider the “Change Verify Code” operation to have been successful.

## \$\$INHIBIT^XUSRB: Check if Logons Inhibited

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 3277

Description: The \$\$INHIBIT^XUSRB extrinsic function checks if logons have been inhibited.

Format: \$\$INHIBIT^XUSRB

Input Parameters: none.

Output: none.

## INTRO^XUSRB: VistALink—Get Introductory Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4054

Description: The INTRO^XUSRB API retrieves the introductory text from M to display in VistALink.

Format: INTRO^XUSRB

Input Parameters: none.

Output: returns: Returns each line in the introductory text as a value stored at the first subscript level node of the pass-by-reference first parameter to the method call. For example:

RETURN(0)=line 1 RETURN(1)=line 2 and so on

## LOGOUT^XUSRB: VistALink—Log Out User from M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4054

Description: The LOGOUT^XUSRB API logs out a VistALink user from M.

Format: LOGOUT^XUSRB

Input Parameters: none.

Output: none.

## SETUP^XUSRB(): VistALink—Set Up User’s Partition in M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4054

Description: The SETUP^XUSRB API sets up a VistALink user’s partition in M prior to signon.

Format: SETUP^XUSRB(ret)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Parameters: ret: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

Input Variables: XWBTIP: (required) The Internet Protocol (IP) address of the client workstation.

XWBCLMAN: (optional) The client workstation name.

XWBVER: (optional) This is the version of the RPC Broker software on the client workstation.

Output: ret(): Returns a subscripted output array:

RET(0)—Server option name  
RET(1)—Volume  
RET(2)—UCI  
RET(3)—Device  
RET(4)—# Attempts  
RET(5)—Skip signon-screen  
RET(6)—Domain name

## VALIDAV^XUSRB(): VistALink—Validate User Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4054

Description: The VALIDAV^XUSRB API validates a VistALink user’s credentials for signon to M.

Format: VALIDAV^XUSRB(credential)

Input Parameters: credential: (required) A credential (typically the encoded “Access Code;Verify Code” string) to use to attempt a signon for the current user.

Output: returns: Returns:

;Return R(0)=DUZ, R(1)=(0=OK, 1,2...=Can't sign on for some reason)  
; R(2)=verify needs changing, R(3)=Message, R(4)=0, R(5)=msg cnt, R(5+n)  
; R(R(5)+6)=# div user must select from, R(R(5)+6+n)=div

## \$\$DECRYP^XUSRB1(): Decrypt String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2241

Description: The \$\$DECRYP^XUSRB1 extrinsic function decrypts a string that was encrypted on a Client system. This function decrypts a string that has been encrypted using the Encrypt Delphi function supplied by the RPC Broker, returning the decrypted string.

Format: \$\$DECRYP^XUSRB1(encrypted_string)

Input Parameters: encrypted_string: (required) Encrypted string to be decrypted.

Output: returns: Returns the decrypted string.

## \$\$ENCRYP^XUSRB1(): Encrypt String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 2240

Description: The \$\$ENCRYP^XUSRB1 extrinsic function encrypts a string before transport to a Client system, where it is decrypted. This function performs encryption on the input string, returning the encrypted string.

Format: \$\$ENCRYP^XUSRB1(string)

Input Parameters: string: (required) The input string to be encrypted.

Output: returns: Returns the encrypted string.

## \$\$HANDLE^XUSRB4(): Return Unique Session ID String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 4770

Description: The \$\$HANDLE^XUSRB4 extrinsic function returns a unique Caché cluster string for a VistA system for use by HealtheVet Desktop applications.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/015.png) NOTE: This API was released with Kernel Patch XU\*8.0\*395.

Format: \$\$HANDLE^XUSRB4("namespace"\[,timetolive\])

Input Parameters: “namespace”: (required) This input parameter should start with the VistA software namespace. In addition, users can add any additional application/software identifiers.

timetolive: (optional) This input parameter indicates the number of days that this handle is available for use. Possible values range from 1 to 7. The default is 1. The ^XTMP global requires that the Zero node hold the save through date. This value is cleaned up using the XQ82 routine (that is Clean old Job Nodes in XUTL \[XQ XUTL \$J NODES\] option).

Output: returns: Returns the unique Vista system Caché cluster string. The value generated includes the data entered in the namespace input parameter and \$J and \$H. If this value is already defined, a new value is generated.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In <u>Figure 14</u>, you are creating a unique session ID for the RPC Broker namespace (that is “XWB”):

<span id="_Ref502213595" class="anchor"></span>Figure 14: \$\$HANDLE^XUSRB4 API—Example

\><span class="mark">S HDL=\$\$HANDLE^XUSRB4("XWB-CCOW")</span>

\><span class="mark">W HDL</span>

XWB-CCOW928-57785_0

When checking the ^XTMP temporary global you would see:

^XTMP("XWB-CCOW928-57785_0",0) = 3050805^3050804

## ^XUVERIFY: Verify Access and Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 10051

Description: The ^XUVERIFY API validates Access and Verify codes. You can use it anytime within an application program to verify that the person using the system is the same person who signed onto the system.

Format: ^XUVERIFY

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
6.  Set all input variables.
7.  Call the API.

Input Variables: %: (required) If % equals:

- A—Check the Access Code.
- V—Check the Verify Code.
- AV—Check both the Access and Verify Code.

%DUZ: (required) The user’s number (DUZ value).

Output Variables: %: Returns the following values:

- 2—Failure (the incorrect code was entered).
- 1—Success (the correct code was entered).
- 0—A question mark was entered.
- -1—A caret (^) was entered.

## \$\$CHECKAV^XUVERIFY(): Check Access/Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Signon/Security

ICR \#: 10051

Description: The \$\$CHECKAV^XUVERIFY extrinsic function checks an Access/Verify Code pair entered by the user (delimited by a semi-colon) and returns whether it is a valid pair.

Format: \$\$CHECKAV^XUVERIFY(access_verify)

Input Parameters: access_verify: (required) This is a string containing the Access and Verify Code pair delimited by a semi-colon (that is Access Code;Verify Code).

Output: returns: Returns:

- Internal Entry Number (IEN)—Codes are OK.
- Zero (0)—Codes are *not* OK.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950712" class="anchor"></span>Figure 15: \$\$CHECKAV^XUVERIFY API—Example

\><span class="mark">S X=\$CHECKAV^XUVERIFY(*\<string\>*)</span>

String = Access Code;Verify Code

## WITNESS^XUVERIFY(): Return IEN of Users with A/V Codes and Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 1513

Description: The WITNESS^XUVERIFY API returns the IEN of a user if they have:

- Access Code
- Verify Code
- Security keys

Format: WITNESS^XUVERIFY(prefix,keys)

Input Parameters: prefix: String to put before the Access/Verify Code prompt.

keys: String of security keys the user *must* have.

Output: returns: Returns:

- IEN (successful)—The user has an Access Code, Verify Code, and security keys.
- 0 (failure)—The user does *not* have an Access Code, Verify Code, and security keys.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950713" class="anchor"></span>Figure 16: WITNESS^XUVERIFY API—Example

\><span class="mark">S Y=\$\$WITNESS^XUVERIFY("Cosign","XUMGR") W !,Y</span>

Cosign ACCESS CODE: \*\*\*\*\*\*\*\*

Cosign VERIFY CODE: \*\*\*\*\*\*\*\*

2

## GETPEER^%ZOSV: VistALink—Get IP Address for Current Session

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4056

Description: The GETPEER^%ZOSV API retrieves an IP address value for the current session, which is required as input (that is XWBTIP input variable) for the <u>SETUP^XUSRB(): VistALink—Set Up User’s Partition in M</u> API. The VistALink security module calls this API.

Format: GETPEER^%ZOSV

Input Parameters: none.

Output: returns: Returns the Internet Protocol (IP) address of the current connected session to M.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-signon-security-user-guide/016.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-signon-security-user-guide/017.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-signon-security-user-guide/018.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.