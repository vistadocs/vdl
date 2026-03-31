---
title: VistA Imaging System Storage Utilities User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: VistA Imaging System Storage Utilities
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: "> This manual explains how to use the utilities in VistA Imaging that concern storage architecture. The following utilities are briefly described and are detailed in separate chapters:"
audience: 
keywords: 
  - table
  - vista
  - class
  - contents
  - strong
  - magkat
  - files
  - platter
  - image
  - imaging
page_count: 0
word_count: 12143
section_count: 31
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 2
revision_newest: 4/21/11
revision_oldest: 11/1/10
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_storage_utilities_user_manual_f.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_storage_utilities_user_manual_f.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-system-storage-utilities-user-manual/001.png)

VistA Imaging System Storage Utilities User Manual

# April 2011 — Revision 2 MAG\*3.0\*98


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [April 2011 — Revision 2 MAG\3.0\98](#april-2011-revision-2-mag3098)
- [Preface](#preface)
  - [VHA Directive](#vha-directive)
  - [Terms of Use](#terms-of-use)
  - [Conventions](#conventions)
  - [Related Manuals](#related-manuals)
  - [Getting Help](#getting-help)
- [Introduction](#introduction)
  - [MagDexter](#magdexter)
  - [MagKat](#magkat)
  - [MagUtility](#magutility)
- [Using MagDexter to Create Platter Reports](#using-magdexter-to-create-platter-reports)
  - [Requirements](#requirements)
  - [How MagDexter Works](#how-magdexter-works)
  - [Setting Up MagDexter](#setting-up-magdexter)
  - [Creating MagDexter Platter Reports and Viewing the Log](#creating-magdexter-platter-reports-and-viewing-the-log)
- [Using MagKat to Update the IMAGE File (#2005)](#using-magkat-to-update-the-image-file-2005)
  - [Introduction](#introduction-1)
  - [Requirements](#requirements-1)
  - [How MagKat Works](#how-magkat-works)
  - [Installing MagKat](#installing-magkat)
  - [Starting MagKat](#starting-magkat)
  - [Processing RAID (Magnetic) Shares](#processing-raid-magnetic-shares)
  - [Processing Jukebox Platters](#processing-jukebox-platters)
  - [Re-Scanning Using Ad Hoc Processing](#re-scanning-using-ad-hoc-processing)
  - [Viewing MagKat Platter Processing Reports and Logs](#viewing-magkat-platter-processing-reports-and-logs)
- [Using MagUtility to Maintain the VistA Database](#using-magutility-to-maintain-the-vista-database)
  - [Introduction](#introduction-2)
  - [Requirements](#requirements-2)
  - [How MagUtility Works](#how-magutility-works)
  - [Starting and Exiting MagUtility](#starting-and-exiting-magutility)
  - [Running the Orphan Files Process](#running-the-orphan-files-process)
  - [Running the Offline Jukebox Images Process](#running-the-offline-jukebox-images-process)
  - [Running the Network Location Cleanup Process](#running-the-network-location-cleanup-process)
  - [Running the Storage Copy Process](#running-the-storage-copy-process)
  - [Viewing and Customizing MagUtility Logs](#viewing-and-customizing-magutility-logs)
- [Glossary](#glossary)
- [Index](#index)
    - [A](#a)
    - [B](#b)
    - [C](#c)
    - [D](#d)
    - [H](#h)
    - [I](#i)
    - [J](#j)
    - [L](#l)
    - [M](#m)
    - [N](#n)
    - [O](#o)
    - [P](#p)
    - [R](#r)
    - [S](#s)
    - [T](#t)
    - [U](#u)
    - [W](#w)
> Department of Veterans Affairs Office of Enterprise Development Health Provider Systems
> Storage Utilities User Manual VistA Imaging MAG\*3.0\*98 April 2011
> Property of the US Government
> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development office.
> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.
> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.
> VistA Imaging Office of Enterprise Development Department of Veterans Affairs
> Internet: <span class="mark">REDACTED</span>
> VA intranet: <span class="mark">REDACTED</span>
> Revision History
| Date    | Rev | Notes                                                                                                                                                              |
|---------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11/1/10 | 1   | Document created for MAG\*3.0\*98. Final work product review completed. Final for release.                                                                         |
| 4/21/11 | 2   | Updated for P39 release. Preface text corrected, refs to the Verifier Manual changed to Verifier chapter in the BP User Manual. <span class="mark">REDACTED</span> |
|         |     |                                                                                                                                                                    |
|         |     |                                                                                                                                                                    |
|         |     |                                                                                                                                                                    |
|         |     |                                                                                                                                                                    |
|         |     |                                                                                                                                                                    |
|         |     |                                                                                                                                                                    |
> Contents
Getting .NET 6
Installing MagDexter 6
Preparing to Use MagDexter 7
Reviewing Jukebox Shares 7
Preparing the Jukebox 8
[Creating MagDexter Platter Reports and Viewing the Log 8](#creating-magdexter-platter-reports-and-viewing-the-log)
Sample Platter Summary Report 10
Sample Platter Detail Report 11
Sample MagDexter Log File 11
[Using MagKat to Update the IMAGE File (#2005) 13](#using-magkat-to-update-the-image-file-2005)
[Introduction 13](#introduction-1)
MagKat Benefits 13
VA-DoD Image Sharing 13
VistARad 13
Description of the VistA Imaging MagKat Window 17
[Processing RAID (Magnetic) Shares 19](#processing-raid-magnetic-shares)
Processing Text Files for Single and Multiple Sites 19
Re-Processing Text Files on the RAID 20
Skipping RAID Processing 20
[Processing Jukebox Platters 21](#processing-jukebox-platters)
Conditions for Skipping Jukebox Processing 21
Verifying Conditions before Jukebox Processing 21
Platter Processing 22
Scanning 22
Acting on the Platter Status 24
Forcing Platters into the “Processed” Status 26
[Re-Scanning Using Ad Hoc Processing 26](#re-scanning-using-ad-hoc-processing)
Re-Scanning Skipped Files 26
Stopping and Resuming Processing 27
[Viewing MagKat Platter Processing Reports and Logs 27](#viewing-magkat-platter-processing-reports-and-logs)
Platter Processing Reports 27
Sample MagKat Platter Report 28
MagKat Log Files 29
Sample MagKatError.log File 29
Sample MagKatImageComplete.log File 29
Sample MagKatInfo.log File 30
For Administrators 31
For Servers 31
For VistA 32
[How MagUtility Works 32](#how-magutility-works)
Orphan Files Process 32
Pointers and Pointer Selection Logic 33
Processing Logic Used in an Orphan Files Check 33
Offline Jukebox Images Process 35
Network Location Cleanup 35
Storage Copy Process 35
[Starting and Exiting MagUtility 35](#starting-and-exiting-magutility)
Starting MagUtility 35
Description of the MagUtility Window 36
Exiting MagUtility 37
[Running the Orphan Files Process 37](#running-the-orphan-files-process)
Prerequisite for Running an Orphan Files Check 37
Running an Orphan Files Check 37
Troubleshooting the Orphan Files Process 39
[Running the Offline Jukebox Images Process 42](#running-the-offline-jukebox-images-process)
Marking Images Offline 42
Marking Images Online 44
Troubleshooting the Offline Jukebox Images Process 45
[Running the Network Location Cleanup Process 46](#running-the-network-location-cleanup-process)
Removing RAID or Jukebox Network Locations 46
Troubleshooting the Network Location Cleanup Process 47
[Running the Storage Copy Process 48](#running-the-storage-copy-process)
Preparing to Use Storage Copy 48
Starting the Storage Copy Process 49
Pausing, Resuming, or Canceling the Storage Copy Process 53
Running After Hours 53
Troubleshooting the Storage Copy Process 53
[Viewing and Customizing MagUtility Logs 55](#viewing-and-customizing-magutility-logs)
Opening a Log File 55
Log File Format 56
Sample MagUtilityInfo.log File 56
Sample MagUtilityDebug.log File 56
Retaining and Deleting Log Files 57
Re-Configuring the Size and Retention Limit 57
[Glossary 59](#glossary)
[Index 63](#index)

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VHA Directive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VHA Directive 2001-045 required that VA medical centers implement a document imaging system by September 30, 2004. This directive stated that medical facilities must scan certain clinical documents to make them part of a patient’s electronic medical record. The directive specifically mentioned advance directives and consent forms.

> To comply with this directive and support the goal to make a patient’s complete medical record available online, the following types of documents should be maintained:

- Consent forms and other documents with “wet” signatures of patients, practitioners, or other personnel
- Advance Directives
- Results/reports from medical procedures that are not acquired directly from the instrument or entered in the VistA system
- Means Tests
- Outside medical reports

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In compliance with Food and Drug Administration (FDA) and VA policies, authorization to use this software is contingent on the execution of a Site Agreement between the VistA Imaging Office of Enterprise Development (OED) group and the site where this software is installed.

> ![](vista-imaging-system-storage-utilities-user-manual/002.png)![](vista-imaging-system-storage-utilities-user-manual/003.png)In addition to any restrictions noted in the Site Agreement, the following restrictions apply.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>The FDA classifies VistA Imaging as a medical device. Unauthorized modifications to VistA Imaging will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual uses the following conventions:

- Change bars in margins indicate content added or updated since the last revision.
- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate menu choices. For example: “Click File \| Open” means: “Click the File menu, and then click the Open option.”
- Keyboard key names are shown in bold and in brackets.
- Sample output is shown in monospace.
- When this document is used online, hyperlinks are indicated by blue text.
- Useful or supplementary information is shown in a Tip.
- Important or required information is shown in a Note.
- Critical information is indicated by: ![](vista-imaging-system-storage-utilities-user-manual/004.png)

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additional information about VistA Imaging can be found in the following documents:

- VistA Imaging System Installation Guide at <span class="mark">REDACTED</span>
- VistA Imaging System User Manual at

<span class="mark">REDACTED</span>

- VistA Imaging System Technical Manual at <span class="mark">REDACTED</span>

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you encounter any problems with the utilities in VistA Imaging that concern storage architecture*,* contact your Imaging Coordinator for assistance. <span class="mark">REDACTED</span>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual explains how to use the utilities in VistA Imaging that concern storage architecture. The following utilities are briefly described and are detailed in separate chapters:

## MagDexter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagDexter is used to create summary and detail platter reports. The reports contain platter information such as the name, serial number, status of each jukebox platter.

## MagKat

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagKat is used to backfill specific fields in the IMAGE file (#2005) in the VistA database using data from the text files associated with images.

## MagUtility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagUtility is used to report and resolve problems with “orphan” files, delete obsolete or incorrect entries from the NETWORK LOCATION file (#2005.2), update the VistA database with image information, and copy images and text files.

# Using MagDexter to Create Platter Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MagDexter utility generates reports about all platters (media) and all files on a jukebox.

> Note: MagDexter Platter Detail reports are a required component for running MagKat (the database backfill tool included with Patch 98) against a jukebox. MagDexter reports may also be useful in planning for jukebox migration.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MagDexter must be installed and run on the Windows 2000-based or 2003-based server hosting the EMC DiskXtender version 4.x or 5.x software. While MagDexter should work with later versions of DiskXtender, it is certified only for use with version 4.x or

> 5.x at this time.

- .NET Framework 2.0 is required to install and run MagDexter. Instructions for downloading .NET are included in this document.
- Users installing and running MagDexter must have Windows Administrator privileges. VistA credentials are not needed.
- Sufficient space must be available for the storage of MagDexter reports. While reports sizes vary, for planning purposes a size of 4 megabytes per report (with one report generated for each side of a scanned platter) should be assumed. Reports can be stored locally or in a folder on a mapped drive. The storage location can be specified and changed in MagDexter as needed.

> Important: Reports <u>should not</u> be saved to a DX drive or root folder of any drive.

- Compacting a jukebox platter during or after MagDexter execution invalidates the results of the Platter Detail reports. For this reason, disable compaction for any platters that need to be processed by MagDexter and MagKat. Compaction can be resumed after MagKat is run successfully.

## How MagDexter Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you start MagDexter, it automatically detects any jukebox shares (i.e., DiskXtender extended drives) on the local server.

> When you run MagDexter, it creates the following reports:

- Platter Summary report that lists the name, serial number, and status (online, offline, or offline error) of every platter containing VistA Imaging files that the jukebox manages. The status of a platter comes from the information that DiskXtender maintains for the platter in the Windows registry.
- Platter Detail report for each jukebox platter. These reports are created by traversing through all the NTFS file headers on every network share mapped to the DiskXtender (DX) drive. MagDexter checks each file header to determine which platter the file resides on, and then writes the filename as a UNC path to the appropriate Platter Detail report file. This process does not cause a load of the file from the jukebox platter to the DX drive.

> The amount of time needed to scan jukebox shares varies significantly based on server speed and capacity. For initial estimations, a good rule of thumb is to plan on a scanning rate of 75,000 to

> 1.1 million files per hour.

## Setting Up MagDexter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Getting .NET

> MagDexter requires the .NET Framework 2.0. If it is not already installed, you can get .NET 2.0 as a part of the .NET 3.5 Family Update (KB951847) at [<u>http://update.microsoft.com/</u>.](http://update.microsoft.com/) Choose Custom, and under optional patches, download and install the entry shown below.

![](vista-imaging-system-storage-utilities-user-manual/005.png)

> Installing MagDexter

1.  Log on as an account with privileges to the server that hosts the EMC DiskXtender 4.x or 5.x software.
2.  Copy the MagDexterSetup.msi file (distributed with test Patch 98) to a local drive location.
3.  Double-click the file to start the wizard, and after the Welcome dialog box is displayed, click

#### Next.

4.  Accept the default installation settings and then click Next twice.
5.  After the installation is finished, click Close to exit the wizard.

> Preparing to Use MagDexter

> Before using MagDexter, you need to:

- Review which jukebox shares to scan
- Prepare the jukebox itself

> <span id="_bookmark0" class="anchor"></span>Reviewing JukeboxShares

> Depending on how data is stored on your site’s jukebox, some minor differences affect how MagDexter should be used. You should determine which of the following conditions applies to your jukebox.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>If Your Jukebox</strong></th>
<th><strong>Then</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Stores data from only one site</td>
<td><p>MagDexter identifies which shares need to be scanned at startup. No additional action is needed.</p>
<p>You can use MagDexter to scan all shares in a single pass, or scan each share separately. When you scan shares separately, save all reports into the same folder.</p></td>
</tr>
<tr class="even">
<td>Stores images from multiple sites, where each site is assigned specific shares</td>
<td><p>You have to scan each share separately.</p>
<p>Before you use MagDexter to scan the shares, determine which site’s images are stored on each jukebox share identified by MagDexter. Then set up a report output folder for each site. When you prepare to scan each share, select the appropriate output folder based on the site.</p></td>
</tr>
<tr class="odd">
<td>Stores data from multiple sites, and co-mingles data from different sites on one or more shares</td>
<td><p>You have to scan each share separately.</p>
<p>Before you use MagDexter to scan the shares, determine which site’s images are stored on each jukebox share identified by MagDexter. Then set up a report output folder for each site.</p>
<p>When you prepare to scan each share, select the appropriate output folder based on the site. Shares that have images from multiple sites need to be scanned multiple times, with each report going into the appropriate output folder.</p></td>
</tr>
</tbody>
</table>

> Preparing the Jukebox

1.  Suspend platter compactions.

> You can resume compaction after MagKat runs successfully.

2.  Important: Use DiskXtender to ensure that all platters are online.

> This step saves time later on by ensuring that MagKat processes platters automatically (rather than manually).

> The platter color code legend is:

- Black = online platters
- Olive green = offline platters (need attention).
- Red = platters in an error state (need attention).

## Creating MagDexter Platter Reports and Viewing the Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Windows Start \| Programs menu, choose VistA Imaging Programs \| MagDexter. The MagDexter window displays a list of network file shares on the DX drive on the server.

![](vista-imaging-system-storage-utilities-user-manual/006.png)

2.  In the MagDexter window, click Select Output Folder to select the folder where you want to save the platter reports.

> <u>Guidelines on Selecting a Save Location</u>

- Important: Avoid saving the reports to a DX drive or root folder of any drive.
- Reports can be saved to a mapped drive, but a mapped drive increases the time needed to scan platters.
- In most cases, all reports can be stored in a single folder. However, if your jukebox stores data from multiple sites, and if the data is segregated by share, create site- specific output folders for the reports. See [*Reviewing Jukebox Shares*](#_bookmark0) for details.
- Because un-hashed network shares contain a large number of files in a single folder, MagDexter may seem to hang and take longer to process while it checks the folder to build the list of files for processing. Once the large file list is assembled, MagDexter starts processing the share.
3.  Use the Select network share box to select which shares to scan. <u>Guidelines on Selecting Shares</u>
    - Select All network shares if the jukebox is used to store data from only one site, or if images from different sites are co-mingled on one or more jukebox shares.
    - If MagDexter detects that two network shares are mapped to the same directory, the All network shares option is not available. To avoid needless processing by MagDexter and MagKat, determine which share should be processed and select only that share as described below.
    - Select a specific share if you want to scan only one share at a time. See [*Reviewing Jukebox Shares*](#_bookmark0) for details.

![](vista-imaging-system-storage-utilities-user-manual/007.png)

4.  Click Create Platter Reports.
    - MagDexter generates a Platter Summary report first. (This report lists all shares, even if only one share was selected in the previous step.)
    - Then MagDexter examines each file on the selected share or shares to determine which platter is storing the file. For each file, MagDexter writes the file name as a fully qualified UNC path to the appropriate Platter Detail report.
    - As MagDexter runs, it displays the name of the current file (being scanned) in the lower left corner of the MagDexter window. You can select several processing options:
      - If the jukebox server is less responsive, set the Wait box to have MagDexter pause after reading each file.

> You can set the value between 0 and 5 milliseconds.

- To temporarily pause a scan, choose Help \| About MagDexter from the menu bar.

> The scan is paused as long as the About window is open.

- To cancel a scan in progress, click Cancel in the lower right corner of the MagDexter window. (This button is visible only when a scan is running.)

> Note: If you cancel a scan of a network share, the share will have to be re-scanned in its entirety, and you will be prompted to select a different output folder when you start the scan. You may want to delete all files in the output folder and re-scan all shares.

> When a scan is finished, the message Platter Reports are complete is displayed after the selected share or shares are processed.

> Sample Platter Summary Report

> All reports are tab-delimited and can be imported into Microsoft Excel. The following sample is a Platter Summary report.

![](vista-imaging-system-storage-utilities-user-manual/008.png)

> The platter statuses are:

- Online = Platter is online, and MagKat can process text files on the platter.
- Offline = Platter is offline, and MagKat cannot process the platter. Set the platter back on.
- OfflineError = Platter is offline and in an error state. Right-click the platter and select Clear Error Status from the popup menu. Process the platter. For details, see [*Acting onthe Platter Status*](#Acting_on_the_Platter_Status).

> Sample Platter Detail Report

> All reports are tab-delimited and can be imported into Microsoft Excel. For each platter identified, MagDexter generates a separate Platter Detail report listing the files on that platter.

> The following example shows a directory of report files. The file name of each Platter Detail report includes the name and serial number of the platter.

![](vista-imaging-system-storage-utilities-user-manual/009.png)

> If you double-click a report, the files contained on the platter are listed as shown in the following example. Each listing is a fully qualified UNC path.

![](vista-imaging-system-storage-utilities-user-manual/010.png)

> Sample MagDexter Log File

> MagDexter’s operations are logged in \Program Files\Vista\Imaging\MagDexter

> \MagDexter Log.txt, as shown in the following example.

![](vista-imaging-system-storage-utilities-user-manual/011.png)

> Each time that MagDexter runs, it adds new entries to the listing. This file is deleted only if you manually do so.

# Using MagKat to Update the IMAGE File (#2005)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagKat is used to backfill specific fields in the IMAGE file (#2005) in the VistA database using data from the text files associated with images.

> MagKat Benefits

> By transferring data from the text files of older images into the appropriate fields in the IMAGE file (#2005) on VistA, MagKat addresses discrepancies that may appear in displaying older images. The benefits affect image sharing and VistARad as described in the following sections.

> *VA-DoD Image Sharing*

> At VA sites that intend to share pre-Patch 50 images with DoD facilities, running MagKat ensures that the multi-series exams are displayed properly.

> Note: In images acquired before the installation of Patch 50 (whose compliance date was August 13 2006), the DICOM series UID (unique identifier) was stored in the image-associated text files only, not in the IMAGE file (#2005).

> If these images are sent as-is to a DoD facility, the series UID data will be absent. On DoD’s display system, all the images in the study are grouped into one series, regardless of the number of series that actually existed in the study.

> After using MagKat, images copied to a DoD facility using the VIX will contain the data needed by the DOD display system to properly group images into series.

> *VistARad*

> Executing MagKat also lets sites that use VistARad take advantage of improved date reporting for exams acquired before the installation of Imaging Patch 54. For details about how improved date reporting affects VistARad, see the Patch 76 Patch Description.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The server where MagKat is installed must have access to the VistA system, and at least 10 gigabytes of free disk space (logs and reports generated by MagKat can become quite large).
- The VistA account used to execute MagKat must be assigned the MAG DOD FIX security key and the SET CONTEXT FOR MAGKAT RPCS \[MAGKAT\] secondary menu option, both introduced in Patch 98.
- Any shares (RAID and jukebox) that MagKat scans must be online and accessible to the system where MagKat is installed. (MagKat can scan “read-only” shares.)
- To populate IMAGE file (#2005) data for jukebox images, MagKat requires reports that the MagDexter utility produces. Refer to [*Generating Platter Reports*](#_bookmark1) for details.
- If you are populating fields in Image file \#2005 for jukebox images, platter compaction activity (which has to be suspended before generating MagDexter reports) must be suspended until MagKat processing is finished also. You can resume compaction after MagKat runs successfully.
- The VistA system must be accessible to MagKat when MagKat is running a scan. If the VistA connection is lost, you can stop MagKat and then resume the scan where it left off.

## How MagKat Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagKat runs in multiple passes. The process involves the following stages:

1.  MagKat processes text files for images stored on the RAID (Redundant Array of Independent Disks).
2.  MagKat then uses reports that the MagDexter utility generates and processes the text files stored on jukebox platters.

> Note: At sites that use non-DiskXtender jukebox configurations, MagKat should still be run for files on the RAID.

> Optionally, you can run MagKat on an ad hoc basis against specific IEN (Internal Entry Number) ranges in the IMAGE file (#2005).

3.  As each pass is executed, MagKat checks specific fields in the appropriate IMAGE file (#2005) entry against the equivalent parts of each text file associated with its image.
4.  If any of the IMAGE file (#2005) fields listed below are empty, MagKat populates the fields using data from the text file (if data is available).

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Text File: Fields Checked</strong></th>
<th><p><strong>IMAGE File:</strong></p>
<p><strong>Fields Populated</strong></p>
<p><strong>(if values are absent)</strong></p></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Study Instance UID (0020,000D)</td>
<td>PACS UID (#2005,60)</td>
<td>Unique identifier for the study</td>
</tr>
<tr class="even">
<td>Series Instance UID (0020,000E)</td>
<td>Series UID (#2005,253)</td>
<td>Unique identifier for the series</td>
</tr>
<tr class="odd">
<td>Series Number (0020,0011)</td>
<td>DICOM Series Num (#2005.04,1)</td>
<td>Series number within the study</td>
</tr>
<tr class="even">
<td>Instance Number (0020,0013)</td>
<td>DICOM Image Num (#2005.04,2)</td>
<td>Image number within the series</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Text File: Fields Checked</strong></th>
<th><p><strong>IMAGE File:</strong></p>
<p><strong>Fields Populated</strong></p>
<p><strong>(if values are absent)</strong></p></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SOP Instance UID (0008,0018)</td>
<td>PACS UID (#2005,60)</td>
<td>Unique identifier for the image</td>
</tr>
<tr class="even">
<td><p>Image (Content) Date (0008,0023),</p>
<p>Acquisition Date (0008,0022), Instance Creation Date (0008,0012)</p></td>
<td>Creation Date (#2005,110)</td>
<td>Date when the image was acquired. Text file values are checked in the order that they are listed in the left column. The first value found is used.</td>
</tr>
<tr class="odd">
<td><p>Image (Content) Time (0008,0033),</p>
<p>Acquisition Time (0008,0032), Instance Creation Time (0008,0013)</p></td>
<td>Creation Date (#2005,110)</td>
<td>Time when the image was acquired. Text file values are checked in the order that they are listed in the left column. The first value found is used.</td>
</tr>
</tbody>
</table>

> Note: IMAGE file (#2005) fields that already have values are not changed.

## Installing MagKat

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log on with an account that has administrator privileges to the server where you plan to install MagKat (typically on an Imaging file server or on the VIX server).
2.  Copy MagKatInstall.exe (distributed with Patch 98) to a local drive.
3.  Double-click the file to start the InstallShield Wizard.

> Note: You can install new versions of MagKat over old versions without any additional action.

4.  After the Welcome dialog box opens, click Next and then Install.

> There are no configurable installation options. The installation typically takes less than 30 seconds.

5.  When the installation is finished, click Finish.
6.  If MagKat is newly installed, perform the followings steps to configure MagKat’s connection to VistA (via the VA Kernel RPC Broker):
    1.  Start MagKat (Start \| All Programs \| VistA Imaging \| MagKat).
    2.  When the MagKat window opens, select File \| Log In. The Enter Server Configuration dialog box opens.
    3.  Enter the VistA Server hostname and the port number that MagKat will use to connect. Then click OK.
7.  Optionally, start MagKat as described below to ensure that the VistA account used to run MagKat has the proper credentials.

> Note: When MagKat needs to connect to a different VistA system, you can choose

> File \| Select VistA Server to change the VistA hostname and port number.

## Starting MagKat

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open Start \| All Programs \| VistA Imaging \| MagKat on the system where MagKat is installed.
2.  After the MagKat window opens, select File \| Log In.
3.  Log into a VistA account that has the following security settings:
    - The MAG DOD FIX security key (introduced in Patch 98)
    - The SET CONTEXT FOR MAGKAT RPCS \[MAGKAT\] secondary menu option
5.  If the site is multi-divisional, select a division when prompted. The VistA Imaging MagKat window opens.

> Note: You can exit MagKat by choosing File \| Exit from the menu bar.

> Description of the VistA Imaging MagKat Window

> The title bar displays the server name and user name, as shown in this example.

![](vista-imaging-system-storage-utilities-user-manual/012.png)

> <u>Menu Bar</u>

- File menu for logging in and logging out, and selecting a server

![](vista-imaging-system-storage-utilities-user-manual/013.png)

- Process menu for magnetic, jukebox, and ad hoc processing

![](vista-imaging-system-storage-utilities-user-manual/014.png)![](vista-imaging-system-storage-utilities-user-manual/015.png)![](vista-imaging-system-storage-utilities-user-manual/016.png)

- Throttle menu for increasing and decreasing processing speed

![](vista-imaging-system-storage-utilities-user-manual/017.png)

> <u>Tabs</u>

> The tabs enable you to perform three different types of scans: Magnetic, Jukebox, and Ad Hoc Processing.

> Note: The tabs are an alternative to using the commands on the Processing menu. <u>Direction Box</u>

- Forwards – MagKat processes files from the lowest IEN to the highest
- Backwards - MagKat processes files from the highest IEN to the lowest. When you select the Magnetic tab, you should select this direction to maximize file processing on the RAID.

> <u>Processing Buttons</u>

> The processing buttons start the scan. They are also an alternative to using the commands on the Processing menu:

- Process Sequentially – This option is selected by default setting on the initial run.
- Stop Processing – All processing is suspended. When you click the Process Sequentially button, scanning begins after the last processed IEN.
- Restart from Beginning – Select this option when a run is aborted and you want to reset the current processing parameters to the initial settings.

> <u>Process Status Box</u>

> When you start the scan, the Process Status box in the lower part of the window shows:

- The IEN (internal entry number) of the text file being processed
- Status messages as they occur (These are written to the log file.)
- The amount of time used to process each text file, calculated by averaging the processing time of the five most recently processed text files
- A count of any errors that occurred in the 50 most recently processed text files (All errors are logged.)

> As a scan runs, the System Impact Throttle box controls the speed of the scan:

- If you set the throttle to Fast, MagKat processes each text file without pausing.
- If you set the throttle to Slow, MagKat pauses 1.5 seconds after processing each text file.

## Processing RAID (Magnetic) Shares

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Processing text files is a two-stage process. MagKat processes text files first on RAID storage and second, on the jukebox (covered in the next section).

> RAID storage is processed differently depending on site configuration.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>If your site stores:</strong></th>
<th><strong>Then</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Images from your local site only</td>
<td>Use MagKat to process all RAID images.</td>
</tr>
<tr class="even">
<td>Images from multiple sites (namespaces)</td>
<td><p>Only one site needs to scan the RAID. Ideally, the site where the VistA database is physically located should be the site that scans the RAID. One of the log files generated by this scan then needs to be sent to the other sites that store images on the RAID.</p>
<p>On receipt of the log file, other sites that store images on the RAID should skip RAID processing as described in <em><a href="#_bookmark4">Skipping RAID</a></em> <a href="#_bookmark4"><em>Processing</em>.</a></p></td>
</tr>
</tbody>
</table>

> Processing Text Files for Single and Multiple Sites

1.  Start MagKat and select the Magnetic tab.
2.  Set the scanning direction by clicking either the Forwards or Backwards option. (Backwards is recommended on the initial scan because the images will be processed more efficiently.)
3.  Click Process Sequentially.
4.  As MagKat runs, periodically check the MagKat window.
    - If the Recent Error Count area near the bottom of the window indicates numerous errors (i.e., shows a count of 50 for a period of time), pause the scan and review MagKat’s log before proceeding.
    - If the system response becomes sluggish, use the System Impact Throttle at the bottom of the window to limit processing speed and thus give other processes more time to run.
5.  MagKat stops after all text files on the RAID are processed, and displays a summary of processing results containing counts for:
    - Processed Files that were updated, as described in the section [*Starting MagKat*](#_bookmark2)
    - Skipped Jukebox Files for processing when MagKat scans the jukebox
    - Failed Files that could not be processed
6.  If the count of failed files exceeds 0.5% of the total files processed (more than 5000 per 1,000,000), review the MagKatError.log file stored in C:\Program Files\Vista \Imaging\\ MagKat\logs.
7.  If images from multiple sites are stored on the local RAID, run MagKat for each of these sites.

> Note: If those sites have their own local jukeboxes, send them a copy of the C:\Program Files\Vista\Imaging\MagKat\logs\\ xxx_MagKatImageComplete.log file, where xxx is the station number of the site that scanned the RAID.

> Re-Processing Text Fileson the RAID

> If needed, all text files on the RAID can be rescanned.

1.  Start MagKat and select the Magnetic tab.
2.  If you want, set the scanning direction for Backwards.
3.  Click Restart From Beginning.
4.  Confirm that you want to rescan all text files by clicking Yes when prompted.

> Note: As mentioned above, if the sites have their own jukeboxes but store images on the local RAID, send an updated xxx_MagKatImageComplete.log file to those sites.

> <span id="_bookmark4" class="anchor"></span>Skipping RAID Processing

> Note: Use these steps only if your site has a local jukebox but stores images on a RAID share at another site (such as in a consolidated site configuration).

1.  Get a copy of the xxx_MagKatImageComplete.log file from the site that processed the RAID (where xxx is the station number of the site that scanned the RAID).
2.  Put a copy of the log file in C:\Program Files\Vista\Imaging\MagKat\logs on the local server where MagKat is installed.
3.  Log into MagKat.
4.  On the main menu, choose Process \| Allow Jukebox Processing without Magnetic.
5.  Verify that you have met the terms of the confirmation message displayed, and then click

> Yes.

6.  In the MagKat window, verify that the Jukebox tab is enabled.

## Processing Jukebox Platters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After all text files on the RAID are scanned, you can use MagKat to process text files stored on jukebox platters. All online platters should be processed at one time, singly, or in manually selected groups.

> Conditions forSkipping Jukebox Processing

- If all images are stored on the RAID as well as the jukebox, and you have never run a purge on the RAID, you can skip jukebox processing.
- If your site does not have a local jukebox, you can skip jukebox processing.

> Verifying Conditions beforeJukebox Processing

> Before using MagKat to process the contents of a jukebox, verify the following:

- Verify that RAID (magnetic) processing is completed.

> Note: Some sites process their own RAIDs. Other sites that use a shared RAID use the log files from a site that processed the shared RAID. For details, see the introduction under section [*Processing RAID (Magnetic) Shares*.](#processing-raid-magnetic-shares)

- Verify that the following files (generated using the MagDexter utility), are available in C:\Program Files\Vista\Imaging\MagKat\Jukebox:
  - Platter Detail Report \<platter ID\>.txt (one file per platter)
  - Platter Summary Report.txt

> Note: If the files above are added to the \Jukebox folder while the MagKat window is open, exit and restart MagKat before processing any platters.

- Verify that platter compaction remains disabled. If it is not disabled, you will need to re- create MagDexter’s reports. See [*Generating Platter Reports*](#_bookmark1) for details.

> Platter Processing

> *Scanning*

1.  Start MagKat and select the Jukebox tab.

![](vista-imaging-system-storage-utilities-user-manual/018.png)

> Important: If no files are listed on the Jukebox tab, it means that you need to move the output from MagDexter to MagKat in the C:\Program Files\Vista\Imaging

> \MagKat\jukebox folder.

2.  <span id="_bookmark5" class="anchor"></span>Review the contents of each platter status and follow the steps:

#### Online Unprocessed

> These platters were not processed.

> Select each platter and then select Process \| Platters.

#### Online Scanned, Needs Review

> Check the log files to determine why these platters did not completely process. (See the section [*“Online Scanned, Needs Review”*](#_bookmark10) *.)*

#### Processed

> These platters were successfully processed.

> No action is required. (See the section *[“Processed ” Status](#_bookmark7).)*

#### Offline Unprocessed

> These platters are not in the jukebox and must be inserted manually before they can be processed. (See the section [*“Offline Unprocessed”*](#_bookmark8) *.*)

#### Offline Error

> DiskXtender failed to access these files and placed the platters into an Offline Error state. (See the section [*“<u>Offline Error”</u>*](#_bookmark9) .)

> To clear the error:

1)  Open DiskXtender Administrator and search the Media folders for any platter IDs that are identified in red text.
2)  Right-click these platters and select Clear Error Status. The error is cleared and the text color turns black.
3)  Close DiskXtender Administrator.
4)  Highlight the platter and select Process \| Platters.

> After a platter is processed, MagKat moves the platter into a different status based on the results of the scan.

3.  Use the appropriate action as described above, when a scan is completed and is moved into a different status category.
4.  As MagKat runs, periodically check the MagKat window for the following conditions:
    - If the Recent Error Count area near the bottom of the window indicates numerous errors (i.e., shows a count “50 failed TXT files in the last 50” for a period of time), pause the scan and review MagKat’s log file before proceeding.
    - If the system response becomes sluggish on other processes, limit MagKat processing speed by moving the slider in the System Impact Throttle field to a slower setting. This will improve processing speed on other system processes.

> When processing of all selected platters is completed, a summary is displayed in the Information window shown. If the summary indicates a large number of errors in one or more platters, review the log file to determine which platter(s) need to be re-processed.

![](vista-imaging-system-storage-utilities-user-manual/019.png)

5.  Note the new status of the processed platters and determine if further action is necessary as described in Ste[p 2](#_bookmark5) above.

> <span id="Acting_on_the_Platter_Status" class="anchor"></span>*Acting on the Platter Status*

> Each possible platter status is listed in this section and described in detail.

![](vista-imaging-system-storage-utilities-user-manual/020.png)

> <span id="_bookmark7" class="anchor"></span><u>“Processed ” Status</u>

> If a platter is in the ![](vista-imaging-system-storage-utilities-user-manual/021.png) Processed status, the relevant data in that platter’s text files was copied to the IMAGE file (#2005).

> If a platter in the Processed status is marked ![](vista-imaging-system-storage-utilities-user-manual/022.png), a small number of text files were flagged as “N/A” or “skipped” because the text files could not be matched to entries in the IMAGE file (#2005). The reasons a file was skipped are noted in the Platter Processing report described in section [*Platter Processing Reports*.](#_bookmark11)

> Usually no further action is required for platters in this node.<span id="_bookmark8" class="anchor"></span> <u>“Offline Unprocessed” Status</u>

> A platter is listed under the ![](vista-imaging-system-storage-utilities-user-manual/023.png) Offline Unprocessed status if it is reported as “offline” in MagDexter’s Platter Summary report.

> If a platter is placed back online after MagDexter’s reports are loaded into MagKat, the change is not reflected in MagKat’s platter list. However, these platters can be processed as follows:

1.  Use DiskXtender to verify that the platter is now online.
2.  Use one of the following methods to indicate that the platter is back online:
    - (Recommended) Use the Offline Platters option in MagUtility to indicate that the platter is back online.
    - Use the VistA Imaging Offline Image Menu \[MAG JB OFFLINE\] option to indicate that the platter is back online (see section 9.5.2.3 in the *Imaging Technical Manual* for details).
3.  In MagKat, select the platter under the ![](vista-imaging-system-storage-utilities-user-manual/024.png) Offline Unprocessed status that you want to process, and click Process Platter.
    - If MagKat can access the platter, MagKat processes the text files on the platter and moves the platter from the Offline Unprocessed status when processing is completed.
    - If MagKat cannot access the platter, MagKat stops processing and shifts the platter to the Offline Error status.

> <span id="_bookmark9" class="anchor"></span>“<u>Offline Error” Status</u>

> Platters are listed under the ![](vista-imaging-system-storage-utilities-user-manual/025.png) Offline Error node if:

- MagDexter’s Platter Summary report indicates that the platter has a status “Offline Error.” This error comes from a status reported by DiskXtender.
- MagDexter’s Platter Detail Report is not present for the platter being scanned.

> After addressing the problem and verifying that the platter is online using DiskXtender, you can select the platter individually in MagKat and try to process it again. Or, if it is acceptable from a data management perspective, you can elect not to process the platter.

> <span id="_bookmark10" class="anchor"></span><u>“Online Scanned, Needs Review” Status</u>

> Platters are placed in the ![](vista-imaging-system-storage-utilities-user-manual/026.png) Online Scanned, Needs Review node if:

- MagKat finds more than two I/O errors when MagKat cannot find text files on a platter (based on MagDexter’s reports) or cannot access them.
- MagKat processed a significant number of text files (but not all of them) in a previous session.
- MagKat could not process a significant number of text files because:
  - There was an error from VistA when MagKat tried to retrieve information about the text file.
  - There was an error from VistA when MagKat tried to update the IMAGE file (#2005) based on the text file.
  - MagKat could not find the text file, or it was flagged as “offline” in the IMAGE file (#2005).
  - MagKat could not find the image record in VistA associated with the text file. Contact your IRM person for help.

> For detailed information about the results for a processed platter, review the Platter Processing report described in the section [*Platter Processing Reports*.](#_bookmark11)

> *Forcing Platters into the “Processed” Status*

> If necessary, you can manually move a platter into the “Processed” status by right-clicking the platter and choosing Mark Platter Processed.

> Note: This operation should be used only if you are sure that MagKat does not need to process the platter, or that MagKat cannot process the platter at all.

> Apart from the absence of a Platter Processing Report, you cannot distinguish between platters moved into the Processed node by MagKat and platters moved by marking them as described above.

> If a platter is inadvertently placed in the Processed node, you can still have MagKat process the platter by right-clicking it and choosing Process Platter.

## Re-Scanning Using Ad Hoc Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can use Ad Hoc processing to re-scan a specified range of text files if some of them were skipped in a previous scan. For example, if some text files on the RAID were skipped because a network location/share was set offline, you can use Ad Hoc processing to scan just those files, rather than all files on the RAID.

> Note: You can use Ad Hoc processing only after a RAID (magnetic) scan is completed.

> Re-Scanning Skipped Files

1.  Start MagKat and select the Ad Hoc Processing tab.
2.  In the Starting TXT IEN and Ending TXT IEN boxes, enter the range of IENs to be processed.
3.  In the Image Storage Location box, select All, Magnetic, or Jukebox.

> Important: Performing an ‘All’ or ‘Jukebox’ scan against a large range of IENs is not recommended as this may cause the jukebox to unload/load the same platters numerous times and may affect the jukebox adversely.

4.  Click Process Range.

> After processing all text files in the specified range, MagKat displays the scan results in a summary box.

5.  If any failed files are listed, check the error log in C:\Program Files\Vista

> \Imaging\MagKat\logs for details.

> Stopping and Resuming Processing

> If needed, you can stop a Magnetic, Jukebox, or Ad hoc scan and restart it later.

> Important: If you know that VistA will be inaccessible for a period of time, you should stop MagKat processing and exit the program.

> To stop processing:

1.  If it is not already visible, select the tab for the scan in progress.
2.  Click Stop Processing.

> When you stop a scan, MagKat records which text file was last processed.

3.  To resume scanning, restart MagKat and click Process Sequentially. MagKat continues processing where it left off.
4.  When processing is completed, exit MagKat.

## Viewing MagKat Platter Processing Reports and Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During processing, MagKat automatically generates two types of output:

- Platter processing reports
- Log files

> <span id="_bookmark11" class="anchor"></span>Platter Processing Reports

> Note: MagKat uses reports from MagDexter to generate platter processing reports, but you do not need to review these reports because they are in their raw form.

> The reports are stored in the \Program Files\Vista\Imaging\MagKat\\ jukebox folder on the server where MagKat is running. They are tab-delimited and can be imported into MS Excel.

> Note: If a platter is scanned more than once, only the most recent Platter Processing report is retained.

1.  To view a platter processing report, select the Jukebox tab.
2.  Right-click any processed platter and choose Platter Processing Report.

> *Sample MagKat Platter Report*

> Each platter processing report lists the text files on the platter, the processing status of each text file, and any error messages that are present, as shown in the following sample. You can sort the contents of the report window by clicking any column heading.

> The report names are based on the media label and the serial number of the platter that they contain information about.

> If the report contains less than 5000 entries, the entire report will be included in the window.

> If the report contains more than 5000 entries, only the first 5000 entries are shown. You can use the Previous Range and Next Range buttons at the bottom of the window to view the rest of the report.

> The following table describes the statuses:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Status</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Processed Successfully</td>
<td><p>Applicable fields in the IMAGE file (#2005) entry, if empty, were populated based on the data in the associated text file.</p>
<p>No further action is needed.</p></td>
</tr>
<tr class="even">
<td>Previously Processed</td>
<td><blockquote>
<p>The IMAGE file (#2005) entry was updated in a previous MagKat run. No further action is needed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>N/A or Skipped</td>
<td><p>The text file was not processed because MagKat detected a deleted, duplicate, or questionable integrity flag. In general, these text files should not be processed.</p>
<p>No further action is needed.</p></td>
</tr>
<tr class="even">
<td>Error</td>
<td>MagKat could not process the text file. Refer to the error message in the report for detailed information.</td>
</tr>
</tbody>
</table>

> MagKat Log Files

> MagKat generates three types of log files and stores them in the C:\Program Files\Vista\Imaging

> \MagKat\logs folder on the server where MagKat is running. Because of the amount of information tracked, the total amount of disk space used by all log files may be up to several gigabytes in size.

> Note: Under normal circumstances, you should not need to review any of these log files except if an error occurs.

> *Sample MagKatError.log File*

> The MagKatError.log file lists any errors that occurred during processing. MagKat appends new information to the end of the file. This file is deleted only if you manually do so.

> *Sample MagKatImageComplete.log File*

> The MagKatImageComplete.log file lists the IENs of the IMAGE file (#2005) entries that MagKat updated. Entries are listed in ranges. The 3-character site code is added as a prefix to the log file name. MagKat generates multiple instances of this file at consolidated/multidivisional sites. New information is appended to the end of the file.

> Important: This file should not be modified.

> \[ \] 7491-7572

> \[ \] 7489-7489

> \[ \] 7487-7487

> \[ \] 7484-7485

> \[ \] 7481-7482

> \[ \] 7472-7477

> \[ \] 7335-7470

> \[ \] 7257-7333

> \[ \] 7230-7255

> \[ \] 7225-7228

> \[ \] 7223-7223

> \[ \] 7178-7221

> \[ \] 7043-7176

> \[ \] 7010-7041

> \[ \] 6977-7008

> *Sample MagKatInfo.log File*

> The MagKatInfo.log file contains general debug output from the application. It is useful for determining what MagKat did. The log lists all statuses that MagKat generated. MagKat generates a new instance of this file if the file size reaches 200 MB. If more than 30 instances of this file accumulate, the oldest instance is deleted. The following sample log shows the processing of two text files.

> 4/13/2009 8:14:38 AM \[ INFO\] Processing TXT file IEN \[9281\], about to scan for new TXT file 4/13/2009 8:14:38 AM \[ INFO\] RPC Response

> \[9278,\\server\share\$\DM00\00\00\00\92\DM000000009278.TXT,M\] 4/13/2009 8:14:39 AM \[DEBUG\] Update VistA database - 9278

> 4/13/2009 8:14:39 AM \[DEBUG\] Series UID: 1.2.840.113704.7.1.1.1856.1076531055.1

> 4/13/2009 8:14:39 AM \[DEBUG\] Series Number: 344656

> 4/13/2009 8:14:39 AM \[DEBUG\] Image Number: 20

> 4/13/2009 8:14:39 AM \[DEBUG\] Image UID: 1.2.840.113704.7.1.1.1856.1076531058.81

> 4/13/2009 8:14:39 AM \[DEBUG\] Study UID: 1.2.840.113704.1.111.11940.1076530348.1

> 4/13/2009 8:14:39 AM \[DEBUG\] Content d/t: 20040211-151228

> 4/13/2009 8:14:39 AM \[DEBUG\] Acquisition d/t: 20040211-151638

> 4/13/2009 8:14:39 AM \[DEBUG\] Creation d/t: 20040211-152418

> 4/13/2009 8:14:39 AM \[DEBUG\] Document Date: 3040211.151228

> 4/13/2009 8:14:39 AM \[ INFO\] TMagKatBroker.updateVistATxtFields, \[9278\] updated result \[0,OK\] 4/13/2009 8:14:39 AM \[ INFO\] Processing TXT file IEN \[9278\], about to scan for new TXT file 4/13/2009 8:14:39 AM \[ INFO\] RPC Response

> \[9277,\\server\share\$\DM00\00\00\00\92\DM000000009277.TXT,M\] 4/13/2009 8:14:39 AM \[DEBUG\] Update VistA database - 9277

> 4/13/2009 8:14:39 AM \[DEBUG\] Series UID: 1.2.840.113704.7.1.1.1856.1076531055.1

> 4/13/2009 8:14:39 AM \[DEBUG\] Series Number: 344656

> 4/13/2009 8:14:39 AM \[DEBUG\] Image Number: 19

> 4/13/2009 8:14:39 AM \[DEBUG\] Image UID: 1.2.840.113704.7.1.1.1856.1076531058.80

> 4/13/2009 8:14:39 AM \[DEBUG\] Study UID: 1.2.840.113704.1.111.11940.1076530348.1

> 4/13/2009 8:14:39 AM \[DEBUG\] Content d/t: 20040211-151228

> 4/13/2009 8:14:39 AM \[DEBUG\] Acquisition d/t: 20040211-151638

> 4/13/2009 8:14:39 AM \[DEBUG\] Creation d/t: 20040211-152418

> 4/13/2009 8:14:39 AM \[DEBUG\] Document Date: 3040211.151228

> 4/13/2009 8:14:39 AM \[ INFO\] TMagKatBroker.updateVistATxtFields, \[9277\] updated result \[0,OK\]

# Using MagUtility to Maintain the VistA Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagUtility is a maintenance and validation tool used to:

- Report and resolve (where possible) problems with “orphan” files on RAID network locations
- Delete certain types of obsolete or incorrect entries from the NETWORK LOCATION file (#2005.2)
- Update VistA with information about images that are no longer available because a jukebox platter was removed
- Update VistA with information about images that are now available because a platter was restored
- Copy images and text files from one RAID share or jukebox network location to another

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For Administrators

> MagUtility is intended for Imaging administrators responsible for maintaining Imaging RAID and jukebox storage resources. Familiarity with and full access to the following is assumed:

- Imaging storage concepts (Imaging shares, network locations, jukebox operation, etc.)
- IMAGE file (#2005), VA FileMan, DICOM
- Background Processor-related applications (e.g., JBTOHD, JUKEBOX queues)

> For Servers

> MagUtility can be installed on any server that has:

- Access to the VistA database (broker connection setup (e.g, Brokerserver,9200)
- Read/Write access to RAID and jukebox shares where Imaging files are stored

> Content removed: FOIA exemption b2/high2

- Minimum of 600 megabytes of free disk space and 2GB system memory (More space may be needed if the default settings for log files are changed.)

> Note: Ideally, MagUtility should be installed on one of the Imaging servers.

> <span id="_bookmark12" class="anchor"></span>Installation instructions for MagUtility are documented in the Patch Description for MAG\*3.0\*98.

> For VistA

- Imaging Patch MAG\*3.0\*98 must be installed in VistA.

> When MagUtility runs, it checks VistA to ensure that Patch 98 is installed. If Patch 98 is not installed, MagUtility exits automatically.

- The VistA user account used to run MagUtility must be assigned the MAG UTILITY secondary menu option.

## How MagUtility Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To maintain the VistA database, MagUtility performs several processes detailed in the following sections. The procedures for running these processes are explained later in this chapter.

> Orphan Files Process

> An orphan file is an image file that:

- Has no pointer to the IMAGE file (\#2005) or IMAGE AUDIT file (#2005.1) in the VistA database (See [*Pointers and Pointer Selection Logic*](#_bookmark12).)
- Has pointers to the IMAGE file (#2005 and IMAGE AUDIT file (#2005.1) in the VistA database
- Has the same name as a file on another share that has a valid pointer to the database
- Has a zero byte size due to a loss of all of its content
- Has an invalid file extension

> Note: Allowable file types are in the IMAGE FILE TYPES file (#2005.021).

> When MagUtility processes orphan files, it verifies that files (such as \*.tga, \*.txt, \*.abs) on RAID network locations in VistA Imaging are properly associated with entries in the IMAGE file (#2005). If the process finds problems, it addresses them, if possible, and logs them if you need to manually intervene or do additional research.

> *Pointers and Pointer Selection Logic*

> Throughout this section, the term *RAID pointer* is used generically to indicate the RAID storage location referenced in the IMAGE file (#2005). Depending on the extension of the file being scanned (\*.abs, \*.tga, \*.big, etc.), the pointer in the IMAGE file (#2005) can be any one of the following fields:

- DISK & VOLUME, ABSTRACT field (#2005,2.1) – used for ABS files
- BIG MAGNETIC PATH field (#2005,102) – used for BIG files
- DISK & VOLUME, MAGNETIC field (#2005,2) – used if the file is *not* ABS, BIG, or TXT

> Note: TXT files are not directly referenced in the IMAGE file (#2005) the way other file types are. To infer the location of a TXT file using an entry in the IMAGE file (#2005), the Orphan Files process checks the following fields in the applicable entry in the following order:

1.  DISK & VOLUME, MAGNETIC field (#2005,2)
2.  DISK & VOLUME, ABSTRACT field (#2005,2.1)
3.  BIG MAGNETIC PATH field (#2005,102)

> The first field that has a pointer, such as (#2005,2), is immediately considered the “applicable RAID pointer”, and no other fields in the sequence are checked.

> *Processing Logic Used in an Orphan Files Check*

> When the Orphan Files process runs on a selected share, MagUtility performs either of two operations:

- If you select the Generate report only option, MagUtility logs both types of problems (corrected and not corrected).
- If you select the Clean up orphan files and generate report option, MagUtility logs problems that are corrected and not corrected, listed as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Problems that MagUtility Corrects</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deletes files with a zero length</td>
</tr>
<tr class="even">
<td>If MagUtility can trace a zero-length file to an entry in the IMAGE file (#2005), and if that entry points back to the location of the zero-length file, MagUtility clears the RAID pointer in that entry and deletes the file.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Problems that MagUtility Corrects</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Deletes duplicate files on the share being processed if:</p>
<ul>
<li><p>MagUtility can trace a file to an entry in the IMAGE file (#2005), but that entry points to another file on a different share, and</p></li>
<li><p>The “other file” has the same properties as the file being traced.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Fixes incorrect RAID pointers in the IMAGE file (#2005) if:</p>
<ul>
<li><p>MagUtility can trace a file on the share being processed to an entry in the IMAGE file (#2005), and</p></li>
<li><p>The RAID pointer in the applicable entry points to a share different from the one being processed, and</p></li>
<li><p>There is no file of the same name on the “different share”.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Updates pointers in the IMAGE file (#2005) to reflect a storage location on the RAID if:</p>
<ul>
<li><p>A file on the share being processed exists both on the RAID and on the jukebox, and</p></li>
<li><p>The applicable IMAGE file (#2005) entry for that file references the jukebox copy only, and</p></li>
<li><p>The properties of the two files match.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Problems that MagUtility Does Not Correct</strong></p>
</blockquote>
<p><strong>Note</strong>: If MagUtility finds any of these issues, you need to manually address them. See <a href="#_bookmark14"><em>Troubleshooting the Orphan Files Process</em>.</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The file has an invalid file extension based on the allowable file types in the IMAGE FILE TYPES file (#2005.021).</td>
</tr>
<tr class="even">
<td>MagUtility cannot associate the file with an entry in the IMAGE file (#2005) because the “F” cross-reference is missing or invalid.</td>
</tr>
<tr class="odd">
<td>The file has a record in the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1). (DUPE field (#2005,13.5) is set.)</td>
</tr>
<tr class="even">
<td>The file has a data integrity problem. (The <em>Verifier</em> chapter in the <em>VistA Imaging System Background Processor User Manual</em> has a listing of the possible integrity problems.) (IQ field (#2005,13) is set.)</td>
</tr>
<tr class="odd">
<td>The record in VistA for the file IEN points to a different file and the file is not on the jukebox.</td>
</tr>
<tr class="even">
<td>The file has no valid RAID pointers, and the jukebox pointer points to a file with properties (date, size, etc.,) different from the one being scanned.</td>
</tr>
<tr class="odd">
<td>The record in VistA points to a file on another share with different properties than the file being traced</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Problems that MagUtility Does Not Correct</strong></p>
</blockquote>
<p><strong>Note</strong>: If MagUtility finds any of these issues, you need to manually address them. See <a href="#_bookmark14"><em>Troubleshooting the Orphan Files Process</em>.</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The file is a text file that can be traced to an entry in the IMAGE file (#2005), but cannot be traced from the IMAGE file (#2005) to a text file. See <em><a href="#_bookmark12">Pointers and</a> <a href="#_bookmark12">Pointer Selection Logic.</a></em></td>
</tr>
</tbody>
</table>

> Offline Jukebox ImagesProcess

> MagUtility's Offline Jukebox Images process should be used whenever platters are removed from or inserted back into the jukebox. Use MagUtility to update VistA with the appropriate status of the files on these platters.

> Network Location Cleanup

> MagUtility’s Network Location Cleanup process deletes outdated or improperly defined entries from the NETWORK LOCATION file (#2005.2).

> Storage Copy Process

> MagUtility’s Storage Copy process transfers Imaging files from one Imaging RAID or jukebox network location to another RAID or jukebox network location. This process can be used to repopulate a RAID from the jukebox after expanding or upgrading the RAID.

> Additionally, the Storage Copy process checks for non-standard file name formats (9 or 10- character names), and converts those names to the proper 14-character format on the source network location as part of the Copy operation. File name references in the IMAGE file (#2005) are updated automatically as well.

## Starting and Exiting MagUtility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Starting MagUtility

1.  On the server where MagUtility is installed, choose VistA Imaging Programs \| MagUtility

> from the Windows Start \| Programs menu.

2.  In the VistA Sign-on dialog box, enter your access and verify codes and then click OK.
3.  If the Select Division dialog box opens, double-click the appropriate division and then click

> OK.

4.  Wait until the MagUtility window opens.

> Description of the MagUtility Window

> The title bar displays the site name and username, as shown in the example.

![](vista-imaging-system-storage-utilities-user-manual/027.png)

> <u>Menu Bar</u>

> The File menu enables you to log in and log out, open the Info and Debug log files from any tab, and exit the utility.

![](vista-imaging-system-storage-utilities-user-manual/028.png)

> <u>Tabs</u>

> Each tab indicates a process in MagUtility. The Orphan Files tab is displayed by default. For the procedures on running each process, see:

- [*Running the Orphan Files*](#_bookmark13)
- [*Running the Offline Jukebox Images*](#_bookmark15)
- [*Running the Network Location Cleanup*](#running-the-network-location-cleanup-process)
- [*Running the Storage Copy*](#running-the-storage-copy-process)

> <u>Process Status Box</u>

> The Process Status box displays the results of processing.

> Exiting MagUtility

1.  Check each tab to ensure that no MagUtility processes are active.
2.  Choose File \| Exit from the menu bar.

> Important: Whenever you exit MagUtility, any active MagUtility processing is aborted.

## Running the Orphan Files Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Processing orphan files can be lengthy depending on your server and network capacity. In general, plan for an hour of processing time for every 30,000 files scanned. However, because this process has a low impact on system response, you can run this process while the Imaging System is active.

> Recommendation: Run this process on the same schedule that your site uses for Verifier processing. If your site runs the Verifier monthly, initially run the Orphan Files process every one to three months. Thereafter, you can increase this interval based on the results of initial Orphan Files scans.

> Prerequisite for Running an Orphan Files Check

> Before you run the Orphan Files process, run the Verifier for all IENs (internal entry numbers) in the IMAGE file (#2005).

> Tip: Running the Verifier first reduces the number of potential problems that may occur during the Orphan Files process. For more information on the Verifier, refer to the *Verifier* chapter in the *VistA Imaging System Background Processor User Manual*.

> Running an Orphan Files Check

> Important: Do not run MagUtility’s Storage Copy process on the same RAID share where the Orphan Files process is running.

> Recommendation: If MagUtility is installed on multiple servers, you should not run multiple Orphan Files processes at the same time.

1.  Start MagUtility (if it is not already running). MagUtility opens on the Orphan Files tab.
2.  Select the network location(s) to process.

> Only RAID (magnetic) network locations that are both online and non-routing are listed.

3.  Select one of the following options on the right side of the Orphan Files tab:

#### Generate report only

> To have MagUtility log all issues but take no corrective action

#### Clean up orphan files and generate report

> To have MagUtility remove confirmed orphan files and log all issues

> Note: If MagUtility detects but cannot correct an issue, it logs the issue but takes no corrective action.

4.  Click Run to start the scan.

> Note: You can abort a scan by clicking Cancel but you cannot pause and resume a scan. The following successful run message is displayed.

> ![](vista-imaging-system-storage-utilities-user-manual/029.png)

5.  Periodically monitor the scan as it progresses.
    - The Orphan File process box at the bottom of the Orphan Files window displays the last (scanned) file and last (scanned) IEN, as shown in this example.

![](vista-imaging-system-storage-utilities-user-manual/030.png)

- If the share being scanned becomes unavailable for some reason, MagUtility pauses for one minute and then tries to reconnect to the share. If MagUtility cannot access the share after three attempts, it aborts the process and logs the problem.
- When MagUtility finishes a scan, it displays the following message.

![](vista-imaging-system-storage-utilities-user-manual/031.png)

6.  To review the results of a scan, check the log files by choosing File \| Open Log. For details on the log files generated, see [*Working with MagUtility Log Files*](#viewing-and-customizing-magutility-logs).

> Note: If MagUtility checks a file and finds no problems, it does not log anything about the file. A prompt is displayed that processing is complete. The log file indicates that zero orphan files were found.

> <span id="_bookmark14" class="anchor"></span>Troubleshooting the Orphan Files Process

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2005 file <em>IEN</em> referenced filename1 file size is 0, but found filename2</td>
<td>The pointer in VistA references a file of zero length. (Generate Report only)</td>
<td>Take no action on this log message</td>
</tr>
<tr class="even">
<td>Cannot verify the off-line image file to process <em>filename</em></td>
<td>The RAID or jukebox share at the VistA network location is OFFLINE. Cannot verify if it is an orphan.</td>
<td>Determine why the share is OFFLINE and set it back ONLINE for Orphan file checking.</td>
</tr>
<tr class="odd">
<td>cleared or updated 2005 file pointer</td>
<td><blockquote>
<p>The file contents are empty. The file was deleted. Its RAID pointer in VistA was cleared.</p>
</blockquote></td>
<td>Take no action on this log message.</td>
</tr>
<tr class="even">
<td>Delete candidate</td>
<td>a file was found that was identified as an orphan. It is not deleted ( Generate Report only option)</td>
<td>Take no action on this log message.</td>
</tr>
<tr class="odd">
<td>deleted file</td>
<td>Orphan file found. File was deleted</td>
<td>Take no action on this log message.</td>
</tr>
<tr class="even">
<td>Error - cannot delete the file <em>filename.</em></td>
<td>File was marked an orphan for deletion but could not be deleted.</td>
<td>Examine permissions or lock on the share/file itself.</td>
</tr>
<tr class="odd">
<td>error clearing or updating 2005 file pointer with <em>RAID ptr, filename</em></td>
<td>The file contents are empty. The file was deleted. But its RAID pointer in VistA database could not be cleared.</td>
<td>Log a Remedy ticket.</td>
</tr>
<tr class="even">
<td>file deleted - cannot find associated 2005 file IEN for <em>filename</em></td>
<td>No IEN was found in VistA for the file name.</td>
<td>Take no action on this log message.</td>
</tr>
<tr class="odd">
<td>file deleted since the same file was found on other RAID <em>name</em></td>
<td><blockquote>
<p>Same copy of file found on another share, deleted duplicate</p>
</blockquote></td>
<td>Take no action on this log message.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>file size variance between the two Network Locations</td>
<td>The file at the VistA RAID location had a size different from the current file.</td>
<td>Compare the two files by viewing them, if possible, to see if they are the same. If no conclusion can be made, copy the file to another location for later reference and delete it from the share.</td>
</tr>
<tr class="even">
<td><em>file_extension</em> is not an approved file extension</td>
<td>The current file extension is not listed in the IMAGE FILE TYPES file (#2005.021).</td>
<td>Examine the file. Change the extension if it has a wrong extension. If not, copy the file to another location for later reference and delete it from the share.</td>
</tr>
<tr class="odd">
<td>Found two or more RAID pointers pointing to the same physical reference</td>
<td><blockquote>
<p>There are two Network Locations that point to the same RAID share: the share that is being traversed and the one indicated in this message.</p>
</blockquote></td>
<td>Run the Network Location File Cleanup utility. If the duplicates remain, Patch 39 post install processing will remove the duplicate.</td>
</tr>
<tr class="even">
<td>image file with different "Date Modified"</td>
<td><blockquote>
<p>Found another file at the RAID location in VistA. The Windows modified date on the current file and the VISTA location RAID file do not match.</p>
</blockquote></td>
<td>Compare the two files by viewing them, if possible, to see if they are the same. If no conclusion can be made, copy the file to another location for later reference and delete it from the share.</td>
</tr>
<tr class="odd">
<td>image file with different "Date Modified" <em>filename1 date1</em> vs <em>filename2 date2</em></td>
<td><blockquote>
<p>The file at the VistA RAID location had a modified date different from the current RAID file.</p>
</blockquote></td>
<td>Compare the 2 files by viewing them, if possible, to see if they are the same image sets. If no conclusion can be made, copy the file to another location for later reference and delete it from the share.</td>
</tr>
<tr class="even">
<td>Index out of bounds</td>
<td>An application error occurred.</td>
<td>Check the application log file (or VistA error log file) for details and log a VA Remedy support call.</td>
</tr>
<tr class="odd">
<td>IQ or DUPE fields are set</td>
<td><p>One or both of these conditions exist:</p>
<p>There is an IMAGE file (#2005) record and an IMAGE AUDIT file (#2005.1) record in VistA.</p>
<p>There is a serious problem with the image records in VistA.</p></td>
<td>Log a Remedy ticket.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><blockquote>
<p><strong>Explanation</strong></p>
</blockquote></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>missing file extension</td>
<td>The current file has no extension</td>
<td>Examine the file. If the proper extension can be determined, add the extension; If not, copy the file to another location for later reference and delete it from the share.</td>
</tr>
<tr class="even">
<td>no IEN "F" x-ref for the filename</td>
<td>The current file record in VistA is missing a critical field - ‘FileRef’ cross-reference, or it can be just an orphan file miss- placed.</td>
<td>Log a Remedy ticket.</td>
</tr>
<tr class="odd">
<td>no RAID or JB pointer</td>
<td>The current file has no references in VistA.</td>
<td><p>If the file exists on the jukebox, run the Verifier over this IEN to set the jukebox pointer.</p>
<p>Log a Remedy ticket.</p></td>
</tr>
<tr class="even">
<td>orphan file cannot be deleted because no archive copy exists for <em>filename</em></td>
<td>There are no jukebox files or no jukebox pointer.</td>
<td><p>Run the Verifier to copy the files to the jukebox.</p>
<p>.</p></td>
</tr>
<tr class="odd">
<td>Orphan TXT file found and removed <em>filename</em></td>
<td><blockquote>
<p>A TXT file was found which matched another file of the same name/size. It was deleted</p>
</blockquote></td>
<td>Take no action on this log message</td>
</tr>
<tr class="even">
<td><p>Orphan TXT file found</p>
<p><em>filename</em></p></td>
<td>A TXT file was found which matched another file of the same name/size. File was not deleted (Generate Report only)</td>
<td>Take no action on this log message</td>
</tr>
<tr class="odd">
<td>Out of memory</td>
<td>The most likely problem is that either the system ran out of memory and prevented the task from continuing or the system disk drive ran out of space.</td>
<td><p>You may use Windows Task Manager to check the process Image named “MagUtility.exe" for Memory Usage.</p>
<p>Verify that there is enough system memory/disk space for the operation before logging a VA Remedy support call.</p></td>
</tr>
<tr class="even">
<td>pointer needs to be updated</td>
<td><blockquote>
<p>Found file with no VistA RAID pointer set or set to another empty RAID location. VistA pointer is not changed.</p>
</blockquote></td>
<td>Take no action on this log message</td>
</tr>
<tr class="odd">
<td>pointer needs to be updated. IMAGE 2005 <em>IEN</em> referenced file does not exist, but found <em>filename</em></td>
<td><p>The file referenced by Vista for this IEN does not exist.</p>
<p>Change the pointer in Vista to this new location</p></td>
<td>Take no action on this log message</td>
</tr>
<tr class="even">
<td>reset 2005 file pointer</td>
<td><blockquote>
<p>File found with no VistA pointer set. It updated VistA record pointer.</p>
</blockquote></td>
<td>Take no action on this log message.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 33%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>reset pointer with selected RAID reference <em>sharename, IEN,filename</em></td>
<td>Found file with no VistA RAID pointer set or set to another empty RAID location. Change pointer.</td>
<td>Take no action on this log message</td>
</tr>
<tr class="even">
<td>the share pointer in the 2005 file, does not match the share pointer selected for review</td>
<td>A text file was found at a location that does not match the Full file location in VistA.</td>
<td><p>Determine if there is a text file at the Full RAID pointer location in VistA. If so and the text files match, delete the text file.</p>
<p>Otherwise, log a Remedy ticket.</p></td>
</tr>
<tr class="odd">
<td>there are different size image files on RAID and Jukebox</td>
<td>The size of the current file on RAID is different from the one on the jukebox.</td>
<td>Log a Remedy ticket.</td>
</tr>
<tr class="even">
<td>There is no VistA #2005 IMAGE file entry</td>
<td>There is no record in VistA for the current file.</td>
<td>Log a Remedy ticket.</td>
</tr>
<tr class="odd">
<td>zero length file deleted file</td>
<td>The file contents are empty. The file was deleted.</td>
<td>Take no action on this log message.</td>
</tr>
</tbody>
</table>

## Running the Offline Jukebox Images Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you run out of room to add additional platters to your jukebox, you can remove platters to create free slots. Use the Offline Jukebox Images process to record the list of image files on these platters in VistA as offline. When these platters are re-inserted into the jukebox, use the utility to mark the images online.

> Note: This operation duplicates the MAG JB OFFLINE menu option available in VistA.

> Marking Images Offline

> This operation updates the status of the files on the jukebox platters in the VistA database.

> Note: You must use the third-party software, DiskXtender, to actually remove platters. This operation assumes that you are using DiskXtender for jukebox management. Other jukebox management systems are not supported.

1.  Use the DiskXtender Administrator to generate a Media Files report for each side of each platter to be removed from the jukebox.
2.  Save each media file report as a \*.txt file (not an \*.rtf file).
3.  Copy each of the reports to a location accessible to MagUtility.
4.  Start MagUtility (if not already running) and select the Offline Jukebox Images tab.

![](vista-imaging-system-storage-utilities-user-manual/032.png)

> Note: You can start Offline Jukebox processing while the VistA system is active and while other MagUtility processes are running.

5.  At the Mark images offline field, click the ellipsis ![](vista-imaging-system-storage-utilities-user-manual/033.png), select one or more platter reports (\*.txt files), and click Open.

> The Clear list button and Mark offline button become enabled.

> To change your selection, you can click the Clear list button and re-select different files.

6.  ![](vista-imaging-system-storage-utilities-user-manual/034.png)Click the Mark offline button. .

> All the files are marked offline - you cannot select individual files. The following message is displayed.

![](vista-imaging-system-storage-utilities-user-manual/035.png)

> The OFFLINE IMAGES file (#2006.033) in the VistA database is updated based on the image file names in these reports.

> Note: If you selected platter reports already marked offline, they will not be processed or recorded in the count of platter reports and the following message will be displayed.

![](vista-imaging-system-storage-utilities-user-manual/036.png)

7.  Use DiskXtender Administrator to physically remove the files marked offline from the jukebox.

> For details on the log files generated, see [*Working with MagUtility Log Files*.](#viewing-and-customizing-magutility-logs)

> Marking Images Online

1.  Use DiskXtender Administrator to insert the offline platters back into the jukebox.
2.  Start MagUtility (if it is not already running) and select the Offline Jukebox Images tab.
3.  At the Mark images online field, click the drop-down list box to select a media file for a patient that you are bringing back online.

> Note: You can select only one file at a time. Be sure to process a file for each platter side.

4.  Click the Mark online button. ![](vista-imaging-system-storage-utilities-user-manual/037.png) The following message is displayed.

![](vista-imaging-system-storage-utilities-user-manual/038.png)

> Entries for images associated with each selected platter are removed from the OFFLINE IMAGES file, and the images become accessible to clinicians.

> For details on the log files generated, see [*Working with MagUtility Log Files*.](#viewing-and-customizing-magutility-logs)

> Troubleshooting the Offline Jukebox Images Process

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 31%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All requested images have been marked online</td>
<td>The image file names have been successfully removed from VistA indicating the images are now viewable.</td>
<td>No action is necessary.</td>
</tr>
<tr class="even">
<td>Marked a total of <em>nnn</em> files offline from <em>number of platters</em> of platter report(s), where <em>number of platters</em> platter reports could not be read</td>
<td>Some of the selected platter reports could not be read</td>
<td>Examine the reports of the failed platters listed to determine if they are corrupted. Regenerate the reports, if necessary.</td>
</tr>
<tr class="odd">
<td>Marked platter: #<em>platter</em> offline by user:</td>
<td>Files on the platter have been marked offline successfully.</td>
<td>No action is necessary</td>
</tr>
<tr class="even">
<td><em>n</em> platter(s) out of <em>m</em> requested JB images have been marked offline by <em>user</em></td>
<td>The count indicates how many platter reports had valid file names out of the total number selected.</td>
<td><p>Examine the platter reports that were not processed. Re- generate a new platter report, if necessary.</p>
<p>Note: Platter reports with no file names listed will not show up in the processed count.</p></td>
</tr>
<tr class="odd">
<td>Selected <em>platter</em> is not in a correct platter report format and will be skipped.</td>
<td>The platter text file is corrupt.</td>
<td>Generate another platter report using DiskXtender.</td>
</tr>
<tr class="even">
<td>Task has completed but there were no image files to process</td>
<td>None of the platters selected had any image files listed in their reports.</td>
<td>Examine the platter reports to verify there are no files listed in each report selected.</td>
</tr>
</tbody>
</table>

## Running the Network Location Cleanup Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can use MagUtility’s Network Location Cleanup to delete outdated or improperly defined entries in the NETWORK LOCATION file (#2005.2).

> To qualify for deletion, an entry must:

- Have a Storage Class of MAGNETIC (for RAID shares) or WORM-OTG (for jukebox shares
- Be set offline
- Not be referenced by any pointers in the IMAGE file (#2005) or IMAGE AUDIT File (#2005.1)

> Removing RAID or Jukebox NetworkLocations

1.  Start MagUtility (if it is not already running) and select the Network Location Cleanup tab.

![](vista-imaging-system-storage-utilities-user-manual/039.png)

> Tip: To refresh the list of network locations in the tab, you can select a different tab and then re-select the Network Location Cleanup tab.

> Note: In running network location cleanup, the file reference(s) listed may not be all of the references. Additional work may need to be done to identify all references still active for the network location.

2.  Select the network location that you want to remove.
3.  Click Remove.
    - The progress bar indicates that processing has begun.

![](vista-imaging-system-storage-utilities-user-manual/040.png)

- MagUtility checks the IMAGE file (#2005) and IMAGE AUDIT file (#2005.1) to ensure that no entries contain pointers to the selected location.
- If the check is successful, the network location is removed and the following message is displayed.

![](vista-imaging-system-storage-utilities-user-manual/041.png)

- If problems are found, they are displayed on the screen and logged. See the Troubleshooting section that follows.

> For details on the log files generated, see [*Working with MagUtility Log Files*.](#viewing-and-customizing-magutility-logs)

> Troubleshooting the Network Location Cleanup Process

| Log Message                                                          | Explanation                                                        | Action                                                                                                                                                                  |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cannot remove NETWORK LOCATION IEN as image files references were found. | There are image records in VistA that reference this Network Location. | Find the record(s) in VistA and move the file(s) that it references to another existing Network Location. Then change the RAID and/or jukebox pointers to the new location. |
| Network location *\#IEN* has been removed.                               | The Network Location indicated has been deleted from VistA.            | No action is necessary.                                                                                                                                                     |

## Running the Storage Copy Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vista-imaging-system-storage-utilities-user-manual/042.png) Do not use the Storage Copy process for general disk migration. The Storage Copy process copies only files that are referenced in the IMAGE file (#2005) in the VistA database. The Storage Copy process ignores non-referenced files.

> If you copy a large number of images, running the Storage Copy process can be lengthy. For example:

- To copy files from the Jukebox, it takes on average 2 minutes per IEN (image set), which includes copying or moving files and updating the pointers to the VistA database.
- To copy files from the RAID, it takes on average 30 seconds per IEN (image set)

> If this process is used to copy images from RAID to RAID, system impact is typically minor. However, if images are copied to or from a jukebox, other jukebox operations (such as media copy, backups, and restore) may be impacted based on the amount of space in the jukebox cache or on the availability of jukebox optical drives. You can optionally run the Storage Copy process only during after-hours to reduce system impact.

> Preparing to Use Storage Copy

1.  Use Windows Explorer to determine the amount of space used by the source files and ensure that the space is available on the destination network location.
2.  Verify that the destination network location is defined as hashed.

> Important: Only hashed network locations can be selected as a destination in MagUtility.

> Tip: You can use Background Processor’s Network Location Manager to determine if a network location is hashed or unhashed. For details, see the *VistA Imaging Background Processor User Manual*.

3.  Run the Verifier for the entire set of IENs in the IMAGE file (#2005) and address any issues found.
4.  Run the MagUtility Orphan Files process for the source network location and address any issues found.

> Starting the Storage Copy Process

1.  Start MagUtility (if it is not already running) and select the Storage Copy tab. The following warning message is displayed on the proper use of this utility.

![](vista-imaging-system-storage-utilities-user-manual/043.png)

2.  Click OK to close the window.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-storage-utilities-user-manual/044.png)</p>
</blockquote></th>
<th><blockquote>
<p>To prevent copies of partially acquired cases, Storage Copy does not copy images having today’s date, even if they fall within a range that you specify.</p>
<p>Ranges are not sensitive to case or image group relationships. If part of a case falls inside a range and part of the case falls outside the range, only the images within the range are copied.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](vista-imaging-system-storage-utilities-user-manual/045.png)

3.  ![](vista-imaging-system-storage-utilities-user-manual/046.png)To copy IENs by date, select the By date option, click the calendar icon to specify the From Date field, and then click OK in the calendar window displayed.

![](vista-imaging-system-storage-utilities-user-manual/047.png)

> Note: *Date* means the date/time when the file was acquired by the DICOM Gateway, Capture workstation, etc. set in the DATE/TIME IMAGE SAVED field (#2005,7).

4.  Repeat the same step to specify the To Date field.

> The approximate IEN number is displayed below the To and From Date fields.

5.  To copy by IEN number, click the By IEN option and perform any of the steps:
    - For a specific range, type the IEN number in the From IEN field and then the To IEN field and press \<Enter\> to specify the lowest and highest IENs in the range of images to copy.

> The approximate capture dates are displayed below the fields.

- For all IENs on a network location, type an asterisk (\*) in the From and To fields and press \<Enter\>.

> The IEN numbers are displayed in the fields, and approximate capture dates are displayed below the fields.

- For a specific starting IEN through the end of the IENs, type an IEN number in the From field and an asterisk (\*) in the To field and press \<Enter\>.

> The ending IEN number is displayed in the To field with the end date below the field.

- For all IENs through a specific ending IEN, type an asterisk (\*) in the From field and an IEN number in the To field and press \<Enter\>.

> The starting date is displayed below the From field.

> Important: Some IENs in the range may not be copied. Only the IENs actually stored on the source network location are copied.

6.  In the From network location (source) box (now enabled when you pressed \<Enter\> above), click the ellipsis ![](vista-imaging-system-storage-utilities-user-manual/048.png), select the source to copy images from in the Source Location window, and click OK.

![](vista-imaging-system-storage-utilities-user-manual/049.png)

> Note: When you click OK, if your selection is not available, an error message is displayed. You must resolve the issue and re-select the source. See *[Troubleshooting the Storage Copy](#_bookmark19)* [*Process*.](#_bookmark19)

7.  In the To network location (destination) box, click the ellipsis ![](vista-imaging-system-storage-utilities-user-manual/050.png), select the destination from the Destination Location window, and click OK.

![](vista-imaging-system-storage-utilities-user-manual/051.png)

> Note: When files are copied to a destination network location, the destination is always populated with a hashed structure, even if the files were stored in a non-hashed (flat) structure on the source network location. The process involves:

- If hashing is used, files are maintained in a 5-level deep subdirectory structure where no directory will contain more than 100 unique filenames with their various extensions.
- If hashing is not used, files are placed and retrieved from the root directory of the share.

> Important: If there are two references to hashed files (with H) and non-hashed files (without H), they are stored in different locations within the same physical location. Therefore, be careful in copying files.

8.  In the Storage Copy window, select any of the Storage Copy options that you want:

| If you select | Then |
|-------------------|----------|

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>If you select</strong></th>
<th><strong>Then</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Remove source files</strong></td>
<td><p>Update #2005 reference is automatically selected and cannot be cleared.</p>
<p>The process moves images and updates the IMAGE file (#2005) references.</p>
<p>Source files and their associated directories (if all files in a directory are copied) are deleted from the source share as the Copy progresses.</p>
<p>Note: This option is disabled if the source network is a jukebox.</p></td>
</tr>
<tr class="even">
<td><strong>Update #2005 reference</strong></td>
<td><p>The process copies the images and updates references in the IMAGE file (#2005).</p>
<p>When the Copy is finished, source images remain. However, they are “orphaned” because the references in the</p>
<p>IMAGE file (#2005) point to the location of the images on the destination network location.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Neither</strong></p>
<p><strong>Remove source files nor Update #2005 reference</strong></p></td>
<td><p>The process copies images to the destination but does not update the references in the IMAGE file (#2005).</p>
<p>The references in the IMAGE file (#2005) still point to the images on the source network location.</p>
<p>The source files are not deleted.</p></td>
</tr>
<tr class="even">
<td><p><strong>Run after-hours</strong></p>
<p><strong>6 PM to 6 AM weekdays and all weekend</strong></p></td>
<td>Running the Storage Copy process during these specified hours limits the system impact. See <a href="#_bookmark18"><em>Running After Hours</em>.</a></td>
</tr>
</tbody>
</table>

9.  To start the process, click Run.

> The process status box at the bottom of the window displays a progress bar with the following results:

- IENs processed successfully indicates the number of IENs that were copied successfully. The following message and sample process status are displayed.

![](vista-imaging-system-storage-utilities-user-manual/052.png)![](vista-imaging-system-storage-utilities-user-manual/053.png)

- IENs that could not be processed indicates the number of IENs where some or all of the requested actions could not be completed.

> For possible causes, see [*Troubleshooting the Storage Copy Process*.](#_bookmark19) You can also open the MagUtilityInfo.log file (File \| Open log) to view information about failed copies of images.

> Note: For details on the log files generated, see [*Working with MagUtility Log Files*.](#viewing-and-customizing-magutility-logs)

> Pausing, Resuming, or Canceling the Storage Copy Process

- To pause processing, click Pause and then click OK to confirm the operation. Processing remains paused until you resume or cancel it.

> Note: If the MagUtility window is closed when a Storage Copy process is paused, the copy process is cancelled.

- To resume the process, click Resume.
- To cancel the process, click the Pause button first and then click Cancel. Note: Canceling the process may create orphan files on the destination share.

> <span id="_bookmark18" class="anchor"></span>Running After Hours

> When you select the Run after hours option, the Storage Copy process runs only from 6PM to 6AM on weeknights and all day on weekends.

> During other time periods, the process is suspended and the process status box at the bottom of the Storage Copy window indicates that the next phase of the process is scheduled to resume at a later time.

> If a scheduled process takes longer than 12 hours or a weekend to finish, MagUtility suspends it from 6AM to 6PM on weekdays and resumes it according to the schedule described above.

> Note: Exiting MagUtility cancels the Storage Copy process, even if it is scheduled to run at a future time.

> <span id="_bookmark19" class="anchor"></span>Troubleshooting the Storage Copy Process

| Log Message                                                                    | Explanation                                                                               | Action             |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------|
| Cleared RAID pointer for image IEN *\#IEN*                                         | A RAID pointer in VistA was cleared. It contained the source location.                        | No action is required. |
| Copied all files found for image IEN *\#IEN*                                       | The Full/ABS/TXT/(BIG) files have been copied from the location specified to the destination. | No action is required. |
| *destination_file* same file already exist at destination, could not move the file | There was another file with the same name as the source at the destination location.          | No action is required. |

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 37%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Error occurred, clearing RAID pointer for image IEN <em>#IEN</em></td>
<td>The attempt to clear a RAID pointer in VistA failed. It contains the source location.</td>
<td>Log a Remedy ticket.</td>
</tr>
<tr class="even">
<td>Image IEN <em>#IEN</em> image entry had been deleted, will be skipped</td>
<td>The pointer in VistA to the FULL file is empty.</td>
<td>No action is required.</td>
</tr>
<tr class="odd">
<td>Index out of bounds</td>
<td>An application error occurred.</td>
<td>Check the application log file (or VistA error log file) for details and log a VA Remedy support call.</td>
</tr>
<tr class="even">
<td>Out of memory</td>
<td>The most likely problem is that either the system ran out of memory and prevented the task from continuing or the system disk drive ran out of space.</td>
<td>Verify that there is enough system memory/disk space for the operation before logging a VA Remedy support call.</td>
</tr>
<tr class="odd">
<td><p>Set image IEN <em>#IEN</em> with new</p>
<p><em>#IEN2</em> reference '</p></td>
<td>The file was copied and a 2005 VistA update was done to match the new location.</td>
<td>No action is required.</td>
</tr>
<tr class="even">
<td><em>Source_dir</em> directory is empty, however it could not be removed</td>
<td>An empty directory was found and it could not be deleted.</td>
<td>Check permissions on the folder.</td>
</tr>
<tr class="odd">
<td><em>Source_dir</em> directory was removed because it was empty</td>
<td>An empty directory was found and deleted.</td>
<td>No action is required.</td>
</tr>
<tr class="even">
<td><p>The source file was not found -</p>
<p><em>FilePath</em></p></td>
<td>There was no file on RAID for the pointer in VistA.</td>
<td>Run the Verifier to validate the pointers in VistA.</td>
</tr>
<tr class="odd">
<td><p>The source file was not found</p>
<p><em>source_filename</em></p></td>
<td>The source folder/file did not exist at the location specified in VistA.</td>
<td>No action is required.</td>
</tr>
<tr class="even">
<td><p>The task paused at <em>time</em> by</p>
<p><em>username</em></p></td>
<td>The Pause button was pressed. Processing has been suspended.</td>
<td>No action is required.</td>
</tr>
<tr class="odd">
<td><p>The task resumed at <em>time</em> by</p>
<p><em>username</em></p></td>
<td>The Resume button was pressed. Processing has been restarted.</td>
<td>No action is required.</td>
</tr>
</tbody>
</table>

## Viewing and Customizing MagUtility Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MagUtility generates the following types of log files for all processes:

- MagUtilityInfo.log, which stores all information and error messages. Review this log after you run any of the four processes.
- MagUtilityDebug.log, which stores error messages of a technical nature to debug all of the MagUtility processes. The information in this log is typically for developer troubleshooting.

> Each log is a running log, meaning that the results of each process run are appended to the end of the same log file. The fields are tab-delimited and the log files can be imported into Microsoft Excel.

> Opening a Log File

1.  To open a log file:
    - Within MagUtility, choose File \| Open Log.
    - Outside MagUtility, navigate to C:\Program Files\VistA\Imaging

> \MagUtility\logs and then open a log file using a text editor or spreadsheet program.

2.  Select an active (newest) or older file, as follows:
    - Active logs are named MagUtilityInfo.log and MagUtilityDebug.log.

> Note: You can open an active log file while a MagUtility process is running, but be aware that the file will not be updated with any new messages until the log file is closed (at which time, the updates will be made).

> Important: When an active log is close to its maximum configured size or retention limit, you may temporarily be prevented from opening the file until MagUtility generates new instances of the log. To re-configure its size or retention limit, see *[Re-](#_bookmark21) [Configuring the Size and Retention Limit](#_bookmark21)*.

- Older logs have a number after the \*.log extension. Lower numbers indicate newer logs, and higher numbers indicate older logs (for example, MagUtilityInfo.log.1, MagUtilityInfo.log.2, and MagUtilityInfo.log.3).

> Log File Format

> Note: Each MagUtility process that runs has a header and trailer in the log file so that you can easily locate entries for each process. For example:

> \[date/time\] \[INFO\] Offline Jukebox Selected User:IMAGPROVIDERONETWOSIX,ONETWOSIX

> The section for a particular process also ends with the name of the tab for that process. For example:

> \[date/time\] \[INFO\] Orphan Files Completed Orphan file processing.

> Each entry in MagUtilityInfo.log and MagUtilityDebug.log contains the following fields:

> \<date\> \<time\> \<level\> \<process\> \<condition/message\>

> 6/16/2009 7:11:48 AM \[INFO\] Startup Open MagUtility

> Note: If the message field is lengthy, you can widen the window to view the contents of the log file more easily.

> Sample MagUtilityInfo.log File

> The following section of the running Info log shows an example of the Orphan Files process.

![](vista-imaging-system-storage-utilities-user-manual/054.png)

> Sample MagUtilityDebug.log File

> The following section of the running Debug log shows an example of the Orphan Files process.

![](vista-imaging-system-storage-utilities-user-manual/055.png)

> Retaining and Deleting Log Files

> MagUtility writes messages to the most recently created Info and Debug log files. When a file reaches its maximum configured size, a new file is started and the existing file has “1” appended to the end of its name (for example, MagUtilityInfo.log.1). Any pre-existing logs are renamed as well, with the highest number in the filename indicating the oldest file.

> The default maximum size of any log file is 10 megabytes. The default retention limit for each type of log file is 30 instances. If there are more than 30 instances of the Debug log or Info log, the oldest instance is deleted.

> <span id="_bookmark21" class="anchor"></span>Re-Configuring the Sizeand Retention Limit

> You can change the default maximum size or retention limit for Info logs and Debug logs as needed. To re-configure the default settings:

1.  On the server where MagUtility is installed, navigate to C:\Program Files\VistA\Imaging\MagUtility.
2.  Open the logging properties file with a text editor.
    - The \#MagUtility loggers section stores settings for MagUtilityInfo.log.
    - The \#Error logger configuration section stores settings for MagUtilityDebug.log.
3.  To change the maximum number of files that are retained, locate the following field in the

> \#Maximum number of backup files section, and set the number to the value that you want.

> log4delphi.appender.MagUtilityErrorAppender.MaxBackupIndex=30

4.  To change the maximum size of a log file, locate the following field in the \#Maximum log file size section, and set the size to the value that you want.

> log4delphi.appender.MagUtilityErrorAppender.MaxFileSize=1M

5.  Save and close the file.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Archive</td>
<td>Long-term storage of data or images. A jukebox is the most common archive type presently used at sites.</td>
</tr>
<tr class="even">
<td>Cache</td>
<td>Short name for the VistA Magnetic Cache or VistA Imaging Cache, alternate terms for RAID. See <em>Raid</em>. Contrast with <em>Caché.</em></td>
</tr>
<tr class="odd">
<td>Caché</td>
<td>Commercial product name of the software used to install and set up the VistA database. Contrast with <em>Cache</em>.</td>
</tr>
<tr class="even">
<td>DICOM</td>
<td>Acronym for Digital Imaging and Communications in Medicine, a protocol for sharing and viewing medical images. DICOM has traditionally been used for radiology images, and recently has been used for images in other specialties such as cardiology, dental, gastrointestinal endoscopy, and ophthalmology.</td>
</tr>
<tr class="odd">
<td>Directory hashing</td>
<td><p>Process of storing files in multiple subdirectories based on the filename., as follows:</p>
<ul>
<li><p>If hashing is used, files are maintained in a 5-level deep subdirectory structure where no directory will contain more than 100 unique filenames with their various extensions.</p></li>
<li><p>If hashing is not used, files are placed and retrieved from the root directory of the share.</p></li>
</ul>
<p>VistA Imaging recommends using hashing.</p></td>
</tr>
<tr class="even">
<td>DiskXtender</td>
<td>Third-party data archiving software used to migrate inactive data from production storage to more cost-effective archive storage.</td>
</tr>
<tr class="odd">
<td>DX</td>
<td>Acronym for DiskXtender.</td>
</tr>
<tr class="even">
<td>File</td>
<td>In the VistA database, the equivalent of a database table, as well as a file in the generic sense.</td>
</tr>
<tr class="odd">
<td>File types</td>
<td><p>In VistA Imaging:</p>
<p>ABS = Abstract or thumbnail image file</p>
<p>BIG = Large image file that takes up a lot of storage space FULL = Full size/full resolution image file</p>
<p>TXT = Site-specific installation or setting file</p></td>
</tr>
<tr class="even">
<td>Hash</td>
<td>See <em>Directory Hashing</em>.</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Acronym for Internal Entry Number</td>
</tr>
<tr class="even">
<td>IMAGE file</td>
<td>File in the VistA database that contains entries of images</td>
</tr>
<tr class="odd">
<td><p>IMAGE AUDIT</p>
<p>file</p></td>
<td>File in the VistA database that keeps a record of any image entries that were deleted or missing. Also, used by the Verifier to ensure that a file set exists at the location(s) specified.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Image Set</td>
<td>Includes the FULL/ABS/TXT files and possibly the BIG file</td>
</tr>
<tr class="even">
<td>Imaging server</td>
<td>Server used to store the most recently acquired and accessed image files</td>
</tr>
<tr class="odd">
<td>Internal Entry Number</td>
<td>Unique record number for a specific entry in a FileMan file. Depending on the context, IENs can serve as identifiers for an image set, a single site, or other unique records in files in the VistA database.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td>Acronym for Information Resources Management, the Imaging support staff at a VA hospital</td>
</tr>
<tr class="odd">
<td>Jukebox</td>
<td>Long-term storage device in VistA that holds multiple optical discs or platters and can load and unload them as needed. Also called Archive.</td>
</tr>
<tr class="even">
<td>Magnetic cache</td>
<td>Same term as RAID. See <em>RAID</em>.</td>
</tr>
<tr class="odd">
<td>Namespace</td>
<td>First three characters of the 14-character name given to image files captured at a site. Each VHA facility has its own unique 3-character namespace.</td>
</tr>
<tr class="even">
<td>Offline</td>
<td>VistA Imaging shares designation used to isolate shares from auto- write candidacy and the purge function.</td>
</tr>
<tr class="odd">
<td>Online</td>
<td>Connected to, served by, or available through a system and especially a computer or telecommunications system (as the Internet).</td>
</tr>
<tr class="even">
<td>PACS</td>
<td>Acronym for Picture Archiving and Communication System. If a site has integrated a commercially available PACS with VistA Imaging, images from that PACS are treated in a manner similar to images produced by modalities such as a CT or MR.</td>
</tr>
<tr class="odd">
<td>Pointer</td>
<td>Reference to a RAID pointer used generically to indicate the RAID storage location referenced in the IMAGE file (#2005).</td>
</tr>
<tr class="even">
<td><p>RAID or RAID</p>
<p>shares</p></td>
<td>Acronym for Redundant Array of Inexpensive Disks, the primary storage area for recently acquired and recently accessed clinical images. Also the term used to identify a specific type of Network Location defined using the Background Processor Queue Manager.</td>
</tr>
<tr class="odd">
<td>Referenced network files</td>
<td>Image file pointers to the network locations of each of the file types stored within the VistA Imaging System.</td>
</tr>
<tr class="even">
<td>RPCs</td>
<td>Acronym for Remote Procedure Calls</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td><p>Short name for the VA Kernel RPC Broker, the Client-Server interface component. RPC Broker 1.1 is required for interfacing with</p>
<p>the hospital database.</p></td>
</tr>
<tr class="even">
<td>Site Parameters</td>
<td>A set of specifications that is configurable to meet the individual needs of each VistA Imaging System implementation.</td>
</tr>
<tr class="odd">
<td>UID</td>
<td>Acronym for Unique Identifier referring to the DICOM UID, which groups images into a series</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UNC</td>
<td><p>Acronym for Universal Naming Convention indicated by the format</p>
<p><u>\\SERVER\SHARE</u>NAME</p></td>
</tr>
<tr class="even">
<td>Veterans Health Information System Technology Architecture</td>
<td>VistA is built on a client-server architecture, which ties together workstations and personal computers with graphical user interfaces at Veterans Health Administration (VHA) facilities, as well as software developed by local medical facility staff.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Acronym for Veterans Health Information System Technology Architecture</td>
</tr>
<tr class="even">
<td>VistA Imaging Cache</td>
<td>Also called VistA Magnetic Cache, an alternative term for RAID. See <em>RAID</em>. Contrast with <em>Caché</em>.</td>
</tr>
<tr class="odd">
<td>VistA Imaging shares</td>
<td>Same as VistA Imaging Cache. Contrast with <em>Caché.</em></td>
</tr>
<tr class="even">
<td>VMC</td>
<td>Acronym for VistA Magnetic Cache, an alternative term for RAID. See <em>RAID</em>. Contrast with <em>Caché.</em></td>
</tr>
<tr class="odd">
<td>Win32</td>
<td>The set Microsoft Windows operating systems internal function calls which support all operating system activity.</td>
</tr>
<tr class="even">
<td>WORM</td>
<td>Acronym for Write Once Read Many.</td>
</tr>
<tr class="odd">
<td>Write Once Read Many</td>
<td><p>Once written to the disc, data is only available for reading and cannot be altered. Jukeboxes should be:</p>
<ul>
<li><p>WORM-DG for Data General Jukeboxes under OpenNetware</p></li>
<li><p>WORM-PDT for Pegasus Jukeboxes</p></li>
<li><p>WORM-OTG for OTG DiskXtender</p></li>
</ul>
<p><strong>Note</strong>: WORM-DG and WORM-PDT are for backward compatibility only.</p></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### .

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> .NET Framework 2.0 · 5, 6

### A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ABS files · 33
> Ad Hoc processing · 26

### B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BIG files · 33
> BIG MAGNETIC PATH field (#2005,102) · 33

### C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Compaction · 5, 8, 14, 21 Consolidated site configuration · 20

### D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Debug information · 30 DICOM
> Gateway, related to Date, Storage Copy process · 50 Image Num · 14
> Series Num · 14
> DISK & VOLUME, ABSTRACT field (#2005,2.1) · 33 DISK & VOLUME, MAGNETIC field (#2005,2) · 33
> DiskXtender · 5, 8, 24, 25, 42, 44
> DUPE field (#2005,13.5) · 34
> DX drive · 5, 6, 8

### H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hashed directory · 48 Hashed files · 51

### I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IMAGE AUDIT file (#2005.1) · 32, 47
> IMAGE file (#2005)
> description of updates in MagKat · 13 related to IENs updated in MagKat · 29 related to Network Location Cleanup · 47 related to orphan files · 32
> related to RAID pointers · 33
> related to references, Storage Copy process · 35, 52 related to referencing TXT files · 33
> related to the Network Location Cleanup · 46 related to the Storage Copy process · 48 required in MagUtility · 31
> text file flagged as offline · 25 text files copied to · 24
> verifying IENS in an Orphan Files check · 37 IMAGE FILE TYPES file (#2005.021) · 32, 34, 40
> IQ field (#2005,13) · 34

### J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Jukebox platters
> color code legend · 8 compaction · 8 Detail report · 6
> generating reports · 8 pausing a scan · 23 Platter Detail report · 11 preparation · 8
> processing · 21 reviewing shares · *7*
> save location for reports · 8 scanning · 22
> status
> forcing into processed · 26 offline error · 25
> offline unprocessed · 24
> online scanned, needs review · 25 processed · 24
> Summary report · 5, 9

### L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Log files
> format in MagUtility · 56 MagKatError.log file · 29 MagKatImageComplete.log file · 29 MagKatInfo.log file · 30 MagUtilityDebug.log file · 55 MagUtilityInfo.log file · 55
> reconfiguring size, retention limit in MagUtility · 57 retaining and deleting in MagUtility · 57

### M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG DOD FIX security key · 13, 16 MAG JB OFFLINE menu option · 24, 42
> MAG UTILITY secondary menu option · 32 MagDexter
> description · 5
> installing · 6 log file · 11
> requirements · 5 setting up · 6 starting · 8
> window · 8
> MagDexterSetup.msi · 6 MagKat
> description · 13 failed files · 20 how it works · 14 installing · 15
> requirements · 13
> starting · 16
> window · 17
> MagKat Platter Processing report · 28 MagKatError.log file · 20, 29
> MagKatImageComplete.log · 20
> MagKatImageComplete.log file · 20, 29 MagKatInfo.log file · 30 MagKatInstall.exe · 15
> Magnetic storage · *See* RAID shares MAGNETIC storage class · 46 MagUtility
> description · 31 how it works · 32
> problems corrected and not corrected · 33 requirements · 31
> starting · 35
> window description · 36 MagUtilityDebug.log file · 55 MagUtilityInfo.log file · 55 Media Files report · 42 Media label of a platter · 28

### N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Network Location Cleanup process description · 35
> running · 46
> troubleshooting · 47
> NETWORK LOCATION file (#2005.2) · 31

### O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Offline Error platter status · 10 OFFLINE IMAGES file (#2006.033) · 44
> Offline Jukebox Images process description · 35, 42
> marking images offline · 42 troubleshooting · 45
> Offline platter status · 10 Online platter status · 10 Orphan file, description · 32 Orphan Files process
> description · 32 pointer logic · 33 processing logic · 33 running · 37
> scanning · 38
> troubleshooting · 40

### P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Platter Detail report · 11 Platter Summary report · 10

### R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> RAID shares description · 19
> processing · 19 Read-only shares · 14
> Recent Error Count area · 23 Removing
> files marked offline · 44 network locations · 46 orphan files · 38
> platters to create free slots · 42 source files · 52
> Reports
> MagKat Platter Processing report · 28 Media Files report · 42
> Platter Detail report · 11 Platter Summary report · 10
> Resume scanning · 27 RPC Broker · 15

### S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security keys
> MAG DOD FIX · 13, 16
> Serial number of a platter · 28
> SET CONTEXT FOR MAGKAT RPCS \[MAGKAT\] secondary
> menu option · 13, 16 Skipped files
> jukebox processing · 21 RAID processing · 20 rescanning · 26
> Storage Copy process description · 35
> running · 48
> troubleshooting · 54
> System Impact Throttle box · 18, 19

### T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Text files
> processing · 19
> reprocessing · 20
> re-scanning · 26 Troubleshooting
> Network Location Cleanup process · 47
> SOP Instance · 15 Study Instance · 14
> UNC path · 9
> Un-hashed network shares · 9
> Offline Jukebox Images process · 45
> Orphan Files process · 40 Storage Copy process · 54

### U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> UID
> DICOM series · 13 PACS · 14
> Series · 14
> Series Instance · 14
> *V*
> Verifier, running before the Orphan Files process · 37 VistARad · 13

### W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> WORM-OTG storage class · 46
