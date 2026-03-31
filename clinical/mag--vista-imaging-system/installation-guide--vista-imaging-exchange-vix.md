---
consolidated_title: "vista imaging exchange (vix) installation guide"
app_code: MAG
doc_type: IG
master_source: "VistA Imaging Exchange (VIX) Installation Guide"
master_pub_date: January 2025
consolidated_from: 5 versions
prior_versions:
  - "MAG*3*269 VistA Imaging Exchange (VIX) Installation Guide"
  - "MAG*3*303 VistA Imaging Exchange (VIX) Installation Guide"
  - "MAG*3*329 VistA Imaging Exchange (VIX) Installation Guide"
  - "MAG*3*348 VistA Imaging Exchange (VIX) Installation Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Imaging eXchange (VIX) Enhancements and Maintenance

  MAG\*3.0\*<span id="PatchNumber" class="anchor"></span>358

  VIX Installation Guide
---

![](vista-imaging-exchange-vix-installation-guide/001.png)

January 2025

Department of Veterans Affairs (VA)

Office of Information Technology (OIT)

# Property of the US Government


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Property of the US Government](#property-of-the-us-government)
- [Introduction](#introduction)
  - [Intended Audience](#intended-audience)
  - [Document Conventions](#document-conventions)
  - [Terms of Use](#terms-of-use)
  - [Related Information](#related-information)
- [Installing a New VIX](#installing-a-new-vix)
  - [Preparing for a New VIX Installation](#preparing-for-a-new-vix-installation)
    - [Selecting and Validating the VIX Server](#selecting-and-validating-the-vix-server)
    - [Getting VIX Component Licenses](#getting-vix-component-licenses)
    - [VIX Security Certificate](#vix-security-certificate)
    - [Java Version Verification](#java-version-verification)
    - [LibreOffice Verification](#libreoffice-verification)
    - [PowerShell 7 Verification](#powershell-7-verification)
  - [New VIX Server Installation](#new-vix-server-installation)
  - [Preparing Passwords, Activating Components, and Staging Files](#preparing-passwords-activating-components-and-staging-files)
    - [VIX Server Installation](#vix-server-installation)
  - [Activating a New VIX](#activating-a-new-vix)
    - [To Register the VIX](#to-register-the-vix)
- [Updating an Existing VIX](#updating-an-existing-vix)
  - [Preparing for a VIX Update](#preparing-for-a-vix-update)
    - [Scheduling Downtime and Impact of a VIX Update](#scheduling-downtime-and-impact-of-a-vix-update)
  - [Preparing Service Account and Passwords](#preparing-service-account-and-passwords)
  - [Performing a VIX Server Update](#performing-a-vix-server-update)
- [Post-Installation for New VIX Installations and Updating Existing VIX Installations](#post-installation-for-new-vix-installations-and-updating-existing-vix-installations)
  - [Apply Security Update](#apply-security-update)
  - [Verifying Installation/Upgrade is Complete](#verifying-installationupgrade-is-complete)
  - [Verifying VIX Operations](#verifying-vix-operations)
    - [Verifying Access to the VIX Tools and VIX Transaction Log](#verifying-access-to-the-vix-tools-and-vix-transaction-log)
    - [Spot-Checking VIX Image Delivery](#spot-checking-vix-image-delivery)
  - [DICOM SCP Configuration](#dicom-scp-configuration)
- [Troubleshooting](#troubleshooting)
  - [Resuming an Interrupted VIX Installation](#resuming-an-interrupted-vix-installation)
    - [Resuming Installation (single server VIX)](#resuming-installation-single-server-vix)
  - [Using the VIX Service Installation Wizard to Reconfigure the VIX](#using-the-vix-service-installation-wizard-to-reconfigure-the-vix)
    - [Reconfiguring a VIX Server](#reconfiguring-a-vix-server)
  - [Tomcat User Permissions](#tomcat-user-permissions)
  - [Java Management Extensions (JMX)](#java-management-extensions-jmx)
  - [VIX Support](#vix-support)
- [Back Out/Uninstall](#back-outuninstall)
  - [Stopping the VIX Services](#stopping-the-vix-services)
  - [Back Out/Uninstall Scenarios](#back-outuninstall-scenarios)
    - [Uninstall/Restore as part of Troubleshooting](#uninstallrestore-as-part-of-troubleshooting)
    - [Relocating a VIX onto a New Server](#relocating-a-vix-onto-a-new-server)
    - [Decommissioning a VIX](#decommissioning-a-vix)
  - [Uninstalling the VIX](#uninstalling-the-vix)
    - [Remove VIX related applications, accounts, directories, and variables](#remove-vix-related-applications-accounts-directories-and-variables)
  - [Rollback and Back Out of MAG\3.0\358](#rollback-and-back-out-of-mag30358)
    - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A: Enable MUSE Functionality](#appendix-a-enable-muse-functionality)
- [Appendix B: DICOM SCP Configuration](#appendix-b-dicom-scp-configuration)
  - [Application Entity (AE) Titles Configuration](#application-entity-ae-titles-configuration)
    - [Laurel Bridge AE Titles Configuration on VIX/CVIX](#laurel-bridge-ae-titles-configuration-on-vixcvix)
    - [AE Titles Configuration on DICOM SCU](#ae-titles-configuration-on-dicom-scu)
  - [Tomcat/ Laurel Bridge DICOM SCP Configuration](#tomcat-laurel-bridge-dicom-scp-configuration)
- [Appendix C: Restart Script](#appendix-c-restart-script)
- [Appendix D: Service Account Settings](#appendix-d-service-account-settings)
- [Appendix E: VIX Install Checklist](#appendix-e-vix-install-checklist)
  - [VIX Install Checklist](#vix-install-checklist)
- [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.
While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.
Product names mentioned in this document may be trademarks or registered trademarks of their respective companies and are hereby acknowledged.
VistA Imaging Product Development  
Internet: <https://www.va.gov/health/imaging/>  
VA intranet: <span class="mark">REDACTED</span>
Revision History
| Date       | Revision | Description                                                                                                                                                                                           | Author                             |
|------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 01/17/2025 | 48.4     | Updates to Installing a New VIX, Updating an Existing VIX, and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                   | VA IT VistA Imaging Technical team |
| 12/06/2024 | 48.3     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 11/26/2024 | 48.2     | Updates to Installing a New VIX.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 11/20/2024 | 48.1     | Updates to Updating an Existing VIX and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                                          | VA IT VistA Imaging Technical team |
| 11/04/2024 | 48.0     | Initial draft for MAG\*3.0\*358.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 01/08/2024 | 47.5     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 01/02/2024 | 47.4     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 12/01/2023 | 47.3     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 11/21/2023 | 47.2     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 11/01/2023 | 47.1     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 10/01/2023 | 47.0     | Initial draft for MAG\*3.0\*348.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 05/01/2023 | 46.5     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 04/19/2023 | 46.4     | Updates to Installing a New VIX, Updating an Existing VIX, and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                   | VA IT VistA Imaging Technical team |
| 04/13/2023 | 46.3     | Updates to Installing a New VIX, Troubleshooting, and Back Out/Uninstall.                                                                                                                             | VA IT VistA Imaging Technical team |
| 04/03/2023 | 46.2     | Updates to Installing a New VIX, Updating an Existing VIX, and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                   | VA IT VistA Imaging Technical team |
| 03/23/2023 | 46.1     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 03/20/2023 | 46.0     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 03/15/2023 | 45.9     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 03/09/2023 | 45.8     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 03/03/2023 | 45.7     | Updates to Installing a New VIX, Updating an Existing VIX, and Enable MUSE Functionality Appendix.                                                                                                    | VA IT VistA Imaging Technical team |
| 02/17/2023 | 45.6     | Updates to Installing a New VIX, Updating an Existing VIX, and Enable MUSE Functionality Appendix.                                                                                                    | VA IT VistA Imaging Technical team |
| 02/13/2023 | 45.5     | Updates to Installing a New VIX and Updating an Existing VIX.                                                                                                                                         | VA IT VistA Imaging Technical team |
| 02/13/2023 | 45.4     | Updates to Installing a New VIX and VIX Install Checklist.                                                                                                                                            | VA IT VistA Imaging Technical team |
| 02/03/2023 | 45.3     | Updates to Installing a New VIX, Updating an Existing VIX, and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                   | VA IT VistA Imaging Technical team |
| 01/14/2023 | 45.2     | Updates to Updating an Existing VIX.                                                                                                                                                                  | VA IT VistA Imaging Technical team |
| 01/09/2023 | 45.1     | Fixed a typo.                                                                                                                                                                                         | VA IT VistA Imaging Technical team |
| 12/15/2022 | 45.0     | Initial draft for MAG\*3.0\*329.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 11/03/2022 | 44.7     | Updates to Updating an Existing VIX, Post-Installation for New VIX Installations and Updating Existing VIX Installations, and Troubleshooting/Reconfiguration.                                        | VA IT VistA Imaging Technical team |
| 10/27/2022 | 44.6     | Updates to Updating an Existing VIX and SQL Server Removal.                                                                                                                                           | VA IT VistA Imaging Technical team |
| 10/07/2022 | 44.5     | Updates to Installing a New VIX.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 10/06/2022 | 44.4     | Updates to Installing a New VIX, Updating an Existing VIX, and Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                   | VA IT VistA Imaging Technical team |
| 10/05/2022 | 44.3     | Updates to Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                                                                       | VA IT VistA Imaging Technical team |
| 09/19/2022 | 44.2     | Revisions to Preparing for a New VIX Installation.                                                                                                                                                    | VA IT VistA Imaging Technical team |
| 09/16/2022 | 44.1     | Updates for MAG\*3.0\*303 based on review.                                                                                                                                                            | VA IT VistA Imaging Technical team |
| 08/25/2022 | 44.0     | Initial draft for MAG\*3.0\*303.                                                                                                                                                                      | VA IT VistA Imaging Technical team |
| 06/07/2022 | 43.4     | Revisions to Service Account Settings Appendix.                                                                                                                                                       | VA IT VistA Imaging Technical team |
| 06/03/2022 | 43.3     | Updates for MAG\*3.0\*269 release date.                                                                                                                                                               | VA IT VistA Imaging Technical team |
| 05/26/2022 | 43.2     | Revisions to Installing a New VIX, Updating an Existing VIX, Post Installation Instructions, Troubleshooting, and Service Account Settings Appendix.                                                  | VA IT VistA Imaging Technical team |
| 05/12/2022 | 43.1     | Revisions to Installing a New VIX, Updating an Existing VIX, Post Installation Instructions, and Troubleshooting.                                                                                     | VA IT VistA Imaging Technical team |
| 05/11/2022 | 43.0     | Revisions to Service Account Settings Appendix.                                                                                                                                                       | VA IT VistA Imaging Technical team |
| 05/10/2022 | 42.9     | Revisions to Installing a New VIX, Updating an Existing VIX, and Post Installation Instructions.                                                                                                      | VA IT VistA Imaging Technical team |
| 04/20/2022 | 42.8     | Revisions to Installing a New VIX and Updating an Existing VIX.                                                                                                                                       | VA IT VistA Imaging Technical team |
| 03/18/2022 | 42.7     | Revisions to Updating an Existing VIX, and Post Installation Instructions.                                                                                                                            | VA IT VistA Imaging Technical team |
| 02/22/2022 | 42.6     | Revisions to Updating an Existing VIX, and Post Installation Instructions.                                                                                                                            | VA IT VistA Imaging Technical team |
| 02/10/2022 | 42.5     | Revisions to Updating an Existing VIX, and Post Installation Instructions.                                                                                                                            | VA IT VistA Imaging Technical team |
| 02/04/2022 | 42.4     | Revisions to Installing a New VIX and Updating an Existing VIX, and Back Out/Uninstall Scenarios.                                                                                                     | VA IT VistA Imaging Technical team |
| 01/03/2022 | 42.3     | Revisions to Installing a New VIX and Updating an Existing VIX.                                                                                                                                       | VA IT VistA Imaging Technical team |
| 12/10/2021 | 42.2     | Revisions to Installing a New VIX and Updating an Existing VIX.                                                                                                                                       | VA IT VistA Imaging Technical team |
| 11/16/2021 | 42.1     | Incorporated comments from reviewers for MAG\*3.0\*269, Revisions to Installing a New VIX, Updating an Existing VIX, Back Out/Uninstall Scenarios, & Appendices. Reduced image file sizes.            | VA IT VistA Imaging Technical team |
| 09/03/2021 | 42.0     | Update for MAG\*3.0\*269, Revisions to Installing a New VIX and Updating an Existing VIX.                                                                                                             | VA IT VistA Imaging Technical team |
| 09/02/2021 | 41.0     | Updates for MAG\*3.0\*284                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 04/06/2021 | 40.4     | Additional Updates for MAG\*3.0\*254, Revisions to Installing a New VIX, Updating an Existing VIX, Post-Installation for New VIX Installations and Updating Existing VIX Installations.               | VA IT Vista Imaging Technical team |
| 03/17/2021 | 40.3     | Additional Updates for MAG\*3.0\*254, Post-Installation for New VIX Installations and Updating Existing VIX Installations.                                                                            | VA IT VistA Imaging Technical team |
| 03/11/2021 | 40.2     | Additional Updates for MAG\*3.0\*254, Back Out/Uninstall Scenarios.                                                                                                                                   | VA IT VistA Imaging Technical team |
| 02/24/2021 | 40.1     | Additional Updates for MAG\*3.0\*254, Post-Installation for New VIX Installations and Updating Existing VIX Installations, & Appendices.                                                              | VA IT VistA Imaging Technical team |
| 01/28/2021 | 40.0     | Additional Updates for MAG\*3.0\*254, Revisions to Installing a New VIX, Updating an Existing VIX, Post-Installation for New VIX Installations and Updating Existing VIX Installations, & Appendices. | VA IT VistA Imaging Technical team |
| 01/20/2021 | 39.0     | Update for MAG\*3.0\*254, Revisions to Installing a New VIX, Updating an Existing VIX, Post-Installation for New VIX Installations and Updating Existing VIX Installations, & Appendix A.             | VA IT VistA Imaging Technical team |
| 05/29/2020 | 38.0     | Update for MAG \*3.0\*249, Addition of PowerShell Verification section, Revisions to Pre-Installation Configuration - Backup Copies and Tomcat User Permissions section.                              | <span class="mark">REDACTED</span> |
| 05/26/2020 | 37.0     | Revisions for Zip/Unzip, Manual restart sections, Figure headings, Post-Installation for New VIX Installations and Updating Existing VIX Installations & Appendix A.                                  | <span class="mark">REDACTED</span> |
| 03/16/2020 | 36.0     | Update for MAG\*3.0\*249, 508 compliant.                                                                                                                                                              | <span class="mark">REDACTED</span> |
| 08/16/2019 | 35.5     | Update for T3 Build.                                                                                                                                                                                  | <span class="mark">REDACTED</span> |
| 08/02/2019 | 35.0     | Update for MAG\*3.0\*230.                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 05/20/2019 | 34.0     | Update to save VIX configuration settings.                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 04/29/2019 | 33.0     | Update to save VIX configuration settings.                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 04/05/2019 | 32.0     | Updated for MAG\*3.0 221 T5 Updates.                                                                                                                                                                  | <span class="mark">REDACTED</span> |
| 03/22/2019 | 31.0     | Updated for MAG\*3.0 221 T4.                                                                                                                                                                          | <span class="mark">REDACTED</span> |
| 03/01/2019 | 30.0     | Updated for MAG\*3.0 221 T4.                                                                                                                                                                          | <span class="mark">REDACTED</span> |
| 02/22/2019 | 29.0     | Updated for MAG\*3.0 221.                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 02/01/2019 | 28.0     | Updated for MAG\*3.0 201 T9.                                                                                                                                                                          | <span class="mark">REDACTED</span> |
| 11/19/2018 | 27.0     | Updated for MAG\*3.0\*201.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 09/27/2018 | 26.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 08/21/2018 | 25.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 08/14/2018 | 24.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 07/26/2018 | 23.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 07/06/2018 | 22.0     | Updated for MAG\*3.0\*197.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 06/21/2018 | 21.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 05/25/2018 | 20.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 03/13/2018 | 19.0     | Additional MAG\*3.0\*197 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 01/26/2018 | 18.0     | Updated for MAG\*3.0\*197.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 01/25/2018 | 17.0     | Additional MAG\*3.0\*185 Updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 01/11/2018 | 16.0     | Additional MAG\*3.0\*185 updates.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 12/05/2017 | 15.0     | Updated MAG\*3.0\*185 build numbers.                                                                                                                                                                  | <span class="mark">REDACTED</span> |
| 11/14/2017 | 14.0     | Incorporated comments from reviewers regarding MAG\*3.0\*185.                                                                                                                                         | <span class="mark">REDACTED</span> |
| 10/25/2017 | 13.0     | MAG\*3.0\*185 Updates.                                                                                                                                                                                | <span class="mark">REDACTED</span> |
| 10/03/2017 | 12.0     | MAG\*3.0\*177 Updates.                                                                                                                                                                                | <span class="mark">REDACTED</span> |
| 08/01/2017 | 11.0     | MAG\*3.0\*177 Updates.                                                                                                                                                                                | <span class="mark">REDACTED</span> |
| 07/26/2017 | 10.0     | MAG\*3.0\*170 Updates.                                                                                                                                                                                | <span class="mark">REDACTED</span> |
| 07/05/2017 | 9.0      | MAG\*3.0\*170 Installer Updates.                                                                                                                                                                      | <span class="mark">REDACTED</span> |
| 04/27/2017 | 8.0      | Updated port information.                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 03/24/2017 | 7.0      | Date updates.                                                                                                                                                                                         | <span class="mark">REDACTED</span> |
| 02/14/2017 | 6.0      | Updated for MAG 3.0\*170.                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 05/10/2016 | 5.0      | Updated for MAG\*3.0\*162.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 09/09/2013 | 4.0      | Updated for MAG\*3.0\*130.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 07/25/2013 | 3.0      | Updated for MAG\*3.0\*034/116/118, MAG\*3.0\*119, MAG\*3.0\*127, MAG\*3.0\*129.                                                                                                                       | <span class="mark">REDACTED</span> |
| 05/07/2012 | 2.0      | Updated for MAG\*3.0\*122.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 10/14/2011 | 1.0      | Created for MAG\*3.0\*104. WPR complete Aug 31; labeled for release Oct 14.                                                                                                                           | <span class="mark">REDACTED</span> |
<span id="_Ref68783760" class="anchor"></span>Table 1: Functions Affected by VIX Updates
Table of Contents
Table of Figures
Table of Tables

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document explains how to install the VistA Imaging eXchange (VIX) service. Please follow the install checklist in *Appendix E: VIX Install Checklist* at the same time as you follow the main sections of this document*.* To do that, most people open two copies of this document at once.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for VA staff responsible for managing a local VIX, called *the VIX server* for the remainder of this document.

This document presumes a working knowledge of the VistA environment, VistA Imaging components and workflow, and Windows administration.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses the following conventions:

Controls, options, and button names are displayed in Bold.

A vertical bar is used to separate successive menu choices. For example: “Click File \| Open” means: “Click the File menu; then click the Open option.”

Keyboard key names are displayed in bold and in brackets.

Sample output is displayed in monospace.

Helpful information is denoted by a TIP.

Important or required information is displayed in a NOTE.

Critical information is indicated by: ![](vista-imaging-exchange-vix-installation-guide/002.png)

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX is a component of VistA Imaging and is regulated as a medical device by the Food and Drug Administration (FDA). Use of the VIX is subject to the following provisions:

![](vista-imaging-exchange-vix-installation-guide/003.png)The FDA classifies VistA Imaging and the VIX (as VistA Imaging component) as a medical device. Unauthorized modifications to VistA Imaging, including the VIX, such as installing unapproved software, adulterates the medical device. The use of an adulterated medical device violates US federal law (21CFR820).

![](vista-imaging-exchange-vix-installation-guide/004.png)Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the VIX server from such systems.

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this manual, the following document contains information about the VIX:

[VIX Administrator’s Guide](https://www.va.gov/vdl/application.asp?appid=105)

# Installing a New VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to implement a new VIX. The installation checklist in *Appendix E: VIX Install Checklist* summarizes the process.

TIP: If you are updating an existing VIX, do not use this section; instead, use the *Updating an Existing VIX* section.

## Preparing for a New VIX Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preparing to install a new VIX involves:

- Configuring the MUSE interface is optional. If using the MUSE interface, this requires the MUSE username, MUSE password, MUSE port, and MUSE protocol for the site’s online MUSE server. If the MUSE username, password, port, and protocol are not documented in existing site VistA Imaging documentation, please contact the local BioMed team or MUSE administrator for the information.
- Acquiring Installation File. Copy MAG3_0P358_VIX_SETUP.msi to C:\temp. (Download if required. See the patch description of the patch for the download location.)
- Selecting and validating the server where the VIX gets installed, see *Selecting and Validating the VIX Server*.
- Getting VIX component licenses, see *Getting VIX Component Licenses*.
- Getting a VIX security certificate, see *VIX Security Certificate*.
- Java Version Verification, see *Java Version Verification*.
- LibreOffice Verification, see *LibreOffice Verification*.

> **NOTE:** Please ensure you have scheduled a downtime of VIX services. It may take 1-2 hours to complete.

Please restart the server, before installing a new VIX.

Specifics are covered in the following sections.

### Selecting and Validating the VIX Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX server must meet the FDA, hardware, and operating system/environmental requirements specified in the following sections.

#### FDA Requirements

The VIX is a component of VistA Imaging and is therefore regulated as a medical device by the FDA. Use of the VIX is subject to the terms of use listed in the introduction.

#### Operating System and Hardware Requirements

The VIX hardware requirements are as follows:

- Installation must be done on a 64-bit Operating System (OS) machine running Windows Server 2019.
- Installation requires at least 2 Gigabytes (GBs) of free disk space.
- The VIX servers run with required settings of at least:
- 4 Central Processing Units (CPUs)
- 32 GBs of Random Access Memory (RAM)
- A primary local drive with 120 GBs of disk space
- A dedicated local drive for the VIX cache with 500 GBs of disk space
- The VIX requires at least a 1 gigabit Ethernet connection.

  It is recommended to install on the latest supported OS. Slow performance may occur with VIX servers running under the required settings.

#### Port Requirements

On the VIX server, ports <span class="mark">REDACTED</span> are accessible to VA wide area network IP addresses (10.x.x.x).

If using standard MUSE (not MUSE NX™), verify that port <span class="mark">REDACTED</span> is open and accessible to the VIX for communication with the site's MUSE.

> **NOTE:** MUSE™ NX requires port <span class="mark">REDACTED</span> is open and accessible to the VIX for communication.

#### Environment Requirements

The VIX environment requirements include .NET 4.8 framework installed. .NET Framework 4.8 is installed if it is not already installed with the VIX Installer.

### Getting VIX Component Licenses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two toolkits used by the VIX require third-party licenses.

#### Laurel Bridge DICOM Connectivity Framework (DCF) Toolkit

The Laurel Bridge DICOM Connectivity Framework (DCF) toolkit is a third-party toolkit used by the VIX to convert images to and from DICOM format.

The VA has purchased an enterprise-wide license for this toolkit.

If you are adding a new server in addition to the current server, you can transfer the current license to a new machine and run it in parallel with the old machine for 2 weeks to ensure your new server works properly. If doing this, please keep Laurel Bridge posted as to your license activity via their license transfer form at <https://laurelbridge.com/support/>. If transferring the Laurel Bridge license please ensure the Product Serial Number has been transferred to the new server.

If you do not have a site-specific serial number for this license, do the following:

1.  From the VIX server, attempt to access the Laurel Bridge activation code server at <https://laurelbridge.com>. (A login page displays if you can access the site.)

    ![](vista-imaging-exchange-vix-installation-guide/005.png) If you cannot access this site, enter a ticket and indicate that your site ACL (access control list) needs to be modified to access<span class="mark">REDACTED</span> over HTTPS port<span class="mark">REDACTED</span>.
1.  Contact the <span class="mark">REDACTED</span> mail group to obtain a request form and instructions for completing the form.

The VIX installation process generates an activation code using the serial number information provided. The activation code allows the Laurel Bridge DCF toolkit to be installed and used.

The Laurel Bridge activation code links to the hardware of the server where the toolkit is installed. If you must replace the licensed server, email the contacts listed previously to arrange to get the serial number(s) transferred as well.

#### Aware JPEG2000 Toolkit License

The Aware JPEG2000 toolkit is a third-party toolkit used for DICOM-to-JPEG2000 image conversion by the VIX.

Sites that implement the VIX must purchase a one-time permanent license for the latest version of the Aware JPEG2000 toolkit from Aware for each server where the VIX is used.

> **NOTE:** Do not install the Aware JPEG2000 toolkit before you run the VIX installer. The VIX installer installs the version of the Aware JPEG2000 toolkit with which the VIX has been tested. If you install the Aware JPEG2000 toolkit before running the VIX installer, this interferes with the installation process.

### VIX Security Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each server that hosts the VIX must have a security certificate.

A default security certificate named federation.zip is included with VIX installer that includes the following files federation.truststore and federation.keystore. The VIX Service Installation Wizard prompts for the federation.zip file during the installation process.

> **NOTE:** It is possible the default security certificate named federation.zip included with the VIX installer is out of date at the time of install. It is recommended to send an email to <VAITVISTAIMAGINGTECH@VA.GOV> and <u>VHAVIVIXSETUP@VA.GOV</u> to see determine if the default security certificate is valid or to obtain an updated certificate if it expired. Include the following: the Fully Qualified Domain Name (FQDN) of the VIX server and contact information for the primary and backup administrators of the VIX. Requests typically process within five business days.

> **NOTE:** If the Fully Qualified Domain Name (FQDN) of the VIX server does not use a standard name (i.e., not ending in med.va.gov or va.gov) send an email to <span class="mark">REDACTED</span> and include the following: the Fully Qualified Domain Name (FQDN) of the VIX server and contact information for the primary and backup administrators of the VIX. Requests typically process within five business days.

### Java Version Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the VIX install, validate any Java version installed. MAG\*3.0\*358 VIX installer uninstalls Java 8.0.371, if installed, and installs Java 8.0.431. If the Java version installed is older than Java 8.0.371, you must uninstall manually. The current Java version can be checked using the Control Panel (Figure 1). Reboot your server after Java uninstall.

<span id="_Ref79491056" class="anchor"></span>Figure : Java and LibreOffice Version Check

![](vista-imaging-exchange-vix-installation-guide/006.png)

### LibreOffice Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the VIX install, validate any LibreOffice version installed. MAG\*3.0\*358 VIX installer uninstalls LibreOffice 7.3.5 and installs LibreOffice 24.2.5. If the LibreOffice version installed is not 7.3.5, it must be uninstalled manually. The current LibreOffice version can be checked using the Control Panel (Figure 1).

### PowerShell 7 Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the VIX install, validate any PowerShell 7 version installed. MAG\*3.0\*358 VIX installer uninstalls PowerShell 7.2.4 and installs PowerShell 7.3.9. If the PowerShell 7 version installed is not 7.2.4, it must be uninstalled manually. The current PowerShell version can be checked using the Control Panel.

## New VIX Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps are used to install a VIX on a server for the first time. Installation should take less than 30 minutes if all preparation steps in the previous sections are complete.

> **NOTE:** Only perform the steps in this section if you are installing the VIX on a single server.

## Preparing Passwords, Activating Components, and Staging Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Use proper safeguards to securely store passwords.

Before starting the VIX installation process, do the following:

1.  If using the MUSE interface, as already stated in Section 2.1, configuring requires the MUSE username, MUSE password, MUSE port, and MUSE protocol for the site’s online MUSE server. If the MUSE username, password, port, and protocol are not documented in existing site VistA Imaging documentation, please contact the local BioMed team or MUSE administrator for the information.
2.  Prepare a password to be used for the Apache Tomcat administrator account created as part of the VIX installation process.
- The password is case sensitive, must contain at least eight (8) alphanumeric characters, and must contain at least one capital letter and one number.
3.  Prepare a password for the Windows account that the VIX installation process creates.
- The system uses this Windows account, named “apachetomcat” when it is created by the VIX installer, to run the VIX in the Tomcat environment. This account is limited to only the functions it needs to run the VIX.
- The password is case sensitive, must contain at least fourteen (14) alphanumeric characters, and must contain at least one capital letter and one number.
4.  To use the Release of Information (ROI) and DICOM Query Retrieve Service Class Provider (SCP), set up a local VistA service account as specified in *Appendix D: Service Account Settings*.
5.  Determine the email address or addresses for notification about invalid ROI periodic processing credentials. The VIX sends an email notification to the email address or addresses if the ROI periodic processing credentials are invalid or have expired. You must specify this address when you install the VIX. You can set up a new email account for this purpose or use an existing one.

### VIX Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIX installation involves running two processes back-to-back. The first short process installs the VIX Service Installation Wizard. The second, longer process involves using the VIX Service Installation Wizard to install the actual VIX.

> **NOTE:** These steps presume you have already obtained a serial number for the Laurel Bridge DCF toolkit. These steps also presume the VIX can access the Laurel Bridge license server via the internet.

#### To install the VIX Server

1.  Use an administrator-level account to log onto the VIX server.
6.  If you did not already do this, copy the latest VIX installer (MAG3_0P358_VIX_SETUP.msi) to C:\temp.
7.  Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P358_VIX_SETUP.msi file and click on Install.
2.  While running the VIX Service Installation Wizard, if prompted with “Do you want to allow the following program from a verified publisher to make changes to this computer?”, click Yes (Figure 2).

<span id="_Ref67914042" class="anchor"></span>Figure : User Account Control - VIX Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/007.png)

> **NOTE:** This step may occur after clicking Next.

1.  When the Welcome page displays, click Next.
2.  When the Confirm Installation page displays, click Next.
3.  When the Installation Complete screen displays, click Close.
8.  Run the VIX Service Installation Wizard as an administrator (Figure 3 shows this for a server with Windows Server 2019).
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> NOTE: If the VIX Service Installation Wizard does not appear in the Search bar as in Figure 3 logout of the Windows administrator account session and log back in.

> NOTE: The VIX Service Installation Wizard may alternatively be run as an administrator by performing the following:

- Open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

<span id="_Ref187995996" class="anchor"></span>Figure : Run the VIX Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/008.png)

9.  If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes (Figure 4).

<span id="_Ref90060692" class="anchor"></span>Figure : User Account Control - VIX Installer

![](vista-imaging-exchange-vix-installation-guide/009.png)

10. If .NET Framework 4.8 or greater is not installed, the VIX Service Installation automatically installs .NET Framework 4.8 and setup dialogs will appear (Figure 5 and Figure 6) to extract files and install. If no .NET Framework setup dialogs appear, skip to step 7. Otherwise, the install of .NET Framework may take over five minutes to complete and the setup dialogs progress bars will update.

<span id="_Ref132125585" class="anchor"></span>Figure : .NET Framework 4.8 Extracting Files

![](vista-imaging-exchange-vix-installation-guide/010.png)

<span id="_Ref132125590" class="anchor"></span>Figure : .NET Framework 4.8 Setup

![](vista-imaging-exchange-vix-installation-guide/011.png)

When the installation of .NET Framework 4.8 completes, click Finish (Figure 7) and then click Restart Now (Figure 8) to reboot your server.

<span id="_Ref132125868" class="anchor"></span>Figure : .NET Framework Setup Complete

![](vista-imaging-exchange-vix-installation-guide/012.png)

<span id="_Ref132125890" class="anchor"></span>Figure : .NET Framework Restart

![](vista-imaging-exchange-vix-installation-guide/013.png)

After the server reboots, Run the VIX Service Installation Wizard as an administrator and if prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes, as discussed in steps 4 and 5, and then continue to step 7.

11. When the Welcome page for the VIX Service Installation Wizard displays, click Next.
12. In the Site Number field of the Specify the VA site... page, enter the STATION NUMBER (field (#99) in the INSTITUTION file (#4) of your site, the information is in FileMan in VistA).
13. Confirm the connection by clicking Lookup Server Address. Then click Next (Figure 9).

<span id="_Ref132386154" class="anchor"></span>Figure : Specify the VA site the VIX will service

![](vista-imaging-exchange-vix-installation-guide/014.png)

14. Verify the site-related information retrieved by the lookup is correct. Then, click Next.

    NOTE: The VIX server hostname is blank, and the port number is 0; these values are populated automatically once the VIX is registered with the VistA site service.
15. Please be patient for the VIX Prerequisites page to appear, as it may take a while. When the Install the VIX Prerequisites page displays, verify that the icons for the first three items on the page are![](vista-imaging-exchange-vix-installation-guide/015.png).
1.  *account* has Administrator role – This line indicates if an administrative account is being used. If not, cancel the installation and restart it using a Windows administrator account.
2.  Current operating system – This line indicates if the proper operating system is present. If a non-supported operating system is identified, the installation cannot continue.
3.  Sufficient disk space – This line indicates if sufficient disk space is available for installation.
16. On the same page, read the line that indicates the state of the Java Runtime Environment. If ![](vista-imaging-exchange-vix-installation-guide/016.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/017.png) displays (Figure 10), do the following:
1.  Click Install.
4.  Wait until the status icon for the Java Runtime Environment changes to ![](vista-imaging-exchange-vix-installation-guide/018.png). This install of Java may take over five minutes to complete. Please be patient, as this step may take a while to complete.

<span id="_Ref67914320" class="anchor"></span>Figure : VIX Service Installation Wizard 30.358.X.XXXX

![](vista-imaging-exchange-vix-installation-guide/019.png)

> **NOTE:** The person installing the VIX software does not need to be in the VHAMASTER domain. The installer’s domain should appear with their name. This (and subsequent screenshots) is just an example of what the installer sees.

17. On the same page, read the line that indicates the state of the Apache Tomcat installation. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/020.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/021.png) displays (Figure 11), do the following:
1.  Click Install.
2.  In the dialog box that displays, enter and confirm the Apache Tomcat administrator account password that you previously prepared as described in *Preparing Passwords, Activating Components, and Staging Files*. Then, click OK.
5.  Wait until the status icon for Apache Tomcat changes to ![](vista-imaging-exchange-vix-installation-guide/022.png). This install of Tomcat may take over five minutes to complete. Please be patient, as this step may take a while to complete.

<span id="_Ref67914450" class="anchor"></span>Figure : VIX Prerequisites - Tomcat Not Installed

![](vista-imaging-exchange-vix-installation-guide/023.png)

18. On the same page, read the line that indicates the state of the Visual C++ Redistributable installation. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/024.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/025.png) displays (Figure 12), do the following:
3.  Click Install.
6.  Wait until the status icon for Visual C++ Redistributable changes to ![](vista-imaging-exchange-vix-installation-guide/026.png). (This install of the Visual C++ Redistributable may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref149141605" class="anchor"></span>Figure : VIX Prerequisites – Visual C++ Redistributable not installed

![](vista-imaging-exchange-vix-installation-guide/027.png)

19. On the same page, read the line that indicates the state of the Laurel Bridge toolkit. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/028.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/029.png) displays (Figure 13), do the following:

<span id="_Ref79492299" class="anchor"></span>Figure : VIX Prerequisites - Laurel Bridge Not Installed

![](vista-imaging-exchange-vix-installation-guide/030.png)

1.  On the Install the VIX Prerequisites window, click Install. The Activate DCF License window opens with the Network Activation tab open and pre-populates with about half of the boxes in the window.
7.  For Network Activation (requires a Product Serial Number) enter all the following information in the Network Activation tab:

    NOTE: The system disables the Activate button if any of the following boxes are left blank.
    1.  Product Serial Number – the new Laurel Bridge DCF serial number (include dashes).
    2.  Site – the name of your site.
    3.  CPUs – the number of CPUs on the server hosting the VIX.
    4.  End User name and End User email – the administrator of your local VistA Imaging system.
    5.  Maintenance Contact Name, Maintenance Contact E-mail, and Maintenance Contact Phone – information for the Health, Clinical Services Diagnostics Team.
8.  Near the bottom of the window, click Activate. After a brief delay, the Status box displays a message.
9.  If a green “Success” message appears click Exit with success and skip to the next prerequisite step, otherwise select the Manual Activation tab.
10. If network activation was not successful, for Manual Activation do the following:
1.  Select the Manual Activation tab.
2.  On the Manual Activation tab on the line Activation Code, enter the activation code.
3.  Near the bottom of the window, click Activate. After a brief delay, the Status box displays a message.
4.  If a green “Success” message appears click Exit with success and skip to the next prerequisite step, otherwise download the Laurel Bridge license from Laurel Bridge’s website and continue with the steps below.

    NOTE: If downloading the Laurel Bridge license, such as using the Manual Product License Activation from <https://laurelbridge.com/product_activation.php>, please select the Version in the drop-down as 3.3.x before clicking Submit.
5.  Click Exit with error to close out of the Manual Activation tab.
6.  Copy the contents of the downloaded Laurel Bridge license into the systeminfo file in C:\DCF_RunTime_x64\cfg.
7.  Click Install again next to the Laurel Bridge DICOM toolkit on the prerequisite window.
20. On the same page, read the line that indicates the state of the service account. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/031.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/032.png) displays (Figure 14), do the following:
1.  Click Create.
2.  In the dialog box that displays, enter the Windows service account password that you prepared in *Preparing Passwords, Activating Components, and Staging Files*, previously. Then, click OK.
11. Wait until the status icon for the service account changes to ![](vista-imaging-exchange-vix-installation-guide/033.png).

<span id="_Ref79492357" class="anchor"></span>Figure : VIX Prerequisites - Service Account not Created

![](vista-imaging-exchange-vix-installation-guide/034.png)

21. On the same page, check the line that indicates the state of VIX security certificate. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/035.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/036.png) displays (Figure 15), do the following:
1.  Click Install.
2.  In the dialog box that displays, click OK if using the default security certificate included with the VIX Installer. Otherwise, in the dialog box that displays, click Select. Specify the location of the security certificate on the local VIX server. Then, click OK.

<span id="_Ref79492669" class="anchor"></span>Figure : VIX Prerequisites - VIX Security Certificate not Installed

![](vista-imaging-exchange-vix-installation-guide/037.png)

22. On the same page, read the line that indicates the state of the LibreOffice installation. If ![](vista-imaging-exchange-vix-installation-guide/038.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/039.png) displays (Figure 16), do the following:
1.  Click Install.
12. Wait until the status icon for LibreOffice changes to ![](vista-imaging-exchange-vix-installation-guide/040.png). (This install of LibreOffice may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref79492658" class="anchor"></span>Figure : VIX Prerequisites - LibreOffice not Installed

![](vista-imaging-exchange-vix-installation-guide/041.png)

23. On the same page, read the line that indicates the state of the PowerShell installation. If ![](vista-imaging-exchange-vix-installation-guide/042.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/043.png) displays (Figure 17), do the following:
1.  Click Install.
13. Wait until the status icon for PowerShell changes to ![](vista-imaging-exchange-vix-installation-guide/044.png). (This install of PowerShell may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref105771999" class="anchor"></span>Figure : VIX Prerequisites - PowerShell not Installed

![](vista-imaging-exchange-vix-installation-guide/045.png)

24. In the Install the VIX Prerequisites page, confirm that all the icons are ![](vista-imaging-exchange-vix-installation-guide/046.png). Then, click Next (Figure 18).

<span id="_Ref67916641" class="anchor"></span>Figure : VIX Service Installation Wizard Prerequisites Complete

![](vista-imaging-exchange-vix-installation-guide/047.png)

25. In the Specify the location page, select the drive for the VIX configuration files to reside. Select the “C:\\ drive for the VixConfig folder. Then, click Create.
26. On the same page, select the drive where to create the VIX cache. Select the appropriate VixCache drive for your site (E: is displayed as an example in Figure 19). Then, click Create.
27. On the same page, select the drive where to create the VIX log archive. Select the appropriate VIX log archive drive for your site (E: is displayed as an example in Figure 19). Then, click Create.

    NOTE: It is suggested to use the same local drive for the VIX Cache and VIX log archive.

<span id="_Ref67916724" class="anchor"></span>Figure : VIX Cache, Configuration, and Log Archive Folder Creation

![](vista-imaging-exchange-vix-installation-guide/048.png)

28. Click Next.
29. In the VistA and Email Configuration (Figure 21), perform the following:
1.  Specify the access and verify codes for the account with the VistA credentials. The VIX uses this account for periodic processing of ROI disclosure requests and DICOM SCP query retrieve requests. The account must be valid VistA credentials with the settings specified in *Appendix D: Service Account Settings*.

    NOTE: Hidden/asterisk and plain text forms of the access and verify codes can by toggled. Click Show to show the plain text forms and click Hide to show the hidden/asterisk forms.
2.  Specify the email address that gets notifications for invalid credentials. The VIX sends an email notification to the address or addresses specified in this field if the ROI periodic processing credentials are expired or invalid. You can enter several addresses, separated by a comma.
3.  Click Confirm (Figure 20).

<span id="_Ref67916832" class="anchor"></span>Figure : VistA and Email Configuration - Confirm

![](vista-imaging-exchange-vix-installation-guide/049.png)

> The VIX installation program checks the information. If it detects an error, it displays a tooltip with information about the error. When it confirms the configuration, Next becomes available. Click Next (Figure 21).

<span id="_Ref67916910" class="anchor"></span>Figure : VistA and Email Configuration – Next

![](vista-imaging-exchange-vix-installation-guide/050.png)

30. In the Specify the MUSE Configuration, if enabling the MUSE, check Enable and configure MUSE. Specify the MUSE site number, server host, username, password, port, and protocol. If changes are needed, please refer to *Appendix A: Enable MUSE Functionality* for additional information to assist with the MUSE configuration.

    If disabling the MUSE, uncheck Enable and configure MUSE.

    After applying any changes for the MUSE settings, click Confirm (Figure 22)

    NOTE: Hidden/asterisk and plain text forms of the username and password can by toggled. Click Show to show the plain text forms and click Hide to show the hidden/asterisk forms.

    NOTE: It is expected that the site administrator is aware of all needed entries in the MUSE configuration, including the MUSE Site Number, Host, Username, Password, Port, and Protocol if changes are needed. One method to obtain the MUSE site number, host, port, and username is from the Background processor discussed in *Appendix A: Enable* MUSE Functionality. If the password is not documented in existing site VistA Imaging documentation or if not available, please contact the local BioMed team or MUSE administrator. The default standard MUSE port is <span class="mark">REDACTED</span> and protocol is http. The default MUSE™ NX port is <span class="mark">REDACTED</span> and protocol is https. Contact the local BioMed team or MUSE administrator if the MUSE port and protocol are not known.

<span id="_Ref92809151" class="anchor"></span>Figure : Specify the MUSE Configuration - Before Confirm

![](vista-imaging-exchange-vix-installation-guide/051.png)

31. In the Specify the MUSE Configuration, after it confirms the configuration, Next becomes available. Click Next (Figure 23).

    NOTE: During MUSE Configuration validation, the VIX installation program checks the information. If the installation program detects an error, it displays a tooltip with information about the error.

<span id="_Ref92809150" class="anchor"></span>Figure 23: Specify the MUSE Configuration - After Confirm

![](vista-imaging-exchange-vix-installation-guide/052.png)

32. On the Install the VIX page (Figure 24), click Install. (The information on this page is saved in C:\Program Files (x86)\VistA\Imaging\VIXInstaller for future reference or troubleshooting.) This starts the installation process. This starts the installation process of the VIX and the VIX Viewer/Render Services.

<span id="_Ref92808177" class="anchor"></span>Figure : Begin the VIX and VIX Viewer/Render Services Install

![](vista-imaging-exchange-vix-installation-guide/053.png)

1.  Wait a moment and then click Configure Viewer/Render (Figure 25).

<span id="_Ref92809820" class="anchor"></span>Figure : VIX Viewer/Render Info Dialog

![](vista-imaging-exchange-vix-installation-guide/054.png)

14. Verify the following settings:
1.  Verify the viewer port number is <span class="mark">REDACTED</span>.
2.  Verify the trusted client port is <span class="mark">REDACTED</span>.
3.  Verify the Render Service \> Port Number is <span class="mark">REDACTED</span>.
4.  Verify Site Service \> Host Name is localhost.
5.  Verify Site Service \> Port Number is <span class="mark">REDACTED</span>.
6.  Verify VIX Service \> Host Name is localhost.
7.  Verify Database \> Instance Name is C:\Program Files\VistA\Imaging\VIX.Render.Service\Db\SQLiteDb.db.
15. Edit image cache directory drive to the dedicated VIX cache drive. (i.e., “E:\VIXRenderCache”)
16. If setting values were modified, click the Save Configuration button in the top right corner.
17. Click OK.
18. The installation updates the VIX Viewer/Render Services in the background. Then the VIX installation will finish. This takes up to over five minutes to complete.
33. During the final install, a PowerShell script utility pops up (Figure 26) to perform additional install tasks and closes when complete.

    NOTE: The PowerShell pop-up performs various configuration and certificate tasks and executes patch-specific post-scripts.

    NOTE: If the MUSE service is not enabled, the PowerShell pop-up may display a red error message in the MUSE check section. See Figure 26.

<span id="_Ref67920307" class="anchor"></span>Figure : PowerShell Pop-up Script

![](vista-imaging-exchange-vix-installation-guide/055.png)

34. The VIX starts automatically (Tomcat and Viewer/Render services) when the installation is complete. When the installation is complete, click Finish to exit the wizard (Figure 27). The VIX Service Installation Wizard closes.

<span id="_Ref67920570" class="anchor"></span>Figure : VIX Install Complete

![](vista-imaging-exchange-vix-installation-guide/056.png)

The VIX starts automatically but cannot be used until it is activated and registered with the VistA Site Service. See the next section for details.

## Activating a New VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the VIX is installed, it is inactive until it is registered with the VistA Site Service. Clinical Display workstations and ISI Rad workstations use the site service to determine if local and remote VIX servers are available.

After the VIX is registered in the site service, the VIX begins to be actively used, both by clinicians at your site and remote VA sites for access to locally stored images.

> **NOTE:** Do not register the VIX with the site service until after it is installed. Registering the VIX before it is installed causes errors and timeout issues for Clinical Display users.

### To Register the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Gather the following information:
- Primary contact name, phone, and email:
- Backup contact name, phone, and email:
- Site name:
- STATION NUMBER (field \#99) from INSTITUTION file (#4):
- Network Name defined for Imaging Resources group:
35. Enter a National ticket to the Health, Clinical Services Diagnostics Team (previously known as Clin 3, the group name is SPM.Health.ClinSvs.Diag) for a site service update.
1.  Paste the lines in the preceding step into the ticket.
2.  Include “Add VIX server to Site Service database.”
36. The Health, Clinical Services Diagnostics Team notifies you, typically within five business days, when the site service registration is complete.
37. Continue to *[Post-Installation for New VIX Installations and Updating Existing VIX Installations](#_Verifying_VIX_Operations).*

# Updating an Existing VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter explains how to update an existing VIX server. An installation checklist that summarizes this process can be found in *Appendix E: VIX Install Checklist*.

## Preparing for a VIX Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preparing for a VIX update involves:

- Configuring the MUSE interface is optional. If using the MUSE interface, this requires the MUSE username, MUSE password, MUSE port, and MUSE protocol for the site’s online MUSE server. If the MUSE username, password, port, and protocol are not documented in existing site VistA Imaging documentation, please contact the local BioMed team or MUSE administrator for the information.
- Acquiring Installation File.
- Acquiring Installation Files. Copy MAG3_0P358_VIX_SETUP.msi to C:\temp. (Download if required. See the patch description of the patch for the download location.)
- Copy the MAG3_0P358_VIX_SETUP.msi to C:\temp for the backup plan if not already present.
- Ensure downtime has been scheduled to install the VIX service. Local administrations of the applications and services impacted by an offline VIX should be contacted prior to installing the MAG3_0P358_VIX_SETUP.msi. The installation needs to be coordinated to avoid any disruption of services. This communication should be done in advance of the VIX update, see *Scheduling Downtime and Impact of a VIX Update.*TIP: VIX-specific account passwords and security key assignments established for older VIX systems automatically carry over to new VIX systems.

> **NOTE:** It is strongly suggested to restart the VIX Server prior to updating an existing VIX.

### Scheduling Downtime and Impact of a VIX Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to schedule downtime with appropriate personnel for the duration of the VIX installation. Schedule 1 to 2 hours for the downtime and notify users of the impact of the VIX update.

While the VIX server is being updated, VIX assisted functions are unavailable. The list of known applications and services impacted by a local offline VIX includes:

- Clinical Display access to remote images may be temporarily inaccessible.
- ISI Rad access to remote images and other teleradiology features.
- DICOM Importer client.
- Local Joint Legacy Viewer / Joint Longitudinal Viewer (JLV) user display of images (local or remote).
- Signed Informed Consent ability to store new consents.
- Any new Ingest consuming application.
- Integrated Visualization System (IVS) mobile application access to local images.
- Enterprise DICOM Q/R functionality.
- Access to DoD images or artifacts.
- Access to VA Cerner images or artifacts.
- Any other external application calling a local VIX service directly.

Table 1 summarizes how a VIX outage affects clinicians.

<table>
<caption><p><span id="_Ref102564585" class="anchor"></span>Table 2: VIX Site’s User Profile SSN, Service Account on Local VistA, and Suggested Service Account on Local VistA</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Clinical Group</th>
<th>Impact</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local Clinical Display Users</td>
<td><p>DoD images are inaccessible for the duration of the VIX shutdown.</p>
<p>Remote VA images may be temporarily inaccessible. Clinical Display attempts to revert to pre-VIX remote image views, but users may have to disconnect from and reconnect to remote sites, or in some cases, restart Clinical Display.</p>
<p>Clinicians may notice longer retrieval times for remote images for the duration of the VIX shutdown.</p>
<p>After the VIX is restarted, restart Clinical Display to ensure that Clinical Display is no longer using pre-VIX remote image views for remote sites.</p></td>
</tr>
<tr class="even">
<td>Local ISI Rad Users</td>
<td>Remote exam data and images and monitored exam lists are unavailable. For additional information, refer to the documentation for ISI Rad.</td>
</tr>
<tr class="odd">
<td>Remote VA or DoD Clinicians requesting Images or Artifacts</td>
<td><p>Remote clinicians may experience transitory application errors if the VIX is shut down while it is in the middle of processing a request; the clinician may have to repeat the request.</p>
<p>Remote VA clinicians issuing new requests may notice longer retrieval times for the duration of the VIX shutdown.</p>
<p>Remote DoD clinicians are unable to retrieve locally stored images for the duration of the VIX shutdown.</p></td>
</tr>
<tr class="even">
<td>Local DICOM Importer Users</td>
<td>The DICOM importer client cannot log into VistA and process imports for the duration that the VIX is down.</td>
</tr>
<tr class="odd">
<td>VIX Image Viewer/JLV Users</td>
<td>Clinical users of JLV cannot access images or artifacts (local or remote) using the VIX image viewer.</td>
</tr>
<tr class="even">
<td>iMedConsent Users</td>
<td>Patients’ consent forms are unavailable. Currently, this results in multiple unsigned Text Integration Utility (TIU) notes in Computerized Patient Record System (CPRS) due to CVIX and iMedConsent Web (ICW) deficiencies until the necessary corrective action(s) can be deployed by both the CVIX and ICW development teams.</td>
</tr>
<tr class="odd">
<td>IVS Mobile Application Users</td>
<td>IVS mobile application users cannot access local images.</td>
</tr>
</tbody>
</table>

<span id="_Ref102564585" class="anchor"></span>Table 2: VIX Site’s User Profile SSN, Service Account on Local VistA, and Suggested Service Account on Local VistA

## Preparing Service Account and Passwords

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before starting the VIX server update process, identify your DICOM/ Release of Information (ROI) periodic processing VistA Imaging VistA service account. It is suggested to verify the name of the VistA service account as described in *Appendix D: Service Account Settings*. To ensure DICOM query retrieve/ROI periodic processing functionality, verify the Social Security Number (SSN) of the service account, verify it has the security keys, secondary menu options, a value for the INITIAL field, and additional options as described in *Appendix D: Service Account Settings*.

Locate the current password used for the Windows account named “apachetomcat” and the DICOM query retrieve/ROI periodic processing VistA Imaging VistA service account credentials.

- The Windows account named “apachetomcat” password is case sensitive, must contain at least fourteen (14) alphanumeric characters, and must contain at least one capital letter and one number.

## Performing a VIX Server Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps to update a VIX server.

> **NOTE:** If LibreOffice has any documents open, please close them before beginning the install process. Otherwise, you do not have to stop any currently running services because this install process automatically stops them for you.

1.  Use an administrator-level account to log onto the VIX server.
38. If you did not already do so in Section 3.1, copy the VIX installation file MAG3_0P358_VIX_SETUP.msi to C:\temp on the VIX server. (Download if required, see the patch description of the patch for the download location).
39. Go into Control Panel/Programs/Programs and Features and remove the prior VIX Service Installation Wizard by right-clicking on it and choosing Uninstall.
40. To Install the VIX Service Installation Wizard perform the following steps:
1.  Right-click the VIX installation file (MAG3_0P358_VIX_SETUP.msi) and click on Install.
2.  While running the VIX Service Installation Wizard, if prompted with “Do you want to allow the following program from a verified publisher to make changes to this computer?”, click Yes (Figure 28)

<span id="_Ref89777021" class="anchor"></span>Figure : User Account Control - Vix Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/057.png)

> **NOTE:** This step may occur after clicking Next.

3.  When the Welcome page displays, click Next.
4.  When the Confirm Installation page displays, click Next.
5.  When the Installation Complete screen displays, click Close.
41. Run the VIX Service Installation Wizard as an administrator (Figure 29 shows this for a server with Windows Server 2019).
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> NOTE: If the VIX Service Installation Wizard does not appear in the Search bar as in Figure 29 logout of the Windows administrator account session and log back in.

> NOTE: The VIX Service Installation Wizard may alternatively be run as an administrator by performing either of the following:

- On the Desktop, find the VIX Shortcuts folder and doubleleft-click. In the folder that opens, right-click VIX Installer and left-click Run as administrator.
- Open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

<span id="_Ref187995791" class="anchor"></span>Figure : Run the VIX Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/058.png)

42. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes (Figure 30).

<span id="_Ref67921616" class="anchor"></span>Figure : User Account Control - VixInstaller

![](vista-imaging-exchange-vix-installation-guide/059.png)

43. If .NET Framework 4.8 or greater is not installed, the VIX Service Installation automatically installs .NET Framework 4.8 and setup dialogs will appear (Figure 31 and Figure 32) to extract files and install. If no .NET Framework setup dialogs appear, skip to step 8. Otherwise, the install of .NET Framework may take over five minutes to complete and the setup dialogs progress bars will update.

<span id="_Ref132872464" class="anchor"></span>Figure : .NET Framework 4.8 Extracting Files

![](vista-imaging-exchange-vix-installation-guide/060.png)

<span id="_Ref132872480" class="anchor"></span>Figure : .NET Framework 4.8 Setup

![](vista-imaging-exchange-vix-installation-guide/061.png)

When the installation of .NET Framework 4.8 completes, click Finish (Figure 33) and then click Restart Now (Figure 34) to reboot your server.

<span id="_Ref132872503" class="anchor"></span>Figure : .NET Framework Setup Complete

![](vista-imaging-exchange-vix-installation-guide/062.png)

<span id="_Ref132872518" class="anchor"></span>Figure : .NET Framework Restart

![](vista-imaging-exchange-vix-installation-guide/063.png)

After the server reboots, Run the VIX Service Installation Wizard as an administrator and if prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes, as discussed in steps 5 and 6, and then continue to step 9.

44. If and only if there are multiple VIX Service Installation Wizards installed (as shown in the Add/Remove Programs in the Control Panel), confirm when running the VIX Service Installation Wizard (VixInstaller.exe) that a message box with an error message appears that says “Installation is unable to proceed” in the title and in the message “Another version of this product is already installed...” (Figure 35). In this case, uninstall any extra VIX Service Installation Wizard(s) and re-run the VIX Service Installation Wizard as an administrator.

<span id="_Ref141283362" class="anchor"></span>Figure : Installation unable to proceed

![](vista-imaging-exchange-vix-installation-guide/064.png)

45. When the Welcome page for the VIX Service Installation Wizard displays, click Next.
46. Click on the button labeled Uninstall version 30.348.1.XXXX to uninstall (Figure 36) the pre-existing VIX software. (If it is not already stopped, the wizard gracefully stops the VIX service before performing the uninstall.)

<span id="_Ref69720406" class="anchor"></span>Figure : Update VIX Components

![](vista-imaging-exchange-vix-installation-guide/065.png)

47. During the uninstall, a PowerShell script utility pops up (Figure 37) to perform back-ups of prior configuration files and, if present, execute any patch-specific pre-scripts. The PowerShell window closes when complete.

<span id="_Ref69479658" class="anchor"></span>Figure : Update VIX Components PowerShell Pop-up Script

![](vista-imaging-exchange-vix-installation-guide/066.png)

48. When the Uninstall is complete, Press Next to continue displays in the VIX Service Installation Wizard, click Next.
49. On the “Specify the VA Site the VIX will service” page, if in Developer Mode (selected after clicking the lower left corner of the VIX Service Installation Wizard in the grey notch) the Site Service URL appears.

    NOTE: Only use Developer mode in the event that changes are needed to the Site Service URL.
50. In the Site Number field of the “Specify the VA Site the VIX will service” page, verify that the Site Number box shows your STATION NUMBER (field (#99) in the INSTITUTION file (#4) of your site, the information is in FileMan in VistA).
51. Confirm the connection by clicking Lookup Server Address. Then click Next (Figure 38).

<span id="_Ref67921872" class="anchor"></span>Figure :Specify the VA site the VIX will service

![](vista-imaging-exchange-vix-installation-guide/067.png)

52. Please be patient for the VIX Prerequisites page to appear, as it may take a while. When the Install the VIX Prerequisites page displays, read the line that indicates the state of the Java Runtime Environment. If ![](vista-imaging-exchange-vix-installation-guide/068.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/069.png) displays (Figure 39), do the following:
1.  Click Install.
19. Wait until the status icon for the Java Runtime Environment changes to ![](vista-imaging-exchange-vix-installation-guide/070.png). (This install of Java may take over five minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref67921985" class="anchor"></span>Figure : VIX Prerequisites - Java Not Installed

![](vista-imaging-exchange-vix-installation-guide/071.png)

> **NOTE:** The person installing the VIX software does not need to be in the VHAMASTER domain. The installer’s domain should appear with their name. This (and subsequent screenshots) is just an example of what the installer sees.

53. On the same page, read the line that indicates the state of the Apache Tomcat installation. If ![](vista-imaging-exchange-vix-installation-guide/072.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/073.png) displays (Figure 40), do the following:
1.  Click Install.
20. Wait until the status icon for Apache Tomcat changes to ![](vista-imaging-exchange-vix-installation-guide/074.png). (This install of Tomcat may take over five minutes complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref67922094" class="anchor"></span>Figure : VIX Prerequisites - Tomcat Not Installed

![](vista-imaging-exchange-vix-installation-guide/075.png)

54. On the same page, read the line that indicates the state of the Visual C++ Redistributable installation. Since you may have reached this page by clicking the Back button on a subsequent page, if ![](vista-imaging-exchange-vix-installation-guide/076.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/077.png) displays (Figure 41), do the following:
4.  Click Install.
21. Wait until the status icon for Visual C++ Redistributable changes to ![](vista-imaging-exchange-vix-installation-guide/078.png). (This install of the Visual C++ Redistributable may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref149142164" class="anchor"></span>Figure : VIX Prerequisites – Visual C++ Redistributable not installed

![](vista-imaging-exchange-vix-installation-guide/079.png)

55. On the same page, check the line that indicates the state of the Laurel Bridge toolkit. Verify ![](vista-imaging-exchange-vix-installation-guide/080.png) displays. If ![](vista-imaging-exchange-vix-installation-guide/081.png) displays, click the Install button next to the Laurel Bridge item. If necessary and only if the Activate DCF License window opens, continue with the steps below. Otherwise skip to the next prerequisite step. If necessary, refer to the *Laurel Bridge DICOM Connectivity* Framework (DCF) Toolkit instructions to obtain an updated serial number and activation code.
1.  The activate DCF License window opens with the Network Activation tab open and pre-populates with about half of the boxes in the window.
22. For Network Activation (requires a Product Serial Number) enter all the following information in the Network Activation tab:

    NOTE: The system disables the Activate button if any of the following boxes are left blank.
    1.  Product Serial Number – the new Laurel Bridge DCF serial number (include dashes).
    2.  Site – the name of your site.
    3.  CPUs – the number of CPUs on the server hosting the VIX.
    4.  End User name and End User email – the administrator of your local VistA Imaging system.
    5.  Maintenance Contact Name, Maintenance Contact E-mail, and Maintenance Contact Phone – information for the Health, Clinical Services Diagnostics Team.
23. Near the bottom of the window, click Activate. After a brief delay, the Status box displays a message.
24. If a green “Success” message appears click Exit with success and skip to the next prerequisite step, otherwise select the Manual Activation tab.
25. If network activation was not successful, for Manual Activation do the following:
1.  Select the Manual Activation tab.
2.  On the Manual Activation tab on the line Activation Code, enter the activation code.
3.  Near the bottom of the window, click Activate. After a brief delay, the Status box displays a message.
4.  If a green “Success” message appears click Exit with success and skip to the next prerequisite step, otherwise download the Laurel Bridge license from Laurel Bridge’s website and continue with the steps below.

    NOTE: If downloading the Laurel Bridge license, such as using the Manual Product License Activation from <https://laurelbridge.com/product_activation.php>, please select the Version in the drop-down as 3.3.x before clicking Submit.
5.  Click Exit with error to close out of the Manual Activation tab.
6.  Copy the contents of the downloaded Laurel Bridge license into the systeminfo file in C:\DCF_RunTime_x64\cfg and save.
7.  Click Install again next to the Laurel Bridge DICOM toolkit on the prerequisite window.
56. On the same page, read the line that indicates the state of the service account. If ![](vista-imaging-exchange-vix-installation-guide/082.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/083.png) displays, do the following:
1.  Click Assign (Figure 42).

<span id="_Ref67922200" class="anchor"></span>Figure : Apache Tomcat Service Account Password

![](vista-imaging-exchange-vix-installation-guide/084.png)

26. In the dialog box that displays enter the Windows service account password that you previously prepared in *Preparing Passwords, Activating Components, and Staging Files.* Then click OK.
- The password is case sensitive, must contain at least fourteen (14) alphanumeric characters, and must contain at least one capital letter and one number.
27. Wait until the status icon for the service account changes to ![](vista-imaging-exchange-vix-installation-guide/085.png).
57. On the same page, check the line that indicates the state of VIX security certificate. Verify ![](vista-imaging-exchange-vix-installation-guide/086.png) displays.
58. On the same page, read the line that indicates the state of the LibreOffice installation. If ![](vista-imaging-exchange-vix-installation-guide/087.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/088.png) displays (Figure 43), do the following:
1.  Click Install.
28. Wait until the status icon for LibreOffice changes to ![](vista-imaging-exchange-vix-installation-guide/089.png). (This install of LibreOffice may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref149732622" class="anchor"></span>Figure : VIX Prerequisites - LibreOffice Not Installed

![](vista-imaging-exchange-vix-installation-guide/090.png)

59. On the same page, read the line that indicates the state of the PowerShell installation. If ![](vista-imaging-exchange-vix-installation-guide/091.png) displays, skip to the next step. If ![](vista-imaging-exchange-vix-installation-guide/092.png) displays (Figure 44), do the following:
1.  Click Install.
29. Wait until the status icon for PowerShell changes to ![](vista-imaging-exchange-vix-installation-guide/093.png). (This install of PowerShell may take several minutes to complete. Please be patient, as this step may take a while to complete.)

<span id="_Ref149732716" class="anchor"></span>Figure : VIX Prerequisites - PowerShell Not Installed

![](vista-imaging-exchange-vix-installation-guide/094.png)

60. Once PowerShell is installed, the Install the VIX Prerequisites page will update with a ![](vista-imaging-exchange-vix-installation-guide/095.png) icon. Confirm that all the icons are ![](vista-imaging-exchange-vix-installation-guide/096.png) and click Next (Figure 45).

<span id="_Ref67922653" class="anchor"></span>Figure : All VIX Prerequisites Installed or Configured

![](vista-imaging-exchange-vix-installation-guide/097.png)

61. If you want to keep your existing locations for the VIX configuration files and the VIX cache, and the Create buttons are grayed out, skip to the next step.

    If you want to change the locations for the VIX configuration files and the VIX cache, select the “C:\\ drive for VixConfig folder and the appropriate VIX cache drive for the VixCache folder for your site. Ensure the VIX cache drive correctly points to the drive letter that is currently being used, for example, “E:\VIXCache” as displayed in Figure 46. For each folder, click Create to confirm and create the folders.
62. If you want to change the location or need to update the location, ensure the VIX log archive drive correctly points to the drive letter currently being used, for example, “E:\ImagingArchivedLogs” as displayed in Figure 46 and click either Create or Update. Then, click Next.

    If you want to keep the existing locations for the VIX log archive, and the Create or Update button is grayed out, click Next.

    NOTE: It is necessary to click Update if Apache Tomcat was installed on the VIX Prerequisites page.

    NOTE: It is suggested to use the same local drive for the VIX Cache and VIX log archive.

<span id="_Ref149640384" class="anchor"></span>Figure : VIX Cache, Configuration, and Log Archive Folder Creation

![](vista-imaging-exchange-vix-installation-guide/098.png)

63. In the Specify the VistA and Email Configuration, specify the access and verify codes for the account with the VistA credentials. If the email address(es) has changed, specify the email address(es) that gets notifications for invalid credentials. You can enter several email addresses, separated by a comma. Click Confirm (Figure 47).

    NOTE: Hidden/asterisk and plain text forms of the access and verify codes can by toggled. Click Show to show the plain text forms and click Hide to show the hidden/asterisk forms.

    NOTE: The VIX uses this account for periodic processing of ROI disclosure requests and DICOM SCP query retrieve requests. The account must be valid VistA credentials with the settings described in *Appendix D: Service Account Settings*.

    NOTE: The VIX sends an email notification to the address or addresses specified if the ROI periodic processing credentials are expired or invalid.

<span id="_Ref67922887" class="anchor"></span>Figure : Specify the VistA and Email Configuration - Before Confirm

![](vista-imaging-exchange-vix-installation-guide/099.png)

64. In the Specify the VistA and Email Configuration, after it confirms the configuration, Next becomes available. Click Next (Figure 48).

    NOTE: During VistA Configuration validation, the VIX installation program checks the information. If the installation program detects an error, it displays a tooltip with information about the error.

<span id="_Ref67922967" class="anchor"></span>Figure : Specify the VistA and Email Configuration - After Confirm

![](vista-imaging-exchange-vix-installation-guide/100.png)

65. In the Specify the MUSE Configuration, verify if the MUSE settings have not changed since the prior installation and if you want to keep the existing values. If the MUSE settings were changed via the configuration file (MuseDataSource-1.0.Config) and the VIX Installer has not ran since, it is necessary to click Confirm.

    If changes are needed, if enabling the MUSE, check Enable and configure MUSE. Specify the MUSE site number, server host, username, password, port, and protocol. If changes are needed, please refer to *Appendix A: Enable* MUSE Functionality for additional information to assist with the MUSE configuration. If disabling the MUSE, uncheck Enable and configure MUSE.

    After applying any changes for the MUSE settings click Confirm (Figure 49).

    NOTE: Hidden/asterisk and plain text forms of the username and password can by toggled. Click Show to show the plain text forms and click Hide to show the hidden/asterisk forms.

    NOTE: It is expected that the site administrator is aware of all needed entries in the MUSE configuration, including the MUSE Site Number, Host, Username, Password, Port, and Protocol if changes are needed. One method to obtain the MUSE site number, host, port, and username is from the Background processor discussed in *Appendix A: Enable* MUSE Functionality. If the password is not documented in existing site VistA Imaging documentation or if not available, please contact the local BioMed team or MUSE administrator. The default standard MUSE port is <span class="mark">REDACTED</span> and protocol is http. The default MUSE™ NX port is <span class="mark">REDACTED</span> and protocol is https. Contact the local BioMed team or MUSE administrator if the MUSE port and protocol are not known.

<span id="_Ref92798980" class="anchor"></span>Figure 49: Specify the MUSE Configuration - Before Confirm

![](vista-imaging-exchange-vix-installation-guide/101.png)

66. In the Specify the MUSE Configuration, Next becomes available after Confirm was clicked in the prior step or if the MUSE configuration was already confirmed in a prior installation and the MUSE configuration settings have not changed. Click Next (Figure 50).

    NOTE: During MUSE Configuration validation, the VIX installation program checks the information. If the installation program detects an error, it displays a tooltip with information about the error.

<span id="_Ref92798994" class="anchor"></span>Figure : Specify the MUSE Configuration - After Confirm

![](vista-imaging-exchange-vix-installation-guide/102.png)

67. On the Install the VIX page (Figure 51), if in Developer Mode (selected after clicking the lower left corner of the VIX Service Installation Wizard in the grey notch) a check box appears to “Update server.xml as if new installation.”. This checkbox can be checked if changes are being made to the Specify Site and Site Service Information a page since the last installation.

    NOTE: Only use Developer mode and checkbox in the event that changes are needed to the Site Service or Site Information.

<span id="_Ref135990144" class="anchor"></span>Figure : Begin the VIX and VIX Viewer/Render Services Install Developer Mode

![](vista-imaging-exchange-vix-installation-guide/103.png)

68. On the Install the VIX page (Figure 52), click Install. (The information on this page is saved in C:\Program Files (x86)\VistA\Imaging\VIXInstaller for future reference or troubleshooting.) This starts the installation process of the VIX and the VIX Viewer/Render Services.

<span id="_Ref92796918" class="anchor"></span>Figure : Begin the VIX and VIX Viewer/Render Services Install

![](vista-imaging-exchange-vix-installation-guide/104.png)

1.  Wait a moment and then click Configure Viewer/Render (Figure 53).

<span id="_Ref67922433" class="anchor"></span>Figure : VIX Viewer/Render Info Dialog Screenshot

![](vista-imaging-exchange-vix-installation-guide/105.png)

30. Verify the following settings:
1.  Verify the viewer port number is <span class="mark">REDACTED</span>.
2.  Verify the trusted client port is <span class="mark">REDACTED</span>.
3.  Verify the Render Service \> Port Number is <span class="mark">REDACTED</span>.
4.  Verify Site Service \> Host Name is localhost.
5.  Verify Site Service \> Port Number is <span class="mark">REDACTED</span>.
6.  Verify VIX Service \> Host Name is localhost.
7.  Verify Database \> Instance Name is C:\Program Files\VistA\Imaging\VIX.Render.Service\Db\SQLiteDb.db.
8.  Verify the image cache directory drive is the dedicated VIX cache drive. (i.e., “E:\VIXRenderCache").
31. If setting values were modified, click the Save Configuration button in the top right corner, otherwise skip to the next step.

    NOTE: The ‘Save Configuration’ button does not activate unless you changed the configuration (Figure 54).

<span id="_Ref67922577" class="anchor"></span>Figure : Save/Configuration Button

![](vista-imaging-exchange-vix-installation-guide/106.png)

32. Click OK.
33. The installation updates the VIX Viewer/Render Services will be updated in the background. Then the VIX installation finishes. This takes up to over five minutes to complete.
69. During the final install, a PowerShell script utility pops up (Figure 55) to perform additional install tasks and closes when complete.

    NOTE: The PowerShell pop-up performs various configuration and certificate tasks and executes patch-specific post-scripts.

    NOTE: If the MUSE service is not enabled, the PowerShell pop-up may display a red error message in the MUSE check section. See *Appendix A: Enable MUSE Functionality*.

<span id="_Ref67988147" class="anchor"></span>Figure : PowerShell Pop-up Script Top Portion

![](vista-imaging-exchange-vix-installation-guide/107.png)

70. When the installation completes, the VIX automatically starts the Tomcat, Viewer, and Render services. Click Finish to exit the wizard (Figure 56). The VIX Service Installation Wizard closes.

<span id="_Ref67988224" class="anchor"></span>Figure : VIX Installation Complete

![](vista-imaging-exchange-vix-installation-guide/108.png)

71. Continue to *[Post-Installation for New VIX Installations and Updating Existing VIX Installations](#_Verifying_VIX_Operations).*

# Post-Installation for New VIX Installations and Updating Existing VIX Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Apply Security Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The .NET 4.8 framework installed with the VIX might not include the latest security updates. If updates are pushed to your server, you may skip this step. If updates are not pushed, perform the following in Windows:

1.  Right-click Start.
2.  Left-click Search.
3.  Type Settings.
4.  Left-click Settings.
5.  Left-click Update & Security.
6.  In Windows Update, install any available .NET Framework 4.8 Knowledge Base (KB) updates.

    NOTE: For upgrade installations, the latest security update for .NET Framework 4.8 may already be installed.

    NOTE: Please avoid updating the pre-requisites (Java, Tomcat, LibreOffice, or PowerShell 7) outside of the VIX Installation Wizard. The Vista Imaging Patch MAG3.0\*358 VIX and VIX Service Installation have been thoroughly tested with the specific versions (see Figure 45) included in the patch. The VIX Service Installation is explicitly designed to deploy the versions included in the patch. Updating any of these Java, Tomcat, LibreOffice, or PowerShell 7 components outside of the VIX Installation Wizard may negatively affect VIX functionality.

## Verifying Installation/Upgrade is Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that your installation is complete by obtaining the current version (Figure 57). Follow these steps:

1.  Go to the VIX homepage: https://*FQDN of VIX server*/
72. The current version is listed in the format XX.XXX.X.X. The first two digits represent Version 3.0 of the VistA Imaging system. The next three digits are the number of the latest patch that has affected the VIX. This patch number should match the number of the VIX component you have most recently installed.

<span id="_Ref67988700" class="anchor"></span>Figure : VISA Version Verification

![](vista-imaging-exchange-vix-installation-guide/109.png)

> **NOTE:** Alternatively go to https://*FQDN*:<span class="mark">REDACTED</span>/vix/viewer/version to obtain the current version.

73. Verify VIX Viewer and VIX Render services are running (Figure 58).

<span id="_Ref67988756" class="anchor"></span>Figure : VIX Viewer and Render Services Running

![](vista-imaging-exchange-vix-installation-guide/110.png)

74. Verify that you have 10 Hydra IX Processor and 5 Hydra VistA Worker processes running (Figure 59):

<span id="_Ref67988871" class="anchor"></span>Figure : 10 Hydra IX Processor and 5 Hydra VistA Worker Processes Running

![](vista-imaging-exchange-vix-installation-guide/111.png)

## Verifying VIX Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a VIX is installed and is registered with the Image Exchange Service (not needed if VIX is only being updated), Clinical Display and ISI Rad workstations automatically start using the VIX.

- Clinical Display begins sending requests for remote data to the VIX immediately. No configuration changes are required for Clinical Display to start using the VIX.
- ISI Rad needs some local configuration changes to enable some of its VIX-supported capabilities; refer to the ISI Rad documentation for details.
- JLV Image Viewing does not require any additional configuration changes. The Image Viewer should launch without issue and be able to display MUSE images.

  NOTE: Please use either Chrome or Edge on your Government Furnished Equipment (GFE) or VIX server to verify and perform VIX Operations.

### Verifying Access to the VIX Tools and VIX Transaction Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIX administrators can use the VIX Tools as described in the *VIX Administrator’s Guide* with a listing of available tools in Appendix B: VIX Tools of the VIX Administrator’s Guide.

To access the VIX Tools, navigate to <span class="mark">REDACTED</span>/vix/viewer/tools to be prompted to login (Figure 60). Use a VistA account with the MAG VIX ADMIN security key and INITIAL to log in.

<span id="_Ref103252625" class="anchor"></span>Figure : Login Page

![](vista-imaging-exchange-vix-installation-guide/112.png)

The VIX transaction log can be used to monitor VIX activities. Once logged in to the VIX Tools page, access to the transaction log at https://*FQDN*:<span class="mark">REDACTED</span>/Vix/secure/VixLog.jsp is available  
(where *FQDN* is the fully qualified domain name of the VIX server) (Figure 61).

<span id="_Ref103250687" class="anchor"></span>Figure : VIX Tools Page

![](vista-imaging-exchange-vix-installation-guide/113.png)

If you cannot access the transaction log, verify that the VIX service is running.

If the VIX is running, but you cannot access the transaction log, ensure that ports <span class="mark">REDACTED</span> on the VIX server are not blocked. Possible culprits of a blocked port include antivirus firewalls and modifications to ACLs (Access Control Lists).

For detailed information about the transaction log contents, refer to the [*VIX Administrator’s Guide.*](https://www.va.gov/vdl/application.asp?appid=105)

### Spot-Checking VIX Image Delivery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows different ways you can spot-check displaying remote images.

1.  Using JLV:
    1.  Select an image with a camera icon, and launch the Image Viewer to display the selected image.
    2.  Select the “Cardiology Studies VA MUSE Only” widget and view a MUSE Electrocardiogram (EKG) image by selecting the camera icon. This launches the Image Viewer to display the selected MUSE EKG image.
    3.  Turn on the Display DOD Image User Preference in JLV. View a Department of Defense (DoD) image by selecting the camera icon. This launches the Image Viewer to display the selected DoD image.
75. On the Clinical Display workstation:
    1.  Select a patient with remote images.
    2.  If it is not visible already, display the Abstracts area to display an abstract for one of the remote images.
    3.  Right-click the abstract for the remote image and open the Image Information Advanced window.
    4.  In the Image Information Advanced window, check the IEN (Internal Entry Number) value or Image Number. If the value starts with “urn”, the remote image was retrieved by the VIX.

## DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to *Appendix B: DICOM SCP Configuration* to configure the DICOM SCP.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Resuming an Interrupted VIX Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have had to interrupt or cancel an in-progress VIX installation, you can resume the installation.

> **NOTE:** If you re-run MAG3_0P358_VIX_SETUP.msi, you are repeating the installation of the VIX Service Installation Wizard software, not the installation of the VIX itself. If you do this, click Cancel, choose Yes when prompted for confirmation, and then exit the installer. Then restart the VIX installation following the steps below.

### Resuming Installation (single server VIX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log onto the VIX server as an administrator.
76. Run the VIX Service Installation Wizard as an administrator (Figure 62 shows this for a server with Windows Server 2019).
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> NOTE: If the VIX Service Installation Wizard does not appear in the Search bar as in Figure 62 logout of the Windows administrator account session and log back in.

> NOTE: The VIX Service Installation Wizard may alternatively be run as an administrator by performing either of the following:

- On the Desktop, find the VIX Shortcuts folder and doubleleft-click. In the folder that opens, right-click VIX Installer and left-click Run as administrator.
- Open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

<span id="_Ref67989744" class="anchor"></span>Figure : Run the VIX Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/114.png)

77. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
78. Follow the steps for a new VIX installation, see *New VIX Server Installation* section, or for updating a VIX, see *Updating an Existing VIX* section.

## Using the VIX Service Installation Wizard to Reconfigure the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must re-execute the VIX Service Installation Wizard if you need to:

- Change the drive where the VixCache, VixConfig, VixTxDb, and/or ImagingArchivedLogs folders are located. It is recommended that the VixCache, VixTxDb, and ImagingArchivedLogs folders reside on the same shared drive.
- Change the VIX configuration to use a different local VistA hostname or port number.

Using the VIX Service Installation Wizard to reconfigure VIX is like the steps for updating a VIX, except the process is much faster since no actual software is being installed.

TIP: Changing a VIX cache location or local connection information should take about 5 minutes.

### Reconfiguring a VIX Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Review the information in the *Scheduling Downtime and Impact of a VIX Update* section, and schedule downtime and notify appropriate groups of the downtime.
79. Run the VIX Service Installation Wizard as an administrator (Figure 63 shows this for a server with Windows Server 2019).
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> NOTE: If the VIX Service Installation Wizard does not appear in the Search bar as in Figure 63 logout of the Windows administrator account session and log back in.

> NOTE: The VIX Service Installation Wizard may alternatively be run as an administrator by performing either of the following:

- On the Desktop, find the VIX Shortcuts folder and doubleleft-click. In the folder that opens, right-click VIX Installer and left-click Run as administrator.
- Open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

<span id="_Ref187996591" class="anchor"></span>Figure : Run the VIX Service Installation Wizard

![](vista-imaging-exchange-vix-installation-guide/115.png)

80. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
81. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*358 VIX” and click Next.
82. Then, when prompted to do so, click Uninstall version 30.358.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.).
83. When the Uninstall is complete, Press Next to continue displays in the VIX Service Installation Wizard, click Next.
84. Click Next until the “Specify the VA Site the VIX will service” page displays.
85. On this page, verify that the Site Number box shows your STATION NUMBER (field (#99) in the INSTITUTION file (#4) of your site, the information is in FileMan in VistA). Then, click the Lookup Server Address.
86. Verify the correct hostname and port number for the local VistA system displays. Then, click Next.
87. When the Install the VIX Prerequisites page displays, click Next. (All prerequisites are installed already.)
88. On the “Specify the VA Site the VIX will service” page, do one of the following:
1.  If you are changing the location of the VIX cache and configuration files, select the new drive for each. Click Create. Then, click Next.
2.  If you are NOT changing the location of the VIX cache and configuration files, click Next.
89. In the Specify the VistA and email Configuration, do the following:
1.  Enter the access and verify codes. If you are changing the email address or addresses enter them. Click Confirm.
2.  Click Next.
90. In the “Specify the MUSE Configuration” page do one of the following:
1.  If you are changing the MUSE configuration, enter the configuration settings. Click Confirm. Then click Next.
34. If you are NOT changing the location of the MUSE configuration, click Next.
91. In the Install the VIX page, click Install.
92. Wait a moment and then click Configure Viewer/Render.
1.  If you are changing the Viewer/Render configuration, enter the configuration settings. Click Save Configuration. Then click OK.
35. If you are NOT changing the Viewer/Render configuration, click OK.
93. Wait until the installation is complete and click Finish.
94. Re-execute the Post-Installation instructions, see *Post-Installation for New VIX Installations and Updating Existing VIX Installations* section.
95. Check the apachetomcat user permissions on the YOUR_DRIVE_LETTER:\VixCache folder. If Modify and Write access rights are not present, run the tomcat permissions script, see *Tomcat User Permissions* section.

## Tomcat User Permissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If encountering file system access errors after VIX Installation, start-up, slowness, or cache not-purged issues, please refer to Appendix C: VIX Utility Scripts of the VIX Administrator’s Guide, for instructions to run the tomcat permissions script (permission_fixer.ps1).

To check the modify and write access on the YOUR_DRIVE_LETTER:\VixCache folder for the apachetomcat user permissions, right-click on the folder, select Properties \> Security then select the apachetomcat user (Figure 64). If the Modify and Write access rights are not present for the apachetomcat user, run the tomcat permissions script (permission_fixer.ps1).

<span id="_Ref43717706" class="anchor"></span>Figure : VixCache Properties Check

![](vista-imaging-exchange-vix-installation-guide/116.png)

## Java Management Extensions (JMX)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If encountering errors starting the Tomcat service or errors during VIX Installation related to the jmxremote.password file, please refer to Appendix C: VIX Utility Scripts of the VIX Administrator’s Guide, for instructions to run the Java Management Extensions (JMX) script (set_jmx_permissions.ps1).

## VIX Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you encounter problems installing the VIX, please call the Enterprise Service Desk (ESD) at <span class="mark">REDACTED</span>.

# Back Out/Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Stopping the VIX Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes stopping any currently running services to assist with the back out/uninstall for complete VIX removal.

(Server Manager \| Tools \| Component Services \| Services (Local), or Task Manager \| Services \| Open Services), sort the Name column, and stop each VIX service shown below by selecting Stop (Figure 65).

- Tomcat9
- VIX Render Service
- VIX Viewer Service

Always use the Window ‘Task Manager’ to monitor the processing tasks as needed.

<span id="_Ref98578973" class="anchor"></span>Figure : Stopping VIX Viewer Service

![](vista-imaging-exchange-vix-installation-guide/117.png)

## Back Out/Uninstall Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this section addresses three possible cases that involve uninstalling a VIX:

- Troubleshooting
- Relocation onto a different server
- Decommission

Each of these scenarios is outlined in the following sections.

### Uninstall/Restore as part of Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to remove and then immediately reinstall the VIX on the same server for troubleshooting purposes, you need to do the following:

1.  Locate the product serial number for the Laurel Bridge software that is bundled with the VIX. This number is in the license paperwork that was provided by <span class="mark">REDACTED</span> when the VIX was set up.

    NOTE: You need to re-enter this serial number as a part of the VIX installation process.
96. Run the VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.
97. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*358 VIX” and click Next.
98. Then, when prompted to do so, click Uninstall version 30.358.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
99. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
100. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 VIX Service Installation Wizard.
101. Re-execute the VIX installation as if for a new VIX, see *New VIX Server Installation* section.
102. Re-execute the Post-Installation instructions, see *Post-Installation for New VIX Installations and Updating Existing VIX Installations* section.
103. Check the apachetomcat user permissions on the YOUR_DRIVE_LETTER:\VixCache folder. If Modify and Write access rights are not present, run the tomcat permissions script, see *Tomcat User Permissions* section.

### Relocating a VIX onto a New Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to remove all traces of the VIX from the old server and set up the VIX on a new server, you need to do the following:

1.  Contact the <span class="mark">REDACTED</span> mail group and arrange to have the existing Laurel Bridge DCF toolkit licenses transferred to a new server.
104. Validate the new VIX server as described in the *Selecting and Validating the VIX Server* section.
105. Manually remove the VIX as described in the *Uninstalling the VIX* section below.
106. Re-execute the VIX installation as if for a new VIX, see *New VIX Server Installation* section.

### Decommissioning a VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to completely decommission a VIX and not replace it by another VIX, do the following:

1.  Notify the <span class="mark">REDACTED</span> mail group that the Laurel Bridge license seats used by your site are no longer being used.
107. Contact <span class="mark">REDACTED</span> mail group to have the VIX retired and the VIX removed from the site service.
108. Manually remove the VIX as described in the *Uninstalling the VIX* section below.
109. In VistA, remove the MAG VIX ADMIN security key from the accounts that have this key assigned.

## Uninstalling the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps explain how to completely remove a VIX and all its supporting components (toolkits, runtime environments, etc.) from the server where the VIX is installed:

![](vista-imaging-exchange-vix-installation-guide/118.png)These steps remove the VIX and permanently delete the VIX cache.

Depending on the VIX server configuration and operating system, the specifics of removing the VIX vary, but the general process is as follows:

1.  Stop the VIX service. See Section 6.1.
110. Remove VIX-related applications, accounts, directories, and variables.

These steps do not require a server reboot and can be performed while the rest of the Imaging system is active.

### Remove VIX related applications, accounts, directories, and variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After stopping (and/or removing) the VIX services as described in the previous sections, you need to remove VIX software and settings.

These steps presume you are already logged in as an administrator on the server where the VIX service used to reside.

These steps cover all supported VIX configurations.

1.  Use Windows Explorer to navigate to the drive where the VIXCache is located, and delete the following folders:

    *shared drive letter*:\VixCache
111. Delete the VixRenderCache, ImagingArchivedLogs, and VixTxDb folders, which are usually on that same drive.
112. Use Windows Explorer to delete the following directories:

     C:\\ DCF_RunTime_x64  
     C:\Program Files\Java\jre-1.8-431
113. If you are removing the VIX permanently, also delete the following folders:

     ![](vista-imaging-exchange-vix-installation-guide/119.png) SKIP THIS STEP if you are uninstalling and reinstalling the VIX on the same server for troubleshooting purposes. If you delete these folders, you need to recreate the VIX configuration.

     C:\VixBackup

     C:\VixConfig  
     C:\VixCertStore
114. Open the window used to remove programs.
1.  On Windows, click Start \| Control Panel. Under the Programs item, click Uninstall a program.
36. Remove these four programs (no reboot required):
- Apache Tomcat 9.0.89
- Java (TM) 1.8.0. Update 431
- LibreOffice 24.2.5
- VIX Service Installation Wizard
115. In Windows Explorer, right-click the Local Disk (C:) folder, select Properties. Then, select the Security tab.
116. Select the apachetomcat user and click Remove.
117. Click OK to close the Properties dialog box and click Yes when asked if you want to continue.

     NOTE: If one or more “Error applying security” messages display, click Continue until they are all closed.
118. Open the Computer Management/Server Manager window.
1.  On Windows, right-click Computer on the desktop. Then, click Manage.
119. In the tree on the left side of the window, navigate to Users.
1.  On Windows, go to Server Manager/Configuration/ Local Users and Groups/Users.
120. On the right side of the window, right-click the apachetomcat user, click Delete, and click Yes when you are asked for confirmation.
121. Open the System Properties dialog box.
1.  On Windows, right-click Computer on the desktop. Then, click Properties. Then on the left side of the System window, click Advanced system settings.
122. In the Advanced tab, click Environment Variables.
123. In the System variables list near the bottom of the dialog, delete the following variables:

     CATALINA_HOME DCF_USER_CLASSES  
     DCF_BIN DCF_USER_LIB  
     DCF_CFG DCF_USER_ROOT  
     DCF_CLASSES LD_LIBRARY_PATH  
     DCF_LIB OMNI_BIN  
     DCF_LOG OMNI_LIB  
     DCF_PLATFORM OMNI_ROOT  
     DCF_ROOT vixcache  
     DCF_TMP vixconfig  
     DCF_USER_BIN vixtxdb
124. In the System variables list, select the Path system variable. Then, click Edit.
     1.  In the Variable value box, delete the following substrings:
     2.  C:\DCF_Runtime_x64\bin  
         C:\DCF_Runtime_x64\lib  
         C:\Program Files\Java\jre-1.8-431\bin
     3.  After removing the substrings, click OK. Then click OK twice more to close the Environment Variables and System Properties dialog boxes.
125. VIX removal is complete.

## Rollback and Back Out of MAG\*3.0\*358

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*358 VIX and back out the VIX to a prior version perform the following steps:

1.  Run the MAG\*3.0\*358 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

    NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.
126. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*358 VIX” and click Next.
127. Then, when prompted to do so, click Uninstall version 30.358.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
128. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
129. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 VIX Service Installation Wizard.
130. Verify backup copies of critical configuration file folders exist within C:\VIXBackup\P348\YYYYMMDDHHMMSS. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Backups exist of the following:
- C:\DCF_RunTime_x64\cfg
- C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf
- C:\Program Files\VistA\Imaging\VIX.Config
- C:\VixConfig
- C:\VixCertStore
- Install logs from C:\Program Files (x86)\Vista\Imaging\VixInstaller
131. Stop each VIX service: Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 65) as described in Section 6.1.
132. Uninstall any Java version later than and including 8.0.431 using the Control Panel.
133. Uninstall any LibreOffice version later than and including 24.2.5 using the Control Panel.
134. Install the previous version of VIX that included an MSI file, which was included in MAG\*3.0\*348 (find it on the VA SFTP site or from a local backup folder). Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P348_VIX_SETUP.msi file and click on Install.
37. When the Welcome page displays, click Next.
38. When the Confirm Installation page displays, click Next.
39. When the Installation Complete screen displays, click Close.
135. Run the MAG\*3.0\*348 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

136. Once the MAG\*3.0\*348 VIX Service Installation Wizard is running, click Next and continue with the installation steps described in detail in the *MAG\*3.0\*348 VIX Installation Guide* as if it is an upgrade MAG\*3.0\*348 install.
137. Upon completion of the MAG\*3.0\*348 installation, if necessary, configuration files in C:\VIXBackup\P348\YYYYMMDDHHMMSS\VixConfig can be copied to C:\VixConfig as needed (e.g., MuseDataSource-1.0.Config) to restore the prior version. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     If configuration files are to be restored, first stop each VIX service: Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service.
138. Stop Tomcat9, by opening Windows Services and then selecting Stop.
139. Also install MAG\*3.0\*357 (find it on the VA SFTP site or from a local backup folder) or otherwise skip to the next step. Follow the installation steps described in MAG3_0P357_Patch_Instructions.txt. Use either the automated script (MAG3_0P357_VIX_Deployer.ps1) or manual update steps.
140. Start Tomcat9, by opening Windows Services and then selecting Start.
141. Reboot your server.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the version of Java after rollback by running Windows ‘Programs and Feature’, is Java 8.0.371
142. Verify the version of Tomcat after rollback by running Windows ‘Programs and Features’, is Tomcat 9.0.75
143. Verify the version of the VIX by going to the VIX homepage <span class="mark">REDACTED</span> using a browser e.g.: Chrome or Edge.

# Appendix A: Enable MUSE Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MUSE configuration is specified during VIX Installation in the Specify the MUSE Configuration page. On this page, set or update if needed, the value for the MUSE site number of the MUSE server that contains EKGs for your facility, the value of the MUSE host, the value of the MUSE username, the password for the MUSE obtained from existing site VistA Imaging documentation (if not available, please contact the local BioMed team or MUSE administrator for the password), the MUSE port, and the MUSE protocol.

Enabling the MUSE functionality is only needed to be performed if this is a new installation, or in the case of an upgrade installation, it is determined it is not enabled and it is desired to enable it by following *Has the MUSE functionality already been configured to be enabled?*Has the MUSE functionality already been configured to be enabled?

- To determine if MUSE functionality is already configured, observe the behavior when the MUSE Configuration page loads during VIX Installation.
- No, it is not enabled. A checkbox does <u>not</u> appear next to Enable and configure MUSE. Continue with this Appendix to perform the steps to enable MUSE functionality if it is desired to enable the MUSE interface.
- Yes, it is enabled. A checkbox appears next to Enable and configure MUSE and values for a real MUSE site number, host, username, password, port, and protocol are pre-populated and present for each entry on the page (Figure 66). The MUSE functionality is already enabled. There is no reason to perform the steps in this Appendix unless reconfiguring.

<span id="R_F_srvr_port_SPECIFY_THE_MUSE_CONFIGU_0" class="anchor"></span>Figure : Specify the MUSE configuration Enable and configure MUSE pre-populated

![](vista-imaging-exchange-vix-installation-guide/120.png)

- Alternatively, a manual check of the MuseDataSource-1.0.Config file may be used to determine if MUSE functionality is already configured. Open the MuseDataSource-1.0.Config file located in C:\VixConfig. Run Notepad, Notepad++, or WordPad as an administrator and then open the file.
- No, it is not enabled. If the MuseDataSource-1.0.Config file located in C:\VixConfig is similar to the template displayed in Figure 67, continue with this Appendix to perform the steps to enable MUSE functionality if it is desired to enable the MUSE interface.
- Yes, it is enabled. If the MuseDataSource-1.0.Config file located in C:\VixConfig is <u>not</u> similar to the template displayed in Figure 67 (i.e. a real MUSE site number, host, username, password, port, and protocol are present), the MUSE functionality is already enabled. There is no reason to perform the steps in this Appendix unless reconfiguring.

> NOTE: A manual check of the MuseDataSource-1.0.Config may not always be reliable.

<span id="_Ref112743437" class="anchor"></span>Figure : Sample MuseDataSource-1.0.Configure File for One Server (MUSE ENABLED FOR JLV VIX Image Viewer)

![](vista-imaging-exchange-vix-installation-guide/121.png)

One of the methods identified to obtain the values of the MUSE site number, host, port, and username is from the Background Processor (BP) Queue Processor. For more information on the Background Processor, please see the [*VistA Imaging System Background Processor User Manual*](https://www.va.gov/VDL/application.asp?appid=105). If the site is running the BP Queue processor, use the below steps to obtain the values of the MUSE site number, host, and username.

1.  From the Background Processor Queue Processor (Figure 68) menu bar, select Edit \> Network Location Manager to open the Network Location Manager window.

<span id="_Ref112743394" class="anchor"></span>Figure : BP Queue Processor

![](vista-imaging-exchange-vix-installation-guide/122.png)

144. Click on the EKG tab in the Network Location Manager window. A listing of the network location of available MUSE servers appears (Figure 69).

     NOTE: Pay attention to the Operational Status of available MUSE servers. Only use the MUSE or MUSE NX server that is <u>On-Line and contains EKGs of the local site.</u>

<span id="_Ref112743346" class="anchor"></span>Figure : EKG Tab in Network Location Manager in BP Queue Processor

![](vista-imaging-exchange-vix-installation-guide/123.png)

145. To obtain details for a MUSE server, right-click on the server and run Properties to launch Network Location Properties. The network share and username for that MUSE server displays (Figure 70).
146. Use the details from the Network Location Properties tab in the BP Queue Processor for the MUSE server that is Operational to obtain the MUSE site number, host, port number, and username.

<span id="_Ref112743241" class="anchor"></span>Figure : Network Location Properties in BP Queue Processor

![](vista-imaging-exchange-vix-installation-guide/124.png)

> Under the “Storage Type” on the right side, the MUSE site number is listed under “Site \#” under “MUSE”. The Fully Qualified Domain Name of the MUSE server for the host entry is listed under “Network Share” between \\ and \\ (Figure 70). The port number (with \\ before and after) is appended to the Fully Qualified Domain Name. The MUSE site username for the username entry displays under “User Name” under “Network Credentials Security”.

> Note the entries for the MUSE site number, host, port number, and username for the MUSE server that is Operational. The MUSE site password can be obtained from the existing site VistA Imaging documentation (if not available, obtain your MUSE site password from the local BioMed team or MUSE administrator).

> NOTE: The default standard MUSE port is <span class="mark">REDACTED</span> and protocol is http while the default MUSE™ NX port is <span class="mark">REDACTED</span> and protocol is https. If using MUSE™ NX, under the “Storage Type” on the right side the Network Location Properties tab in the BP Queue Processor, “NX” is selected under the “Vers \#”.

# Appendix B: DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Perform this step as part of the *Post-Installation for New VIX Installations and Updating Existing VIX Installations.*

The DICOM SCP enables Commercial Picture Archive and Communication System (PACS) and various query retrieve devices at VA facilities to get remote VistA images through the use of DICOM C-FIND and C-MOVE.

Henceforth, this Appendix refers to the Commercial PACS and query retrieve devices as a DICOM SCP client.

You need to configure the DICOM SCP if this is a new installation, or in the case of an upgrade installation, you determine it is not yet configured by following *Has the DICOM SCP functionality already been configured?*Has the DICOM SCP functionality already been configured?

- To determine if DICOM SCP functionality is already configured, open the ae_title_mappings file located in the folder cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default). Run, Notepad, Notepad++, or WordPad as an administrator, and then open the file.
- No, it is not configured. If the ae_title_mappings file located in the folder cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default) is like the template displayed in Figure 71, continue with this Appendix to perform the steps to configure DICOM SCP functionality.
- Yes, it is configured. If the ae_title_mappings file located in the folder cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default) is <u>not</u> like the template displayed in Figure 71 (i.e. a real DICOM SCP host IP, port, and AE Title are present), the DICOM SCP functionality is already configured. There is no reason to perform the steps in this Appendix unless reconfiguring.

Additional details on the DICOM SCP Configuration are provided in the “*Configure DICOM SCP Functionality*” section in the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105).

## Application Entity (AE) Titles Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes both the calling and called Application Entity (AE) Titles that must both be configured for DICOM SCP to work. It is necessary to configure both the AE Titles on the VIX server with those of the DICOM SCP client and also to configure the AE Titles on the DICOM SCP client with those of the VIX server.

> **NOTE:** The port for the host for DICOM SCP must be configured as a bi-directional open port in any firewall.

### Laurel Bridge AE Titles Configuration on VIX/CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to configure the AE Titles configuration file ae_title_mappings located in the folders cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default). Open the ae_title_mappings file to perform edits. Run, Notepad, Notepad++, or WordPad as an administrator, and then open the file.

For each DICOM SCP client, the AE Title name and its host/port attributes must be set. For each DICOM SCP client, update the following entries for the AE Titles configuration file (see Figure 71):

1.  Set the IP address for the host for the DICOM SCP client, (after host = line 11).
147. Set the port for the DICOM SCP client where the DICOM SCP is used for the C-STORE operation, (after port = line 12).
148. Set the AE Title the DICOM SCP client is using to communicate with the DICOM SCP (calling AE) (inside \[ \] on line 10 and after ae_title = line 13).

Ensure that each of these lines is uncommented (i.e., remove the \# at the front of the line if present). Save the ae_title_mappings file after updating the entries.<span id="_Ref69391565" class="anchor"></span>

Figure : AE Titles Configuration File (Template)

![](vista-imaging-exchange-vix-installation-guide/125.png)

An example of the ae_title_mappings file updated for one DICOM SCP client is shown in Figure 72.

> **NOTE:** The example in Figure 72 for configuration of one DICOM SCP client is not how an actual VIX site’s ae_title_mappings file is to be configured. This example is for illustrative purposes only.

<span id="_Ref112742877" class="anchor"></span>Figure : AE Titles Configuration File (Example)

![](vista-imaging-exchange-vix-installation-guide/126.png)

For each additional DICOM SCP client, similarly, add lines for the host, port, and ae_title with the correct values as new lines below the prior lines for the prior DICOM SCP client (Figure 73). Save the ae_title_mappings file after updating the entries.

<span id="_Ref112742808" class="anchor"></span>Figure : AE Titles configuration File with Multiple DICOM SCP Clients (Example)

![](vista-imaging-exchange-vix-installation-guide/127.png)

After updating the ae_title_mappings file, as described above, execute the restart script (Restart_VIX_Services.ps1) to restart the Apache Tomcat service, VIX Viewer and VIX Render services, see *Appendix C: Restart Script*.

### AE Titles Configuration on DICOM SCU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the AE Titles configuration on the DICOM SCU. Installation/administration personnel on the VIX server might not be able to perform this configuration and, in which case, must provide the necessary information to the DICOM SCU administration personnel to perform.

The following three pieces of information are needed for the configuration of the DICOM SCU: 1) the IP address for the host for the VIX server, 2) the port of DICOM SCP on the VIX server, and 3) the AE Title of DICOM SCP (called AE).

Many different DICOM SCU vendors exist and each of these systems has their own distinct approach for configuration. If additional information regarding specifics of configuring the DICOM SCU is needed, please reach out to its vendor or consult its documentation.

## Tomcat/ Laurel Bridge DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX install performs some of the configuration for the DICOM SCP automatically with reasonable defaults and predefined entries. Update two entries in the ScpConfiguration.Config file located in C:\VixConfig to configure the DICOM SCP. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

Update the following entries for the DICOM SCP functionality (see Figure 74):

1.  Set the DICOM SCU calling AE title, inside opening and closing aeTitle tags (inside \<aeTitle\> \</aeTitle\> - line 22). Change the value from the default setting of ALL.
149. Set the DICOM SCU IP address inside the opening and closing callingAeIp tags (inside \< callingAeIp\> \</callingAeIp\> - line 23). Change the value from the default setting of 0.0.0.0.

<span id="_Ref112742655" class="anchor"></span>Figure : DICOM SCP Configuration File (Template)

![](vista-imaging-exchange-vix-installation-guide/128.png)

An example of the ScpConfiguration.Config file updated for one DICOM SCP client is shown in Figure 75.

> **NOTE:** The example in Figure 75 for configuration of the aeTitle and callingAeIp is not how an actual VIX site’s ScpConfiguration.Config file is to be configured. This example is for illustrative purposes only.

<span id="_Ref112742452" class="anchor"></span>Figure : ScpConfiguration Configuration File (Example)

![](vista-imaging-exchange-vix-installation-guide/129.png)

If additional changes to the defaults for the Tomcat DICOM SCP Configuration and/or Laurel Bridge DICOM SCP Configuration are desired, see the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105) for details.

> **NOTE:** For each additional DICOM SCP client, insert an additional block of code containing the elements from lines 21 to 49 before current line 50 (Figure 75), as described in the *[VIX Administrator’s Guide](https://www.va.gov/vdl/application.asp?appid=105).*NOTE: If additional updates are needed to the encrypted access and verify codes in the ScpConfiguration.Config file, refer to lines 3 and 4 in Figure 75, for the account with VistA credentials see the section “Modifying the ROI Processing and DICOM Query/Retrieve Parameters of the VIX” in the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105) to update (preferred) or see the section  
“*Reconfiguring a VIX Server*,” in this VIX Installation Guide to perform a reconfigure installation.

# Appendix C: Restart Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix describes how to execute the restart script (Restart_VIX_Services.ps1) to restart the Apache Tomcat service, VIX Viewer service, and VIX Render service.

Perform the following:

1.  Run PowerShell as an administrator (Figure 76).
    1.  Right-click Start.
    2.  Left-click Search.
    3.  Type powershell.
    4.  Right-click PowerShell 7 (x64).
    5.  Left-click Run as administrator.

<span id="_Ref112742276" class="anchor"></span>Figure : Execute Windows PowerShell

![](vista-imaging-exchange-vix-installation-guide/130.png)

150. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
151. Once PowerShell launches, type the command:

     cd "C:\Program Files\VistA\Imaging\Scripts"

     Then press \[ENTER\] to change the working directory to the Scripts folder.
152. Then type the command:

     .\Restart_VIX_Services.ps1

     And press \[ENTER\] to execute the restart script. Wait for the script to complete (Figure 77).

<span id="_Ref112742121" class="anchor"></span>Figure : Windows PowerShell Restart Script

![](vista-imaging-exchange-vix-installation-guide/131.png)

153. Close PowerShell.

# Appendix D: Service Account Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX uses a service account on the local VistA for periodic processing of ROI disclosure requests and DICOM query retrieve SCP requests. The service account may be the same one used by the DICOM Gateway and the Hybrid DICOM Gateway (HDIG). You may also use it to log into the VIX Tools page described in the *Verifying Access to the VIX Tools and VIX Transaction Log* section.

Table 2 lists each VIX site’s current and suggested local VistA service account. The Designated User (DUZ) identifies the service account. The suggested service account enables each site to have a unique name.

The VIX’s service account on its local VistA must have the following SSN format, security keys, secondary menus, a value for the INITIAL field, RAD/NUC med classification, CPRS TAB, and authorized to write med orders. If any setting is missing, update the service account.

> **NOTE:** If unable to update the service account on the local VistA yourself, please create a ticket assigned to the (ESD) Tier 1 group to update the service account on the local VistA. Example text for the ticket appears after the table.

Verify the SSN of the service account on the local VistA is as specified in Table 2. All SSNs begin with 9 to avoid possible collisions with a real SSN issued by the Social Security Administration.

Verify the service account on the local VistA has the following security keys:

- MAG SYSTEM
- MAG VIX ADMIN
- MAG DOD FIX
- RA MGR
- RA VERIFY
- RA ALLOC

Verify the service account on the local VistA has the following secondary menus:

- MAG WINDOWS (All MAG\* RPC's)
- MAG DICOM VISA (DICOM VISA)
- OR CPRS GUI CHART (CPRSChart version x.xx.xxx.x)
- MAG DICOM GATEWAY FULL
- MAG DICOM QUERY RETRIEVE

Verify the service account on the local VistA has a value for the INITIAL field.

Verify the service account on the local VistA has the following RAD/NUC med classification:

- 1      staff
- 4      technologist

Verify the service account on the local VistA has the following CPRS TAB:

-   CPRS TAB: COR
-   EFFECTIVE DATE: \<TODAY

Verify the service account on the local VistA has the following authorized to write med orders:

- YES

  NOTE: To verify the service account on the local VistA has a value for the INITIAL field perform the following:
1.  Access VA FileMan \[DIUSER\] in your VistA instance.
2.  Select Inquire to File Entries \[DIINQUIRE\], then choose the NEW PERSON file (#200).
3.  When prompted "Select NEW PERSON NAME", select your VistA Imaging service account.
4.  Either answer Yes to Standard Captioned Output (followed by No in "Include COMPUTED fields"), or answer No, and then choose the INITIAL field (#1).
5.  The latter just shows the INITIAL field, the former shows all fields. Either way, verify that the results include a value for the account's initials.

    If the service account on the local VistA does not have a value for the INITIAL field set one:
1.  Access VA FileMan \[DIUSER\] in your VistA instance.
2.  Select Enter or Edit File Entries \[DIEDIT\], then choose the New Person file (#200). When prompted "EDIT WHICH FIELD", choose INITIAL (#1).
3.  When prompted "Select NEW PERSON NAME", choose your VistA Imaging service account.
4.  Finally, when you see the "INITIAL" prompt, enter the initials for the user. Enter any appropriate value, such as VSA.

| Site Name                   | Site Number | VIX User Profile SSN               | VIX's Service Account on Local VistA | Suggested VIX's Service Account on Local VistA |
|-----------------------------|-------------|------------------------------------|--------------------------------------|------------------------------------------------|
| Manila, PI                  | 358         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Togus, ME                   | 402         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| White River Junction, VT    | 405         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Montana HCS                 | 436         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Fargo, ND                   | 437         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Sioux Falls, SD             | 438         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Cheyenne, WY                | 442         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Honolulu, HI                | 459         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Wilmington, DE              | 460         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Anchorage, AK               | 463         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Albuquerque, NM             | 501         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Alexandria, LA              | 502         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Altoona, PA                 | 503         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Amarillo, TX                | 504         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Ann Arbor, MI               | 506         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Atlanta, GA                 | 508         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Augusta, GA                 | 509         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Maryland HCS                | 512         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Battle Creek, MI            | 515         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Bay Pines, FL               | 516         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Beckley, WV                 | 517         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Bedford, MA                 | 518         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Big Spring, TX              | 519         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Biloxi, MS                  | 520         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Birmingham, AL              | 521         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Boston HCS                  | 523         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Bronx, NY                   | 526         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Upstate NY HCS              | 528         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Butler, PA                  | 529         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Boise, ID                   | 531         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Charleston, SC              | 534         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Chicago, IL (Westside)      | 537         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Chillicothe, OH             | 538         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Cincinnati, OH              | 539         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Clarksburg, WV              | 540         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Cleveland, OH               | 541         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Coatesville, PA             | 542         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Columbia, SC                | 544         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Miami, FL                   | 546         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| West Palm Beach, FL         | 548         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| North Texas HCS             | 549         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Danville, IL                | 550         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Dayton, OH                  | 552         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Detroit, MI                 | 553         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Eastern Colorado HCS        | 554         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| North Chicago, IL           | 556         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Dublin, GA                  | 557         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Durham, NC                  | 558         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| New Jersey HCS              | 561         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Erie, PA                    | 562         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Fayetteville, AR            | 564         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Fayetteville, NC            | 565         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Black Hills HCS             | 568         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Fresno, CA                  | 570         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| N. Florida/S. Georgia HCS   | 573         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Grand Junction, CO          | 575         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Hines, IL                   | 578         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Houston, TX                 | 580         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Huntington, WV              | 581         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Indianapolis, IN            | 583         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Iron Mountain, MI           | 585         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Jackson, MS                 | 586         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Kansas City, MO             | 589         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Hampton, VA                 | 590         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Las Vegas, NV               | 593         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Lebanon, PA                 | 595         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Lexington, KY               | 596         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Little Rock, AR             | 598         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Long Beach, CA              | 600         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Louisville, KY              | 603         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Loma Linda, CA              | 605         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Madison, WI                 | 607         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Manchester, NH              | 608         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Northern Indiana HCS        | 610         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Northern California HCS     | 612         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Martinsburg, WV             | 613         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Memphis, TN                 | 614         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Minneapolis, MN             | 618         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Central Alabama HCS         | 619         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Hudson Valley HCS           | 620         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Mountain Home, TN           | 621         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Muskogee, OK                | 623         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Tennessee Valley HCS        | 626         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| New Orleans, LA             | 629         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| NY HCS                      | 630         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Northampton, MA             | 631         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Northport, NY               | 632         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Oklahoma City, OK           | 635         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Central Plains HCS          | 636         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Asheville, NC               | 637         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Palo Alto HCS               | 640         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Philadelphia, PA            | 642         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Phoenix, AZ                 | 644         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Pittsburgh HCS              | 646         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Portland, OR                | 648         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Prescott, AZ                | 649         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Providence, RI              | 650         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Richmond, VA                | 652         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Roseburg, OR                | 653         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Reno, NV                    | 654         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Saginaw, MI                 | 655         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| St. Cloud, MN               | 656         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| St. Louis, MO               | 657         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Salem, VA                   | 658         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Salisbury, NC               | 659         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Salt Lake City, UT          | 660         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| San Francisco, CA           | 662         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Puget Sound HCS             | 663         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| San Diego, CA               | 664         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Sheridan, WY                | 666         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Shreveport, LA              | 667         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Spokane, WA                 | 668         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| South Texas HCS             | 671         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| San Juan, PR                | 672         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Tampa, FL                   | 673         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Central Texas HCS           | 674         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Orlando, FL                 | 675         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Tomah, WI                   | 676         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Tucson, AZ                  | 678         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Tuscaloosa, AL              | 679         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Walla Walla, WA             | 687         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Washington, DC              | 688         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Connecticut HCS             | 689         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| West Los Angeles, CA        | 691         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| White City OR               | 692         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Wilkes Barre, PA            | 693         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Milwaukee, WI               | 695         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Valley Coastal Bend HCS     | 740         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| El Paso, TX                 | 756         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Columbus, OH                | 757         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Billings, MT CBOC           | 436GH       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Pensacola, FL               | 520BZ       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Canandaigua, NY             | 528A5       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Bath, NY                    | 528A6       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Syracuse, NY                | 528A7       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Albany, NY                  | 528A8       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Lake City VA Medical Center | 573A4       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Columbia, MO                | 589A4       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Topeka, KS                  | 589A5       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Leavenworth, KS             | 589A6       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Wichita, KS                 | 589A7       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Lexington, KY -CDD          | 596A4       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Grand Island, NE            | 636A4       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Lincoln, NE                 | 636A5       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Central Iowa HCS            | 636A6       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Iowa City, IA               | 636A8       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Poplar Bluff, MO            | 657A4       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |
| Marion, IL                  | 657A5       | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>   | <span class="mark">REDACTED</span>             |

<span id="_Ref68591786" class="anchor"></span>Table 3: VIX Install Checklist

> **NOTE:** For several sites, the VIX service accounts in Table 2 are missing because they expired at the time of publication of version 43.4 of this document.

> **NOTE:** Sites can find the DUZ corresponding to their VIX service account on the local VistA by following the steps below:

1.  In FileMan, choose the option to Inquire to File Entries, choose the New Person file (#200), and then enter the name of your VIX’s service account on its local VistA.
2.  Accept the defaults for Standard Captioned Output, when asked "Include COMPUTED fields", answer either B or R, as you need to view the record number.
3.  If multiple results are returned based on the name you entered, you will need to view each of them to determine which is your local service account and which are visitor accounts. Select one of the accounts.
4.  In the data listed for each account, check for the presence of the DATE VERIFY CODE LAST CHANGED field (refer to the red highlighted field in Figure 78). If the DATE VERIFY CODE LAST CHANGED field is not present return to step 2 and select a different account upon reaching step 4, otherwise continue to the next step.

<span id="_Ref112744831" class="anchor"></span>Figure : FileMan File Entry 200

![](vista-imaging-exchange-vix-installation-guide/132.png)

5.  If the field is present, it is the local service account. If it is not, it is a visitor account and should not be edited. The number printed in the NUMBER field is the DUZ of the VIX’s service account on the local VistA (refer to the green highlighted field in Figure 78). Record the DUZ of the VIX’s service account on the local VistA. (Consider documenting the DUZ of the service account on the local VistA in your Master Site Profile.)

> **NOTE:** Once the DUZ is obtained, follow the steps below to update the corresponding VIX service account:

1.  To view a record once you have its DUZ value, access VA FileMan \[DIUSER\] and select Inquire to File Entries \[DIINQUIRE\].
2.  When prompted "Output from what File", select NEW PERSON (#200).
3.  When asked to "Select NEW PERSON NAME", enter a back-tick (\`) followed by the DUZ for the account. Select whichever view options you want (the defaults are fine), and then view the account's record to determine the details and make any necessary adjustments.

> **NOTE:** If you are unable to perform the above steps, please create a support ticket with VistA Apps for assistance.

Below is an example of the information to provide in a ticket to update the VIX’s service account on the local VistA. The example shows specifying the access code of the VIX’s service account on the local VistA, the name of the VIX’s service account on the local VistA, the suggested name of the VIX’s service account on the local VistA, the SSN of the VIX’s service account on the local VistA, and any missing VistA menus, keys, and other settings to add. Be sure to copy and paste the security keys, secondary menus, INITIAL, and RAD/NUC information shown before Table 2 into the ticket as needed.

Assignment group: ESD Tier 1

Category: Service

Subcategory: Access

Please use the *SITE_SERVICE_ACCOUNT_ACCESS_CODE_HERE* to look up the DUZ for the *SITE_SERVICE_ACCOUNT_NAME_HERE* service account in *SITE_VISTA_NAME_HERE* VistA and then update the service account with the following:

Change service account name to: *IMAGINGSVC,SITE_ABBREVIATION_HERE*

Add SSN: *SITE_SERVICE_ACCOUNT_SSN_HERE*

Add keys: MAG DOD FIX, RA ALLOC

Add secondary menus: MAG WINDOWS, MAG DICOM QUERY RETRIEVE

Add INITIAL field: VSA

Add RAD/NUC med classification: RAD/NUC MED CLASSIFICATION

1 staff

4 technologist

Add CPRS TAB: CPRS TAB: COR

EFFECTIVE DATE: \<TODAY

Add AUTHORIZED TO WRITE MED ORDERS: YES

> **NOTE:** This is a false SSN, which was not generated by, and will not conflict with, a real SSN issued by the Social Security Administration, but meets the requirements for VistA Broker Security Exchange (BSE) authentication between sites. These changes are required for Enterprise DICOM query retrieve with MAG\*3.0\*269 and beyond.

# Appendix E: VIX Install Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 summarizes the VIX installation process.

## VIX Install Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|     | Requirement                                                                                            | Location in VIX Installation Guide                                                      | Action                                                                                                                                                                                                                                                                |
|-----|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ☐   | Verify VIX server meets required hardware specifications.                                              | See *Operating System and Hardware Requirements*                                        | Allocate more CPU cores/RAM as needed to meet the required specifications.                                                                                                                                                                                            |
| ☐   | Verify MUSE configuration information needed for installation, if any.                                 | See *Appendix A: Enable MUSE Functionality*                                             | Verify MUSE site number, MUSE server name, MUSE username, and MUSE password.                                                                                                                                                                                          |
| ☐   | Initiate the installation of the VIX MAG3_0P358_VIX_SETUP.msi.                                         | See Installation Instructions                                                           | Perform steps in Installation Instructions.                                                                                                                                                                                                                           |
| ☐   | Verify VIX install is complete.                                                                        | [See](#_Verifying_Installation/Upgrade_is) *Verifying Installation/Upgrade is Complete* | Perform steps in Verifying Installation/Upgrade is Complete.                                                                                                                                                                                                          |
| ☐   | Verify that VIX is running.                                                                            | [See](#_Verifying_Installation/Upgrade_is) *Verifying Installation/Upgrade is Complete* | Verify VIX is running.                                                                                                                                                                                                                                                |
| ☐   | Verify that VIX Viewer and VIX Render services running.                                                | [See](#_Verifying_Installation/Upgrade_is) *Verifying Installation/Upgrade is Complete* | Verify VIX Viewer and VIX Render services are running.                                                                                                                                                                                                                |
| ☐   | Request Site Service update to your facility if needed.                                                | See *To Register the VIX*                                                               | Create a national ticket with the Health, Clinical Services Diagnostics Team (previously known as Clin 3, the group name is SPM.Health.ClinSvs.Diag) to update your site service entry to include the new viewer (Port <span class="mark">REDACTED</span> for HTTPS). |
| ☐   | Verify that images, including MUSE EKGs and DoD images, can be viewed via zero-footprint Image Viewer. | See *Spot-Checking VIX Image Delivery*.                                                 | Verify JLV utilizing zero-footprint viewer. If unable to view an image including MUSE EKGs and DoD images, enter a support ticket for assistance.                                                                                                                     |

<span id="_Toc193816931" class="anchor"></span>Table 4: Definitions, Acronyms, and Abbreviations

# Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                      |
|-------|-------------------------------------------------|
| ACL   | Access Control List                             |
| AE    | Application Entity                              |
| BP    | Background Processor                            |
| BSE   | Broker Security Exchange                        |
| CPRS  | Computerized Patient Record System              |
| CPU   | Central Processing Unit                         |
| DCF   | DICOM Connectivity Framework                    |
| DICOM | Digital Imaging and Communications in Medicine  |
| DoD   | Department of Defense                           |
| DUZ   | Designated User                                 |
| EKG   | Electrocardiogram                               |
| ESD   | Enterprise Service Desk                         |
| FDA   | Food and Drug Administration                    |
| FQDN  | Fully Qualified Domain Number                   |
| GFE   | Government Furnished Equipment                  |
| HDIG  | Hybrid DICOM Gateway                            |
| ICW   | IMedConsent Web                                 |
| IEN   | Internal Entry Number                           |
| IVS   | Integrated Visualization System                 |
| JLV   | Joint Legacy Viewer / Joint Longitudinal Viewer |
| JMX   | Java Management Extensions                      |
| KB    | Knowledge Base                                  |
| OIT   | Office of Information Technology                |
| PACS  | Picture Archive and Communication System        |
| RAM   | Random Access Memory                            |
| ROI   | Release of Information                          |
| SCP   | Service Class Provider                          |
| SSN   | Social Security Number                          |
| TIU   | Text Integration Utility                        |
| VA    | Veterans Affairs                                |
| VIX   | VistA Imaging eXchange                          |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MAG*3*303 VistA Imaging Exchange (VIX) Installation Guide

### Setting up VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must install the compatible KIDS package on the VistA system before installing the VIX server software. For information about installing the KIDS package, see the patch description of the patch you are installing.

- If you are implementing a VIX for the first time, the MAG VIX ADMIN key must be assigned to the VistA accounts of administrators who need access to the VIX transaction log.

### Getting a VIX Security Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each server that hosts the VIX must request a security certificate. To receive a security certificate, send an email to <span class="mark">REDACTED</span> and include the following:

- The Fully Qualified Domain Name (FQDN) of the VIX server.
- Contact information for the primary and backup administrators of the VIX.

Requests typically process within five business days, after which the security certificate (one per server) is securely transmitted to the requesting site POC for install on the site VIX. The security certificate includes the following files:

- A federation.zip file containing federation.truststore and federation.keystore.
- A LocalAdmin.jks file.

After receiving the security certificate, copy the contents to the temporary folder in C:\temp on the local server where the VIX software is installed. The VIX Service Installation Wizard prompts you to provide the federation.zip file from the security certificate during the installation process.

### PowerShell Version Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the VIX install, validate the installed Windows PowerShell version. If PowerShell 4.0 is the current installed version, you must install PowerShell 5.1 on your server to replace version 4.0. If PowerShell 5.1 or later is not installed, the post-installation script fails. To determine the PowerShell version:

1.  Choose Start, type PowerShell, then right-click on Windows PowerShell and run as an administrator (Figure 6).

<span id="_Ref67647578" class="anchor"></span>Figure 6: Execute Windows PowerShell

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/011.png)

6.  Once PowerShell launches, type the command:

    Get-Host \| Select-Object Version

    Press \[ENTER\] to display the PowerShell version.
7.  Notice the first two numbers that appear under Version, then close PowerShell. If the first two numbers under Version are 4.0 (Figure 7), proceed with the next step to install PowerShell 5.1.

<span id="_Ref67901869" class="anchor"></span>Figure 7: PowerShell Version 4.0 Check

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/012.png)

PowerShell 5.1 software can be found in the file Win8.1AndW2K12R2-KB3191564-x64.msu, with direct download available from <https://www.microsoft.com/en-us/download/details.aspx?id=54616>. To install PowerShell:

1.  Follow the on-screen instructions (Figure 8).

<span id="_Ref67901988" class="anchor"></span>Figure 8: PowerShell Setup Dialogs

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/013.png)

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/014.png)

8.  After PowerShell 5.1 is installed, a reboot of your server is REQUIRED.

To verify the successful installation of PowerShell:

1.  Choose Start, type PowerShell, then right-click on Windows PowerShell and run as an administrator (Figure 6).
9.  Once PowerShell launches, type the command:

    Get-Host \| Select-Object Version

    Press \[ENTER\] to display the PowerShell version.
10. Notice the first two numbers that appear under Version, then close PowerShell. The first two numbers under Version should display 5.1 (Figure 9) if PowerShell 5.1 installation was successful.

<span id="_Ref67902270" class="anchor"></span>Figure 9: PowerShell Version 5.1 Check

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/015.png)

> **NOTE:** PowerShell must be configured to allow scripts to run. An error may occur (Figure 10) that prevents scripts from running.

<span id="_Ref67902334" class="anchor"></span>Figure 10: PowerShell Script Error

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/016.png)

To fix the above PowerShell script error:

1.  Choose Start, type PowerShell, then right-click on Windows PowerShell and run as an administrator (Figure 6).
11. Once PowerShell launches, type the command:

    Set-ExecutionPolicy RemoteSigned -Force

    Press \[ENTER\] to set the policy to allow scripts to run, then close PowerShell.

### VistA Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX server software requires that a compatible Imaging KIDS package be installed on VistA. For details about the compatible KIDS package and installing it, see the patch description of the specific patch.

### Scheduling Downtown and Impact of a VIX Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to schedule downtime with appropriate personnel for the duration of the VIX installation. Schedule 1 to 2 hours for the downtime and notify users of the impact of the VIX update.

While the VIX server is being updated, VIX assisted functions are unavailable. The list of known applications and services impacted by a local offline VIX includes:

- Clinical Display access to remote images may be temporarily inaccessible.
- VistARad access to remote images and other teleradiology features.
- DICOM Importer client.
- Local Joint Legacy Viewer (JLV) user display of images (local or remote).
- Signed Informed Consent ability to store new consents.
- Any new Ingest consuming application.
- Integrated Visualization System (IVS) mobile application access to local images.
- Enterprise DICOM Q/R functionality.
- Access to DoD images or artifacts.
- Access to VA Cerner images or artifacts.
- Any other external application calling a local VIX service directly.

Table 1 summarizes how a VIX outage affects clinicians.

<table>
<caption><p><span id="_Ref102564585" class="anchor"></span>Table 2: VIX Site’s User Profile SSN, Service Account on Local VistA, and Suggested Service Account on Local VistA</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Clinical Group</th>
<th>Impact</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local Clinical Display Users</td>
<td><p>DoD images are inaccessible for the duration of the VIX shutdown.</p>
<p>Remote VA images may be temporarily inaccessible. Clinical Display attempts to revert to pre-VIX remote image views, but users may have to disconnect from and reconnect to remote sites, or in some cases, restart Clinical Display.</p>
<p>Clinicians may notice longer retrieval times for remote images for the duration of the VIX shutdown.</p>
<p>After the VIX is restarted, restart Clinical Display to ensure that Clinical Display is no longer using pre-VIX remote image views for remote sites.</p></td>
</tr>
<tr class="even">
<td>Local VistARad Users</td>
<td>Remote exam data and images and monitored exam lists are unavailable. For additional information, refer to the documentation for VistARad.</td>
</tr>
<tr class="odd">
<td>Remote VA or DoD Clinicians requesting Images or Artifacts</td>
<td><p>Remote clinicians may experience transitory application errors if the VIX is shut down while it is in the middle of processing a request; the clinician may have to repeat the request.</p>
<p>Remote VA clinicians issuing new requests may notice longer retrieval times for the duration of the VIX shutdown.</p>
<p>Remote DoD clinicians are unable to retrieve locally stored images for the duration of the VIX shutdown.</p></td>
</tr>
<tr class="even">
<td>Local DICOM Importer Users</td>
<td>The DICOM importer client cannot log into VistA and process imports for the duration that the VIX is down.</td>
</tr>
<tr class="odd">
<td>VIX Image Viewer/JLV Users</td>
<td>Clinical users of JLV cannot access images or artifacts (local or remote) using the VIX image viewer.</td>
</tr>
<tr class="even">
<td>iMedConsent Users</td>
<td>Patients’ consent forms are unavailable. Currently, this results in multiple unsigned Text Integration Utility (TIU) notes in Computerized Patient Record System (CPRS) due to CVIX and iMedConsent Web (ICW) deficiencies until the necessary corrective action(s) can be deployed by both the CVIX and ICW development teams.</td>
</tr>
<tr class="odd">
<td>IVS Mobile Application Users</td>
<td>IVS mobile application users cannot access local images.</td>
</tr>
</tbody>
</table>

<span id="_Ref102564585" class="anchor"></span>Table 2: VIX Site’s User Profile SSN, Service Account on Local VistA, and Suggested Service Account on Local VistA

## McAfee Exclusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exclude the following directories using McAfee On-Access Scan Properties (Figure 63). Make sure “Also exclude subfolders” is checked, so subfolders are excluded as well:

- C:\Program Files\Java\\\*\\lib\\
- C:\Program Files\Apache Software Foundation\Tomcat\*\lib\\
- C:\Program Files\Apache Software Foundation\Tomcat\*\logs\\
- C:\Program Files\VistA\Imaging\VIX.Render.Service\log\\
- C:\Program Files\VistA\Imaging\VIX.Viewer.Service\log\\
- C:\VixConfig\logs\\
- ?:\VixCache\\
- ?:\VIXRenderCache\\

> **NOTE:** The wildcards, \* and ? for the java, tomcat, and cache folder exclusions respectively, are new with MAG\*3.0\*303.NOTE: The wildcard \* can replace the wildcard ? for the cache folder exclusions, if desired.

<span id="_Ref67988588" class="anchor"></span>Figure 63: Set Exclusions Dialog

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/104.png)

Click OK in the Set Exclusions window. Then click OK in the McAfee On-Access Scan Properties window.

## Tomcat Permissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If encountering file system access errors after VIX Installation, please refer to *Appendix E: Tomcat Permissions,* i.e.: ...error denying access to apachetomcat account.

## Rollback and Back Out of MAG\*3.0\*303

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*303 VIX and back out the VIX to a prior version perform the following steps:

1.  Run the MAG\*3.0\*303 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

    NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.
133. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*303 VIX” and click Next.
134. Then, when prompted to do so, click Uninstall version 30.303.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
135. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
136. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*303 VIX Service Installation Wizard.
137. Verify backup copies of critical configuration file folders exist within C:\VIXBackup\P269\YYYYMMDDHHMMSS. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Backups exist of the following:
- C:\DCF_RunTime_x64\cfg
- C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf
- C:\Program Files\VistA\Imaging\VIX.Config
- C:\VixConfig
- C:\VixCertStore
138. Stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 77) as described in Section 6.1.
139. Install the previous version of VIX, which was included in MAG\*3.0\*269 (find it on the VA SFTP site or from a local backup folder). Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P269_VIX_SETUP.msi file and click on Install.
30. When the Welcome page displays, click Next.
31. When the Confirm Installation page displays, click Next.
32. When the Installation Complete screen displays, click Close.
140. Run the MAG\*3.0\*269 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> **NOTE:** If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

141. Once the MAG\*3.0\*269 VIX Service Installation Wizard is running, click Next and continue with the installation steps described in detail in the *MAG\*3.0\*269 VIX Installation Guide* as if it is an upgrade MAG\*3.0\*269 install, *except* also perform the following steps regarding SQL Server installation. During the upgrade install, prior to clicking Next on the Install the VIX Prerequisites page, install SQL Server if prompted, by performing the following:
1.  Click OK and select (Figure 78) the SQLEXPRESS_X64-14_0_1000_169.ZIP file in the temporary folder in C:\temp. Depending on your system, this step may take up to twenty minutes (Figure 79).

<span id="_Ref67916431" class="anchor"></span>Figure 78: Select the SQLEXPRESS_X64-14_0_1000_169.ZIP dialog

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/121.png)

<span id="_Ref67916563" class="anchor"></span>Figure 79: SQL Server Setup

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/122.png)

33. Once SQL Server is installed, in the Install the VIX Prerequisites page, confirm that all the icons are ![](mag-3-303-vista-imaging-exchange-vix-installation-guide/123.png). Then, click Next. Then proceed with the remaining installation steps described in detail in the *MAG\*3.0\*269 VIX Installation Guide* as if it is an upgrade MAG\*3.0\*269 install.
142. Upon completion of the installation, if necessary, configuration files in C:\VIXBackup\P269\YYYYMMDDHHMMSS\VixConfig can be copied to C:\VixConfig as needed (e.g. MuseDataSource-1.0.Config) to restore the prior version. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Encryption support for many configuration files was added in MAG\*3.0\*303. If any potential issues arise with configuration files, it is suggested to copy the files IdConversionConfiguration.config, FederationDataSource-1.0.config, ExchangeDataSource-1.0.config, MuseDataSource-1.0.config in C:\VIXBackup\P269\YYYYMMDDHHMMSS\VixConfig to C:\VixConfig and replace over the existing IdConversionConfiguration.config, FederationDataSource-1.0.config, ExchangeDataSource-1.0.config, MuseDataSource-1.0.config files. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     If configuration files are to be restored, first stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service.
143. Apply the McAfee Exclusions after MAG\*3.0\*269 install as discussed in the *MAG\*3.0\*269 VIX Installation Guide*.
144. Reboot your server.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the version of Java after reinstalling MAG\*3.0\*269 by running Windows ‘Programs and Feature’, is Java 8.0.291
145. Verify the version of Tomcat after reinstalling MAG\*3.0\*269 by running Windows ‘Programs and Features’, is Tomcat 9.0.40
146. Verify the version of the VIX by going to the VIX homepage http://*FQDN of VIX server*:<span class="mark">REDACTED</span>/ using a browser e.g.: Chrome or Edge.
147. Verify the SQL Server services are running. For Server 2012 R2 or 2016 (Server Manager \| Tools \| Component Services \| Services (Local), or Task Manager \| Services \| Open Services), sort the Name column, and verify SQL Server (SQLEXPRESS) is running (Figure 80).

     NOTE: If the SQL Server (SQLEXPRESS) service in the Windows Services is not running or disabled, please enable the SQL Server (SQLEXPRESS) service and start it.

<span id="_Ref112416991" class="anchor"></span>Figure 80: Verify SQL Server Service

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/124.png)

## AE Titles Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes both the calling and called Application Entities (AE) Titles that must both be configured for DICOM SCP to work. It is necessary to configure both the AE Titles on the VIX server with those of the DICOM SCP client and also to configure the AE Titles on the DICOM SCP client with those of the VIX server.

> **NOTE:** The port for the host for DICOM SCP must be configured as a bi-directional open port in any firewall.

### Laurel Bridge AE Titles Configuration on VIX/CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to configure the AE Titles configuration file ae_title_mappings located in the folders cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default). Open the ae_title_mappings file to perform edits. Run, Notepad, Notepad++, or WordPad as an administrator and then open the file.

For each DICOM SCP client, the AE Title name and its host/port attributes must be set. For each DICOM SCP client, update the following entries for the AE Titles configuration file (see Figure 86):

1.  Set the IP address for the host for the DICOM SCP client, (after host = line 11).
151. Set the port for the DICOM SCP client where the DICOM SCP is used for the C-STORE operation, (after port = line 12).
152. Set the AE Title the DICOM SCP client is using to communicate with the DICOM SCP (calling AE) (inside \[ \] on line 10 and after ae_title = line 13).

Ensure that each of these lines is uncommented (i.e. remove the \# at the front of the line if present). Save the ae_title_mappings file after updating the entries.

<span id="_Ref70085061" class="anchor"></span>Figure 86: Sample AE Titles Configuration File

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/130.png)

An example of the ae_title_mappings file updated for one DICOM SCP client is shown in Figure 87.

> **NOTE:** The example in Figure 87 for configuration of one DICOM SCP client is not how an actual VIX site’s ae_title_mappings file is to be configured. This example is for illustrative purposes only.

<span id="_Ref95983087" class="anchor"></span>Figure 87: Example AE Titles Configuration File

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/131.png)

For each additional DICOM SCP client, similarly add lines for the host, port, and ae_title with the correct values as new lines below the prior lines for the prior DICOM SCP client (Figure 88). Save the ae_title_mappings file after updating the entries.

<span id="_Ref70503007" class="anchor"></span>Figure 88: Sample AE Titles configuration File with Multiple DICOM SCP Clients

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/132.png)

After updating the ae_title_mappings file, as described above, execute the restart script (Restart_VIX_Services.ps1) to restart the Apache Tomcat service, VIX Viewer and VIX Render services, and Listener Tool, see

### AE Titles Configuration on DICOM SCU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the AE Titles configuration on the DICOM SCU. Installation/administration personnel on the VIX server might not be able to perform this configuration and, in which case, must provide the necessary information to the DICOM SCU administration personnel to perform.

The following three pieces of information are needed for the configuration of the DICOM SCU: 1) the IP address for the host for the VIX server, 2) the port of DICOM SCP on the VIX server, and 3) the AE Title of DICOM SCP (called AE).

Many different DICOM SCU vendors exist and each of these systems has their own distinct approach for configuration. If additional information regarding specifics of configuring the DICOM SCU is needed, please reach out to its vendor or consult its documentation.

## Script SQL Server Removal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If not already present, acquire SQLEXPRESS_X64-14_0_1000_169.ZIP (SQL 2017) and copy to C:\temp. (Download if required. See the patch description of the patch for the download location.)
2.  Run PowerShell as an administrator (Figure 93).
    1.  Right-click Start.
    2.  Left-click Search.
    3.  Type powershell.
    4.  Right-click Windows PowerShell.
    5.  Left-click Run as administrator.

<span id="_Ref95147469" class="anchor"></span>Figure 93: Execute Windows PowerShell

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/137.png)

158. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
159. Once PowerShell launches, type the command:

     cd "C:\Program Files\VistA\Imaging\Scripts"

     Then press \[ENTER\] to change the working directory to the Scripts folder.
160. Then type the command:

     .\uninstall_install_sql_server.ps1

     And press \[ENTER\] to execute the script.
161. When prompted with “Please enter the full path of the SQLEXPRESS_X64-14_0_1000_169.ZIP file” enter C:\temp and press \[ENTER\].
162. When prompted with “Please choose Deployment Option (1 to Uninstall, 2 to Install, or Q to Quit)” enter 1 and press \[ENTER\].
163. When prompted with “Confirm you want to uninstall SQL Server Express (Y/N?)” enter Y and press \[ENTER\].
164. A Remove SQL Server 2017 window appears. On the Select Instance page click Next (Figure 94).

<span id="_Ref117707733" class="anchor"></span>Figure 94: Remove SQL Server Select Instance

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/138.png)

165. On the Select Features page click Select All, then click Next (Figure 95). Wait for the uninstall of SQL Server to complete. This can take about seven to ten minutes.

<span id="_Ref117707737" class="anchor"></span>Figure 95: Remove SQL Server Select Features

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/139.png)

166. On the Complete page click Close (Figure 96).

<span id="_Ref117707759" class="anchor"></span>Figure 96: Remove SQL Server 2017 Complete

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/140.png)

167. Close PowerShell.
168. Restart the server after uninstalling SQL Server*.*

## Manual SQL Server Removal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Stop the Apache Tomcat Service if it is installed and running.
169. Uninstall MS-SQL programs for 2017 (Control Panel – Programs – Programs and Features – Uninstall) (Figure 97).
170. Remove/Delete the folder C:\Program Files\Microsoft SQL Server (include data files if any exist).
171. Restart the server after uninstalling SQL Server*.*

<span id="_Ref67902748" class="anchor"></span>Figure 97: Microsoft SQL Removal

![](mag-3-303-vista-imaging-exchange-vix-installation-guide/141.png)

### From: MAG*3*329 VistA Imaging Exchange (VIX) Installation Guide

## Clearing the VixCache

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reduce downtime required for installation, perform the following steps prior to Section 3.4:

1.  Run PowerShell as an administrator (Figure 27).
    1.  Right-click Start.
    2.  Left-click Search.
    3.  Type powershell.
    4.  Right-click Windows PowerShell.
    5.  Left-click Run as administrator.

<span id="_Ref128688275" class="anchor"></span>Figure : Execute Windows PowerShell

![](mag-3-329-vista-imaging-exchange-vix-installation-guide/053.png)

40. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
41. Once PowerShell launches, type the command:

    \$vixLocalCachePath = \[System.Environment\]::GetEnvironmentVariable('vixcache') -replace "/", "\\

    Then press \[ENTER\] to set the path of YOUR_DRIVE_LETTER:\VixCache.

    NOTE: If the system variable for the vixcache is not set, use the below command instead and replace YOUR_DRIVE_LETTER with your drive letter of the VixCache folder.

    \$vixLocalCachePath = "YOUR_DRIVE_LETTER:\VixCache"
42. Now type the command:

    Get-ChildItem -Path "\\?\\(\$vixLocalCachePath)" -Recurse \| Foreach-object {Remove-item -Recurse -Force -path \$\_.FullName}

    Then press \[ENTER\] to delete the contents and sub-folders in YOUR_DRIVE_LETTER:\VixCache.

> **NOTE:** Each of command in steps 3 and 4 is one line. To copy each command from the Installation Guide into PowerShell, it is suggested to perform the following: copy each command from the Installation Guide and paste into Notepad or Notepad++, then copy each command from Notepad or Notepad++, and then paste into PowerShell.

> **NOTE:** If these steps are not performed, the VIX Server Update will complete but may take an additional 10 minutes or more.

## Rollback and Back Out of MAG\*3.0\*329

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*329 VIX and back out the VIX to a prior version perform the following steps:

1.  Run the MAG\*3.0\*329 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

    NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.
127. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*329 VIX” and click Next.
128. Then, when prompted to do so, click Uninstall version 30.329.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
129. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
130. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*329 VIX Service Installation Wizard.
131. Verify backup copies of critical configuration file folders exist within C:\VIXBackup\P303\YYYYMMDDHHMMSS. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Backups exist of the following:
- C:\DCF_RunTime_x64\cfg
- C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf
- C:\Program Files\VistA\Imaging\VIX.Config
- C:\VixConfig
- C:\VixCertStore
- Install logs from C:\Program Files (x86)\Vista\Imaging\VixInstaller
132. Stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 61) as described in Section 6.1.
133. Install the previous version of VIX, which was included in MAG\*3.0\*303 (find it on the VA SFTP site or from a local backup folder). Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P303_VIX_SETUP.msi file and click on Install.
36. When the Welcome page displays, click Next.
37. When the Confirm Installation page displays, click Next.
38. When the Installation Complete screen displays, click Close.
134. Run the MAG\*3.0\*303 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> **NOTE:** If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

135. Once the MAG\*3.0\*303 VIX Service Installation Wizard is running, click Next and continue with the installation steps described in detail in the *MAG\*3.0\*303 VIX Installation Guide* as if it is an upgrade MAG\*3.0\*303 install.
136. Upon completion of the installation, if necessary, configuration files in C:\VIXBackup\P303\YYYYMMDDHHMMSS\VixConfig can be copied to C:\VixConfig as needed (e.g. MuseDataSource-1.0.Config) to restore the prior version. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     If configuration files are to be restored, first stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service.
137. Apply the McAfee Exclusions after MAG\*3.0\*303 install as discussed in the *MAG\*3.0\*303 VIX Installation Guide*.
138. Reboot your server.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the version of Java after reinstalling MAG\*3.0\*303 by running Windows ‘Programs and Feature’, is Java 8.0.331
139. Verify the version of Tomcat after reinstalling MAG\*3.0\*303 by running Windows ‘Programs and Features’, is Tomcat 9.0.58
140. Verify the version of the VIX by going to the VIX homepage http://*FQDN of VIX server*:<span class="mark">REDACTED</span>/ using a browser e.g.: Chrome or Edge.

### From: MAG*3*269 VistA Imaging Exchange (VIX) Installation Guide

### SQL Version Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the VIX install, remove any SQL version older than SQL 2017.

1.  Stop the Apache Tomcat Service if it is installed and running.
12. Uninstall all old MS-SQL programs (Control Panel – Programs – Programs and Features – Uninstall) (Figure 12).
13. Remove/Delete the folder C:\Program Files\Microsoft SQL Server (include data files if any exist).
14. <u>RESTART the VIX server before proceeding. You MUST restart the server after uninstalling SQL software.</u>

<span id="_Ref67902748" class="anchor"></span>Figure 12: Microsoft SQL Removal

![](mag-3-269-vista-imaging-exchange-vix-installation-guide/018.png)

## Pre-Installation Configuration 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>New with MAG\*3.0\*269:</u> Due to the VA group policy restriction or rules, there may be an issue found while the VIX installer wizard is setting file system access rules.

Check the current size of the YOUR_DRIVE_LETTER:\VixCache folder. Open Windows Explorer and navigate to the YOUR_DRIVE_LETTER:\VixCache folder. Left-click on the VixCache folder and right-click on properties. Note the current size of the VixCache folder.

If the current size of the VixCache folder exceeds 2 GB it is suggested to clear (delete) the contents of the subfolders in the YOUR_DRIVE_LETTER:\VixCache folder to avoid lengthy installation times and potentially prevent a hanging install. Use the following steps to delete the contents of the YOUR_DRIVE_LETTER:\VixCache folder:

1.  Run PowerShell as an administrator (Figure 37).
    1.  Right-click Start.
    2.  Left-click Search.
    3.  Type powershell.
    4.  Right-click Windows PowerShell.
    5.  Left-click Run as administrator.

<span id="_Ref103337613" class="anchor"></span>Figure 37: Execute Windows PowerShell

![](mag-3-269-vista-imaging-exchange-vix-installation-guide/063.png)

48. If prompted with “Do you want to allow the following program from an unknown publisher to make changes to this computer?”, click Yes.
49. Once PowerShell launches, type the command:

    \$vixLocalCachePath = \[System.Environment\]::GetEnvironmentVariable('vixcache') -replace "/", "\\

    Then press \[ENTER\] to set the path of YOUR_DRIVE_LETTER:\VixCache.

    NOTE: If the system variable for the vixcache is not set, use the below command instead and replace YOUR_DRIVE_LETTER with your drive letter of the VixCache folder.

    \$vixLocalCachePath = "YOUR_DRIVE_LETTER:\VixCache"
50. Now type the command:

    Get-ChildItem -Path "\\?\\(\$vixLocalCachePath)" -Recurse \| Foreach-object {Remove-item -Recurse -Force -path \$\_.FullName}

    Then press \[ENTER\] to delete the sub-folders in YOUR_DRIVE_LETTER:\VixCache.
51. Once the command completes, close PowerShell.

## Post-Installation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>New with MAG\*3.0\*269:</u> Perform the following post-installation steps to allow for login to the new VIX Tools page described in the *Verifying Access to the VIX Tools and VIX Transaction Log* section.

1.  Open Windows Explorer and navigate to the C:\Program Files\Vista\Imaging\VIX.Config folder. Run Notepad, Notepad++, or WordPad as an administrator and open the VIX.Viewer.Config file.
79. Add the following line as shown in Figure 61 inside the opening and closing Policies tags (if it does not already exist)

    \<add name="Dashboard.RequireAdministrator" value="false" /\>

    Save the VIX.Viewer.Config file after updating.

    NOTE: If a policy for "Dashboard.RequireAdministrator” already exists, ensure the value is set to “false”.

<span id="_Ref103696546" class="anchor"></span>Figure 61: VIX.Viewer.Config File Policies

![](mag-3-269-vista-imaging-exchange-vix-installation-guide/106.png)

80. Execute the restart script (Restart_VIX_Services.ps1) to restart the Apache Tomcat service, VIX Viewer and VIX Render services, and Listener Tool, see *Appendix C: Restart Script*.

## MUSE Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to *Appendix A: Enable MUSE Functionality* to configure the MUSE (if not previously configured).

## Rollback and Back Out of MAG\*3.0\*269

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*269 VIX and back out the VIX to a prior version perform the following steps:

1.  Run the MAG\*3.0\*269 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

    NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.
130. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*269 VIX” and click Next.
131. Then, when prompted to do so, click Uninstall version 30.269.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
132. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
133. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*269 VIX Service Installation Wizard.
134. Verify backup copies of critical configuration file folders exist within C:\VIXBackup\P284\YYYYMMDDHHMMSS. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Backups exist of the following:
- C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf
- C:\VixConfig
- C:\VixCertStore
- C:\Program Files\VistA\Imaging\VIX.Config
135. Stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 71) as described in Section 6.1.
136. Copy the file ROIPeriodicCommandConfiguration.config in C:\VIXBackup\P284\YYYYMMDDHHMMSS\VixConfig to C:\VixConfig and replace over the existing ROIPeriodicCommandConfiguration.config file. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).
137. Install the previous version of VIX, which was included in MAG\*3.0\*284 (find it on the VA SFTP site or from a local backup folder). Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P284_VIX_SETUP.msi file and click on Install.
28. When the Welcome page displays, click Next.
29. When the Confirm Installation page displays, click Next.
30. When the Installation Complete screen displays, click Close.
138. Run the MAG\*3.0\*284 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> **NOTE:** If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

139. Once the MAG\*3.0\*284 VIX Service Installation Wizard is running, click Next and continue with the installation steps described in detail in the [*MAG\*3.0\*284 VIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105) as if it is an upgrade MAG\*3.0\*284 install.
140. Upon completion of the installation, if necessary, configuration files in C:\VIXBackup\P284\YYYYMMDDHHMMSS\VixConfig can be copied to C:\VixConfig as needed (e.g. MuseDataSource-1.0.Config) to restore the prior version. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date). If configuration files are to be restored, first stop each VIX service: ListenerTool, Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 71) as described in Section 6.1.
141. Uninstall Java 8.0.291 manually using the Control Panel (Figure 13).
142. Apply the McAfee Exclusions after MAG\*3.0\*284 install as discussed in the [*MAG\*3.0\*284 VIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105).

     NOTE: Make sure the subfolder C:\Program Files\Java\\jre1.8.0_251\lib is excluded.
143. Install MAG\*3.0\*326 to apply the log4j fixes.
144. Reboot your server.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the version of Java after reinstalling MAG\*3.0\*284 by running Windows ‘Programs and Feature’, is Java 8.0.251
145. Verify the version of Tomcat after reinstalling MAG\*3.0\*284 by running Windows ‘Programs and Features’, is Tomcat 9.0.34
146. Verify the version of the VIX by going to the VIX homepage http://*FQDN of VIX server*:<span class="mark">REDACTED</span>/ using a browser e.g.: Edge or Chrome.

### From: MAG*3*348 VistA Imaging Exchange (VIX) Installation Guide

## Rollback and Back Out of MAG\*3.0\*348

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*348 VIX and back out the VIX to a prior version perform the following steps:

1.  Run the MAG\*3.0\*348 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

    NOTE: If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.
123. When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch MAG\*3.0\*348 VIX” and click Next.
124. Then, when prompted to do so, click Uninstall version 30.348.xxx. (The wizard gracefully stops the VIX service before performing the uninstall.)
125. When the Uninstall completes, "Press Next to continue" displays in the VIX Service Installation Wizard, click Cancel. Click Yes in the dialog box that displays "Do you really want to quit the VIX Service Installation Wizard?"
126. Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*348 VIX Service Installation Wizard.
127. Verify backup copies of critical configuration file folders exist within C:\VIXBackup\P329\YYYYMMDDHHMMSS. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     NOTE: Backups exist of the following:
- C:\DCF_RunTime_x64\cfg
- C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf
- C:\Program Files\VistA\Imaging\VIX.Config
- C:\VixConfig
- C:\VixCertStore
- Install logs from C:\Program Files (x86)\Vista\Imaging\VixInstaller
128. Stop each VIX service: Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service (Figure 60) as described in Section 6.1.
129. Uninstall any LibreOffice version later than 7.3.5 using the Control Panel.
130. Install the previous version of VIX, which was included in MAG\*3.0\*329 (find it on the VA SFTP site or from a local backup folder). Do the following to prepare the VIX Service Installation Wizard:
1.  Right-click the MAG3_0P329_VIX_SETUP.msi file and click on Install.
35. When the Welcome page displays, click Next.
36. When the Confirm Installation page displays, click Next.
37. When the Installation Complete screen displays, click Close.
131. Run the MAG\*3.0\*329 VIX Service Installation Wizard as an administrator.
1.  Right-click Start.
2.  Left-click Search.
3.  Type VIX.
4.  Right-click VIX Service Installation Wizard.
5.  Left-click Run as administrator.

> **NOTE:** If the VIX Service Installation Wizard does not appear in the Search bar, open Windows Explorer and navigate to the C:\Program Files (x86)\Vista\Imaging\VixInstaller folder, right-click VixInstaller.exe and left-click Run as administrator.

132. Once the MAG\*3.0\*329 VIX Service Installation Wizard is running, click Next and continue with the installation steps described in detail in the *MAG\*3.0\*329 VIX Installation Guide* as if it is an upgrade MAG\*3.0\*329 install.
133. Upon completion of the installation, if necessary, configuration files in C:\VIXBackup\P329\YYYYMMDDHHMMSS\VixConfig can be copied to C:\VixConfig as needed (e.g. MuseDataSource-1.0.Config) to restore the prior version. Where YYYYMMDDHHMMSS is the latest version of the folder that contains the backups (most current date).

     If configuration files are to be restored, first stop each VIX service: Tomcat9, VIX Render Service, and VIX Viewer Service by opening Windows Services and then selecting Stop for each service.
134. If able, apply the McAfee Exclusions after MAG\*3.0\*329 install as discussed in the *MAG\*3.0\*329 VIX Installation Guide*.
135. Reboot your server.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the version of Java after reinstalling MAG\*3.0\*329 by running Windows ‘Programs and Feature’, is Java 8.0.351
136. Verify the version of Tomcat after reinstalling MAG\*3.0\*329 by running Windows ‘Programs and Features’, is Tomcat 9.0.68
137. Verify the version of the VIX by going to the VIX homepage http://*FQDN of VIX server*:<span class="mark">REDACTED</span>/ using a browser e.g.: Chrome or Edge.
