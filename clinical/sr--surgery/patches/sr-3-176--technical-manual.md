---
title: SR*3*176 Surgery VASQIP 2012 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Surgery VASQIP 2012 /Security Guide Change Pages
app_code: SR
app_name: Surgery
section: CLI
app_status: active
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*176
group_key: "SR:SR:3"
file_numbers: []
security_keys: 
  - SR CODER
  - SR MED STUDENT
  - SR NURSE
  - SR PHYSICIAN ASSISTANT
  - SR REQ OVERRIDE
  - SR RISK ASSESSMENT
  - SR STAFF SURGEON
  - SR SURGEON
  - SR TRANSPLANT
  - SROPER
  - SROREP
  - SROREQ
  - SROSCH
menu_options: 0
description: > ![](sr-3-176-surgery-vasqip-2012-technical-manual-security-guide-change-pages/001.png)
audience: 
keywords: 
  - table
  - contents
  - class
  - report
  - strong
  - blockquote
  - surgery
  - surgical
  - deaths
  - even
page_count: 0
word_count: 1142
section_count: 7
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p176_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p176_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=103"
---

> ![](sr-3-176-surgery-vasqip-2012-technical-manual-security-guide-change-pages/001.png)

SURGERY

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 3.0

> July 1993

### (Revised March 2012)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Product Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [(Revised March 2012)](#revised-march-2012)
- [Revision History](#revision-history)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Options Listed by Name](#options-listed-by-name)
  - [Annual Report of Surgical Procedures \[SROARSP\]](#annual-report-of-surgical-procedures-sroarsp)
  - [Circulating Nurse Staffing Report \[SROCNR\]](#circulating-nurse-staffing-report-srocnr)
  - [Comparison of Preop and Postop Diagnosis \[SROPPC\]](#comparison-of-preop-and-postop-diagnosis-sroppc)
    - [This option is used to block out times on the Operating Room Schedule by surgical specialty.](#this-option-is-used-to-block-out-times-on-the-operating-room-schedule-by-surgical-specialty)
  - [Deaths Within 30 Days of Surgery \[SROQD\]](#deaths-within-30-days-of-surgery-sroqd)
  - [Delete or Update Operation Requests \[SRSUPRQ\]](#delete-or-update-operation-requests-srsuprq)
  - [Flag Drugs for Use as Anesthesia Agents \[SROCODE\]](#flag-drugs-for-use-as-anesthesia-agents-srocode)
- [Security Keys](#security-keys)
- [Index](#index)
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
<td>03/12</td>
<td><blockquote>
<p>i, iii, 10, 18-19, 23-</p>
<p>25, 71, 73, 80-82</p>
</blockquote></td>
<td>SR*3*176</td>
<td><p>References to “Quarterly Report” removed. Routine “SROQ30D” added to the list of routines. Removal of “9” from references to ICD. Appendix A removed.</p>
<p>Index renumbered.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/11</td>
<td><blockquote>
<p>i, 13, 18-19, 20-22,</p>
<p>24-29, 34-36, 38,</p>
<p>40, 67, 69, 78-79</p>
</blockquote></td>
<td>SR*3*175</td>
<td><p>Change in definitions. Routine SRTOVRF added to the list of routines. Options description list updated.</p>
<p>Quarterly Report Menu removed. References to CICSP and NSQIP removed from the Glossary.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/10</td>
<td>i, 27</td>
<td><blockquote>
<p>SR*3*174</p>
</blockquote></td>
<td><p>Change in definition of List of Surgery Risk Assessments report.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/08</td>
<td>All</td>
<td><blockquote>
<p>SR*3*167</p>
</blockquote></td>
<td><p>Updated to provide the Surgery Transplant Assessment module information. Additions necessitated a document reissue.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is the list of routines used in the Surgery package. This list excludes all initialization routines, protocol installation routines, and routines exported with patches that performed a one-time function. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine in the SR- namespace.

| SRBL     | SRBLOOD  | SRCHL7A  | SRCHL7U  | SRCUSS   | SRCUSS0  | SRCUSS1  | SRCUSS2  |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SRCUSS3  | SRCUSS4  | SRCUSS5  | SRENSCS  | SRHLDW   | SRHLDW1  | SRHLENV  | SRHLMFN  |
| SRHLOORU | SRHLORU  | SRHLQRY  | SRHLSCRN | SRHLU    | SRHLUI   | SRHLUO   | SRHLUO1  |
| SRHLUO2  | SRHLUO3  | SRHLUO4  | SRHLUO4C | SRHLVOOR | SRHLVORU | SRHLVQRY | SRHLVU   |
| SRHLVUI  | SRHLVUI2 | SRHLVUO  | SRHLVUO1 | SRHLVUO2 | SRHLVUO4 | SRHLVZIU | SRHLVZQR |
| SRHLVZSQ | SRHLXTMP | SRHLZIU  | SRHLZQR  | SRO1L    | SRO1L1   | SROA30   | SROABCH  |
| SROACAR  | SROACAR1 | SROACAT  | SROACC   | SROACC0  | SROACC1  | SROACC2  | SROACC3  |
| SROACC4  | SROACC5  | SROACC6  | SROACCM  | SROACCT  | SROACL1  | SROACL2  | SROACLN  |
| SROACMP  | SROACMP1 | SROACOD  | SROACOM  | SROACOM1 | SROACOP  | SROACPM  | SROACPM1 |
| SROACPM2 | SROACR1  | SROACR2  | SROACS   | SROACTH  | SROACTH1 | SROADEL  | SROADOC  |
| SROADOC1 | SROADX   | SROADX1  | SROADX2  | SROAERR  | SROAEX   | SROAL1   | SROAL11  |
| SROAL2   | SROAL21  | SROALAB  | SROALC   | SROALCP  | SROALCS  | SROALCSP | SROALDP  |
| SROALEC  | SROALEN  | SROALESS | SROALET  | SROALL   | SROALLP  | SROALLS  | SROALLSP |
| SROALM   | SROALMN  | SROALN1  | SROALN2  | SROALN3  | SROALNC  | SROALNO  | SROALOG  |
| SROALSL  | SROALSS  | SROALSSP | SROALST  | SROALSTP | SROALT   | SROALTP  | SROALTS  |
| SROALTSP | SROAMAN  | SROAMEAS | SROAMIS  | SROAMIS1 | SROANEST | SROANEW  | SROANIN  |
| SROANP   | SROANP1  | SROANR   | SROANR0  | SROANR1  | SROANT   | SROANTP  | SROANTS  |
| SROANTSP | SROAO    | SROAOP   | SROAOP1  | SROAOP2  | SROAOPS  | SROAOSET | SROAOTH  |
| SROAOUT  | SROAPAS  | SROAPC   | SROAPCA  | SROAPCA0 | SROAPCA1 | SROAPCA2 | SROAPCA3 |
| SROAPCA4 | SROAPIMS | SROAPM   | SROAPR1A | SROAPR2  | SROAPRE  | SROAPRE1 | SROAPRE2 |
| SROAPRT1 | SROAPRT2 | SROAPRT3 | SROAPRT4 | SROAPRT5 | SROAPRT6 | SROAPRT7 | SROAPS1  |
| SROAPS2  | SROAR    | SROAR1   | SROAR2   | SROARET  | SROARPT  | SROASITE | SROASS   |
| SROASS1  | SROASSE  | SROASSN  | SROASSP  | SROAT0P  | SROAT0T  | SROAT1P  | SROAT1T  |
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
| SROINQ   | SROIRR   | SROKEY   | SROKEY1  | SROKRET  | SROLABS  | SROLOCK  | SROMED   |
| SROMENU  | SROMOD   | SROMOD0  | SROMOR   | SROMORT  | SRONAN   | SRONAN1  | SRONASS  |
| SRONBCH  | SRONEW   | SRONIN   | SRONITE  | SRONON   | SRONOP   | SRONOP1  | SRONOR   |
| SRONOR1  | SRONOR2  | SRONOR3  | SRONOR4  | SRONOR5  | SRONOR6  | SRONOR7  | SRONOR8  |
| SRONP    | SRONP0   | SRONP1   | SRONP2   | SRONPEN  | SRONRPT  | SRONRPT0 | SRONRPT1 |
| SRONRPT2 | SRONRPT3 | SRONUR   | SRONUR1  | SRONUR2  | SRONXR   | SROOPRM  | SROOPRM1 |
| SROP     | SROP1    | SROPAC0  | SROPAC1  | SROPACT  | SROPAT   | SROPCE   | SROPCE0  |
| SROPCE0A | SROPCE0B | SROPCE1  | SROPCEP  | SROPCEU  | SROPCEU0 | SROPCEX  | SROPDEL  |
| SROPECS  | SROPECS1 | SROPER   | SROPFSS  | SROPLIS  | SROPLIST | SROPLST1 | SROPLSTS |
| SROPPC   | SROPREQ  | SROPRI   | SROPRI1  | SROPRI2  | SROPRIN  | SROPRIO  | SROPRIT  |
| SROPROC  | SROPRPT  | SROPS    | SROPS1   | SROPSEL  | SROPSN   | SROQ     | SROQ0    |
| SROQ0A   | SROQ30D  | SROQADM  | SROQD    | SROQD0   | SROQD1   | SROQIDP  | SROQIDP0 |

| SROQL    | SROQN    | SROR     | SRORACE  | SRORAT1  | SRORAT2  | SRORATA  | SRORATP  |
|----------|----------|----------|----------|----------|----------|----------|----------|
| SRORATS  | SROREA   | SROREA1  | SROREA2  | SROREAS  | SROREQ   | SROREQ1  | SROREQ2  |
| SROREQ3  | SROREQ4  | SROREST  | SRORESV  | SRORET   | SRORHRS  | SRORHRS0 | SRORIN   |
| SRORTRN  | SRORUT   | SRORUT0  | SRORUT1  | SRORUT2  | SROSCH   | SROSCH1  | SROSCH2  |
| SROSNR   | SROSNR1  | SROSNR2  | SROSPC1  | SROSPEC  | SROSPLG  | SROSPLG1 | SROSPLG2 |
| SROSPSS  | SROSRPT  | SROSTAFF | SROSTOP  | SROSUR   | SROSUR1  | SROSUR2  | SROTHER  |
| SROTIUD  | SROTRIG  | SROTRPT  | SROTRPT0 | SROUNV   | SROUNV1  | SROUNV2  | SROUTC   |
| SROUTED  | SROUTIN  | SROUTL   | SROUTL0  | SROUTL1  | SROUTLN  | SROUTUP  | SROVAR   |
| SROVER   | SROVER1  | SROVER2  | SROVER3  | SROWC    | SROWC1   | SROWC2   | SROWC3   |
| SROWL    | SROWL0   | SROWRQ   | SROWRQ1  | SROXPR   | SROXR1   | SROXR2   | SROXR4   |
| SROXREF  | SROXRET  | SRSAVG   | SRSAVL   | SRSAVL1  | SRSBD1   | SRSBDEL  | SRSBLOK  |
| SRSBOUT  | SRSBUTL  | SRSCAN   | SRSCAN0  | SRSCAN1  | SRSCAN2  | SRSCD    | SRSCDS   |
| SRSCDS1  | SRSCDW   | SRSCDW1  | SRSCG    | SRSCHAP  | SRSCHC   | SRSCHC1  | SRSCHC2  |
| SRSCHCA  | SRSCHCC  | SRSCHD   | SRSCHD1  | SRSCHD2  | SRSCHDA  | SRSCHDC  | SRSCHK   |
| SRSCHOR  | SRSCHUN  | SRSCHUN1 | SRSCHUP  | SRSCONR  | SRSCOR   | SRSCPT   | SRSCPT1  |
| SRSCPT2  | SRSCRAP  | SRSDIS1  | SRSDISP  | SRSDT    | SRSGRPH  | SRSIND   | SRSKILL  |
| SRSKILL1 | SRSKILL2 | SRSMREQ  | SRSPUT0  | SRSPUT1  | SRSPUT2  | SRSRBS   | SRSRBS1  |
| SRSRBW   | SRSRBW1  | SRSREQ   | SRSREQUT | SRSRQST  | SRSRQST1 | SRSTCH   | SRSTIME  |
| SRSUP1   | SRSUPC   | SRSUPRG  | SRSUPRQ  | SRSUTIN  | SRSUTL   | SRSUTL2  | SRSWL    |
| SRSWL1   | SRSWL10  | SRSWL11  | SRSWL12  | SRSWL13  | SRSWL14  | SRSWL15  | SRSWL2   |
| SRSWL3   | SRSWL4   | SRSWL5   | SRSWL6   | SRSWL7   | SRSWL8   | SRSWL9   | SRSWLST  |
| SRSWREQ  | SRTOVRF  | SRTPASS  | SRTPCOM  | SRTPDONR | SRTPHRT1 | SRTPHRT2 | SRTPHRT3 |
| SRTPHRT4 | SRTPHRT5 | SRTPHRT6 | SRTPKID1 | SRTPKID2 | SRTPKID3 | SRTPKID4 | SRTPKID6 |
| SRTPLIV1 | SRTPLIV2 | SRTPLIV3 | SRTPLIV4 | SRTPLIV5 | SRTPLIV6 | SRTPLIV7 | SRTPLS   |
| SRTPLST  | SRTPLSTP | SRTPLUN1 | SRTPLUN2 | SRTPLUN3 | SRTPLUN5 | SRTPNEW  | SRTPPAS  |
| SRTPRACE | SRTPRH   | SRTPRH1  | SRTPRH2  | SRTPRK   | SRTPRK1  | SRTPRK2  | SRTPRK3  |
| SRTPRLI  | SRTPRLI1 | SRTPRLI2 | SRTPRLU  | SRTPRLU1 | SRTPRLU2 | SRTPSITE | SRTPSS   |
| SRTPTM1  | SRTPTM2  | SRTPTMIT | SRTPTRAN | SRTPUTL  | SRTPUTL4 | SRTPUTLC | SRTPVAN  |

> 624 routines

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains information about the Surgery package options; first, the exported options are listed by name, and then they are provided alphabetically, with a description of the option.

# Options Listed by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table contains a list of all of the options in the Surgery package, listed alphabetically by name.

| SR ANESTH REPORTS           | SR BLOOD PRODUCT VERIFICATION | SR BLOOD PRODUCT VERIFY AUDIT |
|-----------------------------|-------------------------------|-------------------------------|
| SR CPT ACCURACY             | SR CPT REPORTS                | SR MANAGE REPORTS             |
| SR NO ASSESSMENT REASON     | SR NON-OR INFO                | SR NON-OR REPORT              |
| SR NORMAL HOURS             | SR OR HOURS                   | SR OR UTIL                    |
| SR OR UTL1                  | SR PURGE UTILIZATION          | SR STAFFING REPORTS           |
| SR SURGERY REQUEST          | SR TRANSPLANT ASSESSMENT      | SR TRANSPLANT ENTER/EDIT      |
| SR TRANSPLANT PARAMETERS    | SR UPDATE FILES               | SR UPDATE SCHEDULE DEVIC      |
| SR UTIL EDIT ROOM           | SR VIEW HISTORICAL REPORTS    | SRCODING EDIT                 |
| SRCODING MENU               | SRCODING NURSE REPORT         | SRCODING OP REPORT            |
| SRCODING UPDATE/VERIFY MENU | SRHL DOWNLOAD INTERFACE FILES | SRHL DOWNLOAD SET OF CODES    |
| SRHL INTERFACE              | SRHL INTERFACE FLDS           | SRHL PARAMETER                |
| SRO CASES BY DISPOSITION    | SRO CASES BY PRIORITY         | SRO COMPLICATIONS MENU        |
| SRO DEATH RELATED           | SRO DEL MENU                  | SRO DELAY TIME                |
| SRO ECS COMPLIANCE          | SRO INTRAOP COMP              | SRO M&M VERIFICATION REPORT   |
| SRO PACKAGE MANAGEMENT      | SRO PCE NOTRANS               | SRO PCE STATUS                |
| SRO POSTOP COMP             | SRO QUARTERLY REPORT          | SRO SURGICAL PRIORITY         |
| SRO UPDATE CANCELLED CASE   | SRO UPDATE RETURNS            |                               |
| SRO-CHIEF REPORTS           | SRO-LRRP                      | SRO-ROOM                      |
| SRO-UNLOCK                  | SROA ASSESSMENT LIST          | SROA CARDIAC COMPLICATIONS    |
| SROA CARDIAC ENTER/EDIT     | SROA CARDIAC OPERATIVE RISK   | SROA CARDIAC PROCEDURES       |
| SROA CARDIAC RESOURCE       | SROA CARDIAC-OUTCOMES         | SROA CATHETERIZATION          |
| SROA CLINICAL INFORMATION   | SROA CODE ISSUE               | SROA COMPLETE ASSESSMENT      |
| SROA DEMOGRAPHICS           | SROA ENTER/EDIT               | SROA LAB                      |
| SROA LAB TEST EDIT          | SROA LAB-CARDIAC              | SROA MONTHLY WORKLOAD REPORT  |

> *Anesthesia for an Operation Menu* \[SROANES\]

> This menu contains the various Anesthesia related options used to input and display anesthesia staff and technique information.

> *Annual Report of Non-O.R. Procedures* \[SRONOP-ANNUAL\]

> This option is used to generate the Annual Report of Non-OR Procedures. It will display the total number of procedures based on CPT code.

## Annual Report of Surgical Procedures \[SROARSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to generate the Annual Report of Surgical Procedures. It will count procedures within Surgical Specialties.

> *Attending Surgeon Reports* \[SROATT\]

> This option generates the Attending Surgeon Reports that displays staffing information for completed cases along with cumulative totals for each attending code. It can be sorted by surgical specialty and can be generated for an individual surgeon.

> *Blood Product Verification* \[SR BLOOD PRODUCT VERIFICATION\]

> The user can access this option through the *Operation Menu* \[SROPER\] option. After scanning the blood unit ID, the software will check for an association with the patient identified. If there are multiple entries with the Unit ID scanned, these entries will be listed along with the Blood Component, Patient Associated, and Expiration Date. The user will then be prompted to select the one that matches the blood product about to be administered. If the selected product is not associated with the patient identified, the warning message will be displayed.

> *CPT Code Reports* \[SR CPT REPORTS\]

> This menu contains reports based on CPT Codes. It includes the Cumulative Report of CPT Codes, Report of CPT Coding Accuracy, and the Report of Cases Missing CPT Codes.

> *CPT/ICD Coding Menu* \[SRCODING MENU\]

> This menu provides functionality for reviewing operations and non-OR procedures and for editing operation and non-OR procedure CPT and ICD codes.

> *CPT/ICD Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] This menu contains options to be used by those responsible for entering CPT and ICD codes for operations and non-OR procedures.

> *Cancel Scheduled Operation* \[SRSCAN\]

> This option is used to cancel a scheduled operation on a given date. When a scheduled case is cancelled, a new request is automatically generated for that case on the same date.

> *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] This option is used to enter or edit information related to cardiac procedures requiring cardiopulmonary bypass for the cardiac surgery risk assessments.

> *Cardiac Risk Assessment Information (Enter/Edit)* \[SROA CARDIAC ENTER/EDIT\]

> This menu contains options to enter or edit assessment information for the cardiac risk assessments.

> *Chief of Surgery Menu* \[SROCHIEF\]

> This menu contains the various options designed for use by the Chief of Surgery and his package coordinator.

## Circulating Nurse Staffing Report \[SROCNR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides nurse-staffing information, sorted by the circulating nurses’ name.

> *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]

> This option is used to enter the clinical information required for the cardiac surgery risk assessments.

> *Comments* \[SROMEN-COM\]

> This option is used to enter general comments about a case.

## Comparison of Preop and Postop Diagnosis \[SROPPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report contains completed cases in which the principal preoperative and principal postoperative diagnoses are different.

> *Create Service Blockout* \[SRSBOUT\]

### This option is used to block out times on the Operating Room Schedule by surgical specialty.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Cumulative Report of CPT Codes* \[SROACCT\]

> This report displays the total number of each CPT code entered for the date range selected. It also breaks down the totals into two categories, principal procedures and other operative procedures.

## Deaths Within 30 Days of Surgery \[SROQD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lists patients who had surgery within the selected date range and who died within 30 days of surgery. Two separate reports are available through this option.

#### Total Cases Summary

> This report can be printed in one of three ways.

- All Cases: The report lists all patients who had surgery within the selected date range and who died within 30 days of surgery, along with all of the patients’ operations that were performed during the selected date range. These patients are included in the postoperative deaths totals on the Quarterly Report.
- Outpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as outpatient (ambulatory) deaths on the Quarterly Report.
- Inpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as inpatient deaths. Although the count of deaths associated with inpatient cases is not a part of the Quarterly Report, this report is provided to help with data validation.

#### Specialty Procedures

> This report will list the surgical cases that are associated with deaths that are counted for the national surgical specialty linked to the local surgical specialty. Cases are listed by national surgical specialty.

> *Delay and Cancellation Reports* \[SRO DEL MENU\]

> This menu contains various reports used to track delays and cancellations.

> *Delete Service Blockout* \[SRSBDEL\]

> 24 Surgery V. 3.0 Technical Manual/Security Guide March 2012

> This option is used to delete service blockouts already existing on a schedule.

> *Delete a Patient from the Waiting List* \[SROW-DELETE\]

> This option is used to delete a patient currently on the surgery waiting list for a selected service.

## Delete or Update Operation Requests \[SRSUPRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to delete, change the date, or update the information entered on a requested operation.

> *Display Availability* \[SRODISP\]

> This option provides a graph of the availability of operating rooms. Times that are unavailable will be marked by “X”s.

> *Edit Non-O.R. Procedure* \[SRONOP-EDIT\]

> This option allows the editing of information on the pre-selected non-OR procedure.

> *Edit a Patient on the Waiting List* \[SROW-EDIT\]

> This option is used to edit a patient already on the waiting list for a selected surgical specialty.

> *Enter/Edit Transplant Assessments* \[SR TRANSPLANT ENTER/EDIT\]

> This option is used to enter the information required for the transplant assessments.

> *Enter Cardiac Catheterization & Angiographic Data* \[SROA CATHETERIZATION\] This option is used to enter or edit cardiac catheterization and angiographic information for cardiac surgery risk assessments.

> *Enter Irrigations and Restraints* \[SROMEN-REST\]

> This option is used to stuff in multiple restraints and positioning aids.

> *Enter PAC(U) Information* \[SROMEN-PACU\]

> This option is used to enter or edit recovery room scores and times.

> *Enter Referring Physician Information* \[SROMEN-REFER\]

> This option is used to enter the name, phone number, and address of the referring physician or institution.

> *Enter Restrictions for 'Person' Fields* \[SROKEY ENTER\]

> This option is used to enter restrictions on person fields. It will allow the user to add keys to existing entries in the PERSON FIELD RESTRICTION file (#131). If the field to be restricted has not already been entered in the PERSON FIELD RESTRICTION file (#131), the user may enter it along with the restricting keys through this option.

> *Enter a Patient on the Waiting List* \[SROW-ENTER\]

> This option is used to enter a patient on the waiting list for a selected surgical specialty.

> *Ensuring Correct Surgery Compliance Report* \[SRO ECS COMPLIANCE\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option produces the Ensuring Correct Surgery Compliance Report. This report is a two-part report:

> \(1\) the compliance summary and (2) the list of non-compliant cases. The report is printed for a selected date range and may be sorted by surgical specialty. This report is a tool for reviewing compliance with the documentation process for ensuring correct surgery.

> *Exclusion Criteria (Enter/Edit)* \[SR NO ASSESSMENT REASON\] This option is used to flag major cases that will not have a surgery risk assessment due to certain exclusion criteria.

> *File Download* \[SRHL DOWNLOAD INTERFACE FILES\]

> This option is used to download Surgery interface files to the Automated Anesthesia Information System (AAIS). The process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send Health Level 7 (HL7) master file updates.

## Flag Drugs for Use as Anesthesia Agents \[SROCODE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to flag drugs for use as anesthesia agents. Only those drugs that are flagged will be available when selecting anesthesia agents.

> *Flag Interface Fields* \[SRHL INTERFACE FLDS\]

> This option allows the package coordinator to set the INTERFACE field in the SURGERY INTERFACE file (#133.2). The categories listed on the first screen correspond to entries in the SURGERY INTERFACE file (#133.2). These categories are listed in the Surgery Health Level 7 Interface Specifications document as being the OBR (Observation Request) text identifiers. Each identifier corresponds to several fields in the VistA Surgery package. This allows the user to control the flow of data between the VistA Surgery package and the ancillary system on a field-by-field basis.

> The option lists each identifier and its current setting. To receive the data coming from the ancillary system for a category, set the flag to R for receive. To ignore the data, set the flag to N for not receive. To see a second underlying layer of OBX (Observation Information) text identifiers (fields in SURGERY file (#130) and their settings), set the OBR text identifier to RR for receive. The option will allow the user to toggle the settings for a range or for individual items.

> *Intraoperative Occurrences (Enter/Edit)* \[SRO INTRAOP COMP\]

> This option is used to enter or edit intraoperative occurrences. Every occurrence entered must have a corresponding perioperative occurrence category.

> *Key Missing Surgical Package Data* \[SROQ MISSING DATA\]

> This option generates a list of surgical cases performed within the selected date range that are missing key information. This report includes surgical cases with an entry in the TIME PAT IN OR field and does not include aborted cases.

> *Laboratory Interim Report* \[SRO-LRRP\]

> This option will print or display interim reports for a selected patient, within a given time period. The printout will go in inverse date order. This report will output all tests for the time period specified. If no results are available, the option will ask for another patient. This option will only print verified results and at present does not output the microbiology reports.

> *Laboratory Test Results (Enter/Edit)* \[SROA LAB\]

> Print a Surgery Risk Assessment

> Update Assessment Completed/Transmitted in Error List of Surgery Risk Assessments

> Print 30 Day Follow-up Letters Exclusion Criteria (Enter/Edit)

> Monthly Surgical Case Workload Report

> Update Operations as Unrelated/Related to Death M&M Verification Report

> Update 1-Liner Case

> Queue Assessment Transmissions Risk Model Lab Test (Enter/Edit)

> CPT/ICD Coding Menu Locked with SR CODER

> CPT/ICD Update/Verify Menu Locked with SR CODER

> Update/Verify Procedure/Diagnosis Codes Operation/Procedure Report

> Nurse Intraoperative Report Non-OR Procedure Information

> Cumulative Report of CPT Codes Report of CPT Coding Accuracy

> List Completed Cases Missing CPT Codes List of Operations

> List of Operations (by Surgical Specialty) List of Undictated Operations

> Report of Daily Operating Room Activity PCE Filing Status Report

> Report of Non-O.R. Procedures

> Transplant Assessment Menu Locked with SR TRANSPLANT

> Enter/Edit Transplant Assessments Print Transplant Assessment

> List of Transplant Assessments

> Transplant Assessment Parameters (Enter/Edit)

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 23 security keys in the Surgery package. Most are used to restrict access to certain options within the package. Other keys can be used to restrict which people can be entered in specific fields. This section of the manual describes each key. These descriptions can aid the package coordinator in assigning security levels to the user personnel. A list of users' names and security key levels must be supplied to the site manager.

> The following keys are used to determine whether a person can be entered in a specific field. Surgery V.

> 3.0 allows the user to restrict entries for any “person” type field based on keys. For example, the user could restrict entries into the SURGEON (.14) field in the SURGERY (#130) file to only those people who are holders of the SR SURGEON key. When entering data for a surgical case, only those people can be selected as a surgeon. Restriction of fields is not limited to the keys listed below. The user can use any existing key, or create keys of their own, to restrict access. The keys listed below are supplied for convenience. If the user does not choose to restrict "person" type fields, these keys will not be used elsewhere in the Surgery package.

| Security Key       | Description                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| SR ANESTHESIOLOGIST    | This key is used to restrict entry into selected fields in which an anesthesiologist can be entered. |
| SR MED STUDENT         | This key is used to restrict entry into selected fields in which a medical student can be entered.   |
| SR NURSE               | This key is used to restrict entry into selected fields in which a nurse can be entered.             |
| SR NURSE ANESTHETIST   | This key is used to restrict entry into fields in which a nurse anesthetist can be entered.          |
| SR PHYSICIAN ASSISTANT | This key is used to restrict entry into fields in which a physician assistant can be entered.        |
| SR SURGEON             | This key is used to restrict entry into fields in which a surgeon can be entered.                    |

> ![](sr-3-176-surgery-vasqip-2012-technical-manual-security-guide-change-pages/002.png)The following keys are used to restrict access to menus and options. Only holders of these keys will be permitted to access the locked options or functions.

| Security Key   | Description                                                                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SR CODER           | This key should be given to those responsible for entering CPT and ICD codes for operations and non-OR procedures. This key is used to lock the Surgery *CPT/ICD Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] option.                  |
| SR REQ OVERRIDE    | This key allows users to make operation requests beyond the site selected cutoff times. The SR REQ OVERRIDE key should only be given to those users that are permitted to make this type of last minute request.                              |
| SR RISK ASSESSMENT | This key is used to lock the *Surgery Risk Assessment Menu* \[SROA RISK ASSESSMENT\] option and all the options it contains. The SR RISK ASSESSMENT key should be given to the Surgery Risk Data Manager and Surgery Application Coordinator. |
| SR STAFF SURGEON   | This key is used to determine whether a person is a staff surgeon.                                                                                                                                                                            |
| SRCOORD            | This key is used to lock the *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] *option* and the options it contains. The SRCOORD key should be given to the Surgery Application Coordinator.                                       |
| SROAAMIS           | This key is required when accessing the *Anesthesia AMIS* \[SROAMIS\] option and should be given to only those users that will need to print the Anesthesia AMIS Report.                                                                      |
| SROANES            | This key is required when accessing any anesthesia related option, with the exception of the *Anesthesia AMIS* \[SROAMIS\] option, which has its own unique key.                                                                              |
| SROCHIEF           | This key is required when accessing the *Chief of Surgery Menu* \[SROCHIEF\] option and the options it contains. The SROCHIEF key should be given to the Surgery Application Coordinator, Chief of Surgery, and his or her designee.          |
| SROCOMP            | This key is used to lock the *Perioperative Occurrences Menu* \[SRO COMPLICATIONS MENU\] option. It should be given to those users permitted to enter, edit, and delete surgical complications.                                               |
| SROEDIT            | This key is required when entering or editing Surgery related data. Users that do <u>not</u> have this key are limited to viewing access, rather than editing access, on all Surgery screens.                                                 |
| SROPER             | This key is required to access the *Operation Menu* \[SROPER\] option and all of the options it contains.                                                                                                                                     |
| SROREP             | This key is required when accessing the *Surgery Reports* \[SRORPTS\] option. Options in this menu cannot be accessed without this key.                                                                                                       |
| SROREQ             | This key is required when accessing the *Request Operations* \[SROREQ\] option, and is given only to those users responsible for making requests.                                                                                             |
| SROSCH             | This key is required when accessing the *Schedule Operations* \[SROSCHOP\] option and is given only to users responsible for scheduling operations.                                                                                           |

| Security Key | Description                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SROSURG          | This key is required when accessing the *Undictated Operations* \[SRODICT\] option and the *Enter/Edit Non-Operative Complications* \[SROCOMP\] option.                                                     |
| SROWAIT          | This key is required when accessing the *Maintain Surgery Waiting List* \[SROWAIT\] option. Only users responsible for adding, changing, deleting, or printing data on the waiting list are given this key. |
| SR TRANSPLANT    | This key is used to restrict entry into the Transplant Assessment module.                                                                                                                                   |

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term/Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Not Complete</td>
<td><p>Case status indicating one of the following two situations with no entry in the TIME PAT OUT OR field (#.232):</p>
<ol type="1">
<li><p>Case has entry in TIME PAT IN OR field (#.205).</p></li>
<li><p>Case has not been requested or scheduled.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Operation Code</td>
<td>Identifying code for reporting medical services and procedures performed by physicians. See CPT Code.</td>
</tr>
<tr class="odd">
<td>PACU</td>
<td>Post Anesthesia Care Unit.</td>
</tr>
<tr class="even">
<td>Postoperative Occurrence</td>
<td>Perioperative occurrence following the procedure.</td>
</tr>
<tr class="odd">
<td>Procedure Occurrence</td>
<td>Occurrence related to a non-OR procedure.</td>
</tr>
<tr class="even">
<td>Requested</td>
<td>Operation has been slotted for a particular day but the time and operating room are not yet firm.</td>
</tr>
<tr class="odd">
<td>Risk Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>Scheduled</td>
<td>Operation has both an operating room and a scheduled starting time, but the operation has not yet begun.</td>
</tr>
<tr class="odd">
<td>Screen</td>
<td>An illuminated display surface on which display images are presented.</td>
</tr>
<tr class="even">
<td>Screen Server</td>
<td>A format for displaying data on a cathode ray tube display. Screen Server is designed specifically for the Surgery Package.</td>
</tr>
<tr class="odd">
<td>Screen Server Function</td>
<td>The Screen Server prompt for data entry.</td>
</tr>
<tr class="even">
<td>Service Blockouts</td>
<td>The reservation of an operating room for a particular service on a recurring basis. The reservation is charted on a blockout graph.</td>
</tr>
<tr class="odd">
<td>Transplant Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical transplant risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>VASQIP</td>
<td>VA Surgical Quality Improvement Program.</td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### A

> anesthesia agents, 13, 26
> Anesthesia Menu, 22, 67
> Anesthesia Report, 9, 14, 16, 22, 64, 67
> Archiving, 44

#### B

> background tasks, 10, 37

#### C

> callable entry points, 46 Calls, 48
> Change Site Parameters, 71 configurable files, 13, 39
> contingency plan, 60
> CPT/ICD Coding Menu, 23, 71

#### D

> Data Base Integration Agreements, 46, 52

#### E

> exported files, 14, 15, 18
> external packages, 48

#### F

> Field Station Information Security Officers, 60 File descriptions, 16
> Files, 13, 39, 70, 76
> FORUM, 52

#### G

> generic interface, 62 GET ACCOUNT call, 80
> send to PCE, 88
> surgery case cancelled, 86 surgery case creation, 82 surgery case update, 84 surgery request, 80
> globals, 42

#### H

> HL7, 26, 36, 38, 39, 62
> holidays, 9
> HOSPITAL LOCATION file, 10
> I
> IAs, 46, 52
> initialization routines, 18
> Input Templates, 40, 41
> installation, 7, 18
> interface, 8, 26, 36, 39, 62
> ISOs, 60

#### J

> journaling, 42

#### K

> key, 3
> keys, 7, 25, 33, 34, 72, 73

#### L

> List Operation Requests, 27, 66
> List Scheduled Operations, 27, 67

#### M

> mail groups, 13
> Maintain Surgery Waiting List, 28, 66, 74

#### N

> namespaced, 56
> NEW PERSON file, 7
> Non-O.R. Procedures, 23, 29, 35, 68, 71
> Nurse Intraoperative Report, 8, 14, 30, 64, 67

#### O

> Operation Menu, 23, 31, 67
> Operation Report, 14, 16, 31, 67
> operative procedure, 1, 14, 16, 27, 28, 29, 30
> Option Descriptions, 22
> OPTION file, 54

#### P

> package-wide variables, 56
> Patient Financial Services System, 80 Perioperative Occurrences Menu, 33, 67 Print a Transplant Assessment, 71 protocol, 18, 36, 37, 62
> Purging, 44
> March 2012 Surgery V. 3.0 Technical Manual/Security Guide 81

#### R

> REQUEST CUTOFF FOR SUNDAY field, 9
> Request Operations, 35, 66, 73
> routines, 18, 46, 48

#### S

> Schedule Operations, 36, 66, 74
> Security Keys, 7
> Site Specific Parameters, 7 Sort Template, 40
> SR REQ OVERRIDE key, 73
> SURGERY file, 14, 16, 22, 26, 30, 38, 47, 56
> *Surgery Nightly Cleanup and Updates*, 37, 44 Surgery Package Management Menu option, 7,
> 11, 13, 73
> Surgery Site Parameters, 7, 37, 70
> SURGERY UTILIZATION file, 30, 44

#### T

> templates, 41
> Transplant Assessment Menu, 71

#### V

> View a List of Transplant Assessments, 71

#### X

> XU FIRST LINE PRINT, 18
