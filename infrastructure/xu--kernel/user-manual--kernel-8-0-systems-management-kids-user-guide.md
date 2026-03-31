---
title: "Kernel 8.0 Systems Management: KIDS User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: KIDS"
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
  - span
  - install
  - distribution
  - transport
  - installation
  - kids
  - build
  - global
  - class
  - package
page_count: 0
word_count: 11400
section_count: 21
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Kernel Installation and Distribution System (KIDS)  
  User Guide
---

![](kernel-8-0-systems-management-kids-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-kids-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref507515010" class="anchor"></span>Table 1: KIDS-related Terms and Definitions</p></caption>
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
<td>08/31/2025</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>07/25/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<p>Updated external document links to open documents in a new window.</p></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Kernel Installation and Distribution System (KIDS) User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref507515010" class="anchor"></span>Table 1: KIDS-related Terms and Definitions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc204334664" class="anchor"></span>List of Figures

<span id="_Toc204334665" class="anchor"></span>List of Tables

[Table 1: KIDS-related Terms and Definitions [2](#_Ref507515010)](#_Ref507515010)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-systems-management-kids-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [KIDS: System Management—Installations](#kids-system-managementinstallations)
  - [KIDS Options](#kids-options)
    - [Distributions](#distributions)
    - [Installations](#installations)
  - [Build Entries and the BUILD (#9.6) File](#build-entries-and-the-build-96-file)
  - [INSTALL (#9.7) File](#install-97-file)
  - [Changes in the Role of the PACKAGE (#9.4) File](#changes-in-the-role-of-the-package-94-file)
  - [Transport Mechanism: Distributions](#transport-mechanism-distributions)
    - [Two Kinds of Distributions](#two-kinds-of-distributions)
  - [What Happens to DIFROM?](#what-happens-to-difrom)
  - [Installing Standard Distributions](#installing-standard-distributions)
    - [Installation Sequence](#installation-sequence)
    - [Installation Menu](#installation-menu)
    - [Loading a Standard Distribution](#loading-a-standard-distribution)
    - [Loading Transport Globals from a Distribution](#loading-transport-globals-from-a-distribution)
    - [Verifying Checksums in a Transport Global](#verifying-checksums-in-a-transport-global)
    - [Printing Loaded Transport Globals](#printing-loaded-transport-globals)
    - [Comparing Loaded Transport Globals to the Current System](#comparing-loaded-transport-globals-to-the-current-system)
    - [Backing Up Transport Globals](#backing-up-transport-globals)
    - [Running Installations](#running-installations)
    - [When the Installation is Queued](#when-the-installation-is-queued)
    - [Re-answering Installation Questions](#re-answering-installation-questions)
    - [Information Stored in the INSTALL (#9.7) File](#information-stored-in-the-install-97-file)
    - [Answering Installation Questions for a Distribution](#answering-installation-questions-for-a-distribution)
    - [Installation Progress](#installation-progress)
    - [Once the Installation Finishes](#once-the-installation-finishes)
    - [Restarting Aborted Installations](#restarting-aborted-installations)
    - [Recovering from an Aborted Distribution Load](#recovering-from-an-aborted-distribution-load)
  - [Installing Global Distributions](#installing-global-distributions)
  - [Purging the BUILD and INSTALL Files](#purging-the-build-and-install-files)
  - [Alpha/Beta Tracking](#alphabeta-tracking)
- [KIDS: System Management—Utilities](#kids-system-managementutilities)
  - [Build File Print Option](#build-file-print-option)
  - [Install File Print Option](#install-file-print-option)
  - [Edit Install Status Option](#edit-install-status-option)
  - [Convert Loaded Package for Redistribution Option](#convert-loaded-package-for-redistribution-option)
  - [Display Patches for a Package Option](#display-patches-for-a-package-option)
  - [Purge Build or Install Files Option](#purge-build-or-install-files-option)
    - [Versions to Retain](#versions-to-retain)
    - [Selecting Software Names for Purging](#selecting-software-names-for-purging)
    - [Purging Selected Entries](#purging-selected-entries)
    - [Reasons to Retain BUILD and INSTALL File Entries](#reasons-to-retain-build-and-install-file-entries)
  - [Rollup Patches into a Build Option](#rollup-patches-into-a-build-option)
  - [Update Routine File Option](#update-routine-file-option)
  - [Verify a Build Option](#verify-a-build-option)
  - [Verify Package Integrity Option](#verify-package-integrity-option)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Kernel Installation and Distribution System (KIDS) User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. Kernel Installation and Distribution System (KIDS) is the Kernel module used to distribute and install VistA applications and patches in the VistA/M Server environment. KIDS was introduced with Kernel 8.0. Previously, software was exported using a utility called DIFROM and installed by running INIT routines that the DIFROM utility created. KIDS is the replacement for DIFROM.
KIDS provides the following functionality:
- Distributions:
  - Create a Build Using Namespace
  - Copy Build to Build
  - Edit a Build
  - Transport a Distribution
  - Old Checksum Update from Build
  - Old Checksum Edit
  - Routine Summary List
  - Version Number Update
- Installations:
  - Load a Distribution
  - Verify Checksums in Transport Global
  - Print Transport Global
  - Compare Transport Global to Current System
  - Backup a Transport Global
  - Install Package(s)
  - Restart Install of Package(s)
  - Unload a Distribution

# KIDS: System Management—Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Installation and Distribution System (KIDS) was introduced with Kernel 8.0. Previously, software was exported using a utility called DIFROM and installed by running INIT routines that the DIFROM utility created. KIDS is the replacement for DIFROM; it introduces significant revisions to the software distribution and installation processes. This section introduces KIDS and describes some of the changes to the software export process.

<u>Table 1</u> lists the definitions that apply throughout the KIDS documentation:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Transport Global</strong></td>
<td>An exported software application, stored in a global. KIDS exports software (that is package) based on its definition in a build entry. The transport global also contains the build entry and the PACKAGE (#9.4) file entry (if any) for a given software application.</td>
</tr>
<tr class="even">
<td><strong>Build Entry</strong></td>
<td>An entry in the BUILD (#9.6) file that defines the parts of a software application to export. Also known as a build.</td>
</tr>
<tr class="odd">
<td><strong>Component</strong></td>
<td><p>An element of one of the following types:</p>
<ul>
<li><p>Template (<strong>PRINT</strong>, <strong>SORT</strong>, and <strong>INPUT</strong>)</p></li>
<li><p>Form</p></li>
<li><p>Function</p></li>
<li><p>Bulletin</p></li>
<li><p>Help Frame</p></li>
<li><p>Routine</p></li>
<li><p>Option</p></li>
<li><p>Security Key</p></li>
<li><p>Protocol</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Distribution</strong></td>
<td>A Host File Server (HFS) file containing transport globals. If a distribution contains multiple transport globals, KIDS treats them as a single installation when installing from the distribution.</td>
</tr>
<tr class="odd">
<td><strong>Package</strong></td>
<td>A cohesive set of files, data, and components that together form a set of computing activities related to a functional area (that is software).</td>
</tr>
</tbody>
</table>

## KIDS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get to the KIDS: Kernel Installation & Distribution System \[XPD MAIN\] menu (locked with the XUPROG security key) choose the Programmer Options \[XUPROG\] menu option on the Kernel Systems Manager Menu \[EVE\], as shown in <u>Figure 1</u>:

<span id="_Ref511373389" class="anchor"></span>Figure 1: KIDS Menu Options

Select Systems Manager Menu Option: <span class="mark">PROGRAMMER OPTIONS \<Enter\></span>

KIDS Kernel Installation & Distribution System ... \[XPD MAIN\]

\*\*\> Locked with XUPROG

PG Programmer mode \[XUPROGMODE\]

\*\*\> Locked with XUPROGMODE

Delete Unreferenced Options \[XQ UNREF'D OPTIONS\]

Error Processing ... \[XUERRS\]

General Parameter Tools ... \[XPAR MENU TOOLS\]

Global Block Count \[XU BLOCK COUNT\]

List Global \[XUPRGL\]

\*\*\> Locked with XUPROGMODE

Routine Tools ... \[XUPR-ROUTINE-TOOLS\]

Test an option not in your menu \[XT-OPTION TEST\]

\*\*\> Locked with XUMGR

Select Programmer Options Option: <span class="mark">KIDS \<Enter\></span> Kernel Installation & Distribution

System

Edits and Distribution ... \[XPD DISTRIBUTION MENU\]

Utilities ... \[XPD UTILITY\]

Installation ... \[XPD INSTALLATION MENU\]

\*\*\> Locked with XUPROGMODE

Patch Monitor Main Menu ... \[XTPM PATCH MONITOR MAIN MENU\]

Patchman ... \[XPD AUTOMATIC PATCHING MENU\]

As indicated by its name (that is KIDS = Kernel Installation and Distribution System), KIDS supports two major functions:

- [Distributions](#distributions)
- [Installations](#installations)

![](kernel-8-0-systems-management-kids-user-guide/004.png) REF: In addition, KIDS also provides other utilities. For more information on KIDS utilities, see the “<u>KIDS: System Management—Utilities</u>” section.

### Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The distribution related options are located on the Edits and Distribution \[XPD DISTRIBUTION MENU\] menu (see <u>Figure 2</u>). The distribution portion of KIDS allows developers to:

- Define the contents of a software application in a build entry.
- Create transport globals from build entries.
- Export transport globals by creating distributions.

<span id="_Ref86128238" class="anchor"></span>Figure 2: Edits and Distribution Menu Options

Select Kernel Installation & Distribution System Option: <span class="mark">EDITS AND DISTRIBUTION \<Enter\></span>

Create a Build Using Namespace

Copy Build to Build

Edit a Build

Transport a Distribution

Old Checksum Update from Build

Old Checksum Edit

Routine Summary List

Version Number Update

Select Edits and Distribution Option:

![](kernel-8-0-systems-management-kids-user-guide/005.png) REF: For a description on how application developers use the KIDS build and distribution options, see the [*Kernel 8.0 Developer’s Guide: KIDS Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf).

### Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation related options are located on the Installation \[XPD INSTALLATION MENU\] menu (see <u>Figure 3</u>). The installation portion of KIDS allows sites to:

- Load transport globals from KIDS distributions.
- Load transport globals from KIDS PackMan messages.
- Print out the contents of loaded transport globals before installing them.
- Compare the contents of loaded transport globals to the current system before installing them.
- Install loaded transport globals.

<span id="_Ref86128237" class="anchor"></span>Figure 3: Installation Menu Options

Select Kernel Installation & Distribution System Option: <span class="mark">INSTALLATION \<Enter\></span>

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option:

KIDS introduced two files into Kernel:

- BUILD (#9.6) file
- INSTALL (#9.7) file

KIDS also makes use of the existing PACKAGE (#9.4) file, but its role in exporting and installing software is diminished.

## Build Entries and the BUILD (#9.6) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Build entries, stored in the BUILD (#9.6) file, are where developers define a software application. This build entry defines the set of files, data, components, installation questions, national software information, pre- and post-install routines, and other settings that comprise the exported software.

Software components are no longer tied to namespace, as they were previously with DIFROM and the PACKAGE (#9.4) file. Developers can select any components available on the current system and include them in their build entries as software components.

The format of the NAME (#.01) field of a build entry *must* be the software name concatenated with a space, and then a version number. This means that there is a separate entry for every version of a software application that a developer exports.

Also, a software application’s build entry is sent to installing sites as part of the software; after an installation, the site can examine the build entry to see the software definition.

<span id="_Toc193181880" class="anchor"></span>Figure 4: KIDS File Diagram

![](kernel-8-0-systems-management-kids-user-guide/006.png)

## INSTALL (#9.7) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INSTALL (#9.7) file stores a record of each installation a site performs. The INSTALL (#9.7) file allows KIDS to store a separate installation entry for each installation. A new version of software no longer overwrites the installation information of a previous version, and developers’ installation history no longer overwrites the sites’ installation history. The national PACKAGE (#9.4) file is now static at its top level.

The three main items recorded in the INSTALL (#9.7) file for each installation are the installing site’s answers to installation questions, any installation output, and the installation’s timing information.

## Changes in the Role of the PACKAGE (#9.4) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PACKAGE (#9.4) file still plays a role in installations with KIDS, albeit a diminished one. KIDS provides a link from the build entry of a package to the PACKAGE file, so that developers can link a package to a PACKAGE (#9.4) file entry.

The top level of a PACKAGE (#9.4) file entry for a package now stores static package information. The only part of the PACKAGE (#9.4) file entry that installations update automatically now is the VERSION Multiple field. A patch sent with KIDS does *not* transport the entire PACKAGE (#9.4) file entry. It only sends the information that is needed to update the PACKAGE (#9.4) file. Patch installations update the PATCH APPLICATION HISTORY Multiple field, which is within the VERSION Multiple field. KIDS saves patch names along with their sequence numbers in this multiple. Most other fields have been designated for removal at the top level of the PACKAGE (#9.4) file. The PACKAGE (#9.4) file now stores mainly static software information that is *not* version specific, as well as the patch history of the software.

## Transport Mechanism: Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Distributions are the mechanism KIDS uses to export software. They are more flexible than the previous mechanism (INIT routines).

Distributions are usually in the form of an HFS file. The developer creates transport globals from build entries. KIDS stores transport globals in a global. KIDS can WRITE the global (in a format readable only by KIDS) to an HFS file; the HFS file is the distribution. The HFS file can then be distributed by a variety of methods, including FTP (file transfer protocol), diskette, and tape. For example, if your system is a PC, you can also move the Transport Global to a new medium (that is to multiple floppy disks so you can install on other PCs):

1.  Select the Load a Distribution \[XPD LOAD DISTRIBUTION\] option (*Do not* run the Environment Check routine).
1.  Under the Utilities \[XPD UTILITY\] menu, select the Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\] option.
2.  Under the Edits and Distribution \[XPD DISTRIBUTION MENU\] menu, select the Transport a Distribution \[XPD TRANSPORT PACKAGE\] option.
3.  At the “Enter a Host File:” prompt, enter the floppy drive and file name. For example:

Enter a Host File: <span class="mark">A:\KRN8.KID)</span>

One advantage to using distributions over INIT routines is that there is no limit to the size of a software application you can export. Another advantage is that during installations, you no longer must overwrite a software application’s existing routines with the new routines before running the installation.

Alternatively, a KIDS distribution can be sent through a PackMan message in MailMan. But transporting software as host files, especially large ones, avoids slowing down MailMan.

### Two Kinds of Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS supports two kinds of distributions:

- Standard Distribution—This type of distribution contains transport globals for what are traditionally thought of as software applications, including files, data, and all components. A standard distribution can contain one or more transport globals. If there is more than one transport global, KIDS treats each one as a single installation unit.
- Global Distribution—This type of distribution contains one transport global only, and that transport global can export M globals only.

The transport globals in both types of distributions also contain the corresponding build entry, and if linked to a PACKAGE \[#9.4\] file entry, the corresponding PACKAGE (#9.4) file entry. However, a patch sent with KIDS does *not* transport the entire PACKAGE (#9.4) file entry. It only sends the information that is needed to update the PACKAGE (#9.4) file.

## What Happens to DIFROM?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Developers should no longer use the DIFROM entry point to export software. Developers should use KIDS. The DIFROM method is still supported, but only for the support of sites that use standalone VA FileMan (VA FileMan without Kernel).

![](kernel-8-0-systems-management-kids-user-guide/007.png) REF: For more information on using DIFROM, see the *VA FileMan Developers Guide*.

## Installing Standard Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As noted previously, KIDS supports two types of distributions:

- Standard
- Global

This section describes how KIDS installations work when installing standard distributions.

### Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS installs standard distributions in three phases:

1.  Loading transport globals from the distribution.
4.  Answering installation questions for each transport global.
5.  Installing each transport global in the distribution.

#### Phase 1: Loading Transport Globals from a Distribution or PackMan Message

1.  Using the Load a Distribution \[XPD LOAD DISTRIBUTION\] option, the installer chooses the HFS file from which to load distributions. If loading from a PackMan message, choose the message and invoke MailMan’s INSTALL/CHECK MESSAGE option under the Load PackMan Message \[XMPACK\] option.
6.  For each transport global, KIDS makes an entry in the INSTALL (#9.7) file for the transport global.
7.  KIDS loads transport globals from distribution into ^XTMP.
8.  KIDS prompts the user to see if they want to run the environment check for each transport global \[if unsuccessful, the process quits here; the developer may or may *not*KILL INSTALL (#9.7) file entries and transport globals from ^XTMP\].
9.  The installer can print the contents of the transport global, compare the contents to the current system, and verify checksums of the transport global.

#### Phase 2: Answering Installation Questions for Transport Globals in a Distribution

1.  Using the Install Package(s) \[XPD INSTALL BUILD\] option, the installer selects a distribution to install by choosing an entry from the INSTALL (#9.7) file.
10. KIDS runs the environment check for the first transport global; the environment check can allow KIDS to install the transport global, cancel installation of the transport global, or cancel installation of all transport globals in the distribution.
11. The installer answers pre-installation questions for the first transport global.
12. The installer answers standard KIDS questions for the first transport global.
13. The installer answers post-installation questions for the first transport global.
14. The installer repeats Steps \#2-5 for the remaining transport globals, if there are any more transport globals to process.
15. The installer chooses a device for the installation to run on. The installer can queue the installation or run it directly; entering a caret (^) aborts the installation.

#### Phase 3: KIDS Installation of Software

1.  KIDS disables any options and protocols the site has asked to be disabled for this install. However, KIDS does *not* disable options and protocols which have an Action of USE AS LINK FOR MENU ITEMS.
16. KIDS waits for the time-period (from 0 to 60 minutes) the site specifies, if they chose to disable options and protocols.
17. KIDS suspends the running of queued options by TaskMan for this install, if the site chooses to do so.
18. The pre-install routine is run for the first transport global.
19. All components are installed for the first transport global.
20. The post-install routine is run for the first transport global.
21. KIDS repeats Steps 4-6 for any remaining transport globals to install in the distribution.
22. Options and protocols that were disabled for this install (if any) are re-enabled.
23. Queued options are removed from suspense (if the site chose to suspend queued options).

### Installation Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS Installation \[XPD INSTALLATION MENU\] menu contains the options shown in <u>Figure 5</u>:

<span id="_Ref511374675" class="anchor"></span>Figure 5: KIDS Installation Menu Options

Select Kernel Installation & Distribution System Option: <span class="mark">INSTALLATION \<Enter\></span>

\*\*\> Locked with XUPROGMODE

1 Load a Distribution \[XPD LOAD DISTRIBUTION\]

2 Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\]

3 Print Transport Global \[XPD PRINT INSTALL\]

4 Compare Transport Global to Current System \[XPD COMPARE TO SYSTEM\]

5 Backup a Transport Global \[XPD BACKUP\]

6 Install Package(s) \[XPD INSTALL BUILD\]

Restart Install of Package(s) \[XPD RESTART INSTALL\]

Unload a Distribution \[XPD UNLOAD DISTRIBUTION\]

The number next to the options indicates the order of the option entries you should follow when performing a KIDS installation.

### Loading a Standard Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step in installing a standard distribution is to load the transport globals from the distribution. The Load a Distribution \[XPD LOAD DISTRIBUTION\] option does the following:

- Lists what transport globals are contained in the distribution and asks you if you want to continue.
- Creates entries in the INSTALL (#9.7) file for each transport global in the distribution that passed its environment check.
- Loads transport globals from the distribution (HFS file) into the ^XTMP global (if you answer YES to continue).
- Prompts the user to see if they want to run the environment check for each transport global. If a transport global does *not* pass its environment check, KIDS may purge it from ^XTMP; otherwise, the transport global stays in ^XTMP. KIDS tells you the result of each environment check.
- Checks the version number of the incoming software against any existing software of the same name at the site. If the incoming version number is *not* greater than the existing version, KIDS aborts the installation for the transport global in question.
- Echoes the name of the first transport global to pass environment check (that is “Use transport global name to install this Distribution”). The name of the first transport global to pass its environment check is the name you use to install the distribution, in the next phase.

Loading a distribution is the first of three phases to install VistA software. The second phase is answering installation questions, including scheduling the installation; the third and final phase is the actual running of the installation.

When loading from a PackMan message, load the distribution using MailMan’s INSTALL/CHECK MESSAGE option under the Load PackMan Message \[XMPACK\] option. For KIDS PackMan messages, this option through MailMan is equivalent to the Load a Distribution \[XPD LOAD DISTRIBUTION\] option.

<span id="_Ref86049783" class="anchor"></span>Figure 6: Load a Distribution Option—Sample User Dialog

Select Installation Option: <span class="mark">LOAD A DISTRIBUTION \<Enter\></span>

Enter a Host File: <span class="mark">ZXG_EXPT.DAT \<Enter\></span>

Distribution saved on Oct 13, 2004@09:29:08

Comment: TEST PKGS

This Distribution contains Transport Globals for the following Package(s):

TEST 2.1

Want to Continue with Load? YES// <span class="mark">\<Enter\></span>

Loading Distribution...

Want to RUN the Environment Check Routine? YES// <span class="mark">\<Enter\></span>

TEST 2.1

Use INSTALL NAME: TEST 2.1 to install this Distribution.

Select Installation Option:

#### When the Distribution is Split across Diskettes

Distributions can come in a single host file (see <u>Figure 6</u>); alternatively, they can come on diskettes, with the host file split up among the diskettes. If you are installing from a distribution that is spread across diskettes, the Load a Distribution \[XPD LOAD DISTRIBUTION\] option asks you for subsequent diskettes (such as “Insert the next diskette, \#2, and Press the return key”, and so on). Insert the appropriate disk, press the \<Enter\> key, and continue until the distribution is loaded.

### Loading Transport Globals from a Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181883" class="anchor"></span>Figure 7: Loading Transport Globals from a Distribution—Flowchart

![](kernel-8-0-systems-management-kids-user-guide/008.png)

### Verifying Checksums in a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can verify the checksums for a loaded transport global in advance of installing from it, using the Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\] option. This option verifies all checksums of routines in the transport global, reporting any discrepancies. In the future, the ability to verify checksums will be extended to other KIDS components besides routines.

As of Kernel patch XU\*8.0\*369, the integrity checking CHECK1^XTSUMBLD routine supports the Compare local/national checksums report \[XU CHECKSUM REPORT\] option.

As of Kernel patch XU\*8.0\*393, KIDS was modified to send a message to a server on FORUM when a KIDS build is sent to a Host File Server (HFS) device. This message contains the checksums for the routines in the patch. The server on FORUM matches the message with a patch if the sending domain is authorized on FORUM. There is no longer a need for developers to manually include routine checksums (either CHECK^XTSUMBLD or CHECK1^XTSUMBLD routines) in the patch description. The patch module includes the before and after CHECK1^XTSUMBLD values in the “Routine Information” section at the end of the patch document.

With changes in the National Patch Module (NPM) on FORUM, when the patch is released the checksums for the routines are moved to the ROUTINE (#9.8) file on FORUM. The checksum “before” values come from the FORUM ROUTINE (#9.8) file and are considered the GOLD standard for released checksums. The local site’s Compare local/national checksums report \[XU CHECKSUM REPORT\] option uses the FORUM ROUTINE (#9.8) file as its source to create reports showing any routines that do *not* match.

This patch also modified the KIDS BUILD (#9.6) file by adding the TRANSPORT BUILD NUMBER (#63) field used to store a build number that is incremented each time a build is made. This build number is added to the second line of each routine in the 7th “;” piece. This makes it easy to tell if a site is running the current release during testing and afterword. The leading “B” found in the checksum tells the code what checksum routine to use.

### Printing Loaded Transport Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have loaded transport globals from a standard distribution onto your system, you can print out the definitions of the transport globals, using the Print Transport Global \[XPD PRINT INSTALL\] option. This way, you can see every component exported in each transport global, before you install them.

<span id="_Toc193181884" class="anchor"></span>Figure 8: Print Transport Global Option—Sample Printed Transport Global

PACKAGE: ZXG DEMO 1.0 PAGE 1

----------------------------------------------------------------------------

NATIONAL PACKAGE:

DESCRIPTION:

ENVIRONMENT CHECK : ZXGENV

PRE-INIT ROUTINE : ZXGPRE

POST-INIT ROUTINE: ZXGPOS

----------------------------------------------------------------------------

ROUTINE:

ZXGC00 SEND TO SITE

ZXGC01 SEND TO SITE

ZXGC02 SEND TO SITE

ZXGCMOVE SEND TO SITE

ZXGCTEST SEND TO SITE

ZXGCTW1 SEND TO SITE

ZXGCWE SEND TO SITE

ZXGCXMP1 SEND TO SITE

ZXGCXMPL SEND TO SITE

ZXGDEMO SEND TO SITE

ZXGKC SEND TO SITE

ZXGLMSG SEND TO SITE

ZXGLOAD SEND TO SITE

ZXGTMP SEND TO SITE

INSTALL QUESTIONS:

SUBSCRIPT: PRE1

DIR(0)=YA^^

DIR("A")=Do you want to run the pre-install conversion?

DIR("B")=YES

DIR("?")=Answer YES to run the pre-install conversion, NO to skip it...

### Comparing Loaded Transport Globals to the Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you have loaded transport globals from a standard distribution onto your system, you can also compare a transport global to the matching software already installed on your system (if any), using the Compare Transport Global to Current System \[XPD COMPARE TO SYSTEM\] option. This way, you can compare the software you are about to install with the current version of the software on your system.

When this option finds differences, it notes the change by displaying the differences between the current software and the transport global on two lines, labeled as follows:

- \* OLD \*
- \* NEW \*

![](kernel-8-0-systems-management-kids-user-guide/009.png) NOTE: Pointers are converted to FREE TEXT when exporting VA FileMan entries, so these converted free pointers show up as differences when using the compare feature.

<span id="_Toc193181885" class="anchor"></span>Figure 9: Compare Transport Global to Current System Option—Sample Comparison Output

Compare ZXP 1.0 to current site

-------------------------------------------------------------------

Routine: ZUVXD

File \# 3.2 Data Dictionary

File \# 3.2 Data

\* OLD \* ^%ZIS(2,9,8) = \$C(27)\_"\[A"^\$C(27)\_"\[B"^\$C(27)\_"\[C"^\$C(27)\_"\[D"^3^^\$C(27)\_"\[L"

\* NEW \* ^%ZIS(2,9,8) = \$C(27)\_"\[A"^\$C(27)\_"\[B"^\$C(27)\_"\[C"^\$C(27)\_"\[D"^3

\* OLD \* ^%ZIS(2,44,13) = ^\$C(26)^^^^\$J("",X)\_\$C(27,93,(\$X+32-X))

\* NEW \* ^%ZIS(2,44,13) = ^\$C(26)^^^^

\* OLD \* ^%ZIS(2,60,8) = \$C(27)\_"\[A"^\$C(27)\_"\[B"^\$C(27)\_"\[C"^\$C(27)\_"\[D"^3^^\$C(27)\_"\[L"

\* NEW \* ^%ZIS(2,60,8) = \$C(27)\_"\[A"^\$C(27)\_"\[B"^\$C(27)\_"\[C"^\$C(27)\_"\[D"^3

\* ADD \* ^%ZIS(2,93,21) = ^

HELP FRAME

BULLETIN

This option was updated with Kernel patch XU\*8.0\*393 to add a side-by-side comparison in columnar format, which only works if Kernel Toolkit patch XT\*7.3\*93 has also been installed, as shown in <u>Figure 10</u>:

<span id="_Ref29372579" class="anchor"></span>Figure 10: Compare Transport Global to Current System Option—Sample Comparison Output in Columnar Format

Select Kernel Installation & Distribution System Option:

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <span class="mark">4 \<Enter\></span> Compare Transport Global to Current System

Select INSTALL NAME: <span class="mark">XU\*8.0\*381 \<Enter\></span> Loaded from Distribution

Loaded from Distribution 9/14/06@12:39:52

=\> DEMO COMPARE  ;Created on Sep 14, 2006@12:39:17

This Distribution was loaded on Sep 14, 2006@12:39:52 with header of

DEMO COMPARE  ;Created on Sep 14, 2006@12:39:17

It consisted of the following Install(s): XU\*8.0\*381

Select one of the following:

1 Full Comparison

2 Second line of Routines only

3 Routines only

4 Columnar Routine compare

Type of Compare: <span class="mark">4 \<Enter\></span> Columnar Routine compare

DEVICE: HOME// <span class="mark">\<Enter\></span> Telnet terminal

Compare XU\*8.0\*381 to current site Routines Only

--------------------------------------------------------------------------

Compare of routines from KIDS XU\*8.0\*381, and disk

Routine XU8P381 not on disk

--------------------------------------------------------------------------

Routine XUTMTP

KIDS Disk

--------------------------------------------------------------------------

1{XUTMTP ;SEA/RDS - TaskMan:ToolKit} 1{XUTMTP ;SEA/RDS - TaskMan: ToolKit}

 {, Print, Part 1 ;04/18/2006 16:19} {, Print, Part 1 ;04/24/2003  11:06}

                        ^                                       ^

2{ ;;8.0;KERNEL;\*\*20,86,169,242,381\*}2{ ;;8.0;KERNEL;\*\*20,86,169,242\*\*;Ju}

                                ^                                       ^

--------------------------------------------------------------------------

### Backing Up Transport Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Backup a Transport Global \[XPD BACKUP\] option allows the user to back up just the routines or create a backup build of all parts of a patch. It copies all the existing files, fields, routines, and components that are updated by the patch into a backup build. The result is a MailMan message or a Host file that can be installed and restores your system back to a state before the patch.

<span id="_Ref67900662" class="anchor"></span>Figure 11: Backup a Transport Global——Sample System Prompts and User Entries

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">BACKUP A TRANSPORT GLOBAL \<Enter\></span>

Select INSTALL NAME: <span class="mark">XT\*7.3\*147 \<Enter\></span> Loaded from Distribution 7/27/20@13:32

:07

=\> XT\*7.3\*147 TEST v1

This Distribution was loaded on Jul 27, 2020@13:32:07 with header of

XT\*7.3\*147 TEST v1

It consisted of the following Install(s):

XT\*7.3\*147

Subject: Backup of XT\*7.3\*147 on Feb 12, 2021  Replace

Select one of the following:

          B         Build (including Routines)

          R         Routines Only

Backup Type: B// <span class="mark">? \<Enter\></span>

Backup the entire Build(routines, files, options, protocols, templates,

etc.) or just the Routines.

Select one of the following:

          B         Build (including Routines)

          R         Routines Only

Backup Type: B// <span class="mark">?? \<Enter\></span>

Enter 'B' to create a backup of this Build. A new Build will be created using

the same Build name with a 'b' appended to the end. This new Build will be used

to create a KIDS backup of routines, files, options, protocols, templates, etc.

If this backup is a single build, a Packman email is created.  If it is a multi-

package a Host File is created.

Enter 'R' to create a Packman email of only the routines.

Select one of the following:

          B         Build (including Routines)

          R         Routines Only

Backup Type: B// <span class="mark">\<Enter\></span> uild (including Routines)

Created by XUUSER,ONE at *\<REDACTED\>*.VA.GOV  (KIDS) on Friday,

02/12/21 at 08:43

Do you wish to secure this message? NO// <span class="mark">\<Enter\></span>

Send mail to: XUUSER,ONE // <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Message sent

### Running Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have loaded the transport globals from a standard distribution, you can install them. Do this using the Install Package(s) \[XPD INSTALL BUILD\] option.

When you load a distribution, KIDS tells you which transport global name to use to install the distribution (such as “Use PACKAGE 1.0 to install this Distribution”). This is always the first transport global to successfully load from the distribution. When you use the Install Package(s) \[XPD INSTALL BUILD\] option, select the transport global name reported when you loaded the original distribution. Once you’ve done that, you can answer the installation questions for each transport global in the distribution.

#### Processing Each Transport Global

When you select a distribution to install, the Install Package(s) \[XPD INSTALL BUILD\] option processes the installation questions for each transport global in the distribution. For each transport global, you are asked:

- Pre-Install questions.
- Standard KIDS Questions.
- Post-Install Questions.
- Whether to disable any options or protocols. By typing three question marks (???) at this prompt KIDS lists all the options and protocols it will disable. If you answer YES, all incoming options and protocols are disabled. You are also prompted to add to or delete from the list of options and protocols to disable. However, KIDS does *not* disable options and protocols that have an Action of USE AS LINK FOR MENU ITEMS. All scheduled options on the system are also disabled.

Finally, you are asked a time-period for installation:

Delay Install(Minutes): (0-60): 0//"

You can delay before starting the installation after disabling options and protocols from 0 to 60 minutes. This is to allow users already in (disabled) options time to exit the options before the installation starts.

#### Scheduling Installations

The final question you are asked when using the Install Package(s) \[XPD INSTALL BUILD\] option to load software is upon what device to run the installation. Your choices at the “DEVICE:” prompt are:

- Run the installation directly by selecting a device without queueing. The installation runs immediately on the device you specify.
- Queue the installation.
- Abort the installation of the distribution by entering a caret (^).

### When the Installation is Queued

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can cancel a queued installation (before it has started) by deleting the task. KIDS also allows you to restart an install if the install is queued and you get an error during the installation.

If you queued the installation, you could look up the installation task in TaskMan. A KIDS installation task looks like <u>Figure 12</u>:

<span id="_Ref67478156" class="anchor"></span>Figure 12: Queued KIDS Installation—Sample Installation Task

3: (Task \#1179950) EN^XPDIJ, KIDS install. Device VER\$LW. KRN,KDE.

From TODAY at 16:24, By you. Scheduled for TODAY at 22:00

You can cancel a queued installation (before it has started) by deleting the task. KIDS also allows you to restart an install if the install is queued and you get an error during the installation.

### Re-answering Installation Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you queued an installation, you can re-answer installation questions using the Install Package(s) \[XPD INSTALL BUILD\] option. To be able to re-answer the questions, however, you need to locate the task that was queued for the installation and delete it first. Once you delete the installation’s queued task, you can re-answer the install questions. When you re-answer questions, your answers from the previous time come up as default responses.

Also, if you abort an installation after answering its installation questions (that is by entering a caret \[^\]), your responses are again used as the defaults the next time you try to install.

### Information Stored in the INSTALL (#9.7) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS exports the definition of a software application in the BUILD (#9.6) file. KIDS records installations of software in the INSTALL (#9.7) file. The installation records in the INSTALL (#9.7) file provide a record of the start time, timing for each checkpoint, and completion time (if any) for an installation.

When an installation aborts, the contents of the INSTALL (#9.7) file determine where the install starts up again when you use the Restart Install of Package(s) \[XPD RESTART INSTALL\] option (checkpoint information is stored in the INSTALL \[#9.7\] file).

As well as being sent to the installation’s principal device, all output from the installation is also stored in the INSTALL (#9.7) file, in the MESSAGES word-processing-type field.

The installation questions (and your answers to them) are stored in the INSTALL ANSWERS (#50) Multiple field of the INSTALL (#9.7) file.

You can print entries from the INSTALL (#9.7) file with the Install File Print \[XPD PRINT\] option.

### Answering Installation Questions for a Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181888" class="anchor"></span>Figure 13: Answering Installation Questions for a Distribution—Flowchart

![](kernel-8-0-systems-management-kids-user-guide/010.png)

### Installation Progress

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the device selected for output is a VT100-compatible (or higher) terminal, KIDS displays the installation output in a virtual window on the terminal. Below the virtual window, a progress bar graphically illustrates the percentage complete that the current part of the installation has reached. KIDS can report progress for the installation of files and for all components (PRINT templates, forms, help frames, routines, options, and so on). KIDS lists those compiled cross-references, INPUT templates, and PRINT templates that were created during the install process. KIDS does *not* show progress for installing data, nor for pre- and post-install tasks.

On all other devices, progress is reported using dots.

<span id="_Ref20112533" class="anchor"></span>Figure 14: Installation Progress—Sample Output

![](kernel-8-0-systems-management-kids-user-guide/011.png)

### Once the Installation Finishes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the installation runs, its output is sent to the device you specified when you answered the installation questions. If, for example, you queued the installation to a printer, the output is sent to the printer.

You can find out whether an installation finished by looking up the entry in the INSTALL (#9.7) file for that installation (use the Install File Print \[XPD PRINT\] option). You should check whether an installation completed successfully or not:

- If the install completed successfully, the STATUS (#.02) field in the INSTALL (#9.7) file entry is set to “Install Completed.”
- If the install errored out, the STATUS (#.02) field in the INSTALL (#9.7) file entry is still set to “Install Started.” If it errored out, you need to find out what went wrong and restart the installation.

![](kernel-8-0-systems-management-kids-user-guide/012.png) REF: For information on restarting an installation, see the “[Restarting Aborted Installation](#restarting-aborted-installations)” section.

If you disabled scheduled options, options, and protocols, KIDS should have re-enabled those (unless the install errored out).

You should refer to the instructions that came with the software you installed to see what post-installation tasks, if any, you should perform.

### Restarting Aborted Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A feature of KIDS is the ability to restart an aborted installation. KIDS uses a checkpoint system to keep track of how many phases of an installation it completed. When an installation aborts for some reason, you can restart the installation (using the Restart Install of Package(s) \[XPD RESTART INSTALL\] option). KIDS does *not* automatically re-run the entire installation from the beginning; instead, it re-runs the installation only from the last completed checkpoint.

As well as some standard checkpoints built into KIDS (such as completion of pre-install, completion of each component type, and completion of post-install), KIDS lets developers create checkpoints for use within their pre- and post-install routines. So, depending on how the developer has designed a pre- or post-install, it is possible that, when re-started, the pre- or post-install does *not* have to be re-run in its entirety either (if the error occurred there). Instead, KIDS only re-runs the pre- or post-install from the last completed developer checkpoint (if any) within the pre- or post-install.

Before restarting an installation, you should try to determine what caused the installation to abort. If an error occurred, any error messages are in the INSTALL (#9.7) file entry, in the MESSAGES WORD-PROCESSING-type field. Once you have fixed the problem, you can use the Restart Install Of Package(s) \[XPD RESTART INSTALL\] option to continue with the installation. KIDS also allows you to restart an install if the install is queued and you get an error during the installation.

### Recovering from an Aborted Distribution Load

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you encounter an error while loading a distribution (using KIDS’ Load a Distribution \[XPD LOAD DISTRIBUTION\] option from the export medium into the ^XTMP global), you are unable to re-load the distribution until you clear out what was stored during the aborted load attempt.

To clear out the previously loaded distribution, use the Unload a Distribution \[XPD UNLOAD DISTRIBUTION\] option. To unload a distribution, enter the name of the *first* transport global that was loaded when you loaded the distribution. The entries in the INSTALL (#9.7) file for all transport globals in the distribution are removed, and the transport globals themselves are purged from the ^XTMP global.

Once you delete entries in the INSTALL (#9.7) file and entries in the ^XTMP global with the Unload a Distribution \[XPD UNLOAD DISTRIBUTION\] option, you should be able to reload the distribution in question. If the install was already started and you choose to unload the distribution, you first *must* edit the INSTALL (#9.7) file and set the STATUS (#.02) field to Loaded From Distribution (that is 0) prior to using the Unload a Distribution \[XPD UNLOAD DISTRIBUTION\] option.

## Installing Global Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second type of distribution supported by KIDS is called a global distribution. This type of distribution, unlike standard distributions, is used to only export globals.

You still use the Load a Distribution \[XPD LOAD DISTRIBUTION\] option to install global distributions. Unlike loading a standard distribution, however, KIDS installs global distributions immediately from the Load a Distribution \[XPD LOAD DISTRIBUTION\] option. Also, there is no queueing of the installation.

A global distribution can only contain one transport global, and the transport global can only export globals. You know that the distribution you’re installing is a global distribution rather than a standard distribution, because when you load it with the Load a Distribution \[XPD LOAD DISTRIBUTION\] option, KIDS displays the message shown in <u>Figure 15</u>:

<span id="_Ref511376957" class="anchor"></span>Figure 15: KIDS Global Distribution—Sample Message

This is a Global Distribution. It contains Global(s) that will

update your system at this time. The following Global(s) will be installed:

The Load a Distribution \[XPD LOAD DISTRIBUTION\] option lists each global that will be installed from the distribution. Each global in the list is marked OVERWRITE or REPLACE:

- OVERWRITE—Load the global *without* purging the site’s version of the global beforehand.
- REPLACE—Purge the site’s version of the global first and then load the global.

You are given two chances to abort the installation of the global distribution. If you answer YES to both questions, the globals in the global distribution are installed immediately.

## Purging the BUILD and INSTALL Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each KIDS installation adds one entry to the BUILD (#9.6) and INSTALL (#9.7) files; for every transport global installed from the distribution.

![](kernel-8-0-systems-management-kids-user-guide/013.png) REF: For information about purging these files, see the discussion of the Purge Build or Install Files option in the “[Purge Build or Install Files](#purge-build-or-install-files-option)” section in the “<u>KIDS: System Management—Utilities</u>” section.

<span id="_Toc193181891" class="anchor"></span>Figure 16: Installation of a Global Distribution—Load a Distribution Option

Select Installation Option: <span class="mark">LOAD A DISTRIBUTION \<Enter\></span>

Enter a Host File: <span class="mark">\[DMANAGER\]XGGLOBAL.DAT \<Enter\></span>

KIDS Distribution save on Jan 26, 2004@12:58:25

Comment: GLOBAL PACKAGE

This Distribution contains the following Transport global(s):

GLOBAL PACKAGE 1.0

This is a Global Distribution. It contains Global(s) that will

update your system at this time. The following Global(s) will be installed:

^XGRON(1) Overwrite

^XGRON("PX") Replace

^XGRON("TX") Overwrite

If you continue with the Load, the Global(s) will be

Installed at this time.

Want to Continue with Load? YES// <span class="mark">\<Enter\></span>

Loading Distribution...

Globals will now be installed, OK? YES// <span class="mark">\<Enter\></span>

Installing Globals...

Jan 26, 2004@13:04:16

GLOBAL PACKAGE 1.0 Installed.

Jan 26, 2004@13:04:17

Select Installation Option:

## Alpha/Beta Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides a mechanism for tracking and monitoring installation and option usage during the alpha and beta testing phases of VistA software applications. This tool is primarily intended for application developers to use in monitoring the testing process at local test sites.

![](kernel-8-0-systems-management-kids-user-guide/014.png) NOTE: In VA terminology “Alpha” and “Beta” testing are defined as follows:

- Alpha Testing—VistA test software application is running in a site’s Test account.
- Beta Testing—VistA test software application is running in a site’s Production account.

Alpha/Beta Tracking provides the following services to both developers and system administrators:

- Notification when a new alpha or beta software version is installed at a site.
- Periodic option usage reports for alpha or beta options being tracked.
- Periodic listings of errors in the software’s namespace that are currently in alpha or beta test at the site.

The following options are provided on the Alpha/Beta Test Option Usage Menu \[XQAB MENU\], which is located on the Operations Management \[XUSITEMGR\] menu. These options allow developers and system administrators to monitor Alpha/Beta Tracking at a site:

- Errors Logged in Alpha/Beta Test (QUEUED) \[XQAB ERROR LOG XMIT\] option
- Actual Usage of Alpha/Beta Test Options \[XQAB ACTUAL OPTION USAGE\] option
- Low Usage of Alpha/Beta Test Options \[XQAB LIST LOW USAGE OPT\] option
- Print Alpha/Beta Errors (Date/Site/Num/Rou/Err) \[XQAB ERR DATE/SITE/NUM/ROU/ERR\] option
- Send Alpha/Beta Usage to Programmers \[XQAB AUTO SEND\] option

![](kernel-8-0-systems-management-kids-user-guide/015.png) REF: For more detailed information about and description of the Alpha/Beta Tracking functionality (such as starting, stopping, and monitoring options), see the “Alpha/Beta Tracking” section in the [*Kernel 8.0 Developer’s Guide: KIDS Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf#Alpha_Beta_Tracking).

# KIDS: System Management—Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS provides the following Utilities \[XPD UTILITY\] menu options shown in <u>Figure 17</u>:

<span id="_Ref511377455" class="anchor"></span>Figure 17: KIDS Utilities Menu Options

Kernel Installation and Distribution System... \[XPD MAIN\]

Utilities... \[XPD UTILITY\]

Build File Print \[XPD PRINT BUILD\]

Install File Print \[XPD PRINT INSTALL FILE\]

Edit Install Status \[XPD EDIT INSTALL\]

Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\]

Display Patches for a Package \[XPD PRINT PACKAGE PATCHES\]

Purge Build or Install Files \[XPD PURGE FILE\]

Rollup Patches into a Build \[XPD ROLLUP PATCHES\]

Update Routine File \[XPD ROUTINE UPDATE\]

Verify a Build \[XPD VERIFY BUILD\]

Verify Package Integrity \[XPD VERIFY INTEGRITY\]

These utilities can be used both by developers and by sites who install software created by KIDS.

## Build File Print Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Build File Print \[XPD PRINT BUILD\] option prints out the build entry for a software application. It lists the complete definition of the software, including all files, components, install questions, and the environment pre-install and post-install routines, as shown in <u>Figure 18</u>.

<span id="_Ref511378048" class="anchor"></span>Figure 18: Build File Print Option—Sample Output

PACKAGE: ZXG DEMO 1.0 PAGE 1

----------------------------------------------------------------------------

NATIONAL PACKAGE:

DESCRIPTION:

Package containing demonstration of ZXG\* functions.

ENVIRONMENT CHECK : ZXGENV

PRE-INIT ROUTINE : ZXGPRE

POST-INIT ROUTINE: ZXGPOS

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

----------------------------------------------------------------------------

662105 ZXG DEMO YES YES NO

PRINT TEMPLATE:

ZXG PRINT FILE \#662105 SEND TO SITE

ROUTINE:

ZXGC00 SEND TO SITE

ZXGC01 SEND TO SITE

ZXGC02 SEND TO SITE

ZXGC03 SEND TO SITE

ZXGC04 SEND TO SITE

ZXGC05 SEND TO SITE

ZXGC06 SEND TO SITE

ZXGC07 SEND TO SITE

ZXGC08 SEND TO SITE

OPTION:

ZXG TEST SEND TO SITE

INSTALL QUESTIONS:

## Install File Print Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Install File Print \[XPD PRINT INSTALL FILE\] option prints out the results of an installation, as stored in the INSTALL (#9.7) file. Use this option to check on the status of an installation in progress or to print out the results of a completed installation, as shown in <u>Figure 19</u>.

<span id="_Ref511378097" class="anchor"></span>Figure 19: Install File Print Option—Sample Output

PACKAGE: ZXG DEMO 1.0 PAGE 1

COMPLETED ELAPSED

----------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: FEB 07, 2004@07:51:59

NATIONAL PACKAGE:

INSTALL STARTED: FEB 07, 2004@07:52:14 07:52:23 0:00:09

ROUTINES: 07:52:15 0:00:01

PRE-INIT CHECK POINTS:

XPD PREINSTALL STARTED 07:52:15

XPD PREINSTALL COMPLETED 07:52:15

FILES:

ZXG DEMO 07:52:16 0:00:01

PRINT TEMPLATE 07:52:17 0:00:03

OPTION 07:52:21 0:00:02

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED 07:52:21

XPD POSTINSTALL COMPLETED 07:52:21

INSTALL QUESTION PROMPT ANSWER

XPZ1 Want to DISABLE Scheduled Options, Options and Protocols NO

MESSAGES:

Install Started for ZXG DEMO 1.0 :

Feb 07, 2004@07:52:14

Installing Routines:

Feb 07, 2004@07:52:15

Running Pre-Install Routine: ^ZXGPRE

Installing Data Dictionaries:

Feb 07, 2004@07:52:16

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing OPTION

Feb 07, 2004@07:52:21

Running Post-Install Routine: ^ZXGPOS

Updating Routine file...

Updating KIDS files...

ZXG DEMO 1.0 Installed.

Feb 07, 2004@07:52:23

## Edit Install Status Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Install Status \[XPD EDIT INSTALL\] option, released with Kernel patch XU\*8.0\*539, lets you edit the STATUS (#.02) and the INSTALL COMPLETE TIME (#17) fields in the INSTALL (#9.7) file. Use this option to change the status of a patch that was de-installed, as shown in <u>Figure 20</u>.

<span id="_Ref511378180" class="anchor"></span>Figure 20: Edit Install Status Option—Sample User Dialog

Select Utilities Option: <span class="mark">EDIT INSTALL \<Enter\></span> Status

Select INSTALL NAME: <span class="mark">USER TEST \<Enter\></span>

1 USER TEST 1.0 Install Completed 5/14/08@11:21:04

=\> TEST ;Created on May 14, 2008@11:03:58

2 USER TEST 1.0 Loaded from Distribution 7/8/09@10:33:16

=\> TEST ;Created on Jul 08, 2009@10:31:50

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> USER TEST 1.0 Install Completed 5/14/08@11:21:04

=\> TEST ;Created on May 14, 2008@11:03:58

STATUS: Install Completed// <span class="mark">??? \<Enter\></span>

This is the status of this package at this site.

Choose from:

0 Loaded from Distribution

1 Queued for Install

2 Start of Install

3 Install Completed

4 De-Installed

STATUS: Install Completed// <span class="mark">\<Enter\></span>

INSTALL COMPLETE TIME: MAY 14,2008@11:21:04//

## Convert Loaded Package for Redistribution Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\] option to add software to an existing distribution.

A KIDS distribution can transport one or more software applications. What if you want to add additional software to an existing distribution? For example, suppose you have a distribution for a software application. Further, suppose that patches are transported as individual KIDS software, and you want to add all existing patches to the software’s distribution? The Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\] option lets you do this.

In <u>Figure 21</u> and <u>Figure 22</u>, distributions for a software application (that is ZXG 1.0) and a patch (that is ZXG\*1.0\*1) are both loaded. The Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\] option is used to build a new distribution combining both original distributions.

Follow these steps to create a new distribution from existing distributions:

1.  Load the original distributions (there is no need to install them, however).

In this example, you would load the distributions for ZXG 1.0 and ZXG\*1.0\*1 (but you would *not* install them).

24. Use the Convert Loaded Package for Redistribution \[XPD CONVERT PACKAGE\] option. It lets you choose loaded transport globals and transfers them into a format ready for export. Also, it creates build entries for each software application contained in the distributions. This allows you to create a new distribution containing the transport globals from the existing distributions. Kernel patch XU\*8.0\*44 added the “Want to make the Transport Globals Permanent? NO//” prompt, answering YES to this prompt flags the global so that it is *not* deleted after the transportation. This provides a “Gold” account or library of software and patches that are included in a Transport Global.

In the example in <u>Figure 21</u>, you would first convert the loaded distribution ZXG 1.0 into a form ready to re-distribute:

> <span id="_Ref85597561" class="anchor"></span>Figure 21: Convert Loaded Package for Redistribution—Sample User Dialog (1 of 2)

Select Utilities Option: <span class="mark">CONVERT LOADED PACKAGE FOR REDISTRIBUTION \<Enter\></span>

Select INSTALL NAME: <span class="mark">ZXG 1.0 \<Enter\></span> Loaded from Distribution

This distribution was loaded on Feb 28,2004@08:15:05 with header of

It consisted of the following Install(s):

ZXG 1.0

Want to make the Transport Globals Permanent? NO// <span class="mark">YES \<Enter\></span>

Want to continue with the conversion of the package(s)? NO// <span class="mark">YES \<Enter\></span>

\*\* DONE \*\*

Select Utilities Option:

Then you would convert the patch distribution, ZXG\*1.0\*1, into a form ready to re-distribute:

> <span id="_Ref85597575" class="anchor"></span>Figure 22: Convert Loaded Package for Redistribution—Sample User Dialog (2 of 2)

Select Utilities Option: <span class="mark">CONVERT LOADED PACKAGE FOR REDISTRIBUTION \<Enter\></span>

Select INSTALL NAME: <span class="mark">ZXG\*1.0\*1 \<Enter\></span> Loaded from Distribution

This distribution was loaded on Feb 28,2004@08:15:35 with header of

It consisted of the following Install(s):

ZXG\*1.0\*1

Want to make the Transport Globals Permanent? NO// <span class="mark">YES \<Enter\></span>

Want to continue with the conversion of the package(s)? NO// <span class="mark">YES \<Enter\></span>

\*\* DONE \*\*

25. Create the new distribution with the Transport a Distribution \[XPD TRANSPORT PACKAGE\] option. Select each build from the original distributions that you want to be part of the new distribution. For each build that you select, you should be told that the transport global already exists and be asked if you want to use this transport global. Answer YES in each case to use the current transport global.

Once you have selected all the builds for the new distribution, go ahead and create the new distribution.

In the example in <u>Figure 23</u>, you create a new distribution containing both ZXG 1.0 (the original software application) and ZXG\*1.0\*1 (an added software application):

> <span id="_Ref84906185" class="anchor"></span>Figure 23: Transport a Distribution—Sample User Dialog

Select Edits and Distribution Option: <span class="mark">TRANSPORT A DISTRIBUTION \<Enter\></span>

Enter the Package Names to be transported. The order in which they are entered will be the order in which they are installed.

First Package Name: <span class="mark">ZXG 1.0 \<Enter\></span> \*\*Transport Global exists\*\*

Use this Transport Global? <span class="mark">YES \<Enter\></span>

Another Package Name: <span class="mark">ZXG\*1.0\*1 \<Enter\></span> \*\*Transport Global exists\*\*

Use this Transport Global? <span class="mark">YES \<Enter\></span>

Another Package Name: <span class="mark">\<Enter\></span>

Order

1 ZXG 1.0 \*\*will use current Transport Global\*\*

2\. ZXG\*1.0\*1 \*\*will use current Transport Global\*\*

OK to continue? NO//<span class="mark">YES \<Enter\></span>

Enter a Host File: <span class="mark">ZXG1.KID \<Enter\></span>

Header Comment: PATCHED DISTRIBUTION ZXG 1.0

ZXG 1.0...

ZXG\*1.0\*1...

Package Transported Successfully

![](kernel-8-0-systems-management-kids-user-guide/016.png) NOTE: Changing a distribution’s build entries before redistributing is *not* recommended.

## Display Patches for a Package Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Patches for a Package \[XPD PRINT PACKAGE PATCHES\] option prints all patches installed for a software application. It displays the date installed and who installed the patches. It optionally prints the description of the patch. All the displayed information comes from the PACKAGE (#9.4) file, as shown in <u>Figure 24</u>.

<span id="_Ref511378479" class="anchor"></span>Figure 24: Display Patches for a Package Option—Sample User Dialog

Select Utilities Option: <span class="mark">DISPLAY PATCHES FOR A PACKAGE \<Enter\></span>

Select PACKAGE NAME: <span class="mark">KERNEL \<Enter\></span>

Select VERSION: 8.0// <span class="mark">\<Enter\></span> 07-29-95

Do you want to see the Descriptions? NO// <span class="mark">\<Enter\></span>

DEVICE: HOME// <span class="mark">\<Enter\></span> SYSTEM

PACKAGE: KERNEL Oct 09, 2004 1:32 pm PAGE 1

PATCH \# INSTALLED INSTALLED BY

-----------------------------------------------------------------

VERSION: 8.0 JUL 29, 2004 XUUSER,TEN

28 APR 25, 2004 XUUSER,NINE

20 SEQ \#23 FEB 09, 2004 XUUSER,NINE

32 SEQ \#24 MAY 15, 2004 XUUSER,NINE

23 SEQ \#25 MAY 17, 2004 XUUSER,TEN

39 SEQ \#26 JUL 19, 2004 XUUSER,ELEVEN

26 SEQ \#27 JUN 01, 2004 XUUSER,TEN

27 SEQ \#28 JUN 13, 2004 XUUSER,NINE

24 SEQ \#29 JUN 30, 2004 XUUSER,TEN

40 SEQ \#30 AUG 28, 2004 XUUSER,ELEVEN

41 SEQ \#31 AUG 29, 2004 XUUSER,TEN

29 SEQ \#32 AUG 30, 2004 XUUSER,NINE

## Purge Build or Install Files Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each KIDS installation adds one entry to the BUILD (#9.6) and INSTALL (#9.7) files for every transport global installed from the distribution. You can use the Purge Build or Install Files \[XPD PURGE FILE\] option to purge entries in these files.

The first question the option asks is which file to purge, the BUILD (#9.6) or INSTALL (#9.7) file. Choose one of these files.

The next question asked is the number of versions to retain.

### Versions to Retain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you choose to retain some number entries for a software application, the option *must* decide which entries are most recent. The Purge Build or Install Files \[XPD PURGE FILE\] option uses numeric order based on software version number to decide which entries are the most recent. When there are multiple entries for the same version number (such as alpha or beta installs took place), the following order of precedence is used:

1.  Released Version is the most recent (version number contains no letters, such as 8.0)
26. Beta Test Version (version number contains V, such as 8.0V10)
27. Alpha Test Version (version number contains T, such as 8.0T10)

### Selecting Software Names for Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After versions to retain, the next prompt is “Package Name.” You can enter a partial or full software application name. You continue to be prompted for additional software names until you simply press the \<Enter\> key without making any further entries at the “Package Name” prompt.

- Packages (Software)—To select software entries for purging, at the “Package Name” prompt, enter a partial or full software application name. You can optionally enter partial or full version numbers. The list of candidates for purging contains all entries (excluding patch entries) whose first characters match all characters in the software name that you specify. If you enter “ALL”, all software (but *not* patches) are selected for purging.
- Patches—Patches are a special case. To select patch entries for purging, you *must* enter the full namespace of the patch, the full version number, and an asterisk. You can optionally add a partial or full patch number after the asterisk. The list of candidates for purging contain all entries whose first characters match all characters in the string you specify.

<span id="_Toc193181899" class="anchor"></span>Figure 25: Purge or Install Files Option—Sample User Dialog

Select Utilities Option: <span class="mark">PURGE \<Enter\></span> Build or Install Files

Select one of the following:

B Build

I Install

ALL Build & Install

Purge from what file(s): <span class="mark">B \<Enter\></span>

Versions to Retain: (0-100): 1// <span class="mark">0 \<Enter\></span>

Package Name: ALL// <span class="mark">ZXG</span>

Another Package Name: <span class="mark">\<Enter\></span> ...

Package(s) in Build file, Don't retain any versions Page 1

--------------------------------------------------------------------

ZXG 1.0

ZXG 2.0

ZXG 3.0

OK to DELETE these entries? NO// <span class="mark">YES \<Enter\></span>

Select Utilities Option:

### Purging Selected Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on the software name you enter and the number of entries you ask to retain, the Purge Build or Install Files \[XPD PURGE FILE\] option lists the software it finds to purge. If you answer YES to the “OK to DELETE these entries? NO//” prompt, the option purges the listed entries.

### Reasons to Retain BUILD and INSTALL File Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- BUILD File—Entries in the BUILD (#9.6) file are created by the software developers and identify every component in the software. BUILD (#9.6) file entries also contain the checksums for a software application’s components. You may want to retain the build entry for the most recent versions of installed software, so that you can verify the checksums of the loaded software against its original checksums.
- INSTALL File—Each entry in the INSTALL (#9.7) file contains a record of the installation for a given software application. This information is useful as a record of each installation.

## Rollup Patches into a Build Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rollup Patches into a Build \[XPD ROLLUP PATCHES\] option finds all the patches for a software application and add their individual BUILD (#9.6) file definitions to the software’s BUILD (#9.6) file definition. This enables you to create a single BUILD (#9.6) file entry that contains the definition for the patched software.

KIDS checks the BUILD (#9.6) file and lists all KIDS patches with a matching software name and version number. The list of patches is *not* necessarily displayed in patch sequence number.

This list only includes KIDS patches. Also, it does *not* include any pre- or post-install routines. You can use the Edit a Build \[XPD EDIT BUILD\] option to further modify the build and add any additional patches.

<span id="_Toc193181900" class="anchor"></span>Figure 26: Rollup Patches into a Build Option—Sample User Dialog

Select Utilities Option: <span class="mark">ROLLUP PATCHES INTO A BUILD \<Enter\></span>

Rollup patches into Build: <span class="mark">KERNEL 8.0T20 \<Enter\></span> KERNEL

This package already contains the following patches:

XU\*8.0T20\*4

The following patches can be rolled into Package RON 8.0T20

XU\*8.0T20\*5

XU\*8.0T20\*6

XU\*8.0T20\*7

XU\*8.0T20\*8

XU\*8.0T20\*11

OK to continue? YES// <span class="mark">\<Enter\></span>

...SORRY, HOLD ON...............................................................

................Done.

## Update Routine File Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update Routine File option \[XPD ROUTINE UPDATE\] option updates the ROUTINE (#9.8) file to match the routine set stored on the current system.

Ideally, the ROUTINE (#9.8) file would contain an entry for every routine on the current system. However, the ROUTINE (#9.8) file does *not* get updated automatically when routines are added to or deleted from the system. But KIDS needs the ROUTINE (#9.8) file so that it can store the list of routines in a software application as pointers to the ROUTINE (#9.8) file (rather than relying on namespace alone).

Developers should use this option to update the ROUTINE (#9.8) file before editing the routine component in a build entry, to ensure that all the routines they want to include in a software application can be selected by the routines’ matching entries in the ROUTINE (#9.8) file.

If you answer YES to the question “Want me to clean up the Routine file before updating?”, the option goes through the ROUTINE (#9.8) file and deletes any entries across all namespaces that have no matches with an actual routine on the current system. As of Kernel patch XU\*8.0\*393, however, any routine that has been marked in the CHECKSUM REPORT (#6) field in the ROUTINE (#9.8) file as “National” is *not* deleted during the clean up the Routine File phase of the update.

Then, the Update Routine File option \[XPD ROUTINE UPDATE\] option re-populates the ROUTINE (#9.8) file with all routines currently on the system for the namespaces you enter (you can exclude parts of a namespace if you want, as well).

<span id="_Toc193181901" class="anchor"></span>Figure 27: Update Routine File Option—Sample User Dialog

Select Utilities Option: <span class="mark">UPDATE ROUTINE FILE \<Enter\></span>

Routine Namespace: <span class="mark">XU \<Enter\></span>

Routine Namespace: <span class="mark">-XUI \<Enter\></span>

Routine Namespace: <span class="mark">\<Enter\></span>

NAMESPACE INCLUDE EXCLUDE

------- -------

XU XUI

OK to continue? YES// <span class="mark">\<Enter\></span>

Want me to clean up the Routine File before updating? YES// <span class="mark">\<Enter\></span>

...SORRY, THIS MAY TAKE A FEW MOMENTS... ...Done.

## Verify a Build Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verify a Build \[XPD VERIFY BUILD\] option checks whether a build entry’s listed components exist on the current system. This is useful for developers who are preparing to create a transport global. They can check that there are actual components on the system matching the components requested in the build entry, in advance of trying to create a transport global. Therefore, developers should use the Verify a Build \[XPD VERIFY BUILD\] option *before* creating transport globals from build entries.

For any component in the build entry that does *not* actually exist on the system, the option outputs a one-line message identifying the missing component, with the appellation \*\*NOT FOUND\*\*. The developer is also prompted with “Do you want to remove the missing Files? NO//”. This allows you to verify if the missing component should in fact be removed from the build. If the missing component is required, the developer should create the missing component for the build entry before creating a transport global.

<span id="_Toc193181902" class="anchor"></span>Figure 28: Verify a Build Option—Sample User Dialog

Select Utilities Option: <span class="mark">VERIFY A BUILD \<Enter\></span>

Select BUILD NAME: <span class="mark">XU\*8.0\*11 \<Enter\></span> KERNEL

File \#8995 \*\* NOT FOUND \*\*

Do you want to remove the missing Files? NO// <span class="mark">\<Enter\></span>

\*\* DONE \*\*

Select Utilities Option:

## Verify Package Integrity Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Verify Package Integrity \[XPD VERIFY INTEGRITY\] option to compare checksums of software components on the system against the checksums of the components when they were originally transported. Any discrepancies are reported. Currently, routines are the only components that are checked, but checksums are extended to other software components in the future.

The checksums of components for the currently installed software are verified against checksums stored in the BUILD (#9.6) file entry for the software. If the most recent version of the BUILD (#9.6) file entry for a software application has been purged, the Verify Package Integrity \[XPD VERIFY INTEGRITY\] option is no longer able to verify checksums for the loaded software. Because of this, in most cases you should *not* purge the most recent build entry for a software application.

As of Kernel patch XU\*8.0\*369, the integrity checking CHECK1^XTSUMBLD routine supports the Compare local/national checksums report \[XU CHECKSUM REPORT\] option.

As of Kernel patch XU\*8.0\*393, KIDS was modified to send a message to a server on FORUM when a KIDS build is sent to a Host File Server (HFS) device. This message contains the checksums for the routines in the patch. The server on FORUM matches the message with a patch if the sending domain is authorized on FORUM. There is no longer a need for developers to manually include routine checksums (either CHECK^XTSUMBLD or CHECK1^XTSUMBLD routines) in the patch description. The patch module includes the before and after CHECK1^XTSUMBLD values in the “Routine Information” section at the end of the patch document.

With changes in the National Patch Module (NPM) on FORUM, when the patch is released the checksums for the routines are moved to the ROUTINE (#9.8) file on FORUM. The checksum “before” values come from the FORUM ROUTINE (#9.8) file and are considered the GOLD standard for released checksums. The local site’s Compare local/national checksums report \[XU CHECKSUM REPORT\] option uses the FORUM ROUTINE (#9.8) file as its source to create reports showing any routines that do *not* match.

This patch also modified the KIDS BUILD (#9.6) file by adding the TRANSPORT BUILD NUMBER (#63) field used to store a build number that is incremented each time a build is made. This build number is added to the second line of each routine in the 7th “;” piece. This makes it easy to tell if a site is running the current release during testing and afterword. The leading “B” found in the checksum tells the code what checksum API to use.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-kids-user-guide/017.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="_Toc204334721" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-kids-user-guide/018.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-kids-user-guide/019.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.