---
title: MAG*3*48 Diagram Annotation Tool User and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: Diagram Annotation Tool User and
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: MAG
patch_ver: 3
patch_id: MAG*3*48
group_key: "MAG:MAG:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - diagram
  - annotation
  - tool
  - table
  - contents
  - setup
  - class
  - guide
  - strong
  - diagrams
page_count: 0
word_count: 3775
section_count: 16
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag3_0_diag_annot_ug_f.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag3_0_diag_annot_ug_f.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![Diagram Annotation Tool User & Setup Guide](mag-3-48-diagram-annotation-tool-user-and-setup-guide/001.png)

*Diagram Annotation Tool User & Setup Guide*

> V*IST*A Imaging Version 3.0, Patch 48

> February 2005

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/002.png)

> V*IST*A Imaging Software Design & Development Veterans Health Administration Department of Veterans Affairs

> Diagram Annotation Tool User & Setup Guide MAG\*3.0\*48

> February 2005

> Property of the US Government

> No permission to copy or redistribute the software described in this document is given. Use of unreleased versions of this software requires the user to execute a written test agreement with the VistA Imaging Development Office.

> This is a controlled document. No changes to this document may be made without the express written consent of VistA Imaging Development Office.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Software Design & Development <span class="mark">REDACTED</span>

<span class="mark">  
</span>

> <u>Table of Contents</u>

> Revision Table

| Rev | Date    | Notes                                                                                      |
|---------|-------------|------------------------------------------------------------------------------------------------|
| 1.0     | Sep 23 2004 | Initial version, verified against t50.                                                         |
| 1.01    | Nov 18 2004 | Fixed missing numbers & bullets.                                                               |
| 1.1     | Feb 02 2005 | Updates for SOP 192-352 compliance. Typo corrections in Diagram Annotation Tool Setup chapter. |

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [Getting Help](#getting-help)
  - [About this Manual](#about-this-manual)
- [Overview](#overview)
  - [What is the Diagram Annotation Tool?](#what-is-the-diagram-annotation-tool)
  - [How the Diagram Annotation Tool Works](#how-the-diagram-annotation-tool-works)
  - [Diagram Annotation Summary Steps](#diagram-annotation-summary-steps)
- [Using the Diagram Annotation tool](#using-the-diagram-annotation-tool)
  - [Selecting a Diagram Template](#selecting-a-diagram-template)
  - [Annotating Diagrams](#annotating-diagrams)
  - [Diagram Annotation Detailed Steps](#diagram-annotation-detailed-steps)
- [Diagram Annotation Tool Setup](#diagram-annotation-tool-setup)
  - [Diagram Template Setup](#diagram-template-setup)
  - [VistA Imaging Configuration for Diagrams](#vista-imaging-configuration-for-diagrams)
  - [Establishing Diagram-specific Progress Note Titles](#establishing-diagram-specific-progress-note-titles)
  - [Setting up the COM Object Definition](#setting-up-the-com-object-definition)
    - [{9B6B82F4-14DF-493B-B7FE-2EF349F19167}](#9b6b82f4-14df-493b-b7fe-2ef349f19167)
  - [Linking Progress Notes with the Diagrams in CPRS](#linking-progress-notes-with-the-diagrams-in-cprs)
  - [Diagram Annotation Testing](#diagram-annotation-testing)
> This document explains how to use the Diagram Annotation tool, an optional component in the VistA Imaging system.
> For users, this document assumes a basic understanding of the Windows environment, CPRS Chart, and Clinical Display.
> For administrators, this document assumes an understanding CPRS configuration, TIU progress note setup, and VistA Imaging setup and configuration.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In compliance with FDA and VA policies, authorization to use the software described in this document is contingent on the execution of a Site Agreement between the V*IST*A Imaging HSD&D group and the site where this software is installed. The Diagram Annotation tool is a component of V*IST*A Imaging, and if a Site Agreement has already been filed, no modifications to the Site Agreement are needed.

> ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/003.png)![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/004.png)In addition to any restrictions noted in the Site Agreement, the following restrictions apply:

| No modifications may be made to this software without the express written consent of the V*IST*A Imaging National Project Manager.                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The Food and Drug Administration classifies this software as a medical device. Modifications to the computer where this software is installed, such as the installation of unapproved hardware or software, will adulterate the medical device. The use of an adulterated medical device violates US Federal Law (21CFR820). |

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

## About this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contents in Brief

- The [<u>Overview</u>](#overview) describes the Diagram Annotation tool and summarizes its use.
- [<u>Using the Diagram Annotation tool</u>](#using-the-diagram-annotation-tool) explains how to select, annotate, and verify diagrams.
- [<u>Diagram Annotation Tool Setup</u>](#diagram-annotation-tool-setup) explains Diagram Annotation tool configuration. This chapter is intended for use by the Imaging Coordinator or IRM staff.

> Conventions

> This manual uses the following conventions:

- Controls (buttons, boxes, etc.) in the user interface are indicated by initial capitalization. For example: *Click Print to open the Print dialog.*
- Notifications or controls that are identified by a phrase are enclosed in single quotation marks. For example: *Click the ‘Share this folder as’ option.*
- Instructions for using menus are condensed using the ‘\|’ symbol. For example: *Click File \| Save* means: *Click the File menu, then click the Save option*.
- Useful or supplementary information is indicated by a TIP.
- Important or required information is indicated by a NOTE.
- ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/005.png)Warnings (potential data loss or device misuse) are indicated by:

> Related Manuals

> PDF versions of all documents related to VistA Imaging are available at <span class="mark">REDACTED</span>

# Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter provides an overview of the Diagram Annotation tool. It covers the following topics:

- [<u>What is the Diagram Annotation Tool?</u>](#what-is-the-diagram-annotation-tool)
- [<u>How the Diagram Annotation Tool Works</u>](#how-the-diagram-annotation-tool-works)
- [<u>Diagram Annotation Summary Steps</u>](#diagram-annotation-summary-steps)

## What is the Diagram Annotation Tool?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Diagram Annotation tool is an optional Imaging component that is accessed from CPRS.[<sup>\*</sup>](#_bookmark5) The Diagram Annotation tool is used to annotate online diagram ‘templates’ and then save the results directly to a patient’s electronic medical record. Newly annotated diagrams are typically available for display in less than a minute.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/006.png)

> Using the Diagram Annotation tool can reduce or replace, where appropriate, the clinical use of paper-based diagrams. Instead, diagrams are created online, with all users drawing from a shared diagram collection. Using the Diagram Annotation tool also reduces the workload of Clinical Capture users and the costs associated with paper-based records storage and management.

- <span id="_bookmark5" class="anchor"></span>At sites where online diagram annotation is implemented, the Diagram Annotation tool is available on workstations with both CPRS (version 1.0.21 or later) and Clinical Display (version 3.0.8 or later).

## How the Diagram Annotation Tool Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Diagram Annotation tool is launched directly from CPRS when certain site-specified progress note titles are selected. After the Diagram Annotation tool has been started, the user chooses a diagram from a collection of diagram templates, annotates the diagram, and saves the results.

> When a user saves a marked up diagram, the diagram is saved to the ‘Out’ folder in the diagram repository, and an entry is placed into the Background Processor IMPORT queue. When the queue entry is processed, the diagram image is moved to the Imaging shares (RAID) and the image can be viewed using VistA Imaging Clinical Display.

> Images created by the Diagram Annotation tool are in TIF format (for black and white) or JPG format (for color). Most diagram images range in size from 5 to 500K.

## Diagram Annotation Summary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each of these steps are described in detail in the next chapter.

1.  Log into CPRS and select the patient that you want to create a diagram for.
2.  Select or create an encounter (if necessary), then open a new progress note.

> *Select a progress note title that is linked to your site’s online collection of diagram templates. Titles typically will start with or contain the word ‘DIAGRAM’.*

3.  Select the diagram template that you want to use.

> *Selecting a diagram template creates a copy of the diagram for your use. The original template remains unchanged.*

4.  Annotate the diagram as desired.

> *While the Diagram Annotation window is open, the CPRS window cannot be used. The CPRS window will be accessible once the Diagram Annotation window is closed.*

5.  Save the annotated diagram.

> *Saving the diagram adds the diagram as a new image to the patient’s record.*

6.  Verify the diagram using Clinical Display.

> *In most cases, a new diagram is available for display in less than a minute. Diagrams can be identified by the title of the associated progress note.*

7.  Complete the process in CPRS by signing the diagram’s associated progress note.

# Using the Diagram Annotation tool 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains all the steps involved in creating an annotated diagram. It covers:

- [<u>Selecting a Diagram Template</u>](#selecting-a-diagram-template)
- [<u>Annotating Diagrams</u>](#annotating-diagrams)
- [<u>Diagram Annotation Detailed Steps</u>](#diagram-annotation-detailed-steps)

## Selecting a Diagram Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A diagram template is the online equivalent of a paper-based diagram that has not yet been marked up. Selecting a diagram template creates a copy of the image for your use. The diagram template remains unchanged and is available for selection by other users.

> NOTE The CPRS window cannot be used while the Diagram Annotation window is open.

> To select a diagram template

1.  Log into CPRS and select the patient that you want to create a diagram for.
2.  Click the Notes tab, then click the New Note button.
3.  If you are prompted to do so, select an encounter provider or an encounter location.
4.  When the Progress Note Properties dialog displays:
    - Select a title that is linked to your site’s online diagram collection. Titles for diagrams are defined on a site-by-site basis.
    - Set the ‘Date/Time of Note’ and Author boxes as desired.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/007.png)

5.  Click OK. A dialog displaying a list of diagram templates will open.
6.  <span id="_bookmark12" class="anchor"></span>Select the diagram template that you want to use, then click Open.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/008.png)

> NOTE The ‘In’ folder may contain one or more subfolders. Depending on the progress note you selected, one of the subfolders may be already selected. You can navigate manually by double-clicking folders on the left side of the dialog.

7.  The diagram template you selected will be displayed in the Annotation window. For information about annotating the diagram, see the next section.

> NOTE If the wrong template was selected, you can cancel and exit the Diagram Annotation tool, or you can close and then open a new template. For more information, see page [<u>10</u>](#Opening,_Closing,_and_Canceling_Images).

## Annotating Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a diagram template is displayed in the annotation window, it is ready to be annotated.

> To annotate a diagram

1.  Use the zoom tools to adjust the image display size as needed. Zoom tools are described in detail on page [<u>6</u>](#Changing_Zoom).

> ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/009.png)Zoom Tools

2.  Use the drawing and text tools to add annotations to the displayed image.

> ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/010.png)Drawing & Text Tools

- Drawing and text tools are described in detail on page [<u>7</u>](#Using_Drawing_&_Text_Tools).
- Annotations can be moved, resized and deleted as described on page [<u>8</u>](#Moving,_Resizing,_&_Deleting_Annotations).
- Color, line weight, and other properties can be changed as described on page [<u>9</u>](#Changing_Annotation_Properties).
3.  Before you save the diagram, zoom out and make sure all your annotations appear as desired.
4.  ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/011.png)Click , or choose File \| Image Complete. There will be a brief delay after the Annotation window closes.
5.  When the ‘Your diagram is being sent to the VistA Imaging archive’ message is displayed, click OK. The completed diagram will be available for display after a brief delay.

> NOTE If the diagram creation fails, the message noted above will not be displayed, and you will receive an email describing why the process did not complete.

6.  Use VistA Imaging to verify diagram.

#### ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/012.png)A diagram must be verified before its associated progress note is signed.

7.  In CPRS, select the unsigned progress note that the diagram is associated with.
1.  Click Tools \| VistA Imaging Display.
2.  Use either the Abstracts window or the Image List window to locate the diagram.

> Diagrams can be identified by the title of the associated progress note.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/013.png)![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/014.png)

3.  Click (or double-click) the diagram to display it in the Full Resolution viewer.
4.  Verify that image quality is acceptable and that the associated information is correct. If there is a problem with the image, contact your Imaging Coordinator.
8.  After the diagram is verified, its associated progress note can be signed using CPRS.

## Diagram Annotation Detailed Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following section describes all the functions in the Diagram Annotation tool window.

- [<u>Changing Zoom</u>](#Changing_Zoom)
- [<u>Using Drawing & Text Tools</u>](#Using_Drawing_&_Text_Tools)
- [<u>Moving, Resizing, & Deleting Annotations</u>](#Moving,_Resizing,_&_Deleting_Annotations)
- [<u>Changing Annotation Properties</u>](#Changing_Annotation_Properties)
- [<u>Opening, Closing, and Canceling Images</u>](#Opening,_Closing,_and_Canceling_Images)

> <span id="Changing_Zoom" class="anchor"></span>Changing Zoom

> The following table explains how to change zoom settings using the toolbar. You can also use options in the View menu to change the zoom.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To …</strong></th>
<th><strong>Do this…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Zoom to 100%</td>
<td>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/015.png).</td>
</tr>
<tr class="even">
<td>Fit to window</td>
<td>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/016.png).</td>
</tr>
<tr class="odd">
<td>Fit height to window</td>
<td>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/017.png).</td>
</tr>
<tr class="even">
<td>Fit width to window</td>
<td>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/018.png).</td>
</tr>
<tr class="odd">
<td>Change zoom manually</td>
<td><p>Use the Zoom Level bar, located in the upper right corner of the window.</p>
<ul>
<li><p>For quick changes, use the mouse to drag the scroll box left or right.</p></li>
<li><p>To change the zoom by 10% increments, click to the left or right of the scroll box.</p></li>
<li><p>To change the zoom by 1% increments, click the scroll box, then use the arrow keys to move the slider left and right.</p></li>
</ul></td>
</tr>
</tbody>
</table>

> <span id="Using_Drawing_&_Text_Tools" class="anchor"></span>Using Drawing & Text Tools

> A variety of graphic elements such as lines, boxes and arrows can be used to ‘mark up’ a diagram. Drawing and text tools available in the Diagram Annotation toolbar are described below. You can also use options in the Annotations menu to select a drawing or text tool.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To draw…</strong></th>
<th><strong>Do this…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Straight lines</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/019.png).</p></li>
<li><p>Point to where you want the beginning of the line located, then drag the mouse to draw the line.</p></li>
<li><p>Release the left mouse button when the line is the desired length.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Freehand shapes &amp; lines</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/020.png).</p></li>
<li><p>Point to where you want the beginning of the freehand line located, then drag the mouse to draw the line.</p></li>
<li><p>Release the left mouse button when you are finished.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Arrows</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/021.png).</p></li>
<li><p>Point to where you want the beginning of the arrow located, then drag the mouse to draw the line.</p></li>
<li><p>Release the left mouse button when the line is the desired length. The ‘head’ of the arrow will automatically be added to the terminating point of the line.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Boxes</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/022.png) to draw a solid box, or click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/023.png) to draw a hollow box.</p></li>
<li><p>Point to where you want one of the corners of the box located.</p></li>
<li><p>Drag the mouse to draw a rectangular area. Release the left mouse button when the box is the desired size.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Plus or Minus symbols</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/024.png) to create a plus sign, or click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/025.png) to create a minus sign.</p></li>
<li><p>Click where you want to place the sign (there is no need to drag the mouse).</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Text boxes</td>
<td><ol type="1">
<li><p>Click ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/026.png).</p></li>
<li><p>Point to where you want the text box located.</p></li>
<li><p>Drag the mouse to draw a rectangular area. Release the left mouse button when the box is the desired size.</p></li>
<li><p>Type the text that you want to appear in the box.</p></li>
</ol></td>
</tr>
</tbody>
</table>

> <span id="Moving,_Resizing,_&_Deleting_Annotations" class="anchor"></span>Moving, Resizing, & Deleting Annotations

> Existing annotations can be moved, resized, or deleted.

> ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/027.png)NOTE Before using the steps below, turn off any active tools by clicking in the toolbar.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To …</strong></th>
<th><strong>Do this…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Move an annotation</td>
<td><ol type="1">
<li><p>Point to the annotation.</p></li>
<li><p>When the mouse pointer changes to ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/028.png), drag the annotation to a new location.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Resize an annotation</td>
<td><ol type="1">
<li><p>Point to one of the ‘handles’ on the edges and corners of the annotation.</p></li>
<li><p>When the mouse pointer changes to ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/029.png), drag to resize the annotation.</p></li>
</ol>
<p><strong>TIP</strong> Straight lines and rectangles can be easily resized. For other shapes, it is usually faster to delete and recreate them.</p></td>
</tr>
<tr class="odd">
<td>Delete an annotation</td>
<td><ol type="1">
<li><p>Click the annotation you want to delete.</p></li>
<li><p>Click Edit | Clear Selected Annotations.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Delete multiple annotations</td>
<td><ol type="1">
<li><p>Drag the mouse to define a rectangular area that contains the annotations you want to delete.</p></li>
<li><p>Click Edit | Clear Selected Annotations.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Delete all annotations</td>
<td><ol type="1">
<li><p>Click Edit | Clear All Annotations.</p></li>
<li><p>When the confirmation message displays, click Yes.</p></li>
</ol></td>
</tr>
</tbody>
</table>

> <span id="Changing_Annotation_Properties" class="anchor"></span>Changing Annotation Properties

> When a new diagram image is annotated, the annotations you add are based on the following default properties:

- Line weight: medium (5 pt)
- Opaque/Translucent: Opaque[<sup>\*</sup>](#_bookmark20)
- Line & fill color: blue
- Font: MS Sans Serif, 8pt regular, blue

> These properties can be changed as described below. When properties are changed, existing annotations are not affected, but any new annotations will use the new properties.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To …</strong></th>
<th><strong>Do this…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Change line weight</td>
<td><p>Click Line Weight, then click the option you want to use: Thin (2 pt)</p>
<blockquote>
<p>Medium (5 pt)</p>
<p>Thick (10pt)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Make annotations translucent or opaque</td>
<td><ol type="1">
<li><p>If you have not done so already, change the line or fill color to something other than black.</p></li>
<li><p>Click Options, then click Annotations Opaque or Annotations Translucent.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Change line color</td>
<td><ol type="1">
<li><p>Click Options | Line Color.</p></li>
<li><p>In the Color dialog, click one of the Color boxes, then click OK.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Change fill color (solid rectangles)</td>
<td><ol type="1">
<li><p>Click Options | Fill Color.</p></li>
<li><p>In the Color dialog, click one of the Color boxes, then click OK.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Change font color</td>
<td><ol type="1">
<li><p>Click Options | Text Color.</p></li>
<li><p>In the Color dialog, click one of the Color boxes, then click OK.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Change font type, style, or size</td>
<td><ol type="1">
<li><p>Click Options | Text Font.</p></li>
<li><p>Choose the font type you want to use.</p></li>
</ol>
<p><strong>TIP</strong> San-serif fonts (Arial) or monospace fonts (Courier New) are easier to read online.</p>
<ol start="3" type="1">
<li><p>In the Font Style box, choose a style. Avoid italics, which can be difficult to read online.</p></li>
<li><p>In Size box, choose a point size.</p></li>
<li><p>Click OK when you are finished.</p></li>
</ol></td>
</tr>
</tbody>
</table>

- <span id="_bookmark20" class="anchor"></span>An opaque annotation will ‘cover’ non-white areas (lines, text, etc.) in the image. A translucent annotation will create a ‘highlighter’ effect when it is superimposed over non-white areas.

> <span id="Opening,_Closing,_and_Canceling_Images" class="anchor"></span>Opening, Closing, and Canceling Images

> ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/030.png)Typically, a diagram template is opened as described on page [<u>3</u>](#selecting-a-diagram-template). The resulting image is then annotated and saved using or File \| Image Complete.

> If you open the wrong template, or if you want to discard the markups you have made, use the steps below.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>To …</strong></th>
<th><strong>Do this…</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Discard the existing diagram</td>
<td><ol type="1">
<li><p>Click File | Close Image.</p></li>
<li><p>If you have begun marking up the diagram, you will be prompted for confirmation. Click Yes.</p></li>
</ol>
<p><strong>NOTE</strong> The Diagram Annotation window will remain open. Select a new template using the following steps.</p></td>
</tr>
<tr class="even">
<td>Open an new diagram</td>
<td><ol type="1">
<li><p>Click File | Open.</p></li>
<li><p>If you have begun marking up the diagram, you will be prompted for confirmation. Click Yes.</p></li>
<li><p>Select a new diagram template from the dialog that displays.</p></li>
</ol>
<p><strong>NOTE</strong> Make sure the template you select is appropriate for the progress note the diagram will be attached to. If it is not, use the following steps.</p></td>
</tr>
<tr class="odd">
<td>Discard the diagram and exit.</td>
<td><ol type="1">
<li><p>Click File | Cancel Image.</p></li>
<li><p>If you have begun marking up the diagram, you will be prompted for confirmation. Click Yes.</p></li>
<li><p>IMPORTANT: In CPRS, delete the progress note that was created for the diagram (click Actions | Delete Progress Note).</p></li>
</ol></td>
</tr>
</tbody>
</table>

# Diagram Annotation Tool Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No separate installation is needed for the Diagram Annotation tool. It is present on any workstation where CPRS Chart and Clinical Imaging are installed. However, to enable the Diagram Annotation tool, configuration changes need to be made in CPRS Chart, the TIU package, and VistA Imaging.

> This chapter explains how to set up the Diagram Annotation tool. This chapter covers:

- [<u>Diagram Template Setup</u>](#diagram-template-setup)
- [<u>VistA Imaging Configuration for Diagrams</u>](#vista-imaging-configuration-for-diagrams)
- [<u>Establishing Diagram-specific Progress Note Titles</u>](#establishing-diagram-specific-progress-note-titles)
- [<u>Setting up the COM Object Definition</u>](#setting-up-the-com-object-definition)
- [<u>Linking Progress Notes with the Diagrams in CPRS</u>](#linking-progress-notes-with-the-diagrams-in-cprs)
- [<u>Diagram Annotation Testing</u>](#diagram-annotation-testing)

> The information in this chapter is intended for use by Imaging Coordinators and IRM staff. It is assumed that the person setting up the Diagram Annotation tool is familiar with CPRS Chart configuration, the TIU Package, VistA Imaging servers, and the Background Processor.

> Performing these changes will require coordination between Imaging and Clinical Coordinators.

## Diagram Template Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Creating Diagram Templates

> Each image created using the Diagram Annotation tool is based on a diagram template.

> A diagram template is a scanned image file stored in a location accessible by the Diagram Annotation tool.

> The creation of diagram templates involves deciding which paper-based diagrams will be used as diagram templates and then scanning them in (do not use VistA Imaging Capture to do this). The resulting image files:

- Must be in TIF (tagged image file) format and should be saved as a 1-bit (black and white) image.
- Should be scanned at 300dpi. Higher resolutions can be used if necessary (with a corresponding increase in files size).
- Should be given filenames meaningful to the users that will need to select the appropriate template.

> Creating a Diagram Repository

> The diagram repository is a storage location for diagram templates and annotated diagram images waiting for processing. Before you create the diagram repository, you will need to:

- Estimate needed space

> The repository will need enough space to store all diagram templates and to store completed images waiting for processing. Completed images typically range from 5 to 500K (depending on the number of colors used and the amount of annotation added). Images are usually processed and removed in less than a minute.

- Determine a storage location

> The diagram repository can be located on any Windows-based server that is a part of your site’s network *except* the server used for VistA Imaging file shares.

> To create the diagram repository

1.  Log in as an Administrator to the computer where you will be creating the destination folder, and start Windows Explorer (choose Start \| Run, then type Explorer).
2.  Navigate to where you want to create the diagram repository, and create a new folder named ‘Diagrams’.
3.  Assign the following share permissions to the new Diagrams folder (right click the folder, click Sharing, then click Permissions):

> Users group – Change Permissions

> b2/high2 – Full Control (this FOIA exem. b2/high2 is the user that signed into the Background Processor – if another account is used, that account will need Full Control )

> Everyone – \<remove\>

4.  Under the Diagrams folder, create a new folder named ‘In’.
5.  Assign the following *directory* permissions to the new In folder (right click the folder, click Sharing, then click the Security tab):

> Users group – Read access Administrators – Full Control Everyone – \<remove\>

6.  <span id="_bookmark25" class="anchor"></span>Copy your site’s diagram templates into the In folder. If desired, you can create subfolders to organize the templates.
7.  Under the Diagrams folder, create a new folder named ‘Out’. This folder is used to store annotated diagram images after they have been saved. They are removed after being processed by the Background processor.
8.  Assign the following *directory* permissions to the Out folder (right click the folder, click Sharing, then click the Security tab):

> Users group – Read access Administrators – Full Control

> b2/high2 – Full Control (this FOIA exem. b2/high2 is the user that signed into the Background Processor – if another account is used, that account will need Full Control )

> Everyone – \<remove\>

## VistA Imaging Configuration for Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In VistA Imaging, a Network Location must be defined for diagrams, and the Background Processor IMPORT queue must be activated to process diagram images.

> Defining a Diagram Network Location

> After defining the diagram repository as described in the previous section, you will need to create an entry for the diagram repository in the NETWORK LOCATION file (#2005.2). This can be done using the Background Processor or by using FileMan.

> To define a diagram network location using the Background Processor

1.  At the Background Processor workstation, pause queue processing functions by clicking Stop (in the upper right corner of the Background Processor window).
2.  Click Edit \| Network Location Manager.
3.  In the Network Location Manager box that appears, click New. Then click OK to close the ‘required fields’ message. The Network Cache Manager dialog will open.
4.  Locate the Cache IDs area. In the Share Name box, enter the name that will identify the diagram repository. In the Network Path box, enter the computer name and path to the Diagrams folder.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/031.png)

5.  In the same dialog, set the Storage Type to Diagram and make sure the Online Status box is checked.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/032.png)

6.  Check your values before clicking OK; Network Locations can be defined and changed but by design, they cannot be deleted.
7.  In the main window, resume queue processing functions by clicking Start.

> To define a diagram network location using FileMan

1.  Log into the VistA Hospital Information System and select the NETWORK LOCATION

> file (#2005.2) for editing.

2.  Select fields .01, 1, 5 and 6 for editing.
3.  Name the new network location ‘DIAGRAMS’.
4.  At the next prompt, enter the computer name and folder (share) name for the diagram repository.
5.  When prompted for a storage type, enter ‘DGM’.
6.  Enter ‘1’ for the operational status prompt.

> Activating the IMPORT Queue

> The IMPORT queue must be activated for diagram images to be moved from the ‘Out’ folder in the diagram repository to the Imaging shares (RAID).

> To activate the IMPORT queue

1.  At the Background Processor workstation, pause queue processing functions by clicking Stop (in the upper right corner of the Background Processor window).
2.  Click Edit \| BP Workstation Parameters. The ‘Background Processor WS Parameters’ dialog will open.
3.  If your site uses more than one Background Processor, use the list in the top of the dialog to select the Background Processor you want to use for IMPORT queue processing.
4.  Select the IMPORT check box.
5.  ![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/033.png)Click to close the dialog.
6.  In the main window, resume queue processing functions by clicking Start.

## Establishing Diagram-specific Progress Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For each diagram template (or closely related group of diagram templates), you will need to use the TIU package to create a progress note. This can be done using the TIU Document Definitions Manager menu \[TUIF DOCUMENT DEFINITION MGR\].[<sup>\*</sup>](#_bookmark30)

> When defining progress note titles, it is recommended that the following naming conventions be used for the title.

> DIAGRAM—\<procedure/event\>—\<specialty\>

> DIAGRAM is a specific value in the IMAGE INDEX FOR TYPES file (#2005.83).

> \<procedure/event\> if used, should match an entry in the IMAGE INDEX FOR PROCEDURE/EVENT file (#2005.85,.01).

> \<specialty\> if used, should match an entry in the IMAGE INDEX FOR SPEC/SUBSPEC file (#2005.84,.01).

> Each value in the title should be separated with a non-space character. Typically a hyphen should be used.

> Once created, the new progress notes will need to be associated with the Diagram Annotation tool using the CPRS Template Editor. For more information, see page [<u>17</u>](#linking-progress-notes-with-the-diagrams-in-cprs).

## Setting up the COM Object Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new entry for the Diagram Annotation tool will need to be added to the OE/RR COM OBJECTS file (#101.15). This entry will make the Diagram Annotation tool available as a COM Object in the CPRS Template Editor.

1.  Log into the VistA Hospital Information System and use FileMan to select the OE/RR COM OBJECTS file (#101.15) for editing.
2.  Name the new entry ‘DIAGRAM’.

> <span id="_bookmark30" class="anchor"></span><sup>\*</sup> For detailed information, refer to the “Document Definition Setup” chapter in the TIU/ASU Implementation Guide.

3.  <span id="_bookmark31" class="anchor"></span>At the next prompt, enter the following value as the Object GUID. Be sure to enclose the value in braces { }.

### {9B6B82F4-14DF-493B-B7FE-2EF349F19167}

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  Press Enter to cycle through the next two prompts, then enter ‘Annotate Diagrams’ as the description.

## Linking Progress Notes with the Diagrams in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CPRS Template Editor will need to be used to link each diagram-specific progress note title to the Diagram Annotation tool.

> NOTE Access to the Template Editor is limited to users defined in the TIU Package as members of the Clinical Coordinator TIU User Class.

> To link a progress note title to the Diagram Annotation tool

1.  Launch CPRS Chart and select any patient.
2.  Select the Notes tab, then click Options \| Edit Shared Templates. The Template Editor will open.
3.  In the Shared Templates area, right click the Document Titles group, then click New Template.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/034.png)

4.  Enter a temporary name in the Name box (located on the right side of the window). The name you enter will be replaced by an existing progress note title in a later step.
5.  Set the Template Type to COM Object. If COM Object is not available in the list, the steps in the previous section were not performed.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/035.png)

6.  In the bottom of the window, use the Associated Title box to select the progress note that you want associated with the Diagram Annotation tool. The title you select will replace the temporary title you created in Step 4.
7.  In the COM Object list, select Diagram.
8.  If you used subfolders to organize the diagram template repository, enter the name of the appropriate subfolder in the Passed Value box.

> Note that while multiple levels of subfolders can be defined under ‘In’ in the diagram repository, only the highest-level subfolder name can be entered as a passed value.

9.  When you are finished, the Shared Template dialog should look similar to the example below. Click OK save the Title/Template association.

![](mag-3-48-diagram-annotation-tool-user-and-setup-guide/036.png)

## Diagram Annotation Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span class="mark">REDACTED</span>