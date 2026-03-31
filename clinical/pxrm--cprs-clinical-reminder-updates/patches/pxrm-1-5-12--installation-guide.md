---
title: PXRM*1.5*12 Installation Guide - Index Global
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Index Global
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 1.5
patch_id: PXRM*1.5*12
group_key: "PXRM:PXRM:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: The goal of this project is to create a new global in the Clinical Reminders namespace, ^PXRMINDX, that is an index of clinical data. Each of the packages whose data Clinical Reminders uses as a finding type is participating in this project.
audience: 
keywords: 
  - install
  - global
  - index
  - routine
  - table
  - contents
  - package
  - distribution
  - pxrm
  - installation
page_count: 0
word_count: 3027
section_count: 8
table_count: 18
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_1_5_12_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_1_5_12_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

[[![](pxrm-1-5-12-installation-guide-index-global/001.png)](http://vista.med.va.gov/)](http://vista.med.va.gov/)

Clinical RemindersIndex GlobalPXRM\*1.5\*12

INSTALLATION GUIDE

November 2004V*IST*A HSD&D

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
  - [## Getting the Software and Documentation](#getting-the-software-and-documentation)
  - [Documentation](#documentation)
- [Pre-Installation Information](#pre-installation-information)
  - [Required Software – Make sure all required VistA software is installed.Minimum Required Packages and Patches](#required-software-make-sure-all-required-vista-software-is-installedminimum-required-packages-and-patches)
  - [Patch Dependencies](#patch-dependencies)
    - [### Estimating Global Size](#estimating-global-size)
  - [## Global Placement](#global-placement)
    - [Caché/VMS Sites](#cachévms-sites)
    - [DSM Sites](#dsm-sites)
    - [Journaling](#journaling)
- [Installation Instructions](#installation-instructions)
  - [Installation Order](#installation-order)
- [Post-Installation](#post-installation)
  - [## Index Utility](#index-utility)
    - [Error Messages](#error-messages)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of this project is to create a new global in the Clinical Reminders namespace, ^PXRMINDX, that is an index of clinical data. Each of the packages whose data Clinical Reminders uses as a finding type is participating in this project.

> **NOTE:** This global will consume a large amount of disk space and requires a long time to initialize the cross-references. It is important to read the Global Size and Global Placement sections in the Pre-Installation section before installing this patch. When this patch is installed, the cross-references will begin populating the ^PXRMINDX global on all new data. A separate initialization process will populate old data.

The patches that comprise this project are:

|                                       |                        |
|---------------------------------------|------------------------|
| Package                           | Patch              |
| Clinical Reminders                    | PXRM\*1.5\*12          |
| Inpatient Pharmacy\*                  | PSJ\*5\*90             |
| Laboratory                            | LR\*5.2\*295           |
| Mental Health                         | YS\*5.01\*77           |
| Order Entry/Results Reporting (OE/RR) | OR\*3\*157             |
| Outpatient Pharmacy                   | PSO\*7\*118            |
| Patient Care Encounter (PCE)          | PX\*1.0\*119           |
| Pharmacy Data Management\*            | PSS\*1\*62, PSS\*1\*89 |
| PIMS/Scheduling                       | DG\*5.3\*478           |
| Problem List                          | GMPL\*2\*27            |
| Radiology                             | RA\*5\*33              |
| Vitals                                | GMRV\*5\*6             |

\* Due to timing considerations and special requirements, PSJ\*5\*90 and PSS\*1\*62 have been released and distributed individually. All the other builds will be distributed in a multi-package build named CLINICAL_REMINDERS_INDEX.KID.

> **NOTE:** When PX\*1.0\*119 is installed, it will create a new-style “AED” cross-reference and populate the index in the V Health Factors file. If your site has a large number of entries in this file, it can take a while – and a large amount of CPU resources – for the index to build. You will see the following messages while this is happening:

Creating V Health Factor AED cross-reference.

The installation will pause while the index is being populated.

If you have a large V Health Factor file this could take awhile.

## ## Getting the Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software for this patch is not being distributed through the National Patch Module, but is being distributed as a host file. The host file, CLINICAL_REMINDERS_INDEX.KID, contains the following KIDS builds:

> PXRM\*1.5\*12 DG\*5.3\*478 GMPL\*2.0\*27 GMRV\*5.0\*6

> LR\*5.2\*295 OR\*3.0\*157 PSO\*7.0\*118 PSS\*1.0\*89

> PX\*1.0\*119 RA\*5.0\*33 YS\*5.01\*77

## Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this Installation Guide, a Technical/Programmer’s Manual is also available. This documentation is in the form of an Adobe Acrobat file.

PXRM_1_5_12_TM.PDF Technical/Programmer’s Manual

The preferred method is to ftp the files from download.vista.med.va.gov.

This transmits the files from the first available ftp server. Sites may also elect to retrieve software directly from a specific server as follows:

OIFO FTP Address Directory

 Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

 Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

 Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> **NOTE:** Download the software in ASCII mode and the documentation in Binary mode.

The documentation can also be found on the System Design and Development Web page: (http://vista.med.va.gov/vdl/).

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Software – Make sure all required VistA software is installed.Minimum Required Packages and Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package</strong></td>
<td><strong>Minimum Version</strong></td>
</tr>
<tr class="even">
<td>Clinical Reminders</td>
<td>1.5</td>
</tr>
<tr class="odd">
<td><p>PXRM*1.5*10</p>
<p>PXRM*1.5*11</p>
<p>PXRM*1.5*20</p></td>
<td></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>8.0</td>
</tr>
<tr class="odd">
<td>Laboratory</td>
<td>5.2</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>8.0</td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting</td>
<td>3.0</td>
</tr>
<tr class="even">
<td>PSJ*5*90</td>
<td></td>
</tr>
<tr class="odd">
<td>PSS*1*62</td>
<td></td>
</tr>
<tr class="even">
<td>RPC Broker (32-bit)</td>
<td>1.1</td>
</tr>
<tr class="odd">
<td>Toolkit</td>
<td>7.3</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>22.0</td>
</tr>
<tr class="odd">
<td>DI*22*95</td>
<td></td>
</tr>
<tr class="even">
<td>DI*22*140</td>
<td></td>
</tr>
<tr class="odd">
<td>Vitals</td>
<td>5.0</td>
</tr>
</tbody>
</table>

## Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|               |                                                                       |
|---------------|-----------------------------------------------------------------------|
| PATCH     | REQUIRED BUILDS                                                   |
| PXRM\*1.5\*12 | DI\*22.0\*95, DI\*22.0\*140, PSJ\*5\*90, PXRM\*1.5\*11, PXRM\*1.5\*20 |
| DG\*5.3\*478  | DI\*22.0\*95, DI\*22.0\*140, DG\*5.3\*517, DG\*5.3\*549               |
| GMPL\*2\*27   | DI\*22.0\*95                                                          |
| GMRV\*5\*6    | GMRV\*5\*1                                                            |
| LR\*5.2\*295  | LR\*5.2\*259                                                          |
| OR\*3\*157    | OR\*3.0\*138, OR\*3.0\*190                                            |
| PSO\*7\*118   | DI\*22.0\*95, PSO\*7.0\*71,PSO\*7.0\*156                              |
| PX\*1\*119    | DI\*22.0\*95                                                          |
| RA\*5\*33     | DI\*22.0\*95                                                          |
| YS\*5.01\*77  | DI\*22.0\*95                                                          |

Routines

|             |                  |                  |
|-------------|------------------|------------------|
| Routine | Old Checksum | New Checksum |
| PXRMINDC    | N/A              | 9648430          |
| PXRMP12I    | N/A              | 252287           |
| PXRMSXRM    | N/A              | 7089208          |

> 2. Use the size calculator distributed with PXRM\*1.5\*20 to estimate the required space/resources.

### ### Estimating Global Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A utility for estimating the initial size of the index was distributed by patch PXRM\*1.5\*20. To run this utility at the programmer prompt type,

D ESTTASK^PXRMISE.

> This will start a TaskMan job that estimates the initial size of the index for each global as well as the total size. The information will be delivered in a MailMan message sent to members of the mail group defined in file \#800. The estimated sizes will be given in blocks. These are 1K blocks for DSM sites and 2K blocks for Caché sites.

> Global Size

> The size estimate is made by first estimating the number of index entries that will be created for a global and then multiplying that number by a blocks/index entry factor to give the estimated number of blocks. The estimated sizes for each global are summed to give the total estimated size.

> The blocks/index entry factors were determined using test site data, which included seven DSM sites and four Caché sites. The blocks/index entry factors used to make the estimates are listed in the following table. They are based on 2K blocks for Caché and 1K blocks for DSM.

|            |                              |                            |
|------------|------------------------------|----------------------------|
| Global | Caché blocks/index entry | DSM blocks/index entry |
| AUPNVCPT   | 0.022636608                  | 0.07300721                 |
| AUPNVXAM   | 0.02297879                   | 0.079978059                |
| AUPNVHF    | 0.024028924                  | 0.082573858                |
| AUPNVIMM   | 0.023919113                  | 0.077488311                |
| AUPNVPED   | 0.023290489                  | 0.080224754                |
| AUPNVPOV   | 0.022569777                  | 0.071967779                |
| AUPNVSK    | 0.022938475                  | 0.069942116                |
| AUPNPROB   | 0.023941427                  | 0.07777772                 |
| DGPT       | 0.034578654                  | 0.099921811                |
| GMR(120.5) | 0.01879364                   | 0.063012241                |
| LR         | 0.075656684                  | 0.163250688                |
| OR(100)    | 0.046423473                  | 0.136755671                |
| PS(55)     | 0.047974217                  | 0.138609592                |
| PSRX       | 0.044820784                  | 0.138842661                |
| RADPT      | 0.053003195                  | 0.136531655                |
| YTD(601.2) | 0.04392942                   | 0.111356128                |

The size estimate is given in blocks; for Caché they are 2K blocks and for DSM they are 1K blocks.

The most recent version of Caché allows for 8K blocks, but since this is such a recent development, we only have data from one site on how this affects the number of blocks used by the index. Although the block size is 4 times larger, the number of blocks used does not decrease by a factor of 4. The actual factors from the site are listed in the following table:

|            |                 |
|------------|-----------------|
| GLOBAL | 8K/2K ratio |
| AUPNVCPT   | 0.271785247     |
| AUPNVXAM   | 0.264406778     |
| AUPNVHF    | 0.278490736     |
| AUPNVIMM   | 0.274459581     |
| AUPNVPED   | 0.278307394     |
| AUPNVPOV   | 0.273993058     |
| AUPNVSK    | 0.233333335     |
| AUPNPROB   | 0.274497225     |
| DGPT       | 0.267342968     |
| GMR(120.5) | 0.286588517     |
| LR         | 0.260255854     |
| OR(100)    | 0.260094978     |
| PS(55)     | no data         |
| PSRX       | 0.258578069     |
| RADPT      | 0.26021053      |
| YTD(601.2) | 0.279747291     |
| Average    | 0.268139437     |

> If you are using 8K blocks to store the index global, you can multiply the predicted number of blocks by the above factors to get an estimate of the number of 8K blocks that will be used.

Preliminary SAGG data for the test sites

Tampa VAMC grew from 20207 to 21010 MB in 3 months. They have split the index global across 2 volume sets (due to the current 16 MB limit for DSM), each volume set having less than a 5% growth over the 3-month period. (However, when sites convert to Caché, the limitation on the volume set size is lifted)

The PXRM\*1.5\*20 estimates also provide the breakdown of the index global by VistA application subscript. The Lab index is the largest portion of the PXRMINDX global.

The first subscript in the index global is the application file number, therefore lending itself to easy splitting. The following file numbers are indexed:

45, 52, 55, “55NVA”, 63, 70, 100, 120.5, 601.2, 9000010.07, 9000010.11, 9000010.12, 9000010.13, 9000010.16, 9000010.18, 9000010.23, and 9000011.

## ## Global Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This global serves as an index for the clinical data in a number of packages, so it is independent of a particular package. When new data is entered into the globals being indexed, the index will grow, so it needs to be placed where it has room to grow.

Use global translation or global mapping to create a volume or data set and then place the ^PXRMINDX global, according to the instructions that are appropriate to your system, as described below.

### Caché/VMS Sites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of Information recommends placing ^PXRMINDX in its own volume set. The initial size of the Caché dataset should be based on the estimated size, plus leaving room for significant growth.

Instructions for adding a new dataset can be obtained from the Avanti Library located at <http://vaww.va.gov/custsvc/cssupp/axp/Cache_Resource.asp>

Caché 3.2 sites: Download “Adding a new dataset under Caché 32.doc.”

Caché 4.x sites: Download “Add_Dataset_VMSCache.doc.”

Once the new dataset has been created and mounted, a new entry for the PXRMINDX global will need to be added to the Global Mapping section in the Caché Configuration Manager for each running Caché configuration and activated; e.g. Configuration Manager\Namespace\\ VAH\Global Mapping.

> **NOTE:** For Caché/VMS sites, you will need to update each running Caché configuration in the Cluster. It is IMPORTANT that each Caché configuration be updated; otherwise, unpredictable results can occur.

After the Global Mapping has been updated, create the PXRMINDX global:

1\) Log into the VAH namespace

2\) From the programmer mode prompt, issue the following command:

S ^PXRMINDX=""

It is highly recommended to perform the Caché steps without users on the system and PRIOR to the installation of the CLINICAL_REMINDERS_INDEX.KID build.

### DSM Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of Information recommends placing ^PXRMINDX in its own volume set. The first volume, which is reserved for the DSM internal indexes, should be set at 2 GB instead of the usual 0.5 GB. The maximum supported size is 16 GB per volume set, so if the sizing tools estimate that the index global is going to be over 14 GB, then it should be split to begin with. You should also take into consideration the growth rate of the globals being indexed, when deciding whether or not to split the global. You will need to leave enough room to accommodate the growth of the index global.

Use %GLOMAN in the Volume to set the global.

Translation Table Information

|            |          |                                                            |             |                |
|------------|----------|------------------------------------------------------------|-------------|----------------|
| Global | Type | Placement                                              | Journal | Protection |
| PXRMINDX   | Dynamic  | Place in a volume set large enough for this kind of growth | Recommended | RWP or D       |

### Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Historical Seeding - Disable

Once the PXRMINDX global is created, the historical seeding of the index can begin by using the options on the PXRM INDEX MANAGEMENT menu. For this historical seeding, the Office of Information recommends that journaling of ^PXRMINDX be DISABLED. During the initial creation and building of the index, journaling is not recommended because the index is not in use by the application and it can be rebuilt if necessary. In addition, there are concerns about journal files filling up with the large volume of SET commands that occur during the historical seeding of the PXRMINDX global. Due to these factors, the Office of information recommends that journaling be disabled on the PXRMINDX global until the historical index seeding is completed.

After Historical Seeding is completed - Enable

Once the options on PXRM INDEX MANAGEMENT menu are completed, the Office of Information recommends that journaling of the PXRMINDX be ENABLED. The PXRMINDX index global will grow and will become utilized by Clinical Reminders Version 2.0 application when released. If the PXRMINDX global becomes corrupted, it can be rebuilt but the amount of time needed to rebuild the index will impact users of Clinical Reminders application. It is the recommendation of the Office of Information that if the index needs to be rebuilt, it is safer and more efficient to journal the index once the initial build and historical seeding are completed.

.

If you have any questions with respect to global placement or journaling, please contact the VSTS Team by either calling the National Help Desk at (888) 596-4357 or by logging a Remedy ticket before proceeding with this installation.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Users can be on the system during the installation, but due to the length of time and amount of system resources required to build the Health Factor “AED” index, we recommend that you install this patch when the system is not busy.

## Installation Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install patches in the following order:

> A. Released patches: Install or make sure that all the prerequisite released patches have been installed.

> B. PXRM\*1.5\*12 – the multi-package build. Once all the required builds have been installed, then the multi-package build can be installed, using the instructions on the following pages.

> 2\. After downloading the host file, use the Load a Distribution option on the KIDS installation menu. When prompted to enter a host file, type in:

CLINICAL_REMINDERS_INDEX.KID

> 3\. The following routines are modified by the multi-package build:

|               |                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------|
| BUILD     | EXISTING ROUTINES                                                                                                           |
| PXRM\*1.5\*12 | None                                                                                                                            |
| DG\*5.3\*478  | None                                                                                                                            |
| GMPL\*2.0\*27 | GMPLX                                                                                                                           |
| GMRV\*5.0\*6  | None                                                                                                                            |
| LR\*5.2\*295  | LRAPDA, LRAPDSR, LRAPM, LRAPMRL, LRAPRES, LRMIEDZ, LRMIEDZ2, LRMINEW1, LRMISTF1, LRMIV, LRMIV1, LRMIV2, LRMIVER1, LROC, LRVER3A |
| OR\*3.0\*157  | ORDD100, ORDD100A, ORCSAVE2                                                                                                     |
| PSO\*7.0\*118 | PSOCSRL, PSODISPS, PSONVAR1, PSONVARP, PSONVNEW, PSOORUTL                                                                       |
| PX\*1.0\*119  | None                                                                                                                            |
| RA\*5.0\*33   | None                                                                                                                            |
| YS\*5.01\*77  | YTAPI1, YTAPI10, YTFILE                                                                                                         |

> Review your mapped set. If any of these routines are mapped, they should be removed from the mapped set at this time.

> 4\. On the KIDS menu under the INSTALLATION menu, use the following options, as desired:

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Backup a Transport Global

> 5\. On the KIDS menu under the INSTALLATION menu, use the Install Package(s) option to install the patch. Enter PXRM\*1.5\*12, when prompted for package.

> 6\. When prompted “Want KIDS to INHIBIT LOGONs during the install? YES//,” respond NO.

> 7\. When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//,” respond YES. When prompted to select the options you would like to place out of order, use the following table as a guide:

|               |                                   |
|---------------|-----------------------------------|
| Build     | Options To Place Out Of Order |
| PXRM\*1.5\*12 | None                              |
| DG\*5.3\*478  | None                              |
| GMPL\*2.0\*27 | None                              |
| GMRV\*5.0\*6  | None                              |
| LR\*5.2\*295  | None                              |
| OR\*3.0\*157  | None                              |
| PSO\*7.0\*118 | None                              |
| PSS\*1\*89    | None                              |
| PX\*1.0\*119  | None                              |
| RA\*5\*33     | RA\*                              |
| YS\*5.01\*77  | None                              |

> When prompted to select the protocols you would like to place out of order, use the following table as a guide:

|               |                                     |
|---------------|-------------------------------------|
| Build     | Protocols To Place Out Of Order |
| PXRM\*1.5\*12 | None                                |
| DG\*5.3\*478  | None                                |
| GMPL\*2.0\*27 | None                                |
| GMRV\*5.0\*6  | None                                |
| LR\*5.2\*295  | None                                |
| OR\*3.0\*157  | None                                |
| PSO\*7.0\*118 | None                                |
| PSS\*1\*89    | None                                |
| PX\*1.0\*119  | None                                |
| RA\*5\*33     | RA\*                                |
| YS\*5.01\*77  | None                                |

8\. When prompted 'Delay Install (Minutes): (0-60): 0//; respond 0.

> 9\. If any routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.

> 10\. The following init routines may be deleted once the installation has completed:

> DG53478I

> GMPLP27I

> GMV6PST I

> PXP119I

> PXRMP12I

> RA33PST

> YSP77I

> **NOTE:** When PX\*1.0\*119 is installed, it will create a new-style “AED” cross-reference and populate the index in the V Health Factors file. If your site has a large number of entries in this file, it can take a while – and a large amount of CPU resources – for the index to build. You will see the following messages while this is happening:

Creating V Health Factor AED cross-reference.

The installation will pause while the index is being populated.

If you have a large V Health Factor file this could take awhile.

  
Install Capture Example

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

DP Display Patches for a Package

LI Local Modified Routine Check

ML List Routines w/Local Mods

MM MailMan Menu ...

MP Mark routine locally modified

PU Patch Update

SUM Routine Checksum

Select Installation Option: 1 Load a Distribution

Enter a Host File: CLINICAL_REMINDERS_INDEX.KID

KIDS Distribution saved on Sep 21, 2004@08:41:51

Comment: Clinical Reminders Index build 09/21/2004

This Distribution contains Transport Globals for the following Package(s):

PXRM\*1.5\*12

DG\*5.3\*478

GMPL\*2.0\*27

GMRV\*5.0\*6

LR\*5.2\*295

OR\*3.0\*157

PSO\*7.0\*118

PSS\*1.0\*89

PX\*1.0\*119

RA\*5.0\*33

YS\*5.01\*77

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

PXRM\*1.5\*12

DG\*5.3\*478

GMPL\*2.0\*27

GMRV\*5.0\*6

LR\*5.2\*295

OR\*3.0\*157

PSO\*7.0\*118

PSS\*1.0\*89

PX\*1.0\*119

RA\*5.0\*33

YS\*5.01\*77

Use INSTALL NAME: PXRM\*1.5\*12 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

DP Display Patches for a Package

LI Local Modified Routine Check

ML List Routines w/Local Mods

MM MailMan Menu ...

MP Mark routine locally modified

PU Patch Update

SUM Routine Checksum

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: PXRM\*1.5\*12 Loaded from Distribution 9/22/04@17:14:19

=\> Clinical Reminders Index build 09/21/2004 ;Created on Sep 21, 2004@08

This Distribution was loaded on Sep 22, 2004@17:14:19 with header of

Clinical Reminders Index build 09/21/2004 ;Created on Sep 21, 2004@08:41:51

It consisted of the following Install(s):

PXRM\*1.5\*12 DG\*5.3\*478 GMPL\*2.0\*27 GMRV\*5.0\*6 LR\*5.2\*295

OR\*3.0\*157 PSO\*7.0\*118 PSS\*1.0\*89 PX\*1.0\*119 RA\*5.0\*33

YS\*5.01\*77

DEVICE: HOME// VIRTUAL CONNECTION

PACKAGE: PXRM\*1.5\*12 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

3 Routine checked, 0 failed.

PACKAGE: DG\*5.3\*478 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

9 Routine checked, 0 failed.

PACKAGE: GMPL\*2.0\*27 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

3 Routine checked, 0 failed.

PACKAGE: GMRV\*5.0\*6 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

2 Routine checked, 0 failed.

PACKAGE: LR\*5.2\*295 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

34 Routine checked, 0 failed.

PACKAGE: OR\*3.0\*157 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

4 Routine checked, 0 failed.

PACKAGE: PSO\*7.0\*118 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

10 Routine checked, 0 failed.

PACKAGE: PSS\*1.0\*89 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

2 Routine checked, 0 failed.

PACKAGE: PX\*1.0\*119 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

4 Routine checked, 0 failed.

PACKAGE: RA\*5.0\*33 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

2 Routine checked, 0 failed.

PACKAGE: YS\*5.01\*77 Sep 22, 2004 5:14 pm PAGE 1

-------------------------------------------------------------------------------

7 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

DP Display Patches for a Package

LI Local Modified Routine Check

ML List Routines w/Local Mods

MM MailMan Menu ...

MP Mark routine locally modified

PU Patch Update

SUM Routine Checksum

Select Installation Option: Install Package(s)

Select INSTALL NAME: PXRM\*1.5\*12 Loaded from Distribution 9/22/04@17:14:1

9

=\> Clinical Reminders Index build 09/21/2004 ;Created on Sep 21, 2004@08

This Distribution was loaded on Sep 22, 2004@17:14:19 with header of

Clinical Reminders Index build 09/21/2004 ;Created on Sep 21, 2004@08:41:51

It consisted of the following Install(s):

PXRM\*1.5\*12 DG\*5.3\*478 GMPL\*2.0\*27 GMRV\*5.0\*6 LR\*5.2\*295

OR\*3.0\*157 PSO\*7.0\*118 PSS\*1.0\*89 PX\*1.0\*119 RA\*5.0\*33

YS\*5.01\*77

Checking Install for Package PXRM\*1.5\*12

Install Questions for PXRM\*1.5\*12

Incoming Files:

800 CLINICAL REMINDER PARAMETERS

> **NOTE:** You already have the 'CLINICAL REMINDER PARAMETERS' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package DG\*5.3\*478

Install Questions for DG\*5.3\*478

Checking Install for Package GMPL\*2.0\*27

Install Questions for GMPL\*2.0\*27

Checking Install for Package GMRV\*5.0\*6

Install Questions for GMRV\*5.0

Checking Install for Package LR\*5.2\*295

Install Questions for LR\*5.2\*295

Checking Install for Package OR\*3.0\*157

Install Questions for OR\*3.0\*157

Checking Install for Package PSO\*7.0\*118

Install Questions for PSO\*7.0\*118

Checking Install for Package PSS\*1.0\*89

Install Questions for PSS\*1.0\*89

Checking Install for Package PX\*1.0\*119

Install Questions for PX\*1.0\*119

Incoming Files:

839.7 PCE DATA SOURCE (including data)

> **NOTE:** You already have the 'PCE DATA SOURCE' File.

I will OVERWRITE your data with mine.

Checking Install for Package RA\*5.0\*33

Install Questions for RA\*5.0\*33

Checking Install for Package YS\*5.01\*77

Install Questions for YS\*5.01\*77

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \<Enter\>

Enter options you wish to mark as 'Out Of Order': RA\*

Enter options you wish to mark as 'Out Of Order': \<Enter\>

Enter protocols you wish to mark as 'Out Of Order': RA\*

Enter protocols you wish to mark as 'Out Of Order': \<Enter\>

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\> VIRTUAL CONNECTION

+------------------------------------------------------------------------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------+------------------------------------------------------------+\|\|+------------------------------------------------------------+ 0%Complete PXRM\*1.5\*12

Install Started for PXRM\*1.5\*12 :

Sep 22, 2004@17:15:03

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:15:03

Installing Data Dictionaries:

Sep 22, 2004@17:15:04

Installing PACKAGE COMPONENTS:

Installing OPTION

Sep 22, 2004@17:15:04

Running Post-Install Routine: POST^PXRMP12I

Updating Routine file...

Updating KIDS files...

PXRM\*1.5\*12 Installed.

Sep 22, 2004@17:15:04

Install Message sent \#2644 DG\*5.3\*478

Install Started for DG\*5.3\*478 :

Sep 22, 2004@17:15:05

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:15:05

Running Post-Install Routine: CDGPTXR^DG53478I

Creating PTF ICD0 cross-references.

Creating PTF ICD9 cross-references.

Creating Hospital Location cross-references.

Updating Routine file...

Updating KIDS files...

DG\*5.3\*478 Installed.

Sep 22, 2004@17:16:29

Install Message sent \#2651 GMPL\*2.0\*27

Install Started for GMPL\*2.0\*27 :

Sep 22, 2004@17:16:30

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:31

Running Post-Install Routine: CPROB^GMPLP27I

Creating Problem List cross-reference.

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*27 Installed.

Sep 22, 2004@17:16:31

Install Message sent \#2652 GMRV\*4.0\*15

Install Started for GMRV\*5.0\*6 :

Sep 22, 2004@17:16:32

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:32

Running Post-Install Routine: ^ GMV6PST

Creating GMRV Vital Measurement cross-reference.

Updating Routine file...

Updating KIDS files...

GMRV\*5.0\*6 Installed.

Sep 22, 2004@17:16:32

Install Message sent \#2653 LR\*5.2\*295

Install Started for LR\*5.2\*295 :

Sep 22, 2004@17:16:32

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:33

Updating Routine file...

Updating KIDS files...

LR\*5.2\*295 Installed.

Sep 22, 2004@17:16:33

Install Message sent \#2654 OR\*3.0\*157

Install Started for OR\*3.0\*157 :

Sep 22, 2004@17:16:34

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:35

Updating Routine file...

Updating KIDS files...

OR\*3.0\*157 Installed.

Sep 22, 2004@17:16:35

Install Message sent \#2655 PSO\*7.0\*118

Install Started for PSO\*7.0\*118 :

Sep 22, 2004@17:16:35

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:35

Running Post-Install Routine: ^PSOPOST9

25 50 75 0

Creating Prescription file cross-references...

OK!

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*118 Installed.

Sep 22, 2004@17:16:37

Install Message sent \#2656 PSS\*1.0\*89

Install Started for PSS\*1.0\*89 :

Sep 22, 2004@17:16:38

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:38

Running Post-Install Routine: POST^PSSPI89

Creating Pharmacy Patient non-VA med cross-reference.

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*89 Installed.

Sep 22, 2004@17:16:39

Install Message sent \#2657 PX\*1.0\*119

Install Started for PX\*1.0\*119 :

Sep 22, 2004@17:16:40

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:16:40

Installing Data Dictionaries:

Sep 22, 2004@17:16:40

Installing Data:

Sep 22, 2004@17:16:41

Running Post-Install Routine: CVFILE^PXP119I

Creating V file cross-references.

Creating V CPT cross-reference.

Creating V Health Factor cross-reference.

Creating V Health Factor AED cross-reference.

The installation will pause while the index is being populated.

If you have a large V Health Factor file this could take awhile.

Creating V Immunization cross-reference.

Creating V Patient Ed cross-reference.

Creating V POV cross-reference.

Creating V Skin Test cross-reference.

Creating V Exam cross-reference.

Updating Routine file...

Updating KIDS files...

PX\*1.0\*119 Installed.

Sep 22, 2004@17:17:51

Install Message sent \#2658 RA\*5.0\*33

Install Started for RA\*5.0\*33 :

Sep 22, 2004@17:17:52

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:17:52

Running Post-Install Routine: ^RA33PST

Creating RAD/NUC MED PATIENT cross-reference.

Updating Routine file...

Updating KIDS files...

RA\*5.0\*33 Installed.

Sep 22, 2004@17:17:53

Install Message sent \#2659 YS\*5.01\*77

Install Started for YS\*5.01\*77 :

Sep 22, 2004@17:17:54

Build Distribution Date: Sep 21, 2004

Installing Routines:

Sep 22, 2004@17:17:54

Running Post-Install Routine: CMH^YSP77I

Creating Mental Health cross-reference.

Updating Routine file...

Updating KIDS files...

YS\*5.01\*77 Installed.

Sep 22, 2004@17:17:55

Install Message sent \#2660

─────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

# Post-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Index Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Clinical Reminders Index Technical Guide/Programmer’s Manual, PXRM_1_5_12_TM.PDF, for information on how to build the index and for programming information.

### Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there were errors during the building of the index, a MailMan message will be created that gives details about the entries that could not be indexed. The number of entries that cannot be indexed may number in the thousands for the Prescription file and the Pharmacy Patient file.

This may be a result of bad data at the local sites or system errors. It may indicate data that’s missing in application files, and may require local site investigation and correction. The majority of the messages received at test sites have referred to old data that won’t affect reminder validity, but may affect reminder report validity (e.g., long-term retrospective ones).

If you receive these error messages, we recommend that you coordinate with local ADPACs to determine the causes and corrective actions, if necessary.

Each site needs to look at a sample of the error messages to determine if the data needs to be cleaned up or ignored.

See the Patch 12 Technical Manual (PXRM_1_5_12_TM.pdf) for instructions on how to set up and manage the error messages, as well as examples of error messages, and recommended actions.