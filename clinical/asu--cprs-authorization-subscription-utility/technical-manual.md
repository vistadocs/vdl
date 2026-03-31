---
title: ASU Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: 
app_code: ASU
app_name: "CPRS: Authorization Subscription Utility"
section: CLI
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
  - table
  - class
  - contents
  - blockquote
  - classes
  - style
  - width
  - membership
  - access
  - exported
page_count: 0
word_count: 1608
section_count: 9
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/asutm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/asutm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=58"
---

![](asu-technical-manual/001.png)

AUTHORIZATION/SUBSCRIPTION UTILITY(ASU)TECHNICAL MANUAL

July 1997

Technical Services

Computerized Patient Record System Product Line

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td>USR*1*27 Patient Record Flags phase II</td>
<td>Page <a href="#important-integration-agreements">17</a></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

Table Of Contents

Revision History [ii](#revision-history)

Introduction [4](#introduction)

Implementation & Maintenance [6](#implementation-maintenance)

Initialize Membership of User Classes [6](#initialize-membership-of-user-classes)

Exported Menus & Options [7](#exported-menus-options)

Files and Globals [9](#files-and-globals)

Exported Routines [15](#exported-routines)

Purging & Archiving [15](#purging-archiving)

Callable Routines, Entry Points, and APIs [16](#callable-routines-entry-points-and-apis)

Important Integration Agreements [16](#important-integration-agreements)

Direct File Access [16](#direct-file-access)

Calls [16](#calls)

External Relations [18](#external-relations)

Online Documentation [19](#online-documentation)

Globals [20](#globals)

XINDEX [20](#xindex)

?, ??, and ??? Online Help [20](#and-online-help)

Appendix AASU Security [21](#appendix-aasu-security)

Menu Access [21](#menu-access)

VA FileMan File Protection [22](#va-fileman-file-protection)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Implementation & Maintenance](#implementation-maintenance)
  - [Initialize Membership of User Classes](#initialize-membership-of-user-classes)
- [Exported Menus & Options](#exported-menus-options)
- [Files and Globals](#files-and-globals)
- [Exported Routines](#exported-routines)
- [Purging & Archiving](#purging-archiving)
- [Callable Routines, Entry Points, and APIs](#callable-routines-entry-points-and-apis)
  - [Important Integration Agreements](#important-integration-agreements)
    - [Direct File Access](#direct-file-access)
    - [Calls](#calls)
- [External Relations](#external-relations)
- [Online Documentation](#online-documentation)
  - [Globals](#globals)
  - [## XINDEX](#xindex)
  - [?, ??, and ??? Online Help](#and-online-help)
- [Appendix AASU Security](#appendix-aasu-security)
  - [Menu Access](#menu-access)
  - [VA FileMan File Protection](#va-fileman-file-protection)
Overview
> The Authorization/Subscription Utility (ASU) implements a User Class Hierarchy which is useful for identifying the roles that different users fulfill within the hospital. It also provides tools for creating business rules that apply to documents used by members of such groups. ASU provides a method for identifying who is AUTHORIZED to do something (for example, sign and order).
Features
- ASU lets you define, populate, and retrieve information about User Classes. These User Classes can be defined hospital-wide or more narrowly for a specific service and can be used across VISTA to replace and/or complement keys.
- ASU lets you link user classes with TIU Document Definitions and document events. This part of ASU defines behavior for TIU documents only.
- The User Class Membership file is a relational file, which allows a many-to-many relationship to be defined between User Classes and their members (as defined in the New Person File (#200)).
- Membership in classes may be scheduled for automatic transition to other classes (e.g., the PGY1 Residents will rotate on June 30<sup>th</sup>, and will become PGY2 Residents as of July 1<sup>st</sup>).
- Other applications within VistA may access the User Class file to determine the role of an employee.
- The Authorization/Subscription file (#8930.1) is another relational table, linking actions or events (e.g., Signature) with Document Definitions (e.g., Clinical Warning Note), record statuses, user classes (e.g., Provider) and user roles (e.g., Author, Expected Signer, Expected Cosigner, etc.). In this manner, a “Knowledge Base” or table of “Production Rules” can be developed in compliance with the site’s local by-laws (or in some cases, national requirements) for handling of various elements of the medical record. This eliminates the need for “hard-coding” business rules within the application, thereby enforcing policies, independent of the local facility’s preferences. These rules are also “inherited” through both the User Class and Document Definition hierarchies.
- ASU imposes no limitation on the depth or specificity of the User Class hierarchy, which a site may choose to develop.

# Implementation & Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ASU Version 1 is distributed and installed with Text Integration Utilities (TIU) Version 1. After installing these packages, implementation and maintenance are handled through the processes described throughout this manual and the ASU Clinical Coordinators Manual.

## Initialize Membership of User Classes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option invokes a routine for seeding the User Class Membership file (^USRPROV). *Initialize Membership of User Classes* \[USR INITALIZE MEMBERSHIP\] is on the TIU Conversions Menu \[TIU CONVERSIONS MENU\] option.

> This option populates the Provider Class (which includes physicians, nurses, psychologists, social workers, and other caregivers) determined by membership in the New Person file, ownership of keys, possession of a VA NUMBER (to allow Medication ordering), etc. It should be run ONCE when first implementing ASU.

# Exported Menus & Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign menus and options as described in this table: These options provide the means for setting up and managing User Classes and Business Rules. See the *Authorization/Subscription Utility Clinical Coordinator Manual* for examples of using these options. Recommended assignments are shown in the table below.

| Option Text            | Option Name              | Description                                                                                                                                                                                                                                                                    | Assignment                                     |
|----------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| User Class Management Menu | USR CLASS MANAGEMENT MENU    | This is the menu of options for management of User Class Definition and Membership.                                                                                                                                                                                                | IRMS, Clinical Coordinators                        |
| User Class Definition      | USR CLASS DEFINITION         | This option allows review, addition, editing, and removal of User Classes.                                                                                                                                                                                                         | IRMS, Clinical Coordinators                        |
| List Membership by User    | USR LIST MEMBERSHIP BY USER  | This option allows you to review, add, and edit individual members of User Classes.                                                                                                                                                                                                | IRMS, Clinical Coordinators, AO’s & Service Chiefs |
| List Membership by Class   | USR LIST MEMBERSHIP BY CLASS | This option allows review, addition, editing, and removal of individual members in User Classes.                                                                                                                                                                                   | IRMS, Clinical Coordinators, AO’s & Service Chiefs |
| Show Class Membership      | USR SHOW MEMBERSHIP          | This menu option contains the following two options which allow review only of class membership.                                                                                                                                                                                   | End users                                          |
| Show Membership by User    | USR SHOW MEMBERSHIP BY USER  | This option lists User Classes an individual is a member of.                                                                                                                                                                                                                       | End users                                          |
| Show Membership by Class   | USR SHOW MEMBERSHIP BY CLASS | This option lists the members of a selected User Class.                                                                                                                                                                                                                            | End users                                          |
| Edit Business Rules        | USR EDIT BUSINESS RULES      | This option allows the user to enter Business Rules authorizing specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an UNSIGNED PROGRESS NOTE may be EDITED by a PROVIDER who is also the EXPECTED SIGNER of the note, etc.). | IRMS, Clinical Coordinators                        |
| Manage Business Rules      | USR BUSINESS RULE MANAGEMENT | This option allows you to list the Business rules defined by ASU, and to add, edit, or delete them, as appropriate.                                                                                                                                                                | IRM, Clinical Coordinators                         |

> Allowable Statuses

|              |                   |                                                                                                                                                                                                     |
|--------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File IEN | Status        | Description                                                                                                                                                                                     |
| 8        | Amended       | The document has been completed and a privacy act issue has required its amendment.                                                                                                                 |
| 7        | Completed     | The document has acquired all necessary signatures and is legally authenticated.                                                                                                                    |
| 14       | Deleted       | The document has been deleted but the audit trail is retained.                                                                                                                                      |
| 15       | Retracted     | Used instead of Deleted after the document has been signed. If an error is discovered after signature, then the document is made invisible for most users, but retained as part of the audit trail. |
| 6        | Uncosigned    | The document is complete, with the exception of cosignature by the attending physician.                                                                                                             |
| 1        | Undicatated   | The document is required and a record has been created in anticipation of dictation and transcription.                                                                                              |
| 3        | Unreleased    | The document is in the process of being entered into the system, but hasn’t been released by the originator (i.e., the person who entered the text online).                                         |
| 5        | Unsigned      | The document is online in a draft state, but the author's signature hasn’t yet been obtained.                                                                                                       |
| 2        | Untranscribed | This status is used for business rules permitting entry of not-yet-existing documents into the file.                                                                                                |
| 4        | Unverified    | The document has been released or uploaded, but an intervening verification step must be completed before the document is available for signature.                                                  |

> NOTE: The list of statuses shown above should not be considered exhaustive or necessarily complete. As additional document types are incorporated into TIU, new statuses may require definition, to identify stages in workflow not yet anticipated.

> NOTE: Internal File Entry Numbers (IEN) in the USR Status File (#8930.6) are standardized and *must* not be changed.

# Files and Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                 |            |              |          |     |
|---------------------------------|------------|--------------|----------|-----|
| Name                        | Number | Global   | Data |     |
| USR CLASS                       | 8930       | ^USR(8930,   |          | YES |
| USR AUTHORIZATION/ SUBSCRIPTION | 8930.1     | ^USR(8930.1, |          | YES |
| USR ROLE                        | 8930.2     | ^USR(8930.2, |          | YES |
| USR CLASS MEMBERSHIP            | 8930.3     | ^USR(8930.3, |          | YES |
| USR SEARCH CATEGORIES           | 8930.4     | ^USR(8930.4, |          | YES |
| USR RECORD STATUS               | 8930.6     | ^USR(8930.6, |          | YES |
| USR ACTION                      | 8930.8     | ^USR(8930.8, |          | YES |

> The ASU global ^USR (should be journaled.

> USR CLASS (#8930)

> This file is intended to allow the definition of user classes in such a way that they are useful across packages. It will undoubtedly evolve with more experience in this area.

> These user classes are then used to support part of the “authorization” concept: who may do what to a document or order, in its current state.

> They will also used to support part of the “subscription” concept: who should receive something, e.g. a notification that a document needs signature.

> The User Authorization/Subscription file points to the User Class file to allocate authorizations/subscriptions to appropriate user classes. The User Class Membership file links users in the New Person file to User Classes in a many-to-many relationship.

> This file supports an infinite hierarchy of subclasses, with each entry having as many subclasses as desired. Subclasses are contained in the same file, as entries in their own right. A class automatically contains as members all members of its subclasses, as well as explicit members of the class itself.

> USR AUTHORIZATION/SUBSCRIPTION (#8930.1)

> This file associates users with actions on documents.

> Actions are of two kinds— authorization actions such as the signature action, which an associated user is authorized to perform, and subscription actions, such as an unsigned document notification, which the associated user will be able to “sign up to receive.”

> An action may be associated with a USER CLASS in the User Class file (e.g. Staff Physician class) *and/or* with a USER ROLE in relation to the document in question (e.g. author or expected cosigner).

> If an Authorization/Subscription entry has both User Class AND User Role, the AND FLAG field permits these requirements to be “AND'ed”; that is, a user must both belong to the User Class AND must fill the User Role in order to perform the action. If the AND FLAG has value OR, or has no value, then User Class and User Role within the same entry are “OR'ed.”

> Each file entry associates an action with one user class and/or one role. The entry makes this association for a given Document Definition (e.g. Progress Note) of a given status (e.g. Unsigned).

> Multiple file entries for the SAME action/Document Definition/document status allow association with more than one user class/role. Such entries are “OR'ed”; that is, if a user belongs to the user class/role of one OR another of these entries, the user may perform the action.

> User classes automatically INCLUDE members of their subclasses, as defined in the User Class file.

> Document Definitions exist in a hierarchy in file 8925.1, with Classes at the top level, Document Classes at the next level down, and Titles under Document Classes. Authorization/Subscription entries may be defined at any of the above levels. For example, an authorization which applies to most or all Progress Notes should be defined at the Class level for Document Definition “Progress Note.” On the other hand, an authorization, which applies, only to Progress Notes of Title “Dental Hygiene Note” should be defined at the Title level for Document Definition “Dental Hygiene Note.”

> *USR AUTHORIZATION/SUBSCRIPTIONFile, cont’d*

> When using authorizations/subscription to determine whether a given user may perform a given action on a document of a given title in its current status, the code begins by checking entries for that action and status FOR THAT TITLE. If ANY such entries exist, then entries for higher Document Definition levels will be ignored, and the user passes/fails based on that level alone. Thus, if a Title is linked with a certain action, status, and user class, then rules for that Title, action, and status should be entered for ALL user classes that can perform the action on the Title, since broader authorization (e.g. Provider class) set at higher levels (e.g. Progress Notes) is ignored (i.e., inheritance of the privilege is “overridden”).

> If such entries do NOT exist, the next higher level of Document Definition is checked. And so on.

> If no entries are found on any level, no users can perform/subscribe to the action for the given Document Definition and status.

> In this manner, the authority to perform different actions is “inherited” through BOTH the User Class and Document Definition hierarchies.

> USR CLASS MEMBERSHIP (\#8930.3)

> This file links a person from the New Person file to a class in the User Class file. Since user class membership includes members of all subclasses, users should be made members of the most discrete class in a hierarchy of classes. For example, if Jones is a dentist, Jones should be entered into the Dentist class. Since Dentist is a subclass of the Provider class, Jones is then automatically a Provider.

> Persons wearing several different hats can have more than one entry in the file. For example, Smith might be a dietitian also working toward a nursing degree. Smith could be entered twice, once as a Dietitian and once as a Student Nurse.

> USR SEARCH CATEGORIES (#8930.4)

> This file defines the Search Categories available to ASU’s “Rule Browser.” The Rule Browser is a tool which allows the user to call for all rules that apply to a given Document Definition (e.g., Progress Notes), User Class (e.g., PROVIDER), or User Role (e.g., EXPECTED SIGNER). The USR SEARCH CATEGORIES file supports this selection, and allows for its future extension to include other useful categories, as they become apparent.

> USR RECORD STATUS (#8930.6)

> This file contains the allowable statuses that may be applied to a document or order during its path through the system. It also contains statuses for Document Definitions (e.g., ACTIVE, INACTIVE, and TEST).

> USR ACTION (#8930.8)

> This file encodes actions, which occur in connection with clinical narrative documents. These actions are referenced by entries in the User Authorization/ Subscription file to associate users with actions.

> This file contains two kinds of actions: those a user is authorized to perform on a document, and those a user subscribes to for a document. For example, a user is authorized to perform the Signature action, but a user subscribes to (“signs up to receive”) a Notification action.

  
User Class Structure:NOTE: The following diagram illustrates a possible subset of the “standard” user classes. ASU allows membership in multiple classes on a time-dependent basis, and utilities are included to support the scheduled transition of users between classes. The intention is to allow the burden of maintaining membership in such classes to be distributed to the persons at a site who have traditionally maintained personnel rosters: Administrative Officers and Service Chiefs.

The only inheritance which applies to the User Class file that that of membership. Membership in a given User Class automatically includes all members of all subclasses of that class. The User Class file does not contain a single hierarchy like the Document Definition file: a user my belong to sever different user hierarchies. Therefore, settings for a subclass my *not* be used to override setting for a class above it—but the reverse *is* true. Settings for a super class override the settings of the classes below it.

# Exported Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> USRAEDT USRCLASS USRCLST USRECLST USRIL USRL USRLA USRLM USRLS USRM USRMEMBR USRMLST USRNTEG USRPOST USRPRE USRPROV USRRUL USRRUL1 USRRULA USRULST USRUM USRUMMBR

# Purging & Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Archiving utilities are not provided for the distributed files.

# Callable Routines, Entry Points, and APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASU provides a number of entry points to which client applications may subscribe. These are listed on the DBA menu on FORUM.

## Important Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following integration agreements provide access to ASU in a manner that may be useful to package integrators. Database Integration Agreements (DBIA) are available on the DBA menu on Mailman.

### Direct File Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Agreement \#1545 is a Private agreement and has the following provisions:

Read access to the following global:

^USR(8930 The USR CLASS File (#8930)

### Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other agreements provide the following entry points:

#### USRLM 

Each of the following entry points is covered by one or more of the following agreements: 1544, 2324, 2712.

\$\$ISA(USER,CLASS,ERR,USRDT) - Boolean - Is USER a Member of CLASS on the given date USRDT

\$\$SUBCLASS(DA,CLASS) – Boolean – Is class DA a subclass of CLASS as specified in the USR CLASS file \#8930

WHOIS2(MEMBER,CLASS)- Given a Class, return list of members in the array MEMBER

WHATIS(USER,CLASS) - When passed a DUZ in the variable USER returns all the USR classes a user is a member of in the array CLASS

\$\$CLNAME(CLASS) - This entry point when passed the class IEN will return the USR class display name (.04).

\$\$ISTERM(USER) – Boolean – Is USER terminated

#### USRLA

Covered by agreement \#2325.

\$\$CANDO(DOCTYPE,STATUS,EVENT,USER,USRROLE) – Boolean – Can USER perform the action EVENT on a document of type DOCTYPE of status STATUS

#### USRLFF

Covered by agreement \#2329.

\$\$EVNTPTR(EVENT) Given name EVENT of an action, returns action IEN

\$\$EVNTVERB(IEN) Given the IEN of an action, returns its verb

\$\$HASAS(IEN) Boolean – Does title IEN have Authorizations/ Subscriptions.

\$\$USRCLASS(IEN) Returns the 0 node of user class IEN

\$\$USRROLE(ROLE) Returns IEN of ROLE in the USR ROLE file 8930.2

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ASU is dependent upon the following V*IST*A packages to function correctly.

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Package</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Minimum Version</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Information Management System (PIMS)</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Text Integration Utilities (TIU)</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., files, routines and options) exported with this software.

> Use the KIDS Install File Print option if you’d like to print out the results of the installation process.

> You can also use the Kernel option, List Routines \[XUPRROU\], to print a list of any or all of the ASU routines. This option is found on the Routine Tools \[XUPR-ROUTINE-TOOLS\] menu on the Programmer Options \[XUPROG\] menu, which is a sub-menu of the Systems Manager Menu \[EVE\] option. The namespace for the ASU package is USR.

> Example:

> Select Systems Manager Menu Option: programmer Options

> Select Programmer Options Option: routine Tools

> Select Routine Tools Option: list Routines

> Routine Print

> Want to start each routine on a new page: No// \<Enter\>

> routine(s) ? \> USR\*

> The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option, First Line Routine Print \[XU FIRST LINE PRINT\], to print a list of just the first line of each ASU subset routine.

> Example:

> Select Systems Manager Menu Option: programmer Options

> Select Programmer Options Option: routine Tools

> Select Routine Tools Option: First Line Routine Print

> PRINTS FIRST LINES

> routine(s) ? \>USR\*

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The only global distributed by the ASU package is ^ASU(8930.

> Use the Kernel option, List Global \[XUPRGL\], to print this global. This option is on the Programmer Options menu \[XUPROG\], which is a sub-menu of the Systems Manager Menu \[EVE\] option.

> Example:

> Select Systems Manager Menu Option: programmer Options

> Select Programmer Options Option: LIST Global

> Global ^USR\*

## ## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls.

> XINDEX is invoked from programmer mode: D ^XINDEX.

> When selecting routines, select USR\*.

## ?, ??, and ??? Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ? Enter one question mark to see helpful information about the components of the ASU and the options available.

> ?? Enter two question marks to see a list of available ASU components.

> ??? Enter three question marks for detailed help, if available.

# Appendix AASU Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security for ASU is established via a combination of menu assignment, User Class assignment, and FileMan access. See earlier sections in this manual and also the ASU User Manual for descriptions of how User Class assignment works.

## Menu Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                            |                              |                                                                                                                                                                                                                                                                                    |                                                    |
|----------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Option Text            | Option Name              | Description                                                                                                                                                                                                                                                                    | Assignment                                     |
| User Class Management Menu | USR CLASS MANAGEMENT MENU    | This is the menu of options for management of User Class Definition and Membership.                                                                                                                                                                                                | IRMS, Clinical Coordinators                        |
| User Class Definition      | USR CLASS DEFINITION         | This option allows review, addition, editing, and removal of User Classes.                                                                                                                                                                                                         | IRMS, Clinical Coordinators                        |
| List Membership by User    | USR LIST MEMBERSHIP BY USER  | This option allows you to review, add, and edit individual members of User Classes.                                                                                                                                                                                                | IRMS, Clinical Coordinators, AO’s & Service Chiefs |
| List Membership by Class   | USR LIST MEMBERSHIP BY CLASS | This option allows review, addition, editing, and removal of individual members in User Classes.                                                                                                                                                                                   | IRMS, Clinical Coordinators, AO’s & Service Chiefs |
| Show Class Membership      | USR SHOW MEMBERSHIP          | This menu option contains the following two options which allow review only of class membership.                                                                                                                                                                                   | End users                                          |
| Show Membership by User    | USR SHOW MEMBERSHIP BY USER  | This option lists User Classes an individual is a member of.                                                                                                                                                                                                                       | End users                                          |
| Show Membership by Class   | USR SHOW MEMBERSHIP BY CLASS | This option lists the members of a selected User Class.                                                                                                                                                                                                                            | End users                                          |
| Edit Business Rules        | USR EDIT BUSINESS RULES      | This option allows the user to enter Business Rules authorizing specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an UNSIGNED PROGRESS NOTE may be EDITED by a PROVIDER who is also the EXPECTED SIGNER of the note, etc.). | IRMS, Clinical Coordinators                        |
| Manage Business Rules      | USR BUSINESS RULE MANAGEMENT | This option allows you to list the Business rules defined by ASU, and to add, edit, or delete them, as appropriate.                                                                                                                                                                | IRM, Clinical Coordinators                         |

## VA FileMan File Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ASU package files are exported with the following file protection provided by VA FileMan:

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File Number</td>
<td>Name</td>
<td>DD</td>
<td>RD</td>
<td>WR</td>
<td>DEL</td>
<td>LAYGO</td>
<td>AUDIT</td>
</tr>
<tr class="even">
<td>8930</td>
<td>USR CLASS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>8930.1</td>
<td><p>USR AUTHORIZATION/</p>
<p>SUBSCRIPTION</p></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>8930.2</td>
<td>USR ROLE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>8930.3</td>
<td>USR CLASS MEMBERSHIP</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>8930.4</td>
<td>USR SEARCH CATEGORIES</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>8930.6</td>
<td>USR RECORD STATUS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>8930.8</td>
<td>USR ACTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>