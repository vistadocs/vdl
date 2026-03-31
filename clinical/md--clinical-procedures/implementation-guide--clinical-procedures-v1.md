---
title: Clinical Procedures Version 1 Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: anchor
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1
group_key: "MD:MD:1"
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - procedures
  - procedure
  - table
  - clinical
  - contents
  - class
  - instrument
  - device
  - consult
  - service
page_count: 0
word_count: 31137
section_count: 45
table_count: 44
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: April 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_impg-revised.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_impg-revised.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](clinical-procedures-version-1-implementation-guide/001.png)

CLINICAL PROCEDURESIMPLEMENTATION GUIDE

April 2004

Office of Information & Technology

Office of Enterprise Development

#### Revision History

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 20%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Description</strong></td>
<td><strong>Date</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>Originally released.</td>
<td>April 2004</td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Patch MD*1.0*4 released.</td>
<td>September 2006</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>Patch MD*1.0*9 released November 2007. Update Setting up HL7 Parameter for port 5000 with CACHE.</td>
<td>February 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a> Patch MD*1.0*14 released. Updated Setting Up Consults for Clinical Procedures, Exported XPAR Kernel Parameters, add new section called Scheduled Options. Added information about launching CP Gateway under the section Working with CP Gateway.</td>
<td>March 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a>Patch MD*1.0*6 released. Updated MD namespace Clinical Procedures file list and CP Class Upload Header output display, added TIU prompts for adding new TIU Note Titles, added instrument warning for automated instruments, added Processing Application field, changed wording for Count/Non-count clinics, added new Exported Kernel XPAR parameters and screen capture, revised “Setting Up HL7 Parameters chapter for clarity, updated list of Instrument Processing Routines, added Appendix D – Exported Values For Hemodialysis Options.</td>
<td>May 2008</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a>Patch MD*1.0*11 released. Updated Setting Up Procedures, Exported Kernel XPAR Parameters, and Scheduled Options.</td>
<td>June 2009</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><a href="#fn6" class="footnote-ref" id="fnref6" role="doc-noteref"><sup>6</sup></a>Patch MD*1.0*21 released. Updated Chapter 1 - General CP Package Information and added assigning options. Updated Step 2 of Setting up TIU for Clinical Procedures in Chapter 4, updated Kernel XPAR Parameter in Chapter 6, Added Chapter 7, Application Proxy, and Appendix E, High Volume Procedure Checklist. Added Step 3 – Create Ad Hoc Health Summary Components For CP to Chapter 10. Updated Ch 21 Index.</td>
<td>June 2010</td>
<td><mark>REDACTED</mark> </td>
</tr>
<tr class="odd">
<td><a href="#fn7" class="footnote-ref" id="fnref7" role="doc-noteref"><sup>7</sup></a>Patch MD*1.0*20 release added. Added list of tasks that can be queued. Updated Exported Kernel XPAR Parameters.</td>
<td>November 2010</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>MD*1.0*60 release. Added new CP Instrument parameters and VistA menu options.</td>
<td>July 2018</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>MD*1.0*65 release. Added High Volume changes for TIU Technical fields</p>
<p>Consult and Procedure Conversion options</p></td>
<td>December 2018</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch MD*1.0*4 September 2006 Patch 4 release added.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Patch MD*1.0*9 November 2007 Patch 9 release added.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Patch MD*1.0*14 March 2008 Patch 14 release added.<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>Patch MD*1.0*6 May 2008 Patch 6 release added.<a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5"><p>Patch MD*1.0*11 June 2009 Patch 11 release added.<a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn6"><p>Patch MD*1.0*21 June 2010 Patch 21 release added.<a href="#fnref6" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn7"><p>Patch MD*1.0*20 November 2010 Patch 20 release added.<a href="#fnref7" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [About Clinical Procedures](#about-clinical-procedures)
    - [### About CP User](#about-cp-user)
    - [About CP Manager](#about-cp-manager)
    - [About CP Gateway](#about-cp-gateway)
  - [Intended Audience](#intended-audience)
  - [Related Manuals](#related-manuals)
  - [General CP Package Information](#general-cp-package-information)
  - [Resource Requirements](#resource-requirements)
  - [Hospital Location File Requirement (Implementing Workload Reporting)](#hospital-location-file-requirement-implementing-workload-reporting)
  - [VistA Imaging](#vista-imaging)
- [Using CP Manager](#using-cp-manager)
  - [CP Manager Toolbar](#cp-manager-toolbar)
  - [Finding a Parameter](#finding-a-parameter)
  - [Deleting an Automated Instrument or Procedure](#deleting-an-automated-instrument-or-procedure)
  - [Printing Reports](#printing-reports)
- [About Test Accounts and Imaging](#about-test-accounts-and-imaging)
  - [Changing All Test Accounts](#changing-all-test-accounts)
    - [Changing the Current Namespace](#changing-the-current-namespace)
    - [Configuring the Imaging Display Station](#configuring-the-imaging-display-station)
  - [Changing Test Accounts that Use a Background Processor](#changing-test-accounts-that-use-a-background-processor)
  - [Connecting the Background Processor PC to VistA Servers](#connecting-the-background-processor-pc-to-vista-servers)
  - [Refreshing Existing Test Accounts](#refreshing-existing-test-accounts)
- [Setting Up TIU for Clinical Procedures](#setting-up-tiu-for-clinical-procedures)
  - [Step 1 - Verify Clinical Procedures Class Upload Header](#step-1-verify-clinical-procedures-class-upload-header)
  - [Step 2 - Create CP Class Document Definitions](#step-2-create-cp-class-document-definitions)
    - [[^7]Example of New TIU Prompts](#7example-of-new-tiu-prompts)
  - [## Step 3 - Define Clinical Procedures Class Document Parameters](#step-3-define-clinical-procedures-class-document-parameters)
- [About ASU Business Rules and the Role of the Interpreter](#about-asu-business-rules-and-the-role-of-the-interpreter)
  - [How Business Rules Work](#how-business-rules-work)
  - [Role of the Interpreter](#role-of-the-interpreter)
- [# Setting Up Clinical Procedures](#setting-up-clinical-procedures)
  - [Step 1 - Populate the CP Definition (#702.01) file](#step-1-populate-the-cp-definition-70201-file)
  - [Step 2 – Setting Up Instruments](#step-2-setting-up-instruments)
    - [Editing an Automated Instrument](#editing-an-automated-instrument)
    - [Adding an Automated Instrument](#adding-an-automated-instrument)
    - [Additional Instrument Parameters](#additional-instrument-parameters)
    - [### Using the Instrument Analyzer](#using-the-instrument-analyzer)
  - [Step 3 – Setting Up Procedures](#step-3-setting-up-procedures)
    - [Editing a Procedure](#editing-a-procedure)
    - [Adding a Procedure](#adding-a-procedure)
  - [Step 4 – Setting Up System Parameters](#step-4-setting-up-system-parameters)
    - [Allow non-instrument attachments](#allow-non-instrument-attachments)
    - [Bypass CRC Checking](#bypass-crc-checking)
    - [Clinical Procedures Home Page](#clinical-procedures-home-page)
    - [Clinical Procedures On-Line](#clinical-procedures-on-line)
    - [CP/BGP Transfer Directory](#cpbgp-transfer-directory)
    - [CRC Values](#crc-values)
    - [Calculating a File’s CRC Value](#calculating-a-files-crc-value)
    - [Days to keep instrument data](#days-to-keep-instrument-data)
    - [Imaging File Types](#imaging-file-types)
    - [Offline Message](#offline-message)
    - [Version Compatibility](#version-compatibility)
    - [VistA Scratch HFS Directory](#vista-scratch-hfs-directory)
  - [[^24]Step 5 – Exported Kernel XPAR Parameters](#24step-5-exported-kernel-xpar-parameters)
    - [Exported Kernel XPAR Parameters for Patch MD\1.0\14](#exported-kernel-xpar-parameters-for-patch-md1014)
    - [[^25]Exported Kernel XPAR Parameters for Patch MD\1.0\6](#25exported-kernel-xpar-parameters-for-patch-md106)
    - [[^26]Exported Kernel XPAR Parameters for Patch MD\1.0\11](#26exported-kernel-xpar-parameters-for-patch-md1011)
    - [[^27] Exported Kernel XPAR Parameter for Patch MD\1.0\21](#27-exported-kernel-xpar-parameter-for-patch-md1021)
- [Select OPTION NAME: MD HIGH VOLUME PROCEDURE SETUP High Volume Procedure Setup High Volume Procedure Setup](#select-option-name-md-high-volume-procedure-setup-high-volume-procedure-setup-high-volume-procedure-setup)
    - [[^28]Exported Kernel XPAR Parameters for Patch MD\1.0\20](#28exported-kernel-xpar-parameters-for-patch-md1020)
- [[^29]Application Proxy User](#29application-proxy-user)
- [# Scheduled Options](#scheduled-options)
- [Setting Up Consults for Clinical Procedures](#setting-up-consults-for-clinical-procedures)
  - [Step 1 – Setting Up Consult Services](#step-1-setting-up-consult-services)
  - [Step 2 - Creating Consult Procedures](#step-2-creating-consult-procedures)
- [Setting Up CPRS for Clinical Procedures](#setting-up-cprs-for-clinical-procedures)
  - [Step 1 – Setting Up the Notification](#step-1-setting-up-the-notification)
  - [Step 2 – Editing Parameters](#step-2-editing-parameters)
    - [Ask Encounter Update (ORWPCE ASK ENCOUNTER UPDATE)](#ask-encounter-update-orwpce-ask-encounter-update)
    - [Broadcast Messages to Other Apps (ORWOR BROADCAST MESSAGES)](#broadcast-messages-to-other-apps-orwor-broadcast-messages)
    - [Force PCE Entry (ORWPCE FORCE PCE ENTRY)](#force-pce-entry-orwpce-force-pce-entry)
    - [Add CP User to the CPRS Tools Menu (ORWT TOOLS MENU)](#add-cp-user-to-the-cprs-tools-menu-orwt-tools-menu)
  - [[^34]Step 3- Create Ad Hoc Health Summary Components for CP](#34step-3-create-ad-hoc-health-summary-components-for-cp)
- [Working with CP Gateway](#working-with-cp-gateway)
  - [Log File Options](#log-file-options)
- [Setting Up HL7 Parameters](#setting-up-hl7-parameters)
  - [## Configuration Instructions Information](#configuration-instructions-information)
    - [IP Addresses and Ports](#ip-addresses-and-ports)
  - [Setting Up a New HL7 Single Listener for High-Volume Devices](#setting-up-a-new-hl7-single-listener-for-high-volume-devices)
    - [Creating a Logical Link](#creating-a-logical-link)
    - [Creating a Device Protocol Client](#creating-a-device-protocol-client)
    - [Activating the Logical Links](#activating-the-logical-links)
    - [Adding a Device Client as a Server Subscriber](#adding-a-device-client-as-a-server-subscriber)
  - [[^37]Using Port 5000](#37using-port-5000)
    - [Benefits of Using a Single Port Listener](#benefits-of-using-a-single-port-listener)
    - [Setting Up Port 5000](#setting-up-port-5000)
  - [File Settings](#file-settings)
  - [Technical Issues](#technical-issues)
- [Configuring the Automated Instrument Share Folder](#configuring-the-automated-instrument-share-folder)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [Appendix A – CP Application Startup Options and Command Line Switches](#appendix-a-cp-application-startup-options-and-command-line-switches)
  - [Introduction](#introduction-1)
  - [What is a Command Line Switch?](#what-is-a-command-line-switch)
  - [## Shared Broker Environment](#shared-broker-environment)
  - [CPRS Tools Menu](#cprs-tools-menu)
  - [All Command Line Switches](#all-command-line-switches)
- [Appendix B – Exported Procedures List](#appendix-b-exported-procedures-list)
- [Appendix C - Instrument Processing Routines](#appendix-c-instrument-processing-routines)
- [[^40]Appendix D – Exported Values For Hemodialysis Options](#40appendix-d-exported-values-for-hemodialysis-options)
  - [Custom Data List](#custom-data-list)
    - [Anticoagulants](#anticoagulants)
    - [Code Statuses](#code-statuses)
    - [Dialyzer List](#dialyzer-list)
    - [Education Codes](#education-codes)
    - [ESRD Diagnosis](#esrd-diagnosis)
    - [Medication Routes](#medication-routes)
    - [Medication Units](#medication-units)
    - [Modalities](#modalities)
    - [TIU Note Titles](#tiu-note-titles)
    - [Transportation Methods](#transportation-methods)
  - [Preferences](#preferences)
    - [System Preferences](#system-preferences)
    - [The system preferences are exported with the following default values:](#the-system-preferences-are-exported-with-the-following-default-values)
  - [## Report List](#report-list)
    - [### Summary Report Template](#summary-report-template)
- [[^41]Appendix E – High Volume Procedure Checklist](#41appendix-e-high-volume-procedure-checklist)
- [# Appendix F – Consult / Procedure Conversion](#appendix-f-consult-procedure-conversion)
- [Index](#index)
This implementation manual describes how to implement the Clinical Procedures (CP) application. It also contains setup instructions for Consults/Request Tracking, Text Integration Utility (TIU), Computerized Patient Record System (CPRS) and commercial off the shelf (COTS) interfaced devices. All setup instructions and their steps are required for a successful implementation of the Clinical Procedures package.
Topics discussed in this chapter are:
- [About Clinical Procedures](#about-clinical-procedures)
- [Related Manuals](#related-manuals)
- [General CP Package Information](#general-cp-package-information)
- [Resource Requirements](#resource-requirements)
- [Hospital Location File Requirement](#hospital-location-file-requirement-implementing-workload-reporting)

## About Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A clinical procedure is a clinical test where the result is usually obtained from an automated instrument such as pulmonary function devices, EKGs, ECHOs, EMGs, EEGs, endoscopy and bronchoscopy instruments, dialysis machines, or other similar COTS devices. CP is a conduit for passing final patient results, using Health Level 7 (HL7) messaging, between vendor clinical information systems (CIS) and Veterans Health Information Systems and Technology Architecture (VistA). The patient’s test result or report is displayed through the Computerized Patient Record System (CPRS). The report data is stored on the Imaging Redundant Array of Inexpensive Disks (RAID) and in some instances, discrete data is stored in the Medicine database.

CP provides features that can be used across clinical departments such as general medicine, cardiology, pulmonary, women’s health, neurology, and rehabilitation medicine. CP uses the procedure order function that is included with the Consults/Procedures package. For example, a clinician places an order for a procedure, such as an EKG, in the Consults/Procedures application.

If the procedure is performed on a bi-directional instrument, the patient demographics are automatically transmitted to the instrument. When the procedure is complete, the result is then transmitted back to VistA. The result is stored in VistA Imaging and associated with a TIU document. The result and the TIU document are then associated with the original Consults order.

If the procedure is performed on a uni-directional instrument, then the clinician must use the CP User application to match the instrument results to the procedure order. Then the clinician submits the results to Imaging and creates the TIU document. Once the TIU document is in place, standard Consults functionality is used to complete and sign the TIU document.

The following pages contain flowcharts explaining the bi-directional and uni-directional Clinical Procedures process flow.

Clinical Procedures Bi-Directional Interface Process Flow:

Clinical Procedures Uni-Directional Interface Process Flow:

This is a flowchart describing the configuration of Clinical Procedures:

Legend:

### ### About CP User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP User checks in a procedure request for a study. CP User also links the result from the automated instrument to the procedure ordered through Consults in CPRS. With CP User, if the device is bi-directional, the clinician manages the results and submits them to the requested device. The results then are automatically processed by CP Gateway, stored in VistA Imaging, and are ready for review within Consults. If the instrument is uni-directional, the clinician has to associate the results and submit them to the VistA Imaging system for storage. These attachments display under the appropriate TIU document for the original Consults order.

### About CP Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Manager is used to configure the site files, CP INSTRUMENTS, CP PROCEDURES and required system parameters. It is recommended that access to CP Manager be restricted to users who manage the CP applications.

### About CP Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Gateway manages the flow of information from the instrument interfaces to the studies. CP Gateway polls VistA regularly for new data from instruments and processes this data into usable attachments for the VistA Imaging system. This module also manages the log files and purges log file entries.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation Guide is intended for use by Clinical Application Coordinators (CAC), Technical Support Office (TSO), Information Resource Management (IRM), implementation managers, and Enterprise VistA Support (EVS). Each team member is responsible for different aspects of the implementation, and then the maintenance of the product.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of related manuals that you may find helpful:

> Clinical Procedures Installation Guide

> Clinical Procedures Technical Manual and Package Security Guide

> Clinical Procedures User Manual

> Clinical Procedures Release Notes

> CPRS User Guide: GUI Version

> CPRS Setup Guide

> Consult/Request Tracking User Manual

> Consult/Request Tracking Technical Manual

> Text Integration Utilities (TIU) Implementation Guide

> Text Integration Utilities (TIU) User Manual

> VistA Imaging System (Clinical) User Manual

These manuals can be found in the [VistA Documentation Library (VDL)](http://www.va.gov/vdl/), <http://www.va.gov./vdl>. Select Clinical from the VDL web page, select the package you want, and then select the manuals. For example, you can select CPRS on the left side of the page. The list of CPRS manuals is displayed.

[^1] You may also want to read the CP Implementation Process (Webpage), which is available on the CP website. Go to <http://vista.med.va.gov/ClinicalSpecialties/clinproc/>.

Point to Clinical Procedures Project, then click Documentation. When the Documentation page displays, click Clinical Procedures Documents, then click The CP Implementation Process (Webpage). This list includes a high-level step-by-step guide to the installation and the implementation process.

## General CP Package Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Name spacing and file listing.

Clinical Procedures is found in the MD namespace. All routines, templates and options begin with MD. File numbers range from 702 to 704 and are stored in the ^MDD and ^MDS globals. The range of 704.201 to 704.209 is stored in the ^MDK global. Here is a list of the Clinical Procedures files:

> \#702 CP Transaction

> \#702.01 CP Definition

> \#702.09 CP Instrument

> \#703.1 CP Result Report

> [^2]\#703.9 CP Conversion File

> \#704.201 Hemodialysis Access Points File

> \#704.202 Hemodialysis Study File

> \#704.209 Hemodialysis Setting File

2.  Queuing TaskMan jobs.

[^3]Queued TaskMan jobs are associated with this application. Here is a list of options that can be scheduled:

MD SCHEDULED STUDIESMD STUDY CHECK-INMD PROCESS NOSHOW/CANCELMD PROCESS RESULTS

3.  Accessing modules.
- Assign the option \[MD GUI USER\] to the clinical staff, who need access to CP User.
- Assign the option \[MD GUI MANAGER\] to the Clinical Application Coordinator, CP package coordinator, and Information Resource Management Service (IRMS) staff for access to CP Manager.
- Assign the MD MANAGER key to the Clinical Application Coordinator or the CP Package Coordinator. This key controls access to the Update Study Status menu option that allows clinicians to fix study errors. This key also controls access to the Delete Study option.
- Assign the MAGCAP CP user security key to technicians, who will be using VistA Imaging to capture a consent form and link it to a CP study or TIU document.
4.  [^4]Assigning Options:
- Assign the option \[MD COORDINATOR\] to the Clinical Application Coordinator, CP package coordinator, and Information Resource Management Service (IRMS) staff for access to the setup option for the auto study check-in.
- Assign the option \[MD PROC W/INCOMPLETE WORKLOAD\] to the Clinical Application Coordinator, CP package coordinator, and Information Resource Management Service (IRMS) staff to print a list of procedure with incomplete workload.
- Assign the option \[MD STUDIES LIST\] to the Clinical Application Coordinator, CP package coordinator, and Information Resource Management Service (IRMS) staff to print a list of studies list.

> The screen captures below demonstrate how to assign an option to a user:

> ► Use the \[XUSER\] User Management menu option.

> Select OPTION NAME: XUSER

> 1 XUSER User Management

> 2 XUSER DIV CHG Change my Division

> 3 XUSER FILE MGR Manage User File

> 4 XUSER KEY RE-INDEX Reindex the users key's

> 5 XUSER PC BUILD User PC build Print

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: 1 XUSER User Management

► Select \[XUSEREDIT\] Edit An Existing User option.

> Select User Management Option: ?

> Add a New User to the System

> Grant Access by Profile

> Edit an Existing User

> Deactivate a User

> Reactivate a User

> List users

> User Inquiry

> Switch Identities

> File Access Security ...

> Clear Electronic signature code

> Electronic Signature Block Edit

> Manage User File ...

> OAA Trainee Registration Menu ...

> Person Class Edit

> Reprint Access agreement letter

> Select User Management Option: EDit an Existing User

► Select the user.

> Select User Management Option: EDit an Existing User

> Select NEW PERSON NAME: TEST

> 1 TEST,A TA

> 2 TEST,CARL TC PHYSICIAN

> 3 TEST,CAROLE CJT ISC COMPUTER SPECIALIST

> 4 TEST,FRANCE FT

> 5 TEST,KEN RADIOLOGIST

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: 1 TEST,A TA

► Enter the option name, MD COORDINATOR, to the Select SECONDARY MENU OPTIONS: field.

> Edit an Existing User

> NAME: TEST,A Page 1 of 5

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> NAME... TEST,A INITIAL: TA

> TITLE: NICK NAME:

> SSN: 666435465 DOB:

> DEGREE: MAIL CODE:

> DISUSER: TERMINATION DATE:

> Termination Reason:

> PRIMARY MENU OPTION:

> Select SECONDARY MENU OPTIONS: MD COORDINATOR

> Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE:

> Want to edit VERIFY CODE (Y/N):

> Select DIVISION:

> SERVICE/SECTION: IRM FIELD OFFICE

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> High Volume Procedure Setup

> Are you adding 'MD COORDINATOR' as

> a new SECONDARY MENU OPTIONS (the 1ST for this NEW PERSON)? No// Y

► Verify the SECONDARY MENU OPTIONS field has the option name MD COORDINATOR and enter a four characters SYNONYM for the option name.

> Edit an Existing User

> NAME: TEST,A Page 1 of 5

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> NAME... TEST,A INITIAL: TA

> TITLE: NICK NAME:

> SSN: 666435465 DOB:

> DEGREE: MAIL CODE:

> DISUSER: TERMINATION DATE:

> Termination Reason:

> ┌────────────────────────────────────────────────────────┐

> Select │ SECONDARY MENU OPTIONS │

> Want to │ │

> Want to │ SECONDARY MENU OPTIONS: MD COORDINATOR │

> │ SYNONYM: COOR │

> │ │

> └────────────────────────────────────────────────────────┘

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND:

►Enter additional SECONDARY MENU OPTIONS.

> Edit an Existing User

> NAME: TEST,A Page 1 of 5

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> NAME... TEST,A INITIAL: TA

> TITLE: NICK NAME:

> SSN: 666435465 DOB:

> DEGREE: MAIL CODE:

> DISUSER: TERMINATION DATE:

> Termination Reason:

> PRIMARY MENU OPTION:

> Select SECONDARY MENU OPTIONS:

> Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE:

> Want to edit VERIFY CODE (Y/N):

> Select DIVISION:

> SERVICE/SECTION: IRM FIELD OFFICE

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

►When you are finished, enter “SAVE” at the COMMAND field to save the data and enter “EXIT” to exit the editor.

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: SAVE Press \<PF1\>H for help Insert

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: EXIT Press \<PF1\>H for help Insert

► Once the option(s) are added, the person can enter “??” at the primary menu option to get a listing of the secondary menu option and can see the new added option(s).

> Select Core Applications Option: ??

> You can also select a secondary option:

> AUTO Auto Study Check-In Setup \[MD AUTO CHECK-IN SETUP\]

> GI GI Menu ... \[MCARGIUSER\]

> HEVD CM Troubleshooter Clinician ... \[ORRCMM TROUBLESHOOTER CLIN\]

> COOR CP Coordinator Menu ... \[MD COORDINATOR\]

> LIST Clinical Procedures Studies List \[MD STUDIES LIST\]

> MAGS Imaging System Manager Menu ... \[MAG SYS MENU\]

> \*\*\> Locked with MAG SYSTEM

> PFT Pulmonary Menu ... \[MCARPULMUSER\]

> RA Rad/Nuc Med Total System Menu ... \[RA OVERALL\]

> TIU TIU Maintenance Menu ... \[TIU IRM MAINTENANCE MENU\]

> WKLD Print list of Procedure with incomplete workload \[MD PROC W/INCOMPLETE

> WORKLOAD\]

5.  Printer issues.

All reports are printed to Client (Windows) printers.

6.  Online Help.

Online help is available when questions arise. Click Help or choose Help from the menu bar. You can also press F1 for help on a specific window.

7.  Automatic Version Updates.

CP applications (client and server) do not contain automatic update capabilities. You must remove the previous version before you can install the new version.

8.  Command line switches.

For alternate methods of running Clinical Procedures, refer to [Appendix A - CP Application Startup Options and Command Line Switches](#appendix-a-cp-application-startup-options-and-command-line-switches), p. [10-6](#add-cp-user-to-the-cprs-tools-menu-orwt-tools-menu).

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Procedures can only run at sites that are running VistA Imaging V. 3.0.
- Workstations must run Windows 2000 or later. 12 MB of available disc space is required.

> VistA Server resources:

<u>Globals</u> <u>Type of Data</u> <u>Size</u>

^MDS Static global 25 k

^MDD Patient data for the 25-75 k/patient

Clinical Procedures

^MDK Hemodialysis Studies 25-75 k/patient

> NOTE: These globals must all bejournaled.

## Hospital Location File Requirement (Implementing Workload Reporting)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Be sure that the hospital location entry (Hospital Location \#44 file) for each CP procedure contains the correct Institution field entry. The Hospital Location is used for workload reporting. (The Institution field tells VistA Imaging where to store the images on the server. If there is no Institution field, CP defaults to the institution of the user who logged on to CP Gateway.)

## VistA Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Providers at a site must use the VistA Imaging Display client to view CP results and reports. Be sure that VistA Imaging V.3.0 or greater and Patch 7 of Imaging V.3.0 (MAG\*3.0\*7) are installed.

# Using CP Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes how to use CP Manager.

Topics discussed in this chapter are:

- [CP Manager Toolbar](#cp-manager-toolbar)
- [Finding a Parameter](#finding-a-parameter)
- [Deleting an Automated Instrument or Procedure](#deleting-an-automated-instrument-or-procedure)
- [Printing Reports](#printing-reports)

## CP Manager Toolbar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of icon descriptions:

![](clinical-procedures-version-1-implementation-guide/002.png) New Instrument - Creates a new instrument.

![](clinical-procedures-version-1-implementation-guide/003.png) New Procedure - Creates a new procedure.

![](clinical-procedures-version-1-implementation-guide/004.png) Make a Copy of the Selected Item – Creates a copy of the selected instrument or procedure.

![](clinical-procedures-version-1-implementation-guide/005.png) Undo Changes - Cancels changes made since that last save to the current screen.

![](clinical-procedures-version-1-implementation-guide/006.png) Save - Saves changes made to current screen.

![](clinical-procedures-version-1-implementation-guide/007.png) Delete - Deletes an instrument or procedure.

![](clinical-procedures-version-1-implementation-guide/008.png) Print a Report - Prints reports listing instruments, procedures, or system parameters.

![](clinical-procedures-version-1-implementation-guide/009.png) Find a Parameter - Finds an instrument or procedure.

![](clinical-procedures-version-1-implementation-guide/010.png) Calculate a File’s CRC Value - Calculates a file’s CRC (Cyclical Redundancy Check) value.

![](clinical-procedures-version-1-implementation-guide/011.png) Instrument Analyzer - Indicates whether an instrument is ready for use or not and why.

![](clinical-procedures-version-1-implementation-guide/012.png) Refresh - Refreshes the parameter listing on the left side of the Clinical Procedures Manager screen.

![](clinical-procedures-version-1-implementation-guide/013.png) Help - Provides online help for this package.

![](clinical-procedures-version-1-implementation-guide/014.png) Clinical Procedures Home Page - Goes to the Clinical Procedures Home Page on the Web.

## Finding a Parameter 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option when you want to find a specific automated instrument or procedure.

1.  Select Tools \> Find a Parameter.
2.  Enter a partial or complete name of the instrument or procedure.
3.  Click OK to begin the search.
4.  If you find the parameter that you are searching for, click Yes on the confirmation window. The edit window for the parameter is displayed.

## Deleting an Automated Instrument or Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may want to delete an instrument or a procedure that you are no longer using at your site. Before you delete an instrument or procedure, be sure that the CP procedure is not linked to a Consult procedure. (You cannot delete a procedure that is linked to Consults.) If you already used the CP procedure, then it is already linked to Consults. If the CP procedure is associated with a consult procedure, you must remove the links before you can delete the procedure.

To ensure that the links are removed, you can use FileMan to view the CP Definition file. If the CONSULT PROCEDURE column of the report is empty, then you know that there aren’t any Consults/Procedure entries pointing to the definition. Here’s an example of the report:

Using FileMan, do the following...

Select OPTION: 2 PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: CP DEFINITION

SORT BY: NAME// \<Ret\>

START WITH NAME: FIRST// \<Ret\>

FIRST PRINT FIELD: .01;L30;"CP DEFINITION"

THEN PRINT FIELD: GMRC PROCEDURE:

By 'GMRC PROCEDURE', do you mean the GMRC PROCEDURE File,

pointing via its 'CLINICAL PROCEDURE' Field ("AC" Cross-reference)? Yes// Y

THEN PRINT GMRC PROCEDURE FIELD: .01;L30;"CONSULT PROCEDURE"

THEN PRINT GMRC PROCEDURE FIELD: \<Ret\>

THEN PRINT FIELD: \<Ret\>

Heading (S/C): CP DEFINITION LIST// CP DEFINITIONS AND RELATED CONSULT PROCEDURES

STORE PRINT LOGIC IN TEMPLATE: \<Ret\>

DEVICE: HOME

CP DEFINITIONS AND RELATED CONSULT PROCEDURES FEB 6,2004 09:12 PAGE 1

CP DEFINITION CONSULT PROCEDURE

--------------------------------------------------------------------------------

ANO SINGLE TUMOR (HOT/BICAP)

ANOSCOPY

ARRHYTHMIA INDUCTION BY PACING ARRYTHMIA

ARTERIAL BLOOD GASES

ARTERIAL CANNULATION

ARTERIAL PUNCTURE

BIOPSY LUNG, PERCUTANEOUS NDL

BIOPSY, PLEURA

BONE MARROW BONE MARROW ASPIRATE

BONE MARROW INTERPRETATION BONE MARROW BIOPSY

BONE MARROW ASSESSMENT

BRONC DIAGNOSTIC W/BAL

BRONC W/BRONC WASHING BRONCHOSCOPY

BRONC W/TRANSBRONC LUNG BX

BRONCHOSCOPY, LASER

BRONCHOSCOPY, STENT PLACEMENT

After you have determined that the CP procedure is not linked to Consults, follow these steps to delete.

1.  Use the GMRC MGR menu option. Under the Setup Procedure option, delete the CP procedure from the CLINICAL PROCEDURE field.
2.  Logon to CP Manager.
3.  Display the list of automated instruments or procedures on the CP Manager window.
4.  Click the name of the instrument or procedure that you want to delete.
5.  Select File \> Delete.
6.  Click Yes to confirm the deletion.

## Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can print a listing of automated instruments, procedures, or system parameters. You can also print a detailed report of a selected instrument or procedure.

To print a list of instruments, procedures or system parameters, do the following:

1.  Select File \> Print.
2.  Select Automated Instruments, Procedures, or System Parameters. If you previously selected a specific instrument or procedure, you can also select that instrument or procedure name.
3.  Click OK to print.

To print a report of a selected instrument or procedure:

1.  Select the instrument or procedure name.
2.  Select File \> Print.
3.  From the list of available reports, select the procedure or instrument. You may have to enter a report title.
4.  Click OK to print.

Example of an Automated Instruments report:

|                           |                |               |                             |         |            |
|---------------------------|----------------|---------------|-----------------------------|---------|------------|
| Automated Instruments |                |               | Printed: 7/10/03 3:34:21 PM |         |            |
| NAME                  | PRINT NAME | SERIAL \# | M RTN                   | PKG | ACTIVE |
| CLINIVISION               | Clinivision    | CL58374       | MDHL7R1                     | CP V1.0 | No         |
| MUSE                      | Muse           | M8372J2       | MDHL7M1                     | CP V1.0 | Yes        |
| MUSE EKG                  | Muse EKG       | M8372J2       | MDHL7M1                     | CP V1.0 | Yes        |
| OLYMPUS                   | Olympus        | O46237A       | MDHL7E                      | CP V1.0 | Yes        |
| OLYMPUS EGD               | Olympus EGD    | O46237A       | MDHL7E                      | CP V1.0 | Yes        |
| \[End of Report\]         |                |               |                             |         |            |
|                           |                |               |                             |         |            |
|                           |                |               |                             |         |            |
|                           |                |               |                             |         |            |
| Clinical Procedures V1.0  |                |               | Page: 1                     |         |            |

Example of a Procedures report:

|                          |                        |                 |                             |            |              |
|--------------------------|------------------------|-----------------|-----------------------------|------------|--------------|
| Procedures           |                        |                 | Printed: 7/10/03 3:34:30 PM |            |              |
| NAME                 | TREATING SPECIALTY | TIU NOTE    | LOCATION                | ACTIVE | EXT DATA |
| BIOPSY LUNG              | PULMONARY              | PULMONARY NOTE  | PULMONARY CLINIC            | No         | No           |
| ECHO                     | CARDIOLOGY             | CARDIOLOGY NOTE | CARDIOLOGY CLINIC           | Yes        | Yes          |
| EGD DIAGNOSTIC           | GASTROENTEROLOGY       | EGD NOTE        | GI LAB                      | Yes        | Yes          |
| HOLTER                   | CARDIOLOGY             | CARDIOLOGY NOTE | CARDIOLOGY CLINIC           | Yes        | No           |
| PACEMAKER FOLLOWUP       | CARDIOLOGY             | CARDIOLOGY NOTE | CARDIOLOGY CLINIC           | Yes        | Yes          |
| \[End of Report\]        |                        |                 |                             |            |              |
|                          |                        |                 |                             |            |              |
|                          |                        |                 |                             |            |              |
|                          |                        |                 |                             |            |              |
| Clinical Procedures V1.0 |                        |                 | Page: 1                     |            |              |

Example of a System Parameters report:

|                                                                         |                             |                       |
|-------------------------------------------------------------------------|-----------------------------|-----------------------|
| System Parameters                                                   | Printed: 7/10/03 3:34:40 PM |                       |
| System Parameters For: <span class="mark">REDACTED</span>           |                             |                       |
| Parameter: MD ALLOW EXTERNAL ATTACHMENTS                                |                             | Type: yes/no          |
| Description: Allow non-instrument attachments                           |                             | Multiple: No          |
| Value: NO                                                               |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD CRC BYPASS                                                |                             | Type: yes/no          |
| Description: Bypass CRC Checking                                        |                             | Multiple: No          |
| Value: YES                                                              |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD CRC VALUES                                                |                             | Type: free text       |
| Description: Clinical Procedures CRC Values                             |                             | Multiple: Yes         |
| Values:                                                                 |                             |                       |
| CPGATEWAY.EXE.1.0.0.20 = ODCE4C31                                       |                             |                       |
| CPGATEWAY.EXE.1.0.0.21 = ODCE4C31                                       |                             |                       |
| CPMANAGER.EXE.1.0.0.20 = CB12FEE0                                       |                             |                       |
| CPMANAGER.EXE.1.0.0.21 = CB12FEE0                                       |                             |                       |
| CPUSER.EXE.1.0.0.20 = B819E183                                          |                             |                       |
| CPUSER.EXE.1.0.0.21 = B819E183                                          |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD DAYS FOR INSTRUMENT DATA                                  |                             | Type: numeric         |
| Description: Temporary instrument data life (Days)                      |                             | Multiple: No          |
| Value: 2                                                                |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD FILE EXTENSIONS                                           |                             | Type: free text       |
| Description: Imaging File Types                                         |                             | Multiple: Yes         |
| Values:                                                                 |                             |                       |
| .bmp = Bitmap Images                                                    |                             |                       |
| .doc = MS Word files                                                    |                             |                       |
| .html = Hypertext Markup Language files                                 |                             |                       |
| .jpeg = JPEG Images                                                     |                             |                       |
| .jpg = JPEG Images                                                      |                             |                       |
| .pdf = Portable Document Format                                         |                             |                       |
| .rtf = Rich text files                                                  |                             |                       |
| .tiff = TIFF Graphics                                                   |                             |                       |
| .txt = Text files                                                       |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD HFS SCRATCH                                               |                             | Type: free text       |
| Description: VistA Scratch HFS Directory                                |                             | Multiple: No          |
| Value: USER\$:\[HFS\]                                                   |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD IMAGING XFER                                              |                             | Type: free text       |
| Description: Imaging Network Share                                      |                             | Multiple: No          |
| Value: \\Ish-imaging\Uploads                                            |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD OFFLINE MESSAGE                                           |                             | Type: word processing |
| Description: Offline message                                            |                             | Multiple: No          |
| WP-Text:                                                                |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD ONLINE                                                    |                             | Type: yes/no          |
| Description: Clinical Procedure Online/Offline                          |                             | Multiple: No          |
| Value: YES                                                              |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD VERSION CHK                                               |                             | Type: YES/NO          |
| Description: Version Compatibility                                      |                             | Multiple: Yes         |
| Values:                                                                 |                             |                       |
| CPGATEWAY.EXE.1.0.0.20 = YES                                            |                             |                       |
| CPGATEWAY.EXE.1.0.0.21 = YES                                            |                             |                       |
| CPMANAGER.EXE.1.0.0.20 = YES                                            |                             |                       |
| CPMANAGER.EXE.1.0.0.21 = YES                                            |                             |                       |
| CPUSER.EXE.1.0.0.20 = YES                                               |                             |                       |
| CPUSER.EXE.1.0.0.21 = YES                                               |                             |                       |
|                                                                         |                             |                       |
| Parameter: MD WEBLINK                                                   |                             | Type: free text       |
| Description: Clinical Procedures Home Page                              |                             | Multiple: No          |
| Value: <span class="mark">REDACTED</span>/ClinicalSpecialties/clinproc/ |                             |                       |
| \[End of Report\]                                                       |                             |                       |
| Clinical Procedures V1.0                                                |                             | Page: 1               |

Example of a report for an individual automated instrument:

|                                          |                             |
|------------------------------------------|-----------------------------|
| Instrument - Muse EKG                | Printed: 7/10/03 3:34:51 PM |
| Instrument Name: Muse EKG            |                             |
|                                          |                             |
| Notification Mailgroup: MD DEVICE ERRORS |                             |
| Description: Muse EKG Device Interface   |                             |
| Delete when submitted: \<Blank\>         |                             |
| Printable Name: Muse EKG                 |                             |
| Default Ext.: \<Blank\>                  |                             |
| Serial Number: M8372J2                   |                             |
| Active: Yes                              |                             |
| M Routine: MDHL7M1                       |                             |
| Pkg Code: CP V1.0                        |                             |
| Bi-Directional Instrument: Yes           |                             |
| IP Address: 10.3.25.28                   |                             |
| Port: 9300                               |                             |
| HL7 Inst ID: Muse EKG                    |                             |
| HL7 Unv Svc ID: 93000=EKG                |                             |
| HL7 Link: MCAR OUT                       |                             |
| Server Name: \<Blank\>                   |                             |
| Share Name: \<Blank\>                    |                             |
| Path Name: \<Blank\>                     |                             |
| Executable Name: \<Blank\>               |                             |
| UNC: \<Blank\>                           |                             |
| Text: \<Blank\>                          |                             |
| URL: \<Blank\>                           |                             |
| DLL: \<Blank\>                           |                             |
| UUEncode: Yes                            |                             |
| XML: \<Blank\>                           |                             |
| XMS: \<Blank\>                           |                             |
| \[End of Report\]                        |                             |
|                                          |                             |
|                                          |                             |
|                                          |                             |
|                                          |                             |
| Clinical Procedures V1.0                 | Page: 1                     |

Example of a report for an individual procedure:

|                                                            |                             |
|------------------------------------------------------------|-----------------------------|
| Procedure - ECHO                                       | Printed: 7/10/03 3:35:02 PM |
| Procedure Name: ECHO                                   |                             |
|                                                            |                             |
| Treating Specialty: CARDIOLOGY                             |                             |
| Require External Data: Yes                                 |                             |
| TIU Note Title: CARDIOLOGY NOTE                            |                             |
| Hospital Location: CARDIOLOGY CLINIC                       |                             |
| Auto Submit to VistA Imaging: Yes, Submit to VistA Imaging |                             |
| External Attachment Directory: /CARDPATH                   |                             |
| Active: Yes                                                |                             |
|                                                            |                             |
| Associated Instruments:                                    |                             |
| ------------------------------                             |                             |
| MUSE                                                       |                             |
| \[End of Report\]                                          |                             |
|                                                            |                             |
|                                                            |                             |
|                                                            |                             |
|                                                            |                             |
| Clinical Procedures V1.0                                   | Page: 1                     |

# About Test Accounts and Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to prevent Imaging System conflicts at sites where a mirror of a VistA account has been created for test purposes. Be sure to follow the instructions in this section before you add any new images to the test account. These steps are required.

> **NOTE:** This section assumes that the test account has already been created.

> **CAUTION:** The changes described in this section are intended for test accounts only. Making these changes in a production account can compromise the Imaging database and could result in the loss of patient data.

Topics discussed in this chapter are:

- [Changing All Test Accounts](#changing-all-test-accounts)
- [Changing Test Accounts that Use a Background Processor](#changing-test-accounts-that-use-a-background-processor)
- [Connecting the PC to VistA Servers](#connecting-the-background-processor-pc-to-vista-servers)
- [Refreshing Existing Test Accounts](#refreshing-existing-test-accounts)

## Changing All Test Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all test accounts, you must change the current namespace and set the imaging network location operational status.

> **CAUTION:** The changes described in this section are intended for test accounts only. Making these changes in a production account can compromise the Imaging database and may result in the loss of patient data.

### Changing the Current Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must change the value of Current Namespace (2006.1, .02) to prevent test images from mixing with and in some cases overwriting actual patient images. Using VA FileMan, change the Current Namespace field in the IMAGING SITE PARAMETERS file to ZZ as follows:

> DVA\>D P^DI

> VA FileMan 22.0

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: IMAGING SITE PARAMETERS// 2006.1 IMAGING SITE PARAMETERS

> (1 entry)

> EDIT WHICH FIELD: ALL// .02 CURRENT NAMESPACE

> THEN EDIT FIELD: \<enter\>

> Select IMAGING SITE PARAMETERS NAME: \`1 IMGDEM01. <span class="mark">REDACTED</span>

> CURRENT NAMESPACE: AB// ZZ

> Select IMAGING SITE PARAMETERS NAME:

> **NOTE:** If you have more than one million entries in the Imaging file (2005), use a single character for the namespace, such as Z.

After this change is made, the first image captured to the test account creates the ZZ directory on the VistA Imaging file servers. All test account images are stored in the ZZ directory and include the ZZ prefix in their file names such as, ZZ123456.tga.

> **NOTE:** For test accounts at multi-divisional sites that are running the VistA Imaging “Consolidated Code,” you must modify the Current Namespace field for each division defined in the file. Make the value for each instance of Current Namespace unique, such as ZX, ZY, or ZZ.

Setting the Imaging Network Location Status

Be sure the Imaging Network Location status for the test account is set to “online”. There is an option on the Background Processor that lets you view each network and changes its status. Select Edit \> Network Location Manager (Figure 3‑1), and then select the Online Status checkbox (Figure 3‑2).

![](clinical-procedures-version-1-implementation-guide/015.png)

Figure 3‑1

![](clinical-procedures-version-1-implementation-guide/016.png)

Figure 3‑2

### Configuring the Imaging Display Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Imaging Display Station wants to use the test account, the station needs to know the name and port number of the account. Run MAGSYS.EXE to edit the MAG.INI file. For the procedure, refer to the Imaging System Installation Guide, V. 3.0. (<http://vaww.va.gov/imaging/IMGinstallgd.pdf>)

## Changing Test Accounts that Use a Background Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a Background Processor is needed for the test account, you must make the following changes:

1.  Delete test account entries in the Background Processor Queue files. You need to delete the entries to keep the test Background Processor from reprocessing tasks left over from the production account. Use VA FileMan to delete all entries in the following two files:

IMAGE BACKGROUND QUEUE file (2006.03)

IMAGE BACKGROUND QUEUE POINTER file (2006.031)

> Caution: Only perform these steps on a test account. Use extreme caution when deleting all entries in a file.

> DVA\>D P^DI

> VA FileMan 22.0

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: IMAGE BACKGROUND QUEUE// 2006.03 IMAGE BACKGROUND QUEUE

> (6543 entries)

> EDIT WHICH FIELD: ALL// .01///@

> WARNING: THIS MEANS AUTOMATIC DELETION!! QUEUE NAME

> THEN EDIT FIELD: \<enter\>

> Select IMAGE BACKGROUND QUEUE QUEUE NAME: ^LOOP

> EDIT ENTRIES BY: QUEUE NAME// \<enter\>

> START WITH QUEUE NAME: FIRST// \<enter\>

> ...

> JUKEBOX

> JUKEBOX

> JUKEBOX

> JUKEBOX

> LOOP ENDED!

> Select IMAGE BACKGROUND QUEUE QUEUE NAME: ^

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: IMAGE BACKGROUND QUEUE// 2006.031 IMAGE BACKGROUND QUEUE

> POINTER (5 entries)

> EDIT WHICH FIELD: ALL// .01///@

> WARNING: THIS MEANS AUTOMATIC DELETION!! QUEUE NAME

> THEN EDIT FIELD: \<enter\>

> Select IMAGE BACKGROUND QUEUE POINTER QUEUE NAME: ^LOOP

> EDIT ENTRIES BY: QUEUE NAME// \<enter\>

> START WITH QUEUE NAME: FIRST// \<enter\>

> ABSTRACT

> GCC

> IMPORT

> JBTOHD

> JUKEBOX

> LOOP ENDED!

> Select IMAGE BACKGROUND QUEUE POINTER QUEUE NAME:

2\. Configure the Background Processor being used in the test account to process only the ABSTRACTS and IMPORT queues. Turn off all other queue processing. Use the BP Workstation Parameters option to configure queue processing.

> a\. From the Background Processor, choose Edit \> BP Workstation Parameters.

> b\. If there are multiple Background Processors listed in the top dialog, select the one that is being used for the test account.

> c\. Ensure that only the options shown below are selected.

> ![](clinical-procedures-version-1-implementation-guide/017.png)

Figure 3‑3

> d\. When you are finished, close the dialog.

> Note: If you need to test the JUKEBOX, JBTOHD, or GCC queue-processing functions, you need to add new entries to the Network Locations file (2005.2) to prevent conflicts with the with the production account. For assistance, contact the VistA Imaging support team.

> Caution: Using the DELETE queue processing function on a test account can lead to the deletion of image files on the production account. If it is necessary to use the DELETE queue processing function in the test account, contact the VistA Imaging support team.

3\. Decide if you want to setup the test Background Processor on its own PC, or as a second instance on the same PC with the existing Background Processor. If you plan to setup the test and production Background Processor on the same PC, go to the next section, Connecting the PC to VistA Servers.

## Connecting the Background Processor PC to VistA Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If both a test and production Background processor are running on the same PC, you need to connect the PC to the VistA production server and test server. You make this connection by editing the Windows Registry. If DNS or WINS cannot resolve the computer names entered in the registry, you will need to make further changes in the PC’s HOSTS file.

1\. Registry Changes

> Add the “string value” for each VistA Server to the Registry key and use the following syntax:

> \< VistA Server name\>,\<Broker port\> (i.e. VistA -Live,9200)

> HKEY_LOCALMACHINE\Software\Broker\Servers registry key.

> Sample entries are shown below.

> ![](clinical-procedures-version-1-implementation-guide/018.png)

Figure 3‑4

> You can edit the Registry with ServerList.exe (a utility distributed with the RPC Broker development toolkit) or manually with regedit.exe. See the RPC Broker System Guide for more detailed information on using ServerList.exe to edit the registry.

> Caution: Use extreme caution when editing the registry manually. Improper changes can leave your system unstable or non-functional. The VA recommends that you edit the registry with ServerList.exe.

2\. Editing the HOSTS File

> If your site cannot use DNS or WINS to resolve the names added to the registry, you need to create entries in your HOSTS file for each entry added to the registry. A sample HOSTS is shown below.

> \#HOSTS file

> 152.128.12.44 VistA-Live BROKERSERVER DHCPSERVER

> 152.128.11.23 VistA-Test

> \#END

> The HOSTS file has no file extension. It is located in WINNT\SYSTEM32\DRIVERS\ETC.

## Refreshing Existing Test Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a test account is refreshed with a copy of a production account, be sure to repeat the following steps:

- Changing the Current Namespace.
- Deleting test account entries in the Background Processor Queue files.
- Configure the Background Processor used in the Test Account. See [Connecting the PC to VistA Servers](#connecting-the-background-processor-pc-to-vista-servers), p. [3-9](#connecting-the-background-processor-pc-to-vista-servers).

Also, be sure to manually delete the ZZ folder on the VistA Imaging file servers.

# Setting Up TIU for Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the steps to follow to set up TIU for CP. The purpose of setting up TIU is to design the CP document hierarchy that creates the TIU document title, which is displayed to an authorized “Interpreter.” The procedures in this section describe how to configure the new Clinical Procedures Class in TIU. Be sure to follow these steps in sequential order.

Topics discussed in this chapter are:

- [Step 1 – Verify Clinical Procedures Class Upload Header](#step-1---verify-clinical-procedures-class-upload-header)
- [Step 2 – Create CP Class Document Definitions](#step-2---create-cp-class-document-definitions)
- [Step 3 – Define Clinical Procedures Class Document Parameters](#section-1)

> **NOTE:** Be sure the TIU Enhancement for Clinical Procedures patch (TIU\*1\*109) is installed before you set up TIU.

## Step 1 - Verify Clinical Procedures Class Upload Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Upload Utility option displays information about how headers are formatted for dictated documents, which are transcribed offline and uploaded into VistA. This option also displays "blank" character, major delimiter and end of message signal as defined by your site. If the Clinical Procedure CLASS output does not match Figure 4‑1, check to see if the TIU\*1.0\*109 patch was installed. The upload header for the Clinical Procedures Class is automatically set up when the TIU\*1.0\*109 patch is installed.

[^5] To verify that the upload header is appropriately defined for the Clinical Procedures Class, use the option \[TIU UPLOAD HELP\]. The output will look something like this:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Upload Utility: Access the following option:</p>
<p>Help for Upload Utility [TIU UPLOAD HELP]</p></td>
</tr>
<tr class="even">
<td>Select DOCUMENT DEFINITION: <strong>CLINICAL PROCEDURES CLASS</strong></td>
</tr>
<tr class="odd">
<td><p>$HDR: CLINICAL PROCEDURES</p>
<p>TITLE: GENERAL PROCEDURE</p>
<p>SSN: 666-12-1234</p>
<p>VISIT/EVENT DATE: 5/15/2001@08:15</p>
<p>AUTHOR: CPRSPROVIDER,ONE</p>
<p>DATE/TIME OF DICTATION: 5/16/2001@09:25</p>
<p>LOCATION: MEDICAL-CONSULT 6200</p>
<p>EXPECTED COSIGNER: CPRSPROVIDER,TWO</p>
<p>CONSULT REQUEST NUMBER: 1455</p>
<p>TIU DOCUMENT NUMBER: 543</p>
<p>PROCEDURE SUMMARY CODE: Normal</p>
<p>DATE/TIME PERFORMED: 5/15/2001@08:00</p>
<p>$TXT</p>
<p>CLINICAL PROCEDURES Text</p>
<p>* File should be ASCII with width no greater than 80 columns.</p>
<p>* Use "@@@" for "BLANKS" (word or phrase in dictation that isn't understood).</p></td>
</tr>
</tbody>
</table>

Figure 4‑1

## Step 2 - Create CP Class Document Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to create CP document classes and titles. A Document Definition provides the building blocks for the TIU package. A Document Definition organizes a document into a hierarchical structure. This structure allows documents to inherit characteristics such as signature requirements and print characteristics from the higher levels, including Class and Document Class. A Document Definition also lets you create and use boilerplate text, embedded objects, and CPRS templates.

Types of Class Document Definitions:

CL Class – Main class of documents, such as Clinical Procedures.

DC Document Class – Categories of documents with related characteristics, such as CP Cardiology, CP GI.

TL Title – TIU note title, such as CP EKG.

To implement Clinical Procedures, your facility must set up new document definitions for the Clinical Procedures Class within TIU.

The CLINICAL PROCEDURES CLASS is installed with patch TIU\*1.0\*109 and is automatically set to Active.

It is strongly recommended that you create Clinical Procedures Titles and Document Classes with the “CP” prefix. This will avoid confusion with previously created Titles and Document Classes. Only documents under the CP class have the CP functionality.

To construct a new document definition sub-tree for Clinical Procedures, do the following:

1\. Go into the TIU IRM Maintenance menu.

> 2\. Select Document Definitions Manager \> Create Document Definitions.

A screen similar to the following is displayed. (An example of the hierarchy is shown here. On your screen, the levels under Clinical Procedures will not show):

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

Name Type

------------------------------------------------------------------------------

1 CLINICAL DOCUMENTS CL

2 DISCHARGE SUMMARY CL

3 PROGRESS NOTES CL

4 ADDENDUM DC

5 CLINICAL PROCEDURES CL

6 CP CARDIOLOGY DC

7 CP PULMONARY FUNCTION TEST TL

8 CP EKG TL

9 CP GI TESTS DC

10 CP ENDOSCOPY TL

11 CP COLONOSCOPY TL

12 CP HEMATOLOGY DC

13 CP BONE MARROW TL

14 CP RHEUMATOLOGY DC

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Title) Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Level//

The above example suggests a Service oriented set of Document Classes with one or more Titles under each. You need to work with your Clinical Application Coordinator (CAC), IRMS, and the Consulting Services to develop a complete set of Document Definitions for Clinical Procedures.

To view a list of already existing titles, use the Next Level option to expand the class you want to view.

You may have to navigate down the hierarchy to add Document Classes or Titles. The following are examples of going to other levels, creating a document class, and creating a title.

Example of going to the next level:

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

Name Type

------------------------------------------------------------------------------

1 CLINICAL DOCUMENTS CL

2 DISCHARGE SUMMARY CL

3 PROGRESS NOTES CL

4 ADDENDUM DC

5 CLINICAL PROCEDURES CL

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Title) Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Level// \<RET\> Next Level

Select CLINICAL DOCUMENTS Item (Line 2-5): 5........... (Clinical Procedures level)

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

Name Type

------------------------------------------------------------------------------

1 CLINICAL DOCUMENTS CL

2 DISCHARGE SUMMARY CL

3 PROGRESS NOTES CL

4 ADDENDUM DC

5 CLINICAL PROCEDURES CL

6 CP CARDIOLOGY DC

7 CP GI TESTS DC

8 CP HEMATOLOGY DC

9 CP RHEUMATOLOGY DC

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Title) Restart Status...

(Component) Boilerplate Text Delete

Example of creating a Document Class:

Select ACTION: CLASS Class/DocumentClass

Enter the Name of a new CLINICAL PROCEDURES: CP NEUROLOGY

TYPE: (CL/DC): DC DOCUMENT CLASS

CLASS OWNER: CLINICAL COORDINATOR Replace \<RET\>

STATUS: (A/I): INACTIVE// A ACTIVE

SEQUENCE: \<RET\>

MNEMONIC: \<RET\>

MENU TEXT: CP Neurology// \<RET\>

Entry Created

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

Name Type

------------------------------------------------------------------------------

1 CLINICAL DOCUMENTS CL

2 DISCHARGE SUMMARY CL

3 PROGRESS NOTES CL

4 ADDENDUM DC

5 CLINICAL PROCEDURES CL

6 CP CARDIOLOGY DC

7 CP GI TESTS DC

8 CP HEMATOLOGY DC

9 CP RHEUMATOLOGY DC

10 CP NEUROLOGY DC

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Title) Restart Status...

(Component) Boilerplate Text Delete

Example of creating a Title:

You must go to the appropriate level before a Title can be added.

Select Action: Next Level// \<RET\> Next Level

Select CLINICAL DOCUMENTS Item (Line 6-10): 10........... (CP NEUROLOGY level)

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

\+ Name Type

------------------------------------------------------------------------------

2 CLINICAL PROCEDURES CL

3 CP NEUROLOGY DC

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Class/DocumentClass) Next Level Detailed Display/Edit

Title Restart Status...

(Component) Boilerplate Text Delete

At this point a Title may be added.

Select Action: Title// Title

Enter the Name of a new NEUROLOGY: CP PSEUDOFOLLICULAR SCAN

CLASS OWNER: CLINICAL COORDINATOR Replace \<RET\>

[^6]EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

*(See example in the following section: “Example of New TIU Prompts”)*

STATUS: (A/I/T): INACTIVE// A ACTIVE

SEQUENCE: \<RET\>

MENU TEXT: CP Pseudofollicular Scan Replace \<RET\>

Entry Created

If you wish, you may enter another CP NEUROLOGY

Create Document Definitions May 07, 2003@09:03:57 Page: 1 of 1

------------------------------------------------------------------------------

BASICS

\+ Name Type

------------------------------------------------------------------------------

2 CLINICAL PROCEDURES CL

3 CP NEUROLOGY DC

4 CP PSEUDOFOLLICULAR SCAN TL

------------------------------------------------------------------------------

?Help \>Scroll Right PS/PL Print Scrn/List +/- \>\>\>

------------------------------------------------------------------------------

(Title) Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Level//

### [^7]Example of New TIU Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several new TIU prompts display as *each word* of the new TIU note title is run through a series of checks against the national list.

In the following example, the name of the new TIU note title is “CP HEMOTEST.”

EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

Remember, your LOCAL title is: CP HEMOTEST

Attempting to map CP HEMOTEST

to a VHA Enterprise Standard Title...

Is "CP" a Subject Matter Domain? No.

Is "CP" a SYNONYM for a Subject Matter Domain? No.

Is "HEMOTEST" a Subject Matter Domain? No.

Is "HEMOTEST" a SYNONYM for a Subject Matter Domain? No.

Is "CP" a LOINC Role? No.

Is "CP" a SYNONYM for a LOINC Role? No.

Is "HEMOTEST" a LOINC Role? No.

Is "HEMOTEST" a SYNONYM for a LOINC Role? No.

Is "CP" a Setting? No.

Is "CP" a SYNONYM for a Setting? No.

Is "HEMOTEST" a Setting? No.

Is "HEMOTEST" a SYNONYM for a Setting? No.

Remember, your LOCAL title is: CP HEMOTEST

Is "CP" a Service? No.

Is "CP" a SYNONYM for a Service? No.

Is "HEMOTEST" a Service? No.

Is "HEMOTEST" a SYNONYM for a Service? No.

Is "CP" a Document Type? No.

Is "CP" a SYNONYM for a Document Type? No.

Is "HEMOTEST" a Document Type? No.

Is "HEMOTEST" a SYNONYM for a Document Type? No.

AUGH! Let's try a manual look-up...

Again, your LOCAL Title is: CP HEMOTEST

> **NOTE:** Only ACTIVE Titles may be selected...

Select VHA ENTERPRISE STANDARD TITLE: DIALYSIS NOTE

I found a match of: DIALYSIS NOTE

... OK? Yes// YES

Ready to map LOCAL Title: CP HEMOTEST to

VHA Enterprise Standard Title: DIALYSIS NOTE.

... OK? Yes// YES

Done.

In the example above, “DIALYSIS NOTE” was selected as the VHA Enterprise Standard Title. You may use DIALYSIS NOTE as your title, but you are not required to do so. If another title from the VHA Enterprise Standard Title list is more appropriate for your site, you may select it from the list.

[^8]For the high volume procedure(s), there are two steps that you need to do: 1) you must create a title solely for high volume procedure and 2) you must edit the Technical fields of the note. Enter a Q (Quit) for Commit Action and Post-signature Code fields. The MD HIGH VOLUME PROCEDURE SETUP option allows editing of the two technical fields. Note that the title must be in an inactive status before editing these fields either through TIU or the MD options.

The title that you will create for the high volume procedure will be used strictly for the administrative closure purpose. Any subsequent note you need to write, use a separate title for it. The high volume procedure title can be used for one or more procedures. Use the Create CP Class Document Definitions section to assist you in creating a high volume procedure title(s).

The following steps are used to edit the Technical fields of the note:

> **NOTE:** Users must have programmer access to edit the technical fields.

1.  Go into the TIU Maintenance Menu.
2.  Select Document Definitions (Manager).
3.  Select Edit Document Definitions.
4.  Expand/Collapse the CLINICAL PROCEDURES CLASS.
5.  Expand/Collapse a selected DOCUMENT CLASS.
6.  Select Detailed Display/Edit of the title.
7.  Select Entry. (Select the entry of the title.)
8.  Select Basics and change the status field to Inactive.
9.  Select Technical Fields enter Quits for both the Commit Action and Post-Signature Code fields.
10. Select Basics and change the status back to Active.

The following is a screen capture of editing the Technical Fields for the High Volume Title:

> Title HIGH VOLUME TITLE

> Basics Note: Values preceded by \* have been inherited

> Name: HIGH VOLUME TITLE

> VHA Enterprise

> Standard Title:

> Abbreviation:

> Print Name: HIGH VOLUME TITLE

> Type: TITLE

> IFN: 764

> National

> Standard: NO

> Status: INACTIVE

> Owner: CLINICAL COORDINATOR

> In Use: YES

> Suppress Visit

> Selection: \* NO

> \+ ? Help +, - Next, Previous Screen PS/PL

> Basics Technical Fields Find

> Items: Seq Mnem MenuTxt Edit Upload Quit

> Boilerplate Text Try

> Select Action: Next Screen// techn Technical Fields

> COMMIT ACTION: Q//

## ## Step 3 - Define Clinical Procedures Class Document Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to define a set of document parameters for the new CP Class.

1.  Go into the TIU Maintenance Menu.
2.  Select TIU Parameters Menu \> Document Parameter Edit.

> **NOTE:** (Entries in parentheses are recommended values.)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Parameters: Access the following menu:</p>
<p>TIU IRM Maintenance Menu [TIU IRM MAINTENANCE MENU]</p>
<p>TIU Parameters Menu [TIU SET-UP MENU]</p>
<blockquote>
<p>Document Parameter Edit [TIU DOCUMENT PARAMETER EDIT]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Select DOCUMENT DEFINITION: <strong>CLINICAL PROCEDURES CLASS</strong></td>
</tr>
<tr class="odd">
<td>DOCUMENT DEFINITION: CLINICAL PROCEDURES// <strong>&lt;RET&gt;</strong></td>
</tr>
<tr class="even">
<td>REQUIRE RELEASE: <strong>(NO)</strong></td>
</tr>
<tr class="odd">
<td>REQUIRE MAS VERIFICATION: <strong>(NO)</strong></td>
</tr>
<tr class="even">
<td><strong>*REQUIRE AUTHOR TO SIGN:</strong> <strong>(YES)</strong></td>
</tr>
<tr class="odd">
<td>ROUTINE PRINT EVENT(S):</td>
</tr>
<tr class="even">
<td>STAT PRINT EVENT(S):</td>
</tr>
<tr class="odd">
<td>MANUAL PRINT AFTER ENTRY: <strong>(NO)</strong></td>
</tr>
<tr class="even">
<td>ALLOW CHART PRINT OUTSIDE MAS: <strong>(YES)</strong></td>
</tr>
<tr class="odd">
<td>*<strong>ALLOW &gt;1 RECORDS PER VISIT:</strong> <strong>(YES)</strong></td>
</tr>
<tr class="even">
<td>ENABLE IRT INTERFACE:</td>
</tr>
<tr class="odd">
<td><strong>*SUPPRESS DX/CPT ON ENTRY:</strong> <strong>(NO)</strong></td>
</tr>
<tr class="even">
<td>FORCE RESPONSE TO EXPOSURES:</td>
</tr>
<tr class="odd">
<td><strong>*ASK DX/CPT ON ALL OPT VISITS:</strong> <strong>(YES)</strong></td>
</tr>
<tr class="even">
<td>SEND ALERTS ON ADDENDA:</td>
</tr>
<tr class="odd">
<td>ORDER ID ENTRIES BY TITLE:</td>
</tr>
<tr class="even">
<td>SEND ALERTS ON NEW ID ENTRY:</td>
</tr>
<tr class="odd">
<td>SEND COSIGNATURE ALERT:</td>
</tr>
<tr class="even">
<td>EDITOR SET-UP CODE:</td>
</tr>
<tr class="odd">
<td><p>If document is to be uploaded, specify Filing Alert Recipients:</p>
<p>Select FILING ERROR ALERT RECIPIENTS: &lt;identify local recipients as appropriate&gt;</p></td>
</tr>
<tr class="even">
<td><p>Now enter the USER CLASSES for which cosignature will be required:</p>
<p>Select USERS REQUIRING COSIGNATURE: &lt;identify local recipients as appropriate&gt;</p></td>
</tr>
<tr class="odd">
<td><p>Now enter the DIVISIONAL parameters:</p>
<p>Select DIVISION:</p></td>
</tr>
<tr class="even">
<td>CHART COPY PRINTER:</td>
</tr>
<tr class="odd">
<td>STAT CHART COPY PRINTER:</td>
</tr>
</tbody>
</table>

> **NOTE:** You must set parameters marked with an asterisk ‘\*’. If a response is not entered for a particular parameter, the default value is ‘No’.

# About ASU Business Rules and the Role of the Interpreter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the suggested Authorization/Subscription Utility (ASU) business rules that you need to create and it also describes the role of the Interpreter.

Topics discussed in this chapter are:

- [How Business Rules Work](#how-business-rules-work)
- [Role of the Interpreter](#role-of-the-interpreter)

## How Business Rules Work

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Business Rules authorize users or groups of users to perform specified actions on documents in particular statuses. For example, a provider, who is also the Author/Dictator, may view the note.

To add a business rule:

1.  Go into the User Class Management Menu.
2.  Select Manage Business Rules.
3.  Enter specific words at the appropriate prompts (Status, Action, User Class). These words are combined to make a business rule.

Example of adding a business rule:

Select SEARCH CATEGORY: DOCUMENT DEFINITION// \<RET\>

Select DOCUMENT DEFINITION: clinical procedures CLASS

Select Action: Next Screen// a Add Rule

Please Enter a New Business Rule: \<RET\>

Select DOCUMENT DEFINITION: CLINICAL PROCEDURES// \<RET\> CLASS

DOCUMENT DEFINITION: CLINICAL PROCEDURES// \<RET\>

STATUS: unsigned

ACTION: edit

USER CLASS: student

AND FLAG: and

USER ROLE: author/dictator

DESCRIPTION: \<RET\>

No existing text

Edit? NO// \<RET\>

The following rule is constructed:

An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by a STUDENT who is also An AUTHOR/DICTATORSuggested Business Rules for CLINICAL PROCEDURES Class

|     |                                                                                                  |
|-----|--------------------------------------------------------------------------------------------------|
| 1   | A COMPLETED (CLASS) CLINICAL PROCEDURE may BE VIEWED by A USER                                   |
| 2   | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by A STUDENT who is also An AUTHOR/DICTATOR |
| 3   | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE DELETED by An AUTHOR/DICTATOR                      |
| 4   | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by An AUTHOR/DICTATOR                       |
| 5   | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by An AUTHOR/DICTATOR                     |
| 6   | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by An EXPECTED COSIGNER                   |
| 7   | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE PRINTED by An AUTHOR/DICTATOR                      |
| 8   | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE PRINTED by An AUTHOR/DICTATOR                    |
| 9   | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by An EXPECTED COSIGNER                   |
| 10  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by An AUTHOR/DICTATOR                       |
| 11  | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE PRINTED by An EXPECTED COSIGNER                  |
| 12  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE SIGNED by An AUTHOR/DICTATOR                       |
| 13  | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE COSIGNED by An EXPECTED COSIGNER                 |
| 14  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by A CHIEF, MIS                             |
| 15  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE DELETED by A CHIEF, MIS                            |
| 16  | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by A CHIEF, MIS                           |
| 17  | An UNCOSIGNED (CLASS) CLINICAL PROCEDURE may BE DELETED by A CHIEF, MIS                          |
| 18  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by An EXPECTED COSIGNER                     |
| 19  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by An EXPECTED COSIGNER                     |
| 20  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE EDITED by A CLINICAL SERVICE CHIEF                 |
| 21  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE VIEWED by A CLINICAL SERVICE CHIEF                 |
| 22  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE SIGNED by A CLINICAL SERVICE CHIEF                 |
| 23  | An UNSIGNED (CLASS) CLINICAL PROCEDURE may BE SIGNED by An EXPECTED COSIGNER                     |
| 24  | An UNDICTATED (CLASS) CLINICAL PROCEDURE may BE EDITED by An INTERPRETER                         |
| 25  | An UNDICTATED (CLASS) CLINICAL PROCEDURE may BE VIEWED by An INTERPRETER                         |
| 26  | An UNDICTATED (CLASS) CLINICAL PROCEDURE may BE DELETED by A CHIEF, MIS                          |

> Note: Be sure a rule similar to the following exists at the Clinical Documents Class level.

- A COMPLETED (CLASS) CLINICAL DOCUMENT may BE LINKED with a request by A CHIEF, MIS

> This rule is not needed at the Clinical Procedures Class level because of inheritance.

## Role of the Interpreter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INTERPRETER is a user role that is activated with USR\*1\*19 to support the Clinical Procedures Class. Interpreters explain the findings or results of a clinical procedure. In addition, most interpreters can receive alerts on the procedures that are in “Partial Result” status and that are ready for interpretation.

Business rules are used to determine what actions an interpreter can perform on a document of a specified document class, but the interpreters are designated in the Consults application. A business rule must be defined that allows interpreters to view documents.

Using CPRS Consults, the interpreter selects a procedure request, which has a status of Partial Results. Using the Consult option “Complete/Update Results,” the interpreter enters the procedure summary code, the procedure date/time, and the interpretation of the results into the TIU document. (The “Complete/Update Results” option is only available to interpreters.) Any encounter related information can also be entered at this time. When finished, the interpreter electronically signs the note completing the process.

- You can designate a user to be an interpreter by adding the user to any of the following fields on the Consult Management menu (GMRC MGR). See [Step 1 - Setting Up Consult Services](#step-1-setting-up-consult-services), p. [9-1](#step-1-setting-up-consult-services)  
  - INDIVIDUAL TO NOTIFY  
  - SERVICE TEAM TO NOTIFY  
  - NOTIFICATION BY PT LOCATION  
  - UPDATE USERS W/O NOTIFICATIONS  
  - UPDATE TEAMS W/O NOTIFICATIONS

# # Setting Up Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes how to set up CP procedures, instruments, and system parameters. It is recommended that you follow these steps in sequential order. Topics discussed in this chapter include:

- [Step 1 – Populate the CP Definition file](#step-1---populate-the-cp-definition-702.01-file)
- [Step 2 – Setting Up Instruments](#step-2-setting-up-instruments)
- [Step 3 – Setting Up Procedures](#step-3-setting-up-procedures)
- [Step 4 – Setting Up System Parameters](#_Step_4_-)

## Step 1 - Populate the CP Definition (#702.01) file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can populate the CP Definition (#702.01) file with names of clinical procedures automatically by running the INIT^MDPOST routine, and manually by using the procedure edit screen. Editing the procedures is described in detail later in this chapter.

Before you decide which method to use, review [Appendix B – Exported Procedures List](#appendix-b-exported-procedures-list), p. [17-1](#appendix-b-exported-procedures-list), for the list of procedures. If the Clinical Application Coordinator (CAC) and the CP package coordinator decide to use these procedures for the medical center, IRM can run INIT^MDPOST to automatically populate the CP Definition file with a list of known procedures. These procedure definitions are not complete and must be edited using CP Manager to make them work properly. Additional procedures can also be added using CP Manager.

The application coordinators may initially populate the file manually and then run the INIT^MDPOST routine at a later time. This routine does not overwrite the existing data in the CP Definition file; it adds procedures that are not in the current CP Definition file.

All procedures are stored in a subfolder called Unassigned within the Procedures folder. All procedures are initially tagged inactive. Use CP Manager to activate specific procedures and associate the procedures with treating specialties.

## Step 2 – Setting Up Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information on instruments is not complete after instrument information is added during installation. You must go into CP Manager and enter the necessary fields before the package will work successfully.

To access CP Manager:

1\. Double-click CP Manager on the desktop.

> 2\. Enter your access and verify codes.

> 3\. Click OK. The following main screen is displayed:

![](clinical-procedures-version-1-implementation-guide/019.png)

Figure 6‑1

In most cases, you edit an existing automated instrument. The Mallinckrodt Clinivision, Olympus Endoworks, GE Medical Systems Muse and Viasys/Sensormedics Vmax automated device interfaces are exported with Clinical Procedures. You must edit all the automated instruments that you want to implement with necessary information.

### Editing an Automated Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of fields applies to automated instruments:

\* indicates fields that must be filled in for an active instrument to work properly.

BOLD indicates fields that are already populated when an automated instrument is exported.

∗ Instrument Name

∗ Printable NameDescription

∗ M Routine

∗ Pkg. Code

∗ Valid Attachment TypesIf Bi-Directional Instrument is checked:

∗HL7 Inst ID

∗HL7 Link

∗ Notification Mailgroup

∗ Active

Serial Number (Optional)

Delete When Submitted (Optional)

Default Extension (Optional)

IP Address (Optional)

Port (Optional)

HL7 Unv Svc ID (Optional)

Server Name (Optional)

Share Name (Optional)

Path Name (Optional)

Executable Name (Optional)

To edit an automated instrument:

1.  View the list of automated instruments. See Figure 6‑2.
2.  Click on an automated instrument. The edit screen is displayed on the right side of the Clinical Procedures Manager window.
3.  Enter the fields that apply to the instrument you selected.
4.  Click Save when you are done.
5.  Click Print if you want to print an Automated Instrument report. See [Printing Reports](#printing-reports), p. [2-4](#printing-reports).

![](clinical-procedures-version-1-implementation-guide/020.png)

Figure 6‑2

Here is a list of fields for automated instruments.

General: This section contains general information about the instrument.

> Instrument Name: If you are editing an instrument, the name is filled in.

> Note: This field must be filled in for an active instrument to work properly. If you are adding a new instrument that is already supported by CP, do one of the following:

- If the device is bi-directional, you can enter a name of your own choice (3-30 characters), such as Muse EKG (Tampa). The name does not have to be the vendor’s name.
- If the device is uni-directional, you need to enter a CP defined name. In this case, you can contact TSO or NVS for the correct instrument name.

> If you are adding a new instrument (bi-directional or uni-directional) that is not supported by CP, then you must enter a NOIS/Remedy help ticket. Keep in mind that adding unsupported instruments is a complex task and may cause some image quality problems.  

> Printable Name: Enter a name for the instrument report (3 to 30 characters). You can use the same name as the instrument name. This name is used as the printable name on reports. Must be filled in for an active instrument to work properly.

> Notification Mailgroup: Enter the name of a local VistA mailgroup that contains a list of people, who will be notified if a problem arises with this automated instrument.  

> CP also exports a mailgroup called “MD DEVICE ERRORS” that can be used to populate this field. Enter MD and the field fills in with “MD DEVICE ERRORS’. The coordinator of this group is assigned during package installation. Must be filled in for an active instrument to work properly.

> Description: Enter a description of the automated instrument (1-50 characters). Optional.

> Serial Number: Enter the serial number of the automated instrument (1-50 characters). The serial number is used for documentation purposes. Optional.

> Active: Select this option if you want to make the instrument active and able to transmit results. Do not select if the package coordinator wants to prevent data from a specific automated instrument from being processed. A package coordinator may want to enter the basic information for an automated instrument and not make it active. Must be selected to make this instrument active.

Attachment Processing: This section contains information about attachments.

> Delete when Submitted: Select this option if the medical center does not want to store a duplicate report outside of Imaging, or if the vendor wants to delete files because of storage issues. The vendor determines whether or not the report files can be deleted. This information is found in the vendor’s setup instructions. Optional.

> Default Ext.: Enter a default file extension that is exported by the vendor, such as .html, .jpg, and .pdf. This information should be obtained from the vendor or will be exported with future patches. Optional.

> M Routine: Indicates the M routine used to process the HL7 message from the automated instrument (1-8 characters). Enter an M routine if the site is entering a new device. The routine must have a namespace of MDHL7\* for any nationally released interfaces. This field also is automatically populated when an instrument interface patch is installed. If a local M routine is developed, use the local namespace. Refer to [Appendix C – Instrument Processing Routines](#appendix-c---instrument-processing-routines), p. [18-1](#appendix-c---instrument-processing-routines), for a list of appropriate M routines for each instrument. Must be filled in for an active instrument to work properly.

> Pkg. Code: Indicates which package is to process the instrument results. Must be filled in for an active instrument to work properly.

> Medicine: Select if your study data is stored in the Medicine package. If a site is currently running Medicine and has an instrument used for Medicine, you can send the result to Medicine by selecting this field.

> CP V1.0 Select if your study data is stored as a final report (in the format of an Imaging document) in Clinical Procedures.

> Valid Attachment Types: Data types let CP know what kind of data output to expect from the automated instrument so that the data can be processed by the interface routines. The vendor setup instructions provide this information, or Clinical Procedures automatically exports this information. Must be filled in for an active instrument to work properly.

> Here is a list of valid attachment types:

> UNC (Universal Naming Convention or Uniform Naming Convention) - A PC format for specifying the location of resources on a local-area network (LAN).

> UUENCODE (Unix-to-Unix ENCODE) - A set of algorithms for converting files into a set of ASCII characters that can be transmitted over a network.

> Text - Text stored as ASCII codes.

> XML (eXtensible Markup Language) - A specification developed by the World Wide Web Consortium (W3C), the organization that sets standards for the web. XML is a pared-down version of SGML. Designed especially for Web documents.

> URL (Uniform Resource Locator) - The global address of documents and other resources on the World Wide Web.

> XMS - An XML Style Sheet.

> DLL (Dynamic Link Library) - A library of executable functions or data that can be used by a Windows application.

Bi-Directional Capabilities: This section contains specifics on the bi-directional capabilities of the instrument.

> Bi-Directional Instrument: Select this option if this instrument supports a bi-directional interface.

> IP Address: Enter the IP address for the instrument (7-15 characters). This field is for documentation purposes only. Refer to [Chapter 10 – Setting Up HL7 Parameters](#setting-up-hl7-parameters), p. [12-1](#setting-up-hl7-parameters), for more information. Optional.

> Port: Enter the port number for the instrument (a number between 1000 and 99999). This field is for documentation purposes only. Refer to [[Chapter 10 – Setting Up HL7 Parameters](#setting-up-hl7-parameters)](#setting-up-hl7-parameters), p. [12-1](#setting-up-hl7-parameters), for more information. Optional.

> HL7 Inst ID: Enter the name of the actual device as provided by the vendor. This field is used to ID the device (3-30 characters). You can contact TSO or NVS for the correct ID. Must be filled in for an active instrument to work properly.

> HL7 Unv Svc ID: This field defines what type of procedure the device can perform if the device can perform more than one procedure (1-48 characters). Optional.

> HL7 Link: There is one unique link for each instrument. Select the appropriate link to the instrument from the dropdown list. Must be filled in for an active instrument to work properly. (This must be filled in with the outbound link that you have created for the device. For example, MCAR OLY could be entered for an Olympus device.)

Server Executable: The following fields make up the path for the automated instrument server (http://servername/servershare/serverpath/server.exe). Some devices do not produce reports that can be saved. Enter these fields if you want to capture a report from that type of device.

> Server Name: The network name of the automated instrument (1-30 characters).

> Server Share: The name of the share drive on the automated instrument server (1-30 characters).

> Server Path: The full directory path on the automated instrument share (1-150 characters).

> Server Executable: The name of the executable that produces the report on the automated instrument (1-30 characters). Browse to find the path where the server.exe program resides.

### Adding an Automated Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site has an instrument that needs to interface with CP, and that instrument is not exported with the Clinical Procedures package, you need to add the instrument. Make sure that CP supports the instrument interface. (The Mallinckrodt Clinivision, Olympus Endoworks, GE Medical Systems Muse and Viasys/Sensormedics Vmax automated device interfaces are exported with Clinical Procedures.) You can also find an updated list of supported devices on the CP SharePoint at <https://vaww.oed.portal.va.gov/projects/Clinical_Procedures/Device%20Settings/Forms/AllItems.aspx>

Click Medical Device Interfaces on the left navigation bar, then click About Medical Interfaces.

[^9]A warning screen displays when you attempt to add a new instrument (Figure 6‑3). This warning screen informs you that you should make sure CP supports the instrument interface you are attempting to add.

![](clinical-procedures-version-1-implementation-guide/021.png)

Figure 6‑3

If you are adding a new instrument (bi-directional or uni-directional) that is not supported by CP, then you can use the New Instrument Request form, which is also located on the CP website at <http://vista.med.va.gov/ClinicalSpecialties/clinproc/>. You can also check p. [18-1](#appendix-c---instrument-processing-routines) for a list of instruments. Keep in mind that adding unsupported instruments is a complex task and may cause some image quality problems.

In most cases, you can edit an existing automated instrument instead of adding a new one because several automated instruments are installed with Clinical Procedures. To view the names of devices, click the Instruments folder. A list of automated instruments is displayed on the left side of the Clinical Procedures Manager window (Figure 6‑4).

![](clinical-procedures-version-1-implementation-guide/022.png)

Figure 6‑4

Indicates active instruments: ![](clinical-procedures-version-1-implementation-guide/023.png)

Indicates non-active instruments: ![](clinical-procedures-version-1-implementation-guide/024.png)

1.  Select File \> New \> Instrument. The New Instrument screen is displayed.
2.  Enter a name that can be used to identify the automated instrument. If you are adding a new instrument that is already supported by CP, do one of the following:
    - If the device is bi-directional, you can enter a name of your own choice (3-30 characters), such as Muse EKG (Tampa). The name does not have to be the vendor’s name.
    - If the device is uni-directional, enter a CP defined name. In this case, you can contact TSO or NVS for the correct instrument name.

If you are adding a new instrument (bi-directional or uni-directional) that is not supported by CP, then you must you must enter a NOIS/Remedy help ticket. Keep in mind that adding unsupported instruments is a complex task and may cause some image quality problems.

This field must be filled in for an active instrument to work properly.

3.  Click OK. The Edit screen is displayed. Figure 6‑5 is the edit screen for automated instruments. The Automated Instrument Name that you just entered is displayed.
4.  Enter data for each field as applicable. Refer to [Editing an Automated Instrument](#editing-an-automated-instrument), p. [6-3](#editing-an-automated-instrument), for detailed field descriptions.
5.  Click Save when you are done.
6.  Click Print if you want to print an Automated Instrument report. See [Printing Reports](#printing-reports), p. [2-4](#printing-reports).

![](clinical-procedures-version-1-implementation-guide/025.png)

Figure 6‑5

### Additional Instrument Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two additional instrument parameters are now available in CP which can be set using their respective VistA menu options.

The CP – DICOM Interoperability parameter will improves interoperability between Clinical

Procedures and VistA Imaging CPRS Consult Request Tracking DICOM. There are three capabilities:

First, the VistA Imaging consult accession number sss-GMR-nnnnnnnn can be used for the Clinical Procedures Instrument Order Number.

Second, the timing of the DICOM Modality Worklist creation is changed from order release to check-in, making it much more useful.

Third, the VistA Imaging HL7 message body can be used instead of the CP HL7 message body. (The VistA Imaging HL7 has much more information than the CP HL7.)

> **NOTE:** This is for bidirectional CP instruments only. Also, the CP must have an entry in the CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) to have DICOM Modality Worklist and HL7.

The option CP - DICOM Interoperability \[MD DICOM\] resides on the CP Coordinator \[MD COORDINATOR\] menu:

MD COORDINATOR CP Coordinator Menu

Auto Study Check-In Setup

CP - DICOM Interoperability

High Volume Procedure Setup

Keep Consult Open for CART-CL

Select CP Coordinator Menu Option: CP - DICOM Interoperability

Select CP INSTRUMENT NAME: OLYMPUS EGD {554EC814-50A9-8389-1331-CE60DB3CD2FF}

CP - DICOM INTEROPERABILITY: ?

Select special VistA Imaging processing

Choose from:

0 No special action

1 Use VistA Imaging accession number sss-GMR-nnnnnnnn

2 Use VistA Imaging HL7 instead of CP's HL7

The ‘CONSULT KEEP OPEN’ parameter is intended for CART-CL interoperability:

This Clinical Procedures Uni-directional Configuration flag 'CONSULT KEEP OPEN' provides the following functionality:

The CP procedure is automatically placed in Completed status after the HL7 message is sent, thus preventing an "inbound" HL7 message containing the test results from being sent back to the CPRS Consult Note.

The physician can then edit the Consult Note by manually pasting in data from a test result reporting system to complete the Consult.

This modification is beneficial for users of reporting systems-such as the Clinical Assessment, Reporting, and Tracking System for Cardiac Catheterization Laboratories (CART-CL) application-who do not want the test results from the medical instrument to populate the CPRS Consult Note, but prefer to manually paste the test results from the reporting system into the Consult Note.

The option ‘Keep Consult Open for CART-CL’ \[MD CARTCL\] resides on the CP Coordinator \[MD COORDINATOR\] menu:

MD COORDINATOR CP Coordinator Menu

Auto Study Check-In Setup

CP - DICOM Interoperability

High Volume Procedure Setup

Keep Consult Open for CART-CL

Select CP Coordinator Menu Option: keep Consult Open for CART-CL

Select CP INSTRUMENT NAME: IVAULT ECHO {48E0112B-335C-4C78-9EBA-D4362EEE38D1}

CONSULT KEEP OPEN: ?

Enter Yes to keep consult note open or No to close consult note.

Choose from:

0 No

1.  Yes

### ### Using the Instrument Analyzer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Instrument Analyzer to see if an automated instrument is ready to use with CP.

1.  Select Tools \> Instrument Analyzer.
2.  Select the instrument that you want to analyze. Click Analyze. A window similar to Figure 6‑6 is displayed. This window indicates the ready status of the instrument and lists other information as well.

![](clinical-procedures-version-1-implementation-guide/026.png)

Figure 6‑6

- Ready Status - Pass or Fail. If the Ready Status is Fail, a list of missing fields for that automated instrument is displayed.
- If an Imaging share directory has not been configured, the following message is displayed “No Imaging Share indicated in the System Parameters.”
- If the M Routine (processing routine) is not in the MD or MC namespace, a warning is displayed indicating that the M Routine is not in the package namespace.
3.  Click Print or Close.

## Step 3 – Setting Up Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information on procedures is not complete after populating the CP Definition file. You must go into CP Manager and enter the necessary fields before the package will work successfully.

If the INIT^MDPOST routine was run, a limited number of exported procedures are stored in a subfolder called Unassigned within the Procedures folder. If the INIT^MDPOST routine was not run, then you need to add new procedures. Since all procedures are initially inactive, you need to activate existing procedures and associate them with treating specialties.

### Editing a Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the procedures have been exported, then you can edit them as needed. Using CP Manager, you must move each procedure that you want to activate from the Unassigned folder to a treating specialty folder.

- Double-click the procedure. Now you can edit the procedure, complete the necessary fields, and make the procedure active.
- To activate the procedure, be sure to select the Active field, and then fill in the following fields to ensure that the procedure works properly

> Treating Specialty

> TIU Note Title

> Hospital Location

To edit a procedure:

1.  View the list of procedures. See Figure 6‑7.
2.  Click a procedure name. The edit screen is displayed on the right side of the Clinical Procedures Manager window.
3.  Enter the fields as applicable.

> [^10]Note: Make sure to set the Processing Application field to HEMODIALYSIS for Hemodialysis procedures.

4.  Click Save when you are done.
5.  If you selected a different treating specialty folder, a confirmation message is displayed. Click OK to confirm that the procedure is in the correct treating specialty folder.
6.  Click Print if you want to print a Procedure report. See [Printing Reports](#printing-reports), p. [2-4](#printing-reports).

> **NOTE:** A procedure can only be deleted through the main menu bar. Refer to the section [Deleting an Automated Instrument or Procedure](#deleting-an-automated-instrument-or-procedure), p. [2-3](#deleting-an-automated-instrument-or-procedure), for more information. If a procedure has been assigned through Consults, it cannot be deleted.

![](clinical-procedures-version-1-implementation-guide/027.png)

[^11]Figure 6‑7

Here is a list of fields for Procedures.

General: This section contains general information about the procedure.

> Procedure Name: Enter a name used to uniquely identify the procedure (3-30 characters). It is recommended that you enter the name in uppercase, such as PACEMAKER FOLLOWUP.

> After you complete the edits, if you entered the name in upper case, the procedure name that you just entered is displayed in title case, Pacemaker Follow-up, (the first letter of every word is capitalized), in the left side of the CP Manager window. See Figure 6‑6.

> Active: Select if you want the procedure to be mapped to Consults. Only active procedures can be selected and linked to the Consults package. Be sure to fill in the Treating Specialty, TIU Note Title, and Hospital Locations fields. Do not select if you do not want procedures to display. Must be selected to make this procedure active.

> Treating Specialty: Enter at least two letters of a treating specialty, such as CA for CARDIOLOGY, and then click the down arrow to select an appropriate match from the list. This list comes from the Treating Specialty (#45.7) file. Must be filled in for an active procedure to work properly.

> TIU Note Title: Enter at least two letters of a TIU Note Title, such as CP CARD for CP CARDIOLOGY NOTE or CARD for CARDIOLOGY, and then click the down arrow to select an appropriate match from the list, which comes from the 8925.1 file. This title must be in the CLINICAL PROCEDURES CLASS. Must be filled in for an active procedure to work properly.

> [^12]Hospital Location: Enter at least two letters of a hospital location, such as CA for Cardiac Clinic, and then click the down arrow to select an appropriate match from the list, which comes from the \#44 file. The Hospital Location file is the location where the workload credit for the procedure is tracked and is needed so CPRS can display the appropriate encounter form when prompted. Must be filled in for an active procedure to work properly.  

> You can enter a COUNT or NON-COUNT clinic for the hospital location.

- A COUNT clinic captures workload. Patients must be checked in and checked out and an encounter form must be completed in order to collect workload.
- A NON-COUNT clinic is used only for scheduling purposes and not for workload reporting.

> There are three options available for setting up your clinics. The appropriate option for your site depends on how you currently do business and should be discussed with your project implementation manager.

- COUNT clinic for scheduling purposes / NON-COUNT clinic for CP User. Patient must be checked in/out and encounter form completed on the scheduled appointment. CP User appointment will not collect workload.
- NON-COUNT clinic for scheduling purposes / COUNT clinic for CP User. Appointment in scheduling package does not need to be checked in/out, nor does an encounter form need to be completed for the appointment. The check in/out and encounter form must be completed for the appointment created through CP User.
- COUNT clinic for scheduling purposes that passes over to CP User. Patient must be checked in/out and encounter form must be completed. Note, however, that if you use Appointment Manager to check in the patient, you may have to wait up to thirty minutes before you can check-in the patient to CP. During the thirty-minute timeframe, the Patient Care Encounter (PCE) application establishes the visit date. (If you use the Scheduling application to capture workload, make sure that the clinic location is the same as the default location in the Hospital Location field.)

> Auto Submit to VistA Imaging: Select if a procedure is processed by a bi-directional instrument and additional data does not need to be matched. The study is automatically submitted to V*IST*A Imaging. If this field is not selected, the study will be in the Ready to Complete status. Optional.

> Require External Data: Select if you want this procedure to allow external attachments. For example, you might want to attach an independent report from a VA or non-VA health care facility. If you want to manually select external attachments, you must select this field.  

> Be sure the Allow Non-Instrument Attachments checkbox is selected in CP Manager \> System Parameters. There is no default for this field.

> External Attachment Directory: If you select Require External Data, enter the path where the data is located, or browse to locate a directory (3-150 characters). There is no default on this field. You can locate any directory on the LAN. This is the directory that CP User accesses to find attachments. This directory must be a network share directory that the VistA Imaging Background Processor can access.

> [^13]Processing Application: Set the Processing Application field to HEMODIALYSIS for Hemodialysis procedures. Any other CP procedures will default to the Default setting, so you do NOT need to set the field.

> Allowable Instruments: Select each automated instrument that provides results for this procedure. You can select more than one instrument for a procedure. If you only want to use external attachments, do not select any instruments.  

> You can select both Allowable Instruments and Require External Data. For example, you can have a pathology report from an endoscopy and you can attach the report to the procedure.

> [^14]Processed Results: This field is a flag which indicates whether a final result, multiple results, or cumulative result is associated with this procedure. This field is not accessible using the CP Manager application. It must be edited using File Manager.

> [^15]Note: If the site does not have a multiple result instrument, NO setup needs

to be made. CP automatically defaults to using '0' for Final Result. If

> the site has a multiple result instrument, the site can select either '1'

> for Multiple Results which allows creation of a new TIU note for each result

> sent back or a '2' for Cumulative Result which allows the multiple result

> device to continuously send results back to the same TIU note. If the site

> needs to enter the PROCESSED RESULT field, the user will have to use File

> Manager to edit the field in the CP DEFINITION File (#702.01).

### Adding a Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you add a procedure, you can check to see if an appropriated titled procedure already exists that meets your needs. To view the names of procedures, select Procedures and then the appropriate treating specialty folder. A list of procedures is displayed. See Figure 6‑8.

![](clinical-procedures-version-1-implementation-guide/028.png)

Figure 6‑8

![](clinical-procedures-version-1-implementation-guide/029.png) - Identifies an active procedure

![](clinical-procedures-version-1-implementation-guide/030.png) - Identifies an inactive procedure

If you decide that you do need to add a procedure, follow these instructions:

1.  Select File \> New \> Procedure.
2.  Enter the name of the procedure that you want to add. It is recommended that you enter the name in uppercase with a minimum of 3 characters and a maximum of 30 characters.
3.  Click OK. The Edit screen is displayed. Figure 6‑9 is the edit screen for procedures. The Procedure Name that you just entered is displayed in the left side of the CP Manager window in the Unassigned folder.
4.  Enter data for each field as applicable. Refer to [Editing a Procedure](#editing-a-procedure), p. [6-12](#editing-a-procedure), for detailed field descriptions.
5.  Click Save when you are done. After you complete the edits, if you entered the name in upper case, the procedure name that you just entered is displayed in title case.
6.  Click OK. The new procedure appears in the list on the left side of the CP Manager window. Check that the procedure is placed in the correct treating specialty folder.
7.  Click Print if you want to print a Procedure report. See [Printing Reports](#printing-reports), p. [2-4](#printing-reports).

![](clinical-procedures-version-1-implementation-guide/031.png)

[^16]Figure 6‑9

[^17]The following is a screen capture of using File Manager to edit the PROCESSED RESULT field in the CP Definition file (#702.01).

\>D P^DI

VA FileMan 22.0

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: CP TRANSACTION// 702.01 CP DEFINITION

(310 entries)

EDIT WHICH FIELD: ALL// PROCESS

1 PROCESSED RESULT

2 PROCESSING APPLICATION

CHOOSE 1-2: 1 PROCESSED RESULT

THEN EDIT FIELD:

Select CP DEFINITION NAME: PUL

1 PULMONARY ARTERY CATHETER

2 PULMONARY ENDOSCOPY

3 PULMONARY FUNCTION INTERPRET

4 PULMONARY FUNCTION TEST

5 PULMONARY PROCEDURES

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 5 PULMONARY PROCEDURES

PROCESSED RESULT: ?

Enter the processed result.

Choose from:

0 Final Result

1 Multiple Results

2 Cumulative Result

PROCESSED RESULT: 1 Multiple Results

Select CP DEFINITION NAME:

<span id="_Step_4_-" class="anchor"></span>

## Step 4 – Setting Up System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System parameters are system-wide and affect all procedures and instruments. You must select Clinical Procedure On-Line, and fill in the Imaging Network Share and the VistA Scratch HFS Directory fields for CP to work properly. You can edit the other parameters as required for your site.

Here is a list of the system parameters:

\* Indicates fields that must be filled in for CP to work properly.

\*[Clinical Procedures On-Line](#clinical-procedures-on-line)

\* [VistA Scratch HFS Directory](#vista-scratch-hfs-directory)

1.  Click System Parameters, which is displayed under the Clinical Procedures folder. The System Parameters Edit window is displayed. See Figure 6‑10.
2.  Enter information in the necessary fields and in the optional fields as needed by your site.

![](clinical-procedures-version-1-implementation-guide/032.png)

[^19]Figure 6‑10

### Allow non-instrument attachments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select if you want to let users attach files from the network to studies. If selected, the +Files icon displays in the Study window in CP User and lets the user select attachments. Indicates if external attachments (documents) are allowed including when an instrument has not created data.

Be sure to select Allow non-instrument attachments if you selected the Require External Data field in CP Manager for a specific procedure. If you do not select Allow non-instrument attachments, you will not be able to attach files to a procedure.

### Bypass CRC Checking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select if you want to bypass CRC (Cyclical Redundancy Check) during startup. When a CP application starts up, it can check with the server to be sure that the checksum of the application that is running is the same as the checksum of the application that was distributed. If the checksum values do not match, a message displays stating that the values do not match. Even if values don’t match, you can continue using CP.

The checksum value is associated with the version number of the software. You might want to bypass this check when your site is running CP in test mode. If you are running different versions of the application, then the checksum values will not match.

### Clinical Procedures Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the Clinical Procedures home page and directs the browser to this page when accessed.

This parameter is used by the client application in the Help menu when the user selects the option Clinical Procedures on the Web.

> **NOTE:** The MDPOST routine in the KIDS build sets this field during installation. The data in the parameter is predefined. Do not modify this parameter unless the site is performing local modifications to the client software.

### Clinical Procedures On-Line

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Must select if you want to use CP User and CP Gateway. If this parameter is not selected, a warning message is displayed. (If a message has been entered into the Offline Message parameter, that message is displayed when the user tries to access CP User.)

This parameter is only effective when the VistA system is functioning and it is useful if you want to restrict access to Clinical Procedures. For example, you can set this field to offline if you are loading a newer version of CP.

### CP/BGP Transfer Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the shared directory that is accessed by the Imaging Background Processor (BGP) and CP Gateway. Reports generated from text need to be placed in a location that can be accessed by the BGP. The Network share must not reside physically on the Imaging RAID. You can also use Browse to select the directory. Must be filled in for CP to work properly.

### CRC Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A site can check that a specific build of the application is running on the client. This level of checking is not mandatory and you can use the Bypass CRC Checking parameter if the site does not want this level of security.

If a site is running more than one version of the application or is testing a new patch, this field can contain multiple entries, (Figure 6‑11). Each entry contains the name of the application with extension (no directory path) followed by a colon ‘:’ and the executable version number ‘#.#.#.#’. Each of these entries contains the CRC value for that particular version of the executable. You can also obtain CRC values for a version of an executable from the About menu or by selecting CP Manager \>Tools \> Calculate a File’s CRC Value.

> **NOTE:** The MDPOST routine in the KIDS build sets this field during installation. The data in the parameter is predefined. Do not modify this parameter unless the site is performing local modifications to the client software

![](clinical-procedures-version-1-implementation-guide/033.png)

[^20]Figure 6‑11

### Calculating a File’s CRC Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can calculate a file’s CRC (Cyclical Redundancy Check) value to determine if the file is the exact same file as the one that was distributed. CRC values are recalculated every time an application is compiled.

1.  Select Tools \> Calculate a file’s CRC Value.
2.  Select the file.
3.  You can copy the CRC value and paste it into a text file for reference purposes.

### Days to keep instrument data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the number of days (0-365) to save data from auto-instruments, after the data has been associated with a Clinical Procedures study. If the data has not been associated with a study, the data is not purged from the temporary storage area. Enter 0 or leave the field empty if you want the data to be retained forever.

> **NOTE:** CP Gateway purges data daily. This purge only deletes the raw data that comes from the instrument. CP Gateway keeps data for a specified number of days based on the entry in “Days to keep Instrument Data”. Data older than this is purged. The data in Item Value field (#.1) and Item Text field (#.2) of the Upload Item multiple in the CP Results file (#703.1) are purged.

### Imaging File Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verifies that a file type submitted by an instrument or user is acceptable and can be sent to the VistA Imaging RAID. The Open a Study option in CP User uses this system parameter to determine if a file is an acceptable file type, (Figure 6‑12).

> **NOTE:** The MDPOST routine in the KIDS build sets this field during installation. The data in the parameter is predefined. Do not modify this parameter unless the site is performing local modifications to the client software

![](clinical-procedures-version-1-implementation-guide/034.png)

[^21]Figure 6‑12

### Offline Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a message that users see when they try to activate CP User and Clinical Procedures is offline. This message only displays when the Clinical Procedures On-line parameter is not checked. See Figure 6‑13.

![](clinical-procedures-version-1-implementation-guide/035.png)

[^22]Figure 6‑13

### Version Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays a list of client versions, identified by their executable name and windows file version, which are compatible with the currently running server version. More than one version of the software may be flagged as compatible for backward compatibility. See Figure 6‑14.

To check the client version number:

1.  Open Windows Explorer and locate the Clinical Procedures folder.
2.  Right-click CPGateway.exe, or CPUser.exe., or CPManager.exe.
3.  Select Properties, and then click the Version tab. The version number, such as 1.0.0.17, is displayed.
4.  Go back to CP Manager. Double-click Clinical Procedures, and then click System Parameters.
5.  In the Version Compatibility tab, select each version that is compatible with the current server version, (Figure 6‑14).

> **NOTE:** The MDPOST routine in the KIDS build sets this field during installation. The data in the parameter is predefined. Do not modify this parameter unless the site is performing local modifications to the client software

![](clinical-procedures-version-1-implementation-guide/036.png)

[^23]Figure 6‑14

If an executable version is not compatible, the following message is displayed when you try to use a Clinical Procedures application:

![](clinical-procedures-version-1-implementation-guide/037.png)

Figure 6‑15

If the application is CP Manager, the user is allowed to continue. If the application is CP User, the user needs to contact IRM because the client needs to be upgraded to the current version.

### VistA Scratch HFS Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Procedures uses the Host File Server (HFS) functionality in the VA Kernel to create reports. VistA broker processes require full read, write, and delete access to this directory. (Check with IRM about this directory.) If this directory is not filled in, CP tries to use the broker environment directory. Must be filled in for CP to work properly.

## [^24]Step 5 – Exported Kernel XPAR Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Exported Kernel XPAR Parameters for Patch MD\*1.0\*14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four Kernel XPAR Parameters exported with patch MD\*1\*14.

- MD CHECK-IN PROCEDURE LIST
- MD CLINIC QUICK LIST
- MD CLINICS WITH MULT PROC
- MD USE APPT WITH PROCEDURE

A new option called MD AUTO CHECK-IN SETUP was added to setup and implement procedures that will use auto study check-in. Once a procedure is set up to use the auto study check-in functionality in the MD CHECK-IN SETUP option, the software will check-in any existing order requests with the status of “PENDING”, “ACTIVE”, and “SCHEDULED” in the Consult Request Tracking package.

> **NOTE:** If your site uses appointments, schedule them before you enter the procedures for auto check-in. If you do not, the patients associated with those appointments will need to be manually checked in.

This option collects the following information:

- Use Appointment with procedure? (Yes/No) (Required) – The default is “NO”, if the site does not schedule procedures before the order is entered. Enter “YES” if the procedure appointment is scheduled before the order is entered and the ordering provider selects the appointment for the procedure during ordering in CPRS.
- Procedure (Required)– Enter the CP Definition that will be using the auto study check-in functionality.
- Schedule Appointment? (Required) - Enter 0 for None, 1 for Outpatient, 2 for Inpatient, or 3 for Both. This indicates that the site schedules appointments for inpatient, outpatients, both, or none.
- Clinic (Optional) – Enter the hospital location(s) that will be used for scheduling the procedure.

> **NOTE:** If no clinic is entered in the setup, CP will use the hospital location defined in the HOSPITAL LOCATION field of the CP Definition file (#702.01) as the location of the visit for the CP study check-in.

The following two pages contain a screen capture of the MD AUTO CHECK-IN SETUP option:

Select OPTION NAME: MD AUTO CHECK-IN SETUP Auto Study Check-In Setup

Auto Study Check-In Setup

Use Appointment with procedure? NO// ?

Default should be 'N' as most sites do not schedule procedures

before the order is entered. Select 'Y' if the procedure appointment

is scheduled before the order is entered and the ordering provider

selects the appointment for the procedure.

Enter either 'Y' or 'N'.

Use Appointment with procedure? NO//

Procedure: ?

Enter a CP Definition for the procedure to

have auto CP study check-in.

Answer with CP DEFINITION NAME

Do you want the entire CP DEFINITION List? N (No)

Procedure: COLONOSCOPY

Schedule Appointment?: ?

REQUIRED field for the procedure to have auto CP study check-in.

Enter a "^" will exit completely.

Enter 0 if you do not schedule appointments.

1 if you only schedule appointments for outpatients.

2 if you only schedule appointments for inpatients.

3 if you schedule appointments for both 1 and 2.

Select one of the following:

0 None

1 Outpatient

2 Inpatient

3 Both

Schedule Appointment?: Both

Clinic: ?

Only required, if appointments are scheduled for the procedure.

Enter the clinic used for scheduling the procedure.

Answer with HOSPITAL LOCATION NAME, or ABBREVIATION, or TEAM

Do you want the entire 112-Entry HOSPITAL LOCATION List? N (No)

Clinic: GI LAB PIPER,ALPHA

Enter another clinic for the same procedure? NO// ?

Enter either 'Y' or 'N', if you want to assign more than one clinic.

Enter another clinic for the same procedure? NO//YES

Clinic: TEST

1 TEST/PROSTHETICS OBRIEN,FRANCES U

2 TEST1

3 TEST1234

4 TEST3232

CHOOSE 1-4: 2 TEST1

Enter another clinic for the same procedure? NO//

Procedure: ?

Enter a CP Definition for the procedure to

have auto CP study check-in.

COLONOSCOPY

Answer with CP DEFINITION NAME

Do you want the entire CP DEFINITION List? N (No)

Procedure: EKG, ROUTINE (12 LEADS)

Schedule Appointment?: 0 None

Procedure:

\>

### [^25]Exported Kernel XPAR Parameters for Patch MD\*1.0\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four Kernel XPAR Parameters exported with Patch MD\*1.0\*6.

PARAMETER DEFINITION:

- MD APPOINT END DATE
- MD APPOINT START DATE
- MD COMPL PROC DISPLAY DAYS
- MD DAYS TO RETAIN COM STUDY

The users can edit the parameters using the Edit Parameter Values option, \[XPAR EDIT PARAMETER\].

The following is a screen capture of the parameter usage:

> D ^XUP

> Setting up programmer environment

> Terminal Type set to: C-VT100

> You have 2983 new messages.

> Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

> Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: MD APPOINT START DATE Start Date for Encounter Appointments

> --- Setting MD APPOINT START DATE for System: <span class="mark">REDACTED</span> ---

> Days: ?

> Enter a number from 0 to 365.

> Days: ??

> Enter a number from 0 to 365 for the number of days that will be

> used to subtract from today as the start date range of the Encounter

> Appointments. If no value is entered, the default value used

> will be 200.

> Days: 365

> -------------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME: MD APPOINT END DATE End Date for Encounter Appointments

> ---- Setting MD APPOINT END DATE for System: <span class="mark">REDACTED</span> ----

> Days: ?

> Enter a number from 0 to 365.

> Days: ??

> Enter a number from 0 to 365 for the number of days that will be

> used to add to today as the end date range of the Encounter

> Appointments. If no value is entered, the default value used

> will be 0.

> Days: 2

> -------------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME: MD COMPL PROC DISPLAY DAYS Completed Proc Display Days

> Setting MD COMPL PROC DISPLAY DAYS for System: <span class="mark">REDACTED</span>

> Days: ?

> Enter the number of days from 1 to 365.

> Days: ??

> The number of days the completed procedure requests will be

> displayed in the CP Check-in screen.

> Days: 365

> -------------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME: MD DAYS TO RETAIN COM STUDY Days to Retain Completed Study

> Setting MD DAYS TO RETAIN COM STUDY for System: <span class="mark">REDACTED</span>

> Days: ?

> Enter the number of days from 1 to 365.

> Days: ??

> The number of days after check-in date/time to display the study

> that has been complete in the CPUser application. Studies that have

> procedures with multiple or cumulative results are NOT included.

> Cumulative and multiple results studies will have a default value of

> 365\.

> Days:

> -------------------------------------------------------------------------------

> Select PARAMETER DEFINITION NAME:

### [^26]Exported Kernel XPAR Parameters for Patch MD\*1.0\*11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three XPAR Parameters exported with patch MD\*1.0\*11. They are the following:

● MD CLINIC ASSOCIATION

● MD OLYMPUS 7

● MD USE APPOINTMENT

Parameter MD CLINIC ASSOCIATION will be used by option MD AUTO CHECK-IN SETUP.

The users can edit the MD OLYMPUS 7 and MD USE APPOINTMENT parameters using the Edit Parameter Values option,\[XPAR EDIT PARAMETER\].

D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: MD USE APPOINTMENT Use Appointment Location

---- Setting MD USE APPOINTMENT for System: <span class="mark">REDACTED</span> ----

Use Appointment location: ??

Set this value to Yes to allow CPUser to use the location of the

appointment selected during CP study check-in for the workload.

Otherwise, the hospital location of the CP Definition will be used.

If no value is entered, the default value is No.

Use Appointment location:

-------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME: MD OLYMPUS 7 MD OLYMPUS 7

------- Setting MD OLYMPUS 7 for System: <span class="mark">REDACTED</span> -------

Yes/No: ??

This parameter definition indicates whether the Olympus device

is version 7.3.7. The value is Yes/No. The default value

is "No".

Yes/No:

### [^27] Exported Kernel XPAR Parameter for Patch MD\*1.0\*21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three XPAR Parameters exported with patch MD\*1.0\*21. They are the MD GET HIGH VOLUME, MD NOT ADMN CLOSE MUSE NOTE, and MD USE NOTE.

The MD HIGH VOLUME PROCEDURE SETUP option is used for the high volume procedure enhancement. It lets users enter procedures that are high volume such as the electrocardiogram. The users can also indicate whether the text impression should be obtained from the Health Level 7 message from the device and add it to the note or add it to the Significant Findings of the procedure. This option excludes the selection of Hemodialysis procedures because they are handled through the CP Hemodialysis application and procedures that have “Cumulative Result” as the PROCESSED RESULT. The table below shows different ways to setup a high volume procedure:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><u>Procedure</u> <u>Text</u> <u>Setup</u></p>
<p>Any No Auto Closure with Proxy User</p>
<p>EKG(Muse) Yes Auto Closure with Proxy User,</p>
<p>Auto Closure with Muse interpreter, or</p>
<p>Significant Findings</p>
<p>Any Yes Auto Closure with Proxy User or</p>
<p>Significant Findings</p>
</blockquote></td>
</tr>
</tbody>
</table>

An example of how the option is used to setup an EKG with auto closure of an interpreter is shown below.

Select OPTION NAME: MD HIGH VOLUME PROCEDURE SETUP High Volume Procedure Setup High Volume Procedure Setup

Procedure: EKG

1 EKG, ROUTINE (12 LEADS)

2 EKG ECG

CHOOSE 1-2: 1 EKG, ROUTINE (12 LEADS)

Get Text? ?

Indicate whether the text from the result should or should not be obtained.

Enter either 'Y' or 'N'.

Get Text? YES

Use Interpreter to close note? ?

If 'YES', the interpreter of the result will be used to close

the note. If 'NO', the Proxy service will be used.

Enter either 'Y' or 'N'.

Use Interpreter to close note? YES

Procedure:

An example of how the option is used to setup a Colonoscopy with significant findings is shown below.

# Select OPTION NAME: MD HIGH VOLUME PROCEDURE SETUP High Volume Procedure Setup High Volume Procedure Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Procedure: COLON

1 COLONOSCOPY

2 COLONOSCOPY - HIST

CHOOSE 1-2: 1 COLONOSCOPY

Get Text? YES

Do Not Auto Close Note? No// ?

If 'YES', the text of the result will be in the significant finding of the

procedure.

If 'NO', the default auto closure will be used.

Enter either 'Y' or 'N'.

Do Not Auto Close Note? No// YES

If “NO” is entered for the prompt, “Do Not Auto Close Note?”, the proxy user will be used to auto close the note. If “YES”, Significant findings will be used. The only time the user will see the prompt “Use Interpreter to Close the Note?”, is when the procedure uses the Muse device such as the EKGs.

At the Procedure prompt, you can enter a “?”. At initial data entry, there will be no display but the CP Definition search is available. Once you have setup procedures, you will see a list of the procedures entered displayed when you enter a question mark. You will see the procedure name, text or no text, and Auto (auto closure with proxy), SF (Significant Findings), or Muse Interpreter) displayed; otherwise, you can search for a CP Definition.

Select OPTION NAME: MD HIGH VOLUME PROCEDURE SETUP High Volume Procedure

Setup

High Volume Procedure Setup

Procedure: ?

COLONOSCOPY Text SF

EKG, ROUTINE (12 LEADS) Text Muse Interpreter

SPIROMETRY No Text Auto

Answer with CP DEFINITION NAME, or ID

Do you want the entire CP DEFINITION List?

You can remove an existing procedure that was setup as a high volume procedure. When you select a procedure that was already entered, the option will prompt you with a question, “ Delete current procedure setup? NO//” that has a default answer of “NO”. If “YES” is entered, the procedure will be deleted from the high volume procedure list.

Select OPTION NAME: MD HIGH VOLUME PROCEDURE SETUP High Volume Procedure Setup

High Volume Procedure Setup

Procedure: SPIROMETRY

Delete current procedure setup? NO// YES...Procedure deleted

Procedure:

### [^28]Exported Kernel XPAR Parameters for Patch MD\*1.0\*20

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two XPAR Parameters exported with patch MD\*1.0\*20. They are the following:

● MD DAYS TO RET COM MULT

● MD DEVICE SURVEY TRANSMISSION

MD DAYS TO RET COM MULT allows a user to define the numbers of days to display a study

which has cumulative or multiple results after the study has been completed. This can be used to manage the display screen in CPUser executable.

Example parameter edit:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: MD DAYS TO RET COM MULT Days to Retain Completed Multiple Study

-- Setting MD DAYS TO RET COM MULT for System: <span class="mark">REDACTED</span> --

Days: ??

The number of days after check-in date/time to display the study

that has been completed in the CPUser application. This only

pertains to studies that have procedures with multiple studies.

Days:

The MD DEVICE SURVEY TRANSMISSION parameter acts as a flag for the site to indicate whether or not to send information to the Hines Field Office.

Example parameter edit:

Select PARAMETER DEFINITION NAME: MD DEVICE SURVEY TRANSMISSION Device Survey Transmission

Setting MD DEVICE SURVEY TRANSMISSION for System: <span class="mark">REDACTED</span>

Yes/No: ??

Used to determine if the site wants to transmit the device survey to

Hines. Enter 'Y' for 'YES' to send the survey or 'N' for 'NO' to

suppress the transmission.

Yes/No: YES

Sample Medical Device Survey Collection:

During patch 20 installation, the IRM support will be asked, "Do you want to run the device survey transmission?" If "No" is entered, the MD DEVICE SURVEY TRANSMISSION" Parameter Definition will be set to "NO" and the survey transmission will be suppressed. If "YES" is entered, the MD DEVICE SURVEY TRANSMISSION" Parameter Definition will be set to "YES" and a snapshot of a list of device information will be collected in the post-installation run. This device list collection will be sent to Hines Mail Group MDDEVICE for processing. A sample screen capture of the device information is shown below:

Subj: Medical Device Name Report \[#179939\] 12 Dec 2008 11:49:50 -0500 (CDT)

23 lines

From: \<POSTMASTER@<span class="mark">REDACTED</span>\> In 'IN' basket. Page 1

------------------------------------------------------------------------------

499^OLYMPUS^C^0^ZZZNOTHING,NOTHING

499^SMC^C^0^ZZZNOTHING,NOTHING

499^BRAUN^C^0^ZZZNOTHING,NOTHING

499^Muse EKG^C^0^ZZZNOTHING,NOTHING

499^Muse Pacemaker EKG^C^0^ZZZNOTHING,NOTHING

499^Muse Exercise^C^0^ZZZNOTHING,NOTHING

499^Muse Holter^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS EGD^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Colonoscopy^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Sigmoidoscopy^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS ERCP^C^0^ZZZNOTHING,NOTHING

499^Muse^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Endo Ultrasound^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS EGDPEG^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Liver Biopsy^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Paracentesis^C^0^ZZZNOTHING,NOTHING

499^OLYMPUS Enteroscopy^C^0^ZZZNOTHING,NOTHING

499^CLINIVISION^C^0^ZZZNOTHING,NOTHING

The device information collected is as follows:

- Station number
- Device name
- Process Code: Medicine, CP, or CLIO ( Clinical Observation)
- Active
- Name of Person who ran the survey collection

> **NOTE:** Once the Parameter Definition indicator is set to "YES," the device survey is collected each time the instrument record is edited. The data is collected automatically in the background.

# [^29]Application Proxy User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Application Proxy user called CLINICAL,DEVICE PROXY SERVICE will be created with

the post-init routine of patch MD\*1.0\*21. This user will be used to administratively close the note associated with the study for high volume procedures. After the installation of patch 21, the IRM Programmer support at the site should check the application proxy user to ensure it was created and enter a SIGNATURE BLOCK TITLE for this user. The site can designate its own SIGNATURE BLOCK TITLE. The example below shows how one can use VA FileMan to view the application proxy user in the NEW PERSON file (#200).

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: CP RESULT REPORT// 200 NEW PERSON

(1197 entries)

Select NEW PERSON NAME: CLINICAL,DEVICE PROXY SERVICE

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computes

DISPLAY AUDIT TRAIL? No// NO

NAME: CLINICAL,DEVICE PROXY SERVICE DATE ENTERED: MAR 13, 2009

CREATOR:XXXXX,XXXX

SECONDARY MENU OPTIONS: MD GUI MANAGER

SECONDARY MENU OPTIONS: MD GUI USER

TIMESTAMP: 61433,34906

User Class: APPLICATION PROXY ISPRIMARY: Yes

The first example below shows how you can add a Signature Block Title for CLINICAL,DEVICE PROXY SERVICE user. The second example below shows what the record looks like afterwards.

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: NEW PERSON//

EDIT WHICH FIELD: ALL// SIGNATURE BLOCK TITLE

THEN EDIT FIELD:

Select NEW PERSON NAME: CLINICAL,DEVICE PROXY SERVICE

SIGNATURE BLOCK TITLE: Clinical,Device Proxy Service

OUTPUT FROM WHAT FILE: NEW PERSON//

Select NEW PERSON NAME: CLINICAL,DEVICE PROXY SERVICE

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computes

DISPLAY AUDIT TRAIL? No// NO

NAME: CLINICAL,DEVICE PROXY SERVICE DATE ENTERED: MAR 13, 2009

CREATOR:XXXXX,XXXX

SIGNATURE BLOCK TITLE: Clinical, Device Proxy Service

SECONDARY MENU OPTIONS: MD GUI MANAGER

SECONDARY MENU OPTIONS: MD GUI USER

TIMESTAMP: 61433,34906

User Class: APPLICATION PROXY ISPRIMARY: Yes

# # Scheduled Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^30]Two options are added by patch MD\*1\*14.

NAME: MD SCHEDULED STUDIES MENU TEXT: Scheduled Studies

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It will process the HL7

messages that need to be sent to the device on a daily basis for CP studies.

ROUTINE: EN1^MDWORSR SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: SCHEDULED STUDIES

NAME: MD STUDY CHECK-IN MENU TEXT: Study Check-in

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It checks-in CP studies

for procedures that require multiple encounters such as Hemodialysis,

Respiratory Therapy, and Sleep Studies.

ROUTINE: CLINICPT^MDWORSR SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: STUDY CHECK-IN

The two options needs to be scheduled to run daily.

Schedule the option MD SCHEDULED STUDIES to start the next day after patch installation at 4am. This task will process the studies that are associated with the appointments that are dated for that day. If the procedure request is associated with a future appointment, the study that is auto checked-in will have a status of “New”. The MD SCHEDULED STUDIES task will process the study and change the status to “Pending Instrument Data”.

Sample Screen capture of the scheduled option:

Select OPTION to schedule or reschedule: MD

1 MD SCHEDULED STUDIES Scheduled Studies

2 MD STUDY CHECK-IN Study Check-in

CHOOSE 1-2: 1 MD SCHEDULED STUDIES Scheduled Studies (R)

Edit Option Schedule

Option Name: MD SCHEDULED STUDIES

Menu Text: Scheduled Studies TASK ID: 2619819

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAY 22,2007@04:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: site volume

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

Schedule the option MD STUDY CHECK-IN to start to run the next day after patch installation at 5am. If a procedure request requires multiple encounters, this task will auto check-in the study for the multiple encounters using the appointment scheduled. The RESCHEDULING FREQUENCY can be more than 1D (1 day), if your site schedule appointment for the day after 5am and the task will not be able to pick it up.

Select OPTION to schedule or reschedule: MD STUDY CHECK-IN Study Check-in

...OK? Yes// (Yes)

\(R\)

Edit Option Schedule

Option Name: MD STUDY CHECK-IN

Menu Text: Study Check-in TASK ID: 2620037

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAY 22,2007@05:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: site volume

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

[^31]One option was added with patch MD\*1.0\*11 called MD PROCESS NOSHOW/CANCEL.

NAME: MD PROCESS NOSHOW/CANCEL

MENU TEXT: Process No Show/Cancel Studies

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

PACKAGE: CLINICAL PROCEDURES

DESCRIPTION: This option is tasked to run daily. It will check for any

appointment that is No Show or Cancelled for CP studies in the "Pending

Instrument Data" status.

ROUTINE: EN1^MDWCAN

UPPERCASE MENU TEXT: PROCESS NO SHOW/CANCEL STUDIES

This option should be scheduled to run once daily at the end of the day. It is recommended that the option run at the end of the day at 4pm or 5pm. You can increase the RESCHEDULING FREQUENCY to every hour (1H) or every 90 seconds (90S) to pick up no shows and cancellations of the same day.

Select OPTION to schedule or reschedule: MD PROCESS NOSHOW/CANCEL Process

No Show/Cancel Studies

...OK? Yes// (Yes)

\(R\)

Edit Option Schedule

Option Name: MD PROCESS NOSHOW/CANCEL

Menu Text: Process No Show/Cancel Studies TASK ID: 3331757

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUN 23,2008@16:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: Site volume

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

> **NOTE:** It is recommended that all three tasks have the SPECIAL QUEUEING field be set as Startup Persistent so if the task is stopped unexpectedly, it will be re-started

[^32]Patch MD\*1\*21 exported a new option, MD PROCESS RESULTS, that needs to be scheduled with the frequency of every 1 hour daily. This task will update the procedure status to “Complete”. This task will work in conjunction with the administrative closure of the high volume procedure note.

Select OPTION to schedule or reschedule: MD PROCESS

1 MD PROCESS NOSHOW/CANCEL Process No Show/Cancel Studies

2 MD PROCESS RESULTS MD Process Results

CHOOSE 1-2: 2 MD PROCESS RESULTS MD Process Results (R)

Edit Option Schedule

Option Name: MD PROCESS RESULTS

Menu Text: MD Process Results TASK ID: 3667983

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAY 6,2009@08:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1H

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

# Setting Up Consults for Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to set up services and procedures in the Consults package. Be sure the GMRC\*3\*17 patch is present before you implement Consults.

Topics discussed in this chapter are:

- [Step 1 – Setting Up Consult Services](#step-1-setting-up-consult-services)
- [Step 2 – Creating Consult Procedures](#step-2---creating-consult-procedures)

## Step 1 – Setting Up Consult Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult services must be set up so that users can receive alerts about procedure status and be able to process the procedure. You need to determine if a consult service exists that can be used only for CP procedures or if you need to create new consult services. A CP consult service is a subspecialty service that deals specifically with CP procedures. Be sure to use the CP prefix when you add a service.

Create a New Consult Service/Define an Interpreter:

You use the Consult Management menu to create a new consult service, to define an interpreter, and add that new consult service under the All Services specialty/subspecialty. A new consult service has to be added to the “All Services” specialty/subspecialty before the CP procedures will appear on the Consults tab in CPRS.

RPT Consult Tracking Reports ...

SS Set up Consult Services

SU Service User Management

CS Consult Service Tracking

RX Pharmacy TPN Consults

GU Group update of consult/procedure requests

UA Determine users' update authority

UN Determine if user is notification recipient

NR Determine notification recipients for a service

TD Test Default Reason for Request

LH List Consult Service Hierarchy

PR Setup procedures

CP Copy Prosthetics services

DS Duplicate Sub-Service

IFC IFC Management Menu ...

TP Print Test Page

\*\*\*\*\*\* Select Consult Management Option: SS Set up Consult Services

Select Service/Specialty:CP CARDIOLOGY

Are you adding 'CP CARDIOLOGY' as a new REQUEST SERVICES (the 123RD)? No// Y (Yes)

SERVICE NAME: CP CARDIOLOGY// \<RET\>

ABBREVIATED PRINT NAME (Optional): CARDIOL

INTERNAL NAME: \<RET\>

Select SYNONYM: \<RET\>

SERVICE USAGE: \<RET\>

SERVICE PRINTER: \<RET\>

NOTIFY SERVICE ON DC: \<RET\>

REPRINT 513 ON DC: \<RET\>

PREREQUISITE:

No existing text

Edit? NO// \<RET\>

PROVISIONAL DX PROMPT: \<RET\>

PROVISIONAL DX INPUT: \<RET\>

DEFAULT REASON FOR REQUEST: \<RET\>

No existing text

Edit? NO// \<RET\>

RESTRICT DEFAULT REASON EDIT: \<RET\>

Inter-facility information

IFC ROUTING SITE: \<RET\>

IFC REMOTE NAME: \<RET\>

Select IFC SENDING FACILITY: \<RET\>

To define an interpreter, you can enter a user name in one of the following fields.

> **NOTE:** Users entered into Update Users W/O Notifications or Update Teams W/O Notifications will not receive alerts.

\- INDIVIDUAL TO NOTIFY  
- SERVICE TEAM TO NOTIFY  
- NOTIFICATION BY PT LOCATION  
- UPDATE USERS W/O NOTIFICATIONS  
- UPDATE TEAMS W/O NOTIFICATIONS

SERVICE INDIVIDUAL TO NOTIFY: CPPROVIDER, ONE

Select SERVICE TEAM TO NOTIFY: CONSULT TEAM

Select NOTIFICATION BY PT LOCATION: \<RET\>

PROCESS PARENTS FOR NOTIFS: \<RET\>

Select UPDATE USERS W/O NOTIFICATIONS: CPUSER, THREE

Select UPDATE TEAMS W/O NOTIFICATIONS: \<RET\>

Select UPDATE USER CLASS W/O NOTIFS: \<RET\>

Select ADMINISTRATIVE UPDATE USER: \<RET\>

Select ADMINISTRATIVE UPDATE TEAM: \<RET\>

PROCESS PARENTS FOR UPDATES: \<RET\>

SPECIAL UPDATES INDIVIDUAL: \<RET\>

RESULT MGMT USER CLASS: \<RET\>

UNRESTRICTED ACCESS: \<RET\>

Select SUB-SERVICE/SPECIALTY: \<RET\>

Add/Edit Another Service? NO// \<RET\>

Now the service you just created must be added to the All Services service/specialty.

Select Consult Management Option: SS Set up Consult Services

Select Service/Specialty:ALL SERVICES GROUPER ONLY

SERVICE NAME: ALL SERVICES// \<RET\>

ABBREVIATED PRINT NAME (Optional): ALL// \<RET\>

Select SYNONYM: \<RET\>

SERVICE USAGE: GROUPER ONLY// \<RET\>

SERVICE PRINTER: \<RET\>

NOTIFY SERVICE ON DC: \<RET\>

REPRINT 513 ON DC: \<RET\>

PREREQUISITE:

No existing text

Edit? NO// \<RET\>

PROVISIONAL DX PROMPT: \<RET\>

PROVISIONAL DX INPUT: \<RET\>

DEFAULT REASON FOR REQUEST:

No existing text

Edit? NO// \<RET\>

RESTRICT DEFAULT REASON EDIT: \<RET\>

SERVICE INDIVIDUAL TO NOTIFY: CPPROVIDER, ONE

Select SERVICE TEAM TO NOTIFY: CONSULT TEAM

Select NOTIFICATION BY PT LOCATION: \<RET\>

PROCESS PARENTS FOR NOTIFS: \<RET\>

Select UPDATE USERS W/O NOTIFICATIONS: CPUSER, THREE

Select UPDATE TEAMS W/O NOTIFICATIONS: \<RET\>

Select UPDATE USER CLASS W/O NOTIFS: \<RET\>

Select ADMINISTRATIVE UPDATE USER: \<RET\>

Select ADMINISTRATIVE UPDATE TEAM: \<RET\>

PROCESS PARENTS FOR UPDATES: \<RET\>

SPECIAL UPDATES INDIVIDUAL: \<RET\>

RESULT MGMT USER CLASS: \<RET\>

UNRESTRICTED ACCESS: \<RET\>

Select SUB-SERVICE/SPECIALTY: CP CARDIOLOGY

Are you adding 'CP CARDIOLOGY' as a new SUB-SERVICE (the 13TH for this REQUEST SERVICES)? No// Y

(Yes)

MNEMONIC:

Select SUB-SERVICE/SPECIALTY: \<RET\>

Add/Edit Another Service? NO//\<RET\>

Editing Users of an Existing Consult Service:

You can also use the Service User Management option to edit a Consult Service’s Update Users fields.

RPT Consult Tracking Reports ...

SS Set up Consult Services

SU Service User Management

CS Consult Service Tracking

RX Pharmacy TPN Consults

GU Group update of consult/procedure requests

UA Determine users' update authority

UN Determine if user is notification recipient

NR Determine notification recipients for a service

TD Test Default Reason for Request

LH List Consult Service Hierarchy

PR Setup procedures

CP Copy Prosthetics services

DS Duplicate Sub-Service

IFC IFC Management Menu ...

TP Print Test Page

Select Consult Management Option: SU Service User Management

Select Service/Specialty: cp cardiology

Make sure data is entered for the applicable fields listed below:

SERVICE INDIVIDUAL TO NOTIFY: CPPROVIDER, ONE

Select SERVICE TEAM TO NOTIFY: CONSULT TEAM

Select NOTIFICATION BY PT LOCATION: \<RET\>

Select UPDATE USERS W/O NOTIFICATIONS: CPUSER, THREE

Select UPDATE TEAMS W/O NOTIFICATIONS: \<RET\>

Select UPDATE USER CLASS W/O NOTIFS: \<RET\>

Select ADMINISTRATIVE UPDATE USER: \<RET\>

Select ADMINISTRATIVE UPDATE TEAM: \<RET\>

SPECIAL UPDATES INDIVIDUAL: \<RET\>

Select Service/Specialty: \<RET\>

## Step 2 - Creating Consult Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult procedures in the GMRC file (#123.3) must be linked to clinical procedures. Be sure to use the “CP” prefix when you create new consult procedures to differentiate them from other consult procedures.

The following example shows how to create the consult procedure CP EKG 12 LEAD STAT and link it to the clinical procedure definition EKG, ROUTINE (12 LEADS).

[^33]Note: Add the text “Visit Date: \|VISIT DATE\|“ to the first line of the DEAFULT REASON FOR REQUEST field. This will allow CP to pick up the appointment date/time from CPRS for the order request and use it for the auto CP study check-in. If you do not use appointments at all, you can skip the adding of the text. If your site schedules appointments, but the ordering provider does not select the appointment during ordering, you can still add the text. If there is already text in the DEFAULT REASON FOR REQUEST field, add the visit date text to the very first line.

Select Consult Management Option: PR Setup procedures

Select Procedure:CPEKG 12LEAD STAT

NAME: CP EKG 12 LEAD STAT// \<RET\>

INACTIVE: NO// \<RET\>

Select SYNONYM: EKG// \<RET\>

INTERNAL NAME: \<RET\>

Select RELATED SERVICES: CP CARDIOLOGY// \<RET\>

TYPE OF PROCEDURE: ECG// \<RET\>

CLINICAL PROCEDURE: EKG, ROUTINE (12 LEADS)// \<RET\>

PREREQUISITE:

No existing text

Edit? NO// \<RET\>

PROVISIONAL DX PROMPT: REQUIRED// \<RET\>

PROVISIONAL DX INPUT: LEXICON// \<RET\>

DEFAULT REASON FOR REQUEST:

1\>Visit Date: \|VISIT DATE\|

2\>Patient’s heart is beating abnormally. Needs analysis.

Edit? NO// \<RET\>

RESTRICT DEFAULT REASON EDIT: NO EDITING// \<RET\>

Orderable Item Updated

Field Descriptions:

NAME: The name of the procedure as it appears in the GMRC Procedure file (#123.3).

INACTIVE: Indicates if a procedure is no longer in use.

SYNONYM: Enter other names commonly used to refer to this procedure.

INTERNAL NAME: Enter a name for the procedure that is used internally by the facility.

RELATED SERVICES: Indicates which Consult services from the Request Services (#123.5) file are responsible for processing requests for this procedure.

TYPE OF PROCEDURE: Not applicable.

CLINICAL PROCEDURE: Provides a mapping between the CP Definitions (#702.01) file and the GMRC Procedures file. (CP definition entries must be active before you can map them.) Orders placed for a procedure having a valid entry in this field are processed and resulted using the Clinical Procedures package.

PREREQUISITE: Enter information on any consults or procedures that must be performed prior to ordering this consult. This field is presented to the ordering person upon selecting a Consult service and lets the ordering person abort the ordering if necessary. TIU objects may be embedded within this field, which are resolved for the current patient during ordering. Any TIU objects must be contained within vertical bars, such as \|BLOOD PRESSURE\|.

PROVISIONAL DX PROMPT: Used by CPRS to determine how to prompt for the provisional diagnosis when ordering this procedure. Set to OPTIONAL if you want the user to be prompted for the provisional diagnosis but also can let the user bypass answering the prompt. Set to SUPPRESS if you do not want the user to be presented with the provisional diagnosis prompt. Set to REQUIRED if you want to enforce the user to answer the prompt before continuing to place the order.

PROVISIONAL DX INPUT: Determines the method that CPRS uses to prompt the user for input of the provisional diagnosis when ordering this procedure. Set to FREE TEXT and the user may type any text from 2-80 characters in length. Set to LEXICON and the user is required to select a coded diagnosis from the Clinical Lexicon.

DEFAULT REASON FOR REQUEST: Enter default text that can be used as the reason for request when ordering this procedure. This field allows boilerplate text to be imported into the reason for request. If the user places an order using a quick order having boilerplate text, that text supersedes any default text stored in this field. This field may contain any text including TIU objects. TIU Objects must be enclosed in vertical bars, such as \|PATIENT NAME\|.

RESTRICT DEFAULT REASON EDIT: Set to UNRESTRICTED, NO EDITING, or ASK ON EDIT ONLY. If ASK ON EDIT ONLY is used, the user can only edit the default reason if the order is edited before releasing to the service. If a default reason for request exists, the option set in this field affects the ordering person’s ability to edit the default reason.

# Setting Up CPRS for Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to set up notifications and parameters in the CPRS package.

Topics discussed in this chapter are:

- [Step 1 – Setting Up the Notification](#step-1-setting-up-the-notification) - Recommended
- [Step 2 – Editing Parameters](#step-2-editing-parameters) – Some parameters must be defined. See Step 2 – Editing Parameters, p. [10-2](#step-2-editing-parameters).

## Step 1 – Setting Up the Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must enable the CONSULT/PROC INTERPRETATION notification if you want to receive the “Ready for interpretation” alert in CPRS. You can enable the alert for one user, several users, or for the entire service. Use the Notification Mgmt Menu \[ORB NOT COORD MENU\].

1 Enable/Disable Notifications

2 Erase Notifications

3 Set Urgency for Notifications (GUI)

4 Set Deletion Parameters for Notifications

5 Set Default Recipient(s) for Notifications

6 Set Default Recipient Device(s) for Notifications

7 Set Provider Recipients for Notifications

8 Flag Orderable Item(s) to Send Notifications

9 Archive(delete) after \<x\> Days

10 Forward Notifications ...

11 Set Delays for Unverified Orders ...

12 Set Notification Display Sort Method (GUI)

13 Send Flagged Orders Bulletin

14 Determine Recipients for a Notification

15 Display Patient Alerts and Alert Recipients

16 Enable or Disable Notification System

17 Display the Notifications a User Can Receive

Select Notification Mgmt Menu Option: 1 Enable/Disable Notifications

Set PROCESSING FLAG Parameters for Notifications

Processing Flag may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Team (OE/RR) OTL \[choose from OE/RR LIST\]

3 Service SRV \[choose from SERVICE/SECTION\]

4 Location LOC \[choose from HOSPITAL LOCATION\]

5 Division DIV \[<span class="mark">REDACTED</span>\]

6 System SYS \[<span class="mark">REDACTED</span>\]

7 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: Set this parameter according to the individual preference of your site.

------------- Setting Processing Flag -------------

Select Notification: ?

There are currently no entries for Notification.

Answer with OE/RR NOTIFICATIONS NUMBER, or NAME, or PACKAGE ID, or

MESSAGE TEXT

Do you want the entire 49-Entry OE/RR NOTIFICATIONS List? N (No)

Select Notification: CONSULT/PROC INTERPRETATION

Are you adding CONSULT/PROC INTERPRETATION as a new Notification? Yes// \<RET\> YES

Notification: CONSULT/PROC INTERPRETATION// \<RET\> CONSULT/PROC INTERPRETATION CONSULT/PROC INTERPRETATION

Value: ?

Code indicating processing flag for the entity and notification.

Select one of the following:

M Mandatory

E Enabled

D Disabled

Value: Enabled

- Select Mandatory to specify that the notification cannot be turned off by the user.
- Select Enabled to specify that the user can turn off the notifications.
- Select Disabled to specify that notifications are not used.

After you set up the notification, you can set up quick orders and place them on appropriate order menus. Refer to the CPRS Setup Guide, which can be found in the [VistA Documentation Library (VDL)](http://www.va.gov/vdl/).

## Step 2 – Editing Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can edit the following parameters in CPRS to indicate who should enter Patient Care Encounter information and how Windows messages are sent. You can also add CP User to the CPRS Tools menu.

Use the CPRS Manager menu to set these parameters:

- [Ask Encounter Update (ORWPCE ASK ENCOUNTER UPDATE)](#ask-encounter-update-orwpce-ask-encounter-update) Required.
- [Broadcast Messages to Other Apps (ORWOR BROADCAST MESSAGES)](#broadcast-messages-to-other-apps-orwor-broadcast-messages) Required.
- [Force PCE Entry (ORWPCE FORCE PCE ENTRY)](#force-pce-entry-orwpce-force-pce-entry) Required.
- [Add CP User to the CPRS Tools Menu](#add-cp-user-to-the-cprs-tools-menu-orwt-tools-menu) Optional.

### Ask Encounter Update (ORWPCE ASK ENCOUNTER UPDATE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORWPCE ASK ENCOUNTER UPDATE parameter determines if the user should be prompted to enter encounter information when signing a note. The Encounter Form in the AICS package is used to collect workload data. If a specific Encounter Form is not set up and linked to a hospital location, a generic Encounter Form is presented. Each service that has a study associated with it must set this parameter to Always.

Select OPTION NAME: CPRS MANAGER MENU ORMGR CPRS Manager Menu

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

XX General Parameter Tools ...

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

SELECT PARAMETER DEFINITION NAME: ORWPCE ASK ENCOUNTER UPDATE Ask Encounter Update

ORWPCE ASK ENCOUNTER UPDATE may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Service SRV \[choose from SERVICE/SECTION\]

4 Division DIV \[<span class="mark">REDACTED</span>\]

5 System SYS \[<span class="mark">REDACTED</span>\]

6 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: Set this parameter according to the individual preference of your site.

-------- Setting ORWPCE ASK ENCOUNTER UPDATE --------

ASK ENCOUNTER UDPATE: ALWAYS

If the site wants credit for workload for the inpatient and outpatient, select Always at this prompt.

### Broadcast Messages to Other Apps (ORWOR BROADCAST MESSAGES)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORWOR BROADCAST MESSAGES parameter tells CPRS to send a message to all VistA applications stating that a new patient record is open or a new TIU note has been selected. This parameter setting allows all applications on the desktop, such as CP User, and VistA Imaging, to synchronize with CPRS. Always set this parameter to System.

Select PARAMETER DEFINITION NAME: ORWOR BROADCAST MESSAGES Broadcast Window Messages to Other Apps

ORWOR BROADCAST MESSAGES may be set for the following:

1 User USR \[choose from NEW PERSON\]

5 System SYS \[<span class="mark">REDACTED</span>\]

10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 5 System <span class="mark">REDACTED</span>

\- Setting ORWOR BROADCAST MESSAGES for System: <span class="mark">REDACTED</span> -

Enable Broadcasting Windows Messages: YES// \<RET\>

### Force PCE Entry (ORWPCE FORCE PCE ENTRY)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If encounter data is missing, the user should be asked to enter the missing data. You must select Yes to the Force GUI PCE ENTRY prompt.

Select PARAMETER DEFINITION NAME: ORWPCE FORCE PCE ENTRY Force PCE Entry

ORWPCE FORCE PCE ENTRY may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Service SRV \[choose from SERVICE/SECTION\]

4 Division DIV \[<span class="mark">REDACTED</span>\]

5 System SYS \[<span class="mark">REDACTED</span>\]

6 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: Set this parameter according to the individual preference of your site.

---------- Setting ORWPCE FORCE PCE ENTRY ----------

FORCE GUI PCE ENTRY: ?

Do you wish to force entry of PCE data in the CPRS GUI?.

Select one of the following:

0 NO

1 YES

FORCE GUI PCE ENTRY: 1 YES

When data is needed and the user is the primary encounter provider, the ORWPCE FORCE PCE ENTRY parameter is checked to determine if the user needs to enter the missing encounter information before being allowed to sign the note. When this parameter is set to YES, users are asked to enter the missing data. When this parameter is set to NO, users are asked if they want to enter encounter information.

When data is needed and the user is the primary encounter provider, continued checks are made during the note-signing process to determine if there is still missing data. The user is continually prompted to enter the data, regardless of the ORWPCE FORCE PCE ENTRY setting.

If data is not needed or if the user is not the primary encounter provider, “Yes” and “No” prompts are displayed and the user determines what to enter.

### Add CP User to the CPRS Tools Menu (ORWT TOOLS MENU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the ORWT TOOLS MENU to set up access to CP User from the CPRS Tools menu. You can set up the options for the site and then override them as appropriate at the division, service, and user levels. Here are some guidelines:

- Enter each item in the format, NAME=COMMAND.  
    
  NAME is the name that displays on the menu, such as CP User. If you want to provide keyboard access, you can also enter *&* in front of a letter, such as CP &User.  
    
  COMMAND is the directory path followed by the executable name.

Notes:

> • You must surround a path that contains space characters, such as C:\Program Files\\.. with quotation marks. You can also include switches in the path. Here’s an example:

> CP User=”C:\Program Files\Clinical Procedures\CP User.exe” /cprs /dfn=%DFN /s=%SRV /p=%PORT

> • You can pass context-sensitive parameters, which are entered as placeholders, and then converted to the appropriate values at runtime. The placeholder parameter used with Clinical Procedures is:

> %DFN Indicates the DFN of the currently selected patient in CPRS. This parameter passes the current patient to Clinical Procedures. You can also use %DFN as a placeholder in other CP applications.

> %SRV Indicates the name of the server that CPRS is currently connected to. This parameter passes the current server name to Clinical Procedures. You can also use %SRV as a placeholder in other CP applications.

> %PORT Indicates the listener port that CPRS is currently communicating through. This parameter passes the current listener port to Clinical Procedures. You can also use %PORT as a placeholder in other CP applications.

> • Command line switches, such as nonsharedbroker, can be used. Refer to [Appendix A - CP Application Startup Options and Command Line Switches](#appendix-a-cp-application-startup-options-and-command-line-switches), p. [16-1](#appendix-a-cp-application-startup-options-and-command-line-switches) for more information.

Example: Create a tools menu option that contains CP User.

From the system prompt, do the following:

Select PARAMETER DEFINITION NAME: orwt TOOLS MENU CPRS GUI Tools Menu ORWT TOOLS MENU may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[REGION 5\]

4 System SYS \[OEC.ISC-SLC.VA.GOV\]

Enter selection: 1 User NEW PERSON

Select NEW PERSON NAME: CPUSER, FOUR CF

-------------- Setting ORWT TOOLS MENU for User: DELAWARE,JOHN --------------

Select Sequence: 1

Are you adding 1 as a new Sequence? Yes// YES

Sequence: 1// 1

Name=Command: CP User=”\<directory name\>\CP User.exe” /cprs /dfn=%DFN /s=%SRV /p=%PORT

Select Sequence:

Figure 10‑1

When you select “CP User” from the CPRS Tools menu, CP User is displayed and the actual server, port, and global reference are substituted for the command line switches.

## [^34]Step 3- Create Ad Hoc Health Summary Components for CP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a need for the sites to be able to group a specific procedure reports for easier search by the physician. Patch MD\*1.0\*21 distributed a routine called MDPSUL. If the entry point EN2^MDPSUL is run, a list of active devices is displayed. This routine generates the LIST OF HS COMPONENTS NEEDED report. The first column of the report shows the active bi-directional devices in the Instrument list of CP Manager. The Print Routine column shows the entry point in routine MDPSU that can be used to create a Health Summary Component. The last column is an Abbreviation code that Clinical Procedures recognize as an identifier for that device. The Print Routine and Abbreviation columns are fields that the site can use to create a Health Summary Component to consolidate reports of one device in a Health Summary Component. Please contact your IRM Programmer to run this routine.

\>D EN2^MDPSUL

Select LIST Printer: HOME// TELNET Right Margin: 80//

Oct 06, 2009 8:48:17 am Page 1

LIST OF HS COMPONENTS NEEDED

Name Print Routine Abbreviation

--------------------------------------------------------

CCF CPF;MDPSU M1

EnConcert CPF;MDPSU M4

CTX (Bi-Directional) CPF;MDPSU M25

CTX Generic Echo CPF;MDPSU M26

Muse EKG CPF;MDPSU M27

Muse Exercise CPF;MDPSU M33

Muse Holter CPF;MDPSU M34

OLYMPUS EGD CPF;MDPSU M35

Someone with the GMTS MANAGER option can create the Health Summary (HS) component for the instrument generated by the report mentioned above. A sample HS component creation is demonstrated in the screenshot below.

Select OPTION NAME: GMTS MANAGER Health Summary Overall Menu

You have PENDING ALERTS

Select Health Summary Overall Menu Option: ?

1 Health Summary Coordinator's Menu ...

2 Health Summary Enhanced Menu ...

3 Health Summary Menu ...

4 Health Summary Maintenance Menu ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

You have PENDING ALERTS

Select Health Summary Overall Menu Option: 4 Health Summary Maintenance Menu

You have PENDING ALERTS

Select Health Summary Maintenance Menu Option: ?

1 Disable/Enable Health Summary Component

2 Create/Modify Health Summary Components

3 Edit Ad Hoc Health Summary Type

4 Rebuild Ad Hoc Health Summary Type

5 Resequence a Health Summary Type

6 Create/Modify Health Summary Type

7 Edit Health Summary Site Parameters

8 Health Summary Objects Menu ...

9 CPRS Reports Tab 'Health Summary Types List' Menu ...

10 CPRS Health Summary Display/Edit Site Defaults ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

You have PENDING ALERTS

Select Health Summary Maintenance Menu Option: 2 Create/Modify Health Summary C

omponents

Select COMPONENT: EKG REPORT

NAME: EKG REPORT//

PRINT ROUTINE: CPF;MDPSU//

ABBREVIATION: M27//

DESCRIPTION:

Print EKG Report Only.

Edit? NO//

TIME LIMITS APPLICABLE: yes//

MAXIMUM OCCURRENCES APPLICABLE: yes//

HOSPITAL LOCATION APPLICABLE:

ICD TEXT APPLICABLE:

PROVIDER NARRATIVE APPLICABLE:

LOCK:

DEFAULT HEADER NAME: EKG REPORT

Select SELECTION FILE:

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes//

Do you wish to review the Summary Type structure before continuing? NO//

Select COMPONENT: EKG REPORT// M27

EKG REPORT is already a component of this summary.

Select one of the following:

E Edit component parameters

D Delete component from summary

Select Action:

Please hold on while I resequence the summary order.............................

....................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select Health Summary Maintenance Menu Option:

Once you have created the HS component, you should be able to use the component in the Ad Hoc Health Summary selection in the CPRS Reports tab.

Select the Reports tab and select Ad Hoc Report within the Health Summary tree view.

![](clinical-procedures-version-1-implementation-guide/038.png)

Once you click the Ad Hoc Report, an Ad Hoc Health Summary window opens as demonstrated below:

![](clinical-procedures-version-1-implementation-guide/039.png)

Find the Health Summary component that you have created and select it. Enter the Occurrence Limit and Time Limit that you want. The Occurrence Limits field is the number of reports that you want displayed and the Time Limit is the date range to find the report such as 1Y (1 year). Once you click the “OK” button, you should generate only EKG reports found for that occurrence and time limit.

# Working with CP Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP provides bi-directional capabilities for the HL7 interface. With this feature, the VistA system can send information about a patient procedure directly to the instrument, which eliminates duplicate entries of patient data into an instrument. CP Gateway sends the results to the VistA M environment and converts the data into a usable format for the CP and VistA Imaging applications.

Every night after midnight, CP Gateway purges data based on the value in the Days to keep Instrument Data field (See CP Manager \> System Parameters). This purge only deletes the raw data that comes from the instrument. The data to be purged has already been matched to a study.

The following flowchart describes what the CP Gateway does.

![](clinical-procedures-version-1-implementation-guide/040.png)

Starting the CP Gateway application is the same as starting any VistA Broker application, which requires a VistA application and the appropriate command line switches. Refer to [Appendix A - CP Application Startup Options and Command Line Switches](#appendix-a-cp-application-startup-options-and-command-line-switches) for more information. [^35]The CP Gateway application can be run on a server or on a workstation. The application must be launched by a person with VistA Access and Verify codes. This person must be assigned the MD GUI MANAGER menu option to be able to access the CP Gateway. DO NOT run the CP Gateway on a workstation that is running VistA Imaging.

> **NOTE:** Remember to re-start the CP Gateway, if the workstation is re-started for some reason such as upgrade and patches. This will keep the connection up for the device interface and CP.

Note 2: It is not necessary but if you want to configure a stand-alone server or workstation for the CP Gateway, use the VA Naming Conventions.  Your domain will be VHAxxx where xxx is the site's 3-character assigned name (e.g.,VHAISH is the domain name at Hines Field Office).  You could use the following server name: VHA + 3-letter site name + CPG  i.e., VHAISHCPG

After the application starts, three checks are performed to ensure that the proper environment exists.

- Verifies that the CP Gateway is a compatible version with the server installation.
- Verifies that the CP Gateway is the only one running in the selected environment (such as UCI and Volume set).
- Verifies that the CP Gateway has Read Write and Delete access to the directory stored in the MD IMAGING XFER DIRECTORY parameter.

If any of these checks fail, the processor shuts down. If the checks are acceptable, the application displays on the workstation as shown, Figure 11‑1.

![](clinical-procedures-version-1-implementation-guide/041.png)

Figure 11‑1

Click Show Log to view the application log. A session log is kept for the currently running session but is not saved to the workstation’s hard drive for patient security reasons.

![](clinical-procedures-version-1-implementation-guide/042.png)

Figure 11‑2

The log file tracks all the background operations and any problems that occur during the processing of attachments, Figure 11‑2. In addition, the log file lists the date/time stamp of the background operation, a description of the background operation, and the number of studies to process at that time.

## Log File Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are available while viewing the log file.

- Click Find to rapidly search the log file. A standard Windows find dialog is displayed and you can search the entire log file for a text value.
- Click Save if you want to save the entire contents of the log to an external file. The log file is saved in Rich Text Format (RTF) and can easily be opened in MS Word or other word processing applications.
- Click Clear to clear all entries in the current sessions log file. Be careful since you cannot recover past log entries if you have not previously saved them to a file.
- Click Print to select a printer and print the log. Be careful to check the size of the log file as it may be large if you have not cleared it recently.

You can display information about the server and you can also manage how the Gateway works.

- Choose File \> Status. The server settings are displayed, Figure 11‑3.

![](clinical-procedures-version-1-implementation-guide/043.png)

Figure 11‑3

- Choose File \> Shutdown. The server process is stopped and the application is terminated.
- Choose File \> Set Poll Interval, Figure 11‑4. The CP Gateway polls for new instrument data to transmit to VistA. You can adjust the number of seconds between polling operations. Enter a value from 10 to 300 seconds. The new value becomes effective after the next polling operation so it may take up to 5 minutes for the new value to be used.

![](clinical-procedures-version-1-implementation-guide/044.png)

Figure 11‑4

- Choose File \> Set Maximum Log Entries. You can adjust the number of entries that are stored in the log file. Enter a value from 100 to 10000. After this value is reached, entries are deleted from the beginning of the log to keep the log file from growing too large. The new value becomes effective after the next polling operation so it may take up to 5 minutes for the new value to be used. When the CP Gateway is shut down, all entries are deleted from the log file.

# Setting Up HL7 Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^36]This section describes how to set up the HL7 parameters including configuration instructions, file settings, and technical issues. The tasks in this chapter require a working knowledge of the VistA HL7 application.

Topics discussed in this chapter are:

- Configuration Instructions Information
  - IP Addresses and Ports
- Setting Up a New HL7 Single Listener for High-Volume Devices
  - Creating a Logical Link
  - Creating a Device Protocol Client
  - Activating the Logical Links
  - Adding a Device Client as a Server Subscriber
- Using Port 5000
  - Benefits of Using a Single Port Listener
  - Setting Up Port 5000
- File Settings
- Technical Issues

## ## Configuration Instructions Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can follow the steps described in this section to configure the HL7 application.

MCAR INST and MCAR OUT are automatically created during the KIDS installation. MCAR INST is used for all devices that send results information from the device to VistA and CP. Since all devices can use the same link, you only need one entry in the HL Logical Link (870) file.  
<span class="mark">  
</span>However, you need to establish an MCAR OUT entry for each bi-directional device that receives information from VistA and CP. Each entry needs its own IP and port number, which agree with the device configuration. (Use the MCAR OUT sample provided in the HL Logical Link file. Set up the individual links for each bi-directional device. ) All outbound links are non-persistent.

Most devices are able to use a non-persistent connection to VistA. A persistent connection is a connection that is established by the medical device and is kept connected to VistA even after the device has transmitted it HL7 message. A non-persistent connection is a connection that is established by the medical device to VistA and is disconnected once the HL7 message has been sent. Devices can share the same HL Logical link to VistA, if they are non-persistent. If the device is persistent then it must have its own HL Logical Link to VistA (Example: its own inbound and outbound links.)

### IP Addresses and Ports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to set up IP addresses and ports for the medical devices at your facility.

An IP address consists of a string of four numbers each ranging in value from 0 to 255. Here is an example of an IP address: 10.23.55.201. When a new device is installed, be careful when you assign IP addresses to the medical devices. It’s recommended that you set aside a block of IP addresses specifically for the medical devices. The range of numbers chosen is up to the facility, but make sure that there is a large enough range to allow for some growth. For example, IP addresses 10.23.55.201 through 10.23.55.225 could be blocked and used. In this way, the IRM staff can track down any possible problems that may be related to the medical device by looking at the IP address.

A port is the location on a medical device where you send and receive data. Some ports have predefined functions. For example, Port 80 is set up for the Web Server. Some vendors have predefined ports that they may want you to use. For example, Sensormedics recommends using Port 20000 for the VMAX. Others may only allow a limited range. Consult the device manual to determine which ports you can use.

A Startup Node defines the system on which you want the link to start.

## Setting Up a New HL7 Single Listener for High-Volume Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most medical devices send results to VistA using nonpersistent connections to the same port. Each device connects to the port just long enough to send results to VistA, then releases the port so that other devices may connect to it.

However, if you use a high-volume device (i.e., something that sends about 200 or more messages back and forth per day, such as MUSE or a hemodialysis device) that sends a lot of data all the time, we recommend that you give it its own port instead of sharing a port with other devices. This is because high-volume devices send so much data that they can tie up the port for a long time, preventing other devices (e.g., Olympus or Sensormedics) from using it.

Setting up a new HL7 listener involves four steps (which are described in more detail below):

1.  Creating a Logical Link
2.  Creating a Device Protocol Client
3.  Activating the Logical Links
4.  Adding a Device Client as a Server Subscriber

This document also contains information on Using Port 5000 what it is and when to use it).

> **NOTE:** Although you can name your new logical links and device protocols anything you want, keep the names name spaced and descriptive since the names are similar and it can be easy to confuse them.

### Creating a Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A logical link is an inbound or an outbound instrument data port from and to the medical device. It’s a listener waiting for data to come across. The first logical link (MCAR INST) is already created by default. To create a new HL7 single listener logical link for your device, you need to create a new logical link or edit an existing one. Each bi-directional device that receives information from VistA and CP needs its own outbound link set up. All non-persistent devices can share the same inbound logical link, but persistent devices each need their own inbound logical links.

1.  Decide which port to use. The facility, along with IRM, determines which port to use. This is the port used by the device to send data to the VistA listener. You can, for example, use port 1026 for Hemodialysis results and port 1027 for Sensormedics results. Do not use port 5000 for this type of setup. (See below for more information on port 5000.)
2.  From the Systems Manager Menu, choose HL Main Menu (HL) \> Interface Developer Options (IN) \> Link Edit (EL).
3.  At the Select HL Logical Link Note prompt, enter the name of the new logical link for your device. Name your new inbound logical link something like MCAR2 INST. The next one (if you use more than one high-volume device) can be called MCAR3 INST, etc. For an outbound logical link, the following naming convention is suggested: MCAR xxx, where xxx is the first three characters of the device or vendor name. (For example, an outbound link for an Olympus device could be named MCAR OLY.)
4.  Type yes when asked if you are adding ‘MCAR2 INST’ as a new HL LOGICAL LINK. The HL7 LOGICAL LINK screen displays.

HL7 LOGICAL LINK

-----------------------------------------------------------------------

NODE: MCAR2 INST

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 100

LLP TYPE: TCP \<RET\>

DNS DOMAIN:

> **NOTE:** When this screen first displays for a new logical link, only the NODE and QUEUE SIZE fields will already contain values. The NODE field will display the logical link name you just created, and the QUEUE SIZE field will default to 10.

5.  Type Enabled in the Autostart field.
6.  Change the QUEUE SIZE value to 100. (Optional)
7.  Enter TCP in the LLP TYPE field, then press \[Enter\] to display the HL7 LOGICAL LINK screen (see following example).

HL7 LOGICAL LINK

-----------------------------------------------------------------------------

┌─────────────────────TCP LOWER LEVEL PARAMETERS──────────────────────────┐

│ MCAR3 INST │

│ │

│ TCP/IP SERVICE TYPE: SINGLE LISTENER │

│ TCP/IP ADDRESS: │

│ TCP/IP PORT: 1026 │

│ TCP/IP PORT (OPTIMIZED): │

│ │

│ ACK TIMEOUT: 60 RE-TRANSMISION ATTEMPTS: 3 │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: ignore │

│ BLOCK SIZE: SAY HELO: │

│ │

│STARTUP NODE: DEV:ISC4A2 PERSISTENT: NO │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8.  Set TCP/IP SERVICE TYPE to SINGLE LISTENER. If this link is an outbound link then the TCP/IP SERVICE TYPE is CLIENT (SENDER).
9.  In the TCP/IP ADDRESS field, if the link you are creating is an outbound link to a device, you will need to enter the TCP/IP address of that device. For the inbound link, no address is needed.
10. In the TCP/IP PORT field, enter the port number you decided to use (in step 1).
11. Optionally set ACK TIMEOUT to 60.
12. Press \[Tab\] to optionally set RE-TRANSMISION ATTEMPTS to 3.
13. Optionally set EXCEED RE-TRANSMIT ACTION to ignore.
14. Enter the appropriate STARTUP NODE.
15. Set the PERSISTENT field to NO.
16. \[Tab\] down to the COMMAND prompt, then select Close. You return to the HL7 LOGICAL LINK screen.
17. \[Tab\] down to the COMMAND prompt, then select Save.
18. At the COMMAND prompt, select Exit.
19. The new link is useless until you assign protocols to it. Proceed to the next section to create a client protocol.

Below is an example of an outbound link.

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ MCAR OLY │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: 10.3.17.141 │

│ TCP/IP PORT: 9027 │

│ TCP/IP PORT (OPTIMIZED): │

│ │

│ ACK TIMEOUT: 60 RE-TRANSMISION ATTEMPTS: 3 │

│ READ TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore │

│ BLOCK SIZE: SAY HELO: │

│ DIRECT CONNECT OPEN TIMEOUT: │

│STARTUP NODE: DEV:DEVISC4A1 PERSISTENT: NO │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

### Creating a Device Protocol Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have to create a protocol for every inbound listener to VistA.

To create a protocol client from for your new logical link using a copy, follow these steps:

1.  Look at the protocol in 101 or use developer tools. Copy MCAR DEVICE CLIENT to make a new device client. Name it something like MCAR2 DEVICE CLIENT.
2.  Change the entry in the Logical Link field to match the new logical link. For example, if you just created a logical link named MCAR2 INST, change what’s in the Logical Link field from MCAR INST to MCAR2 INST. All other fields should match what was originally in MCAR DEVICE CLIENT.
3.  Proceed to the next section to make the new device protocol a subscriber to the device server.

To create a new protocol client for your new logical link, do the following:

1.  From the Systems Manager Menu, choose HL Main Menu (HL) \> Interface Developer Options (IN) \> Protocol Edit (EP).
2.  At the Select PROTOCOL NAME prompt, enter the name of the new device client for your device. Name your new device client something like MCAR2 Device Client or MCAR2 MUSE (depending on the device name).
3.  Type yes (or simply type y) when asked if you are adding ‘MCAR2 Device Client’ as a new PROTOCOL.
4.  Enter Instrument Device Client in the PROTOCOL ITEM TEXT field.
5.  Enter an appropriate identifier in the PROTOCOL IDENTIFIER field. The HL7 INTERFACE SETUP screen displays.
6.  \[Tab\] down to the TYPE field and enter subscriber, then press \[Enter\] to display PAGE 2 OF 2.

HL7 SUBSCRIBER PAGE 2 OF 2

MCAR2 Device Client

-----------------------------------------------------------------------------

RECEIVING APPLICATION: MCAR INST

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?:

LOGICAL LINK: MCAR2 INST

PROCESSING RTN: D ^MDHL7A

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7.  Type MCAR-INST in the RECEIVING APPLICATION field, then enter the following entries:
8.  RESPONSE MESSAGE TYPE = ACK
9.  EVENT TYPE = R01
10. SENDING FACILITY REQUIRED = NO
11. RECEIVING FACILITY REQUIRED = NO
12. LOGICAL LINK = MCAR2 INST (use the appropriate name)
13. PROCESSING RTN = D ^ MDHL7A (use the appropriate routine)

> Note: The processing routine is the MUMPS routine that VistA uses to process the message received from the logical link.

14. \[Tab\] down to the COMMAND prompt, then select Save.
15. At the COMMAND prompt, select Exit.
16. Proceed to the next section to make the new device protocol a subscriber to the device server.

### Activating the Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Next, the links need to be activated. (The steps below assume that the original logical link has never been activated. If MCAR INST is already active, skip to step 4.)

1.  Choose HL Main Menu (HL) \> Filer and Link Management Options (FI) \>Start/Stop Links (SL).
2.  Activate the first logical link: Select HL LOGICAL LINK NODE: MCAR INST
3.  Select B for Background. (B is the default, so just press \[Enter\].
4.  Activate the next logical link: Select HL LOGICAL LINK NODE: (in this example it is MCAR2 INST)
5.  Select B for Background. (B is the default, so just press \[Enter\].
6.  If you have more logical links to activate, repeat steps 4-5.
7.  If you haven’t done this already, use the CP Manager application to configure the device you are using. Refer to [Editing an Automated Instrument](#editing-an-automated-instrument), p. 6-3.
8.  Proceed to the next section to make the new device protocol a subscriber to the device server.

### Adding a Device Client as a Server Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Next you have to make the newly-created protocols subscribers to MCAR DEVICE SERVER. Every client must be a subscriber to a server. That controls the outbound message to a medical device when you reply to it.

Go into MCAR DEVICE SERVER (under the protocol file or using the Interface Developer Option) and make sure that the new MCAR2 DEVICE CLIENT is a subscriber to it. Detailed steps follow:

1.  At the Select Systems Manager Menu, select HL for the HL7 Main Menu.
2.  At the Select HL7 Main Menu, select IN for Interface Developer Options.
3.  At Select Interface Developer Options, select EP for Protocol Edit.
4.  At the Select PROTOCOL NAME prompt, select MCAR Device Server. (If your site uses a different server name, select the appropriate name. You can display a list of available options, if necessary.)
5.  Press \[Enter\] at the TYPE prompt to go to PAGE 2 OF 2: the HL7 EVENT DRIVER screen. (Example follows.)

HL7 EVENT DRIVER PAGE 2 OF 2

MCAR Device Server

-----------------------------------------------------------------------------

SENDING APPLICATION: INST-MCAR

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

MESSAGE STRUCTURE:

PROCESSING ID: P VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

MCAR Device Client

MCAR Device Client2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.  To add the new protocol as a subscriber, \[Down Arrow\] or \[Tab\] down to the line below MCAR Device Client and enter the name of the new subscriber (e.g., MCAR2 Device Client). The HL7 screen displays.
7.  Verify that the entries are correct, then \[Down Arrow\] down to the COMMAND line and select Close. You return to the MCAR Device Server screen.
8.  Repeat steps 6-7 if you need to add more subscribers.
9.  \[Down Arrow\] down to the COMMAND line and select Save.
10. In the COMMAND line, select Exit.

## [^37]Using Port 5000

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Port 5000 is a Multi-Port Listener. The only reason to use the multiport listener is if your inbound port doesn’t work correctly because Cache is not handling ports correctly.

If Cache is handling ports correctly, then you should let Cache handle them. Use the individually shared ports for your devices rather than using the Multi-Port Listener.

If you’re at a facility that has listener problems under Cache, then use port 5000. Port 5000 is handled by VMS, not Cache.

Most sites allocate 25 ports to port 5000, but more can be allocated, if necessary.

### Benefits of Using a Single Port Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single port is easier to monitor and debug. It’s easy to determine if the problem is caused by the link or something else.

If you set up another Multi-Port Listener, you have to set it up in VMS. You’ll have to do that through UCX, which is a lot of work and beyond the scope of this document,

### Setting Up Port 5000

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Edit MCAR DEVICE CLIENT so the logical link points to VAxxx (where xxx is an abbreviation for the hospital).
2.  Make sure all CP Medical devices send to port 5000.
3.  You don’t need to set up an additional MCAR INST (logical link) because you’re using an existing logical link which is VAxxx, where xxx is an abbreviation for the hospital (e.g., VAHIN for Hines).
4.  Make it an MCAR DEVICE server subscriber.

## File Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parameter settings for the HL7 Application Parameter file, HL Logical Link file, and the Protocol file are automatically set during the CP installation. They are listed here for reference. Fields that have bolded field names and bolded field entries must be set exactly as they appear in these examples.

- HL7 Application Parameter (#771) file

This file contains a list of VistA applications that are capable of sending and receiving HL7 transmissions.

NAME: MCAR-INSTACTIVE/INACTIVE: ACTIVEFACILITY NAME: VISTAMAIL GROUP: POSTMASTERCOUNTRY CODE: USHL7 ENCODING CHARACTERS: ^~\\HL7 FIELD SEPARATOR: \|

NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVECOUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\HL7 FIELD SEPARATOR: \|

- HL Logical Link (#870) file

This file stores parameters that govern the behavior of the Logical Links and also stores information that drives the SYSTEMS LINK MONITOR display option.

NODE: MCAR INST LLP TYPE: TCP

QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

TCP/IP PORT: 1026 TCP/IP SERVICE TYPE: SINGLE LISTENERPERSISTENT: NO

MCAR OUT provides an example of field entries for bi-directional instruments for outbound links to medical devices. The fields that have bolded field names and bolded field entries must be set exactly as they appear in this example. The other bolded fields must be edited to match your device specific requirements. For example, Device Type must be Non-Persistent Client. Non-bolded fields may not have a value depending on the state of the system.

NODE: MCAR OUT LLP TYPE: TCPDEVICE TYPE: Non-Persistent Client STATE: Shutdown

AUTOSTART: Enabled TIME STOPPED: JAN 16, 2003@14:30:15

SHUTDOWN LLP ?: YESEXCEED RE-TRANSMIT ACTION: ignoreRE-TRANSMISSION ATTEMPTS: 3TCP/IP PORT: 1028

ACK TIMEOUT: 60PERSISTENT: NOTCP/IP ADDRESS: 10.3.17.202 STARTUP NODE: DEV:ISC4A2

TCP/IP SERVICE TYPE: CLIENT (SENDER)Note: When you need to create additional HL7 links for new devices, name the link in the following format:

> \- If you need to create more than one inbound link (MCAR INST), name the new links “MCAR”, followed by a number (1,2,3), a space, and then “INST”.

> Example: MCAR2 INST

> \- Name outbound links “MCAR”, followed by a number (1,2,3), a space, and then a name for the device.

> Example: MCAR2 SMC

> See “Configuration Instructions Information” for information on setting the TCP/IP address and port and the Startup Mode.

- Protocol (#101) file:

This file contains the protocols for processing HL7 messages.

NAME: MCAR Device ClientITEM TEXT: Instrument Device ClientTYPE: subscriber CREATOR: CPUSER, FIVE

PACKAGE: MEDICINE

DESCRIPTION: Subscriber protocol for sending data to VISTA from clinical

instruments.

TIMESTAMP: 57540,31165 RECEIVING APPLICATION: MCAR INSTTRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01PROCESSING ID: P LOGICAL LINK: MCAR INST\* VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACKPROCESSING ROUTINE: D ^MDHL7A SENDING FACILITY REQUIRED?: NORECEIVING FACILITY REQUIRED?: NO

NAME: MCAR Device ServerITEM TEXT: Instrument HL7 Event DriverTYPE: event driver CREATOR: CPUSER, FIVE

PACKAGE: MEDICINE

DESCRIPTION: This protocol is used by the HL7 package to send results to

VISTA from various clinical instrumentation.

TIMESTAMP: 57631,55707 SENDING APPLICATION: INST-MCARTRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01PROCESSING ID: P \* VERSION ID: 2.3SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NOSUBSCRIBERS: MCAR Device Client

NAME: MCAR ORM CLIENTTYPE: subscriber

CREATOR: CPUSER, SIX RECEIVING APPLICATION: INST-MCAREVENT TYPE: O02 RESPONSE MESSAGE TYPE: ORRSENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NOSECURITY REQUIRED?: NO ROUTING LOGIC: Q

NAME: MCAR ORM SERVERITEM TEXT: Clinical Procedures ORM Protocol ServerTYPE: event driver CREATOR: CPUSER, SIX

TIMESTAMP: 59276,54156 SENDING APPLICATION: MCAR-INSTTRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01VERSION ID: 2.3SUBSCRIBERS: MCAR ORM CLIENT\*Note: Check vendor documentation for instructions on verifying the Version ID.

## Technical Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For all sites:

> To avoid error messages because of a missing or invalid 'Event Protocol', 'Invalid Processing Code', or 'Invalid Application Code', make sure that all settings (except TCP/IP PORT and TCP/IP ADDRESS, in the HL Logical Link (#870) file, which are site specific) are the same as the file settings listed previously in this chapter.

Be sure that the VERSION ID parameters in the Protocol (#101) file are set to the same HL7 Version that is being sent by the vendor instrument. The ITEM and SUBSCRIBERS fields in the Device Server entry in the Protocol (#101) file MUST be the same as the Device Client name.

# Configuring the Automated Instrument Share Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP uses VistA Imaging as the main storage facility for the images and documents that come from a medical device. After one or more medical devices have been installed at the facility, you need to complete the setup. The vendor can provide you with the directory that is used to store the images and documents. You need to make that directory viewable to the VistA Imaging background processor, which will allow VistA Imaging to retrieve the document and store it on the VistA jukebox.

Here is a list of information you need to ensure that the share folder is set up correctly:

- Directory name that holds the documents and images on the medical device. Be sure to get the directory name from the vendor when the device is installed.
- VistA Imaging User (IU) and VistA Imaging Administrator (IA) accounts that are used when starting up the VistA Imaging background processor. You can get these names from the VistA Imaging coordinator at your facility.
- The medical device and the Imaging background processor *must* be on the same Windows domain.
- The medical device must have the same TCP/IP subnet mask as the Imaging background processor.
- You need administration privileges to complete the setup.
- You need to make the directory viewable on the medical device that has the documents and images.
- The network path to the results folder cannot contain symbols, such as dollar signs (\$).

Example: Setting up an automated instrument share folder:

This example describes how to share a Windows 2000 directory for the Widget EKG automated instrument where the medical device (Widget EKG) and the Imaging background processor are on the same domain VHAExample and subnet 255.255.240.0.

The directory that has the documents and images is C:\widget\doc. The VistA Imaging user is VHAISHIU and has an administrator logon to Windows.

1.  Using Windows Explorer, go to the parent directory of the folder that contains the folder to be shared (doc folder) (Figure 13‑1).

![](clinical-procedures-version-1-implementation-guide/045.png)

Figure 13‑1

2.  Right-click the doc folder. Select Sharing from the drop-down menu. The Sharing tab on the doc properties dialog box is displayed, Figure 13‑2.

![](clinical-procedures-version-1-implementation-guide/046.png)

Figure 13‑2

3.  Click Share this folder.
4.  Click Permissions.

![](clinical-procedures-version-1-implementation-guide/047.png)

Figure 13‑3

5.  Select Everyone, and then click Remove. (Figure 13‑3).
6.  Click Add. The Select Users, Computers, or Groups window is displayed.

![](clinical-procedures-version-1-implementation-guide/048.png)

Figure 13‑4

7.  Enter the name of the VistA Imaging (VHAISHIU) User (IU) into the bottom window and click Check Names. A line is displayed under the name if it is valid. Click OK to add the user (Figure 13‑4). The Select Users, Computers, or Groups window closes and VHAISHIU is displayed in the Permissions dialog box.

![](clinical-procedures-version-1-implementation-guide/049.png)

Figure 13‑5

8.  Make sure the check boxes are selected in the “Allow” column for “Full Control”, “Change” and “Read” (Figure 13‑5).
9.  Click Apply and then click OK. A hand displays under the file, which means that the file is now accessible to the VistA Imaging user.
10. To test that the shared folder is set up correctly, have the VistA Imaging coordinator logon as VHAISHIU on a different PC. Check that the shared folder is viewable.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here are frequently encountered errors and resolutions that can occur while running Clinical Procedures. To resolve most of these errors, you need access to CP Manager and CP User.

1\. You tried to launch a CP application and received the following error:

![](clinical-procedures-version-1-implementation-guide/050.png)

Figure 14‑1

1.  Highlight the CP application icon on your desktop. (When CP in installed, shortcuts for the applications are created on the desktop.)
2.  Right-click, and then click Properties.
3.  Enter the command line switch “/nonsharedbroker” in the Target field.
4.  Press OK.

    You can also add the “/nonsharedbroker” switch to the applications in Start \> Programs \> Clinical Procedures.

2\. If you receive the following error:

![](clinical-procedures-version-1-implementation-guide/051.png)

Figure 14‑2

You need the MD GUI USER option to access CP User and the MD GUI MANAGER option to access CP Manager. Call IRM.

3\. During a CP Study Check-In, a procedure request was ordered but is not listed.

1.  The GRMC procedure has not been linked to a CP procedure. You need to cancel the procedure request, and then use the following Procedure Setup option to link the GMRC procedure to the CP procedure.

> Select OPTION NAME: GMRC MGR Consult Management

> Select Consult Management Option: PR Setup procedures

> Select Procedure:CPEKG 12LEAD STAT

> NAME: CP EKG 12 LEAD STAT// \<RET\>

> INACTIVE: NO// \<RET\>

> Select SYNONYM: EKG// \<RET\>

> INTERNAL NAME: \<RET\>

> Select RELATED SERVICES: CP CARDIOLOGY// \<RET\>

> TYPE OF PROCEDURE: ECG// \<RET\>

> CLINICAL PROCEDURE: EKG, ROUTINE (12 LEADS)// \<RET\>

> If you entered “?” in the Clinical Procedure field and you do not find a procedure that you want, use CP Manager to define and activate the CP procedures.

2.  Open CP Manager.
3.  Enter the name of the CP Procedure in the Procedure Name field. See [Setting Up Clinical Procedures](#section-2), p. [6-1](#section-2).
4.  Re-order the consult procedure.

4\. Allowable Instruments are associated with the CP procedure but you cannot see the instruments during Study Check-In.

1.  Open CP Manager.
2.  Expand the Procedures folder, and then select the procedure.
3.  In the Allowable Instruments list, select the check box for the specific instrument.

5\. After a study is checked-in, you can’t find the study entry in CP User.

1.  Open CP Manager.
4.  Expand the Procedures folder, and then select the procedure.
2.  Check that a treating specialty has been assigned.

![](clinical-procedures-version-1-implementation-guide/052.png)

[^38]Figure 14‑3

6\. An error status is displayed for the study and the Update Study Status selection is unavailable. You must have the MD GUI MANAGER key, and then you can go to File \> Update Study Status to review the problem.  
  
The message in the following figure indicates that a Notification Mailgroup has not been assigned or the Medical Device is not Active.

![](clinical-procedures-version-1-implementation-guide/053.png)

Figure 14‑4

1.  Open CP Manager.
2.  Select the instrument.
3.  Check that the Notification Mail Group has an entry and that the Active checkbox is selected.
4.  Open CP User. Choose File \> Update Study Status.
5.  If the device is bi-directional, delete the study that was checked in and check-in a new study with the same procedure request to get the HL7 message transmitted to the medical device. If the device is uni-directional, check the Ready to Complete status, and click OK.

7\. If a study remains in Pending Instrument Data status and it is a bi-directional medical device, check to see if Auto Submit To VistA Imaging field is selected. .

1)  Open CP Manager.
2)  Expand the Procedures folder, and then select the procedure
3)  Check that Auto Submit to VistA Imaging is selected.

For the current study, you still need to manually submit the result. For future studies, the result will be automatically submitted.

8\. The following two errors indicate that a TIU document Title has not been assigned to the CP procedure. The first error message is from CP during image submission if a TIU document has not been assigned to the CP Definition.

![](clinical-procedures-version-1-implementation-guide/054.png)

Figure 14‑5

This second error screen is the Update Study Status screen from CP User. The first message is a CP warning. The second message is a warning from TIU that there is no TIU document.

![](clinical-procedures-version-1-implementation-guide/055.png)

Figure 14‑6

1.  Open CP Manager
2.  Select the procedure, and check that a TIU Note Title is assigned.
3.  Open CP User and Update the Study Status to Ready to Complete.
4.  Open the study and manually submit the results. By manually submitting the result, you prevent any re-occurrences of the error.

9\. These errors indicate that a Hospital Location has not been defined for the CP procedure.

![](clinical-procedures-version-1-implementation-guide/056.png)

Figure 14‑7

![](clinical-procedures-version-1-implementation-guide/057.png)

Figure 14‑8

1)  Open CP Manager and check that the Hospital Location has been defined.
2)  Open CP User and Update the Study Status to Ready to Complete.
3)  Open the study and submit it manually.

10\. If the Complete/Update Result option in CPRS \> Action \> Consults Results is unavailable, you need to be updated as the Interpreter. Use the Service User Management \> SERVICE INDIVIDUAL TO NOTIFY option to assign the Interpreter role.

Select Consult Management Option: SU Service User Management

Select Service/Specialty: GASTROENTEROLOGY

Select UPDATE USERS W/O NOTIFICATIONS: CPUSER, SEVEN

//

Select UPDATE USERS W/O NOTIFICATIONS:

Select ADMINISTRATIVE UPDATE USER: CPUSER, EIGHT

//

Select ADMINISTRATIVE UPDATE USER:

SERVICE INDIVIDUAL TO NOTIFY: CPUSER, NINE CD 123 IRM FIELD OFFICE IRM FIELD OFFICE

PROGRAMMER

Select SERVICE TEAM TO NOTIFY: consultteam//

Select NOTIFICATION BY PT LOCATION:

Select Service/Specialty:

11\. If you get the following error message:

![](clinical-procedures-version-1-implementation-guide/058.png)

Figure 14‑9

Make sure that the Imaging Background Processor can access the Network Share, where the result resides.

1)  Open CP Manager.
2)  Click Clinical Procedures.
3)  Click System Parameters.
4)  Check the path of the Imaging Network Share. (The Imaging Network Share must be a shared directory that can be accessed by the Imaging Background Processor and CP Gateway.)

12\. If a study remains in “Submitted” status, check the Imaging Background Processor log for errors and make sure that the “Import” checkbox is checked for the Import BP parameter.  
  
From the Background Processor, choose Edit \> BP Workstation Parameters. (You may need to find someone who is responsible for the Imaging Background Processor application.)

13\. If the Interpreter does not receive an alert that the procedure is ready for interpretation, check if the CONSULT/PROC INTERPRETATION notification is enabled and if the user has the Interpreter role.

1)  You must enable the CONSULT/PROC INTERPRETATION notification if you want to receive the “Ready for interpretation” alert in CPRS. You can enable the alert for one user, several users, or for the entire service. Use the Notification Management Menu.
2)  To assign the interpreter role, use the Consult Management menu. If user wants to receive alerts, do not enter them into the Update Users W/O Notifications field. This field is for users who want the role of interpreter but do not want to receive alerts. Refer to [Setting Up Consult Services](#step-1-setting-up-consult-services), p. [9-1](#step-1-setting-up-consult-services).

Select Consult Management Option: SU Service User Management

Select Service/Specialty: GASTROENTEROLOGY

Select UPDATE USERS W/O NOTIFICATIONS: CPUSER, SEVEN

//

Select UPDATE USERS W/O NOTIFICATIONS:

Select ADMINISTRATIVE UPDATE USER: CPUSER, EIGHT

//

Select ADMINISTRATIVE UPDATE USER:

SERVICE INDIVIDUAL TO NOTIFY: CPUSER, NINE CD 123 IRM FIELD OFFICE IRM FIELD OFFICE

PROGRAMMER

Select SERVICE TEAM TO NOTIFY: consultteam//

Select NOTIFICATION BY PT LOCATION:

14\. If you receive the following error while trying to interpret a procedure:

![](clinical-procedures-version-1-implementation-guide/059.png)

Figure 14‑10

> This message can occur if business rules have not been set up or if insufficient business rules have been set up for this document title.

> To add a business rule:

1)  Go into the User Class Management Menu.
2)  Select Manage Business Rules.
3)  Enter specific words at the appropriate prompts (Status, Action, User Class). These words are combined to make a business rule.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
Action A functional process that a clinician uses in a computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.
ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.
Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.
Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version.
Attachments Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:
> .txt Text files
> .rtf Rich text files
> .jpg JPEG Images
> .jpeg JPEG Images
> .bmp Bitmap Images
> .tiff TIFF Graphics (group 3 and group 4 compressed and uncompressed types)
> .pdf Portable Document Format
> .html Hypertext Markup Language
> .DOC (Microsoft Word files) are not supported. Be sure to convert .doc files to .rtf or to .pdf format.
Automatic Version Updates Updating an account with new software versions without user intervention.
Background Processing Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.
Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
Boilerplate Text A pre-defined TIU template that can be filled in for titles to speed up the entry process. TIU exports several titles with boilerplate text, which can be modified to meet specific needs; sites can also create their own.
Browse Lookup the file folder for a file that you would like to select and attach to the study. Such as clicking the “...” button to start a lookup.
Bulletin A canned message that is automatically sent by mail to a user when something happens to the database.
Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).
Class Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
Contingency Plan A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
CP Clinical Procedures.
CP Study A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.
CPRS Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, and reports (including health summaries).
Device A hardware input/output component of a computer system, such as CRT, printer.
Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.
Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.
Edit Used to change/modify data typically stored in a file.
Field A data element in a file.
File The M construct in which data is stored for retrieval at a later time. A computer record of related information.
File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.
File Server A machine where shared software is stored.
Gateway The software that performs background processing for Clinical Procedures.
GUI Graphical User Interface – a Windows interface that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that make a computer program, easier to use and that allows multi-processing (more than one window or process available at once).
Interpreter Interpreter is a user role exported with USR\*1\*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the findings or results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.
IRMS Information Resource Management Service.
Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all VistA applications.
Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
Modality Another name for a medical instrument.
Module A component of a software application that covers a single topic or a small section of a broad topic.
Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.
Network Server Share A machine that is located on the network where shared files are stored.
Notebook This term refers to a GUI screen containing several tabs or pages.
Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.
Package Otherwise known as an application.
Page This term refers to a tab on a GUI screen or notebook.
Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
PersistentConnection A connection that is established by the medical device and is kept connected to VistA even after the device has transmitted it HL7 message.
Non-persistentConnection A connection that is established by the medical device to VistA and is disconnected once the HL7 message has been sent.
Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.
Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.
Security Key A function which unlocks specific options and makes them accessible to an authorized user.
Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
Software A generic term referring to a related set of computer programs.
Status Symbols Codes used in order entry and Consults displays to designate the status of the order.
Study See CP Study.
Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
Title Titles are definitions for documents. They store the behavior of the documents which use them.
TIU Text Integration Utilities.
User A person who enters and/or retrieves data in a system.
User Class User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.
User Role User Role identifies the role of the user with respect to the document in question, such as Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc..
Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
VistA Veterans Health Information Systems and Technology Architecture.

# Appendix A – CP Application Startup Options and Command Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics discussed in this chapter are:

- [Introduction](#introduction-1)
- [What is a Command Line Switch?](#what-is-a-command-line-switch)
- [Shared Broker Environment](#shared-broker-environment)
- [CPRS Tools Menu](#cprs-tools-menu)
- [All Command Line Switches](#all-command-line-switches)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Procedures was designed to operate as a standalone client or, when desired, launched from the tools menu of CPRS. CP uses the new Shared Broker environment and is also backwards compatible with previous releases of the RPC Broker. This functionality is achieved through the use of command line switches, which are applied to the Desktop Icons, Start Menu items, or the command assigned to an item on the CPRS tools menu.

## What is a Command Line Switch?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A command line switch is a setting that is included in the call to the executable that controls the behavior of the executable. A common switch setting deployed in the VistA environment specifies the proper server on the proper listener port for the RPC Broker to connect to without user intervention. This is commonly seen when you create a desktop icon for CPRS with the /s=BrokerServer /p=9200 switch. The connection to the VistA server is defined as BrokerServer on listener port 9200. (See the RPC Broker manuals for a complete description of defining a valid connection to pass to applications.)

## ## Shared Broker Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP was developed when the Shared Broker was being implemented. The Shared Broker provides a more responsive workstation environment by eliminating multiple sign-on requirements and preserving VistA server resources by combining several client applications into a single process/connection. CP provides this new functionality.

To assist sites in the migration to Shared Broker, CP is backwards compatible with the previous RPC Broker environment with a simple command line switch in the desktop icon, start menu item, and CPRS Tools Menu items. During the client GUI installation, desktop icons and start menu items are installed using the command line switch, /NonSharedBroker. By appending this command line switch, a call to launch a CP application causes the application to run with the old style broker and does not require that the workstation be upgraded with the latest broker client software.

Example:

\\MyAppServer\CP\CPuser.exe /server=BrokerServer /Port=9200 /NonSharedBroker

In this example, CPUser is executed from the server MyAppServer in share name CP and tries to connect to the VistA server defined as BrokerServer on listener port 9200. In addition, this command causes CPUser to connect to the previous version of the broker instead of the Shared Broker.

## CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you want to use CP User from the CPRS tools menu, you need to launch CP User in a mode that causes it to listen to CPRS for patient changes and to exit when CPRS is closed. When appending the command line switch /cprs to the command in the CPRS Tools Menu command line, CP runs in a slave mode and does not allow patients to be selected within the CP environment. CPRS provides placeholders for the site to utilize when creating command lines for the tools menu. These are:

%srv Holds the name of the server that CPRS is currently connected to.

%port Holds the listener port that CPRS is currently communicating through.

%dfn Holds the DFN of the currently opened patient record in CPRS.

Example command line for CPRS tools menu:

CPUser=\\MyAppServer\CP\CPuser.exe /cprs /server=%s /port=%p /dfn=%d

In this example, the CPUser.exe on server MyAppServer in the Share CP runs as a slave under the CPRS application while connecting to the server that CPRS defined in %s on the listener port defined in %p. In addition, CP User opens the patient defined in %d upon starting.

For instructions on setting up the CPRS Tools menu, refer to, [Adding Clinical Procedures to the CPRS Tools Menu](#add-cp-user-to-the-cprs-tools-menu-orwt-tools-menu), p. [10-6](#add-cp-user-to-the-cprs-tools-menu-orwt-tools-menu)

## All Command Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Procedures V. 1.0 command line parameters available from the command prompt or within Windows shortcut definitions and the CPRS Tools menu commands are defined by application.

CP User.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/cprs\] \[/dfn=*patientdfn*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/brokertimeout=*seconds*\] \[/bypasscrc\] \[/NonSharedBroker\]

CP Manager.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/brokertimeout=*seconds*\] \[/bypasscrc\] \[/NonSharedBroker\]

CP Gateway.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/brokertimeout=*seconds*\] \[/bypasscrc\] \[/NonSharedBroker\]

Switches:

|                  |                                                                                                                                                                                                                           |                                      |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Name             | Description                                                                                                                                                                                                               | Default                              |
| /server          | Specifies a VistA server to which you are connected.                                                                                                                                                                      | BROKERSERVER                         |
| /port            | Specifies an alternate listener port on the selected server.                                                                                                                                                              | 9200                                 |
| /cprs            | Specifies that the application is to run in slave mode under CPRS. This switch must be utilized when adding the CP User application to the CPRS tools menu.                                                           |                                      |
| /dfn             | Specifies the patient dfn (record identifier) to open upon application startup. This switch must be utilized when adding the CP User application to the CPRS tools menu.                                              |                                      |
| /helpdir         | Location of the Clinical Procedures windows help files.                                                                                                                                                                   | *../appdir/help* of the application. |
| /debug           | Sets the debug mode for both the RPC Broker and the Clinical Procedures application.                                                                                                                                      | Off                                  |
| /brokertimeout   | Overrides the timeout for the RPC Broker when executing a Remote Procedure.                                                                                                                                               | 30                                   |
| /bypasscrc       | Overrides the system parameters setting to check an applications crc32 value upon application startup. This switch should only be used during testing to avoid the messages if the site is implementing CRC verification. |                                      |
| /NonSharedBroker | This switch instructs the application to not utilize the shared broker functionality. Used when the Shared Broker has not been implemented on the target workstation.                                                 |                                      |

*servername* IP Address or Name of VistA server as it appears in the client Hosts. file.

Default Hosts. file locations:

NT 4.0 = c:\winnt\system32\drivers\etc\hosts.

Win95/98 = c:\windows\hosts.

*listenerport* TCP Port that the Broker is running on the VistA server.

*helpdirectory* Directory path to a location containing the Clinical Procedures V. 1.0 Help Files.

*seconds* Integer value specifying the number of seconds the RPC Broker waits for a server response to an RPC.

*patientdfn* Value of the patient dfn to access when starting the CP User application.

# Appendix B – Exported Procedures List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These exported procedures are contained in the MDPOST routine. When the INIT^MDPOST routine is run, these entries are added to your CP Definition (#702.01) file:

ABD PARACENTESIS: FOLLOWUP

ABD PARACENTESIS: INITIAL

ABLATION OF AV NODE FUNCTION

AICD INTER/CONDITION

AIRWAY RESISTANCE

ANO BIOPSY

ANO CONTROL BLEEDING

ANO DIAGNOSTIC (BRUSHINGS)

ANO HOT BIOPSY(IES)

ANO SINGLE TUMOR (HOT/BICAP)

ANOSCOPY

ARRHYTHMIA INDUCTION BY PACING

ARTERIAL BLOOD GASES

ARTERIAL CANNULATION

ARTERIAL PUNCTURE

ARTHROC.ASPIR.INJ.INT.JT.BUR

ARTHROC.ASPIR.INJ.MAJ.JT.BUR

ARTHROCENT.ASPIR.INJ.SM.JT.BUR

ASPIRATION

BIOPSY

BIOPSY LUNG, PERCUTANEOUS NDL

BIOPSY, PLEURA

BONE MARROW

BONE MARROW INTERPRETATION

BRONC DIAGNOSTIC W/BAL

BRONC W/BRONC WASHING

BRONC W/TRANSBRONC LUNG BX

BRONCHIAL BRUSH

BRONCHOSCOPY W/BRONCH BIOPSY

BRONCHOSCOPY W/WANG NEEDLE

BRONCHOSCOPY, LASER

BRONCHOSCOPY, STENT PLACEMENT

BRONCHOSCOPY, THERAPEUTIC

BRONCOSCOPY/FB REMOVAL

C&P EXAM

CARDIAC CATHETERIZATION

CARDIAC REHAB W/O ECG MON

CARDIAC REHAB/W ECG MON

CARDIOPULMONARY REHABILITATION

CARDIOVERSION, ELECTIVE

CENTRAL VENOUS CANNULATION

CHEMOTHERAPY

COL ABL (OTHR THAN SNARE/BI)

COL BIOPSY

COL CONTROL HEM.

COL DIAGNOSTIC (BRUSHINGS)

COL HOT BIOPSY(IES)

COL REMOVAL FB

COL SNARE

COLONOSCOPY

COMPREHENSIVE EP EVALUATION

CPAP/BIPAP VENTILATION

DIALYSIS PROCEDURES, HEMO

DIALYSIS TRAINING/COMPLETE

DIFFUSION

DILUTION STUDIES FOR CO MEAS

ECG

ECG (EKG), RHYTHM STRIP

ECG 12 LEAD

ECG 24 HOUR HOLTER MONITOR

ECG MONITORING

ECG WITH INTERPRETATION

ECG, EVENT RECORDER

ECG, RHYTHM TRACING

ECG, SIGNAL AVERAGE

ECHO

ECHO TRANSESOPHOGEAL SINGLE PL

ECHO, 2D M-MODE

ECHO, DOPPLER COLOR FLOW

ECHO, DOPPLER, COMPLETE

ECHO, TRANSESOPHOGEAL

ECHO, TRANSESOPHOGEAL BIPLANE

ECHO, TRANSTHORACIC

EGD

EGD ABL (OTH THAN SNARE/BI)

EGD BAND LIGATION

EGD BIOPSY

EGD DIAGNOSTIC (BRUSHINGS)

EGD DILATION BALLOON

EGD DILATION WIRE

EGD FOREIGN BODY

EGD HOT BIOPSY(IES) / BICAP

EGD INJECTION / SCLEROSIS

EGD SNARE/SINGLE

EGD TUBE/STENT

EKG, ROUTINE (12 LEADS)

ENDO OF BOWEL POUCH W/ BIOPSY

ENDOMYOCARDIAL BIOPSY

ENDOSCOPIC ULTRASOUND

ENDOSCOPIC ULTRASOUND, BIOPSY

ENDOSCOPY OF BOWEL POUCH

ENDOTRACHEAL INTUBATION

ENTEROSCOPY

EP EVAL OF CARDIO/DEFIB LEADS

EP EVAL OF CARDIOVERTER/DEFIB

EP EVAL W/ ARRHYTHMIA INDUCT

EP EVAL W/ L ATRIAL RECORD

EP EVAL W/ L VENTRIC RECORD

EP FOLLOWUP STUDY W/PACING

EP STUDY

EPICARDIAL/ENDOCARDIAL MAPPING

ERCP

ERCP ABL (OTHR THAN SN/BI)

ERCP BALLOON DILATION

ERCP BIOPSY

ERCP DEST STONES

ERCP DIAGNOSTIC (BRUSHINGS)

ERCP DRAIN, TUBE

ERCP INSERTION OF TUBE/STENT

ERCP PRESSURE OF ODDI

ERCP REM STONES

ERCP RMV FB OR CHG OF TUBE

ERCP SPHINCTEROTOMY

ES ABLATION (OTHER)

ES BAND LIGATION

ES BIOPSY

ES CONTROL BLEEDING

ES DIAGNOSTIC ENDO (BRUSHINGS)

ES DILATION (BALLOON)

ES DILATION (WIRE)

ES HOT BIOPSY(IES)

ES INJECTION / SCLEROSIS

ES INSERTION TUBE/STENT

ES REMOVAL FB

ES SNARE

ESOPHAGEAL DILATION

ESOPHAGEAL MOTILITY STUDY

ESOPHAGEAL RECORDING

ESOPHAGUS

ETT

ETT W/ O2 CONSUMPTION

ETT W/ THALLIUM SCAN

EXAM,SYNOVIAL FLUID CRYSTALS

EXCERCISE CHALLENGE

FINE NEEDLE ASPIRATION

FLEX SIG

FLOW VOLUME LOOP

FLX ABLATION (OTHER)

FLX BIOPSY

FLX CONTROL HEM.

FLX DECOMPRESS VOLVULUS

FLX DIAGNOSTIC (BRUSHINGS)

FLX HOT BIOPSY(IES)

FLX REMOVAL FB

FLX SNARE

FRC

FT CHANGE OF G TUBE

FT EGD FOR PEG PLACEMENT

FT PERC PLACEMENT OF G TUBE

FT REPOS TUBE THRU DUODENUM

FT SM INT ENDO CONV G-J TUBE

FT SM INT ENDO J TUBE PLACE

HEART RATE VAR. ANALYSIS

HEMODIALYSIS, ONE EVAL

HEMODIALYSIS, REPEATED EVAL.

HOLTER

I & D /DEBRIDEMENT

ICD IMPLANTATION

ICD INTERROGATION

ILEOSCOPY THROUGH STOMA

ILEOSCOPY W/ BIOPSY

INFUSION 1-8 HRS.

INFUSION TO 1 HR.

INJ FOR ANGIOGRAPHY

INJ FOR AV BYPASS GRAFTS

INJ TENDON/LIGAMENT/CYST

INJECTION, CARDIAC CATH

INTRA-ATRIAL PACING

INTRA-ATRIAL RECORDING

INTRAVENTRICULAR PACING

INTRODUCTION OF NEEDLE/CATH

IV FLUID THERAPY

IV INFUSION

IV PUSH

IV THER. 1-8 HRS.

IV THER. UP TO 1 HR.

LASER SURGERY (NOT YAG)

LEFT HEART CATHETERIZATIION

LEFT VENTRICULAR RECORDING

LIVER BIOPSY

LUNG COMPLIANCE

MECHANICAL VENTILATION

METHACHOLINE CHALLENGE

MONITOR W/ REVIEW & REPORT

OVER GUIDE WIRE

PACEMAKE IMPLANTATION

PACEMAKER

PACEMAKER FOLLOW UP

PACEMAKER, RHYTHM STRIP

PARACENTESIS

PERIPH BLOOD SMEAR INTERPRET

PHLEBOTOMY

PLACE CATHETER IN VEIN, HEMO

PLEURODESIS

PNEU BALLOON (30MM+) ACHALASIA

PROC ABLATION (OTHER)

PROC BIOPSY

PROC CONTROL BLEEDING

PROC DIAGNOSTIC (BRUSHINGS)

PROC DILATION

PROC HOT BIOPSY(IES)

PROC REMOVAL FB

PROC SNARE

PROC TUMORS, MULT (HOT/SN/BI)

PROCTOSCOPY

PROGRAMMED STIMULATION/PACING

PSEUDOFOLLICULAR SCAN

PULMONARY ARTERY CATHETER

PULMONARY FUNCTION INTERPRET

PULMONARY PROCEDURES

PULSE OXIMETRY MULTIPLE REHAB

PULSE OXIMETRY SINGLE REHAB

PULSE OXIMETRY, MULTIPLE

RHEUMATOLOGY PROCEDURES

RIGHT HEART CATHETERIZATION

RIGHT VENTRICULAR RECORDING

RT & LT HEART CATHETERS

SB ENDO W/ABLATION

SB ENDO W/BLEEDING CONTROL

SB ENDO W/FB REMOVAL

SB ENDO W/HOT BIOPSIES

SB ENDO W/INCL ILEUM

SB ENDO W/INCL ILEUM,BIOPSY

SB ENDO W/INCL ILEUM,BLD CONT

SB ENDO W/TUMORS (SNARE)

SCREENING, MAMMOGRAM

SCREENS AND INJ, ANTI-COAG

SLOW VITAL CAPACITY

SMALL BOWEL ENDOSCOPY

SMALL BOWEL ENDOSCOPY,BIOPSY

SOUND/BOUGIE;SINGLE/MULT

SPIROMETRY

SPIROMETRY, PRE & POST

STO ABLATION

STO BIOPSY

STO CONTROL HEM.

STO DIAG/BRUSHING

STO FOREIGN BODY

STO HOT BIOPSY(IES)

STO SNARE

STOMA

STRESS TEST, ECHO IMAGING

STRESS TEST, EXER (NON-IMAGE)

STRESS TEST, NUCLEAR IMAGING

SUBCUT./IM

SYMPTOM LIMITED EXERCISE TEST

THORACENTESIS

THORACIC GAS VOLUME

THORACOSTOMY

THRESHOLD TEST (DUAL)

THRESHOLD TEST (SGL)

TILT TABLE TEST FOR SYNCOPE

TRANS. BLOOD

TRANS. INDWELL. VEN. ACC. CARE

TRANS. THERAPEUTIC APHERESIS

TRANSFUSION

VENIPUNCTURE (ROUTINE), HEMO

# Appendix C - Instrument Processing Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of the processing routines associated with each instrument.

|                                |                         |
|--------------------------------|-------------------------|
| Instrument Name:           | Processing Routine: |
| CLINIVISION                    | MDHL7R1                 |
| [^39]BRAUN                     | MDHL7D                  |
| BRAUN (Bi-Directional)         | MDHL7D                  |
| FRESENIUS                      | MDHL7D                  |
| FRESENIUS (Bi-Directional)     | MDHL7D                  |
| GAMBRO_EXALIS                  | MDHL7D                  |
| GAMBRO_EXALIS (Bi-Directional) | MDHL7D                  |
| Muse                           | MDHL7M1                 |
| Muse EKG                       | MDHL7M1                 |
| Muse Exercise                  | MDHL7M1                 |
| Muse Holter                    | MDHL7M1                 |
| Muse Pacemaker EKG             | MDHL7M1                 |
| OLYMPUS                        | MDHL7E                  |
| OLYMPUS Bronchoscopy           | MDHL7E                  |
| OLYMPUS Colonoscopy            | MDHL7E                  |
| OLYMPUS EGD                    | MDHL7E                  |
| OLYMPUS EGDPEG                 | MDHL7E                  |
| OLYMPUS ERCP                   | MDHL7E                  |
| OLYMPUS Endo Ultrasound        | MDHL7E                  |
| OLYMPUS Enteroscopy            | MDHL7E                  |
| OLYMPUS Liver Biopsy           | MDHL7E                  |
| OLYMPUS Paracentesis           | MDHL7E                  |
| OLYMPUS Sigmoidoscopy          | MDHL7E                  |
| SMC                            | MDHL7P1                 |

# [^40]Appendix D – Exported Values For Hemodialysis Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Custom Data List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Anticoagulants

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

1 Heparin

2 Citrate

3 Saline Flush

4 None

5 Warfarin

### Code Statuses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 DNR

02 AD Signed

03 Full Resuscitation

04 DNI

### Dialyzer List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 400-HG

02 500-HG

03 50H

04 50M

05 50U

06 600-HE

07 65H

08 65U

09 700-HE

10 75U

11 90U

12 Alwall GFE-09

13 Alwall GFE-11

14 Alwall GFE-12

15 Alwall GFE-15

16 Alwall GFE-18

17 Alwall GFS Plus 11

18 Alwall GFS Plus 12

19 Alwall GFS Plus 16

20 Alwall GFS Plus 20

21 Alwall GFS-12

22 Alwall GFS-16

23 B3-0.8-A

24 B3-1.0-A

25 B3-1.0-A

26 B3-1.6-A

27 B3-2.0-A

28 BK-1.6-U

29 BK-2.1-U

30 C-061

31 C-081

32 C-101

33 C-121

34 C-151

35 CA-110

36 CA-150

37 CA-170

38 CA-210

39 CA-50

40 CA-70

41 CA-90

42 CAHP/DICEA 110G

43 CAHP/DICEA 150G

44 CAHP/DICEA 210G

45 CAHP/DICEA 90G

46 CF-12 (ST-12)

47 CF-15 (ST-15)

48 CF-23 (ST-23)

49 CF-25 (ST-25)

50 CT-110G

51 CT-190G

52 F5

53 F-50

54 F6

55 F-60

56 F-60-M

57 F8

58 F-80

59 F-80-M

60 Filtral 20

61 Lundia Alpha 400

62 Lundia Alpha 500

63 Lundia Alpha 600

64 Lundia Alpha 700

65 Lundia Aria 550

66 Lundia Aria 700

67 Lundia Pro 500

68 Lundia Pro 600

69 Lundia Pro 800

70 M-081

71 M-101

72 M-121

73 M-151

74 Optiflux 200r

75 Polyflux 11S

76 Polyflux 14S

77 Polyflux 17S

78 Polyflux 21S

79 Polyflux 210H

80 PSN120

81 PSN-150

82 PSN-170

83 PSN-210

84 T-150

85 T-175

86 T-220

87 Tricea 110G

88 Tricea 150G

89 Tricea 190G

90 Tricea 210G

### Education Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 One

### ESRD Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 585

02 403.01

03 403.11

04 403.91

05 25000 A Type II, adult-onset type or unspecified type diabetes

06 25001 A Type I, juvenile type, ketosis prone diabetes

07 5829 A Glomerulonephritis (GN)(histologically not examined)

08 5821 A Focal glomerulosclerosis, focal sclerosing GN

09 5831 A Membranous nephropathy

10 5832 A Membranoproliferative GN type 1. diffuse MPGN

11 5832 C Dense deposit disease, MPGN type 2

12 58381 B IgA nephropathy, Berger's Disease (proven by immunofluorescence)

13 58381 C IgM nephropathy (proven by immunofluorescence)

14 5804 B Rapidly progressive GN

15 5834 C Goodpasture's Syndrome

16 5800 C Post infectious GN, SBE

17 5820 A Other proliferative GN

18 7100 E Lupus erythematosus, (SLE nephritis)

19 2870 A Henoch-Schonlein syndrome

20 7101 B Scleroderma

21 2831 A Hemolytic uremic syndrome

22 4460 C Polateritis

23 4464 B Wegener's granulomatosis

24 5839 C Nephropathy due to heroin abuse and related drugs

25 4462 A Vasculitis and its derivatives

26 5839 B Secondary GN, other

27 9659 A Analgesic abuse

28 5830 B Radiation nephritis

29 9849 A Lead nephropathy

30 5909 A Nephropathy caused by other agents

31 27410 A Gouty nephropathy

32 5920 C Nephrolithlasis

33 5996 A Acquired obstructive uropathy

34 5900 A Chronic pyelonephritis, reflux nephropathy

35 58389 B Chronic intersitial nephritis

36 58089 A Acute interstitial nephritis

37 5929 B Urolithiasis

38 2754 A Nephrocalcinosis

39 4039 D Renal disease due to hypertension (no primary renal disease)

40 4401 A Renal artery stenosis

41 59381 B Renal artery occlusion

42 59381 E Cholesterol emboli, renal emboli

43 75313 A Polycystic kidneys, adult type (dominant)

44 75314 A Polycystic, infantile (recessive) 7

45 75316 A Medullary cystic disease, including nephronophthisis

46 7595 A Tubular sclerosis

47 7598 A Hereditary nephritis, Alport's syndrome

48 2700 A Cystinosis

49 2718 B Primary oxalosis

50 2727 A Fabry's disease

51 7533 A Congenital nephrotic syndrome

52 5839 D Drash syndrome, mesangial sclerosis

53 7532 A Congenital obstructive uropathy

54 7530 B Renal hypoplasia, dysplasia, oligonephronia

55 7567 A Prune belly syndrome

56 7598 B Hereditary/familial nephropathy

57 1890 B Renal tumor (malignant)

58 1899 A Urinary tract tumor (malignant)

59 2230 A Renal tumor (benign)

60 2239 A Urinary tract tumor (benign)

61 2395 A Renal tumor (unspecified)

62 2395 B Urinary tract tumor (unspecified)

63 20280 A Lymphoma of kidneys

64 2030 A multiple myeloma

65 2030 B Light chain nephropathy

66 2773 A Amyloidosis

67 99680 A Complication post bone marrow or other transplant

68 28260 A Sickle cell disease/anemia

69 28269 A Sickle cell trait and other sickle cell (HbS/Hb other)

70 64620 A Postpartum renal failure

71 0429 A AIDS nephropathy

72 8660 A Traumatic or surgical loss of kidney(s)

73 5724 A Hepatorenal syndrome

74 5836 A Tubular necrosis (no recovery)

75 59389 A Other renal disorders

76 7999 A Etiology uncertain

### Medication Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 ID

02 IN

03 IV

04 IVP

05 PO

06 SL

07 SQ

### Medication Units

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 ml

02 mg

03 units

04 mcg

05 oz

06 gal

07 gr

08 Gm

09 Kg

10 lb

11 pt

12 in

13 qt

14 liter

15 Tsp

16 Tbsp

17 mEq

### Modalities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 HD

02 Inpatient HD

03 Short Intermittent HD

04 Nocturnal HD

05 ICU HD

06 Outpatient HD

07 Home HD

### TIU Note Titles 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

01 Site Specific TIU Note Title

### Transportation Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Item</u> <u>Value</u>

1 ambulatory

2 bed

3 motorized w/c

4 wheel chair

5 stretcher

## Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The system preferences are exported with the following default values:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allow USER control Study Status = FALSE

Allow USER delete blank F/S records = FALSE

Allow USER Reset Study Status = FALSE

Application Web Page URL = http:// <span class="mark">REDACTED</span>/clinicalspecialties/clinproc/showProject.asp?pid=1

Blanks Placeholder = \<blank\>

Broker Timeout (sec) = 30

Color Disabled = -16777201

Color Editable = -16777211

Color of Background = -16777201

Color of Toolbars = 12632256

Color Read Only = 15793151

Color Read/Write = 12632256

Color Required = -16777192

Color Review = 12632256

Color Unknown = 255

Falls Assessment as Separate TIU Note = TRUE

Flowsheet Refresh Rate (min) = 15

Ignore Unfinished Status = TRUE

Overwrite Manual Input = TRUE

Pain assessment based on how patient tolerates pain = FALSE

Pain Level = 1

Report keyword = TREATMENT REPORT

Reverse Flowsheet Order = TRUE

Save Flowsheet Vitals = FALSE

Save Vitals = FALSE

Set the new study Cover to Read Only = FALSE

Show Additional Reports = TRUE

Show Disabled Studies to Users = FALSE

Show Flowsheet Event Copies = TRUE

Show Infectious Diseases information as Tree = TRUE

Show report signature field = TRUE

Show TIU Note Templates = FALSE

Show Treatment Status Report = TRUE

Study List Refresh Rate (sec) = 60

Study Load Limit = 5

Summary Report Name = Summary Report

## ## Report List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Summary Report Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TREATMENT REPORT for HEMODIALYSIS STUDY \#\<StudyID\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Patient Name: \<PatientName\>

SSN:..........\<PatientSSN\>

DOB:..........\<PatientDOB\>

Age:..........\<PatientAge\>

Sex:..........\<PatientSex\>

Treatment Date:........\<cdsInfo.StudyDate\>

ESRD Diagnosis:........\<Diagnosis\>

Diagnosis Date:........\<DDate\>

Initial Therapy Date:..\<InitialTDate\>

Modality:..............\<Modality\>

Code Status:...........\<CodeStatus\>

Attending Nephrologist:\<Attending Nephrologi\>

Schedule:..............\<SCHEDULE\>

Transplant Candidate...\<cdsSummary.TransCand\>

Work in Progress.....\<cdsSummary.TransWIP\>

Referred to TC.......\<cdsSummary.TransReff\>

Station#: \<Station\>

Machine#: \<Machine\>

TREATMENT SUMMARY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Treatment Start Time:..\<Treatment Start Time\>

Treatment End Time:....\<Treatment End Time\>

Treatment Duration:....\<Treatment Duration\> (instrument data)

Duration Adjusted:....\<Treatment Duration M\> (manual input)

Total UF:..............\<Summary Total UF\> Total LP:..........\<Summary Total LP\>

Mean UFR:..............\<Summary Mean UFR\> Mean TMP:..........\<Summary Mean TMP\>

Average BFR:...........\<Summary Avg BFR\> Average DFR:.......\<Summary Avg DFR\>

Mean Dialysis Temp:....\<Summary Mean Temp\> Mean Conductivity:.\<Summary Mean Cond\>

Total KT:..............\<Summary Total KT\> Total KT/V:........\<Summary Total KT/V\>

URR:...................\<Summary URR\>

Intra Access BF:.......\<IABF\>

VP at Zero BF:.........\<VP0\>

AVP at Zero BF:........\<AVP0BF\>

VP at 200 ml/min:......\<VP200\>

Overall Comments:

\<Summary Comments\>

RX

\_\_

ORDER

Dialyzer:........\<cdsSummary.Dialyzer\>

Reuse: Max#:.....\<cdsSummary.ReuseNum\>

Tx Length:.......\<TxLength\>

Ultrafiltration:.\<cdsSummary.RxUltra\> kg/hr

EDW:.............\<cdsSummary.RxEDW\> Kg

BFR:.............\<cdsSummary.BFR\> cc/min

Dialysate Flow:..\<cdsSummary.DFlow\> cc/min

Temperature:.....\<cdsSummary.Temp\> C

DIALYSATE FORMULA

K:...............\<cdsSummary.DFK\> meq/Liter

HC03:............\<cdsSummary.DFHCO3\> meq/Liter

NA:..............\<cdsSummary.DFNA\> meq/Liter

CA:..............\<cdsSummary.DFCA\> meq/Liter

ANTICOAGULANTS

Type:............\<cdsSummary.ACType\>

Bolus:...........\<cdsSummary.ACLoad\>

Maintenance:.....\<cdsSummary.ACDoses\>

Duration:........\<cdsSummary.ACEndTime\>

Other:...........\<cdsSummary.ACOther\>

MODELING

NA:..............\<cdsSummary.MODNA\>

UF:..............\<cdsSummary.MODUF\>

OTHER ORDERS

\<cdsSummary.RxOther\>

Rx and Lab Notes:

\<cdsSummary.LabNotes\>

PRE-TREATMENT

\_\_\_\_\_\_\_\_\_\_\_\_\_

WEIGHT

Pre-Weight:......\<Summary Pre Weight\> Kg

Dry Weight:......\<cdsSummary.RxEDW\> Kg

Goal Weight:.....\<Summary Goal Weight\> Kg

TEMPERATURE

Pre-Temp:........\<Summary Pre Temp\> F

PRE-BLOOD PRESSURE AND PULSE SEATED

BP:..............\<Sum Pre BP Sys Sit\> / \<Sum Pre BP Dia Sit\> mm Hg

Pulse:...........\<Sum Pre Pulse Sit\> bpm

PRE-BLOOD PRESSURE AND PULSE STANDING

BP:..............\<Sum Pre BP Sys Stand\> / \<Sum Pre BP Dia Stand\> mm Hg

Pulse:...........\<Sum Pre Pulse Stand\> bpm

\<Pre Pain Report\>

MENTAL STATUS

Alert:...........\<Sum Pre Alert\>

Confused:........\<Sum Pre Confused\>

Sedate:..........\<Sum Pre Sedate\>

Unresponsive:....\<Sum Pre Unresponsive\>

Lethargic:.......\<Sum Pre Lethargic\>

Restless:........\<Sum Pre Restless\>

Oriented:........\<Sum Pre Oriented\>

(\<Sum Pre Oriented Tex\>)

OTHER

Edema:...........\<Sum Pre Edema\>

Respirations:....\<Sum Pre Resp\>

Shortness of Breath: \<Sum Pre SOB\>

PATIENT EDUCATION

Has the patient been educated?...\<Educated\>

Education Key:.\<EduKey\>

Education Init.\<EduInit\>

PATIENT TRANSPORTATION

Transported by:..\<PreTransportation\>

SAFETY CHECKS

Have the safety checks been performed? \<SafetyChecks\>

PRE-TREATMENT NOTES:

\<cdsSummary.PreNotes\>

ACCESS USED

\_\_\_\_\_\_\_\_\_\_\_

\<ACCESS USED\>

FLOWSHEET

\_\_\_\_\_\_\_\_\_

\<FLOWSHEET\>

Flowsheet Notes:

\<Flowsheet Notes\>

MEDICINE ADMINISTRATION

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\<MEDICINE TABLE\>

POST-TREATMENT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_

WEIGHT

Post-Weight:.....\<Summary Post Weight\> Kg

Tx Goal Weight:..\<cdsSummary.RxEDW\> Kg

TEMPERATURE

Post-Temp:.......\<Summary Post Temp\> F

POST-BLOOD PRESSURE AND PULSE SEATED

BP:..............\<Sum Post BP Sys Sit\> / \<Sum Post BP Dia Sit\> mm Hg

Pulse:...........\<Sum Post Pulse Sit\> bpm

POST-BLOOD PRESSURE AND PULSE STANDING

BP:..............\<Sum Post BP Sys Stan\> / \<Sum Post BP Dia Stan\> mm Hg

Pulse:...........\<Sum Post Pulse Stand\> bpm

\<Post Pain Report\>

MENTAL STATUS

Alert:...........\<cdsSummary.PostAlert\>

Confused:........\<cdsSummary.PostConfu\>

Sedate:..........\<cdsSummary.PostSedat\>

Unresponsive:....\<cdsSummary.PostUnres\>

Lethargic:.......\<cdsSummary.PostLetha\>

Restless:........\<cdsSummary.PostRestl\>

Oriented:........\<PostOriented\>

(type):........\<PostOrientedText\>

OTHER

Edema:...........\<cdsSummary.PostEdema\>

Respirations:....\<cdsSummary.PostResp\>

Shortness of Breath: \<cdsSummary.PostSOB\>

OBSERVATIONS

Was the treatment weight achieved? \<cdsSummary.POWeight\>

Was any medication administered? \<cdsSummary.POMedicat\>

How did the patient tolerate treatment?

Vomiting:......\<cdsSummary.TlrVom\>

Hypotension:...\<cdsSummary.TlrHyp\>

Syncope:.......\<cdsSummary.TlrSyn\>

Cramping:......\<cdsSummary.TlrCram\>

Stable:........\<Sum Post Stable\>

Other:.........\<cdsSummary.TlrOther\> (\<cdsSummary.TlrOtherD\>)

TRANSPORTATION

Transported by:..\<PostTransportation\>

POST-TREATMENT NOTES

\<cdsSummary.PostNotes\>

FALLS RISK EVALUATION

\<FallsAssessment\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Report was generated by \<Version\>

at \<Now\>

# [^41]Appendix E – High Volume Procedure Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are setting up a CP procedure for the first time, follow the Implementation Guide to set up before using this checklist to indicate it as high volume. If the procedure is already in the CPManager, use this checklist to verify the steps are done. This is a checklist for the site to use to setup a high volume procedure:

- Verify the Application Proxy user is created after installation of patch MD\*1.0\*21.
- Add a TITLE in the SIGNATURE BLOCK TITLE field for the Application Proxy user. The site can designate its own SIGNATURE BLOCK TITLE.
- Review the section on Resulting High Volume Procedure in Chapter 4 of the User Manual.
- Decide which procedure to implement as a high volume procedure and which one of the four processes of resulting the high volume procedure is right for the procedure.
- Decide whether to use a Consults title or a CP note title.
- Create a new title or use an existing title.

(Please refer to Chapter 4 Setting Up TIU For Clinical Procedures and Step 2 Create CP Class Document Definition to create new note title. Remember you must map the new title to a VHA Enterprise Standard Title. Select a generic title to map to.)

- Edit the Technical Fields of the title and enter a Q (Quit) for Commit Action: Q and Post-signature Code: Q The MD HIGH VOLUME PROCEDURE SETUP menu allows you to set these fields. The title must be inactive first.

> **NOTE:** This only applies, if you want to use the auto administrative closure functionality. If you want to use the significant findings functionality, you can skip this step.

(Please refer to Chapter 4 Setting Up TIU For Clinical Procedures. The steps to edit the fields are located after the section on Example of TIU Prompts.)

- Define the note title in Clinical procedures. If you choose to use a Consults title, use VA FileMan to edit the DEFAULT TIU NOTE field in the CP Definition file (#702.01). Otherwise, use CPManager application to enter that field with a CP note title.

> **NOTE:** This title is solely for the use of Administrative Closure. Any subsequent note that will be entered for the procedure in CPRS will need a separate title.

FileMan example:

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: CP DEFINITION//

> EDIT WHICH FIELD: ALL//

> Select CP DEFINITION NAME: EKG

> 1 EKG, ROUTINE (12 LEADS)

> 2 EKG ECG

> CHOOSE 1-2: 1 EKG, ROUTINE (12 LEADS)

> NAME: EKG, ROUTINE (12 LEADS) Replace

> TREATING SPECIALTY: CARDIOLOGY//

> REQUIRE EXTERNAL DATA: Yes//

> DEFAULT TIU NOTE: CP TEST TITLE//

- If you are using a Consults title, skip this step. If you are using a CP title, make sure the business rules for the title allow for editing, signing , and adding of Addendum. You need to add additional business rules to allow for these actions.

> The following business rules are sample rules to allow a Medical Technologist to add an addendum, edit it, and sign it. Once the note is administratively closed, the technicians need the ability to add an addendum to enter the workload. Refer to Chapter 5 About ASU Business Rules and the Role of the Interpreter to add business rules. This chapter has steps on how to add a business rule in TIU.

1 An UNSIGNED (TITLE) CP MUSE EKG may BE ADDENDED by a MEDICAL TECHNOLOGIST

2 An UNSIGNED (TITLE) CP MUSE EKG may BE SIGNED by a MEDICAL TECHNOLOGIST

3 An UNSIGNED (TITLE) CP MUSE EKG may BE EDITED by a MEDICAL TECHNOLOGIST

 Assign the option MD COORDINATOR to your Clinical Application Coordinator (CAC).

- Add the high volume procedure using the option MD HIGH VOLUME PROCEDURE SETUP located on the MD COORDINATOR menu.

(Refer to Chapter 6 - Setting Up Clinical Procedures and Step 5, Section on Exported Kernel XPAR Parameter for Patch MD\*1.0\*21. This section shows you how to setup the procedure as high volume procedure.)

- You can enable notification CONSULT/REQUEST RESOLUTION for users that need to be notified upon consult completion. This is done through CPRS CAC. Use Notification Mgmt Menu option and select the Enable/Disable Notifications option. Example screen capture is shown below:

> Select Notification Mgmt Menu Option: 1 Enable/Disable Notifications

> Set PROCESSING FLAG Parameters for Notifications

> Processing Flag may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

> 2 Team (OE/RR) OTL \[choose from OE/RR LIST\]

> 3 Service SRV \[choose from SERVICE/SECTION\]

> 4 Location LOC \[choose from HOSPITAL LOCATION\]

> 5 Division DIV \[<span class="mark">REDACTED</span>\]

> 6 System SYS \[<span class="mark">REDACTED</span>\]

> 7 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

> Enter selection: 1 User NEW PERSON

> Select NEW PERSON NAME: TEST,

> 1 TEST,A TA

> 2 TEST,CARL TC PHYSICIAN

> 3 TEST,CAROLE CJT ISC COMPUTER SPECIALIST

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-3: 1 TEST,A TA

> ----------------- Setting Processing Flag for User: TEST,A -----------------

> Select Notification: CONSULT/REQUEST RESOLUTION

> Are you adding CONSULT/REQUEST RESOLUTION as a new Notification? Yes// YES

> Notification: CONSULT/REQUEST RESOLUTION// CONSULT/REQUEST RESOLUTION CONSUL

> T/REQUEST RESOLUTION

> Value: ?

> Code indicating processing flag for the entity and notification.

> Select one of the following:

> M Mandatory

> E Enabled

> D Disabled

> Value: Enabled

> Select Notification:

 Assign the option MD PROC W/INCOMPLETE WORKLOAD to your CAC or/and technicians (who will be doing the workload reporting). This tool can help the CAC and/or technicians identify which patient has incomplete workload.

# # Appendix F – Consult / Procedure Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are setting up a CP procedure for an existing consult or medicine procedure, you can automatically convert them to CP using the options ‘Consult to Clinical Procedure conversion utility’ \[MD CONCONVERT\] and Procedure to Clinical Procedure conversion utility \[MD PROCONVERT\]. These two menus are grouped under the ‘Conversion Utilities’ \[MD UTILITIES\] menu which resides on the MD COORDINATOR menu and they are locked with the MD ADMINISTRAOR security key. The utility will convert consult and procedures that are in statuses of Pending / Hold / Scheduled. Note that consults or procedures that are setup under DICOM cannot be converted.

conversion Utilities<span class="mark">CO Consult to Clinical Procedure conversion utility</span>

PR Procedure to Clinical Procedure conversion utility

Select Conversion Utilities \<TEST ACCOUNT\> Option: <span class="mark">CO</span> Consult to Clinical Procedure conversion utility

This routine utility will get all the pending consults of

a selected REQUEST SERVICE and convert them to a selected GMRC procedures.

Note that consults that are currently setup with DICOM (in the CLINICAL

SPECIALTY DICOM & HL7 file) cannot be converted to CP with this utility.

DICOM consults will need to discontinued and re-ordered.

Select REQUEST SERVICES SERVICE NAME: <span class="mark">cardIOLOGY</span>

Select a GMRC Procedure to convert TO:<span class="mark">CP ECHO</span>

...OK? Yes// (Yes)

We will proceed to convert CARDIOLOGY consults to

CP ECHO procedures...

Record \# 13 converted.

Record \# 12 converted.

Record \# 11 converted.

Record \# 9 converted.

Record \# 10 converted

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Ad Hoc Health Summary Components, 10-8
alerts
setting up, 10-1
analyzer
for instruments, 6-11
Anticoagulants, 19-1
Application Proxy User
Clinical, Device Proxy Service, 7-1
Ask Encounter Update, 10-3
B
background processor
and test accounts, 3-6
configuring for test accounts, 3-7
Bi-Directional Interface Process Flow, 1-3
Broadcast Messages, 10-4
business rules
adding, 5-1
understanding, 5-1
C
classes
creating, 4-3
Clinical Procedures, 1-1
flowcharts, 1-1
general information, 1-10
introduction, 1-1
populating definition file, 6-1
setting up, 6-1
troubleshooting, 14-1
Code Statuses, 19-1
Command Line Switches, 16-1
Definition, 16-1
List of, 16-3
configuring
HL7 messages, 12-1
Consult procedures
creating, 9-5
Consult Services
setting up, 9-1
Consults
setting up, 9-1
CP Gateway, 1-8
working with, 11-1
CP Manager, 1-8
CP User, 1-8
CPRS, 10-7
editing parameters.
setting up, 10-1
CPRS Tools Menu, 16-2
Custom Data List, 19-1
D
defnition file
populating, 6-1
deleting an automated instrument or procedure, 2-3
Dialyzer List, 19-1
document parameters
defining, 4-10
E
editing
instruments, 6-3
Education Codes, 19-3
ESRD Diagnosis, 19-3
Exported Procedures List, 17-1
Exported Values For Hemodialysis Options, 19-1
F
finding a parameter, 2-2
flowcharts
Clinical Procedures, 1-1
Force PCE Entry, 10-5
G
Glossary, 15-1
H
HL7
configuring, 12-1
fixing technical issues, 12-11
HL7 parameter
setting up, 12-1
hospital location file requirement, 1-15
I
images
and test accounts, 3-1
imaging, 3-1
Instrument Processing Routines, 18-1
instruments
adding, 6-8
deleting, 2-3
editing, 6-3
printing reports, 2-4
setting up, 6-2
using the instrument analyzer, 6-11
interpreter role
understanding, 5-1
introduction
Clinical Procedures, 1-1
M
manuals
related, 1-9
Medication Routes, 19-5
Medication Units, 19-5
Modalities, 19-6
N
notifications
setting up, 10-1
P
parameters
finding, 2-2
populating
CP definition file, 6-1
Preferences, 19-7
printing
instrument reports, 2-4
procedure reports, 2-4
system parameter reports, 2-4
procedures
adding, 6-17
deleting, 2-3
editing, 6-12
printing reports, 2-4
setting up, 6-12
Processed Results
cumulative, 6-16
multiple, 6-16
R
related manuals, 1-9
Report List, 19-8
reports
printing, 2-4
resource requirements, 1-14
S
Scheduled Options
MD PROCESS NOSHOW/CANCEL, 8-2
MD PROCESS RESULTS, 8-3
MD SCHEDULED STUDIES, 1-10, 8-1
MD STUDY CHECK-IN, 1-10, 8-1
share folder
configuration for an automated instrument, 13-1
Shared Broker Environment, 16-1
Summary Report Template, 19-8
system parameter reports
printing, 2-4
system parameters
allow non-instrument attachments, 6-21
bypass CRC checking, 6-22
calculating a file’s CRC value, 6-24
Clinical Procedures home page, 6-22
Clinical Procedures on-line, 6-22
CP/BGP Transfer Directory, 6-22
CRC values, 6-22
days to keep instrument data, 6-24
imaging file types, 6-24
offline message, 6-26
setting up, 6-20
version compatibility, 6-26
V*IST*A scratch HFS directory, 6-28
System Preferences, 19-7
T
test accounts, 3-1
changing, 3-2
configuring background processor, 3-7
refreshing, 3-10
working with background processor, 3-6
titles
creating, 4-3
TIU
setting up, 4-1
toolbar, CP Manager, 2-1
Transportation Methods, 19-6
troubleshooting, 14-1
U
Uni-Directional Interface Process Flow, 1-5
W
workload
implementing, 1-15
reporting, 1-15
X
XPAR EDIT PARAMETER
MD APPOINT START DATE, 6-31
MD APPOINTMENT END DATE, 6-31
MD CLINIC ASSOCIATION, 6-32
MD COMPL PROC DISPLAY DAYS, 6-31
MD DAYS TO RETAIN COM STUDY, 6-31
MD OLYMPUS 7, 6-32
MD USE APPOINTMENT, 6-32
XPAR Parameter Option
MD AUTO CHECK-IN SETUP, 6-29
MD HIGH VOLUME PROCEDURE SETUP, 6-33
[^1]: MD\*1.0\*6 May 2008 Changed document name from “Site Installation Checklist” to “The CP Implementation Process (Webpage).” Revised directions to access the document.
[^2]: Patch MD\*1.0\*6 May 2008 Files added.
[^3]: Patch MD\*1.0\*20 November 2010 Update queued tasks information.
[^4]: Patch MD\*1.0\*21 May 2010 – Updated General CP Package Information to add Assigning Options for options released with patch 21 and previous patches.
[^5]: Patch MD\*1.0\*14 March 2008 Output display changed.
[^6]: Patch MD\*1.0\*14 March 2008 New prompts added.
[^7]: Patch MD\*1.0\*14 March 2008 Update with new TIU prompts example to reflect TIU field change.
[^8]: Patch MD\*1.0\*21 May 2010 - added note title field change for the high volume procedure.
[^9]: Patch MD\*1.0\*4 September 2006 Add instrument warning added.
[^10]: Patch MD\*1.0\*6 May 2008 Processing Application field added.
[^11]: Patch MD\*1.0\*6 May 2008 Processing Application field added.
[^12]: Patch MD\*1.0\*4 September 2006 Wording for Count/Non-count clinic modified.
[^13]: Patch MD\*1.0\*6 May 2008 Processing Application field added.
[^14]: Patch MD\*1.0\*11 June 2009 Processed Results field added.
[^15]: Patch MD\*1.0\*11 June 2009 Processed Results field added.
[^16]: Patch MD\*1.0\*6 May 2008 Processing Application field added.
[^17]: Patch MD\*1.0\*11 June 2009 Editing the PROCESSED RESULT field of CP Definition file (#702.01).
[^18]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^19]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^20]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^21]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^22]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^23]: Patch MD\*1.0\*4 September 2006 Imaging Network Share directory name changed to CP/BGP Transfer Directory.
[^24]: Patch MD\*1.0\*14 March 2008 Exported Kernel XPAR Parameters, option, and screen sample added.
[^25]: Patch MD\*1.0\*6 May 2008 Exported Kernel XPAR Parameters and screen sample added.
[^26]: Patch MD\*1.0\*11 June 2009 Exported XPAR Parameters sample added.
[^27]: Patch MD\*1.0\*21 May 2010 Parameter Definition added.
[^28]: Patch MD\*1.0\*20 November 2010 Exported Kernel XPAR Parameter and screen sample added.
[^29]: Patch MD\*1.0\*21 May 2010 Added Application Proxy User.
[^30]: Patch MD\*1.0\*14 March 2008 Add Scheduled Options.
[^31]: Patch MD\*1.0\*11 June 2009 Add new scheduled option.
[^32]: Patch MD\*1.0\*21 added new scheduled option MD PROCESS RESULTS.
[^33]: Patch MD\*1.0\*14 March 2008 Added visit date setup for auto study check in.
[^34]: Patch MD\*1.0\*21 May 2010 – Added Step 3 Create Ad Hoc Health Summary Components for CP.
[^35]: Patch MD\*1.0\*14 March 2008 Added information about launching the CP Gateway.
[^36]: Patch MD\*1.0\*14 March 2008 Chapter revised to provide clarity.
[^37]: Patch MD\*1.0\*9 November 2007 Using Port 5000 with CACHE.
[^38]: Patch MD\*1.0\*6 May 2008 Added Processing Application field to image.
[^39]: Patch MD\*1.0\*6 May 2008 Added Hemodialysis instrument entries: BRAUN, FRESENIUS, and GAMBRO.
[^40]: Patch MD\*1.0\*6 May 2008 Listed the exported values for Hemodialysis Options.
[^41]: Patch MD\*1.0\*21 May 2010 Add High Volume Procedure Checklist.
