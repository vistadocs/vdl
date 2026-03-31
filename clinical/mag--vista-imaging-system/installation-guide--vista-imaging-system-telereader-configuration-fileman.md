---
title: VistA Imaging System TeleReader Configuration (FileMan)
doc_type: IG
doc_label: Installation Guide
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
  - telereader
  - table
  - contents
  - site
  - report
  - acquisition
  - unread
  - reader
  - index
  - reading
page_count: 0
word_count: 1570
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_TELEREADER_CONFIGURATION.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_TELEREADER_CONFIGURATION.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-system-telereader-configuration-fileman/001.png)

TeleReader Configuration

> VistA Imaging

> MAG\*3.0\*127

June 2013

![](vista-imaging-system-telereader-configuration-fileman/002.png)

> VistA Imaging Software Design & Development

> Patch 127 TeleReader Configuration June 2013

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

> Revision Table

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Rev</strong></th>
<th><strong>Date</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.1</td>
<td>June 2013</td>
<td>Corrected file names on pp. 4 and 6. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2.0</td>
<td>May 2013</td>
<td>Edited to correct Remedy ticket 375083 and notation format for field and file names. Changed title of manual from TeleOpthamology TeleReader Configuration to TeleReader Configuration. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1.1</td>
<td>Apr 11 2012</td>
<td><ol type="1">
<li><p>Made corrections to filename/number (per Bug report #37069), pages3 and 14.</p></li>
<li><p>Corrected instances of incorrect file name/number conventions (used FILENAME file (#nnnn.nn) convention)</p></li>
<li><p>Changed font to <strong>bold</strong> for user entry/response dialogs throughout.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>1.0</td>
<td>Mar 17 2007</td>
<td>Packaged for release with Patch 46.</td>
</tr>
<tr class="odd">
<td>.9</td>
<td>Jan 18 2007</td>
<td>Initial draft.</td>
</tr>
</tbody>
</table>

> Contents

> This page is intentionally blank.

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
    - [Terms of Use](#terms-of-use)
- [VistA Imaging Configuration for TeleReader](#vista-imaging-configuration-for-telereader)
    - [Defining the Unread Lists at the Acquisition Site](#defining-the-unread-lists-at-the-acquisition-site)
    - [Configuring the DICOM HEALTHCARE PROVIDER SERVICE file for TeleRetinal Imaging](#configuring-the-dicom-healthcare-provider-service-file-for-teleretinal-imaging)
  - [Configuring TeleReader at the Reading Site](#configuring-telereader-at-the-reading-site)
    - [Defining the Reading Site’s List of Acquisition Sites](#defining-the-reading-sites-list-of-acquisition-sites)
    - [Defining the Diagnostic Readers](#defining-the-diagnostic-readers)
  - [Configuring TeleReader at Acquisition Sites and Reading Sites](#configuring-telereader-at-acquisition-sites-and-reading-sites)
  - [Configuring TeleReader Application Timeout](#configuring-telereader-application-timeout)
- [TeleReader Reports](#telereader-reports)
  - [Generating TeleReader Reports](#generating-telereader-reports)
    - [Accessing the Reports Menu](#accessing-the-reports-menu)
    - [TeleReader Status Report](#telereader-status-report)
    - [TeleReader Reader Activity Report](#telereader-reader-activity-report)
    - [TeleReader Reader Time Report](#telereader-reader-time-report)
    - [TeleReader Setup Report](#telereader-setup-report)
    - [Report Telereader Read/Unread List Problems Report](#report-telereader-readunread-list-problems-report)
    - [Repair Telereader Read/Unread List Problems Option](#repair-telereader-readunread-list-problems-option)
> This document explains how to configure the TeleReader application.
> This describes the configuration at both Acquisition Sites and Reading Sites and describes menu option reports that can be run to assist in the configuration.
> This document is meant for site administrators to assist in configuring the TeleReader. This document does not contain information for users of the TeleReader.
> <span id="_bookmark1" class="anchor"></span>Additional information about Telehealth can be found on the VHA Telehealth Services website at [<span class="mark">REDACTED</span>.](http://vaww.telehealth.va.gov/index.asp)

### Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FDA regulations require that each Imaging software distribution is documented and tracked by the VistA Imaging project.
> This page is intentionally blank.

# VistA Imaging Configuration for TeleReader 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At present, the TeleReader application is approved for Diabetic Retinopathy Surveillance, although its design is generic and can be configured to handle many imaging consults.

> TeleReader can be used to facilitate reading of both local and remote consults (that is, Inter-facility Consults).

> The TeleReader works in conjunction with the Consult Request Tracking package (GMRC) to enable a reader to obtain a list of imaging studies that are ready to be diagnosed. Configuration work is required at both the Acquisition Site and the Reading Site. First, at the Acquisition Site, the TELEREADER ACQUISITION SERVICE file (#2006.5841) is defined and the DICOM HEALTHCARE PROVIDER SERVICE file (#2006.5831) is updated for the consult. Second, at the Reading Site, lists of Acquisition Sites and Reader Privileges are established in the TELEREADER ACQUISTION SITE file (#2006.5842) and TELEREADER READER file (#2006.5843). These configuration steps enable the TeleReader application to use the Unread List to direct the reader to imaging studies that are awaiting diagnosis.

> The Unread List (TELEREADER READ/UNREAD LIST file \[#2006.5849\]) is

> maintained at the Acquisition Site and is accessed by a local or a remote reader. Selecting a study off the Unread List automatically switches patient context for the Computerized Patient Record System (CPRS) and Clinical Viewer, making it quicker for the reader to find, diagnose, and result the study. After the images are diagnosed, the entry in this file contains information about the reading session, which can be displayed with the TeleReader application.

> Note: When you have completed your configuration for the TeleReader you can run the [<u>TeleReader Setup Report</u>](#telereader-setup-report) to review your configuration and ensure everything is configured properly.

> <span id="Configuring_TeleReader_at_the_Acquisitio" class="anchor"></span>Configuring TeleReader at the Acquisition Site

> Two steps are required to configure the TeleReader at the Acquisition Site. The primary step is to define the Acquisition Site’s Unread List(s) by configuring the TELEREADER ACQUISITION SERVICE file (#2006.5841). It is also necessary to configure the DICOM HEALTHCARE PROVIDER SERVICE file (#2006.5831) for TeleRetinal

> Imaging. These two steps must be completed before images can be acquired or studies will not appear on TeleReader at the reading site.

### Defining the Unread Lists at the Acquisition Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each Unread List that is defined at the Acquisition Site requires an entry in the TELEREADER ACQUISITION SERVICE file (#2006.5841). This file maps the locally

> defined CPRS Consult Request Tracking “To Service” (and optionally the Procedure) to the nationally defined Specialty (such as Eye Care) and Procedure (such as Diabetic Retinopathy Surveillance) that are used by the Unread List.

> Seven data elements must be specified for each Unread List:

1)  TELEREADER ACQUISITION SERVICE NAME (“To Service”) —this is the locally defined Consult Request Tracking service that performs the request. This is a pointer to the REQUEST SERVICES file (#123.5). This is the consult to which the Imager attaches images. If reading for your studies is done locally, this will be a local consult. If reading for your studies is done remotely, this will be an Inter-Facility consult. The same To Service needs to be configured in the DICOM HEALTHCARE PROVIDER SERVICE file (#2006.5831), as described below.
2)  Procedure—this is optional and is used only if the site wants to map a locally defined Consult Request Tracking procedure to the Unread List. This only works for local requests. It is not supported for Inter-facility Consults. This is a pointer to the GMRC PROCEDURE file (#123.3).
3)  Specialty Index—this is a pointer to the nationally defined IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY file (#2005.84), and is used in conjunction with the Procedure Index to provide a common lexicon for the Unread Lists. An example of a specialty index is Eye Care.
4)  Procedure Index—this is a pointer to the nationally defined IMAGE INDEX FOR PROCEDURE/EVENT file (#2005.85), and is used in conjunction with the Specialty Index to provide a common lexicon for the Unread Lists. An example of a procedure index is Diabetic Retinopathy.
5)  Acquisition Site—this is a pointer to the INSTITUTION file (#4). This should be your site being used for acquisition.
6)  Unread List Creation Trigger— this specifies the activity that will place the study on the Unread List. There are three Unread List creation trigger events:
    1.  “I” — when a DICOM image is acquired. This is the recommended setting.
    2.  “O” — when the consult/procedure request is ordered.
    3.  “F” — when the consult/procedure request is forwarded.

> Note: While procedures may be forwarded at local sites, procedures may not be forwarded to a remote site. Only consults may be forwarded to remote sites to become Inter-facility Consults.

7)  TIU Note File – this is used to automatically create a TIU note for a set of images when the consult request is remotely completed via an Inter-facility Consult.

### Configuring the DICOM HEALTHCARE PROVIDER SERVICE file for TeleRetinal Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: You might have already configured this file for TeleRetinal Imaging when you configured your acquisition camera. Verify below you have used the correct REQUESTED SERVICE. This service should be the same service you used as the TELEREADER ACQUISITION SERVICE NAME in the TELEREADER ACQUISITION SERVICE file.

> This DICOM HEALTHCARE PROVIDER SERVICE file (#2006.5831) configures the DICOM Gateway to receive information for services to acquire images.

> For the TeleRetinal process, two consults are used. The first is created by the Primary Care Physician and the second is created by the Imager. Only the second consult, created by the Imager, should be put into this file.

> Three fields must be specified for each consult:

1)  DICOM HEALTHCARE PROVIDER SERVICE REQUESTED SERVICE— this is the consult the imager will be creating and attaching images to. This should be the same consult you selected as the TELEREADER ACQUISITION SERVICE in the TELEREADER ACQUISITION SERVICE file.
2)  SERVICE GROUP—this should be set to EYE CARE for Diabetic Retinopathy.
3)  SERVICE INSTITUTION—this is the division doing the acquisition. This should be the same as the ACQUISITION SITE in the TELEREADER ACQUISITION SERVICE file.

## Configuring TeleReader at the Reading Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Two steps are required to configure the TeleReader at the Reading Site. The first step is to populate the TELEREADER ACQUISITION SITE file (#2006.5842) to establish the Acquisition Sites for which the Reading Site will provide diagnostic services. The second step is to enter the diagnostic readers into the TELEREADER READER file (#2006.5843) and designate their clinical specialties and where they are authorized to provide diagnostic services. Each Acquisition Site must be specified at the Reading Site and each authorized user must be configured to read. This process must be completed even if the Acquisition Site and the Reading Site are the same.

### Defining the Reading Site’s List of Acquisition Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TELEREADER ACQUISITION SITE file (#2006.5842) contains the list of the Acquisition Sites for each Reading Site. This list must also include the Reading Site itself if it is to perform image acquisition as well. This file must be configured before attempting to add users to read for an acquisition site. An entry must be made in this file for each acquisition site your site is reading for.

> Four data elements must be specified in this list:

1)  Acquisition Site—this is a pointer to the INSTITUTION file (#4). This is the site you would like to read for.
2)  Primary Site—this is where the Acquisition Site’s VistA Hospital Information System (HIS) is located. For most facilities, the Primary Site will be at the Acquisition Site. For a Community Based Outpatient Clinic (CBOC), a multidivisional, or a consolidated facility however, this may be a different site. This data element is a pointer to the INSTITUTION file (#4).
3)  Status—a site may be either active or inactive. The status may be changed operationally to enable/disable reading for Acquisition Sites, for example, if a remote VistA HIS or WAN were temporarily down.
4)  Lock Timeout—this value designates how long a user of the TeleReader application can lock a study for reading. If a reader locks a study, but is then called away for clinical duties, the study will be automatically unlocked when the timeout expires.

### Defining the Diagnostic Readers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TELEREADER READER file (#2006.5843) file contains the diagnostic reader information. All users of the TeleReader must be configured in this file. This file must be modified each time a new Acquisition Site is added, so the readers are configured for the new site.

> Eight data elements must be defined:

1)  Reader—this is a pointer to the NEW PERSON file (#200). The reader must have permission to result and complete CPRS Consult Request Tracking requests at the Reading Site.
2)  Acquisition Site—this is a pointer to the INSTITUTION file (#4).
3)  Acquisition Site Status—indicates whether an Acquisition Site for a reader is Active or Inactive.
4)  Specialty Index—this is a pointer to the nationally defined IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY file (#2005.84), and is used in conjunction with the Procedure Index to provide a common lexicon for the Unread Lists.
5)  Specialty Index Status—indicates whether a Specialty Index for a reader is Active or Inactive.
6)  Procedure Index—this is a pointer to the nationally defined IMAGE INDEX FOR PROCEDURE/EVENT file (#2005.85), and is used in conjunction with the Specialty Index to provide a common lexicon for the Unread Lists.
7)  Procedure Index Status—indicates whether a Procedure Index for a reader is Active or Inactive.
8)  User Preference—determines if the reader’s Site/Specialty/Procedure is checked when the Site/Specialty/Procedure dialog is displayed. This value can be changed by the user from the TeleReader application.
9)  To add a new TeleReader reader at the reading site:

## Configuring TeleReader at Acquisition Sites and Reading Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Acquisition sites may also do their own reading using the TeleReader application. In this situation, follow the above instructions for configuring the TeleReader at the Acquisition Site and the Reading site.

## Configuring TeleReader Application Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: After a specified amount of idle time in minutes, the TeleReader application will automatically close. This time value is site configurable.

> This page intentionally left blank.

# TeleReader Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to generate reports on TeleReader usage. The following reports are available:

- TeleReader Status Report—lists the status of each study from the TeleReader read/unread lists.
- TeleReader Reader Activity Report—lists the number of studies read by a reader in a specified date range.
- TeleReader Reader Time Report—lists the reading start time and reading stop time in minutes for each reader in a specified date range.
- TeleReader Setup Report—lists the configuration of the TeleReader and its associated files. This report is useful to verify the configuration for TeleReader and for debugging problems with the TeleReader configuration.
- Report TeleReader Read/Unread List Problems—reports problems in the TeleReader read/unread list for read or locked studies which were resulted (completed) or cancelled by CPRS.

> The following option is also available in the list of reports on the TeleReader menu:

- Repair TeleReader Read/Unread List Problems—fixes problems in the TeleReader read/unread list that were found in the Report TeleReader Read/Unread List Problems option. This ensures the TeleReader is in sync with CPRS.

> Note: The TeleReader Setup Report is only useful if your site does only image reading. The other reports only display information which is stored at the acquisition site.

## Generating TeleReader Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader reports menu is available to users who have access to the Imaging System Manager Menu (MAG SYS MENU).

### Accessing the Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into the VistA System and access the Imaging System Manager Menu.
2.  Enter Telereader Menu at the prompt. The main menu for the TeleReader reports will be displayed.

### TeleReader Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader Status Report prints the status of each study from the TeleReader read/unread lists.

> 1 From the Telereader Menu select the option \[Telereader Status Report\].

### TeleReader Reader Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader Reader Activity Report prints the number of studies read by a reader in a specified date range.

> 1 From the Telereader Menu select the option \[Telereader Reader Activity Report\].

### TeleReader Reader Time Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader Reader Time Report prints the reading start time and reading stop time in minutes for each reader in a specified date range.

> 1 From the Telereader Menu select the option \[Telereader Reader Time Report\].

### TeleReader Setup Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TeleReader Setup Report prints the configuration of the TeleReader and its associated files. This report is useful to verify the configuration for TeleReader and for debugging problems with the TeleReader configuration.

> Note: If your site only does image acquisition, then only the entries from the DICOM HEALTHCARE PROVIDER SERVICE file (#2006.5831) and the TELEREADER

> ACQUISITION SERVICE file (#2006.5841) will be populated. If your site only does image reading, then only the entries from the TELEREADER ACQUISITION SITE file (#2006.5842) and the TELEREADER READER file (#2006.5843) will be populated. If your site does reading and acquisition, then all four of these files will be populated.

> 1 From the Telereader Menu select the option \[Telereader Setup Report\].

> ST TeleReader Status Report

> RA TeleReader Reader Activity Report TI TeleReader Reader Time Report

> BB TeleReader Setup Report

> RP Report Telereader Read/Unread List Problems FP Repair Telereader Read/Unread List Problems

> Select Telereader Menu Option: BB TeleReader Setup Report DEVICE: HOME// TELNET Right Margin: 80//

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\* \*\*\* DICOM HEALTHCARE PROVIDER SERVICE

> (file 2006.5831) \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> To Service: CARDIOLOGY

> Worklist: CARDIO (CARDIOLOGY) acquired at SALT LAKE CITY Clinics: CARDIOLOGY

> To Service: GASTROENTEROLOGY

> Worklist: GI (GASTROENTEROLOGY) acquired at SALT LAKE CITY Clinics: GI CLINIC

> To Service: OPHTHALMOLOGY

> Worklist: OPHTH (OPHTHALMOLOGY) acquired at COLUMBIA, MO Clinics: OPHTHALMOLOGY-BELKIN

> To Service: DIABETIC TELERETINAL IMAGING-WASHINGTON

> Worklist: EYE (EYE CARE) acquired at SALT LAKE CITY Remote IFC: WASHINGTON, DC

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\*

> \*\*\* TELEREADER ACQUISITION SERVICE (file 2006.5841) \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> To Service: DIABETIC TELERETINAL IMAGING-WASHINGTON \*\*\* DICOM MWL Remote IFC: WASHINGTON, DC

> Unread List: EYE CARE -- DIABETIC RETINOPATHY SURVEILLANCE

> Trigger: Create/update with every acquired image Note for IFC: OPHTHALMOLOGIST CONSULT NOTE

> To Service: OPHTHALMOLOGY \*\*\* DICOM MWL Unread List: EYE CARE -- DIABETIC RETINOPATHY SURVEILLANCE

> Trigger: Create/update with every acquired image Note for IFC: OPHTHALMOLOGIST CONSULT NOTE

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\*

> \*\*\* TELEREADER ACQUISITION SITE (file 2006.5842) \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Acquisition: SALT LAKE CITY Active Lock Time: 300 min. Primary Site: SALT LAKE CITY

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\*\*

> \*\*\* TELEREADER READER (file 2006.5843) \*\*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* TeleReader: OPTOMETRY,CLINICIAN

> Acquisition: SALT LAKE CITY Active Unread List: EYE CARE Active

> DIABETIC RETINOPATHY SURVEILLANCE Active User: Active

### Report Telereader Read/Unread List Problems Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Report Telereader Read/Unread List Problems Report lists problems in the TeleReader read/unread list for read or locked studies which were resulted (completed) or cancelled by CPRS.

> 1 From the Telereader Menu select the option \[Report Telereader Read/Unread List Problems\].

### Repair Telereader Read/Unread List Problems Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Repair Telereader Read/Unread List Problems option fixes problems in the TeleReader read/unread list that were found in the Report Telereader Read/Unread List Problems Report. This function ensures the TeleReader is in sync with CPRS.

> 1 From the Telereader Menu select the option \[Repair Telereader Read/Unread List Problems\].