---
title: XU*8*758 Reverse Negative Lock, Restricted Access User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Reverse Negative Lock, Restricted Access
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*758
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - replacement
  - program
  - class
  - mark
  - table
  - contents
  - vista
  - options
  - prompt
page_count: 0
word_count: 6630
section_count: 19
table_count: 2
figure_count: 9
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2022
revision_count: 1
revision_newest: 03/25/2022
revision_oldest: 03/25/2022
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_758_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_758_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Kernel 8.0

  Patch XU\*8.0\*758

  Reverse Negative Lock, Restricted Access

  User Guide
---

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/001.png)

March 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc99111444" class="anchor"></span>Revision History

| Date       | Revision | Description                                                                                              | Author                                     |
|------------|----------|----------------------------------------------------------------------------------------------------------|--------------------------------------------|
| 03/25/2022 | 1.0      | Initial *Kernel 8.0 Patch Supplement: XU\*8.0\*758 Reverse Negative Lock, Restricted Access User Guide*. | Kernel Patch XU\*8.0\*758 Development Team |

<span id="_Toc99108879" class="anchor"></span>Table 1: Documentation Symbols and Descriptions

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/002.png) NOTE: The revision history cycle begins once changes or enhancements are requested after Revision 1.0.

Table of Contents

<span id="_Toc44311551" class="anchor"></span>List of Figures

<span id="_Toc99111446" class="anchor"></span>List of Tables

[Table 1: Documentation Symbols and Descriptions [3](#_Toc99108879)](#_Toc99108879)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
    - [Background](#background)
    - [Introduction to the Program Replacement Security Key Menu](#introduction-to-the-program-replacement-security-key-menu)
  - [Documentation Conventions](#documentation-conventions)
- [Using the Software](#using-the-software)
  - [Assign the Program Replacement Key to Users for One User](#assign-the-program-replacement-key-to-users-for-one-user)
    - [Overview](#overview)
    - [Procedure](#procedure)
  - [Validate the Task is Complete in TaskMan](#validate-the-task-is-complete-in-taskman)
    - [Overview](#overview-1)
    - [Procedure](#procedure-1)
  - [Assign the Program Replacement Key to Users by Division(s)](#assign-the-program-replacement-key-to-users-by-divisions)
    - [Overview](#overview-2)
    - [Procedure](#procedure-2)
  - [Assign the Program Replacement Key for All Users](#assign-the-program-replacement-key-for-all-users)
    - [Overview](#overview-3)
    - [Procedure](#procedure-3)
  - [Remove the Program Replacement Key from One User](#remove-the-program-replacement-key-from-one-user)
    - [Overview](#overview-4)
    - [Procedure](#procedure-4)
  - [Remove the Program Replacement Key from Users by Division](#remove-the-program-replacement-key-from-users-by-division)
    - [Overview](#overview-5)
    - [Procedure](#procedure-5)
  - [Remove Program Replacement Key for All Users](#remove-program-replacement-key-for-all-users)
    - [Overview](#overview-6)
    - [Procedure](#procedure-6)
  - [Add Program Replacement Key to Options for Namespaces](#add-program-replacement-key-to-options-for-namespaces)
    - [Overview](#overview-7)
    - [Procedure](#procedure-7)
  - [Add Program Replacement Key to Options for a VistA Menu Option](#add-program-replacement-key-to-options-for-a-vista-menu-option)
    - [Overview](#overview-8)
    - [Procedure](#procedure-8)
  - [Remove Program Replacement Key to Options for Namespaces](#remove-program-replacement-key-to-options-for-namespaces)
    - [Overview](#overview-9)
    - [Procedure](#procedure-9)
  - [Remove Program Replacement Key from a VistA Menu Option](#remove-program-replacement-key-from-a-vista-menu-option)
    - [Overview](#overview-10)
    - [Procedure](#procedure-10)
  - [List Users With Program Replacement Key](#list-users-with-program-replacement-key)
    - [Overview](#overview-11)
    - [Procedure](#procedure-11)
  - [List Users Without Program Replacement Key](#list-users-without-program-replacement-key)
    - [Overview](#overview-12)
    - [Procedure](#procedure-12)
  - [List Options With Program Replacement Key](#list-options-with-program-replacement-key)
    - [Overview](#overview-13)
    - [Procedure](#procedure-13)
  - [List Options Without Program Replacement Key](#list-options-without-program-replacement-key)
    - [Overview](#overview-14)
    - [Procedure](#procedure-14)
  - [Show the Keys of a Particular User](#show-the-keys-of-a-particular-user)
    - [Overview](#overview-15)
    - [Procedure](#procedure-15)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Kernel 8.0 Patch Supplement: XU\*8.0\*758 Reverse Negative Lock, Restricted Access User Guide* provides instructions on restricting access to VistA options in preparation for the transition away from Veterans Health Information Systems and Technology Architecture (VistA) software.

### Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of VistA menu options is monitored by the Office of Information and Technology (OIT) during Go-Live and post-Go-Live of the software transition.

Kernel patch, XU\*8.0\*758, is used by all VistA replacement programs including, but not limited to Electronic Health Record (EHR) systems, Defense Medical Logistics Standard Support (DMLSS), and Financial Management Business Transformation Service (FMBT) implementation of Integrated Financial and Acquisition Management System (iFAMS). Use of VistA options during and after the new EHR Go-Live, specifically, is restricted to those options that provide one of the following:

- VistA functionality that the EHR or other VistA replacement program does *not* support.
- VistA functionality requiring close-out of processes that were initiated before the VistA replacement program Go-Live.
- VistA functionality that maintains the VistA database integrity, which remains a vital component of the System of Record (SOR).

Veterans Health Administration (VHA) and OIT collaborated to create software requirements and technical processes for a new VistA patch, XU\*8.0\*758, which provides new functionality to restrict end-user access to VistA options defined by the criteria mentioned above. Patch XU\*8.0\*758 uses the REVERSE/NEGATIVE LOCK feature to restrict end-user access to VistA options by assigning the following security keys to appropriate VistA options:

- DMLSS REPLACEMENT
- EHR REPLACEMENT
- IFAMS REPLACEMENT

The process to restrict end-user access to VistA options requires a three-step process:

1.  Agreement between VHA and OIT on specific VistA options for which end-user access should be restricted.
2.  Assignment of the Program Replacement Security Key to end-users.
3.  Assignment of the Program Replacement Security Key to the REVERSE/NEGATIVE LOCK (#3.01) field in the OPTION (#19) File for those VistA options requiring restricted access.

XU\*8.0\*758 introduces a new menu option, VistA Transition Menu \[XUEHRM MAIN\]. As a secondary menu option, this menu is assigned to a few staff members, specifically the local facility EHR Modernization Cutover Lead or designee(s). All users must be aware of the impact when using the options on the VistA Transition Menu. It must be used only by staff who have received training and know its features, functionalities, and capabilities. Therefore, Patch XU\*8.0\*758 provides functionality to assign a security key to one or more users and one or more options. The security key can be removed when access is required, allowing user access to specific options.

This user guide demonstrates the features, functionalities, and capabilities of the Program Replacement Security Key using the EHR Replacement key as an example. Other VistA replacement program keys have the same features, functionalities, and capabilities; however, the sample user dialogs as presented in this user guide may differ in the local system.

### Introduction to the Program Replacement Security Key Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Program Replacement Security Key menu has nine options. Each option allows for varied functionality to control access and visibility to VistA menu options, which will be restricted after the new system Go-Live. These functions include adding, removing the replacement key from a single user, from a single division, and for all users, as well as adding, removing the program replacement security key from VistA menu options and namespaces. <u>Figure 1</u> shows the main menu of the Program Replacement Security Key.

<span id="_Ref92869633" class="anchor"></span>Figure 1: Program Replacement Security Key Menu Options—Sample User Dialog

1 Assign Program Replacement Key to Users

2 Remove Program Replacement Key from Users

3 Add Program Replacement Key to Options

4 Remove Program Replacement Key from Options

5 List Users with Program Replacement Key

6 List Users without Program Replacement Key

7 List Options with Program Replacement Key

8 List Options without Program Replacement Key

9 Show the keys of a particular user

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes descriptions of any formatting or symbols and their meaning. It describes the format used for test data, note, caution, warning, and danger symbols. Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

| Symbol                                                                                                                                                                                                                                     | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/003.png)                                                        | NOTE: Used to inform the reader of general information, including references to additional reading material |
| ![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/004.png) | CAUTION: Used to caution the reader to take special notice of critical information                          |

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provides step-by-step instructions on removing and assigning the Replacement Key.

## Assign the Program Replacement Key to Users for One User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option to assign users the program replacement key. This is located under the Vista TransitionMenu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign the program replacement key, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to assign to VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter U to assign the key to a single user only.
4.  At the "Select a user:" prompt, enter the name of the user you wish to assign the key.
5.  At the "Select another user:" prompt, continue to enter other users as needed.
6.  At the "Are you ready to assign the program replacement \<EHR REPLACEMENT\> to the users? YES//" prompt, press Enter.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 2</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92809058" class="anchor"></span>

Figure 2: Assign Program Replacement Key to Users Option—Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> Assign Program Replacement Key to Users

What Program Replacement Key do you want to assign to VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D// <span class="mark">U\<Enter\></span> User(s)

Select a user: <span class="mark">LAST NAME, FIRST NAME</span>

Select another user: <span class="mark">\<Enter\></span>

Are you ready to assign the program replacement \<EHR REPLACEMENT\> to the users? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:44:52)

<span class="mark">Task \#: 2771242</span>

## Validate the Task is Complete in TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test if the system has assigned the program replacement key to the *user* by querying TaskMan.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test if the program replacement key was assigned, do the following:

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/005.png) NOTE: TaskMan is available only to staff with permissions. Thus, the following steps can only be completed if TaskMan is included in the menu tree. Also note, for larger facilities TaskMan may take longer to process the task.

1.  Right-click and select Copy to copy the Task# from the previous procedure. (e.g., Task# 2771242, as shown in <u>Figure 3</u>).
2.  From the Vista Transition Menu \[XUEHRM MAIN\], enter “TOOLBOX”. Then, enter “TASK” to access the TaskMan User \[XUTM USER\] option.
3.  At the "Select TASK:" prompt, right-click and select Paste to paste the previously copied task number.
4.  At the "Select Action (Task \# \*\*\*\*\*\*\*):" prompt, enter D for Display Status.
5.  The system shows the completed task with a timestamp (<u>Figure 3</u>).

<span id="_Ref92818440" class="anchor"></span>

Figure 3: Validate Task in TaskMan Option—Sample User Dialog

Select TASK: <span class="mark">2771242 \<Enter\></span> Assign Keys for users.

               Taskman User Option

                    Display status.

                    Stop task.

                    Edit task.

                    Print task.

                    List own tasks.

                    Select another task.

Select Action (Task \# 2771242): <span class="mark">D \<Enter\></span> Display status.

2776464: ASSIGN^XUSEHRM1, Assign Keys for users.  No device.  SPO5,ROU.

From Today at 16:06, By you.  Completed Today at 16:06.

## Assign the Program Replacement Key to Users by Division(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option to assign the program replacement key users across a division. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign the program replacement key to users across a division, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to assign to VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter D to assign the key to a single division only.
4.  At the "Select a division:" prompt, enter the name or code of the division you wish to assign the key.
5.  At the "Select another division:" prompt, continue to enter other divisions, as needed.
6.  At the "Are you ready to assign the program replacement \<EHR REPLACEMENT\> to VistA users at above Division(s)? YES//" prompt, press Enter.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 4</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92813762" class="anchor"></span>

Figure 4: Assign Program Replacement Key to Users by Division Option—Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> Assign Program Replacement Key to Users

What Program Replacement Key do you want to assign to VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D// <span class="mark">D \<Enter\></span> Division(s)

Select a division: Division code <span class="mark">\<Enter\></span>

Select another Division: <span class="mark">\<Enter\></span>

Are you ready to assign the program replacement \<EHR REPLACEMENT\> to VistA users at above Division(s):? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:44:52)

<span class="mark">Task \#: 2776507</span>

## Assign the Program Replacement Key for All Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option to assign the program replacement key to *all* VistA users in the accounts database. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign the program replacement key to ALL USERS, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Assign Program Replacement Key to Users \[XUEHRM ADD KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to assign to VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter A to assign the key to all users.
4.  At the "Are you ready to assign the program replacement \<EHR REPLACEMENT\> to ALL VistA users? YES//" prompt, press Enter.
5.  At the "Requested Start Time: NOW//" prompt, press Enter.
6.  The system processes the request with a task number, as shown in (<u>Figure 5</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92815339" class="anchor"></span>

Figure 5: Assign Program Replacement Key to Users for All Users Option—Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> Assign Program Replacement Key to Users

What Program Replacement Key do you want to assign to VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D// <span class="mark">A \<Enter\></span> All users

Are you ready to assign the program replacement \<EHR REPLACEMENT\> to ALL VistA users? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:44:52)

<span class="mark">Task \#: 2776524</span>

## Remove the Program Replacement Key from One User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Remove Program Replacement Key from Users \[XUEHRM REM KEY USERS\] option to remove the program replacement key from a user. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the program replacement key from a USER, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Remove Program Replacement Key to Users \[XUEHRM REM KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to remove from VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter U to assign the key to a single user only.
4.  At the "Select a user:" prompt, enter the name of the user you wish to remove from the key.
5.  At the "Select another user:" prompt, continue to enter other users as needed.
6.  At the "Are you ready to remove the program replacement \<EHR REPLACEMENT\> from the users? YES//" prompt, press Enter.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 6</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92819031" class="anchor"></span>

Figure 6: Remove Program Replacement Key from One User Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">2</span><span class="mark">\<Enter\></span> Remove Program Replacement Key from Users

What Program Replacement Key do you want to remove from VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D// <span class="mark">U \<Enter\></span> User(s)

Select a user: <span class="mark">LAST NAME, FIRST NAME</span>

Select another user: <span class="mark">\<Enter\></span>

Are you ready to remove the program replacement \<EHR REPLACEMENT\> from the users? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:08:04)

<span class="mark">Task \#: 2771220</span>

## Remove the Program Replacement Key from Users by Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Remove Program Replacement Key from Users \[XUEHRM REM KEY USERS\] function to remove the program replacement key from a user in a specific division. This selection is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the program replacement key from a user in a specific DIVISION, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN, select the Remove Program Replacement Key to Users \[XUEHRM REM KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to remove from VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter D to assign the key to a single division only.
4.  At the "Select a division:" prompt, enter the name or code of the division to which you wish to assign the program replacement key.
5.  At the "Select another division:" prompt, continue to enter other divisions as needed. Press Enter when you have completed adding other namespaces.
6.  At the "Are you ready to remove the program replacement \<EHR REPLACEMENT\> from VistA users at above Division(s)? YES//" prompt, press Enter.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 7</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92820119" class="anchor"></span>

Figure 7: Remove Program Replacement Key to Users Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">2 \<Enter\></span> Remove Program Replacement Key from Users

What Program Replacement Key do you want to remove from VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: <span class="mark">D \<Enter\></span> Division(s)

Select a division: *<span class="mark">Division code</span>*

Select another Division: <span class="mark">\<Enter\></span>

Are you ready to remove the program replacement \<EHR REPLACEMENT\> to VistA users at above Division(s):? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:08:04)

<span class="mark">Task \#: 2771221</span>

## Remove Program Replacement Key for All Users 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Remove Program Replacement Key to Users \[XUEHRM REM KEY USERS\] option to remove the program replacement key from all VistA users in the accounts database. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the program replacement key from ALL USERS, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Remove Program Replacement Key to Users \[XUEHRM REM KEY USERS\] option.
2.  At the "What Program Replacement Key do you want to remove to VistA users?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D//" prompt, enter A to remove the key to all users.
4.  At the "Are you ready to remove the program replacement \<EHR REPLACEMENT\> to ALL VistA users? YES//" prompt, press Enter.
5.  At the "Requested Start Time: NOW//" prompt, press Enter.
6.  The system processes the request with a task number, as shown in (<u>Figure 8</u>) which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92820107" class="anchor"></span>

Figure 8: Remove Program Replacement Key to Users for All VistA Users Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">2 \<Enter\></span> Remove Program Replacement Key from Users

What Program Replacement Key do you want to assign to VistA users? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (U)sers, (D)ivisions, (A)ll users, (Q)uit: D// <span class="mark">A \<Enter\></span> All users

Are you ready to remove the program replacement \<EHR REPLACEMENT\> to ALL VistA users? YES// <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 05, 2022@14:44:52)

<span class="mark">Task \#: 2776574</span>

## Add Program Replacement Key to Options for Namespaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Add Program Replacement Key to Options \[XUEHRM ADD KEY OPTS\] option to add the program replacement key to a VistA menu option for Namespaces. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add the program replacement key to VistA menu options for a NAMESPACE, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Add Program Replacement Key to Options \[XUEHRM ADD KEY OPTS\] option.
2.  At the "What Program Replacement Key do you want to assign to options?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (N)amespaces, (O)ptions, (Q)uit: D//" prompt, enter N to add the key to a namespace.
4.  At the "Please select a Namespace" prompt, enter the namespace to which you wish to add the replacement key.
5.  At the "Select Another Namespace:" prompt, continue to enter other namespaces as needed. Press Enter when you have completed adding other namespaces.
6.  At the "Do you want to remove any options from the list above? YES//" prompt, enter NO.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 9</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92874023" class="anchor"></span>

Figure 9: Add Program Replacement Key to Options for Namespaces Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">3 \<Enter\></span> Add Program Replacement Key to Options

What Program Replacement Key do you want to assign to options? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (N)amespaces, (O)ptions, (Q)uit: O// <span class="mark">N</span> <span class="mark">\<Enter\></span> Namespace

Please select a Namespace: <span class="mark">ORVCO</span>

Another Namespace: <span class="mark">\<Enter\></span>

Option list :

-----------------

ORVCO BENCH ORVCO CREATE

ORVCO MENU ORVCO MONITOR

ORVCO TEST

There are 5 options from the list above.

Do you want to remove any options from the list above? YES// <span class="mark">NO</span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 12, 2022@09:32:36)

<span class="mark">Task \#: 2777107</span>

## Add Program Replacement Key to Options for a VistA Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Add Program Replacement Key to Options \[XUEHRM ADD KEY OPTS\] option to add the program replacement key to a VistA menu option. This selection is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add the program replacement key to a VistA MENU option, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Add Program Replacement Key to Options \[XUEHRM ADD KEY OPTS\] option.
2.  At the "What Program Replacement Key do you want to assign to options?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (N)amespaces, (O)ptions, (Q)uit: D//" prompt, enter O to add the key to an option.
4.  At the "Select an option prompt," enter the option name to which you wish to add the replacement key.
5.  At the "Select an option:" prompt, continue to enter other option names as needed. Press Enter when you have completed adding other options.
6.  At the "Do you want to remove any options from the list above? YES//" prompt, press Enter.
7.  At the "Select an option" prompt, press Enter.
8.  At the "Requested Start Time: NOW//" prompt, press Enter.
9.  The system processes the request with a task number, as shown in (<u>Figure 10</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92874001" class="anchor"></span>Figure 10: Add Program Replacement Key to Options for VistA Menu Options Option– Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">3</span> <span class="mark">\<Enter\></span> Add Program Replacement Key to Options

What Program Replacement Key do you want to assign to options? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (N)amespaces, (O)ptions, (Q)uit: O// <span class="mark">O</span><span class="mark">\<Enter\></span> Option

Select an option: GMRC MGR Consult Management <span class="mark">\<Enter\></span>

Select an option: <span class="mark">\<Enter\></span>

Option list :

-----------------

GMRC MGR

There is 1 option from the list above.

Do you want to remove any options from the list above? YES// <span class="mark">\<Enter\></span>

Select an option: <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 12, 2022@09:54:02)

<span class="mark">Task \#: 2777119</span>

## Remove Program Replacement Key to Options for Namespaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Remove Program Replacement Key to Options \[XUEHRM REM KEY OPTS\] option to remove the program replacement key to a VistA menu option for Namespaces. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the program replacement key to options for a namespace, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Add Program Replacement Key to Options \[XUEHRM REM KEY OPTS\] option.
2.  At the "What Program Replacement Key do you want to remove from options?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (N)amespaces, (O)ptions, (Q)uit: D//" prompt, enter N to add the key to a namespace.
4.  At the "Please select a Namespace" prompt, enter the namespace to which you wish to add the replacement key.
5.  At the "Select Another Namespace:" prompt, continue to enter other namespaces as needed. Press Enter when you have completed adding other namespaces.
6.  At the "Do you want to remove any options from the list above? YES//" prompt, enter NO.
7.  At the "Requested Start Time: NOW//" prompt, press Enter.
8.  The system processes the request with a task number, as shown in (<u>Figure 11</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92875245" class="anchor"></span>

Figure 11: Remove Program Replacement Key to Options for Namespaces Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">4 \<Enter\></span> Remove Program Replacement Key from Options

What Program Replacement Key do you want to remove from options? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (N)amespaces, (O)ptions, (Q)uit: O// <span class="mark">N</span> <span class="mark">\<Enter\></span> Namespace

Please select a Namespace: <span class="mark">ORVCO</span>

Another Namespace: <span class="mark">\<Enter\></span>

Option list :

-----------------

ORVCO BENCH ORVCO CREATE

ORVCO MENU ORVCO MONITOR

ORVCO TEST

There are 5 options from the list above.

Do you want to remove any options from the list above? YES// <span class="mark">NO</span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 12, 2022@10:09:49)

<span class="mark">Task \#: 2777131</span>

## Remove Program Replacement Key from a VistA Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Remove Program Replacement Key from Options \[XUEHRM REM KEY OPTS\] option to remove the program replacement key to a VistA menu option. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the program replacement key from options for a VistA menu OPTION, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the RemoveProgram Replacement Key to Options \[XUEHRM REM KEY OPTS\] option.
2.  At the "What Program Replacement Key do you want to remove from options?" prompt, enter EHR REPLACEMENT to locate the key.
3.  At the "Do you want to select (N)amespaces, (O)ptions, (Q)uit: D//" prompt, enter O to remove the key for an option.
4.  At the "Select an option prompt," enter the option name to which you wish to add the replacement key.
5.  At the "Select an option:" prompt, continue to enter other option names as needed. Press Enter when you have completed adding other options.
6.  At the "Do you want to remove any options from the list above? YES//" prompt, press Enter.
7.  At the "Select an option" prompt, press Enter.
8.  At the "Requested Start Time: NOW//" prompt, press Enter.
9.  The system processes the request with a task number, as shown in (<u>Figure 12</u>), which can be validated in TaskMan (see Section <u>2.2</u>).

<span id="_Ref92877089" class="anchor"></span>Figure 12: Remove Program Replacement Key Option—Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">4</span> <span class="mark">\<Enter\></span> Remove Program Replacement Key from Options

What Program Replacement Key do you want to remove from options? <span class="mark">EHR REPLACEMENT</span>

Do you want to select (N)amespaces, (O)ptions, (Q)uit: O// <span class="mark">O</span><span class="mark">\<Enter\></span> Option

Select an option: <span class="mark">GMRC MGR</span><span class="mark">\<Enter\></span> Consult Management

Select an option: <span class="mark">\<Enter\></span>

Option list :

-----------------

GMRC MGR

There is 1 option from the list above.

Do you want to remove any options from the list above? YES// <span class="mark">\<Enter\></span>

Select an option: <span class="mark">\<Enter\></span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 12, 2022@09:54:02)

<span class="mark">Task \#: 2777141</span>

## List Users With Program Replacement Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the List Users With Program Replacement Key \[XUEHRM LIST USERS KEYS\] option to list users who have been assigned the program replacement key. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/006.png) CAUTION: Executing this option could generate a large report.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list users *with* the program replacement key assigned, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the List Users with Program Replacement Key \[XUEHRM LIST USERS KEYS\] option.
2.  At the "What Program Replacement Key do you want to check?" prompt, enter EHR REPLACEMENT.
3.  At the "Do you want to save this in CSV (excel) Format YES//" prompt, press Enter.
4.  At the "DEVICE: HOME//" prompt, press Enter.
5.  At the "V20 REPORTING SYSTEM Right Margin: 80//" prompt, press Enter.
6.  The system processes the request furnishing a list of users with the Program Replacement Key (<u>Figure 13</u>).

> <span id="_Ref92877070" class="anchor"></span>Figure 13: List Users With Program Replacement Key Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">5</span>

List Users with Program Replacement Key

What Program Replacement Key do you want to check? <span class="mark">EHR REPLACEMENT</span>

Do you want to save this in CSV (Excel) Format? YES// <span class="mark">\<Enter\></span>

DEVICE:HOME// <span class="mark">\<Enter\></span> V20 REPORTING SYSTEM Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">NAME\|DUZ\|SEVICE/SECTION\|PRIMARY MENU\|LAST SIGN_ON</span>

<span class="mark">LAST NAME, FIRST NAME\|123456\|INFORMATION RESOURCE MGMT\|EVE\| 22/1/7</span>

## List Users Without Program Replacement Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the List Users Without Program Replacement Key \[XUEHRM LIST USERS NO KEYS\] option to list users that have *not* been assigned the program replacement key. This option is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/007.png) CAUTION: Executing this option could generate a large report.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list the users WITHOUT the program replacement key assigned, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the List Users without Program Replacement Key \[XUEHRM LIST USERS NO KEYS\] option.
2.  At the "Which Program Replacement Key do you want to check?" prompt, enter EHR REPLACEMENT.
3.  At the "Do you want to save this in CSV (excel) Format YES//" prompt, press Enter.
4.  At the "DEVICE: HOME//" prompt, press Enter.
5.  At the "V20 REPORTING SYSTEM Right Margin: 80//" prompt, press Enter.
6.  The system processes the request furnishing a list of users without the Program Replacement Key (<u>Figure 14</u>).

> <span id="_Ref92880862" class="anchor"></span>Figure 14: List Users Without Program Replacement Key Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">6</span>

List Users without Program Replacement Key

Which Program Replacement Key do you want to check? <span class="mark">EHR REPLACEMENT</span>

Do you want to save this in CSV (Excel) Format? YES// <span class="mark">\<Enter\></span>

DEVICE:HOME// <span class="mark">\<Enter\></span> V20 REPORTING SYSTEM Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">NAME\|DUZ\|SEVICE/SECTION\|PRIMARY MENU\|LAST SIGN_ON</span>

<span class="mark">LAST NAME, FIRST NAME\|123456\|INFORMATION RESOURCE MGMT\|EVE\| 22/1/7</span>

## List Options With Program Replacement Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the List Options With Program Replacement Key \[XUEHRM LIST OPTS KEYS\] option to list options that have been assigned the program replacement key. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/008.png) CAUTION: Executing this option could generate a large report.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list options *with* the program replacement key assigned, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the List Options with Program Replacement Key \[XUEHRM LIST OPTS KEYS\] option.
2.  At the "Which Program Replacement Key do you want to check?" prompt, enter EHR REPLACEMENT.
3.  At the "Do you want to save this in CSV (excel) Format YES//" prompt, press Enter.
4.  At the "DEVICE: HOME//" prompt, press Enter.
5.  At the "V20 REPORTING SYSTEM Right Margin: 80//" prompt, press Enter.
6.  The system processes the request furnishing a list of options with the Program Replacement Key (<u>Figure 15</u>).

> <span id="_Ref92880837" class="anchor"></span>Figure 15: List Options With Program Replacement Key Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">7</span>

List Options with Program Replacement Key

Which Program Replacement Key do you want to check? <span class="mark">EHR REPLACEMENT</span>

Do you want to save this in CSV (Excel) Format? YES// <span class="mark">\<Enter\></span>

DEVICE:HOME// <span class="mark">\<Enter\></span> V20 REPORTING SYSTEM Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">OPTION NAME\|NEGATIVE LOCK\|LOCK</span>

<span class="mark">TIUFZZ43 CLEANUP AFTER PTCH 43\|EHR REPLACEMENT\|</span>

<span class="mark">TIUZZ65 CLEANUP AFTER PTCH 65\|EHR REPLACEMENT\|</span>

<span class="mark">...</span>

## List Options Without Program Replacement Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the List Options Without Program Replacement Key \[XUEHRM LIST OPTS NO KEYS\] option to list options that have *not* been assigned the program replacement key. This option is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

![](xu-8-758-reverse-negative-lock-restricted-access-user-guide/009.png) CAUTION: Executing this option could generate a large report.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list options *without* the program replacement key assigned, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the List Options without Program Replacement Key \[XUEHRM LIST OPTS NO KEYS\] option.
2.  At the "Which Program Replacement Key do you want to check?" prompt, enter EHR REPLACEMENT.
3.  At the "Do you want to save this in CSV (excel) Format YES//" prompt, press Enter.
4.  At the "DEVICE: HOME//" prompt, press Enter.
5.  At the "V20 REPORTING SYSTEM Right Margin: 80//" prompt, press Enter.
6.  The system processes the request furnishing a list of options with the Program Replacement Key (<u>Figure 16</u>).

> <span id="_Ref92881784" class="anchor"></span>Figure 16: List Options Without Program Replacement Key Option – Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">8</span>

List Options without Program Replacement Key

Which Program Replacement Key do you want to check? <span class="mark">EHR REPLACEMENT</span>

Do you want to save this in CSV (Excel) Format? YES// <span class="mark">\<Enter\></span>

DEVICE:HOME// <span class="mark">\<Enter\></span> V20 REPORTING SYSTEM Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">OPTION NAME\|NEGATIVE LOCK\|LOCK</span>

<span class="mark">DGBT FISCAL REPORT\|\|</span>

<span class="mark">DGBT TRAVEL REPORTS MENU\|\|</span>

<span class="mark">DGBT CLAIM DEDUCTIBLE PAID\|\|</span>

<span class="mark">...</span>

## Show the Keys of a Particular User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Show the Keys of a Particular User \[XQLISTKEY\] option to list all keys that have been assigned to a specific user. This is located under the Vista Transition Menu \[XUEHRM MAIN\] option.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list the program replacement keys assigned to a particular user, do the following:

1.  From the Vista Transition Menu \[XUEHRM MAIN\], select the Show the Keys of a Particular User \[XQLISTKEY\] option.
2.  At the "User's name?" prompt, enter the Last Name, First Name of the user whose keys you wish to display.
3.  The system processes the request furnishing a list of keys the user currently holds (<u>Figure 17</u>).

<span id="_Ref92882237" class="anchor"></span>

> Figure 17: Show the Keys of a Particular User Option―Sample User Dialog

Select VistA Transition Menu \<TEST ACCOUNT\> Option: <span class="mark">9 \<Enter\></span> Show the keys of a particular user

User's name: <span class="mark">LAST NAME, FIRST NAME</span>

<span class="mark">FIRST NAME LAST NAME currently holds:</span>

<span class="mark">A1B2 SUPERVISOR A3OSMGR ACRP REPORTS AMIS ASA-ENG-PM</span>

<span class="mark">ASA-ENG-PMCATEDITASA-ENG-PMWODELASB EXAMS ASBPROFI ASC ENCOUNTER</span>

<span class="mark">ASC PRCB MASTER AUI1MGR AUTHORIZE BILL AXVAMM BIG LOCK</span>

<span class="mark">BRADDOCK CYBER SECURITY DDXP-DEFINE DG CONSISTENCY DG DEPDELETE</span>

<span class="mark">DG DETAIL DG ELIGIBILITY DG FEMALE DG G&L RECAL DG INPATIENT</span>