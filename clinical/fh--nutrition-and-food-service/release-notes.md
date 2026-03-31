---
title: Nutrition & Food Services Version 5.5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: FH
app_name: Nutrition and Food Service
section: CLI
app_status: active
pkg_ns: FH
patch_ver: 5.5
patch_id: FH*5.5
group_key: "FH:FH:5.5"
file_numbers: []
security_keys: []
menu_options: 12
description: Version 5.5February 2005Department of Veterans AffairsVistA Health System Design & Development
audience: 
keywords: 
  - meals
  - outpatient
  - table
  - nutrition
  - contents
  - meal
  - class
  - food
  - special
  - allows
page_count: 0
word_count: 1066
section_count: 2
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 02/24/2005
revision_oldest: 02/24/2005
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

![](nutrition-food-services-version-5-5-release-notes/001.png)

*Nutrition and Food ServiceOutpatient MealsRelease Notes*

![](nutrition-food-services-version-5-5-release-notes/002.png)

*Version 5.5February 2005Department of Veterans AffairsVistA Health System Design & Development*

Revision History

| Date   | Description            |
|------------|----------------------------|
| 02/24/2005 | Revised as per EVS review. |

Table of Contents

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
- [Required Patches](#required-patches)
  - [Software Retrieval](#software-retrieval)
- [Nutrition and Food Service Outpatient Meals](#nutrition-and-food-service-outpatient-meals)
- [File Changes](#file-changes)
- [New Menus and Options](#new-menus-and-options)
The Nutrition & Food Service (N&FS) Outpatient Meals Version 5.5 software combines the existing inpatient functionality in the Dietetics V. 5.0 software with an additional module that provides the capability of entering, tracking, and reporting outpatient meals.
- Provides electronic order entry of meals to authorized outpatients when they are kept over mealtimes.
- Enables electronic order entry of meals for other authorized users such as residents, without compensation employees and volunteers.
- Facilitates and tracks the number of meals for each Enhanced Sharing Agreement (selling of meal services), such as the Salvation Army or a Meals-on Wheels program.
- Provides tracking, reporting and projection features currently for Inpatients that will also include Outpatients.
- Provides the ability to request, authorize, print, cancel, and view status of Outpatient Special Meals.
- Provides the ability to request and print Guest Meals.
- Provides the ability to request Recurring Meals for a regularly scheduled outpatient including a patient profile, meal status, early/late trays, tube feeding, and additional orders.
- Creates new reports and modifications of some existing Nutrition options to include Outpatient data.

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch (v) FH\*5\*41 must be installed before \`Nutrition and Food Service v.5.5.

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Nutrition and Food Service V. 5.5 build (FH5_5.KID, ASCII format) and documentation can be retrieved from the \[ANONYMOUS.SOFTWARE\] directory at the sites listed below. The preferred method is to "FTP" the files from the "download.vista.med.va.gov" location. This location will automatically connect and allow the download process to execute from the first available FTP server to the appropriate directory on your system.

|                                    |                                    |
|------------------------------------|------------------------------------|
| OI Field Office                | FTP Address                    |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The documentation files for Nutrition and Food Service V. 5.5 can also be found on the same OI Field Office \[ANONYMOUS.SOFTWARE\] directories.

|               |                                   |                      |
|---------------|-----------------------------------|----------------------|
| File Name | Description                   | Retrieval Format |
| FH5_5ADP.PDF  | ADPAC Guide                       | Binary               |
| FH5_5IG.PDF   | Installation/Implementation Guide | Binary               |
| FH5_5RN.PDF   | Release Notes                     | Binary               |
| FH5_5TM.PDF   | Technical/Security Manual         | Binary               |
| FH5_5UM.PDF   | User Manual                       | Binary               |

# Nutrition and Food Service Outpatient Meals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Meals menus and options are accessible from the Dietetics Management menu \[FHMGR\]. These menus automate and replace the manual processes for ordering individual special meals, recurring meals for VA patients and patients at non-VA facilities, and guest meals for an outpatient or a collateral/volunteer/resident. Each of the new menus has various options specialized for the type of meal being requested and approved through an authorization process that notifies the requestor via Alert Message.

The Outpatient Meals main menu can be accessed from the Dietetics Management menu.

DIETETICS MANAGEMENT

AD Dietetic Administration ...

CM Clinical Management ...

DF Dietetic Facilities ...

OM Outpatient Meals ...

SM System Management ...

XF File Manager ...

Select Dietetics Management Option: OM Outpatient Meals

# File Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three files, 115, 119.6, and 119.8, names have changed:

- DIETETICS PATIENT is now NUTRITION PERSON (115)
- DIETETICS WARD is now NUTRITION LOCATION (119.6)
- DIETETIC EVENTS is now NUTRITION EVENTS (119.8)

For NUTRITION PERSON file (115), this existing field (.01) will be modified and the existing data converted. The field will be modified to be a free text field. This field will store either "P" followed by a pointer value to File (#2) or "N" followed by a pointer value to File (#200). For example, this field might store P27 for IEN \#27 in File (#2). Or this field might store N1866 for IEN \#1866 in File (#200). Existing pointers will be converted to the new format.

# New Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Internal Entry Name</strong></th>
<th><strong>Option Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[FHMGROM]</td>
<td>OM Outpatient Meals Main Menu</td>
<td>This menu allows access to all options pertaining to the outpatient meals functionality.</td>
</tr>
<tr class="even">
<td>[FHOMSMGR]</td>
<td>SM Special Meals Menu</td>
<td>This menu allows access to all special meals options within the outpatient meals menu</td>
</tr>
<tr class="odd">
<td>[FHOMSR]</td>
<td>RO Request a Meal</td>
<td>This option allows the request of a special meal.</td>
</tr>
<tr class="even">
<td>[FHOMSA]</td>
<td>AM Authorize a Meal</td>
<td>This option allows an authorized user to authorize a special meal request.</td>
</tr>
<tr class="odd">
<td>[FHOMSP]</td>
<td>PM Print Meal Voucher</td>
<td>This option allows the printing of a special meal voucher ticket.</td>
</tr>
<tr class="even">
<td>[FHOMSC]</td>
<td>CM Cancel a Meal</td>
<td>This option allows the user to cancel a special meal.</td>
</tr>
<tr class="odd">
<td>[FHOMSS]</td>
<td>MS Meal Status Report</td>
<td>This option allows to prints a list of existing special meals and their current status</td>
</tr>
<tr class="even">
<td>[FHOMRMGR]</td>
<td>RM Recurring Meals Menu</td>
<td>This menu allows access to all recurring meals options within the outpatient meals menu.</td>
</tr>
<tr class="odd">
<td>[FHOMRO]</td>
<td>OD Order/Edit Outpatient Meals</td>
<td>This option allows the ordering of recurring outpatient meals or the editing of existing outpatient meals.</td>
</tr>
<tr class="even">
<td>[FHOMRE]</td>
<td>EL Early/Late Tray</td>
<td>This option allows the entering of an early/late tray for an outpatient recurring meal.</td>
</tr>
<tr class="odd">
<td>[FHOMRR]</td>
<td>RO Review Outpatient Meal</td>
<td>This option is used to display/review recurring outpatient meals.</td>
</tr>
<tr class="even">
<td>[FHORD9]</td>
<td>PP Patient Profile</td>
<td><p>This option will produce a comprehensive display of most dietetic orders and data associated with a patient's admission. It includes diet orders, active or saved consults, early/late tray requests for the next 72 hours, standing orders, tube feedings, supplemental feedings, etc.</p>
<p>As of Version 5.5, this report will include outpatient data as well, including recurring meals, special meals and guest meals.</p></td>
</tr>
</tbody>
</table>

|                         |                                        |                                                                                                                                                                         |
|-------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Internal Entry Name | Option Name                        | Description                                                                                                                                                         |
| \[FHOMRC\]              | CM Cancel Outpatient Meal              | This option allows the cancellation of existing outpatient recurring meal(s).                                                                                           |
| \[FHOMRA\]              | AO Additional Orders                   | This option allows the entry of additional orders for outpatients with recurring meals.                                                                                 |
| \[FHOMRT\]              | TF Tube feeding                        | This option allows the ordering of tube feedings for outpatients with recurring meals.                                                                                  |
| \[FHOMRP\]              | PT Recurring Meal Plan Expiration List | This option displays a list of meal plans expiring for selected outpatient locations.                                                                                   |
| \[FHOMIP\]              | IP Outpatient Isolation/Precaution     | This option is used for entering Isolations/Precautions for outpatients.                                                                                                |
| \[FHOMRAC\]             | CA Cancel Additional Order             | This option is used to cancel existing additional orders.                                                                                                               |
| \[FHOMREC\]             | CE Cancel Early/Late Tray              | This option is used to cancel existing early/late tray orders.                                                                                                          |
| \[FHOMRTC\]             | CT Cancel Tube feeding                 | This option is used to cancel existing tube feeding orders.                                                                                                             |
| \[FHOMGMGR\]            | GM Guest Meals Menu                    | This menu allows access to all guest meals options within the outpatient meals menu.                                                                                    |
| \[FHOMGR\]              | GM Request a Meal                      | This option allows the user to order an outpatient guest meal for individuals categorized in one of the five listed classifications and be added to the N&FS meal list. |
| \[FHOMGP\]              | PT Print Guest Meal List               | This option provides a printed list of requested guest meals by Date, Patient Name, Meal, Class, and Location.                                                          |