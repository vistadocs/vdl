---
title: PECS Version 6.2 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: PECS
app_name: 'Pharmacy: Pharmacy Enterprise Customization System'
section: GUI
app_status: active
pkg_ns: PECS
patch_ver: 6.2
patch_id: PECS*6.2
group_key: PECS:PECS:6.2
file_numbers: []
security_keys: []
menu_options: 0
description: Updated PECS version 6.1 references to 6.2 in the Title page and Footers Updated formatting of most figures, tables, and styles to reflect more current VA standards Updated Title page, Revision History, Table of Contents, List of Figures, List of Tables, and
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 32166
section_count: 69
table_count: 26
figure_count: 1
appendix_count: 0
has_toc: false
is_stub: false
pub_date: June 2021
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_2_1_ug_r.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_2_1_ug_r.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=204
audit_applied: '2026-05-31'
master_source: PECS Version 6.2 User Guide
master_pub_date: June 2021
consolidated_from: 2 versions
prior_versions:
- PREC*7*2 PECS User Guide
consolidated_title: pecs user guide
---

![](pecs-version-6-2-user-guide/001.png)

June 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

<table>
<caption><p><span id="_Toc75767168" class="anchor"></span>Table 1: Acronyms and Abbreviations</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th><p>Version</p>
<p>Patch No.</p></th>
<th>Description/Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>June 2021</td>
<td><p>PECS v6.2</p>
<p>PREC*6.2*1</p></td>
<td><ul>
<li><p>Updated PECS version 6.1 references to 6.2 in the Title page and Footers</p></li>
<li><p>Updated formatting of most figures, tables, and styles to reflect more current VA standards</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, List of Figures, List of Tables, and Footers</p></li>
</ul>
<p>Liberty ITS</p></td>
</tr>
<tr class="even">
<td>July 2017</td>
<td><p>PECS v6.1</p>
<p>PREC*6.1*1</p></td>
<td>Updates for 2FA Compliance and IAM SSOi integration for PIV authentication: <a href="#system-configuration">System Configuration</a>, <a href="#user-access-levels">User Access Levels</a>, &amp; <a href="#login">Login</a>. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2016</td>
<td><p>PECS v6.0</p>
<p>PREC*6.0*1</p></td>
<td>Document wide updates: New version, Section 508 compliance, grammar/format. Added SFTP to <a href="#acronyms-and-abbreviations">acronyms</a>. Replaced FTP with SFTP. – <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Nov 2014</td>
<td><p>PECS v5.0</p>
<p>PREC*5.0*1</p></td>
<td>Document wide updates: New version, Section 508 compliance, grammar/format. Corrected internal document links. Clarified sentence describing the <a href="#hardwaresoftware-components">Pre-Production and Production environments</a>, and <a href="#customize-settings">Customize Settings</a>. All references to FDB MedKnowledge Framework were reverted to FDB-DIF to correct an inaccuracy; the product name does not change until the 4.x series, not the 3.3 version of the FDB product deployed with PECS v5.0. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2014</td>
<td><p>PECS v3.0</p>
<p>PREC*3.0*1</p></td>
<td>Document wide updates: Section 508 compliance and grammar/format. Changed FDB-DIF to FDB MedKnowledge Framework. Made additional changes per CPS. Made changes per CPS: graphics caption formatting, added links, created new heading for cross-reference purposes: <a href="#drug-pair-customization-non-508-compliant-detail">Drug Pair Customization</a> and Modifying Records. – <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>April 2014</td>
<td><p>PECS v3.0</p>
<p>PREC*3.0*1</p></td>
<td>Document wide updates: grammar/format. Section 508 Compliance updates to <a href="#getting-started">Getting Started</a>. Edits to screen shots for <a href="#drug-pair-customization-non-508-compliant-detail">Drug Pair Detail</a> Screen for Multiple Customization. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Mar 2014</td>
<td><p>PECS v3.0</p>
<p>PREC*3.0*1</p></td>
<td><p>Document wide updates: Section 508 compliance and grammar/format. Added <a href="#PREC_3_0_1_ReverseDDI">Reverse DDIs</a>.</p>
<p>– <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>Jan 2014</td>
<td><p>PECS v3.0</p>
<p>PREC*3.0*1</p></td>
<td>Document wide updates: Section 508 compliance. Completed <a href="#pecs-by-tab">PECS by Tab</a>. Rearranged and rewrote major portions of guide. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Feb 2013</td>
<td><p>PECS v3.0</p>
<p>PREC*3.0*1</p></td>
<td>Document wide updates: New version, Section 508 compliance, grammar/format. Added <a href="#drug-pair-detail">FDB Drug Pair</a> content. – <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Feb 2013</td>
<td><p>PECS v2.2</p>
<p>PREC*2.2*1</p></td>
<td>Document wide updates: Section 508 compliance and grammar/format. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>June 2012</td>
<td><p>PECS v2.2</p>
<p>PREC*2.2*1</p></td>
<td><p>Document wide updates: Section 508 compliance and grammar/format. Replaced screen shots for <a href="#requestor-home-page">Requestor</a> &amp; <a href="#approver-home-page">Approver</a> home pages. Updated Quick Drug Pair selection. Added screen capture and write-up to contain info about the date from the FDB update to Null Drug Pair section. Updated <a href="#release-manager">Release Manager</a> information. Added information about CCR5122 in the <a href="#notification-of-drug-pairs-needing-action-for-an-approved-drug-drug-interaction">Notification of Drug Pairs Needing Action for an Approved Drug-Drug Interaction</a> section. Edited and obtained new screen shots for Multiple DDI records to one FDB.</p>
<p>– <mark>REDACTED</mark>, <mark>REDACTED</mark>, &amp; <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>Mar 2012</td>
<td><p>PECS v2.1</p>
<p>PREC*2.2*1</p></td>
<td>Drafted Drug Pair Notification. Record Locking. Creating Multiple Custom DDIs to One FDB Record and Prevention of Duplicate DP on Single Record. Forward/Reverse Monographs. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Feb 2012</td>
<td><p>PECS v2.1</p>
<p>PREC*2.2*1</p></td>
<td><p>Section 508 compliance completed for screen captures. Completed Record Locking. Made a few changes to the text on Edit panels. Created text for Not Editing Single Drug Pair.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>Nov 2011</td>
<td><p>PECS v2.1</p>
<p>PREC*2.2*1</p></td>
<td>Edited information from customer on Action Statuses, and added information on Saved Queries. – <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2011</td>
<td><p>PECS v2.1</p>
<p>PREC*2.2*1</p></td>
<td><p>Document wide updates: New version, Section 508 compliance, and grammar/format. Added information on potential Easy Search/PECS Record discrepancy.</p>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark>, <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>Dec 2010</td>
<td></td>
<td><p>Initial Release.</p>
<p>– <mark>REDACTED</mark> &amp; <mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<span id="_Toc75767168" class="anchor"></span>Table 1: Acronyms and Abbreviations

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
  - [Project References](#project-references)
    - [Information](#information)
    - [Coordination](#coordination)
    - [Help Desk](#help-desk)
  - [Organization of the Manual](#organization-of-the-manual)
  - [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
    - [Deployment Design – PECS](#deployment-design-pecs)
    - [Hardware/Software Components](#hardwaresoftware-components)
    - [Production Environment](#production-environment)
  - [Data Flows](#data-flows)
    - [Process Flow](#process-flow)
    - [Transaction Flow](#transaction-flow)
  - [User Access Levels](#user-access-levels)
    - [Identity Management](#identity-management)
    - [Role Assignment](#role-assignment)
    - [Role Descriptions for Identify Management](#role-descriptions-for-identify-management)
- [Customization Information](#customization-information)
  - [Drug-Drug Interaction and Professional Monograph](#drug-drug-interaction-and-professional-monograph)
  - [Duplicate Therapy](#duplicate-therapy)
  - [Dose Range](#dose-range)
- [Getting Started](#getting-started)
  - [Login](#login)
    - [Logging into PECS](#logging-into-pecs)
    - [Authentication Explanation](#authentication-explanation)
  - [Application Organization](#application-organization)
    - [Welcome and Update Information](#welcome-and-update-information)
    - [General Page Structure and Navigation](#general-page-structure-and-navigation)
    - [Home Page](#home-page)
- [PECS by Tab](#pecs-by-tab)
  - [Home](#home)
  - [Advanced Query/Customization](#advanced-querycustomization)
  - [Easy Search](#easy-search)
  - [Drug Pair Lookup](#drug-pair-lookup)
  - [Reports](#reports)
  - [Contact Us](#contact-us)
  - [Custom Updates](#custom-updates)
  - [Administration](#administration)
  - [Help](#help)
- [Using Advanced Query/Customization](#using-advanced-querycustomization)
  - [Accessing the Advanced Query/Customization Page](#accessing-the-advanced-querycustomization-page)
  - [Build a Query Panel](#build-a-query-panel)
  - [Create a Query](#create-a-query)
    - [Query Filters](#query-filters)
    - [And/Or Usage Examples](#andor-usage-examples)
    - [Query Specifics](#query-specifics)
    - [Add Default DRC Query](#add-default-drc-query)
  - [Save a Query](#save-a-query)
  - [Run a Saved Query](#run-a-saved-query)
  - [Rename a Saved Query](#rename-a-saved-query)
  - [Delete a Saved Query](#delete-a-saved-query)
  - [Query Results](#query-results)
    - [Sort Query Results](#sort-query-results)
    - [Re-Order Results Columns](#re-order-results-columns)
  - [Export Query Results](#export-query-results)
  - [Query Errors](#query-errors)
    - [Database Timeout (Too Many Results)](#database-timeout-too-many-results)
    - [Inappropriate Value](#inappropriate-value)
- [Working with Customization Requests](#working-with-customization-requests)
  - [Create a Customization Request](#create-a-customization-request)
    - [Customize a Drug-Drug Interaction Record](#customize-a-drug-drug-interaction-record)
    - [Customize Other Record Types](#customize-other-record-types)
    - [Create Customization from a Blank Form](#create-customization-from-a-blank-form)
  - [Modify Customization Requests](#modify-customization-requests)
  - [Review Customization Requests](#review-customization-requests)
  - [Approve Customization Requests](#approve-customization-requests)
  - [Reject Customization Requests](#reject-customization-requests)
  - [Delete Customization Requests](#delete-customization-requests)
  - [Record Locking Feature](#record-locking-feature)
    - [Record in Use](#record-in-use)
    - [Record Recently Modified](#record-recently-modified)
    - [Record Time-Out Lock](#record-time-out-lock)
    - [Record Navigation](#record-navigation)
- [User Roles and Tasks](#user-roles-and-tasks)
  - [Requestor](#requestor)
    - [Requestor Home Page](#requestor-home-page)
    - [My Request History: Requestor](#my-request-history-requestor)
    - [Additional Tools Available to Requestors](#additional-tools-available-to-requestors)
  - [Approver](#approver)
    - [Approver Home Page](#approver-home-page)
    - [My Request History: Approver](#my-request-history-approver)
    - [My Assigned Requests for Review](#my-assigned-requests-for-review)
    - [My Assigned Requests for Approval](#my-assigned-requests-for-approval)
    - [My Assigned Requests for Deletion](#my-assigned-requests-for-deletion)
    - [Unassigned Requests](#unassigned-requests)
    - [All Requests](#all-requests)
    - [Additional Tools Available to Approvers](#additional-tools-available-to-approvers)
  - [Release Manager](#release-manager)
    - [Release Manager Home Page](#release-manager-home-page)
    - [Custom Update Tab](#custom-update-tab)
    - [Custom Update Overview](#custom-update-overview)
    - [Update Files Explained](#update-files-explained)
    - [Create a Custom Update](#create-a-custom-update)
    - [Review Custom Update History](#review-custom-update-history)
    - [Additional Tools Available to Release Managers](#additional-tools-available-to-release-managers)
  - [Administrator](#administrator)
    - [Administrator Home Page](#administrator-home-page)
    - [Administration Tab](#administration-tab)
    - [Customize Settings](#customize-settings)
    - [Change Field Display Order](#change-field-display-order)
    - [Update User Roles](#update-user-roles)
    - [Null Drug Pair Removal Process](#null-drug-pair-removal-process)
    - [Editing Contact Us](#editing-contact-us)
    - [Add a Contact Link](#add-a-contact-link)
    - [Edit a Contact Link](#edit-a-contact-link)
    - [Additional Tools Available to Administrators](#additional-tools-available-to-administrators)
- [Easy Search](#easy-search-1)
  - [Easy Search Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy Query](#easy-search-drug-drug-interaction-with-professional-monograph-andor-duplicate-therapy-query)
  - [Easy Search Interactions for a Single Drug Query](#easy-search-interactions-for-a-single-drug-query)
  - [Easy Search Dose Range Query](#easy-search-dose-range-query)
  - [Potential Easy Search Result and PECS Record Discrepancy](#potential-easy-search-result-and-pecs-record-discrepancy)
- [Drug Pair Lookup](#drug-pair-lookup-1)
  - [Performing a Drug Pair Lookup Query](#performing-a-drug-pair-lookup-query)
  - [Export Query Results](#export-query-results-1)
- [Detail Pages](#detail-pages)
  - [Detail Page Overview](#detail-page-overview)
    - [Informational and Warning Messages](#informational-and-warning-messages)
  - [Using Detail Pages](#using-detail-pages)
    - [Viewing Record Details](#viewing-record-details)
    - [Edit a Record](#edit-a-record)
    - [Print a Record](#print-a-record)
    - [Add Pre-Customization Comments](#add-pre-customization-comments)
    - [View Associated Record Links](#view-associated-record-links)
    - [History Report](#history-report)
    - [Field-Level History Table](#field-level-history-table)
    - [Export Date](#export-date)
  - [Drug-Drug Interaction Detail](#drug-drug-interaction-detail)
    - [Multiple VA Customizations for One FDB Record](#multiple-va-customizations-for-one-fdb-record)
    - [Create Multiple Customizations from One FDB Record](#create-multiple-customizations-from-one-fdb-record)
    - [Cannot Add Identical Drug Pairs to Same DDI](#cannot-add-identical-drug-pairs-to-same-ddi)
    - [Reverse Drug-Drug Interactions](#reverse-drug-drug-interactions)
    - [Working with Drug Pairs within the DDI](#working-with-drug-pairs-within-the-ddi)
    - [Fields](#fields)
  - [Drug Pair Detail](#drug-pair-detail)
    - [Fields and Other Information](#fields-and-other-information)
    - [Finding Drug Pairs](#finding-drug-pairs)
    - [FDB Drug Pair Detail Page](#fdb-drug-pair-detail-page)
    - [VA Customized Drug Pair Detail Page](#va-customized-drug-pair-detail-page)
  - [Drug Pair Customization (Non 508-Compliant) Detail](#drug-pair-customization-non-508-compliant-detail)
    - [Drug Pairs Panel](#drug-pairs-panel)
    - [Notification of Drug Pairs Needing Action for an Approved Drug-Drug Interaction](#notification-of-drug-pairs-needing-action-for-an-approved-drug-drug-interaction)
    - [Customizing Drug Pairs from the Selection List](#customizing-drug-pairs-from-the-selection-list)
    - [Review a Drug Pair](#review-a-drug-pair)
  - [Section 508 Compliant Drug Pair Customization Detail](#section-508-compliant-drug-pair-customization-detail)
    - [Select Drug Pairs to Add to the Above VA Custom Interaction Panel](#select-drug-pairs-to-add-to-the-above-va-custom-interaction-panel)
  - [Professional Monograph Detail](#professional-monograph-detail)
    - [Fields](#fields-1)
    - [Buttons](#buttons)
    - [Forward and Reverse Professional Monograph](#forward-and-reverse-professional-monograph)
  - [Duplicate Therapy Detail](#duplicate-therapy-detail)
    - [Fields](#fields-2)
    - [Buttons](#buttons-1)
  - [Dose Range Detail](#dose-range-detail)
    - [Dose Range Concept Types](#dose-range-concept-types)
    - [Fields](#fields-3)
    - [Buttons](#buttons-2)
- [Sample Modification Scenarios](#sample-modification-scenarios)
  - [Duplicate Therapy Modification](#duplicate-therapy-modification)
    - [Process Steps](#process-steps)
  - [Duplicate Therapy Approval](#duplicate-therapy-approval)
    - [Process Steps](#process-steps-1)
  - [Drug Interaction Research](#drug-interaction-research)
    - [Process Steps for Severity Check, Case 1](#process-steps-for-severity-check-case-1)
  - [Drug Interaction Severity Change](#drug-interaction-severity-change)
    - [Process Steps for Editing Case 1](#process-steps-for-editing-case-1)
  - [Drug Interaction Severity Change](#drug-interaction-severity-change-1)
    - [Process Steps for Editing Case 2](#process-steps-for-editing-case-2)
  - [Remove Drug Pair from Interaction](#remove-drug-pair-from-interaction)
    - [Process Steps](#process-steps-2)
  - [Create Professional Monograph](#create-professional-monograph)
    - [Process Steps](#process-steps-3)
- [Contact Us](#contact-us-1)
- [Reports](#reports-1)
  - [Active Customization Reports](#active-customization-reports)
    - [FDB Custom Dose Range Report](#fdb-custom-dose-range-report)
    - [FDB Custom Drug-Drug Interaction Report](#fdb-custom-drug-drug-interaction-report)
    - [FDB Custom Duplicate Therapy Report](#fdb-custom-duplicate-therapy-report)
    - [FDB Custom Professional Monograph Report](#fdb-custom-professional-monograph-report)
    - [Deleted Monograph Customization Report](#deleted-monograph-customization-report)
    - [Null Drug Pairs Customization Report](#null-drug-pairs-customization-report)
  - [FDB Comparison Reports](#fdb-comparison-reports)
    - [FDB Comparison Drug-Drug Interaction/Drug Pair Report](#fdb-comparison-drug-drug-interactiondrug-pair-report)
    - [Structure of the FDB Comparison Report](#structure-of-the-fdb-comparison-report)
    - [FDB Comparison Duplicate Therapy Report](#fdb-comparison-duplicate-therapy-report)
    - [FDB Comparison Dose Range Report](#fdb-comparison-dose-range-report)
- [Online Help](#online-help)
  - [Accessing Online Help](#accessing-online-help)
The Pharmacy Enterprise Customization System (PECS) is a Graphical User Interface (GUI) application that currently allows the VA's Pharmacy Benefits Management (PBM) pharmacists and Automated Data Processing Application Coordinators (ADPACs) to customize the contents of the following five business concepts:
- Drug-Drug Interaction
- Drug Pair
- Duplicate Therapy
- Dose Range
- Professional Monograph

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user guide is to provide a general overview of the PECS application, as well as more detailed working information. It also provides reference material and task-based instructions for entering and approving Drug-Drug Interaction, Drug Pair, Duplicate Therapy, Dose Range, or Professional Monograph Customization Requests.

## Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a VA provider orders a drug for a patient (either through CPRS \[Computerized Patient Record System\] or VistA), the Medication Order Check Healthcare Application (MOCHA) performs order checks on that drug, and alerts the provider if the drug they are ordering has any of the following anomalies:

- Causes an interaction with other drugs the patient is taking
- Is in the same Therapeutic Class as other drugs the patient is taking
- Is prescribed in a dose that is incompatible with patient factors such as age, weight and Body Surface Area (BSA)

The drug information used as a basis for these order checks comes from a Commercial Off the Shelf (COTS) product provided by First Databank (FDB) called the Drug Information Framework (FDB-DIF).

Sometimes, the information provided by FDB is not optimal for the VA Providers or the Veteran community they serve. The primary purpose of the Pharmacy Enterprise Customization System (PECS) is to give Pharmacy Benefits Management (PBM) the ability to customize the drug information provided by FDB so the order checks and resulting alerts are based on drug information tailored specifically for the VA.

The major users of PECS are Pharmacy Benefits Management (PBM) personnel and the Automated Data Processing Application Coordinators (ADPACs) who will research and request the customization of FDB data. Once approved by the National Drug File (NDF) committee members, the changes made will affect all of the VA sites throughout the country to where the data is sent and used in the enhanced order check. The order check is used by VA physicians and pharmacists to see if any serious drug conflicts occur with the patients' existing medication. It will also check for duplication of therapy of other prescribed drugs also taken by the VA patient.

The advantages to the VA for using PECS are as follows:

- All customizations will be performed at the National level to provide consistent order checks between facilities.
- Use of First Databank for drug interaction, duplicate therapy, and dosing data.
- More specificity in drug interaction order checks with the ability to include or exclude dose routes.
- More specificity in duplicate therapy order checks with FDB data.
- Weekly FDB updates with monthly customization updates.
- More frequent customization updates when needed.

## Project References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Guide relies on the following documents, which can be found here:

http://vaww.<span class="mark">REDACTED</span>/projects/pre/PRE_IPT_Rev/PRE_IPT_Rev_PECS/Lists/PECS%20v50%20Review/AllItems.aspx

> **NOTE:** Due to policy constraints, active links cannot be included in this document. Please copy and paste the URLs into your browser.

- PECS Requirements Specification Document (RSD)
- Pharmacy Reengineering (PRE) Configuration Management Plan (CMP)
- PECS Database Design Document
- PEPS Style Guide
- PECS Project Architecture Document
- PECS Interface Control Document
- PECS Production Operations Manual (POM)

### Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to policy constraints, this document cannot support live links. Please copy and paste the links into your browser.

Project contacts for PD PRE PECS project are as follows:

- Office of Information & Technology (OIT) Product Development (PD) Program Manager
- OIT PD Project Manager PECS
- Business Sponsor/Stakeholder
- Business Subject Matter Expert (SME)/Lead Clinical Analyst

The current names of those serving these roles can be found in the organization chart for PD PRE: Be sure to look at the tab for PECS:  
http://vaww.<span class="mark">REDACTED</span>/projects/pre/OverArching%20Documents/PRE_Organization_Chart_all%20tabs.pdf

These people can be contacted through the Global Address List (GAL).

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any coordination activities that must occur will take place between the PBM group and their ADPACs. If something has to be escalated, the ADPACs will have specific procedures for each site.

### Help Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site needs to use the help desk escalation that they normally use. Since each site is different, the only instructions for users are to go their ADPACs and to report issues.

See the Contact Us tab in the PECS Application for guidance.

## Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

An overview of the PECS system and this User Guide

System Summary

A more detailed description of the PECS system including a non-technical overview of the product design, data flow, and application access

Customization Information

Provides a brief overview of customizations and how they're created in PECS

Getting Started

Discusses logging into PECS and the organization of the application

PECS by Tab

PECS functions are organized into Tabs. PECS by Tab describes the tabs found in PECS

Using Advanced Query/Customization

Instruction on using Advanced Query/Customization feature

Working with Customization Requests

Instruction on how to create and process customization requests

User Roles and Tasks

Information on PECS User Roles and the functions they perform

Easy Search

Instruction on using the Easy Search feature

Drug Pair Lookup

Instruction on using the Drug Pair Lookup feature

Detail Pages

Description of the Detail Pages

Sample Modification Scenarios

Sample scenarios on why a record would be customized and the steps to make the customization

Contact Us

Information about the Contact Us page

Reports

Information about PECS Reports

## Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Acronyms and Abbreviations used in this document.

| Term     | Definition                                                                                                          |
|----------|---------------------------------------------------------------------------------------------------------------------|
| ADPAC    | Automated Data Processing Application Coordinator                                                                   |
| AITC     | Austin Information Technology Center                                                                                |
| API      | Application Program Interface                                                                                       |
| BSA      | Body Surface Area                                                                                                   |
| COTS     | Commercial Off-the-Shelf                                                                                            |
| CPRS     | Computerized Patient Record System                                                                                  |
| DATUP    | Application that implements the FDB-DIF update business logic using the FDB Updater APIs to process the update file |
| FDB      | First Databank                                                                                                      |
| FDB-DIF  | First Databank Drug Information Framework database                                                                  |
| FTP      | File Transfer Protocol                                                                                              |
| GCN      | Generic Code Number                                                                                                 |
| GUI      | Graphical User Interface                                                                                            |
| J2EE     | Java 2 Enterprise Edition                                                                                           |
| KAAJEE   | Kernel Authentication and Authorization for J2EE                                                                    |
| NDF      | National Drug File                                                                                                  |
| OIT/OI&T | Office of Information and Technology (verify which to use).                                                         |
| PBM      | Pharmacy Benefits Management                                                                                        |
| PD       | Product Development                                                                                                 |
| PECS     | Pharmacy Enterprise Customization System                                                                            |
| PEPS     | Pharmacy Enterprise Product System                                                                                  |
| PRE      | Pharmacy Reengineering                                                                                              |
| RSD      | Requirements Specification Document                                                                                 |
| SFTP     | Secure File Transfer Protocol                                                                                       |
| URL      | Uniform Resource Locator                                                                                            |
| VA       | Department of Veterans Affairs                                                                                      |
| VAMC     | VA Medical Center                                                                                                   |
| VistA    | Veterans Health Information Systems and Technology Architecture                                                     |
| VPN      | Virtual Private Network                                                                                             |

<span id="_Toc75767169" class="anchor"></span>Table 2: Build a Query Panel Fields

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Enterprise Customization System (PECS) was born out of the need to support enhanced order checks. A decision was made to replace the home-grown order checking process, implemented in M, with a COTS product (FDB-DIF). However, the VA desired to be able to customize the drug information (such as drug interaction severity, monographs etc.) existing in FDB. PECS will satisfy this need, while adhering to stringent requirements intended to ensure patient safety.

The PECS application is designed with the following functionality:

- Allows customization of FDB data used in the enhanced order checking by National Drug File (NDF) Managers
- Provides access to GUI customization application by facility users to request custom changes
- Provides role based system accessibility
- Provides a report to list all customizations created to date compared against corresponding FDB standard reference data
- Provides a process to allow drug interaction information in VistA to be transferred to the custom tables
- Provides a process via Secure File Transfer Protocol (SFTP) to update from a national database to all local/regional instances of FDB standard and custom tables

PECS is developed to allow easy customization of FDB standard reference tables such as Duplicate Therapy, Dose Range, Drug-Drug Interaction, and Drug-Drug Interaction Professional Monograph, which are used in the enhanced order checking by the MOCHA system.

In more detail, PECS does the following:

- Allows users to customize the FDB standard reference tables used in the enhanced order checking that will be used by the Pharmacy Benefits Management (PBM) group, the Automated Data Processing Application Coordinators (ADPACs), and National Drug File (NDF) managers or designees to enter and update the custom table values.
- Allows users to do the following customizations:
  - A custom drug-drug interaction, and any important attributes for that interaction
  - Drug pairs associated with a custom drug-drug interaction
  - A custom Professional Monograph for a drug-drug interaction, including any important attributes
  - A custom duplication allowance value for a duplicate therapy class
  - Custom values for attributes associated with a custom dose range check table
- Provides a Searching capability for a user to see Drug-Drug Interaction, Duplicate Therapy, or Professional Monograph information separately or together, for chosen drugs.
- Provides the following reports:
  - History of custom changes for each of the five concepts
  - Exportable FDB or Custom Data - Individual query data can be exported from the five FDB-DIF or Custom tables. The available format is Excel
  - FDB Comparison Reports to compare incoming updated FDB data against VA customized data to help determine if the VA customized data needs to be modified
- Provides a process via SFTP to transfer Custom data from a National server to all local/regional instances servers.
- Leverages the existing FDB data loader utility at each site that is used to update the FDB-DIF databases.

Custom table content distribution involves using an automated utility, Data Update (DATUP). The distribution method supports the following data content scenarios:

- Only FDB standard reference table data.
- FDB standard reference table data and Custom table data.
- Only Custom table data.

Custom table content distribution supports both periodic and as-needed releases.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is installed in two environments at the Austin Information Technology Center (AITC) in Austin, TX: Pre-Production and Production. The new PECS build, database changes (updates), security patches, etc., are first applied to PECS Pre-Production and then on successful deployment promoted to PECS Production.

### Deployment Design – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 shows the overview of the logical deployment design for the PRE PECS Application.

Application Server

The WebLogic Application Server 12.1.3 will host PRE PECS and its business services.

Data Base Server

The Database Server software is Oracle 11g running on Red Hat Linux Enterprise version RHEL6. It will host the Custom Table Staging database and FDB-DIF database.

Failover Server

The Failover Server will host both the BEA WebLogic Application Server and Oracle Database Server to provide redundancy.

IAM SSOi Interface

Identity and Access Management Single Sign On internal service used for PIV authentication.

<span id="_Ref418173580" class="anchor"></span>Figure 1: Logical Deployment Design for the PRE PECS Application

![](pecs-version-6-2-user-guide/002.png)

### Hardware/Software Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hardware/Software components and deployment architecture of the Pre-Production and Production environments are the same. The PECS Application and database are kept in synchronization for both.

<span id="_Toc346797061" class="anchor"></span>Figure 2: PECS High Level Deployment Design

![](pecs-version-6-2-user-guide/003.png)

### Production Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3 shows the Production environment that will be supported, and the local networks to which they will be attached for Local VA Medical Centers (VAMC), where PECS users are located.

<span id="_Ref413318986" class="anchor"></span>Figure 3: Production Environment for PECS

![](pecs-version-6-2-user-guide/004.png)

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Process Flow 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 4 shows the life cycle of a customization change from the Requestor entry to the point the record is ready to be sent to the production FDB Drug Information Framework (DIF) custom table. The updates and changes are made and maintained in a Staging Table. Records are not extracted until the Release Manager submits approved changes. Records are then formatted and placed in a directory where they will be updated to production. The process that updates these records uses software named DATUP.

<span id="_Ref355339808" class="anchor"></span>Figure 4: PECS Customization Life Cycle

![](pecs-version-6-2-user-guide/005.png)

### Transaction Flow 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 5 depicts the Action Statuses of a record's transition from creation to approval.

<span id="_Ref413319617" class="anchor"></span>Figure 5: Action Statuses

![](pecs-version-6-2-user-guide/006.png)

Action Statuses

This list displays the different Action Statuses a VA customized record may go through as it steps through the approval workflow within PECS. Note that only seven of the following eleven states are displayed in the user interface - in other words, some of this information is "behind-the-scenes." It is included here for informational purposes only.

- *<u>New</u>* - A new customization request has been created. If a user has the appropriate authority, they may modify the request (Modified) to be completed at a later point. Then, if they have the proper authority, they may submit the request as reviewed (Reviewed).
- *<u>Modified</u>* - A user can make changes to their own New requests. The record will remain Modified until a user with the proper authority (Approver role) reviews the request and submits the request as Reviewed.
  - *<u>Modified After Approve</u>- (displays as Modified)* A user with the proper authority has requested a change in the Approved customization that requires another approval process.
  - *<u>Modified After Delete</u>* - *(displays as Modified)* A user with the proper authority has requested the deleted record be considered again for Approval with or without modifications. This requires another approval process.
- *<u>Reviewed</u>* - This is the first stage of approval. A user with the proper authority (Approver role) reviews the new or modified customization request and submits it as Reviewed. The approver may also reject or modify the request. Note that an approver can review their own requests but not approve them.
  - *<u>Reviewed After Approve</u>* - *(displays as Reviewed)* Modifications were made to an approved record. A user with the proper authority (Approver role) reviews the request and submits it as Reviewed. The Approver may also reject the request, in which case the record returns to the Approved state, or they may modify it.
  - *<u>Reviewed After Delete</u>* - *(displays as Reviewed)* Modifications were made to a deleted record. A user with the proper authority (Approver role) reviews the request and submits it as Reviewed. The Approver may also reject the request, in which case the record returns to Deleted state, or they may modify it.
- *<u>Rejected</u>* - The customization request is in a Rejected state. At this point the user may make changes, resubmit, or allow the customization to remain in Rejected state. All records that are rejected or not approved will remain in that state and will be available to the user for any future changes.
- *<u>Approved</u>* - This is the second stage of approval. A user with the proper authority (Approver role) who did *not* submit the request as Reviewed will review the record and may approve, reject, or modify the request.
- <u>*DeleteReviewed*</u> - The record remains active but a user with the proper authority (Approver role) has requested deletion of an existing approved customization.
- *<u>Deleted</u>* - A user in the Approver role who did *not* submit the request for Deletion may delete the customization. If an Approver confirms the deletion, the record will remain active for potential future modifications.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application is accessible only by users signed directly into the VA network, or by users signed into the VA network via approved virtual private network (VPN) software. User authentication into the VA network is a precondition of PECS application access. Application authentication and authorization will be controlled by the VA two factor authentication (2FA) using IAM SSOi. Privileges are granted by PECS Administrators.

In order to log in to the application, each user must have a valid PIV card. At the SSOi login screen, users are prompted to login using their PIV or Windows credentials.

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to PECS is a two-step process. Authentication is handled through the IAM SSOi service and user role-based authorization is handled within the PECS application. The roles (Requestor, Approver, Release Manager and Administrator) have a set of permissions within PECS that allow them to perform specific tasks. A PECS user can hold multiple roles and would have access to all the functions associated with each role. All VA users have the default Requestor role. The requests for other roles with more privilege must go to the PBM NDF Managers and the roles can be granted through the PECS UI.

### Role Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the PIV authentication, users must be assigned to roles by a PECS Administrator in User Roles. The exception is the Requestor role (the least-privileged access to PECS), which does not require specific assignment by an Administrator. See Update User Roles for additional information.

### Role Descriptions for Identify Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is a list of roles available within the application, and a description of what each role can do:

- Requestor: Creates Customization Requests.
- Approver: Creates Customization requests and Reviews and Approves Customization Requests created by other users
- Release Manager: Generates Custom Update Files; Reviews existing Custom Updates.
- Administrator: Grants/Removes User Role privileges; Updates Concepts Settings; Edits content on the Contact us page.

# Customization Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Customization Information section describes the customizations that can be done through PECS.

## Drug-Drug Interaction and Professional Monograph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 6 displays how a Drug-Drug Interaction is tied to Drug Pairs and Professional Monographs: More information on Drug-Drug Interactions, Drug Pairs, and Professional Monographs is provided later in the manual.

<span id="_Ref413402198" class="anchor"></span>Figure 6: Drug-Drug Interaction Relationship

![](pecs-version-6-2-user-guide/007.png)

FDB Drug-Drug interaction severity levels:

1 = Contraindicated

2 = Severe

3 = Moderate

9 = Undetermined severity – Alternate therapy

Within the VA system an FDB or VA Custom drug-drug interaction of severity level 1 will return a Critical order check and severity level 2 will return a Significant order check. Severity levels 3 and 9 will not return an order check.

Types of drug-drug interaction customizations include:

- Change in severity level
- Add or remove drug pairs
- Create drug interactions not found in FDB

> **NOTE:** Due to the millions of possible drug pair combinations, you must be very specific on which two products are involved when reporting problems with the system.

## Duplicate Therapy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duplicate Therapy concept allows you to specify the maximum number (0, 1, 2, 3, or 4) of duplicate therapy matches that can occur within a therapeutic class without creating an order check. A '0' duplicate allowance means only 1 medication from that therapeutic class can be on the patient profile without getting an order check (zero duplication). If a second drug from that class is added, then the provider gets the order check. If the allowance is '1', two drugs can be on the patient profile at once, the 3rd drug added would get the check (one duplication), etc.

The only type of Duplicate Therapy customization allowed is to increase or lower the duplicate therapy allowance for a therapeutic category.

## Dose Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Dose Range is the allowable dosage of a drug based on a number of factors such as patient age, weight, and Dose Route. PECS allows you to modify the Dose Ranges included in the FDB-DIF product.

- Dosing is based on the GCN (Generic Code Number) Sequence Number (GCNSEQNO), a number specific to all drug products with the same generic ingredient(s), route of administration, drug strength(s) and dosage form.
- Dosing is age-specific for most products. FDB has dosing for neonatal, infant, adolescent, adult, and geriatric. All ages are by days, for example, 18 years x 365= 6570 days.
- FDB also has indication-specific dosing, and dosing type. Examples of dosing type are loading, maintenance, single, and initial.
- A typical product may have 30 or more dosing records when all variables are taken into consideration.
- The initial implementation of dosing order checks within VistA looks at the maximum single dose and daily dose range order checks using a common indicator.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Getting Started section provides information that is essential for a user to get started with PECS.

## Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS requires the user to login to prevent unauthorized users from accessing the system and to establish identity for their actions within the application. Note that authentication is handled using the IAM SSOi service via PIV authentication. Authorization is handled using a number of roles for users (Requestor, Approver, Release Manager and Administrator) and each role has a set of permissions. All VA users have the default Requestor role. The roles with higher privileges can be granted through the PECS UI by the [PBM NDF Managers](mailto:pbmNDF@va.gov). To see the list, refer to the Identity Management section.

<span id="_Toc75767203" class="anchor"></span>Figure 7: IAM Single Sign-On Screen

![](pecs-version-6-2-user-guide/008.png)

### Logging into PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To login to PECS:

1.  On the SSOi Login Screen, choose Sign in using VA PIV Card and enter PIN

<span id="_Toc75767204" class="anchor"></span>Figure 8: PECS Help Window

![](pecs-version-6-2-user-guide/009.png)

2.  After entering PIV credentials, PECS displays the Confidentiality Statement. You must agree to this statement to continue. Click Agree.

<span id="_Toc75767205" class="anchor"></span>Figure 9: PECS Help Window

![](pecs-version-6-2-user-guide/010.png)

### Authentication Explanation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application authentication is controlled by VA two factor authentication (2FA) with PIV using the IAM SSOi system. On successful login, the system displays the PECS Home page.

## Application Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is organized into a set of tabs. Only tabs that are relevant to the users role are displayed; for example, a Requestor user will see different tabs than an Approver user.

<span id="_Toc403984389" class="anchor"></span>Figure 10: PECS Tab Groups Displayed

![](pecs-version-6-2-user-guide/011.png)

All available tabs in PECS are listed below. Tab availability by user role and function will be discussed in more detail later in the User Guide.

- Home
- Advanced Query / Customization
- Easy Search
- Drug Pair Lookup
- Reports
- Help
- Contact Us
- Custom Updates
- Administration

See PECS by Tab for additional information.

### Welcome and Update Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Welcome and Update Information section at the top of the Home page displays the current user's account name and the dates of the last FDB-DIF Update and the last Custom Update.

<span id="_Toc403984390" class="anchor"></span>Figure 11: Welcome Text and Update Information

![](pecs-version-6-2-user-guide/012.png)

To Those Using Screen-Reading Assistive Technology

The window that displays the PECS tab groups also contains a link at the top, "Go to Main Content." This link is for screen readers to jump directly to the main content of the selected tab and not read each and every tab every time a tab is selected.

<span id="_Toc403984391" class="anchor"></span>Figure 12: PECS Tab Groups with "Go to Main Content" Link

![](pecs-version-6-2-user-guide/013.png)

### General Page Structure and Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All PECS application pages have certain features that provide information and help navigate the system.

Header

The PECS Header shows the Name of the current user and contains a Logout link for exiting the PECS application.

Tabs

The Tab row is used to access PECS functions.

Content

The tools (such as build a query) or content (such as a customization request) are displayed here.

Footer

The footer contains navigation links; this is a duplicate of the tabs. The application version is also displayed here.

### Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page is the first page that the user sees after logging into PECS, and is organized into panels containing specific information; only panels that are appropriate to the role of the current user are displayed. The Home page provides summary counts of the number of active customization records accessible to the current user. Additionally, it displays when the last update to the First Databank DIF database tables occurred and when the last customization update file was created.

# PECS by Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tabs provide the organization for the functions provided by PECS. This section provides an overview of the tabs and their functions. The tabs themselves are explained in more detail later in the user guide.

## Home

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

The PECS Home tab is the first page you see after a successful login, and can be used to return to this page at any time. The appearance of the home tab is role-specific; what appears on the page is different depending on the role associated with your login credentials.

See the Home Page section in Getting Started for additional information, as well as the role-specific home page sections in User Roles and Tasks.

<span id="_Toc403984430" class="anchor"></span>Figure 13: Requestor Home Page

![](pecs-version-6-2-user-guide/014.png)

## Advanced Query/Customization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Advanced Query/Customization tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

Searching for records is the one common task for all roles in PECS. It is done from the Advanced Query/Customization tab which is available to all users.

The Query Builder Panel on the Advanced Query/Customization page allows you to retrieve a specified set of records from the VA Custom Tables, the FDB standard tables, or both in order to perform research, make customizations, make customization changes, or export data. You can use it to create a new query, load a query you have previously saved, or load a query saved by another user.

<span id="_Toc403984431" class="anchor"></span>Figure 14: Advanced Query/Customization Window with Sample Data

![](pecs-version-6-2-user-guide/015.png)

For detailed information on Advanced Query/Customization, see Using Advanced Query/Customization.

## Easy Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Easy Search tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

Easy Search provides a simple way to display commonly-requested PECS information. Easy Search differs from other methods for finding information in that the results are display-only; the records displayed as a result of an Easy Search query cannot be modified. However, in some cases, a link is provided to an editable version of the resulting records.

<span id="_Toc403984432" class="anchor"></span>Figure 15: Initial Easy Search Window

![](pecs-version-6-2-user-guide/016.png)

For additional information, see Easy Search for additional information.

## Drug Pair Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug Pair Lookup tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

The Drug Pair Lookup tab provides the ability to perform a quick search on the most common elements of a drug pair: Generic Drug Name A, Generic Drug Name B, Interaction, and the Severity Code.

<span id="_Toc403984440" class="anchor"></span>Figure 16: Drug-Drug Pair Lookup Window

![](pecs-version-6-2-user-guide/017.png)

For additional information, see Drug Pair Lookup.

## Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports tab is available to the following type of PECS users:

- Approver
- Administrator

Note to Assistive Technology Users: Please refer to the documentation included with your screen reader for commands related to reading column and row headers.

The Reports tab displays a list of available reports in PECS.

<span id="_Toc403984441" class="anchor"></span>Figure 17: List of Reports

![](pecs-version-6-2-user-guide/018.png)

There are two types of Reports:

- Active Customization Reports
- FDB Comparison Reports

Reports are generated in the form of Excel spreadsheets. To run a Report, click the associated link. For additional information, see Reports.

## Contact Us

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Contact Us tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

The Contact Us page contains a list of PECS Project Contacts should you need additional information about the PECS product. The content of the Contact Us page is decided by users with the Administrator role. Contact Us may include links that allow you to send that person (or group) an email.

> **NOTE:** Clicking the link opens your mail application and a new email message to the person specified in the properties of the link. This may produce a warning message. This is normal.

<span id="_Toc403984444" class="anchor"></span>Figure 18: Example of Contact Us Data

![](pecs-version-6-2-user-guide/019.png)

Note that the above example is only an example – it can be changed to display just about anything.

See Contact Us for additional information.

## Custom Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Custom Updates tab is available to the following type of PECS users:

- Release Manager

The Custom Updates tab is seen and used by a Release Manager to generate a zip file containing files for each Order Check in the FDB update file format. Both update files are created by clicking the "Create New Update" button.

<span id="_Toc403984445" class="anchor"></span>Figure 19: Custom Updates Tab for Release Manager

![](pecs-version-6-2-user-guide/020.png)

## Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administration tab is available to the following type of PECS users:

- Administrator

The Administration tab is used only by PECS users with Administrator privileges to perform specialized tasks such as modifying certain aspects of the PECS environment, adding or deleting Approver users, and removing Null Drug Pairs.

<span id="_Toc403984446" class="anchor"></span>Figure 20: Administrator's Home Page

![](pecs-version-6-2-user-guide/021.png)

See Administrator for additional information.

## Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help tab is available to the following type of PECS users:

- Requestor
- Approver
- Release Manager
- Administrator

The Help tab launches the PECS Online Help System and displays the "front page" of the Help System. To get context-sensitive help, click the Page Help link on the page you need help with.

<span id="_Toc75767217" class="anchor"></span>Figure 21: PECS Help Window

![](pecs-version-6-2-user-guide/022.png)

See Online Help for additional information.

# Using Advanced Query/Customization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Searching for records is a task common to all PECS roles. Advanced Query/Customization is the most comprehensive way to find PECS records. Advanced Query/Customization can be used to find both VA customizations and FDB records so that they can then be customized.

## Accessing the Advanced Query/Customization Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Query Builder (Build a Query) Panel on the Advanced Query/Customization page to retrieve a specified set of records from either the VA Custom Tables, the FDB standard tables, or both. This allows you to perform research, make customizations, change existing customization, or export data. In the Query Builder Pane, you can create new queries or load previously-saved queries (either yours or a query saved by another user).

There are three ways to display the Advanced Query/Customization page:

1.  Click the Advanced Query/Customization tab on the navigation bar near the top of the page. This will open a blank query:

<span id="_Toc75767218" class="anchor"></span>Figure 22: Advanced Query/Customization Tab

![](pecs-version-6-2-user-guide/023.png)

3.  Click the Advanced Query/Customization link on the footer near the bottom of the page. This will open a blank query:

<span id="_Toc75767219" class="anchor"></span>Figure 23: Advanced Query/Customization Footer Link

![](pecs-version-6-2-user-guide/024.png)

4.  Click a link from one of the summary tables displayed on the Home tab. This will generate a query appropriate to the context of the link that was clicked. In the example below, a query displaying criteria to display the unassigned Drug-Drug Interaction records will be produced.

<span id="_Toc75767220" class="anchor"></span>Figure 24: PECS Help Window

![](pecs-version-6-2-user-guide/025.png)

## Build a Query Panel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To build a new query first select a Concept (type of record) and the source for the record you want to find. The concepts are Drug-Drug Interaction, Drug Pair, Professional Monograph, Duplicate Therapy, and Dose Range.

<span id="_Toc403984397" class="anchor"></span>Figure 25: Advanced Query/Customization Build a Query Panel – New Query

![](pecs-version-6-2-user-guide/026.png)

After selecting values for the Select Concept and Select VA, FDB, or Both fields, additional fields display, through which you can create your Query.

| Field Name                            | Definition                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fields                                | Select the field you want to query from the Fields list. The available fields are specific to the selected Concept.                                                                                                                                                                                        |
| Filter                                | Select a filter for the field from the Filter list (Contains, Equal To, etc.) See Query Filters for additional information.                                                                                                                                                                                |
| Value                                 | Enter search criteria in the Value field. Appropriate values are dictated by what was selected from the Fields list.                                                                                                                                                                                       |
| And/Or                                | Use the And/Or field to create complex queries by adding additional search criteria. If the query must meet multiple criteria, use AND; if a value from a list of criteria is acceptable, use OR. AND and OR can be combined when building the query. See And/Or Usage Example for additional information. |
| Query button                          | Click Query to run the query you have built or loaded                                                                                                                                                                                                                                                      |
| Add Default DRC Query button          | Dose Range Queries Only: Adds two standard criteria (Concept Type = '6' and AGEHIGHINDAYS \>= '6570) to the query. You should enter your specific criteria before clicking Add Default DRC Query.                                                                                                          |
| 'Include Historical Records' checkbox | Select Include Historical Records to include inactive historical records in the Query results. Historical records can only be viewed not modified. A Historical Record is any previous version of a record.                                                                                                |
| 'Clear Query' button                  | Click Clear Query to delete the current query; only the Concept Type and record source will remain.                                                                                                                                                                                                        |
| 'Query Name'                          | Enter a name for the current query if you want to save it. The name should be as descriptive as possible so that you (and other users) will understand what results the query will produce.                                                                                                                |
| 'Save Query' button                   | Click Save Query to save the current query for later use. If the Query Name field is blank, this button is inactive.                                                                                                                                                                                       |

<span id="_Toc75767170" class="anchor"></span>Table 3: Query Filters

## Create a Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a query:

1.  On the Advanced Query/Customization tab, select a Concept.

<span id="_Toc75767222" class="anchor"></span>Figure 26: Build a Query Concept Field

![](pecs-version-6-2-user-guide/027.png)

5.  Select the data you want to view – VA, FDB, or Both.

<span id="_Toc75767223" class="anchor"></span>Figure 27: Query Data Field

![](pecs-version-6-2-user-guide/028.png)

6.  In the "Enter a value to build a query" area, select the Field you want to use as a query criteria. The available field options will be determined by the Concept you selected earlier.

<span id="_Toc75767224" class="anchor"></span>Figure 28: Query Criteria Field Selection

![](pecs-version-6-2-user-guide/029.png)

7.  Select the Filter you want to impose on the Field. See Query Filters for additional information.

<span id="_Toc75767225" class="anchor"></span>Figure 29: Query Filter Field

![](pecs-version-6-2-user-guide/030.png)

8.  Enter a Value to use as your query criteria. The Value must be appropriate for the selected Field and Filter or an error message is displayed in the Results panel. See Query Specifics for additional information.

<span id="_Toc75767226" class="anchor"></span>Figure 30: Query Value Field

![](pecs-version-6-2-user-guide/031.png)

9.  To add additional criteria to the query, make a selection from the And/Or list.

<span id="_Toc75767227" class="anchor"></span>Figure 31: Query And/Or Option

![](pecs-version-6-2-user-guide/032.png)

- AND indicates the results must match the new criteria and all the AND-connected criteria above it.
- OR indicates that the results must match either the new criteria or the AND-connected criteria above it. See And/Or Usage Example for additional information.
10. To include Historical Records in the query, select the Include Historical Records check box.
11. When all criteria have been added select the Query button. The results will display in the Results panel appropriate to the query being performed (VA or FDB).
12. To see details of the record follow the link in the Select column. The links are either Active (current VA record), Historical (old version of an active VA record), or Open (FDB record).

<span id="_Toc75767228" class="anchor"></span>Figure 32: Query Record Links for Details

![](pecs-version-6-2-user-guide/033.png)

### Query Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Advanced Query/Customization query function provides Filters that allow you to control what data is returned by the query. The filters are:

| Filter Name              | Filter Function                                                                                                                                                                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contains                 | The contents of the Value field appears somewhere in the database row of the Field being queried. Used primarily for fields containing text data. Contains is the default Filter option. Contains = "25" would match 25, 125, and 250, but not 205. |
| Equal To                 | The contents of the Value field exactly matches the contents of the database row of the Field being queried. "Equal To" = "25" would match 25, but not 125, 250, or 205.                                                                            |
| Less than or Equal to    | The contents of the Value field is less than or equal to the contents of the database row of the Field being queried.                                                                                                                               |
| Greater than or Equal to | The contents of the Value field is greater than or equal to the contents of the database row of the Field being queried.                                                                                                                            |
| Begins with              | The contents of the database row of the Field being queried starts with the contents of the Value field.                                                                                                                                            |
| Ends with                | The contents of the database row of the Field being queried ends with the contents of the Value field.                                                                                                                                              |
| Greater than             | The contents of the Value field is greater than the contents database row of the Field being queried.                                                                                                                                               |
| Less than                | The contents of the Value field is less than the contents database row of the Field being queried.                                                                                                                                                  |
| Not equal to             | The contents of the Value field does not exactly match the contents of the database row of the Field being queried.                                                                                                                                 |

<span id="_Toc75767171" class="anchor"></span>Table 4: And/Or Example 1

### And/Or Usage Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To see approved records with an interaction description equal to "anti" or "Lido", build the query as follows:

| Field                   | Filter | Value    | And/Or |
|-------------------------|--------|----------|--------|
| Interaction description | Equals | anti     | And    |
| Status                  | Equals | approved | Or     |
| Interaction description | Equals | Lido     | And    |
| Status                  | Equals | approved |        |

<span id="_Toc75767172" class="anchor"></span>Table 5: And/Or Example 2

If you build the query below, you will get approved records with an interaction description = "anti", but you will get all records with an interaction description of "Lido", regardless of status.

| Field                   | Filter | Value    | And/Or |
|-------------------------|--------|----------|--------|
| Interaction description | Equals | anti     | And    |
| Status                  | Equals | approved | Or     |
| Interaction description | Equals | Lido     |        |

<span id="_Toc75767173" class="anchor"></span>Table 6: My Request History Columns

### Query Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Use the YYYY-MM-DD date format for searching date fields within a query
- Date values can only use the following filters
  - Equal to
  - Less than or Equal to
  - Greater than or Equal to
  - Greater than
  - Less than

If a value that is not appropriate for the selected Field and Filter, then an error message is displayed in the Results panel.

<span id="_Toc75767229" class="anchor"></span>Figure 33: Bad Query Value Error Message

![](pecs-version-6-2-user-guide/034.png)

### Add Default DRC Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Queries on the Dose Range Concept (DRC) provide a special button that automatically adds predefined query criteria relevant to Dose Range records. These criteria can be used alone or in conjunction with other criteria you provide.

The predefined fields added when using the Add Default DRC Query button are:

- Concept type = 6
- AGEHIGHINDAYS \>= (greater than or equal to) 6570 (18 years old)

To add these criteria to your query, click the Add Default DRC Query button.

<span id="_Toc403984398" class="anchor"></span>Figure 34: Default Dose Range Query Window, with Default Dose Range Query

![](pecs-version-6-2-user-guide/035.png)

<span id="_Toc403984399" class="anchor"></span>Figure 35: Results from Building a Dose Range Query with Default DRC Query

![](pecs-version-6-2-user-guide/036.png)

## Save a Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS allows you to save a complete query so that you and other PECS users can run a specific query without having to re-build it every time.

> **NOTE:** The state of the Historical Records check box will not be saved with the query; if desired, it must be re-selected after the query is loaded at run-time.

To save a query:

1.  Create and run a query in the Build a Query panel. See Build a Query Panel for additional information.
13. Enter a name for the query in the Query Name field. The name must contain at least five characters and cannot be longer than 64 characters.
14. Click Save Query.

## Run a Saved Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS allows you to run a previously saved query with the same Concept and content (VA, FDB, or Both). There are two types of saved queries: My Queries (those that you have saved) or Other Users' Queries (queries saved by other PECS users).

To run a saved query:

1.  On the Advanced Query/Customization tab, select a Concept.
15. Select what data you want to view: VA, FDB, or Both.
16. In the Run a Saved Query sub-panel, select either My Queries or Other Users' Queries, then select the query you want to run.
17. Select the Load button. This will add the components of the saved query to the Build a Query panel.

<span id="_Toc75767232" class="anchor"></span>Figure 36: Running a Saved Query

![](pecs-version-6-2-user-guide/037.png)

18. Select the Query button to run the query. You may also select additional criteria to alter or enhance the saved query.

## Rename a Saved Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A saved query can be renamed by loading it then adding a different name in the Query Name field.

To rename a saved query:

1.  On the Advanced Query/Customization tab, select a Concept.
19. Select what data you want to view-- VA, FDB, or Both.
20. In the Run a Saved Query sub-panel, select My Queries, then select the query to be renamed; a saved query created by another user cannot be renamed.
21. Enter a new name into the Query Name field.
22. Select Save Query. The new query name will appear in the My Queries list in place of the original query.

## Delete a Saved Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can delete queries you have created and saved. Note that the delete operation is immediate; you will not be warned that the query is about to be deleted and there is no undo option.

> To delete a Saved Query:

1.  On the Advanced Query/Customization tab, select a Concept.
23. Select what data you want to view-- VA, FDB, or Both.
24. In the Run a Saved Query sub-panel, select My Queries, then select the query to be deleted; a query created by another user cannot be deleted.
25. Select the Delete button to delete the query.

## Query Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The results of the query will appear in either one or two panels: VA Table Results or FDB Table Results, depending on the type of records being queried. The results can be re-ordered, sorted by specific criteria, and exported.

<span id="_Toc75767233" class="anchor"></span>Figure 37: Example Query Results

![](pecs-version-6-2-user-guide/038.png)

### Sort Query Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the sort order of results of your query by clicking on the column headings in the display grid. Clicking once will display the records in ascending order (A to Z, 1-2-3 etc.) based on the contents of the column of the header selected; clicking a second time display the records in descending order (Z to A, 3-2-1, etc.). A small arrow indicates the direction of the current sort and the primary sort field.

<span id="_Toc403984400" class="anchor"></span>Figure 38: Sort Direction Indicator

![](pecs-version-6-2-user-guide/039.png)

For VA records, the default sort order is by 'Action Date', from newest to oldest. This puts the VA Customizations that have been updated most recently at the top of the returned list. By default, FDB records are displayed in the order they appeared in the update file sent by FDB. However, they can be re-sorted by clicking a column header.

> **NOTE:** Due to technical database restrictions, not all fields can be used to determine the sort order. For example, Concept ID Description on a Dose Range query cannot be used to sort the query results. Clicking these columns will have no result and the current sort order will be retained

### Re-Order Results Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can also move the columns in these tables and compare different fields side-by-side. Click the heading and drag and drop it:

<span id="_Toc403984401" class="anchor"></span>Figure 39: Dragging a Column to a New Position

![](pecs-version-6-2-user-guide/040.png)

<span id="_Toc403984402" class="anchor"></span>Figure 40: Re-positioned "Severity Level Code" Column

![](pecs-version-6-2-user-guide/041.png)

## Export Query Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can export query results for both VA and FDB records to an Excel spreadsheet.

To export the query results:

1.  On the appropriate query results panel, select the Export button.

<span id="_Toc75767237" class="anchor"></span>Figure 41: Exporting Query Button

![](pecs-version-6-2-user-guide/042.png)

26. Select one of the following options from the dialog box:
    - Open
    - Save
    - Cancel
27. Select Open to display the exported data in the spreadsheet; select Save to save a copy of the report to your system, or Cancel to abandon the export operation.

<span id="_Toc75767238" class="anchor"></span>Figure 42: Options Dialog Box for Exported Results

![](pecs-version-6-2-user-guide/043.png)

28. The spreadsheet contains two tabs:
1.  The \[Name of Concept\] tab (either VA or FDB) displays the results of the query.

<span id="_Toc75767239" class="anchor"></span>Figure 43: Exported Query Reporting Fields in the Excel Spreadsheet

![](pecs-version-6-2-user-guide/044.png)

2.  The Criteria tab displays the criteria used in the query.

<span id="_Toc75767240" class="anchor"></span>Figure 44: Query Criteria Tab in the Exported Excel Spreadsheet

![](pecs-version-6-2-user-guide/045.png)

For Drug-Drug Interaction, Drug Pair, Professional Monograph, and Duplicate Therapy records, there is a 1,000,000 line limit for exporting to the spreadsheet; for Dose Range records, the limit is 100,000. If the query returned more than the allowable number of records and the records were submitted for export anyway, the Criteria tab on the report will give the following message: "The number of rows returned in the search (XXXXXX) is greater than the maximum number of rows that can be exported (YYYYYY)."

<span id="_Toc403984403" class="anchor"></span>Figure 45: Export Query Line Limit Message

![](pecs-version-6-2-user-guide/046.png)

## Query Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After running a query an error message may appear in the Results panel. This is usually caused by one of the following:

<span id="_Toc75767242" class="anchor"></span>Figure 46: Generic Query Error

![](pecs-version-6-2-user-guide/047.png)

### Database Timeout (Too Many Results)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The database may timeout if the query produces too many results. If this error happens frequently, try re-writing the queries to be more specific, or add additional criteria that will limit the results when possible.

### Inappropriate Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering a value that is not appropriate for the selected Field and Filter will also produce an error message in the Results panel. For example Export Date \> "Z" produces an error because "Z" is not a date value.

# Working with Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As suggested by the name of the application (Pharmacy Enterprise *Customization* System), customizations are the primary focus of PECS. The process of creating a customization may involve many steps, but the process is relatively simple. In its simplest, "happy path" form, the workflow consists of three steps:

1.  Customization is Requested
29. Request is Reviewed
30. Request is Approved

## Create a Customization Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process for creating a customization request varies with the concept type you are customizing. Customization requests can be made by either Requestor or Approver users.

### Customize a Drug-Drug Interaction Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customizing a Drug-Drug Interaction record is more complicated than other record types in that Drug Pairs associated with the record must also be selected and customized.

To customize a Drug-Drug Interaction record:

1.  Find the Drug-Drug Interaction record to be customized in the FDB database using Advanced Query/Customization. See Using Advanced Query/Customization for additional information.
31. Select the Open link next to the record to be customized.
32. Select the Edit button.
33. Make changes to the record. At minimum, text must be added into the Current Action Reason field.
34. Select Customize. The system will confirm that the customization request has been entered and will be reviewed, that the Drug Pairs have not been approved, or that no Drug Pairs have been associated.
35. Select the Drug Pairs button.
36. Associate one or more drug pairs with the customized Drug-Drug Interaction. See Drug Pair Customization (Non 508-Compliant) Detail for additional information.
37. All the components are now in place for the Drug-Drug Interaction record for review and approval.

### Customize Other Record Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customizing Professional Monograph, Duplicate Therapy, and Dose Range records is relatively straight-forward; there are no associated records (as in Drug-Drug Interactions) that must be modified or selected.

To customize a Professional Monograph, Duplicate Therapy, or Dose Range record:

1.  Find the record to be customized in the FDB database using Advanced Query/Customization. See Using Advanced Query/Customization for additional information.
1.  Select the Open link next to the record to be customized.
2.  Select the Edit button.
3.  Make changes to the record. At minimum, text must be added into the Current Action Reason field.
4.  Select Customize. The system will confirm that the customization request has been entered and will be reviewed.

### Create Customization from a Blank Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new record use the Open Blank Form button. This method can be used to create new Drug-Drug Interaction, Professional Monograph, and Dose Range records. It cannot be used to create a Duplicate Therapy record.

<span id="_Toc75767243" class="anchor"></span>Figure 47: Open Blank Form Button

![](pecs-version-6-2-user-guide/048.png)

To Create a New Record:

1.  Perform an Advanced Query/Customization Query for the record type (Concept) on both VA and FDB Records you want to create.
38. Select the Open Blank Form button at the bottom of the page.
39. Complete the form with as much information as possible. Fields marked as Required must be completed before the record can be saved. Some record types (concepts) have other requirements that must be met before the record can be created. See New Record Requirements by Concept Type for additional information.

New Record Requirements by Concept Type

Some records have specific requirements for new records that are not indicated by the Required label.

Drug-Drug Interaction

For a completely new record, the interacting drugs must be separated by a forward slash (/) character.

Professional Monograph

Custom Professional Monographs can be associated with Drug-Drug Interactions once they are Approved.

Dose Range

The Concept Type can only be 6 and the Concept ID Number must correspond to an existing FDB record for Concept Type 6.

Duplicate Therapy

New Duplicate Therapy records *cannot* be created using this method. A new Duplicate Therapy customization must be made on the Advanced Query/Customization page.

Drug Pairs

New Drug Pair records *cannot* be created using this method. A new Drug Pair can be added by selecting routed generic drugs associated with a drug-drug interaction.

## Modify Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customization requests can be modified at any time. If a required field is changed (other than Current Action Reason), the customization Action Status will change to Modified; non-required fields do not affect Action Status. Requestors can modify customizations they have requested, but cannot modify customizations requested by other users. Approvers can modify any record at any time. Release Managers and Administrator cannot modify customization requests.

> **NOTE:** Although the Edit button will appear on customization requests for Release Managers and Administrators (and for Requestors viewing requests other than their own), there is no way to save any changes made.

The links on the Home page can be used to locate records for processing. See the [User Roles and Tasks](#_User_Roles_and) and/or [Home Page](#_Home_Page_1) sections for additional information.

To modify a customization request:

> **NOTE:** See Section 7.7. [Record Locking Feature](#_Record_Locking_Feature) for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  Select the Advanced Query/Customization tab.
40. Select a Concept to build a Query search using a VA record or FDB record (or both).
41. Select/enter a Field, Filter, and Value.
42. Run a Query search. The results table will be displayed.
43. Select the Active link associated with the record to be modified.
44. Select the Edit button.
45. Make changes to the record. At minimum, text must be added into the Current Action Reason field.
46. Select Modify to save the changes. Select Cancel Edit to abandon the changes and return to the detail page.

## Review Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review is the second step to getting a customization Approved. A Review must be performed by an Approver. Approvers cannot Review customization requests they have created and cannot Approve customization requests they have Reviewed.

The links on the Home page can be used to locate records for processing. See the [User Roles and Tasks](#_User_Roles_and) and/or [Home Page](#_Home_Page_1) sections for additional information.

To Review a customization request:

> **NOTE:** See Section 7.7. [Record Locking Feature](#_Record_Locking_Feature) for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  Select the Advanced Query/Customization tab.
47. Select a Concept to build a Query search using a VA record or FDB record (or both).
48. Select/enter a Field, Filter, and Value.
49. Run a Query search. The results table will be displayed.
50. Select the Active link associated with the record to be reviewed.
51. Select the Edit button.
52. Review the customization request to be approved.
53. Select Submit as Reviewed to save the changes. Select Cancel Edit to abandon the review and return to the detail page.

## Approve Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Approved customization request is considered valid and should be used in making decisions in veteran pharmaceutical care. Approved customization requests are included in the Custom Updates that are distributed to other pharmacy applications, and are used in Order Checks for veteran prescriptions.

Customization requests are Approved by Approvers. Approvers cannot Approve customization requests they Reviewed; they can Approve customization requests they created once they have been Reviewed by another Approver.

The links on the Home page can be used to locate records for processing. See the [User Roles and Tasks](#_User_Roles_and) and/or [Home Page](#_Home_Page_1) sections for additional information.

To Approve a customization request:

> **NOTE:** See Section 7.7. [Record Locking Feature](#_Record_Locking_Feature) for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  Select the Advanced Query/Customization tab.
54. Select a Concept to build a Query search using a VA record or FDB record (or both).
55. Select/enter a Field, Filter, and Value.
56. Run a Query search. The results table will be displayed.
57. Select the Active link associated with the record to be approved.
58. Select the Edit button.
59. Review the customization request to be approved.
60. Select Approve to save the changes. Select Cancel Edit to abandon the changes and return to the detail page.

## Reject Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customization requests can be Rejected at all points of the Create/Review/Approve process. Customization requests are Rejected because they are thought to be invalid as written by either the Reviewer or Approver. Customization requests can also be Rejected by the user who initiated the customization request if they determine that request is no longer needed. Rejected customization requests can be modified and re-submitted for Review and Approval.

The links on the Home page can be used to locate records for processing. See the [User Roles and Tasks](#_User_Roles_and) and/or [Home Page](#_Home_Page_1) sections for additional information.

To Reject a customization request:

> **NOTE:** See Section 7.7.[Record Locking Feature](#_Record_Locking_Feature) for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  Select the Advanced Query/Customization tab.
61. Select a Concept to build a Query search using a VA record or FDB record (or both).
62. Select/enter a Field, Filter, and Value.
63. Run a Query search. The results table will be displayed.
64. Select the Active link associated with the record to be rejected.
65. Select the Edit button.
66. Review the customization request to be certain it is invalid and cannot continue in the Review/Approval process without modification.
67. Select Reject to save the changes. Select Cancel Edit to abandon the Reject process and return to the detail page.

## Delete Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an Approved customization is no longer valid, and should not be used in Order Check decisions, it must be deleted. Deleting a customization request will not remove it from the PECS system, but will remove it from MOCHA during the next Custom Update. Deleted records can be edited and re-submitted for Review and Approval.

Deleting an Approved customization request is a two-step process. One user with Approver privileges must request that the record be deleted, and then a second user with Approver privileges must delete the record. At any time during this process, prior to actual deletion, the deletion request can be Rejected.

The links on the Home page can be used to locate records for processing. See the [User Roles and Tasks](#_User_Roles_and) and/or [Home Page](#_Home_Page_1) sections for additional information.

To Delete a Customization Request:

> **NOTE:** See Section 7.7.[Record Locking Feature](#_Record_Locking_Feature) for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  Select the Advanced Query/Customization tab.
68. Select a Concept to build a Query search using a VA record or FDB record (or both).
69. Select/enter a Field, Filter, and Value.
70. Run a Query search. The results table will be displayed.
71. Select the Active link associated with the record to be deleted.
72. Select the Edit button.
73. Review the content. Once satisfied that the customization request should be deleted write a brief explanation in the Current Action Reason field.
74. Select the Submit for Delete button.
75. A confirmation pop-up will appear. To continue the deletion process, select OK. This will change the Action Status to Delete Reviewed. Select Cancel to return to Edit mode.

Now another Approver can confirm the Delete Reviewed customization request for deletion, and complete the process.

To confirm a Delete Reviewed customization request for deletion:

1.  Find the record to be deleted using Advanced Query/Customization or from the PECS Home page (in My Requests for Deletion).
76. Select the active link associated with the record to be deleted.
77. Select Edit.
78. Enter a comment for agreeing with the Request for Deletion.
79. Select Delete.
80. A confirmation pop-up will appear. To continue the deletion process, select OK. This will change the Action Status to Deleted. Select Cancel to return to Edit mode.

## Record Locking Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Record in Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Records from all five concept types (Drug-Drug Interaction, Drug Pairs, Professional Monograph, Dose Range, and Duplicate Therapy) can be edited only by a single user at a time. If more than one user attempts to edit the same record at the same time, then the user who entered the record first will have precedence and the subsequent users will receive a message that the record is in-use and cannot be edited at the current time.

<span id="_Toc945502" class="anchor"></span>Figure 48: Record in Use

![](pecs-version-6-2-user-guide/049.png)

### Record Recently Modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an opened record has been modified by another user while in use, then PECS will send an alert message warning that the record has been modified and is no longer current. Select OK to load the modified record.

<span id="_Toc945503" class="anchor"></span>Figure 49: Record Recently Modified

![](pecs-version-6-2-user-guide/050.png)

### Record Time-Out Lock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To prevent the record from being locked for an extended amount of time the lock will be automatically removed if no edits are made in two consecutive minutes. Select OK to continue editing the record.

<span id="_Toc945504" class="anchor"></span>Figure 50: Editing Time-Out Warning

![](pecs-version-6-2-user-guide/051.png)

### Record Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user navigates away from an un-saved record, then a warning dialog box will appear. Select Cancel to continue editing the page or Select OK to return to the read-only display.

<span id="_Toc945505" class="anchor"></span>Figure 51: Navigation Causing Loss of Changes Warning

![](pecs-version-6-2-user-guide/052.png)

# User Roles and Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS users have one of four roles within the application, each with specific tasks they perform.

- Requestor
- Approver
- Release Manager
- Administrator

## Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary task of a PECS Requestor is to create customization requests. The Requestor has limited privileges. They can only view and modify the customization requests that they created. The Requestor Home Page reflects this limited privilege.

A Requestor performs the following tasks related to customization requests:

- Create a Customization Request
- Modify Customization Requests

### Requestor Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page for the Requestor role only displays links to the customization requests made by the current user.

<span id="_Toc403984406" class="anchor"></span>Figure 52: Requestor's Home Page

![](pecs-version-6-2-user-guide/053.png)

The following information is displayed on the Requestor Home tab:

- My Request History

### My Request History: Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Request History displays customization requests created by the current user. The results are displayed by Action Status of the requests.

<span id="_Toc403984407" class="anchor"></span>Figure 53: My Request History

![](pecs-version-6-2-user-guide/054.png)

The following table defines the columns found on the My Request History window.

| Column Name | Column Definition                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------|
| New         | The number of active records in the "New" status created by the current user.                            |
| Modified    | The number of active records in the "Modified" status created by the current user.                       |
| Reviewed    | The number of active records in the "Reviewed" and "Delete Reviewed" status created by the current user. |
| Approved    | The number of active records in the "Approved" status created by the current user.                       |
| Rejected    | The number of active records in the "Rejected" status created by the current user.                       |
| Deleted     | The number of active records in the "Deleted" status created by the current user.                        |
| All         | The number of all active records in any status, created by the current user.                             |

<span id="_Toc75767174" class="anchor"></span>Table 7: My Request History Columns

Following the links within the summary table opens pre-defined queries to provide details of the requests. For example, clicking the New - Professional Monograph link will display a query with the appropriate criteria and the query results: Concept = Professional Monograph, Request Submitted By = \<current user\>, Action Status = New.

<span id="_Toc403984408" class="anchor"></span>Figure 54: Home Tab Summary - Pre-Defined Query

![](pecs-version-6-2-user-guide/055.png)

<span id="_Toc403984409" class="anchor"></span>Figure 55: Query Results

![](pecs-version-6-2-user-guide/056.png)

### Additional Tools Available to Requestors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the Home tab, Requestors see the following tabs on their Home page:

- Advanced Query/Customization – See Using Advanced Query/Customization for additional information.
- Easy Search – see Easy Search for additional information.
- Drug Pair Lookup – see Drug Pair Lookup for additional information.
- Contact Us – see Contact Us for additional information.
- Help – see Online Help for additional information.

## Approver

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Approver creates and processes customization requests. In addition to being able to request a customization themselves, they can also Review, Modify, Reject, Approve, and Delete customization requests made by other PECS users.

An Approver performs the following tasks related to customization requests:

- Create a Customization Request
- Modify Customization Requests

Customization requests can be modified at any time. If a required field is changed (other than Current Action Reason), the customization Action Status will change to Modified; non-required fields do not affect Action Status. Requestors can modify customizations they have requested, but cannot modify customizations requested by other users. Approvers can modify any record at any time. Release Managers and Administrator cannot modify customization requests.

> **NOTE:** Although the Edit button will appear on customization requests for Release Managers and Administrators (and for Requestors viewing requests other than their own), there is no way to save any changes made.

The links on the Home page can be used to locate records for processing. See the User Roles and Tasks and/or Home Page sections for additional information.

To modify a customization request:

> **NOTE:** See Section 7.7. Record Locking Feature for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  
2.  
3.  
4.  
5.  Select the Advanced Query/Customization tab.Select a Concept to build a Query search using a VA record or FDB record (or both).Select/enter a Field, Filter, and Value.Run a Query search. The results table will be displayed.Select the Active link associated with the record to be modified.
6.  Select the Edit button.
7.  Make changes to the record. At minimum, text must be added into the Current Action Reason field.
8.  Select Modify to save the changes. Select Cancel Edit to abandon the changes and return to the detail page.
- Review Customization Requests

Review is the second step to getting a customization Approved. A Review must be performed by an Approver. Approvers cannot Review customization requests they have created and cannot Approve customization requests they have Reviewed.

The links on the Home page can be used to locate records for processing. See the User Roles and Tasks and/or Home Page sections for additional information.

To Review a customization request:

> **NOTE:** See Section 7.7. Record Locking Feature for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  
5.  
6.  
7.  
9.  Select the Advanced Query/Customization tab.Select a Concept to build a Query search using a VA record or FDB record (or both).Select/enter a Field, Filter, and Value.Run a Query search. The results table will be displayed.Select the Active link associated with the record to be reviewed.
10. Select the Edit button.
11. Review the customization request to be approved.
12. Select Submit as Reviewed to save the changes. Select Cancel Edit to abandon the review and return to the detail page.
- Approve Customization Requests

An Approved customization request is considered valid and should be used in making decisions in veteran pharmaceutical care. Approved customization requests are included in the Custom Updates that are distributed to other pharmacy applications, and are used in Order Checks for veteran prescriptions.

Customization requests are Approved by Approvers. Approvers cannot Approve customization requests they Reviewed; they can Approve customization requests they created once they have been Reviewed by another Approver.

The links on the Home page can be used to locate records for processing. See the User Roles and Tasks and/or Home Page sections for additional information.

To Approve a customization request:

> **NOTE:** See Section 7.7. Record Locking Feature for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  
8.  
9.  
10. 
13. Select the Advanced Query/Customization tab.Select a Concept to build a Query search using a VA record or FDB record (or both).Select/enter a Field, Filter, and Value.Run a Query search. The results table will be displayed.Select the Active link associated with the record to be approved.
14. Select the Edit button.
15. Review the customization request to be approved.
16. Select Approve to save the changes. Select Cancel Edit to abandon the changes and return to the detail page.
- Reject Customization Requests

Customization requests can be Rejected at all points of the Create/Review/Approve process. Customization requests are Rejected because they are thought to be invalid as written by either the Reviewer or Approver. Customization requests can also be Rejected by the user who initiated the customization request if they determine that request is no longer needed. Rejected customization requests can be modified and re-submitted for Review and Approval.

The links on the Home page can be used to locate records for processing. See the User Roles and Tasks and/or Home Page sections for additional information.

To Reject a customization request:

> **NOTE:** See Section 7.7.Record Locking Feature for images and descriptions of the pop-up windows that may be encountered throughout the process of working with Customization Requests.

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
- Select the Advanced Query/Customization tab.Select a Concept to build a Query search using a VA record or FDB record (or both).Select/enter a Field, Filter, and Value.Run a Query search. The results table will be displayed.Select the Active link associated with the record to be rejected.Select the Edit button.Review the customization request to be certain it is invalid and cannot continue in the Review/Approval process without modification.Select Reject to save the changes. Select Cancel Edit to abandon the Reject process and return to the detail page. Delete Customization Requests

### Approver Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page for the Approver role displays links to customization requests in many different states:

- Customization requests made by the current user (My Request History: Approver)
- Customization requests made by other users that are assigned to the current user for review (My Assigned Requests for Review)
- Customization requests made by other users that are assigned to the current user for approval (My Assigned Requests for Approval)
- Customization requests made by other users that are assigned to the current user for deletion (
- My Assigned Requests for Deletion)
- Customization requests made by other users that are not currently assigned to an Approver (Unassigned Requests)
- Customization requests made by any user in any state (All Requests)

<span id="_Toc403984410" class="anchor"></span>Figure 56: Approver's Home Page

![](pecs-version-6-2-user-guide/057.png)

### My Request History: Approver

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Request History displays active customization records created by the current user (Requestor and Approver roles only). The results will be broken down into numbers of active records, created by the current user by the following Action Statuses: New, Modified, Reviewed, Approved, Rejected, Deleted and All.

<span id="_Toc403984411" class="anchor"></span>Figure 57: My Request History

![](pecs-version-6-2-user-guide/058.png)

The following table defines the columns found on the My Request History window.

| Column Name | Column Definition                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------|
| New         | The number of active records in the "New" status created by the current user.                            |
| Modified    | The number of active records in the "Modified" status created by the current user.                       |
| Reviewed    | The number of active records in the "Reviewed" and "Delete Reviewed" status created by the current user. |
| Approved    | The number of active records in the "Approved" status created by the current user.                       |
| Rejected    | The number of active records in the "Rejected" status created by the current user.                       |
| Deleted     | The number of active records in the "Deleted" status created by the current user.                        |
| All         | The number of all active records in any status, created by the current user.                             |

<span id="_Toc75767175" class="anchor"></span>Table 8: All Request Columns

Following the links within the summary table opens pre-defined queries to provide details of the requests. For example, clicking the New - Professional Monograph link will display a query with the appropriate criteria and the query results: Concept = Professional Monograph, Request Submitted By = \<current user\>, Action Status = New.

<span id="_Toc403984412" class="anchor"></span>Figure 58: Home Tab Summary - Pre-Defined Query

![](pecs-version-6-2-user-guide/059.png)

<span id="_Toc403984413" class="anchor"></span>Figure 59: Query Results

![](pecs-version-6-2-user-guide/060.png)

### My Assigned Requests for Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Assigned Requests for Review are active customization records assigned to the current user to be reviewed. The Awaiting Review count is the number of records that are in the "New" or "Modified" status, that have been assigned to the current user for review. To see the records, select the corresponding link.

<span id="_Toc403984414" class="anchor"></span>Figure 60: My Assigned Request for Review Example

![](pecs-version-6-2-user-guide/061.png)

### My Assigned Requests for Approval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Assigned Requests for Approval are active customization records assigned to the current user to be approved. These records have been reviewed by another Approver. To see the records, select the corresponding link.

<span id="_Toc403984415" class="anchor"></span>Figure 61: Approver's List of Requests for Approval

![](pecs-version-6-2-user-guide/062.png)

### My Assigned Requests for Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

My Assigned Requests for Deletion are active customization records assigned to the logged in user to be deleted. The records have been "delete reviewed" by another "Approver" in the system. To see the records, select the corresponding link.

<span id="_Toc403984416" class="anchor"></span>Figure 62: Approver's List of Requests for Deletion

![](pecs-version-6-2-user-guide/063.png)

### Unassigned Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unassigned Requests are either New, Modified, or Reviewed customization requests that have not been assigned to any user. To see the records, select the corresponding link.

<span id="_Toc75767259" class="anchor"></span>Figure 63: Approver's List of Unassigned Requests

![](pecs-version-6-2-user-guide/064.png)

### All Requests 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Requests displays all customization requests currently in the system by Action Status. The result detail will display the active records associated with the selected custom table summary.

The categories are:

| Column Name | Column Definition                                                            |
|-------------|------------------------------------------------------------------------------|
| New         | The number of active records in the "New" status.                            |
| Modified    | The number of active records in the "Modified" status.                       |
| Reviewed    | The number of active records in the "Reviewed" and "Delete Reviewed" status. |
| Approved    | The number of active records in the "Approved" status.                       |
| Rejected    | The number of active records in the "Rejected" status.                       |
| Deleted     | The number of active records in the "Deleted" status.                        |
| All         | The number of all active records in any status.                              |

<span id="_Toc75767176" class="anchor"></span>Table 9: Customize Table Settings Columns

### Additional Tools Available to Approvers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the Home tab, Approvers see the following tabs on their Home page:

- Advanced Query/Customization – See Using Advanced Query/Customization for additional information.
- Easy Search – see Easy Search for additional information.
- Drug Pair Lookup – see Drug Pair Lookup for additional information.
- Reports – see Reports for additional information.
- Contact Us – see Contact Us for additional information.
- Help – see Online Help for additional information.

## Release Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary task of a PECS Release Manager is to create Custom Updates. Since they are not directly involved in the creation or processing of customization requests, the customization-related panels that appeared on the Requestor and Approver Home Pages do not appear on the Release Manager Home page.

Custom Updates are created at the instruction of the PECS Administrator and/or the National Drug File (NDF) Support Group. Once the Custom Update has been created, the Release Manager should send an Outlook email to the PECS Administrators.

### Release Manager Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page for the Release Manager does not display links associated with customization requests.

<span id="_Toc403984417" class="anchor"></span>Figure 64: Release Manager's Home Page

![](pecs-version-6-2-user-guide/065.png)

### Custom Update Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Custom Update tab contains the Release Manager-specific functions and is available only to PECS Release Managers.

<span id="_Toc75767261" class="anchor"></span>Figure 65: The Custom Update Tab

![](pecs-version-6-2-user-guide/066.png)

### Custom Update Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Custom Update is a set of files that:

- Transmit Approved customization requests to MOCHA (via DATUP) so that the customizations can be used in Order Check decisions.
- Transmit contain Deleted customization requests so that previously approved customizations can be removed from the MOCHA Order Check decision process
- Transmit updates received from FDB

### Update Files Explained

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Custom Update produces two files. The Full Custom Update includes the entire FDB data distribution. The Incremental Update file contains updates from FDB to their database, as well as Approved and Deleted customizations from PECS. These updates will be incorporated in the national and regional databases for use in order check decisions (MOCHA).

Custom Update files use the following file naming standard:

CstmUpdFile\_{FDB Version}.{PECS Generated Version Number}\_{Date/Time Stamp}.zip

For example, the CstmUpdFile_3.2.751_20120503154622.zip has an FDB Version number of "3.2," a PECS-generated Version Number of "751," and was created on May 3, 2012 at 15:46:22 (military time). The contents of the zip file will determine if this is an Incremental or a Full update.

Incremental Update File

The Incremental Update File contains just the updates delivered by FDB and Approved and Deleted customizations from PECS. The custom zip file contains a proddefinition.xml, FDBPRODCONTROL.DAT and several data files that have an extension of UPD.

<span id="_Toc403984423" class="anchor"></span>Figure 66: Custom Update Zip File

![](pecs-version-6-2-user-guide/067.png)

The proddefinition.xml file is a file from FDB that defines the table structures for the FDB tables in an XML format. The FDBUPDCONTROL.DAT file contains control information used by the FDB Data Updater software when determining if this Incremental update should be applied to a database. The UPD files contain data updates for a particular FDB table in the database.

Here is a sample: Note that the "D", "C", and "A" in the left column mean Delete, Change, and Add, respectively.

<span id="_Toc75767263" class="anchor"></span>Figure 67: Custom Update Text File

![](pecs-version-6-2-user-guide/068.png)

Full Update File

The Full Update File contains the complete FDB distribution. The files are:

- CTVERSION.TXT
- FDBCUSTOMDDIM.TXT
- FDBCUSTOMDDIMINTERACTION.TXT
- FDBCUSTOMDDIMSTRINGS.TXT
- FDBCUSTOMDOSERANGE.TXT
- FDBCUSTOMDUPLICATETHERAPY.TXT
- FDBCUSTOMMONOGRAPH.TXT
- FILECOUNTS.DAT
- PRODDEFINITION.XML

Here is a sample of the full update of Drug-Drug Interactions:

<span id="_Toc403984426" class="anchor"></span>Figure 68: Custom Drug-Drug Interaction Full Update File

![](pecs-version-6-2-user-guide/069.png)

### Create a Custom Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Custom Updates can be only be created by Release Managers

To create a Custom Update:

1.  Select the Custom Updates tab:
81. Select Create New Update:
82. After processing, the two new update files will appear in the list.

<span id="_Toc75767265" class="anchor"></span>Figure 69: Newly Created Update Files

![](pecs-version-6-2-user-guide/070.png)

83. Verify today's date in Created Date column. The dates in the Created Date column should match the current date.
84. If an error message is received, report it to PECS Administrator. See Contact Us for additional information.

### Review Custom Update History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing Custom Updates are organized by Year and Month. Select the Year to display the months containing custom updates for that year, then click a month to display the custom updates performed during that month. The custom updates for more than one month can be displayed simultaneously. Selecting a month for a second time will collapse (hide) the custom updates for that month.

<span id="_Toc75767266" class="anchor"></span>Figure 70: Existing Custom Updates by Year and Month

![](pecs-version-6-2-user-guide/071.png)

### Additional Tools Available to Release Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the Home tab and Custom Updates, Release Managers role see the following tabs on their Home page:

- Advanced Query/Customization – See Using Advanced Query/Customization for additional information.
- Contact Us – See Contact Us for additional information.
- Help – See Online Help for additional information.

## Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Administrator performs limited maintenance on the PECS system through the Administration tab. The administrator can modify the page display for the PECS records (both FDB and VA). Demote existing Approvers, remove Null Drug Pairs, and change what is displayed on the Contact Us page. The Administration tab is displayed only to Administrator users.

Since they are not directly involved in the creation or processing of customization requests, the customization-related panels that appeared on the Requestor and Approver Home Pages do not appear on the Administrator Home page.

The unique tasks performed by an Administrator are:

- Customize Settings
- Change Field Display Order
- Null Drug Pair Removal Process
- Editing Contact Us

Most Administrator functions are performed on the Administration tab. Editing the Contact Us page occurs on the Contact Us page itself.

### Administrator Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page for the Administrator does not display links associated with customization requests.

<span id="_Toc403984418" class="anchor"></span>Figure 71: Administrator's Home Page

![](pecs-version-6-2-user-guide/072.png)

### Administration Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administration tab contains most of the Administrator-specific functions and is available only to PECS Administrators.

<span id="_Toc75767268" class="anchor"></span>Figure 72: The Administration Tab

![](pecs-version-6-2-user-guide/073.png)

### Customize Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Customize Settings panel allows Administrators to change the label name for the Field (Display Name), and whether the field should appear in Queries, Detail Pages, and Reports. It also allows the administrator to change the order of the individual fields that are displayed on their respective pages.

To access Customize Settings:

1.  Log in as an Administrator.
85. Select the Administration tab.
86. Select the appropriate concept to change the way data appears in relation to that concept.

<span id="_Toc75767269" class="anchor"></span>Figure 73: The Customize Setting Panel

![](pecs-version-6-2-user-guide/074.png)

Customize Settings Table Description

There are currently five Customize Settings pages, one for each concept: Drug Pair, Drug-Drug Interaction, Dose Range, Duplicate Therapy and Professional Monograph.

| Column             | Description                                                                                                                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name               | Name is the database field name for items displayed for the selected concept. Name cannot be changed; it identifies the field in the database table.                                                              |
| Display Name       | Display Name is what appears within PECS for the field defined by the entry in the Name column. The contents of Display Name will appear in query selection, data entry field and reports for the selected table. |
| Display in Query   | Display in Query allows you to set if the field will be displayed in the Advance Query/Customization results tables. Some fields are required and cannot be turned off.                                           |
| Display in Details | Display in Details allows you to set if the field will be displayed on the Detail page of the selected concept.                                                                                                   |
| Include in Reports | Include in Reports allows you to set if the field will be displayed in any applicable reports.                                                                                                                    |
| Display Order      | A numeric value designating the order the field will be displayed in.                                                                                                                                             |

<span id="_Toc75767177" class="anchor"></span>Table 10: Interactions for a Single Drug Report Fields

> **WARNING:** Changes made on the Settings page will affect all PECS users. Please proceed cautiously.

<span id="_Toc403984427" class="anchor"></span>Figure 74: Customize Settings Example (Drug Pairs)

![](pecs-version-6-2-user-guide/075.png)

Change Field Display Name

To change how the name of a field is displayed on the page, modify the contents of the Display Name field.

1.  In the Customize \<Concept\> List, find the name of the database field to be changed.
87. Modify the contents of the field in the Display Name column.
88. Repeat the process as necessary.
89. Select Save to save the changes, select Cancel to abandon the changes and return to the Settings page.

> **NOTE:** Cancel is immediate. There is no warning that the changes will be lost.

Add/Remove Field from Query Options

To add (or remove) a field from Query options

1.  In the Customize \<Concept\> List, find the name of the database field to be changed.
90. In the Display in Query column, select True to display the field in Query options, select False to prevent the field from displaying in Query options.

> **NOTE:** Display in Query" options are not available for all fields; some fields are explicitly required to be displayed in the Query options while others are forbidden from being displayed. In these cases, the required display option (True or False) will be the only options displayed and cannot be changed.

<span id="_Toc75767271" class="anchor"></span>Figure 75: Example of Display in Query Column of Radio Button Choices

![](pecs-version-6-2-user-guide/076.png)

91. Repeat the process as necessary.
92. Select Save to save the changes, select Cancel to abandon the changes and return to the Settings page.

> **NOTE:** Cancel is immediate. There is no warning that the changes will be lost.

Add/Remove Field from Detail Pages

To add (or remove) a field from Detail pages

1.  In the Customize \<Concept\> List, find the name of the database field you want to change.
93. In the Display in Detail column, select True to display the field on the concept Detail page, select False to prevent the field from displaying on the concept Detail page.

<span id="_Toc75767272" class="anchor"></span>Figure 76: Example of Display in Details Column of Radio Button Choices

![](pecs-version-6-2-user-guide/077.png)

94. Repeat the process as necessary.
95. Select Save to save the changes, select Cancel to abandon the changes and return to the Settings page.

> **NOTE:** Cancel is immediate. There is no warning that the changes will be lost.

Add/Remove Field from Reports

To add (or remove) a field from Reports

1.  In the Customize \<Concept\> List, find the name of the database field you want to change.
96. In the Include in Reports column, select True to display the field on concept-related reports, select False to prevent the field from displaying on the concept-related reports.

<span id="_Toc75767273" class="anchor"></span>Figure 77: Example of Include In Reports Column of Radio Button Choices

![](pecs-version-6-2-user-guide/078.png)

97. Repeat the process as necessary.
98. Select Save to save the changes, select Cancel to abandon the changes and return to the Settings page.

> **NOTE:** Cancel is immediate. There is no warning that the changes will be lost.

### Change Field Display Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change the order that the fields appear in Detail pages and drop-down lists, change the adjacent number in the Display Order field. Note that changing the Display Order is an entirely manual process; each field must be changed individually and the order is not validated in any way. Multiple fields can have the same display order.

When all changes are complete, Select Save, select Cancel to abandon the changes and return to the Settings page.

<span id="_Toc75767274" class="anchor"></span>Figure 78: Display Order List

![](pecs-version-6-2-user-guide/079.png)

### Update User Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS Administrators can add PECS users and modify the roles of existing users. By default, PECS users are assigned Requestor privileges. Once added, the user privileges can be elevated to Approver, Release Manager, and Administrator by an Administrator through the User Roles page. Privileges can also be removed from a user at any time. 

> **NOTE:** Release Manager or Approvers should immediately be assigned the appropriate roles to avoid giving them access to inappropriate privileges (creating customizations).

<span id="_Toc75767275" class="anchor"></span>Figure 79: Update User Roles Panel

![](pecs-version-6-2-user-guide/080.png)

#### Update User Roles

Administrators can assign roles to PECS users. In order to successfully log in, the user must have a valid PIV card. See Identity Management for additional information.

To assign roles to PECS users

1.  From the Administration tab, select Update User Roles.
99. Manage the user roles by selecting the appropriate role for the User Name.
100. Select Save.
101. Select OK to save the user, select Cancel to abandon the operation.

<span id="_Toc75767276" class="anchor"></span>Figure 80: User Roles Save Message

![](pecs-version-6-2-user-guide/081.png)

#### Remove User Roles

To remove a role from a user

1.  From the Administration tab, select Update User Roles.

<span id="_Toc75767277" class="anchor"></span>Figure 81: Update User Roles Option

![](pecs-version-6-2-user-guide/082.png)

102. Clear one or more roles for one or more users from the User Name list.

<span id="_Toc75767278" class="anchor"></span>Figure 82: List of User Roles

![](pecs-version-6-2-user-guide/083.png)

103. Select Save.
104. Select OK to accept changes to the user roles, select Cancel to abandon the operation.

<span id="_Toc75767279" class="anchor"></span>Figure 83: User Roles Save Message

![](pecs-version-6-2-user-guide/084.png)

### Null Drug Pair Removal Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Null Drug Pair Removal changes the status of any VA Drug Pair that contains a null Routed Generic to "Deleted", and removes the null drug pairs from their associated VA Drug-Drug Interactions. VA Drug Pairs have null Routed Generics because one or both of the Routed Generics that make up the Drug Pair has been deleted by FDB. PECS applies the FDB Routed Generic deletions as part of the weekly FDB-DIF update, so it is recommended that the Null Drug Pair Removal process be run weekly, after the FDB-DIF update completes.

The Administrator may initiate this process at any time by clicking the "Null Drug Pair Removal" button on the following window:

<span id="_Toc403984428" class="anchor"></span>Figure 84: Null Drug Pair Removal Button on Administration Tab

![](pecs-version-6-2-user-guide/085.png)

When the process is complete, a message will appear at the top of the page to indicate that the process has completed.

<span id="_Toc403984429" class="anchor"></span>Figure 85: Null Drug Pair Removal Process Complete

![](pecs-version-6-2-user-guide/086.png)

> **NOTE:** The [<u>Null Drug Pairs Customization Report</u>](#null-drug-pairs-customization-report) can be used to identify *approved* VA Drug-Drug Interactions that contain null Drug Pairs. However, the Null Drug Pair Removal Process removes null drug pairs from *any* VA Drug-Drug Interaction, regardless of status. All VA Custom drug pairs that contain a null routed generic drug are updated as follows: the action status of the drug pair is changed to "Deleted" and the current action reason is "FDB Deleted," with the value of the FDB issue date when the custom drug pair was deleted. The FDB issue date is the date associated with the FDB update file that includes the deletion.

### Editing Contact Us

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to viewing, Administrator users can edit the content of the Contact Us page. To edit the Contact Us page:

1.  Select the Contact Us tab.
105. Select the Edit Content link on the right side of the page. This will display a word processor-like editor.

<span id="_Toc75767282" class="anchor"></span>Figure 86: Edit Content Option in the Contact Us Tab

![](pecs-version-6-2-user-guide/087.png)

106. Add or change the content on the page. To add or edit a link, see the appropriate sections below.

<span id="_Toc75767283" class="anchor"></span>Figure 87: Contact Us Edit Page

![](pecs-version-6-2-user-guide/088.png)

107. When the edits are complete, select the Save button.

<span id="_Toc75767284" class="anchor"></span>Figure 88: Save Button on the Contact Us Edit Page

![](pecs-version-6-2-user-guide/089.png)

### Add a Contact Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a link while editing the Contact Us page:

1.  Select the Create Link button. This will display the Link Properties dialog box.

<span id="_Toc75767285" class="anchor"></span>Figure 89: Create Link Button on the Contact Us page

![](pecs-version-6-2-user-guide/090.png)

108. Enter the mailto URL for the person whose contact information being added into the URL field. A mailto URL is the word "mailto" followed by a colon followed by the appropriate email address. VA email addresses are usually (but not always) firstname.lastname@va.gov. Verify the contact information in the Outlook Global Address List (GAL) for the correct email address. Example: [<u>mailto:firstname.lastname@va.gov</u>](mailto:firstname.lastname@va.gov).

<span id="_Toc75767286" class="anchor"></span>Figure 90: URL Field for an Email Address

![](pecs-version-6-2-user-guide/091.png)

109. Enter the contact name in the Description field. This is the text the user will actually see on the Contact Us page.

<span id="_Toc75767287" class="anchor"></span>Figure 91: Description Field for an Email Address

![](pecs-version-6-2-user-guide/092.png)

110. On the Target list, select New Window.

<span id="_Toc75767288" class="anchor"></span>Figure 92: Target List

![](pecs-version-6-2-user-guide/093.png)

111. Select the Set button.

<span id="_Toc75767289" class="anchor"></span>Figure 93: Completed Link Properties

![](pecs-version-6-2-user-guide/094.png)

### Edit a Contact Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To modify an existing contact link while editing the Contact Us page:

1.  Double-click the existing link.
112. Make the necessary adjustments in the Link Properties dialog box.
113. Select the Set button.

### Additional Tools Available to Administrators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the Home tab and Administration, the Release Manager role sees the following tabs on their Home page:

- Advanced Query/Customization – See Using Advanced Query/Customization for additional information.
- Contact Us – see Contact Us for additional information.
- Help – see Online Help for additional information.

# Easy Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Easy Search provides a simple way to display commonly-requested PECS information. Easy Search differs from other methods for finding information in that the results are display-only. The records displayed as a result of an Easy Search query cannot be modified. However, in some cases, a link is provided to an editable version of the resulting records.

The Easy Search queries are handled slightly differently depending on which type of search performed. There are three types of Easy Search Query:

- Dose Range
- Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy
- Interactions for a Single Drug

## Easy Search Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy query allows the user to easily search for any Drug-Drug Interaction (and associated Professional Monographs) and/or Duplicate Therapy records that may exist within PECS for at least two and up to ten drugs that are selected by the user. This page also allows the user to search for Duplicate Therapy information for any drug they select.

<span id="_Toc75767290" class="anchor"></span>Figure 94: Easy Search Results Page

![](pecs-version-6-2-user-guide/095.png)

To perform a Drug-Drug Interaction Easy Search Query

1.  From the Select Search Type drop-down list, select 'Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy.' After selecting this value, the system will then display the 'Select Information Type', 'Search and Select Drugs', 'Search Results,' and 'Drugs to Check' panels.

<span id="_Toc75767291" class="anchor"></span>Figure 95: Easy Search Query Selection Drop Down Menu

![](pecs-version-6-2-user-guide/096.png)

114. Choose the appropriate options from the Select Information Type panel:
     - Select Drug-Drug Interaction with Professional Monograph to find Drug-Drug Interactions with the associated Professional Monograph. If the selection is the Drug-Drug Interaction with Professional Monograph checkbox, then the system will display two options: Display Severity Levels 1 (contraindicated) and 2 (severe) and Display All Severity Levels. Select one of these options.
     - Select Duplicate Therapy checkbox to display Duplicate Therapy records (if any) for the selected drugs.

<span id="_Toc75767292" class="anchor"></span>Figure 96: Select Information Type Panel

![](pecs-version-6-2-user-guide/097.png)

115. Enter a partial string or whole drug name into the Drug field and select Search. The system returns all drugs, that is, both routed generic drugs and dispensable drugs that contain the partial string/whole drug name entered.

<span id="_Toc75767293" class="anchor"></span>Figure 97: Search and Select Drugs Panel

![](pecs-version-6-2-user-guide/098.png)

116. Select a drug from the Search Results window and select Add to Drugs to Check. The selected drug will appear in the Drugs to Check box.

<span id="_Toc75767294" class="anchor"></span>Figure 98: Search Results

![](pecs-version-6-2-user-guide/099.png)

117. If necessary, repeat the Search/Select process to add more drugs to the check. For Drug-Drug Interaction queries, select at least two, but up to ten drugs. For Duplicate Therapy, a user can select multiple drugs to find duplicate therapies, or select a single drug to display the associated Therapeutic Class.
118. When all drugs have been added, select Submit. The query results will appear on a results page.

Results

The Drug-Drug Interaction with Professional Monograph and/or Duplicate Therapy query will produce the following results based on the selections made in the query.

Drugs Checked

All Drugs that were selected by the User are listed first on the page after 'Drugs Checked' and each drug name, the Therapeutic Class(es) that drug belongs to are listed for reference.

<span id="_Toc403984434" class="anchor"></span>Figure 99: Easy Search Results for DDI with PM, Drugs Checked

![](pecs-version-6-2-user-guide/100.png)

Drug-Drug Interaction

The Easy Search query Drug-Drug Interaction with Professional Monograph information will display any Drug-Drug Interactions that apply to any combination of the drugs searched. select the "Link to record in PECS" link to display the record in the standard PECS application where it can undertake additional processing.

<span id="_Toc403984435" class="anchor"></span>Figure 100: DDIs Shown Applicable to Drugs Checked

![](pecs-version-6-2-user-guide/101.png)

Professional Monograph

Any associated Professional Monographs to those Drug-Drug Interactions will be listed after the Drug-Drug Interaction information. Select the + symbol to expand the Professional Monograph (collapsed by default). If there is no Professional Monograph associated to the Drug-Drug Interaction returned by the Easy Search query, then this option will not expand.

<span id="_Toc403984436" class="anchor"></span>Figure 101: The Professional Monograph Associated with the DDI/PM Easy Search

![](pecs-version-6-2-user-guide/102.png)

Duplicate Therapy

Duplicate Therapy results the Duplicate Therapy for the drugs selected in the Drugs to Check box. The record contains the Therapeutic Drug Class that the two drugs belong to and Duplicate Allowance numerical value (0,1, 2, 3, or 4) followed by a short message stating these two drugs may represent a duplication in therapy. To view the Duplicate Therapy record in PECS, select "Link to record in PECS."

<span id="_Toc403984437" class="anchor"></span>Figure 102: Duplicate Therapy Easy Search Results

![](pecs-version-6-2-user-guide/103.png)

## Easy Search Interactions for a Single Drug Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Interactions for a Single Drug allows the user to generate a report for all the drug pairs that would be returned in VistA for the selected drug. The report displays FDB and Approved VA custom drug pairs with the specified severity level. FDB drug pairs will display only if there is not a corresponding Approved VA customized drug pair.

To perform an Interactions for a Single Drug Query:

1.  Select "Interactions for a Single Drug" from the Select Search Type drop-down list.

<span id="_Toc75767299" class="anchor"></span>Figure 103: Select Search Type Drop Down Menu

![](pecs-version-6-2-user-guide/104.png)

119. From the Select Information Type panel, choose the desired Severity Level with the appropriate radio button - Severity Level 1 (contraindicated), Severity Level 2 (severe), or Severity Levels 1 (contraindicated) and 2 (severe).

<span id="_Toc75767300" class="anchor"></span>Figure 104: Select Information Types Radio Buttons

![](pecs-version-6-2-user-guide/105.png)

120. Enter a partial string or whole drug name into the Drug field and select Search. Items that match the search string are displayed in the Search Results box. The drug list displays the drug name, dose, route of delivery, and the drug's GCN sequence number. Note that if both a dispensable generic drug and dispensable drug are found that have the same GCN sequence number, only the dispensable drug are displayed on the list. Select an entry from the list.

<span id="_Toc75767301" class="anchor"></span>Figure 105: Search and Select Drugs

![](pecs-version-6-2-user-guide/106.png)

121. Select the Generate Report button. The report generates in Excel. It contains the FDB and VA custom drug pairs whose severity level matches the selected severity level and contain a routed generic drug that corresponds to the selected generic dispensable drug or dispensable drug.

<span id="_Toc75767302" class="anchor"></span>Figure 106: Excel Report for Drug Pair Interaction

![](pecs-version-6-2-user-guide/107.png)

Interactions for a Single Drug Report Details

| Field                            | Description                                                                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Source                           | Source of the record; either VA or FDB                                                                                                  |
| Routed Generic \#1               | A generic drug name, e.g. "Rifampin Oral"                                                                                               |
| Routed Generic \#2               | A generic drug name, e.g. "Rifampin Oral"                                                                                               |
| Severity Level Code              | The severity of the interaction.                                                                                                        |
| Interaction Description          | A brief description of the interaction.                                                                                                 |
| Interaction ID                   | A numerical identifier assigned to the interaction.                                                                                     |
| Corresponding FDB Interaction ID | VA records only: the interaction as described by First Databank. If there is no corresponding interaction, this field will contain '0'. |
| Action Date                      | The date and time of the most recent update to the record.                                                                              |

<span id="_Toc75767178" class="anchor"></span>Table 11: DDI Fields

## Easy Search Dose Range Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dose Range query allows the user to easily find the appropriate dosage information for a specific drug based on the patient and dose particulars entered for a selected drug. The results of this query allow the user to ensure the amount being prescribed is an acceptable amount. An Easy Search Dose Range query allows the user to find the acceptable dose range for a drug quickly and easily, and presents the results in an easy to understand format.

To perform an Easy Search Dose Range query:

1.  From the Select Search Type drop-down list on the Easy Search page, select 'Dose Range.'

<span id="_Toc75767303" class="anchor"></span>Figure 107: Select Search Type Drop Down Menu

![](pecs-version-6-2-user-guide/108.png)

122. Enter a partial string or whole drug name into the 'Drug' field. Note that the user can enter multiple partial strings, and the system returns drugs that match on both strings -- the order of the strings and case are ignored.
123. Select the Search button. The system returns all drugs, that is, both routed generic drugs and dispensable drugs that contain the partial string/whole drug name entered.
124. Select the appropriate drug from the Search Results list. Note that if the drug does not have a defined dose route and/or a defined dose unit, the query cannot be performed and an error message is displayed.

<span id="_Toc75767304" class="anchor"></span>Figure 108: Drug Information Search Results

![](pecs-version-6-2-user-guide/109.png)

125. In the Selected Drug section, select the Dose Type and Dose Route. The available selections will be limited to those appropriate for the selected drug; in some cases, the default values may be the only options available.

<span id="_Toc75767305" class="anchor"></span>Figure 109: Dose Route Selection for a Selected Drug

![](pecs-version-6-2-user-guide/110.png)

126. The Demographic Information section will automatically be populated with standard values. If more appropriate patient information is available, the default values can be replaced. Factors included are:
     - Age (years)
     - Weight (kg or lbs.)
     - Height (cm or in)

<span id="_Toc75767306" class="anchor"></span>Figure 110: Demographic Information

![](pecs-version-6-2-user-guide/111.png)

In the Dosing Information section, enter information about the proposed dose. Factors include:

- Single Dose
- Dose Unit
- Dose Rate Unit
- Frequency

<span id="_Toc75767307" class="anchor"></span>Figure 111: Dosing Information

![](pecs-version-6-2-user-guide/112.png)

Dose Range Query Results

If available, the Dose Range Results section displays the appropriate dose range for the selected drug. The Dose Range record can be viewed in PECS by clicking "Link to record in PECS"

> **NOTE:** Due to a limitation in the FDB database, not all PECS Dose Range records can be linked directly from Easy Search Results. If the record cannot be linked, "Link to record in PECS Not Available" will appear at the bottom of Dose Range Results. Use Advanced Query/Customization to find and view the record in PECS.

<span id="_Toc403984433" class="anchor"></span>Figure 112: Results for a Dose Range Easy Search

![](pecs-version-6-2-user-guide/113.png)

Drug Information

The Easy Search Results section displays the information that was entered into the query.

- Drug Checked
- Drug Information Submitted
  - Single Dose Amount
  - Dose Unit
  - Dose Rate Unit
  - Frequency

Dose Range Information

The Dose Range Results section displays (if available) the appropriate dose range for the selected drug.

- Max Single Dose
- Max Single Dose Message
- Max Single Dose Status
- High Daily Dose
- High Daily Dose Message
- Daily Dose Status
- Frequency Message
- Frequency Status
- Dose Type Description
- Dose Route Description
- Max Daily Dose Message
- Frequency Low
- Frequency High

> **NOTE:** When PECS can't retrieve the selected dose type, dose unit, and dose route for a drug, it displays a message in a popup:

<span id="_Toc75767309" class="anchor"></span>Figure 113: PECS Unable to Retrieve Dose Information Message

![](pecs-version-6-2-user-guide/114.png)

## Potential Easy Search Result and PECS Record Discrepancy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The custom detail pages in PECS show the custom record as it exists in PECS. These detail pages are accessed through either the Advanced Query/Customization tab, or by following the "Link to record in PECS" link found on the Easy Search Results screens.

When you use Easy Search to look up Drug-Drug Interactions or Duplicate Therapy, Easy Search uses a different database table than the one used to store the actual PECS record. The Easy Search results page shows only data from custom records in an Approved state that have been exported in a custom update and processed by an external process named DATUP. If a custom record has not gone through this process, you will see the FDB record and there will be a discrepancy.

If a previously approved/exported custom record is updated, then Easy Search will not show the updated data in the results page until the record is approved, exported, and processed by DATUP. Instead, Easy Search will show the custom record results that were last uploaded to DATUP.

Below are examples of discrepancies. Remember that these discrepancies cannot be duplicated and re-displayed after a custom update has been approved and run through DATUP, so do not try to re-create them. They are for informational purposes only, and even shown as an older screen capture of PECS (no Contact Us tab). Example one, is from Easy Search.

<span id="_Toc403984438" class="anchor"></span>Figure 114: Easy Search DDI Record

![](pecs-version-6-2-user-guide/115.png)

Example two, is shown by clicking the "Link to record in PECS" link as is shown above. This discrepancy means the custom record has not been approved and/or not processed through DATUP. This potential discrepancy applies to Drug-Drug Interaction, Professional Monograph, Duplicate Therapy, and Dose Range concepts.<span id="_Toc403984439" class="anchor"></span>

Figure 115: Referenced PECS Record with Name Discrepancy

![](pecs-version-6-2-user-guide/116.png)

# Drug Pair Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Drug Pair is a combination of drugs known to cause a drug interaction. A drug interaction is a situation in which a substance (usually another drug) affects the activity of a drug when both are administered together. Drug Pair Lookup provides a quick and easy way to search both the FDB and VA databases for these drug pairs.

When performing a Drug Pair Lookup query, enter query criteria in any or all of the four entry fields. The results are displayed under the VA Table Results and FDB Table Results panels. These consist of active customized Drug Pair records from the VA custom database that are available for modification, as well as their related Drug Pair records from the FDB database from which they were customized.

Field names are as follows:

- Drug A (Generic) - The name (or partial name) of one generic drug associated with an interaction.
- Drug B (Generic) - The name (or partial name) of a second generic drug associated with an interaction.
- Interaction - An assigned drug interaction number and description associated with the drug pair. This can be entered in conjunction with the Drug A and Drug B entries or can be used on its own. Enter either *all* of the Interaction ID, or all or part of the interaction description.
- Severity Level Code - A drop-down list of available severity codes that are allowed for an interaction. This can be used on its own, but is most useful to limit the results produced by the other criteria.

## Performing a Drug Pair Lookup Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To perform a Drug Pair Lookup query:

1.  Fill the query form with the search criteria; greater detail will yield more relevant results.

<span id="_Toc75767312" class="anchor"></span>Figure 116: Drug Pair Descriptions and Severity Level Codes

![](pecs-version-6-2-user-guide/117.png)

127. Select Query.
128. Drug Pairs matching the query criteria (both VA and FDB) will display in their respective panels. If the results are unsatisfactory, then the user can adjust the query criteria and select Query again.

<span id="_Toc75767313" class="anchor"></span>Figure 117: Drug Pairs Matching the Query Display

![](pecs-version-6-2-user-guide/118.png)

129. Select the link in the Select column to view the drug pair record. VA records will display and Active link; FDB records display an Open link.

<span id="_Toc75767314" class="anchor"></span>Figure 118: Drug Pair Selection List

![](pecs-version-6-2-user-guide/119.png)

130. To further customize the record, select the Interaction ID link to display the Drug-Drug Interaction (and the associated Drug Pairs).

<span id="_Toc75767315" class="anchor"></span>Figure 119: Interaction ID Link

![](pecs-version-6-2-user-guide/120.png)

## Export Query Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can export the results of a Drug Pair Lookup query to an Excel spreadsheet.

1.  Perform a Drug Pair Lookup Query.
131. Select the Export button associated with the Results list. The Export option is available for both VA and FDB results.

<span id="_Toc75767316" class="anchor"></span>Figure 120: VA and FDB Results to Export

![](pecs-version-6-2-user-guide/121.png)

132. Select Open to display the Drug Pair Report; select Save to save a copy of the report to your system.

<span id="_Toc75767317" class="anchor"></span>Figure 121: Internet Explorer Download Screen

![](pecs-version-6-2-user-guide/122.png)

The spreadsheet contains two tabs:

1.  The Drug Pair tab (either VA or FDB) displays the results of the query.

<span id="_Toc75767318" class="anchor"></span>Figure 122: Drug Pair Tab of the Excel Exported Report

![](pecs-version-6-2-user-guide/123.png)

3.  The Criteria tab displays the criteria used in the query.

<span id="_Toc75767319" class="anchor"></span>Figure 123: Criteria Tab of Excel Spreadsheet

![](pecs-version-6-2-user-guide/124.png)

Export Query Line Limit

There is a 1,000,000 line limit for exporting to the spreadsheet. If the query returned more than 1,000,000 records and the records were submitted for export anyway, the Criteria tab on the report gives the following message: "The number of rows returned in the search (XXXXXX) is greater than the maximum number of rows that can be exported (1,000,000)."

<span id="_Toc75767320" class="anchor"></span>Figure 124: Export Query Line Limit Message

![](pecs-version-6-2-user-guide/125.png)

# Detail Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail Pages are the display mechanism for PECS records. To display the information contained in the record, and in the case of FDB records, provide a means to customize that record. There are detail pages for each of the five concepts (Drug-Drug Interaction, Drug Pairs, Professional Monograph, Duplicate Therapy, and Dose Range).

## Detail Page Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail Pages display the details of the record appropriate to the concept being viewed for both FDB and VA records. The sections below are taken from a Drug-Drug Interaction records, but the detail page behaviors are consistent among the different Concepts.

FDB Records

<span id="_Toc403984448" class="anchor"></span>Figure 125: FDB DDI Record

![](pecs-version-6-2-user-guide/126.png)

With FDB records, the user can:

- [View Record Details](#viewing-record-details)
- [Customize the FDB Record](#working-with-customization-requests)
- View Associated Record Links

VA Records

<span id="_Toc403984449" class="anchor"></span>Figure 126: VA Custom DDI

![](pecs-version-6-2-user-guide/127.png)

With VA records, the user can:

- [View Record Details](#viewing-record-details)
- Edit a Record
- Print a Record
- [Add Pre-Customization Comments](#add-pre-customization-comments)
- View Associated Record Links
- View [History Report](#history-report)
- View [Field-Level History](#field-level-history-table)
- View Export Date

### Informational and Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some records have informational and warning messages associated with them. These messages provide information about the record itself not necessarily the contents of the record.

<span id="_Toc403984455" class="anchor"></span>Figure 127: Informational and Warning Messages

![](pecs-version-6-2-user-guide/128.png)

## Using Detail Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detail pages provide information about the PECS records. The information on the page is slightly different for each concept, but the basic functions are the same.

<span id="_Toc403984450" class="anchor"></span>Figure 128: Example of a Detail Page

![](pecs-version-6-2-user-guide/129.png)

### Viewing Record Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Page for Requestors and Approvers contains links to pre-defined queries that facilitate viewing records. Requestors can use these links to view details of records that they have created.

Approvers can use the links to view details of records they created, records currently assigned to them for some action, unassigned records, and All records.

All users can use Advanced Query/Customization to find and view record details.

### Edit a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Editing a record is different depending on the type of record it is, and the current state of that record. For example, if viewing an FDB record, editing it produces a customization. If viewing a VA record, editing could mean:

- Changing the record details (modify)
- Reviewing an existing record as part of the approval process
- Approving an existing record
- Rejecting an existing record
- Deleting an existing record

In all cases, select Edit to begin the modification process. See Working with Customization Requests for additional information on the modifications that can performed on a record.

<span id="_Toc75767325" class="anchor"></span>Figure 129: Use the Edit button to Modify Record Details

![](pecs-version-6-2-user-guide/130.png)

Only Requestor and Approvers can modify a record. Requestors can only modify FDB records (customize) or VA records they have created. Approvers can also modify/customize FDB records and can also modify most VA records with the following exception: they cannot Review a record they created. See Working with Customization Requests for additional information.

> **NOTE:** If the user is a Release Manager or Administrator but has not been assigned that role by a PECS Administrator, they will have Requestor privileges until their appropriate role is assigned.

In some cases, PECS will display the Edit button and allow the user to view the record in Edit mode. However, any changes made to the record cannot be saved. Use Cancel Edit to return to the detail page in read-only mode.

### Print a Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Page button calls the browser Print function, allowing the user to print the page to any printer they have connected to their system.

<span id="_Toc75767326" class="anchor"></span>Figure 130: Print Page Button

![](pecs-version-6-2-user-guide/131.png)

### Add Pre-Customization Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approver users can add comments to FDB records that do not have customized VA versions. The comments are visible on the FDB record and contain the text of the comment as well as the date and time it was entered and the PECS User ID of the person who entered it. Once entered, these comments cannot be edited or deleted.

If the FDB record is customized, then the pre-customization comments will become part of the customized record. Once customized, you cannot add additional pre-customization comments to an FDB record.

To add a pre-customization comment:

1.  Select the Add Comment button:

<span id="_Toc75767327" class="anchor"></span>Figure 131: Add Comment Button

![](pecs-version-6-2-user-guide/132.png)

133. Enter the comment in the Enter Comments dialog box:

<span id="_Toc75767328" class="anchor"></span>Figure 132: Enter Comments Dialog Box

![](pecs-version-6-2-user-guide/133.png)

134. Select Save to save your changes, or select Cancel to abandon the enter comments process and return to the record. The comments appear in the Pre-Customization Comment History of the record.

<span id="_Toc75767329" class="anchor"></span>Figure 133: Example of Pre-Customization Comment History

![](pecs-version-6-2-user-guide/134.png)

### View Associated Record Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an FDB record has been customized, then the links to the VA-customized records are provided.

<span id="_Toc403984456" class="anchor"></span>Figure 134: VA Custom Record ID Links

![](pecs-version-6-2-user-guide/135.png)

VA records provide links to the original FDB record as well as any additional customizations created from the original FDB record.

<span id="_Toc403984457" class="anchor"></span>Figure 135: VA Custom and FDB Record Links

![](pecs-version-6-2-user-guide/136.png)

### History Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

History Reports detail all the changes made to the current record. Changes to most editable fields will appear in the report as red text with an asterisk (\*). Changes to the Current Action Reason are not highlighted (red) in the History Report. It is presented as a Microsoft Excel spreadsheet.

To display a History Report:

135. From the Detail page, Select the History button.

<span id="_Toc75767332" class="anchor"></span>Figure 136: History Button

![](pecs-version-6-2-user-guide/137.png)

136. Select Open to display the History Report. Select Save to save a copy of the report to your system:

<span id="_Toc75767333" class="anchor"></span>Figure 137: Internet Explorer Download Dialog Box

![](pecs-version-6-2-user-guide/138.png)

137. If you chose to Open the report, then it will be displayed. If you chose Save, then the report can be opened at any time using Excel.

<span id="_Toc75767334" class="anchor"></span>Figure 138: Example of an Excel Report with Changed Data

![](pecs-version-6-2-user-guide/139.png)

### Field-Level History Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user can review a list of changes to an individual field by hovering over the History Table icon next to a field that has been changed. Field-level history is retained only while the record is in its current state. The field-level history is reset when the state changes to Approved or Deleted (Modified or Reviewed doesn't cause a reset). Field-level history is only displayed for Required Fields with the exception of Current Action Reason; field-level history is not retained for Current Action Reason, but it can be viewed on the History Report along with changes to non-required fields.

<span id="_Toc403984458" class="anchor"></span>Figure 139: At-a-Glance History Icon

![](pecs-version-6-2-user-guide/140.png)

<span id="_Toc403984459" class="anchor"></span>Figure 140: On-Screen History Table from Icon

![](pecs-version-6-2-user-guide/141.png)

### Export Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Export Date field appears on the VA Custom Detail Pages and in the Customization Reports. It contains the date and time an Approved or Deleted record was included in the Incremental Update File, so it is only populated on records with Action Status' equal to Approved or Deleted.

> **NOTE:** If an Incremental Update File has not been created since the record Action Status was change to Approved or Deleted, then the Export Date will be blank until the next Incremental File is created.

Sometimes an Approved or Deleted record included on an Incremental Update File needs to be changed. Any change to that record will cause the Export Date field to be cleared (blank) in the active record. The only way to determine that the record has been exported is to view the History report or search for the record using Advanced Query/Customization and select Include Historical Records.

If the change to the record causes a change to the Action Status and that modification is later Rejected, then the following happens:

If a "Modified after Approved" (displays as Modified in PECS) record is Rejected:

The Action Status "rolls back" to Approved, and the record will be included in the next Incremental Update File and the Export Date will be updated.

If a "Modified after Delete" (displays as Modified in PECS) record is Rejected:

The Action Status "rolls back" to Deleted. However, records that roll back to a Deleted Action Status are NOT included in the next Incremental Update File, so the Export Date will NOT be updated and will remain blank on the active record.

## Drug-Drug Interaction Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug-Drug Interaction Detail page allows users to view the details of both FDB and VA Drug-Drug Interaction records. FDB Drug-Drug Interactions can be customized to become VA Drug-Drug Interactions. See Working with Customization Requests for additional information on creating a VA customization request.

<span id="_Toc403984465" class="anchor"></span>Figure 141: Detail Page of VA Customized DDI Top

![](pecs-version-6-2-user-guide/142.png)

<span id="_Toc75767338" class="anchor"></span>Figure 142: Detail Page of VA Customized DDI Bottom

![](pecs-version-6-2-user-guide/143.png)

### Multiple VA Customizations for One FDB Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A user can create multiple VA Custom Drug-Drug Interactions (DDIs) from one corresponding FDB Record. If a user opens an FDB DDI record on the Advanced Query/Customization page, then the DDI Detail page will open. If there are any VA custom records for this FDB DDI, then a message is displayed stating that "The following VA custom record(s) already exist for this FDB Drug-Drug Interaction," and a table and a link to any interactions displays.

<span id="_Ref418079531" class="anchor"></span>Figure 143: Multiple VA Custom DDIs to One FDB Record

![](pecs-version-6-2-user-guide/144.png)

From here, a user can create another custom record. Checks exist in the system so that the same user cannot make duplicate DDIs or another user cannot come in and make the same DDI that another user just made.

### Create Multiple Customizations from One FDB Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug-Drug Interactions and Dose Range records can be customized multiple times from a single FDB record.

To create multiple customizations from one FDB record:

1.  Find and display the FDB record to be customized using Advanced Query/Customization.
138. Select Edit.
139. Create the custom record by changing something and selecting Customize.
140. The new record is created. The record ID is displayed on the Interaction ID field. If there are any duplicates or other discrepancies, then a warning message will be displayed (such as an identical interaction severity):

<span id="_Toc75767340" class="anchor"></span>Figure 144: FDB ID Record

![](pecs-version-6-2-user-guide/145.png)

141. Repeat the process using the same FDB record as many times as necessary.

### Cannot Add Identical Drug Pairs to Same DDI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After one user has created a new DDI or added new drug pairs to an existing DDI, a second user can come in and attempt to add the same drug pairs. A users cannot add a drug pair that currently exists for the selected DDI:

<span id="_Toc403984467" class="anchor"></span>Figure 145: Error for Duplicate Drug Pairs for One DDI

![](pecs-version-6-2-user-guide/146.png)

The user will also receive an error if they attempt to customize a drug pair for a DDI in Reverse Order:

<span id="_Toc403984468" class="anchor"></span>Figure 146: Error for Duplicate Drug Pairs in Reverse Order for One DDI

![](pecs-version-6-2-user-guide/147.png)<span id="PREC_3_0_1_ReverseDDI" class="anchor"></span>

### Reverse Drug-Drug Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multiple Drug-Drug Interaction records may exist for the same drugs listed in reverse order. For example, FDB Interaction ID 1234 is Drug A/Drug B and FDB Interaction ID 30766 is Drug B/Drug A. Information about reverse DDIs is displayed in the table at the top of the detail page. The screen shot below displays FDB record 1637, which has a DDI customization and a reverse DDI customization.

<span id="_Toc403984469" class="anchor"></span>Figure 147: FDB DDI with a Customization and a Reverse Customization

![](pecs-version-6-2-user-guide/148.png)

If a user selects the link associated with the reverse DDI, then they will see its detail page (next screen shot):

<span id="_Toc403984470" class="anchor"></span>Figure 148: Choosing the Reverse VA DDI Customization

![](pecs-version-6-2-user-guide/149.png)

The detail page of the Reverse VA Customization is displayed:

<span id="_Toc403984471" class="anchor"></span>Figure 149: Reverse FDB Interaction ID

![](pecs-version-6-2-user-guide/150.png)

<span id="Display_Reverse_FDB_DDI_Interaction_ID" class="anchor"></span>Displaying the Reverse FDB DDI Interaction ID

The Reverse FDB DDI Interaction ID is displayed in the VA custom DDI and DP Detail pages, in the results of DDI and Drug Pair queries and on the FDB Custom DDI Report. The Reverse FDB DDI Interaction ID is defined as the reverse of the FDB DDI ID and is obtained by executing this equation:

32,000 – (minus) FDB Monograph ID.

For example:

- If FDB monograph ID is 2246, then the reverse FDB DDI ID is 29745 (32,000 – 2246 = 29745)
- If FDB monograph ID is 29754, then the reverse FDB DDI ID is 2246 (32,000 – 29754 = 2246)
- If FDB monograph ID is 0, then the reverse FDB Interaction ID is 0 ( i.e., DDI was created from scratch using the Open Blank Form option)

Displaying the reverse FDB DDI Interaction ID in the DDI and DP detail pages, query results, and reports enables the user to find information about reverse DDIs easily.

### Working with Drug Pairs within the DDI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that a user can work with a drug pair only by starting from the Drug-Drug interaction page, and selecting the Drug Pairs button.

See the Drug Pair Detail for additional information.

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Table Heading Name                | Table Heading Description                                                                                                                                                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monograph ID                      | The Professional Monograph ID associated with the drug interaction pair.                                                                                                                                                  |
| Action Status                     | Applicable to VA record only. The point this customization is at, within the VA Approval Workflow.                                                                                                                        |
| Corresponding FDB Interaction ID  | The system ID of the FDB record from which the VA customization was created.                                                                                                                                              |
| Interaction ID                    | The system ID of this VA customization.                                                                                                                                                                                   |
| Reverse FDB ID                    | The FDB ID associated with a customized reverse interaction ID.                                                                                                                                                           |
| Severity Level Code               | The level of severity for this Drug-Drug Interaction.                                                                                                                                                                     |
| Action Date                       | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                            |
| Action Performed By               | Applicable to VA record only. The name of the user that performed the last action.                                                                                                                                        |
| Request Submitted By              | Applicable to VA record only. The name of the user that submitted this VA request.                                                                                                                                        |
| Action Effective Date             | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                            |
| Request Assigned To               | Applicable to VA record only. A drop down list to assign an approver.                                                                                                                                                     |
| Clinical Effect Code 1            | Clinical effect code.                                                                                                                                                                                                     |
| Clinical Effect Code 2            | Clinical effect code                                                                                                                                                                                                      |
| EDI Number                        | The severity level from the Evaluations of Drug Interactions (EDI) system.                                                                                                                                                |
| EDI Text                          | The interaction text found in EDI.                                                                                                                                                                                        |
| DI Facts Number                   | Severity number of interaction found in DI Facts.                                                                                                                                                                         |
| DI Facts Onset                    | The onset of the interaction as found in DI facts.                                                                                                                                                                        |
| DI Facts Severity                 | The severity level of the interaction found in DI facts.                                                                                                                                                                  |
| DI Facts Documentation            | Documentation of the interaction found in the DI Facts.                                                                                                                                                                   |
| DI Facts Text                     | The text of the interaction from DI facts.                                                                                                                                                                                |
| Micromedex Severity               | The severity found in Micromedex.                                                                                                                                                                                         |
| Micromedex Onset                  | The onset of the interaction as found in Micromedex.                                                                                                                                                                      |
| Micromedex Substantiation         | Level of documentation of the interaction found in the Micromedex.                                                                                                                                                        |
| Micromedex Text                   | The interaction text found in Micromedex.                                                                                                                                                                                 |
| Medline Hits                      | A dropdown list to select whether or not this reference was checked.                                                                                                                                                      |
| Medline Text                      | Brief description of literature results.                                                                                                                                                                                  |
| Package Insert                    | A dropdown list to select whether or not this reference was checked.                                                                                                                                                      |
| Package Insert Text               | The interaction text found in the package insert.                                                                                                                                                                         |
| PBM Criteria                      | A dropdown list to select whether or not this reference was checked.                                                                                                                                                      |
| PBM Criteria Text                 | Text information found in PBM criteria.                                                                                                                                                                                   |
| AIDS Guidelines                   | A dropdown list to select whether or not this reference was checked.                                                                                                                                                      |
| AIDS Guidelines Text              | Text information from the AIDS guidelines.                                                                                                                                                                                |
| Interaction Source                | A drop-down list to select source.                                                                                                                                                                                        |
| Interaction Type                  | A drop-down list to select type.                                                                                                                                                                                          |
| Highest Level of Evidence         | A drop-down list to select the source of the evidence to support the described drug-drug interaction.                                                                                                                     |
| Group Discussion                  | General comment from meeting.                                                                                                                                                                                             |
| Action Reason History             | Applicable to VA record only. All historical current action reason comments for this record, in one viewable field.                                                                                                       |
| Current Action Reason (optional)  | Applicable to VA record only. Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization. |
| Export Date                       | For Approved or Deleted records. Indicates the date of the last Custom Update. See Export Date for additional information.                                                                                                |
| Pre-Customization Comment         | Approvers can add comments to un-customized FDB records in this field and select the add comment button to save the comment                                                                                               |
| Pre-Customization Comment History | Displays all comments that have been added to this record prior to customization                                                                                                                                          |

<span id="_Ref415651059" class="anchor"></span>Table 12: Field Descriptions for Drug Pair Detail

## Drug Pair Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug Pairs are sets of drugs that are associated with a drug-drug interaction. The Drug Pair detail page allows a user to view the details of a drug pair associated with a Drug-Drug Interaction. Unlike other detail pages, there is no way to directly edit a drug pair from a drug pair detail page. Instead, the user must make the modifications through the associated Drug-Drug Interaction. See Drug Pair Customization (Non 508-Compliant) Detail or Section 508 Compliant Drug Pair Customization Detail for additional information.

<span id="_Toc75767346" class="anchor"></span>Figure 150: The Drug Pair Detail Page – VA

![](pecs-version-6-2-user-guide/151.png)

<span id="_Toc75767347" class="anchor"></span>Figure 151: Drug Pair Detail Page - FDB

![](pecs-version-6-2-user-guide/152.png)

### Fields and Other Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information presented on a drug pair detail page is also different from other record types.

Informational Messages

Informational messages are critical with drug pairs. They associate the displayed drug pair with any associated Drug-Drug Interaction.

<span id="_Toc75767348" class="anchor"></span>Figure 152: Example of Informational Messages for Drug Pair Detail

![Table 12 describes the fields for a Drug Pair record. Not all fields are applicable to all record types (FDB or VA).](pecs-version-6-2-user-guide/153.png)

*Table 12 describes the fields for a Drug Pair record. Not all fields are applicable to all record types (FDB or VA).*

| Field Name                       | Field Description                                                                                                                                                                                                                                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action Status                    | Applicable to VA record only. It is the status of this customization within the VA Approval Workflow.                                                                                                                                                                                                                               |
| Routed Generic \#1               | The ID of the first drug in this Drug Pair.                                                                                                                                                                                                                                                                                         |
| Routed Generic \#1 Description   | Applicable to FDB record only. The description of the first drug in this Drug Pair.                                                                                                                                                                                                                                                 |
| Routed Generic \#2 (required)    | The ID of the second drug in this Drug Pair.                                                                                                                                                                                                                                                                                        |
| Routed Generic \#2 Description   | The description of the second drug in this Drug Pair.                                                                                                                                                                                                                                                                               |
| Severity Level Code              | Applicable to FDB record only. The severity level code for this Drug-Drug Interaction.                                                                                                                                                                                                                                              |
| Severity Level Description       | The description of the severity level code for this Drug-Drug Interaction.                                                                                                                                                                                                                                                          |
| Interaction ID                   | The ID number of the FDB or VA Custom Drug-Drug Interaction associated with the drug pair.                                                                                                                                                                                                                                          |
| Interaction Description          | Applicable to FDB record only. The description of the Interaction ID that the drug pair is associated with.                                                                                                                                                                                                                         |
| Corresponding FDB Interaction ID | Applicable to VA records only. It is the Interaction ID of the FDB record from which the VA Drug interaction customization was created.                                                                                                                                                                                             |
| Reverse FDB ID                   | Applicable to VA records only. It is the Reverse FDB Drug-Drug Interaction ID, or the Reverse Interaction ID of the DDI FDB record from which the DDI custom record was created. For more information about the Reverse FDB DDI ID, see "[Displaying the Reverse FDB DDI Interaction ID](#Display_Reverse_FDB_DDI_Interaction_ID)". |
| Action Performed By              | Applicable to VA records only. The name of the user who performed the action.                                                                                                                                                                                                                                                       |
| Request Assigned To              | Applicable to VA records only. The name of the PECS user assigned to process the customization request.                                                                                                                                                                                                                             |
| Request Submitted by             | Applicable to VA records only. The name of the user that submitted this VA request.                                                                                                                                                                                                                                                 |
| Reference Text                   | Applicable to VA records only. Field for the user to enter any reference text needed to support customization of the drug pair.                                                                                                                                                                                                     |
| Action Reason History            | Applicable to VA records only. All historical 'current action reason' comments for this record, in one viewable field.                                                                                                                                                                                                              |
| Current Action Reason            | Applicable to VA records only. Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization.                                                                                                          |
| Export Date                      | Applicable to VA records only. Date that the approved or deleted drug pair record was exported to the incremental update file                                                                                                                                                                                                       |
| Action Date                      | Applicable to VA records only. The date of the last action taken on the record.                                                                                                                                                                                                                                                     |

<span id="_Ref416092349" class="anchor"></span>Table 13: Drug Pair-related Information

### Finding Drug Pairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug pairs are usually found and processed directly from the Drug-Drug Interaction they are associated with. However, a user can search for them directly using either Advanced Query/Customization or Drug Pair Lookup. When searching for drug pairs directly, what is displayed is dependent the record type (VA or FDB) and whether the associated Drug-Drug Interaction has been customized. In all cases, drug pair records cannot be edited directly; the user must work through an associated Drug-Drug Interaction.

- If the results locate a customized VA Drug Pair, then the VA Drug Pair detail page for that Drug Pair is displayed. The detail page contains a link to the associated Drug-Drug Interaction(s).
- If the results locate an FDB drug pair record that has been customized by VA, then the FDB Drug Pair Detail page is displayed. The detail page contains a link to the FDB Drug-Drug Interaction and the customized VA Drug-Drug Interaction created from the FDB Drug-Drug Interaction.
- If the results locate an FDB drug pair record that has NOT been customized by VA, then the associated FDB Drug-Drug Interaction detail page is displayed.

Using Advanced Query/Customization

To find a drug pair using Advanced Query/Customization:

1.  Select the Advanced Query/Customization tab.
142. Select Drug Pair from the Select Concept List and select the appropriate drug pair type from the Select VA, FDB, or Both list.
143. Build the query to find the appropriate drug pair and select Query.
144. Select the link in the Select column to open the record. The record that is displayed depends on the record type.

See Using Advanced Query/Customization for additional information.

Using Drug Pair Lookup

To find a drug pair using Drug Pair Lookup:

1.  Select the Drug Pair Lookup tab.
145. Build the query to find the appropriate drug pair and select Query.
146. Select the link in the Select column to open the record. The record that is displayed depends on the record type.

See Drug Pair Lookup for additional information.

### FDB Drug Pair Detail Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user opens an FDB Drug Pair that is not customized, but the associated FDB Drug-Drug Interaction is customized, the FDB Drug Pair Detail Page is displayed. The informational message will contain all VA Custom Drug-Drug Interactions associated with the FDB Drug-Drug Interaction(s) associated with the drug pair. To customize the drug pair, select the appropriate linked interaction in the informational message.

<span id="_Toc403984461" class="anchor"></span>Figure 153: Un-Customized FDB Drug Pair

![](pecs-version-6-2-user-guide/154.png)

FDB Drug Pair Not Customized, Not Associated with Customized Drug-Drug Interaction

When a user opens an FDB drug pair that has not been customized and is not associated with a customized Drug-Drug Interaction the FDB Drug-Drug Interaction associated with the drug pair is displayed. To customize the FDB Drug-Drug Interaction and the associated drug pairs, select the Interaction ID link.

<span id="_Toc403984462" class="anchor"></span>Figure 154: FDB Drug-Drug Interaction without Customized Drug Pairs

![](pecs-version-6-2-user-guide/155.png)

FDB Drug Pair Customized Once

When a user opens an FDB Drug pair that has been customized once they will be presented with the VA customized drug pair and a link to the associated VA Drug-Drug Interaction ID.

<span id="_Toc403984463" class="anchor"></span>Figure 155: Drug Pair Detail Page (Read Only)

![](pecs-version-6-2-user-guide/156.png)

FDB Drug Pair Customized More Than Once

An FDB Drug Pair can be customized more than once. For example, a Drug Pair can be customized for a VA Drug-Drug Interaction and subsequently rejected or deleted. It can then be customized a second time for a different VA DDI. In this case, when the user opens the FDB Drug Pair record, they will not only get information about the FDB drug pair and its associated FDB DDI, but they will see two messages about the drug pair and the custom VA DDIs it is associated with. One message says that the drug pair is rejected, and the other message says that it is in the New Action Status. Two examples follow:

1.  The following example shows what will display if the user opens an FDB Drug Pair that was customized for and subsequently rejected from DDI 2021210, and then customized a second time for DDI 2021211. Note the informational messages and the links to the FDB and custom VA DDIs:

<span id="_Toc75767352" class="anchor"></span>Figure 156: FDB Drug Pair Message One

![](pecs-version-6-2-user-guide/157.png)

147. The following example shows what will display if the user opens an FDB Drug Pair that was customized and subsequently rejected from DDI 2021212, customized a second time and subsequently deleted from DDI 2021213, and customized for DDI 2021214. Note the informational messages and links to all customizations:

<span id="_Toc75767353" class="anchor"></span>Figure 157: FDB Drug Pair Message Two

![](pecs-version-6-2-user-guide/158.png)

### VA Customized Drug Pair Detail Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user opens a VA Customized drug pair, they will be presented with the customized Drug Pair Detail page.

<span id="_Toc403984464" class="anchor"></span>Figure 158: VA Customized Drug Pair

![](pecs-version-6-2-user-guide/159.png)

## Drug Pair Customization (Non 508-Compliant) Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug Pair Customization (Non 508 Compliant) page allows users to create or delete drug pairs associated with the VA Customized Drug-Drug Interaction as well as perform mass VA Workflow updates to all associated Drug Pairs. To reach this page, select the "Drug Pairs" button on a VA customized Drug-Drug Interaction detail page.

<span id="_Toc403984472" class="anchor"></span>Figure 159: Drug Pair Customization Window

![Table 13 displays information related to the drug pair.](pecs-version-6-2-user-guide/160.png)

*Table 13 displays information related to the drug pair.*

| Field Name                | Field Description                                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interaction Type          | The type of interaction displayed, either VA or FDB.                                                                                                                  |
| Interaction ID            | The numerical reference number assigned to the interaction by the agency referenced in the Interaction Type field.                                                    |
| Interaction Description   | The name of the drug pair associated with the interaction.                                                                                                            |
| Interaction Severity      | A numerical indicator of the severity of the interaction.                                                                                                             |
| Interaction Action Status | The status of the interaction in the VA Approval Workflow. The Action Status for FDB Records will always be 'N/A,' as it does not go through the VA Approval Workflow |

<span id="_Toc75767181" class="anchor"></span>Table 14: Drug Pair Fields

There are two methods to add drug pairs to a drug-drug interaction customization: from existing FDB Drug Pairs (see page ) and from Routed Generics (see page ).

| Field Name            | Field Description                                                                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Text        | Field for the user to enter any drug pair reference text needed to support the addition of this/these drug pair(s).                                                                                                       |
| Current Action Reason | Applicable to VA record only. Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization. |

<span id="_Toc75767182" class="anchor"></span>Table 15: Drug Pair Buttons

| Button Name | Button Description                                                                         |
|-------------|--------------------------------------------------------------------------------------------|
| Customize   | Creates the Drug Pair record and associates it to the VA Customized Drug-Drug Interaction. |
| Cancel Edit | Disregards chosen Drug Pair and any text entered into fields and collapses this panel.     |

<span id="_Toc75767183" class="anchor"></span>Table 16: Professional Monograph Fields

### Drug Pairs Panel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug Pairs panel contains all the VA Customized Drug Pairs already associated to the VA Customized Drug-Drug Interaction (noted at the top of the page). The panel contains

- Interaction Description - VA Customized Drug-Drug Interaction Description
- Routed Generic \#1 Description - First drug in the drug pair
- Routed Generic \#2 Description - Second drug in the drug pair
- Action Status - current status of the Drug Pair
- Request Submitted By - User ID of the PECS user who made the initial customization request
- Action Date - The date of the most recent action
- Action Performed By - User ID of the PECS user who performed the most recent action
- Request Assigned To - User ID of the PECS user who is responsible for reviewing the drug pair information
- Interaction ID - The numerical identifier for the Drug-Drug Interaction
- Severity Level Description - A text description of the interaction severity
- Reference Text - Contents of the Reference Text field
- Severity Level Code - A numerical identifier for the severity of the Drug-Drug Interaction

The checkboxes at the top allow the user to filter what is displayed in the interaction table by Action Status (Historical records are not displayed). They can only process records that are in the same Action Status.

<span id="_Toc403984473" class="anchor"></span>Figure 160: Drug Pair List Filters

![](pecs-version-6-2-user-guide/161.png)

The "Get Record Counts" button displays count of all VA customized drug pairs associated with the Drug-Drug Interaction. This helps the user to determine how many drug pairs to select to perform an action against at one time. It is recommended that quantities be limited to 200 drug pairs at a time to prevent negative impacts to system performance.

For more information, see the following:

- Customizing Drug Pairs from the Selection List
- Drug-Drug Interaction Detail

### Notification of Drug Pairs Needing Action for an Approved Drug-Drug Interaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The drug pairs that are associated with a Drug-Drug Interaction (DDI) need to go through the approval/status change process themselves (be approved, rejected, modified, or deleted), separately from the DDI. If the drug pairs are acted upon at the same time as the DDI is acted upon, then there is no problem in an Approver knowing that the drug pair needs to be acted upon. However, drug pairs may be added or modified even after a DDI has been acted upon. The way an Approver will know if they need to act on a drug pair associated with an already-approved DDI is by the row on the home page tables that displays the row "Approved Drug-Drug Interaction with Pending Drug Pairs."

<span id="_Toc403984474" class="anchor"></span>Figure 161: Approved DDIs with Pending Drug Pairs on Home Page

![](pecs-version-6-2-user-guide/162.png)

From the screen above, if a user selects the link "My Assigned Drug Pairs Associated with Approved Drug-Drug Interactions" for one of the states listed that has actual counts (not zero), then they are taken to the Advanced Query/Customization page that displays the results for all Drug-Drug Interactions with associated Drug Pairs assigned to the user in that state. Here the user can act on the drug pairs.

<span id="_Ref418087220" class="anchor"></span>Figure 162: My Assigned DDIs with Pending Drug Pairs List

![](pecs-version-6-2-user-guide/163.png)

Here is the Interaction window shown after the link is selected from the Advanced Query Page. On the Interaction window the user can act on the drug pairs -- to do so, select the Drug Pairs button:

<span id="_Toc403984476" class="anchor"></span>Figure 163: DDIs with Needed Drug Pairs – Add with Drug Pairs Button

![](pecs-version-6-2-user-guide/164.png)

After the user selects the Drug Pairs button, they can go through the process described in Customizing Drug Pairs from the Selection List (after the user clicks the Edit button).

The paragraphs below describe in detail the process for assigning the request to other Approvers for action.

When a user is working with the Drug Pair customization window, there is a drop-down where they can assign the request to a user ID. The default is the Approver who is assigned to the DDI, but that can changed.

<span id="_Toc403984477" class="anchor"></span>Figure 164: Assigned To: Drop-Down

![](pecs-version-6-2-user-guide/165.png)

If a user changes the status of the drug pairs to Submit as Reviewed or Submit for Delete, then the drug pairs are automatically reassigned to the "Unassigned" User ID if the user who is assigned to the DDI is the same user who is making the status change. The reassignment happens because the person who submits can't also do the approval or delete the drug pairs.

Notes: If a user changes the status of the drug pairs to Submit as Reviewed or Submit for Delete, then the drug pairs are automatically reassigned to the "Unassigned" category.

If a user puts a Drug-Drug Interaction (DDI) into the Delete Reviewed status, then the Drug Pairs associated with the DDI must be in either a "Delete Reviewed," "Rejected" or "Deleted" status.

A routed generic Drug Pair that was deleted and then customized in the reverse order will be listed with those in the New Action Status and displayed in reverse order in the Drug Pairs table on the Drug Pairs Customization page.

### Customizing Drug Pairs from the Selection List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS allows a user to create multiple drug pairs for an interaction at one time. This same multi-select method allows them to batch process drug pairs for other operations such as Review, Reject, and Delete. The process differs slightly between drug pairs created from a corresponding FDB interaction or using routed generic drugs.

Adding Drug Pairs from Corresponding FDB Interaction

When adding FDB Drug Pairs to an interaction on the Batch Customization page, the user may select single drug pairs, groups of consecutive drug pairs, or a combination of both.

> **NOTE:** The following instructions are written for the screen that is non-compliant for Section 508. See Section 508 Compliant Drug Pair Customization Detail for instructions on how to use the compliant screen.

To select single drug pairs, simply select the corresponding checkboxes of the drug pairs to be selected.

<span id="_Toc403984478" class="anchor"></span>Figure 165: Drug Pair Selection List

![](pecs-version-6-2-user-guide/166.png)

To select groups of consecutive drug pairs, select the first checkbox in the group and then Shift + click (click while holding down the shift key) the last checkbox in the group. All drug pairs between the first and last checkboxes will be selected. If the user wants to add another group to their selection, then select the first checkbox in the second group and Shift + click the last checkbox in the group. Two groups of drug pairs will now be selected. To add other non-consecutive drug pairs, select the corresponding checkbox.

<span id="_Toc403984479" class="anchor"></span>Figure 166: Large Group of Selected Drug Pair for Batch Update

![](pecs-version-6-2-user-guide/167.png)

Drug Pairs from Routed Generic Drugs

To select multiple drug pairs from Routed Generic drugs:

1.  On the Drug Pair Customization window, select Drug pair from Routed Generic Drug lists from the Select Drug Pair(s) Source list.

<span id="_Toc75767363" class="anchor"></span>Figure 167: Select Drug Pairs Source List

![](pecs-version-6-2-user-guide/168.png)

148. Select Edit.
149. Enter all or part of a routed generic drug name in the Routed Generic 1 field. To display all routed generic drugs, enter \*. The list will populate automatically, but the process may take some time based on server load and the specificity of the search term.
150. Enter all or part of a routed generic drug name in the Routed Generic 2 field. To display all routed generic drugs, enter \*. The list will populate automatically, but the process may take some time based on server load and the specificity of the search term.
151. To select a range of routed generic drugs from the results list, select the first item in the range, then Shift + click the last item in the range. Use the scroll bar on the results list if the last item in the range is not immediately visible.

<span id="_Toc75767364" class="anchor"></span>Figure 168: Range Selection of Routed Generic Drugs

![](pecs-version-6-2-user-guide/169.png)

152. To select non-consecutive items in the results list, select the first item, then Ctrl + click (click while holding down the Ctrl key) any additional items. Use the scroll bar on the results list if the last item in the range is not immediately visible. This technique can also be used to de-select items within a previously selected range of items.

<span id="_Toc75767365" class="anchor"></span>Figure 169: Individual Selection of Routed Generic Drugs

![](pecs-version-6-2-user-guide/170.png)

153. Select the Customize button. After processing, the new drug pairs will appear in the Drug Pairs list. In this example, six new drug pairs were created: each of the three selected Routed Generic 1 drugs is now paired with the two selected Routed Generic 2 drugs.

<span id="_Toc75767366" class="anchor"></span>Figure 170: Drug Pairs List Selection List

![](pecs-version-6-2-user-guide/171.png)

<span id="_Toc75767367" class="anchor"></span>Figure 171: Drug Pairs List

![](pecs-version-6-2-user-guide/172.png)

Batch Update Drug Pairs

A user can use the quick selection processes described above to change the actions status of multiple drug pairs at the same time. The Action buttons available are dependent upon the action status of the selected drug pairs. Only mutually appropriate actions will be available.

### Review a Drug Pair

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Approver may be assigned to review drug pairs associated with a drug-drug interaction. The options are to either Submit as Reviewed, indicating that the Drug Pair associated with the drug-drug interaction is appropriate, or Reject the Drug Pair as inappropriately associated with the Drug-Drug interaction.

To review a drug pair associated with an interaction customization:

1.  From the Drug-Drug Interaction record, select Drug Pairs.

<span id="_Toc75767368" class="anchor"></span>Figure 172: Drug Pairs Button

![](pecs-version-6-2-user-guide/173.png)

154. When the Drug Pair Customization page appears, select Edit.

<span id="_Toc75767369" class="anchor"></span>Figure 173: Edit Button on the Drug Pair Customization Page

![](pecs-version-6-2-user-guide/174.png)

155. In the Drug Pairs panel, select one or more drug pairs currently associated with the drug-drug interaction. For information on selecting multiple items within a list, see Customizing Drug Pairs from the Selection List.

<span id="_Toc75767370" class="anchor"></span>Figure 174: Drug Panel for Selecting Drug Pairs

![](pecs-version-6-2-user-guide/175.png)

156. Using the Assigned To list, select the person to Approve the drug pair association with the selected drug-drug interaction. If unsure who this should be, then select Unassigned.

<span id="_Toc75767371" class="anchor"></span>Figure 175: Assigned To List

![](pecs-version-6-2-user-guide/176.png)

157. Select Submit as Reviewed to indicate that the drug pair has been reviewed and confirm that it is correctly associated with the selected drug-drug interaction. Select Reject to indicate that the drug pair is not correctly associated with the selected drug-drug interaction -- this will remove the drug pair from the record. Select Cancel Edit to abandon the current editing session and leave the record unchanged.

<span id="_Toc75767372" class="anchor"></span>Figure 176: Buttons Available to Choose From

![](pecs-version-6-2-user-guide/177.png)

> **NOTE:** Drug Pair records can be modified after they have been Reviewed.

## Section 508 Compliant Drug Pair Customization Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** These are the instructions for the Section 508 compliant version of the Drug Pair Customization page. For Non-compliant Drug Pair customization, see Drug Pair Customization (Non 508-Compliant) Detail.

To reach the Section 508-Compliant version of the Drug Pair Customization page:

1.  Select the "Drug Pairs" button on a VA customized Drug-Drug interaction detail page.
158. Select the 508-Compliant Page link in the Drug Pair Customization banner.

<span id="_Toc403984480" class="anchor"></span>Figure 177: Link to Access 508-Compliant Drug Pair Selection Page

![](pecs-version-6-2-user-guide/178.png)

### Select Drug Pairs to Add to the Above VA Custom Interaction Panel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are instructions on how to select drug pairs on the Section 508 Compliant Drug Pair Customization page.

Add Routed Generic to VA Custom Interaction

If the interaction is customized from a blank form, then there are no FDB drug pairs to choose from. The user will choose drug pairs from Routed Generic drug lists. The user will select the first drug "Routed Generic \#1 Description" and then select the second drug "Routed Generic \#2 Description" for the Drug Pair they are associating to this VA customized Drug-Drug Interaction. Note that a drug pair must be chosen before selecting the "Customize button". "Routed Generic \#1" and "Routed Generic \#2" fields cannot contain the same chosen value. "'Routed Generic \#1" and "Routed Generic \#2"' must follow the same order as the Interaction Description. The user must be careful to select all routed generics that contain the desired drug as an ingredient. Combination products may not fall alphabetically close to single ingredient products. The Routed Generic drug lists can also be used to add drug pairs to a drug-drug interaction customized from an FDB record if the drug pairs to be added do not exist in the FDB database.

<span id="_Toc403984481" class="anchor"></span>Figure 178: Routed Generic Drug List on 508-Compliant Page

![](pecs-version-6-2-user-guide/179.png)

To add a Routed Generic drug pair:

1.  Select the Edit button.
159. In the "Select Generic Drug Pairs to add to the above VA Custom Interaction" panel, select the first drug from the Routed Generic \#1 Description list.
160. Select the second drug from the Routed Generic \#2 Description list.
161. Add any available reference text to the Reference Text field. This is not required.
162. Add a reason for the current action in the Action Reason field. This is required.
163. Select a PECS user to review the action in the Action Reason field.
164. Select the Customize button.

Add FDB Drug Pairs to VA Custom Interaction

If the interaction is customized from an FDB record, the user can select any or all of the corresponding FDB drug pairs. Each FDB drug pair consists of Routed Generic \#1 and Routed Generic \#2. Select the checkbox adjacent to the drug pair or pairs to select it to add to the custom interaction.

<span id="_Toc403984482" class="anchor"></span>Figure 179: Corresponding FDB Drug Pairs, 508-Compliant Page Top

![](pecs-version-6-2-user-guide/180.png)

<span id="_Toc75767376" class="anchor"></span>Figure 180: Corresponding FDB Drug Pairs, 508-Compliant Page Bottom

![](pecs-version-6-2-user-guide/181.png)

To add a FDB drug pair:

1.  Select the Edit button.
165. In the "Select FDB Drug Pairs to add to the above VA Custom Interaction" panel, select the check box adjacent to the drug pair to be added to the customization. Users can select more than one drug pair. To select all the drug pairs, select the 'Select/Deselect All Drug Pairs Displayed from Corresponding FDB Interaction' check box, and to limit the number selected, select one of the number-specific radio buttons.
166. Add any available reference text to the Reference Text field. This is not required.
167. Add a reason for the current action in the Action Reason field. This is required.
168. Select a PECS user to review the action in the Action Reason field.
169. Select the Customize button.

Drug Pairs Panel

The Drug Pairs panel contains all the VA Customized Drug Pairs already associated to the VA Customized Drug-Drug Interaction (noted at the top of the page). The panel contains:

- Interaction Description - VA Customized Drug-Drug Interaction Description
- Routed Generic \#1 Description - First drug in the drug pair
- Routed Generic \#2 Description - Second drug in the drug pair
- Action Status - current status of the Drug Pair
- Request Submitted By - User ID of the PECS user who made the initial customization request
- Action Date - The date of the most recent action
- Action Performed By - User ID of the PECS user who performed the most recent action
- Request Assigned To - User ID of the PECS user who is responsible for reviewing the drug pair information
- Interaction ID - The numerical identifier for the Drug-Drug Interaction
- Severity Level Description - A text description of the interaction severity
- Reference Text - Contents of the Reference Text field
- Severity Level Code - A numerical identifier for the severity of the Drug-Drug Interaction

The checkboxes at the top allow the user to see what is displayed in the interaction table by Action Status (Historical records are not displayed). The drug pairs must be in the same state before an action can be performed on them.

<span id="_Toc403984483" class="anchor"></span>Figure 181: Drug Pair List Filters

![](pecs-version-6-2-user-guide/182.png)

The 'Get Record Counts' button will display the count of all VA customized drug pairs associated with the Drug-Drug Interaction. This helps to determine how many drug pairs require processing. It is recommended that no more than 200 drug pairs are processed at a time to prevent negative impacts to system performance.

To perform a batch update on the drug pairs:

1.  Use the Action Status checkbox filters to make sure all drug pairs selected are in the same Action Statuses
170. Select the amount that will be updated in this one action
171. Select all or the individual drug pairs
172. Select the allowed Approval Workflow action to be performed (Submit as Reviewed, Approve, Reject, etc.)

Repeat this process for all of the drug pairs until the entire set of drug pairs is in the desired point in the Approval Workflow.

## Professional Monograph Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Professional Monograph is a document containing drug interaction information written for healthcare professionals. The Professional Monograph Detail Page allows the user to view the details of a Professional Monograph and customize it for VA use.

FDB monographs are not generally customized, however some Professional Monographs have been created from blank documents at the national level for drug interactions that do not appear in the FDB database.

<span id="_Toc403984484" class="anchor"></span>Figure 182: Professional Monograph Detail Top

![](pecs-version-6-2-user-guide/183.png)

<span id="_Toc75767379" class="anchor"></span>Figure 183: Professional Monograph Detail Bottom

![](pecs-version-6-2-user-guide/184.png)

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fields that cannot be modified are shaded within PECS.

<table>
<caption><p><span id="_Toc75767184" class="anchor"></span>Table 17: Professional Monograph Buttons</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Field Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Monograph Title</td>
<td>The title Monograph is usually the two drugs that have the interaction.</td>
</tr>
<tr class="even">
<td>Monograph ID</td>
<td>The VA-assigned numerical identifier for the Monograph.</td>
</tr>
<tr class="odd">
<td>Action Status</td>
<td>Applicable to VA record only. The point this customization is at, within the VA Approval Workflow.</td>
</tr>
<tr class="even">
<td>Action Date</td>
<td>Applicable to VA record only. The date of the last action taken on the record.</td>
</tr>
<tr class="odd">
<td>Action Performed by</td>
<td>Applicable to VA record only. The name of the user that performed the last action.</td>
</tr>
<tr class="even">
<td>Action Effective Date</td>
<td>Applicable to VA record only. The date of the last action taken on the record.</td>
</tr>
<tr class="odd">
<td>Corresponding FDB Monograph ID</td>
<td>The First Databank (FDB)-assigned numerical identifier for the Monograph.</td>
</tr>
<tr class="even">
<td>Request Assigned To</td>
<td>Applicable to VA record only. Approver the request is assigned to.</td>
</tr>
<tr class="odd">
<td>Request Submitted By</td>
<td>Applicable to VA record only. The name of the user that submitted this VA request.</td>
</tr>
<tr class="even">
<td>Severity Level</td>
<td>The severity level associated with the interaction.</td>
</tr>
<tr class="odd">
<td>Mechanism Of Action</td>
<td><p>The specific biochemical interaction through which a drug interaction occurs. For instance, pharmacokinetic drug interactions may include:</p>
<ul>
<li><p>Inhibition of absorption</p></li>
<li><p>Enzyme inhibition increasing the risk of toxicity</p></li>
<li><p>Enzyme inhibitors resulting in reduced drug effect</p></li>
<li><p>Enzyme induction resulting in reduced effect</p></li>
<li><p>Enzyme induction resulting in toxic metabolites</p></li>
<li><p>Altered renal elimination</p></li>
</ul>
<p>Pharmacodynamic drug interactions include:</p>
<ul>
<li><p>Additive effects</p></li>
<li><p>Antagonistic pharmacodynamic effects</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Clinical Effects (required)</td>
<td>The Clinical effects associated with the interaction.</td>
</tr>
<tr class="odd">
<td>Predisposing Factors (optional)</td>
<td>The factors or conditions that render an individual vulnerable to a drug interaction?</td>
</tr>
<tr class="even">
<td>Patient Management (optional)</td>
<td>Describe the management options available to the provider, for example, Discontinuation of the medication, increased monitoring, laboratory tests, and scheduling the medication at different times</td>
</tr>
<tr class="odd">
<td>Discussion</td>
<td>Usually case reports or discussion.</td>
</tr>
<tr class="even">
<td>Reference</td>
<td>Cited reference information.</td>
</tr>
<tr class="odd">
<td>Disclaimer</td>
<td>Textual reminder that the information provided is not intended to replace the user's clinical judgment.</td>
</tr>
<tr class="even">
<td>Reference Text</td>
<td>Applicable to VA record only. Field for the user to enter any reference text needed to support customization of the Professional Monograph.</td>
</tr>
<tr class="odd">
<td>Action Reason History</td>
<td>Applicable to VA record only. All historical current action reason comments for this record, in one viewable field.</td>
</tr>
<tr class="even">
<td>Current Action Reason</td>
<td>Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization.</td>
</tr>
<tr class="odd">
<td>Export Date</td>
<td>For Approved or Deleted records. Indicates the date of the last Custom Update. See <u>Export Date</u> for additional information.</td>
</tr>
</tbody>
</table>

<span id="_Toc75767184" class="anchor"></span>Table 17: Professional Monograph Buttons

### Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Button Name | Field Description                                      |
|-------------|--------------------------------------------------------|
| Print Page  | Allows the user to print the page being viewed.        |
| History     | Allows the user to open the history of changes report. |
| Comment     | Add a pre-customization comment (FDB Only)             |

<span id="_Toc75767185" class="anchor"></span>Table 18: Forward and Reverse Professional Monograph Pairs

### Forward and Reverse Professional Monograph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single VA Custom Drug-Drug Interaction could be associated with a separate custom Professional Monograph for the forward and reverse interactions. An interaction described as Drug A and Drug B would have a different Custom Monograph from an interaction described as Drug B and Drug A. These different monographs may be necessary because there could be a different Clinical Effect Code between forward and reverse interactions (DrugA+DrugB: Clinical Effect Code = Adverse effects of the former drug; DrugB+DrugA: Clinical Effect Code = Adverse effects of the latter drug).

The following VA Custom Professional Monograph pairs will be associated with each other. This means that when a Monograph is assigned to a VA Custom Drug-Drug Interaction, the corresponding Monograph will be automatically assigned to the reverse Drug-Drug Interaction (DDI1 = DrugA + DrugB; DDI2 = DrugB+DrugA).

Below is a list of the monograph IDs and titles, and the paired Monograph ID and title.

| Monograph ID and Title                                                        | Paired Monograph ID and Title                                                 |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 150022 VA Customized: Adverse Effects of Former Drug (Critical) (ARF1)        | 150024 VA Customized: Adverse Effects of Latter Drug (Critical) (ARL1)        |
| 150023 VA Customized: Adverse Effects of the Former Drug (Significant) (ARF2) | 150025 VA Customized: Adverse Effects of the Latter Drug (Significant) (ARL2) |
| 150030 VA Customized: Decreased Effects (Critical) (DEF1)                     | 150032 VA Customized: Decreased Effects (Critical) (DEL1)                     |
| 150031 VA Customized: Decreased Effects (Significant) (DEF2)                  | 150033 VA Customized: Decreased Effects (Significant) (DEL2)                  |
| 150034 VA Customized: Increased Effects (Critical) (INF1)                     | 150036 VA Customized: Increased Effects (Critical) (INL1)                     |
| 150035 VA Customized: Increased Effects (Significant) (INF2)                  | 150037 VA Customized: Increased Effects (Significant) (INL2)                  |
| 150040 VA Customized: Mixed Effects of Former Drug (Critical) (MXF1)          | 150103 VA Customized: Mixed Effects of Latter Drug (Critical) (MXL1)          |
| 150041 VA Customized: Mixed Effects of the Former Drug (Significant) (MXF2)   | 150104 VA Customized: Mixed Effects of the Latter Drug (Significant) (MXL2)   |

<span id="_Toc75767186" class="anchor"></span>Table 19: Duplicate Therapy Detail Fields

When viewing a Drug-Drug Interaction, the PECS user interface will only display the Professional Monograph associated with the Forward interaction. The associated Reverse Professional Monograph will only be visible in the custom updates file created by the Release Manager.

<span id="_Toc403984486" class="anchor"></span>Figure 184: Forward/Reverse DDIs with Professional Monographs, Custom Update File Created by Release Manager

![](pecs-version-6-2-user-guide/185.png)

## Duplicate Therapy Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duplicate Therapy Detail page allows the user to view and edit the details of a Duplicate Therapy record. If an FDB record is edited, then the result is a VA Customization Request. For FDB records that have not been customized, the user has the option of adding a comment that will be retained with the record. If the record is later customized, then these pre-customization comments will be displayed with the customized record. Once the FDB record has been customized, a link to the VA customized record will be provided. FDB Duplicate Therapy records can be customized only once. If the record has already been customized, then it displays in Read-only mode, and it will not be customizable again (the Edit button will not display).

<span id="_Toc75767381" class="anchor"></span>Figure 185: Duplicate Therapy Detail

![](pecs-version-6-2-user-guide/186.png)

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field Name            | Field Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DTCID                 | Duplicate therapy ID assigned by First Databank (FDB).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Custom Dup Allowance  | The number of drugs a patient can be prescribed, within a Therapeutic Drug Class, before an alert is generated. A 0 duplicate allowance means only 1 medication from that Therapeutic class can be on the patient profile without getting an order check (zero duplication). If a second drug from that class is added the provider gets the order check. If the allowance is 1, two drugs can be on the patient profile at once, the 3rd drug added would get the check (one duplication), etc. |
| Description           | The name of this Therapeutic Drug Class.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Action Status         | Applicable to VA record only. The point this customization is at, within the VA Approval Workflow.                                                                                                                                                                                                                                                                                                                                                                                               |
| Action Date           | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Export Date           | For Approved or Deleted records. Indicates the date of the last Custom Update. See Export Date for additional information.                                                                                                                                                                                                                                                                                                                                                                       |
| Action Effective Date | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Action Performed By   | Applicable to VA record only. The name of the user that performed the last action.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Request Assigned To   | Applicable to VA record only. A drop down list to assign an approver.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Request Submitted By  | Applicable to VA record only. The name of the user that submitted this VA request.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Action Reason History | Applicable to VA record only. All historical current action reason comments for this record, in one viewable field.                                                                                                                                                                                                                                                                                                                                                                              |
| Reference text        | Field for the user to enter any reference text needed to support customization of the Duplicate Allowance.                                                                                                                                                                                                                                                                                                                                                                                       |
| Current Action Reason | Applicable to VA record only. Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization.                                                                                                                                                                                                                                                                        |

<span id="_Toc75767187" class="anchor"></span>Table 20: Duplicate Therapy Detail Buttons

### Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Button Name | Field Description                                                                  |
|-------------|------------------------------------------------------------------------------------|
| Print Page  | Allows the user to print the page being viewed.                                    |
| History     | Allows the user to open the history of changes report.                             |
| Comment     | Un-customized FDB Records Only: Add a Pre-Customization comment to the FDB record. |

<span id="_Toc75767188" class="anchor"></span>Table 21: Dose Range Detail Fields

## Dose Range Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Dose Range is the allowable dosage of a drug based on a number of factors such as patient age, weight, and Dose Route. The Dose Range Detail page allows the user to view the details of a Dose Range record. If the FDB record is Concept Type 6 (Generic Dispensable Drug), then it can be customized. For FDB records of concept type other than 6, the only action that can be taken is to add a comment. Once the FDB record has been customized, a link to the VA customized record (or records) will be provided. For VA records, a link to the original FDB record (if one exists) is provided as well as any additional customizations to the same FDB record.

<span id="_Toc75767382" class="anchor"></span>Figure 186: Dose Range Detail Top

![](pecs-version-6-2-user-guide/187.png)

<span id="_Toc75767383" class="anchor"></span>Figure 187: Dose Range Detail Bottom

![](pecs-version-6-2-user-guide/188.png)

### Dose Range Concept Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FDB Dose Range records can be associated to different drug Concept Types (a type associated in the FDB drug database that PECS uses). However, only Concept Type 6 - Generic Dispensable Drug can be customized. The Concept Types are:

> 1 -- Drug Name

> 2 -- Routed Drug

> 3 -- Dispensable Drug

> 4 -- Generic Drug Name

> 5 -- Generic Routed Drug

> 6 -- Generic Dispensable Drug

> 7 -- Routed Dosage Form Drug

> 8 -- Generic Routed Dosage Form Drug

> 100 -- Packaged Drug

> 101 -- Manufactured Drug

> 102 -- Reference Only Item

> 103 -- Compound

> 104 -- Ingredient

> 105 -- Regional Packaged Drug

> 106 -- Total Parenteral Nutrition Solution

### Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field                           | Description                                                                                                                                                                                                              |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Concept Type                    | Number identifying the drug's concept type (FDB dose range category)                                                                                                                                                     |
| Concept ID Number               | Number identifying the drug (For Concept Type = 6, Concept ID number = GCNSEQ code - an FDB product code)                                                                                                                |
| Concept ID Description          | The name of the drug being described.                                                                                                                                                                                    |
| Action Status                   | Applicable to VA record only. The point this customization is at, within the VA Approval Workflow.                                                                                                                       |
| Age Low in Days                 | Lowest patient age in days to which dosing information applies                                                                                                                                                           |
| Age High in Days                | Highest patient age in days to which dosing information applies                                                                                                                                                          |
| Action Effective Date           | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                           |
| Dose Route                      | Dose route                                                                                                                                                                                                               |
| Dose Type                       | Dose type                                                                                                                                                                                                                |
| FDBDX                           | A nine-character alphanumeric coding system developed by First DataBank that identifies specific disease states or side effects.                                                                                         |
| DXID                            | DXID type code to identify a Medical Condition                                                                                                                                                                           |
| Dose Low                        | Minimum amount to be administered per day                                                                                                                                                                                |
| Dose Low Units                  | Unit of measure for low dose per day                                                                                                                                                                                     |
| Dose High                       | Highest amount to be administered per day                                                                                                                                                                                |
| Dose High Units                 | Unit of measure for high dose per day                                                                                                                                                                                    |
| Dose Form Low                   | Low dose for a given dose form                                                                                                                                                                                           |
| Dose Form Low Units             | Unit of measure for the dose form                                                                                                                                                                                        |
| Dose Form High                  | High dose for a given dose form                                                                                                                                                                                          |
| Dose Form High Units            | Unit of measure for the dose form                                                                                                                                                                                        |
| Frequency Low                   | Indicates the low end of a drug's frequency of administration per day                                                                                                                                                    |
| Frequency High                  | Indicates the high end of a drug's frequency of administration per day                                                                                                                                                   |
| Duration Low                    | Indicates the lowest recommended duration of therapy (in days)                                                                                                                                                           |
| Duration High                   | Indicates the highest recommended duration of therapy (in days)                                                                                                                                                          |
| Max Duration                    | Indicates the maximum recommended duration of therapy (in days)                                                                                                                                                          |
| Max Single Dose                 | Maximum amount to be administered in a single dose                                                                                                                                                                       |
| Max Single Dose Units           | Unit of measure for the maximum single dose                                                                                                                                                                              |
| Max Single Dose Form            | Maximum single dose for a given form                                                                                                                                                                                     |
| Max Single Dose Form Units      | Unit of measure for the dose form                                                                                                                                                                                        |
| Max Daily Dose                  | Maximum amount to be administered per day                                                                                                                                                                                |
| Max Daily Dose Units            | Unit of measure for the maximum daily dose                                                                                                                                                                               |
| Max Daily Dose Form             | Maximum daily dose for a dose form                                                                                                                                                                                       |
| Max Daily Dose Form Units       | Unit of measure for the dose form                                                                                                                                                                                        |
| Max Lifetime Dose               | Maximum amount to be administered over a patient's lifetime, if available                                                                                                                                                |
| Max Life Time Dose Units        | Unit of measure for maximum lifetime dose                                                                                                                                                                                |
| Max LifeTime Dose Form          | Maximum lifetime dose for a given dose form                                                                                                                                                                              |
| Max LifeTime Dose Form Units    | Unit of measure for the dose form                                                                                                                                                                                        |
| Dose Rate Low                   | Minimum amount to be administered per dose rate (hours or minutes)                                                                                                                                                       |
| Dose Rate Low Units             | Unit of measure for low dose rate (hours or minutes)                                                                                                                                                                     |
| Dose Rate High                  | Highest amount to be administered per dose rate (hours or minutes)                                                                                                                                                       |
| Dose Rate High Units            | Unit of measure for high dose rate (hours or minutes)                                                                                                                                                                    |
| Dose Form Rate Low              | Low dose for a given dose form rate (hours or minutes)                                                                                                                                                                   |
| Dose Form Rate Low Units        | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                |
| Dose Form Rate High             | High dose for a given dose form rate (hours or minutes)                                                                                                                                                                  |
| Dose Form Rate High Units       | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                |
| Max Single Dose Rate            | Maximum amount to be administered in a single dose rate (hours or minutes)                                                                                                                                               |
| Max Single Dose Rate Units      | Unit of measure for the maximum single dose rate (hours or minutes)                                                                                                                                                      |
| Max Single Dose Form Rate       | Maximum single dose for a given dose form rate (hours or minutes)                                                                                                                                                        |
| Max Single Dose Form Rate Units | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                |
| Max Daily Dose Rate             | Maximum amount to be administered per dose rate (hours or minutes)                                                                                                                                                       |
| Max Daily Dose Rate Units       | Unit of measure for the maximum daily dose rate (hours or minutes)                                                                                                                                                       |
| Max Daily Dose Form Rate        | Maximum daily dose for a dose form rate (hours or minutes)                                                                                                                                                               |
| Max Daily Dose Form Rate Units  | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                |
| Hepatic Impairment IND          | Boolean (0/1) indicating whether dosing needs to be adjusted for hepatic impairment                                                                                                                                      |
| Renal Impairment IND            | Boolean (0/1) indicating whether dosing needs to be adjusted for renal impairment                                                                                                                                        |
| CRCL Threshold                  | Number indicating lowest creatinine clearance to which dosing applies                                                                                                                                                    |
| CRCL Threshold Units            | Unit of measure for the creatinine clearance threshold                                                                                                                                                                   |
| Low Elimination Half Life       | Indicates the low end of the drug's half-life range                                                                                                                                                                      |
| High Elimination Half Life      | Indicates the high end of the drug's half-life range                                                                                                                                                                     |
| Half Life Units                 | Unit of time for the half-life range of a drug                                                                                                                                                                           |
| Weight Required IND             | Boolean (0/1) indicating whether weight is required for dosing                                                                                                                                                           |
| BSA Required IND                | Boolean (0/1) indicating whether body surface area is required for dosing                                                                                                                                                |
| Request Submitted By            | Applicable to VA record only. The name of the user that submitted this VA request.                                                                                                                                       |
| Request Assigned To             | Applicable to VA record only. A drop down list to assign an approver.                                                                                                                                                    |
| Action Performed By             | Applicable to VA record only. The name of the user that performed the last action.                                                                                                                                       |
| Action Date                     | Applicable to VA record only. The date of the last action taken on the record.                                                                                                                                           |
| Export Date                     | For Approved or Deleted records. Indicates the date of the last Custom Update. See Export Date for additional information.                                                                                               |
| Reference Text                  | Applicable to VA record only. Field for the user to enter any reference text needed to support customization of this Dose Range.                                                                                         |
| Action Reason History           | Applicable to VA record only. All historical 'current action reason' comments for this record, in one viewable field.                                                                                                    |
| Current Action Reason           | Applicable to VA record only Free form text that can be used to specify the reason for taking the specific action of creating new, modifying, assigning, rejecting, reviewing, approving, or deleting the customization. |

<span id="_Toc75767189" class="anchor"></span>Table 22: Dose Range Detail Buttons

### Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Button Name | Field Description                                      |
|-------------|--------------------------------------------------------|
| Print Page  | Allows the user to print the page being viewed.        |
| History     | Allows the user to open the history of changes report. |
| Comment     | Add a Pre-Customization comment (FDB Only).            |

<span id="_Toc75767190" class="anchor"></span>Table 23: FDB Comparison Drug-Drug Interaction/Drug Pair Report Fields

# Sample Modification Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following scenarios are examples of the types of modifications a typical user may perform. It is not a step-by-step guide in instructing users how to perform actual modifications. Sample steps are given, but these could differ based on the customizations being modified.

## Duplicate Therapy Modification 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample case: Making a Duplicate Therapy customization for Topical Pine Tar.

### Process Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit duplicate therapy allowance:

1.  From the Home Page, select the Advanced Query/Customization tab.
173. Select "Duplicate Therapy" from the *Select a Concept* drop-down and select 'FDB' from the *Select VA, FDB, or Both* drop-down
174. Build the query as follows: Fields=Description; Filter=contains; Value=Tar.
175. Select the Query button.
176. Look at the query results at the bottom of the page.
177. Select the Open link for the desired class of drug.
178. The following is displayed:

<span id="_Toc75767384" class="anchor"></span>Figure 188: Duplicate Therapy Modification

![](pecs-version-6-2-user-guide/189.png)

179. Select the Edit button to edit the record.
180. Select the drop down arrow on Custom Dup Allowance (required) and select another number.
181. Enter a Description (required).
182. Enter the Current Action Reason (required).
183. Add any reference text needed (optional).
184. Select the Customize button.

## Duplicate Therapy Approval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: After the duplication allowance has been edited for the above situation, the user needs to submit the request for approval. Assign this request to FOUR_APPROVER.

### Process Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Home page, look at My Request History.
2.  Select the link to the NEW Duplicate Therapy requests.
3.  Look at the query results at the bottom of the page.
4.  Select the link for the desired class of drug (Topical Pine Tar).
5.  Review the information.
6.  Select the Edit button to edit the record.
7.  Select the next business reviewer's name in Request Assigned To (optional) field.
8.  Indicate the action reason in Current Action Reason (optional) field.
9.  Select the Submit As Reviewed button.

## Drug Interaction Research

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: The chief of urology has been told by the Pfizer sales rep that the VA has no drug-drug interaction between Sildenafil and Tamsulosin. The chief insists that a significant (severity level 2) interaction be added to the system.

### Process Steps for Severity Check, Case 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check severity of an existing drug-drug interaction.

1.  From the Home page, Select the Drug Pair Lookup tab.
185. Fill in known information (Drug A: Sildenafil; Drug B: Tamsulosin).
186. Select the Query button.
187. Review the VA custom records and FDB record.
188. Note existing VA custom interaction between Sildenafil and Tamsulosin with severity level 2 and FDB interaction with severity level 3.
189. No action needed.

## Drug Interaction Severity Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: The FDA recently issued a black box warning stating that Cyclosporine and Tolterodine should never be used together due to risk of renal toxicity. This interaction is considered severity level 3 (moderate) by First Data Bank. Based on the issuance of this black box warning, the NDF support group is recommending the severity level be changed to 1 (critical). Create custom drug-drug pairs for this new VA custom drug-drug interaction.

### Process Steps for Editing Case 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the severity of an existing FDB drug interaction

1.  From Home page, choose the Advanced Query/Customization tab.
190. Select "Drug-Drug Interaction" from the *Select a Concept* drop-down and select 'FDB' from the *Select VA, FDB, or Both* drop-down.
191. Build the Query: Fields=Interaction Description; Filter=contains; Value=Cyclosporine; And/Or=Or.
192. Build Query: Column=Interaction Description; Constraints=contains; Value=Tolterodine.
193. Select the Query button.
194. Look at the query results at the bottom of the page.
195. Select the Open link for desired Interaction Description.
196. Select the Edit button to edit the record.
197. Select the drop down arrow on Severity Level Code (required).
198. Select the new desired severity level code (1).
199. Indicate the action reason in the free text Current Action Reason (required) field.
200. Select the Customize button.
201. Select Drug Pairs button.
202. Select the Edit button to edit the Drug Pairs.
203. If the section is not expanded, select the plus sign on Select Drug Pairs to add to the above VA Custom interaction bar.
204. If the radio button is not selected, select the radio button for "Drug Pairs from Corresponding FDB Interaction."
205. Select desired drug pairs to add to the custom interaction.
206. Indicate the action reason in the free text Current Action Reason (required) field.
207. Select the Customize button.

To Submit as Reviewed:

1.  From the home page, look at My Request History.
208. Select the NEW Drug-Drug Interactions link.
209. Look at the query results at the bottom of the page.
210. Select the link for the desired interaction description (Tolterodine/Cyclosporine).
211. Select the Drug Pairs button.
212. Select the Edit button.
213. Scroll down to Drug Pairs section, and select the newly added Drug Pair
214. Select the Submit as Reviewed button.
215. Select the link at the top of the page for the VA interaction
216. Select the Edit button.
217. Review the information.
218. Indicate the Action Reason in the free text Current Action Reason (required) field.
219. Select the Submit as Reviewed button.

## Drug Interaction Severity Change 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: Over the past six months, several local VA facilities have reported adverse reactions (ADRs) involving the use of Digoxin and Metoclopramide resulting in Digoxin toxicity requiring hospital admissions for management. This interaction is classified as severity level 3 (moderate) by FDB and therefore does not create an alert in the physician order entry process. The NDF support group has approved the change of the severity level from 3 to 2 (severe) to provide for order alerts and has assigned the task to be completed. Create custom drug-drug pairs for this new VA custom drug-drug interaction. Then submit the new interaction and drug pairs as reviewed.

### Process Steps for Editing Case 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the severity of an existing FDB drug interaction

1.  From the Home page, choose the Advanced Query/Customization tab.
2.  Select "Drug-Drug Interaction" from the Select a Concept drop-down and select 'FDB' from the Select VA, FDB, or Both drop-down.
3.  Build the Query: Fields=Interaction Description; Filter=contains; Value=Digoxin; And/Or=And.
4.  Build the Query: Fields=Interaction Description; Filter=contains; Value=Metoclopramide.
5.  Select the Query button.
6.  Look at the query results at the bottom of the page.
7.  Select the Active link for the desired Interaction Description.
8.  Select the Edit button.
9.  Select the drop down arrow on Severity Level Code (required).
10. Select the desired new severity level code (2).
11. Indicate the action reason in the free text Current Action Reason (required) field.
12. Select the Customize button.
13. Select Drug Pairs button.
14. Select the Edit button.
15. If the section is not expanded, select the plus sign on Select Drug Pairs to add to the above VA Custom interaction bar.
16. If the radio button is not selected, select the radio button for 'drug pairs from corresponding FDB interaction.'
17. Select the checkbox for 'Select/Deselect all drug Pairs from corresponding FDB interaction.'
18. Indicate the action reason in the free text Current Action Reason (required) box
19. Select the Customize button.
20. From the Home page, look at My Request History.
21. Select the NEW Drug-Drug Interactions link.
22. Look at the query results at the bottom of the page.
23. Select on the Active link for the desired interaction description (digoxin/metoclopramide).
24. Select Drug Pairs button (Drug pairs should be submitted as reviewed prior to submitting the interaction for review)
25. Scroll to the Drug Pairs Bar
26. Select the Edit button
27. Select the checkbox for 'Select/Deselect All Drug Pairs Displayed from VA Custom Interaction'
28. Select the Submit as Reviewed button.
29. Select on the VA Interaction ID at top of page to navigate to Drug Interaction Detail page
30. Select the Submit as Reviewed button.

## Remove Drug Pair from Interaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: The user has been asked to remove the drug pair Sumatriptan Nasal/Tranylcypromine Sulfate Oral from the existing VA custom drug-drug interaction Selected 5HT-1D Agonists/MAO Inhibitors.

### Process Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remove or add a drug pair from an existing VA custom drug-drug interaction.

1.  Choose the Advanced Query/Customization tab.
220. Select "Drug-Drug Interaction" from the Select a Concept drop-down and select 'VA' from the Select VA, FDB, or Both drop-down.
221. Build the Query: Column=Interaction Description; Filter=contains; Value=Selected 5HT.
222. Select the Query button.
223. Look at the query results at the bottom of the page.
224. Select the Active link for the desired Interaction Description.
225. Select the Edit button.
226. Select the Drug Pairs button.
227. Select the Edit button to edit the drug pairs.
228. Select the plus sign on 'Drug Pairs' bar.
229. Select on the checkbox associated with Sumatriptan Nasal and Tranylcypromine Sulfate Oral.
230. Select the Submit for Delete button.
231. Alert another Approver that the drug pair needs to be deleted.

## Create Professional Monograph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample Case: Create a new VA custom monograph using the current FDB interaction monograph created for Cyclosporine and Tolterodine as the guide. Modify the FDB monograph severity level from level 3 to level 1 – contraindication.

### Process Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the Advanced Query/Customization tab.
2.  Select "Professional Monograph" from the Select a Concept drop-down and select 'FDB' from the Select VA, FDB, or Both drop-down.
3.  Build the Query: Column=Monograph Title; Filter=contains; Value=cyclosporine.
4.  Select OR from the And/Or drop-down.
5.  Build the Query: Column=Monograph Title; Filter=contains; Value=tolterodine.
6.  Select the Query button.
7.  Look at the results at the bottom of the page.
8.  Select the link for the desired monograph title in the FDB table results. The Monograph is displayed, as shown.

<span id="_Toc75767385" class="anchor"></span>Figure 189: Creating a Professional Monograph

![](pecs-version-6-2-user-guide/190.png)

232. Select the Edit button to edit the record.
233. Change the Severity level to 1 – Critical.
234. Indicate the action reason in the free text Current Action Reason (required) field.
235. Select the Customize button.

# Contact Us

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Contact Us page contains a list of PECS Project Contacts should the user need additional information about the PECS product. The content of the Contact Us page is created and maintained by users with the Administrator role. In many cases, a linked email address will be included. Select the link associated with the name to send that person (or group) an email.

> **NOTE:** Selecting the link opens the mail application and a new email message to the person specified in the properties of the link. This may produce a warning message. This is normal.

<span id="_Toc403984495" class="anchor"></span>Figure 190: Contact Us Example

![](pecs-version-6-2-user-guide/191.png)

PECS Administrators can edit the content of the Contact Us page. See Editing Contact Us for additional information.

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports page displays a list of available reports in PECS. PECS Reports are essentially exported Excel spreadsheets that can be manipulated and formatted as the user sees fit.

> **NOTE:** The Reports tab is not visible to Requestor or Release Manager users.

Note to Assistive Technology Users: Please refer the documentation included with the screen reader for commands related to reading column and row headers.

To run a report, select the link associated with it. The user will be provided the option of opening the file directly or saving a copy of the file to a location on their workstation (or accessible network location).

<span id="_Toc403984496" class="anchor"></span>Figure 191: List of Reports

![](pecs-version-6-2-user-guide/192.png)

There are two types of Reports:

1.  Active Customization Reports
236. FDB Comparison Reports

## Active Customization Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Active Customization Reports are:

- FDB Custom Dose Range Report
- FDB Custom Drug-Drug Interaction Report
- FDB Custom Duplicate Therapy Report
- FDB Custom Professional Monograph Report
- Deleted Monograph Customization Report
- Null Drug Pairs Customization Report

The first four Active Customization Reports, FDB Custom Dose Range, FDB Custom Drug-Drug Interaction, FDB Custom Duplicate Therapy, and FDB Custom Professional Monograph, display concept records in an Approved status along with their corresponding FDB record data. See the sample below.

<span id="_Toc403984497" class="anchor"></span>Figure 192: Sample Active Customization Report

![](pecs-version-6-2-user-guide/193.png)

The last two reports on the list, Deleted Monograph Customization Report and Null Drug Pairs Customization Report, look for problems. The Deleted Monograph Customization Report displays DDIs with an associated PM that has been deleted (e.g., the FDB update deleted an FDB PM, and that FDB PM is associated to a custom DDI). The Null Drug Pairs Customization Report displays custom DDIs that have an associated DP in which one or both routed generics is null because an FDB update deleted the routed generic(s).

### FDB Custom Dose Range Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Custom Dose Range Report contains active VA custom Dose Range records in an Approved status. The default file name is Dosing_Total_Customization_Report.xlsx.

To Run the FDB Custom Dose Range Report:

1.  Select the Reports tab on the PECS Application Window.
237. Select the FDB Custom Dose Range Report link.
238. Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on the workstation (or accessible network location). The file name is Dosing_Total_Customization_Report.xlsx.
239. If the user selected Open, then the report will automatically appear in the Excel application.

<span id="_Toc75767389" class="anchor"></span>Figure 193: Sample Custom Dose Range Report

![](pecs-version-6-2-user-guide/194.png)

### FDB Custom Drug-Drug Interaction Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Custom Drug-Drug Interaction Report contains active VA custom Drug-Drug interaction records in an Approved status along with their corresponding FDB record data.

To Run the FDB Custom Drug-Drug Interaction Report:

1.  Select the Reports tab on the PECS Application Window.
2.  Select the FDB Custom Drug-Drug Interaction Report link.
3.  Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on the workstation (or accessible network location). The file name is Ddiminteraction_Total_Customization_Report.xlsx.
4.  If the user selected Open, the report will automatically appear in the Excel application.

<span id="_Toc75767390" class="anchor"></span>Figure 194: Sample Custom DDI Report

![](pecs-version-6-2-user-guide/195.png)

### FDB Custom Duplicate Therapy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Custom Duplicate Therapy Report contains active VA custom Duplicate Therapy records in an Approved status along with their corresponding FDB record data.

To run the FDB Custom Duplicate Therapy Report:

1.  Select the Reports tab on the PECS Application Window.
240. Select the FDB Custom Duplicate Therapy Report link.
241. Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on the workstation (or accessible network location). By default, the file name is Dtcat_Total_Customization_Report.xlsx.
242. If the user selected Open, the report will automatically appear in the Excel application.

<span id="_Toc75767391" class="anchor"></span>Figure 195: Sample Custom Duplicate Therapy Report

![](pecs-version-6-2-user-guide/196.png)

### FDB Custom Professional Monograph Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Custom Professional Monograph Report contains active VA custom Professional Monograph records in an Approved status along with their corresponding FDB record data.

To run the FDB Custom Professional Monograph Report:

1.  Click the Reports tab on the PECS Application Window.
2.  Click the FDB Custom Professional Monograph Report link.
3.  Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on your workstation (or accessible network location). By default, the file name is Monograph_Total_Customization_Report.xlsx.
4.  If you selected Open, the report will automatically appear in the Excel application.

<span id="_Toc75767392" class="anchor"></span>Figure 196: Sample Custom Professional Monograph Report

![](pecs-version-6-2-user-guide/197.png)

### Deleted Monograph Customization Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deleted Monograph Customization Report contains active VA custom Drug-Drug interaction records in an Approved status that are associated with a deleted FDB Professional Monograph.

To run the Deleted Monograph Customization Report:

1.  Click the Reports tab on the PECS Application Window.
2.  Click the Deleted Monograph Customization Report link.
3.  Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on your workstation (or accessible network location). By default, the file name is Deleted_Monograph_Report.xlsx.
4.  If you selected Open, the report will automatically appear in the Excel application.

<span id="_Toc75767393" class="anchor"></span>Figure 197: Sample Deleted Monograph Report

![](pecs-version-6-2-user-guide/198.png)

### Null Drug Pairs Customization Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Null Drug Pairs Customization Report contains approved VA custom Drug-Drug Interactions that contain Drug Pairs with null Routed Generic \#1 or Routed Generic \#2 fields. The report will not display drug pairs with Deleted status.

If this report contains any entries, then a user in the Administrator role should initiate the Null Drug Pair Removal Process, which deletes Null Drug Pairs listed on the report. After the Null Drug Pair Removal process is complete, the Administrator may want to run the report to verify that these drug pairs have been removed. The null Drug Pairs listed on this report are the ones that will be deleted during the Null Drug Pair Removal process.

To run the Null Drug Pairs Customization Report:

1.  Select the Reports tab on the PECS Application Window.
2.  Select the Null Drug Pairs Customization Report link.
3.  Select Open to view the exported file in Excel; select Save to save a copy of the file to a location on the workstation (or accessible network location). By default, the file name is Deleted_Monograph_Report.xlsx.
4.  If the user selected Open, the report will automatically appear in the Excel application.

<span id="_Toc75767394" class="anchor"></span>Figure 198: Sample Drug Pairs Customization Report

![](pecs-version-6-2-user-guide/199.png)

> **NOTE:** This report can be used to identify approved VA Drug-Drug Interactions that contain null Drug Pairs.

For more information, see the section Null Drug Pair Removal Process under Administrator.

## FDB Comparison Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Comparison Reports display the changes to existing data included in the Incremental FDB updates. The reports inform an Approver or Administrator of the latest FDB changes for the Duplicate Therapy, Drug-Drug Interaction, Drug Pair, and Dose Range concepts and provide data that helps the these users decide whether or not to change a custom record. The FDB Comparison Reports help an Approver or Administrator keep PECS customizations in sync with FDB changes.

FDB Comparison Reports display:

- Customized records in all action statuses that have differences between the PECS FDB data and the data in the Incremental FDB Update file.
- Un-customized records that have differences between the PECS FDB data and the data in the Incremental FDB Update file.
- Indications that an FDB record is scheduled to be deleted by DATUP.
- Lists of the drug pairs that will be added or deleted by DATUP.
- A "no data found" message if the Incremental FDB Update file has no changes to the FDB data.

Changed data is marked with an asterisk (\*) and colored red. The reports are organized by type and the date of the FDB Incremental Update.

<span id="_Toc403984498" class="anchor"></span>Figure 199: Changed Data in Report

![](pecs-version-6-2-user-guide/200.png)

To run an FDB Comparison report, select the appropriate date of an FDB Incremental Update under the appropriate Report Heading:

<span id="_Toc403984499" class="anchor"></span>Figure 200: FDB Incremental Update Date Samples

![](pecs-version-6-2-user-guide/201.png)

### FDB Comparison Drug-Drug Interaction/Drug Pair Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB Comparison Drug-Drug Interaction/Drug Pairs Report displays the changes to existing Drug-Drug Interactions included in the Incremental FDB updates. All Action Statuses are compared and are included in the report. The following data points are compared between the FDB update and the VA Drug-Drug Interaction records:

- Corresponding FDB Interaction ID
- Interaction Description
- Monograph ID
- Severity Level Code
- Clinical Effect 1
- Clinical Effect 2
- Deleted Drug Pairs
- Added Drug Pairs

The DDI-DP FDB Comparison Report contains two types of spreadsheets:

- The DDI-DP FDB Comparison Report – gives information about the FDB comparisons and the associated VA custom records.
- FDB Interaction ID-DP – gives information about the added or deleted drug pairs for a specific FDB record. Each FDB update record that has added or deleted drug pairs has its own FDB Interaction ID-DP spreadsheet.

The following DDI-specific fields are included in the DDI-FDB Comparison Report spreadsheet:

<table>
<caption><p><span id="_Toc75767191" class="anchor"></span>Table 24: FDB Comparison Drug-Drug Interaction/Drug Pair Report Fields</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA Interaction ID</td>
<td>A VA-assigned numerical identifier for the interaction.</td>
</tr>
<tr class="even">
<td>FDB Interaction ID</td>
<td>An FDB-assigned numerical identifier for the interaction.</td>
</tr>
<tr class="odd">
<td>Interaction Description</td>
<td>A text description of the interaction.</td>
</tr>
<tr class="even">
<td>Monograph ID</td>
<td>A numerical identifier for the Professional Monograph associated with the interaction.</td>
</tr>
<tr class="odd">
<td>Severity Level</td>
<td>A coded severity indicator.</td>
</tr>
<tr class="even">
<td>Clinical Effect 1</td>
<td>A three letter code describing the clinical effect.</td>
</tr>
<tr class="odd">
<td>Clinical Effect 2</td>
<td>A three letter code describing the clinical effect.</td>
</tr>
<tr class="even">
<td>Drug Pairs</td>
<td>If a DDI has drug pairs scheduled to be added or deleted by DATUP, then there will be a message, "See FDB Interaction ID &lt;FDB Interaction ID number&gt;-DP."<br />
If a DDI record in the incremental FDB update file does not have added or drug pairs, then this column will remain blank.</td>
</tr>
</tbody>
</table>

<span id="_Toc75767191" class="anchor"></span>Table 24: FDB Comparison Drug-Drug Interaction/Drug Pair Report Fields

If the latest FDB update contains added or deleted drug pairs, then these will be displayed on separate tabs titled "FDB Interaction ID \<FDB Interaction ID number\>-DP".

Each record consists of at least three lines and individual records are by a blank row (blue). There will be more than three lines if there is more than one VA Customization for the described interaction.

<span id="_Toc403984503" class="anchor"></span>Figure 201: DDI-DP FDB Comparison Report

![](pecs-version-6-2-user-guide/202.png)

- VA Custom - Custom VA information about the Drug-Drug Interaction record(s). If the DDI has not been customized, the record will state "Not customized".
- Latest FDB - Indicates changes to the Drug-Drug Interaction record that appeared on the incremental FDB update the user selected.
- Previous FDB - Displays the value for the Drug-Drug Interaction record in the incremental FDB update immediately prior to the incremental FDB update the user selected.

The following fields are included in the report:

| Field                   | Description                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------|
| Action Status           | The current state of the record based on the most recent action performed on the associated record. |
| Action Date             | The date the current action (Action Status) was performed.                                          |
| DATUP will delete       | YES in this column Indicates the associated record will be deleted by DATUP.                        |
| VA Interaction ID       | A VA-assigned numerical identifier for the interaction.                                             |
| FDB Interaction ID      | An FDB-assigned numerical identifier for the interaction.                                           |
| Interaction Description | A text description of the interaction.                                                              |
| Monograph ID            | A numerical identifier for the Professional Monograph associated with the interaction.              |
| Severity Level          | A coded severity indicator.                                                                         |
| Clinical Effect 1       | A three letter code describing the clinical effect.                                                 |
| Clinical Effect 2       | A three letter code describing the clinical effect.                                                 |

<span id="_Toc75767192" class="anchor"></span>Table 25: FDB Interaction ID-Drug Pairs Fields

If the latest FDB update contains added or deleted drug pairs, then these will be displayed on separate tabs titled "FDB Interaction ID \<FDB Interaction ID number\>-DP".

<span id="_Toc403984504" class="anchor"></span>Figure 202: FDB Interaction ID-Drug Pairs Tab

![](pecs-version-6-2-user-guide/203.png)

The following fields are included in the report:

| Field                        | Description                                                                                                          |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Routed Generic 1 Description | The Routed Generic Description of Drug 1 in the Drug Pair.                                                           |
| Routed Generic 2 Description | The Routed Generic Description of Drug 2 in the Drug Pair.                                                           |
| DATUP Action                 | The action that DATUP will perform. Either DATUP will add the drug pair to the PECS database or delete it from PECS. |

<span id="_Toc75767193" class="anchor"></span>Table 26: FDB Comparison Report Row Fields

> **NOTE:** A DDI record that is not listed on the DDI-DT FDB Comparison Report spreadsheet can still have added or deleted drug pairs listed in the latest incremental FDB update file. In that case, the drug pair information is just listed on an FDB Interaction ID-DP spreadsheet.

### Structure of the FDB Comparison Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc403984500" class="anchor"></span>Figure 203: Sample FDB Comparison Report - Duplicate Therapy

![](pecs-version-6-2-user-guide/204.png)

Each FDB Comparison Report lists the "FDB Update Received" date, which is the date listed in the Incremental FDB Update file. Each report lists comparison sets of VA and FDB data. Each comparison set consists of at least three rows separated by a blue line. The three rows are:

| Row Name          | Row Description                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VA Custom         | Data in the Custom VA record. If the corresponding FDB record has not been customized, then a "Not customized" message will be in the Action Status column and the rest of the row will be blank.                                                                                                                                                                                      |
| FDB After Update  | Data in the Incremental FDB Update File. This data will be in the PECS database shortly after the incremental FDB update is done via DATUP.                                                                                                                                                                                                                                            |
| FDB Before Update | Data in the PECS FDB record. This data will be replaced by the 'FDB After Update' data. If the FDB After Update and FDB Before Update data of the same type are different, then they are marked with an asterisk (\*) and colored red. Records that do not have any differences between the FDB Before Update and FDB After Update data of the same type are not listed in the report. |

<span id="_Toc75767194" class="anchor"></span>Table 27: FDB Comparison Report Statuses

Each FDB Comparison Report has the following columns:

<table>
<caption><p><span id="_Toc75767195" class="anchor"></span>Table 28: FDB Comparison Duplicate Therapy Report Fields</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Column Name</th>
<th>Column Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Action Status</td>
<td>The state of the associated VA record based on the most recent action performed. PECS compares FDB data with VA customizations in any Action Status, including Rejected or Deleted.</td>
</tr>
<tr class="even">
<td>Action Date</td>
<td>The date the current action (Action Status) was taken.</td>
</tr>
<tr class="odd">
<td>DATUP will delete</td>
<td>YES in this column Indicates the associated FDB record will be deleted by DATUP. If the column is blank, then the associated FDB record will not be deleted by DATUP.<br />
<br />
If the FDB record will be deleted by DATUP, then only the FDB Interaction ID and DATUP will delete columns will be filled out in the FDB After Update row. All the other columns will be blank.</td>
</tr>
</tbody>
</table>

<span id="_Toc75767195" class="anchor"></span>Table 28: FDB Comparison Duplicate Therapy Report Fields

The reports are organized by type and the date of the FDB Incremental Update. Links to the reports are kept for eight weeks on the Reports page. To run an FDB Comparison report, select the appropriate FDB Incremental Update date under the appropriate Report Heading.

<span id="_Toc403984501" class="anchor"></span>Figure 204: FDB Incremental Updates

![](pecs-version-6-2-user-guide/205.png)

If there are no differences between the FDB After Update and FDB Before Update data of the same type in any of the records, then a "No Data Found" message is printed on the FDB Comparison Report.

<span id="_Toc403984502" class="anchor"></span>Figure 205: Report with No Differences

![](pecs-version-6-2-user-guide/206.png)

### FDB Comparison Duplicate Therapy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duplicate Therapy FDB Comparison Report displays the differences between the PECS FDB data and the data in the Incremental FDB Update file for the Duplicate Therapy (DT) concept. This report displays the following DT-specific data:

<span id="_Toc403984505" class="anchor"></span>Figure 206: FDB Comparison Duplicate Therapy Report

![](pecs-version-6-2-user-guide/207.png)

The three lines display the following fields:

| Field Name    | Field Description                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------|
| DTCID         | Duplicate Therapy Control ID. A numerical identifier for the DT FDB and VA records.               |
| Dup Allowance | Duplicate Allowance. The number of drugs performing the same function before a warning is issued. |
| Description   | A description (name) of the drug that is the basis of the DT record.                              |

<span id="_Toc75767196" class="anchor"></span>Table 29: FDB Comparison Dose Range Report

To run the Duplicate Therapy FDB Comparison report, click the desired date of an FDB Incremental Update under the appropriate Duplicate Therapy heading.

<span id="_Toc403984506" class="anchor"></span>Figure 207: FDB Incremental Update Dates

![](pecs-version-6-2-user-guide/208.png)

### FDB Comparison Dose Range Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dose Range FDB Comparison Report displays the differences between the PECS FDB data and the data in the Incremental FDB Update file for the Dose Range (DR) concept.

<span id="_Toc403984507" class="anchor"></span>Figure 208: FDB Comparison Dose Range Report

![](pecs-version-6-2-user-guide/209.png)

Only records where the Concept Type = 6 will display on the report. If the DR FDB record has not been customized, then it will display on the report if the following conditions were met:

- Data in all of the first seven fields (Concept ID Number, Age Low in Days, Age High in Days, Dose Route ID, Dose Type ID, FDBDX, HITTYPE) is identical in the PECS FDB record and the latest incremental FDB update
- Data in at least one other field is different in the PECS FDB record and the latest incremental FDB update

If a DR FDB record has been customized, then it will display on the report if all the conditions mentioned above have been met and the active VA custom record and the PECS FDB record are cross-referenced. Thus indicating that the active VA custom record was created from the FDB record.

Fields

| Field Name                          | Field Description                                                                                                                                                                                                                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Concept ID Number                   | Number identifying the drug. Identifies a specific drug within a given concept type.                                                                                                                                                                                                                         |
| Age Low in Days                     | Lowest patient age in days to which dosing information applies                                                                                                                                                                                                                                               |
| Age High in Days                    | Highest patient age in days to which dosing information applies                                                                                                                                                                                                                                              |
| Dose Route ID                       | Dose Route Identifier. Refers to the route of administration, which is the site or method by which a drug is administered                                                                                                                                                                                    |
| Dose Type ID                        | Dose type identifier                                                                                                                                                                                                                                                                                         |
| FDBDX                               | FDBDX type code to identify a Medical Condition                                                                                                                                                                                                                                                              |
| HITTYPE                             | Signifies whether the dose record came from the Dosage Range Check module or the Minimum/Maximum dosing module. There are 3 possible values: 1 – Dose Range Check; 2 – Dosing Not Established For This Age Range; 3 – Minimum/maximum dosing. HITTYPE is used to determine how to structure the dose alerts. |
| Concept ID Description              | Text description of the Concept ID. Also defined as the drug name. For example, the Concept ID Description is GUAIFENESIN/PHENYLPROPANOLAMINE HCL/ACETAMINOPHEN/CAFFEINE ORAL TABLET and the Concept ID is 713.                                                                                              |
| DXID                                | First Databank Medical Lexicon (FML) Disease Identifier                                                                                                                                                                                                                                                      |
| Dose Low                            | Minimum amount to be administered per day                                                                                                                                                                                                                                                                    |
| Dose Low Units                      | Unit of measure for low dose per day                                                                                                                                                                                                                                                                         |
| Dose High                           | Highest amount to be administered per day                                                                                                                                                                                                                                                                    |
| Dose High Units                     | Unit of measure for high dose per day                                                                                                                                                                                                                                                                        |
| Dose Form Low                       | Low dose for a given dose form                                                                                                                                                                                                                                                                               |
| Dose Form Low Units                 | Unit of measure for the dose form (EA/KG/DAY)                                                                                                                                                                                                                                                                |
| Dose Form High                      | High dose for a given dose form                                                                                                                                                                                                                                                                              |
| Dose Form High Units                | Unit of measure for the dose form (EA/KG/DAY)                                                                                                                                                                                                                                                                |
| Frequency Low                       | Low end of a drug's frequency of administration per day                                                                                                                                                                                                                                                      |
| Frequency High                      | High end of a drug's frequency of administration per day                                                                                                                                                                                                                                                     |
| Duration Low                        | Lowest recommended duration of therapy (in days)                                                                                                                                                                                                                                                             |
| Duration High                       | Highest recommended duration of therapy (in days)                                                                                                                                                                                                                                                            |
| Maximum Duration                    | Maximum recommended duration of therapy (in days)                                                                                                                                                                                                                                                            |
| Maximum Single Dose                 | Maximum amount to be administered in a single dose                                                                                                                                                                                                                                                           |
| Maximum Single Dose Units           | Unit of measure for the maximum single dose                                                                                                                                                                                                                                                                  |
| Maximum Single Dose Form            | Maximum single dose for a given form                                                                                                                                                                                                                                                                         |
| Maximum Single Dose Form Units      | Unit of measure for the dose form (EA/KG/DAY)                                                                                                                                                                                                                                                                |
| Maximum Daily Dose                  | Maximum amount to be administered per day                                                                                                                                                                                                                                                                    |
| Maximum Daily Dose Units            | Unit of measure for the maximum daily dose                                                                                                                                                                                                                                                                   |
| Maximum Daily Dose Form             | Maximum daily dose for a dose form                                                                                                                                                                                                                                                                           |
| Maximum Daily Dose Form Units       | Unit of measure for the dose form (EA/KG/DAY)                                                                                                                                                                                                                                                                |
| Maximum Lifetime Dose               | Maximum amount to be administered over a patient's lifetime, if available                                                                                                                                                                                                                                    |
| Maximum Lifetime Dose Units         | Unit of measure for maximum lifetime dose                                                                                                                                                                                                                                                                    |
| Maximum Lifetime Dose Form          | Maximum lifetime dose for a given dose form                                                                                                                                                                                                                                                                  |
| Maximum Lifetime Dose Form Units    | Unit of measure for the dose form (EA/KG/DAY)                                                                                                                                                                                                                                                                |
| Dose Rate Low                       | Minimum amount to be administered per dose rate (hours or minutes)                                                                                                                                                                                                                                           |
| Dose Rate Low Units                 | Unit of measure for low dose rate (hours or minutes)                                                                                                                                                                                                                                                         |
| Dose Rate High                      | Highest amount to be administered per dose rate (hours or minutes)                                                                                                                                                                                                                                           |
| Dose Rate High Units                | Unit of measure for high dose rate (hours or minutes)                                                                                                                                                                                                                                                        |
| Dose Form Rate Low                  | Low dose for a given dose form rate (hours or minutes)                                                                                                                                                                                                                                                       |
| Dose Form Rate Low Units            | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                                                                                                    |
| Dose Form Rate High                 | High dose for a given dose form rate (hours or minutes)                                                                                                                                                                                                                                                      |
| Dose Form Rate High Units           | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                                                                                                    |
| Maximum Single Dose Rate            | Maximum amount to be administered in a single dose rate (hours or minutes)                                                                                                                                                                                                                                   |
| Maximum Single Dose Rate Units      | Unit of measure for the maximum single dose rate (hours or minutes)                                                                                                                                                                                                                                          |
| Maximum Single Dose Form Rate       | Maximum single dose for a given dose form rate (hours or minutes)                                                                                                                                                                                                                                            |
| Maximum Single Dose Form Rate Units | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                                                                                                    |
| Maximum Daily Dose Form Rate        | Maximum daily dose for a dose form rate (hours or minutes)                                                                                                                                                                                                                                                   |
| Maximum Daily Dose Rate             | Maximum amount to be administered per dose rate (hours or minutes)                                                                                                                                                                                                                                           |
| Maximum Daily Dose Form Rate Units  | Unit of measure for the dose form rate (hours or minutes)                                                                                                                                                                                                                                                    |
| Maximum Daily Dose Rate Units       | Unit of measure for the maximum daily dose rate (hours or minutes)                                                                                                                                                                                                                                           |
| Max Single NTE Dose                 | Maximum Not-to-Exceed (NTE) amount to be administered in a single dose                                                                                                                                                                                                                                       |
| Max Single NTE Dose Unit            | Unit of measure for the maximum single NTE dose                                                                                                                                                                                                                                                              |
| Max Single NTE Dose Form            | Maximum Unit of measure for the NTE dose form (EA/KG/DAY)                                                                                                                                                                                                                                                    |
| Max Single NTE Dose Form Unit       | Maximum Not-to-Exceed amount to be administered in a single dose for a given dose form                                                                                                                                                                                                                       |
| Hepatic Impairment Indicator        | Indicates that the drug's dosing information needs to be adjusted for a patient with hepatic impairment. This flag does not differentiate between mild, moderate, and severe hepatic failure.                                                                                                                |
| Renal Impairment Indicator          | Indicates whether the dosing information needs to be modified for any degree of renal impairment in the patient.                                                                                                                                                                                             |
| CRCL Threshold                      | Lowest Creatinine Clearance (CRCL) to which dosing applies.                                                                                                                                                                                                                                                  |
| CRCL Threshold Units                | Unit of measure for the Creatinine Clearance (CRCL) threshold.                                                                                                                                                                                                                                               |
| Low Elimination Half Life           | Low end of the drug's half-life range                                                                                                                                                                                                                                                                        |
| High Elimination Half Life          | High end of the drug's half-life range.                                                                                                                                                                                                                                                                      |
| Half Life Units                     | Unit of time for the half-life range of a drug.                                                                                                                                                                                                                                                              |
| Weight Required Indicator           | Indicates whether weight is required for dosing.                                                                                                                                                                                                                                                             |
| BSA                                 | Required Indicator Indicates whether Body Surface Area (BSA) is required for dosing                                                                                                                                                                                                                          |

Table shows field names and descriptions on FDB Comparison Dose Range Report

# Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS provides an online help system that provides information on using the application.

<span id="_Toc75767405" class="anchor"></span>Figure 209: PECS Online Help Window

![](pecs-version-6-2-user-guide/210.png)

## Accessing Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two ways to access online help: the Help tab and Page Help link.

1.  Select the Help tab to open the main Online Help page

<span id="_Toc75767406" class="anchor"></span>Figure 210: The Help Tab

![](pecs-version-6-2-user-guide/211.png)

243. Select the Page Help link to access help specific to the current page.

<span id="_Toc75767407" class="anchor"></span>Figure 211: The Page Help Link

![](pecs-version-6-2-user-guide/212.png)

Using the Page Help link will display help page relevant to the current page. Click the Show link to display the Table of Contents.

<span id="_Toc75767408" class="anchor"></span>Figure 212: The Show Link

![](pecs-version-6-2-user-guide/213.png)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*7*2 PECS User Guide

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An overview of the PECS system and this User Guide.

### System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A more detailed description of the PECS system including a non-technical overview of the product design, data flow, and application access.

### Customization Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides a brief overview of customizations and how they are created in PECS.

### Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Discusses logging into PECS and the organization of the application.

### PECS by Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS functions are organized into Tabs. PECS by Tab describes the tabs found in PECS.

### Using Advanced Query/Customization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instruction on using Advanced Query/Customization feature.

### Working with Customization Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instruction on how to create and process customization requests.

### User Roles and Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information on PECS User Roles and the functions they perform.

### Detail Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description of the Detail Pages.

### Sample Modification Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample scenarios on why a record would be customized and the steps to make the customization.

### Interactions for a Single Drug Report Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field                            | Description                                                                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Source                           | Source of the record; either VA or FDB                                                                                                  |
| Routed Generic \#1               | A generic drug name, e.g., "Rifampin Oral"                                                                                              |
| Routed Generic \#2               | A generic drug name, e.g., "Rifampin Oral"                                                                                              |
| Severity Level Code              | The severity of the interaction.                                                                                                        |
| Interaction Description          | A brief description of the interaction.                                                                                                 |
| Interaction ID                   | A numerical identifier assigned to the interaction.                                                                                     |
| Corresponding FDB Interaction ID | VA records only: the interaction as described by First Databank. If there is no corresponding interaction, this field will contain '0'. |
| Action Date                      | The date and time of the most recent update to the record.                                                                              |

<span id="_Toc161905523" class="anchor"></span>Table 12: DDI Fields
