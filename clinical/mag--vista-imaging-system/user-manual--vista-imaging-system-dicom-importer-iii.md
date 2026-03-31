---
title: VistA Imaging System DICOM Importer III User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: VistA Imaging System DICOM Importer III
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
menu_options: 2
description: "- [March 2019 – Revision 16](#march-2019-revision-16) - [Preface](#preface) - [Terms of Use](#terms-of-use) - [Document Conventions](#document-conventions) - [Getting Help](#getting-help) - [Contents](#contents) - [Chapter 1: Introduction](#chapter-1-introduction) - [How the Importer III Client Work"
audience: 
keywords: 
  - importer
  - dicom
  - blockquote
  - media
  - study
  - table
  - client
  - contents
  - imaging
  - import
page_count: 0
word_count: 14216
section_count: 46
table_count: 4
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_dicom_importer_iii_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_dicom_importer_iii_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-system-dicom-importer-iii-user-manual/001.png)

VistA Imaging System DICOM Importer III User Manual

# March 2019 – Revision 16


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [March 2019 – Revision 16](#march-2019-revision-16)
- [Preface](#preface)
  - [Terms of Use](#terms-of-use)
  - [Document Conventions](#document-conventions)
  - [Getting Help](#getting-help)
- [Contents](#contents)
- [Chapter 1: Introduction](#chapter-1-introduction)
  - [How the Importer III Client Works](#how-the-importer-iii-client-works)
  - [User Roles](#user-roles)
  - [Associated Security Keys](#associated-security-keys)
- [Chapter 2: Setting Up the Importer III Client](#chapter-2-setting-up-the-importer-iii-client)
  - [Prerequisites](#prerequisites)
  - [Configuring the Importer III Client](#configuring-the-importer-iii-client)
  - [Verifying the Installation](#verifying-the-installation)
  - [Starting the Importer III Client](#starting-the-importer-iii-client)
  - [Stopping the Importer III Client](#stopping-the-importer-iii-client)
- [Chapter 3: Staging the Data](#chapter-3-staging-the-data)
  - [Intake Staging](#intake-staging)
  - [DICOM Correct](#dicom-correct)
  - [Network Import](#network-import)
  - [Non-Compliant Media](#non-compliant-media)
  - [User Roles for Staging](#user-roles-for-staging)
  - [Staging Media when a Patient Record Exists in VistA Imaging](#staging-media-when-a-patient-record-exists-in-vista-imaging)
  - [Staging Media When a Patient Record Does Not Exist in VistA Imaging](#staging-media-when-a-patient-record-does-not-exist-in-vista-imaging)
  - [Advanced Staging of Patient Data](#advanced-staging-of-patient-data)
- [Chapter 4: Working with Studies and Orders (Reconciling)](#chapter-4-working-with-studies-and-orders-reconciling)
  - [Direct Import of Electronic Media](#direct-import-of-electronic-media)
  - [Import Reconciliation Workflow Industry Standard for DICOM Import](#import-reconciliation-workflow-industry-standard-for-dicom-import)
  - [Reconciling](#reconciling)
  - [User Roles](#user-roles-1)
  - [Entering the Reconciliation Workflow Through Direct Import](#entering-the-reconciliation-workflow-through-direct-import)
  - [Reconciling Studies with Existing Orders](#reconciling-studies-with-existing-orders)
  - [Reconciling Studies Requiring New Radiology Orders](#reconciling-studies-requiring-new-radiology-orders)
  - [Adding and Changing Exam Details During Reconciliation](#adding-and-changing-exam-details-during-reconciliation)
  - [Reconciling Partially Imported Studies](#reconciling-partially-imported-studies)
  - [Deleting Studies from Staged Media](#deleting-studies-from-staged-media)
- [Chapter 5: Managing Import Queues](#chapter-5-managing-import-queues)
  - [Reverting Items Stuck in Reconciliation](#reverting-items-stuck-in-reconciliation)
  - [Viewing Importer Items Currently Being Processed by an HDIG](#viewing-importer-items-currently-being-processed-by-an-hdig)
  - [Viewing Failed Importer Items](#viewing-failed-importer-items)
  - [Viewing the Application Log File](#viewing-the-application-log-file)
- [Chapter 6: Viewing Study Data and Images](#chapter-6-viewing-study-data-and-images)
  - [Optionally Viewing the DICOM Header and Group Information](#optionally-viewing-the-dicom-header-and-group-information)
- [Chapter 7: Running Usage Reports](#chapter-7-running-usage-reports)
  - [Sample Reports](#sample-reports)
  - [User Role](#user-role)
  - [Running a Usage Report](#running-a-usage-report)
- [Appendix A: Setting Up Outside Imaging Locations for the Importer III Client](#appendix-a-setting-up-outside-imaging-locations-for-the-importer-iii-client)
  - [Step 1 – Identify Imaging Types and Divisions that Need “No Credit” Imaging Locations](#step-1-identify-imaging-types-and-divisions-that-need-no-credit-imaging-locations)
  - [Step 2 – Create the OUTSIDE STUDY Entry in the CAMERA/EQUIP/RM File](#step-2-create-the-outside-study-entry-in-the-cameraequiprm-file)
  - [Step 3 – Add New Outside Imaging Locations for Each Imaging Type to Divisions](#step-3-add-new-outside-imaging-locations-for-each-imaging-type-to-divisions)
  - [Step 4 – Define Outside Imaging Locations Parameters](#step-4-define-outside-imaging-locations-parameters)
  - [Step 5 – OUTSIDE STUDY Camera/Equip/Room for All Radiology Imaging Locations](#step-5-outside-study-cameraequiproom-for-all-radiology-imaging-locations)
  - [Step 6 – Populate VistA Imaging Outside Imaging Location File](#step-6-populate-vista-imaging-outside-imaging-location-file)
- [Appendix B: Handling Parent-Descendent Procedure Orders with the Importer III Client](#appendix-b-handling-parent-descendent-procedure-orders-with-the-importer-iii-client)
  - [How It Works](#how-it-works)
  - [Questions](#questions)
- [Appendix C: Problems Seen in Importing DICOM Objects from Media](#appendix-c-problems-seen-in-importing-dicom-objects-from-media)
- [Glossary](#glossary)
- [Index](#index)
    - [A](#a)
    - [B](#b)
    - [C](#c)
    - [D](#d)
    - [G](#g)
    - [I](#i)
    - [M](#m)
    - [N](#n)
    - [O](#o)
    - [P](#p)
    - [R](#r)
    - [H](#h)
    - [S](#s)
    - [T](#t)
    - [U](#u)
    - [V](#v)
    - [W](#w)
> DICOM Importer III User Manual VistA Imaging
> March 2019
> Property of the US Government
> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.
> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.
> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies and are hereby acknowledged.
> VistA Imaging Office of Enterprise Development Department of Veterans Affairs
> Internet: [REDACTED](https://vaww.edis2.med.va.gov/main)
> VA intranet: [REDACTED](https://vaww.edis2.med.va.gov/main)
> Revision History
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Rev</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>June 3, 2011</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Document created for MAG*3.0*118. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>November 29, 2011</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>Document updated to reflect changes to the GUI for Beta testing. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>March 16,</p>
<p>2012</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>Major edit – Verified and updated procedures, edited content, and updated formatting and styles. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>April 9,</p>
<p>2012</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>Document updated to reflect changes from the Formal Review WPR. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>September 18, 2012</p>
</blockquote></td>
<td>5</td>
<td><blockquote>
<p>Major edit – Added and updated procedures, and edited content. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>October 29,</p>
<p>2012</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>Major content edits and update. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>January 22,</p>
<p>2013</p>
</blockquote></td>
<td>7</td>
<td><blockquote>
<p>Incorporated comments from VA Formal WPR – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> l</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>February 25,</p>
<p>2013</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>Incorporated comments from VA eWPR – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>August 30,</p>
<p>2013</p>
</blockquote></td>
<td>9</td>
<td><blockquote>
<p>Updated in full for Patch 136. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>January 15,</p>
<p>2016</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>Added the Configuring Maximum Number of Items to Return section under Chapter 2’s Configuring the Importer III Client section in support of MAG*3.0*162. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>June 2, 2016</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>Edits in support of MAG*3.0*162.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>May 22,</p>
<p>2017</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>Edits in support of MAG*3.0*179. Added to the Prerequisites list and added section on Window Registry (page 9). Also added new instructions for 2FA sign on with PIV (page 16).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>March 20,</p>
<p>2018</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>Updated document with Patch 206 (Replacement of cancelled Patch 179); Same Functionality</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>April 11,</p>
<p>2018</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>Edits in support of MAG*3.0*206.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>August 1,</p>
<p>2018</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>Remove Patch reference from the title page and footer.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>March 18,</p>
<p>2019</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>Edits in support of MAG*3.0*237. Updated .NET version <strong>.NET 4.6.2</strong> Only p. 7, 8.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use of the DICOM Importer III is subject to the following provisions:

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-dicom-importer-iii-user-manual/002.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>Caution</strong>: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-dicom-importer-iii-user-manual/003.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Caution</strong>: The FDA classifies VistA Imaging, and the DICOM Importer III (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, such as the installation of unapproved software, will adulterate the</p>
<p>medical device. The use of an adulterated medical device violates US federal law (21CFR820).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses the following typographic conventions.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 32%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Symbol/Typeface</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Meaning/Use</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>User input, selection, GUI element (menu item, button, field)</p>
</blockquote></td>
<td><blockquote>
<p>Click <strong>Finish</strong>.</p>
<p>Choose <strong>Open</strong> from the <strong>File</strong> menu.</p>
<p>Type the user account name in the <strong>Name</strong></p>
<p>field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Monospaced font (typically in a box)</p>
<p>(Bold indicates user input or selection).</p>
</blockquote></td>
<td><blockquote>
<p>Command-line sample or output (such as character- based screen captures and computer source code), menus, file names</p>
</blockquote></td>
<td><blockquote>
<p>Navigate to the \Docs\Imaging_Docs_Latest folder.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>Italics</em></p>
</blockquote></td>
<td><blockquote>
<p>Emphasis, reference to section in the document or another document, or a variable</p>
</blockquote></td>
<td><blockquote>
<p>For more information, see the <em>VistA Imaging DICOM Gateway Installation Guide</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Square brackets, monospace or italics</p>
</blockquote></td>
<td><blockquote>
<p>Variable, placeholder, VistA menu</p>
</blockquote></td>
<td><blockquote>
<p>Access the Kernel Installation and Distribution System Menu [XPD MAIN].</p>
<p>;;3.0;IMAGING;[Patch List];Mar 19,</p>
<p>2002;Build 1989;Feb 21, 2011</p>
<p>MAG*3.0*&lt;<em>PatchNumber</em>&gt;.KID</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[REDACTED](https://vaww.edis2.med.va.gov/main)

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Chapter 1: Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Digital Imaging and Communications in Medicine (DICOM) Importer III (hereafter referred to as the Importer III client) is a client/server application that utilizes desktop client software, supported by server software on the Hybrid DICOM Image Gateway (HDIG), to transfer DICOM objects from studies performed outside the Department of Veterans Affairs (VA) into the VistA Imaging system. The Importer III client supports sharing prior study images from:

- VA Polytrauma clinicians
- Imaging facilities outside the VA
- Imaging facilities contracted to perform studies outside the VA

> This software streamlines the reconciliation of patient names and study identifiers between the outside study data and VA systems. The software breaks the processing down into three independent steps:

- Staging – A user with appropriate privileges copies studies (for example, CD, DVD, flash drive, or external hard drive) to a network share for reconciliation by an authorized user.
- Reconciliation – A user with appropriate privileges associates the images on the media with the correct ordered study and the correct patient.
- Importing –A user with appropriate privileges adds the images to the patient’s electronic health record (EHR).

## How the Importer III Client Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The graphical user interface of the Importer III client is built on the VistA Imaging System Architecture (VISA) within a desktop client.

> The desktop-based approach allows multiple users to simultaneously perform staging/import/reconciliation activities, using the client hardware (media drives) and software (Importer III client), and to stage study data (external media) for later reconciliation and importing. It eliminates the need to have direct access to a server to perform import activities.

> In addition, the Importer III client provides administrative users with a tool for managing problems as they appear in the DICOM Correct queue. All studies in the DICOM Correct queue are managed from the Importer III client, which corrects the study and resubmits it to image processing.

#### Workflow Wizards

> Based on the user role of the individual who signs on, Importer III loads one of four workflow wizards. The wizards walk the users through the necessary steps to perform their designated duties.

#### Work Queues

> Advanced users will use the Importer III client to perform reconciliation and importing activities. As studies are processed, their status changes and they are placed in different workflow queues.

#### Features

> The Importer III client:

- Enables authorized users to manage, reconcile, and correct imported data from a single easy- to-use interface.
- Receives outside DICOM-compliant studies from portable media.
- Receives outside DICOM-compliant studies through a network transmission.
- Receives non-DICOM objects (such as .pdf files) and enables authorized users to add them to patients’ EHRs.
- For non-DICOM compliant media (that is, an invalid or missing DICOMDIR), attempts to build a list of the studies on the media, and proceeds with the staging/importing of the DICOM objects.
- Manages the DICOM Correct functionality by placing studies that fail image processing into a DICOM Correct work queue for resolution by the Imaging Administrator.
- Gives multiple authorized users the ability to access, manage, and reconcile the imported data based on the rights associated with their user role.
- Provides a tool to display the status of a study within the reconciliation process.
- Captures and stores DICOM objects received from multiple devices at different times.
- Provides a reporting system that enables an authorized user to monitor and generate usage or statistical reports.
- Utilizes audit logging, application logging, and sensitive patient logging.

## User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client is a role-based application. Regardless of a user’s job title, each role falls into one or more of the following categories based on tasks required to handle patient data at the site hospital. The following roles are associated with the Importer III client.

- Basic Media Staging User (BMSU)
- Advanced Media Staging User (AMSU)
- Contracted Study Reconciliation Administrator (CSRA)
- Artifact Reconciliation Administrator (ARA)
- Report User (RU)

> Each chapter of this user manual provides the information necessary to perform a major task associated with the Importer III client. Within each chapter is a discussion of how a particular user role (or roles) applies to that task.

> Note: Roles can be combined when performing these tasks. Refer to the individual chapters of this manual to determine how roles can be combined for the described task.

> Important: VistA Imaging users cannot access the Importer III client or data unless they have the appropriate security key. See the section [*Associated Security Keys*](#associated-security-keys) at the end of this chapter for more information.

#### Basic Media Staging User

> The BMSU is the person performing the staging. A BMSU may be file room staff, front desk registration staff, or other staff having minimal medical knowledge. The responsibilities of the BMSU are as follows.

- Receive media from the patient.
- Log into the Importer III client, search for the patient, and select the patient.
- Copy contents from external media to the network staging location.

#### Advanced Media Staging User

> The AMSU performs the staging. An AMSU may be file room staff, front desk registration staff, or other staff having some medical knowledge. The responsibilities of the AMSU are:

- Receive media from the patient.
- Log into the Importer III client, search for the patient, select the patient, and optionally view/select individual studies from the media.
- Copy selected studies from external media to the network staging location.

#### Contracted Study Reconciliation Administrator

> The CSRA is a clinician who identifies the original order for a contracted study, performed by an outside facility, for the patient. A CSRA matches the outside contracted study to the original order so that it can be imported. The CSRA also has the required medical knowledge to perform reconciliation activities on orders placed in VistA, and to have a study performed at an outside location. The responsibilities of the CSRA are:

- Possess all the capabilities designated to the AMSU.
- Work with orders that already exist on VistA.
- Select the procedure/study previously ordered by the provider and match the appropriate staged study to the selected order.
- Designate the study for “*I*”mporting.
- Ensure that the imported study is in VistA Imaging for use by medical staff.

> Important: The CSRA is not allowed to import and process unordered studies. If the CSRA encounters an unordered study that needs to be imported, the workflow for the Staging user is used.

#### Artifact Reconciliation Administrator

> Note: This is the power-user role.

> The ARA is a clinician with in-depth knowledge of the radiology workflow. ARA will identify a VistA order that corresponds to a procedure performed by a non-VA imaging facility. The responsibilities of the ARA are:

- Manage all aspects of the reconciliation process, including the ability to create new radiology orders, match artifacts to existing studies, update or delete information, perform DICOM Correct functions, and perform all AMSU, CSRA, and RU functions.
- Identify the VistA procedure that corresponds to the one performed on the outside for a prior study.
- Log into the Computerized Patient Record System (CPRS) and identify the patient and procedure/study on the system or, if necessary, create and register a new procedure/study.
- Use the patient’s identifying information to retrieve the staged data from the network storage location.
- Reconcile any staged data by matching it with orders and ensure that the reconciled orders are released to the picture archiving and communication system (PACS) system.
- Release the procedure/study to image processing for storage in the VistA Imaging file system, ensuring the imported study is available to the medical staff treating the patient.
- Reconcile studies sent to the DICOM Correct queue to ensure the information is available to clinicians in a timely manner.

#### Report User

> The responsibilities of the RU include generating reports on statistical data, such as the number of studies imported, the number of studies requiring manual reconciliation, and so on.

> Note: This role is for an administrator interested in gathering statistics on system processing.

## Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each user role is associated with security keys that provide rights, from minimum rights (BMSU) to maximum rights (ARA).

> Note: Users of any of the following security keys must also have access to the MAG DICOM VISA secondary menu option.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>KEY NAME</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAGV IMPORT MEDIA STAGER</td>
<td>Users holding this security key may use the Importer III client to stage (copy) from media to the staging persistent storage, where it waits for reconciliation processing.</td>
</tr>
<tr class="even">
<td>MAGV IMPORT STAGE MEDIA ADV</td>
<td><p>Users holding this security key may use the Importer III client to perform all functions of the MAGV IMPORT MEDIA STAGER security key plus the following:</p>
<ul>
<li><p>Stage (copy) studies from media to staging to persistent storage.</p></li>
<li><p>View images on the media.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>MAGV IMPORT RECON CONTRACT</td>
<td>Users holding this security key may use the Importer III client to perform all functions of the MAG IMPORT STAGE MEDIA ADV security key. In addition, users may use the Importer III client to associate study DICOM objects with an existing Rad/Consult order for reconciliation.</td>
</tr>
<tr class="even">
<td>MAGV IMPORT RECON ARTIFACT</td>
<td><p>Users holding this security key may use the Importer III client to perform all functions of the MAGV IMPORT RECON CONTRACT security key plus the following:</p>
<ul>
<li><p>Place new radiology orders through the Importer III client.</p></li>
<li><p>Perform DICOM Correct activities to manage problem studies in the DICOM Correct queue.</p></li>
<li><p>Perform queue management activities.</p></li>
<li><p>Perform reporting activities.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>MAGV IMPORT REPORTS</td>
<td>Users holding this security key may use the Importer III client to view and print Importer reports, as well as save the contents of a report to a text file.</td>
</tr>
</tbody>
</table>

# Chapter 2: Setting Up the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter provides information for setting up the Importer III client on a VistA Imaging system.

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VistA Imaging system running MAG\*3.0\*136 or later
- Microsoft .NET 2.0 and .NET 4.6.2 installed
- “Servers” key in the Windows Registry

> Contact system administration at your site for more information, and to perform any of the following applicable tasks.

- Permission may be required to use the CD/DVD on the local computer where the Importer III client is going to be used for importing. Permission may be granted through VA IT group permissions.
- The computer containing the Importer III client must have the correct drivers installed to use the drives on the computer.
- If the Importer III client is installed on a Windows XP computer, then the correct codecs must be installed to allow the reading of CDs and DVDs.
- When the Importer III client is installed on a Windows 7 computer, the correct codecs allowing the reading of CDs and DVDs are included.

> Note: The Importer III client may be set to read CD-Rs and DVD-Rs by default. Issues may arise if a CD-RW or DVD-RW is placed in a drive and Import is launched.

#### Microsoft .NET Framework

> Microsoft .Net Framework 2.0 and 4.6.2 must be installed prior to installing the Importer III client.

1.  To verify that .NET 2.0 and .NET 4.6.2 are on the PC, select Start \| Settings \| Control Panel

#### \| Add or Remove Programs.

2.  Scroll to find Microsoft .NET Framework 2.0 and Microsoft .NET Framework 4.6.2. If they are installed, then go to the next section, [*Installing the Importer III Client*](#installing-the-importer-iii-client).

> ![](vista-imaging-system-dicom-importer-iii-user-manual/004.png)Figure 1: Add or Remove Programs Screen

3.  If the listed .NET Framework is not listed, then please contact the System Admin to get it installed.

#### Windows Registry

> With the addition of the RPC Broker as part of the 2FA effort, Importer will now rely on VistA server information available in the Windows Registry for each client computer that installs the Importer application. This registry setting is a requirement of the RPC Broker and some other VistA client applications; it is possible that the settings already exist on a client computer, however it should be confirmed before installing Importer. As mentioned above, the following may require support from local site administrators.

> Open the Registry Editor and browse to the

> \HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node key. If a “Vista” key exists, expand it, if not create it. If a “Broker” key exists, expand it, if not create it. If a “Servers” key exists, expand it, if not create it so that the full path is:

> \HKEY_LOCAL_MACHINE\SOFTWARE,Wow6432Node\Vista\Broker\Servers

> Within this key, one (or more) String values are required. The name of Registry String should contain the IP address or Fully Qualified Domain Name (FQDN) of the VistA server, a comma, and then the port number that will accept remote connections. See the figure below:

> ![](vista-imaging-system-dicom-importer-iii-user-manual/005.png)Figure 2: Registry Editor Screen

#### Installing the Importer III Client

> The Importer III client must be installed on any system where a user performs staging, reconciliation, reporting, or DICOM Correct activities. Use of the Importer III client is security key driven, so that only users who have the required security keys are able to log in and use it.

1.  Retrieve the software directly to your desktop by using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

[REDACTED](https://vaww.edis2.med.va.gov/main)

2.  Drag the MAG3_0PXXX_ImporterIII_Setup.exe file from the folder to the desktop, or right- click the file and select Copy, then move the cursor to the desktop, right-click again and select Paste.
3.  Double-click the MAG3_0PXXX_ImporterIII_Setup icon on the desktop.
4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/006.png)At the Welcome to the InstallShield Wizard for VistA Imaging DICOM Importer screen, click Next.

> The installation begins.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/007.png)

5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/008.png)At the InstallShield Wizard Completed screen, click Finish.

> The Importer III client and DICOM Viewer are installed.

## Configuring the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Configuring the Lockout Time

> The DICOM III Importer application will automatically lock and display the log-in screen when the application has been idle for 5 minutes. You may customize the lock-out time. Complete these steps:

1.  In Windows Explorer, go to C:\Program Files\VistA\Imaging\Importer (for Windows 7 users go to C:\Program Files(x86)\VistA\Imaging\Importer).
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/009.png)Right-click the ImagingShell.exe.config file.
3.  Click Open With.
4.  In the Open With window, select Notepad and click OK to edit the file.
5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/010.png)Scroll to the UserIdle Timeout value entry.
6.  Enter the desired value in seconds between the quote marks after value= in the UserIdleLogout value line.
7.  Save the file.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/011.png)Note: Importer III delivers a time-out warning to users before it closes the application. Click the OK button to continue working.

![](vista-imaging-system-dicom-importer-iii-user-manual/012.png)

#### Configuring the Maximum Number of Items to Return

> The DICOM III Importer application will automatically attempt to retrieve all available work items. When a significant large number of work items exist, it is possible to cause network connection timeouts. This connection timeout induces an error and no work items appear in the worklist. You may customize the number of work items return to avoid this connection timeout. Complete these steps:

1.  In Windows Explorer, go to C:\Program Files\VistA\Imaging\Importer. (For Windows 7 users, go to C:\Program Files(x86)\VistA\Imaging\Importer.)
2.  Right-click the ImagingShell.exe.config file.

> Figure 9: Program Files Screen’s File Path

3.  Select Open With.
4.  In the Open With window, select Notepad and click OK to edit the file.
5.  Scroll to the UserIdleTimeout value entry.

![](vista-imaging-system-dicom-importer-iii-user-manual/013.png)

6.  Add the new MaximumNumberOfItemsToReturn line under the UserIdleLogout line. The value “300” is arbitrary. Change the value that best supports the site.
7.  Save the file.

## Verifying the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To verify that the installation and configuration was successful, start the Importer III client using the steps in the following section, [*Starting the Importer III Client*](#starting-the-importer-iii-client). If you are able to get to the DICOM Importer Home screen, the installation and configuration were successful.

## Starting the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Start \| All Programs \| VistA Imaging Program \| Importer to start the Importer III client.
2.  If more than one station number was configured at installation, then the “Connect To” dialog box displays. If the dialog displays, select the desired station from the dropdown and click OK. Otherwise, go to the next step.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/014.png)Figure 11: Multiple Station Configuration Connect To Dialog Box

3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/015.png)Make sure you have a valid PIV card attached to the computer. You will be prompted to select a certificate: Then click on the OK button.
4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/016.png)Next, you will be prompted to enter your PIN. Enter your PIN and click on the OK button.
5.  Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate two-factor authentication (2FA), the application will revert the user to the Access/Verify screen. If the VistA Sign-on box displays, type your access and verify codes in the Access Code and Verify Code boxes, then click OK.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/017.png)Figure 14: VistA Sign-on Dialog Box for the DICOM III Importer

> Note: DICOM Importer III will automatically lock and display the log-in screen after 5 minutes of inactivity on the application. For instructions on how to configure the lockout time, see [Configuring the Lockout Time](#configuring-the-lockout-time) on page [12.](#configuring-the-lockout-time)

6.  ![](vista-imaging-system-dicom-importer-iii-user-manual/018.png)The system displays the DICOM Importer Home screen, as shown below. The application enables buttons based on the security keys assigned to the logged-in user.

## Stopping the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  At the Importer window, go to the File menu and do one of the following:
    - Select Exit to close the Importer III client.
    - Select Log Out to log out and return to the log-in dialog box.

> Note: In either case, if you are currently in the middle of the reconciliation workflow, you are asked if you want to abandon your current work before the exit or logout continues.

![](vista-imaging-system-dicom-importer-iii-user-manual/019.png)

# Chapter 3: Staging the Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are three ways in which DICOM objects are staged and made available in the DICOM Import List: intake staging, DICOM Correct, and network import.

## Intake Staging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Importer III users utilize intake staging when patients deliver external media so that the VA may import the studies into VistA Imaging.

> Note: The media readers on the user’s computer must be unlocked before staging data. Contact VA IT group permissions for help.

> If the media is DICOM-compliant, the Importer III client allows the user to stage the data to the Staging network share. If the media is not DICOM-compliant, the Importer III client attempts to determine the issue and resolve the issue.

> Note: DICOM Importer III displays a warning message for each issue with non-compliant media.

## DICOM Correct

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client includes a centralized work queue for studies requiring corrections (DICOM Correct). Specifically, the Importer III client enables authorized users to centrally manage and correct studies performed at the facility, but rejected by image processing for various reasons. The ability to correct images from a single workstation significantly improves workflow and simplifies the effort of correcting studies performed by the facility. The PACS administrator at a site can view and correct all studies requiring correction in the Importer III client user interface without having to log on to each imaging server. The centralized management also improves server security.

> Users who hold the MAGV IMPORT RECON ARTIFACT security key can use the Importer III client DICOM Correct functionality to fix errors in studies in the DICOM Correct queue.

> Note: Resolving items in the DICOM Correct queue follows the same workflow as reconciling staged studies. Step-by-step instructions for reconciling a staged study needing DICOM Correct can be found in the section [*Entering the Reconciliation Workflow Through Staged Media*](#_bookmark48) located in [Chapter 4: Working with Studies and Orders (Reconciling)](#chapter-4-working-with-studies-and-orders-reconciling).

## Network Import

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When using network import, studies are transmitted directly from an outside facility to the VA over a network (for example, a DICOM proxy server). For each incoming study, a new Importer III client work item is created, and then the images are automatically staged under that work item. For more information on setting up an import location through the AE Security Matrix, see the *DICOM Gateway Planning and Installation Instructions*.

## Non-Compliant Media

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are examples of non-compliant media and how Importer III attempts to deal with them:

- Media contains no DICOMDIR file or contains an invalid DICOMDIR file

> The Importer III client reads all the DICOM objects on the media and attempts to build a list similar to the DICOMDIR reference file. If successful, the study is staged. If unsuccessful, the media is rejected, and a message displays to the user.

- Media contains a DICOMDIR file, but the number of images on the media does not match the DICOMDIR record.

> A warning displays and the user may choose to cancel or continue.

- Media contains DICOM objects, but one or more of them are in a format not currently supported by VistA.

> – If at least one DICOM object on the media is supported, a warning displays indicating the number of unsupported images that will not be imported, and the user can continue or cancel. The SOP class UIDs of the unsupported objects are written to the log file for later reference by technical support.

- If none of the DICOM objects on the media are currently supported by VistA, the user is notified that import is not possible.
- Media does not contain any DICOM objects, Media is rejected, and staging is not possible.
- Media presented is a medical CD/DVD in a vendor proprietary format. Media is rejected, and staging is not possible.
- Media presented is a medical CD/DVD in an encrypted format,

> If the password is unavailable, then the media is rejected, and staging is not possible.

## User Roles for Staging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Staging is primarily the task of the BMSU or the AMSU.

> In addition, instructions are provided for advanced staging of patient data and for optionally viewing the DICOM header and group information (see the section *[Optionally Viewing the](#optionally-viewing-the-dicom-header-and-group-information)* [*DICOM Header and Group Information*](#optionally-viewing-the-dicom-header-and-group-information) in Chapter 6 for more information).

## Staging Media when a Patient Record Exists in VistA Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedure describes how to stage media when a patient record exists on the local VistA database.

> Role: The BMSU’s task is to download all the supported DICOM and non-DICOM files on the external media to a designated Staging storage location.

> Note: Because most patients already have their medical records in the system, the assumption is that patient data at intake is known.

1.  When receiving media from a patient at intake, go to a designated machine to download from the external media.
2.  Start the Importer III client. (See [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
3.  At the DICOM Importer Home screen, under Stage Media for Future Import, click Stage Media to copy the media to your Staging storage location for import processing.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/020.png)Note: The application enables buttons based on the security keys assigned to the logged-in user.

4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/021.png)At the Staging Media Category screen, select the type of media to be staged. The selections are DICOM Only Media, Mixed Media, and Non-DICOM Only Media.
5.  When you select the type of media to stage, the Importer III client lists the conditions under which the media will be staged. In the following screen, Importer III lists the media category details for import of Non-DICOM Only Media.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/022.png)

6.  Click Stage Media.
7.  DICOM Importer III provides a separate workflow for each of the three Media Category options.

> Note: For each workflow, DICOM Importer III selects the Patient is Known radio button by default.

- For the DICOM Only Media option, select the DICOM Media Details from the Drive

drop-down menu and the Media Origin drop-down menu. Then, click Select Patient

> to open the Patient Lookup dialog, search for and select the appropriate patient, and click OK.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/023.png)DICOM Importer III prompts you with messages from the Stage Media Import screen:

- For the Mixed Media option, select the DICOM Media Details from the Drive drop- down menu and the Media Origin drop-down menu. Then, click Select Patient to open the Patient Lookup dialog, search for and select the appropriate patient, and click OK. Finally, click Add to browse the local hard drive of your computer to locate the file containing the non-DICOM media you want to import.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/024.png)

- For the Non-DICOM Only media option, select click Select Patient to open the Patient Lookup dialog, search for and select the appropriate patient, and click OK.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/025.png)Finally, click Add to browse the local hard drive of your computer to locate the file containing the non-DICOM media you want to import.

8.  In the Staging Complete dialog box, click OK to confirm that staging completed successfully.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/026.png)Figure 23: Staging Complete Dialog Box

9.  Remove the media from the drive.
10. Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

## Staging Media When a Patient Record Does Not Exist in VistA Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedure shows how to stage media when a patient record does not exist in the VistA database.

> Role: The BMSU’s task is to download all the files on the media to a designated permanent storage location.

1.  When receiving media from a patient at intake, go to a designated machine to download from the external media.
2.  Start the Importer III client. (See [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
3.  At the DICOM Importer Home screen, under Stage Media for Future Import, click Stage Media to copy the media to your Staging storage location for import processing

> ![](vista-imaging-system-dicom-importer-iii-user-manual/027.png)The application enables buttons based on the security keys assigned to the logged-in user.

4.  At the Staging Media Category Screen, select the type of media to be staged. The choices are DICOM Only Media, Mixed Media, and Non-DICOM Only Media. When you make the selection, the Stage Media button is enabled.
5.  Select Stage Media.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/028.png)

6.  Importer III opens the Stage Media for Import screen. Under Patient, select Patient is unknown.
7.  ![](vista-imaging-system-dicom-importer-iii-user-manual/029.png)Under Media Details, select the drive letter for staging media from the Drive drop-down list, select the media origin from the Media Origin drop-down list, and click Stage for Import.

> Note: Selecting from the Media Origin drop-down box is optional during media staging; however, it is required during the reconciliation process. Selecting a value for the media origin during staging allows this information to be pre-populated during the reconciliation process performed by the ARA.

8.  ![](vista-imaging-system-dicom-importer-iii-user-manual/030.png)In the Staging Complete dialog box, click OK to confirm that you have seen the message that staging has completed successfully.
9.  Remove the media from the drive.
10. Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

## Advanced Staging of Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The advanced staging features of DICOM Importer III enable users with the appropriate permissions to choose selected studies from media and stage these studies for the use of clinicians.

> The following procedure shows how to perform advanced staging of media tasks.

> Role: The AMSU can perform the same tasks as the BMSU. In addition, the AMSU’s task is to check the media and download the studies needed for the clinician.

#### Advanced Data Staging Overview

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/031.png)At the DICOM Importer Home screen, under Stage Media for Future Import, click Stage Media to copy the media to your Staging storage location for import processing. Buttons are enabled or disabled based on the security keys assigned to the logged-in user.
3.  At the Staging Media Category screen, select the type of media that will be staged. The selections are DICOM Only Media, Mixed Media, and Non-DICOM Only Media.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/032.png)

4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/033.png)When you select the type of media to stage, the Importer III client lists the conditions under which the media will be staged. In the following screen, Importer III lists the media category details for import of Non-DICOM Only Media.
5.  Click Stage Media.
6.  Remove the media from the drive.
7.  Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

> DICOM Importer III provides a separate workflow for each of the three Media Category options. The workflow is detailed in the following sections.

#### Staging DICOM Only Media

1.  ![](vista-imaging-system-dicom-importer-iii-user-manual/034.png)On the Staging Media Category screen, select the DICOM Only Media radio button. Click the Stage Media tab.

> Importer III opens the Stage Media for Import screen. In the DICOM Media Details section, select the drive from which you want to stage the media from the Drive drop- down menu and the origin of the media from the Media Origin drop-down menu.

![](vista-imaging-system-dicom-importer-iii-user-manual/035.png)

2.  DICOM Importer III selects the Patient is known radio button by default.
3.  Select click Select Patient to open the Patient Lookup dialog, search for and select the appropriate patient, and click OK.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/036.png)

> Note: To select another patient, click Change Patient.

![](vista-imaging-system-dicom-importer-iii-user-manual/037.png)

4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/038.png)At the Stage Media for Import screen, click Enable Advanced Options. DICOM Importer III displays a list of the DICOM media on the drive you have selected.
5.  Click on a row to select the studies to stage. Each study contains a row with Patient ID, Patient Name, Date of Birth, Sex, Accession \#, Study Date, Description, and Images.
6.  Click the Stage for Import button.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/039.png)Note: If DICOM Importer cannot locate DICOM media on the drive you have selected, the application will display the following error message:

7.  Remove the media from the drive.
8.  Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

#### Staging Mixed Media

1.  On the Staging Media Category screen, select the Mixed Media radio button. Click the

> ![](vista-imaging-system-dicom-importer-iii-user-manual/040.png)Stage Media tab.

2.  Select the DICOM Media Details from the Drive drop-down menu and the Media Origin drop-down menu. Then, click Select Patient to open the Patient Lookup dialog, search for and select the appropriate patient, and click OK. Finally, in the Non-DICOM Media section, click Add to browse the local hard drive of your computer to locate the file containing the non-DICOM media you want to stage for import.

![](vista-imaging-system-dicom-importer-iii-user-manual/041.png)

3.  When you have located the file you want to import, click the Add button again.
4.  Repeat steps 2 and 3 until you have located all the non-DICOM files you want to stage for import.
5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/042.png)Click Enable Advanced Options. DICOM Importer III displays a list of the DICOM media on the drive you have selected.
6.  Click on a row to select the studies to stage. Each study contains a row with Patient ID, Patient Name, Date of Birth, Sex, Accession \#, Study Date, Description, and Images.
7.  Click the Stage for Import button.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/043.png)Note: If DICOM Importer cannot locate DICOM media on the drive you have selected, the application will display the following error message:

8.  Remove the media from the drive.
9.  Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

#### Staging Non-DICOM Media Only

1.  ![](vista-imaging-system-dicom-importer-iii-user-manual/044.png)On the Staging Media Category screen, select the Non-DICOM Only Media radio button. Click the Stage Media tab.
2.  Importer III opens the Stage Media for Import screen. A VA patient is required to import non-DICOM media only. Click Select Patient, move to the Patient Lookup screen, select the correct patient and click OK to return to the Stage Media for Import screen.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/045.png)

3.  Click Add to browse the local hard drive of your computer to locate the file containing the non-DICOM media you want to import. When you add the first file, the Stage for Import button is enabled. Repeat until you have located all the non-DICOM media you want to import to the patient record.
4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/046.png)Click Stage for Import (now enabled). Importer III returns the staging complete message.
5.  Remove the media from the drive.
6.  Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

# Chapter 4: Working with Studies and Orders (Reconciling)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Direct Import of Electronic Media

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Media can be sent to DICOM Importer III electronically. In such a case, a CSRA or an ARA can bypass the step-in staging and perform a direct import of the media by accessing it in a designated queue. In this way, files can be automatically loaded to a designated location (staging share) so that studies can be reconciled with orders as part of the Importer III client reconciliation process.

## Import Reconciliation Workflow Industry Standard for DICOM Import

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Integrating the Healthcare Enterprise (IHE) Import Reconciliation Workflow (IRWF) integration profile specifies the industry-standard technique for importing DICOM objects.<sup>1</sup> With the IRWF, patient and study identification information is obtained from a study on the local system. This information is then used to replace the values of the corresponding data elements in the DICOM objects that will be imported. To provide an audit trail, the original DICOM values, along with the import application attributes, are saved elsewhere in the DICOM header (see the section [*Optionally Viewing the DICOM Header and Group Information*](#optionally-viewing-the-dicom-header-and-group-information) in Chapter 6 for more information). DICOM objects from the outside study, now containing the local patient and study identification, are then imported and associated with the study on the local system.

#### Importing Ordered Studies Using IRWF

> When importing ordered studies using IRWF, both the patient and the study are already registered on the local system. The patient and study identification information, from each local study, is used to update the DICOM objects from the original outside study. Importation then takes place and the DICOM objects from each outside study are associated with the corresponding ordered study on the local system.

> <sup>1</sup> IHE Import Reconciliation Workflow, IHE Technical Framework, vol. I, Rev. 8.0, 2007- 08-30.

#### Importing Unordered Studies Using IRWF

> When importing unordered studies using IRWF, first make sure that the patient is registered in the local system. Then create a corresponding equivalent study in the local system for every unordered outside study to be imported. The patient and study identification information, for each newly created local study, is used to update the DICOM objects from the original outside study. The studies are imported, and the DICOM objects from each outside study are associated with their corresponding newly created studies on the local system.

> The Importer III client can handle both ordered and unordered studies.

- Ordered studies are those that already have corresponding orders on the local VistA system. There are three types of ordered studies.
  - Prior exam or historical study (physician performed a study on the patient)
  - Contracted study with the order already there (physician places an order with an outside contractor to perform a study on the patient who is at a remote site)
- DICOM Correct – A study in the DICOM Correct work queue that has an information mismatch and needs to be corrected
- Unordered studies

> The classic example is the unordered prior study that was performed while the patient was being treated at an outside facility. The patient then brings the media containing the prior study and presents it to the local VA at intake for treatment.

- If CSRAs encounter this situation, then they must work with the ARA or the clinician to resolve the problem.
- If ARAs encounter this problem for a radiology-based study, then the software allows them to place an on-demand radiology order and set the order status.
- If the study is a Consult, then ARAs navigate to the CPRS subsystem and place the order. When they return to the Importer III client and refresh the screen, the order is then listed.

## Reconciling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The original patient/study information and the VA hospital information must be reconciled. For example, the Patient’s ID may be different from the Patient ID assigned by the location where the study was completed. In addition, the VA has an accession number associated with the patient that is different from the accession number used when the imaging facility performed the study. These two sets of data must be reconciled to match the patient’s data on the media with the correct patient/study in VistA.

## User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ARA has all rights including staging media, placing on-demand radiology orders, and reconciling orders and staged studies. An ARA also has rights to correct studies that are in the DICOM Correct queue.

> The CSRA has the rights to stage media and reconcile studies with pending orders, and to perform a direct import.

> Important: Only an ARA can create radiology orders, generate reports, and review reports.<span id="_bookmark48" class="anchor"></span> Entering the Reconciliation Workflow Through Staged Media Role: As the ARA or the CSRA, you choose to reconcile and import previously staged studies.

> The first way to enter the reconciliation workflow is by selecting previously staged media. Media is staged through one of the following processes.

- You or another user staged media using the Importer III client, through one of the Media Staging scenarios described in [*Chapter 3: Staging the Data*](#chapter-3-staging-the-data).
- An HDIG staged the media through a Network Import.
- An HDIG staged the media because a DICOM Correct was necessary.

> Regardless of how the media has been staged, the method for entering the reconciliation workflow is as follows.

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/047.png)At the DICOM Importer Home screen, under View Import List, click Import List.
3.  The DICOM Import List screen displays. The list contains a set of optional filters that you can use to narrow down the results displayed in the list.
    - ![](vista-imaging-system-dicom-importer-iii-user-manual/048.png)The Item Type drop-down filter lets you narrow down the results by staging method: All Types, Direct Import, Staged Media, Network Import, DICOM Correct.
    - The Source drop-down filter lets you narrow down the list by the source of the work item: a particular client machine, a particular HDIG, and so on.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/049.png)

- The Patient Name filter lets you narrow down the list by patient name.
- The two radio buttons also function as filters. You may choose to select Show New Work Items or Show Processed Work Items with Remaining Studies.

> Note: If you logged in as a CSRA, you will see only work items in the list that were staged as FEE origin, or that came in through a network import as FEE origin. Items that were staged with no origin specified, or with a different origin than FEE, will not be available for you to reconcile. They must be reconciled by an ARA.

![](vista-imaging-system-dicom-importer-iii-user-manual/050.png)

4.  Once you have identified the Importer item of interest, select it from the list, and then click

> Process Import Item (now enabled).

5.  The Importer III client displays the Study List screen, containing all the studies on the selected media. At this point, you have entered the reconciliation workflow. Refer to one of the two Reconciliation scenarios ([*Reconciling Studies with Existing Orders*](#reconciling-studies-with-existing-orders) or [*ReconcilingStudies Requiring New Radiology Orders*](#reconciling-studies-requiring-new-radiology-orders)) for further instructions.

## Entering the Reconciliation Workflow Through Direct Import

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The previous section discussed entering the reconciliation workflow by choosing a staged media Importer item. However, you can directly enter the workflow without prior staging if you have a CD or DVD containing the data, or a folder on a local drive containing studies you wish to import. This is called a Direct Import.

> Role: As the ARA or the CSRA, your task involves importing directly from physical media (CD, DVD, local folder on a hard drive, and so on) without performing the staging step first.

1.  Start the Importer III client. (See the section, [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/051.png)At the DICOM Importer Home screen, under DICOM Direct Import, click Direct Import.
3.  At the DICOM Direct Import screen, choose the category of media that you want to import.
    - Select the DICOM Only Media radio button for DICOM only media. DICOM Importer III returns the message: *Only DICOM files will be allowed to be imported* and enables the Direct Media Import button.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/052.png)

- ![](vista-imaging-system-dicom-importer-iii-user-manual/053.png)Select the Mixed Media radio button for DICOM and non-DICOM media from the same source. DICOM Importer III returns the message: *Each non-DICOM file selected must belong with a study in the same media bundle; at least one valid DICOM and non-DICOM file must be selected in order to import* and enables the Direct Media Import button.
- Select the Non-DICOM Only Media radio button for non-DICOM media, such as

> .pdf files. DICOM Importer III returns the message: *Only non-DICOM files will be allowed to be imported; all Non-DICOM files selected must be for the same patient and order*, and enables the Direct Media Import button.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/054.png)

4.  Complete the workflow for the media category selection you have made in step 3 as follows:
    - For DICOM Only files, select Direct Import Media. On the Media Direct Import screen, select the drive or the folder from which you are importing the files. Select Reconcile Media. The Study List screen opens. Select and optionally view at least one study on the study list. Click Reconcile Study. The Patient Selection screen opens. Search for and select a patient. The Study Origin and Target Order page opens. Select the study origin. Select to use an existing order or create a new radiology order. Follow the appropriate workflow for the order choice. At the Reconciliation Summary Screen, review the details of the reconciliation. Return to the Study List screen and complete reconciliation
    - For Mixed Media, select Direct Import Media. On the Media Direct Import screen, select the drive or the folder from which you are importing the files. Under Non- DICOM Media, select Add, and browse to the non-DICOM file you want to reconcile with the exam. Repeat until all the non-DICOM files you require have been added. Select Reconcile Media. The Study List screen opens. Select and optionally view at least one study on the study list. Click Reconcile Study. The Patient Selection screen opens. Search for and select a patient. The Study Origin and Target Order page opens. Select the study origin. Select to use an existing order or create a new radiology order. Follow the appropriate workflow for the order choice. At the Reconciliation Summary Screen, review the details of the reconciliation. Return to the Study List screen and complete the reconciliation.
    - For non-DICOM only files, select Direct Import Media. Under Non-DICOM Media, select Add, and browse to the non-DICOM file you want to reconcile with the exam. Repeat until all the non-DICOM files you require have been added. On the Non- DICOM File Reconciliation screen, select Select Patient to search for and select a patient. Click Next. The Study Origin and Target Order page opens. Select the study origin. Select to use an existing order or create a new radiology order. Follow the appropriate workflow for the order choice. At the Import Confirmation screen, review the details of the reconciliation. Select Import.

> Note: Refer to one of the two reconciliation scenarios ([*Reconciling Studies with Existing Orders*](#reconciling-studies-with-existing-orders)

> or [*Reconciling Studies Requiring New Radiology* Orders](#reconciling-studies-requiring-new-radiology-orders)) for further instructions.

## Reconciling Studies with Existing Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedure shows how to reconcile studies with pending orders. The reconciliation workflow is the same for both staged media and direct imports.

> Role: As the ARA or the CSRA, your task begins after selecting a staged Importer item, or through direct import of media, and involves reconciling studies with pending orders.

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)), or by initiating a Direct Import (see [*Entering theReconciliation Workflow Through Direct Import*](#entering-the-reconciliation-workflow-through-direct-import)).
3.  Under Study List, select the appropriate study. Optionally, click View Study to verify that you selected the correct study (see [*Chapter 6: Viewing Study Data and Images*](#chapter-6-viewing-study-data-and-images) for details). Once you are satisfied that you have selected the correct study, click Reconcile Study.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Study List Status Indicator Definitions</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Letter Indicator (color)</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Definition</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C (red)</p>
</blockquote></td>
<td><blockquote>
<p>Study is reconciled and all images are processed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P (yellow)</p>
</blockquote></td>
<td><blockquote>
<p>Study is reconciled and some images are processed, but not all images</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>I (green)</p>
</blockquote></td>
<td><blockquote>
<p>Study is reconciled and images are waiting for processing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D (pink)</p>
</blockquote></td>
<td><blockquote>
<p>Study is marked for deletion</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: An order with a status of complete (*C*) cannot have images added to it. An Administrative override must be performed to change the status of the order. The exception is Radiology exams that have a credit method of “NO CREDIT.”

> Important: DICOM Correct studies should be processed before they are reported as completed (*C*).

> ![](vista-imaging-system-dicom-importer-iii-user-manual/055.png)![](vista-imaging-system-dicom-importer-iii-user-manual/056.png)

4.  The first step in the reconciliation process is the Patient Selection screen. The DICOM Patient Information section displays patient demographic information as found in the DICOM header. The VA Patient information section may or may not be populated for you already, as described in the following three scenarios:
    - If a patient is selected during staging, then the VA Patient Information section is pre- populated with that patient’s information. Verify that the patient is correct. If the patient is incorrect, click Change Patient to go to the patient search function and change the selection.

![](vista-imaging-system-dicom-importer-iii-user-manual/057.png)![](vista-imaging-system-dicom-importer-iii-user-manual/058.png)

- If you have already reconciled a different study in the same Importer session, and the patient demographics in the DICOM header for the current study identically match the demographic information in the DICOM header for a previously reconciled study, the Importer III client pre-populates the patient information for you, saving you the time of searching again. If the patient is incorrect, click Change Patient to change the selection.
- If neither of the above scenarios is applicable, the Importer III client does not pre- populate a patient for you. You are required to search for and select the appropriate patient before the system allows you to continue.
5.  Once the patient is searched for (or verified if pre-populated), click Next.
6.  If you are logged in as an ARA, the next step is to choose the study origin and target order. If you are logged in as a CSRA, you will not see this step and are instead taken directly to the Choose Existing Order screen, since the study origin is already set to FEE, and you do not have the option to create a new radiology order.
7.  Since in this scenario the order already exists, select Use an Existing Order for target order.
8.  Click Next.

![](vista-imaging-system-dicom-importer-iii-user-manual/059.png)

9.  ![](vista-imaging-system-dicom-importer-iii-user-manual/060.png)At the Choose Existing Order screen, select the appropriate existing order. The list displays both RAD (radiology orders) and CON (consults orders).
10. If a radiology order is chosen, the exam status is updated to EXAMINED by default. This is to allow local workflow to be followed to close out the exam. If you know that the exam should be completed as-is (no additional images need to be added, no diagnostic codes need to be entered, and so on), then you may choose to advance the status to COMPLETE from here by selecting the Set the exam to COMPLETE after import checkbox. This option is not available for consults, only radiology orders.

> Note: At this point in the reconciliation process, you may add one or more non-DICOM files to the record of the patient whose studies you are reconciling. Follow these steps:

- ![](vista-imaging-system-dicom-importer-iii-user-manual/061.png)![](vista-imaging-system-dicom-importer-iii-user-manual/062.png)Click Next. DICOM Importer III opens the Add Non-DICOM Files screen.
- Click Add. Browse to and select the correct file on your computer’s hard drive. Repeat this process until you have selected all desired files.
11. ![](vista-imaging-system-dicom-importer-iii-user-manual/063.png)![](vista-imaging-system-dicom-importer-iii-user-manual/064.png)Click Next. DICOM Importer III opens the Reconciliation Summary screen.
12. At the Reconciliation Summary screen, verify that the study matches the order and then click

#### Return to Study List.

> Note: Non-DICOM files you may have added to the patient record are not listed on the Reconciliation Summary screen.

13. At the Study List screen, note the status indicators added in the Status column of the study. If there are other studies on the media you wish to import, you can continue reconciling them. When all studies of interest are reconciled, click Submit Import Request.
14. ![](vista-imaging-system-dicom-importer-iii-user-manual/065.png)At the Import Confirmation screen, verify that the studies you wish to import are displayed, and verify that the reconciliation is correct. If it is not, you click Return to Study List to update the reconciliations. If you are satisfied with the reconciliations, click Import.
15. In the Queued for Import dialog box, click OK to confirm that the work item is queued for import processing.

![](vista-imaging-system-dicom-importer-iii-user-manual/066.png)

16. The system returns you to either the Direct Import home screen or the DICOM Import List, depending on how you originally entered the reconciliation workflow. From here, you can continue to work on other Importer scenarios, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

## Reconciling Studies Requiring New Radiology Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedure shows how to reconcile studies requiring new orders.

> Role: As the ARA, your task begins after selecting a staged Importer item, or through direct import of media, and involves creating a new radiology order during reconciliation. This scenario is not available to the CSRA.

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)), or by initiating a Direct Import (see [*Entering theReconciliation Workflow Through Direct Import*](#entering-the-reconciliation-workflow-through-direct-import)).
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/067.png)![](vista-imaging-system-dicom-importer-iii-user-manual/068.png)At the Study List screen, select the appropriate study. Optionally, click View Study to verify that you selected the correct study (see [*Chapter 6: Viewing Study Data and Images*](#chapter-6-viewing-study-data-and-images) for details). Once you are satisfied that you have selected the correct study, click Reconcile Study. Note: This step is not required if you are reconciling non-DICOM only media.
4.  The first step in the reconciliation process is the Patient Selection screen. The DICOM patient information section displays patient demographic information as found in the DICOM header. The VA Patient information section may or may not be populated for you already, as described in the following three scenarios:
    - ![](vista-imaging-system-dicom-importer-iii-user-manual/069.png)![](vista-imaging-system-dicom-importer-iii-user-manual/070.png)If the user selects a patient during staging, the VA Patient Information section is pre- populated with that patient’s information. Verify that the patient is correct. If the patient is incorrect, click Change Patient to change the patient.
    - If you have already reconciled a different study in the same Importer session, and the patient demographics in the DICOM header for the current study identically match the demographic information in the DICOM header for a previously reconciled study, the Importer III client pre-populates the patient information for you, saving you the time of searching again. If the patient is incorrect, click Change Patient to change the patient.
    - ![](vista-imaging-system-dicom-importer-iii-user-manual/071.png)If neither of the above scenarios is applicable, the Importer III client does not pre- populate patient information for you. You are required to search for and select the appropriate patient before the system allows you to continue.
5.  Once the patient is searched for (or verified if pre-populated), click Next.

> If you logged in as an ARA, the next step is to choose the study origin and target order. If you logged in as a CSRA, you do not see this step. Instead, the system takes you directly to the Choose Existing Order screen, since the study origin is already set to FEE, and you do not have the option to create a new radiology order.

6.  ![](vista-imaging-system-dicom-importer-iii-user-manual/072.png)To create a new radiology order, select Create Radiology Order under Target Order.
7.  Select the study origin from the Study Origin drop-down menu. Add the study date at the bottom of the screen if needed. The Next button is enabled.
8.  ![](vista-imaging-system-dicom-importer-iii-user-manual/073.png)Click Next. DICOM Importer III opens the Create New Radiology Order screen.

> The Create New Radiology Order screen consists of four groups of information.

- Under VA Patient Information, there is identifying information for the patient selected in the previous step, as found in the VA patient record.
- Under Original Study Information, there is study information retrieved from the DICOM metadata for the selected study.
- Under VA Order Details, there are data entry fields.
- Under Status Change Details, there is information regarding the exam status, standard reports associated with the exam, and diagnostic codes associated with the exam.
9.  Perform the following steps under VA Order Details.
    - Select the appropriate Ordering Provider.
    - Select the appropriate Ordering Location.
    - Select the appropriate Procedure.
    - Optionally, select any applicable Procedure Modifiers.
10. Review the Status Change Details section. To change the entries, click Change Details, and complete the steps detailed in the section titled [*Adding and Changing Exam Details DuringReconciliation of a New Radiology Order*](#adding-and-changing-exam-details-during-reconciliation-of-a-new-radiology-order)*.*
11. Click Next. DICOM Importer III opens the Add Non-DICOM Files screen. Use this screen to add non-DICOM files to the patient record for this exam. When you have finished entering non-DICOM files, click Next.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/074.png)

12. DICOM Importer III opens the Reconciliation Summary screen.
13. At the Reconciliation Summary screen, verify that the study matches the order and then click

#### ![](vista-imaging-system-dicom-importer-iii-user-manual/075.png)![](vista-imaging-system-dicom-importer-iii-user-manual/076.png)Return to Study List.

14. ![](vista-imaging-system-dicom-importer-iii-user-manual/077.png)![](vista-imaging-system-dicom-importer-iii-user-manual/078.png)At the Study List screen, note the marker added in the Status column of the study. If there are other studies on the media you wish to import, you can continue reconciling them. When all studies of interest have been reconciled, click Submit Import Request.
15. At the Import Confirmation screen, verify that the study or studies you wish to import are displayed, and verify that the reconciliation looks correct. If it does not, you may return to

> the study list to update the reconciliations. If you are satisfied with the reconciliations, click

#### ![](vista-imaging-system-dicom-importer-iii-user-manual/079.png)![](vista-imaging-system-dicom-importer-iii-user-manual/080.png)Import.

16. ![](vista-imaging-system-dicom-importer-iii-user-manual/081.png)![](vista-imaging-system-dicom-importer-iii-user-manual/082.png)In the Queued for Import dialog box, click OK indicating that the work item is queued for import processing.
17. The system returns you to either the Direct Import screen or the DICOM Import List screen, depending on how you originally entered the reconciliation workflow. From here, you can continue to work on other Importer scenarios, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

## Adding and Changing Exam Details During Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As part of the reconciliation process, DICOM Importer III enables users to change the status of exams, the diagnostic codes associated with exams, and the standard reports ordered to accompany the exams.

> Role: As the ARA or the CSRA, you change the details of an exam during the process of reconciling studies with patients.

> Note: The workflow required to change study details is different for existing orders and for new radiology orders created during the reconciliation process. See the sections titled [Adding and](#adding-and-changing-exam-details-during-reconciliation-of-an-existing-order) [Changing Exam Details During Reconciliation of An Existing Order](#adding-and-changing-exam-details-during-reconciliation-of-an-existing-order) and [Adding and Changing](#adding-and-changing-exam-details-during-reconciliation-of-a-new-radiology-order) [Exam Details During Reconciliation of a New Radiology Order](#adding-and-changing-exam-details-during-reconciliation-of-a-new-radiology-order) for details.

#### Adding and Changing Exam Details During Reconciliation of An Existing Order

> To add or change exam details for an existing order during the reconciliation process:

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/083.png)Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)), or by initiating a Direct Import (see [*Entering theReconciliation Workflow Through Direct Import*](#entering-the-reconciliation-workflow-through-direct-import)). Click Reconcile Study.
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/084.png)DICOM Importer III opens the Patient Selection screen. Confirm the patient selection and click Next, or click Change Patient to go to the Patient Lookup screen and select another patient. Then, click Next.
4.  DICOM Importer III opens Study Origin and Target Order screen.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/085.png)

5.  Select the origin of the study from the Study Origin drop-down menu.
6.  Select the Use an Existing Order radio button.
7.  Select an Imaging Location from the list at the bottom of the screen.
8.  If required, add the study date in YYYYMMDD format.
9.  Click Next.
10. DICOM Importer III opens the Choose Existing Order screen. From the Existing Orders list, select the order you wish to reconcile.

![](vista-imaging-system-dicom-importer-iii-user-manual/086.png)

11. Click Change Details. DICOM Importer III opens the Status Change Details pop-up box.

![](vista-imaging-system-dicom-importer-iii-user-manual/087.png)

12. In the Status Change Details pop-up box, select the primary diagnostic code from the drop- down menu, and select one or more secondary diagnostic codes from the drop-down menu. An unlimited number of secondary diagnostic codes are allowed.

> Note: Select Complete in the Exam Status drop-down menu. This enables selection of the diagnostic codes and the standard report you want to associate with the exam.

13. Select the standard report to be associated with the exam from the Standard Report drop- down menu. Review the Standard Report Impression (summary) and Standard Report Text (full text) to ensure you have selected the desired report.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/088.png)Note: If the Exam Status drop-down is set to Examined, you will receive a warning message to change the exam status to Complete before you can change the status details of the exam.

14. Select OK. DICOM Importer II returns to the Choose Existing Order screen. Click Next. At this point, you resume the reconciliation process.

#### Adding and Changing Exam Details During Reconciliation of a New Radiology Order

> To add or change exam details while creating a new radiology order during the reconciliation process, follow these steps:

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/089.png)Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)), or by initiating a Direct Import (see [*Entering theReconciliation Workflow Through Direct Import*](#entering-the-reconciliation-workflow-through-direct-import)). Click Reconcile Study.
3.  DICOM Importer III opens the Patient Selection screen. Confirm the patient selection and click Next, or click Change Patient to go to the Patient Lookup screen and select another patient. Then, click Next.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/090.png)

4.  DICOM Importer III opens Study Origin and Target Order screen. Select the origin of the study from the Study Origin drop-down menu.
5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/091.png)Select the Create Radiology Order radio button.
6.  Select an Imaging Location from the list at the bottom of the screen.
7.  If required, add the study date in YYYYMMDD format.
8.  Click Next.
9.  DICOM Importer III opens the Choose Existing Order screen. From the Existing Orders list, select the order you wish to reconcile.

![](vista-imaging-system-dicom-importer-iii-user-manual/092.png)

10. Click Change Details. DICOM Importer III opens the Status Change Details pop-up box.

![](vista-imaging-system-dicom-importer-iii-user-manual/093.png)

11. In the Status Change Details pop-up box, select the primary diagnostic code from the drop- down menu, and select one or more secondary diagnostic codes from the drop-down menu. An unlimited number of secondary diagnostic codes are allowed.
12. Select the standard report to be associated with the exam from the Standard Report drop- down menu. Review the Standard Report Impression (summary) and Standard Report Text (full text) to ensure you have selected the desired report.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/094.png)Note: If the Exam Status drop-down is set to Examined, you will receive a warning message to change the exam status to Complete before you can change the status details of the exam.

13. Select OK. DICOM Importer II returns to the Choose Existing Order screen. Click Next. At this point, you resume the reconciliation process.

## Reconciling Partially Imported Studies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Occasionally, a piece of media that you are attempting to import contains images for a study in which some of the images on the media already exist in VistA, while others do not. This is termed a *partially imported study*, and the system displays these studies in the study list with a status indicator of *P*.

> Role: As the ARA or the CSRA, your task begins after the media is staged or through direct import of media, and involves adding additional images to a partially imported study.

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)), or by initiating a Direct Import (see [*Entering theReconciliation Workflow Through Direct Import*](#entering-the-reconciliation-workflow-through-direct-import)).
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/095.png)At the Study List screen, select a partially imported study (*P*). The system displays the Study Details panel for the selected study. The Study Information column shows patient and study information obtained from the DICOM header. Since the study is partially imported, the Order Information column is populated with the patient and order data that the existing images were filed under. At this point, you can optionally click View Study, to verify that you selected the desired study (see [*Chapter 6: Viewing Study Data and Images*](#chapter-6-viewing-study-data-and-images) for details). When you are satisfied that you have selected the desired study, click Reconcile Study.
4.  You are alerted that the study is partially imported, and offered a choice:

> *Would you like to import the remaining instances to the same patient and order? Choose ‘Yes’ to import the remaining instances to the same patient and order.*

> *Choose ‘No’ to reconcile the remaining instances to a different patient and/or order.*

- If you choose Yes, then the system creates a complete reconciliation automatically, using the same patient and order that are displayed in the Study Details panel in the previous step, and you are returned immediately to the Study List screen, bypassing the manual reconciliation steps. Even though the reconciliation is created for you automatically, you still have the option to reenter the reconciliation workflow to make changes at any time, by selecting the study and clicking Reconcile Study.
- If you choose No, the system takes you directly to the reconciliation workflow. The patient is preselected for you on the Patient Information screen, but you are free to change it if necessary.
5.  Regardless of whether you chose automatic or manual reconciliation in the previous step, once the reconciliation is complete the system gives the study a new status of *PI*. This indicates that the study is partially imported and that the remaining images are reconciled and ready for import. If there are other studies on the media you wish to import, you can continue reconciling them. When all studies of interest are reconciled, click Submit Import Request.
6.  At the Import Confirmation screen, verify that the study or studies you wish to import are displayed, and verify that the reconciliation looks correct. If it does not, you may return to the study list to update the reconciliations. If you are satisfied with the reconciliations, click Import.
7.  ![](vista-imaging-system-dicom-importer-iii-user-manual/096.png)![](vista-imaging-system-dicom-importer-iii-user-manual/097.png)In the Queued for Import dialog box, click OK to acknowledge that the work item is queued for import processing.
8.  The system returns you to either the Direct Import screen or the DICOM Import List screen, depending on how you originally entered the reconciliation workflow. From here, you can continue to work on other Importer scenarios, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

## Deleting Studies from Staged Media

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A piece of staged media that you are attempting to import will occasionally contain multiple studies. If you know that you do not need one or more of these studies, you can choose to delete them from the staged media bundle. This has the benefit of freeing up space on the imaging share, since Importer items and their extra studies remain on the system for a configurable amount of time after submission and processing.

> Role: As the ARA or the CSRA, your task begins after the media is staged, and involves deleting unneeded studies from a staged media bundle. This workflow does not apply to Direct Import.

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  Go to the Study List by selecting a staged Importer item (see [*Entering the ReconciliationWorkflow Through Staged Media*](#_bookmark48)).
3.  At the Study List screen, select a study that you wish to delete. At this point, you can optionally click View Study, to verify that you selected the desired study (see [*Chapter 6:Viewing Study Data and Images*](#chapter-6-viewing-study-data-and-images) for details).
4.  Once you are satisfied that the desired study is selected, click Delete. (This button is only available for staged media, not direct import). The system gives the study a status of *D*, and updates the text of the Delete button to Don’t Delete. If you decide that you do not actually wish to delete the study, make sure it is selected, and then click Don’t Delete. Otherwise, click Submit Import Request to continue the deletion process.

> Note: The system does not actually delete the media until you submit the Importer item, so you can toggle back and forth as often as you like on this screen.

5.  At the Import Confirmation screen, the system displays the total number of studies that you have marked for deletion, just above the list of reconciliations (if any) that you have completed. Click Import to continue the deletion process.
6.  ![](vista-imaging-system-dicom-importer-iii-user-manual/098.png)![](vista-imaging-system-dicom-importer-iii-user-manual/099.png)In the Queued for Import dialog box, click OK to acknowledge that the work item is queued for import processing.
7.  The system returns you to the Direct Import screen or the DICOM Import List screen, depending on how you originally entered the reconciliation workflow. From here, you can continue to work on other Importer scenarios, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

# Chapter 5: Managing Import Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Managing import queues involves performing periodic maintenance involving the following tasks:

- Reverting work items stuck in reconciliation.
- Viewing the Importer items that are currently being processed by an HDIG.
- Viewing failed Importer items.

> Role: The ARA handles these tasks exclusively.

## Reverting Items Stuck in Reconciliation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a user selects an item from the Import List, and the user’s Importer III client or workstation crashes before the item is cancelled or submitted for processing, the Importer item they were actively working will be stuck in a status of In Reconciliation. When this occurs, the Importer item no longer shows up in the Import List, and is therefore unavailable for subsequent reconciliation attempts.

> The Revert Import Item screen allows an administrator to identify Importer items that are stuck in reconciliation, revert them back to a status of *New*, and delete reconciliations that were partially completed, if any. This process restores the Importer item to a known good state, so that it is available once again for selection in the Import List.

![](vista-imaging-system-dicom-importer-iii-user-manual/100.png)

> Use caution when reverting Importer items. The Revert Items list shows all Importer items that are currently in reconciliation, including items that are not stuck and are actively being worked on. The “stuck” items must be identified, using data such as the last person to modify the item, the timestamp of the modification, or other identifying information. If an item that is currently being worked is inadvertently reverted, then the user gets an error when they attempt to submit the import, and will have to go back to the Import List and repeat the reconciliation process.

> Note: As the ARA, the administrator tasks require the MAGV IMPORT RECON CONTRACT security key.

> To revert items stuck in reconciliation:

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/101.png)At the DICOM Importer Home screen, under Administration, click Administration.
3.  At the DICOM Importer Administration Home screen, under Revert Importer Items, click

#### ![](vista-imaging-system-dicom-importer-iii-user-manual/102.png)Revert Items.

4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/103.png)At the Revert Import Item screen, select the Importer item that is stuck in reconciliation, being especially careful not to select other import items that are not stuck, and click Revert Import Item.
5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/104.png)If the reverted item was the last one in the list, DICOM Importer III displays the message: No Importer items are currently in reconciliation.
6.  At the Revert Import Item screen, click Return to Administration Home.
7.  ![](vista-imaging-system-dicom-importer-iii-user-manual/105.png)At the DICOM Importer Administration Home screen, click Return to Importer Home.
8.  At the DICOM Importer Home screen, under View Import List, click Import List to verify the reverted item is now listed.
9.  Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

## Viewing Importer Items Currently Being Processed by an HDIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client allows users to reconcile DICOM studies with the correct VA patient and order data. However, the work of actually importing the studies into VistA is handled asynchronously by an HDIG.

> Administrators have the ability to view the current work status for each of the HDIGs for the logged in station number.

> To view the work status for the HDIGs:

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/106.png)At the DICOM Importer Home screen, under Administration, click Administration.
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/107.png)At the DICOM Importer Administration Home screen, under In-Process Imports, click In- Process Imports.
4.  At the In-Process Importer Items screen, the system displays a list of items (if any) that the HDIGs are currently processing for the logged in station number. The list shows high-level details, including the IEN of the Importer item, the type, when the item was submitted, who submitted the item, and which HDIG is currently processing the item.
5.  The list does not refresh automatically, but you can click Refresh In-Process Import List at any time to refresh the list manually. When you are finished working with in-process Importer items, you can continue working on other Importer use cases, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

![](vista-imaging-system-dicom-importer-iii-user-manual/108.png)

## Viewing Failed Importer Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client allows users to reconcile DICOM studies with the correct VA patient and order data. However, the work of actually importing the studies into VistA is handled asynchronously by an HDIG. Because the import process is asynchronous, errors during import cannot be displayed in real time when the user submits the studies for processing. Instead, the Importer III client supplies functionality to view failed import items after the processing is complete.

> To see a list of failed work items for the logged in station number, and view details related to each of the failures:

1.  Start the Importer III client. (See the section [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/109.png)At the DICOM Importer Home screen, under Administration, click Administration.
3.  At the DICOM Importer Administration Home screen, under View Failed Imports, click

#### ![](vista-imaging-system-dicom-importer-iii-user-manual/110.png)Failed Imports.

4.  At the Failed Import Items screen, the system displays a list of items (if any) that failed at some point during import processing. When you select an item from the list, the system displays the details of the item in the Importer Item Error Details scrolling text box. This data gives you a significant amount of information to assist in resolving the issue.

![](vista-imaging-system-dicom-importer-iii-user-manual/111.png)![](vista-imaging-system-dicom-importer-iii-user-manual/112.png)

5.  Once an item is selected, you have several options:
    - To send the error details to support personnel in an email, you can select the error details text and copy it to the system clipboard through the standard Ctrl+C keyboard combination.
    - If you determine that the error is probably due to a transient condition (for example, a file failed to copy because of a temporary network issue), you may resubmit the Importer item by clicking Resubmit Import Item. This resubmits the Importer item to the HDIG in order to attempt processing again. If it fails again, the Importer item reappears in the Failed Import Items list after processing. Resubmission is only successful for a subset of errors, as described above.
    - If you determine that the issue is resolved in another manner and that you no longer need the Importer item, delete it by clicking Delete Import Item. For example, you may determine that all images are successfully transmitted, but the Importer item failed because the HDIG is not able to complete the exam automatically after import. If you can complete the exam through some other means (for example, CPRS), then you may safely delete the Importer item.
6.  When you are finished working with failed Importer items, you can continue working on other Importer use cases, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*](#stopping-the-importer-iii-client).

## Viewing the Application Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client allows administrators to view log files from within the Importer III client.

1.  Start the Importer III client. (See [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/113.png)At the DICOM Importer Home screen, under Administration, click Administration.
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/114.png)At the DICOM Importer Administration Home screen, under View Log, click Log.
4.  ![](vista-imaging-system-dicom-importer-iii-user-manual/115.png)At the Log screen, the system displays the contents of the latest application log file. You can copy text out of the log to the system clipboard by selecting it and pressing the Ctrl+C key combination on your keyboard.
5.  The list does not refresh automatically. Click Refresh at any time to refresh the display manually. When you are finished working with the application log, you can continue working on other Importer scenarios, or you may exit or log out of the Importer III client by following the steps found in [*Stopping the Importer III Client*.](#stopping-the-importer-iii-client)

# Chapter 6: Viewing Study Data and Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the steps required for viewing study data and images. You can view study data, images, and DICOM headers when performing advanced staging, or from the Study List screen during the reconciliation workflow.

1.  At the Study Details window, enter an image number or a range of image numbers in the text box under Images.
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/116.png)Click View Images.

> The image or images display in the DICOM Viewer.

> ![](vista-imaging-system-dicom-importer-iii-user-manual/117.png)

3.  You may select additional series to review the images and DICOM information.

> Note: If you need to view the DICOM header and group information for details on the institution, address, physician name, and so on, follow the steps in *Optionally Viewing the DICOM Header and Group Information*. In addition, follow this procedure to resolve any issues with the order.

4.  In the File menu, click Exit to close the DICOM Viewer application.
5.  In the Study Details window, click Close.

## Optionally Viewing the DICOM Header and Group Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view DICOM header and group information:

1.  On the ViewInfo menu in the DICOM Viewer window, click DICOM Header. The DICOM Header window displays.
2.  ![](vista-imaging-system-dicom-importer-iii-user-manual/118.png)Check the DICOM header information by clicking the Header tab. The displayed metadata lists provide details such as the name of the institution and department, date, and physician name.
3.  ![](vista-imaging-system-dicom-importer-iii-user-manual/119.png)Click the Group 2 tab to view the technical information.
4.  Close the DICOM Header, Importer, and Study Details windows.

> The Importer window redisplays, so that the staging of media for import can continue.

# Chapter 7: Running Usage Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reports can be displayed on a screen, sent to a printer, or exported to a file. The Importer III client can also generate a real-time report, which displays the total data imported into a network share location, by showing the following:

- Import Details
- Totals by Location
- Totals by Modality

> DICOM Importer III writes all generated errors to the Application log.

## Sample Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Import Details report displays a statistical count for studies, series in a study, and objects (images or reports), both successful and failed, that are imported on a specified date or a range of dates.

![](vista-imaging-system-dicom-importer-iii-user-manual/120.png)

> The Totals by Location report displays a statistical count for studies, series in a study, and objects (images or reports), both successful and failed, that are imported on a specified date for a specified location.

![](vista-imaging-system-dicom-importer-iii-user-manual/121.png)

> The Totals by Modality report displays a statistical count for studies, series in a study, and objects (images or reports) both successful and failed that are imported on a specified date. The report also contains the breakdown by modality, as seen in the following example.

![](vista-imaging-system-dicom-importer-iii-user-manual/122.png)

## User Role

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The role of the RU is to generate statistical reports at the Study level.

## Running a Usage Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To run a usage report.

> Role: As the RU (or ARA), your task is to run usage reports.

1.  Start the Importer III client. (See [*Starting the Importer III Client*](#starting-the-importer-iii-client) for instructions on starting the Importer III client.)
2.  At the Windows Security box, make sure you have a valid PIV card attached to your computer and enter your PIN code to log in to the Importer III client.
3.  Click OK.
4.  If the site has more than one division, then select the division in the Select Division window and click OK. Otherwise, go to step 5.
5.  ![](vista-imaging-system-dicom-importer-iii-user-manual/123.png)![](vista-imaging-system-dicom-importer-iii-user-manual/124.png)At the DICOM Importer Home screen, under Reports, click Reports.
6.  At the Reports Home screen, under Filters, select one of the following report types from the

> Report Type drop-down box.

- Import Details
- Totals by Location
- Totals by Modality

> ![](vista-imaging-system-dicom-importer-iii-user-manual/125.png)

7.  ![](vista-imaging-system-dicom-importer-iii-user-manual/126.png)Click the calendar icon at the far-right end of the Start Date and End Date text boxes to specify the date range. Select dates from the corresponding pop-up calendars.
8.  Click View Report to display the data, as seen in the following examples of the three report types.
9.  To print the report, click Print in the bottom-right corner of the Importer window.
10. In the Print dialog box, specify the printing preferences and click Print.
11. To save the report, click Save As in the bottom-right corner of the Importer window.
12. In the Save As dialog box, specify the path and file name, and then click Save.
13. Exit or log out of the Importer III client by following the steps found in [*Stopping theImporter III Client*.](#stopping-the-importer-iii-client)

# Appendix A: Setting Up Outside Imaging Locations for the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a prior, unordered, outside radiology study is imported into VistA, an order is automatically placed for it. The VistA order, created for the outside radiology study, should not accrue workload statistics for VA technical or professional components, because the exam was neither performed in the VA, nor interpreted by the VA. For this reason, the order created on VistA should use a RADIOLOGY IMAGING LOCATION (#79.1) with a CREDIT METHOD =

> No Credit.

> The VistA Imaging OUTSIDE IMAGING LOCATION file (#2006.5759) is used by the Importer III client to designate the entry in the Radiology IMAGING LOCATIONS file (#79.1) with CREDIT METHOD = No Credit (which is to be used for the order created on VistA). There has to be one entry in the VistA Imaging OUTSIDE IMAGING LOCATION file (#2006.5759) for each enabled Radiology Imaging Type in each division.

> The standard Radiology Package tools are used for creating the entries in the Radiology IMAGING LOCATIONS file (#2006.5759). These include Parameter Set-up \[RA SYSLOC\] and Division Parameter Set-up \[RA SYSDIV\] options of the System Definition Menu \[RA SYSDEF\]. VistA Imaging provides the IMPORTER menu \[MAG IMPORTER MENU\] for constructing the OUTSIDE IMAGING LOCATION file (#2006.5759).

> A Radiology/Nuclear Medicine Automated Data Processing Coordinator (ADPAC) should perform the modifications to Radiology Division and Imaging Locations files, as they should have the necessary menu privileges.

> Note: If a site already has a No Credit outside location established for a Radiology Imaging Type for a division, it may be used instead of creating a new one.

## Step 1 – Identify Imaging Types and Divisions that Need “No Credit” Imaging Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step is performed by VistA Imaging site personnel.

> Log into VistA and select the VistA Imaging System Manager menu \[MAG SYS MENU\]. Then select the IMPORTER Menu \[MAG IMPORTER MENU\] and the Check Outside Imaging Location file option \[MAG CHECK OUT IMG LOC\]. In this example, there are two enabled Image Types (General Radiology and Nuclear Medicine) for the Salt Lake City Division.

> IMAGing System Manager Menu

> HL7 Imaging HL7 Messaging Maintenance ... IX Image Index Conversion Menu ...

> LS Edit Network Location STATUS TR Telereader Menu ...

> Ad hoc Enterprise Site Report Configure AE Security Matrix Settings Delete Image Group

> Enter/edit Reason

> Imaging Database Integrity Checker Menu ... Imaging Site Reports ...

> Importer Menu ...

> Select Imaging System Manager Menu Option: IMPORTER Menu Build Outside Imaging Location file

> Check Outside Imaging Location file Display Studies to be Imported

> Select Importer Menu Option: CHECK Outside Imaging Location file

> Checking the Radiology files... Division: SALT LAKE CITY

> GENERAL RADIOLOGY - Define “No Credit” Imaging Location!

> NUCLEAR MEDICINE - Define “No Credit” Imaging Location!

> Please define missing “No Credit” imaging locations for the aforementioned

> divisions and imaging types (using the Location Parameter Set-up \[RA SYSLOC\]

> Note that the SALT LAKE CITY Division has two Imaging Types (GENERAL RADIOLOGY and NUCLEAR MEDICINE) that need to have a NO CREDIT Imaging Location defined for them. The Radiology ADPAC does this in Steps 2 – 4 of this appendix.

> If the site has a No Credit imaging location already defined for the imaging type, the ADPAC does not have to create a new No Credit imaging location. However, the ADPAC should create the OUTSIDE STUDY Camera/Equip/Rm and assign it to the No Credit imaging location.

## Step 2 – Create the OUTSIDE STUDY Entry in the CAMERA/EQUIP/RM File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Radiology ADPAC performs this step.

> Select the System Definition Menu \[RA SYSDEF\] from the Supervisor Menu \[RA SUPERVISOR\]. Edit the Camera/Equip/Rm parameters. Create a new OUTSIDE STUDY and enter the description, Study performed outside of this facility.

> System Definition Menu ... Unverify a Report for Amendment Update Exam Status

> Utility Files Maintenance Menu ...

> Select Supervisor Menu Option: System Definition Menu

> Camera/Equip/Rm Entry/Edit Division Parameter Set-up List of Cameras/Equip/Rms Location Parameter List Location Parameter Set-up Print Division Parameter List

> Select System Definition Menu Option: CAMERA/Equip/Rm Entry/Edit Select Camera/Equip/Room: OUTSIDE STUDY

> Are you adding ‘OUTSIDE STUDY’ as a new CAMERA/EQUIP/RM (the 10TH)? No// Y (Yes)

> CAMERA/EQUIP/RM DESCRIPTION: Study performed outside of this facility CAMERA/EQUIP/RM: OUTSIDE STUDY//

> DESCRIPTION: Study performed outside of this facility Replace

> Select Camera/Equip/Room:

## Step 3 – Add New Outside Imaging Locations for Each Imaging Type to Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Radiology ADPAC performs this step.

> For each division, enter the name of each outside imaging location; one for each Imaging Type for the Division. The suggested naming convention is as follows:

> OUTSIDE \<*Division Mnemonic*\> \<*Imaging Type Abbreviation*\>

#### Naming Convention Example

> In this fictitious example, the facility has the following Imaging Types enabled.

| Imaging Type (from IMAGING TYPE file \#79.2) | Abbreviation |
|--------------------------------------------------|------------------|
| GENERAL RADIOLOGY                                | RAD              |
| NUCLEAR MEDICINE                                 | NUC MED          |
| ULTRASOUND                                       | US               |
| MAGNETIC RESONANCE IMAGING                       | MRI              |
| CT SCAN                                          | CT               |
| ANGIO/NEURO/INTERVENTIONAL                       | ANGIO            |
| CARDIOLOGY STUDIES (NUC MED)                     | CARD             |
| VASCULAR LAB                                     | VAS              |
| MAMMOGRAPHY                                      | MAM              |

> Let us say that the facility has two divisions, SALT LAKE CITY VAMC and CLEAR WATER LAKE VAMC. We chose SLC as the division mnemonic for the first, and CWL as the mnemonic for the second.

> Here is the list of Outside Imaging Locations that we need to add to the system.

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OUTSIDE SLC RAD</p>
</blockquote></th>
<th><blockquote>
<p>OUTSIDE CWL RAD</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OUTSIDE SLC NUC MED</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL NUC MED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTSIDE SLC US</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL US</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTSIDE SLC MRI</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL MRI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTSIDE SLC CT</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL CT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTSIDE SLC ANGIO</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL ANGIO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTSIDE SLC CARD</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL CARD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTSIDE SLC VAS</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL VAS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTSIDE SLC MAM</p>
</blockquote></td>
<td><blockquote>
<p>OUTSIDE CWL MAM</p>
</blockquote></td>
</tr>
</tbody>
</table>

> End of Naming Convention Example.

> In the rest of the examples, there is only the SALT LAKE CITY Division and two IMAGE TYPES: GENERAL RADIOLOGY and NUCLEAR MEDICINE.

> Select the System Definition Menu \[RA SYSDEF\]. Select a Division. Accept the defaults until reaching the Imaging Locations Associated with this Division section. Enter the name of each outside imaging location, one for each Imaging Type for the Division.

> In this example, we are creating the Imaging Locations, OUTSIDE SLC RAD and OUTSIDE SLC NUC MED (the others are created the same way). For each location, select HOSPITAL LOCATION TYPE: CLINIC, HOSPITAL LOCATION TYPE EXTENSION: CLINIC//, and the

> appropriate Imaging Type.

> Delete Printed Batches By Date Exam Deletion

> Inquire to File Entries

> List Exams with Inactive/Invalid Statuses Maintenance Files Print Menu ...

> Mass Override Exam Status

> Override a Single Exam’s Status to ‘complete’

> Print File Entries

> Rad/Nuc Med Personnel Menu ... Restore a Deleted Report Search File Entries

> Switch Locations

> System Definition Menu ... Unverify a Report for Amendment Update Exam Status

> Utility Files Maintenance Menu ...

> Select Supervisor Menu Option: system Definition Menu

> Camera/Equip/Rm Entry/Edit Division Parameter Set-up List of Cameras/Equip/Rms Location Parameter List Location Parameter Set-up Print Division Parameter List

> Select System Definition Menu Option: division Parameter Set-up Select Division: 660 SALT LAKE CITY UT 660

> ...OK? Yes// (Yes)

> Division-wide Order Entry Parameters:

> ASK ‘IMAGING LOCATION’: NO// TRACK REQUEST STATUS CHANGES: NO// CLINICAL HISTORY MESSAGE:

> Exam Entry/Edit Parameters:

> DETAILED PROCEDURE REQUIRED: no// ASK ‘CAMERA/EQUIP/RM’: no//

> AUTO USER CODE FILING: yes// TRACK EXAM STATUS CHANGES: no// TIME LIMIT FOR FUTURE EXAMS:

> Films Reporting Parameters:

> ALLOW STANDARD REPORTS: yes// ALLOW BATCHING OF REPORTS: yes// ALLOW COPYING OF REPORTS: yes//

> IMPRESSION REQUIRED ON REPORTS: yes// ALLOW VERIFYING BY RESIDENTS: yes// ALLOW RPTS ON CANCELLED CASES?: no// WARNING ON RPTS NOT YET VERIF?: yes// AUTO E-MAIL TO REQ. PHYS?:

> ALLOW E-SIG ON COTS HL7 RPTS: no// INTERPRETING STAFF REQ’D?: YES//

> Miscellaneous Division Parameters:

> PRINT FLASH CARD FOR EACH EXAM: no// PRINT JACKET LBLS W/EACH VISIT: no// CONTRAST REACTION MESSAGE:

> RPHARM DOSE WARNING MESSAGE:

> No existing text Edit? NO//

> HL7 Applications Associated with this Division:

> Select HL7 RECEIVING APPLICATION:

> Imaging Locations Associated with this Division:

> Select IMAGING LOCATION: TD-MAINRAD// OUTSIDE SLC RAD

> Are you adding ‘OUTSIDE SLC RAD’ as

> a new HOSPITAL LOCATION? No// Y (Yes) HOSPITAL LOCATION TYPE: C CLINIC HOSPITAL LOCATION TYPE EXTENSION: CLINIC//

> Are you adding ‘OUTSIDE SLC RAD’ as

> a new IMAGING LOCATIONS (the 3RD)? No// Y (Yes) IMAGING LOCATIONS TYPE OF IMAGING: ?

> Enter an imaging type for this location.

> Answer with IMAGING TYPE OF IMAGING, or ABBREVIATION

> Choose from: ANGIO/NEURO/INTERVENTIONAL CARDIOLOGY STUDIES (NUC MED) CT SCAN

> GENERAL RADIOLOGY MAGNETIC RESONANCE IMAGING MAMMOGRAPHY

> NUCLEAR MEDICINE ULTRASOUND VASCULAR LAB

> IMAGING LOCATIONS TYPE OF IMAGING: GENERAL RADIOLOGY

> Are you adding ‘OUTSIDE SLC RAD’ as

> a new IMAGING LOCATIONS (the 3RD for this RAD/NUC MED DIVISION)? No//

> Y

> (Yes)

> Select IMAGING LOCATION: OUTSIDE SLC NUC MED

> Are you adding ‘OUTSIDE SLC NUC MED’ as a new HOSPITAL LOCATION? No// Y (Yes)

> HOSPITAL LOCATION TYPE: C CLINIC HOSPITAL LOCATION TYPE EXTENSION: CLINIC//

> Are you adding ‘OUTSIDE SLC NUC MED’ as

> a new IMAGING LOCATIONS (the 4TH)? No// Y (Yes) IMAGING LOCATIONS TYPE OF IMAGING: NUCLEAR MEDICINE

> \*\* Caution: You are activating a new Imaging Type. \*\* This means you will have to assign procedures to this imaging type. Workload reports will be printed separately for this Imaging Type.

> Are you sure? YES

> Are you adding ‘OUTSIDE SLC NUC MED’ as

> a new IMAGING LOCATIONS (the 4TH for this RAD/NUC MED DIVISION)? No// (No)??

> Select IMAGING LOCATION:

> Division Parameters have been set!

> Imaging Location TD-RAD is OK.

> Imaging Location TD-MAINRAD is OK.

> Imaging Location file \#79.1 entry OUTSIDE SLC RAD has a missing or invalid DSS ID. The Radiology/Nuclear Medicine ADPAC should use the Location Parameter Set-up \[RA SYSLOC\] option to enter a valid imaging DSS Code for this imaging location.

> Select Division:

> Camera/Equip/Rm Entry/Edit Division Parameter Set-up List of Cameras/Equip/Rms Location Parameter List Location Parameter Set-up Print Division Parameter List

> Select System Definition Menu Option:

## Step 4 – Define Outside Imaging Locations Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Radiology ADPAC performs this step.

> Use the Location Parameter Set-up menu \[RA SYSLOC\] option to specify the CAMERA/EQUIP/RM, and set the CREDIT METHOD to No Credit and the DSS ID to X- RAY.

> ...OK? Yes// Y (Yes)

> (GENERAL RADIOLOGY-660)

> Imaging Location: OUTSIDE SLC RAD

> Flash Card Parameters:

> HOW MANY FLASH CARDS PER VISIT: DEFAULT FLASH CARD FORMAT:

> No default flash card printer has been assigned. Contact IRM.

> Jacket Label Parameters:

> As specified in the division parameters, no jacket labels will be printed automatically upon a patient visit.

> DEFAULT JACKET LABEL FORMAT:

> No default jacket label printer has been assigned. Contact IRM.

> Exam Label Parameters:

> HOW MANY EXAM LABELS PER EXAM: 1// DEFAULT EXAM LABEL FORMAT:

> Exam label printer is always the same as the flash card printer.

> Order Entry Parameters:

> No default request printer has been assigned. Contact IRM.

> Report Parameters:

> DEFAULT REPORT HEADER FORMAT:

> DEFAULT REPORT FOOTER FORMAT:

> REPORT LEFT MARGIN: 10// REPORT RIGHT MARGIN: 70// PRINT DX CODES IN REPORT?:

> VOICE DICTATION AUTO-PRINT:

> No default report printer has been assigned. Contact IRM.

> Cameras/Equip/Rooms Used by this Location:

> Select CAMERA/EQUIP/RM: ?

> ‘^’ TO STOP:

> You may enter a new CAMERAS/EQUIP/RMS, if you wish Enter all the cameras/equip/rms for this location.

> Answer with CAMERA/EQUIP/RM, or DESCRIPTION Choose from:

> OR1 OR RM 1

> OR2 OR RM 2

> PORTABLE MOBILE PICTURES RM0 2150

> RM2 RM 2151

> RM3 CHEST UNIT

> OUTSIDE STUDY Study performed outside of this facility TD RAD-EXAM1 This is the primary x-ray room.

> TD RAD-EXAM2 Sonograms are done in this room. TD RAD-EXAM3 Endoscopies are done in this room.

> You may enter a new CAMERA/EQUIP/RM, if you wish

> Enter a name for this camera/equip/rm, between 1 and 30 characters

> in

> length.

> Select CAMERA/EQUIP/RM: OUTSIDE STUDY Study performed outside of this facility

> Are you adding ‘OUTSIDE STUDY’ as a new CAMERAS/EQUIP/RMS (the 1ST for this IMAGING LOCATIONS)? No// Y (Yes)

> Select CAMERA/EQUIP/RM:

> Default CPT Modifiers used by this Location:

> \+ +

> \| Your entry cannot be compared with a CPT CODE, so be very sure \|

> \| that this is the Default CPT Modifier that you want to stuff \|

> \| into every registered exam from this imaging location. \|

> \+ + Select DEFAULT CPT MODIFIERS(LOC): ?

> You may enter a new DEFAULT CPT MODIFIERS(LOC), if you wish

> VA local modifiers are automatically screened out (rejected.)

> \+ +

> \| Your entry cannot be compared with a CPT CODE, so be very sure \|

> \| that this is the Default CPT Modifier that you want to stuff \|

> \| into every registered exam from this imaging location. \|

> \+ +

> Choose a CPT Modifier that should be automatically stuffed into the exam record, when the following 2 conditions

> are both met :

1.  There is no default CPT Modifier for this exam’s procedure.
2.  This location is the current sign-on (or switched-to) location at the time of registration.

> If your entry is invalid, then during exam registration, this Default CPT Modifier will NOT be stuffed, instead, an error message with the name of the rejected CPT Modifier would be displayed.

> Answer with CPT MODIFIER, or NAME, or CODE, or BEGIN CPT RANGE, or END CPT RANGE

> Do you want the entire CPT MODIFIER List? N

> Select DEFAULT CPT MODIFIERS(LOC):

> Recipients of the ‘Stat’ Alert for this Location: Select STAT REQUEST ALERT RECIPIENTS:

> ALLOW ‘RELEASED/NOT VERIFIED’: no// no INACTIVE:

> TYPE OF IMAGING: GENERAL RADIOLOGY// CREDIT METHOD: 0// ?

> Enter the type of credit this location will receive for this examination.

> Choose from:

1.  Regular Credit
2.  Interpretation Only
3.  No Credit
4.  Technical Component Only CREDIT METHOD: 0// 2 No Credit

> DSS ID: ?

> Enter a valid stop code for this imaging location.

> Only Stop Codes entered in the Imaging Stop Codes file may be selected.

> Answer with CLINIC STOP NAME, or AMIS REPORTING STOP CODE

> Do you want the entire CLINIC STOP List? DSS ID: X-RAY 105

> Imaging Location OUTSIDE SLC RAD is OK.

> Select Location:

> Note: Update the other locations in exactly the same fashion.

## Step 5 – OUTSIDE STUDY Camera/Equip/Room for All Radiology Imaging Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Radiology ADPAC performs this step.

> Every Radiology Imaging Location that is used as a contract outside imaging facility needs to have the OUTSIDE STUDY camera/equipment/room assigned to it. When the study is imported, the examination/report status of the case is advanced to either, Examined/No Report if it is to be read locally, or Complete/Electronically Filed if it is finished.

> If DICOM objects are imported for a study with a Radiology Imaging Location that does not have the OUTSIDE STUDY camera/equipment/room assigned to it, then a message like the one that follows displays in the Importer III client session. The examination/report status then needs to be manually advanced.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*

> \*\*\* WARNING: Exam/Report status not advanced to COMPLETE/ELECTRONICALLY FILED

> \*\*\*

> \*\*\*

> \*\*\*

> \*\*\* The Camera/Equipment/Room “OUTSIDE STUDY” is not defined for the Radiology

> \*\*\*

> \*\*\* Imaging Location “XXXXXXXXXX” that is used for this study.

> \*\*\*

> \*\*\*

> \*\*\*

> \*\*\* The data required to advance the status of this case performed at an outside

> \*\*\*

> \*\*\* location has not been entered.

> \*\*\*

> \*\*\*

> \*\*\*

> \*\*\* Due to this condition, the status of the study had not been automatically

> \*\*\*

> \*\*\* advanced. Please manually advance its status by entering the necessary data

> \*\*\*

> \*\*\* using the Radiology package status tracking option.

> \*\*\*

> \*\*\*

> \*\*\*

> \*\*\* Message generated at MUMPS line tag ERR1102+13^MAGDAIRC

> \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Step 6 – Populate VistA Imaging Outside Imaging Location File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging site personnel perform this step.

> Log into VistA and select the VistA Imaging System Manager Menu \[MAG SYS MENU\]. Then select the IMPORTER menu \[MAG IMPORTER MENU\] and the Build Outside Imaging Location file option \[MAG BUILD OUT IMG LOC\]. In this example, there are two enabled Image Types (General Radiology and Nuclear Medicine) for the Salt Lake City Division. Both of these now have CREDIT METHOD = No Credit entries in the Radiology DIVISION and IMAGING LOCATIONS file. The Build Outside Imaging Location file option interactively helps to add/change entries in the file.

> When finished, run the Check Outside Imaging Location file option \[MAG CHECK OUT IMG LOC\] to verify that everything is set up correctly.

> Select OPTION NAME: IMPORTER MENU

> Build Outside Imaging Location file Check Outside Imaging Location file Display Studies to be Imported

> Select Importer Menu Option: Build Outside Imaging Location file

> Checking the Radiology files... Division: SALT LAKE CITY

> Checking the OUTSIDE IMAGING LOCATION file (#2006.5759)...

> Division: SALT LAKE CITY

> GENERAL RADIOLOGY - Create record in file \#2006.5759!

> NUCLEAR MEDICINE - Create record in file \#2006.5759!

> Please fix the aforementioned problems in the OUTSIDE IMAGING LOCATION file

> (#2006.5759) and then run this option again.

> OUTSIDE IMAGING LOCATIONS for SALT LAKE CITY (660)

> GENERAL RADIOLOGY – (not defined yet) OUTSIDE SLC RAD

> Use this value?? n// YES

>  OUTSIDE SLC RAD

> NUCLEAR MEDICINE – (not defined yet) OUTSIDE SLC NUC MED

> Use this value?? n// YES

>  OUTSIDE SLC NUC MED

> Build Outside Imaging Location file Check Outside Imaging Location file Display Studies to be Imported

# Appendix B: Handling Parent-Descendent Procedure Orders with the Importer III Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Radiology2 supports the ability to order parent procedures. Parent procedures are associated with two or more descendent procedures. When the patient is registered for the parent procedure, a separate distinct radiology study, with its own unique accession number, is created for each descendent procedure.

> An example of a parent procedure may be ANKLES, BILATERAL, 2 VIEWS, which is associated with two descendant procedures: LEFT ANKLE 2 VIEWS and RIGHT ANKLE 2 VIEWS. When the patient is registered for ANKLES, BILATERAL, 2 VIEWS, two studies are created, one for LEFT ANKLE 2 VIEWS and one for RIGHT ANKLE 2 VIEWS.

## How It Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The provider orders the parent procedure through CPRS. This goes into the ORDER file (#100) and when signed the same order is filed in the RAD/NUC MED ORDERS file (#75.1). When this order is registered (for example, by the Importer III client or the REG EDIT menu option), individual studies are created for each descendent procedure and are then filed into the EXAMINATIONS (#70.03) multiple, which is a sub-file of the RAD/NUC MED PATIENT file (#70). Unique accession numbers are created for each procedure of the study. The study for each procedure is then treated as a separate entity for examination purposes.

> Each study for each procedure may have its own unique diagnostic report (that is, being defined as an Exam Set – the default) or there may be a single diagnostic report referenced by the descendant procedures (that is, being defined as a Print Set). A parent procedure can be designated as a print set by exercising the Procedure Enter/Edit option and setting the SINGLE REPORT field (#18) of the parent procedure in the RAD/NUC MED PROCEDURES file (#71) to Yes.

## Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the VA orders a parent procedure as a fee-basis contracted examination, then how does the contractor perform the procedure, how are the resultant DICOM objects created, and how should those DICOM objects be imported into VistA?

> 2 Greg Cebelinski of the Radiology Development Team and Jeannie Jernigan of the Fayetteville, NC VAMC contributed to this document.

#### How Outside Fee-basis Imaging Contractors Work

> The outside imaging contractor can execute an order of ANKLES, BILATERAL, 2 VIEWS by two methods.

- Method 1 – The contractor can perform two separate studies, one for the left ankle and one for the right ankle.
- Method 2 – The contractor can perform a single study, which includes both ankles.

> Depending upon how the contractor executes the order, there are two methods to represent the DICOM images for the examination(s).

- Method 1 – If the contractor performs the bilateral ankle order as two separate studies (one for the left ankle and the other for the right ankle), then there are two different contractor-assigned accession numbers (Study Instance UIDs, procedure names, and so on) for each study. Each DICOM image must have either the Series Laterality or the Image Laterality attribute.
- Method 2 – If the contractor performs the bilateral ankle order as one study, then there is one contractor-assigned accession number (Study Instance UID, procedure name, and so on) for all the DICOM images.

> – The contractor may choose to use two separate series (one for the left ankle and the other for the right ankle) and specify the Series Laterality for all the DICOM images in that series. In this case, each series has a unique Series Instance UID.

- The contractor may also choose to use one series for all the ankle images and specify the Image Laterality for each DICOM image in the series. In this case, there is only one Series Instance UID for the entire study.

#### How to Use the Importer III Client for DICOM Images for Parent/Descendent Procedures

> The choice of method used by the contractor to perform the examination(s), and how the resultant images are represented in DICOM, have a great bearing on how the images should be imported into another system.

> The Importer III client does not handle parent/descendent procedures automatically. Some manual effort is required to do this properly. The level of effort depends on how the study is performed and how the DICOM images are created. The following procedure may be used as a guideline.

1.  Use Importer menu option 2 – Import Outside Contracted studies.
2.  Using the Importer, determine whether the contractor chose to perform the bilateral ankle as one study or as two separate studies.
3.  If the contractor chose to perform the bilateral ankle as two separate studies, then the images from the left outside study are imported to the left VistA study and the images from the right outside study are imported to the right VistA study. Perform the following instructions to complete Step 3.
    - Select the LEFT side study in the Importer.

> Use the lookup in Radiology Order file option.

> Select the patient and the order for the parent procedure. Import the LEFT side study.

> Exit the Importer III client.

> Using the VistA Rad application (the Radiology package to view by case) or CPRS Imaging (local only) Reports tab, confirm that the second study for the right side study is created as a result of the bilateral study order (parent/descendant). This study will be in a *waiting for exam* status. Obtain the accession number for it.

> Use Importer menu option 2 – Import Outside Contracted studies, and re-enter the Importer III client.

> Select the RIGHT side study in the Importer. Use the Modality Worklist look up option.

> Select the VistA RIGHT side procedure study for the patient by entering its accession number for the query key.

> Import the RIGHT side study.

> Confirm that the RIGHT side images from the outside study are attached to the VistA RIGHT side study, and that the study is completed (Exam Status = Exam Complete and Report Status = Electronically Filed).

4.  If the contractor performed the bilateral ankle order as one study, then there is only one accession number, Study Instance UID, procedure name, and so on for all the DICOM images. All of the outside images are imported to the LEFT VistA study. Perform the following instructions to complete step 4.
    - Select the study in the Importer.

> Use the lookup in Radiology Order file option.

> Select the patient and the order for the parent procedure. Import the study.

> – The Importer registers the parent procedure and automatically creates a study for the LEFT ANKLE 2 VIEWS procedure and a study for the RIGHT ANKLE 2 VIEWS procedure.

- The accession number for the study for the LEFT ANKLE 2 VIEWS procedure is returned and all the images are imported to it.

> In the Radiology package, insert your local combined standard report stub to indicate that the images and report are uploaded to the LEFT study. Then update the status manually in the Radiology package per local policy/procedures.

> It is beyond the scope of the Importer III client to be able to identify which images are for the left ankle and import them to the left procedure, and to identify which images are for the right ankle and import them to the right-side procedure. Two facets of this scenario are difficult. First, the Importer III client works at the study level and not the series or image level. Second, DICOM images from one study cannot be filed with two different studies in VistA, because this would create duplicate Study Instance UIDs and possibly duplicate Series Instance UIDs (if all the images were in the same series). This is a violation of the DICOM Standard and not a limitation of the Importer III client or VistA Imaging.

> Note: It is advantageous to require that the outside contracted vendor perform the bilateral ankle as two separate studies. By implementing this requirement, the images can be properly associated with the corresponding two VistA studies.

# Appendix C: Problems Seen in Importing DICOM Objects from Media

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III client is designed to work with media that is formatted according to the DICOM Standard and the IHE PDI integration profile. DICOM objects on compliant media usually are able to be imported. Those on non-compliant media may not be able to be imported.

> Here is a list of some of the problems that one could expect to see.

- The media is just blank.
- The media is written improperly. Here is an example where the vendor did not enter the files into the directory correctly:

> E:\\dir

> Volume in drive E has no label. Volume Serial Number is 8B34-8C3C

> Directory of E:\\

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 21%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>The parameter is incorrect.</th>
<th><blockquote>
<p>12:00 AM</p>
</blockquote></th>
<th><blockquote>
<p>3,920 DICOMDIR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The parameter is incorrect.</td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>759 DiscView.htm</p>
</blockquote></td>
</tr>
<tr class="even">
<td>The parameter is incorrect.</td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>240 QuickViewer.txt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>The parameter is incorrect.</td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>105,320 Readme1st.htm</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 01/15/2010 08:49 AM \<DIR\> Readme1st_files The parameter is incorrect. 01/15/2010 08:49 AM 72 autorun.bat The parameter is incorrect. 01/15/2010 08:49 AM 29 autorun.inf

> 01/15/2010 08:49 AM \<DIR\> data

> 6 File(s) 110,340 bytes4

> 2 Dir(s) 0 bytes free

> E:\\

- There is no DICOMDIR on the media and the images are kept in separate sub-folders. The Importer III client cannot be used directly.

> If there are DICOM files on the media, then they might be able to be sent to a C-Store process on the Importer III gateway. The BATCH_SEND_IMAGE.BAT batch file may be able to be used to extract the DICOM files from the media and send them. Otherwise, it may be necessary to use a commercial product (like Sorna<sup>3</sup>) to read the media and send the DICOM files to the C-Store process.

> <sup>3</sup> <http://www.sorna.com/>

> Appendix C: Problems Seen in Importing DICOM Objects from Media

- There are errors in DICOMDIR.
  - The file name of each DICOM object uses forward slashes, rather than back slashes, as required by the DICOM Standard.
  - The Referenced SOP Class UID is wrong. (One vendor used the Media Storage Directory Storage SOP Class. Another vendor used the character string *SOP UID*. It must be the same as the SOP Class UID of the DICOM object.)
  - The Referenced Transfer Syntax UID is absent even though it is a Type 1 (that is, a required data element with a non-null value).
- The Modality is a DICOM Series attribute. It may not be defined in DICOMDIR for the Series directory record type even though it is a Type 1.
- DICOMDIR is fine, but the DICOM objects are not supported by VistA Imaging.

> The subset of DICOM SOP Classes and Transfer Syntaxes that VistA Imaging supports is specified in the AE Security Matrix. Here is a sample error message:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\*

> \*\*\* There are 871 DICOM objects that cannot be stored on VistA. \*\*\*

> \*\*\* Each is flagged with a yellow question mark ? below. \*\*\*

> \*\*\* \*\*\*

> \*\*\* SOP Class: CT Image Storage \*\*\*

> \*\*\* Transfer Syntax: JPEG Lossless, Non-Hierarchical (Process 14): Default \*\*\*

> \*\*\* Lossless JPEG Compression \*\*\*

> \*\*\* Problem: The Transfer Syntax is not supported – 871 DICOM objects \*\*\*

> \*\*\* \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

- Outside source places multiple patient exams on their same accession number (Skull, hand, foot all done as one exam). This is difficult to handle when this study is imported into VistA Imaging.
- The media contains only JPEG2000 images and no DICOM images.
- One, or more, images in a study are incomplete (for example, only the top half of a chest x-ray). The image(s) fail(s) image processing.
- The exam was not performed according to radiology best practices standard of care. For example, a fee-basis contracted order for a “knee 3 views” only has two images.
- The outside modality creates a study with a UID that is a duplicate of one, which is already on VistA for another patient.
- Some of the expected DICOM header information may be incorrect or blank (for example, technician name, body location, radiology location, and so on).
- The media is a copy of an earlier one. (This one is easy – the Importer III client automatically prevents an imported DICOM object from being imported a second time.)

> March 2019 DICOM Importer III User Manual 114

> VistA Imaging 3.0

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AE</td>
<td>Application Entity</td>
</tr>
<tr class="even">
<td>AE_Title</td>
<td>A unique name assigned to a DICOM device to identify it. AE_Title is used to log machine-to-machine communication within this patch.</td>
</tr>
<tr class="odd">
<td><p>AGFA DICOM</p>
<p>Proxy Server</p></td>
<td>The conduit for the DICOM objects transmitted from the DoD to the VA Polytrauma Centers.</td>
</tr>
<tr class="even">
<td>AMSU</td>
<td>Advanced Media Staging User – See Media Staging</td>
</tr>
<tr class="odd">
<td>Application Log</td>
<td>The application log records information about activities in application instances. This log may contain PHI.</td>
</tr>
<tr class="even">
<td>Artifact</td>
<td>Any object stored within VistA Imaging. This includes images and reports.</td>
</tr>
<tr class="odd">
<td>Artifact Reconciliation Administrator</td>
<td>ARA – A user of MAG*3.0*118 software who has full rights to administer and perform all import and reconciliation activities.</td>
</tr>
<tr class="even">
<td>Audit Log</td>
<td>A chronological sequence of audit records, each of which contains evidence directly pertaining to and resulting from the execution of a business process or system function. This log does not contain any PHI.</td>
</tr>
<tr class="odd">
<td>BMSU</td>
<td>Basic Media Staging User – See Staging</td>
</tr>
<tr class="even">
<td>Business Rules</td>
<td><p>Business rules authorize specific users or groups of users, to perform specified actions on documents in particular statuses (for example, a practitioner who is also the expected signer of the note may edit an Unsigned Progress Note).</p>
<p><strong>Note</strong>: Sites can modify or add to these rules to meet their own local needs.</p></td>
</tr>
<tr class="odd">
<td>CBOC</td>
<td>Community-based Outpatient Clinic – A CBOC is a VA-operated clinic (in a fixed location), or a VA-funded or reimbursed health care facility or site that is geographically distinct or separate from the parent medical facility.</td>
</tr>
<tr class="even">
<td>CD</td>
<td>Compact Disc</td>
</tr>
<tr class="odd">
<td>Contracted Study</td>
<td>A study ordered at the VA, but contracted to be performed at an outside facility. After the examination, the DICOM objects from the outside facility are delivered back to the VA for importing purposes.</td>
</tr>
<tr class="even">
<td>Contracted Study Reconciliation Administrator</td>
<td>CSRA – An individual assigned the rights to use MAG*3.0*118 reconciliation activities on Contracted studies.</td>
</tr>
</tbody>
</table>
| Term            | Definition                                                                                                                                                                                                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cPACS               | Commercial PACS (see the definition for PACS)                                                                                                                                                                                                                                                 |
| CPRS                | Computerized Patient Record System                                                                                                                                                                                                                                                            |
| Data Sources        | Database structures or files that contain required information.                                                                                                                                                                                                                               |
| Decryption          | A security tool used to decode protected information.                                                                                                                                                                                                                                         |
| DICOM               | Digital Imaging and Communications in Medicine – a protocol for sharing and viewing medical images. DICOM has traditionally been used for radiology images, and most recently used for images in other specialties such as cardiology, dental, gastrointestinal endoscopy, and ophthalmology. |
| DICOM Correct       | The name assigned to the software routine used to correct DICOM objects that fail processing on the DICOM Gateway.                                                                                                                                                                            |
| DICOM Gateway       | Interface between VistA and external DICOM Application Entity                                                                                                                                                                                                                                 |
| DICOMDIR            | A file that is a unique and mandatory DICOM Directory file that contains the Media Storage Directory SOP Class as described in DICOM PS 3.10 2008.                                                                                                                                            |
| Direct Import       | Copying DICOM objects from an external media bundle, matching it to the VA study, updating necessary data sources, and sending the objects to the HDIG for processing, bypassing Importer III Persistent Storage.                                                                             |
| DoD                 | Department of Defense                                                                                                                                                                                                                                                                         |
| DVD                 | Digital Versatile Disc                                                                                                                                                                                                                                                                        |
| EMR                 | Electronic Medical Record                                                                                                                                                                                                                                                                     |
| Encryption          | The translation of data into a form that is unintelligible without a deciphering mechanism.                                                                                                                                                                                                   |
| GUI                 | Graphical User Interface                                                                                                                                                                                                                                                                      |
| HDIG                | Hybrid DICOM Imaging Gateway – A gateway that runs both the legacy gateway and the VISA gateway.                                                                                                                                                                                              |
| High Impact Systems | An information system in which a least one security objective (that is, confidentiality, integrity, or availability) is assigned a FIPS 199 potential impact value of high.                                                                                                                   |
| HIPAA               | Health Insurance Portability and Accountability Act                                                                                                                                                                                                                                           |
| HIS                 | Hospital Information System                                                                                                                                                                                                                                                                   |
| IEN                 | Internal Entry Number                                                                                                                                                                                                                                                                         |
| Term                          | Definition                                                                                                                                                                                                                                                                   |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IHE                               | Integrating the Healthcare Enterprise                                                                                                                                                                                                                                            |
| Imaging Type                      | A VistA Radiology Package entity that roughly designates a class of DICOM modalities. For example, General Radiology consists of CR, DX, and RF. CT, MRI, and Ultrasound are other examples of Imaging Types. The Imaging Type must be specified when placing a radiology order. |
| Importer III client               | Software that performs the automated DICOM import process from outside facilities.                                                                                                                                                                                               |
| Importer III Persistent Storage   | Storage area within Vista Imaging where DICOM objects awaiting reconciliation or DICOM Correction are stored.                                                                                                                                                                    |
| Importing                         | Accepting study data from an authorized source, updating relevant data sources, and sending it to the HDIG for processing.                                                                                                                                                       |
| IRA                               | Initial Requirements Analysis                                                                                                                                                                                                                                                    |
| IRWF                              | Import Reconciliation Workflow                                                                                                                                                                                                                                                   |
| ISO                               | Information Security Officer – Individual responsible to the senior agency information security officer, authorizing official, or information system owner for ensuring that the appropriate operational security posture is maintained for an information system or program.    |
| Media Bundle                      | Used to reference all data on an external data source being processed by the MAG\*3.0\*118 software,                                                                                                                                                                             |
| Media Formats                     | Media Formats and Physical Media for Data Interchange (such as a CD, DVD, flash drive, or external hard drive) are defined in DICOM PS 3.12 2008.                                                                                                                                |
| Media Storage Application Profile | Defines a selection of choices at the various layers of the DICOM Media Storage Model which are applicable to a specific need or context in which the media interchange is intended to be performed as described in DICOM PS 3.11 2008.                                          |
| Modality Code                     | A code defined by the DICOM Standard that identifies the type of exam being performed (for example, CR, CT, MR, US).                                                                                                                                                             |
| Modality Device                   | The type of DICOM device being used to generate or utilize DICOM objects.                                                                                                                                                                                                        |
| MUMPS                             | Massachusetts General Hospital Utility Multi-Programming System                                                                                                                                                                                                                  |
| NSR                               | New Service Request                                                                                                                                                                                                                                                              |
| Ordered Study                     | A study that is ordered at the VA and is performed at the VA or contracted to be performed at an outside facility.                                                                                                                                                               |
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ordering Location</td>
<td>The VistA HIS location, which is recorded as the source of the order (for example, for a Polytrauma patient, it would be the Polytrauma ward).</td>
</tr>
<tr class="even">
<td>Ordering Provider</td>
<td>The VistA HIS provider who is recorded as the originator of the order (for example, for a Polytrauma patient, it may be the chief of the Polytrauma Service).</td>
</tr>
<tr class="odd">
<td>Outside Facility</td>
<td>External to the local facility. It can be another VA facility, a DoD facility, or another institution.</td>
</tr>
<tr class="even">
<td>Outside Imaging Location</td>
<td>A VistA HIS/Radiology Package location where the examination is recorded as being performed. For the Importer III client, this is designated as an <em>outside, no credit</em> imaging location. Each radiology Imaging Type must have a corresponding Imaging Location. The Imaging location must be specified when placing a radiology order.</td>
</tr>
<tr class="odd">
<td>PACS</td>
<td>Picture Archive and Communications System</td>
</tr>
<tr class="even">
<td>PDI</td>
<td>Portable Data for Imaging</td>
</tr>
<tr class="odd">
<td>PHI</td>
<td><p>Protected Health Information – is individually identifiable health information transmitted by electronic media, maintained in electronic media, or transmitted or maintained in any other form or medium. PHI excludes education records covered by the Family Educational Rights and Privacy Act, as amended, 20 U.S.C. 1232g, records described at 20 U.S.C.</p>
<p>1232g(a)(4)(B)(iv), and employment records held by a covered entity in its role as employer.</p></td>
</tr>
<tr class="even">
<td>PII</td>
<td>Personal Identifiable Information (see definition for Sensitive Personal Information (SPI))</td>
</tr>
<tr class="odd">
<td>Previously Imported Study</td>
<td>A study that already has some or all of its DICOM objects imported into the VA’s system.</td>
</tr>
<tr class="even">
<td>Queue</td>
<td>A storage location for imported artifacts</td>
</tr>
<tr class="odd">
<td>Reconciliation Administrator</td>
<td>A user of MAG*3.0*118 software who has full rights to administer and perform all import and reconciliation activities.</td>
</tr>
<tr class="even">
<td>Report User</td>
<td>RU – A MAG*3.0*118 user who has the ability to generate reports that summarize the activities performed by the MAG*3.0*118 software.</td>
</tr>
<tr class="odd">
<td>RIS</td>
<td>Radiology Information System</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Call</td>
</tr>
<tr class="odd">
<td>RSD</td>
<td>Requirements Specification Document</td>
</tr>
<tr class="even">
<td>SCP</td>
<td>Service Class Provider</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SCU</td>
<td>Service Class User</td>
</tr>
<tr class="even">
<td>SDD</td>
<td>Software Design Document</td>
</tr>
<tr class="odd">
<td>SOP</td>
<td>Service Object Pair</td>
</tr>
<tr class="even">
<td>SOP Class</td>
<td>Unique Id assigned by the DICOM Standard to identify DICOM objects.</td>
</tr>
<tr class="odd">
<td>SPI</td>
<td>Sensitive Personal Information – The term, with respect to an individual, means any information about the individual maintained by an agency, including the following: (i) education, financial transactions, medical history, and criminal or employment history; (ii) Information that can be used to distinguish or trace the individual’s identity, including name, social security number, date and place of birth, mother’s maiden name, or biometric records.</td>
</tr>
<tr class="even">
<td>Staging</td>
<td><p>Copying study data from either media or an authorized network location into temporary persistent storage for later reconciliation. There are two types of staging (controlled by keys):</p>
<ul>
<li><p>Basic Staging – an authorized user copies all study data from an authorized source to Importer III Persistent Storage.</p></li>
<li><p>Advanced Staging – an authorized user can view source data by study and copy data by study to Importer III Persistent Storage.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Supported SOP Class</td>
<td>A DICOM Object that can be processed by the DICOM Gateway and delivered to other Vista Imaging applications for use within Vista Imaging.</td>
</tr>
<tr class="even">
<td>System Auditing</td>
<td>System audit logs must record sufficient information to establish what events occurred, the sources, and the outcomes of the events. Additional details such as type, location, and subject are also required for moderate and high- risk systems.</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td>Transmission Control Protocol/Internet Protocol</td>
</tr>
<tr class="even">
<td>UID</td>
<td>DICOM Unique Identifier</td>
</tr>
<tr class="odd">
<td>UML</td>
<td>Unified Modeling Language</td>
</tr>
<tr class="even">
<td>Unordered Study</td>
<td>An independently performed study from an outside facility and its DICOM objects, which are delivered to the VA for importing purposes.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>VA Sensitive Patients</td>
<td>Patients tagged in VA systems as requiring additional measures to ensure their health information is protected. Typically, these are employees or VIPs receiving treatment through VA facilities.</td>
</tr>
</tbody>
</table>
| Term                    | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Validated                   | The process of successfully matching an order, DICOM images, and an optional report of imported objects that allows the study to be processed by the DICOM Gateway.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Verifying Provider          | A VistA HIS provider who has permissions to verify radiology reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VISA                        | VistA Imaging System Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VISN                        | Veterans Integrated Service Network                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VistA                       | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| VistA HIS                   | A system that has the ability to store multimedia objects as part of its electronic medical record (EMR). VistA includes the CPRS, which supports order entry, tracking, result entry, and result reporting functions. VistA also includes a complete RIS. VistA Imaging provides a full infrastructure to acquire, store, archive, display, and communicate DICOM and other types of multimedia objects, and is directly interfaced to both CPRS and the RIS. This combination provides PACS capabilities with the VistA HIS for both clinical specialties as well as radiology. |
| VistA Imaging DICOM Gateway | A suite of software used to transfer image files from an acquisition modality or a commercial PACS to VistA, or from VistA to a commercial PACS or workstations.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VistA Study                 | A VistA Radiology study as identified by a corresponding Order and Accession Number, CPRS Consult Request Tracking Consult, or a Procedure Request.                                                                                                                                                                                                                                                                                                                                                                                                                               |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Advanced Staging Media User · 3, 25 Application logging · 2
> ARA role · 4, 34, 35, 37, 40, 55, 60, 63
> Artifact Reconciliation Administrator · 4, 34, 35, 37, 40, 47,
> 55, 60
> ASMU role · 3 Audit logging · 2

### B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Basic Staging Media User · 3 BSMU role · 3

### C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CD/DVD media · 18
> Contracted Study Reconciliation Administrator · 3, 34 Contracted Study Reconciliation Administrator (CSRA) · 40,
> 47, 55, 60
> CPRS · 4
> CSRA role · 3, 34, 35, 37

### D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DICOM compliant · 17 DICOM Correct · 2, 17, 35 DICOM Header · 75 DicomCorrect · 35
> DICOMDIR · 18
> Direct import · 33

### G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hybrid DICOM Image Gateway · 1

### I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IHE · 33
> Import Reconciliation Workflow · 33 Imported Details report · 77
> IRWF · 33

### M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAGV IMPORT MEDIA STAG security key · 5 MAGV IMPORT RECON CONTRACT security key · 5 MAGV IMPORT REPORTS security key · 5
> MAGV IMPORT STAGE MEDIA ADV security key · 5 Media
> Compliant · 17
> Non-compliant · 18

### N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Network, direct import · 17

### O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ordered studies · 34

### P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pending orders · 40, 47, 55, 60 Proxy server · 17

### R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Group details · 76

### H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Header · See DICOM Header
> Reconciling data · 34 Report User · 4 Reports · 77
> Imported Details · 77 Totals by Location · 77 Totals by Modality · 77
> Roles · 2
> RU role · 4, 79

### S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security keys · 4
> Sensitive patient logging · 2 Staging
> Advanced · 25
> Basic · 19 Studies
> Ordered · 34
> Unordered · 34

### T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Terms of use · 3
> Totals by Location report · 77
> Totals by Modality report · 77

### U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unordered studies · 34

### V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VISA · 1
> VistA Imaging System Architecture · 1

### W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workflows Queues · 2
> Wizards · 1
> March 2019 DICOM Importer III User Manual 122
> VistA Imaging 3.0
