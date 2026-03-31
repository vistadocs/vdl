---
title: ASISTS GUI Version 2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: OOPS
app_name: Automated Safety Incident Surveillance Tracking System
section: FIN
app_status: active
pkg_ns: OOPS
patch_ver: 2
patch_id: OOPS*2
group_key: "OOPS:OOPS:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - asists
  - incident
  - report
  - manual
  - employee
  - version
  - sign
  - osha
page_count: 0
word_count: 12074
section_count: 53
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2018
revision_count: 3
revision_newest: 12/13/2018
revision_oldest: 09/02/08
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=56"
---

![](asists-gui-version-2-user-manual/001.png)

Automated Safety Incident Surveillance Tracking System (ASISTS) V. 2.0Graphical User Interface (GUI)User ManualJune 2002

(Revised December 2018)

Office of Enterprise Development

Management & Financial Systems

Revision History

Initiated on 09/02/08

|            |                                                                                                                                                |                     |                      |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------|
| Date   | Description (Patch \# if applicable)                                                                                                       | Project Manager | Technical Writer |
| 09/02/08   | Enhancements from Patch OOPS\*2\*15 – Privacy Act issues, modifications to the CA-7 to meet Department of Labor changes to the form            | REDACTED            | REDACTED             |
| 04/03/12   | Maintenance Patch OOPS\*2\*23 – Update pages 101, 103 regarding the "Reason for Controvert Report" and the "Reason for Dispute Report."        | REDACTED            | REDACTED             |
| 12/13/2018 | Maintenance patch, OOPS\*2.0\*32 – Update to page 5 to reflect disabling of menu options due to the decommissioning of the ASISTS application. | REDACTED            | REDACTED             |

Table of Contents

Introduction [1](#introduction)

Welcome [1](#welcome)

Background [1](#background)

Goals [1](#goals)

Reporting Process for the Incident Report [2](#reporting-process-for-the-incident-report)

Reporting Process (CA-1/CA-2 Claims) [3](#reporting-process-ca-1ca-2-claims)

508 Compliance [4](#compliance)

OSHA [4](#osha)

ASISTS Menus [5](#asists-menus)

Decommissioning of asists [5](\l)

Employee Menu [6](#employee-menu)

Supervisor Menu [7](#supervisor-menu)

Occupational Health Menu [7](#occupational-health-menu)

Safety Menu [8](#safety-menu)

Workers' Comp Menu [9](#workers-comp-menu)

Union Menu [10](#union-menu)

Common Screens [11](#common-screens)

ASISTS Select Case Screen [11](#asists-select-case-screen)

Name Search Screen [12](#name-search-screen)

Duplicate Record Screen [13](#duplicate-record-screen)

Option Documentation [14](#option-documentation)

Change Status of Case [16](#change-status-of-case)

Classify Incident Outcome [17](#classify-incident-outcome)

Complete/Validate/Sign CA1 [19](#completevalidatesign-ca1)

Injury/Witness Data Tab [21](#injurywitness-data-tab)

Agency Tab [22](#agency-tab)

Work Schedule Tab [23](#work-schedule-tab)

Third Party Tab [24](#third-party-tab)

Physician Tab [25](#physician-tab)

Filing Instructions Tab [26](#filing-instructions-tab)

OWCP Tab [27](#owcp-tab)

Complete/Validate/Sign CA2 [30](#completevalidatesign-ca2)

Employee Data Tab [31](#employee-data-tab)

Claim Information Tab [32](#claim-information-tab)

Agency Tab [33](#agency-tab-1)

Work Schedule Tab [34](#work-schedule-tab-1)

Third Party Tab [35](#third-party-tab-1)

Physician Tab [36](#physician-tab-1)

Signatures Tab [37](#signatures-tab)

OWCP Tab [38](#owcp-tab-1)

Complete/Validate/Sign Incident Report [41](#completevalidatesign-incident-report)

Employee Data Tab [42](#employee-data-tab-1)

General Setting Tab [43](#general-setting-tab)

Other Factors Tab [44](#other-factors-tab)

Exposure Tab [45](#exposure-tab)

Equipment Tab [46](#equipment-tab)

OSHA Tab [47](#osha-tab)

Signatures Tab [48](#signatures-tab-1)

Create Amendment [49](#create-amendment)

Create Incident Report [51](#create-incident-report)

Display Incident Outcome Report [54](#display-incident-outcome-report)

Display Incidence Rates Worksheet [56](#display-incidence-rates-worksheet)

Display OSHA 300 Log [59](#display-osha-300-log)

Display OSHA 300A Summary [62](#display-osha-300a-summary)

Edit Site Parameter [63](#edit-site-parameter)

Edit/Validate Stub Record [66](#editvalidate-stub-record)

Electronically Sign for Employee [67](#electronically-sign-for-employee)

Employee Bill of Rights [69](#employee-bill-of-rights)

Enter/Edit Location of Injury Detail [70](#enteredit-location-of-injury-detail)

Enter/Edit OSHA 300A Summary Data [72](#enteredit-osha-300a-summary-data)

Enter/Edit Union Information [74](#enteredit-union-information)

Filing Instructions Report [76](#filing-instructions-report)

Location of Injury Report [78](#location-of-injury-report)

Log of Federal Occupational Injuries and Illnesses [81](#log-of-federal-occupational-injuries-and-illnesses)

Log of Needlestick Incidents [83](#log-of-needlestick-incidents)

Manual Transmission of DOL Data [85](#manual-transmission-of-dol-data)

Manual Transmit of National Database Data [86](#manual-transmit-of-national-database-data)

Print Blank CA1/CA2/CA7 [87](#print-blank-ca1ca2ca7)

Print CA1/CA2 [90](#print-ca1ca2)

Print CA7 [91](#print-ca7)

Print Dual Benefits Form [93](#print-dual-benefits-form)

Print Incident Report Status [94](#print-incident-report-status)

Print Report of Incident [96](#print-report-of-incident)

Reason for Controvert Report [100](#reason-for-controvert-report)

![](asists-gui-version-2-user-manual/002.png)Reason for Dispute Report [102](#_Toc532839411)

![](asists-gui-version-2-user-manual/003.png)Request for Compensation (CA7) [104](#_Toc532839412)

Sections 1-2 Tab [106](#sections-1-2-tab)

Sections 3-4 Tab [107](#sections-3-4-tab)

Sections 5-6 Tab [108](#sections-5-6-tab)

Section 7 [109](#section-7-1)

Sections 8-9 Tab [110](#sections-8-9-tab)

Sections 10-13 Tab [111](#sections-10-13-tab)

Sections 14-15 Tab [112](#sections-14-15-tab)

Summary Incident Reports [113](#summary-incident-reports)

About ASISTS [116](#about-asists)

Technical Support [116](#technical-support)

Release Notes [116](#release-notes)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Welcome](#welcome)
  - [Welcome to ASISTS GUI V. 2.0. This Graphical User Interface (GUI) version of the Automated Safety Incident Surveillance Tracking System (ASISTS) software package combines exciting new features with the established functionality ASISTS users have come to rely on. ASISTS GUI V. 2.0 is a full-featured, automated accident and illness reporting system designed for the Department of Veterans Affairs.](#welcome-to-asists-gui-v-20-this-graphical-user-interface-gui-version-of-the-automated-safety-incident-surveillance-tracking-system-asists-software-package-combines-exciting-new-features-with-the-established-functionality-asists-users-have-come-to-rely-on-asists-gui-v-20-is-a-full-featured-automated-accident-and-illness-reporting-system-designed-for-the-department-of-veterans-affairs)
  - [Background](#background)
  - [Goals](#goals)
  - [Reporting Process for the Incident Report](#reporting-process-for-the-incident-report)
  - [Reporting Process (CA-1/CA-2 Claims)](#reporting-process-ca-1ca-2-claims)
  - [Compliance](#compliance)
  - [Throughout the ASISTS application, if the software detects an active screen reader is being used, additional text is displayed to the user welcoming them to the system and instructing them on how to use the menu options to navigate through the application.](#throughout-the-asists-application-if-the-software-detects-an-active-screen-reader-is-being-used-additional-text-is-displayed-to-the-user-welcoming-them-to-the-system-and-instructing-them-on-how-to-use-the-menu-options-to-navigate-through-the-application)
  - [OSHA](#osha)
- [# ASISTS Menus](#asists-menus)
  - [## Employee Menu](#employee-menu)
  - [Supervisor Menu](#supervisor-menu)
  - [Occupational Health Menu](#occupational-health-menu)
  - [Safety Menu](#safety-menu)
  - [Workers' Comp Menu](#workers-comp-menu)
  - [Union Menu](#union-menu)
  - [Common Screens](#common-screens)
    - [ASISTS Select Case Screen](#asists-select-case-screen)
    - [Name Search Screen](#name-search-screen)
    - [Duplicate Record Screen](#duplicate-record-screen)
- [Option Documentation](#option-documentation)
  - [Change Status of Case](#change-status-of-case)
  - [Classify Incident Outcome](#classify-incident-outcome)
  - [Complete/Validate/Sign CA1](#completevalidatesign-ca1)
    - [### Injury/Witness Data Tab](#injurywitness-data-tab)
    - [Agency Tab](#agency-tab)
    - [Work Schedule Tab](#work-schedule-tab)
    - [Third Party Tab](#third-party-tab)
    - [Physician Tab](#physician-tab)
    - [Filing Instructions Tab](#filing-instructions-tab)
    - [OWCP Tab](#owcp-tab)
  - [Complete/Validate/Sign CA2](#completevalidatesign-ca2)
    - [Employee Data Tab](#employee-data-tab)
    - [### Claim Information Tab](#claim-information-tab)
    - [Agency Tab](#agency-tab-1)
    - [Work Schedule Tab](#work-schedule-tab-1)
    - [Third Party Tab](#third-party-tab-1)
    - [Physician Tab](#physician-tab-1)
    - [Signatures Tab](#signatures-tab)
    - [OWCP Tab](#owcp-tab-1)
  - [Complete/Validate/Sign Incident Report](#completevalidatesign-incident-report)
    - [Employee Data Tab](#employee-data-tab-1)
    - [General Setting Tab](#general-setting-tab)
    - [Other Factors Tab](#other-factors-tab)
    - [Exposure Tab](#exposure-tab)
    - [Equipment Tab](#equipment-tab)
    - [OSHA Tab](#osha-tab)
    - [Signatures Tab](#signatures-tab-1)
  - [Create Amendment](#create-amendment)
  - [Create Incident Report](#create-incident-report)
  - [Display Incident Outcome Report](#display-incident-outcome-report)
  - [Display Incidence Rates Worksheet](#display-incidence-rates-worksheet)
  - [Display OSHA 300 Log](#display-osha-300-log)
  - [Display OSHA 300A Summary](#display-osha-300a-summary)
  - [Edit Site Parameter](#edit-site-parameter)
    - [Delete Station](#delete-station)
  - [Edit/Validate Stub Record](#editvalidate-stub-record)
  - [Electronically Sign for Employee](#electronically-sign-for-employee)
  - [Employee Bill of Rights](#employee-bill-of-rights)
  - [Enter/Edit Location of Injury Detail](#enteredit-location-of-injury-detail)
  - [Enter/Edit OSHA 300A Summary Data](#enteredit-osha-300a-summary-data)
  - [Enter/Edit Union Information](#enteredit-union-information)
  - [Filing Instructions Report](#filing-instructions-report)
  - [Location of Injury Report](#location-of-injury-report)
  - [Log of Federal Occupational Injuries and Illnesses](#log-of-federal-occupational-injuries-and-illnesses)
  - [Log of Needlestick Incidents](#log-of-needlestick-incidents)
  - [Manual Transmission of DOL Data](#manual-transmission-of-dol-data)
  - [Manual Transmit of National Database Data](#manual-transmit-of-national-database-data)
  - [Print Blank CA1/CA2/CA7](#print-blank-ca1ca2ca7)
  - [Print CA1/CA2](#print-ca1ca2)
  - [Print CA7](#print-ca7)
  - [## ## Print Dual Benefits Form](#print-dual-benefits-form)
  - [Print Incident Report Status](#print-incident-report-status)
  - [Print Report of Incident](#print-report-of-incident)
  - [Reason for Controvert Report](#reason-for-controvert-report)
  - [![](asists-gui-version-2-user-manual/095.png) Reason for Dispute Report](#asists-gui-version-2-user-manual095png-reason-for-dispute-report)
  - [![](asists-gui-version-2-user-manual/097.png) Request for Compensation (CA7)](#asists-gui-version-2-user-manual097png-request-for-compensation-ca7)
    - [Sections 1-2 Tab](#sections-1-2-tab)
    - [Sections 3-4 Tab](#sections-3-4-tab)
    - [Sections 5-6 Tab](#sections-5-6-tab)
    - [Section 7](#section-7)
    - [Sections 8-9 Tab](#sections-8-9-tab)
    - [Sections 10-13 Tab](#sections-10-13-tab)
    - [Sections 14-15 Tab](#sections-14-15-tab)
  - [Summary Incident Reports](#summary-incident-reports)
- [About ASISTS](#about-asists)
  - [Technical Support](#technical-support)
  - [Release Notes](#release-notes)

## Welcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Welcome to ASISTS GUI V. 2.0. This Graphical User Interface (GUI) version of the Automated Safety Incident Surveillance Tracking System (ASISTS) software package combines exciting new features with the established functionality ASISTS users have come to rely on. ASISTS GUI V. 2.0 is a full-featured, automated accident and illness reporting system designed for the Department of Veterans Affairs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS software package stores data on accidents causing injuries and illnesses reported via the Report of Incident. The employee may choose to apply for compensation using the Federal Employee's Notice of Traumatic Injury and Claim for Continuation of Pay/Compensation (CA-1) when the incident is an injury and the Notice of Occupational Disease and Claim for Compensation (CA-2) for an illness.

Statistical reporting is performed on incidents occurring nationwide by extracting pertinent Report of Incident data from facilities and transmitting it to the ASISTS National Database (NDB). Reports are periodically generated from the NDB to identify systematic trends and to support prevention programs concerning front line health care worker exposure to bloodborne pathogens.

The ASISTS package provides the capability to electronically transmit CA-1 and CA-2 data to the Department of Labor (DOL). Federal Law requires that these forms be submitted within 14 days after the employee submits a claim for an accident or illness. The data is collected at each facility and is then transmitted to DOL via the Austin Automation Center (AAC). The transmission of each completed form is under the control of workers’ compensation personnel at each facility.

## Goals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS has three major goals.

- Better tracking of employee injuries and illnesses

> ASISTS computerizes the Report of Incident as well as the OWCP CA-1 and CA-2 forms. These reports help improve the ability to trend and analyze accidental injuries and illnesses, thus helping to prevent future incidents from occurring.

- Reduce exposures to bloodborne pathogens from needlesticks, sharps, or body fluids

> ASISTS instantly notifies Occupational Health and other medical personnel when the employee reports an incident involving a bloodborne pathogen exposure, so that proper tests and treatment can be initiated. The data concerning exposure to bloodborne pathogens will be collected in a national database to identify national trends, training needs, and best practices for the benefit of all employees at every VA medical center.

- Reduce worker compensation costs

> ASISTS facilitates a case management approach to preventing future incidents and provides better management of workers' compensation claims. Through automation, the incident reporting process will be more accurate and be processed in a more timely fashion.

## Reporting Process for the Incident Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an incident occurs causing injury or illness, or multiple instances occur over time causing illness, a Report of Incident must be created. The individual involved goes to his/her supervisor, Occupational Health Unit, safety official, or (if it is after hours) to the Administrative Officer of the Day (AOD) to report the incident. A stub record on the incident is created using the option Create Incident Report. The stub record contains basic information related to the incident.

A bulletin called the Employee Bill of Rights is sent to the employee explaining his/her rights and entitlements to benefits following a work-related injury or illness. The safety official, supervisor, union representatives, and workers’ compensation personnel receive a bulletin informing them that an incident occurred. If it happens to be a bodily fluid exposure, Infection Control (where applicable) and Occupational Health are also notified so they may plan follow-up care.

Once the initial stub record is created and a case number is assigned, the supervisor, safety official, or workers’ compensation personnel gathers information about the incident, counsels the employee to complete a CA-1 or CA-2, and completes the Report of Incident using the Complete/Validate/Sign Incident Report menu option. Once the supervisor electronically signs the case, a bulletin is triggered to inform the safety official that the Report of Incident can be reviewed. The employee does not need to wait until the Report of Incident is completed to begin the claim process and may choose to initiate a claim for compensation by using the menu options Complete/Validate/Sign CA-1 for an injury or the Complete/Validate/Sign CA-2 for an illness.

The safety official reviews the Report of Incident using the Complete/Validate/Sign Incident Report menu option and completes the safety official related questions and comments on the Signatures Tab. The case should remain open until it is successfully sent to the Dept. of Labor or when the reporting process is complete.

## Reporting Process (CA-1/CA-2 Claims)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The employee enters data for the CA-1 or CA-2 using the Complete/Validate/Sign CA-1 option for injury and Complete/Validate/Sign CA-2 option for illness. When the employee signs their portion of the CA-1 or CA-2, this triggers a bulletin to the supervisor, union representatives, and workers’ compensation personnel notifying them of the requirement to complete the form and file with the Department of Labor within 2-3 working days.

When the supervisor signs the CA-1 or CA-2 using the Complete/Validate/Sign CA-1 option for injury and Complete/Validate/Sign CA-2 option for illness, a bulletin is sent to the OOPS WCP mail group and also to the supervisor.

The case remains available to the employee for further editing until the supervisor signs it. If the employee retrieves a signed case, the electronic signature is removed and the claim must be resigned. However, once the supervisor signs the case, the original case is no longer available for edit by either the employee or the supervisor. To edit the claim, the safety official or the workers’ compensation personnel must create an amendment.

If an employee is incapacitated and cannot electronically sign the claim, the workers’ compensation personnel may sign for the employee via the Electronically Sign for Employee option.

The workers’ compensation personnel should use the Complete/Validate/Sign CA-1 or Complete/Validate/Sign CA-2 menu option to complete and file the claim with the Dept. of Labor. The workers’ compensation personnel should ensure that they have a hard copy of the claim with the employee and the supervisor’s wet signature and any witness statements before electronically transmitting the claim to the Dept. of Labor. A hard copy of the CA-1 or CA-2 can be printed using the Print CA-1/CA-2 menu option. Two mailman messages will be sent to the OOPS WCP mail group when claims successfully process in ASISTS and transmit to the Dept. of Labor via the Austin Automation Center (AAC).

Data elements are extracted and transmitted from the ASISTS package to the AAC. In order for a case to be transmitted, it must have a "Closed" status. Members of the OOPS NDB MESSAGES mail group should be individuals who need to be notified of error messages or return messages from the AAC. The group must have at least one member for data to be transmitted to AAC. The date that a record is transmitted to the AAC is automatically recorded in ASISTS. Once the record is transmitted, it is no longer editable from ASISTS. ASISTS will not receive data back from the AAC.

The option, Scheduled Transmit National Database (2162) Data \[OOPS SCHEDULED XMIT 2162 DATA\], should be scheduled to run on a weekly basis during off-peak hours. Error checking is preformed to assure that the system is set up as required for mailing the mail messages and that the mail messages are created correctly. If an error occurs, a message will be sent to the mail group OOPS NDB MESSAGES advising of the problem.

## Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Throughout the ASISTS application, if the software detects an active screen reader is being used, additional text is displayed to the user welcoming them to the system and instructing them on how to use the menu options to navigate through the application.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OSHA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information on OSHA’s recordkeeping requirements, go to their website at <http://www.osha.gov/> where you can see the entire regulation on recordkeeping for injury and illness tracking in the work environment.

# # ASISTS Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the decommissioning of ASISTS, effective on January 1, 2019, functionality will be available only to the users who have the "Safety" and "Workers' Comp" secondary menu options. The following menu's will no longer be available upon the release of patch, OOPS\*2.0\*32:

| Menu Name           | Secondary Menu Option Name                                              |
|-------------------------|-----------------------------------------------------------------------------|
| Employee            | ASISTS GUI Employee Menu (Context) \[OOPS GUI EMPLOYEE\]                    |
| Supervisor          | ASISTS GUI Supervisor Menu (Context) \[OOPS GUI SUPERVISOR MENU\]           |
| Occupational Health | ASISTS GUI Employee Health Menu (Context) \[OOPS GUI EMPLOYEE HEALTH MENU\] |
| Union               | ASISTS GUI Union Menu (Context) \[OOPS GUI UNION MENU\]                     |

![](asists-gui-version-2-user-manual/004.png)

There are many different users of the ASISTS application - the employee, supervisor, Occupational Health worker, safety official, workers' compensation specialist, and union representative. Each user is assigned different privileges and a different set of menu options based on their role.

The ASISTS software is organized into the following menus: Employee, Supervisor, Occupational Health, Safety, Workers’ Comp, and Union.

## ## Employee Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All employees have VistA access and are assigned the Employee Menu options. The Employee Menu provides the employee access to initiate a worker's compensation claim. Other menu options ensure the employee has access to the Employee Bill of Rights, as well as the ability to electronically validate and sign their claims. Users of the Employee Menu can only see their own incidents. The Employee Menu contains these options.

> Complete/Validate/Sign CA1

> Complete/Validate/Sign CA2

> Employee Bill of Rights

> Request for Compensation (CA7)

## Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Supervisor Menu may be assigned to any user with supervisory duties. The user creating the Incident Record will list the supervisor(s) of the employee involved. The Supervisor Menu provides a variety of tasks to facilitate efficient and accurate incident reporting.

Users with this menu only see records that have their name listed in the Supervisor or Secondary Supervisor fields on the Report of Incident. The Supervisor Menu contains these options.

> Create Incident Report

> Print CA1/CA2

> Complete/Validate/Sign Incident Report

> Complete/Validate/Sign CA1

> Complete/Validate/Sign CA2

> Employee Bill of Rights

> Print Report of Incident

> Print Incident Report Status

## Occupational Health Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Occupational Health Menu is assigned to users who work in the Occupational Health Unit (Employee Health). Infection Control can be enrolled in the OOPS EH mail group to receive email messages regarding bloodborne pathogen exposure. Users with this menu can access all incidents within their facility. The Occupational Health Menu contains these options.

> Create Incident Report

> Edit/Validate Stub Record

> Employee Bill of Rights

> Reports

> Log of Needlestick Incidents

> Print Incident Report Status

> Print Report of Incident

> Summary Incident Reports

> Display OSHA 300 Log

## Safety Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Safety Menu is assigned to the safety official at the facility. Users with this menu can access all incidents within their facility. The Safety Menu contains these options.

> Change Status of Case

> Create Incident Report

> Create Amendment

> Complete/Validate/Sign Incident Report

> Edit Site Parameter

> Employee Bill of Rights

> Enter/Edit Location of Injury Detail

> Manual Transmission of National Database Data

> OSHA 300 Options

> Classify Incident Outcome

> Enter/Edit OSHA 300A Summary Data

> Display Incident Outcome Report

> Display Incidence Rates Worksheet

> Display OSHA 300A Summary

> Display OSHA 300 Log

> Reports

> Log of Federal Occupational Injuries and Illnesses

> Log of Needlestick Incidents

> Print Incident Report Status

> Print Report of Incident

> Summary Incident Reports

> Location of Injury Report

## Workers' Comp Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Workers’ Comp Menu is assigned to workers’ compensation specialists at the facility. Users with this menu can access all incidents within their facility. The Workers’ Comp Menu contains these options.

> Change Status of Case

> Complete/Validate/Sign CA1

> Complete/Validate/Sign CA2

> Electronically Sign for Employee

> Employee Bill of Rights

> Enter/Edit Union Information

> Print Blank CA1/CA2/CA7

> Edit Site Parameter

> Print CA1/CA2

> Print CA-7

> Print Dual Benefits Form

> Manual Transmission of DOL Data

> OSHA 300 Options

> Display OSHA 300A Summary

> Display OSHA 300 Log

> Request for Compensation (CA7)

> Reports

> Log of Needlestick Incidents

> Print Incident Report Status

> Print Report of Incident

> Summary Incident Reports

> Filing Instructions Report

> Reason for Controvert Report

> Reason for Dispute Report

## Union Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Union Menu is assigned to the union representative members of the Accident Review Board at the facility. The Union menu provides the ability to see the Employee Bill of Rights and modified reports without names. Users with this menu can access all incidents within their facility. The Union contains these options.

> Employee Bill of Rights

> Reports

> Display OSHA 300 Log

> Log of Federal Occupational Injuries and Illness

> Print Incident Report Status

> Print Report of Incident

## Common Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The screens shown below are common to many of the ASISTS options. They are displayed here and, for the most part, not shown in each individual option documentation.

### ASISTS Select Case Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](asists-gui-version-2-user-manual/005.png)

This screen allows the user to narrow the search criteria when selecting a case.

### Name Search Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](asists-gui-version-2-user-manual/006.png)

This screen allows the user to search for an individual who is in the PAID and/or ASISTS database.

### Duplicate Record Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](asists-gui-version-2-user-manual/007.png)

After the individual has been selected, the system will check to see if there is a currently Open case for any person with the same social security number. If applicable, the above screen is displayed.

# Option Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Option Documentation Section contains documentation for all ASISTS software options presented in alphabetical order as listed below. In as much as different users may be assigned a variety of options, this section provides quick access to any specific option documentation.

> Change Status of Case

> Classify Incident Outcome

> Complete/Validate/Sign CA1

> Complete/Validate/Sign CA2

> Complete/Validate/Sign Incident Report

> Create Amendment

> Create Incident Report

> Display Incident Outcome Report

> Display Incidence Rates Worksheet

> Display OSHA 300 Log

> Display OSHA 300A Summary

> Edit Site Parameter

> Edit/Validate Stub Record

> Electronically Sign for Employee

> Employee Bill of Rights

> Enter/Edit Location of Injury Detail

> Enter/Edit OSHA 300A Summary Data

> Enter/Edit Union Information

> Filing Instructions Report

> Location of Injury Report

> Log of Federal Occupational Injuries and Illnesses

> Log of Needlestick Incidents

> Manual Transmission of DOL Data

> Manual Transmission of National Database Data

> Print Blank CA1/CA2/CA7

> Print CA1/CA2

> Print CA-7

> Print Dual Benefits Form

> Print Incident Report Status

> Print Report of Incident

> Reason for Controvert Report

> Reason for Dispute Report

> Request for Compensation (CA7)

> Summary Incident Reports

## Change Status of Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is found on the Safety and Worker’s Comp Menus.

Only the safety official or the workers’ compensation specialist has the option to change the status of a case. After the case has been selected, the Case Status can be changed to Open, Closed, or Deleted. If the status is Deleted, the Reason for Deletion is required.

![](asists-gui-version-2-user-manual/008.png)

> **NOTE:** Closing, deleting, or replacing a record by amendment removes it from all selection lists except for print options.

## Classify Incident Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu under OSHA 300 Options.

This option will enable either the safety official or workers’ comp specialist to track how the incident impacted the individual. This screen is used to enter incident outcome data for any work-related case which is recorded on the OSHA 300 Log. The system will calculate the total days the individual has accumulated for all added incident outcome classification entries. The result will be the summation of the actual number of days for both *Away From Work* and *Job Transfer/Restriction* entries. If the calculated total days for a specific case exceeds 180 days, the maximum number of days that will be reported for that case on the OSHA 300 Log will be 180 days.

Cases available for incident outcome classification include both Open/Closed cases as well as any case that has been electronically transmitted to the National Database or the Department of Labor. *Deleted* and *Replaced by Amendment* cases cannot be selected.

The four Incident Outcome Classifications are as follows.

- Other Recordable – This classification can only be selected for the first entry for an individual. This is a recordable event from the 29 CFR1904 Occupational Injury and Illness Recording and Reporting Requirements.
- Job Transfer/Restriction – This classification is selected when an employee is restricted from performing routine tasks that occur more than once a week or is transferred to another position because of the work-related incident.
- Away From Work – This classification equates to any day after the date of injury that the employee is not at work.
- Death – This classification is selected when the incident results in a fatality and will require a date of death to be entered.

Date of Classification – Includes the Start Date and End Date

- Start Date – The start date cannot be a future date and cannot be on or before the previous entry’s end date.
- End Date – This end date cannot precede the start date and cannot be a future date.

Date of Death - If the incident outcome classification is Death, then the Date of Death is required.

Estimated Return Date (must be future date) - The estimated return date is not used in any OSHA 300 Log calculations and it does not default from one outcome classification entry to the next.

Classify Incident Outcome

![](asists-gui-version-2-user-manual/009.png)

*Add Incident*

The Start Date and Incident Outcome Classification are required in order to add an entry. In order to add a second (or subsequent) entry, an end date must be entered for the previous entry.

*Edit Incident*

If an end date is not entered for the last incident outcome entry, it can be edited by clicking the edit button.

*Delete Incident*

If an end date is entered for the last incident outcome entry, the entry can be deleted.

## Complete/Validate/Sign CA1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Employee, Supervisor, and Worker’s Comp Menus.

All CA-1s begin with an Incident Report.

The Complete/Validate/Sign CA1 option allows the supervisor to complete information on the Supervisor’s Report of the CA-1. Certain data elements collected on the Incident Report are also used on the Federal Employee’s Notice of Traumatic Injury and Claim for Continuation of Pay/Compensation (CA-1) and the Notice of Occupational Disease and Claim for Compensation (CA-2).

The Employee Data, Injury/Witness Data, Agency, Work Schedule, Third Party, Physician, Filing Instructions, and OWCP tabs comprise the CA-1 Form. Each user may see and/or access a different set of tabs according to the type of incident and/or the type of access the user has. For example, from the Employee Menu, the Case Selection List only displays the user’s cases. Also, the supervisor can only retrieve cases where they are listed as the supervisor or secondary supervisor.

Required fields are indicated with a double asterisk (\*\*).

Complete/Validate/Sign CA1

*Employee Data Tab*

The Employee Data Tab is the main entry/edit point for processing CA-1 claims.

Only the employee and/or the workers’ compensation specialist may enter data on this screen. If the employee is incapacitated, the workers’ compensation specialist may electronically sign for the employee via the Electronically Sign for Employee option.

The supervisor can see the fields on this screen, but may only edit the Supervisor or Secondary Supervisor fields. To make changes to the data on this screen, use the Edit/Validate Stub Record menu option.

![](asists-gui-version-2-user-manual/010.png)

Complete/Validate/Sign CA1

### ### Injury/Witness Data Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Miscellaneous injury data along with all the witness information is contained on this tab.

![](asists-gui-version-2-user-manual/011.png)

Complete/Validate/Sign CA1

### Agency Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Duty station, agency, and additional employee information are contained on this tab.

![](asists-gui-version-2-user-manual/012.png)

Complete/Validate/Sign CA1

### Work Schedule Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to an individual's work hours, work schedule, incident dates/times, and pay rate are on this tab.

![](asists-gui-version-2-user-manual/013.png)

Complete/Validate/Sign CA1

### Third Party Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to the third party and incident specific questions is located on this tab.

![](asists-gui-version-2-user-manual/014.png)

Complete/Validate/Sign CA1

### Physician Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to the physician providing medical care, agency controvert of claim, and agency dispute of claim is on this tab.

![](asists-gui-version-2-user-manual/015.png)

Complete/Validate/Sign CA1

### Filing Instructions Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filing instructions and supervisor information such as title and phone number are stored on this tab.

![](asists-gui-version-2-user-manual/016.png)

Complete/Validate/Sign CA1

### OWCP Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information only accessible to OWCP personnel is contained on this tab.

![](asists-gui-version-2-user-manual/017.png)

  
Complete/Validate/Sign CA1

*Prevention of Dual Benefits*

In order to prevent a veteran from receiving dual benefits for the same injury or death (Federal Employees' Compensation Act (FECA), Section 8116), a Dual Benefits form will be attached to the CA1 claim. This form must be signed by both the employee and workers’ compensation personnel indicating that this claim is not a claim covered by another military claim.

When the employee selects the Complete/Validate/Sign CA-1 option, “Are you a Veteran” is displayed as a popup message. If the response is NO, the CA1 form will be displayed. If the response is YES, the Dual Benefits form will be displayed for the user to complete. If the user responds Yes to “Do you refuse to answer the Dual Benefits questions on this form”, they will not be required to respond to the dual benefits questions and can save and exit the Dual Benefits form to get to the CA form. If the user responds NO, the user can answer the dual benefit questions and sign the Dual Benefit form prior to accessing the CA form. The employee will not have to sign the Dual Benefits form prior to signing the CA form.

The Dual Benefits form will be kept in the employee’s workers’ compensation file that is maintained by the facility. It is not transmitted to the DOL. It will be sent to the local VA Regional VBA Office for veteran employees filing an OWCP claim for injuries involving those for which they are service-connected and receiving compensation and pension funds from the Department of Veterans Affairs.

  
Complete/Validate/Sign CA1

![](asists-gui-version-2-user-manual/018.png)

## Complete/Validate/Sign CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Employee, Supervisor, and Worker’s Comp Menus.

All CA2s begin with a Report of Incident.

Certain data elements collected on the Report of Incident are also used on the Notice of Occupational Disease and Claim for Compensation (CA-2).

The Employee Data, Claim Information, Agency, Work Schedule, Third Party, Physician, Signatures, and OWCP tabs comprise the CA-2 Form. Each user may see and/or access a different set of tabs according to the type of incident and/or the type of access the user has. For example, from the Employee Menu, the Case Selection List only displays the user's cases. Also, the supervisor can only retrieve cases where they are listed as the supervisor or secondary supervisor.

Required fields are indicated with a double asterisk (\*\*).

Complete/Validate/Sign CA2

### Employee Data Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Employee Data Tab is the main entry/edit point for processing CA-2 claims.

Only the employee and/or the workers’ compensation specialist may enter data on this screen. If the employee is incapacitated, the workers’ compensation specialist may electronically sign for the employee via the Electronically Sign for Employee option.

The supervisor can see the fields on this screen, but may only edit the Supervisor or Secondary Supervisor fields. To make changes to the data on this screen, use the Edit/Validate Stub Record menu option.

![](asists-gui-version-2-user-manual/019.png)<span class="mark">  
</span>Complete/Validate/Sign CA2

### ### Claim Information Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to the dates of disease or illness, nature of disease or illness, and reasons for delay is located on this tab.

![](asists-gui-version-2-user-manual/020.png)

Complete/Validate/Sign CA2

### Agency Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Duty station, agency, and additional employee information is located here.

![](asists-gui-version-2-user-manual/021.png)

Complete/Validate/Sign CA2

### Work Schedule Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to work hours and schedule along with incident dates/times are contained here.

![](asists-gui-version-2-user-manual/022.png)

Complete/Validate/Sign CA2

### Third Party Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to third party and incident specific questions is located on this tab.

![](asists-gui-version-2-user-manual/023.png)

Complete/Validate/Sign CA2

### Physician Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information pertaining to the physician and medical treatment is contained here.

![](asists-gui-version-2-user-manual/024.png)

Complete/Validate/Sign CA2

### Signatures Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filing instructions and supervisor information such as title and phone number are located on this tab.

![](asists-gui-version-2-user-manual/025.png)

Complete/Validate/Sign CA2

### OWCP Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information only available to OWCP personnel is located on this tab.

![](asists-gui-version-2-user-manual/026.png)

Complete/Validate/Sign CA2

*Prevention of Dual Benefits*

In order to prevent a veteran from receiving dual benefits for the same injury or death (Federal Employees' Compensation Act (FECA), Section 8116 ), a Dual Benefits form will be attached to the CA2 claim. This form must be signed by both the employee and workers’ compensation personnel indicating that this claim is not a claim covered by another military claim.

When the employee selects the Complete/Validate/Sign CA-2 option, “Are you a Veteran” is displayed as a popup message. If the response is NO, the CA2 form will be displayed. If the response is YES, the Dual Benefits form will be displayed for the user to complete. If the user responds Yes to “Do you refuse to answer the Dual Benefits questions on this form”, they will not be required to respond to the dual benefits questions and can save and exit the Dual Benefits form to get to the CA form. If the user responds NO, the user can answer the dual benefit questions and sign the Dual Benefit form prior to accessing the CA form. The employee will not have to sign the Dual Benefits form prior to signing the CA form.

The Dual Benefits form will be kept in the employee’s workers’ compensation file that is maintained by the facility. It is not transmitted to the DOL. It will be sent to the local VA Regional VBA Office for veteran employees filing an OWCP claim for injuries involving those for which they are service-connected and receiving compensation and pension funds from the Department of Veterans Affairs.

Complete/Validate/Sign CA2

![](asists-gui-version-2-user-manual/027.png)

## Complete/Validate/Sign Incident Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Supervisor and Safety Menus.

The Complete/Validate/Sign Incident Report option allows the supervisor to enter information about an incident. It provides the foundation for entering data for the Report of Incident. Some data elements collected on the Report of Incident are also used on the Federal Employee's Notice of Traumatic Injury and Claim for Continuation of Pay/Compensation (CA-1) and the Notice of Occupational Disease and Claim for Compensation (CA-2) forms.

There are seven tabs - Employee Data, General Setting, Other Factors, Exposure, Equipment, OSHA, and Signatures - that comprise the Incident Form. Each user may see and/or access a different set of tabs according to the type of incident and/or the type of access the user has. The supervisor can only retrieve cases where they are listed as the supervisor or secondary supervisor.

Required fields are indicated with a double asterisk (\*\*) and must be completed before the record can be saved.

![](asists-gui-version-2-user-manual/028.png)

Complete/Validate/Sign Incident Report

### Employee Data Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The supervisor can see the fields on this tab, but may only edit the Supervisor or Secondary Supervisor fields. To make changes to the data on this screen, use the Edit/Validate Stub Record menu option.

![](asists-gui-version-2-user-manual/029.png)

Complete/Validate/Sign Incident Report

### General Setting Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information relating to the general setting/location of the incident is collected in the General Setting tab.

![](asists-gui-version-2-user-manual/030.png)

Complete/Validate/Sign Incident Report

### Other Factors Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tab contains information concerning the environmental and contributing factors leading to the incident. It also contains the Description of Incident which was previously on the General Settings tab. The six dropdown box fields must be answered before the supervisor can electronically sign the form.

![](asists-gui-version-2-user-manual/031.png)

Complete/Validate/Sign Incident Report

### Exposure Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Type of Incident selected is Exposure to Body Fluids, Needlesticks, Sharps Exposure, or Hollow Bore Needlestick, then the Exposure tab is visible and many of the fields are required.

![](asists-gui-version-2-user-manual/032.png)

Complete/Validate/Sign Incident Report

### Equipment Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Equipment tab captures data specific to any equipment or safety device in use at the time of the incident.

![](asists-gui-version-2-user-manual/033.png)

Complete/Validate/Sign Incident Report

### OSHA Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OSHA tab displays information pertaining to data entry for the OSHA 300 log.

![](asists-gui-version-2-user-manual/034.png)

Complete/Validate/Sign Incident Report

### Signatures Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Signatures tab displays both the supervisor and safety officials’ signature information. When the Report of Incident is signed, the name and date will appear.

The supervisor must enter corrective action information and the safety official must enter safety comments on this tab.

![](asists-gui-version-2-user-manual/035.png)

## Create Amendment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu.

The Create Amendment option should be used to correct an ASISTS case when the case is no longer available for edit because the supervisor or employee has signed it.

Only cases with the case status of *Open* can be selected. The original case record is duplicated and all signatures are removed. The original case status is changed to *Replaced by Amendment*. The case number references the duplicate case with an alpha character added to the end. For example, case 2002-00100 will be copied into case 2002-00100A and all electronic signatures will be removed.

The original date/time of occurrence cannot be changed using an amendment. If the original date/time of occurrence is incorrect, use the Change Status of Case option to change the case status to *Deleted* and create a new case with the correct date/time of occurrence.

After the new record has been created, the case may be corrected using one or more of the following options: Edit/Validate Stub Record, Complete/Validate/Sign Incident Report, Complete/Validate/Sign CA1, or Complete/Validate/Sign CA2.

> **NOTE:** After a claim is successfully transmitted and accepted at DOL, an amendment should NOT be retransmitted to DOL, even to correct information on the claim. The facility will need to submit the change request via hardcopy.

![](asists-gui-version-2-user-manual/036.png)

The user must select a claim and click the Create Amendment button to initiate the process.

Create Amendment

Once a selection has been made, the following message box will appear automatically. Clicking on the Yes button or pressing the Enter key will create the amendment. Click on the No button or press the ESC key to cancel the request.

![](asists-gui-version-2-user-manual/037.png)

If the Yes button is pressed, the following message box will display the new case number.

![](asists-gui-version-2-user-manual/038.png)

## Create Incident Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Supervisor, Occupational Health, and Safety Menus.

When an incident occurs causing injury or illness, or multiple instances occur over time causing illness, a Report of Incident must be created. The individual involved goes to his/her supervisor, Occupational Health Unit, safety official, or (if it is after hours) to the Administrative Officer of the Day (AOD) to report the incident. A stub record is created using this menu option. The stub record contains basic information related to the incident.

Required fields are indicated with a double asterisk (\*\*) and must be completed before the record can be saved.

If *Illness* is checked on the Incident Information panel, *Illness Type* is prompted for; if *Injury* is checked, *Injury Severity* is prompted for.

![](asists-gui-version-2-user-manual/039.png)

Create Incident Report

*Name Search Screen*

If employee or non-paid employee is selected, the following Name Search Screen is displayed. It allows the user to enter a partial name, SSN, or last initial and last four of the SSN. It returns all the individuals found that match the search criteria and allows the user to select an individual.

![](asists-gui-version-2-user-manual/040.png)

Create Incident Report

*Duplicate Record Checking*

To help prevent duplicate records from being created, after the individual has been selected, the system will check to see if there is a currently Open case for any person with the same SSN. If applicable, the following form is displayed.

![](asists-gui-version-2-user-manual/041.png)

If the case currently being entered is a new case and not a duplicate, press the Create New Record button.

## Display Incident Outcome Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu under OSHA 300 Options.

This report lists all incident outcome entries collected for an individual in the Classify Incident Outcome option. Cases that are available for selection (search) include both Open/Closed cases as well as any case that has been electronically transmitted to the National Database or the Department of Labor. *Deleted* and *Replaced by Amendment* cases cannot be selected.

Once the claim has been selected, the report may be sent to the your default printer or previewed on the computer screen.

![](asists-gui-version-2-user-manual/042.png)

Display Incident Outcome Report

![](asists-gui-version-2-user-manual/043.png)

## Display Incidence Rates Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu under OSHA 300 Options.

The Calculate Injury and Illness Incidence Rates Worksheet will only include cases where the *Include on OSHA Log* field equals YES (that is, OSHA eligible cases).

The user will be prompted to enter a start date, end date, and station. The specified date range must be for 2004 or greater. The selected date range and date/time the report was generated will be displayed in the footer of the Injury and Illness Incidence Rates Worksheet.

![](asists-gui-version-2-user-manual/044.png)

The Incidence Rates Worksheet report will display the following information for the specified date range and station: Total Number Of Injuries and Illnesses, Number Of Hours Worked By All Employees, Total Recordable Case Rate, Number Of Entries In Column H + Column I (columns on the OSHA 300 Log), and DART Incidence Rate.

Display Incidence Rates Worksheet

![](asists-gui-version-2-user-manual/045.png)

To calculate the <u>Total Recordable Case Rate</u> for the specified period, the system sums the Total Number of Injury and Illness incidents for that year, multiplies the number by 200,000, then divides the number by the Number of Hours Worked By All Employees. To calculate the <u>DART Incidence Rate</u> for the specified period, the system sums the Total Number of Injury and Illness entries on the OSHA 300 Log that involved days away from work and job transfer/restriction, multiplies the number by 200,000, then divides the number by the Number of Hours Worked By All Employees.

DEFINITION OF TOTAL RECORDABLE CASE RATE – An incidence rate is the number of recordable injuries and illnesses occurring among a given number of full-time workers (usually 100 full-time workers) over a given period of time (usually one year). The system shall compute the Incidence Rate for all recordable cases of injuries and illnesses.

> Total Number of Number of Hours TOTAL RECORDABLE

> Injuries & Illnesses X 200,000 ÷ Worked by All Employees = CASE RATE

> **NOTE:** To find out the total number of recordable injuries and illnesses that occurred during the year, count the number of OSHA eligible cases and sum the entries for Columns (G), (H), (I) and (J) on the OSHA 300 Log.

> **NOTE:** The safety official will enter the number of hours worked by all employees on a monthly basis in the Enter/Edit OSHA 300A Summary Data option. The system will retrieve and use this information in the calculations for the Injury and Illness Incidence Rates Worksheet.

Display Incidence Rates Worksheet

DEFINITION OF DART INCIDENCE RATE – System will compute the incidence rate for OSHA eligible cases involving days away from work, days of restricted work activity, or job transfer (DART).

> Number of Entries in Number of Hours DART

> Column H + Column I X 200,000 ÷ Worked by All Employees = Incidence Rate

> **NOTE:** Column H = Days Away from Work and Column I = Job Transfer/Restriction on the OSHA 300 form.

## Display OSHA 300 Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Occupational Health Menu and Union Menu under Reports and on the Safety and Workers’ Comp Menus under OSHA 300 Options.

Before the OSHA 300 Log can be displayed or printed, the user must select the start and end dates along with the station from the drop down list. The user must also indicate whether or not to include individuals’ names on the OSHA 300 Log (including names is not available if option is selected from the Union Menu).

If names are included and an OSHA eligible case has been marked as a privacy case in the Complete/Validate/Sign Incident Report option, the name field will display the words *Privacy Case* in the OSHA 300 Log. Additionally, if the Type of Incident for a claim is Hollow Bore Needlestick, Sharps Exposure, Exposure to Body Fluids/Splash, or Suture Needlestick, the words *Privacy Case* will print as the name if Include Names is Yes.

![](asists-gui-version-2-user-manual/046.png)

Display OSHA 300 Log

For the specified date range and station, the system will sum the number of OSHA eligible cases with the following incident outcome classifications and display the total number to the user on the OSHA 300 Log report.

> Death

> Days Away from Work

> Job Transfer or Restriction

> Other Recordable Cases

For the specified date range and station, the system will sum the number of days that the injured or ill worker was (K) On Job Transfer/Restriction or (L) Away From Work and display this total number to the user on the OSHA 300 Log report.

When the total number of days for either (K) On Job Transfer/Restriction is equal to or greater than 180 days, then the system will display the total number as 180 days. (OSHA 300 only demands tracking for 180 days.)

The maximum total number of days for column (K) On Job Transfer/Restriction plus column (L) Away from Work is 180 days. The system will sum the total number of OSHA eligible cases with the following illness or injury types and display the total number to the user on the OSHA 300 Log report.

> (M1) Injury

> (M2) Skin Disorder

> (M3) Respiratory Condition

> (M4) Poisoning

> (M5) Hearing Loss

> (M6) All Other Illnesses

When there are no OSHA eligible cases to print on the OSHA 300 Log report, the system will default a zero in all the report fields.

The system will display the selected date range and date/time the report was generated on the footer of the OSHA 300 Log report.

Display OSHA 300 Log

![](asists-gui-version-2-user-manual/047.png)

## Display OSHA 300A Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety and Workers’ Comp Menus under OSHA 300 Options.

The Display OSHA 300A Summary option includes all cases where the *Include on OSHA Log* field equals YES (OSHA eligible cases). The OSHA 300A summary information is retrieved and calculated from the data entered in the Enter/Edit OSHA 300A Summary Data option, the Create Incident Report option, and the Complete/Validate/Sign Incident Report option. If a case has more than one classification (e.g., the case begins as a restricted duty then becomes a lost time or days away from work claim), the system will only count the most severe classification on the OSHA 300A Summary report. A case can only be included once in the summary totals.

Before the OSHA 300A Summary information can be displayed or printed, the user must select the start and end dates along with the station from the drop down list.

![](asists-gui-version-2-user-manual/048.png)

## Edit Site Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety and Workers’ Comp Menus.

The Edit Site Parameter option provides the safety official the capability to create default information for the facility. If the site is an integrated facility, every station within the network can be defined with default information. The information entered here will populate the Agency, Station, and Physician fields on a CA-1 or CA-2.

The default values for the following fields can be set for each station: Station Number, OWCP Chargeback Code, OWCP Chargeback Suffix, Physician Name, Physician Address, Physician City, Physician State, Physician Zip Code, and Physician Title.

The following information is displayed on the Edit Site Parameter screen.

Site Name The name of your facility in the Site Parameter file.

OWCP District Office The Department of Labor District office that serves your facility.

Station List The list of stations that currently have default information entered.

Station/Physician Info Includes the chargeback code, chargeback suffix, physician

name/address/title.

![](asists-gui-version-2-user-manual/049.png)

Edit Site Parameter

*Add/Edit Station*

To edit or add a station, press the appropriate button. The form shown below is used to add a new station or edit an existing station in the Site Parameter file. The number of stations that can be added is unlimited.

The following information can be entered when adding or editing a station in the Edit Site Parameter option.

Station The station that is selected from the drop-down menu to have

default information added or the station that is selected for

editing.

OWCP Chargeback Code The default chargeback code for the station.

OWCP Chargeback Suffix The default chargeback code suffix for the station.

Physician Information The default Physician data for the station. The information

includes the Physician Name, Physician Address, Physician

City, Physician State, and Physician Zip Code.

![](asists-gui-version-2-user-manual/050.png)

Edit Site Parameter

### *Delete Station*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete a station, select the desired station from the station list and press the Delete button. The following confirmation message will be displayed.

![](asists-gui-version-2-user-manual/051.png)

If Yes, the Station and all default information will be deleted. The following message will be displayed to verify that the station has been deleted.

![](asists-gui-version-2-user-manual/052.png)

## Edit/Validate Stub Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Occupational Health Menu.

This menu option is used to edit the top portion of the Report of Incident. The stub record contains basic information related to the incident and the person involved.

The supervisor and safety official can edit the stub record using the Complete/Validate/Sign Incident Report option.

![](asists-gui-version-2-user-manual/053.png)

## Electronically Sign for Employee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Compensation Menu.

The Electronically Sign for Employee option provides a mechanism to allow the workers’ compensation specialist to sign the Employee portion of a CA1 or CA2 claim. This would only be necessary if the employee was incapacitated and unable to sign for themselves.

> **NOTE:** Obtaining approval from the Occupational Health Unit and safety officer for the workers’ comp specialist to sign for the employee is no longer required.

![](asists-gui-version-2-user-manual/054.png)

Once the case is selected, the user is prompted for their electronic signature. Enter the electronic signature and press the Ok button to file or press the Cancel button to stop the action.

![](asists-gui-version-2-user-manual/055.png)

Once the electronic signature is successfully entered, a confirmation message will appear.

Electronically Sign for Employee

If the fields on the employee’s portion of the CA-1 or CA-2 are incomplete or missing, an error message will appear with the related fields. Use the Complete/Validate/Sign CA1 or the Complete/Validate/Sign CA2 option to complete the employee’s portion of the claim and resign.

![](asists-gui-version-2-user-manual/056.png)

## Employee Bill of Rights

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on all ASISTS menus.

The Employee Bill of Rights option provides the capability to print a hardcopy of the Employee Bill of Rights or view it on a computer screen.

The Employee Bill of Rights is sent to the employee notifying them of their rights and entitlements to benefits following a work related injury or illness. If an employee does not have computer access, and therefore would not receive a message containing the Bill of Rights, this option can be used to print a hard copy.

![](asists-gui-version-2-user-manual/057.png)

## Enter/Edit Location of Injury Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu.

The Enter/Edit Location of Injury Detail option is used to enter/edit details on incident locations.

- Select a station and location of injury from the dropdown lists.
- If you are adding a new detail, click the Add button. Enter the text (maximum 30 characters) and click the OK button. Click the Save button to save your entry.
- If editing an existing detail, select the detail in the Location of Injury Details box and click the Edit button. Edit the text as necessary and click the OK button. Click the Save button to save your entry.

Location of Injury Detail entries may not be deleted. This would invalidate any existing cases that were linked to the entry.

![](asists-gui-version-2-user-manual/058.png)

![](asists-gui-version-2-user-manual/059.png)

Enter/Edit Location of Injury Detail

![](asists-gui-version-2-user-manual/060.png)

## Enter/Edit OSHA 300A Summary Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu under OSHA 300 Options.

The Enter/Edit OSHA 300A Summary option allows the safety official to enter station-specific safety and industrial information, in addition to month/year specific OSHA 300 information. The safety official chooses the station selection from a list box. All the station entries that have been entered through the Edit Site Parameter option will be displayed as valid selections for the station.

![](asists-gui-version-2-user-manual/061.png)

The station-specific safety information includes the Safety Official Name, Safety Official Title, Safety Phone Number, and Safety Phone Extension.

Enter/Edit OSHA 300A Summary Data

The station-specific industrial information includes the Industry Description, Standard Industrial Classification (SIC) code, and North America Industrial Classification (NAICS) code. For an integrated site, the industrial information must be entered for each station.

- Industry Description – free text, no special characters such as \*^()&\$#@?\<\>, required field
- Standard Industrial Classification (SIC) – numeric value, must be 4 digits with range 0000-9999; table-driven
- North America Industrial Classification (NAICS) – numeric value, must be 6 digits with range 000000-999999; table-driven

The Month/Year specific OSHA 300A summary information consists of the Average Number of Employees and Total Hours Worked By Employees per month for the current year. When the safety official chooses to enter/edit OSHA 300A information, the following data fields are included.

- Month – defaults to current month; selectable values are January through December (calendar year)
- Average Number of Employees and Total Hours Employee Worked information is entered by month per year. This information is required.

The monthly OSHA 300A Summary information can be edited for the current year until the end of Feb of the next year. Beginning on March 1<sup>st</sup>, the previous year’s information can be viewed but not edited.

A user can enter/edit the safety information and industrial information and save their changes without affecting the OSHA 300A Summary information.

A user can add or edit the OSHA 300A Summary data for one or more months and view the changes (i.e., update the display) before saving or canceling the information.

## Enter/Edit Union Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu.

The Enter/Edit Union Information option provides workers’ compensation personnel the ability to enter or edit union representative information. This information is used to determine which union representative shall receive union bulletins when so designated by the employees.

![](asists-gui-version-2-user-manual/062.png)

*Add/Edit Union*

To add or edit a union, press the appropriate button. The number of unions that can be added is unlimited. Press the Save button to save the changes.

The following information is displayed on the Union Information screen.

Union Name This is the formal name of the union.

Union Acronym This field is the union’s acronym or abbreviation; e.g., AFGE.

Union Representative Click this button to select the union representative .

Union Representative Name This field contains the union representative's name for the

union. It will be used to send the Mailman bulletin if the

employee consents to sending information regarding their

claim to the union.

Enter/Edit Union Information

![](asists-gui-version-2-user-manual/063.png)

*Delete Union*

To delete a union, select the desired union from the union list and press the Delete button. The following confirmation message will be displayed.

![](asists-gui-version-2-user-manual/064.png)

Press Yes to delete the union or No to return to the union form without deleting. If Yes is pressed and the union is successfully deleted, the following message will display.

![](asists-gui-version-2-user-manual/065.png)

## Filing Instructions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu under Reports.

Use this screen to print or print preview the Filing Instruction Report for a given time frame, for a single station, or all stations.

![](asists-gui-version-2-user-manual/066.png)

Filing Instructions Report

![](asists-gui-version-2-user-manual/067.png)

## Location of Injury Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu under Reports.

The Location of Injury Report displays the number of incidents for a user-selected date range for all stations or a single station. Information provided includes type of incident, location of injury, location detail, and the total number of incidents for each. A cumulative total is also displayed.

Output formats include Standard Report or Excel spreadsheet.

![](asists-gui-version-2-user-manual/068.png)

Location of Injury Report

Example of Standard Report format

![](asists-gui-version-2-user-manual/069.png)

Location of Injury Report

Excel Spreadsheet format

![](asists-gui-version-2-user-manual/070.png)

## Log of Federal Occupational Injuries and Illnesses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety and Union Menus under Reports.

The option prints the Log of Federal Occupational Injuries and Illnesses. Logs can be printed for a date range determined by when the record was first created (Date/Time of Occurrence). This report compiles data from the Report of Incident where the *Include on OSHA Log field* equals YES.

The log prints the Case Number, Date of Occurrence, Name, Pay Plan and Occupation Code, Department, Type of Incident, and Body Part Affected. It also indicates with an X whether the claim resulted in a fatality, lost time, or no lost time, for both injuries and illnesses.

![](asists-gui-version-2-user-manual/071.png)

Log of Federal Occupational Injuries and Illnesses

![](asists-gui-version-2-user-manual/072.png)

## Log of Needlestick Incidents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Occupational Health, Safety, and Workers’ Comp Menus under Reports.

This option prints the Log of Needlestick Incidents report. This report compiles data from the Report of Incident when the Type of Incident is a Hollow Bore Needlestick, Sharps Exposure, Exposure to Body Fluids/Splash, or a Suture Needlestick.

Before the report can be displayed or printed, the user must select the start and end dates along with the station. The report can be run for all stations or a single station. If all stations is selected, the report is not sorted by station. The words *Privacy Case* will print in place of the name for every case on this report.

The Lost Time column has been added back into this report. If the response to the "Initial Return to Work Status" is *Days Away Work*, then YES will be printed in this column; otherwise, NO will be printed.

![](asists-gui-version-2-user-manual/073.png)

Log of Needlestick Incidents

![](asists-gui-version-2-user-manual/074.png)

## Manual Transmission of DOL Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu.

The Manual Transmission of DOL Data option provides workers’ compensation personnel the ability to manually resend CA-1 or CA-2 data that was previously queued to the Austin Automation Center (AAC) for transmission to the Department of Labor (DOL). The CA-1 or CA-2 data can be transmitted immediately or queued for future transmission.

A security key is required to access this option and should be assigned to individuals responsible for sending CA-1 or CA-2 data to the AAC.

This option should ONLY be used when the transmission to the AAC was corrupt or not completely received. This option is NOT designed to retransmit a single case.

![](asists-gui-version-2-user-manual/075.png)

## Manual Transmit of National Database Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Safety Menu.

The Manual Transmit of National Database Data option provides the safety official the ability to manually resend incident data that was previously queued to the Austin Automation Center (AAC) for transmission to the ASISTS National Database (NDB). The data can be transmitted immediately or queued for future transmission.

Data is extracted from incident reports to provide statistical reporting on safety incidents that occur at facilities nationwide. Reports will be periodically generated from the NDB to identify safety incident trends and to support prevention programs for health care workers’ exposure to bloodborne pathogens. The data collected from the Report of Incident should be transmitted to the ASISTS National Database (NDB) on a daily basis.

This option should ONLY be used when the transmission to the AAC was corrupt or not completely received. This option is NOT designed to retransmit a single case.

![](asists-gui-version-2-user-manual/076.png)

## Print Blank CA1/CA2/CA7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu.

The Print Blank CA1/CA2/CA7 option provides workers’ comp personnel the ability to print a blank CA1, CA2, or CA7 form should there be a need to fill one out manually.

![](asists-gui-version-2-user-manual/077.png)

Blank CA1

![](asists-gui-version-2-user-manual/078.png)

Print Blank CA1/CA2/CA7

Blank CA2

![](asists-gui-version-2-user-manual/079.png)

Print Blank CA1/CA2/CA7

Blank CA7

![](asists-gui-version-2-user-manual/080.png)

## Print CA1/CA2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Supervisor and Workers’ Comp Menus.

The Print CA1/CA2 option provides personnel the capability to view on a computer screen or print a hardcopy of the CA1 or CA2 form for an individual. This option also serves as a means to view/print a list of open cases noting the presence or lack of electronic signatures.

![](asists-gui-version-2-user-manual/081.png)

![](asists-gui-version-2-user-manual/082.png)

## Print CA7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu.

![](asists-gui-version-2-user-manual/083.png)

Use this selection screen to either print or print preview a selected claim from the list box. The Print button sends the printed version of the selected claim to the windows default printer. Print Preview displays the report to the screen.

![](asists-gui-version-2-user-manual/084.png)

Print CA7

![](asists-gui-version-2-user-manual/085.png)

## ## ## Print Dual Benefits Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu.

Use this screen to select the claim for which you wish to print the Dual Benefits Form. You can print the report to your Window’s default printer or display the report to the computer screen.

![](asists-gui-version-2-user-manual/086.png)

![](asists-gui-version-2-user-manual/087.png)

## Print Incident Report Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Supervisor Menu and on the Occupational Health, Safety, Workers’ Comp, and Union Menus under Reports.

The Print Incident Report Status option provides Occupational Health Unit personnel, supervisor, safety official, union personnel, or workers’ compensation personnel the ability to view the Incident Report Status on a computer screen or print a hardcopy. This option also serves as a means to view/print a list of open cases noting the presence or lack of electronic signatures.

Before the Incident Report Status can be displayed or printed, the user must select the start and end dates along with the station. The report can be run for all stations or single station. If all stations is selected, the report is not sorted by station. The user must also indicate the case status to be included on the report.

![](asists-gui-version-2-user-manual/088.png)

Print Incident Report Status

![](asists-gui-version-2-user-manual/089.png)

## Print Report of Incident

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Supervisor Menu and on the Occupational Health, Safety, Workers’ Comp, and Union Menus under Reports.

The Print Report of Incident option provides Occupational Health Unit personnel, supervisor, safety official, union personnel, or workers’ compensation personnel the ability to print a hardcopy of the Report of Incident or view the report on the computer screen.

![](asists-gui-version-2-user-manual/090.png)

An example report begins on the following page.

Print Report of Incident

![](asists-gui-version-2-user-manual/091.png)  
Print Report of Incident

![](asists-gui-version-2-user-manual/092.png)  
Print Report of Incident

![](asists-gui-version-2-user-manual/093.png)

## Reason for Controvert Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu under Reports.

The user is asked to enter a start date, end date, and either a single station or all stations. The report gives a count of the number of each of the following reason for controvert codes for both lost time and no lost time cases.

- The disability was not caused by a traumatic injury
- The employee is a volunteer working without pay or for nominal pay, or a member of the office staff of a former president
- The employee is not a citizen or resident of the United States or Canada
- The injury occurred off the employing agencies premises and the employee was not involved in official off premises duty
- The injury was proximately caused by the employee misconduct, intent to bring about injury or death to self or another person, or intoxication
- The injury was not reported on Form CA-1 within 30 days following the injury
- Work stoppage first occurred 45 days or more following the injury
- The employee initially reported the injury after his or her employment was terminated
- The employee is enrolled in the Civil Air Patrol, Peace Corps, Youth Conservation Corps, Work Study Programs, or other similar groups

> **NOTE:** The last item is NOT a Controvert code but is included to handle those possible scenarios.

The report will indicate the number of cases in the total count that had data in block 36 (State the Reason in Detail) and the number of cases not controverted in the report date range.

Reason for Controvert Report

![](asists-gui-version-2-user-manual/094.png)

Reason for Controvert Report

## ![](asists-gui-version-2-user-manual/095.png) Reason for Dispute Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Workers’ Comp Menu under Reports.

The Reason for Dispute Report provides the capability to view the number of dispute code occurrences (for lost time and no lost time cases) for a single station or all stations within a user-specified date range.

The user is asked to enter a start date, end date, and either a single station or all stations. The report gives a count of the number of each of the following reason for dispute codes for both lost time and no lost time cases.

- A personal, emotional, reaction to administrative activities
- Different medical opinions about injury; weight of evidence
- Different stories about what happened
- Employee did not follow facility policies/procedures
- Inappropriate medical provider
- Injury was not work related
- Investigation of incident does not support employee’s statement
- Medical diagnosis/treatment not related to claimed condition
- No medical evidence to support work related injury
- Timeliness of reporting incident

The report will indicate the number of cases in the total count that had data in block 36 (State the Reason in Detail) and the number of cases not disputed in the report date range.

![](asists-gui-version-2-user-manual/096.png)

Reason for Dispute Report

## ![](asists-gui-version-2-user-manual/097.png) Request for Compensation (CA7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Employee and Workers’ Comp Menus.

The Request for Compensation (CA7) option allows either the employee or worker’s compensation personnel to enter information for a request for compensation. There are 6 tab sheets on the CA7 Form. The first three tabs of the form are accessible by both the employee and worker’s compensation personnel; the last 3 tabs on the form can only be accessed by workers’ compensation personnel.

Selecting the Create CA7 button after you have selected the associated CA claim will initiate and create a new CA7 claim with some of the fields auto populated. The CA7 screen is then displayed with all of the associated tab fields available for editing. It is important to remember that the claim will not actually be created/saved until you either click Save on the CA7 form or try to exit the form. After you have selected a CA claim and have clicked the Create CA7 button, a message is displayed that the information for the new CA7 has been populated on the form, but the claim will not be created until the information is saved.

![](asists-gui-version-2-user-manual/098.png)

![](asists-gui-version-2-user-manual/099.png)

![](asists-gui-version-2-user-manual/100.png)

Request for Compensation (CA7)

### Sections 1-2 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 1-2 tab contains the majority of the employee information such as mailing address, Date of Incident, OWCP file number. This tab can be accessed by both the employee and workers’ compensation representative.

Section 2 of this tab involves the reason for filing the CA7. A separate CA7 must be completed by the employee for each option they choose to file.

![](asists-gui-version-2-user-manual/101.png)

Request for Compensation (CA7)

### Sections 3-4 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 3-4 tab contains outside business work information and questions concerning previous claims and dependent information. This tab can be accessed by both the employee and workers’ compensation representative.

![](asists-gui-version-2-user-manual/102.png)

Request for Compensation (CA7)

### Sections 5-6 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 5-6 tab contains dependent, support payments, and questions concerning previous disability claims and annuity information. This tab can be accessed by both the employee and workers’ compensation representative.

![](asists-gui-version-2-user-manual/103.png)

Request for Compensation (CA7)

### Section 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 7 is the Election of Benefits Statement. This is a statement signed by the employee to certify that he/she has been truthful on the CA-7 form. There is not a Section 7 tab displayed in this option because there is no data for the user to input. This statement is printed when the user elects to print the CA-7 form.

> I hereby make claim for compensation because of the injury sustained by me while in the performance of my duty for the United States. I certify that the information provided above is true and accurate to the best of my knowledge and belief. Official statement made by the employee that the information they wrote on this CA-7 form is the truth as it is against the law to make any false statements or hide information to get money from OWCP.

> Employee’s Electronic Signature \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Date:  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The employee must print out the CA-7, sign it in blue ink, then give the original to the Workers’ Compensation office at their facility on the same day they sign it. The employee should also keep a copy for their records.

Request for Compensation (CA7)

### Sections 8-9 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 8-9 tab contains the employee’s pay rate information (both current and pay when work stopped) along with their work schedule. This tab is available only to workers’ compensation personnel.

![](asists-gui-version-2-user-manual/104.png)

Request for Compensation (CA7)

### Sections 10-13 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 10-13 tab contains health benefits, insurance, and retirement questions. This is also the tab where continuation of pay (COP), pay status, and whether or not the employee returned to work information is entered. This tab is available only to workers’ compensation personnel.

![](asists-gui-version-2-user-manual/105.png)

Request for Compensation (CA7)

### Sections 14-15 Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Sections 14-15 tab contains the workers’ compensation remarks and their information including a place to enter a third party that could be contacted for further information on the claim. This tab is available only to workers’ compensation personnel.

![](asists-gui-version-2-user-manual/106.png)

## Summary Incident Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be found on the Occupational Health, Safety, and Workers’ Comp Menus under Reports.

Each report summarizes the number of incidents grouped by various fields. The input criteria is the same for each report type. The report types are as follows.

Type of Incidents Summarizes the number of incidents grouped on the critical

tracking issues

Occupational Code Summarizes the number of incidents grouped by the

occupational code of the individual

Characterization of Injury Summarizes the number of incidents grouped by the

Characterization of Injury field

Service Summarizes the number of incidents grouped by the service

of the individual

Body Part Summarizes the number of incidents grouped by major body part

Day of Week Summarizes the number of incidents grouped by each day of the

week the incident occurred

Time of Day Groups each incident by hour and summarizes the number of

incidents within those time periods

The different output formats include Standard Report, Excel Spreadsheet, Pie Chart, and Bar Graph. The pie chart and bar graph formats print in the landscape orientation.

Summary Incident Reports

![](asists-gui-version-2-user-manual/107.png)

Example of Standard Report Output Format

![](asists-gui-version-2-user-manual/108.png)

# About ASISTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen acknowledges the West Palm Beach programming staff for their contribution to the ASISTS software. It also provides version and CRC (Delphi-generated identification) code information.

![](asists-gui-version-2-user-manual/109.png)

## Technical Support 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Service Desk (formerly Help Desk) can be reached at 1-888-596-4357.

## Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Release Notes for current and past ASISTS GUI V. 2.0 patches, please go to the ASISTS Training page on the VistaU website at: REDACTED

##