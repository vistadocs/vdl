---
title: VistARad User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VistARad
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
description: This document explains how to use the VistARad diagnostic workstation. VistARad is part of the VistA (Veterans’ Hospital Information System Technology and Architecture) Imaging system.
audience: 
keywords: 
  - exam
  - hanging
  - image
  - exams
  - vistarad
  - table
  - viewport
  - contents
  - window
  - images
page_count: 0
word_count: 53588
section_count: 82
table_count: 14
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_VistARad_User_Guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_VistARad_User_Guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

![](vistarad-user-guide/001.png)

VistARad User Guide

March 2018

VistA Imaging System

Version 3.0 MAG\*3.0\*199

VistARad User Guide  
VistA Imaging 3.0 MAG\*3.0\*199  
March 2018Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Office of Enterprise Development Office.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Office of Enterprise Development  

Internet: <span class="mark">REDACTED</span>  
SharePoint: <span class="mark">REDACTED</span>

# RevisionHistory


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [RevisionHistory](#revisionhistory)
- [Contents](#contents)
- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [Conventions](#conventions)
  - [Related Information](#related-information)
  - [Getting Help](#getting-help)
- [VistARad Overview](#vistarad-overview)
  - [What is VistARad?](#what-is-vistarad)
    - [The Manager Window](#the-manager-window)
    - [The Preview Window](#the-preview-window)
    - [Diagnostic Review Windows: Viewer, Browser, & Scrapbook](#diagnostic-review-windows-viewer-browser-scrapbook)
    - [Viewports](#viewports)
  - [VistARad Basics](#vistarad-basics)
    - [Starting VistARad](#starting-vistarad)
    - [New VistARad User Setup](#new-vistarad-user-setup)
    - [Getting Around](#getting-around)
    - [Opening and Reviewing Exams](#opening-and-reviewing-exams)
    - [Exiting VistARad](#exiting-vistarad)
  - [Security & Timeouts](#security-timeouts)
- [Opening and Managing Exams](#opening-and-managing-exams)
  - [Exam List Basics](#exam-list-basics)
  - [Opening Exams](#opening-exams)
  - [Opening Exams with ReadList](#opening-exams-with-readlist)
    - [How ReadList Works](#how-readlist-works)
    - [Using ReadList](#using-readlist)
    - [Using Selection ReadList](#using-selection-readlist)
    - [Setting up Automatic Close/Updates](#setting-up-automatic-closeupdates)
  - [Other Ways to Open Exams](#other-ways-to-open-exams)
    - [Opening Exams without Priors](#opening-exams-without-priors)
    - [Opening Exams for a Specific Patient](#opening-exams-for-a-specific-patient)
    - [Opening Multiple Exams](#opening-multiple-exams)
    - [Opening Reference-Quality Exams](#opening-reference-quality-exams)
    - [Opening Previously Displayed Exams](#opening-previously-displayed-exams)
    - [Opening Printsets](#opening-printsets)
  - [Managing the Exam Load Process](#managing-the-exam-load-process)
    - [­Exam Load Management: Getting Started](#exam-load-management-getting-started)
    - [Exam Load Management: In Depth](#exam-load-management-in-depth)
  - [Exam List Reference](#exam-list-reference)
    - [Types of Exam Lists](#types-of-exam-lists)
    - [Fields in Exam Lists](#fields-in-exam-lists)
    - [Exam Lists and the VistA Host](#exam-lists-and-the-vista-host)
- [Patient Records](#patient-records)
  - [Opening Patient Records](#opening-patient-records)
    - [Displaying Requisitions](#displaying-requisitions)
    - [Displaying Reports](#displaying-reports)
    - [Displaying Patient Profiles](#displaying-patient-profiles)
    - [Displaying Health Summary Reports](#displaying-health-summary-reports)
  - [Using the Reports Window](#using-the-reports-window)
- [Context Management](#context-management)
  - [Context Management](#context-management-1)
  - [The Clinical Context Object Workgroup Protocol](#the-clinical-context-object-workgroup-protocol)
  - [The Context Management Settings Tab](#the-context-management-settings-tab)
  - [Context Changes](#context-changes)
  - [CPRS Tools Menu Option for VistARad](#cprs-tools-menu-option-for-vistarad)
- [VistARad and Voice Dictation](#vistarad-and-voice-dictation)
  - [About the VistARad Dictation Interface](#about-the-vistarad-dictation-interface)
  - [Multiple Locked Exams](#multiple-locked-exams)
    - [When Multiple Locked Exams for Different Patients are Open](#when-multiple-locked-exams-for-different-patients-are-open)
    - [Dictation Dialog Forced Under Certain Conditions](#dictation-dialog-forced-under-certain-conditions)
  - [Starting the Dictation Interface](#starting-the-dictation-interface)
  - [Opening Exams and Reports for Dictation](#opening-exams-and-reports-for-dictation)
  - [Working with the Dictation Interface](#working-with-the-dictation-interface)
- [Working with Open Exams](#working-with-open-exams)
  - [Surveying Exams](#surveying-exams)
    - [Loading Viewports](#loading-viewports)
    - [Using Conditional Indicator Icons](#using-conditional-indicator-icons)
    - [Navigating in Viewports](#navigating-in-viewports)
    - [Working with Images](#working-with-images)
    - [Key Images](#key-images)
    - [Clearing Viewports](#clearing-viewports)
    - [Switching between Patients](#switching-between-patients)
  - [Using the Preview Window](#using-the-preview-window)
    - [Thumbnails and List View Explained](#thumbnails-and-list-view-explained)
    - [Customizing Thumbnail Sizes](#customizing-thumbnail-sizes)
  - [Using the Viewer Window](#using-the-viewer-window)
    - [Using Stages](#using-stages)
    - [Wide Viewports](#wide-viewports)
    - [Hidden Exams and Image Sets in the Viewer](#hidden-exams-and-image-sets-in-the-viewer)
    - [Using the Re-Hang Feature](#using-the-re-hang-feature)
  - [Using the Browser Window](#using-the-browser-window)
  - [Using the Scrapbook Window](#using-the-scrapbook-window)
  - [Using Scout Images](#using-scout-images)
    - [Generating Scouts Manually](#generating-scouts-manually)
  - [Using the Image Detail Window](#using-the-image-detail-window)
  - [Using the Imaging Data Window](#using-the-imaging-data-window)
    - [Closing Exams & Updating Exam Status](#closing-exams-updating-exam-status)
- [Manipulating Images](#manipulating-images)
  - [Changing Image Properties](#changing-image-properties)
    - [Scaling Images](#scaling-images)
    - [Panning images](#panning-images)
    - [Changing Window/Level](#changing-windowlevel)
    - [Inverting Grayscale Values](#inverting-grayscale-values)
    - [Reorienting Images](#reorienting-images)
    - [Using Sharpen/Smooth](#using-sharpensmooth)
    - [Resetting Images](#resetting-images)
  - [Using Image Presets](#using-image-presets)
  - [Changing Layout](#changing-layout)
  - [Using “Apply To”](#using-apply-to)
  - [Copying Properties](#copying-properties)
  - [Linking Viewports](#linking-viewports)
  - [Cloning Image Sets](#cloning-image-sets)
  - [Moving and Splitting Image Sets](#moving-and-splitting-image-sets)
  - [Sorting Image Sets](#sorting-image-sets)
  - [Using the Cine Tool](#using-the-cine-tool)
  - [Using the Magnifying Glass](#using-the-magnifying-glass)
  - [Mensurated Scale](#mensurated-scale)
- [Annotations](#annotations)
  - [Annotation Basics](#annotation-basics)
  - [Adding Shapes and Labels](#adding-shapes-and-labels)
  - [Adding Measurements](#adding-measurements)
  - [Using the Hounsfield Tool](#using-the-hounsfield-tool)
  - [Working with Annotations](#working-with-annotations)
  - [Using Show/Hide](#using-showhide)
  - [Using Calibrate](#using-calibrate)
  - [Setting Annotation Properties](#setting-annotation-properties)
  - [Saving Annotations](#saving-annotations)
  - [Overriding Annotations in Interpreted Exams](#overriding-annotations-in-interpreted-exams)
  - [Annotation Options in the Close Exams / Update Status Dialog](#annotation-options-in-the-close-exams-update-status-dialog)
- [VistARad and Voxar 3D](#vistarad-and-voxar-3d)
  - [Overview](#overview)
  - [Loading Images from VistARad into Voxar](#loading-images-from-vistarad-into-voxar)
  - [Voxar Features Linked to Security Keys](#voxar-features-linked-to-security-keys)
  - [Saving a Voxar Capture to VistA](#saving-a-voxar-capture-to-vista)
- [VistARad Settings](#vistarad-settings)
  - [Customizing the Work Area](#customizing-the-work-area)
    - [Setting the Size of the Viewer Window](#setting-the-size-of-the-viewer-window)
    - [Resizing Controls in the Viewer (and in other Windows)](#resizing-controls-in-the-viewer-and-in-other-windows)
    - [Working with Exam List Tabs](#working-with-exam-list-tabs)
    - [Changing Fonts in the Manager](#changing-fonts-in-the-manager)
    - [Using Pushpins](#using-pushpins)
  - [The VistARad Settings Dialog](#the-vistarad-settings-dialog)
- [Using VistARad for Teleradiology](#using-vistarad-for-teleradiology)
  - [VistARad and Routing](#vistarad-and-routing)
  - [Using On-Demand Routing](#using-on-demand-routing)
  - [Routed Exams and Remote Reading](#routed-exams-and-remote-reading)
    - [One-click Login to a Monitored Site](#one-click-login-to-a-monitored-site)
    - [Dictation and Remote Reading](#dictation-and-remote-reading)
- [Using Templates](#using-templates)
  - [Template Basics](#template-basics)
  - [Selecting and Applying Templates](#selecting-and-applying-templates)
    - [Opening an Exam with a Template Only](#opening-an-exam-with-a-template-only)
    - [Applying a Different Template to an Open Exam](#applying-a-different-template-to-an-open-exam)
  - [Working with Templates](#working-with-templates)
    - [Creating Templates](#creating-templates)
    - [Editing Templates](#editing-templates)
    - [Using the Template Designer](#using-the-template-designer)
    - [Deleting Templates](#deleting-templates)
  - [Working with Screen Templates](#working-with-screen-templates)
- [Using Hanging Protocols](#using-hanging-protocols)
  - [Hanging Protocols Explained](#hanging-protocols-explained)
  - [Selecting a Hanging Protocol](#selecting-a-hanging-protocol)
    - [Manual Hanging Protocol Selection](#manual-hanging-protocol-selection)
    - [Automatic Hanging Protocol Selection](#automatic-hanging-protocol-selection)
    - [Resolving Multiple Matches](#resolving-multiple-matches)
  - [Creating Hanging Protocols](#creating-hanging-protocols)
    - [Designing a Hanging Protocol](#designing-a-hanging-protocol)
    - [Modeling a Hanging Protocol](#modeling-a-hanging-protocol)
    - [Implementing a Hanging Protocol](#implementing-a-hanging-protocol)
  - [Working with Hanging Protocols](#working-with-hanging-protocols)
    - [Using Default Hanging Protocols](#using-default-hanging-protocols)
    - [Expanding the Scope of Hanging Protocols](#expanding-the-scope-of-hanging-protocols)
    - [Editing Hanging Protocols](#editing-hanging-protocols)
    - [Copying Hanging Protocols](#copying-hanging-protocols)
    - [Deleting Hanging Protocols](#deleting-hanging-protocols)
- [Hanging Protocol Reference](#hanging-protocol-reference)
  - [The Hanging Protocol Definition Dialog](#the-hanging-protocol-definition-dialog)
    - [Common Features](#common-features)
    - [Case Info \| HP Lookup Area (for Current Exams)](#case-info-hp-lookup-area-for-current-exams)
    - [Case Info \| Prior Attribute Area](#case-info-prior-attribute-area)
    - [Case Info \| Attribute Area (for Other Related Cases)](#case-info-attribute-area-for-other-related-cases)
    - [Case Info \| Oldest Shown... Check Box](#case-info-oldest-shown-check-box)
    - [Case Info \| Local/Remote Options](#case-info-localremote-options)
    - [Case Info \| Use this Stage... Check Box](#case-info-use-this-stage-check-box)
    - [Case Info \| Disable Series Processing Check Box](#case-info-disable-series-processing-check-box)
    - [Case Info \| Regroup Leftover Image Sets check box](#case-info-regroup-leftover-image-sets-check-box)
    - [Viewport Info \| Clone/Placeholder Options](#viewport-info-cloneplaceholder-options)
    - [Viewport Info \| Specify Attributes List](#viewport-info-specify-attributes-list)
    - [Viewport Info \| Pixel Processing Area](#viewport-info-pixel-processing-area)
    - [More Viewport Info Tab](#more-viewport-info-tab)
  - [Viewport Mapping Explained](#viewport-mapping-explained)
  - [Hanging Protocol Cookbook](#hanging-protocol-cookbook)
    - [A Basic Hanging Protocol for Chest X-Rays](#a-basic-hanging-protocol-for-chest-x-rays)
    - [A Staged Hanging Protocol for “With Prior” and “Without Prior” Views](#a-staged-hanging-protocol-for-with-prior-and-without-prior-views)
    - [An MR Hanging Protocol that uses Links and Explicit Mapping](#an-mr-hanging-protocol-that-uses-links-and-explicit-mapping)
    - [An MR Hanging Protocol that Splits a Series](#an-mr-hanging-protocol-that-splits-a-series)
  - [Internal Hanging Protocols](#internal-hanging-protocols)
    - [Baseline Hanging Protocols](#baseline-hanging-protocols)
    - [1-head Hanging Protocols](#1-head-hanging-protocols)
    - [2-head Hanging Protocols](#2-head-hanging-protocols)
    - [4-head Hanging Protocols](#4-head-hanging-protocols)
- [Teaching Files](#teaching-files)
  - [Enable Teaching Files in VistARad](#enable-teaching-files-in-vistarad)
  - [Make a Teaching File Out of an Image, Image Set or Exam](#make-a-teaching-file-out-of-an-image-image-set-or-exam)
  - [Redact Sensitive Information From a Teaching File](#redact-sensitive-information-from-a-teaching-file)
  - [Send a Teaching File to MIRC](#send-a-teaching-file-to-mirc)
- [Glossary](#glossary)
- [Index](#index)
| Rev | Date      | Patch | Notes                                                                                                                                                                                                                                                                                            |
|---------|---------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13      | Mar 7, 2018   | 3.0\*199  | In support of MAG\*3.0\*199, increased the timeout value during the monitored sites login.                                                                                                                                                                                                           |
| 12      | May 16, 2017  | 3.0\*184  | In support of MAG\*3.0\*184, the 2FA sign on PIV PIN instructions replaced the access/verify instructions for sign on.                                                                                                                                                                               |
| 11      | April 7, 2016 | 3.0\*153  | Removed references to the Ellipse option on page 95, Using the Hounsfield Tool, and from the index on page 208.                                                                                                                                                                                      |
| 10      | Aug 22, 2013  | 3.0\*133  | Added alt. text to make PDF 508-compliant. <span class="mark">REDACTED</span>                                                                                                                                                                                                                        |
| 9       | Aug 6, 2013   | 3.0\*133  | Preview window re-organization; preview thumbnail size user preference; reset VistARad windows function. <span class="mark">REDACTED</span>                                                                                                                                                          |
| 8       | June 4 2012   | 3.0\*120  | Updated to reflect MAG\*3.0\*120. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                 |
| 7       | Feb 08 2011   | 3.0\*115  | Updated to reflect Patch 115. Added content describing user preference management, splitting stacks, conditional indicator icons, VOI LUT alert, scout line modification, toolbar icon modification, and teaching file modification. <span class="mark">REDACTED</span>                              |
| 6       | Jul 06 2010   | 3.0\*90   | Updated to reflect Patch 90. Added content describing mensurated scale, remote viewing, and monitored sites. <span class="mark">REDACTED</span>                                                                                                                                                      |
| 5       | Mar 31 2010   | 3.0\*101  | Corrected packaging issue with links and graphics; no content change. <span class="mark">REDACTED</span>                                                                                                                                                                                             |
| 4       | Jan 06 2010   | 3.0\*101  | Updated to reflect Patch 101. Updated sections on Annotations and added sections on Managing the Exam Load Process and Teaching Files. <span class="mark">REDACTED</span>                                                                                                                            |
| 3       | Dec 03 2007   | 3.0\*76   | Updated to reflect Patch 76. Added new chapter covering use of integrated Voxar software. Added references to keyboard shortcuts and revised information about exam list date/time column for Patch 76. Miscellaneous typo fixes and wording changes for clarity. <span class="mark">REDACTED</span> |
| 2.0     | Feb 21 2007   | 3.0\*65   | Full rewrite; covers Patches 18 and 65. All content updated. <span class="mark">REDACTED</span>                                                                                                                                                                                                      |
| 1.4     | Apr 28 2004   | 3.0\*32   | Relocation of revision table. Updates for monitor and OS support on pages 1 and 85. <span class="mark">REDACTED</span>                                                                                                                                                                               |
| 1.3     | Sep 26 2003   | 3.0\*22   | Updated to reflect p22. Added on demand routing information. Reorganized “Opening Exams” chapter. <span class="mark">REDACTED</span>                                                                                                                                                                 |
| 1.2c    | Apr 2 2003    | 3.0\*23   | Checked content against p23. No updates needed. <span class="mark">REDACTED</span>                                                                                                                                                                                                                   |
| 1.2b    | Oct 21 2002   | 3.0\*16   | Corrected “Getting Help” section. <span class="mark">REDACTED</span>.                                                                                                                                                                                                                                |
| 1.2a    | Oct 7 2002    | 3.0\*16   | Updated with results of Patch 16 WPR. Updated Quick Reference card. Revised workflow diagrams in App A. <span class="mark">REDACTED</span>                                                                                                                                                           |
| 1.1     | May 13 2002   | 3.0\*6    | Updated to reflect Patch 6. Added Appendix C (quick reference). <span class="mark">REDACTED</span>                                                                                                                                                                                                   |
| 1.0     | Mar 20 2002   | 3.0       | Updated from alpha to release s/w. Added shortcut appx. Reworked Stack Viewer information to reflect changes and fixes. Incorporated Work Product Review edits. <span class="mark">REDACTED</span>                                                                                                   |
| .9b     | Feb 4 2002    | N/A       | Updated index to include Stack Viewer. <span class="mark">REDACTED</span>                                                                                                                                                                                                                            |
| .9a     | Jan 22 2002   | N/A       | Draft for Alpha test sites. Incorporates information on latest changes and addition of Stack Viewer. <span class="mark">REDACTED</span>                                                                                                                                                              |
| .9      | Nov 15 2001   | N/A       | Draft. Content subject to change pending review against distribution s/w build. <span class="mark">REDACTED</span>                                                                                                                                                                                   |

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This page intentionally left blank.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document explains how to use the VistARad diagnostic workstation. VistARad is part of the VistA (Veterans’ Hospital Information System Technology and Architecture) Imaging system.

This document is intended for radiologists and clinicians. It assumes that the user is familiar with the Microsoft Windows environment, and that a current version of VistARad is installed.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of the VistARad diagnostic workstation is subject to the following provisions:

| ![](vistarad-user-guide/002.png) | Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistarad-user-guide/003.png) | No modifications may be made to this software without the express written consent of the VistA Imaging National Project Manager.                                                                                                                                                                                                                                                                                                                                                      |
| ![](vistarad-user-guide/004.png) | The Food and Drug Administration classifies the VistARad software as a medical device. Modifications to the VistARad diagnostic workstation, such as the installation of unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).                                                                                                                                                                        |
| ![](vistarad-user-guide/005.png) | Image presentation quality depends on monitor resolution, and on regular monitor testing and calibration to correct for display degradation over time. It is the responsibility of the clinical practitioner to determine if images presented on a VistARad workstation are of sufficient quality for clinical interpretation. Any concerns regarding monitor resolution or calibration should be reported immediately to the Imaging Coordinator before interpretation is performed. |

## Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses the following conventions:

Change bars in margins indicate content added or updated since the last revision.

Controls, options, and button names are shown in Bold.

A vertical bar is used to separate menu choices. For example: “Click File \| Open” means “Click the File menu, and then click the Open option.”

Keyboard key names are shown in Bold and in brackets.

Sample output is shown in monospace.

When this document is used online, hyperlinks are indicated by blue text.

Useful or supplementary information is shown in a Tip.

![](vistarad-user-guide/006.png)Important or required information is shown in a Note.

Critical information is indicated by:

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad-related documentation can be accessed from the VistARad application by choosing File \| Help.

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# VistARad Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

What is VistARad?

VistARad Basics

Security & Timeouts

## What is VistARad?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad is a software application used for primary interpretation of digital images acquired by CR, CT, MR, and other modalities. VistARad lets you display any radiology exam stored in the VistA System at your site, and also lets you access text-based reports. VistARad can interface with commercial voice dictation and 3D reconstruction applications, and can be used to send “teaching file” images to a Medical Imaging Resource Center (MIRC) server.

VistARad can also be used for tele radiology. Copies of exams can be automatically routed to remote VistARad workstations for interpretation. Exams can also be pushed or pulled to a VistARad workstation on demand. VistARad can be used to access patient data at remote sites, including data from DoD sites. VistARad is installed on a Windows XP workstation, typically having one, two, or four diagnostic-quality monitors. An additional color monitor for the Manager window and for color images can also be used.

The functions of VistARad are divided among the Manager window, the Preview window, and windows used for diagnostic review.

### The Manager Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manager is used to locate and open the exams you want to review.

![](vistarad-user-guide/007.png)

### The Preview Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preview window provides a summary view of exams opened using the Manager, and of the system memory in use and available to VistARad. In List View mode, it allows user control over image loading operations.

![](vistarad-user-guide/008.png)

### Diagnostic Review Windows: Viewer, Browser, & Scrapbook

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer window is the primary window used for diagnostic review, and is designed to occupy one or more screens. (Because of its size, a sample of the Viewer window cannot be included in this document.)

The Browser window can also be used for diagnostic review, and it is designed for ad-hoc exam display. The following image shows the Browser window.

![](vistarad-user-guide/009.png)

You can also use the Scrapbook window to review and work with key images (details on page [66](#_Ref136741120)).

### Viewports 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer, Browser and other image-related windows use one or more *viewports* for image display. A viewport can contain a single image, a group of related images, or an entire exam.

All images in a general radiology (CR or DX) and ultrasound exam are usually displayed in a single viewport.

Images in CT or MR exams are usually divided among several viewports: one viewport per series (or sequence), and optionally one viewport for scout (localizer) images.

Images in a viewport can be adjusted independently from images in other viewports. Within a viewport, all images can be adjusted at once, or single images can be adjusted independently.

Viewports can display one image at a time (stacked view) or several images at once (tiled view). Users can switch between views without having to reload an exam.

![](vistarad-user-guide/010.png)

Each viewport contains several informational elements used to place images in their proper context in an exam.

![](vistarad-user-guide/011.png)

The Title bar

The viewport Title bar displays the case ID, status and date of the exam. The Title bar may also display other information such as the series ID.

The following status code abbreviations are used in the Title bar:

W– Waiting (acquisition or case edit/QC not completed)  
E– Examined (awaiting interpretation)  
I– Interpreted (awaiting verification)  
C– Complete

If there is not enough space to display all the text in the Title bar, you can point and hover over the title bar to make it expand to display all its contents.

The Contents bar

The Contents bar is located in the upper right corner of a viewport. It displays the number of exams, image sets (series) and images in the viewport. You can click the Ex or S labels in the Contents bar to view any hidden exams or image sets that are present.

Tick marks

In viewports that contain multiple images, the relative position of the selected image in the stack is indicated by tick marks on the left side of the viewport. The I label in the upper right corner can also indicate the position of an image in the stack.

The Image Information Area

The information area at the bottom of a viewport displays such details about the selected image as image number, acquisition date/time, the image’s current display properties (window/level, scale, etc.) and other acquisition data.

If there is not enough space to display all image information, you can point to and hover over the area with the mouse to make it expand to display all its contents.

Clicking in the information area will open the Image Detail window (details on page [69](#_Ref137003245)).

Auxiliary windows

VistARad uses several other supporting windows. Listed here for orientation, they are described fully in the User Guide chapter indicated.

| Title               | Description                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reports                 | Displays case-specific report, requisition, and history information. See the Patient Records chapter for more information.                                                                                              |
| Imaging Data Display    | Displays image-specific data from the IMAGE File (#2005), along with Matching CPT Codes. See the Working with Open Exams chapter for more information.                                                                  |
| Teaching Files          | Collects descriptive information about an image being shared to a MIRC server. See the Teaching Files chapter for more information.                                                                                     |
| Select Hanging Protocol | Allows selection of a Hanging Protocol or Template, displaying its description and a preview of its layout. See the Using Templates chapter, and the two Hanging Protocols chapters following it, for more information. |

## VistARad Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Starting VistARad 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Login steps can vary, depending on whether you are logging in to a standard site or a consolidated/multi-divisional site.

1\. If VistARad is interfaced to a voice dictation system, log in to that system before starting VistARad.

2\. On the Windows desktop, double-click the VistARad shortcut, or click Start \| Programs \| VistA Imaging Programs \| MAG_VistARad_Patch184.

3\. If the Connect to dialog displays, click the down arrow, then click an option to select which VistA system you want to connect to. Then click OK.

4\. Make sure you have a valid PIV card attached to the computer. You will be prompted to select a certificate. Then click on the OK button.

![](vistarad-user-guide/012.png)

5\. Next, you will be prompted to enter your PIN. Enter your PIN and click on the OK button.

![](vistarad-user-guide/013.png)

6\. Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate two-factor authentication (2FA), the application will revert the user to the Access/Verify screen. If the VistA Sign-on box displays, type your access and verify codes in the Access Code and Verify Code boxes, then click OK.

![](vistarad-user-guide/014.png)

7\. If the Select Division dialog displays, double-click the division that you will be interpreting exams for. Press the \<Enter\> key or click OK.

### New VistARad User Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a new VistARad user first signs on, the Copy User Profile dialog appears automatically. This dialog lists existing user profiles, by user, for active users. If a system administrator has assigned default profiles for radiologist or non-radiologist user types, they will appear at the top of the Copy User Profile dialog’s profile list.

This facilitates granting new users a known working configuration specific to the environment.

It does not list the profile(s) of: 1) the current user, 2) terminated users, or 3) users suspended with the DISUSER flag.

VistARad will prompt to be re-started after new user setup.

NOTE The Copy User Profile dialog is accessible to existing users from the Manager via File \| Import User Profile. This allows on-demand re-configuration to the settings of another user.

### Getting Around

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can switch from one window to another using the toolbar displayed in the Viewer, Browser, and Scrapbook windows.

To switch between windows

In any window that displays the toolbar, click one of the following:

Click ![](vistarad-user-guide/015.png) to display the Manager.

Click ![](vistarad-user-guide/016.png) to display the Preview window and the Browser window (the Browser window will display only if it contains images).

Click ![](vistarad-user-guide/017.png) to display the Scrapbook.

Click ![](vistarad-user-guide/018.png) to display the Scout Image window.

Tip You can also switch from one window to another by pressing \<Ctrl+W\> to open a list of VistARad windows, or by using the taskbar at the bottom of your primary monitor (usually, this is the leftmost high-resolution monitor).

Tip If a window you want hidden remains visible, click ![](vistarad-user-guide/019.png) to hide the window, or click ![](vistarad-user-guide/020.png) to change the pushpin button (details on page [111](#_Ref136742852)).

Tip On very rare occasions on workstations with multiple different-sized screens, VistARad may “lose” one of its windows (Manager, Preview, Browser, Scrapbook, or Scout) so that it is not viewable on any of the screens. Should this occur, the window may be retrieved by the following method: on the main viewer’s menu, select Customize \| Reset VistARad Windows; after clicking OK to the warning message that appears, the various windows will all be re-located to the primary screen. Drag each of them to your preferred screen location, and re-size as desired.

### Opening and Reviewing Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the ‘bare minimum’ steps needed to use VistARad to interpret an exam.

To open and review an exam

If VistARad’s voice dictation interface is enabled, log in to the dictation software you are using.

Start VistARad by double-clicking the VistARad icon on your desktop and entering your PIV PIN.

Tip If the Manager window is not visible, click ![](vistarad-user-guide/021.png), located in the toolbar at the top of the Viewer window.

If the Unread Exams list is not displayed in the Manager window at startup, click the Unread Exams tab located near the top of the window. In the Unread Exams list, double-click the exam you want to open (see page [114](#manager_tab_general) for further details).

If VistARad is interfaced to a voice dictation system, you will be asked if you want to open the report for the exam you are dictating. To proceed, click the Yes/No value under Dictate? as desired, then press \<Enter\> or click OK.

If the Preview window opens automatically, check each thumbnail image in the window.

An ![](vistarad-user-guide/022.png) icon indicates that the images represented by the thumbnail are loaded and visible in the Viewer window.

An ![](vistarad-user-guide/023.png) icon indicates that the images represented by the thumbnail are loaded into the Viewer as hidden image sets (details on page [64](#hidden-exams-and-image-sets-in-the-viewer)).

A ![](vistarad-user-guide/024.png) icon indicates that the image set is only partially loaded.

If there is no icon next to a thumbnail image, you can drag the thumbnail into an empty area (viewport) in the Viewer window to view the associated images.

In the Viewer, point to each group of images and roll the mouse scroll wheels to view each image in the group.

As you review images, you can:

Right-drag over an image to change window/level.

CTRL+right-drag over an image to change scale.

Click ![](vistarad-user-guide/025.png) in a viewport to mark a selected image as a key image.

When you are ready to close the exam, click ![](vistarad-user-guide/026.png) in the toolbar near the top of the Viewer window.

In the dialog that displays, locate the column labeled Interpret? In the row that lists the current exam, click the Yes/No value to set it as desired.

| ![](vistarad-user-guide/027.png) | Setting Interpret? To Yes indicates that you want to update the status of this exam to “Interpreted,” and that you have dictated the exam or entered your findings in your site’s reporting package. |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Click OK.

If you updated the exam’s status, the exam you just closed is removed from the Unread Exams list.

The next exam in the Unread Exams list is automatically selected. You can immediately open this exam by pressing \<Enter\>.

Tip ReadList can be used to quickly open successive exams and reduce wait times (details on page [18](#opening-exams-with-readlist)).

### Exiting VistARad 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit VistARad, go to the main menu in the Manager or the Viewer and click File \|Exit.

If exams are opened, you will be prompted to close the exams before exiting the software (details on page [71](#_Ref257049904)).

If you are using VistARad with a voice dictation system, you will need to log out of the voice dictation system as well.

## Security & Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use VistARad, you must have a VA PIV card and PIN and you must have the MAGJ VISTARAD WINDOWS menu option assigned to your entry in the NEW PERSON File (#200).

To lock and interpret exams using VistARad, you must be defined as staff or as a resident in the Radiology package.

If a VistARad workstation is left idle for more than a site-specified period, a 60-second warning message will display. If there is no response to the message, VistARad will unlock any locked exams (leaving them unread) and close all open exams. Then VistARad will exit automatically.

# Opening and Managing Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Exam List Basics

Opening Exams

Opening Exams with ReadList

Other Ways to Open Exams

Managing the Exam Load Process

Exam List Reference

## Exam List Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam lists can be used to quickly locate and select an exam. Exam lists can be sorted and refreshed as needed.

Locating and selecting exams

Exam lists are displayed as tabs near the top of the Manager window. The name of each tab indicates the type of exams the list contains.

![](vistarad-user-guide/028.png)

To select an exam list and display its contents, click the appropriate tab.

The first exam in an exam list is always selected automatically.

Other exams can be selected by clicking them with the mouse. You can quickly open any selected exam by double-clicking the exam or by pressing \<Enter\>.

The Patient Exams tab and the Custom tab contain subtabs for specific patients and specific custom lists.

![](vistarad-user-guide/029.png)

Sorting exam lists

Most exam lists are automatically sorted by exam date and by priority. You can change the sorting used in an exam list by clicking any column header in the list.

![](vistarad-user-guide/030.png)

If you have changed how a list is sorted, an arrow icon displays in the column heading that was used to sort the list. The direction of the arrow indicates if the sort is ascending or descending.

Exam lists are frequently refreshed to keep their contents current. If you want the sorting you are using to be retained after the exam list is refreshed, right-click an exam list column heading and choose Preserve Sort Order.

The sort order will be retained until the end of the session, or until you explicitly resort the list.

To return to the default sort order, right-click the column heading and choose Restore Sort.

Refreshing exam lists

Exam lists are refreshed each time an exam list tab is selected and each time an exam is closed. Exam lists are refreshed to ensure that they contain all available exams, and to reflect any recent changes that have been made in exam status.

If VistARad has been idle for a period of time, or if there are display problems with an exam list, you can click the Refresh Exams button located near the top of the Manager window to manually refresh the exam lists.

Note that pre-compiling the unread list means that refresh operations involving unread exams will only be as current as the most recent compile event. See the section titled “Pre-compiled vs. on-demand lists,” below.

The exam list shortcut menu

Right-clicking an exam in the exam list will display a shortcut menu with options that duplicate many of the buttons located under the exam list.

Exam lists from remote sites

If the patient has been treated at other VA or DoD sites, VistARad displays the names of the relevant remote sites on buttons within the Patient Exams tab. To retrieve data, click on the button for the site. This accomplishes the following:

- Initiates a connection to the remote site. If the site is unavailable, the name in its button will be displayed with a strikeout line through it.
- Loads remote exam information into the exam list.
- Updates the label of the button with the number of exams at that site, displayed to the right of its name in square brackets.

![](vistarad-user-guide/031.png)

Note DoD studies from one or more DoD facilities are consolidated under a single DOD tab, and can be distinguished by a Day/Case column entry starting with “DOD. ”

Click “Connect All” to automate the steps above for all available sites. The exam list will be refreshed as the exam list data from each site becomes available. Wait for the data from all remote sites to load before working with the consolidated exam list.

The remote exams listed in the Patient Exams list provide access to the respective reports and images by highlighting the entry of interest and accessing in the usual manner. Note that no exams can be accessed for locking and interpretation using this feature.

## Opening Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps below explain how to open a single exam using an automatically selected hanging protocol.

Note If VistARad is interfaced to a voice dictation system, close the report you are dictating before you open any additional exams.

To open an exam

Click ![](vistarad-user-guide/032.png) in the toolbar to display the Manager.

Click one of the exam list tabs located near the top of the Manager window.

Do any one of the following:

Click an exam, then click Open.

Click the exam, then press \<Enter\>.

Double-click the exam.

Right-click the exam, then click Open.

Note that:

The Preview window will display icons that show which groups of images are loaded into viewports (details on page [55](#loading-viewports)).

If more than one matching hanging protocol is found for the exam being opened, you will be asked to select which hanging protocol you want to use. For details, see Resolving Multiple Matches on page [140](#resolving-multiple-matches).

Depending on the hanging protocol being used, one or more prior exams may open automatically.

If you are using an integrated voice dictation system, you will be asked if you want to open the exam’s report for dictation (details on page [51](#opening-exams-and-reports-for-dictation)).

You can begin working with the exam as soon as the first images are displayed. For details, see Surveying Exams on page [55](#_Ref136316510).

| ![](vistarad-user-guide/033.png) | If a Severe Alert! message is displayed, VistARad has detected a data integrity problem with the exam. Contact your Imaging Coordinator immediately. |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|

## Opening Exams with ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How ReadList Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ReadList lets you work through all the unread exams in an exam list without having to open each exam manually. ReadList will reduce the amount of time you need to wait for images in an exam to load.

When you start ReadList, the unread exams in the current exam list are processed in the order of their appearance. While you are reviewing images in the first exam, the next lockable exam is preloaded into memory. When you close the first exam, the next exam is opened and displayed automatically.

Each time a new exam is opened, the current exam list is refreshed, and the first lockable exam from the top of the list is opened. This progression continues until all unread exams have been displayed.

ReadList stops automatically after all unread exams have been displayed. ReadList can also be stopped manually.

### Using ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to start ReadList, how to step through exams when ReadList is active, and how to stop ReadList.

To start ReadList

In the Manager, display an exam list that contains unread exams.

Click the ReadList button, located near the middle of the Manager window.

The first exam to be interpreted is displayed in the Viewer. One or more prior exams may be displayed as well.

The “first” exam is the first unread and lockable exam in the exam list you selected.

As you are reviewing the displayed exam, the next unread exam is reserved and loaded into memory. Any exam that is interpreted or locked is skipped.

If more than one matching hanging protocol is found for the exam being opened, you will be asked to select which hanging protocol you want to use. For details, see Resolving Multiple Matches on page [140](#resolving-multiple-matches).

If you are using an integrated voice dictation system, you will be asked if you want to open the exam’s report for dictation (details on page [51](#opening-exams-and-reports-for-dictation)).

When the exam is fully opened, you can begin reviewing images. For details, see Surveying Exams on page.[55](#_Ref136316510).

To close the current exam and step to the next exam

If VistARad is interfaced to a voice dictation system, and if you are dictating reports, save and close your current report.

In VistARad, click ![](vistarad-user-guide/034.png) in the Viewer toolbar or click Next in the Manager window. You can also press \<Ctrl+ N\>.

If the Close Exams/Update Status dialog opens, set the values of Close?,Interpret?, and Annotations (if applicable), then click OK (details on page [69](#using-the-imaging-data-window)).

Note If the Close Exams/Update Status dialog does not open, automatic close/updates have been enabled (details on page [21](#autoupdate_setup)).

After the current exam is closed, the next exam in the ReadList sequence will be displayed automatically.

Tip Each exam closed while ReadList is active will not be displayed again in the current ReadList session. However, these exams can always be opened manually or can be reopened by stopping and restarting ReadList.

To stop ReadList

ReadList will stop automatically when all unread exams in an exam list have been reviewed. You can also stop ReadList manually by clicking the Stop RL button located near the middle of the Manager window. (This button is visible only when ReadList is active.)

When ReadList is stopped manually, the currently displayed exam will remain open, but no additional exams will be opened after the displayed exam is closed.

### Using Selection ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selection ReadList is a variation of the ReadList feature that lets you work through a set of exams you select, rather than an entire exam list.

To start Selection ReadList

In the Manager, display an exam list that contains unread exams.

Select the exams you want to open.

You can click a column heading in an exam list to group exams with similar properties.

You can use \<SHIFT\>-click to select exams that are listed continuously, or \<Ctrl\>-click to select exams that are not listed continuously.

Click Selection RL (this button replaces the ReadList button whenever multiple exams are selected).

If any of the exams you selected are already locked, you will be asked if you want to open a review-only copy of the exam, or if you want to skip that exam.

If more than one matching hanging protocol is found for the exam being opened, you will be asked to select which hanging protocol you want to use. For details, see Resolving Multiple Matches on page [140](#resolving-multiple-matches).

Review the contents of the new Selection ReadList tab that is displayed. Before proceeding, you can:

Use the Clear button to remove any unwanted exams from the list.

Sort the list to indicate the order in which exams should be displayed.

Click the ReadList button to begin. The first exam in the list will be displayed. All other exams in the list will be reserved.

Depending on the hanging protocol being used, one or more prior exams may open automatically.

If you are using an integrated voice dictation system, you will be asked if you want to open the exam’s report for dictation (details on page [51](#opening-exams-and-reports-for-dictation)).

Once Selection ReadList is active, you can view successive exams the same way as “standard” ReadList is used.

### Setting up Automatic Close/Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an exam is closed, the Close Exams/Update Status dialog is usually displayed as an intervening step. If you are using ReadList, you can suppress the display of this dialog and close exams with a single mouse click.

To set up automatic close/updates

If you want the status of exams being closed to be automatically updated to Interpreted:

In the Viewer or Manager window, click View \| Settings, then the Manager tab.

Clear the Set the Default Status Update Prompt to NO check box.

Note Clearing this check box sets the initial value of the Interpret? field in the Close Exams/Update Status dialog to YES. This setting applies whether or not ReadList is active.

Click OK.

Open any exam or start ReadList mode.

Open the Close Exams/Update Status dialog by clicking Next in the Manager, or by clicking the ![](vistarad-user-guide/035.png) button.

Clear the Show this dialog in ReadList mode check box.

This setting is not retained across VistARad sessions.

The Close Exams/Update Status dialog can always be opened by clicking ![](vistarad-user-guide/036.png), regardless of this setting.

Set other values in the dialog as appropriate for the current exam, then click OK.

## Other Ways to Open Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An exam is usually opened by double-clicking its entry in an exam list or by using ReadList. Other ways to open an exam include:

Opening Exams without Priors

Opening Exams for a Specific Patient

Opening Multiple Exams

Opening Reference-Quality Exams

Opening Previously Displayed Exams

Opening Printsets

### Opening Exams without Priors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generally, VistARad’s hanging protocols are set up to locate and open priors when a current exam is opened. This capability can be disabled on an exam-by-exam basis, or, if necessary, for all exams.

When prior retrieval is disabled, any prior retrieval logic in a hanging protocol is ignored when an exam is opened.

To temporarily disable prior retrieval

Select the exam you want to open.

Click the Open/No Prior button (located to the right of the Open button in the Manager window).

To permanently enable/disable prior retrieval

Click View \| Settings \| Hanging Protocol.

Select or clear the last two check boxes in the dialog as desired.

Click OK.

Note Other settings apply for priors of routed exams (details on page [122](#_Ref136330353)).

### Opening Exams for a Specific Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Patient Exams list or Patient Lookup to locate exams for a specific patient. You can also access a list of previously viewed patients.

To use the Patient Exams list

In any exam list in the Manager, select an exam associated with the patient of interest. Then click the Patient Exams tab.

To view previous patients

Click View in the Manager main menu, then click one of the patient names listed in the bottom part of the menu.

Up to 10 names are listed, with the most recently viewed patient listed first.

Only names for exams viewed in the current VistARad session are listed.

To use the Patient Lookup dialog

Press \<Ctrl+L\>, or click Patient Lookup in the Manager window to display the Patient Lookup dialog.

Type the patient’s last name or ID number using:

One or more letters in the patient’s last name.

The patient’s social security number. (No spaces or dashes.)

The first letter of the last name and the last four digits of the patient’s social security number. (S1234)

The first three letters of the last name and the first letter of the first name separated with a comma. (Smi,J)

Click Search or press \<Enter\>.

If a matching patient is found, the Patient Exams list will display all exams for that patient.

If more than one matching patient is found, each patient is listed in the Patient Lookup dialog. Double-click the patient for whom you want to see a list of exams.

If there are no matching patients, a “NO MATCH” message is displayed at the bottom of the dialog.

| ![](vistarad-user-guide/037.png) | In urgent situations, you can use Patient Lookup to open an exam before all the images in the exam are processed or before the images are verified (QCed) by the technologist. Exams opened this way cannot be locked and cannot have their status updated. These exams can be opened and interpreted normally once they appear on the Unread Exams list. |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Opening Multiple Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several exams in the same exam list can be opened at once.

Tip You can use ReadList to work through all unread exams in an exam list (details on page [19](#using-readlist)).

Note If VistARad is interfaced to a voice dictation system, contact your Imaging Coordinator before opening multiple exams for interpretation. Certain dictation systems may not appropriately manage requests to open multiple reports.

To open multiple exams

Display the exam list that contains the exams you want to open.

Select the exams.

To select exams that are listed consecutively, click the first exam, press and hold down the \<SHIFT\> key, and click the last exam.

To select exams that are not listed consecutively, press and hold down the \<Ctrl\> key, then click each exam.

Click Open. Note that:

If the exams are all associated with the same patient, the most recent exam is treated as the “current” exam, and is used to determine which hanging protocol is automatically selected.

If the exams are associated with different patients, each exam is treated as a “current” exam, and a separate hanging protocol is selected for each exam.

### Opening Reference-Quality Exams 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When x-ray (CR or DX) exams are acquired, both diagnostic and reference quality images are generated. By default, VistARad always displays the highest-resolution images available. However, you can choose to open the reference-quality images as well.

To view reference quality images

Click View \| Settings \| Manager \| General.

In the Options area, select the View Reduced-Resolution Images check box.

Note This is a session-based setting, which will always be cleared when VistARad is started.

Click OK.

Open an exam.

Exams cannot be locked or have their status updated when reference quality images are used.

If no reference-quality images are available, the full-resolution images are used, and the exam (if it is unread) is locked as usual.

### Opening Previously Displayed Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An entry for each exam opened in a VistARad reading session is added to the Exam History list. Exams are retained in the Exam History list for three days. If the same exam is opened several times, there will be several entries for that exam in the Exam History list.

To display the Exam History list

Click the Exam History tab in the Manager window.

If this tab is not visible:

Click View \| Settings \| Manager \| General.

Select the Generate History List check box.

To indicate which exams should be included in the Exam History list, select either the For Locked Exams Only or the For All Exams option.

Click OK.

To clear the Exam History list

Entries for exams opened more than three days ago are automatically removed from the Exam History list. You can also manually remove entries:

1.  In the Manager window, click the Exam History tab.
2.  To delete selected entries, click each entry, then click Clear.
3.  To delete all entries, click Clear All, then click OK when you are asked for confirmation.

### Opening Printsets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A printset is a group of related exams as defined in the Radiology Package. When the printset is interpreted, all exams in the printset share the same report.

In VistARad, opening and locking any exam in a printset will open and lock all exams in the printset. When the status of an exam in a printset is updated, the status of all exams in the printset is updated.

## Managing the Exam Load Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section, Getting Started, is an overview of the techniques available for exam load management. The subsequent section, In Depth, covers the second two of these techniques in more detail.

### ­Exam Load Management: Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad loads and displays a series’ images in a priority governed by the hanging protocol. For a small study, or a collection of small studies, loading is rapid and largely “hands free”. But for large studies, or a collection of large studies, users may want to manage this process. VistARad enables this three ways. Used together, they allow more fine tuning of the loading process.

#### Expedite loading to a viewport

If a viewport that contains images is selected with a mouse click, VistARad will expedite loading images to that viewport. Loading to viewports with linked images is also expedited. This applies to viewports in Viewer, Browser, and Scrapbook windows.

#### Pause or stop all exam loading

VistARad will pause in-progress loading of images for all exams[^1] when you click the Manager’s Stop Load button. VistARad then displays the Cancel/Partial Load dialog, which allows a Partial, Continue, or Cancel, operation for each paused exam load. The selected operation is applied to each exam by clicking OK. The Cancel/Partial Load dialog is illustrated below.

> ![](vistarad-user-guide/038.png)

> Note The example shows a single paused exam load; additional paused loads would appear on additional lines.

#### Pause or stop individual series loading

Note The following applies only to the Preview window in List View mode. Toggle between Thumbnail and List View modes by clicking ![](vistarad-user-guide/039.png) for the exam(s) of interest.

VistARad will pause in-progress loading of images *for an individual series* when you click the Pause button *for that series* in the Preview window. If loading does not complete, the ![](vistarad-user-guide/040.png) icon is displayed, indicating that the series has partially loaded.

Resume loading a paused series by clicking Resume.

Remove a paused series’ images from memory by clicking Purge. A single placeholder thumbnail image, for each purged series, is retained.

More detail about these last two techniques, and the interactions between them, are covered in Exam Load Management: In Depth on page [28](#exam-load-management-in-depth).

#### Split a Stack Which Is Too Large to Load 

In rare cases, an exam may be structured as a single series which is too large to load into memory. VistARad detects this and displays the Split Stacks dialog, which allows the stack to be split into series which are small enough to load. These smaller stacks appear in the Preview window, where they can be managed with the features previously described.

The Split Stacks dialog displays instructions along with the exam in question and its image count. The Splitting Specification frame has three radio button options:

- Even split: The resulting series are approximately equal in size.
- Maximum size: The exam is split into resulting series that are as large as possible. The last series holds the remainder.
- Custom: The user can specify up to 10 series. VistARad will give guidance on the maximum series size possible, and track how many images remain after each series is delineated.

After initial use, the Split Stack dialog will re-appear if the exam is re-hung with a different hanging protocol. See Using Hanging Protocols on page [135](#_Ref137008027).

An illustration of the Split Stacks dialog appears below.

![](vistarad-user-guide/041.png)

### Exam Load Management: In Depth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Cancel / Partial Load Dialog options

When the Cancel / Partial Load dialog is displayed (after clicking the Manager’s Stop Load button), three options are available. (\* indicates the default selection.)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Partial *</strong></td>
<td><p>Unloaded images are not loaded. Images loaded before <strong>Stop Load</strong> was clicked are retained.</p>
<p>BINARY:(loaded/total) appears in the Manager’s List Status column.</p>
<p>![](vistarad-user-guide/042.png), indicating partially loaded, is displayed in the List Mode entry of the Preview window for this series.</p></td>
</tr>
<tr class="even">
<td><strong>Continue</strong></td>
<td><p>Unloaded images are loaded until complete, or until <strong>Stop Load</strong> is clicked again.</p>
<p><strong>Note</strong>: This is equivalent to clicking the <strong>Resume</strong> button of the Preview window for all paused requests.</p></td>
</tr>
<tr class="odd">
<td><strong>Cancel</strong></td>
<td><p>Remaining images are not loaded.</p>
<p>Cancelled\Displayed appears in the Manager’s List Status column if at least one image was loaded.</p>
<p>Cancelled appears in the Manager’s List Status column if no images were loaded.</p></td>
</tr>
</tbody>
</table>

Note Setting an interrupted load request’s option to ‘Cancel’ and then clicking the *dialog box’s*Cancel button resumes loading of remaining images.

Note In a multi-line Cancel/Partial Load dialog, setting a row to Partial (the default) sets all rows beneath it to Partial.

#### The Preview window’s List Mode Pause/Resume and Purge Buttons

The Pause/Resume and Purge buttons presentation depends on which actions are possible for their associated series. They are grayed-out if they do not apply.

Note There is no grayed-out Pause button. It changes directly to Resume if the associated exam load is incomplete, and to grayed-out Resume if an exam load is complete or has been cancelled (using the Stop/Load \| Cancel sequence described above).

The following table identifies the buttons by text, describes their effects, and describes the actions available from each state.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 66%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Button</strong></th>
<th><strong>What it Does &amp; Visible Effect(s)</strong></th>
<th><strong>Available Follow-Up Actions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Pause</strong></td>
<td><p>Pauses an actively loading series. A few additional images may load, and may complete the series.</p>
<p><em>If loading is incomplete:</em><br />
<br />
1) The button’s text changes to Resume.</p>
<p>2) The ![](vistarad-user-guide/043.png) icon, indicating partially loaded, appears.</p>
<p>3) The Load Progress status bar stops short.</p>
<p>4) The Loaded/Total counters are not equal.</p>
<p>5) The Manager’s Load Status column is frozen at the point where the last image loaded.</p></td>
<td><strong>Resume or Purge</strong></td>
</tr>
<tr class="even">
<td><p><em>If loading completes:</em><br />
<br />
1) The button’s text changes to <strong>Purge</strong>.</p>
<p>2) The Load Progress status bar is full.</p>
<p>3) The Loaded/Total counters are equal.</p>
<p>4) Loaded/Displayed appears in the Manager’s Load Status column reports.</p></td>
<td><strong>Purge</strong></td>
</tr>
<tr class="odd">
<td><strong>Resume</strong></td>
<td><p>Resumes loading of the series.<br />
<br />
1) The Load Progress status bar, Memory Usage status bar, and Loaded/Total counters update accordingly.</p>
<p>2) The Manager’s Load Status column resumes updating.</p></td>
<td><strong>Pause</strong></td>
</tr>
<tr class="even">
<td><strong>Purge</strong></td>
<td><p>Removes all images from memory, except for a single “placeholder” thumbnail.</p>
<ol type="1">
<li><p>The button’s text toggles to <strong>Resume</strong>.</p></li>
<li><p>The Load Progress status bar, Memory Usage status bar, and Loaded/Total counters update accordingly.</p></li>
<li><p>“Loaded/Displayed” appears in the Manager’s Load Status column.</p></li>
</ol></td>
<td><strong>Resume</strong></td>
</tr>
</tbody>
</table>

Exam loads paused by Stop Load from the Manager may be managed with Preview window List View mode buttons:

| <u>Manager Stop Load Status</u> | <u>Preview Window List Mode Action</u>                           |
|-------------------------------------|----------------------------------------------------------------------|
| Partial                             | Resume (on a per-series basis)                                   |
| Cancel                              | Purge (on a per series basis, if one or more images were loaded) |
| Continue                            | Purge or Resume                                              |

In-progress exam loading is subject to a Stop Load action, even if it has been Continued from a previous Stop Load action.

## Exam List Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the types of exam lists available in VistARad, the fields that can appear in exam lists, and how exam lists are retrieved from the VistA Host.

### Types of Exam Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each type of exam list is described below.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Exam List</strong></th>
<th><strong>Initial Sort</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient Exams</td>
<td>Most recent image date/time</td>
<td>Contains subtabs for the selected (active) patient in the Viewer and in the Manager. </td>
</tr>
<tr class="even">
<td>Unread Exams</td>
<td>Priority, then oldest image date/time</td>
<td>Exams waiting for interpretation (status of <span class="smallcaps">examined</span>).</td>
</tr>
<tr class="odd">
<td>Custom Exams</td>
<td>Site-defined</td>
<td><p>One or more subtabs for each active custom list will be present. Click <strong>View | Settings | Manager | Custom Lists</strong> to see custom lists available at your site. ‘</p>
<p>My Recent Exams’ is a pre-defined custom list of all exams with a status of Interpreted/Dictated, or Transcribed, which were interpreted by the currently logged-in user. It may be modified at the site’s discretion.</p></td>
</tr>
<tr class="even">
<td>Exam History</td>
<td>Most recent display time</td>
<td>Exams displayed in recent user sessions. Entries more than three calendar days old are removed automatically; removal of old entries is triggered by the user’s first login each day.</td>
</tr>
<tr class="odd">
<td>Recent Exams</td>
<td>Most recent image date/time</td>
<td>Interpreted exams waiting for report verification (status of <span class="smallcaps">interpreted</span> or <span class="smallcaps">transcribed)</span>. This list is available only if it has been explicitly enabled. (<strong>View | Settings | Manager | General</strong>)</td>
</tr>
<tr class="even">
<td>All Active Exams</td>
<td>Most recent image date/time</td>
<td>Combines the Recent and Unread lists. This list is available only if it has been explicitly enabled. (<strong>View | Settings | Manager | General</strong>)</td>
</tr>
<tr class="odd">
<td>Open/ Reserved Exams</td>
<td>Order opened</td>
<td>Located at the bottom of the Manager window, this list shows opened or preloaded exams (preloading is handled by ReadList).</td>
</tr>
</tbody>
</table>

### Fields in Exam Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the fields used in VistARad’s exam lists.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Exam List Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td># Img</td>
<td>Number of acquired images in the exam.</td>
</tr>
<tr class="even">
<td>Case #</td>
<td>The long case (accession) number. Based on a patient’s registration date (MMDDYY) and an ID number generated by the Radiology package. In the Patient Exams list, this field is labeled as “Day/Case.”</td>
</tr>
<tr class="odd">
<td>CPT</td>
<td>The Current Procedural Terminology code associated with the exam. Only present in the Patient Exams list.</td>
</tr>
<tr class="even">
<td>HP/TP;<br />
HP Selected</td>
<td>Indicates which hanging protocol or template was used to open the exam. Only present in the Exam History and Open/Reserved Exams lists.</td>
</tr>
<tr class="odd">
<td>ID #</td>
<td>In VHA implementations, the first letter of a patient’s last name and the last four digits in the patient’s SSN (also called the quick PID). In the Patient Exams list, this is shown at the top of the list only. Indian Health Resource &amp; Patient Management System implementations display the Medical Record Number instead.</td>
</tr>
<tr class="even">
<td>Image Date/Time</td>
<td><p>For exams acquired after the installation of Patch 54, this field indicates the date and time that the images are <em>acquired</em> by the imaging modality.</p>
<p>For exams acquired before the installation of Patch 54, this field indicates the date and time that the images were <em>processed</em> by the DICOM Gateway.</p></td>
</tr>
<tr class="odd">
<td>Imaging Loc</td>
<td>Imaging location as entered in the Radiology Package when exam is registered.</td>
</tr>
<tr class="even">
<td>ImgType</td>
<td>The image type. The exact use of this field is dependent on how it is defined at your site. Can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Interp By </td>
<td>Initials of the radiologist that interpreted the exam. Not present in Unread list.</td>
</tr>
<tr class="even">
<td>IntStat</td>
<td>Internal integer value for status codes. Can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Load Status</td>
<td><p>This field appears only in the Open/Reserved Exams list at the bottom of Manager window, and it will contain one of the following values:</p>
<p><strong>#/#</strong> – Exam is being opened; the first number indicates which image is being processed and the second number indicates the total number of images in the exam.</p>
<p><strong>Loaded</strong> – Exam is loaded into memory and will be displayed automatically as soon as the currently displayed exam is closed. Appears only while ReadList is active.</p>
<p><strong>Displayed</strong> – Exam is displayed in one or more image-related windows (the Preview window, the Viewer window, etc.).</p>
<p><strong>Cancelled</strong> – Exam load was cancelled by the user before any images can be displayed.</p>
<p><strong>Failed</strong> – No images in the exam could be displayed.</p>
<p>Note that if the suffix <strong>Incomplete</strong> is present, one or more images in the exam could not be loaded or displayed, and the exam, if unread, cannot be locked for interpretation.</p></td>
</tr>
<tr class="even">
<td>Location Type</td>
<td>The value of the <span class="smallcaps">type</span> field in the <span class="smallcaps">hospital location</span> File (#44,2); can be used to distinguish inpatient and outpatient locations. This field is derived from the Requesting Location entered in the Radiology order. This field can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Lock</td>
<td><p>Indicates if an exam is locked or reserved, and the initials of who holds the lock or reserve.</p>
<p>In the Exam History list only, this field contains a Yes/No value indicating if the exam was locked when it was opened.</p>
<p>In the Open/Reserved list only, this field contains one of the following values:</p>
<p><strong>VIEW</strong> <strong>–</strong> Exam is displayed by the current user, but is not locked.</p>
<p><strong>LOCKED</strong> <strong>–</strong> Exam is displayed and locked by the current user.</p>
<p><strong>RESERVE</strong> <strong>–</strong> Exam is reserved by current user, but not yet displayed (exam is preloaded).</p>
<p>In the Selection ReadList only, this field can also contain the value <strong>LD:RESERVE</strong>, indicating that the exam is reserved and pre-loaded, but not yet locked.</p></td>
</tr>
<tr class="even">
<td>MAGSRT</td>
<td>Internal value used for sorting exams by the presence or absence of images. A = Images, B = No images. Can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Mod</td>
<td>The acquisition modality type.</td>
</tr>
<tr class="even">
<td>Modifier</td>
<td>Lists any procedure modifiers entered from the radiology requisition. Present in the Patient Exams list; available for use in custom lists.</td>
</tr>
<tr class="odd">
<td>Onl</td>
<td><p>Indicates the online availability of images in the exam.</p>
<p><strong>Y</strong> <strong>–</strong> Images are in short-term storage (image servers).</p>
<p><strong>N</strong> <strong>–</strong> Images are in long-term storage (the jukebox), and may take up to several minutes to open.</p>
<p><strong>n/a</strong> <strong>–</strong> Images are not available.</p></td>
</tr>
<tr class="even">
<td>Patient Name</td>
<td>The name of the examined patient. In the Patient Exams list, this is shown at the top of the list only.</td>
</tr>
<tr class="odd">
<td>Priority</td>
<td><p>The priority of the exam as entered by the ordering clinician. Standard priority levels are: Stat, Urg (Urgent), Pre-op (pre-operative), and Rout (Routine).</p>
<p>Not present in the Patient Exams list.</p></td>
</tr>
<tr class="even">
<td>Procedure</td>
<td>The procedure performed.</td>
</tr>
<tr class="odd">
<td>Pt Loc’n Abb</td>
<td>Abbreviated requesting location as entered in the exam order. Can be used only in custom lists.</td>
</tr>
<tr class="even">
<td>Pt Loc’n Name</td>
<td>Requesting location as entered in the exam order. The exact use of this field is dependent on how it is defined at your site. Can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Rad Div</td>
<td>The hospital division. The exact use of this field is dependent on how it is defined at your site. Can be used only in custom lists.</td>
</tr>
<tr class="even">
<td>RC</td>
<td>If displayed, will indicate which sites, if any, have received routed copies of this exam (details on page <a href="#using-vistarad-for-teleradiology">120</a>).</td>
</tr>
<tr class="odd">
<td>REG DATE</td>
<td>The registration date of the exam. Custom list use only.</td>
</tr>
<tr class="even">
<td>REG DATE-SORT</td>
<td>The registration date of the exam for sorting. Custom list use only.</td>
</tr>
<tr class="odd">
<td>SORT_IMG_DT</td>
<td>Internal date format used for sorting. Can be used only in custom lists.</td>
</tr>
<tr class="even">
<td>SSN-4</td>
<td>The last four digits of the examined patient’s social security number. Can be used only in custom lists.</td>
</tr>
<tr class="odd">
<td>Status</td>
<td>The status of the exam as reported by the Radiology Package. Standard values are <span class="smallcaps">waiting</span> (or <span class="smallcaps">called for)</span>, <span class="smallcaps">examined</span>, <span class="smallcaps">interpreted</span>, <span class="smallcaps">transcribed</span>, and <span class="smallcaps">complete</span>. The names used for these values may vary from site to site.</td>
</tr>
<tr class="even">
<td>TECH</td>
<td>The initials of the technologist who performed the exam. Sortable; custom list use only.</td>
</tr>
<tr class="odd">
<td>Timestamp</td>
<td>The date and time that an exam was opened for display. Present only in the Exam History List.</td>
</tr>
<tr class="even">
<td>Ward </td>
<td>The hospital ward at the time the exam was registered. Can be used only in custom lists.</td>
</tr>
</tbody>
</table>

### Exam Lists and the VistA Host

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you click a tab in the Manager window to display an exam list, you are querying VistA for all exams that meet the criteria of the list. Certain site-wide parameters that reside on the VistA Host also affect what is shown in exam lists.

For a detailed listing of the specific site parameters involved, refer to Chapter 3 in the *Imaging Installation Guide*.

Pre-compiled vs. on-demand lists

Pre-compiling lists allows the VistA Host to assemble them, periodically, in the background. This allows the exam list to display immediately on request. Most sites are configured to pre-compile the Unread Exams list. When pre-compiled data is displayed at a VistARad workstation, the time elapsed since the last compile is displayed as the *List Age*, as illustrated in the figure below. For Unread Exams lists, exams newly marked “Interpreted” are immediately removed from the list, whereas exams newly marked “Examined” do not appear on the list until the next pre-compile has run.

![](vistarad-user-guide/044.png)

Some sites elect to have exam lists generated on demand. If this is the case, a list may take longer to display, but it will contain the most current information.

Pre-compiling also applies to the Recent Exams list and any custom lists that contain unread exams.

Show only exams with images

Sites can determine if the Unread, Recent, and All Active exam lists show all exams, or only those exams that have images available for display. This setting will also affect custom lists defined using the “Pending” exam status.

Excluding old exams

Certain sites, especially new sites transitioning to VistARad, may configure the Unread Exams list or the Recent Exams list to exclude any exams that predate a given time. If used, this setting also affects any custom lists that contain unread exams.

This page intentionally left blank.

# Patient Records 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Opening Patient Records

Using the Reports Window

## Opening Patient Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use VistARad to review requisitions, reports, patient profiles, and health summary reports stored in the VistA system.

Note Opening a record for a patient makes that patient the “active patient.” Exams for other patients, if displayed, will be hidden (not closed) when the record is opened. For more information, see Switching between Patients on page [61](#_Ref135107192).

### Displaying Requisitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam requisitions can be displayed as needed. They can also be displayed automatically whenever an exam is opened for interpretation.

Some sites may limit the display of requisitions to users designated as Radiologists or Radiology Technologists in the Radiology package.

The Complications and Tech Comments portions of a requisition are visible only to users designated as Radiologists or Radiology Technologists in the Radiology package.

Medications and radiopharmaceuticals are visible only to users designated as Radiologists or Radiology Technologists in the Radiology package.

To display requisitions for open exams

In a viewport containing images from the open exam, click ![](vistarad-user-guide/045.png). If the exam is unread, the requisition is displayed. If the exam is already interpreted, the report is displayed.

To explicitly choose the requisition or report, drag down on the ![](vistarad-user-guide/046.png) icon, then click Requisition or Report.

To display requisitions for any exam

In the Manager window, locate the exam of interest.

Click the exam and then click the Requisition button, or right-click the exam and then click Requisition.

To display requisitions automatically

In the Manager or Viewer menu, click View \| Settings.

Under the Manager tab, click the General subtab.

Select the Auto-Open Requisition check box.

Click OK. The next time an exam is opened and locked, its requisition will be opened as well.

### Displaying Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exam reports can be displayed for interpreted exams. Note that:

The Complications and Tech Comments portions of a report are visible only to users designated as Radiologists or Radiology Technologists in the Radiology package.

Medications and radiopharmaceuticals are visible only to users designated as Radiologists or Radiology Technologists in the Radiology package.

Draft (un-verified) exam reports can be viewed by other radiologists. Depending on how the Radiology Package is configured, draft exam reports may also be viewable by other VistA users.

Reports can be displayed with or without opening the associated exam.

To display reports for open exams

In a viewport containing images from the open exam, click ![](vistarad-user-guide/047.png). If a report is not yet available, the exam requisition will be displayed instead.

To display reports for any exam

In the Manager window, locate the exam of interest.

Click the exam and then click the Report button, or right-click the exam and then click Exam Report.

### Displaying Patient Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Profile contains demographic information derived from the ADT (Admission Discharge Transfer) package.

To display a patient profile

In the Manager window, locate an exam associated with the patient of interest.

Click the exam and then click the Patient Profile button, or right-click the exam and then click Patient Profile.

### Displaying Health Summary Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health summary reports are a collection of site-defined reports generated by the Health Summary Package. Using VistARad, you can access any health summary report available at a site. You can also designate a default health summary report and define a personal “short list” of frequently used health summary reports.

To open a Health Summary report

In the Manager window, locate an exam associated with the patient of interest.

Click the Health Summary button. If you have designated a default health summary, that report will display.

Tip An asterisk is displayed in the Health Summary button when you have designated a default report.

If you have not designated a default heath summary, the Health Summary dialog will open instead.

To see all available reports, click Show Preferences in the Health Summary window.

To open a report, click the report, then click View Health Summary.

To define a custom report list or designate a default report

In the Manager window, click the arrow on the right side of the Health Summary button, then click the Health Summary Window option.

In the dialog that displays, click Show Preferences to display the list of all health summary reports.

To modify your personal list in the top part of the dialog:

To add a health summary report to the list, click the report name in the bottom of the dialog, then click Add.

To remove a health summary report from the list, click the report name in the top of the dialog, then click Remove.

To specify a default health summary report, click a report in the top part of the dialog, then click Set Default.

Tip An asterisk is displayed next to the name of the default report. An asterisk is also displayed in the Health Summary button when you have a default report defined.

## Using the Reports Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports window displays patient records that have been opened from the Manager or the Viewer. If a patient record is opened but the Reports window is not visible, the Reports window can be displayed by clicking ![](vistarad-user-guide/048.png).

Tip You can make the Reports window stay visible while you are working with images in other windows. For more information, see Using Pushpins on page [111](#_Ref136742852).

If multiple records are open in the Reports window, only the most recently selected record is visible. Any open patient record is accessible in the Reports window until the record is explicitly closed or until you exit VistARad.

To display other open records

Click the Reports menu option and then click an item in the list of open records.

Note Items under the Reports menu are filtered by the active patient. To change the active patient, click the Active Patient button located in the title bar of the Reports window.

To print a record

Open the record you want to print.

In the Reports window, click File \| Print.

In the dialog that displays, select the printer that you want to use, then click Print.

To close a record

Open records in the Report window are closed automatically when all exams are closed.

To close the currently displayed record, click File \| Close Report in the Reports window.

To close all records, click File \| Close All in the Reports window.

To change the Reports window font

In the Reports window, click File \| Font.

In the Fonts dialog, select the font type, size, and style.

Click OK to apply your changes.

# Context Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter includes:

Context Management

The Clinical Context Object Workgroup Protocol

The Context Management Settings Tab

Context Changes

CPRS Tools Menu for VistARad

## Context Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Context Management (CM) allows users to choose a subject once in one application, and have all applications containing information on that same subject “tune” to the data they contain. This eliminates the need for the user to redundantly select the subject in the varying applications. In the healthcare industry, for example, multiple applications operating “in context” through use of a context manager would allow a user to select a patient (*that is,* the subject) in one application.

Context Management is gaining in prominence in healthcare due to the creation of a standardized protocol, the Clinical Context Object Workgroup (CCOW) Protocol, enabling applications to function in a “context-aware” state.

## The Clinical Context Object Workgroup Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCOW is a Health Level 7 (HL7) standard protocol designed to enable dissimilar healthcare software applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.

CCOW is the primary standard protocol used in healthcare to facilitate the Context Management process. Although both CCOW and non-CCOW compliant applications can use CM, the CCOW standard helps facilitate a more robust and near “plug-and-play” interoperability across applications.

When CCOW is available, the VistARad client uses CCOW to synchronize patient and user context management with the Computerized Patient Record System (CPRS) and other CCOW-enabled applications. A new Settings tab, Context Management, is used to enable context management; the setting Enable Context Management must be checked to use the context management functionality.

## The Context Management Settings Tab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Context Management settings tab, allows the user to manage how CM operates on the individual workstation. The user must check the Enable Context Management in order to use CM capability.

## Context Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A context indicator (icon) appears at the top of the various VistARad windows to the left of the Patient Name and demographics. A Context menu item appears on the Manager and Viewer menu bars for options to Suspend/Resume context, etc. The application also automatically changes the displayed icon to reflect the change in context.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Icon</strong></th>
<th><strong>Title</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">![](vistarad-user-guide/049.png)</td>
<td rowspan="2"><strong>Changing</strong></td>
<td>Displayed when the Clinical Link is changing. This icon may appear so briefly that the user may not see it. It is displayed when the common (linked) patient is changing. For example, if VistARad is linked with CPRS and CPRS changes from one patient to another, this icon will display during the change process.</td>
</tr>
<tr class="even">
<td>Patient Context is Changing</td>
</tr>
<tr class="odd">
<td>![](vistarad-user-guide/050.png)</td>
<td><strong>Broken</strong></td>
<td><p>Displayed when an application is not linked or the application is “out of patient context.” For example, if CPRS is linked and displaying one patient and VistARad is displaying a different patient, then VistARad is said to be “out of patient context” and will display this icon.</p>
<p>Patient Context is Broken</p></td>
</tr>
<tr class="even">
<td rowspan="2">![](vistarad-user-guide/051.png)</td>
<td rowspan="2"><strong>Linked</strong></td>
<td>Displayed when an application is utilizing CCOW to maintain patient context with the CCOW server. For example, if VistARad is open and displaying the same patient (as defined by the CCOW server) for all linked applications, then VistARad will display this icon.</td>
</tr>
<tr class="odd">
<td>Patient Context is Joined</td>
</tr>
</tbody>
</table>

## CPRS Tools Menu Option for VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may also configure a new CPRS Tools menu option for launching VistARad from CPRS. Refer to the *VistA Imaging Installation Guide*, under Associating Display and Capture with CPRS, for background information on this configuration step. See the *VistA Imaging Technical Manual,*CPRS Tools Menu Option for VistARad, for information about configuring for launching VistARad.

This page intentionally left blank.

# VistARad and Voice Dictation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

About the VistARad Dictation Interface

Starting the Dictation Interface

Opening Exams and Reports for Dictation

Working with the Dictation Interface

## About the VistARad Dictation Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dictation interface lets VistARad communicate with voice dictation software[^2]. Contact your Imaging Coordinator to determine if the dictation interface is enabled for your workstation.

If the dictation interface is enabled, opening and locking an exam for interpretation in VistARad triggers the dictation software to open the exam’s report. You can begin dictating a report without manually pre-selecting it.

Note that the VistARad dictation interface is one-way. Locking an exam for interpretation triggers selection of the associated report in the dictation package. However, if you manually switch between reports inside the dictation package, you must manually select the appropriate exam in VistARad.

Whereas “dictation interface” is the term used for software/software communication, VistARad’s user interface for dictation is called the “dictation dialog.” The baseline behavior of the dialog is as follows::Whenever a single exam is opened with a Lock, that exam will appear on the dictation dialog with the “Dictate?” prompt defaulted to “YES.”

Whenever multiple exams (for the same patient) are opened concurrently with a Lock, the first exam listed in the dialog is defaulted “YES” for the “Dictate?” prompt, and all other exams are defaulted to “NO.”

Two user preferences allow you to alter the Dictation dialog’s baseline behavior:

![](vistarad-user-guide/052.png)

The first of these options is enabled/disabled site-wide by the ENA DICT PREF-YES ALL LOCKED field (#13) of the MAG VISTARAD SITE PARAMETERS file (#2006.69). When it is enabled, each user can set this option. When disabled , this option is locked—the default configuration is Disabled.

When checked, “Default the Dictation dialog to YES for ALL locked exams” presets the value of the Dictate? column to YES when multiple Locked exams are opened.

If the second option is checked, when opening multiple Locked exams, only the single exam corresponding to the "Current" exam will be listed in the Dictation dialog, with the Dictate? column defaulted to YES.

| Warning: | Do not set Dictate? to YES for multiple exams unless your Imaging Coordinator has verified that your dictation software can handle multiple case IDs. |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|

| Note: | Some interactions work differently when multiple locked exams are open concurrently. See the Multiple Locked Exams section below. |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|

## Multiple Locked Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User interactions with the application will differ when multiple locked exams are open concurrently.

### When Multiple Locked Exams for Different Patients are Open

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the user simultaneously opens multiple exams for different patients, the dictation dialog is suppressed and will not be displayed. The following message box will be displayed if the user has previously checked the Dictation dialog option Do not show this window again:

![](vistarad-user-guide/053.png)

2.  To initiate a dictation for any of these exams the user must right-click on the exam of interest from the Manager’s Open/Reserved Exams listing, and then select the Dictate option from the context menu drop-down.
3.  For any exam listed in the Open/Reserved Exams, the “Dictate” menu option for that same exam—if selected from the main list window (Patient and Unread exams display)—is now grayed out. That is, the “Dictate” context menu option can only be initiated from the exam’s entry in the Open/Reserved Exams list. The “Dictate” context menu option for any exam in the “Reserved” state is grayed out.

### Dictation Dialog Forced Under Certain Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dictation dialog is now forced on screen if:

1.  The user opens an exam with a Lock while another Locked exam is already open (same or different patient).
2.  The user selects the Dictate context menu option on the main exam list (Unread or Patient) for an exam while another Locked exam is already open (same or different patient).

## Starting the Dictation Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the dictation interface is enabled at your workstation, it will attempt to start automatically when VistARad is started. Optionally, you can manually start the dictation interface if you are logged in to both VistARad and the dictation software you are using.

Starting the dictation interface automatically

Log in to your voice dictation system (this may be on the same workstation as VistARad, or on a separate workstation).

Log in to VistARad.

Starting the dictation interface manually

If you start the dictation software after logging in to VistARad, you will need to start the dictation interface manually. To do this, click Dictation \| Establish Dictation Connection in the Manager main menu.

## Opening Exams and Reports for Dictation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps assume a basic understanding of opening exams (details on page [17](#opening-exams)).

Opening an exam for dictation

Note If another report is already open, be sure to save (or sign) that report before opening other exams for interpretation.

While the dictation interface is active, use the Manager to open an unread exam or to start ReadList.

As the exam is being opened, the Dictation dialog will display. If the Dictate? column is not pre-set by the option described above, check each YES/NO value that is displayed.

If you need to change a value:

Choose YES if you want VistARad to send the case ID to the dictation software (which triggers the display of the associated report).

Choose NO if you want to open the exam without opening the associated report for dictation.

| Warning: | Do not set Dictate? to YES for multiple exams unless your Imaging Coordinator has verified that your dictation software can handle multiple case IDs.                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tip:     | Your Dictate? selection determines the initial value of the Interpret? column in the Close Exams/Update Status dialog. For details, see the table that lists Manager \| General tab settings on page [114](#manager_tab_general). |

Press \<Enter\> or click OK. The dictation software will open the appropriate report for the exam.

Opening a report (only) for dictation

To open a report in your dictation software via VistARad’s dictation interface, right-click any exam in an exam list, then click Dictate. Note that:

This will not open the exam. The exam itself can be opened by selecting it and clicking Open.

You will not be asked to confirm the operation (the Dictation dialog will not display).

This can be used for any exam, regardless of the exam’s status.

Multiple exams and the dictation interface

If you open multiple exams belonging to the same patient with a lock, it is presumed that you will want to dictate a report for the most recent exam, but not for the other exams. This is reflected in the Dictation dialog, where the first exam listed will have Dictate? set to YES, and where other exams will have Dictate? set to NO.

Warning Do not set Dictate? to YES for multiple exams unless your imaging Coordinator has verified that your dictation software can handle multiple cases.

Printsets and the dictation interface

If you open an exam in a printset, all exams in the printset are locked, but the case ID of only one exam (the one you selected) is sent to the dictation software. It is assumed that the dictation software will be able to manage a “combined report” using its own connection to the VistA System.

## Working with the Dictation Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppressing the Dictation dialog

By default, the Dictation dialog displays each time you open an exam with a lock. If you want to always send case IDs to the dictation software without a confirmation prompt, do one of the following:

In the Manager, clear the checkmark from the Dictation \| Prompt for Dictation option.

Open an unread exam for interpretation, and when the Dictation dialog displays, select the Do not show this window again check box before clicking OK.

Note that:

This setting is session-specific and will need to be reset if you exit and restart VistARad.

This setting is ignored if you open and lock multiple exams.

Restoring the Dictation dialog

If you want to be prompted to send the case ID to your dictation software each time you open an exam with a lock, choose the Dictation \| Prompt for Dictation option from the Manager main menu.

Disabling the dictation interface

In the Viewer or Manager, click View \| Settings.

Under the Manager tab, click the Dictation tab, then clear the Enable Dictation Interface check box (connection settings are retained).

Re-enabling the dictation interface

In the Viewer or Manager, click View \| Settings.

Under the Manager tab, click the Dictation tab, then select the Enable Dictation Interface check box.

If you have not done so already, start the dictation software.

In the Manager window, click Dictation \| Establish Dictation Connection.

# Working with Open Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><p>This chapter covers:</p>
<p>Surveying Exams</p>
<p>Using the Preview Window</p>
<p>Using the Viewer Window</p>
<p>Using the Browser Window</p></th>
<th><blockquote>
&#10;</blockquote>
<p>Using the Scrapbook Window</p>
<p>Using Scout Images</p>
<p>Using the Image Detail Window</p>
<p>Using the Imaging Data Window</p>
<blockquote>
&#10;</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Surveying Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers:

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Loading Viewports</p>
<p>Using Conditional Indicator Icons</p>
<p>Navigating in Viewports</p>
<p>Working with Images</p></th>
<th><p>Key Images</p>
<p>Clearing Viewports</p>
<p>Switching between Patients</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Loading Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an exam is opened using an appropriate hanging protocol, images in the exam are automatically loaded into viewports in the Viewer. However, if the exam contains more image sets than the active hanging protocol can accommodate, you may need to load some image sets manually.

To determine which images are loaded

If it is not already visible, display the Preview window by clicking ![](vistarad-user-guide/054.png). In the Preview window, each exam for the active patient is displayed on a separate row. In each row, one or more thumbnail images are displayed. Each thumbnail represents a group of one or more images in the exam.

If ![](vistarad-user-guide/055.png) icon is displayed in a thumbnail, the associated image set is loaded and visible in the Viewer or the Browser (or it has been visible at some point during the current viewing session).

If ![](vistarad-user-guide/056.png) icon is displayed in the thumbnail, the associated image set is loaded as a hidden image set (details on page [59](#_Ref213034482)).

If no icon is displayed in the thumbnail, the associated image set must be loaded manually to be displayed.

To load viewports manually

In the Preview window, locate the images you want to load.

Do one of the following:

To load images into the Viewer, drag each thumbnail image in the exam into a viewport in the Viewer window.

To load images into the Browser, double-click any thumbnail in the exam. The entire exam will be loaded.

Tip The same exam can be loaded into both the Viewer and Browser windows.

### Using Conditional Indicator Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad will place indicator icons in the upper-right corner of images to alert the user to certain conditions. These will appear in any viewport, regardless of the viewport’s parent window.

#### Image Compression Alert 

VistARad indicates a compressed image by displaying the Compression Alert icon ![](vistarad-user-guide/057.png). Right-clicking on the icon displays a context menu with two options:

- Clicking ‘Display Compression Details’ opens the Display Data tab of the Image Detail window. Compression details appear in the ‘Desc’ and ‘Value’ columns of the Display Data tab. For more details, see Using the Image Detail Window on page [69](#_Ref137003245).
- Click Hide Icon to hide the icon. It will re-display if the image, or the image set, is re-set with either “Reset” option available on the image context menu.

#### VOI LUT Indicator

VistARad indicates that an image has a Value Of Interest Look Up Table (VOI/LUT) applied by displaying the ![](vistarad-user-guide/058.png) icon in the upper-right corner of the image (the letters ‘LUT’ appear if the VOI/LUT is currently applied). By default, VistARad displays images with the first embedded VOI/LUT applied. Right-clicking the icon displays a context menu with other options listed, based on modality-supplied information:

1.  Click VOI Lut, if present, to see the VOI LUT(s) available within the image. A check is displayed next to the currently applied VOI LUT. You can select a different VOI LUT, if available, by clicking on its sub-menu text.
2.  Click Window/Level, if present, to see the Window/Levels available within the image. A check is displayed next to the currently applied Window/Level. Select a different Window/Level, if available, by clicking on its sub-menu text. Applying a Window/Level to the image will remove the “LUT” text from the ![](vistarad-user-guide/059.png) icon.
3.  Click Hide Icon to hide the icon. It will re-display if the image, or the image set, is re-set with either “Reset” option available on the image context menu.

> NOTE Window /Level adjustments applied to the image will nullify the effects of the VOI LUT.  To re-apply the VOI LUT, use the Reset Image option, or select the VOI LUT value from the context menu hosted on the ![](vistarad-user-guide/060.png) icon.

### Navigating in Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Viewports can contain one or more images. In viewports that contain multiple images, you can use the mouse or the viewport’s paging buttons to display each image in a viewport. Scout images, if available, can also be used.

As you work with images in a viewport, the relative position of the selected image is indicated by the I label in the upper right corner of the viewport, and by tick marks on the left side of the viewport.

To scroll through images

Scrolling lets you display successive images in a viewport. Use of a three-button mouse is assumed.

Point to the image you want to start scrolling from.

Do one of the following:

Roll the mouse scroll wheel up and down.[^3]

For a faster scroll, drag up and down using the middle mouse button.

To step through images one at a time

To move toward the beginning of an image set, point to the left side of an image, then click once using the middle mouse button or the scroll wheel.

To move toward the end of an image set, point to the right side of an image, then click once using the middle mouse button or the scroll wheel.

To page through images

Paging buttons are displayed in the top right corner of viewports that contain multiple images.

![](vistarad-user-guide/061.png)

To page forward, click ![](vistarad-user-guide/062.png). To page backward, click ![](vistarad-user-guide/063.png).

If the viewport is showing a single image (stacked mode), clicking a page button will move forward or backwards one image.

If the viewport is showing multiple images (tiled mode), clicking a button will step forward or backward based on the number of visible images.

To navigate using the keyboard

Select the viewport, then do one of the following:

- Press the Up Arrow or Left Arrow key to move toward the beginning of the image set.
- Press the Down Arrow or Right Arrow key to move toward the end of the image set.
- Press the Page Up or Page Down keys to move one page up or down (a page equals the number of images displayed in the viewport).

To use a scout image

When an exam is opened, any scout images in the exam are automatically loaded into the Scout Image window. If the Scout Image window is not visible, it can be displayed by clicking ![](vistarad-user-guide/064.png).

- If you loaded an exam in the Browser window, scout images are displayed in the left viewport.
- If a hanging protocol was used to open the exam, scout images may also be displayed in the Viewer window.
- You can click different parts of a scout image to display images in an associated series.

### Working with Images 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you progress through images in a viewport, you may want to:

Click ![](vistarad-user-guide/065.png) to mark an image as a key image (details below).

Double-click an image to switch to full-screen view (Viewer window only), or CTRL-right drag to change scale (details on page [74](#scaling-images)).

Click ![](vistarad-user-guide/066.png) to switch the viewport layout between stack and tiled views (details on page [80](#_Ref136930303)).

Adjust window/level by dragging over an image using the right mouse button (details on page [76](#_Ref136996619)).

Annotate or measure image features (details on page [93](#annotations)).

### Key Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Images of interest can be marked as “key images.” Marking an image as a key image creates an independent copy of the image that is displayed in the Scrapbook window.

- If an image in the Viewer is marked, the Mark icon near the top of the image looks like ![](vistarad-user-guide/067.png)
- If an image in the Viewer is not marked, the Mark icon near the top of the image looks like ![](vistarad-user-guide/068.png)

Once an exam is interpreted, key images become a permanent part of a patient’s record and they cannot be changed. When an exam containing key images is re-opened, the key images are loaded in the Scrapbook window automatically.

Key images marked in an exam that is not locked are discarded when the exam is closed.

To mark a key image

In the Viewer window, locate the image you want to mark (scout images cannot be marked).

Click the ![](vistarad-user-guide/069.png) icon located near the top of the viewport. The image is added to the Scrapbook window.

The image you marked will be saved as a key image when the exam is closed (if the exam is locked).

Key images marked in previous sessions may also be present in the Scrapbook.

Tip To prevent interference with images displayed in the Viewer, the Scrapbook window does not open automatically when an image is marked. To display the Scrapbook window, click ![](vistarad-user-guide/070.png).

Adjust or annotate the key image as desired in the Scrapbook.

Changes to key images are retained in exams that are locked (exams being interpreted in the current session).

Changes to key images are discarded in exams that are not locked.

To unmark a key image

Do either of the following:

Locate the marked image in the Scrapbook and click ![](vistarad-user-guide/071.png).

Locate the marked image in the Viewer and click ![](vistarad-user-guide/072.png).

Unmarking a key image in an exam that is locked will delete the key image from the Scrapbook permanently.

Unmarking a key image in an exam that is not locked will temporarily remove the image from the Scrapbook; to ensure that final medical records cannot be altered, the key image will be re-loaded into the Scrapbook the next time the exam is opened.

### Clearing Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove images from a viewport without closing the exam, click ![](vistarad-user-guide/073.png), located in the upper right corner of the viewport. When images are cleared any display changes made to the images (w/l, scale, etc.) are discarded.

An exam is considered open even if all viewports are cleared. You can reload viewports using the Preview window, or by closing and reopening the exam using a hanging protocol.

Note Clearing images from a viewport does not affect the ![](vistarad-user-guide/074.png) icon in the Preview window. This icon indicates that an image set was displayed at some point in the current viewing session, not that it is presently displayed.

### Switching between Patients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer, Browser, and other windows that display images are designed to show exams for only one patient at a time. The name of the ‘active patent’ is shown in the title bar of each of these windows.

![](vistarad-user-guide/075.png)

When exams for multiple patients are open, pressing \<Ctrl+P\> or clicking the Active Patient button opens a list that shows the names of each patient with open exams. Clicking a patient name will update the display of all windows to that patient. Exams for other patients, while still loaded, are not visible.

## Using the Preview Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preview window uses ‘thumbnail’ images to present a summary view of exams that are currently open. If the Preview window is not visible, it can be displayed by clicking ![](vistarad-user-guide/076.png).

The Preview window lets you load viewports manually when:

You want to view images in the Browser window (instead of the Viewer window).

You want to view images in an exam that was opened using a template only, or using a hanging protocol that cannot accommodate the structure of the exam.

You want to re-load a viewport that was cleared.

You want to view images from an additional exam associated with a patient who already has an exam displayed.

You want to create copies of images already loaded into the Viewer window.

To load viewports manually, you can drag thumbnails from the Preview window into the Viewer, or you can double-click a thumbnail to open the entire exam in the Browser window.

### Thumbnails and List View Explained 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each thumbnail in the Preview window represents an image, a group of images, or an entire exam. The number of images represented by a thumbnail is displayed in the title bar over each thumbnail, and the thumbnail image itself is derived from the first image in the image set represented by the thumbnail.

Thumbnails incorporate icons that let you note which parts of an exam have been loaded into viewports. For details, see Loading Viewports on page [55](#loading-viewports).

In addition to the thumbnail view, the Preview window incorporates a “List View.” In List View, a set of progress bars shows the loading status of all exams. Using List View, you can pause or resume the load of series (image sets) within an exam. You can also purge image sets to free up memory. See Managing the Exam Load Process on page [26](#_Ref248729184) for more detail on the use of List View mode.

Note VistARad will, by default, preview the CT and MR modalities in List View mode. You can override this and preview all modalities in thumbnail view by going to the Settings \| Hanging Protocol tab and checking ‘Display traditional thumbnails in the Preview window’.

### Customizing Thumbnail Sizes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The thumbnail image size in the traditional thumbnail view is fixed. However, a user preference allows you to use different sized thumbnail images in the List view.

To select a different thumbnail size, first close all currently opened exams. Click View \| Settings \| Hanging Protocol; then click the button Select Thumbnail Size. Drag the dialog box that opens to the same screen where you prefer to display the Preview window (to provide an accurate spatial reference), then select the radio button below the thumbnail size you prefer; click OK on that dialog, then OK on the Settings form. The new setting will be applied the next time an exam (CT or MR) is opened.

## Using the Viewer Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer window is the primary window used for diagnostic interpretation. Images are automatically loaded into the Viewer window when an exam is opened using a hanging protocol. You can also manually load images into viewports in the Viewer window (details on page [55](#loading-viewports)).

All standard image manipulations can be performed in the Viewer window (details on page [74](#_Ref137008011)). Stages and wide viewports are available only in the Viewer window.

### Using Stages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stages are an optional feature of hanging protocols. If a hanging protocol has more than one stage, you can use each stage to view different arrangements of the same exam (or exams) in the Viewer window.

Some hanging protocols will automatically select a particular stage for initial display based on the presence or absence of priors. Regardless of which stage is initially used, other stages can be viewed using the Stage button.

The Stage button is located in the upper right area of each monitor occupied by the Viewer window. It indicates if stages are present and which stage is being used.

![](vistarad-user-guide/077.png)

To move from one stage to another, click either side of the Stage button. Adjustments made to viewports or images will be retained as you move back and forth between stages.

### Wide Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Wide viewports are useful for reading some types of exams (such as x-ray or ultrasound exams) on multi-head workstations. With a wide viewport, an entire exam can be loaded into a single viewport while still taking advantage of the space offered by multiple screens. In almost all respects, a wide viewport functions like a standard viewport. All standard manipulation functions and tools are available.

If a wide viewport is present in the Viewer, it can be identified by the position of the paging buttons (![](vistarad-user-guide/078.png) ![](vistarad-user-guide/079.png)). In a wide viewport, paging buttons are located in the middle of the title bar. In a standard viewport, paging buttons are located on the right side of the title bar.

In a wide viewport, images are always tiled. At a minimum, as least one image per monitor is shown. Layout changes made in one monitor occupied by a wide viewport will be mirrored in all monitors occupied by that viewport (details on page [80](#_Ref136930303)).

To see how a wide viewport differs from a standard viewport, manually select the GenRad_2-hd_SYS_INT hanging protocol (details on page [137](#_Ref136748844)), then open a CR or DX exam. Stage 1 of this hanging protocol uses standard viewports. Stage 2 uses a single wide viewport.

### Hidden Exams and Image Sets in the Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Viewports that are automatically loaded by a hanging protocol can contain hidden exams or image sets. Hidden exams or image sets are used when:

There are more prior exams retrieved than there are available viewports.

Two or more image sets are deliberately placed in a viewport to keep the needed number of viewports small and the display size of each viewport as large as possible.

The Contents bar in each viewport will indicate if hidden exams or image sets are present. The Exam button located in the upper right part of the Viewer window will also indicate if hidden exams are present.

![](vistarad-user-guide/080.png)

To display a hidden image set

Click the S label in the Contents bar, then click one of the image sets displayed in the pop-up menu. If the viewport contains more than one exam, only image sets in the currently visible exam are listed in the pop-up menu.

![](vistarad-user-guide/081.png)

To display a hidden exam

Click the Ex label in the Contents bar, then click one of the exams displayed in the pop-up menu.

![](vistarad-user-guide/082.png)

You can also display hidden exams by clicking the left or right side of the Exam button. This will affect all viewports that contain hidden exams. If some viewports contain fewer hidden exams than others, a “viewport not empty” message may be displayed in one or more viewport title bars to keep the viewports in sync.

![](vistarad-user-guide/083.png)

### Using the Re-Hang Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can also apply a different hanging protocol to an exam that is already displayed in the Viewer. When this feature is used, images are not reloaded and no prior exam searching is performed; you are simply re-hanging images that were already loaded.

To re-hang a loaded image

With the image displayed in the Viewer, click the arrow to the right of ![](vistarad-user-guide/084.png) on the toolbar.

Click Select Hanging Protocol; the Select Hanging Protocol/Template window will display.

Click the hanging protocol you want to use from the displayed list; click OK.

## Using the Browser Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Browser window can be used as an alternative to the Viewer window when:

You want to display an additional exam without altering the display of exams in the Viewer.

You are working with both color and grayscale monitors. (The Browser window can be moved to the color monitor, and used for exams with color images.)

You are working with an exam that cannot be easily displayed using a hanging protocol.

Images can be loaded into the Browser window by double-clicking a thumbnail image in the Preview window. Once images are loaded in the Browser, most viewport features are similar to those available in the Viewer. For details, see Surveying Exams on page [55](#_Ref136316510).

When it contains images, the Browser window can be shown by clicking ![](vistarad-user-guide/085.png).

Key differences between the Browser and Viewer windows

Images are always loaded into the Browser window manually. In the Viewer, images can be loaded automatically (via a hanging protocol) or manually.

You can change the layout of viewports in the Browser by clicking ![](vistarad-user-guide/086.png) in the toolbar. In the Viewer, the arrangement of viewports is based on the active template and hanging protocol.

A viewport in the Browser can contain only a single group of images. In the Viewer, a viewport can contain multiple groups of images or multiple exams.

## Using the Scrapbook Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Scrapbook window contains images previously marked as key images or Teaching Files. If the Scrapbook window is not visible, it can be displayed by clicking ![](vistarad-user-guide/087.png).

An image in the Scrapbook window can be manipulated or annotated in much the same way as it would be in the Viewer or the Browser. But in the Scrapbook, annotations and changes to image properties (scale, window/level, etc.) are saved if the exam is locked. In other windows, annotations are saved but changes to image properties are lost when the exam is closed.

If the exam is not locked, changes made to images in the Scrapbook will be discarded when the exam is closed.

Images are added to the Scrapbook in two ways: by clicking ![](vistarad-user-guide/088.png) to mark them as key images in the Viewer (details on page [59](#_Ref213034482)) or by selecting the “Add to Teaching Files” option on the image context menu to mark them as teaching file images (details on page [194](#_Ref248714260)).

Note that in the Scrapbook, each viewport can contain only one image.

## Using Scout Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scout (localizer) images may display in different windows:

*In the Scout Image window* when an exam is opened. If the Scout Image window is hidden, it can be displayed by clicking ![](vistarad-user-guide/089.png) in the toolbar.

*In the Viewer* if they are part of an exam loaded using a hanging protocol or if they are manually loaded from the Preview window.

*In the Browser* if they are manually loaded by double-clicking the scout thumbnail in the Preview window.

VistARad projects cross-referencing slice lines on all applicable cross-sections of simultaneously displayed image sets. VistARad synchronizes them to the stack position of the active viewport. Changing the active viewport re-applies and re-synchronizes all reference slice lines. This is the default behavior, which can be changed from the context menu accessible from the right of the Scout Image window button.

Note This user preference setting persists until changed, even after VistARad is closed.

Note When the Show X-Ref Slice Lines menu item is unchecked, slice lines appear only on the Scout Image window. When the menu item is checked, slice lines appear on both VistARad Viewer and the Scout Image window.

An illustration of the context menu appears below.

![](vistarad-user-guide/090.png)

To navigate using a scout image

To navigate different parts of a series using a scout image, click in the active area of the scout.

Tip If the viewport that contains the associated series does not update, click the viewport, then click the scout image again.

### Generating Scouts Manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can manually generate a scout image for an exam if the exam has images on intersecting planes.

To generate a scout in the Viewer window

Note An empty viewport must be present to use this method.

In the Viewer window, display the image that you want to use as a scout.

Use the right mouse button to drag the image to an unoccupied viewport. A popup menu will display when you complete the drag.

Click Create Scout. The new scout image will be displayed in the Viewer window.

To display slice lines on the new scout, click any image from the same exam that is in a plane that intersects with the newly created scout.

To generate a scout in the Scout Image window

1.  Display the image that you want to use as a scout image.
2.  Right-click the image and click Create Scout.

    The image is copied into the Scout Image window. (The original image remains in the Viewer.)

    If the Scout Image window is not visible, access it by clicking ![](vistarad-user-guide/091.png) in the Viewer toolbar.
3.  To display slice lines on the new scout, click any image from the same exam that is in a plane that intersects with the newly created scout.

To customize slice lines

To change slice line settings, click View \| Settings \| Elements, then choose your options in the Scout Line Indicators area.

## Using the Image Detail Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Detail window is opened by clicking the information area at the bottom of an occupied viewport.[^4] Opening this window causes three tabs to display:

- The Full Header tab displays the entire DICOM header except for private elements and Look Up Tables
- The Display Data tab lists acquisition data for the selected image.
- The Image Data tab lists DICOM header data.

Information in the Image Detail window will be updated if you select a different image in the same viewport.

To close the Image Detail window, click ![](vistarad-user-guide/092.png), or click the information area that the window was opened from.

You can click ![](vistarad-user-guide/093.png) in the toolbar to open an instance of this window for each occupied viewport. Clicking ![](vistarad-user-guide/094.png) again will close all windows.

## Using the Imaging Data Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Imaging Data window is intended for troubleshooting and support. This window provides functionality similar to that available in Clinical Display. Note that some data is reserved to users holding the MAGJ SYSTEM MANAGER security key. Note that the Imaging Data window is independent of the “current patient” context in VistARad, and will not refresh when the current patient is changed. This window can be opened from the File menu in the Manager or the Viewer (shown below), or from the Stack icon ![](vistarad-user-guide/095.png) in an occupied viewport.

When the Imaging Data window is opened from an occupied viewport, data from the associated exam is used to populate the window.

![](vistarad-user-guide/096.png)

Data displayed in the window is fully editable, though copy is only enabled from the keyboard via \<Ctrl+C\>.

Once the window is opened, it can be used to examine other IENs or to look up CPT Matching logic.

Click the Lookup button to display matching logic for the CPT Code already filled-in (or enter a new one).

![](vistarad-user-guide/097.png)

Data from ^MAG(2005, may be displayed in global list format by clicking the ^MAG 2005 button:

> Display NODE: 5711

> ^MAG(2005,5711,0) PATIENT,ONETWOZEROTWO 000001202^DM005711.TGA^2^2^^3^1202^CR^3091209.15082^5710

> ^MAG(2005,5711,2) 3031124.1707^131^^112403-176 CHEST 2 VIEWS PA&LAT^3031124.1415

> ^MAG(2005,5711,40) RAD^1^75^111^29^V

Or in Field format by clicking the Field Values button:

> \*\*\*\*\*\* Fields for Image IEN: 5711 \*\*\*\*\*\*

> ACQUISITION SITE = (660) = SALT LAKE CITY

> BIG MAGNETIC PATH = (2) = MAG1H

> CLASS INDEX = (1) = CLIN

> DATE/TIME IMAGE SAVED = (3031124.1707) = NOV 24, 2003@17:07

> DISK & VOLUME, ABSTRACT = (2) = MAG1H

When the window initially opens with IEN data, global list format is displayed first, followed by field format. The Flags field, which can be left empty, can be used to pass FileMan Flags to the underlying LIST^DIC() call. Available flags are described in the FileManager User Manual.<span id="_Ref257049904" class="anchor"></span>

### Closing Exams & Updating Exam Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you have finished reviewing an exam, you can close the exam with or without updating its status.

| ![](vistarad-user-guide/098.png) | If an exam’s status is inappropriately updated, the Radiology Package must be used to revert the exam to its original status. |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

To close exams (standard)

Press \<Ctrl+Q\>, click ![](vistarad-user-guide/099.png) in the toolbar, or click Close Exams in the Manager window.

If the exam you are closing is locked, and if that exam contains images that have not been viewed, a warning message will display. You can:

Click Continue to close the exam without displaying the images in question.

Click Cancel Exam Close to go back to reviewing images.

Note An image set is considered “viewed” if it has been loaded into a viewport and has been “on top” (non-hidden) at some point in the current exam display session.

Tip You can disable this notification for the current session using the check box at the bottom of the dialog. You can also change this setting using the Prompts tab in the Settings dialog (View \| Settings).

For each exam listed in the dialog, note the value in the Interpret? column. Click the value to set it as desired:

YES – The exam’s status will be updated and your name is entered as the interpreting radiologist in the patient record. Any annotations or key images added in the current display session will be saved when the exam is closed.

NO – The exam’s status will not be updated. Any annotations or key images marked in the current display session will be discarded when the exam is closed.

N/A – The exam’s status cannot be changed; the exam is already interpreted or the exam was not locked when it was opened.

Tip Certain options can control the initial Yes/No value in the Interpret? column. For more information, see the Manager \| General tab settings on page [114](#manager_tab_general).

For each exam listed in the dialog, click the value in the Close? column to set the value to YES (close this exam) or NO (do not close this exam).

For each exam listed in the dialog, set the value of the Annotation Options in the Close Exams / Update Status Dialog on page [102](#annotation-options-in-the-close-exams-update-status-dialog) as appropriate.

Click OK when you have the settings you want, or click Cancel to close the dialog without affecting any open exams.

If VistARad is interfaced to a voice dictation system, close the report you are dictating before you open any additional exams.

If you updated the exam’s status, the exam you just closed is removed from the Unread Exams list.

An exam that has been recently interpreted can be re-opened using the Recent Exams, All Active Exams, or Exam History lists.

To close exams (ReadList)

If VistARad is interfaced to a voice dictation system, save and close your current report.

If the exam you are closing is locked, and if that exam contains images that have not been viewed, a warning message will display. You can:

Click Continue to close the exam without displaying the images in question.

Click Cancel Exam Close to go back to reviewing images.

Note An image set is considered viewed if it has been loaded into a viewport and has been on top (non-hidden) at some point in the current exam display session.

Tip You can disable this notification for the current session using the check box at the bottom of the dialog. You can also change this setting using the Prompts tab in the Settings dialog (View \| Settings).

Press \<Ctrl+Q\>, click ![](vistarad-user-guide/100.png) in the toolbar, or click Close Exams in the Manager window.

Your current settings will determine if the Close Exams/Update Status dialog displays.

If the dialog displays, set the Close and Interpret fields as described in the previous section.

If you have suppressed the display of the dialog, the default value specified for status updates is applied to the exam being closed. For details, see Setting up Automatic Close/Updates on page [21](#autoupdate_setup).

# Manipulating Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p>This chapter covers:</p>
<p>Changing Image Properties</p>
<p>Using Image Presets</p>
<p>Changing Layout</p>
<p>Using “Apply To”</p>
<p>Copying Properties</p>
<p>Linking Viewports</p></th>
<th><p>Cloning Image Sets</p>
<p>Moving and Splitting Image Sets</p>
<p>Sorting Image Sets</p>
<p>Using the Cine Tool</p>
<p>Using the Magnifying Glass</p>
<p>Mensurated Scale</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Changing Image Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can make the following changes to images displayed in viewports:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><p><a href="\l">Scale</a></p>
<p><a href="\l">Pan</a></p>
<p><a href="#_Changing_Window/Level">Window/Level</a></p>
<p><a href="\l">Invert</a></p></th>
<th><p><a href="\l">Orientation</a></p>
<p><a href="\l">Sharpness</a></p>
<p><a href="\l">Reset</a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Scaling Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An image can be dynamically zoomed from 5% to 800%, or it can be scaled to a specific percentage of its original size. You can also expand an image in the Viewer window to the size of an entire screen.

As an image’s scale is changed, the current scale percentage is shown in the image information area at the bottom of the viewport. Unless Apply To settings have been changed, scale changes affect all images in a viewport (details on page [81](#_Ref257058246)).

To change scale dynamically

Point to the image you want to scale, then drag with the right mouse button while pressing the \<Ctrl\> key.

Tip You can customize the operation assigned to the right mouse button (details on page [115](#_Ref169587605)).

You can also turn on the scale tool (click ![](vistarad-user-guide/101.png) in the toolbar or right-click any image, then click Scale) and change scale by dragging with the left mouse button.

Tip If you have image-adjustment shortcuts enabled, you can use the arrow keys to fine-tune scale adjustments (details on page [115](#_Ref169587605)) while the scale tool is active.

When you have finished using the scale tool, turn it off by right-clicking once.

To scale an image to a specific size

Click ![](vistarad-user-guide/102.png) in the toolbar; or right-click any image, then click Scale.

Point to the image you want to change and do any of the following:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To...</strong></th>
<th><strong>Do this...</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Scale image to 100%</td>
<td>Point near the top left corner of the viewport. When the mouse pointer changes to ![](vistarad-user-guide/103.png), click once.</td>
</tr>
<tr class="even">
<td>Scale image to<br />
fit viewport</td>
<td>Point near the top middle part of the viewport. When the mouse pointer changes to ![](vistarad-user-guide/104.png), click once.</td>
</tr>
<tr class="odd">
<td>Scale image to 50, 75, 125, 150, or 200%</td>
<td>Point near the top right corner of the viewport. When the mouse pointer changes to ![](vistarad-user-guide/105.png), click once. Then click a scale option in the menu that displays.</td>
</tr>
</tbody>
</table>

Tip While the scale tool is turned on, you can also zoom in or out by dragging with the left mouse button.

Continue using the Scale tool, or disable it by right-clicking once or by choosing another tool.

To use full-screen view

In the Viewer window, double-click an image. The image will expand to fill an entire screen.

While full-screen view is active, you can:

Adjust (window/level, flip/rotate, etc.) the current image.

Scroll to other images, or use the cine feature.

When you have finished, double-click the image to restore it to its original size.

Note Full-screen view is specific to the Viewer window. In other windows, you can quickly change the view to 1-up by clicking ![](vistarad-user-guide/106.png) in the toolbar.

### Panning images 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To pan an image, point to the image you want to pan and drag using the left mouse button. Note that images that are completely visible cannot be panned.

Tip If the image does not pan, right-click once to make sure that no other tools are active. (The mouse pointer looks like ![](vistarad-user-guide/107.png) when no tools are active).

### Changing Window/Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change an image’s window/level using the mouse, the keyboard, or a combination of both. You can also use the auto-window/level tool to base window/level values on a selected area in an image.

As an image’s window/level is changed, the area under the image updates to show the current window/level values. Unless Apply To settings have been changed, window/level changes affect all images in the viewport (details on page [81](#_Ref257100835)).

To change window/level

Point to the image you want to adjust and drag using the right mouse button.

Drag up or down to change window (window width) values.

Drag left or right to change level (window center) values.

You can also click ![](vistarad-user-guide/108.png) in the toolbar and change window/level by dragging with the left mouse button.

Tip If you have image-adjustment shortcuts enabled, you can use the arrow keys to fine-tune window/level settings (details on page 89) while the window/level tool is active.

When you have finished using the window/level tool, you can turn it off by right-clicking once.

To use the auto-window/level tool

Click ![](vistarad-user-guide/109.png) in the toolbar.

In the image you want to adjust, drag the mouse to define a rectangular area that includes the tissue you want to base the window/level on.

When the drag is completed, the new window/level values will be applied to the entire image.

Continue using the Auto-window/level tool, or disable it by right-clicking once or by choosing another tool.

### Inverting Grayscale Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can invert grayscale values to create a “negative” view of an image.

To invert an image

Click ![](vistarad-user-guide/110.png) in the toolbar, or right-click any image and click Invert.

Click the image you want to invert.

Continue using the Invert tool, or disable it by right-clicking once or by choosing another tool.

Tip Unless Apply To settings have been changed, invert affects all images in the viewport (details on page [81](#_Ref257100835)).

### Reorienting Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change an image’s orientation by rotating it 90 degrees or by flipping it front-to-back. As changes are made, any positional indicators displayed near the edges of the image are updated to reflect the new orientation. (This does not include markers that are burned into the image itself.)

Tip Unless Apply To settings have been changed, orientation changes all images in the viewport (details on page [81](#_Ref257100835)).

To rotate images 90 degrees

Click ![](vistarad-user-guide/111.png) in the toolbar, then point to the image you want to rotate.

To rotate the image counterclockwise, click on the left side of the image.

To rotate the image clockwise, click on the right side of the image.

Continue using the Rotate tool, or disable it by right-clicking once or by choosing another tool.

To flip images

Click ![](vistarad-user-guide/112.png) in the toolbar, then point to the image you want to flip.

To flip the image vertically, click on the top part of the image.

To flip the image horizontally, click on the bottom part of the image.

Continue using the Flip tool, or disable it by right-clicking once or by choosing another tool.

### Using Sharpen/Smooth 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can apply sharpen/smooth filters to an image. Unless Apply To settings have been changed, sharpen/smooth changes affect all images in the viewport (details on page [81](#_Ref257100706)).

The info area at the bottom of each viewport displays which filter is used, where F*+N* indicates a sharpen filter, and where F*‑N* indicates a smooth filter.

To sharpen or smooth an image

Click ![](vistarad-user-guide/113.png) in the toolbar; or right-click any image and then click Sharpen.

Point to the image you want to adjust and drag the mouse using the left mouse button.

To increase sharpness, drag up or left.

To decrease sharpness, drag down or right.

Continue using the Sharpen/smooth tool, or disable it by right-clicking once or by choosing another tool.

Tip If you have image-adjustment shortcuts enabled, you can use the arrow keys to fine-tune sharpen/smooth adjustments (details on page [115](#_Ref169587605)) while the sharpen/smooth tool is active.

### Resetting Images 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To restore the original window/level, scale, position (pan), and orientation of images in a viewport, right-click any image in the viewport and choose Reset \| Image Set.

Tip You can also click ![](vistarad-user-guide/114.png) to clear the viewport, and then reload the viewport manually.

## Using Image Presets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use image presets to quickly set display properties for a specific type of tissue. An image preset typically incorporates a specific window/level value, and can specify a specific sharpen/smooth setting.

Image presets can be applied to images in the Viewer, Browser, or Scrapbook windows. Image presets can also be applied automatically by including them in a hanging protocol definition.

You can define your own collection of image presets and access that collection from any VistARad workstation at your site. Your site may also define a collection of “site level” image presets for general use.

To apply an image preset

Do one of the following:

Right-click the image that you want to apply the preset to, point to Image Presets, then click an option in the submenu.

Press one of the function keys (F1, F2, etc.) to apply a preset. Key assignments, which are site-specific, are shown in the Image Presets submenu.

Tip Image presets are filtered by modality. For example, a preset associated with the CT modality will be available only for CT images.

Tip Unless Apply To settings have been changed, applying an image preset affects all images in a viewport (details on page [81](#_Ref257100835)).

To define or edit an image preset

In the Viewer menu, click Customize \| Presets.

To create a new preset, click New. To edit an existing preset, select a preset from the list at the top of the Image Presets Configuration dialog.

Use the options in the Image Preset Details area to define or modify the preset.

Name– The name of the preset.

Level– Disabled unless you hold the MAGJ SYSTEM USER security key. If enabled, choose *User-level* to define a preset for personal use, or choose *Site-level* to define a preset that can be accessed by all users.

Shortcut– Select a keyboard shortcut from the list to associate with the preset. Note that if the same keyboard shortcut is assigned to both a user-level and a site-level preset, the user’s shortcut takes precedence.

Modality– Select a modality from the list to associate with the preset. The preset will be available only when images of that modality are displayed.

Auto W/L– Select this check box to set initial window/level based on pixel values in the first image in the exam or image group.

Set W/L Value– Select this check box to enter specific values in the Window and Level boxes.

Sharpen– If desired, select a sharpen filter. Positive values increase the sharpness and negative values decrease the sharpness.

Invert– If desired, select the check box to invert the image.

Click Update to save your changes, then click Cancel to close the dialog.

To delete an image preset

In the Viewer menu, click Customize \| Presets.

In the Image Presets dialog, select a preset, then click Delete.

You can delete an image preset if you are the creator of that preset.

If you hold the MAGJ SYSTEM USER security key, you can delete site-level presets associated with the sysAdmin user.

You cannot delete other user’s presets, or presets that are referenced in a hanging protocol definition.

Click Yes when you are asked to confirm the operation.

## Changing Layout 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can specify the layout (number of rows and columns) in a window and in each viewport. The layout of each viewport or window can be set independently.

To use full-screen view (Viewer only)

In the Viewer window only, you can double-click an image to expand it to fit the current screen.

While you are in full-screen view, you can adjust the image or scroll to other images.

When you have finished, double-click again to return to the original screen layout.

If viewport navigation shortcut keys are enabled, you can also press \<F\> to turn full-screen view on or off. To turn on viewport navigation keys, select View Settings \| Mouse/Shortcuts, then select the Enable viewport navigation shortcut keys check box.

To change layout in a viewport

In the upper left corner of a viewport, click ![](vistarad-user-guide/115.png) and drag down using the mouse.

In the box that displays, move the mouse until the desired number of rows and columns are highlighted, then click the left mouse button.

Layout cannot be changed if the viewport contains only one image.

Layout changes affect the active image set only. Hidden image sets are not affected.

Tip In the Viewer window only, a viewport may stretch across multiple monitors. If this is the case, the layout will be at least equal to 1 x *n*, where *n* is the number of monitors that the viewport extends across.

To change layout in a window

These steps can be used for any window except the Viewer window. In the Viewer window, layout is dictated by the active template.

In the toolbar, click ![](vistarad-user-guide/116.png) and drag down using the mouse.

In the box that displays, move the mouse until the desired number of rows and columns are highlighted, then click the left mouse button.

Tip To switch back and forth between 1-up and the last layout you selected, click ![](vistarad-user-guide/117.png).

## Using “Apply To”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Apply To settings determine if changes to properties such as scale, window/level, and orientation affect all images in a viewport or the selected image only. Apply To settings can be altered on a viewport-by-viewport basis.

To check Apply To settings for a property

Turn on the appropriate tool (such as the Scale tool).

In the viewport of interest, note the state of the Apply To icon.

When the icon looks like this: ![](vistarad-user-guide/118.png), using the active tool will affect the selected image only.

When the icon looks like this: ![](vistarad-user-guide/119.png), using the active tool will affect all images in the viewport.

Note Apply To can be set independently for each property. The state of the Apply To icon reflects only the property related to the active tool.

To check Apply To settings for all properties

Click the ![](vistarad-user-guide/120.png) icon.

Drag down to open the pull-down menu.

A property marked with a check mark indicates that changes to that property will affect all images in a viewport.

A property that does not have a check mark indicates that changes to that property will affect the selected image only.

To change Apply To settings

Turn on the tool (window/level, scale, etc.) that you want to change Apply To settings for.

In the viewport where you want to change Apply To settings, click the Apply To icon.

When the icon looks like this: ![](vistarad-user-guide/121.png), using the active tool will affect the selected image only.

When the icon looks like this: ![](vistarad-user-guide/122.png), using the active tool will affect all images in the current image set.

Tip You can also change Apply To settings by dragging down on the ![](vistarad-user-guide/123.png) icon to open the pull-down menu, and then clicking a property to add a checkmark (apply changes to all images) or to remove a check mark (apply changes to current image only).

To set initial Apply To settings

In the Viewer or Manager menu bar, click View \| Settings, then click the Viewport tab.

For each adjustment property listed in the Apply To Options area:

Select the check box if you want changes to that property to affect all images in the viewport.

Clear the check box if you want changes to that property to affect only the selected image.

Click OK. Note that initial Apply To settings in a viewport can be overridden by the active hanging protocol.

## Copying Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can copy properties such as window/level, scale, position (pan), and orientation from one viewport to another. You can copy several properties at once, or copy a single property only.

To control which properties are copied

In any occupied viewport, click ![](vistarad-user-guide/124.png) and drag down to open the pull-down menu.

A check mark indicates properties that will be copied.

The absence of check mark indicates properties that will not be copied.

Select a property to add or remove a checkmark. The settings you choose affect all viewports in all windows, and will be retained for the duration of your session.

To copy properties (Copy icon)

Select the image with the properties that you want to copy.

Click ![](vistarad-user-guide/125.png) in the source viewport.

Click an image in the target viewport.

The target viewport must be in the same window as the source viewport.

Apply To settings in the target viewport determine if all images are changed, or if only the image that was clicked is changed (details on page [81](#_Ref257100835)).

Continue using the Copy tool, or disable it by right-clicking once or by choosing another tool.

To copy properties (mouse drag)

Select the image with the properties that you want to copy.

Using the right mouse button, drag the title bar of the source viewport to the target viewport.

After completing the drag, click Copy Attributes.

Note Apply To settings in the target viewport determine if all images are changed, or if only the image that was clicked is changed.

To set initial copy settings

In the Viewer or Manager toolbar, click View \| Settings, then click the Viewport tab.

In the Copy Options area, select each property that will be copied when the Copy Properties feature is used.

Click OK.

## Linking Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Viewports in the Viewer and Browser windows can be linked. When viewports are linked, scrolling and paging changes made in one viewport affect all linked viewports. Changes to scale, orientation, etc. performed in one viewport can affect all linked viewports as well.

When viewports are linked, the Link icon located near the top of the viewport looks like ![](vistarad-user-guide/126.png). When viewports are not linked, the link icon looks like ![](vistarad-user-guide/127.png).

While there is no limit on how many viewports can be linked, all linked viewports must be in the same window. When images are loaded into the Viewer using a hanging protocol, one or more viewports may be linked automatically.

To link viewports

If the viewports being linked contain images from different exams, select anatomically equivalent areas in each viewport before creating the link.

In one of the viewports you want to link, click ![](vistarad-user-guide/128.png).

Click each viewport you want to link. As the link is established, the Link icon will change to look like ![](vistarad-user-guide/129.png).

When you have finished, right-click once to turn off the link function. Links will be retained until the exam is closed or until the link is explicitly removed.

Scroll or adjust the contents of one of the linked viewports as desired. Changes will be reflected in all linked viewports.

| ![](vistarad-user-guide/130.png) | If the linked viewports contain images from the same exam (i.e., all images have the same Frame of Reference UID), each viewport will show the same anatomy as you scroll or page through images in the linked viewports. |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

To unlink viewports

Use either of the following methods:

Point to the viewport you want to unlink, press the \<Ctrl\> key, then click ![](vistarad-user-guide/131.png).

In the viewport you want to unlink, click ![](vistarad-user-guide/132.png) and drag down a short distance with the mouse. Then click Unlink.

To control which properties are linked

In a linked viewport, click ![](vistarad-user-guide/133.png) and drag down to open the pull-down menu.

A check mark indicates that changes for a particular property will be applied across all linked viewports.

The absence of a check mark indicates that changes for a particular property will be applied to the current viewport only.

Select a property to add or remove a checkmark.

The settings you choose affect all linked viewports until the viewports are cleared.

If there are multiple links active, settings for each link group can be set independently.

To set default link settings

In the Viewer or Manager toolbar, click View \| Settings, then click the Viewport tab.

In the Link Options area, select each property that, when changed, will affect all linked viewports.

Click OK.

Note In the Viewer window, initial link settings can be overridden by the active hanging protocol.

Overriding the Frame of Reference UID

If you need to link series that were inappropriately assigned the same Frame of Reference UID when they were acquired, you can override the Frame of Reference UID and then link the series manually. To do this:

In the upper left corner of any viewport, click ![](vistarad-user-guide/134.png), then drag to open the pull-down menu.

Point to Link Options, then click Link Manual.

| ![](vistarad-user-guide/135.png) | This setting affects all viewports in the Viewer and the Browser for the duration of your session, or until you change the setting back to Link Auto. |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

Use the steps above to link two or more series as desired. Be sure to display the equivalent images in each series before initiating the link.

## Cloning Image Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create multiple copies (clones) of images in Viewer or the Scrapbook.

Tip After you create clones of images, you can link them, and then page/scroll through both clones at once (details on page [84](#_Ref136930307)).

To clone images (Viewer or Scrapbook)

Using the right mouse button, drag the title bar of the viewport with the images you want to clone into an unoccupied viewport.

Click Clone in the popup menu that displays.

You can clone an image set as many times as there are available viewports.

Cloned images in the Viewer window are discarded when the exam is closed.

Cloned images in the Scrapbook window are saved as key images when the exam is closed, provided that the exam is locked.

To clone images (Viewer only)

Click ![](vistarad-user-guide/136.png) to display the Browser and Preview windows.

Locate the viewport (or thumbnail, in the Preview window) that contains the images to be cloned.

Click the title bar of the viewport or thumbnail, and drag it into an empty viewport in the Viewer window.

You can clone an image set as many times as there are available viewports.

Cloned image sets are discarded when the exam is closed.

## Moving and Splitting Image Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Images can be moved from one viewport to another. In the Viewer window only, you also can split the contents of one viewport into two viewports.

To move images (Scrapbook or Browser)

In the viewport that contains the images you want to move, point to the viewport title bar.

Drag the images to a different viewport.

If the target viewport is occupied, the images being dragged are inserted into the target viewport and the pre-existing images are shifted to the left.

If the target viewport is unoccupied, the images being dragged are moved to the last open position in the window (where images wrap from left to right, then top to bottom).

To move images (Viewer only)

Locate the viewport you want to use as the target viewport.

The target viewport can be empty, or it can contain a single image set.

The target viewport cannot contain more than one image set. The Contents bar in the upper right corner indicates how many image sets (series) are present.

Drag the title bar of the viewport that contains the images you want to move into the target viewport.

If the source viewport contains any hidden image sets, the next hidden image set is displayed when the move is completed.

If the target viewport was previously occupied, your current drag and drop settings determine if the contents of the target viewport are swapped or replaced.

Tip To explicitly select if a “swap” or “replace” occurs, use the right mouse button while dragging images to another viewport occupied by a single image set.

To set drag and drop options (Viewer only)

In the Viewer or Manager toolbar, click View \| Settings, then click the Viewport tab.

In the Drag and Drop Options box, select either Swap or Replace.

Click OK.

To split an image set (Viewer only)

Ensure that there is an unoccupied viewport available in the Viewer window.

In the viewport that you want to split, select the image that will be the first image in the *new* image set.

Note You cannot perform a split if you have selected the first image, or if the image set contains only a single image.

Using the right mouse button, drag the title bar of the viewport to an unoccupied viewport. A popup menu will display.

Click Split. The image you selected and all images after that point will be moved to the new viewport.

An image set can be split more than once.

To recombine image sets, click ![](vistarad-user-guide/137.png) to clear the viewports, then re-load the image set by dragging it from the Preview window into an empty viewport.

## Sorting Image Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Images in a viewport are automatically sorted based on information from the acquisition modality. If necessary, you can override the default sorting used and set your own sort order.

To change sort parameters

In the viewport that contains the images to be sorted, click ![](vistarad-user-guide/138.png) and drag down to open the pull-down menu, then click Sort.

In the Set Sort Options dialog, use the Add and Delete buttons to edit the list on the right side of the dialog.

Optionally, select each sort parameter you are using and use the Direction box to set the sort to Increasing or Decreasing.

Click OK. The sort you specified will be applied to the current image set.

Any hidden image sets will not be affected.

The sort you specified will remain active until the viewport is cleared.

## Using the Cine Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cine tool lets you rapidly display each image in a viewport in a repeating sequence. The cine tool is available in any viewport that contains more than one image. Changes window/level, scale, etc. can be made while the cine tool is running.

To start & stop the cine tool

If there are multiple images visible in the viewport (tiled view), click the image that you want to use as a starting point.

Click ![](vistarad-user-guide/139.png), located in the upper left corner a viewport.

When you have finished, click ![](vistarad-user-guide/140.png) to stop the cine tool.

To set cine speed

Open the cine pull-down menu by clicking ![](vistarad-user-guide/141.png) or ![](vistarad-user-guide/142.png) and dragging down with the mouse.

Point to Speed, then click Low, Medium, or High.

Tip To set the default cine speed, click View \| Settings \| Viewport, then choose an option from the Cine Speed box.

To set cine direction

Open the cine pull-down menu by clicking ![](vistarad-user-guide/143.png) or ![](vistarad-user-guide/144.png) and dragging down with the mouse.

Point to Direction, then click LoopForward, LoopReverse, or Yoyo.

The direction you choose will take effect immediately, including any currently running cines.

All viewports are affected by the change.

Tip To set the default cine direction, click View \| Settings \| Viewport, then choose an option from the Cine Direction box.

To set the cine range

If the cine tool is running, stop it by clicking ![](vistarad-user-guide/145.png).

Display the image that will be the first image in the cine range.

Open the cine pull-down menu by clicking ![](vistarad-user-guide/146.png) and dragging down with the mouse. Point to Range, then click First Cine Image.

Display the image that will be the last image in the range.

Open the cine pull-down menu by clicking ![](vistarad-user-guide/147.png) and dragging a short distance with the mouse. Point to Range, then click Last Cine Image.

Tip A different cine range can be set for each displayed image set.

To reset the cine range

Open the cine pull-down menu by clicking ![](vistarad-user-guide/148.png) or ![](vistarad-user-guide/149.png) and dragging down with the mouse.

Point to Range, then click Reset.

## Using the Magnifying Glass

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Magnifying Glass lets you enlarge a specific area in an image. The magnified portion of the image can be manipulated independently from the rest of the image. A shutter (mask) feature is also available.

The Magnifying Glass is available in the Viewer window only.

To add a Magnifying Glass

In the Viewer window, locate the image you want to use the Magnifying Glass in.

Right-click the image, then click Magnifying Glass.

Note The Magnifying Glass is not available for scout images. The Magnifying glass will turn off automatically if any annotations are added.

To move a Magnifying Glass

Confirm that the mouse pointer looks like ![](vistarad-user-guide/150.png). If it does not, right-click once to turn off any active tools.

Point inside the magnified area, and drag it to the desired location.

To resize a Magnifying Glass

Click the one of the boundaries of the magnified area, then point to one of the handles that display.

When the pointer looks like ![](vistarad-user-guide/151.png), drag to resize the magnified area.

To change image display properties in a Magnifying Glass

Right‑click inside the magnified area, then click one of the options displayed in the shortcut menu.

Drag (or click, for Invert) inside the magnified area to make your changes. You do not have to remain inside the magnifying glass borders after you begin dragging.

When you have finished, right-click once to turn off the active tool.

Tip To change window/level, just right-drag inside the magnified area.

To use the Magnifying Glass shutter

To limit your field of view to only the area contained in the Magnifying Glass, right-click inside the magnified area and click Shutter.

When you want to restore the rest of the image, right-click inside the magnified area and click Shutter again.

To remove a Magnifying Glass

Right‑click inside the magnified area, then click Delete Magnifying Glass.

To set initial scale in the Magnifying Glass

In the Manager or Viewer main menu, click View \| Settings. Then click the Element tab.

In the Initial Scale box, click the scale percentage you want to use.

Click OK.

## Mensurated Scale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an image is displayed, a mensurated scale can now be displayed on the left side of the image’s viewport. The scale uses pixel size data in the image header. If there is no pixel size data available for the image, you can use VistARad’s Calibrate tool to establish a pixel size. For details, see Using Calibrate on page [99](#using-calibrate).

![](vistarad-user-guide/152.png)

To display the mensurated scale:

1.  With an image in the viewport, right-click to display the Context menu.
2.  Click the Mensurated scale option from the menu. The scale will display to the left of the image.

To remove the mensurated scale from view:

1.  Right-click the image to display the Image Context menu,
2.  Click the Mensurated scale option, and the scale will no longer be visible.

# Annotations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Annotation Basics

Adding Shapes and Labels

Adding Measurements

Using the Hounsfield Tool

Working with Annotations

Using Show/Hide

Using Calibrate

Setting Annotation Properties

Saving Annotations

Overriding Annotations in Interpreted Exams

## Annotation Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use annotations to call attention to areas of interest in an image. You can also add text labels or measure image features.

## Adding Shapes and Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can add lines, shapes, and text to an image. You can also use the Auto Number tool to quickly add sequential numeric, alphabetic, or spinal labels to an image.

Note If you want annotations to be saved, make sure the exam is locked before adding annotations.

Tip Any hidden annotations in an image are displayed when you select an annotation-related tool.

![](vistarad-user-guide/153.png)

To add lines and arrows

Use the Annotation button in the toolbar to turn on the Line or Arrow tool.

Click to set the start point of the line, drag the mouse, and release the mouse button when the line or arrow is the desired length.

You can add additional annotations, select a different tool, or right-click once to turn off the active tool.

To add rectangles and ellipses

Use the Annotation button in the toolbar to turn on the Rectangle or Ellipse tool.

Drag the mouse to draw the line or shape. An outline will be shown as you drag the mouse.

Release the left mouse button when the outlined area is the desired size.

You can add additional annotations, select a different tool, or right-click once to turn off the active tool.

To add freehand shapes

1.  Use the Annotation button in the toolbar to turn on the Free Hand tool.
2.  Outline the area of interest by clicking three or more spots around its area.
3.  Right-click once to stop adding handles.
4.  Continue adding a new freehand shape, or right-click a second time to turn off the tool.
5.  To make adjustments to the freehand shape, enable edit mode, then drag the handles as needed. See To edit annotations on page [98](#to-edit-annotations) for more details.

To add text labels

Turn on the Text tool by doing one of the following:

Click ![](vistarad-user-guide/154.png) in the toolbar.

If the button noted above is not visible, click the arrow next to the Annotation button ( ![](vistarad-user-guide/155.png) ), then click Text.

In the image you want to annotate, drag the mouse to define a box that will contain the text. When you complete the drag, a blinking cursor is displayed in the box. Type the text that you want to appear in the box.

The text you enter will wrap, based on the width of the box.

You can copy text to and from the text box using \<Ctrl+C\> and \<Ctrl+V\>.

To add a line break, use the \<Enter\> key.

Click once outside of the box to finalize your edits.

You can add additional annotations, select a different tool, or right-click once to turn off the active tool.

To add auto numbers

Turn on the Auto Number tool by doing one of the following:

Click ![](vistarad-user-guide/156.png) in the toolbar.

If the button noted above is not visible, click the arrow next to the Annotation button (![](vistarad-user-guide/157.png)), then click Auto Number.

In the Auto Number dialog that displays, click the buttons that correspond to the numbering style and starting point you want to use.

Click each point in the image where you want a number to appear.

Add additional numbers, select a different tool, or right-click once to turn off the active tool.

Note Spinal labels are incremented from C1 to L6. After L6 is used, auto‑numbering is turned off automatically.

## Adding Measurements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can measure lengths, areas, angles, and Hounsfield values in an image. If you want measurements to be saved, make sure the exam is locked before adding measurements.

Tip Before measuring a small image feature, increase the scale of the image to improve the placement of the measurement.

To measure lines

Click ![](vistarad-user-guide/158.png) in the toolbar. Or right-click an image and choose Measure \| Length.

Note If the mouse pointer changes to ![](vistarad-user-guide/159.png), you will need to use the Calibrate tool before proceeding (details on page [99](#using-calibrate)).

Point to the part of the image from which you want to begin measuring.

Drag the mouse to create the measurement line. Once you have finished dragging, a label will appear next to the line, displaying the measurement.

Drag the text results to reposition as needed.

Note If the measurement label includes a (c) or a (c\*) label, the measurement is based on a manual calibration, rather than on a modality-defined pixel size.

Continue adding measurement lines, or right-click once to turn off the tool.

To measure angles

Click ![](vistarad-user-guide/160.png) in the toolbar , or right-click an image and choose Measure \| Angle.

Drag the mouse to draw the first line of the angle. The second line of the angle is automatically created.

Drag either or both lines by their handles to adjust the angle

Drag the text results to reposition as needed.

Continue adding angles, or right-click once to turn off the tool.

To measure Cobb angles

Click ![](vistarad-user-guide/161.png) in the toolbar, or right-click an image and choose Measure \| Cobb Angle.

Starting with the top-most line to be drawn, drag the mouse to create the line. The program automatically creates the second line.

Reposition the lines as needed by dragging the handles. Drag the text results to reposition as needed.

Continue adding angles, or right-click once to turn off the tool.

## Using the Hounsfield Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hounsfield tool offers the capabilities to measure areas captured in rectangles or freehand shape.

To measure rectangular

Select the area to be measured.

Click to set the start point of the rectangle.

Drag the mouse, and release the mouse button when the rectangle covers the desired area.

Drag the end-points of the perpendicular lines as needed to adjust.

Drag the text results to reposition as needed.

Continue adding Hounsfield measurements, or right-click once to turn off the tool.

To measure freehand areas

Outline the area to be measured by clicking three or more spots around its area.

Right-click once to stop adding handles.

Continue adding a new freehand measurement, or right-click a second time to turn off the tool.

To make adjustments to the measurement, enable Edit mode, then reposition the text results or drag the handles as needed. See To edit annotations on page [98](#to-edit-annotations) for more details.

## Working with Annotations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To show or hide annotations

Right-click the image, then choose Show Session Annotations, Show Stored Annotations, or Show All Annotations.

Or click the downward arrow on the right of ![](vistarad-user-guide/162.png) on the toolbar, and select from the same choices, as shown above.

#### To move annotations 

Click ![](vistarad-user-guide/163.png) in the toolbar, then click ![](vistarad-user-guide/164.png) near the annotation you want to move. Or right-click the annotation, and choose Edit Annotation.

Once you have finished, you can resize, move, or edit other annotations, or you can right-click once to turn off the tool.

#### To resize annotations

Click ![](vistarad-user-guide/165.png) in the toolbar, then click ![](vistarad-user-guide/166.png) near the annotation you want to resize. Or right-click the annotation, and choose Edit Annotation.

Drag any of the sizing handles to change the size of the annotation.

![](vistarad-user-guide/167.png)

Once you have finished, you can resize, move, or edit other annotations, or you can right-click once to turn off the tool.

#### To edit annotations

Click ![](vistarad-user-guide/168.png) in the toolbar, then click ![](vistarad-user-guide/169.png) near the annotation you want to edit. Or right-click the annotation, and choose Edit Annotation.

Note Only one annotation at a time in an image can be unlocked for editing. Clicking ![](vistarad-user-guide/170.png) on an annotation releases only that particular annotation from its locked state.

Make the changes you want to the annotation by clicking and dragging handles in a drawing tool, or clicking and dragging endpoints in a line.

Note While in Editing mode, the arrow drawing tool has handles to drag for repositioning and re-sizing. However, to facilitate precise measurement, the length-measurement tool does not. When the cursor hovers at the line’s endpoint, crosshairs will display to show the cursor is in the correct position for clicking and dragging the line.

Right-click once to turn off the tool.

To edit text labels

1.  Click ![](vistarad-user-guide/171.png) in the toolbar to turn on the Select Annotation tool, or right-click the text annotation you want to edit.
2.  Double-click the text annotation.
3.  Edit the text.
4.  Click once outside the text annotation to finalize your edits.
5.  Once you have finished, you can resize, move, or edit other annotations, or you can right-click once to turn off the tool.

## Using Show/Hide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction to layers

Three different layers (views) are available to you for seeing annotations you or others have made to images. You can elect to see all annotations, or only the ones that were made and saved by a prior user, or only the ones you have made. The show/hide button, directly to the left of the Annotations button, has three different ways to look on the toolbar, depending on which display layer you have selected most recently.

![](vistarad-user-guide/172.png)

Showing and Hiding Annotations

Right-click the image, then choose Show Session Annotations, Show Stored Annotations, or Show All Annotations.

Or click the downward arrow on the right of ![](vistarad-user-guide/173.png), and select from the same choices, as shown above.

## Using Calibrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Calibrate tool displays automatically if you try to measure an image that does not have a modality-defined pixel size. If the image in question has an embedded measurement scale, you can use the embedded scale and the Calibrate tool to set a pixel size manually.

If the Calibrate tool has been used, measurement values will display one of the following:

A (c) label indicates that pixel size was set manually.

A (c\*) label indicates that a manually defined pixel size has been used to override a modality-defined pixel size.

To use the Calibrate tool

If the Calibrate tool is not already turned on, click ![](vistarad-user-guide/174.png) in the viewport and drag down to open the pull-down menu, then click Calibrate.

While the mouse pointer looks like ![](vistarad-user-guide/175.png), draw a line between the two points that you want to use to establish a measurement standard.

The Calibrate Image dialog will display as you start drawing the line.

If the line is not ideally placed, you can re-draw the line.

In the Calibrate Image dialog, enter the length of the line that you drew, and then choose the unit length (centimeters, millimeters, or inches).

Check the Apply to Image Set check-box if you want this calibration to be used for all images in the image set; otherwise, the calibration will apply to the individual image only.

Click OK.

Tip To remove calibration settings for a viewport, clear and reload the image in the viewport.

## Setting Annotation Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can customize the line and font styles used for marking up images. You can also set the measurement units used.

To change line properties

In the Manager or Viewer main menu, click View \| Settings. Then click the Element tab.

In the Annotation area:

Use the Line Thickness box to set the line weight for all annotations.

Use the Line Color to set the line color for all annotations.

Click OK.

To change font properties

In the Manager or Viewer main menu, click View \| Settings. Then click the Element tab.

In the Text area:

Select or clear the Show Text Outline check box to show or hide the bounding box for annotation text.

Use the Font box to select font, style, size, and color.

Click OK.

To set measurement units

In the Manager or Viewer main menu, click View \| Settings. Then click the Element tab.

In the Measurement and Annotation area, use the Measurement Units box to choose centimeters, millimeters, or inches.

Click OK.

## Saving Annotations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you annotate images in a locked exam, you decide whether to save or discard them. If you annotate images in an exam that is *not* locked, the annotations are discarded when the exam is closed.

In the Viewer and Browser windows, only annotations added to the “first” copy of an image can be saved. If you want to annotate multiple copies of the same image, use the Scrapbook window.

## Overriding Annotations in Interpreted Exams 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you hold the MAGJ OVERRIDE ANNOTATIONS security key, you can override and alter annotations in completed exams, as follows:

Right-click the completed exam of interest in the Manager window, and choose Open/Annotation Override.

After the exam opens, make any desired additions or other changes to the annotations.

Click ![](vistarad-user-guide/176.png) in the Viewer toolbar to close the exam.

The options for the Annotations columns will vary, based on a combination of factors, including default user preferences in the Annotations frame of the VistARad Settings’ Prompts tab. These are described more fully in the next section.

Click the desired choice and click OK.

Click Store Annotations in the Close Exams/Update Status dialog.

## Annotation Options in the Close Exams / Update Status Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes the possible entries in the Annotations column of the Close Exams / Update Status dialog:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 35%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Conditions for Display</strong></th>
<th><strong>Description of Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">N/A</td>
<td>Images loaded without annotations, and no annotations were applied during review.</td>
<td>None taken.</td>
</tr>
<tr class="even">
<td>Annotations were applied to an unlocked image.</td>
<td>Annotations applied to an unlocked image are discarded.</td>
</tr>
<tr class="odd">
<td>Save Annotations Only</td>
<td>Images loaded without annotations, and annotations were applied during review.</td>
<td>The newly applied annotations are saved as presentation state data.</td>
</tr>
<tr class="even">
<td rowspan="3">Delete All Annotations</td>
<td>Images loaded without annotations, and annotations were applied during review.</td>
<td>The newly applied annotations are discarded.</td>
</tr>
<tr class="odd">
<td>Images loaded with annotations, and no annotations were applied during review.</td>
<td>The incoming annotations’ presentation state data are deleted from the server.</td>
</tr>
<tr class="even">
<td>Images loaded with annotations, and annotations were applied during review.</td>
<td>Both of the above.</td>
</tr>
<tr class="odd">
<td>Revert to Stored Annotations</td>
<td>Images loaded with annotations, and annotations were applied during review.</td>
<td>The newly applied annotations are discarded. The incoming annotations’ presentation state data are retained on the server.</td>
</tr>
<tr class="even">
<td>Merge Session and Stored Annotations</td>
<td>Images loaded with annotations, and annotations were applied during review.</td>
<td><p>The incoming annotations’ presentation state data are retained on the server.</p>
<p>The newly applied annotations’ presentation state data are appended to the existing data.</p></td>
</tr>
</tbody>
</table>

Two typical combinations of drop-down options are shown below. In the first example, there were annotations associated with the exam upon open, and no new annotations were applied during review. The “Revert to Stored” action, in this case, actually does nothing and thus preserves the existing data on the server. (The same is true if an incoming annotation gets modified: “Revert to Stored” will essentially undo the edits made during the reviewing session.)

> ![](vistarad-user-guide/177.png)

In the second example, there were annotations associated with the exam upon open, and new annotations were applied during review. “Merge Session and Stored” will add the new annotations’ data to what is already stored. The next time this exam is opened, the sum of the separate application events is displayed as a whole.

> ![](vistarad-user-guide/178.png)

# VistARad and Voxar 3D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Overview

Loading Images from VistARad into Voxar

Voxar Features Linked to Security Keys

Saving a Voxar Capture to VistA

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Voxar 3D Workstation is a third-party application used to display volumetric images. Voxar and VistARad can be installed and used on the same workstation. When both applications are properly configured, an image set or exam in VistARad can be opened in Voxar in a single step.

Depending on the configuration and the security keys you have, when images are loaded into Voxar, you may be able to print, copy, export or save image views generated in Voxar.

Note It is assumed that the VistARad/Voxar interface has been properly configured. Contact your Imaging Coordinator for information about what features are available at your workstation.

## Loading Images from VistARad into Voxar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistARad, open an exam and display the images of interest.

In the viewport containing the images you want to load into Voxar, right-click and choose View 3D to load that image set, or choose View 3D All Series to load the entire exam.

Note VistARad tracks which images have been sent to Voxar. The same image cannot be loaded into Voxar twice.

Manipulate the images as desired in Voxar.

When you have finished, click Discard and Finish in the Voxar Reading Manager.

## Voxar Features Linked to Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain features in Voxar 3D are available only if you have the correct security key.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Feature</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Copy to Clipboard</td>
<td>Requires the MAGJ VOXAR COPYIMAGE security key. Refer to Voxar documentation for details about using this feature</td>
</tr>
<tr class="even">
<td>Export-related features</td>
<td>Requires the MAGJ VOXAR EXPORTCAPTURE security key. Refer to Voxar documentation for details about using this feature</td>
</tr>
<tr class="odd">
<td>Print-related features</td>
<td>Requires the MAGJ VOXAR PRINTCOMPOSER security key. Refer to Voxar documentation for details about using this feature</td>
</tr>
<tr class="even">
<td>Finish and Archive (save image to VistA)</td>
<td><p>Requires the MAGJ STORE IMAGES security key.</p>
<p><strong>Note</strong> An issue in the Voxar software makes this button appear enabled even if you do not hold the proper key. To use this feature, all requirements described in the next section must be met.</p></td>
</tr>
</tbody>
</table>

## Saving a Voxar Capture to VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image views generated in Voxar 3D can be saved back to VistA as a separate series. These new images become part of the patient’s permanent medical record. To use this feature, you must hold the MAGJ STORE IMAGES security key.

Note This feature is available only if both VistARad and the DICOM Gateway are properly configured. Contact your Imaging Coordinator to verify that this feature is available.

To save Voxar Captures to VistA

Load images into Voxar from VistARad, and generate the views you want to save.

In the Voxar 3D window, click Capture (located in the lower right corner), then click the view to be captured.

In the Voxar Reading manager window, click the Report tab. Then click the thumbnail representing the image you want to save.

Click Finish and Archive. The Voxar windows will close.

Note After the captured image has been processed by the DICOM Gateway, it will be added to the exam as a single-image series. To view the new series, close and re-open the applicable exam in VistARad.

# VistARad Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Customizing the Work Area

The VistARad Settings Dialog

## Customizing the Work Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the following aspects of VistARad’s look and feel to suit the way you work.

Setting the Size of the Viewer Window

Resizing Controls in the Viewer (and in other Windows)

Working with Exam List Tabs

Changing Fonts in the Manager

Using Pushpins

A note for roving users

If the monitor setup at a given workstation is markedly different from workstations you have used in the past, you may need to establish an additional set of display preferences (font size, window position, etc.) the first time you log in to that workstation. Once established, each new set of preferences is retained.

### Setting the Size of the Viewer Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number of screens occupied by the Viewer window dictates which templates and hanging protocols are available for selection (details on page [137](#_Ref136748844)). Generally, the Viewer window is sized to occupy all available high-resolution monitors.

To set the size of the Viewer window

In the Viewer window toolbar, click ![](vistarad-user-guide/179.png).

In the dialog that displays, select or clear the check boxes to indicate which screens you want the Viewer to occupy. Note that:

The Viewer must occupy at least one screen.

The Viewer must occupy contiguous screens.

Click OK.

### Resizing Controls in the Viewer (and in other Windows)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the size of the following elements in the Viewer, Browser, Scrapbook, and Scout Image windows:

The Active Patient button

The toolbar

The viewport title bar

The viewport icon bar

The viewport information area

To resize the Active Patient button

Open any exam.

In the Viewer window title bar, right-click the Active Patient button.

Choose a size. The change will affect all windows that contain this button.

To resize the toolbar

Right-click the toolbar, and choose one of the available sizes. The size of the toolbar can be set independently in each window.

To resize the viewport title bar

Open any exam and load images into any viewport.

Right-click the title bar at the top of the viewport, then choose a size. The change will affect all viewports.

To resize the viewport icon bar

Open any exam and load images into any viewport.

Right-click any of the icons in the upper left corner of the viewport, then choose a size. The change will affect all viewports.

To change the information area font

In the Manager or Viewer main menu, click View \| Settings.

Click the Fonts tab, then click ![](vistarad-user-guide/180.png) on the right side of the Image Info Area box.

Select the font, font style, and font size, then click OK.

In the Settings dialog, click OK.

### Working with Exam List Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Manager window, you can show, hide, or reorder exam list tabs. You can also resize the area used to display the Open/Reserved Exams list.

To organize exam list tabs

In the Manager or Viewer main menu, click View \| Settings.

Click the Manager tab, then click the General subtab.

In the List Order area:

Select the check box for each exam list tab you want to display.

Clear the check box for each exam list tab you want to hide (the Unread and Patient List tabs cannot be hidden).

Select an entry, then click Move Up or Move Down to change the relative position of that entry. The top entry in the list equates to the leftmost tab in the Manager window.

Click OK.

To show or hide custom list tabs

In the Manager or Viewer main menu, click View \| Settings.

Click the Manager tab, then click the Custom Lists subtab.

Select the check box for each custom list you want to display, or click Enable All or Disable All to show or hide all custom lists.

Tip Settings for specific custom lists apply only when the Custom tab is displayed. See above for steps on displaying the Custom tab.

Click OK.

To resize the Open/Reserved Exams list

To change the height of the Open/Reserved Exams list, drag the separator bar just over the exam list title area up or down.

![](vistarad-user-guide/181.png)

### Changing Fonts in the Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the fonts used in the Manager window to suit your preferences and the type of monitor being used.

To change fonts in the Manager

In the Manager or Viewer main menu, click View \| Settings.

Click the Fonts tab.

Do one of the following:

To change the font used in exam lists, click ![](vistarad-user-guide/182.png) on the right side of the Manager Window box

To change the font used in buttons, click ![](vistarad-user-guide/183.png) on the right side of the Manager Buttons box.

Select the font, font style, and font size, then click OK.

In the Settings dialog, click OK.

Note After changing the font used for Manager buttons, make sure that the text in the buttons is not cut off.

Note If you have problems finding an acceptable font size, contact your Imaging Coordinator. The underlying system font size may need to be changed.

### Using Pushpins 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All windows except the Viewer window contain a pushpin button in the upper right corner. Clicking the pushpin button lets you control which windows will stay visible, and which windows that you want out of the way while you are working with the Viewer.

When the pushpin button looks like ![](vistarad-user-guide/184.png), the window in question remains visible, even if a different window is selected. (Note that for the Manager window, this setting applies only with regard to other VistARad windows. Non-VistARad windows can overlay the Manager even when the Manager pushpin is “in.”)

When the pushpin button looks like ![](vistarad-user-guide/185.png), the window in question is hidden when another window is selected.

Regardless of the state of the pushpin button, you can always click ![](vistarad-user-guide/186.png) to temporarily hide a window.

## The VistARad Settings Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistARad Settings dialog is used to control many of VistARad’s general behaviors. Most settings in this dialog are user-specific and are applied based on user login regardless of which workstation is being logged in to. (Exceptions are noted in the descriptions in for each setting).

To use the VistARad Settings dialog

In the Manager or Viewer menu, click View \| Settings.

Click the tab that contains the options you want to display.

Change the settings as desired. See the tables in the following sections for a detailed list of settings.

Click Apply to apply your changes and leave the dialog open, or click OK to apply your changes and close the dialog.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="element-tab-settings"><strong>Element tab settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Measurement and Annotation</td>
<td><p>Changes to settings will affect new measurements and annotations, but will not alter the appearance of existing ones.</p>
<p><strong>Line Thickness</strong> <strong>–</strong> Lets you specify the width of the line used for measurement and annotation lines.</p>
<p><strong>Measurement Units</strong> <strong>–</strong> Lets you specify centimeters, millimeters, or inches as the unit of measurement.</p>
<p><strong>Line Color</strong> <strong>–</strong> Click ![](vistarad-user-guide/187.png) to specify the color (or shade) used for measurement and annotation lines.</p></td>
</tr>
<tr class="even">
<td>Text</td>
<td><p>Determines the appearance of text labels. Changes to settings will affect new labels, but will not alter the appearance of existing ones.</p>
<p><strong>Font</strong> <strong>–</strong> Click ![](vistarad-user-guide/188.png) to specify the font used for text labels.</p></td>
</tr>
<tr class="odd">
<td>Scout Line Indicators, Current Image</td>
<td><p>Determines the appearance of the active slice line in a scout image.</p>
<p><strong>Line Thickness</strong> <strong>–</strong> Lets you specify the width of the line used for slice lines.</p>
<p><strong>Line Color</strong> <strong>–</strong> Click ![](vistarad-user-guide/189.png) to specify the color (or shade) used for slice lines.</p></td>
</tr>
<tr class="even">
<td>Magnifying Glass, Initial Scale</td>
<td>Lets you set the initial zoom of a Magnifying Glass, relative to the scale of the active image.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="fonts-tab-settings"><strong>Fonts Tab</strong> <strong>Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Image Info Area</td>
<td>Sets the font in the information area at the bottom of a viewport.</td>
</tr>
<tr class="even">
<td>Manager Window</td>
<td>Sets the font in the Manager window. This setting also affects the Routing dialog.</td>
</tr>
<tr class="odd">
<td>Manager Buttons</td>
<td>Sets the font in the Manager buttons. This setting also affects buttons in the Routing dialog.</td>
</tr>
<tr class="even">
<td>Report Text</td>
<td><em>Do not use. Instead, choose <strong>File | Font</strong> in the Reports window.</em></td>
</tr>
<tr class="odd">
<td>Hanging Protocols</td>
<td>Click ![](vistarad-user-guide/190.png) to specify the font in the Hanging Protocol Definition dialog.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="hanging-protocol-tab-settings"><strong>Hanging Protocol Tab</strong> <strong>Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Search for More Recent Unread Exams to Designate<br />
as Current Exam</td>
<td>When selected, you are notified if you try to open an unread exam and there is a more recent exam of the same (or similar) procedure for the same patient.</td>
</tr>
<tr class="even">
<td>Enable Loading Matching Priors and Other Related Cases for Unread Exams</td>
<td><p>When selected, any priors and related exams will be automatically opened for an unread exam if the hanging protocol being used has prior/related exam retrieval logic defined.</p>
<p>This check box can be cleared if network speeds make automatic opening of prior exams impractical.</p></td>
</tr>
<tr class="odd">
<td>Enable Loading Matching Priors and Other Related Cases for Interpreted/ Completed Exams</td>
<td><p>When selected, any priors and related exams will be automatically opened for an interpreted exam if the hanging protocol being used has prior/related exam retrieval logic defined. </p>
<p>This check box can be cleared if network speeds make automatic opening of prior exams impractical.</p></td>
</tr>
<tr class="even">
<td>Display traditional thumbnails in the Preview window</td>
<td>VistARad defaults to List View mode for certain modalities. Checking this option overrides the default to prefer Thumbnail View mode. Individual exams may still be toggled into List View during or after loading.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="manager-custom-lists-tab-settings"><strong>Manager | Custom Lists Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>&lt;List Name&gt;</em></td>
<td><p>In this tab, each custom exam list defined at a site is displayed as a check box. When the check box for a custom exam list is selected, the custom list will be displayed in the Manager window under the Custom Lists tab.</p>
<p>Note that the Custom List check box in the <strong>Manager | General</strong> tab must be selected for the settings in this tab to take effect.</p></td>
</tr>
<tr class="even">
<td>Enable All</td>
<td>Click to select all available custom lists.</td>
</tr>
<tr class="odd">
<td>Disable All</td>
<td>Click to de-select all custom lists.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="manager-dictation-tab-settings"><strong>Manager | Dictation tab settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enable Dictation Interface</td>
<td><p>When selected, VistARad will attempt to connect with a voice dictation system when VistARad is started.</p>
<p>If this check box is cleared in the current session, you will need to use the <strong>File | Establish Dictation Connection</strong> option to manually reactivate the interface in the current session.</p></td>
</tr>
<tr class="even">
<td>Options</td>
<td>Indicates which voice dictation system is being used.</td>
</tr>
<tr class="odd">
<td>Connection Parameters</td>
<td><p>Indicates the parameters needed to communicate with the voice dictation system.</p>
<p><strong>Hostname</strong> <strong>–</strong> If the voice dictation software is installed on a different workstation, this box specifies the IP address or machine name of that workstation. This box is left blank if the voice dictation software is on the same workstation as VistARad.</p>
<p><strong>Port/Socket #</strong> <strong>–</strong> The port/socket number used by VistARad to send messages to the voice dictation software. </p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="manager-general-tab-settings"><strong>Manager | General tab settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto-Open Requisition</td>
<td>When selected, the exam requisition will automatically display when an exam is opened with a lock.</td>
</tr>
<tr class="even">
<td>View Reduced-Resolution Images</td>
<td><p>Use this setting for increased speed if only reference-quality images are needed, or if network performance is an issue. While this setting is active, exams cannot be locked for interpretation.</p>
<p>This setting is retained for the current session only. If it is to be used, it must be reset at the beginning of each session.</p></td>
</tr>
<tr class="odd">
<td>Generate History List</td>
<td>When selected, VistARad will generate the History list, and will add an entry to the list each time an exam is opened. You can indicate if you want all exams added to the list, or if you want only locked exams added.</td>
</tr>
<tr class="even">
<td>Disable Exam Lock/Update</td>
<td>When selected, unread exams are <em>not</em> locked for interpretation when they are opened. This setting can be used when new users are being trained to use VistARad.</td>
</tr>
<tr class="odd">
<td>Default Status Update Prompt to “NO”</td>
<td>When selected, sets “NO“ as the initial value for “Interpret?” in the Close Exams/Update Status dialog.</td>
</tr>
<tr class="even">
<td>When using Dictation interface, default Status Update to YES only for cases sent to Dictation</td>
<td><p>The setting in this check box is applied only if:</p>
<p>VistARad’s dictation interface has been enabled.</p>
<p>The “Disable Exam Lock/Update” check box is cleared.</p>
<p>The “Default Status Update Prompt to “NO” check box is cleared.</p></td>
</tr>
<tr class="odd">
<td>List Order</td>
<td><p>Selecting a check box next to an exam list will cause a tab for that list to be displayed in the Manager. (Tabs for Patient and Unread lists cannot be disabled.)</p>
<p>The <strong>Move Up</strong> and <strong>Move Down</strong> buttons can be used to change the order that list tabs are displayed in. (The position of the Patient Exams list tab cannot be changed.)</p></td>
</tr>
<tr class="even">
<td>Display the UNREAD List at Startup</td>
<td>Checking this box will cause the UNREAD List to display when VistARad starts up.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="mouseshortcuts-tab-settings"><strong>Mouse/Shortcuts Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Reverse Window/Level Direction</td>
<td><p>When selected, window/level operations are applied the way they are executed at a Clinical Display workstation (left-to-right for window (width), top-to-bottom for level (window center)).</p>
<p>When cleared, window/level operations are applied as described in Changing Window/Level on page <a href="#_Ref136996619">76</a>.</p></td>
</tr>
<tr class="even">
<td>Right Mouse Button</td>
<td>Determines if scale or window/level is the default action assigned to a right mouse drag.</td>
</tr>
<tr class="odd">
<td>CTRL-Right Mouse Button</td>
<td>Determines if scale or window/level is the default action assigned to a CTRL-right mouse drag.</td>
</tr>
<tr class="even">
<td>Sensitivity</td>
<td>Determines how much mouse movement it takes to apply a drag-based operation in VistARad. When set to low, more mouse movement is required. When set to high, less mouse movement is required.</td>
</tr>
<tr class="odd">
<td>Enable 508 context menu and all shortcuts</td>
<td>Enables the extended context menu in viewports and all optional VistARad shortcuts. To use the extended context menu, select this check box, then open the context menu in an occupied viewport. Under the <strong>More</strong> option, there is a submenu that provides alternate access to features usually accessed using the mouse only.</td>
</tr>
<tr class="even">
<td>Enable viewport navigation shortcut keys</td>
<td><p>When selected, this option lets you use the following keyboard shortcuts in a viewport:</p>
<p><strong>F</strong> Turns full-screen view on or off in the Viewer.</p>
<p><strong>V</strong> Selects previous viewport and centers the mouse pointer over the image.</p>
<p><strong>B</strong> Selects next viewport and centers the mouse pointer over the image.</p>
<p><strong>T</strong> Opens the layout box for the selected viewport.</p></td>
</tr>
<tr class="odd">
<td>Enable arrow keys for image adjustments</td>
<td><p>When selected, this option lets you use the following arrow key combinations when the window/level, scale, or sharpen tools are turned on:</p>
<p><strong>→</strong> or <strong>↑</strong> Increase window/level, scale, or sharpness (coarse).</p>
<p><strong>CTRL + →</strong> or <strong>CTRL + ↑</strong> Increase window/level, scale, or sharpness (fine).</p>
<p><strong>←</strong> or <strong>↓</strong> Decrease window/level, scale, or sharpness (coarse).</p>
<p><strong>CTRL + ←</strong> or <strong>CTRL + ↓</strong> Decrease window/level, scale, or sharpness (fine).</p>
<p>Note that the tool must be active (by selecting it in the toolbar or from the context menu) for arrow key adjustments to work.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="prompts-tab-settings"><strong>Prompts Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Show Close/Update dialog in ReadList mode (session only)</td>
<td><p>Determines if the Close Exams/Update Status dialog is used when ReadList is active. For details, see </p>
<p>Closing Exams &amp; Updating Exam Status on page <a href="#_Ref257049904">71</a>.</p></td>
</tr>
<tr class="even">
<td>Warn if all image sets of a locked exam have not been viewed<br />
(session only)</td>
<td><p>Determines if “unviewed images” messages are displayed if locked exams are closed before all images in those exams are viewed. For details, see</p>
<p>Closing Exams &amp; Updating Exam Status on page <a href="#_Ref257049904">71</a>.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="remotelocal-reading-tab-settings"><strong>Remote/Local Reading Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Retrieve Priors/Related Exams that are NOT Routed</td>
<td>This setting is applied only at VistARad workstations used for remote reading. When selected, hanging protocols will retrieve all available priors, regardless of their storage location. Users performing remote reading with limited network bandwidth may want to clear this check box.</td>
</tr>
<tr class="even">
<td>In Auto ReadList Mode, Include Exams that are NOT Routed</td>
<td><p>This setting is active only at VistARad workstations used for remote reading. When selected, ReadList will cycle through all exams in an exam list, regardless of the exams’ storage location.</p>
<p>Users performing remote reading with limited bandwidth may want to clear this check box. This check box is cleared by default when VistARad is started.</p></td>
</tr>
<tr class="odd">
<td>In Auto ReadList Mode, Include Exams that ARE Routed</td>
<td><p>This option is intended for sites that route exams to other locations for remote reading. When selected, ReadList will step through all exams in an exam list. When disabled, ReadList will skip exams that have been routed to remote reading locations. </p>
<p>You can select the <strong>Preserve this Setting</strong> box to retain this setting from session to session; otherwise, this setting is disabled by default when VistARad is started.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="viewport-tab-settings"><strong>Viewport</strong> <strong>Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Link Options</td>
<td>Determines if changes to display properties affect all linked viewports, or the current viewport only (details on page <a href="#_Ref136930307">84</a>).</td>
</tr>
<tr class="even">
<td>Apply To Options</td>
<td>Determines if changes to display properties apply to all images in a viewport, or to the current image only (details on page <a href="#_Ref257100835">81</a>).</td>
</tr>
<tr class="odd">
<td>Copy Options</td>
<td>Determines if a property is applied to a target viewport when the Copy tool is used (details on page <a href="#copying-properties">83</a>).</td>
</tr>
<tr class="even">
<td>Cine Options</td>
<td>Determines the default settings of the Cine tool (details on page <a href="#_Ref136930315">89</a>).</td>
</tr>
<tr class="odd">
<td>Drag and Drop Options</td>
<td>Determines how the contents of a viewport are handled when images are moved into that viewport (details on page <a href="#_Ref136930311">87</a>).</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h4 id="voxar-3d-tab-settings"><strong>Voxar 3D Tab Settings</strong></h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Note</strong> Settings in this tab can be changed only if you hold the MAGJ SYSTEM MANAGER security key.</td>
</tr>
<tr class="even">
<td>Voxar 3D Executable File Path</td>
<td>The location of the primary Voxar executable (Voxar3D.exe). Must be specified for VistARad/ Voxar integration. The typical location is C:\Program Files\Toshiba\Voxar 3D.</td>
</tr>
<tr class="odd">
<td>Test</td>
<td>If the image captures from Voxar are enabled, this can be used to verify that there is a working connection between the VistARad/Voxar workstation and the DICOM Image Gateway process responsible for handling captured images. For details, see VistARad and Voxar 3D on page <a href="#vistarad-and-voxar-3d">104</a>.</td>
</tr>
<tr class="even">
<td>Device Name</td>
<td>Hard coded; cannot be changed.</td>
</tr>
<tr class="odd">
<td>AE Title</td>
<td>Hard coded; cannot be changed.</td>
</tr>
<tr class="even">
<td>Host Name</td>
<td>Specifies the computer name or IP address of the DICOM Image Gateway where the images captured from Voxar will be sent for processing.</td>
</tr>
<tr class="odd">
<td>Port/Socket #</td>
<td>The port number of DICOM Image Gateway storage process that will be used to receive Voxar image captures. It is recommended that a separate process (and port) be used for each workstation that is used to capture images from Voxar.</td>
</tr>
<tr class="even">
<td>Service</td>
<td>Hard coded; cannot be changed.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>VIX Configuration Tab Settings: Local Site VIX frame</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto-detect</td>
<td>When selected, allows VistARad to find the nearest VIX server by querying the VIX Site Service.</td>
</tr>
<tr class="even">
<td>Specify Site Number</td>
<td>When Auto-detect is not checked, a site can be found by typing in its correct Site Number in the space provided.</td>
</tr>
<tr class="odd">
<td>Specify Connection</td>
<td>When Auto-detect is not checked, VistARad’s Local VIX Server can be specified directly by selecting this button and entering the Host Name and<br />
Port/Socket #.</td>
</tr>
<tr class="even">
<td>Test</td>
<td>Click Test to check whether connection was achieved after specifying by Site Number or Connection</td>
</tr>
<tr class="odd">
<td>Enable VIX-assisted remote access</td>
<td>When Auto-detect is not checked, allows VIX to provide non-routed, ad hoc access to remote sites.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>VIX Configuration Tab Settings: Monitored Sites frame (controlled by MAGJ REMOTE ACCESS CONTROL security key)</strong></td>
</tr>
<tr class="odd">
<td>Monitored Sites</td>
<td>The following columns appear under the Monitored Sites frame: Site number, list ID, list name, Site Name, Division Code</td>
</tr>
<tr class="even">
<td>New Site</td>
<td>Click button to add site to list of Monitored sites, specifying by Site Number, Division, Site Name, List Name, and List ID.</td>
</tr>
<tr class="odd">
<td>Edit Site</td>
<td>Click button to change information entered regarding a Monitored Site.</td>
</tr>
<tr class="even">
<td>Delete Site</td>
<td>Click button to remove a checked site from the list of Monitored Sites.</td>
</tr>
<tr class="odd">
<td>Test Site</td>
<td>Click button to determine whether connection parameters for monitored sites were successfully retrieved</td>
</tr>
<tr class="even">
<td>Enable dictation reminder message</td>
<td>Check to enable reminder to change dictation servers; or un-check to disable reminder.</td>
</tr>
</tbody>
</table>

# Using VistARad for Teleradiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

VistARad and Routing

Using On-Demand Routing

Routed Exams and Remote Reading

## VistARad and Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistA Imaging, *routing* is the process by which a copy of an exam acquired at one site is sent to a remote location for interpretation, review, or other purposes. When routing is used to support off-site interpretation, the routed copy of the exam can be reviewed without the delays imposed by a wide area network, while still allowing results to be entered into the originating site’s VistA system.

When routing is used:

Exams can be automatically routed as soon as they are acquired using a site-specific set of rules.

A VistARad workstation can be set up to route exams on demand.

A VistARad workstation can be used to interpret copies of exams routed from other sites (remote reading).

Note The following sections describe routing only as it applies to VistARad. For general information about routing, refer to the *VistA Imaging Routing User Guide*.

## Using On-Demand Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On-demand routing is used to send a copy of an exam to another location for interpretation or other purposes. You can also use on-demand routing to pull a local copy of an exam to your workstation from a remote location.

To use on-demand routing, you must hold the MAGJ DEMAND ROUTE security key or the MAGJ DEMAND ROUTE DICOM security key.

If you are frequently using on-demand routing for the same sorts of exams, contact your Imaging Coordinator. This person can determine if automatic routing can be used to improve turnaround times.

Note On-demand routing, if overused, can reduce the overall performance of the wide area network that connects sites in a routing system. Whenever it is practical to do so, consider performing on-demand routing during non-peak hours.

To use on-demand routing

Log in to the VistA System at the site where the exams to be routed were acquired.

In the Manager, select the exams you want to route.

Click the Route Exams button, located near the upper right corner of the Manager window. (This button is displayed only if you have a routing-related security key.)

When the Route Request dialog opens, make sure all the exams you selected are shown.

Note If a selected exam is not on the image shares, a message will appear at the bottom of the Route Request dialog indicating that exam has been requested from the archive. Until the exam has been retrieved from the archive, it is not available for on-demand routing.

Indicate where you want each exam sent.

To send exams to specific locations, click the fields in the Route To column for each exam, and select a location.

To send all exams to the same location, use the Default Route box near the bottom of the window.

In the Route To and Default Route boxes, other VistA locations are listed first. DICOM locations, if present, are shown at the bottom of the list. (DICOM locations are always prefixed by dcm.) For more information, refer to the *Routing User Guide*.

Indicate the routing priority you want to use.

To send each exam with a different priority, click the fields in the Priority column for each exam, and select a priority.

To send all exams with the same priority, use the Priority box near the bottom of the window.

After selecting destinations and priority, click OK to route the exams. Note that factors such as exam size and network traffic will affect how long it takes exams to be routed.

To confirm an exam was routed successfully

When an exam is routed successfully, the RC column in your exam lists will show name of the site that the exam was sent to.

![](vistarad-user-guide/191.png)

Note that the amount of network traffic and the priority used will affect how long it takes the exam to arrive at its destination.

## Routed Exams and Remote Reading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you use VistARad to interpret exams routed to you from other sites, you can use the following features to control how routed exams are handled.

Note Routed exams are automatically deleted from local storage after a certain number of days. If a routed exam was deleted before you had a chance to review or interpret it, contact your Imaging Coordinator and ask for an increase in the exams’ retention period (as specified in the appropriate entry in the NETWORK LOCATION File (#2005.2).)

The Remote Read Filter

When you are logged in to a remote site, VistARad automatically filters exam lists (except the patient lists) to show only the exams that have been routed to you. When this filter is active, the ![](vistarad-user-guide/192.png) button is displayed in the Manager window. When the check box in this button is selected, only routed exams are visible. You can clear the check box if you want to see all exams at the remote site.

If Remote ReadFilter is not present in the Manager window, there are no routed exams available (any previously routed exams have been interpreted and cycled off the selected exam list, or the routed copies have been deleted from local storage).

Opening priors for routed exams

When you are opening routed exams for interpretation, a user setting determines if only priors that have been routed to you are opened, or if all applicable priors are opened. To change this setting:

In the Manager or Viewer menu, click View \| Settings.

Click the Remote/Local Reading tab.

In the Remote Reading area, select or clear the first check box as desired.

Click OK.

ReadList and remote reading

When you are using ReadList while reading remotely, only exams that have been routed to you are opened.

If you want ReadList to open all exams:

Disable the Remote Read Filter in the Manager.

Choose View \| Settings \| Remote/Local Reading, and select the second check box in the Remote Reading area. Note that this setting is not maintained across VistARad sessions. Monitoring Exam Lists of Remote Sites

If you read for multiple sites, you can now view exam lists at other sites while logged in to the current reading site. When this feature is enabled, you can be interpreting exams for one site while monitoring the workload at the other sites.

Note To configure and use multi-site monitoring, you need to hold the MAGJ REMOTE ACCESS CONTROL security key.

A “Monitored Sites” tab is used to access exam lists from other sites. Lists from each of the sites display as separate sub-tabs, and are periodically refreshed with the most current information.

If a STAT or Urgent exam is detected on a monitored exam list, VistARad displays an icon ![](vistarad-user-guide/193.png) on the toolbar above the Monitored Sites tab to notify you; the icon also appears on the site-specific tabs, as applicable.

![](vistarad-user-guide/194.png)

The Monitored sites exam lists are strictly read-only—no interactions with the list entries are allowed, so all of the Manager’s command buttons (except Login and RefreshExams) are disabled, and no context menu options are provided. Also, highlighting a list entry then selecting the Patient Exams tab will return you to the previously accessed *local* patient’s exam list.

Monitored sites are specified, on a per-user basis, in the Monitored Sites frame of the VIX Configuration tab: View \| Settings \| VIX Configuration, after which they appear within the Monitored Sites tab in the Manager window.

### One-click Login to a Monitored Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can quickly log in to a monitored site using the Login button to the right of the Monitored Sites tab. This login process is streamlined so there is no need to re-enter PIV PIN codes. However, you will need to close any currently opened exams; VistARad will prompt you if this is necessary. If the application gives timeout error, you can increase the timeout (TIMEOUTSECONDS) value in the configuration file (MAGJ.ini).

Once you have logged in to the new site, all standard VistARad functions are available.

### Dictation and Remote Reading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you log in to a Monitored site, VistARad can display a message box as a reminder to change dictation servers, if applicable.

![](vistarad-user-guide/195.png)

To disable this reminder, un-check the “Enable dictation reminder” message in the Monitored Sites frame of the VIX Configuration tab.

# Using Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Template Basics

Selecting and Applying Templates

Working with Templates

Working with Screen Templates

## Template Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Viewer window, the number, size, and arrangement of viewports are controlled by the active *template*. Templates are usually applied to the Viewer window automatically when an exam is opened using a hanging protocol. Templates can also be applied manually by the user.

Templates are not used in the Browser window.

Users interested in defining their own hanging protocols will either need to use existing templates, or create their own templates. At most sites, a generalized collection of sysAdmin templates is available. All users can access and create their own copies of sysAdmin templates, but only users who hold the MAGJ SYSTEM USER security key can edit or delete sysAdmin templates.

## Selecting and Applying Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Opening an Exam with a Template Only 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Usually, a template is selected automatically based on the hanging protocol used to open the exam. You can also manually select a template if you want to load viewports manually for the exam you are viewing.

To open an exam with a template only

In the Manager, select the exam you want to open.

Click the Open With button (located to the left of the Open button).

In the dialog that displays, select the template that you want to use.

The dialog is organized into groups by user name, with your user name shown at the top. Under each user name, templates are listed after hanging protocols.

Any template, including templates under other user names, can be selected.

A representation of the selected template is displayed near the bottom of the dialog.

The Apply Filter check box limits the contents of the dialog to templates that match the current size of the Viewer window. Usually, this checkbox should remain selected.

Double-click the selected template or click OK.

The exam will be opened.

The Viewer window will contain only empty viewports.

Images can be loaded into viewports by dragging thumbnails from the Preview window (details on page [55](#loading-viewports)).

Tip In the Manager, the template you selected is displayed to the right of the Open With button. Other exams can be opened with this template by selecting the check box next to the template name and then clicking Open With.

### Applying a Different Template to an Open Exam 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the template being used in the Viewer. Once you have selected a different template, you will need to manually reload viewports with images.

To apply a different template

In the Viewer window, click the TP: \<name\> button. This button is located in the upper right corner of each monitor occupied by the Viewer.

When you are notified that viewports will be cleared, click OK.

In the dialog that displays, select the template you want to use.

The dialog is organized into groups by user name, with your user name shown at the top. Under each user name, templates are listed after hanging protocols.

Any template, including templates under other user names, can be selected.

The bottom of the dialog will show the viewport arrangement for the selected template.

Double-click the selected template or click OK.

Manually reload images into viewports (details on page [55](#loading-viewports)).

## Working with Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Templates can be created and edited using the Template Designer.

### Creating Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps explain how to create a new template.

Tip Before creating a new template, use the Select Hanging Protocol/Template dialog to see if an existing template can be used or adapted.

To create a template

Choose Customize \| Template Designer from the Viewer menu.

In the Template Designer, click New.

Define the viewport arrangement to be used in the template.

For details about adding, modifying, and merging viewports, see Using the Template Designer on page [131](#_Ref136058677).

To insert a pre-defined screen template, right-click the display area and choose Insert Screen Template. For details, see Working with Screen Templates on page [133](#_Ref136058412).

When you have finished, click Save.

Enter a name for the template.

Note The template name should reflect naming conventions in use at a site. At a minimum, the name should indicate the number of monitors and number of viewports per monitor defined in the template.

If you hold the MAGJ SYSTEM USER security key, you can set the template level to user-level (associating the template with your user name), or site-level (associating the template with the sysAdmin user).

Click OK to save the template.

### Editing Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can edit an existing template if you are the creator of the template and if the template is not referenced in a hanging protocol.

Other templates can still be opened for editing. However, instead of saving your edits to the existing template, you will be opening a copy of the template that can be saved as a new template in your collection.

To edit a template

If the template you want to edit is being used in the Viewer, do one of the following:

Click Customize \| Edit Template (this is available only if you are the owner of the template, and if the template is not referenced in a hanging protocol).

Click Customize \| Copy / Edit Template open a copy of the template for editing.

If the template you want to edit is NOT being used in the Viewer:

Click Customize \| Template Designer.

In the Template Designer, click Edit.

Select the template that you want to edit.

Use the preview area at the bottom of the dialog to verify that the desired template is selected.

Click OK.

In Template Designer, alter the viewport arrangement in the template as desired.

For details about adding, modifying, and merging viewports, see Using the Template Designer on page [131](#_Ref136058677).

To insert a pre-defined screen template, right-click the display area and choose Insert Screen Template. For details, see Working with Screen Templates on page [133](#_Ref136058412).

When you have finished, do one of the following:

Click Save to apply your changes (this is available only if you are the owner of the template, and if the template is not referenced in a hanging protocol).

Click Save As, enter a name for the new template, then click OK.

Tip If you hold the MAGJ SYSTEM USER security key, you can set the template level to user-level (associating the template with your user name), or site-level (associating the template with the sysAdmin user).

### Using the Template Designer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to use the Template Designer. It is assumed that the steps for Creating Templates on page [129](#_Ref136058675) or Editing Templates on page [129](#_Ref136058676) have been used to open a template for editing.

Template Designer basics

In the Template Designer, the display area (the dark part of the screen) represents the space available for viewports. Gray gridlines indicate viewport boundaries.

If you are creating a new template, the display area in the Template Designer is initially set to one viewport per monitor.

If you are editing a template, each monitor may contain one or more viewports. A viewport may also span multiple monitors.

To add viewports

In the Template Designer display area, point to the area you want to divide into smaller viewports.

Click the mouse. A layout tool will display under the mouse pointer.

Move the mouse to highlight the number of rows and columns you want to divide the existing viewport into.

Click the mouse. The area is divided into the number of rows and columns specified in the layout tool.

Optionally, repeat these steps to further subdivide the area into smaller viewports.

To size viewports

To change the proportions of a viewport in the Template Designer, drag a gridline using the mouse. Note that:

You cannot drag gridlines located at the edge of the monitor.

Dragging any other gridline to the edge of a monitor deletes the gridline.

To make wide (multi-screen) viewports

Ensure that the Template Designer display area contains one viewport per screen on two or more adjacent screens.

Right-click the viewport that you want to extend across another screen, then choose Merge Left or MergeRight.

To remove viewports

You can delete viewports in the Template Designer using any of the following methods:

To delete a gridline between viewports, drag the gridline past the edge of a screen.

To combine all viewports on a screen into a single viewport, right-click on that screen and choose Clear Screen.

To remove one level of “nesting” in a viewport, click a nested viewport and choose Delete Grid.

If the viewport is extended across more than one screen, right-click the extended viewport and choose Undo Merge.

### Deleting Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Templates no longer used by a hanging protocol can be deleted as described below. Templates being used by a hanging protocol cannot be deleted.

To delete a template

Do one of the following:

In the Viewer, click Customize \| Template Designer. Then click Edit in the Template Designer.

In the Manager, click Open With (make sure the check box next to this button is cleared before clicking the button).

In the Select Hanging Protocol / Template dialog, select the template you want to delete.

Templates are listed after hanging protocols under your user name.

If you hold the MAGJ SYSTEM USER security key, you can also select a template under the sysAdmin user.

You cannot delete other users’ templates.

Click Delete, then click OK when you are asked for confirmation.

Click Close.

## Working with Screen Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A screen template is a saved arrangement of viewports for a single monitor. Screen templates are used to speed up template creation.

Screen templates can be added to a template that you are editing in the Template Designer. Screen templates are created and deleted using the Screen Template dialog.

To apply a screen template

If it is not running already, click Customize \| Template Designer to start the Template Designer.

On the screen where you want add the screen template, right-click and choose Insert Screen Template.

On the left side of the dialog that displays, select the screen template you want to insert.

Screen templates are grouped by user name. Any screen template can be selected.

To expand or collapse the list of screen templates for any user, double-click the appropriate user name.

A preview of the selected screen template is displayed in the main part of the Screen Template dialog.

Click Insert. The dialog will close and the screen template you selected will display on the appropriate screen.

To create a screen template

If it is not running already, click Customize \| Template Designer to start the Template Designer.

In the Template Designer, create the arrangement of viewports you want to use for a single screen only. For detailed steps, see Using the Template Designer on page [131](#_Ref136058677).

Right-click the screen you want to use and choose Save as Screen Template.

Enter a name for the new screen template, then click OK.

To delete a screen template

In the Viewer, click Customize \| Template Designer.

Right-click the template editing area and choose Insert Screen Template.

On the left side of the Screen Template dialog, select the screen template you want to delete.

Screen templates are grouped by user name, with your user name displayed at the top.

To expand or collapse the list of your screen templates, double-click your user name.

If you hold the MAGJ SYSTEM USER security key, you can also select a screen template under the sysAdmin user.

Click Delete, then click Yes when you are asked for confirmation.

Note Deleting a screen template does not affect templates based on that screen template; the deleted screen template is simply no longer available for future use.

# Using Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Hanging Protocols Explained

Selecting a Hanging Protocol

Creating Hanging Protocols

Working with Hanging Protocols

## Hanging Protocols Explained

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hanging protocols automate the display of exams in the Viewer window. When an exam is opened using a hanging protocol, the hanging protocol can:

Identify and display comparison exams in the Viewer window along with the exam that you opened.

Automatically arrange images in the Viewer window for efficient review.

Apply pre-defined display settings (stack/tile, window/level, scale, etc.) to each group of images in the Viewer window.

Use stages to arrange exams into multiple views (details on page [63](#_Ref137003237)).

For sites that use routing, hanging protocols can be selected based on the location of the user relative to where the exam being opened was acquired (details on page [159](#_Ref148930507)).

Capabilities of hanging protocols vary, based on how they are defined and the conditions under which they are used. The following sections outline the main factors that govern how hanging protocols behave.

How hanging protocols are selected

Unless you specify otherwise, a hanging protocol is automatically selected when you open an exam (details on page [139](#_Ref157332912)).

If there are two or more hanging protocols that are equally appropriate for the exam that you are opening, you will be notified and asked to select one of the matching hanging protocols (details on page [140](#resolving-multiple-matches)).

Hanging protocols can also be manually selected (details on page [137](#manual-hanging-protocol-selection)).

About the “current” exam

When you open a single exam, that exam is automatically considered the current exam. The procedure (CPT) or modality of the current exam is used as a reference point for automatically selecting a hanging protocol.

Tip Optionally, you can be notified if you try to open an unread exam and there is a more recent exam of the same or similar procedure for the same patient. To use this option, click View \| Settings, select the Hanging Protocol tab, then select the first check box.

If you open multiple exams for the same patient at the same time, the following logic is used to determine which exam is the current exam and to manage image display:

If only one of the exams is unread (ready to be interpreted), that exam is considered the current exam.

If all (or none) of the exams have been interpreted, the most recent exam is considered the current exam.

Once the current exam is identified, a single hanging protocol is used for all the exams being opened. The images for the current exam will be loaded into the Viewer window.

The other “non-current” exams will also be opened into the Preview window, but their images will be displayed in the Viewer only if they are identified as prior or related exams by the active hanging protocol.

How hanging protocols identify prior and related exams

Once the current exam has been identified, the procedure (CPT) or modality information associated with the exam can be used to identify and load prior exams.

Note If a current exam has the Left or Right procedure modifier, an exam with the opposite modifier will not be selected as a matching prior.

Hanging protocols can also retrieve one or more “related cases.” Related cases are comparison exams that are dissimilar (in terms of procedure or modality/body part) from the current exam, but which are still relevant to the current exam.

Hanging protocols can limit the age and/or number of prior and related cases to retrieve. Specific values can vary from one hanging protocol to another.

User-level and site-level hanging protocols

VistARad incorporates the following types of hanging protocols:

User-level hanging protocols  
Each VistARad user can define their own collection of hanging protocols. User-level hanging protocols are grouped under a user’s name in the Select Hanging Protocol / Template dialog (opened by clicking Open With in the Manager). User-level hanging protocols can be edited or deleted only by the user who created them.

Site-level hanging protocols  
A user who holds the MAGJ SYSTEM USER security key can define site-level hanging protocols. Site-level hanging protocols are stored under the sysAdmin user in the Select Hanging Protocol / Template dialog. Site-level hanging protocols can be accessed by any user, but they can be edited or deleted only by users who hold the MAGJ SYSTEM USER security key.

Several site-level hanging protocols are present when VistARad is installed. These hanging protocols, identified by the SYS_INT suffix in their names, are used for basic system operations and cannot be deleted. For more information, see Internal Hanging Protocols on page [181](#_Ref153180625).

There is an equivalent type of template for both user-level and site-level hanging protocols.

## Selecting a Hanging Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections cover:

Manual Hanging Protocol Selection

Automatic Hanging Protocol Selection

Resolving Multiple Matches

### Manual Hanging Protocol Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps to manually select a hanging protocol for an exam being opened.

To manually select a hanging protocol

In the Manager, select the exam you want to open.

Click the Open With button located on the left side of the window.

In the dialog that displays, select the hanging protocol that you want to use.

Hanging protocols are organized into groups by user name.

Any hanging protocol listed under any user name can be selected; to see a list of hanging protocols for a user, click the ![](vistarad-user-guide/196.png) icon next to the user name.

The Apply Filter check box limits the contents of the dialog to hanging protocols that match the current size of the Viewer window. Usually, this check box should remain selected.

Click OK to use the selected hanging protocol to open the exam.

If the dialog shown below displays, do one of the following:

To confirm that you want to use the selected hanging protocol, click View case with HP.

If you want the selected hanging protocol’s definition to be updated, allowing it to be selected for the same type of exams in the future, select the Add the new value to the HP check box.

To open the exam into the Preview window only, click View case without HP.

![](vistarad-user-guide/197.png)

Tip In the Manager, the hanging protocol you selected is displayed to the right of the Open With button. Other exams can be opened with this hanging protocol by selecting the check box next to the hanging protocol name and then clicking Open With.

### Automatic Hanging Protocol Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hanging protocols are selected automatically unless you have specified otherwise. When automatic selection is used, the following process is used to identify the most appropriate hanging protocol:

The procedure (CPT code) and the modality of the current exam are identified.

A search for hanging protocols with the same CPT code as the current exam is performed. If no match is found...

A search for hanging protocols with a similar[^5] CPT code relative to the current exam is performed. If no match is found...

A search for hanging protocols with the same modality as the current exam is performed.

For each search described in steps 2 – 4 above, hanging protocols are evaluated in the following order:

The current user’s default hanging protocols are checked first. If no default hanging protocol is found...

Site-level (the sysAdmin user’s) default hanging protocols are checked. If no default hanging protocol is found...

The current user’s complete collection of hanging protocols is checked. If there are no user hanging protocols found...

All site-level hanging protocols are checked.

At a minimum, if no other hanging protocols are found, one of VistARad’s modality-based internal hanging protocols will be selected and used to load images into the Viewer and locate and load priors. For details, see Internal Hanging Protocols on page [181](#_Ref153180625).

### Resolving Multiple Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are multiple hanging protocols that are equally appropriate for an exam being opened, you will be prompted to select a hanging protocol.

![](vistarad-user-guide/198.png)

When the dialog shown above displays, do either of the following:

To use one of the hanging protocols listed in the dialog, click the hanging protocol, then click Use Selected HP.

To open the exam into the Preview window only, click Default Processing.

If you want one of the hanging protocols listed in the dialog to *always* be automatically selected for the listed procedure or modality, select one the Save Selected... check boxes near the bottom of the dialog before clicking Use Selected HP.

This will designate the selected hanging protocol as a default hanging protocol.

Depending on how the hanging protocol was defined, one or both of the Save Selected... check boxes may be disabled.

For additional details, see Using Default Hanging Protocols on page [147](#_Ref157236611).

## Creating Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In broad terms, creating a hanging protocol breaks down into the following parts:

Design– Determining what the hanging protocol will do and identifying the types of exam that the hanging protocol will be used for.

Model– Using existing exams and a template to model the hanging protocol in the Viewer window. This will probably be done more than once as you refine the hanging protocol’s design.

Implement– Using the Define Hanging Protocol dialog to pick up the broad outlines of the hanging protocol you have modeled, and to define any special functions such as stages, local/remote settings, or explicit viewport mapping.

Once defined, a hanging protocol can be accessed by any VistARad user at your site.

Tip To get a feel for how to define a hanging protocol without having to design it first, see the Hanging Protocol Cookbook on page [170](#hanging-protocol-cookbook).

### Designing a Hanging Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When designing a hanging protocol, you will want to consider the following factors.

Initial steps

Identify the procedure (CPT code) or modality of the exams that will be displayed using the new hanging protocol. Determine how many prior exams (if any) you will want retrieved for comparison.

Before proceeding further:

Review the existing pool of hanging protocols (including those defined by other users). A useful hanging protocol for the procedure/modality in question may already exist.

Make sure you have access to enough exams to model the hanging protocol (details on page [143](#_Ref151276015)).

Choose a name

Determine in advance what the name of the hanging protocol will be. Use naming conventions in force at your site.

At a minimum, the hanging protocol name should reflect the applicable modality and body part. You can reference the specific procedure as well, but take care to keep the name relatively short.

Each hanging protocol for a particular user must have unique name. Hanging protocol names are case-sensitive, and can include alphanumeric characters, spaces, and some punctuation marks. However, the following characters are not allowed:

/ , \\ (slash, backslash)

^ (caret)

~ (tilde)

\| (vertical bar)

\*(asterisk)

" (quotation mark)

\>, \< (greater-than, less-than)

& (ampersand)

If you are defining hanging protocols for workstations with different display setups (number of monitors, resolution, etc.), it is useful to indicate the display setup in the name of the hanging protocol. This will make it easier to distinguish between hanging protocols when filtering (details on page 122) is turned off.

Determine how images will be arranged in the Viewer

Determine if images in each exam will all be loaded into a single viewport, or if they will be distributed across viewports as groups (series).

Determine if you want groups of images to be cloned and linked to allow different display settings to be used at the same time. To see an example of how clones and links can be used, open an exam using the CT_Thorax_2-hd_SYS_INT hanging protocol (details on page [183](#ct_thorax_2-hd_sys_int)).

Select or create a template that reflects the viewport arrangement you will want to use.

If you are designing a hanging protocol for x-rays on a multi-head workstation, you may want to use a wide/merged viewport to allow a single exam to be viewed across multiple monitors.

If you are designing a hanging protocol for complex exams, you may want to set aside one or more overflow viewports to accommodate extra groups of images (such as additional referenced image sequences in MR exams).

Within each planned viewport, determine:

If you want images to be stacked (1-up) or tiled (displayed in two or more rows and columns).

If more than one viewport will be used for an exam, decide if you want groups of images mapped into viewports explicitly or generically (details on page [169](#viewport-mapping-explained)).

Optionally, determine if you want to use stages to arrange images in multiple views. A frequently used method is to define a hanging protocol that has separate stages for “with priors” and “without priors” views.

Define image display properties

Determine the window/level, scale, apply to settings, etc., you want to use in each viewport. Virtually all of the display settings made in a viewport can be “picked up” in the process of defining a hanging protocol.

Note Unless you explicitly set a scale percentage when you model an exam, the default scale setting in a new hanging protocol is “fit to size.”

Define availability

Determine if this will be a user-level or site-level hanging protocol.

User-level hanging protocols are available for automatic selection only for the user who created the hanging protocol. (However, other users can manually select the hanging protocol if they so desire.)

Site-level hanging protocols are available for automatic selection by any user. An applicable site-level hanging protocol will be selected automatically if a particular user does not have their own user-level hanging protocol that takes precedence.

If your site uses routing, determine if the hanging protocol should be accessible by local readers only, by remote readers only, or by all VistARad users.

### Modeling a Hanging Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a design for a new hanging protocol has been established, you will need to use existing exams to model the new hanging protocol. To do this:

Check the Viewport tab in the VistARad Settings dialog (View \| Settings). Make sure that initial viewport settings for Link, Apply To, etc. are set as desired.

If needed, you can override baseline settings for specific viewports once images are loaded into viewports.

Note that if you use a hanging protocol to open your model exams, the settings in the hanging protocol may override the baseline settings in the VistARad Settings dialog.

Locate exams to use to model the hanging protocol.

The exams must all be associated with the same patient.

The exam used to model the current exam must reflect the procedure (or modality) that you want the hanging protocol to be applicable for.

Exams used to model prior exams (if any) must match the modality of the current exam. For modeling purposes, the procedures of priors do *not* need to match the current exam.

The exams used to model other related exams (if used) must reflect the properties of the exams you want the hanging protocol to retrieve. For example, if you want chest CTs to be retrieved as related cases, your model exam must be a chest CT.

The number of model exams must be the same as the number of exams you want displayed simultaneously by the hanging protocol. (For example if you want the hanging protocol to display a current and two priors, you will need three exams. However, additional hidden priors do not need a model exam.)

Locate or create a template that reflects the viewport arrangement you have defined.

Open the model exams using the Open With button, and manually select the desired template.

Use the Preview window to load images from each exam into the Viewer.

For each viewport, set the display properties (scale, layout, clone/link, apply) you want reflected in the hanging protocol.

Tip If you do not explicitly set a scale percentage, “Fit to Size” will be used for the viewport.

Tip You can also set display properties later on using the Define Hanging Protocol dialog, but it is usually easier to set general display properties directly in the viewports.

### Implementing a Hanging Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps explain how the Define Hanging Protocol dialog is used to create a hanging protocol.

Model the hanging protocol as described in the previous section.

In the Viewer window, click Customize \| Create Hanging Protocol.

Enter the name and (optionally) the level of the hanging protocol, then click OK.

The Define Hanging Protocol dialog will open. Notice that:

The Case Info tab is displayed automatically, and the settings related to the current exam are active.

The first occupied viewport in the Viewer is highlighted. Unless you specify otherwise, this exam is presumed to be the current exam.

In the Case Info tab, use the following options to specify global settings for the hanging protocol:

To control if exams are divided into groups based on series UID, use the Disable Series Processing check box (details on page [161](#case-info-disable-series-processing-check-box)).

If your hanging protocol will be using explicit viewport mapping, set the Regroup leftover image sets check box as desired (details on page [162](#_Ref149966843)).

If your site uses routing, use the Local/Remote options to control the availability of the hanging protocol (details on page [159](#_Ref148930507)).

If you are creating a staged hanging protocol, set the Use this stage... check box as desired (details on page [160](#_Ref149969563)).

In the Case Info tab, verify (or change) the Case Type setting that indicates if the exam is the current exam, a matching prior exam or an “other related” exam. Identify the type of exam in the selected viewport:

If the Case Type is Current, use the HP Lookup area to specify the procedure (CPT code) or modality that will be used to match this hanging protocol to other exams (details on page [155](#case-info-hp-lookup-area-for-current-exams)).

If the Case Type is Matching Prior, use the Prior Attribute area to specify selection criteria for prior exams (details on page [156](#case-info-prior-attribute-area)).

If the Case Type is Other Related Cases, use the Attribute area to specify selection criteria for additional cases (details on page [157](#_Ref148924459)).

Click Save Case Info. This indicates that you finished setting parameters for exams of the active Case Type.

The Viewport Info tab will display automatically. It will reflect the display settings and attributes for the images in the selected viewport.

Use the Pixel Processing area near the bottom of the tab to set or change display attributes, or to select an image preset (details on page [167](#viewport-info-pixel-processing-area)).

If you are using explicit viewport mapping, use the Specify attributes... list to define which images should be included in the viewport (details on page [164](#_Ref150761455)).

If the selected viewport contains cloned images, use the Clone/Placeholder controls to indicate if the images are actual clones, or if they are being used to reserve a space for an additional unique series (details on page [163](#viewport-info-cloneplaceholder-options)).

Optionally, use the More Viewport Info tab to set additional display settings for the selected viewport ( details on page [159](#_Ref148930507)).

When you have finished, click Save Viewport Info. If it is enabled, click the Next button as well.

Depending on where you are in the definition process, do one of the following:

If you are creating a staged hanging protocol, click Next Stage. See step 12.

If you have finished creating this hanging protocol, click Save HP.

If the Viewport Info tab remains visible, the newly selected viewport contains images from the same exam. Repeat steps 8 through 10.

If the Case Info tab displays, the newly selected viewport contains images from a different exam. Repeat steps 6 through 10.

*Staged hanging protocols only:* After clicking Next Stage, the Define Hanging protocol dialog will temporarily disappear. Do the following:

Note Do not click buttons in the Multi-Stage HP... dialog until you have finished arranging the new stage.

In the Viewer window, re-arrange your existing exams to model the next stage (additional exams cannot be opened).

If this is not your last stage, click Next Stage. Then repeat steps 8 through 10.

If this is your last stage, click Save HP in the Multi-Stage HP... dialog.

Tip For detailed steps that explain how to create a basic staged hanging protocol, refer to the Hanging Protocol Cookbook on page [170](#hanging-protocol-cookbook).

Close the exams that were used to model the hanging protocol.

Reopen the current exam to verify that the new hanging protocol is automatically selected and that images are arranged as expected.

## Working with Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections cover:

Using Default Hanging Protocols

Expanding the Scope of Hanging Protocols

Editing Hanging Protocols

Copying Hanging Protocols

Deleting Hanging Protocols

### Using Default Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hanging protocols can be defined in such a way that there is more than one hanging protocol appropriate for an exam with a given procedure or modality. To eliminate the need to select between multiple matching hanging protocols, you can designate a hanging protocol as a default for a particular procedure (CPT) or modality.

Designating a default hanging protocol does not alter which CPT or modality codes are associated with that hanging protocol; it gives only one hanging protocol precedence over other similar hanging protocols.

For each CPT or modality code, only one hanging protocol can be designated as a default.

The default hanging protocol for a CPT or modality can be changed by designating a different hanging protocol for that CPT or modality.

You can designate a default hanging protocol on the fly when the “Multiple Matching Hanging Protocols” dialog displays (details on page [140](#resolving-multiple-matches)). You can also designate a default hanging protocol as described below.

To designate a default hanging protocol

In the Manager, select an exam that reflects the procedure or modality for which you want to designate a default hanging protocol.

Make sure the checkbox next to the Open With button is cleared, then click Open With.

In the Select Hanging Protocol/Template dialog, select the hanging protocol you want to designate as a default.

If you want to select another user’s hanging protocol, or if you want to select a sysAdmin hanging protocol and you do not hold the MAGJ SYSTEM USER security key, use Save As to create a personal copy of that hanging protocol. Then select the new copy you just made.

If you hold the MAGJ SYSTEM USER security key, you can select a sysAdmin hanging protocol and designate it as a default for all users at a site. However, if a user has set up his or her own default hanging protocol for the same CPT or modality, that user’s default will take precedence over the site-level default hanging protocol you designated.

Select either the Default HP for Selected Procedure or the Default HP for Selected Modality check box.

If the selected hanging protocol was originally defined for a CPT (procedure), only the Default HP for Selected Procedure check box will be enabled.

If the selected hanging protocol was originally defined for a modality, both check boxes will be enabled.

Note The settings in the Default HP for... check boxes are applied as soon as the check boxes are selected or cleared (it is not necessary to click OK or Close to apply any changes).

### Expanding the Scope of Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a hanging protocol is created, it is associated with a CPT (procedure) or modality. You can use the following steps to add additional CPT or modality values to an existing hanging protocol, allowing it to be automatically selectable for an exam with the same procedure or modality type.

Note that when you add a new CPT or modality value to a hanging protocol’s definition:

The addition does not affect the default hanging protocol designated for a particular CPT or modality (details on page [147](#_Ref157236611)).

The addition may result in multiple hanging protocol matches for exams being opened (details on page [140](#resolving-multiple-matches)).

To expand the scope of a hanging protocol

Locate an exam that reflects the procedure or modality you want to associate with a particular hanging protocol.

Use the Open With button to manually select the hanging protocol you want to use (details on page [137](#manual-hanging-protocol-selection)).

When you are notified that there is a difference between the hanging protocol definition and the exam, select the Add the new value to the HP check box, then click OK.

Tip If the exam opens without displaying the “Difference between the HP definition...” dialog, the association you are trying to create already exists.

### Editing Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following properties of a hanging protocol can be directly edited:

Prior and “Other related” exam selection attributes.

Display properties for each viewport populated by the hanging protocol.

Settings in the Specify Attributes list.

To edit a hanging protocol

Select Customize \| Edit Hanging Protocol from the Viewer main menu.

In the dialog that displays, select the hanging protocol to be edited.

If you want to edit another user’s hanging protocol, use Save As to make a personal copy of that hanging protocol before proceeding.

To edit a hanging protocol associated with the sysAdmin user, you need to hold the MAGJ SYSTEM USER security key.)

Click OK. Note that:

Because the current exam selection criteria of a hanging protocol cannot be directly edited, the system proceeds directly to the viewport-level settings for the current exam.

The Viewer will be replaced by a mockup of the template and viewports defined for the selected hanging protocol, and the first viewport containing the current exam is selected.

Use the Next and Previous buttons to move from one viewport mock-up to the next. For each viewport occupied by images:

Use the controls in the Viewport Info and More Viewport Info tabs as desired.

Be sure to use the Save Viewport Info button to apply your changes.

When you navigate to a viewport assigned to a prior exam, you can optionally click the Case Info tab and change attributes for the matching prior.

Any changes will affect all viewports assigned to prior exams.

Be sure to click Save Viewport Info to apply your changes.

If the hanging protocol includes “other related” exams, you can navigate to a viewport assigned to another related exam, and use the Case Info tab and change attributes (except for the listed CPT code) for other related exams.

Any changes will affect all viewports that assigned to other related exams.

Be sure to click Save Viewport Info to apply your changes.

If the hanging protocol contains multiple stages, click the Next Stage button and repeat steps 4-6.

Note Once you use the Next Stage button, you cannot return to the previous stage.

Click Save HP.

Open an exam with the edited hanging protocol to verify that the changes have been made as expected.

### Copying Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create a personal copy of another user’s hanging protocol (or template) using the steps below. Note that:

These steps will not open the hanging protocol or template for editing; they will just create a copy using the name you specify.

These steps cannot be used for hanging protocols and templates that are already grouped under your user name.

To copy a hanging protocol or template

In the Manager, click Open With (make sure the check box next to this button is cleared before clicking the button).

In the Select Hanging Protocol / Template dialog, select the hanging protocol or template you want to create a copy of.

Hanging protocols and templates are grouped by user name.

You can also select a hanging protocol or template under the sysAdmin user.

Click Save As.

In the dialog that displays, enter the name to use for the new hanging protocol (or template).

If you do not hold the MAGJ SYSTEM USER security key, you can save the hanging protocol as a user-level hanging protocol only under your own user name.

If you hold the MAGJ SYSTEM USER security key, you can save the hanging protocols as a user-level hanging protocol under your user name, or as a site-level hanging protocol under the sysAdmin user.

Click OK.

Note If you saved a copy of a hanging protocol, you will be prompted specify the name and level of the associated template as well.

### Deleting Hanging Protocols 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unneeded hanging protocols can be deleted as described below.

To delete a hanging protocol

In the Manager, click Open With (make sure the check box next to this button is cleared before clicking the button).

In the Select Hanging Protocol / Template dialog, select the hanging protocol you want to delete.

Hanging protocols are grouped by user name, with your user name displayed at the top.

You cannot delete other users’ hanging protocols.

If you hold the MAGJ SYSTEM USER security key, you can also select a hanging protocol under the sysAdmin user.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>![](vistarad-user-guide/199.png)</th>
<th><p>A deleted hanging protocol cannot be restored.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Click Delete, then click OK when you are asked for confirmation.

Click Close.

# Hanging Protocol Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

The Hanging Protocol Definition Dialog

Viewport Mapping Explained

Hanging Protocol Cookbook

Internal Hanging Protocols

## The Hanging Protocol Definition Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hanging Protocol Definition dialog is used to create or edit a hanging protocol. The following sections describe how each option in the dialog can be used. Sections are grouped by tab name (Case Info, Viewport Info, etc.). See the previous chapter for steps on how to create a hanging protocol.

### Common Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the Define Hanging Protocol dialog is being used, the informational area at the top of dialog and the buttons at the bottom of the dialog are always visible. The informational area displays details about the hanging protocol being created and the selected viewport. It is updated as successive viewports are selected.

![](vistarad-user-guide/200.png)

The buttons at the bottom of the dialog function as follows.

Previous– Use this button to re-select a viewport that you have already established case-level or viewport-level settings for. If you change settings in the dialog after using the Previous button, be sure to click Save Case Info or Save Viewport Info to apply your changes.

Next– Use this button to step from one viewport to the next as you are defining a hanging protocol. This button will be disabled until case- and viewport-level settings have been saved for the selected viewport.

Save Stage– Use this button to save settings for all viewports as a stage. This button will be disabled until case- and viewport-level settings have been saved for all viewports. For detailed steps describing how to create a staged hanging protocol, refer to the Hanging Protocol Cookbook on page [170](#hanging-protocol-cookbook).

Save HP– Use this button to save a hanging protocol after all case- and viewport-level settings have been saved for all viewports.

Save HPAs– Use this button to save a completed hanging protocol under a different name than the one initially specified.

Cancel– Use this button to discard the definition in progress and close the dialog.

### Case Info \| HP Lookup Area (for Current Exams)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/201.png)

The settings in the HP Lookup area determine which types of exams the hanging protocol being defined will apply to.

The HP Lookup area is active only when Current is the selected Case Type. The HP Lookup area displays the CPT code and modality code derived from the exam in the selected viewport.

Use CPT code– When this option is selected, the hanging protocol is associated with the same CPT code (procedure) as the current exam.

Use modality– When this option is selected, the hanging protocol is associated with the same modality as the current exam. Note that a hanging protocol associated with a modality will not be automatically selected if a different hanging protocol with a CPT appropriate for the exam being opened is present (details on page [139](#_Ref157332912)).

### Case Info \| Prior Attribute Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/202.png)

The settings in the Prior Attribute area determine the type, quantity, and organization of prior exams that will be retrieved by the hanging protocol being defined. The Prior Attribute area is active only when Matching Prior is the selected Case Type.

Note that the settings in the Up to, Max Priors and Match Type boxes are applied to all prior exams. Only the Prior Index box is set differently for each prior exam.

Up to– Use the two boxes to specify the maximum age of priors to be retrieved.

Max Priors– Use this box to specify the maximum number of priors to be retrieved.

If network capacity is limited or if the exams are likely to be very large,[^6] set this to a low number (1 or 2).

If the value in this box allows more priors to be retrieved than there is available space, any extra priors will still be opened. Depending on how the hanging protocol is designed, extra priors will either be placed in the last viewport(s) assigned to priors, or will open into the Preview window only.

By default, if a viewport (or group of viewports) contains multiple exams, the most recent exam will be shown on top. This behavior can be changed by using the Oldest Shown... check box (details on page [158](#_Ref148926400)).

Match Type– Use this box to specify how prior exams are identified. Use Exact CPT to retrieve only priors that exactly match the CPT code (procedure) of the current exam. Use Similar CPT to retrieve priors that are the same or similar to the current exam. Use Modality & Body part to retrieve the widest range of priors.

Note Similar CPT matching is site-specific. If exams that are presumed similar are not retrieved when Similar CPT matching is used, contact your Imaging Coordinator.

Prior Index– This box is enabled only if more than one prior exam will be visible at the same time. The viewport(s) with a prior index of 1 will contain the most recent prior. The viewport(s) with the highest prior index value will contain the oldest prior. For an example of how this box is used, see A Basic Hanging Protocol for Chest X-Rays on page [170](#_Ref148859968).

### Case Info \| Attribute Area (for Other Related Cases)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/203.png)

The settings in the Attribute area determine which types of other related cases (if any) will be retrieved by the hanging protocol being defined. The Attribute area is active only when Other Related Case is the selected Case Type.

Unlike the settings for matching priors, settings in the Attribute area can be different for each viewport (or group of viewports) that will be used to display a related case.

Up to– Use the two boxes to specify the maximum age of the related case to be retrieved.

Max Priors – Use this box to specify the maximum number of related cases to be placed in the active viewport (or group of viewports).

If the value in this box allows more cases to be retrieved than there is available space, any extra cases will still be opened. Depending on how the hanging protocol is designed, extra cases will either be placed in the last viewport(s) assigned to other related cases, or will open into the Preview window only.

By default, if a viewport (or group of viewports) contains multiple exams, the exams are ordered from most to least recent with the most recent exam shown ‘on top’. This behavior can be changed by using the Oldest Shown... check box (details below).

Match Type– Use this box to specify how related cases are identified. Note that the reference point for a related case is the value in the CPT box (described below), *not* the CPT or modality of the current exam.

Note Similar CPT matching is site-specific. If exams that are presumed similar are not retrieved when Similar CPT matching is used, contact your Imaging Coordinator.

CPT– This box displays the CPT code used as the basis for selecting a related case. The value in this box is derived from the CPT code of the exam in the currently selected viewport, and cannot be changed manually.

### Case Info \| Oldest Shown... Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/204.png)

The Oldest Shown... check box determines which exam is displayed on top if a viewport contains multiple prior or related exams. The setting in this box affects any viewport that contains multiple prior or other related exams.

If this check box is selected, the least recent exam will be displayed on top.

If this check box is cleared, the most recent exam will displayed on top.

Note that the setting in this check box does not alter how exams are sorted; it only determines which exam is initially visible.

### Case Info \| Local/Remote Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/205.png)

Local/remote settings are intended for sites that send or receive routed exams using VistARad. They determine which hanging protocols are available to users based on a user’s login.

Local Only– When this option is selected, the hanging protocol being defined will be automatically selectable for local users only (relative to where the exam being opened was acquired).

Remote Only– When this option is selected, the hanging protocol being defined will be automatically selectable for remote users only (relative to where the exam being opened was acquired).

Remote and Local– When this option is selected, the hanging protocol being defined will be automatically selectable without regard to the user’s location.

Note Local/remote settings can be overridden if a user manually selects a hanging protocol after turning off filtering (details on page [137](#manual-hanging-protocol-selection)).

### Case Info \| Use this Stage... Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/206.png)

The Use this stage... check box is intended for use with multi-stage hanging protocols that have “with priors” and “without priors” views defined.

If this check box is cleared, the first stage defined in a hanging protocol will always be the first stage displayed when that hanging protocol is used.

If this check box is selected for a particular stage, that stage will be the initial stage displayed if there are no prior exams retrieved when the hanging protocol is used. If prior exams *are* present, the first stage defined in the hanging protocol will be first stage displayed.

Note This setting applies only to matching priors. Exams retrieved as “other related cases” will not trigger the display of a “with priors” stage, even if this check box is selected.

For an overview of how staged hanging protocols work, see Using Stages on page [63](#_Ref137003237). For detailed steps describing how to create a staged hanging protocol, see the steps for A Staged Hanging Protocol for “With Prior” and “Without Prior” Views on page [173](#_Ref153180798).

### Case Info \| Disable Series Processing Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/207.png)

The Disable series processing check box indicates if an exam’s series UID is used to divide an exam between multiple viewports.

For hanging protocols that will display CT or MR exams, this check box should usually be cleared.

For hanging protocols that will display CR or DX exams, this check box should usually be selected.

For hanging protocols that will display US or XA (angiography) exams, or exams from other modalities, this check box can be set to suit your reading preference.

This check box applies to all exams that will be loaded by the hanging protocol.

### Case Info \| Regroup Leftover Image Sets check box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/208.png)

The setting in Regroup leftover image sets check box needs to be considered only when the hanging protocol you are defining:

Uses the Specify Attributes... list to explicitly map images into viewports.

Does not use series processing (the Disable series processing check box is selected).

When the resulting hanging protocol is used, and if there are leftover unmapped images, the Regroup leftover image sets check box determines how those unmapped images are organized.

When Regroup leftover image sets is selected, any unmapped images are left in the groups established by the settings in the Specify Attributes... list. Each group is presented as a thumbnail in the Preview window, and may be loaded into a viewport as a separate image set.

When Regroup leftover image sets is cleared, all unmapped images are combined into a single group. That group is presented as one thumbnail in the Preview window, and may be loaded into a viewport as a single image set.

### Viewport Info \| Clone/Placeholder Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/209.png)

The Clone/Placeholder options are enabled only if the active viewport contains images cloned from a previous viewport. Selecting an option dictates how images in the active viewport are handled.

Clone of Viewport– Select this option if the viewport’s contents are to be treated as an actual clone (usually for applying specialized image processing).

Place Holder– Select this option if the viewport’s contents are being used as stand-ins for additional series. For example, if you have used a six-series exam as a model, but you want the hanging protocol being defined to handle more than six series, you would clone one or more series, and then select Place Holder for each clone.  
  
Note that while Place Holder allows you to create spaces for additional series, it cannot be used for viewports that contain an entire exam.

### Viewport Info \| Specify Attributes List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/210.png)

Usually, *generic mapping* (details on page [169](#viewport-mapping-explained)) is used by a hanging protocol to organize images into viewports. If this does not produce the desired results, the Specify Attributes... list can be used for greater control over what goes into a specific viewport.

The Specify Attributes... list lets you set up a comparison between specific attributes (on the left side of the list) and operators and values that you specify (on the right side of the list). In the resulting hanging protocol, if the actual attribute of a given image meets the criteria specified by the operator and value you supply, that image is placed in the viewport.

You may want to use the Specify Attributes... list if:

You want certain types of images to always appear in a particular viewport (and you want the viewport to be empty if those images are absent in an exam).

You want to use something other than the series UID to divide an exam into groups of images.

You want to subdivide one or more series into smaller groups.

When you use the Specify Attributes... list, you are *explicitly mapping* images into a viewport. For more information about mapping, see Viewport Mapping Explained on page [169](#viewport-mapping-explained)).

Existing attributes

The first three columns in the Specify Attributes... list show the attributes you can use as the basis of your comparison. These attributes are derived from the header data of the selected image in the active viewport.

![](vistarad-user-guide/211.png)

| ![](vistarad-user-guide/212.png) | If your site uses different modality models to perform the same procedure, you should review the image attributes produced by each modality to make sure the design of your hanging protocol can accommodate vendor-specific variations in header data. You may need to work with one or both of the vendors to obtain the DICOM elements necessary to build a particular protocol. |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Operators

To place images into a viewport based on a particular attribute, you usually need to specify both an operator and a comparison value (see below). Any operator can be changed by clicking on the operator and choosing a different one from the pull-down list that displays.

![](vistarad-user-guide/213.png)

Most operators function exactly as they are named, and must have a comparison value to act on. The following operators are exceptions.

Not Present – Used to split a group of images based on the on the absence of a contrast agent. If the Contrast Agent attribute is not present, or if the attribute has a value of N, No, none, etc., a comparison using the Not Present operator is considered True.

Present – Used to split a group of images based on the presence of a contrast agent. If the Contrast Agent attribute is present, and contains a value that cannot be construed as No or none, a comparison using the Present operator is considered True.

Split – used to sub-divide a series into groups based on unique instances of a value (rather than the value itself). For an example of how this operator is used to split an MR sequence based on Echo Time, see the steps for An MR Hanging Protocol that Splits a Series on page [178](#_Ref153180801)

Values

Along with an operator (see above), a user-supplied value is needed to compare to the existing value for a given attribute. To enter a comparison value for an attribute, click in the rightmost Value column and type a value.

Values are case-sensitive.

Multiple values can be used; separate each value with a backslash (\\. Multiple values are handled as ORs; only one of the values must match for a condition to be considered true.

![](vistarad-user-guide/214.png)

General usage notes

The Specify Attributes... list can be used on a viewport-by-viewport basis.

When you use the Specify Attributes... list, you can use the Regroup Leftover Image Sets checkbox to determine how to handle any unmapped images.

Settings in the Specify Attributes... list are applied only if one or more rows in the list are selected when the Save Viewport Info button is clicked.

If multiple rows are selected, then all the conditions in all the rows must be met for images to be included in the viewport (multiple conditions are treated as AND statements).

For a step-by-step example of how the Specify Attributes... list is used, see An MR Hanging Protocol that uses Links and Explicit Mapping on page [175](#_Ref153180800).

### Viewport Info \| Pixel Processing Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/215.png)

The Pixel Processing area reflects the window/level and sharpen/smooth settings that will be applied to images in the active viewport.

Use Image Preset– When this option is selected, you can use the Select button to have an image preset applied to the active viewport. If you select an image preset, other options in the Pixel Processing area are not used.

Set Window/Level– When this option is selected, the window/level values in the two boxes to the right of this option will be applied to the active viewport. The values can be edited manually if desired.

Other– When this option is selected, window/level values in the active viewport are set using information from the acquisition device and/or set automatically based on pixel information in the first image in the viewport. If both the Modality W/L and the Auto W/L check boxes are selected, the Auto W/L setting applies only if there are no window/level values available from the acquisition device

Sharpen– This box reflects any sharpen (F+) or smooth (F–) filters specified for images in the active viewport. A value of F0 indicates no sharpen/smooth filters will be used.

Invert– This check box indicates if window/level values are inverted in the active viewport.

The modality of the images in the active viewport will determine if the Set Window/Level option is initially selected, or if the Other option is initially selected.

### More Viewport Info Tab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vistarad-user-guide/216.png)

The options in the More Viewport Info tab reflect processing values derived from the active viewport. These values can be edited or left as-is.

Grid– Indicates if images are stacked (1 x 1) or tiled (*N* x *N*).

Scale– Indicates the scale value that will be applied. Fit to Size is selected if no manual scale adjustments have been made in the active viewport. Set Scale is selected if scale has been changed manually in the active viewport.

Orientation– Indicates any manual flip/rotate adjustments made in the active viewport.

Apply To Image Set– Indicates the initial “Apply To” settings in the active viewport (details on page [81](#_Ref257120277)). Note that the settings specified here will override default Apply To settings when the hanging protocol is used.

Link Settings– Indicates the link settings (if any) for the active viewport (details on page [55](#loading-viewports)). Note that these settings affect all viewports in the “link group”. Settings specified here will override default link settings when the hanging protocol is used.

Sorting– Indicates the sort order used in the active viewport. The Advanced button can be used to specify a different sort order (details on page [88](#_Ref136930313)).

## Viewport Mapping Explained

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a hanging protocol calls for groups of images in an exam (typically, series) to be distributed across multiple viewports, *mapping* is used to determine which images go where. Mapping can be *generic* or *explicit*. Generic and explicit mapping can be used together in the same hanging protocol.

Generic mapping

When generic mapping is used, viewports are loaded on a “first-come first-served” basis based on series UID. If all series in a given procedure are acquired and processed in a consistent order, exams for that procedure will display in a predictable manner in the Viewer.

However, generic mapping is “blind” to specific attributes of a series. It does not, for example, place a series in a viewport based on the presence or absence of a contrast agent.

If a hanging protocol includes at least one generically-mapped viewport, that viewport can serve as an overflow viewport for additional images, or for images that do not meet any criteria for explicit mapping within a hanging protocol.

Explicit mapping

When explicit mapping is used, a viewport will be loaded only if images with one or more user-specified attributes are present. Otherwise, the viewport is left empty.

Two ways that explicit mapping can be used are:

To ensure that a series with a specified set of attributes is always displayed in the same viewport. (For example, placing series into specific viewports based on anatomical plane and/or processing type).

To subdivide an existing series between multiple viewports. (For example, splitting a multi-echo MR sequence into multiple viewports).

Explicit mapping is defined using the Specify Attributes... list in the Hanging Protocol Definition dialog (details on page [164](#_Ref150761455)). For instructions on how to create a sample hanging protocol that uses explicit mapping, see An MR Hanging Protocol that uses Links and Explicit Mapping on page [175](#_Ref153180800).

## Hanging Protocol Cookbook

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains step-by-step instructions for creating the following hanging protocols:

A Basic Hanging Protocol for Chest X-Rays

A Staged Hanging Protocol for “With Prior” and “Without Prior” Views

An MR Hanging Protocol that uses Links and Explicit Mapping

An MR Hanging Protocol that Splits a Series

### A Basic Hanging Protocol for Chest X-Rays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose

These steps demonstrate basic hanging protocol creation techniques. They also demonstrate how “stand-in” exams can be used if you do not have enough prior exams of the desired procedure available.

The resulting hanging protocol will display a current chest x-ray exam on one monitor and up to four similar prior exams. The use of a 2-head workstation is presumed.

To create this hanging protocol, you will need five exams for the same patient, where one exam must be a chest x-ray (CR or DX), and the other four can be of any procedure as long as they have a modality of CR or DX.

Steps to model the hanging protocol

Create a new template where the left monitor contains a single viewport and the right monitor contains four equally sized viewports.

In the Manager, use the Open With button to open the five exams using the template you created in Step 1.

In the Preview window, locate the chest x-ray. The chest x-ray will represent the current exam.

Load the current exam into the large viewport on the left monitor. Adjust each viewport to the display settings that you want to include in the hanging protocol definition. Note that:

You do not have to manually adjust window/level if window/level information is sent from the modality; instead, you can have the hanging protocol pick up that information when you define the hanging protocol itself.

If you do not explicitly set a scale percentage, “Fit to Size” will be used for each occupied viewport.

Be sure that the “Apply To” settings are set as desired for each viewport. For CR images, it is recommended Apply To for window/level and orientation be turned off (details on page [81](#_Ref257122958)).

Steps to define the hanging protocol

In the Viewer menu, click Customize \| Create Hanging Protocol. In the box that is displayed:

Enter a name for the hanging protocol.

If the HP Level box is enabled, select User-level.

Click OK.

The Define Hanging Protocol dialog will be displayed. Notice that:

The viewport on the left monitor is highlighted automatically.

In the Define Hanging Protocol dialog, the Case Info tab is selected, and Case Type is set to Current.

Use the Case Info tab to specify how the current exam is to be identified and handled:

In the HP Lookup area, verify that Use CPT code is selected. The displayed CPT code is what will be used to match the hanging protocol being created with exams with a specific procedure.

Verify that the Disable series processing check box is selected. This ensures that all images in the current exam are loaded into a single viewport.

Click Save Case Info. This indicates that you have finished setting parameters for the current exam.

The Viewport Info tab will display automatically.

Verify that the settings in the in the Pixel Processing area are set as desired; change these settings as needed.

Click Save Viewport Info, then click Next.

Note that:

The viewport in the upper left corner of the right monitor is selected automatically. Because this viewport contains a different exam than the previous viewport, the Case Info tab is displayed again.

In the Case Info tab, Case Type is already set to Matching Prior.

Use the steps below to specify what types of exams qualify as matching prior exams.

In the Prior Attribute area, set the Up To box to 5 years, and the Max Priors box to 4.

Leave the Match Type value set to Exact CPT. This means that only exams with the same procedure as the current exam will be considered priors (optionally, you can set Match Type to Similar CPT to retrieve both the same and similar procedures).

Note that the Prior Index box to is set to 1—this indicates that the most recent of any prior exams is to be displayed in the currently selected viewport.

Click Save Case Info.

Note that the same viewport remains selected in the Viewer, and that the Viewport Info tab is now displayed.

In the selected viewport, verify that the settings in the Pixel Processing area are set as desired; change these settings as needed. Click Save Viewport Info, then click Next.

Repeat steps 6 through 8 for the three remaining viewports; for each viewport, note how the Prior Index box increments to 2, 3 and 4 (oldest).

After saving settings for the last viewport, click Save HP.

Close the model exams.

Test the new hanging protocol:

Open a CR exam that has the same procedure as the current exam you used to model the hanging protocol.

Verify that the current exam is displayed on the left monitor, and that up to four prior exams are displayed on the right monitor.

In any viewport that contains a prior, double-click to toggle back and forth between full screen and standard view.

### A Staged Hanging Protocol for “With Prior” and “Without Prior” Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose

These steps demonstrate how to create a two-stage hanging protocol, and how to automatically select a stage based on the presence or absence of priors.

These steps assume that you are familiar with the basics of creating a hanging protocol that includes priors (see the previous section). These steps also assume that you are familiar with the concept of stages (details on page [63](#_Ref137003237)).

Steps to model the hanging protocol

Identify the template(s) you want to use for each stage:

One stage will include priors, one stage will show the current exam only.

You can use the same template for each stage, or you can use a different template for each stage.

Locate the exams you will use to model the current exam and one or more priors.

In the Manager, use the Open With button to open all of the exams using the template you want to use in the “with priors” stage.

Using the Preview window, load viewports in the Viewer window as desired.

Steps to define the hanging protocol

In the Viewer menu, click Customize \| Create Hanging Protocol. In the box that is displayed:

Enter a name for the hanging protocol. If the HP Level box is enabled, select User-level.

Click OK.

In the Define Hanging Protocol dialog, define your “with priors” stage:

Use the HP Lookup area to set selection attributes for the current exam. Click Save Case Info to proceed.

Optionally, use the Viewport Info and More Viewport info tabs to set attributes for each viewport with current images. Click Save Viewport Info, then click Next to proceed.

Use the Prior Attributes area to set selection attributes for the prior exam(s). Click Save Case Info to proceed.

Optionally, use the Viewport Info and More Viewport info tabs to set attributes for each viewport with prior images. Click Save Viewport Info, then click Next to proceed.

After saving settings for the last viewport, click Next Stage.

The Define Hanging Protocol dialog will close and the “Multi-stage HP Creation In Process” box will display.

IMPORTANT Do not click any buttons in the Multi-stage... box. This box will be used later.

In the upper-right corner of the Viewer window, click the TP: \<name\> button, then click OK when you are warned that viewports will be cleared.

Note If you are using the same template for both stages, skip the above step, and clear viewports manually by clicking ![](vistarad-user-guide/217.png).

Load viewports with the current exam to define your “without priors” view.

In the “Multi-stage HP Creation In Process” box, click Next Stage.

When the Define Hanging Protocol dialog displays, it will show the Viewport Info tab with settings for the second stage. Use the Save Viewport Info and the Next buttons to save settings for each viewport.

Select the Case Info tab and select the Use this stage when priors are not available check box.

Click Save Case Info, then click Save HP.

Test the new hanging protocol to verify that it works as designed.

### An MR Hanging Protocol that uses Links and Explicit Mapping 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose

These steps demonstrate how to create a hanging protocol that used image attributes to explicitly map MR images into specific viewports. These steps also demonstrate how to link series automatically for navigation.

Because of the variability of MR exams, these steps focus only on the process of mapping viewports, rather than trying to create a hanging protocol for an actual reading scenario. These steps are built around a model exam that is made up of sagittal and axial series and that primarily uses two different pulse sequences (though other forms may be present).

These steps assume that you have created a hanging protocol before. If you have not, it is suggested you work through the A Basic Hanging Protocol for Chest X-Rays section on page [170](#_Ref148859968) before performing the steps below.

Steps to model the hanging protocol

Locate an MR exam that contains two or more sagittal and axial series and that uses at least two different pulse sequences.

Locate or create a template that contains at least four viewports (two rows and two columns) per monitor, and open the exam using that template.

In the Preview window, double-click any series in the exam to load the exam into the Browser window.

In the Browser window, use the title bar and the info area to identify two sagittal series and two axial series.

For each plane, each series should reflect a specific pulse sequence.

Tip If plane and pulse sequence information is not visible in the title bar, click the info area at the bottom of the viewport to open the Image Info window, and use the Display Data tab to locate the information.

Arrange the series in the Viewer window as shown below. (If you are using multiple monitors, arrange the images in any one monitor.)

![](vistarad-user-guide/218.png)

To link the series in each plane together, do the following:

Click ![](vistarad-user-guide/219.png) in an occupied viewport in the top row, and then click the other occupied viewport in the top row to link them together.

Turn off the link tool by right-clicking once.

Link the bottom row of occupied viewports together.

In the top row of viewports, drag down on the ![](vistarad-user-guide/220.png) icon and make sure Window/Level is *not* checked. Repeat this step for the middle row of viewports.

Set other display settings for each viewport as desired.

Tip Be sure that the “Apply To” settings are set as desired for each viewport. For MR images, it is recommended that Apply To for window/level be turned off (details on page [81](#_Ref257124612)).

Steps to define the hanging protocol

In the Viewer menu, click Customize \| Create Hanging Protocol.

In the box that is displayed, enter a name for the hanging protocol. Verify that User-level is shown in the HP Level box, then click OK.

In the Define Hanging Protocol dialog, the Case Info tab will display by default. Make sure the Disable Series Processing check box is cleared.

Click Save Case Info. The Viewport Info tab will display.

In the Specify Attributes area, locate the row(s) that specify the plane and pulse sequence used.

In the row(s) that specify the plane and pulse sequence, do the following:

Set the Operator to Contains.

Note the contents of the non-editable Value column (the column to the left of the operator).

In the editable Value column, change the value to indicate the plane and/or pulse sequence used. Whenever possible, eliminate unneeded characters, but be sure to retain the structure inferred in the non-editable Value column.

![](vistarad-user-guide/221.png)

Tip The editable value does not have to contain any component of the displayed comparison value—for example, you can specify a value of T1 even if the comparison value indicates that the active series is a T2-wieghted sequence. In the resulting hanging protocol, only series with “T1” in the referenced field would be placed in the applicable viewport.

Note The above example shows sample values in the Series Description row. At your site, these values may be presented differently, or stored in a different row, or split between two rows.

IMPORTANT Make sure that any rows you have edited are selected. If you have edited multiple rows, you can use CTRL-click to select each row. To de-select one of several selected rows, CTRL-click the row again to de-select it.

Click Save Viewport Info, then click Next.

The next occupied viewport will be selected.

Note that the rows you edited in the previous step are automatically selected and now appear at the top of the Specify Attributes... list.

Repeat step 6 above for each viewport, using values that will indicate the plane/processing combination that is unique to each viewport.

After saving settings for the last viewport, click Save HP.

Close the model exam, and test the new hanging protocol to verify that it works as designed.

### An MR Hanging Protocol that Splits a Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purpose

Some MR devices may produce series that contain multiple views of the same slice, rather than putting each view into a separate sequence. If this occurs, a hanging protocol can be used to split each view into separate viewports.

The steps below demonstrate how to create a hanging protocol that will split a multi-echo sequence into separate viewports based on Echo Time.

Because of the variability of MR exams, these steps focus only on the process of splitting a sequence, rather trying to create a hanging protocol for an actual reading scenario.

These steps assume that you have created a hanging protocol before. If you have not, it is suggested you work through the A Basic Hanging Protocol for Chest X-Rays section on page [170](#_Ref148859968) before performing the steps below.

Steps to model the hanging protocol

Locate an MR exam with that contains a series where images with different Echo Times are interleaved.

Open the exam using a template that contains at least four viewports per monitor.

In the Preview window, double-click any series in the exam to load the exam into the Browser window.

In the Browser window, use the title bar or the info area to identify the multi-echo sequence.

Determine where Echo Time values are displayed.

Echo Time values may be displayed in the info area near the bottom of the viewport.

If the Echo Time values are not apparent, click the info area. In the dialog that displays, Echo Time values will be displayed near the bottom of the Display Data tab.

Scroll through the multi-echo sequence to determine how many unique Echo Time values are present.

If the Image Info dialog is already open, values in the dialog (including Echo Time) will update as you scroll.

You do not need to note the actual values; you need to determine only how many “sets” of unique values are present.

Load the multi-echo sequence into the Viewer window.

Create a copy of the multi-echo sequence in an adjacent viewport using the clone feature (details on page [86](#_Ref136930309)).

If there are more than two Echo Time values, clone the multi-echo sequence as until the total number of viewports used is the same as the number of Echo Time values.

Optionally, link each multi-echo sequence together using the ![](vistarad-user-guide/222.png) icon.

Set other display settings for each viewport as desired.

Tip Be sure that the “Apply To” settings are set as desired for each viewport. For MR images, it is recommended that Apply To for window/level be turned off (details on page [81](#_Ref257124866)).

Steps to define the hanging protocol

In the Viewer menu, click Customize \| Create Hanging Protocol.

In the box that is displayed, enter a name for the hanging protocol, ensure that User-level is shown in the HP Level box, then click OK.

In the Define Hanging Protocol dialog, the Case Info tab will display by default. Make sure the Disable Series Processing check box is cleared.

Click Save Case Info. The Viewport Info tab will display.

In the Specify Attributes area, locate a row that indicates the presence of the multi-echo sequence. Often this will be the Series Description or Series Name row. In that row:

Set the Operator to Contains.

In the editable Value column, change the value shown to the minimum contiguous string (usually PD) that indicates the type of processing.

Next, locate the Echo Time row and set the Operator to Split.

![](vistarad-user-guide/223.png)

Note When Split is used, there is no need to enter anything in the editable Value column; using Split will create a separate image set for each unique value found.

Use CTRL-click to select each row.

Click Save Viewport Info, then click Next.

The next occupied viewport will be selected. Because this viewport contains a cloned series, the Clone/placeholder options near the top of the Viewport Info tab will be selected.

> **IMPORTANT:** Select the Place Holder option.

Review the first two rows in the Specify Attributes area to ensure that PD is being used as a selection attribute, and that Split is being used as an operator for Echo Time.

Click Save Viewport Info, then click Next.

If you have additional cloned viewports, repeat step 6 above.

After saving settings for the last viewport, click Save HP.

Close the model exam, and test the new hanging protocol to verify that it works as designed.

## Internal Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Internal hanging protocols serve two purposes: they organize exams in the Preview window, and they provide basic exam display on 1-, 2-, and 4-head workstations.

Internal hanging protocols are listed under the sysAdmin user in the Select Hanging Protocol / Template dialog. Most internal hanging protocols will not be visible unless the filter in this dialog is disabled.

All internal hanging protocols can be identified by the SYS_INT suffix in their names. Internal hanging protocols cannot be edited or deleted.

When they are visible, internal hanging protocols are listed alphabetically along with any site-level hanging protocols defined by users who hold the MAGJ SYSTEM USER security key.

Tip If you are using an internal hanging protocol and would like to refine how it works, you can load exams with that hanging protocol, and then use it as the basis of a new hanging protocol that will be saved in your personal collection. Once created, a personal (user-level) hanging protocol takes precedence over a similar internal (site-level) hanging protocol for purposes of automatic selection.

The internal hanging protocols listed in the following sections are always available at a VistARad workstation.

### Baseline Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Baseline hanging protocols are used to organize images in the Preview window. They are also used as the foundation of other hanging protocols.

In normal installations, baseline hanging protocols will not be automatically selected (other internal hanging protocols will take precedence over them). Baseline hanging protocols are visible in the Select Hanging Protocol/Template dialog only if filtering is turned off.

The following baseline hanging protocols are present:

CPTMatchAllSYS_INT – Baseline hanging protocol used for single-modality exams that are *not* DX, CR, CT, or MR; will split exams by series.

CRSYS_INT – Baseline hanging protocol for CR and DX exams; will split exams by image.

CTSYS_INT – Baseline hanging protocol for CT exams; will split exams by series and scout/localizer.

MODMatchAllSYS_INT – Will split images in an exam based on modality. Intended for exams that contain images from multiple modalities (such as radio fluorography exams).

MRSYS_INT – Baseline hanging protocol for MR exams; will split exams by series (sequence) and scout/localizer.

### 1-head Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following internal hanging protocols are designed for workstations that use one diagnostic quality monitor.

CT_1-hd_SYS_INT

GenRad_1-hd_SYS_INT

NM_1-hd_SYS_INT

US_1-hd_SYS_INT

XA_1-hd_SYS_INT

These hanging protocols are used only if they are manually selected, or if there are no other applicable hanging protocols for the exam being opened.

### 2-head Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following internal hanging protocols are designed for workstations that use two diagnostic quality monitors.

[CT_Thorax_2-hd_SYS_INT](\l)

[CT_2-hd_SYS_INT](\l)

[GenRad_2-hd_SYS_INT](\l)

[MR_2-hd_SYS_INT](\l)

[NM_2-hd_SYS_INT](\l)

[RF_2-hd_SYS_INT](\l)

[US_2-hd_SYS_INT](\l)

[XA_2-hd_SYS_INT](\l)

These hanging protocols are used only if they are manually selected, or if there are no other applicable hanging protocols for the exam being opened.

#### CT_Thorax_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of CT thorax exams; exams are split into multiple viewports based on series UID; up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>One stage only. (4-up_4-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout</strong></td>
<td>![](vistarad-user-guide/224.png)</td>
</tr>
<tr class="odd">
<td><strong>Image layout</strong></td>
<td>1x1</td>
</tr>
<tr class="even">
<td><strong>Image display</strong></td>
<td>Window/level settings for the first series are optimized for the display of lung tissue; for the second series, soft tissue; for the third series, bone. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

#### CT_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of CT exams, exams are split into multiple viewports based on series UID; up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (9-up_4-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (4-up_4-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/225.png)</td>
</tr>
<tr class="odd">
<td><strong>Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/226.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>1x1</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied. Otherwise, window/level is calculated automatically based on the first image in each series. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

#### GenRad_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Purpose</strong></th>
<th>Display of x-ray (CR and DX) exams; 1 exam per viewport; up to 4 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (1-up_2-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (Wide-2_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong><br />
Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/227.png)</td>
</tr>
<tr class="odd">
<td><strong><br />
Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/228.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>In stage 1, images are shown 1x1. In stage 2, images are shown 2x1 in a viewport that occupies both monitors.</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied. Otherwise, window/level is calculated automatically based on the first image in each exam. Changes to scale and sharpness will affect all images in a viewport. Changes to window/level and orientation affect only the selected image.</td>
</tr>
</tbody>
</table>

#### MR_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Purpose</strong></th>
<th>Display MR exams; exams are split into series based on series UID. Up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (9-up_9-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (9-up_9-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/229.png)</td>
</tr>
<tr class="odd">
<td><strong>Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/230.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>1x1</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied. Otherwise, window/level is calculated automatically based on the first image in each series. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

#### NM_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of NM exams, 1 exam per viewport. Up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>One stage only. (2-up_2-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout</strong></td>
<td>![](vistarad-user-guide/231.png)</td>
</tr>
<tr class="odd">
<td><strong>Image layout</strong></td>
<td>1x1</td>
</tr>
<tr class="even">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied to the images. Otherwise, window/level is calculated automatically based on the first image in each series. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

#### RF_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of RF exams; each exam split into 2 viewports based on the modality of the images (CR or RF). Up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (2-up_2-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (1-up_1-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/232.png)</td>
</tr>
<tr class="odd">
<td><strong>Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/233.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>1X1</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td><p>If window/level values from the modality are available, those values are applied to the images. Otherwise, window/level is calculated automatically based on the first image in each series.</p>
<p>In viewports that contain CR images, changes to scale, window/level, and sharpness will affect all images in the viewport. Changes to orientation will affect only the selected image.</p>
<p>In viewports that contain RF images, changes to scale, window/level, orientation and sharpness will affect all images in the viewport.</p></td>
</tr>
</tbody>
</table>

#### US_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of US exams; 1 exam per viewport. Up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (1-up_1-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (Wide-2_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/234.png)</td>
</tr>
<tr class="odd">
<td><strong>Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/235.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>In stage 1, images are shown 3x3. In stage 2, images are shown 3x6 in a single viewport that occupies both monitors.</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied to the images. Otherwise, window/level is calculated automatically based on the first image in each series. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

#### XA_2-hd_SYS_INT

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Summary</strong></th>
<th>Display of x-ray angiography exams; exams are split into series based on series UID. Up to 2 priors may be loaded automatically.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Stages (template)</strong></td>
<td>If priors are present, stage 1 is displayed first. (4-up_4-up_SYS_INT)<br />
If no priors are present, stage 2 is displayed first. (4-up_4-up_SYS_INT)</td>
</tr>
<tr class="even">
<td><strong>Viewport<br />
layout<br />
(stage 1)</strong></td>
<td>![](vistarad-user-guide/236.png)</td>
</tr>
<tr class="odd">
<td><strong>Viewport<br />
layout<br />
(stage 2)</strong></td>
<td>![](vistarad-user-guide/237.png)</td>
</tr>
<tr class="even">
<td><strong>Image layout</strong></td>
<td>1x1</td>
</tr>
<tr class="odd">
<td><strong>Image display</strong></td>
<td>If window/level values from the modality are available, those values are applied to the images. Otherwise, window/level is calculated automatically based on the first image in each series. Changes to scale, window/level, orientation, and sharpness will affect all images in the viewport.</td>
</tr>
</tbody>
</table>

### 4-head Hanging Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following internal hanging protocols are designed for workstations that use four diagnostic quality monitors.

CT_4-hd_SYS_INT

GenRad_4-hd_SYS_INT

MR_4-hd_SYS_INT

NM_4-hd_SYS_INT

US_4-hd_SYS_INT

XA_4-hd_SYS_INT

These hanging protocols are used only if they are manually selected, or if there are no other applicable hanging protocols for the exam being opened.

Tip If you are using an internal hanging protocol and would like to refine how it works, you can load exams with that hanging protocol, and then use it as the basis of a new hanging protocol that will be saved in your personal collection. Once created, a personal (user-level) hanging protocol takes precedence over a similar internal (site-level) hanging protocol for purposes of automatic selection.

# Teaching Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter covers:

Enable Teaching Files in VistARad

Make a Teaching File Out of an Image

Send a Teaching File to MIRC

VistARad provides the ability to create teaching files from images in VistARad exams. Files you upload to the Medical Imaging Resource Center (MIRC) server will be searchable and available as teaching references for any user searching MIRC for particular types of images. This chapter describes how to enable the Teaching Files function in VistARad, create a teaching file, and upload it to your facility’s teaching folder on the MIRC server.

Note When teaching files are uploaded using VistARad, VistARad automatically removes personally identifiable information from the image header.  However, removal of “burned-in” information from pixel data is not a capability of VistARad or of the MIRC software. As the responsible party creating the teaching file, you need to ensure that images you upload do not contain any personally identifiable information.

Note When a teaching file uploads to MIRC from VistARad, no annotations that were created in VistARad will be saved.

## Enable Teaching Files in VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the VistARad Viewer, click View, then Settings, then the Teaching Files tab.

Check the EnableTeaching Files box, and fill in the information for Connection Parameters.

Fill in the values under AE Title, Host Name, and Port/Socket number where indicated. Consult with your Imaging Coordinator for support, as a Security Key is required to make edits here.

Click the Test button, and click OK in the box that says “Remote SCP is available.”

Click Apply, and close out of Settings.

## Make a Teaching File Out of an Image, Image Set or Exam

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display an image in the VistARad Viewer that you wish to make into a teaching file.

Right-click the image on the screen to bring up the context menu, then click Add to Teaching Files.

> ![](vistarad-user-guide/238.png)

Click Image, Image Set, or Exam, to send the image(s) to the Teaching Files section of the Scrapbook window.

Repeat the process for any additional images, image sets or exams you wish to use.

## Redact Sensitive Information From a Teaching File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When teaching files are uploaded using VistARad, VistARad automatically removes personally identifiable information from the image header. As the responsible party creating the teaching file, you need to ensure that images you upload do not contain any personally identifiable information. VistARad now offers the capability to “erase” such information contained in the image itself. This process is called *redacting*.

1.  Select the image to be edited and drag it into a viewport. Right-click on the image, and then select Add to Teaching Files \| Image from the drop-down menu:

> ![](vistarad-user-guide/239.png)

> ![](vistarad-user-guide/240.png)

2.  In the Scrapbook, click on the Teaching Files tab. Click to select the image you added.
3.  ![](vistarad-user-guide/241.png) Find the “eraser” image on the right of the toolbar. This is the \[Redact Teaching File\] button.

> ![](vistarad-user-guide/242.png)

> Click the \[Redact Teaching File\] button.

4.  Using the mouse, draw a rectangle on the image so that the material you wish to redact is covered:

> ![](vistarad-user-guide/243.png)

5.  A context menu appears, allowing you to edit, delete or apply the “redact region” to the image:

> ![](vistarad-user-guide/244.png)

## Send a Teaching File to MIRC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click here ![](vistarad-user-guide/245.png) in the Teaching Files toolbar.

A warning will display not to upload any files with “burned-in” personally identifiable information (see *Redact Sensitive Information From a Teaching File*, above). Click Continue.

The Teaching Files window will display. Select the Title box, and enter the name to be used for the teaching file.

> ![](vistarad-user-guide/246.png)

Click the drop-down menu under Category and click the desired category.

The Findings box displays a tree of possible diagnoses, with subcategories either displayed or collapsed. Double-click the appropriate descriptive terms in the Findings box. Click the left arrow and the selected terms will populate the Findings field to its left.

Similarly, find and click the appropriate terms in the Anatomic Location box, and click the left arrow to populate the Anatomic Location field to its left.

Note The Findings and Anatomic Location boxes are searchable by keyword. Type the desired term in Search, just below each box.

Enter any desired free text into the boxes for Diagnosis and Abstract. You can either type the text directly in or use Copy/Paste.

Click Send, or Send and Close, and the images will be sent to your facility’s teaching folder on the MIRC server.

Once you have finished, click here ![](vistarad-user-guide/247.png) in the Teaching Files toolbar to open the MIRC server Query Page in your Web browser.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

annotation– A line, shape, text box, or number added to an image by a user. Annotations added to locked exams are saved. Annotations added to unlocked exams are discarded.
Browser window– The window used to display images for review or interpretation.
CCOW – *See* Clinical Context Object Workgroup Protocol
cine– A tool that lets you display each image in a viewport in rapid succession, creating a flipbook effect.
Clinical Context Object Workgroup Protocol (CCOW) – A Health Level 7 (HL7) standard protocol designed to enable dissimilar healthcare software applications to synchronize in real-time, and at the user-interface level.
context management – An approach to database management that allows users to choose a subject once in one application, and have all applications containing information on that same subject “tune” to the data they contain. This eliminates the need for the user to redundantly select the subject in the varying applications.
hanging protocol– A set of rules that govern how an exam and any related prior exams are displayed in the Viewer window. Each user can define hanging protocols that reflect their personal presentation preferences, or can use pre‑defined hanging protocols.
hidden image set– An image set that is loaded into a viewport, but not yet visible. The Contents bar in the upper right corner of a viewport indicates if hidden image sets are present.
image set– A group of one or more images. VistARad divides exams into image sets based on the exam’s attributes. Examples: 1) a CT exam with a scout and two series will be typically divided into three image sets: one for the scout, and one for each series. 2) a two-image chest X-ray is usually treated as a single image set.
key images– An image of interest that has been marked by a user. Key images are displayed in the Scrapbook window. The presentation state of a key image is saved when the key image is marked, and is retained in future viewing sessions. Key images cannot be marked, unmarked, or changed after an exam’s status has been updated to Interpreted.
layout– The number of images displayed in a viewport, or the number of viewports displayed in a window. Layout is generally expressed in terms of rows and columns. A layout of 1x1 is referred to as 1-up or stacked view. A layout of multiple rows and columns is referred to as a tiled view.
lock– A flag used to indicate that an exam is being interpreted. A locked exam can be viewed by another user, but the status of a locked exam can be updated only by the user who holds the lock.
Magnifying Glass– A tool used to define an area of an image that can be manipulated independently from the rest of the image.
Manager window– The window that provides access to exams and reports in the VistA System.
mensurated scale – A visual signifier for the length of an image, displayed (when enabled) to the left of the image in the VistARad viewport.
MIRC– Medical Imaging Resource Center
Monitored Site– A site, remote to the logon site, whose exam list data is viewed by a radiologist who reads for that site.
presentation state– The information that describes how a particular image is to be displayed. VistARad saves the presentation state of key images, allowing user specified window/level, zoom, and annotations to be retained for future viewing sessions.
Preview window– The window that shows a representative image for each image set in an exam. The Preview window is populated whenever an exam is loaded. In List View mode, allows user management of some aspects of exam loading.
printset– A group of related exams as defined in the Radiology Package. Exams in a printset have individual case numbers, and are displayed as separate items in a VistARad exam list. Opening any exam in a printset will open all exams in the printset; the printset is interpreted as a unit and results in the creation of a single report for all of the member exams.
Radiology Package– A VistA System component responsible for order entry, registration, reporting, verification, and tracking functions specific to radiology. VistARad uses status information from the Radiology Package to organize exams. Status updates performed using VistARad are passed back to the Radiology package.
Radiology Package user– A person with user privileges defined within the Radiology Package. Certain Radiology Package privileges enable certain VistARad functions. Most importantly, only users defined as Radiology Technologists, Radiology Residents, or Radiology Staff can *lock* exams and change exam status using VistARad.
remote reading– The process of interpreting exams at an alternate location using VistARad and local copies of exam images routed from the acquisition site.
ReadList– A VistARad feature that allows a user to successively display and review unread exams with increased efficiency. When ReadList is active, exams are preloaded to minimize delay, and the user can close an existing exam and open a new exam in a single operation.
redact, redacting – The process of blocking out part of an image which has “burned in” personally identifiable information before the image is submitted as a teaching file.
reserve– A flag used to indicate that an exam has been preloaded using ReadList and will soon be locked for interpretation. A reserve can be overridden; if this occurs the exam is removed from the ReadList sequence of the user who reserved the exam.
routing– The process responsible for sending images across a wide area network from an acquisition site to one or more other sites. Routing can be performed automatically when an exam is acquired, or on-demand from a properly configured VistARad workstation. If a VistARad workstation is part of a routing system, exam lists in the Manager will include an RC (remote cache) column.
screen template– A predefined set of viewports for a single screen. Screen templates are used to streamline the creation of templates.
Scrapbook window–The window used for the display and manipulation of key images, and for uploading “teaching file” images – and information describing them – to a MIRC server..
series UID – A unique value in an image’s header file used to identify each series in an exam. Used by VistARad to divide series between viewports.
stage– A hanging protocol that contains multiple arrangements of the same exams. When a hanging protocol with stages is used, users can switch from one stage to another without having to reload the exams.
teaching file – An image, image set or exam that has been saved and sent to a Medical Imaging Resource Center (MIRC) server for educational or reference purposes.
thumbnail– A representation of one or more images displayed in the Preview window.
template– A named definition of the number, size, and arrangement of viewports in the Viewer window. Templates are used as the basis of hanging protocols. As an alternative to using a hanging protocol, a user can display images using a template only.
viewport– A discrete area used to display images. Viewports provide the primary work area for interpreting exams.
Viewer window– The primary window used for the display and interpretation of images on the VistARad workstation.
VIX – VistA Imaging Exchange Service, which automates retrieval of remote data to a local VIX server’s cache.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3
3D software, using with VistARad, 102
A
abstracts. *See* thumbnails
active patient, 59, 105
All Active Exams list, 30
angles, measurement
adding, 94
annotations
adding, 91
cloned images and, 91
properties of, 98, 109
saving, 91
Apply Filter button, 124, 134
Apply To
initial settings for, 114
setting in hanging protocols, 164
using, 79
areas, measurement
adding, 94
Attribute area (for other related cases), 153
attributes, DICOM
displaying, 67
viewport mapping with, 165
attributes, image, changing, 72
Auto Number tool, 93
auto-window/level
setting in hanging protocols, 163
using, 74
auxiliary windows, 8
B
Browser window
described, 5
layout of, 78
loading, 53
using, 64
C
Calibrate tool, 97
Case \# field, 31
case presets. *See* hanging protocols
CCOW, 43
Change Monitor Configuration button, 104
cine tool
initial settings for, 114
using, 87
Clinical Context Object Workgroup (CCOW), 43
clones, image
creating, 84
in hanging protocols, 159
Close/Update dialog
suppressing during ReadList, 20
using, 69
closing exams, 69
color images, 64
context changes icon images, 44
context changes indicator icon, 44
context management, 43
Context Management Settings tab, 44
copy tool
initial settings for, 114
using, 81
CPRS Tools menu option, 44
CPT codes
default hanging protocols and, 143
hanging protocol selection and, 132
in exam lists, 31
CT_2-hd_SYS_INT, 180
CT_Thorax_2-hd_SYS_INT, 179
current exams, identifying, 132
custom exam lists
described, 30
displaying tabs for, 110
show/hide settings for, 106
using, 14
D
Day/Case field, 31
DICOM attributes
displaying, 67
viewport mapping with, 165
dictation interface
described, 47
opening reports using, 49
settings for, 111
direction, cine, 87
Disable Series Processing check box, 157
E
ellipses, annotation
adding, 92
properties of, 98
Exam History list, 24
exam lists
fields in, 31
refreshing, 15
site-wide settings for, 34
sorting, 14
tabs for, 106
types of, 30
using, 13
exam reports, 38
exam requisitions, 37
exams
closing, 69
current, 132
hidden, 62
opening
basic steps, 16
high-priority, 22
multiple, 23
reference quality, 23
with ReadList, 18, 19
with selected hanging protocols, 133
with templates only, 123
prior, selection of, 132
priority of, 33
routed, 119
routing on-demand, 117
selecting, 13
status of, 7, 34
exiting VistARad, 12
explicit mapping, 165
F
filters
for hanging protocols, 134
for remote reading, 119
for templates, 124
flipping images, 75
fonts
annotation and measurement, 98
Manager window, 107
Reports window, 40
settings for, 109
viewport title bar, 7
Frame of Reference UID, 83
full-screen view, 73, 78
G
generic mapping, 165
GenRad_2-hd_SYS_INT, 181
glossary, 195
grayscale, inverting, 75
H
hanging protocols
creating, 137
current exams in, 132
default, 143
deleting, 147
described, 131
designing, 137
dialog for defining, 149
editing, 145
expanding scope of, 144
implementing, 140
internal, 133, 177
modelling, 139
multiple matches dialog, 136
resolving differences between, 134
routing-related options for, 155
saving copies of, 146
selecting automatically, 135
selecting manually, 133
settings for, 110
site-level, 133
stages, 61
user-level, 133
Health Summary reports, 39, 40
hidden exams, 62
hidden image sets, 62
history, exam, 24
Hounsfield area
freehand, 95
rectangle, 94
Hounsfield units, measuring, 94
HP Lookup area, 151
I
icon
context changes indicator, 44
ID \# field, 31
image data, displaying, 67
Image Date/Time field, 31
image information area, 8
image presets
creating and applying, 76
in hanging protocols, 163
image sets. *See Also* images
described, 195
hidden, 62
loading into viewports, 59
images
3D display of, 102
adjusting individually, 79
annotating, 91
capturing and saving, 103
cine tool and, 87
clearing, 58
cloning, 84
context changes icon, 44
copying properties of, 81
displaying, 16
full-screen view, 73
inverting, 75
key, 57
layout of, 78
linking, 82
measuring features in, 93
moving, 85
paging and scrolling, 55
presets for, 76
reference quality, 23
reorienting, 75
resetting, 76
scout, 56
sharpening, 76
sorting, 86
window/level, changing in, 74
zooming, 72
Imaging Data window, 67
Imaging Loc field, 31
Img Type field, 31
indicators, orientation, 75
internal hanging protocols, 177
Interp By field, 31
interpreted, updating exams to, 69
IntStat field, 31
invert, 75
K
key images
described, 57
marking, 57
Scrapbook window and, 64
unmarking, 58
keyboard
adjusting images with, 113
image presets and, 76
navigating with, 56, 113
L
labels, annotation, adding, 92
layout
changing, 78
described, 195
wide viewports and, 61
lines, annotation
adding, 92
properties of, 98
lines, measurement
adding, 93
properties of, 98
links
creating, 82
in hanging protocols, 164
initial settings for, 114
List view, 60
Load Status field, 32
localizer, 65
localizer images, 56
Location Type field, 32
Lock field, 32
logging in, 8
long case number, 31
lookup, patient, 21
loop, cine, 87
M
magnifying glass, 88, 196
MAGSRT field, 33
management
context, 43
Manager window
described, 3
exam lists in, 13
fonts in, 107
opening exams from, 16
opening reports from, 37
settings for, 111
mapping, viewport, 165
Mark icon, 57
masks, image, 89
measurements
adding, 93
Calibrate tool and, 97
cloned images and, 91
properties of, 98, 109
saving, 91
merge viewports, 127
MIRC, 188
Mod field, 33
modality
hanging protocols selection and, 132
image presets and, 76
Modifier field, 33
monitored site, 121
monitors, wide viewports and, 61
More Viewport Info tab, 164
mouse
images with, 55
settings for, 112
MR_2-hd_SYS_INT, 182
multiple exams, opening, 23
N
NM_2-hd_SYS_INT, 183
numbers, annotation, 93
O
Oldest Shown on Loading check box, 154
on-demand routing, 117
Onl field, 33
Open button, 16
Open With button, 133
Open/Reserved Exams list, 30
orientation
changing, 75
copying, 81
other related exams
defining selection criteria for, 141
described, 132
Overriding Annotations, 99
P
Patient Exams list, 30
patient lookup, 21
Patient Name field, 33
Patient Profiles
opening, 38
working with, 40
patients
active, 30, 59
opening exams for, 21
opening records for, 37
Pixel Processing area, 163
placeholders, 159
pre-op indicator, 33
preserve sort order, 14
presets, 76
Preview window
described, 4
display state icons in, 53
using, 59
printsets
described, 196
opening, 25
voice dictation and, 51
Prior Attribute area, 152
prior exams
defining selection criteria for, 141
identifying based on current exam, 132
in viewports, 7
Priority field, 33
Procedure field, 33
Pt Loc’n field, 33
pushpins, 108
R
Rad Dic field, 33
Radiology Package, 196
range, cine, defining, 87
RC column, 119
RC field, 33
ReadList
described, 17
remote reading and, 120
Selection ReadList, 19
sorting and, 14
starting, 18
stopping, 19
Recent Exams list, 30
records, patient, 37
rectangles, annotation
adding, 92
properties of, 98
reference quality images, 23
Refresh Exams button, 15
REG DATE, 33
REG DATE-SORT, 33
related exams, 132
Remote Read Filter, 119
remote reading
described, 196
settings for, 114
using VistARad for, 119
reorienting images, 75
reports
displaying, 38
opening for dictation, 49
working with, 40
Reports window, 40
requisitions
opening, 37
working with, 40
restore sort, 14
RF_2-hd_SYS_INT, 184
rotating images, 75
Route Request dialog, 117
routing
described, 117
hanging protocol filtering for, 155
on-demand, using, 117
settings for, 114
ruler, 93
S
Save As, 146
saving image captures to VistA, 103
scale
changing, 72
copying, 81
full-screen view, 73
in Magnifying Glass, 88
scale, mensurated
described, 196
Scout Image window
changing layout in, 78
scout images
described, 56
generating, 66
settings for slice lines, 109
Scrapbook window
and key images, 57
changing layout in, 78
using, 64
screen templates, 129
search. *See* patient lookup
Selection ReadList, 19
series. *See Also* images, image sets
adjusting images in, 72
cloning, 84
hidden, 62
linking, 82
moving, 85
sorting, 86
splitting, 85
series processing, disabling, 157
settings dialog, 108
sharpen/smooth
changing, 76
copying, 81
shortcut keys
adjusting images with, 113
image presets and, 76
navigating with, 56, 113
show text outline, 98
show/hide
measurements, 95, 97
Shutter option, 89
site-level hanging protocols, 133
SORT_IMG_DT field, 33
sorting
exam lists, 14
image sets in Viewer, 86
images using hanging protocols, 164
Specify Attributes... list, 160
speed, cine, 87
splitting image sets
in Viewer, 85
using hanging protocols, 160
SSN, search using, 21
SSN-4 field, 33
stacked view, 78
stages
auto-selecting based on priors, 156
defining, 150
using, 61
status, exam
in exam lists, 34
in viewports, 7
updating, 69
updating automatically, 20
SYS_INT hanging protocols, 177
sysAdmin user, 133
T
tab
Context Management settings, 44
teaching files, 188
teleradiology, 117
Template Designer, using, 127
templates
creating, 125
deleting, 128
described, 123
editing, 126
saving copies of, 146
selecting in the Manager, 123
selecting in the Viewer, 124
terms of use, 1
text, annotation
adding, 92
editing, 96
properties of, 98
thumbnail image size, 60
thumbnails
described, 60
icons in, 53
tick marks, 55
tiled view, 78
timeouts, 12
title bar, viewport, 7
toolbars, resizing, 105
U
units, setting measurement, 98
unread exams
exam list for, 30
opening, 16
updating status of, 69
US_2-hd_SYS_INT, 185
user settings, 108
user-level hanging protocols, 133
Using Calibrate, 97
Using Show/Hide, 97
V
Viewer window
described, 5
hidden image sets in, 62
loading manually, 53
size, setting, 104
stages, 61
using, 60
wide viewports and, 61
viewports
adjusting images in, 72, 79
changing layout of, 78
clearing, 58
described, 5
hidden image sets in, 62
linking, 82
loading, 53
paging and scrolling in, 55
settings for, 105, 114
templates for, 127
title bars in, 7
wide, 61, 127
VistARad, 8
described, 3
exiting, 12
starting, 8
switching between windows in, 9
using, 10
VistARad Settings dialog, 108
VIX
described, 198
VOI LUT, 54
voice dictation
settings for, 111
using VistARad interface for, 49
Voxar 3D, using with VistARad, 102
W
Ward field, 34
wet reads, 22
wide viewports, 61
window/level
changing, 74
copying, 81
setting in hanging protocols, 163
setting in image presets, 76
X
XA_2-hd_SYS_INT, 186
Z
zoom, changing, 72
[^1]: The loading of header/text data cannot be paused.
[^2]: Talk or Powerscribe
[^3]: If you inadvertently lock the middle button or scroll wheel on your mouse into a function where the cursor presents with the ![](vistarad-user-guide/248.png) icon, this will cause the images to scroll rapidly when you move the cursor up and down or from side to side over the exam on the screen. To unlock this function, click once on the middle button or scroll wheel.
[^4]: It also opens from the “Display Compression Information” context menu option of the Image Compression Alert icon.
[^5]: The determination of what is a ‘similar’ CPT code is based on the CPT matching defined using the E/E VistARad CPT Matching Set \[MAGJ E/E CPT MATCHING SET\] option on the VistA Host. See Chapter 3 in the *Imaging Installation Guide* for details.  
[^6]: While VistARad (Patch 18 and later) can manage several large exams at once, it has been determined that Windows XP cannot. Windows XP has a 2GB per process limit. Loading several large prior exams (such as MRs) may go beyond this process limit and cause a crash.
