---
title: VistA Scheduling Enhancement (VSE) 622 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: VistA Scheduling Enhancement (VSE) 622
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - clinic
  - appointment
  - letter
  - table
  - contents
  - print
  - scheduling
  - telephone
  - extension
  - documentation
page_count: 0
word_count: 985
section_count: 2
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2014
revision_count: 1
revision_newest: 12/15/2014
revision_oldest: 12/15/2014
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vse_enh4_rn_sd_5_3_622.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vse_enh4_rn_sd_5_3_622.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

---
title: <span id="_Toc205632711" class="anchor"></span>Department of Veterans Affairs
---

VistA Scheduling Enhancement

Release Notes

SD\*5.3\*622

![](vista-scheduling-enhancement-vse-622-release-notes/001.png)

December 2014

*This page intentionally left blank*

Revision History

|            |         |                     |                                    |
|------------|---------|---------------------|------------------------------------|
| Date       | Version | Description         | Author                             |
| 12/15/2014 | 1.0     | Sent for Submission | <span class="mark">REDACTED</span> |

*This page intentionally left blank*

Table of Contents

[4. Upgrades](#upgrades) 1

[5. Known Issues ..](#known-issues)2

[6. Product Documentation](#product-documentation) 2

*This page intentionally left blank*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
  - [This Release](#this-release)
- [Features and Functionality](#features-and-functionality)
- [Upgrades](#upgrades)
- [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide a summary of enhancements and new features to the VistA Scheduling package as implemented in the patch SD\*5.3\*622.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the VistA Scheduling package, version 5.3.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following provide the new features and functions added to the VistA Scheduling package, version 5.3 by the patch SD\*5.3\*622.

- A Clinic inactivation reminder mail message that is sent to the new mail group SD CLINIC INACTIVATE REMINDER on the date that the Clinic is set to go inactive.
- The ability to add Default Provider to the Scheduling letter template in Enter/Edit Letters.
- The ability to add Clinic Location to the Scheduling letter template in Enter/Edit Letters.
- The ability to print the Default Provider on a Scheduling letter sent or given to the Patient.
- The ability to print the Clinic location on a Scheduling letter sent or given to the Patient.
- The ability to add telephone extension to Clinic Set up.
- The ability to display/print telephone extension in Clinic Profile.
- The ability to print the Clinic telephone number and telephone extension number on a Scheduling letter sent or given to the Patient.
- The ability to display the Patient’s Desired Date (current date) when Next Available prompt is answered Yes by the Clerk creating a Patient appointment
- The ability to print the Pre-appointment letter for a patient immediately after creation of the appointment and before leaving the option.
- Ensure correct entry of Desired Date in Expanded Profile (EP),Clinic Wait Time Information, for multiple appointments.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections list the new features and the software components that support the features in the patch SD\*5.3\*622.

- Clinic Inactivation Reminder Mail Message – supported by the option Inactivate a clinic \[SD INACTIVATE\].
- Select whether or not to print the Default Provider and the Clinic Location on a letter by populating or leaving blank the new fields ‘Print Default Provider?’ and ‘Print Clinic Location?’ via the option Enter/Edit Letters \[SDEDLET\]
- Print Default Provider in Pre-Appointment Letter, Clinic Location, Telephone and Telephone Extension – supported by the options Make Appointment \[SDM\]and Print Scheduling Letters \[SDPRLETTERS\]. Additionally and depending on how the Pre-Appointment Letter has been set up, every time a letter is printed after a ‘No Show’ or ‘Cancel Appointment’, the resulting letter will contain the new information above.
- Print the Clinic Telephone number and Telephone Extension number on a Pre-Appointment Letter if the fields are populated when executing the option Set up a Clinic \[SDBUILD\].
- Display the current date (Desired Date) for 3 seconds to the clerk creating an appointment when executing the option Make Appointment \[SDM\],
- Print the Pre-Appointment Letter for a patient when executing the option Make Appointment \[SDM\].
- Display the Desired Date for an appointment when executing the option Expand Entry (EP) in screen \#3 after creation of the appointment when using the Multiple Appointment Booking option
- Display/print the telephne extension on the Clinic Profile option \[SDCLINIC\]
- Corrected the header of the Clinic Profile option \[SDCLINIC\] to display only once per page

# Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the E4 enhancement of a group of enhancements for the VistA Scheduling package. The following components have been modified or added.

- New field \#99.1, TELEPHONE EXTENSION, in the HOSPITAL LOCATION file, \#44.
- New field \#4, PRINT DEFAULT PROVIDER?, in the LETTER file, \#407.5.
- New field \#5, PRINT CLINIC LOCATION?, in the LETTER file, \#407.5.
- New mail group SD CLINIC INACTIVATE REMINDER, in the MAIL GROUP file, \#3.8.
- Modified input template Set Up a Clinic \[SDB\] in the HOSPITAL LOCATION file, \#44, to include the field \#99.1, TELEPHONE EXTENSION.
- Modified the Pre-Appointment Letter to include more comprehensive appointment information that can display the Default Provider, Clinic Location, Telephone Number, and Telephone Extension Number when printing the letter for a Patient.
- Modified the option Make Appointment \[SDM\] to allow the clerk to print the Pre-Appointment Letter for a Patient before leaving the option. The default for printing the letter is No//.
- Modify Clinic Profile option \[SDCLINIC\] to display/print the Telephone Extension.
- Corrected the Clinic Profile option \[SDCLINIC\] to display and print the report header only once per page instead of twice at the top of the page.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues specific to this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

The ADT manuals are posted on the VistA Documentation Library (VDL) page. <http://www4.va.gov/vdl/application.asp?appid=55>.

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to FTP the files from  
<span class="mark">REDACTED</span>

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Documentation can also be found on the VA Software Documentation Library at: <http://www4.va.gov/vdl/>

The following VistA Scheduling user manuals are updated with changes for SD\*5.3\*622.

- Installation Guide for SD\*5.3\*622
- PIMS v5.3 Scheduling Module User Manual Appointment Menu
- PIMS v5.3 Scheduling Module User Manual Scheduling Menu
- VSE E4 System Design Document
- PIMS 5.3 Technical Manual