---
title: IVMB*2*491 Purple Heart Phase 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Purple Heart Phase 1
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*491
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Installation Instructions](#installation-instructions) - [Associated Patch](#associated-patch) - [Patch Dependencies](#patch-dependencies) - [Install Patch IVMB\2.0\491](#install-patch-ivmb20491) - [Schedule the Purple Heart Background Processor](#schedule-the-purple-heart-background-processor)
audience: 
keywords: 
  - table
  - patch
  - purple
  - heart
  - press
  - contents
  - schedule
  - installation
  - access
  - database
page_count: 0
word_count: 1671
section_count: 8
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ph_ivmb_2_491_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ph_ivmb_2_491_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-491-purple-heart-phase-1-installation-guide/001.png)

Purple Heart

Installation Guide

Health Eligibility Center (HEC)  
Module

Patch IVMB\*2.0\*491

March 2001

*VISTA* Technical Services
# # Installation Instructions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Installation Instructions](#installation-instructions)
  - [Associated Patch](#associated-patch)
  - [Patch Dependencies](#patch-dependencies)
  - [Install Patch IVMB\2.0\491](#install-patch-ivmb20491)
  - [Schedule the Purple Heart Background Processor](#schedule-the-purple-heart-background-processor)
  - [Schedule the Daily Purple Heart Status Report](#schedule-the-daily-purple-heart-status-report)
- [Post-Installation Instructions](#post-installation-instructions)
  - [MUMPS Database Conversion Instructions](#mumps-database-conversion-instructions)
  - [Access Database Conversion Instructions](#access-database-conversion-instructions)
    - [Export the Access Data to a Delimited Text File](#export-the-access-data-to-a-delimited-text-file)
    - [Converting the Access data to the MUMPS System](#converting-the-access-data-to-the-mumps-system)
This patch can be loaded with users on the system. Installation will take less than 10 minutes.
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Warnings</strong></td>
<td><p>After patch IVMB*2.0*491 is installed, KIDS will attempt to rebuild all user menus, which could be a lengthy (several hour) process. If you are running the installation interactively, you will be prompted to specify a start time for the menu rebuild. If installation is not being run interactively, KIDS will start the menu rebuild immediately after the installation completes. To avoid inconveniencing system users, you should consider scheduling the installation to run at a time of low system activity.</p>
<p>In order to ensure that Purple Heart data are transferred to the National Enrollment Database (NED), patch IVMB*2.0*537 must be installed immediately after this patch and before the Purple Heart Background Processor is scheduled and the database conversions are run.</p></td>
</tr>
</tbody>
</table>
Installation has three components, install the patch, schedule the Purple Heart Background Processor, and schedule the Daily Purple Heart Status report.

## Associated Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IVMB\*2.0\*537 must be installed immediately after this patch and before the Purple Heart Background Processor is scheduled and the database conversions are run.

## Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches are required to be installed prior to installing this patch at the HEC:

- IVME\*1\*15
- IVMB\*2\*248
- IVMB\*2\*455
- IVMB\*2\*487
- IVMB\*2\*501

## Install Patch IVMB\*2.0\*491

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Disable user access to the "Class 3" Purple Heart Database options and the Purple Heart Access database application.
2.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu  
    \[Note: TEXT PRINT/DISPLAY option in the PackMan menu will display the patch text only\].
3.  Review your mapped set. If any of the routines listed in the ROUTINE SUMMARY section are mapped, they should be removed from the mapped set at this time.
4.  To avoid missing HL7 traffic while the patch is being installed, place TaskMan in WAIT state.
5.  From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.
6.  From Installation menu, you may elect to use the following options: (when prompted for INSTALL NAME, enter IVMB\*2.0\*491)
    1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - this option will allow you to ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
7.  Use the Install Package(s) option and select the package IVMB\*2.0\*491.
8.  Respond to the installation questions as follows:

|                                                                       |              |
|-----------------------------------------------------------------------|--------------|
| Question                                                          | Response |
| Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//     | YES      |
| Want KIDS to INHIBIT LOGINs during the install? YES//                 | YES      |
| Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// | NO       |

9.  If routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has competed.

To ensure that Purple Heart data is transferred to the National Enrollment Database, make sure that patch IVMB\*2.0\*537 is installed before proceeding to the next step.

## Schedule the Purple Heart Background Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Schedule the AYCEPH BACKGROUND PROCESSOR menu option in TaskMan using the following instructions.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Warnings</strong></td>
<td><p>Ensure that patch IVMB*2.0*537 has been successfully installed prior to starting the Purple Heart Background Processor is scheduled. If this step is not taken, Purple Heart data will not be transferred to the National Enrollment Database.</p>
<p>To ensure proper processing, the AYCEPH BACKGROUND PROCESSOR option must be tasked to run after PH Processing has completed for the day but BEFORE Midnight.</p></td>
</tr>
</tbody>
</table>

1.  Ensure that Patch IVMB\*2.0\*537 has been installed an is operating properly.
2.  From the TaskMan Management menu, select Schedule/Unschedule Options.
10. At the Select OPTION to schedule or reschedule: prompt, type AYCEPH BACKGROUND PROCESSOR and press \<Enter\>.
11. At the OK? Yes// prompt, press \<Enter\> to respond YES. The Edit Option Schedule screen appears.
12. Press the tab key until the QUEUED TO RUN AT WHAT TIME: field is highlighted. Type in an appropriate start date and time (11:00 <span class="smallcaps">p.m</span>. is suggested) and press \<Enter\>.
13. Press the tab key until the RESCHEDULING FREQUENCY: field is highlighted. Type in 1D and press \<Enter\> to schedule the frequency as daily.
14. Press the tab key until the COMMAND: field is highlighted. Type SAVE and press \<Enter\>.
15. With the COMMAND field still highlighted, type EXIT and press \<Enter\>.

## Schedule the Daily Purple Heart Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To schedule the Daily Purple Heart Status report

1.  From the TaskMan Management menu, select Schedule/Unschedule Options.
16. At the Select OPTION to schedule or reschedule: prompt, type DAILY PH STATUS REPORT and press \<Enter\>.
17. At the OK? Yes// prompt, press \<Enter\> to respond YES. The Edit Option Schedule screen appears.
18. Press the tab key until the QUEUED TO RUN AT WHAT TIME: field is highlighted. Type in an appropriate start date and time (5:00 <span class="smallcaps">a.m</span>. is suggested) and press \<Enter\>.
19. Press the tab key until the RESCHEDULING FREQUENCY: field is highlighted. Type in 1D and press \<Enter\> to schedule the frequency as daily.
20. Press the tab key until the COMMAND: field is highlighted. Type SAVE and press \<Enter\>.
21. With the COMMAND field still highlighted, type EXIT and press \<Enter\>.

# Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Warning | Patch IVMB\*2\*537 must be installed immediately following the installation of IVMB\*2\*491, and prior to running the database conversions: |

|                    |                                                                                                                                                                                                                                                                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Important Note | The process to update veteran records with Purple Heart information will generate Z11 HL7 messages to be sent to the VAMC sites of record for each veteran. To minimize the impact of this increased interface traffic on the local VAMC systems, it is recommended that the database conversion processes be started after close of business on a Friday. |

## MUMPS Database Conversion Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Warnings</strong></td>
<td><ul>
<li><p>If this process is run before all Phase 1 and 2 Purple Heart patches have been installed both on the HEC and at all of the VAMCs, Purple Heart data will not be distributed correctly to all sites of record and other errors and/or problems may occur during the Z11 upload at the VAMCs and/or HEC.</p></li>
<li><p>This procedure is to be followed only after all VAMCs have installed the VAMC associated Phase 1 patches.</p></li>
<li><p>This process may take up to 12 hours and should be tasked to run.</p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  From the TaskMan Management menu, select Schedule/Unschedule Options.
22. At the Select OPTION to schedule or reschedule: prompt, type AYCEPHMC and press \<Enter\>.
23. At the Are you adding 'AYCEPHMC' as a new OPTION SCHEDULING (the nnTH)? No// prompt, type YES and press \<Enter\>.
24. The Edit Option Schedule screen appears.
25. Press the tab key until the QUEUED TO RUN AT WHAT TIME: field is highlighted. Enter an appropriate start time.
26. Press the tab key until the COMMAND: field is highlighted. Type SAVE and press \<Enter\>.
27. With the COMMAND field still highlighted, type EXIT and press \<Enter\>.

## Access Database Conversion Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two parts to the Access database conversion, exporting the Access data to a delimited text file, and converting the Access data to the MUMPS system.

### Export the Access Data to a Delimited Text File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure is done in Access.

1.  Open the Purple Heart Access Database in programmer mode.
28. On the Objects list, select Tables.
29. Select PURPLE_HEART_REGISTRY from the Tables listing.
30. From the File menu, select Export.
31. On the Export Table dialog box, select TEXT FILES from the "Save as Type:" listbox and click Save.
32. Select the Delimited option on Export Text Wizard dialog box and click Next.
33. Select the Other option on Export Text Wizard dialog box and type "\|" (without the quotes) in the adjacent text box. Click Next.
34. If you want to specify a file location, enter the path and filename in the Export to File text box.
35. Click Finish.
36. When the export operation is complete, a message box will display the name and location for the exported file. Please make a note of this information; it is necessary to convert the exported file into the MUMPS database.

### Converting the Access data to the MUMPS System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Transfer the exported Access file to the server where Purple Heart was installed via FTP.
37. Place the file in the default directory for your MUMPS session.
38. Ensure that the MUMPS database conversion has completed and then from a MUMPS programmer prompt, enter the following command: D ^AYCEPHAC
39. When prompted for FILENAME: enter the filename of the text file exported from the Access database. Do not enter the path, just the filename.
40. When the conversion has finished, the following message will be displayed:

    Access file conversion complete.
41. Capture the data contained in the ^XTMP("AYCEPH", global and send to REDACTED (REDACTED for an analysis of the conversion process. The global will report any problems and/or inconsistencies found during the conversion processes.