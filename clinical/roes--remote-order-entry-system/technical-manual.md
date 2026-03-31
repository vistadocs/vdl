---
title: ROES Version 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
description: The Remote Order Entry System (ROES 3.0) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC). This manual provides information regarding the technical components of the ROES 3.0 software. The information in
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - roes
  - table
  - contents
  - patient
  - application
  - order
  - strong
  - dalc
  - entry
  - manual
page_count: 0
word_count: 4898
section_count: 32
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/rmpf3_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=99"
---

![](roes-version-3-technical-manual/001.png)

Remote Order Entry System

(ROES)

Technical Manual

![](roes-version-3-technical-manual/002.png)

Version 3.0\*4

October 2003

(Updated) February 2011

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
- [Orientation](#orientation)
  - [General Rules for ROES 3.0 Data Entry pages](#general-rules-for-roes-30-data-entry-pages)
  - [Symbols Used in Manual](#symbols-used-in-manual)
  - [ROES 3.0 Display Considerations](#roes-30-display-considerations)
  - [Recommended Desktop Minimums for ROES 3.0](#recommended-desktop-minimums-for-roes-30)
  - [## Getting Additional Information](#getting-additional-information)
- [Chapter 1: Implementation and Maintenance](#chapter-1-implementation-and-maintenance)
  - [Application Architecture Overview](#application-architecture-overview)
  - [Overview of Installation Instructions](#overview-of-installation-instructions)
  - [Companion QUASAR Patch](#companion-quasar-patch)
- [Chapter 2: Files](#chapter-2-files)
- [Chapter 3: Flow Charts](#chapter-3-flow-charts)
  - [## ROES 3.0 Patient Order from CPRS](#roes-30-patient-order-from-cprs)
  - [Get Patient Information](#get-patient-information)
  - [Eligibility Determination](#eligibility-determination)
  - [Desktop Station Order Application](#desktop-station-order-application)
- [Chapter 4: Routines](#chapter-4-routines)
  - [VistA Routine List](#vista-routine-list)
  - [Delphi Routine list](#delphi-routine-list)
- [Chapter 5: Exported Options](#chapter-5-exported-options)
  - [ROES 3.0 Patient Order from CPRS (GUI)](#roes-30-patient-order-from-cprs-gui)
  - [Station Orders from the Desktop (GUI)](#station-orders-from-the-desktop-gui)
  - [## Archiving/Purging](#archivingpurging)
- [Chapter 6: Entry Points & APIs](#chapter-6-entry-points-apis)
  - [New Remote Procedures](#new-remote-procedures)
  - [External Relations](#external-relations)
  - [Integration Agreements](#integration-agreements)
  - [Internal Relations](#internal-relations)
    - [Authority to Use ROES 3.0](#authority-to-use-roes-30)
    - [Internal Option Use](#internal-option-use)
    - [Remote System Access](#remote-system-access)
- [# Acronyms](#acronyms)
- [Glossary](#glossary)
- [Appendices](#appendices)
  - [A: Error and Other Messages](#a-error-and-other-messages)
  - [## B: Mail Groups](#b-mail-groups)
  - [C: Section 508 Compliance Statement](#c-section-508-compliance-statement)
  - [## D: Request for Access and Verify Codes from DALC](#d-request-for-access-and-verify-codes-from-dalc)
- [<span class="mark">REDACTED</span> Index](#span-classmarkredactedspan-index)
|                    |                                      |                                    |
|--------------------|--------------------------------------|------------------------------------|
| Date           | Description                      | Author                         |
| September 16, 2003 | Format manual and input revisions    | <span class="mark">REDACTED</span> |
| September 18, 2003 | Revised format                       | <span class="mark">REDACTED</span> |
| October 20, 2003   | Revised base on NVS input            | <span class="mark">REDACTED</span> |
| July 2007          | Changed DDC to DALC                  | <span class="mark">REDACTED</span> |
| February 2009      | Modifications and enhancements added | <span class="mark">REDACTED</span> |
| February 2011      | Changes to eligibility process added | <span class="mark">REDACTED</span> |
Table of Contents

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the Remote Order Entry System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System Version 3.0 (ROES 3.0) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC).

## Scope of Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides instructions for the installation and maintenance of the ROES 3.0 software.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is intended for Information Resource Management (IRM) staff. However it may also be helpful to: National V*ist*A Support (NVS), System Design & Development (SD&D), and ADPACs in Audiology and Speech Pathology Service (ASPS) and Prosthetics and Sensory Aids Service (PSAS).

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Remote Order Entry System (ROES) Version 3.0\*4 Security GuideRemote Order Entry System (ROES) Version 3.0\*4 User ManualRemote Order Entry System (ROES) Version 3.0\*4 Installation Guide*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Order Entry System (ROES 3.0) gives authorized end users at VHA facilities the ability to order products and services from the VA Denver Acquisition & Logistics Center (DALC). This manual provides information regarding the technical components of the ROES 3.0 software. The information in this manual is intended for IRM or equivalent staff who are responsible for the installation, maintenance, and support of the ROES 3.0 application and local facility V*ist*A and general IT resources.

## Purpose of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 was developed to simplify and enhance the ordering of products and services from the Denver Acquisition & Logistics Center (DALC) including hearing aids and numerous other commodities. Ancillary functions such as updating patient records and registering devices may also be done through the Web interface. ROES 3.0 is accessed from the end user’s workstation as a Web application through the browser allowing orders to be placed using an interactive, real-time, point and click interface. ROES 3.0 also accommodates keyboard navigation and entry.

ROES 3.0 was designed to use advanced technologies and practices in software design, supporting hardware platform, database management, and network integration to provide DALC customers and staff with simple and easy to use ordering capabilities. The application provides patient care providers and associated Veterans Health Administration (VHA) staff with comprehensive patient information and order histories. It was also designed to use progressive procurement and distribution practices, advanced general business practices, and current VA Regulations, which have evolved since the introduction of ROES 2.0

A definitive criterion used to establish the strategic direction and development path for ROES 3.0 involved combining:

- The necessity to optimize compatibility and data communications capability with established VA systems and business practices
- The objective of applying leading edge information technology resources to strategic business systems development, comparable to the best that can be found in the private sector
- The desire to provide a "progressive continuity" to DALC customers, implementing significant enhancements to the existing application, while minimizing transition apprehension for end users

## Benefits of ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ROES 3.0 application architecture makes available, for the first time, a Web-based application for activities such as order placement and inquiry functions, while retaining and improving upon the character-based interface formerly used in ROES 2.0. It is expected that a Web interface, enabling point-and-click functionality, allows information to be presented in a more organized fashion, enhancing the navigation and data entry procedures.

In another departure from previous versions, the majority of ROES 3.0 system software and data files reside on DALC computer resources, leaving only selected key components on local Medical Center systems. There are a number of factors supporting this transition. These include:

- Assurance of a singularity and consistency of the available product database
- Opportunity for immediate real-time processing of orders placed
- Reduced dependency on VAMC application of patches and file modifications

Higher capacity VA wide area network resources implemented since ROES 2.0 enable these architectural changes.

In addition to the overall architecture, ROES 3.0 provides a number of process-specific benefits, features, and functionality improvements, such as the following:

1.  Provides users with a simplified ordering process.
2.  Includes cost comparison functionality for display/selection of all contract hearing aids meeting selected specifications.
3.  Allows repair orders to be entered by the provider.
4.  Includes a module to enter audiometric data and display or print the resulting information.
5.  Provides information in "real time".
6.  Provides enhanced commodity ordering capabilities.
7.  Provides enhanced device registration capabilities.
8.  Provides enhanced display/update capabilities for authorized aids.
9.  Provides enhanced station stock ordering capabilities.
10. Decreases delivery time to patients since orders are submitted immediately for processing.
11. Links with the CPRS clinical record application already in place in the VHA environment.
12. Provides increased accuracy in patient eligibility determination prior to order placement, with improvements to subsequent reporting and statistical analysis.
13. Provides access to multiple ROES 3.0 functions (clinical and administrative) through a comprehensive entry point.
14. Provides supervisory designation of user authorization/approval levels.
15. Provides a Cochlear Implant registry for tracking of cochlear implant information.
16. Reduces the likelihood of erroneous orders (i.e., orders for combinations of device specifications that cannot be accommodated by hearing aid manufacturers).

# Orientation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Rules for ROES 3.0 Data Entry pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  There are no "double clicks" in ROES 3.0. Click the selection one time only.
2.  There are no "right mouse button” commands in ROES 3.0.

> NOTE: There is a key distinction between Windows-based applications (where double-clicks and right-button functionality are common) and web applications. There will not be a noticeable consequence to the user for these actions; however, the results may be unexpected. Double clicking may cause a drop-down list to open and close quickly. Right-clicking will produce selectable functions made available by the browser, but nothing specific to ROES. We strongly discourage use of the right-click in order to prevent the use of the browser's back and forward functions.

3.  It is recommended that users not click the "X" in the top right hand section of the ROES 3.0 browser window to close a window. Use the navigational links and buttons provided within the application to exit the system. Closing the browser window without properly exiting the application will not have any detrimental effects on the user but may leave an open user session and incomplete or 'phantom' order information in the application.
4.  Only use the ![](roes-version-3-technical-manual/003.png) ![](roes-version-3-technical-manual/004.png) or ![](roes-version-3-technical-manual/005.png) command buttons provided on the ROES\*3.0 pages for navigation - never use the windows provided "back" and "forward" commands.
5.  The command buttons within the application perform background housekeeping functions that maintain the integrity of the order as a user navigates through the ordering process. The Windows browser's 'Forward' and 'Back' commands bypass those functions and could result in loss of information from the order.
6.  “Grayed out” fields cannot be accessed.
7.  Any ![](roes-version-3-technical-manual/006.png) button will return you to the *View OrderHistory* page.

## Symbols Used in Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In code examples, the caret (^) or 'U' may be used interchangeably as separators.

The caret is also used to designate a global reference when used in front of a global name as in "^DPT(".

## ROES 3.0 Display Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: ROES 3.0 application pages display best at a display resolution of 1024x768. If this is not an end user's preferred resolution, ROES pages will not appear properly formatted. This will not affect application functionality, but may make page content more difficult to understand and navigate. If an end user chooses to increase their resolution to 1024x768, they should be aware that all other Windows applications and objects in their Windows environment will be reduced in size.

## Recommended Desktop Minimums for ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>SPECIFICATION</strong></td>
<td><strong>RECOMMENDED MINIMUM</strong></td>
</tr>
<tr class="even">
<td><strong>Processor</strong></td>
<td>866 MHz</td>
</tr>
<tr class="odd">
<td><strong>Memory</strong></td>
<td>512 MB</td>
</tr>
<tr class="even">
<td><strong>Hard Drive</strong></td>
<td>20 GB</td>
</tr>
<tr class="odd">
<td><strong>Video</strong></td>
<td>Super VGA</td>
</tr>
<tr class="even">
<td><strong>CD-ROM</strong></td>
<td>32x CD</td>
</tr>
<tr class="odd">
<td><strong>Monitor</strong></td>
<td>17" VGA, .28 pixel resolution</td>
</tr>
<tr class="even">
<td><strong>LAN Interface</strong></td>
<td>10/100 remote wake-on-LAN Ethernet Interface</td>
</tr>
<tr class="odd">
<td><strong>Keyboard</strong></td>
<td>101 -key</td>
</tr>
<tr class="even">
<td><strong>Mouse</strong></td>
<td>MS-Compatible Wheel or Button Mouse</td>
</tr>
<tr class="odd">
<td><strong>Operating System*</strong></td>
<td><p>Microsoft Windows 9x</p>
<p>Microsoft Windows NT Workstation v4.0 or Windows 2000 Pro strongly recommended.</p></td>
</tr>
<tr class="even">
<td><strong>Browser</strong></td>
<td>Internet Explorer v6+</td>
</tr>
</tbody>
</table>

\*NOTE: ROES 3.0 is compatible with Microsoft Windows XP.

\*\*NOTE: There are no minimum Browser Service Pack requirements.

A system meeting the above specifications can be expected to provide the functionality necessary for ROES 3.0. The VA Assistant Secretary for Information and Technology has established a set of minimum configurations for any new procurement of desktop systems across the enterprise (VA Directive 6401). For most of the specifications listed above, the VA minimum baseline exceeds the recommended minimum for ROES 3.0. The above specifications are provided to allow for use of equipment in current inventory, if necessary. In assessing procurement and/or other resource acquisition actions to meet ROES 3.0 desktop requirements, each facility is advised to give consideration to the specifications mandated by the above-mentioned Directive. Conformance with these established and/or emerging VA standards is encouraged. A dynamic update of the VA desktop standards is maintained at <span class="mark">REDACTED</span>.

## ## Getting Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following resources for additional information about the Remote Order Entry System (ROES).

- Visit the V*ist*A document library: <http://www.va.gov/vdl/> for the ROES 3.0 PDF and WORD documentation.
- Use the *KIDS Build File Print* \[XPD PRINT BUILD\] option if you would like a complete listing of package components exported with this software.
- Use the *KIDS Install File Print* \[XPD PRINT INSTALL FILE\] option if you'd like to print out the results of the installation process.
- Use the *List Routines* \[XUPRROU\] option prints a list of any or all of the ROES 3.0 routines.
- The Installation and User manuals also contain additional information.

# Chapter 1: Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Application Architecture Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 includes application components that reside on two systems: the VAMC V*ist*A system and the DALC system. The VAMC components include ‘M’ routines, RPC Broker calls, and Delphi executables. The general purpose of these components is to gather information and initiate an interactive session to the DALC-resident ROES 3.0 Web application, passing the assembled information to the application. Once in the Web application, ROES users then place orders and perform other order management functions within that application.

Different capabilities within ROES 3.0 are invoked by each of two Delphi executables. One executable and associated set of broker calls integrates as an option on the CPRS Tools menu (see also *Chapter 3:* [Charts](#chapter-3-flow-charts)). This set of components performs the following functions:

- Gathers [patient information](#get-patient-information) for the selected patient
- Determines the patient’s [eligibility](#eligibility-determination) for DALC services
- Assembles patient and user information
- [Initiates a browser session](#roes-3.0-patient-order-from-cprs) to the ROES 3.0 Patient Web application and passes the assembled information to ROES with a secure https connection
- Allows for copying of specified order information to the Windows clipboard with subsequent pasting to a CPRS Progress Note or to an external application

The second combination of Delphi executable and associated set of broker calls comprises an executable [application](#desktop-station-order-application) that can be invoked directly (separate from CPRS) or from an application shortcut, and performs the following functions (see also *Chapter 3:* [Charts](#chapter-3-flow-charts)):

- Assembles user information
- Initiates a browser session to the ROES 3.0 Web application and passes the assembled information to ROES 3.0 Station web site

The DALC-resident component of ROES 3.0 exists as a Web-based order entry application. The interactive order entry process utilizes the browser as the application interface. Depending on which of two ROES 3.0 entry points is accessed (determined by the calling Delphi executable), end users have access to specific functional modules associated with the entry and management of orders for DALC products and services. Navigation and order entry is accomplished using typical Windows and Web methods, including drop-down selection, check boxes, radio buttons, free text, etc. Information entered in the Web application is processed by the DALC order fulfillment system.

## Overview of Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation of ROES 3.0 requires both server-side V*ist*A installation procedures and client-side desktop installation procedures.

The ROES 3.0 distribution package includes a KIDS build. The KIDS build installs the necessary routines, menu options, and RPC broker calls within the V*ist*A environment.

The ROES 3.0 GUI requires that the RPC Broker Listener V1.1 be installed on any workstation from which either GUI application will be executed. Refer to the RPC Broker Website: <span class="mark">REDACTED</span> to install the RPC Broker Listener.

> NOTE: If a workstation can already connect successfully via CPRS, BCMA, or PCMM, then the RPC Broker has already been installed.

Refer to the *ROES 3.0 Installation Guide* for complete installation instructions.

## Companion QUASAR Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT NOTE: DALC ROES 3.0 order processing incorporates patient-specific audiometric information from the Quality: Audiology and Speech Pathology Audit and Review (QUASAR) package. A companion QUASAR patch (ACKQ\*3.0\*13) provides end users with data entry and display capabilities for this information. It is recommended that ACKQ\*3.0\*13 be installed concurrently with ROES 3.0 if it has not previously been installed.

# Chapter 2: Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one file previously exported with the ROES 3.0 package. It is for the storage of eligibility requests and replies. It is a standard ROES name spaced (RMPF), FileMan-compatible file. After the installation of patch RMPF\*3.0\*4, this file will only be used for previously stored eligibilities and may if the future be removed. New eligibilities are no longer stored in this file, but recalculated each time.

Prior [eligibility determinations](#eligibility-determination) entries were stored in the "^RMPF(791814," global in the following format:

^RMPF(791814,D0,0)= (#.01) PATIENT \[1P\] ^ (#.02) DATE REQUEST ENTERED \[2D\] ^

(#.03) ENTERING USER (ASPS) \[3P\] ^ (#.04) EXPIRATION DATE \[4D\]

^RMPF(791814,D0,1)= (#1.01) SUGGESTED ELIGIBILITY \[1F\] ^ (#1.02) EMAIL MSG NUMBER \[2P\]

^RMPF(791814,D0,2)= (#2.01) PSAS ELIGIBILITY \[1F\] ^ (#2.02) APPROVE/REJECT ^

(#2.03) USER (PSAS) \[3P\] ^ (#2.04) ACTION DATE \[4D\] ^

# Chapter 3: Flow Charts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## ROES 3.0 Patient Order from CPRS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This ROES 3.0 access point (ROES3.EXE) is used when performing functions that are primarily patient-specific. In accordance with Standard Operating Procedure (SOP) 192-507, the patient identifier obtained from the Master Patient Index (MPI-V*ist*A) is included in information passed to the DALC ROES Web ordering system.

![](roes-version-3-technical-manual/007.png)

## Get Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram describes the tasks performed by the 'Get Patient Information' function on the previous page.

> ![](roes-version-3-technical-manual/008.png)*ROES 3.0 Get Patient Information Flowchart*

## Eligibility Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagrams describe the algorithm used within the application code to determine patient eligibility for DALC products and services. The business rules used in this eligibility determination were

developed in accordance with the national ASPS Program Office and VA policy and regulations.

![](roes-version-3-technical-manual/009.png)

![](roes-version-3-technical-manual/010.png)

## Desktop Station Order Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram describes the flow of functions performed when the ROES stand-alone (non-CPRS) desktop application is invoked.

> ![](roes-version-3-technical-manual/011.png)

> *ROES 3.0 Desktop Station Order Flowchart*

# Chapter 4: Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|              |                                                                                              |
|--------------|----------------------------------------------------------------------------------------------|
| ROUTINE  | DESCRIPTION                                                                              |
| RMPFRPC0 | Called from RMPFRPC1 to collect information and calculate eligibility and return to Windows. |
| RMPFRPC1 | Used by RPC RMPFDEMOG to collect patient demographic information and return to the Windows.  |

Upon selection of the ROES 3.0 option from the CPRS Tools menu, an RPC Broker lookup is done to retrieve the patient DFN. A call is then made through the RMPFDEMOG RPC. From the PATIENT file, the name, SSN, date of birth, current address, and temporary address parameters are retrieved. The routine RMPFRPC0 is then called for added eligibility calculation information.

## Delphi Routine list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                        |                                                                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ROUTINE            | DESCRIPTION                                                                                                                                |
| ROES3.exe          | Main application for patient orders.                                                                                                           |
| fRMPFR3Main.pas    | Main Pascal program for ROES3.exe that drives the collection of user and patient information and connects to the ROES3 Patient Order web site. |
| fRMPFR3Main.dfm    | Invisible Main form for the application.                                                                                                       |
| uRMPFR3Patient.pas | Maintains Patient information.                                                                                                                 |
| Roes3DeskTop.exe   | Main station order routine to be run from the desktop.                                                                                         |
| fRMPFDesktop.pas   | Main Pascal program for the desktop application for station orders, supervisor options and reports.                                            |
| fRMPFDeskTop.dfm   | Invisible form used to hold the Broker component, retrieve user information and connect to the DALC Station Order web site.                    |

# Chapter 5: Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ROES 3.0 Patient Order from CPRS (GUI) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to invoke the Delphi utility that initiates access to ROES 3.0, the RMPF ROES3 option should be assigned to any individual who places ROES 3.0 orders for patient-specific items. ROES 3.0 users are typically ASPS and PSAS staff as designated by the appropriate Service Chief. A call to the executable ROES3.EXE will normally be placed on the CPRS Tools menu (*see ROES 3.0 Installation Manual*).

NAME: RMPF ROES3

MENU TEXT: ROES 3 OPTION ACCESS

TYPE: Broker (Client/Server)

PACKAGE: REMOTE ORDER/ENTRY SYSTEM

DESCRIPTION: This is the option that allows users to access the Delphi executable that connects the user to the DALC Website from the desktop or CPRS Tools menu.

RPC: RMPFDEMOG

RPC: DDR GETS ENTRY DATA

RPC: DDR LISTER

RPC: DDR FINDER

RPC: DDR KEY VALIDATOR

RPC: DDR GET DD HELP

RPC: DDR VALIDATOR

RPC: XUS AV CODE

RPC: XUS SIGNON SETUP

RPC: XUS AV HELP

RPC: XUS GET USER INFO

RPC: XWB CREATE CONTEXT

RPC: XWB GET VARIABLE VALUE

## Station Orders from the Desktop (GUI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As described earlier, a desktop (non-CPRS) application is also available for initiating certain types of orders through ROES 3.0. In order to run this application, the user must also have the RMPF ROES3 option assigned to his/her menu tree for the context to be created. The executable is Roes3Desktop.exe and consists of Delphi routines: fRMPFDesktop.pas and an invisible form, fRMPFDesktop.dfm.

This option should be assigned to ASPS and PSAS staff who place non-patient specific ROES station orders. This may or may not be the same staff who use the CPRS option, as determined by the appropriate Service Chief. Prior to installation, the DALC establishes one or more persons at each facility to have 'Supervisory' access to ROES 3.0. These designated supervisors use a module within the desktop web application to indicate order entry/approval privileges for each member of their staff. See the *ROES 3.0 Installation Manual* for more detailed instructions.

## ## Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-specific archiving or purging procedures or recommendations for the ROES 3.0 package. All product and order detail information is stored and maintained on the DALC system. The only locally-stored information is that related to [patient eligibility determination](#eligibility-determination), which is stored in the VistA ROES ELIGIBILITY CONFIRMATION global (#791814). With release of ROES 3.0\*4 the entries in this file will be used for reference only and no longer added to. A purge function will be issued in a future ROES 3.0 patch to remove the file.

Upon implementation and complete changeover to ROES 3.0, many of the V*ist*A routines and globals maintained on the local VAMC system under ROES 2.0 will no longer be needed. View the patch description to view those removed in patch 3.0\*4.

# Chapter 6: Entry Points & APIs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RPC NAME</strong></th>
<th><strong>PURPOSE</strong></th>
<th><strong>INPUT</strong></th>
<th><strong>OUTPUT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RMPFDEMOG</strong></td>
<td>Collection of patient demographic information</td>
<td>DFN from local PATIENT file (#2)</td>
<td><p>Subscripted array:</p>
<p>0=FM and print DOD</p>
<p>1=name text</p>
<p>2=FM and print DOB</p>
<p>4=current addr line 1</p>
<p>5=current addr line 2</p>
<p>6=current addr line 3</p>
<p>7=current city</p>
<p>8=current state</p>
<p>pointer and abbrev</p>
<p>9=current zip</p>
<p>10=FM and print temp start date</p>
<p>11= FM and print temp end date</p>
<p>12=current phone</p>
<p>13= FM and print elig status date</p>
<p>14=calc eligibility</p>
<p>15=elig status (V^Verified)</p>
<p>16=sensitive record</p>
<p>(1 or "")</p>
<p>17=error message</p>
<p>18=primary eligibility</p>
<p>19=priority group</p>
<p>20=integration control number</p></td>
</tr>
</tbody>
</table>

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 requires a standard V*ist*A operating environment, V*ist*A RPC Broker and Internet Explorer in order to function correctly. See the recommended minimums in *Orientation* section of this manual.

As described in the [Application Architecture Overview](#application-architecture-overview), the VAMC resident components interface externally with the DALC Web-based ROES 3.0 application. Once a ROES 3.0 order has been submitted and the order enters the DALC processing cycle, DALC order fulfillment systems complete the processing and payment of the order through established external interfaces, such as those with the VA Financial Management System (FMS) and with DALC contract vendors.

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 29%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ROUTINE</strong></td>
<td><strong>FILE NUMBER</strong></td>
<td><strong>AGREEMENT #</strong></td>
</tr>
<tr class="even">
<td>RMPFRPC0</td>
<td><p>2</p>
<p>38.1</p></td>
<td><p># 174</p>
<p># 767</p></td>
</tr>
<tr class="odd">
<td>RMPFRPC1</td>
<td>38.1</td>
<td># 767</td>
</tr>
</tbody>
</table>

Many supported Integration Agreements (IA’s) are addressed in the included routines. They are listed at the top of each routine. Those referenced are: 2343, 2701, 3006, 4055, 4440, 10003, 10009, 10015, 10035, 10061, 10063, 10064, 10066, 10070, 10081, 10086, 10089, 10103, 10104,.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Authority to Use ROES 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the ROES 3.0 options is controlled by menu assignment and application access (see the *ROES 3.0 Installation Manual* for details). Supervisors are designated and assigned within the DALC system (in coordination with the respective Service Chief) and determine the level of order entry/approval privileges for members of their staff. Only supervisors have access to the DALC module used for assigning these privilege levels. All users accessing the DALC Web applications must have the appropriate [security agreement](#d-request-for-access-and-verify-codes-from-dalc) signed and on file before access to the DALC Web applications will be allowed. If a user already has access for the Remote Inquiry System from ROES 2.0, they will already be in the system and can continue to use their assigned codes.

### Internal Option Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Installation Manual has detailed instruction for the setup of these options.

The VistA option RMPF ROES3 is a Broker (Client/Server) option that creates context for both of the Delphi ROES applications. It is set up during installation and must be manually assigned to users of either application.

### Remote System Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES 3.0 includes no specific restrictions or limitations on remote access to the application. However, note that ROES 3.0 can be accessed only through the Delphi executable applications integrated into the CPRS and desktop entry points. The methodology used to implement remote access must allow for adequate performance of RPC broker-based applications. If the remote access implementation is sufficient to support broker access and CPRS, then ROES 3.0 access should be adequately supported, as well.

# # Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| TERM    | DESCRIPTION                                                 |
|-------------|-----------------------------------------------------------------|
| API     | Application Programmer Interface                                |
| ASPS    | Audiology and Speech Pathology Service                          |
| DALC    | Denver Acquisition & Logistics Center                           |
| GUI     | Graphical User Interface                                        |
| HTTP    | HyperText Transfer Protocol                                     |
| HTTPS   | Hypertext Transfer Protocol over Secure Socket Layer            |
| IRM     | Information Resource Management                                 |
| PSAS    | Prosthetics and Sensory Aid Service                             |
| ROES    | Remote Order Entry System                                       |
| RPC     | Remote Procedure Call                                           |
| *VistA* | Veterans Health Information Systems and Technology Architecture |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| TERM                | DEFINITION                                                                                                                                                                                                                                      |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALERTS              | Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide notification of pending computing activities, such as the failure of a required process or of missing required data. |
| APPLICATION PACKAGE | Software and documentation that support the automation of a service. In this case, the Remote Order Entry System.                                                                                                                                   |
| KERNEL              | A set of V*ist*A software routines that function as an intermediary between the host operating system and the V*ist*A application package (in this case ROES 3.0).                                                                                  |
| LISTENER            | In ROES 3.0 this is the RPC Broker on the workstation and the server.                                                                                                                                                                               |
| NAME SPACING        | A convention for naming V*ist*A package elements, assigned by the Database Administrator (DBA). For ROES 3.0 the name spacing is RMPF.                                                                                                              |
| OPTION              | An item in the V*ist*A OPTION file (#19).                                                                                                                                                                                                           |
| ROUTINE             | Groups of program lines that are saved, loaded, and called as a single unit via a specific name.                                                                                                                                                    |
| SECURITY KEY        | A non-visual object or code that provides a layer of protection on the range of computing capabilities available with a particular software package. ROES 3.0 uses menu access for controlling access to its options.                               |
| SUBSCRIPT           | A numeric or string value that identifies a specific node within an array or global.                                                                                                                                                                |

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A: Error and Other Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message 'A problem was encountered communicating with the Server (XUS GET USER INFO could not be executed)' is shown if this remote procedure call fails.

The message '\*\*Alert\*\* Allied Agency Agreement 'must be on record at the local Institution' if the patient's eligibility is calculated to be either CAN (Canadian) or BRI (British) and Service Connected.

The message 'Cannot enter the ROES3 PATIENT web site from a Non-Production account, as this would register non-patients.' appears if the user tries to connect to ROES3Patient web site from a development or training account.

The message 'Cannot connect to ROES without a Patient Date of Birth' appears if the DATE OF BIRTH field in the PATIENT file is blank.

The message 'Cannot connect to ROES without a Patient Name' appears if the NAME field is not returned from the PATIENT file.

The message ‘Cannot connect to ROES without a Patient SSN' appears if the SSN field in the PATIENT file is blank.

The message 'Connection to Broker Server: ' + name of server + 'could not be established. Broker error: '+ text of the Broker Error encountered appears if a broker call err’s out.

The message 'Connection to Broker Server: ' + name of server + ' Failed' appears if the login to the server failed.

The message 'Connection to Broker Server could not be established' if the connection to the selected Broker port could not be completed.

The message 'Could not retrieve necessary patient information' is shown if the lookup of patient demographic information fails.

The message 'Failed to connect to Denver. ' is shown when the https connection to the DALC Website fails.

The message 'Invalid Patient Selection.' appears if the patient lookup fails in the CPRS tools option.

The message ‘The application was unable to identify the internal patient number. This can often be resolved by simply returning to the CPRS Toolbar and selecting the ROES option again. If this message consistently reappears, contact your local IRM Service to verify that the command string for this option is configured correctly in CPRS.

The message 'User Authorization could not be established' is shown if the XUS GET USER INFO remote procedure call (RPC) returns a nil.

The message 'You do not have access to this option (context failed)' or 'You are not authorized to use this option' is shown if the user does not have the necessary option RMPF ROES3 assigned to his menu tree.

## ## B: Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  RMPF ROES UPDATES (ASPS) receives messages (VA MailMan) Receives various ROES messages and updates.
2.  RMPF ROES UPDATES (PSAS) receives messages (VA MailMan) Receives various ROES messages and updates.

These mail groups are set up during the installation, if it was not set up during a prior ROES 3.0 install. At that time a coordinator was selected for each group and they would add the necessary individuals to their group. See the *ROES 3.0 Installation Manual* for further instructions.

## C: Section 508 Compliance Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application has been evaluated and approved for compliance with Section 508 of the Rehabilitation Act Amendments of 1998.

## ## D: Request for Access and Verify Codes from DALC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <span class="mark">REDACTED</span> Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

calc eligibility 24

eligibility 21

calculated 29

calculation 21

determination 8, 18

detrmination process 15

for DALC services 13

patient 18, 21

requests 15

fRMPFDesktop.pas 21, 22

fRMPFR3Main.dfm 21

fRMPFR3Main.pas 21

Master Patient Index (MPI-V*ist*A) 16

patient eligibility determination 23

primary eligibility 24

RMPF ROES3 26

RMPF ROES3 option 22

RMPFDEMOG 21, 22, 24

RMPFRPC0 21, 25

RMPFRPC1 21, 25

ROES3.exe 21

Roes3DeskTop.exe 21

Standard Operating Procedure (SOP) 192-507 16

#