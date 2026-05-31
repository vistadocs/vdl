---
title: Inpatient Medications Technical Manual/Security Guide (Updated PSJ*5*399)
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Inpatient Medications /Security Guide (Updated PSJ*5*399)
app_code: PSJ
app_name: 'Pharmacy: Inpatient Medications'
section: CLI
app_status: archive
pkg_ns: PSJ
patch_ver: 5.0
patch_id: PSJ*5.0*399
group_key: PSJ:PSJ:5.0
file_numbers:
- '1'
- '2'
- '3'
- '3.2'
- '3.5'
- '4'
- '4.5'
- '5'
- '7'
- '8'
- '20.2'
- '24'
- '25.1'
- '25.2'
- '26'
- '34'
- '42'
- '44'
- '50'
- '50.2'
- '50.3'
- '50.4'
- '50.606'
- '50.68'
- '50.7'
- '50.713'
- '50.8'
- '51.1'
- '51.15'
- '51.2'
- '52.6'
- '52.7'
- '52.75'
- '53.1'
- '53.2'
- '53.3'
- '53.45'
- '53.46'
- '53.5'
- '53.52'
- '55'
- '55.06'
- '57.1'
- '57.5'
- '57.6'
- '57.7'
- '57.8'
- '58.1'
- '58.6'
- '58.601'
- '58.63'
- '58.64'
- '58.7'
- '58.71'
- '58.72'
- '59.4'
- '59.5'
- '59.6'
- '59.7'
- '62'
- '64'
- '100'
- '101'
- '104'
- '135'
- '154'
- '200'
- '870'
- '2802'
- '900932.4'
security_keys:
- PROVIDER
- PSJ PHARM TECH
- PSJ RNFINISH
- PSJ RNURSE
- PSJ RPHARM
- PSJI MGR
- PSJI PHARM TECH
- PSJI PURGE
- PSJI RNFINISH
- PSJU RPH
- RPHARM
menu_options: 1
description: The Inpatient Medications computer software package is one segment of the Veterans Health Information Systems and Technology Architecture (VistA) for the Department of Veterans Affairs. This package is a computerized system of tracking and assisting in the manufacture, dispensing, and administration
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 46084
section_count: 59
table_count: 33
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: December 1997
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med_Archive/PSJ_5_0_P399_tm.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med_Archive/PSJ_5_0_P399_tm.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=390
audit_applied: '2026-05-31'
master_source: Inpatient Medications Technical Manual/Security Guide (Updated PSJ*5*399)
master_pub_date: December 1997
consolidated_from: 2 versions
prior_versions:
- Inpatient Medications Technical Manual/Security Guide (PSJ*5.0*447)
consolidated_title: inpatient medications technical manual/security guide
---

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/001.png)

INPATIENT MEDICATIONS

TECHNICAL MANUAL/SECURITY GUIDE

December 1997

(Revised September 2022)

Enterprise Program Management Office

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Installation](#installation)
  - [Inpatient Parameters](#inpatient-parameters)
    - [Fields from the PHARMACY SYSTEM File (#59.7)](#fields-from-the-pharmacy-system-file-597)
    - [Fields from the INPATIENT WARD PARAMETERS File (#59.6)](#fields-from-the-inpatient-ward-parameters-file-596)
    - [Fields from the INPATIENT USER PARAMETERS File (#53.45)](#fields-from-the-inpatient-user-parameters-file-5345)
    - [Fields from the IV ROOM File (#59.5)](#fields-from-the-iv-room-file-595)
    - [Fields from the CLINIC DEFINITION File (#53.46)](#fields-from-the-clinic-definition-file-5346)
    - [Fields from the IV MEDICATION ORDERS DC'D File (#52.75)](#fields-from-the-iv-medication-orders-dcd-file-5275)
- [Package Security](#package-security)
  - [Option Security Keys](#option-security-keys)
  - [File Security](#file-security)
- [File List](#file-list)
  - [Unit Dose File Diagram](#unit-dose-file-diagram)
  - [IV File Diagram](#iv-file-diagram)
- [Routines](#routines)
  - [Descriptions](#descriptions)
  - [Callable Routines](#callable-routines)
    - [Deleting Inpatient Routines](#deleting-inpatient-routines)
- [Templates](#templates)
  - [Print Templates](#print-templates)
  - [Input Templates](#input-templates)
  - [List Templates](#list-templates)
- [Exported Options](#exported-options)
  - [Stand-alone Options](#stand-alone-options)
  - [Top-level Menus](#top-level-menus)
    - [Menu Assignment](#menu-assignment)
    - [Menu Placement](#menu-placement)
  - [Options](#options)
- [Data Archiving and Purging](#data-archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
    - [Unit Dose Auto Purging](#unit-dose-auto-purging)
    - [IV Auto Purging](#iv-auto-purging)
    - [Unit Dose Manual Purging – Temporarily Unavailable](#unit-dose-manual-purging-temporarily-unavailable)
    - [IV Manual Purging – Temporarily Unavailable](#iv-manual-purging-temporarily-unavailable)
- [Inpatient Medications and CPRS](#inpatient-medications-and-cprs)
  - [Installation of the Protocols for CPRS](#installation-of-the-protocols-for-cprs)
  - [Converting](#converting)
    - [Order Conversion](#order-conversion)
    - [Pick List Conversion](#pick-list-conversion)
    - [Order Set Conversion](#order-set-conversion)
    - [Verification Data Conversion](#verification-data-conversion)
  - [Protocol Descriptions](#protocol-descriptions)
  - [Health Level Seven (HL7) Messaging](#health-level-seven-hl7-messaging)
    - [HL7 Ordering Fields](#hl7-ordering-fields)
    - [Order Event Messages](#order-event-messages)
    - [Special Escaping Characters](#special-escaping-characters)
  - [STAT, ASAP, and NOW Order Notification](#stat-asap-and-now-order-notification)
    - [PSJ STAT NOW PENDING ORDER Mail Group](#psj-stat-now-pending-order-mail-group)
    - [PSJ STAT NOW ACTIVE ORDER Mail Group](#psj-stat-now-active-order-mail-group)
    - [Adding a Remote Member as a Subscriber](#adding-a-remote-member-as-a-subscriber)
    - [Setting Up Ward-Specific Mail Groups](#setting-up-ward-specific-mail-groups)
- [Inpatient Medications and BCMA](#inpatient-medications-and-bcma)
  - [API Exchange](#api-exchange)
    - [APIs provided to BCMA](#apis-provided-to-bcma)
    - [APIs provided to Inpatient Medications](#apis-provided-to-inpatient-medications)
  - [Med Order Button](#med-order-button)
- [Interfacing with the Bar Code Label Printer](#interfacing-with-the-bar-code-label-printer)
  - [Hardware Set Up](#hardware-set-up)
  - [Software Set Up](#software-set-up)
    - [Zebra Printers](#zebra-printers)
    - [Dot Matrix and Laser Printers](#dot-matrix-and-laser-printers)
  - [Printed Bar Code IV Label Sample](#printed-bar-code-iv-label-sample)
- [Interfacing with the ATC](#interfacing-with-the-atc)
  - [Pharmacy Set Up](#pharmacy-set-up)
    - [Drug Set Up](#drug-set-up)
    - [Ward Group Set Up](#ward-group-set-up)
  - [Hardware Set Up](#hardware-set-up-1)
    - [Device File Example](#device-file-example)
    - [MUX Table Example](#mux-table-example)
    - [DECServer Examples](#decserver-examples)
    - [Wiring for CXA16 Card](#wiring-for-cxa16-card)
    - [ATC-HPS Configuration Set Up](#atc-hps-configuration-set-up)
    - [Device File Setup Network Change](#device-file-setup-network-change)
    - [Common Problems](#common-problems)
- [Resource Requirements](#resource-requirements)
  - [Hardware](#hardware)
  - [Disk Space](#disk-space)
    - [Routines](#routines-1)
    - [Data](#data)
  - [Journaling Globals](#journaling-globals)
  - [Translating Globals](#translating-globals)
  - [Nightly Background Jobs](#nightly-background-jobs)
  - [Queuing and Printing across CPUs](#queuing-and-printing-across-cpus)
- [External Relationships](#external-relationships)
  - [Packages Needed to Run Inpatient Medications](#packages-needed-to-run-inpatient-medications)
  - [Unit Dose Medications and Ward Stock](#unit-dose-medications-and-ward-stock)
  - [Unit Dose Medications and Drug Accountability](#unit-dose-medications-and-drug-accountability)
  - [Calls Made by Inpatient Medications](#calls-made-by-inpatient-medications)
  - [Introduction to Integration Agreements and Entry Points](#introduction-to-integration-agreements-and-entry-points)
- [Internal Relationships](#internal-relationships)
- [Internal Calls and Variables](#internal-calls-and-variables)
  - [Package-Wide Variables](#package-wide-variables)
    - [Inpatient Sign-on Variables](#inpatient-sign-on-variables)
    - [Standard Variables Used Throughout the Package](#standard-variables-used-throughout-the-package)
    - [IV Sign-on Variables](#iv-sign-on-variables)
    - [Variables](#variables)
- [On-line Documentation](#on-line-documentation)
  - [On-line Help](#on-line-help)
  - [Printing Data Dictionaries](#printing-data-dictionaries)
- [Additional Information](#additional-information)
  - [SAC Exemptions](#sac-exemptions)
  - [IV Ward List](#iv-ward-list)
  - [IV Manufacturing List](#iv-manufacturing-list)
  - [IV Suspense List](#iv-suspense-list)
  - [Unit Dose "Defaults"](#unit-dose-defaults)
    - [Order Start Date/Time Calculation](#order-start-datetime-calculation)
    - [Stop Date/Time: Calculation](#stop-datetime-calculation)
    - [Patient's Default Stop Date/Time](#patients-default-stop-datetime)
    - [Pick List Wall](#pick-list-wall)
- [Glossary](#glossary)
- [Appendix A: Inpatient Medication Orders for Outpatients–Phase I & II and Inpatient Medication Reqs for SFG IRA–Phase II](#appendix-a-inpatient-medication-orders-for-outpatientsphase-i-ii-and-inpatient-medication-reqs-for-sfg-iraphase-ii)
  - [Introduction](#introduction-1)
  - [Inpatient Medication Orders for Outpatients – Phase I & II](#inpatient-medication-orders-for-outpatients-phase-i-ii)
    - [Inpatient Medications V. 5.0](#inpatient-medications-v-50)
    - [Order Entry Results Reporting V. 3.0 (CPRS)](#order-entry-results-reporting-v-30-cprs)
    - [Scheduling V. 5.3](#scheduling-v-53)
  - [Inpatient Medication Requirements for SFG IRA – Phase II](#inpatient-medication-requirements-for-sfg-ira-phase-ii)
    - [Inpatient Medications V. 5.0 and Pharmacy Data Management V. 1.0](#inpatient-medications-v-50-and-pharmacy-data-management-v-10)
  - [Installation](#installation-1)
    - [Overview](#overview)
    - [Post-Installation Setup](#post-installation-setup)
- [Appendix B: Pharmacy Interface Automation](#appendix-b-pharmacy-interface-automation)
  - [Introduction](#introduction-2)
  - [New Functionality](#new-functionality)
  - [Options and Build Components](#options-and-build-components)
  - [HL7 Messaging](#hl7-messaging)
    - [SCH Schedule Activity Information](#sch-schedule-activity-information)
  - [Modified and New Routines](#modified-and-new-routines)
  - [PADE Stock Requisition Order: OMS^O05](#pade-stock-requisition-order-omso05)
    - [PADE OMS – MSH Segment](#pade-oms-msh-segment)
    - [PADE OMS – PID Segment](#pade-oms-pid-segment)
    - [PADE OMS – PV1 Segment](#pade-oms-pv1-segment)
    - [PADE OMS – ORC Segment](#pade-oms-orc-segment)
    - [PADE OMS – RQD Segment](#pade-oms-rqd-segment)
    - [PADE OMS – NTE Segment](#pade-oms-nte-segment)
  - [Application Acknowledgements](#application-acknowledgements)
Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual.
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/2022</td>
<td><p>Title, i,</p>
<p><a href="#Patch_399_Protocol_Updates">49</a>,</p>
<p><a href="#Patch_399_Indication_New_Update">129</a>,</p>
<p><a href="#Patch_399_Indication_Modified_new_routin">147</a></p></td>
<td>PSJ*5*399</td>
<td><p>Updated Title page, Revision History, and Footer.</p>
<p>Listed <a href="#Patch_399_Protocol_Updates">which protocols were updated for patch PSJ*5*399 to support Indications</a>.</p>
<p>Added an item for patch <a href="#Patch_399_Indication_New_Update">PSJ*5*399 about Indications under New Updates</a>.</p>
<p>Added a <a href="#Patch_399_Indication_Modified_new_routin">section for patch PSJ*5*399 and indications under Modified and New Routines</a>.</p></td>
</tr>
<tr class="even">
<td>07/2021</td>
<td><p>Title, i</p>
<p>27</p>
<p>146</p></td>
<td>PSJ*5*364</td>
<td><p>Updated Title page, Revision History, Glossary, and Footer.</p>
<p>Added missing routines: <a href="#P27_PSJPDCLU">PSJPDCLU</a> and <a href="#P27_PSJPDCLV">PSJPDCLV</a></p>
<p>Added Hazardous Indicators to <a href="#P146_HL7_ZZZ">HL7 segment ZZZ</a></p></td>
</tr>
<tr class="odd">
<td>09/2020</td>
<td><p>Title, i</p>
<p><a href="#CLINIC_APPT_DATE_RANGE_MIN">15</a></p>
<p><a href="#PSJ_LM_NEW_CM_ORDER">46</a></p>
<p><a href="#CM_New_Clinic_Medication_Entry">114</a></p></td>
<td>PSJ*5*319</td>
<td><p>Updated Title page and Revision History</p>
<p>Added <a href="#CLINIC_APPT_DATE_RANGE_MIN">CLINIC APPT DATE RANGE MIN</a>, and <a href="#CLINIC_APPT_DATE_RANGE_MAX">CLINIC APPT DATE RANGE MAX</a> to Clinic Definitions</p>
<p>Added <a href="#PSJ_LM_NEW_CM_ORDER">PSJ LM NEW CM ORDER</a> (New Clinic Medication Entry) to Protocol Descriptions</p>
<p>Glossary: Under <strong><u>Patient/Order Action Prompts</u></strong>, added <a href="#CM_New_Clinic_Medication_Entry">CM New Clinic Medication Entry</a></p>
<p>Global: Updated Footers, made the manual 508-compliant.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/2020</td>
<td><a href="#Complex_Order_note">112</a></td>
<td>PSJ*5*388</td>
<td><p>Added <a href="#Complex_Order_note">Note for Complex Order</a> that explains the rules established to resolve the issue of overlapping administration schedules for a complex order</p>
<p>Revised dates on Title page and in footers</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/2019</td>
<td><p><a href="#TOC">ii</a></p>
<p><a href="#file-list">19</a><br />
<a href="#descriptions">25</a></p>
<p><a href="#PSJL_Manager">33</a></p>
<p><a href="#PSJL_Manager2">35</a></p></td>
<td>PSJ*5*327</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Updated Section 4 File List and 4.1 Unit Dose File Diagram</p>
<p>Updated Section 5.1: Description</p>
<p>Updated Section 7.2.1 Added PSJL Manager</p>
<p>Updated Section 7.3: Options - Added PSJL Manager</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/2018</td>
<td><a href="#_top">Title Page</a>, <a href="#options">32-33</a></td>
<td>PSJ*5*353</td>
<td><p>Update Menu Options</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td><p>Title Page</p>
<p>25</p></td>
<td>PSJ*5*347</td>
<td><p>Updated revision month/year</p>
<p>Deleted routine: PSJDGAL; Added missing routine: PSJPDCL</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/2017</td>
<td>i-iv, viii, 14, 15-16, 19, 24</td>
<td>PSJ*5*325</td>
<td><p>Added new field to IV ROOM File (#59.5).</p>
<p>Added new file, IV MEDICATION ORDERS DC'D (#52.75), and its fields.</p>
<p>Added IV MEDICATION ORDERS DC'D (#52.75) to File List.</p>
<p>Added new routines: PSIVARH, PSIVARH1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/2016</td>
<td><p>i-x</p>
<p>32</p>
<p>19</p>
<p>27</p>
<p>44</p>
<p>137-160</p></td>
<td>PSJ*5*317</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Updated section 7.3 Options List</p>
<p>Updated section 4: File List</p>
<p>Updated section 6.2: Input Templates</p>
<p>Updated section 9.3: Protocol Descriptions</p>
<p>Added Appendix B for Pharmacy Interface Automation.</p>
<p>Updated section 21.4 HL7 Messaging.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/2016</td>
<td><p>i-x</p>
<p>23</p></td>
<td>PSJ*5*315</td>
<td><p>Updated Revision History and Table of Contents</p>
<p>Added PSGAH routine to section 5.1 Descriptions.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/2016</td>
<td><p>i-ii,</p>
<p>24,25</p>
<p>92, 119</p>
<p>121, 123</p></td>
<td>PSJ*5*281</td>
<td><p>Update Revision History</p>
<p>Updated example : How to print DBIA information from FORUM</p>
<p>Updated Glossary /Added Allergy Order Checks,</p>
<p>Clinical Reminder Order Checks, Enhanced Order Checks</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/2015</td>
<td>123</td>
<td>PSJ*5*259</td>
<td><p>Added verbiage to 'Pending Orders' section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td><p>All</p>
<p>i-vi, vii-x</p>
<p>15</p>
<p>122-123</p></td>
<td>PSJ*5*252<br />
PSJ*5*257</td>
<td><p>Renumbered all pages</p>
<p>Updated Revision History &amp; Table of Contents</p>
<p>Added IMO DC/EXPIRED DAY LIMIT bullet and note</p>
<p>Update Glossary</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2013</td>
<td>i-iii, 8a, 14, 14a-14b, 23, 23a, 121-130, 130a-130b</td>
<td>PSJ*5*279</td>
<td><p>Added new fields, "CLINIC MISSING DOSE REQUEST PRINTER" and "PRE-EXCHANGE REPORT DEVICE" to the CLINIC DEFINITION (#53.46) file. Updated Clinic Definition file description and added new routines: PSJBCMA6, PSJIBAG. Updated Glossary</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/2013</td>
<td><p>i-iii, 23, 23a-23b, 29, 32, 32a-32b,</p>
<p>47-50</p></td>
<td>PSJ*5*275</td>
<td><p>Added new Templates, new Option and updated Routines</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>01/2013</td>
<td><p>i-ii</p>
<p>23</p>
<p>25</p>
<p>32</p>
<p>47-48</p>
<p>69-70b</p>
<p>86</p>
<p>94a</p>
<p>118</p>
<p><a href="#p120">120</a><a href="#p118">-</a><a href="#p122">122</a></p></td>
<td>PSJ*5*260<br />
PSJ*5*268</td>
<td><p>Updated Revision History</p>
<p>Updated Routines: PSJADM, PSJCLNOC, PSJDGAL2, PSJDGCK, PSJOEA2, PSJUTL5</p>
<p>Sentence reworded by CPS</p>
<p>Added option PSJ CHECK DRUG INTERACTION</p>
<p>Added new Protocols</p>
<p>Fix page numbering to eliminate pages with number 70</p>
<p>Changed wording in Section 14.5</p>
<p>Added Integration Agreement</p>
<p>Added three new Hidden Actions</p>
<p>Added BSA, CrCL, &amp; DATUP to the Glossary</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/2012</td>
<td>i-ii, vi-vii, 81-82, 82a- 82b</td>
<td>PSJ*5*284</td>
<td><p>Added instructions for editing the Device File for ATC Device to use Network Channel.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/2012</td>
<td>i, 21-23, 69, 94a</td>
<td>PSJ*5*267</td>
<td>Added new Routine<br />
Added new API<br />
Added new Integration Agreement<br />
(R. Singer, PM; B. Thomas, Tech Writer)</td>
</tr>
<tr class="odd">
<td>01/2012</td>
<td><p>i-ii<u>,</u> v-viii</p>
<p>22, 23</p>
<p>69</p>
<p>94</p></td>
<td>PSJ*5*254</td>
<td><p>Updated Table of Contents</p>
<p>Updated Routines</p>
<p>Added API</p>
<p>Added 5653 and 5654 Inpatient Medications Integration Agreements</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>i, v, vi, vii, vii, 5-8b, (changed flow) 22, 23, 24, removed 25-26, changed 53, 85, 86, 93-94;94a-b, 121--130</td>
<td>PSJ*5*181</td>
<td><p>Changes to <em>Revision History</em>, <em>Table of Contents</em>; added new field to PHARMACY SYSTEM File (#59.7), added new field to the INPATIENT WARD PARAMETERS File (#59.6). Added information re: the Pharmacy Reengineering (PRE) API Manual under "<em>Callable Routines</em>"; removed entire section 5.3, Routine Mapping, and all its sub-sections; added Health Level Seven (HL7) data field under segment {RXC}. Added the following "<em>Inpatient Medications Custodial Integration Agreements</em>": 4074, 4264, 4580, 5001, 5057; 5058, 5306, 5385. Added two packages, HWSC and VistALink, to <em>External Relationships</em>, under <em>Packages Needed to Run Inpatient Medications</em>. Added the following call routines and their entry points: OROCAPI, PSSDSAPD, PSSDSAPI, PSSFDBRT, PSODDPR4, PSODRDU2. Added the items <strong>DATUP, MOCHA,</strong> <strong>PECS, and</strong> <strong>PEPS</strong> in Glossary, which shifted all subsequent glossary items.</p>
<p>Added routines PSJMISC2 &amp;PSJOCVAR to the routines table and removed Section 5.3</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/2011</td>
<td>i, 53, 62, 64, 65</td>
<td>PSJ*5*226</td>
<td><p>Added to RXC section Field 5, "Additive Frequency" in HL7 Ordering Fields; updated Front Door – IV Fluids table with Field 5; updated Back Door – IV Fluids table with Field 5; updated example.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/2010</td>
<td>i, 22-23</td>
<td>PSJ*5*113</td>
<td><p>Added routine PSGSICH1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/2010</td>
<td><a href="#pi">i</a>, 23</td>
<td>PSJ*5*214</td>
<td>Added PSJQUTIL to the routine list in Section 5.1 for Patients on Specific Drug(s) Multidivisional Enhancements Project.<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/2009</td>
<td>22-23</td>
<td>PSJ*5*222</td>
<td><p>Added routine PSGOEF2.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/2008</td>
<td>vi, 23, 51-53, 57-58, 60-61, 63, 65, 65a-65b</td>
<td>PSJ*5*134</td>
<td><p>Parameters for escaping special characters added. New HL7 messages added. New routines added. HL7 order fields table contains an asterisk for each field that has special escaping characters.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/2007</td>
<td>74-76</td>
<td>PSJ*5*178</td>
<td><p>MED ROUTE now appears in larger font on IV labels from the Zebra bar code printer. Med ROUTE now prints on the IV labels for bar-code enabled printers, and it prints in larger font than surrounding text.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/2006</td>
<td>23, 94</td>
<td>PSJ*5*172</td>
<td><p>Encapsulation Cycle II project: Added PSJ53P1 to the Routine List in Section 5.1. Added DBIA 4537 to DBIA list. Changed the date on the Title Page to December 1997.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td><p>v-viii</p>
<p>8a-8b</p>
<p>66-68b</p></td>
<td>PSJ*5*154</td>
<td><p>In Section 2.2.2 Added "PRIORITIES FOR NOTIFICATION" field.</p>
<p>In Section 9.5, made correction to include the priority of ASAP in notifications. Added information regarding the three notifications parameters.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/2005</td>
<td>23</td>
<td>PSJ*5*146</td>
<td><p>Remote Data Interoperability (RDI) Project: Added PSJLMUT2 to the Routine List in Section 5.1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/2005</td>
<td>All</td>
<td>PSJ*5*163</td>
<td><p>Encapsulation Cycle II project: Added PSJ59P5 to the Routine List in Section 5.1. Added DBIA 4819 to DBIA list. Deleted DBIAs 172, 634, and 1882 from the DBIA list.</p>
<p>Reissued entire document due to a page numbering issue.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>
Preface
This technical manual is written for the Information Resources Management Service (IRMS) Chief/Site Manager and the Automated Data Processing Application Coordinator (ADPAC) for implementation and installation of the Inpatient Medications package. The main text of the manual outlines routine descriptions, file list, site configuration issues, variables, resource requirements, and package security.
<span id="TOC" class="anchor"></span>Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications computer software package is one segment of the Veterans Health Information Systems and Technology Architecture (VistA) for the Department of Veterans Affairs. This package is a computerized system of tracking and assisting in the manufacture, dispensing, and administration of medications within a medical care facility by using information common to all VistA packages such as patient information and Inpatient Medications orders entered by the users. The Inpatient Medications package consists of two modules: IV Medications and Unit Dose Medications.

The IV Medications module is one segment of VistA in use at the Department of Veterans Affairs Medical Centers (VAMCs). This module shares a common source of information, the Patient Database, with other applications such as the Outpatient Pharmacy and Laboratory packages. The basis for information in the Inpatient Medications IV Medications module is the patient data stored in the Patient Database.

The Unit Dose Medications module is a method of computerizing the inpatient drug distribution within the hospital. Unit dose orders are entered and edited by a ward clerk, provider, nurse, or pharmacist, and verified by a pharmacist and/or nurse. Orders can also be discontinued or renewed as appropriate. Once active, the orders are dispensed to the wards by means of the pick list. The system allows for dispensing tracking from the pick list.

The Unit Dose Medications module can also produce 24-hour, 7-day, or 14-day Medication Administration Records (MARs), which are the computerized versions of the manual Continuing Medication Records (CMRs). The MAR contains patient demographics, all requested types of active orders, and their administration schedules.

<u>Functional Description</u>

The Unit Dose Medications module is designed to provide a flexible method for order entry and medication dispensing. Each VAMC should be able to adapt the system to fit its own needs. The Unit Dose Medications module has the ability to perform the following functions:

- Tailor processes by facility, user, and/or medication.
- Allow for immediate entry of predefined sets of orders.
- Provide on-line order maintenance (e.g., edit, renewal, discontinuation).
- Generate labels containing order and patient information on demand and upon the entry/maintenance of an order.
- Provide on-line or printed patient profiles, which include a history of medication orders for the current or last facility visit.
- Display patient and order information.
- Mark orders that need attention.
- Display histories of all actions taken on active orders.
- Provide computerized pick lists, which include pre-calculated doses for pharmacists.
- Print various reports and forms for individual patients, individual wards, and pre-defined groups of wards.
- Provide an Action Profile of patient medication orders for use by physicians to cancel or continue medications.
- Provide medication administration records, alleviating the need for ward personnel to transcribe orders at the time of entry or renewal.
- Provide a Stop Order Notice report to notify users of orders near expiration.
- Discontinue medication orders for patients transferred between wards and/or services.
- Provide dispensing cost reports by patient, ward, service, drug, and provider.
- Provide a computerized order form when a provider enters orders.

The Inpatient Medications IV Medications module is a dispensing package. It will provide the pharmacy users with:

- IV labels
- Manufacturing worksheets
- Ward list for order update
- Management reports

The module will allow control of the manufacturing of IVs not achievable through manual procedures. The IV Medications module will also allow the pharmacy to establish and maintain, through order entry and ward updating, an accurate and timely data set of the hospital's IV orders.

All reports in the IV Medications module can be queued. When the module is entered for the first time, the user will be asked to define an IV room. Part of the IV room definition includes entering a printer label device and a printer report device. (These devices are defined in the *Site Parameters (IV)* \[PSJI SITE PARAMETERS\] option.) The device entered is the one most frequently used for label and report printing, and will be the default answer for the "LABEL DEVICE:" and "REPORT DEVICE:" prompts when signing into the module. At the device prompt(s), the user can:

- Accept the default answer that is defined.
- Enter another device to which output is to be directed.
- Enter 0 to get output on the computer screen.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For initial installation of the Inpatient Medications V. 5.0 software package, please refer to the *Computerized Patient Record System (CPRS) Installation Guide*.

## Inpatient Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the parameters that are used in defining the functions that affect the entire Inpatient Medications package for the site. Please consult the Supervisor's Manual for more detail on the use of these options.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/002.png)Note: The Inpatient Site file (#59.4) is no longer used by the Inpatient Medications package.

To edit these parameters from the IV Medications module, use the following menu path:

*IV Menu* \[PSJI MGR\]

*SUPervisor's Menu* (IV) \[PSJI SUPERVISOR\] (Locked: PSJI MGR)

*AUto-Discontinue Set-Up* \[PSJ AC SET-UP\]

*SIte Parameters (IV)* \[PSJI SITE PARAMETERS\]

To edit these parameters from the Unit Dose Medications module, use the following menu path:

*Unit Dose Medications* \[PSJU MGR\]

*Supervisor's Menu* \[PSJU FILE\] (Locked: PSJU MGR)

*PARameters Edit Menu* \[PSJ PARAM EDIT MENU\]

### Fields from the PHARMACY SYSTEM File (#59.7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- SITE NAME - This is the name of the site using the pharmacy packages. Because of the nature of this file and the fact that all the Pharmacy packages use this file, it is very important that only one site name ever be entered into this file. Sites must not edit fields or make local field additions to the PHARMACY SYSTEM file (#59.7).
- FROM WARD - This is the ward the patient has been transferred from whenever an action is to take place (e.g., placing orders on hold, discontinuing orders). For each FROM WARD, there are the following fields:
- TO WARD - Whenever a patient is transferred from the previously selected From Ward to a ward selected here as a TO WARD, the patient's IV and Unit Dose orders are discontinued.
- 'ON PASS' ACTION - This is the action the Inpatient Medications package will take on a patient's orders whenever the patient is transferred from the selected From Ward to "Authorized Absence less than 96 hours" (known as On Pass). If PLACE ORDERS ON HOLD is chosen, the patient's orders will be taken off of hold whenever the patient returns.
- ACTION ON AUTHORIZED ABSENCE - This is the action that is to take place on a patient's Inpatient (Unit Dose and IV) Medications orders whenever the patient is transferred from the selected FROM WARD to AUTHORIZED ABSENCE. If PLACE ORDERS ON HOLD is selected, the orders will automatically be taken off of hold when the patient returns.
- ACTION ON UNAUTHORIZED ABSENCE - This is the action that is to take place on a patient's Inpatient (Unit Dose and IV) Medications orders whenever the patient is transferred from the selected FROM WARD to UNAUTHORIZED ABSENCE. If PLACE ORDERS ON HOLD is selected, the orders will automatically be taken off of hold when the patient returns.
- FROM SERVICE - This is the service the patient has been transferred from whenever the patient's Inpatient Medications (IV and Unit Dose) orders are to be discontinued. For each FROM SERVICE, there is the following field:
- TO SERVICE - Whenever a patient is transferred from the previously selected From Service to a service selected here as a TO SERVICE, the patient's IV and Unit Dose orders are discontinued.
- NON-FORMULARY MESSAGE - This is a message that will be shown to non-pharmacists when they order drugs not currently stocked by the pharmacy. This is typically a warning, and describes a procedure the non-pharmacist must follow before the pharmacy will dispense the non-formulary drug.
- EDIT Option - This option is used to edit the NON-FORMULARY MESSAGE above.
- PRINT 6 BLOCKS FOR THE PRN MAR - This field is used to indicate if 4 or 6 blocks are to be used for ONE-TIME/PRN (pro re nata – Latin for "as needed") orders on the 7/14 DAY MAR ONE-TIME/PRN SHEET. The 7/14 DAY MAR ONE-TIME/PRN SHEET will print 4 blocks if this field is <u>not</u> set to YES.
- PRINT DIET ABBR LABEL ON MAR - If this field contains a 1 or YES, the Dietetics Abbreviated Label will be printed on the MAR.
- MAR SORT - If this field contains a 0, the MAR will be sorted by the order's Schedule Type\* and then by Medication Names. When this field contains a 1, the MAR will be sorted by the order's Medication Names.

\* Schedule Type is sorted based on the following orders:

Continuous MAR One-Time/PRN MAR

---------------------------------- ------------------------------------

Unit Dose Orders: Unit Dose Orders:

Continuous One-time

Fill on Request PRN

IV Orders: IV Orders:

Piggyback or Syringe type One-time

Admixture type PRN

Hyperal type Acknowledged Pending PRN orders

Chemo type

Acknowledged Pending Orders:

Inpatient Meds

IV fluids

- ATC SORT PARAMETER - This parameter allows sending of the Pick List to the Automated Tablet Counter (ATC) machine by ATC mnemonic or admin time within patient.
- CALC UNITS NEEDED PRN ORDERS - This field controls whether or not the units needed will be calculated for the orders with PRN in the SCHEDULE field (#26) of the UNIT DOSE sub- file (#55.06) of the PHARMACY PATIENT file (#55) on the Pick List. This information will show on the Pick List if this field is set to 1.
- DAYS UNTIL STOP FOR ONE-TIME - This field indicates the number of days a one-time order should last. This field is only used if the ward parameter, DAYS UNTIL STOP FOR ONE-TIME, is not defined. This number can be between 1 and 30.
- ROUND ATC PICK LIST UNITS – This field allows the site to decide whether or not fractional units per dose will be rounded to the next whole number before the pick list is sent to the ATC.
- HOURS OF RECENTLY DC/EXPIRED– This field allows the INPATIENT MEDICATIONS profiles to display the recently discontinued/expired orders that fall within the number of hours specified. The value of this field is a number between 1 and 120. If no value is found for this parameter, a default value of 24 hours will be assumed by the software. The SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option should be used to enter/edit values for this parameter.
- EXPIRED IV TIME LIMIT – This is the maximum number of hours after a continuous IV order expires that it may still be renewed. The value of the parameter is a number between 0 and 24, inclusive.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/003.png)Note: The "AUTO-DC IMO ORDERS:" field has been moved from the PHARMACY SYSTEM file (#59.7) to the CLINIC DEFINITION file (#53.46). To access this field, use the *Clinic Definition* \[PSJ CD\] option under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option.

### Fields from the INPATIENT WARD PARAMETERS File (#59.6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/004.png)Note: Fields from the Inpatient WARD PARAMETERS file (#59.6) are still edited through the Inpatient Medications package.

- WARD - This is a ward for which the site wants to tailor specific aspects of the Inpatient Medications package.
- DAYS UNTIL STOP DATE/TIME - This is the number of days a standard order should last. The first order entered for a patient uses this number to calculate a default value for the order's STOP DATE/TIME field (#34) of the UNIT DOSE sub-file (#55.06) of the PHARMACY PATIENT file (#55). This number is also used if SAME STOP DATE ON ALL ORDERS parameter has no entry, or an entry of NO.
- DAYS UNTIL STOP FOR ONE-TIME - This is the number of days a one-time order should last. The number can be from 1-100; however, it cannot exceed the number of days that standard orders last (DAYS UNTIL STOP DATE/TIME). When this parameter is not available, the system parameter, DAYS UNTIL STOP FOR ONE-TIME, will be used to determine the stop date. When neither parameter has been set, one-time orders will use the ward parameter, DAYS UNTIL STOP DATE/TIME, to determine the stop date instead of the start and stop date being equal.
- SAME STOP DATE ON ALL ORDERS - This flag, if set to YES, uses the STOP DATE/TIME field (#34) of the UNIT DOSE sub-file (#55.06) of the PHARMACY PATIENT file (#55) from the patient's first order as a default value for these fields on all of the patient's following orders.
- TIME OF DAY THAT ORDERS STOP - This is a time of day that, if found, is used in calculating the default value for the STOP DATE/TIME field (#34) of the UNIT DOSE sub-file (#55.06) of the PHARMACY PATIENT file (#55) of patients' orders. This time is in military time format with leading and trailing zeros (0001 means 1 minute after midnight).
- DEFAULT START DATE CALCULATION – When an order originates in CPRS and a duration accompanies the order, this field is used to calculate the Calc Start Date/Time. Otherwise, this field allows the ward to determine how the default Start date for orders should be calculated. The default may use the NEXT ADMIN TIME, the CLOSEST ADMIN TIME, or the login date/time of the order (NOW) as the default Start Date for Unit Dose and IV orders.
- START TIME FOR 24-HOUR MAR - This is the start time for the 24-hour MAR. It is used whenever a user enters a start date without a time when running the 24-hour MAR. This time is in military time format with leading and trailing zeros (0001 means 1 minute after midnight).
- LABEL FOR WARD STAFF - The following codes are used to select when labels will print for ward staff:
- NO LABELS - Labels are not created when ward staff (nurses, clerks, physicians, etc.) take action on an order. Labels are always created for actions taken on orders after they are verified, unless NO LABELS is selected.
- FIRST LABEL ON ORDER ENTRY/EDIT - Labels are created whenever ward staff enter an order or edit a non-verified order, but not when the nurse verifies an order.
- FIRST LABEL ON NURSE VERIFICATION - Labels are not created for ward staff until a nurse has verified the order.
- LABEL ON ENTRY/EDIT AND VERIFICATION - Labels are created whenever the order is entered or edited and verified.
- WARD LABEL PRINTER - If a device name is entered here, labels created by ward staff, due to actions taken on orders, will print automatically to the device.
- LABEL FOR PHARMACY - The following codes are used to select when labels will print for the pharmacy staff:
- NO LABELS - Labels will not be created when the pharmacy staff (pharmacists and pharmacy technicians) takes action on an order.
- FIRST LABEL ON ORDER ENTRY/EDIT - Labels will be created whenever the pharmacy staff enters an order or edits a non-verified order, but not when the pharmacist verifies an order.
- LABEL ON ENTRY/EDIT AND VERIFICATION - Labels are created whenever the order is entered or edited and verified.
- FIRST LABEL ON PHARMACIST VERIFICATION - Labels will not be created for the pharmacy staff until a pharmacist has verified the order.
- PHARMACY LABEL PRINTER - If a device name is entered here, labels created by the pharmacy staff, due to actions taken on orders, will print automatically to the device.
- LABEL ON AUTO-DISCONTINUE - This is used to determine if labels should be created when orders for a patient from this ward are auto-discontinued (d/c) due to a patient movement. Patient movements include discharges and transfers. Labels are created for the ward on which the patient resided before the move took place.
- MAR HEADER LABELS - This is used to determine if MAR header labels should be generated when orders are processed for patients.
- DAYS NEW LABELS LAST - The Unit Dose Medications module runs a background job once a day that deletes all unprinted new labels older than the number of days specified here. If no days are specified for this field, any unprinted new labels for this site will be purged at the end of the day.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/005.png)Note: A label can still be printed for an order even though its new label record has been purged.

- MAR ORDER SELECTION DEFAULT - This identifies the default for the type of orders to be included on MARs printed for this ward. All Medication, Non-IV medications only, IV piggybacks, admixtures, hyperals, and/or IV chemotherapy medication types may be selected. Multiple types may be specified.
- PRINT PENDING ORDERS ON MAR - This is used to determine if pending orders, that were acknowledged by a nurse, should be included on the MARs and the Medication Due Worksheet.
- 'SELF MED' IN ORDER ENTRY - If the word YES (or a 1) is entered here, the regular order entry process will prompt the user for SELF MED and HOSPITAL SUPPLIED SELF MED for each order entered. The abbreviated processes, ward order entry, and order sets are not affected in any way by this site parameter.
- PRE-EXCHANGE REPORT DEVICE – This is the device that is used as a default for the Pre-Exchange Report. If the value is null, the user will not be prompted for a device, which will disable the printing of this report for that ward. At the time the report is run, if the user enters an output device that is different from the device in this file, the option to override this parameter and define a temporary device for the remainder of this session is displayed. For Clinic Orders, "HOME" is the default printer when no default device is defined in the Clinic Definition file. The last inpatient location is not used in determining the correct default pre-exchange printer. The user may select the default device when printing the Pre-Exchange Report upon finishing a new order.
- STAT NOW MAIL GROUP – This is the name of the mail group to be used for STAT/NOW active order notifications for this ward.
- PRIORITIES FOR NOTIFICATION – This is the priorities /schedules for notification for this ward. The value may be selected for the priorities / schedules for notifications to be sent to the mail group defined in the STAT NOW MAIL GROUP field (#5) mentioned above. This parameter may be empty / not defined, or it may be set via this option: INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\].
- HOURS OF RECENTLY DC/EXPIRED – This field allows the Inpatient Medications profiles to display the recently discontinued/expired orders that fall within the number of hours specified. The value of this field is a number between 1 and 120. No default will be provided; the parameter may be empty or not defined, and it may be set via the INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option. The value defined in this field will take precedence over the Inpatient System parameter.

### Fields from the INPATIENT USER PARAMETERS File (#53.45)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/006.png)Note: Fields from the Inpatient USER PARAMETERS file (#53.45) are still edited through the Inpatient Medications package.

- INPATIENT USER - This is a user for whom the Inpatient Medications package can be tailored.
- ALLOW USER TO RENEW ORDERS - If this field is set to YES, this ward clerk/pharmacy technician can actually renew patients' inpatient orders. If this is set to NO (or is not set), this clerk/technician can only mark orders for renewal by another user.
- ALLOW USER TO HOLD ORDERS - If this field is set to YES, this ward clerk/pharmacy technician can actually place patients' inpatient orders on hold or take orders off of hold. If this is set to NO (or is not set), this clerk/technician can only mark orders for hold and take off of hold.
- ALLOW USER TO D/C ORDERS - If this field is set to YES, this ward clerk/pharmacy technician can actually discontinue patients' inpatient orders. If this is set to NO (or is not set), this clerk/technician can only mark orders to be discontinued by another user.
- MAY SELECT DISPENSE DRUGS - Unless the user is a pharmacist, the user can select only Orderable Items during the Unit Dose order entry process. A YES answer will allow the non-pharmacist user to select Dispense Drugs during order entry.
- ALLOW AUTO-VERIFY FOR USER - This is used to determine if the user can enter Unit Dose orders as active, allowing the user to skip the step of manually verifying those orders entered by this user.
- ORDER ENTRY PROCESS - This is the type of order entry process to be used by this user.
- Regular - Order entry is the full set of prompts for the entry of an order, after which the user is shown a full view of the order and allowed to take immediate action on the order.
- Abbreviated - Order entry gives the user fewer prompts for the entry of an order, after which the user is shown a full view of the order and is allowed to take immediate action on the order.
- Ward - Order entry gives the user the same prompts as the abbreviated order entry, but then gives a brief view of the entered order and does not allow immediate action to be taken on the order.

> ![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/007.png)Note: No entry here is the same as selecting Regular order entry.

- PRINT PROFILE IN ORDER ENTRY - If this field is set to YES, the user will be given the opportunity to print a patient profile after entering Unit Dose orders for the patient.
- LABEL PRINTER POINTER - This is a device to which labels created by this user will print. If a device is entered here, it will be used instead of any device selected for the ward or pharmacy to print labels.
- USE WARD LABEL SETTINGS - This allows the pharmacist (or pharmacy technician) working on the ward(s) to use the label settings defined for the ward(s) instead of the label settings defined for the pharmacy.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/008.png)Note: When a label printer is defined for the user, that printer will always be used to print labels instead of either the ward or pharmacy label printer.

- INPATIENT PROFILE ORDER SORT - This is the sort order in which the Inpatient Profile will show inpatient orders. The options will be sorted either by medication or by start date of order. Entering the words "Medication Name" (or the number 0) will show the orders within schedule type (continuous, one-time, and then PRN) and then alphabetically by drug name. Entering the words "Start Date of Order" (or the number 1) will show the order chronologically by start date, with the most recent dates showing first and then by schedule type (continuous, one-time, and then PRN).

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/009.png)Note: The Inpatient Profile first shows orders by status (active, non-verified and then non-active).

### Fields from the IV ROOM File (#59.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/010.png)Note: Fields from the IV ROOM file (#59.5) are still edited through the Inpatient Medications package.

- IV ROOM NAME - This is the arbitrary name of an IV room. A site can have more than one name defined. Each IV order belongs to the IV room that input the order. An IV room can process only orders that belong to that IV room.
- LENGTH OF LABEL - The labels can vary in height from 12 to 66 lines. Measure the height of the label and multiply that height by the number of lines per inch for which the printer is configured.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/011.png)Note: If all lines of print cannot fit within the length that is defined here, the lines of print will continue to the next label. For example, the average piggyback label is three inches high. If the printer will print 6 lines per inch, the number 18 should be entered as the answer to this parameter.

- WIDTH OF LABEL - Enter the maximum allowable width of the label in number of characters. If data is not entered into this field, the default will be 30. If a line of print cannot fit within the width defined here, it will continue on the next line of the label.
- LINE FEEDS BETWEEN LABELS - Enter a number between 0 and 6. This is the number of line feeds between each IV label. This parameter makes it possible to have a top and bottom margin on the IV labels.
- END OF LABEL TEXT - Enter any "end of label" text that is wanted to print at the bottom of every IV label. Separate the lines with an up-arrow (^). For example, to have this phrase print at the bottom of the IV labels:

RETURN TO IV ROOM IN 24-HOURS

FILLED BY: \_\_\_\_ CHECKED BY: \_\_\_\_

The user must enter the following characters:

> RETURN TO IV ROOM IN 24-HOURS^FILLED BY: \_\_\_\_

> CHECKED BY: \_\_\_\_

- HEADER LABEL - When set to YES, an extra label is generated to record lot numbers and provide a record for new orders entered since the last printing of the active order list. This extra label, together with the active order list, provides a paper backup system in the event the computer system becomes unavailable to the user.
- SHOW BED LOCATION ON LABEL - The patient's ward location is always printed on the IV label. However, if bed location information is available and the user wishes to have this additional information on the label, enter YES or the number 1 in this field.
- USE SUSPENSE FUNCTIONS - If the user wants the SUSPEND LABELS as a valid choice at the "ACTION:" prompt after order entry, respond with the number 1. If the user does not want any labels suspended after order entry, but rather have them printed, respond with the number 0.
- DOSE DUE LINE - This parameter affects the printing of the dose due line on the IV label. If the number 0 is entered, the time the dose is due will not be printed on the IV label. The dose due line will be printed for Intravenous Piggybacks (IVPBs) only if the number 1 is selected, Large Volume Parenterals (LVPs) dose due line will be printed if the number 2 is selected and both IVPBs and LVPs if the number 3 is selected.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/012.png)Note: LVPs include HYPERAL type orders.

- LVPS GOOD FOR HOW MANY DAYS - This number is one of the parameters used when the stop date of a new LVP order is computed. The computed stop date is the least of this parameter, the NUMBER OF DAYS FOR IV ORDER field (#3) in the IV ADDITIVES file (#52.6), and the DAY (nD) or DOSE (nL) LIMIT field (#.05) in the PHARMACY ORDERABLE ITEM file (#50.7) for the orderable item associated with this order. For example, if large volume IVs are good for 14 days and a new order is input with a start date of today, the stop date is T+14. If the same order contained an additive or orderable item defined for 10 days, the stop date is T+10.
- HYPERAL GOOD FOR HOW MANY DAYS - This number is one of the parameters used when the stop date of a new hyperal order is computed. The computed stop date is the least of this parameter, the NUMBER OF DAYS FOR IV ORDER field (#3) in the IV ADDITIVES file (#52.6), and the DAY (nD) or DOSE (nL) LIMIT field (#.05) in the PHARMACY ORDERABLE ITEM file (#50.7) for the orderable item associated with this order. For example, if a hyperal order is good for 14 days and a new order is input with a start date of today, the stop date is T+14. If the same order contained an additive or orderable item defined for 10 days, the stop date is T+10.
- PBS GOOD FOR HOW MANY DAYS - This number is one of the parameters used when the stop date of a new piggyback order is computed. The computed stop date is the least of this parameter, the NUMBER OF DAYS FOR IV ORDER field (#3) in the IV ADDITIVES file (#52.6), and the DAY (nD) or DOSE (nL) LIMIT field (#.05) in the PHARMACY ORDERABLE ITEM file (#50.7) for the orderable item associated with this order. For example, if a piggyback order is good for 14 days and a new order is entered today, the stop date is T+14. If the same order contained an additive or orderable item defined for 10 days, the stop date is T+10.
- SYRNS GOOD FOR HOW MANY DAYS - This number is one of the parameters used when the stop date for the IV syringe order is computed. The computed stop date is the least of this parameter, the NUMBER OF DAYS FOR IV ORDER field (#3) in the IV ADDITIVES file (#52.6), and the DAY (nD) or DOSE (nL) LIMIT field (#.05) in the PHARMACY ORDERABLE ITEM file (#50.7) for the orderable item associated with this order.
- CHEMO'S GOOD FOR HOW MANY DAYS - This number is one of the parameters used to determine the stop date for chemotherapy IV orders. The computed stop date is the least of this parameter, the NUMBER OF DAYS FOR IV ORDER field (#3) in the IV ADDITIVES file (#52.6), and the DAY (nD) or DOSE (nL) LIMIT field (#.05) in the PHARMACY ORDERABLE ITEM file (#50.7) for the orderable item associated with this order.
- STOP TIME FOR ORDER - Enter, in military time, the time of the day that the automatic stop of orders should occur.
- EXPIRE ALL ORDERS ON SAME DAY - Enter the number 1 to stop all IV orders automatically on the same day. The day the orders are stopped will be the stop date of the first active IV order found in the file. The stop date that is found will be shown as a default for the stop date of the IV ORDER.
- ACTIVITY RULER - The activity ruler provides a visual representation of the relationship between coverage times, doses due, and order start times. The intent is to provide the on-the-floor user with a way to track activity in the IV room and determine when to call for doses before the normal delivery.
- TOTAL VOL. ON HYPERAL LABELS - Enter the number 1 or YES if the total volume of solutions and additives are to be displayed on all hyperal labels.
- Select START OF COVERAGE - Enter the military time that designates the first administration time covered by this manufacturing run. In other words, if the previous manufacturing period covered up to and included the 0900 dose, the start of coverage would begin at 0901. For each START OF COVERAGE, there are the following fields:
- TYPE - Enter the IV type for this start of coverage period. The user can enter only one type for each period that is defined.
- DESCRIPTION - A description for each delivery time (3 to 30 characters) can be entered. The user will be prompted with a default description. This description will appear when manufacturing records and ward lists are requested. Using the default prompt will help lead to less confusion for the users.
- END OF COVERAGE - Enter the military time that designates the last administration time covered by this manufacturing run. Enter midnight as 2400.
- MANUFACTURING TIME - Enter the military time that designates the general time when the manufacturing list will be run and the orders prepared. This is for documentation and does not affect IV processing. Enter midnight as 2400.
- DELIVERY TIME - Delivery time must be entered using a 24-hour clock (e.g., 9 <span class="smallcaps">AM</span> is entered as 0900). Delivery time is used as a default start time for admixtures and hyperalimentations. Enter midnight as 2400.
- LABEL DEVICE - Enter the name that is used most frequently as the label device for this IV room. This field displays as the default for the "Current IV LABEL device is:" prompt when signing into the IV software.
- REPORT DEVICE - Enter the PROFILE device number or name that will be used most frequently by this IV room. This field displays as the default for the "Current IV REPORT DEVICE:" prompt when signing into the IV software.
- INACTIVATION DATE - This is used to place an IV room out of service. Once the inactive date is reached, the IV room will no longer be selectable in IV Order Entry options.
- DAYS TO RETAIN IV STATS - This is used to allow the site to specify the number of days to keep data in the IV STATS file (#50.8).
- DC'D IV ORDERS HOURS FILTER - This field provides a filter for the D/C'd orders report. Discontinued IV orders older than the entered number of hours will not be included in the report. By entering a zero in this field, no D/C'd or edited orders will appear in the report.

### Fields from the CLINIC DEFINITION File (#53.46)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/013.png)Note: This file was formerly named the CLINIC STOP DATES file (#53.46)

- CLINIC – This is the Outpatient clinic for which the site wishes to define a stop date. The clinic should allow the ordering of Inpatient Medications for Outpatients (IMO).
- NUMBER OF DAYS UNTIL STOP – The number of days to be used to calculate the stop date for orders placed in the specified clinic. This only affects stop date calculations for Inpatient Medication Orders for Outpatients. Enter a value from 1-365 or null. If no answer is specified and no other calculation is in place for the stop date, 14 days will be used.
- AUTO-DC IMO ORDERS – This field allows the site to specify, by clinic, whether or not orders placed for Outpatients are auto-dc'd upon admission, discharge, ward transfer, or treating specialty change. If this field is set to YES or null, IMO orders will be auto-dc'd whenever any of these events occurs. If this field is set to NO, no IMO orders will be auto‑dc'd on any type of patient movement.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/014.png)Note: This field is only used if the auto-dc parameters in Inpatient Medications are controlling the movement actions. Otherwise, this field would be ignored.

- SEND TO BCMA? – This field allows the site to define, by clinic, whether or not IMO orders should be available in BCMA. Allows YES, NO or null answer. Only orders from clinics marked with a YES will be sent to BCMA. For example, if the patient is admitted, an IMO order is active, and the SEND TO BCMA field is a YES, that order will be included in the information transmitted to BCMA.
- CLINIC MISSING DOSE REQUEST PRINTER – This field allows the site to specify a clinic-specific Clinic Orders Missing Dose Request printer. When a missing dose is created for a clinic order, the system will first look in the CLINIC DEFINITION (#53.46) file, and if it finds a clinic-specific Clinic Orders Missing Dose Request Printer definition, it will use it. If it does not find a Clinic Orders Missing Dose Request Printer definition for a particular clinic, it will use the BCMA GUI Parameter division Clinic Orders Missing Dose Request Printer parameter. If the system does not find a clinic-specific Clinic Orders Missing Dose Request Printer definition or a division Clinic Orders Missing Dose Request Printer parameter, it will use the current BCMA GUI Parameter for Inpatient Missing Dose Requests Printer for printing of Clinic Orders missing dose requests.
- PRE-EXCHANGE REPORT DEVICE – This field allows the site to specify a clinic-specific clinic default printer device for a clinic as defined in the CLINIC DEFINITION file (#53.46). If no default device is defined in the CLINIC DEFINITION file (#53.46), "HOME" is selected as the default printer. The last inpatient location is not used in determining the correct default pre-exchange printer. The user may select the default device when printing the PRE-Exchange Report upon finishing a new order.
- <span id="CLINIC_APPT_DATE_RANGE_MIN" class="anchor"></span>CLINIC APPT DATE RANGE MIN: The number of days to search for past appointments when entering a clinic order. If not specified, the default period of 90 days (3 months) will be used. Appointments will display with dates between CLINIC APPT DATE RANGE MIN and CLINIC APPT DATE RANGE MAX.
- <span id="CLINIC_APPT_DATE_RANGE_MAX" class="anchor"></span>CLINIC APPT DATE RANGE MAX: The number of days to search for future appointments when entering a clinic order. If not specified, the default period of 365 days (1 year) will be used. Appointments will display with dates between CLINIC APPT DATE RANGE MIN and CLINIC APPT DATE RANGE MAX.
- IMO DC/EXPIRED DAY LIMIT: Enter number of days that DC/Expired clinic orders will be included in the enhanced order checks for drug interaction and therapeutic duplications. If this field is left blank, a default value of 30 days will be used; otherwise sites can define this field to be a number from 1–120 to represent the number of days that DC/EXPIRED IMO orders should be included in Order Checks.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/015.png)Note: This field is only used for clinic orders in Inpatient Medications. Otherwise, this field would be ignored.

### Fields from the IV MEDICATION ORDERS DC'D File (#52.75)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- DATE/TIME D/C – This field allows the site to enter the date/time that an order was edited or discontinued through CPRS. The data are copied from an HL7 message that is processed through the protocol OR EVSEND PS.
- SIG – This field allows the site to enter the dosage that was entered in CPRS for the IV Order. the dosage entered must be 1 – 100 characters in length.
- PATIENT – This field allows the site to enter the patient for which the order was D/C'd or edited in CPRS.
- DRUG – This field allows the site to enter the pharmacy orderable item associated with the order. This field is a pointer to the PHARMACY ORDERABLE ITEM file and is copied from the IV order entered in CPRS.
- ROOM-BED – This field allows the site to enter the room-bed of the patient related to the order. If no room-bed is present int eh HL7, the value will be 9999. The value entered must be 1 – 20 characters in length.
- WARD – This field allows the site to enter the name of the ward in which the patient is currently admitted. The value entered must be 1 – 20 characters in length.
- WARD IEN – This field allows the site to enter the hospital location in which the patient is currently admitted. This field is a pointer to the HOSPITAL LOCATION File (#44) and points to the ward in which the patient is currently admitted.
- PS ORDER IEN – This field allows the site to enter the order IEN within the PHARMACY PATIENT file (#55). The value entered must be 1 – 10 characters in length and must be nnV, with V denoting an IV order for the patient pdfn within the PHARMACY PATIENT file (#55) as follows: ^PS(55,pdfn,"IV",nn,
- WARD GROUP – This field allows the site to enter the ward group of the patient's admission ward. This field is a pointer to the WARD GROUP file (#57.5).
- STATUS – This field allows the site to enter the status of the pharmacy order as it was received. Only two status will be stored in this field: XO (changed) or DC (discontinued). In instances where no status is transferred, none are stored.

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Option Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the users are assigned the primary menu options of *Unit Dose Medications* \[PSJU MGR\] option and/or *IV Menu* \[PSJI MGR\] option, it is necessary to give the appropriate security keys to each user as required.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/016.png)Note: The security key PSJU RPH is no longer used.

The following security keys do <u>not</u> lock any options: however, they are used to identify the type of user:

- PSJ PHARM TECH This key identifies the user as a pharmacy technician.
- PSJ RNURSE This key identifies the user as a nurse and gives them access to verify orders.
- PSJ RPHARM This key identifies the user as a pharmacist and gives them access to verify orders.

The following security keys give the user access to certain order actions:

- PSJ RNFINISH This key can only be granted to holders of the PSJ RNURSE key. It allows the holder to enter a Dispense Drug and to finish Unit Dose orders.
- PSJI PHARM TECH This key allows the holder to finish IV orders.
- PSJI RNFINISH This key can only be granted to holders of the PSJ RNURSE key. It allows the holder to finish IV orders.

The following security keys do lock options and give the user certain access capabilities:

- PSJI MGR Locks the *IV Menu* \[PSJI MGR\] option. This key allows access to the supervisor functions necessary to run the IV Medications package, and should be given to the Inpatient coordinator.
- PSJI PURGE This key gives access to the purge IV functions, which allows the purging of expired orders. This key should be given to the Inpatient coordinator.
- PSJU MGR This key allows the editing of basic background files needed to run the Unit Dose package, and various management reports. This key should be given to the Unit Dose package coordinator and/or Inpatient supervisor.
- PSJU PL This key allows the user to have access to the Unit Dose Medications PICK LIST options and functions.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Affairs (VA) FileMan file access codes are used sparingly by the Inpatient Medications package. Only the following codes are given:

- Every file sent with the package is given a Data Dictionary (DD) access code of "@".
- IV STATS (#50.8), ACTIVITY LOG REASON (#53.3), PICK LIST (#53.5), UNIT DOSE PICK LIST STATS (#57.6), INPATIENT WARD PARAMETERS (#59.6), files are all given Write (WR), Learn as you go (LAYGO), and Delete (DEL) access codes of ^.
- No code is given for the Read (RD) access of any of the files. Anyone may print the data from any of the files.

No other access codes are given. Sites may add their own codes as they see fit, but it is highly recommended that they *do not* change the codes that are sent with the package.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/017.png)Note: Please refer to page 432 of Kernel V. 8.0 Systems Manual concerning installation of security codes entitled "Sending Security Codes."

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 50.2 IV CATEGORY

> 50.8 IV STATS

> 51.15 ADMINISTRATION SHIFT

> 52.75 IV MEDICATION ORDERS DC'D

> 53.1 NON-VERIFIED ORDERS

> 53.2 UNIT DOSE ORDER SET

> 53.3 ACTIVITY LOG REASON

> 53.4 PRE-EXCHANGE NEEDS

> 53.41 MAR LABELS

> 53.42 INPATIENT BACKGROUND JOB

> 53.43 MISCELLANEOUS REPORT FILE

> 53.44 PHYSICIANS' ORDERS

> 53.45 INPATIENT USER PARAMETERS

> 53.46 CLINIC DEFINITION

> 52.54 CLOZAPINE OVERRIDE REASONS

> 53.5 PICK LIST

> 53.55 UNIT DOSE/ATC MEDS

> 53.8 CLOZAPINE MEDICATION OVERRIDES

> 57.5 WARD GROUP

> 57.6 UNIT DOSE PICK LIST STATS

> 57.7 MEDICATION ADMINISTERING TEAM

> 57.8 CLINIC GROUP

> 58.6 PADE INBOUND TRANSACTIONS

> 58.601 PADE INVENTORY SYSTEM

> 58.63 PADE DISPENSING DEVICE

> 58.64 PADE USER

> 58.7 PADE SYSTEM SETUP

> 58.71 PADE SEND LOCATION

> 59.5 IV ROOM

> 59.6 INPATIENT WARD PARAMETERS

Example: How to Print File Information Using VA FileMan

VA FileMan 22.0

Select OPTION: 8 DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: INPATIENT USER PARAMETERS// \<Enter\>

GO TO WHAT FILE: INPATIENT USER PARAMETERS // \<Enter\>

Select SUB-FILE: \<Enter\>

Select LISTING FORMAT: STANDARD// \<Enter\>

DEVICE: *\[Enter Print Device Here\]* RIGHT MARGIN: 80// \<Enter\>

The file's DD will now print on the user-specified device.

## Unit Dose File Diagram 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Microsoft's latest version of Word, the user will not be able to see the File Diagram below if viewing this document electronically, unless the user is in Page Layout view. To switch to Page Layout, select View from the Word menu above and then select Page Layout. The entire manual can be viewed in this format.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/018.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/019.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/020.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/021.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/022.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/023.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/024.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/025.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/026.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/027.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/028.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/029.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/030.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/031.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/032.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/033.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/034.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/035.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/036.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/037.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/038.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/039.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/040.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/041.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/042.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/043.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/044.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/045.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/046.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/047.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/048.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/049.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/050.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/051.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/052.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/053.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/054.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/055.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/056.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/057.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/058.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/059.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/060.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/061.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/062.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/063.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/064.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/065.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/066.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/067.png)

## IV File Diagram 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Microsoft's latest version of Word, the user will not be able to see the File Diagram below if viewing this document electronically unless the user is in Page Layout view. To switch to Page Layout, select View from the Word menu above and then select Page Layout. The entire manual will be viewed in this format.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/068.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/069.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/070.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/071.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/072.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/073.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/074.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/075.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/076.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/077.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/078.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/079.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/080.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/081.png)![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/082.png)

(*This page included for two-sided copying*.)

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\* IMPORTANT \*\*

> A routine name followed by an asterisk (such as PSJ\*) is used to designate the complete set of the routines that start with those characters.

## Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are exported by the Inpatient Medications package. Routine names starting with the letters PSG designate routines used mainly by the Unit Dose Medications module. Routine names starting with the letters PSIV designate routines used mainly by the IV Medications module. Routine names starting with the letters PSJ designate Inpatient Medications routines - utilities used by IV, Unit Dose, and other packages.

| PSGAH    | PSGAP0                                                 | PSGAPH                                                 | PSGAPIV  |
|----------|--------------------------------------------------------|--------------------------------------------------------|----------|
| PSGAP    | PSGAXR                                                 | PSGBRJ                                                 | PSGCAP   |
| PSGAPP   | PSGCAPIV                                               | PSGCAPP                                                | PSGCAPP0 |
| PSGCAP0  | PSGDCC                                                 | PSGDCCM                                                | PSGDCR0  |
| PSGCT    | PSGDCT1                                                | PSGDCTP                                                | PSGDL    |
| PSGDCT   | PSGDS0                                                 | PSGDSP                                                 | PSGDSP0  |
| PSGDS    | PSGDSPN                                                | PSGEUD                                                 | PSGEUDD  |
| PSGDSP1  | PSGFILD0                                               | PSGFILD1                                               | PSGFILD2 |
| PSGEUDP  | PSGFILED                                               | PSGGAO                                                 | PSGIU    |
| PSGFILD3 | PSGL0                                                  | PSGLBA                                                 | PSGLH    |
| PSGL     | PSGLPI                                                 | PSGLW                                                  | PSGMAR   |
| PSGLOI   | PSGMAR1                                                | PSGMAR2                                                | PSGMAR3  |
| PSGMAR0  | PSGMIV                                                 | PSGMMAR                                                | PSGMMAR0 |
| PSGMI    | PSGMMAR2                                               | PSGMMAR3                                               | PSGMMAR4 |
| PSGMMAR1 | PSGMMARH                                               | PSGMMIV                                                | PSGMMIVC |
| PSGMMAR5 | PSGNE3                                                 | PSGO                                                   | PSGOD    |
| PSGMUTL  | PSGOE0                                                 | PSGOE1                                                 | PSGOE2   |
| PSGOE    | PSGOE31                                                | PSGOE4                                                 | PSGOE41  |
| PSGOE3   | PSGOE5                                                 | PSGOE6                                                 | PSGOE7   |
| PSGOE42  | PSGOE81                                                | PSGOE82                                                | PSGOE9   |
| PSGOE8   | PSGOE92                                                | PSGOEC                                                 | PSGOECA  |
| PSGOE91  | PSGOEE                                                 | PSGOEE0                                                | PSGOEEW  |
| PSGOECS  | PSGOEF1                                                | PSGOEF2                                                | PSGOEH0  |
| PSGOEF   | PSGOEHA                                                | PSGOEI                                                 | PSGOEL   |
| PSGOEH1  | PSGOEM1                                                | PSGOENG                                                | PSGOEPO  |
| PSGOEM   | PSGOER0                                                | PSGOER1                                                | PSGOERI  |
| PSGOER   | PSGOES                                                 | PSGOESF                                                | PSGOETO  |
| PSGOERS  | PSGOEV                                                 | PSGOEVS                                                | PSGON    |
| PSGOETO1 | PSGORVW                                                | PSGOT                                                  | PSGOTR   |
| PSGORS0  | PSGP                                                   | PSGPEN                                                 | PSGPER   |
| PSGOU    | PSGPER1                                                | PSGPER2                                                | PSGPL    |
| PSGPER0  | PSGPL1                                                 | PSGPLD                                                 | PSGPLDP  |
| PSGPL0   | PSGPLDPH                                               | PSGPLF                                                 | PSGPLFM  |
| PSGPLDP0 | PSGPLPRG                                               | PSGPLR                                                 | PSGPLR0  |
| PSGPLG   | PSGPLUP                                                | PSGPLUP0                                               | PSGPLUTL |
| PSGPLRP  | PSGPO                                                  | PSGPOR                                                 | PSGPR    |
| PSGPLXR  | PSGPRVR0                                               | PSGRET                                                 | PSGRPNT  |
| PSGPRVR  | PSGSCT                                                 | PSGSCT0                                                | PSGSEL   |
| PSGS0    | PSGSETU                                                | PSGSH                                                  | PSGSICH  |
| PSGSET   | PSGSICH2                                               | PSGSICHK                                               | PSGSSP   |
| PSGSICH1 | PSGTAP0                                                | PSGTAP1                                                | PSGTCTD  |
| PSGTAP   | PSGTI                                                  | PSGVBW                                                 | PSGVBW0  |
| PSGTCTD0 | PSGVBWP                                                | PSGVBWU                                                | PSGVDS   |
| PSGVBW1  | PSGVW0                                                 | PSGVWP                                                 | PSIV     |
| PSGVW    | PSIVAL                                                 | PSIVALN                                                | PSIVALNC |
| PSIVACT  | PSIVAOR                                                | PSIVAOR1                                               | PSIVBCID |
| PSIVAMIS | PSIVARH                                                | PSIVARH1                                               | PSIVCHK  |
| PSIVCHK1 | PSIVCSED                                               | PSIVCAL                                                | PSIVDCR1 |
| PSIVDCR2 | PSIVDRG                                                | PSIVDCR                                                | PSIVEDT  |
| PSIVEDT1 | PSIVHIS                                                | PSIVEDRG                                               | PSIVHLP  |
| PSIVHLP1 | PSIVHLP2                                               | PSIVHLD                                                | PSIVHYP  |
| PSIVHYPL | PSIVHYPR                                               | PSIVHLP3                                               | PSIVLABR |
| PSIVLB   | PSIVLBDL                                               | PSIVLABL                                               | PSIVLBRP |
| PSIVLTR  | PSIVLTR1                                               | PSIVLBL1                                               | PSIVMAN1 |
| PSIVOC   | PSIVOCDS                                               | PSIVMAN                                                | PSIVOPT  |
| PSIVOPT1 | PSIVOPT2                                               | PSIVOE                                                 | PSIVORA1 |
| PSIVORAL | PSIVORC                                                | PSIVORA                                                | PSIVORC2 |
| PSIVORE  | PSIVORE1                                               | PSIVORC1                                               | PSIVOREN |
| PSIVORFA | PSIVORFB                                               | PSIVORE2                                               | PSIVORH  |
| PSIVORLB | PSIVORV1                                               | PSIVORFE                                               | PSIVPAT  |
| PSIVPCR  | PSIVPCR1                                               | PSIVORV2                                               | PSIVOD   |
| PSIVPR   | PSIVPRO                                                | PSIVPGE                                                | PSIVRD   |
| PSIVRDC  | PSIVREC                                                | PSIVQUI                                                | PSIVRP   |
| PSIVRP1  | PSIVRQ                                                 | PSIVRNL                                                | PSIVSET  |
| PSIVSP   | PSIVSPDC                                               | PSIVRQ1                                                | PSIVUTL  |
| PSIVUTL1 | PSIVUWL                                                | PSIVUDL                                                | PSIVWCR  |
| PSIVWCR1 | PSIVWL                                                 | PSIVVW1                                                | PSIVWRP  |
| PSIVXREF | PSIVXU                                                 | PSIVWL1                                                | PSJ59P5  |
| PSJAC    | PSJADM                                                 | PSJ53P1                                                | PSJADT0  |
| PSJADT1  | PSJADT2                                                | PSJADT                                                 | PSJAPIDS |
| PSJBCMA  | PSJBCMA1                                               | PSJALG                                                 | PSJBCMA3 |
| PSJBCMA4 | PSJBCMA5                                               | PSJBCMA2                                               | PSJBLDOC |
| PSJCLNOC | PSJCLOR                                                | PSJBCMA6                                               | PSJCLOR2 |
| PSJCLOR3 | PSJCLOR4                                               | PSJCLOR1                                               | PSJCOM   |
| PSJCOM1  | PSJCOMR                                                | PSJCLOR5                                               | PSJCROC  |
| PSJDCHK  | PSJDCU                                                 | PSJCOMV                                                | PSJDDUT2 |
| PSJDDUT3 | PSJDEA                                                 | PSJDDUT                                                | PSJDGAL2 |
| PSJDGCK  | PSJDIN                                                 | PSJDPT                                                 | PSJEEU   |
| PSJEEU0  | PSJDOSE                                                | PSJEXP                                                 | PSJEXP0  |
| PSJFTR   | PSJENV                                                 | PSJH1                                                  | PSJHEAD  |
| PSJHEH   | PSJGMRA                                                | PSJHL10                                                | PSJHL11  |
| PSJHL2   | PSJHIS                                                 | PSJHL4                                                 | PSJHL5   |
| PSJHL6   | PSJHL3                                                 | PSJHL9                                                 | PSJHLERR |
| PSJHLU   | PSJHL7                                                 | PSJHVARS                                               | PSJIBAG  |
| PSJLIACT | PSJHLV                                                 | PSJLIFNI                                               | PSJLIORD |
| PSJLIPRF | PSJLIFN                                                | PSJLIVFD                                               | PSJLIVMD |
| PSJLMAL  | PSJLIUTL                                               | PSJLMGUD                                               | PSJLMHED |
| PSJLMPRI | PSJLMDA                                                | PSJLMUDE                                               | PSJLMUT1 |
| PSJLMUT2 | PSJLMPRU                                               | PSJLOAD                                                | PSJLOI   |
| PSJMAI   | PSJLMUTL                                               | PSJMDIR                                                | PSJMDIR1 |
| PSJMDWS  | PSJMAI1                                                | PSJMISC                                                | PSJMISC2 |
| PSJMIV   | PSJMEDS                                                | PSJMP                                                  | PSJMPEND |
| PSJMPRT  | PSJMON                                                 | PSJMUTL                                                | PSJNEWOA |
| PSJNEWOC | PSJMPRTU                                               | PSJNTEG1                                               | PSJO     |
| PSJNTEG  | PSJNTEG0                                               | PSJO3                                                  | PSJOC    |
| PSJO1    | PSJO2                                                  | PSJOCDS                                                | PSJOCDSD |
| PSJOCDC  | PSJOCDI                                                | PSJOCOR                                                | PSJOCVAR |
| PSJOCDT  | PSJOCERR                                               | PSJOE1                                                 | PSJOEA   |
| PSJOE    | PSJOE0                                                 | PSJOEEW                                                | PSJOERI  |
| PSJOEA1  | PSJOEA2                                                | PSJOREN                                                | PSJORMA1 |
| PSJORAPI | PSJORDA                                                | PSJORP2                                                | PSJORPOE |
| PSJORMA2 | PSJORMAR                                               | PSJORREN                                               | PSJORRN  |
| PSJORRE  | PSJORRE1                                               | PSJORRO                                                | PSJORRN1 |
| PSJORUT2 | PSJORUTL                                               | PSJP                                                   | PSJPATMR |
| PSJPDCL  | <span id="P27_PSJPDCLU" class="anchor"></span>PSJPDCLU | <span id="P27_PSJPDCLV" class="anchor"></span>PSJPDCLV | PSJPDV0  |
| PSJPDV1  | PSJPDIR                                                | PSJPDV                                                 | PSJPR0   |
| PSJPST50 | PSJPL0                                                 | PSJPR                                                  | PSJQUTIL |
| PSJRXI   | PSJPXRM1                                               | PSJQPR                                                 |          |
|          | PSJSPU                                                 | PSJUTL5                                                |          |
|          |                                                        |                                                        |          |

The following routines are not used in this version of Inpatient Medications. They were exported in the initial Kernel Installation and Distribution System (KIDS) build as Delete at Site.

| PSGDCR   | PSGDCT0  | PSGEXP   | PSGEXP0  |
|----------|----------|----------|----------|
| PSGMMPST | PSGOROE0 | PSGORU   | PSGQOS   |
| PSIVNVO  | PSIVOEDO | PSIVOENT | PSIVOEPT |
| PSIVRD0  | PSIVRD0  | PSJMAN   | PSJOAC   |
| PSJOAC0  | PSJOE8   | PSJOE81  | PSJOEE   |
| PSJOER   | PSJOER0  | PSJORA   | PSJORIN  |
| PSJUTL   | PSJUTL1  | PSJUTL2  | PSJUTL3  |

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entry points provided by the Inpatient Medications package to other packages can be found in the External Relationships section of this manual. No other routines are designated as callable from outside of this package. Additional information on other external calls and their entry points can be found on the VA Software Document Library (VDL). Under the Clinical Section select the Pharm: Inpatient Medications page and then select the "API Manual - Pharmacy Reengineering (PRE)".

### Deleting Inpatient Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Since this initial version is distributed using KIDS, the transport global is automatically deleted after the install. If the plan is to delete existing Inpatient Medications routines before loading V. 5.0, be sure not to delete PSGW\* (Ward Stock) routines. These routines are not included as part of Inpatient Medications.
- The following Inpatient Medications routines were sent with a past version of the Kernel, and are no longer needed. They can be deleted.  
  PSGZ1TSK
- PSGZ2TSK
- PSIVZTSK

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/083.png)Note: It is okay if any of these routines are missing, because they are no longer used.

The information contained on pages 25 & 26 has been removed from the manual because mapping is no longer required now that all routines reside in ROU.

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME               | FILE              |
|------------------------|-----------------------|
| PSJ DOSAGE FORM REPORT | DOSAGE FORM (#50.606) |

## Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NAME                   | FILE                              |
|----------------------------|---------------------------------------|
| PSJ ECSP                   | PHARMACY SYSTEM (#59.7)               |
| PSJ FILED                  | DRUG (#50)                            |
| PSJ IUP SUPER EDIT         | INPATIENT USER PARAMETERS (#53.45)    |
| PSJ IUP USER EDIT          | INPATIENT USER PARAMETERS (#53.45)    |
| PSJ IWP EDIT               | INPATIENT WARD PARAMETERS (#59.6)     |
| PSJ OAOPT                  | PHARMACY SYSTEM (#59.7)               |
| PSJ PADE DISPENSING DEVICE | PADE DISPENSING DEVICE (#58.63)       |
| PSJ PADE INVENTORY         | PADE INVENTORY SYSTEM (#58.601)       |
| PSJ PADE SYSTEM            | PADE SYSTEM SETUP (#58.7)             |
| PSJ SHIFT EDIT             | ADMINISTRATION SHIFT (#51.15)         |
| PSJI PAT UPDATE            | PATIENT (#2)                          |
| PSJI SCHEDULE              | MEDICATION INSTRUCTION (#51.1)        |
| PSJI SITE PARAMETERS       | IV ROOM (#59.5)                       |
| PSJIADM                    | PATIENT (#2)                          |
| PSJIDE                     | DRUG ELECTROLYTES (#50.4)             |
| PSJIDRUG                   | DRUG(#50)                             |
| PSJIEDT                    | PHARMACY PATIENT (#55)                |
| PSJIEDT                    | NON-VERIFIED ORDERS (#53.1)           |
| PSJIES                     | DRUG (#50)                            |
| PSJINEW                    | PHARMACY PATIENT (#55)                |
| PSJIPS                     | DRUG (#50)                            |
| PSJIRNW                    | PHARMACY PATIENT (#55)                |
| PSJU DRUG EDIT             | DRUG (#50)                            |
| PSJU EASP                  | INPATIENT SITE (#59.4)                |
| PSJU ECSP                  | INPATIENT SITE (#59.4)                |
| PSJU ELSP                  | INPATIENT SITE (#59.4)                |
| PSJU EMSP                  | INPATIENT SITE (#59.4)                |
| PSJU EOSP                  | INPATIENT SITE (#59.4)                |
| PSJU EPLSP                 | INPATIENT SITE (#59.4)                |
| PSJU FILED                 | DRUG (#50)                            |
| PSJU IVSP                  | INPATIENT SITE (#59.4)                |
| PSJU WG                    | WARD GROUP (#57.5)                    |
| PSJUED                     | PHARMACY PATIENT (#55)                |
| PSJUMATE                   | MEDICATION ADMINISTERING TEAM (#57.7) |
| PSJUOSE                    | UNIT DOSE ORDER SET (#53.2)           |
| PSJUPAC                    | PHARMACY PATIENT (#55)                |
| PSJURET                    | PHARMACY PATIENT (#55)                |
| PSJUSCH                    | PHARMACY PATIENT (#55)                |
| PSJUSFE                    | INPATIENT SITE (#59.4)                |

The following input templates are no longer used and are exported as Delete at Site.

| NAME              | FILE                        |
|-----------------------|---------------------------------|
| PSJ EXT SCHEDULE EDIT | ADMINISTRATION SCHEDULE (#51.1) |
| PSJ PD EDIT           | PRIMARY DRUG (#50.3)            |
| PSJ SCHEDULE EDIT     | ADMINISTRATION SCHEDULE (#51.1) |
| PSJ FILED             | DRUG (#50)                      |
| PSJI ADD              | IV ADDITIVES (#52.6)            |
| PSJI SOL              | IV SOLUTIONS (#52.7)            |
| PSJQ FLUID            | PHARMACY QUICK ORDER (#57.1)    |
| PSJQ MED              | PHARMACY QUICK ORDER (#57.1)    |
| PSJUED                | NON-VERIFIED ORDERS (#53.1)     |
| PSJUPDE               | PHARMACY PATIENT (#55)          |

## List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ LM ALLERGY DETAIL

PSJ LM ALLERGY DISPL

PSJ LM BRIEF PATIENT INFO

PSJ LM CLINIC ORDERS

PSJ LM DETAILED ALLERGY

PSJ LM IV AC/EDIT

PSJ LM IV DISPLAY

PSJ LM IV INPT ACTIVE

PSJ LM IV INPT DISPLAY

PSJ LM IV INPT PENDING

PSJ LM IV LABELS

PSJ LM IV OE

PSJ LM IV PENDING

PSJ LM IV PROFILE

PSJ LM IV RETURN LABELS

PSJ LM OE

PSJ LM OE DISPLAY

PSJ LM PENDING EDIT

PSJ LM PNV

PSJ LM UD ACTION

PSJU LM ACCEPT

PSJU LM OE

Example: How to Print List Templates using VA FileMan

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION// LIST TEMPLATE (62 entries)

Select LIST TEMPLATE NAME: PSJ LM ALLERGY DETAIL

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed Fields

NAME: PSJ LM ALLERGY DETAIL TYPE OF LIST: PROTOCOL

RIGHT MARGIN: 80 TOP MARGIN: 8

BOTTOM MARGIN: 20 OK TO TRANSPORT?: OK

USE CURSOR CONTROL: YES

PROTOCOL MENU: PSJ LM DETAILED ALLERGY MENU

SCREEN TITLE: DETAILED ALLERGY VIEW ALLOWABLE NUMBER OF ACTIONS: 2

AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME: ^TMP("PSJAL",\$J)

EXIT CODE: D DISALL^PSJLMUTL(DFN) S VALMBCK="Q" K ^TMP("PSJALLRG",\$J)

HEADER CODE: D HDR^PSJLMHED(DFN) HELP CODE: D HELP^PSJALG

ENTRY CODE: D DETAIL^PSJALG

(*This page included for two-sided copying*.)

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Stand-alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Inpatient Medications package options are designed to stand-alone and can be accessed without first accessing the top-level menu. All of the options can be placed on menus other than their original menu without any additional editing.

## Top-level Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no top-level menu for Inpatient Medications. The Inpatient Medications options are included in the IV and Unit Dose top-level menus.

### Menu Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the following menus to the Inpatient Medications users:

| PSJU MGR                                                   | This is the only Unit Dose Medications menu, and is to be assigned to all Unit Dose users.                                                            |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PSJL_Manager" class="anchor"></span>PSJL MANAGER | This is the Clozapine Inpatient Medications Manager menu and should be assigned to the pharmacy users coordinating the inpatient clozapine dispensing |
| PSJI MGR                                                   | This IV Medications menu is to be assigned to the pharmacists, inpatient supervisors, and package coordinators.                                       |
| PSJI USR1                                                  | This IV Medications menu is to be assigned to the nurses.                                                                                             |
| PSJI USR2                                                  | This IV Medications menu is to be assigned to the pharmacy technicians.                                                                               |

### Menu Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is strongly recommended that the user <u>does not</u> place the Inpatient Medications (IV and Unit Dose) menus under the Outpatient Pharmacy menu. It is suggested that they be placed on the same menu as the Outpatient Pharmacy menu instead.

Although it has been common practice to place the Inpatient Medications top-level menus under the Outpatient Pharmacy menu, this can cause \<STORE\> errors.

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are exported with the Inpatient Medications package:

| Option Name                                             | Menu Text                                |
|-------------------------------------------------------------|----------------------------------------------|
| PSJ AC SET-UP                                               | AUto-Discontinue Set-Up                      |
| PSJ CD                                                      | Clinic Definition                            |
| PSJ CHECK DRUG INTERACTION                                  | Check Drug Interaction                       |
| PSJ ECO                                                     | Edit Clinic Med Orders Start Date/Time       |
| PSJ EXP                                                     | INpatient Stop Order Notices                 |
| PSJ EXTP                                                    | Patient Profile (Extended)                   |
| PSJ IWP EDIT                                                | Inpatient Ward Parameters Edit               |
| PSJ MDWS                                                    | Medications Due Worksheet                    |
| PSJ OAOPT                                                   | Order Action on Patient Transfer             |
| PSJ OE                                                      | Inpatient Order Entry                        |
| PSJ PADE SETUP                                              | PADE SYSTEM SETUP                            |
| PSJ PADE INVENTORY SYSTEM                                   | PADE INVENTORY SYSTEM SETUP                  |
| PSJ PADE SEND AREA SETUP                                    | PADE SEND AREA SETUP                         |
| PSJ PADE MAIN MENU                                          | PADE Main Menu                               |
| PSJ PADE SURGERY TASK                                       | PADE Surgery Task                            |
| PSJ PADE SEND SURGERY CASES                                 | PADE Send Surgery Cases                      |
| PSJ PADE INVENTORY MENU                                     | PADE Inventory Setup                         |
| PSJ PADE DEVICE SETUP                                       | PADE Dispensing Device Setup                 |
| PSJ PADE SEND ORDERS                                        | PADE Send Patient Orders                     |
| PSJ PADE INVENTORY REPORT                                   | PADE On-Hand Amounts                         |
| PSJ PADE DIVISION SETUP                                     | PADE System Division Setup                   |
| PSJ PADE TRANSACTION REPORT                                 | PADE Transaction Report                      |
| PSJ PADE REPORTS MENU                                       | PADE Reports                                 |
| PSJ PADE APPOINTMENT TASK                                   | PADE Appointment Task                        |
| PSJ PARAM EDIT MENU                                         | PARameters Edit Menu                         |
| PSJ PDV                                                     | Patients on Specific Drug(s)                 |
| PSJ PR                                                      | Inpatient Profile                            |
| PSJ SEUP                                                    | Inpatient User Parameters Edit               |
| PSJ SYS EDIT                                                | Systems Parameters Edit                      |
| PSJ UD ALIGN LABEL                                          | Align Unit Dose Labels                       |
| PSJ UEUP                                                    | Edit Inpatient User Parameters               |
| PSJI 200                                                    | Correct Changed Names in IV Orders           |
| PSJI ACTIVE                                                 | Active Order List (IV)                       |
| PSJI ALIGNMENT                                              | Align Labels (IV)                            |
| PSJI AMIS                                                   | AMIS (IV)                                    |
| PSJI AOR                                                    | ACtive Order Report by Ward/Drug (IV)        |
| PSJI BACKGROUND JOB                                         | Compile IV Costs in Background               |
| PSJI CHANGE                                                 | Change to Another IV Room (IV)               |
| PSJI COMPILE STATS                                          | COmpile IV Statistics (IV)                   |
| PSJI COMPLETE                                               | COmplete Orders (IV)                         |
| PSJI CONTROL CODES                                          | Test Control Codes (IV)                      |
| PSJI DELETE ORDER                                           | Delete Orders (IV)                           |
| PSJI DEVICE                                                 | Change Report/Label Devices (IV)             |
| PSJI DRUG COST REPORT                                       | Drug Cost Report (132 COLUMNS) (IV)          |
| PSJI DRUG FORM                                              | IV Drug Formulary Report (IV)                |
| PSJI DRUG INQUIRY                                           | Drug Inquiry (IV)                            |
| PSJI INDIVIDUAL SUSPENSE                                    | Individual Order Suspension (IV)             |
| PSJI LBLI                                                   | Individual Labels (IV)                       |
| PSJI LBLMENU                                                | Label Menu (IV)                              |
| PSJI LBLR                                                   | Reprint Scheduled Labels (IV)                |
| PSJI LBLS                                                   | Scheduled Labels (IV)                        |
| PSJI MAN                                                    | Manufacturing List (IV)                      |
| PSJI MANAGEMENT REPORTS                                     | Management Reports (IV)                      |
| PSJI MGR                                                    | IV Menu                                      |
| PSJI ORDER                                                  | Order Entry (IV)                             |
| PSJI PATIENT COST                                           | Patient Cost Report (132 COLUMNS) (IV)       |
| PSJI PROFILE                                                | Profile (IV)                                 |
| PSJI PROFILE REPORT                                         | Patient Profile Report (IV)                  |
| PSJI PROVIDER REPORT                                        | PRovider Drug Cost Report (132 COLUMNS) (IV) |
| PSJI PURGE                                                  | PUrge Data (IV)                              |
| PSJI PURGE ORDERS                                           | Purge Expired Orders (IV)                    |
| PSJI RECOMPILE                                              | Recompile Stats File (IV)                    |
| PSJI REPORTS                                                | REPorts (IV)                                 |
| PSJI RETURN BY BARCODE ID                                   | Barcode ID – Return and Destroy (IV)         |
| PSJI RETURNS                                                | RETurns and Destroyed Entry (IV)             |
| PSJI RNL                                                    | Renewal List (IV)                            |
| PSJI SITE PARAMETERS                                        | SIte Parameters (IV)                         |
| PSJI SUPERVISOR                                             | SUPervisor's Menu (IV)                       |
| PSJI SUSLBDEL                                               | Delete Labels from Suspense (IV)             |
| PSJI SUSLBLS                                                | Labels from Suspense (IV)                    |
| PSJI SUSLIST                                                | Suspense List (IV)                           |
| PSJI SUSMAN                                                 | Manufacturing Record for Suspense (IV)       |
| PSJI SUSMENU                                                | SUSpense Functions (IV)                      |
| PSJI SUSREP                                                 | Reprint Labels from Suspense (IV)            |
| PSJI UP                                                     | Update Daily Ward List (IV)                  |
| PSJI USR1                                                   | IV Menu                                      |
| PSJI USR2                                                   | IV Menu                                      |
| PSJI WARD                                                   | Ward List (IV)                               |
| PSJI WARD/DRUG USAGE REPORT                                 | Ward/Drug Usage Report (132 COLUMNS) (IV)    |
| <span id="PSJL_Manager2" class="anchor"></span>PSJL MANAGER | Clozapine Inpatient Medications Manager      |
| PSJU 14D MAR                                                | 14 Day MAR                                   |
| PSJU 24H MAR                                                | 24 Hour MAR                                  |
| PSJU 7D MAR                                                 | 7 Day MAR                                    |
| PSJU AL                                                     | Align Labels (Unit Dose)                     |
| PSJU AMIS                                                   | AMIS (Cost per Ward)                         |
| PSJU AP-1                                                   | Action Profile \#1                           |
| PSJU AP-2                                                   | Action Profile \#2                           |
| PSJU AT                                                     | Administering Teams                          |
| PSJU BRJ                                                    | Unit Dose Clean-Up                           |
| PSJU CA                                                     | Discontinue All of a Patient's Orders        |
| PSJU CPDD                                                   | Edit Patient's Default Stop Date             |
| PSJU DCT                                                    | Drug (Cost and/or Amount)                    |
| PSJU DOSAGE REPORT                                          | Free-text Dosage Report                      |
| PSJU DS                                                     | AUthorized Absence/Discharge Summary         |
| PSJU ECG                                                    | Clinic Groups                                |
| PSJU EPPD                                                   | Pharmacy Patient Data Edit                   |
| PSJU EUD                                                    | EXtra Units Dispensed                        |
| PSJU EUDD                                                   | Extra Units Dispensed Report                 |
| PSJU EWG                                                    | Ward Groups                                  |
| PSJU FILE                                                   | Supervisor's Menu                            |
| PSJU HOLD ALL                                               | Hold All of a Patient's Orders               |
| PSJU INQ DRUG                                               | Dispense Drug Look-Up                        |
| PSJU INQ STD SCHD                                           | Standard Schedules                           |
| PSJU INQMGR                                                 | INQuiries Menu                               |
| PSJU LABEL                                                  | Label Print/Reprint                          |
| PSJU MAR                                                    | Medication Administration Record             |
| PSJU MGR                                                    | Unit Dose Medications                        |
| PSJU MNGMT REPORTS                                          | MANagement Reports Menu                      |
| PSJU NE                                                     | Order Entry                                  |
| PSJU NSS REPORT                                             | Non-Standard Schedule Report                 |
| PSJU OSE                                                    | Order Set Enter/Edit                         |
| PSJU PL                                                     | Pick List                                    |
| PSJU PL MENU                                                | PIck List Menu                               |
| PSJU PLAPS                                                  | PIck List Auto Purge Set/Reset               |
| PSJU PLATCS                                                 | Send Pick List to ATC                        |
| PSJU PLDEL                                                  | Delete a Pick List                           |
| PSJU PLDP                                                   | ENter Units Dispensed                        |
| PSJU PLMGR                                                  | PIck List Menu                               |
| PSJU PLPRG                                                  | PUrge Pick Lists                             |
| PSJU PLRP                                                   | Reprint Pick List                            |
| PSJU PLUP                                                   | Update Pick List                             |
| PSJU PO PURGE                                               | PATient Order Purge                          |
| PSJU PR                                                     | PAtient Profile (Unit Dose)                  |
| PSJU PRVR                                                   | PRovider (Cost per)                          |
| PSJU REPORTS                                                | Reports Menu                                 |
| PSJU RET                                                    | Report Returns                               |
| PSJU SCT                                                    | Service (Total Cost per)                     |
| PSJU NSS SEARCH                                             | Non-Standard Schedule Search                 |
| PSJU SYSTEM                                                 | Unit Dose System                             |
| PSJU TCTD                                                   | Total Cost to Date (Current Patients)        |
| PSJU VBW                                                    | Non-Verified/Pending Orders                  |
|                                                             |                                              |

The following options are no longer in this initial version of Inpatient Medications. They were exported in the KIDS build as Delete at Site.

| Option Name             | Menu Text                  |
|-----------------------------|--------------------------------|
| PSJ AUTO CREATE THROUGH NDF | Auto create by VA Generic Name |
| PSJ CREATE                  | Create/Update Orders in OE/RR  |
| PSJ MANUAL MATCH            | Manual match Dispense Drugs    |
| PSJ QUICK ORDER REPORT      | Quick Order Report             |
| PSJ QUICK ORDERS            | Quick Order Add/Edit           |
| PSJ QUICK ORDERS MENU       | Quick Orders Menu              |
| PSJI NON-VERIFIED ORDERS    | Non-verified Orders (IV)       |
| PSJI NON VERIFIED ORDERS    | Non verified Orders (IV)       |
| PSJU AP                     | Action Profile (Unit Dose)     |
| PSJU EXP                    | Stop Order Notices             |
| PSJU DCC                    | Edit Cost Data                 |
| PSJU DCR                    | Cost at Discharge              |
| PSJU DRUG/ATC SET UP        | Dispense Drug/ATC Set Up       |
| PSJU PLSP                   | Site Parameters                |

Example: How to Print the Exported Options Using VA FileMan

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: PRINT TEMPLATE// OPTION

1 OPTION (2109 entries)

2 OPTION SCHEDULING (9 entries)

CHOOSE 1-2: 1

Select OPTION NAME: PSJ AC SET-UP AUto-Discontinue Set-Up

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed Fields

DISPLAY AUDIT TRAIL? No// \<Enter\> (No)

NAME: PSJ AC SET-UP MENU TEXT: AUto-Discontinue Set-Up

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: INPATIENT MEDICATIONS X ACTION PRESENT: YES

DESCRIPTION:

This allows the site to determine if patients' Inpatient Medications (IV and

Unit Dose) orders are d/c'd when the patient is transferred between wards,

between services, or to authorized absence. This determination can be made

on a ward-by-ward and/or service-by-service basis.

EXIT ACTION: K C,I,I1,DIC,DLAYGO ROUTINE: ENOAOPT^PSGFILD0

UPPERCASE MENU TEXT: AUTO-DISCONTINUE SET-UP

(*This page included for two-sided copying*.)

# Data Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At present, the Inpatient Medications package does not provide for the archiving of its data.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unit Dose Auto Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Inpatient Medications initial installation is run, it sets up the *Unit Dose Clean-Up* \[PSJU BRJ\] option as a background job that is initially scheduled to run every day at 1:45 a.m. This job should run every night to "clean up" after the Unit Dose Medications module to free up as much disk space as possible, performing the tasks that would slow the package down if performed during the day. The time of day that the job runs can be changed, but this option should be run every day. The option performs the following functions:

- Deletes records in the NON-VERIFIED ORDERS file (#53.1) that have been discontinued or have become active.
- Deletes label records that are older than the number of days specified in the site parameters.
- Performs the pick list auto purge, deleting pick lists that have been filed away and are older than the number of days specified by the user.

To have this background job purge filed away pick lists (which can recover considerable disk space), a user needs to enter the number of days that pick lists can last through the *PIck List Auto Purge Set/Reset* \[PSJU PLAPS\] option. If no entry is made here, or the entry is deleted, the auto-purge of pick lists will not occur.

### IV Auto Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the Inpatient Medications package is initially installed, the *Compile IV Costs in Background* \[PSJI BACKGROUND\] option should be scheduled to run each night. When this job is run, it purges any IV statistics in the IV STATS file (#50.8) that are over 100 days old before compiling the new transactions.

### Unit Dose Manual Purging – Temporarily Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/084.png)Note: The *PATient Order Purge* \[PSJU PO PURGE\] option is "<u>Out of Order</u>" and <u>TEMPORARILY UNAVAILABLE</u>.

The *PATient Order Purge* \[PSJU PO PURGE\] option under the *Supervisor's Menu* \[PSJU FILE\] option allows the user to delete orders for patients who have been discharged. Whenever a patient is discharged, a cross-reference is created for each order <u>for that admission only</u>. In this way, it is possible to delete all of the orders for a patient's past admissions while not affecting any current orders if the patient is currently admitted. (The cross-reference is deleted when the order is deleted.)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/085.png)Note: This option requires that there are no outstanding pick lists within 30 days of the date selected to purge. This is to ensure that no data is purged before the pick lists are done with it. Also, if the *PATient Order Purge* \[PSJU PO PURGE\] option is not properly purging orders for the date range specified, it might be necessary to re-cross-reference the AUDDD index on the PURGE FLAG sub-field (#64), within the UNIT DOSE multiple (#62) within the PHARMACY PATIENT file (#55). The following example shows re-indexing this field through VA FileMan:

Example: Re-Indexing the Purge Flag in the PHARMACY PATIENT file (#55)

VA FileMan 22.0

Select OPTION: UTILITY FUNCTIONS

Select UTILITY OPTION: RE-INDEX FILE

MODIFY WHAT FILE: PHARMACY PATIENT

THERE ARE 146 INDICES WITHIN THIS FILE

DO YOU WISH TO RE-CROSS-REFERENCE ONE PARTICULAR INDEX? NO// Y (YES)

Select FIELD: UNIT DOSE (multiple)

Select Unit Dose SUB-FIELD: PURGE FLAG

CURRENT CROSS-REFERENCES:

1 MUMPS 'AL79' INDEX OF UNIT DOSE SUB-FIELD

(UNIT DOSE ACTIVITY)

2 REGULAR 'AUDDD' INDEX OF FILE

(NEEDED BY UNIT DOSE)

WANT TO RE-CROSS-REFERENCE ONE OF THEM? NO// Y (YES)

WHICH NUMBER: 2

ARE YOU SURE YOU WANT TO DELETE AND RE-CROSS-REFERENCE THE 'AUDDD' INDEX? NO// Y

...HMM, I'M WORKING AS FAST AS I CAN...

...EXCUSE ME, HOLD ON..... ...DONE!

Select UTILITY OPTION: \<Enter\>

The *PUrge Pick Lists* \[PSJU PLPRG\] option allows users to immediately purge pick lists that have been filed away, if deemed necessary for immediate recovery of disk space.

### IV Manual Purging – Temporarily Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/086.png)Note: The *PUrge Data (IV)* \[PSJI PURGE\] option is "<u>Out of Order</u>" and <u>TEMPORARILY UNAVAILABLE</u>.

The *PUrge Data (IV)* \[PSJI PURGE\] option allows the deletion of IV orders for a specific patient. It is locked with the PSJI PURGE security key, and is designed to be used only if an order has been entered for the wrong patient. IV orders can only be deleted if no labels have been printed for the order.

The *Purge Expired Orders (IV)* \[PSJI PURGE ORDERS\] option allows users to purge expired or discontinued orders that have been inactive for at least 30 days. The PSJI PURGE security key controls access to this option and holders of this key should be selected carefully. When invoked, the user is required to enter a date at least 30 days in the past.

All IV orders that expired or were discontinued before the date entered will be purged. A large number of orders are entered in this package, this option should be run at least once a month to ensure maximum processing speed while using the IV Medications module.

*(This page added for two-sided copying).*

# Inpatient Medications and CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications is designed for use with the CPRS package.

## Installation of the Protocols for CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The protocols used to interface with the CPRS package are automatically installed. (For more information, consult the Pharmacy Data Management (PDM) Installation Guide.) The initial installation will also add the Inpatient Medications actions on the Patient movements to the Patient Information Management System (PIMS) Movement Event protocol (DGPM MOVEMENT EVENTS).

## Converting 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four conversions that will run with the initial install.

### Order Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For V. 5.0, Orderable Item replaces the Primary Drug. Conversions are included with this initial version that copy data in the old Dosage Ordered fields to the new Dosage Ordered fields, and determines and adds an Orderable Item to each order. Only orders that have a stop date less than 365 days prior to the V. 5.0 installation date will be converted. The installation date, used by both methods described below, is determined by the DATE INITS LAST RUN field (#20.2) in the PHARMACY SYSTEM file (#59.7). Order Location Codes will be standardized to V for the IV sub-file (#100) of the PHARMACY PATIENT file (#55), U for the Unit Dose sub-file (#62) of the PHARMACY PATIENT file (#55), and P for Orders in the NON-VERFIED ORDERS file (#53.1). For orders in the IV sub-file (#100) of the PHARMACY PATIENT file (#55), a new field was added to the ACTIVITY LOG REASON file (#53.3) multiple that is a pointer to the NEW PERSON file (#200). This ENTRY BY field (#135) is populated by taking the free-text data from the ENTRY CODE field (#.23) and determining the corresponding internal entry number (IEN) in the NEW PERSON file (#200). If the determination cannot be made, a mail message is sent to holders of the PSJI MGR key with these identified. Two methods are used to perform this conversion:

#### Background

When CPRS V. 1.0 is initially installed, a process is queued to run in the background and convert existing Inpatient Medications orders. After a patient's orders have been processed, that patient's IEN will be stored in the DATE 5.0 UD VER CONV FINISHED field (#25.1) of the PHARMACY SYSTEM file (#59.7). This will be used to determine where the process should begin if it must be restarted. When all of the orders for a patient have been processed, the

CONVERTED FOR VERSION 5.0? field (#104) of the PHARMACY PATIENT file (#55) is set, showing the conversion has been accomplished for that patient. When all Inpatient Medications orders within the specified time frame on the system have been converted, the date/time the process completed will be stored in the DATE 5.0 CONVERSION COMPLETED field (#25.2) of the PHARMACY SYSTEM file (#59.7).

#### Patient Selection

The capability has been added to convert the data "on the fly" if an order is accessed before the background conversion completes and before the background process has converted the selected patient's data. After converting the orders for the selected patient, the CONVERTED FOR VERSION 5.0? field (#104) of the PHARMACY PATIENT file (#55) is set, showing the conversion has been accomplished for that patient.

### Pick List Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new ORDERABLE ITEM sub-field (#.06) within the ORDER multiple (#1) within the PATIENT multiple (#1) in the PICK LIST file (#53.5) has been added. The ORDERABLE ITEM sub-field (#.06) of the ORDER SUB-FIELD multiple (#53.52) is populated as part of this initial conversion and the cross-references are recompiled so that the pick lists are ready for use with V. 5.0.

### Order Set Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Dispense Drug is used to determine Orderable Item, which replaces Primary Drug. Once this initial conversion occurs, the Order Sets are ready for use with V. 5.0. If any order, within an order set, is found that has multiple Dispense Drugs matched to different Orderable Items, the Order Set is not converted. A mail message is sent to all holders of the RPHARM key with these Order Sets identified.

### Verification Data Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional cross-references have been added to identify orders that have not been verified by nursing or pharmacy.

Inpatient Medications protocols will be installed into the PROTOCOL file (#101). These protocols will be used for Inpatient Medication's interactions with CPRS, and to trigger the appropriate order action when Medical Administration Service (MAS) detects a patient movement.

## Protocol Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package sends the following protocols for use in V. 5.0. These protocols are automatically installed when the Inpatient Medications initial installation is run.

The protocols with "PAT" as part of their name assume that the patient has already been selected through CPRS before the protocol is selected. The other protocols will prompt the user for patients.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Protocol Name</strong></th>
<th><strong>Item Text</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSJ ADT-A01 CLIENT</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A01 SERVER</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A01 ROUTER</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A02 CLIENT</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A02 SERVER</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A03 CLIENT</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A03 SERVER</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A08-SDAM CLIENT</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A08-SDAM ROUTER</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A08-SDAM SERVER</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A11 CLIENT</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A11 SERVER</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT-A12 CLIENT</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ ADT-A12 SERVER</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>PSJ ADT A13 SERVER</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>PSJ DISPLAY DRUG ALLERGIES</td>
<td>Display Drug Allergies</td>
</tr>
<tr class="odd">
<td>PSJ LM 14D MAR</td>
<td>14 Day MAR</td>
</tr>
<tr class="even">
<td>PSJ LM 24H MAR</td>
<td>24 Hour MAR</td>
</tr>
<tr class="odd">
<td>PSJ LM 7D MAR</td>
<td>7 Day MAR</td>
</tr>
<tr class="even">
<td>PSJ LM AP1</td>
<td>Action Profile #1</td>
</tr>
<tr class="odd">
<td>PSJ LM AP2</td>
<td>Action Profile #2</td>
</tr>
<tr class="even">
<td>PSJ LM BPI HIDDEN ACTIONS</td>
<td>Brief Patient Info Hidden Actions Menu</td>
</tr>
<tr class="odd">
<td>PSJ LM BRIEF PATIENT INFO MENU</td>
<td>Brief Allergy Display</td>
</tr>
<tr class="even">
<td>PSJ LM BYPASS</td>
<td>Bypass</td>
</tr>
<tr class="odd">
<td>PSJ LM CWAD</td>
<td>CWAD Information</td>
</tr>
<tr class="even">
<td>PSJ LM DC</td>
<td>Discontinue</td>
</tr>
<tr class="odd">
<td>PSJ LM DETAILED ALLERGY</td>
<td>Detailed Allergy/ADR List</td>
</tr>
<tr class="even">
<td>PSJ LM DETAILED ALLERGY MENU</td>
<td>ALLERGY/ADR LIST MENU</td>
</tr>
<tr class="odd">
<td>PSJ LM DIN</td>
<td>Drug Restriction/Guideline</td>
</tr>
<tr class="even">
<td><p>PSJ LM DRUG CHECK</p>
<p>PSJ LM ECO HIDDEN ACTIONS</p>
<p>PSJ LM ECO IM PR</p>
<p>PSJ LM ECO MENU</p>
<p>PSJ LM ECO RANGE</p>
<p>PSJ LM ECO SELECT</p>
<p>PSJ LM ECO START</p></td>
<td><p>Check Interactions</p>
<p>Clinic Order Hidden Actions Menu</p>
<p>Inpatient Medications Profile</p>
<p>Clinic Order Edit Start Date/Time</p>
<p>Date Range</p>
<p>Edit Start Date</p>
<p>Edit Start Date</p></td>
</tr>
<tr class="odd">
<td><p>PSJ LM DRUG LOOK</p>
<p>PSJ LM EDIT ALLERGY/ADR DATA</p></td>
<td><p>Disp Drug Lookup</p>
<p>Enter/Edit Allergy/ADR Data</p></td>
</tr>
<tr class="even">
<td>PSJ LM EDIT NEW</td>
<td></td>
</tr>
<tr class="odd">
<td>PSJ LM EXTP</td>
<td>Patient Profile (Extended)</td>
</tr>
<tr class="even">
<td>PSJ LM FINISH</td>
<td>Finish</td>
</tr>
<tr class="odd">
<td>PSJ LM FINISH MENU</td>
<td></td>
</tr>
<tr class="even">
<td>PSJ LM FLAG</td>
<td>Flag</td>
</tr>
<tr class="odd">
<td>PSJ LM HOLD</td>
<td>Hold</td>
</tr>
<tr class="even">
<td>PSJ LM INTERVENTION DELETE</td>
<td>Delete Pharmacy Intervention</td>
</tr>
<tr class="odd">
<td>PSJ LM INTERVENTION EDIT</td>
<td>Edit Pharmacy Intervention</td>
</tr>
<tr class="even">
<td>PSJ LM INTERVENTION NEW ENTRY</td>
<td>Enter Pharmacy Intervention</td>
</tr>
<tr class="odd">
<td>PSJ LM INTERVENTION PRINTOUT</td>
<td>Print Pharmacy Intervention</td>
</tr>
<tr class="even">
<td>PSJ LM INTERVENTION VIEW</td>
<td>View Pharmacy Intervention</td>
</tr>
<tr class="odd">
<td>PSJ LM IV NEW SELECT ORDER</td>
<td></td>
</tr>
<tr class="even">
<td>PSJ LM IV OE MENU</td>
<td>IV ORDER ENTRY MENU</td>
</tr>
<tr class="odd">
<td>PSJ LM IV SELECT ORDER</td>
<td>Select Order</td>
</tr>
<tr class="even">
<td>PSJ LM LABEL PRINT/REPRINT MENU</td>
<td>Label Print/Reprint</td>
</tr>
<tr class="odd">
<td>PSJ LM MAR MENU</td>
<td>MAR Menu</td>
</tr>
<tr class="even">
<td>PSJ LM MDWS</td>
<td>Medications Due Worksheet</td>
</tr>
<tr class="odd">
<td><span id="PSJ_LM_NEW_CM_ORDER" class="anchor"></span>PSJ LM NEW CM ORDER</td>
<td>New Clinic Medication Entry</td>
</tr>
<tr class="even">
<td>PSJ LM NEW ORDER</td>
<td>New Order Entry</td>
</tr>
<tr class="odd">
<td>PSJ LM NEW ORDER FROM PROFILE</td>
<td>New Order Entry</td>
</tr>
<tr class="even">
<td>PSJ LM NEW SELECT ALLERGY</td>
<td></td>
</tr>
<tr class="odd">
<td>PSJ LM NEW SELECT ORDER</td>
<td></td>
</tr>
<tr class="even">
<td>PSJ LM OE MENU</td>
<td>ORDER ENTRY MENU</td>
</tr>
<tr class="odd">
<td>PSJ LM ORDER VIEW HIDDEN ACTIONS</td>
<td>Order View Hidden Actions Menu</td>
</tr>
<tr class="even">
<td>PSJ LM OTHER PHARMACY OPTIONS</td>
<td>Other Pharmacy Options</td>
</tr>
<tr class="odd">
<td>PSJ LM OVERRIDES</td>
<td>Overrides/Interventions</td>
</tr>
<tr class="even">
<td>PSJ LM PAT PR</td>
<td>Inpatient Medications Profile</td>
</tr>
<tr class="odd">
<td>PSJ LM PATIENT DATA</td>
<td>Patient Record Update</td>
</tr>
<tr class="even">
<td>PSJ LM PATIENT INFO</td>
<td>Patient Information</td>
</tr>
<tr class="odd">
<td>PSJ LM PENDING ACTION</td>
<td>Pending Order Actions</td>
</tr>
<tr class="even">
<td>PSJ LM PHARMACY INTERVENTION MENU</td>
<td>Pharmacy Intervention Menu</td>
</tr>
<tr class="odd">
<td>PSJ LM PNV JUMP</td>
<td>Jump to a Patient</td>
</tr>
<tr class="even">
<td>PSJ LM PRINT OUTPATIENT PROFILE</td>
<td>Outpatient Prescriptions</td>
</tr>
<tr class="odd">
<td>PSJ LM PROFILE HIDDEN ACTIONS</td>
<td>Profile Hidden Actions Menu</td>
</tr>
<tr class="even">
<td>PSJ LM PROFILE MENU</td>
<td>Patient Profiles</td>
</tr>
<tr class="odd">
<td>PSJ LM RETURNS/DESTROYED MENU</td>
<td>Returns/Destroyed Menu</td>
</tr>
<tr class="even">
<td>PSJ LM SELECT ORDER</td>
<td>Select Order</td>
</tr>
<tr class="odd">
<td><p>PSJ LM SHOW PROFILE</p>
<p>PSJ LM VIEW ORDER DETAIL</p></td>
<td><p>View Profile</p>
<p>View Order Detail</p></td>
</tr>
<tr class="even">
<td><p>PSJ LM VIEW PROVIDER</p>
<p>PSJ OR MENU</p></td>
<td><p>Provider Lookup</p>
<p>Inpatient Medications Ward Reports</p></td>
</tr>
<tr class="odd">
<td>PSJ OR PAT ADT</td>
<td>Inpatient Medications Actions on Patient ADT</td>
</tr>
<tr class="even">
<td>PSJ OR PAT MENU</td>
<td>Inpatient Medications Patient Reports</td>
</tr>
<tr class="odd">
<td>PSJ OR PAT OE</td>
<td>Inpatient Medications</td>
</tr>
<tr class="even">
<td>PSJ OR PAT OE MENU</td>
<td>Inpatient Medications</td>
</tr>
<tr class="odd">
<td>PSJ OR PAT PR</td>
<td>Inpatient Medications Profile</td>
</tr>
<tr class="even">
<td>PSJ OR PAT PR MENU</td>
<td>Inpatient Medications Profiles</td>
</tr>
<tr class="odd">
<td>PSJ OR PR</td>
<td>Inpatient Medications Profile</td>
</tr>
<tr class="even">
<td>PSJ PC IV AC/EDIT ACTION</td>
<td>IV ACCEPT EDIT ACTIONS</td>
</tr>
<tr class="odd">
<td>PSJ PC IV ACCEPT</td>
<td>Accept</td>
</tr>
<tr class="even">
<td>PSJ PC IV CANCELLED</td>
<td>Cancelled</td>
</tr>
<tr class="odd">
<td>PSJ PC IV DESTROYED</td>
<td>Destroyed</td>
</tr>
<tr class="even">
<td>PSJ PC IV LABELS ACTION</td>
<td>INDIVIDUAL IV LABEL ACTIONS</td>
</tr>
<tr class="odd">
<td>PSJ PC IV LOG</td>
<td>Activity Logs</td>
</tr>
<tr class="even">
<td>PSJ PC IV NEW LABELS</td>
<td>PRINT NEW IV LABELS</td>
</tr>
<tr class="odd">
<td>PSJ PC IV RECYCLED</td>
<td>Recycled</td>
</tr>
<tr class="even">
<td>PSJ PC IV REPRINT LABELS</td>
<td>Reprint IV label(s)</td>
</tr>
<tr class="odd">
<td>PSJ PC RETURN IV LABELS ACTION</td>
<td>RETURN IV LABELS ACTIONS</td>
</tr>
<tr class="even">
<td>PSJ SELECT ALLERGY</td>
<td>Select Allergy</td>
</tr>
<tr class="odd">
<td>PSJI LM ACTIVE MENU</td>
<td>IV Active Order Actions</td>
</tr>
<tr class="even">
<td>PSJI LM ACTIVITY LOG</td>
<td>View Activity Log</td>
</tr>
<tr class="odd">
<td>PSJI LM ALIGNMENT</td>
<td>Align Labels (IV)</td>
</tr>
<tr class="even">
<td>PSJI LM DISCONTINUE</td>
<td>Discontinue</td>
</tr>
<tr class="odd">
<td>PSJI LM EDIT</td>
<td>Edit</td>
</tr>
<tr class="even">
<td>PSJI LM FINISH</td>
<td>Finish</td>
</tr>
<tr class="odd">
<td>PSJI LM LABEL LOG</td>
<td>View Label Log</td>
</tr>
<tr class="even">
<td>PSJI LM LBLI</td>
<td>Individual Labels (IV)</td>
</tr>
<tr class="odd">
<td>PSJI LM LBLR</td>
<td>Reprint Scheduled Labels (IV)</td>
</tr>
<tr class="even">
<td>PSJI LM LBLS</td>
<td>Scheduled Labels (IV)</td>
</tr>
<tr class="odd">
<td>PSJI LM LOG MENU</td>
<td>IV Profile Log Menu</td>
</tr>
<tr class="even">
<td>PSJI LM PAT PR</td>
<td>IV Medications Profile</td>
</tr>
<tr class="odd">
<td>PSJI LM PENDING ACTION</td>
<td>IV Pending Order Actions</td>
</tr>
<tr class="even">
<td>PSJI LM RETURNS</td>
<td>Returns/Destroyed Entry (IV)</td>
</tr>
<tr class="odd">
<td>PSJI OR PAT FLUID OE</td>
<td>IV Fluids</td>
</tr>
<tr class="even">
<td>PSJI OR PAT FLUID OE MENU</td>
<td>IV FLUIDS...</td>
</tr>
<tr class="odd">
<td>PSJI OR PAT HYPERAL OE</td>
<td>IV Hyperal</td>
</tr>
<tr class="even">
<td>PSJI OR PAT PR</td>
<td>IV Medications Profile</td>
</tr>
<tr class="odd">
<td>PSJI OR PR</td>
<td>IV Medications Profile</td>
</tr>
<tr class="even">
<td>PSJI PC HOLD</td>
<td>Hold</td>
</tr>
<tr class="odd">
<td>PSJI PC ONCALL</td>
<td>On Call</td>
</tr>
<tr class="even">
<td>PSJI PC RENEWAL</td>
<td>Renew</td>
</tr>
<tr class="odd">
<td>PSJU LM ACCEPT</td>
<td>Accept</td>
</tr>
<tr class="even">
<td>PSJU LM ACCEPT EDIT</td>
<td>Edit</td>
</tr>
<tr class="odd">
<td>PSJU LM ACCEPT MENU</td>
<td></td>
</tr>
<tr class="even">
<td>PSJU LM ACTIONS MENU</td>
<td></td>
</tr>
<tr class="odd">
<td>PSJU LM ACTIVITY LOG</td>
<td>Activity Logs</td>
</tr>
<tr class="even">
<td>PSJU LM AL</td>
<td>Align Labels (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU LM COPY</td>
<td>Copy</td>
</tr>
<tr class="even">
<td>PSJU LM EDIT</td>
<td>Edit</td>
</tr>
<tr class="odd">
<td>PSJU LM HIDDEN ACTIONS</td>
<td>UD Hidden Actions</td>
</tr>
<tr class="even">
<td>PSJU LM HIDDEN UD ACTIONS</td>
<td>Unit Dose Hidden Actions</td>
</tr>
<tr class="odd">
<td>PSJU LM LABEL</td>
<td>Label Print/Reprint</td>
</tr>
<tr class="even">
<td>PSJU LM MARK INCOMPLETE</td>
<td>Mark Order As Incomplete</td>
</tr>
<tr class="odd">
<td>PSJU LM MARK NOT GIVE</td>
<td>Mark Order Not To Be Given</td>
</tr>
<tr class="even">
<td>PSJU LM PAT PR</td>
<td>Unit Dose Medications Profile</td>
</tr>
<tr class="odd">
<td>PSJU LM PL</td>
<td>Pick List</td>
</tr>
<tr class="even">
<td>PSJU LM PL MENU</td>
<td>Pick List Menu</td>
</tr>
<tr class="odd">
<td>PSJU LM PLDP</td>
<td>Enter Units Dispensed</td>
</tr>
<tr class="even">
<td>PSJU LM PLEUD</td>
<td>Extra Units Dispensed</td>
</tr>
<tr class="odd">
<td>PSJU LM PLRP</td>
<td>Reprint Pick List</td>
</tr>
<tr class="even">
<td>PSJU LM PLUP</td>
<td>Update Pick List</td>
</tr>
<tr class="odd">
<td>PSJU LM RENEW</td>
<td>Renew</td>
</tr>
<tr class="even">
<td>PSJU LM RET</td>
<td>Report Returns (UD)</td>
</tr>
<tr class="odd">
<td>PSJU LM SPEED DISCONTINUE</td>
<td>Speed Discontinue</td>
</tr>
<tr class="even">
<td>PSJU LM SPEED FINISH</td>
<td>Speed Finish</td>
</tr>
<tr class="odd">
<td>PSJU LM SPEED RENEW</td>
<td>Speed Renew</td>
</tr>
<tr class="even">
<td>PSJU LM SPEED VERIFY</td>
<td>Speed Verify</td>
</tr>
<tr class="odd">
<td>PSJU LM VERIFY</td>
<td>Verify</td>
</tr>
<tr class="even">
<td>PSJU OR 14D MAR</td>
<td>14 Day MAR (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU OR 7D MAR</td>
<td>7 Day MAR (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU OR AP-1</td>
<td>Action Profile #1</td>
</tr>
<tr class="odd">
<td>PSJU OR AP-2</td>
<td>Action Profile #2</td>
</tr>
<tr class="even">
<td>PSJU OR DS</td>
<td>Authorized Absence/Discharge Summary (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU OR PAT 14D MAR</td>
<td>14 Day MAR (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU OR PAT 7D MAR</td>
<td>7 Day MAR (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU OR PAT AP-1</td>
<td>Action Profile #1 (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU OR PAT AP-2</td>
<td>Action Profile #2 (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU OR PAT DS</td>
<td>Discharge Summary (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU OR PAT PR</td>
<td>Unit Dose Medications Profile</td>
</tr>
<tr class="odd">
<td>PSJU OR PAT VBW</td>
<td>Non-Verified Orders (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU OR PR</td>
<td>Patient Profile (Unit Dose)</td>
</tr>
<tr class="odd">
<td>PSJU OR VBW</td>
<td>Non-Verified Orders (Unit Dose)</td>
</tr>
<tr class="even">
<td>PSJU PLATCS</td>
<td>Send Pick List to ATC</td>
</tr>
<tr class="odd">
<td>VALM DOWN A LINE</td>
<td>Down a Line</td>
</tr>
<tr class="even">
<td>VALM FIRST SCREEN</td>
<td>First Screen</td>
</tr>
<tr class="odd">
<td>VALM GOTO PAGE</td>
<td>Go to Page</td>
</tr>
<tr class="even">
<td>VALM HIDDEN ACTIONS</td>
<td>Standard Hidden Actions</td>
</tr>
<tr class="odd">
<td>VALM LAST SCREEN</td>
<td>Last Screen</td>
</tr>
<tr class="even">
<td>VALM LEFT</td>
<td>Shift View to Left</td>
</tr>
<tr class="odd">
<td>VALM NEXT SCREEN</td>
<td>Next Screen</td>
</tr>
<tr class="even">
<td>VALM PREVIOUS SCREEN</td>
<td>Previous Screen</td>
</tr>
<tr class="odd">
<td>VALM PRINT LIST</td>
<td>Print List</td>
</tr>
<tr class="even">
<td>VALM PRINT SCREEN</td>
<td>Print Screen</td>
</tr>
<tr class="odd">
<td>VALM QUIT</td>
<td>Quit</td>
</tr>
<tr class="even">
<td>VALM REFRESH</td>
<td>Re-Display Screen</td>
</tr>
<tr class="odd">
<td>VALM RIGHT</td>
<td>Shift View to Right</td>
</tr>
<tr class="even">
<td>VALM SEARCH LIST</td>
<td>Search List</td>
</tr>
<tr class="odd">
<td>VALM TURN ON/OFF MENUS</td>
<td>Auto-Display (On/Off)</td>
</tr>
<tr class="even">
<td>VALM UP ONE LINE</td>
<td>Up a Line</td>
</tr>
</tbody>
</table>

With patch <span id="Patch_399_Protocol_Updates" class="anchor"></span>PSJ\*5\*399, the following protocols were modified to support the prompt for INDICATION:

- PSJ LM PENDING ACTION
- PSJ PC IV AC/EDIT ACTION
- PSJI LM ACTIVE MENU
- PSJI LM PENDING ACTION

Example: How to Print the Exported Protocols Using VA FileMan

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: PROTOCOL// PROTOCOL (742 entries)

Select PROTOCOL NAME: PSJ LM 14D MAR 14 Day MAR

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed Fields

NAME: PSJ LM 14D MAR ITEM TEXT: 14 Day MAR

TYPE: action CREATOR: POSTMASTER

PACKAGE: INPATIENT MEDICATIONS

DESCRIPTION: This allows the user to print a selected patient's medication

orders on a Medication Administration Record (MAR) for the charting of the

administration of the orders over a 14 day period. It is designed to replace

the manual Continuing Medication Record (CMR). This protocol assumes that a

patient has already been selected.

EXIT ACTION: S VALMBCK="R"

ENTRY ACTION: N VADM,VAIN S PSGMARDF=14 D FULL^VALM1,ENLM^PSGMMAR

TIMESTAMP: 56693,43648

## Health Level Seven (HL7) Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Ordering Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of HL7 data fields that will be used in transactions between Order Entry/Results Reporting (OE/RR) V. 3.0 and the Pharmacy packages. Not every data field will be used in every message.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><em>SEG</em></th>
<th><em>SEQ</em></th>
<th><em>FIELD NAME</em></th>
<th><em>EXAMPLE</em></th>
<th><em>HL7 TYPE</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MSH</strong></td>
<td>1</td>
<td>Field Separator</td>
<td>|</td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Encoding Characters*</td>
<td>^~\&amp;</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Sending Application</td>
<td>ORDER ENTRY</td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Sending Facility</td>
<td>660</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Receiving Application</td>
<td>PHARMACY</td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>Receiving Facility</td>
<td>660</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>D/T of Message</td>
<td>199409151010</td>
<td>timestamp</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>Message Type</td>
<td>ORM</td>
<td>ID</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>PID</strong></td>
<td>3</td>
<td>Patient ID</td>
<td>5340747</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Patient Name</td>
<td>PSJPATIENT1,ONE</td>
<td>patient name</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>PV1</strong></td>
<td>2</td>
<td>Patient Class</td>
<td>I</td>
<td>table 4</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Patient Location*</td>
<td>32^234-4</td>
<td>user table</td>
</tr>
<tr class="odd">
<td></td>
<td>45</td>
<td>Appointment Date/Time</td>
<td>200308040800-0600</td>
<td>timestamp</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>{ ORC</strong></td>
<td>1</td>
<td>Order Control</td>
<td>NW</td>
<td>table 119</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Placer Order Number*</td>
<td>234123;1^OR</td>
<td>number^application</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Filler Order Number*</td>
<td>870745^PS</td>
<td>number^application</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Order Status</td>
<td>CM</td>
<td>table 38</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>Quantity/Timing*</td>
<td>325&amp;MG&amp;1&amp;TABLET&amp;325MG&amp;638^Q1D^D14^199409151010^^R^^325MG^</td>
<td>dose^schedule^duration^start^^priority^^text^ conjunction</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>D/T of Transaction</td>
<td>199409151010</td>
<td>timestamp</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Entered by</td>
<td>10</td>
<td>composite ID</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>Verified by</td>
<td>23</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>Ordering Provider</td>
<td>97378</td>
<td>composite ID</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>Order Effective D/T</td>
<td>199409151010</td>
<td>timestamp</td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>Order Control Reason*</td>
<td>E^ELECTRONICALLY ENTERED^99ORN^12^ Requesting Physician Cancelled^99ORR</td>
<td><p>coded element:</p>
<p>NoO Code^NoO Name^99ORN ^#^Reason for Action^ 99ORR</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RXO</strong></td>
<td>1</td>
<td>Requested Give Code*</td>
<td>^^^8^DIGOXIN TAB^99PSP</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Requested Give Amt</td>
<td>125</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Requested Dispense Code*</td>
<td>576.4^DIGOXIN 0.5MG TAB^99NDF^4213^DIGOXIN 0.5MG TAB^99PSD</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>Requested Disp Amt</td>
<td>30</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>13</td>
<td>Number of Refills</td>
<td>5</td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>17</td>
<td>Requested Give Per</td>
<td>D30</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>RXE</strong></td>
<td>1</td>
<td>Quantity/Timing*</td>
<td><p>325&amp;MG&amp;1&amp;TABLET^QD^^</p>
<p>199409150600^19940925</p>
<p>0600^^^325MG^</p></td>
<td><p>dose^schedule^duration^</p>
<p>start^stop^priority^^</p>
<p>text^conjunction</p></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Give Code*</td>
<td>576.4^^99NDF^21^^99PSD</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>Dispense Amount</td>
<td>100</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>Number of Refills</td>
<td>11</td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>22</td>
<td>Give Per Time</td>
<td>D30</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>23</td>
<td>Give Rate Amount</td>
<td>125</td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td>24</td>
<td>Give Rate Units*</td>
<td>^^^^ml/hr99PSU</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>25</td>
<td>Give Strength</td>
<td>325</td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>Give Strength Units*</td>
<td>^^^20^MG^99PSU</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>{ NTE }</strong></td>
<td>1</td>
<td>Set ID</td>
<td>7</td>
<td>set ID</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Source of Comment</td>
<td>P</td>
<td>table 105</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Comment</td>
<td>take with food</td>
<td>formatted text</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>{ RXR }</strong></td>
<td>1</td>
<td>Route*</td>
<td>^^^23^ORAL^99PSR</td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>{ RXC }</strong></td>
<td>1</td>
<td>RX Component Type</td>
<td>B</td>
<td>table 166</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Component Code*</td>
<td>^^^4132^D5 W NS^99PSD</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Component Amount</td>
<td>1</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Component Units*</td>
<td>^^^PSIV-1^ML^99OTH</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Additive Frequency</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>{ OBX }</strong></td>
<td>1</td>
<td>Set ID</td>
<td>1</td>
<td>set ID</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Value Type</td>
<td>TX</td>
<td>table 125</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Observation ID</td>
<td>^^^38^Critical Drug-Drug interaction^99OCX</td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Observation Value</td>
<td>Critical drug-drug interaction Aspirin-Warfarin</td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>14</td>
<td>Date/time of Observation</td>
<td>199606130813</td>
<td>timestamp</td>
</tr>
<tr class="even">
<td></td>
<td>16</td>
<td>Observer</td>
<td>10</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>NTE</strong></td>
<td>1</td>
<td>Set ID</td>
<td>1</td>
<td>set ID</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Source of Comment</td>
<td>P</td>
<td>table 105</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Comment</td>
<td>Worth the risk</td>
<td>formatted text</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZRX</strong></td>
<td>1</td>
<td>Previous Order #</td>
<td>2355</td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Nature of Order</td>
<td>W</td>
<td>set of codes</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Reason Order Created</td>
<td>N</td>
<td>set of codes</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Routing</td>
<td>W</td>
<td>set of codes</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Current User*</td>
<td>DUZ^NAME^99NP</td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>IV Identifier</td>
<td>IV</td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>ZSC</strong></td>
<td>1</td>
<td>Service Connected</td>
<td>SC</td>
<td>coded element</td>
</tr>
<tr class="even">
<td><strong>}</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

\*- Fields marked with an asterisk require special escaping characters in order to send and receive the correct data contained in an HL7 message. See Special Escaping Characters for details.

\*\*-RXC Segment Field 5 "Additive Frequency" applies only to additives used to specify IV bag information.

> **NOTE:** The following are definitions of some of the data fields under the FIELD NAME column.

SENDING APPLICATION is the name of the VistA package generating the message; RECEIVING APPLICATION is the name of the VistA package that is the intended recipient of the message. SENDING FACILITY and RECEIVING FACILITY are the station numbers.

PATIENT ID is the patient IEN in the PATIENT file (#2).

PATIENT LOCATION, for an inpatient, is Hospital Location IEN^Room^Bed. For an outpatient, it is the Hospital Location IEN. In both cases, this is the location from which the order is being placed.

APPOINTMENT DATE/TIME is for Inpatient Medication orders for Outpatients. This is the appointment date/time that this order is associated with.

PLACER ORDER NUMBER is the OE/RR order number.

FILLER ORDER NUMBER is the Pharmacy order number.

ORDERING PROVIDER is the IEN in the NEW PERSON file (#200).

ORDER STATUS identifies the current status of the order. Codes from table 38, located in HL7 V. 2.3, that will be used, and those added, include:

> IP = pending

> CM = finished/verified by pharmacist (active)

> DC = discontinued

> RP = replaced

> HD = on hold

> ZE = expired

> ZS = suspended (active)

> ZU = un-suspended (active)

> ZX = unreleased

> ZZ = renewed

QUANTITY/TIMING contains the give amount, schedule, duration, start and stop times, and priority for the order, as well as the actual text of the dose ordered. The quantity field is delimited with '&' as:

Total Dose & Unit & Give Amount & Unit & Text & Dispense Drug

By using the quantity and conjunction fields, orders with multiple schedules may be sent. For outpatient orders, multiple schedules will be sent delimited by '~' and combined into a single signature (SIG); an inpatient order with multiple schedules will be sent as separate orders for each schedule. The conjunction will be S (then), A (and), or X (except).

REQUESTED GIVE CODE identifies a combination of the drug and dosage form in the format of a universal service ID. The last three pieces (alternate components) are used to identify an entry in the PHARMACY ORDERABLE ITEM file (#50.7).

PROVIDER'S PHARMACY INSTRUCTIONS are text instructions from the provider to the pharmacist; these are passed in an NTE segment following a RXO segment with an ID of 6.

PROVIDER'S ADMINISTRATION INSTRUCTIONS are Outpatient Pharmacy's "Patient Instructions" if the provider wishes to include them with the order; these are passed in an NTE segment following a RXO or RXE segment with an ID of 7.

REQUESTED DISPENSE CODE identifies the drug ordered as it maps to the National Drug File (NDF) and to the local drug file. The first three pieces identify a VA Product Name entry in the NDF, the last three pieces (alternate components) are used to identify an entry in the DRUG file (#50). The 'code' field (piece 1) of the NDF portion uses two numbers, separated by a period, to identify VA Generic Name and VA Product Name. The fourth piece uses the IEN of the DRUG file (#50) to identify a dispensed drug. This field will be blank if a pharmacy orderable item, but no dispensed drug, was selected.

REQUESTED DISPENSE AMOUNT is used to pass the amount that was entered in the QUANTITY field (#7) for an outpatient order.

REQUESTED GIVE PER is used to pass the amount that was entered in the DAYS SUPPLY field (#8) for an outpatient order.

ROUTE uses the IEN of the MEDICATION ROUTES file (#51.1) to identify a route. To truly be HL7 compatible, the MEDICATION ROUTES file (#51.1) should be mapped to the four route fields identified in HL7 V. 2.3 Section 4.8.3.

In the case of an order for IV Fluids, the REQUESTED GIVE CODE will be PS-1^IV^99OTH. This will indicate that the order is for IV fluids and the solutions and additives will be found in the RXC segment.

The RXC segment may repeat, once for each solution and additive in an IV order. The RX COMPONENT TYPE is B for a solution and A for an additive.

The COMPONENT CODE identifies additives and solutions by their IEN in the PHARMACY ORDERABLE ITEM file (#50.7).

COMPONENT UNITS uses 99OTH codes to map the IV Additive units.

The OBX segment is used if there was a positive order check that the physician chose to override.

The special code, 38^Critical Drug-drug interaction^99OCX, is used to identify this OBX segment in the OBSERVATION ID data field, and the OBSERVATION VALUE data field contains the actual order check message displayed to the provider; the OBX segment will be followed by a NTE segment, if an override reason was entered.

A Z-segment (ZRX) is used to pass additional data on new orders:

- PREVIOUS ORDER NUMBER identifies the order being edited or renewed by the current order; for front-door orders this will be the Pharmacy order number, and for back-door orders it will be the Order Entry order number.
- NATURE OF ORDER may be (W)ritten, (V)erbal, (P)honed, (S)ervice Correction, (X) Rejected, (D)uplicate, Pol(I)cy, (A)uto, or (E)lectronically entered.
- REASON the order was created may be (N)ew, (E)dit, or (R)enew.
- ROUTING may be (W)indow, (M)ail, or (C)linic.
- CURRENT USER identifies the user currently on the system performing the actions on the order.
- IV IDENTIFIER will indicate a fluid (IV), Total Parenteral Nutrition (TPN), or IV med ("").

A Z-segment (ZSC) is used for service connection, as this must be at the individual order level; values may be either SC or NSC.

### Order Event Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tables identify the HL7 data fields that are passed in each kind of event associated with OE/RR. For each event there is an order control code and a set of data fields listed. For any given event; however, some of the data fields may be empty (provider instructions, for example). Pharmacy may wish to send additional data fields in a RXE segment.

The protocols identified in the tables use OE/RR name spacing conventions. The messages sent by OE/RR will use the OR name spaced protocols indicated. Individual packages may use whatever protocol names they wish.

#### Front Door - Inpatient Medications

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><em>Action</em></th>
<th><em>Request from OE/RR</em></th>
<th><em>Pharmacy accepts</em></th>
<th><em>Pharmacy rejects</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td>PS EVSEND OR</td>
<td>PS EVSEND OR</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>NW (new order)</p>
<p>XO (change)</p></td>
<td><p>OK (accepted)</p>
<p>XR (new order)</p></td>
<td><p>UA (unable to accept)</p>
<p>UX (unable to change)</p></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,7,9,10,12,15,16</p>
<p>RXO: 1,10</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>OBX: 1,2,3,5,14,16</p>
<p>ZRX: 1,2,3</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,12,15,16</p>
<p>RXE: 2</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>ZV (verified)</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3,19</p>
<p>ORC: 1,2,3,11,15</p></td>
<td>There is no return event.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td>PS EVSEND OR</td>
<td>PS EVSEND OR</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>CA (cancel)</p>
<p>DC (discontinue)</p>
<p>HD (hold)</p>
<p>RL (release)</p>
<p>SS (send status)</p></td>
<td><p>CR (cancelled)</p>
<p>DR (discontinued)</p>
<p>HR (held)</p>
<p>OR (released)</p>
<p>SC (status update)</p></td>
<td><p>UC (unable to cancel)</p>
<p>UD (unable to dc)</p>
<p>UH (unable to hold)</p>
<p>UR (unable to release)</p>
<p>DE (data errors)</p></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3,19</p>
<p>ORC: 1,2,3,10,12,15,16</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p>
<p>RXE: 1</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
</tbody>
</table>

OE/RR will use CA to cancel orders, which have not been finished by Pharmacy; DC will be used for orders that have been finished.

Example: Digoxin .125 mg QAM*<u>New Order</u>*

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165

> 101-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> ORC\|NW\|12613;1^OR\|\|\|\|\|2&MG&1&TABLET&2 MG&58^BID&01-13

> ^^200803050100-0600^^R^C^2 MG^~\|\|200803041650-0600\|11884\|\|11884\|\|\|20080304165101

> -0600\|I^POLICY^99ORN^^^

> RXO\|^^^81^BIPERIDEN TAB ^99PSP\|\|\|\|\|\|\|\|\|785.4409^^99ND

> F^58^^99PSD

> RXR\|^^^1^ORAL (BY MOUTH)^99PSR

> ZRX\|\|I\|N

*<u>Verified by Nursing staff</u>*

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165

> 253-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> ORC\|ZV\|12613^OR\|2929P^PS\|\|\|\|\|\|\|\|11884\|\|\|\|200803041652

> 53-0600

*<u>Discontinue Order</u>*

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165

> 754-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> ORC\|DC\|12614;2^OR\|54U^PS\|\|\|\|\|\|\|11884\|\|11884\|\|\|2008030

> 4165754-0600\|I^POLICY^99ORN^14^Requesting Physician Cancelled^99ORR

#### Back Door - Inpatient Medications

Back door orders are handled by sending OE/RR the RDE message (pharmacy encoded order) with a 'send number' order control code. This allows OE/RR to store the order in its database and return the OE/RR order number to pharmacy with a 'number assigned' order control code. OE/RR cannot actually reject pharmacy events. The 'data errors' order control code is just used as some way to communicate to pharmacy that OE/RR could not interpret the RDE message. This should generally not happen.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 28%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><em>Action</em></th>
<th><em>Event from Pharmacy</em></th>
<th><em>OE/RR accepts</em></th>
<th><em>OE/RR rejects</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td>OR EVSEND PS</td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SN (send number)</p>
<p>ZC (conversion)</p></td>
<td>NA (number assigned)</td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,3,5,9,10,12,15,16</p>
<p>RXO: 1</p>
<p>RXE: 1,2,25,26</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>ZRX: 1,2,3,5</p></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3</p></td>
<td><p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SC (finished)</p>
<p>RO (finished/replaced)</p>
<p>XX (order changed)</p></td>
<td>ORC-5 = CM (active)</td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,</p>
<p>16</p>
<p>RXO: 1</p>
<p>RXE: 1,2,25,26</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>ZRX: 1,2,3,5</p></td>
<td>There is no return event. OE/RR must accept the instruction from Pharmacy.</td>
<td><p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>ZV (verified)</td>
<td></td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,11,15</p></td>
<td>There is no return event. OE/RR must accept the instruction from Pharmacy.</td>
<td><p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>OC (cancel)</p>
<p>OD (discontinue)</p>
<p>OH (hold)</p>
<p>OR (release)</p>
<p>SC (status change)</p></td>
<td></td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,12,15,16</p>
<p>RXE: 1</p>
<p>ZRX: 2,5</p></td>
<td>There is no return event. OE/RR must accept the instruction from Pharmacy.</td>
<td><p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
</tbody>
</table>

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/087.png)Note: The following are Order Control Codes:

OC - order cancelled before pharmacist verification

OD - order cancelled after pharmacist verification

SC - sent by pharmacy when order is verified, expired, or suspended

XX - sent by pharmacy when fields change that do not generate new order

Example: Digoxin .125 mg QAM*<u>New Order from Pharmacy through backdoor</u>*

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\|

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SN\|^OR\|2934P^PS\|\|IP\|\|^Q4H&01-05-09-13-17-21^^^^^C

> \|\|200803041715-0600\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|200803041700-0600\|W^W

> ritten^99ORN^^^\|\|

> RXO\|^^^81^BIPERIDEN TAB^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|2&MG&1&^Q4H&01-05-09-13-17-21^^200803041700-0600^

> 200803190000-0600^^C^2 MG\|785.4409^BIPERIDEN HCL 2MG TAB^99NDF^58^BIPERIDEN 2MG

> TAB^99PSD\|\|\|^^^20^MG^99PSU\|^^^63^TAB^99PSF\|\|\|\|\|\|\|\|11884^PROVIDER,INPATIENT

> \>\>\>^99NP\|\|\|\|\|\|\|^01-05-09-13-17-21^99PSA^^^\|\|\|\|2\|

> RXR\|^^^30^ORAL^99PSR\|\|\|

> ZRX\|\|W\|N\|\|11884^PROVIDER,INPATIENT^99NP\|

*<u>Order has expired</u>*

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\|

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SC\|12617;1^OR\|55U^PS\|\|ZE\|\|^NOW&^^^^^O\|\|2008030417

> 07-0600\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|200803041700-0600\|^^99ORN^^BCMA E

> XPIRED^\|\|

> RXO\|^^^81^BIPERIDEN TAB^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|2&MG&1&^NOW&^^200803041700-0600^20080304170847-06

> 00^R^O^2 MG\|785.4409^BIPERIDEN HCL 2MG TAB^99NDF^58^BIPERIDEN 2MG TAB^99PSD\|\|\|^^

> ^20^MG^99PSU\|^^^63^TAB^99PSF\|\|\|\|\|\|\|\|11884^PROVIDER,INPATIENT^99NP\|\|\|\|\|\|\|^^

> \>\>\>99PSA^^^\|\|\|\|2\|^^^20^MG^99PSU

> RXR\|^^^1^ORAL (BY MOUTH)^99PSR\|\|\|

> ZRX\|\|\|N\|\|11884^PROVIDER,INPATIENT^99NP\|

*<u>Front door order has been finished and verified by Pharmacy</u>*

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\|

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SC\|12618^OR\|56U^PS\|\|CM\|\|^Q4H&01-05-09-13-17-21^^^

> ^^C\|\|200803041715-0600\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|200803041700-0600\|

> ^^99ORN^^^\|\|

> RXO\|^^^81^BIPERIDEN TAB^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|2&MG&1&^Q4H&01-05-09-13-17-21^^200803041700-0600^

> 200803190000-0600^^C^2 MG\|785.4409^BIPERIDEN HCL 2MG TAB^99NDF^58^BIPERIDEN 2MG

> TAB^99PSD\|\|\|^^^20^MG^99PSU\|^^^63^TAB^99PSF\|\|\|\|\|\|\|\|11884^PROVIDER,INPATIENT

> \>\>\>^99NP\|\|\|\|\|\|\|^01-05-09-13-17-21^99PSA^^^\|\|\|\|2\|

> RXR\|^^^30^ORAL^99PSR\|\|\|

> ZRX\|\|\|\|\|11884^PROVIDER,INPATIENT^99NP\|

#### Front Door - IV Fluids

IV fluid orders use a RXC segment to contain information about solutions and additives. Therefore, a special code is sent in a RXO segment;1 to identify the order as an IV order (PS-1^IV Order^99OTH). Since RXC segments are used, the give fields in a RXO segment are unnecessary.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Action</strong></em></th>
<th><em><strong>Request from OE/RR</strong></em></th>
<th><em><strong>Pharmacy accepts</strong></em></th>
<th><em><strong>Pharmacy rejects</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td>PS EVSEND OR</td>
<td>PS EVSEND OR</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>NW (new order)</p>
<p>XO (changed order)</p></td>
<td><p>OK (accepted)</p>
<p>XR (new order)</p></td>
<td><p>UA (unable to accept)</p>
<p>UX (unable to change)</p></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,7,9,10,12,15,16</p>
<p>RXO: 1,2</p>
<p>NTE: 1,2,3</p>
<p>RXC: 1,2,3,4,5</p>
<p>OBX: 1,2,3,5,14,16</p>
<p>ZRX: 1,2,3</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,12,15,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>ZV (verified)</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,11,15</p></td>
<td>There is no return event.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td>PS EVSEND OR</td>
<td>PS EVSEND OR</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>CA (cancel)</p>
<p>DC (discontinue)</p>
<p>HD (hold)</p>
<p>RL (release)</p>
<p>SS (send status)</p></td>
<td><p>CR (canceled)</p>
<p>DR (discontinued)</p>
<p>HR (held)</p>
<p>OR (released)</p>
<p>SC (status update)</p></td>
<td><p>UC (unable to cancel)</p>
<p>UD (unable to dc)</p>
<p>UH (unable to hold)</p>
<p>UR (unable to release)</p>
<p>DE (data errors)</p></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,10,12,15,16</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
</tbody>
</table>

Example: POTASSIUM CHLORIDE INJ,SOLN FOR IV ORDERS 125 MEQ inSODIUM INJ,SOLN FOR IV ORDERS 1000 ml 100 ml/hr*<u>New Order CPRS Continuous</u>*

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304170

> 224-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> ORC\|NW\|12615;1^OR\|\|\|\|\|^^^^^R\|\|200803041702-0600\|11884

> \|\|11884\|\|\|20080304170224-0600\|I^POLICY^99ORN^^^

> RXO\|^^^PS-1^IV^99OTH\|333 ml/hr

> RXR\|^^^14^INTRAVENOUS^99PSR

> RXC\|B\|^^^196^DEXTROSE INJ,SOLN ^99PSP\|50\|^^^PSIV-1^ML

> ^99OTH

> RXC\|A\|^^^435^MORPHINE INJ ^99PSP\|33\|^^^PSIV-1^ML^99OT

> H\|1,3

> ZRX\|\|I\|N\|\|\|C

*<u>New Order CPRS Intermittent</u>*

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304170

> 224-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> ORC\|NW\|12616;1^OR\|\|\|\|\|^BID&01-13^^^^R\|\|200803041702-0

> 600\|11884\|\|11884\|\|\|20080304170224-0600\|I^POLICY^99ORN^^^

> RXO\|^^^PS-1^IV^99OTH\|

> RXR\|^^^15^INTRAMUSCULAR^99PSR

> RXC\|B\|^^^196^DEXTROSE INJ,SOLN ^99PSP\|500\|^^^PSIV-1^M

> L^99OTH

> RXC\|A\|^^^281^FUROSEMIDE INJ,SOLN ^99PSP\|33\|^^^PSIV-4^

> MG^99OTH\|1,3

> ZRX\|\|I\|N\|\|\|I

#### Back Door - IV Fluids

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Action</strong></em></th>
<th><em><strong>Event from Pharmacy</strong></em></th>
<th><em><strong>OE/RR accepts</strong></em></th>
<th><em><strong>OE/RR rejects</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td>OR EVSEND PS</td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SN (send number)</p>
<p>ZC (conversion)</p></td>
<td>NA (number assigned)</td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,3,5,9,10,12,15,16</p>
<p>RXE: 1,23,24</p>
<p>RXC: 1,2,3,4,5</p>
<p>ZRX: 1,2,3,5,6</p></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3</p></td>
<td><p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SC (finished)</p>
<p>XX (order changed)</p></td>
<td></td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,16</p>
<p>RXE: 1,23,24</p>
<p>NTE: 1,2,3</p>
<p>RXC: 1,2,3,4,5</p>
<p>ZRX: 1,2,3,5,6</p></td>
<td>There is no return event. OE/RR must accept the instruction from Pharmacy.</td>
<td><p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td>OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>OC (cancel)</p>
<p>OD (discontinue)</p>
<p>OH (hold)</p>
<p>OR (release)</p>
<p>SC (status change)</p></td>
<td></td>
<td>DE (data errors)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,16</p>
<p>RXE: 1</p>
<p>ZRX: 2,5</p></td>
<td>There is no return event. OE/RR must accept the instruction from Pharmacy.</td>
<td><p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p></td>
</tr>
</tbody>
</table>

Example: POTASSIUM CHLORIDE INJ,SOLN FOR IV ORDERS 125 MEQ inSODIUM INJ,SOLN FOR IV ORDERS 1000 ml 100 ml/hr*<u>New Order Continuous</u>*

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\|

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SC\|12619^OR\|46V^PS\|\|CM\|\|^&^^^^^\|\|200803041719-060

> 0\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|200803041900-0600\|W^Written^99ORN^^^\|\|

> RXO\|^^^435^MORPHINE INJ^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|^&^^200803041900-0600^200803100000-0600^\|\|\|\|\|\|\|\|\|

> \|\|\|\|11884^PROVIDER,INPATIENT^99NP\|\|\|\|\|\|\|^^99PSA^^^\|\|300\|^^^^ml/hr^PSU\|\|

> RXC\|A\|^^^435^MORPHINE^99PSP\|20\|^^^PSIV-1^ML^99OTH\|1,3\|\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXC\|B\|^^^196^DEXTROSE^99PSP\|1000\|^^^PSIV-1^ML^99OTH\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXR\|^^^14^INTRAVENOUS^99PSR\|\|\|

> ZRX\|\|W\|N\|\|11884^PROVIDER,INPATIENT^99NP\|C

*<u>New Order Intermittent</u>*

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\|

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SC\|12620^OR\|47V^PS\|\|CM\|\|^Q4H&01-05-09-13-17-21^^^

> ^^\|\|200803041721-0600\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|200803041700-0600\|W

> ^Written^99ORN^^^\|\|

> RXO\|^^^281^FUROSEMIDE INJ,SOLN^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|^Q4H&01-05-09-13-17-21^^200803041700-0600^2008030

> 60000-0600^\|\|\|\|\|\|\|\|\|\|\|\|\|11884^PROVIDER,INPATIENT^99NP\|\|\|\|\|\|\|^01-05-09-13-17-21^99PSA^^^

> \|\|INFUSE OVER 300 MINUTES\|\|\|

> RXC\|A\|^^^281^FUROSEMIDE^99PSP\|250\|^^^PSIV-4^MG^99OTH\|1,3

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXC\|B\|^^^196^DEXTROSE^99PSP\|1000\|^^^PSIV-1^ML^99OTH\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXR\|^^^160^IV PIGGYBACK^99PSR\|\|\|

> ZRX\|\|W\|N\|\|11884^PROVIDER,INPATIENT^99NP\|I

### Special Escaping Characters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard HL7 field delimiters represented by the "~ , &, \| " (tilde, ampersand, pipe) characters as well as the commonly used VistA "^" (caret) are sometimes needed by users of Inpatient Medications in various fields to provide complete information about a patient or order. The use of these characters can cause sending and receiving software to format HL7 messages incorrectly, and/or construct/deconstruct the information incorrectly. Data loss can also occur if data is truncated at one of the special delimiter characters.

The following fields require special escaping characters.

- Patient ID - PID segment / piece 3
- Patient Name - PID segment / piece 5
- Schedule - ORC segment / piece 7 / subpiece 2
- Text - ORC segment / piece 7 / subpiece 8
- Requested Give Code - RXO segment / piece 1 / subpiece 5
- Requested Dispense Code - RXO segment / piece 10 / subpieces 2 and 4
- Schedule - RXE segment / piece 1 / subpiece 2
- Text - RXE segment / piece 2 /subpiece 8
- Comment - NTE segment / piece 3
- Route - RXR segment / piece 1 / subpiece 5
- Component Code - RXC segment / piece 2 / subpiece 5
- Component Units - RXC segment / piece 4 / subpiece 4
- Observation Value - OBX segment / piece 5
- Current User - ZRX segment / piece 5 / subpieces 1 and 2

See External Relationships for the components used to escape and unescape characters.

## STAT, ASAP, and NOW Order Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A STAT, ASAP, and NOW Order Notification has been added in Inpatient Medications to notify pharmacy and nursing staff when orders are received with a priority of STAT and ASAP or a schedule of STAT and NOW. The Notification sends a text message when a pending STAT, ASAP, or NOW order has either been received from CPRS or has been verified and made active. To receive these messages, the user must subscribe to the mail group(s) listed in this section.

There are three parameters that can be defined to control which priorities / schedules are used to produce these notifications.

The SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, PRIORITIES FOR PENDING NOTIFY parameter will control what priority or schedule of an order will cause a notification when the order is PENDING.

The SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, PRIORITIES FOR ACTIVE NOTIFY parameter will control what priority or schedule of an order will cause a notification when the order is ACTIVE.

The INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option, PRIORITIES FOR NOTIFICATION parameter will control what priority or schedule of an order will cause a notification when the order is PENDING or ACTIVE for each individual WARD.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/088.png)Note: If all three parameters are left blank, then STAT, ASAP, and NOW orders will cause notifications. If the PRIORITIES FOR PENDING NOTIFY parameter is set and the other parameters left blank, then the PRIORITIES FOR PENDING NOTIFY parameter will control what priorities are sent.

### PSJ STAT NOW PENDING ORDER Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This mail group notifies subscribers when a pending STAT or NOW order has been received from CPRS.

Example: Messages in subscriber's Inbox

\*207. GEN MED-PENDING STAT-PSJPATIENT1,ONE MEDICATIONS,INPATIENT

\*208. GEN MED-PENDING NOW-PSJPATIENT1,ONE MEDICATIONS,INPATIENT

Example: Pending STAT Order Message

Subj: GEN MED-PENDING STAT-PSJPATIENT1,ONE \[#88119\] 04/02/04@08:30 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket.

Page 1 \*New\*

------------------------------------------------------------------------

Inpatient Medications has received the following STAT order (PENDING)

Patient: PSJPATIENT1,ONE (0001)

Order Information: SODIUM POLYSTYRENE SULF 15GM ONCE

Order Date: 04/02/04 08:30

Enter message action (in IN basket): Ignore//

Example: Pending NOW Order Message

Subj: GEN MED-PENDING NOW-PSJPATIENT1,ONE \[#88124\] 04/02/04@08:51 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket.

Page 1 \*New\*

-----------------------------------------------------------------------

Inpatient Medications has received the following NOW order (PENDING)

Patient: PSJPATIENT1,ONE (0001)

Order Information: DIGOXIN 0.25MG NOW

Order Date: 04/02/04 08:51

Enter message action (in IN basket): Ignore//

### PSJ STAT NOW ACTIVE ORDER Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This mail group notifies subscribers when a pending STAT or NOW order is made active.

Example: Messages in subscriber's Inbox

\*209. GEN MED-ACTIVE STAT-PSJPATIENT1,ONE MEDICATIONS,INPATIENT

\*210. GEN MED-ACTIVE NOW-PSJPATIENT1,ONE MEDICATIONS,INPATIENT

Example: Active STAT Order Message

Subj: GEN MED-ACTIVE STAT-PSJPATIENT1,ONE \[#88125\] 04/02/04@08:53 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket.

Page 1 \*New\*

-----------------------------------------------------------------------

Inpatient Medications has received the following STAT order (ACTIVE)

Patient: PSJPATIENT1,ONE (0001)

Order Information: SODIUM POLYSTYRENE SULF 15GM ONCE

Order Date: 04/02/04 08:30

Enter message action (in IN basket): Ignore//

Example: Active NOW Order Message

Subj: GEN MED-ACTIVE NOW-PSJPATIENT1,ONE \[#88127\] 04/02/04@08:57 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket.

Page 1 \*New\*

----------------------------------------------------------------------

Inpatient Medications has received the following NOW order (ACTIVE)

Patient: PSJPATIENT1,ONE (0001)

Order Information: DIGOXIN 0.25MG NOW

Order Date: 04/02/04 08:51

Enter message action (in IN basket): Ignore//

### Adding a Remote Member as a Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STAT and NOW Order Notification mail groups can be set up to send text messages to a remote device. This enables anyone who has subscribed to these mail groups to use a pager, or any device that can receive an email message, to receive notification quickly when these high-priority orders are received. The following example illustrates how to define a remote device for a mail group using FileMan.

Example: Using FileMan to Define a Remote Device (for the PSJ STAT NOW ACTIVE ORDER mail group)

VA FileMan 22.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: MAIL GROUP// \<Enter\>

EDIT WHICH FIELD: ALL// MEMBERS - REMOTE (multiple)

EDIT WHICH MEMBERS - REMOTE SUB-FIELD: ALL//

THEN EDIT FIELD:

Select MAIL GROUP NAME: PSJ STAT NOW ACTIVE ORDER

Select REMOTE MEMBER: ?

You may enter a new MEMBERS - REMOTE, if you wish

Enter a remote address (name@domain) or local device (D.device or

H.device) or local server (S.server).

Select REMOTE MEMBER: PSJPROVIDER.ONE@sprintpcs.com

Are you adding 'PSJPROVIDER.ONE@SPRINTPCS.COM' as

a new MEMBERS - REMOTE (the 1ST for this MAIL GROUP)? No// Y (Yes)

Select REMOTE MEMBER:

### Setting Up Ward-Specific Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A site may prefer to send active order notifications only to pharmacy and the ward the patient is on. In this case, set up the mail group in the INPATIENT WARD PARAMETERS file (#59.6).

# Inpatient Medications and BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications is designed for use with the Bar Code Medication Administration (BCMA) package.

## API Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient and order information is exchanged between Inpatient Medications and BCMA. This exchange is possible through Application Program Interfaces (APIs).

### APIs provided to BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJBCMA - The entry point EN^PSJBCMA is provided by the Inpatient Medications package to return patient active orders to BCMA to be used in administering medications at patient's bedside. The SEND TO BCMA field (#3) in the CLINIC DEFINITION file (#53.46) allows the user to specify, by clinic, whether or not Inpatient Medication Orders for Outpatients will be sent to BCMA.

PSJBCMA1 - The entry point EN^PSJBCMA1 is provided by the Inpatient Medications package to return the detail information on a patient's order for BCMA to use.

PSJBCMA2 - The entry point EN^PSJBCMA2 is provided by Inpatient Medications package to return a patient order's activity logs for BCMA to use.

PSJBCMA3 - The purpose of this API is to get information from BCMA to put in the PHARMACY PATIENT FILE (#55). It also updates the BCMA status information for the bag associated with a Unique Bar Code ID label.

PSJBCMA4- The purpose of this API is to allow BCMA to expire/reinstate Inpatient Medications orders based on an administration event.

PSJBCMA5 – The entry point GETSIOPI is provided by the Inpatient Medications package to return the Special Instructions or the Other Print Info associated with a specific Inpatient Medications order. The returned values will be retrieved from the word processing SPECIAL INSTRUCTIONS (LONG) field (#135) in the UNIT DOSE multiple (#62) in the PHARMACY PATIENT file (#55) for Unit Dose orders, or the OTHER PRINT INFO (LONG) – field (#154) in the IV multiple (#100) in the PHARMACY PATIENT file (#55).

PSGSICH1 - The entry point GETPROVL^PSGSICH1 is provided by the Inpatient Medications package to return CPRS Provider Overrides associated with a specific Inpatient Medications order. Entry point INTRDIC^PSGSICH1 is provided by the Inpatient Medications package to return Pharmacist Interventions associated with a specific Inpatient Medications order.

### APIs provided to Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EN^PSBIPM - The entry point EN^PSBIPM is provided by the BCMA package to provide information to Inpatient Medications to be used in determining the start date for a renewed order. \[Database Integration Agreement (DBIA) \# 3174\].

MOB^PSBIPM - The entry point MOB^PSBIPM is provided by the BCMA package to provide Inpatient Medications with an array of data returned by the BCMA/CPRS Med Order function.

MOBR^PSBIPM - The entry point MOBR^PSBIPM is provided by the BCMA package to provide Inpatient Medications a way to notify BCMA that the BCMA/CPRS Med Order Button order has been processed or rejected. There is no return from this entry point.

## Med Order Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA/CPRS Med Order Button (Med Order) software is an integrated component of the VistA environment and uses bar code technology to electronically order, sign, and document STAT and NOW medications from verbal or telephoned medication orders for inpatients from the BCMA Virtual Due List (VDL). Medications are ordered and signed through the CPRS Inpatient Medication order dialog and are passed to the Inpatient Medications V. 5.0 software application as nurse-verified orders with the Priority of Done. The medications are documented as administered to the patient in the BCMA Medication Log and Medication Administration History (MAH).

The BCMA VDL has been modified to contain a Med Order button that allows the authorized user the ability to properly document a STAT or NOW medication order through BCMA. Each user must hold a special key to allow them access to the button on the BCMA VDL. There is a system parameter in BCMA that allows the site the added ability to turn off or on the functionality system wide.

When the Med Order button is activated, BCMA opens a CPRS Graphical User Interface (GUI) medication dialog ordering session. The medication dialog screen allows for the entry of STAT or NOW Unit Dose or IV Type orders within the same session. The user is able to scan a bar coded IEN or National Drug Code (NDC) number affixed to the product, to select the dispense drug for this administration. Pharmacy Orderable item, IV Additive, and IV Solution selection (based on dispense drug) occurs in the background and is automatic. Dispense drugs selected for IV Type orders that point to multiple active IV Additive or IV Solution file links require the user to make a single selection. Manual entry of the dispense drug into the medication field is allowed if bar codes are damaged or missing.

All orders entered through this interface are automatically marked as "Done" in CPRS GUI. Unit Dose, Piggyback, and Syringe (intermittent) orders are marked as "GIVEN" in BCMA and will not appear on the BCMA VDL. IV Type orders including Admixture and Syringe (non-intermittent) are marked as "INFUSING" in BCMA and will appear on the BCMA VDL for further interaction. CPRS GUI passes the order to Inpatient Medications for pharmacist verification. Order administration data will still be available to be edited through the BCMA menu option Edit Medication Log. All orders require an electronic signature.

The administration date/time box on the order screen defaults to the time the Med Order button was accessed. The user is allowed to edit this date/time to a date/time in the past since some STAT and NOW orders are actually entered after they are administered. The user will NOT be allowed to enter a date/time in the future.

Once the Unit Dose or IV Type order is entered and the accept order button is selected, the user will be taken back to the order screen to specify ordering dialog and enter additional orders.

When the medication entry is completed, the CPRS GUI Review/Sign Changes screen will display all STAT and NOW orders entered during this input session. The user is required to select Telephoned or Verbal as the Nature of Order. Nature(s) of order Policy, Hold until signed, and Signed on Chart will NOT appear on this screen.

After selecting the appropriate Nature of Order the nurse will click on the OK button. When any entered order triggers a critical Order Check, the Order Check screen will display for the user. These Order Checks screens appear based on the medications selected during the ordering process. Some Order Checks may require Comments prior to selecting the continue button. The user is required to enter justification for overriding existing Order Checks or the user will be allowed to cancel the selected order.

The user is then required to enter their electronic signature code to release orders to Inpatient Medications. The user will then be returned to the BCMA VDL.

When the OK button on the Electronic Signature screen is selected, an entry will be created on the MAH and the Medication Administration Log in BCMA for the orders entered. In addition, the Medication Administration Log will display the following text with the order "BCMA /CPRS Interface Entry." The following actions will then take place:

BCMA will pass the administration date/time information to Inpatient Medications for display to the pharmacist who verifies the order. The administration data will be displayed in the order view by BCMA LAST ACTION: Date, Time, and Status.

A DONE priority code for inpatient orders will be created by CPRS and passed with nurse‑verified orders to Inpatient Medications. The DONE priority displays on the Inpatient Profiles with a "d" immediately preceding the order within Inpatient Medications. In addition, the Unit Dose and IV Verification screens display "EXPIRED UNIT DOSE or IV (DONE)" in the upper left-hand corner of the order screen. All Inpatient Medications profile print options used prior to the order being verified (profile and expanded view) will reflect "d" or the "DONE" priority.

The administration information is passed to Inpatient Medications. Inpatient Medications displays the administration information to the pharmacist during the order verification process. Administration Date/Time is used as the Start Date/Time and Stop Date/Time for all Med Order button orders. The only allowable Inpatient Medications actions on this nurse-verified order would be "VF" Verify and "AL" Activity Log. The pharmacist is given an opportunity to enter a progress note after verifying this order. The pre-exchange doses prompt for Unit Dose orders defaults to 0, since no doses will need to be delivered to complete this administration. The IV label print prompt for IV Type orders defaults to "B" for BYPASS, since no IV labels will need to be delivered to complete this administration. The only allowable Inpatient Medications actions on this pharmacist verified order would be "AL" Activity Logs, "CO" Copy, "N" Mark Not to be Given, and "I" Mark Incomplete. In order to support future Inpatient Medications enhancements to renewal orders, the "RN" Renew action will not be allowed.

# Interfacing with the Bar Code Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package includes an interface between the IV Medications module and the Bar Code label printer. The IV Medications module currently prints IV labels on a label printer. This interface allows a Unique Bar Code to be printed on the first line of the IV label.

Any printer that supports bar code printing can be used for the IV labels. However, the scan success rate will probably be lower if anything other than direct thermal transfer on synthetic labels is used. Labels from dot matrix printers, laser printers, or even barcode printers using other types of transfer, wipe off more easily. The label could become unreadable, especially in areas where the bag might become wet. With a direct thermal transfer onto a synthetic label, the print actually bonds to the label material. Essentially, the label would have to be ripped to damage the print.

## Hardware Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

## Software Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The type of printer will determine the next step. The Zebra printer requires Control Codes where the Dot Matrix or Laser printers do not require these codes. The IV label print routine checks the existence of the Control Codes before attempting to execute. It is not required for all Control Codes to be defined; just build the necessary Control Codes for the selected printer.

### Zebra Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For this type of printer to print a Unique Bar Code on the IV labels, IRM must build Control Codes. The CONTROL CODES fields are added to the TERMINAL TYPE file (#3.2) in the Kernel patch XU\*8\*205. This patch must be installed before proceeding.

#### Control Code Set Up

The IV label print uses twelve control codes presently. These control codes must be built with FileMan using the names listed in order for the routine to work correctly. These twelve codes are listed below:

| Code | Description         |
|----------|-------------------------|
| FI       | Format Initialization   |
| FE       | Format End              |
| SL       | Start of Label          |
| EL       | End of Label            |
| SB       | Start of Bar Code       |
| EB       | End of Bar Code         |
| SBF      | Start of Bar Code Field |
| EBF      | End of Bar Code Field   |
| ST       | Start of Text           |
| ET       | End of Text             |
| STF      | Start of Text Field     |
| ETF      | End of Text Field       |

Patch PSJ\*5\*178 provides the ability to make the medication route print on the IV labels as well as making it appear in a larger font than the other text. The following new control codes must be set up to provide this functionality:

| Code | Description       |
|----------|-----------------------|
| SM       | Start Med Route       |
| EM       | End Med Route         |
| SMF      | Start Med Route Field |
| EMF      | End Med Route Field   |

#### Pseudo-Code Listing

The following pseudo-code listing shows the flow and the points at which each of the CONTROL CODES are used. (It is not required for all Control Codes to be defined; just build the necessary Control Codes for the selected printer.)

1.  Label print routine invoked.
2.  CONTROL CODES loaded into local array PSJIO. Variable PSJIO defined to indicate whether or not CONTROL CODES exist.
3.  Format Initialization.
4.  If selected, header label printed.
    1.  Start of Label.
    2.  Start of Text.\*
    3.  Start of Text Field.\*
    4.  Text Information.\*
    5.  End of Text Field.\*
    6.  End of Text.\*
    7.  End of Label.
5.  IV label printed.
    1.  Start of Label.
    2.  Barcode unique ID assigned.
    3.  Print barcode.
        1.  If no CONTROL CODES, check for IOBARON and execute.
        2.  If CONTROL CODES, Start of Barcode, Start of Barcode Field.
        3.  Unique ID printed.
        4.  If no CONTROL CODES, check for IOBAROFF and execute.
        5.  If CONTROL CODES, End of Barcode Field, End of Barcode.
    4.  Start of Text.\*
    5.  Start of Text Field.\*
    6.  Text Information.\*
    7.  End of Text Field.\*
    8.  End of Text.\*
    9.  End of Label.
6.  Format End.

In the event the label text needs to continue on another label, the following CONTROL CODE sequence will be used.

1.  End of Label.
2.  Start of Label.

'\*' indicates items that may be executed repeatedly.

#### Example Set Up

The following is a setup example that was used in the development process. This example is provided to guide the user in this set up. Please note that it is only an example and may not hold true in all cases.

Example: Zebra Printer Example Set Up

NUMBER: 1 ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION CONTROL CODE: W "^XA",!,"^LH0,0^FS",!

NUMBER: 2 ABBREVIATION: SB

FULL NAME: START OF BARCODE

CONTROL CODE: W "^BY2,3.0^FO60,25^B3N,N,80,Y,N"

NUMBER: 3 ABBREVIATION: ST

FULL NAME: START OF TEXT

CONTROL CODE: W "^FO",PSJBARX,",",PSJBARY,"^A0N,30,20" S PSJBARY=PSJBARY+40

NUMBER: 6 ABBREVIATION: EB

FULL NAME: END OF BARCODE CONTROL CODE: S LINE=LINE+1,PSJBARY=130

NUMBER: 7 ABBREVIATION: STF

FULL NAME: START OF TEXT FIELD CONTROL CODE: W "^FD"

NUMBER: 8 ABBREVIATION: SBF

FULL NAME: START OF BARCODE FIELD CONTROL CODE: W "^FD"

NUMBER: 9 ABBREVIATION: ETF

FULL NAME: END OF TEXT FIELD CONTROL CODE: W "^FS",!

NUMBER: 10 ABBREVIATION: SL

FULL NAME: START OF LABEL

CONTROL CODE: W "^XA",! S PSJBARY=50,PSJBARX=60

NUMBER: 11 ABBREVIATION: EL

FULL NAME: END OF LABEL CONTROL CODE: W "^XZ",!

NUMBER: 12 ABBREVIATION: EBF

FULL NAME: END OF BARCODE FIELD CONTROL CODE: W "^FS",!

NUMBER: 13 CTRL CODE ABBREVIATION: SM

FULL NAME: START MED ROUTE

CONTROL CODE: W "^FO",PSJBARX,",",PSJBARY,"^A0N,36,30",!!

NUMBER: 14 CTRL CODE ABBREVIATION: EM

FULL NAME: END MED ROUTE CONTROL CODE: S PSJBARY=PSJBARY+40

NUMBER: 15 CTRL CODE ABBREVIATION: SMF

FULL NAME: START MED ROUTE FIELD CONTROL CODE: W "^FD"

NUMBER: 16 CTRL CODE ABBREVIATION: EMF

FULL NAME: END MED ROUTE FIELD CONTROL CODE: W "^FS",!

### Dot Matrix and Laser Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Control Codes in the TERMINAL TYPE file (#3.2) are not required for these printers. However, the BAR CODE ON and BAR CODE OFF fields in the TERMINAL TYPE file (#3.2) are needed.

An example of each field is shown below for the Output Technology Corporation (OTC) printers. Please note that it is only an example and may not hold true in all cases.

Example: OTC Printer Example

BAR CODE OFF: \$C(27),"\[0t",! BAR CODE ON: \$C(27),"\[4;4;0;2;4;2;4;2}",\$C(27),"\[3t"

## Printed Bar Code IV Label Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With this interface, a Unique Bar Code will be printed on the first line of the IV label with the label number printed below it. This label number is comprised of the patient IEN, a "V" as a delimiter, and the label sequential number for the patient (not the order). Depending upon the type of printer used, the asterisks (\*) may or may not be printed on either side of the label number.

Example: Bar Code IV Label Example

> ![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/089.png)

> \*520V452\*

> \[65\] 9111 ONE EAST 03/19/02

> PSJPATIENT1,ONE B-12

> ACETAMINOPHEN 100 MEQ

> 0.9% SODIUM CHLORIDE 100 ML

> Dose due at: \_\_\_\_\_\_\_\_

> ROUTE: INTRAVENOUS

> 100 ml/hr

> Fld by: \_\_\_\_ Chkd by: \_\_\_\_

> 1\[1\]

# Interfacing with the ATC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This initial version of Inpatient Medications includes an interface between the Unit Dose Medications module and the Automatic Tablet Counter (ATC) Unit Dose Dispensing machine. The Unit Dose Medications module currently allows the users to send their pick lists to the ATC. The interface allows for multiple ATCs, tying the ATCs to ward groups.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/090.png)Note: If a site elects to send Pick Lists to the ATC machine by ADMIN TIME, the following change must be made to the ATC machine parameter:

> At the password screen, enter \<F8\> for system parameter. Move over to the SORT parameter. The choices will be Time or Medication. Select Medication and press \<Enter\>.

## Pharmacy Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to send medication orders to the ATC, the Pharmacy must determine the Dispense Drugs that can be sent to the ATC and the pharmacy ward groups that will be sending pick lists to the ATC. This can be done before the ATC is set up or even delivered.

### Drug Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each drug that the pharmacy determines can be sent to the ATC, the pharmacy must enter a MNEMONIC, and enter a CANISTER NUMBER for each pharmacy ward group that will be sending the drug to an ATC. This can be assigned through the *Dispense Drug/ATC Set Up* \[PSSJU DRUG/ATC SET UP\] option. This option is no longer part of the Unit Dose *Supervisor'sMenu* \[PSJU FILE\]. It is sent out with the Pharmacy Data Management package as a stand-alone option. This option should be added to the menu of designated users on an as needed basis.

The pharmacy must also enter each drug into the ATC's software, giving each drug the same mnemonic entered into the Pharmacy Data Management package.

### Ward Group Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each ward group that will be sending to the ATC, the device name given to the ATC must be entered into the WARD GROUP file (#57.5). This can be assigned through the *Ward Groups* \[PSJU EWG\] option found within the Unit Dose *Supervisor's Menu* \[PSJU FILE\].

## Hardware Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the pharmacy to be able to send Unit Dose Medications orders to the ATC, the ATC must be set up as a device in the system. The ATC should be set up similar to a printer, but must be set up for two-way communication. Some of these corresponding settings must also be made in the ATC setup software. The following examples are provided to guide the user in this set up. Please note that they are only examples and may not hold true in all cases.

### Device File Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of a device file (#3.5) entry for the ATC. (The entry for the \$I field will more than likely be different at each site.) Only those fields to which data is entered are shown.

Example: Device File Entry for the ATC

LOCATION OF TERMINAL: ATC

\$I: 142

TYPE: TERMINAL

SUBTYPE: C-OTHER

DEFAULT SUBTYPE: C-OTHER// \<Enter\>

ASK DEVICE: YES// \<Enter\>

ASK PARAMETERS: YES// N (NO)

MARGIN WIDTH: 80// 255

FORM FEED: \#// \<Enter\>

PAGE LENGTH: 66// \<Enter\>

### MUX Table Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a Digital Standard MUMPS (DSM) example of a Multiplexer (MUX) table entry for the ATC. Please note that OUTPUT ONLY is set to NO.

Enter device number, or range of device numbers (NN:NN). Enter \<CR\> when done.

Parity Auto Modem Output Stall Lower

\| Baud Cntrl only Count Case

\| \| \| \| \| \|

Device \|CRT \| Rcvr Xmit \|ZUSE \| Login \| Tab \|Output Rtn Edit

Number \| \| \| Spd Spd \| \| \| \| \| \| \|Margin num Comment

-----------------------------------------------------------------------------

142 N Y N 9600 9600 N N N N 0 Y Y 255 2 N

142 N Y N 9600 9600 N N N N 0 Y Y 255 2 N

### DECServer Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples for setting up the ATC for DECServers:

Device Output Tab Lowcase CRT Login Output ZUSE Comment

Only Cntrl Cntrl Allowed Margin

---------------------------------------------------------------------------PORT_15@DSV1 N Y Y Y N 255 N ATC-212

---------------------------------------------------------------------------

SHO POR 15

Port 15: Server: DSV1

Character size: 8 Input Speed: 9600

Flow Control: XON Output Speed: 9600

Parity: None Modem Control: Disabled

Access: Remote Local Switch: None

Backward Switch: None Name: PORT_15

Break: Disabled Session Limit: 4

Forward Switch: None Type: HARD

Preferred Service: None

Authorized Groups: 0

(Current) Groups: 0

Enabled Characteristics:

Lock, Loss Notification, Message,...Verification

--------------------------------------------------------------------------------------

### Wiring for CXA16 Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2----------3

3----------2

7----------7

(Do not connect pin \#20)

### ATC-HPS Configuration Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the ATC software setup:

Host Port Set up (HPS) Configuration Settings

|                                        |           |       | Current                |
|----------------------------------------|-----------|-------|----------------------------|
| Baud Rate (9600, 4800, 1200)           |           | :     | 9600                       |
| Parity (S, M, E, O, N)                 |           | :     | O                          |
| Data Bits (7, 8)                       |           | :     | 7                          |
| Stop Bits (1, 2)                       |           | :     | 1                          |
| STX                                    | \(050\)   | :     | 050\*                  |
| PSOH                                   | \(052\)   | :     | 052\*                  |
| PETB                                   | \(053\)   | :     | 053\*                  |
| MSOH                                   | \(054\)   | :     | 054\*                  |
| METB                                   | \(055\)   | :     | 055\*                  |
| ETX                                | (051) | : | 013\* (most important) |
| ACK                                    | \(048\)   | :     | 048\*                  |
| NACK                                   | \(049\)   | :     | 049\*                  |
| Lineterm (1=On, 0=Off)                 |           | :     | 0                          |
| Drug Mnemonic Length (01, 02..., 15)   |           | :     | 04\*                   |
| Drug Mnemonic Mode (1=True, 0=False)   |           | :     | 0                          |
| Response Timer-Control (0, 1, 2..., 9) |           | :     | 0†                         |
| Response Timer-Data (0, 1, 2..., 9)    |           | :     | 0†                         |
| Wake-up (1=Yes, 0=No)                  |           | :     | 0                          |
| Flag Fixed Lngth Records (1=Yes, 0=No) |           | :     | 0                          |

> \* The Unit Dose Medications module is set up for the HPS Configuration Settings to be set as shown, and might not function properly if they are changed.

> † If the ATC is dropping the line, it might be necessary to increase these timers.

### Device File Setup Network Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the Device File (#3.5) for ATC Device to use Network Channel.

Obtain the IP address and port assignment for the Receiving Lantronix/TCP IP Interface.

Lookup the ATC Device setup for the Ward location(s):

Select Supervisor's Menu Option: ward Groups

Select WARD GROUP NAME:    4C 

PHARMACY     ATC

NAME: 4C//

Select WARD: 4C//

LENGTH OF PICK LIST (in hours):

PICK LIST - OMIT WARD SORT: NO (SORT BY WARD)//

PICK LIST - OMIT ROOM-BED SORT: YES (DO NOT SORT BY ROOM-BED)

         //

PICK LIST - FORM FEED/PATIENT: NO//

PICK LIST - FORM FEED/WARD: YES//

PICK LIST - LINES ON FORM FEED: NO//

PRINT NON-ACTIVE ORDERS FIRST:

BAXTER ATC DEVICE: ATC// 

USE OLD ATC INTERFACE:

Edit the Device with the following information:

Select DEVICE NAME:    ATC    BAXTER ATC-PHARM     TNA991:    

NAME: ATC//

LOCATION OF TERMINAL: BAXTER ATC-PHARM//

Select MNEMONIC:

LOCAL SYNONYM:

\$I: TNA991:// \|TCP\|9100 This \$I in use by other Devices. -\|TCP\|"Port Assignment"

VOLUME SET(CPU):

SIGN-ON/SYSTEM DEVICE:

TYPE: OTHER// NET  NETWORK CHANNEL

SUBTYPE: C-OTHER//

DEFAULT SUBTYPE: C-OTHER//

ASK DEVICE: NO//

ASK PARAMETERS: NO//

ASK HOST FILE: NO//

ASK HFS I/O OPERATION:

QUEUING:

OUT-OF-SERVICE DATE:

NEAREST PHONE:

KEY OPERATOR:

MARGIN WIDTH:

PAGE LENGTH:

SUPPRESS FORM FEED AT CLOSE: YES//

\*BLINK ON:

\*BLINK OFF:

SECURITY:

CLOSEST PRINTER:

FORM CURRENTLY MOUNTED:

\*PHYSICAL AREA: UNIT DOSE (ACI)//

OPEN PARAMETERS: ("10.18.6.168":9100:"+Q"::512:512) ----("IP Address":" Port Assignment": "+Q"::512:512)

CLOSE PARAMETERS:

USE PARAMETERS:

PRE-OPEN EXECUTE: ^

Verify Device File changes:

OUTPUT FROM WHAT FILE: DEVICE//    DEVICE  (1252 entries)

Select DEVICE NAME:    ATC    BAXTER ATC-PHARM     \|TCP\|9100    

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes//   (Yes)

Include COMPUTED fields:  (N/Y/R/B): NO//  - No record number (IEN), no Computed

Fields

NAME: ATC                               \$I: \|TCP\|9100

  ASK DEVICE: NO                        ASK PARAMETERS: NO

  LOCATION OF TERMINAL: BAXTER ATC-PHARM

  DEFAULT SUBTYPE: C-OTHER              ASK HOST FILE: NO

  SUPPRESS FORM FEED AT CLOSE: YES      OPEN COUNT: 225

  OPEN PARAMETERS: ("10.18.6.168":9100:"+Q"::512:512)

  \*PHYSICAL AREA: UNIT DOSE (ACI)

SUBTYPE: C-OTHER                      TYPE: NETWORK CHANNEL

  \# OF ATTEMPTS: 4

### Common Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally, a site experiences trouble getting the interface to run properly when the site first acquires an ATC, or has trouble later with the interface stopping in the middle of pick lists sends. If this happens, please try one or more of the following:

- Some sites have found that lowering the baud rate from 9600 to 4800, or even 2400, solves their problem.
- Sometimes, there is an error in the ATC HPS CONFIGURATION SETTINGS. If the user experiences trouble, please double-check these settings.
- In some cases, it is only a matter of changing the time of day that pick lists are sent to the ATC to avoid peak loads on the VistA computer system.
- In other cases, it has simply been a matter of adjusting the RESPONSE TIMER-CONTROL and/or RESPONSE TIMER-DATA settings within the HPS CONFIGURATION settings.
- If all else fails and the interface still does not want to work, the user may consider setting the USE OLD INTERFACE flag in the Ward Group file (#57.5) for all ward groups that will be sending pick lists to the ATC. (See the Ward Groups section in the *Inpatient Medications Supervisor's User Manual*.)

(*This page included for two-sided copying*.)

# Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unit Dose labels and MAR are designed to print at 16 or 16.5 pitch (6 lines per inch). The user might need to add entries in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

If the site plans to use the labels, an extra printer will be needed in the pharmacy, and at each nursing station that also plans to use the labels.

An extra terminal might also be needed at each nursing station planning to use this package.

An extra printer will be needed in the pharmacy to print IV labels.

## Disk Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since this version was distributed using KIDS, the transport global was automatically deleted after the initial install.

Depending on how the VA FileMan compiles the cross-references, there will be approximately 364 Inpatient Medications routines, taking up approximately 813K of disk space.

### Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each inpatient order uses approximately 600 bytes of disk space.

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only global used by the Inpatient Medications package that is recommended for journaling is the ^PS global.

## Translating Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In previous versions of Inpatient Medications, it was recommended that if the site was translating PS\*, that the PSG global be placed above the PS\* in the translation table, and that PSG be translated back to itself. This was suggested because the PSG global was subscripted by \$J and translating it would produce errors.

Version 5.0 no longer uses the PSG global, and entries in the translation table referring to it can be deleted.

## Nightly Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IV Medications and Unit Dose Medications modules each have a background job that is scheduled to run every night. These background jobs are needed to compile statistics and to perform general clean-up of no longer needed data. Both of these background jobs are options.

For IV Medications, the option is PSJI BACKGROUND JOB (*Compile IV Costs in Background*).

For Unit Dose Medications, the option is PSJU BRJ (*Unit Dose Clean-Up*).

## Queuing and Printing across CPUs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All reports and labels can be queued and can be printed across Central Processing Units (CPUs). When the labels are first created, they are automatically queued, unless the terminal or a slave printer is selected as the user's label device.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Packages Needed to Run Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package requires the minimum version, stated on the following external packages, to run effectively:

| <u>PACKAGE</u>                        | <u>MINIMUM VERSION NEEDED</u> |
|---------------------------------------|-------------------------------|
| Kernel                                | 8.0                           |
| VA FileMan                            | 22.0                          |
| MailMan                               | 8.0                           |
| PIMS                                  | 5.3                           |
| CPRS                                  | 1.0                           |
| Outpatient Pharmacy                   | 7.0                           |
| PDM                                   | 1.0                           |
| Dietetics                             | 5.0                           |
| Bar Code Medication Administration    | 3.0                           |
| HealtheVet Web Services Client (HWSC) | 1.0                           |
| VistALink                             | 1.5                           |

## Unit Dose Medications and Ward Stock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package also has a tie to the Automatic Replenishment/Ward Stock package so that if the site is running the Automatic Replenishment/Ward Stock package, the Inpatient Medications package will know which items in the Drug file (#50) are ward stock items for each ward. The tie is a cross-reference under the PHARMACY AOU STOCK file (#58.1).

## Unit Dose Medications and Drug Accountability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications package also has a tie to the Drug Accountability package so that if the site is running the Drug Accountability package, the Inpatient Medications package will know which items in the Drug file (#50) are ward stock items for each ward. This cross-reference is the link between the Controlled Substances package and the Unit Dose package for determining ward-stocked drugs.

## Calls Made by Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following external calls are supported via inter-package agreements:

| ROUTINE | ENTRY POINTS USED                                          |
|-------------|----------------------------------------------------------------|
| ECXUD1      | ^ECXUD1                                                        |
| ECXPIV1     | ^ECXPIV1                                                       |
| GMRVUTL     | EN6                                                            |
| GMRADPT     | EN1                                                            |
| GMRAOR      | \$\$ORCHK                                                      |
| GMRAOR2     | EN1                                                            |
| GMRAPEM0    | EN2                                                            |
| OR3CONV     | OTF                                                            |
| ORCONV3     | PSJQOS                                                         |
| ORERR       | EN                                                             |
| OROCAPI     | \$\$AOC, \$\$DOC, \$\$GOC                                      |
| ORUTL       | READ                                                           |
| ORX1        | NA                                                             |
| ORX2        | LK,ULK                                                         |
| PSAPSI5     | EN                                                             |
| PSBIPM      | EN, MOB, MOBR                                                  |
| PSSDSAPD    | \$\$DOSE, \$\$DRT                                              |
| PSSDSAPI    | \$\$BSA, \$\$DS, \$\$EXMT, \$\$FRQ, \$\$MRT, \$\$UNIT, \$\$SUP |
| PSSFDBRT    | GROUTE                                                         |
| PSSHLSCH    | EN                                                             |
| PSODDPR4    | BLD                                                            |
| PSODRDU2    | EN                                                             |
| SDROUT2     | DIS                                                            |
| SDAMA203    | SDIMO                                                          |
| VADPT       | IN5, INP, PID, SDA                                             |

## Introduction to Integration Agreements and Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following integration agreements and entry points are provided for the associated packages; only those packages listed can use these integration agreements and entry points. For complete information regarding the IAs, please refer to the Integration Agreement Menu. It can be found in FORUM under DBA MENU \> INTEGRATION CONTROL REGISTRATIONS.

<u>Inpatient Medications Custodial Integration Agreements</u>

206 NAME: DBIA206

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: SURGERY Birmingham

ROUTINE: PSIVACT

296 NAME: DBIA296

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

FILE: 50.8

ROOT: PS(50.8,

435 NAME: DBIA435

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 50.8

ROOT: PS(50.8,

438 NAME: DBIA438

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 57.6

ROOT: PS(57.6,

472 NAME: DBIA472

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 50.8

ROOT: PS(50.8,

475 NAME: DBIA475

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 57.6

ROOT: PS(57.6

486 NAME: PSJEEU0

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

ADVERSE REACTION TRACKING Chicago

CONTROLLED SUBSTANCES Birmingham

ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJEEU0

534 NAME: DBIA68-C

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

FILE: 53.1

ROOT: PS(53.1,

771 NAME: DBIA271-C

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: DRUG ACCOUNTABILITY Birmingham

FILE: 50.8

ROOT: PS(50.8,

772 NAME: DBIA271-D

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: DRUG ACCOUNTABILITY Birmingham

FILE: 57.6

ROOT: PS(57.6,

900 NAME: PSIVACT

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: SURGERY Birmingham

ROUTINE: PSIVACT

902 NAME: PSJSV0

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE:

ROUTINE: PSJSV0

1095 NAME: DBIA1095

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: CONTROLLED SUBSTANCES Birmingham

1884 NAME: DBIA1884

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: DSS EXTRACTS Birmingham

DRUG ACCOUNTABILITY Birmingham

FILE: 59.5

ROOT: PS(59.5

2100 NAME: DBIA2100

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

2108 NAME: DBIA2108

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

2109 NAME: DBIA2109

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 53.45

ROOT: PS(53.45,

2110 NAME: DBIA2110

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 59.6

ROOT: PS(59.6,

2111 NAME: DBIA2111

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 57.7

ROOT: PS(57.7,

2112 NAME: DBIA2112

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 57.5

ROOT: PS(57.5

2114 NAME: DBIA2114

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 51.15

ROOT: PS(51.15,

2115 NAME: DBIA2115

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 53.2

ROOT: PS(53.2,

2116 NAME: DBIA2116

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

2125 NAME: DBIA2125

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 53.45

ROOT: PS(53.45

2127 NAME: DBIA2127

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 50.3

ROOT: PS(50.3,

2132 NAME: DBIA2132

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 51.15

ROOT: PS(51.15,

2139 NAME: DBIA2139

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 57.1

ROOT: PS(57.1,

2140 NAME: DBIA2140

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

FILE: 53.1

ROOT: PS(53.1

2144 NAME: DBIA2144

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSGAL5

2145 NAME: DBIA2145

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSGAMSA

2146 NAME: DBIA2146

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSGCT

2150 NAME: DBIA2150

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSGNE3

2153 NAME: DBIA2153

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSGSETU

2154 NAME: DBIA2154

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSIVWL

2155 NAME: DBIA2155

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSIV

2156 NAME: DBIA2156

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSIVHLP1

2157 NAME: DBIA2157

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSIVXU

2350 NAME: DBIA2350

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

2376 NAME: DBIA2376

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJORUT2

2383 NAME: DBIA2383

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJORRE

2384 NAME: DBIA2384

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJORRE1

2401 NAME: OE/RR CONVERSION CALL TO PSJIPST3

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJIPST3

2402 NAME: INPATIENT MED CALLS FOR OE/RR

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORUT2

2403 NAME: OE/RR CALLS TO PSJORUTL

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORUTL

2404 NAME: OE/RR CALL TO PSJORMAR

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORMAR

2411 NAME: DBIA2411

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJUTL1

2417 NAME: Pharmacy Schedule and Admin Team Utilities

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJEEU

2499 NAME: DBIA2499

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 59.5

ROOT: PS(59.5

2612 NAME: DBIA2612

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: NATIONAL DRUG FILE Birmingham

FILE: 50.3

ROOT: PS(50.3,

2805 NAME: DBIA2805

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY BENEFITS MANAGEMENT Birmingham

FILE: 59.6

ROOT: PS(59.6,

2828 NAME: DBIA2828

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCMA

2829 NAME: DBIA2829

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCMA1

2830 NAME: DBIA2830

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCMA2

2907 NAME: TIU MEDICATION OBJECTS READ PHARMACY FILE

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: TEXT INTEGRATION UTILITIES Salt Lake City

FILE: 53.1

ROOT: PS(53.1,

2945 NAME: Use of calls in PSIVSP

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSIVSP

3143 NAME: DBIA3143

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

ROUTINE: PSJORAPI

3167 NAME: 3167

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORPOE

3243 NAME: Active Flag

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORREN

3320 NAME: UPDATE BCMA STATUS INFORMATION

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCMA3

3416 NAME: DBIA3416

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCMA4

3598 NAME: DBIA3598

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJOERI

3836 NAME: PSJPXRM1

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

ROUTINE: PSJPXRM1

3876 NAME: PSJBCBU

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: PSJBCBU

4074 NAME: OR Call to PSJORUT2

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJORUT2

4264 NAME: PDM ACCESS TO PSJXRFS

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSJXRFS

4265 NAME: PDM ACCESS TO PSJXRFK

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSJXRFK

4537 NAME: PSJ53P1

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE:

ROUTINE: PSJ53P1

4580 NAME: VALIDATE DOW SCHEDULES

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

ROUTINE: PSIVUTL

4819 NAME: PSJ59P5

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE:

ROUTINE: PSJ59P5

5001 NAME: Pointing to the PHARMACY QUICK ORDER (#57.1) File

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE:

USUAGE: Supported

5057 NAME: BCMA LAST ACTION

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

DRUG ACCOUNTABILITY

ROUTINE: PSJUTL2

5058 NAME: ALLERIES ARRAY

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJMUTL

5306 NAME: PSJBLDOC

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

ROUTINE: PSJBLDOC

5385 NAME: Dosing Checks for IVs

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

ROUTINE: PSJAPIDS

5653 NAME: RETURN CPRS ORDER CHECKS AND OVERRIDES TO BCMA

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: GETPROVL^PSGSICH1

5654 NAME: INPATIENT INTERVENTIONS TO BCMA

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

ROUTINE: INTRDIC^PSGSICH1

5764 NAME: PSODGAL1

CUSTODIAL PACKAGE: OUTPATIENT PHARMACY

SUBSCRIBING PACKAGE: INPATIENT MEDICATIONS

ROUTINE: PSODGAL1

Example: How to Print DBIA Information from FORUM

Select FORUM Primary Menu Option: DBA MENU

Select DBA MENU Option: INTEGRATION CONTROL REGISTRATION

Select INTEGRATION CONTROL REGISTRATIONS option:INQ Inquire to an Integration control Registration

Select INTEGRATION REFERENCES: DBIA296 296 INPATIENT MEDICATIONS DBIA296 PS(50.8,

DEVICE: *\[Select Print Device\]*

INTEGRATION REFERENCE INQUIRY \#296 OCT 1,1996 10:24 PAGE 1

------------------------------------------------------------------------------

296 NAME: DBIA296

CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 50.8 ROOT: PS(50.8,

DESCRIPTION: TYPE: File

Outpatient Pharmacy 6.0v will be printing a management report. In order

to complete the report, we need to read ^PS(50.8 (IV STATS FILE). We are

reporting the outpatient ward's number of dispensed units, average cost of

the dispensed units, and the total costs of the dispensed units.

To obtain this data, we need to read the 0 node in subfile 50.804, the

Average Drug Cost Per Unit field (#4) on the 0 node piece 5 in subfile

50.805, the Dispensed Units (Ward) field (#2) on the 0 node piece 2 in the

subfile 50.808, and the B cross-reference in subfile 50.808.

GLOBAL MAP DATA DICTIONARY \#50.8 -- IV STATS FILE STORED IN ^PS(50.8,

SITE: BIRMINGHAM ISC

--------------------------------------------------------------------------

^PS(50.8 D0,2,D1,1,0)=^50.804P^^ (#1) WARD ^PS(50.8,D0,2,D1,2,D2,0)=^^^^

(#4) AVERAGE DRUG COST PER UNIT \[5N\] ^PS(50.8,D0,2,D1,2,D2,3,D3,0)=^ (#2)

DISPENSED UNITS (WARD) \[2N\] ^

*\<This page left blank for two-sided copying\>*

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the Inpatient Medications package options have been designed to stand-alone.

*\<This page left blank for two-sided copying\>*

# Internal Calls and Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a description of the major Inpatient Medications routines and subroutines. These routines and subroutines are not callable from outside of the package.

| ^PSGAL5        | Places entries into the orders' activity logs. Called when any action is taken upon a verified order, either through the package or through the VA FileMan.                                                                                                                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENDEV^PSGTI    | Used by most of the cost reports to select a print device.                                                                                                                                                                                                                                                                                                                                                           |
| ENDTS^PSGAMS   | Used by most of the cost reports to select a range of dates over which the report is to run.                                                                                                                                                                                                                                                                                                                         |
| ^PSGCT         | Adds or subtracts minutes from a date.                                                                                                                                                                                                                                                                                                                                                                               |
| ^PSGFILED      | Used at various entry points to edit the files used by the Inpatient Medications package.                                                                                                                                                                                                                                                                                                                            |
| ENDPT^PSGP     | All individual patients are selected here. Will not allow the selection of patients who have never been admitted. Will allow the selection of patients, not currently admitted, only to print a profile or to enter returned meds. Also, checks to see if the patient selected has been transferred, discharged, etc.                                                                                                |
| ^PSGNE3        | Calculates default values for an order's start and stop dates during the order entry process. Sometimes called at ENFD entry point to calculate a new stop date.                                                                                                                                                                                                                                                     |
| ^PSGO          | Prints the Unit Dose Medications orders for a patient.                                                                                                                                                                                                                                                                                                                                                               |
| EN^PSGOE1      | Allows the user to take various actions on an order (edit, cancel, etc.). First determines the actions that are allowed for the order, depending on the status of the order (active, non-verified, etc.) and the type of user (pharmacist, nurse, or ward clerk).                                                                                                                                                    |
| ENUNM^PSGOU    | Goes through a patient's orders, updating the status of the orders that have expired.                                                                                                                                                                                                                                                                                                                                |
| ^PSGPLG        | Used to select pick lists that have already been run, for reprinting, updating, etc.                                                                                                                                                                                                                                                                                                                                 |
| ^PSGPL0        | Calculates the number of units needed of a medication over a given date range.                                                                                                                                                                                                                                                                                                                                       |
| ^PSGSEL        | Handles the "WARD GROUP (G), WARD (W), OR PATIENT (P)" prompt and the associated help text.                                                                                                                                                                                                                                                                                                                          |
| ^PSGSET        | Sets the variables necessary to run the Unit Dose Medications module. Also sets the variables into the ^XUTL("OR","PSG") global for use by the various Unit Dose options, to allow the option to be independent.                                                                                                                                                                                                     |
| ENCV^PSGSETU   | Used by the Unit Dose Medications options to set the package variables. If the ^XUTL("OR","PSG") global is found, this global is used to set the variables. If it is not found, the routine ^PSGSET is called.                                                                                                                                                                                                       |
| ENIVKV^PSGSETU | These are used by the IV Medications and Unit Dose Medications                                                                                                                                                                                                                                                                                                                                                       |
| ENKV^PSGSETU   | Module, (respectively), to kill the package-wide variables when exiting options.                                                                                                                                                                                                                                                                                                                                     |
| ^PSGTI         | The Unit Dose interface to TaskMan, using the ^%ZTLOAD routine.                                                                                                                                                                                                                                                                                                                                                      |
| EN2^PSGVW      | Prints the expanded view of an order. It calls the ^PSGVW0 routine to print the activity log, if the order has one.                                                                                                                                                                                                                                                                                                  |
| ^PSIV          | Used for patient selection, editing of administration schedules, and selection of IV orders from the IV profile.                                                                                                                                                                                                                                                                                                     |
| ^PSIVACT       | Called each time an IV order is addressed to update the order's status and ward location.                                                                                                                                                                                                                                                                                                                            |
| ^PSIVCAL       | Calculates the default Start and Stop times for an order during IV order entry.                                                                                                                                                                                                                                                                                                                                      |
| ^PSIVCHK       | Called after an IV order has been entered or edited to ensure the order is in the correct format for that IV type.                                                                                                                                                                                                                                                                                                   |
| ^PSIVHLP\*     | These routines contain help text to be displayed to the user during interactive sessions. When a PSIVHLP\* routine is invoked, the variable "HELP" is set to the name of a line label which begins the appropriate help text.                                                                                                                                                                                        |
| ^PSIVLABL      | Prints IV labels (except hyperals) to the IV label device.                                                                                                                                                                                                                                                                                                                                                           |
| ^PSIVHYPL      | Prints IV hyperal labels to the IV label device.                                                                                                                                                                                                                                                                                                                                                                     |
| ^PSIVOPT       | Called each time an order entry option is invoked. When an order is chosen from the profile, this routine prompts the user on actions available on the order. When an action is chosen, the order is checked to be sure the action is allowed and to make sure another user is not currently editing the order. The orders activity log is also updated by this routine after an action has been taken on the order. |
| ^PSIVSTAT      | Creates "transaction nodes" in the IV STATS file (#50.8) each time an IV label is printed, or a "return/destroyed" item is entered. This routine is also called (at different entry points) by the PSJI BACKGROUND JOB (*Compile IV Costs in Background*) and PSJI COMPILE STATS (*COmpile IV Statistics (IV*)) options to compile these transactions into the file.                                                 |
| ^PSIVVW        | Displays an IV order to the screen when one is selected for "viewing" through the order entry or patient profile options.                                                                                                                                                                                                                                                                                            |
| ^PSIVXU        | When the IV Medications module is entered, this routine calls the ^PSIVSET routine, which prompts the user for the IV site parameters to be used during that session. ^PSIVXU routine stores these variables in the ^XUTL global, so they can be reused during that session without prompting the user each time they are needed.                                                                                    |
| ^PSJAC         | Checks to see if the patient has been transferred, discharged, re-admitted, or has died and takes the appropriate action, depending on the site parameters.                                                                                                                                                                                                                                                          |
| ^PSJO          | Prints Inpatient (IV and Unit Dose) Medications orders for a patient.                                                                                                                                                                                                                                                                                                                                                |

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the more important namespace variables used by the Inpatient Medications package. These variables are listed here for support purposes only and can change from version to version.

### Inpatient Sign-on Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Inpatient Medications system variables are set whenever a user enters any of the Inpatient Medications options. These variables are needed to use many of the options. The variables are killed when the user exits each option.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PSJSYSU</strong></th>
<th><p>Used by the Inpatient Medications package in defining the characteristics of the user – what the user can or cannot do with regards to the package.</p>
<blockquote>
<p>1st piece = <strong>3</strong> if the user is seen as a pharmacist,</p>
<p><strong>1</strong> if the user is seen as a nurse, otherwise, <strong>0</strong> or NULL</p>
<p>2nd piece = <strong>1</strong> if the user is seen as a valid provider, able to write medication orders, otherwise, NULL</p>
<p>3rd piece = <strong>3</strong> if the user is seen as a pharmacist,</p>
<p><strong>2</strong> if the user is a pharmacy technician,</p>
<p><strong>1</strong> if the user is a nurse,</p>
<p><strong>0</strong> (or NULL), in which case the user is ward staff</p>
<p>4th piece = <strong>1</strong> if the user can select from dispense drugs when prompted for a drug during Inpatient/Unit Dose order entry, otherwise,</p>
<p><strong>0</strong> in which case the user must select an Orderable Item during order entry</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PSJSYSP</strong></td>
<td>IEN of the user's entry in the INPATIENT User Parameters file (#53.45), defined using the user logged on to the system.</td>
</tr>
<tr class="even">
<td><strong>PSJSYSP0</strong></td>
<td>The user's record (zero node) from the INPATIENT User Parameters file (#53.45). This is another set of user characteristics that define what the user can and cannot do with regard to the Inpatient Medications package. The user, through the <em>Edit Inpatient User Parameters</em> [PSJ UEUP] option, can set some of these parameters. Other parameters can only be set by the Inpatient Supervisor. A list of these characteristics can be obtained by printing the data dictionary for the INPATIENT User Parameters file (#53.45).</td>
</tr>
<tr class="odd">
<td><strong>PSJSYSL</strong></td>
<td><p>Defines how the package should act in regards to Unit Dose labels when the user takes actions on Unit Dose orders.</p>
<blockquote>
<p>1<sup>st</sup> piece = <strong>0</strong> if labels are not to be created</p>
<p><strong>1</strong> if the first label is to be created when the order is entered or completed, but not on verification</p>
<p><strong>2</strong> if the label is to be created when the order is entered and when the order is verified</p>
<p><strong>3</strong> if the first label is not to be created until the order is verified</p>
<p>If the setting for the first piece is 1 or 2, labels will be created when a non-verified Unit Dose order is edited. If the setting of the 1<sup>st</sup> piece is greater than 0, a label will be created on all actions taken on the order after it is verified. If the setting for the 1<sup>st</sup> piece is 0, the 2<sup>nd</sup> and 3<sup>rd</sup> pieces will be NULL.</p>
<p>2<sup>nd</sup> piece = device name (<strong>ION</strong>) to which labels are to be printed - can be NULL, in which case labels will be created but not printed</p>
<p>3<sup>rd</sup> piece = device (<strong>IO</strong>) to which labels are to be printed - will be NULL if 2<sup>nd</sup> piece is NULL</p>
</blockquote>
<p>PSJSYSL is defined when the user first enters an option, but is redefined each time a patient is selected to reflect the settings in the INPATIENT Ward Parameters file (#59.6) for the ward on which the patient currently resides.</p></td>
</tr>
<tr class="even">
<td><strong>PSGDT</strong></td>
<td><p>This is the current date and time in VA FileMan internal format. This is reset as needed by the package.</p>
<blockquote>
<p>^TMP("PSJUSER",$J,"PSG",0)</p>
<p>^TMP("PSJUSER",$J,"PSG",1)</p>
</blockquote>
<p>Used to store the above variables, except for PSGDT. These global variables are not killed until the user completely exits VistA. If these variables are found, they are used to set PSJSYSU, PSJSYSP, and PSJSYSP0. If the ^TMP variables are not found, PSJSYSU, PSJSYSP, and PSJSYSP0 are calculated and the ^TMP variables are set accordingly.</p>
<blockquote>
<p>^TMP("PSJUSER",$J,"PSG",0)=PSJSYSU_"^"_PSJSYSP</p>
<p>^TMP("PSJUSER",$J,"PSG",1)=PSJSYSP0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PSJRNF</strong></td>
<td>Is defined when the user first enters an option if the user holds the PSJ RNFINISH key.</td>
</tr>
<tr class="even">
<td><strong>PSJIRNF</strong></td>
<td>Is defined when the user first enters an option if the user holds the PSJI RNFINISH key.</td>
</tr>
<tr class="odd">
<td><strong>PSJITECH</strong></td>
<td>Is defined when the user first enters an option if the user holds the PSJI PHARM TECH key.</td>
</tr>
</tbody>
</table>

### Standard Variables Used Throughout the Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following variables are set whenever a patient is selected.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PSJSYSW</strong></th>
<th>IEN of an entry in the INPATIENT WARD PARAMETERS file (#59.6), defined by the ward on which the selected patient is found to reside, or by the ward on which the patient was last found to reside if the patient is not currently admitted to the medical center.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PSJSYSW0</strong></td>
<td>The record (zero node) from the INPATIENT Ward Parameters file (#59.6), as determined by the PSJSYSW variable. This is another set of characteristics that define what the user can and cannot do with regards to the Inpatient Medications package, determined by the ward on which the selected patient is found to reside, or last found to reside. These parameters are set by an Inpatient Supervisor or ADPAC. A list of these characteristics can be obtained by printing the DD for the INPATIENT Ward Parameters file (#59.6).</td>
</tr>
<tr class="even">
<td><strong>PSJSYSL</strong></td>
<td><p>Defines how the package should act in regards to Unit Dose labels when the user takes actions on Unit Dose orders.</p>
<blockquote>
<p>1<sup>st</sup> piece = <strong>0</strong> if labels are not to be created</p>
<p><strong>1</strong> if the first label is to be created when the order is entered or completed, but not on verification</p>
<p><strong>2</strong> if the label is to be created when the order is entered and when the order is verified</p>
<p><strong>3</strong> if the first label is not to be created until the order is verified</p>
<p>If the setting for the first piece is 1 or 2, labels will be created when a non-verified Unit Dose order is edited. If the setting of the 1<sup>st</sup> piece is greater than 0, a label will be created on all actions taken on the order after it is verified. If the setting for the 1<sup>st</sup> piece is 0, the 2<sup>nd</sup> and 3<sup>rd</sup> pieces will be NULL.</p>
<p>2<sup>nd</sup> piece = device name (<strong>ION)</strong> to which labels are to be printed - can be NULL, in which case labels will be created but not printed</p>
<p>3<sup>rd</sup> piece = device (<strong>IO</strong>) to which labels are to be printed - will be NULL if 2<sup>nd</sup> piece is NULL</p>
</blockquote>
<p>PSJSYSL is defined when the user first enters an option, but is redefined each time a patient is selected to reflect the settings in the INPATIENT Ward Parameters file (#59.6) for the ward on which the patient currently resides.</p></td>
</tr>
<tr class="odd">
<td><strong>PSGP</strong></td>
<td>The IEN of the selected patient - the pointer to the Patient file (#2).</td>
</tr>
<tr class="even">
<td><strong>PSGP(0)</strong></td>
<td>The zero node of the entry in the Patient file (#2) of the selected patient.</td>
</tr>
<tr class="odd">
<td><strong>PSJPAD</strong></td>
<td>The date of the selected patient's current or last admission, in the form of <em>internal^external.</em></td>
</tr>
<tr class="even">
<td><strong>PSJPBID</strong></td>
<td>The short form of the selected patient's identifier, as provided by the PIMS package.</td>
</tr>
<tr class="odd">
<td><strong>PSJPDD</strong></td>
<td>The date of the selected patient's last discharge, in the form of <em>internal^external.</em> Will be NULL if the patient is currently admitted.</td>
</tr>
<tr class="even">
<td><strong>PSJPDOB</strong></td>
<td>The date of the selected patient's birth, in the form of <em>internal^external</em>.</td>
</tr>
<tr class="odd">
<td><strong>PSJPDX</strong></td>
<td>The short diagnosis of the selected patient's current or last admission.</td>
</tr>
<tr class="even">
<td><strong>PSJPHT</strong></td>
<td>The selected patient's height, in centimeters.</td>
</tr>
<tr class="odd">
<td><strong>PSJPRB</strong></td>
<td>The selected patient's current or last room-bed.</td>
</tr>
<tr class="even">
<td><strong>PSJPSEX</strong></td>
<td>The selected patient's sex, in the form of <em>internal^external</em>.</td>
</tr>
<tr class="odd">
<td><strong>PSJPSSN</strong></td>
<td>The selected patient's social security number.</td>
</tr>
<tr class="even">
<td><strong>PSJPPID</strong></td>
<td>The selected patient's identifier, as provided by the PIMS package.</td>
</tr>
<tr class="odd">
<td><strong>PSJPTD</strong></td>
<td>The date of the last transfer of the current or last admission for the selected patient, in the form of <em>internal^external</em>.</td>
</tr>
<tr class="even">
<td><strong>PSJPTS</strong></td>
<td>The selected patient's current or last treating specialty.</td>
</tr>
<tr class="odd">
<td><strong>PSJPTSP</strong></td>
<td>The selected patient's current or last treating specialty provider.</td>
</tr>
<tr class="even">
<td><strong>PSJPWD</strong></td>
<td>The selected patient's current or last ward. This is a pointer to the WARD LOCATION file (#42).</td>
</tr>
<tr class="odd">
<td><strong>PSJPWDN</strong></td>
<td>The name of the selected patient's current or last ward.</td>
</tr>
<tr class="even">
<td><strong>PSJPWT</strong></td>
<td>The selected patient's weight, in kilograms.</td>
</tr>
</tbody>
</table>

### IV Sign-on Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These variables are set whenever a user selects the IV or Inpatient Medications option.

| PSIVPL   | The default label device set either from the IV room site parameters, or through the *Change Report/Label Devices(IV)* \[PSJI DEVICE\] option.                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSIVPR   | The default report device set either from the IV room site parameters, or through the *Change Report/Label Devices (IV)* \[PSJI DEVICE\] option.                                   |
| PSIVSITE | Contains the site parameters for the IV room chosen upon entry to the package. It is the one node concatenated with the five node of the entry chosen in the IV ROOM file (#59.5). |
| PSIVSN   | The pointer value to the IV ROOM file (#59.5) of entry chosen upon entry to the IV Medications module.                                                                             |

### Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| PSGORD  | Contains the IEN of the order currently being worked on, concatenated with a set of codes that "tell" the package where to look for the order. If PSGORD contains a V, the order is an IV, and the package will look for the order at ^PS(55,PSGP, "IV",+PSGORD,. Similarly if PSGORD contains a P or a N, the package will look for the order at ^PS(53.1,+PSGORD,. If PSGORD contains a U, the package will look for the order at ^PS(55,PSGP,5,+PSGORD,. |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSGSS   | Returned by the routine PSGSEL in response to the "WARD GROUP (G), WARD (W), OR PATIENT (P)" prompt. Its value will be G, W, P, ^, or NULL.                                                                                                                                                                                                                                                                                                                 |
| ON      | The IEN of the IV order in the PHARMACY PATIENT file (#55).                                                                                                                                                                                                                                                                                                                                                                                                                 |
| HELP    | When one of the IV help routines is invoked (PSIVHLP\*), this variable is set to the line label identifying the help text to be displayed.                                                                                                                                                                                                                                                                                                                                  |
| P(n)    | Where *n* is a number from 1 to 23. This local array is set to each piece of data stored on the zero node for an IV order (^PS(55,PSGP,"IV",ON,0)), so that a disk access is not necessary each time this information is needed.                                                                                                                                                                                                                                            |
| PSIVNOL | The number of IV labels being printed, returned, destroyed, recycled, or canceled.                                                                                                                                                                                                                                                                                                                                                                                          |

Other namespace variables usually follow certain conventions. For example, most namespace variables are namespace by routine (e.g., PSGPL for pick list variables, PSGAL for activity log variables). Most variables ending in "WD" contain the IEN of a ward in the WARD LOCATION file (#42), while those ending in "WDN" usually contain the name of the ward. Variables ending in "WG" will usually contain the IEN of a ward group from the WARD GROUP file (#57.5), while those ending in "WGN" will usually contain the name of the ward group. Variables ending in "SD" will usually be the start date for a range of dates over which a report or process is run. Those ending in "FD" will usually be the stop date for the same range of dates.

(*This page included for two-sided copying*.)

# On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the entire Inpatient Medications package, the user will always be able to enter a question mark (?) to obtain on-line information to assist in the choice of actions at any prompt.

## Printing Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DDs are considered part of the on-line documentation for this software application. The user can, and should, print the DDs as soon as the software has been installed and initialized. The following are the files for which the user should print DDs:

> 50.2 IV CATEGORY

> 50.8 IV STATS

> 51.15 ADMINISTRATION SHIFT

> 53.1 NON-VERIFIED ORDERS

> 53.2 UNIT DOSE ORDER SET

> 53.3 ACTIVITY LOG REASON

> 53.4 PRE-EXCHANGE NEEDS

> 53.41 MAR LABELS

> 53.42 INPATIENT BACKGROUND JOB

> 53.43 MISCELLANEOUS REPORT FILE

> 53.44 PHYSICIANS' ORDERS

> 53.45 INPATIENT USER PARAMETERS

> 53.46 CLINIC DEFINITION

> 53.5 PICK LIST

> 53.55 UNIT DOSE/ATC MEDS

> 57.5 WARD GROUP

> 57.6 UNIT DOSE PICK LIST STATS

> 57.7 MEDICATION ADMINISTERING TEAM

> 57.8 CLINIC GROUP

> 59.5 IV ROOM

> 59.6 INPATIENT WARD PARAMETERS

Use VA FileMan \[DATA DICTIONARY UTILITIES\] option to print the DDs.

Example: How to Print DDs Using VA FileMan

VA FileMan 22.0

Select OPTION: 8 DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH WHAT FILE: INPATIENT USER PARAMETERS// \<Enter\>

GO TO WHAT FILE: INPATIENT USER PARAMETERS // \<Enter\>

Select SUB-FILE: \<Enter\>

Select LISTING FORMAT: STANDARD// BRIEF

ALPHABETICALLY BY LABEL? NO// Y (YES)

DEVICE: *\[Enter Print Device Here\]* RIGHT MARGIN: 80// \<Enter\>

The DD will now print on the user-specified device*.*

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unit Dose Medications module has been granted a permanent Standards and Conventions (SAC) exemption to use asterisk (\*) reads in its interface with the ATC Unit Dose dispensing machine.

The IV Medications module has been granted a permanent SAC exemption from VA FileMan compatibility for the WARD LIST cross-reference, MANUFACTURING LIST cross-reference and the SUSPENSE LIST.

## IV Ward List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all of the IV orders needed for the date and IV types specified. The Ward List must be run before scheduled labels can be printed for IV orders. The labels are printed in the order of the ward list, and only counted as usage the first time they are printed.

The data for the ward list is stored in a non-VA FileMan compatible cross-reference in the Pharmacy Patient file (#55). Because of this, ward lists should not be manipulated using VA FileMan. The basic structure of this cross-reference is as follows:

^PS(55,"PSIVWL",S1,S2,S3,S4,S5)=P1^P2^P3^P4

^PS(55,"PSIVWL",S1,S2,S3,S4,S5,BCMA ID)= ""

where:

> S1 = The IEN of the IV Room for which the order is associated.

> S2 = The name of the ward where the patient is located.

> S3 = The first letter of the IV type, concatenated with the start date/time of the coverage period this entry is associated with. For example, if the ward list was run on 2/22/91 for admixtures which had a period of coverage from 0859 to 0858, S3 would look like "A2910222.0859."

> S4 = The IEN of the patient for whom the order exists.

> S5 = The IEN of the order.

> BCMA ID = Unique Bar Code ID printed for the order.

> P1 = The number of labels needed for this period of coverage.

> P2 = The start date concatenated with the administration times for the order.

> P3 = The cumulative number of labels that have been printed for the order.

> P4 = When scheduled labels have been run, this piece is set to "1." This is used to prevent labels from being counted again in the IV Stats file (#50.8) if scheduled labels are printed more than once.

## IV Manufacturing List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IV Manufacturing List produces a report by additive or solution of all orders due to be mixed for the specified date and IV types. The total number of admixtures, piggybacks, hyperals, chemotherapies, and syringes containing each additive is shown, as well as how many belong to each patient. As the manufacturing list is compiled from the ward list cross-reference, the manufacturing list must be run after the ward list.

The data for the manufacturing list is stored in a non-VA FileMan compatible cross-reference in the Pharmacy Patient file (#55). Because of this, manufacturing lists should not be manipulated using VA FileMan. The basic structure of this cross-reference is as follows:

The top node for each drug listed on the manufacturing list:

^PS(55,"PSIVWLM",S1,S2,S3,S4,0)=P1

where:

> S1 = The IEN of the IV Room for which this order is associated.

> S2 = The first letter of the IV type, concatenated with the start date/time of the coverage period for which this entry is associated. For example, if the manufacturing list was run on 2/22/91 for admixtures which had a period of coverage from 0859 to 0858, S2 would look like "A2910222.0859."

> S3 = The first letter of the IV type.

> S4 = If the order includes an additive, the first piece of S4 contains the first 10 characters of the additive print name, the second piece contains the additive strength, and the third piece contains "6" concatenated with the IEN of the additive in the IV Additives file (#52.6). If the order does not include an additive, piece one contains the first 10 characters of the solution print name, piece two contains the solution volume, and piece three contains "7" concatenated with the solution's IEN in the IV Solutions file (#52.7).

> P1 = The total number of each type order containing the drug identified in S4.

Each record on the manufacturing list should be in the following format:

> ^PS(55,"PSIVWLM",S1,S2,S3,S4,S5,S6,S7,S8)=P1^P2

where:

> S1 = The IEN of the IV Room for which this order is associated.

> S2 = The first letter of the IV type, concatenated with the start date/time of the coverage period for which this entry is associated. For example, if the manufacturing list was run on 2/22/91 for admixtures which had a period of coverage from 0859 to 0858, S2 would look like "A2910222.0859."

> S3 = The first letter of the IV type.

> S4 = If the order includes an additive, the first piece of S4 contains the first 10 characters of the additive print name, the second piece contains the additive strength, and the third piece contains "6"; concatenated with the internal number of the additive in the IV Additives file (#52.6). If the order does not include an additive, piece one contains the first 10 characters of the solution print name, piece two contains the solution volume, and piece three contains "7"; concatenated with the solution's internal number in the IV Solutions file (#52.7).

> S5 = If the order contains an additive, piece one contains the first 10 characters of the first solution's print name, piece two contains the solution's volume, and piece three contains "7"; concatenated with the solution's IEN in the IV Solutions file (#52.7). If no additive was found for the order, S4 contains "zz6" only.

> S6 = The IEN of the patient for whom the order exists.

> S7 = The IEN of the order.

> P1 = The number of labels needed for this order and period of coverage.

> P2 = The name of the ward where the patient is located at the time the list is run.

## IV Suspense List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When labels for an order are suspended, an entry is made in the "PSIVSUS" cross-reference of the Pharmacy Patient file (#55). Because this cross-reference is non-VA FileMan compatible, suspense data should not be manipulated using VA FileMan. The basic structure of this cross-reference is as follows:

^PS(55,"PSIVSUS",S1,S2,S3,S4)=P1^P2^P3

where:

> S1 = The IEN of the IV Room associated with this order.

> S2 = The IEN of the patient for whom the order exists.

> S3 = The IEN of the order.

> S4 = The date and time the order was suspended.

> P1 = The number of labels suspended for the order.

> P2 = The start date concatenated with the administration times for the order.

> P3 = The cumulative number of labels that have been printed for the order (does not include those labels suspended and not printed).

When the *Labels from Suspense(IV)* \[PSJI SUSLBLS\] option is used, the routine first deletes any orders that labels have been printed for and are more than 1 day old. The new labels are then printed, a new entry is added to the cross-reference and set to the same values as the old entry, and the old entry is then deleted. This new node shows that labels for this suspended order have already been printed, and is used by the *Reprint Label from Suspense (IV)* \[PSJI SUSREP\] option when reprinting batches of labels. The structure of the new node is as follows:

^PS(55,"PSIVSUS",S1,S2,S3,S4,S5)=P1^P2^P3

^PS(55,"PSIVSUS",S1,S2,S3,S4,S5,BCMA ID)= ""

where:

> S1 = The IEN of the IV Room associated with this order.

> S2 = "A" concatenated with the date and time labels for the order were printed.

> S3 = The IEN of the patient for whom the order exists.

> S4 = The IEN of the order.

> S5 = The date and time the order was suspended.

> BCMA ID = Unique Bar Code ID printed for the order.

> P1 = The number of labels suspended for the order.

> P2 = The start date concatenated with the administration times for the order.

> P3 = The cumulative number of labels that have been printed for the order (does not include those labels suspended and not printed).

The *Manufacturing Record for Suspense (IV)* \[PSJI SUSMAN\] option creates a temporary cross-reference in the Pharmacy Patient file (#55) to hold the data needed for this report. This is done so that the same routines, which build and print the Manufacturing List described above, can be used for this report also. It only exists during the running of this option. The structure of the cross-reference is as follows:

^PS(55,"PSIVSUSM",S1,S2,S3,S4,0)=P1

where:

> S1 = The IEN of the IV Room associated with this order.

> S2 = The job number (\$J).

> S3 = The first letter of the IV type.

> S4 = If the order includes an additive, the first piece of S4 contains the first 10 characters of the additive print name, the second piece contains the additive strength, and the third piece contains "6"; concatenated with the internal number of the additive in the IV Additives file (#52.6). If the order does not include an additive, piece one contains the first 10 characters of the solution print name, piece two contains the solution volume, and piece three contains "7"; concatenated with the solution's IEN in the IV Solutions file (#52.7).

> P1 = The total number of each type order containing the drug identified in S4.

Each record on the Suspense Manufacturing List should be in the following format:

^PS(55,"PSIVWLM",S1,S2,S3,S4,S5,S6,S7)=P1

where:

> S1 = The IEN of the IV Room associated with this order.

> S2 = The job number (\$J).

> S3 = The first letter of the IV type.

> S4 = If the order includes an additive, the first piece of S4 contains the first 10 characters of the additive print name, the second piece contains the additive strength, and the third piece contains "6"; concatenated with the IEN of the additive in the IV Additives file (#52.6). If the order does not include an additive, piece one contains the first 10 characters of the solution print name, piece two contains the solution volume, and piece three contains "7"; concatenated with the solution's IEN in the IV Solutions file (#52.7).

> S5 = If the order contains an additive, piece one contains the first 10 characters of the first solution's print name, piece two contains the solution's volume, and piece three contains "7"; concatenated with the solution's IEN in the IV Solutions file (#52.7). If no additive was found for the order, S4 contains "zz6" only.

> S6 = The IEN of the patient for whom the order exists.

> S7 = The IEN of the order.

> P1 = The number of labels suspended for this order.

## Unit Dose "Defaults"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Order Start Date/Time Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an order is created, the software will calculate a Start Date/Time for the order. If the order is entered through a Unit Dose Order Set, the Calculated Start Date/Time is automatically entered into the order and may be edited later. If the regular, abbreviated, or ward order entry process is used, the Calculated Start Date/Time is shown as a default value during the order entry process and may be edited immediately.

If the order is an Inpatient Medication for Outpatients order, the default Start Date/Time will be the clinic Appointment Date/Time.

If the order originated in CPRS and a duration is received with the order, the default Start Date/Time will be the <u>expected first dose</u> that was displayed in CPRS at the time the order was created. The DEFAULT START DATE CALCULATION parameter is used to calculate the Calc Start Date/Time value displayed when the order is finished.

If the order originated in CPRS and no duration is received with the order, The DEFAULT START DATE CALCULATION parameter is used to calculate the Start Date/Time value. The <u>expected first dose</u> that was displayed in CPRS at the time the order was created is displayed as the Requested Start Date/Time.

This DEFAULT START DATE CALCULATION parameter is set using the *Inpatient Ward Parameters Edit* \[PSJ IWP EDIT\] option under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option under the *Supervisor's Menu* \[PSJU FILE\]*.* The choices for the DEFAULT START DATE CALCULATION are as follows:

1.  NOW - If this choice is selected, the Start Date/Time will equal the Login Date/Time of the order.
2.  CLOSEST ADMIN TIME - If this choice is selected, the Admin Date/Time that is closest to the Login Date/Time of the order will be used as the default.
3.  NEXT CLOSEST ADMIN TIME - If this choice is made, the closest Admin Date/Time after the Login Date/Time of the order, will be used as the default.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/091.png)Note: When an order is placed through CPRS prior to the next administration time of the schedule for the order, the <u>Expected First Dose</u> will be today at the next administration time. However, if the order is placed after the <u>last</u> administration time of the schedule for the order, the Expected First Dose will be the <u>next</u> administration time. This Expected First Dose <u>date/time</u> is seen through CPRS and is always based on the logic of using "next administration time, " regardless of what the site has set for the ward parameter. The Expected First Dose displayed in CPRS displays as Requested Start Date/Time on the order view if no duration is received from CPRS. The Expected First Dose displays as the default Start Date/Time on the order view when a duration is received.

### Stop Date/Time: Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an order is created, the package will calculate a Stop Date/Time for the order. If the order is entered through the abbreviated or ward order entry process, or through an Order Set, the Calculated Stop Date/Time is automatically entered into the order, and can be edited later. If the regular order entry process is used, the Calculated Stop Date/Time is shown as a default value during the order entry process, and can be edited immediately.

When calculating the default Stop Date/Time, the software uses the following criteria (<u>in the</u> <u>order shown</u>):

1.  If the order was created in CPRS and a duration is received with the order, the order's default Stop Date/Time is calculated using the default Start Date/Time plus the duration. The system also calculates the default Stop Date/Time that would have been used if no duration had been received, and this date is displayed as the Calc Stop Date/Time.
4.  If the patient has a default Stop Date/Time associated with him/her, and this date/time is not less than the current date/time, the order's default Stop Date/Time will be set to the patient's default Stop Date/Time.
5.  If the order is a renewal and the Start Date/Time of the order is within three days of the patient's current default Stop Date/Time, the order's default Stop Date/Time will be set to NULL.
6.  If the order has a Schedule Type of One-Time, the ward parameter, DAYS UNTIL STOP FOR ONE-TIME, is accessed to determine the stop date. When the ward parameter is not available, the system parameter, DAYS UNTIL STOP FOR ONE-TIME, will be used to determine the stop date. When neither parameter has been set, one-time orders will use the ward parameter, DAYS UNTIL STOP DATE/TIME, to determine the stop date instead of the start and stop date being equal.
7.  If the Orderable Item of the order contains a day or dose limit and the Start Date/Time of the order plus the day or dose limit is less than the order's current default Stop Date/Time, the order's default Stop Date/Time will equal the order Start Date/Time plus the day or dose limit.
8.  If the default Stop Date/Time has not been determined by the previous methods and the order is for an Inpatient or is for a clinic that has no specific stop times defined, the order's default Stop Date/Time will be calculated using the DAYS UNTIL STOP DATE/TIME and TIME OF DAY THAT ORDERS STOP parameters. These parameters may be edited under the *Inpatient Ward Parameters Edit* \[PSJ IWP EDIT\] option under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option under the *Supervisor's Menu* \[PSJU FILE\] option. If a number is found for the DAYS UNTIL STOP DATE/TIME, the Stop Date of the order will be set to the Start Date of the order plus this number. If no number is found, the Stop Date of the order will be set to the Start Date of the order plus fourteen days. The default Stop Time will be set to the military time found in the TIME OF DAY THAT ORDERS STOP parameter. If no time is found in this parameter, the Stop Time will be set to the order's Start Time.
9.  If the default Stop Date/Time has not been determined by the previous methods and the order is for an Outpatient, the stop date will be calculated using the information in the CLINIC DEFINITION file (#53.46). If no default is entered in the file, the stop date will be 14 days.

    ![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/092.png)Note: <span id="Complex_Order_note" class="anchor"></span>The following rules resolve the issue of overlapping administration schedules for a complex order:

    START DATE of a component should match the STOP DATE of a previous component. Also, the START DATE of a component does not need to align with an admin time of the new component's schedule.

    TIME on the STOP DATE should always end up being an admin time.

### Patient's Default Stop Date/Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software shows a default Stop Date/Time for the order when creating and renewing orders. The default depends largely on the patient's default Stop Date/Time (sometimes referred to as the patient's "wall").

A wall will exist for a patient if the SAME STOP DATE ON ALL ORDERS parameter is set to YES. This parameter may be edited with the *Inpatient Ward Parameters Edit* \[PSJ IWP EDIT\] option under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option under the *Supervisor's Menu* \[PSJU FILE\] option*.*

The wall for the patient is calculated based on the DAYS UNTIL STOP DATE/TIME and the TIME OF DAY THAT ORDERS STOP parameters. These parameters may be updated under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option under the *Supervisor's Menu* \[PSJU FILE\] option. If a number is found for the DAYS UNTIL STOP DATE/TIME, the date of the wall will be set to the Start Date of the order being created plus this number. If no number is found, the date of the wall will be set to the Start Date of the order plus fourteen days. If a time is found in the TIME OF DAY THAT ORDERS STOP parameter, the time of the wall will be set to that time. If no time is found, the time for the wall will be set to the order's Start Time.

The following tells when the wall is updated:

1.  If the patient has no active orders, the wall is set to NULL.
10. If the order is a new order and the patient's current wall is less than the current date/time, a new wall is assigned.
11. If the order is a renewal and the order's Start Date plus three is greater than the current wall, a new wall is assigned.
12. If the order is created due to an edit, the wall remains the same.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/093.png)Note: The wall may be edited by a pharmacist, or pharmacy technician, using the *Edit Patient's Default Stop Date* \[PSJU CPDD\] option.

### Pick List Wall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a pick list is created (run), the START DATE selected is, in effect, a wall for the pick list. As long as the actual date (and time) is less than the Start Date, the pick list can be updated. Also, until the Start Date is reached, the pick list cannot be filed away. Conversely, once the Start Date is reached, the pick list can be filed away, but can no longer be updated.

The user can now enter units dispensed before the Start Date is reached to allow greater accuracy of the units needed when a pick list is sent to the ATC dispensing machine.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/094.png)Note: If the user enters the units dispensed for a pick list before the Start Date is reached and then updates the pick list, the units dispensed data could be lost for any order that is updated.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action Prompts</strong></th>
<th>There are three types of Inpatient Medications "Action" prompts that occur during order entry: ListMan, Patient/Order, and Hidden action prompts.</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p><strong>ListMan Action Prompts</strong></p></li>
</ul></td>
<td><p>+ Next Screen</p>
<p>- Previous Screen</p>
<p>UP Up a Line</p>
<p>DN Down a Line</p>
<p>&gt; Shift View to Right</p>
<p>&lt; Shift View to Left</p>
<p>FS First screen</p>
<p>LS Last Screen</p>
<p>GO Go to Page</p>
<p>RD Re Display Screen</p>
<p>PS Print Screen</p>
<p>PT Print List</p>
<p>SL Search List</p>
<p>Q Quit</p>
<p>ADPL Auto Display (on/off)</p></td>
<td></td>
</tr>
<tr class="even">
<td><ul>
<li><p><strong>Patient/Order Action Prompts</strong></p></li>
</ul></td>
<td><p>PU Patient Record Updates</p>
<p>DA Detailed Allergy/ADR List</p>
<p>VP View Profile</p>
<p>NO New Orders Entry</p>
<p>CM Clinic Medication</p>
<p><span id="CM_New_Clinic_Medication_Entry" class="anchor"></span>CM New Clinic Medication Entry</p>
<p>IN Intervention Menu</p>
<p>PI Patient Information</p>
<p>SO Select Order</p>
<p>DC Discontinue</p>
<p>ED Edit</p>
<p>FL Flag</p>
<p>VF Verify</p>
<p>HD Hold</p>
<p>RN Renew</p>
<p>AL Activity Logs</p>
<p>OC On Call</p>
<p>NL Print New IV Labels</p>
<p>RL Reprint IV Labels</p>
<p>RC Recycled IV</p>
<p>DT Destroyed IV</p>
<p>CA Cancelled IV</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Hidden Action Prompts</strong></td>
<td><p>LBL Label Patient/Report</p>
<p>JP Jump to a Patient</p>
<p>OTH Other Pharmacy Options</p>
<p>MAR MAR Menu</p>
<p>DC Speed Discontinue</p>
<p>RN Speed Renew</p>
<p>SF Speed Finish</p>
<p>SV Speed Verify</p>
<p>CO Copy</p>
<p>N Mark Not to be Given</p>
<p>I Mark Incomplete</p>
<p>DIN Drug Restr/Guide</p>
<p>DA Display Drug Allergies</p>
<p>OCI Overrides/Interventions</p>
<p>CK Check Drug Interaction</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Active Order</strong></td>
<td>Any order which has not expired or been discontinued. Active orders also include any orders that are on hold or on call.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Activity Reason Log</strong></td>
<td>The complete list of all activity related to a patient order. The log contains the action taken, the date of the action, and the user who took the action.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Activity Ruler</strong></td>
<td>The activity ruler provides a visual representation of the relationship between manufacturing times, doses due and order start times. The intent is to provide the on-the-floor user with a means of tracking activity in the IV room and determining when to call for doses before the normal delivery. The activity ruler can be enabled or disabled under the <em>SIte Parameters (IV)</em> [PSJI SITE PARAMETERS] option.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Additive</strong></td>
<td>A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin or other nutrient, or an antibiotic. Only electrolyte or multivitamin type additives can be entered as IV fluid additives in CPRS.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>ADMINISTRATION SCHEDULE File</strong></td>
<td>File #51.1. This file contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule type (e.g., QUID, Q4H, PRN). The administration time entered is in military time, with each time separated from the next by a dash, and times listed in ascending order.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Administering Teams</strong></td>
<td>Nursing teams used in the administration of medication to the patients. There can be a number of teams assigned to take care of one ward, with specific rooms and beds assigned to each team.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Admixture</strong></td>
<td>An admixture is a type of intravenously administered medication comprised of any number of additibes (including zero) in one solution. It is given at a specified flow rate, when one bottle or bag is empty, another is hung.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Allergy /ADR Order Check</strong></td>
<td>The screening of a patient's documented allergies or adverse reaction against a medication ordered by a provider.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>APSP INTERVENTION File</strong></td>
<td>File #900932.4. This file used to enter pharmacy interventions. Interventions in this file are records of occurrences where the pharmacist had to take some sort of action involving a particular prescription or order. A record would record the provider involved, why an intervention was necessary, what action was taken by the pharmacists, etc</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Average Unit Drug Cost</strong></td>
<td>The total drug cost divided by the total number of units of measurement.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BCMA</strong></td>
<td>A VistA computer software package named Bar Code Medication Administration. This package validates medications against active orders prior to being administered to the patient.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BSA</strong></td>
<td><p>Body Sufrace Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:<br />
<em>BSA (m²) = 0.20247 x Height (m)<sup>0.725</sup> x Weight (kg)<sup>0.425</sup></em></p>
<p>The equasion is performed using the most recent patient height and weight values that are entered into the vitals package.<br />
The calculation is not intended to be a replacement for independent clinical judgement.</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Chemotherapy</strong></td>
<td>Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type administration can be a syringe, admixture, or a piggyback. Once the subtype (syringe, piggyback, etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (e.g., piggyback type of chemotherapy follows the same entry procedure as regular piggyback IV).</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy "Admixture"</strong></td>
<td>The Chemotherapy "Admixture" IV type follows the same order entry procedure as the regular admixture IV type. This type is in use when the level of toxicity of the chemotherapy drug is high and is to be administered continuously over an extended period of time (e.g., seven days).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Chemotherapy "Piggyback"</strong></td>
<td colspan="2">The Chemotherapy "Piggyback" IV type follows the same order entry procedure as the regular piggyback IV type. This type of chemotherapy is in use when the chemotherapy drug does not have time constraints on how fast it must be infused into the patient. These types are normally administered over a 30-60 minute interval.</td>
</tr>
<tr class="odd">
<td><strong>Chemotherapy "Syringe"</strong></td>
<td colspan="2">The Chemotherapy "Syringe" IV type follows the same order entry procedure as the regular syringe IV type. Its administration may be continuous or intermittent. The pharmacist selects the type when the level of toxicity of the chemotherapy drug is low and needs to be infused directly into the patient within a short time interval (usually 1-2 minutes).</td>
</tr>
<tr class="even">
<td><p><strong>Clinic Group</strong></p>
<p><span id="p118" class="anchor"></span><strong>Clinical Reminder Order Checks (CROC)</strong></p></td>
<td colspan="2"><p>A clinic group is a combination of outpatient clinics that have been defined as a group within Inpatient Medications to facilitate processing of orders.</p>
<p>CPRS Order Checks that use Clinical Reminder functionality, both reminder terms and reminder definitions, to perform checks for groups of orderable items.</p></td>
</tr>
<tr class="odd">
<td><strong>CLINIC DEFINITION File</strong></td>
<td colspan="2">File #53.46.This file is used in conjunction with Inpatient Medications for Outpatients (IMO) to give the user the ability to define, by clinic, default stop dates, whether to auto-dc IMO orders, and whether to send IMO orders to BCMA. Users may also define a Missing Dose Request printer and a Pre-Exchange Report printer.</td>
</tr>
<tr class="even">
<td><strong>CLINIC GROUP File</strong></td>
<td colspan="2">File #57.8. This file is used to provide grouping of clinics for the Non-Verified Pending option and miscellaneous reports.</td>
</tr>
<tr class="odd">
<td><strong>Continuous Syringe</strong></td>
<td colspan="2">A syringe type of IV that is administered continuously to the patient, similar to a hyperal IV type. This type of syringe is commonly used on outpatients and administered automatically by an infusion pump.</td>
</tr>
<tr class="even">
<td><strong>Coverage Times</strong></td>
<td colspan="2">The start and end of coverage period designates administration times covered by a manufacturing run. There must be a coverage period for all IV types: admixtures and primaries, piggybacks, hyperals, syringes, and chemotherapy. For one type, admixtures for example, the user might define two coverage periods; one from 1200 to 0259 and another from 0300 to 1159 (this would mean that the user has two manufacturing times for admixtures).</td>
</tr>
<tr class="odd">
<td><strong>CPRS</strong></td>
<td colspan="2">A VistA computer software package called Computerized Patient Record Systems. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application. All pending orders that appear in the Unit Dose and IV Medications modules are initially entered through the CPRS package.</td>
</tr>
<tr class="even">
<td><strong>CrCL</strong></td>
<td colspan="2"><p>Creatinine Clearance. The CrCL value which displays in the pharmacy header is identical to the CrCL value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p><em>Modified Cockcroft-Gault equation using Adjusted Body Weight in kg (if ht &gt; 60in)</em></p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="odd">
<td><strong>Cumulative Doses</strong></td>
<td colspan="2">The number of IV doses actually administered, which equals the total number of bags dispensed less any recycled, destroyed, or canceled bags.</td>
</tr>
<tr class="even">
<td><strong>DATUP</strong></td>
<td colspan="2">Data Update (DATUP). Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out VA custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the production and pre-production centralized MOCHA databases at Austin and Philadelphia.</td>
</tr>
<tr class="odd">
<td><strong>Default Answer</strong></td>
<td colspan="2">The most common answer, predefined by the system to save time and keystrokes for the user. The default answer appears before the two slash marks (//) and can be selected by the user by pressing &lt;<strong>Enter</strong>&gt;.</td>
</tr>
<tr class="even">
<td><strong>Delivery Times</strong></td>
<td colspan="2">The time(s) when IV orders are delivered to the wards.</td>
</tr>
<tr class="odd">
<td><strong>Dispense Drug</strong></td>
<td colspan="2">The Dispense Drug name has the strength attached to it (e.g., Acetaminophen 325 mg). The name alone without strength attached is the Orderable Item name.</td>
</tr>
<tr class="even">
<td><strong>Dosage Ordered</strong></td>
<td colspan="2">After the user has selected the drug during order entry, the dosage ordered prompt is displayed.</td>
</tr>
<tr class="odd">
<td><strong>DRUG ELECTROLYTES File</strong></td>
<td colspan="2">File #50.4. This file contains the names of anions/cations, and their concentration units.</td>
</tr>
<tr class="even">
<td><strong>DRUG File</strong></td>
<td colspan="2">File #50. This file holds the information related to each drug that can be used to fill a prescription.</td>
</tr>
<tr class="odd">
<td><p><strong>Electrolyte</strong></p>
<p><span id="p120" class="anchor"></span><strong>Enhanced Order Checks</strong></p></td>
<td colspan="2"><p>An additive that disassociates into ions (charged particles) when placed in solution.</p>
<p>Drug–Drug Interaction, Duplicate Therapy, and Dosing order checks that are executed utilizing FDB's MedKnowledge Framework APIs and database.</p></td>
</tr>
<tr class="even">
<td><strong>Entry By</strong></td>
<td colspan="2">The name of the user who entered the Unit Dose or IV order into the computer.</td>
</tr>
<tr class="odd">
<td><strong>Hospital Supplied Self Med</strong></td>
<td colspan="2">Self-med which is to be supplied by the Medical Center's pharmacy. Hospital supplied self-med is only prompted for if the user answers Yes to the SELF MED prompt during order entry.</td>
</tr>
<tr class="even">
<td><strong>Hyperalimentation (Hyperal)</strong></td>
<td colspan="2">Long term feeding of a protein-carbohydrate solution. Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.</td>
</tr>
<tr class="odd">
<td><strong>Infusion Rate</strong></td>
<td colspan="2">The designated rate of flow of IV fluids into the patient.</td>
</tr>
<tr class="even">
<td><strong>INPATIENT USER PARAMETERS File</strong></td>
<td colspan="2">File #53.45. This file is used to tailor various aspects of the Inpatient Medications package with regards to specific users. This file also contains fields that are used as temporary storage of data during order entry/edit.</td>
</tr>
<tr class="odd">
<td><strong>INPATIENT WARD PARAMETERS File</strong></td>
<td colspan="2">File #59.6. This file is used to tailor various aspects of the Inpatient Medications package with regards to specific wards.</td>
</tr>
<tr class="even">
<td><strong>Intermittent Syringe</strong></td>
<td colspan="2">A syringe type of IV that is administered periodically to the patient according to an administration schedule.</td>
</tr>
<tr class="odd">
<td><strong>Internal Order Number</strong></td>
<td colspan="2">The number on the top left corner of the label of an IV bag in brackets ([ ]). This number can be used to speed up the entry of returns and destroyed IV bags.</td>
</tr>
<tr class="even">
<td><strong>IV ADDITIVES File</strong></td>
<td colspan="2">File #52.6. This file contains drugs that are used as additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.</td>
</tr>
<tr class="odd">
<td><strong>IV CATEGORY File</strong></td>
<td colspan="2">File #50.2. This file allows the user to create categories of drugs in order to run "tailor-made" IV cost reports for specific user-defined categories of drugs. The user can group drugs into categories.</td>
</tr>
<tr class="even">
<td><strong>IV Duration</strong></td>
<td colspan="2">The duration of an order may be entered in CPRS at the IV DURATION OR TOTAL VOLUME field in the IV Fluids order dialog. The duration may be specified in terms of volume (liters or milliliters), or time (hours or days). Inpatient Medications uses this value to calculate a default stop date/time for the order at the time the order is finished.</td>
</tr>
<tr class="odd">
<td><strong>IV Label Action</strong></td>
<td colspan="2"><p>A prompt, requesting action on an IV label, in the form of "Action ( )", where the valid codes are shown in the parentheses. The following codes are valid:</p>
<p>P – Print a specified number of labels now.</p>
<p>B – Bypass any more actions.</p>
<p>S – Suspend a specified number of labels for the IV room to print on demand.</p></td>
</tr>
<tr class="even">
<td><strong>IV Room Name</strong></td>
<td colspan="2">The name identifying an IV distribution area.</td>
</tr>
<tr class="odd">
<td><strong>IV SOLUTIONS File</strong></td>
<td colspan="2">File #52.7. This file contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.</td>
</tr>
<tr class="even">
<td><strong>IV STATS File</strong></td>
<td colspan="2">File #50.8. This file contains information concerning the IV workload of the pharmacy. This file is updated each time the <em>COmpile IV Statistics</em> option is run and the data stored is used as the basis for the AMIS (IV) report.</td>
</tr>
<tr class="odd">
<td><strong>Label Device</strong></td>
<td colspan="2">The device, identified by the user, on which computer-generated labels will be printed.</td>
</tr>
<tr class="even">
<td><strong>Local Possible Dosages</strong></td>
<td colspan="2">Free-text dosages associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="odd">
<td><strong>LVP</strong></td>
<td colspan="2">Large Volume Parenteral – Admixture. A solution intended for continuous parenteral infusion, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. It is comprised of any number of additives, including zero, in one solution. An LVP runs continuously, with another bag hung when one bottle or bag is empty.</td>
</tr>
<tr class="even">
<td><strong>Manufacturing Times</strong></td>
<td colspan="2">The time(s) that designate(s) the general time when the manufacturing list will be run and IV orders prepared. This field in the <em>SIte Parameters (IV)</em> [PSJI SITE PARAMETERS] option (IV Room file (#59.5)) is for documentation only and does not affect IV processing.</td>
</tr>
<tr class="odd">
<td><strong>MEDICATION ADMINISTERING TEAM File</strong></td>
<td colspan="2">File #57.7. This file contains wards, the teams used in the administration of medication to that ward and the rooms/beds assigned to that team.</td>
</tr>
<tr class="even">
<td><strong>MEDICATION INSTRUCTION File</strong></td>
<td colspan="2">File #51.2. This file is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion, and intended use.</td>
</tr>
<tr class="odd">
<td><strong>MEDICATION ROUTES File</strong></td>
<td colspan="2">File #51.2. This file contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="even">
<td><strong>Medication Routes/ Abbreviations</strong></td>
<td colspan="2">Route by which medication is administered (e.g., oral). The Medication Routes file (#51.2) contains the routes and abbreviations, which are selected by each VAMC. The abbreviation cannot be longer than five characters to fit on labels and the MAR. The user can add new routes and abbreviations as appropriate.</td>
</tr>
<tr class="odd">
<td><strong>MOCHA</strong></td>
<td colspan="2">Medication Order Check Healthcare Application.</td>
</tr>
<tr class="even">
<td><strong>Non-Formulary Drugs</strong></td>
<td colspan="2">The medications that are defined as commercially available drug products not included in the VA National Formulary.</td>
</tr>
<tr class="odd">
<td><strong>Non-Verified Orders</strong></td>
<td colspan="2">Any order that has been entered in the Unit Dose or IV Medications module that has not been verified (made active) by a nurse and/or pharmacist. Ward staff may not verify a non-verified order.</td>
</tr>
<tr class="even">
<td><strong>Order Check</strong></td>
<td colspan="2">Order checks (drug-allergy/ADR interactions, drug-drug interactions, duplicate drug, and duplicate therapy, and dosing) are performed when a new medication order is placed through either the CPRS or Inpatient Medications applications. They are also performed when medication orders are renewed, when Orderable Items are edited, or during the finishing process in Inpatient Medications. This functionality will ensure the user is alerted to possible adverse drug reactions and will reduce the possibility of a medication error.</td>
</tr>
<tr class="odd">
<td><strong>Order Sets</strong></td>
<td colspan="2">An Order Set is a set of N pre-written orders. (N indicates the number of orders in an Order Set is variable.) Order Sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices and procedures.</td>
</tr>
<tr class="even">
<td><strong>Order View</strong></td>
<td colspan="2">Computer option that allows the user to view detailed information related to one specific order of a patient. The order view provides basic patient information and identification of the order variables.</td>
</tr>
<tr class="odd">
<td><strong>Orderable Item</strong></td>
<td colspan="2">An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense Drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="even">
<td><strong>Parenteral</strong></td>
<td colspan="2">Introduced by means other than by way of the digestive track.</td>
</tr>
<tr class="odd">
<td><strong>Patient Profile</strong></td>
<td colspan="2">A listing of a patient's active and non-active Unit Dose and IV orders. The patient profile also includes basic patient information, including the patient's name, social security number, date of birth, diagnosis, ward location, date of admission, reactions, and any pertinent remarks.</td>
</tr>
<tr class="even">
<td><strong>PECS</strong></td>
<td colspan="2">Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update via DATUP, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, and dosing.</td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td colspan="2">A pending order is one that has been entered by a provider through CPRS without Pharmacy or Nursing finishing the order. Once Pharmacy or Nursing has finished and verified the order, it will become active.</td>
</tr>
<tr class="even">
<td><strong>PEPS</strong></td>
<td colspan="2">Pharmacy Enterprise Product Services. A suite of services that includes Outpatient and Inpatient services.</td>
</tr>
<tr class="odd">
<td><strong>PHARMACY SYSTEM File</strong></td>
<td colspan="2">File #59.7. This file contains data that pertains to the entire Pharmacy system of a medical center, and not to any one site or division.</td>
</tr>
<tr class="even">
<td><strong>Piggyback</strong></td>
<td colspan="2">Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (e.g., Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.</td>
</tr>
<tr class="odd">
<td><strong>Possible Dosages</strong></td>
<td colspan="2">Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="even">
<td><strong>Pre-Exchange Units</strong></td>
<td colspan="2">The number of actual units required for this order until the next cart exchange.</td>
</tr>
<tr class="odd">
<td><strong>Primary Solution</strong></td>
<td colspan="2">A solution, usually an LVP, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. Infusion is generally continuous. An LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.</td>
</tr>
<tr class="even">
<td><strong>Print Name</strong></td>
<td colspan="2">Drug generic name, as it is to appear on pertinent IV output, such as labels and reports. Volume or Strength is not part of the print name.</td>
</tr>
<tr class="odd">
<td><strong>Print Name{2}</strong></td>
<td colspan="2">Field used to record the additives contained in a commercially purchased premixed solution.</td>
</tr>
<tr class="even">
<td><strong>Profile</strong></td>
<td colspan="2">The patient profile shows a patient's orders. The Long profile includes all the patient's orders, sorted by status: active, non-verified, pending, and non-active. The Short profile will exclude the patient's discontinued and expired orders.</td>
</tr>
<tr class="odd">
<td><strong>Prompt</strong></td>
<td colspan="2">A point at which the system questions the user and waits for a response.</td>
</tr>
<tr class="even">
<td><strong>Provider</strong></td>
<td colspan="2">Another term for the physician involved in the prescription of an IV or Unit Dose order for a patient.</td>
</tr>
<tr class="odd">
<td><strong>PSJI MGR</strong></td>
<td colspan="2">The name of the <em>key</em> that allows access to the supervisor functions necessary to run the IV medications software. Usually given to the Inpatient package coordinator.</td>
</tr>
<tr class="even">
<td><strong>PSJI PHARM TECH</strong></td>
<td colspan="2">The name of the <em>key</em> that must be assigned to pharmacy technicians using the IV Medications module. This key allows the technician to finish IV orders, but not verify them.</td>
</tr>
<tr class="odd">
<td><strong>PSJI PURGE</strong></td>
<td colspan="2">The key that must be assigned to individuals allowed to purge expired IV orders. This person will most likely be the IV application coordinator.</td>
</tr>
<tr class="even">
<td><strong>PSJI RNFINISH</strong></td>
<td colspan="2">The name of the <em>key</em> that is given to a user to allow the finishing of IV orders. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="odd">
<td><strong>PSJI USR1</strong></td>
<td colspan="2">The primary menu option that may be assigned to nurses.</td>
</tr>
<tr class="even">
<td><strong>PSJI USR2</strong></td>
<td colspan="2">The primary menu option that may be assigned to technicians.</td>
</tr>
<tr class="odd">
<td><strong>PSJU MGR</strong></td>
<td colspan="2">The name of the <em>primary menu</em> <em>option</em> and of the <em>key</em> that must be assigned to the pharmacy package coordinators and supervisors using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJU PL</strong></td>
<td colspan="2">The name of the <em>key</em> that must be assigned to anyone using the <em>Pick List Menu</em> options.</td>
</tr>
<tr class="odd">
<td><strong>PSJ PHARM TECH</strong></td>
<td colspan="2">The name of the <em>key</em> that must be assigned to pharmacy technicians using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJ RNFINISH</strong></td>
<td colspan="2">The name of the <em>key</em> that is given to a user to allow the finishing of a Unit Dose order. This user must also be a holder of the PSJ RNURSE key.</td>
</tr>
<tr class="odd">
<td><strong>PSJ RNURSE</strong></td>
<td colspan="2">The name of the <em>key</em> that must be assigned to nurses using the Unit Dose Medications module.</td>
</tr>
<tr class="even">
<td><strong>PSJ RPHARM</strong></td>
<td colspan="2">The name of the <em>key</em> that must be assigned to a pharmacist to use the Unit Dose Medications module. If the package coordinator is also a pharmacist he/she must also be given this key.</td>
</tr>
<tr class="odd">
<td><strong>PSJ STAT NOW ACTIVE ORDER Mail Group</strong></td>
<td colspan="2">A mail group that notifies subscribers when a pending STAT or NOW order is made active.</td>
</tr>
<tr class="even">
<td><strong>PSJ STAT NOW PENDING</strong></td>
<td colspan="2">A mail group that notifies subscribers when a pending</td>
</tr>
<tr class="odd">
<td><strong>ORDER Mail Group</strong></td>
<td colspan="2">STAT or NOW order has been received from CPRS.</td>
</tr>
<tr class="even">
<td><strong>Quick Code</strong></td>
<td colspan="2">An abbreviated form of the drug generic name (from one to ten characters) for IV orders. One of the three drug fields on which lookup is done to locate a drug. Print name and synonym are the other two. Use of quick codes will speed up order entry, etc.</td>
</tr>
<tr class="odd">
<td><strong>Report Device</strong></td>
<td colspan="2">The device, identified by the user, on which computer-generated reports selected by the user will be printed.</td>
</tr>
<tr class="even">
<td><strong>Schedule</strong></td>
<td colspan="2">The frequency of administration of a medication (e.g., QID, QDAILY, QAM, STAT, Q4H).</td>
</tr>
<tr class="odd">
<td><strong>Schedule Type</strong></td>
<td colspan="2">Codes include: <strong>O</strong> - one time (i.e., STAT - only once), <strong>P</strong> - PRN (as needed; no set administration times). <strong>C</strong>- continuous (given continuously for the life of the order; usually with set administration times). <strong>R</strong> - fill on request (used for items that are not automatically put in the cart - but are filled on the nurse's request. These can be multidose items (e.g., eye wash, kept for use by one patient and is filled on request when the supply is exhausted). And <strong>OC</strong> - on call (one time with no specific time to be given, i.e., 1/2 hour before surgery).</td>
</tr>
<tr class="even">
<td><strong>Self-Med</strong></td>
<td colspan="2">Medication that is to be administered by the patient to himself.</td>
</tr>
<tr class="odd">
<td><strong>Standard Schedule</strong></td>
<td colspan="2">Standard medication administration schedules stored in the Administration Schedule file (#51.1).</td>
</tr>
<tr class="even">
<td><strong>Start Date/Time</strong></td>
<td colspan="2">The date and time an order is to begin.</td>
</tr>
<tr class="odd">
<td><strong>STAT and NOW Order Notification</strong></td>
<td colspan="2">Sends a text message to subscribers of the PSJ STAT NOW mail groups when a pending STAT or NOW order has been received from CPRS or has been verified and made active.</td>
</tr>
<tr class="even">
<td><strong>Status</strong></td>
<td colspan="2"><strong>A</strong> - active, <strong>E</strong> - expired, <strong>R</strong> - renewed (or reinstated), <strong>D</strong> - discontinued, <strong>H</strong> - on hold, <strong>I</strong> - incomplete, or <strong>N</strong> - non-verified, <strong>U</strong> – unreleased, <strong>P</strong> – pending, <strong>O</strong> – on call, <strong>DE</strong> – discontinued edit, <strong>RE</strong> – reinstated, <strong>DR</strong> – discontinued renewal.</td>
</tr>
<tr class="odd">
<td><strong>Stop Date/Time</strong></td>
<td colspan="2">The date and time an order is to expire.</td>
</tr>
<tr class="even">
<td><strong>Stop Order Notices</strong></td>
<td colspan="2">A list of patient medications that are about to expire and may require action.</td>
</tr>
<tr class="odd">
<td><strong>Syringe</strong></td>
<td colspan="2">Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.</td>
</tr>
<tr class="even">
<td><strong>Syringe Size</strong></td>
<td colspan="2">The syringe size is the capacity or volume of a particular syringe. The size of a syringe is usually measured in number of cubic centimeters (ccs).</td>
</tr>
<tr class="odd">
<td><strong>TPN</strong></td>
<td colspan="2">Total Parenteral Nutrition. The intravenous administration of the total nutrient requirements of the patient. The term TPN is also used to mean the solution compounded to provide those requirements.</td>
</tr>
<tr class="even">
<td><strong>Units per Dose</strong></td>
<td colspan="2">The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted.</td>
</tr>
<tr class="odd">
<td><strong>VA Drug Class Code</strong></td>
<td colspan="2">A drug classification system used by VA that separates drugs into different categories based upon their characteristics. IV cost reports can be run for VA Drug Class Codes.</td>
</tr>
<tr class="even">
<td><strong>VDL</strong></td>
<td colspan="2">Virtual Due List. This is a Graphical User Interface (GUI) application used by the nurses when administering medications.</td>
</tr>
<tr class="odd">
<td><strong>Ward Group</strong></td>
<td colspan="2">A ward group indicates inpatient nursing units (wards) that have been defined as a group within Inpatient Medications to facilitate processing of orders.</td>
</tr>
<tr class="even">
<td><strong>WARD GROUP File</strong></td>
<td colspan="2">File #57.5. This file contains the name of the ward group, and the wards included in that group. The grouping is necessary for the pick list to be run for specific carts and ward groups.</td>
</tr>
<tr class="odd">
<td><strong>Ward Group Name</strong></td>
<td colspan="2">A field in the WARD GROUP File (#57.5) used to assign an arbitrary name to a group of wards for the pick list and medication cart.</td>
</tr>
<tr class="even">
<td><strong>WARD LOCATION File</strong></td>
<td colspan="2">File #42. This file contains all of the facility ward locations and their related data, i.e., Operating beds, Bedsection, etc. The wards are created/edited using the <em>Ward Definition</em> option of the Automatic Data Transmission (ADT) module.</td>
</tr>
</tbody>
</table>
(*This page included for two-sided copying*.)

# Appendix A: Inpatient Medication Orders for Outpatients–Phase I & II and Inpatient Medication Reqs for SFG IRA–Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides a brief description of the new features and functions of the Inpatient Medication Orders for Outpatients and the Inpatient Medication Requirements for SFG IRA – Phase II projects. These projects consist of multiple patches, which must be installed for the functionality to perform.

This product shall run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters and run VMS DSM, or Cache VMS.

The following software must be running to support the enhancements requested:

- Kernel V. 8.0
- VA FileMan V. 22.0
- MailMan V. 8.0
- Inpatient Medications V. 5.0
- Scheduling V. 5.3
- Order Entry Results Reporting V. 3.0 (CPRS)Bar Code Medication Administration V. 3.0 (BCMA)

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/095.png)Note: PSI-03-060 "IV Fluid Dialog" has been addressed in CPRS GUI V. 25 by adding a new field "Duration or Total Volume" to the IV dialog per the CPRS Clinical Workgroup recommendation. By using this field, a user can specify administrative duration or total volume for the IV order. This new field, when utilized as a duration, however, will override the IV Room site parameter LVP'S GOOD FOR HOW MANY DAYS, as well as any other time restrictions on Orderable Items. Additional CPRS Clinical and Inpatient Medications Workgroup discussion is necessary to determine a resolution to this issue.

## Inpatient Medication Orders for Outpatients – Phase I & II 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the Inpatient Medication Orders for Outpatients are grouped and discussed below. These changes will give the user the ability to order unit dose medications for outpatients. This project consists of multiple patches, which must be installed for the functionality to perform.

- OR\*3\*195 (with GUI V. 25) (released January 2005)
- PSS\*1\*59 (released January 2005)
- PSJ\*5\*111 (released January 2005)
- SD\*5.3\*285 (released March 2005)
- PSJ\*5\*112 (released March 2005)
- PSS\*1\*86 (released March 2005)

### Inpatient Medications V. 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality required for permitting Inpatient Medication unit dose orders for Outpatients.

#### New Functionality

<u>Unit Dose Medications</u>

Modifications were made to most Unit Dose Medications options to allow processing of unit dose orders for patients currently in or with an appointment scheduled for a clinic that allows Inpatient Medication orders. The order will be associated with a specific clinic and appointment. However, the order may cover more than one appointment. The existing IV order functionality for Outpatients that are not in a clinic that allows administration of Inpatient Medications for Outpatients (IMO) will not be affected by this enhancement.

1.  All Inpatient Medications unit dose orders for Outpatients shall sort under the Clinic or Clinic Group for the following options:
    1.  *Non-Verified/Pending Orders* \[PSJU VBW\] *– Pending/Non-Verified Order Totals Display*
    2.  *Non-Verified/Pending Orders* \[PSJU VBW\] *– Unit Dose Orders Selection Display*
13. The Patient Information Display screen was modified to add Clinic and Date/Time of Appointment. Only those appointments with a clinic that allows administration of Inpatient Medications will be displayed.
14. The software was modified to allow an Inpatient Medications unit dose non-verified order for an outpatient to be selected, finished, accepted and verified via the following options:
1.  *Non-Verified Orders* \[PSJU VBW\]
2.  *Inpatient Order Entry* \[PSJ OE\]
15. The clinic and appointment date and time that the order is associated with will be stored in the PHARMACY PATIENT file (#55) for both unit dose and IV orders.
16. Modifications were made to specific Reports on the Reports Menu that will allow sorting and reporting for patients that are currently in or with an appointment scheduled for a clinic that allows administration of Inpatient Medication orders for Outpatients. The following options were modified to allow selection by the Ward Group ^OTHER or to select Outpatients:
1.  *Inpatient Profile* \[PSJ PR\]
2.  *Action Profile \#1* \[PSJU AP-1\]
3.  *Medications Due Worksheet* \[PSJ MDWS\]
4.  *Patient Profile Extended* \[PSJ EXTP\]
17. Modifications were made to specific Reports on the Reports Menu that will allow sorting and reporting by Clinic and Clinic Group for patients that are currently in or with an appointment scheduled for a clinic that allows administration of Inpatient Medication orders for Outpatients. The following options were modified:
1.  *Action Profile \#2* \[PSJU AP-2\]
2.  *Patient Profile (Unit Dose)* \[PSJU PR\]
3.  *Inpatient Stop Order Notices* \[PSJ EXP\]
4.  *Label Print/Reprint* \[PSJU LABEL\]
18. The MAR reports were modified in the following ways:
1.  *Allow selection of Clinic and Clinic Group, to include Outpatients with Inpatient Medication orders.*
2.  *Leave the Room/Bed blank when printing Outpatients.*
3.  *Change the 'Ward' to 'Loc'.*
4.  *Print Ward for Loc for Inpatients and hospital location for Loc for Outpatients.*
19. Messaging between CPRS and Inpatient Medications has been changed to include the appointment date/time for Inpatient Medication orders for Outpatients that are associated with a clinic appointment.
20. The CLINIC STOP DATES file (#53.46) was renamed to the CLINIC DEFINITION file (#53.46). The *Clinic Stop Dates* \[PSJ CSD\] option has been removed, and the *Clinic Definition* \[PSJ CD\] option has been added under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option. The option allows sites to define additional parameters on a clinic-by-clinic basis for handling Inpatient Medications for Outpatients orders. Users can define, by clinic, stop date calculations, auto-dc behavior, and availability in BCMA.
21. With patch PSJ\*5\*399, <span id="Patch_399_Indication_New_Update" class="anchor"></span>the user will be prompted for Indication. The list of indications is retrieved from the Pharmacy Orderable item file (#50.7) field \#14 MOST COMMON INDICATION FOR USE and field \#13 INDICATION FOR USE subfile (#50.713). Indication is not a required field in backdoor but is a required field in CPRS.

### Order Entry Results Reporting V. 3.0 (CPRS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality that CPRS now provides to permit an ordering provider to enter an Inpatient Medication (unit dose) order for any Outpatient in an authorized HOSPITAL LOCATION file (#44) as established by the Location for Current Activities.

#### New Functionality

CPRS was modified to present the user with the Inpatient Medication Order Dialog in conjunction with the Inpatient Orderable Item Medication list when an order is placed for an Outpatient from an authorized Hospital Location.

When a user selects the Inpatient Medication Order action in a Hospital Location that is not authorized, they shall continue to be presented with the IV Medication Orderable Item list. If an IV Medication order needs to be placed for an Outpatient from an authorized clinic, sites that have not added the IV Medications list to the Write Order list will need to do so.

Inpatient Medication (unit-dose) orders are permitted for Outpatients when the following conditions are met:

- The patient has a status of *Outpatient.*
- The patient has an appointment on the current day, or a day in the future, in an authorized Hospital Location.
- The unit dose order is being placed against an authorized Hospital Location.
- The order is placed from the CPRS Orders Tab or the CPRS Meds Tab when the parameter ORWDX is set with a menu pointing to the Inpatient Medication order dialog.

The system was modified to permit Inpatient Medication orders to be placed for patients in an authorized clinic, without a scheduled appointment, when the visit is concurrent with placement of the order. This permission allows designated Hospital Locations, such as the Emergency Room, to submit Inpatient orders in the absence of a scheduled appointment in an authorized clinic.

Inpatient Medication orders written for outpatients have the status of inpatient orders. They are:

- Filled by Inpatient Pharmacy
- Dispensed by Inpatient Pharmacy
- Displayed in CPRS as inpatient orders

CPRS continues to apply all existing medication order checks to the Inpatient Medication orders written for Outpatients.

Providers are permitted to use Personal Quick Orders to submit orders from the Inpatient Medication Orderable Item list when such orders are congruent with the patient's appointment in an authorized Hospital location. Medication quick orders that have been created and placed on site-defined order menus shall perform according to existing functionality.

Users shall continue to be permitted to define the date range of appointments listed in the Location for Current Activities box with the appointments/visits conforming to the API ORWCV VST.

#### Modified and New Routines

<u>ORWDX (Modified)</u>

Before saving the Inpatient Medication Order for an Outpatient, the routine will run an internal check to see if it is an IMO order. If true, the display group will be set to inpatient display group. The order will be saved with the appointment data.

<u>ORMBLD (New)</u>

Previously, the Health Level Seven (HL7) message of Inpatient Medication order was passed to the Inpatient Medications package from CPRS side without the scheduled appointment data. The HL7 message of Inpatient Medication order shall now include the appointment data along with the order's data.

<u>ORWDXA (New)</u>

When any of the copy, change, and renew actions are being taken on IMO orders, the validation routine shall check the authorization of the hospital location. If it is an authorized location, the action can proceed, otherwise, action shall be denied.

#### CPRS Modifications for Inpatient Medications Interface

CPRS shall pass to the Inpatient Medication (IPM) the IEN of the HOSPITAL LOCATION file (#44) from which the medication orders are being written and the appointment the order is being written against. CPRS shall use the existing HL7 messaging with IPM.

#### CPRS Requirements for Post-Entry Action

IMO orders are eligible for post-entry actions when the order-action is submitted against an appointment/visit in an authorized clinic on the current day or in the future. The following actions are permitted:

- Change
- Copy to New Order
- Renew

The system was modified to display warning dialogs if a user attempts a post-entry edit action on an existing IMO order from an unauthorized clinic or if the action is not permitted.

### Scheduling V. 5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality that Scheduling will provide to define Inpatient Medications orders in the HOSPITAL LOCATION file (#44) and in the API, which will return the necessary information to CPRS to process an order.

#### New Functionality

The HOSPITAL LOCATION file (#44) was modified to add the ADMINISTER INPATIENT MEDS? field (#2802). Valid values are YES and null. A YES value indicates that the clinic is authorized to dispense Inpatient Medications to Outpatients. This field is editable to allow a YES to be deleted.

The *Set-up a Clinic* \[SDBUILD\] option was modified to include a prompt for the new ADMINISTER INPATIENT MEDS? field (#2802).

A new *Inpatient Medications to Clinic* \[SD IMO EDIT\] option was added, which enables Non-Scheduling users to modify the values of the ADMINISTER INPATIENT MEDS? field (#2802) outside of the *Set-up a Clinic* \[SDBUILD\] option. This option allows the user to select the clinic in the HOSPITAL LOCATION NAME field (#.01) and enter YES to designate the clinic is authorized to dispense Inpatient Medications to Outpatients in the ADMINISTER INPATIENT MEDS?" field (#2802).

Scheduling provides an API to return the date/time of a scheduled appointment or checked-in visit in an authorized clinic for a selected patient. The date/time of the checked-in visit shall be not less than <today@.0001> and not greater than [today @2359](mailto:today@2359). Appointments scheduled for the current day or a day in the future are allowed regardless of check-in status.

## Inpatient Medication Requirements for SFG IRA – Phase II 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a brief description of the new features, functions, and enhancements of the Inpatient Medication Requirements for SFG IRA – Phase II project. This project consists of multiple patches, which must be installed for the functionality to perform.

- OR\*3\*195 (with GUI V. 25)
- PSS\*1\*59
- PSJ\*5\*111

### Inpatient Medications V. 5.0 and Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications Requirements for the Special Focus Group IRA – Phase II project will prevent users from entering free-text schedules for inpatient medication orders. This change was requested for patient safety purposes. There have been problems with the calculation of the correct frequency for schedules that are entered as free-text. The best example is the schedule "EVERY NIGHT". A person can interpret this easily. However, using pattern matching logic, the only character that is recognized is the letter 'H', which would indicate an 'hourly' schedule, rather than the once-a-day that is being requested.

For the purposes of this project a valid schedule must meet one of the following conditions:

- Defined in the ADMINISTRATION SCHEDULE file (#51.1)
- Contain PRN, if the rest of the schedule is in the ADMINISTRATION SCHEDULE file (#51.1), i.e., Q4H PRN, where Q4H is in 51.1.
- Day-of-Week or <Day-of-Week@admin> time schedule
- Admin-time only schedule format

The patch PSS\*1\*59 helps accomplish this by changing the validation of schedules entered through Computerized Patient Record System (CPRS) V. 1.0. This validation requires that schedule meet the valid schedule guidelines above. In addition, this patch modifies the definition of schedules in the ADMINISTRATION SCHEDULE file (#51.1). To accomplish this, the following changes are being made to the PSSJ SCHEDULE EDIT input template:

- Do not allow entry of a schedule with the name of "OTHER."
- Do not allow entry of administration times for odd schedules.
- Display the calculated frequency to the user.

Based on the upcoming requirement from the Joint Commission on Accreditation of Hospital Organizations, schedule names that are considered dangerous will no longer be allowed. The four schedules that will no longer be allowed are: QD, HS, TIW, and QOD. These schedules cannot be used either alone or as part of a schedule name. For example: QD is not allowed. Neither is QD ONCE.

The Inpatient Medications patch PSJ\*5\*111 helps accomplish the goals of the Inpatient Medications Requirements for the Special Focus Group IRA – Phase II project by ensuring that no order will be allowed to become active if the schedule does not meet the guideline outlined above.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/096.png)Note: No changes are forced for currently active orders. However, when an action other than discontinue is taken on the order, the software will require the user to select a schedule that meets the valid schedule conditions listed above.  
Order Entry Results Reporting V. 3.0 (CPRS)

When placing inpatient medication orders, users can no longer enter free-text schedules. Instead, users must select standard schedules from the Schedule list box or select "OTHER" from the Schedule list box to create a customized day-of-week or admin/time schedule. If users try to copy, transfer, or renew inpatient medication orders, CPRS allows only orders with valid schedules to proceed.

![](inpatient-medications-technical-manual-security-guide-updated-psj-5-399/097.png)Note: If the user selects "OTHER" to create a customized schedule, the order may require that the pharmacist and the physician work out a valid schedule, which might delay the order becoming active. The parameter ORWIM NSS MESSAGE enables sites to customize the message in the text box on the Order with Schedule "OTHER" dialog to inform providers that a delay may be caused or give instructions. A default message appears in the text box if the site does not enter one.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the necessary patches, you must install the Computerized Patient Record System (CPRS) V. 1.0 GUI V. 25 multi-package build, following its installation instructions.

### Post-Installation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are ready to implement Inpatient Medication Orders for Outpatients, you will need to perform the following setup actions.

#### CPRS V. 1.0

You will need to add the Clinic Medications display group. Please refer to the CPRS V. 1.0 GUI V. 25 Release Notes (OR_30_195RN.PDF) for detailed instructions on adding the Clinic Medications display group.

#### Scheduling V. 5.3

Use the *Set-up a Clinic* \[SDBUILD\] option or the *Inpatient Medications To Clinic* \[SD IMO EDIT\] option to mark the appropriate HOSPITAL LOCATIONS as able to administer inpatient medications.

#### Inpatient Medications V. 5.0

Use the *Clinic Definition* \[PSJ CD\] option to define the behavior you require for Inpatient Medication Orders for Outpatients. In this option, you can control the auto-dc of IMO orders (where Inpatient Medications V. 5.0 controls this action), the stop date calculation, and whether or not IMO orders will be sent to BCMA if the patient is admitted.

# Appendix B: Pharmacy Interface Automation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides a brief description of the new features and functions of the Pharmacy Interface Automation project. This projects consist of multiple patches, which must be installed for the functionality to perform.

The Clinical Ancillary Services (CAS) Development Delivery of Pharmacy enhancements (DDPE) Pharmacy Interface Automation project supports the initiative to create an automated interface between the Pharmacy Automated Dispensing Equipment (PADE) used in the inpatient and outpatient care settings and VistA Pharmacy and Admission Discharge Transfer (ADT) applications. This will allow VA health care users the ability to access, transmit, receive alerts, and generate reports on medication transactions.

Pharmacy Interface Automation is a vital enhancement to the medication transaction functions of the PADE. It will allow pharmacists to access dispensing equipment remotely; keep a perpetual inventory of all medication received, dispensed, and wasted; alert the pharmacy of medication removed from the devices without orders; and establishes monitors for potentially inappropriate electronic pharmacy transactions.

This product shall run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities.

The minimum required VistA software is:

| Package                                        | Minimum Version Needed |
|----------------------------------------------------|----------------------------|
| Adverse Reaction Tracking (ART)                    | 4.0                        |
| BCMA                                               | 3.0                        |
| Computerized Patient Record System (CPRS)          | 3.0                        |
| Controlled Substance                               | 3.0                        |
| Drug Accountability                                | 3.0                        |
| VA FileMan                                         | 22.0                       |
| HL7                                                | 2.4                        |
| Inpatient Medications (IP)                         | 5.0                        |
| Kernel                                             | 8.0                        |
| MailMan                                            | 7.1                        |
| Master Patient Index/Patient Demographics (MPI/PD) | 1.0                        |
| National Drug File (NDF)                           | 4.0                        |
| Nursing Service                                    | 4.0                        |
| Order Entry/Results Reporting (OERR)               | 3.0                        |
| Registration                                       | 5.3                        |
| Pharmacy Data Management (PDM)                     | 1.0                        |
| Remote Procedure Call (RPC) Broker                 | 1.1                        |
| Scheduling                                         | 5.3                        |

## New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new automated bidirectional interface between VistA and PADE will be designed and developed utilizing VIE as the middleware component for communication of HL7 messages and error handling. The added functional components are:

- Provide pharmacists the capability to remotely access dispensing equipment to provide the pharmacist the status of drugs: whether they have been dispensed, or in the queue or some error condition that may have been encountered by the dispensing equipment.
- Provide PADE the capability to transmit dispensing information to VistA Pharmacy to keep a perpetual inventory of all drugs/medications received, dispensed, and wasted.
- Provide PADE the capability to alert VistA Pharmacy of medication removal from PADE without orders.
- Establish monitors of all potentially inappropriate electronic pharmacy transactions. The contractor shall implement trending reports in order to address and detect potentially inappropriate pharmacy transactions, such as drug diversion. For example, reports include the ability to sort transactions by nursing, user, drug, etc., and from the VA-side of the interface.

Refer to the following Pharmacy Interface Automation documents for additional information:

- 
- [Pharmacy Interface Automation Installation Guide](http://www.va.gov/vdl/application.asp?appid=88)
- [Inpatient Medications Nurse's User Manual](http://www.va.gov/vdl/application.asp?appid=88) [Pharmacy Interface Automation Troubleshooting Guide](http://www.va.gov/vdl/application.asp?appid=88)
- [Pharmacy Data Management Technical Manual/Security Guide](http://www.va.gov/vdl/application.asp?appid=93)
- [Pharmacy Data Management User Manual](http://www.va.gov/vdl/application.asp?appid=93)

## Options and Build Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the options and build components for Pharmacy Interface Automation for PSJ\*5.0\*317:

1\. The following new files were created:

PADE SYSTEM SETUP file (#58.7)

PADE SEND AREA file (#58.71)

PADE OUTBOUND MESSAGES file (#58.72)

PADE INVENTORY SYSTEM file (#58.601)

PADE INBOUND TRANSACTIONS file (#58.6)

PADE DISPENSING DEVICE file (#58.63)

PADE USER file (#58.64)

2\. A new menu, PADE Main Menu \[PSJ PADE MAIN MENU\], with the following

options was created:

PADE Send Area Setup \[PSJ PADE SEND AREA SETUP\] option

PADE System Setup \[PSJ PADE SETUP\] option

PADE Send Surgery Cases \[PSJ PADE SEND SURGERY CASES\] option

PADE Send Patient Orders \[PSJ PADE SEND ORDERS\] option

PADE Inventory Setup \[PSJ PADE INVENTORY MENU\] option

...Inventory System Setup \[PSJ PADE INVENTORY SYSTEM\] option

...Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option

PADE Reports \[PSJ PADE REPORTS MENU\] option

...PADE On-Hand Amounts \[PSJ PADE INVENTORY REPORT\] option

...PADE Transaction Report \[PSJ PADE TRANSACTION REPORT\] option

3\. A new security key, PSJ PADE MGR, was created to allow access to the

above menus noted in item 2.

4\. The option, PADE System Division Setup \[PSJ PADE DIVISION SETUP\],

was exported as a separate option so that it can be given to an

assigned user to set up a division under a PADE.

5\. A new security key, PSJ PADE ADV, was created to allow access to the

above option noted in item 4.

6\. The option, PADE Surgery Task \[PSJ PADE SURGERY TASK\], was exported as

a standalone option so that sites can schedule it as a recurring task.

7\. The option, PADE Appointment Task \[PSJ PADE APPOINTMENT TASK\], was

exported as a standalone option so that sites can schedule it as a

recurring task.

8\. Two HL7 application parameters, PSJ VISTA and PSJ PADE SERVER, were

created for site specific information.

9\. One Logical Link, PSJ PADE, was created to support the Outbound HL7

messages.

10\. The following protocols were created to receive and send outbound

Admission, Discharge and Transfer (ADT) events:

PSJ ADT-A01 ROUTER

PSJ ADT-A01 SERVER - Admission event

PSJ ADT-A01 CLIENT

PSJ ADT-A02 SERVER - Transfer event

PSJ ADT-A02 CLIENT

PSJ ADT-A03 SERVER - Discharge event

PSJ ADT-A03 CLIENT

PSJ ADT-A08 SERVER - Demographic changes

PSJ ADT-A08 CLIENT

PSJ ADT-A11 SERVER - Cancel Admission event

PSJ ADT-A11 CLIENT

PSJ ADT-A12 SERVER - Cancel Transfer event

PSJ ADT-A12 CLIENT

PSJ ADT-A13 SERVER - Cancel Discharge event

PSJ ADT-A13 CLIENT

PSJ ADT-A01 ROUTER is setup as a subscribing protocol to VAFC ADT-A01

SERVER, VAFC ADT-A02 SERVER, VAFC ADT-A03 SERVER, VAFC ADT-A08 SERVER,

VAFC ADT-A08-TSP SERVER (bed switch), VAFC ADT-A11 SERVER, VAFC

ADT-A12 SERVER, VAFC ADT-A13 SERVER.

In the REGISTRATION V. 5.3 package, options like Admit a Patient \[DG

ADMIT PATIENT\], Transfer a Patient \[DG TRANSFER PATIENT\], Discharge a

Patient \[DG DISCHARGE PATIENT\], Switch Bed \[DG BED SWITCH\] etc., will

trigger appropriate outbound HL7 messages.

The routine tied to protocol PSJ ADT-A01 ROUTER that subscribes to

these events (VAFC ADT related protocol) will scan the HL7 message and

will build a modified copy of the HL7 message including the Allergy

(AL1) and the Observation/Result (OBX) segments. The generated HL7

message will be sent to the respective PADE via the Vitria Interface

Engine (VIE).

11\. The following protocols were created to receive and send outbound

Clinic check-ins and appointments.

PSJ SIU-SDAM ROUTER - subscribing protocol to VAFC ADT-A08-SDAM

SERVER

PSJ SIU-S12 SERVER - event driver for clinic check-in

PSJ SIU-S12 CLIENT - subscriber

During patient check-in in the Scheduling V. 5.3 package, the

protocol, VAFC ADT-A08-SDAM SERVER builds a standard HL7 message.

The routine tied to protocol PSJ SIU-SDAM ROUTER that subscribes

to the VAFC ADT-A08-SDAM SERVER, will scan the HL7 message and will

build a new copy of the HL7 message including the Allergy (AL1)

and the Observation/Result (OBX) segments. The generated HL7 message

will be sent to the respective PADE via the Vitria Interface Engine

(VIE).

12\. The following protocols were created to send outbound order messages

in the form of RDE-O11 HL7 messages to the appropriate PADE system.

PSJ RDEO11 SERVER

PSJ RDEO11 CLIENT

In Inpatient Medications, when orders are verified, edited, renewed,

discontinued, reinstated, put on hold/removed from hold, and when

orders are discontinued in Computerized Patient Record System (CPRS)

V. 3.0, an outbound HL7 message will be sent to the respective PADE

via the Vitria Interface Engine (VIE).

13\. The following protocols were created to receive and process inbound

PADE Activity (e.g., Dispense, Load, etc.) in the form of

OMS-O05 HL7 messages:

PSJ PADE OMS-O05 EVENT

PSJ PADE OMS-O05 SUB

PSJ PADE OMS-O05 EVENT 2.3

PSJ PADE OMS-O05 SUB 2.3

Backward compatible HL7 v2.3 protocols accept and parse current

industry standard Pocket Maintenance (ZPM) segments to facilitate

transition to the new PADE standard.

Inbound HL7 messages from the PADE vendor are validated and filed into

the PADE INBOUND TRANSACTION file (#58.6), which triggers an

automatic update of the inventory information in the PADE INVENTORY

SYSTEM file (#58.601).

14\. A new multiple, DWO MESSAGE ENTITY, has been added to the PADE

INVENTORY SYSTEM file (#58.601) to contain mail groups that will

receive Mailman messages when PADE drugs are Dispensed Without an

Order (DWO).

15\. A new multiple, CONFIG ERRORS MAIL GROUPS, has been added to the PADE

INVENTORY SYSTEM file (#58.601) to receive error messages when

configuration problems are encountered with Inbound PADE HL7

messages.

16\. A new multiple, DATA ERRORS MAIL GROUPS, has been added to the PADE

INVENTORY SYSTEM file (#58.601) to receive error messages when data

validation problems are encountered with Inbound PADE HL7 messages.

17\. Inpatient Pharmacy Order Entry screens have been modified to

display PADE inventory information, specifically:

a\. The Inpatient Pharmacy Order Entry order detail screens

will contain a new "PADE" column when displaying Dispense Drugs,

containing the PADE inventory availability for the displayed

dispense drug. To make room for the PADE inventory information,

the message field will continue displaying, but drug classes will

no longer display as a FileMan identifier when a list of dispense

drug choices are displayed.

b\. The Inpatient Pharmacy Order Entry Patient Profile screen

includes a flag, (PD), indicating whether or not the order

contains a drug that is a PADE stock item. If a drug is both a

PADE item and a Ward Stock item, the ward stock flag (WS) is

combined with the PADE flag (WP).

18\. A Kernel parameter, PSJ PADE OE BALANCES, has been created to allow

each site to control whether or not PADE inventory information

displays in the Inpatient Order Entry profile screens and drug

lookups. A prompt to set the parameter has been added to the new PSJ

PADE INVENTORY Input Template, accessible via the Inventory System

Setup \[PSJ PADE INVENTORY SYSTEM\] option.

19\. The option, Pick List \[PSJU PL\], has been modified to include the

drug Internal Entry Number (IEN) field after the drug name and to

include the word "PADE" if the medication listed is a PADE stock

item.

20\. A new Protocol, PSJ LM PADE ACTIVITY, has been added to the PSJ LM

PROFILE HIDDEN ACTIONS Protocol to display a new hidden action (PD)

in the Inpatient Pharmacy patient profile screen. The new PD hidden

action displays all of the PADE transactions for the patient being

displayed.

21\. The Pre-Exchange DOSES prompt that displays after verifying an

Inpatient Unit Dose order has been modified to default the number of

doses to zero when the drug may be dispensed from PADE, and a message

is displayed explaining the drug is a PADE item.

22\. This patch also provides a log file, PADE OUTBOUND MESSAGES

file (#58.72) of the outbound ADT, SIU and RDE HL7 messages to use

with FileMan for trouble shooting purposes only.

> **NOTE:** The nightly background job (PSGBRJ) has been modified to purge

records older than 30 days.

> **NOTE:** This patch also exports a post-install routine PSJ317P that will

setup PSJ ADT-A01 ROUTER as a subscribing protocol to VAFC ADT-A01

SERVER, VAFC ADT-A02 SERVER, VAFC ADT-A03 SERVER, VAFC ADT-A08 SERVER,

VAFC ADT-A08-TSP SERVER, VAFC ADT-A11 SERVER, VAFC ADT-A12 SERVER and VAFC

ADT-A13 SERVER protocols. It will also setup protocol PSJ SIU-SDAM ROUTER

as a subscribing protocol to VAFC ADT-A08-SDAM SERVER protocol.

The post-install also sets the following field to the PSJ PADE entry in

the HL LOGICAL LINK file (#870):

a\. AUTOSTART field (#4.5) is set to 1 (Enabled) so that the PSJ PADE

logical link will be started automatically when Cache or TaskMan is

restarted.

b\. DO NOT PING field (#24) is set to 1 (Yes) due to the unique aspects

of the PADE interface. If PSJ PADE is sent an HLO PING CLIENT

message, an infinite loop will be created consisting of VIE sending

VistA additional CR messages and VistA not responding. This

situation requires manual intervention by a member of the VIE

National Admins team and therefore needs to be avoided.

This post-install routine will be deleted from your system upon completion

of the patch installation.

Patch Components

================

Files & Fields Associated:

File Name (#) Field Name New/Modified/Deleted

------------ ---------- --------------------

PADE SYSTEM SETUP (#58.7) All fields New

PADE SEND AREA (#58.71) All fields New

PADE OUTBOUND MESSAGES (#58.72) All fields New

PADE DISPENSING DEVICE (#58.63) All fields New

PADE INBOUND TRANSACTIONS (#58.6) All fields New

PADE INVENTORY SYSTEM (#58.601) All fields New

PADE USER (#58.64) All fields New

INPATIENT WARD PARAMETERS (#59.6) DEFAULT 0 ON PADE New

PRE-EXCHANGE (#8)

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

Kernel Parameters Associated:

Kernel Parameter Name Entities Values

--------------------- --------------- --------

PSJ PADE OE BALANCES System,Division YES/NO

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

Options Associated:

Option Name Type New/Modified/Deleted

----------- ---- --------------------

Unit Dose Medications \[PSJU MGR\] Menu Modified

PADE Main Menu \[PSJ PADE MAIN MENU\] Menu New

PADE Send Area Setup \[PSJ PADE SEND Option New

AREA SETUP\]

PADE System Setup \[PSJ PADE SETUP\] Option New

PADE Inventory Setup \[PSJ PADE Menu New

INVENTORY MENU\]

Inventory System Setup \[PSJ PADE Option New

INVENTORY SYSTEM\]

Dispensing Device Setup \[PSJ PADE Option New

DEVICE SETUP\]

PADE Send Surgery Cases \[PSJ PADE Option New

SEND SURGERY CASES\]

PADE Surgery Task \[PSJ PADE SURGERY Option New

TASK\]

PADE Reports \[PSJ PADE REPORTS MENU\] Menu New

PADE On-Hand Amounts \[PSJ PADE Option New

INVENTORY REPORT\]

PADE Transaction Report \[PSJ PADE Option New

TRANSACTION REPORT\]

PADE System Division Setup \[PSJ PADE Option New

DIVISION SETUP\]

PADE Send Patient Orders \[PSJ PADE Option New

SEND ORDERS\]

PSJ PADE Appointment Task \[PSJ PADE Option New

APPOINTMENT TASK\]

Protocols Associated:

Protocol Name New/Modified/Deleted

------------- --------------------

PSJ ADT-A01 CLIENT New

PSJ ADT-A01 ROUTER New

PSJ ADT-A01 SERVER New

PSJ ADT-A02 SERVER New

PSJ ADT-A02 CLIENT New

PSJ ADT-A03 SERVER New

PSJ ADT-A03 CLIENT New

PSJ ADT-A11 SERVER New

PSJ ADT-A11 CLIENT New

PSJ ADT-A12 SERVER New

PSJ ADT-A12 CLIENT New

PSJ ADT-A13 SERVER New

PSJ ADT-A13 CLIENT New

PSJ SIU-SDAM ROUTER New

PSJ SIU-S12 SERVER New

PSJ SIU-S12 CLIENT New

PSJ RDEO11 SERVER New

PSJ RDEO11 CLIENT New

PSJ PADE OMS-O05 EVENT New

PSJ PADE OMS-O05 SUB New

PSJ PADE OMS-O05 EVENT 2.3 New

PSJ PADE OMS-O05 SUB 2.3 New

PSJ LM PADE ACTIVITY New

PSJ LM PROFILE HIDDEN ACTIONS Modified

Security Keys Associated:

Security Key Name New/Modified/Deleted

----------------- --------------------

PSJ PADE ADV New

PSJ PADE MGR New

Templates Associated:

Template Name Type File Name (#) New/Modified/Deleted

------------- ---- ------------ --------------------

PSJ PADE SYSTEM Input 58.7 New

PSJ PADE INVENTORY Input 58.601 New

PSJ PADE DISPENSING DEVICE Input 58.63 New

New Service Requests (NSRs):

----------------------------

20000801 - Inpatient Pharmacy Orders HL7 Interface

Patient Safety Issues (PSIs):

-----------------------------

N/A

Remedy Ticket(s) & Overviews:

-----------------------------

N/A

TEST Sites:

===========

HC NETWORK UPSTATE NY (ALBANY)

HEARTLAND-WEST HCS

INDIANAPOLIS, IN

LONG BEACH, CA

MARYLAND HCS

Software and Documentation Retrieval Instructions:

--------------------------------------------------

Software being released as a host file and/or documentation describing

the new functionality introduced by this patch are available.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may

also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure

File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at

the following OI Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library

at: http://www.va.gov/vdl/

The documentation will be in the form of Adobe Acrobat files.

File Description File Name FTP Mode

--------------------------------------------------------------------------

Inpatient Medications Pharmacist's PSJ_5_UM_R0816.PDF Binary

User Manual

Inpatient Medications Technical PSJ_5_TM_R0816.PDF Binary

Manual/ Security Guide

Inpatient Medications Pharmacy Interface PSJ_5_P317_IG.PDF Binary

Automation Installation Guide

Inpatient Medications Pharmacy Interface PSJ_5_P317_TG.PDF Binary

Automation Startup and Troubleshooting Guide

Patch Installation:

Pre/Post Installation Overview

------------------------------

N/A

Installation Instructions

-------------------------

This patch should be installed with users off the system during off-peak

hours. Installation takes less than five minutes.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System menu, select the

Installation menu.

3\. From this menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter PSJ\*5.0\*317)

a\. Backup a Transport Global - this option will create a backup

message of any routines exported with the patch. It will NOT

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - this option will

allow you to view all changes that will be made when the patch

is installed. It compares all components of the patch (routines,

DDs, templates, etc.).

c\. Verify Checksums in Transport Global - this option will ensure

the integrity of the routines that are in the transport global.

4\. Use the Install Package(s) option and select the package PSJ\*5.0\*317.

5\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//" respond NO.

6\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

7\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

Routine Information:

====================

The second line of each of these routines now looks like:

;;5.0;INPATIENT MEDICATIONS;\*\*\[Patch List\]\*\*;16 DEC 97;Build 130

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSGBRJ

Before: B19761653 After: B21011842 \*\*12,50,244,317\*\*

Routine Name: PSGOE7

Before: B30726260 After: B40214304 \*\*9,26,34,52,55,50,87,111,181,

254,267,260,288,281,317\*\*

Routine Name: PSGOE82

Before: B21878874 After: B33061347 \*\*2,35,50,67,58,81,127,168,181,

276,317\*\*

Routine Name: PSGOE92

Before: B30935948 After: B43137679 \*\*2,35,50,58,81,110,215,237,

276,316,317\*\*

Routine Name: PSGOEF1

Before: B28843982 After: B38004561 \*\*2,7,35,39,45,47,50,63,67,58,

95,110,186,181,267,315,317\*\*

Routine Name: PSGPEN

Before: B40801558 After: B57822787 \*\*30,37,50,58,115,110,127,129,

323,317\*\*

Routine Name: PSGPLR

Before: B39066813 After: B40061443 \*\*10,50,67,119,129,191,317\*\*

Routine Name: PSJ317P

Before: n/a After: B6017554 \*\*317\*\*

Routine Name: PSJHLU

Before: B45959307 After: B50964072 \*\*1,56,72,102,134,181,267,285,317\*\*

Routine Name: PSJLMPRU

Before: B15059824 After: B19004803 \*\*16,58,85,110,185,181,267,323,317\*\*

Routine Name: PSJLMUDE

Before: B66391198 After: B86619867 \*\*7,47,50,63,64,58,80,116,110,

111,164,175,201,181,254,267,

228,315,317\*\*

Routine Name: PSJO

Before: B28881243 After: B32312057 \*\*31,58,110,181,267,275,317\*\*

Routine Name: PSJO2

Before: B20134007 After: B21667076 \*\*58,317\*\*

Routine Name: PSJPAD50

Before: n/a After:B143814904 \*\*317\*\*

Routine Name: PSJPAD70

Before: n/a After:B193106268 \*\*317\*\*

Routine Name: PSJPAD7I

Before: n/a After: B91877682 \*\*317\*\*

Routine Name: PSJPAD7U

Before: n/a After:B183094975 \*\*317\*\*

Routine Name: PSJPADE

Before: n/a After: B89070355 \*\*317\*\*

Routine Name: PSJPADIT

Before: n/a After:B218833371 \*\*317\*\*

Routine Name: PSJPADPT

Before: n/a After: B74926353 \*\*317\*\*

Routine Name: PSJPADSI

Before: n/a After:B210554864 \*\*317\*\*

Routine Name: PSJPDAPP

Before: n/a After: B26391444 \*\*317\*\*

Routine Name: PSJPDCL

Before: n/a After: B59118380 \*\*317\*\*

Routine Name: PSJPDCLA

Before: n/a After:B123693086 \*\*317\*\*

Routine Name: PSJPDCLU

Before: n/a After:B182600427 \*\*317\*\*

Routine Name: PSJPDRIN

Before: n/a After:B220627483 \*\*317\*\*

Routine Name: PSJPDRIP

Before: n/a After: B92189032 \*\*317\*\*

Routine Name: PSJPDRTP

Before: n/a After:B164604296 \*\*317\*\*

Routine Name: PSJPDRTR

Before: n/a After:B204379013 \*\*317\*\*

Routine Name: PSJPDRU1

Before: n/a After:B196519581 \*\*317\*\*

Routine Name: PSJPDRUT

Before: n/a After:B233123274 \*\*317\*\*

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For ADT related HL7 messages please refer to the [Patient Information Management System (PIMS) Technical Manual](http://www.va.gov/vdl/application.asp?appid=55).

Refer to the following tables for more details on SCH schedule activity.

### SCH Schedule Activity Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCH\|759:169:20160808163051-0400\|\|\|S12\|\|\|\|\|\|\|\~\~~20160808163051-0400

| SEQ | Description/ Field Name | COMMENTS                                                          | Data Value              |
|---------|-----------------------------|-----------------------------------------------------------------------|-----------------------------|
| 1       | Placer Appointment ID       | PATIENT IEN:HOSPITAL LOCATION FILE \#44 IEN:APPOINTMENT DATE AND TIME | 759:169:20160808163051-0400 |
| 2       | Filler Appointment ID       |                                                                       |                             |
| 3       | Occurrence Number           |                                                                       |                             |
| 4       | Placer Group Number         |                                                                       | S12                         |
| 5       | Schedule ID                 |                                                                       |                             |
| 6       | Event Reason                |                                                                       |                             |
| 7       | Appointment Reason          |                                                                       |                             |
| 8       | Appointment Type            |                                                                       |                             |
| 9       | Appointment Duration        |                                                                       |                             |
| 10      | Appointment Duration Units  |                                                                       |                             |
| 11      | Appointment Timing Quantity |                                                                       | \~\~~20160808163051-0400    |

<span id="P146_HL7_ZZZ" class="anchor"></span>ZZZ Segment

ZZZ\|7E-WEST\|OPT CLINIC \|GENERAL MEDICINE\|Y\|N

| SEQ | Description/ Field Name    | Comments                                                                                                                 | Data Value       |
|---------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 1       | WARD SEND LOCATION             | PADE SEND LOCATION defined in PSJ PADE SERVER SETUP ( PADE SYSTEM SETUP File \#58.7) for the PADE Ward                       | 7E-WEST              |
| 2       | CLINIC SEND LOCATION           | PADE SEND LOCATION defined in PSJ PADE SERVER SETUP for the PADE Clinic                                                      | OPT CLINIC           |
| 3       | FACILITY TREATING SPECIALTY    | Admission facility treating specialty                                                                                        | GENERAL MEDICINE     |
| 4       | HAZARDOUS TO HANDLE INDICATOR  | HAZARDOUS TO HANDLE INDICATOR identifies the medication is Hazardous to Handle as identified in the PSNDF file (#50.68)      | Y/N (HL7 table 0136) |
| 5       | HAZARDOUS TO DISPOSE INDICATOR | HAZARDOUS TO DISPOSE INDICATOR identifies the medication is Hazardous to Dispose as identified in in the PSNDF file (#50.68) | Y/N (HL7 table 0136) |

## Modified and New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With patch <span id="Patch_399_Indication_Modified_new_routin" class="anchor"></span>PSJ\*5\*399, the following routines were modified to add a second line to support the Indication prompt:

- <u>PSGOD</u>
- <u>PSGOE4</u>
- <u>PSGOE41</u>
- <u>PSGOE42</u>
- <u>PSGOEE</u>
- <u>PSGOEE0</u>
- <u>PSGOEF1</u>
- <u>PSGOETO</u>
- <u>PSGON</u>
- <u>PSGOT</u>
- <u>PSGVW</u>
- <u>PSIVEDT</u>
- <u>PSIVEDT1</u>
- <u>PSIVINDL</u>
- <u>PSIVORAL</u>
- <u>PSIVORC2</u>
- <u>PSIVORE1</u>
- <u>PSIVORE2</u>
- <u>PSIVORFA</u>
- <u>PSIVORFB</u>
- <u>PSJCOM</u>
- <u>PSJHL3</u>
- <u>PSJHL4</u>
- <u>PSJHL4A</u>
- <u>PSJHL9</u>
- <u>PSJLIFN</u>
- <u>PSJLIVFD</u>
- <u>PSJLIVMD</u>
- <u>PSJLMGUD</u>
- <u>PSJLMUDE</u>
- <u>PSJOE</u>
- <u>PSJOEA1</u>
- <u>PSJOE1</u>
- <u>PSJORRE</u>
- <u>PSJORRE1</u>
- <u>PSJORRN</u>
- <u>PSJORRN1</u>
- <u>PSJORRO</u>
- <u>PSJPXRM1</u>

The following are the routines for PSJ\*5\*317:

- PSGOE7  
- PSGOE82 
- PSGOE92 
- PSGOEF1 
- PSGPLR  
- PSJ317P 
- PSJHLU  
- PSJLMPRU
- PSJLMUDE
- PSJO   
- PSJO2  
- PSJPAD50
- PSJPAD7I
- PSJPAD7U
- PSJPADE
- PSJPADIT
- PSJPADPT
- PSJPADSI
- PSJPDCL
- PSJPDCLA
- PSJPDCLU
- PSJPDRIN
- PSJPDRIP
- PSJPDRTP
- PSJPDRTR

## PADE Stock Requisition Order: OMS^O05

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PADE OMS – MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                                  | Seq | DT | Len | Opt | Rep | Tbl | Ex Val                 |
|-------------------------------------------|---------|--------|---------|---------|---------|---------|----------------------------|
|   Field Separator                         |   1 |   ST   |   1     |   R     |   False |         |   \|                       |
|   Encoding Characters                     |   2 |   ST   |   4     |   R     |   False |         |   ^~\\                     |
|   Sending Application                     |   3 |   HD   |   227   |   R     |   False |   0361  |                            |
|    namespace ID                           |   1     |   IS   |   20    |   RE    |         |   0300  |                            |
|   Sending Facility                        |   4 |   HD   |   227   |   R     |   False |   0362  |                            |
|    namespace ID                           |   1     |   IS   |   20    |   RE    |         |   0300  |                            |
|    universal ID                           |   2     |   ST   |   199   |   R     |         |         |   10.168.11.186:4000       |
|    universal ID type                      |   3     |   ID   |   6     |   R     |         |   0301  |   DNS                      |
|   Receiving Application                   |   5 |   HD   |   227   |   R     |   False |   0361  |                            |
|    namespace ID                           |   1     |   IS   |   20    |   RE    |         |   0300  |                            |
|   Receiving Facility                      |   6 |   HD   |   227   |   R     |   False |   0362  |                            |
|    namespace ID                           |   1     |   IS   |   20    |   RE    |         |   0300  |                            |
|    universal ID                           |   2     |   ST   |   199   |   R     |         |         |   FO-BIRM.MED.VA.GOV:6777  |
|    universal ID type                      |   3     |   ID   |   6     |   R     |         |   0301  |   DNS                      |
|   Date/Time Of Message                    |   7 |   TS   |   26    |   R     |   False |         |                            |
|    time                                   |   1     |   DTM  |   24    |   R     |         |         |   20040328134623.1234+0300 |
|   Security                                |   8     |   ST   |   40    |   NS    |   False |         |                            |
|   Message Type                            |   9     |   MSG  |   15    |   R     |   False |         |                            |
|    message code                           |   1     |   ID   |   3     |   R     |         |   0076  |   OMS                      |
|    trigger event                          |   2     |   ID   |   3     |   R     |         |   0003  |   O05                      |
|    message structure                      |   3     |   ID   |   7     |   R     |         |   0354  |   OMS_O05                  |
|   Message Control ID                      |   10    |   ST   |   20    |   R     |   False |         |   123456                   |
|   Processing ID                           |   11    |   PT   |   3     |   NS    |   False |         |                            |
|   Version ID                              |   12    |   VID  |   971   |   R     |   False |         |                            |
|    version ID                             |   1     |   ID   |   5     |   R     |         |   0104  |   2.5                      |
|   Sequence Number                         |   13    |   NM   |   15    |   NS    |   False |         |                            |
|   Continuation Pointer                    |   14    |   ST   |   180   |   NS    |   False |         |                            |
|   Accept Acknowledgment Type              |   15    |   ID   |   2     |   R     |   False |   0155  |   AL                       |
|   Application Acknowledgment Type         |   16    |   ID   |   2     |   R     |   False |   0155  |   NE                       |
|   Country Code                            |   17    |   ID   |   3     |   NS    |   False |   0399  |                            |
|   Character Set                           |   18    |   ID   |   16    |   NS    |   False |   0211  |                            |
|   Principal Language Of Message           |   19    |   CE   |   483   |   NS    |   False |         |                            |
|   Alternate Character Set Handling Scheme |   20    |   ID   |   20    |   NS    |   False |   0356  |                            |
|   Message Profile Identifier              |   21    |   EI   |   427   |   NS    |   False |         |                            |

### PADE OMS – PID Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                                              | Seq | DT | Len | Opt | Rep | Tbl | Ex Val                 |
|-------------------------------------------------------|---------|--------|---------|---------|---------|---------|----------------------------|
|   Set ID - PID                                        |   1     |   SI   |   4     |   R     |   False |         |   1                        |
|   Patient ID                                          |   2     |   CX   |   1672  |   NS    |   False |         |                            |
|   Patient Identifier List                             |   3     |   CX   |   250   |   R     |   True  |         |                            |
|    ID number                                          |   1     |   ST   |   15    |   R     |         |         |   123123                   |
|    check digit                                        |   2     |   ST   |   1     |   R     |         |         |   1                        |
|    check digit scheme                                 |   3     |   ID   |   3     |   R     |         |   0061  |   M10                      |
|   Alternate Patient ID - PID                          |   4     |   CX   |   1687  |   NS    |   False |         |                            |
|   Patient Name                                        |   5     |   XPN  |   294   |   R     |   True  |         |                            |
|    family name                                        |   1     |   FN   |   194   |   R     |         |         |                            |
|   �  surname                                          |   1     |   ST   |   50    |   R     |         |         |   Patientlastname          |
|    given name                                         |   2     |   ST   |   30    |   R     |         |         |   Patientfirstname         |
|    second and further given names or initials thereof |   3     |   ST   |   30    |   RE    |         |         |                            |
|    suffix (e.g., JR or III)                           |   4     |   ST   |   16    |   RE    |         |         |                            |
|   Mother_s Maiden Name                                |   6     |   XPN  |   1044  |   NS    |   False |         |                            |
|   Date/Time of Birth                                  |   7     |   TS   |   26    |   R     |   False |         |                            |
|    time                                               |   1     |   DTM  |   24    |   R     |         |         |   20040328134623.1234+0300 |
|    degree of precision                                |   2     |   ST   |   0     |   NS    |         |   0529  |                            |
|   Administrative Sex                                  |   8     |   IS   |   1     |   NS    |   False |   0001  |                            |
|   Patient Alias                                       |   9     |   XPN  |   1044  |   NS    |   False |         |                            |
|   Race                                                |   10    |   CE   |   483   |   NS    |   False |   0005  |                            |
|   Patient Address                                     |   11    |   XAD  |   578   |   NS    |   False |         |                            |
|   County Code                                         |   12    |   IS   |   4     |   NS    |   False |   0289  |                            |
|   Phone Number - Home                                 |   13    |   XTN  |   651   |   NS    |   False |         |                            |
|   Phone Number - Business                             |   14    |   XTN  |   651   |   NS    |   False |         |                            |
|   Primary Language                                    |   15    |   CE   |   483   |   NS    |   False |   0296  |                            |
|   Marital Status                                      |   16    |   CE   |   483   |   NS    |   False |   0002  |                            |
|   Religion                                            |   17    |   CE   |   483   |   NS    |   False |   0006  |                            |
|   Patient Account Number                              |   18    |   CX   |   1687  |   NS    |   False |         |                            |
|   SSN Number - Patient                                |   19    |   ST   |   16    |   NS    |   False |         |                            |
|   Driver's License Number - Patient                   |   20    |   DLN  |   66    |   NS    |   False |         |                            |
|   Mother's Identifier                                 |   21    |   CX   |   1687  |   NS    |   False |         |                            |
|   Ethnic Group                                        |   22    |   CE   |   483   |   NS    |   False |   0189  |                            |
|   Birth Place                                         |   23    |   ST   |   250   |   NS    |   False |         |                            |
|   Multiple Birth Indicator                            |   24    |   ID   |   1     |   NS    |   False |   0136  |                            |
|   Birth Order                                         |   25    |   NM   |   2     |   NS    |   False |         |                            |
|   Citizenship                                         |   26    |   CE   |   483   |   NS    |   False |   0171  |                            |
|   Veterans Military Status                            |   27    |   CE   |   483   |   NS    |   False |   0172  |                            |
|   Nationality                                         |   28    |   CE   |   483   |   NS    |   False |   0212  |                            |
|   Patient Death Date and Time                         |   29    |   TS   |   26    |   NS    |   False |         |                            |
|   Patient Death Indicator                             |   30    |   ID   |   1     |   NS    |   False |   0136  |                            |
|   Identity Unknown Indicator                          |   31    |   ID   |   1     |   NS    |   False |   0136  |                            |
|   Identity Reliability Code                           |   32    |   IS   |   20    |   NS    |   False |   0445  |                            |
|   Last Update Date/Time                               |   33    |   TS   |   26    |   NS    |   False |         |                            |
|   Last Update Facility                                |   34    |   HD   |   241   |   NS    |   False |         |                            |
|   Species Code                                        |   35    |   CE   |   483   |   NS    |   False |   0446  |                            |
|   Breed Code                                          |   36    |   CE   |   483   |   NS    |   False |   0447  |                            |
|   Strain                                              |   37    |   ST   |   80    |   NS    |   False |         |                            |
|   Production Class Code                               |   38    |   CE   |   483   |   NS    |   False |   0429  |                            |
|   Tribal Citizenship                                  |   39    |   CWE  |   705   |   NS    |   False |   0171  |                            |

PID.3 Patient identifier listDefinition: This field contains the list of identifiers (one or more) used by the healthcare facility to uniquely identify a patient (e.g., VistA internal id \[DFN\], Claim number, VHA MVI integration control number \[ICN\], social security number, unique individual identifier, etc.. The currently supported values are listed below.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Identifier</strong></th>
<th><strong>Assigning Authority</strong></th>
<th><strong>Identifier type</strong></th>
<th><p><strong>Assigning Location</strong></p>
<p><strong>unique station# id</strong></p></th>
<th><strong>Expiration date</strong></th>
<th><strong>Effective date</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National ICN <strong></strong></td>
<td>USVHA</td>
<td>NI</td>
<td>200M</td>
<td><p>If populated, the ICN ID State is considered Deactivated</p>
<p>If both Expiration Date and Effective date are not populated the ICN ID State is Temporary</p></td>
<td><p>If populated, the ID State of the ICN is Permanent (see note above)</p>
<p>If both Expiration Date and Effective date are not populated the ICN ID State is Temporary</p></td>
</tr>
<tr class="even">
<td>Local ICN</td>
<td>USVHA</td>
<td>NI</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>USSSA</td>
<td>SS</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VistA id (DFN)</td>
<td>USVHA</td>
<td>PI</td>
<td>unique station# id</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

PID.5 Patient NameDefinition: This field contains the names of the patient, the primary or legal name of the patient is reported first. Note that "last name prefix" is synonymous to "own family name prefix" of previous versions of HL7, as is "second and further given names or initials thereof" to "middle initial or name". Multiple given names and/or initials are separated by spaces.

PID.7 Patient NameDefinition: This field contains the patient's date and time of birth.

### PADE OMS – PV1 Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                    | Seq | DT | Len | Opt | Rep | Tbl | Ex Val  |
|-----------------------------|---------|--------|---------|---------|---------|---------|-------------|
|   Set ID - PV1              |   1     |   SI   |   4     |   NS    |   False |         |             |
|   Patient Class             |   2     |   IS   |   1     |   R     |   False |   0004  |   I         |
|   Assigned Patient Location |   3     |   PL   |   1220  |   R     |   False |         |             |
|    point of care            |   1     |   IS   |   20    |   RE    |         |   0302  |             |
|    room                     |   2     |   IS   |   20    |   RE    |         |   0303  |             |
|    bed                      |   3     |   IS   |   20    |   RE    |         |   0304  |             |
|    facility (HD)            |   4     |   HD   |   227   |   R     |         |         |             |
|   �  namespace ID           |   1     |   IS   |   20    |   RE    |         |   0300  |             |
|   �  universal ID           |   2     |   ST   |   199   |   C     |         |         |             |
|   �  universal ID type      |   3     |   ID   |   6     |   C     |         |   0301  |             |
|   Admission Type            |   4     |   IS   |   2     |   NS    |   False |   0007  |             |
|   Preadmit Number           |   5     |   CX   |   1687  |   NS    |   False |         |             |
|   Prior Patient Location    |   6     |   PL   |   1230  |   NS    |   False |         |             |
|   Attending Doctor          |   7     |   XCN  |   2718  |   NS    |   False |   0010  |             |
|   Referring Doctor          |   8     |   XCN  |   2718  |   NS    |   False |   0010  |             |
|   Consulting Doctor         |   9     |   XCN  |   2718  |   NS    |   False |   0010  |             |
|   Hospital Service          |   10    |   IS   |   3     |   NS    |   False |   0069  |             |
|   Temporary Location        |   11    |   PL   |   1230  |   NS    |   False |         |             |
|   Preadmit Test Indicator   |   12    |   IS   |   2     |   NS    |   False |   0087  |             |
|   Re-admission Indicator    |   13    |   IS   |   2     |   NS    |   False |   0092  |             |
|   Admit Source              |   14    |   IS   |   6     |   NS    |   False |   0023  |             |
|   Ambulatory Status         |   15    |   IS   |   2     |   NS    |   False |   0009  |             |
|   VIP Indicator             |   16    |   IS   |   2     |   NS    |   False |   0099  |             |
|   Admitting Doctor          |   17    |   XCN  |   2718  |   NS    |   False |   0010  |             |
|   Patient Type              |   18    |   IS   |   2     |   NS    |   False |   0018  |             |
|   Visit Number              |   19    |   CX   |   250   |   RE    |   False |         |             |
|    ID number                |   1     |   ST   |   15    |   R     |         |         |   987654321 |
|   Financial Class           |   20    |   FC   |   50    |   NS    |   False |   0064  |             |
|   Charge Price Indicator    |   21    |   IS   |   2     |   NS    |   False |   0032  |             |
|   Courtesy Code             |   22    |   IS   |   2     |   NS    |   False |   0045  |             |
|   Credit Rating             |   23    |   IS   |   2     |   NS    |   False |   0046  |             |
|   Contract Code             |   24    |   IS   |   2     |   NS    |   False |   0044  |             |
|   Contract Effective Date   |   25    |   DT   |   8     |   NS    |   False |         |             |
|   Contract Amount           |   26    |   NM   |   12    |   NS    |   False |         |             |
|   Contract Period           |   27    |   NM   |   3     |   NS    |   False |         |             |
|   Interest Code             |   28    |   IS   |   2     |   NS    |   False |   0073  |             |
|   Transfer to Bad Debt Code |   29    |   IS   |   4     |   NS    |   False |   0110  |             |
|   Transfer to Bad Debt Date |   30    |   DT   |   8     |   NS    |   False |         |             |
|   Bad Debt Agency Code      |   31    |   IS   |   10    |   NS    |   False |   0021  |             |
|   Bad Debt Transfer Amount  |   32    |   NM   |   12    |   NS    |   False |         |             |
|   Bad Debt Recovery Amount  |   33    |   NM   |   12    |   NS    |   False |         |             |
|   Delete Account Indicator  |   34    |   IS   |   1     |   NS    |   False |   0111  |             |
|   Delete Account Date       |   35    |   DT   |   8     |   NS    |   False |         |             |
|   Discharge Disposition     |   36    |   IS   |   3     |   NS    |   False |   0112  |             |
|   Discharged to Location    |   37    |   DLD  |   47    |   NS    |   False |   0113  |             |
|   Diet Type                 |   38    |   CE   |   483   |   NS    |   False |   0114  |             |
|   Servicing Facility        |   39    |   IS   |   2     |   NS    |   False |   0115  |             |
|   Bed Status                |   40    |   IS   |   1     |   NS    |   False |   0116  |             |
|   Account Status            |   41    |   IS   |   2     |   NS    |   False |   0117  |             |
|   Pending Location          |   42    |   PL   |   1230  |   NS    |   False |         |             |
|   Prior Temporary Location  |   43    |   PL   |   1230  |   NS    |   False |         |             |
|   Admit Date/Time           |   44    |   TS   |   26    |   NS    |   False |         |             |
|   Discharge Date/Time       |   45    |   TS   |   26    |   NS    |   False |         |             |
|   Current Patient Balance   |   46    |   NM   |   12    |   NS    |   False |         |             |
|   Total Charges             |   47    |   NM   |   12    |   NS    |   False |         |             |
|   Total Adjustments         |   48    |   NM   |   12    |   NS    |   False |         |             |
|   Total Payments            |   49    |   NM   |   12    |   NS    |   False |         |             |
|   Alternate Visit ID        |   50    |   CX   |   1687  |   NS    |   False |   0203  |             |
|   Visit Indicator           |   51    |   IS   |   1     |   NS    |   False |   0326  |             |
|   Other Healthcare Provider |   52    |   XCN  |   2718  |   NS    |   False |   0010  |             |

PV1.2 Patient ClassDefinition: This field is used to categorize patients Suggested values are listed below:

> Patient Class

| Value | Description |
|-----------|-----------------|
| E         | Emergency       |
| I         | Inpatient       |
| O         | Outpatient      |
| U         | Unknown         |

PV1.3 Assigned Patient LocationDefinition: For inpatients, this field contains the location of the patient in the medical center.

### PADE OMS – ORC Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                                      | Seq | DT | Len | Opt | Rep | Tbl | Ex Val            |
|-----------------------------------------------|---------|--------|---------|---------|---------|---------|-----------------------|
|   Order Control                               |   1     |   ID   |   2     |   R     |   False |   0119  |   NW                  |
|   Placer Order Number                         |   2     |   EI   |   424   |   RE    |   False |         |                       |
|    entity identifier                          |   1     |   ST   |   199   |   R     |         |         |   12345U              |
|   Filler Order Number                         |   3     |   EI   |   424   |   RE    |   False |         |                       |
|    entity identifier                          |   1     |   ST   |   199   |   R     |         |         |   777111              |
|   Placer Group Number                         |   4     |   EI   |   427   |   NS    |   False |         |                       |
|   Order Status                                |   5     |   ID   |   2     |   NS    |   False |   0038  |                       |
|   Response Flag                               |   6     |   ID   |   1     |   NS    |   False |   0121  |                       |
|   Quantity/Timing                             |   7     |   TQ   |   1788  |   NS    |   False |         |                       |
|   Parent                                      |   8     |   EIP  |   855   |   NS    |   False |         |                       |
|   Date/Time of Transaction                    |   9     |   TS   |   26    |   R     |   False |         |                       |
|    time                                       |   1     |   DTM  |   24    |   R     |         |         |   20040328134623.1234 |
|    degree of precision                        |   2     |   ST   |   0     |   NS    |         |   0529  |                       |
|   Entered By                                  |   10    |   XCN  |   2718  |   NS    |   False |         |                       |
|   Verified By                                 |   11    |   XCN  |   2718  |   NS    |   False |         |                       |
|   Ordering Provider                           |   12    |   XCN  |   2718  |   NS    |   False |         |                       |
|   Enterer's Location                          |   13    |   PL   |   1230  |   NS    |   False |         |                       |
|   Call Back Phone Number                      |   14    |   XTN  |   651   |   NS    |   False |         |                       |
|   Order Effective Date/Time                   |   15    |   TS   |   26    |   NS    |   False |         |                       |
|   Order Control Code Reason                   |   16    |   CE   |   483   |   NS    |   False |         |                       |
|   Entering Organization                       |   17    |   CE   |   483   |   NS    |   False |         |                       |
|   Entering Device                             |   18    |   CE   |   483   |   NS    |   False |         |                       |
|   Action By                                   |   19    |   XCN  |   2718  |   NS    |   False |         |                       |
|   Advanced Beneficiary Notice Code            |   20    |   CE   |   483   |   NS    |   False |   0339  |                       |
|   Ordering Facility Name                      |   21    |   XON  |   563   |   NS    |   False |         |                       |
|   Ordering Facility Address                   |   22    |   XAD  |   578   |   NS    |   False |         |                       |
|   Ordering Facility Phone Number              |   23    |   XTN  |   651   |   NS    |   False |         |                       |
|   Ordering Provider Address                   |   24    |   XAD  |   578   |   NS    |   False |         |                       |
|   Order Status Modifier                       |   25    |   CWE  |   705   |   NS    |   False |         |                       |
|   Advanced Beneficiary Notice Override Reason |   26    |   CWE  |   705   |   NS    |   False |   0552  |                       |
|   Filler's Expected Availability Date/Time    |   27    |   TS   |   26    |   NS    |   False |         |                       |
|   Confidentiality Code                        |   28    |   CWE  |   705   |   NS    |   False |   0177  |                       |
|   Order Type                                  |   29    |   CWE  |   705   |   NS    |   False |   0482  |                       |
|   Enterer Authorization Mode                  |   30    |   CNE  |   705   |   NS    |   False |   0483  |                       |

ORC.2 Placer Order NumberDefinition: This field contains the VistA pharmacy order number, as originally sent in the outbound PADE orders interface.

ORC.3 Filler Order NumberDefinition: This field contains an optional external order number.

### PADE OMS – RQD Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                      | Seq | DT | Len | Opt | Rep | Tbl | Ex Val    |
|-------------------------------|---------|--------|---------|---------|---------|---------|---------------|
|   Requisition Line Number     |   1     |   SI   |   4     |   NS    |   False |         |               |
|   Item Code - Internal        |   2     |   CE   |   478   |   R     |   False |         |               |
|    identifier                 |   1     |   ST   |   20    |   R     |         |         |   111999      |
|   Item Code - External        |   3     |   CE   |   478   |   R     |   False |         |               |
|    identifier                 |   1     |   ST   |   20    |   R     |         |         |   12345678    |
|    text                       |   2     |   ST   |   199   |   R     |         |         |   Haloperidol |
|   Hospital Item Code          |   4     |   CE   |   483   |   NS    |   False |         |               |
|   Requisition Quantity        |   5     |   NM   |   6     |   R     |   False |         |   2           |
|   Requisition Unit of Measure |   6     |   CE   |   478   |   R     |   False |         |               |
|    identifier                 |   1     |   ST   |   0     |   NS    |         |         |               |
|    text                       |   2     |   ST   |   199   |   R     |         |         |   Tablet      |
|   Dept. Cost Center           |   7     |   IS   |   30    |   NS    |   False |   0319  |               |
|   Item Natural Account Code   |   8     |   IS   |   30    |   NS    |   False |   0320  |               |
|   Deliver To ID               |   9     |   CE   |   483   |   NS    |   False |         |               |
|   Date Needed                 |   10    |   DT   |   8     |   NS    |   False |         |               |

RQD.2 Item Code - InternalDefinition: This field contains the VistA ID of the medication from the VistA Drug File (#50).

RQD.3 Item Code - ExternalDefinition: This field contains an external ID and text name of the drug in RQD.2. The External Item Code may be the same as the Internal Item Code.

PADE OMS – ZPM Segment

| Name                                              | Seq | DT | Len | Opt | Rep | Tbl | Ex Val     |
|-------------------------------------------------------|---------|--------|---------|---------|---------|---------|----------------|
|   Transaction Type                                    |   1     |   IS   |   35    |   R     |   False |   VA481 |   V            |
|   Dispensing System                                   |   2     |   ST   |   10    |   R     |   False |         |   PYX12        |
|   Device Name                                         |   3     |   ST   |   10    |   R     |   False |         |   PYX12        |
|   Drawer Number                                       |   4     |   ST   |   2     |   R     |   False |         |   10           |
|   Pocket Descriptor                                   |   5     |   ST   |   5     |   RE    |   False |         |   15B          |
|   Item ID                                             |   6     |   CE   |   107   |   R     |   False |         |                |
|    identifier                                         |   1     |   ST   |   15    |   R     |         |         |   12345        |
|    text                                               |   2     |   ST   |   30    |   R     |         |         |   ASPIRIN      |
|    name of coding system                              |   3     |   ST   |   5     |   RE    |         |         |   99PSD        |
|    alternate identifier                               |   4     |   ST   |   15    |   RE    |         |         |   98767        |
|    alternate text                                     |   5     |   ST   |   30    |   RE    |         |         |   ASPIRIN      |
|    name of alternate coding system                    |   6     |   ST   |   7     |   RE    |         |         |   99PSP        |
|   Item Class                                          |   7     |   ST   |   1     |   RE    |   False |         |   1            |
|   Expected Begin Count                                |   8     |   NM   |   8     |   RE    |   False |         |   20           |
|   Actual Begin Count                                  |   9     |   NM   |   8     |   R     |   False |         |   19           |
|   Transaction Amount                                  |   10    |   NM   |   8     |   R     |   False |         |   2            |
|   User ID                                             |   11    |   XCN  |   60    |   R     |   False |         |                |
|    ID number (ST)                                     |   1     |   ST   |   10    |   R     |         |         |   12345        |
|    family name                                        |   2     |   FN   |   24    |   R     |         |         |                |
|   �  surname                                          |   1     |   ST   |   22    |   R     |         |         |   LASTNAME     |
|    given name                                         |   3     |   ST   |   22    |   R     |         |         |   FIRSTNAME    |
|    second and further given names or initials thereof |   4     |   ST   |   1     |   RE    |         |         |                |
|   Witness ID                                          |   12    |   XCN  |   60    |   R     |   False |         |                |
|    ID number (ST)                                     |   1     |   ST   |   10    |   R     |         |         |   12345        |
|    family name                                        |   2     |   FN   |   24    |   R     |         |         |                |
|   �  surname                                          |   1     |   ST   |   24    |   R     |         |         |   LASTNAME     |
|    given name                                         |   3     |   ST   |   24    |   R     |         |         |   FIRSTNAME    |
|   Total Item Count                                    |   13    |   NM   |   8     |   RE    |   False |         |   20           |
|   Facility Code                                       |   14    |   XON  |   28    |   RE    |   False |         |                |
|    organization name                                  | 1       |   ST   |   15    |   RE    |         |         |   ALBANY       |
|    organization name type code                        | 2       |   IS   |   1     |   RE    |         |   0204  |   D            |
|    ID Number                                          | 3       |   NM   |   10    |   RE    |         |         |   500          |
|   Ward                                                | 15      |   CE   |   26    |   RE    |   False |         |                |
|    identifier                                         | 1       |   ST   |   10    |   RE    |         |         |   12345        |
|    text                                               | 2       |   ST   |   15    |   R     |         |         |   GENMED3E     |
|   Subdrawer                                           |   16    |   ST   |   2     |   RE    |   False |         |   A1           |
|   Pocket Capacity                                     |   17    |   NM   |   8     |   RE    |   False |         |   50           |
|   Pocket Reorder Level                                |   18    |   NM   |   8     |   RE    |   False |         |   25           |
|   Transaction Date/Time                               |   19    |   TS   |   12    |   R     |   False |         |                |
|    Transaction Date                                   |   1     |   ST   |   12    |   R     |         |         |   200506151336 |
|   Lot Number                                          |   20    |   ST   |   30    |   NS    |   False |         |   123456789A   |
|   Serial Number                                       |   21    |   ST   |   30    |   NS    |   False |         |   123456789    |

ZPM–1 Transaction Type—Defines the purpose of the message. Appropriate codes are:

Code Description

| B     | Number of items removed to empty a bin in the device              |
|-------|-------------------------------------------------------------------|
| C | Pocket inventory, a count of items stocked in device          |
| F     | Pocket refill, a count of items being resupplied to device        |
| L | Initial pocket load, a count of items being stocked in device |
| U | Pocket unload a count of items being removed from device      |
| R     | Return to bin, return to stock, return to pharmacy                |
| V | Dispense from station, issue to patient                       |
| W     | Waste from a station, waste from user                             |

ZPM–2 Dispensing System Name—This field is the configurable system name. Cabinets/Dispensing devices will only be unique per ZPM-2 System Name.

ZPM–3 Device name—Name of the dispensing device where the message originated.

ZPM–4 Drawer number—A location within the dispensing device where the item was stored.

ZPM–5 Pocket —The location within the drawer where the item was stored.

ZPM–6 Item ID—Unique code identifies the item contained in this message.

ZPM–7 Item class—A code describing the Medication class.

ZPM–8 Expected begin count — The number of items that are expected to be in the pocket at the start of the transaction.

ZPM–9 Actual begin count— The number of items found to be in the pocket at the start of the transaction.

ZPM–10 Transaction Amount— The item amount involved in the transaction.

ZPM–11 User ID—The system ID for the person performing the transaction.

ZPM–12 Witness ID—The system ID for the person witnessing the transaction.

ZPM–13 Total Item Count—The total amount of the item stored in the device, including when an item is stored in multiple drawers and/or pockets.

ZPM–14 Facility Code—Facility code identifier.

ZPM–15 Ward—For inpatients, the hospital location to which the patient is admitted.

ZPM–16 Subdrawer—A more specific storage location within the dispensing device.

ZPM–17 Pocket Capacity—The maximum amount of an item that may be stored in a pocket.

ZPM–18 Pocket Reorder Level—The amount of an item that generates a refill notice.

ZPM–19 Transaction Date/Time—The date and time the pocket activity occurred.

### PADE OMS – NTE Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name            | Seq | DT | Len | Opt | Rep | Tbl | Ex Val                                                                  |
|---------------------|---------|--------|---------|---------|---------|---------|-----------------------------------------------------------------------------|
|   Set ID - NTE      |   1     |   SI   |   4     |   R     |   False |         |   1                                                                         |
|   Source of Comment |   2     |   ID   |   8     |   NS    |   False |   0105  |                                                                             |
|   Comment           |   3     |   FT   |   65536 |   R     |   True  |         |   The drug was removed from the dispensing device and given to the patient. |
|   Comment Type      |   4     |   CE   |   483   |   NS    |   False |   0364  |                                                                             |

## Application Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA PADE Inventory Interface will send an ACK message in response messages it receives, if an application acknowledgement was requested in the original message. and will NACK (Negative ACKnowledgement) a message if there is an error in its format.

The VistA PADE Inventory interface will begin processing as soon as it has received a complete message, and will ACK a message as soon as it has processed all required segments of the message. Segments not used by VistA Inpatient Medications PADE interface will not be validated in any way.

It is recommended that PADE systems retransmit un-ACKed messages, as there is no guarantee without an ACK that a message has been received and processed. The VistA Inpatient Medications PADE interface will send an HL7 ACK message with acknowledgment code "AE" (error) in response to any messages containing unrecognized or out of sequence segments or where required data is missing.

| ACK | General Acknowledgment Message |
|---------|------------------------------------|
| MSH     | Message Header                     |
| MSA     | Message Acknowledgment             |

<u>  
</u><u>MSA Message Acknowledgement</u>

| Seq | Used | Len | Req/Opt | Tbl \# | Element Name         |
|---------|----------|---------|-------------|------------|--------------------------|
| 1\.     | Y        | 2       | R           | 0008       | Acknowledgement Code     |
| 2\.     | Y        | 20      | R           |            | Message Control ID       |
| 3\.     | Y        | 80      | O           |            | Text Message             |
| 4\.     | Y        | 15      | O           |            | Expected Sequence Number |
| 5\.     | N        | 1       | O           | 0102       | Delayed Acknowledgment   |
| 6\.     | Y        | 100     | O           |            | Error Condition          |

1\. ACKNOWLEDGEMENT CODE - Table 0008 (ACK Codes)

| Code | Used | Description |
|----------|----------|-----------------|
| AA   | Y    | Accept      |
| AE   | Y    | Error       |
| AR   | Y    | Reject      |

The VistA PADE Inventory interface will ACK each message received with one of the codes in table 0008, following the validation rules in the HL7 specification.

2\. MESSAGE CONTROL ID - This contains the Message Control ID from the message being acknowledged (field 10 of the MSH segment).

3\. TEXT MESSAGE – VistA PADE Inventory will not send a text message unless the ACK is a reject or error condition. When sending an "AE" or "AR" ACK message, VistA PADE Inventory may send a text message in this field if any further information is available.

4\. EXPECTED SEQUENCE NUMBER – VistA PADE Inventory places the sequence number it

expected to receive on the message being acknowledged in this field; under normal

circumstances, this should be the sequence number received.

5\. DELAYED ACK TYPE - Delayed ACKs are not supported by VistA PADE Inventory. This field will be ignored if present.