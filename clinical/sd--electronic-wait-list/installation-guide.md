---
title: VistA Scheduling Enhancement (VSE) GUI 2.0.0.14 Action Item-Install
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: .14 Action Item-Install
app_code: SD
app_name: Scheduling
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 2.0.0
patch_id: SD*2.0.0
group_key: "SD:SD:2.0.0"
file_numbers: []
security_keys: []
menu_options: 0
description: "ACTION REQUIRED: Install VistA Scheduling Enhancement (VSE) Production and TEST GUI v 2.0.0.14 using the CMCB package on all workstations at all VistA sites."
audience: 
keywords: 
  - vista
  - span
  - appointments
  - clinic
  - scheduling
  - test
  - cmcb
  - view
  - action
  - appointment
page_count: 0
word_count: 736
section_count: 0
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/VSE_GUI_2_0_0_14_Action_Item_Install.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling/VSE_GUI_2_0_0_14_Action_Item_Install.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=100"
---

ACTION TO: Directors (IO \[Core (Client Technology)\], EUO)

ACTION FROM:  Deputy Assistant Secretary, IT Operations and Services (ITOPS)

ACTION DUE:  COB, 30 days from release

ACTION REQUIRED: Install VistA Scheduling Enhancement (VSE) Production and TEST GUI v 2.0.0.14 using the CMCB package on all workstations at all VistA sites.

REPORTING METHOD: <u>National dashboards will be used to validate compliance</u>

DESCRIPTION: Purpose: Scheduling personnel will be able to use the graphical user interface (GUI) to schedule appointments for our Veterans and to view appointment availability. 

A resource management dashboard will display pertinent resource management metrics in a single view, and enhance the scheduling resource management capabilities of individual facilities and staff at various levels within VHA. 

The enhancement will also allow the National Director's Office the ability to measure and track supply, demand, and efficiency metrics related to outpatient scheduling operations.

Reference Solution Delivery Change Order: CO458363FY18 (Production); CO458056FY18 (Test)

(\*Note: Tier III Support Teams should follow internal change control processes)

BACKGROUND: VSE GUI is a software module that allows schedulers to make appointments quickly by viewing multiple appointment request types and multiple clinics in one screen. A scheduler can easily view patient requests for service, find the next available open appointment, view the provider’s availability in multiple clinics, and track a patient’s appointment process.

SD\*5.3\*672 requires the installation of VS GUI version 2.0.0.14 to properly function. Both SD\*5.3\*672 and VS GUI version 2.0.0.14 must be coordinated and installed at the same time during the same maintenance window. The Vista Scheduling (VS) Graphical User Interface GUI v2.0.0.14 and VistA M patch SD\*5.3\*672 provide additional enhancements to the VS GUI v2.0.0.13. The enhancements included in this patch are listed as follows:

- Provides the capability for VSE users to authenticate via Personal Identity Verification (PIV)
- Clinic Group will display for second patient without searching for a different clinic group first. (Users should put curser in the clinic group field and click Enter to refresh.)
- Electronic Wait List (EWL) can now be consistently dispositioned from the Resource Management (RM) Grid
- Scheduling grid no longer allows overbooks in the evenings after a FULL DAY availability cancellation. The visual display does not extend the cancellation hash marks to midnight, but it will not allow the user to book, and presents an appropriate error message to user
- Drag and drop rescheduling within the current calendar view (including clinic groups and provider search calendar views) is now available for most existing appointments. Consult linked appointments and appointments in the past cannot drag and drop as they have other linkages that still require manual cancellation
- Slot tallies no longer move as the calendar view is scrolled down
- Schedulers cannot add new request or appointments in VSE GUI after a patient is listed as deceased in VistA
- Cancel by Clinic no longer allows PID to be changed by switching between Cancel by Clinic and Cancel by Patient
- VSE GUI Audit Report now reports accurate counts of actions within VSE GUI for both individual and all schedulers
- Checking out appointment “Follow-up Needed” now works better than it did in former versions, however we continue to keep it tied to the SD SUPERVISOR key until we can completely separate the administrative check out function in VSE GUI from any ties to the encounter files. We do not recommend use of check out at this time
- Appointments scheduled in VSE GUI with a past date will now show in CPRS cover sheet and visit location lists
- SDRR CLINIC LETTER REPORT will now run properly (was hanging on bad data in previous versions)

Instructions to Complete Action: Note: The following VistA patch, which was released via FORUM, needs to be installed in order to make the GUI functional for the users.  It is necessary that the CMCB deployment team verify with the VistA Application team on the scheduled patch installs to coordinate the VSE GUI install timeline.

| Patch        | Application |
|--------------|-------------|
| SD\*5.3\*672 | Scheduling  |

STEP 1 (Core):  All VistA sites shall install the VSE PRODUCTION and TEST GUIs on all workstations using the CMCB package provided by SD.  The TEST GUIs will be used to provide training to VSE users.

- CMCB Build Document (Production): <span class="mark">REDACTED</span>
- CMCB Build Document (Test): <span class="mark">REDACTED</span>

Compliance will be tracked via CMCB reportsVA VistA Scheduler GUI Standard Report:    
<span class="mark">REDACTED</span>

VA VistA Scheduler GUI Test Report:    
<span class="mark">REDACTED</span>

Implementation Manager POC:

<span class="mark">REDACTED</span>