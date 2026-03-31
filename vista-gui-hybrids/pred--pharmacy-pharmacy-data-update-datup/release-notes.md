---
consolidated_title: "datup release notes"
app_code: PRED
doc_type: RN
master_source: "DATUP Version 2 Release Notes"
master_pub_date: June 2014
consolidated_from: 3 versions
prior_versions:
  - "DATUP Version 3 Release Notes"
  - "PRED*4*3 DATUP Version 4.0.3 Release Notes"
---

**Data Update (DATUP) Release Notes**

<!-- image -->

**Version 2.0**

**June 2014**

**Department of Veterans Affairs Office of Information and Technology (OIT)**

**Product Development (PD)**

*(This page included for two-sided copying.)*

**Table of Contents**

1. Introduction	1
2. Enhancements	2
    - 2.1. Functional Enhancements	2
    - 2.2. Architectural Enhancements	2

June 2014	Data Update (DATUP) v2.0	i Release Notes

*(This page included for two-sided copying.)*

ii	Data Update (DATUP) v2.0	June 2014 Release Notes

### Introduction

The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. PRE is intended to build on the work accomplished in 2006 with the development of the Pharmacy Enterprise Product System (PEPS) Proof of Concept (POC). The first phase, PRE V.0.5, implements enhanced order checking functionality utilizing Health *e* Vet (H *e* V) compatible architecture and First Databank (FDB) MedKnowledge 1 Application Program Interfaces (APIs) and database. Data Update (DATUP) is a JAVA-based utility that supports the Medication Order Check Healthcare Application (MOCHA) by performing data source updates. MOCHA conducts order checks using First Databank (FDB) FDB-DIF within the existing VistA pharmacy application. FDB-DIF is a data product that provides the latest identification and safety information on medications. Additionally, FDB provides the latest algorithms used to perform order checks. DATUP processes the data updates associated with FDB’s DIF. DATUP is installed as a local instance as well as nationally, and there are two installation guides.

In response to the Project Management Accountability System (PMAS) initiative instituted in the summer of 2009 that requires projects to complete an increment every six months, PRE now uses an Agile Development methodology, which focuses on developing a usable product at the end of small, iterative timeframes, with involvement and approval from the product owner at every iteration. Each small timeframe, called a sprint, ends with a workable product that is built on the previous efforts until the increment is complete and meets the PMAS schedule. Each increment produces agreed-upon functionality that is available to the entire user community upon National Deployment.

DATUP v1.0, the initial version, was deployed to production in 2010 and remained in use until DATUP v1.1 was deployed. The initial version included some changes to how the email notifications, informing users that a new First Databank Incremental Update file is available, were displayed. DATUP v1.1 was deployed in 2012 and included XXX???

This Release Notes document provides a brief description of the new features and functions of DATUP v2.0.

1. At the time of development, this product was known as FDB Drug Information Framework (commonly abbreviated as FDB- DIF). The references to FDB-DIF in this Release Notes document are necessary because that was the product that was installed with this release, and references to the new database (MedKnowledge) would be inaccurate, as it has a different schema.

June 2014	Data Update (DATUP) v2.0	1

Release Notes

### Enhancements

DATUP v2.0 provides both functional and architectural enhancements.

#### Functional Enhancements

#### Update Files:

- Copies the image files included in the First Databank Incremental Update files to the file system so that PPS-N can display those images.

#### Architectural Enhancements

DATUP updated from FDB-DIF 3.2 to FDB-DIF 3.3 API and Schema

1. Data Update (DATUP) v2.0	June 2014 Release Notes

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DATUP Version 3 Release Notes

## Purpose

These release notes cover the changes to DATUP v3.0 for this release.

## Audience

This document targets users and administrators of DATUP 3.0 and applies to the changes made between this release and any previous release for this software.

## This Release

The purpose of this release was to make DATUP 3.0 Technical Reference Model (TRM) compliant.

### New Features and Functions Added

No new features and functions were added to the DATUP 3.0 release:

### Enhancements and Modifications to Existing

Implementation of SFTP for DATUP. This updates the DATUP source code to use Apache SFTP instead of Apache FTP

Update DATUP WebLogic Server to v12 so that DATUP is compliant with the TRM.

Modifications were made to make DATUP 3.0 TRM compliant.

### Known Issues

None.

## Product Documentation

The following documents apply to this release:

Data Update (DATUP) Requirements Specification v3.0 dated September 2015

PRE V0 5 OC SRS 012210\_V6\_3

Pharmacy Re-Engineering (PRE) Deployment Architecture Option, Version 0.3 dated 4/2007

Pharmacy Re-Engineering (PRE) Deployment Architecture, Version 0.1 dated 4/2008

PRE V. 0.5 Interface Control Document (ICD) v.1-1 (April 2008)

PRE V. 0.5 VistA Pharmacy to PEPS Interface Document (draft) dated 3/2008

### From: PRED*4*3 DATUP Version 4.0.3 Release Notes

### ### 2 Introduction

The Pharmacy Reengineering (PRE) Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). Medication order checks are accomplished through the synergistic functionality of multiple applications, including Medication Order Check Healthcare Application (MOCHA), Pharmacy Product System-National (PPS-N), Pharmacy Enterprise Customization System (PECS), and Data Update (DATUP).

DATUP is a utility that runs an automated process to maintain the First Databank Drug Information Framework (commonly abbreviated as FDB-DIF) and VA custom data used by regional MOCHA instances and at the national level by PPS-N.
