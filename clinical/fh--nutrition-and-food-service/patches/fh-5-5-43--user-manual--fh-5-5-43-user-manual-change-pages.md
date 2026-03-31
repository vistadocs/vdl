---
title: FH*5.5*43 User Manual Change Pages
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Change Pages
app_code: FH
app_name: Nutrition and Food Service
section: CLI
app_status: active
pkg_ns: FH
patch_ver: 5.5
patch_id: FH*5.5*43
group_key: "FH:FH:5.5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Document Purpose](#document-purpose) - [Scope of Patch FH\5.5\43](#scope-of-patch-fh5543) - [Updates to Nutrition and Food Service](#updates-to-nutrition-and-food-service) - [Enhancements](#enhancements) - [Package Management](#package-management) - [Package Operation (Page 9)](#package-operati
audience: 
keywords: 
  - tray
  - table
  - contents
  - tickets
  - print
  - supplemental
  - options
  - test
  - manual
  - feeding
page_count: 0
word_count: 1607
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_um_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh_5_5_p43_um_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

Nutrition and Food Service User Manual

Change Pages for Patch FH\*5.5\*43

![](fh-5-5-43-user-manual-change-pages/001.png)

March 2019Version 2.0

Revision History

| Date    | Description of Change(s)                                                                                                                                                                                                                                       | VA Project Manager                 | Technical Writer                   |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 03/2019 | Added a Note to page [3](#FHPRO11_setting_Note) to clarify a required setting.                                                                                                                                                                                 | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 01/2019 | Added Patch FH\*5.5\*43 enhancements to sections [<u>Package Management</u>](#package-management), [<u>DM Dietetics Management \[FHMGR\]</u>](#dm-dietetics-management-fhmgr), and [<u>CM Clinical Management \[FHMGRC\]</u>](#cm-clinical-management-fhmgrc). | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

# # Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Document Purpose](#document-purpose)
- [Scope of Patch FH\5.5\43](#scope-of-patch-fh5543)
- [Updates to Nutrition and Food Service](#updates-to-nutrition-and-food-service)
- [Enhancements](#enhancements)
  - [Package Management](#package-management)
    - [Package Operation (Page 9)](#package-operation-page-9)
  - [DM Dietetics Management \[FHMGR\]](#dm-dietetics-management-fhmgr)
    - [WL Ward Supplemental Feeding Lists \[FHNO3\] (Page 102)](#wl-ward-supplemental-feeding-lists-fhno3-page-102)
  - [CM Clinical Management \[FHMGRC\]](#cm-clinical-management-fhmgrc)
    - [TT Tray Tickets \[FHMTKM\] (Page 180)](#tt-tray-tickets-fhmtkm-page-180)
    - [PT Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\] (Page 186)](#pt-print-tray-tickets-fhmtk1p-tray-ticket-print-page-186)
This document presents the new functionality provided by patch FH\*5.5\*43 and should be considered an update to the existing *Nutrition and Food Service User Manual, Version 5.5* (2005). The new material presented in this document is provided in lieu of inserting revisions directly into the text of the existing User Manual because no editable (MS Word) document can be located.

# Scope of Patch FH\*5.5\*43

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 modifies the VistA Dietetics Report Queuing software to automatically queue Nutrition and Food Service (NFS) reports and labels to run daily, or as often as necessary, without requiring Dietetics staff to manually queue them each day. This enhancement also <span class="mark"></span>enables staff in a Community Living Center (CLC) to enter meal instructions for morning, midday, and evening meals that are displayed as flags at the bottom of each tray ticket.

# Updates to Nutrition and Food Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements and modifications discussed herein are provided to update the existing *Food and Nutrition Service (NSF) User Manual, Version 5.5* to include the functionality provided in patch FH\*5.5\*43. The following User Manual sections are impacted by the functionality introduced with this patch:

- Package Management
- DM Dietetics Management \[FHMGR\]
- CM Clinical Management \[FHMGRC\]

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Package Operation (Page 9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 modifies the VistA Dietetics Report Queuing software to automatically queue Nutrition and Food Service (NFS) reports and labels to run daily, or as often as necessary, without requiring Dietetics staff to manually queue them each day.

An NSF Manager, Clinical Application Coordinator (CAC), or Automated Data Processing Application Coordinator (ADPAC) can set pre-defined options for printing NFS reports and labels automatically. Three new options enabling this functionality are added to the existing Tray Tickets \[FHMTKM\] menu. The Manager/CAC/ADPAC must be assigned the NFS security key FHMGR to access these options.

![](fh-5-5-43-user-manual-change-pages/002.png)

New VistA Options for Queuing Dietetics ReportsNotes:

- The new options can alternatively be accessed by typing “FHQUE” at the “Select OPTION NAME:” prompt.
- The Manager/CAC/ADPAC must be assigned the NFS security key FHMGR to access these options.

![](fh-5-5-43-user-manual-change-pages/003.png)

Queuing Dietetics Reports Options Displayed from the FHQUE OptionNote: Refer to [TT Tray Tickets \[FHMTKM\]](#tt-tray-tickets-fhmtkm-page-180) for more information on these options.

## DM Dietetics Management \[FHMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### WL Ward Supplemental Feeding Lists \[FHNO3\] (Page 102)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FH\*5.5\*43 enhances the existing Patient Supplemental Feeding List to display the most recent patient Diet Order. Diet orders can change frequently based on a patient’s medical needs; sometimes diet orders are changed in VistA after a supplemental feeding is prepared by a food service worker.

Currently, there is no easy way to check supplemental feeding orders against the patient’s most recent diet order before delivering the supplemental nutrition. This enhancement reduces the risk of improper feeding by retrieving current diet order information from VistA and using that data to prepare the Patient Supplemental Feeding List, so that both the current diet order and the supplemental feeding order are included.

![](fh-5-5-43-user-manual-change-pages/004.png)

Patient Supplemental Feeding List

The enhanced Patient Supplemental Feeding List and Consolidated Ingredients list are accessible from the “Run SF Labels/Consolid Ingred List” \[FHNO2\] option on the SUPPLEMENTAL FEEDINGS \[FHNOM\] menu. Navigate to this option using the following path:

> Dietetics Management \[FHMGR\]

> Clinical Management \[FMHGRC\]

> Clinical Dietetics \[FHDIET\]

> Supplemental Feedings \[FHNOM\]

> Run SF Labels/Consolid Ingred List \[FHNO2\]

Refer to the *LA Run SF Labels/Consolid Ingred List \[FHNO2\]* section in the *Nutrition and Food Service User Manual* for more information on the FHNO2 option.

<span id="FHPRO11_setting_Note" class="anchor"></span>Note: The Diet Order will display on the Patient Supplemental Feeding List only if the SEPARATE SUPP FDG LABELS? field is set to NO, or if the site does not have a Supplemental Feeding Site configured. An ADPAC who is assigned the FHMGR key can change the value of the SEPARATE SUPP FDG LABELS? field using the “Enter/Edit Supplemental Fdg. Sites” \[FHPRO11\] option on the DIETETIC FACILITIES \[FHPRG\] menu in VistA.

> ![](fh-5-5-43-user-manual-change-pages/005.png)

## CM Clinical Management \[FHMGRC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TT Tray Tickets \[FHMTKM\] (Page 180)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table is updated with the new options added to the Tray Tickets \[FHMTKM\] menu; the first four options are new. Details about each new option are provided in this section.

| FE  | Tray Ticket Flag Edit \[FHMTK1D TRAY TICKET EDIT\] |
|-----|----------------------------------------------------|
| FHE | Queued Options Edit \[FHQUE OPTION EDIT\]          |
| FHQ | Queue Diet Reports \[FHQUE QUEUE DIET REPORTS\]    |
| FHT | Test an Individual Queued Option \[FHQUE TEST\]    |
| HP  | History of Diet Patterns \[FHMTKH\]                |
| LD  | List Patients With No/prev Patterns \[FHMTKN\]     |
| PD  | Print Diet Cards \[FHDCRP\]                        |
| PT  | Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\]   |

#### FE Tray Ticket Flag Edit \[FHMTK1D TRAY TICKET EDIT\]

This option enables CLC staff to enter meal instructions for morning, midday, and evening meals in free-text fields. The text entered in these fields is printed at the bottom of the tray ticket where it can be easily seen by clinical staff.

> **NOTE:** To use this option, the Ward to which a patient is assigned must include “CLC” in the Ward name.

After selecting the Tray Ticket Flag Edit option, the user is prompted to select either a Ward or a Patient. The BREAKFAST FLAG, NOON FLAG, and EVENING FLAG fields display so that text can be entered in one or more of the fields.

> **NOTE:** Flag text is limited to 18 characters.

Example:

Select Tray Tickets \<TEST ACCOUNT\> Option: FE  Tray Ticket Flag Edit

     Select one of the following:

          P         PATIENT

          W         WARD

Select by (P)atient or (W)ard: P// WARD

     BXHUKXXZ,TLZZDH E DD   CLC   138-2

BREAKFAST FLAG: test morn flg//

NOON FLAG: test noon flg//

EVENING FLAG: test eve flg//

![](fh-5-5-43-user-manual-change-pages/006.png)

Tray Ticket Displaying a Tray Ticket Flag

#### FHE Queued Options Edit \[FHQUE OPTION EDIT\]

This option displays a list of available reports that can be selected and configured by an NFS Manager, CAC, or ADPAC whose permissions include the FHMGR key. When configuring a report, the user is prompted for the desired printer and whether it is active, the days of the week to run the report, and the time at which to run the report (e.g., T-1@18:00), if applicable.

> Available options are:

>     1. FHASNR4         List Inpats By Nutrition Status Level

>     2. FHBIR           Birthday List

>     3. FHMTKP          Print Tray Tickets

>     4. FHORD10         Nutrition Location Diet Order List

>     5. FHORD13         Diet Activity Report/Labels

>     6. FHORD5          NPO/Pass List

>     7. FHORT5S         Tubefeeding Pull Lists

>     8. FHORTF5         Preparation/Delivery of Tubefeedings

>    9. FHPATM          Patient Movements

> FHE Queued Options Edit List of Reports

A new report option, Print Tray Tickets \[FHMTKP\], prompts the user for the meal ticket to print (Breakfast, Noon, or Evening).

Example:

Your choice, choose by number: 3 Print Tray Tickets

Time to run the option (use 4 digit military time): 0010

Add entry "FHMTKP 0010"? Yes//   (Yes)

Entry added.

Now add/change the printer and whether it's active.

PRINTER: P-MESSAGE-HFS      HFS FILE =\> MESSAGE     XMHFS.TMP    

ACTIVE: YES//   YES

Select DAYS TO RUN:

Choose a meal to print: B for Breakfast, N for Noon, E for Evening meal: B

Option added!

Notes:

- The Print Tray Tickets \[FHMTKP\] option is only available when working with Inpatients.
- Enter ?? \<RET\> to get help or \<RET\> at the // prompt for the default selection.
- The default for DAY TO RUN = ALL.

#### FHQ Queue Diet Reports \[FHQUE QUEUE DIET REPORTS\]

This option passes the configured reports and labels to TaskMan to be executed and printed. After configuration, TaskMan run this option at a selected time. Typically, Queue Diet Reports is scheduled to run once per day, soon after midnight.

An NFS Manager, CAC, or ADPAC whose permissions include the FHMGR key can use this option to pass configured reports to a printer to test that all configured reports print as expected.

#### Test an Individual Queued Option \[FHQUE TEST\]

This option is used by an NFS Manager, CAC, or ADPAC whose permissions include the FHMGR key to immediately run an individual test report and validate selected report options.

After the option is specified and a printer is selected, a task number is returned (e.g., ZTSK=123456).

Example:

Select OPTION NAME: FHQUE  
     1   FHQUE       Queue Diet Reports   
     2   FHQUE OPTION EDIT       Queued Options Edit   
     3   FHQUE TEST       Test an Individual Queued Option   
CHOOSE 1-3: 3  FHQUE TEST     Test an Individual Queued Option 

Test an Individual Queued Option

IEN: ?   
1         FHMTKP 0010

IEN: 1 

Select printer: P-MESSAGE-HFS      HFS FILE =\> MESSAGE     XMHFS.TMP     

ZTSK=158368

Notes:

- Enter ?? \<RET\> to get help or \<RET\> at the // prompt for the default selection.
- Only previously configured options are available to test.
- TaskMan will schedule and run immediately if the report time is before or at the current time and today is selected as the day of the week.
- The ZTSK task number will not appear if the report is not scheduled.

### PT Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\] (Page 186)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables printing patient Tray Tickets. Refer to the section “PT Print Tray Tickets \[FHMTKP\]” in the *VistA Nutrition and Food Service User Manual, Version 5.5* for additional details. The functionality described here represents a modification of this option.

> **NOTE:** This modification is intended for use in a CLC facility only.

The existing PT Print Tray Tickets \[FHMTK1P TRAY TICKET PRINT\] option is modified to include printing flag text on patient tray tickets where it can be easily seen by clinical staff at mealtime.

![](fh-5-5-43-user-manual-change-pages/007.png)

Print Tray Tickets Option