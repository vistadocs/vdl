---
title: VistA Imaging Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: VistA Imaging
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
description: > The new VistARad diagnostic radiology reading software is used to retrieve and display full-resolution images and reports for radiology exams. VistARad is integrated with the VISTA Hospital Information System and with the Radiology Package in particular.
audience: 
keywords: 
  - class
  - table
  - blockquote
  - contents
  - image
  - strong
  - even
  - patient
  - style
  - width
page_count: 0
word_count: 2591
section_count: 20
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/imgreleasents.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/imgreleasents.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-release-notes/001.png)

> IMAGING SYSTEM

RELEASE NOTES

> Version 3.0

> March 2002

> Department of Veterans Affairs System Design and Development V*IST*A Imaging

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Section 1 Introduction](#section-1-introduction)
- [Section 2 New Features](#section-2-new-features)
  - [Data Integrity Checking](#data-integrity-checking)
  - [VistA Imaging Server Changes](#vista-imaging-server-changes)
  - [Clinical Display Workstation Changes](#clinical-display-workstation-changes)
  - [Clinical Capture Workstation Changes](#clinical-capture-workstation-changes)
  - [Background Processor Changes](#background-processor-changes)
  - [DICOM Gateway Changes](#dicom-gateway-changes)
  - [Scanning Administrative Documents and Automatic Means Test Transmission](#scanning-administrative-documents-and-automatic-means-test-transmission)
  - [Administrative Document Scanning](#administrative-document-scanning)
  - [Automatic Means Test Transmission](#automatic-means-test-transmission)
  - [Other Enhancements](#other-enhancements)
  - [Clinical Display Enhancements](#clinical-display-enhancements)
  - [DICOM Gateway Enhancements](#dicom-gateway-enhancements)
  - [Background Processor Enhancements](#background-processor-enhancements)
- [Section 3 VistARad Diagnostic Radiology Workstation Software](#section-3-vistarad-diagnostic-radiology-workstation-software)
  - [Overview](#overview)
  - [How VistARad Works](#how-vistarad-works)
  - [The Manager](#the-manager)
  - [The Layout Viewer](#the-layout-viewer)
  - [The Stack Viewer](#the-stack-viewer)
  - [VistA HIS Menu Options for VistARad](#vista-his-menu-options-for-vistarad)
> This document describes new features and enhancements to existing functionality of the V*IST*A Imaging System, V. 3.0. This document is part of the V*IST*A Imaging software documentation set, which includes:
- Release Notes
- Installation Guides
- Security Guide
- Technical Manual
- User Manuals
> Preface

# Section 1 Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging version 3.0 incorporates the new functionality provided by all released patches (1, 3, 4, 5, 8) to version 2.5. In addition, VistARad, the diagnostic radiology workstation software, has been added. A number of DICOM Gateway modifications have also been included in this new version.

> Note: VistA Imaging software is subject to FDA regulation, and the VistA Imaging group must be able to track and document the distribution of this software. Sites will need to file or update their release agreements before receiving this software. Please contact [REDACTED](https://vaww.edis2.med.va.gov/main) for more information.

> For information about resolved defects in this release, refer to the NPM (National Patch Module), or to the patch descriptions available at [REDACTED](https://vaww.edis2.med.va.gov/main)

# Section 2 New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Integrity Checking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vista Imaging 3.0 incorporates data integrity checking tools that will detect and report the following types of inconsistencies:

- Image and associated report are associated with different patients.
- Image is associated with a report that is not associated with this image (or with any image).
- Report is associated with an image that is not associated with this report (or with any report).
- The group’s image information and the image’s group information do not agree.
- An image in a group belongs to a different patient from the patient associated with that group.
- The associated report for an image does not exist.

## VistA Imaging Server Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Created the Database Scanning Utility. When run, this utility checks for discrepancies in the VistA database IMAGING file (2005) and related parent report data files (such as the Radiology Report file).

> Two types of reports can be generated using this utility: a report that lists problems produced by the DSM Global/Volume Set Repacking procedure; and a report that lists all data for images where an inconsistency has been detected. When a report is generated, a copy of the report is emailed automatically to the VistA Imaging Team for analysis.

## Clinical Display Workstation Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Added the capacity to alert users if images fail internal integrity checks. If an inconsistency is detected, the user is alerted and cannot open the suspect image or its associated report. User alerts include information that describes the discrepancy detected.

> Section 2 – New Features

## Clinical Capture Workstation Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Added data integrity checking to the final step of the capture process. If a discrepancy is detected between selected patient and report, the images will be captured, but no association will be made to the report, and the user will be informed that there are consistency problems.

## Background Processor Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Added data integrity checking to the Verifier. In addition to performing the checks described on the preceding page, the Verifier can optionally scan all text (.txt) files within the VistA Imaging Network for matching patient IDs. The range of entries to scan can be defined by selecting a date range (forwards or backwards) or by selecting a range of internal entry numbers of the Image file. The user may also indicate whether the associated image text files should be scanned.

## DICOM Gateway Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Added the capability to check the integrity of the VistA database IMAGING file (2005) and related parent report data files, and to detect the possibility of database rollbacks. If a discrepancy is found, the acquisition process is halted and user intervention is required to continue. The user should investigate the cause of the discrepancy. If a database rollback has occurred, processing should not be restarted until the rollback problem is resolved.

## Scanning Administrative Documents and Automatic Means Test Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Administrative Document Scanning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An image and scanned document index has been added to distinguish Administrative Chart documents/images from Clinical Chart documents/images. Traditionally, there have been two patient charts: the clinical chart and the administrative chart.

- The clinical chart is traditionally located on the ward or clinic when the patient is being seen. It is used for patient care, and clinicians write notes, place orders and review patient records in the clinical chart.
- The administrative chart generally houses administrative documents related to the patient. These include patient correspondence, eligibility documents, financial worksheets, inventory of patient property, request for information, reports of contact and patient rights and responsibilities forms.

> These two major chart categories – Administrative and Clinical – are now the top level index for scanned documents. A new security key is required for viewing administrative documents.

> The document type forms the second level index. When Administrative documents are scanned, the user now selects the document type from a standard, defined list of twenty-three types.

## Automatic Means Test Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Added the capacity to automatically copy scanned Means Test images to a network location provided by the Health Eligibility Center (HEC). When a scanned document is indexed as a Means Test document, the image is automatically flagged for transmission to the HEC. After transmission, the associated patient’s record is updated to reflect that the Means Test form has been transmitted.

Section 2 – New Features

## Other Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Clinical Display Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The capability to display full resolution images has been added to the Radiology viewer. Full resolution images, when available, can be displayed by clicking the “Full Res” option in the Radiology Viewer’s menu bar.

## DICOM Gateway Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DICOM Gateway Enhancements include…

- Improved image acquisition from modalities that have embedded image icons, color overlays, and floating point VR (value representation).
- Improved the error reporting used when initiating new or updated dictionary files.
- Added an option to display the MSM license expiration date on the MUMPS Utilities sub-menu (part of the System Maintenance menu option).
- Corrected the handling of DICOM Unlimited Text (UT) value representation.
- The DICOM Viewer can now display the text file associated with DICOM images that have been captured. Images can also be browsed using a directory window.

## Background Processor Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Improved the interface used to define network locations.

> Section 2 – New Features

# Section 3 VistARad Diagnostic Radiology Workstation Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new VistARad diagnostic radiology reading software is used to retrieve and display full-resolution images and reports for radiology exams. VistARad is integrated with the V*IST*A Hospital Information System and with the Radiology Package in particular.

> VistARad is run on a dedicated Windows NT-based workstation that incorporates one, two, or four high- resolution monitors. A properly configured VistARad workstation is suitable for primary diagnostic interpretation of radiology exams.

> From the VistARad workstation, a radiologist can use a variety of exam lists to select the images to be displayed. Exam lists are based on information from the Radiology package and the V*IST*A patient database, and are used to divide the pool of available exams into useful categories. Core exam lists include the UnRead list, All Active (exams) list, and patient name-based lists.

> For any exam selected, both the images and the text report associated with the exam may be displayed. A radiologist can also view other parts of a patient's medical record, such as laboratory and pathology information, using the V*IST*A Health Summary reporting capability.

> VistARad provides a full range of image display and manipulation features, including: window/level adjustment, scale, sharpen, rotate/flip, etc. It can display multiple exams concurrently, allowing for comparisons with prior studies.

> Once a user has finished reviewing images, they can use the Close/Update Exams window to close exams and if appropriate, update the Exam Status from EXAMINED to INTERPRETED (specific values may vary from site to site).

## How VistARad Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistARad is composed of three interrelated components: the Manager, the Layout Viewer, and the Stack Viewer.

- The Manager is used to locate and select image and text data for display. It also serves as the link between VistARad and the V*IST*A patient database, updating the database when exams are locked or exam status is updated.
- The Layout Viewer is used for image display. Images belonging to each study are displayed side- by-side. It provides the tools used to manipulate and analyze images.
- The Stack Viewer can be used, at the user’s preference, to display CT, MR and XA

> (x-angiographic) exams. In addition to duplicating the standard tools incorporated by the Layout Viewer, the Stack Viewer provides specialized tools for creating image cines, series comparison, and navigation.

> The Manager, the Layout Viewer, and the Stack Viewer are described in more detail below.

> Section 3 – VistARad Diagnostic Radiology Workstation Software

## The Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Manager, five standard exam lists can be used to select images or reports for display. Additional custom lists can be defined on a site-by-site basis. Each type of list is described below.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 18%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Exam List</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Criteria</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Initial Sort</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">UnRead</td>
<td><blockquote>
<p>Exam status of</p>
</blockquote></td>
<td>Priority, then</td>
<td>Contains exams ready to be</td>
</tr>
<tr class="even">
<td>EXAMINED</td>
<td>Exam</td>
<td>interpreted.</td>
</tr>
<tr class="odd">
<td></td>
<td>Date/Time</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>Recent</p>
</blockquote></td>
<td><blockquote>
<p>Exam status of</p>
</blockquote></td>
<td>Exam</td>
<td rowspan="3">Does not include unread exams.</td>
</tr>
<tr class="odd">
<td>INTERPRETED or</td>
<td>Date/Time</td>
</tr>
<tr class="even">
<td>TRANSCRIBED</td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3">All Active</td>
<td>Exam status</td>
<td>Exam</td>
<td>Combines the Recent and UnRead</td>
</tr>
<tr class="even">
<td><p>of EXAMINED,</p>
<p>INTERPRETED, or</p></td>
<td>Date/Time</td>
<td>lists.</td>
</tr>
<tr class="odd">
<td>TRANSCRIBED.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4">Patient Exams</td>
<td>An abbreviated list of exams for a</td>
<td rowspan="4">Exam Date/Time</td>
<td>The list description may include a note that indicates if there are</td>
</tr>
<tr class="odd">
<td><p>selected patient.</p>
<p>Patient name</p></td>
<td><p>additional older exams for that</p>
<p>patient. Additional exams can be</p></td>
</tr>
<tr class="even">
<td><p>selected from</p>
<p>another exam list, or</p></td>
<td><p>opened from the All Patient Exams</p>
<p>list.</p></td>
</tr>
<tr class="odd">
<td>by using patient lookup.</td>
<td></td>
</tr>
<tr class="even">
<td>All Patient</td>
<td>Lists all exams for a</td>
<td>Exam</td>
<td>Lists all exams for a selected</td>
</tr>
<tr class="odd">
<td>Exams</td>
<td>selected patient.</td>
<td>Date/Time</td>
<td>patient.</td>
</tr>
<tr class="even">
<td>Custom lists</td>
<td>Site-defined</td>
<td>Site-defined</td>
<td>Typically, a site-defined subset of the UnRead list.</td>
</tr>
</tbody>
</table>

> The Manager uses exam locks to prevent multiple radiologists from simultaneously reading the same exam. An exam that has not yet been interpreted is locked when the exam has been opened by a radiologist. When an exam is locked, the reviewing radiologist’s initials are shown in the list entry for that exam, and any other users attempting to open the exam are notified that the exam is locked. Locked exams can be displayed, but only the user who “holds” the exam lock can update the exam’s status. A lock is removed if an un-interpreted exam is closed without updating its status.

> Whenever images or reports are displayed, the Manager checks the Radiology and Imaging database to confirm that the patient ID used in the patient record and the images match. If a mismatch is detected, the user is notified and given a description of the problem, and the display of images or reports is blocked. A special security key can be used by designated users to review “problem” images and reports.

> Section 3 – VistARad Diagnostic Radiology Workstation Software

## The Layout Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following image interpretation tools are available in the Layout Viewer.

> Image Manipulation Tools

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Window/Level</td>
<td>User can change window/level using mouse drag or controls in a floating dialog box.</td>
</tr>
<tr class="even">
<td>Scale</td>
<td>User can control image size by specifying an absolute percentage value, or by making the scale dependent on the current layout. Changes can be made using mouse drag or a floating dialog box.</td>
</tr>
<tr class="odd">
<td>Sharpen/Smooth</td>
<td>User can select one of multiple algorithms to enhance edges or to reduce image noise. Changes can be made using mouse drag or a floating dialog box.</td>
</tr>
<tr class="even">
<td>Invert Grayscale</td>
<td>User can invert (create a negative) image.</td>
</tr>
<tr class="odd">
<td>Pan</td>
<td>If image is larger than the space allotted to it by current layout settings, user can reveal hidden portions of the image using mouse drag or controls in a floating dialog box.</td>
</tr>
<tr class="even">
<td>Reorient</td>
<td><blockquote>
<p>User can rotate or flip images by 90° or 180° increments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ROI (magnifying glass)</td>
<td>User can define a movable, rectangular or elliptical area that can be manipulated independently from the rest of the image. May also be used as the basis of a mask, where areas outside the ROI are blacked out.</td>
</tr>
</tbody>
</table>

> Image Measurement Tools

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Angle tool</td>
<td>User can create two lines (lines do not have to be connected) to calculate acute or obtuse angles.</td>
</tr>
<tr class="even">
<td>Hounsfield Area tool</td>
<td>User can designate a rectangular area within a CT image to view Hounsfield unit average, range, and standard deviation.</td>
</tr>
<tr class="odd">
<td>Measure Line/Area tool</td>
<td>User can display measurement length or area for line or rectangle defined by dragging the mouse.</td>
</tr>
<tr class="even">
<td>Pixel Data tool</td>
<td>User can display grayscale, X-Y coordinate and Hounsfield values (CT images only) for pixel currently “under” mouse pointer.</td>
</tr>
</tbody>
</table>

> Image Annotation Tools

> Image annotation tools are available for Radiologists during reading, but are presently not saved. This functionality will be added in a future patch.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Text tool</td>
<td><blockquote>
<p>User can create a text box and label image features.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">Auto Number tool</td>
<td><blockquote>
<p>User can drag to create boxes that are automatically numbered using</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>numbering style of user’s choice. Available styles include, numeric,</td>
</tr>
<tr class="even">
<td>alphabetic, and spinal (cervical, thoracic, and lumbar).</td>
</tr>
<tr class="odd">
<td rowspan="2">Line/Arrow tool</td>
<td><blockquote>
<p>User can draw straight lines, single-headed pointers, or double-headed</p>
</blockquote></td>
</tr>
<tr class="even">
<td>pointers.</td>
</tr>
</tbody>
</table>

> Section 3 – VistARad Diagnostic Radiology Workstation Software

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">Ellipse tool</td>
<td><blockquote>
<p>User can draw a circle or ellipse—diameter and proportions are controlled</p>
</blockquote></td>
</tr>
<tr class="even">
<td>by dragging the mouse.</td>
</tr>
<tr class="odd">
<td rowspan="2">Rectangle tool</td>
<td>User can draw a rectangle—height and width are controlled by dragging</td>
</tr>
<tr class="even">
<td>the mouse.</td>
</tr>
</tbody>
</table>

> Case and Image Presets

> Case and image presets allow adjustments to be made to all images in an exam in a single step. They can control window/level, inversion, and sharpness. Case presets can also control scale, layout, and image-by-image or modality-based window/level settings. Case and image presets can be created, changed, and applied on demand. Additionally, case presets can be associated with a modality type, and then applied automatically when images acquired by a particular modality are displayed.

## The Stack Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A stack is a collection of cross-section images comprising part or all of an exam. The Stack Viewer window uses a grid format to display multiple exams at once. Each exam is displayed on a single row of the grid. Each scout image or series (stack) is displayed in a single cell of that row. Within a stack, only a single image is displayed at one time. A number of tools are available in the Stack Viewer Window to assist in interpreting studies.

> Stack Manipulation Tools

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cine</td>
<td>Creates a “flipbook” by displaying each image in a stack within a single cell. User can turn the function on or off, set direction, and define a subset of images within a series to view in this manner.</td>
</tr>
<tr class="even">
<td><p>Navigate through series</p>
<p>(in addition to cine)</p></td>
<td>User can use a variety of methods to display a particular image within a stack and determine that image’s relative position within a stack.</td>
</tr>
<tr class="odd">
<td>Link/Synchronize</td>
<td>Creates a link between two or more displayed stacks. After creating the link, cine or image manipulation functions applied to any one of the linked stacks will be applied to all linked stacks. User can choose which properties are linked and which are not.</td>
</tr>
<tr class="even">
<td>Copy Image Attribute</td>
<td>Allows user to propagate window/level, scale, sharpen/smooth, relative position (pan), or orientation from one stack to another.</td>
</tr>
<tr class="odd">
<td>Move Scout / Series</td>
<td><blockquote>
<p>Allows user to reposition stacks or scout images by dragging.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Split Stack</td>
<td><p>Allows user to divide an existing stack into two new stacks. Associations between the new stacks and the related scout image are retained.</p>
<p>Intended for use when series info is not available for displayed exam.</p></td>
</tr>
<tr class="odd">
<td>Change Layout</td>
<td><blockquote>
<p>User can change layout by dragging.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Image Presets</td>
<td>Image presets, which are defined in the Layout Viewer, can be applied to stacks. Image presets can control window/level, inversion, and sharpness.</td>
</tr>
</tbody>
</table>

> Section 3 – VistARad Diagnostic Radiology Workstation Software

> Image Manipulation Tools

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Window/Level</td>
<td>User can change window/level by dragging mouse.</td>
</tr>
<tr class="even">
<td>Scale</td>
<td>User can control image scale by dragging mouse.</td>
</tr>
<tr class="odd">
<td>Sharpen/Smooth</td>
<td>User can enhance edges or to reduce image noise by dragging mouse.</td>
</tr>
<tr class="even">
<td>Invert Grayscale</td>
<td>User can invert (create a negative) image.</td>
</tr>
<tr class="odd">
<td rowspan="2">Pan</td>
<td><blockquote>
<p>If image is larger than the space allotted to it by current layout settings,</p>
</blockquote></td>
</tr>
<tr class="even">
<td>user can reveal hidden portions of the image by dragging mouse.</td>
</tr>
<tr class="odd">
<td>Reorient</td>
<td><blockquote>
<p>User can rotate or flip images by 90° or 180° increments.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3">ROI (magnifying glass)</td>
<td>User can define a rectangular or elliptical, area that can be manipulated</td>
</tr>
<tr class="odd">
<td>independently from the rest of the image. May also be used as the basis</td>
</tr>
<tr class="even">
<td>of a mask, where areas outside the ROI are blacked out.</td>
</tr>
</tbody>
</table>

> Image Measurement Tools

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">Angle tool</td>
<td><blockquote>
<p>User can create two lines (lines do not have to be connected) to calculate</p>
</blockquote></td>
</tr>
<tr class="even">
<td>acute or obtuse angles.</td>
</tr>
<tr class="odd">
<td rowspan="3">Hounsfield Area tool</td>
<td>User can designate a rectangular area within a CT image to view</td>
</tr>
<tr class="even">
<td>Hounsfield unit average, range, and standard deviation. Dimensions are</td>
</tr>
<tr class="odd">
<td>measured as well.</td>
</tr>
<tr class="even">
<td rowspan="2">Measure Line tool</td>
<td>User can display measurement length for lines defined by dragging the</td>
</tr>
<tr class="odd">
<td>mouse.</td>
</tr>
</tbody>
</table>

## VistA HIS Menu Options for VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following menu options have been added to VistA Imaging to support VistARad. These options are used for configuration and maintenance, and are described in the VistA Imaging 3.0 Installation Guide.

> MAGJ MAIN

> MAGJ E/E VISTARAD LISTS MAGJ VISTARAD WINDOWS MAGJ LIST INQUIRY

> MAGJ VISTARAD SITE PARAMETERS MAGJ E/E PREFETCH LOGIC

> MAGJ PREFETCH PRINT

> MAGJ INQUIRE PREFETCH LOGIC MAGJ SCHED RECENT LIST COMPILE