---
title: Ask A Pharmacist Technical Guide (Mobile Applications Phase 2)
doc_type: TG
doc_label: Technical Guide
doc_layer: plain
doc_subject: Ask A Pharmacist  (Mobile Applications Phase 2)
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - contents
  - table
  - application
  - apache
  - server
  - mobile
  - installing
  - html
  - procedures
  - pharmacist
page_count: 0
word_count: 1221
section_count: 10
table_count: 1
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2016
revision_count: 1
revision_newest: 4/4/2016
revision_oldest: 4/4/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/aap_technical_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/aap_technical_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

---
title: <span id="_Toc205632711" class="anchor"></span>Department of Veterans Affairs
---

Mobile Applications (Apps) Phase Two (MAP2)

Ask A Pharmacist – Technical Guide

![](ask-a-pharmacist-technical-guide-mobile-applications-phase-2/001.png)

Software Version 1.0

April 2016

Revision History

| Date     | Revision | Description                               | Author |
|----------|----------|-------------------------------------------|--------|
| 4/4/2016 | 1.0      | Created from wiki template for use on VDL |        |

Revision HistoryRevision History

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Installation Prerequisites](#installation-prerequisites)
  - [Software](#software)
  - [Hardware](#hardware)
- [Installation Instructions](#installation-instructions)
  - [Installing GIT](#installing-git)
  - [Installing Node](#installing-node)
  - [Building HTML5 Application](#building-html5-application)
  - [Deploying Application to Apache Static Server](#deploying-application-to-apache-static-server)
  - [LaunchPad SQL](#launchpad-sql)
  - [Apache Proxy Configuration](#apache-proxy-configuration)
- [Deployment to Apache Web Server](#deployment-to-apache-web-server)
- [Rollback Procedure](#rollback-procedure)
- [Un-install](#un-install)
- [Pre-release Testing](#pre-release-testing)
- [User and Group Account](#user-and-group-account)
- [System Back-up](#system-back-up)
- [Application Maintenance Procedures](#application-maintenance-procedures)
Veterans Health Administration (VHA), Patient Care Services (PCS), Pharmacy Benefits Management (PBM) has requested an Ask A Pharmacist (AAP) mobile application that will expand patient care services by providing trusted medication resources and answers to frequently asked medication questions developed by Department of Veterans Affairs (VA) pharmacists to VA patients and their caregivers. AAP will provide a link to Secure Messaging (SM) resources on My Health*e*Vet (MHV) so that patients and/or caregivers can learn how to submit specific questions directly related to their local VHA pharmacy. AAP will also link to medication functionality within MHV. AAP will consist of a landing page containing links to various internal and external medication resources and information (e.g., trusted sources of information, other VA Medical Centers \[VAMC\]), as well as Frequently Asked Questions (FAQs). 
Additionally, it is envisioned that once Veterans and/or caregivers become “In-Person Authenticated” (IPA), they can submit specific questions for a prompt, personal response through SM. Providing an additional route of communication will ultimately lead to streamlining the pharmacy workflow and increase patient satisfaction. 
AAP will allow users access to vetted information in an easy-to-use format without the users having to worry about locating valid information on their own via the Internet and/or potentially untrusted sources. AAP will also allow front line triage staff to handle the majority of AAP submitted questions via SM.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this AAP Technical Guide is to provide system implementers and developers with a technical overview of the AAP application. The guide will provide detail on the installation, removal, access control mechanisms, and system administration details for the AAP application.

# Installation Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AAP application requires an Apache Web Server and common VAMF Shared Services.

 ![](ask-a-pharmacist-technical-guide-mobile-applications-phase-2/002.png)

Figure 1: AAP Deployment Diagram

Note that hardware and software configurations are dependent upon the load and suspected usage of the application and may need to be upgraded to match the environment in which they will run.

## Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the AAP System Design Document (SDD) for information on Technologies, Libraries, and Tools Used in the App. The AAP SDD can be viewed in the AAP wiki.

## Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hardware specifications are specific to loads within the VA Mobile Framework (VAMF). Sizing can be based off of systems being deployed and shared in the dev-int environment.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current version is Version 1.0, and the build is AAP09162015.

## Installing GIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instructions for installing GIT are located on the VA Mobile Health wiki.

## Installing Node

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instructions for installing Node are located on the VA Mobile Health wiki.

## Building HTML5 Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instructions for building the HTML5 application are located on the VA mobile health wiki.

## Deploying Application to Apache Static Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This should be deployed to /var/www/html

Set the permissions for the directory:

Deploy Application

chown -R apache:apache aap

## LaunchPad SQL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Insert Chicklet

insert into hadb.launchpad_item (NAME, ITEM_MODE, TYPE, ITEM_POSITION, DESCRIPTION, URL, IMAGE_URL)

values

('Ask a Pharmacist',

'VETERAN',

'APP',

100,

'Veteran access to resources and secure messaging about health and medications',

'/aap',

'../aap/img/app_chicklet.png');

commit;

Remove Chicklet

DELETE FROM hadb.launchpad_item where NAME = 'Ask a Pharmacist';

commit;

## Apache Proxy Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If using an Apache Proxy in front of the webserver, the following configuration must be placed on the Proxy server:

/etc/httpd/conf.d/aap.conf

\<Location /aap\>

ProxyPass http://\<Apache Static IP\>/aap

ProxyPassReverse http://\<Apache Static IP\>/aap

\</Location\>

# Deployment to Apache Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After building the HTML5 Web Application, extract the contents of the .WAR file under the \_build directory or from Jenkins onto the Apache Web Server root under the folder aap (ignoring the WEB-INF folder only needed for deployment to a J2EE server).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application follows the standard operating procedures for applications installed in the MAE/VAMF, currently operated by the PAMS support team. Rollback of services (since these are hosted on WebLogic) are typically an 'undeploy' of the existing application version within the WebLogic Administrator Console followed by re-deploy of the previous released version. The HTML5 web application is similar, where all contents of the web applications root directory on the Apache Web Server www directory are replaced with files from the previously released version.

# Un-install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow any required data retention policies as suggested by VA. To uninstall the AAP Web Application (HTML5), simply remove the folder containing the application from the Apache Web Server www directory. To remove the AAP Service and Medication Image Library Service, simply undeploy the WAR file from the WebLogic container. Lastly, remove any reverse proxy routes from the Apache Proxy Server that point to the AAP application, AAP Service, and Medication Image Library Service.

# Pre-release Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ask A Pharmacist Master Test Plan (AAP MTP) contains details related to AAP test procedures. The AAP MTP can be viewed at AAP wiki.

# User and Group Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans can access this application without login; no further account or group procedures are needed. System (hosting systems and associate eCRUD/Mongo system) account management is performed in accordance with existing MAE/VAMF procedures.

# System Back-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This application and supporting services is hosted in VA's MAE/VAMF Dedicated Core environment; ongoing system backups are provided as part of the Terremark hosting facility agreement.

# Application Maintenance Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application maintenance is governed by the MAE Change Control Procedures, which include the processes used for both non-production and production environments.