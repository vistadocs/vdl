---
title: Network Health Exchange Version 5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: AFJX
app_name: Network Health Exchange (NHE)
section: INF
app_status: active
pkg_ns: AFJX
patch_ver: 5
patch_id: AFJX*5
group_key: "AFJX:AFJX:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Simple User Interface](#simple-user-interface) - [Retrieval and Printing of Patient Data](#retrieval-and-printing-of-patient-data) - [Quick Response](#quick-response) - [Data Returned in VistA Health Summary Format](#data-returned-in-vista-health-summary-format) - [User Notification with Alerts](
audience: 
keywords: 
  - patient
  - health
  - exchange
  - network
  - table
  - contents
  - vista
  - returned
  - summary
  - clinical
page_count: 0
word_count: 856
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=79"
---

## Table of Contents

    - [Simple User Interface](#simple-user-interface)
    - [Retrieval and Printing of Patient Data](#retrieval-and-printing-of-patient-data)
    - [Quick Response](#quick-response)
    - [Data Returned in VistA Health Summary Format](#data-returned-in-vista-health-summary-format)
    - [User Notification with Alerts](#user-notification-with-alerts)
    - [VISN Network Health Exchange Partners](#visn-network-health-exchange-partners)
    - [Purging Retrieved Patient Data](#purging-retrieved-patient-data)
    - [Special Security Features](#special-security-features)
    - [Software Management](#software-management)
![](network-health-exchange-version-5-release-notes/001.png)
NETWORK HEALTH EXCHANGE (NHE)RELEASE NOTES
February 1996
VistA Health Systems Design & Development (HSD&D)
Infrastructure and Security Services (ISS)
Network Health Exchange
Release Notes
The Network Health Exchange (NHE) was created by the Chicago Westside Veterans Affairs Medical Center (VAMC) and has gone through several iterations. This version of the software is being released as an interim bridge to a more fully integrated clinical patient data exchange system. Network Health Exchange (NHE) allows VAMC clinicians easy access to clinical patient data. The requester is notified of returned patient data through an alert that appears within the Veterans Health Information Systems and Technology Architecture (VistA) menu system. The patient data can be viewed onscreen or printed. It is displayed in a format similar to the integrated clinical reports in Health Summary.
The Network Health Exchange (NHE) is another tool, similar to Patient Data Exchange (PDX), comprising the VistA Master Patient Index (MPI). As compared to PDX, Network Health Exchange (NHE) offers fewer retrieval options requiring less input by the user. This results in a simpler, faster access to patient data using predefined formats. Clinicians have reported that NHE is easy to learn and use.

### Simple User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange offers a simple user interface to retrieve and print patient data. Users simply select the data type (Clinical or Pharmacy only) and amount of patient data (full or 12 months) they would like returned, then enter the patient's name (last,first) or Social Security Number (SSN), in order to initiate the request for data from another VA facility.

### Retrieval and Printing of Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinicians can use the Network Health Exchange menu to select Pharmacy or Medical Record information for patients, either a comprehensive history or limited to activity within the last 12 months. Retrieved patient data can be printed or viewed onscreen.

### Quick Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Network Health Exchange (NHE) is a fully automated process. Unlike PDX, a user's request for a clinical patient data is *not* subject to human intervention or review. Thus, responses to user requests are generally fulfilled in a matter of minutes by the responding VistA computer system.

### Data Returned in VistA Health Summary Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient data is returned in a Network Health Exchange (NHE) mail message, formatted similarly to the VistA Health Summary. However, it is not necessary to have Health Summary installed in order to use this software.
NHE messages begin with patient demographics, followed by categorized medical information. The title line of each NHE message contains the name of the VA facility where the data resides. NHE messages are reviewed by entering the NHE message number at the appropriate prompt. The user can enter up to 10 NHE message numbers at one time separated by commas.

### User Notification with Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user requesting patient data via Network Health Exchange (NHE) is notified of data receipt through an alert that appears within the VistA menu system. Alerts are notices to the user of an urgent, time-sensitive, pending matter; in this case, a returned request for patient data. The alert can be processed onscreen or printed by entering "VA at the "Enter "VA VIEW ALERTS to review data" prompt. Returned patient data is accessed through the NHE menu options.

### VISN Network Health Exchange Partners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange (NHE) allows patient data to be exchanged between VA facilities. VISN sites can establish groups for patient data exchange among VA facilities within the VISN. The VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025) is comprised of domain names for authorized VA sites.

### Purging Retrieved Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange (NHE) provides an option to purge the retrieved patient data messages nightly. This provides sites with the means to control disk space usage.

### Special Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This system is intended for use by health professionals who have direct patient care responsibilities and have need for clinical information.
Network Health Exchange (NHE) generates a bulletin if data is requested for a *sensitive* patient. This bulletin is directed to the same user group that currently reviews notices about access to *sensitive* patient records.

### Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The availability of VistA Network Health Exchange (NHE) options is based on the level of menu access granted to each user.
