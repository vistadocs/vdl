---
title: VistA Imaging Error Message Guide
doc_type: SUP
doc_label: Supplement
doc_layer: plain
doc_subject: 
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
menu_options: 1
description: > Department of Veterans Affairs Office of Enterprise Development Health Provider Systems
audience: 
keywords: 
  - table
  - contents
  - class
  - blockquote
  - error
  - dicom
  - image
  - even
  - cannot
  - gateway
page_count: 0
word_count: 19957
section_count: 261
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_imgerrormsg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_imgerrormsg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-error-message-guide/001.png)

VistA Imaging Error Message Guide

June 2013 – Revision 11

MAG\*3.0\*34, 116 and 118

> Department of Veterans Affairs Office of Enterprise Development Health Provider Systems

> Error Message Guide

> VistA Imaging MAG\*3.0\*34, 116 and 118

> June 2013

## Property of the US Government

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development office.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Revision History</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4 June 2013</td>
<td><blockquote>
<p>Rev 11: MAG*3.0*34, MAG*3.0*116<strong>,</strong> and MAG*3.0*118 updates. Affected sections: 1.5, 1.7, 1.8, 1.9, 1.13,</p>
<p>1.16, 1.17, 3.1, 3.2, 4.1. Added Terms and Abbreviations table to Preface. <mark>REDACTED</mark> .</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>21 May 2013</p>
</blockquote></td>
<td><blockquote>
<p>Rev 10: MAG*3.0*34, MAG*3.0*116<strong>,</strong> and MAG*3.0*118 updates. Affected sections: 1.1, 1.2, 1.5, 1.8, 1.9,</p>
<p>1.10, 1.15, 1.17, 1.18, 2.14, 2.19, 3.2, 3.4, 4.1. <mark>REDACTED</mark> .</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29 Jan 2013</td>
<td><blockquote>
<p>Rev 9: MAG*3.0*34, MAG*3.0*116<strong>,</strong> and MAG*3.0*118 updates. Affected sections: Chapter 2, Chapter 3, Chapter 4. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1 Dec 2010</td>
<td><blockquote>
<p>Rev 8: MAG*3.0*53 and MAG*3.0*66 updates. Affected sections: 1.1, Chapter 2. Added chapter numbers.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>20 Oct 2009</p>
</blockquote></td>
<td><blockquote>
<p>Rev 7: Applied change pages for Patch 54. Corrected minor errors in sections 1.10.5 and 1.14; repaired corrupt images throughout; standardized mouse usage conventions throughout. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>6 Mar 2007</td>
<td><blockquote>
<p>Rev 6: Patch 69 updates for conversion to Caché. Affected sections: 1.1 – 1.2.1, 1.5.1.2, 1.7.2, 1.7.3, 1.8.3, 1.11, and 1.12.2. Also added sections 1.16.6.20-29; these sections describe previously undocumented error messages introduced in Patch 26. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>1 Mar 2005</td>
<td><blockquote>
<p>Rev 5: Patch 51 updates. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14 Oct 2004</p>
</blockquote></td>
<td><blockquote>
<p>Rev 4: Patch 30 updates</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>20 Mar 2004</p>
</blockquote></td>
<td><blockquote>
<p>Rev 3: Patch 11 updates</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20 Nov 2003</p>
</blockquote></td>
<td><blockquote>
<p>Rev 2: Corrected references to C-Store.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13 Nov 2003</p>
</blockquote></td>
<td><blockquote>
<p>Rev 1: Edited document to remove Reference Source errors, changed title page/footer dates.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Property of the US Government](#property-of-the-us-government)
- [Preface](#preface)
  - [Food and Drug Administration Policy](#food-and-drug-administration-policy)
  - [VA Policy](#va-policy)
  - [Terms and Abbreviations](#terms-and-abbreviations)
  - [Document Conventions](#document-conventions)
- [Chapter 1 DICOM Gateway Error Messages](#chapter-1-dicom-gateway-error-messages)
  - [License Limits](#license-limits)
  - [Limit on Number of C-Store Processes](#limit-on-number-of-c-store-processes)
  - [Limit on Number of Telnet Sessions](#limit-on-number-of-telnet-sessions)
  - [Improper Start-Up Sequence](#improper-start-up-sequence)
  - [Start C-Store Program before MUMPS Server is Running](#start-c-store-program-before-mumps-server-is-running)
  - [Start C-Store Program While it is Already Running](#start-c-store-program-while-it-is-already-running)
  - [Transmit Image before C-Store Program is Running](#transmit-image-before-c-store-program-is-running)
  - [Too Many Instruments for One Image Gateway](#too-many-instruments-for-one-image-gateway)
  - [Images are Acquired, but are not Moved to the File Server](#images-are-acquired-but-are-not-moved-to-the-file-server)
  - [Menu Options not Available](#menu-options-not-available)
  - [System Configuration Settings](#system-configuration-settings)
  - [User Privileges](#user-privileges)
  - [Ad Hoc Operational Issues](#ad-hoc-operational-issues)
  - [Logins Disabled](#logins-disabled)
  - [Privileges and Permissions](#privileges-and-permissions)
  - [Disk Full](#disk-full)
  - [Full MUMPS Databases](#full-mumps-databases)
  - [Data Stored in Wrong Database](#data-stored-in-wrong-database)
  - [Purge MUMPS Error Log](#purge-mumps-error-log)
  - [Purge Old Modality Worklist Entries](#purge-old-modality-worklist-entries)
  - [Purge Old HL7 Transaction Global Nodes](#purge-old-hl7-transaction-global-nodes)
  - [Purge Old Audit Records](#purge-old-audit-records)
  - [Physical Disk Full](#physical-disk-full)
  - [Purge Old DICOM Message Files](#purge-old-dicom-message-files)
  - [Purge DICOM Image Files](#purge-dicom-image-files)
  - [Other Possible Issues](#other-possible-issues)
  - [Extremely Slow Performance](#extremely-slow-performance)
  - [Network Connectivity Problems](#network-connectivity-problems)
  - [Only one VistA Imaging DICOM Gateway (that used to work) is Affected](#only-one-vista-imaging-dicom-gateway-that-used-to-work-is-affected)
  - [Several Processors Are Affected](#several-processors-are-affected)
  - [One or More Windows Show an Error Message](#one-or-more-windows-show-an-error-message)
  - [PACS Isn’t Sending an Image Complete Message](#pacs-isnt-sending-an-image-complete-message)
  - [Other Configuration Issues](#other-configuration-issues)
  - [Loading Master Files](#loading-master-files)
  - [Multiple Instruments are Configured to Use the Same Port Number](#multiple-instruments-are-configured-to-use-the-same-port-number)
  - [Digitized Images Appear Small on the Diagnostic Workstation](#digitized-images-appear-small-on-the-diagnostic-workstation)
  - [Digitized Images Appear Dark](#digitized-images-appear-dark)
  - [Modality Worklist Find Failure](#modality-worklist-find-failure)
  - [Dictionaries Fail to Load](#dictionaries-fail-to-load)
  - [Failover Procedure](#failover-procedure)
  - [Error Messages from VistA Imaging DICOM Gateway Executable Programs](#error-messages-from-vista-imaging-dicom-gateway-executable-programs)
  - [Error Messages from MAGCSTORE.EXE](#error-messages-from-magcstoreexe)
  - [Error Messages from MAGDCMTOTGA.exe](#error-messages-from-magdcmtotgaexe)
  - [Error Messages from MAGABSTRTGA.exe](#error-messages-from-magabstrtgaexe)
  - [Error Messages from MAGDCMCOPY.exe](#error-messages-from-magdcmcopyexe)
  - [Error Messages from MAGTGATODCM.exe](#error-messages-from-magtgatodcmexe)
  - [Run Time Error Messages](#run-time-error-messages)
  - [DICOM Error Messages](#dicom-error-messages)
  - [Error message: \$ZE=\<STKOV\>BTXT+2^DIALOG:::6:6:](#error-message-zestkovbtxt2dialog66)
  - [Error Message “Port in Use” or “Port Unavailable”](#error-message-port-in-use-or-port-unavailable)
  - [Dumping Files that Cannot be Processed by the Gateway Application](#dumping-files-that-cannot-be-processed-by-the-gateway-application)
  - [-b](#b)
  - [-A {d,o,x,n}](#a-doxn)
  - [-N number](#n-number)
  - [-j number](#j-number)
  - [-t {a,c,d,f,o,u,x}](#t-acdfoux)
  - [Microsoft Windows Error Code](#microsoft-windows-error-code)
  - [Run Time Errors Reported by the DICOM Gateway](#run-time-errors-reported-by-the-dicom-gateway)
  - [DICOM Association Errors](#dicom-association-errors)
  - [Unexpected “DATA” PDU](#unexpected-data-pdu)
  - [Peer application entity Requests “Abort Association”](#peer-application-entity-requests-abort-association)
  - [DICOM Association – Invalid Protocol Identifier](#dicom-association-invalid-protocol-identifier)
  - [Opcode for Unsupported Operation](#opcode-for-unsupported-operation)
  - [DICOM Association – Invalid DICOM Standard UID](#dicom-association-invalid-dicom-standard-uid)
  - [Invalid Context Identifier](#invalid-context-identifier)
  - [Invalid Sub-Type](#invalid-sub-type)
  - [Illegal Unique Identifier (UID)](#illegal-unique-identifier-uid)
  - [Storage Provider Error – Unexpected Response](#storage-provider-error-unexpected-response)
  - [Errors Encountered in Reading/Writing DICOM Messages](#errors-encountered-in-readingwriting-dicom-messages)
  - [Unsupported Value Representation (Input)](#unsupported-value-representation-input)
  - [Value Representation Mismatch](#value-representation-mismatch)
  - [Required Type 1 Data Item Missing](#required-type-1-data-item-missing)
  - [Unsupported Value Representation (Output)](#unsupported-value-representation-output)
  - [Modality Worklist – Invalid SOP Class (C-Find)](#modality-worklist-invalid-sop-class-c-find)
  - [HL7 Error Messages](#hl7-error-messages)
  - [Bad HL7 Message Header](#bad-hl7-message-header)
  - [Incomplete HL7 Message](#incomplete-hl7-message)
  - [Bad Fillers Order Number](#bad-fillers-order-number)
  - [DICOM Image Processing Errors During Input](#dicom-image-processing-errors-during-input)
  - [Undefined Imaging Service](#undefined-imaging-service)
  - [File 2005 Corruption Problem](#file-2005-corruption-problem)
  - [Radiology Report File Corruption Problem](#radiology-report-file-corruption-problem)
  - [Group Entry Number Problem](#group-entry-number-problem)
  - [Image Entry Number Problem](#image-entry-number-problem)
  - [Imaging Patient Mismatch Problem](#imaging-patient-mismatch-problem)
  - [Radiology Patient Mismatch Problem](#radiology-patient-mismatch-problem)
  - [No Radiology Case Number](#no-radiology-case-number)
  - [Radiology Case Not in ^RADPT](#radiology-case-not-in-radpt)
  - [Cannot Create Group for Old Radiology Images](#cannot-create-group-for-old-radiology-images)
  - [Cannot Create Group for New Radiology Images](#cannot-create-group-for-new-radiology-images)
  - [Cannot Find Image Group Pointer in Radiology Report](#cannot-find-image-group-pointer-in-radiology-report)
  - [Cannot Create Image File Entry in VistA Database](#cannot-create-image-file-entry-in-vista-database)
  - [Cannot Create Subdirectory to Store Image File](#cannot-create-subdirectory-to-store-image-file)
  - [Cannot Write Image File](#cannot-write-image-file)
  - [TIU Note Patient/Report Mismatch](#tiu-note-patientreport-mismatch)
  - [TIU External Data Link Association Error](#tiu-external-data-link-association-error)
  - [Cannot Find Table with Additional Data Items](#cannot-find-table-with-additional-data-items)
  - [DICOM Element has Too Many Values](#dicom-element-has-too-many-values)
  - [Cannot Create Targa File](#cannot-create-targa-file)
  - [Cannot Create Abstract File](#cannot-create-abstract-file)
  - [No Image File Created](#no-image-file-created)
  - [Error while Creating Image File](#error-while-creating-image-file)
  - [Could not Copy Image File](#could-not-copy-image-file)
  - [Could not Create Image File](#could-not-create-image-file)
  - [Image File Created, but File Size not Greater than 0](#image-file-created-but-file-size-not-greater-than-0)
  - [Image File Created, but Size Differs from Expected File Size](#image-file-created-but-size-differs-from-expected-file-size)
  - [Image File Created, but File Size Differs from Expected File Size](#image-file-created-but-file-size-differs-from-expected-file-size)
  - [Could not Delete Image File](#could-not-delete-image-file)
  - [Cannot find Table with Additional Data Items](#cannot-find-table-with-additional-data-items-1)
  - [Image Patient Mismatch (parent file 2006.5839)](#image-patient-mismatch-parent-file-20065839)
  - [Image and TIU Note Associated with different Notes](#image-and-tiu-note-associated-with-different-notes)
  - [Wrong Group Object Type](#wrong-group-object-type)
  - [Ignore Image File](#ignore-image-file)
  - [Unknown Instrument Mnemonic](#unknown-instrument-mnemonic)
  - [Rename Failed](#rename-failed)
  - [Image File Creation Error](#image-file-creation-error)
  - [Image File Subdirectory Creation Error](#image-file-subdirectory-creation-error)
  - [New Files Might Overwrite Existing Ones (Single)](#new-files-might-overwrite-existing-ones-single)
  - [New Files Might Overwrite Existing Ones (Multiple)](#new-files-might-overwrite-existing-ones-multiple)
  - [Cannot Delete File](#cannot-delete-file)
  - [Unknown Status (Patient Safety RPC)](#unknown-status-patient-safety-rpc)
  - [Rollback Error (number of returned elements)](#rollback-error-number-of-returned-elements)
  - [Rollback error (returncode)](#rollback-error-returncode)
  - [Problem with Temporary File (1)](#problem-with-temporary-file-1)
  - [Problem with Temporary File (2)](#problem-with-temporary-file-2)
  - [Problem with Temporary File (3)](#problem-with-temporary-file-3)
  - [Image Copy Error](#image-copy-error)
  - [Image Write Failed](#image-write-failed)
  - [Targa Abstract Creation Error](#targa-abstract-creation-error)
  - [Multiframe Image File Creation Error (number of returned elements)](#multiframe-image-file-creation-error-number-of-returned-elements)
  - [Multiframe Image File Creation Error (return code not “processed”)](#multiframe-image-file-creation-error-return-code-not-processed)
  - [Multiframe Image File Creation Error (return code not “store”)](#multiframe-image-file-creation-error-return-code-not-store)
  - [Multiframe Image File Creation Error (error in command)](#multiframe-image-file-creation-error-error-in-command)
  - [Targa File Creation Error](#targa-file-creation-error)
  - [Could not Open Image File for Write](#could-not-open-image-file-for-write)
  - [Data Transfer Dictionary Missing](#data-transfer-dictionary-missing)
  - [Invalid Multiplicity](#invalid-multiplicity)
  - [Routing Not Actively Used](#routing-not-actively-used)
  - [Cannot Create Abstract](#cannot-create-abstract)
  - [DICOM Image Processing Errors During Output](#dicom-image-processing-errors-during-output)
  - [Bad Targa File](#bad-targa-file)
  - [Cannot Establish Connection with MAGVISTASENDIMAGE](#cannot-establish-connection-with-magvistasendimage)
  - [Connection to Destination Storage Provider Failed](#connection-to-destination-storage-provider-failed)
  - [Could Not Establish Association with Destination SCP](#could-not-establish-association-with-destination-scp)
  - [DICOM Network Error](#dicom-network-error)
  - [Image Transmission Acknowledgement Failed](#image-transmission-acknowledgement-failed)
  - [Image Transmission Failed](#image-transmission-failed)
  - [Cannot Acknowledge Establishment of Association](#cannot-acknowledge-establishment-of-association)
  - [Cannot Acknowledge Release of Association](#cannot-acknowledge-release-of-association)
  - [Error Messages Report by DICOM Message Queuing Software](#error-messages-report-by-dicom-message-queuing-software)
  - [Error in Directory Lookup of FIFO Queue Subdirectory](#error-in-directory-lookup-of-fifo-queue-subdirectory)
  - [Cannot Create FIFO Queue Subdirectory](#cannot-create-fifo-queue-subdirectory)
  - [Invalid Data in Queue Pointer File](#invalid-data-in-queue-pointer-file)
  - [Cannot Create a FIFO Queue Text File](#cannot-create-a-fifo-queue-text-file)
  - [Unrecognized Command Code in DICOM Message](#unrecognized-command-code-in-dicom-message)
  - [Unsupported Command in DICOM Message](#unsupported-command-in-dicom-message)
  - [TCP/IP Communications Errors](#tcpip-communications-errors)
  - [Cannot Connect to TCP/IP Socket (Set-Up Error)](#cannot-connect-to-tcpip-socket-set-up-error)
  - [Cannot Find DICOM Message File to Send](#cannot-find-dicom-message-file-to-send)
  - [Invalid First 8-bytes in DICOM Message](#invalid-first-8-bytes-in-dicom-message)
  - [Length-to-End Missing in DICOM Message](#length-to-end-missing-in-dicom-message)
  - [SOP Class UID Missing in DICOM Message](#sop-class-uid-missing-in-dicom-message)
  - [Invalid SOP Class UID in DICOM Message](#invalid-sop-class-uid-in-dicom-message)
  - [Unknown Presentation Context ID](#unknown-presentation-context-id)
  - [Unexpected PDU (expected 04 = P-Data)](#unexpected-pdu-expected-04-p-data)
  - [Errors that may occur in Remote Procedure Calls](#errors-that-may-occur-in-remote-procedure-calls)
  - [UID Checking Errors](#uid-checking-errors)
  - [Notes:](#notes)
  - [MAGV STUDY UID CHECK return codes:](#magv-study-uid-check-return-codes)
  - [MAGV SERIES UID CHECK return codes:](#magv-series-uid-check-return-codes)
  - [MAGV SOP UID CHECK return codes:](#magv-sop-uid-check-return-codes)
  - [Errors Reported by the Menu Processor](#errors-reported-by-the-menu-processor)
  - [Cannot Start Application because Conflicting Application Is Running](#cannot-start-application-because-conflicting-application-is-running)
  - [Cannot Start Multiple Instances of the Same Application](#cannot-start-multiple-instances-of-the-same-application)
  - [Expired Credentials](#expired-credentials)
  - [VistA Send Image](#vista-send-image)
- [Chapter 2 DICOM Query/Retrieve Server Error Messages](#chapter-2-dicom-queryretrieve-server-error-messages)
  - [Class not Found](#class-not-found)
  - [Cannot Bind Port](#cannot-bind-port)
  - [DICOM Connectivity Framework (DCF) Read Configuration](#dicom-connectivity-framework-dcf-read-configuration)
  - [Cannot Open File](#cannot-open-file)
  - [Audit Log](#audit-log)
  - [C-Find Requests](#c-find-requests)
  - [C-Move Requests](#c-move-requests)
  - [Moving Objects](#moving-objects)
  - [VR Violation](#vr-violation)
  - [Accessing DICOM Object from Storage](#accessing-dicom-object-from-storage)
  - [Sending DICOM objects to DICOM device](#sending-dicom-objects-to-dicom-device)
  - [Association with DICOM device](#association-with-dicom-device)
  - [Invalid Calling AETitle](#invalid-calling-aetitle)
  - [Invalid Called AETitle](#invalid-called-aetitle)
  - [Study Level Only](#study-level-only)
  - [Assembling DICOM Object](#assembling-dicom-object)
  - [Null Pointer Exception](#null-pointer-exception)
  - [Querying Whole Database](#querying-whole-database)
  - [Duplicate Study Instance UID during a C-Move operation](#duplicate-study-instance-uid-during-a-c-move-operation)
- [Chapter 3 DICOM Storage SCP Error Messages](#chapter-3-dicom-storage-scp-error-messages)
  - [Initialization Errors](#initialization-errors)
  - [DICOM Listener could not Start on Port](#dicom-listener-could-not-start-on-port)
  - [Calling AETitle Rejected](#calling-aetitle-rejected)
  - [Called AETitle Rejected](#called-aetitle-rejected)
  - [AETitle Authentication Association Request Rejected](#aetitle-authentication-association-request-rejected)
  - [DICOM Toolkit Internal Error](#dicom-toolkit-internal-error)
  - [DICOM Toolkit Configuration File Read Error](#dicom-toolkit-configuration-file-read-error)
  - [Data Processing Errors](#data-processing-errors)
  - [IOD Violations](#iod-violations)
  - [Unexpected Data in IOD](#unexpected-data-in-iod)
  - [Unknown SOP Class](#unknown-sop-class)
  - [Error Status or Message Delivery Failure to remote Storage SCU](#error-status-or-message-delivery-failure-to-remote-storage-scu)
  - [Storing Object Failure](#storing-object-failure)
  - [Queuing E-mail Error](#queuing-e-mail-error)
  - [DICOM Legacy Gateway Configuration Loading Failed](#dicom-legacy-gateway-configuration-loading-failed)
  - [No DICOM Instruments Defined in VistA](#no-dicom-instruments-defined-in-vista)
  - [HDIG and DICOM Gateway Site IDs do not Match](#hdig-and-dicom-gateway-site-ids-do-not-match)
  - [Formatted Data/UID Failure](#formatted-datauid-failure)
  - [Write Out DICOM Object Error](#write-out-dicom-object-error)
  - [DICOM Filename and IEN Error](#dicom-filename-and-ien-error)
  - [DICOM File to RAID Error](#dicom-file-to-raid-error)
  - [E-mail to Queue Message Table Error](#e-mail-to-queue-message-table-error)
  - [Connection Settings Error](#connection-settings-error)
  - [E-mail Error](#e-mail-error)
  - [Requeuing E-mail Failure](#requeuing-e-mail-failure)
  - [Create Icon Image Failure](#create-icon-image-failure)
  - [Unable to Find Current File Error](#unable-to-find-current-file-error)
  - [Reading Current File Error](#reading-current-file-error)
  - [Requeuing After Failed Icon Creation Error](#requeuing-after-failed-icon-creation-error)
  - [Create Icon Image Failure After Maximum Retries](#create-icon-image-failure-after-maximum-retries)
  - [DICOM Router Error](#dicom-router-error)
  - [DICOM Object Contains VR Error for Critical Element](#dicom-object-contains-vr-error-for-critical-element)
  - [Storage Errors](#storage-errors)
  - [URL not Following CIFS Convention Error](#url-not-following-cifs-convention-error)
  - [HDIG Unable to Access SMB File](#hdig-unable-to-access-smb-file)
  - [Storage Error Messages](#storage-error-messages)
  - [DICOM Storage SCP IOD Validation Error](#dicom-storage-scp-iod-validation-error)
  - [DICOM Storage SCP Processing/DB Connection Error](#dicom-storage-scp-processingdb-connection-error)
  - [Archiving Errors](#archiving-errors)
  - [Failed to Write Stream to Disk Filename](#failed-to-write-stream-to-disk-filename)
  - [Failed to Delete Incomplete File](#failed-to-delete-incomplete-file)
  - [Archive Configuration Error](#archive-configuration-error)
- [Chapter 4 DICOM Importer II Error Messages](#chapter-4-dicom-importer-ii-error-messages)
  - [General Error Messages](#general-error-messages)
  - [Work Item Not Found](#work-item-not-found)
  - [Work Item in Invalid Status](#work-item-in-invalid-status)
  - [Work in Progress](#work-in-progress)
  - [Importer Item Failed Processing](#importer-item-failed-processing)
  - [Staging and Direct Import Error Messages](#staging-and-direct-import-error-messages)
  - [Drive Not Ready](#drive-not-ready)
  - [Folder Doesn’t Exist](#folder-doesnt-exist)
  - [Media Has Changed](#media-has-changed)
  - [Order Selection Error Messages](#order-selection-error-messages)
  - [Outside Locations Not Configured](#outside-locations-not-configured)
  - [Valid Study Date Required](#valid-study-date-required)
  - [Reports Error Messages](#reports-error-messages)
  - [Invalid Report Parameters](#invalid-report-parameters)
  - [Image Viewing Error Messages](#image-viewing-error-messages)
  - [DICOM Viewer Not Found](#dicom-viewer-not-found)
  - [Invalid Instance Range](#invalid-instance-range)
  - [Too Many Instances Selected](#too-many-instances-selected)
> The purpose of this guide is to provide information about error messages as they relate to the Veterans Health Information Systems and Technology Architecture (VistA) Imaging V. 3.0 package (i.e., files, routines, and configuration that comprise the VistA Imaging System).

## Food and Drug Administration Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.

## VA Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment. Modifying FDA regulated software under any other conditions is a severe violation of the Code of Federal Regulations. Local, that is field-based, developers are prohibited from modifying national software that is certified by the FDA.

> Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.

June 2013 VistA Imaging System MAG\*3.0\*34, 116 and 118 iii

Error Message Guide – Rev. 11

> Preface

## Terms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following terms are used in this document.

| Term          | Definition                                                                                                                                                                                                                                                         |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AE                | Application Entity: An end point of a DICOM information exchange, including the DICOM network or media interface software; that is, the software that sends or receives DICOM information objects or messages. A single device may have multiple Application Entities. |
| AE_Title          | The unique name assigned to a DICOM application to identify the application to other DICOM applications on the network.                                                                                                                                                |
| Application log   | The primary log on the HDIG to which it writes application-level events.                                                                                                                                                                                               |
| CIFS              | Common Internet File System                                                                                                                                                                                                                                            |
| cPACS             | Commercial PACS                                                                                                                                                                                                                                                        |
| CPU               | Central Processing Unit                                                                                                                                                                                                                                                |
| DB                | Database                                                                                                                                                                                                                                                               |
| DCF               | DICOM Connectivity Framework                                                                                                                                                                                                                                           |
| DHCP              | Dynamic Host Configuration Protocol                                                                                                                                                                                                                                    |
| DICOM             | Digital Imaging and Communication in Medicine                                                                                                                                                                                                                          |
| DICOM Correct     | The name assigned to the process used to correct DICOM Objects that fail processing on the DICOM Gateway.                                                                                                                                                              |
| DICOM Importer II | Refers to the application that performs the automated DICOM import process from outside facilities.                                                                                                                                                                    |
| DIMSE             | DICOM Message Service Element                                                                                                                                                                                                                                          |
| DNS               | Domain Name System                                                                                                                                                                                                                                                     |
| DoD               | Department of Defense                                                                                                                                                                                                                                                  |
| DVD               | Digital Versatile Disc                                                                                                                                                                                                                                                 |
| HDIG              | Hybrid DICOM Image Gateway: An image gateway that combines the legacy DICOM Gateway and the new VISA Gateway. It implements DICOM services.                                                                                                                            |
| HIS               | Healthcare Information System                                                                                                                                                                                                                                          |
| HL7               | Health Level 7                                                                                                                                                                                                                                                         |
| KIDS              | Kernel Installation and Distribution System                                                                                                                                                                                                                            |
| MUMPS             | Massachusetts General Hospital Utility Multi-Programming System                                                                                                                                                                                                        |
| MWL               | Modality Worklist                                                                                                                                                                                                                                                      |
| NIC               | Network Interface Card                                                                                                                                                                                                                                                 |
| PACS              | Picture Archiving and Communications System                                                                                                                                                                                                                            |
| PDU               | Protocol Data Unit                                                                                                                                                                                                                                                     |
| Q/R               | Query/Retrieve                                                                                                                                                                                                                                                         |
| RAID              | Redundant Array Of Independent Disks                                                                                                                                                                                                                                   |
| RPC               | Remote Procedure Call                                                                                                                                                                                                                                                  |

Preface

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
<td>SCP</td>
<td>Service Class Provider</td>
</tr>
<tr class="even">
<td>SCU</td>
<td>Service Class User</td>
</tr>
<tr class="odd">
<td>SMTP</td>
<td>Simple Mail Transfer Protocol</td>
</tr>
<tr class="even">
<td>SOP</td>
<td>Service Object Pair</td>
</tr>
<tr class="odd">
<td>SOP Class</td>
<td>Unique identifier assigned by the DICOM Standard to identify DICOM objects.</td>
</tr>
<tr class="even">
<td>Staging</td>
<td><p>Copying study data from either media or an authorized network location into temporary persistent storage for later reconciliation. There are two types of staging (controlled by Security Keys):</p>
<p><em><strong>Basic Staging</strong></em>: An authorized user copies all study data from an authorized source to Importer II Persistent Storage.</p>
<p><em><strong>Advanced Staging</strong></em>: An authorized user can view source data by study and copy data by study to Importer II Persistent Storage.</p></td>
</tr>
<tr class="odd">
<td>Supported SOP Class</td>
<td>A DICOM Object that can be processed by the DICOM Gateway and delivered to other VistA Imaging applications for use within VistA Imaging.</td>
</tr>
<tr class="even">
<td>TARGA</td>
<td>Truevision Advanced Raster Graphics Adapter</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td>Transmission Control Protocol / Internet Protocol</td>
</tr>
<tr class="even">
<td>TIU</td>
<td>Text Integration Utility</td>
</tr>
<tr class="odd">
<td>UID</td>
<td>Unique identifier</td>
</tr>
<tr class="even">
<td>VA</td>
<td>US Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>VISA</td>
<td>VistA Imaging Services Architecture</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="odd">
<td>VIX</td>
<td>VistA Imaging eXchange</td>
</tr>
<tr class="even">
<td>VLAN</td>
<td>Virtual Local Area Network</td>
</tr>
<tr class="odd">
<td>WINS</td>
<td>Windows Internet Name Service</td>
</tr>
</tbody>
</table>

> Preface

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses the following typographic conventions.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol/Typeface</strong></th>
<th><blockquote>
<p><strong>Meaning/Use</strong></p>
</blockquote></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Bold</strong></td>
<td><blockquote>
<p>User input, selection, GUI element (menu item, button, field)</p>
</blockquote></td>
<td><p>Click <strong>Finish</strong>.</p>
<p>Choose <strong>Open</strong> from the <strong>File</strong> menu. Type the user account name in the</p>
<p><strong>Name</strong> field.</p></td>
</tr>
<tr class="even">
<td><p>Monospaced font (typically in a box)</p>
<p>(Bold indicates user input or selection).</p></td>
<td><blockquote>
<p>Command-line sample or output (such as character- based screen captures and computer source code), menus, file names</p>
</blockquote></td>
<td><p>Navigate to the</p>
<p>\Docs\Imaging_Docs_Latest</p>
<p>folder.</p></td>
</tr>
<tr class="odd">
<td><em>Italics</em></td>
<td><blockquote>
<p>Emphasis, reference to section in the document or another document, or a variable</p>
</blockquote></td>
<td>For more information, see the <em>VistA Imaging DICOM Gateway Installation Guide</em>.</td>
</tr>
<tr class="even">
<td>Square brackets, monospace or italics</td>
<td><blockquote>
<p>Variable, placeholder, VistA menu</p>
</blockquote></td>
<td><p>Access the Kernel Installation and Distribution System Menu [XPD MAIN].</p>
<p>;;3.0;IMAGING;[Patch</p>
<p>List];Mar 19, 2002;Build</p>
<p>1989;Feb 21, 2011</p>
<p>MAG*3.0*&lt;<em>PatchNumber</em>&gt;.KID</p></td>
</tr>
</tbody>
</table>
# Chapter 1 DICOM Gateway Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter contains a listing of error messages generated by the DICOM Gateway, grouped by general subject.

## License Limits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MUMPS (Massachusetts General Hospital Utility Multi-Programming System) database server used by the Veterans Health Information Systems and Technology Architecture (VistA) Imaging Digital Imaging and Communication in Medicine (DICOM) Gateway requires a large enough license to allow all users, background tasks, and network connections to operate simultaneously. Of course, the larger the license, the higher the fee. In the *MAG\*3.0\*34, MAG\*3.0\*116, and MAG\*3.0\*118 Planning and Installation Instructions*, a minimum license size is specified for Caché as 16 concurrent users. This size system will allow for a sufficient number of job partitions. When the MUMPS engine on a VistA Imaging DICOM Gateway has a smaller license, it may not function adequately, and the error messages shown in this section may appear.

> An error message may appear when an attempt is made to start an additional task on the database server, while all license slots are being utilized. There are a number of situations where such a message can show up.

- C-Store connection
- Telnet connection

> The discussion below provides more details about each of these.

> As the actual usage of the database server increases, the first action should be to rethink the allocation of tasks over the various VistA Imaging DICOM Gateway processors. Only when additional tasks are needed, and all of the available processors have been *maxed out*, should an additional processor be acquired, or the license count on at least one processor be increased.

> Contact the vendor of the MUMPS Database server (InterSystems Corporation) or a designated reseller to acquire licenses, or to increase license limits.

## Limit on Number of C-Store Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For each C-Store processor, a background task will be started on the VistA Imaging DICOM Gateway. The license quota for number of users needs to be high enough to support all C-Store processes that are assigned to a single Image Gateway.

> When the quota for *users* is not high enough to start all C-Store processes, the startup log of the failing MAG_CSTORE.EXE task will contain this error message:

> Chapter 1 DICOM Gateway Error Messages

![](vista-imaging-error-message-guide/002.png)

> Error message: Trying to connect to MUMPS storage controller. No additional MUMPS partitions are available. Increase the number of TCP/IP connections for your MUMPS license.

> If this error message occurs, first try to re-distribute the various C-Store providers over the VistA DICOM Image Gateways. If all Image Gateways are maxed out, consider obtaining a license with a higher *user* quota.

## Limit on Number of Telnet Sessions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vista-imaging-error-message-guide/003.png)Each telnet session counts as one user. When the *user* quota is not high enough to accommodate all needed interactive sessions, the attempt to launch a telnet session will produce this error message:

> Error message: License limit exceeded. Connection to host lost.

> When this error occurs, the local system manager should use the Caché Control Panel (right- click the Caché cube, select Control-Panel) to run a System Status, and terminate any non- essential telnet sessions. (Select the display that shows all running processes, right-click on redundant processes and select Terminate.)

> When all running telnet sessions are essential, consider obtaining a license with a higher user quota.

> Chapter 1 DICOM Gateway Error Messages

## Improper Start-Up Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Start C-Store Program before MUMPS Server is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When an attempt is made to start a C-Store program (MAG_CSTORE.EXE) before the MUMPS Server has been started, an error message like the following will appear:

> Note: This section applies to MAG\*3.0\*99 and earlier image gateways.

![](vista-imaging-error-message-guide/004.png)

> Error message: Trying to connect to MUMPS storage controller. Connect error in init_client\< \>. Could not connect to the MUMPS storage controller. Check that the DICOM CSTORE process is active. Also verify that the IP address “localhost” & port number “60000” are correct.

> To resolve this problem, first start the MUMPS Server and then start the C-Store program.

## Start C-Store Program While it is Already Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When an attempt is made to start an instance of a C-Store program, while a copy of that program for that instrument is already running, the following error message will be reported:

> Note: This section applies to MAG\*3.0\*99 and earlier image gateways.

![](vista-imaging-error-message-guide/005.png)

> Error message: Trying to connect to MUMPS storage controller. The CT1 modality is already running.

> To resolve this problem, press \<Enter\> to terminate the second instance of the program.

> Chapter 1 DICOM Gateway Error Messages

## Transmit Image before C-Store Program is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When an attempt is made to store an image while the C-Store program for the instrument is not running, an error message is likely to appear. The actual error message is instrument-specific. The following is a sample message produced by the Mallinckrodt Send_Image program.

![](vista-imaging-error-message-guide/006.png)

> To resolve this problem, first start the C-Store program by double-clicking on its icon, and then transmit the image.

## Too Many Instruments for One Image Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: This section applies to MAG\*3.0\*99 and earlier image gateways.

> Each instrument that transmits images to an Image Gateway uses one MUMPS background partition. When too many instruments are assigned to one single Image Gateway exceeding the maximum partition count, the following error message will appear:

![](vista-imaging-error-message-guide/007.png)

> Error message: Error in network_write\< \>, WSAGetLaserError = 10054 To be written: 43

> Peer DICOM Application Entity dropped the TCP/IP circuit connection MUMPS length network_read\< \> error: -1

> When this happens, first try to re-distribute the various instruments over the available Image

> Chapter 1 DICOM Gateway Error Messages

> Gateways. If that isn’t possible, consider acquiring a license for more *users* for the processor.

## Images are Acquired, but are not Moved to the File Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When images are being acquired successfully, but are not being transported to the Windows File Server, this is most likely due to the fact that the *Process DICOM Images* task is not running.

> Check to make sure that it is running.

> If *Process DICOM Images* is running, and images are still not moving to the Windows File Server, one of the following six problems might be happening:

- The patient/study information in the image header is incorrect and the association cannot be properly made.
- The network connection from the DICOM Image Gateway to the Windows File Server may be down.
- There may not be an entry in the Modality.DIC for the manufacturer-model-modality defined in the image header.
- There may be a run-away job on the VistA Imaging DICOM Gateway, either in MUMPS or elsewhere, which is preventing the image-processing task from having the necessary CPU resources. (Use Windows Task Manager and ^%SS to further identify this problem.)
- There may be a problem with a run-away job on the VistA main HIS preventing the Kernel Broker from having the necessary CPU resources.
- There may be other problems.

## Menu Options not Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The availability of the menu options on the DICOM Gateway is affected by a number of issues:

- System configuration settings
- User privileges
- Ad hoc operational issues

> The very first time that the menu is displayed on a newly installed system, only those menu options that relate to set-up and configuration will be available. Menu options that are available are shown in bold face; menu options that are not available are shown in a fainter font and are enclosed in parentheses:

> Chapter 1 DICOM Gateway Error Messages

> VistA DICOM Gateway Menu --

1.  (Text Gateway)
2.  (Image Gateway)
3.  (Routing Gateway)
4.  System Maintenance
5.  Quit OPTION:

## System Configuration Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using menu option Update Gateway Configuration Parameters (menu path 4-2-2), a number of parameters can be (re)defined. These parameters determine how the DICOM Gateway can be used. Three of these parameters determine which main menu groups will be available.

> When these parameters are set as indicated in the sample dialog below, only the menu options for the Text Gateway will be available.

> *Sample dialog*:

> Will this computer be a DICOM Image Gateway? NO \<Enter\> Will this computer be a DICOM Text Gateway? YES \<Enter\> Will this computer be a Routing Processor? NO \<Enter\>

> *Sample menu*:

> VistA DICOM Gateway Menu -- Test System

1.  Text Gateway
2.  (Image Gateway)
3.  (Routing Gateway)
4.  System Maintenance
5.  Quit OPTION:

## User Privileges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A user can be logged in on a DICOM Gateway as either a *fully-privileged* user or as a *view-only* user. When a user is *fully-privileged*, typically all menu options will be available. When a user has *view-only* access, all menu options that can be used to modify data will be made unavailable. For instance, a *view-only* user will see the following menu on the Text Gateway:

> Chapter 1 DICOM Gateway Error Messages

> VistA DICOM Text Gateway -- Test System

1.  (Start Processing Text Messages from HIS)
2.  (Send DICOM Text Messages to Commercial PACS or Broker)
3.  Display Text Gateway Statistics
4.  Display Modality Worklist Statistics
5.  Modality Worklist Query
6.  Display a HL7 Message
7.  Display a DICOM Message
8.  (Modify the HL7 Message Pointer)
9.  Generate a Daily Summary Report
10. (Purge Old Modality Worklist Entries)
11. (Purge Old DICOM Message Files)
12. (Purge Old HL7 Transaction Global Nodes)
13. (Purge Old Audit Records)<span id="1.3.3_Ad_Hoc_Operational_Issues" class="anchor"></span> OPTION:

## Ad Hoc Operational Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Certain menu options can only be executed after certain configuration steps have been completed. For instance, there are menu options that can send e-mail messages when errors occur. Those menu options will not be available until an e-mail address has been configured (using menu option Update Gateway Configuration Parameters (menu path 4-2-2). When menu options are made unavailable because no e- mail address has been set up yet, the following message will appear at the bottom of the menu:

> VistA DICOM Text Gateway -- Test System

1.  (Start Processing Text Messages from HIS)
2.  Send DICOM Text Messages to Commercial PACS or Broker
3.  Display Text Gateway Statistics
4.  Display Modality Worklist Statistics
5.  Modality Worklist Query
6.  Display a HL7 Message
7.  Display a DICOM Message
8.  Modify the HL7 Message Pointer
9.  Generate a Daily Summary Report
10. Purge Old Modality Worklist Entries
11. Purge Old DICOM Message Files
12. Purge Old HL7 Transaction Global Nodes
13. Purge Old Audit Records

> You must first use option 4-2-2 to specify E-mail information.

> OPTION:

> Other menu options require that the location of the DICOM Gateway must be properly configured. The location information is also set up using menu option Update Gateway Configuration Parameters (menu path 4-2-2). When the location information is missing, the following error message will appear:

> Chapter 1 DICOM Gateway Error Messages

> VistA DICOM Text Gateway -- Test System

1.  (Start Processing Text Messages from HIS)
2.  (Send DICOM Text Messages to Commercial PACS or Broker)
3.  (Display Text Gateway Statistics)
4.  (Display Modality Worklist Statistics)
5.  Modality Worklist Query
6.  Display a HL7 Message
7.  Display a DICOM Message
8.  Modify the HL7 Message Pointer
9.  (Generate a Daily Summary Report)
10. Purge Old Modality Worklist Entries
11. Purge Old DICOM Message Files
12. Purge Old HL7 Transaction Global Nodes
13. (Purge Old Audit Records)

> You must first use option 4-2-2 to obtain Location information.

> OPTION:

> Finally, the menu program can be started in two different ways. Normally, the menu program is started after a user logs in using an access and verify code that is valid on the VistA system.

> When proper credentials have been provided, the user can use the various menu options and perform actions that may require that Remote Procedures are executed on the VistA system.

> The other possibility is that a user logs in using credentials that are used for local maintenance on the DICOM Gateway only. In this case, the DICOM Gateway will not be able to call any Remote Procedures on the VistA, but menu options will be available to perform any local maintenance that may be necessary. When a user is logged in using *local maintenance* credentials, a warning message is displayed at the bottom of the menu:

> VistA DICOM Gateway Menu -- Test System

1.  Text Gateway
2.  Image Gateway
3.  Routing Gateway
4.  System Maintenance
5.  Quit

> Currently not authorized to invoke RPCs on VistA. OPTION:

## Logins Disabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Usually, users are permitted to login into their VistA system. However, there are times when this permission is temporarily withdrawn. This may happen in a number of cases:

- <u>automatically</u>, when there are too many users on the VistA system
- <u>intentionally</u>, when maintenance on the VistA system is scheduled
- <u>casually</u>, for the duration of a single KIDS installation

> When any of these situations occurs, logins will be temporarily disabled, and all attempts to execute Remote Procedure Calls (RPCs) will fail.

> Chapter 1 DICOM Gateway Error Messages

> In such a case, a DICOM Gateway will report a failure to connect to VistA:

> Could not connect to M-to-M Broker

> (0,SIGNON - - - Signons not currently allowed on this processor.)

> When a Remote Procedure was called for an interactive application option, the software will return to the menu, and the user can restart that application at a later time.

> When the RPC was called from a non-interactive application, the software will wait for 5 minutes, and then attempt to reconnect to VistA.

> \*\*\* Error: \<ECODE\>CALLRPC+14^MAGM2VCU:::6:27:

> (,M13\<NORPC\> 0SIGNON - - - Signons not currently allowed on this processor.,) \*\*\* Attempting to reconnect...

> Cannot re-connect to VistA at this time.

> 0,SIGNON - - - Signons not currently allowed on this processor.

> \*\*\* Wed 15:49 A time-out has occurred on the M2M Broker \*\*\*

> \*\*\* (communication with the VistA System). \*\*\*

> \*\*\* This system will wait 5 minutes and try to link again \*\*\*

> Attempting to reconnect...

> ... reconnected

## Privileges and Permissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> By the nature of the information that is stored and manipulated in a hospital environment, many aspects of the VistA Imaging DICOM Gateway are subject to access restrictions. It is important to keep track of the various user-accounts that have to be created and utilized to ensure proper access for the various parts of the system.

> When any part of the software reports an access restriction type of error, the most common causes are that…

- The current user is logged in using a user-account that does not have the privileges needed to perform the action at hand
- A password has been changed, and the current user has not yet updated the registered copy of that password to the current value.

> It is also important to be aware that…

- Some access restrictions apply to the current user
- Some access restrictions apply to the file at hand
- Some access restrictions apply to the disk-share where a file is stored
- Different access privileges may apply for reading an existing file and for creating a new file

> Typical error messages that may appear are *Image file subdirectory creation error*, *Cannot create the image subdirectory: -5*, *Cannot find file xxxx* and *Access Denied*.

> Chapter 1 DICOM Gateway Error Messages

## Disk Full

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the course of doing their work, the various processes create temporary data files which are later removed. On occasion, it may be necessary to manually remove data files that have been inadvertently left behind, perhaps by a run-away task (for example, one that is trying to read an incorrectly constructed DICOM image file). The sections below describe several utility functions that may be of help in removing this old computer litter.

> There are two major groups of problems that result in *disk full* error messages:

- Situations where all space within a MUMPS database has been used up.
- Situations where all space on a physical medium has been used up.

## Full MUMPS Databases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Stored in Wrong Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging DICOM Gateway locally *only* stores and maintains data in *its own* database (Namespace DICOM). Any error messages that indicate issues with storage in other databases (for example, %SYS or USER) would indicate that data has been stored in a wrong place. When this happens, the spurious data should be removed from the database where it should not have been stored. (Of course, the VistA Imaging DICOM Gateway remotely stores data in

> ^MAG(2005) and other VistA System globals.)

## Purge MUMPS Error Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a database fills up, *DO NOT* increase the size of the database container file. Under normal circumstances, 15MB is more than enough to hold the DICOM database. As a safety margin, the database is sized at 500MB. When the database becomes *full*, this indicates an error by itself.

> First, the root-cause of this error should be determined, and then the extraneous data should be removed. After this normal processing can continue with plenty of space in the 500MB database.

> The most likely cause for a *database full* situation is that a burst of similar errors caused the error log to overflow the database.

> When this type of error occurs, execute the following steps (preferably, call the CLIN 3 team for help in executing these steps):

1.  Start the Caché Control Panel (right-click the Caché cube and select Control Panel).
2.  In the window for the Caché Control Panel, click Processes.
3.  In the right-hand pane, a list of all active Caché processes will be displayed. Identify the active telnet sessions and terminate all of them (right-click the line for the process and select Terminate).

> Chapter 1 DICOM Gateway Error Messages

4.  In the window for the Caché Control Panel, expand the tree for Local Databases, then right-click the folder for the DICOM database, and select Integrity Check.
5.  A new window will appear; a log of the integrity check will be compiled in this window. If all is well, the log will end with the text, “No Errors were found in this directory”.

![](vista-imaging-error-message-guide/008.png)

6.  If the database is corrupted, first resolve all issues that are reported, using ^REPAIR. (Learning to use ^REPAIR requires a multi-day class from the database vendor. Most of the information learned in this class is *under non-disclosure restrictions*. Call the CLIN 3 team if a database repair is needed.)
7.  Special cases are global variables ^TMP and ^MAGDMLOG. When either of these global variables has become corrupted, it’s not worth the time to try and fix it. Use

> ^REPAIR to remove the global variable from the Global Directory.

8.  Once it is established that it is safe to use the database, proceed with the next steps; otherwise, continue repairing the database.
9.  Check the error-log: in the Caché Control Panel expand the tree for Logs, and go to Application Errors  DICOM  current date. If the error log indicates that there is a persistently recurring software problem, be sure to save a copy of one of these error reports for the CLIN 3 team.
10. Once the important error-logs are saved, erase all error logs.
11. Remove temporary data:
    1.  Open a console window (right-click the Caché cube and select Terminal)

> Chapter 1 DICOM Gateway Error Messages

2.  Issue the commands:
12. Check how much space is now available (in the window for the Caché Control Panel, select the Local Databases folder in the left-hand panel). A survey of the statuses of all local databases will appear in the right-hand panel. Look at the line for the DICOM database.

![](vista-imaging-error-message-guide/009.png)

> If the amount of free space in the DICOM Database is more than 15%, the system can be put back into operation. If necessary, shut down Caché and restart it, so that all background processes will be running again.

> Once the system is back up and running, execute routine purge functions.

> Purging the files and Health Level 7 (HL7) pointers to 30 days should clear sufficient disk space. (Options 10, 11, and 12 on the menu)

> The U-V/W-X queue pointers should be checked.

> MUMPS error logs reside in the MUMPS databases on each VistA Imaging DICOM Gateways in global variable ^ERRORS.

> Old entries in the MUMPS error log can be purged using a menu-option.

## Purge Old Modality Worklist Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Modality Worklist database resides in the MUMPS database on the DICOM Text Gateway in global variable ^MAGDWLST.

> Chapter 1 DICOM Gateway Error Messages

> Old entries in the Modality Worklist database can be purged using menu Option 1-10.

## Purge Old HL7 Transaction Global Nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 transactions are stored in the main hospital VistA MUMPS database in global variable

> ^MAGDHL7.

> Old nodes in that global variable can be purged using menu Option 1-12.

> CAUTION: Running this option will purge the HL7 global on VistA. Once this purge is run you will NOT be able to go back beyond this date to recompile the Modality Worklist (MWL).

## Purge Old Audit Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Audit records that pertain to the whole system are stored in the main hospital VistA MUMPS database in global variable ^MAGDAUDT.

> Old audit records can be purged using menu Option 1-13. This allows the global space to be recovered for other use.

## Physical Disk Full

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purge Old DICOM Message Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the DICOM Text Gateway, the DICOM message files reside in directories with names like

> C:\DICOM\DATA*n*, where *n* is an integer number, typically 1 and usually not higher than 2.

> Old DICOM message files are purged automatically by the message generating application. They can also be purged using a menu-option.

> The entire subdirectory tree can be purged by running INIT_DICOM.BAT in the DATAn directory from the command line. (This has to run on a *quiet system* – be sure to stop all MUMPS processes before doing this.)

> Note: This purging can take many hours to run if it has not been performed in a long time. This should only be run on systems that send messages to a commercial picture archiving and communications system (cPACS). It will not help on systems that do not forward out to a cPACS.

## Purge DICOM Image Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the DICOM Image Gateway, the DICOM image files are stored in the C:\DICOM\IMAGE_IN

> and C:\DICOM\IMAGE_OUT directories for incoming and outgoing images respectively. Normally, all image deletion from these two directories is under automatic program control.

> Chapter 1 DICOM Gateway Error Messages

> Incoming images are deleted from the C:\DICOM\IMAGE_IN directory as they are processed. Incoming images that cannot be processed remain in the directory until they are resolved using the DICOM Failed Image Correction application. Incomplete image files will remain in this directory for at least an hour before they are renamed by appending “\_incomplete” to the filename. These files (\*.dcm_incomplete) will remain in the C:\DICOM\IMAGE_IN directory for further research by site personnel and will require manual deletion.

> Outgoing images are automatically deleted from the C:\DICOM\IMAGE_OUT directory as they are sent. However, they may remain if there is a problem with the transmission. A \*.dcm file in this directory that is older than the current day can be manually deleted.

> On an as-needed basis, use Windows Explorer to delete the old image files from the C:\DICOM\IMAGE_OUT directory.

## Other Possible Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In addition to the possibility that a disk is physically full, there are a number of other reasons why an error message like, *Insufficient disk space to store images. Waiting 10 minutes*. might appear:

- Images are not processed due to lost connection with server
- Images are not processed due to incorrect information in headers.
- Images are not processed due to failure of the “Process Image” process.

> See the window for the session labeled Image Status (2_5) for details. The window will contain information on how badly backed up the system may be (number of files to be processed). Disk space will become available as images are processed. Just keep an eye on the status window to make sure the image count is decreasing.

> Make sure that the session labeled Process DICOM Images (2_3) is running.

> It is very likely that the directory C:\DICOM\Image_In contains files for images that require corrections.

> Some image files may be as large as 30-40MB. When a site needs to store a large number of these files, it is imperative to ensure that sufficient disk space is available.

> It may be possible to use the DICOM Importer II to perform DICOM Corrects for images with demographic information that does not match the HIS information.

> Chapter 1 DICOM Gateway Error Messages

> The VistA Imaging DICOM Gateway uses a site parameter that establishes the percentage of disk space that should remain free. If this percentage is too high, the system will start producing error messages about insufficient disk space when there still is a lot of disk space. To ensure that this parameter is set to a reasonable value, use the US Department of Veterans Affairs (VA)- FileMan (Enter/Edit, file 2006.1):

> PCT FREE SPACE DICOM MSGS: 15//

> Typically, this value should not be larger than 15%.

## Extremely Slow Performance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a normally operating system begins to run very slowly, the first question to ask is “what changed?”

> If a specific system is extremely slow and others are fine, then launch Windows Task Manager to determine what is running on the system. Is there a run-away task? (The problem might be as simple as a user who inadvertently clicked too many times on an icon and launched multiple tasks!)

> The problem might be with the main Hospital Information System. There could be a *run-away* job on it or a situation where the MUMPS-to-MUMPS Broker connection is not functioning properly.

> A slow DICOM Image Gateway may be related to the Windows file server problem. Is there adequate free disk space on the server for new images?

> The problem could also be with the network. The settings should be the same on the VistA Imaging DICOM Gateway as on the hubs and routers. In a wide-area network situation, check that the WAN is operating properly.

> If you suspect that the amount of work for the system might be exceeding the available resources, check the following possible causes:

- If bad performance mainly occurs during peak times, there may be a network bandwidth issue. All devices used for VistA Imaging must be placed on a switched rather than a shared connection. This will reduce delays due to contention and collisions on the device’s Ethernet segment. If the device is already on switched Ethernet, one could try upgrading the network for a higher throughput capacity.
- There could be a bottleneck on the Imaging Storage Server. This could be the case when the Storage Server has a shared Ethernet connection or is connected via a 10 Mbps or a 100 Mbps Ethernet. In that case, upgrading to 1000 Mbps (Gigabit Ethernet) may resolve the problem.

> Chapter 1 DICOM Gateway Error Messages

- There could be an IP routing bottleneck. If the device is on a different TCP/IP subnet than the Imaging Storage Server, the router might be the bottleneck. It is recommended that all VistA Imaging devices be on the same subnet, so that there will be no need for any routing. The VistA Imaging DICOM Gateways and Background Processors must be on the same subnet as the Imaging Storage Server. It may be possible to *collapse* multiple subnets into a single one by migrating to a wider subnet mask.
- If the site uses virtual local area networks (VLANs), routing bottlenecks may not be completely eliminated. Double-check the definitions of the VLANs and the assignment of processors to subnets. Review the routing set-up.
- Check the Network Interface Card (NIC) and the network switch or hub to make sure that none of the components are using “automatic sensing” of speed. If one component is set to *auto* or *auto-detect*, and another component is expecting to use a specific speed, time may be lost in unnecessary negotiations. This feature can sometimes fail.

## Network Connectivity Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Connectivity problems can exhibit themselves in a number of ways:

- Users are unable to login. They see messages like *Domain Controller Unavailable* when they attempt to login into the system.
- The window Network Neighborhood does not show any other computers
- There are error messages while booting up the computer, or when attempting to start a program.
- There are error messages related to TCP/IP, NetBIOS name resolution, or NIC hardware in the system’s Event Viewer.
- There may be errors in configuration information.

> If any of the above situations occurs, the following steps usually lead to a quick assessment of the actual problem.

## Only one VistA Imaging DICOM Gateway (that used to work) is Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Check first whether the problem is localized in one computer, or shared by multiple ones. If the problem occurs only in one computer, check the following:

1.  Check that all cables are properly connected.
2.  Check that the information in the appropriate configuration file is correct (Instrument.DIC and PortList.DIC contain port numbers; SCU_List.DIC contains IP addresses, port numbers, and application entity (AE) Titles).
3.  Try to ping the affected computer from itself (first try *ping 127.0.0.1* and then try *ping assigned_IP_address*). If either of these attempts fails, the IP settings are mis-configured.

> Chapter 1 DICOM Gateway Error Messages

4.  Check the computer’s IP configuration (utility program ipconfig.exe). Make sure that the computer has a usable IP address, subnet mask and gateway address. Attempt to reach a server or network resource that is known to be operational. Use the *ping* utility to see if network traffic is being routed correctly to the ailing system. Use tracert.exe to further verify the network pathway.
5.  Try to ping the default gateway from the affected computer. If this fails, either the address for the default gateway is not entered, or it is wrong.
6.  Make sure that no other system has the VistA Imaging DICOM Gateway’s IP address. This can be easily checked by disconnecting the ailing system, and then trying to ping its IP address from another location. If there is a response, then obviously another computer is using the same IP address.
7.  Make sure that no other MUMPS system has the same machine name.
8.  Make sure that Microsoft’s Dynamic Host Configuration Protocol (DHCP) is <u>not</u> being used; check that the affected computer has correct Windows Internet Name Service (WINS) and Domain Name System (DNS) information. Make sure that IP addresses of any incoming clients are in the Gateway’s HOSTS table. This will prevent excessive name lookup.
9.  Double-check the values for the subnet mask and the default gateway. If either of these is wrong, the processor may not be able to *see outside* its subnet. As a result, Image Gateways and Workstations may be unable to access either the modalities or the VistA Hospital Information System.
10. Double-check that the TCP/IP protocol is configured properly on the system in question by looking at the network properties. Confirm that TCP/IP is in the list of protocols and verify that it is configured with an IP address and an address for a default gateway. The default gateway must have an address that is on the same subnet as the system itself.
11. Use a utility program like netperf.exe (combined with netserver.exe) to measure the effective speed of the network connection.

## Several Processors Are Affected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When multiple computers are having problems, check the following:

1.  Look for problems with the network or with the router. To see if network traffic is being routed correctly, use the *ping* utility on an affected computer to attempt to reach a server or network resource that is known to be operational.
2.  Check the server(s). Is the domain controller up and running? Is it reachable from the network? Can the server be reached via the network? Are the network interface cards and protocols configured properly?
3.  If it is possible to login into the Windows Domain, but not into VistA, check whether VistA is running and “reachable” via the network.

> Chapter 1 DICOM Gateway Error Messages

4.  On the server, use Server Manager to check Services to make sure that the appropriate services are running.
5.  Check that the information in the appropriate configuration file is correct (Instrument.DIC and PortList.DIC contain port numbers; SCU_List.DIC contains IP addresses, port numbers and AE Titles).
6.  Try to ping the server from any of the affected processors. If this attempt fails, try to *ping*

> *127.0.0.1* on the server to make sure that the server’s IP address and settings are correct. From the server, try to ping its default gateway. From one of the affected stations, try to ping the server’s gateway.

7.  Use the utility program tracert.exe to trace the access route to the server. For example,

> C:\\ipconfig \<Enter\> Windows NT IP Configuration

> Ethernet adapter DC21X41:

> IP Address. . . . . . . . . : 11.22.33.43

> Subnet Mask . . . . . . . . : 255.255.255.0

> Default Gateway . . . . . . : 11.22.33.45 C:\\tracert 11.22.33.45 \<Enter\>

> Tracing route to wciofo-reglwan.eth100.net.va.gov \[11.22.33.45\] over a maximum of 30 hops:

> 1 \<10 ms \<10 ms \<10 ms wciofo-reglwan.eth100.net.va.gov \[11.22.33.45\] Trace complete.

> C:\\

8.  If tracert is not successful, there is most likely a routing problem. Links that are probably down are indicated by asterisks in the report from tracert.
9.  Try using Windows Explorer to see if it is possible to browse to the server. Users with Administrator privileges on the server have access to the *administrative shares*. They could attempt to map a drive to one of these shares. If such attempts fail, it is likely that the WINS/DNS setup is incorrect.

## One or More Windows Show an Error Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One error message that may show up on occasion is *MUMPS length network_read() error: -1*. There are several possible causes for this error message:

- Network error
- Caché console is closed or crashed
- Disk is Full

> Chapter 1 DICOM Gateway Error Messages

> When this error message appears, follow the steps below to find the root-cause of the problem:

- Verify connectivity by PINGing in both directions
- Verify connectivity by executing a DICOM echo
- Check that the Caché Server is still up and running (Caché cube is blue).
- Verify that there is sufficient disk space on the disk that contains the directories

> C:\DICOM\Data1 and C:\DICOM\Image_In

- Check that there is sufficient space in the MUMPS database for normal processing

## PACS Isn’t Sending an Image Complete Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This situation typically comes about when the TCP link with the Picture Archiving and Communications System (PACS) is broken.

> Before attempting to restart any processes, examine the log files to ascertain that the exam complete message is being received from the PACS. The correct C-Move request should be issued by VistA, but response may not be returned from the PACS. Restarting the gateway process for the PACS (1-2-x) usually restores normal functionality

## Other Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Loading Master Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After (re)loading the Master Files, the error message “nnn error(s) encountered while building master files” may appear. When this message appears, it indicates that some error(s) have been found in one or more of the Master Files. The site-modifiable master files are:

- AE_TITLE.DIC
- INSTRUMENT.DIC
- MODALITY.DIC
- PORTLIST.DIC
- SCU_List.DIC
- WORKLIST.DIC

> Check the contents of these files to repair any reported issues.

> See the *MAG\*3.0\*34, MAG\*3.0\*116, and MAG\*3.0\*118 Planning and Installation Instructions*

> for more information about properly formatted specifications in Master Files.

## Multiple Instruments are Configured to Use the Same Port Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging DICOM Gateways should be configured such that each instrument has its own unique port number assigned for communication. When multiple instruments share a port number, only the one that happens to connect first will be able to communicate with its gateway. Any other instrument attempting to use the same port number will cause an error message

> Chapter 1 DICOM Gateway Error Messages

> stating, *Cannot listen to DICOM port because it is already being used*.

> When this happens, verify that there are no conflicts in the master file Instrument.DIC. Reload the master file after it has been corrected.

> When the configuration has been corrected, restart the VistA Imaging DICOM gateway. Just closing and re-starting the modality windows will not have the effect that any ports are released. The Caché Server must be restarted to release all ports.

## Digitized Images Appear Small on the Diagnostic Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The master file Modality.dic contains a parameter that provides a number of settings that influence the conversion from the original file format to TARGA format. See the *MAG\*3.0\*34, MAG\*3.0\*116, and MAG\*3.0\*118 Planning and Installation Instructions* for a complete description of these parameters.

> Pay special attention to the (sub)parameters R1, R2, R4 and R8 that may be used to create a small thumbnail version of the image (also known as an *abstract* or *icon*). When one of these parameters is applied to the conversion of the *full* image, a severe loss of resolution may be the result.

## Digitized Images Appear Dark

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The master file Modality.dic contains a parameter that provides a number of settings that influence the conversion from the original file format to TARGA format. See the *MAG\*3.0\*34, MAG\*3.0\*116, and MAG\*3.0\*118 Planning and Installation Instructions* for a complete description of these parameters.

> Pay special attention to the (sub)parameter Bnnn. When the number of bits specified by this parameter is incorrect, the resulting images may appear with a severely reduced number of gray- values, typically showing extremely dark colors.

## Modality Worklist Find Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The registration of a modality’s AE Title in the master file Worklist.DIC must be an exact match with the string that the modality transmits. This value is case-sensitive.

> After the master file Worklist.DIC has been corrected, verify that the values in the master files Instrument.DIC and Modality.DIC are also correct, and be sure to re-load any modified master files into the database.

## Dictionaries Fail to Load

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When attempted updates or re-initialization of the dictionaries fails to find the .DIC files, another TELNET session may need to be opened to re-establish connectivity, an incorrect dictionary file path may require updating, or a file share permissions problem may need to be addressed..

> Chapter 1 DICOM Gateway Error Messages

## Failover Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is possible to allow a gateway processor to take over the tasks of another, in case one of the gateways should fail. To allow for a smooth *fail-over*, take the following steps:

1.  Add the TCP/IP address of the *failed* gateway to the substitute gateway processor. This will be the *second* IP address on the substitute gateway's Network Interface Card (NIC). Make sure that the failed gateway is taken off of the network.
2.  On the substitute gateway, open the INSTRUMENT.DIC file and add the settings from the INSTRUMENT.DIC on the failed gateway that are not already on the substitute gateway, allowing the substitute gateway to listen on the respective ports. Make sure the hostname (content of the Machine ID field prior to MAG\*3.0\*34) on the end of each line refers to the hostname of the substitute gateway. Once editing is complete, run menu option 4-2-4 Update INSTRUMENT.DIC, and restart Tomcat. The substitute gateway can continue to work for the modalities that already were assigned to that processor.
3.  If the failed gateway is an HDIG and performed extra options (such as, ProcessAsyncStorage, IconImageCreation, and so forth) that the substitute does not perform, then the appropriate settings must be enabled/replicated in the C:\\:\VixConfig\DicomServerConfiguration.config XML file and the PeriodicCommandConfiguration.config file.

> Nothing will have to be changed on the modality configurations. It will be completely *transparent* to the modalities; however, there might be a small performance degradation on the substitute gateway.

## Error Messages from VistA Imaging DICOM Gateway Executable Programs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Messages from MAG_CSTORE.EXE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: This section applies to MAG\*3.0\*99 and earlier image gateways.

> The program MAG_CSTORE.EXE maintains a TCP socket connection with an image acquisition device on one side and with a MUMPS Server on the other side. It processes bi-directional data streams that are encoded according the DICOM standard and causes image files to be stored on its host-PC. It is called with the following parameters:

> Mag_cstore \<IP address\> \<port\> \<modality\> \[\<debug level\>\]

> Parameter Meaning

> IP address For the VistA Imaging DICOM Gateway, this value is always *localhost*.

> Port For the VistA Imaging DICOM Gateway, the port number for the on which the MUMPS Server listens, which is always 60000.

> Modality An abbreviation for the name of the instrument that is sending the images, typically a code like *CR1*, *CT3*, …

> Debug Level A code that indicates the verbosity of debug messages:

> Chapter 1 DICOM Gateway Error Messages

> 0=none, 1=some, 2=lots

> The program MAG_CSTORE.EXE can produce the following error codes:

> Error: Could not connect to the MUMPS storage controller Error in reading PDU header -- connection dropped

> Error in reading dataset -- connection dropped

> Error in writing echo response -- connection dropped Error in reading control dataset -- connection dropped The WinSock initialization has failed

> Error writing control PDU to disk

> Error writing control PDU to DICOM socket Error reading PDV header

> Error reading PDV data, *nnn* bytes input Disk read error in net_write_data() Unknown disk read error in net_write_data() Error writing PDU hdr to socket

> Error writing PDV hdr to socket Error writing DATA PDU to socket select() error in network_read()

> Error in network_read(), total read: *nnn*, errno=*nnn* MS NT Socket Error \#*nnn*

> select() error in network_write()

> Error in network_write(), Error Number: *nnn* Socket initialization error in init_client() Connect error in init_client()

> ioctlsocket() (non-block) error in init_client() ioctl() (non-block) error in init_client() setsockopt(SO_LINGER) error in init_client() socket() error in init_server()

> gethostid() error in init_server() bind() error in init_server

> Could not listen on the DICOM port because it is already in use listen() error in init_server()

> ioctlsocket() (non-block) error in init_server() ioctl() (non-block) error in init_server() select() error in init_server()

> accept() error in init_server() setsockopt(SO_LINGER) error in init_server() MUMPS length network_read() error: *nnn* MUMPS message network_read() error: *nnn* Disk Read error

> Unknown read error

> Write error: number_written= *nnn* count= *nnn*

> Unknown write error

> Error: Incorrect Message *xxx* It should have been *xxx*

> Chapter 1 DICOM Gateway Error Messages

> Error: No additional MUMPS partitions are available Error Reading PDU Header

## Error Messages from MAG_DCMTOTGA.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: This section applies to MAG\*3.0\*99 and earlier image gateways.

> The program MAG_DCMTOTGA.exe reads files that are encoded according to the DICOM standard and produces files in TARGA format. It is called with the following parameters:

> MAG_DCMTOTGA {input filename} {output filename} {parameter(s)}

> Parameter Meaning

> A*nnn* Add *nnn* to each pixel (before min/max check)

> B*nnn*† Number of bits in a pixel (stored in the TARGA header)

> C*nnn* Ceiling (maximum) pixel value (any value \> *nnn* becomes nnn)

> F*nnn* Floor (minimum) pixel value (any value \< *nnn* becomes *nnn*)

> I Invert each pixel

> O*nnn*† Byte offset in DICOM file to image

> R1 Reduce the size of the image file a factor of two (a two-byte 8-bit pixel is stored in one byte, loss-less)

> R2 Reduce the size of the image file a factor of two (a two-byte 16-bit pixel is stored as one byte, usually not loss-less)

> R4 Reduce the size of the image file a factor of four (a square of four 16-bit pixels is averaged and stored in two bytes (16 bits) as one pixel, definitely not loss-less)

> R8 Reduce the size of the image file a factor of eight (a square of four 16-bit pixels is averaged and stored in one byte as one pixel, definitely not loss-less)

> R16 Reduce the size of the image file a factor of sixteen (a square of four by four pixels is averaged and stored in as one pixel, definitely not loss-less)

> R32 Reduce the size of the image file a factor of thirsty-two (a square of sixteen 16-bit pixels is averaged and stored in one byte as one pixel, definitely not loss-less)

> S*nnn* Subtract *nnn* from each pixel (unsigned arithmetic -- before add) X*nnn*† X-dimension of image (horizontal width or number of columns) Y*nnn*† Y-dimension of image (vertical height or number of rows)

> † - Required *nnn* represents an unsigned integer number

> The environment variable MAG_DCMTOTGA_VERBOSE may be used to override the default settings:

> MAG_DCMTOTGA_VERBOSE=1 Selects brief verbose mode MAG_DCMTOTGA_VERBOSE=2 Selects total verbose mode MAG_DCMTOTGA_VERBOSE=3 Turns on density histogram

> The program MAG_DCMTOTGA.exe can produce any of the following error codes:

> -1 End of Input File

> -2 Read Error detected by ferror()

> -3 End of Output File

> -4 Write Error detected by ferror()

> -5 Maximum number of columns exceeded

> -999 Unknown Error

> Chapter 1 DICOM Gateway Error Messages

## Error Messages from MAG_ABSTRTGA.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The program MAG_ABSTRTGA.exe reads files that are encoded in Targa format and produces reduced resolution (thumbnail, abstract) copies of these files. It is called with the following parameters:

> MAG_ABSTRTGA.c {input filename} {output filename} \[/s:x,y\] \[/8\]

> Parameter Meaning

> /s:x,y (Optional) Modify the maximum X and Y dimensions.

> /8 (Optional) Force all black & white (monochrome) pixels to be 8-bits The following environment variables can override the default settings:

> ABSTR_VERBOSE=1 Select verbose mode ABSTR_MAX_X=*nnn* Maximum X dimension is *nnn* ABSTR_MAX_Y=*nnn* Maximum Y dimension is *nnn*

> The program MAG_ABSTRTGA.exe can produce any of the following error codes:

> -1 End of Input File

> -2 Read Error detected by ferror()

> -3 End of Output File

> -4 Write Error detected by ferror()

> -5 Maximum number of columns exceeded

> -999 Unknown Error

## Error Messages from MAG_DCM_COPY.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The program MAG_DCM_COPY.exe is typically called when the DICOM header is being updated either to change from Explicit Value Representation (VR) to Implicit VR or when the values of the attributes are being changed. It is called with the following parameters:

> Mag_dcm_copy {input file} {output file} {input offset} {number of bytes to copy}

> Parameter Meaning

> Offset The byte address where the copy program starts reading

> Number of Bytes The number of bytes to be copied to the output file. (Any information to be copied is appended to the output file.)

> The program MAG_DCM_COPY.exe can produce any of the following error codes:

> -1 End of Input File

> -2 Read Error detected by ferror()

> -3 End of Output File

> -4 Write Error detected by ferror()

> -999 Unknown Error

> Chapter 1 DICOM Gateway Error Messages

## Error Messages from MAG_TGATODCM.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The program MAG_TGATODCM.exe reads files in TARGA format and produces files that are encoded according to the DICOM standard. It is with the following parameters:

> Mag_tgatodcm {input filename} {output filename} {number of bytes to copy}

> The program MAG_TGATODCM.exe can produce any of the following error codes:

> -1 End of Input File

> -2 Read Error detected by ferror()

> -3 End of Output File

> -4 Write Error detected by ferror()

> <span id="1.11_Run_Time_Error_Messages" class="anchor"></span>-999 Unknown Error

## Run Time Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system error log contains a list of any errors that have occurred within the Caché Server. It is good practice to review this log on a regular basis and to report important errors.

> Some entries in the error log are the result of the normal operation of the system and can be ignored.

> The Caché system may issue the following error messages:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;BLOCKNUMBER&gt;</td>
<td><p>A reference has been made to a block outside the range of the</p>
<p>database file.</p></td>
</tr>
<tr class="even">
<td><p>&lt;CANNOT GET THIS</p>
<p>PROPERTY&gt;</p></td>
<td><p>There has been an attempt to get a property of a class for which</p>
<p>getting this property is invalid.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;CANNOT SET THIS</p>
<p>PROPERTY&gt;</p></td>
<td><p>There has been an attempt to set a property of a class for which</p>
<p>setting this property is invalid.</p></td>
</tr>
<tr class="even">
<td>&lt;CLASS COMPILING&gt;</td>
<td><p>There has been an attempt to instantiate a class or invoke a class</p>
<p>method of a class which is currently being recompiled on the local system.</p></td>
</tr>
<tr class="odd">
<td>&lt;CLASS DESCRIPTOR&gt;</td>
<td><p>There has been an attempt to run a routine which is actually a</p>
<p>class descriptor.</p></td>
</tr>
<tr class="even">
<td>&lt;CLASS DOES NOT EXIST&gt;</td>
<td>A reference has been made to a nonexistent class.</td>
</tr>
<tr class="odd">
<td>&lt;CLASS EDITED&gt;</td>
<td><p>There has been an attempt to use an object hosted on the local</p>
<p>system whose class has been recompiled from a remote system since the object was created.</p></td>
</tr>
<tr class="even">
<td>&lt;CLASS RECOMPILED&gt;</td>
<td>There has been an attempt to use an object hosted on the local system whose class has been recompiled on the local system since the object was created.</td>
</tr>
<tr class="odd">
<td><p>&lt;CLASS TOO BIG TO</p>
<p>LOAD&gt;</p></td>
<td><p>A class cannot be used because its class descriptor is too large to</p>
<p>fit into a routine buffer.</p></td>
</tr>
<tr class="even">
<td><p>&lt;CLASS TOO BIG TO</p>
<p>SAVE&gt;</p></td>
<td><p>A class cannot be created because its class descriptor is too large</p>
<p>to fit into a routine buffer.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;CLIENT-SERVER</p>
<p>MISMATCH&gt;</p></td>
<td><p>A network request cannot be processed due to incompatibility</p>
<p>between the client and server.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;CLUSTERFAIL&gt;</td>
<td><p>A cluster member has failed during global buffer lock</p>
<p>processing.</p></td>
</tr>
<tr class="even">
<td>&lt;COLLATEMISMATCH&gt;</td>
<td><p>Subscript level mapping failed due to misconfigured collation</p>
<p>type.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;COLLATION NOT</p>
<p>SUPPORTED&gt;</p></td>
<td><p>A reference has been made to a global whose collation type is</p>
<p>not supported on the current system.</p></td>
</tr>
<tr class="even">
<td>&lt;COMMAND&gt;</td>
<td><p>A command has been used improperly in this context, such as an</p>
<p>argumentless GoTo in a routine.</p></td>
</tr>
<tr class="odd">
<td>&lt;COMMITFAIL&gt;</td>
<td><p>Received during a COMMIT when Caché receives an error while processing a TCommit. This error means that Caché is not sure whether one or more remote machines actually processed the</p>
<p>commit.</p></td>
</tr>
<tr class="even">
<td><p>&lt;CONFLICTING BLOCK</p>
<p>NUMBERS&gt;</p></td>
<td><p>There has been an attempt to reserve a block that was already</p>
<p>reserved.</p></td>
</tr>
<tr class="odd">
<td>&lt;CORRUPT OBJECT&gt;</td>
<td><p>An internal object system error occurred. Contact InterSystems</p>
<p>Worldwide Response Center if this error occurs.</p></td>
</tr>
<tr class="even">
<td>&lt;CORRUPT VOLUME SET&gt;</td>
<td><p>The volume set is corrupted. Usually, this means the label on the</p>
<p>volume set is wrong. Use the ^LABEL utility to correct it.</p></td>
</tr>
<tr class="odd">
<td>&lt;CP NOT STARTED&gt;</td>
<td>One of the major processes required for proper operation of the system failed to start. This is potentially a very serious system error; notify your system manager.</td>
</tr>
<tr class="even">
<td>&lt;DATABASE MAP LABEL&gt;</td>
<td>There is an invalid label in a database map block.</td>
</tr>
<tr class="odd">
<td>&lt;DATABASE&gt;</td>
<td><p>Caché has detected degradation in this database (this is</p>
<p>potentially a very serious system error; notify your system manager).</p></td>
</tr>
<tr class="even">
<td>&lt;DIRECTORY&gt;</td>
<td><p>There is no such directory on the target system, no Caché database, the Caché database is not mounted, or the database is</p>
<p>locked by another configuration.</p></td>
</tr>
<tr class="odd">
<td>&lt;DISCONNECT&gt;</td>
<td><p>A TCP disconnect has been detected while a long-duration</p>
<p>request is being processed.</p></td>
</tr>
<tr class="even">
<td>&lt;DISKHARD&gt;</td>
<td><p>Caché has encountered an uncorrectable disk hardware error (this</p>
<p>may also be the result of a database problem; notify your system manager).</p></td>
</tr>
<tr class="odd">
<td>&lt;DIVIDE&gt;</td>
<td>There has been an attempt to divide by zero.</td>
</tr>
<tr class="even">
<td>&lt;DOMAINSPACERETRY&gt;</td>
<td><p>Repeated attempts to contact the domain space master have</p>
<p>failed.</p></td>
</tr>
<tr class="odd">
<td>&lt;DSCON&gt;</td>
<td>There has been an attempt to read from a disconnected terminal.</td>
</tr>
<tr class="even">
<td>&lt;DYNAMIC LIBRARY LOAD&gt;</td>
<td><p>An error has occurred during an attempt to load a dynamic</p>
<p>library via callout. See cconsole.log for additional information.</p></td>
</tr>
<tr class="odd">
<td>&lt;ECODETRAP&gt;</td>
<td><p>A user-generated software trap was generated by setting the</p>
<p>$ECODE system variable to a non-null string value.</p></td>
</tr>
<tr class="even">
<td>&lt;EDITED&gt;</td>
<td><p>There has been an attempt either (1) to return to an edited routine or edited line, (2) to edit or save a routine was being edited, or</p>
<p>(3) to issue a Use command on a file for the first time after opening it and the routine issuing the Use command has been</p>
<p>edited.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;ENDOFFILE&gt;</td>
<td><p>There has been an attempt to read past the end-of-file marker of a</p>
<p>sequential file.</p></td>
</tr>
<tr class="even">
<td>&lt;FILEFULL&gt;</td>
<td><p>Caché attempted to allocate a disk block for more global data or routine storage, but the attempt failed because the Caché</p>
<p>database is full and could not be expanded.</p></td>
</tr>
<tr class="odd">
<td>&lt;FRAMESTACK&gt;</td>
<td><p>The routine has too many nested calls to Do, For, Xecute,</p>
<p>New, or user-written functions.</p></td>
</tr>
<tr class="even">
<td>&lt;FUNCTION&gt;</td>
<td>The specified function does not exist or is being used improperly.</td>
</tr>
<tr class="odd">
<td>&lt;GARBAGE COLLECTOR FAILED&gt;</td>
<td><p>The one of the processes that reclaims space in the database has failed. This is potentially a very serious system error; notify your</p>
<p>system manager.</p></td>
</tr>
<tr class="even">
<td>&lt;HALTED&gt;</td>
<td>An internal error message.</td>
</tr>
<tr class="odd">
<td>&lt;ILLEGAL VALUE&gt;</td>
<td><p>There has been an attempt to use a negative value where one is</p>
<p>not allowed, such as, for $X or $Y.</p></td>
</tr>
<tr class="even">
<td><p>&lt;INSUFFICIENT CLASS</p>
<p>MEMORY&gt;</p></td>
<td><p>A class cannot be used because Caché has run out of shared</p>
<p>memory.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;INTERNAL OBJECT</p>
<p>ERROR&gt;</p></td>
<td><p>An internal object system error. Contact Intersystem’s</p>
<p>Worldwide Response Center if this error occurs.</p></td>
</tr>
<tr class="even">
<td>&lt;INTERRUPT&gt;</td>
<td><p>A user has interrupted the routine. (In many implementations, the</p>
<p>user has pressed CTRL-C.)</p></td>
</tr>
<tr class="odd">
<td>&lt;INVALID ARGUMENT&gt;</td>
<td><p>There is an invalid argument prototype in the zfentry</p>
<p>specification of a callout function.</p></td>
</tr>
<tr class="even">
<td>&lt;INVALID BIT STRING&gt;</td>
<td>The bit string used in a bit string operation is not valid.</td>
</tr>
<tr class="odd">
<td>&lt;INVALID CLASS&gt;</td>
<td>There has been an attempt to use a class that has been corrupted. Recompile the class and try again.</td>
</tr>
<tr class="even">
<td>&lt;INVALID OREF&gt;</td>
<td>No object with the specified OREF is currently in memory.</td>
</tr>
<tr class="odd">
<td>&lt;INVALID TYPE&gt;</td>
<td>An OREF has been used where not allowed.</td>
</tr>
<tr class="even">
<td>&lt;Java Exception&gt;</td>
<td><p>An exception occurred during a call into the Java runtime</p>
<p>environment.</p></td>
</tr>
<tr class="odd">
<td>&lt;Java VM not loaded&gt;</td>
<td>No Java Virtual Machine is available.</td>
</tr>
<tr class="even">
<td>&lt;LABELREDEF&gt;</td>
<td><p>A routine has a duplicate label within it. Labels must be unique</p>
<p>within the routine.</p></td>
</tr>
<tr class="odd">
<td>&lt;LANGUAGE MISMATCH&gt;</td>
<td><p>While compiling and inserting code into an existing routine, the</p>
<p>current language mode differs from that of the routine.</p></td>
</tr>
<tr class="even">
<td><p>&lt;LICENSE LIMIT</p>
<p>EXCEEDED&gt;</p></td>
<td><p>There has been an attempt to exceed the number of processes</p>
<p>allowed on your system under the current license.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;LICENSE SERVER</p>
<p>UNAVAILABLE&gt;</p></td>
<td><p>The license server is unreachable at the moment. Check your</p>
<p>network.</p></td>
</tr>
<tr class="even">
<td>&lt;LIST&gt;</td>
<td>An improperly-formed list has been used.</td>
</tr>
<tr class="odd">
<td>&lt;LOCKLOST&gt;</td>
<td>Some locks once owned by this job have been reset.</td>
</tr>
<tr class="even">
<td>&lt;LOGIN INHIBITED&gt;</td>
<td>The system is initializing. No users are permitted to begin work.</td>
</tr>
<tr class="odd">
<td>&lt;MAGTAPE&gt;</td>
<td>A magnetic tape operation encountered an error. Check $ZA.</td>
</tr>
<tr class="even">
<td>&lt;MAXARRAY&gt;</td>
<td>There are too many subscripts at this level.</td>
</tr>
<tr class="odd">
<td>&lt;MAXNUMBER&gt;</td>
<td><p>An arithmetic operation has produced a number larger than the</p>
<p>implementation allows.</p></td>
</tr>
<tr class="even">
<td>&lt;MAXSCOPE&gt;</td>
<td><p>There has been an attempt to issue more than 31 levels of New</p>
<p>commands.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;MAXSTRING&gt;</td>
<td><p>There has been an attempt to specify or create a data string</p>
<p>longer than the implementation allows (32,767 characters).</p></td>
</tr>
<tr class="even">
<td><p>&lt;METHOD DOES NOT</p>
<p>EXIST&gt;</p></td>
<td><p>The method does not exist in the specified class or the class of</p>
<p>the specified object.</p></td>
</tr>
<tr class="odd">
<td>&lt;MNEMONICSPACE&gt;</td>
<td><p>There has been an attempt to use control mnemonics for a device</p>
<p>with no associated mnemonic space.</p></td>
</tr>
<tr class="even">
<td>&lt;NAKED&gt;</td>
<td><p>There has been an attempt to use a naked global reference when</p>
<p>the naked state was undefined.</p></td>
</tr>
<tr class="odd">
<td>&lt;NAME&gt;</td>
<td>There is invalid syntax in a name.</td>
</tr>
<tr class="even">
<td>&lt;NAMEADD&gt;</td>
<td><p>There has been an overflow of device name table, resulting from</p>
<p>the Open command.</p></td>
</tr>
<tr class="odd">
<td>&lt;NAMESPACE&gt;</td>
<td>The specified namespace is undefined or not active.</td>
</tr>
<tr class="even">
<td>&lt;NETFORMAT&gt;</td>
<td><p>There has been an error in a network message. The remote</p>
<p>system found fault with the format of a request. Call the CLIN 3 team to resolve this serious error.</p></td>
</tr>
<tr class="odd">
<td>&lt;NETGLOREF&gt;</td>
<td><p>There has been an error in a network message. The remote system found fault with the format of a request. Call the CLIN 3 team to resolve this serious error. (This can also occur if a remote global is a string-collated or 7-bit encoded global on a DSM</p>
<p>system.)</p></td>
</tr>
<tr class="even">
<td>&lt;NETJOBMAX&gt;</td>
<td><p>Another high-speed networking process cannot be added. This is</p>
<p>usually due to an insufficient number of global buffers.</p></td>
</tr>
<tr class="odd">
<td>&lt;NETLOCK&gt;</td>
<td><p>A Caché ObjectScript Lock command has been attempted to a remote computer whose remote system index is greater than 31.</p>
<p>To correct, redefine your network configuration to include fewer than 32 remote computers.</p></td>
</tr>
<tr class="even">
<td>&lt;NETRETRY&gt;</td>
<td>An operation failed at the network level in a way that could be immediately retried.</td>
</tr>
<tr class="odd">
<td>&lt;NETSRVFAIL&gt;</td>
<td><p>During a transaction COMMIT or a Set, Kill, ZKill</p>
<p>command, a client system has detected that one of the servers involved in the transaction has restarted while the transaction</p>
<p>was open. Caché</p></td>
</tr>
<tr class="even">
<td>&lt;NETVERSION&gt;</td>
<td><p>The client and server systems are running different DDP</p>
<p>versions, which cannot accept each other's message format.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>BLOCKNUMBER&gt;</p></td>
<td><p>Updates sent over the network were lost because the remote system attempted to refer to a block that is outside the bounds of</p>
<p>the database; notify your system manager.</p></td>
</tr>
<tr class="even">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - CLIENT- SERVER MISMATCH&gt;</p></td>
<td><p>Updates sent over the network were lost because a network</p>
<p>request could not be processed due to incompatibility between the client and server.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>CLUSTERFAILED&gt;</p></td>
<td>Updates sent over the network were lost because a cluster member failed during global buffer lock processing.</td>
</tr>
<tr class="even">
<td>&lt;NETWORK DATA UPDATE FAILED - DATABASE&gt;</td>
<td><p>Updates sent over the network were lost because Caché on the server has detected degradation in this database. This is potentially a very serious system error; notify your system</p>
<p>manager.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>DIRECTORY&gt;</p></td>
<td>Updates sent over the network were lost because the referenced directory is not on the remote system.</td>
</tr>
<tr class="even">
<td>&lt;NETWORK DATA UPDATE FAILED - DISKHARD&gt;</td>
<td><p>Updates sent over the network were lost because Caché on the server has encountered an uncorrectable disk hardware error. This may also be the result of a database problem; notify your</p>
<p>system manager.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>FILEFULL&gt;</p></td>
<td>In networked operation, a &lt;FILEFULL&gt; error occurred.</td>
</tr>
<tr class="even">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - MAXSTRING&gt;</p></td>
<td>There has been an attempt to specify or create a data string longer than the implementation allows (32,767 characters).</td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>NETFORMAT&gt;</p></td>
<td><p>Updates sent over the network were lost because the remote system found fault with the format of a request. Call the CLIN 3</p>
<p>team to resolve this serious error.</p></td>
</tr>
<tr class="even">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - NETGLOREF&gt;</p></td>
<td><p>Updates sent over the network were lost because the remote</p>
<p>system found fault with the format of a request. Call the CLIN 3 team to resolve this serious error.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - NETVERSION&gt;</p></td>
<td>The client and server systems are running different ECP versions, which cannot accept each other's message format.</td>
</tr>
<tr class="even">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>PROTECT&gt;</p></td>
<td>In networked operation, a &lt;PROTECT&gt; error occurred.</td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - STRINGSTACK&gt;</p></td>
<td>In networked operation, a &lt;STRINGSTACK&gt; error occurred.</td>
</tr>
<tr class="even">
<td><p>&lt;NETWORK DATA</p>
<p>UPDATE FAILED - STRMISMATCH&gt;</p></td>
<td>Updates sent over the network were lost because there has been an internal error handling big strings over the network.</td>
</tr>
<tr class="odd">
<td><p>&lt;NETWORK DATA UPDATE FAILED -</p>
<p>SUBSCRIPT&gt;</p></td>
<td>In networked operation, a &lt;SUBSCRIPT&gt; error occurred.</td>
</tr>
<tr class="even">
<td>&lt;NETWORK DATA UPDATE FAILED - SYSTEM&gt;</td>
<td><p>Updates sent over the network were lost because a &lt;SYSTEM&gt; error occurred on the server. Either there has been an attempt to do something not allowed by the operating system or ECP. Or</p>
<p>there is an error condition in Caché, in which case you should notify the CLIN 3 team with as much information as possible.</p></td>
</tr>
<tr class="odd">
<td>&lt;NETWORK DATA UPDATE FAILED - WIDECHAR&gt;</td>
<td>In networked operation, a &lt;WIDECHAR&gt; error occurred.</td>
</tr>
<tr class="even">
<td>&lt;NETWORK DATA UPDATE FAILED&gt;</td>
<td><p>Updates sent over the network were lost. The reasons for the loss are undetermined. Call the CLIN 3 team to resolve this serious</p>
<p>error.</p></td>
</tr>
<tr class="odd">
<td>&lt;NETWORK&gt;</td>
<td><p>Typically, one of the following has occurred: the network timeout has expired; the local port has gone down; the node being accessed is down; or the remote server connection is</p>
<p>disabled.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;NLS TABLE&gt;</td>
<td><p>There has been an attempt to perform NLS translation using data</p>
<p>that is not proper for the conversion table.</p></td>
</tr>
<tr class="even">
<td>&lt;NO CURRENT OBJECT&gt;</td>
<td>There is no current object.</td>
</tr>
<tr class="odd">
<td>&lt;NO MAILBOX&gt;</td>
<td><p>A resource needed for inter-process communication is</p>
<p>unavailable.</p></td>
</tr>
<tr class="even">
<td>&lt;NO SOURCE&gt;</td>
<td><p>A source line is missing from a routine in the routine source</p>
<p>global.</p></td>
</tr>
<tr class="odd">
<td>&lt;NODEV&gt;</td>
<td><p>There has been an attempt to a write-only device, or write to a</p>
<p>read-only device, with interjob communication.</p></td>
</tr>
<tr class="even">
<td>&lt;NOJOB&gt;</td>
<td><p>There has been an attempt to specify an incorrect process number</p>
<p>in a View command, or an error occurred in a Job command.</p></td>
</tr>
<tr class="odd">
<td>&lt;NOLINE&gt;</td>
<td>There has been an attempt to refer to a nonexistent routine line.</td>
</tr>
<tr class="even">
<td>&lt;NOROUTINE&gt;</td>
<td>There has been an attempt to refer to a nonexistent routine.</td>
</tr>
<tr class="odd">
<td>&lt;NOSYS&gt;</td>
<td><p>There has been an attempt to make an extended or implicit reference to a remote system that is not reachable in the current network configuration. The remote system is not in the tables, or</p>
<p>is a DSM system that has not advertised itself.</p></td>
</tr>
<tr class="even">
<td>&lt;NOT PRIMARY VOLUME&gt;</td>
<td><p>Volume sequence is not 1; the volume label disagrees with the</p>
<p>function of the volume.</p></td>
</tr>
<tr class="odd">
<td>&lt;NOTOPEN&gt;</td>
<td><p>The device cannot be opened, or there has been an attempt to use</p>
<p>an unopened device.</p></td>
</tr>
<tr class="even">
<td>&lt;NULL VALUE&gt;</td>
<td>A null string appears where one is not allowed.</td>
</tr>
<tr class="odd">
<td>&lt;OUT OF $ZF HEAP SPACE&gt;</td>
<td><p>The $ZF heap lacks the necessary available space to support one of the input or output parameters being passed between Caché</p>
<p>and the external program invoked via the $ZF function.</p></td>
</tr>
<tr class="even">
<td>&lt;PARAMETER&gt;</td>
<td><p>The number of parameters passed to a labeled line by a user-</p>
<p>written function reference or a Do command exceeded the number of formal parameters declared for the labeled line.</p></td>
</tr>
<tr class="odd">
<td>&lt;PRIVATE METHOD&gt;</td>
<td><p>There has been an attempt to invoke a private and, therefore,</p>
<p>unavailable method.</p></td>
</tr>
<tr class="even">
<td>&lt;PRIVATE PROPERTY&gt;</td>
<td><p>There has been an attempt to access a private and, therefore,</p>
<p>unavailable property.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;PROPERTY DOES NOT</p>
<p>EXIST&gt;</p></td>
<td>The property is not part of the class of the specified object.</td>
</tr>
<tr class="even">
<td>&lt;PROTECT&gt;</td>
<td><p>There has been an attempt to do something with a global (Read, Write, or Kill) for which there was no authorization; or there has been an attempt to use a View command which modifies memory, $View or $ZUtil(49); or there has been an attempt to use a nonexistent directory, possibly with extended global</p>
<p>syntax, or some other protection violation occurred.</p></td>
</tr>
<tr class="odd">
<td>&lt;RANGE&gt;</td>
<td>A bit position is out of allowable range.</td>
</tr>
<tr class="even">
<td>&lt;READ&gt;</td>
<td>The record cannot be read.</td>
</tr>
<tr class="odd">
<td>&lt;RECOMPILE&gt;</td>
<td><p>A routine has been compiled under a different version of Caché or an Intersystem’s legacy product. It cannot be loaded onto this system with ^%RIMF, which transfers object code. Transfer it as source code (using ^%RO and ^%RI, or the Caché</p>
<p>Explorer) and then recompile it.</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;REMOTE CLASS EDITED&gt;</td>
<td><p>There has been an attempt to use an object hosted on a remote system whose class has been recompiled from a remote system</p>
<p>since the object was created.</p></td>
</tr>
<tr class="even">
<td>&lt;REMOTE CLASS RECOMPILED&gt;</td>
<td><p>There has been an attempt to use an object hosted on a remote</p>
<p>system whose class has been recompiled from the local system since the object was created.</p></td>
</tr>
<tr class="odd">
<td>&lt;ROLLFAIL&gt;</td>
<td><p>Caché has encountered an error processing a call to</p>
<p>TRollBack. This error means that Caché is not sure whether one or more remote machines actually processed the rollback.</p></td>
</tr>
<tr class="even">
<td>&lt;ROUTINELOAD&gt;</td>
<td>An error occurred in loading a routine. This is database degradation; notify the system manager.</td>
</tr>
<tr class="odd">
<td>&lt;SELECT&gt;</td>
<td>A $Select function contains no true condition.</td>
</tr>
<tr class="even">
<td>&lt;SLMSPAN&gt;</td>
<td><p>There has been an attempt to kill a global across a subscript level</p>
<p>mapping boundary.</p></td>
</tr>
<tr class="odd">
<td>&lt;STACK&gt;</td>
<td>The argument stack is out of room or contains an incorrect type.</td>
</tr>
<tr class="even">
<td>&lt;STORE&gt;</td>
<td><p>The partition space for the process is exhausted. The process needs a block larger than the largest contiguous block of available space in the partition. Even though $S may show available space, it is fragmented. Reduce the number or size of the local variables. Utilities may not be available until some variables are deleted in order to free up space. Issuing ZLOAD for too large a routine from a tape or sequential file can also cause</p>
<p>this error.</p></td>
</tr>
<tr class="odd">
<td>&lt;STRINGSTACK&gt;</td>
<td>An expression is too long, there are too many expressions in an argument for a single command, or an expression contains many very long strings. Simplify the expression.</td>
</tr>
<tr class="even">
<td>&lt;STRMISMATCH&gt;</td>
<td><p>There has been an internal error handling big strings over the</p>
<p>network.</p></td>
</tr>
<tr class="odd">
<td>&lt;SUBSCRIPT&gt;</td>
<td><p>A subscript has an illegal value or a global reference is too long. If a global reference is too long, then either (1) the encoded length of an individual subscript exceeds 255 bytes or (2) the sum of the encoded lengths of the following items exceeds 512 bytes: the length of the global name; the lengths of all subscripts; the number of subscripts; the number of numeric subscripts; and</p>
<p>the number of negative numeric subscripts.</p></td>
</tr>
<tr class="even">
<td>&lt;SYNTAX&gt;</td>
<td><p>There is a syntax error (an error in the formation of a language</p>
<p>constructs, such as a misspelled or missing keyword).</p></td>
</tr>
<tr class="odd">
<td>&lt;SYSTEM&gt;</td>
<td><p>Either there has been an attempt to do something not allowed by the operating system, or there is an error condition in Caché, in which case you should notify the CLIN 3 team with as much</p>
<p>information as possible.</p></td>
</tr>
<tr class="even">
<td>&lt;TERMINATOR&gt;</td>
<td><p>There has been an attempt to read on a terminal or device in image mode with no terminator and it was not a fixed-length</p>
<p>read.</p></td>
</tr>
<tr class="odd">
<td>&lt;TOO MANY CLASSES&gt;</td>
<td>This process has attempted to access too many active classes.</td>
</tr>
<tr class="even">
<td>&lt;TOO MANY OREFS&gt;</td>
<td><p>This process has attempted to create too many simultaneously</p>
<p>open objects.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;TOO MANY USERS OF</p>
<p>CLASS&gt;</p></td>
<td><p>Too many processes are trying to use a particular class</p>
<p>simultaneously (more than 65561).</p></td>
</tr>
</tbody>
</table>

> Chapter 1 DICOM Gateway Error Messages

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Caché Error</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;TOO MANY USERS&gt;</td>
<td><p>Too many users are attempting to use the system at the same</p>
<p>time.</p></td>
</tr>
<tr class="even">
<td>&lt;TOOMANYFILES&gt;</td>
<td><p>Caché is unable to open a file because the underlying operating</p>
<p>system has run out of file descriptors.</p></td>
</tr>
<tr class="odd">
<td>&lt;TRANSLATE&gt;</td>
<td><p>Caché has read an input value for which it has no translation value. It therefore carries out the Default Action defined on the</p>
<p>Translation tab of the Caché NLS utility.</p></td>
</tr>
<tr class="even">
<td>&lt;TRANSLOST&gt;</td>
<td><p>A distributed transaction initiated by this job has been</p>
<p>asynchronously rolled back by the server.</p></td>
</tr>
<tr class="odd">
<td>&lt;UNDEFINED&gt;</td>
<td>There has been a reference to an undefined variable.</td>
</tr>
<tr class="even">
<td>&lt;UNIMPLEMENTED&gt;</td>
<td>There has been an attempt to use either an unimplemented function or an unimplemented argument of a legitimate command or function.</td>
</tr>
<tr class="odd">
<td>&lt;UNKNOWN ERROR&gt;</td>
<td><p>An unexpected error has occurred. Call the CLIN 3 team to</p>
<p>resolve this serious error.</p></td>
</tr>
<tr class="even">
<td>&lt;VALUE OUT OF RANGE&gt;</td>
<td><p>The value is outside the maximum or minimum permissible</p>
<p>range.</p></td>
</tr>
<tr class="odd">
<td><p>&lt;VOLUME IS NOT</p>
<p>FORMATTED&gt;</p></td>
<td>The volume does not have the required formatting.</td>
</tr>
<tr class="even">
<td><p>&lt;VOLUME SET ALREADY</p>
<p>CREATED&gt;</p></td>
<td><p>There has been an attempt to format a Caché database that is</p>
<p>already formatted.</p></td>
</tr>
<tr class="odd">
<td>&lt;WIDE CHAR&gt;</td>
<td><p>Caché read a multi-byte character where a 1-byte character was</p>
<p>expected.</p></td>
</tr>
<tr class="even">
<td>&lt;WRITE DEMON FAILED&gt;</td>
<td><p>The write daemon is unable to continue. Call the CLIN 3 team to</p>
<p>resolve this serious error.</p></td>
</tr>
<tr class="odd">
<td>&lt;WRITE&gt;</td>
<td>The record cannot be written.</td>
</tr>
<tr class="even">
<td>&lt;ZFILE&gt;</td>
<td><p>There has been a file-related problem, such as that a file cannot</p>
<p>be found or cannot be opened; consult the error log for more details.</p></td>
</tr>
<tr class="odd">
<td>&lt;ZMISC&gt;</td>
<td><p>An error has occurred of a different type than the others listed in</p>
<p>this table. More detail follows the &lt;ZMISC&gt; code itself.</p></td>
</tr>
<tr class="even">
<td>&lt;ZOPEN&gt;</td>
<td><p>There has been an error opening a device with TCP; the database</p>
<p>server being shadowed is down.</p></td>
</tr>
<tr class="odd">
<td>&lt;ZREAD&gt;</td>
<td><p>There has been a failure to read from the database server that is being shadowed, indicating that the server is disconnected or not</p>
<p>currently running.</p></td>
</tr>
<tr class="even">
<td>&lt;ZSTOP&gt;</td>
<td>Shadowing has been stopped by system shutdown or the user.</td>
</tr>
<tr class="odd">
<td>&lt;ZTRAP&gt;</td>
<td>There has been an attempt to issue a ZTrap command with no argument.</td>
</tr>
</tbody>
</table>

## DICOM Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error message: \$ZE=\<STKOV\>BTXT+2^DIALOG:::6:6:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Problem: This error may occur while attempting to correct images, and while trying to input data into a field that does not exist in the FileMan Data Dictionary on the VistA side.

> Solution: Have site install the latest KIDS application and restart the process images procedure.

> Chapter 1 DICOM Gateway Error Messages

> Note: This error will only occur during the process of corrected images because the exclusive kill does not take place during this process.

## Error Message “Port in Use” or “Port Unavailable”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This message indicates that multiple processes are contending for the same socket. The resolution of this problem is usually fairly simple.

> First try to close the C-Store window that displays the error message. Check that there is no other C-Store session active that is attempting to run the same program for the same instrument. If there is, that other session is probably successfully using the port that the former one could not obtain. If there is no other session attempting to run the same task, try to start it by double- clicking on its icon. This usually resolves the problem.

> If the problem persists, wait until the Image Gateway is not actively processing images (all active windows show the “idle” indicator). Close the windows that display the *idle* indicator one by one. When no more telnet sessions are active, shut down and restart Caché. Once Caché is running again, restart all telnet sessions.

> If, after this, the problem still persists, wait until the Image Gateway is not actively processing images (all active windows show the *idle* indicator). Close the windows that display the *idle* indicator one by one. When no more telnet sessions are active, shut down Caché. Once Caché is shut down, shut down Windows as well. Power down the PC, wait 20 seconds, and power it up again. Restart Windows. Log in using the appropriate username and password and restart Caché. Once Caché is running again, restart all telnet sessions.

> If, after this, the problem still persists, log a Remedy call.

## Dumping Files that Cannot be Processed by the Gateway Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Occasionally, input files cannot be processed properly. The public domain OD.EXE tool, installed on DICOM Gateways in C:\Program Files\VistA\Imaging\DICOM, can be used to diagnose such problems. This utility program is intended to be started from the DOS-prompt, and will accept the following parameters:

- od –b –A {doxn} –N number –j number –t {acdfoux} filename

> The meaning of the various parameters is described below.

## -b

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter means that the content of the file is to be displayed in *bytes* rather than in *words*

> (default, when this parameter is omitted).

## -A {d,o,x,n}

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter indicates how the counter in the left-most column is to be displayed. Only one of the four possible sub-options may be specified:

> Chapter 1 DICOM Gateway Error Messages

> -A d means: display the counter in decimal representation

> -A o means: display the counter in octal representation (default)

> -A x means: display the counter in hexadecimal representation

> -A n means: do not display the counter

## -N number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter indicates how many bytes need to be displayed. Only the first *so many* bytes of the file will be displayed, where *so many* is the number indicated by this parameter.

> Note: The value of this parameter is written in decimal representation.

## -j number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter indicates where in the input file, the program is to start displaying characters. The program will start at the character indicated by the value of *number* in this parameter.

> Note: The value of this parameter is written in decimal representation.

## -t {a,c,d,f,o,u,x}

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When this parameter is omitted, the utility program will only display the numeric values of the various characters in the file. When additional information is desired, this parameter may be used to indicate which additional information should be displayed:

> -t a means: display all ASCII characters

> -t c means: display only printable ASCII characters

> -t d means: display decimal representation

> -t f means: display floating point representation

> -t o means: display octal representation

> -t u means: display unsigned decimal representation

> -t x means: display hexadecimal representation Example:

> C:\DICOM\DICT\>od -N 80 -j 50 -b -A d -t c instrument.dic \<Enter\>

| 0000000050 | 162 | 151 | 160 | 164 | 151 | 157 | 156 | 174 | 111 | 156 | 163 | 164 | 151 | 164 | 165 | 164 |
|------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|            | r   | i   | p   | t   | i   | o   | n   | \|  | I   | n   | s   | t   | i   | t   | u   | t   |
| 0000000066 | 151 | 157 | 156 | 040 | 116 | 141 | 155 | 145 | 174 | 111 | 155 | 141 | 147 | 151 | 156 | 147 |
|            | i   | o   | n   |     | N   | a   | m   | e   | \|  | I   | m   | a   | g   | i   | n   | g   |
| 0000000082 | 040 | 123 | 145 | 162 | 166 | 151 | 143 | 145 | 174 | 120 | 157 | 162 | 164 | 174 | 015 | 012 |
|            |     | S   | e   | r   | v   | i   | c   | e   | \|  | P   | o   | r   | t   | \|  | \r  | \n  |
| 0000000098 | 043 | 040 | 111 | 155 | 141 | 147 | 151 | 156 | 147 | 040 | 163 | 145 | 162 | 166 | 151 | 143 |
|            | \#  |     | I   | m   | a   | g   | i   | n   | g   |     | s   | e   | r   | v   | i   | c   |

> Chapter 1 DICOM Gateway Error Messages

0000000114 145 163 040 141 162 145 040 144 145 146 151 156 145 144 040 141

e s a r e d e f i n e d a

> 0000000130

> C:\DICOM\DICT\>

## Microsoft Windows Error Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In some cases, the system reports an error number. Such error numbers are typically returned by platform-specific system calls. Usually, the software will display both the error code and the meaning. If a code, but no meaning is displayed, the ErrLook program may be of help to find out the meaning of the code.

> ErrLook.exe is stored in the following directory so that is always in an accessible *execution path*: \Program Files\VistA\Imaging\DICOM.

> When this program is started, it asks for an error code number. When a number is entered, click

> Look Up to display the meaning of the code.

![](vista-imaging-error-message-guide/010.png)

> Error message: Cannot create a file when that file already exists.

## Run Time Errors Reported by the DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For ease of use, all of these errors are alphabetically listed in the Index under the heading *Run Time Error*.

## DICOM Association Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These errors are non-recoverable protocol violations on the part of the peer DICOM application entity. They cause both the association and the communications task to be terminated.

> Chapter 1 DICOM Gateway Error Messages

## Unexpected “DATA” PDU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* PDU is out of sequence. \*\*\*

> \*\*\* PDU Type is 04, data. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when an unexpected DICOM message is encountered during the lower-level communication *handshaking* with a peer application entity. (A PDU is a Protocol Data Unit.)

## Peer application entity Requests “Abort Association”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* PDU Type is 07, abort association. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The peer application entity is requesting to terminate the communication. VistA terminates the communications task.

## DICOM Association – Invalid Protocol Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected protocol version 1. \*\*\*

> \*\*\* Found "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The DICOM protocol version is exchanged during the initial negotiation of the association. The only legal DICOM protocol is *Version 1*.

## Opcode for Unsupported Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* No subroutine for opcode: "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR1/3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when an unexpected association sub-item field is presented by a calling application entity negotiating an association with VistA. This is possibly a violation of the DICOM standard. It is a problem that a user cannot resolve and that must be reported to the CLIN 3 team. The error message will include the offending opcode code.

> Chapter 1 DICOM Gateway Error Messages

## DICOM Association – Invalid DICOM Standard UID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected UID for "DICOM Application Context Name", \*\*\*

> \*\*\* which is "1.2.840.10008.3.1.1.1". \*\*\*

> \*\*\* Found "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The DICOM Standard UID is exchanged during the initial negotiation of the association. The only legal value for DICOM is *1.2.840.10008.3.1.1.1*.

## Invalid Context Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Context ID should be an odd number. \*\*\*

> \*\*\* The number encountered is "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> DICOM Presentation Context IDs are odd numbers in the range 1:255. If an even number is presented, it is an error.

> The error message will include the number specified.

## Invalid Sub-Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected sub-type 51(hex) is missing. \*\*\*

> \*\*\* Found "xxxxxxxxxx" instead. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDACR3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The VistA Imaging DICOM Gateway found a *User Information Item Field (Item-type 50H)* in an association request. The user data field must contain Item-type 51H, and did not. The error message will include the incorrect hexadecimal value specified.

> Chapter 1 DICOM Gateway Error Messages

## Illegal Unique Identifier (UID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN DICOM UNIQUE IDENTIFIER DICTIONARY \*\*\*

> \*\*\* \*\*\*

> \*\*\* The UID Dictionary is not properly setup! \*\*\*

> \*\*\* There is no entry in the UID dictionary for "xxxxxxxxxx" \*\*\*

> \*\*\* \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDUID1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The UID dictionary must contain the proper entries in order for the gateway applications to operate properly. This error is probably caused by an old version of the dictionary being loaded. Load the current version.

## Storage Provider Error – Unexpected Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN STORAGE SERVICE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected return value "STORAGE COMPLETE", \*\*\*

> \*\*\* Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDCST1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The C-Store task running in the foreground sent an unexpected message to the MUMPS Storage Controller. It should have sent *STORAGE COMPLETE*. The erroneous text is displayed in the error message.

> This error is fatal and causes the DICOM Storage Provider to terminate.

## Errors Encountered in Reading/Writing DICOM Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Unsupported Value Representation (Input)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Undefined value representation: "xxxxxxxxxx”. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDDR3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur during the reading of a DICOM message. This error occurs when a data element is encountered to have a *value representation* that is not recognized by the VistA Imaging DICOM Gateway software (All legal DICOM value representations are handled by VistA Imaging DICOM Gateway software).

> The error message will contain the code for the offending value representation. The erroneous message will have to be skipped.

> Chapter 1 DICOM Gateway Error Messages

## Value Representation Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR -- WRITING DICOM FILE \*\*\*

> \*\*\* \*\*\*

> \*\*\* VR Mismatch \*\*\*

> \*\*\* Requested Value Representation="xxxxxxxxxx", Dictionary="xxxxxxxxxx". \*\*\*

> \*\*\* Group: xxxxxxxx, Group Owner: xxxxxxxx Element: xxxxxxxx (xxxxxxxxxx) \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDDW3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur when trying to re-generate an Explicit VR image header where the VR specified for an element by a vendor is not in agreement with the DICOM Standard.

> The error message will contain the offending value representation, as well as the list of value representations that is specified in the DICOM Data Dictionary. The error message will include identify the offending element.

## Required Type 1 Data Item Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR -- WRITING DICOM FILE \*\*\*

> \*\*\* \*\*\*

> \*\*\* REQUIRED TYPE 1 DATA MISSING \*\*\*

> \*\*\* Group: xxxxxxxx, Group Owner: xxxxxxxx Element: xxxxxxxx (xxxxxxxxxx) \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDDW3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when a required element’s value is not provided, while formatting a DICOM message. The error message will include identify the offending element.

> This is usually caused by a programming error that a user cannot resolve and that must be reported to the CLIN 3 team.

## Unsupported Value Representation (Output)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR -- WRITING DICOM FILE \*\*\*

> \*\*\* \*\*\*

> \*\*\* ERROR -- Undefined value representation: xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDDW4 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur during the writing of a DICOM message. This error occurs when a data element is encountered to have a *value representation* that is not recognized by the VistA Imaging DICOM Gateway software. (All legal DICOM value representations are handled by VistA Imaging DICOM Gateway software.)

> This is usually caused by a dictionary file or programming error that a user cannot resolve and that must be reported to the CLIN 3 team.

> Chapter 1 DICOM Gateway Error Messages

> The error message will contain the offending value representation.

## Modality Worklist – Invalid SOP Class (C-Find)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN C-FIND \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected SOP Class "Modality Worklist Information Model – FIND \*\*\*

> \*\*\* Found "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDFND1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while processing a C-Find request. As part of the message, the client specifies the name of the Service Object Pair (SOP) class, which defines the context for the entire transaction. This error occurs when the name of this SOP class is not recognized. (Currently, only the SOP class *Modality Worklist Information Model – FIND* is recognized.) This is an error on the part of the application entity that issued the C-Find request.

> The error message will include the name of the class that is specified by the client. This is a fatal error that terminates the association.

## HL7 Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 messages are generated on the main VistA hospital system in the ^MAGDHL7 global. They are read by the Text Gateway and used to update the Modality Worklist database ^MAGDWLST global and to create the DICOM messages that are sent to commercial PACS.

> All of these errors are detected while reading and processing them. Bad HL7 message can be bypassed by incrementing the HL7 pointer.

## Bad HL7 Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY -- HL7 DATA ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Error: BAD HL7 MESSAGE HEADER \*\*\*

> \*\*\* \*\*\*

> \*\*\* HL7 message header should start with "MSH", \*\*\*

> \*\*\* starts with "xxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDHR1/1A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* BAD HL7 MESSAGE HEADER \*\*\*

> \*\*\* \*\*\*

> \*\*\* HL7 message header should start with "MSH", \*\*\*

> \*\*\* starts with "xxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDHRP Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Each HL7 message should start with the prefix *MSH*. These errors will occur when the DICOM Text Gateway detects a message that does not start with this prefix. It indicates a badly garbled

> Chapter 1 DICOM Gateway Error Messages

> message that cannot be further processed.

## Incomplete HL7 Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY -- HL7 DATA ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Incomplete copy of HL7 message encountered. \*\*\*

> \*\*\* In message number “nnn”, \*\*\*

> \*\*\* segment number “mmm” is missing. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDHR2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> A portion of the HL7 message is missing, due to a problem on the main hospital system. The incomplete message will have to be bypassed manually.

## Bad Fillers Order Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY -- HL7 DATA ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* HL7 consult processing detected a bad “Fillers Order \#” \*\*\*

> \*\*\* OBR-3 contained="xxxxxxxxxx". It should have been “GMRC” \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDHR4A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This might occur if the message for the consult/procedure request is incorrectly formatted. Please call the CLIN 3 team.

## DICOM Image Processing Errors During Input

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These errors in processing a DICOM image may indicate database corruption and may require manual intervention. Maybe the image processing pointer can be incremented to bypass offending images until the problem can be resolved.

> When this type of error occurs, it usually indicates a serious database inconsistency. Report it immediately to the CLIN 3 team.

## Undefined Imaging Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Undefined Imaging Service: xxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: MAGDIR81 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error is due to an erroneous Imaging Service field in the INSTRUMENT.DIC file. Legal values are *RAD* and *CON*.

> Chapter 1 DICOM Gateway Error Messages

## File 2005 Corruption Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 87%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>Wed 12:09 DICOM IMAGE PROCESSING ERROR - FILE 2005 CORRUPTION</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The ^MAG(2005) file has been corrupted so that new images will</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>overwrite old ones and general image database inconsistency</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>will result.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Latest internal entry number processed: 102158 Wed SEP 20, at 11:40</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Bad ^MAG(2005,0) internal entry number: 102146</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Routine: MAGDIR84</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image processing task has determined that the most recent internal entry number contained in the ^MAG(2005,0) node has been decremented. This could have been caused by restoring previously saved copy of the ^MAG global without applying the journal files. This is a VERY SERIOUS ERROR since it would allow new images to overwrite old ones, resulting in general corruption of the VistA Imaging database. <span class="mark">REDACTED</span>

## Radiology Report File Corruption Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 88%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>Wed 07:02 DICOM IMAGE PROCESSING ERROR - ^RARPT FILE CORRUPTION</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The RAD REPORT file has been corrupted so that new reports will</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>overwrite old ones and general image/report database inconsistency</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>will result.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Latest internal entry number processed: 77710 SEP 11 at 09:51:39</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Bad ^RARPT(0) internal entry number: 77643</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>This is a VERY SERIOUS ERROR. Image processing</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Routine: ^MAGDIR84</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image processing task has determined that the most recent internal entry number contained in the ^RARPT(0) node has been decremented. This could have been caused by restoring a previously saved copy of the ^RARPT global without applying the journal files. This is a VERY SERIOUS ERROR since it would allow new images to overwrite old ones, resulting in general corruption of the VistA Imaging database. <span class="mark">REDACTED</span>

> Chapter 1 DICOM Gateway Error Messages

## Group Entry Number Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 88%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>Wed 13:07 DICOM IMAGE PROCESSING ERROR - GROUP ENTRY NUMBER PROBLEM</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The internal entry number for this group is less than that of the</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>last processed image. This will cause new images to overwrite</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>old ones and general image database inconsistency will result.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Latest internal entry number processed: 102158 Wed SEP 20, at 11:40</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Bad internal entry number of new group: 102100</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Routine: MAGDIR9A and MAGDIR9E</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has determined that the internal entry number of the new group is less than the most recently created entry. This could have been caused by restoring a previously saved copy of the ^MAG global without applying the journal files. This is a VERY SERIOUS ERROR since it would allow new images to overwrite old ones, resulting in general corruption of the VistA Imaging database. <span class="mark">REDACTED</span>

## Image Entry Number Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 88%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>Wed 12:38 DICOM IMAGE PROCESSING ERROR - IMAGE ENTRY NUMBER PROBLEM</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The internal entry number for this image is less than that of the</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>last processed image. This will cause new images to overwrite</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>old ones and general image database inconsistency will result.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Latest internal entry number processed: 102158 Wed SEP 20, at 11:40</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Bad internal entry number of new image: 102100</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Routine: MAGDIR9B and MAGDIR71</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has determined that the internal entry number of the new image is less than the most recently created entry. This could have been caused by restoring a previously saved copy of the ^MAG global without applying the journal files. This is a VERY SERIOUS ERROR since it would allow new images to overwrite old ones, resulting in general corruption of the VistA Imaging database. <span class="mark">REDACTED</span>

> Chapter 1 DICOM Gateway Error Messages

## Imaging Patient Mismatch Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* Wed 12:53 DICOM IMAGE PROCESSING ERROR - PATIENT MISMATCH PROBLEM \*\*\*

> \*\*\* \*\*\*

> \*\*\* The image and the group point to different patients. \*\*\*

> \*\*\* \*\*\*

> \*\*\* The Image points to PATIENT file internal entry number 100 \*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 44%" />
<col style="width: 43%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p>
<p>*</p></th>
<th><blockquote>
<p>IMAGPATIENT1,ONE | 000-05-6789 |</p>
<p>The Group points to PATIENT file</p>
</blockquote></th>
<th><p>M | Dec 25,1925</p>
<p>internal entry number 90271</p></th>
<th><blockquote>
<p>*</p>
<p>*</p>
<p>*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*</p>
<p>*</p></td>
<td><blockquote>
<p>IMAGPATIENT2,TWO | 000-05-4321 |</p>
</blockquote></td>
<td>F | Oct 31,1919</td>
<td><blockquote>
<p>*</p>
<p>*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>*</td>
<td colspan="2"><blockquote>
<p>Internal entry number of group: 102138</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>*</p>
<p>*</p>
<p>*</p></td>
<td colspan="2"><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
<p>This is a VERY SERIOUS ERROR. Image processing</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
<p>*</p>
<p>*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>*</p>
<p>*</p>
<p>*</p>
<p>*</p>
<p>*</p></td>
<td colspan="2"><blockquote>
<p>will be halted until it is resolved.</p>
<p><mark>REDACTED</mark> Routine: MAGDIR9A, MAGDIR9B, and MAGDIR9E</p>
</blockquote></td>
<td><blockquote>
<p>*</p>
<p>*</p>
<p>*</p>
<p>*</p>
<p>*</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has determined that the image and the group entries would point to different patients. An unknown software problem or manual modification of the data could have caused this to occur. This is a VERY SERIOUS ERROR since it might lead to a corrupted VistA Imaging database. <span class="mark">REDACTED</span>

## Radiology Patient Mismatch Problem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* Mon 06:50 DICOM IMAGE PROCESSING ERROR - RAD PATIENT/REPORT MISMATCH \*\*\*

> \*\*\* \*\*\*

> \*\*\* The image and the radiology report point to different patients. \*\*\*

> \*\*\* \*\*\*

> \*\*\* The Image points to PATIENT file internal entry number 90263 \*\*\*

> \*\*\* IMAGPATIENT,ONE M. \| 000-01-9676 \| M \| Dec 25,1925 \*\*\*

> \*\*\* \*\*\*

> \*\*\* The Rad Report points to PATIENT file internal entry number \#17 \*\*\*

> \*\*\* IMAGPATIENT,TWO N. \| 000-02-7748 \| F \| Oct 31,1919 \*\*\*

> \*\*\* \*\*\*

> \*\*\* Internal entry number of report: ^RARPT(12345) \*\*\*

> \*\*\* Image Gateway: "VistA DICOM Gateway Development System" \*\*\*

> \*\*\* \*\*\*

> \*\*\* This is a VERY SERIOUS ERROR. Image processing \*\*\*

> \*\*\* will be halted until it is resolved. \*\*\*

> \*\*\* \*\*\*

> \*\*\* <span class="mark">REDACTED</span> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: MAGDIR9A \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has determined that the image and the radiology report entries would point to different patients. An unknown software problem or manual modification of the data could have caused this to occur. This is a VERY SERIOUS ERROR since it might lead to a corrupted VistA Imaging and/or Radiology database. REDACTED

> Chapter 1 DICOM Gateway Error Messages

## No Radiology Case Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* No radiology case number specified for patient xxxxxxxxxx \*\*\*

> \*\*\* Routine: ^MAGDIR9A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> A database inconsistency may exist in the Radiology package. There should be a radiology case number specified for this patient. Perhaps the case has been deleted. The DICOM Image Input pointer can be incremented to temporarily get around this problem.

## Radiology Case Not in ^RADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* Radiology case xxxxx is not in ^RADPT(yyyyyyyy) \*\*\*

> \*\*\* Routine: ^MAGDIR9A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The entry in the Radiology Patient File (^RADPT) for this case number appears to be missing. This may be due to a database inconsistency in the Radiology package. Perhaps the case has been deleted. The DICOM Image Input pointer can be incremented to temporarily get around this problem.

## Cannot Create Group for Old Radiology Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* IMAGE GROUP CREATION ERROR: \*\*\*

> \*\*\* Radiology Report has been archived and purged. \*\*\*

> \*\*\* Patient xxxxxxxxxx, Date xxxxxxxxxx, Case xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR9A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while attempting to enter information into the VistA database to establish a group of images. This error happens when the image files are for a Radiology study whose reports already have been archived and purged, as may happen when films are scanned in for *old* studies.

## Cannot Create Group for New Radiology Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* IMAGE GROUP CREATION ERROR: \*\*\*

> \*\*\* xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR9A & ^MAGDIR9E Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while attempting to create a radiology image group in the VistA database.

> Chapter 1 DICOM Gateway Error Messages

## Cannot Find Image Group Pointer in Radiology Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* IMAGE GROUP LOOKUP ERROR: \*\*\*

> \*\*\* Looking for 2005 cross reference in ^RARPT(xxxxxxxxxx) \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR9A Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while attempting to access a radiology image group in the VistA database.

## Cannot Create Image File Entry in VistA Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* IMAGE FILE CREATION ERROR: \*\*\*

> \*\*\* xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR9B Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while attempting to create the image entry in the VistA database.

## Cannot Create Subdirectory to Store Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* IMAGE FILE SUBDIRECTORY CREATION ERROR \*\*\*

> \*\*\* Cannot create the image subdirectory “xxxxxxxxxx” \*\*\*

> \*\*\* xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR71 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Images are stored in a hierarchy of subdirectories. This error may occur when the creation of a new subdirectory. The error message will contain the name of the directory that failed to be created. Check that the network file server is still *reachable*. Try to map a network drive to it and manually create the subdirectory using the command prompt.

> Chapter 1 DICOM Gateway Error Messages

## Cannot Write Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* The writing of image file "xxxxxxxxxx" failed \*\*\*

> \*\*\* The error message was "xxxxxxxxxx" \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> When an image is stored on the network file server, the software checks whether the size of the created file is greater than zero. This error message is reported if the newly created file is either not created or has a zero size. Check that the network file server is still “reachable”. Try to map a network drive to it and manually copy a file using the command prompt.

> Try the following steps to correct this problem:

1.  From a DOS session, copy a small file to the share using the UNC path and file name for the destination. If the write fails it is usually caused by permission problems. Fix the permission problem using the Windows user administration tools (if necessary, find a System Administrator who has the appropriate privileges).
2.  Check the available disk space on the share. If the disk space is low, run a purge on the background processor to free up space on the magnetic shares.

## TIU Note Patient/Report Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 89%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>Mon 06:50 DICOM IMAGE PROCESSING ERROR - TIU PATIENT/REPORT MISMATCH</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The image and the TIU note point to different patients.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The Image points to PATIENT file internal entry number 90263</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>IMAGPATIENT,ONE M. | 000-01-9676 | M | Dec 25,1925</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>The TIU note points to PATIENT file internal entry number #17</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>IMAGPATIENT,TWO N. | 000-02-7748 | F | Oct 31,1919</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Internal entry number of TIU note: ^TIU(8925,1)</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>Routine: MAGDIR9E</td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has determined that the image and the Text Integration Utility (TIU) note entries would point to different patients. An unknown software problem or manual modification of the data could have caused this to occur. This is a VERY SERIOUS ERROR since it might lead to a corrupted VistA Imaging and/or TIU Note database. REDACTED

> Chapter 1 DICOM Gateway Error Messages

## TIU External Data Link Association Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>ERROR ASSOCIATING WITH TIU EXTERNAL DATA LINK (file 8925.91)</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>&lt;error message from TIU&gt;</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Image Gateway: "VistA DICOM Gateway Development System"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>This is a VERY SERIOUS ERROR. Image processing</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td>Routine: MAGDIR9E and MAGDHWA</td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The image-processing task has encountered an error in attempting to create an association between the image and the TIU External Data Link. An unknown software problem or manual modification of the data could have caused this to occur. This is a VERY SERIOUS ERROR since it might lead to a corrupted VistA Imaging and/or TIU Note database. REDACTED

## Cannot Find Table with Additional Data Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Data transfer dictionary \<\<xxxxxxxxxx\>\> is missing \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The error message will include the name of the missing table.

> This error may occur when the designated data transfer dictionary cannot be found. This is probably either a configuration or an installation problem.

> The data transfer dictionaries are DataGECT.DIC, Data_CR.DIC, and DataMisc.DIC, all of which should be in the f:\DICOM\Dict subdirectory. The Modality.DIC file should contain the names of the data transfer dictionaries.

> The missing data transfer dictionary will be created when the information from master file F:\DICOM\Dict\Modality.DIC is reloaded into the database of the VistA Imaging DICOM Gateway (use menu option 4-2-5, Update MODALITY.DIC).

> If the file(s) in directory F:\DICOM\Dict are also missing, these can be re-copied from the distribution medium (either CD-ROM or network).

> Chapter 1 DICOM Gateway Error Messages

## DICOM Element has Too Many Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Processing "xxxxxxxxxx", tag is "xxxxxxxxxx". \*\*\*

> \*\*\* Multiplicity is "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while building the set of data elements that is to be displayed on a diagnostic workstation. Within the DICOM protocol, each data item may have 0 (zero) or more values. How many values a specific data item may have is defined in the DICOM Data Dictionary. When a data item is encountered that has more actual values than the maximum defined in the DICOM Data Dictionary, this error will occur.

> The error message will identify the data stream being processed, the *tag* for the data item in question, and the actual number of values.

## Cannot Create Targa File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* TARGA IMAGE FILE CREATION ERROR \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* ... host system error message(s) ... \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation of the Targa file for an image. The actual display will include the error message that was produced by the host operating system.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started.

## Cannot Create Abstract File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* DICOM IMAGE ABSTRACT CREATION ERROR \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* ... host system error message(s) ... \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation of the *abstract* file (also known as thumbnail or icon) for an image. The actual display will include the error message that was produced by the host operating system.

> Chapter 1 DICOM Gateway Error Messages

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started.

## No Image File Created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY *\<type\>* IMAGE FILE (1) \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* Temporary TGA file *\<name\>* not in the directory \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation of an image file (Targa file, abstract file, etc.). The actual display will include the error message that was produced by the host operating system.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started.

> This particular error is most likely the result of a *disk full* or *privilege not granted* condition. Check that the disk share is still accessible through the network, check that the disk has enough free space to store new files, and check that the current user has appropriate credentials to execute the task at hand.

## Error while Creating Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY *\<type\>* IMAGE FILE (2) \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* Error *\<message\>* for temporary *\<type\>* file *\<name\>* \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation an image file (Targa file, abstract file, etc.). The actual display will include the error message that was produced by the external program.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started

> This particular error is most likely the result of a *disk full* or *privilege not granted* condition. Check that the disk share is still accessible through the network, check that the disk has enough free space to store new files, and check that the current user has appropriate credentials to execute the task at hand.

> Chapter 1 DICOM Gateway Error Messages

## Could not Copy Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\\<type\>* IMAGE COPY ERROR \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* ... host system error message(s) ... \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command to copy an image file, an error occurred that prevented the proper creation of the copied file. The actual display will include the error message that was produced by the host operating system.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started.

## Could not Create Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* The writing of the image file failed. \*\*\*

> \*\*\* Path: "*\<name\>*" \*\*\*

> \*\*\* The error message was "*\<message\>*" \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation an image file (Targa file, abstract file, etc.). The actual display will include the error message that was produced by the external program.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started

> This particular error is most likely the result of a *disk full* or *privilege not granted* condition. Check that the disk share is still accessible through the network, check that the disk has enough free space to store new files, and check that the current user has appropriate credentials to execute the task at hand.

> Chapter 1 DICOM Gateway Error Messages

## Image File Created, but File Size not Greater than 0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* The writing of the image file failed. \*\*\*

> \*\*\* Path: "*\<name\>*" \*\*\*

> \*\*\* Size of written file is *\<number\>* bytes. \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation an image file (Targa file, abstract file, etc.). The actual display will include the error message that was produced by the external program.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started

> This particular error is most likely the result of a *disk full* or *privilege not granted* condition. Check that the disk share is still accessible through the network, check that the disk has enough free space to store new files, and check that the current user has appropriate credentials to execute the task at hand.

## Image File Created, but Size Differs from Expected File Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY *\<type\>* IMAGE FILE (3) \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* Temporary *\<type\>* file *\<name\>* has ZERO LENGTH \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation an image file (Targa file, abstract file, and so on). The actual display will include the error message that was produced by the external program.

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started.

> Chapter 1 DICOM Gateway Error Messages

## Image File Created, but File Size Differs from Expected File Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* The writing of the image file failed. \*\*\*

> \*\*\* Path: "*\<name\>*" \*\*\*

> \*\*\* Size of written file is *\<wrong number\>* -- should be *\<correct number\>* \*\*\*

> \*\*\* Imaging entry *\<number\>* successfully removed \*\*\*

> \*\*\* MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command, an error occurred that prevented the proper creation an image file (Targa file, abstract file, and so on). The display will include the error message that was produced by the external program. When the file size on the source (the Imaging Gateway) and destination (Imaging Server) are different, the Processing on the Gateway will halt, with error messages provided through an e-mail message sent to a designated mail group and include a recipient in the <span class="mark">REDACTED</span>

> Information about the image was successfully removed from the VistA database, and a new attempt to process the image can be started

> This particular error is most likely the result of a problem in the site’s local area network. When the size of the newly created file is reported as being approximately equal to 57kB, it is very likely that a gigabit Ethernet card has failed.

## Could not Delete Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* ERROR DELETING *\<type\>* \*\*\*

> \*\*\* Unexpected error in *\<host system command\>* \*\*\*

> \*\*\* ... *host system error message(s)* ... \*\*\*

> \*\*\* MAGDIR71 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> While executing a host operating system command to delete an image file, an error occurred that prevented the proper deletion of that file. The actual display will include the error message that was produced by the host operating system.

## Cannot find Table with Additional Data Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Data transfer dictionary *\<\<xxxxxxxxxx\>\>* is missing \*\*\*

> \*\*\* \*\*\*

> \*\*\* MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The error message will include the name of the missing table.

> Chapter 1 DICOM Gateway Error Messages

> This error may occur when the designated data transfer dictionary cannot be found. This is probably either a configuration or an installation problem.

> The data transfer dictionaries are DataGECT.DIC, Data_CR.DIC, and DataMisc.DIC, all of which should be in the f:\DICOM\Dict subdirectory. The Modality.DIC file should contain the names of the data transfer dictionaries.

> The missing data transfer dictionary will be created when the information from master file F:\DICOM\Dict\Modality.DIC is reloaded into the database of the VistA Imaging DICOM Gateway (use menu option 4-2-5, Update MODALITY.DIC).

> If the file(s) in directory F:\DICOM\Dict are also missing, these can be re-copied from the distribution CD-ROM.

> Chapter 1 DICOM Gateway Error Messages

## Image Patient Mismatch (parent file 2006.5839)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 85%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR – IMAGE GROUP MISMATCH</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>The image group does not point to PARENT FILE 2006.5839.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>The image group should point to PARENT FILE 2006.5839.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Instead it point to PARENT FILE #nnnnnn</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>The image group is ^MAG(2005,nnnnnn)</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Routine: MAGDIR9E</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Image and TIU Note Associated with different Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 85%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>*</th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR – TIU/IMAGE GROUP MISMATCH</p>
</blockquote></th>
<th>*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>The image group and TIU point to different notes.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>TIU points to TUI note ien #nnnnnn</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>The image points to TIU note ien #nnnnnn</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>TIU External Data File (8925.91) ien #nnnnnn</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>points to image group ien #nnnnn</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Routine: MAGDIR9E</p>
</blockquote></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Wrong Group Object Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR – WRONG GROUP OBJECT TYPE \*\*\*

> \*\*\* The group entry in ^MAG(2005) does not have the proper group \*\*\*

> \*\*\* object type. \*\*\*

> \*\*\* \*\*\*

> \*\*\* The expected value is 11. The value in the group entry is nnnnnn. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Internal entry number of incorrect group: nnnnnn \*\*\*

> \*\*\* \*\*\*

> \*\*\* This is a VERY SERIOUS ERROR. Image processing \*\*\*

> \*\*\* will be halted until it is resolved. \*\*\*

> \*\*\* \*\*\*

> \*\*\* <span class="mark">REDACTED</span> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: MAGDIR9B \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Ignore Image File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* Image \<filename\> will be ignored. \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Unknown Instrument Mnemonic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* Image nnnnn has an unknown instrument mnemonic "xxx" skipped \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Rename Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* Renaming oldname to newname failed. \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.37_Image_File_Creation_Error" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Image File Creation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 87%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p></th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR</p>
</blockquote></th>
<th><blockquote>
<p>*</p>
<p>*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>IMAGE FILE CREATION ERROR:</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>&lt;error message&gt;</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Gateway: "&lt;name&gt;"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>This is a VERY SERIOUS ERROR. Image processing</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Problem detected by routine MAGDIR71.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
</tbody>
</table>

> <span id="1.15.6.38_Image_File_Subdirectory_Creati" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Image File Subdirectory Creation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 75%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p></th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR</p>
</blockquote></th>
<th><p>*</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>IMAGE FILE SUBDIRECTORY CREATION ERROR</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Cannot create the image subdirectory "name"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>&lt;error message&gt;</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Imaging entry #nnnnn was successfully removed.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## New Files Might Overwrite Existing Ones (Single)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 89%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p></th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR</p>
</blockquote></th>
<th><p>*</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>IMAGE FILE CREATION ERROR - NEW FILES MIGHT OVERWRITE EXISTING ONES</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Trying to create file:</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>"filename"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>However, this file already exists in that directory:</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>"filename"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Cannot overwrite this with the image files.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Imaging entry #nnnnn was successfully removed.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Gateway: "&lt;name&gt;"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Problem detected by routine MAGDIR71.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
</tbody>
</table>

> <span id="1.15.6.40_New_Files_Might_Overwrite_Exis" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## New Files Might Overwrite Existing Ones (Multiple)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 89%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p></th>
<th><blockquote>
<p>DICOM IMAGE PROCESSING ERROR</p>
</blockquote></th>
<th><p>*</p>
<p>*</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>IMAGE FILE CREATION ERROR - NEW FILES MIGHT OVERWRITE EXISTING ONES</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Trying to create file:</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>"filename"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>However, these nnn files already exist in that directory:</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>"filename"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>. . .</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>"filename"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Cannot overwrite these with the image files.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Gateway: "&lt;name&gt;"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td>This is a VERY SERIOUS ERROR. Image processing</td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Problem detected by routine MAGDIR71.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Cannot Delete File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* ERROR DELETING xxx \*\*\*

> \*\*\* Unexpected error in \<command\> \*\*\*

> \*\*\* \<error message\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR71 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.42_Unknown_Status_(Patient_Safety" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Unknown Status (Patient Safety RPC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 87%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><p>*</p>
<p>*</p></th>
<th><blockquote>
<p>UNKNOWN STATUS IN "PATIENT SAFETY" RPC RESULT</p>
</blockquote></th>
<th><blockquote>
<p>*</p>
<p>*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>Status = "&lt;status&gt;"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Gateway: "&lt;name&gt;"</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>This is a VERY SERIOUS ERROR. Image processing</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p>will be halted until it is resolved.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
<tr class="even">
<td>*</td>
<td><blockquote>
<p>Problem detected by routine MAGDIR74.</p>
</blockquote></td>
<td>*</td>
</tr>
<tr class="odd">
<td>*</td>
<td></td>
<td>*</td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Rollback Error (number of returned elements)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* ROLLBACK M-to-M RPC BROKER ERROR \*\*\*

> \*\*\* Unexpected number of array elements returned by RPC: nnn \*\*\*

> \*\*\* \<result text\> \*\*\*

> \*\*\* . . . \*\*\*

> \*\*\* \<result text\> \*\*\*

> \*\*\* Only one element ("ROLLBACK") should be returned \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.44_Rollback_error_(returncode)" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Rollback error (returncode)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* ROLLBACK M-to-M RPC BROKER ERROR \*\*\*

> \*\*\* Unexpected return from RPC: "\<returncode\>" \*\*\*

> \*\*\* Expected "ROLLBACK\|STATUS\|IMAGEPTR" \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Problem with Temporary File (1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY \<type\> IMAGE FILE (1) \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* Temporary TGA file "\<filename\>" not in the directory \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.46_Problem_with_Temporary_File_(2" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Problem with Temporary File (2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY \<type\> IMAGE FILE (2) \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* Error "\<text\>" for temporary \<type\> file "\<filename\>" \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Problem with Temporary File (3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* DIRECTORY PROBLEM WITH TEMPORARY \<type\> IMAGE FILE (3) \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* Temporary \<type\> file "\<filename\>" has ZERO LENGTH \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Image Copy Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* \<type\> IMAGE COPY ERROR \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* \<error message\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Image Write Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* The writing of image file failed. \*\*\*

> \*\*\* Path: "\<filename\>" \*\*\*

> \*\*\* \<error message\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR75 Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.50_Targa_Abstract_Creation_Error" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Targa Abstract Creation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* TARGA IMAGE ABSTRACT CREATION ERROR \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* \<error message\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.51_Multiframe_Image_File_Creation" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Multiframe Image File Creation Error (number of returned elements)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* MULTIFRAME IMAGE FILE CREATION ERROR \*\*\*

> \*\*\* Unexpected number of array elements returned by RPC: nnn \*\*\*

> \*\*\* Element 1) \<text\> \*\*\*

> \*\*\* . . . \*\*\*

> \*\*\* Element n) \<text\> \*\*\*

> \*\*\* Two elements (PROCESSED and STORE) should be returned \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Multiframe Image File Creation Error (return code not “processed”)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* MULTIFRAME IMAGE FILE CREATION ERROR \*\*\*

> \*\*\* Unexpected return from RPC: "\<text\>" \*\*\*

> \*\*\* Expected "PROCESSED\|location\|instname\|imageptr\|0" \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.53_Multiframe_Image_File_Creation" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Multiframe Image File Creation Error (return code not “store”)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* MULTIFRAME IMAGE FILE CREATION ERROR \*\*\*

> \*\*\* Unexpected return from RPC: "\<text\>" \*\*\*

> \*\*\* Expected "STORE\|0\|imageptr^topath^file" \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7C Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Multiframe Image File Creation Error (error in command)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE ABSTRACT CREATION ERROR \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* 1) \<text\> \*\*\*

> \*\*\* . . . \*\*\*

> \*\*\* n) \<text\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7D Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Targa File Creation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* TARGA IMAGE FILE CREATION ERROR \*\*\*

> \*\*\* Unexpected error in "\<command\>" \*\*\*

> \*\*\* 1) \<text\> \*\*\*

> \*\*\* . . . \*\*\*

> \*\*\* n) \<text\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7G Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Could not Open Image File for Write

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* Could not open about image text file "\<filename\>" for Write. \*\*\*

> \*\*\* STATUS: \<xxx\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Imaging entry \#nnnnn was successfully removed. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Data Transfer Dictionary Missing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Data transfer dictionary \<\<*filename*\>\> is missing \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> <span id="1.15.6.58_Invalid_Multiplicity" class="anchor"></span>\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Invalid Multiplicity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Processing "\<*node*\>", tag is "\<*tag*\>". \*\*\*

> \*\*\* Multiplicity is "*nnn*". \*\*\*

> \*\*\* \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIR7T Please Call Support Personnel \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Chapter 1 DICOM Gateway Error Messages

## Routing Not Actively Used

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM IMAGE PROCESSING ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* More than a week has elapsed since dd-Mon-yyyy \*\*\*

> \*\*\* when the last activity occurred that is related \*\*\*

> \*\*\* to the processing of Routed Image files. \*\*\*

> \*\*\* \*\*\*

> \*\*\* The site parameter for "This is a Routing Site" is \*\*\*

> \*\*\* currently turned ON. \*\*\*

> \*\*\* If this site is no longer actively routing image files \*\*\*

> \*\*\* this site parameter must be turned OFF. \*\*\*

> \*\*\* This parameter needs to be turned OFF on each VistA \*\*\*

> \*\*\* DICOM Gateway that processes incoming images. \*\*\*

> \*\*\* \*\*\*

> \*\*\* There are currently nnn entries \*\*\*

> \*\*\* waiting to be processed in the evaluation queue. \*\*\*

> \*\*\* \*\*\*

> \*\*\* There are currently nnn entries \*\*\*

> \*\*\* waiting to be processed in the transmission queue. \*\*\*

> \*\*\* \*\*\*

> \*\*\* If this site is still a routing site, then both the \*\*\*

> \*\*\* Routing Rule Evaluator and the Routing Transmitter \*\*\*

> \*\*\* must be restarted. \*\*\*

> \*\*\* Problem detected by routine MAGDIR82. Error Code: -405 \*\*\*

> \*\*\* \*\*\*

> \*\*\* MAGDIR72 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This message will appear (once per day) when a DICOM Gateway is processing images, and the setting for Routing Active is turned on, while no files have been routed or no rule-evaluation has taken place for over a week.

> When the setting for Routing Active is turned on, an entry will be created in the Routing Rule Evaluation Queue for each image that is processed. If no rule-evaluator is running, this queue will grow and eventually fill any available storage space. (When a rule-evaluator is running, queue entries will be deleted after they have been processed.)

> The action to be taken will depend on the situation at the site: if it is intentional that routing rule evaluation and file transmission is no longer active, then the setting for Routing Active should be turned off.

> When Routing is intended to be active, the rule-evaluator and file transmitter(s) should be restarted.

## Cannot Create Abstract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For some image files, the DICOM Gateway may be unable to create an *abstract* file. When this happens, the message stream on the Image Gateway will contain text like:

> Chapter 1 DICOM Gateway Error Messages

> ...

> MAG_MAKEABS c:\DICOM\IMAGE_IN\Y0000138.DCM c:\DICOM\IMAGE_IN\TMP_IMAGE.ABS JPEG 100

> HDR c:\DICOM\IMAGE_IN\MAG_MAKEABS_msg.txt & TYPE c:\DICOM\IMAGE_IN\MAG_MAKEABS_msg.txt

1.  1^Failure Processing Image - Abstract Not Created

> ...

> Since these messages are likely to scroll off the monitor without being noticed, an e-mail message is also sent. The contents of such a message will look like:

> DICOM IMAGE ABSTRACT CREATION ERROR

> Error reported by MAG_MAKEABS in creating the image abstract: Image number \# nnnnnnn.

> 1^Failure Processing Image - Abstract Not Created Routine: MAGDIR7D

> <span id="1.15.7_DICOM_Image_Processing_Errors_Dur" class="anchor"></span>DICOM Gateway "Non-DDP Test System (Y)".

## DICOM Image Processing Errors During Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Images are internally stored in Targa file format with an *about image text file*, which contains an ASCII version of the DICOM Header. When DICOM images are to be sent to another application entity, the DICOM images are *reconstituted* from the Targa image files and the text files, and are then sent.

> Like the VistA DICOM Storage Provider architecture, two processes are used to send a DICOM image, the MUMPS Transmission Controller and the C executable MAG_VISTA_SEND_IMAGE.exe.

> The MUMPS Transmission Controller has managerial responsibilities for the effort and spawns the MAG_VISTA_SEND_IMAGE.exe program to transmit the actual image files. The two processes communicate with each other via TCP/IP, with the MUMPS routine instructing the C program with what to do.

## Bad Targa File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Bad Targa File -- xxxxxxxxxx \*\*\*

> \*\*\* Neither RGB color, nor gray scale. \*\*\*

> \*\*\* Image Type is "xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error may occur while re-constituting a DICOM file from a Targa file and a Text file. In the Targa file, a code occurs that indicates the internal *image type*. Currently, only image types gray scale and RGB color are supported. When a file with a different image type is encountered, this error will occur.

> Chapter 1 DICOM Gateway Error Messages

## Cannot Establish Connection with MAG_VISTA_SEND_IMAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected return value "Connection established to MUMPS". \*\*\*

> \*\*\* Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW5 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> When the MAG_VISTA_SEND_IMAGE.exe program is spawn by the MUMPS Transmission Controller (^MAGDIW5), it tries to establish a TCP/IP connection back to the MUMPS controller task. This error message denotes that this communications failed.

## Connection to Destination Storage Provider Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected return value "CONNECTION SUCCESSFUL". \*\*\*

> \*\*\* Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW5 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The MAG_VISTA_SEND_IMAGE.exe program to attempts to create a TCP/IP connection to the destination Storage Provider application entity. This connection could not be created.

## Could Not Establish Association with Destination SCP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected return value "ASSOCIATION ACKNOWLEDGE". \*\*\*

> \*\*\* Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW6 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The MUMPS Transmission Controller created an Association Request and had the MAG_VISTA_SEND_IMAGE.exe program send it to the destination Storage Service Class Provider (SCP). The destination did not send back an Association Response.

> Chapter 1 DICOM Gateway Error Messages

## DICOM Network Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Job terminated due to Network Error \#n \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW5 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs while sending a DICOM message when one of the following conditions arises:

- Connection/association dropped/aborted by peer application entity
- Unknown PDU (Protocol Data Unit) type received
- Garbled transmission

> These are errors caused by the DICOM system receiving images from VistA.

## Image Transmission Acknowledgement Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Unexpected Response \*\*\*

> \*\*\* Expected "IMAGE SENT", received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW5 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The MUMPS Transmission Controller instructed the MAG_VISTA_SEND_IMAGE.exe program to send an image to the destination Storage SCP. An error on the Storage SCP prevented successful transmission of the image.

## Image Transmission Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE: DESTINATION STORAGE FAILURE \*\*\*

> \*\*\* Status=XXXXX Error ID: YYYYYY \*\*\*

> \*\*\* Comment: ZZZZZ \*\*\*

> \*\*\* Offending Element: (gggg,eeee) \<name of element\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW5 \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The destination Storage SCP was not able to properly handle an image transmitted to it by the MAG_VISTA_SEND_IMAGE.exe program. The complete reason for the error is given in the message.

> Chapter 1 DICOM Gateway Error Messages

## Cannot Acknowledge Establishment of Association

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected return value “ASSOCIATION ACKNOWLEDGE”. \*\*\*

> \*\*\* Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW6 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The MUMPS Transmission Controller had the MAG_VISTA_SEND_IMAGE.exe program send an Association Acknowledge Request to the destination Storage SCP. The error is that the Storage SCP did not respond with a proper Association Acknowledge Response.

## Cannot Acknowledge Release of Association

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* ERROR IN VISTA SEND IMAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Unexpected response \*\*\*

> \*\*\* Expected "ASSOCIATION ENDED", Received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDIW6 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The MUMPS Transmission Controller had the MAG_VISTA_SEND_IMAGE.exe program send an Association Release Request to the destination Storage SCP. The error is that the Storage SCP did not respond with a proper Association Release Response.

## Error Messages Report by DICOM Message Queuing Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Between the message processing and transmission steps, all DICOM messages are stored in intermediate files (\*.DCM) on the local system. For the sake of flexibility, four different mechanism are provided:

1.  First-In-First-Out (FIFO) queues for PACS messages for the Text Gateway
2.  Direct mode for queries (for example, Modality Worklist) for the Text Gateway
3.  FIFO queue for image acquisition (C:\DICOM\Image_In\\)
4.  FIFO queue for image transmission (C:\DICOM\Image_Out\\)

> The error messages in this section pertain to the intermediate file processing for the Text Gateway.

> Chapter 1 DICOM Gateway Error Messages

## Error in Directory Lookup of FIFO Queue Subdirectory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Cannot locate directory xxxxxxxxxx \*\*\*

> \*\*\* Host File System Error xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE0 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the Text Gateway is doing a directory lookup of a FIFO queue subdirectory (typically C:\dicom\data1\ANNNNN) for writing a new file. This is a catastrophic error that prevents the application from even creating the new file’s subdirectory, if it did not already exist.

> The error message includes the name of the subdirectory that got the error and the error code from the directory lookup operation. The most likely problem is that the path is pointing to a non-existent C:\dicom\data1 directory.

## Cannot Create FIFO Queue Subdirectory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Cannot create directory xxxxxxxxxx \*\*\*

> \*\*\* Host File System Error: xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE0 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the Text Gateway is creating a new FIFO queue subdirectory (typically

> C:\DICOM\Data1\Annnnn).

> The error message includes the name of the subdirectory that got the error and the error code from the MKDIR operation. The most likely problems are either that the permissions prevent the subdirectory from being created or the disk drive is out of space.

> Chapter 1 DICOM Gateway Error Messages

## Invalid Data in Queue Pointer File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR -- WRITING DICOM FILE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Bad File Pointer: \*\*\*

> \*\*\* "xxxxxxxxxx" = "xxxxxxxxxx". \*\*\*

> \*\*\* Value of pointer should be 7 digits. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE0 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the Text Gateway finds Queue processor invalid data in one of the FIFO queue pointers files. (The pointer files are named x_READ.PTR and x_WRITE.PTR, where *x* is A, B, C, D, E, F, G, H, S, T, U, V, W, X, Y,or Z.) The values in these files must be 7-digit integer numbers with leading zeroes. When any other value is encountered in one of these files, this error will occur.

> The error message will include the name of the offending file and the value that is encountered in that file.

> Typically, this error occurs when a queue pointer file was modified manually, not through the software in the VistA Imaging DICOM Gateway. When the displayed value indicates that a *strange* character appears leading or trailing the queue entry number, use Notepad to correct the offending file and enter the appropriate value. When the value contains an embedded control character, it may be necessary to erase the complete line, and re-enter it.

> For example, suppose the X_READ.PTR is null (zero bytes long), and should really contain 12345. Use Notepad and type the value 0012345\<Enter\>.

## Cannot Create a FIFO Queue Text File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM TEXT GATEWAY ERROR -- WRITING DICOM FILE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Renaming xxxxxxxxxx to xxxxxxxxxx failed \*\*\*

> \*\*\* Please delete the file "xxxxxxxxxx" and restart. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE0 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the DICOM Text Gateway is not able to create a file in a FIFO Queue. When writing a DICOM file, the file is first created with a temporary name (typically ANNNNNNN.tmp), and then is renamed to its permanent name (in this case, ANNNNNNN.dcm). The error occurs whenever the temporary file cannot be renamed to its permanent name. This may occur when there is already a file present with that same name present, with permissions set so that it can’t be deleted. Manually deleting the file will allow the processing to continue.

> The error message will include the temporary file name and the permanent file name.

> Chapter 1 DICOM Gateway Error Messages

## Unrecognized Command Code in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Unexpected command value processing "xxxxxxxxxx". \*\*\*

> \*\*\* Expected an integer numeric value, received "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE4 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the DICOM Gateway encounters an unrecognized command code in an incoming DICOM message.

> The error message will include the name of the data stream being processed and the offending command code.

> This is probably an error on the configuration of the peer application entity.

## Unsupported Command in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Unexpected command value processing "xxxxxxxxxx". \*\*\*

> \*\*\* Cannot find label "xxxxxxxxxx" in routine ^MAGDQUE4. \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDQUE4 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the DICOM Gateway encounters an unsupported command in an incoming DICOM message.

> The error message will include the name of the data stream being processed and the offending command code.

> This is probably an error on the configuration of the peer application entity.

## TCP/IP Communications Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Cannot Connect to TCP/IP Socket (Set-Up Error)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* TCP not setup correctly \*\*\*

> \*\*\* \*\*\*

> \*\*\* Connecting to IP Address "xxxxxxxxxx", port "xxxxxxxxxx". \*\*\*

> \*\*\* Cannot open Socket \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP1 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the DICOM Gateway attempts to connect to a TCP/IP socket, and no connection can be established.

> Chapter 1 DICOM Gateway Error Messages

> The error message will include the values of the IP Address and the port number that were used in the attempt to open the socket.

> Typically, the cause of this error is that either the IP Address or the Port Number is incorrectly specified in the F:\DICOM\Dict\SCU_List.DIC master file. Notepad can be used to correct this file.

## Cannot Find DICOM Message File to Send

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Cannot find file "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the file containing the DICOM message file to be transmitted cannot be located.

## Invalid First 8-bytes in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Incorrect DICOM Message -- first 8 bytes are wrong \*\*\*

> \*\*\* Group=xxxxxxxxxx, Element=xxxxxxxxxx, Length=xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The first eight bytes of a DICOM message file should be *0 0 0 0 4 0 0 0* hexadecimal. This represents element (0000,0000) with a length of 4. This data must always be correct.

> This error most likely occurs when the system is trying to send a zero-length DICOM file that was created due to running out of disk space.

## Length-to-End Missing in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Incorrect DICOM Message -- Length to End not present \*\*\*

> \*\*\* Group=xxxxxxxxxx, Element=xxxxxxxxxx, Length=xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The second required element in a VistA DICOM message is (0000,0001) which specifies the length to the end of the message. This is used by the TCP routine for performance to concatenate several messages into a single file (typically for Modality Worklist responses).

> If this element is missing, it probably represents a programming error.

> Chapter 1 DICOM Gateway Error Messages

## SOP Class UID Missing in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Incorrect DICOM Message -- SOP Class UID not present \*\*\*

> \*\*\* Group=xxxxxxxxxx, Element=xxxxxxxxxx, Length=xxxxxxxxxx \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The third required element in a VistA DICOM message (0000,0002) specifies the SOP Class UID for the message. This is needed to determine the Presentation Contact ID for the message.

> If this element is missing, it probably represents a programming error.

## Invalid SOP Class UID in DICOM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Incorrect SOP Class UID format \<\<xxxxxxxxxx\>\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> If the SOP Class UID for the message, element (0000,0002), has the wrong format (that is, doesn’t begin with a numeric), this error will occur.

> This probably represents a programming error.

## Unknown Presentation Context ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Unknown Presentation Context ID for \<\<xxxxxxxxxx\>\> \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP2 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> If the SOP Class UID for the message, element (0000,0002), has the wrong value this error will occur.

> This is most likely caused by trying to send a message for a SOP Class that was not negotiated for the association. It is typically seen during *trial and error* configuration of vendor systems.

> Chapter 1 DICOM Gateway Error Messages

## Unexpected PDU (expected 04 = P-Data)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* DICOM GATEWAY ERROR \*\*\*

> \*\*\* \*\*\*

> \*\*\* Expected PDU type 04(hex), \*\*\*

> \*\*\* found "xxxxxxxxxx". \*\*\*

> \*\*\* \*\*\*

> \*\*\* Routine: ^MAGDTCP3 Please Call Support Personnel \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This error occurs when the DICOM Gateway attempts to receive data from a peer application entity and the code for the PDU Type is not equal to 04 (hex), which is the code for P-Data. (A PDU is a Protocol Data Unit.)

> This is caused by a DICOM implementation problem with a vendor system.

## Errors that may occur in Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The error messages listed in this chapter may occur in Remote Procedure Calls. The message texts are typically displayed on the client workstation from which the Remote Procedures were invoked.

1.  <span id="1.16.1_MAG_DICOM_AUDIT_COUNT_(COUNT^MAGD" class="anchor"></span>MAG DICOM AUDIT COUNT (COUNT^MAGDRPC7)

> This Remote Procedure may return the following error messages:

- -1,No Location Specified
- -2,No Message Specified

> Both messages indicate that the software on the client-station omitted to specify a parameter that is needed for proper operation of the Remote Procedure.

1.  <span id="1.16.2_MAG_DICOM_FIND_LOCATION_(FINDLOC^" class="anchor"></span>MAG DICOM FIND LOCATION (FINDLOC^MAGDRPC8)

> This Remote Procedure may return the following error message:

- -1,Invalid location "*name*"

> This message indicates that there is no location (or division) at the current site with the name that was specified by the client-system. Either the client-system is mis-configured, or a user entered an invalid name.

1.  <span id="1.16.3_MAG_DICOM_GET_BASIC_IMAGE_(IMAGE^" class="anchor"></span>MAG DICOM GET BASIC IMAGE (IMAGE^MAGDRPC2)

> This Remote Procedure may return the following error messages:

- -1,Invalid IEN (*number*)
- -2,No data for "*numbe*r".
- -3,Image \#*number* has been deleted.

> Chapter 1 DICOM Gateway Error Messages

> The first message (-1…) indicates that the value of the parameter that should identify the image for which information is to be retrieved is not a numeric value.

> The second message (-2…) indicates that the value of this parameter has a numeric value, but there is no image with that (internal) number.

> The third message (-3…) indicates that information is requested about an image that has been deleted. In this case, no information other than the error message is returned.

1.  <span id="1.16.4_MAG_DICOM_GET_NEXT_QUEUE_ENTRY_(N" class="anchor"></span>MAG DICOM GET NEXT QUEUE ENTRY (NEXTIMG^MAGDRPC4)

> This Remote Procedure may return the following error messages:

- -1,No Origin Specified
- -2,No studies to be transmitted
- -3,No files to be transmitted

> The first message indicates that the software on the client-station omitted to specify an essential parameter. Most likely, this error condition is the result of a mis-configuration of the client- station.

> The second and third messages are informational only and indicate that all requested images (or studies) have been transmitted.

1.  <span id="1.16.5_MAG_DICOM_GET_PLACE_(GETPLACE^MAG" class="anchor"></span>MAG DICOM GET PLACE (GETPLACE^MAGDRPC8)

> This Remote Procedure may return the following error message:

- -1,Location "*name*" not found.

> This message indicates that there is no location (or division) at the current site with the name that was specified by the client-system. Either the client-system is mis-configured, or a user entered an invalid name.

1.  <span id="1.16.6_MAG_DICOM_GET_SERVICE_INFO_(SERVI" class="anchor"></span>MAG DICOM GET SERVICE INFO (SERVICE^MAGDRPC2)

> This Remote Procedure may return the following error message:

- -1,No Imaging Site Parameters defined

> This message indicates that the configuration of the Imaging Site Parameters (on the VistA) system still has to be completed. Operation on the client cannot proceed until the configuration on the server is complete.

1.  <span id="1.16.7_MAG_DICOM_HL7_POINTER_ACTION_(HL7" class="anchor"></span>MAG DICOM HL7 POINTER ACTION (HL7PTR^MAGDRPC8)

> This Remote Procedure may return the following error messages:

- -1,Invalid Pointer "*value*".
- -2,Invalid Request: "*action*".

> Chapter 1 DICOM Gateway Error Messages

> The first of these messages indicates that the value of the parameter that identifies the HL7- message, as specified by the software on the client-station, cannot be used to identify a message that is currently present in the system. Either the software on the client system is working from obsolete information (server was purged since last update of the client), or a user entered an erroneous pointer number.

> The second message indicates that the software on the client-station specified an erroneous value for the parameter that indicates the action to be taken by the Remote Procedure. This condition can only be resolved with a correction to the client-software.

1.  <span id="1.16.8_MAG_DICOM_IMAGE_PROCESSING_(ENTRY" class="anchor"></span>MAG DICOM IMAGE PROCESSING (ENTRY^MAGDIR8)

> This Remote Procedure may return the following error messages:

- xxxxx

> Problem detected by routine xxxxx Error Code: xxxxx

> Messages of this type are always followed by one of the messages in sec[tion 1.15.6](#dicom-image-processing-errors-during-input). The subsequent message provides more detailed information about the error. See section [1.15.6](#dicom-image-processing-errors-during-input) for these details.

1.  <span id="1.16.9_MAG_DICOM_INCORRECT_IMAGE_CT_(COR" class="anchor"></span>MAG DICOM INCORRECT IMAGE CT (CORRECT^MAGDRPC8)

> This Remote Procedure may return the following error messages:

- -1,No Location Specified
- -2,No Gateway Specified

> These messages indicate that the software on the client-station omitted to specify a value for a required parameter. Most likely, these error conditions are the result of a mis-configuration of the client-station.

1.  <span id="1.16.10__MAG_DICOM_LOOKUP_STUDY_(LOOKUP^" class="anchor"></span>MAG DICOM LOOKUP STUDY (LOOKUP^MAGDRPC4)

> This Remote Procedure may return the following error messages:

- -1,No Case or Consult Number Specified
- -2,No Study Date Specified
- -3,Invalid study date “*text*”.
- -4,Consult is cancelled
- -5,Consult/procedure not on file
- -6,Invalid image (nnn)
- -7,Parent file xxx not yet supported

> The first two messages indicate that the software on the client-station omitted to specify a required parameter. Such an omission may happen when a user just presses the enter-key, rather than provide a complete answer to a question.

> Chapter 1 DICOM Gateway Error Messages

> The other five messages indicate cases where the provided information cannot be matched successfully with information in the VistA database.

1.  <span id="1.16.11_MAG_DICOM_NETWORK_STATUS_(ONOFLI" class="anchor"></span>MAG DICOM NETWORK STATUS (ONOFLINE^MAGDRPC5)

> This Remote Procedure may return the following error message:

- -1,No Network Location Specified

> This message indicates that the client system omitted to provide a value for the parameter that indicates the location (or division) at the current site from which images are to be transmitted. Most likely, the client-system is mis-configured.

1.  <span id="1.16.12_MAG_DICOM_PACS_CUTOFF_DATE_(CUTO" class="anchor"></span>MAG DICOM PACS CUTOFF DATE (CUTOFF^MAGDRPC1)

> This Remote Procedure may return the following error messages:

- -2,No PACS Installed
- -3,PACS Retention Parameter not defined

> Both messages are informational only. The first message (-2,…) indicates that the site-(location, division) is configured as if no PACS is installed. The other message indicates that as yet no value for the retention period parameter has been entered into the site configuration.

1.  <span id="1.16.13_MAG_DICOM_PACS_MINIMUM_SPACE_(MI" class="anchor"></span>MAG DICOM PACS MINIMUM SPACE (MINSPACE^MAGDRPC1)

> This Remote Procedure may return the following error messages:

- -2,No PACS Installed
- -3,PACS Minimum Space Percentage Parameter not defined

> Both messages are informational only. The first message (-2,…) indicates that the site-(location, division) is configured as if no PACS is installed. The other message (-3,…) indicates that as yet no value for the minimum disk space parameter has been entered into the site configuration.

1.  <span id="1.16.14_MAG_DICOM_QUEUE_IMAGE_(QUEUE^MAG" class="anchor"></span>MAG DICOM QUEUE IMAGE (QUEUE^MAGDRPC3)

> This Remote Procedure may return the following error messages:

- -1,No Image specified
- -2,No Destination specified
- -3,No Origin specified
- -4,Cannot Queue Image Object Type "*type*".

> The first three messages indicate that the software on the client-station omitted to specify values for required parameters. Most likely, such a situation is the result of a failure to make a selection at an earlier stage in the process.

> Chapter 1 DICOM Gateway Error Messages

> The fourth message (-4,…) indicates that the requested image is of such a nature that it is not permitted to enter that image into this transmission queue. Only images that are of the following “types” can be transmitted using the DICOM C-Store protocol:

- Type 3 = X-Ray
- Type 11 = X-Ray Group
- Type 100 = DICOM Image
  1.  <span id="1.16.15_MAG_DICOM_QUEUE_INIT_(INIT^MAGDR" class="anchor"></span>MAG DICOM QUEUE INIT (INIT^MAGDRPC4)

> This Remote Procedure may return the following error messages:

- -1,No entries at all in queue.
- -2,No entries present for "*name*".
- -3,No origin specified.

> The last message (-3,…) indicates that the client system omitted to provide a value for the parameter that indicates the location (or division) at the current site from which images are to be transmitted. Most likely, the client-system is mis-configured.

> The other two messages are informational only. Both indicate that currently no images are queued up to be transmitted.

1.  <span id="1.16.16_MAG_DICOM_ROUTE_EVAL_LOG_(EVALLO" class="anchor"></span>MAG DICOM ROUTE EVAL LOG (EVALLOG^MAGDRPC6)

> This Remote Procedure may return the following error messages:

- -1,No task \#*number*
- -2,MAXIMUM parameter = *number* \< 1
- -3,*text*

> The first message (-1, …) indicates that the client-system specified a value for the TaskMan task number that does not correspond to any active task. Most likely, the VistA system has been restarted and some clean-up or house-keeping tasks have been performed.

> The second message (-2, …) indicates that the value for the parameter that specifies the maximum number of log-messages that are to be returned to the client has an unusable value. This condition can only be remedied by correcting the software on the client-system.

> The third message (-3, …) is informational only. This message indicates that the TaskMan task, for which messages were being relayed, has stopped. The text that is included in this message contains the reason that TaskMan provided for ending the task.

> Chapter 1 DICOM Gateway Error Messages

1.  <span id="1.16.17_MAG_DICOM_ROUTE_EVAL_START_(STAR" class="anchor"></span>MAG DICOM ROUTE EVAL START (START^MAGDRPC5)

> This Remote Procedure may return the following error messages:

- -1,No Location Specified
- -2,No Routing Rules Specified
- -3,A Rule Evaluator is Already Running for \<location\>
- -4,TaskMman did not Accept Request

> The first two messages indicate an error or omission in the set-up of the DICOM Gateway from which the request was issued.

> The third message indicates that a rule-evaluator is already running for the requested location. Only one evaluation may be running for any given location (or division) at any time.

> The fourth message indicates that the process could not be started. (Perhaps an illegal input or it is already running.)

1.  <span id="1.16.18_MAG_DICOM_ROUTE_NEXT_FILE_(XMIT^" class="anchor"></span>MAG DICOM ROUTE NEXT FILE (XMIT^MAGDRPC5)

> This Remote Procedure may return the following error messages

- -1,No Location Specified
- -2,No Valid Destinations Specified
- -1~No routable files found for image *nnnnn*

> The first message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

> The second message indicates that the user did not select any destinations to which files might be transmitted.

> The third message indicates that a queue entry is being processed for an image that has no actual files associated with it (that is, there are no files to be transmitted for that image). Either the image is currently in a *deleted* state, or there were never any files successfully stored for this image.

1.  <span id="1.16.19_MAG_DICOM_ROUTE_PURGE_DONE_(PURG" class="anchor"></span>MAG DICOM ROUTE PURGE DONE (PURGDONE^MAGDRPC6)

> This Remote Procedure may return the following error message:

- -1,No Location Specified

> This message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

> Chapter 1 DICOM Gateway Error Messages

1.  <span id="1.16.20_MAG_DICOM_ROUTE_REMOVE_OBSO_(REM" class="anchor"></span>MAG DICOM ROUTE REMOVE OBSO (REMOBSO^MAGDRPC6)

> This Remote Procedure may return the following error message:

- -1,No Location Specified

> This message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

1.  <span id="1.16.21_MAG_DICOM_ROUTE_REQUEUE_(REQUEUE" class="anchor"></span>MAG DICOM ROUTE REQUEUE (REQUEUE^MAGDRPC6)

> This Remote Procedure may return the following error message:

- -1,No Location Specified

> This message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

1.  <span id="1.16.22_MAG_DICOM_ROUTE_TRANSACT_STS_(TR" class="anchor"></span>MAG DICOM ROUTE TRANSACT STS (TRANSTS^MAGDRTIM)

> This Remote Procedure may return the following error messages:

- -1,No Location Specified
- -2,Invalid Transaction ID

> The first message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

> The second message indicates an error in the software that performed the request from the client station. A status can only be provided for a *known* transaction. The client system receives transaction identifiers as new transactions are created.

1.  <span id="1.16.23_MAG_DICOM_ROUTE_VALID_DEST_(VALD" class="anchor"></span>MAG DICOM ROUTE VALID DEST (VALDEST^MAGDRPC1)

> This Remote Procedure may return the following error message:

- -1,"xxxxxx" is not a valid destination

> This message indicates that an attempt to re-configure a DICOM Gateway included a name for a location that is not defined in the VistA database.

1.  <span id="1.16.24_MAG_DICOM_SET_PACS_PARAMS_(SETPA" class="anchor"></span>MAG DICOM SET PACS PARAMS (SETPACS^MAGDRPC8)

> This Remote Procedure may return the following error messages:

- -1,No Place Specified.
- -2,Invalid Place Specified.

> The first message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

> Chapter 1 DICOM Gateway Error Messages

> The second message indicates that an attempt to re-configure a DICOM Gateway included a name for a location that is not defined in the VistA database.

1.  <span id="1.16.25_MAG_DICOM_TEXT_PROCESSING_(ENTRY" class="anchor"></span>MAG DICOM TEXT PROCESSING (ENTRY^MAGDHRS1)

> This Remote Procedure may return the following error message:

- -1 ^MAGDHL7(2006.5,*nnnnnn*,*mmm*,...) is incomplete

> This message indicates that, after waiting the maximum time, an HL7 message is still not complete. Most likely, the process that generated the message did not complete successfully.

1.  <span id="1.16.26_MAG_DICOM_UPDATE_GATEWAY_NAME_(U" class="anchor"></span>MAG DICOM UPDATE GATEWAY NAME (UPDTGW^MAGDRPC8)

> This Remote Procedure may return the following error messages:

- -1,No Gateway Name specified
- -2,No Gateway Location specified

> These messages indicate omissions in the set-up of the DICOM Gateway from which the request was issued.

1.  <span id="1.16.27_MAG_DICOM_UPDATE_SCU_LIST_(UPDTA" class="anchor"></span>MAG DICOM UPDATE SCU LIST (UPDTAPP^MAGDRPC8)

> This Remote Procedure may return the following error message:

- -1,Missing or Inconsistent Parameters.

> This indicates an omission or inconsistency in the set-up of the DICOM Gateway from which the request was issued.

1.  <span id="1.16.28_MAG_DICOM_WORKSTATION_VERSION_(S" class="anchor"></span>MAG DICOM WORKSTATION VERSION (STATION^MAGDRPC1)

> This Remote Procedure may return the following error message:

- -1,No Station Identifier Specified

> This message indicates an omission in the set-up of the DICOM Gateway from which the request was issued.

1.  <span id="1.16.29_MAGV_DGW_ACTION_UID_LIST_error_c" class="anchor"></span>MAGV DGW ACTION UID LIST error code: (ACTUIDS^MAGVDGWP)

> This Remote Procedure may return the following error message:

- -1^Error getting action UID list

> Chapter 1 DICOM Gateway Error Messages

1.  <span id="1.16.30_MAGV_DGW_INSTRUMENT_LIST_error_c" class="anchor"></span>MAGV DGW INSTRUMENT LIST error code: (INSTRMNT^MAGVDGWP)

> This Remote Procedure may return the following error message:

- -1^Error getting instrument list

> This message indicates an omission in the set-up or initialization of the DICOM Gateway INSTRUMENT.DIC file either on the DICOM gateway or propagation of it on the Vista System (run menu option 4-2-4 to update INSTRUMENT.DIC. Once the INSTRUMENT.DIC issue has been addressed, the HDIG Tomcat service should be restarted.

1.  <span id="1.16.31_MAGV_DGW_MODALITY_LIST_error_cod" class="anchor"></span>MAGV DGW MODALITY LIST error code: (MODALITY^MAGVDGWP)

> This Remote Procedure may return the following error message:

- -1^Error getting modality list

> This message indicates an omission in the set-up or initialization of the DICOM Gateway MODALITY.DIC file either on the DICOM gateway or propagation of it on the Vista System. Once the MODALITY.DIC issue has been addressed, the HDIG Tomcat service should be restarted.

1.  <span id="1.16.32_MAGV_DGW_ACTION_UID_LIST_(ACTUID" class="anchor"></span>MAGV DGW ACTION UID LIST (ACTUIDS^MAGVDGWP)

> This Remote Procedure may return the following error message:

- -1^Error getting action UID list

> This message indicates an omission in the set-up or initialization of the DICOM UID SPECIFIC ACTION table (file \#2006.539) on the Vista System. Once the issue has been addressed, the HDIG Tomcat service should be restarted.

1.  <span id="1.16.33_MAGV_GET_DGW_CONFIG_error_codes:" class="anchor"></span>MAGV GET DGW CONFIG error codes: (GETGWCFG^MAGVDGWP)

> This Remote Procedure may return the following error messages:

- -1~Error getting DGW Config info
- -1~No HostName provided
- -1~HostName returned from DB, \<HOST\> doesn't match request.

> This message indicates an omission in the set-up or initialization of the DICOM Gateway Configuration either on the DICOM gateway or propagation of it on the Vista System with the proper hostname. Once the issue has been addressed, the HDIG Tomcat service should be restarted.

> Chapter 1 DICOM Gateway Error Messages

1.  <span id="1.16.34_MAGV_STUDY_LOOKUP___(LOOKUP^MAGV" class="anchor"></span>MAGV STUDY LOOKUP (LOOKUP^MAGVSTDY)

> This Remote Procedure may return the following error messages:

> 0~DFN~SITE-ID~0~PID OK

> 0~DFN~SITE-ID~-1~\<Msg to Dicom Correct\> 0~DFN~SITE-ID~-1~PID ERROR

> -1~INVALID IMAGE SERVICE

> -1~BAD CASE \#

> -1~NO CASE \#

> Note: \<Msg to Dicom Correct\> is one of the last 3 errors’ text.

## UID Checking Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each of the following 3 RPCs have inputs, like DFN, \[Long\]- ACC#, SITE-ID and the proper UID to level. In return, if 0 is returned, the UID is accepted. When negative numbers are returned, it means a real error. When positive numbers are returned, it means a special case..

## Notes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  These three calls are executed in Study, Series and SOP order for every first SOP instance received for a new Series, for the rest of the SOP Instances in the Series only the SOP level is called.
2.  When 0 and positive numbers are returned, there are logs made into a UID history tracking file, assuming that subsequent DB operations will follow UID checking, so please do not try to invoke these RPCs individually.

## MAGV STUDY UID CHECK return codes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No duplicate Study found  0~OK no duplicate Study UID found DFN/ACC# match; Existing Study  0~OK same Study UID found

> No DFN &/or ACC# match;

> Duplicate Study  1~NewUIDToUse~STD-UID’ DFN/ACC# match; Dupl. Study  1~ LogUIDToUse~STD-UID’

> Illegal Study UID  3~Illegal UID Replacement~STD-UID’ Fatal (resource, etc.) Error  -1~\<Fatal \[Error\] or \[UID \>96 Characters\]\>

> -3~\<Fatal UIDGenError\>

> Chapter 1 DICOM Gateway Error Messages

## MAGV SERIES UID CHECK return codes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No duplicate Series found  0~OK no duplicate Series UID found DFN/ACC#/Study match;

> Existing Series  0~OK same Series UID found No DFN, ACC# &/or Study match;

> Duplicate Series 1~NewUIDToUse ~SER-UID’ DFN/ACC#/Std match; Dupl. Series  1~ LogUIDToUse~SER-UID’

> Illegal Series UID  3~Illegal UID Replacement~SER-UID’ Fatal (resource, etc.) Error  -1~\<Fatal \[Error\] or \[UID \>96 Characters\]\>

> -3~\< Fatal UIDGenError\>

## MAGV SOP UID CHECK return codes:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No duplicate SOP found  0~OK no duplicate SOPI UID found No DFN, ACC#, Study &/or

> Series match; Duplicate SOP  1~NewUIDToUse~SOP-UID’ DFN/ACC#/Study/Series match;

> Duplicate SOP  2~RERUN resend Detected, Don’t store! DFN/ACC#/Std/Ser match;

> Dup. SOP logged  2~RERUNLog

> Illegal SOP UID  3~Illegal UID Replacement~SER-UID’ Fatal (resource, etc.) Error  -1~\<Fatal \[Error\] or \[UID \>96 Characters\]\>

> -3~\< Fatal UIDGenError\>

## Errors Reported by the Menu Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Cannot Start Application because Conflicting Application Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a user selects a menu option, the menu processor double-checks whether that option can be executed, or whether another application is already running that conflicts with the selected menu option. When such a conflict is detected, a warning message is presented that looks like:

> Chapter 1 DICOM Gateway Error Messages

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* Cannot start this application while the following \*\*\*

> \*\*\* \*\*\*

> \*\*\* application is active: \*\*\*

> \*\*\* \*\*\*

> \*\*\* Update Gateway Configuration Parameters \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Or

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* Cannot start this application while the following \*\*\*

> \*\*\* \*\*\*

> \*\*\* application is active: \*\*\*

> \*\*\* \*\*\*

> \*\*\* Start Processing Text Messages from HIS \*\*\*

> \*\*\* \*\*\*

> \*\*\* Process DICOM Images \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> When a message like this appears:

- Wait until the conflicting application completes normally
- Use the menu to stop the conflicting application

## Cannot Start Multiple Instances of the Same Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a user selects a menu option, the menu processor double-checks whether the selected option may have multiple instances of itself running at the same time. If this is not permitted, and an instance of that menu option is already running, a warning message is presented that looks like:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \<name of application\> is already running \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The following menu options may have only one instance active at any given time:

1.  VistA DICOM Text Gateway

> 1 Start Processing Text Messages from HIS

10. Purge Old Modality Worklist Entries
11. Purge Old DICOM Message Files
12. Purge Old HL7 Transaction Global Nodes
13. Purge Old Audit Records
2.  VistA DICOM Image Gateway
3.  Process DICOM Images
4.  Increment DICOM Image Input Pointer

> 8 Send DICOM Images to Another Storage Server

> 5 Batch Export VistA Radiology Images

> 11 Purge Incomplete Image Information

> 4 VistA DICOM System Maintenance

> 2 Gateway Configuration and DICOM Master Files

2.  Update Gateway Configuration Parameters
3.  Update AE_TITLE.DIC

> Chapter 1 DICOM Gateway Error Messages

4.  Update INSTRUMENT.DIC
5.  Update MODALITY.DIC
6.  Update PORTLIST.DIC
7.  Update SCU_LIST.DIC
8.  Update WORKLIST.DIC
9.  Reinitialize All the DICOM Master Files
10. Create Shortcuts for Instruments
11. Validate Access/Verify Codes for Modality Worklist
12. Display Versions and/or Time Stamps of Components

## Expired Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DICOM Gateway stores a set of access and verify codes as part of its configuration parameters. If the codes are changed in VistA, but not updated on the DICOM Gateway, the DICOM Gateway will not be able to log into VistA, and the following error will display:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* Credentials for Background Processes need to be set up \*\*\*

> \*\*\* \*\*\*

> \*\*\* First use menu option 4-2-2 to set up these credentials, \*\*\*

> \*\*\* \*\*\*

> \*\*\* then use menu option 4-2-11 to verify them. \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This message will be displayed each time a menu is shown, until new credentials have been set up using menu option 4-2-2 (Update Gateway Configuration Parameters), and validated using menu option 4-2-11 (Validate Access/Verify Codes for Modality Worklist).

> Once valid access and verify codes are stored again, the warning message will disappear.

## VistA Send Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* ERROR IN VISTA SEND I\*MAGE \*\*\*

> \*\*\* \*\*\*

> \*\*\* Undefined User Application: "xxxxxxxxx" \*\*\*

> \*\*\* \*\*\*

> \*\*\* This entry may have come from SCU_LIST.DIC at another site \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Try the following steps to correct this problem:

1.  By removing the ordering location when you start the Transmit, option 2-8-2.
2.  Adding the User Application to SCU_LIST.DIC and loading it using menu option 4-2-7.

> Chapter 1 DICOM Gateway Error Messages

> This page is intentionally left blank.

# Chapter 2 DICOM Query/Retrieve Server Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter contains a listing of error messages generated by the DICOM Query/Retrieve Server. These error messages are written to the Hybrid DICOM Image Gateway (HDIG) application log, which is called ImagingExchangeWebApp.log and is located on the computer on which the HDIG is installed in the folder C:\Program Files\Apache Software Foundation\Tomcat 6.0\logs\\

> Date and time may be amended to the name of the log file. For example, ImagingExchangeWebApp.log.2011-06-21.

> Users with the security key MAG VIX ADMIN can view the HDIG log using the URL to the Java Logs page. For more information about accessing the HDIG log, see the *VistA Imaging DICOM Gateway User Manual*.

## Class not Found

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> java.lang.ClassNotFoundException: \<class name including package path\>

> This error occurs if the requested class is not in the class path.

> All classes are stored in various .jar files (a .jar file is basically a zip file containing a selected group of java classes). All .jar files associated with the Query/Retrieve (Q/R) application are stored in the C:\Program Files\Apache Software Foundation\Tomcat 6.0\lib\\ folder. Generally, an error only occurs if something went wrong with the installation process and not all

> .jar files are in C:\Program Files\Apache Software Foundation\Tomcat 6.0\lib\\ folder. To resolve this issue, perform the installation process again. If the message recurs, contact the CLIN 3 team.

## Cannot Bind Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Fatal Error: AssociationManager could not create server socket: java.net.BindException: Cannot assign requested address: bind

> This error occurs if the Q/R application cannot bind to the TCP port (socket) and cannot start listening on the specified port number.

> To resolve this problem, do either of the following:

- Stop the Q/R application. Then use the Window Task Manager locate and terminate any processes named java.exe or javaw.exe.
- Reboot the computer (If the computer is also being used as a DICOM Gateway, stop all DICOM Gateway processes and exit the DICOM Gateway application first).

> Chapter 2 DICOM Query/Retrieve Server Error Messages

## DICOM Connectivity Framework (DCF) Read Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Failure to read DCF Configuration File. Used hardcoded default.

> This error occurs the Q/R application could not read the DICOM Toolkit configuration file. If this happens, the application automatically sets certain values to continue working. This error message specifies which values are being used for two DICOM fields: *Class Implementation UID* and *Class Implementation Version*. These fields are involved with the Association process only.

> Ensure that the Listen file is present in the \DCF_Runtime\cfg\apps\defaults folder. If it is not, recover a copy of this file from another Q/R application, or reinstall the software.

## Cannot Open File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Could not find or open \<filename\>

> The Q/R application could not open or access a specified file. This generally refers to those files on the Imaging Server that define the DICOM object.

> Confirm the computer running the Q/R application has proper authentication/authorization to the Imaging Server(s). Confirm that the user logged into the computer has proper authentication/authorization to the Imaging Server(s).

## Audit Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: Exception thrown posting to Audit Log.

> The HDIG failed to write to the VistA Imaging Audit Log. This is generally likely when there is a network or RPC problem with the VistA Healthcare Information System (HIS). This does not stop the HDIG from performing rest of its functions.

## C-Find Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: \<AETitle\> is invalid to perform C-Find Requests.

> The AETitle does not have permission to perform C-Find Requests. This can be changed by editing the DICOM AE Security Matrix.

## C-Move Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: \<AETitle\> is invalid to perform C-Move Requests.

> The AETitle does not have permission to perform C-Move Requests. This can be changed by editing the DICOM AE Security Matrix.

> Chapter 2 DICOM Query/Retrieve Server Error Messages

## Moving Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: Exception thrown while moving objects.

> The C-Move operation failed to move images to the requested DICOM device. Check rest of the log for additional messages that pertain to this error. Generally, this happens when VistA Imaging was unsuccessful establishing a DICOM Association with the DICOM device or this application failed to get the DICOM objects from VistA Imaging Imageshare.

## VR Violation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR VR Violation Error(s) in C-Find-RQ message=\<DIMSE msg\>

> The DIMSE message is illegal according to the DICOM Standard. The DICOM Message Service Element (DIMSE) message is rejected at this point.

## Accessing DICOM Object from Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: Exception thrown during reconstitution of DICOM Object while accessing Text file.

> Application failed to read the DICOM object file in Storage. Possible problem may be either the Storage subsystem is not on the network or the login user of the HDIG does not have the correct permissions.

## Sending DICOM objects to DICOM device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR: C-Store SCP failed during DICOM object send.

> Application failed to send a specific DICOM object to DICOM device. The application will continue to send all other associated DICOM objects.

> Error: C-Store AETitle Error:\<result\>

> Application does not have permission to initiate a DIMSE message with the DICOM device. This can be corrected by either the DICOM AE Security Matrix or at the DICOM device itself.

## Association with DICOM device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR: C-Store SCP rejecting DICOM C-Store Association.

> Application does not have permission to initiate a DICOM Association with the DICOM device. This can be corrected by either the DICOM AE Security Matrix or at the DICOM device itself.

> Chapter 2 DICOM Query/Retrieve Server Error Messages

## Invalid Calling AETitle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: This section applies to MAG\*3.0\*99 and earlier gateways.

> ERROR-MAG DICOM CHECK AE TITLE: \[-2,No entry for AE Title \\\<AETitle\>\\.

> INFO-...throwing due to rejected CallingAETitle, \<AETitle\>, for \<hostname of SCU\>.

> This error occurs if an invalid AE (Application Entity) Title is provided by the device contacting the Q/R application.

> Confirm that this device should have access to VistA Imaging. Confirm that the spelling of the Calling AE Title is the same on the device as it is in SCU_List.dic. Confirm that the current version of SCU_List.dic is imported into the appropriate DICOM Gateway (option 4-2-7.

> For details about how SCU_List.dic is used by the Q/R application, see the *VistA Imaging DICOM Gateway User Manual*.

## Invalid Called AETitle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: This section applies to MAG\*3.0\*99 and earlier gateways.

> ERROR - MAG DICOM CHECK AE TITLE: \[-2,No entry for AE Title \\\<AETitle\>\\.

> INFO - ...throwing due to rejected CalledAETitle, \<AETitle\>, for \<hostname of SCU\>.

> This error occurs if the Called AETitle is rejected.

> Confirm that this device should have access to VistA Imaging. Confirm that the spelling of the Called AE Title is the same on the device as it is in SCU_List.dic entry for the Q/R application. Confirm that the current version of SCU_List.dic is imported into the appropriate DICOM Gateway.

## Study Level Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Currently, only supports Study Level.

> This error occurs if the remote DICOM device (SCU -- Service Class User) was attempting to perform a query or move using a level other than Study; currently, the Q/R application only supports Study Level queries and moves.

> This action must be corrected at the remote DICOM device (SCU).

## Assembling DICOM Object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Failure to assemble Dicom Object.

> This error occurs if the Q/R application was not able to build a DICOM Object during the reconstitution process. This may occur before a DICOM object is sent out to the remote Storage SCU device. If it does occur, the DICOM object is not sent.

> Contact the CLIN 3 team for assistance.

> Chapter 2 DICOM Query/Retrieve Server Error Messages

## Null Pointer Exception

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - java.lang.NullPointerException

> This error occurs if a Java variable is set to NULL and some action is acting upon the NULL value. Contact the CLIN 3 team.

## Querying Whole Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ERROR - Query request failed...-2,Errors encountered No permission to query whole database.

> This error occurs if the query request from the remote DICOM device (SCU) does not contain any query parameters, or if the request has too many *wildcard* values in its parameters.

> To prevent this from happening, ensure that the remote DICOM device (SCU) has at least one query parameter with a value for filtering. Examples would be the Patient Name field contains *SMITH\ for only Smith’s studies or the Accession# field contains *010307-1234* for a single specific study.

## Duplicate Study Instance UID during a C-Move operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error: VistA Imaging contains Duplicate Study Instance UID.

> The C-Move operation failed to move images to the requested DICOM device. This happens when more than one Study in the database contains the same Study Instance UID. This is done to protect the user/clinician from receiving the wrong patient and/or order. There is no work around. One of the orders must be corrected.

> Chapter 2 DICOM Query/Retrieve Server Error Messages

> This page is intentionally blank.

# Chapter 3 DICOM Storage SCP Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter contains a listing of the error messages generated by the DICOM Storage SCP (Service Class Provider). These error messages are written to the Hybrid DICOM Image Gateway (HDIG) application log, which is called ImagingExchangeWebApp.log and is located on the computer on which the HDIG is installed in the folder C:\Program Files\Apache Software Foundation\Tomcat 6.0\logs\\

> Date and time may be amended to the name of the log file. For example, ImagingExchangeWebApp.log.2011-06-21.

> Users with the security key MAG VIX ADMIN can view the HDIG log using the URL to the Java Logs page. For more information about accessing the HDIG log, see the *VistA Imaging DICOM Gateway User Manual*.

## Initialization Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DICOM Listener could not Start on Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) Port \<port#\> failed to start listening. Refer to other logs for more detail.

> \(J\) Error listening for SCU Requests on port \<port#\>

> The DICOM Listener could not start on this port (the port may already be in use), use the netstat –a command, in a Command Prompt window, to find out. After resolving this problem, restart the Apache Tomcat listener (using Component Services).

## Calling AETitle Rejected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) The calling AETitle does not have permission to access VistA Imaging. This permission is configurable using DICOM AE Security Matrix.

> (J)...throwing due to rejected CallingAETitle \<caet\> for \<srcIPAddress\>.

> OR

> \(S\) The calling AETitle, \<caet\> does not have permission to perform a C-Store DIMSE Service.

> This permission is configurable using DICOM AE Security Matrix.

> \(J\) …: \<caet\> is invalid to perform C-Store Requests.

> Edit the DICOM AE Security Matrix.

> Chapter 3 DICOM Storage SCP Error Messages

## Called AETitle Rejected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) The called AETitle does not have permission to access VistA Imaging. This permission is configurable using DICOM AE Security Matrix.

> (J)...throwing due to rejected CalledAETitle \<caet\> for \<srcIPAddress\>.

> Edit the AE Security Matrix.

## AETitle Authentication Association Request Rejected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) AETitle Authentication internal exception thrown. Refer to other logs for more detail.

> \(J\) …: AETitle Authentication internal exception thrown during Association Request. Throwing Association Rejection.

> Contact the CLIN 3 team with detailed information (HDIG error).

## DICOM Toolkit Internal Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) DICOM Toolkit internal exception thrown. Refer to other logs for more detail.

> \(J\) …: Exception thrown while DCF was creating DICOM Session Settings. Throwing Association Rejection.

> Contact the CLIN 3 team with detailed information (HDIG DCF toolkit setting/configuration error)

## DICOM Toolkit Configuration File Read Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) Failed to read information from the DCF Configuration file. The HDIG will not function properly with this failure.

> \(J\) …: Exception thrown while reading Attributes from DCF configuration file.

> Contact the CLIN 3 team with detailed information (HDIG DCF toolkit configuration error in: x\DCF_RunTime\cfg\apps\default\Listen). After resolving the issue, please restart the Apache Tomcat listener (using Component Services).

## Data Processing Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IOD Violations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) Received object contains IOD Violations. Object dumped on local disk as \<path and filename\> for review.

> \(J\) Dumped object to local disk due to IOD Violations: \<path and filename\>

> Dump the DICOM object using one of the command line DICOM header dump tools (DCF’s dcf_dump utility is on every HDIG, as part of the toolkit run-time deployment), after viewing the log file for particular IOD validation errors, contact the vendor and the CLIN 3 team.

> Chapter 3 DICOM Storage SCP Error Messages

> If the Relax Validation flag is set to *Yes* for the calling AE (SCU) in the AE Security Matrix, only the Patient Name, ID, Accession Number, the Study/series/SOP UIDs, and a few display parameters (Photometric Interpretation, Rows, Columns, Bits Allocated and Bits Stored) are checked for validity; otherwise, the entire Image header with all tags is checked.

## Unexpected Data in IOD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: Exception thrown while validating object IOD.

> \<IOD violation details\>

> The validation process failed due to unexpected data in the IOD.

## Unknown SOP Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unknown SOP Class for IOD Validation: \<SOP class\>

> Encountered a SOP class that is not in the data definitions for IOD validation.

## Error Status or Message Delivery Failure to remote Storage SCU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to set error status and/or message for \<problem\> in c_store_rsp response -

> \<RemoteAETitle/thread ID\>

<span class="mark">REDACTED</span>

## Storing Object Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) Failed to store object to VistA Imaging, received from AETitle \<remote AE\>, SOP Instance UID \<sop_instance_uid\>.

> \(J\) …: DICOM Storage SCP Exception thrown while storing object received from \<remote AE/ThreadID\>

> \(J\) …: DCS Exception - Could not read Presentation Context ID from Association/DIMSE message. - \<remote AE/ThreadID\>

> Error in metadata related transaction processing, streaming to RAID, not enough memory, or DICOM communication.

> Check if the physical memory of the Gateway is less than 4GB; if it is, then follow the procedure in the *MAG\*3.0\*34, MAG\*3.0\*116, and MAG\*3.0\*118 Planning and Installation Instructions* to increase virtual memory for the HDIG Apache Tomcat process and restart it.

> For RAID, check the network share (authentication) settings for the RAID location. For DICOM communication, collect all available logs and contact the CLIN 3 team.

## Queuing E-mail Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Process error while queuing Email for \<message\> - \<calling AEtitle/threadID\>

> Error in submitting e-mail information into the E-mail Queue. Make sure the legacy DICOM Gateway configuration (e-mail address, port, and SMTP server address) are configured properly and they are populated to the VistA server-side DB.

> Chapter 3 DICOM Storage SCP Error Messages

## DICOM Legacy Gateway Configuration Loading Failed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: Failed to load Legacy DICOM Gateway Configuration …

> Make sure the legacy DICOM Gateway configuration items (e-mail address, port, SMTP server address, and the Importer flag) are configured properly and populated to the VistA server-side DB.

## No DICOM Instruments Defined in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) There are no DICOM instruments defined.

> \(J\) DICOM instrument configuration is empty.

> Make sure the legacy DICOM Gateway Instrument.dic configuration file is properly filled and is populated to the VistA server-side DB.

## HDIG and DICOM Gateway Site IDs do not Match

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HDIG site ID=\<hdig-siteID\> does not match DGW site ID=\<DgwSiteID\>

> The HDIG installer has a different site ID than the legacy gateway.

> Make sure the legacy DICOM Gateway Site setting matches with the HDIG siteId (C:\VixConfig\DicomServerConfiguration.config file siteId setting).

## Formatted Data/UID Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inserting \<tag In Seq\> with UID \<tagValue\> to Original Attribute sequence Failed -

> \<callingAE\> -\> \<listener port#/threadID\>

> DICOM error (poorly formatted data/UID). Collect all available logs and contact the CLIN 3 team.

## Write Out DICOM Object Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Could not create file to write out DICOM object \<callingAE\> -\> \<listener port#/threadID\>

> Error creating DICOM object in C:\DICOM\\ Image_In folder for legacy image processing.

## DICOM Filename and IEN Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Could not write to temporary DICOM file \<callingAE\> -\> \<listener port#/threadID\>

> Error creating a DICOM filename (C:\DICOM\\ Image_In) and IEN for the entry or error creating the entry on the assigned TCP port for legacy image processing.

## DICOM File to RAID Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …; Error Writing Input Stream to \<filespec\> \<callingAE\> -\> \<listener port#/threadID\>

> Error writing the DICOM file to RAID, check the share location settings and space on the drive.

> Chapter 3 DICOM Storage SCP Error Messages

## E-mail to Queue Message Table Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PostEmailQueueCommandImpl.java:xx\] - …

> Error writing e-mail into the Queue Message table (file \#2006.928).

## Connection Settings Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: ConnectionException thrown while correcting DICOM File. \<callingAE\> -\> \<listener port#/threadID\>

> Error processing an object as a result of Connection settings to the VistA database.

## E-mail Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[ProcessEmailQueueCommandImpl.java:xx\] - …

> Error sending e-mail.

## Requeuing E-mail Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to requeue Email for \<recipient(s)\>. No Email will be sent.

> Error requeuing failed e-mail transfer.

## Create Icon Image Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: Failed to create icon image.

> Error creating a thumbnail from the pixel data of the processed object.

## Unable to Find Current File Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: Icon Image Creation: Could not find file \<currentFile\>.

> Could not find \<*currentfile*\>.

## Reading Current File Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> …: Icon Image Creation: IO problem with file \<currentFile\>.

> Error reading \<*currentfile*\> .

## Requeuing After Failed Icon Creation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to requeue \<SOP Instance IEN\> to create Icon Image. No Icon Image will be created.

> Icon Creation request could not be re-queued after failed icon creation.

## Create Icon Image Failure After Maximum Retries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to create Icon Image for \<SOP Instance IEN\> after maximum number of retries. No Icon Image will be created.

> Icon Creation failed. No icon image is created.

> Chapter 3 DICOM Storage SCP Error Messages

## DICOM Router Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Error getting DicomRouter instance. Application deployment is probably incorrect.

> Try to reinstall the HDIG MSI file after stopping the application.

## DICOM Object Contains VR Error for Critical Element

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IOD minimum VR check error in object=\<SOP Instance UID\> of Series=\<Series Instance UID\>.

> The received DICOM object contains a Value Representation (VR) error for a critical element. Since the error is in a critical element, the DICOM object is automatically rejected. After viewing the log file and/or email for the specific VR error, contact the vendor and the CLIN 3 team.

## Storage Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## URL not Following CIFS Convention Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MalformedURLException creating SMB server share, \<message\>.

> The URL does not follow the Common Internet File System (CIFS) naming convention (file://ServerName.Domain:Port/Directory/Filename). If the NETWORK LOCATION file value of the … field does not conform to the CIFS format, this message is generated.

## HDIG Unable to Access SMB File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \(S\) UnknownHostException opening SMB file \<filename\>, \<Message\>

10) IOException opening SMB file \<filename\>, \<Message\>

> HDIG cannot access the file, or cannot open/read it. Possible causes are as follows:

- Share (defined in NETWORK LOCATION) is incorrectly defined.
- The authentication is not correct: definition in (NETWORK LOCATION, etc.) vs. real share.
- The Shared device is not accessible.
- The network is down.

## Storage Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DICOM Storage SCP IOD Validation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Storage process will continue for this object.

> Chapter 3 DICOM Storage SCP Error Messages

## DICOM Storage SCP Processing/DB Connection Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fatal Error: CANNOT COPY FILE TO SERVER

## Archiving Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following errors can occur during archive (asynchronous write) and initial storage (synchronous write).

## Failed to Write Stream to Disk Filename

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to write stream to disk filename \<*full File Specification*\>

> \<*IO subsystem error message*\>; Error Writing Input Stream to \<*full File Specification*\>.

> The object is not saved properly on the given media.

## Failed to Delete Incomplete File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed to delete incomplete file \<*full File Specification*\>

> The object that is not saved properly on the given media could not be removed.

## Archive Configuration Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \<*N*\> unsatisfied maps detected for artifact \<*artifact-ID*\>

> One error that shows before archiving occurs when the Archive is not configured properly.

> Chapter 3 DICOM Storage SCP Error Messages

> This page is intentionally blank.

# Chapter 4 DICOM Importer II Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter contains a listing of error messages generated by the DICOM Importer II GUI. These error messages are displayed in the GUI as message boxes, and are also captured in the application log file.

## General Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Work Item Not Found

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *The selected work item was not found on the server. It may have been deleted*.

> This message is displayed when the user attempts to perform an action on a work item that has been deleted. It is primarily informational, as the software will take appropriate action based on the context. For example, if a user tries to submit a work item that has been deleted while they were working on it, the user will be returned to the appropriate start screen to begin working on a new task.

## Work Item in Invalid Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text sample: *Work item 47 has a status of InReconciliation, not the expected status of ReadyForImport*.

> This message is displayed when the user attempts to perform an action on a work item, but its expected status has been changed in the meantime. It is primarily informational, as the software will take appropriate action based on the context. For example, if a user tries to submit a work item, but another user has already submitted it, the user will be returned to the appropriate start screen to begin working on a new task.

## Work in Progress

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *You currently have work in progress. You must either cancel it or wait for it to complete*.

> This message is displayed if the user chooses to shut down, log out, or navigate to a different screen while background work is in progress.

## Importer Item Failed Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Server *vhaxxxdig1* at Site *xxx*

> Chapter 4 DICOM Importer II Error Messages

## Staging and Direct Import Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Drive Not Ready

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text sample during Direct Import: *Drive E cannot be read from at this time. Direct Import cannot continue*.

> Message text sample during Staging: *Drive E cannot be read from at this time. Staging cannot continue*.

> This message is displayed during Direct Import if the drive selected by the user is unavailable for some reason. The user should make sure a CD/DVD is actually inserted in the drive.

## Folder Doesn’t Exist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *The specified folder does not exist. Please choose another folder*.

> This message is shown in Direct Import if the user selects a folder to read from, but the folder is deleted from the file system prior to attempting the Import scan. The solution is to select a folder that exists on the file system.

## Media Has Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *Something is wrong with CD/DVD disk. The disk does not appear to be the same one that was used at the start of the Importer session. Could the original disk have been removed and another one inserted into the drive?*

> This message is displayed when the user attempts to submit a direct import for processing or attempts to initiate a staging operation, but the CD/DVD in the drive is different from the one in the drive at the start of the operation. The user can return the original media to the drive and try again, or they can cancel their current operation and start over.

## Order Selection Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Outside Locations Not Configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *The Procedure List could not be loaded. The most likely cause is that no Outside Imaging Locations have been configured. Until this configuration issue is corrected, you will not be able to complete any reconciliations. Please contact an administrator for assistance*.

> This message is displayed when the user reaches the order selection or creation screen in a reconciliation, but the administrator has not configured any outside locations, which results in an empty procedure list. The solution is for an administrator to configure the outside locations as described in the installation manual.

> Chapter 4 DICOM Importer II Error Messages

## Valid Study Date Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *A valid study date is required. Please enter a date on or before today, in DICOM (YYYYMMDD) format*.

> This message is displayed if the user, during reconciliation, wishes to create a new Radiology order, but the DICOM header for the study has a missing or invalid study date. The solution is for the user to input a valid date, in DICOM format, into the provided field in the GUI.

## Reports Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Invalid Report Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This message is displayed when the user is requesting a report, but the report parameters are invalid. The message will be some combination of the following sub-messages:

- *You must select a report type.*
- *You must select a report style.*
- *The Start Date must be less than or equal to the End Date.*
- *The Start Date must be less than or equal to today's date.*

> The solution is to fix the identified problem

## Image Viewing Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DICOM Viewer Not Found

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This message is displayed when attempting to view images from the study details page, and the DICOM Viewer (MAG_DCMView.exe) is not installed on the workstation. The solution is to contact an Administrator to have the DICOM Viewer installed on the workstation.

## Invalid Instance Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This dialog is displayed when the user is viewing study details and attempts to view one or more images using the DICOM Viewer. The user is required to enter the image number (for example, 4), or a range of numbers (for example, 6-15) for the image or images they would like to view. There are a variety of detailed validation messages that may be displayed here if the range is invalid. For example, there are 6 images in the selected series, and the user requests image 7. Or there are 5 images in the series and they request images 4-9. The detailed error messages should be sufficient to guide the user into correctly specifying a valid range of images.

> Chapter 4 DICOM Importer II Error Messages

## Too Many Instances Selected

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Message text: *There are too many instances in the range you have selected. Please select a smaller range of instances to view*.

> There is a limit to the size of the command line that can be passed to the external DICOM viewer (MAG_DCMView.exe). If the user is looking at the study details, and requests to view an excessive number of images from a study at one time, this command line length may be exceeded. In this case, the message will be displayed. The solution is for the user to select a smaller sized range of images to view.