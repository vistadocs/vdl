---
title: ROES Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: ROES
app_name: Remote Order Entry System
section: CLI
app_status: active
pkg_ns: ROES
patch_ver: 3
patch_id: ROES*3
group_key: "ROES:ROES:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Remote Order Entry System (ROES) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC). This manual provides instructions for the use of the ROES 3.0 software. The information in this manual is intended fo
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - order
  - roes
  - table
  - contents
  - manual
  - patient
  - version
  - button
  - form
  - dalc
page_count: 0
word_count: 33264
section_count: 37
table_count: 6
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=99"
---

![](roes-version-3-user-manual/001.png)

Remote Order Entry System

(ROES)

User Manual

![](roes-version-3-user-manual/002.png)

Version 3.0\*4

Updated February 2011

VistA Health Systems Design and Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Preface](#preface)
  - [Purpose of the Remote Order Entry System](#purpose-of-the-remote-order-entry-system)
  - [Scope of Manual](#scope-of-manual)
  - [Audience](#audience)
  - [Related Manuals](#related-manuals)
- [Introduction](#introduction)
  - [Purpose of ROES 3.0](#purpose-of-roes-30)
  - [Benefits of ROES 3.0](#benefits-of-roes-30)
  - [General Rules for ROES 3.0 Data Entry pages](#general-rules-for-roes-30-data-entry-pages)
  - [ROES 3.0 Display Considerations](#roes-30-display-considerations)
- [Orientation](#orientation)
  - [Organization of User Manual](#organization-of-user-manual)
- [Access Through CPRS](#access-through-cprs)
- [Screens](#screens)
  - [View Order History](#view-order-history)
    - [Heading Section](#heading-section)
    - [Existing Orders Section](#existing-orders-section)
    - [Actions Section](#actions-section)
    - [Command Section](#command-section)
- [Detail Pages](#detail-pages)
  - [Custom Hearing Aid Order Detail](#custom-hearing-aid-order-detail)
    - [Heading Section](#heading-section-1)
    - [Command Section](#command-section-1)
  - [Commodity Detail](#commodity-detail)
    - [Heading Section](#heading-section-2)
    - [Order Summary Section](#order-summary-section)
    - [Command Section](#command-section-2)
  - [Service Request Detail](#service-request-detail)
    - [Heading Section](#heading-section-3)
    - [Service Request Section](#service-request-section)
    - [Command Section](#command-section-3)
  - [Commodity Ordering (Patient)](#commodity-ordering-patient)
    - [Commodity Order](#commodity-order)
    - [Heading Section](#heading-section-4)
    - [Order Section](#order-section)
    - [Command Section](#command-section-4)
  - [Special Request Order](#special-request-order)
    - [Heading Section](#heading-section-5)
    - [Order Section](#order-section-1)
    - [Command Section](#command-section-5)
  - [ROES Order Summary](#roes-order-summary)
    - [Summary Section](#summary-section)
    - [Command Section](#command-section-6)
  - [Custom Hearing Aids (Patient)](#custom-hearing-aids-patient)
    - [Page 1 - Hearing Aid Information](#page-1-hearing-aid-information)
    - [Heading Section](#heading-section-6)
    - [Order Section](#order-section-2)
    - [Command Section](#command-section-7)
    - [Page 2 - ROES Hearing Aid Cost Analysis Table](#page-2-roes-hearing-aid-cost-analysis-table)
    - [Heading Section](#heading-section-7)
    - [Display SectionVendor Column: The vendor name is displayed as well as the ![](roes-version-3-user-manual/063.png) button described above. The same vendor name may be displayed multiple times if the vendor has more than one model fitting the search criteria. Only one entry is shown on this page when you select a specific make and model from the first page.](#display-sectionvendor-column-the-vendor-name-is-displayed-as-well-as-the-roes-version-3-user-manual063png-button-described-above-the-same-vendor-name-may-be-displayed-multiple-times-if-the-vendor-has-more-than-one-model-fitting-the-search-criteria-only-one-entry-is-shown-on-this-page-when-you-select-a-specific-make-and-model-from-the-first-page)
    - [Command Section](#command-section-8)
    - [Page 3 - Circuits/Components/Secondary Features](#page-3-circuitscomponentssecondary-features)
    - [Heading Section](#heading-section-8)
    - [Order SectionCircuit (required): Click on the drop down box to see the circuits that are available for the selected model. Only those circuits compatible with the selected model and allowed with the hearing aid bundle will be presented. When the desired circuit is selected the system may require several seconds for the database to be searched for compatible components and secondary features. After a pause, the page will be refreshed and the components and secondary features may then be selected.](#order-sectioncircuit-required-click-on-the-drop-down-box-to-see-the-circuits-that-are-available-for-the-selected-model-only-those-circuits-compatible-with-the-selected-model-and-allowed-with-the-hearing-aid-bundle-will-be-presented-when-the-desired-circuit-is-selected-the-system-may-require-several-seconds-for-the-database-to-be-searched-for-compatible-components-and-secondary-features-after-a-pause-the-page-will-be-refreshed-and-the-components-and-secondary-features-may-then-be-selected)
    - [Command Section](#command-section-9)
    - [Page 4 - Audiometric Data/Vendor Information](#page-4-audiometric-datavendor-information)
    - [Order SectionAir and Bone Conduction (KHz) (Audiometric Data): In the event that audiometric exam data has not been transmitted to the DALC from the clinic, air and bone conduction values may be entered by clicking on the appropriate text box and entering the value. The air and bone conduction values will be printed out on the vendor order form.](#order-sectionair-and-bone-conduction-khz-audiometric-data-in-the-event-that-audiometric-exam-data-has-not-been-transmitted-to-the-dalc-from-the-clinic-air-and-bone-conduction-values-may-be-entered-by-clicking-on-the-appropriate-text-box-and-entering-the-value-the-air-and-bone-conduction-values-will-be-printed-out-on-the-vendor-order-form)
    - [Command Section](#command-section-10)
    - [Page 5 - Custom Hearing Aid Order Summary](#page-5-custom-hearing-aid-order-summary)
    - [Display Section](#display-section)
    - [Command Section](#command-section-11)
  - [FMs/Remotes](#fmsremotes)
    - [ROES FM Device/Remote Control Order Form](#roes-fm-deviceremote-control-order-form)
    - [Heading Section](#heading-section-9)
    - [Order Section](#order-section-3)
    - [Command Section](#command-section-12)
    - [ROES FM/Remote Control Device Order Summary](#roes-fmremote-control-device-order-summary)
    - [Display Section](#display-section-1)
    - [Command Section](#command-section-13)
  - [Service Requests (Patient)](#service-requests-patient)
    - [Service Request Form](#service-request-form)
    - [Page 1 - Service Request Form](#page-1-service-request-form)
    - [Heading Section](#heading-section-10)
    - [Service Request Section](#service-request-section-1)
    - [Page 2 - Service Request Form](#page-2-service-request-form)
    - [Heading Section](#heading-section-11)
    - [Command Section](#command-section-14)
    - [Page 3 - Service Request Form](#page-3-service-request-form)
    - [Heading Section](#heading-section-12)
    - [Service Request Section](#service-request-section-2)
    - [Command Section](#command-section-15)
    - [Page 4 - Service Request Summary](#page-4-service-request-summary)
    - [Heading Section](#heading-section-13)
    - [Service Request Section](#service-request-section-3)
    - [Command Section](#command-section-16)
    - [Page 5 - Hearing Aid Service Request Form](#page-5-hearing-aid-service-request-form)
  - [Cochlear Implant Registry](#cochlear-implant-registry)
    - [Page 1 – Cochlear Implant History](#page-1-cochlear-implant-history)
    - [Heading Section](#heading-section-14)
    - [History Section](#history-section)
    - [Command Section](#command-section-17)
    - [Page 2 – Cochlear Implant Registration Form](#page-2-cochlear-implant-registration-form)
    - [Order Section](#order-section-4)
    - [OutcomesPIPSL Score: This table is used to gather information prior to the implant and after the implant. You may enter a pre-measure score and a post-measure score for various methods of testing. Based on these scores, a benefit score is derived from subtracting the pre-measure score from the post-measure score. The methods used in the PIPSL scoring are: USV, INT, RAF, ES, USNV, and PER. The Benefit score is not editable.](#outcomespipsl-score-this-table-is-used-to-gather-information-prior-to-the-implant-and-after-the-implant-you-may-enter-a-pre-measure-score-and-a-post-measure-score-for-various-methods-of-testing-based-on-these-scores-a-benefit-score-is-derived-from-subtracting-the-pre-measure-score-from-the-post-measure-score-the-methods-used-in-the-pipsl-scoring-are-usv-int-raf-es-usnv-and-per-the-benefit-score-is-not-editable)
    - [Command Section](#command-section-18)
    - [Page 3 - Audiometric Data](#page-3-audiometric-data)
    - [Command Section](#command-section-19)
  - [Registering Devices](#registering-devices)
    - [Device Registration Form](#device-registration-form)
    - [Heading Section](#heading-section-15)
    - [Order Section](#order-section-5)
    - [Command Section](#command-section-20)
    - [ROES Device Registration Summary](#roes-device-registration-summary)
    - [Summary TableCommodity Group column: This is the commodity group as selected on the Device Registration Form.](#summary-tablecommodity-group-column-this-is-the-commodity-group-as-selected-on-the-device-registration-form)
  - [Record Updates (Patient)](#record-updates-patient)
    - [Record Update Form](#record-update-form)
    - [Heading Section](#heading-section-16)
    - [Update Section](#update-section)
    - [Demographic Updates](#demographic-updates)
    - [Edit Authorizing ClinicEligibility Station: This is the station responsible for care of the patient with regard to the disability on that line. Two choices are available in the drop down box – the patient’s current station of record and the user’s station. In order to edit the address information below, at least one eligibility station must be the same as the user’s station. In order to edit the authorized aids, the Eligibility Station for Deaf/B, Deaf/U, or A0/DIS must be the user’s station. You can make the change by selecting the correct station from the drop down box. You can ONLY change from the station shown to your station.](#edit-authorizing-cliniceligibility-station-this-is-the-station-responsible-for-care-of-the-patient-with-regard-to-the-disability-on-that-line-two-choices-are-available-in-the-drop-down-box-the-patients-current-station-of-record-and-the-users-station-in-order-to-edit-the-address-information-below-at-least-one-eligibility-station-must-be-the-same-as-the-users-station-in-order-to-edit-the-authorized-aids-the-eligibility-station-for-deafb-deafu-or-a0dis-must-be-the-users-station-you-can-make-the-change-by-selecting-the-correct-station-from-the-drop-down-box-you-can-only-change-from-the-station-shown-to-your-station)
    - [Change AddressNew Address: The fields on the right side of this section display the patient’s current address with edit capability. The address can be changed by editing the related fields.](#change-addressnew-address-the-fields-on-the-right-side-of-this-section-display-the-patients-current-address-with-edit-capability-the-address-can-be-changed-by-editing-the-related-fields)
    - [Edit Authorized Aids](#edit-authorized-aids)
    - [Command Section](#command-section-21)
  - [Authorized Aids](#authorized-aids)
    - [Heading Section](#heading-section-17)
    - [Authorized Aids Section](#authorized-aids-section)
    - [Command Section](#command-section-22)
  - [Delivery Address Pages](#delivery-address-pages)
    - [Patient Delivery Address](#patient-delivery-address)
    - [Command Section](#command-section-23)
    - [Station Delivery Address](#station-delivery-address)
    - [Command Section](#command-section-24)
- [Access from the Desk Top](#access-from-the-desk-top)
  - [ROES Desk Top Entry Page](#roes-desk-top-entry-page)
    - [Desk Top Entry Page Links](#desk-top-entry-page-links)
  - [Patient Actions](#patient-actions)
  - [Patient Information](#patient-information)
    - [Header Section](#header-section)
    - [Command Section](#command-section-25)
  - [Station Actions](#station-actions)
    - [View Station Order History](#view-station-order-history)
    - [Heading Section](#heading-section-18)
    - [Existing Orders Section](#existing-orders-section-1)
    - [Actions Section](#actions-section-1)
    - [Command Section](#command-section-26)
    - [Station Stock Order Form](#station-stock-order-form)
    - [Heading Section](#heading-section-19)
    - [Order Section](#order-section-6)
    - [Command Section](#command-section-27)
    - [Stock Special Request Order Form](#stock-special-request-order-form)
    - [Heading Section](#heading-section-20)
    - [Order Section](#order-section-7)
    - [Command Section](#command-section-28)
    - [Station Stock Summary](#station-stock-summary)
    - [Summary Section](#summary-section-1)
    - [Command Section](#command-section-29)
  - [Managing ROES 3.0 Orders](#managing-roes-30-orders)
    - [System Parameters](#system-parameters)
    - [Command Section](#command-section-30)
  - [Pending Actions](#pending-actions)
    - [View Pending Actions Section](#view-pending-actions-section)
    - [ROES Orders – Pending Approval](#roes-orders-pending-approval)
    - [ROES Orders – Pending Certification](#roes-orders-pending-certification)
    - [ROES Orders – Pending Issue](#roes-orders-pending-issue)
    - [Command Section](#command-section-31)
- [Glossary](#glossary)
- [Appendices](#appendices)
  - [A. How ROES 3.0\4 Calculates Eligibilities](#a-how-roes-304-calculates-eligibilities)
  - [B. Enrollment Priority Groups](#b-enrollment-priority-groups)
  - [C. Warranty Types](#c-warranty-types)
  - [D. Request Types](#d-request-types)
  - [E. Statuses](#e-statuses)
    - [For Processed Orders:](#for-processed-orders)
    - [For Unprocessed Orders:](#for-unprocessed-orders)
  - [F. Security Agreement](#f-security-agreement)
- [Index](#index)
- [2cc Coupler Gain 38](#2cc-coupler-gain-38)
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 44%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td>September 11, 2003</td>
<td>Format manual and input revisions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>September 18, 2003</td>
<td>Revised format</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>October, 17, 2003</td>
<td>Revised based on input from NVS</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2007</td>
<td><p>Changed DDC to DALC.</p>
<p>Changed the screen captures - substituted generic information for personal information and DDC to DALC</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>February 2011</td>
<td>Changes to eligibility calculations and removal of emails for ROES 3*4</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the Remote Order Entry System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System (ROES) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC).

## Scope of Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides instructions for the use of the ROES 3.0 software.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is intended for providers in Audiology and Speech Pathology Service (ASPS) and Prosthetics and Sensory Aids Service (PSAS).

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Remote Order Entry System (ROES) Version 3.0\*4 Installation GuideRemote Order Entry System (ROES) Version 3.0\*4 Security GuideRemote Order Entry System (ROES) Version 3.0\*4 Technical Manual*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System (ROES) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC). This manual provides instructions for the use of the ROES 3.0 software. The information in this manual is intended for providers in Audiology and Speech Pathology Service (ASPS) and Prosthetics and Sensory Aids Service (PSAS).

## Purpose of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 was developed to simplify and enhance the ordering of products and services from the Denver Acquisition & Logistics Center (DALC) including hearing aids and numerous other commodities. Ancillary functions such as updating patient records and registering devices may also be done through the web interface. ROES 3.0 is accessed from your workstation as a web application through your browser, allowing orders to be placed using an interactive, real time point and click interface. ROES 3.0 also accommodates keyboard navigation and entry.

ROES 3.0 was designed to use advanced technologies and practices in software design, supporting hardware platform, database management, and network integration to provide DALC customers and staff with simple and easy to use ordering capabilities. The application provides patient care providers and associated Veterans Health Administration (VHA) staff with comprehensive patient information and order histories. It was also designed to use progressive procurement and distribution practices, advanced general business practices, and current VA regulations, which have evolved since the introduction of ROES 2.0.

A definitive criterion used to establish the strategic direction and development path for ROES 3.0 involved combining:

The necessity to optimize compatibility and data communications capability with established VA systems and business practices

The objective of applying leading edge information technology resources to strategic business systems development, comparable to the best that can be found in the private sector

The desire to provide a "progressive continuity" to DALC customers, implementing significant enhancements to the existing application, while minimizing transition apprehension for end users

## Benefits of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES 3.0 application architecture makes available, for the first time, a web-based application for activities such as order placement and inquiry functions, while retaining and improving upon the functionality of the character-based interface formerly used in ROES 2.0. It is expected that a web interface, enabling point-and-click functionality, will allow information to be presented in a more organized fashion, enhancing the navigation and data entry procedures.

In another departure from previous versions, the majority of ROES 3.0 system software and data files reside on DALC computer resources, leaving only selected key components on local Medical Center systems. The factors supporting this transition include:

- Insurance of a singularity and consistency of the available product database
- Opportunity for immediate real-time processing of orders placed
- Reduced dependency on VAMC application of patches and file modifications
- The higher capacity VA wide area network resources implemented since ROES 2.0 enable these architectural changes.

In addition to the overall architecture, ROES 3.0 provides a number of process-specific benefits, features, and functionality improvements, such as the following:

- Provides users with a simplified ordering process.
- Includes cost comparison functionality for display/selection of all contract hearing aids meeting selected specifications.
- Allows repair orders to be entered by the provider.
- Includes a module to enter audiometric data and display or print the resulting audiogram in graph or tabular format.
- Provides information in "real time".
- Provides enhanced commodity ordering capabilities.
- Provides enhanced device registration capabilities.
- Provides enhanced display/update capabilities for authorized aids.
- Provides enhanced station stock ordering capabilities.
- Decreases delivery time to patients since orders are submitted immediately for processing.
- Links with the CPRS clinical record application already in place in the VHA environment.
- Provides increased accuracy in veteran eligibility determination prior to order placement, with improvements to subsequent reporting and statistical analysis.
- Provides access to multiple ROES 3.0 functions (clinical and administrative) through a comprehensive entry point.
- Provides supervisory designation of user authorization/approval levels.
- Provides a Cochlear Implant registry for tracking of cochlear implant information.
- Reduces the likelihood of erroneous orders (i.e., orders for combinations of device specifications that cannot be accommodated by hearing aid manufacturers).

## General Rules for ROES 3.0 Data Entry pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  There are no "double clicks" in ROES 3.0. Click the selection one time only.
2.  There are no "right mouse button” commands in ROES 3.0.

> NOTE: There is a key distinction between Windows-based applications (where double-clicks and right-button functionality are common) and web applications. There will not be a noticeable consequence to the user for these actions; however, the results may be unexpected. Double clicking may cause a drop-down list to open and close quickly. Right-clicking will produce selectable functions made available by the browser, but nothing specific to ROES. We strongly discourage use of the right-click in order to prevent the use of the browser's back and forward functions.

3.  It is recommended that users not click the "X" in the top right hand section of the ROES 3.0 browser window to close a window. Use the navigational links and buttons provided within the application to exit the system. Closing the browser window without properly exiting the application will not have any detrimental effects on the user but may leave an open user session and incomplete or 'phantom' order information in the application.
4.  Only use the ![](roes-version-3-user-manual/003.png) ![](roes-version-3-user-manual/004.png) or ![](roes-version-3-user-manual/005.png) command buttons provided on the ROES 3.0 pages for navigation - never use the windows provided "back" and "forward" commands.
5.  The command buttons within the application perform background housekeeping functions that maintain the integrity of the order as a user navigates through the ordering process. The Windows browser's 'Forward' and 'Back' commands bypass those functions and could result in loss of information from the order.
6.  “Grayed out” fields cannot be accessed.
7.  Any ![](roes-version-3-user-manual/006.png) button will return you to the *View OrderHistory* page.

## ROES 3.0 Display Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: ROES 3.0 application pages display best at a display resolution of 1024x768. If this is not an end user's preferred resolution, ROES pages will not appear properly formatted. This will not affect application functionality, but may make page content more difficult to understand and navigate. If an end user chooses to increase their resolution to 1024x768, they should be aware that all other Windows applications and objects in their Windows environment will be reduced in size.

# Orientation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Organization of User Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 can be accessed through two different methods, and each method makes available a different set of ROES functions.

Many ROES actions are patient-specific (i.e., order placement for custom hearing aids.) For these functions, ROES is integrated with and accessed from the CPRS application. This access method and the specific functions available are described in detail in the section entitled Access Through CPRS, beginning in the next section.

Vendor names displayed in examples are used for demonstration purposes only.

Other ROES actions either are not patient-specific or do not require CPRS integration (i.e., ordering items for station stock.) For these functions, a stand-alone (non-CPRS) application serves as the entry point into ROES 3.0. This is a Windows-style application that is intended to be available through a user's desktop shortcut created during the installation process. It is thus referred to throughout this manual as the 'desktop application'. This access method and the specific functions available are described in detail in the section titled Access from the Desktop later in this document.

Additional detailed reference material is available in the Glossary and the Appendices at the back of this manual.

# Access Through CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Initiation of ROES 3.0 access occurs upon selection of the ROES 3.0 option from the CPRS Tools menu. If it does not appear on the Tools menu, the local IRM Service will need to set it up.

In general, when this option is selected, the following actions take place, which are described further in subsequent sections of this document:

- Patient information is gathered for the selected patient
- Patient eligibility for DALC services is determined
- Patient and ROES user information are assembled
- A browser session to the ROES 3.0 web application is initiated and the assembled information is passed to ROES 3.0

Prior to actually opening a ROES 3.0 session, a background action checks for an acceptable eligibility status for the selected patient.

These eligibility categories are all based on medical need. By requesting orders for the patient, the audiologist stipulates that he/she has evaluated the patient and has determined that medical need exists for amplification in accordance with 38 CFR 17.149, VHA Directive 2002-039, and the supplemental guidance published by the A&SP National Office. For these reasons the National Program offices have agreed that the emails requiring PSAS approval of some of the ROES eligibility categories are no longer necessary.

After a browser session has been initiated with the ROES 3.0 application at the DALC, the following Access and Verify code page is rendered if the system does not recognize your electronic identity. You will be required to enter your codes the first time you enter the ROES 3.0 application. These are your DALC Access/Verify codes, not your local VistA codes. If you already have existing access to the DALC Remote Inquiry System (RIS), your RIS Access and Verify codes should be used. To obtain access to DALC resources, including ROES 3.0, contact the DALC IRM Division at <span class="mark">REDACTED</span>

![](roes-version-3-user-manual/007.png)

If you have successfully connected to ROES 3.0 on a prior occasion by entering valid access and verify codes, you will not see the above access page. The system will recognize you by the user information in the session startup string, sent from CPRS. Enter your Outlook e-mail address the first time you sign in. This address will be added on to vendor order forms generated by ROES 3.0.

Following a verified connection, you will see the *View Order History* page for the patient. At this point you would proceed with ROES 3.0 actions as listed in the side column.

# Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## View Order History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Order History page is initially presented upon entering ROES 3.0. This page lists the current orders for a patient in date sequence, with the most recent being displayed first. From this page you are able to view an order in detail, or select an action from the left hand side of the page. Below is a sample of the View Order History page.

![](roes-version-3-user-manual/008.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name, Social Security number, and date of birth of the patient you selected. These fields cannot be edited.

### Existing Orders Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing orders section is a table listing orders that have previously been entered for the selected patient. These orders appear in date order and can be sorted to show processed or unprocessed orders. A detailed view is available for each order.

Tran Date column: This is the date that the order was placed at the DALC. This date is also a link to a detailed display of the order. Click on the blue <u>date</u> link to view the detailed display.

Order Number column: This is a unique number for a specific order. This number will either be a purchase order number, or a sequence number for orders that do not require a purchase order. This number should be used as the identifier when assistance is needed from DALC staff.

Order Type column: This displays the order type, for example, Custom Hearing Aid, Batteries, HA Repair, etc.

By column: This field displays the initials of the individual who placed the order. This may not be the same as the person who requested the order.

Status column: This is the current status for the order. See [Appendix E](#e.-statuses) for further information.

Serial Number column: A serial number will be displayed for items that are serialized devices.

Item(s) column: This field displays the currently active line items for the order. For example, a custom hearing aid order that has been modified by a model change will display the new models. An order may contain multiple items.

### Actions Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actions section contains links to various functions available in ROES 3.0 when entering through CPRS. You can create new orders, initiate repairs, register a cochlear implant, view patient information, etc. Depending upon your current privileges for ROES 3.0 processing, some of these links may be unavailable to you.

Custom Hearing Aids link: Click on this link to access the ordering process for items on the custom hearing aid contract with the exception of FM devices and Remote Control Devices purchased independently of custom hearing aids.

FMs/Remotes link: This link will bring up the order form for FM devices and Remote Control devices. You may also order a remote control device when you place your custom hearing aid order.

Other Commodities link: Use this link to access the ordering process for batteries, prosthetic socks, accessories, etc., for a patient. Special request items, such as non-contract items may also be ordered through this link.

Service Request link: Click on this link to access the process for modifying a device on a patient's record. This includes making adjustments such as model and component changes, adding components after the trial period (extra component orders) and repairs.

Device Registration link: Use this link for registering a serialized device, such as a hearing aid (custom, stock or BTE), FM or remote, with the DALC. Additionally, this form may be used to register a non-serialized device, such as an assistive device. This option is not used for registering cochlear implants.

CI Registry link: Click on this link to register a cochlear implant with the DALC.

Record Updates link: Click on this link to edit the patient address, eligibility, clinic, and to authorize or not authorize a device.

Station Parameters link: Use this link, if you have supervisor privileges, to access the Station Parameters Page. From this link you are able to grant various processing permissions, and terminate a user's access.

Pending Actions link: Click on this link to access the display of orders that are in need of approval, or have delinquent certifications or issues.

Authorized Aids link: Use this link to view the patient’s current authorized devices.

Exit ROES link: Click on this link to exit the ROES 3.0 application.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains four possible actions that you may take:

![](roes-version-3-user-manual/009.png) Click on this button to view the previous page of orders for the patient. If you are on the first list of orders the list will stay the same.

![](roes-version-3-user-manual/010.png) Click on this button to view the next series of orders for the patient. If you are on the last display of orders the list will stay the same.

![](roes-version-3-user-manual/011.png) Click on this button to view any orders that have not been processed by the Denver Acquisition & Logistics Center.

![](roes-version-3-user-manual/012.png) Click on this button to view orders that have been processed.

# Detail Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail pages present a display of information for a selected order in a very detailed format. When in the View Order History page, there are two entry points to the order detail pages. To see the detail of any of the orders you have placed, click on the blue date link for the selected order. You may also access the detail pages from the Pending Actions link in the blue section on the left side of the page. In this latter case, only those orders with a pending action may be selected for viewing. Within the detail page, different actions will be enabled depending on the entry point.

Regardless of the entry point, an order specific page will be rendered displaying the detail of that order and allowing you to complete certain actions (for example, cancellations, certifications and issues) for that order.

The following detail pages are described in this section:

- Custom Hearing Aid (CHA) Order Detail
- Commodity Detail
- Service Request Detail

## Custom Hearing Aid Order Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Custom Hearing Aid (CHA) Detail page allows you to view all of the order data associated with a specific order. You may also approve an order that was entered by a staff member without approval privileges (this function only from the Pending Actions link), cancel the purchase order, certify the hearing device(s), issue the hearing device(s), reprint the original order form, or print form 2477b (Issue report) after the device(s) is/are issued. The actions that you may complete depend on the status of the order.

Included below is an example of the Custom Hearing Aid Detail page and a description of the actions you may perform.

![](roes-version-3-user-manual/013.png)

The above form shows a custom hearing aid order in "Certification Pending" status. This status would typically be seen after the provider submitted the order but prior to receipt and certification.

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general information about the order in the gray bar at the top of the form is provided for review purposes and is not editable.

#### Order Summary Section

The order summary section contains pertinent order information. Within this section you are also able to certify, issue, or cancel specific lines item for the order.

#### Certify a Line Item

You may certify the receipt of the hearing devices anytime after they have been received, however, you may, to save a step, wait until the devices are issued to the patient before certifying. The DALC will enter the serial number and battery type upon receipt of the invoice, which may be electronic. Usually, the invoice data will be entered electronically or by the DALC's Fiscal Division prior to the certification. In this case the serial number and battery will be displayed on the form and will not be editable. Click on the Certify check box and submit the form to complete the certification.

If there are multiple line items to certify, check the Certify check box for the first item and the other line items will be checked automatically. (You may uncheck a box if you do not want to certify all of the items.)

After entering the certification information and pressing the ![](roes-version-3-user-manual/014.png) button the status of the line item will change to "Issue Date Pending".

#### Issue a Line Item

To issue an item, enter the issue date by either keying in the date or using the Calendar pop-up to select a date. If you enter a date for the first line item and click on the Issue Date field for the next item, the issue date entered for the first item will automatically be transferred to the next item. Most date formats will be accepted including "T" for "Today" as well as "T +- n" for "today plus or minus n days".

After entering the issue date and pressing the ![](roes-version-3-user-manual/015.png) button the status of the order will change to "Complete".

> NOTE: You may enter the certification information and the issue date at the same time. When you press the SUBMIT button the order status will change to "Complete".

#### Cancel a Line Item

To cancel a line item, click on the Cancel check box and press submit. If there are multiple line items on the purchase order, the other line items will not automatically be checked - you must check each line item that you want to cancel. A pop-up calendar will ask you for the date the items were returned to the vendor. Click on the actual date you returned the device(s) to the vendor. The date you select will not be viewable, however, it will be validated to make sure it is not a future date or prior to the date the order was shipped (if there is no ship date, it will be compared to the order date.) If the system determines the date returned to vendor is invalid you will see an alert and be asked to select another date. If the aids are being canceled prior to have not being received, close the calendar by clicking on the "X" in the top right hand corner of the calendar (use of the "X" in the upper right corner of any page is not recommended unless explicitly mentioned in this document.)

Once you have pressed the submit button, the cancel transaction will show on the Unprocessed Orders page as awaiting processing. The original custom hearing aid order will show on the Processed Orders page with a status of "Cancel Pending".

> FYI: The devices must be within the trial period to cancel the order. The trial period begins 30 days after the vendor ships the devices and ends 180 days later. The ship date is entered into the system when the DALC's Fiscal Division pays the invoice. The Cancel checkbox will be disabled if the device is past the trial period.

> NOTE: If you need to cancel one line item and certify and/or issue a second line item, submit the certification and/or issue first and then submit the cancel as two separate actions.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The selectable buttons will change based on the current status of the order and the actions that have been taken previously.

![](roes-version-3-user-manual/016.png) Click this button to return to the View Order History page.

![](roes-version-3-user-manual/017.png) Click this button after you have finished entering the data for the actions you want to complete. This button will disappear if the order has been canceled.

![](roes-version-3-user-manual/018.png) Click this button to print or re-print the original vendor order form for inclusion in the box with the ear mold

## Commodity Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Commodity Detail page will be similar for any commodity ordered through the Other Commodities order form. The only action provided on this page is the Cancel Order functionality; however, you may only cancel a commodity order that has not been processed for shipment. Most commodity orders will be processed for shipment the same day they are entered.

![](roes-version-3-user-manual/019.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general information about the order in the gray bar at the top of the form is provided for review purposes and is not editable.

### Order Summary Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The item ordered, make of the item, quantity, item cost, total cost, and current status of the order are shown in the summary section. The total cost for all items ordered is displayed below the table of items ordered.

#### Cancel a Line Item

To cancel a line item, click on the ![](roes-version-3-user-manual/020.png) button and submit the form. If the Cancel Order button is not displayed, the order has processed too far in the shipment cycle to be canceled.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/021.png) Click this button to return to the View Order History page.

## Service Request Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Service Request Detail page allows you to view all of the data associated with a service request. You may certify the receipt of the service and re-print the service request form.

![](roes-version-3-user-manual/022.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient. It also displays the name of the person entering the data. These fields cannot be edited.

### Service Request Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section displays the service request that was processed in detail. The description of each field is explained below. You may also certify the receipt of the service or goods by clicking ![](roes-version-3-user-manual/023.png) (if the order was for a repair or component change) or ![](roes-version-3-user-manual/024.png) (if the order was for a model change).

The area in gray under the heading displays the general information about the service request for review purposes and is not editable.

Type of Request: Different service request types are explained in detail in [Appendix D](\l).

Status: This shows the status of the service request. Please see [Appendix E](#e.-statuses) for detailed explanation.

Purchase Order: This is the purchase order number that authorized the purchase or repair of the hearing aid. The original CHA purchase order number will be shown if the service request is for an adjustment within the trial period. It will display a repair purchase order number if the request was for repair.

Model: This is the model of the hearing device for which the service request was made. This column will also display the circuits and components if they were part of the hearing aid. If the service request resulted in a model change, this column will show the new model also underneath the old model with the field heading "Model Changed To". If options were added or removed, they are displayed in this column as well.

Warranty: This is the hearing device's current warranty type. Please refer to [Appendix C](#c.-warranty-types) for detailed explanation of warranty types.

Serial Number: This field shows the serial number of the hearing aid. "PENDING" indicates that the clinic ordered a hearing aid but has not yet received the aid from the vendor.

![](roes-version-3-user-manual/025.png) Depending on the type of a service request, you may see different buttons in this field. If the request was for a model change, you will see the ![](roes-version-3-user-manual/026.png) button. Clicking the Cert/Issue button will take you to the *CHA Order Detail* page, where you will be able to certify and issue the device. Please refer to the [*CHA Order Detail*](#custom-hearing-aid-order-detail) page section for explanations on how to certify and issue a hearing device. For all other service request types, you will see the Certify button. Click this button to certify the receipt of the service or goods.

Circuit Problems: This field lists the circuit problems the hearing device had at the time of the request.

Case/Shell Problems: This field lists the case or shell problems the hearing device had at the time of the request.

Secondary Features: This field will list secondary feature options selected for the circuit.

Additional Information: This field lists the additional comments the ordering person made to the vendor.

Items to Vendor: This field identifies items on the hearing aid at the time the aid was sent to the vendor for repair, for example, hearing aid, transmitter, and/or cord, etc. When the vendor sends the repaired aid back, DALC or the clinic will check to ensure all items are returned from the vendor.

Control Settings: This section displays the hearing aid's potentiometer settings the aid had at the time it was sent to the vendor for repair.

Charges: This section will display itemized repair cost information. Depending on the warranty type, repair items such as recase, replate, remake, repair of a programmable or digital aid may or may not incur additional charges. One time loss and damage warranty replacement information, if requested, will also be displayed here.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/027.png) Click this button to return to the View Order History page.

![](roes-version-3-user-manual/028.png) Click this button to reprint the original service request form sent to the vendor. The error message, "Unable to Print Order Form for Completed ROES 3 Service Requests", is generated when there is no reference to the service request file entry. This is because the *Service Request Form* can only be printed if the order was made using the Service Request option in ROES 3.

## Commodity Ordering (Patient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Commodity Order 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Commodity Order Form is used to order all products handled by the DALC with the exception of custom hearing aids. The form allows you to order multiple line items, including different commodities, with a single transaction. The order form is displayed below:

![](roes-version-3-user-manual/029.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the order. These fields cannot be edited.

### Order Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box.

Disability Code (required): From the drop down box, select the patient disability that is associated with the order you are entering.

Select Commodity Group (required): From the drop down box, select the commodity group of the product you wish to order. This action will populate the next drop down box (Select Item:) with the items in the commodity group you chose. If you choose the Prosthetic Socks commodity group, you will need to use the search feature (described below) to find the sock you wish to order since the list of possible selections is so long.

Select Item (required): Select the item that you wish to order from the drop down list. Use the Search function (described below) to reduce the number of items in the list.

![](roes-version-3-user-manual/030.png) Click on this button to order items that the DALC may not normally keep in stock. A new page will be rendered that will allow you to enter a free text make and item name. These requests will be evaluated on a one-by-one basis.

![](roes-version-3-user-manual/031.png) This button, to the right of the Select Item: prompt, can be used with all commodity groups to help you find the exact item you wish to order. When you click on the button, a search text box will open. There you may type in one or more of the characters of the item (e.g., W-5 for wool socks, 5-ply). Typing in more characters will reduce the number of items that are displayed. When you click on the ![](roes-version-3-user-manual/032.png) button, the line item drop down box will be populated with all of the items that begin with the characters you typed (W-5). If the characters you typed in produce a list of more than 100 items, an alert box will prompt you to narrow your search by entering additional characters.

Quantity (required): You can select the number of items you wish to order from this drop down box. If an item can only be ordered in a specific multiple, this list in the box will only contain the available multiples for the item (e.g., batteries in packages of 8 will contain selections of 8, 16, 24, etc.). The list will also be bounded by minimum and/or maximum order quantities.

Type of Transaction (required): You will need to make a selection from the drop down box that best describes the type of order you are entering. You may select from Initial, Spare, and Replace.

Delivery Category (required): You have three options for delivery: Routine, Priority, and Emergency. Routine orders will be shipped within 4 business days, priority orders will be shipped within 24 hours on business days, and emergency orders will be delivered within 24 hours if received by 2:00 pm MT on a business day. Orders will be defaulted to Routine. If you wish to select another option, click on the appropriate radio button. If Emergency is selected, you must enter a patient or facility contact phone number in the text box below the Delivery Category prompt.

Enter a phone number for emergency orders: (required for emergency orders): If you selected a delivery category of emergency, you must enter a phone number, starting with area code. This is required for overnight shipment.

DALC Quantity on Hand: This box displays the amount of the selected item the DALC currently has on hand. If the quantity ordered exceeds the DALC Quantity on Hand, the DALC will fill an order partially with the quantity on hand. The outstanding items will go into backorder status, and shipment may be delayed beyond the 4-day standard. This field cannot be edited.

On the right hand side of the page is a ![](roes-version-3-user-manual/033.png) button. If you click on the button, a new page will open to allow you to view and change the delivery address. An explanation of how to use this form may be found in the [Patient Delivery Address](#patient-delivery-address) section of this manual.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial command section contains three possible actions that you may take:

![](roes-version-3-user-manual/034.png) If you click on this button, you will return to the View Order History page.

![](roes-version-3-user-manual/035.png) If you click on this button, all fields for the current line item you are ordering will be returned to the default settings.

![](roes-version-3-user-manual/036.png) You should click on this button when you have finished putting in all of the information about the line item you are ordering. Taking this action will open the ROES Order Summary page, which will contain the order for the line item you just submitted and any other line items that have been previously submitted.

After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/037.png) button on the summary screen. When you return to the order form, you will see an additional button in the command section: labeled View Order Summary.

![](roes-version-3-user-manual/038.png) This button will load the ROES Order Summary page without adding another line item to the order.

If you attempt to exit from the order form without submitting your order, you will see a pop up box that says, “You have not submitted your order – click ok to exit anyway!” Click the ![](roes-version-3-user-manual/039.png) button if you wish to exit without saving the order or Cancel to remain in the order form.

## Special Request Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Special Request Order Form is used to order products that are not found on drop down list of the Commodity Order page. The form allows you to order multiple line items, including different commodities, with a single transaction. These orders will be evaluated and processed if deemed necessary. An example of the Special Request Order form follows:

![](roes-version-3-user-manual/040.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the order. These fields cannot be edited.

### Order Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box.

Disability Code (required): From the drop down box, select the patient disability that is associated with the order you are entering.

Select Commodity Group (required): From the drop down box, select the commodity group of the product you wish to order.

Enter Make (required): Enter the make of the item in the text box that you wish to order.

Enter Item (required): Enter the item name in the text box that you wish to order.

Quantity (required): Enter the number of items you wish to order.

Type of Transaction (required): You will need to make a selection from the drop down box that best describes the type of order you are entering. You may select from Initial, Spare, and Replace.

Delivery Category (required): You have three options for delivery: Routine, Priority, and Emergency. Routine orders will be shipped within 4 business days, priority orders will be shipped within 24 hours on a business day, and emergency orders will be delivered within 24 hours if received by 2:00 pm MT on business days. Orders will be defaulted to Routine. If you wish to select another option, click on the appropriate radio button. If Emergency is selected, you must enter a patient or facility contact phone number in the text box below the Delivery Category prompt.

Enter a phone number for emergency orders: (required for emergency orders): If you selected a delivery category of emergency, you must enter a phone number, starting with area code. This is required for overnight shipment.

On the right hand side of the page is the ![](roes-version-3-user-manual/041.png) button. If you click on the button, a new page will open to allow you to view and change the delivery address. An explanation of how to use this form may be found in the [Patient Delivery Address](#patient-delivery-address) section of this manual.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial command section contains three possible actions that you may take:

![](roes-version-3-user-manual/042.png) If you click on this button, you will return to the Commodity Order Form page.

![](roes-version-3-user-manual/043.png) If you click on this button, all fields for the current line item you are ordering will be returned to the default settings.

![](roes-version-3-user-manual/044.png) You should click on this button when you have finished putting in all of the information about the line item you are ordering. Taking this action will open the ROES Order Summary page, which will contain the order for the line item you just submitted and any other line items that have been previously submitted.

After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/045.png) button on the summary screen. When you return to the order form, you will see an additional button in the command section labeled View Order Summary.

![](roes-version-3-user-manual/046.png) This button will load the ROES Order Summary page without adding another line item to the order.

If you attempt to exit from the order form without submitting your order, you will see a pop up box that says, “You have not submitted your order – click ok to exit anyway!” Click the ![](roes-version-3-user-manual/047.png) button if you wish to exit without saving the order or ![](roes-version-3-user-manual/048.png) to remain in the order form.

## ROES Order Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Summary Section is used to display all items contained on the order and allow you edit, delete, add or submit your order. The summary section is displayed below:

![](roes-version-3-user-manual/049.png)

### Summary Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Summary section is a table that displays all items in the order. Below is a description of each column and the actions that can be done.

Commodity Group column: This column displays the commodity group for each item ordered.

Item column: This column contains a brief description of each item, the associated HCPCS code, and the order number. The order number will not be displayed until the order is submitted for processing.

Delivery Category column: This column displays the type of delivery for the item.

Quantity column: This column displays the selected number of items ordered for the line item.

Unit Price column: This column displays the individual price for the item.

Total Price column: This column displays the total cost for the item. This is based on the unit price and the quantity selected for the item.

![](roes-version-3-user-manual/050.png) This button will delete the item from the order. This button will only delete a specific item and not the entire order.

![](roes-version-3-user-manual/051.png) This button allows you to edit an item from the order. Selecting this button will take you back to the Station Stock Order Form, where you will be able to change any information as needed.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains two possible actions that you may take:

![](roes-version-3-user-manual/052.png) If you click on this button, you will return to the ROES Station Stock Order Form for entry of an additional item. Multiple items may be entered for one order.

![](roes-version-3-user-manual/053.png) If you click on this button, all items for the order will be submitted for processing. When the order is submitted you will receive a pop-up box stating, “Order has been submitted”, and the order number will appear in the item column for each item ordered. After submitting the order, you will only be able to Exit from the Station Stock Summary Screen.

## Custom Hearing Aids (Patient) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Page 1 - Hearing Aid Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Custom Hearing Aid Order Form is used to order custom hearing aids. Each order may include up to 2 hearing aids and a remote control device if available. The order form is displayed below:

![](roes-version-3-user-manual/054.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the order. These fields cannot be edited.

### *Order Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Disability (required): From the drop down box, select the disability of the patient that is associated with the order you are entering. Only disabilities allowed for hearing loss are displayed.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box. The service will default to "Audiology and Speech Pathology".

Date Patient Requested Care (required): Enter the date the patient requested care in the text box or click on the ![](roes-version-3-user-manual/055.png) button to choose a date from the pop-up calendar. The date may be entered in almost any commonly-used format (i.e. 6-20-02, 6/20/02, June 20, 2002, etc) including "T" for "Today" as well as "T +- n" for "today plus or minus n number of days".

Audiological Assessment Date (required): Enter the date of the patient's audiological assessment in the text box or click on the calendar button to choose a date from the pop-up calendar. The date may be entered in almost any commonly-used format including "T" for "Today" as well as "T +- n" for "today plus or minus n number of days".

Transaction Type (required): Make a selection from the drop down box that best describes the type of order you are entering. You may select from Initial, Spare, and Replace. The default transaction type is Initial.

Fitting (required): Select the appropriate radio button to indicate if the hearing aids ordered will be for the left ear, the right ear or both ears. The default fitting is Both.

Select Aids by (required): You have the option of selecting a specific hearing aid model or searching the database of hearing aids based on user-selected search criteria. When you choose a "Select Aids by" radio button, the appropriate section of the form will be activated, allowing you to enter either the make and model, or enter fields to perform a database inquiry.

#### Selecting Aids

You may select aids by the make and model or by using the Search option.

By Make and Model:

1.  Click on the "Make/Model" radio button to activate the make and model drop down boxes. If the "Right" fitting button is selected, only the right column will be activated and vice versa.
2.  Click on the "Make" drop down box to see a list of vendors currently under contract for custom hearing aids.
3.  Select the desired vendor. After a few seconds the "Model" drop down box will be populated with the items currently on contract for the selected vendor. These models correspond to the classification selected (see below). Select the model of the aid you wish to order.

Using the Search Option:

The "Search" option provides the provider the opportunity to compare the costs of similar characteristics found on aids provided by different vendors.

1.  Select the search criteria for the database query and then click on the ![](roes-version-3-user-manual/056.png) button to submit the request. The system will search the database for aids that match the search criteria and present the list on the Hearing Aid Cost Analysis page.

From the Hearing Aid Cost Analysis page you may select the aid you want to order with either a standard one year or the extended two year warranty. A remote control, if available, may also be selected. For a further description, this document includes a section describing the Hearing Aid Cost Analysis page.

You may search on channel/memory options (programmable and digital aids only), shell types and circuit types, plus you can indicate if you want to include a directional microphone and a variety of interfaces.

Channel and memory options go hand-in-hand, so if you select one, you must select the other. The choices for both channel and memory options are "none", "single" and "multiple" (choose "none" if you do not want to include channel and memory options in your search.)

The choices for shell type are "Full Shell", "Half Shell", "Canal", “Completely in the Ear", abbreviated as "CIC" and "Behind the Ear", abbreviated as "BTE". You must select at least a shell type to perform a search. The “Circuit Types” field may include "AGCI/WDRC","AGCO", "ASP", "CLD", "KAMP” and "POWER", however, you may not see all of the circuit types listed for all shell types. Across the bottom of the search box are checkboxes for "DMIC" (directional microphone), "TM" (tinnitus masker),"TC" (telecoil), "DAI" (directional audio input), "BICROS" and "CROS". Click on one or more of these checkboxes to narrow the search results.

Not all search options need be selected for the search to work; however, choosing additional search criteria can narrow the search. For example, if shell type is the only search criteria selected, the cost analysis page will display far too many aids for an effective comparison.

> FYI: Keep in mind that when performing a search for two aids (left and right) and using different search criteria for the two sides, the system will only deliver results if models can be paired for a single vendor. For example, if a vendor's model is found to match the left aid, but not the right aid, that vendor will not show up on the cost analysis page.

Classification (required): The classification of the aid may be "Non-Programmable", "Programmable" or "Digital". The default classification is "Non-Programmable". The choice of classification affects some of the other fields on the order form. For example, channel and memory options are disabled when "non-programmable" is the selected classification.

Copy Over buttons: ![](roes-version-3-user-manual/057.png) ![](roes-version-3-user-manual/058.png) These buttons, located below the search criteria box may be used to duplicate the left aid selections to the right side or vice versa. You may move the data over from one side to the other and then make changes to those data fields. These buttons may be used with either the make/model or search selection.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/059.png) Click on this button to exit back to the patient's Order History page. If you have gotten through the complete order process but have not submitted your order, a message pops up at this point to alert you.

![](roes-version-3-user-manual/060.png) Click on this button to reset the fields on the order form to the original defaults.

![](roes-version-3-user-manual/061.png) Click on this button after you have selected a make and model or have entered the desired search criteria. Pop-up messages remind you of missing or invalid data. The next page delivered is the "ROES Hearing Aid Cost Analysis Table" page.

### Page 2 - ROES Hearing Aid Cost Analysis Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Hearing Aid Cost Analysis Table presents the provider with a comparison, sorted by cost from lowest to highest, of hearing aid models based on the search criteria selected on page one of the order form. This page is also displayed when a specific make and model are selected off the first page. From this page, the user may select the aid that they would like to order, indicating whether the aid should include the standard one-year warranty or the extended two year warranty. A remote control device, if offered by the vendor, may also be selected from this page.

In addition, clicking on the "?" in the first column will render a page displaying cost and component information for the models of the specific shell type and classification.

The following is an example of the ROES Hearing Aid Cost Analysis Table:

![](roes-version-3-user-manual/062.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For searches only, the heading section shows the search criteria selected on the first page of the order form.

### *Display Section*Vendor Column: The vendor name is displayed as well as the ![](roes-version-3-user-manual/063.png) button described above. The same vendor name may be displayed multiple times if the vendor has more than one model fitting the search criteria. Only one entry is shown on this page when you select a specific make and model from the first page.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the ![](roes-version-3-user-manual/064.png) button to see detailed information for all models of the same shell type for this vendor. Hold your mouse over the name of the component or circuit to see a pop-up of the item's ROES code. Click on the "Close" button at the bottom of the page when you have finished viewing this page.

The following is an example of the ROES Hearing Aid Model Information page:

![](roes-version-3-user-manual/065.png)

Model Column: For a monaural order, one aid is displayed with the identifying side and for a binaural order, two aids.

Cost with 1 yr Warranty Column: Click on the checkbox in the appropriate row to order that model or models with the standard one-year warranty. To de-select your choice, click again on the checkbox.

Cost with 2 yr Warranty Column: Click on the checkbox in the appropriate row to order that model or models with the extended two year warranty. To de-select your choice, click again on the checkbox.

Remotes Column: Remote control devices may be provided by some vendors. To select a remote control device, click on the drop down box in the right hand column. Device names and costs are listed. A device may be displayed twice allowing the user to purchase the item with the one year warranty or the extended two year warranty. An "\*" next to the cost indicates that the cost of the remote includes an extended warranty.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/066.png) Click this button to return to the first page of the Custom Hearing Aid Order Form. You may change your selections on the first page as many times as you like before going on to complete the order.

![](roes-version-3-user-manual/067.png) When you are satisfied with the model that you have selected, click on this button to render the Circuits/Components/Secondary Features page and complete the selection of options for your order. Even after going on to the next page, you may come back to the first two pages to make changes.

### Page 3 - Circuits/Components/Secondary Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Circuits/Components/Secondary Features page presents the provider with a simple point and click method of selecting specific options for the aid that is being ordered. The selection of these options, including a circuit, one or more miscellaneous components, one or more interfaces, a microphone and several secondary features will not change the cost of the model(s) as displayed on the Hearing Aid Cost Analysis Table.

The manufacturer of the aid has provided the options presented on this page. Only certain combinations of options are allowed. This may help alleviate errors caused by selecting options that may not work or fit together.

Below is an example of the Circuits/Components/Secondary Features page:

![](roes-version-3-user-manual/068.png)![](roes-version-3-user-manual/069.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section displays the model(s) chosen on the previous page.

### *Order Section*Circuit (required): Click on the drop down box to see the circuits that are available for the selected model. Only those circuits compatible with the selected model and allowed with the hearing aid bundle will be presented. When the desired circuit is selected the system may require several seconds for the database to be searched for compatible components and secondary features. After a pause, the page will be refreshed and the components and secondary features may then be selected.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: If there is only one circuit available for the selected model, the page will be populated with that circuit and its associated primary and secondary options when the page is rendered. Also, if you are using the search option, only those circuits fitting the circuit type selected on the first page will be available for selection here.

Components: You may select one or more miscellaneous components to be included with the aid. Click on the drop down box to see the available miscellaneous components. When an item is selected, the ROES code for that item will appear in the text box to the right of the drop down box. To de-select an item, single click on the item in the drop down box again. It will be removed from the text box on the right.

Interfaces: You may select one or more interfaces to be included with the aid. Click on the drop down box to see the available interfaces. Selection and de-selection of items in this field are the same as the method described for Components.

D-Mic (Directional Microphone): You may select one microphone to be included with the aid. Click on the drop down box to display the microphones compatible with the selected aid. You may change the selected item as many times as you like. To de-select the microphone, click on "None selected".

Secondary Features: There are currently 13 categories of secondary features on this form. Click on the individual drop down boxes to view the secondary features compatible with the selected aid. A text box to the right of the drop down box indicates that multiple selections are allowed for that category. When an item is selected for multiple selection categories, it will appear in the text box to the right of the drop down box. To de-select an item, single click on the item in the drop down box again. It will be removed from the text box on the right. The "Miscellaneous" category may contain features that do not fit into one of the other categories.

Copy Over Buttons: ![](roes-version-3-user-manual/070.png) ![](roes-version-3-user-manual/071.png) These buttons, located below the selection boxes may be used to duplicate the left aid selections to the right side or vice versa. You may move the data over from one side to the other and then make changes to those data fields. These buttons will be disabled if you select different models for the right and left ear.

Vendor codes: Some vendors may include their own feature code in parentheses next to the name of the feature, i.e. PINK (P). These codes are provided for the manufacturer's benefit and are not related to ROES codes. Vendor codes may show up on the Primary/Secondary features page and also on the CHA Order form.

Factory defaults: Factory defaults are prefixed by an ("\*") i.e. \*PINK. They will appear as the first item in the list on a single selection drop down list and will be automatically selected for you. Click on a different item to change from the factory default to something else, Items designated as "factory default" will also be the first item in a multiple selection list, and, although the option will be pre-selected for you in the text box, you may de-select it by clicking on it *in the drop down list* and then selecting the item you want. You will see the term "None selected" when there are no factory or standard option designations for that feature.

Standard options: Standard options are features that are provided as standard on a device by a particular vendor. While these features may be provided as options by other vendors, a standard option is a feature that a vendor will always include on the device. The standard option provided by the vendor will automatically be selected for you and cannot be deselected. Standard option features are designated with a suffix of "\[STD\]” i.e., HYPOALLERGENIC \[STD\]. If multiple selections are allowed, a second option may also be selected.

> NOTE: Factory default and standard option designations are provided to the DALC by the hearing aid manufacturer. Some manufacturers may choose to not provide these designations; therefore you may not see these designations for all makes and models.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/072.png) Click this button to return to the Hearing Aid Cost Analysis page. You may change your selection on the Hearing Aid Cost Analysis page as many times as you like before going on to complete the order.

![](roes-version-3-user-manual/073.png) Click on this button to reset the fields on the form to the original defaults.

![](roes-version-3-user-manual/074.png) When you are satisfied with the circuit, components, etc. that you have selected, click on this button to render the Audiometric Data/Vendor Instructions page. Even after going on to the next page, you may come back to this page to make changes.

### Page 4 - Audiometric Data/Vendor Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiometric Data/Vendor Information page is the final page of data entry for Custom Hearing Aid orders. The audiometric data presented on this page is populated from data collected through the Audiometric Data Enter/Edit module exported in conjunction with ROES 3.0 as QUASAR patch ACKQ\*3.0\*3. That data is entered when the patient visits the clinic for an audiometric examination, and is transmitted to the DALC via EDI (Electronic Data Interchange) when the exam is complete and the provider has signed the form. The data is filed at the DALC for display at the time a hearing aid order is placed. The audiometric data presented on this page may be changed, however, if edited, it will not change the data stored at the DALC for this audiometric examination. The edited data will, however, appear on the vendor order form. The data may be entered manually if no data has been transmitted from the clinic.

This form also allows for the keying in of additional information that may be of use to the manufacturer.

![](roes-version-3-user-manual/075.png)

### *Order Section*Air and Bone Conduction (KHz) (Audiometric Data): In the event that audiometric exam data has not been transmitted to the DALC from the clinic, air and bone conduction values may be entered by clicking on the appropriate text box and entering the value. The air and bone conduction values will be printed out on the vendor order form.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Speech Audiometry: In the event that speech data has not been transmitted to the DALC from the clinic, values may be entered by clicking on the appropriate text box and entering the value. The speech audiometry values will be printed out on the vendor order form.

Matrix Selection: In the event that matrix data has not been transmitted to the DALC from the clinic, values may be entered by clicking on the appropriate text box and entering the value. The matrix values will be printed out on the vendor order form.

2cc Coupler Gain: In the event that 2cc coupler gain data has not been transmitted to the DALC from the clinic, values may be entered by clicking on the appropriate text box and entering the value. The 2cc coupler gain values will be printed out on the vendor order form.

Fitting Formula: Click on the drop down box to view the choices for fitting formula and select the appropriate one. To de-select the fitting formula, click on "None selected".

Special Instructions: This is a "free text" section in which you may key in any additional instructions to the manufacturer regarding the hearing aids.

Below the "Special Instructions" section are checkboxes that allow you to indicate additional special needs to the vendor.

Patient Delivery Address for Batteries: Clicking on this ![](roes-version-3-user-manual/076.png) button will render the Patient Delivery Address page and allow you to edit or just verify the address currently on file for this patient. This is the address that batteries will be sent to (for eligible patients) upon issuance of the hearing aid. See [Patient Delivery Address](#patient-delivery-address) for a description of the Patient Address page.

Station Delivery Address for Aids: Clicking on this ![](roes-version-3-user-manual/077.png) button will render the Station Delivery Address page and allow you to edit certain fields or just verify that the address on file for the station is correct. You may also change the site for delivery to one within your VISN or a site that does contract work for you. This address will print out on the vendor order form as the "ship to" address for the hearing aids. See the [Station Delivery Address](#station-delivery-address) section for a description of the Station Delivery Address page.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/078.png) Click this button to return to the Circuit/Components/Secondary Features page. You may change your selections on the Circuit/Components/Secondary Features page as many times as you like before going on to complete the order.

![](roes-version-3-user-manual/079.png) When you are satisfied with the data entered on the Audiometric Data/Vendor Instructions page, click on this button to render the Custom Hearing Aid Summary page. You may come back to this page to make changes until your order is submitted.

### Page 5 - Custom Hearing Aid Order Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Custom Hearing Aid Order Summary page displays the line items that have been selected during the ordering process. The order is not placed until the ![](roes-version-3-user-manual/080.png) button has been pressed. The user may at any time, until the order is submitted, return to previous pages to edit the order. The command section buttons will change after the order has been submitted and those that appear are dependent upon the status of the order after submission.

![](roes-version-3-user-manual/081.png)

### *Display Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The manufacturer of the selected items is displayed at the top of the page since various vendors have similar or identical model names.

Item column: The Item column shows the name of the item ordered which may be a hearing aid or a remote. Also shown is the HCPCS code for that item. The purchase order number shows as "pending" until the order is submitted. Then, if the order is placed successfully, the purchase order number is updated.

Circuit/Components column: The circuit/components column displays the ROES codes for the circuit, interface(s), microphone, and miscellaneous components selected.

Ear column: This column displays "Left", "Right" for hearing aids and "N/A" for remote control devices.

Cost of Item column: This is the contract cost for the specific line item not including the extended warranty.

Cost of Warranty column: This is the contract cost of the 2 year warranty, if selected; otherwise "N/A" is displayed.

Total Cost: This column displays the total cost for the individual line item.

Total Cost row: The "Total Cost" row, shown in dark pink below the line items, shows the total cost for the entire order.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Command section will change after submission of the order, based on the status of the order.

![](roes-version-3-user-manual/082.png) Press this button to exit to the View Order History page without saving your order.

![](roes-version-3-user-manual/083.png) Click this button to return to the Audiometric Data/Vendor Instructions page. You may change your selections on the Audiometric Data/Vendor Instructions page, or any of the other pages as many times as you like before submitting the order.

![](roes-version-3-user-manual/084.png) Clicking on this button will submit your order and return a purchase order number if all checkpoints have been cleared. Please verify that your order is correct prior to submission. You may experience a pause of several seconds while your order processes.

If the system is unable to create a new ROES 3.0 transaction, you will see an alert box, similar to the one shown below, that says "Error creating order - please exit and contact DALC IRM". This type of message should be a rare occurrence and might indicate a system problem. If, however, a ROES 3.0 transaction is created but the purchase order number cannot be generated, you will see an alert box, similar to the one shown below, that says "This order will require processing by a DALC technician". This message, although rare, may indicate a file error that will need to be resolved by DALC staff.

For users that do not have approval privileges, the alert box will display "Order in pending approval status!" These orders will require approval by a provider with the appropriate approval privileges. In each of these situations a purchase order number will not be generated until further action is taken, either by the DALC or the clinic, depending on the message delivered. An alert pop-up displays.

![](roes-version-3-user-manual/085.png)

Typically, the order will pass through all of the checkpoints and generate a purchase order number. An alert box will indicate that your order has been successfully submitted and the PO# shown will change from "Pending" to the actual purchase order number, as in the next example.

In the case of vendors who are Electronic Data Interchange (EDI) partners with the DALC, the purchase order will be electronically dispatched to the vendor immediately. Otherwise, the purchase order will be faxed to the vendor the following morning.

![](roes-version-3-user-manual/086.png)

You will notice that the Command section buttons have changed. These buttons are described here.

![](roes-version-3-user-manual/087.png) Click on this button to print the generic order form provided by ROES 3.0. This order form contains all of the information collected during the ordering process, including the purchase order number for approved orders. You may still print the order form for orders that have not been approved; however, the vendor will have to wait for the approval before receiving a purchase order number. The intent is for this form to be sent to the manufacturer with the earmold. When you select this button, you will see a printer dialog box. Select the device you wish to print to and click "OK".

The following is an example of the generic order form for custom hearing aid orders.

![](roes-version-3-user-manual/088.png)![](roes-version-3-user-manual/089.png)

![](roes-version-3-user-manual/090.png) Click on this button to display the generic order form to your screen. At the bottom of the form are buttons for printing the order form or returning to the Custom Hearing Aid Order Summary page.

![](roes-version-3-user-manual/091.png) Click on this button when you are ready to exit back to the patient's View Order History page and/or exit ROES completely. The information on the Custom Hearing Aid Order Summary page will automatically be copied to your clipboard for pasting into the patient's clinical record or anywhere you choose.

## FMs/Remotes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ROES FM Device/Remote Control Order Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES FM Device/Remote Control Order Form may be used to order all FM receivers and transmitters, and any remote controls ordered after the initial custom hearing aid order. You may order up to three line items using this order form; however, all items must be for devices from the same manufacturer.

![](roes-version-3-user-manual/092.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the order. These fields cannot be edited.

### *Order Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Disability Code (required): From the drop down box, select the disability of the patient that is associated with the order you are entering. Only disabilities allowed for hearing loss are displayed.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box. The service will default to "Audiology and Speech Pathology".

Type of Transaction (required): Make a selection from the drop down box that best describes the type of order you are entering. You may select from “Initial”, “Spare”, and “Replace”. The default transaction type is "Initial".

Select Device Type (required): Select the type of device you wish to order from the drop down list. The choices are "FM Receiver", "FM Transmitter" and "Remote Control".

Select Make (required): Select the make of the device you wish to order. The make must be the same for multiple line items, such as a receiver and a transmitter.

Select Model (required): The drop down list of models includes the model name and the cost of the device with a one year warranty.

The following example displays a second entry showing the cost of ownership for the same device when a 2 year warranty is applicable:

DHC2 REMOTE w/1 yr wrty - 99.05

DHC2 REMOTE w/2 yr wrty - 128.05

DHC3 EPROM REMOTE w/1 yr wrty - 99.05

DHC3 EPROM REMOTE w/2 yr wrty - 128.05

Aid Ordered for (required for FM device orders): This is a free text field. Enter the model of the aid you are ordering the FM device for so the vendor will be able to provide the appropriate audio boot.

> NOTE: This field will be disabled if you choose a remote control as the type of device.

Special Instructions: You may enter a free text comment up to 100 characters. This information will be transmitted to the vendor and will print out on the order form.

“Patient Delivery Address for Batteries:” Clicking on ![](roes-version-3-user-manual/093.png) button will render the Patient Delivery Address page and allow you to edit or just verify the address currently on file for this patient. This is the address that batteries will be sent to (for eligible patients) upon issuance of the device. See [Patient Delivery Address](#patient-delivery-address) for a description of the Patient Delivery Address page.

“Station Delivery Address for Device:” Clicking on ![](roes-version-3-user-manual/094.png) will render the Station Delivery Address page and allow you to edit certain fields or just verify that the address on file for the station is correct. You may also change the site for delivery to one within your VISN or a site that does contract work for you. This address will print out on the vendor order form as the "ship to" address for the hearing aids. See [Station Delivery Address](#station-delivery-address) for a description of the Station Delivery Address page.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains three possible actions that you may take:

![](roes-version-3-user-manual/095.png) Click on this button if you want to return to the View Order History page.

![](roes-version-3-user-manual/096.png) If you click on this button, all fields for the current line item you are ordering will be returned to the default settings.

![](roes-version-3-user-manual/097.png)You should click on this button when you have finished putting in all of the information about the line item you are ordering. Taking this action will open the ROES FM/Remote Control Device Order Summary page, which will contain the order for the line item you just submitted and any other line items that have been previously submitted.

After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/098.png) button on the summary page.

### ROES FM/Remote Control Device Order Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES FM/Remote Control Device Order Summary page displays the items you have selected for your order

![](roes-version-3-user-manual/099.png)

### *Display Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The manufacturer of the selected items is displayed at the top of the page since various vendors have similar or identical model names.

Item column: The Item column shows the name of the item ordered which may be an FM device or a remote. Also shown is the HCPCS code for that item. The purchase order number shows as "pending" until the order is submitted. Then, if the order is placed successfully, the purchase order number is updated.

Device Type: This is the device type chosen on the first page of the order form.

Cost of Item column: This is the contract cost for the specific line item not including the extended warranty, if selected.

Cost of Warranty column: This is the contract cost of the 2-year warranty, if selected; otherwise "N/A" is displayed.

Total Cost: This column displays the total cost for the individual line item.

Total Cost row: The "Total Cost" row, shown in dark pink below the line items, shows the total cost for the entire order.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Command section will change after submission of the order, based on the status of the order. These buttons on not shown in the example but are similar to the example of the Custom Hearing Aid Order Summary page example.

![](roes-version-3-user-manual/100.png) Press this button to exit to the ROES FM/Remote Control Device Order Summary page without saving your order.

![](roes-version-3-user-manual/101.png) Clicking on this button will submit your order and return a purchase order number if all checkpoints have been cleared. Please verify that your order is correct prior to submission. You may have a several second "hang" while your order processes.

If the system is unable to create a new ROES 3.0 transaction, an alert will display the following message: "Error creating order - please exit and contact DALC IRM". This type of message should be a rare occurrence and might indicate a system problem. If, however, a ROES 3.0 transaction is created but the purchase order number cannot be generated, you will see an alert box, similar to the one shown below, that says "This order will require processing by a DALC technician". This message, although rare, may indicate a file error that will need to be resolved by DALC staff.

For users that do not have approval privileges, the alert box will display "Order in pending approval status!” These orders will require approval by a provider with the appropriate approval privileges.

In each of these situations a purchase order number will not be generated until further action is taken, either by the DALC or the clinic, depending on the message delivered.

Typically, the order will pass through all of the checkpoints and generate a purchase order number. An alert box will indicate that you order has been successfully submitted and the PO# shown will change from "Pending" to the actual purchase order number, as in the example below.

In the case of vendors using Electronic Data Interchange (EDI) the purchase order will be electronically dispatched to the vendor immediately. Otherwise, the purchase order will be faxed to the vendor the following morning.

You will notice that the Command Section buttons change after submission of the order. These buttons are described here.

![](roes-version-3-user-manual/102.png) Click on this button to print the generic order form provided by ROES 3.0. This order form contains all of the information collected during the ordering process, including the purchase order number for approved orders. You may still print the order form for orders that have not been approved; however, the vendor will have to wait for the approval before receiving a purchase order number. When you select this button, you will see a printer dialog box. Select the device you wish to print to and click "OK".

Below is an example of the generic order form for FM and remote control device orders.

![](roes-version-3-user-manual/103.png)![](roes-version-3-user-manual/104.png)

![](roes-version-3-user-manual/105.png) Click on this button to display the generic order form to your screen. At the bottom of the form are buttons for printing the order form or returning to the Custom Hearing Aid Order Summary page.

![](roes-version-3-user-manual/106.png) Click on this button when you are ready to exit back to the patient's View Order History page and/or exit ROES completely. The information on the Custom Hearing Aid Order Summary page will automatically be copied to your clipboard for pasting into the patient's clinical record or anywhere you choose.

## Service Requests (Patient) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Service Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The service request process is used for any 'service'-related actions following the initial order of a custom hearing aid. These actions are largely governed by DALC contractual agreements, and include adjustments to orders within the contract-specified trial period (model changes, component changes within same bundle, etc.), extra component orders, and/or repair requests. The Service Request Form allows for order entry related to these types of actions.

### Page 1 - Service Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Page 1 of the Service Request Form below displays all authorized hearing devices currently assigned to the patient. Click the ![](roes-version-3-user-manual/107.png) button that corresponds to the device to order a service request.

![](roes-version-3-user-manual/108.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the service request. These fields cannot be edited.

### *Service Request Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your service request. A description of how to use each field is included below. Fields required for completion of the service request are indicated.

Disability (required): From the drop down box, select the disability of the patient that is associated with the service request order you are entering. Only disabilities allowed for hearing loss are displayed.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box. The service will default to "Audiology and Speech Pathology".

Ear: Displays the ear designation of the hearing device: "Left" for the left ear, "Right" for the right ear, and "N/A" for the remotes. This field cannot be edited.

Serial Number: Displays the serial number of the hearing device. "PENDING" indicates that the clinic ordered a hearing device but has not yet received it from the vendor and that an invoice has not yet been processed by the DALC. This field cannot be edited.

Warranty Type: Displays the hearing device's warranty type. A blank space in this column indicates that there is no warranty established for the device because the vendor has not yet sent the aid to the clinic. This field cannot be edited. See "Warranty Type" in [Appendix C](#c.-warranty-types).

Exp Date: Displays the expiration date of the warranty. The ending date of the trial period may also be displayed if applicable. This field cannot be edited.

Issuing Station: The Issuing Station displays the station number of the clinic where the aid was issued to the patient. When the mouse cursor is placed over the station number, the name of the station is displayed. This field cannot be edited.

Eligibility Station: Displays the station number of the clinic where the patient's eligibility was determined when the aid was initially ordered. When the mouse cursor is placed over the station number, the name of the station is displayed. This field cannot be edited.

![](roes-version-3-user-manual/109.png) Click this button to select an aid requiring a service request.

A pop-up window with the warning message below is displayed if you select an aid that currently has an adjustment order in the Awaiting Processing status. The existing adjustment order must be processed by a DALC technician before you can proceed.

![](roes-version-3-user-manual/110.png)

A warning message below is displayed if you try to open a repair order when there is one already open for the same aid. You need to either cancel or certify the existing repair order before you can create a new one. You may proceed to request an extra component or adjustment order for an aid under the New aid warranty.

![](roes-version-3-user-manual/111.png)

A warning message below is displayed if you select an aid currently in the Cancel Pending status. And no further action is allowed.

![](roes-version-3-user-manual/112.png)

![](roes-version-3-user-manual/113.png) Click this button to exit back to the patient's Order History page. If you have gotten through the complete order process but have not submitted your order, a message pops up at this point to alert you.

### Page 2 - Service Request Form 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Page 2 of the Service Request Form is used to change models or components (during trial period), to order extra components, to order other repair items, and to indicate circuit and case/shell problems.

> FYI: The displays on the following pages include all of the information and data entry fields that might appear on page 2 of the Service Request Form in different scenarios. There will be slight variations in the appearance of this page beyond these examples depending on the selected device's warranty type, aid type, or default repair vendor. For instance, the next display shown matches what would be presented for an aid that is still within the contract-specified trial period following the invoice date for the order. A service request order for an aid that is beyond its trial period, for example, will have a slightly different appearance. These variations are described in the narrative text that accompanies the displays.

New (In Trial Period) - custom hearing aid: The following page is displayed if the aid is under the New-aid warranty and within the contract trial period. The appearance of this page, however, will vary depending on the aid's warranty. For example, if the vendor had not yet shipped the aid to the clinic (the warranty has not been established), the "Circuit Problems", “Case/Shell Problems" and "Special Requests" sections would not appear on the page. If the trial period had expired, the "Model Change - Search Criteria" section would not appear since no adjustment to the aid would be allowed.

Hearing aids that have been purchased under previous contracts may not have the correct classification information in the DALC database; therefore, the selectable options generated within ROES may not be accurate. If the aid is not currently on contract, select the correct classification from the "Identify Classification to Load Circuit Data" field. This field will only be displayed when the aid is not currently under contract. Click the radio button to the left of the classification to generate the correct circuit list, and then select a circuit to list compatible components and secondary feature options.

![](roes-version-3-user-manual/114.png)

![](roes-version-3-user-manual/115.png)

#### New (In Trial Period) - FM device 

The following page is displayed if the FM device is under the New-aid warranty and within the trial period.

There will be slight variations in the appearance of this page depending on the selected device's warranty type.

![](roes-version-3-user-manual/116.png)

#### New (In Trial Period) - remote device

The following page is displayed if the remote device is under the New-aid warranty and within the trial period.

#### ![](roes-version-3-user-manual/117.png) Out of Warranty - stock hearing aid

The following form is displayed if the hearing device is a stock hearing aid and has no warranty.

![](roes-version-3-user-manual/118.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient. It also displays the make, model, serial number and warranty type of the hearing device you selected. These fields cannot be edited.

#### Service Request Section

The following prompts will help you complete your service request. A description of how to use fields is included below. Fields required for completion of a service request are indicated.

Repair Vendor (required): If the hearing device is under the New-aid warranty, the repair vendor is automatically selected based on the DALC contract in place. In this case a user does not have an option to change. If the aid is under the Service warranty or is out of warranty, the system chooses the repair vendor based on DALC repair contracts and the knowledge base established by the DALC Electronics Lab, but a user has an option to select DALC as the repair vendor. The default repair vendor for stock hearing aids is DALC.

Current Classification, Current Channel/Memory, Current Shell Type: Displays the classification, channel/memory and shell type currently on the selected aid. These fields cannot be edited and are not applicable to FM and remote control devices.

Current Circuit/Components: Displays circuit and components currently on the selected aid. Hearing aids purchased prior to ROES 3.0 may not display circuit and components correctly because that data was not collected in earlier versions of ROES. These fields cannot be edited and are not applicable to FM, remote control devices or stock hearing aids.

Identify Classification to Load Circuit Data: This field is displayed if the hearing aid is not currently on contract. If the current classification listed for this aid is incorrect, click a radio button to the left of the classification to generate the correct circuit list. Then select a circuit to list compatible components and secondary feature options.

#### Model Change - Search Criteria: This section applies to custom hearing aids that are under the New-aid warranty (See [Appendix C](#c.-warranty-types) for the description of the warranty type) and within the contract-specified trial period. You cannot change models once the trial period is over. This section does not apply to FM, remote control devices or stock hearing aids.

Select Classification (required for a model change): The classification of the aid may be "Non-Programmable", "Programmable" or "Digital". The default classification is "Non-Programmable". The choice of classification determines whether other related fields are active or inactive. For example, channel and memory options are disabled when the "Non-programmable" classification is selected. As a minimum, this field is required for the search criteria.

Select Channel/Memory: Channel and memory options are enabled when "Programmable" or "Digital" is selected. You may select any of the options for the channel/memory to limit the search criteria.

Select Shell Type: You may select a shell type to limit the search criteria.

![](roes-version-3-user-manual/119.png) Click this button to display all models meeting the search criteria in the "Select a New Model" list box.

Select a New Model: After searching using the 'Find Models' button, select a new model from this list box to change the model. Upon selecting a new model, the system clears out the component and secondary feature options list boxes, and populates the circuits in the "Circuit" list box that are available for the new model

Add/Remove Circuit/Components (Charge Options):

The manufacturer of the aid has provided the options presented in this section. Only certain combinations of options are allowed. This will help alleviate errors caused by selecting options that may not work or fit together. This section does not apply to FM, remote control devices or stock hearing aids.

Circuit (required): The list box for the Circuit will initially display all circuits available for the aid you selected on page 1 of the Service Request Form. If the circuit currently on the aid is known to the system, components and other options compatible to the circuit will be displayed for selection. If the circuit is unknown because we did not collect the data, the list boxes for components, interfaces and microphones will be empty. However, they will be populated as soon as you select a circuit.

Because there can only be one circuit installed on an aid, changing the circuit will remove the old circuit.

You must first select a circuit to add a charge or no-charge option if the circuit information is not known to the system.

Component, Interface, Microphone: Components, interfaces and microphones are displayed based on the circuit currently installed on the aid. The components and interfaces currently installed on the aid are displayed in the text areas shown on the right, and the microphone currently installed is displayed in the list box. The text areas may be incorrect if the aid was purchased prior to ROES 3.0 and we did not collect the data.

In general, you will click an option in a list box once to add the option. However, if the option is already listed in the text area, when you click that option, it will remove the option. If the option is not listed in the text area, clicking the same option twice will also remove the option. This functionality was added to the system so that a user can remove an option when the text area does not list the options installed on the aid because ROES 2.0 did not collect the data.

For microphones, selecting "None" in the list box will remove the microphone currently installed on the aid. If there is no existing microphone, no change will be made. Selecting a new microphone will add the microphone to the order and remove the old one if exists.

Secondary Features (No Charge Options)

Options for the secondary features will be listed based on the circuit selected. If the aid's circuit is known, all secondary feature options currently on the circuit will be displayed in the list boxes and the text areas. Adding and removing option functionality will work the same, in general, as it does for the circuit and components. However, clicking the same option twice to remove an option does not apply to secondary features. This section is not applicable to FM, remote control devices or stock hearing aids.

#### Model Change of an FM or Remote Control Device

Select a new model from the list box and click the ![](roes-version-3-user-manual/120.png) button.

Special Requests

This section is displayed if an aid has had a serial number assigned within the ROES/DALC system (i.e., not in the Pending status).

Aid Classification: Programmable or digital aids may incur additional charges when they are repaired. Please ensure the classification is correctly indicated.

Change Matrix To: This is a text field provided in case the aid's matrix needs to be changed.

Repair Damaged Case/Shell: For this type of repair, an ear impression/investment must be sent to the vendor along with the hearing aid. A mouse over function is provided to display help text when a user places the mouse over each radio button. Use the following guidelines for selecting the recase, replate or remake:

Recase: To re-pour with new ear impression, investment/reinvestment or make a new shell or case of a hearing instrument for the following reasons:

- Fit problems to include canal lengthening/shortening.
- Cracks, splits or holes.
- Addition or replacement of existing flex canals, concha, canal or helix locks.

Replate: Full replacement of the “faceplate” portion of an “ITE” hearing instrument to include; malfunctioning internal components, wiring or circuitry and faceplate damage including addition of new components where space on the faceplate is a concern.

Remake: When the combination of both, recase and replate are necessary in the repair action to make the hearing instrument perform as originally designed or to specifications indicated by a current audiogram. This should include the replacement of all malfunctioning internal and external components, circuits, shells, cases, and faceplates or to accommodate matrix changes. It should exclude: incomplete circuitry and damage caused by abuse.

Add Additional Chargeable Items: A repair vendor may charge additional cost in addition to the basic repair fee for some repair items such as Cros, Bicros or Bone Conduction.

Lost/Damaged: There is a provision in the contract to provide one-time warranty replacement of an aid if the patient loses the aid or damages it beyond repair. Click the checkbox to request the replacement.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains two possible actions that you may take:

![](roes-version-3-user-manual/121.png) Click this button to return to page 1 of the ROES3 Service Request Form to start over.

![](roes-version-3-user-manual/122.png) When you are satisfied with the selections you made so far, click this button to go to page 3 of the ROES3 Service Request Form. Even after going on to the next page, you may come back to this page to make changes. If the circuit selected in the circuit list box is different from the original circuit, you may be prompted, "Do you want to order the new circuit you selected in the circuit list box?"

![](roes-version-3-user-manual/123.png)

You may click the "OK button" to add the circuit to the order, or the "Cancel" button not to order the circuit.

### Page 3 - Service Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This page is used to record potentiometer settings for non-programmable aids, to indicate items that are being sent to the vendor with the hearing aid, to record additional comments to the vendor, and to indicate to where the repaired device should be shipped.

![](roes-version-3-user-manual/124.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient. It also displays the make, model, serial number and warranty type of the hearing device you selected. These fields cannot be edited.

### *Service Request Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your service request. A description of how to use each field is included below. Fields required for completion of the service request are indicated.

POT 1 - POT 6: POT 1 - POT6 provide a standard set of instructions for reading the potentiometer settings for non-programmable aids is provided below for your reference. You can also click the ![](roes-version-3-user-manual/125.png) icon to display the potentiometer reading instructions. You can leave the instruction page open or close it by clicking the close button on the top right corner of the page. Potentiometer settings recorded here are not sent to the vendor. Rather, they are used to reset the potentiometers when the vendor sends back the repaired aid without resetting them. This area is disabled if the aid does not have the serial number.

![](roes-version-3-user-manual/126.png)

Items To Vendor: This is a required field if the hearing device is to be delivered to Patient via DALC. Be sure to include items, size, length, etc. in the additional information box. This area is disabled if the device does not have the serial number.

Additional Information: Use this text box for any additional comments you would like to send to the vendor. This field is currently limited to 200 characters. Since repair items a user may select are limited when DALC is the repair vendor, use this field to communicate with DALC regarding the repair information as much as possible.

Ship Repaired Device To: Default is the Clinic. Select 'Patient via DALC' if you want the vendor to send the repaired device to DALC for DALC to inspect and send the device to the patient. You cannot select 'Patient via DALC' if the device is under the trial period, as it must be sent back to the clinic after the repair is made. This area is disabled if the device does not have the serial number.

Patient Delivery Address: Click the ![](roes-version-3-user-manual/127.png) button to view or change the current address of the patient. It is important the patient's address be current when you request the repaired aid be shipped to 'Patient via DALC', as DALC will use this address to send the aid to the patient. An explanation of how to use the address form to change the patient address may be found in the [Patient Delivery Address](#patient-delivery-address) section of this manual.

Station Delivery Address: Click the ![](roes-version-3-user-manual/128.png) button to view the station delivery address. You may edit certain fields or just verify that the address on file for the station is correct. You may also change the station delivery address by selecting a different site within your VISN or a site that does contract work for you. This address will print out on the order form as the "ship to" address for the hearing aids. See the [Station Delivery Address](#station-delivery-address) section for a description of the Station Delivery Address page.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains three possible actions that you may take:

![](roes-version-3-user-manual/129.png) Click this button to return to page 2 of the ROES3 Service Request Form.

![](roes-version-3-user-manual/130.png) When you are satisfied with the selections you made so far, click this button to go to the ROES3 Service Request Summary page.

![](roes-version-3-user-manual/131.png) Click this button to exit back to the patient's Order History page. If you have gotten through the complete order process but have not submitted your order, a message pops up at this point to alert you.

### Page 4 - Service Request Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Service Request Summary page displays the summary of the service requests currently being made. The service request will not be placed until the ![](roes-version-3-user-manual/132.png) button is pressed. The user may, at any time until the request is submitted, click the ![](roes-version-3-user-manual/133.png) button to return to previous pages to edit the order, or click the ![](roes-version-3-user-manual/134.png) button to delete the request. The command buttons will change after the request has been submitted successfully. "Edit" and "Delete" buttons are replaced with ![](roes-version-3-user-manual/135.png) and ![](roes-version-3-user-manual/136.png) buttons and the ![](roes-version-3-user-manual/137.png) button will appear on the bottom of the page.

The summary page shown below is displayed if the ![](roes-version-3-user-manual/138.png) button has not been pressed.

![](roes-version-3-user-manual/139.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section displays the name and Social Security number of the patient. These fields cannot be edited.

### Service Request Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table in this section displays the summary and cost information of the service requests.

Item column: The Item column shows the name of the hearing device for which a service request was made. Also shown is the HCPCS code for that item. The purchase order number displays the original CHA purchase order number if the service request is for an adjustment within the trial period. For an extra component order, it will display "pending" until the request is submitted. Once submitted and if the order is placed successfully, it will display a new CHA purchase order number. For all repairs, whether out of warranty or within the New-aid warranty period, it will initially display "pending", and then a repair purchase order number after the order is placed successfully.

Warranty Type column: See [Appendix C](#c.-warranty-types).

Cost column: The cost column displays an estimated cost for the service request per the CHA and repair contracts. If DALC is the repair vendor, " Pending repair vendor selection" will be displayed, as the system cannot estimate the repair cost at this time.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The buttons in this section will change after submission of the service request based on the status of the submission. There are eight possible actions that you may take:

![](roes-version-3-user-manual/140.png) Click this button to edit the service request currently ordered for the aid. It will take you to page 2 of the Service Request Form. This button is displayed if the request was not submitted.

![](roes-version-3-user-manual/141.png) Click this button to delete the service request currently ordered for the aid. This button is displayed if the request was not submitted.

![](roes-version-3-user-manual/142.png) Click this button to add another service request. Clicking this button will take you to page 1 of the Service Request Form, where you may select another hearing aid to order a service request.

![](roes-version-3-user-manual/143.png) Clicking this button will submit your service request. If all checkpoints have been cleared, it will return a purchase order number if it was "pending". Please verify that your order is correct prior to submission. You may experience a pause of several seconds while your request processes.

You may see the following error message if you try to submit a repair order when there is one already open. You must first cancel or certify the existing repair order depending on the situation: cancel if the repair order was created in error, or certify to close the order after the repair has been made. No further processing is allowed in this case.

![](roes-version-3-user-manual/144.png)

If the system is unable to create a new ROES 3.0 transaction, you will see an alert box that says "File error - please exit and contact DALC IRM". This type of message should be a rare occurrence and might indicate a system problem that will need to be resolved by DALC staff.

For users that do not have approval privileges, the alert box will display "Order in pending approval status!" These orders will require approval by a provider with the appropriate approval privileges.

In each of these situations a service request will not be submitted nor will a purchase order number be generated until further action is taken, either by the DALC or the clinic, depending on the message delivered.

All adjustment orders such as model or component changes will require processing by a DALC technician after your submission of the order. Only after the adjustment is processed by DALC, the service request order is sent to the vendor via EDI or fax. You will see the following pop-up message after successful submission of an adjustment order.

![](roes-version-3-user-manual/145.png)

![](roes-version-3-user-manual/146.png) Click this button to exit back to the patient's View Order History page without submitting the request. You will see a pop up box that says, “You have not submitted your order – click ok to exit anyway!” You should click the “OK” button if you wish to exit without submitting the request or “Cancel” to remain in the service request form.

![](roes-version-3-user-manual/147.png) Click this button to display the service request form that a clinic will need to send to the vendor with the hearing aid.

![](roes-version-3-user-manual/148.png) Click this button to print the service request form that a clinic will need to send to the vendor with the hearing aid. Be sure the printer is turned on before sending the print request.

![](roes-version-3-user-manual/149.png) Click this button when you are ready to exit back to the patient's View Order History page and/or exit ROES completely. The information on the Service Request Summary page will automatically be copied to your clipboard for pasting into the patient's clinical record or anywhere you choose.

### Page 5 - Hearing Aid Service Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the order has been submitted successfully, you will be able to display or print the service request form. This form must accompany the hearing device you are sending to the vendor for repair. If the request is for one time warranty replacement, you will still need to send this form to the vendor.

![](roes-version-3-user-manual/150.png)

Ship to: This is the station delivery address to where the vendor should send back the hearing device after it is repaired. If a clinic has requested the repaired device be sent to "Patient via DALC", the DALC address will be the delivery address.

Bill to: The invoices should always be billed to DALC.

Contact Person: This is the name of the contact person at the ordering facility for the vendor to contact for questions.

PO#: This field identifies the purchase order (PO) number generated by DALC. This field will list either a CHA purchase order number (e.g., 791G12345-6789) or a repair purchase order number (e.g., 7913G2345-6789) depending on the type of the service request and the warranty status. The original CHA purchase order number is the order number for any service request made within the contract trial period, including a repair order. For an extra component order made during the New-aid warranty period but after the trial period, the system will generate a new CHA purchase order number. For all other in warranty or out of warranty repairs, you will see a repair purchase order number.

A Hearing Aid Service Request Form is not an official purchase order, nor an authorization for work. The actual purchase order will be delivered from the DALC to the specified vendor via either EDI or hard copy fax. The exception to this is a service request order that is purely a repair order (vs. model change or component change). For repair orders, a printed hard copy of the order form with an assigned purchase order number serves as an official work order.

Patient: This field has the patient name and the last four digits of his or her SSN.

Account \#: This is the account number the vendor assigned to the clinic. Vendors primarily use this number to identify the clinic to where the repaired devices should be shipped.

Deliver On/Before: The vendors are required, by contract, to deliver the repaired aid to the clinic within a certain number of business days, depending on the contract, after receiving the purchase order.

Warranty Type: See [Appendix C](#c.-warranty-types).

Original PO#: This field displays, if known, the original CHA purchase order number under which the device was originally purchased.

Circuit Problems: This field lists the circuit problems an audiologist identified that need to be corrected.

Case/Shell Problems: This field lists the case or shell problems an audiologist identified that need to be corrected. Depending on the problem, you may need to send in the ear impression or investment along with the aid.

Special Requests: This field will list information regarding model changes, adding/removing options, matrix changes, recase, replate, remake request, repair items that require additional charges, the aid classification for programmable or digital aids, and/or one time lost and damage warranty replacement request.

Additional Information: This field lists the additional comments you made to the vendor.

Secondary Features: This field will list secondary feature options selected for the circuit.

Items to Vendor: This field identifies items on the hearing aid at the time the device was sent to the vendor for repair, for example, hearing aid, transmitter, and/or cord, etc. When the vendor sends the repaired device to DALC rather than to the clinic, DALC will check whether all items are returned from the vendor.

Total Cost: This is an estimated cost. The actual cost will be on the invoice received from the vendor. If DALC is the repair vendor, " Pending repair vendor selection" will be printed, as the system cannot estimate the repair cost at this time.

![](roes-version-3-user-manual/151.png) Click this button to go back to the Service Request Summary page.

## Cochlear Implant Registry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Page 1 – Cochlear Implant History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Cochlear Implant History page is used to view the existing cochlear implants for an individual. Through this page you are able to register a new implant or edit an existing one. The Cochlear Implant History page is displayed below:

![](roes-version-3-user-manual/152.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected as well as the user entering the information.

### *History Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The history section is a table displaying the current Cochlear implants for a patient. This is only a display of the current Cochlear Implant information. Within each implant you can select the ![](roes-version-3-user-manual/153.png) button to edit that Implant.

![](roes-version-3-user-manual/154.png) When this button is clicked, you will be directed to the “Cochlear Implant Registration Form” where you will be able to edit the information for the selected implant. The only fields that are editable for a previously registered implant are “Follow Up Site”, “Follow Up VISN”, “Processor Cost”, and “Outcomes”.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains two possible actions that you may take:

![](roes-version-3-user-manual/155.png) Click on this button to exit the Cochlear Implant Registry page.

![](roes-version-3-user-manual/156.png) Click on this button to add a new implant for the patient. When this button is clicked, you will be directed to the “Cochlear Implant Registration Form”, where you will be able to add all the information needed to register an implant. If an implant currently exists for the selected ear, it will inform you that an implant currently exists and that it will be replaced with the new implant if the information is submitted.

### Page 2 – Cochlear Implant Registration Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Cochlear Implant Registration Form is used to register individuals who have had Cochlear Implants within the Veterans Health Administration.

The following is an example of the Cochlear Implant Registry form:

![](roes-version-3-user-manual/157.png)

### *Order Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

#### General Information

Implant Date (required): Enter the date of the Cochlear implant in the text box or click on the ![](roes-version-3-user-manual/158.png) button to choose a date from the pop-up calendar. The date may be entered in almost any commonly-used format (i.e. 6-20-02, 6/20/02, June 20, 2002, etc.)

Activation Date: In the text box enter the date the Cochlear implant was activated or click on the calendar button to choose a date from the pop-up calendar. The date may be entered in almost any commonly-used format (i.e. 6-20-02, 6/20/02, June 20, 2002, etc.)

Ear Implanted (required): Select the appropriate radio button to indicate if the implant was performed for the left ear, or the right ear.

Implant Site: Enter the name of the site where the procedure was performed. This may or may not be a VA Facility. This is a free text field allowing 50 characters.

Implant VISN: From the drop down list, select the VISN of the site where the procedure was performed. If the VISN is not applicable, you can select “NA”.

Follow Up Site: Enter the name of the site that will perform the follow up visits and procedures. This may or may not be a VA Facility. This is a free text field allowing 50 characters.

Follow Up VISN: From the drop down list, select the VISN of the site that will perform the follow up visits and procedures. If the VISN is not applicable, you can select “NA”.

#### Implant Information

Make (required): From the drop down list, select the make of the Cochlear Implant. When a make is selected the “Model” drop down list is populated with the appropriate models for that make. The lists of make and model for the processors are also populated at this time. The make for a Processor can be different then the make for an implant.

Model (required): Select the implant model from the drop down list.

Serial \# (required): Enter the serial number of the implant in the text box.

Cost: Enter the cost of the Cochlear Implant. This is only the cost of the device itself.

Fitting: Select the appropriate radio button to indicate if the implant is the initial one or a replacement for an existing one.

#### Processor Information

Make (required): Select the make of the processor from the drop down list. If it is different than the implant make the processor model drop down list will populate based on the new make. Default value is the current value of the implant model.

Model (required): Select the processor model from the drop down list. When a model is selected the battery drop down list is populated with the appropriate batteries for the selected model.

Serial \# (required): Enter the serial number of the processor in the text box.

Cost: Enter the cost of the selected processor.

Fitting: Select the appropriate radio button to indicate if the processor is the initial one or a replacement for an existing one.

Battery: From the drop down list select the desired battery for the processor. All listed batteries are appropriate to use for the selected processor.

Order Battery: Select the appropriate radio button to order batteries for the selected processor(s). To change the delivery address of the patient, click on the ![](roes-version-3-user-manual/159.png) button. When clicking on this, it will allow you to view/edit the delivery address.

### *Outcomes*PIPSL Score: This table is used to gather information prior to the implant and after the implant. You may enter a pre-measure score and a post-measure score for various methods of testing. Based on these scores, a benefit score is derived from subtracting the pre-measure score from the post-measure score. The methods used in the PIPSL scoring are: USV, INT, RAF, ES, USNV, and PER. The Benefit score is not editable.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Quality of Life: This table is used to gather information based on personal satisfaction from the patient and another individual. These scores are recorded for readings prior to the implant and after the implant. You may enter a pre-measure score and a post-measure score for the patient and another individual. Based on these scores, a benefit score is derived from subtracting the pre-measure score from the post-measure score. The Benefit score is not editable.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains three possible actions that you may take:

![](roes-version-3-user-manual/160.png) Click on this button to exit back to the patient's Cochlear Implant History page. No information will be saved when clicking on the ![](roes-version-3-user-manual/161.png) button.

![](roes-version-3-user-manual/162.png) Click on this button to submit the current registration form. This information will replace any existing information if needed. After all information is processed, you will be directed back to the Cochlear Implant History page for that patient.

![](roes-version-3-user-manual/163.png) Click on this button after you have selected an implant and processor. A pop-up message reminds you of missing or invalid data. The next page delivered is the Audiometric Data for Cochlear Implant Registry.

### Page 3 - Audiometric Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiometric Data page is the last page for the Cochlear Implant Registry. This page is strictly a display of the audiometric data prior to the implant and after the implant. This information is displayed based on the implant date. This information is not editable. The audiometric data presented on this page is populated from data collected through the Audiometric Data Enter/Edit module exported in conjunction with ROES 3.0 as QUASAR patch ACKQ\*3.0\*3. That data is entered when the patient visits the clinic for an audiometric examination. When the exam is completed and signed by the provider the data is then transmitted to the DALC via EDI (Electronic Data Interchange). The data is filed at the DALC for display at the time a cochlear implant is registered.

![](roes-version-3-user-manual/164.png)

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains three possible actions that you may take:

![](roes-version-3-user-manual/165.png) Click on this button to exit back to the patient's “Cochlear Implant History Screen”. No information will be saved when clicking on the “Exit” button.

![](roes-version-3-user-manual/166.png) Click on this button to submit the current registration form. This information will replace any existing information if needed. After all information is processed, you will be directed back to the “Cochlear Implant History Screen” for that patient.

![](roes-version-3-user-manual/167.png) Click on this button to redirect you back to the “Cochlear Implant Registration Form”.

## Registering Devices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Device Registration Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Device Registration Form can be used to register a custom hearing aid, FM device, BTE (behind the ear) hearing aid, stock hearing aid, remote control, or assistive device to a patient’s record. The device may be selected from the DALC’s product database or entered as a free text make and model if the item cannot be found in the database or the make or model is unknown. This option may also be used to register a loaned device to a patient.

Registering a device to a patient authorizes that patient to receive batteries and repair services from the DALC.

The Device Registration Form is shown below.

![](roes-version-3-user-manual/168.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name and Social Security number of the patient you selected. The user displayed in the “Entered by:” field is the user who is actually entering the order. These fields cannot be edited.

### *Order Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requesting Service (required): Select the name of the requestor’s service from the drop down box.

Disability Code (required): From the drop down box, select the disability of the patient that is associated with the order you are entering.

Make (required): The device “Make”, or manufacturer, can be selected by using the drop down box on the left or, if unknown or not in the DALC database, can be entered as a free text field on the right. When you select a “Make” by clicking on an item in the drop down list, you will be presented with a pop-up prompt (shown below) requiring you to enter one or more characters of the model you are looking for. This is due to the fact that the number of hearing device models in the DALC database may be too vast to populate a drop down list efficiently. After entering one or more characters of the model name, click “OK”. The “Model” drop down list will be populated with those items that start with the characters entered.

![](roes-version-3-user-manual/169.png)

Model (required): The device model can be selected by use of the “Model” drop down box on the left, or if the model is unknown or not in the DALC database, can be entered as a free text field on the right. If you are using the drop down box to make your selection you may click on the “search” feature to re-populate the drop down list with a different collection of model names.

> NOTE: You must use either both drop down boxes on the left or both free text boxes on the right.

Issue Date (required): Enter the date the aids were issued to the patient, if known, or an approximate date, if unknown. You may type the date in using the keyboard, or use the calendar pop-up feature. Most date formats are allowed including the use of "T" for today or "T+-n" for today plus or minus a number of days.

Serial Number (required for serialized devices): The serial number field must be entered for all stock and custom hearing aids. A serial number is not, however, required for assistive devices. Please be especially careful that you enter the serial number correctly.

> FYI: The software will automatically convert all lower case alpha characters in the serial number to upper case.

Furnished By (required): Choose the appropriate selection from the drop down list to indicate how the patient acquired the device.

- Clinic Direct Purchase: Devices purchased directly from a hearing aid vendor (for example: off contract items.) These devices may include stock hearing aids, custom hearing aids, assistive devices, FM devices and remote control devices. You may not use the "CDP" furnished by type for serial numbers already existing in the DALC's database. Use the "CDP" furnished by type the first time a clinic purchased device is registered to a patient. For subsequent registrations of the same device, use "Clinic Prior Issue" as the furnished by type.
- Clinic Station Stock: Stock hearing aids originally purchased through the DALC. The system will check the serial number against the DALC database to determine if this serial number is recorded as a stock item that has not yet been issued to a patient. A pop-up error message will alert you if the serial number/make/model combination cannot be found on file. The warranty for "CSS" aids is 3 years from DALC receipt from the vendor or, 2 years from registration to a patient.

> FYI: If a clinic station stock hearing aid is returned to the clinic by the patient and the clinic wishes to register it to a different patient, choose "Clinic Prior Issue" as the ‘furnished by’ type. The warranty will stay intact if transferred from one patient to another.

For aids returned to your clinic that your clinic wishes to then re-register to another patient, select "Clinic Prior Issue" from the drop down list. You no longer have to return a loaner to DALC stock when the patient returns it. Just re-register it to another patient when loaned out again. You will be alerted if this device is already on the record of another patient and asked if you would like to register it to the current patient. The alert box will look like this:

![](roes-version-3-user-manual/170.png)

This alert box will display after you have finished entering all data and have clicked on the “Add to Order” button. At that time the ROES Device Registration Summary page will be displayed showing the item you entered. Click “OK” to assign this aid to the current patient. If you decide not to reassign this aid to the current patient, by clicking the “Cancel” button, the entry will be deleted from the summary page.

> NOTE: A BTE purchased off the custom hearing aid contract cannot be registered to a different patient within the 180-day trial period. After the trial period, the aid may be registered to a different patient.

Select "Military Issue" for an aid that the patient was given while in a branch of the military. Serial numbers entered as "Military Issue" must be brand new entries in the DALC's database.

Select "Self-Purchased" for aids that the patient self-purchased outside of the VA. Serial numbers entered as "Self-Purchased" must be brand new entries in the DALC's database.

Select "Other" if none of the other categories are appropriate. Serial numbers entered as "Other" must be brand new entries in the DALC's database.

Replenish stock if available?: This radio button which is defaulted to "Yes" is only enabled when "Clinic Station Stock" is selected as the furnished by type. By default, the DALC will send a replacement aid, if available, of the same make and model to add to the clinic's stock. Check the "No" radio button if you do not want the DALC to ship a replacement aid to your clinic.

Serial Number of Replaced Item (optional): This field is used to indicate that the aid you are registering is replacing an aid already on the patient’s record. You will be presented with a list of serialized devices on record for this patient. An aid selected from this list will be moved to the patient’s “Unauthorized Devices” list.

Ear (required): Click on the “right” or “left” radio button to select the ear of the item being registered. An ear designation is required for all devices with the exception of FM devices, remote control devices and assistive devices.

Battery Type: Select the battery furnished to the patient from the drop down list provided. You may only select a battery that the DALC currently carries.

Order Batteries?: Click on the “Yes” radio button to indicate to DALC staff that you would like an initial order of batteries sent to the patient. Select the “No” radio button if no batteries are to be sent. You are required to select a battery type if you click the "yes" radio button.

Delivery address for batteries: On the right hand side of the screen is a button that you may click to access the patient delivery address page. An explanation of how to use the address form may be found in the [Patient Delivery Address](#patient-delivery-address) section of this manual.

Remarks: You may enter up to 50 characters in this free text field. This field should only be used to inform the DALC about something regarding this aid.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/171.png) Click this button to return to the Patient Order History page without placing an order for a registration

![](roes-version-3-user-manual/172.png) Click on this button to reset the fields on the form to the original defaults.

![](roes-version-3-user-manual/173.png) You should click on this button when you have finished putting in all of the information about the line item you are ordering. If you have left out any required information, you will see an alert box, like that shown below, telling you which fields are missing. When all fields have been entered correctly, the ROES Device Registration Summary page will be rendered.

> NOTE: After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/174.png) button on the summary screen. When you return to the order form, you will see an additional button in the command section labeled “View Order Summary”.

![](roes-version-3-user-manual/175.png) This button will load the ROES Device Registration page without adding another line item to the order.

### ROES Device Registration Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Device Registration Summary page displays the line items that you have entered for submission. This information should be reviewed prior to clicking on the ![](roes-version-3-user-manual/176.png) button. After clicking the "submit" button a pop-up box will let you know that your order has been submitted for processing. A ![](roes-version-3-user-manual/177.png) button will then appear. An example of the ROES Device Registration Summary page is shown below.

![](roes-version-3-user-manual/178.png)

### *Summary Table*Commodity Group column: This is the commodity group as selected on the Device Registration Form.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Item column: This is the model of the item selected and to be recorded on the patient’s record. After the order has been submitted you will see the order number of the ROES 3.0 transaction below the item. The order number will show as “Pending” prior to submission of the order.

Disability column: This column shows the disability selected for the line item. This column may be different for each line item if the patient has different disabilities that apply to the different items being registered.

Issue Date column: This column shows the issue date entered for this line item.

Serial Number column: This column shows the serial number that was entered for this line item. It is very important to double check the serial numbers keyed in prior to submission of the order.

Ear column: This column shows the ear, or side, selected for the item being registered.

Battery column: This column shows the battery selected for this item.

## Record Updates (Patient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Record Update Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Update Patient Record Form is used to make changes to the patient’s Eligibility Station, postal address in DALC records, hearing aids authorized for repair and batteries that are on the patient’s record. (See the sample display below)

![](roes-version-3-user-manual/179.png)

![](roes-version-3-user-manual/180.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the patient’s name, the patient’s Social Security number, and the user’s name. It cannot be edited within this update form.

### *Update Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your changes. A description of how to use each field is included below. Fields required for completion of the order are indicated.

### Demographic Updates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### *Edit Authorizing Clinic*Eligibility Station: This is the station responsible for care of the patient with regard to the disability on that line. Two choices are available in the drop down box – the patient’s current station of record and the user’s station. In order to edit the address information below, at least one eligibility station must be the same as the user’s station. In order to edit the authorized aids, the Eligibility Station for Deaf/B, Deaf/U, or A0/DIS must be the user’s station. You can make the change by selecting the correct station from the drop down box. You can ONLY change from the station shown to your station.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remarks – These are remarks that were entered when the disability was initially entered. They cannot be edited with this option.

### *Change Address*New Address: The fields on the right side of this section display the patient’s current address with edit capability. The address can be changed by editing the related fields.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### *Edit Authorized Aids* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section may be used to remove aids from the patient’s record. The bottom of the table will display a button that will allow you to toggle between the patient’s authorized and unauthorized aids. The title of the button will change as you go from one set of aids to the other. Information in the individual columns may NOT be edited through this option. The aid may only be removed from or returned to the patient’s record.

![](roes-version-3-user-manual/181.png) This button may be used to remove an aid from service or to return an aid to service. The title of the button will change when clicked. The color of the line will also change to highlight the choice. If you have toggled to the Unauthorized Aids list the button will have the appropriate label and will also change when selected.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/182.png) Clicking on this button will return all information to the default originally seen on the patient’s record.

![](roes-version-3-user-manual/183.png) Clicking on this button will submit the record updates. You will have the option to print the changes you just made. If you wish to make additional changes you will then need to return to the View Order History page.

![](roes-version-3-user-manual/184.png) Clicking on this button returns to the View Order History page

## Authorized Aids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES View Authorized Aids page is used to review the aids currently on a patient’s record. No editing may be done on this page. You may View Unauthorized Aids, go to the Update Record, or exit to the View Orders page.

![](roes-version-3-user-manual/185.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the name of the patient whose record is being changed, the patient’s Social Security number, and the name of the user signed on to the computer. It cannot be edited within this update form.

### Authorized Aids Section 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the Aids authorized for the patient.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/186.png) Clicking this button returns to the View Order History page and menu

![](roes-version-3-user-manual/187.png) This button displays aids formerly on the patient’s record. The title of this button will change as you toggle between the

![](roes-version-3-user-manual/188.png) Clicking this button will take you to the ROES 3 Update Patient Record Form

## Delivery Address Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patient Delivery Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Delivery Address page is accessible from several different modules within ROES 3.0. Use it to verify and edit, if necessary, the delivery address for items that will be shipped to a patient from the DALC. The left side of the page shows the patient address that the DALC currently has on file for the selected patient. The right side of the page shows the same address but allows you to edit the address fields. You may indicate if the address entered is a temporary address by entering temporary start and end dates.

The address will be stored in the DALC's database if you select "Yes" to "update the Patient File with the delivery address". If you edit the address but select "No" to update the patient address, the edited address will be used for the delivery of goods but not recorded.

![](roes-version-3-user-manual/189.png)

> NOTE: You may use the pop-up calendar feature for entering temporary start and end dates or type the date in as free text. Most date formats will be accepted including "T" for today or "T +- n" for today plus or minus n number of days.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/190.png) Click this button to take you back to the previous page without recording any changes.

![](roes-version-3-user-manual/191.png) Click this button to reset any changes you made back to the original settings.

![](roes-version-3-user-manual/192.png) Click on this button after you have edited the address. The new address you entered will be used for delivery of goods associated with this order.

> FYI: To make sure this address gets stored permanently in the patient record, click on "yes" to update the DALC patient file with the new address.

### Station Delivery Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Station Delivery Address page is accessible from the Custom Hearing Aid module, the Service Request module, and the Station Stock module within ROES 3.0. This is the address that will be printed on the vendor order form and where the vendor will ship the aids.

The displayed address is recorded in the Institution file at the DALC and cannot be edited. You may, however, select a different address to have the aids shipped to. The selectable sites in the drop down list include all sites within your VISN and also any sites that you may contract with (if provided to the DALC for inclusion in ROES 3.0) When you select a different site, the page will be refreshed with the address of the new site.

You may edit your service's routing number, and fill in the attention line. These are free text fields and the data entered will only be used for this order.

![](roes-version-3-user-manual/193.png)

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/194.png) Click this button to take you back to the previous page without recording any changes.

![](roes-version-3-user-manual/195.png) This button will reset any changes you made back to the original settings.

![](roes-version-3-user-manual/196.png) Click on this button after you have edited the allowable address fields. The address changes you entered will be used for delivery of goods associated with this order.

# Access from the Desk Top 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ROES Desk Top Entry Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to accessing ROES 3.0 through CPRS, separate ROES 3.0 functions can be accessed through a desktop application not tied to CPRS. This application should be available through a desktop shortcut created during the ROES installation process. If such a shortcut or other means to invoke the application is not available, please contact your local facility IRM Service.

In general, when this application is invoked, the following actions take place:

- Assembles end user information
- Initiates a browser session to the ROES 3.0 web application and passes the assembled information to ROES 3.0

These actions are described in the subsequent sections of this document.

The ROES 3.0 Desk Top Entry Page is the entry point when accessing DALC from the Desktop Icon. From this page you are able to access various patient displays and updates, service request actions, station stock orders, and other miscellaneous actions. The ROES 3.0 Desk Top Entry Page is displayed below:

![](roes-version-3-user-manual/197.png)

### Desk Top Entry Page Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Actions link: If this link is selected, it will allow you to look up a patient, view patient information; update a patient record, enter a service request, and authorize/un-authorize devices.

Station Actions link: This link will allow you to enter commodity orders for a station.

Pending Actions link: This link allows you to view any pending actions and if authorized to resolve them.

Contact Us link: This link allows you to contact various departments, and or individuals at the DALC.

What's New in ROES III link: This link renders a page that gives the user information on new features in ROES III.

FAQ link: This link contains the answers to any frequently asked questions and should be a first stop for help information.

DALC Catalog link: This link gives the user access to the DALC Catalog in .pdf format.

Quit link: Clicking on this link will quit the ROES 3.0 desktop application.

## Patient Actions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Lookup page is the first page you will see if you enter through the Desktop application and choose ‘Patient Actions’ from the ROES 3.0 desktop Entry page. This page allows you to choose a patient from the DALC database.

![](roes-version-3-user-manual/198.png)

Enter Patient: The text box and ![](roes-version-3-user-manual/199.png) button allow patient selection. Enter the last name, the last initial and last four of the Social Security number (e.g. C0003), or the patient’s entire name. Then click on the "Search" button.

If only one patient matches your input, you will be taken directly to the Patient Information page. A drop down box will appear if more than one patient matches the input. You may choose a patient from the drop down box. If the information entered produces more than 50 matches a warning box will appear and ask you to enter more information and narrow the search. Click the ![](roes-version-3-user-manual/200.png) button and you will be returned to the Patient Lookup page.

## Patient Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES 3 Patient Information Page displays information maintained on the DALC system for the specified patient. The page offers access to the Order History page. No editing can be done from this page.

![](roes-version-3-user-manual/201.png)

### Header Section 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Name, Social Security Number, and User signed on to DALC.

The Display section contains general information on the patient, including the address and disabilities recorded at DALC. None of the information can be edited from this page.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/202.png) Click this button to return to the Patient Lookup Page and select another patient.

![](roes-version-3-user-manual/203.png) Click this button to go to the View Order History page. This page will be similar to the View Order History page that was previously described in the section titled “Access through CPRS”. All orders for the patient will be displayed, but there is limited number of actions that can be performed when entering the View Order History page from the Desktop. Some of the actions that can be performed are the entry of a Service Request order, Update Patient record, Access the Parameter Page, and Process Pending Actions. Please review the View Order History page in the Access through CPRS Section of this manual for specific information.

## Station Actions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View Station Order History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Station Stock Order History page is the first page presented when entering Station Stock actions. From this page you are able to view station orders for your primary station or, alternatively, for additional stations with which you are affiliated. You will be directed to this page after having entered your DALC Access and Verify codes. Below is a sample of the ROES Station Stock Order History page.

![](roes-version-3-user-manual/204.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the current station name and number. You can select the station number for display to one that is in the drop down list. This list is generated off of the first three digits of the main station.

### *Existing Orders Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing orders section is a table that contains orders that have previously been entered for the selected station. These orders are listed in date order and can be viewed by Processed, or Unprocessed orders. A detailed view is available for each order.

Tran Date column: This is the date the order was placed at the DALC. This date is also a link to a detailed display of the order. Click on the blue date to view the detailed display.

Order Number column: This is a unique number for a specific order. This number will either be a purchase order number, or a specific number to an unprocessed order. This number should be used as the identifier when assistance is needed at the DALC.

Order Type column: This field displays the type of order, for example, stock hearing aids, batteries, and prosthetic items.

By column: This field displays the name of the individual who placed the order. This is not the name of the person who requested the order.

Status column: This is the current status for the order.

Item(s) column: This field displays the items that were selected for the order. An order may contain more than one item.

### *Actions Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actions section contains all the links to various applications in the ROES 3.0 desktop application. You can create new stock orders, change current user settings for ROES 3.0 processing, and process pending actions. Some of these links may be unavailable to you based on your current user privilege setting for processing.

Commodity Stock Orders link: Use this link to access the ordering process for station stock orders on batteries, prosthetic socks, accessories, etc.

Station Parameters link: Use this link, if accessible, to access the Station Parameters page. From this link you are able to grant various processing permission, and terminate a user’s access.

Exit to Desk Top Entry link: Click on this link to return to the Desk Top Entry menu page.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains four possible actions that you may take:

![](roes-version-3-user-manual/205.png) Click on this button to view the previous orders for the patient. If you are on the first list of orders the list will stay the same.

![](roes-version-3-user-manual/206.png) Click on this button to view the next series of orders for the patient.

![](roes-version-3-user-manual/207.png) Click on this button to view orders that have been processed.

![](roes-version-3-user-manual/208.png) Click on this button to view any orders that have not been.

> NOTE: Unprocessed orders are orders that ROES was unable to process through to completion, usually due to a system problem at the DALC. These orders will be picked up daily by DALC staff and processed by a technician. No action is required by the clinician.

### Station Stock Order Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Station Stock Order Form is used to order all products handled by the DALC with the exception of custom hearing aids. The form allows you to order multiple line items, including different commodities, with a single transaction. The order form is displayed below:

![](roes-version-3-user-manual/209.png)

### *Heading Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the site name of the station for which the order is being placed. This field cannot be edited within this order form.

### *Order Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box.

Commodity Group (required): From the drop down box, select the commodity group of the product you wish to order. This action will populate the next drop down box (“Select Item :”) with the items in the commodity group you chose. If you choose the Prosthetic Socks commodity group, you will need to use the search feature to find the sock you wish to order since the list of possible selections is so long.

Select Item: From this drop down box, select the item (product) you wish to order. This drop down box is populated based on the selection of the Commodity Group. To find an exact item, or a specific list of items you can use the “Search” button to populate the “Select Item” drop down list. When an item is selected, the field for “DALC Quantity on Hand” will be populated with the current inventory at the Denver Acquisition & Logistics Center.

![](roes-version-3-user-manual/210.png) This button to the right of the “Select Item:” prompt can be used with all commodity groups to help you find the exact item you wish to order. When you click on the button, a search text box will open. There you may type in one or more of the characters of the item (e.g., “W-5” for wool socks, 5-ply). Typing in more characters will reduce the number of items that are displayed. When you click on the “OK” button, the line item drop down box will be populated with all of the items that begin with the characters you typed (“W-5”).

![](roes-version-3-user-manual/211.png) Click on this button to order items that the DALC may not normally keep in stock. A new page will be rendered that will allow you to enter a free text make and item name. These requests will be evaluated on a one-by-one basis.

Quantity (required): You can select the number of items you wish to order from this drop down box. If an item can only be ordered in a specific multiple, this list in the box will only contain the available multiples for the item (e.g., batteries in packages of 8 will contain selections of 8, 16, 24, etc.). The list will also be bounded by minimum and/or maximum order quantities.

DALC Quantity on Hand: This box displays the amount of the selected item the DALC currently has on hand. If the quantity ordered exceeds the DALC Quantity on Hand, the DALC will fill an order partially with the quantity on hand. The outstanding items will go into backorder status, and shipment may be delayed beyond the 4-day standard. This field cannot be edited.

Remarks: This text box will allow you to enter any extra order, delivery, or other information that may be needed to process the order.

Current Delivery Address: These lines of text show you the current address of the station that the order will be delivered to. This information can be modified to send the order to a different location, but it will not be a permanent change in the DALC database. To make a change in the delivery address, click on the ![](roes-version-3-user-manual/212.png) button. This will open a new page allowing you to view and change the delivery address. An explanation of how to use this form may be found in the [Station Delivery Address](#station-delivery-address) section of this manual.

Delivery Category (required): You have three options for delivery, Routine, Priority, and Emergency. Routine orders will be shipped within 4 business days, priority orders will be shipped within 24 hours on a business day, and emergency orders will be delivered within 24 hours if received by 2:00 pm MT on a business day. Orders will be defaulted to “Routine”. If you wish to select another option, click on the appropriate radio button. If “Emergency” is selected, you must enter a facility contact phone number in the text box below the Delivery Category prompt.

Enter a phone number for emergency orders (required for emergency orders): If you selected a delivery category of “Emergency”, you must enter a phone number for the station, starting with area code. This is required for overnight shipment.

Routing Symbol: This box will allow you to enter a routing symbol so delivery can be made to a specific department of the station. This is not a required field.

Deliver To: If the order is to be delivered to a specific individual, that person’s name can be entered in this field. This is not a required field.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial command section contains three possible actions that you may take:

![](roes-version-3-user-manual/213.png) If you click on this button, you will return to the ROES Patient Orders page without placing an order.

![](roes-version-3-user-manual/214.png) If you click on this button, all fields for the current line item you are ordering will be returned to the default settings.

![](roes-version-3-user-manual/215.png) You should click on this button when you have finished putting in all of the information about the line item you are ordering. Taking this action will open the ROES Order Summary page, which will contain the order for the line item you just submitted and any other line items that have been previously submitted.

After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/216.png) button on the summary page. When you return to the order form, you will see additional buttons in the command section labeled “View Order Summary” and “Accept Changes”.

![](roes-version-3-user-manual/217.png) Clicking on this button will load the ROES Order Summary page without adding another line item to the order.

![](roes-version-3-user-manual/218.png) Clicking on this button will resubmit the order if there were any changes done, and take you to the ROES Order Summary page.

If you attempt to exit from the order form without submitting your order, you will see a pop up box that says, “You have not submitted your order – click ok to exit anyway!” Click the “OK” button if you wish to exit without saving the order or “Cancel” to remain in the order form.

### Stock Special Request Order Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Station Stock Special Request Order Form is used to order products that are not found on the drop down list of the Station Stock Order page. The form allows you to order multiple line items, including different commodities, with a single transaction. These orders will be evaluated and processed if deemed necessary. The order form is displayed below:

![](roes-version-3-user-manual/219.png)

### Heading Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The heading section contains the site name of the station for which the order is being placed. This field cannot be edited within this order form.

### Order Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following prompts will help you complete your order. A description of how to use each field is included below. Fields required for completion of the order are indicated.

Requested By (required): From this drop down box, select the name of the provider or other user who actually requested that the order be placed. The name of the user entering the order will be defaulted in the drop down box. This list is populated from the DALC's database based on users from that facility that have access to the DALC system. If the requestor’s name is not on the list, contact your ROES Supervisor to have it added.

Requestor’s Service (required): Select the name of the requestor’s service from the drop down box.

Select Commodity Group (required): From the drop down box, select the commodity group of the product you wish to order. This action will populate the next drop down box (“Select Item:”) with the items in the commodity group you chose. If you choose the Prosthetic Socks commodity group, you will need to use the search feature to find the sock you wish to order since the list of possible selections is so long.

Enter Make (required): Enter the make of the item in the text box that you wish to order.

Enter Item (required): Enter the item name in the text box that you wish to order from the drop down list.

Quantity (required): Enter the number of items you wish to order.

Remarks: This text box will allow you to enter any extra order, delivery, or other information that may be needed to process the order.

Current Delivery Address: These lines of text show you the current address of the station that the order will be delivered to. This information can be modified to send the order to a different location, but it will not be a permanent change in the DALC database. To make a change in the delivery address, click on the button with the text ![](roes-version-3-user-manual/220.png). This will open a new page allowing you to view and change the delivery address. An explanation of how to use this form may be found in the [Station Delivery Address](#station-delivery-address) section of this manual.

Delivery Category (required): You have three options for delivery, Routine, Priority, and Emergency. Routine orders will be shipped within 4 business days, priority orders will be shipped within 24 hours on a business day, and emergency orders will be delivered within 24 hours if received by 2:00 pm MT on a business day. Orders will be defaulted to “Routine”. If you wish to select another option, click on the appropriate radio button. If “Emergency” is selected, you must enter a facility contact phone number in the text box below the Delivery Category prompt.

Enter a phone number for emergency orders (required for emergency orders): If you selected a delivery category of Emergency, you must enter a phone number for the station, starting with area code. This is required for overnight shipment.

Routing Symbol: This box will allow you to enter a routing symbol so delivery can be made to a specific department of the station. This is not a required field.

Deliver To: If the order is to be delivered to a specific individual, that person’s name can be entered in this field. This is not a required field.

### *Command Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial command section contains three possible actions that you may take:

![](roes-version-3-user-manual/221.png) If you click on this button, you will return to the Station Stock Order Form page.

![](roes-version-3-user-manual/222.png) If you click on this button, all fields for the current line item you are ordering will be returned to the default settings.

![](roes-version-3-user-manual/223.png) You should click on this button when you have finished putting in all of the information about the line item you are ordering. Taking this action will open the ROES Order Summary page, which will contain the order for the line item you just submitted and any other line items that have been previously submitted.

After you have submitted one line item for the order, you can continue to add additional line items by using the ![](roes-version-3-user-manual/224.png) button on the summary screen. When you return to the order form, you will see additional buttons in the command section labeled View Order Summary and Accept Changes.

![](roes-version-3-user-manual/225.png) This button will load the ROES Order Summary page without adding another line item to the order.

![](roes-version-3-user-manual/226.png) This button will resubmit the order if there were any changes done, and take you to the ROES Order Summary page.

If you attempt to exit from the order form without submitting your order, you will see a pop up box that says, “You have not submitted your order – click ok to exit anyway!” Click the OK button if you wish to exit without saving the order or Cancel to remain in the order form.

### Station Stock Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES Station Stock Summary Section is used to display all items contained on the order and allow you edit, delete, add or submit your order. The summary section is displayed below:

![](roes-version-3-user-manual/227.png)

### *Summary Section*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Summary section is a table that displays all items in the order. Below is a description of each column and the actions that can be done.

Commodity Group column: This column displays the commodity group for each item ordered.

Item column: This column contains a brief description of each item, the associated HCPCS code, and the order number. The order number will not be displayed until the order is submitted for processing.

Delivery Category column: This column displays the type of delivery for the item.

Quantity column: This shows the quantity for this item selected by the user.

Unit Price column: This column displays the individual price for the item.

Total Price column: This column displays the total cost for the item. This is based on the unit price and the quantity selected for the item.

![](roes-version-3-user-manual/228.png) This button will delete the item from the order. This button will only delete a specific item and not the entire order.

![](roes-version-3-user-manual/229.png) This button allows you to edit an item from the order. Selecting this button will take you back to the Station Stock Order Form, where you will be able to change any information as needed.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The command section contains two possible actions that you may take:

![](roes-version-3-user-manual/230.png) If you click on this button, you will return to the ROES Station Stock Order Form for entry of an additional item. Multiple items may be entered for one order.

![](roes-version-3-user-manual/231.png) If you click on this button, all items for the order will be submitted for processing. When the order is submitted you will receive a pop-up box stating, “Order has been submitted”, and the order number will appear in the item column for each item ordered. After submitting the order, the only action you may take is to exit the Station Stock Summary page.

## Managing ROES 3.0 Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The System Parameters page is available only to designated individuals with ROES supervisory privileges. From this page, a supervisor can control user access to ROES 3.0 and its components by granting or removing specific user access privileges.

The page displays the names of the ROES users for the specific station, their title, and their assigned privileges. The supervisor can use the drop-down list and checkboxes on this page to assign or modify a user’s title and privileges.

The following titles can be selected from the drop-down list:

- Audiologist
- Speech Pathologist
- Health Tech
- Student
- Clerical Support

> NOTE: The user's title controls how certain pages and drop-down lists throughout ROES 3.0 are populated.

Supervisor check box: When the Supervisor check box is checked, it automatically selects all the other check boxes for the user. This will give the user all privileges in ROES 3.0. To selectively inactivate one or more privileges, clear the corresponding check box to remove that privilege. All users with the Supervisor check box selected can assign privileges for other users.

The other check boxes grant individual privileges as follows:

Approval Privileges check box: When the Approval Privileges check box is checked, the user can submit orders to the DALC without requiring further review. Users with this privilege can access the Pending Actions page and approve orders entered by a person without this privilege.

Certification Privileges check box: When the Certification Privileges is checked, the user can certify a custom hearing aid order.

Approve Stock Orders check box: When the Approve Stock Orders check box is checked, the user can enter station stock orders for their site.

Deactivate User check box: When the Deactivate User check box is checked the user will be denied access to all of the applications within the DALC, including ROES 3.0 and RIS.

![](roes-version-3-user-manual/232.png)

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/233.png) Click this button to return to the View Order History page or to the Desk Top Entry page.

![](roes-version-3-user-manual/234.png) Click this button to save any changes that were made on the System Parameter page.

## Pending Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pending Actions page allows you to view and act on orders that are in need of some type of approval for a particular station or patient. If coming in from the desktop, you will only see actions for the selected station. If coming in from the CPRS/patient access, you will only see actions for the selected patient. This page is broken down into three types of approvals:

- Orders that need to be approved by an individual with approval privileges before the order can be submitted to the DALC and processed
- Orders that have been processed but need to be certified
- Orders that have been processed but need to be issued

Below is a sample of the Pending Actions page.

![](roes-version-3-user-manual/235.png)

### View Pending Actions Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pending actions section is a table that contains orders that have previously been entered for a selected patient or station, but are in need of some type of action. These orders are listed in date order and a detailed view is available for each order.

### ROES Orders – Pending Approval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of orders that have been entered through ROES 3.0 but the entering user(s) do not have privileges allowing the orders to be submitted to the DALC and processed. These orders will need to be approved by an individual who has approval privileges. An order listed in red is deemed to be delinquent. To approve an order, click on the order date for the order. This will direct you to the proper detail screen so the order can be approved. Once the order is approved, it will be removed from the Pending Actions screen.

### *ROES Orders – Pending Certification*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of hearing aid orders that have been processed through ROES 3.0 that are pending certification. An order listed in red is deemed to be delinquent. To certify an order, click on the order date for the desired order. This will direct you to the CHA Detail screen. In the CHA Detail screen, the certification date can be entered, and the aid is removed from the Pending Actions screen. A certification becomes delinquent 20 days after the order is placed or 5 days after DALC receives and enters the invoice.

### *ROES Orders – Pending Issue*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of hearing aid orders that have been processed through ROES 3.0 that are pending issuance. An order listed in red is deemed to be delinquent. To certify an order, click on the order date for the desired order. This will direct you to the CHA Detail screen. In the CHA Detail screen, the issue date can be entered, and the aid is removed from the Pending Actions screen. An issue becomes delinquent 30 days after certification.

### Command Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](roes-version-3-user-manual/236.png) Click this button to return to the *View Order History* page or to the *Desk Top Entry p*age.

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TERM</strong></th>
<th><strong>DEFINITION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ASPS</strong></td>
<td>Audiology and Speech Pathology Service</td>
</tr>
<tr class="even">
<td><strong>C&amp;P</strong></td>
<td>Compensation and Pension</td>
</tr>
<tr class="odd">
<td><strong>CPRS</strong></td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="even">
<td><strong>DB</strong></td>
<td>Decibel</td>
</tr>
<tr class="odd">
<td><strong>DALC</strong></td>
<td><p>Denver Acquisition &amp; Logistics Center , also known as VADALC.</p>
<p>Previously known as DDC (Denver Distribution Center)</p></td>
</tr>
<tr class="even">
<td><strong>Delivery Category</strong></td>
<td>There are three options for delivery, Routine, Priority, and Emergency. Routine orders will be shipped within 4 business days, priority orders will be shipped within 24 hours on a business day, and emergency orders will be delivered within 24 hours if received by 2:00 pm MT on a business day.</td>
</tr>
<tr class="odd">
<td><strong>Disability</strong></td>
<td>Disability recorded on the Patient’s record at DALC</td>
</tr>
<tr class="even">
<td><strong>Ear</strong></td>
<td>Ear aid issued for, usually designated as R, L or X for unknown</td>
</tr>
<tr class="odd">
<td><strong>Eligibility</strong></td>
<td>This is the eligibility associated with the disability shown on the same line</td>
</tr>
<tr class="even">
<td><strong>Eligibility Date</strong></td>
<td>This is the date that the eligibility was entered in the DALC record. It may not be edited with this option</td>
</tr>
<tr class="odd">
<td><strong>Eligibility Station</strong></td>
<td>This is the station responsible for care of the patient with regard to the disability on that line</td>
</tr>
<tr class="even">
<td><strong>ES</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="odd">
<td><strong>Hz</strong></td>
<td>Hertz</td>
</tr>
<tr class="even">
<td><strong>INT</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="odd">
<td><strong>IRM</strong></td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td><strong>Issue Date</strong></td>
<td>Date the aid was issued as recorded in DALC records.</td>
</tr>
<tr class="odd">
<td><strong>Military Issue</strong></td>
<td>An aid that the patient was given while in a branch of the military</td>
</tr>
<tr class="even">
<td><strong>Model</strong></td>
<td>Hearing aid model</td>
</tr>
<tr class="odd">
<td><strong>PER</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="even">
<td><strong>Permanent Address</strong></td>
<td>Patient’s permanent address or place of residence.</td>
</tr>
<tr class="odd">
<td><strong>PIPSL Scores</strong></td>
<td><p>Performance Inventory for Profound and Severe Loss.</p>
<p>Table used to gather information prior to a cochlear implant and after the implant</p></td>
</tr>
<tr class="even">
<td><strong>PSAS</strong></td>
<td>Prosthetics &amp; Sensory Aids Service</td>
</tr>
<tr class="odd">
<td><strong>RAF</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="even">
<td><strong>RIS</strong></td>
<td>Remote Inquiry System</td>
</tr>
<tr class="odd">
<td><strong>ROES</strong></td>
<td>Remote Order Entry System</td>
</tr>
<tr class="even">
<td><strong>Self-Purchased</strong></td>
<td>Item that the patient self-purchased outside of the VA, must be brand new entries in the DALC database</td>
</tr>
<tr class="odd">
<td><strong>Serial Number</strong></td>
<td>Current registered serial number of aid</td>
</tr>
<tr class="even">
<td><strong>Temporary Address</strong></td>
<td>Temporary Address, i.e., patient is on vacation</td>
</tr>
<tr class="odd">
<td><strong>USNV</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="even">
<td><strong>USV</strong></td>
<td>Method used in the PIPSL scoring</td>
</tr>
<tr class="odd">
<td><strong>Vendor</strong></td>
<td>Original manufacturer of the hearing aid</td>
</tr>
<tr class="even">
<td><strong>VHA</strong></td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td><strong>Warranty Types</strong></td>
<td>1 year and 2 year</td>
</tr>
</tbody>
</table>

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. How ROES 3.0\*4 Calculates Eligibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A patient is automatically declared eligible for ROES 3.0 orders if standard calls into the patient record determine that he falls into categories SC, COM, POW, PH, PG3, PG4, CAN or BRI, NCA, 0CA, OIF, SCV, OGA, NSC, PG8 or has a previously approved eligibility in the ROES ELIGIBILITY CONFIRMATION file (#791814). If the standard calls do not make that determination then NSC is the default used to access ROES for a registered patient.

SC eligibility is accepted if the patient is in Priority Groups 1, 2, 3, 5, 7 or 8 and has a Service Connected Disability (0 to 100%) for hearing loss based on diagnostic codes:

6016, 6200 to 6110, 6199 to 6211, 6250 to 6263, or 6277 to 6299

COM eligibility is accepted if the patient is listed as Service Connected and has a total disability of 10% or greater for conditions other than hearing-related disorders as defined in category 1 and in Priority Groups 1-3.

POW eligibility is accepted if the patient has a POW status indicator.

PH eligibility is accepted if the patient has a PH indicator.

PG3 eligibility is accepted if the patient is in Priority Group 3.

PG4 eligibility is accepted if the patient is in Priority Group 4, including the homebound (HB) and those receiving Aid and Attendance benefits (AAA).

CAN or BRI eligibility is accepted if the patient is Service Connected and listed in the AGENCY/ALLIED COUNTRY field of the PATIENT file as either Great Britain or Canada. If the eligibility is CAN or BRI then the user will see the message: "\*\*Alert\*\* Allied Agency Agreement must be on record at the DALC".

NCA eligibility is accepted , if the patient has Primary Eligibility of NSC and is either in Priority Group 5 or is receiving a VA Pension.

0CA eligibility is accepted , if the patient is 0% Service Connected for a condition other than the hearing-related disorders defined in category 1 (SC) and is in either Priority Group 5, 7a , or 8 .

OIF eligibility is accepted if the patient is a veteran of Operation Iraqi Freedom or Operation Enduring Freedom and in Priority Group 6.

SCV eligibility is accepted if the patient is in Priority Group 6.

OGA eligibility is accepted if the patient has a secondary eligibility that includes OTHER FEDERAL AGENCY.

NSC eligibility is accepted if the patient is not Service Connected, but qualifies as Priority Group 7c or 7g.

PG8 eligibility is accepted, if the patient is in priority group 8 and not already included in OCA or SC.

These eligibility categories are all based on medical need. By requesting orders for the patient, the audiologist stipulates that he/she has evaluated the patient and has determined that medical need exists for amplification in accordance with 38 CFR 17.149, VHA Directive 2002-039, and the supplemental guidance published by the A&SP National Office. For these reasons the National Program offices have agreed that the emails requiring PSAS approval of some of the ROES eligibility categories are no longer necessary.

## B. Enrollment Priority Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Priority Group 1

Veterans with service-connected disabilities rated 50% or more disabling

Priority Group 2

Veterans with service-connected disabilities rated 30% or 40% disabling

Priority Group 3

Veterans who are former POWs

Veterans awarded the Purple Heart

Veterans whose discharge was for a disability that was incurred or aggravated in the line of duty

Veterans with service-connected disabilities rated 10% or 20% disabling

Veterans awarded special eligibility classification under Title 38, U.S.C., Section 1151, "benefits for individuals disabled by treatment or vocational rehabilitation"

Priority Group 4

Veterans who are receiving aid and attendance or housebound benefits

Veterans who have been determined by VA to be catastrophically disabled

Priority Group 5

Nonservice-connected veterans and Noncompensable service-connected veterans rated 0% disabled whose annual income and net worth are below the established VA Means Test thresholds

Veterans receiving VA pension benefits

Veterans eligible for Medicaid benefits

Priority Group 6

Compensable 0% service-connected veterans

World War I veterans

Mexican Border War veterans

Veterans solely seeking care for disorders associated with:

Exposure to herbicides while serving in Vietnam; or

Exposure to ionizing radiation during atmospheric testing or during the occupation of Hiroshima and Nagasaki; or

For disorders associated with service in the Gulf War; or

For any illness associated with service in combat in a war after the Gulf War or during a period of hostility after November 11, 1998

Priority Group 7

Veterans who agree to pay specified co-payments with income and/or net worth above the VA Means Test threshold and income below the HUD geographic index

Sub-priority a: Noncompensable 0% service-connected veterans who were enrolled in the VA Health Care System on a specified date and who have remained enrolled since that date

Sub-priority c: Nonservice-connected veterans who were enrolled in the VA Health Care System on a specified date and who have remained enrolled since that date

Sub-priority e: Noncompensable 0% service-connected veterans not included in Sub-priority a. above.

Sub-priority g: Nonservice-connected veterans not included in Sub-priority c above.

Priority Group 8

Veterans who agree to pay specified co-payments with income and/or net worth above the VA Means Test threshold and the HUD geographic index

Sub-priority a: Noncompensable 0% service-connected veterans enrolled as of January 16, 2003 who have remained enrolled since that date

Sub-priority c: Nonservice-connected veterans enrolled as of January 16, 2003 and who have remained enrolled since that date

Sub-priority e: Noncompensable 0% service-connected veterans applying for enrollment after January 16, 2003

Sub-priority g: Nonservice-connected veterans applying for enrollment after January 16, 2003

## C. Warranty Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A blank warranty type indicates the hearing device has not yet established a warranty because the clinic has not received the device. This also applies when there is a certification, but no ship date (because DALC has not received the invoice) or issue date. Only model changes or component changes are allowed.

In trial period: The hearing device was issued but DALC has not yet received the invoice, and therefore, there is no ship date to establish the warranty. Model changes, component changes and/or repairs are allowed.

New (In Trial Period): The hearing device has the New-aid warranty and within the contract trial period. Model changes, component changes and/or repairs are allowed.

New (Beyond Trial Period): Only extra component orders and/or repairs are allowed.

Out of Warranty: Only repairs are allowed.

Service Warranty: An out of warranty repair will result in the service warranty for six months.

## D. Request Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Repair: Repairs apply to any service request made on a device that does not have the New-aid warranty

Model change: Model changes are allowed only during the contract trial period.

Component change: Component changes are allowed only during the contract trial period.

Extra component order: Extra components can only be ordered after the contract trial period. Only those components available under the same classification and shell type can be ordered. If you order a new circuit as an extra component, the vendor will remove the current circuit on the aid and replace it with the new one you just ordered.

Model change/repair: The request has a combination of model change and repair actions.

Component change/repair: The request has a combination of component change and repair actions.

Extra component order/repair: The request has a combination of extra component order and repair action.

## E. Statuses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 order statuses are displayed on a number of the application's pages including the Order History Display and several of the detail pages.

> NOTE: On the Pending Action list, a status of "Pending" indicates that the request was entered by a user without approval privileges and is waiting to be completed by a user with the appropriate privileges. Once approved, the status will change to "Certification Pending" for CHA actions or "Awaiting Processing" for commodity orders and repairs.

### For Processed Orders:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Certification Pending - Orders with this status have been placed and are awaiting certification by the clinician. This status is typical for CHA actions and repairs.

For orders requiring certification, the status will be updated to "Issue Date Pending" for CHA orders and "Complete" for those orders that do not require certification.

- Issue Date Pending - Orders with this status are awaiting entry of an issue date by the clinician. This status is typical of CHA actions including model changes.
- Complete - CHA actions with this status require no additional action on the part of the clinician. Commodity orders displaying this status have been shipped and require no additional action by DALC staff.
- Backordered - This status indicates that the DALC is awaiting receipt of additional stock for order fulfillment. This status is typical of commodity orders.

Canceled - An order with this status has been canceled by the clinician or the DALC. This status may be displayed for CHA actions or commodity orders.

Repair actions that are not combined with model changes, adjustments, or extra component orders may have the following statuses:

Open - This status is typically displayed while the device being repaired is in transit to the vendor, the DALC or the clinic.

Awaiting Payment - This status indicates that a repair has been certified, however, the invoice has either not been received or has not been entered.

Closed - For repair actions, this status indicates that the order has been completed.

### For Unprocessed Orders:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Awaiting Processing - This status indicates that the order could not be processed, usually due to a problem requiring DALC staff review. These orders are monitored by DALC staff and corrected and processed in a timely manner. Upon DALC review, the status will change to "Certification Pending" for CHA actions and complete for other transaction types.
- Error - This status also indicates a problem requiring DALC staff review. These orders are monitored by DALC staff and corrected and processed in a timely manner.

## F. Security Agreement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Date:

From:

Subj: VADALC Computer Access Security Agreement

To: Chief, Information Resources Management Division (905IRM)

This is a request for access to the Veterans Affairs Denver Acquisition & Logistics Center (VADALC) Computer System made in accordance with the following security agreement:

VADALC COMPUTER ACCESS SECURITY AGREEMENT

As a user of the VADALC computer system, you will be given an access code, verify code and menu options that are necessary to provide information and ordering options required for your position.

When you sign on to the system with your access and verify codes, the computer recognizes only the codes entered and not the person entering those codes. Any transactions performed in the computer will be recorded under your name, and you will be held responsible for these transactions, including your facility’s financial responsibility for products and services ordered under your code. Care must be taken in signing off of the system so that another user does not enter at the point where you finished. <u>YOU ARE RESPONSIBLE FOR SAFEGUARDING YOUR CODES.</u>

The confidentiality of all patient information is protected by Federal Law. The unauthorized disclosure of any information from the patient's record or computerized files may be punishable by federal law. <u>YOU ARE RESPONSIBLE, BY LAW, FOR PROTECTING ALL PATIENT AND VA RELATED COMPUTER INFORMATION.</u>

Suspected security violations should be immediately reported to the VADALC Chief, IRM Division, 303-914-5160. Any questions concerning policies or procedures should also be referred to the Chief, VADALC IRM Division. Failure to comply with security procedures could result in the loss of computer privileges. In addition, the VADALC reserves the right to deny access when suspected violations occur. <u>YOU MUST REPORT SUSPECTED COMPUTER SECURITY VIOLATIONS.</u>

Please check the box below that best represents your organization.

|                                 |           |                                                      |
|---------------------------------|-----------|------------------------------------------------------|
| VA AUDIOLOGY & SPEECH PATHOLOGY | ARMY      | OTHER (<span class="smallcaps">specify below)</span> |
| VA PROSTHETICS                  | NAVY      |                                                      |
| VA FISCAL                       | AIR FORCE |                                                      |
| OTHER VA SERVICE                | MARINES   |                                                      |

By signature below I acknowledge that I have read the above agreement and understand my responsibilities and obligations.

|                                                                                           |     |       |     |          |     |      |     |       |     |       |     |          |     |     |
|-------------------------------------------------------------------------------------------|-----|-------|-----|----------|-----|------|-----|-------|-----|-------|-----|----------|-----|-----|
| User Name (Please print)                                                                  |     | Title |     |          |     | Date |     |       |     |       |     | User SSN |     |     |
|                                                                                           |     |       |     |          |     |      |     |       |     |       |     |          |     |     |
| Signature of Requesting User                                                              |     |       |     |          |     |      |     |       |     |       |     |          |     |     |
| Facility Name/Address (include routing)                                                   |     |       |     | City     |     |      |     |       | /   | State |     |          | /   | Zip |
|                                                                                           |     |       |     |          |     |      |     |       |     |       |     |          |     |     |
| Please give the above mentioned member of my staff access to the VA DALC computer system. |     |       |     |          |     |      |     |       |     |       |     |          |     |     |
| Signature of Approving Official                                                           |     |       |     | Phone \# |     |      |     | Title |     |       |     |          |     |     |

Mail requests to: VA DENVER ACQUISITION & LOGISTICS CENTER (905IRM)

P O BOX 25166

DENVER CO 80225-0166

Or FAX to: (303) 914-5159

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 2cc Coupler Gain 38

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add Additional Chargeable Items 59

Aid Ordered for 44

Air and Bone Conduction 37

authorized 84, 90

aids 3, 10, 83, 84, 85

aids, edit 84

devices 10

end users 1, 2

for repair 82

hearing devices 49

purchase or repair 17

backorder 96

status 20

Backordered 115

By column 9, 94

Change Matrix To 58

CI Registry link 9

Circuit/Components column 39

classification 28, 29, 30, 52, 57, 114

aid 58, 67

current 57

eligibility 111

identify 57

select 57

Classification 29

Clinic Direct Purchase 78

Clinic Station Stock 78, 79

Commodity Group column 25, 81, 101

Component, Interface, Microphone 58

Copy Over buttons 29

Copy Over Buttons 35

Cost column 64

Cost of Warranty column 40, 46

Cost with 1 yr Warranty Column 32

Cost with 2 yr Warranty Column 32

CPRS 3, 5, 7, 9, 89, 92, 93, 104, 106

Access Through 6

Tools Menu 6

Current Circuit/Components 57

Custom Hearing Aids link 9

DALC 1, 2, 106

Access and Verify codes 93

accessing from the Desktop icon 90

address 66

Catalog 90

Catalog link 90

computer resources 2

contract in place 56

contractual agreements 49

customers 2

database 52, 77, 78, 79, 97, 99

Electronics Lab 56

Fiscal Division 13

IRM 6, 40, 47, 65

product database 76

Quantity on Hand 20, 96

receipt 78

Remote Inquiry System 6

repair contracts 56

review 116

staff 40, 47, 65, 79, 115, 116

staff review 116

stock 78

system 77, 92

technician 40, 47, 51, 65

DALC patient file 87

DALC records 82

Delivery Category 20, 23, 25, 97, 99, 101, 106

Device Registration 76, 78, 80, 81

Summary page 80

Device Registration link 9

Disability Code 19, 22, 43, 77

D-Mic (Directional Microphone) 35

Ear column 39, 81

Ear Implanted 72

eligibility 10, 106, 109

acceptabilty 109

categories are based on medical need 6, 110

date 106

determination 3

patient 6, 50

primary 109

special classification 111

Station 50, 82, 83, 107

status 6

error message

Due to existing open order 64

Unable to Print Order Form... 18

When serial number, make/model combination cannot be found, 78

Exit ROES link 10

Exp Date 50

Fitting Formula 38

FMs/Remotes link 9

Follow Up Site 70, 72

Furnished By 78

Implant Site 72

Issuing Station 50

Item column 25, 39, 40, 46, 64, 81, 101

Item(s) column 9, 94

Items To Vendor 61

Lost/Damaged 59

Matrix Selection 38

Model Column 32

New (In Trial Period) - remote device 55

Order Number column 9, 94

Order Type column 9, 94

Other Commodities link 9

Out of Warranty - stock hearing aid 56

Patient Delivery Address for Batteries 38, 44

Pending Actions link 10, 11, 90

PIPSL Score 73

PO# 41, 47, 66

Original 67

POT 1 - POT 6 60

Quantity column 25, 101

Recase 59

Record Updates link 10

Remake 59

Remotes Column 32

Repair Damaged Case/Shell 58

Repair Vendor 56

Replate 59

Requestor’s Service 19, 22, 28, 44, 50, 96, 99

requests 20, 96

Mail to: 118

repair 49

service 18, 49, 63, 64

special 52, 58, 67

Secondary Features (No Charge Options) 58

Select a New Model 57

Select Aids by 28

Select Channel/Memory 57

Select Commodity Group 20, 23, 99

Select Device Type 44

Select Make 44

Select Model 44

Select Shell Type 57

Serial Number column 9, 81

Service Request link 9

Ship Repaired Device To 61

Special Instructions 38, 44

Speech Audiometry 38

Standard options 36

Station Delivery Address for Aids 38

Station Parameters link 10, 94

Status column 9, 94

supervisory designation 3

Total Cost row 40, 47

Total Price column 25, 101

Tran Date column 9, 94

Transaction Type 28

Type of Transaction 20, 23, 44

unauthorized

aids 84

devices 79

disclosure 117

Unit Price column 25, 101

Vendor codes 35

Vendor Column 31

VISN 38, 44, 62, 70, 72, 87

Follow Up 72

Implant 72

VistA

codes 6

Warranty Type 50, 64, 67

# #
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)