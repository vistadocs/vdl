---
title: PSO*7*201 PFSS Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PFSS
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*201
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - pfss
  - charge
  - table
  - contents
  - billing
  - outpatient
  - cots
  - pharmacy
  - prescription
  - switch
page_count: 0
word_count: 1349
section_count: 9
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p201_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p201_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-201-pfss-release-notes/001.png)

Patient Financial Services System (PFSS) 1B Pilot

Outpatient Pharmacy (OP)

Release Notes

> PSO\*7\*201

September 2006

VistA Health Systems Design & Development

Table of Contents

*(This page intentionally left blank for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Software Interfaces](#software-interfaces)
  - [Overview of New Functionality](#overview-of-new-functionality)
- [Outpatient Pharmacy Enhancements](#outpatient-pharmacy-enhancements)
  - [PFSS Switch Status](#pfss-switch-status)
  - [PFSS Account Reference and Charge Identifier](#pfss-account-reference-and-charge-identifier)
  - [Messages to the COTS Billing System](#messages-to-the-cots-billing-system)
  - [Charge Location](#charge-location)
  - [Files and Fields](#files-and-fields)
  - [Changed Option](#changed-option)
This patch is part of the Patient Financial Services System (PFSS) project. PFSS patches are being released on various schedules. Some patch functionality will not be active until a new PFSS switch is activated during final implementation. PFSS will initially be implemented at select pilot sites ONLY.
The purpose of the PFSS project is to prepare the Veterans Health Information Systems and Technology Architecture (VistA) environment for the implementation of a commercial off-the-shelf (COTS) billing replacement system. The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system. Significant changes to VistA legacy systems and ancillary packages are necessary.
Some of the PFSS software components are not operational until the PFSS On/Off Switch, distributed with patch IB\*2\*260, is set to “ON”. The ability for the local site to set the switch to “ON” will be provided at the appropriate time with the release of a subsequent Integrated Billing (IB) patch.
For more information about the PFSS project, review the documentation accompanying this patch and refer to the following website: <http://vista.med.va.gov/billreplace/>.
These release notes present a brief description of the new features and functions of the Outpatient Pharmacy (OP) package provided in Patch PSO\*7\*201.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy will interface with the new COTS billing replacement system. These new interfaces are documented in the PFSS 1B Pilot <span class="mark">REDACTED</span> and Charge Messaging Interface Control Document (ICD).

The following applications must be running to support the new PFSS functionality:

|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
| Kernel                                       | 8.0                        |
| VA FileMan                                   | 22.0                       |
| MailMan                                      | 8.0                        |
| National Drug File (NDF)                     | 4.0                        |
| Pharmacy Data Management (PDM)               | 1.0                        |
| Outpatient Pharmacy (OP)                     | 7.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP) | 2.0                        |
| Controlled Substances (CS)                   | 3.0                        |
| Health Level 7 (HL7)                         | 2.4                        |
| Computerized Patient Record System (CPRS)    | 26.0                       |
| Integrated Billing (IB)                      | 2.0                        |
| VistA Data Extraction Framework (VDEF)       | 1.0                        |

> NOTE: The Clinical Indicator Data Capture (CIDC) patches PSO\*7\*143 and IB \*2\*260 are required and must be installed and operational.

Changes have been made to Outpatient Pharmacy to accommodate the inclusion of the COTS billing system Account Number and Charge Identifier. These changes are outlined in the <span class="mark">REDACTED</span>.

## Overview of New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality will ensure that all prescription fills (including refills but not partial fills) will have a check for activation of the COTS billing system (PFSS On/Off Switch).

If the switch is activated, the following functionality is operational:

- An account reference number upon finish and a unique charge identifier upon release.
- An interface to successfully communicate charge and credit information and updates to the COTS billing system.
- An associated charge code/service code and charge location for all prescription charges sent to the COTS billing system.

# Outpatient Pharmacy Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of Patch PSO\*7\*201 are grouped and discussed below. These changes provide a check for PFSS functionality, an account reference number and unique charge identifier, and a means of communicating information to the COTS billing system.

The following changes are implemented only when the PFSS Switch is set to ON, unless specifically noted otherwise.

## PFSS Switch Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy is modified to verify the status of the PFSS switch. If the PFSS switch is active (ON), prescription information will be passed to the new COTS billing system for copay determination and processing. If the PFSS switch is not activated (OFF), the current IB copay process will continue. In either scenario, the exchange of information will take place in the background with no user impact.

> NOTE: If the PFSS switch had previously been “ON” and a PFSS Account Reference is defined for the fill, the prescription information will be sent to the COTS billing system regardless of the status of the switch.

## PFSS Account Reference and Charge Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two unique identifiers have been added to the Outpatient Pharmacy prescription process:

1.  PFSS Account Reference
2.  Charge Identifier

In the current prescription order entry process, a new order is created by performing any of the following actions:

- Entering a new order
- Copying an existing prescription to a new order
- Renewing a prescription
- Editing a prescription (starred fields)

When a new order is <u>finished</u>, OP is modified to request a PFSS Account Reference from IBB (a subsystem of IB).

When a prescription is <u>released, including CMOP and Outpatient Automation Interface (OPAI) releases,</u> Outpatient Pharmacy is modified to request a unique Charge Identifier from IBB.

These two new identifiers will uniquely identify the prescription fill in the COTS billing system.

## Messages to the COTS Billing System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy is modified to send messages using the IB Application Programmer Interface (API) to the COTS billing system. These messages pass information on charges, charge updates, and charge credits.

> NOTE: IB will continue to be used for the initial copay eligibility assessment that is performed at finish. There are no changes to the Outpatient Pharmacy copay evaluation for Service Connection (SC), Environmental Indicators (EI), supply items and investigational drugs, income exemption, and RX (Pharmacy) Patient Status checks. The final copay billing determination, however, will be performed by the COTS billing system based on the Outpatient Pharmacy copay evaluation and current IB business rules.

Outpatient Pharmacy will send the following messages to the COTS billing system via IBB:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Message Function</th>
<th>Reason(s) for Sending</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Charge</td>
<td><ul>
<li><p>A prescription is released.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Charge Credit</td>
<td><ul>
<li><p>Return to stock, or a delete that performs a return to stock.</p></li>
<li><p>Copay charges cancelled on a released prescription by using the <em>Reset Copay Status/Cancel Charges</em> [PSOCP RESET COPAY STATUS] option.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Charge Update</td>
<td><ul>
<li><p>The patient’s SC and/or EI modified on a released prescription without cancelling copay by using the <em>Reset Copay Status/Cancel Charges</em> [PSOCP RESET COPAY STATUS] option.</p></li>
<li><p>The Days Supply edited on a released prescription.</p></li>
</ul>
<blockquote>
<p>NOTE: The COTS billing system will pick up the latest charge update.</p>
</blockquote>
<ul>
<li><p>The provider changed the SC/EI of a released prescription from the CPRS side.</p></li>
</ul></td>
</tr>
</tbody>
</table>

If there is a change in copay status, no charge message will be sent. The copay status change is flagged as effective for future fills.

## Charge Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy is modified to add a new Charge Location field. Upon installation of the patch, the user will need to define the location in the new CHARGE LOCATION field (#1007) in the OUTPATIENT SITE file (#59). This field is used to group charges in the COTS billing system according to the type of service.

> IMPORTANT: Entering and defining the Charge Locations is crucial to the success of this function. Initially, however, a unique Charge Location must be entered in the HOSPITAL LOCATION file (#44) by Registration or Scheduling. It is recommended that the Charge Location be coordinated with the Medical Center’s business office. A Charge Location should be defined for every division currently in the OUTPATIENT SITE file (#59), which means that there could be multiple hospital locations or one location for all divisions.

If a Charge Location is not defined for a particular division, Outpatient Pharmacy will search all active divisions in the OUTPATIENT SITE file (#59) for a Charge Location and use the first one it finds. If the PFSS switch is ON and no Charge Locations are defined in any divisions, the information will not be passed on to IB or the COTS billing system.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or updated files and fields in the Outpatient Pharmacy package.

#### OUTPATIENT SITE file (#59) Update

#### New Field

CHARGE LOCATION field (#1007)

#### PRESCRIPTION file (#52) Update

#### New Fields

PFSS ACCOUNT REFERENCE field (#125)

PFSS CHARGE ID field (#126)

In REFILL subfile (#52.1): PFSS ACCOUNT REFERENCE field (#21)

PFSS CHARGE ID field (#22)

#### Changed Fields

When PFSS functionality is activated, the following IB billing fields will no longer be populated:

- IB NUMBER field (#106)
- COPAY TYPE AUDIT field (#106.5)
- COPAY EXCEEDING CAP field (#106.6)
- In REFILL subfile (#52.1): IB NUMBER field (#9)

  COPAY EXCEEDING CAP field (#9.1)

## Changed Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option is modified to allow entry of the new CHARGE LOCATION field. Information in this field cannot be deleted, but it can be replaced by another Charge Location.