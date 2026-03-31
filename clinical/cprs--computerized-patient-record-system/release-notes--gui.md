---
consolidated_title: "cprs gui release notes"
app_code: CPRS
doc_type: RN
master_source: "OR*3*569 CPRS GUI Release Notes"
master_pub_date: September 2022
consolidated_from: 3 versions
prior_versions:
  - "OR*3*422 CPRS GUI Release Notes"
  - "OR*3*542 CPRS GUI Release Notes"
---

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
    - [New Features and Functions Added](#new-features-and-functions-added)
    - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
    - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
---
title: |
  <span id="_Toc205632711" class="anchor"></span>
  Anatomic Pathology Order Dialog
---
OR\*3.0\*569/LR\*5.2\*553
Release Notes
![](or-3-569-cprs-gui-release-notes/001.png)
September 2022
Artifact Rationale
Release Notes describe changes to existing software and new features and functions of a subsequent release of software, which makes them useful as a marketing tool.
For the initial distribution of software, Release Notes are optional. Revisions to a product that involve major changes to technical specifications or end-user functionality require Release Notes. Changes to software or documentation that have a minimal impact do not require Release Notes. The project manager, as the authoritative source and in consultation with the technical writer, determines if a Release Notes document is a required artifact for the project.
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is part of a multi-package build. The other patch is LR\*5.2\*553. These patches resolve some technical issues needed before anatomic pathology order dialogs can be enabled nationwide. It also adds an Update AP Order Dialogs option to the Order Menu Management menu.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purposes of these patches are to resolve some technical issues so that Anatomic Pathology (AP) order dialogs can be enabled nationwide. Once these patches are released, sites are approved to enable Anatomic Pathology ordering in CPRS.

When your site is ready to enable Anatomic Pathology ordering in CPRS, please follow the setup instructions in the 'OR\*3\*569 CPRS AP Order Dialog Setup and Configuration Guide that is being released with this patch.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of OR\*3.0\*569/LR\*5.2\*563 AP Ordering to the Order Menu Management and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for OR\*3.0\*569/LR\*5.2\*553 AP Order Dialogs.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the OR\*3.0\*569/LR\*5.2\*553 AP Order Dialogs release:

1.  Quick Orders can now be created for AP orders. At this time, this will only work for system quick orders, but a personal quick order can still not be created for AP.
2.  There was a GUI bug preventing making the Surgeon/Provider order prompt required (in the CPRS AP Dialog). This bug is being fixed in CPRS v32b. This patch creates a background task, that will update the Surgeon/Provider order prompt to be required (for the 13 pre-configured national AP order dialogs) once CPRS v32b (OR\*3.0\*405) is installed at the site.
3.  This patch creates a new file, AP DIALOG CONFIG (#101.45), to configure anatomic pathology order dialogs. This file is almost identical to the LR AP DIALOG CONFIG File (#69.73). File \#69.73 will not be used anymore and will be deleted in the bundled patch, LR\*5.2\*553. File \#101.45 will resolve the following issues that existed in file \#69.73:
    1.  Logically, this file should have existed in the ORDER ENTRY/RESULTS REPORTING (OR) namespace.
    2.  It was impossible for sites to change which entry in the ORDERABLE ITEMS File (#101.43) was associated with a specific test.
    3.  It was impossible to add new entries to the file without a patch.
    4.  It was difficult to create patches that sent changes to nationally distributed dialogs.
    5.  The UROLOGY,PROSTATE entry was missing configuration information needed before Operative Findings and Post-Operative Findings entered in CPRS would save with the order.
4.  A new option, Update AP Order Dialogs \[ORCM UPDATE AP DIALOGS\], is being added to the Order Menu Management \[ORCM MGMT\] menu. This option lets you copy, edit, or create new anatomic pathology order dialogs for use in CPRS.
5.  This patch updates which Laboratory Tests can be mapped to an AP Order Dialog. In order to be mapped to an AP Order Dialog, the test must:
1.  Have a SUBSCRIPT of SP, CY, or EM
2.  Be mapped to a NATIONAL VA LAB CODE
3.  Be mapped to a CPRS SCREEN

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Specimen Gets Deleted Until Another Key Is Selected</u>  
  If there is only one specimen on the AP Order Dialog, and the user deletes it, it will ask for confirmation that they want to delete the entry. If the user selects “yes,” the specimen is removed, however, if they click in any other boxes in the dialog, the specimen that was just deleted gets added back.
- <u>Specimen Bottles Getting Switched</u>  
  Staff report that from time to time, the specimen bottles will get changed. Specimen \#1 will become \#2 and vice versa. Staff requests to be able reorder the specimen by either dragging and dropping or having arrow keys to reorder them.
- <u>Auto-Populate the Specimen Number in the CPRS Order or in VistA</u>  
  Site requests to have the numbers in the specimen description box stored with the specimens that are entered. In the dialog, the numbers are there, but when the order is stored, there are no associated numbers. The current work around would be to educate the providers to enter the number of the specimen in the Specimen Description/Anatomic Site box.
- <u>Exception When Closing Parent Menu</u>  
  If the AP order dialog is opened, and then the CPRS order menu behind it is closed by clicking the done button, an error is generated.
- <u>When Logging in the Specimen, the Tech is No Longer Able to Put in the Gross Description  
  </u>When the Histology techs log in the specimen, they are no longer able to put in the gross description. They must go to another option to put it in.
- <u>Automatically Use the Abbreviation When the Text Gets Too Long</u>  
  > A request was made to automatically use the abbreviation when the text gets too long for the specimen.
- <u>Default Urgency in Quick Orders Do Not Work  
  </u>The default Urgency in Quick Orders do not work.
- <u>Quick Orders Need At least One, and Same Number of Collection Sample, Specimen, and Specimen Description  
  </u>Cannot create quick orders that do not have at least one predefined collection sample, specimen and specimen description, and you must have the same number of each one.
- <u>Changed, Copied, or Quick Orders Do Not Parse Specimen Description Text to Populate Special Fields  
  </u>When changing or copying an order, or creating an order from a quick order, the system is not parsing the specimen description text to populate the special fields.
- <u>Changes to the Specimen Descriptions Field Are Wiped Out When Any of the Special Fields Are Updated</u>  
  > Changes to the specimen descriptions field are wiped out when any of the special fields are updated. This includes any specimen description that pulls info from a changed or copied order, quick orders, as well as manual changes made to the description while working in the AP Dialog.
- <u>Cannot Create Auto-Accept Quick Orders</u>  
  The system does not allow users to create auto-accept AP quick orders.
- <u>Cannot Auto-Verify a Quick Order</u>  
  The system does not allow users to auto-verify an AP quick order.
- <u>Quick Order Default Comment is Word Processing Field and CPRS Dialog Are Single Line Edit</u>  
  > Quick order default comment is a Word Processing field and the field on the CPRS dialog are single line edit. This discrepancy needs to be resolved. If multiple lines entered in the quick-order they do carry over into the edit box, but they are displayed without carriage returns. In the final order the carriage returns come back.
- <u>Tab Order of “How Often” and “How Long” Fields Are Backwards</u>  
  The Tab order for the How Often” and “How Long” fields are backwards.
- <u>“How Long” Field Sometimes Incorrectly Enabled</u>  
  If the “How Often” order prompt is displayed, and defaults to a one-time frequency (such as ONCE), the “How Long” field is incorrectly enabled, but if you manually select ONCE, the field is correctly disabled. Default can be from the 101.45 file, a quick order, or from a changed or copied order.
- <u>Cannot Create Personal AP Dialog Quick Orders in CPRS</u>  
  The system does not allow users to create personal AP Dialog quick orders in CPRS.
- <u>Surgeon/Provider Required Error Message Says Surgeon/Physician</u>  
  If the Surgeon/Provider field is marked as required, and the user creating an AP order does not populate that field, an error message will display, notifying the user that they need to populate that field. However, the message says “Surgeon/Physician” instead of Surgeon/Provider.”
- <u>Required Collection Date/Time Not Enforced</u>  
  If the Collection Date/Time field is marked as required, the system is not enforcing it.
- <u>Update AP Order Dialogs Allows Entry of Invalid Defaults</u>  
  The Update AP Order Dialogs option allows entry of invalid defaults. For example, a user can enter urgencies that do not show up in the CPRS AP Dialog.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

<u>Documentation Title VDL File Name</u>

OR\*3\*569 CPRS AP Order Dialog Setup and or_3_0_569_setup.docx

Configuration Guide or_3_0_569_setup.pdf

OR\*3\*569 Release Notes CPRS GUI or_3_0_569_rn.docx

or_3_0_569_rn.pdf

CPRS User Manual: GUI Version (OR\*3.0\*569) cprsguium.docx

cprsguium.pdf

CPRS Technical Manual - GUI Version (OR\*3.0\*569) cprsguitm.docx

cprsguitm.pdf

CPRS Technical Manual: List Manager Version (OR\*3.0\*569) cprslmtm.docx

cprslmtm.pdf

Laboratory Anatomic Pathology Version 5.2 User Guide lab_ap_lr_5_2_ug.docx

lab_ap_lr_5_2_ug.pdf

Laboratory Version 5.2 Technical Manual lab5_2tm.docx

lab5_2tm.pdf

Laboratory Version 5.2 Planning and Implementation Guide lab5_2pi.docx

lab5_2pi.pdf

All AP dialog documents are available at the VA (Software) Documentation Library (VDL) website. This website is usually updated within 1-3 days of the patch release date.