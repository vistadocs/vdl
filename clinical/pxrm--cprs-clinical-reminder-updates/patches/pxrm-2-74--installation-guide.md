---
title: PXRM*2*74 COVID-19 CPRS Status Version 5
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: COVID-19 CPRS Status Version 5
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*74
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > This update will update the CPRS BANNER to Version 5. To keep from having to remap your Lab and Orderable Item terms, we will ask you to do an INSTALL SELECTED for items 10,22 and 25. Detailed information provided below in installation section. > This reminder content contains 1 Reminder Exchange
audience: 
keywords: 
  - install
  - table
  - contents
  - reminder
  - clinical
  - reminders
  - guide
  - august
  - details
  - example
page_count: 0
word_count: 113
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_va_covid_19_cprs_status_version_5_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_va_covid_19_cprs_status_version_5_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-74-covid-19-cprs-status-version-5/001.png)

> VA-COVID-19 CPRS STATUS VERSION 5

# Clinical Reminders Install Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Clinical Reminders Install Guide](#clinical-reminders-install-guide)
    - [August 2020](#august-2020)
  - [Pre-install](#pre-install)
- [Install Details](#install-details)
- [Install Example](#install-example)

### August 2020

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Product Development Office of Information Technology Department of Veterans Affairs

#### Introduction

> This update will update the CPRS BANNER to Version 5. To keep from having to remap your Lab and Orderable Item terms, we will ask you to do an INSTALL SELECTED for items 10,22 and 25. Detailed information provided below in installation section.
> This reminder content contains 1 Reminder Exchange entry:

#### VA-COVID-19 CPRS STATUS VERSION 5

> The exchange file contains the following components: HEALTH FACTORS
> VA-COVID-19
> VA-COVID-19 NO LONGER SUSPECTED
> VA-COVID-19 INCORRECT PRIOR POSITIVE PCR VA-COVID-19 RESOLVED
> VA-COVID-19 SUSPECTED
> VA-COVID-19 OUTSIDE PCR SPEC COLLECTED VA-COVID-19 PCR LAB OUTSIDE NEGATIVE VA-COVID-19 PCR LAB OUTSIDE POSITIVE

#### REMINDER COMPUTED FINDINGS

> VA-DATE OF DEATH

#### REMINDER TAXONOMY

> VA-COVID-19 SNOMED CODES

#### REMINDER TERM

> VA-COVID-19 PROB LIST DX VA-COVID-19 PCR LAB ORDERS VA-COVID-19 CLINICAL INFO
> VA-COVID-19 OUTSIDE RESULTS VA-COVID-19 PRESUMED
> VA-COVID-19 ANTIBODY LAB TEST VA-COVID-19 PCR/AG LAB RESULTS VA-COVID-19 NO LONGER PRESUMED
> VA-COVID-19 INCORRECT PRIOR POSITIVE PCR RESULT VA-COVID-19 PCR LAB RESULTS POSITIVE
> VA-COVID-19 OUTSIDE PCR LAB POSITIVE
> VA-COVID-19 OUTSIDE PCR SPECIMEN COLLECTED VA-COVID-19 RECOVERED
> VA-COVID-19 OUTSIDE PCR LAB NEGATIVE VA-COVID-19 PCR LAB RESULTS NEGATIVE

#### REMINDER DEFINITION

> VA-COVID-19 CPRS STATUS

## Pre-install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may want to save a printout of your reminder terms which contain your COVID-19 lab tests and COVID-19 Orderable items in case these are accidentally overwritten.

> The terms you may want to save are:

> VA-COVID-19 ANTIBODY LAB TEST – only for COVID antibody Lab Tests VA-COVID-19 PCR LAB ORDERS – only for PCR Orderable items

> VA-COVID-19 PCR LAB RESULTS NEGATIVE – only for PCR Lab Tests VA-COVID-19 PCR LAB RESULTS POSITIVE – only for PCR Lab Tests

> VA-COVID-19 PCR/AG LAB RESULTS – only for PCR Lab tests

# Install Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This update is being distributed as a web host file. The address for the host file is:

<span class="mark">REDACTED</span>

> The file will be installed using Reminder Exchange, programmer access is not required.

> Installation:

> =============

> This update can be loaded with users on the system. Installation will take less than 10 minutes

# Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To Load the Web Host File. Navigate to Reminder exchange in Vista

![](pxrm-2-74-covid-19-cprs-status-version-5/002.png)

> At the Select Action: prompt, enter LWH for Load Web Host File

> At the Input the url for the .prd file: prompt, type the following web address: https://vaww.va.gov/reminders/docs/COVID_VERSION_5.PRD You should see a message at the top of your screen that the file loaded successfully

> ![](pxrm-2-74-covid-19-cprs-status-version-5/003.png)

> Search and locate an entry titled VA-COVID-19 CPRS STATUS VERSION 5 in reminder exchange

![](pxrm-2-74-covid-19-cprs-status-version-5/004.png)

> At the Select Action prompt, enter IFE for Install Exchange File Entry

> Enter the number that corresponds with your entry titled VA-COVID-19 CPRS STATUS VERSION 5 *(in this example it is entry 337, it will vary by site).* Ensure the date of the exchange file is 08/07/2020

> ![](pxrm-2-74-covid-19-cprs-status-version-5/005.png)

> At the Select Action prompt, type IS for Install Selected Components. Choose items 10, 22 and 25 to install and hit enter.

> You will INSTALL all NEW components. When prompted for an action on the Reminder Definition, user OVERWRITE action

> REMINDER TERM entry VA-COVID-19 PROB LIST DX is NEW,

> what do you want to do?

> Select one of the following:

> C Create a new entry by copying to a new name I Install

> Q Quit the install

> S Skip, do not install this entry Enter response: I// nstall

> REMINDER TERM entry named VA-COVID-19 RECOVERED already exists but the packed component is different, what do you want to do?

> Select one of the following:

> C Create a new entry by copying to a new name M Merge findings

> O Overwrite the current entry

> U Update

> Q Quit the install

> S Skip, do not install this entry Enter response: O// verwrite the current entry

> Are you sure you want to overwrite? N// YES

> REMINDER DEFINITION entry named VA-COVID-19 CPRS STATUS already exists but the packed component is different, what do you want to do?

> Select one of the following:

> C Create a new entry by copying to a new name O Overwrite the current entry

> U Update

> Q Quit the install

> S Skip, do not install this entry Enter response: O// verwrite the current entry

> Are you sure you want to overwrite? N// Y

> You may then Quit the Install

> <span class="mark">REDACTED</span>