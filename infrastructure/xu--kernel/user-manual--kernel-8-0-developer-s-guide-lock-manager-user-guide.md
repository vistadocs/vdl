---
title: "Kernel 8.0 Developerâ€™s Guide: Lock Manager User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Lock Manager"
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
  - xulmu
  - guide
  - kernel
  - stack
  - lock
  - span
  - manager
  - table
  - cleanup
  - patient
page_count: 0
word_count: 1842
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_lock_manager_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_lock_manager_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259452" class="anchor"></span>Lock Manager Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Lock Manager Developer Tools User Guide</em>.</p>
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

<span id="_Toc207000598" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [Housekeeping](#housekeeping)
    - [CLEANUP^XULMU(): Execute the Housecleaning Stack](#cleanupxulmu-execute-the-housecleaning-stack)
    - [SETCLEAN^XULMU(): Register a Cleanup Routine](#setcleanxulmu-register-a-cleanup-routine)
    - [UNCLEAN^XULMU(): Remove Entries from the Housecleaning Stack](#uncleanxulmu-remove-entries-from-the-housecleaning-stack)
  - [Lock Dictionary](#lock-dictionary)
    - [ADDPAT^XULMU(): Add Patient Identifiers for a Computable File Reference](#addpatxulmu-add-patient-identifiers-for-a-computable-file-reference)
    - [PAT^XULMU(): Get a Standard Set of Patient Identifiers](#patxulmu-get-a-standard-set-of-patient-identifiers)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Lock Manager Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="Housekeeping_APIs" class="anchor"></span>Several Lock Manager APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Function are described below.

## Housekeeping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an application terminates, there may be housekeeping required. A prime example is the need to delete temporary data kept in the ^TMP and ^XTMP globals. An application that is terminated by the Lock Manager does *not* have the opportunity to do its own housecleaning, but the Lock Manager can do it for the application if it registers a housecleaning routine through the APIs described below.

### CLEANUP^XULMU(): Execute the Housecleaning Stack

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Lock Manager

ICR \#: 5832

Description: The CLEANUP^XULMU API executes the housecleaning stack set by the process identified by DOLLARJ. Entries are executed in the first-in-first-out (FIFO) order, with the last entry added being the first to be executed, and last being the last entry executed. If the last parameter is *not* passed in, then the entire stack is executed.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/004.png) NOTE: This API was released with Kernel Patch XU\*8.0\*608.

Format: CLEANUP^XULMU(\[last\])

Input Parameters: last: (optional) This is the last entry that is executed. If *not* passed in, then the entire housecleaning stack is executed.

Output: returns: None.

#### Examples

#### Example 1

An application can execute the entire housecleaning stack with the code shown in <u>Figure 1</u>:

<span id="_Ref508103371" class="anchor"></span>Figure 1: CLEANUP^XULMU API—Example 1

DO CLEANUP^XULMU

#### Example 2

If an application is called by another application, then the first application may have already placed entries of its own on the stack. So, the last parameter needs to be passed, with last being the first entry placed on the stack. It is the last entry executed, since that stack is executed in FIFO order.

<span id="_Toc23169103" class="anchor"></span>Figure 2: CLEANUP^XULMU API—Example 2

DO CLEANUP^XULMU(last)

### SETCLEAN^XULMU(): Register a Cleanup Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Lock Manager

ICR \#: 5832

Description: The SETCLEAN^XULMU API registers a cleanup routine that should be executed when the process is terminated by the Kernel Lock Manager. An entry is created on a stack kept for the process. The location is:

^XTMP(“XULM CLEANUP\_”\_\$J)

Where \$J uniquely identifies the process.

A process can call SETCLEAN^XULMU repeatedly, and each time a new entry is placed on the stack.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/005.png) CAUTION: Once an application calls SETCLEAN, upon exiting it *must* either execute its housecleaning stack or delete it using the APIs CLEAN or UNCLEAN.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*608.

Format: SETCLEAN^XULMU(rtn,.var)

Input Parameters: rtn: (required) The routine to be executed when the process is terminated.

.var: (required) An input array containing a list of variables that should be defined when the routine is executed. It is up to the application to ensure that all the required variables are defined when [CLEANUP^XULMU](#cleanupxulmu-execute-the-housecleaning-stack) is called.

Output: returns: Returns: An integer that identifies the entry created on the stack. The application needs to retain the value to either execute the entry on the housecleaning stack or to remove it.

#### Example

Suppose the application has a cleanup routine CLEANUP^XXAPP, and it needs to be executed with DFN defined with its present valued. The application would use this API as shown in Figure 3:

<span id="_Ref508102816" class="anchor"></span>Figure 3: SETCLEAN^XULMU API—Example

N VAR,CLEANUP

S VAR("DFN")=DFN

S CLEANUP=\$\$SETCLEAN^XULMU("CLEANUP^XXAPP",.VAR)

The application’s housekeeping stack would look like <u>Figure 4</u>:

<span id="_Ref508103332" class="anchor"></span>Figure 4: SETCLEAN^XULMU API—Sample Stack

^XTMP("XULM CLEANUP",\$J,1,"ROUTINE")="CLEANUP^XXAPP"

^XTMP("XULM CLEANUP",\$J,1,"VARIABLES","DFN")=1000061

### UNCLEAN^XULMU(): Remove Entries from the Housecleaning Stack

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Lock Manager

ICR \#: 5832

Description: The UNCLEAN^XULMU API removes entries from the housecleaning stack set by calling the <u>SETCLEAN^XULMU(): Register a Cleanup Routine</u> API. Entries are removed in First-In-First-Out (FIFO) order. If the last input parameter is *not* passed in, then the entire stack is deleted; otherwise, just the entries back to last are removed.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/007.png) NOTE: This API was released with Kernel Patch XU\*8.0\*608.

Format: UNCLEAN^XULMU(\[last\])

Input Parameters: last: (optional) Identifies the last entry on the housekeeping stack to remove. Entries are removed in FIFO order. Therefore, the first entry removed is the last entry that was added, and the last entry removed is last. If *not* passed in, the entire housecleaning stack is deleted.

Output: returns: None.

#### Examples

#### Example 1

The example in <u>Figure 5</u> would remove the entire housecleaning stack:

<span id="_Ref501631060" class="anchor"></span>Figure 5: UNCLEAN^XULMU API—Example 1

DO UNCLEAN^XULMU

#### Example 2

If an application is called by another application, then the first application may have already placed entries of its own on the stack. So, the last input parameter needs to be passed, with last being the first entry placed on the stack. It is the last entry deleted, since that stack is executed in first-in-first-out (FIFO) order.

<span id="_Toc508103427" class="anchor"></span>Figure 6: UNCLEAN^XULMU API—Example 2

DO UNCLEAN^XULMU(last)

## Lock Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ADDPAT^XULMU(): Add Patient Identifiers for a Computable File Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Lock Manager

ICR \#: 5832

Description: The ADDPAT^XULMU API is very similar to the <u>PAT^XULMU(): Get a Standard Set of Patient Identifiers</u> API, except that it is used to *add* the patient identifiers for a computable file reference for a file that is *not* the PATIENT (#2) file. The computable file references can include additional identifiers. For example, a computable file reference for a billing file can contain the bill number as an identifier as well as the patient identifiers returned by the ADDPAT^XULMU API.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*608.

Format: ADDPAT^XULMU(dfn)

Input Parameters: dfn: (required) The IEN of a record in the PATIENT (#2) file.

Output: returns: Returns: ID(0): If *not* defined at the point the ADDPAT^XULMU API is called, it is initially set to Zero (0). When the ADDPAT^XULMU API returns, the ID(0) is incremented by 4.

ID(ID(0)+1)=*\<patient name\>*

ID(ID(0)+2)=*\<patient sex\>*

ID(ID(0)+3)=*\<patient date of birth\>*

ID(ID(0)+4)=*\<patient Social Security Number\>*

### PAT^XULMU(): Get a Standard Set of Patient Identifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Lock Manager

ICR \#: 5832

Description: The PAT^XULMU API is for use within the M code for a computable file reference to the PATIENT (#2) file. It returns a standard set of patient identifiers.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/009.png) NOTE: This API was released with Kernel Patch XU\*8.0\*608.

Format: PAT^XULMU(dfn)

Input Parameters: dfn: (required) The IEN of a record in the PATIENT (#2) file.

Output: returns: Returns the following variables:

- ID(“IEN”)=DFN
- ID(0)=4
- ID(1)=*\<patient name\>*
- ID(2)=*\<patient sex\>*
- ID(3)=*\<patient date of birth\>*
- ID(4)=*\<patient Social Security Number\>*

#### Example

Assuming that DFN is a variable defined within the Lock template, then the M code for a computable file reference to the PATIENT (#2) file is shown in <u>Figure 7</u>:

<span id="_Ref508104060" class="anchor"></span>Figure 7: PAT^XULMU API—Example

DO PAT^XULMU(DFN)

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/010.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/011.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-lock-manager-user-guide/012.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.