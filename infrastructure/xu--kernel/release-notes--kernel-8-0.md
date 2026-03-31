---
title: Kernel 8.0 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
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
  - kernel
  - table
  - contents
  - software
  - kids
  - entry
  - alerts
  - device
  - alert
  - blockquote
page_count: 0
word_count: 3254
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn8_0rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn8_0rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

![](kernel-8-0-release-notes/001.png)

KERNELRELEASE NOTES

July 1995

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>07/95</td>
<td>1.0</td>
<td>Initial Kernel V. 8.0 software and documentation release</td>
<td><p>San Francisco, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>08/15/06</td>
<td>2.0</td>
<td><p>Kernel V. 8.0 documentation reformatting/revision.<br />
<br />
This is the initial complete reformatting of the <em>Kernel Release Notes</em> since its original release in July 1995.</p>
<p>Also, at this point in time, only minimal content updates have been made based on select released Kernel patches. Due to time constraints, not all released Kernel patches with content changes have been added at this time. We wanted to get a new baseline document published so that in the future we can more easily update the <em>Kernel Release Notes</em>.</p>
<p>As time allows, we will be updating this reformatted manual with all released patch information that affects its content. Because of the chapter-numbering scheme, future additions can be made with minimal disruption to the entire manual page flow.</p>
<p>Thanks for your patience!</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: XUPATIENT,[N] or XUUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., XUPATIENT, ONE, XUPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td><p>Oakland, CA OIFO:</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>02/08/07</td>
<td>2.1</td>
<td><p>Changed Kernel document title references to:</p>
<ul>
<li><blockquote>
<p><em>Kernel Developer's Guide</em> (previously known as the <em>Kernel Programmer Manual</em>).</p>
</blockquote></li>
<li><blockquote>
<p><em>Kernel Systems Management Guide</em> (previously known as the <em>Kernel Systems Manual</em>).</p>
</blockquote></li>
</ul></td>
<td><p>Oakland, CA OIFO:</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

Table i. Documentation revision history

Patch Revisions

For the current patch history related to this software, please refer to the Patch Module on FORUM.

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [KIDS](#kids)
- [Alerts](#alerts)
- [Device Handler](#device-handler)
- [Documentation](#documentation)
- [Function Libraries](#function-libraries)
- [Menu Manager](#menu-manager)
- [Signon/Security](#signonsecurity)
- [TaskMan](#taskman)
- [Miscellaneous](#miscellaneous)
Kernel consists of programs that function as a set of standard software tools. These tools provide a uniform interface between the underlying operating system and Veterans Health Information Systems and Technology Architecture (VistA) application modules. Kernel supports VistA modules through the coordination of database, device, menu management, background job scheduling, security, auditing, and programming functions.
Kernel V. 8.0 introduces a new Kernel module:
- Kernel Installation and Distribution System (KIDS)
Kernel V. 8.0 also introduces many incremental changes in the following areas:
- Alerts
- Device Handler
- Documentation
- Function Libraries
- Menu Manager
- Signon/Security
- TaskMan
- Miscellaneous changes
These release notes describe the new features and changes with Kernel V. 8.0.

# KIDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Installation and Distribution System (KIDS) is a replacement for the previous software installation and distribution system, DIFROM, which was part of VA FileMan. KIDS provides greater flexibility to both programmers and installers in software and database transport. Specific features include:

For Users

> Not Applicable

For System Managers

- VistA software is exported in transport globals (not INIT routines). Transport globals can be sent alone or in groups to a site. Transport globals can be sent either in an HFS file (called a distribution) or in a MailMan message.
- You can load a software application's transport globals into ^XTMP as a separate step prior to the actual installation. You can list the contents of transport globals loaded in ^XTMP without installing them.
- KIDS does not load an incoming software application's routines when it runs the environment check for the software. KIDS only updates routines and other software components after you commit to run the installation.
- The developer of the software can allow you to disable options and protocols for the installation. This feature allows other software to remain operational during many installations.
- KIDS asks all installation questions before the install starts, including the post-install questions. KIDS stores all questions and answers in the INSTALL file, so that if you queue an install, you can review the questions and their answers by printing the INSTALL file entry.
- If you choose to disable any options or protocols during an installation, KIDS suspends the running of all scheduled options on the system during the install. This prevents scheduled options from interfering with the install of VistA software.
- You can instruct KIDS to update routines on multiple CPUs other than the CPU that the main installation is running on.
- KIDS captures all installation output in a word processing field in the INSTALL file, as well as sending it to the home device of the installation process.
- KIDS stores timing information for each phase of an installation in the INSTALL file.
- KIDS divides installations into phases using checkpoints. If an installation aborts, it can be restarted from the last completed checkpoint, rather than having to run it again from the beginning.
- The install history of software and patch installations is still maintained in the PACKAGE file, in the VERSION and PATCH APPLICATION HISTORY multiples. Sites' local installation history is no longer overwritten during installs, however.
- It is no longer necessary to clean INIT routines off your system, since KIDS no longer uses INIT routines as the export mechanism. KIDS automatically deletes the transport global (the new export mechanism) when an install completes.

For Programmers

- Selecting software components is no longer tied exclusively to a single namespace. You can now build software with components from multiple namespaces.
- KIDS stores software definitions in the BUILD file, stored in ^XPD(9.6,. Printing a BUILD file entry shows you exactly what components are being sent.
- KIDS lets you send multiple VistA software in one distribution. Your environment check routines can determine if any given software in a distribution should be installed or skipped.
- KIDS makes sure that any incoming software is at a version greater than or equal to the site's version.
- Installations use standard checkpoints for each component, to facilitate restarting installs that fail to complete. In addition, you can add custom checkpoints in your Pre- and Post-install routines, to allow installations to be restarted from where they failed in Pre- and Post-install code.
- For installing data, KIDS adds two new modes (Replace and Add Only If New File) to the two existing modes (Merge and Overwrite). Replace overwrites the site's data, even for incoming null fields, but still retains data in local fields. Add Only If New File adds data only if the file didn't exist at the site before the installation.
- You can use search templates and screens to export subsets of a VA FileMan file's data.
- KIDS performs limited pointer resolution when installing data.
- When you send partial data dictionaries, you can send individual fields within a multiple, without sending the entire multiple.
- For options and protocols, you can Merge, Replace, or Use as a Link at the installing site. Using a menu option or protocol as a link allows you to attach an option to a menu that you didn't export (e.g., EVE).

# Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users

- When you select a group of information-only alerts to process, you can simply read them, without being asked what action to take between each one.
- Forwarding is a new alert processing action. You can forward individual alerts or groups of alerts to users and mail groups or to a printer. You can forward them as either alerts or mail messages.

For System Managers

- Holders of a new key (XQAL-DELETE) are able to delete current alerts for other users. This can be useful is if a user is inactive for a period of time (for example, on leave). This option is intended for IRM personnel and ADPACs.
- Alerts are moved out of the multiple in the NEW PERSON file and into the new ALERT file, stored in global ^XTV(8992,. A post-install conversion moves current alerts into the new file from the NEW PERSON file.
- The new ALERT TRACKING file, stored in ^XTV(8992.1, holds alert auditing records. Alerts are now automatically audited. Information stored includes when the alert was created, when the alert was seen by each user, what action each user took as well as when they took it and when the associated alert was deleted.
- The purge option for the ALERT file (Delete Old (\>14d) Alerts) can now be queued. Also, if the option is scheduled to run regularly, you can specify a different purge interval than 14 days by using the OPTION SCHEDULING file's TASK PARAMETERS field.
- The purge option for the ALERT file (Delete Old (\>14d) Alerts) now purges entries in the ALERT TRACKING file as well. It uses a purge interval of 30 days for each alert, unless a different interval is specified when the associated alert is created.

For Programmers

- Three new entry points, RECIPURG^XQALBUTL, NOTIPURG^XQALBUTL, and PTPURG^XQALBUTL, provide ways to purge alerts based on recipient, notification code, and patient.
- The new entry point ACTION^XQALERT processes an alert.
- The new entry point FORWARD^XQALFWD allows you to forward alerts.
- The new entry point PATIENT^XQALERT returns an array of all open alerts for a particular patient.
- The new XQAARCH input variable for SETUP^XQALERT entry point allows you to specify how long alert tracking information should be retained in ALERT TRACKING file.
- The XQADATA input variable for SETUP^XQALERT entry point now allows up to 245 characters.
- The new XQASURO and XQASUPV input variables for SETUP^XQALERT allow you to set a number of days (from 1 to 30) for the alert to be processed by the original recipient. After this, if it has not been processed, the alert can be forwarded to the recipient's surrogate or supervisor. Forwarding is triggered by the site running the Delete Old (\>14d) Alerts option.
- The new entry point USER^XQALERT returns an array of all alerts for a given user.

# Device Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users

- The Spooler Menu has a new option to view spool documents using VA FileMan's Browser.
- Kernel supports VA FileMan Browser as a device. Any report that can be sent to a device, can now be sent for viewing to VA FileMan's Browser. An improvement over the home device, VA FileMan's Browser allows scrollable, searchable online viewing of any report.

For System Managers

- Auto-Despooling now allows you to specify the number of copies to print on each selected printer.
- Two new DEVICE file fields are provided for executable M code: PRE-OPEN EXECUTE and POST-CLOSE EXECUTE.
- The QUEUING field in the DEVICE file now has three settings: Allowed, Forced, and Not Allowed.
- New fields in the TERMINAL TYPE file support enhanced terminal capabilities: CURSOR ON and CURSOR OFF.
- New fields in the TERMINAL TYPE file support enhanced printer capabilities: COLOR ON, COLOR OFF, SIMPLEX, DUPLEX LONG EDGE BINDING and DUPLEX SHORT EDGE BINDING.

For Programmers

- The new ^%ZISH API has a comprehensive set of entry points for working with HFS (Host File System) files.
- The new ^%ZISUTL API allows opening, using, and closing multiple devices (the existing ^%ZIS API only supports the concurrent use of one additional device beyond the home device).
- The internal entry number of a device can now be used to select a device with the ^%ZIS call (through the IOP input variable).
- Two new entry points, PSET^%ZISP and PKILL^%ZISP, manage a set of Device Handler IO\* variables for printers. This set of variables allows control of the following printer features: Bar Code On/Off, Color On/Off, Simplex and Duplex printing, Italics On/Off, Superscript On/Off, and Subscript On/Off.
- New RESETVAR^%ZIS entry point allows re-setting home device variables without altering the active right margin setting.

# Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users, System Managers, and Programmers

- The *Kernel Systems Management Guide* is reorganized into shorter, more focused chapters. All programmer-related content was removed and placed in a new *Kernel Developer's Guide*.
- The Kernel documentation set is updated to reflect new Kernel modules and features.
- The Kernel documentation set is available in electronic form, in Adobe Acrobat's Portable Document Format (PDF).
- Kernel APIs are available at the following Web address:

> <http://vista.med.va.gov/kernel/apis/index.asp>

# Function Libraries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users and System Managers

> Not Applicable

For Programmers

- The new Kernel XGF Function Library supports programmers designing text-based applications, providing advanced screen handling capabilities. Functions supported include cursor positioning, overlapping text windows, video attribute control, and keyboard escape processing, all in a text-mode environment.
- The new \$\$SCH^XLFDT function helps determine what time to schedule tasked jobs, based on scheduling interval codes.
- The new \$\$CCD^XLFUTL and \$\$VCD^XLFUTL functions provide the ability to compute and verify a terminal check digit for a number.
- The new \$\$EN^XUA4A71 function returns the soundex representation of a string.
- The new \$\$BASE^XLFUTL, \$\$CNV^XLFUTL, and \$\$DEC^XLFUTL functions provide entry points to convert numbers from one base to another (supports bases two through sixteen).
- The new \$\$KSP^XUPARAM function retrieves values of some Kernel site parameters.

# Menu Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users

- You can now create a menu template (named LOGIN) that is executed on your first signon each day.

For System Managers

- Menu audits are moved to a VA FileMan-compatible file, AUDIT LOG FOR OPTIONS, stored in ^XUSEC(19,. Sites can use VA FileMan to generate audit reports.
- Delegation levels now apply to keys as well as options.
- Out-Of-Order Option Sets allow you to define sets of options and then enable and disable sets of options.
- Enhanced error processing for DSM for OpenVMS sites is supported. For versions of DSM for OpenVMS that support the proposed 95 M standard, Kernel's error trap captures variables in their state at the time errors occur, regardless of how variables may have been NEWed beforehand. Stack levels for the routine call stack are recorded in the error trap in the \$STACK variable. When MSM-DOS supports the enhanced error processing in the proposed 95 M standard, a Kernel patch will be issued to support the MSM-DOS implementation.

For Programmers

- The new \$\$ADD^XPDMENU function allows you to add an option to a menu.
- The new OUT^XPDMENU entry point allows you to edit an option's OUT OF ORDER MESSAGE field.
- The new RENAME^XPDMENU entry point allows you to rename an option.

# Signon/Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users

- The Electronic Signature Code Edit option now lets you edit the Voice Pager and Digital Pager fields.
- In the Edit User Characteristics option, to change your verify code you must now enter your existing verify code first.

For System Managers

- Batch-mode Access Grant is fixed. If the selected user already exists, you are given a choice of whether to merge into current user entry or delete entry first.
- Kernel provides a new post-sign-in message that is similar to the current introductory text, but is displayed after user has signed in.
- The new DISUSER field in NEW PERSON file allows you to prevent a user from signing on, while still leaving their account enabled.
- KILL^XUSCLEAN has been modified, so that when it is called from an option, it preserves the values of any variables stored in the option's PROTECTED VARIABLES field.
- The XUSERAOLD option (Purge Log of Old Access and Verify Codes) can now be queued.

For Programmers

- A new Kernel extended action option \[XU USER SIGN-ON\] is executed at signon for each user. You can attach other options to this option to perform software-specific tasks at signon.
- A new Kernel extended action option \[XU USER TERMINATE\] is executed for each user on termination of their account. You can attach other options to this option and perform software-specific tasks for each user as his account is terminated.

# TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Users

> Not Applicable

For System Managers

- TaskMan now stores tasks in ^%ZTSCH subscripted by the total number of seconds in their scheduling time (as contained in \$H), rather than in direct \$H format. As a result, tasks now sort in the order scheduled.
- TaskMan user interface routines are moved out of the ZTM namespace in the manager's account, and into the XUTM namespace in the production account.
- A new option, Cleanup Task List, cleans up TaskMan's running task list.
- The new OPTION SCHEDULING file, stored in ^DIC(19.2, holds option scheduling information formerly stored in the OPTION file (#19). As a result, options can have multiple schedule entries. Also, incoming options will no longer overwrite site scheduling. Kernel V. 8.0 post-install performs the conversion.
- TaskMan provides enhanced frequency choices for option scheduling.
- A new option, SYNC Flag File Control, cleans up after the failure of a job using TaskMan SYNC FLAGs.

For Programmers

- The new EN^XUTMDEVQ entry point encapsulates logic to handle both direct printing and queuing into a single call.
- The new TaskMan SYNC FLAGs feature supports job series. When each job in a series uses the same resource, SYNC FLAGs allow you to permit the next job in the series to start only if the previous job completed successfully.

# Miscellaneous

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For System Managers

- Kernel site parameters are moved out of the MAILMAN SITE PARAMETERS file (#4.3), which is stored in ^XMB, and placed in the KERNEL SYSTEM PARAMETERS file, stored in ^XTV(8989.3,, and the KERNEL PARAMETERS file, stored in ^XTV(8989.2,. File \#4.3 continues to store MailMan-related site parameters.
- Kernel provides limited support for the DataTree and M/SQL M implementations.
- Kernel now uses ^TMP for temporary storage, rather than ^UTILITY.

For Programmers

- The new \$\$VERSION^%ZOSV function returns operating system version or name, as defined by vendor.