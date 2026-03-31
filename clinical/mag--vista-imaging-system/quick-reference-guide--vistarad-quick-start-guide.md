---
title: VistARad Quick Start Guide
doc_type: QRG
doc_label: Quick Reference Guide
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
menu_options: 0
description: 
audience: 
keywords: 
  - vistarad
  - contents
  - table
  - exam
  - image
  - window
  - images
  - exams
  - guide
  - start
page_count: 0
word_count: 10458
section_count: 33
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/VistARad_Quick_Start_Guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/VistARad_Quick_Start_Guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

![](vistarad-quick-start-guide/001.png)

IMAGING SYSTEM

VistARad Quick Start Guide

Version 3.0 99  
March 2018

Office of Enterprise Development

Health Provider Systems

VistARad Quick Start Guide  
VistA Imaging 3.0 MAG\*3.0\*199  
March 2018Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Office of Enterprise Development  

Internet: <span class="mark">REDACTED</span>  
SharePoint: <span class="mark">REDACTED</span>

Contents

Revision Table

| Date      | Rev | Notes                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mar 7, 2018   | 14      | In support of MAG\*3.0\*184, TimeOutSeconds key was added into the configuration file. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                   |
| May 16, 2017  | 13      | In support of MAG\*3.0\*184, the 2FA sign on PIV PIN instructions replaced the access/verify instructions for sign on. The requirement for IE 11 was also added.                                                                                                                                                                                                                            |
| April 7, 2016 | 12      | In support of MAG\*3.0\*153, the section Measuring Image Features: Hounsfield Areas on page 25 has been updated to remove references to the Ellipse tool in the Hounsfield measurement. <span class="mark">REDACTED</span>                                                                                                                                                                  |
| Aug 6, 2013   | 11      | Updates for MAG\*3.0\*133. Preview window re-organization & thumbnail size preference. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                   |
| June 4 2012   | 10      | Updates for MAG\*3.0\*120. Integrates the Clinical Context Object Workgroup (CCOW) protocol at the user- and patient-context levels. Dictation interface now allows multiple locked exams to be open concurrently. New (optional) pixel erase function allows removal of sensitive information prior to storing images to the MIRC Teaching file system. <span class="mark">REDACTED</span> |
| Feb 3 2011    | 9       | Updates for Patch 115. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                   |
| Jun 8 2010    | 8       | Updates for Patch 90. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                |
| Mar 31 2010   | 7       | Corrections related to packaging issues with graphics and links. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                         |
| Dec 10 2009   | 6       | Updates for Patch 101. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                   |
| Dec 03 2007   | 5       | Remove non-essential p65 content. Reorganize *Surveying Exams* section. Updates for Patch 76. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                            |
| Feb 21 2007   | 4       | Updates for Patch 65. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                    |
| April 3 2006  | 3       | Updated for release of Patch 18. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                         |
| Jun 20 2005   | 2       | Pre-alpha draft. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                         |
| May 23 2005   | 1       | VEHU draft. <span class="mark">REDACTED</span>                                                                                                                                                                                                                                                                                                                                              |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [Getting Help](#getting-help)
- [Getting Started](#getting-started)
  - [New Users](#new-users)
- [Starting & Exiting VistARad](#starting-exiting-vistarad)
  - [Starting VistARad](#starting-vistarad)
  - [How VistARad Windows Behave](#how-vistarad-windows-behave)
  - [Exiting VistARad](#exiting-vistarad)
- [Locating & Opening Exams](#locating-opening-exams)
  - [Using the Manager Window](#using-the-manager-window)
    - [Exam Locks and Exam Reserves](#exam-locks-and-exam-reserves)
  - [Opening Exams](#opening-exams)
    - [Opening an Exam I](#opening-an-exam-i)
    - [Opening an Exam II](#opening-an-exam-ii)
  - [Using ReadList](#using-readlist)
    - [Starting ReadList](#starting-readlist)
    - [Stepping through Exams with ReadList](#stepping-through-exams-with-readlist)
    - [Stopping ReadList Manually](#stopping-readlist-manually)
  - [Working with Routed Exams](#working-with-routed-exams)
- [Surveying Exams](#surveying-exams)
  - [How VistARad Displays Exams](#how-vistarad-displays-exams)
    - [The Preview Window](#the-preview-window)
    - [The Viewer Window](#the-viewer-window)
    - [The Browser Window](#the-browser-window)
  - [Images and Viewports](#images-and-viewports)
    - [Navigating in Viewports](#navigating-in-viewports)
    - [### ## Conditional Indicator Icons](#conditional-indicator-icons)
    - [Image Compression Alert](#image-compression-alert)
    - [VOI LUT Indicator](#voi-lut-indicator)
  - [Navigating with Scouts](#navigating-with-scouts)
  - [Navigating between Patients](#navigating-between-patients)
- [Working with Images](#working-with-images)
  - [Adjusting Images](#adjusting-images)
    - [Using Built-In Pan, Scale, and Window/Level](#using-built-in-pan-scale-and-windowlevel)
    - [Using Image Manipulation Tools](#using-image-manipulation-tools)
    - [Using Arrow Keys for Precise Control](#using-arrow-keys-for-precise-control)
  - [Changing Layout in a Viewport](#changing-layout-in-a-viewport)
    - [Using Full-Screen View](#using-full-screen-view)
  - [Changing Layout in a Window](#changing-layout-in-a-window)
  - [Manipulating Image Sets](#manipulating-image-sets)
    - [Moving an Image Set](#moving-an-image-set)
    - [Cloning an Image Set](#cloning-an-image-set)
    - [Removing an Image Set](#removing-an-image-set)
  - [Mensurated Scale](#mensurated-scale)
  - [Annotations](#annotations)
    - [Annotating Images](#annotating-images)
    - [Measuring Image Features: Ruler and Angles](#measuring-image-features-ruler-and-angles)
    - [Measuring Image Features: Hounsfield Areas](#measuring-image-features-hounsfield-areas)
    - [Working with Annotations](#working-with-annotations)
    - [Overriding Saved Notations](#overriding-saved-notations)
- [Key Images](#key-images)
    - [Marking Images](#marking-images)
    - [Working with Key Images](#working-with-key-images)
    - [Unmarking Images](#unmarking-images)
- [Reviewing Online Records](#reviewing-online-records)
    - [Displaying Records](#displaying-records)
    - [Working with Health Summaries](#working-with-health-summaries)
- [Closing Exams](#closing-exams)
- [Hanging Protocols & Templates](#hanging-protocols-templates)
  - [Template & Hanging Protocol Basics](#template-hanging-protocol-basics)
    - [Basic Hanging Protocol Settings](#basic-hanging-protocol-settings)
    - [Handling Multiple Matches](#handling-multiple-matches)
- [VistARad and Voxar 3D](#vistarad-and-voxar-3d)
  - [Loading Images from VistARad into Voxar](#loading-images-from-vistarad-into-voxar)
  - [Saving a Voxar Capture to VistA as a New Series](#saving-a-voxar-capture-to-vista-as-a-new-series)
- [Teaching Files](#teaching-files)
  - [Creating Teaching Files](#creating-teaching-files)
  - [Redact Sensitive Information from a Teaching File](#redact-sensitive-information-from-a-teaching-file)
- [Context Management](#context-management)
  - [Context Management](#context-management-1)
  - [The Clinical Context Object Workgroup Protocol](#the-clinical-context-object-workgroup-protocol)
  - [The Context Management Settings Tab](#the-context-management-settings-tab)
  - [Context Changes](#context-changes)
- [VistARad and Voice Dictation](#vistarad-and-voice-dictation)
  - [About the VistARad Dictation Interface](#about-the-vistarad-dictation-interface)
  - [Opening Exams and Reports for Dictation](#opening-exams-and-reports-for-dictation)
    - [Before you Begin](#before-you-begin)
    - [Opening an Exam and Report for Dictation](#opening-an-exam-and-report-for-dictation)
  - [Multiple Locked Exams](#multiple-locked-exams)
    - [When Multiple Locked Exams for Different Patients are open](#when-multiple-locked-exams-for-different-patients-are-open)
    - [Dictation Dialog forced under certain conditions](#dictation-dialog-forced-under-certain-conditions)
    - [Opening a Report (only) for Dictation](#opening-a-report-only-for-dictation)
- [Remote Data/Image Views](#remote-dataimage-views)
This document is intended for radiologists and clinicians who use the VistARad diagnostic workstation. Information is included for new users about how to use key VistARad features. For returning users, a summary of changes in the most recent VistARad patch is provided, with an explanation of how those changes affect existing VistARad features.
It is assumed that:
- You are familiar with the Windows environment.
- The client is installed either on a Windows XP-based or a Windows 7-based diagnostic workstation, and the KIDS is installed on the VistA Host.
- IE 11 is installed.
- Appropriate test exams are available.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use of the VistARad diagnostic workstation is subject to the following provisions:

| ![](vistarad-quick-start-guide/002.png) | Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistarad-quick-start-guide/003.png) | No modifications may be made to the VistARad diagnostic workstation without the express written consent of the VistA Imaging National Project Manager.                                                                                                                                                                                                                                                                                                                                |
| ![](vistarad-quick-start-guide/004.png) | The Food and Drug Administration classifies the VistARad software as a medical device. Modifications to the VistARad diagnostic workstation, such as the installation of unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).                                                                                                                                                                        |
| ![](vistarad-quick-start-guide/005.png) | Image presentation quality depends on monitor resolution, and on regular monitor testing and calibration to correct for display degradation over time. It is the responsibility of the clinical practitioner to determine if images presented on a VistARad workstation are of sufficient quality for clinical interpretation. Any concerns regarding monitor resolution or calibration should be reported immediately to the Imaging Coordinator before interpretation is performed. |

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To learn how to use VistARad for basic exam interpretation, review the Basic Workflow topics listed below. For information about speeding up and fine-tuning interpretation, review the topics listed under Workflow Refinements.

| Basic Workflow      | See…                        |     | Workflow Refinements  | See…                                  |
|-------------------------|---------------------------------|-----|---------------------------|-------------------------------------------|
| Log in                  | page [2](#starting-vistarad)    |     | Use ReadList              | page [6](#_Toc104284954)                  |
| Open an exam            | page [5](#opening-exams)        |     | Select a hanging protocol | page [6](#opening-an-exam-ii)             |
| Display patient records | page [26](#_Toc117391487)       |     | Move, clone images        | page [19](#moving-an-image-set)           |
| Survey exams            | page [9](#surveying-exams)      |     | Annotate/measure images   | page [21](#annotations)                   |
| Work with images        | page [15](#working-with-images) |     | Change layout             | page [17](#changing-layout-in-a-viewport) |
| Close an exam           | page [27](#_Ref125167116)       |     | Mark images               | page [25](#key-images)                    |
| Work with images        | page [15](#working-with-images) |     | Context Management        | page [35](#context-management)            |
|                         |                                 |     | Multiple Locked Exams     | page [38](#multiple-locked-exams)         |
|                         |                                 |     |                           |                                           |

# Starting & Exiting VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Starting VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If VistARad is interfaced to a voice dictation system such as Talk or PowerScribe, log in to the voice dictation software before starting VistARad.

Double-click the VistARad shortcut on the Windows desktop, or go to the Start menu and select AllPrograms \| VistA Imaging Programs \| MAG_VistARad.

If the Connect To box displays, select which VistA System you want to connect to, then click OK.

Make sure you have a valid PIV card attached to the computer. In the Windows Security box, choose the correct certificate and type in your PIN code when prompted in the ActivClient Login box. Then click OK.

Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate two-factor authentication (2FA), the application will revert the user to the Access/Verify screen. If the VistA Sign-on box displays, type your access and verify codes in the Access Code and Verify Code boxes, then click OK.

If the Select Division box displays, double-click the division you want to log in to.

When VistARad starts, both the Manager and Viewer windows open.

## How VistARad Windows Behave

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer window is designed to stretch across multiple monitors, and is usually not resized or minimized. Other VistARad windows can be sized, minimized, or ‘tacked’ into place as needed.

The Viewer

The buttons in the upper right corner of the Viewer work as follows:

![](vistarad-quick-start-guide/006.png) Clicking this button minimizes the Viewer window.

![](vistarad-quick-start-guide/007.png) This button is disabled.

![](vistarad-quick-start-guide/008.png) Clicking this button exits VistARad.

Other VistARad windows

Except for the Viewer window, other VistARad windows have the following buttons in their upper right corners:

![](vistarad-quick-start-guide/009.png) (or ![](vistarad-quick-start-guide/010.png) ) Clicking this button lets you control which windows stay visible while you are working with the Viewer, and which windows that you want ‘out of the way’ when you are not actively using them.

![](vistarad-quick-start-guide/011.png) If present, clicking this button either maximizes the window to cover the entire screen or restores the window to its original size. This button is not available in the Preview, Scout, or Reports window.

![](vistarad-quick-start-guide/012.png) Clicking this button minimizes the window.

Restoring minimized windows

Use one of the buttons in the Viewer window toolbar to restore minimized windows.

![](vistarad-quick-start-guide/013.png)

Alternatively, press \<CTRL+W\> or use the Windows taskbar to restore any window.

## Exiting VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to the menu bar in either the Manager or the Viewer and click File \| Exit VistARad.

If the Close Exams/Update Status dialog displays, make sure the Interpret? and Annotation fields are set as desired for each exam in the dialog, then click OK. For details, see page [27](#_Ref103862839).

# Locating & Opening Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using the Manager Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manager window is used to locate and open exams and reports.

![](vistarad-quick-start-guide/014.png)

Exam lists, which are used to organize exams into manageable groups, are displayed as a row of tabs near the top of the Manager window. Many sites use customized exam lists to create specific groupings of exams. These lists, if available, can be viewed by clicking the Custom tab.

You can use the settings under View \| Settings \| Manager \| General to show or hide exam lists. Some lists, such as the Unread Exams list, cannot be hidden.

### Exam Locks and Exam Reserves

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistARad, locks and reserves are used to prevent two radiologists from interpreting the same exam.

![](vistarad-quick-start-guide/015.png)

Unless locks are explicitly disabled, unread exams are locked on a first come, first served basis—the exam is automatically locked in the name of the first radiologist to display an unread exam.

If a radiologist closes a locked exam without updating its status, the lock is removed, and the exam can be locked and interpreted by a different radiologist.

Exam reserves are a ‘pre-lock’ used for exams that have been loaded into memory as part of the ReadList process. A reserved exam is automatically locked when it is displayed.

For details about ReadList, see page [6](#_Toc104284954).

## Opening Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections explain two of the most frequently used methods used to open an exam. For additional methods, see the *VistARad User Guide*.

### Opening an Exam I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use these steps to open an exam and to automatically select a hanging protocol. (Hanging protocols are described on page [28](#hanging-protocols-templates).)

1.  Display the Manager window by clicking ![](vistarad-quick-start-guide/016.png) in the Viewer toolbar.
2.  In the Manager window, click the Unread Exams tab.
    - To open the selected exam in the list, click Open or press \<ENTER\>.
    - To open any exam in the list, select the exam you want to open, then double-click the exam, or click Open.
3.  As the exam opens and images are loaded, additional prompts or windows may display:
    - Usually, the requisition for the exam displays automatically.
    - If more than one matching hanging protocol is found, you are asked to select which hanging protocol you want to use. For details, see page [29](#handling-multiple-matches).
    - If the voice dictation interface of VistARad is enabled, the report for that exam automatically opens for dictation. For details, see page [37](#about-the-vistarad-dictation-interface).
    - If the exam being opened is locked, and if not all image sets are loaded in the Viewer window, the Preview window displays. For complex exams (such as CT and MR exams), the Preview window can be used to monitor and alter the order in which series are loaded. For details, see page [9](#the-preview-window).
4.  Images in the Viewer can be interacted with as soon as they display. For more details about the Viewer, see page [9](#the-preview-window).

### Opening an Exam II 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use these steps to open an exam using a manually selected hanging protocol. (Hanging protocols are described on page [28](#hanging-protocols-templates).)

Display the Manager window by clicking ![](vistarad-quick-start-guide/017.png) in the Viewer toolbar.

In the Manager window, click the Unread Exams tab.

Select the exam you want to open.

Make sure the check box to the right of the Open With button is cleared.

Click Open With.

Use the dialog that opens to select a hanging protocol.

Hanging protocols are grouped under each username, and a default collection is available under the “sysAdmin” group.

The viewport arrangement of the selected hanging protocol is shown in the Preview area near the bottom of the dialog.

Select the hanging protocol or template you want to use, and click OK.

<span id="_Toc104284954" class="anchor"></span>As the exam opens and images are loaded, additional prompts or windows may display:

Usually, the requisition for the exam displays automatically.

If the voice dictation interface with VistARad is enabled, the report for the exam automatically opens for dictation. For details, see page [37](#about-the-vistarad-dictation-interface).

If the exam being opened is locked, and if not all image sets are loaded in the Viewer window, the Preview window displays. For details, see page [9](#the-preview-window).

## Using ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ReadList lets you successively display all unread exams in an exam list. When ReadList is active, you can step from one unread exam to the next in a single step, without displaying the Manager, and with minimal wait times.

### Starting ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display the Manager window by clicking ![](vistarad-quick-start-guide/018.png) in the Viewer toolbar.

In the Manager window, click the Unread Exams tab.

Click the ReadList button, located near the middle of the Manager window. This opens the first unread exam in the list.

A matching hanging protocol is selected automatically. If there are multiple matches, you are prompted to select the hanging protocol you want to use. For details, see page [29](#handling-multiple-matches).

Any priors identified by the selected hanging protocol also open automatically.

The exam and any priors display. As you are reviewing the displayed exam, the next exam in the Unread list is reserved and loaded into memory. Any applicable priors are loaded as well.

![](vistarad-quick-start-guide/019.png)

Note If the voice dictation interface for VistARad is enabled, the report for the exam being opened displays in the voice dictation window. Save any findings you entered for that exam before the next exam in VistARad.

### Stepping through Exams with ReadList

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When ReadList is active, you can step through exams without using the Manager. When you are ready to close an exam, do the following:

If VistARad has been integrated with a voice dictation system, and if you have a report open in that system, save or sign the report.

In VistARad, press \<CTRL + N\>, click Next in the Manager, or click ![](vistarad-quick-start-guide/020.png) in the Viewer toolbar. The Close Exams/Update Status dialog opens.

Set the values in the Close Exams/Update Status dialog as desired. For details, see page [27](#_Ref148231953).

Click OK to close the Close Exams/Update Status dialog.

After the dialog is closed, the next exam in the ReadList sequence displays.

VistARad automatically refreshes the active exam list, and preloads and reserves the next exam in the list.

ReadList mode continues until all unread exams have been displayed or until ReadList is stopped manually.

### Stopping ReadList Manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop ReadList manually, click the Stop RL button located near the middle of the Manager window. (This button is only visible when ReadList is active.) The currently displayed exam remains open, but no additional exams open once the currently displayed exam is closed.

## Working with Routed Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your workstation is set up for remote reading, you can use VistARad to interpret copies of exams routed to you from other sites. Working with a routed exam that is temporarily stored on your workstation is much faster than retrieving that exam from the originating site.

When you log in to a site to read exams from a remote location, the Manager window displays the Remote Read Filter button and the RC column to indicate that routed exams may be present.

![](vistarad-quick-start-guide/021.png)

The process to open and interpret a routed exam is the same process used for non‑routed exams. For information about opening exams, see page [5](#opening-exams).

Certain settings control how VistARad manages prior exams and ReadList functions when routed exams are present. To review these settings, click View \| Settings and select the Remote/Local Reading tab.

A VistARad workstation can also be set up to route exams on-demand. For details, see the *VistARad User Guide* or the *Routing User Guide*.

# Surveying Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How VistARad Displays Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an exam has been opened using the Manager, images are generally loaded into the Preview and Viewer windows. Images can also be manually loaded into the Browser window.

### The Preview Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preview window provides a summary view of exams that are currently open. If the Preview window is not visible, it can be displayed by clicking ![](vistarad-quick-start-guide/022.png) in the toolbar near the top of the screen.

Each exam in the Preview is shown as one or more thumbnail images, where each thumbnail represents an *image set* consisting of one or more related images. General radiology (CR) exams are usually presented as a single image set. Cross-sectional (CT and MR) exams are usually presented as multiple image sets, with each thumbnail representing a series.

The Preview window (see screenshot below) tracks the display state of each image set in an open exam.

- If an ![](vistarad-quick-start-guide/023.png) icon is displayed in the thumbnail, the associated image set is (or has been) loaded and made visible in the Viewer or the Browser during the current load instance.
- If a ![](vistarad-quick-start-guide/024.png) icon is displayed in the thumbnail, the associated image set is partially loaded (loading is in progress, or was paused).
- If an ![](vistarad-quick-start-guide/025.png) icon is displayed in the thumbnail, the images are loaded into the Viewer window but are hidden. For details, see page [11](#navigating-in-viewports).
- If no icon is displayed in the thumbnail, the associated image set has been loaded but must be loaded manually.

Two presentation styles are available in the Preview window: a traditional thumbnail view; and “List view.” In the List view, progress bars shows the loading status of all the image sets in each exam, and other controls allow you to pause or resume loading of image sets, or to purge image sets to free up memory if needed.

A user preference allows you to use different sized thumbnail images in the List view. For details, refer to the *VistARad User Guide,* “Customizing Thumbnail Size.”

![](vistarad-quick-start-guide/026.png)

To load an image set manually

From either the traditional thumbnail or list view, drag the corresponding thumbnail image from the Preview window into a viewport in the Viewer window. You can also double-click any thumbnail to display the entire exam in the Browser window.

### The Viewer Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer window occupies most of the display space on a VistARad workstation, and is the primary workspace for exam interpretation. The Viewer window contains one or more *viewports* where images can be manipulated. Viewports are described on page [11](#images-and-viewports).

You can interact with images in the viewer as soon as they are visible, while the exam load continues in the background.

Depending on how the exam is opened, the Viewer window may not display the entire exam. To determine which images in an exam have been displayed, use the Preview window. For details, see page [9](#the-preview-window).

### The Browser Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Browser window provides a flexible work area for exams that do not lend themselves to display with a hanging protocol. To load an open exam into the Browser window, go to the Preview window and double-click any thumbnail image from that exam.

The Browser displays automatically when images are loaded into it from the Preview window. It can also be displayed (if loaded) by clicking ![](vistarad-quick-start-guide/027.png) (the same button used to open the Preview window).

Like the Viewer, the Browser window contains one or more *viewports* where images can be manipulated. Viewports are described below.

## Images and Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Viewer, Browser, and other image-oriented windows are made up of one or more *viewports*. A viewport can contain one or more exams, part of an exam (such as a series), or a single image.

The viewport title bar displays the case number, exam status[^1], exam date, and series ID, for the images in the viewport.

![](vistarad-quick-start-guide/028.png)The viewport contents title bar displays the number of images, series or sequences, and exams in the viewport.

The viewport info area displays information about the active image in the viewport.

If there are multiple images in a viewport, the active layout dictates if images are displayed 1-up (stacked) or in one or more rows and columns (tiled). In the Viewer and the Browser windows, the layout of each viewport can be changed independently. For details, see page [17](#changing-layout-in-a-viewport).

### Navigating in Viewports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a viewport, the Contents bar and tick marks indicate if there are multiple images present, and indicate your relative position in the group of images.

![](vistarad-quick-start-guide/029.png)

In a viewport that contains multiple images, you can do any of the following to display each image:

- Roll the scroll wheel of your mouse up or down while pointing to the viewport to step through images one at a time.
- Drag up and down using the scroll wheel (or middle mouse button) to scroll rapidly.
- Click the paging buttons located near the top of the viewport. A “page” is based on the current layout (number of visible images) in the viewport.

![](vistarad-quick-start-guide/030.png)If a viewport contains multiple exams or multiple series, only one exam/series can be active at once. Other exams or series are considered hidden. The Contents bar indicates if hidden exams or series are present.

To display a hidden exam or series, click on the Ex or S label on the Contents bar. Then click the item you want to display.

### ### ## Conditional Indicator Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad places indicator icons in the upper-right corner of images to alert you to certain conditions. These will appear in any viewport, regardless of the viewport’s parent window.

### Image Compression Alert 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad indicates a compressed image by displaying the Compression Alert icon ![](vistarad-quick-start-guide/031.png). Right-clicking on the icon displays a context menu with two options: Clicking Display Compression Details opens the Display Data tab of the Image Detail window. Clicking Hide Icon will hide it.

### VOI LUT Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad indicates that an image has a Value Of Interest Look Up Table (VOI/LUT) applied by displaying the ![](vistarad-quick-start-guide/032.png) icon in the upper-right corner of the image (the letters ‘LUT’ appear if the VOI/LUT is currently applied). By default, VistARad displays images with the first embedded VOI/LUT applied. Right-clicking the icon displays a context menu with other options listed, based on modality-supplied information.

For more details, refer to the *VistARad User Guide,* “Using Conditional Indicator Icons.”

## Navigating with Scouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scout (localizer) images, if present, load automatically into the Scout Image window when an exam is opened. To display the Scout Image window, click ![](vistarad-quick-start-guide/033.png) in the Viewer toolbar.

Scout images may load into a viewport in the Viewer if so directed by the hanging protocol in use.

In the Viewer, you can generate a scout image if the displayed exam contains images from intersecting planes. To generate a scout, select the image you want to use, right-click, and then click Create Scout. This adds the scout image to the Scout Image window.

> VistARad projects cross-referencing slice lines on all applicable cross-sections of simultaneously displayed image sets. VistARad synchronizes them to the stack position of the active viewport. Changing the active viewport re-applies and re-synchronizes all reference slice lines. This is the default behavior, which can be changed from the context menu accessible from the right of the Scout Image window button.

> NOTE This user preference setting persists until changed, even after VistARad is closed.

> NOTE When the Show X-Ref Slice Lines menu item is unchecked, slice lines appear only on the Scout Image window. When the menu item is checked, slice lines appear on both VistARad Viewer and the Scout Image window.

> An illustration of the context menu appears below.

![](vistarad-quick-start-guide/034.png)

## Navigating between Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Except for the Manager, all VistARad windows are designed to display information for only one patient at a time. When exams for multiple patients are open, only exams related to the active patient are visible.

All image-related windows include the Active Patient button in their title bars. The Active Patient button displays the name, SSN, age, and sex of the patient associated with the currently displayed exam.

![](vistarad-quick-start-guide/035.png)

When exams for multiple patients are open, you can click the Active Patient button and use a drop-down list to switch between each patient’s exams. Switching to a different patient updates all windows in VistARad.

# Working with Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Adjusting Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The most commonly used tools (pan, scale, window/level) are always assigned to specific buttons on your mouse. You can also temporarily assign any of the standard manipulation tools to the left button of your mouse.

### Using Built-In Pan, Scale, and Window/Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Point to the image you want to change.

Click the appropriate mouse button and drag the mouse.

![](vistarad-quick-start-guide/036.png)

\* Pan is the default operation, and is active when the mouse pointer looks like ![](vistarad-quick-start-guide/037.png). See the next section for details.

\*\* Scrolling is used for viewports that contain more than one image. See page [11](#navigating-in-viewports) for more details.

\*\*\* Window/level is the default operation. Settings for the right mouse button can be changed using the options under View \| Settings \| Mouse.

### Using Image Manipulation Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to the toolbar at the top of the window and click one of the following tools. You can also right-click an image and use the shortcut menu.

![](vistarad-quick-start-guide/038.png)

Point to the image you want to work with. The mouse pointer changes, showing the “active area” where the tool can be used.

Depending on which tool you have selected, do one of the following:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Tool</strong></th>
<th><strong>Pointer</strong></th>
<th><strong>Point to image, then...</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Window/level</td>
<td>![](vistarad-quick-start-guide/039.png)</td>
<td>Drag up or down to change window;<br />
drag left or right to change level.</td>
</tr>
<tr class="even">
<td>Zoom in/out</td>
<td>![](vistarad-quick-start-guide/040.png)</td>
<td>Drag up or left to increase zoom; drag down or right to decrease zoom.</td>
</tr>
<tr class="odd">
<td>Scale image to 100%</td>
<td>![](vistarad-quick-start-guide/041.png)</td>
<td>Turn on scale tool, then click in upper left part of image.</td>
</tr>
<tr class="even">
<td>Scale image to fit viewport</td>
<td>![](vistarad-quick-start-guide/042.png)</td>
<td>Turn on scale tool, then click in upper middle part of image.</td>
</tr>
<tr class="odd">
<td>Scale image to specific size</td>
<td>![](vistarad-quick-start-guide/043.png)</td>
<td>Turn on scale tool, then click in upper right part of image. Choose a scale option from the menu that displays.</td>
</tr>
<tr class="even">
<td>Sharpen</td>
<td>![](vistarad-quick-start-guide/044.png)</td>
<td>Drag up or left to sharpen;<br />
drag down or right to smooth.</td>
</tr>
<tr class="odd">
<td>Invert</td>
<td>![](vistarad-quick-start-guide/045.png)</td>
<td>Click to invert.</td>
</tr>
<tr class="even">
<td>Flip</td>
<td>![](vistarad-quick-start-guide/046.png) or ![](vistarad-quick-start-guide/047.png)</td>
<td>Click on top part of image to flip vertically; click on bottom to flip horizontally.</td>
</tr>
<tr class="odd">
<td>Rotate</td>
<td>![](vistarad-quick-start-guide/048.png) or ![](vistarad-quick-start-guide/049.png)</td>
<td>Click on left side of image to rotate 90° counterclockwise; click on right side to rotate 90° clockwise.</td>
</tr>
</tbody>
</table>

The tool remains active until disabled. You can change other images, select a different tool, or disable the tool by right-clicking once.

### Using Arrow Keys for Precise Control 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you need to make precise window/level, scale, or sharpen adjustments, you can use the arrow keys.

In the VistARad Settings dialog (View \| Settings), go to the Mouse/Shortcut tab and make sure the Enable arrow keys for image adjustments check box is checked.

Turn on the window/level, scale, or sharpen tool (assign this tool to the left mouse button as described in the previous section).

Drag the mouse to make initial rough adjustments (this step can be skipped for the Sharpen tool).

Use the arrow keys as follows to make precision adjustments:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Shortcut</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>→ or ↑</td>
<td>Increase window/level, scale, or sharpness (coarse)</td>
</tr>
<tr class="even">
<td>CTRL + →<br />
or CTRL + ↑</td>
<td>Increase window/level or scale (fine)</td>
</tr>
<tr class="odd">
<td>← or ↓</td>
<td>Decrease window/level, scale, or sharpness (coarse)</td>
</tr>
<tr class="even">
<td>CTRL + ←<br />
or CTRL + ↓</td>
<td>Decrease window/level or scale (fine)</td>
</tr>
</tbody>
</table>

Tip For a complete list of keyboard shortcuts and shortcut-related options, see the VistARad Help menu.

‘Apply To’ Settings

Usually changes to window/level, scale, etc., affect all images in a viewport. You can change this behavior and make changes affect only the selected image.

Click the tool for the property you want to change Apply To settings for:

![](vistarad-quick-start-guide/050.png) Window/level ![](vistarad-quick-start-guide/051.png) Scale (zoom)

![](vistarad-quick-start-guide/052.png) Sharpen ![](vistarad-quick-start-guide/053.png) Invert

![](vistarad-quick-start-guide/054.png) Flip 180° ![](vistarad-quick-start-guide/055.png) Rotate 90°

In the viewport containing the image you want to change, click the Apply To icon.

When the Apply To icon looks like ![](vistarad-quick-start-guide/056.png), your change is applied only to the selected image.

When the Apply To icon looks like ![](vistarad-quick-start-guide/057.png), your change is applied to all the images in the viewport.

You can set the default ‘Apply To’ behavior using the options under   
View \| Settings \| Viewport. (Note that Apply To settings defined in a hanging protocol overrides the settings in this tab.)

## Changing Layout in a Viewport 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a viewport, images can be arranged 1-up (stacked) or in multiple rows and columns (tiled). In the Viewer and Browser windows only, you can change viewport layout as follows:

![](vistarad-quick-start-guide/058.png)

### Using Full-Screen View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Viewer window only, you can double-click an image to expand it to fit the size of the current monitor. While full-screen view is active, you can change the current image (window/level, flip/rotate, etc.), scroll to other images, or use the cine feature.

If viewport navigation shortcut keys are enabled, you can also press \<F\> to turn full-screen view on or off. See page [16](#using-arrow-keys-for-precise-control) for steps to enable shortcut keys.

## Changing Layout in a Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Browser, Scrapbook, and Scout windows, you can change window layout as follows:

Click ![](vistarad-quick-start-guide/059.png) and drag down using the mouse.

In the box that displays, move the mouse to highlight the rows and columns you want to set the layout to.

When the desired number of rows and columns are highlighted, click the left mouse button.

Tip Click ![](vistarad-quick-start-guide/060.png) to switch back and forth between 1-up and the last selected layout.

Note In the Viewer window, the arrangement of viewports is dictated by the current hanging protocol and template.

## Manipulating Image Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An image set (the active group of images in a viewport) can be moved, or cloned. You can also clear a viewport without closing the associated exam.

### Moving an Image Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Viewer window, you can move any image set to a different viewport by dragging the title bar of one viewport into a different viewport.

If the target viewport in the Viewer is empty, the images being moved are shifted to the target viewport.

If the target viewport in the Viewer contains a single image set, your user settings determine if the contents of the two viewports are swapped, or if the images being moved replace the images in the target viewport. [^2]

If the target viewport in the Viewer contains multiple image sets, you cannot move more images into that viewport.

In the Browser window, you can move image sets from one viewport to another by dragging the title bar of the viewport you want to move.

If the target viewport in the Browser is empty, the image being dragged is moved to the last position in the Browser window (where images wrap from left to right, then top to bottom).

If the target viewport in the Browser is occupied, the image being dragged is inserted into the target cell and the pre-existing image set is shifted to the left.

### Cloning an Image Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Viewer window only, you can copy the images in one viewport into another (empty) viewport. The resulting ‘clone’ can be manipulated independently of the source images.

Point to the title bar at the top of the image set you want to clone.

Using the right mouse button, drag the images to an empty viewport. A popup menu displays when you complete the drag.

Click the Clone option from the menu that displays.

### Removing an Image Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove images from a viewport, click ![](vistarad-quick-start-guide/061.png) in the upper right corner of the viewport. Note that even when all viewports are emptied using this method, the exam is still considered open by VistARad.

Images can be re-loaded into viewports using the Preview window.

## Mensurated Scale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an image is displayed, a mensurated scale can be displayed to the left of the image in the viewport. This scale signifies the length dimensions of the image. The scale uses pixel size data in the image header. If there is no pixel size data available for the image, you can use the Calibrate tool in VistARad to establish a pixel size. For details, see “Using the Calibrate Tool” in the *VistARad User Guide*.

![](vistarad-quick-start-guide/062.png)

To display the mensurated scale:

1.  With an image in the viewport, right-click to display the Context menu.
2.  Click the Mensurated scale option from the menu. The scale will display to the left of the image.

To remove the mensurated scale from view:

1.  Right-click the image to display the Image Context menu,
2.  Click the Mensurated scale option, and the scale will no longer be visible.

## Annotations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can add annotations to images displayed in the Viewer, Browser, or Scrapbook windows. The Line Measurement tool is accessed through its own dedicated button ( ![](vistarad-quick-start-guide/063.png)). For the four other annotation-related buttons, the appearance of each icon varies, displaying whichever tool you have used most recently.

![](vistarad-quick-start-guide/064.png)

### Annotating Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display the image you want to annotate.

In the Viewer toolbar, click the pulldown arrow to the right of the Drawing tool. Depending on which feature you used last, the icon displays as Text, Line, Arrow, Rectangle, Ellipse, Free Hand, or Auto Number.

> ![](vistarad-quick-start-guide/065.png)

Annotate the image. Steps for each tool are noted below:

| Tool    | Steps                                                                                                                                                                                      | Pointer                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Text        | Drag to create the text box, then enter the text.                                                                                                                                              | ![](vistarad-quick-start-guide/066.png)  |
| Line        | Click, then drag. Complete the drag when the line is the desired length.                                                                                                                       | ![](vistarad-quick-start-guide/067.png)        |
| Arrow       | Click where you want the head of the arrow to display, then drag and adjust as needed.                                                                                                         | ![](vistarad-quick-start-guide/068.png)       |
| Rectangle   | Click, then drag. Complete the drag when the shape is the desired size.                                                                                                                        | ![](vistarad-quick-start-guide/069.png)   |
| Ellipse     | Click, then drag. Complete the drag when the shape is the desired size, and use the drag handles to adjust.                                                                                    | ![](vistarad-quick-start-guide/070.png)     |
| Free Hand   | Click three or more spots around the desired area, then use the drag handles to adjust as needed.                                                                                              | ![](vistarad-quick-start-guide/071.png)   |
| Auto Number | In the Auto Number dialog that displays, click the buttons that correspond to the numbering style and starting point you want to use. Then click each point where you want a number to appear. | ![](vistarad-quick-start-guide/072.png) |

The tool remains active until it is disabled. You can add additional annotations, select a different tool, or right-click once to disable the tool.

### Measuring Image Features: Ruler and Angles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To measure length:

1.  Display the image that contains the feature you want to measure.
2.  In the Viewer toolbar, click the Length measurement ![](vistarad-quick-start-guide/073.png) tool.
3.  Measure the image feature.

Right-click once to disable the tool. To measure an angle:

1.  Click the pulldown arrow to the right of the Angle measurement tool. Depending on which feature you used last, the icon displays as either an angle or a Cobb angle.

![](vistarad-quick-start-guide/074.png)

2.  Measure the image feature. Steps for each tool are noted below:

| Measure | Pointer                                                                                                                                               | Point to image, then...                                                                                                                                                          |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length      | ![](vistarad-quick-start-guide/075.png)                                  | Click to set the start point of the line, drag the mouse, and release the mouse button when the line is the desired length.                                                          |
| Angle       | ![](vistarad-quick-start-guide/076.png)                                  | Starting at the vertex, drag the mouse to draw the first line of the angle. The second line is attached to it. Drag either or both lines by their handles to adjust their positions. |
| Cobb Angle  | ![](vistarad-quick-start-guide/077.png) | Starting with the top-most line to be drawn, drag the mouse to create the line. Re-position the lines as needed by dragging the handles.                                             |

3.  The tool remains active until disabled. You can add additional measurements, select a different tool, or right-click once to disable the tool.

### Measuring Image Features: Hounsfield Areas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Display the image that contains the feature you want to measure.
2.  In the Viewer toolbar, click the pulldown arrow to the right of the Hounsfield tool ![](vistarad-quick-start-guide/078.png). Depending on which of its two features you have used most recently: the icon displays as Rectangle or Free Hand.

![](vistarad-quick-start-guide/079.png)

3.  Measure the image feature. Steps for each tool are noted below:

| Measure | Pointer                                                                                                                                   | Point to image, then...                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Rectangle   | ![](vistarad-quick-start-guide/080.png) | Click to set the start point of the rectangle, drag the mouse, and release the mouse button when the rectangle covers the desired area. |
| Free Hand   | ![](vistarad-quick-start-guide/081.png) | Click three or more spots around the desired area, then use the drag handles to adjust as needed                                        |

4.  The tool remains active until disabled. You can add additional annotations, select a different tool, or right-click once to disable the tool.

### Working with Annotations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change the shape of an annotation, right-click the annotation, choose Edit Annotation from the context menu, then drag the handles as desired.

To hide an annotation, click the arrow on the left of ![](vistarad-quick-start-guide/082.png) on the toolbar, and choose whether you want just the annotations you have made in that session to display, annotations that have been made in previous sessions, or both.

![](vistarad-quick-start-guide/083.png)

To delete an annotation, right-click it and choose Delete Annotation.

### Overriding Saved Notations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have the MAGJ OVERRIDE ANNOTATIONS security key, you can delete annotations in completed exams, as follows:

1.  Right-click the completed exam of interest in the Manager window, and choose Override Annotations.
2.  Make any desired additions or other changes to the annotations.
3.  Click ![](vistarad-quick-start-guide/084.png) in the Viewer toolbar.
4.  Click Store Annotations in Close Exams/Update Status.

# Key Images 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A *key image* is an image that a radiologist has marked as being pertinent to the interpretation of an exam. A key image includes any annotations and display settings (such as window/level) made to the image by the interpreting radiologist.

If an open exam contains key images, they are automatically loaded into the Scrapbook window. If the Scrapbook is not visible, it can be shown by clicking ![](vistarad-quick-start-guide/085.png) in the toolbar near the top of the screen.

### Marking Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Marking an image creates an independent copy of the image in the Scrapbook window.

Open an exam. If you want marked images to be saved as key images, you must have the exam locked in your name.

Display the image to be marked.

Click the ![](vistarad-quick-start-guide/086.png) icon.

Continue marking images, or, if you want to work with the image immediately, click ![](vistarad-quick-start-guide/087.png) to display the Scrapbook window.

### Working with Key Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can manipulate and annotate mages in the Scrapbook window.

If the exam in question is locked, changes to images in the Scrapbook are saved when the exam is closed, and when the status of the exam is updated, images in the Scrapbook become key images.

If the exam is not locked, changes to the contents Scrapbook are discarded when the exam is closed.

### Unmarking Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To unmark an image and remove it from the Scrapbook, locate the marked image in the Scrapbook and click ![](vistarad-quick-start-guide/088.png), or locate the marked image in the Viewer and click ![](vistarad-quick-start-guide/089.png).

If the exam in question is locked in your name, the key image is also permanently deleted (the source image is not affected).

If the exam is not locked, the key image is retained and displays in the Scrapbook the next time the exam is opened.

# Reviewing Online Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc117391487" class="anchor"></span>VistARad is typically configured to open requisitions automatically when an exam is opened. You can open other records such as reports or health summaries as well.

### Displaying Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To display a requisition or report for an open exam, click ![](vistarad-quick-start-guide/090.png) in an occupied viewport. The requisition displays if the exam is unread. The report displays if the exam has been completed. You can also click, then drag down on the ![](vistarad-quick-start-guide/091.png) icon to select either the requisition or the report.

To display a record in the Manager, select an exam. Then right-click the exam and choose an option, or click one of the report-related buttons located under the exam lists in the Manager window.

### Working with Health Summaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Summary button is used to access health summary reports.

- If the button includes an asterisk: ![](vistarad-quick-start-guide/092.png), clicking the button will open the report you have designated as the default health summary report. Clicking the arrow on the right side of the button will open the Health Summary window.
- If the button looks like this: ![](vistarad-quick-start-guide/093.png), there is no default health summary defined, and clicking the button will open the Health Summary window.

The Health Summary window lists any health summary reports that have been selected as preferred reports by the current user.

- To display one of these reports, select the name of the report and click View Heath Summaries.
- To view a list of all available health summary reports, click Show Preferences.
- To edit the user-specific list of preferred reports, click Show Preferences, then use the Add and Remove buttons.
- To select a default report, click Show Preferences, select a report, then click Set Default. Click the Health Summary button in the Manager to immediately open that report.<span id="_Ref103862839" class="anchor"></span>

# Closing Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If VistARad has been integrated with a voice dictation system, and if you have a report open in that system, save or sign the report.

In VistARad, do one of the following to open the Close Exams / Update Status dialog:

- Press \<CTRL+Q\>.
- Click the ![](vistarad-quick-start-guide/094.png) button in the Viewer, Browser, or Scrapbook window.
- Click Close Exams in the Manager window.

  If the exam being closed is locked, and if that exam contains images that have not been viewed,[^3] a warning message displays.
- Click Continue to close the exam without displaying all images.
- Click Cancel Exam Close to go back to reviewing images.

  For each exam listed in the dialog, note the values in the Close?, Interpret?, and Annotations columns. Click the values to determine the following:

  Whether the exam is to be closed.

  Whether the Interpreted status of the exam has changed (values of N/A cannot be changed).

  Whether and how annotations, if any, are saved.

![](vistarad-quick-start-guide/095.png)

Click OK.

- When an exam is closed, all images are removed from all windows in VistARad.
- If Interpret? was set to YES for a listed exam, that exam’s status is updated to indicate that it has been read.

# Hanging Protocols & Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of hanging protocols and templates, and the settings that affect how they are applied.

## Template & Hanging Protocol Basics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A template is a specific arrangement of viewports in the VistARad Viewer window. Templates are selected automatically when a hanging protocol is applied to an exam being opened. For more information about using templates, refer to the *VistARad User Guide*.

A hanging protocol automates tasks related to displaying exams. When a hanging protocol is applied, it can:

- Locate priors.
- Load images from current and prior exams into viewports.
- Apply pre-defined image display settings in each viewport.

Hanging protocols are typically selected automatically when an exam is opened. Hanging protocols are matched to exams based on CPT code (procedure), modality type, or both.

You can select a hanging protocol manually before opening an exam. For details, see page [6](#opening-an-exam-ii).

You can also re-display a loaded exam using a different hanging protocol.

### Basic Hanging Protocol Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The settings under View \| Settings \| Hanging Protocol govern general hanging protocol behaviors. You can:

- Allow or prevent automatic display of priors and related exams for unread exams. There is a similar setting for completed exams.
- Have VistARad notify you if there is a more recent unread exam for a patient than the one you select for display. What qualifies as a more recent unread exam can be based on exact or similar CPT (procedure) matching.

### Handling Multiple Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If more than one hanging protocol is found for an exam being opened, a dialog listing each of the matching hanging protocols is displayed.

![](vistarad-quick-start-guide/096.png)

You can choose one of the listed hanging protocols, or you can use default processing (see below).

You can also use one of the Save... check boxes in the dialog to make the selected hanging protocol the only hanging protocol used for the current type of exam or modality. (This prevents the multiple match from happening in the future.)

Default Processing

Default processing is used if there are no matching hanging protocols for an exam being opened, or if you explicitly select the Default Processing option in the Multiple Hanging Protocol Match dialog.

When default processing is used for an exam:

- Images are loaded in the Preview window and a viewport arrangement (template) is selected in the Viewer.
- No images are loaded into viewports. You can use the Preview window to manually load images into viewports. For details, see page [8](#working-with-routed-exams).

For details about hanging protocol selection logic and hanging protocols in general, refer to the *VistARad User Guide*.

# VistARad and Voxar 3D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Voxar 3D Workstation is a third-party application used to display volumetric images. Voxar and VistARad can be installed and used on the same workstation. When both applications are properly configured, part or all of an exam in VistARad can be opened in Voxar in a single step.

Note It is assumed that the VistARad/Voxar interface has been properly configured, and that the proper version of Voxar is present on the VistARad workstation. For details about configuration, refer to Chapter 3 in the *VistA Imaging System Installation Guide*.

With the proper configuration and security keys, users can also save an image capture from Voxar to the VistA system).

## Loading Images from VistARad into Voxar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistARad, open an exam and display the images of interest.

Right-click the images you want to load into Voxar, and:

- Choose View 3D to load the image set into Voxar.
- Choose View 3D all series to load the exam into Voxar.

  The Voxar software starts automatically and the images load into the Voxar Reading Manager window.

  Manipulate the images as desired in Voxar.

Tip Depending on which security keys you have, you might be able to export, print, or copy images from the Voxar application.

Note The Finish and Archive button appears to be enabled even when it is not functional. This button functions only if the ability to save images to VistA has been configured.

When you have finished, click Discard and Finish in the Voxar Reading Manager.

## Saving a Voxar Capture to VistA as a New Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note This feature is available only if both VistARad and the DICOM Gateway are properly configured.

Note This feature is enabled only for users who hold the MAGJ STORE 3D IMAGES security key.

Before using the following steps, contact your Imaging Coordinator to verify that this feature is available.

Load images into Voxar from VistARad, and generate the views you want to save.

When you have created the desired view in Voxar, click Capture (located in the lower right corner), then click the view to be captured.

In the Voxar Reading Manager window, click the Report tab. Then click the thumbnail representing the image you want to save.

Click Finish and Archive. The Voxar windows closes.

Close and reopen the exam in VistARad. The new image is now available as a separate series.

After the captured image has been processed by the DICOM Gateway, it is added to the exam as a single-image series. To view the new series, close and re-open the applicable exam in VistARad.

# Teaching Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad provides the ability to create teaching files from images, images sets, and exams. Once uploaded to the Medical Imaging Resource Center (MIRC) server, these files become searchable and available as teaching references for MIRC users.

NOTE   It is imperative that images posted to MIRC servers contain no personally identifiable information (PII). Ensuring that images contain no PII is the user’s responsibility. VistARad will have already removed any PII from text data. However, burned-in pixel data cannot be removed. Therefore, the user must ensure that there is no PII in the burned-in pixel data of any image uploaded to the MIRC.

NOTE   Annotations added to images in VistARad cannot be uploaded to a MIRC; only the images themselves can be uploaded.

NOTE    For information about enabling the MIRC interface, see Chapter 3 in the *VistA Imaging System Installation Guide*, or contact your Imaging Coordinator.

## Creating Teaching Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open the image, image set or exam in the VistARad Viewer that you wish to make into a teaching file.

Right-click the image on the screen to bring up the context menu, then click Add to Teaching Files.

Select Image, Image Set, or Exam. This copies the image to the Teaching Files section of the Scrapbook window.

Repeat the process for any additional images you wish to use; for best results, you should work only with images that are part of the same exam.

## Redact Sensitive Information from a Teaching File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When teaching files are uploaded using VistARad, VistARad automatically removes personally identifiable information from the image header. As the responsible party creating the teaching file, you need to ensure that images you upload do not contain any personally identifiable information. VistARad now offers the capability to “erase” such information contained in the image itself. This process is called *redacting*.

1.  Select the image to be edited and drag it into a viewport. Right-click on the image, and then select Add to Teaching Files \| Image from the drop-down menu:

![](vistarad-quick-start-guide/097.png)

2.  Click ![](vistarad-quick-start-guide/098.png) in the toolbar to display the Scrapbook window, and click the Teaching Files tab.
3.  Click ![](vistarad-quick-start-guide/099.png) in the Teaching Files toolbar.
4.  A warning will display not to upload any files with “burned-in” personally identifiable information. Click Continue.
5.  The Teaching Files window will display. Select the Title box, and enter the name to be used for the teaching file.
6.  Click the drop-down menu under Category and click the desired category.
7.  Double-click the appropriate descriptive terms in the Findings, and Anatomic Location boxes on the right, and those choices will populate the corresponding boxes on the left.
8.  Enter any desired free text into the boxes for Diagnosis and Abstract. You can either type or use Copy/Paste to enter text here.
9.  Click Send, or Send and Close, and the images will be sent to the teaching folder of your facility on the MIRC server.
10. Once you have finished, click ![](vistarad-quick-start-guide/100.png) in the Teaching Files toolbar to open the MIRC server Query Page in your browser.

# Context Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Context Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Context Management (CM) allows users to choose a subject once in one application, and have all applications containing information on that same subject “tune” to the data they contain. This eliminates the need for the user to redundantly select the subject in the varying applications. In the healthcare industry, for example, multiple applications operating “in context” through use of a context manager would allow a user to select a patient (*that is,* the subject) in one application.

## The Clinical Context Object Workgroup Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCOW is a Health Level 7 (HL7) standard protocol designed to enable dissimilar healthcare software applications to synchronize in real-time, and at the user-interface level. It is vendor-independent and allows applications to present information at the desktop and/or portal level in a unified way. CCOW is the primary standard protocol used in healthcare to facilitate the Context Management process.

When CCOW is available, the VistARad client uses CCOW to synchronize patient and user context management with the Computerized Patient Record System (CPRS) and other CCOW-enabled applications. A new Settings tab, Context Management, is used to enable context management.

## The Context Management Settings Tab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Context Management settings tab , allows the user to manage how CM operates on the individual workstation. The user must check the Enable Context Management in order to use CM capability.

## Context Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A context indicator (icon) appears at the top of the various VistARad windows to the left of the Patient Name and demographics. A context menu item appears on the Manager and Viewer menu bars for options to Suspend/Resume context, etc. The application also automatically changes the displayed icon to reflect the change in context.

| Icon                                                                                                                          | Title    | Meaning                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistarad-quick-start-guide/101.png)   | Changing | Displayed when the Clinical Link is changing. This icon may appear so briefly that the user may not see it. It is displayed when the common (linked) patient is changing. For example, if VistARad is linked with CPRS and CPRS changes from one patient to another, this icon will display during the change process. |
|                                                                                                                                   |              | Patient Context is Changing                                                                                                                                                                                                                                                                                            |
| ![](vistarad-quick-start-guide/102.png) | Broken   | Displayed when an application is not linked or the application is “out of patient context.” For example, if CPRS is linked and displaying one patient and VistARad is displaying a different patient, then VistARad is said to be “out of patient context” and will display this icon.                                 |
|                                                                                                                                   |              | Patient Context is Broken                                                                                                                                                                                                                                                                                              |
| ![](vistarad-quick-start-guide/103.png) | Linked   | Displayed when an application is utilizing CCOW to maintain patient context with the CCOW server. For example, if VistARad is open and displaying the same patient (as defined by the CCOW server) for all linked applications, then VistARad will display this icon.                                                  |
|                                                                                                                                   |              | Patient Context is Joined                                                                                                                                                                                                                                                                                              |

# VistARad and Voice Dictation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About the VistARad Dictation Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistARad dictation interface allows communication with approved voice dictation systems, installed on the same workstation as VistARad, or on a separate workstation. Consult the Imaging Team for a list of approved voice dictation software products.

If the dictation interface is enabled and properly set up, opening and locking an exam for interpretation in VistARad trigger the opening of the exam’s report in the dictation software. You can begin dictating a report without having to manually select it ahead of time.

| ![](vistarad-quick-start-guide/104.png) | When the VistARad dictation interface is being used, it is the user’s responsibility to verify that the proper login is being used to access reports, that the report opened for dictation is the appropriate report, and that report is handled appropriately once dictation is complete. |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

For information on setting up the VistARad dictation interface, see chapter 3 in the *VistA Imaging System Installation Guide*.

## Opening Exams and Reports for Dictation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Before you Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log in to your voice dictation software (this can either be on the same workstation as VistARad, or on a separate workstation).

Log in to VistARad.

If you start the dictation software after logging in to VistARad, you need to start the dictation interface manually. To do this, click Dictation \| Establish Dictation Connection in the Manager main menu.

### Opening an Exam and Report for Dictation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the dictation interface is active, use the Manager to open an unread exam or to start ReadList.

Note If another report is already open, be sure to save or sign that report before opening additional exams for interpretation.

As the exam is being opened, the Dictation dialog displays. In the Dictate? column, click the YES/NO value to set it as desired.

- Choose YES if you want VistARad to send the case ID to the dictation software (which in turn triggers the display of the associated report).
- Choose NO if you want to open the exam without opening the associated report.

| Warning: | Do not set Dictate? to YES for multiple exams unless your Imaging Coordinator has verified that your dictation software can handle multiple case IDs. |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Note:    | Some interactions work differently when multiple locked exams are open concurrently. See the Multiple Locked Exams section below.                     |

Click OK. The dictation software opens the report for the exam.

Note When you go to close an exam that is locked and has a report open for dictation, the value for Interpret? in the Close Exams/Update Status dialog defaults to YES. This is based on a user preference in the Manager \| General tab in the VistARad settings dialog (View \| Settings).

## Multiple Locked Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User interactions with the application will differ when multiple locked exams are open concurrently.

### When Multiple Locked Exams for Different Patients are open

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the user simultaneously opens multiple exams for different patients, the dictation dialog is suppressed and will not be displayed. The following message box will be displayed if the user has previously checked the Dictation dialog option Do not show this window again:

![](vistarad-quick-start-guide/105.png)

2.  To initiate a dictation for any of these exams the user must right-click on the exam of interest from the Manager’s Open/Reserved Exams listing, and then select the Dictate option from the context menu drop-down.
3.  For any exam listed in the Open/Reserved Exams, the “Dictate” menu option for that same exam—if selected from the main list window (Patient and Unread exams display)—is now grayed out. That is, the “Dictate” context menu option can only be initiated from the exam’s entry in the Open/Reserved Exams list. The “Dictate” context menu option for any exam in the “Reserved” state is grayed out.

### Dictation Dialog forced under certain conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dictation dialog is now forced on screen if:

1.  The user opens an exam with a Lock while another Locked exam is already open (same or different patient).
2.  The user selects the Dictate context menu option on the main exam list (Unread or Patient) for an exam while another Locked exam is already open (same or different patient).

### Opening a Report (only) for Dictation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To open a report in your dictation software via VistARad’s dictation interface, right-click any exam in an exam list, then click Dictate. Note that:

- This neither opens nor locks the exam. To open the exam itself, select it and click Open.
- You are not asked to confirm the operation (the Dictation dialog does not display).
- This can be used for any exam, regardless of the status of the exam.

# Remote Data/Image Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use VistARad to view images and reports for radiology exams stored at any remote VA site. You can also view exams stored at DoD medical facilities for VA/DoD shared patients.

When the Patient Exams list is displayed in VistARad, remote sites where the patient has been treated are shown as buttons at the top of the list. Clicking one of the buttons adds exams (if any) from the named site onto the Patient Exams list, and re-sorts the list to show all exams in chronological order.

![](vistarad-quick-start-guide/106.png)

Remote exams shown in the Patient Exams list can be opened for image review, and reports and requisitions can also be displayed. (Note that for DoD exams, images and reports are accessible, but requisitions are not.) The site-local VIX handles retrieval and caching automatically.

When a patient might have remote exams available, based on information from the Master Patient Index, VistARad displays the names of the relevant remote sites on buttons within the Patient Exams tab. Initially, data from the remote sites is not retrieved. To retrieve the data:

1.  Click the button for the site. This will accomplish the following:
- Initiates a connection to the remote site. If the site is unavailable, the name in its button will be displayed with a strikeout line through it.

> ![](vistarad-quick-start-guide/107.png)

- Loads any available studies into the exam list.
- Updates the label of the button with the number of exams at that site, displayed to the right of its name in square brackets \[3\].
2.  Click “Connect All” to automate the steps above for all available sites. The exam list will refresh as the exam list data from each site becomes available.
3.  Once the data from all remote sites has finished loading, you can begin working with the consolidated exam list.

Remote exams listed in the Manager are available for all VistARad operations available to the current user.

Note DOD studies are consolidated under a single DOD tab, and can be distinguished by a Day/Case column entry starting with “DOD-”:

![](vistarad-quick-start-guide/108.png)

[^1]: E = examined, I = interpreted, C = complete.

[^2]: To set “swap” or “replace” as the default behavior, choose View \| Settings \| Viewport and change the settings in the Drag and Drop Options area.

[^3]: An image set is considered “viewed” if it has been loaded into a viewport and has been “on top” (non-hidden) at some point in the current exam display session.