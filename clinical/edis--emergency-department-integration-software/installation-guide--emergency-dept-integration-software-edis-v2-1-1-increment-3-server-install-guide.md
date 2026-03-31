---
title: Emergency Dept Integration Software (EDIS) Version 2.1.1 Increment 3 Server Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Increment 3 Server Install Guide
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.1
patch_id: EDIS*2.1.1
group_key: "EDIS:EDIS:2.1.1"
file_numbers: []
security_keys: []
menu_options: 6
description: - [Department of Veterans Affairs](#department-of-veterans-affairs) - [Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3](#emergency-department-integration-software-edis-version-211-increment-3) - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server
audience: 
keywords: 
  - blockquote
  - edis
  - emergency
  - software
  - integration
  - server
  - version
  - increment
  - dept
  - instal
page_count: 0
word_count: 4843
section_count: 16
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2013
revision_count: 28
revision_newest: 7/17/2013
revision_oldest: 01/09/2012
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

# Department of Veterans Affairs


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs](#department-of-veterans-affairs)
    - [Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3](#emergency-department-integration-software-edis-version-211-increment-3)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/021.png)Product Description](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal021pngproduct-description)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/022.png)Referenced Documents](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal022pngreferenced-documents)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/023.png)Before Beginning the Update](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal023pngbefore-beginning-the-update)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/024.png)Retrieve patch EDP\2\6](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal024pngretrieve-patch-edp26)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/025.png)VistA Download Site download.vista.med.va.gov anonymous.software Check VistA Software Requirements](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal025pngvista-download-site-downloadvistamedvagov-anonymoussoftware-check-vista-software-requirements)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/026.png)Check the 230-234 Number Space](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal026pngcheck-the-230-234-number-space)
    - [Place and Protect New Globals](#place-and-protect-new-globals)
    - [Namespace and Number Space](#namespace-and-number-space)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/027.png)Installing M Server Components](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal027pnginstalling-m-server-components)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/028.png)Install patch EDP\2\6](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal028pnginstall-patch-edp26)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/029.png)Edit the EDPF LOCATION Parameter](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal029pngedit-the-edpf-location-parameter)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/030.png)Edit the EDPF NURSE STAFF SCREEN Parameter](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal030pngedit-the-edpf-nurse-staff-screen-parameter)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/031.png)Install and Configure VistALink for EDIS](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal031pnginstall-and-configure-vistalink-for-edis)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/032.png)Post Installation](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal032pngpost-installation)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/033.png)Rebuild Menus](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal033pngrebuild-menus)
    - [Assign Menu Options](#assign-menu-options)
    - [Rebuild Menu Trees](#rebuild-menu-trees)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/034.png)Assign Options for Emergency Department Users](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal034pngassign-options-for-emergency-department-users)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/035.png)Assign Keys for EDIS Users](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal035pngassign-keys-for-edis-users)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/036.png)Fixing the Primary/Secondary Status of a Bed](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal036pngfixing-the-primarysecondary-status-of-a-bed)
    - [Re-Index Files 230 & 231.8](#re-index-files-230-2318)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/037.png)Configure EDIS to work with other Applications](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal037pngconfigure-edis-to-work-with-other-applications)
  - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/038.png)Configure EDIS to Work with Omnicell](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal038pngconfigure-edis-to-work-with-omnicell)
- [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/039.png)Acronyms](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal039pngacronyms)

### Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Server Installation Guide
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/001.png)
> July 2013
> Document Version 3.3
> Document Revision History
| Date   | Document Version | Description                                             | Author                         |
|------------|----------------------|-------------------------------------------------------------|------------------------------------|
| 01/09/2012 | 1.0                  | Initial EDIS v2.0                                           | <span class="mark">REDACTED</span> |
| 01/10/2012 | 1.0                  | Technical Review                                            | <span class="mark">REDACTED</span> |
| 01/11/2012 | 2.0                  | Technical Edits                                             | <span class="mark">REDACTED</span> |
| 01/12/2012 | 2.0                  | Final Review prior to Submission                            | <span class="mark">REDACTED</span> |
| 02/28/2012 | 2.1                  | Post Installation Updates                                   | <span class="mark">REDACTED</span> |
| 02/28/2012 | 2.1                  | Technical Review and Edits                                  | <span class="mark">REDACTED</span> |
| 03/04/2012 | 2.1                  | Final Review prior to Submission                            | <span class="mark">REDACTED</span> |
| 05/08/2012 | 2.2                  | Technical Review and Update                                 | <span class="mark">REDACTED</span> |
| 05/09/2012 | 2.2                  | Review                                                      | <span class="mark">REDACTED</span> |
| 05/17/2012 | 2.2                  | Final Review prior to submission                            | <span class="mark">REDACTED</span> |
| 06/20/2012 | 2.3                  | Technical Review and Update                                 | <span class="mark">REDACTED</span> |
| 06/20/2012 | 2.3                  | Review                                                      | <span class="mark">REDACTED</span> |
| 06/20/2012 | 2.3                  | Final Review prior to submission                            | <span class="mark">REDACTED</span> |
| 09/07/2012 | 2.4                  | Review &edits                                               | <span class="mark">REDACTED</span> |
| 09/07/2012 | 2.4                  | Final review prior to submission                            | <span class="mark">REDACTED</span> |
| 10/14/2012 | 2.5                  | Updated links within document                               | <span class="mark">REDACTED</span> |
| 10/23/2012 | 2.6                  | Made updates (incorporated edits from (T.S.)                | <span class="mark">REDACTED</span> |
| 11/29/2012 | 2.7                  | Updated footer                                              | <span class="mark">REDACTED</span> |
| 11/30/2012 | 2.7                  | Final review prior to submission                            | <span class="mark">REDACTED</span> |
| 01/03/2013 | 2.8                  | Technical edits were made                                   | <span class="mark">REDACTED</span> |
| 01/03/2013 | 2.8                  | Reviewed prior to submission                                | <span class="mark">REDACTED</span> |
| 1/10/13    | 2.9                  | Edited file to reflect changes from a patch to a host file. | <span class="mark">REDACTED</span> |
| 1/14/2013  | 3.0                  | Incorporate Product Support Feedback                        | <span class="mark">REDACTED</span> |
| 05/11/2013 | 3.1 | Updated cover page and product description, technical and grammatical review | <span class="mark">REDACTED</span> |
|------------|-----|------------------------------------------------------------------------------|------------------------------------|
| 05/12/2013 | 3.1 | Final review prior to submission                                             | <span class="mark">REDACTED</span> |
| 06/13/2013 | 3.2 | Update to Section 5.4 to reflect Secondary or Null for bed configs           | <span class="mark">REDACTED</span> |
| 6/20/2013  | 3.2 | Technical and grammatical review. Update of TOC and footers                  | <span class="mark">REDACTED</span> |
| 7/17/2013  | 3.3 | Update to remove zip reference and to HWS                                    | ProdDev                            |
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/002.png)[PRODUCT DESCRIPTION 1](#product-description)
[1.1. Recommended Audience 1](#recommended-audience)
2.  [About this Guide 1](#about-this-guide)
3.  [Document Conventions 1](#document-conventions)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/003.png)[REFERENCED DOCUMENTS 1](#referenced-documents)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/004.png)[BEFORE BEGINNING THE UPDATE 2](#before-beginning-the-update)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/005.png)[Retrieve patch EDP\*2\*6 2](#retrieve-patch-edp26)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/006.png)[VistA Download Site download.vista.med.va.gov anonymous.software Check VistA Software Requirements 3](#vista-download-site-download.vista.med.va.gov-anonymous.software-check-vista-software-requirements)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/007.png)[Check the 230-234 Number Space 3](#check-the-230-234-number-space)
1.  [Place and Protect New Globals 3](#place-and-protect-new-globals)
2.  [Namespace and Number Space 3](#namespace-and-number-space)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/008.png)[INSTALLING M SERVER COMPONENTS 4](#installing-m-server-components)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/009.png)[Install patch EDP\*2\*6 4](#install-patch-edp26)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/010.png)[Edit the EDPF LOCATION Parameter 5](#edit-the-edpf-location-parameter)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/011.png)[Edit the EDPF NURSE STAFF SCREEN Parameter 5](#edit-the-edpf-nurse-staff-screen-parameter)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/012.png)[Install and Configure VistALink for EDIS 6](#install-and-configure-vistalink-for-edis)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/013.png)[POST INSTALLATION 6](#post-installation)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/014.png)[Rebuild Menus 6](#rebuild-menus)
1.  [Assign Menu Options 7](#assign-menu-options)
2.  [Rebuild Menu Trees 7](#rebuild-menu-trees)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/015.png)[Assign Options for Emergency Department Users 8](#assign-options-for-emergency-department-users)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/016.png)[Assign Keys for EDIS Users 10](#assign-keys-for-edis-users)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/017.png)[Fixing the Primary/Secondary Status of a Bed 10](#fixing-the-primarysecondary-status-of-a-bed)
> [5.4.1. Re-Index Files 230 & 231.8 11](#re-index-files-230-231.8)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/018.png)[CONFIGURE EDIS TO WORK WITH OTHER APPLICATIONS 11](#configure-edis-to-work-with-other-applications)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/019.png)[Configure EDIS to Work with Omnicell 11](#configure-edis-to-work-with-omnicell)
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/020.png)[ACRONYMS 13](#acronyms)
List of Tables
[TABLE 1: TYPES OF DOCUMENTATION 2](#_bookmark0)
[TABLE 2: GLOBAL FILES 3](#_bookmark1)

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/021.png)Product Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fundamental mission of Department of Veterans Affairs (VA), Office of Information & Technology (OI&T), Emergency Department Integration Software (EDIS) Program Services is to provide Veterans the benefits they have earned throughout their military service to the United States. OI&T accomplishes its mission by delivering high-quality, client-centered, effective and efficient Information Technology (IT) services to those responsible for providing care to the Veterans at the point-of-care as well as throughout all the points of the Veterans’ health care in an effective, timely and compassionate manner. VA depends on Information Management/Information Technology (IM/IT) systems to meet mission goals.

> The VHA Health Workflow System (HWS). (HWS) Initiative is a single initiative whose mission is to expand health care access for Veterans, including women and rural populations. Multiple programs and projects have been assigned as part of the HWS Initiative, including EDIS.

> The system is an extension to Veterans Health Information Systems and Technology Architecture / Computerized Patient Record System (VistA/CPRS) for tracking and managing the delivery of care to patients in an Emergency Department (ED). The system provides - Recording and tracking Emergency Department patients during incidents of care - Display of the current state of care delivery - Reports and data extracts on the delivery of care. The system can be configured to specifics of different Veterans Health Administration (VHA) Emergency Departments.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) information resource management (IRM) staff to facilitate the ability to install and configure their systems to run EDIS.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This installation provides instructions for installing application components that run on M servers at VAMC facilities. It also provides instructions for performing post-installation tasks— including configuration tasks—that require knowledge of the underlying VistA system.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bold type indicates application elements (views, panes, links, buttons, prompts, and text boxes, for example) and keyboard key names.

- Keyboard key names appear in angle brackets \< \>.
- *Italicized* text indicates special emphasis or user responses.
- ALL CAPS indicates M routines, parameters, and option names.
- Dot-dash-dot boarders indicate excerpted text (from other documents or from applications).

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/022.png)Referenced Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following documents are available on the VistA Documentation Library (VDL), which is located at [<u>http://www.va.gov/vdl/application.asp?appid=179</u>](http://www.va.gov/vdl/application.asp?appid=179) :

- EDIS Client Installation Guide
- EDIS Server Installation Guide
- IRM Big Board Installation Guide
- EDIS User Manual
- EDIS Glossary
- EDIS Technical Manual

> From the ANONYMOUS software directories:

> OIFO FTP Address Directory

- <span class="mark">REDACTED</span>

> Table 1: Types of Documentation

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Title</strong></th>
<th><strong>File Name</strong></th>
<th><strong>FTP Mode</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDP_2_1_1_SrvrIG.PDF</td>
<td><p>Emergency Department Integration Software Version</p>
<p>2.1.1 Server Installation Guide</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_TM.PDF</td>
<td><p>Emergency Department Integration Software Version</p>
<p>2.1.1 Technical Manual</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDP_2_1_1_UM.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 User Manual</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_ClientIG.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 Client Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDP_2_1_1_BigBoardIG.PD</td>
<td>Emergency Department Integration Software Version2.1.1 IRM Big Board Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_Glossary.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 Glossary</td>
<td>Binary</td>
</tr>
</tbody>
</table>

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/023.png)Before Beginning the Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/024.png)Retrieve patch EDP\*2\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The EDP .ear file for the Graphical User Interface will show a version

> of 2.1.1, while patch 6 for VistA will show a version of 2.0. This is okay and should not be a reason for concern. The application guides will appear with version 2.1.1

> Patch 6 (EDP\*2\*6) is a FORUM patch and will be pushed to the IRM’s by product support. Once you have been notified that the patch has been pushed, you can retrieve and extract the patch from Mail Manager.

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/025.png)VistA Download Site download.vista.med.va.gov anonymous.software Check VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses the following packages, which must be installed and fully patched in your accounts:

- CPRS 26 (OR\*3.0\*215) or greater
- VistALink 1.6 or greater
- Kernel Patch XU\*8.0\*451
- EDP 1.0

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/026.png)Check the 230-234 Number Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site has local files that are stored in the EDIS number space (230-234), remove the files

> *before* you install EDIS. Do this in your site’s test and production VistA accounts.

### Place and Protect New Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EDIS KIDS (Kernel Installation and Distribution System) build creates files in the following globals:

> <span id="_bookmark1" class="anchor"></span>Table 2: Global Files

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Placement</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Journal</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Protection</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDP</p>
</blockquote></td>
<td><blockquote>
<p>Dynamic</p>
</blockquote></td>
<td><blockquote>
<p>This global will grow at a yearly rate of about 2000 bytes multiplied by the number of emergency visits per year. For example, 12,000 emergency visits per year will increase the global yearly by about 24 MB</p>
</blockquote></td>
<td><blockquote>
<p>Place the EDP global in a volume set that is large enough to accommodate this kind of growth</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>RWP or D</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDPB</p>
</blockquote></td>
<td><blockquote>
<p>Static</p>
</blockquote></td>
<td><blockquote>
<p>This global should remain fairly small—its size is currently about 50K</p>
</blockquote></td>
<td><blockquote>
<p>Place the EDPB global as desired</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>RWP or D</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Namespace and Number Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The namespace for EDIS is *EDP*. The number space is *230-234*.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/027.png)Installing M Server Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/028.png)Install patch EDP\*2\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow these instructions to install EDIS patch 6. Installation time is less than one minute.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch \#(ex.EDP\*2.0\*6):
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install (EDP\*2\*6).
5.  You may receive a prompt to overwrite a few files. In the event you receive this prompt, answer YES. The list of possible file names is below:

> TRACKING STAFF (#231.7)

> EDP REPORT TEMPLATE (#232.1) EDP REPORT ELEMENTS (#232.11) CPE ROLE (#232.5)

> EDP WORKSHEET SPECIFICATION (#232.6) EDP WORKSHEET SECTION (#232.71)

> EDP WORKSHEET COMPONENT (#232.72)

> EDP WORKSHEET COMPONENT TYPE (#232.73) EDP COMPONENT VALIDATORS (#232.74)

6.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer ‘NO’
7.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer ‘NO’.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// , answer ‘NO’.
9.  If prompted “Delay Install (Minutes): (0 – 60): 0// respond 0.

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/029.png)Edit the EDPF LOCATION Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter should contain the hospital location or locations that your emergency department uses. If you have a multi-division site, make an entry for each division.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools Option prompt, type *ep* (for Edit Parameters) and then press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf l* (for EDPF LOCATION)*,* and then press the \<Enter\> key.
5.  At the Select INSTITUTION NAME prompt, type the name or station number of your institution and then press the \<Enter\> key.
6.  At the Select Time Range (ex. 0800-1200) or Sequence prompt, type the time range during which the clinic location you are about to select functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department from 8:00 a.m. to 5:00 p.m., type *0800-1700*. Alternately, type a number that represents the location’s preference rating (the number *1* represents the most-preferred location). Press the \<Enter\> key. When users create a PCE encounter, EDIS uses time-of- day-based or preference-based criteria to determine the encounter’s location.

> Note: When selecting time ranges, be sure to account for all hours of emergency-department operation. EDIS does not create PCE encounters for patients whom users enter during times that you do not include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE encounter for the patient.

> Further, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE encounter for the first clinic.

> EDIS uses the time and preference settings you specify here to populate its Clinic list when you select the Show clinics on entry form check box in the application’s Configure view. This parameter allows users at sites that have multiple emergency-department locations to select the location EDIS will use when it creates the patient’s emergency-department visit in CPRS.

> VistA displays your new time range or selection as a default value. Press the \<Enter\> key to accept this default value.

> At the ED LOCATION prompt, type the name of the location that serves as your site’s emergency department during this time range or for this sequence and press the \<Enter\> key. Repeat steps 6 through 8 for additional emergency-department locations (if any).

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/030.png)Edit the EDPF NURSE STAFF SCREEN Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EDPF NURSE STAFF SCREEN parameter allows you to select the type of filtering EDIS uses to populate the nursing-staff selection list in its Assign Staff view. By default, the application allows all entries in the New Person (#200) file. Options for narrowing the list of possible staff selections include:

- Allow only persons who are present and active in the NURS STAFF file (#210)
- Allow only persons who hold the ORELSE key
- Allow only persons who hold the PSJ RNURSE key
- Allow selection from all entries in the New Person file (#200)
1.  Log in to VistA
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select OPTION NAME prompt, type *xpar edit parameter* and press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf nurse staff* and press the \<Enter\> key.
5.  At the Enter selection prompt, type the number *3* (for Division) and press the \<Enter\> key. If your site has only one division, you can set this parameter at the system level by typing the number *5* (for System).
6.  At the Select INSTITUTION NAME prompt, type your institution’s name and then press the \<Enter\> key. VistA displays a list of criteria that EDIS can use to filter entries in the New Person (#200) file.
7.  At the Allow Persons prompt, type one of the following numbers to select a screening criterion and then press the \<Enter\> key:

#### *0* (Active in NURS STAFF (210)

1.  *1* (Hold ORELSE Key)

#### *2* (Hold PSJ RNURSE Key)

2.  *3* (All Persons (No Screen))

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/031.png)Install and Configure VistALink for EDIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Check the Status of Your Site’s VistALink Listener.
2.  Send VistALink Connector Information to the National Server EDIS Administrators or Support Staff.
3.  The next step is to send the following information to the EDIS administrator. VA Policy: You must send this information securely via public key infrastructure (PKI). Securely send this information for both the VistALink connector on your test VistA system and the VistALink connector on your production VistA system.
    1.  The IP name for your site’s VistA server (i.e. ecp.vista.med.va.gov)
    2.  The IP address and port number of your site’s VistALink listener (i.e.

#### 10.10.10.10:18123)

3.  The access code for the VistALink connector (i.e. 1234abc)
4.  The verify code for the VistALink connector (i.e. 5678abc!)

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/032.png)Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/033.png)Rebuild Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The KIDS installation process does not rebuild VistA menu trees *before* you assign new EDIS menus. You must therefore perform a menu rebuild *after* you assign these menus *for the first time*. If you do not, graphical user interface (GUI) applications like EDIS won’t know who has access to the new options. Again, performing a menu rebuild is necessary only once for menus that have never before been assigned.

> The EDIS project team recommends that you assign the EDPF TRACKING MENU ALL option to the CAC or ED coordinator—which includes all EDIS menus—and then manually rebuild VistA menu trees.

### Assign Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type *user* (for User Management) and press the \<Enter\> key.
5.  At the Select User Management Option prompt, types *edit* (for Edit an Existing User) and press the \<Enter\> key.
6.  At the Select NEW PERSON NAME prompt, type your (or another user’s) name using the following format: lastname, firstname. Press the \<Enter\> key.
7.  Press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark (*?*) to see a list of the secondary options that are currently assigned to you.)
8.  In the Select SECONDARY MENU OPTIONS field, type *EDPF TRACKING MENU ALL* and then press the \<Enter\> key.
9.  At the Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No// prompt, type *Yes* and press the \<Enter\> key.
10. Press the \<Enter\> key again to accept this new option. In the SYNONYM field, type a synonym for the option (optional). Press the \<Enter\> key.
11. Press the \<Enter\> key to close the COMMAND field and return to the Select SECONDARY MENU OPTIONS field.
12. Type the word *exit* in the COMMAND field.
13. At the Save changes before leaving form (Y/N)? Prompt, type the letter *Y* and press the

> \<Enter\> key.

### Rebuild Menu Trees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

14. Log in to VistA.
15. At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
16. At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and press the \<Enter\> key.
17. At the Select Systems Manager Menu Option prompt, type the word *menu* (for Menu Management) and press the \<Enter\> key.
18. At the Select Menu Management Option prompt, type the word *menu* (for Menu Rebuild Menu) and press the \<Enter\> key.
19. At the Select Menu Rebuild Menu Option prompt, type the word *build* (for Build Primary Menu Trees) and press the \<Enter\> key.
20. At the Do you wish to verify each primary menu? NO// prompt, press the \<Enter\> key to accept the default selection.
21. At the Would you like to build secondary menu trees too? YES// prompt, press the

> \<Enter\> key to accept the default selection.

> Note: If you type NO in response to this question, VistA will remove access to all EDIS options for all users.

22. At the Would you like to queue this job? YES// prompt, press the \<Enter\> key to accept the default selection. If you want to run the job immediately, type *NO,* and then press the \<Enter\> key. If you choose the latter option, be advised that running a menu rebuild can take time.
23. At the Requested Start Time: NOW// prompt, press the \<Enter\> key to accept the default selection.
24. After the system runs the menu rebuild, remove the menu options you don’t need.

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/034.png)Assign Options for Emergency Department Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You must assign to users and clinical application coordinators (CACs) at least one of the following secondary menu options. These options provide rudimentary capabilities for limiting application access based on user roles. The EDIS project team recommends working with your site’s emergency-department administrative and IT staff to determine which users should receive which menu options.

- EDIS HOME PAGE with all buttons active provides access to:

#### CPE

1.  Configure
2.  Edit Closed
3.  Assign Staff
4.  Reports
5.  Display Board
- EDPF TRACKING MENU CLINICIAN: provides access to the CPE views—it includes the ability to remove patients from the board and provides access to the following data- entry fields:

#### Room/Area

1.  Status
2.  Provider, Resident, and Nurse staff-assignment lists
3.  Comments
4.  Disposition
5.  Delay Reason (if the Delay reason is required…parameter is enabled)
6.  Diagnosis
- EDPF TRACKING VIEW CONFIGURE: provides access to the Configure view—which includes the ability to configure rooms and areas, colors, one or multiple display boards, site-configurable parameters, and the contents of application pick lists
- EDPF TRACKING VIEW EDIT CLOSED: provides access to the Edit Closed view, which includes the ability to edit all data-entry fields for closed visits; the EDIS project team recommends limiting access to this view
- EDPF TRACKING VIEW REPORTS: provides access to the Reports view, which includes the ability to run administrative reports; separate keys control user access to export and print privileges, and to limited-access reports (See Section 5.3, “[<u>Assign Keys for EDIS</u> <u>Users</u>](#_bookmark2)”)
- EDPF TRACKING VIEW STAFF: provides access to the Assign Staff view—it offers the ability to update physician-, resident-, and nursing-staff pick lists

> To reiterate: work with your site’s IT Staff and emergency-department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views he or she needs.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt type EVE and then press the

> \<Enter\> key.

3.  From the Choose 1-5 prompt, type the number 1 (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  From the Select Systems Manager Menu Option prompt, type User Management and press the \<Enter\> key.
5.  From the Select User Management Option prompt , types edit (for Edit an Existing User) and press the \<Enter\> key.
6.  From the Select NEW PERSON NAME prompt, type the user’s name using the following format: lastname, firstname. Press the \<Enter\> key.
7.  Press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark (?) to see a list of the secondary options that are currently assigned to the user.)
8.  In the SECONDARY MENU OPTIONS field, type one of the options listed above and then press the \<Enter\> key.
9.  From the Are you adding …as a new SECONDARY MENU OPTIONS

> (the…for this NEW PERSON)? No// prompt, type Yes and press the

> \<Enter\> key.

10. Press the \<Enter\> key again to accept this new option.
11. In the SYNONYM field, type a synonym for the option (optional). Press the

> \<Enter\> key.

12. Press the \<Enter\> key to close the COMMAND field and return to the Select SECONDARY MENU OPTIONS field.
13. Repeat steps 6 through 12 to assign other options as necessary.
14. Press the \<Down Arrow\> key to move through the Edit Existing User dialog. At the end of each page, type the letter n in the COMMAND field to enter the following page.
15. Stop on page 3.
16. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active. Note: The active person class is only needed for the Providers.
17. If the user’s person class is not active, select an active person class for the user.
18. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
19. From the Save changes before leaving form (Y/N)? prompt, type the letter Y

> and press the \<Enter\> key.

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/035.png)Assign Keys for EDIS Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign keys for users who need access to additional reporting capabilities. The following keys are available:

- EDPR EXPORT enables the export option for EDIS reports
- EDPR PROVIDER allows users to access to the Provider report, which lists statistics for each emergency department provider
- EDPR XREF provides access to the Patient XRef (cross reference) report, which associates patients’ emergency department visit numbers with their patient IDs
  1.  Log in to VistA
  2.  At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
  3.  At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and then press the \<Enter\> key.
  4.  At the Select Systems Manager Menu Option prompt, type *menu* (for Menu Management) and then press the \<Enter\> key.
  5.  At the Select Menu Management Option prompt, type the word *key* (for Key Management) and then press the \<Enter\> key. .
  6.  At the Select Key Management Option prompt, type the word *allocation* (for

> Allocation of Security Keys). Press the \<Enter\> key.

7.  At the Allocate key prompt, type the name of the security key you want to assign—*EDPF EXPORT*, for example. Press the \<Enter\> key.
8.  At the Holder of key prompt, type the name of the first user to whom you are assigning the key and then press the \<Enter\> key.
9.  At the Another holder prompt, type the name of a second user to whom you are assigning the key and then press the \<Enter\> key. Repeat this step for all users to whom you are assigning the key.
10. At the You are allocating keys. Do you wish to proceed? YES// prompt, press the \<Enter\> key to accept the default response.

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/036.png)Fixing the Primary/Secondary Status of a Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During testing, a problem with the Primary/Secondary status of beds at some facilities was identified. This creates problems with beds being released when a patient is discharged. In order to ensure that all beds are set to ‘Primary’, follow these steps.

> In file Manager:

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: TRACKING ROOM-BED \<-- choose the TRACKING ROOM/BED

> file (#231.8)

> EDIT WHICH FIELD: ALL// .13 PRIMARY \<-- choose field .13 (Primary) THEN EDIT FIELD:

> Select TRACKING ROOM-BED NAME: BWF-TEST-1 \<--- enter the name of the bed PRIMARY: P Primary \<--- choose 'P' for primary (only if bed is set to Secondary or is Null)

> Repeat above steps for any beds that are listed as 'Secondary' or Null.

### Re-Index Files 230 & 231.8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Re-index ALL indices on files 230 and 231.8. It is suggested that this be done during non-peak hours to limit performance impact for users.

> VA FileMan 22.0

> Select OPTION: UTILITY FUNCTIONS Select UTILITY OPTION: RE-INDEX FILE

> MODIFY WHAT FILE: TRACKING ROOM-BED// 230 ED LOG (example) THERE ARE 23 INDICES WITHIN THIS FILE

> DO YOU WISH TO RE-CROSS-REFERENCE ONE PARTICULAR INDEX? No// (No)

> OK, ARE YOU SURE YOU WANT TO KILL OFF THE EXISTING 23 INDICES? No// Y (Yes) DO YOU THEN WANT TO 'RE-CROSS-REFERENCE'? Yes// (Yes)

> ...EXCUSE ME, JUST A MOMENT PLEASE...

> FILE WILL NOW BE 'RE-CROSS-REFERENCED'......

> VA FileMan 22.0

> Select OPTION: UTILITY FUNCTIONS Select UTILITY OPTION: RE-INDEX FILE

> MODIFY WHAT FILE: ED LOG// 231.8 TRACKING ROOM-BED (example) THERE ARE 3 INDICES WITHIN THIS FILE

> DO YOU WISH TO RE-CROSS-REFERENCE ONE PARTICULAR INDEX? No// (No)

> OK, ARE YOU SURE YOU WANT TO KILL OFF THE EXISTING 3 INDICES? No// Y (Yes) DO YOU THEN WANT TO 'RE-CROSS-REFERENCE'? Yes// (Yes)

> ...HMMM, THIS MAY TAKE A FEW MOMENTS...

> FILE WILL NOW BE 'RE-CROSS-REFERENCED'....

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/037.png)Configure EDIS to work with other Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/038.png)Configure EDIS to Work with Omnicell

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site wants EDIS to work with its Omnicell implementation, you must manually add the Omnicell event protocol (VEFS SDAM) to the EDIS EDP NEW PATIENT event. If you are already running EDIS Version 1.0, please review the below configuration to be certain nothing has changed.

1.  Open VA FileMan.
2.  At the Select OPTION prompt, type the number *1* (ENTER OR EDIT FILE ENTRIES).
3.  At the INPUT TO WHAT FILE prompt, type the word *protocol* (PROTOCOL).
4.  At the EDIT WHICH FIELD prompt, type the word *item.*
5.  At the CHOOSE 1–2 prompt, type the number *1* (ITEM (multiple)).
6.  At the EDIT WHICH ITEM SUB-FIELD prompt, press the \<Enter\> key to accept the default response (ALL). \\
7.  At the THEN EDIT FIELD prompt, press the \<Enter\> key without typing a response.
8.  At the Select PROTOCOL NAME prompt, type *EDP NEW PATIENT*.
9.  At the Select ITEM prompt, type *VEFS SDAM* (the Omnicell event protocol). You don’t need to respond to prompts for other fields in the ITEM multiple.

# ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-server-instal/039.png)Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AMS</p>
</blockquote></td>
<td><blockquote>
<p>Medical Automation Systems</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CACs</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Application Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPE</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Practice Environment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient System Records</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ED</p>
</blockquote></td>
<td><blockquote>
<p>Emergency Department</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EDIS</p>
</blockquote></td>
<td><blockquote>
<p>Emergency Department Integration Software</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EDP</p>
</blockquote></td>
<td><blockquote>
<p>Namespace for EDIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ER</p>
</blockquote></td>
<td><blockquote>
<p>Emergency Room</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVE</p>
</blockquote></td>
<td><blockquote>
<p>Client Server Program – Systems Manager</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphical User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GPO</p>
</blockquote></td>
<td><blockquote>
<p>Group Policy Objects</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GTS</p>
</blockquote></td>
<td><blockquote>
<p>Generic Traffic Shaping</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Internet Explorer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>Internet Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resource Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAWS</p>
</blockquote></td>
<td><blockquote>
<p>Job Access with Speech</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KIDS</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Installation and Distribution System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LCD</p>
</blockquote></td>
<td><blockquote>
<p>Liquid Crystal Display</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NSR</p>
</blockquote></td>
<td><blockquote>
<p>National Service Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PKI</p>
</blockquote></td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POC</p>
</blockquote></td>
<td><blockquote>
<p>Point-of-Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RAM</p>
</blockquote></td>
<td><blockquote>
<p>Random Access Memory</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RALS</p>
</blockquote></td>
<td><blockquote>
<p>Point of Care IT Connectivity System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SSL</p>
</blockquote></td>
<td><blockquote>
<p>Secure Sockets Layer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAMC</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Affairs Medical Center</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Services Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VDL</p>
</blockquote></td>
<td><blockquote>
<p>VistA Documentation Library</p>
</blockquote></td>
</tr>
</tbody>
</table>