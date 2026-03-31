---
consolidated_title: "mental health assistant deployment, installation, back-out & roll back guide"
app_code: YS
doc_type: DIBR
master_source: "YS*5.01*179 Mental Health Assistant Deployment, Installation, Back-Out & Roll Back Guide"
master_pub_date: June 2021
consolidated_from: 2 versions
prior_versions:
  - "YS*5.01*178 Mental Health Assistant Deployment, Installation, Back-Out & Roll Back Guide"
---

---
title: |
  Mental Health YS\*5.01\*179

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](ys-5-01-179-mental-health-assistant-deployment-installation-back-out-roll-back-g/001.png)

June 2021

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| 06/23/2021 | 1.0         | Initial Version | Liberty IT Solutions |

<span id="_Toc72322916" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

List of Tables

[Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [2](#_Toc72322916)](#_Toc72322916)

[Table 2: Acronyms [8](#_Toc72322917)](#_Toc72322917)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics (optional)](#facility-specifics-optional)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [User Configuration](#user-configuration)
    - [Add the necessary SECURITY KEYs](#add-the-necessary-security-keys)
  - [Configure MHA Web on the CPRS Tools Menu](#configure-mha-web-on-the-cprs-tools-menu)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A – Acronyms](#appendix-a-acronyms)
This document describes how to deploy and install the patch YS\*5.01\*179 of the Mental Health package, as well as how to back-out the product and rollback to a previous version or data set.
This document is a companion to the project charter and management plan for this effort in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*179 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system. Patch YS\*5.01\*158 must be installed.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*179. This is a web application only patch and will only require a Post-Install step once the web application has been deployed by the Azure application team.

| Team                                     | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|----------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Project Manager                              | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | Design                           |
| Software Quality Assurance (SQA), Test Sites | Deployment       | Test for operational readiness                                                                                      | Test                             |
| Project Manager, Release Manager             | Deployment       | Execute deployment                                                                                                  | Release                          |
| Individual VistA Sites                       | Installation     | Plan and schedule installation                                                                                      | Release                          |
| Azure Manager                                | Installation     | Plan and schedule installation                                                                                      | Release                          |
| Release Manager                              | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Release                          |
| Sustainment Team                             | Post Deployment  | Hardware, Software and System Support                                                                               | Sustain                          |

<span id="_Toc72322917" class="anchor"></span>Table 2: Acronyms

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*179 will be available for installation and deployment at all sites.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run during June 2021.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the YS\*5.01\*179 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*179 will be deployed to the Azure application server. Local sites as well as regional data centers will only need to execute the Post-Installation steps in order to access the web application.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The verification of this functionality was performed in User Acceptance Testing (UAT). Once UAT testing was completed, approval for national release was given for YS\*5.0\*179 which will be deployed to all VistA systems.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*179 requires a fully patched VistA system. In particular, YS\*5.01\*158 (MHA Planning and Staff Entry) should be installed prior to the installation of YS\*5.01\*179.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No specific facility resources needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No hardware resources needed.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No software resources needed.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When YS\*5.01\*179 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package as an Informational patch.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no pre-installation requirements.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no VistA installation required.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no VistA installation required and no specific skills needed.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The users must have the following Secondary Menu assigned:

- YS BROKER1

### Add the necessary SECURITY KEYs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new Security Keys required.

## Configure MHA Web on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure configures VistA so that “MHA Web” appears as a choice on a user’s Tools menu on the CPRS desktop software. MHA Web must be started from the CPRS Tools Menu.

Go to the GUI TOOL Menu, Select 4 for System. At the Select Sequence prompt, enter the sequence number to assign for MHA Web. The Name=Command is

MHA Web=https://\<server\>/app/home?station=\<station number\>&poi=%DFN

You need to substitute the \<server\> with the MHA Web server name “mha.med.va.gov” and the \<station number\> with your VistA instance station number.

Example: The example below shows the set up of MHA Web on the CPRS Tools menu from the GUI TOOLS MENU \[ORW TOOL MENU ITEMS\] option:

\<CPM\> Select OE/RR MASTER MENU \<NGOLD\> Option: ^GUI TOOL Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[LYNCHBURG (CLL)\]

4 System SYS \[NGOLD.DEVSLC.FO-SLC.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 4 System NGOLD.DEVSLC.FO-SLC.MED.VA.GOV

-- Setting CPRS GUI Tools Menu for System: NGOLD.DEVSLC.FO-SLC.MED.VA.GOV --

Select Sequence: 5

Are you adding 5 as a new Sequence? Yes// \<enter\> YES

Sequence: 5// \<enter\> 5

Name=Command:MHA Web=https://mha.med.va.gov/app/home?station=999&poi=%DFN

Select Sequence: \<enter\>

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning required.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the Mental Health Application – Web (MHA Web) application. If MHA Web does not perform as desired, it is possible to back out to the previous implementation.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*179 patch is backed out, there will be minimal impact to users other than MHA Web will no longer be available to non-Cerner users.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA Web no longer functions, or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the MHA Web will be unavailable.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*179 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to back out the CPRS Tools menu option, go to the GUI Tools Menu option

> Select 4 System

> Select the Sequence number for the MHA Web option.

> Enter @ at the Sequence number prompt to delete it from the list.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the back-out procedure, run CPRS, select a patient, and click on the Tools option. Verify that MHA Web no longer exists in the list.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*179 is an Azure web application update only. This patch will utilize existing application data.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback criteria.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback risks.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback authority needed.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback procedure.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback verification.

# Appendix A – Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                 |
|-------------|----------------------------------------------------------------|
| CAG         | Citrix Access Gateway                                          |
| DIBRG       | Deployment, Installation, Back-out, and Rollback Guide         |
| IOC         | Initial Operating Capability                                   |
| KIDS        | Kernel Installation and Distribution System                    |
| MHA         | Mental Health Assistant                                        |
| PIN         | Personal Identification Number                                 |
| PIV         | Personal Identity Verification                                 |
| SPP         | Suicide Prevention Package                                     |
| SQA         | Software Quality Assurance                                     |
| SSOi        | Single Sign-On Integration                                     |
| VA          | Department of Veterans Affairs                                 |
| VAMC        | Veterans Affairs Medical Center                                |
| VIP         | Veteran-focused Integration Process                            |
| VistA       | Veterans Health Information System and Technology Architecture |