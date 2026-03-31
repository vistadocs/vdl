---
title: Kernel Toolkit 7.3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 7.3
patch_id: XU*7.3
group_key: "XU:XU:7.3"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Kernel Toolkit Version 7.3 Release Notes](#kernel-toolkit-version-73-release-notes) Decentralized Hospital Computer Program KERNEL TOOLKITRELEASE NOTES April 1995 Information Systems Center San Francisco
audience: 
keywords: 
  - toolkit
  - performance
  - kernel
  - monitor
  - release
  - look
  - version
  - notes
  - files
  - table
page_count: 0
word_count: 567
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/ktk_7_3rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/ktk_7_3rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

## Table of Contents

  - [Kernel Toolkit Version 7.3 Release Notes](#kernel-toolkit-version-73-release-notes)
Decentralized Hospital Computer Program
KERNEL TOOLKITRELEASE NOTES
April 1995
Information Systems Center
San Francisco

## Kernel Toolkit Version 7.3 Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Toolkit (also referred to as "Toolkit") is a robust set of tools developed to aid the Decentralized Hospital Computer Program (DHCP) development community and Information Resources Management (IRM) in writing, testing, and analysis of code. It is a set of generic tools that are useful to developers, site managers, documenters, and verifiers to support distinct tasks.

Many of these utilities have been used by the San Francisco Information Systems Center (ISC) for internal management and have proven valuable. Kernel Toolkit also includes tools provided by other ISCs based on their proven utility.

 <span class="smallcaps">New Features in Toolkit</span>

######## Multi-Term Look-Up

Multi-Term Look-Up (MTLU) is an adaptation of a tool developed by the Indian Health Service (IHS) which was made generic by the Albany ISC. Multi-Term Look-Up can be distinguished from a standard VA FileMan look-up by its ability to accept both terms and *phrases* from the user. This has been applied successfully to files such as the ICD DIAGNOSIS (#80) and ICD OPERATION/PROCEDURE (#80.1) files.

This Utility includes two security keys:

> 1\. XTLKZMGR

> 2\. XTLKZUSER

A series of new procedure calls have been added to Toolkit Version 7.3 allowing developers to non-interactively populate and manage MTLU, synonym, keyword, and shortcut files.

An enhanced Application Programmer Interface (API) for performing look-ups is now in the form of a single procedure call. Flags can be set to partially or fully eliminate screen writes and return data in an array.

######## VAX/Alpha Performance Monitor (VPM)

VPM has been significantly enhanced to provide performance assurance functions. This includes the ability to compute tolerance limits for system metrics, disk space and database consumption, and to enable alerts for critical events. New data elements have been added and reports have been enhanced. A computer-generated analysis of performance can now be run based on the site-specific tolerance limits.

A new routine, ^XUCMTM, is being shipped to assist sites with configuring TaskMan to run from a DCL Context.

The VPM Setup option now allows the site to configure data collections to be driven via node-specific batch queues rather than using the VMS SYSMAN utility.

A VAX/Alpha Performance Monitor pre-init synchronizes the ^XUCM( global with the file numbers, i.e., ^XUCM(1, becomes ^XUCM(8986.095,.

######## Bernstein Response Time Monitor

The Bernstein Response Time Monitor has not been updated for use on Alpha platforms and is not exported with this release. Sites are encouraged to request the monitor from their local ISC if they are still supporting a VAX.

######## MSM/486 Performance Monitor (MPM)

MSM systems can now begin automated performance monitoring using data from MSM RTHIST. RTHIST is started twice daily on all nodes and historical data is maintained in VA FileMan files. The package offers a variety of reports/graphs of historical performance data and a subset of the data is automatically sent to the Capacity Management Directorate at the San Francisco ISC for inclusion in a national performance database.

######## %INDEX

Two versions of %INDEX are supplied with this release. The XIND\* routines are supplied to provide support for the Type A extensions to the 1990 MUMPS Language Standard but are not connected to ^%INDEX by ^ZTMGRSET.