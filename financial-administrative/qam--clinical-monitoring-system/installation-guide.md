---
title: Clinical Monitoring System Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: QAM
app_name: Clinical Monitoring System
section: FIN
app_status: active
pkg_ns: QAM
patch_ver: 1
patch_id: QAM*1
group_key: "QAM:QAM:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Installing the System](#installing-the-system) - [# IRM Setup](#irm-setup) - [# Resource Requirements](#resource-requirements) - [# Installation Example](#installation-example) - [# Implementation Check List](#implementation-check-list) - [Monitoring System Manager Menu](#monitoring-system-mana
audience: 
keywords: 
  - filed
  - group
  - loading
  - loaded
  - edit
  - deleting
  - auto
  - monitoring
  - site
  - table
page_count: 0
word_count: 2698
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 2/23/09
revision_oldest: 2/23/09
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cminst.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Clin_Monitoring_System/cminst.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=32"
---

![](clinical-monitoring-system-version-1-installation-guide/001.png)

Clinical Monitoring System V. 1.0Installation GuideSeptember 1993

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 2/23/09

| Date    | Description (Patch \# if applic.) | Project Manager | Technical Writer |
|---------|-----------------------------------|-----------------|------------------|
| 2/23/09 | Reformatted Manual                |                 | REDACTED         |

Table of Contents

# # Installing the System


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Installing the System](#installing-the-system)
- [# IRM Setup](#irm-setup)
- [# Resource Requirements](#resource-requirements)
- [# Installation Example](#installation-example)
- [# Implementation Check List](#implementation-check-list)
- [Monitoring System Manager Menu](#monitoring-system-manager-menu)
  - [## Site Parameters Edit Option](#site-parameters-edit-option)
  - [Application Group Edit Option](#application-group-edit-option)
This package requires Kernel 7.0 or later, VA FileMan 19 or later, MAS 5 or later, and the NEW PERSON file (#200). This software has a condition that accesses the Lab package and was developed using Lab Version 5.1. If your site is running Mental Health Version 4.18 and/or Outpatient Pharmacy Version 5.5 or later, the Clinical Monitoring System software also offers conditions using those packages. The global ^QA should be journaled and backed up. Journaling should be suspended during the installation. All QA package end users should be off the system. Others may remain on. It is recommended that the initialization be done at a time of low activity.
Do not delete any of the QAQ\* routines prior to loading this package. A pre-init routine will take care of the loading and/or deleting of the appropriate QAQ routines.1. There are a number of ICD/Diagnosis and Procedure groups used by JCAHO indicator monitors that can be installed either during the initial installation via a post-init or at a later date (See Installation Example). Check with your QM ADPAC to determine if and/or when these should be loaded.
2. Load the QAM\*, QAQ\* and QAI\* routines into the account where the ^QA global resides, or where you want it to reside. If ^QA does not exist, place it by using the GLOMAN (DSM) or %GCH (MSM) utility and set global protection to "RW". Before using %GCH, "S ^QA=0".
> **NOTE:** QAQ routines are used by all QA namespaced packages and therefore are distributed with them. QAI routines install and clean up older versions of the QAQ routines.
3. Initialize the package by running the Clinical Monitoring System installation routine.
D ^QAMINST
The install routine will update the QA Integration Module based upon the version you are running, if any. The Clinical Monitoring System V1.0 will then perform the init routines. See the Installation Example.

# # IRM Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the main steps for IRM in the setup of the software. For more complete instructions, see the Implementation Check List.

1. Using the TaskManager *Schedule/Unschedule Options* option, please queue the automatic enrollment option *QAM TASKED AUTO ENROLL RUN* to run daily after midnight. This option calls the routine QAMAUTO0 that searches the database for patient activities that meet defined conditions from the previous day. For more information on conditions, please refer to the User Manual or ADPAC Guide.
2. Do not select a printer device within TaskMan. Define the device for output by using the manager menu option *Site Parameters Edit*. The other site parameters that control the manual running of auto enroll should also be edited at this time. See the Site Parameters option documentation in this manual for more details.
3. Use the *Application Group Edit* option to add the desired files to the QAM application group. This step is necessary before any groups can be created from those files via the *Group Edit* option. Below is the default list of files included in this option. Files can be added to or removed from this list.

| 2    | Patient                     | 80.1  | ICD Operation/Procedure       |
|------|-----------------------------|-------|-------------------------------|
| 37   | Disposition                 | 405.3 | MAS Movement Transaction Type |
| 42   | Ward Location               | 405.2 | MAS Movement Type             |
| 44   | Hospital Location           | 409.1 | Appointment Type              |
| 45.7 | Facility Treating Specialty | 615.5 | S/R Reason                    |
| 49   | Service / Section           | 615.6 | S/R Category                  |
| 80   | ICD Diagnoses               | 743   | QA Monitor                    |

4. Ascertain that the QA users have their terminals and printers in place and functional.
5. With the assistance of the QM ADPAC, assign the menus to users. The Monitoring System Manager Menu is usually given only to the QM ADPAC. The Monitoring System Programmer Menu should be assigned to the IRM support person for the Clinical Monitoring System. This may vary with the site. There are no security keys to take into consideration at this time.

# # Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*CRTs*

At least one CRT for the use of the QM Coordinator; more if required for the QM staff.

*Printers*

At least one dedicated for QM use. It is preferable to route the report of the daily auto enrollment running to this printer. The printer needs to be available at all times for producing reports

CPU Capacity

The daily interactive use of the package uses only a small amount of the total CPU capacity. The nightly run of the auto enroll routines is more intensive, but this process should be queued to run at a time of low CPU activity.

*Disk Capacity*

File \#743 1000 bytes per record

File \#743.1 1000 bytes per record

# # Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that the text of the init dialogue may not be an exact match of what you will see when running the installation. It is provided as a best approximation of a typical install.

D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: \<RET\>

D ^QAMINST

Beginning installation of Clinical Monitoring System Version 1.0.

You are running Version \#.# of the QA Integration Module.

I have to update the QA Integration Module to version 1.5

> **NOTE:** The version number displayed (#.#) may be any number less than 1.5. If it is equal to 1.5, it will not be updated.

This version (#1.5) of 'QAQINIT' was created on 29-JUL-1993

(at VAMCSITE ISC, by VA FileMan V.19)

I HAVE TO RUN A PRE-INITIALIZATION ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

740 QUALITY ASSURANCE SITE PARAMETERS

> **NOTE:** You already have the 'QUALITY ASSURANCE SITE PARAMETERS' File.

740.1 AD HOC MACRO

740.5 QA AUDIT

> **NOTE:** You already have the 'QA AUDIT' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? Y (YES)

Install/Clean-up QA Integration Module routines.

Loading QAIADLAU Replacing QAQADLAU Deleting QAIADLAU

Loading QAIAHOC0 Saving as QAQAHOC0 Deleting QAIAHOC0

Loading QAIAHOC1 Saving as QAQAHOC1 Deleting QAIAHOC1

Loading QAIAHOC2 Saving as QAQAHOC2 Deleting QAIAHOC2

Loading QAIAHOC3 Saving as QAQAHOC3 Deleting QAIAHOC3

Loading QAIAHOC4 Saving as QAQAHOC4 Deleting QAIAHOC4

Loading QAIAHOCH Saving as QAQAHOCH Deleting QAIAHOCH

Loading QAIAHOCX Saving as QAQAHOCX Deleting QAIAHOCX

Loading QAIAHOCY Saving as QAQAHOCY Deleting QAIAHOCY

Loading QAIAHOCZ Saving as QAQAHOCZ Deleting QAIAHOCZ

Loading QAIAPGRP Replacing QAQAPGRP Deleting QAIAPGRP

Loading QAIAUDIT Replacing QAQAUDIT Deleting QAIAUDIT

Loading QAIAUTL Replacing QAQAUTL Deleting QAIAUTL

Loading QAIAXREF Replacing QAQAXREF Deleting QAIAXREF

Loading QAIDATE Replacing QAQDATE Deleting QAIDATE

Loading QAINTEG Replacing QAQNTEG Deleting QAINTEG

Loading QAIPKGVR Replacing QAQPKGVR Deleting QAIPKGVR

Loading QAISELCT Replacing QAQSELCT Deleting QAISELCT

Loading QAISITE Replacing QAQSITE Deleting QAISITE

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND..........................

'QAQ MANAGER' Option Filed

'QAQ PACKAGES INQUIRE' Option Filed

'QAQ SITE PARAMETERS' Option Filed

'QAQ USER' Option Filed......

OK, I'M DONE.

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

You are running Version 1.5 of the QA Integration Module.

Now installing Clinical Monitoring System Version 1.0.

This version (1.0) of 'QAMINIT' was created on 29-JUL-1993

(at VAMCSITE ISC, by VA FileMan V.19)

I HAVE TO RUN A PRE-INITIALIZATION ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

743 QA MONITOR

743.1 FALL OUT

743.2 MONITOR HISTORY

743.3 CONDITION (including data)

I will OVERWRITE your data with mine.

743.4 DATA ELEMENT (including data)

I will OVERWRITE your data with mine.

743.5 GROUP

743.6 AUTO ENROLL RUN DATE

743.91 RATIONALE (including data)

I will OVERWRITE your data with mine.

743.92 TIME FRAME (including data)

I will OVERWRITE your data with mine.

> **NOTE:** This package also contains BULLETINS

> **NOTE:** This package also contains FUNCTIONS

> **NOTE:** This package also contains OPTIONS

ARE YOU SURE EVERYTHING'S OK? Y (YES)

...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS.......................................

...................................................

'QAM MONITOR TOOL 1' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'QAM MONITOR TOOL 2' BULLETIN FILED -- Remember to add mail groups for new bulletins........

...........................

'QAM BUILD MONITOR EDIT' Option Filed

'QAM BUILD MONITOR MENU' Option Filed

'QAM BUILD PATIENT GROUP' Option Filed

'QAM COPY MONITOR EDIT' Option Filed

'QAM FALL OUT EDIT' Option Filed

'QAM GROUP FILE EDIT' Option Filed

'QAM INQ AUDIT FILE' Option Filed

'QAM INQ CONDITION FILE' Option Filed

'QAM INQ DATA ELEMENT FILE' Option Filed

'QAM INQ FALL OUT FILE' Option Filed

'QAM INQ GROUP FILE' Option Filed

'QAM MANAGER MENU' Option Filed

'QAM MANAGER REPORTS MENU' Option Filed

'QAM MANUAL AUTO ENROLL RUN' Option Filed

'QAM PGMR APP GROUP EDIT' Option Filed

'QAM PGMR CONDITIONS EDIT' Option Filed

'QAM PGMR DATA ELEMENTS EDIT' Option Filed

'QAM PGMR MENU' Option Filed

'QAM PGMR MONITOR EDIT' Option Filed

'QAM PGMR TIME FRAME EDIT' Option Filed

'QAM PURGE AUTO RUN DATES FILE' Option Filed

'QAM PURGE FALL OUT FILE' Option Filed

'QAM PURGE HISTORY FILE' Option Filed

'QAM PURGE MENU' Option Filed

'QAM QUICK MONITOR EDIT' Option Filed

'QAM RATIONALE FILE EDIT' Option Filed

'QAM RPT ADHOC' Option Filed

'QAM RPT AUTO/MAN MONITORS RUN' Option Filed

'QAM RPT BUILD MON WORKSHEET' Option Filed

'QAM RPT MONITOR ADHOC' Option Filed

'QAM RPT MONITOR DESCRIPTION' Option Filed

'QAM RPT MONITOR HISTORY' Option Filed

'QAM RPT MULTIPLE FALL OUTS' Option Filed

'QAM SAMPLE SIZE EDIT' Option Filed

'QAM SITE PARAMETERS EDIT' Option Filed

'QAM TASKED AUTO ENROLL RUN' Option Filed

'QAM USER MENU' Option Filed

'QAM USER REPORTS MENU' Option Filed.

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

> **NOTE:** The following prompt will only appear if you have never installed any of the QM packages.

Select QUALITY ASSURANCE SITE PARAMETERS NAME: Your VAMC

ARE YOU ADDING 'Your VAMC' AS A NEW QUALITY ASSURANCE SITE PARAMETERS

(THE 1ST)? Y (YES)

Do you want to load the ICD Diagnosis/Procedure groups now? NO// ?

Answer Y(es) to load the ICD Diagnosis and Procedure groups used by the

JCAHO Anesthesia, Trauma, and Cardiovascular indicator monitors. Answer

N(o) to skip loading these groups. The groups may be loaded at a later

time by entering: DO ^QAMGRP1. Please note, some of these groups are quite

large, over 2000 entries.

> **NOTE:** The time required to create these groups on a lightly loaded VAX was about one and a half minutes. These groups can be created with QA users on the system. If you decide to load these groups at a later time, enter "D ^XUP" before "DO ^QAMGRP1".

Do you want to load the ICD Diagnosis/Procedure groups now? NO// Y (YES)

Loading: AN-1 DIAG GROUP

Working

431\. 433.0 433.1 433.2 433.3 433.8 433.9 434.0

434.1 434.9 436. 668.20 668.21 668.22 997.0

15 ICD-9-CM Diagnosis Codes loaded.

Loading: AN-2 DIAG GROUP

Working

736.05 736.79 781.4 782.0

4 ICD-9-CM Diagnosis Codes loaded.

Loading: AN-3 DIAG GROUP

Working

410.01 410.11 410.21 410.31 410.41 410.51 410.61 410.71

410.81 410.91

10 ICD-9-CM Diagnosis Codes loaded.

Loading: AN-4 DIAG GROUP

Working

427.5 668.11 668.12 669.41 669.42 997.1

6 ICD-9-CM Diagnosis Codes loaded.

Loading: AN-5 DIAG GROUP

Working

669.10 799.1 995.4 998.0

4 ICD-9-CM Diagnosis Codes loaded.

Loading: TR-8A DIAG GROUP (GUNSHOT)

Working

879.2 879.3 879.4 879.5

4 ICD-9-CM Diagnosis Codes loaded.

Loading: TR-8B DIAG GROUP (KNIFE)

Working

879.2 879.3 879.4 879.5

4 ICD-9-CM Diagnosis Codes loaded.

Loading: TR-10 DIAG GROUP

Working

821.01 821.11

2 ICD-9-CM Diagnosis Codes loaded.

Loading: TR-11 DIAG GROUP

Working

852.20 852.50 868.03 868.13 860.2 860.3 860.4 860.5

901.0 902.0 423.9 560.0 560.1

13 ICD-9-CM Diagnosis Codes loaded.

Loading: TR-12 DIAG GROUP-BASIC TRAUMA

Working

800.00 800.01 800.02 800.03 800.04 800.05 800.06 800.09

800.10 800.11 800.12 800.13 800.14 800.15 800.16 800.19

800.20 800.21 800.22 800.23 800.24 800.25 800.26 800.29

800.30 800.31 800.32 800.33 800.34 800.35 800.36 800.39

800.40 800.41 800.42 800.43 800.44 800.45 800.46 800.49

800.50 800.51 800.52 800.53 800.54 800.55 800.56 800.59

800.60 800.61 800.62 800.63 800.64 800.65 800.66 800.69

800.70 800.71 800.72 800.73 800.74 800.75 800.76 800.79

800.80 800.81 800.82 800.83 800.84 800.85 800.86 800.89

800.90 800.91 800.92 800.93 800.94 800.95 800.96 800.99

801.00 801.01 801.02 801.03 801.04 801.05 801.06 801.09

801.10 801.11 801.12 801.13 801.14 801.15 801.16 801.19

801.20 801.21 801.22 801.23 801.24 801.25 801.26 801.29

801.30 801.31 801.32 801.33 801.34 801.35 801.36 801.39

801.40 801.41 801.42 801.43 801.44 801.45 801.46 801.49

801.50 801.51 801.52 801.53 801.54 801.55 801.56 801.59

801.60 801.61 801.62 801.63 801.64 801.65 801.66 801.69

801.70 801.71 801.72 801.73 801.74 801.75 801.76 801.79

801.80 801.81 801.82 801.83 801.84 801.85 801.86 801.89

801.90 802.1 802.30 802.31 802.32 802.33 802.34 802.35

802.36 802.37 802.38 802.39 802.5 802.7 802.9 803.00

803.01 803.02 803.03 803.04 803.05 803.06 803.09 803.10

803.11 803.12 803.13 803.14 803.15 803.16 803.19 803.20

803.21 803.22 803.23 803.24 803.25 803.26 803.29 803.30

803.31 803.32 803.33 803.34 803.35 803.36 803.39 803.40

803.41 803.42 803.43 803.44 803.45 803.46 803.49 803.50

803.51 803.52 803.53 803.54 803.55 803.56 803.59 803.60

803.61 803.62 803.63 803.64 803.65 803.66 803.69 803.70

803.71 803.72 803.73 803.74 803.75 803.76 803.79 803.80

803.81 803.82 803.83 803.84 803.85 803.86 803.89 803.90

803.91 803.92 803.93 803.94 803.95 803.96 803.99 804.00

804.01 804.02 804.03 804.04 804.05 804.06 804.09 804.10

804.11 804.12 804.13 804.14 804.15 804.16 804.19 804.20

804.21 804.22 804.23 804.24 804.25 804.26 804.29 804.30

804.31 804.32 804.33 804.34 804.35 804.36 804.39 804.40

804.41 804.42 804.43 804.44 804.45 804.46 804.49 804.50

804.51 804.52 804.53 804.54 804.55 804.56 804.59 804.60

804.61 804.62 804.63 804.64 804.65 804.66 804.69 804.70

804.71 804.72 804.73 804.74 804.75 804.76 804.79 804.80

804.81 804.82 804.83 804.84 804.85 804.86 804.89 804.90

804.91 804.92 804.93 804.94 804.95 804.96 804.99 805.00

805.01 805.02 805.03 805.04 805.05 805.06 805.07 805.08

805.10 805.11 805.12 805.13 805.14 805.15 805.16 805.17

805.18 805.2 805.3 805.4 805.5 805.6 805.7 805.8

805.9 806.00 806.01 806.02 806.03 806.04 806.05 806.06

806.07 806.08 806.09 806.10 806.11 806.12 806.13 806.14

806.15 806.16 806.17 806.18 806.19 806.20 806.21 806.22

806.23 806.24 806.25 806.26 806.27 806.28 806.29 806.30

806.31 806.32 806.33 806.34 806.35 806.36 806.37 806.38

806.39 806.4 806.5 806.60 806.61 806.62 806.69 806.70

806.71 806.72 806.79 806.8 806.9 807.00 807.01 807.02

807.03 807.04 807.05 807.06 807.07 807.08 807.09 807.10

807.11 807.12 807.13 807.14 807.15 807.16 807.17 807.18

807.19 807.2 807.3 807.4 807.5 807.6 808.0 808.1

808.2 808.3 808.41 808.42 808.43 808.49 808.51 808.52

808.53 808.59 808.8 808.9 809.0 809.1 810.10 811.10

812.10 812.30 812.50 813.10 813.30 813.50 813.90 818.0

818.1 819.0 819.1 820.00 820.01 820.02 820.03 820.09

820.10 820.11 820.12 820.13 820.19 820.20 820.21 820.22

820.30 820.31 820.32 820.8 820.9 821.00 821.01 821.10

821.11 821.20 821.21 821.22 821.23 821.29 821.30 821.31

821.32 821.33 821.39 822.0 822.1 823.10 823.30 823.90

827.0 939.9 950.0 950.1 950.2 950.3 950.9 951.0

951.1 951.2 951.3 951.4 951.5 951.6 951.7 951.8

951.9 952.00 952.01 952.02 952.03 952.04 952.05 952.06

952.07 952.08 952.09 952.10 952.11 952.12 952.13 952.14

952.15 952.16 952.17 952.18 952.19 952.2 952.3 952.4

952.8 952.9 953.0 953.1 953.2 953.3 953.4 953.5

953.8 953.9 954.0 954.1 954.8 954.9 955.0 955.1

955.2 955.3 955.4 955.5 955.6 955.7 955.8 955.9

956.0 956.1 956.2 956.3 956.4 956.5 956.8 956.9

957.0 957.1 957.8 957.9 958.0 958.1 958.2 958.3

958.4 958.5 958.6 958.7 958.8 959.0 959.1 959.2

959.3 959.4 959.5 959.6 959.7 959.8 959.9

591 ICD-9-CM Diagnosis Codes loaded.

Loading: CV-4 DIAG GROUP

Working

410.0 410.00 410.01 410.02 410.1 410.10 997.1

7 ICD-9-CM Diagnosis Codes loaded.

Loading: ANESTHESIA INDICATOR PROC LIST

Working

01.01 02.02 02.022 04.04 10.0 11.1 11.21 11.22

11.29 11.31 11.32 11.39 11.41 11.42 11.43 11.49

11.51 11.52 11.53 11.59 11.60 11.61 11.62 11.63

11.64 11.69 11.691 11.71 11.72 11.73 11.74 11.75

11.76 11.79 11.91 11.92 11.99 12.00 12.01 12.02

12.11 12.12 12.121 12.122 12.13 12.14 12.141 12.21

12.22 12.29 12.31 12.32 12.33 12.34 12.35 12.39

12.40 12.41 12.42 12.43 12.44 12.442 12.51 12.52

12.53 12.54 12.55 12.59 12.61 12.62 12.63 12.64

12.65 12.66 12.69 12.71 12.72 12.73 12.74 12.79

12.81 12.82 12.83 12.84 12.85 12.86 12.87 12.88

12.89 12.891 12.91 12.92 12.921 12.93 12.97 12.98

12.99 13.00 13.01 13.02 13.11 13.19 13.2 13.3

13.41 13.42 13.43 13.51 13.59 13.61 13.62 13.63

13.64 13.65 13.66 13.69 13.70 13.71 13.72 13.8

13.9 14.00 14.01 14.02 14.11 14.19 14.21 14.22

14.23 14.24 14.25 14.26 14.27 14.29 14.31 14.32

14.33 14.34 14.35 14.39 14.41 14.411 14.49 14.491

14.51 14.52 14.53 14.54 14.55 14.59 14.6 14.71

14.72 14.73 14.74 14.75 14.79 14.9 15.01 15.09

15.11 15.12 15.13 15.19 15.21 15.22 15.29 15.3

15.31 15.32 15.33 15.4 15.5 15.6 15.7 15.9

16.01 16.02 16.09 16.1 16.21 16.22 16.23 16.29

16.31 16.39 16.41 16.42 16.49 16.51 16.52 16.59

16.61 16.62 16.63 16.64 16.65 16.66 16.69 16.71

16.72 16.81 16.82 16.89 16.91 16.92 16.93 16.98

16.99 20.21 20.22 20.23 20.32 20.39 20.41 20.42

20.49 20.491 20.51 20.59 20.61 20.62 20.71 20.72

20.721 20.79 20.791 20.792 20.793 20.794 20.795 20.8

20.91 20.92 20.921 20.93 20.94 20.95 20.96 20.97

20.98 20.99 21.00 21.03 21.04 21.05 21.06 21.07

21.09 21.1 21.12 21.22 21.29 21.4 21.5 21.61

21.62 21.69 21.71 21.72 21.81 21.82 21.83 21.84

21.85 21.86 21.87 21.88 21.89 21.91 21.99 22.00

22.12 22.2 22.31 22.39 22.41 22.42 22.421 22.50

22.51 22.52 22.53 22.60 22.61 22.62 22.621 22.63

22.631 22.632 22.633 22.64 22.71 22.79 22.9 23.01

23.09 23.11 23.19 23.2 23.3 23.41 23.42 23.43

23.49 23.5 23.6 23.70 23.71 23.72 23.73 24.0

24.2 24.31 24.311 24.32 24.39 24.4 24.5 24.91

24.99 25.02 25.1 25.2 25.3 25.4 25.59 25.591

25.93 25.94 25.99 26.0 26.12 26.19 26.21 26.29

26.30 26.31 26.311 26.312 26.313 26.32 26.321 26.322

26.323 26.41 26.42 26.49 26.99 27.0 27.1 27.31

27.311 27.312 27.32 27.321 27.42 27.43 27.431 27.432

27.49 27.491 27.492 27.51 27.53 27.54 27.55 27.56

27.561 27.57 27.59 27.61 27.62 27.63 27.69 27.71

27.72 27.721 27.73 27.79 27.92 27.99 28.0 28.19

28.2 28.21 28.3 28.31 28.4 28.5 28.51 28.6

28.7 28.91 28.92 28.99 29.0 29.12 29.19 29.2

29.3 29.31 29.32 29.33 29.39 29.4 29.51 29.52

29.53 29.54 29.59 29.91 29.92 29.99 30.01 30.09

30.1 30.21 30.22 30.29 30.291 30.292 30.293 30.3

30.4 31.0 31.1 31.21 31.29 31.3 31.31 31.32

31.42 31.43 31.44 31.45 31.48 31.49 31.5 31.51

31.61 31.62 31.63 31.64 31.69 31.71 31.72 31.73

31.74 31.75 31.79 31.91 31.92 31.93 31.94 31.95

31.98 31.99 32.0 32.01 32.09 32.1 32.21 32.28

32.29 32.291 32.3 32.4 32.41 32.5 32.6 32.9

33.0 33.1 33.22 33.23 33.24 33.25 33.27 33.28

33.29 33.31 33.32 33.33 33.34 33.39 33.41 33.42

33.43 33.48 33.481 33.49 33.5 33.6 33.91 33.92

33.93 33.98 33.99 34.01 34.02 34.03 34.031 34.04

34.09 34.091 34.092 34.1 34.11 34.12 34.21 34.22

34.23 34.24 34.26 34.27 34.28 34.29 34.3 34.4

34.41 34.42 34.51 34.59 34.591 34.592 34.6 34.71

34.72 34.73 34.74 34.79 34.791 34.81 34.82 34.83

34.84 34.85 34.89 34.93 34.99 35.00 35.01 35.02

35.03 35.04 35.10 35.11 35.12 35.13 35.14 35.20

35.21 35.22 35.23 35.24 35.25 35.26 35.27 35.28

35.31 35.32 35.33 35.34 35.35 35.39 35.41 35.42

35.50 35.51 35.52 35.53 35.531 35.54 35.60 35.61

35.62 35.621 35.63 35.70 35.71 35.72 35.73 35.81

35.82 35.83 35.84 35.91 35.92 35.93 35.94 35.95

35.96 35.98 35.99 36.0 36.00 36.03 36.04 36.09

36.10 36.11 36.12 36.13 36.14 36.15 36.16 36.19

36.2 36.3 36.91 36.99 37.0 37.10 37.11 37.12

37.24 37.25 37.26 37.27 37.29 37.31 37.32 37.321

37.33 37.331 37.34 37.4 37.5 37.62 37.63 37.64

37.70 37.74 37.75 37.80 37.81 37.82 37.83 37.84

37.85 37.853 37.854 37.86 37.87 37.89 37.99 37.991

38.00 38.01 38.02 38.021 38.022 38.03 38.031 38.04

38.05 38.06 38.061 38.07 38.08 38.09 38.091 38.10

38.11 38.12 38.121 38.122 38.13 38.14 38.15 38.16

38.161 38.18 38.181 38.182 38.21 38.22 38.29 38.30

38.31 38.311 38.32 38.321 38.33 38.34 38.341 38.342

38.35 38.36 38.361 38.362 38.37 38.38 38.381 38.382

38.39 38.40 38.41 38.411 38.42 38.422 38.43 38.44

38.441 38.45 38.46 38.47 38.48 38.49 38.50 38.51

38.52 38.53 38.55 38.57 38.59 38.60 38.61 38.611

38.62 38.621 38.622 38.63 38.64 38.641 38.642 38.65

38.66 38.661 38.662 38.67 38.68 38.681 38.682 38.69

38.7 38.80 38.81 38.82 38.821 38.822 38.83 38.84

38.85 38.851 38.86 38.87 38.88 38.89 39.0 39.1

39.11 39.21 39.22 39.23 39.24 39.25 39.251 39.252

39.26 39.27 39.28 39.29 39.291 39.292 39.293 39.294

39.295 39.30 39.31 39.311 39.32 39.41 39.42 39.43

39.49 39.51 39.511 39.512 39.52 39.521 39.522 39.523

39.53 39.531 39.532 39.54 39.55 39.56 39.561 39.57

39.571 39.58 39.59 39.7 39.8 39.81 39.91 39.93

39.94 39.96 39.97 39.98 39.981 39.99 40.0 40.11

40.111 40.112 40.19 40.21 40.22 40.23 40.24 40.29

40.3 40.40 40.401 40.41 40.42 40.50 40.51 40.52

40.53 40.54 40.59 40.61 40.62 40.63 40.64 40.69

40.9 41.0 41.00 41.01 41.02 41.03 41.1 41.2

41.33 41.38 41.39 41.41 41.42 41.43 41.5 41.91

41.92 41.93 41.94 41.95 41.98 41.99 42.01 42.09

42.091 42.10 42.11 42.12 42.19 42.21 42.23 42.231

42.24 42.25 42.29 42.31 42.32 42.321 42.33 42.39

42.40 42.41 42.411 42.42 42.421 42.51 42.52 42.53

42.54 42.55 42.56 42.58 42.59 42.61 42.62 42.63

42.64 42.65 42.66 42.68 42.69 42.7 42.81 42.82

42.83 42.84 42.85 42.86 42.87 42.89 42.91 42.92

42.99 43.0 43.01 43.1 43.11 43.19 43.2 43.3

43.41 43.42 43.421 43.49 43.5 43.6 43.7 43.81

43.89 43.91 43.99 44.00 44.01 44.02 44.03 44.11

44.13 44.131 44.14 44.15 44.19 44.2 44.21 44.22

44.29 44.31 44.39 44.392 44.393 44.40 44.41 44.42

44.43 44.44 44.49 44.5 44.61 44.62 44.63 44.64

44.65 44.66 44.69 44.691 44.91 44.92 44.99 45.00

45.01 45.02 45.03 45.11 45.13 45.14 45.141 45.15

45.151 45.16 45.19 45.21 45.26 45.261 45.27 45.28

45.29 45.30 45.31 45.32 45.33 45.331 45.34 45.41

45.49 45.50 45.51 45.52 45.61 45.62 45.63 45.71

45.72 45.73 45.74 45.75 45.76 45.79 45.8 45.90

45.91 45.92 45.93 45.94 45.95 46.01 46.02 46.03

46.04 46.10 46.11 46.12 46.13 46.14 46.20 46.21

46.22 46.23 46.24 46.31 46.32 46.39 46.391 46.40

46.41 46.411 46.42 46.43 46.50 46.51 46.52 46.60

46.61 46.62 46.63 46.64 46.71 46.72 46.73 46.74

46.75 46.76 46.79 46.791 46.80 46.81 46.811 46.812

46.82 46.821 46.822 46.85 46.91 46.92 46.93 46.931

46.94 46.99 47.0 47.1 47.2 47.91 47.92 47.99

48.0 48.01 48.02 48.1 48.21 48.25 48.26 48.29

48.31 48.311 48.32 48.321 48.33 48.331 48.34 48.341

48.35 48.351 48.352 48.353 48.41 48.49 48.5 48.61

48.62 48.63 48.64 48.65 48.66 48.69 48.71 48.72

48.73 48.731 48.732 48.74 48.75 48.76 48.79 48.81

48.811 48.82 48.91 48.92 48.93 48.99 49.01 49.02

49.03 49.04 49.11 49.12 49.43 49.44 49.45 49.46

49.47 49.49 49.51 49.52 49.59 49.6 49.71 49.72

49.73 49.74 49.79 49.91 49.92 49.93 49.94 49.95

49.99 50.0 50.12 50.121 50.19 50.21 50.211 50.22

50.29 50.3 50.4 50.51 50.59 50.61 50.69 50.91

50.92 50.93 50.94 50.99 51.02 51.03 51.04 51.10

51.11 51.13 51.14 51.15 51.19 51.21 51.22 51.23

51.31 51.32 51.33 51.34 51.35 51.36 51.361 51.37

51.39 51.41 51.42 51.43 51.49 51.51 51.59 51.61

51.62 51.63 51.64 51.69 51.71 51.72 51.79 51.81

51.82 51.821 51.83 51.84 51.85 51.86 51.87 51.88

51.89 51.91 51.92 51.93 51.94 51.95 51.96 51.97

51.98 51.99 52.01 52.09 52.091 52.12 52.13 52.14

52.19 52.2 52.21 52.22 52.3 52.4 52.51 52.52

52.53 52.59 52.6 52.7 52.80 52.81 52.82 52.83

52.91 52.92 52.93 52.94 52.95 52.951 52.96 52.961

52.97 52.98 52.99 53.00 53.001 53.01 53.011 53.02

53.021 53.03 53.031 53.04 53.041 53.05 53.10 53.11

53.111 53.12 53.121 53.13 53.131 53.14 53.141 53.15

53.151 53.16 53.161 53.17 53.21 53.211 53.29 53.291

53.31 53.311 53.39 53.391 53.41 53.49 53.51 53.59

53.591 53.592 53.61 53.69 53.691 53.692 53.7 53.80

53.81 53.82 53.9 53.91 53.92 54.0 54.11 54.12

54.19 54.21 54.22 54.23 54.29 54.3 54.31 54.4

54.41 54.5 54.51 54.61 54.62 54.63 54.631 54.64

54.641 54.71 54.72 54.73 54.731 54.74 54.75 54.751

54.92 54.93 54.94 54.95 54.99 55.01 55.011 55.02

55.03 55.04 55.11 55.111 55.12 55.21 55.22 55.24

55.29 55.31 55.39 55.4 55.5 55.501 55.51 55.52

55.53 55.532 55.54 55.61 55.69 55.691 55.692 55.7

55.81 55.82 55.83 55.84 55.85 55.86 55.87 55.89

55.91 55.96 55.97 55.98 55.99 56.0 56.01 56.1

56.2 56.21 56.31 56.32 56.34 56.35 56.39 56.40

56.41 56.42 56.51 56.52 56.61 56.611 56.62 56.71

56.711 56.72 56.73 56.74 56.75 56.79 56.791 56.81

56.82 56.83 56.84 56.85 56.86 56.89 56.891 56.91

56.911 56.92 56.93 56.94 56.95 56.99 57.0 57.12

57.18 57.19 57.191 57.192 57.21 57.22 57.34 57.39

57.41 57.49 57.491 57.492 57.493 57.51 57.59 57.591

57.592 57.6 57.71 57.79 57.81 57.82 57.83 57.831

57.84 57.841 57.85 57.86 57.87 57.88 57.881 57.89

57.91 57.93 57.96 57.97 57.98 57.99 58.0 58.22

58.23 58.231 58.24 58.29 58.3 58.31 58.32 58.39

58.41 58.42 58.43 58.431 58.44 58.45 58.46 58.47

58.49 58.491 58.5 58.91 58.92 58.93 58.99 59.00

59.01 59.02 59.021 59.09 59.11 59.19 59.191 59.21

59.211 59.29 59.3 59.4 59.5 59.6 59.71 59.79

59.8 59.81 59.91 59.911 59.92 59.99 60.0 60.01

60.12 60.14 60.15 60.18 60.19 60.2 60.3 60.4

60.41 60.5 60.52 60.53 60.61 60.62 60.621 60.69

60.72 60.73 60.79 60.81 60.82 60.91 60.93 60.94

60.95 60.99 61.0 61.01 61.2 61.3 61.31 61.42

61.49 61.491 61.92 61.921 61.99 62.0 62.01 62.12

62.19 62.2 62.3 62.41 62.42 62.5 62.61 62.69

62.7 62.91 62.92 62.99 63.01 63.011 63.09 63.1

63.11 63.2 63.3 63.31 63.4 63.51 63.52 63.53

63.59 63.6 63.81 63.82 63.821 63.83 63.84 63.85

63.89 63.92 63.93 63.94 63.95 63.99 64.0 64.19

64.2 64.3 64.31 64.41 64.42 64.43 64.44 64.45

64.49 64.5 64.92 64.93 64.95 64.96 64.97 64.98

64.99 65.0 65.11 65.12 65.19 65.21 65.22 65.29

65.3 65.4 65.51 65.52 65.61 65.62 65.71 65.72

65.73 65.79 65.8 65.91 65.92 65.93 65.94 65.95

65.99 66.0 66.01 66.02 66.11 66.19 66.21 66.22

66.29 66.31 66.32 66.39 66.4 66.51 66.52 66.61

66.62 66.63 66.69 66.71 66.72 66.73 66.74 66.79

66.91 66.92 66.93 66.94 66.95 66.96 66.97 66.99

67.0 67.2 67.31 67.32 67.33 67.39 67.4 67.5

67.62 67.69 68.0 68.13 68.14 68.15 68.16 68.19

68.21 68.22 68.29 68.3 68.4 68.5 68.6 68.7

68.8 68.9 69.01 69.02 69.09 69.11 69.19 69.21

69.22 69.23 69.29 69.3 69.41 69.42 69.49 69.51

69.52 69.59 69.91 69.95 69.98 69.99 70.0 70.12

70.13 70.14 70.32 70.33 70.4 70.50 70.51 70.52

70.61 70.62 70.71 70.72 70.73 70.74 70.75 70.77

70.79 70.8 70.91 70.92 71.01 71.09 71.19 71.22

71.23 71.24 71.29 71.3 71.4 71.5 71.61 71.62

71.71 71.72 71.79 71.8 71.9 72.0 72.1 72.21

72.29 72.31 72.39 72.4 72.51 72.52 72.53 72.54

72.6 72.71 72.79 72.8 72.9 73.1 73.21 73.22

73.8 73.91 73.92 73.93 73.94 73.99 74.0 74.1

74.2 74.3 74.4 74.91 74.99 75.0 75.31 75.35

75.36 75.4 75.50 75.52 75.61 75.69 75.7 75.8

75.91 75.92 75.93 75.94 75.99 76.01 76.09 76.091

76.11 76.19 76.2 76.31 76.39 76.391 76.41 76.42

76.43 76.44 76.45 76.451 76.452 76.46 76.5 76.51

76.61 76.62 76.63 76.64 76.641 76.65 76.66 76.67

76.68 76.69 76.70 76.71 76.711 76.712 76.72 76.721

76.722 76.73 76.731 76.732 76.733 76.74 76.741 76.742

76.743 76.75 76.76 76.77 76.78 76.781 76.79 76.791

76.91 76.92 76.93 76.94 76.95 76.97 76.99 77.00

77.01 77.02 77.03 77.04 77.05 77.06 77.07 77.08

77.09 77.10 77.11 77.12 77.13 77.14 77.15 77.16

77.17 77.18 77.19 77.20 77.21 77.22 77.23 77.24

77.25 77.26 77.27 77.28 77.29 77.30 77.31 77.311

77.32 77.321 77.33 77.331 77.34 77.341 77.35 77.351

77.36 77.37 77.371 77.38 77.381 77.39 77.391 77.40

77.41 77.42 77.43 77.44 77.45 77.46 77.47 77.48

77.49 77.51 77.52 77.53 77.54 77.56 77.57 77.58

77.59 77.60 77.61 77.611 77.62 77.621 77.63 77.631

77.64 77.641 77.65 77.651 77.66 77.661 77.67 77.671

77.68 77.681 77.69 77.70 77.71 77.72 77.73 77.74

77.75 77.76 77.77 77.78 77.79 77.80 77.81 77.82

77.83 77.84 77.85 77.86 77.87 77.88 77.89 77.894

77.90 77.91 77.911 77.912 77.92 77.93 77.94 77.95

77.96 77.97 77.98 77.99 78.00 78.01 78.010 78.011

78.012 78.013 78.014 78.015 78.02 78.020 78.021 78.022

78.023 78.024 78.025 78.03 78.030 78.031 78.032 78.033

78.034 78.035 78.04 78.040 78.041 78.042 78.043 78.044

78.045 78.05 78.050 78.051 78.052 78.053 78.054 78.055

78.06 78.060 78.061 78.062 78.063 78.064 78.065 78.07

78.070 78.071 78.072 78.073 78.074 78.075 78.08 78.080

78.081 78.082 78.083 78.084 78.085 78.09 78.090 78.091

78.092 78.093 78.094 78.095 78.10 78.11 78.12 78.13

78.14 78.15 78.16 78.17 78.18 78.19 78.20 78.22

78.23 78.24 78.25 78.27 78.28 78.29 78.30 78.31

78.32 78.33 78.34 78.35 78.37 78.38 78.39 78.40

78.41 78.42 78.43 78.44 78.45 78.46 78.47 78.48

78.49 78.50 78.51 78.52 78.53 78.54 78.55 78.56

78.57 78.58 78.59 78.60 78.61 78.62 78.63 78.64

78.65 78.66 78.67 78.68 78.69 78.70 78.71 78.72

78.73 78.74 78.75 78.76 78.77 78.78 78.79 78.80

78.81 78.82 78.83 78.84 78.85 78.86 78.87 78.88

78.89 78.90 78.91 78.92 78.93 78.94 78.95 78.96

78.97 78.98 78.99 79.00 79.01 79.02 79.05 79.06

79.061 79.07 79.09 79.091 79.093 79.10 79.11 79.12

79.13 79.14 79.15 79.151 79.16 79.161 79.17 79.18

79.19 79.191 79.193 79.20 79.21 79.22 79.23 79.24

79.25 79.26 79.27 79.28 79.29 79.30 79.31 79.32

79.33 79.34 79.35 79.351 79.352 79.353 79.354 79.36

79.361 79.362 79.363 79.37 79.38 79.39 79.391 79.393

79.40 79.41 79.42 79.45 79.46 79.49 79.50 79.51

79.52 79.55 79.56 79.59 79.60 79.61 79.62 79.63

79.64 79.65 79.66 79.67 79.68 79.69 79.70 79.71

79.72 79.75 79.76 79.77 79.79 79.791 79.793 79.80

79.81 79.82 79.83 79.84 79.85 79.86 79.87 79.88

79.89 79.891 79.893 79.90 79.91 79.92 79.93 79.94

79.95 79.96 79.97 79.98 79.99 80.00 80.01 80.02

80.03 80.04 80.05 80.06 80.07 80.08 80.09 80.10

80.11 80.112 80.12 80.122 80.13 80.132 80.14 80.142

80.15 80.152 80.16 80.162 80.17 80.172 80.18 80.182

80.19 80.40 80.41 80.42 80.43 80.44 80.45 80.46

80.47 80.48 80.49 80.5 80.50 80.51 80.52 80.59

80.6 80.70 80.71 80.72 80.73 80.74 80.75 80.76

80.77 80.78 80.79 80.80 80.81 80.82 80.83 80.84

80.85 80.86 80.87 80.88 80.89 80.90 80.91 80.92

80.93 80.94 80.95 80.96 80.97 80.98 80.99 81.00

81.01 81.02 81.021 81.03 81.031 81.04 81.05 81.06

81.061 81.07 81.071 81.08 81.09 81.11 81.12 81.13

81.14 81.15 81.16 81.17 81.171 81.18 81.20 81.21

81.22 81.23 81.24 81.25 81.26 81.27 81.28 81.29

81.31 81.39 81.40 81.41 81.412 81.413 81.42 81.43

81.44 81.45 81.46 81.47 81.472 81.48 81.49 81.51

81.52 81.53 81.54 81.55 81.56 81.57 81.59 81.61

81.62 81.622 81.63 81.64 81.642 81.69 81.71 81.72

81.73 81.74 81.75 81.79 81.80 81.81 81.812 81.82

81.83 81.832 81.84 81.85 81.852 81.86 81.87 81.93

81.932 81.933 81.934 81.935 81.94 81.95 81.955 81.96

81.97 81.98 81.99 82.01 82.02 82.03 82.04 82.09

82.11 82.12 82.19 82.21 82.22 82.29 82.31 82.32

82.33 82.34 82.35 82.36 82.39 82.41 82.42 82.43

82.44 82.45 82.46 82.51 82.52 82.53 82.54 82.55

82.56 82.57 82.58 82.59 82.61 82.69 82.71 82.72

82.79 82.81 82.82 82.83 82.84 82.85 82.86 82.89

82.91 82.92 82.93 82.94 82.95 82.96 82.99 83.01

83.011 83.02 83.03 83.09 83.11 83.12 83.13 83.14

83.19 83.191 83.21 83.211 83.212 83.213 83.29 83.31

83.32 83.321 83.39 83.391 83.41 83.42 83.43 83.431

83.44 83.45 83.49 83.5 83.61 83.62 83.63 83.64

83.65 83.651 83.71 83.72 83.73 83.74 83.75 83.76

83.77 83.79 83.81 83.82 83.821 83.83 83.84 83.85

83.851 83.86 83.87 83.88 83.89 83.91 83.92 83.93

83.94 83.95 83.99 83.991 83.992 83.993 84.00 84.01

84.011 84.02 84.021 84.03 84.04 84.05 84.06 84.07

84.08 84.09 84.10 84.11 84.111 84.12 84.13 84.14

84.15 84.16 84.17 84.18 84.19 84.21 84.22 84.23

84.24 84.25 84.26 84.27 84.28 84.29 84.3 84.31

84.40 84.44 84.91 84.92 84.93 84.99 85.0 85.01

85.12 85.19 85.20 85.21 85.22 85.23 85.24 85.25

85.31 85.32 85.33 85.34 85.35 85.36 85.41 85.42

85.43 85.44 85.45 85.46 85.47 85.48 85.50 85.53

85.54 85.6 85.7 85.81 85.82 85.83 85.84 85.85

85.86 85.87 85.89 85.91 85.92 85.93 85.94 85.95

85.96 85.99 86.03 86.05 86.06 86.07 86.09 86.21

86.211 86.22 86.4 86.41 86.42 86.51 86.59 86.60

86.61 86.62 86.63 86.64 86.65 86.66 86.69 86.691

86.70 86.71 86.72 86.721 86.722 86.723 86.724 86.725

86.73 86.74 86.741 86.742 86.743 86.744 86.745 86.75

86.751 86.752 86.753 86.754 86.755 86.756 86.81 86.82

86.83 86.84 86.841 86.842 86.843 86.85 86.86 86.89

86.891 86.892 86.893 86.91 86.93 86.99 93.26 94.26

94.27 98.51 98.52 98.59

2644 ICD-9-CM Procedure Codes loaded.

Loading: TR-8 PROC GROUP

Working

39.31 39.32 39.56 39.57 41.43 41.5 41.95 41.99

44.61 46.71 46.73 50.22 50.3 50.4 50.61 50.69

52.95 54.11 54.92 55.4 55.5 55.81 55.82 57.79

24 ICD-9-CM Procedure Codes loaded.

Loading: TR-10 PROC GROUP

Working

79.15 79.35

2 ICD-9-CM Procedure Codes loaded.

Loading: TR-11 PROC GROUP

Working

02.02 38.06 38.07 38.44 38.46 38.47 38.7 38.84

38.86 38.87 39.1 39.24 39.25 39.26 39.29 39.30

39.31 39.311 39.32 39.56 39.57 39.58 44.49 44.61

46.10 46.20 46.21 46.73 46.75 50.22 50.4 51.71

51.79 51.91 52.6 52.95 54.11 54.19 54.3 54.74

54.75 54.91 54.92 55.4 55.5 55.81 56.82 32.3

32.4 33.41 33.42 33.43 33.48 33.481 33.49 34.01

34.91 34.93 38.85 39.21 39.22 39.30 39.31 39.311

39.32 39.56 39.57 39.58 37.0 37.12 37.4 34.02

38.04 38.34 38.35 38.84 38.85 39.57 39.58 54.11

33.41 33.42 33.43 33.48 33.481 33.49 34.01 34.02

34.04 34.09 34.71 34.91 34.92 34.93

94 ICD-9-CM Procedure Codes loaded.

Loading: CV-4 PROC GROUP

Working

36.10 36.11 36.12 36.13 36.14 36.15 36.16 36.19

36.01 36.02 36.09

11 ICD-9-CM Procedure Codes loaded.

Creating the QM User and Manager Menus...............

Installation of Clinical Monitoring System Version 1.0 complete!

\>

# # Implementation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do the following after installation of the software.

- 1. Read the Introduction, Orientation, and Package Management sections of the User Manual. Also acquaint yourself with the following chapters in the ADPAC Guide: Functional Flow, Conditions, Groups, Data Elements, and Appendix B. This should give you sufficient background to understand what this software is about.
- 2. Using the TaskManager *Schedule/Unschedule Options* option, queue the automatic enrollment option *QAM TASKED AUTO ENROLL RUN* to run daily after midnight. This task scans the database for activities from the previous day.
- 3. Define the site parameters via the *Site Parameters Edit* option. See the Site Parameters Edit option documentation in this manual for step-by-step instruction.
- 4. Use the *Application Group Edit* option to add the desired files to the QAM application group. This step is necessary before any groups can be created from those files via the *Group Edit* option. A default list of files is included in this option. It is suggested that they be loaded. See the *Application Group Edit* option documentation in this manual for more detail.
- 5. The following software is used by CMS. To capture patients with the conditions MH Seclusion/Restraint or RXS 2+ Drugs in the Same Class, the Mental Health or Outpatient Pharmacy software must be running and routinely used. If a condition is chosen that looks at a non-existent file (say Mental Health), the user will be beeped. If the file is there but empty, meaning the site is not using the software or entering data into the file, no fall outs will result.

> VA FileMan Version 19 or later

> MAS Version 5.2 or later (includes PTF and Scheduling)

> Kernel Version 7.0 or later

> Lab Version 5.1 or later

> Mental Health Version 4.18 or later

> Outpatient Pharmacy Version 5.5 or later

- 6. With the assistance of the QM ADPAC, assign the menus to users. We suggest limiting the number of users given the Manager Menu to those with a good VA FileMan and VistA background. They should also have had some experience designing QM indicators of care. The Monitoring System Manager Menu is usually given only to the QM ADPAC. The Monitoring System Programmer Menu should be assigned to the IRM support person for the Clinical Monitoring System. This may vary with the site. There are no security keys to take into consideration at this time.
- 7. Ask the users to define the mail group(s) that will receive bulletins from the active monitors. Mail groups will depend largely on who the users are. (The mail groups must be PUBLIC, not PRIVATE.)

# Monitoring System Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Site Parameters Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the parameters which may be edited through the Site Parameters Edit option.

DAY WEEKLY TIME FRAME BEGINS

This is the day of the week that should begin each weekly time frame. Generally, this would be Sunday but could be Monday since that is considered a regular work day.

MONITORING SYSTEM DEVICE

The device on which auto enroll reports will print.

ALLOW USE OF ‘\[‘ IN GROUP EDIT

If this field is set to YES the user may enter \[GROUP MEMBER at the

Select GROUP MEMBER prompt to select all entries that contain the text

GROUP MEMBER as part of their name.

The following three fields control the manual run of auto enroll.

MAX DAYS PER MANUAL AUTO RUN

This field contains the maximum number of auto enroll runs that may be run consecutively.

TIME BETWEEN MANUAL AUTO RUNS

This field contains the number of minutes between queued runs of auto enroll. This parameter, together with the MAX DAYS PER MANUAL AUTO RUN parameter, is used to tightly control the use of computer resources that auto enroll processing uses.

MANUAL AUTO RUN ALLOWED TIMES

This field contains the range of time during which auto enroll may be manually queued to run. The format is HHMM-HHMM, where HH = hours and MM = minutes. The second time must be greater than the first.

## Application Group Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Group Edit option is utilized (on setup) to select files from which the user can build groups through the Group Edit option. The Clinical Monitoring System software comes with a set of default files which should be added to the QAM application group. The user can only create groups from files that are in the QAM application group.

This option also allows the programmer to add/delete files from the QAM application group at times other than setup.

Checking the QAM application group.........

Select FILE: ?

Enter a file name/number to add a file to the list

Enter a minus (-) file name/number to remove a file from the list

Files selected for LOADING:

2 PATIENT (Not Loaded)

37 DISPOSITION (Not Loaded)

42 WARD LOCATION (Not Loaded)

44 HOSPITAL LOCATION (Not Loaded)

45.7 FACILITY TREATING SPECIALTY (Not Loaded)

49 SERVICE/SECTION (Not Loaded)

80 ICD DIAGNOSES (Not Loaded)

80.1 ICD OPERATION/PROCEDURE (Not Loaded)

405.2 MAS MOVEMENT TYPE (Not Loaded)

405.3 MAS MOVEMENT TRANSACTION TYPE (Not Loaded)

409.1 APPOINTMENT TYPE (Not Loaded)

615.5 S/R REASON (Not Loaded)

615.6 S/R CATEGORY (Not Loaded)

743 QA MONITOR (Not Loaded)

Files selected for UNLOADING:

\*\*\* None \*\*\*

Select FILE: \<RET\>

Load / Unload application groups? NO// YESApplication Group Edit Option

Loading:

2 PATIENT

37 DISPOSITION

42 WARD LOCATION

44 HOSPITAL LOCATION

45.7 FACILITY TREATING SPECIALTY

49 SERVICE/SECTION

80 ICD DIAGNOSES

80.1 ICD OPERATION/PROCEDURE

405.2 MAS MOVEMENT TYPE

405.3 MAS MOVEMENT TRANSACTION TYPE

409.1 APPOINTMENT TYPE

615.5 S/R REASON

615.6 S/R CATEGORY

743 QA MONITOR

Unloading:

\*\*\* Finished \*\*\*