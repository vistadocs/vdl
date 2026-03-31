---
title: "Kernel 8.0 Systems Management: Signon/Security User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: Signon/Security"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: 
  - 3
security_keys: []
menu_options: 39
description: 
audience: 
keywords: 
  - span
  - access
  - strong
  - class
  - security
  - kernel
  - mark
  - code
  - signon
  - table
page_count: 0
word_count: 33209
section_count: 21
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Signon/Security User Guide
---

![](kernel-8-0-systems-management-signon-security-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-signon-security-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref332704228" class="anchor"></span>Table 1: User’s Toolbox Menu Options and Documentation References</p></caption>
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
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Signon/Security User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref332704228" class="anchor"></span>Table 1: User’s Toolbox Menu Options and Documentation References

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="List_of_Figures" class="anchor"></span>List of Figures

<span id="List_of_Tables" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

How to Use this Manual

![](kernel-8-0-systems-management-signon-security-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Signon/Security: User Interface](#signonsecurity-user-interface)
  - [Signing On](#signing-on)
    - [Defining a Strong Verify Code](#defining-a-strong-verify-code)
    - [LOGIN Menu Template](#login-menu-template)
    - [Signon Shortcuts](#signon-shortcuts)
    - [Normal Signoff](#normal-signoff)
    - [Abnormal Signoff and Error Handling](#abnormal-signoff-and-error-handling)
    - [Terminal Type Prompt](#terminal-type-prompt)
  - [Escaping from a Jumbled Screen](#escaping-from-a-jumbled-screen)
  - [Alerts](#alerts)
  - [User’s Toolbox Menu](#users-toolbox-menu)
  - [Change my Division Option](#change-my-division-option)
  - [Edit User Characteristics Option](#edit-user-characteristics-option)
  - [Display User Characteristics Option](#display-user-characteristics-option)
  - [Switch UCI Option](#switch-uci-option)
  - [Summary](#summary)
- [Signon/Security: System Management](#signonsecurity-system-management)
  - [Signon Process](#signon-process)
    - [Introductory Text](#introductory-text)
    - [Parameters Checked during Signon](#parameters-checked-during-signon)
    - [XU USER SIGN-ON Option](#xu-user-sign-on-option)
    - [XU USER START-UP Option](#xu-user-start-up-option)
    - [Clear all users at startup Option](#clear-all-users-at-startup-option)
    - [Enabling and Disabling Logons](#enabling-and-disabling-logons)
  - [Adding New Users](#adding-new-users)
    - [Add a New User to the System Option](#add-a-new-user-to-the-system-option)
    - [Grant Access by Profile Option](#grant-access-by-profile-option)
    - [Security Forms](#security-forms)
  - [Edit an Existing User Option](#edit-an-existing-user-option)
    - [Editable Field Attributes](#editable-field-attributes)
    - [ScreenMan Forms](#screenman-forms)
    - [Additional Attributes Editable by Users](#additional-attributes-editable-by-users)
    - [Edit User Characteristics Form and Template](#edit-user-characteristics-form-and-template)
  - [Deactivating and Reactivating Users](#deactivating-and-reactivating-users)
    - [Deactivating Users](#deactivating-users)
    - [Automatically Deactivating Users](#automatically-deactivating-users)
    - [Purging Mail and Security Keys for Inactive Users](#purging-mail-and-security-keys-for-inactive-users)
    - [Reactivating Users](#reactivating-users)
  - [User Management Menu](#user-management-menu)
    - [Find a User Option](#find-a-user-option)
    - [Proxy User List Option](#proxy-user-list-option)
    - [List Users Option](#list-users-option)
    - [Print Sign-on Log Option](#print-sign-on-log-option)
    - [Proxy (Connector) Detail Report Option](#proxy-connector-detail-report-option)
    - [Proxy (Connector) Inquire Option](#proxy-connector-inquire-option)
    - [Release user Option](#release-user-option)
    - [Remote Access User Sign-on Log Option](#remote-access-user-sign-on-log-option)
    - [User Inquiry Option](#user-inquiry-option)
    - [User Status Report Option](#user-status-report-option)
    - [Users with Foreign Visits Option](#users-with-foreign-visits-option)
  - [Signon Audits](#signon-audits)
    - [Signon Statistics](#signon-statistics)
    - [Failed Access Attempts Audit](#failed-access-attempts-audit)
    - [Purge Old Access and Verify Codes](#purge-old-access-and-verify-codes)
- [File Access Security](#file-access-security)
  - [File Access Security User Interface](#file-access-security-user-interface)
  - [File Access Security System Management](#file-access-security-system-management)
    - [When is File Access Security Checked?](#when-is-file-access-security-checked)
    - [What in VA FileMan is Still Protected by the File Manager Access Code?](#what-in-va-fileman-is-still-protected-by-the-file-manager-access-code)
    - [Purpose for Granting File Access](#purpose-for-granting-file-access)
    - [Who Needs File Access?](#who-needs-file-access)
    - [Levels of File Access Security](#levels-of-file-access-security)
    - [Audit Access to Files](#audit-access-to-files)
    - [How to Grant File Access](#how-to-grant-file-access)
    - [Using the File Access Options](#using-the-file-access-options)
  - [Running the File Access Security Conversion](#running-the-file-access-security-conversion)
    - [Advantages](#advantages)
    - [Advance Preparation for the Conversion](#advance-preparation-for-the-conversion)
    - [Summary of the File Access Security Conversion](#summary-of-the-file-access-security-conversion)
    - [File Access Security Conversion Instructions](#file-access-security-conversion-instructions)
    - [After the File Access Security Conversion](#after-the-file-access-security-conversion)
- [Electronic Signatures](#electronic-signatures)
  - [Electronic Signatures User Interface](#electronic-signatures-user-interface)
    - [Electronic Signature code Edit Option](#electronic-signature-code-edit-option)
  - [Electronic Signature System Management](#electronic-signature-system-management)
    - [Electronic Signature Block Edit Option](#electronic-signature-block-edit-option)
    - [Clear Electronic signature code Option](#clear-electronic-signature-code-option)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Signon/Security User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. Signon/Security is the Kernel module that regulates access to the VistA M-based menu system. It performs several checks to determine whether access can be permitted at a particular time. A log of signons is maintained.

# Signon/Security: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step you take each time you access the computer system is called signing on. When you sign on to the VistA computer system, you are required to use the appropriate user credentials:

- Access and Verify Codes.
- 2-Factor Authentication (2FA)—Digital certificate in a VA-approved smart card, such as the Personal Identification Verification (PIV) smart card plus a Personal Identification Number (PIN).

![](kernel-8-0-systems-management-signon-security-user-guide/004.png) NOTE: Access and Verify Codes is the fallback signon in cases when 2FA signon is *not* available.

These credentials identify you to the computer system, and, as these credentials are private to you, serve to prevent unauthorized access to your account.

![](kernel-8-0-systems-management-signon-security-user-guide/005.png) NOTE: Because Access and Verify Code authentication is less secure than 2FA, their use may be deprecated and disabled at some future date.

You are shielded from most steps in the signon process. In the background, Kernel’s Signon/Security does the following:

- Establishes the proper environment.
- Records and monitors the signon event.
- Takes you to Menu Manager, which presents a list of menu options that let you interact with other parts of Kernel and software applications.

When you complete a session on the computer system, you sign out to exit.

## Signing On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To authenticate yourself to VistA (Kernel’s “front door”), you need to sign onto the system. The user signon (authentication) interface varies based on the type of Vista application software being run:

- 2-Factor Authentication (2FA)—VistA supports delegated 2-Factor Authentication (2FA) through Identity and Access Management (IAM). A smart card containing Public Key Infrastructure (PKI) digital certificates combined with a private security is used to authenticate and uniquely identify the user. The user is prompted for a Personal Identification Number (PIN) to unlock the security key and authenticate. This method of authentication provides a higher level of security and takes precedence over all other forms of authentication. As client applications are migrated to 2-Factor Authentication (2FA), other forms of authentication may be deprecated and disabled.
- Character User Interface (CHUI)-based applications—This includes M-based roll-and-scroll applications used to access Kernel on the VistA M Server (such as Laboratory, Pharmacy). With this type of authentication interface, users are first prompted with an “ACCESS CODE:” prompt. Entering an Access Code and pressing the \<Enter\> key brings up the “VERIFY CODE:” prompt.

![](kernel-8-0-systems-management-signon-security-user-guide/006.png) REF: For a sample of the roll-and-scroll signon prompts, please see [Figure 1](#_Ref332703265).

- Graphical User GUI client/server applications—This includes rich client or client/server applications used to access Kernel on the VistA M Server through RPC Broker (Delphi/Pascal)- or VistALink (Java)-based components (such as Computerized Patient Record System \[CPRS\] or Care Management). With this type of authentication interface, users are presented with a GUI signon dialog box. Users can click in or tab to the Access and Verify Code entry fields and press OK.

![](kernel-8-0-systems-management-signon-security-user-guide/007.png) REF: For a sample of the RPC Broker signon dialog box and more information on RPC Broker, see the RPC Broker documentation located on the VA Software Document Library (VDL) at: [VDL RPC Broker Application Documents](http://www.va.gov/vdl/application.asp?appid=23)

- Web-based applications—This includes Web-based applications that use a client Web browser and Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) to access Kernel on the VistA M Server (such as Blind Rehab). With this type of authentication interface, users are presented with a GUI signon dialog Web page. Users can click in or tab to the Access and Verify Code entry fields and press Login.

![](kernel-8-0-systems-management-signon-security-user-guide/008.png) REF: For a sample of the KAAJEE signon dialog Web page and more information on KAAJEE, see the KAAJEE documentation located on the VA Software Document Library (VDL) at: [VDL KAAJEE Application Documents](http://www.va.gov/vdl/application.asp?appid=151)

[Figure 1](#_Ref332703265) shows a sample of the roll-and-scroll signon prompts. Your Access Code establishes your unique identity to Kernel. Your matching Verify Code corroborates your identity completing the VistA Kernel authentication process. Asterisks only are displayed when you enter your Access and Verify Codes, so that the actual characters are *not* displayed (echoed back) on the screen. Codes are encrypted after they are entered and compared with the encrypted stored values for a match.

![](kernel-8-0-systems-management-signon-security-user-guide/009.png) REF: For a description of valid and strong Verify Code, see the “[Defining a Strong Verify Code](#defining-a-strong-verify-code)” section.

<span id="_Ref332703265" class="anchor"></span>Figure 1: Signing on to VistA—Sample Roll-and-Scroll User Authentication Dialog

ACCESS CODE: <span class="mark">\*\*\*\*\*\*\*\*</span>

VERIFY CODE: <span class="mark">\*\*\*\*\*\*\*\*</span>

Device: \_TNA8628: <span class="mark">\<Enter\></span>

<span class="mark">Not a valid ACCESS CODE/VERIFY CODE pair.</span>

ACCESS CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

VERIFY CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

Good evening *FRIEND* You last signed on Apr 21,1992 at 07:57

There was 1 unsuccessful attempt since you last signed on:

You were last executing the 'MailMan Menu' menu option.

Do you wish to resume? YES//

Entering a valid Access and Verify Code combination completes the signon authentication process and takes you beyond Signon/Security into Kernel’s Menu Manager (or other security role-based access keys) used to authorize your appropriate level of access to data or application functionality.

If you have *not* been assigned a primary menu, Kernel displays a message indicating that access is *not* allowed and signs you out from the computer system. Similarly, if your primary menu has been marked as “out-of-order” (an option attribute), Kernel also denies you access (see [Figure 2](#_Ref158528556)).

![](kernel-8-0-systems-management-signon-security-user-guide/010.png) REF: For more information on primary menus, see the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf).

<span id="_Ref158528556" class="anchor"></span>Figure 2: Access Denied Due to No Primary Menu or Menu “Out of Order” Message

ACCESS CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

VERIFY CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

<span class="mark">No access allowed for this user.</span>

### Defining a Strong Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While Access Codes are a unique identifier (that is username) for your user record in Kernel’s NEW PERSON (#200) file, Verify Codes are secret passwords assuring that the person signing on is the one for whom the user record was established. You rarely need to be issued a new Access Code, but you *must* change your Verify Code (that is password) if you suspect that someone else has used it to gain access to the system or when your Verify Code has expired (that is every 90 days or less). You can change your Verify Code with the Edit User Characteristics \[XUEDITSELF\] option, which is available from the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu) User’s Toolbox \[XUSERTOOLS\] menu.

![](kernel-8-0-systems-management-signon-security-user-guide/011.png) NOTE: Kernel records all signons to VistA using appropriate user credentials through either of the following methods:

- Access and Verify Codes.
- 2-Factor Authentication (2FA—Digital certificate in a VA-approved smart card, such as the Personal Identification Verification (PIV) smart card plus a Personal Identification Number (PIN).  
    
  Once a user starts using PIV for all access to VistA, their Verify Code will expire after 90 days. An expired Verify Code will *not* prevent access to VistA through PIV+PIN. If for some reason the user later needs to access VistA with their Access and Verify Codes, the first time they sign on with their expired Verify Code they will be prompted to reset their Verify Code before continuing.

![](kernel-8-0-systems-management-signon-security-user-guide/012.png) REF: For more information on using the Edit User Characteristics \[XUEDITSELF\] option to reset the Verify Code, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

![](kernel-8-0-systems-management-signon-security-user-guide/013.png) REF: For more information on Verify Code expiration dates, see Section [3.1.2.9](#lifetime-of-verify-code), “[LIFETIME OF VERIFY CODE](#lifetime-of-verify-code).”

As of Kernel patch XU\*8.0\*180, *strong* Access and Verify Codes *must* adhere to the following criteria:

- Access and Verify Codes *cannot* be identical.
- Verify Codes (that is passwords) *must* be at least 8 characters in length. A *minimum* of 15 characters is *recommended* and may be enforced later.
- Strong passwords in general contain at least three of the following four-character types:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters/symbols that are neither letters nor numbers (such as*-, \_,*\#, &, \$, \*, @)

![](kernel-8-0-systems-management-signon-security-user-guide/014.png) NOTE: The caret (^) is a reserved symbol and *cannot* be used as part of a Verify Code. Also, some *non*-VistA-based systems restrict certain special characters/symbols used as part of a username or password.

Because VistA is case-insensitive, VistA only has three sets of characters from which to build a strong Verify Code (that is password):

- Letters (of any case)
- Numbers
- Special characters/symbols that are neither letters nor numbers (such as*-, \_,*\#, &, \$, \*, @)

![](kernel-8-0-systems-management-signon-security-user-guide/015.png) NOTE: Some *non*-VistA-based systems restrict certain special characters/symbols used as part of a username or password.

- Verify Codes *must* be changed at least every 90 days (or less). You *must* change your Verify Code at periodic intervals as specified by the system administrators. Information systems shall *not* permit re-assignment of the last three passwords used. When required, you are prompted during signon to pick a new Verify Code.

![](kernel-8-0-systems-management-signon-security-user-guide/016.png) REF: For more information on Verify Code expiration dates, see Section [3.1.2.9](#lifetime-of-verify-code), “[LIFETIME OF VERIFY CODE](#lifetime-of-verify-code).”

- Accounts that have been inactive for 90 days shall be disabled.
- To preclude password guessing, an intruder lockout feature shall suspend accounts after five invalid attempts to log on:
  - Where around-the-clock system administration service is available, system administrator intervention shall be required to clear a locked account.
  - Where around-the-clock system administration service is *not* available, accounts shall remain locked out for at least ten minutes.

![](kernel-8-0-systems-management-signon-security-user-guide/017.png) NOTE: These rules are taken from the *VA Account and Password Management Interim Policy* document.  
  
All of these restrictions are enforced whenever Access or Verify Codes are created or changed.  
  
These changes were made to meet [VA Directive 6500](http://www1.va.gov/vapubs/viewPublication.asp?Pub_ID=637&FType=2) and [VA Handbook 6500](http://www1.va.gov/vapubs/viewPublication.asp?Pub_ID=56).

![](kernel-8-0-systems-management-signon-security-user-guide/018.png) REF: For more tips and general advice regarding Access and Verify Codes and security in general, see the *Kernel Security Tools Manual*.

#### Why Longer Passwords?

Passwords used to access VA systems *must* be at least 8 characters long because longer passwords are stronger, and thus, harder to guess than shorter ones. While VistA currently supports 8-character passwords (Verify Codes), current security policy *recommends* that a minimum of 15 characters be used. This policy will be enforced in a future VistA Kernel patch.

The more tries it takes a hacker or a program to guess a password, the more secure the system is. Adding just one character to the length of a password greatly increases the difficulty of guessing the password.

For an 8-character password made up of letters and numbers (assuming you can repeat characters and that there are no restrictions, such as requiring the first character to be a letter), there are 36 possibilities for the first position, 36 possibilities for the second position, 36 possibilities for the third position, and so on. Thus, there are 36 x 36 x 36 x 36 x 36 x 36 x 36 x 36 = 2,821,109,907,456 possibilities for an 8-character password.

If you have forgotten your Verify Code (password), the site’s Information Security Officer (ISO) should delete the existing Verify Code and instruct you to sign on again. At the “Verify code” prompt simply press the \<Enter\> key without making any other entries. You are prompted to enter a new Verify Code and then re-prompted to enter the same Verify Code again as confirmation. If you do *not* want to bother inventing a Verify Code, entering a question mark (?) at the “Verify code” prompt displays a possible although cryptic choice (such as DKMl&493). Entering a question mark a second time displays another choice. When you log off, you’re reminded to remember the new Verify Code for use at your next signon.

### LOGIN Menu Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can execute a script of options on your first signon of the day by having a MENU template called LOGIN.

![](kernel-8-0-systems-management-signon-security-user-guide/019.png) REF: For more information, see the “Menu Manager: User Interface” section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf#Menu_Manager_User_Interface).

### Signon Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In roll-and-scroll VistA, to reach the primary menu in one step at the “ACCESS CODES:” prompt, you can enter the Access and Verify Code as one string separated by a semicolon:

<span id="_Toc193181620" class="anchor"></span>Figure 3: Entering the Access and Verify Codes at the Same Time

ACCESS CODES: <span class="mark">ACCESSCODE;VERIFYCODE</span><span class="mark">\<Enter\></span>

Good afternoon. You last signed on today at 12:00

To “jump start” directly to a particular option, you can specify the name of an option after another semicolon:

<span id="_Toc193181621" class="anchor"></span>Figure 4: Entering the Access and Verify Codes at the Same Time and Jumping Directly to a Specified Option

ACCESS CODES: <span class="mark">ACCESSCODE;VERIFYCODE;INTRO \<Enter\></span>

Good afternoon. You last signed on today at 12:00

INTROductory text edit

To force the Kernel query of the terminal type identity, you can include a colon anywhere in the string.

![](kernel-8-0-systems-management-signon-security-user-guide/020.png) REF: If you want to avoid the terminal type query, see the “[Terminal Type Prompt](#terminal-type-prompt)” section.

### Normal Signoff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you complete a session on the computer system, you should sign off the system so that no one can come along and use the computer system under your identity. There are several ways you can sign off the system.

<span id="_Toc193181622" class="anchor"></span>Figure 5: System Commands: Menu Options for Signoff

SYSTEM COMMAND OPTIONS \[XUCOMMAND\]

Halt \[XUHALT\]

Continue \[XUCONTINUE\]

Restart Session \[XURELOG\]

There are multiple ways to sign off:

- Enter “halt” at any menu prompt. When you sign off using “halt,” at next signon, after entering Access and Verify Codes, your normal primary menu is your first menu.
- Enter “continue.” At your next signon, after entering Access and Verify Codes, your last-used menu when you signed off is your first menu for that session.
- If remotely connected by a modem or other network device, enter “restart” to sign out of Kernel without dropping the communication line.
- Sign off without using any of these shortcuts simply by pressing \<Enter\> at each menu prompt to step back up the menu pathway and finally exit.

![](kernel-8-0-systems-management-signon-security-user-guide/021.png) REF: For more information on menus and menu prompts, see the “Menu Manager: User Interface” section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf#Menu_Manager_User_Interface).

### Abnormal Signoff and Error Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you encounter an error while using the VistA computer system, Kernel traps it, issues the message “Sorry ‘bout that”, and attempts to return you to your primary menu. Kernel can recover from most error conditions, and given a suitable environment permits you to continue. Some error conditions, however, cause an abnormal exit, which immediately logs you off the computer system. When this happens, you can sign on again if you still need to use the computer system.

### Terminal Type Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When signing on, you may be prompted to enter a terminal type. You should *not* see this prompt very often, however, since Kernel usually can identify your terminal type without needing to prompt you to enter one. If you are prompted, you should enter the name of the actual terminal type to use (such asC-VT220). The entered terminal type tells Kernel how to support screen-oriented and other enhanced displays. If unusual circumstances arise and the wrong terminal type is in effect, you can redefine it by using the Edit User Characteristics \[XUEDITSELF\] option (available through the User’s Toolbox \[XUSERTOOLS\] menu).

The Edit User Characteristics \[XUSEREDITSELF\] option lets you edit a setting (ASK DEVICE TYPE AT SIGN-ON) that allows you to decide whether to bypass the usual terminal type query. If you always work at the same terminal and want to save a small amount of time during the signon process, you can set ASK DEVICE TYPE AT SIGN-ON to DON’T ASK. Kernel then assumes that your last terminal type should be used as the default.

If you have ASK DEVICE TYPE AT SIGN-ON set to DON’T ASK and then sign on using a terminal whose terminal type is different from the one normally used, you should sign on by including a colon (:) after your Access Code. This forces Kernel to query the terminal for its identity. Alternatively, once signed on, you could:

- Invoke the Edit User Characteristics \[XUSEREDITSELF\] option to change your terminal type to the one currently in use.  
    
  Or
- Use this option to reset the ASK DEVICE TYPE AT SIGN-ON question to ASK, log off and sign back on (whereby Signon/Security obtains the correct terminal type identification).

![](kernel-8-0-systems-management-signon-security-user-guide/022.png) REF: For more information on the Edit User Characteristics \[XUEDITSELF\] option, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

## Escaping from a Jumbled Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One consequence of your signon terminal type *not* matching the actual one being used is that full-screen display could appear jumbled. To escape from a ScreenMan form (such as Edit User Characteristics), all you need to do is enter two carets (^), each followed by the \<Enter\> key. To escape from VA FileMan’s Screen Editor, you should press \<PF1\>E to exit.

## Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After signing on, you could be presented with an alert notice just before the menu prompt. If so, you need to pick the View Alerts \[XQALERT\] option for viewing alerts to take care of urgent, pending matters.

![](kernel-8-0-systems-management-signon-security-user-guide/023.png) REF: For more information about alerts, see the “Alerts” section in the [*Kernel 8.0 Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf#Alerts).

<span id="_Toc193181623" class="anchor"></span>Figure 6: System Commands: View Alerts Option

SYSTEM COMMAND OPTIONS ... \[XUCOMMAND\]

View Alerts "VA" \[XQALERT\]

## User’s Toolbox Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User’s Toolbox \[XUSERTOOLS\] menu is available from any menu prompt, by entering the toolbox synonym (such as “TBOX”) or “User’s Toolbox.” It makes available, from one menu, some of the most frequently used Kernel options, as shown in [Figure 7](#_Ref511383502).

<span id="_Ref511383502" class="anchor"></span>Figure 7: User’s Toolbox Menu Options

Select User's Toolbox Option:

Change my Division \[XUSER DIV CHG\]

Display User Characteristics \[XUUSERDISP\]

Edit User Characteristics \[XUSEREDITSELF\]

Electronic Signature code Edit \[XUSESIG\]

Menu Templates ... \[XQTUSER\]

Spooler Menu ... \[XU-SPL-MENU\]

\*\*\> Locked with XUMGR

Switch UCI \[XU SWITCH UCI\]

TaskMan User \[XUTM USER\]

User Help \[XUUSERHELP\]

<u>Table 1</u> lists the options contained in the User’s Toolbox \[XUSERTOOLS\] menu and the sections and guides where each option is described:

<table>
<caption><p><span id="_Ref236731957" class="anchor"></span>Table 2: Edit User Characteristics Option—Editable Fields</p></caption>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Text</th>
<th>Section Described</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Change my Division [XUSER DIV CHG]</td>
<td><a href="#signonsecurity-user-interface">Signon/Security: User Interface</a></td>
</tr>
<tr class="even">
<td>Display User Characteristics [XUUSERDISP]</td>
<td><a href="#signonsecurity-user-interface">Signon/Security: User Interface</a></td>
</tr>
<tr class="odd">
<td>Edit User Characteristics [XUSEREDITSELF]</td>
<td><a href="#signonsecurity-user-interface">Signon/Security: User Interface</a></td>
</tr>
<tr class="even">
<td>Electronic Signature code Edit [XUSESIG]</td>
<td><u>Electronic Signatures</u></td>
</tr>
<tr class="odd">
<td>Menu Templates [XU-SPL-MENU]</td>
<td>“<strong>Menu Manager: User Interface</strong>” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf#Menu_Manager_User_Interface"><em>Kernel 8.0 Systems Management: Menu Manager User Guide</em></a></td>
</tr>
<tr class="even">
<td>Spooler Menu [XU-SPL-MENU]<br />
(locked with <strong>XUMGR</strong> security key)</td>
<td>“<strong>Spooling</strong>” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf#Spooling"><em>Kernel 8.0 Systems Management: Device Handler User Guide</em></a></td>
</tr>
<tr class="odd">
<td>Switch UCI [XU SWITCH UCI]</td>
<td><a href="#signonsecurity-user-interface">Signon/Security: User Interface</a></td>
</tr>
<tr class="even">
<td>TaskMan User [XUTM USER]</td>
<td>“<strong>TaskMan: User Interface</strong>” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf#TaskMan_User_Interface"><em>Kernel 8.0 Systems Management: TaskMan User Guide</em></a></td>
</tr>
<tr class="odd">
<td>User Help [XUUSERHELP]</td>
<td>(accesses online help)</td>
</tr>
</tbody>
</table>

<span id="_Ref236731957" class="anchor"></span>Table 2: Edit User Characteristics Option—Editable Fields

## Change my Division Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change my Division \[XUSER DIV CHG\] option allows users to select from a list of divisions, if any, stored for that user in the NEW PERSON (#200) file.

## Edit User Characteristics Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit User Characteristics \[XUSEREDITSELF\] option is one of the options available from the User’s Toolbox \[XUSERTOOLS\] menu. It allows you to define some characteristics of your online environment through ScreenMan, as shown in [Figure 8](#_Ref456877428):

<span id="_Ref456877428" class="anchor"></span>Figure 8: Edit User Characteristics Option—ScreenMan Form

EDIT USER CHARACTERISTICS

NAME: XUUSER,ONE PAGE 1 OF 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

INITIAL: ONE PHONE:

NICK NAME: ONE OFFICE PHONE: (555) 555-5555

TITLE: DOCTOR VOICE PAGER:

DIGITAL PAGER:

ASK DEVICE TYPE AT SIGN-ON: DON'T ASK

AUTO MENU: YES, MENUS GENERATED

TYPE-AHEAD: ALLOWED

TEXT TERMINATOR:

PREFERRED EDITOR: SCREEN EDITOR - VA FILEMAN

NETWORK USERNAME: VHAIXXXUUSERO

ELECTRONIC SIGNATURE CODE: \<Hidden\>

Want to edit VERIFY CODE (Y/N): DISABILITY USER: No \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

To Exit form and save changes, enter: \<PF1\>E

To Quit form without saving changes, enter: \<PF1\>Q

Press \<PF1\>H for help Insert

<u>Table 2</u> lists several NEW PERSON (#200) file field values that you can edit with the Edit User Characteristics \[XUEDITSELF\] option:

<table>
<caption><p><span id="_Ref236554578" class="anchor"></span>Table 3: Edit an Existing User Option—Editable Field Attributes</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INITIAL (#1)</td>
<td>Enter your initials, which can serve as an alternate way for users to specify your account (such as when sending mail to you).</td>
</tr>
<tr class="even">
<td>NICK NAME (#13)</td>
<td>Enter a nick name, which can serve as an alternate way for users to specify your account (such as when sending mail to you).</td>
</tr>
<tr class="odd">
<td>TITLE (#8)</td>
<td>Enter a title from a given list of choices or enter a new TITLE.</td>
</tr>
<tr class="even">
<td><p>Telephone Contact Information:</p>
<ul>
<li><p>PHONE (HOME) (#.131)</p></li>
<li><p>OFFICE PHONE (#.132)</p></li>
<li><p>VOICE PAGER (#.137)</p></li>
<li><p>DIGITAL PAGER (#.138)</p></li>
</ul></td>
<td>Enter the appropriate phone numbers in the fields indicated.</td>
</tr>
<tr class="odd">
<td>ASK DEVICE TYPE AT SIGN-ON (#200.05)</td>
<td>This field controls whether Kernel should determine what kind of terminal you are using when you sign on. If this is set to <strong>DON’T ASK</strong>, Kernel assumes you are using the same kind of terminal you used the last time you signed on. This can cause problems if you are using a different kind of terminal (screen displays may <em>not</em> work properly), so this should normally be set to <strong>ASK</strong>.</td>
</tr>
<tr class="even">
<td>AUTO MENU (#200.06)</td>
<td>This field determines whether, in the menu system, a list of items on the current menu is displayed with the menu prompt. Beginning users should usually set AUTO MENU to <strong>YES</strong>, so that they can see menu items for each menu. Experienced users who are familiar with their menus may prefer to set this field to <strong>NO</strong>, which makes menu displays speedier, since individual items on each menu are <em>not</em> displayed.</td>
</tr>
<tr class="odd">
<td>TYPE-AHEAD (#200.09)</td>
<td>This field controls whether characters you type faster than the system can process end up being processed or not. Normally you should set TYPE-AHEAD to <strong>YES</strong>, so that keystrokes you enter are <em>not</em> lost due to system slowness.</td>
</tr>
<tr class="even">
<td>TEXT TERMINATOR (#31.2)</td>
<td><p>The TEXT TERMINATOR is a setting used by VA FileMan’s Line Editor. When you are using the Line Editor and are importing text from an external source, you may <em>not</em> want a blank line to indicate the end-of-file, which could prematurely terminate the text transfer. By default, the TEXT TERMINATOR in VA FileMan’s Line Editor is the carriage return character (<strong>&lt;Enter&gt;</strong>). Setting this to another character string, like <strong>ZZ</strong> (something that is <em>not</em> encountered in the target text) can permit downloading without interruption. If you change the setting of the TEXT TERMINATOR from the default of the carriage return character, you need to remember your TEXT TERMINATOR when using the Line Editor; otherwise, you are unable to exit the Line Editor.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/024.png) <strong>REF:</strong> For more information on the TEXT TERMINATOR, see the <em>VA FileMan User Manual</em>.</p></td>
</tr>
<tr class="odd">
<td>PREFERRED EDITOR (#31.3</td>
<td>Users can choose which text editor Kernel uses when you edit <strong>WORD-PROCESSING</strong> fields on the system. You can choose any editor defined on your system.</td>
</tr>
<tr class="even">
<td>NETWORK USERNAME (#501.1)</td>
<td><p>Enter your network username. This is the username that is used by the Windows Active Directory (AD). It allows VISN data extracts to link the VistA user with their network username.</p>
<p>Format:</p>
<p><strong>“VHA” + 3-character station ID + first 5 characters of last name + first character of first name</strong></p>
<p>For example, for user <strong>One Xuuser</strong> at Station ID <strong>999</strong>, the network username would be:</p>
<blockquote>
<p><strong>VHA999XUUSEO</strong></p>
</blockquote>
<p>Holders of the <strong>XUMGR</strong> security key can override this field.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/025.png) <strong>NOTE:</strong> This field was added to the NEW PERSON (#200) file with Kernel patch XU*8.0*514.</p></td>
</tr>
<tr class="odd">
<td>ELECTRONIC SIGNATURE CODE (#20.4)</td>
<td>Enter a new electronic signature code. This is a code (like a password) used to electronically sign documents within VistA. When you press <strong>Enter</strong>, the code is hidden for security purposes.</td>
</tr>
<tr class="even">
<td>VERIFY CODE (#7.2)</td>
<td>Users can change their Verify Code by answering <strong>YES</strong> to this field. First enter your current Verify Code; then, enter a new Verify Code. You are asked to confirm the new Verify Code by entering it a second time; if you confirm it, the new Verify Code takes effect immediately.</td>
</tr>
<tr class="odd">
<td>DISABILITY USER (#508.1</td>
<td><p>Users can set this field value to <strong>Yes</strong> or <strong>No</strong>. If the user has a visual disability, set this field to <strong>Yes</strong>. Applications should check this field value for visually disabled users for Section 508 compliance.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/026.png) <strong>NOTE:</strong> This field was added to the NEW PERSON (#200) file with Kernel Patch XU*8.0*741. The <strong>DISABILITY USER</strong> display field was added to the “<strong>EDIT USER CHARACTERISTICS</strong>” screen with Kernel Patch XU*8.0*753.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref236554578" class="anchor"></span>Table 3: Edit an Existing User Option—Editable Field Attributes

## Display User Characteristics Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display User Characteristics \[XUUSERDISP\] option, like the Edit User Characteristics \[XUSEREDITSELF\] option, is an option in the User’s Toolbox \[XUSERTOOLS\] menu. It prints out a description of many of the characteristics of your current computing environment, including some of the characteristics that can be set through the Edit User Characteristics \[XUSEREDITSELF\] option.

<span id="_Toc193181627" class="anchor"></span>Figure 9: Display User Characteristics Option—Sample Output and User Dialog

XUUSER,TWO (#9999) DEVICE: DEVICE: TELNET (\$I: TNA730:) JOB: 541754169

ENVIRONMENT ATTRIBUTES

----------- -----------

Site ........ TESTSITE Type-ahead ....... Y

UCI ......... KRN,KDE Time-out ......... 300

Signed on ... 08:48 Fileman code(s) .. \#

Terminal type C-VT100

Person Class: Physicians (M.D. and D.O.)

Physician/Osteopath

Pathology, Anatomic

KEYS HELD

---------

XMMGR XUPROG XUPROGMODE

MENU PATH

---------

SYSTEM COMMAND OPTIONS (XUCOMMAND)

User's Toolbox (XUSERTOOLS)

Display User Characteristics (XUUSERDISP)

'^' to escape, \<CR\> to view Mailman user info: <span class="mark">\<Enter\></span>

Current Banner: Technical Writer

Last used MailMan: 07/12/06@15:09

NEW messages: 274 (274 in the IN basket)

Office phone: (555) 555-5555

Fax: (555) 555-5555

Add'l phone: (555) 555-5555

Add'l phone: (555) 555-5555

Introduction:

My name is One Xmuser and I am one of the Technical Writers for the

Common Services (CS) products/projects (such as Broker, Components,

Kernel, VA FileMan, MailMan, Toolkit).

Mail Groups:

*\<REDACTED\>* STAFF (Public)

KERNEL PROGRAMMERS (Public)

## Switch UCI Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Switch UCI \[XU SWITCH UCI\] option allows users to select from a list of UCIs, if any, stored for that user in the NEW PERSON (#200) file.

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA’s Kernel’s Signon/System Security module provides the means for signing into Kernel with a unique identity. Once you complete the signon process, you are sent to Kernel’s menu system, where you can run any option your system manager has placed in your menus. When you finish a computer session, always be sure to sign off; this protects your account from misuse by someone else.

# Signon/Security: System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the system management tools for Kernel’s Signon/Security module.

## Signon Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If signons are enabled, as shown in the Signon Flow Chart in [Figure 13](#_Ref84929982), the signon process begins with a gathering of information from the KERNEL SYSTEM PARAMETERS (#8989.3) file and then from the DEVICE (#3.5) file to determine whether to allow signon for this session and, if so, how to create an appropriate environment. If, for example, the MAX SIGNON ALLOWED limit has been reached, the signon attempt fails. If the current device is tied to a routine (as specified in the TIED ROUTINE field of the DEVICE \[#3.5 file\]), that routine is executed, and the session is halted. If *not*, the user is prompted for Access and Verify Codes. After a successful signon, attributes for that user are then retrieved from the NEW PERSON (#200) file. Signon/Security then sends the user to Menu Manager. If a primary menu is associated with the device (PRIMARY MENU OPTION field in the DEVICE \[#3.5\] fil), that menu is presented. Otherwise, the user’s primary menu is presented. If the user does *not* have a primary menu (the PRIMARY MENU OPTION field in the NEW PERSON \[#200\] file is NULL), the session is halted.

The signon flow chart in this section (see [Figure 13](#_Ref84929982)) illustrates the procedural steps taken by Kernel’s Signon/Security system to determine whether to permit signons and, if so, how to create an appropriate computing environment. Typically, after site parameters and device characteristics are checked:

1.  System prompts the user for their Access and Verify Codes. Alternatively, client applications that are enabled to use 2-Factor Authentication (2FA) will automatically enter a Security Assertion Mark-up Language (SAML) token obtained from Identity and Access Management (IAM) instead of an Access and Verify Code to authenticate and identify the user.
1.  System collects user attributes.
2.  System presents a primary menu prompt to the user.

### Introductory Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before gathering system parameters or prompting for Access and Verify Codes, Signon/Security displays contents of the INTRO TEXT field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. The text can be edited with the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option or with the Introductory text edit \[XUSERINT\] option, an option specially designed for this purpose).

<span id="_Toc193181628" class="anchor"></span>Figure 10: Introductory text edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

<span class="mark">Introductory text edit</span> \[XUSERINT\]

### Parameters Checked during Signon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various parameters are checked as an initial step in the signon process. The KERNEL SYSTEM PARAMETERS (#8989.3) file stores the default values for most of the parameters. Values for critical fields should be defined by system administrators when Kernel is installed. The values in the KERNEL SYSTEM PARAMETERS (#8989.3) file can be edited any time, though, with the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option.

<span id="_Toc193181629" class="anchor"></span>Figure 11: Enter/Edit Kernel Site Parameters Option

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

Kernel Management Menu ... \[XUKERNEL\]

<span class="mark">Enter/Edit Kernel Site Parameters</span> \[XUSITEPARM\]

<span id="_Ref29190914" class="anchor"></span>Figure 12: Enter/Edit Kernel Site Parameters Option—ScreenMan Form 1

Kernel Site Parameter edit

DOMAIN:*\<REDACTED\>*.VA.GOV

DEFAULT \# OF ATTEMPTS: 3 AGENCY CODE: VA

DEFAULT LOCK-OUT TIME: 600

DEFAULT MULTIPLE SIGN-ON: Only one MULTIPLE SIGN-ON LIMIT: 2

DEFAULT AUTO-MENU: YES DEFAULT AUTO SIGN-ON: Disabled

DEFAULT LANGUAGE: ENGLISH SIGN-ON LOG RETENTION: 365

DEFAULT TYPE-AHEAD: YES STRICT TOKEN VALIDATION: NO

DEFAULT TIMED-READ (SECONDS): 300 BROKER TIMEOUT: 180

BYPASS DEVICE LOCK-OUT: NO CCOW TOKEN TIMEOUT:6000:

<u>LIFETIME OF VERIFY CODE</u>: 90 ASK DEVICE TYPE AT SIGN-ON: YES

<u>DEFAULT INSTITUTION</u>: SAN FRANCISCO

AUTO-GENERATE ACCESS CODES: NO

LOG RESOURCE USAGE?: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

#### Signon Attempts and Device Lock-out Times

The DEFAULT \# OF ATTEMPTS field in the KERNEL SYSTEM PARAMETERS (#8989.3) file holds the default limit of the number of times a user can try to enter a valid Access and Verify Code pair. When the limit is reached, Signon/Security is unresponsive for the duration specified by the DEFAULT LOCK-OUT TIME field. The values for number of attempts and lock-out time are overridden by any values for the current device specified by comparable fields in the DEVICE (#3.5) file.

Device values are ignored, however, if the BYPASS DEVICE LOCK-OUT site parameter in the KERNEL SYSTEM PARAMETERS (#8989.3) file is set to YES. In particular, the fields that are bypassed are:

- OUT-OF-SERVICE DATE
- SECURITY
- PROHIBITED TIMES FOR SIGN-ON

Device values are put back into effect for the current device if the DEVICE file’s PERFORM DEVICE CHECKING field is set to YES.

#### MAX SIGNON ALLOWED

One Kernel site parameter used in the initial signon screening is MAX SIGNON ALLOWED. It is a field within the VOLUME SET Multiple field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. Its value sets an upper limit for number of M processes (interactive, background, and system) that can run concurrently on the specified Volume Set or CPU. The TASKMAN JOB LIMIT, a field in the TASKMAN SITE PARAMETERS (#14.7) file, should be set to a number slightly lower than MAX SIGNON ALLOWED to leave room for a few interactive logons when TaskMan is busiest.

![](kernel-8-0-systems-management-signon-security-user-guide/027.png) NOTE: OpenVMS Sites: The OpenVMS interactive logins parameter (set by the DCL command SET LOGINS/INTERACTIVE) should be set to a number less than the Kernel MAX SIGNON ALLOWED to conserve system resources. If the OpenVMS limit is set too high in relation to the Kernel limit, users try to access Kernel only to be rejected when reaching Signon/Security. That means that they would waste system resources by creating a new OpenVMS process and activating a Caché image, all to no avail.  
  
REF: For more information about alerts, see “[Alerts](\l).”

#### PROHIBITED TIMES FOR SIGN-ON

Time periods can be specified, during which interval signons can be barred by device or by user. This is controlled by the PROHIBITED TIMES FOR SIGN-ON field in the DEVICE (#3.5) file and a comparable field in the NEW PERSON (#200) file.

<span id="_Ref84929982" class="anchor"></span>Figure 13: Kernel Signon Flow Chart

![](kernel-8-0-systems-management-signon-security-user-guide/028.png)

#### Multiple Sign-On Restriction

The DEFAULT MULTIPLE SIGN-ON field in the KERNEL SYSTEM PARAMETERS (#8989.3) file controls whether users can create two or more simultaneous sessions by signing on to more than one device. The setting is overridden by comparable fields in the DEVICE (#3.5) and NEW PERSON (#200) files, respectively. The value is checked at signon to prevent unauthorized multiple sessions.

If multiple signons are prohibited, problems can occur if users experience an abnormal exit such that the signon record *cannot* be cleared. To clear an individual user, use the [Release user](#release_user_option) \[XUSERREL\] option. To make sure all users are clear when the system is brought up after a crash, system administrators can use the Clear all users at startup \[XUSER-CLEAR-ALL\] option.

#### INTERACTIVE USER’S PRIORITY

The INTERACTIVE USER’S PRIORITY parameter in the KERNEL SYSTEM PARAMETERS (#8989.3) file should usually be left NULL. A setting here affects the job priority of interactive users and could result in poor response time.

#### ASK DEVICE TYPE AT SIGN-ON

The ASK DEVICE TYPE AT SIGN-ON parameter controls whether the user’s current device at signon is queried for its display attributes (DA). Thus, the correct terminal type can be identified without prompting the user.

It is *recommended* that you set ASK DEVICE TYPE AT SIGN-ON to ASK so that Signon/Security performs the DA query and allows the Device Handler to set up the correct terminal type attributes. This has become more important with the advent of screen control. VA FileMan’s Screen Editor and Screen Manager, for example, does *not* function properly if the terminal type recorded by Kernel fails to match the actual terminal type being used.

As with other parameters, the site default (ASK DEVICE TYPE AT SIGN-ON field in the KERNEL SYSTEM PARAMETERS \[#8989.3\] file) is overridden by a DON’T ASK setting for the device (like-named field in the DEVICE \[#3.5\] file), which would similarly be overridden by a DON’T ASK setting for the user (like-named field in the NEW PERSON \[#200\] file). A NULL value functions as ASK. The user override can be set by any user through the Edit User Characteristics \[XUSEREDITSELF\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/029.png) REF: For more information on the Edit User Characteristics \[XUEDITSELF\] option, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

If the parameter is set to DON’T ASK, Signon/Security does *not* perform the DA query and assumes the user’s last terminal type is still appropriate. Although the difference in resource consumption is negligible, the user can appreciate a split second’s savings in time. Thus, bypassing the DA query can be acceptable, if the same terminal type is always being used. But if the user should sign onto another terminal type, problems can occur with the presentation of screen-oriented displays unless the user knows how to change the terminal type to match the actual current one.

If the device is *non*-ANSI-standard, Signon/Security may *not* find a DA but continues to determine the terminal’s identity by querying its answerback message. All known *non*-ANSI devices (such as Qume 102 terminal) should have their answerback messages programmed. This is accomplished by using the terminal type setup mechanism and entering C-QUME as the Qume 102’s answerback message. The name *must* match an entry in Kernel’s TERMINAL TYPE (#3.2) file to take effect. If the answerback message contains additional characters (such as a serial number), the message does *not* match an entry in the TERMINAL TYPE (#3.2) file and is useless for signon purposes.

If the terminal’s DA return code does *not* match an entry in the DA RETURN CODES (#3.22) file, or if the terminal is *non*-ANSI and *cannot* be programmed with an appropriate answerback message, Signon/Security prompts the user to identify the terminal type if the user’s ASK DEVICE TYPE AT SIGN-ON setting is set to ASK. This is the only case in which the terminal type prompt is asked during signon. The last terminal type used is presented as the default (it is stored in the NEW PERSON \[#200\] file). If ASK DEVICE TYPE AT SIGN-ON is set to DON’T ASK, Signon/Security assumes that the last terminal type is appropriate and does *not* prompt the user for validation.

#### Display Attributes (DA) Return Codes

The DA RETURN CODES (#3.22) file is used to equate DA return codes to entries in the TERMINAL TYPE (#3.2) file. You can use the DA Return Code Edit \[XU DA EDIT\] option to automate the population of the DA RETURN CODES (#3.22) file.

![](kernel-8-0-systems-management-signon-security-user-guide/030.png) REF: For more information, see the “Managing Display Attributes (DA) Return Codes” section in the [*Kernel 8.0 Systems Management: Device Handler User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf#Managing_Display_Attributes_Return_Codes).

#### SELECTABLE AT SIGNON

System administrators can also control which devices can be selected at signon with a field in the TERMINAL TYPE (#3.2) file. The SELECTABLE AT SIGN-ON flag should be set to YES for all devices commonly used for signon. Ordinarily, it should *not* be set for printers (such as P- terminal types P-DEC or P-OTHER). To allow the loading of ScreenMan forms and proper functioning of other screen-oriented displays, the flag should also *not* be set for PK- types, that is, printers with keyboards. This is *not* an actual restriction, however, but a recommendation.

#### LIFETIME OF VERIFY CODE

To ensure that users change their Verify Codes at periodic intervals, system administrators should set the LIFETIME OF VERIFY CODE parameter in the KERNEL SYSTEM PARAMETERS (#8989.3) file to a certain number of days. The maximum number is 90 days, and the minimum number is 1 day. Thus, sites can choose any number from 1-90 days before requiring users to change their Verify Code. At the end of that period (such as every 90 days), users *must* then change their Verify Codes. Signon/Security checks whether the Verify Code needs to be changed, and if so, prompts the user at signon to enter a new Verify Code.

#### AUTO-GENERATE ACCESS CODES

When assigning Access Codes, the security officer or system administrators can invent an alphanumeric string or can ask Kernel to generate one. If the AUTO-GENERATE ACCESS CODES site parameter in the KERNEL SYSTEM PARAMETERS (#8989.3) file is set to YES, only generated, cryptic codes can be assigned. It is *not* necessary to pick the first one presented; others can be generated for selection.

#### DEFAULT INSTITUTION and AGENCY

The institution running Kernel software is defined during the Kernel installation when prompted for the DEFAULT INSTITUTION in the KERNEL SYSTEM PARAMETERS (#8989.3) file. This field is a pointer to the INSTITUTION (#4) file. One or more institutional affiliations can also be associated with a user (such as a VA Outpatient Clinic and an Army Medical Center). This data is stored in the DIVISION Multiple field in the NEW PERSON (#200) file. If a user is associated with more than one institution (division), the user is prompted at signon to select a division. In this way, the local variable DUZ(2) can be set to the appropriate value. If the user’s DIVISION Multiple field is blank, the DEFAULT INSTITUTION field (File \#8989.3) is used to define DUZ(2). Since the INSTITUTION (#4) file contains a pointer to the AGENCY (#4.11) file, the signed-on user’s agency affiliation can also be determined.

The KERNEL SYSTEM PARAMETERS (#8989.3) file also contains the AGENCY CODE (#9). This field is *not* a pointer but is instead a SET OF CODES (such as N for Navy or V for VA). This field is presented for editing during Kernel installation. Its value is used at sign on to set the DUZ(“AG”) local variable. Thus, the agency associated with the overall Kernel system can be determined.

#### AUTO MENU

The AUTO MENU flag, stored in the local variable DUZ(“AUTO”), is used by Menu Manager to control whether all items on a menu are presented automatically after each cycle through the menu system. If the items are *not* displayed, the user can always invoke the display by entering a question mark (?). New users often like to see all the menu choices. Experienced users probably do *not* need to see the choices and the display can be suppressed to save system resources. The user setting for AUTO MENU in the NEW PERSON (#200) file overrides any comparable device setting in the DEVICE (#3.5) file, which will, in turn, override the site parameter default in the KERNEL SYSTEM PARAMETERS (#8989.3) file. Users can edit the setting with the Edit User Characteristics \[XUSEREDITSELF\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/031.png) REF: For more information on the Edit User Characteristics \[XUEDITSELF\] option, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

#### TYPE-AHEAD

If TYPE-AHEAD is disabled, any keystrokes that the user enters while computer system processes previously issued instructions do *not* register. If TYPE-AHEAD is enabled, keystrokes entered in advance of processing are stored in the TYPE-AHEAD buffer and is interpreted when the earlier process is finished. New users may experience unwanted results if TYPE-AHEAD is enabled and they had *not* anticipated the effect. Experienced users may prefer TYPE-AHEAD for efficiency. The user setting overrides the device setting, which, in turn, overrides the site parameter setting. Users can edit the setting with the Edit User Characteristics \[XUSEREDITSELF\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/032.png) REF: For more information on the Edit User Characteristics \[XUEDITSELF\] option, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

#### TIMED READ

The value for the TIMED READ parameter is stored in the local variable DTIME and is used to calculate how long Kernel should wait before terminating a READ. If, for example, a user does *not* respond to a menu prompt in the number of seconds defined by the TIMED READ, Kernel takes steps towards signoff and, without subsequent user response, halts the user session. The user setting overrides the device setting, which, as usual, overrides the site default.

Based on VA organizational requirements, users can choose a number between 0 and 900 seconds (that is 15 minutes) for this field.

![](kernel-8-0-systems-management-signon-security-user-guide/033.png) NOTE: Users who require a timeout of greater than 900 seconds (15 minutes) are required to have an Approval Memo based on their role/position. They have alternate methods available to them to assign greater than the system maximum, but they are required to have that memo for approval and a risk accepted Program Objectives and Milestones (POAM).

#### POST SIGN-IN MESSAGE

The POST SIGN-IN MESSAGE is like introductory text (that is INTRO TEXT field in File \#8989.3), except that Kernel displays it only after a successful signon. Like the introductory text, you can edit the message text using the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option; alternately, you can use the Post sign-in Text Edit \[XUSERPOST\] option, which is specially designed for this purpose:

<span id="_Toc193181632" class="anchor"></span>Figure 14: Post Sign-in Text Edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

<span class="mark">Post sign-in Text Edit</span> \[XUSERPOST\]

Applications can append information to the POST SIGN-IN MESSAGE (on a per-user, per signon basis only) by attaching to the User sign-on event \[XU USER SIGN-ON\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/034.png) REF: For more information on the User sign-on event \[XU USER SIGN-ON\] option, see the [*Kernel 8.0 Developer’s Guide: Signon/Security Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf).

#### 2-Factor Authentication (2FA)

The KERNEL SYSTEM PARAMETERS (#8989.3) file also contains fields that are required to enable 2-Factor Authentication (2FA). These fields are *not* included in the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option, because they should *not* be edited in VA Production systems. If VistA is being installed in a *non*-VA environment, they can be edited using VA FileMan.

Kernel Patch XU\*8.0\*701 introduced the STRICT TOKEN VALIDATION (#220) field that defaults to NO. This field is included in the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/035.png) NOTE: The original implementation of 2FA did *not* enforce all the verifications of the SSOi token. Thus, the default value of NO in this field permits the continued use of “*non*-strict” validation and records any verification failures as “warnings” in the SIGN-ON LOG (#3.081) file. In the future, it will be possible to enforce strict token validation by changing this field’s value to YES.

![](kernel-8-0-systems-management-signon-security-user-guide/036.png) NOTE: Kernel Patch XU\*8.0\*701 also introduced the cache.cer certificate file, which contains the chain of Certificate Authorities (CA) used to validate the signature of the 2FA SSOi token. The installation of the cache.cer file is *not* mandatory when setting the STRICT TOKEN VALIDATION (#220) field to NO; however, the certificate file is required when setting it to YES.

2FA Field descriptions (listed in field number order):

- SECURITY TOKEN SERVICE (#200.1): When using brokered authentication with a security token issued by a Security Token Service (STS), this field contains the identification of the issuer of the token. The STS is trusted by both the client and the server to provide the interoperable security tokens. Security Assertion Markup Language (SAML) tokens are standards-based XML tokens that are used to exchange security information, including:
  - Attribute statements
  - Authentication decision statements
  - Authorization decision statements

They can be used as part of a Single Sign-On (SSO) solution allowing a client to talk to services running on disparate technologies. The value of this field should be set to the domain name of the STS as found in the “Issued to:” field of the STS PKI certificate used to digitally sign the token. For VA Production systems, the value should be set to the following value:

*\<REDACTED\>*.va.gov

- ORGANIZATION (#200.2): Identity and Access Management field used to identify the VistA instance organization. For internally authenticated users, this field matches the SUBJECT ORGANIZATION (#205.2) field of the user identified in the NEW PERSON (#200) file. For VA Production systems, this field should always contain the following value:
- ORGANIZATION ID (#200.3): Identity and Access Management field used to uniquely identify the VistA instance organization. For internally authenticated users, this field matches the SUBJECT ORGANIZATION ID (#205.3) field of the user identified in the NEW PERSON (#200) file. For VA Production systems, this field should always contain the following value:

urn:oid:2.16.840.1.113883.4.349

- STRICT TOKEN VALIDATION (#220): This field is used to apply strict credential token validation by Kernel during sign-on. The default is NO, *non*-strict token validation. Setting it to YES, strict token validation, may cause problems with users signing on to VistA if the required infrastructure is *not* properly set up.

### XU USER SIGN-ON Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User sign-on event \[XU USER SIGN-ON\] option can attach action-type options to this extended-action-type option, so that software-specific actions can be performed at signon.

![](kernel-8-0-systems-management-signon-security-user-guide/037.png) REF: For more information, see the [*Kernel 8.0 Developer’s Guide: Signon/Security Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf).

### XU USER START-UP Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User start-up event \[XU USER START-UP\] option is a protocol option used exclusively during a VistA user signon event. Items attached to this option are “TYPE: action” options in the OPTION (#19) file, which can be used for software-specific actions that prompt users for input upon VistA signon before their primary menu option is displayed. Unlike the User sign-on event \[XU USER SIGN-ON\] option, it can provide interactive prompting to users. It is *not* used for GUI signon. It is called from the XQ12 routine.

![](kernel-8-0-systems-management-signon-security-user-guide/038.png) REF: This option was added with Kernel patch XU\*8.0\*593. For more information, see the [*Kernel 8.0 Developer’s Guide: Signon/Security Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf).

### Clear all users at startup Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181633" class="anchor"></span>Figure 15: Clear All Users at Startup Option

PARENT OF QUEUABLE OPTIONS ... \[ZTMQUEUABLE OPTIONS\]

<span class="mark">Clear all users at startup</span> \[XUSER-CLEAR-ALL\]

If multiple signons are prohibited, users may be prevented from signing on to the system when it is brought up after a crash (which can cause numerous abnormal exits). To prevent this problem from occurring, system administrators can use the Clear all users at startup \[XUSER-CLEAR-ALL\] option. Kernel *recommends* this option be scheduled to run at system startup. Although this option can be invoked interactively without ill effects, it was designed as a background process, thus, it is placed along with other tasked options on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu.

![](kernel-8-0-systems-management-signon-security-user-guide/039.png) REF: For information on how to release a single user, see the “[Proxy (Connector) Detail Report Option](#proxy-connector-detail-report-option)” section.

### Enabling and Disabling Logons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System administrators have full control over whether logons are enabled. Access to a particular Volume Set can be disabled by setting the INHIBIT LOGONS? flag in the VOLUME SET (#14.5) file. Setting the flag to YES sets the ^%ZIS(“14.5”,”LOGON”,”*volume set”*) node, whose presence disallows user logons. That is, logons through Signon/Security, invoking the ^ZU routine, fails (terminals for user access are usually linked to ZU within the operating system setup. Some special terminals, like the console, are untied.) The ^%ZIS(“14.5”,“LOGON”,“*volume set”*) node is also checked after each cycle through the menu system; signed-on users are logged off as soon as they return to a menu prompt.

## Adding New Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Creating a new user account involves:

- Adding a record to the NEW PERSON (#200) file.
- Assigning an Access Code.
- Assigning a primary menu.

You need the XUMGR security key to assign primary menu options. Even the at-sign (@; Programmer access) is insufficient, as checked by the PRIMARY MENU OPTION (#201) field’s input transform.

<span id="_Toc193181634" class="anchor"></span>Figure 16: User Management Menu Options: Associated Menu Options when Adding a New User

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

Add a New User to the System \[XUSERNEW\]

Grant Access by Profile \<locked: XUMGR\> \[XUSERBLK\]

User Inquiry \[XUSERINQ\]

### Add a New User to the System Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the legacy Add a New User to the System \[XUSERNEW\] option to set up user accounts one-by-one. The Add a New User to the System \[XUSERNEW\] option presents a standard scrolling-mode editing sequence for user attributes.

When using this option, entry of a social security number in the SSN (#9) field is usually required. While SSN is *not* required in the NEW PERSON (#200) file data dictionary, it is a required field when using this option. If the option is used by someone who holds the XUSPF200 security key, however, entry of an SSN is *not* required.

You can also print security forms for the new user with this option.

When signing on for the first time, the new user should simply press \<Enter\> at the “Verify code” prompt, which then lets them enter their own secret Verify Code.

<span id="_Ref184879779" class="anchor"></span>Figure 17: Add a New User to the System Legacy Option—System Prompts and User Entries and ScreenMan Forms 1 - 5

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

<span class="mark">User Management ...</span>

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">USER \<Enter\></span> Management

<span class="mark">Add a New User to the System</span>

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> a New User to the System

Enter NEW PERSON's name (Family,Given Middle Suffix): <span class="mark">XUSER,FORTY \<Enter\></span>

Are you adding 'XUSER,FIFTY' as a new NEW PERSON (the 1556TH)? No// <span class="mark">Y \<Enter\></span> (Yes)

Checking SOUNDEX for matches.

USER,LAB

USER,OPC

USER,MC

USER,DOCTOR

USER,NEW

Do you still want to add this entry: NO// <span class="mark">YES \<Enter\></span>

Now for the Identifiers.

INITIAL: <span class="mark">FX \<Enter\></span>

SSN: <span class="mark">000123456 \<Enter\></span>

SEX: <span class="mark">M \<Enter\></span> MALE

NPI: <span class="mark">\<Enter\></span>

Edit an Existing User

NAME: XUSER,FORTY <span class="mark">Page 1 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME...XUSER,FORTY INITIAL: FX

TITLE: NICK NAME:

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

Terminati. <span class="mark">NAME COMPONENTS</span> .

. <span class="mark">Prefix:</span> .

. <span class="mark">Given (First): FORTY</span> .

Select SEC. <span class="mark">Middle:</span> .

Want to edi. <span class="mark">Family (Last): XUSER</span> .

Want to edi. <span class="mark">Suffix:</span> .

. .

. <span class="mark">XUSER,FIFTY</span> .

F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">Close</span>

Edit an Existing User

NAME: XUSER,FIFTY <span class="mark">Page 1 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME...XUSER,FIFTY INITIAL: FX

TITLE: NICK NAME: <span class="mark">FORTY</span>

SSN: <span class="mark">000123456</span> DOB: <span class="mark">JAN 10,1960</span>

DEGREE: <span class="mark">BS</span> MAIL CODE: <span class="mark">250</span>

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: <span class="mark">EVE</span>

Select SECONDARY MENU OPTIONS:

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE:

Want to edit VERIFY CODE (Y/N):

Select DIVISION:

SERVICE/SECTION: <span class="mark">MEDICAL ADMINISTRATION</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save <span class="mark">Next Page</span> Previous Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">N</span> <span class="mark">Press \<PF1\>H for helpInsert</span>

Edit an Existing User

NAME: XUSER,FIFTY <span class="mark">Page 2 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NETWORK USERNAME: VHAISPXUUSF

TIMED READ (# OF SECONDS):

MULTIPLE SIGN-ON: MULTIPLE SIGN-ON LIMIT:

ASK DEVICE TYPE AT SIGN-ON: AUTO MENU:

PROHIBITED TIMES FOR SIGN-ON: TYPE-AHEAD:

AUTO SIGN-ON:

Preferred Editor: SCREEN EDITOR - VA FILEMAN

ALLOWED TO USE SPOOLER: PAC:

CAN MAKE INTO A MAIL MESSAGE:

FILE RANGE:

ALWAYS SHOW SECONDARIES:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save <span class="mark">Next Page</span> Previous Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">N</span> <span class="mark">Press \<PF1\>H for helpInsert</span>

Edit an Existing User

NAME: XUSER,FIFTY <span class="mark">Page 3 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROHIBITED TIMES FOR SIGN-ON:

PHONE: OFFICE PHONE: <span class="mark">5555555555</span>

COMMERCIAL PHONE: FAX NUMBER:

VOICE PAGER: DIGITAL PAGER:

LANGUAGE: <span class="mark">ENGLISH</span>

Person Class Effective Expired

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save <span class="mark">Next Page</span> Previous Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">N</span>Press \<PF1\>H for helpInsert

Edit an Existing User

NAME: XUSER,FIFTY <span class="mark">Page 4 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RESTRICT PATIENT SELECTION: OE/RR LIST:

CPRS TAB ACCESS:

Name Description Effective Date Expiration Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save <span class="mark">Next Page</span> Previous Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">N</span> <span class="mark">Press \<PF1\>H for helpInsert</span>

Edit an Existing User

NAME: XUSER,FIFTY Page 5 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PERMANENT ADDRESS:

Street 1: <span class="mark">1234 Main Street</span>

Street 2:

Street 3:

City: <span class="mark">ANYTOWN</span>

State: <span class="mark">CALIFORNIA</span>

Zip Code: <span class="mark">92264</span>

E-Mail Address: <span class="mark">FORTY.XUUSER@VA.GOV</span>

Is this person an active Trainee?: <span class="mark">NO</span>

VHA Training Fac.:

Start Date of Training: Last Training Month & Year:

Trainee Inactive (Date):

Program of Study:

Target Degree Lvl:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Exit</span> Save Next Page Previous Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">E</span> <span class="mark">Press \<PF1\>H for helpInsert</span>

Without a VERIFY code the user will not be able to sign-on!

Print User Account Access Letter? <span class="mark">NO \<Enter\></span>

Do you wish to allocate security keys? NO// <span class="mark">\<Enter\></span>

### Grant Access by Profile Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Grant Access by Profile \[XUSERBLK\] option includes features unavailable in the [Add a New User to the System](#add-a-new-user-to-the-system-option) \[XUSERNEW\] option. With the Grant Access by Profile \[XUSERBLK\] option you can grant access to one or more people based on a typical user profile. All characteristics of the typical user, including menus, keys, and service/section, are copied to the new user or replace the characteristics of an existing user. For new users, access security forms are generated as part of the process. These forms can be delivered to the service/section coordinator by inter-office mail and can be distributed to the new users.

The Grant Access by Profile \[XUSERBLK\] option is locked with the XUMGR security key and is strictly limited for use by system administrators. It *must* be restricted, because any user profile, even that of a developer, can be copied to another user. As with the [Add a New User to the System](#add-a-new-user-to-the-system-option) \[XUSERNEW\] option, the SSN (#9) field is required when adding new records except by holders of the XUSPF200 security key or if another default set of New Person Identifiers has been defined.

Access is assigned according to an existing user profile. Characteristics of the new user are cloned from the existing one. Rather than copying the characteristics from an actual user, creating several dummy users with profiles of typical positions can be worthwhile. A user (such as PHARMACY,TECH or RESIDENT,SURGERY) could be created with the appropriate user attributes, including menu options, keys, and service/section codes.

Several steps are involved in copying access to new or existing users. First, you enter the name of the user account from which you want to clone. Then, optionally, you can specify a TERMINATION DATE. Next, you enter the names of the new users to create.

The system pauses for each new user as it:

- Verifies identifiers.
- Checks for duplicates.
- Updates the NEW PERSON (#200) file.

You *must* enter a device upon which to print the computer account notification letters. You can either run the access assignment immediately or queue it for a later time.

![](kernel-8-0-systems-management-signon-security-user-guide/040.png) NOTE: The PSDRPH security key *cannot* be allocated using this option, the Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option *must* be used to allocate this security key.

<span id="_Ref184883362" class="anchor"></span>Figure 18: Grant Access by Profile \[XUSERBLK\] Legacy OptionSystem Prompts and User Entries

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

<span class="mark">User Management ...</span>

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">USER \<Enter\></span> Management

Add a New User to the System

<span class="mark">Grant Access by Profile</span>

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management \<TEST ACCOUNT\> Option: <span class="mark">GRANT \<Enter\></span> Access by Profile

Batch Entry of New Persons

--------------------------

Please select a person to copy from

Template PERSON: <span class="mark">XUSER,ONE \<Enter\></span> OX

NAME: XUSER,ONE INITIAL: OX

ACCESS CODE: \<Hidden\> FILE MANAGER ACCESS CODE: @

DATE VERIFY CODE LAST CHANGED: FEB 10,2022

VERIFY CODE: \<Hidden\> NICK NAME: One

SEX: MALE

PREFERRED EDITOR: SCREEN EDITOR - VA FILEMAN

DATE ENTERED: DEC 08, 2021 CREATOR: XUSER,TWO

SSN: 000123456

LAST SIGN-ON DATE/TIME: OCT 26, 2022@15:19:34

XUS Logon Attempt Count: 0 XUS Active User: Yes

Entry Last Edit Date: DEC 08, 2021 TERMINAL TYPE LAST USED: C-VT320

NAME COMPONENTS: 200

SERVICE/SECTION: INFORMATION SYSTEMS CENTER

SIGNATURE BLOCK PRINTED NAME: ONE XUUSER

KEY: XUPROG GIVEN BY: XUSER,TWO

DATE GIVEN: DEC 08, 2021

KEY: XUMGR GIVEN BY: XUSER,TWO

DATE GIVEN: DEC 08, 2021

KEY: XUPROGMODE GIVEN BY: XUSER,TWO

Type \<Enter\> to continue or '^' to exit:

DATE GIVEN: DEC 08, 2021

KEY: XMMGR GIVEN BY: XUSER,TWO

DATE GIVEN: DEC 08, 2021

MULTIPLE SIGN-ON: ALLOWED ASK DEVICE TYPE AT SIGN-ON: ASK

AUTO MENU: YES, MENUS GENERATED TYPE-AHEAD: ALLOWED

TIMED READ (# OF SECONDS): 999 AUTO SIGN-ON: Yes

PRIMARY MENU OPTION: EVE

Is this the person whose data you want cloned? <span class="mark">Y \<Enter\></span> YES

You may enter a date, when the users that are being created/updated

will no longer have access to the system.

Enter (optional) TERMINATION DATE: <span class="mark">\<Enter\></span>

Batch Entry of New Persons

--------------------------

Clone of: XUSER,ONE

Enter NEW PERSON's name (Family,Given Middle Suffix): <span class="mark">XUSER,EIGHTY \<Enter\></span>

Are you adding 'XUSER,EIGHTY' as a new NEW PERSON (the 1557TH)? No// <span class="mark">Y \<Enter\></span> (Yes)

Checking SOUNDEX for matches.

XUSER,FIFTY

USER,LAB

USER,OPC

USER,MC

USER,DOCTOR

USER,NEW

Do you still want to add this entry: NO// <span class="mark">Y \<Enter\></span>

Name components.

FAMILY (LAST) NAME: XUSER// <span class="mark">\<Enter\></span>

GIVEN (FIRST) NAME: EIGHTY// <span class="mark">\<Enter\></span>

MIDDLE NAME: <span class="mark">\<Enter\></span>

SUFFIX: <span class="mark">\<Enter\></span>

Now for the Identifiers.

INITIAL: <span class="mark">EX \<Enter\></span>

SSN: <span class="mark">000456789 \<Enter\></span>

SEX: <span class="mark">F \<Enter\></span> FEMALE

NPI:

Do You Want To Clone PERSON CLASS? <span class="mark">YES \<Enter\></span>

Next!

Enter NEW PERSON's name (Family,Given Middle Suffix): <span class="mark">\<Enter\></span>

Where do you want to print the COMPUTER ACCOUNT NOTIFICATION LETTERS?

DEVICE: HOME// <span class="mark">\<Enter\></span> TELNET PORT Right Margin: 80// <span class="mark">\<Enter\></span>

CREATING A NEW ACCOUNT FOR 'XUSER,EIGHTY'

One moment please...

USER ACCOUNT NOTIFICATION

SuperStar VAMC

123 anywhere

anytown, state, zip

EIGHTY XUSER

INFORMATION SYSTEMS CENTER ()

---

A user account has been created in your name to enable you

to access on-line clinical and/or administrative data

required to perform your duties as an employee of the

Department of Veterans Affairs. Please read the enclosed

NEW USER INFORMATION before you attempt your first log-on

to the system. Questions about access should be referred

to the AIS Application Coordinator in your service, your

facility Information Security Officer (ISO), or your IRM

Service.

Your Computer Access Coordinator is:

Your Facility Information Security Officer:

Your Alternate Information Security Officer:

---

Access Code: XXXXXXXX

Verify Code: YYYYYYYY

COMPUTER ACCOUNT ACCESS POLICY

Your VA Facility

EIGHTY XUSER

INFORMATION SYSTEMS CENTER ()

As an authorized user of VHA automated information systems (AISs) and

having access to data stored in them, I will be given sufficient access to

perform my assigned duties. I will use this access ONLY for its intended

purpose and understand the following policies that apply to VA data and

computer systems:

I agree to safeguard all passwords (e.g., Access/Verify codes, electronic

signature codes) assigned to me and am strictly prohibited from disclosing

these codes to anyone including family, friends, fellow workers,

supervisor(s), and subordinates for ANY reason.

I understand that I may be held accountable for all entries/changes made to

any government AIS using my passwords.

I am aware of the regulations and facility AIS security policies designed

to ensure the confidentiality of all sensitive information. I am aware

that information about patients or employees is confidential and protected

from unauthorized disclosure by law. I understand that my obligation to

protect VA information does not end with either the termination of my

access to this facility's systems or with the termination of my government

employment.

I will exercise common sense and good judgment in the use of electronic

mail. I understand that electronic mail is not inherently confidential and

I have no expectation of privacy in using it. I understand that technical

or administrative problems may create situations which requires viewing of

my messages. I also understand that facility management officials may

authorize access to my electronic mail messages whenever there is a

legitimate purpose for such access.

I understand that a violation of this notice constitutes disregard of a

local and/or VHA policy and will result in appropriate disciplinary action

as defined in VA employee conduct Regulations (VAR 820(b)) as well as

suspension/termination of access privileges.

I affirm with my signature that I have read, understand, and agree to

fulfill the provisions of this User Access notice.

Signature:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

EIGHTY XUSER INFORMATION SYSTEMS CENTER

RETURN THIS FORM TO: IRMS - NEW ACCTS (xxx/xxx)

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management \<TEST ACCOUNT\> Option:

### Security Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181635" class="anchor"></span>Figure 19: Reprint Access agreement letter Option

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

Reprint Access agreement letter \[XUSERREPRINT\]

Two security forms are printed for each new user:

- The Computer Account Notification—Includes the user’s auto-generated Access Code and the name of the service/section coordinator who can answer questions.
- The Computer Access Policy—A contract to which users *must* adhere. It states the terms of granting access to sensitive information; the user *must* accept these terms as a condition of being given system access.

These security forms are stored in the XUSER COMPUTER ACCOUNT help frame and should be edited for local use as follows:

1.  Copy the XUSER COMPUTER ACCOUNT help frame into a new site help frame (such as SFO COMPUTER ACCOUNT).
3.  Edit the security forms for local use. Replace the “placeholder” text with the actual name and address of the facility.
4.  Repoint the Kernel Parameter to the new site XUSER COMPUTER ACCOUNT help frame using VA FileMan.

For example:

<span id="_Toc207519104" class="anchor"></span>Figure 20: Security Forms—Sample User Entries (1 of 4)

\><span class="mark">D ^XUP \<Enter\></span>

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320

You have 13 new messages.

Select OPTION NAME: <span class="mark">SYSTEMS MANAGER MENU \<Enter\></span>

Device Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Management ...

Manage Mailman ...

Menu Management ...

VA FileMan ...

Verifier Tools Menu ...

Select Systems Manager Menu Option: <span class="mark">VA FILEMAN \<Enter\></span>

VA FileMan Version 22.2

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">TRANSFER ENTRIES \<Enter\></span>

Select TRANSFER OPTION: <span class="mark">TRANSFER FILE ENTRIES \<Enter\></span>

INPUT TO WHAT FILE: HELP FRAME// <span class="mark">HELP FRAME \<Enter\></span> (562 entries)

TRANSFER FROM FILE: HELP FRAME// <span class="mark">\<Enter\></span>

TRANSFER DATA INTO WHICH HELP FRAME: <span class="mark">ISC COMPUTER ACCESS \<Enter\></span>

Not a known package or a local namespace.

Are you adding 'ISC COMPUTER ACCESS' as a new HELP FRAME (the 563RD)? No// <span class="mark">Y \<Enter\></span> (Yes)

HELP FRAME NUMBER: 742// <span class="mark">\<Enter\></span>

HELP FRAME HEADER: <span class="mark">Computer Access \<Enter\></span>

TRANSFER FROM HELP FRAME: <span class="mark">XUSER COMPUTER ACCOUNT \<Enter\></span> Batch user access document

WANT TO DELETE THIS ENTRY AFTER IT'S TRANSFERRED? No// <span class="mark">\<Enter\></span> (No)

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

SINCE THE TRANSFERRED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'HELP FRAME' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// <span class="mark">\<Enter\></span> (No)

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">ENTER OR EDIT FILE ENTRIES \<Enter\></span>

INPUT TO WHAT FILE: HELP FRAME// <span class="mark">\<Enter\></span>

EDIT WHICH FIELD: ALL// <span class="mark">TEXT \<Enter\></span> (word-processing)

Select HELP FRAME NAME: <span class="mark">ISC COMPUTER ACCESS \<Enter\></span> Computer Access

NAME: ISC COMPUTER ACCESS// <span class="mark">\<Enter\></span>

HEADER: Computer Access// <span class="mark">\<Enter\></span>

TEXT: . . .

. . .

suspension/termination of access privileges.

I affirm with my signature that I have read, understand, and agree to

fulfill the provisions of this User Access notice.

\|INDENT(5)\|\|WIDTH(75)\|\|NOWRAP\|

Signature:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\|#20.2\| \|#29\|

RETURN THIS FORM TO: IRMS - NEW ACCTS (xxx/xxx)

Edit? NO// <span class="mark">YES \<Enter\></span>

<span id="_Ref194993331" class="anchor"></span>Figure 21: Security Forms—Sample User Entries (2 of 4)

==\[ WRAP \]==\[ INSERT \]=============\< TEXT \>============\[ \<PF1\>H=Help \]====

\|INDENT(5)\| \|WIDTH(70)\|

\|NOWRAP\|

\|CENTER("USER ACCOUNT NOTIFICATION")\|

\|CENTER("<span class="mark">Department of Veterans Affairs</span>")\|

\|CENTER("<span class="mark">SuperStar VAMC</span>")\|

\|CENTER("<span class="mark">123 Any Street</span>")\|

\|CENTER("<span class="mark">Any Town, ST., 99999</span>")\|

\|XUVT(12)\|

\|#20.2\|

\|#29\| ( \|#29:#1.5\| )

\|XUVT(19)\|

---

\|WRAP\|

A user account has been created in your name to enable you to access

on-line clinical and/or administrative data required to perform your

duties as an employee of the Department of Veterans Affairs. Please read

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>

Select RELATED FRAME KEYWORD: <span class="mark">\<Enter\></span>

Want to LOAD KEYWORDS (Y/N)?: <span class="mark">N</span>

Select INVOKED BY ROUTINE: <span class="mark">\<Enter\></span>

Select EDITOR: <span class="mark">\<Enter\></span>

Select OBJECT: <span class="mark">\<Enter\></span>

ENTRY EXECUTE STATEMENT: <span class="mark">\<Enter\></span>

EXIT EXECUTE STATEMENT: <span class="mark">\<Enter\></span>

Select HELP FRAME NAME: <span class="mark">\<Enter\></span>

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">ENTER OR EDIT FILE ENTRIES \<Enter\></span>

INPUT TO WHAT FILE: HELP FRAME// <span class="mark">8989.2 \<Enter\></span> KERNEL PARAMETERS (6 entries)

EDIT WHICH FIELD: ALL// <span class="mark">\<Enter\></span>

Select KERNEL PARAMETERS NAME: <span class="mark">XUSER COMPUTER ACCOUNT \<Enter\></span>

NAME: XUSER COMPUTER ACCOUNT Replace <span class="mark">\<Enter\></span>

TYPE: <span class="mark">\<Enter\></span>

DEFAULT: <span class="mark">\<Enter\></span>

REPLACEMENT: <span class="mark">ISC COMPUTER ACCESS \<Enter\></span>

Select KERNEL PARAMETERS NAME: <span class="mark">\<Enter\></span>

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">\<Enter\></span>

FM VA FileMan ...

Core Applications ...

Device Management ...

Information Security Officer Menu ...

Manage Mailman ...

Menu Management ...

Operations Management ...

Programmer Options ...

Spool Management ...

Taskman Management ...

User Management ...

Select Systems Manager Menu Option: <span class="mark">USER MANAGEMENT \<Enter\></span>

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management Option: <span class="mark">REPRINT ACCESS AGREEMENT LETTER \<Enter\></span>

Select NEW PERSON NAME: <span class="mark">REQUEST,ACCESS \<Enter\></span> AR COMPUTER SPECIALIST

Is REQUEST,ACCESS the one you want? YES// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">0;80;60 \<Enter\></span> Telnet Terminal

<span id="_Toc207519106" class="anchor"></span>Figure 22: Security Forms—Sample User Account Notification Form (3 of 4)

USER ACCOUNT NOTIFICATION

Superstar VAMC

123 Any Street

Any Town, ST. 99999

ACCESS REQUEST

Superstar VAMC

---

A user account has been created in your name to enable you to

access on-line clinical and/or administrative data required to

perform your duties as an employee of the Department of Veterans

Affairs. Please read the enclosed NEW USER INFORMATION before

you attempt your first log-on to the system. Questions about

access should be referred to the AIS Application Coordinator in

your service, your facility Information Security Officer (ISO),

or your IRM Service.

Your Computer Access Coordinator is:

XUUSER,ONE

123X

510-555-9999

Your Facility Information Security Officer:

Two Xuser

Your Alternate Information Security Officer:

Three Xuser

---

NT Domain: \_\_\_\_\_\_\_\_\_\_

NT Username: VHA\_\_\_\_\_\_\_

NT Password: \_\_\_\_\_\_\_\_\_\_

VistA Access Code: \_\_\_\_\_\_\_\_

VistA Verify Code: \_\_\_\_\_\_\_\_

<span id="_Toc207519107" class="anchor"></span>Figure 23: Security Forms—Sample Computer Account Access Policy Form (4 of 4)

COMPUTER ACCOUNT ACCESS POLICY

SuperStar VAMC

ACCESS REQUEST

SuperStar VAMC

As an authorized user of VHA automated information systems (AISs) and

having access to data stored in them, I will be given sufficient access

to perform my assigned duties. I will use this access ONLY for its

intended purpose and understand the following policies that apply to VA

data and computer systems:

I agree to safeguard all passwords (e.g., Access/Verify codes, electronic

signature codes) assigned to me and am strictly prohibited from

disclosing these codes to anyone including family, friends, fellow

workers, supervisor(s), and subordinates for ANY reason.

I understand that I may be held accountable for all entries/changes made

to any government AIS using my passwords.

I am aware of the regulations and facility AIS security policies designed

to ensure the confidentiality of all sensitive information. I am aware

that information about patients or employees is confidential and

protected from unauthorized disclosure by law. I understand that my

obligation to protect VA information does not end with either the

termination of my access to this facility's systems or with the

termination of my government employment.

I will exercise common sense and good judgment in the use of electronic

mail. I understand that electronic mail is not inherently confidential

and I have no expectation of privacy in using it. I understand that

technical or administrative problems may create situations which requires

viewing of my messages. I also understand that facility management

officials may authorize access to my electronic mail messages whenever

there is a legitimate purpose for such access.

I understand that a violation of this notice constitutes disregard of a

local and/or VHA policy and will result in appropriate disciplinary

action as defined in VA employee conduct Regulations (VAR 820(b)) as well

as suspension/termination of access privileges.

I affirm with my signature that I have read, understand, and agree to

fulfill the provisions of this User Access notice.

Signature:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCESS REQUEST SuperStar VAMC

RETURN THIS FORM TO: IRMS - NEW ACCTS (xxx/xxx)

VA FileMan WORD-PROCESSING “windows” are used to retrieve the:

- User’s name
- Service/Section
- Service/Section coordinator’s name

To be effective, the SERVICE/SECTION field in the NEW PERSON (#200) file *must* be filled in for the new user. The COORDINATOR (IRM) field, a field in the SERVICE/SECTION (#49) file, *must* also be filled in and updated when necessary. WORD-PROCESSING “windows” are also used for formatting, like \|TOP\|, to separate the two forms. When using the File Access Security system, READ access to the SERVICE/SECTION (#49) file is needed to retrieve the coordinator’s name within the window command.

![](kernel-8-0-systems-management-signon-security-user-guide/041.png) REF: For more information on using WORD-PROCESSING “windows,” the File Access Security system, and navigation, see the *VA FileMan User Manual*.

The Reprint Access Agreement Letter \[XUSERREPRINT\] option allows you to reprint the computer access agreement letter in case there was a problem printing the first form (such as the first form is jammed in the printer). It does *not* reprint the Access Code on the letter, however.

## Edit an Existing User Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc59528917" class="anchor"></span>Figure 24: Edit an Existing User Option—Menu

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

<span class="mark">Edit an Existing User</span> \[XUSEREDIT\]

The attributes of an existing user can be edited with the Edit an Existing User \[XUSEREDIT\] option. This option invokes a screen-oriented display using ScreenMan.

It is impossible to exit the form and save changes unless all required fields (such as the SERVICE/SECTION field in the NEW PERSON \[#200\] file) are filled in (see Section <u>3.3.2</u>).

<span id="_Ref194993348" class="anchor"></span>Figure 25: Edit an Existing User \[XUSEREDIT\] Option

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

<span class="mark">User Management ...</span>

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">User \<Enter\></span> Management

Add a New User to the System

Grant Access by Profile

<span class="mark">Edit an Existing User</span>

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management \<TEST ACCOUNT\> Option: <span class="mark">EDIT \<Enter\></span> an Existing User

Select NEW PERSON NAME:

### Editable Field Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> describes each of the user field attributes you can edit with the Edit an Existing User \[XUSEREDIT\] option.

<table>
<caption><p><span id="_Ref236559165" class="anchor"></span>Table 4: Deactivate a User Option—Editable Fields/Attributes</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)<br />
(Required)</td>
<td>The user’s name should be entered in capital letters. The syntax should be “LAST,FIRST MI.” with only a comma (no spaces) between the last and first name. A middle initial can follow, separated with a space and followed with a period. It is <em>not</em> appropriate to add credentials (such as M.D.), since there are other ways to specify such additional information (by the Title and the Signature Block Printed Name). Furthermore, the parsing algorithms commonly used in software applications only recognize two pieces, before and after the comma, rearranging them and using uppercase/lowercase to generate “First MI. Last”.</td>
</tr>
<tr class="even">
<td>INITIAL (#1)</td>
<td>The user’s initials can be entered, usually two or three capital letters with no spaces. The NEW PERSON (#200) file contains a lookup-type cross-reference by INITIAL (C), so if the INITIAL field is filled in, the user can be found in the NEW PERSON (#200) file by entering the initials. For example, just the initials can be used at the “Select NEW PERSON Name:” prompt, or when addressing mail messages, or for other lookup purposes. Users can edit their initials at any time since this field is included in the common <strong>Edit User Characteristics</strong> [XUSEREDITSELF] option.</td>
</tr>
<tr class="odd">
<td>TITLE (#8)</td>
<td>This field points to the TITLE (#3.1) file, a file exported with Kernel but without data (records). The User Management options to add or edit a user’s record allow <strong>LAYGO</strong> into the TITLE (#3.1) file, so titles can be added through the NEW PERSON (#200) file. Although <em>not</em> required, it may be wise to assign appropriate titles to users, so this field can be referenced by other software applications. MailMan, for example, displays titles in message headers if the user who is reading mail has so indicated with a flag in MailMan’s Edit User Options called <strong>Show Titles</strong>.</td>
</tr>
<tr class="even">
<td>NICK NAME (#13)</td>
<td>Like INITIAL, NICK NAME has a lookup type cross-reference (<strong>D</strong>) in the NEW PERSON (#200) file so that lookups succeed simply by using the NICK NAME. This field is also included in Edit User Characteristics.</td>
</tr>
<tr class="odd">
<td>SSN (#9)</td>
<td><p>The SSN (#9) field is <em>not</em> a required field in the data dictionary for the NEW PERSON (#200) file. SSN is required when using the User Management options to add a new user unless the <strong>XUSPF200</strong> security key is held by the person using the option.</p>
<p>It is <em>highly recommended</em> that each new user have the SSN (#9) field filled in to minimize the problem of subsequent duplicate entries. Since many existing users do <em>not</em> have an SSN entered, however, the <strong>Edit an Existing User</strong> [XUSEREDIT] option does <em>not</em> require that one be entered.</p></td>
</tr>
<tr class="even">
<td>MAIL CODE (#28)</td>
<td>The user’s MAIL CODE can be entered for purposes of interoffice routing of manually delivered mail.</td>
</tr>
<tr class="odd">
<td>PRIMARY MENU OPTION (#201)<br />
(Required for functional access)</td>
<td><p>Users <em>must</em> be assigned a PRIMARY MENU OPTION (#201) field to reach Menu Manager after successfully entering Access and Verify Codes. The PRIMARY MENU OPTION should provide a route to all the computing functions the user can be expected to need. The <strong>XUMGR</strong> security key <em>must</em> be held by the person assigning the menu (unless delegated options are available for use with the Secure Menu Delegation system).</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/042.png) <strong>REF:</strong> Building and rearranging menus is discussed in the “<strong>Menu Manager: System Management</strong>” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf#Menu_Manager_System_Interface"><em>Kernel 8.0 Systems Management: Menu Manager User Guide</em></a>.</p></td>
</tr>
<tr class="even">
<td>SECONDARY MENU OPTIONS (#203)</td>
<td>The SECONDARY MENU OPTIONS (#203) field can be used to assign options to individual users to customize their menu choices. While a user may have a standard primary menu to carry out the usual functions of a department or service, additional special functions just for this user can be assigned as secondary options. This is a multiple field, unlike the PRIMARY MENU OPTION (#201) field, so additional items can easily be added.</td>
</tr>
<tr class="odd">
<td><p>ACCESS CODE (#2)</p>
<p>VERIFY CODE (#7.2)</p></td>
<td><p>These fields can be used to edit a user’s Access or Verify Code as needed. If a user has forgotten the Verify Code, or needs a new one, system administrators/ISO should delete the existing code so that when the user logs on and presses the <strong>&lt;Enter&gt;</strong> key at the “VERIFY CODE” prompt, a new (secret) password (VERIFY CODE) can be entered. To accomplish this, “<strong>Y</strong>” should be entered at the “Want to edit VERIFY CODE (Y/N) :” prompt. An at-sign (<strong>@</strong>) should then be entered to delete the existing code. The change is filed immediately, unlike other changes that are processed as part of the overall transaction when leaving the ScreenMan form.</p>
<p>Users can edit their Verify Code at any time using the <strong>Edit User Characteristics</strong> [XUEDITSELF] option on the <strong>SYSTEM COMMAND OPTIONS</strong> [XUCOMMAND] menu (aka <strong>Common</strong> menu). If this option uses a local template, the ability to edit the VERIFY CODE field should probably remain, as a security measure. System administrators can choose to add the ability to edit the ACCESS CODE field as well.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/043.png) <strong>REF:</strong> For more information on the <strong>Edit User Characteristics</strong> [XUEDITSELF] option, see the “<a href="#edit-user-characteristics-option">Edit User Characteristics Option</a>” section.</p></td>
</tr>
<tr class="even">
<td>FILE MANAGER ACCESS CODE (#3)</td>
<td><p>The FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON [#200] file) is stored in the local variable <strong>DUZ(0)</strong>. If <strong>DUZ(0)=@</strong>, the user is a developer with the highest level of <strong>Programmer</strong> access authority. Other <em>non</em>-reserved symbols can be assigned for File Access Security, depending on the user’s needs. Software applications indicate which symbols are needed for site-specific File Access Security.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/044.png) <strong>NOTE:</strong> In previous documentation and data dictionaries, it has been <em>implied</em> that the hashtag (<strong>#</strong>) symbol/character was reserved for File Access Security for system administrators; however, this is <em>not</em> true. It has merely been used as a convention<em>.</em></p>
<p>If the File Access Security conversion has been run, the FILE MANAGER ACCESS CODE (#3) field is <em>not</em> used to control file-level access security as it was <em>before</em> the conversion. The <u>File Access Security</u> system (formerly known as Part 3 of the Kernel installation) permits the association of a user with a file whereby explicit access can be granted. While the conversion process is somewhat involved, the benefits resulting from implementing the <u>File Access Security</u> system are worthwhile.</p>
<p>Even after running the file access conversion, the FILE MANAGER ACCESS CODE (#3) field continues to serve several functions:</p>
<p>If a user has been granted full file access privileges for a particular file, a further restriction can be placed at the file or field level to prohibit modification of the definition or entry of data. Files have top-level restrictions of <strong>READ</strong>, <strong>WRITE</strong>, or <strong>DELETE</strong> access as do fields and templates.</p>
<p>If the file, field, or template is protected with the at-sign (<strong>@</strong>; <strong>Programmer</strong> access), the user <em>must</em> also have the at-sign in the FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON (#200) file.</p>
<p>The Device Handler also checks the FILE MANAGER ACCESS CODE (#3) field of the user if the SECURITY field in the DEVICE (#3.5) file has been defined with a character string. The user would <em>not</em> be able to select the device unless at least one of the characters in the user’s code matched at least one character in the device code.</p>
<p>The most important FILE MANAGER ACCESS CODE (#3) field character is the at-sign (<strong>@</strong>; <strong>Programmer</strong> access). It has special meaning and overrides other file access restrictions or other FILE MANAGER ACCESS CODE (#3) field characters. It is <em>not</em> recommended that the at-sign be allocated unless absolutely needed. Allocation is, in part, restricted by the fact that only those few users who have <strong>Programmer</strong> access to the system can give other users the at-sign.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/045.png) <strong>NOTE:</strong> A <strong>SET</strong> statement from <strong>Programmer</strong> mode can be used to temporarily assign <strong>DUZ(0)=“@”</strong> <em>without</em> storing the code in the NEW PERSON (#200) file, which would give permanent <strong>Programmer</strong> access.</p>
<p>Use of the at-sign (<strong>@</strong>; <strong>Programmer</strong> access) is less common now than in the past since alternative security measures have been developed. It is still required for several critically sensitive checks, however, such as entering M code into VA FileMan files (such as OPTION [#19] and FUNCTION [#.5] files).</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/046.png) <strong>REF:</strong> For more information on File Access Security, see “<u>File Access Security</u>” in this manual and the <em>VA FileMan (Version 22.2) and Kernel (Version 8.0) File Access Security</em> supplemental documentation located on the VA Software Document Library (VDL) at: <a href="http://www.va.gov/vdl/application.asp?appid=5">VDL VA FileMan Application Documents</a></p></td>
</tr>
<tr class="odd">
<td>PREFERRED EDITOR (#31.3)</td>
<td><p>If a user’s PREFERRED EDITOR field is <strong>NULL</strong>, Kernel uses VA FileMan’s Line Editor to edit <strong>WORD-PROCESSING</strong> fields. If the PREFERRED EDITOR is set to another entry in the ALTERNATE EDITOR (#1.2) file, like VA FileMan’s Screen Editor, Kernel uses that editor when the user edits <strong>WORD-PROCESSING</strong> fields. As described in VA FileMan’s documentation, users can switch from the Line Editor to another editor by using the Utility suboption on the <strong>Edit options</strong> [XUEDITOPT] menu.</p>
<p><span id="_Toc193181637" class="anchor"></span>Figure 26: VA FileMan Line Editor—Sample User Dialog</p>
<p>1&gt;<strong><mark>_ &lt;Enter&gt;</mark></strong></p>
<p>2&gt;<strong><mark>&lt;Enter&gt;</mark></strong></p>
<p>EDIT Option: <strong><mark>Utilities in Word-Processing &lt;Enter&gt;</mark></strong></p>
<p>UTILITY Option: <strong><mark>Editor &lt;Enter&gt;</mark></strong></p>
<p>Select ALTERNATE EDITOR: <strong><mark>SCREEN EDITOR - VA FILEMAN &lt;Enter&gt;</mark></strong></p>
<p>If the PREFERRED EDITOR is the Screen Editor, it is also possible to switch to another editor, like the Line Editor, to take advantage of Line Editor features such as File Transfer from Foreign CPU.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/047.png) <strong>NOTE:</strong> Other editors (such as Class III editors) may <em>not</em> support switching to the Line Editor, which may be a limitation in some circumstances.</p>
<p>This field is also included in <strong>Edit User Characteristics</strong> [XUSEREDITSELF] and MailMan’s Edit User options, so that all users can define a PREFERRED EDITOR if they so choose.</p></td>
</tr>
<tr class="even">
<td>DIVISION (#16)</td>
<td>The DIVISION Multiple field has a corresponding site parameter, the Default Institution, that sets users’ <strong>DUZ(2)</strong> if this field is <em>not</em> filled in. A user setting, however, takes precedence over the site parameter. This is a multiple field and if the user is associated with more than one institution, the user is prompted at signon to pick the one corresponding to the computing activities to be carried out in that session.</td>
</tr>
<tr class="odd">
<td>SERVICE/SECTION (#29)<br />
(Required)</td>
<td>This field points to the SERVICE/SECTION (#49) file distributed with Kernel’s virgin installation. No data is included. It is a required field since applications have begun to use it in various utilities. Kernel’s <strong>CPU/Service/User/Device Stats</strong> [XUSTAT] option, for example, can summarize signon information for all users in the same Service/Section. The <strong>Grant Access by Profile</strong> [XUSERBLK] option also makes use of this field to specify the Service/Section Coordinator to whom the access forms of the new users should be delivered.</td>
</tr>
<tr class="even">
<td>NETWORK USERNAME (#501.1)</td>
<td>This is the username that is used by the Windows Active Directory. It can be used to help identify the user; although it should <em>not</em> be relied on for accuracy as it is manually entered data that is <em>not</em> validated by Active Directory.</td>
</tr>
<tr class="odd">
<td>TIMED READ (#200.1)</td>
<td>As discussed with other site parameters earlier in this section, TIMED READ defines the length of time Kernel should wait for a user response to a <strong>READ</strong>. A setting for the user attribute overrides the site default. It is used to define the local variable <strong>DTIME</strong>.</td>
</tr>
<tr class="even">
<td>MULTIPLE SIGN-ON (#200.04)</td>
<td>As discussed with other site parameters, this field controls whether the user is permitted to have two or more concurrent signon sessions. The user setting takes precedence.</td>
</tr>
<tr class="odd">
<td>AUTO MENU (#200.06)</td>
<td>As discussed with other site parameters, this field controls whether the entire list of menu options is automatically presented or whether the user needs to enter a question mark (<strong>?</strong>) to invoke the display. The user setting takes precedence.</td>
</tr>
<tr class="even">
<td>ASK DEVICE TYPE AT SIGN-ON (#200.05)</td>
<td>As discussed with other site parameters, this field controls whether the device being used at signon is queried for its terminal type. The user setting takes precedence.</td>
</tr>
<tr class="odd">
<td>TYPE-AHEAD (#200.09)</td>
<td>This field controls whether the user can enter text faster than the computer can read it. If set to <strong>YES</strong>, the computer buffers input from the user. If set to <strong>NO</strong>, keystrokes from the user are lost if they are typed faster than the computer can process them.</td>
</tr>
<tr class="even">
<td>ALLOWED TO USE SPOOLER (#41)</td>
<td>This field controls whether a user can pick the spool device at the device prompt to send output to the spooler.</td>
</tr>
<tr class="odd">
<td>PAC (#14, Programmer Access Code)</td>
<td>For users who have been granted the <strong>Programmer mode</strong> [XUPROGMODE] option along with the <strong>XUPROG</strong> and <strong>XUPROGMODE</strong> security keys, a <strong>Programmer</strong> Access Code can be assigned as additional security. If a PAC is defined, Kernel prompts for the PAC just before allowing a user to enter <strong>Programmer</strong> mode. If this field is <strong>NULL</strong>, a PAC is <em>not</em> asked.</td>
</tr>
<tr class="even">
<td>CAN MAKE INTO A MAIL MESSAGE (#41.2)</td>
<td>This field controls whether a spooled document can be transformed into a regular mail message for use within MailMan.</td>
</tr>
<tr class="odd">
<td>DISUSER (#7)</td>
<td>If set to <strong>YES</strong>, disables access to the system for this user (without terminating the user’s account).</td>
</tr>
<tr class="even">
<td>FILE RANGE (#31.1)</td>
<td>Users who have VA FileMan privileges to create files can be given a numeric range of numbers to use as file numbers. Assigning number ranges acts as a safeguard to keep users from picking a number within a range that is nationally reserved for VistA software applications. It can also serve local database administration needs of segmenting local development by number ranges.</td>
</tr>
<tr class="odd">
<td>TERMINATION DATE (#9.2)</td>
<td>As described in the “<a href="#deactivating-users">Deactivating Users</a>” section, this field indicates when a user’s access privileges should be revoked.</td>
</tr>
<tr class="even">
<td>ALWAYS SHOW SECONDARIES (#200.11)</td>
<td>If set to <strong>YES</strong>, contents of a user’s SECONDARY MENU OPTIONS (#203) are shown when the user enters one question mark (<strong>?</strong>) at a menu prompt. Otherwise, the user <em>must</em> enter two question marks (<strong>??</strong>) to see their secondary menu.</td>
</tr>
<tr class="odd">
<td>PROHIBITED TIMES FOR SIGN-ON (#15)</td>
<td>As discussed with other signon parameters, this field can be used to regulate when the user can sign on to the system. The user setting takes precedence over any corresponding device setting.</td>
</tr>
<tr class="even">
<td><p>PHONE (HOME) (#.131)</p>
<p>OFFICE PHONE (#.132)</p>
<p>PHONE #3 (#.133)</p>
<p>PHONE #4 (#.134)</p>
<p>COMMERCIAL PHONE (#.135)</p>
<p>FAX NUMBER (#.136)</p></td>
<td>Set up phone numbers for the user in these fields.</td>
</tr>
<tr class="odd">
<td><p>VOICE PAGER (#.137)</p>
<p>DIGITAL PAGER (#.138)</p></td>
<td>Set up pager numbers for the user in these fields.</td>
</tr>
<tr class="even">
<td>LANGUAGE (#200.07)</td>
<td>Overrides the setting of the DEFAULT LANGUAGE field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. Both are used to set the <strong>DUZ(“LANG”)</strong> flag for each user. VA FileMan uses this setting to enable the display of language-specific dates and times, numeric formats, and dialogs.</td>
</tr>
</tbody>
</table>

<span id="_Ref236559165" class="anchor"></span>Table 4: Deactivate a User Option—Editable Fields/Attributes

### ScreenMan Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 27</u> - <u>Figure 31</u> are examples of the five ScreenMan forms displaying the fields that you can edit with the Edit an Existing User \[XUSEREDIT\] option:

<span id="_Ref530058564" class="anchor"></span>Figure 27: Edit an Existing User Option—Screen 1

Edit an Existing User

NAME: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: COMPUTER SPECIALIST NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS: ISCSTAFF

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION:

<u>SERVICE/SECTION</u>: INFORMATION SYSTEMS CENTER

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref456878156" class="anchor"></span>Figure 28: Edit an Existing User Option—Screen 2

Edit an Existing User

NAME: XUUSER,ONE Page 2 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NETWORK USERNAME: VHAIXXXUUSERO

TIMED READ (# OF SECONDS): 900

MULTIPLE SIGN-ON: ALLOWED MULTIPLE SIGN-ON LIMIT:

ASK DEVICE TYPE AT SIGN-ON: DON'T ASK AUTO MENU: YES, MENUS GENERATED

PROHIBITED TIMES FOR SIGN-ON: TYPE-AHEAD: ALLOWED

AUTO SIGN-ON:

Preferred Editor: SCREEN EDITOR - VA FILEMAN

ALLOWED TO USE SPOOLER: PAC:

CAN MAKE INTO A MAIL MESSAGE:

FILE RANGE:

ALWAYS SHOW SECONDARIES:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Toc207519113" class="anchor"></span>Figure 29: Edit an Existing User Option—Screen 3

Edit an Existing User

NAME: XUUSER,ONE Page 3 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROHIBITED TIMES FOR SIGN-ON:

PHONE: 510-768-6874 OFFICE PHONE: 510-768-6874

COMMERCIAL PHONE: FAX NUMBER:

VOICE PAGER: DIGITAL PAGER:

LANGUAGE:

Person Class Effective Expired

Technologists, Technicians and Other Tec DEC 7,2005 JAN 1,2006

Emergency Medical Service Providers JAN 1,2006 DEC 7,2005

Other Service Providers DEC 7,2005 DEC 8,2005

Allopathic and Osteopathic Physicians DEC 8,2005

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Toc207519114" class="anchor"></span>Figure 30: Edit an Existing User Option—Screen 4

Edit an Existing User

NAME: XUUSER,ONE Page 4 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RESTRICT PATIENT SELECTION: OE/RR LIST:

CPRS TAB ACCESS:

Name Description Effective Date Expiration Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref530058565" class="anchor"></span>Figure 31: Edit an Existing User Option—Screen 5

Edit an Existing User

NAME: XUUSER,ONE Page 5 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PERMANENT ADDRESS:

Street 1:

Street 2:

Street 3:

City:

State:

Zip Code:

E-Mail Address:

Is this person an active Trainee?:

VHA Training Fac.:

Start Date of Training: Last Training Month & Year:

Trainee Inactive (Date):

Program of Study:

Target Degree Lvl:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

### Additional Attributes Editable by Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some but *not* all user attribute fields can be edited by users using the Edit User Characteristics \[XUSEREDITSELF\] option. The only field the user can edit that is *not* part of the system manager’s Edit an Existing User form is the TEXT TERMINATOR field.

![](kernel-8-0-systems-management-signon-security-user-guide/048.png) REF: For a description of the fields users can edit (using the default Edit User Characteristics form and template), see <u>Table 2</u> in the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

### Edit User Characteristics Form and Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel exports a ScreenMan form and a template to be used in the Edit User Characteristics \[XUSEREDITSELF\] option. Both are called XUEDIT CHARACTERISTICS. The INPUT template by the same name is invoked if the ScreenMan form *cannot* be loaded on the current terminal type.

System administrators can substitute a locally-developed template by entering its name in the USER CHARACTERISTICS TEMPLATE field in the KERNEL PARAMETERS (#8989.2) file. System administrators can also design a customized form with the same name as the local INPUT template that is displayed instead, terminal type setup permitting. In other words, to invoke a locally modified display, an INPUT template *must* exist. If a ScreenMan form by the same name also exists, an attempt is made to display the form before defaulting to the INPUT template.

![](kernel-8-0-systems-management-signon-security-user-guide/049.png) REF: For more information on creating a local Edit User Characteristics form and template, see the *Kernel Installation Guide*.  
  
For a sample form, see the “[Edit User Characteristics Option](#edit-user-characteristics-option)” section.

## Deactivating and Reactivating Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides options to deactivate and reactivate users on the User Management \[XUSER\] menu. When users no longer need access privileges, system administrators can partially or entirely close access to their account.

<span id="_Toc193181638" class="anchor"></span>Figure 32: User Management Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

Deactivate a User \[XUSERDEACT\]

Purge Inactive Users' Attributes \[XUSERPURGEATT\]

Reactivate a User \[XUSERREACT\]

### Deactivating Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deactivate a User \[XUSERDEACT\] option lets you temporarily or permanently disable access for users. You can schedule termination of a user for a future date. The Deactivate a User \[XUSERDEACT\] option loads a ScreenMan form with the fields described in <u>Table 4</u>:

<table>
<caption><p><span id="_Ref488227830" class="anchor"></span>Table 5: Kernel Sign-On Log Report Data Values</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Field/Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DISABLE USER</td>
<td><p>Setting the DISABLE USER field to <strong>YES</strong> prevents a user from signing on, but leaves all their menus, security keys, and other attributes (essentially the user’s entire account) still enabled. It sets the DISUSER (#7) field in the user’s NEW PERSON (#200) file to <strong>YES</strong>.</p>
<p>You might want to use this feature to prevent access to your system by an external support person, except during pre-approved times (where you may want to monitor their actions). Setting DISUSER to <strong>YES</strong> prevents them from logging on to the system until you clear the field.</p>
<p>If you set this field to <strong>YES</strong>, <em>do not set any other fields</em> in the “<strong>Deactivate a User</strong>” form (they only apply to terminating a user). Then, to re-enable access, use the <strong>Reactivate a User</strong> [XUSERREACT] option.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/050.png) <strong>REF:</strong> For a description of the <strong>Reactivate a User</strong> [XUSERREACT] option, see the “<a href="#reactivating-users">Reactivating Users</a>” section.</p></td>
</tr>
<tr class="even">
<td>TERMINATION DATE (#9.2)</td>
<td><p>Terminating a user is the way to formally deactivate a user (as opposed to temporarily disabling their account). Setting this date effectively terminates that user’s account, effective from that date forward.</p>
<p>The <strong>Deactivate a User</strong> [XUSERDEACT] option automatically performs the following steps when you deactivate a user:</p>
<ul>
<li><p>Revokes the user’s status as an authorized sender of any mail groups.</p></li>
<li><p>Revokes the user’s status as a surrogate.</p></li>
<li><p>Revokes the user’s status as a Secure Menu Delegation delegate.</p></li>
<li><p>Deletes the user’s Access Code, Verify Code, Electronic Signature code, VA FileMan Access Code (that is FILE MANAGER ACCESS CODE [#3] field), and <strong>Programmer</strong> Access Code.</p></li>
<li><p>Deletes the user’s <strong>MENU</strong> templates.</p></li>
<li><p>Deletes the user’s delegated options.</p></li>
<li><p>Purges the <strong>^DISV</strong> global on that CPU for that user.</p></li>
</ul>
<p>You can also decide whether all mail messages and all security keys for the account are deleted on the TERMINATION DATE with the final two fields in the <strong>Deactivate a User</strong> [XUSERDEACT] option (DELETE ALL MAIL ACCESS and DELETE KEYS AT TERMINATION). If the user is expected to return to the facility and needs to have the user account reopened, security keys and mail could be retained.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/051.png) <strong>REF:</strong> For more information on cleaning up user access and privileges at termination, see the “<strong>XU USER TERMINATE Option</strong>” section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf"><em>Kernel 8.0 Developer’s Guide: Signon/Security Developer Tools User Guide</em></a>.</p></td>
</tr>
<tr class="odd">
<td>DELETE ALL MAIL ACCESS (#9.21</td>
<td>Setting the DELETE ALL MAIL ACCESS field causes all mail messages for the user to be deleted when their account is terminated on the TERMINATION DATE.</td>
</tr>
<tr class="even">
<td>DELETE KEYS AT TERMINATION (#9.22)</td>
<td><p>Setting the DELETE KEYS AT TERMINATION field causes all security keys for the user to be deleted at termination (except security keys marked “<strong>KEEP AT TERMINATE</strong>”).</p>
<p>As discussed in the “<a href="\l">Security Keys</a>” section, the application developer can export a security key with the KEEP AT TERMINATE field set to <strong>YES</strong> in such a situation. The <strong>PROVIDER</strong> security key, included with Kernel, has the flag set to <strong>YES</strong> for this purpose. Although a user may have been deactivated, it could be important to continue a processing activity that the user had authorized, based on privileges associated with a security key. A medical order could continue to hold an approved status, for example, even though the authorizing provider had been deactivated.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref488227830" class="anchor"></span>Table 5: Kernel Sign-On Log Report Data Values

### Automatically Deactivating Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automatic Deactivation of Users \[XUAUTODEACTIVATE\] option finds all users in the NEW PERSON (#200) file with a TERMINATION DATE (#9.2) in the past, but who still have an Access Code. In addition, it also looks to see if there are any users who have *not* signed on in the last “n” days.

![](kernel-8-0-systems-management-signon-security-user-guide/052.png) NOTE: Kernel records all signons to VistA using appropriate user credentials through either of the following methods:

- Access Codes.
- 2-Factor Authentication (2FA)—Digital certificate in a VA-approved smart card, such as the Personal Identification Verification (PIV) smart card plus a Personal Identification Number (PIN).

The Automatic Deactivation of Users \[XUAUTODEACTIVATE\] option terminates any users who fit these criteria. Any such users are users who had been scheduled for termination but were *not* terminated (usually because the task that should have terminated them did *not* run). It acts as a safety net to ensure that all users who were scheduled for termination are, in fact, terminated. It should be scheduled to run on a regular basis.

The Automatic Deactivation of Users \[XUAUTODEACTIVATE\] option is normally tasked to run daily through TaskMan.

![](kernel-8-0-systems-management-signon-security-user-guide/053.png) REF: For *recommended* frequency of scheduling, see the *Kernel Installation Guide*.

Because the Automatic Deactivation of Users \[XUAUTODEACTIVATE\] option is *not* intended for interactive use, it is placed on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu.

#### Bulletin Notification

As of Kernel Patch XU\*8.0\*693, when the Automatic Deactivation of Users \[XUAUTODEACTIVATE\] option is used, it generates the XUSERDEAC MailMan bulletin, which is sent to the designated ISO SECURITY mail group in the bulletin's parameters. The Information Security Officers (ISOs) and their alternates are instructed to request membership in the ISO SECURITY mail group at their facility.

<span id="_Ref67482241" class="anchor"></span>Figure 33: Sample XUSERDEAC MailMan Bulletin

Subj: XUSER DEACTIVATION \[#55995\] 03/15/18@09:48 8 lines

From: XULASTNAME,ONEFIRSTNAME In 'IN' basket. Page 1

--------------------------------------------------------------------------

User name : XULAST,ONEFIRST C

Title : DEVELOPER

Service : VHIT Field Office

IEN : 1039

Station \# : 662 SAN FRANCISCO

was deactivated on Mar 15, 2018.

Enter message action (in IN basket): Ignore//

The XUSERDIS MailMan bulletin was created to differentiate between DISUSERed and Deactivated users. Setting the DISUSER (#7) field in the NEW PERSON (#200) file to “Yes” for a user triggers the XUSERDIS bulletin. Setting the DISUSER (#7) field in the NEW PERSON (#200) file field to “Yes” only disables the user's ability to log on to the VistA system. It leaves all menus, security keys, and other attributes intact. The XUSERDIS bulletin is sent to the designated ISO SECURITY mail group in the bulletin's parameters. The data fields displayed in the XUSERDIS bulletin are the same as the XUSERDEAC bulletin.

<span id="_Ref67482245" class="anchor"></span>Figure 34: Sample XUSERDIS MailMan Bulletin

Subj: USER DISUSERED \[#306499\] 02/26/18@16:46 1 line

From: LASTNAME,FIRSTNAME (VHA OCC) In 'IN' basket. Page 1

--------------------------------------------------------------------------

User name : LAST,TEST C

Title : DEVELOPER

Service : VHIT Field Office

IEN : 1039

Station \# : 662 SAN FRANCISCO

was DISUSERED on Apr 05, 2018.

Enter message action (in IN basket): Ignore//

![](kernel-8-0-systems-management-signon-security-user-guide/054.png) REF: For more information on the XUSERDEAC and XUSERDIS MailMan bulletins, see the “Bulletins” section in the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.

#### Termination Process

The termination process does the following:

- Sets the DISUSER (#7) field in the NEW PERSON (#200) file to YES (1).
- Deletes the user’s Access Code.
- Deletes the user’s security keys.
- Calls the XU USER TERMINATE protocol in the OPTION (#19) file so other applications can take any action they need.
- If the DELETE ALL MAIL ACCESS (#9.21) field in the NEW PERSON (#200) file is set to YES, then the user is also removed from the VistA MailMan system, which deletes their MailMan mailboxes and deletes them from any mail groups.

![](kernel-8-0-systems-management-signon-security-user-guide/055.png) CAUTION: Kernel patch XU\*8\*645 created the XU645 parameter. It determines if a terminated user information should be purged from the system (Inspector General investigation request). When XU645 is set to YES, then data is deleted and the background AUTODEACTIVATE job purges those users who were previously terminated. The default value for XU645 is blank, which is equivalent to NO; it only deletes the user’s Access Code and does *not* delete any other information or trigger any background jobs.

#### Academic Affiliation Waiver

The *VA Handbook 6500* page 60 (POLICY AND PROCEDURES, Technical Controls, Logical Access Controls), Item “d” states that accounts are automatically disabled if inactive for 30 days. This requirement is repeated in *VA Handbook 6500* Appendix D.

The Office of Academic Affiliation requested a waiver for the 30-day disabling of inactive accounts asking it to be 90 days and the waiver was approved.

![](kernel-8-0-systems-management-signon-security-user-guide/056.png) REF: A copy of the approved waiver is available as an attachment to Remedy Ticket \#283028.

Kernel patch XU\*8.0\*514 added the ACADEMIC AFFILIATION WAIVER (#13) field to the KERNEL SYSTEM PARAMETERS (#8989.3) file. This field is used to control the LAST SIGN-ON DATE/TIME (#202) field in the NEW PERSON (#200) file. If the Office of Academic Affiliation waiver is applicable to a site, the site can set the ACADEMIC AFFILIATION WAIVER (#13) field to YES (1). The default for this field is NULL.

When the ACADEMIC AFFILIATION WAIVER (#13) field is set to YES, the users is only automatically disabled if they have been inactive for over 90 days (that is LAST SIGN-ON DATE/TIME is over 90 days). If it is *not* set, this option works as usual (that is 30-day limit).

### Purging Mail and Security Keys for Inactive Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Purge Inactive Users’ Attributes \[XUSERPURGEATT\] option to clean up files. It removes all mailboxes, messages, mail groups, and security keys for users who have been terminated. If any of these users still retain Access Codes, they are deleted.

This is particularly significant with mail. A mail message *cannot* be completely removed from a system until all recipients have deleted it from their mail baskets. If a user is no longer active, then it becomes unlikely that the message ever gets purged.

There are two modes of running this option. You can VERIFY the process for each user that the computer selects as eligible. If you choose *not* to verify the process for each user, then for every user with a *non*-future TERMINATION DATE, their set of security keys, mail groups, messages, and mail baskets are deleted.

### Reactivating Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Reactivate a User \[XUSERREACT\] option to re-enable access for a user who has either been terminated, or whose access has been temporarily disabled. To re-enable access for someone whose account is merely disabled (with the DISUSER field set to YES), use this option to simply clear the DISUSER field. Otherwise, using this option, you can fill in all the fields needed for an active account (that is FILE MANAGER ACCESS CODE \[#3\] field, PRIMARY MENU OPTION \[#201\], and so on).

When you reactivate a user, you are asked whether to deny access to old mail messages. If the reactivated user account is a less privileged account than previously, it may be appropriate to deny the user access to messages that were received in the user’s prior capacity. Even if that user’s mailbox was deleted at termination, once the user is reactivated, an old message would be delivered if responded to by another recipient.

## User Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides the User Management Menu \[XUOPTUSER\] located under the Operations Management \[XUSITEMGR\] menu. This menu provides a set of options for system administrators to monitor and support users logged onto the system. It includes the options shown in <u>Figure 35</u>:

<span id="_Ref511384654" class="anchor"></span>Figure 35: User Management Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

User Management Menu ... \[XUOPTUSER\]

FIND Find a user \[XU FINDUSER\]

PXY Proxy User List \[XUSAP PROXY LIST\]

List users \[XUSERLIST\]

Print Sign-on Log \[XUSC LIST\]

Proxy (Connector) Detail Report \[XUSAP PROXY CONN DETAIL ALL\]

Proxy (Connector) Inquire \[XUSAP PROXY CONN DETAIL INQ\]

Release user \[XUSERREL\]

Remote Access User Sign-on Log \[XUSEC REMOTE ACCESS\]

User Inquiry \[XUSERINQ\]

User Status Report \[XUUSERSTATUS\]

Users with Foreign Visits \[XUS VISIT USERS\]

### Find a User Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Find a User \[XU FINDUSER\] option is used to find a user who is currently signed on to the system in this UCI group. If you are on the same CPU as the user, this option also shows the menu path of the user. The option finds users based on the “CUR” cross-reference of the SIGN-ON LOG (#3.081) file.

### Proxy User List Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Proxy User List \[XUSAP PROXY LIST\] option runs a report listing any users in the NEW PERSON (#200) file that have a USER CLASS (#9.5) field of APPLICATION PROXY or CONNECTOR PROXY.

### List Users Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Users \[XUSERLIST\] option lists all users known to the system.

### Print Sign-on Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Sign-on Log \[XUSC LIST\] option prints out a Kernel sign-on log report (see <u>Figure 36</u>) that lists data values from fields in the SIGN-ON LOG (#3.081) file.

<u>Table 5</u> lists the data displayed on the Kernel sign-on log report (see <u>Figure 36</u>):

<table>
<caption><p><span id="_Toc207519141" class="anchor"></span>Table 6: Kernel Signon Auditing Files</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Report Field</th>
<th>File #3.081 Field Reference</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sign-on time</td>
<td>DATE/TIME (#.001)</td>
<td><p>This is the date and time that the user signed onto the system.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/057.png) <strong>NOTE:</strong> To allow more than one signon per second the time can have values that show hundredth of a second.</p></td>
</tr>
<tr class="even">
<td>ELAPSED TIME (MINUTES)</td>
<td>ELAPSED TIME (MINUTES) (#99)</td>
<td>This is the amount of time in minutes that the user has been signed onto the system.</td>
</tr>
<tr class="odd">
<td>USER</td>
<td><p>USER (#.01)</p>
<p>Points to the NEW PERSON (#200) file.</p></td>
<td>This is the username signed onto the system (that is <strong>LAST NAME,FIRST NAME</strong>).</td>
</tr>
<tr class="even">
<td><strong>$I</strong></td>
<td>DEVICE $I (#1)</td>
<td>This is the <strong>$I</strong> device to which the user signed onto the system. This field holds the Hardware port name that the operating system (OS) can identify when referencing a port on a CPU. On layered systems where opening of host files is supported, this field can hold the host file name.</td>
</tr>
<tr class="odd">
<td>NODE NAME</td>
<td>NODE NAME (#10)</td>
<td>This is the VAX/VMS cluster node name or system name to which the user signed onto the system.</td>
</tr>
<tr class="even">
<td>IPV6 ADDRESS</td>
<td>IPV6 ADDRESS (#100)</td>
<td><p>This is the IPV6 address from the calling system. Under the Dynamic Host Control Protocol (DHCP) Internet Protocol (IP) addresses are dynamically allocated, so more than one client could have used the same IP address over some time-period. Also, under IPv6, each client could have more than one IP address.</p>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/058.png) <strong>NOTE:</strong> IPv4 addresses are stored as IPv4-mapped IPv6 addresses, and all addresses are stored in expanded IPv6 format.</p></td>
</tr>
<tr class="odd">
<td>LOA</td>
<td>LEVEL OF ASSURANCE (#101)</td>
<td><p>This is the Level of Assurance (LOA) of the user’s authentication into VistA. There are currently four levels defined by the <a href="http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63-2.pdf">National Institution of Standards and Technology Special Publication (NIST SP) 800-63-2 Electronic Authentication Guideline</a>:</p>
<ul>
<li><p><strong>Level 1—</strong>No identity proofing requirement. This generally refers to a “self-asserted” user identity and is the lowest form of authentication. This form of authentication does <em>not</em> satisfy <a href="http://www1.va.gov/vapubs/viewPublication.asp?Pub_ID=56">VA Handbook 6500</a> security requirements.</p></li>
<li><p><strong>Level 2—</strong>Single factor authentication. This form of authentication includes username/password or, in the case of VistA, Access/Verify Code authentication.</p></li>
<li><p><strong>Level 3—</strong>Multi-factor authentication. This form of authentication includes VA 2-Factor Authentication (2FA) using smart cards (PKI certificates) and Personal Identification Number (PIN).</p></li>
<li><p><strong>Level 4—</strong>Highest practical authentication assurance. At this level, in-person identity proofing (such as fingerprint or retinal scan) is used to authenticate and identify the user.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>REMOTE APP</td>
<td><p>REMOTE APP (#18)</p>
<p>Points to the REMOTE APPLICATION (#8994.5) file</p></td>
<td><p>The REMOTE APP (#18) field was added to the Kernel sign-on log report as of Kernel Patch XU*8.0*630. The data identifies how users are accessing VistA. For example, through any of the following applications:</p>
<ul>
<li><p>JLV Application using National Health Information Network (NHIN).</p></li>
<li><p>VistA Applications (such as CPRS GUI, VistA Imaging VIX, and so on).</p></li>
<li><p>Terminal Emulator Software (such as Micro Focus<sup>®</sup> Reflection, Attachmate<sup>®</sup> Reflection, other terminal emulator, or generic default for a telnet/SSH interface).</p></li>
<li><p>Web Services.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>CREDENTIAL</p>
<p>TYPE</p></td>
<td>CREDENTIAL TYPE (#102)</td>
<td><p>This field contains the value of the type of credential used during VistA Kernel signon. In the past, it was assumed credentials were Access/Verify Codes; now it lists other credentials being used:</p>
<ul>
<li><p><strong>AVCODES</strong></p></li>
<li><p><strong>SSOI<br />
</strong></p></li>
</ul>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/059.png) <strong>NOTE:</strong> This field was added with Kernel Patch XU*8.0*701.</p></td>
</tr>
<tr class="even">
<td><p>CREDENTIAL</p>
<p>WARNINGS</p></td>
<td>CREDENTIAL WARNINGS (#103)</td>
<td><p>This field contains a list of credential verification failures that are considered warnings, when setting the STRICT TOKEN VALIDATION (#220) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file to <strong>NO</strong>, <em>non</em>-strict validation:</p>
<ul>
<li><p><strong>CAFILE—</strong>CA certificate chain file “<strong>cache.cer</strong>” has not been installed.</p></li>
<li><p><strong>DIGEST—</strong>Token has been modified.</p></li>
<li><p><strong>SIGNATURE—</strong>Token might have been reformatted and signature verification failed.</p></li>
<li><p><strong>EXPIRED—</strong>Token has expired.</p></li>
</ul>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/060.png) <strong>NOTE:</strong> This field was added with Kernel Patch XU*8.0*701.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207519141" class="anchor"></span>Table 6: Kernel Signon Auditing Files

<span id="_Ref488222885" class="anchor"></span>Figure 36: Sample Kernel Sign-On Log Report

SIGN-ON LOG List NOV 06, 2019@15:03 PAGE 3

ELAPSED

TIME

Sign-on time (MINUTES) USER \$I NODE NAME

IPV6 ADDRESS LOA REMOTE APP

CREDENTIAL

TYPE

CREDENTIAL WARNINGS

--------------------------------------------------------------------------------

OCT 30,2019@05:56:19 3 XUUSER,NINE /dev/pts/ vhaausdhct033

0000:0000:0000:0000:0000:FFFF:0AEC:84EF 2 TERMINAL EMULATOR

AVCODES

OCT 29,2019@12:31:26 6 XUUSER,SEVEN /dev/pts/ vhaausdhct033

0000:0000:0000:0000:0000:FFFF:0AEC:84E4 3 MICRO FOCUS REFLECTION

SSOI

OCT 29,2019@11:22:04 10 XUUSER,TEN         /dev/pts/ vhaausdhct033

0000:0000:0000:0000:0000:FFFF:0A06:0226 3 REMOTE APP1

SSOI

CAFILE;SIGNATURE;

OCT 29,2019@12:11:36 26 XUUSER,ELEVEN /dev/pts/ vhaausdhct033

0000:0000:0000:0000:0000:FFFF:0A06:0226 3 REMOTE APP2

SSOI

SIGNATURE;

### Proxy (Connector) Detail Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Proxy (Connector) Detail Report \[XUSAP PROXY CONN DETAIL ALL\] option provides information about CONNECTOR PROXY accounts for the purposes of:

- Monitoring compliance with the 3-year mandate (per VA Handbook 6500) to expire/change Verify Codes for service accounts.
- Reporting any misconfigured CONNECTOR PROXY accounts.
- Listing account activity to help determine whether accounts are active and are being accessed from which remote locations.

When running the report, the following options determine how much additional content is listed for each account:

- Check/display connector proxy fields? YES/NO (checks for misconfigured accounts).
- Scan sign-on log for connector proxy activity? YES/NO (lists account activity).

Possible categorizations for whether accounts are reported as “Compliant w/3-year Service Account Mandate?” are:

- YES (account is compliant).
- \*\*\* NO \<---- MUST FIX \*\*\* (date created and date verify code last changed \> 3 years in the past).
- No, but user *not* active.
- UNABLE TO DETERMINE (until patch XU\*8.0\*574, date verify code last changed for Connector Proxy accounts was incorrectly recorded as 4/10/2005)
- Unable to determine but *not* active.

If an account’s Date Verify Code Last Changed is listed as “(changed but date *not* recorded)”, that means the “fake” 4/10/2005” date is present, and unless the account was created within the last 3 years, it is impossible to determine if the account complies with the 3-year mandate.

Also, if there is a value in the XUS LOGON ATTEMPT COUNT field, that value is displayed, as it could indicate a remote system attempting to connect and failing with an invalid Verify Code.

If the option to “Check/display connector proxy fields?” is selected, the following checks are performed:

- Warnings: (any field listed in the warning section should *not* be populated. However, before changing, consult the National Help Desk or Customer Support as some applications may (currently) be depending (incorrectly) on a misconfigured connector configuration.)
- Values for other fields allowed/expected: (field normally populated for connector proxies).
- Other Fields Populated (not expected fields, but *not* problematic either).
- Other Multiples Populated (not expected, but *not* problematic either).

If the option to “Scan sign-on log for connector proxy activity?” is selected, the report scans the sign-on log for all signon activity associated with the account. Any activity found is displayed, organized by client IP address, and within IP address, by date of signon.

The purpose of this report section is to help sites determine the following:

- Which accounts are active.
- Which external systems (by IP address) are logging onto the site with the specified account.

This helps determine which remote applications a change to the account (such as Verify Code change) might impact, and it also helps a site determine whether too many remote applications/data centers are using the same account (which could result in a more widespread service disruption if an account *must* be changed).

![](kernel-8-0-systems-management-signon-security-user-guide/061.png) NOTE: This option can be scheduled.

### Proxy (Connector) Inquire Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Proxy (Connector) Inquire \[XUSAP PROXY CONN DETAIL INQ\] option provides information about CONNECTOR PROXY accounts for the same purposes as the [Proxy (Connector) Detail Report Option](#proxy-connector-detail-report-option); however, it allows the selection of a specific NEW PERSON (#200) file CONNECTOR PROXY entry.

### Release user Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If multiple signons are prohibited, problems can occur if users experience an abnormal exit such that the signon record *cannot* be cleared. System administrators can use the Release user \[XUSERREL\] option to remedy the problem for individual users.

To clear all users on startup, schedule the Clear all users at startup \[XUSER-CLEAR-ALL\] option.

### Remote Access User Sign-on Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Access User Sign-on Log \[XUSEC REMOTE ACCESS\] option prints sign-on log entries from remote users (VISITORS) that have been authenticated on an external system (usually another VistA server) using Broker Security Enhancement (BSE) or the (deprecated) Medical Domain Web Service (MDWS) visitor access.

The report shows:

- Remote Site Name.
- Date of First Visit.
- Date of Last Visit.

BSE allows users to be validated through 2-Factor Authentication (2FA) or the traditional VistA Access and Verify Codes on their home system and then carry that authentication to other VistA systems. A packet of information is retrieved from the authenticating (home) site and is entered in the NEW PERSON (#200) file, so that a trace to the original authentication can be made.

### User Inquiry Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Inquiry Option \[XUSERINQ\] option displays various attributes of a specified user. If the user is currently signed on, it displays the following:

- Job and Device numbers.
- Signon time.
- What option is being executed.

Otherwise, it displays the last signon time. It also displays which security keys are held by the user.

### User Status Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Status Report \[XUUSERSTATUS\] option produces a report of the users currently signed on to this CPU and UCI. It shows the option each user is running and when they signed on, as well as their device and job numbers.

### Users with Foreign Visits Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Users with Foreign Visits \[XUS VISIT USERS\] option shows NEW PERSON (#200) file entries that have been VISITORS to this site using Broker Security Enhancement (BSE) or the (deprecated) Medical Domain Web Service (MDWS) visitor access.

## Signon Audits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Signon events are recorded in the SIGN-ON LOG (#3.081) file. Statistics, such as the time of access and the user’s identity, are stored for audit purposes. If the user exits normally (is *not* “bumped” off the system), the signon record includes the time of exit. If the user exits abnormally with an error or enters Programmer mode, the signon record *cannot* include a time of exit.

Information about signon activity can be reviewed with options on the Systems Manager Menu \[EVE\] and Operations Management \[XUSITEMGR\] menus.

The SIGN-ON LOG (#3.081) file is purged with the Purge Sign-On log \[XUSCZONK\] option that should be tasked to run on a regular schedule (such as every night). This option *cannot* be reached from Menu Manager; like other options that should only be queued, it is on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu.

As of Kernel Patch XU\*8.0\*756, the following functionality enhancements were made:

- Added the SIGN-ON LOG RETENTION (#221) parameter field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. This parameter determines the number of entries (number of days) to retain data in the Kernel sign-on log \[SIGN-ON LOG (#3.081) file\]. Larger values will consume more disk space; so, sites should evaluate the impact on data storage *before* changing the default value of 365 days.
- Added the "SIGN-ON LOG RETENTION" field to the Enter/Edit Kernel Site Parameters \[XUSITEPARM\] option form (<u>Figure 12</u>). This new form field allows the user to set the value of the SIGN-ON LOG RETENTION (#221) parameter field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.
- Enhanced the SCPURG^XUSPURGE routine. It updated the Purge Sign-on Log \[XUSCZONK\] option so that it protects sign-on log entries for at least the number of days specified by the ISO, or the default 365 days as defined in the SIGN-ON LOG RETENTION (#221) parameter field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.

### Signon Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Statistics about active sessions can be obtained with the CPU/Service/User/Device Stats \[XUSTAT\] option. This option permits sorting by CPU, by the user’s Service/Section (such as MAS), by individual users, or by devices.

<span id="_Toc193181641" class="anchor"></span>Figure 37: CPU/Service/User/Device Stats Option

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

<span class="mark">CPU/Service/User/Device Stats</span> \[XUSTAT\]

### Failed Access Attempts Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Access/Verify Codes Authentication

When a user enters invalid Access and Verify Code pairs, the number of attempts is recorded, and the device appears to lock after the site parameter limit of failed access attempts is reached as designated in the DEFAULT \# OF ATTEMPTS field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. After this point, Signon/Security continues to record what the user types (but only to create a record in the FAILED ACCESS ATTEMPTS LOG \[#3.05\] file).

![](kernel-8-0-systems-management-signon-security-user-guide/062.png) REF: For more information on the DEFAULT \# OF ATTEMPTS field in the KERNEL SYSTEM PARAMETERS (#8989.3) file, see Section [3.1.2.1](#signon-attempts-and-device-lock-out-times), “[Signon Attempts and Device Lock-out Times](#signon-attempts-and-device-lock-out-times).”

If a valid Access Code is entered, Signon/Security can link the attempt with a known user and records that user’s name in the log. Since it is a valid code, its text is *not* recorded in the log. The text of subsequently entered invalid Verify Codes can, however, be recorded as clues to the source of the access attempt. If the Access Code is *not* valid, a user’s name *cannot* be associated but the text of the attempt can be recorded.

The log also records the following:

- Time of day.
- Device used.
- CPU/UCI location.

#### PIV 2-Factor Authentication (2FA)

With Personal Identity Verification (PIV) 2-Factor Authentication (2FA) the following occurs:

1.  User gets *one* attempt with PIV card authentication. If it fails, the failure is recorded in the FAILED ACCESS ATTEMPTS LOG \[#3.05\] file and the authentication process automatically reverts to using the Access and Verify Codes.

![](kernel-8-0-systems-management-signon-security-user-guide/063.png) NOTE: Prior to Kernel Patch XU\*8\*701, these failures were *not* being recorded, and it was very difficult for sites to troubleshoot PIV card failures.

5.  User gets *as many attempts* using Access and Verify Codes as they are configured in the DEFAULT \# OF ATTEMPTS field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. When the number is reached, the failure is recorded in the FAILED ACCESS ATTEMPTS LOG \[#3.05\] file.

![](kernel-8-0-systems-management-signon-security-user-guide/064.png) NOTE: When troubleshooting issues related to PIV card authentication or other related credentials like Access/Verify Codes, the site can “temporarily” set the value of the FAILED ACCESS ATTEMPTS field in the Establish System Audit Parameters \[XUAUDIT\] option to the following value:

ALL DEVICES/TEXT RECORDED

![](kernel-8-0-systems-management-signon-security-user-guide/065.png) CAUTION: Due to the unexpected number of PIV authentication failures, your site may need to increase the frequency of running the Failed Access Attempts Log Purge \[XUFPURGE\] option for the FAILED ACCESS ATTEMPTS LOG \[#3.05\] file.

#### PIV 2-Factor Authentication Failures

Failures recorded when using the PIV 2-Factor Authentication (2FA) authentication contain the value of the SecID and name of the user identified in the SSOi token derived from PIV 2FA. Other failures in validating the SSOi token or other tokens are also listed, as shown in <u>Figure 38</u>.

<span id="_Ref29220325" class="anchor"></span>Figure 38: Failed Access Attempts Log Report

LOG OF USER FAILED ACCESS LIST NOV 6,2019 3:38 PM PAGE 1

--------------------------------------------------------------------------------

\*\*\* USER NAME:

DATE/TIME OF ATTEMPT: NOV 6,2019@15:37:40

NUMBER OF ATTEMPTS: 3 TYPE OF FAILED ATTEMPT: ACCESS

CPU: KRN UCI: KRN DEVICE: TELNET (LINUX) (10.6.2.38)

TEXT ENTERED:

Access: XXXXX

Access: YYYYYY

Access: ZZZZZZ

\*\*\* USER NAME:

DATE/TIME OF ATTEMPT: NOV 6,2019@15:37:13

NUMBER OF ATTEMPTS: 1 TYPE OF FAILED ATTEMPT: SSOI

CPU: KRN UCI: KRN DEVICE: TELNET (LINUX) (10.6.2.38)

TEXT ENTERED:

NON-STRICT Failed-verifications: CAFILE;SECID;SIGNATURE;   ERROR:User not found. SECID not linked to existing user, SECID:1005555055 NAME:TEN XUUSER

#### Failed Verifications for Token (SSOi)

The following is a list of some failed verification that you may encounter:

- SECID—VistA Kernel could not match the SecID in the token to an entry in the NEW PERSON (# 200) file.
- EXPIRED—Token has expired.
- CAFILE—CA certificate chain file “cache.cer” has not been installed.
- DIGEST—Token has been modified.
- SIGNATURE—Token might have been reformatted and signature verification failed.
- EXPIRED—Token has expired.

#### Kernel Signon Auditing Files

<table style="width:100%;">
<caption><p><span id="_Ref175452908" class="anchor"></span>Table 7: File Access—Security Level Properties</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Global Location</th>
<th>Set Parameters</th>
<th>Display Parameters</th>
<th>Initiate/ Terminate</th>
<th>Print Reports</th>
<th>Purge Logs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SIGN-ON LOG (#3.081)</td>
<td><strong>^XUSEC(0,</strong></td>
<td>Predefined</td>
<td>N/A</td>
<td>Always done</td>
<td>Print Sign-on Log [XUSC LIST]</td>
<td>Purge Sign-on Log [XUSCZONK]</td>
</tr>
<tr class="even">
<td>FAILED ACCESS ATTEMPTS LOG (#3.05)</td>
<td><strong>^%ZUA(3.05,</strong></td>
<td>Establish System Audit Parameters [XUAUDIT]</td>
<td>Display the Kernel Audit Parameters [XU-SPY-SHOW]</td>
<td>On/Off switch</td>
<td><p>Devices: Device Failed Access Attempts [XUFDEV]</p>
<p>Users: User Failed Access Attempts [XUFDISP]</p></td>
<td>Failed Access Attempts Log Purge [XUFPURGE]</td>
</tr>
<tr class="odd">
<td>OLD ACCESS AND VERIFY CODES (#200 XREF)</td>
<td><strong>^VA(200,</strong></td>
<td>Predefined</td>
<td>N/A</td>
<td>Always done</td>
<td>N/A</td>
<td>Purge Log of Old Access and Verify Codes [XUSERAOLD]</td>
</tr>
</tbody>
</table>

<span id="_Ref175452908" class="anchor"></span>Table 7: File Access—Security Level Properties

### Purge Old Access and Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181643" class="anchor"></span>Figure 39: Purge Log of Old Access and Verify Codes Option

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

<span class="mark">Purge Log of Old Access and Verify Codes</span> \[XUSERAOLD\]

The Purge Log of Old Access and Verify Codes \[XUSERAOLD\] option purges all inactive Access and Verify Codes, which allows for the recycling of codes. Old Access and Verify Codes are stored so that users *cannot* pick a previously used code when required to choose a new code. If old codes are stored indefinitely, though, it may become difficult for users to invent new codes. When you use this option interactively, you can purge codes older than a retention period you specify, from 7 to 90 days. When scheduled, the retention period defaults to 90 days, but can be changed to anything from 30 to 90 days by putting the number of days in the TASK PARAMETERS field of the OPTION SCHEDULING (#19.2) file.

The log of Access Codes is stored in the whole-file AOLD cross-reference of the NEW PERSON (#200) file. The log of Verify Codes is stored per user in the VOLD cross-reference of the NEW PERSON (#200) file, *not* a whole-file cross-reference). Thus, Verify Codes are *not* necessarily unique between users, while Access Codes are unique.

# File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Access Security system is an optional Kernel module. It provides an enhanced security mechanism for controlling user access to VA FileMan files.

![](kernel-8-0-systems-management-signon-security-user-guide/066.png) REF: For more information on File Access Security, see the *VA FileMan (Version 22.2) and Kernel (Version 8.0) File Access Security* supplemental documentation located on the VA Software Document Library (VDL) at: [VDL VA FileMan Application Documents](http://www.va.gov/vdl/application.asp?appid=5)

## File Access Security User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a user, you typically access VistA data by use of application options. You enter data into files and retrieve information from files through the menu options within the software. Except under a few unusual circumstances, your use of the system is *not* affected by the File Access Security system. If you need to work directly with files by using VA FileMan options, however, you are affected.

VA FileMan options provide direct access to data files. <u>Figure 40</u> lists some sample VA FileMan options:

<span id="_Ref175452546" class="anchor"></span>Figure 40: Sample VA FileMan Menu Options

Select VA FileMan Option: <span class="mark">?</span><span class="mark">\<Enter\></span>

Enter or Edit File Entries \[DIEDIT\]

Print File Entries \[DIPRINT\]

Search File Entries \[DISEARCH\]

Inquire to File Entries \[DIINQUIRE\]

If the File Access Security system is implemented, the only files you can access directly through VA FileMan options are those listed in your ACCESSIBLE FILE (#32) Multiple field in the NEW PERSON (#200) file. System administrators grant file access by using a submenu on the User Management \[XUSER\] menu.

There are six levels of File Access Security properties (listed alphabetically):

- AUDIT
- DATA DICTIONARY (“DD”)
- DELETE (“DEL”)
- LAYGO
- READ (“RD”)
- WRITE (“WR”)

![](kernel-8-0-systems-management-signon-security-user-guide/067.png) REF: These File Access Security level properties are described in <u>Table 7</u>.

Each level of access is granted as YES or NO. If the File Access Security system is implemented, file access is controlled by these YES/NO flags, *not* by the matching of your FILE MANAGER ACCESS CODE (#3) field string in the NEW PERSON (#200) file with security placed on the file.

If you have *not* been granted any security access to VA FileMan files, entering two question marks (??) when prompted for a file name/number shows no files to access:

<span id="_Toc193181647" class="anchor"></span>Figure 41: User has *Not* been Granted Security Access to any VA FileMan Files—Sample User Dialog

Select VA FileMan Option: <span class="mark">ENTER OR EDIT FILE ENTRIES \<Enter\></span>

INPUT TO WHAT FILE: <span class="mark">?? \<Enter\></span>

INPUT TO WHAT FILE:

In this case, you need to contact the system administrators to get access to the VA FileMan files you need.

File Access Security is also invoked when an option uses VA FileMan’s Line Editor. In particular, the Transfer Lines from Another Document option, which is hard coded in the DIWE routine and is also referred to as the Line Editor, does *not* permit access to other word-processing documents in the current file or other files unless READ access to that file has been explicitly granted. If you need to transfer text from other files using the Line Editor, contact the system administrators to request access to those files.

## File Access Security System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to introduction of the File Access Security system, user access to VA FileMan files through VA FileMan options was controlled by matching a character in a user’s FILE MANAGER ACCESS CODE (#3) field \[the DUZ(0) string\] in the NEW PERSON (#200) file with a character in the file’s top level file security fields.

Kernel’s optional File Access Security system uses a different method. It allows you to control access to files for any user using VA FileMan options directly. Access is granted (or denied) by adding (or removing) a file from a user’s ACCESSIBLE FILE (#32) Multiple field in their NEW PERSON (#200) file entry.

The File Access Security system does *not* affect access to files through *non*-VA FileMan options; security in this case is managed by controlling the availability of the option.

![](kernel-8-0-systems-management-signon-security-user-guide/068.png) REF: For exceptions, see the “[When is File Access Security Checked?](#when-is-file-access-security-checked)” section.

If a user’s DUZ(0) is set to the at-sign (@; Programmer access), VA FileMan options allow complete file access. If it is set to anything else (except the caret \[^\]), VA FileMan options use the ACCESSIBLE FILE (#32) Multiple field specifications in the NEW PERSON (#200) file to grant varying levels of file access.

![](kernel-8-0-systems-management-signon-security-user-guide/069.png) NOTE: The caret (^) overrides the at-sign (@; Programmer access).

This higher degree of control over a user’s file access comes at a price, because it requires more management on the system administrator’s part to provide each user access to the files to which they need access. However, the payoff in using the File Access Security system is in enhanced control and security for VA FileMan files.

### When is File Access Security Checked?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using VA FileMan options, access to files through the File Access Security system is checked.

When initially accessing data in a file through software options (such as options using VA FileMan Application Program Interfaces \[APIs\]), File Access Security is *not* checked. File Access Security is checked, however, when calling the following VA FileMan APIs:

- ^DIC calls—Adding an entry to the top level of a file (that is LAYGO access)
- ^DIE calls—Deleting an entry at the top level of a file (that is DELETE access).

Developers can bypass these LAYGO and DELETE access checks using the following variables, respectively:

- DLAYGO
- DIDEL

When accessing data through software options, File Access Security is also checked when a file is navigated to from another file (that is READ, WRITE, DELETE, and LAYGO access). Currently, there is no way for developers to override access checks when navigating to a file from another file, so explicit access to files navigated to/from an application option *must* be granted by the system administrators.

### What in VA FileMan is Still Protected by the File Manager Access Code?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the File Access Security system is enabled, access to templates (such as INPUT, PRINT, SORT, and so on) is denied when using VA FileMan options, if the user’s DUZ(0) string does *not* contain a matching character. Similarly, when editing fields using VA FileMan’s Enter or Edit File Entries \[DIEDIT\] option, the DUZ(0) matching process is invoked to permit or deny editing for protected fields. The DUZ(0) value is also checked by some *non*-VA FileMan applications. Finally, if a user’s DUZ(0) is @, they are allowed complete access to all files.

### Purpose for Granting File Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System administrators are responsible for granting file access. They *must* determine each user’s needs and assign an appropriate degree of access authority. Too much access may risk the security of your system, while too little may inhibit productive activity.

What is the purpose of File Access Security? Why bother specifying who has access to which files? The answer is threefold:

- To monitor the use of VA FileMan.
- To regulate the extent of VA FileMan access from among six levels of security that allow AUDIT, DATA DICTIONARY (“DD”), DELETE (“DEL”), LAYGO, READ (“RD”), or WRITE (“WR”) access.

![](kernel-8-0-systems-management-signon-security-user-guide/070.png) REF: These File Access Security level properties are described in <u>Table 7</u>.

- To reserve DUZ(0), the FILE MANAGER ACCESS CODE (#3) field, as a security measure to protect just templates and fields, *not* files, from VA FileMan options.

With file access security, it is possible to know who has access to which files and what kind of access they have. This information can also be retrieved by user or by file. In addition, privileges can also be entirely restricted for an individual user or for a single file that may contain sensitive information.

### Who Needs File Access?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to grant File Access Security in the following cases:

- A user needs to access files directly through VA FileMan options.
- Within an application option, VA FileMan is used to navigate from one file to another.
- Within an application option that calls the ^DIE API to edit a file entry; a user is unable to add or delete entries in a pointed-to file.
- Within an application option that calls the ^DIE or ^DIC APIs to edit a file entry; a user is unable to add or delete entries in the primary file (because the application did *not* set the DLAYGO or DIDEL variables).
- A user needs to use VA FileMan’s Line Editor’s Transfer Lines from Another Document option.

Application developers can document which files need to be granted to whom, or they can modify their code or data dictionary (DD) specifications to allow access.

### Levels of File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are six file access security properties involved with File Access Security. If a file access security property is *not* defined (that is the value is NULL), the VA FileMan exported menu options for that property are *not* open to full access for users.

![](kernel-8-0-systems-management-signon-security-user-guide/071.png) REF: <u>Table 7</u> is taken from the *VA FileMan (Version 22.2) and Kernel (Version 8.0) File Access Security* supplemental documentation located on the VA Software Document Library (VDL) at: [VDL VA FileMan Application Documents](http://www.va.gov/vdl/application.asp?appid=5)

<table>
<caption><p><span id="_Ref29373566" class="anchor"></span>Table 8: DUZ Array Variables</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Access</th>
<th>Security Property Description</th>
<th>Property Location (Classic VA FileMan)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AUDIT</strong></td>
<td><p>The <strong>AUDIT</strong> security property controls the setting of auditing characteristics and the deletion of audit trails. This property only deals with the auditing of data and <em>not</em> the auditing of data dictionary (DD) changes. To audit DD changes, users would enter <strong>YES</strong> at the “DD AUDIT? NO//” prompt when modifying a file’s File Security Access. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Fields Being Audited</strong> [DIAUDITED FIELDS]</p></li>
<li><p><strong>Data Dictionaries Being Audited</strong> [DIAUDIT DD]</p></li>
<li><p><strong>Purge Data Audits</strong> [DIAUDIT PURGE DATA]</p></li>
<li><p><strong>Purge DD Audits</strong> [DIAUDIT PURGE DD]</p></li>
<li><p><strong>Turn Data Audit On/Off</strong> [DIAUDIT TURN ON/OFF]</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”AUDIT”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>DATA DICTIONARY (“DD”)</strong></td>
<td><p>The <strong>DATA DICTIONARY</strong> security property controls who has access to modify the data dictionary. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Modify File Attributes</strong> [DIMODIFY]</p></li>
<li><p><strong>Utility Functions</strong> [DIUTILITY]</p></li>
<li><p><strong>Data Dictionary Utilities</strong> [DI DDU]<br />
<br />
For example, to use the <strong>Map Pointer Relations</strong> [DI DDMAP] option, <strong>DD</strong> access is needed to the PACKAGE (#9.4) file and to the files one selects for mapping.</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”DD”)=&lt;value&gt;</strong></td>
</tr>
<tr class="odd">
<td><strong>DELETE (“DEL”)</strong></td>
<td><p>The <strong>DELETE</strong> security property controls who can delete an existing record that is contained within the file. It does <em>not</em> permit deletion of the file or any of its attribute fields. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Enter or Edit File Entries</strong> [DIEDIT]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”DEL”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>LAYGO</strong></td>
<td><p>The <strong>LAYGO</strong> (Learn As You Go) security property controls who can add a new record to the file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Enter or Edit File Entries</strong> [DIEDIT]</p></li>
</ul>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/072.png) <strong>NOTE:</strong> You <em>must</em> have <strong>LAYGO</strong> and <strong>WRITE</strong> access to a file to add new entries. In addition, you <em>must</em> have <strong>WRITE</strong> access at the field level for all required identifier fields.</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”LAYGO”)=&lt;value&gt;</strong></td>
</tr>
<tr class="odd">
<td><strong>READ (“RD”)</strong></td>
<td><p>The <strong>READ</strong> security property controls who has access to read data contained within a file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Print File Entries</strong> [DIPRINT]</p></li>
<li><p><strong>Search File Entries</strong> [DISEARCH]</p></li>
<li><p><strong>Inquire to File Entries</strong> [DIINQUIRE]</p></li>
<li><p><strong>Statistics</strong> [DISTATISTICS]</p></li>
<li><p><strong>List File Attributes</strong> [DILIST]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]<br />
<br />
To transfer text, the user needs <strong>READ</strong> access to the file from which text is being transferred. Similarly, <strong>WRITE</strong> access is needed for the file to which entries are being transferred with this option.</p></li>
</ul>
<p>![](kernel-8-0-systems-management-signon-security-user-guide/073.png) <strong>NOTE:</strong> <strong>READ</strong> access is also required to use some of the Filegram and Audit options.</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”RD”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>WRITE (“WR”)</strong></td>
<td><p>The <strong>WRITE</strong> security property controls who can alter data in an existing record that is contained within the file. It does <em>not</em> permit the adding of new entries to the file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Enter or Edit File Entries</strong> [DIEDIT]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]<br />
<br />
To transfer text, the user needs <strong>READ</strong> access to the file from which text is being transferred. Similarly, <strong>WRITE</strong> access is needed for the file to which entries are being transferred with this option.</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”WR”)=&lt;value&gt;</strong></td>
</tr>
</tbody>
</table>

<span id="_Ref29373566" class="anchor"></span>Table 8: DUZ Array Variables

Any or all six levels of access can be enabled for each of the user’s accessible files. This is done by changing the field value from NULL to YES. This flag is overridden for developers whose DUZ(0)=@.

Granting the READ, WRITE, DELETE, and LAYGO levels of access permits adding and deleting file entries as well as editing their attribute field data values. This is true unless the attribute field has been protected. If so (that is if there is READ, WRITE, or DELETE protection within the data dictionary \[DD\] for a given field), the user’s FILE MANAGER ACCESS CODE (#3) field, DUZ(0), is checked. Access is denied if the user’s DUZ(0) does *not* contain a character matching the field protection. Again, DUZ(0)=@ overrides this restriction.

The DATA DICTIONARY (“DD”) and AUDIT levels of access pertain to the structure of the file itself. While this provides a generous scope for VA FileMan data dictionary (DD) modification, it falls short of, for example, deleting a field protected with the at-sign (@; Programmer access).

The same applies to templates. If the template is protected, the user who has access to the file does *not* have access to the template from VA FileMan options unless there is a match in the DUZ(0) character string.

### Audit Access to Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Audit privileges might be granted to advanced VA FileMan users who are interested in developing new audit capabilities. With AUDIT access, which *must* be accompanied by DD access, VA FileMan’s Modify File Attributes \[DIMODIFY\] option can be used to set an audit flag for a particular field within a file. This access does *not* include setting audit conditions with M code, which is reserved for users with a FILE MANAGER ACCESS CODE (#3) field containing @.

The data values for attribute fields can be recorded in the AUDIT (#1.1) file by setting an audit flag in the data dictionary (DD) for that field. For example, the SSN field in the PATIENT (#2) file could be audited. There are two choices for the audit in the AUDIT (#1.1) file:

- An entry can be made when a value is entered or changed.
- An entry can be made *only* when the value is changed (that is edited or deleted).

The second method may be all that’s needed. In the SSN example, you would monitor just the circumstances of the change, *not* of the initial SSN assignment.

To display the results of the audit, your DUZ(0) *must* equal the at-sign (@; Programmer access). Then, you can query the AUDIT (#1.1) file in the usual way with VA FileMan’s Inquire to File Entries \[DIINQUIRE\] option.

### How to Grant File Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System administrators specify the files and levels of access for users. The File Access Security \[XUFILEACCESS\] menu, on the User Management \[XUSER\] menu, provides options to grant file access security. These options edit the ACCESSIBLE FILE (#32) Multiple field in the NEW PERSON (#200) file.

The options for granting file access privileges fall into three functional categories:

- EDITING—To assign file access to an individual user or a group of users. One user’s profile can also be duplicated or copied to another user or group of users. To simplify adding files, number ranges can be specified.
- LISTING—To display one user’s profile, a name-sorted list of all user’s profiles, or a file or range of files with associated users and the access levels of each.
- RESTRICTING—To entirely limit access by user or by file, or to delete a range of files for a user or group of users.

The options are designed to facilitate queries by user or by file. You can add or delete file access for one user or for many users. You can begin with the file and list users with access or restrict access.

### Using the File Access Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Access Security \[XUFILEACCESS\] menu options are shown in <u>Figure 42</u>.

<span id="_Ref86542134" class="anchor"></span>Figure 42: File Access Security Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

User Management ... \[XUSER\]

File Access Security ... \[XUFILEACCESS\]

Grant Users' Access to a Set of Files \[XUFILEGRANT\]

Copy One User's File Access to Others \[XUFILECOPY\]

Single file add/delete for a user \[XUFILESINGLEADD\]

Inquiry to a User's File Access \[XUFILEINQUIRY\]

List Access to Files by File number \[XUFILELIST\]

Print Users Files \[XUFILEPRINT\]

Delete Users' Access to a Set of Files \[XUFILESETDELETE\]

Remove All Access from a Single User \[XUFILEREMOVEALL\]

Take away All access to a File \[XUFILEDELETE\]

Assign/Delete a File Range \[XUFILERANGEASSIGN\]

When using options on the File Access Security \[XUFILEACCESS\] menu, you may have the following questions:

- What is the DUZ# that appears next to the user’s name?
- How is a range of file numbers specified?
- What are the queuing questions all about?

#### Understanding DUZ (User Number)

When listing the file accesses by user or by file, the user’s name is followed by a number in parentheses. The heading indicates that this is the “User \#,” which is the same as the DUZ#.

Once the user enters an Access and Verify Code, Kernel’s Signon/Security uses the DUZ variable to identify an entry in the NEW PERSON (#200) file. It *must* be a unique identifier, so the user’s name does *not* work. Instead, the Internal Entry Number (IEN) is used. That is what becomes the value of DUZ.

![](kernel-8-0-systems-management-signon-security-user-guide/074.png) NOTE: Some users have low numbers while others have high ones. This simply indicates the order their names were entered into the NEW PERSON (#200) file. Users with low numbers are often people who began using the system some years ago, while users with high numbers tend to be recent entries in the file.

DUZ is a local variable array that identifies the user who has signed onto the system. It is the Internal Entry Number (IEN) for the user in the NEW PERSON (#200) file. Besides the unique IEN, the DUZ array contains other variables specific to the signed-on user, which are listed in <u>Table 8</u>:

<table>
<caption>DUZ Array VariablesDUZ Array Variables</caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DUZ(0)</strong></td>
<td>This variable stores the level of <strong>Programmer</strong> access (that is VA FileMan Access Code) of the user at signon (such as <strong>@</strong>). This variable is derived from the value stored in the FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td><strong>DUZ(1)</strong></td>
<td>This variable is obsolete; it is always set to <strong>NULL</strong>.</td>
</tr>
<tr class="odd">
<td><strong>DUZ(2)</strong></td>
<td>If a user is associated with more than one institution (division), the user is prompted at signon to select a division. This variable is set to the appropriate value. This variable is derived from the values stored in the DIVISION (#16) Multiple field in the NEW PERSON (#200) file. This field points to the INSTITUTION (#4) file.</td>
</tr>
<tr class="even">
<td><strong>DUZ(“AG”)</strong></td>
<td>This variable stores the agency code at signon (such as <strong>V</strong> <strong>=</strong> <strong>VA</strong>). This variable is derived from the value stored in the AGENCY CODE (#9) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. This value is a defined Set of Codes.</td>
</tr>
<tr class="odd">
<td><strong>DUZ(“AUTHENTICATION”)</strong></td>
<td>This variable stores the method used to authenticate the user. Examples include “<strong>ASHTOKEN</strong>”, “<strong>AVCODES</strong>”, “<strong>BSETOKEN</strong>”, “<strong>CCOWTOKEN</strong>”, “<strong>SSOI</strong>”, “<strong>SSOE</strong>”, “<strong>NHIN</strong>”, “<strong>NONE</strong>”, and “<strong>XUP</strong>”.</td>
</tr>
<tr class="even">
<td><strong>DUZ(“AUTO”)</strong></td>
<td>Menu Manager uses this variable to control whether all items on a menu are presented automatically after each cycle through the menu system. This variable stores the user’s menu display preference at signon (such as <strong>1</strong> = Auto Generate Menus). This variable is derived from the value stored in the AUTO MENU (#.06) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="odd">
<td><strong>DUZ(“BUF”)</strong></td>
<td>This variable stores the user’s type ahead (buffer) preference (such as <strong>1</strong> = Allowed). This variable is derived from the value stored in the TYPE-AHEAD (#.09) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td><strong>DUZ(“LANG”)</strong></td>
<td><p>This variable stores the display language as it is stored in the LANGUAGE (#.01) field in the LANGUAGE (#.85) file. VA FileMan uses this setting to enable the display of language-specific dates and times, numeric formats, and dialogs. VA FileMan currently distributes only the English language entry for this file (entry number <strong>1</strong>).</p>
<p>The LANGUAGE (#.01) field in the LANGUAGE (#.85) file is pointed to by the following:</p>
<ul>
<li><p>LANGUAGE (#.01) field of the TRANSLATION (#.847) subfield of the DIALOG (#.84) file.</p></li>
<li><p>LANGUAGE (#200.07) field in the NEW PERSON (#200) file.</p></li>
<li><p>DEFAULT LANGUAGE (#207) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file, which overrides the setting of the LANGUAGE (#200.07) field.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>DUZ(“LOA”)</strong></td>
<td><p>This variable records the “Level of Assurance” (LOA) of the user’s authentication and identity. Four levels are currently defined by National Institution of Standards and Technology Special Publication (NIST SP) 800-63-2 Electronic Authentication Guideline:</p>
<ul>
<li><p><strong>Level 1—</strong>No identity proofing requirement. This generally refers to a “self-asserted” user identity and is the lowest form of authentication. This form of authentication does <em>not</em> satisfy VA HANDBOOK 6500 security requirements. Application developers may choose to programmatically deny access to sensitive data if a user’s LOA equals “<strong>1</strong>”.</p></li>
<li><p><strong>Level 2—</strong>Single factor authentication. This form of authentication includes username/password or, in the case of VistA, Access/Verify Code authentication.</p></li>
<li><p><strong>Level 3—</strong>Multi-factor authentication. This form of authentication includes VA 2-Factor Authentication (2FA) using smart cards (PKI certificates) and Personal Identification Number (PIN).</p></li>
<li><p><strong>Level 4—</strong>The highest practical authentication assurance. At this level, in-person identity proofing such as fingerprint or retinal scan is used to authenticate and identify the user.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>DUZ(“REMAPP”)</strong></td>
<td>This variable is used to identify an external client application whenever possible. Examples include “<strong>BMS</strong>”, “<strong>CAPRI</strong>”, “<strong>MDWS</strong>”, “<strong>NUMI</strong>”, “<strong>VISTA IMAGING</strong>”, and others. The information is currently obtained from the REMOTE APPLICATION (#8994.5) file, but plans are to obtain client application identity from the 2-Factor Authentication (2FA) token when fully implemented.</td>
</tr>
<tr class="odd">
<td><strong>DUZ(“TEST”)</strong></td>
<td><p>This variable is used during menu generation. It indicates to the user when they are in a Test account by inserting the phrase “ &lt;TEST ACCOUNT&gt;” into the “Select…” main menu prompt. For example (see <u>Figure 44</u>):</p>
<p>Select <em>VA FileMan</em> <mark>&lt;TEST ACCOUNT&gt;</mark> Option:</p></td>
</tr>
</tbody>
</table>

DUZ Array VariablesDUZ Array Variables

<span id="_Toc207519127" class="anchor"></span>Figure 43: Displaying the DUZ Array for a Signed-on User at a Programmer Prompt

KRN\><span class="mark">ZW DUZ \<Enter\></span>

<span class="mark">DUZ=8</span>

DUZ(0)="@"

DUZ(1)=""

DUZ(2)=2

DUZ("AG")="V"

DUZ("AUTO")=1

DUZ("BUF")=1

DUZ("LANG")=1

DUZ("TEST")=" \<TEST ACCOUNT\>"

When you want to display/print the DUZ, VA FileMan recognizes that when you enter “NUMBER” as a print field that you want to display/print the DUZ for the user entry from the NEW PERSON (#200) file.

<span id="_Ref352760552" class="anchor"></span>Figure 44: Displaying the DUZ (Internal Entry Number) in a VA FileMan Report

Select VA FileMan <span class="mark">\<TEST ACCOUNT\></span> Option: <span class="mark">PRINT \<Enter\></span> File Entries

OUTPUT FROM WHAT FILE: <span class="mark">NEW PERSON</span>// <span class="mark">\<Enter\></span>

SORT BY: NAME// <span class="mark">\<Enter\></span>

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">NUMBER \<Enter\></span>

THEN PRINT FIELD: <span class="mark">NAME \<Enter\></span>

1 NAME

2 NAME COMPONENTS

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> NAME

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): NEW PERSON LIST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Network

NEW PERSON LIST APR 3,2013 09:55 PAGE 1

<span class="mark">NUMBER</span> NAME

--------------------------------------------------------------------------------

<span class="mark">1000228</span> XUUSER,EIGHT

<span class="mark">1000084</span> XUUSER,ELEVEN

<span class="mark">52</span> XUUSER,FIFTEEN

<span class="mark">74</span> XUUSER,FIVE

<span class="mark">73</span> XUUSER,FOUR

<span class="mark">21</span> XUUSER,FOURTEEN

<span class="mark">150</span> XUUSER,NINE

<span class="mark">1000182</span> XUUSER,ONE

<span class="mark">1000166</span> XUUSER,SEVEN

<span class="mark">1000108</span> XUUSER,SIX

<span class="mark">1000039</span> XUUSER,SIXTEEN

<span class="mark">151</span> XUUSER,TEN

<span class="mark">8</span> XUUSER,THIRTEEN

<span class="mark">164</span> XUUSER,THREE

<span class="mark">71</span> XUUSER,TWELVE

<span class="mark">183</span> XUUSER,TWO

#### Using Ranges of File Numbers

Can files be specified by number ranges? Yes, it is useful to do this when granting several files at once. First, find out the number of the files. Typing a question mark (?) at the “to Files:” prompt displays the number and name of the files. Note the numbers and then put them together on one line. You can use hyphens to indicate a consecutive range and commas to separate the single numbers and hyphenated groups as follows:

2,3,4,6,7,8,125,236,799

OR

2-4,6-8,125,236,799

File numbers are also used when printing a group of consecutive files. The prompt asks for a place to start with a default file name presented. To print just this one file, respond to the next prompt by simply pressing the \<Enter\> key, thereby accepting the default of ending after printing that one file.

To print a consecutive range of files, the lowest number is entered as the starting point and the highest number as the ending point. All files that fall in this range are printed.

#### Queuing File Access Specifications

Most of the options provide the opportunity to queue, after specifying who is to be granted which files. Queuing sends the specifications to TaskMan to assign to users later. TaskMan can work at an off-peak time (such as midnight) to avoid consuming system resources during the daytime. If the system is *not* busy, queuing is still a good idea since your terminal is otherwise tied up while the report is being printed.

## Running the File Access Security Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Advantages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To implement File Access Security, you need to run a conversion. Some advantages of implementing File Access Security include:

- Easier to identify levels of access—Running the conversion makes it possible to identify the levels of access each individual user has to each file.
- Enhanced system performance—Checking file access by user is slightly faster in terms of global accesses and CPU time.

### Advance Preparation for the Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Access Security conversion is designed to allocate access privileges to all users according to their current FILE MANAGER ACCESS CODE (#3) field value in the NEW PERSON (#200) file, DUZ(0), combined with information about their file access through options stored in the ^DISV global. After the conversion you should get only a few user requests for file access. The File Access Security \[XUFILEACCESS\] menu, an option on the User Management \[XUSER\] menu, should then be used to add a file to a user’s ACCESSIBLE FILE (#32) Multiple field in the NEW PERSON (#200) file.

The conversion uses the FILE MANAGER ACCESS CODE (#3) field \[DUZ(0) string\] to assign file access according to the characters in the string. If a file is protected with a particular character that matches one in the user’s code, that file is entered into the user’s ACCESSIBLE FILE (#32) Multiple field. Levels of access are granted according to the file’s original security (field-level security continues to function the same, by checking the FILE MANAGER ACCESS CODE (#3) field).

![](kernel-8-0-systems-management-signon-security-user-guide/075.png) NOTE: Users with Programmer-level access (FILE MANAGER ACCESS CODE \[#3\] field = @) does *not* need to have any files in their ACCESSIBLE FILE (#32) Multiple field, since they are able to access *all* files *without* restriction.

#### ^DISV Global

The File Access Security conversion process makes use of the ^DISV global to identify which files have recently been accessed by which users. The conversion adds all files that the user has been able to access (select from) to the user’s ACCESSIBLE FILE (#32) Multiple field list. It grants READ access to these files.

Using the ^DISV global to grant file access has the benefit of permitting option usage “as usual” the day after the conversion is run. KILLing the ^DISV global just *before* the conversion is *not* advised, since many users suffer inappropriate access restrictions and need special attention by system administrators just after the conversion. KILLing the ^DISV global a week or two before the conversion, however, may be worthwhile as a way of purging obsolete user data. In multi-CPU environments, where each CPU has its own copy of the ^DISV global, you should choose the busiest user node upon which to run the conversion (to pick up the most comprehensive information from that node’s ^DISV). Caché sites should run the conversion from their busiest user node.

It is assumed that ^DISV is *not* translated, so K ^DISV on the CPU where the conversion is run. Do this about two weeks before you perform the conversion, as advance preparation. ^DISV is reset as soon as a user responds to a “Select:” prompt.

<span id="_Toc193181650" class="anchor"></span>Figure 45: KILLing ^DISV—Sample Code

\><span class="mark">K ^DISV \<Enter\></span>

#### Adding Explicit File Access for System Administrators

If there are any files that are neither protected nor accessed by users (such as the DOMAIN \[#4.2\] file) the conversion does *not* list them in any user’s ACCESSIBLE FILE (#32) Multiple field. Before the conversion, these types of files are accessible to everyone, while after the conversion these files are only accessible to users with Programmer-level access. Therefore, before the conversion, assign a unique symbol/character to otherwise unprotected files. This ensures that at least those users with that unique symbol (such as system administrators) are granted access. VA FileMan’s Edit File \[DIEDFILE\] option can be used to edit the codes.

![](kernel-8-0-systems-management-signon-security-user-guide/076.png) NOTE: In previous documentation and data dictionaries, it has been *implied* that the pound sign (“\#”) symbol/character was reserved for File Access Security for system administrators; however, this is *not* true. It has merely been used as a convention*.*

<span id="_Toc193181651" class="anchor"></span>Figure 46: Updating File Access Settings (*Before* Conversion)

Select OPTION: <span class="mark">UTILITY FUNCTIONS \<Enter\></span>

Select UTILITY OPTION: <span class="mark">EDIT FILE \<Enter\></span>

MODIFY WHAT FILE: USER// <span class="mark">DOMAIN \<Enter\></span> (227 entries)

Do you want to use the screen-mode version? YES// <span class="mark">N \<Enter\></span> NO

NAME: DOMAIN// <span class="mark">\<Enter\></span>

DESCRIPTION:

No existing text

Edit? NO// <span class="mark">\<Enter\></span>

Select APPLICATION GROUP: <span class="mark">\<Enter\></span>

DEVELOPER: <span class="mark">\<Enter\></span>

<span class="mark">DATA DICTIONARY ACCESS</span>: <span class="mark">\<Enter\></span>

<span class="mark">READ ACCESS</span>: <span class="mark">\<Enter\></span>

<span class="mark">WRITE ACCESS</span>: <span class="mark">\<Enter\></span>

<span class="mark">DELETE ACCESS</span>: <span class="mark">\<Enter\></span>

<span class="mark">LAYGO ACCESS</span>: <span class="mark">\<Enter\></span>

<span class="mark">AUDIT ACCESS</span>: <span class="mark">\<Enter\></span>

### Summary of the File Access Security Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Access Security conversion prepares the NEW PERSON (#200) file for VA FileMan’s method of file access (lookup into a user’s record for file access). VA FileMan’s ability to protect data within files on fields and templates remains the same. The summary steps that occur when the conversion is run are outlined below:

1.  Setup structure. The structure for implementing the file access method is set up through the following:
1.  Place the data dictionary (DD) for the ACCESSIBLE FILE (#32) Multiple field in the NEW PERSON (#200) file. This multiple is permanently put in place by running the File Access Security conversion.
2.  Install menu options, help frames, and templates used for maintaining the user file access method (that is entries with the XUFI namespace).
6.  Add protected files to the ACCESSIBLE FILE (#32) Multiple field. Each user’s FILE MANAGER ACCESS CODE (#3) field is used to add entries to the ACCESSIBLE FILE (#32) Multiple field as follows:
1.  Create a list of files to be processed by examining each file’s protection codes. Files that meet *both* of the following requirements are temporarily stored in the ^UTILITY(\$J global:
- Files that have protection defined.
- Files with protection *not* equal to @.

![](kernel-8-0-systems-management-signon-security-user-guide/077.png) NOTE: Files that lack any protection are bypassed. Such unprotected files are *not* later listed in anyone’s ACCESSIBLE FILE (#32) Multiple field. Protection should therefore be applied *before* running the conversion so that at least some users (such as system administrators) are granted access.

3.  Examine each user in the NEW PERSON (#200) file. Each user meeting *all* of the following requirements is selected for further processing:
- Users are *not* terminated.
- Users with an Access Code.
- Users with a VA FileMan Access Code (that is FILE MANAGER ACCESS CODE \[#3\] field in the NEW PERSON \[#200\] file).
- Users with a FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON \[#200\] file *not* equal to @.

The user’s FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON \[#200\] file is parsed. Each symbol/character is compared with the list of files in the ^UTILITY(\$J global. All files that have a protection code matching this symbol/character are added to the user’s ACCESSIBLE FILE (#32) Multiple field in the NEW PERSON \[#200\] file. If the symbol/character is used as the file’s DATA DICTIONARY (“DD”) file security, the user is granted DD access; if it is used as LAYGO, the user is granted LAYGO access, and so on.

7.  Add files accessed by the user to the ACCESSIBLE FILE (#32) Multiple field. Files accessed by the user through options since the last time the ^DISV global was KILLed are added to the user’s ACCESSIBLE FILE (#32) Multiple field by the processing of the ^DISV global. Entries in ^DISV that meet *both* of the following requirements are added to the ACCESSIBLE FILE (#32) Multiple field, with READ access:
- The file *mustnot* be in VA FileMan’s file number range (that is file number *must* be equal to or greater than 1.1.
- The user does *not* already have access to this file.

### File Access Security Conversion Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps that occur when the file access security conversion is run are described below:

1.  Identify unprotected files and assign protection codes as desired (as described in the “[Advance Preparation for the Conversion](#advance-preparation-for-the-conversion)” section). For example, the DOMAIN (#4.2) file may need to be protected so that it is granted to users having a FILE MANAGER ACCESS CODE (#3) field containing the assigned symbol/character.

![](kernel-8-0-systems-management-signon-security-user-guide/078.png) NOTE: In previous documentation and data dictionaries, it has been *implied* that the pound sign (“\#”) symbol/character was reserved for File Access Security for system administrators; however, this is *not* true. It has merely been used as a *convention.*

8.  Review the FILE MANAGER ACCESS CODE fields (#3) of VA FileMan users. The codes should contain symbols/characters matching those used to protect the files that these individuals use. Since the conversion automatically grants files to users according to previous privileges as indicated by the FILE MANAGER ACCESS CODE (#3) field, add any additional symbols/characters to their FILE MANAGER ACCESS CODE fields (#3) to take advantage of the conversion’s automated file assignment according to levels of access.
9.  Be ready to use the File Access Security \[XUFILEACCESS\] menu, [Figure 43](#_Ref86542134), to review and grant file access privileges *after* the conversion.
10. In the Production account, enable File Access Security system features and options with ENABLE^XUFILE3, as illustrated in <u>Figure 47</u>:

> <span id="_Ref29371435" class="anchor"></span>Figure 47: Enabling File Access Security—Sample User Dialog

In VAH:

\><span class="mark">D ENABLE^XUFILE3 \<Enter\></span>

\>

11. In the Production account, begin the conversion with ^XUINCON:

> <span id="_Toc193181653" class="anchor"></span>Figure 48: ^XUINCON Conversion Routine—Sample User Dialog

In VAH:

\><span class="mark">D ^XUINCON \<Enter\></span>

Version 7 of the Kernel defined a new multiple-valued field

in the New Person File called Accessible File. This conversion

will store file access in this multiple in the following manner:

Those Users who have a FileMan Access Code (DUZ(0)) which

is not null, i.e., contains some character string,

will have their access string matched to the protection

currently on your files. For each match between the file

and the user, the file will be listed in the user's

Accessible File multiple as will the type of access

(dictionary, delete, laygo, read, write, audit).

> **NOTE:** Files with no protection will NOT be assigned to any user.

Would you like to run the conversion now? NO//

12. If you are ready to run the conversion, answer YES:

> <span id="_Toc193181654" class="anchor"></span>Figure 49: Running a Conversion—Sample User Dialog

Would you like to run the conversion now? NO// <span class="mark">YES \<Enter\></span>

56237,36565

Build Table.

Convert Users.

Give access from DISV file.

X-ref.

Done56237,36565.

\>

13. Review the newly assigned access settings. Use the File Access Security \[XUFILEACCESS\] menu, [Figure 43](#_Ref86542134), located on the User Management \[XUSER\] menu, to display file access by user and by file.

### After the File Access Security Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the file access security conversion, users may complain about *not* being able to add entries to files as they previously could. This typically results from use of an option that navigates from one file to another. To be able to add entries to the navigated-to file, the user needs LAYGO access to that file. System administrators can solve the problem by granting LAYGO access using the File Access Security \[XUFILEACCESS\] menu options, [Figure 43](#_Ref86542134).

If this form of security is implemented, system administrators should find that it provides a more accurate and precise knowledge of who has what level of access to which files. When the conversion is run, privileges are granted to existing users by making use of information stored in the VA FileMan record of file manipulation activity, the ^DISV global. The file access conversion grants each user READ access to files that the user had recently accessed as indicated in the ^DISV global. System administrators can grant file access privileges to new users by copying the profile of an existing user with similar duties (such as a laboratory application coordinator or admissions clerk).

To be sure that appropriate levels of access have been allocated, system administrators should determine who has what level of access to which files. Access to sensitive files (such as the NEW PERSON \[#200\] file) should be reviewed and readjusted for individual users as appropriate. All files on a system should be reviewed before and after running the File Access Security conversion.

<u>Figure 50</u> shows how to create a PRINT template to display a report on the current file access security:

<span id="_Ref86743760" class="anchor"></span>Figure 50: Creating a PRINT Template to Display File Access Security—Sample User Dialog

Select OPTION: <span class="mark">PRINT FILE ENTRIES \<Enter\></span>

OUTPUT FROM WHAT FILE: <span class="mark">FILE \<Enter\></span>

SORT BY: NAME// <span class="mark">@NUMBER \<Enter\></span>

START WITH NUMBER: FIRST// <span class="mark">3 \<Enter\></span>

GO TO NUMBER: LAST// <span class="mark">4 \<Enter\></span>

WITHIN NUMBER, SORT BY: <span class="mark">\<Enter\></span>

FIRST PRINT ATTRIBUTE: <span class="mark">NUMBER;L8;S;"" \<Enter\></span>

FIRST PRINT ATTRIBUTE: <span class="mark">NAME;L25;"" \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">DD ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">RD ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">WR ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">DEL ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">LAYGO ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">AUDIT ACCESS;R6 \<Enter\></span>

THEN PRINT ATTRIBUTE: <span class="mark">\<Enter\></span>

HEADING: FILE LIST// <span class="mark">FILE SECURITY \<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">ZZFILE SECURITY \<Enter\></span>

Once the conversion has been run, you can use the File Access Security \[XUFILEACCESS\] menu, [Figure 43](#_Ref86542134), to print the accessible files for individual users. Thus, you can establish profiles that would be typical of groups of users (such as Nursing, Pharmacy, or other services). Then, when establishing an account for a new user or reactivating the access of a previously terminated user, the profile is available for copying to the new user.

# Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Electronic Signatures User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An electronic signature (esig) is a security tool that software applications can use as an additional identification check. For example, software can require an electronic signature be applied to a particular form or document before subsequent processing can continue.

Electronic signature codes are stored in the NEW PERSON (#200) file.

### Electronic Signature code Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to create an electronic signature for yourself, you can choose the Electronic Signature code Edit \[XUSESIG\] option, available from the User’s Toolbox \[XUSERTOOLS\] menu.

You can enter a new electronic signature code or change the existing code. The length of the code *must* be between 6 and 20 uppercase characters. Requiring all uppercase allows the code to be verified with either uppercase or lowercase input, since lowercase is converted to uppercase in the matching process. You should choose a code that other users are *not* likely to guess, as this code verifies that it is you who are signing off on some important action.

The Electronic Signature code Edit \[XUSESIG\] option also allows you to edit the following fields in the NEW PERSON (#200) file:

- INITIAL (#1)
- SIGNATURE BLOCK PRINTED NAME (#20.2)
- SIGNATURE BLOCK TITLE (#20.3)
- OFFICE PHONE (#.132)
- VOICE PAGER (#.137)
- DIGITAL PAGER (#.138)

Applications can print some or all fields when printing an electronically signed document. You should therefore ensure that the values entered in these fields are accurate.

#### Electronic Signature Code Edit Restrictions

As of Patch XU\*8.0\*679, the system restricts entries in the following fields in the NEW PERSON (#200 file when accessed through the Electronic Signature code Edit \[XUSESIG\] option:

- SIGNATURE BLOCK PRINTED NAME (#20.2)
- SIGNATURE BLOCK TITLE (#20.3)

As noted in Section [5.1.1](#electronic-signature-code-edit-option), you can use the Electronic Signature code Edit \[XUSESIG\] option to enter and maintain electronic signature information for yourself. However, if the patch restrictions are activated, then access to the SIGNATURE BLOCK PRINTED NAME (#20.2 and SIGNATURE BLOCK TITLE (#20.3 fields will be enabled only for users who have the XUSIG security key assigned.

To enable restrictions, authorized site personnel *must* set the XU SIG BLOCK DISABLE general parameter to a value of ON (1). The parameter definition is stored in the PARAMETER DEFINITION (#8989.51) file, and the parameter data is stored in the PARAMETERS (#8989.5) file:

- If the XU SIG BLOCK DISABLE parameter is set to ON and the user has the XUSIG security key assigned in the NEW PERSON (#200) file, then access to the restricted fields is allowed.
- If the XU SIG BLOCK DISABLE parameter is set to ON, but the user does *not* have the XUSIG security key assigned, then access to the restricted fields is *not* allowed.
- If the site leaves the XU SIG BLOCK DISABLE parameter set to OFF (0), then access to all electronic signature fields is allowed.

To set the XU SIG BLOCK DISABLE parameter to ON, do the following:

1.  Log into VistA with Programmer access.
14. At the “Select OPTION NAME:” prompt, enter XPAR MENU TOOLS.
15. At the “Select General Parameter Tools Option:” prompt, enter EP.
16. At the “Select PARAMETER DEFINITION NAME:” prompt, enter XU SIG BLOCK DISABLE.
17. At the “Sig Block Disable:” prompt, enter YES.

## Electronic Signature System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181645" class="anchor"></span>Figure 51: User Edit Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

User Edit ... \[XUSER\]

Electronic Signature Block Edit \[XUSESIG BLOCK\]

Clear Electronic signature code \<locked: XUMGR\> \[XUSESIG CLEAR\]

### Electronic Signature Block Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Signature Block Edit \[XUSESIG BLOCK\] option lets you edit the electronic signature code for any user on the system. When you create an electronic signature code for a user, the SIGNATURE BLOCK PRINTED NAME field in the NEW PERSON (#200) file is initially filled in by a cross-reference on the NAME (#.01) field (and is overwritten if the NAME \[#.01\] field is changed). Credentials (such as “M.D.”) can be added to customize the printed name. As a security feature, an input transform requires that the user’s last name (first comma piece of the NAME (#.01) field) be included in the printed name. (This field *cannot* be edited through VA FileMan, since it is WRITE-protected with a caret \[^\].)

#### Electronic Signature Block Edit Restrictions

As of Patch XU\*8.0\*679, the system restricts entries in the following fields in the NEW PERSON (#200) file when accessed through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option:

- SIGNATURE BLOCK PRINTED NAME (#20.2)
- DEGREE (#10.6)

As noted in Section [5.2.1](#electronic-signature-block-edit-option), you can use the Electronic Signature Block Edit \[XUSESIG BLOCK\] option to enter and maintain electronic signature information for other users. However, if the patch restrictions are activated, access to the SIGNATURE BLOCK PRINTED NAME (#20.2) and DEGREE (#10.6) fields will be enabled only for users who have the XUSIG security key assigned. To enable supervisors who hold the XUSIG security key to change the SIGNATURE BLOCK TITLE (#20.3) field for other users when patch restrictions are in force, Patch XU\*8.0\*679 added access to that field through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option.

![](kernel-8-0-systems-management-signon-security-user-guide/079.png) REF: For instructions on activating restrictions, see Section [5.1.1.1](#electronic-signature-code-edit-restrictions), “[Electronic Signature Code Edit Restrictions](#electronic-signature-code-edit-restrictions).”

To maintain valid educational credentials, DEGREE (#10.6) field entries made through the Electronic Signature Block Edit \[XUSESIG BLOCK\] option are restricted to valid degrees stored in the EDUCATION (#20.11) file. To support this functionality, Patch XU\*8.0\*679 added the EDUCATION (Degree) File Edit \[XUSESIG DEG\] option to the User Management \[XUSER\] menu. The EDUCATION (Degree) File Edit \[XUSESIG DEG\] option, which is locked by the XUSIG security key, enables maintenance of DEGREE field entries in the EDUCATION (#20.11) file. VistA uses these records to validate user entries when appending one or more degrees to an electronic signature. This validation applies even when the XU SIG BLOCK DISABLE parameter is set to OFF.

![](kernel-8-0-systems-management-signon-security-user-guide/080.png) NOTE: Because VistA automatically cross-references DEGREE (#10.6) field entries in the NEW PERSON (#200) file with the DEGREE (#6) field in the NAME COMPONENTS (#20) file, any updates made directly to the DEGREE (#6) field in the NAME COMPONENTS (#20) file will also be validated against degrees in the EDUCATION (#20.11) file.

### Clear Electronic signature code Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clear Electronic signature code \[XUSESIG CLEAR\] option is another option available to system administrators that allows the clearing (deleting) of an electronic signature code. This option is locked with the XUMGR security key. This option can be used to clear a user’s electronic signature code if the user has forgotten the code. The user can then enter a new code with the Electronic Signature code Edit \[XUSESIG\] option in the User’s Toolbox \[XUSERTOOLS\] menu.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-signon-security-user-guide/081.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-signon-security-user-guide/082.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-signon-security-user-guide/083.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.