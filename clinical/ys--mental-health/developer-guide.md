---
title: Veteran's Crisis Line Version 1 Developer Guide
doc_type: DG
doc_label: Developer Guide
doc_layer: anchor
doc_subject: 
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 1
patch_id: YS*1
group_key: "YS:YS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - developer
  - guide
  - crisis
  - version
  - line
  - application
  - veteran
  - code
page_count: 0
word_count: 2106
section_count: 9
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 1
revision_newest: 11/14/2014
revision_oldest: 11/14/2014
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_developer_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_developer_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: |

  Department of Veterans Affairs
---

Enhancements to the Veterans Crisis Line Application (VCL)

Developer Guide

![](veteran-s-crisis-line-version-1-developer-guide/001.png)

November 2014

Revision History

|            |         |                 |                                    |
|------------|---------|-----------------|------------------------------------|
| Date       | Version | Description     | Author                             |
| 11/14/2014 | 1.0     | Initial version | <span class="mark">REDACTED</span> |
|            |         |                 |                                    |
|            |         |                 |                                    |

Table of Contents

List of Tables

No table of figures entries found.

List of Figures

No table of figures entries found.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose of the Developer Guide](#purpose-of-the-developer-guide)
  - [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
- [Background](#background)
  - [Overview of the System](#overview-of-the-system)
- [Required Software Components](#required-software-components)
  - [Obtaining Required Software Components](#obtaining-required-software-components)
  - [Installing Required Software Components](#installing-required-software-components)
- [Obtaining VCL Code from RTC](#obtaining-vcl-code-from-rtc)
- [Overview of the VCL Solution](#overview-of-the-vcl-solution)
- [Running VCL on a GFE](#running-vcl-on-a-gfe)
  - [Running Hotline](#running-hotline)
  - [Running Admin](#running-admin)
  - [Running Response](#running-response)
- [Troubleshooting / Additional Information](#troubleshooting-additional-information)
The Office of Mental Health Services (OMHS) is currently managing a web-based application called the Veterans Crisis Line (VCL) utilized by their confidential, free, 24-hour hotline staff to make referrals to the appropriate field-based Suicide Prevention Coordinators (SPCs).
OMHS is requesting the Office of Information & Technology (OIT) assist OMHS to enhance, deploy and support the existing VCL application and hardware platform utilizing Information Technology (IT) best practices and procedures rather than maintaining the existing reporting environment.
Goals include remediating coding issues within the application that are preventing standardized reporting and the replacement of the underlying hardware.

## Purpose of the Developer Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Developer Guide (DG) is to provide new and current developers with the information needed to set up an environment to develop enhancements or fix issues with the VCL code.

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term       | Definition                                                      |
|------------|-----------------------------------------------------------------|
| AITC       | Austin Information Technology Center                            |
| ANR        | Automated Notification Reporting                                |
| AERB       | Architecture and Engineering Review Board                       |
| API        | Application Programming Interface                               |
| BRD        | Business Requirements Document                                  |
| CPRS       | Computerized Patient Record System                              |
| DR         | Disaster Recovery                                               |
| ESS        | Enterprise Support Solution                                     |
| FIPS       | Federal Information Processing Standard                         |
| GFE        | Government Furnished Equipment                                  |
| GUI        | Graphical User Interface                                        |
| HIPAA      | Health Insurance Portability and Accountability Act             |
| IIS        | Internet Information Services                                   |
| ISO        | Information Security Officers                                   |
| IT         | Information Technology                                          |
| MDO        | Medical Domain Objects                                          |
| MDWS       | Medical Domain Web Services                                     |
| MHS        | Mental Health Services                                          |
| MOU        | Memorandum of Understanding                                     |
| .NET       | The Microsoft .NET Framework                                    |
| NIST       | National Institute of Standard and Technology                   |
| NSR        | New Service Request                                             |
| O&M        | Operations & Maintenance                                        |
| OEF/OIF    | Operation Enduring Freedom/Operation Iraqi Freedom              |
| OHI        | VHA Office of Health Information                                |
| OIT        | Office of Information & Technology                              |
| OMB        | Office of Management and Budget                                 |
| OMHS       | Office of Mental Health Services                                |
| PD         | Product Development                                             |
| PMAS       | Program Management Accountability System                        |
| PMP        | Program Management Plan                                         |
| RPC        | Remote Procedure Call                                           |
| RSD        | Requirements Specification Document                             |
| SDD        | System Design Document                                          |
| SDV        | Self-Directed Violence                                          |
| SLA        | Service Level Agreement                                         |
| SOA        | Service-Oriented Architecture                                   |
| SOAP       | Simple Object Access Protocol                                   |
| SOP        | Standard Operating Procedures                                   |
| SPC        | Suicide Prevention Coordinator                                  |
| SPCE       | Suicide Prevention Center of Excellence                         |
| SQL        | Structured Query Language                                       |
| SQL Server | Microsoft SQL Server Database                                   |
| SSRS       | SQL Server Reporting Service                                    |
| TRM        | Technical Reference Model                                       |
| TSPR       | Technical Services Project Repository                           |
| UI         | User Interface                                                  |
| VA         | The Department of Veterans Affairs                              |
| VAE        | VistA Applications Enhancement                                  |
| VAMC       | VA Medical Center                                               |
| VCL        | Veterans Crisis Line                                            |
| Vet        | Veteran                                                         |
| VHA        | Veterans Health Administration                                  |
| VISN       | Veterans Integrated Service Network                             |
| VistA      | Veterans Health Information Systems and Technology Architecture |
| VSC        | Veterans Service Center                                         |
| WT         | Warm Transfer                                                   |
| WWI        | World War I                                                     |
| WWII       | World War II                                                    |

# Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health Services (MHS) currently manages a web-based application (herein referred to as the VCL Application) utilized by its confidential, free, 24-hour hotline staff to make referrals to appropriate field-based SPCs.

MHS requests that OIT assist MHS as it enhances, deploys, and supports the existing VCL application. In addition, MHS requests assistance with the hardware platform in utilizing IT best practices and procedures rather than maintaining the existing enhanced reporting environment.

## Overview of the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHS currently manages the VCL, a free, 24-hour, confidential hotline that veterans can access when experiencing emotional crises. VCL staff use a web-based application to make referrals from the national hotline to the appropriate field-based SPCs. Currently, the application form that VCL staff use does not electronically integrate standard, industry-wide nomenclature needed to properly classify self-directed violence. Instead, staff must record levels of self-directed violence classifications manually into the free-text comments field of the web-based form.

Unfortunately, nomenclature used in this free-text field cannot be extracted as discrete data elements. As a result, the SPCE, which gathers data from the VCL Application, does not have the ability to properly report on self-directed violence in a manner that is consistent with industry nomenclature and standards. This leads to an inability of the VA to share and compare its information with other suicide prevention centers.

MHS will establish and present the standardized nomenclature on the web-based application form in a way that allows the SPCE to extract the information as useable and reportable data, develop a tool that the SPCE and MHS can use to pull reports on this data, and solidify ongoing support and maintenance of the VCL Application.

The VCL application was developed to make referrals from the national hotline to the appropriate field-based SPCs. Up to this point in time, enhancements and changes to the VCL application have been unofficially completed during a staff member’s free time. MHS recognizes the need for permanent, dedicated support for the management of this important application. In order to effectively support veterans in crisis, it is necessary that MHS implement a long-term application management solution with dedicated resources for enhancements, ongoing maintenance and management of this application.

# Required Software Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tools will be needed to obtain and work on VCL code. If you are unsure how to obtain these tools, please contact the National Service Helpdesk.

## Obtaining Required Software Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Visual Studio 2010 Ultimate with SP1 installed.

> ![](veteran-s-crisis-line-version-1-developer-guide/002.png)

- IBM Installation Manager 1.7.2, which is used to install the RTC plug-in for Visual Studio.

> ![](veteran-s-crisis-line-version-1-developer-guide/003.png)

- The RTC (Rational Team Concert) plug-in for Visual Studio 2010 Ultimate, version 3.0.1. The last known location to download the plug-in is \\vhaishmul35.vha.med.va.gov\RationalReleaseArea\TeamConcert get the zip file: RTC-VisualStudio-Client-repo-3.0.1
- The Microsoft Anti-Cross Site Scripting Library V4.2, available for download at <http://www.microsoft.com/en-us/download/details.aspx?id=28589>

## Installing Required Software Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Visual Studio 2010 Ultimate

Follow the instructions detailed by Microsoft to install this component. Select C# as the language to be used when prompted.

IBM Installation Manager

Follow the instructions detailed by IBM to install this component.

RTC plug-in for Visual Studio 2010 Ultimate

Once VS is installed on your machine, make sure it is closed, and go get the RTC plug-in for MS VS from the RationalReleaseArea in Hines: <span class="mark">REDACTED</span>. Get the zip file: RTC-VisualStudio-Client-repo-3.0.1 and unzip it to a location on your machine.

Open up Installation manager, and beneath the “File” menu select “Preferences”

![](veteran-s-crisis-line-version-1-developer-guide/004.png)

Select “Add Repository…”

![](veteran-s-crisis-line-version-1-developer-guide/005.png)

Navigate to the file named “repository.config” in the unzipped directory.  You should find it in: …\RTC-VisualStudio-Client-repo-3.0.1\im\repo\rtc-vsclient-

offering\offering-repo..

![](veteran-s-crisis-line-version-1-developer-guide/006.png)

Select it and choose “Open”, then “OK”, then “Apply”, and finally “OK” again.  Once added to the list of Installation Managers Repositories.  Choose the “Install” in Installation Manager:

![](veteran-s-crisis-line-version-1-developer-guide/007.png)

Check the box for “Rational Team Concert – client for Microsoft Visual Studio IDE” and then “next”

![](veteran-s-crisis-line-version-1-developer-guide/008.png)

Move thru and use the default selection to install the software.  It will find Visual Studio and install the plug-in.  You can now open VS and you should see the “Team Concert” menu:

![](veteran-s-crisis-line-version-1-developer-guide/009.png)

Microsoft Anti-Cross Site Scripting Library V4.2

Run the executable you downloaded and follow the default prompts. If prompted for a .NET version of the assemblies to install, select .NET 3.5.

# Obtaining VCL Code from RTC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you have installed all the required components, you will be ready to open Visual Studio 2010 Ultimate and obtain the latest VCL code from the RTC code repository.

You will need to verify that your account is set up for RTC access in the MHLTH (CM) repository.

In Visual Studio, Go to Team Concert -\> Windows -\> Team Artifacts

![](veteran-s-crisis-line-version-1-developer-guide/010.png)

In the Team Artifacts window, right click Repository Connections, and select New -\> Jazz Repository Connection

![](veteran-s-crisis-line-version-1-developer-guide/011.png)

Fill in the requested fields with information shown in the following graphic. You will need to enter your own User ID and Password. Click OK when finished.

![](veteran-s-crisis-line-version-1-developer-guide/012.png)

Next you will need to set up a sandbox for the code from RTC to reside on your machine. In the Team Artifacts window, right-click Sandboxes and select New Sandbox.

![](veteran-s-crisis-line-version-1-developer-guide/013.png)

In the New Sandbox window, type in the location you’d like the code to be placed, and click OK.

![](veteran-s-crisis-line-version-1-developer-guide/014.png)

At this point you should be able to obtain the VCL code.

# Overview of the VCL Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From Visual Studio, navigate to the Solution Explorer.

![](veteran-s-crisis-line-version-1-developer-guide/015.png)

The MasterSolution contains all the projects necessary to compile and run the VCL applications.

All of the \*.Web projects contain the web application code. They are the presentation layer projects.

The CrisisCenter.Data project is the data layer project, and contains code that interfaces between the presentation layer and the database.

The CrisisCenter.WebServices project is the web service layer, and contains the code that is responsible for interfacing with MDWS, which in turn interfaces with VistA to obtain patient data.

The CrisisCenter.Managers project contains legacy code that interfaces between the presentation layer and the web service layer.

The CrisisCenter.Service project contains common functionality among all the projects. It also serves as a business logic layer.

# Running VCL on a GFE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run VCL on a GFE, you will need to select one of the .Web projects as the startup project in Visual Studio. Begin running the project in debug mode to begin executing the application – Visual Studio will use its internal web server to host the application.

All three VCL applications (Hotline, Admin, and Response) have a warning banner that you must acknowledge before proceeding. This is to satisfy VA 6500 requirements.

All three VCL applications must also be logged in to before using them. The following information is what you will need in order to log in:

VISN: VISN1 – CPM VISN

Site: Dev

Access Code: 1programmer

Verify Code: programmer1

## Running Hotline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hotline will load with a screen similar to this.

![](veteran-s-crisis-line-version-1-developer-guide/016.png)

After you log in, you will be able to log a call, or click the Reports Menu to select from a list of reports to execute.

## Running Admin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Admin will load with a screen similar to this. Select a user type will change the types of selections and permissions you will have after logging in. Super Admin has the highest level of access, while CR has the lowest.

![](veteran-s-crisis-line-version-1-developer-guide/017.png)

After logging in you are presented with a menu of options, depending on your level of access.

![](veteran-s-crisis-line-version-1-developer-guide/018.png)

From here you can enter calls, run a series of call listing functions, or run reports. Keep in mind that the Custom Reports link opens a new tab/window to SQL Server Reporting Services (SSRS), which is what certain high-level VCL users use to create and run their own reports.

## Running Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Response will load with a screen similar to this. You will need to log in before accessing its functionality.

![](veteran-s-crisis-line-version-1-developer-guide/019.png)

After logging in you are presented with a screen similar to this.

![](veteran-s-crisis-line-version-1-developer-guide/020.png)

From this point you can view a series of call lists, select a call to view its details, or click Find Past Referrals to show a page that has call searching capabilities.

# Troubleshooting / Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If you are missing a reference to the Microsoft anti-XSS assemblies, you will have to manually add them to the projects that need them (i.e., the \*.Web projects). Assuming you have installed it, the assemblies can be found in a location such as C:\Program Files (x86)\Microsoft Information Security\AntiXSS Library v4.2\NET35\AntiXSSLibrary.dll.
- Developers and testers are bound to use a development instance of MDWS since any instance of MDWS that points to production VistAs will contain private patient information. The development instance of MDWS that VCL has been using is part of VA Innovations, and the URL to the MDWS web service is <span class="mark">REDACTED</span>. There is no one available to contact at VA Innovations, so if anything happens to this development instance of MDWS, an alternative will need to be found.
- The version number you see on the warning banner is stored in AssemblyInfo.cs files of each of the three VCL applications.
- In the event that a Fortify scan is requested, you will need to get in touch with the Fortify team to obtain a license and the latest Fortify software.