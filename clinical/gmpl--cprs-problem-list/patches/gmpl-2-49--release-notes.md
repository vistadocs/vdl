---
title: GMPL*2*49 and OR*3*429 Problem Selection List Enhancements Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: and OR*3*429 Problem Selection List Enhancements
app_code: GMPL
app_name: "CPRS: Problem List"
section: CLI
app_status: active
pkg_ns: GMPL
patch_ver: 2
patch_id: GMPL*2*49
group_key: "GMPL:GMPL:2"
file_numbers: []
security_keys: []
menu_options: 0
description: <span class="smallcaps">Problem Selection List Enhancements (Patches GMPL\2.0\49 and OR\3.0\429)</span><span class="smallcaps">Release Notes</span>
audience: 
keywords: 
  - span
  - selection
  - problem
  - class
  - gmpl
  - enhancements
  - patches
  - anchor
  - package
  - lists
page_count: 0
word_count: 517
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmpl_2_0_49_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmpl_2_0_49_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=64"
---

<span class="smallcaps">Problem Selection List Enhancements (Patches GMPL\*2.0\*49 and OR\*3.0\*429)</span><span class="smallcaps">Release Notes</span>

![](gmpl-2-49-and-or-3-429-problem-selection-list-enhancements-release-notes/001.png)

<span class="smallcaps">December 2017</span>

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

<span id="_Toc500191676" class="anchor"></span>Table of Contents

<span id="_Toc500191677" class="anchor"></span>Installation Requirements

<span id="_Toc500191678" class="anchor"></span>Required Patches

Below is a list of patches that you must verify are properly installed on your system before OR\*3.0\*434 can be installed:

- GMPL\*2.0\*40
- GMPL\*2.0\*45
- OR\*3.0\*385

Please see the *Problem Selection List Enhancements (Patches OR\*3.0\*429 and GMPL\*2.0\*49) Deployment, Installation, Back-Out, and Rollback Guide* for further instructions.

<span id="_Toc500191679" class="anchor"></span>Release Method

The Problem Selection List Enhancements will be released as part of a combined multi-package build under PROBLEM SELECTION LIST BUILD 1.0. This combined build consists of the GMPL\*2.0\*49 and OR\*3.0\*429 patches. The patches are expected to be installed on existing VistA platforms.

<span id="_Toc500191680" class="anchor"></span>Known Issue

There are no known issues with Problem Selection List Enhancements.

<span id="_Toc500191681" class="anchor"></span>New Features

Problem Selection List Enhancements include new features and changes include

- Problem Selectin List file structure
- A new parameter ORQQPL SELECTION LIST
- The migration of existing lists if they are actively assigned
- The installation of a new VA National Problem Selection List

  ![](gmpl-2-49-and-or-3-429-problem-selection-list-enhancements-release-notes/002.png)

> A CAC, or appropriate person, can assign a Problem Selection List that will display on the left of the Problems tab. If a list is assigned, there will be a listing of categories and when the category is selected, the pane below displays the problems it contains. This screen capture shows the VA-National Problem Selection List Content.

- A new key GMPL IMPRT UTIL that will enable the users to import problem selection lists
- updates to the Problem Selection List menu items
- additions and updates to menu actions that assist in the creation and maintenance of selection lists

For users that only use CPRS, the only change they may see would be in the problem selection list they are assigned.

Users who work on problem list creation and assignments will see new menu options, including the ability to import problem selection lists for those who have been assigned the GMPL IMPRT UTIL key.

<span id="_Toc500191682" class="anchor"></span>New Parameter

ORQQPL SELECTION LIST is a new parameter that will contain the problem selection list assignments. During the installation process, any existing problem selection lists that are actively assigned will be moved from where they are now stored to this new parameter.

When the patches are installed, the VA National Problem Selection List will be assigned at the Package level. Unless some other active assignment exists, all users and clinics will use the national list. If sites choose, they may make other assignments.

Assignments can be made at the following levels starting at the most general and going to the most specific: Package, System, Division, Location, and User. Package is only set by a nationally released patch. As with all parameters, the more specific level always takes priority over the more general assignment. So, if no other problem selection lists are assigned, all levels will inherit the Package level national list. However any assignment to a more specific level overrides the more general. So an assignment at Division or User overrides the Package level.