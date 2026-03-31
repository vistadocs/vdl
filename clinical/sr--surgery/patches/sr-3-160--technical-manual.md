---
title: SR*3*160 Surgery NSQIP-CICSP 2007 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Surgery NSQIP-CICSP 2007 /Security Guide Change Pages
app_code: SR
app_name: Surgery
section: CLI
app_status: active
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*160
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 3
description: > ![](sr-3-160-surgery-nsqip-cicsp-2007-technical-manual-security-guide-change-pages/001.png)
audience: 
keywords: 
  - blockquote
  - strong
  - mark
  - class
  - added
  - table
  - routines
  - routine
  - updated
  - surgery
page_count: 0
word_count: 833
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p160_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p160_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=103"
---

> ![](sr-3-160-surgery-nsqip-cicsp-2007-technical-manual-security-guide-change-pages/001.png)

SURGERY

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 3.0

> July 1993

> (Revised June 2007)

> Department of Veterans Affairs

> VistA Health Systems Design & Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Routines](#routines)
- [File Security](#file-security)
> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/07</td>
<td>21-22, 81</td>
<td>SR*3*160</td>
<td><blockquote>
<p>Added these routines to the routine listing: SR160UT0, SR160UTL, SROALEC, SROAX. Corrected the File Security section, which is unrelated to this patch.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/06</td>
<td>15-16, 21-22, 54-55</td>
<td>SR*3*153</td>
<td><blockquote>
<p>Added new information regarding laboratory tests to the Implementation and Maintenance section. Added the routine SROALMN to the routine listing, and updated the Calls Made by Surgery section to reflect current external calls.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/06</td>
<td>iv, 21-22, 85-96</td>
<td>SR*3*144</td>
<td><blockquote>
<p>Updated the Table of Contents. Added these routines to the routine listing: SRCHL7A, SRCHL7U, SROPFSS. Added Appendix A: Surgery Source Data Elements for PFSS, and updated and renumbered the Index.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/06</td>
<td>21-28, 75</td>
<td>SR*3*146</td>
<td><blockquote>
<p>Added the routine SROACOD to the routine listing. Added the <em>Alert Coder Regarding Coding Issues</em> [SROA CODE ISSUE] option to the Exported Options and Menus sections.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>04/06</td>
<td><p>17, 21-22, 29, 34-</p>
<p>35, 41, 51-52, 81</p></td>
<td>SR*3*142</td>
<td><blockquote>
<p>Updated the Files and File Security sections to include the new SURGERY PROCEDURE/DIAGNOSIS</p>
<p>CODES file (#136). Added these new routines to the routine listing: SROCD, SROCD0, SROCD1, SROCD2, SROCD3, SROCD4, SROCDX, SROCDX1, SROCDX2, SROCPT0, SROMOD0, SROPCEP, and</p>
<p>SROUTLN. Updated option description section for the <em>List Completed Cases Missing CPT Codes</em> [SRSCPT] and the <em>PCE Filing Status Report</em> [SRO PCE STATUS] options.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>01/06</td>
<td>53-55</td>
<td>SR*3*151</td>
<td><blockquote>
<p>Updated the Calls Made by Surgery section to reflect current external calls.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/05</td>
<td>21-22</td>
<td>SR*3*148</td>
<td><blockquote>
<p>Added the routine SRBL to the routine listing.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>
June 2007 Surgery V. 3.0 Technical Manual/Security Guide i
> SR\*3\*160
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/05</td>
<td>12, 21-22, 51, 52</td>
<td>SR*3*119</td>
<td><blockquote>
<p>These fields in the SURGERY SITE PARAMETERS file (#133) are no longer editable: UPDATES TO PCE field (#18), PCE UPDATE ACTIVATION DATE field (#18.5), and ASK CLASSIFICATION QUESTIONS</p>
<p>field (#19). Added new routines SR119PI, SROADX, SROADX1, SROADX2, and SROANEST to the</p>
<p>routines listing. Added SROANEST to the Callable Routines section.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/04</td>
<td><p>21-24, 32-34, 73,</p>
<p>76</p></td>
<td>SR*3*132</td>
<td><p>Added these new routines to the routine listing: SRONPEN, SRONP0, SRONP1, and SRONP2. Add the</p>
<p>new <em>Non-OR Procedure Information</em> [SR NON-OR INFO] option to the Exported Options section. Updated the menu list with the new option.</p></td>
</tr>
<tr class="odd">
<td>08/04</td>
<td><p>i, 21-24, 26, 29-30,</p>
<p>34, 75</p></td>
<td>SR*3*125</td>
<td><p>Added these new routines to the routine listing: SR125UTL, SROACAR1, SROACL2, SROACPM1, SROACPM2, SROACR2, SROACTH1, SROAOUT, SROATCM3, SROCLAB, SRORACE, and SROUTC.</p>
<p>Added the new <em>Laboratory Test Results (Enter/Edit)</em> [SROA LAB-CARDIAC] option and the <em>Outcome Information (Enter/Edit)</em> [SROA CARDIAC- OUTCOMES] option to the Exported Options section.</p>
<p>Updated the menu list with changes.</p></td>
</tr>
<tr class="even">
<td>08/04</td>
<td>17, 21-22</td>
<td>SR*3*129</td>
<td>Updated the Files section to include the new ATTENDING CODES file (#132.9), and updated the Routines section to include the new SRENSCS routine.</td>
</tr>
<tr class="odd">
<td>04/04</td>
<td>All Pages</td>
<td><blockquote>
<p>SR*3*100</p>
</blockquote></td>
<td>This manual was updated to reflect new local documentation standards, and includes changes resulting from the Surgery Electronic Signature for Operative Reports patch SR*3*100. See the patch description for details of all changes related to this patch.</td>
</tr>
</tbody>
</table>
> ii Surgery V. 3.0 Technical Manual/Security Guide April 2004

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is the list of routines used in the Surgery package. This list excludes all initialization routines, protocol installation routines, and routines exported with patches that performed a one-time function. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine in the SR- namespace.

| SR160UT0 | SR160UTL | SRBL     | SRBLOOD  | SRCHL7A  | SRCHL7U  | SRCUSS   | SRCUSS0  |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SRCUSS1  | SRCUSS   | SRCUSS3  | SRCUSS4  | SRCUSS5  | SRENSCS  | SRHLDW   | SRHLDW1  |
| SRHLENV  | SRHLMFN  | SRHLOORU | SRHLORU  | SRHLPOST | SRHLPRE  | SRHLQRY  | SRHLSCRN |
| SRHLU    | SRHLUI   | SRHLUO   | SRHLUO1  | SRHLUO2  | SRHLUO3  | SRHLUO4  | SRHLUO4C |
| SRHLVOOR | SRHLVORU | SRHLVQRY | SRHLVU   | SRHLVUI  | SRHLVUI2 | SRHLVUO  | SRHLVUO1 |
| SRHLVUO2 | SRHLVUO4 | SRHLVZIU | SRHLVZQR | SRHLVZSQ | SRHLXTMP | SRHLZIU  | SRHLZQR  |
| SRO1L    | SRO1L1   | SRO3P90  | SROA30   | SROA38   | SROA38A  | SROABCH  | SROAC    |
| SROAC1   | SROAC2   | SROACAR  | SROACAR1 | SROACAT  | SROACC   | SROACC0  | SROACC1  |
| SROACC2  | SROACC3  | SROACC4  | SROACC5  | SROACC6  | SROACCM  | SROACCR  | SROACCT  |
| SROACL1  | SROACL2  | SROACLN  | SROACMP  | SROACMP1 | SROACOD  | SROACOM  | SROACOP  |
| SROACPM  | SROACPM1 | SROACPM2 | SROACR1  | SROACR2  | SROACRC  | SROACS   | SROACTH  |
| SROACTH1 | SROADEL  | SROADOC  | SROADOC1 | SROADX   | SROADX1  | SROADX2  | SROAERR  |
| SROAEX   | SROAL1   | SROAL11  | SROAL2   | SROAL21  | SROALAB  | SROALC   | SROALCP  |
| SROALCS  | SROALCSP | SROALDP  | SROALEN  | SROALESS | SROALEC  | SROALET  | SROALL   |
| SROALLP  | SROALLS  | SROALLSP | SROALM   | SROALMN  | SROALN1  | SROALN2  | SROALN3  |
| SROALNO  | SROALOG  | SROALSS  | SROALSSP | SROALST  | SROALSTP | SROALT   | SROALTP  |
| SROALTS  | SROALTSP | SROAMAN  | SROAMEAS | SROAMIS  | SROAMIS1 | SROANEST | SROANEW  |
| SROANIN  | SROANP   | SROANP1  | SROANR   | SROANR0  | SROANR1  | SROANT   | SROANTP  |
| SROANTS  | SROANTSP | SROAO    | SROAOP   | SROAOP1  | SROAOP2  | SROAOPS  | SROAOSET |
| SROAOTH  | SROAOUT  | SROAPAS  | SROAPC   | SROAPCA  | SROAPCA0 | SROAPCA1 | SROAPCA2 |
| SROAPCA3 | SROAPCA4 | SROAPIMS | SROAPM   | SROAPR1A | SROAPR2  | SROAPRE  | SROAPRE1 |
| SROAPRE2 | SROAPRT1 | SROAPRT2 | SROAPRT3 | SROAPRT4 | SROAPRT5 | SROAPRT6 | SROAPRT7 |
| SROAPS1  | SROAPS2  | SROAR    | SROAR1   | SROAR2   | SROARET  | SROARPT  | SROASITE |
| SROASS   | SROASS1  | SROASSE  | SROASSN  | SROASSP  | SROASWAP | SROASWP  | SROASWP0 |
| SROASWP1 | SROASWP2 | SROASWP3 | SROASWPD | SROAT0P  | SROAT0T  | SROAT1P  | SROAT1T  |
| SROAT2P  | SROAT2T  | SROATCM  | SROATCM1 | SROATCM2 | SROATCM3 | SROATM1  | SROATM2  |
| SROATM3  | SROATM4  | SROATMIT | SROATMNO | SROATT   | SROATT0  | SROATT1  | SROATT2  |
| SROAUTL  | SROAUTL0 | SROAUTL1 | SROAUTL2 | SROAUTL3 | SROAUTL4 | SROAUTLC | SROAWL   |
| SROAWL1  | SROAX    | SROBLOD  | SROCAN   | SROCAN0  | SROCANUP | SROCASE  | SROCCAT  |
| SROCD    | SROCD0   | SROCD1   | SROCD2   | SROCD3   | SROCD4   | SROCDX   | SROCDX1  |
| SROCDX2  | SROCL1   | SROCLAB  | SROCMP   | SROCMP1  | SROCMP2  | SROCMPD  | SROCMPED |
| SROCMPL  | SROCMPS  | SROCNR   | SROCNR1  | SROCNR2  | SROCODE  | SROCOM   | SROCOMP  |
| SROCON   | SROCON1  | SROCOND  | SROCPT   | SROCPT0  | SROCRAT  | SROCVER  | SRODATE  |
| SRODEL76 | SRODELA  | SRODEV   | SRODIS   | SRODIS0  | SRODLA1  | SRODLA2  | SRODLAY  |
| SRODLT   | SRODLT0  | SRODLT1  | SRODLT2  | SRODPT   | SRODTH   | SROERR   | SROERR0  |
| SROERR1  | SROERR2  | SROERRPO | SROES    | SROESAD  | SROESAD1 | SROESAR  | SROESAR0 |
| SROESAR1 | SROESAR2 | SROESARA | SROESHL  | SROESL   | SROESNR  | SROESNR0 | SROESNR1 |
| SROESNR2 | SROESNR3 | SROESNRA | SROESPR  | SROESPR1 | SROESPR2 | SROESTV  | SROESUTL |
| SROESX   | SROESX0  | SROESXA  | SROESXP  | SROFILE  | SROFLD   | SROGMTS  | SROGMTS0 |
| SROGMTS1 | SROGMTS2 | SROGTSR  | SROHIS   | SROICD   | SROICU   | SROICU1  | SROICU2  |
| SROINQ   | SROIRR   | SROKEY   | SROKEY1  | SROKRET  | SROLOCK  | SROMED   | SROMENU  |
| SROMOD   | SROMOD0  | SROMOR   | SROMORT  | SRONAN   | SRONAN1  | SRONASS  | SRONBCH  |
| SRONEW   | SRONI001 | SRONIN   | SRONIT   | SRONIT1  | SRONIT2  | SRONIT3  | SRONITE  |
| SRONON   | SRONOP   | SRONOP1  | SRONOR   | SRONOR1  | SRONOR2  | SRONOR3  | SRONOR4  |
| SRONOR5  | SRONOR6  | SRONOR7  | SRONOR8  | SRONP    | SRONP0   | SRONP1   | SRONP2   |
| SRONPEN  | SRONRPT  | SRONRPT0 | SRONRPT1 | SRONRPT2 | SRONRPT3 | SRONUR   | SRONUR1  |
| SRONUR2  | SRONXR   | SROOPRM  | SROOPRM1 | SROP     | SROP1    | SROPAC0  | SROPAC1  |
| SROPACT  | SROPAT   | SROPCE   | SROPCE0  | SROPCE0A | SROPCE0B | SROPCE1  | SROPCEP  |
| SROPCEU  | SROPCEU0 | SROPCEX  | SROPDEL  | SROPECS  | SROPECS1 | SROPER   | SROPFSS  |
| SROPLIS  | SROPLIST | SROPLST1 | SROPLSTS | SROPOST  | SROPOST0 | SROPOST1 | SROPOST2 |

June 2007 Surgery V. 3.0 Technical Manual/Security Guide 21

> SR\*3\*160

| SROPPC   | SROPRE   | SROPRE0  | SROPREQ  | SROPRI   | SROPRI1  | SROPRI2  | SROPRIN  |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SROPRIO  | SROPRIT  | SROPROC  | SROPRPT  | SROPS    | SROPS1   | SROPSEL  | SROPSN   |
| SROQ     | SROQ0    | SROQ0A   | SROQ1    | SROQ1A   | SROQ2    | SROQADM  | SROQD    |
| SROQD0   | SROQD1   | SROQIDP  | SROQIDP0 | SROQL    | SROQM    | SROQM0   | SROQM1   |
| SROQN    | SROQT    | SROR     | SRORACE  | SRORAT1  | SRORAT2  | SRORATA  | SRORATP  |
| SRORATS  | SROREA   | SROREA1  | SROREA2  | SROREAS  | SROREQ   | SROREQ1  | SROREQ2  |
| SROREQ3  | SROREQ4  | SROREST  | SRORESV  | SRORET   | SRORHRS  | SRORHRS0 | SRORIN   |
| SRORTRN  | SRORUT   | SRORUT0  | SRORUT1  | SRORUT2  | SROSCH   | SROSCH1  | SROSCH2  |
| SROSNR   | SROSNR1  | SROSNR2  | SROSPC1  | SROSPEC  | SROSPLG  | SROSPLG1 | SROSPLG2 |
| SROSPSS  | SROSRPT  | SROSRRT  | SROSTAFF | SROSTOP  | SROSUR   | SROSUR1  | SROSUR2  |
| SROTHER  | SROTIUD  | SROTRIG  | SROTRPT  | SROTRPT0 | SROUNV   | SROUNV1  | SROUNV2  |
| SROUTC   | SROUTED  | SROUTIN  | SROUTL   | SROUTL0  | SROUTL1  | SROUTLN  | SROUTUP  |
| SROVAR   | SROVER   | SROVER1  | SROVER2  | SROVER3  | SROWC    | SROWC1   | SROWC2   |
| SROWC3   | SROWL    | SROWL0   | SROWRQ   | SROWRQ1  | SROXPR   | SROXR1   | SROXR2   |
| SROXR4   | SROXREF  | SROXRET  | SRSAVG   | SRSAVL   | SRSAVL1  | SRSBD1   | SRSBDEL  |
| SRSBLOK  | SRSBOUT  | SRSCAN   | SRSCAN0  | SRSCAN1  | SRSCAN2  | SRSCD    | SRSCDS   |
| SRSCDS1  | SRSCDW   | SRSCDW1  | SRSCG    | SRSCHAP  | SRSCHC   | SRSCHC1  | SRSCHC2  |
| SRSCHCA  | SRSCHCC  | SRSCHD   | SRSCHD1  | SRSCHD2  | SRSCHDA  | SRSCHDC  | SRSCHK   |
| SRSCHOR  | SRSCHUN  | SRSCHUN1 | SRSCHUP  | SRSCONR  | SRSCOR   | SRSCPT   | SRSCPT1  |
| SRSCPT2  | SRSCRAP  | SRSDIS1  | SRSDISP  | SRSDT    | SRSGRPH  | SRSIND   | SRSKILL  |
| SRSKILL1 | SRSKILL2 | SRSLOOK  | SRSLOOK1 | SRSMREQ  | SRSPUT0  | SRSPUT1  | SRSPUT2  |
| SRSRBS   | SRSRBS1  | SRSRBW   | SRSRBW1  | SRSREQ   | SRSREQUT | SRSRQST  | SRSRQST1 |
| SRSTCH   | SRSTIME  | SRSUP1   | SRSUPC   | SRSUPRG  | SRSUPRQ  | SRSUTIN  | SRSUTL   |
| SRSUTL2  | SRSWL    | SRSWL1   | SRSWL10  | SRSWL11  | SRSWL12  | SRSWL13  | SRSWL14  |
| SRSWL15  | SRSWL2   | SRSWL3   | SRSWL4   | SRSWL5   | SRSWL6   | SRSWL7   | SRSWL8   |
| SRSWL9   | SRSWLST  | SRSWREQ  |          |          |          |          |          |

> 603 routines

> 22 Surgery V. 3.0 Technical Manual/Security Guide June 2007 SR\*3\*160

# File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following files were distributed with limited access for first time installations of the VistA Surgery software. Files not listed below were sent without restrictions on VA FileMan access. Sites can add their own file access codes as needed, but it is highly recommended that they do not change the codes that are sent with this software package.

| File Number | File Name               | Read | Write | Delete | LAYGO |
|-----------------|-----------------------------|----------|-----------|------------|-----------|
| 131             | PERSON FIELD RESTRICTION    | @        | ^         | ^          | @         |
| 132.9           | ATTENDING CODES\*           | @        | @         | @          | @         |
| 132.95          | ANESTHESIA SUPERVISOR CODES |          | ^         | ^          | ^         |
| 134             | OPERATING ROOM TYPE         |          | ^         | ^          | ^         |
| 136.5           | OCCURRENCE CATEGORY         | ^        | ^         | ^          | ^         |

> \* This file was not included in the original release of Surgery V. 3.0, but was added by patch SR\*3\*129.

June 2007 Surgery V. 3.0 Technical Manual/Security Guide 81

> SR\*3\*160

> *(This page included for two-sided copying.)*

> 82 Surgery V. 3.0 Technical Manual/Security Guide April 2004