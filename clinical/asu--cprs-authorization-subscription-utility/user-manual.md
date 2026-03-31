---
title: ASU Clinical Coordinator Manual
doc_type: UM
doc_label: Clinical Coordinator Manual
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
menu_options: 2
description: "<table> <colgroup> <col style=\\"width: 27%\\" /> <col style=\\"width: 22%\\" /> <col style=\\"width: 20%\\" /> <col style=\\"width: 29%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><p>USR138 –</p> <p>Updated Notes on User Class and User Role SURROGATE</p></td> <td>Page <a href=\\"#notes-on-user-class-and-user-role"
audience: 
keywords: 
  - class
  - table
  - clinical
  - document
  - contents
  - classes
  - chief
  - rules
  - business
  - unsigned
page_count: 0
word_count: 6372
section_count: 12
table_count: 13
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: July 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/asuum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/asuum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=58"
---

![](asu-clinical-coordinator-manual/001.png)

AUTHORIZATION/SUBSCRIPTION UTILITY(ASU)CLINICAL COORDINATOR MANUAL

July 1997

Technical Services

Computerized Patient Record System Product Line

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>USR*1*38 –</p>
<p>Updated Notes on User Class and User Role SURROGATE</p></td>
<td>Page <a href="#notes-on-user-class-and-user-role-surrogate">27</a></td>
<td>January 2016</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Remedy 248385</td>
<td>Page 27</td>
<td>October 2011</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td colspan="2">USR*1*30 New action EDIT COSIGNER</td>
<td>December 2006</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td colspan="2">USR*1*27 Patient Record Flags phase II</td>
<td>May 2006</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  
Preface

> This manual provides descriptions of menus, options, and other information required for Clinical Coordinators, IRM staff, ADPACs, or other managers to effectively set up and use the Authorization/ Subscription Utility.

> Related Manuals

*Authorization/Subscription Utility (ASU) Technical ManualText Integration Utility (TIU) Clinical Coordinator & User ManualText Integration Utility (TIU) Implementation Guide<u>  
</u>*Table of Contents

Revision History [i](#_Toc307764381)

Section I: Introduction [1](#section-i-introduction)

Chapter 1: Introduction to ASU [2](#chapter-1-introduction-to-asu)

Purpose of ASU [2](#purpose-of-asu)

Chapter 2: Software and Documentation Conventions [4](#chapter-2-software-and-documentation-conventions)

About This Manual [4](#_Toc307764386)

Web Resources [4](#_Toc307764387)

Package Conventions [5](#package-conventions)

Online Help [6](#online-help)

Other (hidden) Actions [7](#other-hidden-actions)

Section II: Using ASU [8](#section-ii-using-asu)

Chapter 3: Defining and Managing User Classes [9](#chapter-3-defining-and-managing-user-classes)

ASU Menu and options [12](#asu-menu-and-options)

User Class Definition Option [14](#user-class-definition-option)

List Membership by User [17](#list-membership-by-user)

List Membership by Class [18](#list-membership-by-class)

Action Definitions [19](#action-definitions)

Example: Assigning Medical Record Technicians and Chief, HIMS to user classes. [20](#example-assigning-medical-record-technicians-and-chief-hims-to-user-classes.)

Chapter 4: Adding, Editing, and Managing Business Rules [23](#chapter-4-adding-editing-and-managing-business-rules)

Edit Business Rules [24](#edit-business-rules)

Notes on User Class and User Role SURROGATE [27](#notes-on-user-class-and-user-role-surrogate)

Example 3: Entering user classes that require cosignature [31](#example-3-entering-user-classes-that-require-cosignature)

Status List [39](#status-list)

Action List [40](#action-list)

Helpful Hints [43](#helpful-hints)

Troubleshooting & Helpful Hints for ASU Business Rules [43](#troubleshooting-helpful-hints-for-asu-business-rules)

More Information about ASU and User Class [45](#more-information-about-asu-and-user-class)

Relationship between User Class file and Person Class file [45](#relationship-between-user-class-file-and-person-class-file)

Amount of Set-up for User Class & Business Rules [46](#amount-of-set-up-for-user-class-business-rules)

Initial Population of Basic User Classes [46](#initial-population-of-basic-user-classes)

Glossary [47](#glossary)

Appendices [49](#appendices)

Appendix A: Exported User Classes [51](#appendix-a-exported-user-classes)

Appendix B: Exported Business Rules [57](#appendix-b-exported-business-rules)

Index [62](#index)

# Section I: Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Section I: Introduction](#section-i-introduction)
- [# Chapter 1: Introduction to ASU](#chapter-1-introduction-to-asu)
  - [Purpose of ASU](#purpose-of-asu)
- [Chapter 2: Software and Documentation Conventions](#chapter-2-software-and-documentation-conventions)
  - [About This Manual](#about-this-manual)
  - [Web Resources](#web-resources)
  - [Package Conventions](#package-conventions)
  - [Online Help](#online-help)
    - [### Other (hidden) Actions](#other-hidden-actions)
- [Section II: Using ASU](#section-ii-using-asu)
- [Chapter 3: Defining and Managing User Classes](#chapter-3-defining-and-managing-user-classes)
    - [### ASU Menu and options](#asu-menu-and-options)
    - [User Class Definition Option](#user-class-definition-option)
    - [### ### List Membership by User](#list-membership-by-user)
    - [> NOTE: Two new options were created with ASU patch 4, May 1998, to be used for viewing only: Show Membership by User and Show membership by Class.](#note-two-new-options-were-created-with-asu-patch-4-may-1998-to-be-used-for-viewing-only-show-membership-by-user-and-show-membership-by-class)
    - [List Membership by Class](#list-membership-by-class)
    - [Action Definitions](#action-definitions)
    - [Example: Assigning Medical Record Technicians and Chief, HIMS to user classes.](#example-assigning-medical-record-technicians-and-chief-hims-to-user-classes)
- [Chapter 4: Adding, Editing, and Managing Business Rules](#chapter-4-adding-editing-and-managing-business-rules)
    - [Edit Business Rules](#edit-business-rules)
    - [Example 3: Entering user classes that require cosignature](#example-3-entering-user-classes-that-require-cosignature)
    - [### > NOTE: Your site might redefine the User Classes so that Nursing Supervisor is under the User Class Nurse. In this case, steps 8 and 9 in the above example wouldn’t be necessary.](#note-your-site-might-redefine-the-user-classes-so-that-nursing-supervisor-is-under-the-user-class-nurse-in-this-case-steps-8-and-9-in-the-above-example-wouldnt-be-necessary)
    - [Status List](#status-list)
    - [### Action List](#action-list)
- [Helpful Hints](#helpful-hints)
    - [Troubleshooting & Helpful Hints for ASU Business Rules](#troubleshooting-helpful-hints-for-asu-business-rules)
    - [More Information about ASU and User Class](#more-information-about-asu-and-user-class)
    - [### Relationship between User Class file and Person Class file](#relationship-between-user-class-file-and-person-class-file)
  - [Amount of Set-up for User Class & Business Rules](#amount-of-set-up-for-user-class-business-rules)
    - [### Initial Population of Basic User Classes](#initial-population-of-basic-user-classes)
- [Glossary](#glossary)
- [Appendices](#appendices)
- [Appendix A: Exported User Classes](#appendix-a-exported-user-classes)
  - [INTERN: OSTEOPATHIC](#intern-osteopathic)
  - [PSYCHOLOGY INTERN](#psychology-intern)
  - [STAFF PHYSICIAN](#staff-physician)
- [Appendix B: Exported Business Rules](#appendix-b-exported-business-rules)
- [Index](#index)
Chapter 1: Overview of ASU
Purpose of ASU
Background
Functionality
Chapter 2:Introduction to the ASU User Manual
Purpose of the manual
How the manual is organized
Graphic conventions used in this manual
Software Conventions

# # Chapter 1: Introduction to ASU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of ASU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Authorization/Subscription Utility (ASU) implements a User Class Hierarchy which is useful for identifying the roles that different users fulfill within the hospital. It also provides tools for creating business rules that apply to documents used by members of such groups. ASU provides a method for identifying who is AUTHORIZED to do something (for example, sign and order). ASU originated in response to the long recognized demand for a means of implementing the “Scope of Practice” model, which was first discussed during the analysis and design of OE/RR v1.96, but the driving force behind its development was the complexity of Text Integration Utilities’ (TIU’s) document definition needs. Current security key capabilities were unable to efficiently manage the needs of clinical documentation (Discharge Summaries, Progress Notes, etc.).

> ASU Features & Benefits

- ASU lets you define, populate, and retrieve information about User Classes. These User Classes can be defined hospital-wide or more narrowly for a specific service and can be used across V*IST*A to replace and/or complement keys.
- ASU lets you link user classes with Document Definitions and document events. This part of ASU defines behavior TIU documents only.
- The User Class Membership file is a relational file which allows a many-to-many relationship to be defined between User Classes and their members (as defined in the New Person File (#200)).
- Membership in classes may be scheduled for automatic transition to other classes (e.g., the PGY1 Residents will rotate on June 30<sup>th</sup>, and will become PGY2 Residents as of July 1<sup>st</sup>).
- The Authorization/Subscription file (#8930.1) is another relational table, linking actions or events (e.g., Signature) with Document Definitions (e.g., Clinical Warning Note), record statuses, user classes (e.g., Provider) and user roles (e.g., Author, Expected Signer, Expected Cosigner, etc.). In this manner, a “Knowledge Base” or table of “Production Rules” can be developed in compliance with the site’s local by-laws (or in some cases, national requirements) for handling of various elements of the medical record. This eliminates the need for “hard-coding” business rules within the application, thereby enforcing policies, independent of the local facility’s preferences. These rules are also “inherited” through both the User Class and Document Definition hierarchies.
- ASU imposes no limitation on the depth or specificity of the User Class hierarchy which a site may choose to develop.
- Other applications within VistA may access the User Class file to determine the role of an employee.

# Chapter 2: Software and Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual contains a description of the ASU package and all the ASU options. A glossary, index, and appendices are located at the end of this manual and contain added information and guidance for the user. The appendices contain lists of the user classes and business rules exported with TIU/ASU.

## Web Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product is available on the intranet at the following address:

<http://www.va.gov/vdl/>

This address takes you to the VistA Document Library (VDL) page where you find a listing of all the clinical software manuals. Click on the CPRS: Authorization/ Subscription Utility (ASU) link and it will take you to the ASU Document Library page which has the latest revisions of each ASU manual.

Another usefull link is to select CPRS: Text Integration Utility (TIU). Since ASU is closely related to TIU the latest TIU manuals may be helpful.

The links given above are outside the VA Firewall and can be accessed from any computer with a WWW hookup. Also useful are the ASU and TIU home pages, which are only accessible from computers equiped with an network browser and connected to the VA intranet. These pages are:

[redacted](http://vista.med.va.gov/asu) and [redacted](http://vista.med.va.gov/tiu)

These pages often contain information that is not in the manual as well as information on upcoming enhancements.

  
Documentation Conventions\<Enter\>

This symbol is used throughout the manual in computer screen dialogues to indicate the Enter, RETURN, or ↵ key. Press it after every response you enter or when you wish to bypass a prompt, accept a default (//), or return to a previous action.

Option examples

Menus and examples of computer dialogue that you’ll see on your terminal are shown here in boxes.

Select User Class Management Option: 1 User Class Definition

Select User Class Status: ACTIVE// \<Enter\> Active ?

Active All User Classes

Inactive

Enter selection(s) by typing the name(s), number(s), or abbreviation(s).

Start With Class: FIRST// \<Enter\>

Go To Class: LAST// \<Enter\>User responses

In computer dialogues, user responses are shown in boldface type.

Select NEW PERSON NAME: GRIN,JONIcons

Icons used to highlight key points in this manual include:

Indicates especially important information.

## Package Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defaults (//)

Defaults are responses provided to speed up your entry process. They are either the most common responses, the safest responses, or the previous response. Examples:

*Most common*: Enter the ending date: NOW//

*Safest:* Do you wish to delete the entire entry: NO//

*Last entered* Enter the Provider Name: WELBY,DOCTOR//

To accept the response, press the \<Enter\> key.

To enter a different response, type in your preferred answer.

  
Up-arrows (caret or a circumflex)

^ A single up-arrow does several functions in the package depending on where you are and what you are doing.

The up-arrow can terminate a series of questions and return you to a previous level.

^^ Two up-arrows exit you out of the option you’re in and return you to the menu.

## Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

?, ??, ??? Online help is available if you enter one, two, or three question marks at a prompt. One question mark elicits a brief statement of what information is appropriate for the prompt; two question marks will get you more help, plus the hidden actions shown above; and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

List Manager Screen Display

ASU uses the List Manager utility which allows TIU (and other applications) to display a list of items in a screen format. If the list is longer than one screen, the header and action portion of the screen remain stable, while the center display scrolls. So if there are too many user classes to fit within the scrolling portion of the screen, pressing the return key causes that portion of the screen to scroll up while the top and bottom stay unchanged.

<u>User Classes Jan 11, 1996 16:29:56 Page: 1 of 38</u>

ACTIVE USER CLASSES 568 Classes

<u>Class Name Abbrev</u>

1 ADP Coordinator ADPAC Active

2 ADP Security Officer ISO Active

3 ASC Member ASCM Active

4 Accountant ACC Active

5 Accounts Payable Employee PAY Active

6 Accounts receivable employee RCV Active

7 Accreditation Representative JCAHO Active

8 Acting Assistant Chief AAC Active

9 Acting Assistant Director AAD Active

10 Acting Chief AC Active

+ + Next Screen - Prev Screen ?? More Actions

Find Expand/Collapse Tree Quit

Create a Class List Members

Edit User Class Change View

Select Action: Next Screen// Create a Class

The List Manager utility then lets you:

- browse through the list
- select items that need action
- take action against those items
- select other actions without leaving the option

> At the Select Action prompt, type the name or abbreviation of the action you wish (Find, Create a Class, Edit a Class, etc.) or the number of the item in the middle portion of the screen (Class Name), after which you will be prompted to enter the Action.

> Shortcut: Type the action abbreviation, then the number of the user class on the list (Example: ED=1 will process entry 1 for Edit) or vice versa. Type the item \# followed by an equals sign (=) and the Action or its abbreviation ("1=L" will produce a List of members of the ADP Coordinator user class).

### ### Other (hidden) Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you enter two question marks (??) at the Select Item(s) prompt, you will see a list of more actions that you can use with ASU.

> Select Item(s): Quit// ??

> The following actions are also available:

> \+ Next Screen UP Up a Line GO Go to Page

> \- Previous Screen DN Down a Line RD Re Display Screen

> FS First Screen \> Shift View to Right PL Print List

> LS Last Screen \< Shift View to Left ADPL Auto Display(On/Off)

> Press RETURN to continue or '^' to exit:

## > .

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Section II: Using ASU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Chapter 3: How to Define and Manage User Classes

ASU Menus and options

Chapter 4: How to Add, Edit, and Manage Business Rules  

# Chapter 3: Defining and Managing User Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Authorization/Subscription Utility (ASU) assists IRM staff, Clinical Coordinators, and other managers in defining and populating a User Class Hierarchy which is useful for identifying the roles that different users fulfill within the hospital. It also lets you specify business rules for the handling of documents by members of such groups. This version of ASU defines behavior only for Text Integration Utility (TIU) documents.

> A routine for seeding the User Class Membership file (USRPROV) can be started through the option, *Initialize Membership of User Classes* \[USR INITALIZE MEMBERSHIP\]. This option populates the Provider User Class, based on membership in the Provider file. It should be run ONCE when first implementing ASU.

> User classes can also be populated through options described here. Class members may be active or inactive. Events such as ordering or signing can be linked with Document/Order type (e.g., Clinical Warning Note) with user classes (e.g., Provider Class).

> Infinite hierarchies of subclasses can be created and one level of document type can inherit authorizations from a higher level.

> For example, if an entry in the Authorization/Subscription file states that the user class, Physician, may sign Progress Notes, and if Service Chief is a subclass, then Service Chiefs may also sign Progress Notes.

> *Defining and Managing User Classescontd*

> Keep it Simple!!

> ASU is exported with pre-defined sets of Document Classes and Business Rules, and we offer some simple tools or suggestions for populating the basic User Classes (i.e., PROVIDERS, and MIS personnel) required for the “least restrictive” implementation of TIU. We recommend that you first implement TIU and ASU with these as your baseline rules and classes. As you gain familiarity with the package and begin to recognize areas where more control of access is appropriate, then you can think about defining a necessary and sufficient set of Rules and/or User Classes to handle your site requirements. Your guiding principles should be: “Keep it simplekeep it open” to the extent possible. Don’t impose restrictions on your users until you really have justification to do so. If you burden yourself with complexity too soon, you may pay a premium in unnecessary maintenance overhead and confusion.

> Some General Guidelines

- Since user class membership includes members of all subclasses, users should be made members of the most specific class in a hierarchy of classes. For example, if Dr. Jones is a dentist, she should be entered as a member of the Dentist class. Since Dentist is a subclass of the Provider class, Dr. Jones is then automatically a Provider.
- Distribute as much of the workload for identifying group membership as possible. Your facility’s Administrative Officers and Service Chiefs can probably direct you to the people in their departments who are already maintaining personnel rosters (frequently on paper). These are the ideal people to assist you in populating the User Class Membership at your site. Depending on their level of familiarity with V*IST*A, you may even want to give them access to the USR LIST MEMBERSHIP BY CLASS option, along with appropriate training as to its use.
- Persons wearing several different hats can have concurrent membership in more than one User Class. For example, Mr. Smith might be a dietitian also working toward a nursing degree. He can be entered as a member in two User Classes, once as a Dietitian and once as a Student Nurse.
- It is important to keepuser class membership up to date. Active membership in a user class can grant or limit privilege. Business rules always grand privilige. Other package sometime use user classes to limit privilege. For example, TIU Document Parameter USERS REUQIRE COSIGNATURE limits privlilege. If, say, user class STUDENT is listed for this parameter and as user’s membership in the STUDENT class expires, the the user *no longer requires cosignature when signing notes.*
- It is not necessary to populate the user class named USER. The Authorization/Subscription utility considers that every user is a member of this class whether or not they have been set explicityl as a member. This class is used for granting univaerals privilege via business rules for a given action on a given Document Definition. As always, these rules may be overrridden by setting additional rules at lower levels of the Document Definition Hierarchy.
- Any member of a given User Class is uatomatically considered a member of all superclasses of that class. For example, a suer who is set explicityl as a member of user class Physician is automatically a Provider, since Physician is a subclass of Provider. A user considered a Provider is automaticall a User, since Provider is a subclass of User.
- Membership in a given User Class automaticall includes all member of subclasses of that class. For example, the class Provider automatically includes all Social Worker and Physician members, since they are both subclasses of provider.

> Process for creating user classes:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td><blockquote>
<p><strong>Populate basic user classes with the exported user class file</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>2</strong></td>
<td><blockquote>
<p><strong>Finish implementation of TIU and get acquainted with the package, as well as the needs of your facility</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>3</strong></td>
<td><blockquote>
<p><strong>Define additional user classes</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>4</strong></td>
<td><blockquote>
<p><strong>Add members to user classes</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>5</strong></td>
<td><blockquote>
<p><strong>Modify (add or delete) user classes and their members, as needed</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>6</strong></td>
<td><blockquote>
<p><strong>Create or edit Business Rules</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

### ### ASU Menu and options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                          |                              |                                                                                                                                                                                                                                                                                    |
|--------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Option               | Option Name              | Description                                                                                                                                                                                                                                                                    |
| User Class Definition    | USR CLASS DEFINITION         | This option allows review, addition, editing, and removal of User Classes.                                                                                                                                                                                                         |
| List Membership by User  | USR LIST MEMBERSHIP BY USER  | This option allows review, addition, editing, and removal of individual members to and from User Classes.                                                                                                                                                                          |
| List Membership by Class | USR LIST MEMBERSHIP BY CLASS | This option allows review, addition, editing, and removal of individual members to and from User Classes.                                                                                                                                                                          |
| Show Class Membership    | USR SHOW MEMBERSHIP          | This menu option, which contains the two options listed below, can be assigned to users who only need to view membership.                                                                                                                                                          |
| Show Membership by User  | USR SHOW MEMBERSHIP BY USER  | This option lists the User Classes that an individual is a members of.                                                                                                                                                                                                             |
| Show Membership by Class | USR SHOW MEMBERSHIP BY CLASS | This option allows review only of members of selected User Classes.                                                                                                                                                                                                                |
| Edit Business Rules      | USR EDIT BUSINESS RULES      | This option allows the user to enter Business Rules authorizing specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an UNSIGNED PROGRESS NOTE may be EDITED by a PROVIDER who is also the EXPECTED SIGNER of the note, etc.). |
| Manage Business Rule     | USR BUSINESS RULE MANAGEMENT | This option allows you to list the Business rules defined by ASU, and to add, edit, or delete them, as appropriate.                                                                                                                                                                |

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td><blockquote>
<p><strong>Populate imported user classes</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> A basic set of user classes is exported with the ASU package. Use the option *Initialize Membership of User Classes* (on the TIU Conversion Menu) to populate the Provider User Class and the most common sub-classes with your local clinicians. Work with Administrative Officers and Service Chiefs to identify Students and MIS Staff, and set them up as members of the appropriate classes.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>2</strong></td>
<td><blockquote>
<p><strong>Finish implementation of TIU and get acquainted with the package, as well as with the needs of your facility</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> We recommend that you first implement TIU and ASU with the exported rules and classes as your baseline rules and classes. As you become more familiar with the package, then you can plan additional Rules and/or User Classes to handle the requirements of your site. Keep it as simple and open as you can. Avoid imposing unnecessary restrictions. ASU can handle an enormous spectrum of conditions and rules, but don’t burden yourself with unnecessary complexity too soon.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>3</strong></td>
<td><blockquote>
<p><strong>Define user classes</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> You can add or modify classes, as needed, to meet your site needs. The option *User Class Definition* lets you add and delete classes. Then use the options *List Membership by User* and *List Membership by Class* to add individual members to these user classes.

> When you begin to use ASU to develop a higher degree of control, keep the following in mind: Since user class membership includes members of all subclasses, users should be made members of the most specific class in a hierarchy of classes. For example, if Dr. Jones is a dentist, she should be entered as a member of the Dentist class. Since Dentist is a subclass of the Provider class, Dr. Jones is then automatically a Provider. Distribute as much of the workload for identifying group membership as possible. Your facility’s Administrative Officers and Service Chiefs can probably direct you to the people in their departments who are already maintaining personnel rosters (frequently on paper). These are the ideal people to assist you in populating the User Class Membership at your site. Depending on their level of familiarity with V*IST*A, you may even want to give them access to the USR LIST MEMBERSHIP BY CLASS option, along with appropriate training as to its use.

> Persons wearing several different hats can have concurrent membership in more than one User Class. For example, Mr. Smith might be a dietitian also working toward a nursing degree. He can be entered as a member in two User Classes, once as a Dietitian and once as a Student Nurse.

### User Class Definition Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Steps to Use Option:*

> 1. Select the option *User Class Definition* from the User Class Management menu.

> 2. Select the user class status— active, inactive, or both.

> 3. Select the starting and ending classes you want displayed.

> Select User Class Status: ACTIVE// ?

> Active All User Classes

> Inactive

> Select User Class Status: ACTIVE// \<Enter\>

> Start With Class: FIRST//\<Enter\>

> Go To Class: LAST// \<Enter\>

> Searching for the User Classes....

> 4. The User Classes within the parameters you selected are displayed.

> <u>User Classes Mar 04, 1997 08:49:29 Page: 1 of 39</u>

> ACTIVE USER CLASSES 578 Classes

> <u>Class Name Abbrev</u>

1.  ADP Coordinator ADPAC Active
2.  Acting Assistant Director AAD Active
3.  Acting Chief AC Active
4.  Acting Director AD Active
5.  Addiction Medicine ADDICT Active
6.  Adolescent Medicine Internist ADOLMD Active
7.  Allergist ALLRG Active
8.  \+ Allergy & Immunology ADR Active
9.  Allergy & Immunology: Clinical & Laboratory ALLCL Active
10. Ancillary Testing AT Active
11. \+ Anesthesiologist ANES Active
12. Anesthesiologist - Critical Care ANESCC Active
13. Anesthesiologist - Pain Management ANESPM Active
14. Applications Coordinator ADPAC Active
15. Assistant Chief AC Active 16. Assistant Chief Of Staff

> + + Next Screen - Prev Screen ?? More Actions

> Find Expand/Collapse Tree Change View

> Create a Class List Members Quit

> Edit User Class

> Select Action: Next Screen//

> *User Class Definition, cont’d*

> 5. To see subclasses of the classes shown on this screen, enter a class name at the prompt Start with Class: FIRST//. Then after the screen displays the class name, choose the action Expand/Collapse Tree (EX).

> User Class Definition

> Select User Class Management Option: 1 User Class Definition

> Select User Class Status: ACTIVE// \<Enter\>

> Start With Class: FIRST// provider

> Go To Class: LAST// prov

> Searching for the User Classes....

> <u>User Classes Feb 04, 1997 17:26:02 Page: 1 of 1</u>

> ACTIVE USER CLASSES 1 Classes

> <u>Class Name Abbrev</u>

> 1 Provider ... PROV Active

> + Next Screen - Prev Screen ?? More Actions

> Find Expand/Collapse Tree Change View

> Create a Class List Members Quit

> Edit User Class

> Select Action: Quit// EX

> Expanding User Class Hierarchy.........................

> 6. The screen expands to show the subclasses.

> <u>User Classes Feb 04, 1997 17:26:02 Page: 1 of 6</u>

> ACTIVE USER CLASSES 31 Classes

> <u>+ Class Name Abbrev</u>

> 31 Provider PROV Active

> \|-Nurse

> \| \|-Nurse Anesthetist

> \| \|-Nurse Clinical Specialist

> \| \|-Nurse Epidemiologist

> \| \|-Nurse Practitioner

> \| \|-Nursing Continuing Care

> \| \|-Nursing Supervisor

> \| \|-Head Nurse

> \| \|-Research Nurse

> \| \|\_Nurse - Licensed Practical

> \|-Physician Assistant

> + + Next Screen - Prev Screen ?? More Actions

> Find Expand/Collapse Tree Change View

> Create a Class List Members Quit

> Edit User Class

> Select Action: Next Screen// ???

> Actions

> FIND

> Allows users to search list of USER CLASSES, MEMBERS, or BUSINESS

> RULES for a text string (word or partial word) from current position to the end

> of the list. Upon reaching the end of the last page of the list, the user

> will be asked whether to continue the search from the beginning of the

> list through the origin of the search.

> CREATE A CLASS

> Lets authorized users create new user classes.

> EDIT USER CLASS

> Allows authorized users to edit selected reports online. When electronic

> signature is enabled, physicians will be prompted for their signatures upon

> exit, thereby allowing doctors to review, edit and sign as a one-step

> process.

> EXPAND/COLLAPSE TREE

> Allows you to select a user class and see its subclasses and members;. You can collapse an expanded tree to just show the user class name.

> LIST MEMBERS

> Allows you to select a user class and then see all the members of that class.

> CHANGE VIEW

> Allows users to modify the list of reports by signature status, review

> screen and dictation date range without exiting the review screen.

> QUIT

> Allows user to quit the current menu level.

> The following actions are also available:

> \+ Next screen UP Up a Line GO Go to Page

> \- Previous Screen DN Down a Line RD Re Display Screen

> FS First Screen \< Shift View to Left PL Print List

> LS Last Screen \> Shift View to Right ADPL Auto Display(On/Off)

> 7. Select the action Create a Class.

> 8. Enter a new user class name.

> Select USR CLASS NAME: Clinical Manager

> Are you adding 'Clinical Manager' as a new USR CLASS (the 569th)? y (Yes)

> Rebuilding main class list........................................

### |       |                                 |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-------|---------------------------------|
| 4 | Add members to user classes |

### ### ### List Membership by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this option, you select a user and the program shows you what classes the user belongs to. You can then review, edit, or remove individual members of user classes, or add new members.

> Select User Class Management Option: 2 List Membership by User

> Select USER: ?

> Answer with NEW PERSON NAME, or INITIAL, or SSN, or NICKNAME, or DEA#, or VA#

> Do you want the entire 109-Entry NEW PERSON List? n (No)

> Select USER: Russ,Joe E. JER

> Searching for the User Classes.

> <u>Current User Classes Jan 18, 1997 13:48:53 Page: 1 of 1</u>

> Joe E. Russ 1 Class

> <u>User Class Effective Expires</u>

> 1 Staff Physician

> + Next Screen - Prev Screen ?? More Actions

> Add Remove

> Edit Change View

> Select Action: Quit//

### > NOTE: Two new options were created with ASU patch 4, May 1998, to be used for viewing only: *Show Membership by User* and *Show membership by Class.*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### List Membership by Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option shows you all the current members of a User Class. It then allows review, addition, editing, and removal of individual members to and from that Class.

> Select User Class Management Option: 3 List Membership by Class

> Select CLASS: PHYSICIAN

> Searching for the User Classes.

> <u>User Class Members Jan 18, 1996 13:51:09 Page: 1 of 1</u>

> PHYSICIANs 6 Members

> <u>Member Effective Expires</u>

> 1 BXX CXXXXX 06/01/95

> 2 Mxxx X. Cxxxxx 11/02/95 01/01/99

> 3 HXXXX CXXXXX

> 4 DXXXXX HXXXX

> 5 DXXXXX PXXXX

> 6 Jxx E. Rxxx

> + Next Screen - Prev Screen ?? More Actions \>\>\>

> Add Remove Change View

> Edit Schedule Changes

> Select Action: Quit//

### Action Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                          |                                                                                                                                                                                                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action               | Description                                                                                                                                                                                                                                                                                 |
| Next Screen          | If multiple screens of information are available, this will page to the next screen.                                                                                                                                                                                                            |
| Previous Screen      | If multiple screens of information are available, and you are not on the first screen, this will allow paging back to the previous screens, one at a time.                                                                                                                                      |
| First Screen         | If multiple screens are available, this will page to the first screen.                                                                                                                                                                                                                          |
| Last Screen          | If multiple screens of information are available, this will page to the last screen.                                                                                                                                                                                                            |
| Search List          | Lets you search a list of User Classes for a text string (word or partial word) from current position to the end of the list. Upon reaching the end of the last page of the list, you are asked whether to continue the search from the beginning of the list through the origin of the search. |
| Create A Class       | Lets authorized users create classes online.                                                                                                                                                                                                                                                    |
| Edit User Class      | Lets authorized users edit selected classes online.                                                                                                                                                                                                                                             |
| Expand/Collapse Tree | Lets you see subclasses of a class, or go back to the class level if you’re in a subclass.                                                                                                                                                                                                      |
| Change View          | Lets you modify the list of reports by signature status, review screen and dictation date range without exiting the review screen.                                                                                                                                                              |
| Quit                 | Lets you quit the current menu level.                                                                                                                                                                                                                                                           |

### Example: Assigning Medical Record Technicians and Chief, HIMS to user classes.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: These titles may vary from site-to-site. Check to see which titles correspond to MRT and HIMS at your site (e.g., HIMS=MIS).

1.  To identify the users who should be allocated to the CHIEF, HIMS and MEDICAL RECORD TECHNICIAN classes, get a list of MRTS and transcriptionists from the HIMS office.

> 2. Start assigning members to classes through the *List Membership by Class* option on the User Class Management Menu, as shown in the example below.

> Select TIU Maintenance Menu Option: 3 User Class Management

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> Select User Class Management Option: 3 List Membership by Class

> Select CLASS: MRT MEDICAL RECORDS TECHNICIAN

> Searching for the User Classes.

> <u>User Class Members Jun 14, 1997 14:21:31 Page: 1 of 1</u>

> MEDICAL RECORDS TECHNICIANs 0 Members <u>Member Effective Expires</u>

> No MEDICAL RECORDS TECHNICIANs found

> + Next Screen - Prev Screen ?? More Actions \>\>\>

> Add Remove Change View

> Edit Schedule Changes Quit\_\[JSelect Action: Quit// AD Add

> Select MEMBER: DENINGER,JOY C. DCJ 274 MEDICAL RECORD TECHNICIAN

> MEMBER: DENINGER,JOY C.// \<Enter\>

> EFFECTIVE DATE: T (JUN 14, 1997)

> EXPIRATION DATE: \<Enter\>

> Rebuilding membership list.

> <u>User Class Members Jun 14, 1996 14:21:53 Page: 1 of 1</u>

> MEDICAL RECORDS TECHNICIANs 1 Member

> <u>Member Effective Expires</u>

> JXX C. DXXXXXXX 06/14/97

> \*\* JXX X DXXXXXXX Added \*\* \>\>\>

> Jun 14, 1997 14:21:53_8

> Add Remove Change View

> Edit Schedule Changes Quit

> Select Action: Quit// A Add

> *Assigning members to User Class, cont’d*

> Select MEMBER: DXXXX, CXXXXX X. DKC 828 MEDICAL RECORD TECHNICIAN

> MEMBER: DXXXX, CXXXXX X.// \<Enter\>

> EFFECTIVE DATE: T (JUN 14, 1997)

> EXPIRATION DATE: \<Enter\>

> Rebuilding membership list.

> 3. Continue to add all the MRTs on the list.

> 4. Change your view to add the Chief of HIMS.

> <u>User Class Members Jun 14, 1997 14:24:11 Page: 1 of 1</u>

> MEDICAL RECORDS TECHNICIANs 7 Members <u>Member Effective Expires</u>

> 1 JXX X DXXXXXXX 07/14/97

> 2 XXXXXX XXXXXXXXX 07/14/97

> 3 XXXXXX XXXXXXXXX 07/14/97

> 4 XXXXXX XXXXXXXXX 07/14/97

> 5 XXXXXXXXXXXXXXX. 07/14/97

> 7 XXXXXXXXXXXXXXXX 07/14/97

> 7 CCCCCCCCCCCCCCCC 07/14/97

> \*\* ABIGALE N. QUIGLEY Added \*\* \>\>\>

> Jun 14, 1997 14:24

> Add Remove Change View

> Edit Schedule Changes Quit

> Select Action: Quit// CH Change View

> Select CLASS: CHIEF, HIMS

> Searching for the User Classes.

> <u>User Class Members Jun 14, 1997 14:24:24 Page: 1 of 1</u>

> CHIEF, MISs 0 Members

> <u>Member Effective Expires</u>

> No CHIEF, HIMS found

> + Next Screen - Prev Screen ?? More Actions \>\>\>

> Add Remove Change View

> Edit Schedule Changes Quit\_\[JSelect Action: Quit// AD Add

> Select MEMBER: XXXXXXXXXXXXXXXXXX. SPL 364 CHIEF MIS

> MEMBER: XXXXXXXXXXXXXXX.// \<Enter\>

> EFFECTIVE DATE: T (JUN 14, 1997)

> EXPIRATION DATE:

> Rebuilding membership list.

# Chapter 4: Adding, Editing, and Managing Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an UNSIGNED PROGRESS NOTE may be EDITED by a PROVIDER who is also the EXPECTED SIGNER of the note, etc.).

> A set of Business Rules is exported with ASU. Sites can modify or add to these rules, to meet their own local needs. Examples on the next few pages demonstrate basic use of the two options, *Edit Business Rules* and *Manage Business Rules.* The second option is also known as the ASU Rule Browser, as it lets you look at all of the defined rules by several categories: Document, User Class, and User Role. You can then add, edit, or delete rules, if you are authorized.

### Edit Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lets you enter or edit Business Rules authorizing specific users or groups of users to perform specified actions on documents in particular statuses (e.g, an *unsigned progress note* may be *edited* by a *provider* who is also the *expected signer* of the note).

> NOTE: Enter two question marks (as shown in the examples) to get help on prompts.

> Example 1: Editing a business rule for a cosigner

> Select User Class Management Option: EDIT Business Rules

> Please edit a Business Rule:

> Select DOCUMENT: RADIOLOGY

> 1 RADIOLOGY IMPRESSION COMPONENT

> 2 RADIOLOGY NOTE DOCUMENT CLASS

> 3 RADIOLOGY NURSING NOTE TITLE

> 4 RADIOLOGY REPORT TITLE

> 5 RADIOLOGY REPORTS CLASS

> TYPE '^' TO STOP, OR

> CHOOSE 1-5: 2

> Are you adding 'RADIOLOGY NOTE' as

> a new USR AUTHORIZATION/SUBSCRIPTION (the 82ND)? Y (Yes)

> DOCUMENT TYPE: RADIOLOGY NOTE// \<Enter\>

> STATUS: ??

> Choose from:

> AMENDED

> COMPLETED

> DELETED

> INCOMPLETE

> LIVE

> PURGED

> RETIRED

> TEST

> UNCOSIGNED

> UNDICTATED

> UNRELEASED

> UNSIGNED

> UNTRANSCRIBED

> UNVERIFIED

> STATUS: UNCOSIGNED

> ACTION: ??

> This is the action to be permitted for a given document type and status.

> Choose from:

> AMENDMENT

> CHANGE TITLE

> COPY RECORD

> COSIGNATURE

> DELETE RECORD

> DICTATION

> EDIT RECORD

> ENTRY

> IDENTIFY SIGNERS

> MAKE ADDENDUM

> PRINT RECORD

> *Edit Business Rules cont’d*

> REASSIGN

> RELEASE FROM TRANSCRIPTION

> SEND BACK

> SIGNATURE

> UNCOSIGNED NOTIFICATION

> UNSIGNED NOTIFICATION

> VERIFICATION

> VIEW

> ACTION: COSIGNATURE

> USER CLASS: STAFF RADIOLOGIST

> AND FLAG: ??

> This field allows the ADPAC to indicate whether the conditions specified by User Class and User Role should be logically "AND'ed," or logically "OR'ed," as they will be unless otherwise specified. i.e., if you want to specify that an unsigned discharge summary may be signed by a user, where:

> User Class = Provider AND User Role = Author,

> then you'll want to set this field to AND.

> Choose from:

> & AND

> ! OR

> AND FLAG: & AND

> USER ROLE: ??

> This identifies the role of the user with respect to the document

> in question (e.g., Author/Dictator, Expected Signer, Expected

> Cosigner, Attending Physician, etc.).

> Choose from:

> ADDITIONAL SIGNER

> ATTENDING PHYSICIAN

> AUTHOR/DICTATOR

> EXPECTED COSIGNER

> EXPECTED SIGNER

> SURROGATE

> TRANSCRIBER

> USER ROLE: E

> 1 EXPECTED COSIGNER

> 2 EXPECTED SIGNER

> CHOOSE 1-2: 1

> DESCRIPTION:

> 1\>\<Enter\>

> You defined the following rule:

> An UNCOSIGNED RADIOLOGY NOTE may be COSIGNED by A STAFF RADIOLOGIST who

> is also AN EXPECTED COSIGNER

> Press RETURN to continue...\<Enter\>

#### Noteson User Class and User Role SURROGATE

> The User Class SURROGATE is honored by ASU Business Rules. For example, rule

> An UNSIGNED (CLASS) PROGRESS NOTE may BE SIGNED by a SURROGATE

> authorizes any member of the SURROGATE User Class to sign an unsigned Progress Note.

> However, *UserRole* SURROGATE has never been implemented in ASU and is not honored by rules with one exception.

> If user B is designated as a Surrogate for user A *and*  there is a rule authorizing *User Role* Surrogate to take action on a document *and* User A is identified as an Additional Signer for that document, then User B may take that action.

> For example,

> The business rule “A COMPLETED (CLASS) PROGRESS NOTE may BE SIGNED by a SURROGATE ROLE” authorizes User B to sign a COMPLETED Progress Note if User A has been identified as an Additional Signer for that document.

> Note: Alerts for additional signers and surrogates of additional signers are sent only after the document has been signed.

> Note: A user can designate their own surrogate when processing alerts. As an alternative, an ADPAC may designate a surrogate for a user using option XQALERT SURROGATE SET/REMOVE \[XQALERT SURROGATE SET/REMOVE\]. 

> Example 2:Creating a rule for who may Copy or Send Back a Clinical Document.

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> 6 Initialize Membership of Provider Class

> Select User Class Management Option: EDit Business Rules

> Please edit a Business Rule:

> Select DOCUMENT DEFINITION: "CLINICAL DOCUMENTS" CLASS

> Are you adding 'CLINICAL DOCUMENTS' as

> a new USR AUTHORIZATION/SUBSCRIPTION (the 50TH)? Y (Yes)

> DOCUMENT DEFINITION: CLINICAL DOCUMENTS// \<Enter\>

> STATUS: UNSIGNED

> ACTION: COPY RECORD

> USER CLASS: \<Enter\>

> AND FLAG: \<Enter\>

> USER ROLE: AUTHOR/DICTATOR

> DESCRIPTION:

> No existing text

> Edit? NO// \<Enter\>

> You defined the following rule:

> An UNSIGNED CLINICAL DOCUMENT may be COPIED by AN AUTHOR/DICTATOR

> Press RETURN to continue... \<Enter\>

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> Select User Class Management Option \[SPACE\]\<Enter\> Edit Business Rules

> Please edit a Business Rule:

> Select DOCUMENT DEFINITION: "CLINICAL DOCUMENTS" CLASS

> Are you adding 'CLINICAL DOCUMENTS' as

> a new USR AUTHORIZATION/SUBSCRIPTION (the 51ST)? Y (Yes)

> DOCUMENT DEFINITION: CLINICAL DOCUMENTS// \<Enter\>

> STATUS: COMPLETED

> ACTION: COPY RECORD

> USER CLASS: USER

> AND FLAG: ??

> This field allows the ADPAC to indicate whether the conditions specified by User Class and User Role should be logically "AND'ed," or logically "OR'ed," as they will be unless otherwise specified. i.e., if you want to specify that an unsigned discharge summary may be signed by a user, where:

> User Class = Provider AND User Role = Author,

> *Edit Business Rules cont’d*

> then you'll want to set this field to AND.

> Choose from:

> & AND

> ! OR

> AND FLAG: \<Enter\>

> USER ROLE: \<Enter\>

> DESCRIPTION:

> No existing text

> Edit? NO// \<Enter\>

> You defined the following rule:

> A COMPLETED CLINICAL DOCUMENT may be COPIED by A USER

> Press RETURN to continue...\<Enter\>

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> You have PENDING ALERTS

> Enter "VA VIEW ALERTS to review alerts

> Select User Class Management Option: Edit Business Rules

> Please edit a Business Rule:

> Select DOCUMENT DEFINITION: "CLINICAL DOCUMENTS" CLASS

> Are you adding 'CLINICAL DOCUMENTS' as

> a new USR AUTHORIZATION/SUBSCRIPTION (the 52ND)? Y (Yes)

> DOCUMENT DEFINITION: CLINICAL DOCUMENTS// \<Enter\>

> STATUS: UNSIGNED

> ACTION: SEND BACK

> USER CLASS: MIS

> 1 MIS FILE CLERK

> 2 MIS MEDICAL INFORMATION SECTION

> CHOOSE 1-2: 2 MEDICAL INFORMATION SECTION

> AND FLAG: \<Enter\>

> USER ROLE: \<Enter\>

> DESCRIPTION:

> No existing text

> Edit? NO// \<Enter\>

> You defined the following rule:

> An UNSIGNED CLINICAL DOCUMENT may be SENT BACK by A MEDICAL INFORMATION SECTION

> Press RETURN to continue...\<Enter\>

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> Select User Class Management Option: \[SPACE\]\<Enter\> Edit Business Rules

> *  
> Edit Business Rules cont’d*

> Please edit a Business Rule:

> Select DOCUMENT DEFINITION: "CLINICAL DOCUMENTS" CLASS

> Are you adding 'CLINICAL DOCUMENTS' as

> a new USR AUTHORIZATION/SUBSCRIPTION (the 53RD)? Y (Yes)

> DOCUMENT DEFINITION: CLINICAL DOCUMENTS// \<Enter\>

> STATUS: UNVERIFIED

> ACTION: \[SPACE\]\<Enter\> SEND BACK

> USER CLASS: \<SPACE\>\<Enter\> MEDICAL INFORMATION SECTION

> AND FLAG: \<Enter\>

> USER ROLE: \<Enter\>

> DESCRIPTION:

> No existing text

> Edit? NO// \<Enter\>

> You defined the following rule:

> An UNVERIFIED CLINICAL DOCUMENT may be SENT BACK by A MEDICAL INFORMATION SECTION

> Press RETURN to continue... \<Enter\>

> --- User Class Management Menu ---

> 1 User Class Definition

> 2 List Membership by User

> 3 List Membership by Class

> 4 Edit Business Rules

> 5 Manage Business Rules

> You have PENDING ALERTS

> Enter "VA VIEW ALERTS to review alerts

> Select User Class Management Option: \<Enter\>

> Do you really want to halt? YES// \<Enter\>

### Example 3: Entering user classes that require cosignature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you want to specify user classes who must have co-signatures for specified documents, use the *Document Parameter Edit* on the TIU Parameters Menu on the IRM Maintenance Menu.

> Select TIU Parameters Menu Option: 3 Document Parameter Edit

> First edit Institution-wide parameters:

> Select DOCUMENT: PROGRESS NOTES CLASS

> ...OK? Yes// \<Enter\> (Yes)

> REQUIRE RELEASE: NO// \<Enter\>

> REQUIRE MAS VERIFICATION: NO// \<Enter\>

> REQUIRE AUTHOR TO SIGN: YES// \<Enter\>

> ROUTINE PRINT EVENT(S): \<Enter\>

> STAT PRINT EVENT(S): \<Enter\>

> MANUAL PRINT AFTER ENTRY: YES// \<Enter\>

> ALLOW CHART PRINT OUTSIDE MAS: YES// \<Enter\>

> ALLOW \>1 RECORDS PER VISIT: YES// \<Enter\>

> ENABLE IRT INTERFACE:

> If document is to be uploaded, specify Filing Alert Recipients:

> Select FILING ERROR ALERT RECIPIENTS: RUSS,JOE

> Now enter the USER CLASSES for which cosignature will be required:

> Select USERS REQUIRING COSIGNATURE: INTERN// student

> ...OK? Yes// \<Enter\> (Yes)

> USERS REQUIRING COSIGNATURE: STUDENT//\<Enter\>

> Select USERS REQUIRING COSIGNATURE: \<Enter\>

> Now enter the DIVISIONAL parameters:

> Select DIVISION: SALT LAKE CITY 660

> Are you adding 'SALT LAKE CITY' as a new DIVISION (the 1ST for this TIU DOCUMENT PARAMETERS)? y

> (Yes)

> CHART COPY PRINTER: PRINTER

> STAT CHART COPY PRINTER: \<Enter\>

> Select DIVISION: \<Enter\>

> Press RETURN to continue... ^

> Manage Business Rules

> This option (also known as the ASU Rule Browser) lets you display all the Business Rules for a given Document, User Class, or User Role. You can then add, edit, or delete them, as appropriate.

> NOTE: Enter two question marks (as shown in the examples) to get help on prompts.

> Example 1: Adding a new Business Rule

1.  In this example we’ll create a new Business Rule: “An unsigned clinical document may be sent back by a Medical Record Technician.”

> Select User Class Management Option: 5 Manage Business Rules

> Select SEARCH CATEGORY: DOCUMENT// ??

> Choose from:

> DOCUMENT

> USER CLASS

> USER ROLE

> Select SEARCH CATEGORY: DOCUMENT// \<Enter\>

> Select DOCUMENT DEFINITION: ??

> Choose from:

> CLINICAL DOCUMENTS CLASS

> DISCHARGE SUMMARY CLASS

> Select DOCUMENT DEFINITION: Clinical (CLINICAL DOCUMENTS)

2.  After specifying the search category and document type, all rules for that type are displayed.

> <u>ASU Rule Browser Jan 09, 1997 15:12:34 Page: 1 of 4</u>

> List Business Rules by DOCUMENT 64 Rules

> for CLINICAL DOCUMENTS

> 1 An UNTRANSCRIBED CLINICAL DOCUMENT may be ENTERED by A USER

> 2 An UNRELEASED CLINICAL DOCUMENT may be RELEASEED by AN TRANSCRIBER

> 3 An UNSIGNED CLINICAL DOCUMENT may be EDITED by AN AUTHOR/DICTATOR

> 4 An UNSIGNED CLINICAL DOCUMENT may be EDITED by AN EXPECTED SIGNER

> 5 An UNSIGNED CLINICAL DOCUMENT may be SIGNED by AN EXPECTED SIGNER

> 6 An UNSIGNED CLINICAL DOCUMENT may be SIGNED by A PROVIDER who is also

> AN EXPECTED COSIGNER

> 7 A COMPLETED CLINICAL DOCUMENT may be VIEWED by A USER

> 8 An UNRELEASED CLINICAL DOCUMENT may be EDITED by A TRANSCRIBER

> 9 An UNRELEASED CLINICAL DOCUMENT may be EDITED by A TRANSCRIPTIONIST

> 10 An UNCOSIGNED CLINICAL DOCUMENT may be COSIGNED by AN EXPECTED

> COSIGNER

> 11 An UNSIGNED CLINICAL DOCUMENT may be SIGNED by A STUDENT who is also

> AN EXPECTED SIGNER

> 12 An UNSIGNED CLINICAL DOCUMENT may be EDITED by AN EXPECTED COSIGNER

> + + Next Screen - Prev Screen ?? More Actions

> Find Edit Rule Change View

> Add Rule Delete Rule Quit

> Select Action: Next Screen// a Add Rule

> *Manage Business Rules cont’d*

> Please Enter a New Business Rule:

> Select DOCUMENT DEFINITION: ?

> 1 CLINICAL DOCUMENTS CLASS

> 2 CLINICAL WARNING TITLE

> 3 CLINICAL WARNING DOCUMENT CLASS

> 4 CRISIS NOTE TITLE

> 5 CRISIS NOTE DOCUMENT CLASS

> TYPE '^' TO STOP, OR

> CHOOSE 1-5: 1

> DOCUMENT DEFINITION: CLINICAL DOCUMENTS// \<Enter\>

> STATUS: ?

> Enter the status of document for which the event is authorized.

> Answer with USR RECORD STATUS NAME, or SEQUENCE

> Do you want the entire USR RECORD STATUS List? y (Yes)

> Choose from:

> AMENDED

> COMPLETED

> DELETED

> PURGED

> UNCOSIGNED

> UNDICTATED

> UNRELEASED

> UNSIGNED

> UNTRANSCRIBED

> UNVERIFIED

> STATUS: UNSIGNED

> ACTION: ??

> This is the action to be permitted for a given document type and status.

> Choose from:

> AMENDMENT

> COPY RECORD

> COSIGNATURE

> DELETE RECORD

> DESIGNATE OPTIONAL COSIGNER

> DICTATION

> EDIT DOCUMENT DEFINITION

> EDIT RECORD

> ENTRY

> INCLUDE IN UNSIGNED LIST

> MAKE ADDENDUM

> PRINT RECORD

> RELEASE FROM TRANSCRIPTION

> SEND BACK

> SIGNATURE

> VERIFICATION

> VIEW

> ACTION: SEND BACK

> USER CLASS: MEDICAL RECORD TECHNICIAN

> AND FLAG: ??

> This field allows the ADPAC to indicate whether the conditions specified by User Class and User Role should be logically "AND'ed," or logically "OR'ed," as they will be unless otherwise specified. i.e., if you want to specify that an unsigned discharge summary may be signed by a user, where:

> User Class = Provider AND User Role = Author,

> *Manage Business Rules option cont’d*

> then you'll want to set this field to AND.

> Choose from:

> & AND

> ! OR

> AND FLAG: & AND

> USER ROLE: ??

> This identifies the role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner,

> Attending Physician, etc.).

> Choose from:

> ADDITIONAL SIGNER

> ATTENDING PHYSICIAN

> AUTHOR/DICTATOR

> EXPECTED COSIGNER

> EXPECTED SIGNER

> SURROGATE

> TRANSCRIBER

> USER ROLE: \<Enter\>

> DESCRIPTION:

> 1\> \<Enter\>

> <u>ASU Rule Browser Jan 09, 1997 17:35:52 Page: 1 of 1</u>

> List Business Rules by DOCUMENT 2 Rules

> for CLINICAL DOCUMENTS

> 1 An UNTRANSCRIBED CLINICAL DOCUMENT may be ENTERED by A NURSE

> 2 An UNRELEASED CLINICAL DOCUMENT may be SENT BACK by a MEDICAL

> RECORDS TECHNICIAN

> \*\* Item 2 Added \*\*

> Find Edit Rule Change View

> Add Rule Delete Rule Quit

> Select Action: Quit//

> Example 2: Deleting and Editing Business Rules

> In this example, we will be viewing business rules by User Class with Nurse as the User Class.

1.  Choose *Manage Business Rules* from the User Class Management menu. Then select User Class for the search category and nurse for the user class.

> Select User Class Management Option: 5 Manage Business Rules

> Select SEARCH CATEGORY: DOCUMENT// USER CLASS

> Select USER CLASS: NURSE

> 1 NURSE

> 2 NURSE - STUDENT

> 3 NURSE ANESTHETIST

> 4 NURSE CLINICAL SPECIALIST

> 5 NURSE EPIDEMIOLOGIST

> TYPE '^' TO STOP, OR

> CHOOSE 1-5:1

> 2. The current rules for the Nurse User Class are displayed.

> <u>ASU Rule Browser Jan 14, 1997 13:46:48 Page: 1 of 1</u>

> List Business Rules by USER CLASS 2 Rules

> for NURSE

> 1 An UNTRANSCRIBED NURSE'S NOTE may be ENTERED by A NURSE

> 2 An AMENDED NURSE'S NOTE may be EDITED by A NURSE OR An

> AUTHOR/DICTATOR

> + Next Screen - Prev Screen ?? More Actions

> Find Edit Rule Change View

> Add Rule Delete Rule Quit

> Select Action: Quit// D Delete Rule

3.  Select the number of the Business Rule you want to delete.

> Select Business Rule(s): (1-2): 2

> Deleting \#2

> Removing the rule:

> An AMENDED NURSE'S NOTE may be EDITED by A NURSE OR An AUTHOR/DICTATOR

> Are you SURE? NO// \<Enter\>

> Business Rule NOT Removed.

4.  After first deciding to delete the rule, you change your mind and decide to edit it instead. Example dialogue for deleting a rule follows on the next page.

> *Deleting and Editing Business Rules cont’d*

> 5. Select the action Edit Rule.

> <u>ASU Rule Browser Jan 14, 1997 13:47:33 Page:1 of 1</u>

> List Business Rules by USER CLASS 2 Rules

> for NURSE

> 1 An UNTRANSCRIBED NURSE'S NOTE may be ENTERED by A NURSE

> 2 An AMENDED NURSE'S NOTE may be EDITED by A NURSE OR An

> AUTHOR/DICTATOR

> \*\* Nothing removed \*\*

> Add Rule Delete Rule Quit

> Edit Rule Change View

> Select Action: Quit// E Edit Rule

6.  Select the rule (#2) and then respond to each of the prompts by entering a new rule component or hitting the enter key to accept the current component.

> Select Business Rule(s): (1-2): 2

> Editing \#2

> DOCUMENT TYPE: NURSE'S NOTE// \<Enter\>

> STATUS: AMENDED// \<Enter\>

> ACTION: EDIT RECORD// \<Enter\>

> USER CLASS: NURSE// NURSING SUPERVISOR

> AND FLAG: OR// \<Enter\>

> USER ROLE: AUTHOR/DICTATOR// \<Enter\>

> DESCRIPTION:

> 1\> \<Enter\>

> Refreshing the list.

7.  The screen is redisplayed with current rules for this User Class.
8.  Note that the edited rule isn’t displayed. That’s because the User Class was changed; so you need to Change View to the new User Class, Nursing Supervisor.

> <u>ASU Rule Browser Jan 14, 1997 13:49:50 Page:1 of 1</u>

> List Business Rules by USER CLASS 1 Rule

> for NURSE

> 1 An UNTRANSCRIBED NURSE'S NOTE may be ENTERED by A NURSE

> \*\* Item 2 Edited \*\*

> Find Edit Rule Change View

> Add Rule Delete Rule Quit

> Select Action: Quit// C Change View

> *  
> Deleting and Editing Business Rules cont’d*

9.  After you respond to prompts for User Class and enter Nursing Supervisor, the screen is redisplayed with current rules for this User Class.

> Select SEARCH CATEGORY: DOCUMENT// USER CLASS

> Select USER CLASS: NURSING SUPERVISOR

> <u>ASU Rule Browser Jan 14, 1997 14:16:20 Page: 1 of 1</u>

> List Business Rules by USER CLASS 1 Rule

> for NURSING SUPERVISOR

> 1 An AMENDED NURSE'S NOTE may be EDITED by A NURSING SUPERVISOR OR An AUTHOR/DICTATOR

> + Next Screen - Prev Screen ?? More Actions

> Find Edit Rule Change View

> Add Rule Delete Rule Quit

> Select Action: Quit//

### ### > NOTE: Your site might redefine the User Classes so that Nursing Supervisor is under the User Class Nurse. In this case, steps 8 and 9 in the above example wouldn’t be necessary.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Status List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This list of statuses may be added to as additional document types are incorporated.

> **NOTE:** Internal File Entry Numbers (IEN) in the USR Status File (#8930.6) are standardized and *must* not be changed.

|                   |                                                                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status        | Description                                                                                                                                                                                     |
| Amended       | The document has been completed and a privacy act issue has required its amendment.                                                                                                                 |
| Completed     | The document has acquired all necessary signatures and is legally authenticated.                                                                                                                    |
| Deleted       | The document has been deleted but the audit trail is retained.                                                                                                                                      |
| Retracted     | Used instead of Deleted after the document has been signed. If an error is discovered after signature, then the document is made invisible for most users, but retained as part of the audit trail. |
| Uncosigned    | The document is complete, with the exception of cosignature by the attending physician.                                                                                                             |
| Undicatated   | The document is required and a record has been created in anticipation of dictation and transcription.                                                                                              |
| Unreleased    | The document is in the process of being entered into the system, but hasn’t been released by the originator (i.e., the person who entered the text online). See the TUI Document Parameters.        |
| Unsigned      | The document is online in a draft state, but the author's signature hasn’t yet been obtained.                                                                                                       |
| Untranscribed | This status is used for business rules permitting entry of not-yet-existing documents into the file.                                                                                                |
| Unverified    | The document has been released or uploaded, but an intervening verification step must be completed before the document is available for signature. See the TUI Document and Upload Parameters.      |

### ### Action List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This list of actions may be added to as additional document types and/or statuses are incorporated.

> **NOTE:** File entry numbers in the USR ACTION file (#8930.8) are standard and must not be changed.

|              |                   |                                                                                                                                                                                              |
|--------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File IEN | Action        | Comments                                                                                                                                                                                 |
| 18           | AMENDMENT         | Involves the Privacy Act Amendment of a document by authorized individuals *after* electronic Signature. (Note that the old unamended document is kept in a retracted status.)               |
| 25           | ATTACH ID ENTRY   | Rule applies to interdisciplinary PARENT notes and permits notes of this title to have child notes attached.                                                                                 |
| 24           | ATTACH TO ID NOTE | Rule applies to individual ID CHILD entries and permits notes of this title to be attached (to a parent note).                                                                               |
| 22           | CHANGE TITLE      | The title may be changed during the life of the document. This most often happens when the medical center is reorganizing their title structure.                                             |
| 16           | COPY RECORD       | Allows an authorized user to copy a document from one patient or encounter to another.                                                                                                       |
| 5            | COSIGNATURE       | This action occurs when a second-line signature is obtained for a document.                                                                                                                  |
| 15           | DELETE RECORD     | The document is deleted. This only applies to unsigned documents. If the document has been signed, it is retracted and remains in the file as part of the audit trail.                       |
| 9            | EDIT RECORD       | Users authorized to perform this action may edit the text of the document. The text of completed documents may not be edited. Edit attempts result in scrambled electronic signature blocks. |
| 27           | EDIT COSIGNER     | Permits editing the Expected Cosigner of UNCOSIGNED and UNSIGNED documents using a new TIU VISTA List Manager action which does not include access to the text body.                         |
| 2            | ENTRY             | Used to permit the creation of new documents in the TIU Document File (#8925).                                                                                                               |

|              |                   |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------|-------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File IEN |                   | Action | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 20           | IDENTIFY SIGNERS  |            | This action allows the identification of users whose signature is expected, but *not required*. This action causes VistA to send an alert to the selected provider(s). The recipient of the alert for an additional signature may add an addendum or sign the document, but may not generally edit the document itself. The signature in this case does not complete the document, but simply indicates that the document has been seen.                                           |
| 26           | LINK TO FLAG      |            | Users authorized to create NEW PRF documents are automatically authorized (in fact, REQUIRED) to link the new documents when creating them. Explicit authorization for (re)-linking a PRF document to a flag is required only for documents which already exist. Such documents may have been created before PRF Phase II introduced links and have NO links, or they may require re-linking to the correct Assignment History Action for the correct patient and flag assignment. |
| 23           | LINK WITH REQUEST |            | Involves the linking (or re-linking) of a result with a request in another application (e.g., a PULMONARY CONSULT with its corresponding request).                                                                                                                                                                                                                                                                                                                                 |
| 19           | MAKE ADDENDUM     |            | Addenda may be added to documents for the purposes of clarification or augmenting. Addenda may be thought of as extensions of their parent documents, and inherit their properties from them (i.e., an addendum to a discharge summary is treated like a discharge summary, while an addendum to a progress note is treated like a progress note, etc.).                                                                                                                           |
| 14           | PRINT RECORD      |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 21           | REASSIGN          |            | Reassignment of records involves the correction of Patient, Visit, or Signatory information, and may typically be accomplished by the author or MIS prior to signature, or by the CHIEF, MIS following signature. (Note that the old unchanged document is kept in a retracted status.)                                                                                                                                                                                            |

|              |                            |                                                                                                                                                                                                    |
|--------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File IEN | Action                 | Comments                                                                                                                                                                                       |
| 8            | RELEASE FROM TRANSCRIPTION | The transcriptionist is satisfied with the transcription and releases the document for signature. See the TIU Document Parameters.                                                                 |
| 17           | SEND BACK                  | Involves sending back a document to transcription for correction (and possibly redictation). It removes documents which require release from view, except by the originator or a transcriptionist. |
| 4            | SIGNATURE                  | This applies to a first-time signature or and additional signature depending on the document status                                                                                                |
| 3            | VERIFICATION               | See TIU Document and Upload Parameters.                                                                                                                                                            |
| 7            | VIEW                       | This action permits users to view the text of the document.                                                                                                                                        |

# Helpful Hints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Shortcut

> Type the action abbreviation, then the number of the user class on the list (Example: ED=1 will process entry 1 for Edit) or vice versa. Type the item \# followed by an equals sign (=) and the Action or its abbreviation ("1=L" will produce a List of members of the ADP Coordinator user class).

### Troubleshooting & Helpful Hints for ASU Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If a particular person should be able to do something governed by a particular Business Rule, but can’t, check the following:
- Make sure he/she is in the referenced User Class.
- Check the business rule for the proper status.
- Check that the document to be acted on is the one referenced by the rule or is a descendant of the document referenced by the rule. If the rule involves a User Role, make sure the person actually plays that role for the document.
- Check to see if the rule has been overridden. If the same rule (same action and same status) is defined for a lower-level document, the lower level rule *overrides* the rule at the higher level. For example, suppose you are checking the rule, “An UNDICATATED PROGRESS NOTE can be ENTERED by a PROVIDER.” You wonder why Dr. Jones, a Provider, can’t enter a Nurse Practitioner Note, which is a descendant of Progress Notes. If there is a rule, “An UNDICTATED NURSE PRACTITIONER NOTE can be ENTERED by a NURSE PRACTITIONER,” then the rule you are checking has been overridden for Undictated Nurse Practitioner Notes. Any User Classes who can enter Nurse Practitioner Notes must have their own explicit Business Rule at the Nurse Practitioner Note level. The easiest way to check for overriding rules is to do a FileMan print by the same Action and the same Status.
1.  If a particular person should NOT be able to do something, but CAN, check the following:
- That the person doesn’t have inappropriate menus.
- That he/she is not a member of inappropriate User Classes.
- That the document involved is in the correct place in the document definition hierarchy.
- Check any business rules for the given action, status, user role, and document or ancestors of the document.
- Check to see if they have somehow been given an inappropriate role in relation to the document. For example, the person might mistakenly have been made the author when he/she isn’t the author.

> Q: When I edited a rule, the edited rule wasn’t displayed, even though it said “Rule \#2 edited” in the black bar.

> A: In changing the rule, you may have changed the User Class. Look at the top of the screen to see if you are in a different User Class than the one you started with. If so, you need to Change View to the new User Class.

### More Information about ASU and User Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Relationship between User Class file and Person Class file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Although there are a number of superficial similarities between the User Class File (#8930) and Kernel’s Person Class File (#8932.1), the files are structurally dissimilar, designed to serve completely different applications. In fact, the roles of the two files are analogous to those of the LABORATORY TEST File (#60) and the WKLD CODE File (#64).

> The *User Class File* provides for the definition of a hierarchy of User Classes, flexible enough to describe the organizational structure of the local facility. To that end, it is designed to be both *general* and *extensible*, much in the same way that file 60 can be viewed as a “model” of the local laboratory’s “catalogue” of tests and panels.

> The *Person Class File*, in contrast, is designed to accommodate the HCFA National Provider System Taxonomy of Professionals/Occupations, which is an emerging industry standard for identifying the Occupations, Specialties, and Subspecialties to which Health Care Providers belong. This file is standardized across VHA, and cannot be extended to accommodate differences in local organizational structure. It is very useful, however, for inter-facility data transfer, where enterprise-wide consistency is the name of the game. The same role is fulfilled, in the case of laboratory tests, by file 64. This combination of locally extensible files which help to model the differences between facilities, mapped to national “nomenclature” files which help to impose a standard reference frame, has proven to be most useful on many occasions throughout V*IST*A.

> Other Differences between User Class and Person Class

- User Class is *general*, allowing for identification of an array of non-Providers whose access to clinical applications must be accommodated and controlled (e.g., transcribers, file clerks, ward clerks, unit secretaries, hospital directors, etc.). The HCFA Taxonomy (and therefore the Person Class file) currently offers a very restricted subset of the administrative or clerical occupations required by the applications which ASU is designed to serve.
- User Class may be dynamically extended or revised to accommodate a wide variety of common organizational changes (e.g., product line reorganizations, site consolidations, etc.), with their attendant local variations.

    
  *Differences between User Class and Person Class cont’d*
- The User Class file accommodates a true “object-class” hierarchy, which allows the definition of a set of locally controlled business rules, conferring privileges which may be defined for any level in the hierarchy, and “inherited” by members of all subordinate classes. For example, one such rule states that a User may view a completed Clinical Document, where User is the “root class” of the User Class Hierarchy, and Clinical Document is the root class of TIU’s Document Definition hierarchy.

## Amount of Set-up for User Class & Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Initial Population of Basic User Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the initial implementation of TIU and ASU, it is *NOT* necessary to populate all of the exported user classes, or to allocate *every*V*IST*A user membership in *any* of the exported classes. Any users who are not allocated to a specific class will be treated as members of the root class USER. An option is provided to “seed” the PROVIDER class based on ownership of the PROVIDER Security Key.

> NOTE*:If your site has allocated the PROVIDER key to non-Providers in order to accommodate the requirements of the Ambulatory Care Data Capture package, we suggest that you review the holders of the key and de-allocate it from such users as necessary.*

> In the set-up section of this Guide, we illustrate how you might allocate members to the Medical Records Technician, Chief, MIS, and Transcriptionist classes. These are the only user classes whose membership must be allocated for basic implementation of TIU.

> Creation of Business Rules

> TIU and ASU are exported with a very general set of business rules, which should be sufficient for initial implementation. As stated earlier in this Guide, we recommend that you *keep the User Class file, TIU Document Definition Hierarchy, and Business Rule base as simple as possible* in your initial implementation. Once you have grown acquainted with the basic operation of these two complex packages, you might then begin to explore the more advanced levels of control that are possible in accordance with your site’s HIM by-laws and concerns for the trade-off between access and confidentiality. Instructions for creating Business Rules are also provided earlier in this Guide.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Action A functional process that a clinician or clerk uses in the ASU computer program; for example, “Edit.” An action is also called a protocol.
> Authorization Who is AUTHORIZED to do something (for example, sign and order).
> Business Rules Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses
> Clinician A doctor or other provider in the medical center who is authorized to provide patient care.
> Discharge Summary A formal synopsis of a patient’s medical care during a single hospitalization, including tests procedures, and conclusions. A discharge summary is prepared for all discharges and transfers from a VA medical center or domiciliary or from nursing home care. The automated Discharge Summary module of TIU provides an efficient and immediate mechanism for clinicians to capture transcribed patient discharge summaries online, where they’re available for review, signing, adding addendum.
> Document Class Classes group documents. For example, “Progress Notes” is a class with many kinds of progress notes under it. Classes may themselves be subdivided into further Classes and/or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
> Document Definition Document Definition provides the building blocks for TIU, by organizing the elements of documents in a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class.
> *Glossary, cont’d*
> Progress Notes The Progress Notes module of TIU is used by health care givers to enter and sign online patient progress notes and by transcriptionists to enter notes to be signed by caregivers at a later date. Caregivers may review progress notes online or print progress notes in chart format for filing in the patient’s record.
> Subscription A group of persons who *subscribe* to receive something; for example, an Attending physician receives a resident’s unsigned Discharge Summary on his/her list of Unsigned Discharge Summaries. (Subscription is not included in this version of ASU)
> TIU Text Integration Utilities, a V*IST*A document management application.
> User Class User Classes and sub-classes (e.g., Provider, physician, transcriptionist, Medical Record Technician, MIS Manager, Medical Student, Nurse, Resident, etc.) are defined in the User Class File (8930), which is the principal foundation for ASU. Responsibilities and privileges (for signing, cosigning, editing, etc.) are defined through this file.

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A. Exported User Classes
B. Exported Business Rules

# Appendix A: Exported User Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACTING ASSISTANT CHIEF

ACTING CHIEF

ADDICTION MEDICINE

ADJUDICATION OFFICER

ALLERGIST

ALLERGY & IMMUNOLOGY

ALLERGY & IMMUNOLOGY: CLINICAL & LABORATORY

ANCILLARY TESTING

ANESTHESIOLOGIST

ANESTHESIOLOGIST - CRITICAL CARE

ANESTHESIOLOGIST - PAIN MANAGEMENT

ASSISTANT CHIEF

ASSISTANT CHIEF OF STAFF

ASSOCIATE CHIEF OF STAFF

ATTENDING PHYSICIAN

AUDIOLOGIST

AUDIOVISUAL SPECIALIST

BODY IMAGING

CADIOLOGIST

CAST TECHNICIAN

CHAPLAIN

CHIEF

CHIEF RESIDENT

CHIEF TECHNOLOGIST

CHIEF, ANESTHESIOLOGY SERVICE

CHIEF, MEDICAL SERVICE

CHIEF, MIS

CHIEF, PSYCHIATRY SERVICE

CHIEF, RESEARCH SERVICE

CHIEF, SURGICAL SERVICE

CLINICAL CLERK

CLINICAL COORDINATOR

CLINICAL DIETITIAN

CLINICAL INTERN

CLINICAL PHARMACIST

CLINICAL SERVICE CHIEF

CLINICAL SPECIALIST

CONSULT/LIAISON

CONSULTANT

COORDINATOR, OPERATING ROOM

COORDINATOR, QM/MIS

COUNSELOR

CYTOTECHNOLOGIST

DENTAL ASSISTANT

DENTAL INTERN

DENTAL RESIDENT

DENTIST

DERMATOLOGIST

*Exported User Classes cont’d*

DERMATOLOGIST: CLINICAL & LABORATORY

DERMATOLOGY FELLOW

DERMATOPATHOLOGIST

DIABETES STUDY NURSE

DIALYSIS TECHNICIAN

DIETETIC INTERN

DIETETIC TECHNICIAN STUDENT

DIETITIAN

DIETITIAN CLINICAL SPECIALIST

DISTINGUISHED PHYSICIAN

DRG COORDINATOR

ECHO TECHNICIAN

EDUCATION STAFF SPECIALIST

ELECTRON MICROSCOPIST

EMERGENCY MEDICINE PHYSICIAN

EMERGENCY SPORTS MEDICINE

EMG TECHNICIAN

ENDOCRINOLOGIST

EPIDEMIOLOGIST

EXERCISE PHYSIOLOGIST

FAMILY GERIATRICIAN

FAMILY PRACTICE PHYSICIAN

FAMILY SPORTS MEDICINE

FEE BASIS NURSE

FELLOW

GENERAL PRACTICE PHYSICIAN

GENERIC SCREENING NURSE

GERIATRICS, GENERAL PRACTITIONER

GRADUATE NURSE TECHNICIAN

GYNECOLOGIST

HEAD NURSE

HEALTH CARE TECHNICIANS

HEMATOLOGY & ONCOLOGY

HEMODIALYSIS TECHNICIAN

HISTOPATHOLOGY TECHNICIAN

HISTOTECHNOLOGIST

HIV/AIDS COORDINATOR

HOME CARE CLINICAL COORDINATOR

HOSPITAL EPIDEMIOLOGIST

HYGIENIST

IMAGE ASSISTANT

INDUSTRIAL HYGIENIST

INFECTION CONTROL NURSE

INFECTIOUS DISEASE FELLOW

INPATIENT PSYCHOLOGIST

INTERN

INTERN PHYSICIAN

INTERN: ALLOPATHIC

*Exported User Classes cont’d*

## INTERN: OSTEOPATHIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IV PHARMACIST

IV TECHNICIAN

JUNIOR ASSISTANT RESIDENT

JUNIOR RESIDENT

KINESIOTHERAPIST

LABORATORY PATHOLOGIST

LABORATORY PROGRAM ASSISTANT

LABORATORY TECHNICIAN

LEAD PHARMACIST

MEDICAL CLERK

MEDICAL CLERK SUPERVISOR

MEDICAL DATA CLERK

MEDICAL INFORMATION SECTION

MEDICAL INTERN

MEDICAL PROGRAM ASSISTANT

MEDICAL RECORD SUPERVISOR

MEDICAL RECORDS TECHNICIAN

MEDICAL STUDENT

MEDICAL STUDENT III

MEDICAL STUDENT IV

MEDICAL TECHNICIAN

MEDICAL TECHNOLOGIST

MEDICAL TECHNOLOGY STUDENT

MEDICAL TOXICOLOGIST

MIS FILE CLERK

NARCOTIC TECHNICIAN

NEUROLOGY PROGRAM CLERK

NEUROLOGY RESIDENT

NEUROLOGY TECHNICIAN

NUCLEAR CARDIOLOGY

NUCLEAR CARDIOLOGY DIRECTOR

NUCLEAR MEDICINE TECHNICIAN

NURSE

NURSE - STUDENT

NURSE ANESTHETIST

NURSE CLINICAL SPECIALIST

NURSE EPIDEMIOLOGIST

NURSE LICENSED PRACTICAL

NURSE PRACTITIONER

NURSING ASSISTANT

NURSING CLERK TYPIST

NURSING CONTINUING CARE

NURSING SUPERVISOR

NUTRITION CLINIC DIETITIAN

NUTRITION SUPPORT NURSE

OCCUPATIONAL THERAPIST

OCCUPATIONAL THERAPY ASSISTANT

OCCUPATIONAL THERAPY STUDENT

*Exported User Classes cont’d*

OCCURRENCE SCREENING

ONCOLOGY NURSE

OPC SCHEDULING SUPERVISOR

OPERATING ROOM COORDINATOR

OPERATING ROOM TECHNICIAN

OPHTHALMOLOGIST

OPTOMETRIST

ORAL SURGERY RESIDENT

ORTHOTIST/PROSTHETIST

OTOLARYNGOLOGY

OUTPATIENT CLINIC

OUTPATIENT CLINIC SUPERVISOR

OUTPATIENT PSYCHOLOGIST

OUTPATIENT RX SUPERVISOR

OUTPATIENT TECHNICIAN

PATHOLOGIST

PATHOLOGY RESIDENT

PEDIATRIC EMERGENCY PHYSICIAN

PHARMACIST

PHARMACY COORDINATOR

PHARMACY MEDICAL CLERK

PHARMACY STUDENT

PHARMACY SUPERVISOR

PHARMACY TECHNICIAN

PHARMACY TRAINEE

PHLEBOTOMIST

PHYSICAL THERAPIST

PHYSICAL THERAPY AID

PHYSICIAN

PHYSICIAN ASSISTANT

PHYSICIST

PODIATRIST

POST GRADUATE YEAR 1 RESIDENT

POST GRADUATE YEAR 2 RESIDENT

POST GRADUATE YEAR 3 RESIDENT

POST GRADUATE YEAR 4 RESIDENT

PRIVACY ACT OFFICER

PROCTOLOGIST

PROSTHETIC REPRESENTATIVE TRAINEE

PROSTHETICS

PROSTHETICS CLERK

PROSTHETICS REPRESENTATIVE

PROVIDER

PSYCHIATRIC RESEARCH ASSISTANT

PSYCHIATRIST

PSYCHIATRY CLERK

PSYCHIATRY PROGRAM ASSISTANT

PSYCHIATRY RESIDENT

PSYCHOLOGY CLINICAL ASSOCIATE

*Exported User Classes cont’d*

## PSYCHOLOGY INTERN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSYCHOLOGY PROGRAM CLERK

PSYCHOLOGY REHABILITATION TECHNICIAN

PSYCHOLOGY RESEARCH

PSYCHOLOGY VOCATIONAL REHAB SPEC

PULMONARY CHIEF

PULMONARY CLINICAL SPECIALIST

PULMONARY FELLOW

PULMONARY FUNCTION TECH

PULMONARY LAB SUPERVISOR

PULMONARY STAFF CHIEF OF STAFF

PULMONARY TECHNICIAN

RADIATION DIAGNOSTIC TECHNOLOGIST

RADIATION ONCOLOGIST

RADIATION THERAPY TECHNOLOGIST

RADIOGRAPHER

RADIOLOGIST

RADIOLOGY DIAGNOSTIC TECH

RADIOLOGY FILE ROOM SUPERVISOR

RADIOLOGY RESIDENT

RADIOLOGY TECHNICIAN

RADIOLOGY TRANSCRIPTIONIST

RECREATION THERAPIST

RECREATIONAL THERAPY ASSISTANT

REMOTE USER

RENAL FELLOW

RESEARCH NURSE

RESEARCH TECHNICIAN

RESEARCH TECHNOLOGIST

RESIDENT PHYSICIAN

RESPIRATORY THERAPIST

SECTION CHIEF

SENIOR ASSISTANT RESIDENT

SENIOR RESIDENT

SOCIAL WORK ASSOCIATE

SOCIAL WORK INTERN

SOCIAL WORK SECRETARY

SOCIAL WORKER

SOCIAL WORKER SUPERVISOR

SOLUTIONS TECHNICIAN

SPECIAL PROCEDURES

SPEECH PATHOLOGIST

SPEECH PATHOLOGY SECTION CHIEF

STAFF DENTIST

STAFF INTERNIST

STAFF NURSE

STAFF PATHOLOGIST

STAFF PHARMACIST

*Exported User Classes cont’d*

## STAFF PHYSICIAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STAFF PSYCHIATRIST

STAFF PSYCHOLOGIST

STAFF RADIOLOGIST

STAFF SOCIAL WORKER

STAFF SURGEON

STUDENT

STUDENT RADIOGRAPHER

SUB-INTERN

SUPERVISOR

SUPERVISOR, BLOOD BANK

SUPERVISOR, C&P UNIT

SUPERVISOR, EVENING LABS

SUPERVISOR, HEMATOLOGY LAB

SUPERVISOR, IMMUNOLOGY LAB

SUPERVISOR, MICROBIOLOGY LAB

SUPERVISOR, MIS

SUPERVISOR, PULMONARY FUNCTION LAB

SUPERVISOR, SPECIAL CHEM LAB

SUPERVISOR, STAT CHEM LAB

SUPERVISORY BIOCHEMIST

SUPERVISORY IMMUNOLOGIST

SUPERVISORY MICROBIOLOGIST

SUPERVISORY PHARMACIST

TRANSCRIPTIONIST

TUMOR REGISTRAR

UNIT COORDINATOR

UNIT NURSE

UNIT TEACHER

USER

VASCULAR NURSE

VETERINARIAN MEDICAL OFFICER

VOCATIONAL REHABILITATION SPECIALIST

# Appendix B: Exported Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASU Rule Browser Jun 20, 1997 16:33:39 Page: 1 of 5

List Business Rules by DOCUMENT DEFINITION 64 Rules

for CLASS CLINICAL DOCUMENTS

-------------------------------------------------------------------------------

1 An UNTRANSCRIBED (CLASS) CLINICAL DOCUMENT may be ENTERED by A USER

2 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be RELEASED by A TRANSCRIBER

3 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by An AUTHOR/DICTATOR

4 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by An EXPECTED SIGNER

5 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be SIGNED by An EXPECTED SIGNER

6 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be SIGNED by A PROVIDER who is

also An EXPECTED COSIGNER

7 A COMPLETED (CLASS) CLINICAL DOCUMENT may be VIEWED by A USER

8 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be EDITED by A TRANSCRIBER

9 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be EDITED by A TRANSCRIPTIONIST

10 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be COSIGNED by An EXPECTED

COSIGNER

11 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be SIGNED by A STUDENT who is

also An EXPECTED SIGNER

12 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by An EXPECTED COSIGNER

13 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by An EXPECTED COSIGNER

14 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

15 An UNDICTATED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

16 An UNTRANSCRIBED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

17 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

18 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

19 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

20 A COMPLETED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

21 An AMENDED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

22 A COMPLETED (CLASS) CLINICAL DOCUMENT may be PRINTED by A USER

23 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be VIEWED by An EXPECTED COSIGNER

24 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by A CLINICAL SERVICE

CHIEF

25 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be EDITED by A CLINICAL SERVICE

CHIEF

26 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be SIGNED by An ADDITIONAL SIGNER

27 A COMPLETED (CLASS) CLINICAL DOCUMENT may be SIGNED by An ADDITIONAL SIGNER

28 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be SIGNED by An ADDITIONAL

SIGNER

29 An AMENDED (CLASS) CLINICAL DOCUMENT may be VIEWED by A USER

30 An AMENDED (CLASS) CLINICAL DOCUMENT may be PRINTED by A USER

31 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be COPIED by An AUTHOR/DICTATOR

32 A COMPLETED (CLASS) CLINICAL DOCUMENT may be COPIED by A USER

33 A DELETED (CLASS) CLINICAL DOCUMENT may be DELETED by A CLINICAL

COORDINATOR

34 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be SENT BACK by A MEDICAL

INFORMATION SECTION

35 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be SENT BACK by A MEDICAL

INFORMATION SECTION

36 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be VIEWED by An EXPECTED

COSIGNER

37 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be VIEWED by A CLINICAL SERVICE CHIEF

38 A COMPLETED (CLASS) CLINICAL DOCUMENT may be AMENDED by A CHIEF, MIS

39 A COMPLETED (CLASS) CLINICAL DOCUMENT may be ADDENDED by A USER

40 An AMENDED (CLASS) CLINICAL DOCUMENT may be ADDENDED by A USER

41 A DELETED (CLASS) CLINICAL DOCUMENT may be VIEWED by A USER

42 A DELETED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

43 A PURGED (CLASS) CLINICAL DOCUMENT may be DELETED by A CHIEF, MIS

*Exported Business Rules, cont’d *

44 A PURGED (CLASS) CLINICAL DOCUMENT may be VIEWED by A USER

45 An UNTRANSCRIBED (CLASS) CLINICAL DOCUMENT may be VIEWED by A CHIEF, MIS

46 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be VIEWED by A CHIEF, MIS

47 An UNDICTATED (CLASS) CLINICAL DOCUMENT may be VIEWED by A USER

48 A COMPLETED (CLASS) CLINICAL DOCUMENT may be IDENTIFIED FOR SIGNATURE by An AUTHOR/DICTATOR

49 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be IDENTIFIED FOR SIGNATURE by

An AUTHOR/DICTATOR

50 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be IDENTIFIED FOR SIGNATURE by An EXPECTED COSIGNER

51 A COMPLETED (CLASS) CLINICAL DOCUMENT may be IDENTIFIED FOR SIGNATURE by An EXPECTED COSIGNER

52 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be REASSIGNED by A MEDICAL

INFORMATION SECTION

53 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be REASSIGNED by An

AUTHOR/DICTATOR

54 An UNSIGNED (CLASS) CLINICAL DOCUMENT may be HAVE ITS TITLE CHANGED by An

AUTHOR/DICTATOR

55 A COMPLETED (CLASS) CLINICAL DOCUMENT may be HAVE ITS TITLE CHANGED by A

CHIEF, MIS

56 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be HAVE ITS TITLE CHANGED by An EXPECTED COSIGNER

57 An UNCOSIGNED (CLASS) CLINICAL DOCUMENT may be HAVE ITS TITLE CHANGED by A

CLINICAL SERVICE CHIEF

58 A COMPLETED (CLASS) CLINICAL DOCUMENT may be REASSIGNED by A CHIEF, MIS

59 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be VIEWED by A MEDICAL

INFORMATION SECTION

60 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be VERIFIED by A MEDICAL

INFORMATION SECTION

61 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be EDITED by A MEDICAL

INFORMATION SECTION

62 An UNVERIFIED (CLASS) CLINICAL DOCUMENT may be PRINTED by A MEDICAL

INFORMATION SECTION

63 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be VIEWED by A TRANSCRIBER

64 An UNRELEASED (CLASS) CLINICAL DOCUMENT may be VIEWED by A TRANSCRIPTIONIST

List Business Rules by DOCUMENT DEFINITION 23 Rules

for CLASS PROGRESS NOTES

-------------------------------------------------------------------------------

1 A COMPLETED (CLASS) PROGRESS NOTE may be VIEWED by A USER

2 An UNSIGNED (CLASS) PROGRESS NOTE may be EDITED by A STUDENT who is also An AUTHOR/DICTATOR

3 An UNSIGNED (CLASS) PROGRESS NOTE may be DELETED by An AUTHOR/DICTATOR

4 An UNSIGNED (CLASS) PROGRESS NOTE may be VIEWED by An AUTHOR/DICTATOR

5 An UNCOSIGNED (CLASS) PROGRESS NOTE may be VIEWED by An AUTHOR/DICTATOR

6 An UNCOSIGNED (CLASS) PROGRESS NOTE may be VIEWED by An EXPECTED COSIGNER

7 An UNSIGNED (CLASS) PROGRESS NOTE may be PRINTED by An AUTHOR/DICTATOR

8 An UNCOSIGNED (CLASS) PROGRESS NOTE may be PRINTED by An AUTHOR/DICTATOR

9 An UNCOSIGNED (CLASS) PROGRESS NOTE may be EDITED by An EXPECTED COSIGNER

10 An UNSIGNED (CLASS) PROGRESS NOTE may be EDITED by An AUTHOR/DICTATOR

11 An UNCOSIGNED (CLASS) PROGRESS NOTE may be PRINTED by An EXPECTED COSIGNER

12 An UNSIGNED (CLASS) PROGRESS NOTE may be SIGNED by An AUTHOR/DICTATOR

13 An UNCOSIGNED (CLASS) PROGRESS NOTE may be COSIGNED by An EXPECTED COSIGNER

14 An UNSIGNED (CLASS) PROGRESS NOTE may be VIEWED by A CHIEF, MIS

15 An UNSIGNED (CLASS) PROGRESS NOTE may be DELETED by A CHIEF, MIS

16 An UNCOSIGNED (CLASS) PROGRESS NOTE may be VIEWED by A CHIEF, MIS

17 An UNCOSIGNED (CLASS) PROGRESS NOTE may be DELETED by A CHIEF, MIS

18 An UNSIGNED (CLASS) PROGRESS NOTE may be EDITED by An EXPECTED COSIGNER

19 An UNSIGNED (CLASS) PROGRESS NOTE may be VIEWED by An EXPECTED COSIGNER

20 An UNSIGNED (CLASS) PROGRESS NOTE may be EDITED by A CLINICAL SERVICE CHIEF

21 An UNSIGNED (CLASS) PROGRESS NOTE may be VIEWED by A CLINICAL SERVICE CHIEF

22 An UNSIGNED (CLASS) PROGRESS NOTE may be SIGNED by A CLINICAL SERVICE CHIEF

23 An UNSIGNED (CLASS) PROGRESS NOTE may be SIGNED by An EXPECTED COSIGNER

*Exported Business Rules, cont’d *

List Business Rules by DOCUMENT DEFINITION 17 Rules

for CLASS DISCHARGE SUMMARY

-------------------------------------------------------------------------------

1 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be EDITED by A PROVIDER who is

also An EXPECTED COSIGNER

2 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be SIGNED by A PROVIDER who is

also An ATTENDING PHYSICIAN

3 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be COSIGNED by A PROVIDER who

is also An EXPECTED COSIGNER

4 An UNVERIFIED (CLASS) DISCHARGE SUMMARY may be VIEWED by A MEDICAL

INFORMATION SECTION

5 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be EDITED by A PROVIDER who is

also An EXPECTED COSIGNER

6 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be SIGNED by A CLINICAL SERVICE

CHIEF

7 An UNVERIFIED (CLASS) DISCHARGE SUMMARY may be VERIFIED by A MEDICAL

INFORMATION SECTION

8 An UNVERIFIED (CLASS) DISCHARGE SUMMARY may be EDITED by A MEDICAL

INFORMATION SECTION

9 An UNVERIFIED (CLASS) DISCHARGE SUMMARY may be PRINTED by A MEDICAL

INFORMATION SECTION

10 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be VIEWED by A USER

11 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be PRINTED by A USER

12 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be ADDENDED by A USER

13 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be ADDENDED by A USER

14 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be VIEWED by A USER

15 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be COSIGNED by A CLINICAL

SERVICE CHIEF

16 An UNCOSIGNED (CLASS) DISCHARGE SUMMARY may be EDITED by A CLINICAL SERVICE CHIEF

17 An UNSIGNED (CLASS) DISCHARGE SUMMARY may be SIGNED by An EXPECTED SIGNER

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<
\<Enter\>, 6
A
About This Manual, 5
Action, 46
Action Definitions, 21
Action List, 39
Actions, 8
active, 11, 16
Adding a new Business Rule, 32
Adding and Editing Business Rules, 24
Amended, 38
AMENDMENT, 39
Appendices, 48
Appendix A: Exported User Classes, 50
Appendix B: Exported Business Rules, 56
ASU home page, 5
ASU Rule Browser, 24, 32
ATTACH ID ENTRY, 39
ATTACH TO ID NOTE, 39
Authorization, 46
AUTHORIZED, 3, 46
B
Benefits, 4
Browser, 24, 32
Business Rules, 24, 46
C
CHANGE TITLE, 39
Class, 20
Clinician, 46
Completed, 38
Copy or Send Back a Clinical Document, 28
COPY RECORD, 39
COSIGNATURE, 39
CPRS, 11
Create or edit Business Rules, 14
creating user classes, 14
D
Defining and Managing User Classes, 11
DELETE RECORD, 39
Deleting and Editing Business Rules, 35
Discharge Summaries, 3
Discharge Summary, 46
Document Class, 46
Document Definition, 46
E
Edit Business Rules, 25
EDIT COSIGNER, 39
EDIT RECORD, 39
ENTRY, 39
Expand/Collapse Tree, 17
Exported Business Rules, 56
Exported User Classes, 50
F
Features, 4
H
hidden) Actions, 8
hierarchies, 11
HIMS, 22
I
Icons, 6
IDENTIFY SIGNERS, 40
inactive, 11
Introduction, 1
Introduction to TIU, 3
L
LINK TO FLAG, 40
LINK WITH REQUEST, 40
List Manager utility, 7
List Membership by Class, 20
List Membership by User, 19
M
MAKE ADDENDUM, 40
*Manage Business Rules*, 24, 32
Medical Record Technicians, 22
Menu and options, 14
MIS, 22
O
Online Help, 7
P
Progress Notes, 3, 47
Provider Class, 11
Purpose of ASU, 3
R
REASSIGN, 40
RELEASE FROM TRANSCRIPTION, 41
Rule Browser, 24, 32
S
Screen Display, 7
security key, 3
SEND BACK, 41
SIGNATURE, 41
Status List, 38
statuses, 24
subclasses, 11, 17
SUBSCRIBE, 47
Subscription, 47
SURROGATE User Role, 27
T
Text Integration Utility, 11
TIU home page, 5
U
Uncosigned, 38
Undicatated, 38
Unreleased, 38
Unsigned, 38
*unsigned progress note*, 25
Untranscribed, 38
Unverified, 38
User Class, 20, 47
User Class Definition, 16
User Class SURROGATE, 27
User classes, 11
User Classes, 11
User responses, 6
User Role SURROGATE, 27
V
VERIFICATION, 41
VIEW, 41
VistA Document Library (VDL), 5
W
Web Resources, 5
