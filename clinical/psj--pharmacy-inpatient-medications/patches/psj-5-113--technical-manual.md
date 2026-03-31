---
title: PSJ*5*113 Technical Manual / Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*113
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Version 5.0](#version-50) - [Revision History](#revision-history) - [Descriptions](#descriptions) - [Callable Routines](#callable-routines) - [Routine Mapping](#routine-mapping) - [Do Not Map](#do-not-map) > December 1997 > (Revised June 2010) > Department of Veterans Affairs > VistA Health Syste
audience: 
keywords: 
  - blockquote
  - class
  - table
  - style
  - width
  - mark
  - even
  - strong
  - psgoe
  - contents
page_count: 0
word_count: 1363
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p113_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p113_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-113-technical-manual-security-guide-change-pages/001.png)

INPATIENT MEDICATIONS

> TECHNICAL MANUAL/ SECURITY GUIDE

# Version 5.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Version 5.0](#version-50)
- [Revision History](#revision-history)
  - [Descriptions](#descriptions)
  - [Callable Routines](#callable-routines)
  - [Routine Mapping](#routine-mapping)
    - [Do Not Map](#do-not-map)
> December 1997
> (Revised June 2010)
> Department of Veterans Affairs
> VistA Health Systems Design and Development

# Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
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
<td>06/10</td>
<td>i, 22-23</td>
<td><blockquote>
<p>PSJ*5*113</p>
</blockquote></td>
<td><p>Added routine PSGSICH1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/10</td>
<td><blockquote>
<p>i, 23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*214</p>
</blockquote></td>
<td><p>Added PSJQUTIL to the routine list in Section 5.1 for Patients on Specific Drug(s) Multidivisional Enhancements Project.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/09</td>
<td>22-23</td>
<td><blockquote>
<p>PSJ*5*222</p>
</blockquote></td>
<td><p>Added routine PSGOEF2.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/08</td>
<td><blockquote>
<p>vi, 23, 51-</p>
<p>53, 57-58,</p>
<p>60-61, 63,</p>
<p>65, 65a-</p>
<p>65b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*134</p>
</blockquote></td>
<td><p>Parameters for escaping special characters added. New HL7 messages added. New routines added. HL7 order fields table contains an asterisk for each field that has special escaping characters.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/07</td>
<td>74-76</td>
<td><blockquote>
<p>PSJ*5*178</p>
</blockquote></td>
<td><p>MED ROUTE now appears in larger font on IV labels from the Zebra bar code printer. Med ROUTE now prints on the IV labels for bar-code enabled printers, and it prints in larger font than surrounding text.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/06</td>
<td>23, 94</td>
<td><blockquote>
<p>PSJ*5*172</p>
</blockquote></td>
<td><p>Encapsulation Cycle II project: Added PSJ53P1 to the Routine List in Section 5.1. Added DBIA 4537 to DBIA list. Changed the date on the Title Page to December 1997.</p>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/06</td>
<td><blockquote>
<p>v-viii 8a-8b 66-68b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*154</p>
</blockquote></td>
<td><p>In Section 2.2.2 Added “PRIORITIES FOR NOTIFICATION”</p>
<p>field.</p>
<p>In Section 9.5, made correction to include the priority of ASAP in notifications. Added information regarding the three notifications parameters.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2005</td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*146</p>
</blockquote></td>
<td><p>Remote Data Interoperability (RDI) Project: Added PSJLMUT2 to the Routine List in Section 5.1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

> June 2010 Inpatient Medications V. 5.0 i Technical Manual/Security Guide

> PSJ\*5\*113

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
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
<td>11/2005</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*163</p>
</blockquote></td>
<td><p>Encapsulation Cycle II project: Added PSJ59P5 to the Routine List in Section 5.1. Added DBIA 4819 to DBIA list. Deleted DBIAs 172, 634, and 1882 from the DBIA list.</p>
<p>Reissued entire document due to a page numbering issue. <mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

> ii Inpatient Medications V. 5.0 November 2005 Technical Manual/Security Guide

5.  Routines

## Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following routines are exported by the Inpatient Medications package. Routine names starting with the letters PSG designate routines used mainly by the Unit Dose Medications module. Routine names starting with the letters PSIV designate routines used mainly by the IV Medications module. Routine names starting with the letters PSJ designate Inpatient Medications routines - utilities used by IV, Unit Dose, and other packages.

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>PSGAL5</th>
<th><blockquote>
<p>PSGAMS</p>
</blockquote></th>
<th>PSGAMS0</th>
<th><blockquote>
<p>PSGAMSA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSGAP</td>
<td><blockquote>
<p>PSGAP0</p>
</blockquote></td>
<td>PSGAPH</td>
<td><blockquote>
<p>PSGAPIV</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGAPP</td>
<td><blockquote>
<p>PSGAXR</p>
</blockquote></td>
<td>PSGBRJ</td>
<td><blockquote>
<p>PSGCAP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGCAP0</td>
<td><blockquote>
<p>PSGCAPIV</p>
</blockquote></td>
<td>PSGCAPP</td>
<td>PSGCAPP0</td>
</tr>
<tr class="even">
<td>PSGCT</td>
<td><blockquote>
<p>PSGDCC</p>
</blockquote></td>
<td>PSGDCCM</td>
<td><blockquote>
<p>PSGDCR0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGDCT</td>
<td><blockquote>
<p>PSGDCT1</p>
</blockquote></td>
<td>PSGDCTP</td>
<td><blockquote>
<p>PSGDL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGDS</td>
<td><blockquote>
<p>PSGDS0</p>
</blockquote></td>
<td>PSGDSP</td>
<td><blockquote>
<p>PSGDSP0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGDSP1</td>
<td><blockquote>
<p>PSGDSPN</p>
</blockquote></td>
<td>PSGEUD</td>
<td><blockquote>
<p>PSGEUDD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGEUDP</td>
<td><blockquote>
<p>PSGFILD0</p>
</blockquote></td>
<td>PSGFILD1</td>
<td><blockquote>
<p>PSGFILD2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGFILD3</td>
<td><blockquote>
<p>PSGFILED</p>
</blockquote></td>
<td>PSGGAO</td>
<td><blockquote>
<p>PSGIU</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGL</td>
<td><blockquote>
<p>PSGL0</p>
</blockquote></td>
<td>PSGLBA</td>
<td><blockquote>
<p>PSGLH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGLOI</td>
<td><blockquote>
<p>PSGLPI</p>
</blockquote></td>
<td>PSGLW</td>
<td><blockquote>
<p>PSGMAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGMAR0</td>
<td><blockquote>
<p>PSGMAR1</p>
</blockquote></td>
<td>PSGMAR2</td>
<td><blockquote>
<p>PSGMAR3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGMI</td>
<td><blockquote>
<p>PSGMIV</p>
</blockquote></td>
<td>PSGMMAR</td>
<td><blockquote>
<p>PSGMMAR0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGMMAR1</td>
<td><blockquote>
<p>PSGMMAR2</p>
</blockquote></td>
<td>PSGMMAR3</td>
<td>PSGMMAR4</td>
</tr>
<tr class="odd">
<td>PSGMMAR5</td>
<td><blockquote>
<p>PSGMMARH</p>
</blockquote></td>
<td>PSGMMIV</td>
<td><blockquote>
<p>PSGMMIVC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGMUTL</td>
<td><blockquote>
<p>PSGNE3</p>
</blockquote></td>
<td>PSGO</td>
<td><blockquote>
<p>PSGOD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGOE</td>
<td><blockquote>
<p>PSGOE0</p>
</blockquote></td>
<td>PSGOE1</td>
<td>PSGOE2</td>
</tr>
<tr class="even">
<td>PSGOE3</td>
<td><blockquote>
<p>PSGOE31</p>
</blockquote></td>
<td>PSGOE4</td>
<td><blockquote>
<p>PSGOE41</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSGOE42</td>
<td><blockquote>
<p>PSGOE5</p>
</blockquote></td>
<td>PSGOE6</td>
<td><blockquote>
<p>PSGOE7</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSGOE8</td>
<td><blockquote>
<p>PSGOE81</p>
</blockquote></td>
<td>PSGOE82</td>
<td><blockquote>
<p>PSGOE9</p>
</blockquote></td>
</tr>
</tbody>
</table>

November 2005 Inpatient Medications V. 5.0 21

> Technical Manual/Security Guide

| PSGOE91  | PSGOE92  | PSGOEC   | PSGOECA  |
|----------|----------|----------|----------|
| PSGOECS  | PSGOEE   | PSGOEE0  | PSGOEEW  |
| PSGOEF   | PSGOEF1  | PSGOEF2  | PSGOEH0  |
| PSGOEH1  | PSGOEHA  | PSGOEI   | PSGOEL   |
| PSGOEM   | PSGOEM1  | PSGOENG  | PSGOEPO  |
| PSGOER   | PSGOER0  | PSGOER1  | PSGOERI  |
| PSGOERS  | PSGOES   | PSGOESF  | PSGOETO  |
| PSGOETO1 | PSGOEV   | PSGOEVS  | PSGON    |
| PSGORS0  | PSGORVW  | PSGOT    | PSGOTR   |
| PSGOU    | PSGP     | PSGPEN   | PSGPER   |
| PSGPER0  | PSGPER1  | PSGPER2  | PSGPL    |
| PSGPL0   | PSGPL1   | PSGPLD   | PSGPLDP  |
| PSGPLDP0 | PSGPLDPH | PSGPLF   | PSGPLFM  |
| PSGPLG   | PSGPLPRG | PSGPLR   | PSGPLR0  |
| PSGPLRP  | PSGPLUP  | PSGPLUP0 | PSGPLUTL |
| PSGPLXR  | PSGPO    | PSGPOR   | PSGPR    |
| PSGPRVR  | PSGPRVR0 | PSGRET   | PSGRPNT  |
| PSGS0    | PSGSCT   | PSGSCT0  | PSGSEL   |
| PSGSET   | PSGSETU  | PSGSH    | PSGSICH1 |
| PSGSICHK | PSGSSP   | PSGTAP   | PSGTAP0  |
| PSGTAP1  | PSGTCTD  | PSGTCTD0 | PSGTI    |
| PSGVBW   | PSGVBW0  | PSGVBW1  | PSGVBWP  |
| PSGVBWU  | PSGVDS   | PSGVW    | PSGVW0   |
| PSGVWP   | PSIV     | PSIVACT  | PSIVAL   |
| PSIVALN  | PSIVALNC | PSIVAMIS | PSIVAOR  |
| PSIVAOR1 | PSIVBCID | PSIVCAL  | PSIVCHK  |
| PSIVCHK1 | PSIVCSED | PSIVDCR  | PSIVDCR1 |
| PSIVDCR2 | PSIVDRG  | PSIVEDRG | PSIVEDT  |
| PSIVEDT1 | PSIVHIS  | PSIVHLD  | PSIVHLP  |
| PSIVHLP1 | PSIVHLP2 | PSIVHLP3 | PSIVHYP  |
| PSIVHYPL | PSIVHYPR | PSIVLABL | PSIVLABR |
| PSIVLB   | PSIVLBDL | PSIVLBL1 | PSIVLBRP |
| PSIVLTR  | PSIVLTR1 | PSIVMAN  | PSIVMAN1 |
| PSIVOE   | PSIVOPT  | PSIVOPT1 | PSIVOPT2 |
| PSIVORA  | PSIVORA1 | PSIVORAL | PSIVORC  |
| PSIVORC1 | PSIVORC2 | PSIVORE  | PSIVORE1 |
| PSIVORE2 | PSIVOREN | PSIVORFA | PSIVORFB |
| PSIVORFE | PSIVORH  | PSIVORLB | PSIVORV1 |
| PSIVORV2 | PSIVPAT  | PSIVPCR  | PSIVPCR1 |
| PSIVPGE  | PSIVPR   | PSIVPRO  | PSIVQUI  |
| PSIVRD   | PSIVRDC  | PSIVREC  | PSIVRNL  |
| PSIVRP   | PSIVRP1  | PSIVRQ   | PSIVRQ1  |
| PSIVSET  | PSIVSP   | PSIVSPDC | PSIVST2  |

> 22 Inpatient Medications V. 5.0 June 2010 Technical Manual/Security Guide

> PSJ\*5\*113

| PSIVSTAT | PSIVSUS  | PSIVSUS1 | PSIVUDL  |
|----------|----------|----------|----------|
| PSIVUTL  | PSIVUTL1 | PSIVUWL  | PSIVVW1  |
| PSIVWCR  | PSIVWCR1 | PSIVWL   | PSIVWL1  |
| PSIVWRP  | PSIVXREF | PSIVXU   | PSJ53P1  |
| PSJ59P5  | PSJAC    | PSJADT   | PSJADT0  |
| PSJADT1  | PSJADT2  | PSJALG   | PSJBCMA  |
| PSJBCMA1 | PSJBCMA2 | PSJBCMA3 | PSJBCMA4 |
| PSJCOM   | PSJCOM1  | PSJCOMR  | PSJCOMV  |
| PSJDCHK  | PSJDCU   | PSJDDUT  | PSJDDUT2 |
| PSJDDUT3 | PSJDEA   | PSJDGAL  | PSJDIN   |
| PSJDOSE  | PSJDPT   | PSJEEU   | PSJEEU0  |
| PSJENV   | PSJEXP   | PSJEXP0  | PSJFTR   |
| PSJH1    | PSJHEAD  | PSJHEH   | PSJHIS   |
| PSJHL10  | PSJHL11  | PSJHL2   | PSJHL3   |
| PSJHL4   | PSJHL4A  | PSJHL5   | PSJHL6   |
| PSJHL7   | PSJHL9   | PSJHLERR | PSJHLU   |
| PSJHLV   | PSJHVARS | PSJLIACT | PSJLIFN  |
| PSJLIFNI | PSJLIORD | PSJLIPRF | PSJLIUTL |
| PSJLIVFD | PSJLIVMD | PSJLMAL  | PSJLMDA  |
| PSJLMGUD | PSJLMHED | PSJLMPRI | PSJLMPRU |
| PSJLMUDE | PSJLMUT1 | PSJLMUT2 | PSJLMUTL |
| PSJLOAD  | PSJLOI   | PSJMAI   | PSJMAI1  |
| PSJMDIR  | PSJMDIR1 | PSJMDWS  | PSJMEDS  |
| PSJMIV   | PSJMP    | PSJMPEND | PSJMPRT  |
| PSJMPRTU | PSJMUTL  | PSJNTEG  | PSJNTEG0 |
| PSJNTEG1 | PSJO     | PSJO1    | PSJO2    |
| PSJO3    | PSJOE    | PSJOE0   | PSJOE1   |
| PSJOEA   | PSJOEA1  | PSJOEEW  | PSJOERI  |
| PSJORAPI | PSJORDA  | PSJOREN  | PSJORMA1 |
| PSJORMA2 | PSJORMAR | PSJORP2  | PSJORPOE |
| PSJORRE  | PSJORRE1 | PSJORREN | PSJORRN  |
| PSJORRN1 | PSJORRO  | PSJORUT2 | PSJORUTL |
| PSJP     | PSJPATMR | PSJPDIR  | PSJPDV   |
| PSJPDV0  | PSJPDV1  | PSJPL0   | PSJPR    |
| PSJPR0   | PSJPST50 | PSJPXRM1 | PSJQPR   |
| PSJQUTIL | PSJRXI   | PSJSPU   | PSJSPU0  |
| PSJSV    | PSJSV0   | PSJUNITD | PSJUTL   |
| PSJUTL1  | PSJUTL2  | PSJUTL3  | PSJUTL5  |
| PSJUTL6  |          |          |          |

June 2010 Inpatient Medications V. 5.0 23

> Technical Manual/Security Guide PSJ\*5\*113

> The following routines are not used in this version of Inpatient Medications. They were exported in the initial Kernel Installation and Distribution System (KIDS) build as Delete at Site.

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>PSGDCR</th>
<th><blockquote>
<p>PSGDCT0</p>
</blockquote></th>
<th>PSGEXP</th>
<th>PSGEXP0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSGMMPST</td>
<td><blockquote>
<p>PSGOROE0</p>
</blockquote></td>
<td>PSGORU</td>
<td><blockquote>
<p>PSGQOS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSIVNVO</td>
<td><blockquote>
<p>PSIVOEDO</p>
</blockquote></td>
<td>PSIVOENT</td>
<td><blockquote>
<p>PSIVOEPT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSIVRD0</td>
<td><blockquote>
<p>PSIVRD0</p>
</blockquote></td>
<td>PSJMAN</td>
<td>PSJOAC</td>
</tr>
<tr class="even">
<td>PSJOAC0</td>
<td><blockquote>
<p>PSJOE8</p>
</blockquote></td>
<td>PSJOE81</td>
<td><blockquote>
<p>PSJOEE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSJOER</td>
<td><blockquote>
<p>PSJOER0</p>
</blockquote></td>
<td>PSJORA</td>
<td><blockquote>
<p>PSJORIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSJUTL</td>
<td><blockquote>
<p>PSJUTL1</p>
</blockquote></td>
<td>PSJUTL2</td>
<td><blockquote>
<p>PSJUTL3</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Entry points provided by the Inpatient Medications package to other packages can be found in the External Relationships section of this manual. No other routines are designated as callable from outside of this package.

## Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routines not listed here are used sparingly, and can be mapped if the site desires.

### Do Not Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSGXR\* PSJIP\* PSJXR\*

> The PSGXR\* and PSJXR\* routines are created by VA FileMan when it compiles the cross- references of the NON-VERIFIED ORDERS (#53.1) and PHARMACY PATIENT (#55) files.

> 24 Inpatient Medications V. 5.0 November 2005 Technical Manual/Security Guide