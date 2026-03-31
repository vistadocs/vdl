---
title: "Kernel 8.0 Systems Management: Menu Manager User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: Menu Manager"
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
menu_options: 3
description: 
audience: 
keywords: 
  - options
  - span
  - table
  - class
  - contents
  - help
  - security
  - keys
  - management
  - server
page_count: 0
word_count: 23586
section_count: 21
table_count: 6
figure_count: 1
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Menu Manager User Guide
---

![](kernel-8-0-systems-management-menu-manager-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-menu-manager-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref26360709" class="anchor"></span>Table 1: Menu Diagramming Options to Discover Tree Roots and Relationships between Options/Suboptions</p></caption>
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
<td>07/25/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<p>Updated external document links to open documents in a new window.</p></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Menu Manager User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref26360709" class="anchor"></span>Table 1: Menu Diagramming Options to Discover Tree Roots and Relationships between Options/Suboptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="List_of_Figures" class="anchor"></span>List of Figures

<span id="List_of_Tables" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-systems-management-menu-manager-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Menu Manager: User Interface](#menu-manager-user-interface)
  - [Navigating Kernel’s Menus](#navigating-kernels-menus)
    - [Choosing Options](#choosing-options)
    - [Listing Options](#listing-options)
    - [Displaying Option Help](#displaying-option-help)
    - [Listing Secondary and Common Options](#listing-secondary-and-common-options)
    - [Displaying Option Descriptions](#displaying-option-descriptions)
    - [Jumping to Options—”Up-Arrow Jump”](#jumping-to-optionsup-arrow-jump)
    - [Jumping to Options—”Rubber-Band Jump”](#jumping-to-optionsrubber-band-jump)
    - [Common Menu](#common-menu)
  - [Menu Templates Option](#menu-templates-option)
    - [LOGIN Menu Template](#login-menu-template)
  - [Summary](#summary)
- [Menu Manager: System Management](#menu-manager-system-management)
  - [Creating Menus and Options](#creating-menus-and-options)
    - [Option Name and Menu Text](#option-name-and-menu-text)
    - [Synonyms and Display Order](#synonyms-and-display-order)
    - [PRIORITY](#priority)
    - [HELP FRAME](#help-frame)
    - [DISPLAY OPTION](#display-option)
    - [If the Option Invokes Non-VistA Applications](#if-the-option-invokes-non-vista-applications)
    - [If the Option Should Be Regularly Scheduled](#if-the-option-should-be-regularly-scheduled)
    - [Auditing Option Use](#auditing-option-use)
  - [Display Menus and Options Menu](#display-menus-and-options-menu)
    - [Diagramming Options](#diagramming-options)
    - [Option Descriptions](#option-descriptions)
    - [Displaying Options](#displaying-options)
    - [Option Access by User Option](#option-access-by-user-option)
  - [Managing Menus and Options](#managing-menus-and-options)
    - [Managing Primary Menus](#managing-primary-menus)
    - [Assigning Secondary Menus](#assigning-secondary-menus)
    - [ALWAYS SHOW SECONDARIES Field](#always-show-secondaries-field)
    - [Redefining the Common Menu](#redefining-the-common-menu)
    - [Altering Exported Menus](#altering-exported-menus)
    - [Delete Unreferenced Options Option](#delete-unreferenced-options-option)
    - [Fix Option File Pointers Option](#fix-option-file-pointers-option)
    - [Testing a User’s Menus](#testing-a-users-menus)
    - [Managing Out-Of-Order Option Sets](#managing-out-of-order-option-sets)
  - [Restricting Option Usage](#restricting-option-usage)
    - [Setting Options Out of Order](#setting-options-out-of-order)
    - [Locks](#locks)
    - [Prohibited Times](#prohibited-times)
    - [Permitted Devices](#permitted-devices)
    - [QUEUING REQUIRED Flag](#queuing-required-flag)
  - [Menu Manager Options that Should Be Scheduled](#menu-manager-options-that-should-be-scheduled)
    - [Clean Old Job Nodes in XUTL Option](#clean-old-job-nodes-in-xutl-option)
    - [Rebuilding Primary Menu Trees](#rebuilding-primary-menu-trees)
  - [Error Messages during Menu Jumping](#error-messages-during-menu-jumping)
  - [^XUTL Global: Structure and Function](#xutl-global-structure-and-function)
    - [User Stacks](#user-stacks)
    - [XQT Nodes—MENU Templates](#xqt-nodesmenu-templates)
    - [Display Nodes](#display-nodes)
    - [Jump Nodes](#jump-nodes)
  - [Menu Startup Parameter](#menu-startup-parameter)
  - [Menu Manager Variables—Troubleshooting](#menu-manager-variablestroubleshooting)
  - [Security Keys](#security-keys)
  - [Security Keys User Interface](#security-keys-user-interface)
  - [Security Keys System Management](#security-keys-system-management)
    - [Identifying Locked Options](#identifying-locked-options)
    - [Key Management](#key-management)
    - [Allocating and De-allocating Security Keys](#allocating-and-de-allocating-security-keys)
    - [Delegating Security Keys](#delegating-security-keys)
    - [Creating and Editing Security Keys](#creating-and-editing-security-keys)
    - [Deleting Security Keys](#deleting-security-keys)
    - [Reindexing All Users’ Security Keys Option](#reindexing-all-users-security-keys-option)
    - [Using Security Keys with Reverse Locks](#using-security-keys-with-reverse-locks)
    - [Security Key Delegation Levels](#security-key-delegation-levels)
- [Secure Menu Delegation](#secure-menu-delegation)
  - [User Interface: Acting as a Delegate](#user-interface-acting-as-a-delegate)
    - [Delegate’s Menu](#delegates-menu)
    - [Edit a User’s Options Option](#edit-a-users-options-option)
    - [Build a New Menu Option](#build-a-new-menu-option)
    - [Copy Everything About an Option to a New Option Option](#copy-everything-about-an-option-to-a-new-option-option)
    - [Copy One Users Menus and Keys to others Option](#copy-one-users-menus-and-keys-to-others-option)
    - [Limited File Manager Options (Build) Option](#limited-file-manager-options-build-option)
  - [System Management: Managing Delegates](#system-management-managing-delegates)
    - [Delegating Options: Select Options to be Delegated Option](#delegating-options-select-options-to-be-delegated-option)
    - [Further Delegation](#further-delegation)
    - [Options too Sensitive to Delegate](#options-too-sensitive-to-delegate)
    - [Replicate or Replace a Delegate Option](#replicate-or-replace-a-delegate-option)
    - [Remove Options Previously Delegated Option](#remove-options-previously-delegated-option)
    - [Specify Allowable New Menu Prefix Option](#specify-allowable-new-menu-prefix-option)
    - [Reports](#reports)
- [Server Options](#server-options)
  - [Server Options System Management](#server-options-system-management)
    - [What is a Server Option?](#what-is-a-server-option)
    - [What Can Server Options Do?](#what-can-server-options-do)
    - [Can Server Requests Be Denied?](#can-server-requests-be-denied)
    - [How Can the Number of Instances of a Server Option Be Controlled?](#how-can-the-number-of-instances-of-a-server-option-be-controlled)
    - [Setting Up a Server Option](#setting-up-a-server-option)
    - [Testing if a Site is Reachable: XQSPING Server Option](#testing-if-a-site-is-reachable-xqsping-server-option)
    - [Testing a Server Option: XQSCHK](#testing-a-server-option-xqschk)
    - [Errors and Warnings from the XQSCHK Server Option](#errors-and-warnings-from-the-xqschk-server-option)
- [Help Processor](#help-processor)
  - [Help Processor User Interface](#help-processor-user-interface)
    - [Help Frames in the Menu System](#help-frames-in-the-menu-system)
  - [Help Processor System Management](#help-processor-system-management)
    - [Display/Edit Help Frames Option](#displayedit-help-frames-option)
    - [List Help Frames Option](#list-help-frames-option)
    - [New/Revised Help Frames Option](#newrevised-help-frames-option)
    - [Cross Reference Help Frames Option](#cross-reference-help-frames-option)
    - [Fix Help Frame File Pointers Option—Deleting Help Frames](#fix-help-frame-file-pointers-optiondeleting-help-frames)
    - [Assigning/De-assigning Help Frame Editors](#assigningde-assigning-help-frame-editors)
    - [Disk Space Concerns](#disk-space-concerns)
    - [Creating and Editing Help Frames](#creating-and-editing-help-frames)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Menu Manager User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. Menu Manager is the Kernel module that controls the presentation of user activities (e.g., menu choices or options). Information about each user’s menu choices is stored in the Compiled Menu System (i.e., ^XUTL global) for easy and efficient access.

# Menu Manager: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel’s menu system presents menu options within VistA software in a standard fashion. Once you become familiar with using the menu system in one application, using other applications is easier, since the same rules apply.

## Navigating Kernel’s Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you successfully sign into the computer system, Menu Manager presents your primary menu options. Your primary menu is the top-level menu assigned to you by the system administrators. Most options that are available to you are available from your primary menu, or from a submenu attached to your primary menu.

The menu system prompts you with a “Select (menu name) Option:” prompt. For example, in a menu named Billing, Menu Manager would prompt you with “Select Billing Option:”. You can navigate through the menu system by responding to this prompt in different ways, which are described in this section.

You can enter question marks to see option choices and obtain online help. You can enter an option’s synonym or the first few letters of its menu text, using upper or lowercase, to select the option. You can also enter a caret (^) along with the option specification (option menu text or synonym) to jump to the destination option rather than traversing the menu pathways step-by-step.

### Choosing Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can choose an option from your current menu at the select prompt. Choosing the option launches the software application associated with the option. To choose an option, type in the first few letters of the option as it is displayed and press the \<Enter\> key. If multiple options match those first few characters you are presented with a list of matching options from which you can choose the specific option you want to run. If the option is another menu, indicated by trailing ellipses (...), it becomes the current menu, and so on down the menu pathway.

To come back up the menu pathway, press \<Enter\> at the select prompt. Each time you press \<Enter\>, Menu Manager returns you to the next higher menu level, until you reach your highest menu, the primary menu. If you press \<Enter\> at the primary menu, Menu Manager asks if you want to halt your session. If you answer YES, your Kernel session is ended.

### Listing Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you enter a menu, the items may or may *not* be displayed automatically, based on whether you have AUTO MENU turned on. The AUTO MENU feature, as described in the “Signon/Security: User Interface” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_User_Interface), is a flag that controls the menu display. If you do *not* have a setting specified for AUTO MENU, the site parameter default is used. Often, to save system resources, the site parameter can be set to disable automatic display. In this case, to display menu items, simply enter a single question mark (?), as shown in <u>Figure 1</u>:

<span id="_Ref29371576" class="anchor"></span>Figure 1: One Question Mark (?) Help—Sample User Dialog

Select Any Level Menu Option: <span class="mark">? \<Enter\></span>

First Item

Second Item

Third Item of Menu Choices ...

Fourth Item

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Any Level Menu Option:

### Displaying Option Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a lengthier description of an individual option, enter a single question mark (?), and the first few letters of the option name. If there is an extended description of the option, or a help frame describing the option, they are displayed, as shown in <u>Figure 2</u>:

<span id="_Ref67401218" class="anchor"></span>Figure 2: Using ?Option to Get Help on a Named Option—Sample User Dialog

Select User's Toolbox Option: <span class="mark">? \<Enter\></span>

Display User Characteristics

Edit User Characteristics

Electronic Signature Code Edit

Menu Templates...

Spooler Menu...

TaskMan User

User Help

Select User's Toolbox Option: <span class="mark">?DISPLAY \<Enter\></span>

'Display User Characteristics' Option name: XUUSERDISP

Display the user's name, location, and characteristics

\*\*\> Press 'RETURN' to continue, '^' to stop: <span class="mark">\<Enter\></span>

Select User's Toolbox Option:

### Listing Secondary and Common Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At any select prompt you can enter two question marks (??) to see options on the Secondary menu and SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu), as well as options available on the current branch of your menu tree.

The Secondary and Common menus contain options that you can select at any location in the menu system:

- Options on the Secondary menu are typically created by your system manager.
- Options on the Common menu are standard Kernel options available from anywhere in the menu system.
- Options on the current menu, on the other hand, can only be directly selected while that menu is the current menu.

The two-question-mark display shows the option’s synonym (a short abbreviation), if one exists. You can select an option by its synonym as well as by its full name. On the same line, it lists the option’s full name followed by the formal option name in capital letters enclosed in square brackets. (The name is the .01 field of the OPTION \[#19\] file.) It also shows any option restrictions, such as:

- Out-of-Order
- Locked
- Prohibited times

<span id="_Toc193181658" class="anchor"></span>Figure 3: Two Question Marks (??) Help—Listing Primary, Secondary, and Common Menu Options

Select Systems Manager Menu Option: <span class="mark">?? \<Enter\></span>

FM VA FileMan ... \[DIUSER\]

Core Applications ... \[XUCORE\]

Device Management ... \[XUTIO\]

\*\*\> Locked with XUPROG

Information Security Officer Menu ... \[XUSPY\]

Manage Mailman ... \[XMMGR\]

Menu Management ... \[XUMAINT\]

Operations Management ... \[XUSITEMGR\]

Programmer Options ... \[XUPROG\]

\*\*\> Locked with XUPROG

Spool Management ... \[XU-SPL-MGR\]

Taskman Management ... \[XUTM MGR\]

User Management ... \[XUSER\]

You can also select a secondary option:

OUT Equipment Checked Out to Myself \[A6A EQUIP USER\]

PAID SIGN INTO MARTINEZ VIA TELNET, TYPE DUSER \[A6A USE PAID\]

RUM Capacity Planning ... \[XTCM MAIN\]

ISC OFFICE MENU OPTIONS ... \[ISCSTAFF\]

Or a Common Option:

KNF Kernel New Features Help \[XUVERSIONEW-HELP\]

Halt \[XUHALT\]

Continue \[XUCONTINUE\]

Restart Session \[XURELOG\]

MM MailMan Menu ... \[XMUSER\]

NPI PROVIDER NPI SELF ENTRY \[XUS NPI PROVIDER SELF ENTRY\]

TBOX User's Toolbox ... \[XUSERTOOLS\]

VA View Alerts \[XQALERT\]

Time \[XUTIME\]

Where am I? \[XUSERWHERE\]

### Displaying Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering three question marks (???) at any select prompt displays option descriptions (from a WORD-PROCESSING-type field in the OPTION \[#19\] file). If entered at the select prompt for a menu within the primary tree, the top-level options are described; then you are prompted whether you want to see descriptions for Secondary or Common options.

<span id="_Toc193181659" class="anchor"></span>Figure 4: Three Question Marks (???) Help—Sample User Dialog

Select Spooler Menu Option: <span class="mark">??? \<Enter\></span>

'Allow other users access to spool documents' Option name: XU-SPL-ALLOW

This option edits the 'OTHER AUTHORIZED USERS' field of the SPOOL

DOCUMENT file to allow other users access to a spool document.

'Delete A Spool Document' Option name: XU-SPL-DELETE

\*\*\> Extended help available. Type "?Delete" to see it.

Delete a spool document from the spool document file and delete the

associated message if they are still linked.

'List Spool Documents' Option name: XU-SPL-LIST

\*\*\> Extended help available. Type "?List" to see it.

This option lists entries in the spool document file.

'Make spool document into a mail message' Option name: XU-SPL-MAIL

\*\*\> Extended help available. Type "?Make" to see it.

This option will take a spool document and post it as a mailman

message to the user's IN basket. This doesn't move the data at all

but does decrease the number of lines charged to the user.

\*\*\> Press 'RETURN' to continue, '^' to stop, or '?\[option text\]' for more

help: <span class="mark">\<Enter\></span>

'Print A Spool Document' Option name: XU-SPL-PRINT

\*\*\> Extended help available. Type "?Print" to see it.

This allows the printing of a document that has been spooled.

Shall I show you your secondary menus too? No// <span class="mark">\<Enter\></span>

Would you like to see the Common Options? No// <span class="mark">\<Enter\></span>

Select Spooler Menu Option:

You should be ready to use three question marks (???) to learn more about unfamiliar options (such as options distributed in a new software release).

### Jumping to Options—”Up-Arrow Jump”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pathways of the Primary, Secondary, and Common menus have tree-like structures. You can step up or down the pathways to reach your destination or invoke the menu system’s “Up-arrow Jump” feature as a shortcut. To jump to an option, enter a caret (^) before the option specification (the option’s menu text or synonym in upper- or lowercase letters). You only need to enter the first few characters needed to uniquely identify the option. You can use the option’s synonym to limit ambiguity, especially if the synonym is distinct from other synonyms or menu texts.

<span id="_Toc193181660" class="anchor"></span>Figure 5: Using the “Up-arrow Jump”—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">^INTRO \<Enter\></span> ductory text edit

The menu system carries out the necessary footwork to reach the desired option. If, along the way, there are pathway restrictions (such as locks or prohibited times), access to the option is denied, just as when stepping to an option. If a match is found within the primary or secondary menus, that option is executed.

![](kernel-8-0-systems-management-menu-manager-user-guide/004.png) NOTE: The menu system does *not* search the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu) if it can find a match in the primary or secondary menus.

If the menu system finds *more than one* matching option on *t*he Primary, Secondary, or Common menu tree, the menu system presents a list of matching choices. Entering a caret (^) followed by a question mark (?) displays all the options available to you.

<span id="_Toc193181661" class="anchor"></span>Figure 6: List of Choices—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">^LIST NAMES \<Enter\></span>

1 List Namespaces \[XUZ NAMESPACES\]

2 List Namespaces \[ZZ NAMESPACE LIST\]

Type '^' to stop, or choose a number from 1 to 2 :

System administrators should assign “shallow” secondary menus to facilitate menu jumping. When a jump is requested, the menu system searches all the way through the primary as well as the secondary, looking for a match. Users are inconvenienced and system resources are consumed if secondary menus are “deep” in terms of their hierarchical tree-like structure.

You may occasionally find jumping disabled; when you try to jump, you may get a message that quick access is temporarily disabled. Jumping stays disabled until the needed menu trees are rebuilt.

### Jumping to Options—”Rubber-Band Jump”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu system’s jump feature includes the ability to jump out to a destination option and then back again, something like the motion of a rubber band. The syntax for the “Rubber-band Jump” request is the use of a double caret (^^) followed by the usual option specification. For example:

<span id="_Toc193181662" class="anchor"></span>Figure 7: “Rubber-band Jump”—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">^^TASKMAN USER \<Enter\></span>

As with the single “Up-arrow Jump” (^), restrictions along the menu pathways are checked.

If you enter two carets (^^) without a following option specification/name, you are returned to the primary menu. This technique is a quick way for you to “go home” to the menu that is displayed at signon; it is called the “Go-home Jump.”

![](kernel-8-0-systems-management-menu-manager-user-guide/005.png) CAUTION: It is important to note that when you invoke the “Rubber-band Jump,” there is no attempt to protect variables that can be SET or KILLed, using Entry or Exit Actions, as you jump through the menu tree. Thus, the “Rubber-band Jump” can be inappropriate under certain circumstances, since it could cause significant alteration of your environment.

### Common Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu) is designed as a collection of options that are available to all users. The standard SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu items are:

- User’s Toolbox \[XUSERTOOLS\]: As described in the “User’s Toolbox Menu” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#User_Toolbox_Menu), the User’s Toolbox is a menu containing options that allow users to control some aspects of their computing environment.
- System Logout Options:
  - Halt \[XUHALT\]
  - Continue \[XUCONTINUE\]
  - Restart Session \[XURELOG\]

![](kernel-8-0-systems-management-menu-manager-user-guide/006.png) REF: These three options offer different ways to log out of the system as described in the “Signon/Security: User Interface” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_User_Interface).

- View Alerts \[XQALERT\]: As described in the “[Alerts](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Alerts)” and “[Signon/Security: User Interface](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_User_Interface)” sections in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_User_Interface), this option lets you process alerts.
- Time \[XUTIME\]: This option simply displays the date and time.
- Where am I? \[XUSERWHERE\]: This option lists information identifying what computer system you are signed into (such as UCI, Volume Set, Node, and Device).

#### Selecting Common Options with the Double Quote

Since SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu options (aka Common menu) are intended to be readily accessible, there is a shortcut method to reach them. While you could use an “Up-arrow Jump,” it is quicker to enter a quotation mark followed by the option specification (such as name, synonym). <u>Figure 8</u> selects the User’s Toolbox \[XUSERTOOLS\] menu from the Common menu using its synonym, TBOX:

<span id="_Ref84915269" class="anchor"></span>Figure 8: Selecting Common Options Using the Double Quote—User’s Toolbox Menu Option

Select Sample Menu Option: <span class="mark">"TBOX \<Enter\></span>

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Spooler Menu ...

TaskMan User

User Help

Select User's Toolbox Option:

## Menu Templates Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENU templates are like scripts. You can use them to execute a fixed series of options, in sequence. Tools for creating, deleting, listing, and renaming templates are options on the Menu Templates menu, part of the User’s Toolbox (TBOX) \[XUSERTOOLS\] menu:

<span id="_Toc193181664" class="anchor"></span>Figure 9: Menu Templates Option

Select Menu Templates Option: <span class="mark">? \<Enter\></span>

Create a new menu template

Delete a Menu Template

List all Menu Templates

Rename a menu template

Show all options in a Menu Template

Select Menu Templates Option:

When you create a MENU template, you are prompted for a series of options that lead to a final non-menu (that is executable) destination option. Once you choose one *non*-menu option to be executed, you can navigate to other options and choose them to be executed as well, if you wish. When you have selected each executable option to be part of the template, enter a plus sign (+) to store the sequence of options. You are asked to confirm the sequence of options in the template, and then to give the template a name.

To invoke the template, simply enter a left square bracket followed by the template name, as shown in <u>Figure 10</u>:

<span id="_Ref29303734" class="anchor"></span>Figure 10: Invoking a Template—Sample User Dialog

Select Option: <span class="mark">\[MYTEMPLATE \<Enter\></span>

Loading MYTEMPLATE...

The template then executes each option that is part of the template, in the same order as the options were selected for the template.

MENU templates are stored in the MENU TEMPLATE (#19.8) Multiple field of the NEW PERSON (#200) file, so you can use any name for MENU templates. If your MENU template points to options that are subsequently removed from the OPTION (#19) file, you receive a message that the MENU template no longer functions properly and needs to be deleted or rebuilt.

Use menu jumping (that is the “Up-arrow Jump”) when you want to jump immediately to an option. Use MENU templates when you have a series of options that you need to run in the same order repeatedly, over a time-period.

### LOGIN Menu Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beginning with Kernel 8.0, you can have a MENU template execute automatically, on your first signon of the day. If you have a MENU template named LOGIN (all uppercase), the MENU template is executed on your first signon of the day. So, if you have a series of options you execute on your first signon every day, an easy way to execute them is to create a MENU template; store the series of options in the template; and name the template LOGIN.

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you learn how to navigate Kernel’s menu tree, you can use some of Menu Manager’s additional features to help increase your productivity in the VistA computer system. These features include:

- “Up-arrow Jump”.
- “Rubber-band Jump”.
- Using three question marks (???) to obtain online option help.
- Using MENU templates as scripts.

# Menu Manager: System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menu Manager is built around options, which are entries in the OPTION (#19) file. There are several types of options:

- Menus—Options with subentries in the MENU (#10; item) Multiple field.
- Multiples—Options that point back to the OPTION (#19) file itself.
- Plugins—Options that are designed as items that plug into the MENU (#10, item) Multiple field of a menu-type option.

Kernel provides tools to create and manage menus and options.

## Creating Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181667" class="anchor"></span>Figure 11: Edit Options Option

SYSTEMS MANAGER MENU ... \[EVE\]

Menu Management ... \[XUMAINT\]

<span class="mark">Edit options</span> \[XUEDITOPT\]

One task system administrators perform frequently is defining local primary menus that are appropriate for their users. This task of menu creation is accomplished by grouping exported menus from various software applications together on a new master menu. You can use Edit options \[XUEDITOPT\], on the Menu Management \[XUMAINT\] menu, to define a new menu if READ, WRITE, and LAYGO access to the OPTION (#19) file has been granted (either through the FILE MANAGER ACCESS CODE \[#3\] field or through the File Access Security system if that is enabled). Only a few fields need to be defined, as shown in <u>Figure 12</u>. The new menu can then be assigned to a user, as described in the “Signon/Security: User Interface” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Signon_Security_User_Interface), with one of several options.

<span id="_Ref433272359" class="anchor"></span>Figure 12: Defining Local Primary Menus (System Administrators)—Sample User Dialog

Select OPTION to edit: <span class="mark">ZZSTAFF MENU \<Enter\></span>

Located in the Z (Local) namespace.

ARE YOU ADDING 'ZZSTAFF MENU' AS A NEW OPTION (THE 721ST)? <span class="mark">Y \<Enter\></span> (YES)

OPTION MENU TEXT: <span class="mark">STAFF MENU \<Enter\></span>

NAME: ZZSTAFF MENU// <span class="mark">\<Enter\></span>

MENU TEXT: Staff Menu// <span class="mark">\<Enter\></span>

PACKAGE: <span class="mark">\<Enter\></span>

OUT OF ORDER MESSAGE: <span class="mark">\<Enter\></span>

LOCK: <span class="mark">\<Enter\></span>

REVERSE/NEGATIVE LOCK: <span class="mark">\<Enter\></span>

DESCRIPTION:

1\><span class="mark">This is the primary menu for staff members.</span>

2\><span class="mark">\<Enter\></span>

EDIT Option: <span class="mark">\<Enter\></span>

TYPE: <span class="mark">MENU \<Enter\></span>

Select ITEM: <span class="mark">XUCORE \<Enter\></span> Core Applications

ARE YOU ADDING 'XUCORE' AS A NEW MENU (THE 1ST FOR THIS OPTION)? <span class="mark">Y \<Enter\></span> (YES)

MENU SYNONYM: <span class="mark">\<Enter\></span>

SYNONYM: <span class="mark">\<Enter\></span>

DISPLAY ORDER: <span class="mark">10</span>

Select ITEM: <span class="mark">XUSPY \<Enter\></span> System Security

ARE YOU ADDING 'XUSPY' AS A NEW MENU (THE 2ND FOR THIS OPTION)? <span class="mark">Y \<Enter\></span> (YES)

MENU SYNONYM: <span class="mark">\<Enter\></span>

SYNONYM: <span class="mark">\<Enter\></span>

DISPLAY ORDER: <span class="mark">20</span>

Select ITEM: <span class="mark">XT-KERMIT MENU \<Enter\></span> Kermit menu

ARE YOU ADDING 'XT-KERMIT MENU' AS A NEW MENU (THE 3RD FOR THIS OPTION)?

<span class="mark">YES \<Enter\></span> (YES)

MENU SYNONYM: <span class="mark">\<Enter\></span>

SYNONYM: <span class="mark">\<Enter\></span>

DISPLAY ORDER: <span class="mark">30 \<Enter\></span>

Select ITEM: <span class="mark">\<Enter\></span>

CREATOR: SITE,MANAGER// <span class="mark">\<Enter\></span>

HELP FRAME: <span class="mark">\<Enter\></span>

PRIORITY: <span class="mark">\<Enter\></span>

Select TIMES PROHIBITED: <span class="mark">\<Enter\></span>

Select TIME PERIOD: <span class="mark">\<Enter\></span>

RESTRICT DEVICES?: <span class="mark">\<Enter\></span>

Select PERMITTED DEVICE: <span class="mark">\<Enter\></span>

### Option Name and Menu Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By convention, the formal option name is usually entered in all capital letters. According to namespacing conventions, it *must* begin with a namespace that identifies the associated software. It is the NAME (#.01) field of the OPTION (#19) file. The menu text is what is displayed to the user at the select prompt. Like the words of a heading or title, initial capitalization is used for all words except prepositions and articles, all of which are presented in lowercase. To minimize the number of keystrokes needed to select an option, different first letters should be used for the text of each menu item. Menus should be limited to about seven items, so they all appear together on one screen. The most frequently used items should be presented first.

### Synonyms and Display Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, the items on the menu are displayed in alphabetical order by menu text. If any of the items is assigned a synonym, those items are displayed before others lacking synonyms. To facilitate menu jumping, synonyms should ideally be unique; numbers are *not* good choices for synonyms.

To customize the order of the display, each item on the menu can be assigned a Display Order. This field is an option attribute that is presented when using Edit options \[XUEDITOPT\]. When first assigning a number for the display order, you may want to use 10, 20, and 30 rather than 1, 2, and 3 to permit easier modification in the future if another item needs to be inserted.

### PRIORITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can set an option’s PRIORITY field to set a run priority for an option. Experimentation is needed to determine the effect of priority settings.

### HELP FRAME

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can specify a help frame for an option. The help frame is displayed if, at the “Select...” menu prompt, the user enters ?OPTION (where OPTION is the name of an option).

### DISPLAY OPTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If AUTO MENU (#200.06) is in effect for a user, the items on that user’s current menu are always displayed. A problem can arise when, if an option displays output and then quits, AUTO MENU’s automatic display of menu options scrolls the output off the screen. Since the AUTO MENU display usually scrolls the option’s output off the screen faster than the user can read the output, it can effectively render the option unusable. You can avoid this problem by setting the option’s DISPLAY OPTION (#11) field in the OPTION (#19) file to YES. If set to YES and the user has AUTO MENU turned on, Menu Manager prompts “Press RETURN to continue...” after the option completes, but before displaying the list of menu options. The user then has a chance to review the output before returning to their menu.

![](kernel-8-0-systems-management-menu-manager-user-guide/007.png) REF: For information on other fields in the OPTION (#19) file, including how to create options of a type other than MENU, see the [*Kernel 8.0 Developer’s Guide: Menu Manager Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.pdf).

### If the Option Invokes Non-VistA Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you create an option that invokes *non*-VistA applications (such as Class III software) include a call to the Device Handler with the code D HOME^%ZIS in the EXIT ACTION field of the OPTION (#19) file so that the required IO variables is present when leaving these options. Do the same for any other utility that is known to KILLIO variables upon exit.

### If the Option Should Be Regularly Scheduled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an option should be regularly scheduled to run through TaskMan, you *must* set its SCHEDULING RECOMMENDED (#209) field in the OPTION (#19) file to YES. You are *not* able to use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option to schedule an option unless this field is set to YES for the option.

### Auditing Option Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181669" class="anchor"></span>Figure 13: Auditing Menu Options

SYSTEM MANAGER MENU... \[EVE\]

System Security... \[XUSPY\]

Audit Features ... \[XUAUDIT MENU\]

Maintain System Audit Options ... \[XUAUDIT MAINT\]

Establish System Audit Parameters \[XUAUDIT\]

Audited Options Purge \[XUOPTPURGE\]

Audit Display ... \[XUADISP\]

Option Audit Display \[XUOPTDISP\]

You can establish an audit on options to record every time an option is used. You can do this with the Establish System Audit Parameters \[XUAUDIT\] option, which is in the Audit Features \[XUAUDIT MENU\] menu tree. Simply enter a time to initiate audit and a time to terminate audit. Then enter the specific options you want to audit (you can also choose all options).

Each time a user uses an audited option, an entry is made in the AUDIT LOG FOR OPTIONS (#19.081) file. You can display these entries using the Option Audit Display \[XUOPTDISP\] option. You can purge the AUDIT LOG FOR OPTIONS (#19.081) file with the Audited Options Purge \[XUOPTPURGE\] option.

If Kernel Toolkit is installed at your site, you can also use its Alpha/Beta Test Option Usage \[XQAB MENU\] menu to count the number of times an option is invoked.

![](kernel-8-0-systems-management-menu-manager-user-guide/008.png) REF: For more information, see the Kernel Toolkit documentation and the *Kernel Security Tools Manual*.

## Display Menus and Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181670" class="anchor"></span>Figure 14: Display Menus and Options Menu

SYSTEMS MANAGER MENU ... \[EVE\]

Menu Management ... \[XUMAINT\]

List Options by Parents and Use \[XUXREF\]

<span class="mark">Display Menus and Options</span> \[XQDISPLAY OPTIONS\]

Abbreviated Menu Diagrams \[XUUSERACC2\]

Diagram Menus \[XUUSERACC\]

Inquire \[XUINQUIRE\]

Menu Diagrams (with Entry/Exit Actions) \[XUUSERACC1\]

Print Option File \[XUPRINT\]

Kernel provides options to display and diagram menus and options on the Display Menus and Options \[XQDISPLAY OPTIONS\] menu.

### Diagramming Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To discover the menu tree roots of other software applications and how options and suboptions are related, you can use the menu diagramming options in <u>Table 1</u>:

| Menu                                    | Description                                                                                       |
|-----------------------------------------|---------------------------------------------------------------------------------------------------|
| Abbreviated Menu Diagrams               | Outlines the menu tree.                                                                           |
| Diagram Menus                           | Outlines the menu tree and shows option attributes (such as locks and prohibited times).          |
| Menu Diagrams (with Entry/Exit Actions) | Outlines the menu tree, shows option attributes, and shows entry/exit and header actions as well. |

<span id="_Ref29374279" class="anchor"></span>Table 2: Menu Manager Variables (Always Defined)

Also, the List Options by Parents and Use \[XUXREF\] option identifies which options have “no parents,” and thus, are standalone roots. It also indicates whether options are used as primary menus, secondary menus, or as regularly scheduled tasks.

### Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To learn more about the options included in a software application, you can use the Print Option File \[XUPRINT\] option (from the Display Menus and Options \[XQDISPLAY OPTIONS\] menu) to print the option description, type, and other information. This listing can be sorted by namespace. For example, to print all the VA FileMan options, you can sort from DD to DI.

### Displaying Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To display an option, use the Option Function Inquiry \[XUINQUIRE\] option:

<span id="_Toc193181672" class="anchor"></span>Figure 15: Option Function Inquiry Option—Sample User Dialog and Report

Select Display Menus and Options Option: <span class="mark">Option Function Inquire \<Enter\></span>

Which OPTIONS item to display: <span class="mark">XT-KERMIT MENU \<Enter\></span> Kermit menu

DEVICE: <span class="mark">\<Enter\></span> Network

OPTION List APR 11, 2018@12:09 PAGE 1

--------------------------------------------------------------------------------

NAME: XT-KERMIT MENU MENU TEXT: Kermit menu

TYPE: menu CREATOR: POSTMASTER

PACKAGE: KERNEL E ACTION PRESENT: YES

X ACTION PRESENT: YES

DESCRIPTION: This is the top level menu for kermit functions. It gives access to the send, receive, and edit options.

ITEM: XT-KERMIT RECEIVE SYNONYM: R

ITEM: XT-KERMIT SEND SYNONYM: S

ITEM: XT-KERMIT EDIT SYNONYM: E

EXIT ACTION: D CLEAN^XTKERM4 ENTRY ACTION: D INIT^XTKERM4

TIMESTAMP: 61180,30558 TIMESTAMP OF PRIMARY MENU: 53899,50477 UPPERCASE MENU TEXT: KERMIT MENU

Which OPTIONS item to display:

### Option Access by User Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181673" class="anchor"></span>Figure 16: Option Access by User Option

Menu Management ... \[XUMAINT\]

<span class="mark">Show Users with Selected Primary Menu</span> \[XUXREF-2\]

<span class="mark">Option Access By User</span> \[XUOPTWHO\]

Use the Show Users with Selected Primary Menu \[XUXREF-2\] menu to show which users have been assigned a particular option as a primary or secondary menu. The Option Access by User \[XUOPTWHO\] option is another cross-referencing tool.

## Managing Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Managing Primary Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When system administrators receive new software applications, existing primary menus should be modified to include the new menus. It is *not* wise to create a new primary menu for every new or unusual circumstance. This would lead to a tremendous variety of menus that would be difficult to sort out and use in the future. Primary menus can be customized with security keys.

![](kernel-8-0-systems-management-menu-manager-user-guide/009.png) REF: For more information on security keys, see the “[Security Keys](#security-keys)” section.

If there are a few menu options that require special privilege, they can be locked, and the security keys assigned to the appropriate users. In this way, a smaller number of primary menus can serve the needs of a larger number of users.

Also, while putting new master menus onto users’ secondary menus can be a quick fix, it is *not* a good idea to do this. Too many options on a user’s secondary menu can be cumbersome for the user. In addition, in the long run, it is easier for system administrators to manage access to a menu reached from a few well-defined primary menus than to manage access to a menu reached from many users’ secondary menus.

### Assigning Secondary Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An easy way to allocate menu options is to assign them to users individually as SECONDARY MENU OPTIONS (#203) Multiple field entries. Secondary options are unique for each user and are stored in a multiple in the user’s NEW PERSON (#200) file entry. Assignment of SECONDARY MENU OPTIONS should be limited to the essential few and should *not* involve deep structures with multiple levels. Instead, new primary menus should be built or existing ones modified. During menu jumping, all branches of both the primary and secondary menu trees are searched each time a jump request is received by the menu system. Greater efficiency and user convenience results if the depth of the secondary menu trees is confined.

### ALWAYS SHOW SECONDARIES Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can set the ALWAYS SHOW SECONDARIES (#200.11) field in a user’s NEW PERSON (#200) file entry. If set to YES for a user, that user always has their secondary and common options listed when options on their primary menu are listed, which occurs either by the user entering two question marks (??) at the “Select...” menu prompt, or when AUTO MENU is turned on.

### Redefining the Common Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users automatically have access to the options on the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu) by virtue of the menu system’s design. As described earlier, entering two question marks (??) at any select prompt displays the Common menu. The only way to deny access to a particular user is to lock the Common menu option with a reverse key and then allocate the security key to the same user.

![](kernel-8-0-systems-management-menu-manager-user-guide/010.png) REF: For more information on security keys, see the “[Security Keys](#security-keys)” section.

The items on the Common menu can be left as they are distributed by Kernel or modified locally as desired. For example, an item can be added to display online help about local computer access policies. This is accomplished by using Edit options to edit the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu option. The Item Multiple lists the existing menu choices; other locally namespaced options can be added.

If options are locally added to the standard SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu set, new installations of Kernel do *not* overwrite the changes. During installation, items on the local SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu are compared with the exported items. Any previously exported items that were removed by the site are *not* added back. Brand new items, however, are added and any matching items are updated. Other items that the site may have added are left in place.

### Altering Exported Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generally, exported menu structures should stay intact. If local modifications to exported menus are made, great care *must* be taken to preserve any logic that may exist in the exported structure. For example, the entry action of one option can set up key variables that are then assumed to exist when another option, one further down on the menu tree, is invoked. Although each one of a software’s options should be able to be invoked independently once the steps described in the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual* for creating and KILLing software-wide variables have been taken (according to the Programming Standards and Conventions \[SAC\]), this is *not* always the case and *cannot* be assumed.

If an option *cannot* be invoked independently, the developer can set that option’s INDEPENDENTLY INVOCABLE field to NO, as an alert that some other option or action *must* be done before the option can be called.

To give users the options associated with new software applications, system administrators should try to allocate the menus as whole entities. If dissection appears necessary, the “Internal Relations” section of the software documentation should be consulted before rearranging any of the items.

### Delete Unreferenced Options Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181674" class="anchor"></span>Figure 17: Delete Unreferenced Options Option

Programmer Options ... \<locked: XUPROG\> \[XUPROG\]

<span class="mark">Delete Unreferenced Options</span> \[XQ UNREF'D OPTIONS\]

All options for interactive use (*not* designed exclusively as queueable tasks) should normally be tied to a menu that is used as a primary menu or at least as a secondary menu. Standalone options that have no parents and are *not* menu-type options should be reviewed. They may be obsolete software options or local test options and could be candidates for deletion. Use the Delete Unreferenced Options \[XQ UNREF’D OPTIONS\] option to delete unreferenced options. It can be used to cycle through the entire OPTION (#19) file and delete *non*-menu options that are *not* referenced by other options. Deletion should obviously be done with care. Use of this option is limited to those who hold the XUPROG security key.

### Fix Option File Pointers Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181675" class="anchor"></span>Figure 18: Fix Option File Pointers Option

Menu Management ... \[XUMAINT\]

<span class="mark">Fix Option File Pointers</span> \[XQOPTFIX\]

After performing maintenance work on the OPTION (#19) file (such as deleting obsolete options that may have been items on a menu), you can use the Fix Option File Pointers \[XQOPTFIX\] option (see <u>Figure 19</u>) to remove any dangling pointers that may have been left in the Item multiple. Running this option is an alternative to having VA FileMan update the pointers each time an individual option is deleted.

<span id="_Ref85532599" class="anchor"></span>Figure 19: Fix Option File Pointers Option—Sample User Dialog

Select OPTION NAME: <span class="mark">ZZTEST3 \<Enter\></span> Test Option

NAME: ZZTEST3// <span class="mark">@</span>

SURE YOU WANT TO DELETE THE ENTIRE 'ZZTEST3' OPTION? <span class="mark">Y \<Enter\></span> (YES)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'USER' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? NO// <span class="mark">\<Enter\></span>

### Testing a User’s Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181677" class="anchor"></span>Figure 20: Switch Identities Option

User Management... \[XUSER\]

<span class="mark">Switch Identities</span> \[XUTESTUSER\]

You can test a user’s menus using the Switch Identities \[XUTESTUSER\] option. It lets you test the user’s menus and security keys. It does *not* allow you to execute any bottom-level menu options, however; it only lets you navigate menu trees. You are reminded at each prompt whose menu it is that you are testing. To exit this mode and return to your own menus, simply enter an asterisk (\*).

### Managing Out-Of-Order Option Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181678" class="anchor"></span>Figure 21: Out-Of-Order Set Management Menu Options

Menu Management ... \[XUMAINT\]

<span class="mark">Out-Of-Order Set Management...</span> \[XQOOMAIN\]

Create a Set of Options To Mark Out-Of-Order \[XQOOMAKE\]

List Defined Option Sets \[XQOOSHOW\]

Mark Option Set Out-Of-Order \[XQOOFF\]

Options in the Option File that are Out-of-Order \[XQOOSHOFIL\]

Protocols Marked Out-of-Order in Protocol File \[XQOOSHOPRO\]

Recover Deleted Option Set \[XQOOREDO\]

Remove Out-Of-Order Messages from a Set of Options \[XQOON\]

Toggle options/protocols on and off \[XQOOTOG\]

Menu Manager, starting with Kernel 8.0, provides a mechanism for defining sets of options and protocols, and a way to disable and enable access for these pre-defined option and protocol sets using options on the Out-Of-Order Set Management \[XQOOMAIN\] menu. This can be handy when you need to repeatedly disable and enable sets of options and protocols.

Use the Create a Set of Options to Mark Out-Of-Order \[XQOOMAKE\] option to define a set of options. You are prompted first to select options, and then to select protocols.

For both options and protocols, you can use the following to:

- Add a group of options to the set—Use the wildcard asterisk (\*) with or without a namespace.
- Add a range of options to a set—Use NAM1-NAM2 to add a range of options from NAM1 to NAM2 to the set, where “NAM” represents a namespace.
- Subtract/Remove a group of options from a set—Use the minus sign (that is hyphen, -) followed by a namespace.

Use the Mark Option Set Out-Of-Order \[XQOOFF\] option to disable access to a set of options. You are asked to enter the message used to place all options in the set out-of-order. The option then places the message in each option’s OUT OF ORDER MESSAGE (#2) field.

Use the Remove Out-Of-Order Messages from a Set of Options \[XQOON\] option to enable access to an option set.

To toggle the status of an individual option only, use the Toggle Options/Protocols On and Off \[XQOOTOG\] option.

Out-of-Order Option sets are stored in the ^XTMP global, with a purge date set for seven days in the future. If you place a set of options out of order, but the option set is purged from ^XTMP before you enable access to it, you can rebuild the out-of-order option set using the Recover Deleted Option Set \[XQOOREDO\] option. It asks you to specify the exact text of the message used to place the set of options out of order; it then recreates an out-of-order option set containing all options currently placed out of order with the specified message

![](kernel-8-0-systems-management-menu-manager-user-guide/011.png) NOTE: Make sure the message you specify is unique to the set of options you are re-enabling.

You can then enable access to the rebuilt option set with the Remove Out-Of-Order Messages from a Set of Options \[XQOON\] option.

To see what sets of options have been grouped in sets on the system, use the List the Defined Options Sets \[XQOOSHOW\] option. To show all options and protocols currently marked out of order, use the Options in the Option File that are Out-of-Order \[XQOOSHOFIL\] option, and the Protocols Marked Out-of-Order in Protocol File \[XQOOSHOPRO\] option.

## Restricting Option Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181679" class="anchor"></span>Figure 22: Restrict Availability of Options Option

Menu Management ... \[XUMAINT\]

<span class="mark">Restrict Availability of Options</span> \[XQRESTRICT\]

Options can be restricted in terms of when users can select them and when devices can be used to invoke them. Many of the option restrictions are included in the Restrict Availability of Options \[XQRESTRICT\] option.

### Setting Options Out of Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To completely restrict access, you can mark an option to be out-of-order. Do this by entering text in an option’s OUT OF ORDER MESSAGE (#2) field in the OPTION (#19) file. If a user attempts to invoke the option, the Out of Order Message is displayed.

### Locks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Both the normal lock and Reverse/Negative lock can be associated with options (as described in the “[Security Keys](#security-keys)” section). Also, M code can be entered in the HEADER or EXIT ACTION fields to restrict the use of an option given certain conditions.

### Prohibited Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can prohibit the use of an option at certain times during the day by assigning a set of prohibited time periods at the “Select TIMES PROHIBITED” prompt. Options scheduled to run through TaskMan will also be prohibited from running during these prohibited times.

### Permitted Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the RESTRICT DEVICES flag is set to YES, the option can only be invoked on one of the devices listed in the PERMITTED DEVICES Multiple field. Thus, the running of an option can be restricted. This flag does *not* affect the choice of devices used for the output from options. It instead controls the processing involved in the use of the option itself.

### QUEUING REQUIRED Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Edit options \[XUEDITOPT\] option, you can allow users to invoke an option but force any output to be queued outside of certain times of day, by editing the option’s QUEUING REQUIRED Multiple field. In this multiple’s TIME PERIOD (#.01) and DAY(S) FOR TIME PERIOD (#.02) fields enter the time periods and days in which you do *not* want the option’s output to be produced. During these time periods, the output of the options can only be queued. When a user requests a time for queuing, the menu system determines the next permissible day and time for output. Thus, users can invoke the option and use it to define the parameters for the subsequent processing, but the actual work is done during a later time-period, presumably when the system is less busy.

## Menu Manager Options that Should Be Scheduled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the two Menu Manager options that should be regularly scheduled.

Kernel exports other options that should be scheduled to run at regular intervals. Most of these are located on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu.

![](kernel-8-0-systems-management-menu-manager-user-guide/012.png) REF: For a complete list, along with suggested scheduling frequencies, see the *Kernel Installation Guide*.

### Clean Old Job Nodes in XUTL Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clean old Job Nodes in the XUTL \[XQ XUTL \$J NODES\] option is Kernel’s purge option for Kernel globals. This option purges the following globals:

- ^XUTL
- ^UTILITY
- ^TMP
- ^XTMP
- ^XUSEC

<span id="_Toc193181680" class="anchor"></span>

Figure 23: Clean old Job Nodes in XUTL Option

Operations Management ... \[XUSITEMGR\]

Clean old Job Nodes in XUTL \[XQ XUTL \$J NODES\]

User stacks for each user’s job are stored in the ^XUTL global.

![](kernel-8-0-systems-management-menu-manager-user-guide/013.png) REF: For more information, see the “[^XUTL Global: Structure and Function](#xutl-global-structure-and-function)” section.

This is also called the compiled menu system. If a job ends abnormally (such as upon error, UCI switching, or developer exits that bypass ^XUS), the entries remain in the global (this explains why developers are advised to halt out of Programmer mode with D ^XUSCLEAN rather than simply halting.)

The purge routine sets a purge date of seven days in the past. Any user stack in ^XUTL older than seven days is purged. Any entries with a matching \$J at the top level of ^UTILITY and ^TMP are also KILLed.

Next, after cleaning out the user stacks in ^XUTL, the purge routine checks ^UTILITY and ^TMP. Any entry at subscript (\$J) or (namespace, \$J) that does *not* have a matching entry in the user stacks in ^XUTL is KILLed.

Next, the purge routine checks ^XTMP. Any entry in ^XTMP at subscript (namespace) lacking a header node at (namespace,0), or with a purge date in the header node less than the purge date determined by the purge routine is KILLed.

Finally, the purge routine goes through the signon nodes stored at ^XUSEC(0,“CUR”,DUZ,DATE). Any nodes older than the purge date are KILLed.

The XQ XUTL \$J NODES option should be queued to run on a regular basis. If separate copies of the ^XUTL global are maintained on different CPUs, separate entries should be made in the OPTION SCHEDULING (#19.2) file for each CPU, so that a separate job purges each CPU’s XUTL global. Because this option deletes any user stacks that are time-stamped with a date earlier than the purge date determined by this option (seven days) you need to take care how frequently you schedule it (in the unusual event of a seven-day long job, this option should obviously *not* be run).

### Rebuilding Primary Menu Trees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181681" class="anchor"></span>Figure 24: Building Primary Menu Trees Options

PARENT OF QUEUABLE OPTIONS \[ZTMQUEUABLE OPTIONS\]

Non-interactive Build Primary Menu Trees \[XQBUILDTREEQUE\]

Menu Management ... \[XUMAINT\]

Build Primary Menu Trees \[XQBUILDTREE\]

The menu system uses local menu trees to process requests. When changes are made to the menu structure, the local menu trees are rebuilt (a process also known as microsurgery). If a user attempts an “Up-arrow Jump” when the local trees need to be rebuilt or are being rebuilt, a message is issued about quick access being temporarily disabled; the user is *not* able to jump to reach the option. Microsurgery is triggered in the following situations:

- The Edit options \[XUEDITOPT\] option is used.
- An Out-of-Order option set is enabled or disabled.
- A sufficiently large number of changes have been made to a menu tree.

It is also *recommended* to rebuild all primary menu trees every other day during non-peak hours, using the XQBUILDTREEQUE option. If separate copies of ^XUTL are maintained on different CPUs, separate entries should be made in the OPTION SCHEDULING (#19.2) file for each CPU so that a separate job rebuilds each CPU’s ^XUTL global.

Primary menu trees can also be built/repaired immediately using the Build Primary Menu Trees \[XQBUILDTREE\] option. If menu jumping has stopped working and microsurgery is *not* fixing the menus, use the Build Primary Menu Trees \[XQBUILDTREE\] option to force a menu rebuild to fix the problem.

## Error Messages during Menu Jumping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are some conditions under which a menu jump may *not* be completed. In these cases, the user sees one of the following error messages (<u>Figure 25</u> to <u>Figure 30</u>):

<span id="_Ref29290616" class="anchor"></span>Figure 25: Menu Jump Error Message (1 of 6)

I NEED TO REBUILD MENUS .... QUICK ACCESS IS TEMPORARILY DISABLED Please proceed to {target option's menu text}

This means that the time stamps on the OPTION (#19) file and the ^XUTL global indicate that the OPTION (#19) file has been modified since the menus were compiled in ^XUTL and the global is therefore locked until XQ8 can recompile the modified menus. This error message can be generated by both user-generated jumps and phantom jumps.

<span id="_Toc193181683" class="anchor"></span>Figure 26: Menu Jump Error Message (2 of 6)

\*\*\* WARNING \*\*\*

Illegal jump requested to option '{option's menu text}' Jump pathway locked at option '{locked option's menu text}'

This indicates that a locked option for which the user does *not* possess the security key has been encountered in the tree between the option where the jump was requested and the target option to which the jump was requested. This error message can be generated by both user-generated jumps and phantom jumps.

<span id="_Toc193181684" class="anchor"></span>Figure 27: Menu Jump Error Message (3 of 6)

\*\*\* WARNING \*\*\*

Illegal jump was requested to option '{option menu text}' Jump path out of order from '{option's menu text}' with message '{out of order message}'

This means that an option on the tree between the option where the phantom jump was requested, and the target option has been marked as out of order (OUT OF ORDER MESSAGE \[#2\] Field of the OPTION \[#19\] file). This error message can be generated by both user-generated jumps and phantom jumps.

<span id="_Toc193181685" class="anchor"></span>Figure 28: Menu Jump Error Message (4 of 6)

\*\*\* WARNING \*\*\*

Illegal jump was requested to option '{option menu text}' Variable XQUIT encountered at option '{option name}'

This means that the jump logic has encountered the variable XQUIT (detected with a \$DATA statement). This variable is usually set by an Entry Action (Field \#20 of the OPTION \[#19\] file) and causes the menu system to refuse to run or jump past that option. This error message can be generated by both user-generated jumps and phantom jumps.

<span id="_Toc193181686" class="anchor"></span>Figure 29: Menu Jump Error Message (5 of 6)

\*\*\* WARNING \*\*\*

Background jump requested to option '{value in XQMM("J")}' but this option does not exist on your system.

A VA FileMan lookup was attempted for the option set in the variable XQMM(“J”), but no such option was found in the OPTION (#19) file. This error message can only be generated from a phantom jump.

<span id="_Ref29290648" class="anchor"></span>Figure 30: Menu Jump Error Message (6 of 6)

\*\*\* WARNING \*\*\*

Background jump requested to option '{option's menu text}' but you do not have access to this option. See your computer representative.

This means that the target option requested by XQMM(“J”)is *not* in the tree of options to which this user has access (that is, the target option was neither in the user’s primary menu tree nor specifically listed as a secondary menu for that user). This error message can only be generated from a phantom jump.

![](kernel-8-0-systems-management-menu-manager-user-guide/014.png) REF: For more information on phantom jumps, see the [*Kernel 8.0 Developer’s Guide: Menu Manager Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.pdf).

## ^XUTL Global: Structure and Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^XUTL global is an account-specific global. It should exist in each Production account on your system. This global is created primarily from information in the OPTION file \[ ^DIC(19) \] and is therefore sometimes referred to as “the compiled menu system.”

^XUTL is divided into three main sections:

- User Stacks^XUTL(“XQ”,\$J)^XUTL(“XQT”,\$J) (MENU templates only)
- Display Nodes^XUTL(“XQO”,ien)
- Jump Nodes^XUTL(“XQO”,“P”\_ien)

### User Stacks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User stacks are stored in nodes in ^XUTL(“XQ”,\$J) and ^XUTL(“XQT”,\$J).

The example illustrated in [Figure 111](#_Ref84826843) shows a typical user stack. In this case the \$J is 541065826.

The “XQ” nodes can be divided into meaningful sets according to what is contained in the third subscript. The numeric third subscripts begin with the Zero node, which is set to the date and time in VA FileMan format by the program ^XUS1 when the user logs on or ^%XUCI when the user is changing UCIs.

The other numeric, third subscripts (in this case the numbers 1 to 3) reflect the user’s progression through the menu system.

Each time a new option is invoked, a new node is created that contains the following:

- Option number, concatenated with a P.
- Number of the option whose compiled menu tree contains the current option.
- A caret (^).
- Zero-node of the OPTION (#19) file for that option.

A different format is used for options in a user’s secondary menu tree.

A pointer in the node ^XUTL(“XQ”, \$J, “T”) indicates which option in this list of numbered nodes the menu driver is currently using. This pointer is set and reset by the menu driver as the user moves up and down the menu tree. In the example, XUPROGMODE is the option that the menu driver is currently using.

Other “XQ” nodes of the global that have a non-numeric third subscript are used to store various pieces of Kernel information that are set up at signon. ^XUTL(“XQ”,\$J,“XQM”) points to the user’s primary menu.

In the example in <u>Figure 31</u>, the user’s primary menu is OPTION (#19) file entry \#29.

<span id="_Ref84826843" class="anchor"></span>Figure 31: User Stack Example

^XUTL("XQ",541065826,0) = 2920113.081624

^XUTL("XQ",541065826,1) = 29P29^EVE^Systems Manager

Menu^^M^.5^^192^^^^^^n^1^^^

^XUTL("XQ",541065826,2) = 31P29^XUPROG^Programmer Options^^M^^

XUPROG^^^^^^^n^^

^XUTL("XQ",541065826,3) = 49P29^XUPROGMODE^Programmer mode^^R

^^XUPROGMODE^^^^^^^ n^^

^XUTL("XQ",541065826,"DUZ") = 63

^XUTL("XQ",541065826,"DUZ(0)") = LlPp

^XUTL("XQ",541065826,"DUZ(2)") = 16000

^XUTL("XQ",541065826,"IO") = \_TNA5103:

^XUTL("XQ",541065826,"IOBS") = \$C(8)

^XUTL("XQ",541065826,"IOF") = \#,\$C(27,91,50,74,27,91,72)

^XUTL("XQ",541065826,"ION") = LAT DEVICE

^XUTL("XQ",541065826,"IOS") = 158

^XUTL("XQ",541065826,"IOSL") = 24

^XUTL("XQ",541065826,"IOST") = C-VT100HIGH

^XUTL("XQ",541065826,"IOST(0)") = 149

^XUTL("XQ",541065826,"IOT") = VTRM

^XUTL("XQ",541065826,"IOXY") = W \$C(27,91)\_((DY+1))\_\$C(59)\_((DX+1))\_\$C(72)

^XUTL("XQ",541065826,"T") = 3

^XUTL("XQ",541065826,"XQM") = 29

### XQT Nodes—MENU Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “XQT” nodes are used to create a stack of options like the “XQ” stack when a MENU template is invoked. These nodes are translated from the ^VA(200,DUZ,19.8) Multiple when a user precedes an option selection with a left square bracket character, “\[”, much like a PRINT template is invoked in VA FileMan. For example, if the user has defined a MENU template named “DOIT” using the Menu Template menu options of the User’s Tool Box, typing “\[DOIT” loads that sequence of options into the “XQT” nodes and begins executing them. When a MENU template is requested by the user, the option tree of that template is loaded into the “XQT” nodes and remains loaded if the user is logged on. Further requests for “\[DOIT” uses that same stack.

### Display Nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display nodes are stored in ^XUTL(“XQO”, internal number).

The first example in [Figure 112](#_Ref84826444) shows the display nodes for EVE, the System Manager’s Menu. The internal number of EVE in this OPTION (#19) file is 29. In the first part of the example the option names and menu texts, along with a limited number of fields for that option compiled from the OPTION (#19) file, are concatenated together. It is from this part that XQ2 (the menu display program) gets the information it needs.

In the second part, all the menu texts and synonyms are listed in order in uppercase. It is here that XQ tries to match what the user entered at the terminal with the correct option. The third part of the example, the 0th node of the options, is listed by number and provides the remaining information that the Menu System may need to make the option work. To understand what the various ^ pieces mean, look at a VA FileMan global format data dictionary listing of the OPTION (#19) file.

Illustrated in the second example in <u>Figure 33</u> is the display node for the SECONDARY MENU OPTIONS of a user whose DUZ is equal to 66. Here, the user has only a single secondary menu called “Secondary Menu” (with an internal number of 580 in the OPTION \[#19\] file). The various parts of this example are identical to those of the Display Nodes for the EVE menu example (<u>Figure 32</u>).

![](kernel-8-0-systems-management-menu-manager-user-guide/015.png) NOTE: The second subscript, instead of pointing to a menu in the OPTION (#19) file, is a “U” concatenated with the user’s DUZ which points to the NEW PERSON (#200) file entry. This is because secondary menu options are stored in the SECONDARY MENU OPTIONS (#203) Multiple field in the NEW PERSON (#200) file entry for each user.

<span id="_Ref84826444" class="anchor"></span>Figure 32: Display Nodes for EVE Example

^XUTL("XQO",29,0) = 2^55048,38923

^XUTL("XQO",29,0,1) = ^XUCORE^Core Applications ...^NOT

AVAILABLE^^^^^^XUTIO^Device Handler

...^^^^n^^FM^DIUSER^VA FileMan ...^^^^n^^^XMMGR^

Manage Mailman ...^^^^^^^XUMAINT^Menu Management

...^^^^n^^^XUPROG^Programmer Options ...^^XUPROG^^^

...^

^XUTL("XQO",29,0,2) = ^XUSITEMGR^Operations Management ...^^^^^^^XU-SPL-MGR

^Spool Management ...^^^^^^^XUSPY^System Security

...^^^^^^^ZTMMGR^Task Manager ...^^^^n^^^XUSER^User

Edit ...^^^^^^

^XUTL("XQO",29,"CORE APPLICATIONS") = 40^1

^XUTL("XQO",29,"DEVICE HANDLER") = 32^1

^XUTL("XQO",29,"FM") = 19^0

^XUTL("XQO",29,"MANAGE MAILMAN") = 30^1

^XUTL("XQO",29,"MENU MANAGEMENT") = 9^1

^XUTL("XQO",29,"OPERATIONS MANAGEMENT") = 174^1

^XUTL("XQO",29,"PROGRAMMER OPTIONS") = 31^1

^XUTL("XQO",29,"SPOOL MANAGEMENT") = 415^1

^XUTL("XQO",29,"SYSTEM SECURITY") = 226^1

^XUTL("XQO",29,"TASK MANAGER") = 83^1

^XUTL("XQO",29,"USER EDIT") = 39^1

^XUTL("XQO",29,"VA FILEMAN") = 19^1

^XUTL("XQO",29,"^",9) = ^XUMAINT^Menu Management^^M^^^105^^^n^n^^n^^^^

^XUTL("XQO",29,"^",19) = FM^DIUSER^VA FileMan^^M^^^^^^n^^^n^1^^

^XUTL("XQO",29,"^",30) = ^XMMGR^Manage Mailman^^M^^^299^^^^^54^^1^1^^^

^XUTL("XQO",29,""^",31) = ^XUPROG^Programmer Options^^M^^XUPROG^^^^^^^n^^

^XUTL("XQO",29,"^",32) = ^XUTIO^Device Handler^^M^^^413^^^n^^20^n^^

^XUTL("XQO",29,"^",39) = ^XUSER^User Edit^^M^^^153^^^^^^n^^

^XUTL("XQO",29,"^",40) = ^XUCORE^Core Applications^1^M^^^^^^^^^n^^

^XUTL("XQO",29,"^",83) = ^ZTMMGR^Task Manager^^M^^^^^^n^^50^^1^^

^XUTL("XQO",29,"^",174) = ^XUSITEMGR^Operations Management^^M^^^^^^^y^^n^^

^XUTL("XQO",29,"^",226) = ^XUSPY^System Security^^M^^^^^^^^119^n^^

^XUTL("XQO",29,"^",415) = ^XU-SPL-MGR^Spool Management^^M^^^419^^^^^20^^

<span id="_Ref84825452" class="anchor"></span>Figure 33: Display Nodes for a Secondary Menu

^XUTL("XQO","U66",0) = 1^54927,30758

^XUTL("XQO","U66",0,1) = ^ZZTSTSM^Secondary Menu ...^^^^n^^

^XUTL("XQO","U66","SECONDARY MENU") = 580^1

^XUTL("XQO","U66","^",580) = ^ZZTSTSM^Secondary Menu^^M^^^^^^n^^^^1^1^^1

### Jump Nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Jump nodes are stored in ^XUTL(“XQO”,“P”\_internal number), where there is one “P\_...” entry in ^XUTL(“XQO”) for each primary menu that exists. The jump nodes, for each primary menu, store the pathways to all options that can be jumped to.

The jump nodes are created in the XQ8\* series of programs. They are very similar to display nodes, except that:

- They have a P concatenated on the front of the primary option’s number in the second subscript.
- These nodes describe the entire primary menu tree rather than just the single level tree.

Examples of the jump nodes for a single primary menu are shown in <u>Figure 34</u> and <u>Figure 35</u>. Since these nodes can be very extensive in number, some nodes have been removed from the examples to save space.

In the first example (<u>Figure 34</u>) are the “lookup” nodes, where the jump software tries to match a menu text or synonym with what the user has entered at the terminal. Each node is set to its internal number in the OPTION (#19) file and, in the second ^ piece, a:

- 0—If it is a synonym.
- 1—If it is menu text.

In the second example (<u>Figure 35</u>), the “menu pathway” entries below the “P580” node show all the options that can be jumped to from the primary menu whose internal entry number (IEN) is 580. Each entry contains lists of the series of options that *must* be navigated through in a jump from the primary menu. In the case of the option DILIST (# 17), the list of options that must be processed is 520,519,518,411,17. If, as in the case of ZZTEST4 (# 318), there is more than one possible pathway, then each is listed along with various other necessary pieces of information (such as locks, time restraint, and so on).

<span id="_Ref84825176" class="anchor"></span>Figure 34: Jump Nodes Example—Lookup Nodes

^XUTL("XQO","P580",0) = 55165,28536

^XUTL("XQO","P580","19^") = 394^0

^XUTL("XQO","P580","2ND SECOND LEVEL MENU TEST^") = 575^1

^XUTL("XQO","P580","3^") = 518^0

^XUTL("XQO","P580","ACTN^") = 391^0

^XUTL("XQO","P580","ALL^") = 420^0

<span id="_Ref84825186" class="anchor"></span>Figure 35: Jump Nodes Example—Menu Pathways

^XUTL("XQO","P580","LIST FILE ATTRIBUTES^") = 17^1

^XUTL("XQO","P580","TEST 4^") = 318^1

...

^XUTL("XQO","P580","TOOL^") = 581^0

^XUTL("XQO","P580","X-TYPE OPTION TEST^") = 576^1

^XUTL("XQO","P580","X^") = 576^0

^XUTL("XQO","P580","ZDAVE^") = 411^1

^XUTL("XQO","P580","^",5) = ^XUEDITOPT^Edit

options^^E^581,5,^^106^^^^^20^n^^^^

^XUTL("XQO","P580","^",17) = ^DILIST^List File Attributes^^A^

520,519,518,411,17,^^^^^n,^y^^n^1^^^

...

^XUTL("XQO","P580","^",318) = ^ZZTEST4^Test

4^^O^520,575,397,318,^^^^^n,^^^^^^

^XUTL("XQO","P580","^",318,0) = 2

^XUTL("XQO","P580","^",318,0,1) = 520,575,578,397,318,^^^n,^

^XUTL("XQO","P580","^",318,0,2) = 520,575,578,318,^^^n,^

...

^XUTL("XQO","P580","^",579) = ^ZZLEVEL3B^Phantom

Mother^^M^520,575,579,^^^^^n,^^^^1^1^^1

^XUTL("XQO","P580","^",580) = ^ZZTSTPM^Primary Menu^^M^^^^^^n^^^^1^1^^1

^XUTL("XQO","P580","^",581) = ^ZZLUKTOOLS^Luke's

Tools^^M^581,^^^^^^^^^1^1^^1

## Menu Startup Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XQ MENUMANAGER PROMPT parameter is checked during menu startup. It allows sites to change the default \<TEST ACCOUNT\> prompt to another value (such as \<LEGACY SYSTEM\>) in menu prompts of *non*-Production VistA systems. The text defined by this parameter is inserted in the Menu Manager prompts. If no text is defined, the hard-coded default is “ \<TEST ACCOUNT\>”. Alternatives could be:

- “ \<LEGACY SYSTEM\>
- “ \<CONTINGENCY\>”
- “ \<READ ONLY\>”
- Any other value from 3 to 20 characters, depending upon the purpose of the *non*-Production VistA system.

To change the value on a *non*-Production system, use the General Parameter Tools \[XPAR MENU TOOLS\] option and select “EP Edit Parameter Values.” You must log off and log back into VistA to see the changed menu prompt.

![](kernel-8-0-systems-management-menu-manager-user-guide/016.png) NOTE: The prompt can be set in advance on a Production system before it is mirrored to a *non*-Production system, and the prompt only appears on the *non*-Production system.

![](kernel-8-0-systems-management-menu-manager-user-guide/017.png) NOTE: The XQ MENUMANAGER PROMPT parameter was released with Kernel Patch XU\*8.0\*614.

## Menu Manager Variables—Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the Menu Manager variables that are always defined. It may be useful for system administrators to know what these variables signify when investigating errors. If an error is reported in VA FileMan’s DIP routine, for example, knowing the value of XQY at the time of the error indicates which option was invoking the DIP routine. The option can then be reviewed to discover the name of the routine that was calling DIP.

<table>
<caption><p><span id="_Toc207462696" class="anchor"></span>Table 3: Secure Menu Delegation Menu Options</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XQABTST</strong></td>
<td>Flag that signals whether alpha-beta testing is in effect.</td>
</tr>
<tr class="even">
<td><strong>XQDIC</strong></td>
<td><p>Internal entry number (IEN) of the option’s parent (which <em>must</em> be a menu) in the OPTION (#19) file, if an option is executing. If the user is in a menu, <strong>XQDIC</strong> is set to the IEN of the current menu’s parent (unless they are in their primary menu, in which case <strong>XQDIC</strong> is set to the IEN of the primary menu).</p>
<p>The value of <strong>XQDIC</strong> also corresponds to the second subscript in the display nodes portion of the <strong>^XUTL</strong> global, <strong>^XUTL(“XQO”,)</strong> for the menu in question.</p></td>
</tr>
<tr class="odd">
<td><strong>XQPSM</strong></td>
<td>Like <strong>XQDIC</strong>, a lookup value into the second subscript of <strong>^XUTL</strong>, the compiled menu global. <strong>XQPSM</strong> points to the tree of the target option in the jump. It resulted from the ability to jump to any option, <em>not</em> just ones on the primary menu tree. It can help identify jumps from a primary, secondary, or Common option.</td>
</tr>
<tr class="even">
<td><strong>XQT</strong></td>
<td>Current option’s type (such as <strong>M</strong> for menu, <strong>A</strong> for action).</td>
</tr>
<tr class="odd">
<td><strong>XQUR</strong></td>
<td>User’s response to the menu prompt (replaces <strong>A</strong>).</td>
</tr>
<tr class="even">
<td><strong>XQUSER</strong></td>
<td>User’s name in the form <strong>SEVEN A. XUUSER</strong>.</td>
</tr>
<tr class="odd">
<td><strong>XQY</strong></td>
<td>Internal entry number (IEN) of the current option or menu (replaces <strong>Y</strong>).</td>
</tr>
<tr class="even">
<td><strong>XQY0</strong></td>
<td>First node (subscript of <strong>Zero</strong>) of the current option [replaces <strong>Y(0)</strong>].</td>
</tr>
<tr class="odd">
<td><strong>XQXFLG</strong></td>
<td>Contains several flags, including whether capacity management testing is active.</td>
</tr>
</tbody>
</table>

<span id="_Toc207462696" class="anchor"></span>Table 3: Secure Menu Delegation Menu Options

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Keys User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security keys are primarily used to allow access to specially protected options. If a software application exports a menu that has one or two options that require a secured level of access, they can use security keys to lock those special options. When an option is locked, you can only use the locked option if you hold the security key matching the key with which the option was locked.

Entering two question marks (??) at the menu system’s select prompt displays the current options. If any of the options are locked, that fact is listed also, along with the names of any associated security keys. In the example in <u>Figure 36</u>, the option Programmer Options is locked with the XUPROG security key:

<span id="_Ref26360814" class="anchor"></span>Figure 36: Sample Locked Menu Options Showing Required Security Key—Entering Two Question Marks (??)

Select Systems Manager Menu Option: <span class="mark">?? \<Enter\></span>

Device Handler ... \[XUTIO\]

Menu Management ... \[XUMAINT\]

Programmer Options ... \[XUPROG\]

\*\*\> Locked with XUPROG

You can list which security keys you currently hold by using the Display User Characteristics \[XUUSERDISP\] option on the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu). It displays a list of all security keys you hold, like <u>Figure 37</u>:

<span id="_Ref511215267" class="anchor"></span>Figure 37: Display User Characteristics Option—Sample Output

KEYS HELD

---------

XUPROG XUMGR XUPROGMODE XUAUTHOR ZTMQ

The security keys you need to carry out computing activities should be assigned by system administrators when your computer account is first added to the system. Other keys can be allocated later by system administrators or designee (such as an application coordinator) with the use of the Secure Menu Delegation menu utilities.

## Security Keys System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Identifying Locked Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System administrators can list which security keys lock what options by using the Diagram Menus \[XUUSERACC\] option, which is located on the Display Menus and Options \[XQDISPLAY OPTIONS\] menu under the Menu Management \[XUMAINT\] menu. <u>Figure 38</u> shows that the Programmer Options \[XUPROG\] menu is locked with the XUPROG security key. It also shows that one of its options, Programmer mode \[XUPROGMODE\], is locked with the XUPROGMODE security key:

<span id="_Ref84823269" class="anchor"></span>Figure 38: Diagram Menus Option—Sample User Dialog

Select Menu Management Option: <span class="mark">DIAGRAM MENUS \<Enter\></span>

Select USER (U.xxxxx) or OPTION (O.xxxxx) name: <span class="mark">O.XUPROG \<Enter\></span>

Programmer Options (XUPROG)

\*\*<span class="mark">LOCKED: XUPROG</span>\*\*

--------------------------PG Programmer mode

\[XUPROGMODE\]

\*\*<span class="mark">LOCKED: XUPROGMODE</span>\*\*

Security keys are stored in the SECURITY KEY (#19.1) file. Security keys given to users are stored in the users’ NEW PERSON (#200) file entries, in the KEYS Multiple field.

Options are locked by a given security key when the name of that key is entered into the LOCK (#3) field of the OPTION (#19) file. If an option is locked, users need to be given the security key to invoke the option.

### Key Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keys are defined and allocated to users with options on the Key Management \[XUKEYMGMT\] menu, as shown in <u>Figure 39</u>:

<span id="_Ref511395287" class="anchor"></span>Figure 39: Key Management Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Menu Management ... \[XUMAINT\]

Key Management ... \[XUKEYMGMT\]

<span class="mark">Allocation of Security Keys</span> \[XUKEYALL\]

De-allocation of Security Keys \[XUKEYDEALL\]

Enter/Edit of Security Keys \[XUKEYEDIT\]

All the keys a user needs \[XQLOCK1\]

Change user's allocated keys to delegated keys \[XQKEYALTODEL\]

Keys for a given menu tree \[XQLOCK2\]

Delegate keys \[XQKEYDEL\]

List users holding a certain key \[XQSHOKEY\]

Remove delegated keys \[XQKEYRDEL\]

Show the keys of a particular user \[XQLISTKEY\]

### Allocating and De-allocating Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main option to assign security keys to a user or users is the Allocation of Security Keys \[XUKEYALL\] option. Allocating a security key to a user lets them invoke options that are locked with the key. For options with reverse locks, allocating the security key locks the user out from the option. In either case, allocating the key to a user does *not* allow the user to give the key to anyone else.

![](kernel-8-0-systems-management-menu-manager-user-guide/018.png) REF: For more information on reverse locks, see the “[Using Security Keys with Reverse Locks](#using-security-keys-with-reverse-locks)” section.

![](kernel-8-0-systems-management-menu-manager-user-guide/019.png) NOTE: The PSDRPH security key *cannot* be allocated using this option, the Allocate/De-Allocate of PSDRPH Key(Audited) \[PSO EPCS PSDRPH KEY\] option *must* be used to allocate this security key.  
  
REF: For mor einformation on the Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option, see the “Allocate/De-Allocate of PSDRPH Key Option” section in the [*Kernel Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf#Allocate_DeAllocate_PSDRPH_Key_Option).

To remove a security key from a user, use the De-allocation of Security Keys \[XUKEYDEALL\] option.

Unless you have been delegated a security key, the only way you can allocate or de-allocate keys is if you hold the XUMGR security key or have a FILE MANAGER ACCESS CODE (#3) field of @.

![](kernel-8-0-systems-management-menu-manager-user-guide/020.png) REF: For more information on delegating security keys, see the “[Delegating Security Keys](#delegating-security-keys)” section.

![](kernel-8-0-systems-management-menu-manager-user-guide/021.png) NOTE: The PSDRPH security key *cannot* be de-allocated using this option, the Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option *must* be used to de-allocate this security key.  
  
REF: For more information on the Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option, see the “Allocate/De-Allocate of PSDRPH Key Option” section in the [*Kernel Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf#Allocate_DeAllocate_PSDRPH_Key_Option).

All the security keys that a new user needs to use their assigned options can be determined by using the All the Keys a User Needs \[XQLOCK1\] option on the Key Management \[XUKEYMGMT\] menu. This produces a list of the primary and secondary menus for that user and compiles a list of the keys for that menu tree. This list can then be assigned or delegated. It can also be edited before the keys are given to the user. Similarly, the Keys For a Given Menu Tree \[XQLOCK2\] option examines a menu and lists all the security keys associated with all sibling options.

### Delegating Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delegating keys allows you to give a user the ability to assign specific security keys to other users, as opposed to the XUMGR security key and @ VA FileMan Access Code (that is FILE MANAGER ACCESS CODE \[#3\] field), which allow all keys to be assigned.

One way to delegate security keys is to use the Change user’s allocated keys to delegated keys \[XQKEYALTODEL\] option. This option delegates to a user all the security keys that are currently allocated to that user. Any entries in their KEYS Multiple field are entered in the DELEGATED KEYS Multiple field as well. They can now use the Allocation of Security Keys \[XUKEYALL\] option to give the security keys to others.

Alternatively, system administrators can use the Delegate keys \[XQKEYDEL\] option to populate the DELEGATED KEYS Multiple field one-by-one.

A user who has been delegated a security key can allocate that key to others in two ways:

- Through the Allocation of Security Keys \[XUKEYALL\] option, if it is on their menu.
- By delegating an option locked by the security key in question; the key is allocated along with the option.

The key recipients (excepting holders of the XUMGR security key or a FILE MANAGER ACCESS CODE \[#3\] field of @) *cannot* assign the security key to others, however, even if they have access to the Allocation of Security Keys \[XUKEYALL\] option, because the key does *not* exist in their DELEGATED KEYS Multiple field.

One example of key delegation is a system administrator designee, delegated the Provider key, who allocates that key to incoming medical residents.

For security reasons, users who have a key in their DELEGATED KEYS Multiple field *cannot* allocate that key to themselves. That key *must* be awarded by another user who has been delegated the key or by a system administrator who holds the XUMGR system security key.

### Creating and Editing Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keys can be created using the Enter/Edit of Security Keys \[XUKEYEDIT\] option on the Key Management \[XUKEYMGMT\] menu. If a security key has already been defined, its name *cannot* be edited. It also *cannot* be deleted, as discussed below. Other key attributes stored in the SECURITY KEY (#19.1) file can be used for special purposes. Attributes of the PROVIDER security key are shown in the example in <u>Figure 40</u>:

<span id="_Ref26360855" class="anchor"></span>Figure 40: Attributes for the Provider Security Key—Sample User Dialog

Select SECURITY KEY NAME: <span class="mark">PROVIDER \<Enter\></span>

NAME: PROVIDER// <span class="mark">\<Enter\></span>

DESCRIPTIVE NAME: Provider// <span class="mark">\<Enter\></span>

PERSON LOOKUP: LOOKUP// <span class="mark">\<Enter\></span>

KEEP AT TERMINATE: YES// <span class="mark">\<Enter\></span>

DESCRIPTION:

1\>This KEY is given to all entries in the New Person file that need

2\>to be looked up as a Provider. Those entries that hold this key

3\>are considered to be providers. It was given to all active

4\>Providers in file 6 at the time of the Kernel 7 install.

EDIT Option: <span class="mark">\<Enter\></span>

Select SUBORDINATE KEY: <span class="mark">\<Enter\></span>

GRANTING CONDITION: <span class="mark">\<Enter\></span>

#### PERSON LOOKUP

As described in the [*Kernel 8.0 Developer’s Guide: Security Keys Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_security_keys_ug.pdf), a special AK cross-reference on the NEW PERSON (#200) file is maintained automatically for anyone who is granted a security key that is flagged for Person Lookup. This cross-reference has been introduced to facilitate identification of user groups, like providers.

#### KEEP AT TERMINATE

As described in the “Deactivating Users” section in the [*Kernel Systems Management: Signon/Security User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf#Deactivating_Users), security keys that are marked as “KEEP AT TERMINATE” are *not* removed as a user attribute of terminated users. This allows the continued processing of activities that had been previously authorized (such as for billing purposes, notes, pending orders, or other actions), because the user held the security key.

For example, the PROVIDER security key KEEP AT TERMINATE field is set to YES in case a medical order continues to hold an approved status, even though the authorizing provider had been deactivated. As another example, the AudioCare (COTS) pharmacy software depends on the PROVIDER security key remaining. The renewal process (OR\*3\*336, ORAREN routine) looks at the original order and creates a new order with the same information, sending an alert to the provider to review and sign the order. If the original provider is no longer active, the order still gets created, but the alert gets forwarded to a surrogate or backup reviewer for signature of the order.

#### SUBORDINATE KEY—Exploding Keys

If a security key has any associated subordinate keys (that is entries in the SUBORDINATE KEY Multiple field), the subordinate keys are automatically assigned along with the overall key. A security key with this feature is called an exploding key, since it and its subordinates are assigned all at once.

![](kernel-8-0-systems-management-menu-manager-user-guide/022.png) NOTE: If entries in the SUBORDINATE KEY Multiple Field are edited, dynamic updating of the security keys already assigned to users does *not* occur.

Exploding security keys *cannot* be exported with software, although, there may be support for this functionality in the future. They are intended to be created by system administrators as a timesaving method in the key allocation process.

### Deleting Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keys should *not* be deleted from the SECURITY KEY (#19.1) file. Kernel has made the NAME (#.01) field of the SECURITY KEY (#19.1) file uneditable to prevent deletion of security keys through VA FileMan. System administrators should *not* attempt to edit the key global directly to remove a key, since associated pointing relationships are left to cause errors. The one mechanism Kernel does provide for deletion of security keys is through the Kernel Installation and Distribution System (KIDS).

![](kernel-8-0-systems-management-menu-manager-user-guide/023.png) REF: For more information on KIDS, see the [*Kernel Systems Management: Kernel Installation and Distribution System (KIDS) User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf) and the [*Kernel 8.0 Developer’s Guide: KIDS Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf).

### Reindexing All Users’ Security Keys Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181699" class="anchor"></span>Figure 41: Reindex the users key’s Option

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

Manage User File ... \[XUSER FILE MGR\]

<span class="mark">Reindex the users key's</span> \[XUSER KEY RE-INDEX\]

You can use the Reindex the users key’s \[XUSER KEY RE-INDEX\] option to re-index all users’ security keys in the NEW PERSON (#200) file. If a user has a security key but is lacking the corresponding ^XUSEC cross-reference for the key, you can use this option to regenerate the ^XUSEC cross-reference. While the ^XUSEC cross-reference is being rebuilt, there can be an impact on all users with security key lookups failing in ^XUSEC until the index is entirely rebuilt; therefore, this option should be used with caution and is best delayed until users are *not* signed on.

### Using Security Keys with Reverse Locks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a security key is associated with an option through the REVERSE/NEGATIVE LOCK (#3.01) field, rather than the LOCK (#3) field, it functions to lock out users who hold the key. The security key used for a reverse lock is just like any other key, differing only in the way it is associated with an option. Menu Management’s Diagram Menus \[XUUSERACC\] option indicates the existence of any reverse locks, such as the use of the XMNOPRIV security key to prevent access to MailMan’s shared mail facility.

The typical use of a security key with the REVERSE/NEGATIVE LOCK (#3.01) field is to restrict access to options otherwise available to all users (such as MailMan User and other options on the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu \[aka Common menu\]).

### Security Key Delegation Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Starting with Kernel 8.0, security keys are subject to delegation levels just as options are subject to delegation levels. A field in the NEW PERSON (#200) file, DELEGATION LEVEL, stores a user’s delegation level (for security keys and options). When a security key is delegated, the person to whom it is delegated is assigned a level one number lower than the delegation level of the person doing the delegating. This is to prevent the delegated-to person from removing DELEGATED KEYS from someone with a lower delegation level.

![](kernel-8-0-systems-management-menu-manager-user-guide/024.png) REF: For more information about delegation levels, see the “<u>Secure Menu Delegation</u>” section.

# Secure Menu Delegation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The job of allocating menu options to users can be a time-consuming activity, so site managers may want to consider delegating this responsibility to application coordinators. Application coordinators are familiar with the menus for their software and can learn how to assign these to new users in their service area.

The Secure Menu Delegation \[XQSMD MGR\] menu allows the site manager to delegate the management of certain menu options to another user (such as an application coordinator). This user, now a delegate, can then assign these as primary or secondary options (along with their security keys) to users who fall under their administrative jurisdiction.

For example, the site manager might delegate the management of the Laboratory software options to the Lab Application Coordinator (LAC), and the LAC could then allocate or remove options from everybody in the Laboratory software. The system is set up in such a way that the LAC could also delegate, with the site manager’s permission and manager’s menu, the management of all the chemistry menus to the head of the Chemistry section, and so on, creating another level of delegation.

There are two divisions in Secure Menu Delegation:

- The menu to create and manage delegates.
- The menu for the delegates themselves to assign options to end users.

## User Interface: Acting as a Delegate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a delegate, you have been delegated options (usually by system administrators). If you have been delegated options, you can assign these options to computer users on the computer system.

As a delegate, you can assign the following options to your users:

- Options that have been delegated to you.
- Menus that you have created from options delegated to you.
- Options you have created from VA FileMan templates.

As a delegate, you need to understand the basic structure of the OPTION (#19) file, which is a file that points back to itself. That is, a menu is an entry in the OPTION (#19) file; but items on menus are themselves pointers to other entries in the OPTION (#19) file. You should also understand the difference between types of options, be familiar with menu trees, and be sufficiently reluctant to assign great numbers of secondary menus.

### Delegate’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delegate options to users, you need to be assigned the Delegate’s Menu Management \[XQSMD USER MENU\] menu, which is located under the Secure Menu Delegation \[XQSMD MGR\] menu. The options on the Delegate’s Menu Management \[XQSMD USER MENU\] menu are as shown in <u>Figure 42</u>:

<span id="_Toc207462679" class="anchor"></span>Figure 42: Delegate’s Menu Management Options

<span class="mark">Delegate's Menu Management</span> \[XQSMD USER MENU\]

Build a New Menu \[XQSMD BUILD MENU\]

Edit a User's Options \[XQSMD EDIT OPTIONS\]

Copy Everything About an Option to a New Option \[XQCOPYOP\]

Copy One Users Menus and Keys to others \[XQSMD COPY USER\]

Limited File Manager Options (Build) \[XQSMD LIMITED FM OPTIONS\]

Each of these options on the delegate’s menu is discussed in the topics that follow.

### Edit a User’s Options Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Edit a User’s Options \[XQSMD EDIT OPTIONS\] option allows you to edit a user’s primary and secondary menus. This is the chief method you can use to add (and subtract) options on your users’ menus.

Most of your work is in adding and deleting options on your users’ secondary menus. You are only able to add or delete options from a user’s secondary menu if the option in question has been delegated to you. That means that you do *not* have access to a user’s entire secondary menu; instead, only those options on the secondary menu that are also delegated to you.

If, when you edit a user’s secondary menu, you choose an option that is already on a user’s secondary menu, you are asked if you want to delete it from their secondary menu. Otherwise, you are asked if you want to add the option to their secondary menu.

If you are assigning an option that is locked with a security key, the delegation process checks whether you have been delegated the key as well. If you have, the key is automatically assigned to the user along with the option. If you have *not* been delegated the key, you get an error message saying that you have *not* been delegated the needed security key (the option is assigned to the user, but they do *not* have the key to unlock the option).

If you delete an option that is locked with a security key and that key is delegated to you (and you are at a higher key delegation level than the option holder), the key is deleted along with the option (unless the user holds another option locked by the same security key).

In the example in <u>Figure 43</u>, the user uses the Edit a User’s Options \[XQSMD EDIT OPTIONS\] option to add the LRZ MAIN menu option to the user’s secondary menu. LRZ MAIN is locked with the ZZLRMAIN security key, and that key is automatically assigned when the option is assigned:

<span id="_Toc207462680" class="anchor"></span>Figure 43: Edit a User’s Options—Sample User Dialog

Select Delegate's Menu Management Option: <span class="mark">EDIT A USER'S OPTIONS \<Enter\></span>

Select NEW PERSON NAME: <span class="mark">XUUSER,FIVE \<Enter\></span>

PRIMARY MENU OPTION: XMUSER// <span class="mark">\<Enter\></span> MailMan Menu .

No keys needed to delete!.

No keys needed to give!

SECONDARY MENU OPTION: <span class="mark">LRZ MAIN \<Enter\></span> Lab User Menu ...

ZZLRMAIN key also given!

SECONDARY MENU OPTION: <span class="mark">\<Enter\></span>

Select NEW PERSON NAME:

Unlike secondary menus, you are only able to edit a user’s PRIMARY MENU OPTION (#201) field if their current primary menu is an option that has been delegated to you. Otherwise, you are *not* allowed to change that user’s PRIMARY MENU OPTION.

![](kernel-8-0-systems-management-menu-manager-user-guide/025.png) NOTE: You *cannot* add or subtract options on a user’s primary menu; you can only replace the user’s entire PRIMARY MENU OPTION with another one.

### Build a New Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Build a New Menu \[XQSMD BUILD MENU\] option, located on the Delegate’s Menu Management \[XQSMD USER MENU\] menu, you can create new menus with menu items chosen from your delegated options.

First, you need to provide an option name for the new menu you are creating. The menu name prefix, used by the delegate to create local options, can be in one of two forms:

- (Preferred) A system administrator-assigned local namespace beginning with the letter “A” (such as A6A).
- (Discouraged) Package namespace (such as LR) to which the user *must* add the letter “Z” (such as LRZ) to avoid conflict with national releases.

![](kernel-8-0-systems-management-menu-manager-user-guide/026.png) NOTE: As of Kernel patch XU\*8.0\* 482, options in the A\* namespace can be created *without* adding a “Z” to the end of the package namespace.

Once you provide a name for the menu, you are asked to provide the following information:

- Text for the menu.
- Description for the menu.
- Items for the menu (choose from your delegated options).

Once you have created a new menu, you can assign it to your users just as if it were an option delegated to you.

### Copy Everything About an Option to a New Option Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Copy Everything About an Option to a New Option \[XQCOPYOP\] option, you can copy any option on the computer system into a new option. First you are asked which existing option you would like to copy; then, you are asked for a name for the copied option. The option name *must* begin with a namespace assigned to you by the system administrators.

### Copy One Users Menus and Keys to others Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Copy One Users Menus and Keys to others \[XQSMD COPY USER\] option, you can copy the menus and security keys of one user to another user. Each menu or security key you copy, however, *must* have been delegated to you; otherwise, they are skipped in the copy process. What gets copied from one user into the other user are the following fields of the NEW PERSON (#200) file:

- PRIMARY MENU OPTION (#201) (and all descendant menus)
- SECONDARY MENU OPTIONS (#203)
- KEYS (#51)

The PRIMARY MENU OPTION of the user you are copying from replaces the PRIMARY MENU OPTION of the user you are copying to. The SECONDARY MENU OPTIONS (#03) and the KEYS (#51) of the user you are copying from are merged into the SECONDARY MENU OPTIONS (#203) and the KEYS (#51) of the user to which you are copying.

![](kernel-8-0-systems-management-menu-manager-user-guide/027.png) NOTE: The PSDRPH security key *cannot* be allocated using this option, the Allocate/De-Allocate of PSDRPH Key(Audited) \[PSO EPCS PSDRPH KEY\] option *must* be used to allocate this security key.  
  
REF: For mor einformation on the Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option, see the see the “Allocate/De-Allocate of PSDRPH Key Option” section in the [*Kernel Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf#Allocate_DeAllocate_PSDRPH_Key_Option).

### Limited File Manager Options (Build) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Secure Menu Delegation system provides a way for delegates to create options out of VA FileMan templates. Delegates who have enough access to VA FileMan to create INPUT, SORT, or PRINT templates can create menu options for their users that directly call these templates.

#### Characteristics of Intended Users

The Limited File Manager Options (Build) \[XQSMD LIMITED FM OPTIONS\] option is designed for delegates, such as some application coordinators who have VA FileMan access to a set of files and can create INPUT, SORT, or PRINT templates. These delegates may have the VA FileMan options for editing or printing without the ability to modify data dictionaries. They may also have explicit file access to a specified set of files through the File Access Management system. Typically, they would be working without the special FILE MANAGER ACCESS CODE (#3) field, DUZ(0).

#### System Administrator Setup to Enable Building Options from Templates

To allow a user to create menu options from VA FileMan templates, system administrators *must* first assign to the user:

- Delegate’s Menu Management \[XQSMD USER MENU\] menu.
- XQSMDFM Security Key.
- A namespace beginning with the letter A (such as A6A) in which to create options. To do this, use the Specify Allowable New Menu Prefix \[XQSMD SET PREFIX\] option located on the Secure Menu Delegation \[XQSMD MGR\] menu. System administrators are discouraged from assigning package namespaces (such as LR) to which the user *must* add the letter Z (such as LRZ) to avoid conflict with national releases.

#### Building Options

The tool for building options with VA FileMan templates is called the Limited File Manager Options (Build) \[XQSMD LIMITED FM OPTIONS\]. option It is part of the Delegate’s Menu Management \[XQSMD USER MENU\] menu under the Secure Menu Delegation \[XQSMD MGR\] menu and is locked with the XQSMDFM security key.

First, you *must* have created a SORT, PRINT, or INPUT template for a VA FileMan file. Once you have created a template, you can make this template available as an option to your users by turning it into an option.

You can create three types of options:

- Edit-type option (from an EDIT template).
- Print-type option (from PRINT and SORT templates).
- Inquire-type option (from either a PRINT template or a file name).

Once you have turned the template into an option, you can assign that option to your users as you deem necessary. Then, when a user uses the option, they execute the PRINT, SORT, or INPUT template from which the option was created.

Suppose you have created a PRINT template called LRZ REFERRAL PRINT for the Lab’s REFERRAL file. To turn this PRINT template into an Inquire option, use the Limited File Manager Options (Build) \[XQSMD LIMITED FM OPTIONS\] option, as shown in <u>Figure 44</u>:

<span id="_Toc207462681" class="anchor"></span>Figure 44: Limited File Manager Options (Build)—Sample User Dialog

Select Delegate's Menu Management Option: <span class="mark">LIMITED FILE MANAGER OPTIONS (BUILD) \<Enter\></span>

The menu options you build or edit must begin with the namespace:

LRZ

The option types that may be built are P(rint), E(dit), and I(nquire), and

you must have a template or templates ready to be included in the option.

Or enter D(elete) to DELETE an option

Select Option Type (P/E/I/D): <span class="mark">I \<Enter\></span>

Enter Print Template Name (Optional): <span class="mark">LRZ REFERRAL PRINT \<Enter\></span>

Option Name: <span class="mark">LRZ REFERRAL INQUIRE \<Enter\></span>

Located in the LR (LAB SERVICE) namespace.

ARE YOU ADDING 'LRZ REFERRAL INQUIRE' AS A NEW OPTION (THE 996TH)? <span class="mark">Y \<Enter\></span> (YES)

OPTION MENU TEXT: <span class="mark">DISPLAY A REFERRAL \<Enter\></span>

MENU TEXT: Display a Referral Replace <span class="mark">\<Enter\></span>

DESCRIPTION:

1\> <span class="mark">Display Lab Referral entries (option created by LAB ADPAC).</span>

2\> <span class="mark">\<Enter\></span>

EDIT Option: <span class="mark">\<Enter\></span>

Select Delegate's Menu Management Option:

## System Management: Managing Delegates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options for creating and managing delegates are on the Secure Menu Delegation \[XQSMD MGR\] menu, which is on the Menu Management menu. Typically, system administrators would be the sole holder of this menu. <u>Table 3</u> lists the options on this menu:

| Option Text \[Name\]                                       | Function          |
|------------------------------------------------------------|-------------------|
| Select Options to be Delegated \[XQSMD ADD\]               | Delegate options  |
| List Delegated Options and their Users \[XQSMD BY OPTION\] | Print Report      |
| Print All Delegates and their Options \[XQSMD BY USER\]    | Print Report      |
| Remove Options Previously Delegated \[XQSMD REMOVE         | Undo Delegation   |
| Replicate or Replace a Delegate \[XQSMD REPLICATE\]        | Copy a Delegate   |
| Show a Delegate’s Options \[XQSMD SHOW\]                   | Print Report      |
| Delegate’s Menu Management \[XQSMD USER MENU\]             | Delegate’s menu   |
| Specify Allowable New Menu Prefix \[XQSMD SET PREFIX\]     | Assign namespaces |

<span id="_Toc207462697" class="anchor"></span>Table 4: SERVER ACTION (#221) Field Security Values for Server Requests

The main options to create and manage delegates are:

- Select Options to be Delegated \[XQSMD ADD\]
- Replicate or Replace a Delegate \[XQSMD REPLICATE\]

### Delegating Options: Select Options to be Delegated Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delegate options, use the Select Options to be Delegated \[XQSMD ADD\] option from the Secure Menu Delegation \[XQSMD MGR\] menu. Using this option is a two-step process:

1.  
1.  Choose the users to whom options are delegated.Choose which options to delegate to that group of users.

You can choose to set up one user or many users as delegates. You can choose one option or a group of options to delegate to them.

You also need to assign (*not* delegate!) the Delegate’s Menu Management \[XQSMD USER MENU\] menu to the delegate; this menu gives delegates the means to assign delegated options to users, as shown in <u>Figure 45</u>.

<span id="_Toc207462682" class="anchor"></span>Figure 45: Delegating Options: Select Options to be Delegated Option—Sample User Dialog

Select Secure Menu Delegation Option: <span class="mark">SELECT OPTIONS TO BE DELEGATED \<Enter\></span>

Enter the name(s) of your delegate(s), one at a time

Name: <span class="mark">XUUSER,THREE \<Enter\></span>

Name: <span class="mark">XUUSER,FOUR \<Enter\></span>

Name: <span class="mark">\<Enter\></span>

Enter options you wish to DELEGATE TO these users

Add option(s): <span class="mark">XUINQUIRE \<Enter\></span>

Add option(s): <span class="mark">XUUSERACC \<Enter\></span>

Add option(s): <span class="mark">\<Enter\></span>

For the following user(s):

1\. XUUSER,THREE

2\. XUUSER,FOUR

You will delegate the following options:

XUINQUIRE Inquire

XUUSERACC Diagram Menus

Delegated by XUUSER,FIVE on Jul. 21, 2004 3:55 PM.

Ready to delegate these options to these people? Y// <span class="mark">\<Enter\></span>

Request to add delegated options has been queued, task \# 465,

named: XUUSER,FIVE adding delegated options.

#### Delegating Security Keys

If options that you intend to delegate are locked with security keys, you need to delegate the matching keys to the delegate; otherwise, the delegate is *not* able to assign keys to unlock options they have assigned to their users.

If the option is locked with a security key that you possess, the Select Options to be Delegated \[XQSMD ADD\] option branches you to the Key Management program and lets you allocate the appropriate keys to the delegates you are creating.

However, to assign security keys to users, the delegate *must be delegated* the key. To do that, you need to use the Key Management \[XUKEYMGMT\] menu option, Delegate keys \[XQKEYDEL\] option. This option allows you to delegate security keys to delegates by populating the DELEGATED KEYS Multiple field in their NEW PERSON (#200) file entry. Security keys entered in a delegate’s DELEGATED KEYS Multiple allow them to allocate the entered keys to other users (but *not* themselves).

When a delegate assigns options to a user, they can assign the matching security keys as part of that process. However, as an enhancement to a delegate’s ability to work with keys, system administrators can assign the delegate the following options from the Key Management \[XUKEYMGMT\] menu option:

- Allocation of Security Keys \[XUKEYALL\]
- De-allocation of Security Keys \[XUKEYDEALL\]
- Show the Keys of a Particular User \[XQLISTKEY\]

If the delegate does *not* hold the XUMGR security key, which allows any key to be allocated, the Key Management \[XUKEYMGMT\] menu option only allow delegates to allocate and de-allocate security keys they have been delegated. Kernel also follows key delegation levels with the Allocation of Security Keys \[XUKEYALL\] and De-allocation of Security Keys \[XUKEYDEALL\] options.

![](kernel-8-0-systems-management-menu-manager-user-guide/028.png) NOTE: Key Management \[XUKEYMGMT\] menu options *must* be separately assigned; they are *not* a part of the Delegate’s Menu Management \[XQSMD USER MENU\] menu.

#### Delegation Level—Options and Keys

The DELEGATION LEVEL (#19.2) field in the NEW PERSON (#200) file specifies the number of steps that a person is from the original delegation of options by the site manager (whose DELEGATION LEVEL is 0). Starting with Kernel 8.0, the delegation level is also maintained for the DELEGATED KEYS (#52) field. For instance, if the site manager delegates all laboratory options to the Lab ADP Application Coordinator (ADPAC), then the Lab ADPAC would have a DELEGATION LEVEL of 1. Should the Lab ADPAC further delegate a set of those options to the Lab Chief of Chemistry, the chief would have a level of 2, and so on.

The use of levels ensures that supervision is *not* compromised such that the lower-level user could alter menus or remove security keys of the higher-level person. No attempt is made to determine who works for whom, since that information is *not* available to the software. Delegation chains should therefore be constructed with some care.

To modify the set of options (and accompanying security keys) delegated to a particular person, you *must* have a DELEGATION LEVEL equal to, or less than, the person you are trying to modify. If you create a new delegate by delegating some (or all) of the options delegated to you, that person has a DELEGATION LEVEL equal to your level +1.

It may be necessary to modify delegation levels using VA FileMan as the organization’s structure changes over time.

### Further Delegation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only way a delegate can delegate, rather than simply assign options to someone else is if the delegate has access to either of the following options:

- Select Options to be Delegated \[XQSMD ADD\]
- Replicate or Replace a Delegate \[XQSMD REPLICATE\]

These options should only be on the Secure Menu Delegation \[XQSMD MGR\] menu. You should carefully evaluate whether to give this menu to delegates, because it gives them the right to further delegate.

### Options too Sensitive to Delegate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain options (such as programmer-related options) are considered too sensitive or powerful to be delegated. They are marked as *not* delegable in the OPTION (#19) file, and the Secure MenuMan Delegation software does *not* delegate these options. The traditional methods of assigning these menu options *must* be employed by the Site Manager.

It should be noted that a higher-level option, such as the Systems Manager Menu \[EVE\] menu, would still give the delegate access to lower-level options, such as the Menu Management \[XUMAINT\] menu, even though XUMAINT is itself marked in the OPTION (#19) file as *non*-delegable. The delegation software does *not* follow the option trees down to ensure that options of options are *not* delegable.

![](kernel-8-0-systems-management-menu-manager-user-guide/029.png) CAUTION: It is *highly recommended* that the site manager, information security officer (ISO), or chief system administrator review the options marked as too sensitive to be delegated and, using VA FileMan, add any locally sensitive options to this list.  
  
It is the responsibility of each site to ensure that the security of the system is *not* violated.

### Replicate or Replace a Delegate Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can copy the delegated options of a delegate to another user. Use the Replicate or Replace a Delegate \[XQSMD REPLICATE\] option to do this. The options that you transfer to another user do *not* replace any options the user has been previously delegated. They are added to those options, if any. Like the Select Options to be Delegated \[XQSMD ADD\] option, this option also can branch you to the security key allocation program for the new delegate.

You are also asked if the delegated options should be removed from the original delegate. If you say NO (N), the original delegate remains a delegate. If you say YES (Y), all delegated options are removed from the original delegate, who is no longer an active delegate. To remove the options from a delegate, however, you *must* have a DELEGATION LEVEL lower than they do.

### Remove Options Previously Delegated Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To simply remove an option from a delegate’s list of delegable options, use the Remove Options Previously Delegated \[XQSMD REMOVE\] option:

1.  
2.  

Enter the name or names of the delegates from which you want to remove options.Enter the option or options you want to remove from the specified set of delegates.

You are given a chance to review the choices you made; if you say to proceed, a task is queued that removes the options you selected from the delegates you specified.

### Specify Allowable New Menu Prefix Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Specify Allowable New Menu Prefix \[XQSMD SET PREFIX\] option to assign allowable menu prefixes to your delegates. Your delegates need to be given allowable new menu prefixes if they:

- Build new menus.
- Copy options.
- Create options from VA FileMan templates.

Typically, if your delegate works with one software application, you will assign them that software’s namespace as an allowable prefix. Options that the delegate creates *must* then be prefixed with that namespace, appended with a Z.

If you do *not* specify an allowable prefix for a delegate, they are *not* able to use the following options:

- Build a New Menu \[XQSMD BUILD MENU\]
- Copy Everything About an Option to a New Option \[XQCOPYOP\]
- Limited File Manager Options (Build) \[XQSMD LIMITED FM OPTIONS\]

You can specify multiple new menu prefixes for a given delegate.

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the following options to generate reports about delegates on your system:

- List Delegated Options and their Users \[XQSMD BY OPTION\]  
  (Sort by delegated option.)
- Print All Delegates and their Options \[XQSMD BY USER\]  
  (Sort by delegate name.)
- Show a Delegate’s Options \[XQSMD SHOW\]  
  (Display all delegated options for one delegate.)

# Server Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server Options System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### What is a Server Option?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A server option is a special type of option (stored in the OPTION \[#19\] file) that can be triggered by mail messages. Addressing a mail message to a server option is termed a “server request.” A server request awakens the option and causes it to execute the following:

- Any M code in the server option’s ENTRY ACTION (#20) field.
- Any M code in the HEADER (#26) field.
- The routine indicated in the ROUTINE (#25) field.
- Any M code in the EXIT ACTION (#15) field.

A server-type option is like a Run Routine-type option. The difference is that a server option is activated by a mail message while a run routine option is activated by a user choosing that option from a menu on a screen. Server options should only be invoked by mail messages (never directly by a user).

The form of the mail message that activates the server option is identical to any other mail message except that it is addressed to S.*\<option name\>*. The “S.” (like the “G.” form for sending to mail groups) routes the message to the server request software.

### What Can Server Options Do?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A server request might trigger a bulletin, send a MailMan reply, or initiate an audit of itself. Developers and local system administrators can also customize the bulletins or MailMan replies.

### Can Server Requests Be Denied?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only server-type options can be activated by mail messages. The following *must* be true for a server request to be processed:

- The server option *must* be set to type “s” in the TYPE (#4) field of the OPTION (#19) file. If the type is *not* “s” and a request is received, it results in an error that, by default, is recorded in the AUDIT LOG FOR OPTIONS (#19.081) file.
- The server option name *must* be complete and exact when a server request is made, or the request is denied.
- The server option *mustnot* be disabled (it can be disabled for all requests by setting its LOCK \[#3\] or OUT OF ORDER MESSAGE \[#2\] fields).

If the conditions listed above are satisfied, the only mechanism a site has for security for server requests is the setting of the server option’s SERVER ACTION (#221) field. This field has the settings listed in <u>Table 4</u>:

| Value | Description                                                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R | Run immediately. This code causes the server request to be honored in real time as soon as it is received from MailMan (run immediately), provided it is *not* prevented by a setting in the TIMES/DAYS PROHIBITED (#3.91) field.                                                             |
| Q | Queue server. This code causes the server request to be honored (queued) as soon as permitted by the TIMES/DAYS PROHIBITED (#3.91) Multiple field.                                                                                                                                            |
| N | Notify local authorities. This code causes the server request to create a TaskMan entry but does *not* schedule it to run. A local mail group is notified along with the task number so that it can be approved locally and then scheduled to run using TaskMan’s Requeue Tasks\] option. |
| I | Ignore any server requests. This code causes the software to ignore all requests for this server option. A bulletin or MailMan message can still be sent, however.                                                                                                                            |

<span id="_Toc207462698" class="anchor"></span>Table 5: OPTION (#19) File Field Values When Setting Up a Server Option

When a server request is received, the server option itself is executed similarly to the way a normal option is executed. That is, if a server request causes a server option to be run or queued, the server option, (along with its associated entry action code, header code, routine, and exit action code), does *not* run until the option runs as scheduled by TaskMan.

### How Can the Number of Instances of a Server Option Be Controlled?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To tie a server option to a device of type RESOURCES, use the SERVER DEVICE (#227) field and set the SERVER ACTION (#221) field to Q (Queue server) in the OPTION (#19) file. This allows you to control how many instances of the server option can run at any one time. Only as many server option processes can run at any one time as are set up in the associated device’s RESOURCE SLOTS (#35) field in the DEVICE (#3.5) file. So, if 30 mail messages come in at the same time and attempt to fire off 30 server option processes, you can control the maximum number of simultaneous processes that run. Additional server options can run when resource slots are freed up from the resource device.

### Setting Up a Server Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A server option has many fields in common with other option types and is set up using the Edit options \[XUEDITOPT\] option, which is located on the Menu Management \[XUMAINT\] menu. This option calls the VA FileMan Template Edit \[DITEMP\] option, which prompts for data to be entered in the fields shown in <u>Table 5</u> (listed in field number order):

<table>
<caption><p><span id="_Toc207462699" class="anchor"></span>Table 6: XQSCHK Server Option—Error/Warning Messages</p></caption>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td>This should be a namespaced set of <strong>3</strong> to <strong>30 uppercase letters</strong>.</td>
</tr>
<tr class="even">
<td>MENU TEXT (#1)</td>
<td>Since there is never a menu prompt for a server option, this field should instead contain an accurate description of what this server option does, as it is used by the server request in error messages, bulletins, and MailMan replies. It should be <strong>3</strong> to <strong>50 characters</strong> in length.</td>
</tr>
<tr class="odd">
<td>OUT OF ORDER MESSAGE (#2)</td>
<td>If this field contains between <strong>1</strong> and <strong>80 characters</strong> of text, the server option is placed “out of order” and is <em>not</em> activated by a server request. The message itself is included in bulletins or MailMan replies that report the failure.</td>
</tr>
<tr class="even">
<td>LOCK (#3)</td>
<td>Since server options have no online user associated with them, the existence of a lock in this field prevents the execution of a server option, much like an OUT OF ORDER MESSAGE. The user for all server options is the PostMaster. The originator of a server request is recorded, however, in the return address variable.</td>
</tr>
<tr class="odd">
<td>DESCRIPTION (#3.5)</td>
<td>This <strong>WORD-PROCESSING</strong> field should contain an extensive description of the server option intended for the local site manager and system administrators. The description should include an exact description of what the server option does and the resources it requires.</td>
</tr>
<tr class="even">
<td>PRIORITY (#3.8)</td>
<td>This field determines the priority at which the server option runs.</td>
</tr>
<tr class="odd">
<td>TIMES/DAYS PROHIBITED (#3.91) Multiple</td>
<td>This Multiple allows the local system administrators to control the days and times during which the server request is honored. If data is entered that prevents the server option from being honored immediately, the software determines the next available time slice that is <em>not</em> prohibited and queues the request for that time. Server options that are marked <strong>R</strong> for Run Immediately in the SERVER ACTION field are instead queued to run at the next non-prohibited time-period.</td>
</tr>
<tr class="even">
<td>TYPE (#4)</td>
<td>This field <em>must</em> always contain the code “<strong>s</strong>” for server-type option, or the request is denied and an error results.</td>
</tr>
<tr class="odd">
<td>EXIT ACTION (#15)</td>
<td>The M code stored in this field is executed just before the server option exits.</td>
</tr>
<tr class="even">
<td>ENTRY ACTION (#20)</td>
<td>The M code in this field is executed if the server request is honored. If, as with other options, the variable <strong>XQUIT</strong> exists after the Entry Action is executed, the request is terminated at that point and an error is generated.</td>
</tr>
<tr class="odd">
<td>ROUTINE (#25)</td>
<td><p>If there is a routine name in this field in any of the following forms, the routine is run:</p>
<ul>
<li><p><strong>ROUTINE</strong></p></li>
<li><p><strong>^ROUTINE</strong></p></li>
<li><p><strong>TAG^ROUTINE</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>HEADER (#26</td>
<td>This field of M code is executed, if it exists.</td>
</tr>
<tr class="odd">
<td>SERVER BULLETIN (#220)</td>
<td><p>This field is a pointer to the BULLETIN (#3.6) file; it indicates the bulletin to use to notify the local mail group of a server request on their system. If there is no bulletin entered in this field, the default bulletin <strong>XQSERVER</strong> is used.</p>
<p>Unless there are pressing reasons to do otherwise, it is recommended that the default bulletin <strong>XQSERVER</strong> be used by leaving the SERVER BULLETIN field blank.</p>
<p>If the mail groups pointed to by <strong>XQSERVER</strong> (or the bulletin pointed to in this field) do <em>not</em> contain an active user (that is a user possessing a Verify Code and no effective TERMINATION DATE) the software turns on auditing (that is SERVER AUDIT described below) and sends a MailMan message to the local PostMaster.</p>
<p>![](kernel-8-0-systems-management-menu-manager-user-guide/030.png) CAUTION: The most common reason for server options not functioning is that there is no active user associated with the bulletin specified. For security reasons, server options do <em>not</em> run without a locally defined active user associated with the chosen bulletin.</p></td>
</tr>
<tr class="even">
<td>SERVER ACTION (#221)</td>
<td>This <strong>SET OF CODES</strong> field allows the local system administrators to decide how a server request is to be treated (see <u>Table 4</u>).</td>
</tr>
<tr class="odd">
<td>SERVER MAIL GROUP (#222)</td>
<td><p>This field is a pointer to another mail group (the first is pointed to by <strong>XQSERVER</strong> or the bulletin in Field #220) to which server request notifications are to be sent. The software notifies all legitimate users in all mail groups pointed to. It is <em>recommended</em> that this field be left blank, and a mail group be assigned the chosen bulletin instead.</p>
<p>![](kernel-8-0-systems-management-menu-manager-user-guide/031.png) CAUTION: Server options do <em>not</em> work unless there is a local, active user associated with the specified mail group.</p></td>
</tr>
<tr class="even">
<td>SERVER AUDIT (#223)</td>
<td><p>This field causes the server request to be audited in the AUDIT LOG FOR OPTIONS (#19.081) file. The default is <strong>YES</strong>. The information stored for an audited server option includes:</p>
<ul>
<li><p>Option name</p></li>
<li><p>User (always PostMaster)</p></li>
<li><p>Device</p></li>
<li><p>Job number</p></li>
<li><p><strong>DATE/TIME</strong></p></li>
<li><p>CPU</p></li>
<li><p>Message number</p></li>
<li><p>Return address of sender</p></li>
<li><p>Subject of the message</p></li>
<li><p>Error message</p></li>
</ul>
<p>A server option can also be audited using the normal option auditing software. Auditing the PostMaster or the namespace “<strong>XQSRV</strong>” captures all server requests.</p></td>
</tr>
<tr class="odd">
<td>SUPPRESS BULLETIN (#224)</td>
<td>If set to “<strong>Y</strong>” (<strong>YES</strong>), it prevents a bulletin from being sent under normal conditions. If there is an error or a possible security breach, a bulletin is still fired. If the field is <em>not</em> filled in, it takes the default of “<strong>N</strong>,” which means that the sending of bulletins is <em>not</em> suppressed.</td>
</tr>
<tr class="even">
<td>SERVER REPLY (#225)</td>
<td><p>This <strong>SET OF CODES</strong> controls the MailMan reply to a server request. The reply is a message returned to the user who has sent the server request and should <em>not</em> be confused with the local user to whom the bulletin is addressed. If a reply is requested, the software uses the return address of the sender as supplied by MailMan to send a local or network reply.</p>
<p>![](kernel-8-0-systems-management-menu-manager-user-guide/032.png) <strong>REF:</strong> For an example of a server-type option return message, see <u>Figure 47</u>.</p>
<p>The possible codes are:</p>
<ul>
<li><p><strong>N—</strong>No reply is sent (the default).</p></li>
<li><p><strong>E—</strong>A reply is sent to the return address of the sender only in the event of an error.</p></li>
<li><p><strong>R—</strong>A reply is always sent.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>SERVER DEVICE (#227)</td>
<td>Optionally, use this field and the SERVER ACTION (#221) field set to “<strong>Q</strong>” (Queue server) to control the number of server requests for this server option that can be processed at any one time. Enter the name of a device of type RESOURCES (in the DEVICE [#3.5] file). The number of instances of this server option that can run at any one time is limited to the number of resource slots in the selected resource device (that is RESOURCE SLOTS (#35) field in the DEVICE (#3.5) file).</td>
</tr>
</tbody>
</table>

<span id="_Toc207462699" class="anchor"></span>Table 6: XQSCHK Server Option—Error/Warning Messages

### Testing if a Site is Reachable: XQSPING Server Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the TCP/IP Type Ping Server \[XQSPING\] server option to invoke the Kernel XTSPING utility at a site. This utility tests to see if the domain to which a message is addressed is reachable. For example, if you want to see if the network link to the Field Office (FO) is working properly, you could address a message to:

S.XQSPING@*\<REDACTED\>*.VA.GOV

If the text of the message and the subject are simply the line “Testing”, you should get the message shown in <u>Figure 46</u> in return:

<span id="_Toc207462683" class="anchor"></span>Figure 46: Sample Message Received when “pinging” a Domain Address

MailMan message for Xmuser,One COMPUTER SPECIALIST

Subj: PING reply to: TESTING \[#999\] 28 Nov 92 12:17 1 line

From: PING SERVER in 'IN' basket.

-----------------------------------------------------------

Testing.

The XTSPING utility copies the message addressed to it and returns it to the person who sent it.

### Testing a Server Option: XQSCHK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Server-type Option Test Server \[XQSCHK\] server option to return information about a server option on a remote system. You should list the server option you want to test in the text of the message addressed to XQSCHK. The subject of the message sent to the XQSCHK server option is *not* important. However, the body of the text *must* contain the name of the server option to be checked. When you specify the server option to be checked, do *not* precede the server option name with an “S.”, instead, list the server option’s name exactly as it appears in the OPTION (#19) file’s .01 field.

The XQSCHK server option returns Fields \#220 to \#225 from the OPTION (#19) file to show how the option has been set up. In addition, several other things about the option are investigated and error or warning messages may be also returned.

For example, if you want diagnostic information about a server option named ZZSERVER, and the option resides on the system at a field office (FO), you should create a message containing the text ZZSERVER and send it to:

S.XQSCHK@*\<REDACTED\>*.VA.GOV

The XQSCHK server option unloads the name of the server option (in this example ZZSERVER, see <u>Figure 47</u>). Assuming such a server option exists, you would expect to receive a reply in a MailMan message as shown in <u>Figure 47</u>:

<span id="_Toc207462684" class="anchor"></span>Figure 47: XQSCHK Server Option—Sample MailMan Return Message

MailMan message for XUUSER,ONE COMPUTER SPECIALIST

Subj: Server Request Reply from *\<REDACTED\>*.VA.GOV

From: Postmaster in 'IN' basket

---------------------------------------------------------------------------------

Nov. 28, 1992 12:18 PM

Sender: XUUSER,ONE

Option name: ZZSERVER

Subject: TESTING XQSCHK

Message \#: 999

This is a reply from *\<REDACTED\>*.VA.GOV

Checking Server Option ZZSERVER.

Fields 220 to 225 in the Option File:

220 - No bulletin selected, will use default XQSERVER.

221 - The server action code is Run Immediately.

222 - The mail group ZZGROUP is pointed to.

223 - Auditing is turned off.

224 - The server's bulletin is not suppressed.

225 - Reply mail is sent when an error is trapped.

### Errors and Warnings from the XQSCHK Server Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the errors or warnings that might be included in the return message from the XQSCHK server option, along with an explanation of each:

| Error/Warning Message                                                            | Description                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Can't unload name of server from message: \[message subject\].                   | The name of the server option to be tested could *not* be unloaded from the text of the message sent to waken the XQSCHK server option. The message should contain just the name of the server option to be tested and nothing more. XQSCHK ignores blank lines (up to 4) and any lines of text that follow the line where it finds the options’ name. |
| The option \[option name\] is not in the Option File.                            | There is no option in the remote site’s OPTION (#19) File that matches the name of the server option that was unloaded from the text of the message. The string it is using to search the OPTION (#19) File is returned in \[option name\].                                                                                                                        |
| Option \[option name\] is not shown as a server-type option but a \[type\].      | The option is *not* marked in the remote OPTION (#19) File as a server-type option, but some other kind of option returned in \[type\], such as a print-type option.                                                                                                                                                                                               |
| \[Option name\] is marked as Out Of Order with the message: \[message\].         | The OUT OF ORDER MESSAGE field for that option has been filled in with the text that is returned in \[message\].                                                                                                                                                                                                                                                   |
| The expected data in ^DIC(19,\[option number\], 220) is missing.                 | There is no information for this option in Fields \#220 through \#225. The 220 node of the OPTION (#19) File is missing or blank.                                                                                                                                                                                                                              |
| No bulletin associated with this option default XQSERVER is missing from system. | There is no bulletin pointed to by Field \#220 of this option in the OPTION (#19) File, and the default XQSERVER bulletin has been removed from the system. Server options are *not* run without an associated bulletin, even if it is suppressed.                                                                                                                 |
| Option \[option name\] points to a bulletin not in the bulletin file.            | WARNING: there is an invalid pointer in Field \#220 of the OPTION (#19) File that points to a nonexistent bulletin. The default bulletin XQSERVER is used.                                                                                                                                                                                                         |
| Option \[option name\] points to a mail group not in the Mail Group File.        | WARNING: there is an invalid pointer in Field \#222 of the OPTION (#19) File indicating a mail group that should receive the bulletin in addition to the mail group pointed to by the BULLETIN (#3.6) file.                                                                                                                                                        |
| There are no mail groups associated with the bulletin \[bulletin name\].         | The bulletin returned in \[bulletin name\] does *not* have a mail group associated with it in the BULLETIN (#3.6) file.                                                                                                                                                                                                                                            |
| There is no active user associated with the bulletin \[bulletin name\].          | When following the pointers from the bulletin to the mail group to the NEW PERSON (#200) file, an active user was *not* found. Each server option *must* be linked to a user who has an Access and Verify Code and is not terminated.                                                                                                                              |
| There is no routine in field 25 of the Option File for this option.              | This server option has no routine associated with it in the ROUTINE field of the remote site’s OPTION (#19) File.                                                                                                                                                                                                                                                  |
| The routine \[routine name\] is not on the system.                               | The routine that is named in the ROUTINE field of the OPTION (#19) File is *not* found on the system. It has been removed or is in another UCI.                                                                                                                                                                                                                    |
| There is no server action code for this option.                                  | The required server option action code in Field \#221 of the OPTION (#19) File is blank.                                                                                                                                                                                                                                                                           |

<span id="_Toc207462700" class="anchor"></span>Table 7: Help System Command Actions

# Help Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Help Processor User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel’s Help Processor is a utility for displaying help frames. A help frame is a screen of text that explains some part of a software application. Each individual help frame can have keyword links to other help frames. Using these keywords, you can navigate through a series of related help frames to learn more about each help frame section.

Some places where you may encounter help frames are:

- When requesting help on options in the menu system.
- When requesting help on a menu in the menu system.
- As a standalone option describing some part of a software application.

<span id="_Toc207462685" class="anchor"></span>Figure 48: Help Frame Example

USING THE 'Help Processor' OPTION

The Help processor is a frame-oriented display system which allows

users and programmers to access and manage help text.

The system is driven off of the HELP FRAME FILE.

There are several LINKS which will cause the help text to be

displayed to the user. The system is interactive, and the user may

select which section he/she wishes further information on.

The Help Frame Processor Menu contains the following options:

DISPLAY/EDIT - Displays the text of a help frame, and allows for the

edit of the name, header, text, or related frames.

CROSS REFERENCE - Lists all the help frames for a specified package,

showing parent help frames, linked to menu option,

and invoking routine.

LIST - Lists the help frames in several different formats.

MORE OPTIONS...

Select HELP SYSTEM action or \<return\>:

At the bottom of every displayed help frame is a “Select HELP SYSTEM action...” prompt. You have several choices at this prompt. To back your way out of the help frame system, you can simply press the \<Enter\> key. This backs you up one level or exits you if you are at the top level of a help frame tree. If you want to exit quickly from help frames, you can enter ^Q to quit immediately without having to back all the way out.

You can list other choices at the “Select HELP SYSTEM action...” prompt by entering a question mark (?). The full list of choices are shown in <u>Table 7</u>:

| Response      | Action                                                   |
|---------------|----------------------------------------------------------|
| Keyword   | Jump to help frame associated with Keyword.              |
| \<Enter\> | Quit to previous help frame (exit if no previous).       |
| ^Q        | Quit the help system.                                    |
| ^R        | Refresh the current frame.                               |
| ^T        | Table of related frames.                                 |
| ^O        | On/off switch for bracketing/reverse video of keywords.  |
| ^H        | How you got to this frame.                               |
| ^E        | Edit this frame (only if authorized as editor of frame). |

Keywords in a help frame are displayed by the help processor in reverse video. If you enter the first few letters of a keyword and press the \<Enter\> key, the help processor jumps to the help frame linked to the entered keyword.

### Help Frames in the Menu System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a menu option has associated help frames, you can display them by entering a question mark (?) followed by an option’s menu text or synonym at a menu prompt (that is ?option), as shown in <u>Figure 49</u>:

<span id="_Toc207462686" class="anchor"></span>Figure 49: Display a Help Frame for an Option—Entering One Question Mark (?) and Option Name

Select Office Menu Option: <span class="mark">?MAILMAN \<Enter\></span>

Entering three question marks (???) at the menu prompt (<u>Figure 50</u>) indicates which options have associated extended help (help frames).

<span id="_Toc207462687" class="anchor"></span>Figure 50: Display a Help Frame for an Option—Entering Three Question Marks (???)

Select Office Menu Option: <span class="mark">??? \<Enter\></span>

If a menu itself has an associated help frame, entering four question marks (????) at the menus “Select ... action: ” prompt (<u>Figure 51</u>) displays the help frame associated with that menu if one exists:

<span id="_Toc207462688" class="anchor"></span>Figure 51: Display a Help Frame for an Option—Entering Four Question Marks (????)

Select Help Processor Option: <span class="mark">???? \<Enter\></span>

## Help Processor System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help frames are entries in the HELP FRAME (#9.2) file. The Header and Text of help frames can be displayed to users to provide instruction about software or other topics. Help frames can be distributed with software or can be created locally to provide information about local policies and procedures.

The options used to create, edit, and link help frames are on the Help Processor \[XQHELP-MENU\] menu, are shown in <u>Figure 52</u>:

<span id="_Toc207462689" class="anchor"></span>Figure 52: Help Processor Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Menu Management ... \[XUMAINT\]

<span class="mark">Help Processor ...</span> \[XQHELP-MENU\]

Display/Edit Help Frames \[XQHELP-DISPLAY\]

List Help Frames \[XQHELP-LIST\]

New/Revised Help Frames \[XQHELP-UPDATE\]

Cross Reference Help Frames \[XQHELP-XREF\]

Assign Editors \[XQHELP-ASSIGN\]

Unassign Editors \[XQHELP-DEASSIGN\]

Fix Help Frame File Pointers \[XQHELPFIX\]

Use of the Help Processor options is explained by help frames associated with the options.

### Display/Edit Help Frames Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The help frames can be displayed with the Display/Edit Help Frames option \[XQHELP-DISPLAY\]. You can use the ?option syntax at the select prompt, as shown in <u>Figure 53</u>:

<span id="_Toc207462690" class="anchor"></span>Figure 53: Display/Edit Help Frames Option—Displaying Help Using the ?option Syntax

Select Help Processor Option: <span class="mark">?DISPLAY \<Enter\></span> /Edit Help Frames

### List Help Frames Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Help Frames \[XQHELP-LIST\] option can be used to print a series of frames with a table of contents and page numbering to resemble a hard copy manual.

<span id="_Toc207462691" class="anchor"></span>Figure 54: List Help Frames Option—Sample User Dialog

Select Help Processor Option: <span class="mark">LIST HELP FRAMES \<Enter\></span>

Select primary HELP FRAME from which to list: <span class="mark">XUDOC NEW \<Enter\></span>

### New/Revised Help Frames Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The New/Revised Help Frames \[XQHELP-UPDATE\] option produces a VA FileMan-generated print of all help frames that have been updated during a specified time-period.

### Cross Reference Help Frames Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cross Reference Help Frames \[XQHELP-XREF\] option lists any of the following cross-references to a specified set of help frames:

- Parents (other help frames that call the specified help frame).
- Options (options whose HELP FRAME field references the specified help frame).
- Routines (if a developer has entered the routine in the specified help frame’s INVOKED BY ROUTINE field).

### Fix Help Frame File Pointers Option—Deleting Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no Kernel utility to delete help frames, but the menu system does *not* generate errors if a pointed-to help frame is missing. If a site chooses to delete help frames using VA FileMan, they should use the Fix Help Frame File Pointers \[XQHELPFIX\] option afterwards to delete dangling pointers from the OPTION (#19) file’s HELP FRAME field.

### Assigning/De-assigning Help Frame Editors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An existing help frame can be edited, through the Help Processor options, by the following people:

- The help frame author.
- Any holder of the XUAUTHOR security key.
- Anyone who has been assigned as an editor to that help frame.

To assign an editor to a given help frame use the Assign Editors\[XQHELP-ASSIGN\] option or to de-assign an editor to a given help frame, use the Unassign Editor \[XQHELP-DEASSIGN\] option.

### Disk Space Concerns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help frames consume disk space. The amount can be considerable if numerous frames are exported with a software application. You can estimate the size of the HELP FRAME (#9.2) file by Kernel’s Block Count utility.

<span id="_Toc207462692" class="anchor"></span>Figure 55: Estimating the Size of the HELP FRAME (#9.2) File Using Kernel’s Block Count Utility

Select Systems Manager Menu Option: <span class="mark">PROG \<Enter\></span> rammer Options

Select Programmer Options Option: <span class="mark">GLOBAL \<Enter\></span> Block Count

Block Count for Global <span class="mark">^DIC(9.2) \<Enter\></span>

### Creating and Editing Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One way to edit help frames from the HELP FRAME (#9.2) file is to use the Display/Edit Help Frames \[XQHELP-DISPLAY\] option to display the help frame in question. Then, at the “Select Help System Action:” prompt, you can enter ^E to edit the help frame if you have edit access to the help frame. You have edit access if:

- You are the help frame’s author.
- You are assigned as an editor for the help frame.
- You are a holder of the XUAUTHOR security key.

Another handy way to edit help frames is within the help frame system as invoked from a software application. For example, if the help frames are tied to a software’s options, you can use the software, invoke the help frame for each field or option, and then edit that help frame on the spot. To edit a help frame in this manner, enter ^E at the help frame action prompt. To do this, however, you *must* have edit access to the help frame as described above.

#### Namespacing of Help Frames

Like entries in the OPTION (#19) or SECURITY KEY (#19.1) files, entries in the HELP FRAME (#9.2) file *must* be namespaced to avoid overwriting problems.

#### Help Frame Layout Considerations

When entering the text of help frames, you should keep each line to fewer than 80 characters for proper screen display.

![](kernel-8-0-systems-management-menu-manager-user-guide/033.png) NOTE: The text is displayed “as it stands” and is *not* processed by VA FileMan’s text formatter. That is, the text is *not* wrapped, and WORD-PROCESSING “windows” are *not* evaluated. Frames are usually 22 lines in length although an end-of-page READ is issued to allow a pause if the frame exceeds 22 lines.

If there are only a few lines of text, the Help Processor displays a table at the bottom of the screen of all related frames (those frames that the current frame has keyword links to). The table shows the choices of other frames, so the user need *not* enter the keywords in the text. You can force the table of related frames out of the display by entering enough blank lines so that the frame’s length is 20 lines (assuming the display has a page length of 24 lines).

For the Help Processor to identify and highlight keywords, the keywords are entered in the text of the help frame enclosed in square brackets. By convention, keywords in help frames are usually in all capital letters. A square bracket character can be displayed as part of the frame’s text by entering two of the characters (such as \[\[ or \]\]).

If the frames are to be printed using the List Help Frames \[XQHELP-LIST\] option, the resulting help manual has an organized outline, if the frames are linked in a top-down tree structure without any circular connections among the branches.

#### Linking a Help Frame as Help for an Option or Menu

Once a help frame (or a series of help frames) has been created, you can associate it (them) with options by entering the name of the top-level help frame in the HELP FRAME (#3.7) field of the OPTION (#19) file. You can use Menu Manager’s Edit options \[XUEDITOPT\] option to do this. That way, when a user enters a single question mark (?) in conjunction with the option name, Menu Manager invokes the associated help frame.

<span id="_Toc207462693" class="anchor"></span>Figure 56: Linking Help Frames to an Option—Sample User Dialog

Select Systems Manager Menu Option: <span class="mark">MENU \<Enter\></span> Management

Select Menu Management Option: <span class="mark">EDIT OPTIONS \<Enter\></span>

Select OPTION to edit: <span class="mark">XQHELP-MENU \<Enter\></span> Help Processor

NAME: XQHELP-MENU// <span class="mark">^HELP FRAME \<Enter\></span>

HELP FRAME: <span class="mark">XQHELP \<Enter\></span>

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-menu-manager-user-guide/034.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      |             | TBDTBD |

<span id="_Toc207462637" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-menu-manager-user-guide/035.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-menu-manager-user-guide/036.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.