---
title: IVMB*2*686 Geographic Means Test (GMT) Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Geographic Means Test (GMT)
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*686
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - conversion
  - table
  - ivmb
  - installation
  - contents
  - install
  - patch
  - distribution
  - transport
page_count: 0
word_count: 2708
section_count: 10
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

geographic means test (GMT)

installation guide

IVMB\*2\*686

December 2002

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Related Manuals](#related-manuals)
- [Preinstallation Considerations](#preinstallation-considerations)
  - [Patch Installation Sequence](#patch-installation-sequence)
  - [User Access to the GMT Menu Options](#user-access-to-the-gmt-menu-options)
  - [Other Software Versions Required](#other-software-versions-required)
  - [Routine List with Checksums](#routine-list-with-checksums)
- [Installation Instructions](#installation-instructions)
- [Sample Installation](#sample-installation)
- [Post-Installation Considerations](#post-installation-considerations)
  - [GMT Conversion](#gmt-conversion)
  - [Initiating the Conversion](#initiating-the-conversion)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, President Bush signed into law Public Law 107-135, *The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001*. Section 202 of this Act requires the implementation of HUD indices to determine geographic income thresholds in support of more discrete means testing. Veterans in Priority Group 7 are eligible for treatment as a low-income family under section 3(b) of the United States Housing Act of 1973 (42 U.S.C. 1437a(b)) for the area in which such veterans reside, regardless of whether such veterans are treated as single person families under paragraph (3)(A) of such section 3(b) or as families under paragraph (3)(b). This Act also established Priority Group 8 for any veterans described in section 1710(a)(3) of titles 38 U.S.C. who are not covered by Priority Group 7.

Development of the GMT software is a combined effort on the part of Office of Policy and Planning (OPP), Office of Information (OI), and Chief Business Office (CBO).

A one-time conversion of Means Test Copay Required veterans who declined to provide income information, whose means test is greater than one year old or whose current income is greater than the MT threshold will occur only in the HEC Legacy system upon implementation of the GMT software. This conversion will determine whether these veterans should be placed in the new Priority Group 8 or the new GMT Copay Required means test status. The results of the conversion will be transmitted to all applicable VAMCs upon completion of the process.

During the processing of the GMT Conversion, a HEC user can monitor the progress by running the GMT Conversion Processing Report. Refer to the GMT Technical Manual for information about how to generate and use this report.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of Patch IVMB\*2\*686 is to implement the functionality defining Geographic Means Test (GMT). The purpose of this installation guide document is to provide guidance to technical staff who will be installing and maintaining the GMT software.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 
- 
- 

GMT User Manual (IVMB_2_P686_UM.PDF)GMT Technical Manual (IVMB_2_P686_TM.PDF)GMT Release Notes (IVMB_2_P686_RN.PDF)

# Preinstallation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful GMT implementation will require that all GMT patches are installed in the sequence specified in the following table. Implementation cannot proceed from one step to the next step until each step has been completed at all applicable facilities. Please note that installation of Patch IVMB\*2\*686 takes place as Step 3 in the table. Due to the data conversion and billing components, there can be no exception to this requirement.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 10%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Patches</strong></th>
<th><p><strong>Release to</strong></p>
<p><strong>NVS</strong></p></th>
<th><p><strong>National</strong></p>
<p><strong>Release to</strong></p>
<p><strong>Field</strong></p></th>
<th colspan="2"><p><strong>Compliance</strong></p>
<p><strong>Date</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p><strong>IB Part 1</strong></p>
<p>IB*2.0*179</p></td>
<td><strong>9/20/02</strong></td>
<td><strong>9/25/02</strong></td>
<td colspan="2"><strong>9/30/02</strong></td>
<td>Effective Date: 10/1/02</td>
</tr>
<tr class="even">
<td>2</td>
<td><p><strong>AI Kernel</strong></p>
<p>XU*8*246</p>
<p><em><strong>The following patches are being released in HOST file DG_53_P454.KID:</strong></em></p>
<p><strong>Enrollment V<em>IST</em>A Part 1</strong></p>
<p>DG *5.3*454</p>
<p>IVM*2*58</p>
<p><strong>PIMS</strong></p>
<p>DG*5.3*466</p>
<p>SD*5.3*258</p></td>
<td><strong>11/25/02</strong></td>
<td><strong>12/2/2002</strong></td>
<td colspan="2"><strong>12/4/2002</strong></td>
<td><ol type="1">
<li></li>
<li></li>
<li></li>
<li></li>
</ol></td>
</tr>
<tr class="odd">
<td>Release Kernel patch first; sites must install before PIMS &amp; Enrollment patches. Release PIMS &amp; Enrollment patches in HOST file DG_53_P454.KID. NVS sends patches to Hines Anonymous directory 11/29 and monitors replication to Albany &amp; SLC servers 11/30 – 12/1. Project Implementation Team will contact sites not in compliance on 12/5/02. 3</td>
<td><p><strong>HEC Legacy</strong></p>
<p>IVMB*2*686</p></td>
<td><strong>N/A</strong></td>
<td><p><strong>Release to HEC Production</strong></p>
<p><strong>12/9/02</strong></p></td>
<td colspan="2"><strong>12/11/02</strong></td>
<td>Monitor in HEC production 12/9-10-11</td>
</tr>
<tr class="even">
<td>4</td>
<td><p><em><strong>The following files are being released in HOST file EAS_1_P13.KID:</strong></em></p>
<p><strong>Enrollment V<em>IST</em>A Part 2</strong></p>
<p>EAS*1*13</p>
<p>DG*5.3*456</p>
<p>IVM*2*62</p>
<p><strong>IB Part 2</strong></p>
<p>IB*2.0*183</p>
<p>PRCA*4.5*181</p></td>
<td><strong>12/5/02</strong></td>
<td><strong>12/16/02</strong></td>
<td colspan="2"><strong>12/19/02</strong></td>
<td><ol type="1">
<li></li>
<li></li>
<li></li>
</ol></td>
</tr>
<tr class="odd">
<td>Release PIMS &amp; Enrollment patches in HOST file EAS_1_P13.KID. NVS sends patches to Hines Anonymous directory 12/13 and monitors replication to Albany &amp; SLC servers 12/13 – 12/14. Project Implementation Team will contact sites not in compliance on 12/20/02. 5</td>
<td colspan="6"><em><strong>All patches listed in Steps 1 – 4 above must be operational at sites on 1/03/03</strong></em></td>
</tr>
<tr class="even">
<td>6</td>
<td><p>IVM*2*67</p>
<p>DG*5.3*481</p>
<p>IB*2.0*202</p></td>
<td>Approximately 2 weeks after conversion completion (date TBD)</td>
<td colspan="2">TBD</td>
<td>TBD</td>
<td>Clean up patches to remove code no longer used after GMT conversion completes. Patches will be released in a HOST file.</td>
</tr>
</tbody>
</table>

## User Access to the GMT Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can access the following GMT options from the DCD Contact Representative Menu. Refer to the HEC GMT User Manual for instructions about how to use the options.

- 
- 

GMT Threshold Address LookupGMT Threshold Lookup by ZIP Code or City

## Other Software Versions Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your system must be running the following minimum software versions or higher to successfully implement and operate the GMT software:

- 
- 
- 
- 

VA FileMan V. 22.0VA MailMan V. 8.0Kernel V. 8.0V*IST*A HL7 V. 1.6

## Routine List with Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;2.0;INCOME VERIFICATION;\*\*\[patch list\]\*\*;May 25, 1994

Routine name Before Patch After Patch Patch List

============ ============ =========== ==========

AYAZ05 2854545 3307972 2,174,217,243,418

521,635,680,692,693

686

AYAZ052 2458618 3222821 24,2,686

AYCBBP1 14945427 14945472 256,450,686

AYCBBUT7 7637796 7640520 256,455,686

AYCBCADR 9334615 8914740 229,248,438,686

AYCBCDT1 2118123 2219329 277,392,453,686

AYCBCDT2 3442251 3563048 277,392,453,686

AYCBCEN 9527364 9591679 277,392,399,453,497

455,614,686

AYCBCMN 13903817 13857767 277,510,455,463,601

686

AYCBEGT 2985576 2985658 392,453,487,614,686

AYCBEGT1 5686287 5705082 392,614,686

AYCBEGT3 9445095 9445136 392,427,614,686

AYCBENA1 12281537 12810815 190,257,290,315,392

453,485,506,523,455

491,614,544,686

AYCBENA4 5966573 6080039 392,455,614,686

AYCBENAV 5179127 5260933 188,195,201,221,190

257,287,295,330,359

392,455,532,601,620

686

Routine List with Checksums, continued

AYCBHL71 1440223 2159093 356,686

AYCBLTR1 4772449 4809075 178,189,394,392,398

400,405,416,420,425

411,453,487,535,567

614,686

AYCBLTRI 6870642 6870725 392,398,400,420,453

487,686

AYCBLTRV 7337952 7667540 198,248,392,411,453

487,491,535,686

AYCBPRI2 3229846 3242113 392,453,614,686

AYCBPRIO 8449309 8724400 94,120,132,141,142

188,235,241,392,453

455,491,636,686

AYCBRLT1 5920567 5974778 453,686

AYCBRLT2 7320475 7590996 453,614,686

AYCBTAAC 10277952 10280676 125,224,313,332,401,

455,561,601,628,634,

645,686

AYCBUTIL 5599737 5607705 201,206,228,190,238

356,277,392,455,491

614,612,686

AYCBUTL1 8931832 9169394 229,279,340,686

AYCBUTL2 5663532 5666256 248,332,455,601,686

AYCBVUTL 14563366 14972237 190,257,281,287,295

340,332,392,401,417

428,455,570,696,686

AYCEPHPC 9795909 9998622 491,614,686

AYCGMTLP N/A 7038181 686

AYCGMTUL N/A 5381563 686

AYCHLSA7 8435377 9003270 412,600,627,686

AYCHZ07 11211015 12059203 642,687,695,712

686

AYCHZ071 5468937 5970580 642,695,686

AYCHZ103 4628930 5140431 395,679,627,686

AYCHZMT 7315236 7754183 642,626,694,695,686

AYCMTSR1 18508183 18628695 600,630,646,682,686

AYCMTSR2 12130488 12246613 600,630,646,682,686

AYCMTSR3 10933079 11053591 646,682,686

AYCNMF31 10126020 12039971 548,593,613,618,621,

686

AYCZIP 5459579 7385832 163,197,209,686

IVMB686 N/A 2116679 686

IVMB686P N/A 16910283 686

IVMB686R N/A 20743316 686

IVMB686U N/A 9094153 686

IVMBAIL1 N/A 1830914 686

IVMBAILK N/A 7270098 686

IVMBZ05 6234409 6268459 3,1,105,123,642

686

IVMBZ05A 4046696 5002416 642,686

IVMBZ07 9672313 12290494 1,83,90,95,126

129,202,153,287,288

392,407,455,491,530

608,573,686

IVMBZ071 5738489 5956608 83,95,530,686

IVMBZ07A 6287478 6470255 72,3,83,90,95

159,249,190,257,288

295,335,356,395,501

530,608,573,686

Routine List with Checksums, continued

IVMBZ07B 5794104 7117119 501,562,651,626,683

686

IVMBZ07M 10455772 11006132 395,458,655,626,675

681,683,694,686

IVMBZ07N 9607645 9871077 395,458,626,686

IVMBZ07O 13561980 14406724 458,626,544,694,686

IVMBZMT 7066124 7521485 1,260,288,333,395

455,562,626,686

IVMD502 3237582 3261079 400,686

IVMDAJ 2453451 3367251 475,566,686

IVMDCAL 11817350 12773568 33,471,514,585,686

IVMDCAL2 13232162 15605313 23,26,395,36,686

IVMDCALP 12441494 14069789 395,36,590,655,675

686

IVMDCM01 14227905 14657065 638,686

IVMDCMLT 31835597 32215616 638,686

IVMDDOCK 6475131 6634552 686

IVMDHDA 4300954 4432123 395,686

IVMDHDA1 9249680 9321917 395,409,686

IVMDMTA1 8397028 9565848 395,600,626,686

IVMDMTA2 7690138 8166859 395,600,686

IVMDNR 2621736 2860809 26,565,686

IVMDPTA 3860357 5184122 395,626,686

IVMDPTA1 12091698 12817528 395,36,626,627,686

IVMDPTA4 6982785 8423945 409,686

IVMDPTA5 7687972 8299039 409,544,686

IVMDPTA6 9630675 9960754 409,686

IVMDPTA7 12290506 12662886 409,686

IVMDPTA8 10858816 11442188 409,686

IVMDRFS 1959781 2160713 26,686

IVMDRO2 10620643 11527651 36,686

IVMDZ051 8216359 9015719 243,642,686

IVMDZ103 4748885 5260386 395,627,686

IVMEUTL2 3512557 3551369 94,167,534,686

IVMEWL 13375515 12227735 6,8,31,252,686

IVMEWL1 N/A 3135474 686

IVMR5 4765414 4891551 3,686

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

A T T E N T I O N

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

In order to avoid missing HL7 traffic while this patch is being installed,

- 
- 

Place TaskMan in a WAIT state. Empty all HEC HL7 transmission queues before continuing.

The following scheduled options/tasks must be STOPPED or UNSCHEDULED in TaskMan before installation of Patch IVMB\*2\*686:

- 
- 
- 
- 
- 
- 
- 
- 
- 

SEND BATCH Z05S TO SITES FOR RECORD UPDATE \[AYCB SEND Z05S\]SEND BATCH Z11S TO SITES FOR RECORD UPDATE \[AYCB SEND Z11S\]Resend Enrollment Correspondence \[AYCBLTR5 RESEND LETTERS\]Generate Enrollment Letter File \[AYCB FILE ENROLLMENT LETTER\]Correspondence Status Report \[AYCB CORRESPONDENCE STATUS REPORT\]Resend MKN Messages not ACK'ed \[AYCB AYCBMFK3\]Purple Heart Priority Group Change Report \[AYCEPH PRIORITY CHANGES REPORT\]NED Nightly Update Process \[AYCN NED UPDATE\]Transmit Batch Financial(ORU~Z10) Updates \[IVMD BATCH TRANSMISSIONS JOB\]

Patch IVMB\*2\*686 can be loaded with users on the system; however, it should be installed outside of normal business hours to avoid any complications resulting from users on the system. Installation will take less than 30 minutes.

1.  

Use the INSTALL/CHECK MESSAGE option on the PackMan menu. \[Note: TEXT PRINT/DISPLAY option in the PackMan menu will display the patch text only\].

2.  

From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.

3.  
1.  
2.  
3.  
4.  

From this menu, you may elect to use the following options (when prompted for INSTALL NAME, enter IVMB\*2.0\*686):Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).Verify Checksums in Transport Global - this option will allow you to ensure the integrity of the routines that are in the transport global.Print Transport Global - this option will allow you to view the components of the KIDS build.

4.  

Use the Install Package(s) option and select the package IVMB\*2.0\*686.

5.  

Respond NO when prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//”.

6.  

Respond NO when prompted “Want KIDS to INHIBIT LOGONs during the install? YES//”.

7.  

Respond YES when prompted “Want to DISABLE Scheduled options, Menu Options, and Protocols? YES//”.

8.  

When prompted to select the options you would like to place out of order, enter the following:

- 
- 
- 
- 

SEND BATCH Z05S TO SITES FOR RECORD UPDATES \[AYCB SEND Z05S\]SEND BATCH Z11S TO SITES FOR RECORD UPDATES \[AYCB SEND Z11S\]Transmit Batch Financial (ORU~Z10) Updates \[IVMD BATCH TRANSMISSIONS JOB\]Resend HL7 messages not ACK'ed \[IVMB IVMBACK3\]

9\. After the installation has completed:

1.  
2.  

Reschedule any jobs that were unscheduled prior to installing this patch.Remove TaskMan from the Wait State.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following sample installation, user responses are shown in bold.

D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: KERNEL INSTALLATION & DISTRIBU XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INstallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: INstall Package(s)

Select INSTALL NAME: IVMB\*2.0\*686 Loaded from Distribution 11/1/02@19:51:

15

=\> IVMB\*2\*686 TEST v24

This Distribution was loaded on Nov 01, 2002@19:51:15 with header of

IVMB\*2\*686 TEST v24

It consisted of the following Install(s):

IVMB\*2.0\*686

Checking Install for Package IVMB\*2.0\*686

Install Questions for IVMB\*2.0\*686

Incoming Files:

300.11 VETERANS ID & VERIFICATION ACCESS (Partial Definition)

> **NOTE:** You already have the 'VETERANS ID & VERIFICATION ACCESS' File.

300.12 IVM MASTER CLIENT (Partial Definition)

> **NOTE:** You already have the 'IVM MASTER CLIENT' File.

300.13 IVM CLIENT INCOME (Partial Definition)

> **NOTE:** You already have the 'IVM CLIENT INCOME' File.

300.132 ENROLLMENT (Partial Definition)

> **NOTE:** You already have the 'ENROLLMENT' File.

300.9 IVM COUNTY CODES (Partial Definition)

> **NOTE:** You already have the 'IVM COUNTY CODES' File.

301.1 DCD FINANCIAL/INCOME TEST DATA (Partial Definition)

> **NOTE:** You already have the 'DCD FINANCIAL/INCOME TEST DATA ' File.

742024 PRIORITIZATION RULES (including data)

> **NOTE:** You already have the 'PRIORITIZATION RULES' File.

I will OVERWRITE your data with mine.

742060 ENROLLMENT GROUP THRESHOLD (Partial Definition)

> **NOTE:** You already have the 'ENROLLMENT GROUP THRESHOLD' File.

742070 HEC PARAMETER (Partial Definition)

> **NOTE:** You already have the 'HEC PARAMETER' File.

742087 GMT THRESHOLDS (including data)

> **NOTE:** You already have the 'GMT THRESHOLDS' File.

I will REPLACE your data with mine.

742096 GMT MSA (including data)

> **NOTE:** You already have the 'GMT MSA' File.

I will REPLACE your data with mine.

742098 CONVERSION LETTER FILE

> **NOTE:** You already have the 'CONVERSION LETTER FILE' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<ENTER\> GENERIC INCOMING TELNET

Install Started for IVMB\*2.0\*686 :

Nov 01, 2002@19:54:16

Build Distribution Date: Nov 01, 2002

Installing Routines:

Nov 01, 2002@19:54:21

Running Pre-Install Routine: PRE^IVMB686

Installing Data Dictionaries: ...

Nov 01, 2002@19:54:26

Installing Data:

Nov 01, 2002@20:07:35

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing FORM

Installing OPTION

Nov 01, 2002@20:07:37

Running Post-Install Routine: POST^IVMB686

IVMB\*2\*686 Post Install Processor

Updating the NET WORTH CALCULATION field in the

HEC PARAMETER (#742070) file and the ENROLLMENT GROUP

THRESHOLD (#742060) file.

Updating Routine file...

Updating KIDS files...

IVMB\*2.0\*686 Installed.

Nov 01, 2002@20:08:07

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option:

# Post-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTANT

Do <u>not</u> proceed with post-installation instructions until <u>after December 31, 2002.</u>

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## GMT Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation is completed, you must queue the GMT Conversion process via TaskMan to begin on the appropriate date (on or about January 3, 2003). Do not run the conversion before January 1, 2003, or before you receive confirmation that all V*IST*A field sites have installed all patches associated with GMT.

## Initiating the Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To initiate the conversion process, invoke the one-time GMT Conversion option \[IVMB PATCH 686 GMT CONVERSION\]. If you opt to proceed with the conversion, the task will be queued via TaskMan to begin one hour in the future. In the following example, user responses are shown in bold.

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: IVMB PATCH 686 GMT CONVERSION

ONE-TIME GMT CONVERSION PROCESS for IVMB\*2\*686

You are about to start the GMT Conversion

process beginning with Master IEN \#1.

Do you want to continue? NO// YES

Start up GMT Conversion processing --

Request queued as Task \#6365940.

Task queued for 1/3/2003 12:36:28 am.

The conversion does not go through the IVM MASTER CLIENT File (#300.12) in one long, continuous process. The number of veteran records processed in any given run will depend upon the number of nodes contained in the AZ11 index of File \#300.11 at the time. The GMT Conversion module holds a parameter which specifies the maximum number of nodes allowed in the AZ11 index. In any conversion run, the number of records to be converted will be:

Maximum allowed index nodes minus Current number of index nodes

If this difference is 100 or more, the task will proceed with the conversion; otherwise, the task is simply re-queued to start again one hour in the future. After this limited number has been processed, the conversion task will automatically queue itself again to run again one hour in the future in order to process the next batch of records. It will queue itself again until all enrolled veterans in File \#300.12 have been processed. If the process is interrupted by a system shutdown or application error, you can restart it via the IVMB PATCH 686 GMT CONVERSION option. Once the GMT Conversion process has completed, you should either disable or delete the IVMB PATCH 686 GMTCONVERSION option.

The conversion parameter for the maximum allowable number of AZ11 nodes will be set to 25,000 when the conversion is initially tasked. It may be adjusted as needed by a user with programmer mode access. In the following example, user responses are shown in bold.

\>D MAXQ^IVMB686U

Resetting maximum number of AZ11 nodes for GMT Conversion process --

Currently this maximum is set at: 25000

Maximum entries in AZ11 xref: (1000-50000): 50000

Resetting...