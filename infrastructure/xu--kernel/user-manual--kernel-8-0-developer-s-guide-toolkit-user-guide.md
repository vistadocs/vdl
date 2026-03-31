---
title: "Kernel 8.0 Developerâ€™s Guide: Toolkit User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Toolkit"
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
menu_options: 1
description: 
audience: 
keywords: 
  - span
  - class
  - parameter
  - table
  - toolkit
  - routine
  - contents
  - guide
  - kernel
  - entry
page_count: 0
word_count: 34966
section_count: 13
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259615" class="anchor"></span>Toolkit Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-toolkit-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-toolkit-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Toc199951064" class="anchor"></span>Table 1: .03 DUPLICATE TEST ROUTINE—Variables Passed to the Test Routine</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Toolkit Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc199951064" class="anchor"></span>Table 1: .03 DUPLICATE TEST ROUTINE—Variables Passed to the Test Routine

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Toc207255805" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-toolkit-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Developer Tools](#developer-tools)
  - [Toolkit—Data Standardization](#toolkitdata-standardization)
    - [Overview](#overview)
    - [Replacement Relationships](#replacement-relationships)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
    - [\$\$GETRPLC^XTIDTRM(): Get Mapped Terms (Term/Concept)](#getrplcxtidtrm-get-mapped-terms-termconcept)
    - [\$\$RPLCLST^XTIDTRM(): Get Replacement Terms, w/Optional Status Date and History (Term/Concept)](#rplclstxtidtrm-get-replacement-terms-woptional-status-date-and-history-termconcept)
    - [\$\$RPLCMNT^XTIDTRM(): M One Term to Another (Term/Concept)](#rplcmntxtidtrm-m-one-term-to-another-termconcept)
    - [\$\$RPLCTRL^XTIDTRM(): Get Replacement Trail, w/ Replaced “BY” and Replacement “FOR” Terms](#rplctrlxtidtrm-get-replacement-trail-w-replaced-by-and-replacement-for-terms)
    - [\$\$RPLCVALS^XTIDTRM(): Get Field Values of Final Replacement Term (Term/Concept)](#rplcvalsxtidtrm-get-field-values-of-final-replacement-term-termconcept)
    - [\$\$SETRPLC^XTIDTRM(): Set Replacement Terms (Term/Concept)](#setrplcxtidtrm-set-replacement-terms-termconcept)
  - [Toolkit—Duplicate Record Merge](#toolkitduplicate-record-merge)
    - [Overview](#overview-1)
  - [Toolkit—Developing a File Merge Capability](#toolkitdeveloping-a-file-merge-capability)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
    - [Description of What Occurs during the Merge](#description-of-what-occurs-during-the-merge)
    - [Entries Needed in the PACKAGE (#9.4) File](#entries-needed-in-the-package-94-file)
    - [Step 3](#step-3)
    - [Special Processing Routine Examples](#special-processing-routine-examples)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis-1)
    - [EN^XDRMERG(): Merge File Entries](#enxdrmerg-merge-file-entries)
    - [RESTART^XDRMERG(): Restart Merge](#restartxdrmerg-restart-merge)
    - [SAVEMERG^XDRMERGB(): Save Image of Existing and Merged Data](#savemergxdrmergb-save-image-of-existing-and-merged-data)
  - [Toolkit—HTTP Client](#toolkithttp-client)
    - [Overview](#overview-2)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis-2)
    - [\$\$GETURL^XTHC10: Return URL Data Using HTTP](#geturlxthc10-return-url-data-using-http)
    - [\$\$ENCODE^XTHCURL: Encodes a Query String](#encodexthcurl-encodes-a-query-string)
    - [\$\$MAKEURL^XTHCURL: Creates a URL from Components](#makeurlxthcurl-creates-a-url-from-components)
    - [\$\$PARSEURL^XTHCURL: Parses a URL](#parseurlxthcurl-parses-a-url)
    - [\$\$DECODE^XTHCUTL: Decodes a String](#decodexthcutl-decodes-a-string)
  - [Toolkit—KERMIT APIs](#toolkitkermit-apis)
    - [RFILE^XTKERM4: Add Entries to Kermit Holding File](#rfilextkerm4-add-entries-to-kermit-holding-file)
    - [RECEIVE^XTKERMIT: Load a File into the Host](#receivextkermit-load-a-file-into-the-host)
    - [SEND^XTKERMIT: Send Data from Host](#sendxtkermit-send-data-from-host)
  - [Toolkit—Multi-Term Look-Up (MTLU)](#toolkitmulti-term-look-up-mtlu)
    - [How to Override](#how-to-override)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis-3)
    - [XTLKKWL^XTLKKWL: Perform Supported VA FileMan Calls on Files Configured for MTLU](#xtlkkwlxtlkkwl-perform-supported-va-fileman-calls-on-files-configured-for-mtlu)
    - [DK^XTLKMGR(): Delete Keywords from the Local Keyword File](#dkxtlkmgr-delete-keywords-from-the-local-keyword-file)
    - [DLL^XTLKMGR(): Delete an Entry from the Local Lookup File](#dllxtlkmgr-delete-an-entry-from-the-local-lookup-file)
    - [DSH^XTLKMGR(): Delete Shortcuts from the Local Shortcut File](#dshxtlkmgr-delete-shortcuts-from-the-local-shortcut-file)
    - [DSY^XTLKMGR(): Delete Synonyms from the Local Synonym File](#dsyxtlkmgr-delete-synonyms-from-the-local-synonym-file)
    - [K^XTLKMGR(): Add Keywords to the Local Keyword File](#kxtlkmgr-add-keywords-to-the-local-keyword-file)
    - [L^XTLKMGR(): Define a File in the Local Lookup File](#lxtlkmgr-define-a-file-in-the-local-lookup-file)
    - [LKUP^XTLKMGR(): General Lookup Facility for MTLU](#lkupxtlkmgr-general-lookup-facility-for-mtlu)
    - [SH^XTLKMGR(): Add Shortcuts to the Local Shortcut File](#shxtlkmgr-add-shortcuts-to-the-local-shortcut-file)
    - [SY^XTLKMGR(): Add Terms and Synonyms to the Local Synonym File](#syxtlkmgr-add-terms-and-synonyms-to-the-local-synonym-file)
  - [Toolkit—M Unit Utility](#toolkitm-unit-utility)
    - [Overview](#overview-3)
    - [Introduction to M Unit Testing](#introduction-to-m-unit-testing)
    - [M Unit Test Definitions](#m-unit-test-definitions)
    - [Getting Started](#getting-started)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis-4)
    - [EN^XTMUNIT(): Run Unit Tests](#enxtmunit-run-unit-tests)
    - [CHKEQ^XTMUNIT: Check Two Values for Equivalence](#chkeqxtmunit-check-two-values-for-equivalence)
    - [CHKLEAKS^XTMUNIT(): Check for Variable Leaks](#chkleaksxtmunit-check-for-variable-leaks)
    - [CHKTF^XTMUNIT(): Test Conditional Values](#chktfxtmunit-test-conditional-values)
    - [FAIL^XTMUNIT(): Generate an Error Message](#failxtmunit-generate-an-error-message)
    - [\$\$ISUTEST^XTMUNIT: Evaluate if Unit Test is Running](#isutestxtmunit-evaluate-if-unit-test-is-running)
    - [SUCCEED^XTMUNIT: Increment Test Counter](#succeedxtmunit-increment-test-counter)
    - [M Unit Utility Sample Output](#m-unit-utility-sample-output)
  - [Toolkit—Parameter Tools](#toolkitparameter-tools)
    - [Overview](#overview-4)
    - [Definitions](#definitions)
    - [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis-5)
    - [ADD^XPAR(): Add Parameter Value](#addxpar-add-parameter-value)
    - [CHG^XPAR(): Change Parameter Value](#chgxpar-change-parameter-value)
    - [DEL^XPAR(): Delete Parameter Value](#delxpar-delete-parameter-value)
    - [EN^XPAR(): Add, Change, Delete Parameters](#enxpar-add-change-delete-parameters)
    - [ENVAL^XPAR(): Return All Parameter Instances](#envalxpar-return-all-parameter-instances)
    - [\$\$GET^XPAR(): Return an Instance of a Parameter](#getxpar-return-an-instance-of-a-parameter)
    - [GETLST^XPAR(): Return All Instances of a Parameter](#getlstxpar-return-all-instances-of-a-parameter)
    - [GETWP^XPAR(): Return Word-Processing Text](#getwpxpar-return-word-processing-text)
    - [NDEL^XPAR(): Delete All Instances of a Parameter](#ndelxpar-delete-all-instances-of-a-parameter)
    - [PUT^XPAR(): Add/Update Parameter Instance](#putxpar-addupdate-parameter-instance)
    - [REP^XPAR(): Replace Instance Value](#repxpar-replace-instance-value)
    - [BLDLST^XPAREDIT(): Return All Entities of a Parameter](#bldlstxparedit-return-all-entities-of-a-parameter)
    - [EDIT^XPAREDIT(): Edit Instance and Value of a Parameter](#editxparedit-edit-instance-and-value-of-a-parameter)
    - [EDITPAR^XPAREDIT(): Edit Single Parameter](#editparxparedit-edit-single-parameter)
    - [EN^XPAREDIT: Parameter Edit Prompt](#enxparedit-parameter-edit-prompt)
    - [GETENT^XPAREDIT(): Prompt for Entity Based on Parameter](#getentxparedit-prompt-for-entity-based-on-parameter)
    - [GETPAR^XPAREDIT(): Select Parameter Definition File](#getparxparedit-select-parameter-definition-file)
    - [TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)](#tedxparedit-edit-template-parameters-no-dash-dividers)
    - [TEDH^XPAREDIT(): Edit Template Parameters (with Dash Dividers)](#tedhxparedit-edit-template-parameters-with-dash-dividers)
  - [Toolkit—VHA Unique ID (VUID) APIs](#toolkitvha-unique-id-vuid-apis)
    - [GETIREF^XTID(): Get IREF (Term/Concept)](#getirefxtid-get-iref-termconcept)
    - [\$\$GETMASTR^XTID(): Get Master VUID Flag (Term/Concept)](#getmastrxtid-get-master-vuid-flag-termconcept)
    - [\$\$GETSTAT^XTID(): Get Status Information (Term/Concept)](#getstatxtid-get-status-information-termconcept)
    - [\$\$GETVUID^XTID(): Get VUID (Term/Concept)](#getvuidxtid-get-vuid-termconcept)
    - [\$\$SCREEN^XTID(): Get Screening Condition (Term/Concept)](#screenxtid-get-screening-condition-termconcept)
    - [\$\$SETMASTR^XTID(): Set Master VUID Flag (Term/Concept)](#setmastrxtid-set-master-vuid-flag-termconcept)
    - [\$\$SETSTAT^XTID(): Set Status Information (Term/Concept)](#setstatxtid-set-status-information-termconcept)
    - [\$\$SETVUID^XTID(): Set VUID (Term/Concept)](#setvuidxtid-set-vuid-termconcept)
  - [Toolkit—Routine Tools](#toolkitroutine-tools)
    - [Direct Mode Utilities](#direct-mode-utilities)
    - [Routine Tools Menu](#routine-tools-menu)
  - [Toolkit—Verification Tools](#toolkitverification-tools)
    - [Direct Mode Utilities](#direct-mode-utilities-1)
    - [Verifier Tools Menu](#verifier-tools-menu)
    - [Programmer Options Menu](#programmer-options-menu)
  - [XINDEX](#xindex)
    - [Types of XINDEX Findings](#types-of-xindex-findings)
    - [Running the XINDEX Utility](#running-the-xindex-utility)
    - [Analysis of XINDEX Error Findings by Category](#analysis-of-xindex-error-findings-by-category)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Toolkit Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several tools and Application Programming Interfaces (APIs) are available for developers to work with Kernel Toolkit. This section describes these APIs by type.

## Toolkit—Data Standardization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The API set in this section has been developed to support Data Standardization’s effort to allow the mapping of one term to another term. Mapping of terms is done through the REPLACED BY VHA STANDARD TERM (#99.97) field and provides the high-level goals of the following:

- *Non*-standard terms inheriting standardized characteristics.
- Deprecating a term and replacing it with a new term.

The Data Standardization API set:

1.  Maps one term to another term.
2.  Obtains the term in which another term is mapped.
3.  Extracts field values from the term in which another term is mapped.
4.  Shows the mapping relationships that a term has with other terms.

Keywords:

- VHA Unique ID (VUID)
- Data Standardization
- Term
- Replacement Term

![](kernel-8-0-developer-s-guide-toolkit-user-guide/004.png) NOTE: This Data Standardization API set was released with Kernel Toolkit Patch XT\*7.3\*111.

### Replacement Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the replacement relationships in <u>Figure 1</u> to map the Data Standardization API set in context. These APIs are documented in this section:

<span id="_Ref505757013" class="anchor"></span>Figure 1: Toolkit—Replacement Relationships: Data Standardization

     A --\> B --\> C --\> D      A is replaced by B     G is replaced by C

    ^ ^         ^ ^           B is replaced by C     H is replaced by C

    \|  \\       \|  \\         C is replaced by D     I is replaced by F

    \|   \\      \|   \\        D has no replacement   J is replaced by F

    \|    \\     \|    \\       E is replaced by A     K is replaced by H

    \|     F     \|     H       F is replaced by A     L is replaced by H

    \|    ^ ^    \|    ^ ^

    \|   /   \\  \|   /   \\

    E  I     J  G  K     L

   

   \$\$GETRPLC(B) would return C

   

   \$\$RPLCMNT(B) would return D

   

   \$\$RPLCVALS(J) would return the requested field values from entry D

   

   \$\$RPLCTRL(G) in both directions would return D and the output array would

   be set as follows:

   

    OutArr("BY",A) = B                  OutArr("FOR",A,E) = ""

    OutArr("BY",B) = C                  OutArr("FOR",A,F) = ""

    OutArr("BY",C) = D                  OutArr("FOR",B,A) = ""

    OutArr("BY",D) = ""                 OutArr("FOR",C,B) = ""

    OutArr("BY",E) = A                  OutArr("FOR",C,G) = ""

    OutArr("BY",F) = A                  OutArr("FOR",C,H) = ""

    OutArr("BY",G) = C                  OutArr("FOR",D,C) = ""

    OutArr("BY",H) = C                  OutArr("FOR",F,I) = ""

    OutArr("BY",I) = F                  OutArr("FOR",F,J) = ""

    OutArr("BY",J) = F                  OutArr("FOR",H,K) = ""

    OutArr("BY",K) = H                  OutArr("FOR",H,L) = ""

    OutArr("BY",L) = H

   

   \$\$RPLCTRL(L) in the forward direction would return D and the output array

   would be set as follows:

   

    OutArr("BY",C) = D                  OutArr("FOR",C,H) = ""

    OutArr("BY",D) = ""                 OutArr("FOR",D,C) = ""

    OutArr("BY",H) = C                  OutArr("FOR",H,L) = ""

    OutArr("BY",L) = H

   

   \$\$RPLCTRL(B) in the backward direction would return D and the output array

   would be set as follows:

   

    OutArr("BY",A) = B                  OutArr("FOR",A,E) = ""

    OutArr("BY",E) = A                  OutArr("FOR",A,F) = ""

    OutArr("BY",F) = A                  OutArr("FOR",B,A) = ""

    OutArr("BY",I) = F                  OutArr("FOR",F,I) = ""

    OutArr("BY",J) = F                  OutArr("FOR",F,J) = ""

   

   \$\$RPLCLST(G) in both directions would return D and the output array would

   be set as follows:

   

    OutArr(1) = G ^ 0                   OutArr("INDEX",A) = 8

    OutArr(2) = C ^ 0                   OutArr("INDEX",B) = 7

    OutArr(3) = D ^ 1                   OutArr("INDEX",C) = 2

    OutArr(4) = H ^ 0                   OutArr("INDEX",D) = 3

    OutArr(5) = K ^ 0                   OutArr("INDEX",E) = 9

    OutArr(6) = L ^ 0                   OutArr("INDEX",F) = 10

    OutArr(7) = B ^ 0                   OutArr("INDEX",G) = 1

    OutArr(8) = A ^ 0                   OutArr("INDEX",H) = 4

    OutArr(9) = E ^ 0                   OutArr("INDEX",I) = 11

    OutArr(10) = F ^ 0                  OutArr("INDEX",J) = 12

    OutArr(11) = I ^ 0                  OutArr("INDEX",K) = 5

    OutArr(12) = J ^ 0                  OutArr("INDEX",L) = 6

   

   \$\$RPLCLST(L) in the forward direction would return D and the output array

   would be set as follows if the status history was also included:

    

    OutArr(1) = L ^ 0                   OutArr("INDEX",C) = 3

    OutArr(1,3080101.0954) = 0          OutArr("INDEX",D) = 4

    OutArr(2) = H ^ 0                   OutArr("INDEX",H) = 2

    OutArr(2,3080101.1308) = 1          OutArr("INDEX",L) = 1

    OutArr(2,3080105.09) = 0

    OutArr(3) = C ^ 0

    OutArr(3,3080105.0859) = 1

    OutArr(3,3080112.1722) = 0

    OutArr(4) = D ^ 1

    OutArr(4,3080112.1723) = 1

   

   \$\$RPLCLST(B) in the backward direction would return D and the output array

   would be set as follows:

   

    OutArr(1) = A ^ 0                   OutArr("INDEX",A) = 1

    OutArr(2) = E ^ 0                   OutArr("INDEX",E) = 2

    OutArr(3) = F ^ 0                   OutArr("INDEX",F) = 3

    OutArr(4) = I ^ 0                   OutArr("INDEX",I) = 4

    OutArr(5) = J ^ 0                   OutArr("INDEX",J) = 5

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \$\$GETRPLC^XTIDTRM(): Get Mapped Terms (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$GETRPLC^XTIDTRM extrinsic function gets the REPLACED BY VHA STANDARD TERM (#99.97) field for a given entry.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/005.png) REF: For an overview of the Data Standardization API set, see <u>Toolkit—Data Standardization APIs</u>.  
  
For a chart mapping the Data Standardization API set in context, see <u>Replacement Relationships</u>.

Format: \$\$GETRPLC^XTIDTRM(file,ien)

Input Parameters: file: (required) File number.

ien: (required) Internal Entry Number (IEN).

Output: returns: Returns the REPLACED BY VHA STANDARD TERM (#99.97) field for a given entry.

#### Example

The \$\$GETRPLC^XTIDTRM extrinsic function sets X to IEN\_“;”\_FileNumber of entry that replaces the input entry:

<span id="_Toc199950734" class="anchor"></span>Figure 2: \$\$GETRPLC^XTIDTRM API—Example

\><span class="mark">S X=\$\$GETRPLC^XTIDTRM(file,ien)</span>

![](kernel-8-0-developer-s-guide-toolkit-user-guide/006.png) NOTE:

- NULL is returned on error. This typically occurs when the input entry does *not* exist.
- If the input entry is *not* replaced by another term then a reference to the input term is returned.

### \$\$RPLCLST^XTIDTRM(): Get Replacement Terms, w/Optional Status Date and History (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$RPLCLST^XTIDTRM extrinsic function traverses the REPLACED BY VHA STANDARD TERM (#99.97) field forwards and backwards to find all terms that are replacement terms for the input entry and all terms for which the input entry is a replacement. This is recursively done so that each potential branch of replacement terms forwards and backwards is traversed.

Format: \$\$RPLCLST^XTIDTRM(file,ien,drctn,statdate,stathst,outarr)

Input Parameters: file: (required) File number.

ien: (required) Entry number.

drctn: (optional) Flags denoting which direction to follow the trail of replacement terms. Possible flag values are:

- F (default)—Follow the trail forwards.
- B—Follow the trail backwards.
- \*—Follow the trail in both directions (same as FB/BF).

statdate: (optional) VA FileMan DATE/TIME in which to return term’s status. Defaults to current DATE/TIME.

stathst: (optional) Flag denoting if a term’s full status history should be included in the output:

- 0 (default)—No.
- 1—Yes.

Input/OutputParameters: outarr: I: (required) Array to put trail of replacement terms into (closed root).

O: The output array contains the list terms to which the input entry is somehow related.

- OutArr(1..*n*) = Term ^ StatusCode (based on input StatDate).
- OutArr(1..*n*,StatusDateTime) = StatusCode on this DATE/TIME.
- This node is only returned if StatHst is set to 1 (Yes).
- OutArr(“INDEX”,Term) = 1..*n*.

Where:

- Term is in the format IEN;FileNumber.
- StatusCode:
- 1—Active.
- 0—Inactive.
- StatusDateTime is in VA FileMan format.

#### Example

The \$\$RPLCLST^XTIDTRM extrinsic function sets X=IEN\_“;”\_FileNumber of the entry that ultimately replaces the input entry:

<span id="_Toc199950735" class="anchor"></span>Figure 3: \$\$RPLCLST^XTIDTRM API—Example

\><span class="mark">S X=\$\$RPLCLST^XTIDTRM(File,IEN,Drctn,StatDate,StatHst,OutArr)</span>

![](kernel-8-0-developer-s-guide-toolkit-user-guide/007.png) NOTE:

- NULL is returned on error. This typically occurs when the input entry does *not* exist.
- If the input entry is *not* replaced by another term then a reference to the input term is returned.

### \$\$RPLCMNT^XTIDTRM(): M One Term to Another (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$RPLCMNT^XTIDTRM extrinsic function recursively traverses the REPLACED BY VHA STANDARD TERM (#99.97) field until the final replacement term is reached.

Format: \$\$RPLCMNT^XTIDTRM(fle,ien)

Input Parameters: file: (required) File number.

ien: (required) Internal Entry Number (IEN).

Output: none.

#### Example

The \$\$RPLCMNT^XTIDTRM extrinsic function sets X to IEN\_“;”\_FileNumber of the entry that ultimately replaces the input entry:

<span id="_Toc199950736" class="anchor"></span>Figure 4: \$\$RPLCMNT^XTIDTRM API—Example

\><span class="mark">S X=\$\$RPLCMNT^XTIDTRM(file,ien)</span>

![](kernel-8-0-developer-s-guide-toolkit-user-guide/008.png) NOTES:

- NULL is returned on error. This typically occurs when the input entry does *not* exist.
- If the input entry is *not* replaced by another term then a reference to the input term is returned.

### \$\$RPLCTRL^XTIDTRM(): Get Replacement Trail, w/ Replaced “BY” and Replacement “FOR” Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$RPLCTRL^XTIDTRM extrinsic function traverses the REPLACED BY VHA STANDARD TERM (#99.97) field forwards and backwards to find all terms that are replacement terms for the input entry and all terms for which the input entry is a replacement. This is recursively done so that each potential branch of replacement terms forwards and backwards is traversed.

Format: \$\$RPLCTRL^XTIDTRM(file,ien,drctn,outarr)

Input Parameters: file: (required) File number.

ien: (required) Internal Entry Number (IEN).

drctn: (optional) Flags denoting which direction to follow the trail of replacement terms. Possible flag values are:

- F (default)—Follow the trail forwards.
- B—Follow the trail backward.
- \*—Follow the trail in both directions (same as FB/BF).

Input/OutputParameters: outarr: I: (required) Array to put trail of replacement terms into (closed root).

O: The output array contains the trail of replacement terms.

- OutArr(“BY”,Term) = Replacement Term means: Entry “Term” is replaced BY entry “Replacement Term.”
- OutArr(“FOR”,Replacement Term, Term) = “” means: Entry “Replacement Term” is a replacement FOR entry “Term.”
- Term and Replacement Term is in the format IEN;FileNumber.

#### Example

The \$\$RPLCTRL^XTIDTRM extrinsic function sets X to IEN\_“;”\_FileNumber of the entry that ultimately replaces the input entry:

<span id="_Toc199950737" class="anchor"></span>Figure 5 \$\$RPLCTRL^XTIDTRM API—Example

\><span class="mark">S X=\$\$RPLCTRL^XTIDTRM(file,ien,drctn,outarr)</span>

![](kernel-8-0-developer-s-guide-toolkit-user-guide/009.png) NOTES:

- NULL is returned on error. This typically occurs when the input entry does *not* exist.
- If the input entry is *not* replaced by another term then a reference to the input term is returned.

### \$\$RPLCVALS^XTIDTRM(): Get Field Values of Final Replacement Term (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$RPLCVALS^XTIDTRM extrinsic function retrieves one or more fields of data from an entry’s final replacement term. The REPLACED BY VHA STANDARD TERM (#99.97) field is recursively traversed until the final replacement term is reached. The requested fields of the final replacement term are returned. It effectively bundles \$\$RPLCMNT^XTIDTRM and GETS^DIQ into a single call.

Format: \$\$RPLCVALS^XTIDTRM(file,ien,fields,flags,outarr)

Input Parameters: file: (required) File number.

ien: (required) Internal Entry Number (IEN).

fields: (required) Fields for which you wish to get values.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/010.png) REF: For detailed description, see the definition of the FIELD parameter in the GETS^DIQ API in the *VA FileMan Developer’s Guide*.

flags: (required) Flags that control output format.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/011.png) REF: For detailed description, see the definition of the FLAGS parameter in the GETS^DIQ API in the *VA FileMan Developer’s Guide*.

Input/Output:Parameters outarr: Input/Output:

- I: (required) Array to put output field values into (closed root).
- O: The output array is in FDA format.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/012.png) REF: For example output, see the GETS^DIQ API in the *VA FileMan Developer’s Guide*.

#### Example

The \$\$RPLCVALS^XTIDTRM extrinsic function sets X to IEN\_“;”\_FileNumber of the entry that ultimately replaces the input entry:

<span id="_Toc199950738" class="anchor"></span>Figure 6: \$\$RPLCVALS^XTIDTRM API—Example

\><span class="mark">S X=\$\$RPLCVALS^XTIDTRM(file,ien,fields,flags,outarr)</span>

![](kernel-8-0-developer-s-guide-toolkit-user-guide/013.png) NOTES:

- NULL is returned on error. This typically occurs when the input entry does *not* exist.
- If an error occurs when extracting the requested fields from the final replacement term then a reference to the final replacement term is still returned and outarr is KILLed.
- If the input entry is *not* replaced by another term then a reference to the input term is returned and outarr( ) contains the field values for the input entry.

### \$\$SETRPLC^XTIDTRM(): Set Replacement Terms (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Data Standardization

ICR \#: 5078

Description: The \$\$SETRPLC^XTIDTRM extrinsic function sets the REPLACED BY VHA STANDARD TERM (#99.97) field.

Format: \$\$SETRPLC^XTIDTRM(file,ien,rplcmnt)

Input Parameters: file: (required) File number.

ien: (required) Internal Entry Number (IEN).

rplcmnt: (required) Entry number of replacement term.

Output Variables: X: Results:

- 1 (success)—If POINTER to replacement term stored.
- 0 (failure)—If unable to store POINTER to replacement term.

#### Example

The \$\$SETRPLC^XTIDTRM extrinsic function sets X to 1 if POINTER to replacement term stored (that is success) or 0 if Unable to store POINTER to replacement term (that is failure):

<span id="_Toc199950739" class="anchor"></span>Figure 7: \$\$SETRPLC^XTIDTRM API—Example

\><span class="mark">S X=\$\$SETRPLC^XTIDTRM(File,IEN,Rplcmnt)</span>

## Toolkit—Duplicate Record Merge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A file in which entries need to be merged can be entered in the DUPLICATE RESOLUTION (#15.1) file. This requires adding the file as one that can be selected as the VARIABLE POINTER, and search criteria would usually need to be specified to assist in identifying potential duplicate pairs (although an option can be used by which selected pairs can be added directly to the DUPLICATE RECORD (#15) file as verified duplicates). Verified duplicate pairs may be approved for merging, and a merge process generated for those approved pairs. A DUPLICATE RECORD (#15) file entry also has handle files that are *not* associated as normal POINTERs identified in the PACKAGE (#9.4) file under the AFFECTS RECORD MERGE subfile with special processing routines.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/014.png) CAUTION: If a file has related files that are *not* normal pointers, they should be handled only as entries in the duplicate record file and the Kernel Toolkit options used for merges involving the file.

The merge utility of Kernel Toolkit as revised by Kernel Toolkit Patch XT\*7.3\*23 provides an entry point that is available to developers for the merging of one or more pairs of records (a FROM record and a TO record) in a specified file. The merge process merges the data of the FROM record into that of the TO record and deletes the FROM record, restoring by a hard set only the Zero node with the .01 value on it until the merge process is completed (such that any references to that location by POINTERs does *not* error out). Any files that contain entries DINUMed with the data pairs are then also merged (and any files that are related to them by DINUM as well). Any POINTERs that can be identified rapidly by cross-references are modified so that references for the FROM entry become references to the TO entry instead. Following this, any files that contain other POINTERs are searched entry by entry to test for POINTERs to a FROM entry, and when found are modified to reference the TO entry. This search for POINTER values is the most time consuming part of the entire process and may take an extended period depending upon the number of files that *must* be searched, the number of entries in those files, and how many levels at which subfiles POINTERs may be located. Since the search through these files takes the same period independent of the number of pairs that are being merged, it is suggested that as many pairs as convenient be combined in one process. At the end of the conversion of these POINTERs, the Zero node stubs are removed from the primary file and all related DINUMed files.

The merge process is a single job that is tracked with frequent updates on location and status from start to finish. The job can be stopped at any time if necessary using TaskMan utilities (or in the event of a system crash, and so on) and restarted at the point of interruption later.

#### How Data is Merged

When a primary file or a DINUMed files entries are merged, any top level (single value) fields that are present in the FROM entry that are *not* present in the TO entry is merged into the TO entries data. Any of these fields that contain cross-references are entered using a VA FileMan utility (FILE^DIE) so that the cross-references are fired. Other fields (those *without* cross-references) are directly set into the data global.

If a subfile entry (Multiple) exists in the FROM record that is *not* present in the TO record (as identified by the .01 value), that entry is created with a VA FileMan utility (UPDATE^DIE) and the rest of the subfile merged over into the TO record and the cross-references within the subfile and any descendent subfiles run.

If a subfile entry (Multiple) exists in the FROM record and an identical .01 value exists in the TO record, the subfile in the FROM record is searched for any descendent subfiles that are *not* present in the TO record subfile. If such a subfile is found it is merged into the subfile in the TO record and any cross-references in the merged subfile run.

For fields that are simple POINTERs to the primary file (or any other file DINUMed to the primary file) the reference to the FROM record is changed to a reference to the TO record. If the field contains a cross-reference this editing is performed using a VA FileMan Utility call (FILE^DIE); otherwise, it is set directly into the global node.

## Toolkit—Developing a File Merge Capability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides developers with a set of instructions to follow in building a merge capability for a file. After a developer identifies a file that has a substantial number of duplicates and that the nature and use of the file warrants a merge utility, they then follows the steps outlined in this section in developing that merge capability.

For demonstration purposes, the rest of this section uses a specific example of developing a Patient Merge using the Duplicate Resolution Utilities.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notify the Kernel Toolkit developers of the perceived need for a duplicate checking/merge capability for a file. They will do the following:

1.  Assists the developer in deciding whether there is indeed a need for a Duplicate Resolution Utility for the file.
5.  Add the file to the .01 and .02VARIABLE POINTER field definitions in the DUPLICATE RECORD (#15) file.
6.  Notifies the application developer when the modified dictionary is to be released to the field.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The developer needs to now communicate to the larger development community his/her intention to develop a merge capability for this file. All developers need to determine if the merging and deleting of records in this file affects their package in such a way that they need to have their own unique merge routine that deals with only their package's files. A developer usually must write their own unique merge routine if any of the following conditions exist:

- Patient POINTER field is defined as a NUMERIC or FREE TEXT field rather than a POINTER.
- Developer wants their end users to complete some task prior to the merge occurring.
- There are compound cross-references that include the patient POINTER on another field, but the cross-reference is *not* triggered by the changing of the patient POINTER.
- Merge (Duplicate Resolution Utilities) does *not* do what the package developer desires.

### Description of What Occurs during the Merge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a brief description of what occurs during the merge process:

1.  The base file (such as PATIENT file, \#2) is checked to see if it exists.
7.  The PT nodes (such as ^DD(2,0,"PT",) are checked and any false positives are removed.
8.  Creates a list of files and fields within those files that point to the file being merged (such as in this example the file being merged is the PATIENT file, \#2).
9.  If a file is pointing to the file being merged by its .01 field, and if that .01 field is DINUM, then all files/fields that point to that file are also gathered. The DINUM rule also applies to that file and any files pointing to it, to any depth.
10. Each file/field is checked and re-pointed/merged as follows:
- If the field pointing is *not* a .01 field, the FROM entry is changed to the TO entry.
- If the field pointing is the .01 field but *not*DINUM, the FROM entry is changed to the TO entry.
- Each pointing .01DINUM field is handled as follows:
- If the .01DINUM field is at the file level, ^DIT0 is called to merge the FROM entry to the TO entry and then the FROM entry is deleted.  
  >   
  > ^DIT0 merges field by field but does *not* change any value in the TO entry. That means that NULL fields in the TO entry get the value from the same field in the FROM entry if it is *not*NULL, and valued fields in the TO entry remain the same.  
  >   
  > ^DIT0 also merges Multiples. If a Multiple entry in the FROM entry *cannot* be found in the TO entry, it is added to the TO entry. If a Multiple entry in the FROM entry can be found in the TO entry, then that Multiple entry is merged field by field.
- If the .01 DINUM field is at the subfile level (in a Multiple), it is handled as follows:
- If there is a FROM entry but no TO entry, the FROM entry is added to the TO entry, changing the .01 field value in the process, and the FROM entry is deleted.
- If there is a FROM entry and a TO entry, the FROM entry is deleted and the TO entry remains unchanged.

If it is determined that a developer *must* have their own unique merge that deals with their files, they *must* make the appropriate entries in the PACKAGE (#9.4) file. If they must have some sort of action taken by end-users prior to the merging of the records, they *must* update the MERGE PACKAGES (#1101) Multiple field in the DUPLICATE RECORD (#15) file for that pair of records.

### Entries Needed in the PACKAGE (#9.4) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the PACKAGE (#9.4) file make entries in the following fields:

- AFFECTS RECORD MERGE (#20) field.
- NAME (#.01) field—Enter the file affected (such as PATIENT \[#2\] file).
- NAME OF MERGE ROUTINE (#9.402,3) field—Enter the name of the merge routine, which is executed using indirection by Duplicate Resolution Utilities.  
    
  If you leave this field blank but still place an entry in the PACKAGE (#9.4) file, Duplicate Resolution Utilities assumes that you have some sort of interactive merge process that your end-users *must* complete prior to the main merging of the two records. It also assumes that this interactive merge process is on a separate option within the developer's package options. The values of the two records being merged are placed in:
- ^TMP("XDRMRGFR",\$J,XDRMRG("FR"),
- ^TMP("XDRMRGTO",\$J,XDRMRG("TO"),

These should be referenced by the developer if they need any certain field values since the values might have been changed prior to the execution of their merge routine.

- RECORD HAS PACKAGE DATA (#9.402,4) field—Enter a string of M executable code that is passed the variable XDRMRG("FR") (the FROM record IEN) and set XDRZ to 0. The code should set XDRZ=1 if XDRMRG("FR") has data within your package files.

Remember to only make these entries in the PACKAGE (#9.4) file if the normal merge does *not* suffice for your package. If you have an entry in the PACKAGE (#9.4) file, the repointing and merging as described above does *not* take place for those files within your Package entry.

At the completion of your interactive merge process, the developer *must* set the STATUS (#15.01101,.02) field of the MERGE PACKAGES (#1101) Multiple field for their package in the DUPLICATE RECORD (#15) file entry to Ready. This *must* be done using VA FileMan, because of the trigger that is on the STATUS field. Once all MERGE PACKAGE entries have a STATUS of Ready, the main merging of the two records can occur.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The developer needs to add an entry in the DUPLICATE RESOLUTION (#15.1) file for the file being built. The following fields need to be updated in the DUPLICATE RESOLUTION (#15.1) file and data should be entered by the developer:

- .01 FILE TO BE CHECKED (required)
- .06 CROSS-REF FOR NEW SEARCH (optional)
- .09 CANDIDATE COLLECTION ROUTINE (required)
- .11 DUPLICATE MANAGER MAIL GROUP (optional)
- .15 POTENTIAL DUPLICATE THRESHOLD% (required)
- .16 VERIFIED DUPLICATE MAIL GROUP (optional)
- .17 VERIFIED DUPLICATE MSG ROUTINE (optional)
- .18 VERIFIED DUPLICATE THRESHOLD% (optional)
- .25 MERGE STYLE (required)
- .26 DELETE FROM ENTRY (optional)
- .27 PRE-MERGE ROUTINE (optional)
- .28 POST-MERGE ROUTINE (optional)
- .29 MERGE MAIL GROUP (optional)
- .31 MERGE MSG ROUTINE (optional)
- .33 MERGE DIRECTION INP TRANSFORM (optional)
- 1100 DUPLICATE TESTS (required)
- .01 DUPLICATE TEST (required)
- .02 ORDER OF TEST (required)
- .03 DUPLICATE TEST ROUTINE (required)
- .04 FILE FOR INFORMATION (optional)
- .05 FIELD TO BE CHECKED (required)
- .06 SUCCESSFUL MATCH WEIGHT (required)
- .07 UNSUCCESSFUL MATCH WEIGHT (required)
- 1200 DINUM FILES FOR MERGE (optional)
- .01 DINUM FILES FOR MERGE (optional)

#### Explanation of Fields in Logical Order of Entry

Selected fields are explained in the logical order of entry versus strict NUMERIC field order as follows:

#### .01 FILE TO BE CHECKED

Enter the file for which the developer wants to check and merge duplicates. You can only enter files that are also defined in the .01VARIABLE POINTER field of the DUPLICATE RECORD (#15) file. If the file you are interested in is *not* there, contact the Kernel Toolkit team for coordination.

#### .09 CANDIDATE COLLECTION ROUTINE

This field is updated with the name of the routine that the Duplicate Resolution Utilities executes to generate the list of potential duplicate candidates. The list of candidates is passed back to the merge shell in ^TMP(“XDRD”,\$J,file number. For example, if this is a patient merge utility, the candidate collection routine might pass back, to the merge shell, all patients who have the same last name as the record being processed, the same DOB as the record being processed, or who have the same or similar Social Security Number (SSN). This candidate collection routine is used to minimize the number of records the merge shell must process in determining potential duplicates.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/015.png) REF: For an example of a Candidate Collection routine, see the “<u>Candidate Collection Routine for Patient Merge Example</u>” section.

Selecting Fields to Compare in Candidate Collection:

- The developer needs to give this considerable thought as selecting wrong fields for candidate collection results in missed or many false potential duplicate candidates.
- The most important characteristic that a field should have is the probability of containing data. If a SSN field exists in a file but the field is rarely filled in, it would *not* be a good field from which to build candidates.
- Since selection of candidates deals with minimizing the set of records to test further, look at the whole file initially. It becomes desirable for the field to have a cross reference.
- Uniqueness of a field is also important. If all records contain one of two possible values (such as Male or Female), it makes little sense for you to select all records that are the same value as the record compared. However, such a field can be useful later in performing individual tests.
- One final point to keep in mind is, if you finally come up with very few fields to collect candidates on, you may need to be very liberal in the comparison. Furthermore, you might want to make more than one pass through the same field with different comparison logic, hoping to find additional records that you missed initially.

#### DUPLICATE TESTS

The developer *must* identify data items/fields to be used to assist in determining if a pair of records are duplicates. These items/fields *must* be single valued fields (that is data in Multiple fields is *not* supported), as follows:

#### .01 DUPLICATE TEST

This is a FREE TEXT name for the test (such as Name, SSN, and DOB).

#### .02 ORDER OF TEST

Enter in the NUMERIC value of the order you want the tests executed.

#### .03 DUPLICATE TEST ROUTINE

Enter the name of the routine that is called to do the actual comparison of the two records for a specific field.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/016.png) REF: For examples of duplicate test routines, see the “<u>Duplicate Test Routine Examples</u>” section.

| Variable                                   | Value                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------|
| XDRCD                                  | IEN of Record 1.                                                       |
| XDRCD2                                 | IEN of Record 2.                                                       |
| XDRFL                                  | File number being checked                                                  |
| XDRDTEST(XDRDTO)                       | Zero node of the test entry from the DUPLICATE RESOLUTION (#15.1) file |
| XDRDCD(XDRFL,XDRCD,field number,"I")   | Internal data value for this field for Record 1.                       |
| XDRDCD2(xdrfl,xdrcd2,field number,"I") | Internal data value for this field for Record 2.                       |
| XDRD("test score")                     | 0; This variable is used to pass the test score back to XDRDUP.    |

<span id="_Toc199951065" class="anchor"></span>Table 2: \$\$GETURL^XTHC10—Common HTTP Status Codes Returned

The successful maximum score can be obtained from the following:

\$P(XDRDTEST(xdrdto),U,6)

The unsuccessful score can be obtained from the following:

\$P(XDRDTEST(xdrdto),U,7)

Within the duplicate test routine, the developer can assign the entire successful match weight if both records’ data is the same, or he can assign a percentage of the match score if the data is similar, but *not* the same. For example, if Record 1 has a NAME of XUPATIENT,ONE-TWO and Record 2 has a NAME of XUPATIENT,ONE and the successful match weight for NAME is 50 points, this pair might be assigned 90% of the total 50 points. The developers must go through trial and error methods of changing and calculating the percent of the total match score that is assigned.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/017.png) REF: For examples of duplicate test routines, see the “<u>Duplicate Test Routine Examples</u>” section.

#### .04 FILE FOR INFORMATION

If the field that is being tested is *not* in the base file being checked, the developer *must* enter the file where the information is stored. For example, in the Indian Health Service (IHS) Patient Merge, the TRIBE OF MEMBERSHIP field is used for a duplicate test, and this data field is stored in the IHS PATIENT (#2) file. If no entry is made in this field, the Merge (Duplicate Resolution Utilities) assumes the base file.

#### .05 FIELD TO BE CHECKED

This field contains the field number of the data being used for this test. The developer *must* be aware that Multiple fields *cannot* be used for duplicate tests.

#### .06 SUCCESSFUL MATCH WEIGHT

This is the score, or total number of points assigned when a match is made on the data item being checked. This score can be anywhere from 0 to 99. The development team needs to determine the level of confidence associated with each test. The higher confidence fields would be assigned a greater successful match score than the lower confidence fields. For example, in a Patient Merge, if NAME matches exactly, a total of 60 points might be given, but if SEX or TRIBE OF MEMBERSHIP match exactly only 10 points is given. The total number of points between all the tests does *not* have to equal 100. The calculations to determine whether the pair is a potential duplicate is based on a percentage of the total possible score. If a data item is missing, it does *not* figure in the denominator in calculating the percentage.

#### .07 UNSUCCESSFUL MATCH WEIGHT

This is the score, or total number of points assigned when the data items for the two records being checked do *not* match. This score is normally a negative number. For example, if the DOB for the two records is different, a score of -40 might be assigned. This score can be anywhere from 0 to -99. The development team needs to determine the level of confidence associated with each test. The higher confidence fields would be assigned a greater negative unsuccessful match score than the lower confidence fields.

#### .15 POTENTIAL DUPLICATE THRESHOLD%

This is the possible percentage out of 100 after the accumulation of the test scores. If the final accumulated test score is equal to or greater than this percentage of the total possible points, the record pair is added to the DUPLICATE RECORD (#15) file as a potential duplicate pair. The percentage must be experimented with to find the best percentage to use. It is *recommended* that the percentage be set low at first and gradually increased to find the best possible percentage, so that you do *not* have many false negatives.

#### .25 MERGE STYLE

This determines whether the merge process is to be interactive or *not*. It is *highly recommended* that the merge be interactive. If it is interactive, the user can select fields from both the FROM and the TO (target) record. If *non*-interactive, all values are taken from the source record.

#### .11 DUPLICATE MANAGER MAIL GROUP

This field contains a POINTER to the mail group that receives messages in cases when the duplicate checking process could *not* be started. Some examples of conditions that would generate bulletins include:

- Test routine is *not* present.
- No entry in the DUPLICATE RESOLUTION (#15.1) file for this field.
- Global root node in ^DIC is undefined.

#### .16 VERIFIED DUPLICATE MAIL GROUP

This field contains a POINTER to the mail group that receives messages when a pair of records have been verified as duplicates. For example, in the case of a patient merge, there might be things that pharmacy or lab staff want to do before the two records are merged.

#### .17 VERIFIED DUPLICATE MSG ROUTINE

This field allows a software developer to send a customized bulletin notifying the Verified Duplicate Mail Group about verified duplicates. If nothing is entered, the Kernel Duplicate Resolution software sends a brief bulletin to the members of the mail group. This bulletin only provides the .01 value and the DFN numbers of the two records. The Duplicate Resolution software passes the XDRMFR and XDRMTO routines and it is up to this routine to gather any other information it wants to send in the bulletin and to send the bulletin to the Verified Duplicate Mail Group. A label entry point is allowed but you *must* use a hyphen (-) instead of the normal caret (^), such as ENTRY POINT-.

#### .29 MERGE MAIL GROUP

This field contains a POINTER to the mail group that receives messages when a pair of records have been merged. Generally, this is the same mail group as the VERIFIED DUPLICATE MAIL GROUP (#.16). These recipients can examine the merged-to record to make sure that all data transferred from the merged-from record successfully.

#### .31 MERGE MSG ROUTINE

This field allows a software developer to send a customized bulletin notifying the Merge Mail Group about merged duplicate pairs. If nothing is entered, the Kernel Duplicate Resolution software sends a brief bulletin to the members of the mail group. The Kernel Bulletin only provides the .01 values and the DFNs of the two records. The Duplicate Resolution software passes the XDRMFR and XDRMTO routines and it is up to the routine to gather any information it wants to send in the bulletin and to send the bulletin to the Merge Mail Group. A label entry point is allowed but you *must* use a hyphen (-) instead of the normal caret (^), such as ENTRY POINT-ROUTINE. This entry point is executed by the Duplicate Resolution software after transforming the - into a ^.

Also, this routine might very well need to be different from the VERIFIED DUPLICATE MSG ROUTINE (#.17), because the information that users need to see after the merge is different from before.

#### .18 VERIFIED DUPLICATE THRESHOLD%

If this field contains a percentage from 0 to 100, the Duplicate Resolution Utilities (XDR namespace) software automatically marks the two records as Verified Duplicates if the comparison score percentage is equal or greater to this value. This number, if entered, needs to be somewhat high, probably above 90% (such as IHS does *not* use this field in the case of the patient merge, because they would like human determination if the two records are indeed duplicates).

### Special Processing Routine Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Candidate Collection Routine for Patient Merge Example

<span id="_Toc199950740" class="anchor"></span>Figure 8: Special Processing Routine Examples—Candidate Collection Routine for Patient Merge

DPTDCAN ;IHS/OHPRD/JCM - GETS POSSIBLE DUPLICATE CANDIDATES ;09/16/93/ 08:19

;;1.0;DPTD;;

;

; Calls: EN^DIQ1

;

START ;

K ^TMP("XDRD",\$J,XDRFL),DPTDCAN

Q:\$P(^DPT(XDRCD,0),U,19)

D VALUE

D NAME

D SSN

D DOB

END D EOJ

Q

;

VALUE ;

S DIC=2,DA=XDRCD,DIQ(0)="I",DIQ="DPTDCAN",DR=".01;.03;.09"

D EN^DIQ1 K DIC,DA,DR,DIQ

Q

;

NAME ;Get patients with the same last name and first initial

G:DPTDCAN(XDRFL,XDRCD,.01,"I")'\]"" NAMEX

S DPTDCAN("NAME")=DPTDCAN(XDRFL,XDRCD,.01,"I")

S DPTDCAN("LNAME&FI")=\$P(DPTDCAN("NAME"),",",1)\_","\_\$E(\$P(DPTDCAN("NAME"

),",",2),1)\_"AAA"

S DPTDCAN("BNAME")=DPTDCAN("LNAME&FI")

F I=0:0 S DPTDCAN("BNAME")=\$O(^DPT("B",DPTDCAN("BNAME"))) Q:DPTDCAN("BNA

ME")=""!((\$P(DPTDCAN("NAME"),",",1)\_","\_\$E(\$P(DPTDCAN("NAME"),",",2),1)

)'=(\$P(DPTDCAN("BNAME"),",",1)\_","\_\$E(\$P(DPTDCAN("BNAME"),",",2),1)))

D

. S DPTDCAN("BNAMEDFN")=0 F S DPTDCAN("BNAMEDFN")=\$O(^DPT("B",DPTDCAN("

BNAME"),DPTDCAN("BNAMEDFN"))) Q:DPTDCAN("BNAMEDFN")="" S:DPTDCAN("BNAM

EDFN")'=XDRCD ^TMP("XDRD",\$J,XDRFL,DPTDCAN("BNAMEDFN"))="".

QNAMEX Q

;

SSN ;Get patients with same last four digits of ssn

G:DPTDCAN(XDRFL,XDRCD,.09,"I")'\]"" SSNX

S DPTDCAN("SSN")=DPTDCAN(XDRFL,XDRCD,.09,"I")

S DPTDCAN("L4SSN")=\$E(DPTDCAN("SSN"),6,9)

S DPTDCAN("BL4SSN")=XDRCD

F %=0:0 S DPTDCAN("BL4SSN")=\$O(^DPT("BS",DPTDCAN("L4SSN"),DPTDCAN("BL4SS

N"))) Q:'DPTDCAN("BL4SSN") S ^TMP("XDRD",\$J,XDRFL,DPTDCAN("BL4SSN"))=""

;

; Check SSNS with same first five digits

; Commented out the following line, is not specific enough for IHS

; but would be useful for the VA

;

;S DPTDCAN("F5SSN")=\$E(DPTDCAN("SSN"),1,5)\_"0000",DPTDCAN("5SSN")=DPTDCA

N("F5SSN") D

. F %=0:0 S DPTDCAN("5SSN")=\$O(^DPT("SSN",DPTDCAN("5SSN"))) Q:DPTDCAN("5

SSN")'=+DPTDCAN("5SSN")!(\$E(DPTDCAN("5SSN"),1,5)'=\$E(DPTDCAN("SSN"),1,5

)) S ^TMP("DPTDCAN",\$J,XDRFL,\$O(^DPT("SSN",DPTDCAN("5SSN"),"")))=""

. Q

SSNX Q

;

DOB ;Get patients with same date of birth

G:DPTDCAN(XDRFL,XDRCD,.03,"I")'\]"" DOBX

S DPTDCAN("DOB")=DPTDCAN(XDRFL,XDRCD,.03,"I")

S DPTDCAN("BDOB")=XDRCD

F %=0:0 S DPTDCAN("BDOB")=\$O(^DPT("ADOB",DPTDCAN("DOB"),DPTDCAN("BDOB"))

) Q:'DPTDCAN("BDOB") S ^TMP("XDRD",\$J,XDRFL,DPTDCAN("BDOB"))=""

;

;Transpose day of birth and get patients with same date of birth

;

S DPTDCAN("TDOB")=\$E(DPTDCAN("DOB"),1,5)\_\$E(DPTDCAN("DOB"),7)\_\$E(DPTDCAN

("DOB"),6)

S DPTDCAN("BDOB")=XDRCD

F %=0:0 S DPTDCAN("BDOB")=\$O(^DPT("ADOB",DPTDCAN("TDOB"),DPTDCAN("BDOB")

)) Q:'DPTDCAN("BDOB") S ^TMP("XDRD",\$J,XDRFL,DPTDCAN("BDOB"))=""

DOBX Q

;

EOJ ;

K DPTDCAN,%

Q

#### Duplicate Test Routine Examples

#### Name Test Routine for a Patient Merge Example

<span id="_Toc199950741" class="anchor"></span>Figure 9: Special Processing Routine Examples—Name Test Routine for a Patient Merge

DPTDN ;IHS/OHPRD/JCM;COMPARES NAMES; \[ 06/08/92 12:14 PM \]

;;1.0;DPTD;;AUG 13, 1991

;

; Calls: SOU^DICM1

;

START ;

D INIT

D NAME

I \$O(^DPT(XDRCD,.01,0)) D OTHER

END D EOJ

Q

;

EN ; EP - Entry Point for any routines comparing names

;

D INIT1

D COMPARE

D EOJ

Q

;

INIT ;

D EOJ

S DPTDN("MATCH")=\$P(XDRDTEST(XDRDTO),U,6)

S DPTDN("NO MATCH")=\$P(XDRDTEST(XDRDTO),U,7)

S DPTDN=\$G(XDRCD(XDRFL,XDRCD,.01,"I")),DPTDN2=\$G(XDRCD2(XDRFL,XDRCD2,.01

,"I"))

;

INIT1 S DPTDNL=\$P(DPTDN,","),DPTDNF=\$P(\$P(DPTDN,",",2)," "),DPTDNFI=\$E(DPTDNF)

,DPTDNM=\$P(\$P(DPTDN,",",2)," ",2),DPTDNMI=\$E(DPTDNM)

;

INIT2 S DPTDNL2=\$P(DPTDN2,","),DPTDNF2=\$P(\$P(DPTDN2,",",2)," "),DPTDNFI2=\$E(DP

TDNF2),DPTDNM2=\$P(\$P(DPTDN2,",",2)," ",2),DPTDNMI2=\$E(DPTDNM2)

Q

;

NAME ;

D COMPARE

D:\$O(^DPT(XDRCD2,.01,0)) OTHER2

Q

;

OTHER ;

F DPTDNO=0:0 S DPTDNO=\$O(^DPT(XDRCD,.01,DPTDNO)) Q:'DPTDNO S DPTDN=\$P(^

DPT(XDRCD,.01,DPTDNO,0),U,1) S:'\$D(DPTDN2) DPTDN2=XDRCD2(XDRFL,XDRCD2,.01,"I") D INIT1,NAME

Q

;

OTHER2 ;

F DPTDNO2=0:0 S DPTDNO2=\$O(^DPT(XDRCD2,.01,DPTDNO2)) Q:'DPTDNO2 S DPTDN

2=\$P(^DPT(XDRCD2,.01,DPTDNO2,0),U,1) D INIT2,COMPARE

Q

;

COMPARE ;

S:'\$D(DPTDN("TEST SCORE")) DPTDN("TEST SCORE")=DPTDN("NO MATCH")

I DPTDN=DPTDN2 S DPTDN("TEST SCORE2")=DPTDN("MATCH") G COMPAREX

I DPTDNF=DPTDNF2,DPTDNL=DPTDNL2 S DPTDN("TEST SCORE2")=DPTDN("MATCH")\*.8

G COMPAREX

I DPTDNFI=DPTDNFI2,DPTDNL=DPTDNL2 S DPTDN("TEST SCORE2")=DPTDN("MATCH")\*

.6 G COMPAREX

I DPTDNL=DPTDNL2 S DPTDN("TEST SCORE2")=DPTDN("MATCH")\*.4 G COMPAREX

S X=DPTDNL D SOU^DICM1 S DPTDNLS=X S X=DPTDNL2 D SOU^DICM1 S DPTDNL2S=X

S X=DPTDNF D SOU^DICM1 S DPTDNFS=X S X=DPTDNF2 D SOU^DICM1 S DPTDNF2S=X

I DPTDNLS=DPTDNL2S,DPTDNFS=DPTDNF2S S DPTDN("TEST SCORE2")=DPTDN("MATCH"

)\*.6 G COMPAREX

I DPTDNFS=DPTDNF2S S DPTDN("TEST SCORE2")=DPTDN("MATCH")\*.2 G COMPAREX

S DPTDN("TEST SCORE2")=DPTDN("NO MATCH")

COMPAREX ;

S:DPTDN("TEST SCORE2")\>(DPTDN("TEST SCORE")) DPTDN("TEST SCORE")=DPTDN("

TEST SCORE2")

K X,DPTDNLS,DPTDNL2S,DPTDNFS,DPTDNF2S,DPTDN("TEST SCORE2")

Q

;

EOJ ;

S:\$D(DPTDN("TEST SCORE")) XDRD("TEST SCORE")=DPTDN("TEST SCORE")

K DPTDN,DPTDN2,DPTDNF,DPTDNF2,DPTDNL,DPTDNL2,DPTDNM,DPTDNM2

K DPTDNMI,DPTDNMI2,DPTDNFI,DPTDNFI2,DPTDNO,DPTDNO2

Q

#### Date of Birth test Routine for a Patient Merge Example

<span id="_Toc199950742" class="anchor"></span>Figure 10: Special Processing Routine Examples—Date of Birth Test Routine for a Patient Merge

DPTDOB ;IHS/OHPRD/JCM;COMPARES DATE OF BIRTHS; \[ 06/08/92 12:10 PM \]

;;1.0;DPTD;;AUG 13, 1991

START ;

D INIT

EN ; EP - Entry point for comparing dates

D COMPARE

END D EOJ

Q

;

INIT ;

K DPTDOB,DPTDOB2

S DPTDOB=\$G(XDRCD(XDRFL,XDRCD,.03,"I")),DPTDOB2=\$G(XDRCD2(XDRFL,XDRCD2,.

03,"I"))

S DPTDOB("MATCH")=\$P(XDRDTEST(XDRDTO),U,6)

S DPTDOB("NO MATCH")=\$P(XDRDTEST(XDRDTO),U,7)

Q

;

COMPARE ;

I DPTDOB'\]""!(DPTDOB2'\]"") G COMPAREX

I DPTDOB=DPTDOB2 S XDRD("TEST SCORE")=DPTDOB("MATCH") G COMPAREX

S DPTDOB("CNT")=0

F DPTDOBI=1:1:7 Q:DPTDOB("CNT")\>2 I \$E(DPTDOB,DPTDOBI)'=\$E(DPTDOB2,DPTD

OBI) S DPTDOB("CNT")=DPTDOB("CNT")+1

K DPTDOBI

S XDRD("TEST SCORE")=\$S(DPTDOB("CNT")\>2:DPTDOB("NO MATCH"),1:(DPTDOB("MA

TCH")\*.8))

COMPAREX Q

;

EOJ ;

K DPTDOB,DPTDOB2

Q

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EN^XDRMERG(): Merge File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Duplicate Record Merge

ICR \#: 2365

Description: The EN^XDRMERG API provides for merging of one or more pairs of records in a specified file. This API takes two (2) arguments:

- File number (a NUMERIC value).
- Closed reference to the location where the program finds an array with subscripts indicating the record pairs to be merged (a text value).

Format: EN^XDRMERG(file,arraynam)

Input Parameters: file: (required) Specifies the file number of the file in which the indicated entries are to be merged.

Input/OutputParameter: arraynam: (required) This parameter contains the name of the array as a closed root under which the subscripts indicating the FROM and TO entries are found. The data can have either two or four subscripts descendent from the array, which is passed.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/018.png) REF: For examples of its usage, see the “<u>Overview</u>” section.

#### Examples

The following command would result in record pairs specified as subscripts in the array MYLOC to be merged in a hypothetical file \#999000014:

D EN^XDRMERG(999000014,"MYLOC")

The MYLOC array might have been set up prior to this call in the following manner (or any equivalent way) where the subscripts represent the internal entry numbers of the FROM and TO records, respectively.

S MYLOC(147,286)="",MYLOC(182,347)="",MYLOC(2047,192)=""S MYLOC(837,492)="",MYLOC(298,299)=""

This would result in five record pairs being merged with record 147 (the FROM record) being merged into record 286 (the TO record), record 182 being merged into record 347, and so on, to record 298 being merged into 299. Merges using the two subscript format occurs without a specific record of the entries prior to the merge (The internal entry numbers merged would be recorded under the file number in XDR REPOINTED ENTRY \[#15.3\] file) An alternative is a four subscript format for the data array that uses VARIABLE POINTER formats for the FROM and TO records as the third and fourth subscripts. If the merge is performed with this four subscript array, then a pre-merge image of the data of both the FROM and TO records in the primary file and all other merged files (those related by DINUM) and information on all single value POINTER values modified is stored in the MERGE IMAGE (#15.4) file.

For the sample data above \[if the global root for the hypothetical File \#999000014 is ^DIZ(999000014,\] the four subscript array might be generated using the following code:

<span id="_Toc199950743" class="anchor"></span>Figure 11: EN^XDRMERG API—Example

S MYROOT=";DIZ(99900014," \<--- note the leading ^ is omitted

S MYLOC(147,286,147_MYROOT,286_MYROOT)=""

S MYLOC(182,347,182_MYROOT,347_MYROOT)=""

S MYLOC(2047,192,2047_MYROOT,192_MYROOT)=""

S MYLOC(837,492,837_MYROOT,492_MYROOT)=""

S MYLOC(298,299,298_MYROOT,299_MYROOT)=""

;

D EN^XDRMERG(99900014,"MYLOC")

Exclusion of Multiple Pairs For a Record—To insure that there are no unanticipated problems due to relationships between a specific record in multiple merges, prior to merging any data the various FROM and TO records included in the process are examined, and if one record is involved in more than one merge, all except the first pair of records involving that one are excluded from the merge. If any pairs are excluded for this reason, a mail message is generated to the individual responsible for the merge process as indicated by the DUZ.

If the following entries were included in the MYLOC array:

MYLOC(128,247)

MYLOC(128,536) and

MYLOC(247,128)

Only the first of these entries (based on the numeric sorting of the array) would be permitted to remain in the merge process, while the other two pairs would be omitted). And although it may seem unlikely that someone would indicate that a record should be merged into two different locations, while another location should be merged into one that was merged away, if the pairs are selected automatically and checks are *not* included to prohibit such behavior, they show up. That is why the merge process does *not* include more than one pair with a specific record in it.

#### Problems Related To Data Entry While Merging

The Merge Process has been designed to combine data associated with the two records in the manner described above. On occasion, however, there are problems that cause VA FileMan to reject the data that is being entered. This may happen for several reasons. Some examples that have been observed include:

- Clinics that had been changed so they no longer were indicated as Clinics (so they would *not* add to the number that people had to browse through to select a clinic) but were rejected since the input transform checked that they be clinics.
- POINTER values that no longer had a valid value in the pointed to file (dangling POINTERs).
- Fields that have input transforms that prohibit data entry.

It is possible to use a validity checker on your data prior to initiating the actual merge process (this is the action taken by merges working from the Potential Duplicate file). The data pairs are processed in a manner like the actual merge, so only that data in any of the files that would be merged and for which the data would be entered using VA FileMan utilities for the specific pair are checked to insure they pass the input transform. Any problems noted are incorporated into a mail message for resolution prior to attempting to merge the pair again, and the pair is removed from the data array that was passed in. Pairs that pass through this checking should *not* encounter any data problems while being merged.

### RESTART^XDRMERG(): Restart Merge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Duplicate Record Merge

ICR \#: 2365

Description: The RESTART^XDRMERG API restarts a merge that has been stopped. The information necessary for restarting can be viewed using the CHKLOCAL^XDRMERG2 API (see LOCAL MERGE STATUS).

Format: RESTART^XDRMERG(file,arraynam,phase,currfile,currien)

Input Parameters: file: (required) Specifies the file number of the file in which the indicated entries are to be merged.

arraynam: (required) This parameter contains the name of the array as a closed root under which the subscripts indicating the FROM and TO entries are found. The data can have either two or four subscripts descendent from the array, which is passed.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/019.png) REF: For examples of its usage, see the “<u>Overview</u>” section in the "<u>Toolkit—Duplicate Record Merge</u>" section.

phase: (required) This parameter indicates the phase of the merge process in which the merge should be restarted. The value is a number in the range of 1 to 3, with no decimal places:

- Phase 1 is usually quite short and is the merge of the specified entries in the primary file.
- Phase 2 is the merging of entries in files that are DINUMed to the primary file and changing POINTERs that can be identified from cross-references.
- Phase 3 is finding POINTER values by searching each entry in a file. This is usually the longest phase of the merge process.

currfile: (required) This is the current file number on which the merge process is operating.

currien: (required) This is the current internal entry number in the file on which the merge process is operating.

Output: none.

### SAVEMERG^XDRMERGB(): Save Image of Existing and Merged Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Toolkit—Duplicate Record Merge

ICR \#: 2338

Description: During special processing related to the Patient Merge, the IBAXDR routine needs to call the SAVEMERG^XDRMERGB API. The SAVEMERG^XDRMERGB API saves the file image of an entry involved in the merge process when only one of the entries (the entry being merged or the entry being merged into) is present in the filenum input parameter. Normally, the merge process would handle when it can identify a FROM or a TO entry that is *not* present based on the DINUMed values. For filenum, however, the internal entry numbers are determined from the “B”-cross-reference, and missing entries need to be handled separately.

This API acts to save an image of the currently existing data for the merge entry and merged into entry in the MERGE IMAGE (#15.4) file.

Format: SAVEMERG^XDRMERGB(filenum,ienfrom\[,iento\])

Input Parameters: filenum: (required) This is the file number for the file that is being merged and for which the images are to be saved.

ienfrom: (required) The internal entry number of the FROM entry (the entry being merged into another entry).

iento: (optional) The internal entry number of the TO entry (the entry into which the entry is being merged).

Output: results: Stored image.

## Toolkit—HTTP Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Toolkit Hypertext Transfer Protocol (HTTP) Client Helper software release adds a new tool in a set of Infrastructure software tools that developers can use. HTTP is a fast and reliable way for an application to collect data from another source. Kernel Toolkit patch XT\*7.3\*123 allows VistA to t into this information and retrieve Web data.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/020.png) NOTE: Kernel Toolkit patch XT\*7.3\*138 adds support for IPv6, HTTP/1.1, and HTTPS.

This code was originally developed by another VistA application that had a pressing need for this capability. The Kernel Toolkit development team is providing and maintaining it as generic tool so that other developers may use its functionality for their needs. For example:

- KIDS: Uses it to get the checksums from FORUM of patches that are sent in a Host File System (HFS) file.
- Pharmacy: Uses it to request the printing of FDA data sheets.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/021.png) NOTE: XTHC\* routines are part of the HTTP Client Helper application for developers.

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \$\$GETURL^XTHC10: Return URL Data Using HTTP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—HTTP Client Helper

ICR \#: 5553

Description: The \$\$GETURL^XTHC10 extrinsic function is a Hypertext Transfer Protocol (HTTP)/1.1 client that can request a Web page from another system and pass the returned data to the calling routine.

It can make both GET and POST requests.

It is the main API and returns in xt8rdat the returned data from the website.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/022.png) NOTE:XTHC\* routines are part of the HTTP Client Helper application for developers.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/023.png) NOTE: This API was released with Kernel Toolkit patch XT\*7.3\*123.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/024.png) NOTE: This API is IPv6 compliant as of Kernel Toolkit patch XT\*7.3\*138.

Format:

\$\$GETURL^XTHC10(url\[,xt8flg\],xt8rdat,.xt8rhdr\[,xt8sdat\]\[,.xt8shdr\]\[,.xt8meth\])

Input Parameters: url: (required) This is the Universal Resource Locator (URL) to access (http://host:port/path). It could be as simple as "www.va.gov".

xt8flg: (optional) Request timeout. Default is 5 seconds.

xt8sdat: (optional) Closed root of a variable containing the body of the request message. Data should be formatted as described in the xt8rdat parameter.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/025.png) NOTE: If this parameter is defined (that is *not* empty) and the referenced array contains data, then the POST request is generated; otherwise, the GET request is sent.

.xt8shdr: (optional) Reference to a local variable containing header values, which is added to the request. For example:

XT8SHDR("CONTENT-TYPE")="text/html".xt8meth: (optional) Flag to indicate the request method:

- GET—Default if xt8sdat contains no data.
- POST—Default if xt8sdat contains data.
- HEAD
- PUT
- OPTIONS
- DELETE
- TRACEOutput / OutputParameters: xt8rdat: (required) Closed root of the variable where the message body is returned. Data is stored in consecutive nodes (numbers starting from 1). If a line is longer than 245 characters, only 245characters are stored in the corresponding node. After that, overflow sub-nodes are created. For example:

@XT8DATA@(1)="\<html\>"  
 @XT8DATA@(2)="\<head\>\<title\>VistA\</title\>\</head\>"  
 @XT8DATA@(3)="\<body\>"  
 @XT8DATA@(4)="\<p\>"  
 @XT8DATA@(5)="Beginning of a very long line"  
 @XT8DATA@(5,1)="Continuation \#1 of the long line"  
 @XT8DATA@(5,2)="Continuation \#2 of the long line"  
 @XT8DATA@(5,...)=...  
 @XT8DATA@(6)="\</p\>"

.xt8rhdr: (required) Reference to a local variable where the parsed headers are returned. Header names are converted to uppercase; the values are left “as is”. The root node contains the status line. For example:

XT8HDR="HTTP/1.1 200 OK"  
XT8HDR("ACCEPT-RANGES")="bytes"  
XT8HDR("CONNECTION")="close"  
XT8HDR("CONTENT-LENGTH")="16402"  
XT8HDR("CONTENT-TYPE")="text/html; charset=UTF-8"  
XT8HDR("DATE")="Thu, 25 Jun 2015 14:43:01 GMT"  
XT8HDR("ETAG")="a93a2-4012-5180156550680"  
XT8HDR("LAST-MODIFIED")="Mon, 08 Jun 2015 13:08:26 GMT"  
XT8HDR("SERVER")="Apache/2.2.15 (CentOS)"

Output: returns: Returns:

- Success: HTTP_Status_Code^Description  
  >   
  > Common HTTP status codes returned:

| Status Code | Description                   |
|-------------|-------------------------------|
| 200         | OK                            |
| 301         | Moved Permanently             |
| 400         | Bad Request                   |
| 401         | Unauthorized                  |
| 404         | Not Found                     |
| 407         | Proxy Authentication Required |
| 408         | Request Time-out              |
| 500         | Internal Server Error         |
| 505         | HTTP Version *not* supported  |

<span id="_Ref212540468" class="anchor"></span>Table 3: Parameter Tool—Parameter Entity Levels

- Fail:-1^Error Descriptor  
  >   
  > Additional error information can be found in the VistA error trap or ^XTER in Programmer mode.

> ![](kernel-8-0-developer-s-guide-toolkit-user-guide/026.png) REF: For more details, visit the [HTTP Frequently Asked Questions (FAQ) website](http://www.faqs.org/rfcs/rfc1945.html) or the Internet Engineering Task Force (IETF) sites at [HTTP/1.1](http://www.ietf.org/rfc/rfc2616.txt) and [HTTP Authentication](http://www.ietf.org/rfc/rfc2617.txt).

### \$\$ENCODE^XTHCURL: Encodes a Query String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—HTTP Client Helper

ICR \#: 5554

Description: The \$\$ENCODE^XTHCURL extrinsic function encodes the query string. The <u>\$\$MAKEURL^XTHCURL: Creates a URL from Components</u> API uses this extrinsic function.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/027.png) NOTE: This API was released with Kernel Toolkit patch XT\*7.3\*123.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/028.png) NOTE:XTHC\* routines are part of the HTTP Client Helper application for developers.

Format: \$\$ENCODEURL^XTHCURL(str)

Input Parameters: str: (required) String of data to be encoded.

Output: returns: Returns:

- Success: Encoded query string.
- Fail:-1^String *not* defined (if missing str parameter).

#### Example

<span id="_Toc199950744" class="anchor"></span>Figure 12: \$\$ENCODE^XTHCURL API—Example

\><span class="mark">W \$\$ENCODE^XTHCURL("123+main+st.,Anycity,CA")</span>

123%2Bmain%2Bst.%2CAnycity%2CCA

### \$\$MAKEURL^XTHCURL: Creates a URL from Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—HTTP Client Helper

ICR \#: 5554

Description: The \$\$MAKEURL^XTHCURL extrinsic function creates a URL from components.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/029.png) NOTE:XTHC\* routines are part of the HTTP Client Helper application for developers.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/030.png) NOTE: This API is IPv6 compliant as of Kernel Toolkit patch XT\*7.3\*138.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/031.png) NOTE: This API was released with Kernel Toolkit patch XT\*7.3\*123.

Format: \$\$MAKEURL^XTHCURL(host\[,port\]\[,path\]\[,.query\])

Input Parameters: host: (required) The Fully Qualified Domain Name (FQDN) or Internet Protocol (IP) address of the system to which it connects.

port: (optional) The port to use. Default is:

- HTTP—Port \<REDACTED\>.
- HTTPS—Port \<REDACTED\>.

path: (optional) The path to the Web page on the called server.

.query: (optional) An array of query parameters.

Output: returns: Returns:

- Success: Normalized path (see <u>Example</u>).
- Fail:-1^Host *not* defined (if missing host parameter).

#### Example

<span id="_Toc199950745" class="anchor"></span>Figure 13: \$\$MAKEURL^XTHCURL API—Example

<span class="mark">S host="http://www.map.com"</span><span class="mark">S path="api/staticmap"</span><span class="mark">S query("center")="main+st.,Anycity,CA"</span><span class="mark">S query("sensor")="false"</span><span class="mark">W \$\$MAKEURL^XTHCURL(host,,path,.query)</span>

http://www.map.com/api/staticmap?center=main%2Bst.%2CAnycity%2CCA&sensor=false

### \$\$PARSEURL^XTHCURL: Parses a URL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—HTTP Client Helper

ICR \#: 5554

Description: The \$\$PARSEURL^XTHCURL extrinsic function parses a URL using into host, port, and path (path includes query string).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/032.png) NOTE:XTHC\* routines are part of the HTTP Client Helper application for developers.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/033.png) NOTE: This API was released with Kernel Toolkit patch XT\*7.3\*123.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/034.png) NOTE: This API is IPv6 compliant as of Kernel Toolkit patch XT\*7.3\*138.

Format: \$\$PARSEURL^XTHCURL(url,.host,.port,.path)

Input Parameters: url: (required) Reference to variable where host name is to be returned.

Output Parameters: host: (required) Input URL.

port: (required) Reference to variable where port is to be returned.

.path: (required) Reference to variable where path string is to be returned.

Output: returns: Returns:

- Success: 0
- Fail: -1^Error Description

#### Example

<span id="_Toc199950746" class="anchor"></span>Figure 14: \$\$PARSEURL^XTHCURL API—Example

<span class="mark">D PARSEURL^XTHCURL("http://\<REDACTED\>.va.gov:9999/tpl/PKG",.ZH,.ZP,.ZA)</span><span class="mark">W ZH,!,ZP,!,ZA</span>

\<REDACTED\>.va.gov

9999

/tpl/PKG

### \$\$DECODE^XTHCUTL: Decodes a String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—HTTP Client Helper

ICR \#: 5555

Description: The \$\$DECODE^XTHCUTL extrinsic function is used with the HTTP/1.1 Client. It decodes one string replacing the following:

- &lt; with \<
- &gt; with \>
- &amp; with &
- &nbsp; with “ ” (a space)
- &os; with ‘
- &quot; with “
- &#65; with A

![](kernel-8-0-developer-s-guide-toolkit-user-guide/035.png) NOTE:XTHC\* routines are part of the HTTP Client Helper application for developers.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/036.png) NOTE: This API was released with Kernel Toolkit patch XT\*7.3\*123.

Format: \$\$DECODE^XTHCUTL(str)

Input Parameters: str: (required) String to be decoded.

Output: returns: Returns:

- Success: Decoded string.
- Fail:-1^String *not* defined (if missing str parameter).

#### Example

<span id="_Toc199950747" class="anchor"></span>Figure 15: \$\$DECODE^XTHCUTL API—Example

<span class="mark">\$\$DECODE^XTHCUTL("123%2Bmain%2Bst.%2CAnytown%2CCA")</span>

 123%2Bmain%2Bst.%2CAnytown%2CCA

## Toolkit—KERMIT APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RFILE^XTKERM4: Add Entries to Kermit Holding File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—KERMIT

ICR \#: 2075

Description: The RFILE^XTKERM4 API allows access to the KERMIT HOLDING (#8980) file and the API that adds entries to it, RFILE^XTKERM4. Check the “AOK” cross-reference of the KERMIT HOLDING (#8980) file to see if the user has an entry in the KERMIT HOLDING (#8980) file. If *not*, call RFILE^XTKERM4 to add an entry to the file.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/037.png) NOTE: A call to RFILE^XTKERM4 allows a user to add or select an entry in the KERMIT HOLDING (#8980) file.

Format: RFILE^XTKERM4

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
11. Set all input variables.
12. Call the API.

Output Variables: XTKDIC: This variable returns the global root and is a calling variable used by calls to [RECEIVE^XTKERMIT: Load a File into the Host](#receivextkermit-load-a-file-into-the-host) or <u>SEND^XTKERMIT: Send Data from Host</u> APIs.

XTMODE: This variable is returned. It is used as input to calls to RECEIVE^XTKERMIT: Load a File into the Host or <u>SEND^XTKERMIT: Send Data from Host</u> APIs.

### RECEIVE^XTKERMIT: Load a File into the Host

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—KERMIT

ICR \#: 10095

Description: The RECEIVE^XTKERMIT API loads a file into the host.

Format: RECEIVE^XTKERMIT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
13. Set all input variables.
14. Call the API.

Variables to call from outside of Kermit:XTKDIC: (required) Set XTKDIC to VA FileMan type global root.

DWLC: (required) Set DWLC to last current data node.

Return DWLC to last data node, XTKDIC is KILLed.

TIREF: (optional) Set XTKMODE as follows to send/receive:

- 0—Send/Receive in IMAGE mode (no conversion).
- 1—Send/Receive in DATA mode (just convert control character).
- 2—Send/Receive as TEXT (VA FileMan WORD-PROCESSING). Text mode sends a carriage return (CR) after each global node; makes a new global node for each CR received. XTKMODE set to 2 would be normal for most VistA applications.

### SEND^XTKERMIT: Send Data from Host

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—KERMIT

ICR \#: 10095

Description: The SEND^XTKERMIT API sends data from the host.

Format: SEND^XTKERMIT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
15. Set all input variables.
16. Call the API.

Variables to call from outside of KERMIT:XTKDIC: (required) Set XTKDIC to VA FileMan type global root.

DWLC: (required) Set DWLC to last current data node.

Return DWLC to last data node; XTKDIC is KILLed.

TIREF: (optional) Set XTKMODE as follows to send/receive:

- 0—Send/Receive in IMAGE mode (no conversion).
- 1—Send/Receive in DATA mode (just convert control character).
- 2—Send/Receive as TEXT (VA FileMan WORD-PROCESSING). Text mode sends a carriage return (CR) after each global node; makes a new global node for each CR received. XTKMODE set to 2 would be normal for most VistA applications.

## Toolkit—Multi-Term Look-Up (MTLU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How to Override

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If files are fully configured for the special Multi-Term Look-Up, all standard VA FileMan lookups invoke MTLU. The following procedures can be taken to override MTLU::

- Users can enter an accent grave (\`) as a prefix to request a lookup by the Internal Entry Number (IEN).
- Users can enter a tilde (~) as a prefix to force a standard VA FileMan lookup.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/038.png) NOTE: If a search produces no matches, MTLU continues with a standard VA FileMan search by default.

- Developers can override MTLU by setting the variable XTLKUT=“” prior to referencing the file and KILLing it upon exit, or set DIC(0) to include I:

S DIC=81,DIC(0)="AEMQI",X="" D ^DIC

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MTLU and VA FileMan Supported Calls

Developers can perform any supported VA FileMan calls on files fully configured for MTLU.

The preferred method of performing lookups from Programmer mode is to add the target file to the LOCAL LOOKUP (#8984.4) file and call LKUP^XTLKMGR. However, Multi-Term Look-Ups can be performed on any VA FileMan file, even if it has *not* been configured for use by MTLU. Using the developer API, the lookup can be performed using any index contained within the file, such as a VA FileMan KWIC cross-reference.

Entry Point: XTLKKWL

Required Input Variables:(XTLKGBL, XTLKKSCH(“GBL”)): This is the global root (same as DIC).

XTLKKSCH(“DSPLY”): This variable displays the routine. For example:

DGEN^XTLKKWLD

> XTLKKSCH(“INDEX”): Cross-reference selected by the developer for performing a multi-term lookup.

XTLKX: This is the user input.

Optional Input Variables:XTLKSAY: This variable equals 1 or 0. If XTLKSAY = 1, MTLU displays details during the lookup.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/039.png) NOTE: The purpose of XTLKSAY is to control the degree of output to the screen, *not* the amount of “file information” displayed.

XTLKHLP: Executable code to display custom help.

#### Kernel Toolkit Enhanced APIs

Programmer calls to MTLU-configured files return all standard VA FileMan variables (that is Y, DTOUT, DUOUT, DIROUT, and DIRUT).

The programmer’s API for performing a lookup has been enhanced functionally, simplified, and converted to a procedure call.

Procedure calls provide full, *non*-interactive management of the following MTLU control files:

- LOCAL KEYWORD (#8984.1)
- LOCAL SHORTCUT (#8984.2)
- LOCAL SYNONYM (#8984.3)
- LOCAL LOOKUP (#8984.4)

All procedure calls are contained in the routine ^XTLKMGR.

Errors are returned in the XTLKER() array. KILL this array *before* calling any of these new procedure calls and check the array after returning from the calls. All calls require that the target file be defined in the LOCAL LOOKUP (#8984.4) file. If removing an entry from the LOCAL LOOKUP (#8984.4) file, all shortcuts, synonyms, and keywords associated with that file *must* be deleted first.

### XTLKKWL^XTLKKWL: Perform Supported VA FileMan Calls on Files Configured for MTLU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10122

Description: The XTLKKWL^XTLKKWL API lets developers perform any supported VA FileMan calls on files configured for MTLU. To ignore the special lookup routine, XTLKDICL, be sure that DIC(0) includes an I. Alternatively, multi-term lookups can be performed on any VA FileMan file, even if it has *not* been configured for primary use by MTLU. Using the API, the lookup can be performed using any index contained within the file, such as a VA FileMan Key Word In Context (KWIC) cross-reference.

Format: XTLKKWL^XTLKKWL

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
17. Set all input variables.
18. Call the API.

Input Variables: (XTLKGBL, XTLKKSCH(“GBL”)): (required) This is the global root (same as DIC).

XTLKKSCH(“DSPLY”): (required) This variable displays the routine. For example:

DGEN^XTLKKWLDXTLKKSCH(“INDEX”): (required) Cross-reference selected by the developer for performing a MTLU.

XTLKX: (required) This is the user input.

XTLKSAY: (optional) XTLKSAY values:

- 1—MTLU displays details during the lookup.
- 0.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/040.png) NOTE: The purpose of XTLKSAY variable is to control the degree of output to the screen, *not* the amount of “file information” displayed.

XTLKHLP: (optional) XTLKHLP=Executable code to display custom help.

### DK^XTLKMGR(): Delete Keywords from the Local Keyword File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The DK^XTLKMGR API deletes keywords from the LOCAL KEYWORD (#8984.1) file.

Format: DK^XTLKMGR(xtlk1,xtlk2)

Input Parameters: xtlk1: (required) File name.

xtlk2: (required) Leave this parameter undefined to delete *all* keywords for a given target file or pass in an array for *selected* keywords.

Output: none.

### DLL^XTLKMGR(): Delete an Entry from the Local Lookup File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The DLL^XTLKMGR API deletes an entry from the LOCAL LOOKUP (#8984.4) file.

Format: DLL^XTLKMGR(xtlk1)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
19. Set all input variables.
20. Call the API.

Input Parameters: xtlk1: (required) The associated file name or number.

OutputVariables: XTLKER(1,FILENAME): File is *not* in the LOCAL LOOKUP (#8984.4) file.

XTLKER: Entries exist for keywords, shortcuts, or synonyms for the associated file. These *must* be deleted first.

### DSH^XTLKMGR(): Delete Shortcuts from the Local Shortcut File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The DSH^XTLKMGR API deletes shortcuts from the LOCAL SHORTCUT (#8984.2) file.

Format: DSH^XTLKMGR(xtlk1,xtlk2)

Input Parameters: xtlk1: (required) File name.

xtlk2: (required) Leave this parameter undefined to delete all shortcuts for a given target file or pass in an array for selected shortcuts.

Output: none.

### DSY^XTLKMGR(): Delete Synonyms from the Local Synonym File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The DSY^XTLKMGR API deletes synonyms from the LOCAL SYNONYM (#8984.3) file.

Format: DSY^XTLKMGR(xtlk1,xtlk2)

Input Parameters: xtlk1: (required) File name.

xtlk2: (required) Leave this parameter undefined to delete *all* synonyms for a given target file or pass in an array for *selected* synonyms.

Output: none.

### K^XTLKMGR(): Add Keywords to the Local Keyword File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The K^XTLKMGR API adds Keywords to the LOCAL KEYWORD (#8984.1) file.

Format: K^XTLKMGR(xtlk1,xtlk2,xtlk3)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
21. Set all input variables.
22. Call the API.

Input Parameters: xtlk1: (required) Associated file.

xtlk2: (required) Code in the associated file.

xtlk3: (required) Keyword.

Output Variables: XTLKER(1,FILENAME): File *not* defined in the LOCAL LOOKUP (#8984.4) file.

XTLKER(2,CODE): The code is *not* in the associated file.

XTLKER(3,SYNONYM): The keyword could *not* be added.

### L^XTLKMGR(): Define a File in the Local Lookup File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The L^XTLKMGR API defines a file in the LOCAL LOOKUP file (8984.4). Adding the target file here does *not* automatically place the special lookup routine, ^XTLKDICL, in the file’s Data Dictionary. Since use of this routine is at the discretion of the developer, it should be manually added using the Edit File option under VA FileMan’s Utilities Menu.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/041.png) REF: For information on the Edit File option, see the “Utility Functions” section in the *VA FileMan User Manual*.

Format: L^XTLKMGR(xtlk1\[,xtlk2\],xtlk3,xtlk4)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
23. Set all input variables.
24. Call the API.

Input Parameters: xtlk1: (required) File name or number.

xtlk2: (optional) Application-specific display protocol.

xtlk3: (required) MTLU index to use for lookups.

xtlk4: (required) Variable pointer prefix.

Output Variables: XTLKER(1,FILENAME): File could *not* be added.

The following are examples (index and prefix can differ from actual implementation):

- For the ICD DIAGNOSIS (#80) file:

\>K XTLKER  
\>D L^XTLKMGR(80,"DSPLYD^XTLKKWLD","AIHS","D")

- For the ICD OPERATION/PROCEDURE (#80.1) file:

\>K XTLKER  
\>D L^XTLKMGR(80.1,"DSPLYO^XTLKKWLD","KWIC","O")

### LKUP^XTLKMGR(): General Lookup Facility for MTLU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The LKUP^XTLKMGR API adds terms and synonyms to the LOCAL SYNONYM (#8984.3) file.

Format: LKUP^XTLKMGR(fil,xtlkx\[,xtlksay\]\[,xtlkhlp\]\[,xtlkmore\])

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
25. Set all input variables.
26. Call the API.

Input Parameters: fil: (required) Target file (*must* be defined in the LOCAL LOOKUP (#8984.4) file.

xtlkx: (required) Word or phrase to use in lookup.

xtlksay: (optional) Set to any of the following:

- 1 (default) or “”—Full screen (normal) display.
- -1—Prevents screen display.
- 0—Minimize screen display.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/042.png) NOTE: The purpose of xtlksay is to control the degree of output to the screen, *not* the amount of “file information” displayed.  
  
If screen displays are turned off, MTLU matches can be processed by checking the count in ^TMP(“XTLKHITS”,\$J). ^TMP(“XTLKHITS”,\$J,count)=IEN of the entry in the target file. ^TMP(“XTLKHITS”) should be killed after processing.

xtlkhlp: (optional) The lookup was successful.

xtlkmore: (optional) Set to 1 to continue with VA FileMan search (default=1).

Output Variables: Y=-1: File *not* defined in the LOCAL LOOKUP (#8984.4) file.

Y=N^S:N is the internal entry number (IEN) of the entry in the file and S is the value of the .01 field for that entry.

Y=N^S^1:N and S are defined as above and the 1 indicates that this entry has just been added to the file.

#### Examples

#### Example 1

<span id="_Toc200270048" class="anchor"></span>Figure 16: LKUP^XTLKMGR API—Example 1: Standard Lookup; Single Term Entered

VAH,MTL\><span class="mark">D LKUP^XTLKMGR(80,"MALIG") \<Enter\></span>

( MALIG/MALIGNANT )

..........................................................................

..........................................................................

...........................................

The following 443 matches were found:

1: 140.1 (MAL NEO LOWER VERMILION)

MALIGNANT NEOPLASM OF LOWER LIP, VERMILION BORDER

2: 140.3 (MAL NEO UPPER LIP, INNER)

MALIGNANT NEOPLASM OF UPPER LIP, INNER ASPECT

3: 140.4 (MAL NEO LOWER LIP, INNER)

MALIGNANT NEOPLASM OF LOWER LIP, INNER ASPECT

4: 140.5 (MAL NEO LIP, INNER NOS)

MALIGNANT NEOPLASM OF LIP, UNSPECIFIED, INNER ASPECT

5: 140.6 (MAL NEO LIP, COMMISSURE)

MALIGNANT NEOPLASM OF COMMISSURE OF LIP

Press \<RET\> or Select 1-5: <span class="mark">^ \<Enter\></span>

...Nothing selected. Attempting Fileman lookup.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/043.png) NOTE: Pressing the \<Enter\> key continues listing the MTLU matches. If no selection is made, MTLU initiates a standard VA FileMan lookup (using all available cross-references).

#### Example 2

<span id="_Toc200270049" class="anchor"></span>Figure 17: LKUP^XTLKMGR API—Example 2: Standard Lookup; Multiple Terms Entered

VAH,MTL\><span class="mark">D LKUP^XTLKMGR(80,"MALIGNANCY OF THE LIP") \<Enter\></span>

(LIP/LIPIDOSES/LIPODYSTROPHY/LIPOID/LIPOMA/LIPOPROTEIN/LIPOTROPIC/LIPS MALIGNAN/MALIGNANT)

The following words were not used in this search:

OF

THE

............

The following 12 matches were found:

1: 140.1 (MAL NEO LOWER VERMILION)

MALIGNANT NEOPLASM OF LOWER LIP, VERMILION BORDER

2: 140.3 (MAL NEO UPPER LIP, INNER)

MALIGNANT NEOPLASM OF UPPER LIP, INNER ASPECT

3: 140.4 (MAL NEO LOWER LIP, INNER)

MALIGNANT NEOPLASM OF LOWER LIP, INNER ASPECT

4: 140.5 (MAL NEO LIP, INNER NOS)

MALIGNANT NEOPLASM OF LIP, UNSPECIFIED, INNER ASPECT

5: 140.6 (MAL NEO LIP, COMMISSURE)

MALIGNANT NEOPLASM OF COMMISSURE OF LIP

Press \<RET\> or Select 1-5: <span class="mark">^ \<Enter\></span>

...Nothing selected. Attempting Fileman lookup. ??

#### Example 3

<span id="_Toc200270050" class="anchor"></span>Figure 18: LKUP^XTLKMGR API—Example 3: Display Minimized by Setting the 3rd Parameter = 0

VAH,MTL\><span class="mark">S XTLKX="MALIGNANCY OF THE LIP" \<Enter\></span>

VAH,MTL\><span class="mark">D LKUP^XTLKMGR(80,XTLKX,0) \<Enter\></span>

The following 12 matches were found:

1: 140.1 (MAL NEO LOWER VERMILION)

MALIGNANT NEOPLASM OF LOWER LIP, VERMILION BORDER

2: 140.3 (MAL NEO UPPER LIP, INNER)

MALIGNANT NEOPLASM OF UPPER LIP, INNER ASPECT

3: 140.4 (MAL NEO LOWER LIP, INNER)

MALIGNANT NEOPLASM OF LOWER LIP, INNER ASPECT

4: 140.5 (MAL NEO LIP, INNER NOS)

MALIGNANT NEOPLASM OF LIP, UNSPECIFIED, INNER ASPECT

5: 140.6 (MAL NEO LIP, COMMISSURE)

MALIGNANT NEOPLASM OF COMMISSURE OF LIP

Press \<RET\> or Select 1-5: <span class="mark">^ \<Enter\></span> ??

VAH,MTL\>

#### Example 4

<span id="_Toc200270051" class="anchor"></span>Figure 19: LKUP^XTLKMGR API—Example 4: MTLU with Screen Display Turned Off

VAH,MTL\><span class="mark">D LKUP^XTLKMGR(80,XTLKX,-1) \<Enter\></span>

VAH,MTL\><span class="mark">D ^%G \<Enter\></span>

Global ^TMP("XTLKHITS",\$J

TMP("XTLKHITS",\$J

^TMP("XTLKHITS",591795907) = 12

^TMP("XTLKHITS",591795907,1) = <span class="mark">167</span>

^TMP("XTLKHITS",591795907,2) = 168

^TMP("XTLKHITS",591795907,3) = 169

^TMP("XTLKHITS",591795907,4) = 170

^TMP("XTLKHITS",591795907,5) = 171

^TMP("XTLKHITS",591795907,6) = 172

^TMP("XTLKHITS",591795907,7) = 173

^TMP("XTLKHITS",591795907,8) = 220

^TMP("XTLKHITS",591795907,9) = 221

^TMP("XTLKHITS",591795907,10) = 8595

^TMP("XTLKHITS",591795907,11) = 8623

^TMP("XTLKHITS",591795907,12) = 8624

### SH^XTLKMGR(): Add Shortcuts to the Local Shortcut File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The SH^XTLKMGR API adds Shortcuts to the LOCAL SHORTCUT (#8984.2) file.

Format: SH^XTLKMGR(xtlk1,xtlk2,xtlk3)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
27. Set all input variables.
28. Call the API.

Input Parameters: xtlk1: (required) Associated file.

xtlk2: (required) Code in the associated file.

xtlk3: (required) Shortcut (word or phrase).

Output Variables: XTLKER(1,FILENAME): File *not* defined in the LOCAL LOOKUP (#8984.4) file.

XTLKER(2,CODE): The code is *not* in the associated file.

XTLKER(3,SHORTCUT): The shortcut could *not* be added.

### SY^XTLKMGR(): Add Terms and Synonyms to the Local Synonym File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Multi-Term Look-Up (MTLU)

ICR \#: 10153

Description: The SY^XTLKMGR API adds Terms and Synonyms to the LOCAL SYNONYM (#8984.3) file.

Format: SY^XTLKMGR(xtlk1,xtlk2,xtlk3)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
29. Set all input variables.
30. Call the API.

Input Parameters: xtlk1: (required) Associated file.

xtlk2: (required) Term.

xtlk3: (required) Synonym (or optional array for multiple synonyms per term).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/044.png) NOTE: Use one-dimensional arrays wherever supported in ^XTLKMGR as in the following example:

SYN(1)=*\<first synonym\>*  
SYN(2)=*\<second synonym\>*  
SYN(3)=*\<third synonym\>*  
\>D SY^ROUTINE(XTLK1,XTLK2,.SYN)Output Variables: XTLKER(1,FILENAME): File *not* defined in the LOCAL LOOKUP (#8984.4) file.

XTLKER(2,TERM): The term could *not* be added.

XTLKER(3,SYNONYM): The synonym could *not* be added.

## Toolkit—M Unit Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

M Unit is a utility (tool) that permits a series of tests to be written to address specific tags or entry points within a project and act to verify that the return results are as expected for that code. Kernel Toolkit patch XT\*7.3\*81 provides the M Unit code but was never released to production. It is available to M developers upon request from the Kernel development team.

If run routinely any time that the project is modified, the tests indicate whether the intended function has been modified inadvertently, or whether the modification has had unexpected effects on other functionality within the project. The set of unit tests for a project should run rapidly (usually within a matter of seconds) and with minimal disruption for developers. Another function of unit tests is that they indicate what the intended software was written to do. This can be especially useful when new developers start working with the software or a programmer returns to a project after a prolonged period. Ensuring that well-designed unit tests are created for each project; therefore, it does the following:

- Assists development.
- Enhances maintainability.
- Improves end-user confidence in the deployed software.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/045.png) NOTE: None of the Application Programming Interfaces (APIs), extrinsic functions, or sections of code in the M Unit are callable from outside a unit test but are all part of a unit test. M UNIT is a self-contained application.

### Introduction to M Unit Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Unit Test framework permits small tests to be written to verify that the code under examination is doing what you expect it to do. Generally, the tests are performed on the smaller blocks of the application, and do *not* necessarily test all functionality within the application. These tests can be run frequently to validate that no errors have been introduced subsequently as changes are made in the code. The phrase “Test-Driven Development” is frequently used to indicate the strong use of unit testing during development; although, some think of it as equivalent to “Test First Development”, in which the tests for code are written prior to writing the code. In “Test First Development”, the test should initially fail (since nothing has been written) and then pass after the code has been written.

For client side languages, Junit (for Java), DUnit (for Delphi), NUnit and HarnessIt (for dotNet) all provide Unit Test frameworks. The ^XTMUNIT and ^XTMUNIT1 routines provide the same capabilities for unit testing M code. The tests are console-based (that is command line text, *not* windows).

For those who have problems keeping track of routine names for unit testing and with which application they are associated, the MUNIT TEST GROUP (#8992.8) file can be used to maintain groups of unit test routines with the MUnit Test Group edit \[XTMUNIT GROUP EDIT\] option. These unit tests can be run using either of the following:

- Menu Option: Run MUnit Tests from Test Groups \[XTMUNIT GROUP RUN\] option.
- Direct Mode Utility: D <span id="runset_xtmunit" class="anchor"></span>RUNSET^XTMUNIT(setname).

While the order of processing within M Unit tests can be fairly constant, or at least appear to be so, it is preferable to have the unit tests independent of the order in which they are run. Having dependencies between tests can result in problems if the order were to change or if changes are made in the test being depended upon.

### M Unit Test Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supported References in ^XTMUNIT are:

- <u>EN^XTMUNIT(): Run Unit Tests</u>
- <u>CHKEQ^XTMUNIT: Check Two Values for Equivalence</u>
- <u>CHKLEAKS^XTMUNIT(): Check for Variable Leaks</u>
- <u>CHKTF^XTMUNIT(): Test Conditional Values</u>
- <u>FAIL^XTMUNIT(): Generate an Error Message</u>
- <u>\$\$ISUTEST^XTMUNIT: Evaluate if Unit Test is Running</u>
- [RUNSET^XTMUNIT](#runset_xtmunit) (Direct Mode Utility)
- <u>SUCCEED^XTMUNIT: Increment Test Counter</u>

### Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are going to modify sections of your code, it is best to create a unit test for those areas that you want to work. Then, the unit tests can be run as changes are made to ensure that nothing unexpected has changed. For modifications, the unit tests are then written to reflect the new expected behavior and used to ensure that it is what is expected.

A sample unit test can be found in the ^XTMZZUT1 routine.

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-toolkit-user-guide/046.png) NOTE: None of the Application Programming Interfaces (APIs), extrinsic functions, or sections of code in the M Unit are callable from outside a unit test but are all part of a unit test. M UNIT is a self-contained application.

### EN^XTMUNIT(): Run Unit Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: N/A; Not callable from outside a unit test.

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The EN^XTMUNIT API runs unit tests. It is typically the first command within a suite of unit test routines, so that the entire suite of tests (multiple routines) can be run by executing the first routine of the suite. For example, the unit tests for testing M Unit can be run by:

\>D ^XTMZZUT1"

The EN^XTMUNIT API starts the unit testing process.

Format: D EN^XTMUNIT(rouname,\[verbose,\]\[break\])

Input Parameters: rouname: (required) provides the name of the routine where the testing should be started. That routine *must* have at least one test entry point (and possibly more) either specified as follows:

- In the lines immediately following the XTENT tag as the third semi-colon piece on the line.  
  >   
  > Or:
- It can have tags with @TEST as the first text of the comment for the tag line.

verbose: (optional) If it evaluates to True (such as 1), it turns on verbose mode, which lists each individual test being run as well as its result.

break: (optional) If it evaluates to True, it causes the M Unit test process to terminate upon a failure or error instead of continuing until all tests have been evaluated.

Output: returns: Results of the unit tests.

The following sections of code in the XTMUNIT routine are additional test entry points added by the developer; however, they are *not* callable by the developer from inside or outside of the routine:

- <u>STARTUP</u>
- <u>SHUTDOWN</u>
- <u>SETUP</u>
- <u>TEARDOWN</u>
- <u>XTENT: List Unit Test Entry Points</u>
- <u>XTROU: List of Routines Containing Additional Tests</u>

#### STARTUP

This section of code in the XTMUNIT routine runs *before* anything else. It is useful for setting up an environment or variable values that are common to all tests.

#### SHUTDOWN

This section of code in the XTMUNIT routine runs *after* everything else. It is useful for shutting down an environment or clearing variable values that are common to all tests. It can also be used for cleaning up global or file entries that are left because of testing.

#### SETUP

This section of code in the XTMUNIT routine runs *before* every test. It is useful for resetting an environment or variable values that are used by the tests.

#### TEARDOWN

This section of code in the XTMUNIT routine runs *after* every test. It is useful for cleaning up an environment or variable values that are used by the tests.

#### XTENT: List Unit Test Entry Points

This section of code in the XTMUNIT routine is used to store information required by the [EN^XTMUNIT](#enxtmunit-run-unit-tests) API to run a unit test. It provides a list of unit test entry points. Each entry describes a group of tests.

<span id="_Toc199950752" class="anchor"></span>Figure 20: XTENT: List Unit Test Entry Points

;;T4;Entry point using XTMENT

;;T5;Error count check

#### XTROU: List of Routines Containing Additional Tests

This section of code in the XTMUNIT routine is used to store information required by the [EN^XTMUNIT](#enxtmunit-run-unit-tests) API to run a unit test. It provides a list of routines containing additional tests. It extends a suite of tests beyond the limits of a single routine.

<span id="_Toc199950753" class="anchor"></span>Figure 21: XTROU: List of Routines Containing Additional Tests

;;XTMZZUT2;

;;XTMZZUT3;

### CHKEQ^XTMUNIT: Check Two Values for Equivalence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test.

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The CHKEQ^XTMUNIT API runs a test that checks two values for equivalence.

Format: D CHKEQ^XTMUNIT(expect,actual,msg)

Input Parameters: expect: (required) The expected value.

actual: (required) The actual value.

msg: (required) The error message to be generated if the result of the test is False (*not* equal).

Output: returns: Returns:

- A period or “dot”—If the result of the test is True.
- The *\<expected value\>*, the *\<actual value\>*, and the error message “msg”—If the result of the test is False.

### CHKLEAKS^XTMUNIT(): Check for Variable Leaks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The CHKLEAKS^XTMUNIT API runs a test that can be used within:

- Unit tests.
- Standalone test for variable leaks; those created within called code that are allowed to leak into the calling environment, unintentionally.

Format: D CHKLEAKS^XTMUNIT(code,testloc,.nameinpt)

Input Parameters: code: (required) Contains a command to be executed in the test for leaks. For example:

S X=\$\$NOW^XLFDT()testloc: (required) Indicates the location under test. For example:

\$\$NOW^XLFDT() leak test

> Or simply:

\$\$NOW^XLFDT.nameinpt: (required) This parameter is passed by reference and is an array that contains a list of all variables that the user is passing in and/or expects to be present when the code is finished. The variable X would be in the latter category, since it would then be present. The input is in the form of an array:

NAMEINPT("VARNAME")="VARVALUE"

Where:

- VARNAME—Name of a variable.
- VARVALUE—Value that is to be assigned to the variable *before* the contents of the code input parameter is to be executed.

Output: returns: Returns:

- Inside a unit test environment—When run in a unit test environment, variables that are present after the contents of the code input parameter is executed that were *not* included in NAMEINPT array as variables, are listed as failures.
- Outside a unit test environment—When called outside of a unit test environment; any leaked variables are listed on the current device.

### CHKTF^XTMUNIT(): Test Conditional Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test.

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The CHKTF^XTMUNIT API runs a test that checks conditional values (True or False).

Format: D CHKTF^XTMUNIT(val,msg)

Input Parameters: val: (required) The conditional value to be tested.

msg: (required) The error message to be generated if the result of the test is False.

Output: returns: Returns:

- A period or “dot”—If the result of the test is True.
- An error message—If the result of the test is False.

### FAIL^XTMUNIT(): Generate an Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The FAIL^XTMUNIT API runs a test that simply generates an error message. This command is useful for more complex unit tests that are built within the unit test routine itself.

Format: D FAIL^XTMUNIT(msg)

Input Parameters: msg: (required) The text of the error message.

Output: returns: Returns the error message.

### \$\$ISUTEST^XTMUNIT: Evaluate if Unit Test is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The \$\$ISUTEST^XTMUNIT extrinsic function is used to evaluate if a unit test is currently running. If a test is running, it returns a value of 1; otherwise, it returns a value of Zero (0). This can be used to select code to be run based on whether it is currently being tested (or something else that calls it is being tested).

Format: S X=\$\$ISUTEST^XTMUNIT

Input Parameters: none.

Output: returns: Returns:

- 1—If a test is running.
- Zero (0)—If a test is *not* running.

### SUCCEED^XTMUNIT: Increment Test Counter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Not callable from outside a unit test

Category: Toolkit—M Unit Utility

ICR \#: N/A

Description: The SUCCEED^XTMUNIT API runs a test command that increments the test counter; writes a “dot” to the screen for activity, which indicates a successful test. This command is useful for indicating a successful test within a more complex unit test built within the unit test routine itself and is the counterpart to the <u>FAIL^XTMUNIT(): Generate an Error Message</u> API.

Format: D SUCCEED^XTMUNIT

Input Parameters: none.

Output: returns: Increments test counter; writes a period or “dot” to the screen for activity, which indicates a successful test.

### M Unit Utility Sample Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 22</u> is an example of the output from running a suite of unit tests to test M Unit:

<span id="_Ref409619839" class="anchor"></span>Figure 22: Sample Output from the M Unit Test Tool—Verbose

VISTA\><span class="mark">D ^XTMZZUT1 \<Enter\></span>

T1 - - Make sure Start-up Ran.-------------------------------------- \[OK\]

T2 - - Make sure Set-up runs.--------------------------------------- \[OK\]

T3 - - Make sure Teardown runs.------------------------------------- \[OK\]

T4 - Entry point using XTMENT--------------------------------------- \[OK\]

T5 - Error count check

T5^XTMZZUT1 - Error count check - This is an intentional failure.

.

T5^XTMZZUT1 - Error count check - Intentionally throwing a failure

.----------------------------------------------------------------- \[FAIL\]

T6 - Succeed Entry Point...----------------------------------------- \[OK\]

T7 - Make sure we write to principal even though we are on another device\[OK\]

T8 - If IO starts with another device, write to that device as if it's the principal device---------------------------------------------------- \[OK\]

T11 - An @TEST Entry point in Another Routine invoked through XTROU offsets.\[OK\]

T12 - An XTENT offset entry point in Another Routine invoked through XTROU offsets.----------------------------------------------------------------- \[OK\]

MAIN - - Test coverage calculations--------------------------------- \[OK\]

NEWSTYLE - identify new style test indicator functionality.--------- \[OK\]

OLDSTYLE - identify old style test indicator functionality..------- \[OK\]

OLDSTYL1 - identify old style test indicator 2.-------------------- \[OK\]

BADCHKEQ - CHKEQ should fail on unequal value

BADCHKEQ^XTMZZUT5 - CHKEQ should fail on unequal value - \<4\> vs \<3\> - SET UNEQUAL ON PURPOSE - SHOULD FAIL---------------------------------- \[FAIL\]

BADCHKTF - CHKTF should fail on false value

BADCHKTF^XTMZZUT5 - CHKTF should fail on false value - SET FALSE (0) ON PURPOSE - SHOULD FAIL--------------------------------------------- \[FAIL\]

BADERROR - throws an error on purpose

BADERROR^XTMZZUT5 - throws an error on purpose - Error: \<UNDEFINED\>BADERROR+6^X

TMZZUT5 \*Q

------------------------------------------------------------------ \[FAIL\]

CALLFAIL - called FAIL to test it

CALLFAIL^XTMZZUT5 - called FAIL to test it - Called FAIL to test it

------------------------------------------------------------------ \[FAIL\]

LEAKSOK - check leaks should be ok---------------------------------- \[OK\]

LEAKSBAD - check leaks with leak

LEAKSBAD^XTMZZUT5 - check leaks with leak - LEAKSBAD TEST - X NOT SPECIFIED VARIABLE LEAK: X---------------------------------------- \[FAIL\]

NVLDARG1 - check invalid arg in CHKEQ

NVLDARG1^XTMZZUT5 - check invalid arg in CHKEQ - NO VALUES INPUT TO CHKEQ^XTU - no evaluation possible-------------------------------- \[FAIL\]

ISUTEST - check ISUTEST inside unit test.--------------------------- \[OK\]

CHKCMDLN - check command line processing of XTMZZUT5---------------- \[OK\]

CHKGUI - check GUI processing of XTMZZUT5--------------------------- \[OK\]

CKGUISET - check list of tests returned by GUISET------------------- \[OK\]

NEWSTYLE - test return of valid new style or @TEST indicators...---- \[OK\]

Ran 5 Routines, 26 Entry Tags

Checked 25 tests, with 7 failures and encountered 1 error.

## Toolkit—Parameter Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameter Tools is a generic method of handling parameter definitions, assignments, and retrieval. A parameter may be defined for various entities where an entity is the level at which you want to allow the parameter defined (such as package level, system level, division level, location level, user level, and so on). A developer can then determine in which order the values assigned to given entities are interpreted.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/047.png) REF: Integration Control Registration (ICR) \#2263 defines the various callable entry points in the XPAR routine.  
  
ICR \#2336 defines the various callable entry points in the XPAREDIT routine.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/048.png) REF: For more information on parameter tools and files, see the “Parameter Tools” section in the [*Kernel 8.0 Systems Management: Toolkit User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.pdf).

### Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are some basic definitions used by Parameter Tools:

- <u>Entity</u>
- <u>Parameter</u>
- <u>Instance</u>
- <u>Value</u>
- <u>Parameter Template</u>

#### Entity

An entity is a level at which you can define a parameter. The entities allowed are stored in the PARAMETER ENTITY (#8989.518) file. <u>Table 3</u> lists the allowable entities at the time this utility was released:

| Entity Prefix | Message      | Points to File          |
|---------------|--------------|-------------------------|
| PKG       | Package      | PACKAGE (#9.4)          |
| SYS       | System       | DOMAIN (#4.2)           |
| DIV       | Division     | INSTITUTION (#4)        |
| SRV       | Service      | SERVICE/SECTION (#49)   |
| LOC       | Location     | HOSPITAL LOCATION (#44) |
| TEA       | Team         | TEAM (#404.51)          |
| CLS       | Class        | USR CLASS (#8930)       |
| USR       | User         | NEW PERSON (#200)       |
| BED       | Room-Bed     | ROOM-BED (#405.4)       |
| OTL       | Team (OE/RR) | OE/RR LIST (#100.21)    |
| DEV       | Device       | DEVICE (#3.5)           |

<span id="_Toc200270057" class="anchor"></span>Table 4: Routine Tools—Direct Mode Utilities

![](kernel-8-0-developer-s-guide-toolkit-user-guide/049.png) NOTE: Entries are maintained through Kernel Toolkit patches. Entries existing in the file at the time it is referenced are considered supported.

#### Parameter

A parameter is the actual name under which values are stored. The name of the parameter *must* be namespaced and it *must* be unique. Parameters can be defined to store the typical package parameter data (such as the default add order screen in OE/RR), but they can also be used to store GUI application screen settings a user has selected (such as font or window width). When a parameter is defined, the entities that can set that parameter are also defined. The definition of parameters is stored in the PARAMETER DEFINITION (#8989.51) file.

#### Instance

Most parameters set instance to 1. Instances are used when more than one value may be assigned to a given entity/parameter combination. An example of this would be lab collection times at a division. A single division may have multiple collection times. Each collection time would be assigned a unique instance.

#### Value

A value may be assigned to every parameter for the entities allowed in the parameter definition. Values are stored in the PARAMETERS (#8989.5) file.

#### Parameter Template

A parameter template is like an input template. It contains a list of parameters that can be entered through an input session (such as option). Templates are stored in the PARAMETER TEMPLATE (#8989.52) File. Entries in this file *must* also be namespaced.

### Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It’s *not* possible to directly add, edit, or delete entries in in the PARAMETERS \[#8989.5\] file . The only way to do this is programmatically through the APIs described in this section.

### ADD^XPAR(): Add Parameter Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The ADD^XPAR API adds a new parameter value as an entry to the PARAMETERS (#8989.5) file if the Entity/Parameter/Instance combination does *not* already exist.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/050.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: ADD^XPAR(entity,parameter\[,instance\],value\[,.error\])

Input / OutputParameters See [EN^XPAR](#enxpar-add-change-delete-parameters) For the definition of the input and output parameters used in this API, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950755" class="anchor"></span>Figure 23: ADD^XPAR API—Example

\><span class="mark">D ADD^XPAR("PKG.KERNEL","XPAR TEST FREE TEXT",,"Today Good",.ERROR)</span>

### CHG^XPAR(): Change Parameter Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The CHG^XPAR API changes the value assigned to an existing parameter if the Entity/Parameter/Instance combination already exists.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/051.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: CHG^XPAR(entity,parameter\[,instance\],value\[,.error\])

Input / OutputParameters: See [EN^XPAR](#enxpar-add-change-delete-parameters) For the definition of the input and output parameters used in this API, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950756" class="anchor"></span>Figure 24: CHG^XPAR API—Example

\><span class="mark">D CHG^XPAR("PKG.KERNEL","XPAR TEST FREE TEXT",,"Tomorrow Hot",.ERROR)</span>

### DEL^XPAR(): Delete Parameter Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The DEL^XPAR API deletes an existing parameter instance if the value assigned is an at-sign (@).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/052.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: DEL^XPAR(entity,parameter\[,instance\]\[,.error\])

Input / OutputParameters: See [EN^XPAR](#enxpar-add-change-delete-parameters) For the definition of the input and output parameters used in this API, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950757" class="anchor"></span>Figure 25: DEL^XPAR API—Example

\><span class="mark">D DEL^XPAR("PKG.KERNEL","XPAR TEST FREE TEXT",),.ERROR) I ERROR\>0 W !.ERROR</span>

### EN^XPAR(): Add, Change, Delete Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The EN^XPAR API performs any one of the following functions:

- Adds the value as a new entry to the PARAMETERS (#8989.5) file if the Entity\|Parameter\|Instance combination does *not* already exist.
- Changes the value assigned to the parameter in the PARAMETERS (#8989.5) file if the Entity\|Parameter\|Instance combination already exists.
- Deletes the parameter instance in the PARAMETERS (#8989.5) file if the value assigned is @.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/053.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: EN^XPAR(entity,parameter\[,instance\],value\[,.error\])

Input Parameters:entity: (required) Entity can be set to the following:

- Internal VARIABLE POINTER (nnn;GLO(123,).
- External format of the VARIABLE POINTER using the three-character prefix (prefix.entryname).
- Prefix alone to set the parameter based on the current entity selected.

This works for the following entities:

- USR—Uses current value of DUZ.
- DIV—Uses current value of DUZ(2).
- SYS—Uses system (domain).
- PKG—Uses the package to which the parameter belongs.

parameter: (required) Can be passed in external or internal format. Identifies the name or internal entry number (IEN) of the parameter as defined in the PARAMETER DEFINITION (#8989.51) file.

instance: (optional) Defaults to 1 if *not* passed. It can be passed in external or internal format. Internal format requires that the value be preceded by the grave accent (\`) character.

value: (required) Can be passed in external or internal format. If using internal format for a POINTER type parameter, the value *must* be preceded by the grave accent (\`) character.

If the value is being assigned to a WORD-PROCESSING parameter, the text can be passed in the subordinate nodes of Value \[such as Value(1,0)=Text\] and the variable “Value” itself can be defined as a title or description of the text.

Output Parameter:.error: (optional) If used, *must* be passed in by reference. It returns any error condition that may occur:

- 0 (Zero)—If no error occurs.
- \#^*errortext*—If an error does occur.  
  >   
  > The \# is the number in the VA FileMan DIALOG (#.84) file and the “*errortext*” describes the error.

#### Example

<span id="_Toc199950758" class="anchor"></span>Figure 26: EN^XPAR API—Example

\><span class="mark">D EN^XPAR("SYS","XPAR TEST FREE TEXT",0,"Good times",.ERROR)</span>

\><span class="mark">D EN^XPAR("SYS","XPAR TEST FREE TEXT",1,"to night",.ERROR)</span>

### ENVAL^XPAR(): Return All Parameter Instances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The ENVAL^XPAR API returns all parameter instances.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/054.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: ENVAL^XPAR(.list,parameter,instance\[,.error\]\[,gbl\])

Input / OutputParameters: .list: (required) If the gbl parameter is set to 1, then the .list parameter becomes an input and holds the closed root of a global where the [GETLST^XPAR(): Return All Instances of a Parameter](#getlst_xpar) API should put the output. For example:

\$NA(^TMP(\$J,"XPAR"))Input Parameters: parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

instance: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

gbl: (optional) If this optional parameter is set to 1, then the .list parameter *must* be set before the call to the closed global root where the return data should be put. For example:

S LIST=\$NA(^TMP(\$J)) ENVAL^XPAR(LIST,par,inst,.error,1Output Parameters: .error: (optional) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

### \$\$GET^XPAR(): Return an Instance of a Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The \$\$GET^XPAR extrinsic function retrieves the value of a parameter. The value is returned from this call in the format defined by the format input parameter.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/055.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: \$\$GET^XPAR(entity,parameter,instance\[,format\])

Input Parameters:entity: (required) Entity is defined as the single entity or group of entities you want to look at to retrieve the value. Entities may be passed in internal or external format \[such as LOC.PULMONARY, LOC.’57, or 57;SC(\]. The list of entities in this variable may be defined as follows:

- A single entity to look at (such as LOC.PULMONARY).
- The word ALL that tells the utility to look for values assigned to the parameter using the entity precedence defined in the PARAMETER DEFINITION (#8989.51) file.
- A list of entities you want to search (such as “USR^LOC^SYS^PKG”). The list is searched from left to right with the first value found returned.
- Items 2 or 3 with specific entity values referenced such as:
- ALL^LOC.PULMONARY—To look at the defined entity precedence, but when looking at location, only look at the PULMONARY location.
- USR^LOC.PULMONARY^SYS^PKG—To look for values for all current user, PULMONARY location, system, or package).

parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

instance: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

format: (optional) The format input parameter determines how the value is returned. It can be set to the following:

- I—Internal; returns list(#) = “internal value”.
- Q—Quick; returns list(#) = “internal instance^internal value”. Returns the value in the quickest manner (default if *not* specified).
- E—External; returns list(#) = “external instance^external value”.
- B—Both; returns both list(#,“N”) = “internal instance^external instance” and list(#,“V”) = “internal value^external value”.
- N—Returns list(#) = “internal value^external value”.

Output: returns: Returns the parameter value in the format defined by the format input parameter.

### GETLST^XPAR(): Return All Instances of a Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The GETLST^XPAR API is like the <u>ENVAL^XPAR(): Return All Parameter Instances</u> API; however, it returns *all* instances of a parameter.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/056.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “Definitions” section.

Format: GETLST^XPAR(.list,entity,parameter\[,format\]\[,.error\]\[,gbl\])

Input/ OutputParameters: .list: (required) The array passed as .list is returned with all possible values assigned to the parameter.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/057.png) REF: To see how this data can be returned, see the [format](#format_parameter) parameter description.

If the gbl parameter is set to 1, then the .list parameter becomes an input and holds the closed root of a global where the GETLST^XPAR API should put the output \[that is \$NA(^TMP(\$J,“XPAR”))\].

Input Parameters:entity: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

<span id="format_parameter" class="anchor"></span>format: (optional) For a description of this parameter, see the <u>\$\$GET^XPAR(): Return an Instance of a Parameter</u> API.

gbl: (optional) If this optional parameter is set to 1. Then the .list parameter *must* be set before the call to the closed global root where the return data should be put. For example:

GETLST^XPAR(\$NA(^TMP(\$J)),ent,par,fmt,.error,1)Output Parameters: .error: (optional) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950759" class="anchor"></span>Figure 27: GETLST^XPAR API—Example

\><span class="mark">D GETLST^XPAR(.LIST,"SYS","XPAR TEST MULTI FREE TEXT",,.ERROR)</span>

### GETWP^XPAR(): Return Word-Processing Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The GETWP^XPAR API returns WORD-PROCESSING text in the returnedtext parameter. The returnedtext parameter itself contains the value field, which is FREE TEXT that may contain a title, description, and so on. The WORD-PROCESSING text is returned in returnedtext(#,0).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/058.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: GETWP^XPAR(returnedtext,entity,parameter\[,instance\]\[,.error\])

Input / OutputParameters: .returnedtext: (required) This parameter is defined as the name of an array in which you want the text returned. The .returnedtext parameter is set to the title, description, and so on. The actual WORD-PROCESSING text is returned in returnedtext(#,0). For example:

\>returnedtext="Select Notes Help"  
\>returnedtext(1,0)="To select a progress note from the list, "  
\>returnedtext(2,0)="click on the date/title of the note."

Input Parameters: entity: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

instance: (optional) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

Output Parameters: .error (optional) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950760" class="anchor"></span>Figure 28: GETWP^XPAR API—Example

\><span class="mark">D GETWP^XPAR(.X,"PKG","ORW HELP","lstNotes",.ERROR)</span>

### NDEL^XPAR(): Delete All Instances of a Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The NDEL^XPAR API deletes the value for all instances of a parameter for a given entity.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/059.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: NDEL^XPAR(entity,parameter\[,.error\])

Input Parameters: entity: (required) Entity can be set to the following:

- Internal VARIABLE POINTER (nnn;GLO(123,).
- External format of the VARIABLE POINTER using the three-character prefix (prefix.entryname).
- Prefix alone to set the parameter based on the current entity selected.

This works for the following entities:

- USR—Uses current value of DUZ.
- DIV—Uses current value of DUZ(2).
- SYS—Uses system (domain).
- PKG—Uses the package to which the parameter belongs.

parameter: (required) Can be passed in external or internal format. Identifies the name or internal entry number (IEN) of the parameter as defined in the PARAMETER DEFINITION (#8989.51) file.

Output Parameter.error: (optional) If used, *must* be passed in by reference. It returns any error condition that may occur:

- 0 (Zero)—If no error occurs.
- \#^errortext—If an error does occur.  
  >   
  > The \# is the number in the VA FileMan DIALOG (#.84) file and the “errortext” describes the error.

#### Example

<span id="_Toc199950761" class="anchor"></span>Figure 29: NDEL^XPAR API—Example

\><span class="mark">D NDEL^XPAR("SYS","XPAR TEST MULTI FREE TEXT",.ERROR)</span>

### PUT^XPAR(): Add/Update Parameter Instance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The PUT^XPAR API adds or updates a parameter instance and bypass the input transforms.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/060.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: PUT^XPAR(entity,parameter\[,instance\],value\[,.error\])

Input / OutputParameters: See [EN^XPAR](#enxpar-add-change-delete-parameters) For the definition of the input and output parameters used in this API, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

#### Example

<span id="_Toc199950762" class="anchor"></span>Figure 30: PUT^XPAR API—Example

\><span class="mark">D PUT^XPAR("SYS","XPAR TEST MULTI FREE TEXT",0,"Good times",.ERROR)</span>

### REP^XPAR(): Replace Instance Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2263

Description: The REP^XPAR API replaces the value of an instance with another value.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/061.png) REF: For descriptive information about the elements and how they are used in the callable entry points into XPAR, see the “<u>Definitions</u>” section.

Format: REP^XPAR(entity,parameter,currentinstance,newinstance\[,.error\])

Input Parameters: entity: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

currentinstance: (required) The instance for which the value is currently defined.

newinstance: (required) The instance to which you want to assign the value that is currently assigned to currentinstance.

Output Parameters: .error: (optional) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

### BLDLST^XPAREDIT(): Return All Entities of a Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The BLDLST^XPAREDIT API returns in the array list all entities allowed for the input parameter.

Format: BLDLST^XPAREDIT(.list,parameter)

Input Parameters: .list: (required) Name of array to receive output.

parameter: (required) Internal Entry Number (IEN) of entry in the PARAMETER DEFINITION (#8989.51) file.

> Output Parameters: .list: The array passed as list is returned with all possible values assigned to the parameter.

> Data is returned in the following format:

list(ent,inst)=val

### EDIT^XPAREDIT(): Edit Instance and Value of a Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The EDIT^XPAREDIT API interactively edits the instance (if multiple instances are allowed) and the value for a parameter associated with a given entity.

Format: EDIT^XPAREDIT(entity,parameter)

Input Parameters: entity: (required) Identifies the specific entity for which a parameter can be edited. The entity *must* be in VARIABLE POINTER format.

parameter: (required) Identifies the parameter that should be edited. Parameter should contain two pieces:

IEN^DisplayNameOfParameterOutput: results: Returns parameter for Interactive edits.

### EDITPAR^XPAREDIT(): Edit Single Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The EDITPAR^XPAREDIT API edits a single parameter.

Format: EDITPAR^XPAREDIT(parameter)

Input Parameters: parameter: (required) For a description of this parameter, see the <u>EN^XPAR(): Add, Change, Delete Parameters</u> API.

Output: returns: Returns requested parameter.

### EN^XPAREDIT: Parameter Edit Prompt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The EN^XPAREDIT API prompts the user for a parameter to edit. This is provided as a tool for developers and is *not intended for exported calls* as it allows editing of *any* parameter.

Format: EN^XPAREDIT

Input Parameters: none.

Output: none.

### GETENT^XPAREDIT(): Prompt for Entity Based on Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The GETENT^XPAREDIT API interactively prompts for an entity, based on the definition of a parameter.

Format: GETENT^XPAREDIT(.entity,parameter\[,.onlyone?\])

Input Parameters: .entity: (required) Returns the selected entity in VARIABLE POINTER format.

parameter: (required) Identifies the parameter that should be edited. Parameter should contain two pieces:

IEN^DisplayNameOfParameterOutput: .onlyone?: (optional) Returns 1 if there is only one possible entity for the value. For example:

- 1—If the parameter can only be set for the system, onlyone?.
- 0—If the parameter could be set for any location, onlyone?.

### GETPAR^XPAREDIT(): Select Parameter Definition File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The GETPAR^XPAREDIT API allows the user to select the PARAMETER DEFINITION (#8989.51) file entry.

Format: GETPAR^XPAREDIT(.variable)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
31. Set all input variables.
32. Call the API.

Input Parameters: .variable: (required) The name of the variable where data is returned.

Output Variables: .OUTPUTVALU: Returns the value Y in standard VA FileMan DIC lookup format.

### TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The TED^XPAREDIT API allows editing of parameters defined in a template. The parameters in the template are prompted in VA FileMan style—prompt by prompt. No dashed line dividers are displayed between each parameter.

Since the dashed line headers are suppressed, it is important to define the VALUE TERM for each parameter in the template, as this is what prompts for the value.

Format: TED^XPAREDIT(template\[,reviewflags\]\[,allentities\])

Input Parameters: template: (required) The Internal Entry Number (IEN) or NAME of an entry in the PARAMETER TEMPLATE (#8989.52) file.

reviewflags: (optional) There are two flags (A and B) that can be used individually, together, or *not* at all:

- A—Indicates that the new values for the parameters in the template are displayed *after* the prompting is done.
- B—Indicates that the current values of the parameters are displayed *before* editing.

allentities: (optional) This is a VARIABLE POINTER that should be used as the entity for all parameters in the template. If left blank, prompting for the entity is done as defined in the PARAMETER TEMPLATE (#8989.52) file.

Output: none.

### TEDH^XPAREDIT(): Edit Template Parameters (with Dash Dividers)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—Parameter Tools

ICR \#: 2336

Description: The TEDH^XPAREDIT API is like the <u>TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)</u> API except that the dashed line headers *are* shown between each parameter.

It allows editing of parameters defined in a template. The parameters in the template are prompted in VA FileMan style—prompt by prompt.

Format: TEDH^XPAREDIT(template\[,reviewflags\]\[,allentities\])

Input Parameters: template: (required) For a description of this parameter, see the <u>TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)</u> API.

reviewflags: (optional) For a description of this parameter, see the <u>TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)</u> API.

allentities: (optional) For a description of this parameter, see the <u>TED^XPAREDIT(): Edit Template Parameters (No Dash Dividers)</u> API.

Output: none.

## Toolkit—VHA Unique ID (VUID) APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GETIREF^XTID(): Get IREF (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The GETIREF^XTID API searches and returns a list of terms/concepts for a given VHA Unique ID (VUID; that is vuid input parameter). Filtering of the list is applied when the following optional input parameters are defined:

- file
- field
- masterFormat: GETIREF^XTID(\[file\]\[,field\],vuid,array\[,master\])

Input Parameters: file: (optional) VistA file/subfile number where term/concept is defined.

- Defined—If defined, the search is limited to those term/concepts that exist in that file and have the VUID assigned to the vuid input parameter.
- Not Defined—If *not* defined, the search includes term/concepts that have the VUID assigned to the vuid input parameter and can exist in both file terms and in SET OF CODES terms.

field: (optional) Field number, in the file input parameter, where term/concept is defined.

- Defined—The search finds those terms/concepts that have the VUID assigned to the vuid input parameter and is limited to those terms/concepts that exist in the given file/field combination.
- Entered as .01, it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.
- Not Defined—The search finds those terms/concepts that have the VUID assigned to the vuid input parameter and is limited to those terms/concepts found in the file defined in the file input parameter.

vuid: (required) The VHA Unique ID (VUID) value, which is specified to limit the search.

array: (required) The name of the array (local or global) where results of the search is stored.

master: (optional) Flag to limit the search of terms based on the value of the MASTER ENTRY FOR VUID field.

Returns:

- 0—Include all terms.
- 1—Include only those terms designated as MASTER ENTRY FOR VUID.

Output: array: Returns the given array populated as follows:

- @TARRAY = *\<list count\>*
- @TARRAY@(\<file#\>,\<field#\>,\<internalreference\>) = *\<status info\>*

Where the *\<status info\>* is defined as “*\<internal value\>*^*\<VA FileMan effective date/time\>*^*\<external value\>*^*\<master entry?\>* ”

- Empty Array—Unpopulated array when no entries are found.
- Error Array—When an error occurs, the array is populated as follows:

> @TARRAY(“ERROR”)=“*\<error message\>*”

#### Examples

#### Example 1

<span id="_Toc199950763" class="anchor"></span>Figure 31: GETIREF^XTID API—Example 1

\><span class="mark">N array S array="MYARRAY"</span>

\><span class="mark">S file=16000009,field=.01,vuid=12343,master=0</span>

\><span class="mark">D GETIREF^XTID(file,field,vuid,array,master)</span>

\><span class="mark">ZW MYARRAY</span>

MYARRAY=2

MYARRAY(16000009,.01,"1,")=1^3050202.153242^ACTIVE^0

MYARRAY(16000009,.01,"3,")=0^3050215.07584^INACTIVE^1

#### Example 2

When no entries are found, the named array is populated as shown in <u>Figure 32</u>:

<span id="_Ref62647778" class="anchor"></span>Figure 32: GETIREF^XTID API—Example 2

\><span class="mark">ZW MYARRAY</span>

MYARRAY=0

#### Example 3

When an error occurs, the named array is populated as shown in <u>Figure 33</u>:

<span id="_Ref62647823" class="anchor"></span>Figure 33: GETIREF^XTID API—Example 3

\><span class="mark">ZW MYARRAY</span>

MYARRAY("ERROR")=\<error message\>

### \$\$GETMASTR^XTID(): Get Master VUID Flag (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$GETMASTR^XTID extrinsic function retrieves the value of the MASTER ENTRY FOR VUID field for a given term/concept reference.

Format: \$\$GETMASTR^XTID(file\[,field\],iref)

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number in the file input parameter where term/concept is defined:

- Not Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file input parameter.
- Defined:
- Entered as .01, it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept:

- File Entries—This is an IENS. For example:  
  >   
  > iref=“5,”
- SET OF CODES—This is the internal value of the code. For example, any of the following:  
  >   
  > iref = 3  
  > iref = “f”  
  > iref = “M”

Output: returns: Returns results of operation as follows:

- Successful—Internal value of the MASTER ENTRY FOR VUID field as follows:
- 0—NO.
- 1—YES.
- Unsuccessful—^*\<error message\>*

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950766" class="anchor"></span>Figure 34: \$\$GETMASTR^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M"</span>

\><span class="mark">W \$\$GETMASTR^XTID(file,field,iref)</span>

1

#### Example 2

For terms defined in a single file:

<span id="_Toc199950767" class="anchor"></span>Figure 35: \$\$GETMASTR^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,"</span>

\><span class="mark">W \$\$GETMASTR^XTID(file,field,iref)</span>

0

### \$\$GETSTAT^XTID(): Get Status Information (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$GETSTAT^XTID extrinsic function retrieves the status information for a given term/concept reference and a specified DATE/TIME.

Format: \$\$GETSTAT^XTID(file\[,field\],iref\[,datetime\])

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number, in the file input parameter where term/concept is defined:

- Not Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered must be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept.

- File entries—This is an IENS. For example:

iref = “5,”

- SETS OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

datetime: (optional) VA FileMan DATE/TIME. It defaults to NOW.

Output: returns: Returns results of operation as follows:

- Successful—*\<internal value\>*^*\<VA FileMan effective date/time\>*^*\<external value\>*  
  >   
  > For example:

0^3050220.115720^INACTIVE  
1^3050225.115711^ACTIVE

- Unsuccessful—^*\<error message\>*

![](kernel-8-0-developer-s-guide-toolkit-user-guide/062.png) NOTE: The first piece is empty. This differentiates it from the successful case, where the first piece is either 0 or 1.

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950768" class="anchor"></span>Figure 36: \$\$GETSTAT^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M",datetime=\$\$NOW^XLFDT</span>

\><span class="mark">W \$\$GETSTAT^XTID(file,field,iref,datetime)</span>

1^3050121.154752^ACTIVE

#### Example 2

For terms defined in a single file:

<span id="_Toc199950769" class="anchor"></span>Figure 37: \$\$GETSTAT^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,",datetime=""</span>

\><span class="mark">W \$\$GETSTAT^XTID(file,field,iref,datetime)</span>

0^3050122.154755^INACTIVE

### \$\$GETVUID^XTID(): Get VUID (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$GETVUID^XTID extrinsic function retrieves the VHA Unique ID (VUID) for a given term/concept reference.

Format: \$\$GETVUID^XTID(file\[,field\],iref)

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number in the file input parameter where term/concept is defined.

- Not Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file entered in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept:

- File Entries—This is an IENS. For example:

iref=“5,”

- SET OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

Output: returns: Returns results of operation as follows:

- Successful—VHA Unique ID (VUID)
- Unsuccessful—0^*\<error message\>*

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950770" class="anchor"></span>Figure 38: \$\$GETVUID^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M"</span>

\><span class="mark">W \$\$GETVUID^XTID(file,field,iref)</span>

123456

#### Example 2

For terms defined in a single file:

<span id="_Toc199950771" class="anchor"></span>Figure 39: \$\$GETVUID^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,"</span>

\><span class="mark">W \$\$GETVUID^XTID(file,field,iref)</span>

123457

### \$\$SCREEN^XTID(): Get Screening Condition (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$SCREEN^XTID extrinsic function retrieves the screening condition for a given term/concept reference and specified DATE/TIME. It returns whether a given entry should be screened out of selection lists. This API should *not* be used to determine if the given entry is active/inactive, since the API takes into consideration where in the standardization process the facility is. It returns the following values:

- 0—If the given entry is selectable (that is “do *not* screen it out”).
- 1—If the entry is *not* selectable (that is “screen it out”).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/063.png) NOTE: This extrinsic function was released with Kernel Toolkit Patch XT\*7.3\*108.

Format: \$\$SCREEN^XTID(file\[,field\],iref\[,datetime\]\[,.cached\])

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number, in the file input parameter where term/concept is defined.

- *Not* Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file entered in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept:

- File entries—This is an IENS. For example:

iref = “5,”

- SET OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

datetime: (optional) VA FileMan DATE/TIME against which screening is checked. It defaults to NOW.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/064.png) NOTE: If the value of the datetime parameter contains a date and no time, no entries are returned for the first day.

.cached: (optional) Flag to indicate caching. Used mainly when defining the screen parameter \[such as DIC(“S”)\] while searching large files. This improves the speed of the search.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/065.png) NOTE: It *must* be KILLed before initiating each search query (such as before calling the VA FileMan ^DIC API).

Output: returns: Returns the screening condition as follows:

- 0—When term/concept is selectable (that is do *not* screen it out).
- 1—When term/concept is *not* selectable (that is screen it out).

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950772" class="anchor"></span>Figure 40: \$\$SCREEN^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M",datetime=\$\$NOW^XLFDT</span>

\><span class="mark">W \$\$SCREEN^XTID(file,field,iref,datetime)</span>

0

#### Example 2

For terms defined in a single file:

<span id="_Toc199950773" class="anchor"></span>Figure 41: \$\$SCREEN^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,",datetime=""</span>

\><span class="mark">W \$\$SCREEN^XTID(file,field,iref,datetime)</span>

0

#### Example 3

When searching a large file:

<span id="_Toc199950774" class="anchor"></span>Figure 42: \$\$SCREEN^XTID API—Example 3

\><span class="mark">S file=120.52,field=.01,datetime=""</span>

\><span class="mark">S SCREEN="I '\$\$SCREEN^XTID(file,field,Y\_"","",datetime,.cached)"</span>

\>. . .

\><span class="mark">K cached</span>

\><span class="mark">D LIST^DIC(file,,".01;99.99",,"\*",,,,SCREEN,,"LIST","MSG")</span>

\><span class="mark">K cached</span>

### \$\$SETMASTR^XTID(): Set Master VUID Flag (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$SETMASTR^XTID extrinsic function stores (SETs) the value of the MASTER ENTRY FOR VUID field for a given term/concept reference. The MASTER ENTRY FOR VUID field distinguishes references that might be duplicates.

Format: \$\$SETMASTR^XTID(file\[,field\],iref,mstrflag)

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number in the file input parameter where term/concept is defined.

- *Not* Defined—If *not* defined, this field defaults to the .01 field number. It represents the terms defined in the file entered in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept:

- File Entries—This is an IENS. For example:

iref=“5,”

- SET OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

mstrflag: (required) The internal value of the MASTER ENTRY FOR VUID field. Possible values are as follows:

- 0—NO.
- 1—YES.

Output: returns: Returns results of operation as follows:

- Successful—1
- Unsuccessful—0^*\<error message\>*

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950775" class="anchor"></span>Figure 43: \$\$SETMASTR^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M",mstrflag=0</span>

\><span class="mark">W \$\$SETMASTR^XTID(file,field,iref,mstrflag)</span>

1

#### Example 2

For terms defined in a single file:

<span id="_Toc199950776" class="anchor"></span>Figure 44: \$\$SETMASTR^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,",mstrflag=1</span>

\><span class="mark">W \$\$SETMASTR^XTID(file,field,iref,mstrflag)</span>

1

#### Example 3

<span id="_Toc199950777" class="anchor"></span>Figure 45: \$\$SETMASTR^XTID API—Example 3

\><span class="mark">S file=16000009,field=.01,iref="6,",mstrflag=1</span>

\><span class="mark">W \$\$SETMASTR^XTID(file,field,iref,mstrflag)</span>

0^pre-existing master entry

### \$\$SETSTAT^XTID(): Set Status Information (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$SETSTAT^XTID extrinsic function stores (SETs) the status and effective DATE/TIME for the given term/concept.

Format: \$\$SETSTAT^XTID(file\[,field\],iref,status\[,datetime\])

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number in the file input parameter where term/concept is defined.

- *Not* Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file entered in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept:

- File Entries—This is an IENS. For example:

iref = “5,”

- SET OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

status: (required) The status internal value. Possible values are as follows:

- 0—INACTIVE.
- 1—ACTIVE.

datetime: (optional) VA FileMan DATE/TIME. It defaults to NOW.

Output: returns: Returns results of operation as follows:

- Successful—1
- Unsuccessful—0^*\<error message\>*

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950778" class="anchor"></span>Figure 46: \$\$SETSTAT^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M",status=1,datetime=\$\$NOW^XLFDT</span>

\><span class="mark">W \$\$SETSTAT^XTID(file,field,iref,status,datetime)</span>

1

#### Example 2

For terms defined in a single file:

<span id="_Toc199950779" class="anchor"></span>Figure 47: \$\$SETSTAT^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,",status=1,datetime=\$\$NOW^XLFDT</span>

\><span class="mark">W \$\$SETSTAT^XTID(file,field,iref,status,datetime)</span>

1

### \$\$SETVUID^XTID(): Set VUID (Term/Concept)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Toolkit—VHA Unique ID (VUID)

ICR \#: 4631

Description: The \$\$SETVUID^XTID extrinsic function populates (SETs) the VHA Unique ID (VUID) for a given term/concept reference.

It also automatically sets the MASTER ENTRY FOR VUID field to distinguish references that might be duplicates:

- If this is the first reference assigned the VUID, it sets the MASTER ENTRY FOR VUID equal to 1.
- If another entry already has the given VUID, it sets the MASTER ENTRY FOR VUID equal to 0.

Format: \$\$SETVUID^XTID(file\[,field\],iref,vuid)

Input Parameters: file: (required) VistA file/subfile number where term/concept is defined.

field: (optional) Field number in the file input parameter where term/concept is defined.

- *Not* Defined—If *not* defined, this field defaults to the .01 field number, and it represents terms defined in the file entered in the file input parameter.
- Defined:
- Entered as .01; it represents the terms defined in the file entered in the file input parameter.
- Otherwise, the field number entered *must* be a SET OF CODES data type field in the file entered in the file input parameter.

iref: (required) Internal reference for term/concept.

- File Entries—This is an IENS. For example:

iref = “5,”

- SET OF CODES—This is the internal value of the code. For example, any of the following:

iref = 3  
iref = “f”  
iref = “M”

vuid: (required) The VHA Unique ID (VUID) to assign the given term/concept reference.

Output: returns: Returns results of operation as follows:

- Successful—1
- Unsuccessful—0^*\<error message\>*

#### Examples

#### Example 1

For terms defined in fields that are SET OF CODES:

<span id="_Toc199950780" class="anchor"></span>Figure 48: \$\$SETVUID^XTID API—Example 1: Terms Defined in Fields that are SET OF CODES

\><span class="mark">S file=2,field=.02,iref="M",vuid=123456</span>

\><span class="mark">W \$\$SETVUID^XTID(file,field,iref,vuid)</span>

1

#### Example 2

For terms defined in a single file:

<span id="_Toc199950781" class="anchor"></span>Figure 49: \$\$SETVUID^XTID API—Example 2: Terms Defined in a Single File

\><span class="mark">S file=16000009,field=.01,iref="3,",vuid=123457</span>

\><span class="mark">W \$\$SETVUID^XTID(file,field,iref,vuid)</span>

1

## Toolkit—Routine Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit provides developer utilities for working with M routines and globals. This section describes the routine tools exported with Kernel Toolkit. These tools are useful to system administrators and VistA software developers.

### Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Kernel Toolkit direct mode utilities are available for developers to use at the M prompt, usually involving the DO command. They are *not* APIs and *cannot* be used in software application routines.

<table>
<caption><p><span id="_Ref152648828" class="anchor"></span>Table 5: Verification Tools—Direct Mode Utilities</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Direct Mode Utility</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&gt;<strong>D ^XTFCR</strong></td>
<td>Generate a flow chart of an entire routine.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XTFCE</strong></td>
<td>Generate a flow chart of the processing performed from a specified entry point to the termination of processing resulting from that entry point.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^%INDEX</strong></td>
<td>(obsolete) To run <strong>%INDEX</strong>.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XINDEX</strong></td>
<td>To run <strong>XINDEX</strong>.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>X ^%Z</strong></td>
<td>Invokes the <strong>^%Z</strong> Editor.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XTRGRPE</strong></td>
<td>Edit a group of routines.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^XTVCHG</strong></td>
<td>Changes all occurrences of one variable to another.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XTVNUM</strong></td>
<td>Update or set the version number into a set of routines.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^%ZTP1</strong></td>
<td>A summary listing of the first, and optionally the second, line of one or more routines can be obtained.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^%ZTPP</strong></td>
<td>Print a listing of entire routines.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^XTRCMP</strong></td>
<td>Compare two routines with different names and display the differences (using MailMan’s PackMan compare utilities).</td>
</tr>
<tr class="even">
<td>&gt;<strong>D TAPE^XTRCMP</strong></td>
<td><p>Compares routines in a Host File Server (HFS) file to an installed routine and displays the differences.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/066.png) <strong>NOTE:</strong> While it is still called a “<strong>TAPE</strong>” compare, it is comparing a routine in an HFS file to an installed routine.</p></td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^%ZTRDEL</strong></td>
<td>Delete one or more routines.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^%RR</strong> (OS-specific)</td>
<td>Loads routines from an external device, such as magtape.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^%RS</strong> (OS-specific)</td>
<td>Output routines to an external device, such as a magtape.</td>
</tr>
</tbody>
</table>

<span id="_Ref152648828" class="anchor"></span>Table 5: Verification Tools—Direct Mode Utilities

### Routine Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of these tools are available as options on the Routine Tools \[XUPR-ROUTINE-TOOLS\] menu located on the Programmer Options \[XUPROG\] menu, which is locked with the XUPROG security key. Some subordinate menu options are locked with the XUPROGMODE or XUPROG security keys as an extra level of security.

Routines can be edited, analyzed by flow-charting, printed, compared, deleted, and moved by using an option or its corresponding direct mode utility.

The Routine Tools menu is shown in <u>Figure 50</u>:

<span id="_Ref454453940" class="anchor"></span>Figure 50: Routine Tools—Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Programmer Options ... \<locked with XUPROG\> \[XUPROG\]

Routine Tools ... \[XUPR-ROUTINE-TOOLS\]

%Index of Routines \[XUINDEX\]

Compare local/national checksums report \[XU CHECKSUM REPORT\]

Compare routines on tape to disk \[XUPR-RTN-TAPE-CMP\]

Compare two routines \[XT-ROUTINE COMPARE\]

Delete Routines \<locked with XUPROGMODE\> \[XTRDEL\]

Flow Chart Entire Routine \[XTFCR\]

Flow Chart from Entry Point \[XTFCE\]

Group Routine Edit \<locked with XUPROGMODE\> \[XTRGRPE\]

Input routines \<locked with XUPROG\> \[XUROUTINE IN\]

List Routines \[XUPRROU\]

Load/refresh checksum values into ROUTINE file \[XU CHECKSUM LOAD\]

Output routines \[XUROUTINE OUT\]

Routine Edit \<locked with XUPROGMODE\> \[XUPR RTN EDIT\]

Routines by Patch Number \[XUPR RTN PATCH\]

Variable changer \<locked with XUPROGMODE\> \[XT-VARIABLE CHANGER\]

Version Number Update \<locked with XUPROGMODE\> \[XT-VERSION NUMBER\]

These options are documented in the sections that follow, grouped by routine type.

#### Analyzing Routines

#### %Index of Routines Option—XINDEX

The %Index of Routines \[XUINDEX\] option calls Kernel Toolkit’s XINDEX utility (formerly known as %INDEX utility). XINDEX is a static analysis tool that plays the dual role of a VistA-aware cross-referencing tool and a code checker (or recognizer).

As of Kernel Toolkit patch XT\*7.3\*132, the %Index of Routines \[XUINDEX\] option allows users to check the contents of any of the following:

- Routines—XINDEX checks the specified routines (such as XU\*).
- Builds:
- XINDEX checks the contents of the specified build defined in the BUILD (#9.6) file.
- XINDEX checks all components of the build on the current system, which includes routines, options, templates, data dictionaries, and so on.
- Installs
- XINDEX checks the contents of the specified install defined in the INSTALL (#9.7) file.
- XINDEX checks all components of the install that have temporarily been loaded into ^XTEMP global, which includes, routines, options, templates, data dictionaries, and so on.
- Packages:
- XINDEX checks the contents of the specified package defined in the PACKAGE (#9.4) file.
- XINDEX checks all components of the package on the current system, which includes routines, options, templates, data dictionaries, and so on.

<span id="_Toc199950783" class="anchor"></span>Figure 51: %Index of Routines Option—Sample User Entries

Select Routine Tools Option: <span class="mark">%INDEX \<Enter\></span> of Routines

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Dec 13, 2011@07:40:44

All Routines? No =\> <span class="mark">N</span>O

Routine: <span class="mark">HLUOPT\<Enter\></span>

Routine: <span class="mark">\<Enter\></span>

1 routine

<span class="mark">Select BUILD NAME:</span> <span class="mark">\<Enter\></span>

<span class="mark">Select INSTALL NAME:</span> <span class="mark">\<Enter\></span>

<span class="mark">Select PACKAGE NAME:</span> <span class="mark">\<Enter\></span>

Print more than compiled errors and warnings? YES// <span class="mark">\<Enter\></span>

Print summary only? NO// <span class="mark">\<Enter\></span>

Print routines? YES// <span class="mark">\<Enter\></span>

Print (R)egular,(S)tructured or (B)oth? R// <span class="mark">\<Enter\></span>

Print errors and warnings with each routine? YES// <span class="mark">\<Enter\></span>

Save parameters in ROUTINE file? NO// <span class="mark">\<Enter\></span>

Index all called routines? NO// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Telnet Terminal Right Margin: 80// <span class="mark">\<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Dec 13, 2011@07:40:44

Routines: 1 Faux Routines: 0

HLUOPT

--- CROSS REFERENCING ---

Press return to continue: <span class="mark">\<Enter\></span>

Compiled list of Errors and Warnings Dec 13, 2011@07:40:44 page 1

HLUOPT \* \* 69 Lines, 3758 Bytes, Checksum: B18177059

<span class="mark">HOLD+4 W - Null line (no commands or comment).</span>

--- Routine Detail --- with REGULAR ROUTINE LISTING ---

Press return to continue:

<span class="mark">\<Enter\></span>

HLUOPT \* \* 69 Lines, 3758 Bytes, Checksum: B18177059

Dec 13, 2011@07:40:44 page 2

548 bytes in comments

HLUOPT ;AISC/SAW-Main Menu for HL7 Module ;07/26/99 08:47

;;1.6;HEALTH LEVEL SEVEN;\*\*57\*\*;Oct 13, 1995

![](kernel-8-0-developer-s-guide-toolkit-user-guide/067.png) REF: For more information on the XINDEX utility, see the “<u>XINDEX</u>” section.

#### Flow Chart Entire Routine Option

The Flow Chart Entire Routine \[XTFCR\] option generates a flow chart, showing the processing performed within an entire routine.

The following corresponding direct mode utility can be used in Programmer mode:

\>D ^XTFCR

#### Flow Chart From Entry Point Option

The Flow Chart from Entry Point \[XTFCE\] option generates a flow chart of the processing performed from a specified entry point to its termination of processing. It also allows the user to expand the code in other routines or entry points referenced by DO or GOTO commands.

The following corresponding direct mode utility can be used in Programmer mode:

\>D ^XTFCE

#### Editing Routines

#### Group Routine Edit Option

The Group Routine Edit \[XTRGRPE\] option calls the XTRGRPE routine to edit a group of routines. Once several routines are identified, the Kernel Toolkit ^%Z Editor is called. This option is locked with the XUPROGMODE security key.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^XTRGRPE

#### Routine Edit Option

The Routine Edit \[XUPR RTN EDIT\] option invokes the ^%Z Editor. The ^%Z Editor can be used to edit a group of routines with the Group Routine Edit \[XTRGRPE\] option. This allows developers at an external site (such as on the site manager’s staff) to edit M routines. This option is locked with the XUPROGMODE security key.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>X ^%Z

![](kernel-8-0-developer-s-guide-toolkit-user-guide/068.png) REF: For more information on the ^%Z Editor, see the “^%Z Editor” section in the [*Kernel 8.0 Developer’s Guide: Miscellaneous Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_miscellaneous_ug.pdf).

#### Routines by Patch Number Option

The Routines by Patch Number \[XUPR RTN PATCH\] option allows users to print routines associated with a patch. When prompted, enter a list of routines. The output is sorted by patch number.

#### Variable Changer Option

The Variable Changer \[XT-VARIABLE CHANGER\] option runs the XTVCHG routine, which changes all occurrences of one variable to another. This option is locked with the XUPROGMODE security key.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/069.png) CAUTION: This option changes DOs and GOTOs also, but it does *not* change the target of the DOs and GOTOs. For example, if you request to change all occurrences of “TAG” to “TAGS”, “DO TAG” would be changed to “DO TAGS”. However, the actual Line Label called TAG would not be changed.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^XTVCHG

#### Version Number Update Option

The Version Number Update \[XT-VERSION NUMBER\] option updates version numbers of one or more routines. This option runs the XTVNUM routine to update or set the version number into a set of routines. This option is locked with the XUPROGMODE security key.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^XTVNUM

#### Printing Routines

#### List Routines Option

The List Routines \[XUPRROU\] option uses the %ZTPP utility to print a listing of entire routines.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^%ZTPP

#### Comparing Routines

#### Compare local/national checksums report Option

The Compare local/national checksums report \[XU CHECKSUM REPORT\] option compares checksums for routines to the values in the ROUTINE (#9.8) file. It produces a report listing routines that differ by the following criteria:

- Patch or version, where the version or patch may be correct, but checksums are off
- Local routines being tracked
- Information is *not* on record for a patch (such as test patches)

Nationally released routine checksums are sent by Master File Updates to the local ROUTINE (#9.8) file automatically. Local sites may also record checksums in the CHECKSUM VALUE field in the ROUTINE (#9.8) file. To compare local routines that are being tracked, the CHECKSUM REPORT field should be set to “Local – report.”

As of Kernel Patch XU\*8.0\*369, the integrity checking CHECK1^XTSUMBLD routine supports the Compare local/national checksums report \[XU CHECKSUM REPORT\] option.

As of Kernel Patch XU\*8.0\*393, KIDS was modified to send a message to a server on FORUM when a KIDS build is sent to a Host File Server (HFS) device. This message contains the checksums for the routines in the patch. The server on FORUM matches the message with a patch if the sending domain is authorized on FORUM. There is no longer a need for developers to manually include routine checksums (either CHECK^XTSUMBLD or CHECK1^XTSUMBLD routines) in the patch description. The patch module includes the before and after CHECK1^XTSUMBLD values in the “Routine Information” section at the end of the patch document.

With changes in the National Patch Module (NPM) on FORUM, when the patch is released the checksums for the routines are moved to the ROUTINE (#9.8) file on FORUM. The checksum “before” values come from the FORUM ROUTINE (#9.8) file and are considered the GOLD standard for released checksums. The local site’s Compare local/national checksums report \[XU CHECKSUM REPORT\] option uses the FORUM ROUTINE (#9.8) file as its source to create reports showing any routines that do *not* match.

This patch also modified the KIDS BUILD (#9.6) file by adding the TRANSPORT BUILD NUMBER (#63) field used to store a build number that is incremented each time a build is made. This build number is added to the second line of each routine in the 7th “;” piece. This makes it easy to tell if a site is running the current release during testing and afterword. The leading “B” found in the checksum tells the code what checksum API to use.

#### Compare Routines on Tape to Disk Option

The Compare Routines on Tape to Disk \[XUPR-RTN-TAPE-CMP\] option compares routines and displays the differences. This option reads a standard Caché %RO Host File Server (HFS) file and compares the routines on the HFS file with a routine with the same name in the current account.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D TE^XTRCMP

![](kernel-8-0-developer-s-guide-toolkit-user-guide/070.png) NOTE: While it is still called a “TAPE” compare, it is comparing a routine in a Host File Server (HFS) file to an installed routine.

#### Compare Two Routines Option

The Compare Two Routines \[XT-ROUTINE COMPARE\] option compares two routines with different names that are in the same account and displays/prints the differences (using MailMan’s PackMan compare utilities).

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^XTRCMP

#### Deleting Routines

#### Delete Routines Option

The Delete Routines \[XTRDEL\] option can be used to delete one or more routine(s). The wildcard syntax can be used to delete a set, such as ABC\* to delete all those routines beginning with the letters ABC. This option is locked with the XUPROGMODE security key.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^%ZTRDEL

#### Load and Save Routines

The Input Routines and Output Routines options can be used to move routines from one UCI to another. These make use of operating system-specific utilities such as %RR for routine restore and %RS for routine save.

#### Input Routines Option

The Input Routines \[XUROUTINE IN\] option loads routines from an external device. This option is locked with the XUPROG security key.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^%RR (OS-specific)

#### Output Routines Option

The Output Routines \[XUROUTINE OUT\] option outputs routines to an external device, such as a host file.

The corresponding direct mode utility can be used in Programmer mode as follows:

\>D ^%RS (OS-specific)

#### Load/refresh checksum values into ROUTINE file Option

The Load/refresh checksum values into ROUTINE file option \[XU CHECKSUM LOAD\] can be used to update the ROUTINE (#9.8) file with the latest checksum values from FORUM.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/071.png) REF: Kernel Toolkit Application Programming Interfaces (APIs) are documented in the “<u>Toolkit: Developer Tools</u>” section. Kernel and Kernel Toolkit APIs are also available in HTML format on the VA Intranet Website.

## Toolkit—Verification Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit provides an Application Programming Interface (API) that includes developer utilities for working with routines and globals. This section describes the verification tools exported with Kernel Toolkit that are useful to system administrators and developers for reviewing Veterans Health Information Systems and Technology Architecture (VistA) software.

Verification tools can be accessed through one of three methods:

- <u>Direct Mode Utilities</u>
- <u>Programmer Options Menu</u>
- <u>Operations Management Menu</u>

### Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Kernel Toolkit direct mode utilities are available for developers to use at the M prompt, usually involving the DO command. They are *not* APIs and *cannot* be used in software application routines. These direct mode utilities are described below by category.

The XINDEX utility can be used to check a routine or set of routines against standards such as the 1995 ANSI M Standard syntax and VA *Programming Standards and Conventions (SAC)*.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/072.png) REF: For more information on the XINDEX utility, see the “<u>%Index of Routines Option</u>” section in the “<u>Toolkit—Routine Tools</u>” section.

The corresponding direct mode utility can be used in Programmer mode:

\>D ^XINDEX

Many of the options on the Programmer Options menu can also be run as direct mode utilities. Some are *not* available as options, but only as direct mode utilities callable at the M prompt.

<u>Table 5</u> lists examples on how to run these utilities when working in Programmer mode.

<table>
<caption><p><span id="_Toc199951069" class="anchor"></span>Table 6: XINDEX—Types of Findings (Category Codes or Flags)</p></caption>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Direct Mode Utility</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&gt;<strong>D CHCKSUM^XTSUMBLD</strong></td>
<td><p>Check the checksum value of a routine at any given time.</p>
<p>This direct mode utility allows the developer to choose from the old <strong>CHECK^XTSUMBLD</strong> checksum routine or the new and more accurate <strong>CHECK1^XTSUMBLD</strong> checksum routine.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/073.png) <strong>REF:</strong> For more information on the <strong>CHECK^XTSUMBLD</strong> and <strong>CHECK1^XTSUMBLD</strong> routines, see the <em>Kernel 8.0 Systems Management: Kernel Installation and Distribution System (KIDS) User Guide</em>.</p></td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^nsNTEG</strong></td>
<td>Check Integrity of namespace (ns) Package. For example, <strong>D ^XTNTEG</strong> compares the Kernel Toolkit namespace (<strong>XT</strong>) checksums with expected values.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ONE^nsNTEG</strong></td>
<td>Check Integrity Routine in namespace (ns) Package.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^%ZTER</strong></td>
<td>Record an Error.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^XTER</strong></td>
<td>Display Error Trap.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XTERPUR</strong></td>
<td>Purge Error Log.</td>
</tr>
<tr class="odd">
<td>&gt;<strong>D ^%INDEX</strong></td>
<td>(obsolete) To run <strong>%INDEX</strong>.</td>
</tr>
<tr class="even">
<td>&gt;<strong>D ^XINDEX</strong></td>
<td>To run <strong>XINDEX</strong>. <strong>XINDEX</strong> is like <strong>%INDEX</strong> but supports the most current M standard.</td>
</tr>
</tbody>
</table>

<span id="_Toc199951069" class="anchor"></span>Table 6: XINDEX—Types of Findings (Category Codes or Flags)

![](kernel-8-0-developer-s-guide-toolkit-user-guide/074.png) NOTE: For information on the options associated with the routines associated with these verification tools direct mode utilities, see the “Verification Tools” section in the [*Kernel 8.0 Systems Management: Toolkit User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.pdf).

### Verifier Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verifier Tools Menu contains options that are available as tools for verification during program development. These options are located on the Verifier Tools Menu \[XTV MENU\], which is located on the Systems Manager Menu. These tools are useful for developers to:

- Record the text of the routines indicated in the file used to maintain changes in routines.
- Compare one or more current routines to previous versions.

The Verifier Tools Menu \[XTV MENU\] consists of the following options shown in <u>Figure 52</u>:

<span id="_Ref62648376" class="anchor"></span>Figure 52: Verifier Tools—Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

<span class="mark">Verifier Tools Menu ...</span> \[XTV MENU\]

<span class="mark">Update with current routines</span> \[XTVR UPDATE\]

<span class="mark">Routine Compare - Current with Previous</span> \[XTVR COMPARE\]

#### Update with Current Routines Option

The Update with Current Routines \[XTVR UPDATE\] option records the text of the routines indicated in the file used to maintain changes in routines. Only the last version entered is kept intact; previous entries reflect only the changes in lines added or deleted to make the next version. This option records the current routine structure so that it can be compared with future versions of the routine using the Routine Compare - Current with Previous \[XTVR COMPARE\] option.

After editing the routine, the Update with Current Routines option can again be used to store changes. Rather than storing all minor changes, the user can choose to wait and use the Update with Current Routines option only after extensive edits have been made. Lines are compared and changes, including inserted or deleted lines, are recorded. (Alteration of the routine’s second line is usually insignificant and is ignored.) The Update with Current Routines option can be used whenever the developer would like a new “snapshot” of the routine. The XTV ROUTINE CHANGES (#8991) file holds each new snapshot as a new version. This filing method does *not*, however, alter the actual version number of the routine itself.

#### Routine Compare - Current with Previous Option

The Routine Compare - Current with Previous \[XTVR COMPARE\] option compares one or more current routines to previous versions. To use the routine compare utility, copies of the selected routines *must* first be stored in the XTV ROUTINE CHANGES (#8991) file, stored in the ^XTV(8991, global. This is achieved by use of the Update with Current Routines \[XTVR UPDATE\] option on the Verifier Tools Menu. Routines can be specified one by one or as a group with the wildcard syntax (such as XQ\*). Any initialize routines are automatically excluded. Differences between the current version and the indicated number of prior versions are noted. The user is prompted for the number of previous versions from which to begin the listing. An entire history or just a brief display of recent modifications can be obtained.

### Programmer Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Programmer Options \[XUPROG\] menu comprised of the following options:

<span id="_Toc193181929" class="anchor"></span>Figure 53: Programmer Options—Menu options: Toolkit Verification Tools

SYSTEMS MANAGER MENU ... \[EVE\]

<span class="mark">Programmer Options ...</span> \[XUPROG\]

\*\*\> Locked with XUPROG

KIDS Kernel Installation & Distribution System ... \[XPD MAIN\]

\*\*\> Locked with XUPROG

PG Programmer mode \[XUPROGMODE\]

\*\*\> Locked with XUPROGMODE

<span class="mark">Calculate and Show Checksum Values \[XTSUMBLD-CHECK\]</span>

Delete Unreferenced Options \[XQ UNREF'D OPTIONS\]

<span class="mark">Error Processing ... \[XUERRS\]</span>

General Parameter Tools ... \[XPAR MENU TOOLS\]

Global Block Count \[XU BLOCK COUNT\]

List Global \[XUPRGL\]

\*\*\> Locked with XUPROGMODE

Routine Tools ... \[XUPR-ROUTINE-TOOLS\]

Test an option not in your menu \[XT-OPTION TEST\]

\*\*\> Locked with XUMGR

Tools found on the Programmer Options menu that can be of use for verification purposes include:

- Calculate and Show Checksum Values \[XTSUMBLD-CHECK\]
- Error Processing \[XUERRS\]

These options are described in the sections that follow.

#### Calculate and Show Checksum Values Option

The Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] option gives developers the ability to check the value of a routine at any given time. It does *not* regenerate NTEG routines and can safely be used anytime.

This option calls the CHCKSUM^XTSUMBLD direct mode utility to calculate and show the checksum value for one or more routines in the current account. This value is referenced in the Patch Module description for routine patches.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/075.png) NOTE: Kernel Toolkit patch XT\*7.3\*94, deployed the CHECK1^XTSUMBLD routine and the new logic Checksum: %^ZOSF(“RSUM1”). Kernel Toolkit patch XT\*7.3\*100 included the CHECK1^XTSUMBLD routine into the Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] option.

The CHECK1^XTSUMBLD routine is more accurate than the old integrity checking utility (CHECK^XTSUMBLD). CHECK1^XTSUMBLD. It determines the current checksums for selected routine(s), the functionality of which is shown as follows:

- Any comment line with a single semi-colon is presumed to be followed by comments and only the line tag is included.
- Line 2 is excluded from the count.
- The total value of the routine is determined (excluding exceptions noted above) by multiplying the ASCII value of each character by its position on the line and position of the line in the routine being checked.

The corresponding direct mode utility can be used in Programmer mode:

\>D CHCKSUM^XTSUMBLD

![](kernel-8-0-developer-s-guide-toolkit-user-guide/076.png) NOTE: The integrity checking utility CHCKSUM^XTSUMBLD supports the Compare local/national checksums report \[XU CHECKSUM REPORT\] option, as released with Kernel Patch XU\*8.0\*369.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/077.png) NOTE: The modification, CHECK1^XTSUMBLD, to the integrity checking utility CHCKSUM^XTSUMBLD fixes the problem in which the old checksum output is the same checksum value, even if some lines were swapped within a routine.

#### Error Processing—Kernel Error Trapping and Reporting

Technical personnel who have entered Programmer mode with D ^XUP might choose to record an error encountered with D ^%ZTER. The error log can be displayed with D ^XTER, or with the corresponding option. Also, the error log can be purged with D ^XTERPUR. Errors can also be purged from within the menu system with an option that is locked with the XUPROGMODE security key.

The corresponding direct mode utilities can be used in Programmer mode as follows:

- Record an Error:

\>D ^%ZTER

- Display Error Trap:

\>D ^XTER

- Purge Error Log:

\>D ^XTERPUR

![](kernel-8-0-developer-s-guide-toolkit-user-guide/078.png) REF: For more information on Error Processing, see the “Error Processing” section in the [*Kernel 8.0 Systems Management: Utilities User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf).

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit’s XINDEX utility (formerly known as %INDEX utility) is a static analysis tool that plays the dual role of a VistA-aware cross-referencing tool and a code checker (or recognizer). As of Kernel Toolkit patch XT\*7.3\*132, XINDEX creates a cross-referenced list of global references and routines invoked by selecting any of the following:

- Routines—XINDEX checks the specified routines (such as XU\*).
- Builds—XINDEX checks the contents of the specified build defined in the BUILD (#9.6) file. XINDEX checks all components of the build on the current system, which includes routines, options, templates, data dictionaries, and so on.
- Installs—XINDEX checks the contents of the specified install defined in the INSTALL (#9.7) file. XINDEX checks all components of the install that have temporarily been loaded into ^XTEMP global, which includes, routines, options, templates, data dictionaries, and so on.
- Packages—XINDEX checks the contents of the specified package defined in the PACKAGE (#9.4) file. XINDEX checks all components of the package on the current system, which includes routines, options, templates, data dictionaries, and so on.

Use XINDEX to verify parts of a software application in the VistA environment that contain M code, including the following:

- Routines
- Options
- Compiled Templates
- Data Dictionaries (DD)
- Functions

XINDEX provides greater analysis capability than other syntax analysis tools that operate at the routine level only. As a *static* analysis tool, however, XINDEX has a *fundamental* limitation of the types of errors that it can catch and report. XINDEX is only able to look at the written structure of M code. It *cannot* look at dynamic aspects, such as the run-time symbol table or flow of control when it is modified by conditional branching (such as through post-conditionals or argument indirection). XINDEX is also generally conservative, at times preferring to report false positives rather than ignore potential problems. When analyzing XINDEX output, you *must* take all of this into consideration.

VistA applications are required to follow a set of Standards and Conventions (SAC) as set by the VA’s Standards and Conventions Committee (SACC), which are defined as follows:

- Standard—Requirement that *must* be adhered to.
- Convention—Rule that *should* be followed.

VistA protects many of its abstractions by convention, even when those conventions are requirements. XINDEX checks that the MUMPS (M) routine code conforms to the 1995 ANSI M Standard and *VA Programming Standards and Conventions (SAC)*. XINDEX considers all SAC prohibitions as an error. XINDEX checks SAC requirements, because conformance to the SAC is essential to the proper function of VistA.

VistA is comprised of several software packages (defined by namespace), which can be further divided into the following two basic groups:

- Applications—VistA client applications or application modules (such as Pharmacy, Laboratory, Patient Care Encounter \[PCE\]).
- Infrastructure Applications—Collection of Infrastructure packages that implement the basic programming and runtime VistA framework. For example:
- Kernel/Kernel Toolkit—Provides a portable system interface, a common execution environment, and essential services such as signon and security.
- MailMan—Provides VistA email functionality.
- VA FileMan—Provides database functionality built on top of the M global subsystem integrated with the VistA security model.

It is important to recognize that the rules for VistA infrastructure packages (particularly Kernel and VA FileMan) are different from other VistA applications. Code used in infrastructure packages to implement a system interface *must* be able to use implementation-specific code. Accordingly, Kernel (and sometimes VA FileMan) has standing exemptions from many of the requirements of the SAC. Thus, XINDEX sometimes reports errors and standards violations for allowed constructs.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/079.png) REF: For more information on the Standards and Conventions Committee (SACC) and Standards and Conventions (SAC) documentation, see the [SACC VA Intranet website](https://dvagov.sharepoint.com/sites/OITEPMODevelopment/sac/default.aspx).

### Types of XINDEX Findings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XINDEX reports its findings under the following general categories of codes (error flags):

<table>
<caption><p><span id="_Ref311614132" class="anchor"></span>Table 7: XINDEX—List of Error Conditions (Messages) Flagged: Grouped by Category and Listed Alphabetically); Messages are Stored in XINDX1 Routine</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Category Code/Other</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>F</strong></td>
<td><p><strong><u>Fatal M Errors (Hard MUMPS Error)</u>—</strong>These are unrecoverable errors that cause a program to fail if the commands are executed. It is possible, however, that these types of errors might exist in routines that run correctly. The error occurs (or may occur, depending on the underlying implementation) only when the errant commands are executed.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/080.png) <strong>REF:</strong> For a description and sample code analysis on errors in this category, see Section <u>2.12.3.1</u>, “<u>Fatal M Errors (Hard MUMPS Error)</u>.”</p></td>
</tr>
<tr class="even">
<td><strong>W</strong></td>
<td><p><strong><u>Warning Violation Errors (According to VA Conventions)</u>—</strong>These are potential problems that are <em>not</em> necessarily fatal errors but most likely indicate an error. They require careful implementation.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/081.png) <strong>REF:</strong> For a description and sample code analysis on errors in this category, see Section <u>2.12.3.2</u>, “<u>Warning Violation Errors (According to VA Conventions)</u>.”</p></td>
</tr>
<tr class="odd">
<td><strong>S</strong></td>
<td><p><u><br />
<strong>Standards Violation Errors (According to VA Standards)</strong></u><strong>—</strong>These are issues that do <em>not</em> pertain to the M language <em>per se</em>, but rather the requirements of the VA Standards and Conventions (SAC). Issues flagged as Standards Violations can still be syntactically correct M code that follows the portability guidelines but does <em>not</em> follow the more stringent requirements set forth in the SAC.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/082.png) <strong>REF:</strong> For a description and sample code analysis on errors in this category, see Section <u>2.12.3.3</u>, “<u>Standards Violation Errors (According to VA Standards)</u>.”</p></td>
</tr>
<tr class="even">
<td><strong>I</strong></td>
<td><p><strong><u>Informational Errors</u>—</strong>These issues are <em>not</em> necessarily errors but still require attention, because they could indicate potential problems.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/083.png) <strong>REF:</strong> For a description and sample code analysis on errors in this category, see Section <u>2.12.3.4</u>, “<u>Informational Errors</u>.”</p></td>
</tr>
<tr class="odd">
<td><strong>Manual Check</strong></td>
<td><p><strong><u>Marked Items Errors (Manual Check</u>—</strong>These issues only apply if a line contains <strong>$TEXT</strong> <strong>($T)</strong>. <strong>XINDEX</strong> records the location and prints it out under the “Marked Items” sub-header on the <strong>XINDEX</strong> report.</p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/084.png) <strong>REF:</strong> For a description on errors in this category, see Section <u>2.12.3.5</u>, “<u>Marked Items Errors (Manual Check)</u>.”</p></td>
</tr>
</tbody>
</table>

<span id="_Ref311614132" class="anchor"></span>Table 7: XINDEX—List of Error Conditions (Messages) Flagged: Grouped by Category and Listed Alphabetically); Messages are Stored in XINDX1 Routine

<u>Table 7</u> lists the current error conditions (messages) that the XINDEX utility flags. XINDEX retrieves and displays the messages from the XINDX1 routine.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/085.png) NOTE: Any updates (such as add, modify, or delete messages) made to the list of XINDEX messages are based on changes to the XINDEX utility through subsequent Kernel Toolkit patches.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Message Displayed (click on link for more detail)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Category: <u>Fatal M Errors (Hard MUMPS Error)</u></strong></td>
</tr>
<tr class="even">
<td><u>F—Bad Number</u></td>
</tr>
<tr class="odd">
<td><u>F—Bad WRITE syntax</u></td>
</tr>
<tr class="even">
<td><u>F—Block structure mismatch</u></td>
</tr>
<tr class="odd">
<td><u>F—Call to missing label ‘label’ in this routine</u></td>
</tr>
<tr class="even">
<td><u>F—Call to this <em>label/routine</em> (MISSING LABEL)</u></td>
</tr>
<tr class="odd">
<td><u>F—Command missing an argument</u></td>
</tr>
<tr class="even">
<td><u>F—Error in pattern code</u></td>
</tr>
<tr class="odd">
<td><u>F—FOR Command followed by only one space</u></td>
</tr>
<tr class="even">
<td><u>F—FOR Command did not contain ‘=‘</u></td>
</tr>
<tr class="odd">
<td><u>F—General Syntax Error</u></td>
</tr>
<tr class="even">
<td><u>F—GO or DO mismatch from block structure (M45)</u></td>
</tr>
<tr class="odd">
<td><u>F—Invalid or wrong number of arguments to a function</u></td>
</tr>
<tr class="even">
<td><u>F—Label is not valid</u></td>
</tr>
<tr class="odd">
<td><u>F—Missing argument to a command post-conditional</u></td>
</tr>
<tr class="even">
<td><u>F—Non-standard (Undefined) ‘Z’ command</u></td>
</tr>
<tr class="odd">
<td><u>F—Quoted string not followed by a separator</u></td>
</tr>
<tr class="even">
<td><u>F—Reference to routine ‘^<em>routine name’</em>. That isn’t in this UCI</u></td>
</tr>
<tr class="odd">
<td><p><u>F—UNDEFINED COMMAND (rest of line not checked)</u></p>
<p>![](kernel-8-0-developer-s-guide-toolkit-user-guide/086.png) <strong>NOTE:</strong> Developers <em>must</em> manually check these errors.</p></td>
</tr>
<tr class="even">
<td><u>F—Undefined Function</u></td>
</tr>
<tr class="odd">
<td><u>F—Undefined Special Variable</u></td>
</tr>
<tr class="even">
<td><u>F—Unmatched Parenthesis</u></td>
</tr>
<tr class="odd">
<td><u>F—Unmatched Quotation Marks</u></td>
</tr>
<tr class="even">
<td><u>F—Unrecognized argument in SET command</u></td>
</tr>
<tr class="odd">
<td><strong>Category: <u>Warning Violation Errors (According to VA Conventions)</u></strong></td>
</tr>
<tr class="even">
<td><u>W—Blank(s) at end of line</u></td>
</tr>
<tr class="odd">
<td><u>W—Duplicate label, (M57)</u> (M standard error)</td>
</tr>
<tr class="even">
<td><u>W—First line label NOT routine name</u></td>
</tr>
<tr class="odd">
<td><u>W—Invalid global variable name</u></td>
</tr>
<tr class="even">
<td><u>W—Invalid local variable name</u></td>
</tr>
<tr class="odd">
<td><u>W—Line contains a CONTROL (non-graphic) character</u></td>
</tr>
<tr class="even">
<td><u>W—Null line (no commands or comment)</u></td>
</tr>
<tr class="odd">
<td><strong>Category: <u><br />
Standards Violation Errors (According to VA Standards</u></strong>)</td>
</tr>
<tr class="even">
<td><u>S—$View function used</u></td>
</tr>
<tr class="odd">
<td><u>S—Access to SSVN’s restricted to Kernel</u></td>
</tr>
<tr class="even">
<td><u>S—Break command used</u></td>
</tr>
<tr class="odd">
<td><u>S—Extended reference</u></td>
</tr>
<tr class="even">
<td><u>S—First line of routine violates the SAC</u></td>
</tr>
<tr class="odd">
<td><u>S—2nd line of routine violates the SAC</u></td>
</tr>
<tr class="even">
<td><u>S—Patch number ‘nnn’ missing from second line</u></td>
</tr>
<tr class="odd">
<td><u>S—‘HALT’ command should be invoked through ‘G ^XUSCLEAN’</u></td>
</tr>
<tr class="even">
<td><u>S—Kill of a protected variable (<em>variable name</em>)</u></td>
</tr>
<tr class="odd">
<td><u>S—Kill of an unsubscripted global</u></td>
</tr>
<tr class="even">
<td><u>S—Unargumented Kill</u></td>
</tr>
<tr class="odd">
<td><u>S—Exclusive Kill</u></td>
</tr>
<tr class="even">
<td><u>S—Exclusive or Unargumented NEW command</u></td>
</tr>
<tr class="odd">
<td><u>S—LABEL+OFFSET syntax</u></td>
</tr>
<tr class="even">
<td><u>S—Line is longer than 245 bytes</u></td>
</tr>
<tr class="odd">
<td><u>S—Lock missing Timeout</u></td>
</tr>
<tr class="even">
<td><u>S—Lower/Mixed case Variable name used</u></td>
</tr>
<tr class="odd">
<td><u>S—Lowercase command(s) used in line</u></td>
</tr>
<tr class="even">
<td><u>S—Non-Incremental Lock</u></td>
</tr>
<tr class="odd">
<td><u>S—Non-standard $Z function used</u></td>
</tr>
<tr class="even">
<td><u>S—Non-standard $Z special variable used</u></td>
</tr>
<tr class="odd">
<td><u>S—‘OPEN’ command should be invoked through ^%ZIS</u></td>
</tr>
<tr class="even">
<td><u>S—‘Close’ command should be invoked through ‘D ^%ZISC’</u></td>
</tr>
<tr class="odd">
<td><u>S—Read command doesn’t have a timeout</u></td>
</tr>
<tr class="even">
<td><u>S—Routine code exceeds SACC maximum size of 15000 (<em>nnnnn</em>)</u></td>
</tr>
<tr class="odd">
<td><u>S—Routine exceeds SACC maximum size of 20000 (<em>nnnnn</em>)</u></td>
</tr>
<tr class="even">
<td><u>S—Set to a ‘%’ global</u></td>
</tr>
<tr class="odd">
<td><u>S—Should use ‘TASKMAN’ instead of ‘JOB’ command</u></td>
</tr>
<tr class="even">
<td><u>S—View command used</u></td>
</tr>
<tr class="odd">
<td><u>S—Violates VA programming standards</u></td>
</tr>
<tr class="even">
<td><strong>Category: <u>Informational Errors</u></strong></td>
</tr>
<tr class="odd">
<td><u>I—QUIT Command followed by only one space</u></td>
</tr>
<tr class="even">
<td><u>I—Star or pound READ used</u></td>
</tr>
</tbody>
</table>

### Running the XINDEX Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-toolkit-user-guide/087.png) CAUTION: When running XINDEX to review an entire software application, it is best to queue the report for an off-peak time, since processing is intensive.

Use either of the following methods to call the XINDEX utility:

- Direct Mode Utility:

\>D ^XINDEX

![](kernel-8-0-developer-s-guide-toolkit-user-guide/088.png) REF: For examples using the Direct Mode Utility, see “<u>Examples</u>.”

- Option—Use the %Index of Routines \[XUINDEX\] option located on the on the Routine Tools \[XUPR-ROUTINE-TOOLS\] menu located on the Programmer Options \[XUPROG\] menu, which is locked with the XUPROG security key.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/089.png) REF: For more information on the %Index of Routines option, see the “<u>%Index of Routines Option—XINDEX</u>” section.

#### Examples

#### Example 1

Specifying a Routine Name Only:

<span id="_Toc199950786" class="anchor"></span>Figure 54: XINDEX—Direct Mode Utilities Sample User Entries: Specifying a Routine Name Only

KRN\><span class="mark">D ^XINDEX \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@14:47:16

All Routines? No =\> <span class="mark">\<Enter\></span> No

Routine: <span class="mark">XDRMAIN \<Enter\></span>

Routine: <span class="mark">\<Enter\></span>

1 routine

Select BUILD NAME: <span class="mark">\<Enter\></span>

Select INSTALL NAME: <span class="mark">\<Enter\></span>

Select PACKAGE NAME: <span class="mark">\<Enter\></span>

Print more than compiled errors and warnings? YES// <span class="mark">\<Enter\></span>

Print summary only? NO// <span class="mark">\<Enter\></span>

Print routines? YES// <span class="mark">\<Enter\></span>

Print (R)egular,(S)tructured or (B)oth? R// <span class="mark">\<Enter\></span>

Print errors and warnings with each routine? YES// <span class="mark">\<Enter\></span>

Save parameters in ROUTINE file? NO// <span class="mark">\<Enter\></span>

Index all called routines? NO// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">;P-OTHER \<Enter\></span> Telnet Terminal Right Margin: 255// <span class="mark">80 \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@14:47:16

Routines: 1 Faux Routines: 0

XDRMAIN

--- CROSS REFERENCING ---

Compiled list of Errors and Warnings Jan 12, 2012@14:47:16 page 1

No errors or warnings to report

--- Routine Detail --- with REGULAR ROUTINE LISTING ---

XDRMAIN \* \* 80 Lines, 3431 Bytes, Checksum: B16902409

Jan 12, 2012@14:47:16 page 2

104 bytes in comments

XDRMAIN ;SF-IRMFO/IHS/OHPRD/JCM - MAIN DRIVER FOR DUPLICATE MERGE SOFTWARE;

\[ 08/13/92 09:50 AM \]

;;7.3;TOOLKIT;\*\*23\*\*;r 25, 1995

;;

START ;

S XDRMAINI="MERGE" D ^XDRMAINI G:XDRQFLG END

F XDRMI1=0:0 S XDRMPAIR=\$O(@XDRM("GL")) Q:'XDRMPAIR!(XDRQFLG) S XDRMPD

A="^VA(15,""OT"","\_""""\_\$P(XDRGL,U,2)\_""""\_",XDRMPAIR,0)" S XDRMPDA=

\$O(@XDRMPDA) D MAIN D:'\$D(XDRM("NOTALK")) ASK

END D EOJ

Q

;

MAIN ;

S XDRMCD=\$P(XDRMPAIR,U,1),XDRMCD2=\$P(XDRMPAIR,U,2)

S XDRMRG("LCK")="+" D LOCK^XDRU1 K XDRMRG("LCK") I \$D(XDRMLOCK) G MAINX

I '\$D(XDRM("NOVERIFY")) S XDRMRG=0 D ^XDRMVFY G:'XDRMRG!(XDRQFLG) MAINX

S (XDRMRG("FR"),XDRMAIN("FR"))=\$S(\$P(^VA(15,XDRMPDA,0),U,4)=2:XDRMCD2,1

:XDRMCD)

.

.

.

#### Example 2

Specifying a Build Name:

<span id="_Ref311528489" class="anchor"></span>Figure 55: XINDEX—Direct Mode Utilities Sample User Entries: Specifying a Build Name

\><span class="mark">D ^XINDEX \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@14:47:16

All Routines? No =\> <span class="mark">\<Enter\></span> No

Routine: <span class="mark">\<Enter\></span>

0 routines

Select BUILD NAME: <span class="mark">XT\*7.3\*102 \<Enter\></span> TOOLKIT

Include the compiled template routines: N// <span class="mark">\<Enter\></span>

Print more than compiled errors and warnings? YES// <span class="mark">\<Enter\></span>

Print summary only? NO// <span class="mark">\<Enter\></span>

Print routines? YES// <span class="mark">\<Enter\></span>

Print (R)egular,(S)tructured or (B)oth? R// <span class="mark">\<Enter\></span>

Print the DDs, Functions, and Options? YES// <span class="mark">\<Enter\></span>

Print errors and warnings with each routine? YES// <span class="mark">\<Enter\></span>

Save parameters in ROUTINE file? NO// <span class="mark">\<Enter\></span>

Index all called routines? NO// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">;P-OTHER \<Enter\></span> Telnet Terminal Right Margin: 255// <span class="mark">80 \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@14:43:02

The BUILD file Data Dictionaries are being processed.

The option and function files are being processed.

Routines are being processed.

Routines: 1 Faux Routines: 0

XTPOST

--- CROSS REFERENCING ---

Compiled list of Errors and Warnings Jan 12, 2012@14:59:51 page 1

XTPOST \* \* 106 Lines, 3234 Bytes, Checksum: B14328994

;;8.0;KERNEL;\*\*102\*\*;Jul 10, 1995

XTPOST+1 S - 2nd line of routine violates the SAC.

.S \$P(^%ZRTL(3.091,0),U)="RESPONSE TIME"

CHECK+34 S - Set to a '%' global.

.S \$P(^%ZRTL(3.091,0),U,2)="3.091P"

CHECK+35 S - Set to a '%' global.

.S \$P(^%ZRTL(3.092,0),U)="RT DATE_UCI,VOL"

CHECK+38 S - Set to a '%' global.

.S \$P(^%ZRTL(3.092,0),U,2)="3.092"

CHECK+39 S - Set to a '%' global.

.S \$P(^%ZRTL(3.094,0),U)="RT RAWDATA"

CHECK+42 S - Set to a '%' global.

.S \$P(^%ZRTL(3.094,0),U,2)="3.094D"

CHECK+43 S - Set to a '%' global.

--- Routine Detail --- with REGULAR ROUTINE LISTING ---

.

.

.

#### Example 3

Specifying a Package Name:

<span id="_Toc199950788" class="anchor"></span>Figure 56: XINDEX—Direct Mode Utilities Sample User Entries: Specifying a Package Name

\><span class="mark">D ^XINDEX \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@15:01:53

All Routines? No =\> <span class="mark">\<Enter\></span> No

Routine: <span class="mark">XDRMAIN \<Enter\></span>

Routine: <span class="mark">\<Enter\></span>

1 routine<span class="mark">\<Enter\></span>

Select BUILD NAME: <span class="mark">\<Enter\></span>

Select INSTALL NAME: <span class="mark">\<Enter\></span>

Select PACKAGE NAME: <span class="mark">KERNEL \<Enter\></span> XU

Include the compiled template routines: N// <span class="mark">\<Enter\></span>

Print more than compiled errors and warnings? YES// <span class="mark">\<Enter\></span>

Print summary only? NO// <span class="mark">\<Enter\></span>

Print routines? YES// <span class="mark">\<Enter\></span>

Print (R)egular,(S)tructured or (B)oth? R// <span class="mark">\<Enter\></span>

Print the DDs, Functions, and Options? YES// <span class="mark">\<Enter\></span>

Print errors and warnings with each routine? YES// <span class="mark">\<Enter\></span>

Save parameters in ROUTINE file? NO// <span class="mark">\<Enter\></span>

Index all called routines? NO// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">;P-OTHER \<Enter\></span> Telnet Terminal Right Margin: 255// <span class="mark">80 \<Enter\></span>

V. A. C R O S S R E F E R E N C E R 7.3

\[2008 VA Standards & Conventions\]

UCI: KRN CPU: KRN Jan 12, 2012@15:01:53

The package file Data Dictionaries are being processed.

The option and function files are being processed.

Routines are being processed.

Routines: 1 Faux Routines: 2

XDRMAIN

Data Dictionaries

\|func \|opt

--- CROSS REFERENCING ---

Compiled list of Errors and Warnings Jan 12, 2012@15:01:53 page 1

\|opt \* \* 974 Lines, 35949 Bytes, Checksum:

I '\$P(^VA(200,D0,0),U,11),\$P(^(0),U,4)="@"!(\$N(^("FOF",0))\>0)

161+4 F - Undefined Function.

589+2 F - Reference to routine '^XUCSPRG'. That isn't in this UCI.

--- Routine Detail --- with REGULAR ROUTINE LISTING ---

.

.

.

### Analysis of XINDEX Error Findings by Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Fatal M Errors (Hard MUMPS Error)

These are unrecoverable errors that cause a program to fail if the commands are executed. It is possible, however, that these types of errors might exist in routines that run correctly. The error occurs (or may occur, depending on the underlying implementation) only when the errant commands are executed.

#### F—Bad Number

XINDEX can only check static numbers in code. It does *not* check the boundaries of the number, only that it is a legitimate number and *not* a string.

#### F—Bad WRITE syntax

This error is usually a WRITE argument misuse. The most common occurrence is due to a missing comma after the argument.

#### F—Block structure mismatch

These are potentially one of the most serious types of errors and may lead to fatal runtime exceptions. However, examination of several routines indicates that a significant number of these errors are empty DO blocks. These are still potential logic errors, but do *not* cause runtime exceptions under Caché. The DO command, Section 8.2.3 of the standard, does *not* seem to have a provision for empty blocks, so this is an error.

<u>Figure 57</u> is a code extract from ENGET^DGRUGMFU is an example of this type of error:

<span id="_Ref62648697" class="anchor"></span>Figure 57: F - Block structure mismatch—Sample Code Error

ENGET() ;DETERMINE DIVISION TO GET SUBSCRIBERS

;

N I,J,X

F I=1:1 X HLNEXT Q:HLQUIT'\>0 D

.S X(I)=HLNODE,J=0

<span class="mark">..F S J=\$O(HLNODE(J)) Q:'J S X(I,J)=HLNODE(J)</span>

Because there is no DO command before the double dot syntax, that line is never executed.

#### F—Call to missing label ‘*label*’ in this routine

In this case, reference is made to a label inside a routine that is *not* (or no longer) present. There could be many reasons for this. The most likely candidate being removal of code that is no longer used.

#### F—Call to this *label/routine* (MISSING LABEL)

This is the complementary situation in which code calls a label/routine that is no longer present on the system. Again, there are several reasons why this might occur, including typographical errors and removal of code that is no longer used.

#### F—Command missing an argument

This is another syntax type error. Most M command arguments are optional. This error is usually associated with the WRITE argument tab character, which is the question mark (?). It *must* be followed by an integer or variable.

#### F—Error in pattern code

XINDEX checks that only the seven pattern codes (that is ACELNPU) of the 1995 M Standard are used. They also can be lowercase (that is acelnpu). The seven pattern codes are defined as:

- A—Alphabetic
- C—Control
- E—Every Character
- L—Lowercase
- N—NUMERIC
- P—Punctuation
- U—Uppercase

#### F—FOR Command followed by only one space

This error is only for the argumentless FOR command. It *must* be followed by two spaces.

#### F—FOR Command did not contain ‘=’

XINDEX checks that if the FOR command has an argument, it *must* set a variable.

#### F—General Syntax Error

This error indicates a construct that is *not* valid M syntax and is otherwise unrecognized. Almost any malformed code is possible here.

#### F—GO or DO mismatch from block structure (M45)

This is another error that has to do with the dot syntax used to create anonymous blocks in standard M. Typically, a GOTO that jumps from one stack level to another would generate this type of error.

<span id="_Toc199950790" class="anchor"></span>Figure 58: F—GO or DO mismatch from block structure (M45)—Sample Code Error

TEST ;test routine

F I=1:1 D

. S X=1,Y=Z

.I Y\>0 <span class="mark">G QUIT^TESTA</span>

.S Z=0

In this example, the code is trying to GO out of the DO block to another routine.

#### F—Invalid or wrong number of arguments to a function

This error involves calling functions with the wrong number of arguments, or with invalid argument syntax.

#### F—Label is not valid

M allows the arguments to commands (such as DO) to be specified indirectly (that is using the @ syntax). What is *not* standard, however, is to use indirection just to specify the *label* in a label^routine combination.

The following code extract from EN+6^MXMLPRSE is invalid:

<span id="_Toc199950791" class="anchor"></span>Figure 59: F - Label is not Valid—Sample Code Error

F Q:EOD <span class="mark">D</span> READ,EPOS<span class="mark">,@ST^MXMLPRS0</span>:'EOD

#### F—Missing argument to a command post-conditional

Most M commands allow a post condition, which is designated by a colon and followed by the argument. This error occurs if the argument is missing.

#### F—Non-standard (Undefined) ‘Z’ command

XINDEX flags all uses of Z commands. Vendor-specific commands use the Z prefix. The SAC restricts the use of such commands to Kernel. You may occasionally see other packages make use of these commands, but in these cases, an exemption is required.

#### F—Quoted string not followed by a separator

XINDEX checks that anywhere a quoted string is used, it *must* stand alone or have a separator after it.

#### F—Reference to routine ‘^*routine name*’. That isn’t in this UCI

These errors flag references to routines that are *not* present on the system.

#### F—UNDEFINED COMMAND (rest of line not checked)

This is a syntax error. It requires a manual check of the line/routine.

#### F—Undefined Function

Checks that a function is part of the M standard.

#### F—Undefined Special Variable

This is essentially the same as the “<u>F - Undefined Function</u>” error. The only difference is that in M special variables are built-in functions that take no arguments.

#### F—Unmatched Parenthesis

This is a syntax error. XINDEX checks that the static code has matching parenthesis. It does have problems when indirection is used, which are evaluated during execution.

#### F—Unmatched Quotation Marks

This is a syntax error. XINDEX checks that the static code has matching quotation marks. It does have problems when indirection is used, which are evaluated during execution.

#### F—Unrecognized argument in SET command

XINDEX checks the syntax of the SET statement. It does have problems when indirection is used, which are evaluated during execution.

#### Warning Violation Errors (According to VA Conventions)

These are potential problems that are *not* necessarily fatal errors but most likely indicate an error. They require careful implementation.

#### W—Blank(s) at end of line

Standard M has very specific whitespace requirements. Some text editors create extra whitespace that is caught by XINDEX.

#### W—Duplicate label, (M57)

This is an M standard error. During execution, the first occurrence of the label is executed.

#### W—First line label NOT routine name

The first line of VistA routines is required to be a label that is the same as the routine name.

#### W—Invalid global variable name

Checks that the global name is uppercase and *not* longer than eight characters.

#### W—Invalid local variable name

XINDEX checks that the local variable name is uppercase and *not* longer than sixteen characters.

#### W—Line contains a CONTROL (non-graphic) character

The only *non*-graphic characters permitted in VistA routines are whitespace.

#### W—Null line (no commands or comment)

Every line in an M routine *must* contain at least one character. The most common single character is the semi-colon (;), which denotes a comment.

#### Standards Violation Errors (According to VA Standards)

These are issues that do *not* pertain to the M language *per se*, but rather the requirements of the VA Standards and Conventions (SAC). Issues flagged as Standards Violations can still be syntactically correct M code that follows the portability guidelines but does *not* follow the more stringent requirements set forth in the SAC.

#### S—\$View function used

The \$VIEW function directly examines memory. The use of \$VIEW is restricted to Kernel and VA FileMan.

#### S—Access to SSVN’s restricted to Kernel

Structured System Variable Names (SSVNs) are a mechanism used to provide programmatic information to certain system information and are covered in Section 7.1.3 of the M language standard. The use of SSVNs is restricted to Kernel.

Common SSVNs include the following:

- ^\$ROUTINE
- ^\$JOB
- ^\$LOCK
- ^\$GLOBAL

#### S—Break command used

The BREAK command is prohibited except for Kernel.

If applications ever need to use BREAK, they should use ^%ZOSF(“BRK”) and ^%ZOSF(“NBRK”) instead.

#### S—Extended reference

In M, use extended references to refer to routines or globals outside the current environment (called a namespace in Caché). The use of extended references is restricted to Kernel.

#### S—First line of routine violates the SAC

Section 2.2.1 of the SAC specifies the format of the first line of a routine as follows:

2.2.1 The first line of a routine *must* be in the following format: routine name\<ls\>; site/programmer\<space\>-\<space\>brief description \[optional space\];date \[time is optional\].

ZZAA12 ;DALOI/XXX - Example Routine;2/13/07

![](kernel-8-0-developer-s-guide-toolkit-user-guide/090.png) NOTE: M editors frequently modify the first line of a routine.

#### S—2nd line of routine violates the SAC

In VistA, the second line of routines records the following information:

- Package/Application version number
- Package/Application name
- Patches ID numbers (if any applied)
- Original routine creation date and time
- Build number

Section 2.2.2 of the SAC specifies the second line format as follows:

> 2.2.2 The second line of a routine *must* be in the following format: \[LABEL-optional\]\<ls\>;;version number; package name; \*\*pm,...pn\*\*; version date;Build n where:

> ;;1.0;PACKAGE;\*\*pm,…pn\*\*;Feb 1, 2007;Build 1

#### S—Patch number ‘*nnn*’ missing from second line

The list of patch numbers *must* fall between the set of asterisks (\*\*) and be separated by commas as shown in Section 2.2.2 of the SAC (see Section <u>2.12.3.3.6</u>).

#### S—‘HALT’ command should be invoked through ‘G ^XUSCLEAN’

The HALT command causes a program to exit; this is *not* a common requirement in VistA. If for some reason a routine needs to halt, you *must* first perform certain housekeeping tasks. Kernel provides an API to cleanly halt a program. Application programs *cannot* use the HALT command.

Anomaly

This reported error message is out of date; applications should use [H^XUS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf#h_xus) (see Section 2.4.3 of the SAC).

#### S—Kill of a protected variable (*variable name*)

Kernel makes use of certain local variables to maintain a standard environment for processes. Applications *cannot*KILL the following variables:

- DT
- DTIME
- DUZ
- IOST
- IOM
- U

#### S—Kill of an unsubscripted global

The SAC specifies that unsubscripted globals shall be KILLed:

> 2.3.2.3 The KILLing of unsubscripted globals is prohibited and should be protected. (Special instruction to the site is required to enable the KILLing of an unsubscripted global. Application developers *must* document when calls to EN^DIU2 are made to delete files stored in unsubscripted globals).

#### S—Unargumented Kill

Kernel maintains a set of local variables that *cannot* be SET or KILLed. The unargumented KILL is prohibited except for Kernel.

#### S—Exclusive Kill

The use of the exclusive KILL is prohibited except for Kernel.

#### S—Exclusive or Unargumented NEW command

The exclusive NEW command is the same as the exclusive KILL and is restricted except for Kernel.

#### S—LABEL+OFFSET syntax

The only situation in which application routines are allowed to use the LABEL+OFFSET syntax to refer to lines of code is when using \$TEXT to retrieve data lines. For example, it *cannot* be used in conjunction with a DO or GOTO command.

#### S—Line is longer than 245 bytes

Lines of code *cannot* be longer than 245 bytes.

#### S—Lock missing Timeout

In M, a LOCK command may include a timeout. If the specified timeout period expires before obtaining the lock, the LOCK command fails. In VistA, application programs are required to specify a timeout when using this command. If for some reason it is necessary to use a LOCK with no timeout (such as to manage collaborating processes), an exemption is required.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/091.png) NOTE: Kernel can use locks *without* a timeout. Kernel can also use *non*-incremental and unargumented locks.

#### S—Lower/Mixed case Variable name used

The rules regarding variable case have been relaxed somewhat in the most recent revision of the SAC. The relevant sections are:

> 2.2.5 The line body *must* contain at least 1 printable character, *mustnot* exceed 245 characters in length, and *must* contain only the ASCII characters values 32-126. Line labels, global variable names, system variables, SSVNs, and so on *must* be uppercase.

> 2.3.1.1 Local variable names may *not* exceed sixteen characters. Namespaced variables may *not* contain lowercase characters. Variables local to a routine, subroutine or DoDot may be any case. Any variable containing lowercase characters *must* be NEWed at the beginning of the routine, subroutine or DoDot.

#### S—Lowercase command(s) used in line

All M commands *must* be uppercase. They can be spelled out or abbreviated to the first character.

#### S—Non-Incremental Lock

M allows locks to be one of the following types:

- Incremental—Allows a process to maintain multiple locks on the same resource and release them one at a time.
- *Non-*Incremental—Either a process obtains the lock or the command fails.

Application programs are required to use the incremental form of the LOCK command.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/092.png) NOTE: This restriction does *not* apply to Kernel.

#### S—Non-standard \$Z function used

M implementations may provide special functions with names beginning with \$Z. These are platform dependent. Application programs *cannot* use them.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/093.png) NOTE: This restriction does *not* apply to Kernel.

#### S—Non-standard \$Z special variable used

M implementations may provide special variables with names beginning with \$Z. These are platform dependent. Application programs *cannot* use them.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/094.png) NOTE: This restriction does *not* apply to Kernel.

#### S—‘OPEN’ command should be invoked through ^%ZIS

Applications *cannot* directly use the OPEN and CLOSE commands. Instead, they *must* use the Kernel Device Handler.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/095.png) NOTE: This restriction does *not* apply to Kernel, MailMan, and VA FileMan. See the noted exemptions in Section 2.4.8.1 of the SAC.

#### Anomaly

This error is a bit misleading, because there are now several APIs other than [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) that can be used. This includes:

- ^%ZISH
- ^%ZISUTL
- ^%ZISTCP

Regardless, applications *must* use one of the ^%ZIS\* APIs and *cannot* use OPEN directly.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/096.png) REF: For more details of the CLOSE command, see the “<u>S—‘Close’ command should be invoked through ‘D ^%ZISC’</u>” section.

#### S—‘Close’ command should be invoked through ‘D ^%ZISC’

Kernel’s Device Handler encapsulates certain I/O-related commands (such as OPEN and CLOSE) and provides a common device abstraction used by VistA applications. Applications are required to use the Device Handler.

At one time, devices were always opened using D ^%ZIS and closed using D ^%ZISC, but that is no longer true. Kernel provides some additional APIs:

- ^%ZISH for working with host files (that is, operating system files).
- ^%ZISUTL to make working with multiple devices easier.
- ^%ZISTCP for TCP connections.

If a device is opened using [OPEN^%ZISUTL](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#open_zisutl), it *must* be closed with [CLOSE^%ZISUTL](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#close_zisutl). Do *not* close the device through the CLOSE command.

#### S—Read command doesn’t have a timeout

Application programs *must* provide a timeout (usually the variable DTIME) when using the READ command. In fact, it is good practice for applications to *not* use READ at all but use the VA FileMan ^%DIR API (commonly known as the “Response Reader”); though, this is *not* a requirement. It is, however, a requirement to use a timeout.

In addition, if a timeout exceeds 300 seconds, you *must* document that fact in the package technical manual.

If for some reason this is inappropriate, an exemption is required.

#### S—Routine code exceeds SACC maximum size of 15000 (*nnnnn*)

The maximum routine size for M code and ;; comments (comments beginning with double semi-colons are considered code) is set to 15K characters in a routine.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/097.png) NOTE: An additional 5K characters in a routine is available for regular comments (that is comments beginning with a single semi-colon).

#### S—Routine exceeds SACC maximum size of 20000 (*nnnnn*)

The maximum routine size as determined by ^%ZOSF(“SIZE”) is set to 20K for all characters in a routine.

#### S—Set to a ‘%’ global

Application programs *cannot* modify globals with names beginning with %.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/098.png) NOTE: This restriction does *not* apply to Kernel.

#### S—Should use ‘TASKMAN’ instead of ‘JOB’ command

This is a requirement. Application programs *cannot* start background processes with the JOB command but *must* use one of the APIs provided by TaskMan.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/099.png) NOTE: This restriction does *not* apply to Kernel.

#### S—View command used

The VIEW command modifies memory or disk buffers. Use of this command is restricted to Kernel and VA FileMan.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/100.png) REF: For more details about VIEW and \$VIEW, see the “<u>S—\$View function used</u>” section.

#### S—Violates VA programming standards

This is something of a catchall category and requires manual review for violations of VA programming standards.

#### Informational Errors

These issues are *not* necessarily errors but still require attention, because they could indicate potential problems.

#### I—QUIT Command followed by only one space

This is another whitespace issue. In standard M, a routine is terminated by a single QUIT command and a function returns a value with a QUIT followed by a single space and then an expression that evaluates to the value to be returned. When you encounter a QUIT followed by a space, it is most likely extra whitespace at the end of a line.

#### I—Star or pound READ used

In M, READ is normally a line-oriented command. However, there are two syntactic variations on the READ command where its use is inappropriate:

<span id="_Toc199950792" class="anchor"></span>Figure 60: API—Star or pound READ used—Syntactic Variation (1 of 2)

READ \*X

Reads a single character into X.

<span id="_Toc199950793" class="anchor"></span>Figure 61: API—Star or pound READ used—Syntactic Variation (2 of 2)

READ X#100

Reads 100 contiguous characters (bytes on most M systems) into X. Use of so-called star and pound READs was once disallowed but is now permitted so long as applications follow other relevant standards.

#### Marked Items Errors (Manual Check)

You *must* manually check flagged references under Marked Items.

Currently, Marked Items only apply if a line contains \$TEXT (\$T). XINDEX records the location of the \$T code and prints it out under the “Marked Items” sub-header on the XINDEX report, since XINDEX does *not* check the references of a \$T.

M uses the \$TEXT function to retrieve lines from a routine, and routines sometimes incorporate data items that are retrieved in this fashion. Section 2.2.4 of the SAC describes the required format for lines referenced by \$TEXT, which states (in part):

> 2.2.4.1 LABEL+OFFSET references will *not* be used except for \$TEXT references.

> 2.2.4.2 Lines referenced by \$TEXT for use other than to check for the existence of a routine or a line label in that routine *must* be in the following format: \[LABEL-optional\]\<ls\>;;text or M code.

In standard M, a semicolon (;) introduces comments. A double semicolon (;;) indicates that the comment should be preserved even if the routine is compiled. The LABEL+OFFSET syntax is required to prevent errors that could be introduced if lines are inserted ahead of the label. According to the SAC, if code uses \$T, the reference *must* start with a double semicolon (;;).

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-toolkit-user-guide/101.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-toolkit-user-guide/102.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-toolkit-user-guide/103.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.