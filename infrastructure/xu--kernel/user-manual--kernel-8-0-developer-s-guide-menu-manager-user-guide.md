---
title: "Kernel 8.0 Developerâ€™s Guide: Menu Manager User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Menu Manager"
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
  - protocol
  - table
  - contents
  - guide
  - manager
  - input
  - kernel
  - developer
  - xqmm
  - options
page_count: 0
word_count: 5168
section_count: 22
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259421" class="anchor"></span>Menu Manager Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Menu Manager Developer Tools User Guide</em>.</p>
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

<span id="_Toc207254149" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Developer Tools](#developer-tools)
  - [Creating Options](#creating-options)
    - [Option Types](#option-types)
    - [Creating Options (Edit Options)](#creating-options-edit-options)
  - [Variables for Developer Use](#variables-for-developer-use)
    - [XQUIT: Quit the Option](#xquit-quit-the-option)
    - [XQMM(“A”): Menu Prompt](#xqmma-menu-prompt)
    - [XQMM(“B”): Default Response](#xqmmb-default-response)
    - [XQMM(“J”): The Phantom Jump](#xqmmj-the-phantom-jump)
    - [XQMM(“N”): No Menu Display](#xqmmn-no-menu-display)
  - [Direct Mode Utilities](#direct-mode-utilities)
    - [^XQ1: Test an Option](#xq1-test-an-option)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$ADD^XPDMENU(): Add Option to Menu](#addxpdmenu-add-option-to-menu)
  - [\$\$DELETE^XPDMENU(): Delete Menu Item](#deletexpdmenu-delete-menu-item)
  - [\$\$LKOPT^XPDMENU(): Look Up Option IEN](#lkoptxpdmenu-look-up-option-ien)
  - [LOCK^XPDMENU(): Set LOCK Field in OPTION File](#lockxpdmenu-set-lock-field-in-option-file)
  - [OUT^XPDMENU(): Edit Option’s Out of Order Message](#outxpdmenu-edit-options-out-of-order-message)
  - [RENAME^XPDMENU(): Rename Option](#renamexpdmenu-rename-option)
  - [RLOCK^XPDMENU(): Set REVERSE/NEGATIVE Field in OPTION File](#rlockxpdmenu-set-reversenegative-field-in-option-file)
  - [\$\$TYPE^XPDMENU(): Get Option Type](#typexpdmenu-get-option-type)
  - [\$\$ADD^XPDPROT(): Add Child Protocol to Parent Protocol](#addxpdprot-add-child-protocol-to-parent-protocol)
  - [\$\$DELETE^XPDPROT(): Delete Child Protocol from Parent Protocol](#deletexpdprot-delete-child-protocol-from-parent-protocol)
  - [FIND^XPDPROT(): Find All Parents for a Protocol](#findxpdprot-find-all-parents-for-a-protocol)
  - [\$\$LKPROT^XPDPROT(): Look Up Protocol IEN](#lkprotxpdprot-look-up-protocol-ien)
  - [OUT^XPDPROT(): Edit Protocol’s Out of Order Message](#outxpdprot-edit-protocols-out-of-order-message)
  - [RENAME^XPDPROT(): Rename Protocol](#renamexpdprot-rename-protocol)
  - [\$\$TYPE^XPDPROT(): Get Protocol Type](#typexpdprot-get-protocol-type)
  - [NEXT^XQ92(): Restricted Times Check](#nextxq92-restricted-times-check)
  - [\$\$ACCESS^XQCHK(): User Option Access Test](#accessxqchk-user-option-access-test)
  - [OP^XQCHK(): Current Option Check](#opxqchk-current-option-check)
    - [Examples](#examples)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Menu Manager Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Creating Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can develop applications quickly and easily using Menu Manager. Once you have defined a set of files using VA FileMan, you can use Menu Manager to provide a menu of options including entering, editing, displaying, and printing information. You can use M code to tailor the functioning of an option, in the option’s header, entry, or exit action. You can create specialized routine-type options. And you can associate help frames with options (as described in the Help Processor section) to further enhance option creation and custom tailoring.

### Option Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several different option types ;exist:

- Edit, Inquire, and Print are mainly used to access VA FileMan files.
- Action and Run Routine types are available for invoking M code.
- Menu types, as discussed earlier in this section, are used to group other options for presentation to the user at the select prompt.
- Server options are options that can be addressed through MailMan (sending to S.SERVER NAME). The server activity, such as the running of a routine, is then carried out.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/004.png) REF: For a complete description, see the [*Kernel 8.0 Developer's Guide: Server Options Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_server_options_ug.pdf).

- Protocol, Protocol Menu, Extended Action, and Limited option types are specific to the XQOR (Unwinder) software application. Control is passed to the XQOR (Unwinder) software for processing. The Extended Action type, for example, “unwinds” the items on a menu in a specific order. Protocol Menus are formatted in multiple columns allowing several items to be selected at once. The Protocol-type option prompts the user for a selection. Limited protocols involve patient-oriented processing, rather than application-specific tasks. Any of these option types are included, like other options, when a software application is exported.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/005.png) REF: For more information, see the Computerized Patient Record System (CPRS) or Unwinder (XQOR) documentation.

### Creating Options (Edit Options)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200270028" class="anchor"></span>Figure 1: Menu Manager—Edit options \[XUEDITOPT\]

MENU MANAGEMENT... \[XUMAINT\]

<span class="mark">Edit options</span> \[XUEDITOPT\]

You can define options with the Edit Options template, available from the Menu Management menu. Depending on what type of option you are editing, the Edit Options template branches to the fields in the OPTION (#19) file appropriate for that option type.

Some option types (Edit, Inquire, and Print) have fields whose names correspond to VA FileMan DI variables. The Edit Options template branches to the DI fields that have relevance to the type of VA FileMan call being made by the option.

For Edit type options, the DI fields presented correspond to the input variables for a VA FileMan ^DIE call. Likewise, inquire-type options correspond to VA FileMan ^DIQ calls, and print options to ^DIP calls.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/006.png) REF: For a complete description of the meaning of the variables represented by each of the DI fields, see the *VA FileMan Developer’s Guide*.

#### Options that Should be Regularly Scheduled

If an option should be regularly scheduled to run through TaskMan, you should set its SCHEDULING RECOMMENDED (#209) field in the OPTION (#19) file) to YES. Sites are *not* able to use Schedule/Unschedule Options to schedule an option unless this field is set to YES for the option.

## Variables for Developer Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance and functioning of the menu system can be modified by developers by using several variables. The variables can be defined within applications, such as in an option’s:

- Entry Action
- Exit Action
- Header

The following variables are described in the sections below:

- <u>XQUIT: Quit the Option</u>
- <u>XQMM(“A”): Menu Prompt</u>
- <u>XQMM(“B”): Default Response</u>
- <u>XQMM(“J”): The Phantom Jump</u>
- <u>XQMM(“N”): No Menu Display</u>

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/007.png) NOTE: The XQMM variables can be used individually or together. It is *strongly recommended* that you test the effects of XQMM variables with the AUTO MENU display, DUZ(“AUTO”), turned on and off.

### XQUIT: Quit the Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XQUIT variable can be set in an option’s Entry Action to cause Menu Manager to quit and *not* invoke the option. The menu system does *not* run the option, either as a foreground job or background task, and does *not* jump past the option. If an option’s use depends on the existence of certain application-specific key variables, for example, the Entry Action logic can set XQUIT if those variables are *not* defined. Menu Manager simply checks for the existence of the XQUIT variable, so it can be set to NULL (S  XQUIT=“”) or to a value as the developer chooses.

### XQMM(“A”): Menu Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If XQMM(“A”) exists, the menu system uses it as the prompt instead of the normal “Select...option” menu prompt. The XQMM(“A”) variable is KILLed immediately after it is used. It does *not* inhibit the AUTO MENU display. If the user has chosen to have options displayed at each cycle of the menu system, then the options are displayed *before* the XQMM(“A”) prompt is presented. Unlike the phantom jump, prompts *must* be set singularly and cannot be concatenated with a semicolon.

### XQMM(“B”): Default Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If XQMM(“B”) is defined, the menu system uses it as the default response and is presented along with the usual two slashes (//). If the user accepts the default by pressing \<Enter\>, the default becomes the user’s response.

XQMM(“B”) identifies an option if set to a unique synonym or a unique string of text from the beginning of the option’s menu text. This option *must* exist on the user’s current menu. If the option *cannot* be found, Menu Manager responds with two question marks (??), KILL both XQMM(“A”) and XQMM(“B”), and display the standard menu prompt.

### XQMM(“J”): The Phantom Jump

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XQMM(“J”) variable can be used to force a menu jump to an option within the user’s menu tree. Set it equal to the exact option name (that is .01 field of the OPTION \[#19\] file) to which Menu Manager should jump. For example:

\>S XQMM("J")="XUMAINT"

This jumps to the Menu Management option if that option is within the user’s menu tree.

The phantom jump automatically turns off the user’s menu display for one cycle through the menu system so that the user does *not* see a list of choices before jumping to an option that is *not* on that list.

The phantom jump can also be used to designate a set of options for a series of jumps, called a script. The exact option names should be separated with semicolons. For example:

\>S XQMM("J")="XUMAINT;DIUSER"

After jumping to Menu Management, the menu system would jump to VA FileMan (if all access and security requirements are met).

After all the options in a script have been completed, the phantom jump logic returns the user to the option that was last run before the script was invoked. If for some reason this cannot be accomplished, the user is returned to their primary menu.

### XQMM(“N”): No Menu Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XQMM(“N”) variable can be used to suppress the AUTO MENU display of menu options for one menu cycle. XQMM(“N”) is then KILLed, and the display resumes as usual. XQMM(“N”) can be used in conjunction with XQMM(“A”) and XQMM(“B”) to present only the custom tailored menu prompts.

Setting XQMM(“N”) does *not* change the display for users who already suppress the AUTO MENU display. For users who have AUTO MENU turned on, XQMM(“N”) takes precedence over DUZ(“AUTO”).

It is *not* necessary to define XQMM(“N”) when using the phantom jump, XQMM(“J”), since the display is already suppressed. If XQMM(“J”) is present, then XQMM(“N”) is *not*KILLed after the first cycle since the phantom jump is already inhibiting the display. In this case, XQMM(“N”) is KILLed after the second cycle (the display of menus after the jump is completed). If several phantom jumps are chained together, XQMM(“N”) is *not*KILLed until one cycle after the final jump unless code is added to explicitly KILL it between jumps.

## Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Menu Manager direct mode utilities are available for developers to use at the M prompt. They are *not* APIs and *cannot* be used in software application routines. These direct mode utilities are described below.

### ^XQ1: Test an Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^XQ1 routine asks you to select an option; it then uses the selected option as the primary menu option for entry into the menu system (at the top of ^XQ). This provides a way for an individual in Programmer mode to enter the menu system at a desired option:

\>D ^XQ1^XQ1 is also called by ^XUP.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/008.png) CAUTION: Developers are advised to use ^XUP instead of ^XQ1 to enter Kernel from Programmer mode, since the ^XUP routine sets up a standard environment and takes care of cleanup activities.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/009.png) REF: For a description of the ^XUP direct mode utility, see the [*Kernel 8.0 Developer's Guide: Signon/Security Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf).

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/010.png) NOTE: While D ^XQ1 is a direct mode utility, it is *not* a callable API.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Menu Manager APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$ADD^XPDMENU(): Add Option to Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The \$\$ADD^XPDMENU extrinsic function adds an option as a new item to an existing menu.

Format: \$\$ADD^XPDMENU(menu,option\[,syn\]\[,order\])

Input Parameters: menu: (required) Name of the menu to which an option should be added.

option: (required) Name of the option being added to the menu.

syn: (optional) Synonym to add to the SYNONYM field in the new menu item.

order: (optional) Order to place in the DISPLAY ORDER field in the new menu item.

Output: returns: Returns:

- 1—Success, option added to menu.
- 0—Failure, option *not* added to menu.

## \$\$DELETE^XPDMENU(): Delete Menu Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The \$\$DELETE^XPDMENU extrinsic function deletes an option from the Menu field of another option. It returns the following values:

- 1—If the function succeeded.
- 0—If it failed.

Format: \$\$DELETE^XPDMENU(menu,option)

Input Parameters: menu: (required) This is the name of the option from which you want to delete a menu item.

option: (required) This is the name of the option you want to delete from the menu item of the menu input parameter.

Output: returns: Returns:

- 1—Success, menu item deleted.
- 0—Failure, menu item *not* deleted.

## \$\$LKOPT^XPDMENU(): Look Up Option IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The \$\$LKOPT^XPDMENU extrinsic function looks up an option’s Internal Entry Number (IEN) using the “B” cross-reference.

Format: \$\$LKOPT^XPDMENU(option)

Input Parameters: option: (required) The name of the option.

Output: returns: Returns the Internal Entry Number (IEN) of the input option in the OPTION (#19) file.

## LOCK^XPDMENU(): Set LOCK Field in OPTION File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The LOCK^XPDMENU API sets the LOCK (#3) field in the OPTION (#19) file for a given option.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/011.png) NOTE: This API was released with Kernel Patch XU\*8.0\*672.

Format: LOCK^XPDMENU(opt,txt)

Input Parameters: opt: (required) This is the name of the option you want to lock.

txt: (required) This is the security key name used to lock the option. It *must* match an entry in the SECURITY KEY (#19.1) file.

Output: none. Sets the LOCK (#3) field in the OPTION (#19) file for the opt input parameter.

## OUT^XPDMENU(): Edit Option’s Out of Order Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The OUT^XPDMENU API creates or deletes an out of order message for an option; this action effectively puts the option out of order or back in order.

Format: OUT^XPDMENU(option,text)

Input Parameters: option: (required) Name of option in which to place a value in the OUT OF ORDER MESSAGE (#2) field in the OPTION (#19) file.

text: (required) Text of message to place in the option’s OUT OF ORDER MESSAGE (#2) field.

If this is *not*NULL, the text is stored in the option’s OUT OF ORDER MESSAGE (#2) field and the option is placed out of order.

If this parameter is passed as a NULL string, the current OUT OF ORDER MESSAGE (#2) field value is deleted, and the option is put back in order.

Output: none.

## RENAME^XPDMENU(): Rename Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The RENAME^XPDMENU API renames an existing option.

Format: RENAME^XPDMENU(old,new)

Input Parameters: old: (required) Current option name (.01 field of OPTION \[#19\] file entry). *Must* be an exact match.

new: (required) New name for option.

Output: none.

## RLOCK^XPDMENU(): Set REVERSE/NEGATIVE Field in OPTION File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The RLOCK^XPDMENU API sets the REVERSE/NEGATIVE (#3.01) field in the OPTION (#19) file for a given option.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/012.png) NOTE: This API was released with Kernel Patch XU\*8.0\*672.

Format: RLOCK^XPDMENU(opt,txt)

Input Parameters: opt: (required) This is the name of the option you want to reverse lock.

txt: (required) This is the security key name used to reverse lock the option. It *must* match an entry in the SECURITY KEY (#19.1) file.

Output: none. Reverses the lock on the REVERSE/NEGATIVE (#3.01) field in the OPTION (#19) file for the opt input parameter.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/013.png) REF: For more information on reverse locks, see the “Using Security Keys with Reverse Locks” section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf).

## \$\$TYPE^XPDMENU(): Get Option Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 1157

Description: The \$\$TYPE^XPDMENU extrinsic function returns the option’s TYPE (#4) field in the OPTION (#19) file.

Format: \$\$TYPE^XPDMENU(option)

Input Parameters: option: (required) The name of the option.

Output: returns: Returns the one character TYPE (#4) field value of the input option in the OPTION (#19) file. For example:

- A—Action
- E—Edit
- I—Inquire
- M—Menu
- P—Print
- R—Run routine
- O—Protocol
- Q—Protocol Menu
- X—Extended Action
- S—Server
- L—Limited
- C—ScreenMan
- W—Window
- Z—Window Suite
- B—Broker (Client/Server)

## \$\$ADD^XPDPROT(): Add Child Protocol to Parent Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The \$\$ADD^XPDPROT extrinsic function adds a child input protocol to a parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/014.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: \$\$ADD^XPDPROT(parent,child\[,mnemonic\]\[,sequence\])

Input Parameters: parent: (required) Name of the parent input protocol in the PROTOCOL (#101) file to which a child input protocol should be added.

child: (required) Name of the child input protocol being added to the parent input protocol in the PROTOCOL (#101) file.

mnemonic: (optional) The mnemonic value to be added to the MNEMONIC (#2) field in the ITEM (#10) Multiple field in the PROTOCOL (#101) file for the child in the parent protocol.

sequence: (optional) The sequence value to be added to the SEQUENCE (#3) field in the ITEM (#10) Multiple field in the PROTOCOL (#101) file for the child in the parent protocol.

Output: returns: Returns:

- 1—Success, child input protocol added to the parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.
- 0—Failure, child input protocol *not* added to the parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.

## \$\$DELETE^XPDPROT(): Delete Child Protocol from Parent Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The \$\$DELETE^XPDPROT extrinsic function deletes a child input protocol from a parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/015.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: \$\$DELETE^XPDPROT(parent,child)

Input Parameters: parent: (required) Name of the parent protocol in the PROTOCOL (#101) file from which a child protocol should be deleted.

child: (required) Name of the child protocol being deleted from the parent protocol in the PROTOCOL (#101) file.

Output: returns: Returns:

- 1—Success: The child input protocol deleted from the parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.
- 0—Failure: The child input protocol *not* deleted from the parent input protocol ITEM (#10) Multiple field in the PROTOCOL (#101) file.

## FIND^XPDPROT(): Find All Parents for a Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The FIND^XPDPROT API finds all parents for a protocol in the PROTOCOL (#101) file and returns the list in the RESULT array:

- RESULT(0)=Number of parents found or -1^error message.
- RESULT(IEN)=Protocol name.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/016.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: FIND^XPDPROT(.result,protocol)

Input Parameters: .result: (required) The array to return the results, passed by reference:

- RESULT(0)=Number of parents found or  
  > -1^error message.
- RESULT(IEN)=Protocol name.

protocol: (required) Name of the protocol in the PROTOCOL (#101) file for which to find the parents.

Output: returns: Returns the RESULT array:

RESULT(0)=Number of parents found or -1^error message.

RESULT(ien)=Protocol name

## \$\$LKPROT^XPDPROT(): Look Up Protocol IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The \$\$LKPROT^XPDPROT extrinsic function returns the internal entry number (IEN) of the input protocol from the PROTOCOL (#101) file.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/017.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: \$\$LKPROT^XPDPROT(protocol)

Input Parameters: protocol: (required) Name of the protocol to look up in the PROTOCOL (#101) file.

Output: returns: Returns the internal entry number (IEN) of the input protocol in the PROTOCOL (#101) file.

## OUT^XPDPROT(): Edit Protocol’s Out of Order Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The OUT^XPDPROT API creates or deletes an “Out of Order” message in the DISABLE (#2) field in the PROTOCOL (#101) file for the input protocol.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/018.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: OUT^XPDPROT(protocol,text)

Input Parameters: protocol: (required) Name of the protocol in the PROTOCOL (#101) file to which the “Out of Order” text is assigned.

text: (required) Text value:

- Text—Message text to place in the DISABLE (#2) field in the PROTOCOL (#101) file for the input protocol.
- NULL—Delete any message text in the DISABLE (#2) field in the PROTOCOL (#101) file for the input protocol.

Output: returns: Returns:

- Text—Updated message text in the DISABLE (#2) field in the PROTOCOL (#101) file for the input protocol. Marking the protocol “Out of Order.”
- NULL—Deleted message text in the DISABLE (#2) field in the PROTOCOL (#101) file for the input protocol.

## RENAME^XPDPROT(): Rename Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The RENAME^XPDPROT API renames an existing protocol name. It updates the value in the NAME (#.01) field in the PROTOCOL (#101) file.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/019.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: RENAME^XPDPROT(old,new)

Input Parameters: old: (required) Current (old) name of the protocol to be renamed in the PROTOCOL (#101) file.

new: (required) New name for the protocol.

Output: returns: Returns the updated NAME (#.01) field in the PROTOCOL (#101) file.

## \$\$TYPE^XPDPROT(): Get Protocol Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 5567

Description: The \$\$TYPE^XPDPROT extrinsic function returns the value of the TYPE (#4) field in the PROTOCOL (#101) file for the input protocol IEN.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/020.png) NOTE: This API was released with Kernel Patch XU\*8.0\*547.

Format: \$\$TYPE^XPDPROT(protocol_ien)

Input Parameters: protocol_ien: (required) The protocol’s internal entry number (IEN) in the PROTOCOL (#101) file.

Output: returns: Returns the one character TYPE (#4) field value in the PROTOCOL (#101) file for the input protocol IEN. For example:

- A—Action: Same as the X type, except any existing sub-items are *not* executed.
- M—Menu: Use this type for displaying and selecting items.
- O—Protocol: This value is strictly related to the Add orders function. It is the same as the Q type, except the protocol is the item selected. Protocols are directly executed when encountered.
- Q—Protocol Menu: This value is strictly related to the Add orders function. Use it for displaying and selecting orderable items during the add sequence. When this type of protocol is encountered OE/RR prompts the user with “Select PATIENT:,” “LOCATION:,” and “Provider:,” and execute the transaction logic for the new orders screen.
- L—Limited Protocol: This value is strictly related to the Add orders function. It is the same as the O type, except any existing sub-items are *not* executed.
- X—Extended Action: Protocols of this type execute the entry action plus all sub-items.
- D—Dialog.
- T—Term.
- E—Event Driver.
- S—Subscriber.

## NEXT^XQ92(): Restricted Times Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 10077

Description: The NEXT^XQ92 API returns the next time an option can run, checking any time or date restrictions placed on the option. If there are no times in the next week when the option can be run, the x parameter is returned as NULL, and a message is issued regarding the time restriction.

Format: NEXT^XQ92(ien,x)

Input Parameters: ien: (required) Internal entry number (IEN) of the option in the OPTION (#19) file.

Output: x: The DATE/TIME in VA FileMan format of the next unrestricted runtime when the option can run:

- Current Time—If the option can run at the current time.
- NULL—If the option is prohibited for the entire next week. It also issues a message regarding the time restriction.

## \$\$ACCESS^XQCHK(): User Option Access Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 10078

Description: The \$\$ACCESS^XQCHK extrinsic function determines if a user has access to a particular option.

Format: \$\$ACCESS^XQCHK(duz,option)

Input Parameters: duz: (required) The identification number of the user in question in the NEW PERSON (#200) file.

option: (required) The Internal Entry Number (IEN) or option name of the option in question in the OPTION (#19) file.

Output: returns: Returns:

- -1—No such user in the NEW PERSON (#200) file.
- -2—User terminated or has no Access Code.
- -3—No such option in the OPTION (#19) file.
- 0—No access found in any menu tree the user owns.
- 4-Piece String:access^menu tree IEN^a SET OF CODES^key0^tree^codes^key: No access because of locks (see XQCODES below).

  1^OpIEN^^: Access allowed through Primary Menu.

  2^OpIEN^codes^: Access found in the Common Options.

  3^OpIEN^codes^: Access found in top level of secondary option.

  4^OpIEN^codes^: Access through the secondary menu tree OpIEN.

XQCODES can contain the following:

- N—No Primary Menu in the NEW PERSON (#200) file (warning only).
- L—Locked and the user does *not* have the key (forces Zero \[0\] in first piece).
- R—Reverse lock and user has the key (forces Zero \[0\] in first piece).

## OP^XQCHK(): Current Option Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Menu Manager

ICR \#: 10078

Description: The OP^XQCHK API returns the current option or protocol name and menu text in the first and second pieces of the XQOPT output variable. It looks for the local XQORNOD variable if defined or the local XQY variable; the internal number of the option. If XQORNOD is defined, it needs to be in the VARIABLE POINTER format:

XQORNOD=*\<internal number of the protocol\>*;*\<protocol file\>*

If the search is unsuccessful, because the job is *not* running out of the menu system or is *not* a tasked option, XQOPT is returned with -1 in the first piece and “Unknown” in the second.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/021.png) NOTE: OP^XQCHK *cannot* return option/protocol information if the job is a task that did *not* originate from an option.

Format: OP^XQCHK

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: XQORNOD: (optional) If this variable is defined, it should be in VARIABLE POINTER format. For example:

XQORNOD="1234;ORD(101,"Output Variables: XQOPT: Returns a string in the following format:

Option/Protocol Name^Menu Text

> If neither an option nor a protocol can be identified, XQOPT is returned as:

-1^Unknown

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950638" class="anchor"></span>Figure 2: OP^XQCHK API—Example 1

\><span class="mark">K XQORNOD D OP^XQCHK W !,XQOPT</span>

\>EVE^Systems Manager Menu

#### Example 2

<span id="_Toc199950639" class="anchor"></span>Figure 3: OP^XQCHK API—Example 2

\><span class="mark">S XQORNOD="445;ORD(101," D OP^XQCHK W !,XQOPT</span>

\>XU USER EVENT TERMINATE^Terminate User Event

#### Example 3

<span id="_Toc199950640" class="anchor"></span>Figure 4: OP^XQCHK API—Example 3

\><span class="mark">S XQORNOD="9;DIC(19," D OP^XQCHK W !,XQOPT</span>

\>EVE^Systems Manager Menu

#### Example 4

<span id="_Toc199950641" class="anchor"></span>Figure 5: OP^XQCHK API—Example 4

\><span class="mark">K XQORNOD,XQY,XQOPT D OP^XQCHK W !,XQOPT</span>

\>-1^Unknown

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/022.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/023.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-menu-manager-user-guide/024.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.