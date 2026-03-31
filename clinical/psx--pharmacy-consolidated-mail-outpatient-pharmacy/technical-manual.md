---
consolidated_title: "technical manual change pages"
app_code: PSX
doc_type: TM
master_source: "PSX*2*65 Technical Manual Change Pages"
master_pub_date: April 1997
consolidated_from: 2 versions
prior_versions:
  - "PSX*2*71 Technical Manual Change Pages"
---

> ![](psx-2-65-technical-manual-change-pages/001.png)

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP)

> TECHNICAL MANUAL

> Version 2.0

> April 1997

> (Revised July 2009)

> Department of Veterans Affairs VistA Health Systems Design & Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Routine List](#routine-list)
> Each time this manual is updated, the Title Page lists the new revised date and this page
> describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Revision Date</strong></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2009</td>
<td><blockquote>
<p>i, 33</p>
</blockquote></td>
<td><blockquote>
<p>PSX*2*65</p>
</blockquote></td>
<td>Added PSXRPPL2 and PSXBPSR1 to the routine List. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/2007</td>
<td><blockquote>
<p>33, 65, 68-</p>
<p>69, 71, 75,</p>
<p>75a-b, 77</p>
</blockquote></td>
<td><blockquote>
<p>PSX*2*54</p>
</blockquote></td>
<td><p>Added PSXBLD1 to the Routine List. Updated affected HL7 segments to reference the new warning label source.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/2006</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSX*2*61</p>
</blockquote></td>
<td><p>Encapsulation II Follow-up Patches. Added PSX550 to the Routine List. (Clean-up - fixed both Table of Contents, added blank pages, deleted headers, re-numbered pages, etc.) This is a re-issue of the full manual.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/1997</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>
> July 2009 Consolidated Mail Outpatient Pharmacy V. 2.0 i Technical Manual
> PSX\*2\*65
> (*Page intentionally left blank for two-sided copying.*)
> ii Consolidated Mail Outpatient Pharmacy V. 2.0 July 2009 Technical Manual
> PSX\*2\*65

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of routines you will see for Consolidated Mail Outpatient Pharmacy (including those patched through PSX\*2\*48) when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the *First Line Routine Print* \[XU FIRST LINE PRINT\] option found within the Kernel *Routine Tools*

> \[XUPR-ROUTINE-TOOLS\] menu to print the first line description of each PSX\* routine.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>PSX41NDX</th>
<th>PSX41PRE</th>
<th>PSX41PST</th>
<th><blockquote>
<p>PSX550</p>
</blockquote></th>
<th><blockquote>
<p>PSXACK</p>
</blockquote></th>
<th><blockquote>
<p>PSXACT</p>
</blockquote></th>
<th>PSXARC</th>
<th><blockquote>
<p>PSXARC1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSXARC2</td>
<td>PSXARPT</td>
<td>PSXATREJ</td>
<td><blockquote>
<p>PSXAUTO</p>
</blockquote></td>
<td><blockquote>
<p>PSXAUTOC</p>
</blockquote></td>
<td><blockquote>
<p>PSXBKD</p>
</blockquote></td>
<td>PSXBKG</td>
<td><blockquote>
<p>PSXBLD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXBLD1</td>
<td>PSXBPSMS</td>
<td>PSXBPSR1</td>
<td><blockquote>
<p>PSXBPSRP</p>
</blockquote></td>
<td><blockquote>
<p>PSXBPSUT</p>
</blockquote></td>
<td><blockquote>
<p>PSXCH</p>
</blockquote></td>
<td>PSXCHENV</td>
<td><blockquote>
<p>PSXCMOP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXCMOP0</td>
<td>PSXCMOP1</td>
<td>PSXCOSTU</td>
<td><blockquote>
<p>PSXCRENV</p>
</blockquote></td>
<td><blockquote>
<p>PSXCSCMN</p>
</blockquote></td>
<td><blockquote>
<p>PSXCSDA</p>
</blockquote></td>
<td>PSXCSDC</td>
<td><blockquote>
<p>PSXCSDC1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXCSDC2</td>
<td>PSXCSHI</td>
<td>PSXCSHI1</td>
<td><blockquote>
<p>PSXCSLG1</p>
</blockquote></td>
<td><blockquote>
<p>PSXCSLOG</p>
</blockquote></td>
<td><blockquote>
<p>PSXCSMN1</p>
</blockquote></td>
<td>PSXCSMON</td>
<td><blockquote>
<p>PSXCSSUM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXCST</td>
<td>PSXCST1</td>
<td>PSXCSTPG</td>
<td><blockquote>
<p>PSXCSUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSXDB</p>
</blockquote></td>
<td><blockquote>
<p>PSXDENT</p>
</blockquote></td>
<td>PSXDODAC</td>
<td><blockquote>
<p>PSXDODAK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXDODAT</td>
<td>PSXDODB</td>
<td>PSXDODB1</td>
<td><blockquote>
<p>PSXDODFX</p>
</blockquote></td>
<td><blockquote>
<p>PSXDODH</p>
</blockquote></td>
<td><blockquote>
<p>PSXDODH1</p>
</blockquote></td>
<td>PSXDODNT</td>
<td><blockquote>
<p>PSXDODQY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXDQUE</td>
<td>PSXDQUEC</td>
<td>PSXDRPT</td>
<td><blockquote>
<p>PSXDUAL</p>
</blockquote></td>
<td><blockquote>
<p>PSXEDIT</p>
</blockquote></td>
<td><blockquote>
<p>PSXEDRG</p>
</blockquote></td>
<td>PSXEDUTL</td>
<td><blockquote>
<p>PSXERR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXERR1</td>
<td>PSXHENV</td>
<td>PSXHL7</td>
<td><blockquote>
<p>PSXHL71</p>
</blockquote></td>
<td><blockquote>
<p>PSXHSYS</p>
</blockquote></td>
<td><blockquote>
<p>PSXHSYS1</p>
</blockquote></td>
<td>PSXJOB</td>
<td><blockquote>
<p>PSXLBL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXLBL1</td>
<td>PSXLBL2</td>
<td>PSXLBLNR</td>
<td><blockquote>
<p>PSXLBLPT</p>
</blockquote></td>
<td><blockquote>
<p>PSXLBLT</p>
</blockquote></td>
<td><blockquote>
<p>PSXLBLU</p>
</blockquote></td>
<td>PSXLIST</td>
<td><blockquote>
<p>PSXLKUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXLM1</td>
<td>PSXLTST</td>
<td>PSXMISC</td>
<td><blockquote>
<p>PSXMISC1</p>
</blockquote></td>
<td><blockquote>
<p>PSXMSGS</p>
</blockquote></td>
<td><blockquote>
<p>PSXMST</p>
</blockquote></td>
<td>PSXNEW</td>
<td><blockquote>
<p>PSXNOCMP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXNOTE</td>
<td>PSXOCMOP</td>
<td>PSXOPUTL</td>
<td><blockquote>
<p>PSXPLOG</p>
</blockquote></td>
<td><blockquote>
<p>PSXPOST</p>
</blockquote></td>
<td><blockquote>
<p>PSXPOST1</p>
</blockquote></td>
<td>PSXPST32</td>
<td><blockquote>
<p>PSXPURG</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXPURG1</td>
<td>PSXQRY</td>
<td>PSXQUE</td>
<td><blockquote>
<p>PSXRACT</p>
</blockquote></td>
<td><blockquote>
<p>PSXRCVRY</p>
</blockquote></td>
<td><blockquote>
<p>PSXRECV</p>
</blockquote></td>
<td>PSXRECV1</td>
<td><blockquote>
<p>PSXREF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXREJ</td>
<td>PSXREL</td>
<td>PSXRENV</td>
<td><blockquote>
<p>PSXRESUB</p>
</blockquote></td>
<td><blockquote>
<p>PSXRHLP</p>
</blockquote></td>
<td><blockquote>
<p>PSXRPPL</p>
</blockquote></td>
<td>PSXRPPL1</td>
<td><blockquote>
<p>PSXRPPL2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXRPT</td>
<td>PSXRSTAT</td>
<td>PSXRSUS</td>
<td><blockquote>
<p>PSXRSUS1</p>
</blockquote></td>
<td><blockquote>
<p>PSXRSYU</p>
</blockquote></td>
<td><blockquote>
<p>PSXRTN</p>
</blockquote></td>
<td>PSXRTN1</td>
<td><blockquote>
<p>PSXRTR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXRTRA1</td>
<td>PSXRTRAN</td>
<td>PSXRTRAO</td>
<td><blockquote>
<p>PSXRXQU</p>
</blockquote></td>
<td><blockquote>
<p>PSXRXU</p>
</blockquote></td>
<td><blockquote>
<p>PSXSERV</p>
</blockquote></td>
<td>PSXSITE</td>
<td><blockquote>
<p>PSXSMRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXSND</td>
<td>PSXSRP</td>
<td>PSXSRST</td>
<td><blockquote>
<p>PSXSTAT</p>
</blockquote></td>
<td><blockquote>
<p>PSXSTP</p>
</blockquote></td>
<td><blockquote>
<p>PSXSTRT</p>
</blockquote></td>
<td>PSXSUDCN</td>
<td><blockquote>
<p>PSXSYS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSXTL</td>
<td>PSXTNRPT</td>
<td>PSXUNHLD</td>
<td><blockquote>
<p>PSXUNREL</p>
</blockquote></td>
<td><blockquote>
<p>PSXUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSXVCK</p>
</blockquote></td>
<td>PSXVCK1</td>
<td><blockquote>
<p>PSXVEND</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSXVIEW</td>
<td>PSXVND</td>
<td>PSXVPN</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

July 2009 Consolidated Mail Outpatient Pharmacy V. 2.0 33

> Technical Manual PSX\*2\*65

> (*Page intentionally left blank for two-sided copying*.)

> 34 Consolidated Mail Outpatient Pharmacy V. 2.0 July 2009 Technical Manual

> PSX\*2\*65