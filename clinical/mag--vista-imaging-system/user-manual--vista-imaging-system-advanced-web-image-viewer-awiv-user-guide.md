---
title: VistA Imaging System Advanced Web Image Viewer (AWIV) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VistA Imaging System Advanced Web Image Viewer (AWIV)
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: archive
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
  - image
  - blockquote
  - awiv
  - viewer
  - table
  - contents
  - vista
  - imaging
  - advanced
  - guide
page_count: 0
word_count: 6898
section_count: 46
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: March 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag_awiv_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag_awiv_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=413"
---

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/001.png)

VistA Imaging System

Advanced Web Image Viewer (AWIV) User Guide

> March 2013 – Revision 2.0

> Department of Veterans Affairs Office of Enterprise Development Health Provider Systems

> Advanced Web Image Viewer (AWIV) User Guide

> VistA Imaging MAG\*3.0\*124 March 2013

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Office of Enterprise Development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: [REDACTED](https://vaww.edis2.med.va.gov/main)

> VA intranet: [REDACTED](https://vaww.edis2.med.va.gov/main)

> Revision History

| Date  | Rev | Notes                                                                                                                                                                                                                                                                 |
|-----------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mar 2013  | 2.0     | Added Web Application section and DoD abstract info. [REDACTED](https://vaww.edis2.med.va.gov/main) . Updated for Patch 124. Added section on AWIV Web Application; added Print button and images of toolbars; copyedited. [REDACTED](https://vaww.edis2.med.va.gov/main) |
| Oct 2010  | 1.0     | Updated per WPR. [REDACTED](https://vaww.edis2.med.va.gov/main)                                                                                                                                                                                                           |
| Sept 2010 | .9      | Initial draft; WPR complete. [REDACTED](https://vaww.edis2.med.va.gov/main)                                                                                                                                                                                               |

> Contents

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Terms of Use](#terms-of-use)
  - [Conventions](#conventions)
  - [Related Information](#related-information)
  - [Getting Help](#getting-help)
- [AWIV Overview](#awiv-overview)
  - [How the AWIV Works](#how-the-awiv-works)
  - [Main AWIV Window](#main-awiv-window)
  - [How the AWIV Handles Images](#how-the-awiv-handles-images)
  - [AWIV Web Application](#awiv-web-application)
- [Getting to the AWIV](#getting-to-the-awiv)
  - [Launching the AWIV Using VistAWeb](#launching-the-awiv-using-vistaweb)
  - [Launching the AWIV Using the AWIV Web Application](#launching-the-awiv-using-the-awiv-web-application)
- [Viewing Images Using Abstracts](#viewing-images-using-abstracts)
  - [Loading Images](#loading-images)
  - [Viewing a Study Report](#viewing-a-study-report)
  - [DoD Image Abstracts](#dod-image-abstracts)
  - [Working with Abstracts](#working-with-abstracts)
- [Using the Full Resolution Viewer](#using-the-full-resolution-viewer)
  - [Changing Image Orientation](#changing-image-orientation)
  - [Changing Image Size](#changing-image-size)
    - [To resize an image](#to-resize-an-image)
    - [To zoom in or out incrementally](#to-zoom-in-or-out-incrementally)
    - [To zoom to a specified value](#to-zoom-to-a-specified-value)
    - [To use the Zoom Slider](#to-use-the-zoom-slider)
    - [To use the Zoom In on Selected Area Tool](#to-use-the-zoom-in-on-selected-area-tool)
    - [To use the Mouse Magnifier Tool](#to-use-the-mouse-magnifier-tool)
  - [Panning Images](#panning-images)
  - [Adjusting Brightness/ Contrast](#adjusting-brightness-contrast)
  - [Inverting an Image](#inverting-an-image)
  - [Printing an Image](#printing-an-image)
  - [Working with Multi-Page Images](#working-with-multi-page-images)
  - [Working with Multiple Images](#working-with-multiple-images)
  - [Resetting an Image](#resetting-an-image)
  - [Refreshing an Image](#refreshing-an-image)
  - [Removing Images](#removing-images)
    - [To remove some or all images from the main image display area](#to-remove-some-or-all-images-from-the-main-image-display-area)
- [Using the Radiology Viewer](#using-the-radiology-viewer)
  - [Images Available in a Study](#images-available-in-a-study)
  - [Choosing a Series to View](#choosing-a-series-to-view)
  - [Changing Image Orientation](#changing-image-orientation-1)
  - [Changing Image Size](#changing-image-size-1)
    - [To resize an image](#to-resize-an-image-1)
    - [To use the Zoom Slider](#to-use-the-zoom-slider-1)
    - [To use the Zoom In on Selected Area tool](#to-use-the-zoom-in-on-selected-area-tool-1)
    - [To use the Mouse Magnifier tool](#to-use-the-mouse-magnifier-tool-1)
  - [Printing an Image](#printing-an-image-1)
  - [Getting Diagnostic Quality Images](#getting-diagnostic-quality-images)
  - [Changing Window/Level](#changing-windowlevel)
    - [To change window/level with the mouse](#to-change-windowlevel-with-the-mouse)
    - [To use the Auto Window/ Level tool](#to-use-the-auto-window-level-tool)
    - [To change window/level using toolbar sliders](#to-change-windowlevel-using-toolbar-sliders)
  - [Using the Protractor to Measure Angles](#using-the-protractor-to-measure-angles)
    - [To measure an angle](#to-measure-an-angle)
    - [To change the angle after making an angle selection](#to-change-the-angle-after-making-an-angle-selection)
  - [Using the Ruler Tool](#using-the-ruler-tool)
  - [Panning Images](#panning-images-1)
    - [To pan an image with the mouse](#to-pan-an-image-with-the-mouse)
    - [To use the pan window](#to-use-the-pan-window)
  - [Resetting an Image](#resetting-an-image-1)
  - [![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/077.png)Inverting an Image](#vista-imaging-system-advanced-web-image-viewer-awiv-user-guide077pnginverting-an-image)
  - [Scrolling Through Images](#scrolling-through-images)
  - [Using the Cine Viewer](#using-the-cine-viewer)
- [Using Other Viewers](#using-other-viewers)
  - [Viewing Documents](#viewing-documents)
  - [Viewing Movie Files](#viewing-movie-files)
    - [Options \| Show Progress Bar.](#options-show-progress-bar)
- [Closing the AWIV](#closing-the-awiv)
- [Troubleshooting](#troubleshooting)
  - [About the AWIV](#about-the-awiv)
  - [Message Log](#message-log)
- [Appendix B – AWIV Toolbars](#appendix-b-awiv-toolbars)
  - [Full Resolution Viewer Toolbars](#full-resolution-viewer-toolbars)
  - [Radiology Viewer Toolbars](#radiology-viewer-toolbars)
> This manual describes the VistA Imaging Advanced Web Image Viewer (AWIV). It is intended for clinicians who use VistAWeb and need access to images. This manual assumes that a current version of the AWIV is installed and that users are familiar with the Microsoft Windows environment.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use of the AWIV is subject to the following provisions:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/002.png)</p>
</blockquote></th>
<th><blockquote>
<p>Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/003.png)</p>
</blockquote></td>
<td><blockquote>
<p>The AWIV is not intended for the primary interpretation of radiology exams. When the AWIV is installed on approved and properly maintained hardware, primary interpretation of other image types is permissible by licensed practitioners at their discretion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/004.png)</p>
</blockquote></td>
<td><blockquote>
<p>The FDA classifies VistA Imaging, and the AWIV (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, including the AWIV, such as the installation of unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses the following conventions:

- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate menu choices. For example: “Click File \| Open” means: “Click the File menu, then click the Open option.”
- Keyboard key names are shown in bold and in brackets.
- Sample output is shown in monospace.
- When this document is used online, hyperlinks are indicated by blue text.
- Useful or supplementary information is shown in a Tip.
- Important or required information is shown in a NOTE.
- ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/005.png)Critical information is indicated by:

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additional information about VistA Imaging and VistAWeb can be found at:

- VistAWeb: [<u>http://www.va.gov/vdl/application.asp?appid=147</u>](http://www.va.gov/vdl/application.asp?appid=147)
- VistA Imaging: [REDACTED](https://vaww.edis2.med.va.gov/main)

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you encounter any problems using the AWIV, contact your local Imaging Coordinator or support staff. If the problem cannot be resolved locally, use Remedy to place a service request, or contact the National Help Desk at 1-888-596-4357.

# AWIV Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How the AWIV Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging Advanced Web Image Viewer (AWIV) adds image display capabilities to VistAWeb in much the same way that the Clinical Display application adds image display capabilities to the Computerized Patient Record System (CPRS). The AWIV is a Web-based application and hence provides a subset of the features of Clinical Display.

> With the AWIV, a user can display images associated with progress notes or radiology reports within the VistAWeb application.

> The VistA Imaging AWIV can be launched either from the VistAWeb in a VA-approved version of Microsoft Internet Explorer or from within the AWIV Web Application.

> VistAWeb (version 13 or later) displays an image icon to allow the user to launch the AWIV. Whereas, double-clicking any study from within the AWIV Web Application launches the AWIV.

> The AWIV retrieves information and images from across the VA WAN. This may affect the performance of the AWIV in displaying images.

> Note that certain Clinical Display features (such as filters) and image types (such as EKG images stored on MUSE servers) are not available in the AWIV.

> NOTE: Turn off pop-up blockers on your computer to allow opening the AWIV component in a new browser window. The AWIV Web Application is hosted on the CVIX and enables use of the AWIV via Microsoft Internet Explorer, independent of VistAWeb. When the AWIV Web Application is used, workstations do not require access to VistAWeb or access to VistA Imaging Clinical Display. Images will be available in a Web-based interface, making it easier for users to access the images. Users can view images available in VistA Imaging and the Department of Defense (DoD), including Neurocognitive Assessment Tool (NCAT) reports, and radiology images and artifacts stored in Healthcare Artifact and Image Management Solution (HAIMS) using AWIV through Microsoft Internet Explorer 7, 8, or 9. For more information on using the AWIV Web Application, see the *VistA Imaging AWIV Web Application User Guide.*

> NOTE: The NCAT system must be online and available in order for AWIV users to view NCAT reports.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/006.png)![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/007.png)

## Main AWIV Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The image below shows the main AWIV window and the various components of this window.

AWIV Overview

## How the AWIV Handles Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Most images handled by the AWIV are shown in one of two primary viewers, the Full Resolution style viewer, or the Radiology style viewer. These two viewers incorporate many of the controls available in the similarly named viewers in Clinical Display. In general, images associated with progress notes are shown in the Full Resolution Viewer, and images associated with radiology are shown in the Radiology Viewer. However, there are exceptions to this.

> The AWIV uses outside viewers to handle certain types of images and non-image objects. For example, Word documents are opened in Microsoft Word if Word is available. For a detailed list of image types and the viewer associated with each type, see [*Appendix A - Supported File Extensions*.](#Appendix_A_-_Supported_File_Extensions)

## AWIV Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging AWIV Web Application enables users to access patient images using VA approved versions of Internet Explorer independent of VistAWeb and VistA Imaging Clinical Display, similar to the way that VistAWeb currently does. The AWIV Web Application can be accessed using the URL: [REDACTED](https://vaww.edis2.med.va.gov/main)

> The AWIV Web Application allows users to locate and display any patient images available to the VA from VistA Imaging, the DoD, including NCAT reports, and radiology images and artifacts stored in HAIMS.

> NOTE: The NCAT system must be online and available in order for AWIV users to view NCAT reports.

> For more information on AWIV Web Application, see the *VistA Imaging AWIV Web Application User Guide.*

> This page is intentionally blank.

# Getting to the AWIV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Launching the AWIV Using VistAWeb

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AWIV can be launched from within VistAWeb. To launch the AWIV and display images, you will first need to select the patient and record that is associated with the remote images you want to view.

> The following steps summarize how this is done when VistAWeb is launched in a standalone mode directly from a browser.

> NOTE: Turn off pop-up blockers on your computer to allow opening the AWIV component in a new browser window.

1.  Start VistAWeb.
2.  In VistAWeb, select the site that you want to access.
3.  Log in to the site when you are prompted to do so.
4.  Select a patient.
5.  Use the list on the left side of the page to view the progress notes or radiology reports for the selected patient.
6.  Use the controls at the top of the page to query for the records you want to view. A list of records is displayed.
7.  Records with associated images display an image icon ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/008.png) in the AWIV column. Click the icon to launch the AWIV.

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/009.png)

8.  The AWIV window opens and images are presented as abstracts on the left side of the window. To view images, click abstracts as described in the following section.

> If you launch VistAWeb from the CPRS, the specific steps you use will vary.

> For specific information on how to launch VistAWeb from CPRS, see the VistAWeb User Guide at [<u>http://www.va.gov/vdl/application.asp?appid=147</u>.](http://www.va.gov/vdl/application.asp?appid=147)

## Launching the AWIV Using the AWIV Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To display images using the AWIV Web Application,

1.  Go to the URL [[REDACTED](https://vaww.edis2.med.va.gov/main)](https://vhacvixclu2.r04.med.va.gov/Awiv/) using a VA approved version of Internet Explorer.
2.  Select a site (to which the user has credentials) to log into.
3.  Select a patient.
4.  Select one or more sites that the patient has been seen at in the site information bar, to display studies from that site(s).
5.  Click on a study to open images in the AWIV.
6.  Review and manipulate images as needed, using the AWIV.

> For more details on how to use the VistA Imaging AWIV Web Application, refer to the

> *AWIV Web Application User Guide*.

# Viewing Images Using Abstracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Loading Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the AWIV window opens, it displays abstract placeholders until the abstracts themselves are retrieved.

> NOTE: You can click abstracts and work with them while they are being retrieved. The abstracts do not have to be fully loaded.

> To display images associated with abstracts,

1.  ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/010.png)On the left side of the AWIV window, locate the abstract for the image you want to load.
2.  Click the desired abstract. A progress icon with a yellow arrow image is being retrieved.

> indicates that the

3.  ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/011.png)Wait until the progress icon turns green image display area.

## Viewing a Study Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> . At this point the image is loaded in the main

> To view the associated progress note or study report, right-click an abstract and click

> Study Report. The report or progress note will display in the Study Report window.

## DoD Image Abstracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you select a DoD artifact, the AWIV window opens with all image abstracts automatically loaded in the abstracts area, and the selected abstract displayed in the main AWIV viewer or in an external viewer (depending on the image type).

> NOTE: This only applies to DoD NCAT and non-radiology artifacts from HAIMS selected from within the AWIV Web Application.

## Working with Abstracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can use the functions described below to change how abstracts are displayed.

> NOTE: Any changes made to the abstracts as described below apply only to the current session. They will not be saved for subsequent sessions.

> <span id="Resizing_Abstracts" class="anchor"></span>Resizing Abstracts

> To resize abstracts,

1.  Right-click any abstract.
2.  Click Resize the abstracts… A message box displays.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/012.png)

> NOTE: Do not click Finished until after you have completed resizing images.

3.  Resize the abstract by dragging the highlighted edges or a corner of the abstract to desired size, as shown in the image below.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/013.png)

4.  Click Finished in the pop-up window when you have finished resizing the abstract. All abstracts in the study selected will be resized.

> <span id="Changing_Font_Size" class="anchor"></span>Changing Font Size

> To change the size of the image title font displayed,

1.  Right-click an abstract.

> Viewing Images Using Abstracts

2.  Click Font Size.
3.  Select one of the available font sizes. The font will be resized.

> <span id="Using_the_Abstracts_Toolbar" class="anchor"></span>Using the Abstracts Toolbar

> To show the abstracts toolbar, right-click an abstract and click Toolbar.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/014.png)

> Using the abstracts toolbar, you can:

- Navigate abstracts using Previous ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/015.png) and Next ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/016.png).
- Resize abstracts using Zoom In ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/017.png) and Zoom Out ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/018.png).
- Refresh abstracts using Refresh![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/019.png).

> <span id="Arranging_the_Abstracts_Horizontally" class="anchor"></span>Arranging the Abstracts Horizontally

> In the AWIV window, abstracts are arranged vertically by default. To temporarily display abstracts horizontally, right-click an abstract, and click Scroll \| Horizontal.

> This page is intentionally blank.

# Using the Full Resolution Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AWIV uses the Full Resolution Viewer for most non-DICOM images. The Full Resolution Viewer can be recognized by three image manipulation toolbars displayed at the top of the image area. (The Radiology Viewer has two toolbars at the top and one at the side).

> The following sections explain how to work with images in the Full Resolution Viewer using the buttons in the image manipulation toolbars.

> For information about the Radiology Viewer, see page [16.](#_bookmark37)

## Changing Image Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To change the orientation of an image,

- ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/020.png)![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/021.png)To flip the image vertically, click Flip Vertical .
- To flip the image horizontally, click Flip Horizontal .
- To rotate the image counter clockwise, click Rotate Counter Clockwise 90 ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/022.png).
- To rotate the image clockwise, click Rotate Clockwise 90 ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/023.png).

## Changing Image Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changing an image size in the Full Resolution Viewer includes resizing an image, zooming, using the mouse magnifier and resetting the image. Below are instructions on how to use each of these functions.

### To resize an image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To fit the image in the window, click Fit Image to Window ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/024.png).
- To fit the entire image width in the window, click Fit Image Width button ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/025.png).

### To zoom in or out incrementally

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To zoom in on an image, click Zoom In ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/026.png).
- To zoom out from an image, click Zoom Out ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/027.png).

> March 2013 VistA Imaging v 3.0 11

### To zoom to a specified value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click the arrow on the Zoom Out/Zoom Menu ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/028.png).
2.  Choose one of the available settings.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/029.png)

### To use the Zoom Slider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click the Zoom Slider ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/030.png).
2.  Drag the bar until desired zoom level is reached for the image.
3.  Alternatively, click the arrows on the left and right of the slider bar.

### To use the Zoom In on Selected Area Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Zoom In on Selected Area![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/031.png) on the toolbar.
2.  Drag the mouse to define a rectangular area that contains the image feature you want to magnify.
3.  Release the left mouse button. The selected area will be enlarged to fit the available display area.

### To use the Mouse Magnifier Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Mouse Magnifier![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/032.png).
2.  Point to an area in the image and drag the mouse. A magnification area will display and will move as you drag the mouse.
3.  Release the left mouse button. The magnified area will disappear on its own.

## Panning Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To pan an image that is larger than the display area, left-click in the image and drag to view the desired part.

## Adjusting Brightness/ Contrast

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To adjust the brightness of an image, click the brightness slider ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/033.png) and drag to achieve desired brightness level.
2.  To adjust the contrast of an image, click the contrast slider ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/034.png) and drag to achieve desired contrast level.

## Inverting an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To invert an image, click Invert Image ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/035.png) on the toolbar.

## Printing an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To print an image, click Print Image ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/036.png) on the toolbar.

## Working with Multi-Page Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When multiple pages are available in a single image, the scroll buttons in the middle image manipulation toolbar are enabled. To scroll through multiple pages, use the scroll buttons on the toolbar.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/037.png)

- ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/038.png)![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/039.png)![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/040.png)Click to go to the next page.
- Click to go to the previous page.
- Click to go to the first page.
- Click to go to the last page.

## Working with Multiple Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When multiple images are available, you can choose to display one or all of the available images in the main image display area by clicking the abstracts. There are several other AWIV functions multiple images, which are described below.

> <span id="To_Change_Layout" class="anchor"></span>To Change Layout

1.  To tile images currently displayed in the main image display area, click Tile Images ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/041.png)

> on the toolbar.

2.  To maximize an image, click the arrow on the Maximize Image (Layout utils.) ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/042.png) on the toolbar, and click Maximize Image.
3.  To control how many images are displayed at one time in the main image display area, click the arrow on the Maximize Image (Layout utils.) ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/043.png) and then choose one of the available layouts.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/044.png)

> <span id="Using_Viewer_Pages" class="anchor"></span>Using Viewer Pages

> If images are laid out across multiple pages, use the Previous Viewer Page and the Next Viewer Page options in the Maximize Image menu to switch between pages.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/045.png)

> <span id="To_apply_actions_to_all_images" class="anchor"></span>To apply actions to all images

> To apply selected actions to all images currently displayed in the main image display area,

1.  ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/046.png)Click Apply Actions to all Images on the toolbar.
2.  Select an action from one of the toolbar options, to apply that action to all images currently displayed in the main image display area.

## Resetting an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To undo any changes made to an image, click Reset ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/047.png).

## Refreshing an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To refresh/reload an image, click Refresh ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/048.png) on the toolbar.

## Removing Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To remove some or all images from the main image display area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To remove a single image, click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/049.png) in the upper right corner of the image.
2.  ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/050.png)To remove multiple images CTRL-Click the images to remove and then click Remove Selected Images ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/051.png) on the toolbar.
3.  To remove all images, click Remove All Images on the toolbar<span id="_bookmark37" class="anchor"></span>.

> This page intentionally left blank.

# Using the Radiology Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While the AWIV Web Application allows access to other types of images, the AWIV uses the Radiology Viewer to view and manipulate DICOM radiology images. The Radiology Viewer can be recognized by two toolbars at the top and side of the image display area. (The Full Resolution Viewer has three toolbars.)

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/052.png)

> The following sections explain how to work with images in the Radiology Viewer. For information about the Full Resolution Viewer, see page 11.

## Images Available in a Study

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there are multiple images, the information bar above the image displays, the number of images available in that study as shown in the image below.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/053.png)

## Choosing a Series to View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view a particular series of images, use the dropdown menu in the information bar above the image to select the series.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/054.png)

> March 2013 VistA Imaging v 3.0 17

## Changing Image Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To change the orientation of an image, use toolbar buttons as follows,

- To flip the image vertically, click Flip Vertical ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/055.png).
- To flip the image horizontally, click Flip Horizontal ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/056.png).
- To rotate the image to the left, click Rotate Left ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/057.png).
- To rotate the image to the right, click on Rotate Right ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/058.png).

## Changing Image Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can resize an image, zoom, use the mouse magnifier, and reset images to their original viewing size, as follows,

### To resize an image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To fit the image in the window, click Fit Image to Window ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/059.png).
- To fit the entire image height in the window, click Fit Image Height ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/060.png).
- To fit the entire image width in the window, click Fit Image width ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/061.png).
- To view the image in its original size, click Actual Size ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/062.png).

### To use the Zoom Slider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click the Zoom slider ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/063.png).
2.  Drag the bar until desired zoom level is reached for the image.
3.  Alternatively, click the arrows on the left and right of the slider bar.

### To use the Zoom In on Selected Area tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Zoom In on Selected Area ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/064.png) on the toolbar.
2.  Drag the mouse to define a rectangular area that contains the image feature you want to magnify.
3.  Release the left mouse button. The selected area will be enlarged to fit the available display area.

### To use the Mouse Magnifier tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Mouse Magnifier ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/065.png) on the toolbar.
2.  Point to an area in the image and drag the mouse. A magnification area will display and will move as you drag the mouse.
3.  Release the left mouse button. The magnified area will disappear on its own.

## Printing an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To print an image, click Print Image ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/066.png) on the toolbar.

## Getting Diagnostic Quality Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there are both reference and diagnostic quality versions of an image available, the AWIV will display the reference quality image by default. This is done to reduce the time needed for images to load across the VistA Imaging WAN.

> When reference-quality images are displayed in the main image window, the yellow bar displayed near the bottom of the window indicates that this is a reference quality image with the phrase “Reduced size – Reference quality image.”

> To retrieve the diagnostic quality image,

1.  ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/067.png)Right-click an abstract.
2.  Select “Get Diagnostic Image.” A progress icon with a yellow arrow image is being retrieved.
3.  Wait for the diagnostic image to display.

## Changing Window/Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> indicates that the

> You can change the window/level of an image using the mouse. You can also use the auto-window/level tool to base window/level values on a selected area in an image.

### To change window/level with the mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Point to the image you want to adjust and drag using the right mouse button.
2.  Drag up or down to change window (window width) values.
3.  Drag left or right to change level (window center) values.

### To use the Auto Window/ Level tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Auto Window/Level ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/068.png) in the toolbar near the top of the window.
2.  In the image you want to adjust, drag the mouse to define a rectangular area that includes the tissue you want to base the window/level on.
3.  When the drag is completed, the new window/level values will be applied to the entire image.
4.  Continue using the Auto-Window/Level tool, or disable it by choosing another tool.

### To change window/level using toolbar sliders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can also click Win. / Lev. ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/069.png) on

> the toolbar and change window/level by dragging with the left mouse button or by using the slider.

## Using the Protractor to Measure Angles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To measure an angle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To enable the option, click Protractor ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/070.png).
2.  Once the option is selected, click the mouse on the image, to begin measuring the angle.
3.  Drag mouse to stop point and click once again to draw the line.
4.  Select desired area and draw an angled line to measure angle. The angle between the lines is displayed on the image, as shown below.

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/071.png)

### To change the angle after making an angle selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click the Use Protractor Ruler Pointer ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/072.png).
2.  Select the line to extend in the angle.
3.  Drag the line to desired location.
4.  Re-measure angle.

> NOTE: You can delete an angle measurement by clicking the Reset Image button.

## Using the Ruler Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To measure a feature in an image,

1.  Click Ruler ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/073.png) on the toolbar.
2.  Click on the image to start measuring.
3.  Drag to desired area to get a measurement. The length is displayed on the image, as shown below.

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/074.png)

> NOTE: The ruler is available only if the applicable sizing information is available in the DICOM image header.

## Panning Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To pan an image with the mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To pan an image that is larger than the display area, left click and drag to view desired part of the image.

### To use the pan window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To pan an image using a pan window,

1.  Click Pan Window ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/075.png) in the tool bar above the image.
2.  Click and drag the rectangular box that appears in the pan window to move to the desired area in the image.

## Resetting an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To undo any changes made to an image click Reset ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/076.png) to restore the original image.

## ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/077.png)Inverting an Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To invert an image, click Invert Image on the toolbar.

## Scrolling Through Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If multiple images are available in the study, you can scroll through these images by using the scroll tools available to the left of the image.

- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/078.png) to go to next image.
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/079.png) to go to previous image.
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/080.png) to go to the first image in the study.
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/081.png) to go to the last image in the study
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/082.png) to play the images as a slide show.
- To change the speed of the slide show, drag the smaller slider at the bottom of the scroll tools. Speed increases as you drag from top to bottom. ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/083.png)

> You can also scroll through images using the long vertical slider bar. Drag the slider from top to bottom to go to the next image.

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/084.png)

## Using the Cine Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When DICOM multi-frame images are loaded in the Radiology Viewer, a special toolbar displays automatically. You can use this to work with multi-frame images as described below.

> ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/085.png)

- To play the study, click Cine.
- To stop playing the study, click Stop.
- To returns to the first page in the study, click Reset.
- To repeat play, select the Repeat option in the Play Mode area.
- To play once, select the Play once option in the Play Mode area.
- To change the play speed, click and drag the Cine Speed slider.
- To go to the previous page in the study, click PrevPg. Alternatively, use the page slider.
- To go to the next page in the study, click NextPg. Alternatively, use the page slider.

# Using Other Viewers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Viewing Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a progress note or radiology report has a Word .doc file or .avi movie file associated with it, the AWIV launches the appropriate outside viewer when abstracts for these files are selected.

> Clicking Word documents will open the document in a Microsoft Word window.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/086.png)</p>
</blockquote></th>
<th><blockquote>
<p>If you close the AWIV and select another patient in VistAWeb, the .doc file with information for the previous patient remains displayed.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Viewing Movie Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a selected patient image is a motion video clip, it will open in the Video Player window, as shown below.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/087.png)

- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/088.png) to play.
- ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/089.png)Click to pause play.
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/090.png) to stop playing.
- Click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/091.png) to rewind.
- Click and drag the slider to browse the video clip, frame by frame.
- Click View \| Set Start Point to set start point.
- Click View \| Set End Point to set end point.
- Click Options \| Video Loop to continuously play all or part of the file.
- You can choose to display or hide the progress bar in the video player, by clicking

### Options \| Show Progress Bar.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With the progress bar,

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/092.png)

> Without the progress bar,

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/093.png)

# Closing the AWIV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To close the AWIV window, click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/094.png) in the upper right hand corner of the AWIV Window or click either of the Close buttons at the top and bottom of the AWIV window.

> NOTE: The AWIV closes automatically when a different patient is selected in either VistAWeb or in the AWIV Web Application.

> This page is intentionally blank.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About the AWIV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To display version and memory usage information about the AWIV, click the About

> button located in the lower left corner of the AWIV window.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/095.png)

## Message Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Message History window is used to view system messages for debugging purposes. To open this window, click Message History ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/096.png) in the lower left corner of the AWIV window to view message history as shown in the image below.

![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/097.png)

> To exit the message history window, click ![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/098.png) in the top right corner of the Message History window or click File \| Exit.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="Glossary" class="anchor"></span><strong>Acronym /Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AWIV</td>
<td>Advanced Web Image Viewer</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>DICOM</td>
<td>Digital Imaging and Communications in Medicine</td>
</tr>
<tr class="even">
<td>EKG</td>
<td>Electrocardiogram</td>
</tr>
<tr class="odd">
<td>FAQ</td>
<td>Frequently Asked Questions</td>
</tr>
<tr class="even">
<td>FDA</td>
<td>Food and Drug Administration</td>
</tr>
<tr class="odd">
<td>HIMS ROI</td>
<td>Health Information Management Services Release of Information (department)</td>
</tr>
<tr class="even">
<td>ID</td>
<td>Identifier or Identification</td>
</tr>
<tr class="odd">
<td>Multi-frame</td>
<td>A DICOM image that contains multiple two-dimensional pixel planes in a single file. When the file is displayed, each plane (frame) is presented as a separate image. This separation is automatically handled in the Radiology Viewer.</td>
</tr>
<tr class="even">
<td>MUSE</td>
<td>A third party cardiology information system used to store and manage ECG/EKG (electrocardiogram) images. If a VA facility stores their ECG images in MUSE, they will not be accessible to the AWIV.</td>
</tr>
<tr class="odd">
<td>TGA</td>
<td>Targa (image type)</td>
</tr>
<tr class="even">
<td>US</td>
<td>United States</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Veteran Affairs</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information System and Technology Architecture</td>
</tr>
<tr class="odd">
<td>VistAWeb</td>
<td>VistAWeb is an intranet web application used to review remote stored VistA and Health Data Repository (HDR) patient information; see <a href="http://vista.med.va.gov/vistaweb/index.htm"><span>REDACTED</span></a> for details about VistAWeb</td>
</tr>
</tbody>
</table>

> This page is intentionally left blank.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="Appendix_A_-_Supported_File_Extensions" class="anchor"></span><strong>Extension</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Associated Viewer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>756</td>
<td><blockquote>
<p>Historical 756</p>
</blockquote></td>
<td>Radiology Viewer or Full Resolution Viewer depending on image type.</td>
</tr>
<tr class="even">
<td>ABS</td>
<td><blockquote>
<p>Abstract file</p>
</blockquote></td>
<td>Abstract area</td>
</tr>
<tr class="odd">
<td>ASC</td>
<td>ASCII text file</td>
<td>Not Supported</td>
</tr>
<tr class="even">
<td>AVI</td>
<td>Motion video</td>
<td>Video Player</td>
</tr>
<tr class="odd">
<td>BIG</td>
<td><blockquote>
<p>X-ray file 2000K</p>
</blockquote></td>
<td>Radiology Viewer</td>
</tr>
<tr class="even">
<td>BMP</td>
<td><blockquote>
<p>Bitmap</p>
</blockquote></td>
<td>Full Resolution Viewer</td>
</tr>
<tr class="odd">
<td>BW</td>
<td><blockquote>
<p>Black and white</p>
</blockquote></td>
<td>Radiology Viewer or Full Resolution Viewer depending on image type.</td>
</tr>
<tr class="even">
<td>DCM</td>
<td>DICOM</td>
<td>Radiology Viewer</td>
</tr>
<tr class="odd">
<td>DOC</td>
<td><blockquote>
<p>MS Word document</p>
</blockquote></td>
<td>Microsoft Word</td>
</tr>
<tr class="even">
<td>DOCX</td>
<td><blockquote>
<p>MS Word document</p>
</blockquote></td>
<td>Microsoft Word</td>
</tr>
<tr class="odd">
<td>HTM</td>
<td><blockquote>
<p>Web HTM document</p>
</blockquote></td>
<td>Not Supported</td>
</tr>
<tr class="even">
<td>HTML</td>
<td><blockquote>
<p>Web HTML document</p>
</blockquote></td>
<td>Not Supported</td>
</tr>
<tr class="odd">
<td>JPG</td>
<td><blockquote>
<p>JPEG full color</p>
</blockquote></td>
<td>Full Resolution Viewer</td>
</tr>
<tr class="even">
<td>MHT</td>
<td>MIME HTML web page archive</td>
<td>Not Supported</td>
</tr>
<tr class="odd">
<td>MHTML</td>
<td><blockquote>
<p>MIME HTML web page archive</p>
</blockquote></td>
<td>Not Supported</td>
</tr>
<tr class="even">
<td>MP3</td>
<td>Motion video MPEG-3</td>
<td>Not Supported</td>
</tr>
<tr class="odd">
<td>MP4</td>
<td>Motion video MPEG-4</td>
<td>Not Supported</td>
</tr>
<tr class="even">
<td>MPEG</td>
<td><blockquote>
<p>Motion video MPG</p>
</blockquote></td>
<td>Not Supported</td>
</tr>
<tr class="odd">
<td>MPG</td>
<td>Motion video MPG</td>
<td>Not Supported</td>
</tr>
<tr class="even">
<td>PAC</td>
<td>X-ray PAC image</td>
<td>Radiology Viewer</td>
</tr>
<tr class="odd">
<td>PDF</td>
<td><blockquote>
<p>Adobe PDF</p>
</blockquote></td>
<td>Full Resolution Viewer</td>
</tr>
<tr class="even">
<td>RTF</td>
<td><blockquote>
<p>Rich text format</p>
</blockquote></td>
<td>MS Word</td>
</tr>
<tr class="odd">
<td>TGA</td>
<td>TARGA image</td>
<td>Radiology Viewer</td>
</tr>
<tr class="even">
<td>TIF</td>
<td>Tagged Image File Format</td>
<td>Full Resolution Viewer</td>
</tr>
<tr class="odd">
<td>WAV</td>
<td><blockquote>
<p>Audio wave file</p>
</blockquote></td>
<td>Not Supported</td>
</tr>
</tbody>
</table>

> This page intentionally left blank.

# Appendix B – AWIV Toolbars

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Full Resolution Viewer Toolbars

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Full Resolution Viewer has three toolbars. Each toolbar is shown below with a description of each button on the toolbar.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/099.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/100.png)</p>
</blockquote></td>
<td>Apply</td>
<td><blockquote>
<p>Applies the actions to all images.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/101.png)</p>
</blockquote></td>
<td>Fit Image to Window</td>
<td><blockquote>
<p>Resizes the image to fit in the viewing window.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/102.png)</p>
</blockquote></td>
<td>Width</td>
<td>Fits the image to the width of the viewing window.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/103.png)</p>
</blockquote></td>
<td>Zoom In</td>
<td><blockquote>
<p>Incrementally magnifies the image.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/104.png)</p>
</blockquote></td>
<td>Zoom Out</td>
<td><blockquote>
<p>Decreases image magnification with each click.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/105.png)</p>
</blockquote></td>
<td>Mouse Magnifier</td>
<td>Allows the user to select a portion of the image to magnify using a mouse click.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/106.png)</p>
</blockquote></td>
<td>Zoom (Selected Area)</td>
<td>Allows the user to click an area to zoom in on the image. The image point selected zooms in or out with the movement of the mouse.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/107.png)</p>
</blockquote></td>
<td>Pointer</td>
<td><blockquote>
<p>Changes the mouse back to a pointer.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/108.png)</p>
</blockquote></td>
<td>Image Layout</td>
<td>Allows the user to specify the image size and layout. A drop down list appears when selected with options for the user to select.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/109.png)</p>
</blockquote></td>
<td>Tile Images</td>
<td><blockquote>
<p>Tiles the images.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/110.png)</p>
</blockquote></td>
<td>Rotate Image Counter Clockwise</td>
<td><blockquote>
<p>Rotates the Image 90 degrees counterclockwise.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/111.png)</p>
</blockquote></td>
<td>Rotate Image Clockwise</td>
<td><blockquote>
<p>Rotates the Image 90 degrees clockwise.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/112.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/113.png)</td>
<td><blockquote>
<p>Refresh Images</p>
</blockquote></td>
<td>Refreshes current image.</td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/114.png)</td>
<td>Remove Selected Images</td>
<td><blockquote>
<p>Removes the selected image from the Full</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>Resolution Viewer pane.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/115.png)</td>
<td>Remove all images</td>
<td><blockquote>
<p>Removes all of the images from Full Resolution Viewer pane.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/116.png)</p>
</blockquote></td>
<td>Print Image</td>
<td><blockquote>
<p>Prints the image.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/117.png)</td>
<td><blockquote>
<p>Flip Vertical</p>
</blockquote></td>
<td><blockquote>
<p>Flips the image vertically.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/118.png)</td>
<td><blockquote>
<p>Flip Horizontal</p>
</blockquote></td>
<td><blockquote>
<p>Flips the image horizontally.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/119.png)</td>
<td><blockquote>
<p>Invert Image</p>
</blockquote></td>
<td><blockquote>
<p>Inverts the image.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/120.png)</td>
<td><blockquote>
<p>Reset Image</p>
</blockquote></td>
<td><blockquote>
<p>Adjusts the image to its original size.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/121.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/122.png)</p>
</blockquote></td>
<td>Increases or decreases magnification.</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/123.png)</p>
</blockquote></td>
<td>Increases or decreases brightness.</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/124.png)</p>
</blockquote></td>
<td>Increases or decreases contrast.</td>
</tr>
</tbody>
</table>

> Appendix B – AWIV Toolbars

## Radiology Viewer Toolbars

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Radiology Viewer has two toolbars that can be used to manipulate images. Each toolbar is shown below with a description of each button on the toolbar.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 32%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/125.png)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/126.png)</p>
</blockquote></td>
<td>Reset Images</td>
<td><blockquote>
<p>Resets the image to its original settings.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/127.png)</p>
</blockquote></td>
<td>Fit Image to Window</td>
<td><blockquote>
<p>Resizes image to fit to the window.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/128.png)</p>
</blockquote></td>
<td>Fit Image to height.</td>
<td>Resizes image to fit to the height of the window.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/129.png)</p>
</blockquote></td>
<td>Fit Image to width.</td>
<td><blockquote>
<p>Resizes image to fit to the width of the window.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/130.png)</p>
</blockquote></td>
<td>Actual Size</td>
<td><blockquote>
<p>Resets the image to the actual size.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/131.png)</p>
</blockquote></td>
<td>Flip Vertical</td>
<td>Flips the image vertically.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/132.png)</p>
</blockquote></td>
<td>Flip Horizontal</td>
<td>Flips the image horizontally.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/133.png)</p>
</blockquote></td>
<td>Rotate Left</td>
<td><blockquote>
<p>Rotates the image to the left.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/134.png)</p>
</blockquote></td>
<td>Rotate right</td>
<td><blockquote>
<p>Rotates the image to the right.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/135.png)</p>
</blockquote></td>
<td>Invert Image</td>
<td>Inverts the image.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/136.png)</p>
</blockquote></td>
<td>Pan Image with mouse.</td>
<td><blockquote>
<p>Pans image on mouse click.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/137.png)</p>
</blockquote></td>
<td>Mouse Magnifier</td>
<td><blockquote>
<p>Magnifies image on mouse click.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/138.png)</p>
</blockquote></td>
<td>Zoom</td>
<td>Zooms in on the selected area.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/139.png)</p>
</blockquote></td>
<td>Ruler</td>
<td><blockquote>
<p>Measures on mouse click.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/140.png)</p>
</blockquote></td>
<td>Protractor</td>
<td><blockquote>
<p>Measures angle on mouse click.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/141.png)</p>
</blockquote></td>
<td>Ruler/Protractor pointer</td>
<td><blockquote>
<p>Moves lines drawn.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/142.png)</p>
</blockquote></td>
<td>Auto Window Level</td>
<td>Window control.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 32%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/143.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/144.png)</p>
</blockquote></td>
<td>Pan Window</td>
<td>Opens the pan window.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/145.png)</p>
</blockquote></td>
<td>Print Image</td>
<td>Prints the image.</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/146.png)</p>
</blockquote></td>
<td>Changes Window/ Level values of the image.</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>![](vista-imaging-system-advanced-web-image-viewer-awiv-user-guide/147.png)</p>
</blockquote></td>
<td>Zooms in or out of the image.</td>
</tr>
</tbody>
</table>