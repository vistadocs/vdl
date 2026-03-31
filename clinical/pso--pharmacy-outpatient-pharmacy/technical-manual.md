---
consolidated_title: "outpatient pharmacy technical manual security guide"
app_code: PSO
doc_type: TM
master_source: "Outpatient Pharmacy Version 7 Technical Manual Security Guide (PSO*7*766)"
master_pub_date: revision_count: 3
consolidated_from: 2 versions
prior_versions:
  - "Outpatient Pharmacy Version 7 Technical Manual Security Guide (PSO*7*774)"
---

# Outpatient Pharmacy (PSO) 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Outpatient Pharmacy (PSO)](#outpatient-pharmacy-pso)
- [Version 7.0](#version-70)
- [Technical Manual / Security Guide](#technical-manual-security-guide)
  - [Introduction](#introduction)
  - [Orientation](#orientation)
    - [Online Documentation](#online-documentation)
    - [Related Manuals](#related-manuals)
  - [Implementation and Maintenance](#implementation-and-maintenance)
    - [Resource Requirements](#resource-requirements)
    - [Options to be Deleted during Installation](#options-to-be-deleted-during-installation)
    - [Templates to be Deleted during Installation](#templates-to-be-deleted-during-installation)
    - [Routines to be Deleted during Installation](#routines-to-be-deleted-during-installation)
    - [M AudioCARE (Telephone Refill Requests)](#m-audiocare-telephone-refill-requests)
    - [Setting up the Bingo Board Device](#setting-up-the-bingo-board-device)
    - [Mail Group Setup for the HL7 External Interface](#mail-group-setup-for-the-hl7-external-interface)
    - [Using the Maintenance Menu](#using-the-maintenance-menu)
    - [Queue Background Jobs \[PSO AUTOQUEUE JOBS\]](#queue-background-jobs-pso-autoqueue-jobs)
  - [Files](#files)
    - [Outpatient Pharmacy Files](#outpatient-pharmacy-files)
    - [EPIP Outpatient Pharmacy Remediation, Patch PSO\7.0\452 Data Dictionary Update](#epip-outpatient-pharmacy-remediation-patch-pso70452-data-dictionary-update)
    - [Native Domain Standardization Medication Patch PSO\7\472, PSO\7\497, Data Dictionary Update](#native-domain-standardization-medication-patch-pso7472-pso7497-data-dictionary-update)
  - [Routine List](#routine-list)
  - [Exported Options](#exported-options)
    - [Menu Assignments](#menu-assignments)
    - [Security Keys](#security-keys)
    - [Package Security](#package-security)
  - [Archiving and Purging](#archiving-and-purging)
    - [Setting up the Archive Device](#setting-up-the-archive-device)
  - [Callable Routines](#callable-routines)
  - [External Interfaces](#external-interfaces)
    - [Steps for Startup / Shutdown of the External Interface](#steps-for-startup-shutdown-of-the-external-interface)
  - [External Relations](#external-relations)
    - [Data Base Integration Agreements (IAs)](#data-base-integration-agreements-ias)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
  - [Templates](#templates)
  - [Software Product Security](#software-product-security)
    - [Mail Group Setup for the HL7 External Interface](#mail-group-setup-for-the-hl7-external-interface-1)
    - [Archiving / Purging](#archiving-purging)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Menu Assignments](#menu-assignments-1)
    - [Security Keys](#security-keys-1)
    - [File Security](#file-security)
  - [Outpatient Pharmacy V. 7.0 Menu Diagrams](#outpatient-pharmacy-v-70-menu-diagrams)
    - [Outpatient Pharmacy Manager](#outpatient-pharmacy-manager)
    - [Pharmacist Menu](#pharmacist-menu)
    - [Pharmacy Technician’s Menu](#pharmacy-technicians-menu)
    - [Standalone Options](#standalone-options)
  - [Journaling Globals](#journaling-globals)
  - [Barcodes and Label Printer Support](#barcodes-and-label-printer-support)
    - [Barcodes on Dot Matrix Printers](#barcodes-on-dot-matrix-printers)
    - [New Label Stock (Version 6.0 and Later Versions) – Dot Matrix Labels](#new-label-stock-version-60-and-later-versions-dot-matrix-labels)
    - [Laser Label Printers](#laser-label-printers)
  - [Glossary](#glossary)
  - [Appendix A: Outpatient Pharmacy HL7 Interface Specifications](#appendix-a-outpatient-pharmacy-hl7-interface-specifications)
    - [A. General Information](#a-general-information)
    - [B. Transaction Specifications](#b-transaction-specifications)
  - [Appendix B: HL7 Messaging with an External System](#appendix-b-hl7-messaging-with-an-external-system)
    - [New Protocol](#new-protocol)
    - [New Application Parameter](#new-application-parameter)
    - [New Logical Link](#new-logical-link)
    - [HL7 Order Message Segment Definition Table](#hl7-order-message-segment-definition-table)
  - [Appendix C](#appendix-c)
  - [Appendix D: HL7 Messaging for VistA Data Extraction Framework (VDEF)](#appendix-d-hl7-messaging-for-vista-data-extraction-framework-vdef)
    - [New Protocols](#new-protocols)
    - [New Application Parameters](#new-application-parameters)
    - [New Logical Link](#new-logical-link-1)
    - [HL7 Outpatient Pharmacy VDEF Message](#hl7-outpatient-pharmacy-vdef-message)
    - [HL7 Outpatient Pharmacy VDEF Message](#hl7-outpatient-pharmacy-vdef-message-1)
  - [Appendix E: Outpatient Pharmacy ASAP Standard for Prescription Monitoring Programs (PMP)](#appendix-e-outpatient-pharmacy-asap-standard-for-prescription-monitoring-programs-pmp)
    - [Introduction](#introduction-1)
    - [Safety Updates for Medication Prescription Management (SUMPM) Patch \7\408 – State Prescription Drug Monitoring Program](#safety-updates-for-medication-prescription-management-sumpm-patch-7408-state-prescription-drug-monitoring-program)
    - [ASAP Segment Hierarchy Layout](#asap-segment-hierarchy-layout)
    - [SPMP Data Source (PSO\7\408)](#spmp-data-source-pso7408)
    - [SPMP Data Source (PSO\7\772)](#spmp-data-source-pso7772)
  - [Appendix F: OneVA Pharmacy HL7 Messaging using Middleware Application for External System](#appendix-f-oneva-pharmacy-hl7-messaging-using-middleware-application-for-external-system)
    - [OneVA Pharmacy General Information](#oneva-pharmacy-general-information)
    - [OneVA Pharmacy New Menu](#oneva-pharmacy-new-menu)
    - [OneVA Pharmacy New Logical Link](#oneva-pharmacy-new-logical-link)
    - [OneVA Pharmacy New Flag](#oneva-pharmacy-new-flag)
    - [OneVA Pharmacy Modified Protocols](#oneva-pharmacy-modified-protocols)
    - [OneVA Pharmacy New Protocols](#oneva-pharmacy-new-protocols)
    - [OneVA Pharmacy New Application Parameters](#oneva-pharmacy-new-application-parameters)
    - [New Fields on Existing Files](#new-fields-on-existing-files)
    - [OneVA Pharmacy New File](#oneva-pharmacy-new-file)
    - [OneVA Pharmacy Component Diagram](#oneva-pharmacy-component-diagram)
    - [OneVA Pharmacy HL7 Message Types](#oneva-pharmacy-hl7-message-types)
    - [OneVA Pharmacy Messaging Exceptions](#oneva-pharmacy-messaging-exceptions)
  - [Appendix G: Inbound ePrescribing (IEP)](#appendix-g-inbound-eprescribing-iep)
    - [Inbound ePrescribing Process Flow](#inbound-eprescribing-process-flow)
    - [Inbound ePrescribing Protocols](#inbound-eprescribing-protocols)
    - [Inbound ePrescribing Remote Procedures](#inbound-eprescribing-remote-procedures)
    - [Inbound ePrescribing Menu Option](#inbound-eprescribing-menu-option)
    - [Inbound ePrescribing Holding Queue File (File \#52.49)](#inbound-eprescribing-holding-queue-file-file-5249)
    - [Inbound ePrescribing External Patient File (File \#52.46)](#inbound-eprescribing-external-patient-file-file-5246)
    - [Inbound ePrescribing External Pharmacy File (#52.47)](#inbound-eprescribing-external-pharmacy-file-5247)
    - [Inbound ePrescribing External Person (File \#52.48)](#inbound-eprescribing-external-person-file-5248)
    - [Inbound ePrescribing External Person (File \#52.45)](#inbound-eprescribing-external-person-file-5245)
    - [Inbound ePrescribing New Field in Existing File](#inbound-eprescribing-new-field-in-existing-file)
  - [Appendix H: DEA# Migration Enhancements](#appendix-h-dea-migration-enhancements)
    - [General Information](#general-information)
    - [The Web Server](#the-web-server)
    - [Menu and Options](#menu-and-options)
    - [Print Audits for Prescriber Editing \[PSO EPCS PRINT EDIT AUDIT\]](#print-audits-for-prescriber-editing-pso-epcs-print-edit-audit)
    - [Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH Key Allocate/De-Allocate\]](#allocatede-allocate-of-psdrph-key-audited-pso-epcs-psdrph-key-allocatede-allocate)
    - [Remote Procedure](#remote-procedure)

# Version 7.0 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Technical Manual / Security Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/001.png)

December 1997  
(Revised August 2025)

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc207089076" class="anchor"></span>Table 1: Routines</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2025</td>
<td>PSO*7*766</td>
<td><ul>
<li><blockquote>
<p>Updated Section 5 – <a href="#routine-list">Routine List</a></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>08/2025</td>
<td>PSO*7*737</td>
<td><ul>
<li><blockquote>
<p>Updated Introduction with <a href="#PSO_7_737">PSO*7*737</a> patch description</p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#related-manuals">Section 2.2 Related Manuals</a></p>
</blockquote></li>
<li><blockquote>
<p>Added <a href="#PSOOCPGX">PSOOCPGX</a> to 5 – Routine List</p>
</blockquote></li>
<li><blockquote>
<p>Updated the <a href="#glossary">Glossary</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated Revision History and Footer</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>08/2025</td>
<td>PSO*7*774</td>
<td><ul>
<li><blockquote>
<p>Updated <a href="#introduction">Introduction</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#routine-list">Routine List</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#PSO_774_Note1">note</a> under <a href="#external-relations">External Relations</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#data-base-integration-agreements-ias">Data Base Integration Agreements (IAs)</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#oneva-pharmacy-general-information">OneVA Pharmacy General Information</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#oneva-pharmacy-new-menu">OneVA Pharmacy New Menu</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#oneva-pharmacy-new-flag">OneVA Pharmacy New Flag</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#new-fields-on-existing-files">New Fields on Existing Files</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#oneva-pharmacy-new-file">OneVA Pharmacy New File</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#oneva-pharmacy-hl7-message-types">OneVA Pharmacy HL7 Message Types</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#Table37">Table 37: Segment</a></p>
</blockquote></li>
<li><blockquote>
<p>Updated <a href="#Figure2">Figure 2: Example RTB^K13 Prescription Query Service Response</a></p>
</blockquote></li>
<li><blockquote>
<p>Added Note to <a href="#rdso13-pharmacytreatment-dispense-message-request">RDS^O13 Pharmacy/Treatment Dispense Message Request</a></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>07/2025</td>
<td>PSO*7*772</td>
<td><ul>
<li><blockquote>
<p>Added PSOASAP1 and PSOASAP2 to <a href="#routine-list">5 – Routine List</a></p>
</blockquote></li>
<li><blockquote>
<p>Added section <a href="#spmp-data-source-pso7772">23.5 SPMP Data Source (PSO*7*772)</a></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>07/2025</td>
<td>PSO*7*770</td>
<td><ul>
<li><p>Updated <a href="#routine-list">5 – Routine List</a></p></li>
<li><p>Updated <a href="#inbound-eprescribing-protocols">25.2 – Protocol List</a></p></li>
<li><p>Updated Data Dictionary <a href="#inbound-eprescribing-holding-queue-file-file-52.49">File #52.49</a>, <a href="#inbound-eprescribing-external-person-file-52.45">File #52.45</a></p></li>
<li><p>Updated <a href="#security-keys">6.2 – Security Keys</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2025</td>
<td>PSO*7*748</td>
<td>Updated Section <a href="#routine-list">5 – Routine List</a></td>
</tr>
<tr class="odd">
<td>09/2024</td>
<td>PSO*7*732</td>
<td>PSO EPCS PSDRPH FILER Remote Procedure added to <a href="#remote-procedure">section 26.5</a> in Appendix H</td>
</tr>
<tr class="even">
<td>07/2024</td>
<td>PSO*7*746</td>
<td><ul>
<li><p>Updated <a href="#routine-list">5 – Routine List</a></p></li>
<li><p>Updated <a href="#inbound-eprescribing-protocols">25.2 – Protocol List</a></p></li>
<li><p>Updated Data Dictionary <a href="#inbound-eprescribing-holding-queue-file-file-52.49">File #52.49</a>, <a href="#inbound-eprescribing-external-person-file-52.45">File #52.45</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>04/2024</td>
<td>PSO*7*736</td>
<td><p>OneVA Pharmacy migration from IBM WebSphere (VIERS) to VDIF</p>
<ul>
<li><p><a href="#introduction">Introduction</a></p></li>
<li><p>Updated <a href="#external-relations">External Relations</a></p></li>
<li><p>Updated <a href="#_Ref161303409">_Ref161303409</a> RDT and RDF data segments to change VA Product ID to VA Product IEN</p></li>
<li><p>Updated Figure 6 to replace VA Product ID with VA Product IEN in the 14<sup>th</sup> position</p></li>
<li><p>Updated <a href="#glossary">Glossary</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>12/2023</td>
<td>PSO*7*700</td>
<td><ul>
<li><p>Updated 5 – Routine List</p></li>
<li><p>Updated 6.2 – Security Keys (New key: PSO ERX WORKLOAD TECH)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>12/2023</td>
<td>PSO*7*731</td>
<td><ul>
<li><p>Removed instances of Detox number (#) in DEA Number Integrity Check [PSO EPCS DEA INTEGRITY REPORT]</p></li>
</ul></td>
</tr>
<tr class="even">
<td>06/2023</td>
<td>PSO*7*545</td>
<td><ul>
<li><p>Updated <a href="#routine-list">Routine List</a>: PSO7E545</p></li>
<li><p>Updated <a href="#standalone-options">Standalone Options</a></p></li>
<li><p>Updated <a href="#menu-and-options">Menu and Options</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>10/2022</td>
<td>PSO*7*701</td>
<td><ul>
<li><p>Updated Menu Text of option PSO EPCS PSDRPH KEY</p></li>
<li><p>26.3.6 Kernel Key Allocation to Honor Delegation</p></li>
<li><p>26.4 Orphan PSO EPCS PSDRPH Key Allocate/De-Allocate (Audited)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>9/2022</td>
<td>PSO*7*441</td>
<td><ul>
<li><p>Added new routines PSO441PI, PSOPRK, PSOPRKA, PSORPC01, PSORPTP</p></li>
<li><p>Added PSO PARK LIST and PSO PARK to the Templates section.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>08/2022</td>
<td>PSO*7*684</td>
<td><ul>
<li><p>Updated <a href="#routine-list">Routine List</a>: PSO7E684, PSO7P684</p></li>
<li><p>Updated <a href="#glossary">Glossary</a></p></li>
<li><p>Updated <a href="#_26_Appendix_H:">_Ref108689655</a></p></li>
<li><p>Merged Appendix I into <a href="#_26_Appendix_H:">_Ref108689655</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2022</td>
<td>PSO*7*667</td>
<td><ul>
<li><p>Updated <a href="#routine-list">Routine List</a>: PSODEARP, PSODEART, PSODEARU, PSOERXUT.</p></li>
<li><p>Added <a href="#standalone-options">Standalone Options</a>: [PSO EPCS UTILITY FUNCTIONS] and menu options: [PSO EPCS EXPIRE DATE REPORT], [PSO EPCS LOGICAL ACCESS REPORT], [PSO EPCS PHARMACIST ACC REPORT], [PSO EPCS ACCESS REPORTS], [PSO EPCS PSDRPH]</p></li>
<li><p>Added Appendix I: Pharmacy Operational Updates</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>04/2022</td>
<td>PSO*7*529</td>
<td><ul>
<li><p>Updated Routine List: PSO7L529, PSO7M529, PSODEAU0, PSODEAUT, PSOVEXRX.</p></li>
<li><p>Added Standalone Options: DEA Delete [PSO DEA DELETE], DEA Migration Report [PSO DEA MIGRATION REPORT].</p></li>
</ul></td>
</tr>
<tr class="even">
<td>12/2021</td>
<td>PSO*7*653</td>
<td><ul>
<li><p>Added new PHARMACY TELEPHONE REFILLS file (#52.444) to Outpatient Pharmacy file Table located in the Files section</p></li>
<li><p>Added new routines PSOVEXRX and PSOVEXR1 to Routine List section.</p></li>
<li><p>Updated the M AudioFax section with the new M AudioCARE option description.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/2021</td>
<td>PSO*7*561</td>
<td>Added new routines PSOBPSS2, PSOBPSU4, PSOSULB2</td>
</tr>
<tr class="even">
<td>07/2021</td>
<td>PSO*7*630</td>
<td><ul>
<li><p>Added new routine PSORXFIN to Routine List section</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>07/2021</td>
<td>PSO*7*524</td>
<td><ul>
<li><p>Updated Dispense Request with the new ZZZ segment for Hazardous Indicators (p. 62)</p></li>
<li><p>Updated Segments used in the Outpatient Pharmacy HL7 interface Dispense Request with the new ZZZ segment for Hazardous Indicators (p. 68)</p></li>
<li><p>Updated data elements for the Hazardous to Handle Indicator and the Hazardous to Dispose Indicator (p. 73)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2021</td>
<td>PSO*7*560</td>
<td><ul>
<li><p>Added new routine PSOREJP6.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>04/2021</td>
<td>PSO*7*635</td>
<td><ul>
<li><p>Updated for PSO*7.0*635 (pg2)</p></li>
<li><p>HPS Review. Updated file #52.45 to ERX SERVICE REASON CODES file (#52.45) (pg2), Updated Introduction with bullet list format (pg1)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>03/2021</td>
<td>PSO*7*635</td>
<td><ul>
<li><p>Update for Patch PSO*7.0*635. Updated Introduction (pg1), updated Related Manuals (pg4)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>03/2021</td>
<td>PSO*7*625</td>
<td><ul>
<li><p>Added new routines PSOSPML7, PSOSPML8, PSOSPMV to Routine List section.</p></li>
<li><p>Added three new menu options to the State Prescription Monitoring Program (SPMP) Menu:</p>
<ul>
<li><p>View/Export Void Prescriptions</p></li>
<li><p>Manual Export/Prescription Correction</p></li>
<li><p>CS Prescriptions Not Transmitted</p></li>
</ul></li>
<li><p>Added ASAP Zero Report Specifications to Appendix E</p></li>
</ul></td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>PSO*7*581</td>
<td><ul>
<li><p>Deleted PSO ERX VD SBN and PSO ERX HIDDEN #1 from Inbound ePrescribing protocols list. <a href="file:///C:/eRX/eRx_4.0/Documentation/Release_Management/Documents_for_Review/Baylis_Randall/pso_7_0_p581_TM_Draft_20201019.docx#pg149">(p.149)</a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>12/2020</td>
<td>PSO*7*581</td>
<td><ul>
<li><p>Updated Routine list:</p>
<ul>
<li><blockquote>
<p>P14: PSO581EN &amp; PSO581PO</p>
</blockquote></li>
<li><blockquote>
<p>P15: PSOERX1D, PSOERX1E, PSOERXA5, PSOERXA6, PSOERXC1, PSOERXEN, PSOERXI1, PSOERXIA, PSOERXIB, PSOERXIC, PSOERXID, PSOERXIE, PSOERXIF, PSOERXIG, PSOERXIH, PSOERXII, PSOERXIU, PSOERXOA, PSOERXOB, PSOERXOC, PSOERXOD, PSOERXOE, PSOERXOF, PSOERXOG, PSOERXOH, PSOERXOI, PSOERXOJ, PSOERXOK, PSOERXOL, PSOERXOM, PSOERXON, PSOERXOU, PSOERXU2, PSOERXU3, PSOERXU5, PSOERXU6, PSOERXU7, and PSOERXU8</p>
</blockquote></li>
</ul></li>
<li><p>Updated protocol name: PSO ERX CHANGE REQUEST, PSO ERX RX RENEWALREQUEST, PSO ERX SINGLE RXRENEWAL REQUEST (p.148)</p></li>
<li><p>Updated File #52.49 (p.150), File #52.46 (p.154), File #52.47 (p.155), File #52.48 (p.156)</p></li>
<li><p>Updated to Figure 5 (p.147)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>06/2020</td>
<td>PSO*7*612</td>
<td>Added routine PSOCLADD to Routine List (p. 14)</td>
</tr>
<tr class="odd">
<td>06/2020</td>
<td>PSO*7*546</td>
<td><ul>
<li><p>Added new routines PSOUTOR and PSOUTOR1.</p></li>
<li><p>Added the Medication Status Check supervisor function.</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
</tr>
<tr class="even">
<td>07/2019</td>
<td>PSO*7*528</td>
<td>Changed name of the TRICARE CHAMPVA Bypass/Override Report (pp. 20, 34, 39, 42).</td>
</tr>
<tr class="odd">
<td>03/2019</td>
<td>PSO*7*522</td>
<td>Updated Appendix A section B: Processing Rules - Deleted the text, "event type O01" and "event type O02"; and corrected the RDS message from "Pharmacy Encoded Order Message" to "Pharmacy Encoded Order/Treatment Dispense Message". Updated Appendix A section B:Transaction Specifications, subsection "Specific Transaction - Dispense Request" - corrected RDS-O01 references, the implemented message type is RDS-O13</td>
</tr>
<tr class="even">
<td>02/2019</td>
<td>PSO*7*481</td>
<td>Added the new menu option for PSO*7*481, Non-VA Provider Import, to the PSO Maintenance Menu which is under the Outpatient Pharmacy Manager. Added the new option Non-VA Provider Inactivate to Standalone Options. Routine List updated.</td>
</tr>
<tr class="odd">
<td>11/2018</td>
<td>PSO*7*452</td>
<td><p>Added a summary of Data Dictionary changes introduced by this patch.</p>
<p>Added routines PSODIR4, PSODEMSB, PSOEOPNW, and PSOSUCAT to the Routine List.</p>
<p>Added the PSO CLINICAL ALERT ENTER/EDIT template to the Templates section.</p></td>
</tr>
<tr class="even">
<td>11/2018</td>
<td>PS0*7*508</td>
<td>Added new Patch Details for Inbound ePrescribing (PSO*7.0*508) to Intro, pg1; Added PSO*7*508 documents to related manuals pg3; Updated Security Keys: PSO ERX ADV TECH, PSO ERX TECH, pg18 * PSDRPH, pg32a PSO ERX TECH, pg32b PSO ERX VIEW, pg32c; Appendix G. Updated IEP Protocols; Removed PSO*7.0*508 reference from Inbound ePrescribing Remote Procedures; Updated Fig 5. IEP Process Flow v3.0, pg146; Removed New and Modified labels from Inbound ePrescribing Protocols, p147 and Inbound ePrescribing, pg148: Holding Queue File (File #52.49), p149 ; External Patient File (File #52.46), p152a ; EXTERNAL PHARMACY FILE (#52.47), pg152b EXTERNAL PERSON (File #52.48), pg153a; SERVICE REASON CODES (File #52.45) lists, p153b; Updated Outpatient Pharmacy: PRESCRIPTION FILE (File #52), p153c; and OUTPATIENT SITE (File #59), pg154.</td>
</tr>
<tr class="odd">
<td>11/2018</td>
<td>PSO*7*517</td>
<td>Routine added PSO7P517 (p.13)</td>
</tr>
<tr class="even">
<td>08/2018</td>
<td>PSO*7*482</td>
<td>Added one routine (PSOPTC0) to list of routines (p. 13).</td>
</tr>
<tr class="odd">
<td>08/2018</td>
<td>PSO*7*505</td>
<td><p>Clinical Ancillary Services updates:</p>
<p><a href="#OLE_LINK3">Updates to ORC HL7 segment.</a></p>
<p><a href="#orc30">Added definition for ORC-30, Authorization mode.</a></p></td>
</tr>
<tr class="even">
<td>05/2018</td>
<td>PSO*7*463</td>
<td>Added technical components pertaining to the HAPE EDI Revenue Enhancements patch PSO*7*463 and updated the Routine List (PG. 13, 36)</td>
</tr>
<tr class="odd">
<td>04/2018</td>
<td>PSO*7*502</td>
<td><p>Updates for ScripTalk enhancement:</p>
<p>ScripTalk Printer</p>
<p>508 and OIT Compliance update throughout</p></td>
</tr>
<tr class="even">
<td>02/2018</td>
<td>PSO*7*500</td>
<td>Routine deleted: PSODGAL</td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td>PSO*7*402</td>
<td>Routines added: PSO7P402, PSODOSU4</td>
</tr>
<tr class="even">
<td>01/2018</td>
<td>PSO*7*497</td>
<td>Data Dictionary Updates, Index</td>
</tr>
<tr class="odd">
<td>12/2017</td>
<td>PSO*7*467</td>
<td>Adding PSO*7*467 information</td>
</tr>
<tr class="even">
<td>04/2017</td>
<td>PSO*7*472</td>
<td>Added New Patch Details for Native Domain Standardization Medication Patch PSO*7*472, Data Dictionary Update.</td>
</tr>
<tr class="odd">
<td>02/2017</td>
<td>PSO*7*465</td>
<td>Added the Confidential Address and revised the Temporary Address.</td>
</tr>
<tr class="even">
<td>12/2016</td>
<td>PSO*7*454</td>
<td>Added new OneVA Pharmacy routines; updated sections and added information about the new OneVA Pharmacy label; added Data Base Integration Agreement, added new External packages: eMI, HDR/CDS Repository; added Appendix for OneVA Pharmacy HL7-eMI-HDR/CDS Repository &amp; HL7-eMI-VistA messaging; updated Table of Contents to include changes; updated revision date for December 2016; Updated Index.</td>
</tr>
<tr class="odd">
<td>08/2016</td>
<td>PSO*7*451</td>
<td><p>Routines added: PSOASAP, PSOSPMA3, PSOSPMB3, PSOSPMKY, PSOSPMU0, PSOSPMU2, PSOSPMU3</p>
<p>Added PSO SPMP ADMIN Security Key entry.</p>
<p>Update the Outpatient Pharmacy Menu Diagrams</p></td>
</tr>
<tr class="even">
<td>06/2016</td>
<td>PSO*7*448</td>
<td><p>Updated Title Page to current OI&amp;T standards</p>
<p>Updated routine list; added the menu option Pharmacy Productivity/Revenue Report; added Electronic Claims Management Engine (ECME) to the External Relations table.</p></td>
</tr>
<tr class="odd">
<td>04/2016</td>
<td>PSO*7*411</td>
<td>Updated Routine List with routines PSOCROC, PSODGAL3, PSONEWOA, PSONEWOC, and PSOOCKV1.</td>
</tr>
<tr class="even">
<td>08/2014</td>
<td>PSO*7*408</td>
<td><p>Updated [PSO AUTOQUEUE JOBS] option</p>
<p>Files added to OP: (#58.4) SPMP ASAP RECORD DEFINITION, (#58.41) SPMP STATE PARAMETERS, (#58.42) SPMP EXPORT BATCH</p>
<p>Routines added: PSO408PI, PSOASAP0, PSORTSUT, PSOSPML0, PSOSPML1, PSOSPML2, PSOSPML3, PSOSPML4, PSOSPML5, PSOSPML6, PSOSPMSP, PSOSPMU1, PSOSPMUT</p>
<p>Added new Supervisor Functions menu option: State Prescription Monitoring Program Menu with option names</p>
<p>Updated the Glossary</p>
<p>Added Appendix E: Outpatient Pharmacy ASAP Standard for Prescription Monitoring Programs (PMP)</p>
<p>Updated Index</p></td>
</tr>
<tr class="odd">
<td>08/2014</td>
<td>PSO*7*313</td>
<td>Added new routine PSOOTMRX</td>
</tr>
<tr class="even">
<td>05/2014</td>
<td>PSO*7*423</td>
<td>Updated PID-11 documentation, updated RDX segment example, updated Expense Notes &amp; Dispensing Provider, updated RXD-9 documentation.</td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td><p>PSO*7*372</p>
<p>PSO*7*416</p></td>
<td><p>Renumber all pages</p>
<p>Updated Revision History and Table of Contents.</p>
<p>Added to the Related Manuals</p>
<p>Update Index</p></td>
</tr>
<tr class="even">
<td>01/2014</td>
<td>PSO*7*434</td>
<td><p>Two documentation updates:</p>
<p>The <em><u>active</u></em> Veteran’s Health Identity Card (VHIC) number was added to the PID segment (PID-4) on the VistA side.</p>
<p>Format:</p>
<p>[VIC Card #]~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;742V1&amp;L</p>
<p>The Outpatient Pharmacy Automation Interface (OPAI) has been changed to delimit the text on the pharmacy warning labels, correcting the problem in which text from one warning label runs into the text of another warning label.</p></td>
</tr>
<tr class="odd">
<td>11/2013</td>
<td>PSO*7*421</td>
<td><p>Changed graphic from VA Seal to VistA logo; changed layout for cover page.</p>
<p>Update other front matter including TOC, revision history, etc.</p>
<p>Update routine count. Add new routines: PSO7P421, PSOBPSSL</p>
<p>Add PSO EPHARMACY SITE MANAGER to security keys (added twice to document).</p></td>
</tr>
<tr class="even">
<td>05/2013</td>
<td>PSO*7*391</td>
<td><p>Added new routine PSOPKIV2 to the list of routines.</p>
<p>PSDRPH key added to Security key section.</p></td>
</tr>
<tr class="odd">
<td>01/2013</td>
<td>PSO*7*390</td>
<td><p>Update Revision History</p>
<p>Added option Automate Internet Refill that was missed in the manual for PSO*7*264</p>
<p>Add new routines: PSODGAL2, PSODDPR7, PSODDPR8</p>
<p>Add menu option; Check Drug Interaction<br />
Added BSA &amp; CrCL to the Glossary</p></td>
</tr>
<tr class="even">
<td>09/2012</td>
<td>PSO*7*386</td>
<td>Added description of patch’s new security key PSO TECH ADV and modifications to the HOLD/UNHOLD functionality.</td>
</tr>
<tr class="odd">
<td>03/2012</td>
<td>PSO*7*367</td>
<td><p>Added routine PSOFDAUT.</p>
<p>Updated NTE Segment listing.</p></td>
</tr>
<tr class="even">
<td>03/2012</td>
<td>PSO*7*354</td>
<td><p>Added new menu option Enter/Edit Automated Dispensing Devices</p>
<p>Updated list of files with file 52.53</p>
<p>Added file 52.53 to file security section</p>
<p>Added new menu option Enter/Edit Automated Dispensing Devices</p>
<p>Added RXD-13 Dispense-To location</p></td>
</tr>
<tr class="odd">
<td>02/2012</td>
<td>PSO*7*385</td>
<td><p>Removed "TRICARE" from file 52.87 name</p>
<p>Changed name of PSO TRICARE and PSO TRICARE MGR security keys to PSO TRICARE/CHAMPVA and PSO TRICARE/CHAMPVA MGR respectively.</p>
<p>Updated ePharmacy Menu with correct menu items</p>
<p>Added Advanced Beneficiary Notice Code for ePharmacy Rx in Appendix A references</p></td>
</tr>
<tr class="even">
<td>02/2012</td>
<td>PSO*7*354</td>
<td>Updated list of files with file 52.53</td>
</tr>
<tr class="odd">
<td>09/2011</td>
<td>PSO*7*382</td>
<td>Added routine PSOMPHRC.</td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>PSO*7*343</td>
<td>Added routine PSOFDAMG.</td>
</tr>
<tr class="odd">
<td>04/2011</td>
<td>PSO*7*316</td>
<td><p>Removed routine PSOQUAP.</p>
<p>Documentation released with PSO*7*343.</p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>PSO*7*251</td>
<td><p>Updated the Table of Contents.</p>
<p>Change the number of files from 24 to 26.</p>
<p>Added the following routines for PRE: PSO251PO, PSOCPPRE, PSODDPR1, PSODDPR2, PSODDPR3, PSODDPR4, PSODDPR5, PSODDPRE, PSODGAL1, PSODGDGP, PSODOSCL, PSODOSUN, PSODOSUT, PSOORROC, PSODOSU2, PSOVRPT.</p>
<p>Added information under Callable Routines section. And Removed links and added references under the External Interfaces.</p>
<p>Updated the External Relations table</p>
<p>Change the number of files from 24 to 26.</p>
<p>Changed menu item Process Drug/Drug Interactions to Process Order Checks.</p>
<p>Removed heading and information under Routine Mapping.</p></td>
</tr>
<tr class="odd">
<td>11/2010</td>
<td>PSO*7*358</td>
<td>Update routine list, security keys, file list, and options for the Bypass/Override functionality and added in the TRICARE Active Duty Release.</td>
</tr>
<tr class="even">
<td>06/2010</td>
<td>PSO*7*348</td>
<td>Added routines PSORLST &amp; PSORLST2; added options Prescription List for Drug Warnings and List of Patients/ Prescriptions for Recall Notice in Output Reports menu;</td>
</tr>
<tr class="odd">
<td>10/2009</td>
<td>PSO*7*326</td>
<td>Added routine PSOPATLK.</td>
</tr>
<tr class="even">
<td>08/2009</td>
<td>PSO*7*320</td>
<td>Added routines PSORMRX, PSORMRXD, and PSORMRXP.</td>
</tr>
<tr class="odd">
<td>08/2009</td>
<td>PSO*7*311</td>
<td>Deleted Pharmacy Patient Non-VA Meds Report/Clean-up menu.</td>
</tr>
<tr class="even">
<td>07/2009</td>
<td>PSO*7*289</td>
<td>Added files, routines, and the NDC Validation and ePharmacy Site Parameter options to the list.</td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td>PSO*7*305</td>
<td>Added routine PSOATRFC. Extended the PSOAUTRF security key description. Added the Privacy Notification element to the NTE segment.</td>
</tr>
<tr class="even">
<td>08/2008</td>
<td>PSO*7*225</td>
<td><p>The following changes are included in this patch.</p>
<p>New routines have been added: PSOCAN3N, PSOHLSN3, PSOORFI5, PSOORFI6, PSOORFL, PSOORRL3, PSOORRLN, and PSOORRLO. Special Escaping Characters information has been added.</p></td>
</tr>
<tr class="odd">
<td>07/2008</td>
<td>PSO*7*279</td>
<td>Update for the addition of the PSOAUTRF key.</td>
</tr>
<tr class="even">
<td>06/2008</td>
<td>PSO*7*288</td>
<td>Update for the new menu option [Pharmacy Patient Non-VA Meds Report/Clean-up].</td>
</tr>
<tr class="odd">
<td>05/2008</td>
<td>PSO*7*294</td>
<td>Update Routine List with routines PSOQ0076, PSOQ0186, PSOQ0236, PSOQ0496, PSOQ0595, PSOQCF04, PSOQMCAL, PSOQRART, PSOQTIU4, PSOQUAP, PSOQUAP2, and PSOQUTIL.</td>
</tr>
<tr class="even">
<td>10/2007</td>
<td>PSO*7*260</td>
<td>Updated Routine List with routines PSO260PI, PSOBPSR1, PSOBPSRP, PSOBPSU1, PSOBPSU2, PSONVAVW, PSOPMP0, PSOPMP1, PSOPMPPF, and PSOREJP3. Updated menu listing with new ePharmacy menu options.</td>
</tr>
<tr class="odd">
<td>10/2007</td>
<td>PSO*7*264</td>
<td><p>Re-numbered pages; removed section heading numbering.</p>
<p>Updated Routine List with routines: PSOATRD, PSOATRF, PSOATRF1, PSOATRP, PSOATRPP, PSOATRR, and PSORESUS. Updated menu listing with new option.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207089076" class="anchor"></span>Table 1: Routines

Table of Contents

List of Tables

List of Figures

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document briefly describes the technical and security aspects of Outpatient Pharmacy V.7.0. It is intended for members of the Automated Data Processing (ADP)/Information Resources Management Service (IRMS) staff who has had experience with other Veterans Health Information Systems and Technology Architecture (VistA) software and has worked or will work with a package coordinator who is familiar with the functions of the Outpatient Pharmacy V.7.0 in a VA Medical Center. Readers without this background are referred to the documentation for the Kernel, the VA FileMan and the User’s Manual for this release.

The Outpatient Pharmacy V.7.0 package provides a method for managing the medications given to veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital. Prescription labels are automatically generated, and refill request forms are printed. Medication histories are kept online to permit checks for potential interactions. Profiles can be generated to assist the clinician in managing the patient’s medication regimen. Management reports aid the pharmacy in controlling inventory and costs.

A number of site parameters allow the individual Department of Veterans Affairs Medical Center (VAMC) to customize the package to meet local needs. The User’s Manual describes these site parameters and the ways they influence the operation of the package.

Effective with the OneVA Pharmacy Patch PSO\*7.0\*454 (December 2016), Pharmacists are able to dispense prescriptions that originated in other VistA host sites. The OneVA Pharmacy User Manual and Installation Guide describe the site parameter required to use this functionality.

Effective with the Inbound ePrescribing Patch PSO\*7.0\*467 (December 13, 2017), pharmacists are able to receive and process prescriptions that originated from external providers. The Inbound ePrescribing User Manual, Installation Guide, and Implementation Guide describe the site parameters required to use this functionality.

Effective with the Inbound ePrescribing Patch PSO\*7.0\*508 (October 2018), pharmacists are able to receive and process prescriptions that originated from external providers. The Inbound ePrescribing User Manual, Installation Guide, and Implementation Guide describe the site parameters required to use this functionality.

Effective Inbound ePrescribing Patch PSO\*7.0\*581 (December 2020), pharmacists are able to receive and process incoming electronic prescription (eRX) sent from the IEP Processing Hub down to VistA and into the eRX Holding Queue.

Effective Inbound ePrescribing Patch PSO\*7.0\*635 (April 2021), Warranty defect remediation provides software fixes for:

- SIG text is supposed to be up to 1000 characters, Inbound eRx software assigns wrong unit of measure in RxRenewal Request, RxRenewal Request failing at hub because "IndicationForUse" segment is not sending in "Sig" segment
- Inbound eRx software assigns wrong unit of measure in RxRenewal Request
- RxRenewal Request failing at hub because "IndicationForUse" segment is not sending in "Sig" segment.
- NewRx coming in with ObservationDateTime, causing a failure at the eRx processing hub when generating an RxRenewal Request
- Updated Data Dictionary - ERX SERVICE REASON CODES file (#52.45), ACR codes in ERX SERVICE REASON CODES file (#52.45) have an extra space at the end
- ACR codes in ERX SERVICE REASON CODES file (#52.45) have an extra space at the end.
- VA 'Refills' displaying incorrectly for RxRenewal response replace response messages
- VA 'Refills' not displaying correct refills for Replace RxRenewal Response message, extend the logic from 365 days to 1 and half year for messages related to display at hub (Track/Audit page), a backlog of messages is queueing up and waiting for outbound delivery to CH during peak hours, reports page columns are missing in the last three reports
- NewRx counts not showing for summary new Rx Only and report totals at the bottom of the tables do not align with the correct column
- Reports - number of records not being displayed at the bottom of all reports and column width for Message Type in Track / Audit not wide enough
- When editing the Validate Drug / SIG for Replace RxRenewal Response, eRx refills are not decrementing correctly and incorrectly displays the \# of refills.

The OneVA Pharmacy patch PSO\*7\*736 (April 2024) replaces the query to the HDR/CDS repository with a query to the Veterans Data Information Exchange (VDIF). This patch also includes modifications to the "PROVIDER HOLD" status abbreviation from "PH" to "HP" and also adds "DISCONTINUED BY PROVIDER", "DISCONTINUED (EDIT)", and "NON-VERIFIED" statuses for display on the patient’s medication profile for remote prescriptions.

The OneVA Pharmacy Patch PSO\*7.0\*774 (September 2025) extends OneVA functionality to include Auto-Unpark and Auto-Release capabilities.

See External Relations Section of this manual for a listing of software not included in this package that must be installed before this version of Outpatient Pharmacy is fully functional.

<span id="PSO_7_737" class="anchor"></span>PSO\*7\*737, along with other related patches, adds Pharmacogenomic (PGx) order checking to medication orders entered through Inpatient Medications, Outpatient Pharmacy, and Computerized Patient Record System (CPRS). PSO\*7\*737 also creates a new Pharmacy option called ‘Check Pharmacogenomic Interaction Check’ (PSS CHECK PGX INTERACTION) that allows a user to enter drug(s), gene(s), phenotype(s), and genotype(s) and see the PGx order checks returned from the vendor for the data entered. This option also allows for patient selection and returns PGx order checks based on the patient’s Genomic lab data and current medication profile.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the entire Outpatient Pharmacy V. 7.0 package, enter a question mark (?) to obtain online information to assist in choosing actions at any prompt. Where examples of screen dialogs are given, user responses are shown as bolded text.

Additional information about this package is contained in help prompts and comments, which are available online. Detailed information can also be obtained by using the Kernel routine XINDEX to produce detailed listings of the routines and by using the VA FileMan to generate listings of data dictionaries for the files.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use VA FileMan *List File Attributes* \[DILIST\] option, under the *Data Dictionary Utilities* \[DI DDU\] option, to print the DDs.

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Outpatient Pharmacy V. 7.0 Release Notes*

> *Outpatient Pharmacy V. 7.0 User Manual*

> *Computerized Patient Record System V. 1.0 Installation Guide*

> *Computerized Patient Record System V. 1.0 Set-up Guide*

> *Pharmacy Ordering Enhancements (POE) Phase 2 Release Notes*

> *Outpatient Medication Copay Release Notes*

> *Laser Printed Prescription Labels with PMI Sheets Phase I Release Notes*

> *ScripTalk Talking Prescription Labels Installation Guide*

> *Herbal/OTC/Non-VA Meds Documentation Release Notes*

> *VistA Data Extraction Framework (VDEF) Installation & User Configuration Guide*

> *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual*

> *Dosing Order Check User Manual*

> *VistA to MOCHA Interface Document*

> *Installation Guide – OneVA Pharmacy*

> *Release Notes – OneVA Pharmacy*

> *User Manual – OneVA Pharmacy*

> *Release Notes – Inbound ePrescribing (PSO\*7\*467)*

> *Installation Guide – Inbound ePrescribing (PSO\*7\*467)*

> *User Manual – Inbound ePrescribing (PSO\*7\*467)*

> *Pharmacy Re-Engineering (PRE) Installation Guide – Inbound ePrescribing (PSO\*7\*508)*

> *Pharmacy Re-Engineering (PRE) Release Notes – Inbound ePrescribing (PSO\*7\*508)*

> *Pharmacy Re-Engineering (PRE) User Guide – Inbound ePrescribing (PSO\*7\*508)*

> *Technical Manual/Security Guide - Outpatient Pharmacy V.7.0'*

> *Pharmacy Re-Engineering (PRE) Installation Guide – Inbound ePrescribing (PSO\*7\*581)*

> *Pharmacy Re-Engineering (PRE) Release Notes – Inbound ePrescribing (PSO\*7\*581)*

> *Pharmacy Re-Engineering (PRE) User Guide – Inbound ePrescribing (PSO\*7\*581)*

> *Technical Manual/Security Guide - Outpatient Pharmacy V.7.0'*

> [*Pharmacy Re-Engineering (PRE) Installation Guide – Inbound ePrescribing (PSO\*7\*635)*](\l)

> [*Pharmacy Re-Engineering (PRE) Release Notes – Inbound ePrescribing (PSO\*7\*635)*](\l)

> [*Pharmacy Re-Engineering (PRE) User Guide – Inbound ePrescribing (PSO\*7\*635)*](\l)

> [*Technical Manual/Security Guide - Outpatient Pharmacy V.7.0'*](\l)

> *Pharmacy Outpatient Release Notes – (PSO\*7\*737)*

> *Pharmacy Outpatient Pharmacist’s User Guide V.7.0 - (PSO\*7\*737)*

> *Pharmacy Outpatient Manager’s User Guide V.7.0 – (PSO\*7\*737)*

> *Pharmacy Outpatient Technician’s User Guide V.7.0 - (PSO\*7\*737)*

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy V. 7.0 contains approximately 850 routines including all PSO\* routines and compiled templates, PSOX\* and APSPT\* that take up approximately 3.76MB disk space.

Response Time monitor hooks have been placed in the following routines:

| Routine | Purpose                                  |
|---------|------------------------------------------|
| PSON52  | File New Prescriptions in File (#52)     |
| PSORN52 | File Renewed Prescriptions in File (#52) |
| PSOR52  | File Refill Prescriptions in File (#52)  |

<span id="_Toc207089077" class="anchor"></span>Table 2: Disk Space

This package requires 28 files (see “Files” section in this manual). A typical site may require the following disk space:

| Space                          | Description                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| 1 Mbyte                        | DRUG file (#50) (4000 entries)                                                                                                |
| 3 Mbytes per month             | DRUG COST file (#50.9) (800 items dispensed by 200 dispensing physicians)                                                     |
| 150 Mbytes                     | PRESCRIPTION file (#52) (500,000 prescriptions)                                                                               |
| 50 Mbytes                      | PHARMACY PATIENT file (#55) (500,000 prescriptions)                                                                           |
| About 1 to 2 Mbytes            | Routines and the other files (except for RX VERIFY file (#52.4), RX SUSPENSE file (#52.5), and PHARMACY ARCHIVE file (#52.8)) |
| 3 to 5 Mbytes of “swing space” | RX VERIFY file (#52.4), RX SUSPENSE file (#52.5), and PHARMACY ARCHIVE file (#52.8)                                           |

<span id="_Toc207089078" class="anchor"></span>Table 3: Options to be Deleted during Installation

Outpatient Pharmacy V. 7.0 may be expected to require about 350 Mbytes of disk space. The actual disk utilization will, of course, depend primarily on the size of the three large files —PRESCRIPTION file (#52), PHARMACY PATIENT file (#55) and DRUG COST file (#50.9).

The requirements for Video Display Terminals (VDTs) and printers also depend on the number of transactions Outpatient Pharmacy V. 7.0 performs. Approximately three VDTs and one printer are needed for each 500 prescriptions (or fraction of 500) issued each day. If mail-out refills are handled separately, at least one VDT and one printer for each 500 refills are required. An additional VDT and a printer may be desired in the supervisor’s office, and 1 VDT in the office of people who are assigned to consult with patients about their medication regimens.

There are no special device requirements for dot matrix labels except to print barcodes on labels. In this case, the label printer must be able to print barcodes and must be able to be set to a form length of either 4 inches or 24 lines. The section in this document on barcodes provides additional information about this function.

Laser printed labels require one or more specially configured printers. The printer must be able to print to a legal length form and must print barcodes. In addition, the printer must support Hewlett Packard’s Printer Control Language (PCL) version 5 or greater.

1.  The OneVA Pharmacy Patch PSO\*7\*454 introduced the OneVA Pharmacy label-generation functionality with new/updated label routines. In order to print the OneVA Pharmacy label, each site must use a standard VistA laser label printer and label stock. The printer must be able to print a legal length form and must print barcodes. In addition, the printer must support Hewlett Packard’s Printer Control Language (PCL) version 5 or greater. For additional information related to the label stock go to the VA Software Document Library (VDL), select the Clinical section then choose the “Pharm: Outpatient Pharmacy” page. Locate the “User Manual – Supplemental – Outpatient Pharmacy” document and refer to the section titled “Laser Labels Phase II (PSO\*7\*161) and FY07 Q2 Release (PSO\*7\*200).”
2.  The barcode printed on the OneVA Pharmacy label will contain the host site information where the prescription order originated.

### Options to be Deleted during Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  The options listed below are deleted on the initial installation of Outpatient Pharmacy V. 7.0. No options are deleted after the initial installation, up to patch PSO\*7\*46.

| Option Name               | Menu Text                            |
|---------------------------|--------------------------------------|
| PSO DRUG                  | Drug Enter/Edit                      |
| PSO DRUGMENU              | Drug/Drug Interaction Functions      |
| PSO HOLDRX                | Hold Rx                              |
| PSO INTERACTION           | Drug Interactions Menu               |
| PSO INTERACTION LOCAL ADD | Enter/Edit Local Drug Interaction    |
| PSO INTERACTION SEVERITY  | Edit Drug Interaction Severity       |
| PSO LAB MONITOR           | Mark/Unmark Lab Monitor Drugs        |
| PSO NEW                   | New Prescription Entry               |
| PSO REF                   | Refill Prescriptions                 |
| PSO RXEDIT                | Edit Prescriptions                   |
| PSO RXHOLD                | Hold Features                        |
| PSO RXPAR                 | Partial Prescription                 |
| PSO SIGED                 | Medication Instruction File Add/Edit |
| PSO UNHOLDRX              | Unhold Rx                            |
| PSO FACILITY SETUP        | Enter Facility Data for Clozapine    |
| PSO MARK DRUG             | Mark Clozapine Drug                  |
| PSOL UNMARK DRUG          | Unmark Clozapine Drug                |
| PSOARCCO                  | Find                                 |
| PSOARCHLIST               | List One Patient’s Archived Rxs      |
| PSOARCIN                  | Tape Retrieval                       |
| PSOARCPURGE               | Purge                                |
| PSOARCSV                  | Save                                 |

<span id="_Toc207089079" class="anchor"></span>Table 4: Templates to be Deleted - Input

### Templates to be Deleted during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  The templates listed below are deleted on the initial installation of Outpatient Pharmacy V. 7.0. No options are deleted after the initial installation up to patch PSO\*7\*46.

| Input             | File |
|-------------------|------|
| PSO DRUG          | \#50 |
| PSO SIGED         | \#51 |
| PSO BATCH PARTIAL | \#52 |

<span id="_Toc207089080" class="anchor"></span>Table 5: Templates to be Deleted - Print

| Print                  | File |
|------------------------|------|
| PSO ACTION PROFILE \#3 | \#44 |
| PSOBJP                 | \#52 |

<span id="_Toc207089081" class="anchor"></span>Table 6: Templates to be Deleted - Dort

| Sort   | File |
|--------|------|
| PSOBJP | \#52 |

<span id="_Toc207089082" class="anchor"></span>Table 7: Routines to be Deleted

### Routines to be Deleted during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  The routines listed below are deleted on the initial installation of Outpatient Pharmacy V. 7.0. No options are deleted after the initial installation up to patch PSO\*7\*46.

| Routine  | Routine  | Routine  | Routine  | Routine  |
|----------|----------|----------|----------|----------|
| PSOCLDRG | PSOCLUS1 | PSOCLUS2 | PSOCLUS3 | PSOCSRL1 |
| PSOCSTAR | PSODRUG  | PSOGMINS | PSOGMP12 | PSOGMP25 |
| PSOLIST  | PSONODIB | PSONUM   | PSOPOST3 | PSOPRE   |
| PSORX    | PSORXPAR |          |          |          |

<span id="_Toc207089083" class="anchor"></span>Table 8: Files and Fields Associated

Prior to the initial installation of Outpatient Pharmacy V. 7.0, it is recommended that all PSO\* routines be deleted using the system utility to delete routines. Back up local modifications to any PSO\* routines.

After installation of Outpatient Pharmacy V. 7.0, compare routines to note the changes between locally modified routines and the V. 7.0 routines. Take care when installing local modifications as Outpatient Pharmacy V. 7.0 has been modified greatly with patch PSO\*7\*46.

### M AudioCARE (Telephone Refill Requests)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If telephone refill requests are processed using AudioCARE, the installation of PSO\*7\*653 patch will add the new class I *Process Telephone Refills* \[PSO PROCESS TELEPHONE REFILLS\] option and take out-of-order the class III *Process Telephone Refills* \[A3A PHONE REFILLS\] option. PSO\*7\*653 enhanced the Process Telephone Refills functionality by replacing the widely distributed class III VEXRX routine with the new class I PSOVEXRX routine suitable for national release. This modification enables enhancements and updates to the Telephone Refills system to be deployed across the enterprise using the National Patch Module.

<table>
<caption><p><span id="_Toc207089084" class="anchor"></span>Table 9: Waiver Permit</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/002.png)</th>
<th><p><strong>*Important*</strong></p>
<p>Telephone refill requests (M AudioCARE) cannot be processed without the new PSOVEXRX routine.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc207089084" class="anchor"></span>Table 9: Waiver Permit

### Setting up the Bingo Board Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A dedicated device must be set up for use with the bingo board. The device setup is similar to that used to set up a printer, except the sub-type will be C-VT. Only devices with the sub-type C-VT will be allowed for entry at the “DISPLAY DEVICE” prompt in the *Enter/Edit Display* \[PSO BINGO ENTER/EDIT DISPLAY\] option found on the *Bingo Board Manager* \[PSO BINGO MANAGER\] menu. For further information, see the site’s systems guide for information on setting up the device. Once a dedicated device is set up, the bingo board can be scheduled to automatically start, stop, or both at user-defined times.

### Mail Group Setup for the HL7 External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A mail group and device must be set up in order to run the HL7 external interface. The recommended name of the mail group is REDACTED. The recommended device name is REDACTED.

### Using the Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Maintenance (Outpatient Pharmacy)* \[PSO MAINTENANCE\] menu is used for implementation as well as maintenance of the Outpatient Pharmacy V. 7.0 package. The first five options, *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] (example follows)*, Edit Provider* \[PSO PROVIDER EDIT\], *AddNew Providers* \[PSO PROVIDER ADD\], *Queue Background Jobs* \[PSO AUTOQUEUE JOBS\], and *Autocancel Rx’s on Admission* \[PSO AUTOCANCEL1\] are used for implementation. The remaining options on this menu may be used for maintenance. (An example is given below for the *Queue Background Jobs* \[PSO AUTOQUEUE JOBS\] option. See the Outpatient Pharmacy V. 7.0 User Manual for an explanation of the other options on this menu.)

#### Maintenance (Outpatient Pharmacy) \[PSO MAINTENANCE\] Menu

> *Site Parameter Enter/Edit*

> *Edit Provider*

> *Add New Providers*

> *Queue Background Jobs*

> *Autocancel Rx’s on Admission*

> *Bingo Board Manager*

> *Edit Data for a Patient in the Clozapine Program*

> *Enter/Edit Clinic Sort Groups*

> *Initialize Rx Cost Statistics*

> *Edit Pharmacy Intervention*

> *Delete Intervention*

> *Auto-delete from Suspense*

> *Automate Internet Refill*

> *Delete a Prescription*

> *Enter/Edit Automated Dispensing Devices*

> *Expire Prescriptions*

> *Manual Auto Expire Rxs*

> *Non-VA Provider Import*

> *Prescription Cost Update*

> *Purge Drug Cost Data*

> *Purge External Batches*

> *Recompile AMIS Data*

### Queue Background Jobs \[PSO AUTOQUEUE JOBS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to queue all background jobs. Once the *Queue Background Jobs* \[PSO AUTOQUEUE JOBS\] option is selected, the option automatically pre-selects the jobs. Entering “E” for exit will not exit the option. An up arrow (^) must be entered to exit a specific job and go on to the next one. The background jobs are as follows:

- Autocancel Rx’s on Admission
- Nightly Rx Cost Compile
- Nightly Management Data Compile
- Compile AMIS Data (NIGHT JOB)
- Expire Prescriptions
- Auto-delete from Suspense
- Scheduled SPMP Data Export

A date and time at least 2 minutes in the future must be entered. The jobs should be set to run at a time convenient for the site.

6.  The options listed above must be scheduled to run through the *Queue Background Jobs* \[PSO AUTOQUEUE JOBS\] option. Attempting to run them from any other option will cause problems.

Only the following prompts require responses. All others will be left blank.

QUEUED TO RUN AT WHAT TIME: This is the date/time desired for TaskMan to start this option.

RESCHEDULING FREQUENCY: If this field is blank then the job will run only once.

The *Scheduled SPMP Data Export* \[PSO SPMP SCHEDULED EXPORT\] nightly background job option can also be scheduled via the *Schedule/Unschedule* \[XUTM SCHEDULE\] option.

7.  When the background job fails to transmit the data to the state, a MailMan message is generated and sent to the subscribers of the REDACTED mail group.

Example: View of Queue Background Jobs Screen

Select Maintenance (Outpatient Pharmacy) Option: QUEue Background Jobs

If time to run option is current do not edit.

Autocancel System Parameter must be set to 'YES'

before prescriptions are discontinued.

8.  The default values on the screen display below for TASK ID, QUEUED TO RUN AT WHAT TIME, DEVICE FOR QUEUED JOB OUTPUT, and RESCHEDULING FREQUENCY, not to indicate user input.

Edit Option Schedule

Option Name: PSO AUTOCANCEL

Menu Text: Autocancel on Admission TASK ID: 2617405

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUN 13,2000@01:00

DEVICE FOR QUEUED JOB OUTPUT: PP6;P-OTHER;132;64

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires the 28 files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use the VA FileMan *List File Attributes* \[DILIST\] option*,* under the Data Dictionary Utilities \[DI DDU\] option, to print the DDs. The following are the files for which DDs should be printed:

### Outpatient Pharmacy Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

-------------------------------------------------------------------------------

50.073 DUE QUESTIONNAIRE YES YES NO

50.0731 DUE ANSWER SHEET YES YES NO

50.0732 DUE QUESTION YES YES NO

50.0733 DUE SECTION YES YES NO

50.9 DRUG COST YES YES NO

52 PRESCRIPTION YES YES NO

52.09 REMOTE PRESCRIPTION LOG YES YES NO

52.11 PATIENT NOTIFICATION (Rx READY) YES YES NO

52.4 RX VERIFY YES YES NO

52.41 PENDING OUTPATIENT ORDERS YES YES NO

52.444 PHARMACY TELEPHONE REFILLS YES NO NO

52.43 PRESCRIPTION REFILL REQUEST YES YES NO

52.45 ERX SERVICE REASON CODES YES YES NO

52.46 ERX EXTERNAL PATIENT YES YES NO

52.47 ERX EXTERNAL PHARMACY YES YES NO

52.48 ERX EXTERNAL PERSON YES YES NO

52.49 ERX HOLDING QUEUE YES YES NO

52.5 RX SUSPENSE YES YES NO

52.51 PHARMACY EXTERNAL INTERFACE YES NO NO

52.52 CLOZAPINE PRESCRIPTION OVERRIDES YES YES NO

52.53 PHARMACY AUTOMATED DISPENSING DEVICES YES YES NO

52.8 PHARMACY ARCHIVE YES YES NO

52.86 EPHARMACY SITE PARAMETERS YES YES NO

52.87 PSO AUDIT LOG YES YES NO

52.9 PHARMACY PRINTED QUEUE YES YES NO

52.91 TPB ELIGIBILITY YES NO NO

52.92 TPB INSTITUTION LETTERS YES YES NO

53 RX PATIENT STATUS YES YES NO

58.4 SPMP ASAP RECORD DEFINITION

58.41 SPMP STATE PARAMETERS

58.42 SPMP EXPORT BATCH

59 OUTPATIENT SITE YES YES NO

59.1 OUTPATIENT AMIS DATA YES YES NO

59.12 OUTPATIENT PHARMACY MANAGEMENT DATA YES YES NO

59.2 WAITING TIME YES YES NO

59.3 GROUP DISPLAY YES NO NO

59.8 OUTPATIENT CLINIC SORT GROUP YES YES NO

### EPIP Outpatient Pharmacy Remediation, Patch PSO\*7.0\*452 Data Dictionary Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSO\*7.0\*452 enables a new warning message that is sent to members of the new PHARMACY SUPERVISORS MailMan group, notifying recipients that one or more Outpatient Pharmacy sites are approaching the upper limit of the defined prescription numbering series. The new warning is intended to prevent an unintentional shutdown of prescription processing that will occur if the pharmacy reaches the upper limit of the numbering series. For additional information about the early warning message, refer to the *Outpatient Pharmacy (PSO) Manager’s User Manual*.

This patch is delivered with companion patch PSS\*1.0\*215, which adds a new RX# UPPER BOUND WARNING LIMIT field (#48) to the PHARMACY SYSTEM file (#59.7). The value stored in this field determines when the early warning message is sent. If no custom value is entered in this field, then the message will be sent when 1000 numbers remain in the series. For more information about this Data Dictionary change, refer to the Pharmacy Data Management Technical Manual/Security Guide.

PSO\*7.0\*452 also adds a Clinical Alert that displays in the header area with patient demographic information when using certain Outpatient Pharmacy \[PSO\] options. Pharmacy Supervisors can use the Clinical Alert to make Pharmacy staff aware of information such as drug interactions or the patient’s participation in clinical trials. For more information about Clinical Alerts, refer to the Outpatient Pharmacy (PSO) Manager’s User Manual.

The companion patch PSS\*1.0\*215 adds a CLINICAL ALERT multiple field (#109) to the PHARMACY PATIENT file (#55). This field stores the date and time of the alert and provides a free-text field for the alert text. For more information about this Data Dictionary change, refer to the *Pharmacy Data Management Technical Manual/Security Guide*.

### Native Domain Standardization Medication Patch PSO\*7\*472, PSO\*7\*497, Data Dictionary Update 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Description

This patch will add a new field Coding System multiple to files DRUG INGREDIENTS (#50.416), VA GENERIC (#50.6), VA PRODUCT (#50.68), VA DRUG CLASS (#50.605) for the purpose of interoperability.

DRUG INGREDIENTS (#50.416) file shall be updated to include a new field multiple to store the RXNORM / UNII codes from the respective Standards Development Organizations.

VA GENERIC (#50.6) file shall be updated to include a new field multiple to store the RXNORM / UNII codes from the respective Standards Development Organizations.

VA PRODUCT (#50.68) file shall be updated to include a new field multiple to store the RXNORM code from the Standards Development Organization.

VA DRUG CLASS (#50.605) file shall be updated to include a new field multiple to store the RXNORM / UNII codes from the respective Standards Development Organizations.

#### Patch Components

| File Name (Number)       | Field Name (Number)  | New / Modified / Deleted |
|--------------------------|----------------------|--------------------------|
| DRUG INGREDIENTS (#50.6) | CODING SYSTEM (#5)\_ | Modified                 |
| VA PRODUCT (#50.68)      | CODING SYSTEM (#43)  | New                      |
| VA DRUG CLASS (#50.605)  | CODING SYSTEM (#5)   | New                      |

<span id="_Toc207089085" class="anchor"></span>Table 10: Supporting Documentation

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routine list for Outpatient Pharmacy appears when the new routine set is loaded. Each routine’s first line contains a brief description of the routine’s function. Use the First Line Routine Print \[XU FIRST LINE PRINT\] option to print a list of just the first line of each PSO\* routine.

- PSO5241
- PSO5252
- PSO525AP
- PSO5291
- PSO52AP1
- PSO52API
- PSO52B
- PSO52CLR
- PSO52EX
- PSO53
- PSO55FX2
- PSO55FX3
- PSO581EN
- PSO581PO
- PSO59
- PSO770PI
- PSO7L529
- PSO7L684
- PSO7M529
- PSO7P517
- PSO7P529
- PSO7P684
- PSOACR
- PSOADDR
- PSOAMIS
- PSOAMIS0
- PSOAMIS1
- PSOARC
- PSOARCCO
- PSOARCCV
- PSOARCDE
- PSOARCF1
- PSOARCF2
- PSOARCF3
- PSOARCF4
- PSOARCF5
- PSOARCF6
- PSOARCIN
- PSOARCLT
- PSOARCR1
- PSOARCR2
- PSOARCRR
- PSOARCS2
- PSOARCSV
- PSOARCTG
- PSOARCTP
- PSOARX
- PSOARX1
- PSOASAP
- PSOASAP0
- PSOASAP1
- PSOASAP2
- PSOATRD
- PSOATRF
- PSOATRF1
- PSOATRFC
- PSOATRP
- PSOATRPP
- PSOATRR
- PSOAUTOC
- PSOB
- PSOBAI
- PSOBAIR2
- PSOBAIRP
- PSOBARV
- PSOBBC
- PSOBGMG1
- PSOBGMG2
- PSOBGMG3
- PSOBGMGR
- PSOBING1
- PSOBINGO
- PSOBKDE1
- PSOBKDED
- PSOBMST
- PSOBORP0
- PSOBORP1
- PSOBORP2
- PSOBORP3
- PSOBPSR1
- PSOBPSRP
- PSOBPSS2
- PSOBPSSL
- PSOBPSSP
- PSOBPSU1
- PSOBPSU2
- PSOBPSU3
- PSOBPSU4
- PSOBPSUT
- PSOBRPRT
- PSOBSET
- PSOBSET1
- PSOBUILD
- PSOCAN
- PSOCAN1
- PSOCAN2
- PSOCAN3
- PSOCAN3N
- PSOCAN4
- PSOCIDC1
- PSOCIDC2
- PSOCIDC3
- PSOCIDC4
- PSOCIDC7
- PSOCIDC8
- PSOCIDC9
- PSOCLADD
- PSOCLEAN
- PSOCLERK
- PSOCLO1
- PSOCLOLS
- PSOCLUTL
- PSOCMOP
- PSOCMOPA
- PSOCMOPB
- PSOCMOPC
- PSOCMOPR
- PSOCMOPT
- PSOCOPAY
- PSOCOST
- PSOCOSTP
- PSOCP
- PSOCP1
- PSOCPA
- PSOCPB
- PSOCPBA2
- PSOCPBAK
- PSOCPBK1
- PSOCPBK2
- PSOCPBK3
- PSOCPBK4
- PSOCPBK5
- PSOCPC
- PSOCPD
- PSOCPDUP
- PSOCPE
- PSOCPF
- PSOCPF1
- PSOCPF2
- PSOCPIB
- PSOCPIB3
- PSOCPIB4
- PSOCPIB5
- PSOCPIBC
- PSOCPIBF
- PSOCPPRE
- PSOCPTRH
- PSOCPTRI
- PSOCPVW
- PSOCROC
- PSOCSRL
- PSOCST
- PSOCST10
- PSOCST11
- PSOCST12
- PSOCST2
- PSOCST3
- PSOCST4
- PSOCST5
- PSOCST6
- PSOCST7
- PSOCST8
- PSOCST9
- PSOCSTD
- PSOCSTM
- PSOCSTX
- PSODACT
- PSODAWUT
- PSODDPR1
- PSODDPR2
- PSODDPR3
- PSODDPR4
- PSODDPR5
- PSODDPR7
- PSODDPR8
- PSODDPRE
- PSODEA
- PSODEADD
- PSODEAED
- PSODEAMA
- PSODEAME
- PSODEARA
- PSODEARB
- PSODEARL
- PSODEARP
- PSODEARP
- PSODEART
- PSODEART
- PSODEARU
- PSODEARV
- PSODEARW
- PSODEARX
- PSODEAU0
- PSODEAU1
- PSODEAUJ
- PSODEAUT
- PSODEDT
- PSODELI
- PSODEM
- PSODEMSB
- PSODGAL1
- PSODGAL2
- PSODGAL3
- PSODGDG1
- PSODGDG2
- PSODGDGI
- PSODGDGP
- PSODI
- PSODIAG
- PSODIR
- PSODIR1
- PSODIR2
- PSODIR3
- PSODIR4
- PSODIR5
- PSODISP
- PSODISP1
- PSODISP2
- PSODISP3
- PSODISPS
- PSODIV
- PSODLKP
- PSODOSCL
- PSODOSU2
- PSODOSU4
- PSODOSUN
- PSODOSUT
- PSODP
- PSODPT
- PSODRDU1
- PSODRDU2
- PSODRDUP
- PSODRG
- PSODRGN
- PSODRGU0
- PSODSPL
- PSODSRC
- PSODUE
- PSOECMC2
- PSOECMP2
- PSOECMPS
- PSOELPS2
- PSOELPST
- PSOEN145
- PSOEOPNW
- PSOEPED
- PSOEPREP
- PSOEPRPT
- PSOEPU1
- PSOEPUT
- PSOEPUT2
- PSOEPVER
- PSOEPVR
- PSOERALL
- PSOERBT
- PSOERBT0
- PSOERBT1
- PSOERBT2
- PSOERCR0
- PSOERCR1
- PSOERHL0
- PSOERHL1
- PSOERPC0
- PSOERPC1
- PSOERPC2
- PSOERPC3
- PSOERPR0
- PSOERPR1
- PSOERPR2
- PSOERPT0
- PSOERPT1
- PSOERPT2
- PSOERPV1
- PSOERRX0
- PSOERRX1
- PSOERRX2
- PSOERSE1
- PSOERSE2
- PSOERSE3
- PSOERSE4
- PSOERSE5
- PSOERUT
- PSOERUT0
- PSOERUT1
- PSOERUT2
- PSOERUT3
- PSOERUT4
- PSOERUT5
- PSOERUT6
- PSOERUT7
- PSOERX
- PSOERX1
- PSOERX1A
- PSOERX1B
- PSOERX1C
- PSOERX1D
- PSOERX1E
- PSOERX1F
- PSOERX1G
- PSOERX1H
- PSOERX1I
- PSOERXA0
- PSOERXA1
- PSOERXA2
- PSOERXA3
- PSOERXA4
- PSOERXA5
- PSOERXA6
- PSOERXC1
- PSOERXD1
- PSOERXD2
- PSOERXD3
- PSOERXEN
- PSOERXH1
- PSOERXH2
- PSOERXI1
- PSOERXI2
- PSOERXIA
- PSOERXIB
- PSOERXIC
- PSOERXID
- PSOERXIE
- PSOERXIF
- PSOERXIG
- PSOERXIH
- PSOERXII
- PSOERXIU
- PSOERXO1
- PSOERXOA
- PSOERXOB
- PSOERXOC
- PSOERXOD
- PSOERXOE
- PSOERXOF
- PSOERXOG
- PSOERXOH
- PSOERXOI
- PSOERXOJ
- PSOERXOK
- PSOERXOL
- PSOERXOM
- PSOERXON
- PSOERXOU
- PSOERXP1
- PSOERXR1
- PSOERXU1
- PSOERXU2
- PSOERXU3
- PSOERXU4
- PSOERXU5
- PSOERXU6
- PSOERXU7
- PSOERXU8
- PSOERXU9
- PSOERXUT
- PSOERXUX
- PSOERXX1
- PSOERXX2
- PSOERXX3
- PSOERXX4
- PSOERXX5
- PSOEXBCH
- PSOEXDT
- PSOEXREF
- PSOEXRST
- PSOFDAMG
- PSOFDAUT
- PSOFSIG
- PSOFTDR
- PSOFUNC
- PSOHCPRS
- PSOHCSUM
- PSOHDR
- PSOHELP
- PSOHELP1
- PSOHELP2
- PSOHELP3
- PSOHELP4
- PSOHLD
- PSOHLDA
- PSOHLDC
- PSOHLDI1
- PSOHLDIS
- PSOHLDS
- PSOHLDS1
- PSOHLDS2
- PSOHLDS3
- PSOHLDS4
- PSOHLDS5
- PSOHLDS6
- PSOHLEXC
- PSOHLEXP
- PSOHLINC
- PSOHLINL
- PSOHLNE1
- PSOHLNE2
- PSOHLNE3
- PSOHLNE4
- PSOHLNEW
- PSOHLPII
- PSOHLPIS
- PSOHLSG
- PSOHLSG1
- PSOHLSG2
- PSOHLSG3
- PSOHLSG4
- PSOHLSG5
- PSOHLSIG
- PSOHLSIH
- PSOHLSN
- PSOHLSN1
- PSOHLSN2
- PSOHLSN3
- PSOHLSNC
- PSOHLUP
- PSOHLUP1
- PSOICDA
- PSOIOS
- PSOLAB
- PSOLBL
- PSOLBL1
- PSOLBL2
- PSOLBL3
- PSOLBL4
- PSOLBLD
- PSOLBLD1
- PSOLBLN
- PSOLBLN1
- PSOLBLN2
- PSOLBLS
- PSOLBLT
- PSOLLL1
- PSOLLL2
- PSOLLL3
- PSOLLL4
- PSOLLL5
- PSOLLL6
- PSOLLL7
- PSOLLL8
- PSOLLL9
- PSOLLLH
- PSOLLLHN
- PSOLLLI
- PSOLLLW
- PSOLLU1
- PSOLLU2
- PSOLLU3
- PSOLLU4
- PSOLMAL
- PSOLMAO
- PSOLMDA
- PSOLMLST
- PSOLMPAT
- PSOLMPF
- PSOLMPI
- PSOLMPO
- PSOLMPO1
- PSOLMPO2
- PSOLMRN
- PSOLMUTL
- PSOLSET
- PSOMAUEX
- PSOMGCM1
- PSOMGCOM
- PSOMGM31
- PSOMGMN1
- PSOMGMN2
- PSOMGMN3
- PSOMGMN4
- PSOMGMRP
- PSOMGR31
- PSOMGREP
- PSOMGRP1
- PSOMGRP2
- PSOMGRP3
- PSOMGRP4
- PSOMHV1
- PSOMLLD2
- PSOMLLDT
- PSOMPHRC
- PSON52
- PSONCPD1
- PSONCPD2
- PSONCPD3
- PSONCPDP
- PSONDCUT
- PSONDCV
- PSONEW
- PSONEW1
- PSONEW2
- PSONEW3
- PSONEWF
- PSONEWG
- PSONEWOA
- PSONEWOC
- PSONFI
- PSONGR
- PSONRXN
- PSONTEG
- PSONVAP2
- PSONVAP3
- PSONVAP4
- PSONVAR1
- PSONVARP
- PSONVAVW
- PSONVNEW
- PSOOCKV1
- <span id="PSOOCPGX" class="anchor"></span>PSOOCPGX
- PSOORAL
- PSOORAL1
- PSOORAL2
- PSOORAL3
- PSOORAPI
- PSOORCPY
- PSOORDA
- PSOORDER
- PSOORDRG
- PSOORED1
- PSOORED2
- PSOORED3
- PSOORED4
- PSOORED5
- PSOORED6
- PSOORED7
- PSOOREDT
- PSOOREDX
- PSOORFI1
- PSOORFI2
- PSOORFI3
- PSOORFI4
- PSOORFI5
- PSOORFI6
- PSOORFIN
- PSOORFL
- PSOORNE1
- PSOORNE2
- PSOORNE3
- PSOORNE4
- PSOORNE5
- PSOORNE6
- PSOORNEW
- PSOORNW1
- PSOORNW2
- PSOORRD2
- PSOORRDI
- PSOORRL
- PSOORRL1
- PSOORRL3
- PSOORRLN
- PSOORRLO
- PSOORRNW
- PSOORROC
- PSOORUT1
- PSOORUT2
- PSOORUT3
- PSOORUTL
- PSOOTMRX
- PSOP
- PSOP1
- PSOP2
- PSOP288F
- PSOP288R
- PSOPAT
- PSOPATLK
- PSOPFSU0
- PSOPFSU1
- PSOPI136
- PSOPKIV1
- PSOPKIV2
- PSOPMP0
- PSOPMP1
- PSOPMPPF
- PSOPOLY
- PSOPOS10
- PSOPOS12
- PSOPOS13
- PSOPOST
- PSOPOST1
- PSOPOST2
- PSOPOST3
- PSOPOST4
- PSOPOST5
- PSOPOST6
- PSOPOST7
- PSOPOST8
- PSOPOST9
- PSOPRA
- PSOPRF
- PSOPRFSS
- PSOPRI
- PSOPRK
- PSOPRKA
- PSOPROD1
- PSOPROD2
- PSOPRVW
- PSOPRVW1
- PSOPST68
- PSOPTC0
- PSOPTPST
- PSOPXRM1
- PSOPXRMI
- PSOPXRMU
- PSOQ0076
- PSOQ0186
- PSOQ0236
- PSOQ0496
- PSOQ0595
- PSOQCF04
- PSOQMCAL
- PSOQRART
- PSOQTIU4
- PSOQUAP2
- PSOQUTIL
- PSOR52
- PSORDS
- PSOREF
- PSOREF0
- PSOREF1
- PSOREF2
- PSOREJP0
- PSOREJP1
- PSOREJP2
- PSOREJP3
- PSOREJP4
- PSOREJP5
- PSOREJP6
- PSOREJP7
- PSOREJU1
- PSOREJU2
- PSOREJU3
- PSOREJU4
- PSOREJUT
- PSORELD1
- PSORELDT
- PSORENW
- PSORENW0
- PSORENW1
- PSORENW2
- PSORENW3
- PSORENW4
- PSORESK
- PSORESK1
- PSORESUS
- PSORFL
- PSORLLL1
- PSORLLL2
- PSORLLL3
- PSORLLL4
- PSORLLL5
- PSORLLLH
- PSORLLLI
- PSORLST
- PSORLST2
- PSORMRX
- PSORMRXD
- PSORMRXP
- PSORN52
- PSORN52A
- PSORN52C
- PSORN52D
- PSOROS
- PSORPC01
- PSORPTP
- PSORPTS
- PSORPTS1
- PSORRD
- PSORREF
- PSORREF0
- PSORREF1
- PSORRP
- PSORRPA1
- PSORRX1
- PSORRX2
- PSORTSUT
- PSORWRAP
- PSORX1
- PSORXCLE
- PSORXDL
- PSORXED
- PSORXED1
- PSORXEDT
- PSORXFIN
- PSORXI
- PSORXL
- PSORXL1
- PSORXLAB
- PSORXPA1
- PSORXPR
- PSORXPR1
- PSORXRP1
- PSORXRP2
- PSORXRPT
- PSORXVW
- PSORXVW1
- PSORXVW2
- PSOSD
- PSOSD0
- PSOSD1
- PSOSD2
- PSOSD3
- PSOSDP
- PSOSDRAP
- PSOSIG
- PSOSIGCX
- PSOSIGDS
- PSOSIGMX
- PSOSIGNO
- PSOSIGTX
- PSOSITED
- PSOSPMA3
- PSOSPMB3
- PSOSPMKY
- PSOSPML0
- PSOSPML1
- PSOSPML2
- PSOSPML3
- PSOSPML4
- PSOSPML5
- PSOSPML6
- PSOSPML7
- PSOSPML8
- PSOSPMSP
- PSOSPMU0
- PSOSPMU1
- PSOSPMU2
- PSOSPMU3
- PSOSPMUT
- PSOSPMV
- PSOSPSIG
- PSOSUBCH
- PSOSUCAT
- PSOSUCH1
- PSOSUCHG
- PSOSUCLE
- PSOSUDCN
- PSOSUDEL
- PSOSUDP1
- PSOSUDP2
- PSOSUDPR
- PSOSUINV
- PSOSULB1
- PSOSULB2
- PSOSULBL
- PSOSULOG
- PSOSUP
- PSOSUPAT
- PSOSUPOE
- PSOSUPRX
- PSOSURST
- PSOSUSRP
- PSOSUTL
- PSOSUTL1
- PSOTALK
- PSOTALK1
- PSOTALK2
- PSOTALK3
- PSOTEXP1
- PSOTPCAN
- PSOTPCEE
- PSOTPCL
- PSOTPCLP
- PSOTPCLR
- PSOTPCLW
- PSOTPCRP
- PSOTPCRX
- PSOTPCUL
- PSOTPENV
- PSOTPHL1
- PSOTPHL2
- PSOTPINA
- PSOTPPOS
- PSOTPPRE
- PSOTPPRV
- PSOTPRP1
- PSOTPRX1
- PSOTRI
- PSOTRLBL
- PSOUT433
- PSOUTIL
- PSOUTL
- PSOUTLA
- PSOUTLA1
- PSOUTLA2
- PSOUTOR
- PSOUTOR1
- PSOVCNT
- PSOVDF1
- PSOVDF2
- PSOVDF3
- PSOVDFK
- PSOVER
- PSOVER1
- PSOVER2
- PSOVERC
- PSOVEXR1
- PSOVEXRX
- PSOVRPT
- PSOVWI
- PSOXR
- PSOXR1
- PSOXR10
- PSOXR11
- PSOXR12
- PSOXR13
- PSOXR14
- PSOXR15
- PSOXR16
- PSOXR17
- PSOXR18
- PSOXR19
- PSOXR2
- PSOXR20
- PSOXR21
- PSOXR22
- PSOXR3
- PSOXR4
- PSOXR5
- PSOXR6
- PSOXR7
- PSOXR8
- PSOXR9
- PSOXWRH
- PSOXWRN
- PSOXX
- PSOXZA
- PSOXZA1
- PSOXZA10
- PSOXZA11
- PSOXZA12
- PSOXZA13
- PSOXZA14
- PSOXZA15
- PSOXZA16
- PSOXZA17
- PSOXZA18
- PSOXZA2
- PSOXZA3
- PSOXZA4
- PSOXZA5
- PSOXZA6
- PSOXZA7
- PSOXZA8
- 
- PSOXZA9

Additional InformationStandards and Conventions Committee (SACC) Exemptions

The following PSO routines will generate errors reported in the XINDEX utility from using non-standard M syntax, due to the need to consume external web services:

PSOERXA1

PSOERXO1

The following waiver permits the use of this non-standard M syntax to allow the use of Cache features to consume external web services. This waiver is located in the HealtheVet Web Services Client (HWSC) Developer Guide.

| OITIMB33554520 - Migration from M2J to VistA Web Services Client (VWSC) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Keywords                                                                | M2J,VWSC,J2EE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Decision Date                                                           | 12/1/2006                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Decision Type                                                           | Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Decision Making Body                                                    | HPMO CCB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Description                                                             | On December 1, 2006, the HPMO Change Control Board voted to accept the migration of VistA from the current M2J solution to the VistA Web Services Client (VWSC). This decision was made for a number of reasons, in particular the fact that the existing 12-year-old M standard has been surpassed by evolving technologies and can no longer address today’s requirements. Additionally, we are no longer required to support DSM, previously the primary VistA/M hosting environment. Today, all sites are standardized on Caché 5.0 systems. As such, approvals were granted as follows: Waiver of the requirement to adhere to the existing 1995 M standard (that does not address the implementation of web services); Implementation of an industry standard such as web services for VistA/M to J2EE calls using Caché’s built in HTTP and web service client feature; Use of VWSC as an interim solution that ensures continuity of integration between VistA/M applications and migrated J2EE applications as HealtheVet evolves by enabling the consumption of external web services by legacy VistA applications; and Deprecation of the original M2J approach. |
| Rationale                                                               | This architectural change allows for a number of improvements, including better scalability, resilience, and performance. Deployment and configuration is far less complicated for administrators, and the APIs can be used by a variety of clients rather than solely M-based. It also places responsibility for support, maintenance, etc. with the vendor rather than OIT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Record Type                                                             | TDR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| State                                                                   | Approved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Date Submitted                                                          | 2/14/2007 8:37:24 AM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

<span id="_Toc207089086" class="anchor"></span>Table 11: Security Keys

| Link     | Document Title                                                            | Description                                               | Date      |
|----------|---------------------------------------------------------------------------|-----------------------------------------------------------|-----------|
| Download | Migration from M2J to VistA Web Services Client (VWSC) Email Notification | Email notification alerting of the decision               | 2/13/2007 |
| Download | VWSC Architecture                                                         | Proposed architecture view of VWSC                        | 12/1/2006 |
| Download | VWSC Proposed View                                                        | Proposed logical view of VistA Web Services Client (VWSC) | 12/1/2006 |

<span id="_Toc207089087" class="anchor"></span>Table 12: Packages - External

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unless menus have already been assigned, the *Outpatient Pharmacy Manager* \[PSO MANAGER\] menu should be assigned to the Package Coordinator for Outpatient Pharmacy. It should also be added to the menu of the Site Manager and any ADP/IRMS staff that the Package Coordinator selects to help in the operation of Outpatient Pharmacy. The *Pharmacist Menu* \[PSO USER1\] option should be assigned to all pharmacists and the *Pharmacy Technician’s Menu* \[PSO USER2\] option should be assigned to all pharmacy technicians and other pharmacy personnel who may view prescriptions, inquire into other Outpatient Pharmacy V. 7.0 files, or both.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089088" class="anchor"></span>Table 13: Packages - Internal</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PROVIDER</td>
<td>Holders of this key will be prompted for ICD-9 Diagnosis code entry.</td>
</tr>
<tr class="even">
<td>PSDRPH</td>
<td><p>This key is assigned to users for accessing the Inbound ePrescribing (eRx) Holding Queue functionality. The key allows users to access all options in the eRx Holding Queue. This key also authorizes pharmacists to verify and dispense controlled substance prescription(s).</p>
<p>Introduced by the Controlled Substances patch PSD*3*76. This key authorizes pharmacists to finish/verify a digitally signed Schedule II-V CS orders placed via CPRS. The PSDRPH security key should be given to registered Pharmacists working on controlled substances to honor Drug Enforcement Administration regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.</p></td>
</tr>
<tr class="odd">
<td>PSORPH</td>
<td>This key is required to use all of the Outpatient Pharmacy V. 7.0 options. It should be assigned to all pharmacists, the package coordinator, and all appropriate members of the ADP / IRMS staff.</td>
</tr>
<tr class="even">
<td>PSO ERX ADV TECH</td>
<td>This key was updated by patch PSO*7*508 for the Inbound eRx Holding Queue. The key allows users to Validate Patient / Provider / Drug / SIG, Accept Patient / Provider / Drug Validations, Reject, Hold / Un Hold, Search, Sort, Remove / UnRemove, and Print Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP), Acknowledge (ACK) – Rx Cancel, Acknowledge (ACK) – Inbound Refill Error.</td>
</tr>
<tr class="odd">
<td>PSO ERX TECH</td>
<td>This key was updated by patch PSO*7*508 for the Inbound eRx Holding Queue functionality. The key allows users to Validate Patient / Provider / Drug / SIG, Hold / Un Hold, Search, Sort, and Print, Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP).</td>
</tr>
<tr class="even">
<td>PSO ERX WORKLOAD RPH</td>
<td>This key was introduced by patch PSO*7*770 for the Inbound eRx Holding Queue functionality. The key is used to identify users that are supposed to work through a list of eRx in a FIFO (First In First Out) sequence. It will be mostly used by Meds-By-Mail (MbM) given the high volume of eRx prescriptions they process daily.</td>
</tr>
<tr class="odd">
<td>PSO ERX WORKLOAD TECH</td>
<td>This key was updated by patch PSO*7*770 for the Inbound eRx Holding Queue functionality. The key is used to identify users that are supposed to work through a list of eRx in a FIFO (First In First Out) sequence. It will be mostly used by Meds-By-Mail (MbM) given the high volume of eRx prescriptions they process daily.</td>
</tr>
<tr class="even">
<td>PSO ERX VIEW</td>
<td>This key was introduced by patch PSO*7*467 for the Inbound eRx Holding Queue functionality. The key allows users to Search, Sort, and View an eRx only.</td>
</tr>
<tr class="odd">
<td>PSO TECH ADV</td>
<td>This security key is used by pharmacy technicians to HOLD and UNHOLD prescriptions using a subset of the HOLD reasons available to PSORPH key holders.</td>
</tr>
<tr class="even">
<td>PSO COPAY</td>
<td>This key is used to identify users to notify when a copay exemption cannot be determined at the time a prescription fill is released. Holders of this key are also notified any time the <em>Exempt Rx Patient Status from Copayment</em> [PSOCP EXEMPTION] option is used to change the copay exemption for an Rx Patient Status.</td>
</tr>
<tr class="odd">
<td>PSO REJECTS BACKGROUND MESSAGE</td>
<td>When prescriptions remain on the Third Party Payer Reject - Worklist over the specified number of days, the system will send a Mailman Message to holders of this key.</td>
</tr>
<tr class="even">
<td>PSOA PURGE</td>
<td><ol start="9">
<li><p>Disabled until further notice.</p></li>
</ol>
<p>This key should be assigned to the package coordinator, any person who will be responsible for archiving prescriptions, or both.</p></td>
</tr>
<tr class="odd">
<td>PSOLOCKCLOZ</td>
<td>This key is used to override the lockouts in the Clozapine options. All members of the Clozapine treatment team must be entered as users on the system and must be given this key. All pharmacists who have the ability to override the lockouts in this option must also hold this key. The Pharmacy Service representative of the Clozapine treatment team should identify these pharmacists.</td>
</tr>
<tr class="even">
<td>PSOINTERFACE</td>
<td>This key is used to access the <em>External Interface Menu</em> [PSO EXTERNAL INTERFACE] option.</td>
</tr>
<tr class="odd">
<td>PSOAUTRF</td>
<td>This key allows the use of the Automate Internet Refill functionality and the Automate CPRS Refill functionality.</td>
</tr>
<tr class="even">
<td>PSO TRICARE/CHAMPVA</td>
<td>This key is required to be able to do an override on TRICARE or CHAMPVA prescription.</td>
</tr>
<tr class="odd">
<td>PSO TRICARE/CHAMPVA MGR</td>
<td>This key is required to access the <em>TRICARE CHAMPVA Override Report</em> [PSO TRI CVA OVERRIDE REPORT] option</td>
</tr>
<tr class="even">
<td>PSO EPHARMACY SITE MANAGER</td>
<td>This key is required to access the <em>PSO ePharmacy Site Parameters</em> [PSO ePHARM SITE PARAMETERS] option.</td>
</tr>
<tr class="odd">
<td>PSO SPMP ADMIN</td>
<td>This key is used by the Outpatient Pharmacy (OP) package to grant certain users administration privileges to perform configuration updates in the State Prescription Monitoring Program (SPMP) module.</td>
</tr>
<tr class="even">
<td>PROVIDER</td>
<td>Holders of this key will be prompted for ICD-9 Diagnosis code entry.</td>
</tr>
<tr class="odd">
<td>PSDRPH</td>
<td><p>This key is assigned to users for accessing the Inbound ePrescribing (eRx) Holding Queue functionality. The key allows users to access all options in the eRx Holding Queue. This key also authorizes pharmacists to verify and dispense controlled substance prescription(s).</p>
<p>Introduced by the Controlled Substances patch PSD*3*76. This key authorizes pharmacists to finish / verify a digitally signed Schedule II-V CS orders placed via CPRS. The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.</p></td>
</tr>
<tr class="even">
<td>PSORPH</td>
<td>This key is required to use all of the Outpatient Pharmacy V. 7.0 options. It should be assigned to all pharmacists, the package coordinator, and all appropriate members of the ADP / IRMS staff.</td>
</tr>
<tr class="odd">
<td>PSO ERX ADV TECH</td>
<td>This key was updated by patch PSO*7*508 for the Inbound eRx Holding Queue. The key allows users to Validate Patient / Provider / Drug / SIG, Accept Patient / Provider / Drug Validations, Reject, Hold / Un Hold, Search, Sort, Remove / UnRemove, and Print Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP), Acknowledge (ACK) – Rx Cancel, Acknowledge (ACK) – Inbound Refill Error.</td>
</tr>
<tr class="even">
<td>PSO ERX TECH</td>
<td>This key was updated by patch PSO*7*508 for the Inbound eRx Holding Queue functionality. The key allows users to Validate Patient / Provider / Drug / SIG, Hold / Un Hold, Search, Sort, and Print, Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP).</td>
</tr>
<tr class="odd">
<td>PSO ERX WORKLOAD TECH</td>
<td>This key was introduced by patch PSO*7*700 for the Inbound eRx Holding Queue functionality. The key is used to identify users that are supposed to work through a list of eRx in a FIFO (First In First Out) sequence. It will be mostly used by Meds-By-Mail (MbM) given the high volume of eRx prescriptions they process daily.</td>
</tr>
<tr class="even">
<td>PSO ERX VIEW</td>
<td>This key was introduced by patch PSO*7*467 for the Inbound eRx Holding Queue functionality. The key allows users to Search, Sort, and View an eRx only.</td>
</tr>
<tr class="odd">
<td>PSO TECH ADV</td>
<td>This security key is used by pharmacy technicians to HOLD and UNHOLD prescriptions using a subset of the HOLD reasons available to PSORPH key holders.</td>
</tr>
<tr class="even">
<td>PSO COPAY</td>
<td>This key is used to identify users to notify when a copay exemption cannot be determined at the time a prescription fill is released. Holders of this key are also notified any time the <em>Exempt Rx Patient Status from Copayment</em> [PSOCP EXEMPTION] option is used to change the copay exemption for an Rx Patient Status.</td>
</tr>
<tr class="odd">
<td>PSO REJECTS BACKGROUND MESSAGE</td>
<td>When prescriptions remain on the Third Party Payer Reject - Worklist over the specified number of days, the system will send a Mailman Message to holders of this key.</td>
</tr>
<tr class="even">
<td>PSOA PURGE</td>
<td><ol start="10">
<li><p>Disabled until further notice.</p></li>
</ol>
<p>This key should be assigned to the package coordinator, any person who will be responsible for archiving prescriptions, or both.</p></td>
</tr>
<tr class="odd">
<td>PSOLOCKCLOZ</td>
<td>This key is used to override the lockouts in the Clozapine options. All members of the Clozapine treatment team must be entered as users on the system and must be given this key. All pharmacists who have the ability to override the lockouts in this option must also hold this key. The Pharmacy Service representative of the Clozapine treatment team should identify these pharmacists.</td>
</tr>
<tr class="even">
<td>PSOINTERFACE</td>
<td>This key is used to access the <em>External Interface Menu</em> [PSO EXTERNAL INTERFACE] option.</td>
</tr>
<tr class="odd">
<td>PSOAUTRF</td>
<td>This key allows the use of the Automate Internet Refill functionality and the Automate CPRS Refill functionality.</td>
</tr>
<tr class="even">
<td>PSO TRICARE/CHAMPVA</td>
<td>This key is required to be able to do an override on TRICARE or CHAMPVA prescription.</td>
</tr>
<tr class="odd">
<td>PSO TRICARE/CHAMPVA MGR</td>
<td>This key is required to access the <em>TRICARE CHAMPVA Override Report</em> [PSO TRI CVA OVERRIDE REPORT] option</td>
</tr>
<tr class="even">
<td>PSO EPHARMACY SITE MANAGER</td>
<td>This key is required to access the <em>PSO ePharmacy Site Parameters</em> [PSO ePHARM SITE PARAMETERS] option.</td>
</tr>
<tr class="odd">
<td>PSO SPMP ADMIN</td>
<td>This key is used by the Outpatient Pharmacy (OP) package to grant certain users administration privileges to perform configuration updates in the State Prescription Monitoring Program (SPMP) module.</td>
</tr>
</tbody>
</table>

<span id="_Toc207089088" class="anchor"></span>Table 13: Packages - Internal

### Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures may be established by using the *Electronic Signature code Edit* \[XUSESIG\] option.

In Kernel V. 8.0 the *Electronic Signature codeEdit* \[XUSESIG\] option has been tied to the Common Options, under the *User’s Toolbox* \[XUSERTOOLS\] submenu, for easy access by all users.

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed information is kept for each prescription, including all information about the original prescription, all refills, and all editing. An average prescription requires about 300 bytes (0.3 Kbytes) of disk storage. The archiving options under the manager’s menu allow the package coordinator and IRMS/ADP staff to manage this file. Old prescriptions, typically those that have been expired or canceled for more than a year, can be saved to tape and then purged from online storage. NOTE: The purge options under the *Archive Menu* \[PRCAK AR SUPERVISOR\] option are out of order until further notice. The User’s Manual describes the operation of these options. Because not all prescriptions require the same amount of space and because of the way the operating system utilizes the disk, do not expect to regain 300 bytes of disk storage for every prescription purged. As prescriptions are purged, all references to these prescriptions from other files are also deleted.

The RX SUSPENSE file (#52.5) holds information about all prescriptions that have been suspended for later printing. There is an automatic purge for this file for prescriptions printed from 7 to 90 days ago. The package coordinator can run the Auto-delete from Suspense \[PSO PNDEL\] option at regular intervals to purge this file of suspended prescriptions which have been printed 7 to 90 days ago. The purging is tasked to run every 7 days.

Specific entries can be deleted using the Change Suspense Date \[PSO PNDCHG\] or Pull Early From Suspense \[PSO PNDRX\] options.

Drug cost data can now be purged using the *Purge Drug Cost Data* \[PSO PURGE DRUG COST\] option.

### Setting up the Archive Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following examples display archive device setups for file and tape.

These examples may differ from site to site. If a device differs, check with IRMS for information on device set up.

HOST FILE SERVER (HFS) DEVICE SETUP:

NAME: HFS \$I: ARC0797.TMP

ASK DEVICE: YES ASK PARAMETERS: NO

VOLUME SET(CPU): VAA QUEUING: ALLOWED

LOCATION OF TERMINAL: COMPUTER AREA ASK HOST FILE: YES

ASK HFS I/O OPERATION: YES \*MARGIN WIDTH: 132

\*FORM FEED: \# \*PAGE LENGTH: 64

\*BACK SPACE: \$C(8) SUBTYPE: P-OTHER

TYPE: HOST FILE SERVER

BAUD RATE (c): UNKNOWN

MAGNETIC TAPE DEVICE SETUP:

NAME: TAPE (T7867) \$I: \$3\$MKA600:

ASK DEVICE: YES ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO

LOCATION OF TERMINAL: COMPUTER ROOM

\*MARGIN WIDTH: 255 \*FORM FEED: \#

\*PAGE LENGTH: 256 \*BACK SPACE: \$C(8)

OPEN PARAMETERS: (FORMAT="VAL4":BLOCKSIZE=2048)

SUBTYPE: MAGTAPE TYPE: MAGTAPE

PERFORM DEVICE CHECKING: NO

BAUD RATE (c): UNKNOWN

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entry points provided by the Outpatient Pharmacy V. 7.0 package to other packages can be found in the External Relations section of this manual. No other routines are designated as callable from outside of this package. For additional information of other external calls and their entry points go to VA Software Document Library (VDL), see under the Clinical Section on the “Pharm: Outpatient Pharmacy” page. Choose the “API Manual: Pharmacy Reengineering (PRE).”

## External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information on HL7 External Interface, go to VA Software Document Library (VDL), select the Infrastructure Section, then choose “HL7 (VistA Messaging).”

11. The HL Logical Link Entry / Node set up for Outpatient Pharmacy V. 7.0 is PSO DISP. This is a new Logical Link installed with Patch PSO\*7\*156.
12. The HL Logical Link Entry / Node set up for Outpatient Pharmacy V. 7.0 is PSORRXSEND. This is a new Logical Link installed with Patch PSO\*7\*454.

### Steps for Startup / Shutdown of the External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens depict the steps necessary to startup and shutdown the external interface for Version 1.6 of the VistA Health Level Seven (HL7) application package. See Appendix A of this manual for more information on the Outpatient Pharmacy V. 7.0 HL7 Specification.

The following examples are options from the HL7 package. The top-level menu option being used is the HL MAIN MENU \[*HL7 Main Menu*\] option.

Example: Starting Up the Interface

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO DISP

The LLP was last shutdown on MAY 11, 2004 07:29:53.

This LLP has been enabled!

Example: Shutting Down the Interface

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO DISP

The LLP was last started on JUN 02, 2004 09:52:02.

Okay to shut down this job? YES

The job for the PSO DISP Lower Level Protocol will be shut down.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software is not included in this package and must be installed before this version of Outpatient Pharmacy is completely functional.

| Package                                                                | Minimum Version Needed |
|------------------------------------------------------------------------|------------------------|
| Accounts Receivable (AR)                                               | 4.5                    |
| Adverse Reaction Tracking (ART)                                        | 4.0                    |
| Clinical Information Resources Network (CIRN)                          | 1.0                    |
| Consolidated Mail Outpatient Pharmacy (CMOP)                           | 2.0                    |
| Computerized Patient Record System (CPRS)                              | 3.0                    |
| Decision Support System (DSS)                                          | 3.0                    |
| Electronic Claims Management Engine (ECME)                             | 1.0                    |
| Fee Basis                                                              | 3.5                    |
| VA FileMan                                                             | 22.0                   |
| HealtheVet Web Services Client (HWSC)                                  | 1.0                    |
| Integrated Funds Control, Accounting, and Procurement (IFCAP)          | 5.0                    |
| Inpatient Medications (IP)                                             | 5.0                    |
| Integrated Billing (IB)                                                | 2.0                    |
| Kernel                                                                 | 8.0                    |
| Laboratory                                                             | 5.2                    |
| MailMan                                                                | 7.1                    |
| Master Patient Index/Patient Demographics (MPI/PD)                     | 1.0                    |
| National Drug File (NDF)                                               | 4.0                    |
| Order Entry/Results Reporting (OERR)                                   | 3.0                    |
| Patient Information Management System (PIMS)                           | 5.3                    |
| Pharmacy Data Management (PDM)                                         | 1.0                    |
| Remote Procedure Call (RPC) Broker                                     | 1.1                    |
| VistALink                                                              | 1.5                    |
| Enterprise Messaging Infrastructure (eMI) Enterprise Service Bus (ESB) | 2.2                    |
| Health Data Repository/Clinical Data Service (HDR/CDS) Repository      | 3.14.1                 |

<span id="_Toc207089089" class="anchor"></span>Table 14: Templates - Sort

13. For Outpatient Medication Copay options to be fully functional, the Pharmacy Ordering Enhancement (POE) project software must be installed, which includes patches to Outpatient Pharmacy (PSO\*7\*46), Order Entry/Results Reporting (OR\*3\*94), Pharmacy Data Management (PSS\*1\*38), and Inpatient Medications (PSJ\*5\*50).
14. For Clinical Indicator Data Capture (CIDC) to be fully functional, the Outpatient Pharmacy CIDC software (PSO\*7\*143) must be installed along with CPRS Version 25.
15. The OneVA Pharmacy Patch PSO\*7\*454 introduced new functionality that allows for a pharmacist to remotely refill <span id="PSO_774_Note1" class="anchor"></span>(and original fill with the introduction of PSO\*7\*774) a prescription from another VistA instance. This patch utilizes Health Level 7 (HL7) messaging to send and receive remote prescription details from another VAMC. This allows a 'dispensing', or 'non-custodial' Pharmacy to refill a prescription that originated from another VA facility. The VA facility where the prescription exists is considered the 'host' facility. Before the release of patch PSO\*7\*736, VistA utilized HL7 to send a query message to middleware application and then the middleware application was used to query the Health Data Repository/Clinical Data Service (HDR/CDS) Repository for all active medications from all sites. The medications are returned to the querying site. Once the prescriptions are received, they are displayed below any 'local' prescriptions within the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option sorted by facility. The pharmacist can then view the remote prescriptions and will be able to refill or partially fill (or original fill with the introduction of PSO\*7\*774) any active prescriptions that are not considered controlled substances at either facility. The OneVA Pharmacy patch PSO\*7\*736 (January 2024) replaces the query to the HDR/CDS repository with a query to the Veterans Data Information Exchange (VDIF). The OneVA Pharmacy software sends an HL7 message to VDIF National Health Connect to an existing TCP Service to request patient medications. PSO\*7\*774 (September 2025) also introduced auto-unpark and auto-release functionality (on the ‘host’ facility) for OneVA Pharmacy processing.
16. The OneVA HL7 Listener Service is using an existing connection that all 130+ VistAs have with the National HL7 Health Connect.

### Data Base Integration Agreements (IAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy V. 7.0 has Data Base Integration Agreements (IAs) with the packages listed above, in addition to the following: Consolidated Mail Outpatient Pharmacy (CMOP), Drug Accountability (DA), Controlled Substances (CS), and Health Level Seven. Pharmacy patch PSO\*7\*774 also introduced Outpatient Pharmacy as a subscriber to Kernel as part of IA 4129 to set the DUZ to PSOAUTORELEASE,PROXY USER for downstream ECME processing. For complete information regarding the IAs for Outpatient Pharmacy V. 7.0, please refer to the *Integration AgreementMenu* \[DBA IA ISC\] option under the *DBA* \[DBA\] option on FORUM.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Very few of the options in this package can be invoked independently. Those that can be so invoked independently are:

| Package                                     | Description                 |
|---------------------------------------------|-----------------------------|
| PSO MANAGER                                 | Outpatient Pharmacy Manager |
| PSO P                                       | Medication Profile          |
| PSO USER1                                   | Pharmacist Menu             |
| PSO USER2                                   | Pharmacy Technician’s Menu  |
| Any other option may not run independently. |                             |

<span id="_Toc207089090" class="anchor"></span>Table 15: Templates - Input

Any locally created menu which includes options from this package *must* have the ENTRY ACTION field read: D:'\$D(PSOPAR) ^PSOLSET and should have the MENU EXIT ACTION field read: D FINAL^PSOLSET

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The variables PSODIV, PSOINST, PSOIOS, PSOPAR, PSOPAR7, PSOSYS, PSOLAP, PSOPROP, PSOCLC, PSOCNT, PSODTCUT, PSOSITE, PSOPRPAS, PSOBAR0, PSOBAR1 and PSOBARS are used extensively throughout the package. They are set by the routine PSOLSET and are not killed until exiting from the package.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Sort                   | File      |
|------------------------|-----------|
| PSO COST STAT          | 50.9      |
| PSO BBWAIT SORT        | 52.11     |
| PSO DEA DISUSER2 SORT  | 200       |
| PSO DEA DIV SORT       | 200       |
| PSO DEA PSDRPH SORT    | 200       |
| PSO DEA SET PARMS SORT | 200       |
| PSO DRUG LIST          | 50        |
| PSO DRUG WARNINGS      | 52        |
| PSO HOLD LIST          | 52        |
| PSO INTERVENTIONS      | 9009032.4 |
| PSO NARC LIST          | 52        |
| PSOUPAT                | 52        |
| PSO PARK LIST          | 52        |

<span id="_Toc207089091" class="anchor"></span>Table 16: Templates - Print

| Input                         | File      |
|-------------------------------|-----------|
| PSO CLINICAL ALERT ENTER/EDIT | 55        |
| PSO CLOZDRUG                  | 50        |
| PSO DISPLAY EDIT              | 59.3      |
| PSO INTERACT                  | 56        |
| PSO INTERVENTION EDIT         | 9009032.4 |
| PSO INTERVENTION NEW          | 9009032.4 |
| PSO OUTPT                     | 2         |
| PSO OUTPTA                    | 2         |
| PSO PARTIAL                   | 52        |
| PSO SITE                      | 59        |
| PSOD DUE BUILD QUESTIONNAIRE  | 50.073    |
| PSOD DUE EDIT                 | 50.0731   |

<span id="_Toc207089092" class="anchor"></span>Table 17: Security Keys

| Print                       | File      |
|-----------------------------|-----------|
| PSO ACTION PROFILE          | 44        |
| PSO ACTION PROFILE \#2      | 44        |
| PSO ALPHA DRUG LIST         | 50        |
| PSO BBWAIT PRINT            | 52.11     |
| PSO COST STAT               | 50.9      |
| PSO DEA PRIVS PRINT         | 200       |
| PSO DEA DISUSER PRIVS PRINT | 200       |
| PSO DEA PSDRPH PRINT        | 200       |
| PSO DEA SET PARMS PRINT     | 200       |
| PSO DRUG LIST               | 50        |
| PSO DRUG WARNINGS           | 52        |
| PSO DRUG WARNINGS HEADER    | 52        |
| PSO HOLD                    | 52        |
| PSO INACTIVE DRUG LIST      | 50        |
| PSO INTERVENTIONS           | 9009032.4 |
| PSO N/F LIST                | 50        |
| PSO NARC LIST               | 52        |
| PSO PARK                    | 52        |
| PSO PHARMACY STATS          | 50.9      |
| PSO REQUEST STATISTICS      | 50.9      |
| PSO SUSPENSE LIST           | 52.5      |
| PSO SYNONYM LIST            | 50        |
| PSOD PRINT ANSWER SHEET     | 50.0731   |

<span id="_Toc207089093" class="anchor"></span>Table 18: File Attributes

## Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Group Setup for the HL7 External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A mail group and device should be set up in order to run the HL7 external interface. The recommended name of the mail group is REDACTED. The recommended device name is REDACTED.

### Archiving / Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For archiving and purging information, see the section titled “Archiving and Purging” in this manual.

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For interface information, see the section titled “External Interfaces” in this manual.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures may be established by using the *Electronic Signature codeEdit* \[XUSESIG\] option. In Kernel V. 8.0 the *Electronic Signature codeEdit* \[XUSESIG\] option has been tied to the Common Options, under the *User’s Toolbox* \[XUSERTOOLS\] submenu, for easy access by all users.

### Menu Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Outpatient Pharmacy Manager* \[PSO MANAGER\] menu should be assigned to the Package Coordinator for Outpatient Pharmacy and also added to the menu of the Site Manager and any ADP/IRMS staff that s/he selects to help in the operation of Outpatient Pharmacy. The *Pharmacist Menu* \[PSO USER1\] option should be assigned to all pharmacists and the *Pharmacy Technician’s Menu* \[PSO USER2\] option should be assigned to all pharmacy technicians and other pharmacy personnel who may view prescriptions, inquire into other Outpatient Pharmacy files, or both.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089094" class="anchor"></span>Table 19: Variables</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSDRPH</td>
<td><a href="\l">This key is assigned to users for accessing the Inbound ePrescribing (eRx) Holding Queue functionality. The key allows users to access all options in the eRx Holding Queue. This key also authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered Pharmacists working on controlled substances to honor Drug Enforcement Administration regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist. This security key is used to Validate Patient (VP), Validate Provider (VM), Validate Drug/SIG (VD), Accept Validation (AV), Accept eRx (AC), Reject (RJ), Remove (RM), Hold (H), Un-Hold (UH), Search / Sort, Print, Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP), Acknowledge (ACK) – Rx Cancel, Acknowledge (ACK) – Inbound Refill Error.</a></td>
</tr>
<tr class="even">
<td>PSORPH</td>
<td>This key is required to use all of the Outpatient Pharmacy V. 7.0 options. It should be assigned to all pharmacists, the package coordinator, and all appropriate members of the ADP/IRMS staff.</td>
</tr>
<tr class="odd">
<td>PSO ERX ADV TECH</td>
<td><a href="\l">This security key is used by advanced pharmacy technicians to Validate Patient / Provider / Drug / SIG, Accept Patient / Provider / Drug Validations, Reject, Hold / Un Hold, Search, Sort, Remove, and Print Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP), Acknowledge (ACK) – Rx Cancel, Acknowledge (ACK) – Inbound Refill Error in the Inbound ePrescribing Holding Queue.</a></td>
</tr>
<tr class="even">
<td>PSO ERX TECH</td>
<td>This security key is used by pharmacy technicians to Validate Patient / Provider / Drug / SIG, Hold / Un Hold, Search, Sort, and Print Message View (MV), Acknowledge (ACK) – Refill Response, Refill Request (OP)in the Inbound ePrescribing Holding Queue.</td>
</tr>
<tr class="odd">
<td>PSO ERX VIEW</td>
<td><a href="#pg32c">This security key is assigned to users with the need to Search, Sort, Print, Message View (MV) an eRx only in the Inbound ePrescribing Holding Queue.</a></td>
</tr>
<tr class="even">
<td>PSO TECH ADV</td>
<td>This security key is used by pharmacy technicians to HOLD and UNHOLD prescriptions using a subset of the HOLD reasons available to PSORPH key holders.</td>
</tr>
<tr class="odd">
<td>PSO COPAY</td>
<td>This key should be assigned to any users who need to be notified when a copay exemption cannot be determined at the time a prescription fill is released. Holders of this key are also notified any time the Exempt Rx Patient Status from Copayment [PSOCP EXEMPTION] option is used to change the copay exemption for an Rx Patient Status.</td>
</tr>
<tr class="even">
<td>PSO REJECTS BACKGROUND MESSAGE</td>
<td>When prescriptions remain on the Third Party Payer Reject - Worklist over the specified number of days, the system will send a Mailman Message to holders of this key.</td>
</tr>
<tr class="odd">
<td>PSOA PURGE</td>
<td><ol start="17">
<li><p>Disabled until further notice.</p></li>
</ol>
<p>This key should be assigned to the package coordinator, any person who will be responsible for archiving prescriptions, or both.</p></td>
</tr>
<tr class="even">
<td>PSOLOCKCLOZ</td>
<td>This key is used to override the lockouts in the Clozapine option. All members of the Clozapine treatment team must be entered as users on the system and must be given this key. All pharmacists who have the ability to override the lockouts in this option must also hold this key. The Pharmacy Service representative of the Clozapine treatment team should identify these pharmacists.</td>
</tr>
<tr class="odd">
<td>PSOINTERFACE</td>
<td>This key is used to access the External Interface Menu [PSO EXTERNAL INTERFACE] option.</td>
</tr>
<tr class="even">
<td>PSO TRICARE/CHAMPVA</td>
<td>This key should be assigned to a pharmacist in order to perform an Override and electronically sign a prescription for a TRICARE or CHAMPVA patient.</td>
</tr>
<tr class="odd">
<td>PSO TRICARE/CHAMPVA MGR</td>
<td>This key is required to access the TRICARE CHAMPVA Override Report [PSO TRI CVA OVERRIDE REPORT] option.</td>
</tr>
<tr class="even">
<td>PSO EPHARMACY SITE MANAGER</td>
<td>This key is required to access the PSO ePharmacy Site Parameters [PSO ePHARM SITE PARAMETERS] option.</td>
</tr>
<tr class="odd">
<td>PSO SPMP ADMIN</td>
<td>This key is used by the Outpatient Pharmacy (OP) package to grant certain users administration privileges to perform configuration updates in the State Prescription Monitoring Program (SPMP) module.</td>
</tr>
</tbody>
</table>

<span id="_Toc207089094" class="anchor"></span>Table 19: Variables

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires 26 files in addition to those of the Kernel and other files to which it points, for example the PATIENT file (#2). Information about all files, including these can be obtained by using the VA FileMan to generate a list of file attributes.

<table>
<caption><p><span id="_Toc207089095" class="anchor"></span>Table 20: Glossary</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 53%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>File Numbers</th>
<th>File Names</th>
<th>DD</th>
<th>RD</th>
<th>WR</th>
<th>DEL</th>
<th>LAYGO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>50.073</td>
<td>DUE QUESTIONNAIRE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>50.0731</td>
<td>DUE ANSWER SHEET</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.0732</td>
<td>DUE QUESTION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>50.0733</td>
<td>DUE SECTION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.9</td>
<td>DRUG COST</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>52</td>
<td>PRESCRIPTION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.09</td>
<td>REMOTE PRESCRIPTION LOG</td>
<td>#</td>
<td>P</td>
<td>P</td>
<td>P</td>
<td>P</td>
</tr>
<tr class="even">
<td>52.11</td>
<td>PATIENT NOTIFICATION (Rx READY)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.4</td>
<td>RX VERIFY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.41</td>
<td>PENDING OUTPATIENT ORDERS</td>
<td></td>
<td></td>
<td>@</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.43</td>
<td>PRESCRIPTION REFILL REQUEST</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.45</td>
<td>ERX SERVICE REASON CODES</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>52.46</td>
<td>ERX EXTERNAL PATIENT</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.47</td>
<td>ERX EXTERNAL PHARMACY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>52.48</td>
<td>ERX EXTERNAL PERSON</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.49</td>
<td>ERX HOLDING QUEUE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>52.5</td>
<td>RX SUSPENSE</td>
<td></td>
<td></td>
<td></td>
<td>#</td>
<td></td>
</tr>
<tr class="even">
<td>52.51</td>
<td>PHARMACY EXTERNAL INTERFACE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>52.52</td>
<td>CLOZAPINE PRESCRIPTION<br />
OVERRIDES</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.53</td>
<td>PHARMACY AUTOMATED DISPENSING DEVICES</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.8</td>
<td>PHARMACY ARCHIVE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>52.86</td>
<td>EPHARMACY SITE PARAMETERS</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>52.87</td>
<td>PSO AUDIT LOG</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>52.9</td>
<td>PHARMACY PRINTED<br />
QUEUE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.91</td>
<td>TPB ELIGIBILITY</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>52.92</td>
<td>TPB INSTITUTION LETTERS</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>53</td>
<td>RX PATIENT STATUS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>58.4</td>
<td>SPMP ASAP RECORD DEFINITION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>58.41</td>
<td>SPMP STATE PARAMETERS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>58.42</td>
<td>SPMP EXPORT BATCH</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>59</td>
<td>OUTPATIENT SITE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>59.1</td>
<td>OUTPATIENT AMIS DATA</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>59.12</td>
<td>OUTPATIENT PHARMACY<br />
MANAGEMENT DATA</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>59.2</td>
<td>WAITING TIME</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>59.3</td>
<td>GROUP DISPLAY</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>59.8</td>
<td>OUTPATIENT CLINIC SORT<br />
GROUP</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc207089095" class="anchor"></span>Table 20: Glossary

18. Please refer to Chapter 28 of Kernel V. 8.0 Systems Manual concerning installation of security codes sections entitled “Sending Security Codes.”

## Outpatient Pharmacy V. 7.0 Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three main menus are exported with the package. The *Outpatient Pharmacy Manager* \[PSO MANAGER\] menu should be assigned to supervisors, package coordinators, and members of the ADP/IRMS staff. Pharmacists should have the *Pharmacist Menu* \[PSO USER1\] option and clerks and technicians should have the *Pharmacy Technician’s Menu* \[PSO USER2\] option.

### Outpatient Pharmacy Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Archiving

> Find

> Save to Tape

> Tape Retrieval

> Archive to File

> File Retrieval

> Purge

> \*\*\> Out of order: Unavailable - Under Construction

> List One Patient's Archived Rx's

> Print Archived Prescriptions

> Autocancel Rx’s on Admission

> Bingo Board ...

> BM Bingo Board Manager ...

> Enter/Edit Display

> Auto-Start Enter/Edit

> Print Bingo Board Statistics

> Print Bingo Board Wait Time

> Purge Bingo Board Data

> Start Bingo Board Display

> Stop Bingo Board Display

> BU Bingo Board User ...

> Enter New Patient

> Display Patient’s Name on Monitor

> Remove Patient’s Name from Monitor

> Status of Patient’s Order

> Change Label Printer

> Check Drug Interaction

> Clozapine Pharmacy Manager

> Display Lab Tests and Results

> Edit Data for a Patient in the Clozapine Program

> List of Override Prescriptions

> Register Clozapine Patient

> Copay Menu ...

> CHAMPUS Billing Exemption

> Exempt Rx Patient Status from Copayment

> Reset Copay Status List Manager

> Reset Copay Status/Cancel Charges

> DUE Supervisor ...

> 1 Enter a New Answer Sheet

> 2 Edit an Existing Answer Sheet

> 3 Create/Edit a Questionnaire

> 4 Batch Print Questionnaires

> 5 DUE Report

> Enter/Edit Clinic Sort Groups

> External Interface Menu …

> Purge External Batches

> Reprint External Batches

> View External Batches

> Label/Profile Monitor Reprint

> Maintenance (Outpatient Pharmacy) ...

> Site Parameter Enter/Edit

> Edit Provider

> Add New Providers

> Queue Background Jobs

> Autocancel Rx’s on Admission

> Bingo Board Manager ...

> Enter/Edit Display

> Auto-Start Enter/Edit

> Print Bingo Board Statistics

> Print Bingo Board Wait Time

> Purge Bingo Board Data

> Start Bingo Board Display

> Stop Bingo Board Display

> Edit Data for a Patient in the Clozapine Program

> Enter/Edit Clinic Sort Groups

> Initialize Rx Cost Statistics

> Edit Pharmacy Intervention

> Delete Intervention

> Auto-delete from Suspense

> Automate Internet Refill

> Delete a Prescription

> Enter/Edit Automated Dispensing Devices

> Expire Prescriptions

> Manual Auto Expire Rxs

> Non-VA Provider Import

> Prescription Cost Update

> Purge Drug Cost Data

> Purge External Batches

> Recompile AMIS Data

> Medication Profile

> Output Reports ...

> Action Profile (132 COLUMN PRINTOUT)

> Alpha Drug List and Synonyms

> AMIS Report

> Bad Address Reporting Main Menu …

> Bad Address Suspended List

> List Prescriptions Not Mailed

> CMOP Controlled Substance Rxs Dispense Report

> Commonly Dispensed Drugs

> Cost Analysis Reports ...

> Clinic Costs

> Division Costs by Drug

> Drug Costs

> Drug Costs by Division

> Drug Costs by Division by Provider

> Drug Costs by Provider

> High Cost Rx Report

> Patient Status Costs

> Pharmacy Cost Statistics Menu ...

> Pharmacy Statistics

> Sort Statistics By Division

> Provider by Drug Costs

> Provider Costs

> Request Statistics

> Daily AMIS Report

> Drug List By Synonym

> Free Text Dosage Report

> Inactive Drug List

> Internet Refill Report

> List of Patients/Prescriptions for Recall Notice

> List Prescriptions on Hold

> Management Reports Menu ...

> Daily Management Report Menu ...

> All Reports

> Cost of Prescriptions

> Count of Prescriptions

> Intravenous Admixture

> Type of Prescriptions Filled

> Date Range Recompile Data

> Initialize Daily Compile

> Monthly Management Report Menu ...

> All Reports

> Cost of Prescriptions

> Count of Prescriptions

> Intravenous Admixture

> Type of Prescriptions Filled

> One Day Recompile Data

> Purge Data

> Medication Profile

> Monthly Drug Cost

> Narcotic Prescription List

> Non-Formulary List

> Non-VA Meds Usage Report

> Poly Pharmacy Report

> Prescription List for Drug Warnings

> Released and Unreleased Prescription Report

> Pharmacy Intervention Menu ...

> Enter Pharmacy Intervention

> Edit Pharmacy Intervention

> Print Pharmacy Intervention

> Delete Intervention

> View Intervention

> Process Order Checks

> Release Medication

> Return Medication to Stock

> Rx (Prescriptions) ...

> Patient Prescription Processing

> Barcode Rx Menu ...

> Barcode Batch Prescription Entry

> Check Quality of Barcode

> Process Internet Refills

> Complete Orders from eRX

> Complete Orders from OERR

> Discontinue Prescription(s)

> Edit Prescriptions

> ePharmacy Menu ...

> Ignored Rejects Report

> ePharmacy Medication Profile (View Only)

> NDC Validation

> ePharmacy Medication Profile Division Preferences

> ePharmacy Site Parameters

> Third Party Payer Rejects - View/Process

> Third Party Payer Rejects – Worklist

> TRICARE CHAMPVA Override Report

> Pharmacy Productivity/Revenue Report

> View ePharmacy Rx

> List One Patient’s Archived Rx’s

> Manual Print of Multi-Rx Forms

> OneVA Pharmacy Prescription Report

> Reprint an Outpatient Rx Label

> Signature Log Reprint

> View Prescriptions

> ScripTalk Main Menu ...

> PT ScripTalk Patient Enter/Edit

> QBAR Queue ScripTalk Label by Barcode

> QRX Queue ScripTalk Label by Rx#

> RPT ScripTalk Reports ...

AUD ScripTalk Audit History Report

WHO Report of ScripTalk Enrollees

> Reprint a non-voided Outpatient Rx Label

> PARM Set Up and Test ScripTalk Device ...

ScripTalk Device Definition Enter/Edit

Print Sample ScripTalk Label

Test ScripTalk Device

Reinitialize ScripTalk Printer

> Supervisor Functions ...

> Add New Providers

> Batch eRx Change Request/VistA Drug Replacement

> Daily Rx Cost

> Delete a Prescription

> Edit Provider

> Initialize Rx Cost Statistics

> Inter-Divisional Processing

> Inventory

> Lookup Clerk by Code

> Medication Status Check

> Monthly Rx Cost Compilation

> Patient Address Changes Report

> Pharmacist Enter/Edit

> Purge Drug Cost Data

> Recompile AMIS Data

> Site Parameter Enter/Edit

> State Prescription Monitoring Program Menu

> View/Edit ASAP Definitions

> View/Edit SPMP State Parameters

> View/Export Single Prescription

> View/Export Void Prescriptions

> View/Export Batch

> Export Batch Processing

> Accounting Of Disclosures Report

> Manage Secure SHell (SSH) Keys

> Unmark Rx Fill as Administered In Clinic

> CS Prescriptions Not Transmitted

> Manual Export/Prescription Correction

> View Provider

> Suspense Functions ...

> Auto-delete from Suspense

> Change Suspense Date

> Count of Suspended Rx’s by Day

> Delete Printed Rx’s from Suspense

> Log of Suspended Rx’s by Day (this Division)

> Print from Suspense File

> Pull Early from Suspense

> Queue CMOP Prescription

> Reprint Batches from Suspense

> Update Patient Record

> Verification ...

> List Non-Verified Scripts

> Non-Verified Counts

> Rx Verification by Clerk

### Pharmacist Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bingo Board User ...

> Enter New Patient

> Display Patient’s Name on Monitor

> Remove Patient’s Name from Monitor

> Status of Patient’s Order

> Change Label Printer

> Change Suspense Date

> Check Drug Interaction

> DUE Supervisor ...

> 1 Enter a New Answer Sheet

> 2 Edit an Existing Answer Sheet

> 3 Create/Edit a Questionnaire

> 4 Batch Print Questionnaires

> 5 DUE Report

> Enter/Edit Clinic Sort Groups

> External Interface Menu …

> Purge External Batches

> Reprint External Batches

> View External Batches

> Medication Profile

> Pharmacy Intervention Menu ...

> Enter Pharmacy Intervention

> Edit Pharmacy Intervention

> Print Pharmacy Intervention

> Delete Intervention

> View Intervention

> Print from Suspense File

> Process Order Checks

> Pull Early from Suspense

> Queue CMOP Prescription

> Release Medication

> Return Medication to Stock

> Rx (Prescriptions) ...

> Patient Prescription Processing

> Barcode Rx Menu ...

> Barcode Batch Prescription Entry

> Check Quality of Barcode

> Process Internet Refills

> Complete Orders from OERR

> Discontinue Prescription(s)

> Edit Prescriptions

> ePharmacy Menu ...

> Ignored Rejects Report

> ePharmacy Medication Profile (View Only)

> NDC Validation

> ePharmacy Medication Profile Division Preferences

> ePharmacy Site Parameters

> Third Party Payer Rejects - View/Process

> Third Party Payer Rejects - Worklist

> TRICARE CHAMPVA Override Report

> Pharmacy Productivity/Revenue Report

> View ePharmacy Rx

> List One Patient’s Archived Rx’s

> Manual Print of Multi-Rx Forms

> OneVA Pharmacy Prescription Report

> Reprint an Outpatient Rx Label

> Signature Log Reprint

> View Prescriptions

> Update Patient Record

> Verification ...

> List Non-Verified Scripts

> Non-Verified Counts

> Rx Verification by Clerk

### Pharmacy Technician’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bingo Board User ...

> Enter New Patient

> Display Patient’s Name on Monitor

> Remove Patient’s Name from Monitor

> Status of Patient’s Order

> Change Label Printer

> DUE User ...

> 1 Enter a New Answer Sheet

> 2 Edit an Existing Answer Sheet

> 3 Batch Print Questionnaires

> Medication Profile

> Patient Prescription Processing

> Pull Early from Suspense

> Queue CMOP Prescription

> Release Medication

> Update Patient Record

### Standalone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transitional Pharmacy Benefit (TPB) options were available in previous releases of Outpatient Pharmacy V. 7.0 but are currently placed “Out of Order” by PSO\*7\*227.

Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] option was added by patch PSO\*7.0\*481. This option is not attached to a menu and therefore must be assigned individually to each user requiring access. See the Non-VA Provider Import (PSO\*7.0\*481) Deployment, Installation, Back-out and Rollback Guide for more information.

The DEA Delete \[PSO DEA DELETE\] option was added by patch PSO\*7.0\*529. This option is not attached to a menu. NOTE: THIS OPTION SHOULD NEVER BE RUN. See the PSO\*7.0\*529 Deployment, Installation, Back-out and Rollback Guide for more information.

DEA Migration Report \[PSO DEA MIGRATION REPORT\] option was added by patch PSO\*7.0\*529. This option is not attached to a menu and therefore must be assigned individually to each user requiring access. See the PSO\*7.0\*529 Deployment, Installation, Back-out and Rollback Guide for more information.

The ePCS DEA Utility Functions \[PSO EPCS UTILITY FUNCTIONS\] menu option was added as a stand-alone menu option to support Pharmacy Operational Updates as part of patch PSO\*7.0\*667 and updated as part of patch PSO\*7.0\*545. This option is not attached to a menu and therefore must be assigned individually to each user requiring access. See the PSO\*7.0\*667 and PSO\*7.0\*545 Deployment, Installation, Back-out and Rollback Guide for more information. This option has the following menu items:

- DEA Expiration Date Report \[PSO EPCS EXPIRE DATE REPORT\]
- Changes to DEA Prescribing Privileges Report \[PSO EPCS LOGICAL ACCESS REPORT\]
- Allocation Audit of PSDRPH Key Report \[PSO EPCS PHARMACIST ACC REPORT\]
- Enter/Edit EPCS Access Reports Parameters \[PSO EPCS ACCESS REPORTS PARAM\]
- Print PSDRPH Key Holders \[PSO EPCS PSDRPH\]
- Set Pharmacy Operating Mode \[PSO VAMC MBM PHARMACY MODE\]
- Print Setting Parameters Privileges \[PSO EPCS SET PARMS\]
- Print Prescribers with Privileges \[PSO EPCS PRIVS\]
- Edit Facility DEA# and Expiration Date \[PSO EPCS EDIT DEA# AND XDATE\]
- Print Audits for Prescriber Editing \[PSO EPCS PRINT EDIT AUDIT\]
- Print DISUSER Prescribers with Privileges \[PSO EPCS DISUSER PRIVS\]
- Allow VA Number if DEA Number Expired \[PSO EPCS EXPIRED DEA FAILOVER\]
- Manual DEA Number Entry \[PSO EPCS DEA MANUAL ENTRY\]
- Manually Entered DEA Number Report \[PSO EPCS MANUAL DEA REPORT\]
- DEA Number Integrity Check \[PSO EPCS DEA INTEGRITY REPORT\]

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary global the Outpatient Pharmacy V. 7.0 package uses is ^PSRX. This global is recommended if journaling is used. The majority of the other files used by the Outpatient Pharmacy package are stored in the ^PS global. This global is also recommended for journaling, if used.

## Barcodes and Label Printer Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of Outpatient Pharmacy includes the ability to print barcodes on the patient copy, the pharmacist’s copy, and the patient narrative documents for new label stock and laser labels. Two options utilize the barcodes.

19. The OneVA Pharmacy Patch PSO\*7\*454 introduced the OneVA Pharmacy label-generation functionality with new/updated label routines. The barcode printed on the OneVA Pharmacy label will contain the host site information where the prescription order originated not the dispensing site where the prescription is being filled.

    *Check Quality of Barcode* \[PSO BARCODE CHECK\] option is used to monitor the quality and readability of the barcode before it is mailed.

    *Barcode Batch Prescription Entry* \[PSO BATCH BARCODE\] option is used to actually refill the prescriptions utilizing barcodes in a batch entry.

If barcodes are not used, enter an “OUT OF ORDER MESSAGE” for these two options.

### Barcodes on Dot Matrix Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three parameters are used.

- X is the barcode height. Values can be "S", "M" or "L". If X is undefined or not equal to one of these, the default value of "S" is used. "S" is 2/10 inch for the DS-220 and 1/6 inch for the MT-290. "M" is 4/10 inch for the DS-200 and 1/3 inch for the MT-290. "L" is one inch for both.
- X1 is the value of \$X at the left edge of the barcode. If X1 is undefined, the default value of 0 is used.
- X2 is the data to be bar coded. Remember the code 39 character set that the VA uses is a limited subset of the ASCII character set containing only the numbers, uppercase letters, and eight punctuation characters. In most cases, any other characters are not printed. For example, the barcode for the string 123abc will be the same as the string 123.

On most printers, printing a barcode is a graphics operation that causes the value of \$Y to be something other than the line count from the top of the page. Forms with barcodes must use a form feed to go to the top of the next form rather than a counted number of line feeds. This is why printers used to print barcodes on outpatient pharmacy labels *must be set for a form length of 24 lines or four inches.*

The following section, New Label Stock, contains barcode on and off sequences for various printers.

### New Label Stock (Version 6.0 and Later Versions) – Dot Matrix Labels 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089096" class="anchor"></span>Table 21: HL7 Messages will be used to Support the Exchange of Outpatient Pharmacy Data with Any Automatic Dispensing System</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/003.png)</th>
<th><p><strong>*Important*</strong></p>
<p>Please test new label stock on all printers that will be used before going into production with new label stock.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc207089096" class="anchor"></span>Table 21: HL7 Messages will be used to Support the Exchange of Outpatient Pharmacy Data with Any Automatic Dispensing System

Printers used to print the new label stock must be set to print at 12 characters per inch. The form length must be set to 5 inches.

Previously, old label stock printed barcodes in one column at 10 characters per inch. New label stock prints barcodes at 12 characters per inch in 2 columns, (columns 54 and 102). The following barcode entries in the TERMINAL TYPE file (#3.2) have worked at either the Birmingham Office of Information Field Office (OIFO) or at a site.

20. If you cannot find barcodes that work, please contact the nearest OIFO.

Check to see that a line feed is performed after the barcode off sequence is executed. Due to limited space, information must be printed after certain barcodes print, without relying on a line feed in the Outpatient Pharmacy code. To test this, print a test label for an Rx with no refills. On the center copy of the label, on the next line after the “station number-Rx no.” which prints directly under the barcode, one of the two following lines should print clearly:

\* NO REFILLS REMAINING \*\* PHYSICIAN USE ONLY \*

or

\*\*\* This prescription CANNOT be renewed \*\*\*

If there is a problem, insert a line feed at the end of the Barcode Off sequence.

(Add a ,! to the end of the sequence.)

Remember to set the New Label Stock site parameter to Yes.

Three site parameters provide patient instructions that will print after each patient’s prescriptions. They are “NARRATIVE NON-REFILLABLE RX”, “NARRATIVE REFILLABLE RX”, and “NARRATIVE FOR COPAY DOCUMENT”. The “NARRATIVE FOR COPAY DOCUMENT” will only print if at least one of the patient’s prescriptions is subject to a Copay charge.

For the Data South 220

BAR CODE ON=

\*27,"\[1w",\*27,"\$70s",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"10",1: "04"),\*94, "BDB"

BAR CODE OFF=\*94,"G",\*27,"\$70c",\*27,"\[2w",!

For the MT-661

BAR CODE ON=

\*27,"\[\<4h",\*94,\$S(\$X\<60:"T450",1:"T850"),\*94,"W9;5;1",\*94,"B1;35;1;3",\*13

BAR CODE OFF=\*13,\*10,\*27,"\[\<4l",\*27,"\[5w"

The character after the \[\<4 in the BAR CODE OFF above is a lower case L.

For the Genicom 4440:

BAR CODE ON=\*27,"\[;3;1;;4;;4;;;1;}",\*27,"\[3t"

BAR CODE OFF=\*27,"\[0t",!

For the MT290:

BAR CODE ON=\*26, "F0",\$S(‘\$D(X):2,X="M":2,X="S":1,X="L":6,1:2), ";000",\*25,\*20,"\*"

BAR CODE OFF="\*",\*20,!,?\$S(\$D(X1):X1,1:0),\$S(\$D(X2):X2,1:"")

or

BAR CODE ON=\*26,\*34,"F3;000",\*25,\*20,"\*"

BAR CODE OFF="\*",\*20

For the OTC 560:

BAR CODE ON=\*27,"\[;",\$S('\$D(X):3,X="M":6,X="L":12,1:3),"} ",\*27,"\[3t"

BAR CODE OFF=\*27,"\[0t"

For the Genicom 4490:

BAR CODE ON=\*27,"\[3t",\*14

BAR CODE OFF=\*15,\*27,"\[0t",\*13

21. \*\*The setup of the MT290 will not allow for a form length of 5 inches. It skips from 4 to 5.5. Following is the terminal type information that will allow the MT290 to print the labels at a form length of 5 inches.

NAME: P-MANNESMANN MT290/132 (PHAR) RIGHT MARGIN: 132

FORM FEED: \# PAGE LENGTH: 30

BACK SPACE: \$C(8)

OPEN EXECUTE: W \*27,"\[4W",\*27,"\[0Y",\*27,"\[30t"

10 PITCH: \$C(27)\_"\[4w" 12 PITCH: \$C(27)\_"\[5w"

DESCRIPTION: MANNESMANN TALLY 290/132 COLUMNS

16 PITCH: \$C(27)\_"\[6w" DEFAULT PITCH: \$C(27)\_"\[4w"

BAR CODE OFF: "\*",\*20,!,?\$S(\$D(X1):X1,1:0),\$S(\$D(X2):X2,1:"")

BAR CODE ON: \*26,"F0",\$S('\$D(X):2,X="M":2,X="S":1,X="L":6,1:2),";000", \*25,\*20,"\*"

The \*27,"\[30t" was added to the Open Execute.

### Laser Label Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy package, with the release of PSO\*7\*120, supports the use of laser printers to print prescription labels and all associated documents.

#### Hardware Setup

The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files just as any other laser printer on your network is defined.

In addition, the CONTROL CODES field (#55) of the TERMINAL TYPE file (#3.2) must be defined correctly. To facilitate this, a new routine assists with the setup. At the programmer prompt enter: D ^PSOLLU2. You will be prompted for the device. Enter the device you want to use for printing laser labels. Then, you will be prompted for HP or LexMark. Enter the appropriate selection.

Phase I of Laser Labels introduced the routine PSOLLU2. A pre-release to Phase II introduced the PSOLLU3 routine and Phase II introduced the PSOLLU4 routine. (Instructions for running the PSOLLU3 and PSOLLU4 routines are the same as running the PSOLLU2 routine above.) If you are setting up a laser printer for the first time, run all three routines in order – PSOLLU2, PSOLLU3, and PSOLLU4. If you are already running laser labels, you will only need to run the PSOLLU4 routine to update the control codes.

22. If you are not using either an HP or a LexMark printer, select one. Then, you may need to modify the control codes to work correctly with your printer.
23. Since there are many options for the barcode chip your printer supports, you may have to modify the codes that control the barcode. The names of the codes are: BLBC, EBLBC, SBT and EBT. If you were already using this printer to print barcodes, you can use the information in the fields BAR CODE ON (#60) and BAR CODE OFF (#61) from the TERMINAL TYPE file (#3.2) as a guide. If you were not, the barcode chip should have come with documentation showing the sequences necessary. If the documentation is not available, many printers have the ability to print the font set, with escape sequences, from the control panel of the printer.
24. The OneVA Pharmacy Patch PSO\*7\*454 introduced the OneVA Pharmacy label-generation functionality with new/updated label routines. The barcode printed on the OneVA Pharmacy label will contain the host site information where the prescription order originated not the dispensing site where the prescription is being filled.

Example Session:

\>D ^PSOLLU2

DEVICE: HOME// FIDO PRINTERS CORNER - LINE 000 Right Margin: 132//

HP or LexMark: L

You will be copying the CONTROL CODES to device: \_LTA9053: are you sure? Y Copying...

#### Sample Control Code Entries

The following are sample control code entries from one TERMINAL TYPE. Actual entries may vary depending on make and model of printer or barcode chip.

NUMBER: 1 CTRL CODE ABBREVIATION: LLI

FULL NAME: LASER LABEL INIT

CONTROL CODE: W \*27,"&r1F",\*27,"E",\*27,"&l0O",\*27,"&u300D",\*27,"&l3A",\*27,"&l0

E",!

NUMBER: 2 CTRL CODE ABBREVIATION: F10

FULL NAME: TEN POINT FONT - NO BOLD

CONTROL CODE: W \*27,"(10U",\*27,"(s1p10v0s0b16602X"

NUMBER: 3 CTRL CODE ABBREVIATION: F8

FULL NAME: EIGHT POINT FONT - NO BOLD

CONTROL CODE: W \*27,"(10U",\*27,"(s1p8v0s0b16602X"

NUMBER: 4 CTRL CODE ABBREVIATION: F12

FULL NAME: TWELVE POINT FONT - NO BOLD

CONTROL CODE: W \*27,"(10U",\*27,"(s1p12v0s0b16602X"

NUMBER: 5 CTRL CODE ABBREVIATION: F9

FULL NAME: NINE POINT FONT - NO BOLD

CONTROL CODE: W \*27,"(10U",\*27,"(s1p9v0s0b16602X"

NUMBER: 6 CTRL CODE ABBREVIATION: ST

FULL NAME: START OF TEXT

CONTROL CODE: S PSOY=PSOY+PSOYI W \*27,"\*p",PSOX,"x",PSOY,"Y"

NUMBER: 7 CTRL CODE ABBREVIATION: CDII

FULL NAME: CRITICAL DRUG INTERACTION INITIALIZATION

CONTROL CODE: S PSOX=0,PSOY=1400,PSOYI=50,PSOFONT="F10"

NUMBER: 8 CTRL CODE ABBREVIATION: PMII

FULL NAME: PMI SECTION INITIALIZATION

CONTROL CODE: S PSOX=0,PSOY=1350,PSOYI=50,PSOFONT="F10",PSOYM=3899

NUMBER: 12 CTRL CODE ABBREVIATION: ACI

FULL NAME: ADDRESS CHANGE INITIALIZATION

CONTROL CODE: S PSOHFONT="F12",PSOX=1210,PSOY=700,PSOFY=1270

NUMBER: 13 CTRL CODE ABBREVIATION: ALI

FULL NAME: ALLERGY SECTION INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOX=0,PSOY=1350,PSOYI=50,PSOYM=2700

NUMBER: 14 CTRL CODE ABBREVIATION: FWU

FULL NAME: FONT WITH UNDERLINE CONTROL CODE: W \*27,"&d0D"

NUMBER: 15 CTRL CODE ABBREVIATION: FDU

FULL NAME: FONT DISABLE UNDERLINE CONTROL CODE: W \*27,"&d@"

NUMBER: 17 CTRL CODE ABBREVIATION: SPI

FULL NAME: SUSPENSE PRINT INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOX=1210,PSOY=1350,PSOYI=50,PSOCX=1775,PSOYM=27

00

NUMBER: 18 CTRL CODE ABBREVIATION: WLI

FULL NAME: WARNING LABEL INITIALIZATION

CONTROL CODE: S PSOX=1050,PSOY=55

NUMBER: 19 CTRL CODE ABBREVIATION: RNI

FULL NAME: REFILL NARRATIVE INITIALIZATION

CONTROL CODE: S PSOY=2860,PSOFONT="F10",PSOX=0,PSOYI=50,PSOYM=3950

NUMBER: 20 CTRL CODE ABBREVIATION: CNI

FULL NAME: COPAY NARRATIVE INITIALIZATION

CONTROL CODE: S PSOY=2860,PSOX=1210,PSOYM=3950,PSOFONT="F10",PSOYI=50

NUMBER: 21 CTRL CODE ABBREVIATION: PII

FULL NAME: PATIENT INSTRUCTION INITIALIZATION

CONTROL CODE: S PSOX=1210,PSOY=760,PSOFONT="F12"

NUMBER: 22 CTRL CODE ABBREVIATION: RPI

FULL NAME: REFILL PRINT INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOBYI=65,PSOTYI=50,PSOLX=0,PSORX=1210,PSOY=1350

,PSOYM=3650,PSOXI=90,PSOSYI=135

NUMBER: 23 CTRL CODE ABBREVIATION: BLH

FULL NAME: BOTTLE LABEL HEADER INITIALIZATION

CONTROL CODE: S PSOX=100,PSOY=50,PSOYI=30,PSOFONT="F9"

NUMBER: 24 CTRL CODE ABBREVIATION: BLB

FULL NAME: BOTTLE LABEL BODY INITIALIZATION

CONTROL CODE: S PSOX=0,PSODX=275,PSOY=150,PSOYI=40,PSOYM=379,PSOFONT="F10"

NUMBER: 25 CTRL CODE ABBREVIATION: BLF

FULL NAME: BOTTLE LABEL FOOTER INITIALIZATION

CONTROL CODE: S PSODY=460,PSOX=0,PSOCX=280,PSOQY=550,PSOTY=610,PSOFONT="F10",P

SOQFONT="F8",PSODFONT="F9",PSOTFONT="F10"

NUMBER: 26 CTRL CODE ABBREVIATION: RT

FULL NAME: ROTATE TEXT CONTROL CODE: W \*27,"&a90P"

NUMBER: 27 CTRL CODE ABBREVIATION: NR

FULL NAME: NORMAL ROTATION CONTROL CODE: W \*27,"&a0P"

NUMBER: 28 CTRL CODE ABBREVIATION: PFDI

FULL NAME: PHARMACY FILL DOCUMENT INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOX=0,PSOY=700,PSOYI=40,PSOYM=969

NUMBER: 29 CTRL CODE ABBREVIATION: PFDQ

FULL NAME: PHARMACY FILL DOCUMENT QUANTITY

CONTROL CODE: S PSOX=0,PSOCX=200,PSOY=970,PSOYI=50,PSOQFONT="F8",PSOFONT="F10"

NUMBER: 31 CTRL CODE ABBREVIATION: AWI

FULL NAME: ALLERGY WARNING INITIALIZATION

CONTROL CODE: S PSOX=0,PSOY=1400,PSOYI=50,PSOFONT="F10"

NUMBER: 32 CTRL CODE ABBREVIATION: F6

FULL NAME: SIX POINT FONT - NO BOLD

CONTROL CODE: W \*27,"(10U",\*27,"(s1p6v0s0b16602X"

NUMBER: 33 CTRL CODE ABBREVIATION: EBT

FULL NAME: END OF BARCODE TEXT

CONTROL CODE: W \*27,"(8U",\*27,"(s1p8v0s0b16602T",!

NUMBER: 34 CTRL CODE ABBREVIATION: BLBC

FULL NAME: BOTTLE LABEL BARCODE

CONTROL CODE: W \*27,"(s1p10.4v4,12b4,12s24670T",\*27,"&a90P",\*27,"\*p3650x1000Y"

NUMBER: 35 CTRL CODE ABBREVIATION: PFDT

FULL NAME: PHARMACY FILL DOCUMENT TRAILER

CONTROL CODE: S PSOY=1015,PSOYI=45,PSOX=0,PSOFONT="F10",PSOBYI=50,PSOTFONT="F9

",PSOBY=1280

NUMBER: 36 CTRL CODE ABBREVIATION: EBLBC

FULL NAME: END OF BOTTLE LABEL BARCODE

CONTROL CODE: W \*27,"(10U",\*27,"(s1p10v0s0b16602T",\*27,"&a0P",!

NUMBER: 37 CTRL CODE ABBREVIATION: SBT

FULL NAME: START OF BARCODE TEXT

CONTROL CODE: S PSOY=PSOY+PSOYI W \*27,"\*p",PSOX,"x",PSOY,"Y",\*27,"(s1p14.4v6,1

8b6,18s24670T"

NUMBER: 43 ABBREVIATION: F6B

FULL NAME: SIX POINT FONT, BOLDED

CONTROL CODE: W \*27,"(10U",\*27,"(s1p6v0s3b16602T"

NUMBER: 44 ABBREVIATION: F8B

FULL NAME: EIGHT POINT FONT, BOLDED

CONTROL CODE: W \*27,"(10U",\*27,"(s1p8v0s3b16602T"

NUMBER: 45 ABBREVIATION: F9B

FULL NAME: NINE POINT FONT, BOLDED

CONTROL CODE: W \*27,"(10U",\*27,"(s1p9v0s3b16602T"

NUMBER: 46 ABBREVIATION: F10B

FULL NAME: TEN POINT FONT, BOLDED

CONTROL CODE: W \*27,"(10U",\*27,"(s1p10v0s3b16602T"

NUMBER: 47 ABBREVIATION: F12B

FULL NAME: 12 POINT FONT BOLDED

CONTROL CODE: W \*27,"(10U",\*27,"(s1p12v0s3b16602T"

NUMBER: 72 ABBREVIATION: PFI

FULL NAME: PATIENT FILL INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOX=1210,PSOY=710,PSOYI=45,PSOHFONT="F12",PSOBY

I=100

NUMBER: 73 ABBREVIATION: PFDW

FULL NAME: PHARMACY FILL DOCUMENT WARNING

CONTROL CODE: S PSOY=1258,PSOX=660,PSOYI=30,PSOFONT="F8",PSOYM=1329

NUMBER: 74 ABBREVIATION: MLI

FULL NAME: MAILING LABEL INITIALIZATION

CONTROL CODE: S PSOFONT="F10",PSOX=1680,PSOY=175,PSOYI=50

NUMBER: 75 ABBREVIATION: RMI

FULL NAME: RETURN MAIL INITIALIZATION

CONTROL CODE: S PSOHFONT="F8",PSOFONT="F10",PSOX=1680,PSOY=35,PSORYI=40,PSOHYI

=40,PSOTFONT="F8",PSOTY=550

NUMBER: 12172 CTRL CODE ABBREVIATION: LL

FULL NAME: LASER LABEL CONTROL CODE: Q

#### VMS Print Queue Setup

If you use VMS print queues, an additional setup may be necessary. The form for laser labels must have specific characteristics. If you need help defining the form, please contact the National Help Desk.

25. The form must have a length of 255 and a width of 512.

The following is an example form:

Form name Number Description

--------- ------ -----------

LABELFORM 2 LASER LABEL

/LENGTH=255 /MARGIN=(BOTTOM=6) /STOCK=LABELFORM /TRUNCATE /WIDTH=512

#### Control Codes

To modify the control codes to work appropriately with your device, use the following information.

Control Codes in use by Laser Labels:

ACI = ADDRESS CHANGE INITIALIZATION

ALI = ALLERGY SECTION INITIALIZATION

AWI = ALLERGY WARNING INITIALIZATION

BLB = BOTTLE LABEL BODY INITIALIZATION

BLBC = BOTTLE LABEL BARCODE

BLF = BOTTLE LABEL FOOTER INITIALIZATION

BLH = BOTTLE LABEL HEADER INITIALIZATION

CDII = CRITICAL DRUG INTERACTION INITIALIZATION

CNI = COPAY NARRATIVE INITIALIZATION

EBLBC = END OF BOTTLE LABEL BARCODE

EBT = END OF BARCODE TEXT

F10 = TEN POINT FONT - NO BOLD

F10B = TEN POINT FONT, BOLDED

F12 = TWELVE POINT FONT - NO BOLD

F12B = 12 POINT FONT BOLDED

F6 = SIX POINT FONT - NO BOLD

F6B = SIX POINT FONT BOLDED

F8 = EIGHT POINT FONT - NO BOLD

F8B = EIGHT POINT FONT BOLDED

F9 = NINE POINT FONT - NO BOLD

F9B = NINE POINT FONT BOLDED

FDU = FONT DISABLE UNDERLINE

FWU = FONT WITH UNDERLINE

LL = LASER LABEL

LLI = LASER LABEL INIT

MLI = MAILING LABEL INITIALIZATION

NR = NORMAL ROTATION

PFDI = PHARMACY FILL DOCUMENT INITIALIZATION

PFDQ = PHARMACY FILL DOCUMENT QUANTITY

PFDT = PHARMACY FILL DOCUMENT TRAILER

PFDW = PHARMACY FILL DOCUMENT WARNING

PFI = PATIENT FILL INITIALIZATION

PII = PATIENT INSTRUCTION INITIALIZATION

PMII = PMI SECTION INITIALIZATION

RMI = RETURN MAIL INITIALIZATION

RNI = REFILL NARRATIVE INITIALIZATION

RPI = REFILL PRINT INITIALIZATION

RT = ROTATE TEXT

SBT = START OF BARCODE TEXT

SPI = SUSPENSE PRINT INITIALIZATION

ST = START OF TEXT

WLI = WARNING LABEL INITIALIZATION

In addition to escape sequences to control printer output, variables are defined in the control codes that allow the routine to correctly position text and use the appropriate font.

The following is the description of the variables and their usage:

PSOX – X coordinate

PSOY – Y coordinate

PSOYI – Y increment, used to determine spacing between lines

PSOFONT – font size to be used. The font used is Arial.

PSOYM – bottom margin for this section

Some sections contain variables specific only to that section. They are as follows:

| Control Code | Variable                                      |
|--------------|-----------------------------------------------|
| MLI          | PSOHFONT – font for header lines              |
| ACI          | PSOHFONT – font for header lines              |
| RMI          | PSORYI – Y coordinate for return mail name    |
|              | PSOHYI – Y coordinate for header line         |
|              | PSOTFONT – font for trailer line              |
|              | PSOTY – Y coordinate for trailer line         |
| SPI          | PSOCX – X coordinate for date                 |
| RPI          | PSOBYI – Y increment for barcode              |
|              | PSOTYI – Y increment for trailer information  |
|              | PSOLX – X coordinate for left side of page    |
|              | PSORX – X coordinate for right side of page   |
|              | PSOSYI – Y increment for signature line       |
|              | PSOXI – X increment                           |
| BLB          | PSOBX – X coordinate for barcode              |
| BLF          | PSODY – Y coordinate for discard line         |
|              | PSOCX – X coordinate for continued line       |
|              | PSOQY – Y coordinate for quantity information |
|              | PSOTY – Y coordinate for trailer information  |
|              | PSOQFONT – font for quantity                  |
|              | PSODFONT – font for discard line              |
|              | PSOTFONT – font for trailer information       |
| PFDQ         | PSOCX – X coordinate for continued line       |
|              | PSOQFONT – font for quantity                  |
| PFDT         | PSOBYI – Y increment for barcode              |
|              | PSOTFONT – font for trailer information       |
|              | PSOBY – Y coordinate for barcode              |
| PFI          | PSOHFONT – font for header                    |
|              | PSOBYI – Y increment for barcode              |

<span id="_Toc207089097" class="anchor"></span>Table 22: Messages for the Dispense Request will consist of the following HL7 Segments

#### ScripTalk Printers

ScripTalk is a registered trademark of En-Vision America.

The Outpatient Pharmacy V. 7.0 package, with the release of PSO\*7\*135, supports the use of ScripTalk printers that print to microchip-embedded label stock. The label will have printed text on it, along with the microchip containing the contents of the label. Pharmacy or other designated staff will enroll patients to receive these labels and issue those patients a special reader. When the patient holds a ScripTalk label near the reader and presses a button, the content of the label is read aloud.

The ScripTalk label, released in 2003, has a 2K memory capacity, which limits the amount of prescription data that can be audibly read to the blind or low-vision Veteran using the system. New ScripTalk labels with 10K capacity are now available. Patch PSO\*7\*502 takes advantage of that capacity by sending more prescription data, including Drug Warnings, to the ScripTalk label.

The data sent to the ScripTalk label (either 2K or 10K), will now be controlled by one of two new parameters, depending on how your ScripTalk device definitions are set up. If they are set up at the system level using a mapped device, the dataset will be controlled by the new SCPIPTALK PRINTER TYPE SubField (#.03) in the SCRIPTALK PRINT DEVICE MAPPING SubFile (#59.747) of the PHARMACY SYSTEM File (#59.7), which patch PSS\*1.0\*217 introduces. If your ScripTalk device definition is set at the Outpatient Site level, the dataset will be controlled by the new SCRIPTRALK PRINTER TYPE Field (#107.2) in the OUTPATIENT SITE File (#59), which this patch introduces. Neither of these new fields will be populated upon patch install of PSO\*7\*502, and the software assumes a 2k dataset when either parameter is null.

The new ScripTalk 10K printers and labels are backward compatible with the 2K dataset. When a site upgrades to the new 10K equipment, once the hardware is set up and ready for implementation of the new 10K dataset, simply set the applicable parameter to 10K.

In addition, sites will now be able to control whether or not the non-ScripTalk label prints as voided or not voided. This will be in the OUTPATIENT SITE File (#59) and will be by division (outpatient site).

The TCP/IP-enabled printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files. To connect the printer to the network, a micro print server is necessary for communication to VistA. En-Vision America can assist in identifying the micro print server necessary for the site.

26. when using 10k printers make sure that the device is set up to use a Print Queue. If it is not then the 10k labels will not print.

The following are examples of the file set-ups. These examples are provided to guide the user in this set up. Please note that these are only examples and there will be some differences in the settings.

Example: DEVICE File (#3.5) Set Up for VMS Sites

NAME: WP706 \$I: USER\$:\[DSM_SPOOL\]WP706.TXT

LOCATION OF TERMINAL: ScripTalk ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO BARCODE AVAIL: YES

OPEN PARAMETERS: (NEWVERSION,PROTECTION=(S:RWED,O:RWED,W:RWED))

SUBTYPE: P-ZEBRA-PHARM

Example: DEVICE File (#3.5) Set Up for Cache Sites

NAME: WP706 \$I: PQ\$:WP706\$PRT.TXT

ASK DEVICE: YES ASK PARAMETERS: NO

TASKMAN PRINT A HEADER PAGE: NO SIGN-ON/SYSTEM DEVICE: NO

QUEUING: FORCED LOCATION OF TERMINAL:

1B-111/ScripTalk

ASK HOST FILE: NO ASK HFS I/O OPERATION: NO

SUPPRESS FORM FEED AT CLOSE: YES BARCODE AVAIL: YES

OPEN PARAMETERS: "NWS" SUBTYPE: P-ZEBRA-PHARM

TYPE: HOST FILE SERVER

PRINT SERVER NAME OR ADDRESS: xxxxx.xxxxxxxxx.xxx.xx.xxx

REMOTE PRINTER NAME: wp706

Example: TERMINAL TYPE File (#3.2) Set Up for VMS Sites

NAME: P-ZEBRA-PHARM SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 64 BACK SPACE: \$C(8)

CLOSE EXECUTE: U IO K IO(1,IO) S IO=\$ZIO C IO S

QUE="/QUEUE="\_\$E(ION,1,6)\_"/DELETE",QUE=\$ZC(%PRINT,IO,QUE)

NUMBER: 1 CTRL CODE ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION CONTROL CODE: W "^XA",!,"^LH30,60^FS",!

NUMBER: 2 CTRL CODE ABBREVIATION: SB

FULL NAME: START OF BARCODE

CONTROL CODE: W "^BY2,3.0^FO70,25^B3N,N,80,Y,N"

NUMBER: 3 CTRL CODE ABBREVIATION: ST

FULL NAME: START OF TEXT

CONTROL CODE: W "^FO",PSJBARX,",",PSJBARY,"^A0N,30,20" S PSJBARY=PSJBARY+40

NUMBER: 6 CTRL CODE ABBREVIATION: EB

FULL NAME: END OF BARCODE CONTROL CODE: S LINE=LINE+1,PSJBARY=130

NUMBER: 7 CTRL CODE ABBREVIATION: STF

FULL NAME: START OF TEXT FIELD CONTROL CODE: W "^FD"

NUMBER: 8 CTRL CODE ABBREVIATION: SBF

FULL NAME: START OF BARCODE FIELD CONTROL CODE: W "^FD"

NUMBER: 9 CTRL CODE ABBREVIATION: ETF

FULL NAME: END OF TEXT FIELD CONTROL CODE: W "^FS",!

NUMBER: 10 CTRL CODE ABBREVIATION: SL

FULL NAME: START OF LABEL

CONTROL CODE: W "^XA",! S PSJBARY=50,PSJBARX=60

NUMBER: 11 CTRL CODE ABBREVIATION: EL

FULL NAME: END OF LABEL CONTROL CODE: W "^XZ",!

NUMBER: 12 CTRL CODE ABBREVIATION: EBF

FULL NAME: END OF BARCODE FIELD CONTROL CODE: W "^FS",!

Example: TERMINAL TYPE File (#3.2) Set Up for Cache Sites

NAME: P-ZEBRA-PHARM SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 140 FORM FEED: \#

PAGE LENGTH: 64 BACK SPACE: \$C(8)

CLOSE EXECUTE: D CLOSE^NVSPRTU

NUMBER: 1 CTRL CODE ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION CONTROL CODE: W

"^XA",!,"^LH30,60^FS",!

NUMBER: 2 CTRL CODE ABBREVIATION: SB

FULL NAME: START OF BARCODE

CONTROL CODE: W "^BY2,3.0^FO70,25^B3N,N,80,Y,N"

NUMBER: 3 CTRL CODE ABBREVIATION: ST

FULL NAME: START OF TEXT

CONTROL CODE: W "^FO",PSJBARX,",",PSJBARY,"^A0N,30,20" S

PSJBARY=PSJBARY+40

NUMBER: 6 CTRL CODE ABBREVIATION: EB

FULL NAME: END OF BARCODE CONTROL CODE: S

LINE=LINE+1,PSJBARY=130

NUMBER: 7 CTRL CODE ABBREVIATION: STF

FULL NAME: START OF TEXT FIELD CONTROL CODE: W "^FD"

Example: TERMINAL TYPE File (#3.2) Set Up for Cache Sites (continued)

NUMBER: 8 CTRL CODE ABBREVIATION: SBF

FULL NAME: START OF BARCODE FIELD CONTROL CODE: W "^FD"

NUMBER: 9 CTRL CODE ABBREVIATION: ETF

FULL NAME: END OF TEXT FIELD CONTROL CODE: W "^FS",!

NUMBER: 10 CTRL CODE ABBREVIATION: SL

FULL NAME: START OF LABEL

CONTROL CODE: W "^XA",! S PSJBARY=50,PSJBARX=60

NUMBER: 11 CTRL CODE ABBREVIATION: EL

FULL NAME: END OF LABEL CONTROL CODE: W "^XZ",!

NUMBER: 12 CTRL CODE ABBREVIATION: EBF

FULL NAME: END OF BARCODE FIELD CONTROL CODE: W "^FS",!

Example: ScripTalk Device Definition Enter/Edit

CHOOSE 1-5: 4 PSO SCRIPTALK MAIN MENU ScripTalk Main Menu

PT ScripTalk Patient Enter/Edit

QBAR Queue ScripTalk Label by Barcode

QRX Queue ScripTalk Label by Rx#

RPT ScripTalk Reports ...

Reprint a non-voided Outpatient Rx Label

PARM Set Up and Test ScripTalk Device ...

Void Label Setup

Select ScripTalk Main Menu \<TEST ACCOUNT\> Option: PARM Set Up and Test ScripTal

k Device

ScripTalk Device Definition Enter/Edit

Print Sample ScripTalk Label

Test ScripTalk Device

Reinitialize ScripTalk Printer

Select Set Up and Test ScripTalk Device \<TEST ACCOUNT\> Option: SCRIPTalk Device

Definition Enter/Edit

Define ScripTalk Printer by (D)ivision or (P)rinter mapping?: (D/P): Division

Division: *\<enter your division\>*

SCRIPTALK DEVICE: SCRIPTALK 10K// \<enter your ScripTalk device\>

SCRIPTALK AUTO-PRINT SETTINGS: AUTO PRINT// ?

Enter 'A' if ScripTalk label printing should be automatic, "M" if label

will be queued manually.

Choose from:

A AUTO PRINT

M MANUAL PRINT

SCRIPTALK AUTO-PRINT SETTINGS: AUTO PRINT//

SCRIPTALK PRINTER TYPE: 10K LABEL// ?

Enter 2 if this ScripTalk printer is a 2K printer, enter 10 if this

ScripTalk printer is a 10K printer.

Choose from:

2 2K LABEL

10 10K LABEL

SCRIPTALK PRINTER TYPE: 10K LABEL//

Define ScripTalk Printer by (D)ivision or (P)rinter mapping?: (D/P): Printer

Select LABEL PRINTER TO BE MAPPED: *\<enter label printer\>*

SCRIPTALK DEVICE: SCRIPTALK 10K *\<ScripTalk device\>*

SCRIPTALK PRINTER TYPE: ?

Enter 2 if this ScripTalk printer is a 2K printer, enter 10 if this

ScripTalk printer is a 10K printer.

Choose from:

2 2K LABEL

10 10K LABEL

SCRIPTALK PRINTER TYPE:

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089098" class="anchor"></span>Table 23: Pharmacy Encoded Order / Treatment Dispense Message</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADP</td>
<td>Automated Data Processing</td>
</tr>
<tr class="even">
<td>Archive</td>
<td>Prescriptions, typically those that have been expired or canceled for more than a year, can be saved to tape, and then purged from online storage.</td>
</tr>
<tr class="odd">
<td>ASAP</td>
<td>American Society for Automation in Pharmacy</td>
</tr>
<tr class="even">
<td>BSA</td>
<td><p>Body Surface Area. The Dubois formula is used to calculate the Body Surface Area using the following formula:</p>
<p>BSA (m²) = 0.20247 x Height (m)<sup>0.725</sup><br />
x Weight (kg)<sup>0.425</sup></p>
<p>The equation is performed using the most recent patient height and weight values that are entered into the vitals package.</p>
<p>The calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td>Computerized Patient Record System. CPRS is a Graphical User Interface (GUI) in VistA that provides order entry and results reporting for multiple packages.</td>
</tr>
<tr class="even">
<td>CrCL</td>
<td><p>Creatinine Clearance. The CrCL value that displays in the pharmacy header is identical to the CrCL value calculated in CPRS. The formula approved by the CPRS Clinical Workgroup is the following:</p>
<p>Modified Cockcroft-Gault equation using Adjusted Body Weight in kg (if ht &gt; 60in)</p>
<p>This calculation is not intended to be a replacement for independent clinical judgment.</p></td>
</tr>
<tr class="odd">
<td>DEA</td>
<td>Drug Enforcement Agency</td>
</tr>
<tr class="even">
<td>DHCP</td>
<td>See VistA.</td>
</tr>
<tr class="odd">
<td>DOJ</td>
<td>Department of Justice</td>
</tr>
<tr class="even">
<td>eMI</td>
<td>Enterprise Messaging Services</td>
</tr>
<tr class="odd">
<td>eRx</td>
<td>ePrescription</td>
</tr>
<tr class="even">
<td>ESB</td>
<td>Enterprise Service Bus</td>
</tr>
<tr class="odd">
<td>Gene</td>
<td>A gene is a section of an individual’s DNA that provides instructions for making proteins, including those that affect how the body processes medications.</td>
</tr>
<tr class="even">
<td>Genotype</td>
<td>A genotype is a combination of alleles (version of a gene) which can influence how an individual processes medications.</td>
</tr>
<tr class="odd">
<td>HDR/CDS</td>
<td>Health Data Repository/Clinical Data Services</td>
</tr>
<tr class="even">
<td>IRMS</td>
<td>Information Resources Management Service</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td>International Standards Organization</td>
</tr>
<tr class="even">
<td>Non-VA Meds</td>
<td>Term that encompasses any Over-the-Counter (OTC) medications, Herbal supplements, Veterans Health Administration (VHA) prescribed medications but purchased by the patient at an outside pharmacy, and medications prescribed by providers outside VHA. All Non-VA Meds must be documented in patients’ medical records.</td>
</tr>
<tr class="odd">
<td>OneVA Pharmacy Label</td>
<td>Labels printed for traveling Veterans against prescriptions that originated from another VistA instance other than the site dispensing the prescription.</td>
</tr>
<tr class="even">
<td>OPAI</td>
<td>Outpatient Pharmacy Automated Interface</td>
</tr>
<tr class="odd">
<td>OSI</td>
<td>Open System Interconnection</td>
</tr>
<tr class="even">
<td>PDMP</td>
<td>Prescription Drug Monitoring Programs</td>
</tr>
<tr class="odd">
<td>PGx</td>
<td>Pharmacogenomic</td>
</tr>
<tr class="even">
<td>POE</td>
<td>Pharmacy Ordering Enhancements project. POE is a series of enhancements to improve the ordering processes between Inpatient Medications and Outpatient Pharmacy. For Outpatient Pharmacy, POE changes occur in patch PSO*7*46.</td>
</tr>
<tr class="odd">
<td>Prescription</td>
<td>This term is now referred to throughout the software as medication orders.</td>
</tr>
<tr class="even">
<td>Purge</td>
<td>Prescriptions, typically those that have been expired or canceled for more than a year, are saved to tape. Purging removes them from online storage.</td>
</tr>
<tr class="odd">
<td>Reprinted Label</td>
<td>Unlike a partial prescription, a reprint does not count as workload.</td>
</tr>
<tr class="even">
<td>SPMP</td>
<td>State Prescription Monitoring Program</td>
</tr>
<tr class="odd">
<td>VDEF</td>
<td>VistA Data Extraction Framework</td>
</tr>
<tr class="even">
<td>VDIF</td>
<td>Veterans Data Information Exchange</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans’ Health Administration</td>
</tr>
<tr class="even">
<td>VHIC</td>
<td>Veterans’ Health Identification Card</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).</td>
</tr>
<tr class="even">
<td>VUID</td>
<td>VHA Unique Identifier. A unique integer assigned to reference terms VHA wide.</td>
</tr>
</tbody>
</table>
<span id="_Toc207089098" class="anchor"></span>Table 23: Pharmacy Encoded Order / Treatment Dispense Message

## Appendix A: Outpatient Pharmacy HL7 Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A. General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

This document specifies an interface between the VistA Outpatient Pharmacy V. 7.0 application and any automatic dispensing system. It is based upon the Health Level 7 Standard (HL7) V. 2.4.

The term “Level 7” refers to the highest level of the Open System Interconnection (OSI) model of the International Standards Organization (ISO). The OSI model is divided into seven levels or layers. The HL7 Standard is primarily focused on what happens within the seventh or application layer. At this layer, the definitions of the data to be exchanged, the timing of the exchanges, and the communication of certain application specific errors occurs. The lower levels support the actual movement of data between systems.

The high-level communication requirements for this interface include TCP/IP, HL7 Logical link and bi-directional communications for the BusinessWare server at the VAMC. BusinessWare will support MLLP connection.

#### Message Rules

The HL7 Standard describes the basic rules for the exchange of information between two computer systems. The unit of data transferred is referred to as the message. It is comprised of a group of segments in a defined sequence. Each message has a three-character code called a message type that defines its purpose. The real-world event that initiates an exchange of messages is called a trigger event. There is a one-to-many relationship between message types and trigger event codes. A message type may be associated with more than one trigger event, but the same trigger event code may not be associated with more than one message type. All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.

Some special characters are used to construct messages. They are the segment terminator, field separator, component separator, sub-component separator, repetition separator, and escape character. The segment terminator is always a carriage return (CR in ASCII or hex OD). The other characters recommended by HL7 are used in this application (See HL7 Standard V. 2.4, Chapter 2 for details).

#### Segment Rules

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message, or they may be allowed to repeat. Each segment is given a name and is identified by a unique three-character code. All segments beginning with Z are reserved for locally defined messages. No such code will be defined within the HL7 Standard.

#### Field Rules

A field is a string of characters. HL7 does not care how systems actually store data within an application. Except where noted, HL7 data fields may take on the null value. Sending the null value, which is transmitted as two double quote marks (""), is different from omitting an optional data field. The difference appears when the contents of a message will be used to update a record in a database rather than create a new one. If no value is sent (i.e., it is omitted) the old value should remain unchanged. If the null value is sent, the old value should be changed to null. In defining a segment, the following information is specified about each field:

1.  position - position of the data field within the segment.
2.  name - unique descriptive name for the field.
3.  ID number - integer that uniquely identifies the data field throughout the Standard.
4.  maximum length - maximum number of characters that one occurrence of the data field may occupy.
5.  optionality - whether the data field is required (R), optional (O), or conditional (C) in a segment.
6.  repetition - whether the field may repeat (N=no; Y=yes; (integer)= no. of repeats).
7.  table - a table of values for a field (See HL7 Standard V. 2.4, Section 2.7.6 for source of tables).
8.  data type - restrictions on the contents of the data field (See HL7 Standard V. 2.4, Section 2.9).

#### Special Escaping Characters

Standard HL7 field delimiters represented by the “~ , &, \| ” (tilde, ampersand, pipe) characters, as well as the commonly used VistA “^” (caret), are sometimes needed by users of Outpatient Pharmacy in various fields to provide complete information about a patient or order. The use of these characters can cause sending and receiving software to format HL7 messages incorrectly, construct / deconstruct the information, or both incorrectly. Data loss can also occur if data is truncated at one of the special delimiter characters.

The following fields require special escaping characters.

- Dosage Ordered field – RXE segment / piece 1 / subpiece 1
- Schedule field – RXE segment / piece 1 /subpiece 2
- VA Product Name field – RXE segment / piece 2 / subpiece 2 
- Generic drug name field – RXE segment / piece 2 / subpiece 6
- Units name field – RXE segment / piece 5 / subpiece 5
- Dose Form name field – RXE segment / piece 6 / subpiece 5
- Provider Comments field – NTE 6 segment / piece 3
- Expanded Patient Sig field – NTE 7 segment / piece 3
- Front Door Sig field – NTE 21 segment / piece 3
- Back Door Sig field – NTE 21 segment / piece 3

### B. Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Communication Protocol

The lower level communication protocol used by Outpatient Pharmacy V. 7.0 to transmit data between systems is either X3.28 or HLLP over an RS-232 connection.

A site parameter in the Outpatient Pharmacy V. 7.0 application called External Interface controls transmission of data to the dispensing machine. If the parameter is set to 0, no transmission will occur.

There is also a new parameter that is used for sites running HL7 V.2.4. It is in the OUTPATIENT SITE file (#59) and is called AUTOMATED DISPENSE. This must be set to determine which version of HL7 the site is running.

#### Processing Rules

A Pharmacy Encoded Order Message is transmitted whenever an order is placed in Outpatient Pharmacy V. 7.0 and the criteria are met for the dispensing machine. Upon successful receipt and storage of the message, the dispensing machine will generate and transmit a Pharmacy Encoded Order Acknowledgement Message.

| RDS | Pharmacy Encoded Order / Treatment Dispense Message |
|-----|-----------------------------------------------------|
| RRD | Pharmacy Encoded Order Ack. Message                 |
| ACK | General Ack. Message                                |

<span id="_Toc207089099" class="anchor"></span>Table 24: Pharmacy Encoded Order Acknowledgment Message

| IAM | Patient Adverse Reaction Information   |
|-----|----------------------------------------|
| MSH | Message Header                         |
| NTE | Notes and Comments                     |
| PID | Patient Identification                 |
| PV1 | Patient Visit                          |
| PV2 | Patient Visit – additional information |
| ORC | Common Order                           |
| RXE | Pharmacy/Treatment Encoded Order       |
| RXD | Pharmacy/Treatment Dispense            |
| RXR | Pharmacy/Treatment Route               |

<span id="_Toc207089100" class="anchor"></span>Table 25: Segments used in the Outpatient Pharmacy HL7 interface Dispense Request

#### Specific Transaction – Dispense Request

| RDS     | Pharmacy Encoded Order / Treatment Dispense Message |
|---------|-----------------------------------------------------|
| MSH     | Message Header                                      |
| \[PID\] | Patient Identification                              |
| \[PV1\] | Patient Visit                                       |
| \[PV2\] | Patient Visit – additional information              |
| {IAM}   | Patient Adverse Reaction Information                |
| {ORC    | Common Order                                        |
| {NTE}   | Notes and Comments                                  |
| RXE     | Pharmacy/Treatment Encoded Order                    |
| RXD     | Pharmacy/Treatment Dispense                         |
| {NTE}   | Notes and Comments (contains PMI)                   |
| {RXR}   | Pharmacy/Treatment Route                            |
| ZZZ     | Hazardous Drug Information                          |
| }       |                                                     |

<span id="_Toc207089101" class="anchor"></span>Table 26: Segments used in the Outpatient Pharmacy HL7 interface Dispense Release Date / Time Request

Example:

MSH\|^~\\\|PSO VISTA\|521^OUTPATIENT\|PSO DISPENSE\|521\|20030620125043\|\|RDS^O13^RDS_O13\|10001\|P\|2.4\|\|\|AL\|AL

PID\|\|\|5000002199V009321\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20140212^234234987\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~TIN~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~FIN~VA FACILITY ID&500&L^7172676\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|333888478\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L^492994922\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L\|PSOPATIENT~MULTIPLE\~~RX\~\~~L\|\|19111111\|M\|\|\|123 MAIN ST~""~ANY TOWN ONE~CA~94114~USA~P~""~075^\~~ ANY TOWN TWO~CA\~\~~N\|\|(555)555-5555~PRN~PH\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

PV1\|\|O

PV2\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|SCL50~NO COPAY

IAM\|\|D^Drug^LGMR120.8\|128^ASPIRIN^LGMR120.8\|SV\|ALLERGY\|\|\|\|\|\|\|\|19961205\|\|\|\|C

ORC\|NW\|116211~OP7.0\|\|\|\|\|\|\|20131204\|2438~ OPPROVIDER~TWO \|\|2438~OPPROVIDER~TWO\|NULL\|\|20131204\|REPRINT\|0~UNKNOWN~99PSC\|\|\|VA5\|ALBANY ISC\~~500\|5400 LEGACY DR\~~1000~TX~75024\|(555)555-5555

NTE\|1\|\|ONE TAKE MOUTH TAKE\|Medication Instructions

NTE\|3\|\|May cause drowsiness. Alcohol may intensify this effect. Use care when operating a car or dangerous machines.\\sp\May cause dizziness\\sp\It is very important that you take or use this exactly as directed. Do not skip doses or discontinue unless directed by your doctor.\|Drug Warning Narrative

RXE\|""""\|R0009~RESERPINE 0.1MG TAB~99PSNDF~57.586.222~RESERPINE 0.1MGS.T.~99PSD\|\|\|20~MG~99PSU\|1~AEROSOL~99PSF\|\|""""\|\|3\|~\|3\|\|\~~\|104822\|3\|0\|\|\|\|~RESERPINE 0.1MG S.T.^~RESERPINE 0.1MG TAB\|\|\|\|\|\|\|\|\|\|N^0^N

RXD\|3\|D0082^DIGOXIN 0.25MG TAB^99PSNDF^372.3^DIGOXIN 0.25MG TAB^99PSD\|20030610\|\|\|\|100001351\|3\|~6P~6505-00-584-0398\|157^OPPROVIDER^TWO\|\|30\|CERTIFIED MAIL\|\|^NON-SAFETY\|\|\|\|20040615

NTE\|PMI\|\|CORTICOSTEROIDS - ORAL\|Patient Medication Instructions

RXR\|6^Oral^99PSR

ZZZ\|\|\|\|N\|N

| RRD | Pharmacy Encoded Order Ack. Message |
|-----|-------------------------------------|
| MSH | Message Header                      |
| MSA | Message Acknowledgement             |

<span id="_Toc207089102" class="anchor"></span>Table 27: Segments used in the Outpatient Pharmacy HL7 interface Dispense Completion

Example:

MSH\|~^\\\|PSO DISPENSE\|BP-CHEYENNE\|PSO VISTA\|BP-CHEYENNE\|20040227222454-0500\|\|ACK\|4425981296\|T\|2.4\|\|

MSA\|AA\|10001

#### Active Veteran's Health Information Card (VHIC) Numbers Added to PID-4 Segment

Sites that use the Outpatient Pharmacy Automated Interface (OPAI) interface and COTS products, such as ScriptPro and OptiFill, rely on patient identifying information contained in the PID segment of HL7 messages. The new Veteran's Health Information Card (VHIC) no longer contains the patient's Social Security Number (SSN). Patch PSO\*7\*434 utilized Patch DG\*5.3\*874 to include the current *active* VHIC card numbers in the HL7 PID-4 component, providing an interoperability between the barcode on the VHIC card and data in the HL7 PID segment. As of Patch PSO\*7\*434, the *<u>active</u>* VHIC number(s) were added to the list of identifiers in the PID Segment in sequence PID-4.

27. The changes in HL7 message generated by OPAI are tested with ScriptPro and OptiFill, only. Sites using other vendors are requested to inform them of the changes, so that they can make necessary changes to ensure smooth running of interface at their sites.

Example:

\[VHIC Card \#\]\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L

The following example shows an *active* VHIC number repeated twice in PID-4 for interoperability between DoD and VA because this patient has two *<u>active</u>* VHIC numbers.

Example:

PID\|\|\|5000002199V009321\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20140212^234234987\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~TIN~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~FIN~VA FACILITY ID&500&L^7172676\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|333888478\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L^492994922\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L\|PSOPATIENT~MULTIPLE\~~RX\~\~~L\|\|19111111\|M\|\|\|123 MAIN ST~""~ANY TOWN ONE~CA~94114~USA~P~""~075^\~~ ANY TOWN TWO~CA\~\~~N\|\|(555)555-5555~PRN~PH\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

<table>
<caption><p><span id="_Toc207089103" class="anchor"></span>Table 28: HL7 Order Message Segment</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>SEGMENT</th>
<th>SEQ#</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>EXAMPLE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MSH</td>
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>|</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td>~^\&amp;</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0361</td>
<td>Sending Application</td>
<td>PSO VISTA</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0362</td>
<td>Sending Facility – station ID and station DNS name</td>
<td>521~XXXXXXX.XXX.XX.XXX~DNS</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0361</td>
<td>Receiving Application</td>
<td>PSO DISPENSE</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0362</td>
<td>Receiving Facility – DNS name and port of dispensing machine</td>
<td>~XXXXXXXX.XXX.XXX.XX.XXX:####~DNS</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time of Message</td>
<td>20040405152416</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>15</td>
<td>CM</td>
<td>R</td>
<td>0076</td>
<td></td>
<td>Message Type</td>
<td>RDS~013</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>10001</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>3</td>
<td>PT</td>
<td>R</td>
<td>0103</td>
<td></td>
<td>Processing ID</td>
<td>P</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>3</td>
<td>VID</td>
<td>R</td>
<td>0104</td>
<td></td>
<td>Version ID</td>
<td>2.4</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Ack. Type</td>
<td>AL</td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Ack Type</td>
<td>AL</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PID</td>
<td>3</td>
<td>250</td>
<td>CX</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (will contain IEN, SSN, ICN, Claim #, etc., if exists)</td>
<td>218~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;500&amp;L</td>
</tr>
<tr class="even">
<td>PID</td>
<td>4</td>
<td>250</td>
<td>CX</td>
<td></td>
<td></td>
<td></td>
<td>Active Veteran’s Health Identification Card (VHIC) number(s)</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>250</td>
<td>XPN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>OPPATIENT~ONE</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date/Time of Birth</td>
<td>19280622</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>0001</td>
<td>Administrative Sex</td>
<td>M</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>250</td>
<td>XAD</td>
<td>R</td>
<td>Y/3</td>
<td></td>
<td>Patient Address</td>
<td>164 Friendship DR~""~TROY~NY~12180~~P~""</td>
</tr>
<tr class="odd">
<td></td>
<td>13</td>
<td>250</td>
<td>XTN</td>
<td>R</td>
<td>Y/3</td>
<td></td>
<td>Phone Number-Home</td>
<td>(555)555-5555</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PV1</td>
<td>2</td>
<td>1</td>
<td>IS</td>
<td>R</td>
<td></td>
<td>0004</td>
<td>Patient Class</td>
<td>O for Outpatient</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PV2</td>
<td>24</td>
<td>15</td>
<td>IS</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient Status Code</td>
<td>SC~NO COPAY</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>IAM</td>
<td>2</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0127</td>
<td>Allergen Type Code</td>
<td>D~DRUG~LGMR120.8</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Allergen Code/Mnemonic/Description</td>
<td>128~ASPIRIN~LGMR120.8</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0128</td>
<td>Allergy Severity Code</td>
<td>SV</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>15</td>
<td>ST</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Allergy Reaction Code</td>
<td>ALLERGY</td>
</tr>
<tr class="odd">
<td></td>
<td>13</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Reported Date/Time</td>
<td>19961205</td>
</tr>
<tr class="even">
<td></td>
<td>17</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0438</td>
<td>Allergy Clinical Status Code</td>
<td>C</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>1</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0119</td>
<td>Order Control</td>
<td>NW</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>80</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>Placer Order Number</td>
<td>402331~OP7.0</td>
</tr>
<tr class="odd">
<td></td>
<td>9</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Date/Time of Transaction</td>
<td>20040405</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td></td>
<td></td>
<td>Entered By</td>
<td>10~OPPROVIDER~TWO</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordering Provider</td>
<td>987~OPPROVIDER~ONE</td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>Enterer’s Location</td>
<td>_TNA1225:</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Order Effective Date</td>
<td>20030616</td>
</tr>
<tr class="even">
<td></td>
<td>16</td>
<td>10</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Order Control Code Reason</td>
<td>NEW</td>
</tr>
<tr class="odd">
<td></td>
<td>17</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Entering Organization</td>
<td>57~7<sup>TH</sup> FLOOR~99PSC</td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Action By</td>
<td>65421~OPPROVIDER5~THREE</td>
</tr>
<tr class="odd">
<td></td>
<td>20</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0339</td>
<td>Advanced Beneficiary Notice Code</td>
<td>VA5</td>
</tr>
<tr class="even">
<td></td>
<td>21</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordering Facility Name</td>
<td>AL BANY~~500</td>
</tr>
<tr class="odd">
<td></td>
<td>22</td>
<td>250</td>
<td>XAD</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordering Facility Address</td>
<td>101 CHURCH AVE~~ALBANY~NY~12208</td>
</tr>
<tr class="even">
<td></td>
<td>23</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordering Facility Phone #r</td>
<td>(518)555-5554</td>
</tr>
<tr class="odd">
<td><span id="OLE_LINK3" class="anchor"></span></td>
<td>30</td>
<td>250</td>
<td>CNE</td>
<td>O</td>
<td>1</td>
<td>0483</td>
<td>Enterer Authorization Mode</td>
<td>EL</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>NTE</td>
<td>1</td>
<td>1</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>Set ID</td>
<td>1</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>65536</td>
<td>FT</td>
<td>O</td>
<td></td>
<td></td>
<td>Comment</td>
<td>USE 50 FOR TESTING BY MOUTH TWICE A DAY FOR 30 DAYS</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>250</td>
<td>RE</td>
<td>O</td>
<td></td>
<td></td>
<td><p>Comment Type –</p>
<p>1 = Medication Instructions</p>
<p>2 = Patient Instructions Narrative</p>
<p>3 = Drug Warning Narrative</p>
<p>4 = Profile Information</p>
<p>5 = Drug Interactions</p>
<p>6 = Drug Allergy Indications</p>
<p>7 = PMI Sheet</p>
<p>8 = Medication Instructions</p>
<p>9 = Privacy Notification</p></td>
<td><p>Medication Instructions</p>
<p><strong>NOTE</strong>: The separator value “\.sp\” has been added to NTE-3, 3 = Drug Warning Narrative, to separate the different warning labels.</p></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>1</td>
<td>200</td>
<td>TQ</td>
<td>R</td>
<td></td>
<td></td>
<td>Quantity/Timing</td>
<td>Null</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Give Code</td>
<td>XH001~HEMATEST TAB (NOT FOR ORAL USE)~99PSNDF~3207.12039.4321~HEMATEST REAGENT TAB. 100/BTL~99PSD</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>20</td>
<td>NM</td>
<td>R</td>
<td></td>
<td></td>
<td>Give Amount-Minimum</td>
<td>Null</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Give Units</td>
<td>20~MG~99PSU</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Give Dosage Form</td>
<td>165~TAB,TEST~99PSF</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>200</td>
<td>CM</td>
<td>O</td>
<td></td>
<td></td>
<td>Deliver-To Location</td>
<td>WINDOW</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Substitution Status</td>
<td>(Trade name)</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispense Amount</td>
<td>30</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispense Units</td>
<td>~TAB</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Number of Refills</td>
<td>3</td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Ordering Provider’s DEA Number</td>
<td>EZ9278277</td>
</tr>
<tr class="odd">
<td></td>
<td>14</td>
<td>250</td>
<td>XCN</td>
<td>C</td>
<td></td>
<td></td>
<td>Pharmacist/Treatment Supplier’s Verifier ID</td>
<td>188~OPPROVIDER3~ONE</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Prescription Number</td>
<td>100002202</td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Number of Refills Remaining</td>
<td>3</td>
</tr>
<tr class="even">
<td></td>
<td>17</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Number of Refills/Doses Dispensed</td>
<td>0</td>
</tr>
<tr class="odd">
<td></td>
<td>18</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>D/T of Most Recent Refill</td>
<td>200404050830</td>
</tr>
<tr class="even">
<td></td>
<td>21</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td><p>Pharmacy/treatment</p>
<p>dispense instructions</p></td>
<td><p>^IBUPROFEN</p>
<p>400MG TAB</p></td>
</tr>
<tr class="odd">
<td></td>
<td>31</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td></td>
<td>Supplementary Code = spec hdlg, ScripTalk, PMI language preference</td>
<td>N^0^N</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RXD</td>
<td>1</td>
<td>10</td>
<td>NM</td>
<td>R</td>
<td></td>
<td></td>
<td>Dispense Sub-ID Counter</td>
<td>0</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Dispense/Give Code</td>
<td>XH001~HEMATEST TAB (NOT FOR ORAL USE)~99PSNDF~3207.12039.4321~HEMATEST REAGENT TAB. 100/BTL~99PSD</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date/Time Dispensed</td>
<td>20040405</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Prescription Number</td>
<td>100002202</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>Number of Refills Remaining</td>
<td>3</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispense Notes – DEA spec hdlg, NDC code</td>
<td>S^193-2426-21</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>200</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispensing Provider</td>
<td>157~OPPROVIDER~TWO</td>
</tr>
<tr class="even">
<td></td>
<td>12</td>
<td>10</td>
<td>CQ</td>
<td>O</td>
<td></td>
<td></td>
<td>Total Daily Dose</td>
<td>30</td>
</tr>
<tr class="odd">
<td></td>
<td>13</td>
<td>200</td>
<td>CM</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispense-To Location</td>
<td>CERTIFIED MAIL</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>10</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Pharmacy/Treatment Supplier’s Special Dispensing Instructions</td>
<td>~NON-SAFETY</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Substance Expiration Date</td>
<td>20040615</td>
</tr>
<tr class="even">
<td></td>
<td>25</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Supplementary Code</td>
<td>8~NO ALCOHOL</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NTE</td>
<td>1</td>
<td>4</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>Set ID-Notes and Comments</td>
<td>7</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>6000</td>
<td>FT</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Comment</td>
<td>PMI free text</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Comment Type – P MI</td>
<td><p>Patient Medication Instructions</p>
<p><strong>NOTE</strong>: The separator value “\.sp\” has been added to NTE-3, 3 = Drug Warning Narrative, to separate the different warning labels.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>RXR</td>
<td>1</td>
<td>250</td>
<td>CE</td>
<td></td>
<td></td>
<td>0162</td>
<td>Route</td>
<td>1~ORAL (BY MOUTH)~99PSR</td>
</tr>
<tr class="odd">
<td>ZZZ</td>
<td>4</td>
<td>1</td>
<td>TX</td>
<td>R</td>
<td></td>
<td>0136</td>
<td>Hazardous to Handle Indicator</td>
<td><p>Y</p>
<p>(Data Value is either Y or N)</p></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>1</td>
<td>TX</td>
<td>R</td>
<td></td>
<td>0136</td>
<td>Hazardous to Dispose Indicator</td>
<td><p>N</p>
<p>(Data Value is either Y or N)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207089103" class="anchor"></span>Table 28: HL7 Order Message Segment

Notes pertaining to some of the data elements:

\[MSH-3\] Sending Application is the station ID along with the DNS name of the sending facility.

\[MSH-5\] Receiving Application is the DNS name and DNS port number of the dispensing application.

\[MSH-10\] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

\[PID-3\] Patient ID will contain the following possibilities to identify a patient:

- NI = ICN \#
- SS = Social Security \#
- PN = Claim \#
- PI = DFN \#

\[PID-4\] Alternate Patient ID will contain the active Veteran’s Health Identification Card (VHIC) number(s) to identify a patient.

\[PID-11\] Patient Address

The PID-11 segment contains the following data:

- Patient Permanent Address 1<sup>st</sup> up-arrow piece
- Patient Place of Birth (City & State) 2<sup>nd</sup> up-arrow piece
- Confidential Address 3<sup>rd</sup> up-arrow piece if it is Active

> If Confidential Address is Active, for each Confidential Address Category, an entry will be made into the HL7 record starting in the up-arrow piece 3.

- Patient Temporary Address 3<sup>rd</sup> up-arrow piece or piece after the last Confidential Address entry if the Confidential Address is active.

PID\|\|\|\|Permanent Address^Place of Birth^Temporary Address\|\|\|\|

\[PID-11\] Patient Permanent Address

When the <u>permanent</u> address is active, it is the only address in PID-11

Example: 321 Dakota Ave.~""~WASHINGTON~DC~20032~USA~P~""~001

\[PID-11\] Patient Confidential Address

When the <u>confidential</u> address is active, both the confidential and permanent addresses are located in PID-11.

\[PID-11\] Patient Temporary Address

When the <u>temporary</u> address is active, both the temporary and permanent addresses are located in PID-11.

> Example: 100 PERMANENT ADDRESS~""""~NEW YORK~NY~10018~USA~P~""""~061^\~~SAN ANTONIO~TX\~\~~N^1 CONFIDENTIAL STREET~""""~NEW YORK~NY~10019~USA~VACAE~""""~061\~\~~20160628&20160718^1 CONFIDENTIAL STREET~""""~NEW YORK~NY~10019~USA~VACAA"

> ^HL(772,35537819,"IN",3,0)="~""""~061\~\~~20160628&20160718^1 CONFIDENTIAL STREET~""""~NEW YORK~NY~10019~USA~VACAM~""""~061\~\~~20160628&20160718^200 TEMPROARY ADDRESS~""""~NEW YORK~NY~10017~USA~C

\[PID-11\] If the BAD ADDRESS INDICATOR (BAI) field (#.121) of the PATIENT file (#2) is set, the text “VAB” concatenated with the BAI code is sent in the Address field of the PID segment of the HL7 message to the filling equipment.

Example: Permanent address – active:

> PADD-1~PADD-2~SPRING~TX~77379\~~P~PADD-3~201^\~~""~""\~\~~N\|""\|\|\|\|\|\|\|\|

Example: Confidential address – active:

> PADD-1~PADD-2~SPRING~TX~77379\~~P~PADD-3~201^\~~""~""\~\~~N^1 CONFIDENTIAL STREET~""""~NEW YORK~NY~10019~USA~VACAM~

Example: Temporary address – active:

> PADD-1~PADD-2~SPRING~TX~77379\~~P~PADD-3~201^\~~""~""\~\~~N^TADD-1~TADD-2

> TADD-3~PLANO~TX~12345\~~C\~~""\~\~~

Example: Address flagged as BAI:

> PADD-1~PADD-2~SPRING~TX~77379\~~VAB1~PADD-3~201^\~~""~""\~\~~N\|""\|\|\|\|\|\|\|\|\|

> "VAB1" - indicates Bad Address Indicator and 1 is for UNDELIVERABLE (2 for

> HOMELESS, 3 for OTHER)

28. For each Active Confidential Address Category entered for the patient, an entry will be made into the HL7 record delimited by ^.

The code is looping down the Confidential Address Categories and creating an entry for each one.

category=1 (ELIGIBILITY/ENROLLMENT): VACAE

category=2 (APPOINTMENT/SCHEDULING): VACAA

category=3 (COPAYMENTS/VETERAN BILLING): VACAC

category=4 (MEDICAL RECORDS): VACAM

category=5 (ALL OTHERS): VACAO

otherwise= null

The “C” is hardcoded after USA (the country) on the Temporary Address record.

The vendor will need to read through the addresses (^ pieces) until it finds the C in the 7th ~ piece of data for a temporary address.

The following determines whether to send the Temporary Address.

It first checks the TEMPORARY ADDRESS ACTIVE? flag, if set to Yes then checks the TEMPORARY ADDRESS START DATE against the processing date range start date and if passes then checks the TEMPORARY ADDRESS END DATE against the processing date range end date. If these pass, then the Temporary Address is sent in the HL7 record.

There can be up to 5 Confidential address entries (one for each active Confidential Address Category) , 1 Permanent address and 1 Temporary address.

Below is an example of a PID-11 segment with all 7 addresses populated.

^HL(772,35537804,"IN",0)="^^241^241^3160628^"

^HL(772,35537804,"IN",1,0)="PID\|\|\|1004459532V886809\~\~~USVHA&&0363~NI~VA FACILITY

ID&200M&L^101017111\~\~~USSSA&&0363~SS~VA FACILITY ID&442&L^""""\~\~~USDOD&&0363~TI

N~VA FACILITY ID&442&L^""""\~\~~USDOD&&0363~FIN~VA FACILITY ID&442&L^7187158\~\~~USV

HA&&0363~PI~VA FACILITY ID&442&L\|"

^HL(772,35537804,"IN",2,0)="\|last~name~M\~\~\~~L\|\|19710313\|F\|\|\|100 PERMANENT ADDR

ESS~""""~NEW YORK~NY~10018~USA~P~""""~061^\~~SAN ANTONIO~TX\~\~~N^1 CONFIDENTIAL ST

REET~""""~NEW YORK~NY~10019~USA~VACAE~""""~061\~\~~20160628&20160718^1 CONFIDENTIA

L STREET~""""~NEW YORK~NY~10019~USA~VACAA"

^HL(772,35537804,"IN",3,0)="~""""~061\~\~~20160628&20160718^1 CONFIDENTIAL STREET~

""""~NEW YORK~NY~10019~USA~VACAC~""""~061\~\~~20160628&20160718^1 CONFIDENTIAL STR

EET~""""~NEW YORK~NY~10019~USA~VACAM~""""~061\~\~~20160628&20160718^1 CONFIDENTIAL

STREET~""""~NEW YORK~NY~10019~USA~VACAO~"""""

^HL(772,35537804,"IN",4,0)="~061\~\~~20160628&20160718^200 TEMPROARY ADDRESS~""""~

NEW YORK~NY~10017~USA~C~""""~061\~\~~20160623&20160802\|\|(222)222-2222~PRN~PH^(111)

111-1111~WPN~PH\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|"

\[PV1-2\] Patient Class is hard-coded to an O for outpatient.

\[PV2-24\] Patient Status Code contains the patient status from the prescriptions file followed by a tilde and then whether or not the patient is COPAY.

\[IAM-2\] Allergen Type Code is the allergy type of F=Food, DF=Drug/Food, D=Drug, DP=Drug/Other, O=Other, DFO=Drug/Food/Other.

\[IAM-5\] Allergy Reaction Code will contain the possible reactions ALLERGY, PHARMACOLOGIC or UNKNOWN.

\[IAM-17\] Allergy Clinical Status Code is VERIFIED or NON-VERIFIED.

\[ORC-2\] Placer Order Number is a composite field. The first component is the IEN from the PRESCRIPTION file (#52). The second component is hard-coded to a value of OP7.0.

\[ORC-10\] Entered By is the person’s pointer to the NEW PERSON file (#200) and name in VistA who keyed in the order.

\[ORC-12\] Ordering Provider is a composite ID field. The first component is the Provider’s pointer to the NEW PERSON file (#200) in VistA and the second component is his/her name.

\[ORC.13\] Enterer’s Location is the printer where the dispensing machine should print the label.

\[ORC-15\] Order Effective Date is the date/time the order took effect.

\[ORC-16\] Order Control Code Reason is a coded element field. The fifth component reflects the status of the order (for example, New, Refill, Partial, Reprint, or Partial Reprint).

\[ORC-17\] Entering Organization is the Clinic number and name.

\[ORC-19\] Action By is the physician who cosigned, if any, and is a composite field. The first component is the physician’s pointer to the NEW PERSON file (#200) in VistA and the second component is his/her name.

\[ORC-20\] Advanced Beneficiary Notice Code is used to send an indicator to an automated dispensing system that the RX being dispensed is for an electronically billed prescription and that a patient signature is needed. The value of “VA5” will be sent as the indicator in the RDS^O13 Dispense Request message for an ePharmacy patient prescription.

\[ORC-21\] Ordering Facility Name is the facility name and number found in the OUTPATIENT SITE file (#59).

<span id="orc30" class="anchor"></span>\[ORC-30\] Enterer Authorization Mode is passed for digitally signed controlled substance orders. The value of ‘EL’ is used, representing a value of ‘Electronic’.

\[NTE\] The Set ID field will identify the NTE segment (1=Med. Instructions; 2=Patient Instructions Narrative; 3=Drug Warning Narrative; 4=Profile Information; 5=Drug Interactions; 6=Drug Allergy Indications; 7=PMI Sheet; 8=Medication Instructions; 9=Privacy Notification.) The Comment field will contain the respective information.

29. The separator value “\\sp\\ has been added to NTE-3, 3 = Drug Warning Narrative, to separate the different warning labels.

\[RXE-1\] Quantity Timing is a required field, but it will not be used in Outpatient Pharmacy V. 7.0. It will always be a null value ("").

\[RXE-2\] Give Code identifies the substance ordered as encoded by the Pharmacy. The components, in order, are the VA Product ID, VA Product Name, National Drug File, local file pointer, local drug name, and the local file.

\[RXE-3\] Give Amount - Minimum is a required field but it will not be used in Outpatient Pharmacy V. 7.0. It will always be a null value ("").

\[RXE-5\] Give Units identifies the units for the give amount as encoded by the VA National Drug file.

\[RXE-6\] Give Dosage Form is a coded element field. The fourth component is the pointer to the DOSAGE FORM file (#50.606). The fifth component is the form name, and the sixth component is the name of coding system (99PSF).

\[RXE-8\] Deliver-To-Location is the Method of Pickup (Window or Mail).

\[RXE-9\] Substitution Status is the value of the TRADE NAME field (#6.5) found in the PRESCRIPTION file (#52).

\[RXE-10\] Dispense Amount identifies the quantity.

\[RXE-11\] Dispense Units identifies the units for the dispense amount as encoded by the Pharmacy.

\[RXE-13\] Ordering Provider’s DEA Number will contain the physician’s DEA number if the drug is a controlled substance.

\[RXE-14\] Pharmacist/Treatment Supplier’s Verifier ID identifies the pharmacist who verified the order. The first component is the DFN pointer in the NEW PERSON file (#200) of VistA and the second component is the name.

\[RXE-18\] D/T of Most Recent Refill or Dose Dispensed contains the last date/time the patient received this particular drug. This is the PRIOR FILL DATE field (#102.1) from the PRESCRIPTION file (#52).

\[RXE-21\] Pharmacy/treatment dispense Instructions. (Label name & VA PRINT NAME).

\[RXE-31\] Supplementary Code contains three pieces of information:

- An indicator that the drug is a controlled substance or not (Y/N).
- An indicator if the patient is a ScripTalk patient (0 or 1).
- An indicator if the patient’s PMI language preference is something other than English (Y/N).

\[RXD-1\] Dispense Sub-ID Counter identifies the prescription fill number.

\[RXD-2\] Dispense/Give code will contain the same give code as in RXE-2.

\[RXD-9\] Dispense Notes have two pieces of information:

- DEA, SPECIAL HDLG field (#3) from the DRUG file (#50).
- NDC field (#27) from the PRESCRIPTION file (#52).

\[RXD-10\] Dispensing Provider is the person who finished the order.

\[RXD-12\] Total Daily Dose is the days of supply for a partial fill.

\[RXD-13\] Dispense-To-Location will contain how the patient will receive the medication. Possible answers are WINDOW, REGULAR MAIL, CERTIFIED MAIL or DO NOT MAIL.

\[RXD-15\] Pharmacy/Treatment Supplier’s Special Dispensing Instructions will indicate what sort of bottle cap should be employed. It is a safety cap or non-safety cap.

\[RXD-25\] Supplementary Code is the drug warning number and text.

\[NTE\] This segment following the RXD segment will contain the Patient Medication Instructions if any.

30. The separator value “\\sp\\ has been added to NTE-3, 3 = Drug Warning Narrative, to separate the different warning labels.

\[RXR-1\] Route is the medication route.

\[ZZZ-4\] The Hazardous to Handle Indicator identifies the medication is Hazardous to Handle as identified in the PSNDF file (#50.68). Data value is either Y or N.

\[ZZZ-5\] The Hazardous to Dispose Indicator identifies the medication is Hazardous to Dispose as identified in the PSNDF file (#50.68). Data value is either Y or N.

#### Specific Transaction – Dispense Release Date/Time

The messages for the Dispense Release Date/Time will consist of the following HL7 segments:

MSH Message Header

PID Patient Identification

PV1 Patient Visit

PV2 Patient Visit – additional information

RXE Pharmacy/Treatment Encoded Order

RXD Pharmacy/Treatment Dispense

Example:

MSH\|^~\\\|PSO VISTA\|521^OUTPATIENT\|PSO DISPENSE\|521\|20030620125043\|\|RDS^O13^RDS_O13\|10001\|P\|2.4\|\|\|AL\|AL

PID\|\|\|5000002199V009321\~\~~USVHA&&0363~NI~VA FACILITY ID&500&L\~~20140212^234234987\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~TIN~VA FACILITY ID&500&L^""""\~\~~USDOD&&0363~FIN~VA FACILITY ID&500&L^7172676\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L\|333888478\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L^492994922\~\~~USVHA&&0363~PI~VA FACILITY ID&742V1&L\|PSOPATIENT~MULTIPLE\~~RX\~\~~L\|\|19111111\|M\|\|\|123 MAIN ST~""~ANY TOWN ONE~CA~94114~USA~P~""~075^\~~ ANY TOWN TWO~CA\~\~~N\|\|(555)555-5555~PRN~PH\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

PV1\|\|O

PV2\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|SCL50~NO COPAY

RXE\|""""\|D0082^DIGOXIN 0.25MG TAB^99PSNDF^372.3^DIGOXIN 0.25MG TAB^99PSD\|""""\|\|20^MG^99PSU\|120^TAB, RAPID DISINTEGRATE^99PSF\|\|\|LAXOXIN 0.125MG\|\|\|\|\|\|123987

RXD\|3\|^ASPIRIN 325 MG TAB\|20030610\|\|\|\|100001351\|\|20031212~233~6505-00-584-0398\|\|\|\|\|\|\|\|\|\|20040615

| SEGMENT | SEQ# | LEN | DT  | R/O | RP/# | TBL# | ELEMENT NAME                                                       | EXAMPLE                                                                                           |
|---------|------|-----|-----|-----|------|------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| MSH     | 1    | 1   | ST  | R   |      |      | Field Separator                                                    | \|                                                                                                |
|         | 2    | 4   | ST  | R   |      |      | Encoding Characters                                                | ~^\\                                                                                              |
|         | 3    | 180 | HD  | R   |      | 0361 | Sending Application                                                | PSO VISTA                                                                                         |
|         | 4    | 180 | HD  | R   |      | 0362 | Sending Facility – station ID and station DNS name                 | 521~XXXXXXX.XXX.XX.XXX~DNS                                                                        |
|         | 5    | 180 | HD  | R   |      | 0361 | Receiving Application                                              | PSO DISPENSE                                                                                      |
|         | 6    | 180 | HD  | R   |      | 0362 | Receiving Facility – DNS name and port of dispensing machine       | ~XXXXXXXX.XXX.XXX.XX.XXX:####~DNS                                                                 |
|         | 7    | 26  | TS  |     |      |      | Date/Time of Message                                               | 20040405152416                                                                                    |
|         | 9    | 15  | CM  | R   | 0076 |      | Message Type                                                       | RDS~013                                                                                           |
|         | 10   | 20  | ST  | R   |      |      | Message Control ID                                                 | 10001                                                                                             |
|         | 11   | 3   | PT  | R   | 0103 |      | Processing ID                                                      | P                                                                                                 |
|         | 12   | 3   | VID | R   | 0104 |      | Version ID                                                         | 2.4                                                                                               |
|         | 15   | 2   | ID  |     |      | 0155 | Accept Ack. Type                                                   | AL                                                                                                |
|         | 16   | 2   | ID  |     |      | 0155 | Application Ack Type                                               | AL                                                                                                |
|         |      |     |     |     |      |      |                                                                    |                                                                                                   |
| PID     | 3    | 250 | CX  | R   | Y    |      | Patient ID (will contain IEN, SSN, ICN, Claim \#, etc., if exists) | 218\~\~~USVHA&&0363~PI~VA FACILITY ID&500&L                                                       |
| PID     | 4    | 250 | CX  |     |      |      | Active Veteran’s Health Identification Card (VHIC) number(s)       |                                                                                                   |
|         | 5    | 250 | XPN | R   |      |      | Patient Name                                                       | OPPATIENT~ONE                                                                                     |
|         | 7    | 26  | TS  | R   |      |      | Date/Time of Birth                                                 | 19280622                                                                                          |
|         | 8    | 1   | IS  |     |      | 0001 | Administrative Sex                                                 | M                                                                                                 |
|         | 11   | 250 | XAD | R   | Y/3  |      | Patient Address                                                    | 164 Friendship DR~""~TROY~NY~12180\~~P~""                                                         |
|         | 13   | 250 | XTN | R   | Y/3  |      | Phone Number-Home                                                  | (555)555-5555                                                                                     |
|         |      |     |     |     |      |      |                                                                    |                                                                                                   |
| PV1     | 2    | 1   | IS  | R   |      | 0004 | Patient Class                                                      | O for Outpatient                                                                                  |
|         |      |     |     |     |      |      |                                                                    |                                                                                                   |
| PV2     | 24   | 15  | IS  | R   | Y    |      | Patient Status Code                                                | SC~NO COPAY                                                                                       |
|         |      |     |     |     |      |      |                                                                    |                                                                                                   |
| RXE     | 1    | 200 | TQ  | R   |      |      | Quantity/Timing                                                    | Null                                                                                              |
|         | 2    | 250 | CE  | R   |      |      | Give Code                                                          | XH001~HEMATEST TAB (NOT FOR ORAL USE)~99PSNDF~3207.12039.4321~HEMATEST REAGENT TAB. 100/BTL~99PSD |
|         | 3    | 20  | NM  | R   |      |      | Give Amount-Minimum                                                | Null                                                                                              |
|         | 5    | 250 | CE  | R   |      |      | Give Units                                                         | 20~MG~99PSU                                                                                       |
|         | 6    | 250 | CE  | O   |      |      | Give Dosage Form                                                   | 165~TAB,TEST~99PSF                                                                                |
|         | 8    | 200 | CM  | O   |      |      | Deliver-To Location                                                | WINDOW                                                                                            |
|         | 9    | 25  | ST  | O   |      |      | Substitution Status                                                | (Trade name)                                                                                      |
|         | 15   | 20  | ST  | R   |      |      | Prescription Number                                                | 100002202                                                                                         |
| RXD     | 1    | 10  | NM  | R   |      |      | Dispense Sub-ID Counter                                            | 3                                                                                                 |
|         | 2    | 250 | CE  | R   |      |      | Dispense/Give Code                                                 | XH001~HEMATEST TAB (NOT FOR ORAL USE)~99PSNDF~3207.12039.4321~HEMATEST REAGENT TAB. 100/BTL~99PSD |
|         | 3    | 26  | TS  | R   |      |      | Date/Time Dispensed                                                | 20040405                                                                                          |
|         | 7    | 20  | ST  | R   |      |      | Prescription Number                                                | 100002202                                                                                         |
|         | 9    | 25  | ST  | O   |      |      | Dispense Notes – Release Date/Time, Bingo Wait time, NDC Code      | 200312120830^35^6505-00-584-0398                                                                  |

<span id="_Toc207089104" class="anchor"></span>Table 29: Segment

Notes pertaining to some of the data elements:

\[MSH-3\] Sending Application is the station ID along with the DNS name of the sending facility.

\[MSH-5\] Receiving Application is the DNS name and DNS port number of the dispensing application.

\[MSH-10\] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

\[PID-3\] Patient ID will contain the following possibilities to identify a patient:

- NI = ICN \#
- SS = Social Security \#
- PN = Claim \#
- PI = DFN \#

\[PID-4\] Alternate Patient ID will contain the active Veteran’s Health Identification Card (VHIC) number(s) to identify a patient.

\[PV1-2\] Patient Class is hard-coded to an O for outpatient.

\[PV2-24\] Patient Status Code contains the patient status from the prescriptions file followed by a tilde and then whether or not the patient is COPAY.

\[RXE-1\] Quantity Timing is a required field, but it will not be used in Outpatient Pharmacy V. 7.0. It will always be a null value ("").

\[RXE-2\] Give Code identifies the substance ordered as encoded by the Pharmacy. The components, in order, are the VA Product ID, VA Product Name, National Drug File, local file pointer, local drug name, and the local file.

\[RXE-3\] Give Amount - Minimum is a required field but it will not be used in Outpatient Pharmacy V. 7.0. It will always be a null value ("").

\[RXE-5\] Give Units identifies the units for the give amount as encoded by the VA National Drug file.

\[RXE-6\] Give Dosage Form is a coded element field. The fourth component is the pointer to the DOSAGE FORM file (#50.606). The fifth component is the form name, and the sixth component is the name of coding system (99PSF).

\[RXD-1\] Dispense Sub-ID Counter identifies which fill the prescription is.

\[RXD-2\] Dispense/Give code will contain the same give code as in RXE-2.

\[RXD-9\] Dispense Notes has three pieces of information:

- FILE RELEASE DATE/TIME field (#105.1) from the PRESCRIPTION file (#52).
- BINGO WAIT TIME field (#32) from the PRESCRIPTION file (#52).
- NDC field (#27) from the PRESCRIPTION file (#52).

#### Specific Transaction – Dispense Completion

The messages for the dispense completion will consist of the following HL7 segments:

MSA Message Acknowledgment

MSH Message Header

PID Patient Identification

ORC Common Order

RXD Pharmacy/Treatment Dispense

Example:

MSH\|^~\\\|PSO DISPENSE\|521\|PSO VISTA\|521\|20031215125043\|\|RRD^O14^RRD_O14\|10001\|P\|2.4\|\|\|AL\|AL

MSA\|AA~CA\|10001

PID\|\|\|5000000022V981671^^^USVAMC^PN~1234^^^PN^PI~000456789^^^USSSA^SS\|\|OPPATIENT^ONE\|\|19590116\|M

ORC\|OR\|12345\|\|\|\|\|\|\|\|^OPPROVIDER2^THREE\|^OPPROVIDER^TWO

RXD\|1\|D0082^DIGOXIN 0.25MG TAB^99PSNDF^372.3^DIGOXIN 0.25MG TAB^99PSD\|20031215\|\|\|\|123987\|\|06505-5840-00^20031212^1\|1234567^OPPROVIDER1^ONE\|\|\|123456789101112131415\|\|\|\|\|45201\|20041201\|BAXTER

<table>
<caption><p><span id="_Toc207089105" class="anchor"></span>Table 30: Segment</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>SEGMENT</th>
<th>SEQ#</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>EXAMPLE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MSH</td>
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td>|</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td>^~\&amp;</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0361</td>
<td>Sending Application</td>
<td>PSO DISPENSE</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0361</td>
<td>Sending Facility</td>
<td>~XXXXXXXX.XXX.XXX.XX.XXX:####~DNS</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0361</td>
<td>Receiving Application</td>
<td>PSO VISTA</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>180</td>
<td>HD</td>
<td>R</td>
<td></td>
<td>0362</td>
<td>Receiving Facility</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date/Time of Message</td>
<td>200304050938</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>15</td>
<td>CM_MSG</td>
<td>R</td>
<td></td>
<td>0076</td>
<td>Message Type</td>
<td>RRD~014</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>10001</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>3</td>
<td>PT</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td>P</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>60</td>
<td>VID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>2.4</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment</td>
<td>AL</td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td>NE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MSA</td>
<td>1</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0008</td>
<td>Acknowledgment Code</td>
<td>AA</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>10001</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>3</td>
<td>250</td>
<td>CX</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (will contain IEN, SSN, ICN, Claim #, etc., if exists)</td>
<td>218~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;500&amp;L</td>
</tr>
<tr class="even">
<td>PID</td>
<td>4</td>
<td>250</td>
<td>CX</td>
<td></td>
<td></td>
<td></td>
<td>Active Veteran’s Health Identification Card (VHIC) number(s)</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>250</td>
<td>XPN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>OPPATIENT~ONE</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date/Time of Birth</td>
<td>19280622</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>0001</td>
<td>Administrative Sex</td>
<td>M</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>1</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0119</td>
<td>Order Control</td>
<td>OR</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>22</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>Placer Order Number</td>
<td>12345</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Entered By</td>
<td>114~OPPROVIDER2~THREE</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td>Verified By</td>
<td>115~OPPROVIDER~TWO</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>RXD</td>
<td>1</td>
<td>4</td>
<td>NM</td>
<td>R</td>
<td></td>
<td></td>
<td>Dispense Sub-ID Counter</td>
<td>1 (Fill Number)</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0292</td>
<td>Dispense/Give Code</td>
<td>XH001~HEMATEST TAB (NOT FOR ORAL USE)~99PSNDF~3207.12039.4321~HEMATEST REAGENT TAB. 100/BTL~99PSD</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td></td>
<td></td>
<td>Date/Time Dispensed</td>
<td>20040405</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Prescription Number</td>
<td>100002202</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td><p>Dispense Notes</p>
<p>NDC Code^Release Date time^Vendor dispense code</p></td>
<td>06505-5840-00^200312120915^1</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>200</td>
<td>XCN</td>
<td>O</td>
<td></td>
<td></td>
<td><p>Dispensing Provider</p>
<p>(Verifying/Dispensing Pharmacist)</p></td>
<td>1234567~OPPROVIDER1~ONE</td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td>200</td>
<td>CM</td>
<td>O</td>
<td></td>
<td></td>
<td>Dispense-To Location</td>
<td>123456789101112131415</td>
</tr>
<tr class="odd">
<td></td>
<td>18</td>
<td>20</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>Substance Lot Number</td>
<td>45201</td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Substance Expiration Date</td>
<td>20050405</td>
</tr>
<tr class="odd">
<td></td>
<td>20</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0227</td>
<td>Substance Manufacturer Name</td>
<td>BAXTER</td>
</tr>
</tbody>
</table>

<span id="_Toc207089105" class="anchor"></span>Table 30: Segment

Notes pertaining to some data elements:

\[MSH-3\] Receiving Application is the DNS name and DNS port number of the dispensing application.

\[MSH-5\] Sending Application is the station ID along with the DNS name of the facility.

\[MSH-10\] Message Control ID is the number that uniquely identifies the message.

\[MSA-2\] Message Control ID is the same number that was in MSH-2 in the dispense request message.

\[PID-3\] Patient ID will contain the following possibilities to identify a patient:

- NI = ICN \#
- SS = Social Security \#
- PN = Claim \#
- PI = DFN \#

\[PID-4\] Patient ID will contain the active Veteran’s Health Identification Card (VHIC) number(s) to identify a patient.

\[ORC-2\] Placer Order Number is the RX internal entry number.

\[ORC-10\] Entered By is the name of the Filling Person for the prescription.

\[ORC-11\] Verified By is the name of the Checking Pharmacist for the prescription.

\[RXD-1\] Dispense Sub-ID Counter is the fill number for the prescription.

\[RXD-3\] Date/Time Dispensed is the fill date and time.

\[RXD-9\] Dispense Notes contains 3 components: 1) The NDC code. 2) The release date time. 3) The Vendor Dispense Code.

\[RXD-10\] Dispensing Provider is the name of the releasing pharmacist.

\[RXD-13\] Dispense-To-Location will contain the mail tracking number of the medication sent to the patient.

## Appendix B: HL7 Messaging with an External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new protocol, PSO RECEIVE ORDER, is exported for processing orders from an external system. To use this functionality, this protocol must be added as a SUBSCRIBER to the Event Driver protocol in the PROTOCOL file (#101), which sends the external order message.

### New Application Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new HL7 application parameter, PSO RECEIVE, is exported as the Receiving Application of the PSO RECEIVE ORDER protocol from the HL7 APPLICATION PARAMETER file (#771).

### New Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new HL7 logical link, PSO LLPO from the HL LOGICAL LINK file (#870), is being exported as the Logical Link of the PSO RECEIVE ORDER protocol. This link information will need to be edited to match the communication method of the interface if this interface is activated.

For any orders received from an external source, two new fields are stored with the Outpatient Pending Order and with the prescription once the Pending Order is finished. These fields are EXTERNAL PLACER ORDER NUMBER field (#114) and EXTERNAL APPLICATION field (#116) in the PENDING OUTPATIENT ORDERS file (#52.41). These fields are also within the PRESCRIPTION file (#52) and are the EXTERNAL PLACER ORDER NUMBER field (#123) and EXTERNAL APPLICATION field (#124).

Any external systems that send orders through this interface to VistA must comply with having unique external placer order numbers within the orders from this system. This number is used for various look-ups within the interface, in conjunction with the EXTERNAL APPLICATION field (#116) in the PENDING OUTPATIENT ORDERS file (#52.41) and the EXTERNAL APPLICATION field (#124) in the PRESCRIPTION file (#52).

Any message sent through this interface to VistA, whether it is a New Order message or a Discontinue message must contain only one order per message. The interface is not set up to receive multiple orders per message.

### HL7 Order Message Segment Definition Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the PSO RECEIVE ORDER protocol is enabled to process orders from an external system, the following table defines the data elements required for each segment of the incoming order message. This is a unilateral interface. No order information will be returned to the external system.

| Segment | Piece | Description / Field Name                       | Data                                                                                         | Data Type                    |
|---------|-------|------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------|
| MSH     | 1     | Field Separator                                | \|                                                                                           | String                       |
|         | 2     | Encoding Characters                            | ^~\\                                                                                         | String                       |
|         | 3     | Sending Application                            | Sending Application Name                                                                     | String                       |
|         | 4     | Sending Facility                               |                                                                                              | String                       |
|         | 5     | Receiving Application                          | PSO RECEIVE                                                                                  | String                       |
|         | 6     | Receiving Facility                             |                                                                                              | String                       |
|         | 9     | Message Type                                   | ORM^O01                                                                                      | Coded Value                  |
|         | 10    | Message Control ID                             |                                                                                              | String                       |
|         | 11    | Processing ID                                  | P                                                                                            | Coded Value                  |
|         | 12    | Version ID                                     | 2.3.1                                                                                        | Coded Value                  |
|         | 15    | Accept Acknowledgement                         | NE                                                                                           | Coded Value                  |
|         | 16    | Application Acknowledgement                    | AL                                                                                           | Coded Value                  |
|         | 17    | Country Code                                   | USA                                                                                          | Coded Value                  |
|         |       |                                                |                                                                                              |                              |
| PID     | 3     | Patient (pointer to File \#2)                  | VistA IEN of Patient from File \#2                                                           | Composite ID                 |
|         | 5     | Patient Name                                   |                                                                                              | Person Name                  |
|         |       |                                                |                                                                                              |                              |
| PVI     | 3     | Clinic (pointer to File \#44)                  | VistA IEN of Hospital Location from File \#44                                                | Composite                    |
|         |       |                                                |                                                                                              |                              |
| ORC     | 1     | Order Control Code                             | ‘NW’                                                                                         | Coded Value                  |
|         | 2     | Placer Order Number\*                          | External Placer Order Number                                                                 | Composite                    |
|         | 9     | Date/Time of Transaction                       | Current Date/Time                                                                            | Time Stamp                   |
|         | 10    | Entered By                                     | VistA IEN of Provider from File \#200                                                        | Composite ID Number and Name |
|         | 12    | Ordering Provider                              | VistA IEN of Provider from File \#200                                                        | Composite ID Number and Name |
|         | 15    | Order Effective Date                           | Current Date/Time                                                                            | Time Stamp                   |
| RXO     | 10    | Dispense Drug                                  | VistA IEN of Drug from File \#50                                                             | Coded Element                |
|         | 11    | Quantity                                       | Quantity                                                                                     | Numeric                      |
|         | 13    | Number of Refills                              | Number of Refills                                                                            | Numeric                      |
|         |       |                                                |                                                                                              |                              |
| NTE     | 6     | Provider’s Instructions to Dispensing Pharmacy | Free Text Provider Comments                                                                  | String                       |
|         | 7     | Patient’s Instructions                         | Expanded Sig                                                                                 | String                       |
|         |       |                                                |                                                                                              |                              |
| ZRN     | 1     | Non-VA                                         | N                                                                                            | Coded Element (N=Non VA med) |
|         | 2     | Statement/Reason                               | Non-VA Medication not recommended by VA provider or Medication prescribed by non-VA provider | String                       |
|         |       |                                                |                                                                                              |                              |
| ZRX     | 4     | Routing                                        | ‘W’ (for Window)                                                                             | String                       |

<span id="_Toc207089106" class="anchor"></span>Table 31: Example of VDEF HL7 Message Details

\* Field must contain unique data

The PSO RECEIVE ORDER protocol can also receive discontinue order messages. The following table gives the details of the fields that need to be received in the incoming order message.

| Segment | Piece | Description / Field Name      | Data                                                                                         | Data Type                    |
|---------|-------|-------------------------------|----------------------------------------------------------------------------------------------|------------------------------|
| MSH     | 1     | Field Separator               | \|                                                                                           | String                       |
|         | 2     | Encoding Characters           | ^~\\                                                                                         | String                       |
|         | 3     | Sending Application           | Sending Application Name                                                                     | String                       |
|         | 4     | Sending Facility              |                                                                                              | String                       |
|         | 5     | Receiving Application         | PSO RECEIVE                                                                                  | String                       |
|         | 6     | Receiving Facility            |                                                                                              | String                       |
|         | 9     | Message Type                  | ORM^O01                                                                                      | Coded Value                  |
|         | 10    | Message Control ID            |                                                                                              | String                       |
|         | 11    | Processing ID                 | P                                                                                            | Coded Value                  |
|         | 12    | Version ID                    | 2.3.1                                                                                        | Coded Value                  |
|         | 15    | Accept Acknowledgement        | NE                                                                                           | Coded Value                  |
|         | 16    | Application Acknowledgement   | AL                                                                                           | Coded Value                  |
|         | 16    | Country Code                  | USA                                                                                          | Coded Value                  |
|         |       |                               |                                                                                              |                              |
| PID     | 3     | Patient (pointer to File \#2) | VistA IEN of Patient from File \#2                                                           | Composite ID                 |
|         | 5     | Patient Name                  |                                                                                              | Person Name                  |
|         |       |                               |                                                                                              |                              |
| PVI     | 3     | Clinic (pointer to File \#44) | VistA IEN of Hospital Location from File \#44                                                | Composite                    |
|         |       |                               |                                                                                              |                              |
| ORC     | 1     | Order Control Code            | ‘CA’                                                                                         | Coded Value                  |
|         | 2     | Placer Order Number\*         | External Placer Order Number                                                                 | Composite                    |
|         | 9     | Date/Time of Transaction      | Current Date/Time                                                                            | Time Stamp                   |
|         | 10    | Entered By                    | VistA IEN of Provider from File \#200                                                        | Composite ID Number and Name |
|         | 12    | Ordering Provider             | VistA IEN of Provider from File \#200                                                        | Composite ID Number and Name |
|         | 15    | Order Effective Date          | Current Date/Time                                                                            | Time Stamp                   |
|         |       |                               |                                                                                              |                              |
| ZRN     | 1     | Non-VA                        | N                                                                                            | Coded Element (N=Non VA med) |
|         | 2     | Statement/Reason              | Non-VA Medication not recommended by VA provider or Medication prescribed by non-VA provider | String                       |

<span id="_Toc207089107" class="anchor"></span>Table 32: ASAP Zero Report Specifications (PSO\*7\*625)

\* Field must contain unique data

An Application Acknowledgement message is returned for new and discontinue messages received from the external system. Sequence 1 (Acknowledgement Code) of the MSA segment will always be Application Accept (AA), regardless of whether or not the incoming message passed all of the exception checks. Sequence 3 (Text Message) of the MSA segment will be null if the message was accepted and passed all of the exception checks. If the message is rejected by the receiving application, Sequence 3 (Text Message) will contain the reason for the rejection.

| Segment | Piece | Description / Field Name    | Data                         | Data Type   |
|---------|-------|-----------------------------|------------------------------|-------------|
| MSH     | 1     | Field Separator             | \|                           | String      |
|         | 2     | Encoding Characters         | ^~\\                         | String      |
|         | 3     | Sending Application         | PSO RECEIVE                  | String      |
|         | 4     | Sending Facility            | (Sending Facility)           | String      |
|         | 5     | Receiving Application       | (Receiving Application Name) | String      |
|         | 6     | Receiving Facility          | (Receiving Facility)         | String      |
|         | 7     | Date/time of Message        | Current Date/Time            | Time Stamp  |
|         | 9     | Message Type                | ORR^O01                      | Coded Value |
|         | 10    | Message Control ID          |                              | String      |
|         | 11    | Processing ID               | P                            | Coded Value |
|         | 12    | Version ID                  | 2.3.1                        | Coded Value |
|         | 15    | Accept Acknowledgement      | NE                           | Coded Value |
|         | 16    | Application Acknowledgement | NE                           | Coded Value |
|         | 17    | Country Code                | US                           | Coded Value |
|         |       |                             |                              |             |
| MSA     | 1     | Acknowledgement Code        | AA                           | Coded Value |
|         | 2     | Message Control ID          |                              | String      |
|         | 3     | Text Message                | (Null, or Rejection Reason)  | String      |

<span id="_Toc200637849" class="anchor"></span>Table 33: ASAP 4.2A Baseline Dataset

#### Order Messaging Exceptions

Exceptions will occur when VistA rejects a new or discontinue order message. For new order messages, the rejections are largely based on the drug, provider, or patient associated with the prescription order.

Drug exceptions

- Drug is inactive (less than today’s date)
- Drug is not marked for outpatient use
- Drug is not associated with a Pharmacy Orderable Item
- Invalid drug entry

Provider exceptions

- Provider is not authorized to write med orders
- Provider has an inactive date (date of today or less)
- Provider has a termination date (date of today or less)
- Provider does not hold the PROVIDER key
- Invalid provider entry

Patient exceptions

- Patient is deceased
- Invalid patient entry

Other exceptions

- Invalid NTE segment, greater than 245 characters
- Invalid message structure
- Missing MSH segment
- Missing PID segment
- Missing PVI segment
- Missing ORC segment
- Missing RXO segment
- External order, unable to successfully transmit to CPRS
- Unable to derive Institution from Clinic
- Unable to add order to Pending file
- Missing sending application name
- Invalid Order Control Code
- No Patient Location
- Missing CHCS Placer Order Number
- Duplicate order number in Outpatient Pending file
- Duplicate order number in Outpatient Prescription file
- Missing number of refills
- Missing effective date
- Missing Entered by data

For discontinue order messages, these are the possible exceptions:

Provider exceptions

- Provider is not authorized to write med orders
- Provider has an inactive date (date of today or less)
- Provider has a termination date (date of today or less)
- Provider does not hold the PROVIDER key
- Invalid provider entry

Other exceptions

- Invalid message structure
- Missing MSH segment
- Missing PID segment
- Missing ORC segment
- Missing sending application name
- Missing CHCS Placer Order Number
- Unable to find order in Pharmacy
- Patient mismatch in Pending order
- Pending order is being edited by another user
- Unable to cancel Pending order, status is HOLD
- Unable to cancel Pending order, status is RENEW
- Unable to cancel Pending order, status is DISCONTINUE (EDIT)
- Unable to cancel Pending order, status is DISCONTINUE
- Unable to cancel Pending order, status is REFILL REQUEST
- Patient mismatch in prescription
- Prescription is being edited by another user
- Unable to cancel prescription, status is DISCONTINUED
- Unable to cancel prescription, status is DELETED
- Unable to cancel prescription, status is DISCONTINUED BY PROVIDER
- Unable to cancel prescription, status is DISCONTINUED (EDIT)

## Appendix C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transitional Pharmacy Benefit (TPB) functionality has been placed “Out of Order” with the PSO\*7\*227 patch.

## Appendix D: HL7 Messaging for VistA Data Extraction Framework (VDEF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089109" class="anchor"></span>Table 34: Information Source (IS) 4.2A</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/004.png)</th>
<th><p><strong>*Important*</strong></p>
<p>Patch PSO*7*190 should not be installed prior to the site's assigned HDR installation date. Each site will be contacted approximately two weeks prior to the assigned HDR installation date and provided instructions on when and in what order to install this patch and the VDEF V. 1.0 software. Additionally, sites should not configure or attempt to utilize the VDEF software associated with this patch prior to the assigned HDR installation date. Technical Support Office personnel will work with each site to activate that application and start the site's data transmissions to the HDR database.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc207089109" class="anchor"></span>Table 34: Information Source (IS) 4.2A

Please refer to the VistA Data Extraction Framework (VDEF) Installation & User Configuration Guide for all technical assistance.

### New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*190 adds six new protocols to the PROTOCOL file (#101) to facilitate the VistA Data Extraction Framework (VDEF) Outpatient Pharmacy messaging.

PROTOCOL: (VS = Event Driver protocol, HR = Subscriber protocol)

PSO VDEF RDE O11 OP PHARM PRES VS

PSO VDEF RDE O11 OP PHARM PRES HR

PSO VDEF RDS O13 OP PHARM PPAR VS

PSO VDEF RDS O13 OP PHARM PPAR HR

PSO VDEF RDS O13 OP PHARM PREF VS

PSO VDEF RDS O13 OP PHARM PREF HR

### New Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*190 adds four new HL7 application parameters to the HL7 APPLICATION PARAMETER file (#771):

HDRPPAR is exported as the Sending Application for the PSO VDEF RDS O13 OP PHARM PPAR VS protocol.

HDRPREF is exported as the Sending Application for the PSO VDEF RDS O13 OP PHARM PREF VS protocol.

HDRPRES is exported as the Sending Application for the PSO VDEF RDE O11 OP PHARM PRES VS protocol.

PSO VDEF IE SIDE is exported as the Receiving application for the three Subscriber protocols:

PSO VDEF RDE O11 OP PHARM PRES HR

PSO VDEF RDS O13 OP PHARM PPAR HR

PSO VDEF RDS O13 OP PHARM PREF HR

### New Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are currently four HL7 logical links (VDEFVIEn) exported with VDEF V. 1.0. The VDEFVIEn links will transmit messages from the local site to the HDR Receiving host system at Austin. VDEFVIE3 is the logical link assigned to Outpatient Pharmacy and it has been added to the HL LOGICAL LINK file (#870).

### HL7 Outpatient Pharmacy VDEF Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When particular events (listed below) occur to a prescription within the Outpatient Pharmacy package, a VDEF request will be queued up at the VDEF Request Queue, with the MessageType, EventType, SubType, and the internal entry number to the PRESCRIPTION file (#52). VDEF will then go through the VDEF Request Queue to generate an HL7 message that contains all of the prescription information and send the message to the Receiving Facility through the VDEFVIE3 Logical Link.

Outpatient Pharmacy VDEF messages will be generated when:

- A new order is entered through the Outpatient Pharmacy options
- A Pending Order from Computerized Patient Record System (CPRS) is finished in the Outpatient Pharmacy options
- A refill is entered for a prescription
- A partial fill for a prescription is entered
- All prescription status changes
- A Prescription is edited and does not create a new order

Example of VDEF HL7 Message

MSH^~\|\\^HDRPREF^613~XXXX.XXXXXXXXXXX.XXX.XX.XXX~DNS^PSO VDEF IE SIDE^200HD~XXX.XXX.XX.XXX~DNS^20041216192259-0500^^RDS~O13^61332594923^T^2.4^^^AL^NE^US

PID^1^1234567890V123456^1234567890V123456\~\~~USVHA&&0363~NI~VA FACILITY ID&613&L\|000654321\~\~~USSSA&&0363~SS~VA FACILITY ID&613&L\|1234\~\~~USVHA&&0363~PI~VA FACILITY ID&613&L\|000654321\~\~~USVBA&&0363~PN~VA FACILITY ID&613&L^^LastName~FirstName~M\~\~\~~L^MotherMaidenLastName\~\~\~\~\~~M^19150511^M^^""^HC 11, BOX 22B~""~CAPON BRIDGE~WV~12345\~~P~""\|\~~BARNESVILLE~MD\~\~~N^027^(123)555-1212^""^^D^0^^000654321^^^""^BARNESVILLE MD^^^^^^20000301^^

ORC^RE^^1685567~613_52\_.001^^CM^^\~\~~19950109~19960110\~~FILL/EXPIRATION\|\~\~\~~19950109\~~ISSUED\|\~\~~19950109~19950330\~~DISPENSED/LAST DISPENSED\|\~\~\~~19950629\~~CANCEL^^19950109123449-0500^63~OPPROVIDER40~TWO\~\~\~\~~VistA200^^947~OPPROVIDER41~TWO~A~MD\~~MD~RE^ CCS/HOME VISIT~2559^^^613~MARTINSBURG VAMC~613_52_20~5005423~MARTINSBURG VAMC~NCPDP^^^^MARTINSBURG, WV^^^^4500704~DISCONTINUED~99VA_52_100

RXE^1&100MG\~\~~19950109~19950629\~~FILL/CANCEL^4005192~AMANTADINE HCL 100MG CAP~99VA_52_6~0781-2048-01\~~NDC^0^^20~MG~613_52_6^63~CAP~613_50.7\_.02^~TAKE~613_52.0113_8\|~CAPSULE~613_52.0113_3\|~Q8H~613_52.0113_7\|~QAMHS~613_52_114\|~IN THE MORNING AND AT BEDTIME~613_52_115^\~\~\~\~~WINDOW^^90^^1^^2992~OPPROVIDER42~THREE~M\~\~\~~PHARMACIST^5430744^^^19950111170823-0500^^^TAKE ONE CAPSULE BY MOUTH EVERY EIGHT HOURS IN THE MORNING AND AT BEDTIME\~~613_52_10.2^D90^^^^^^^^^11135~ AMANTADINE HCL 100MG CAP ~613_50\_.01\|C0255\~~613_50_27

RXR^1~ORAL (BY MOUTH)~613_52.0113_6

FT1^^^^19950109^^CG^620~AMANTADINE\~~613_52_39.2^^^^^0.009^^^^^^ONSC^12345~FINISHING PHARM~613_52_38

FT1^2^^^19950109^^CO^1~PSO NSC RX COPAY NEW~500_52_105

OBX^1^CE^WAS THE PATIENT COUNSELED^^4500633~YES~99VA_52_41^^^^^^F

OBX^2^CE^WAS COUNSELING UNDERSTOOD^^4500630~NO~99VA_52_42^^^^^^F

NTE^1^^RENEWED FROM RX \# 123456^RE~REMARKS~613_52_12

ORC^RF^^1^^^^\~\~~19950330\~\~~DISPENSED^~1685567^19950306^^^947~OPPROVIDER41~TWO~A~MD\~~MD~VistA200^^^^REFILL^613~MARTINSBURG

VAMC~613_52.1_8~5005423~MARTINSBURG VAMC~NCPDP^^^^MARTINSBURG, WV RXE^\~\~~19950330\~\~~REFILL^4005192~AMANTADINE HCL 100MG CAP~99VA \_52_6~0781-2048-01\~~NDC ^0^^20~MG~613_52_6^^^\~\~\~\~~MAIL^^90^^^^2992~OPPROVIDER42~THREE~M\~\~\~~PHARMACIST^^^^199503290934-0500^^^^D90^^^^^^^^^11135~ AMANTADINE HCL 100MG CAP ~613_50\_.01\|C0255\~~613_50_27

FT1^^^^19950330^^CG^620~AMANTADINE\~~613_52_39.2^^^^^0.009

FT1^2^^^19950330^^CG^1~PSO NSC RX COPAY NEW~500_52_105

ORC^RF^^1^^^^^~1685567^199503061212-0500^^^947~OPPROVIDER41~TWO~A~MD\~~MD~VistA200^^^^PARTIAL^613~MARTINSBURG VAMC~613_52.2\_.09~5005423~MARTINSBURG VAMC~NCPDP^^^^MARTINSBURG, WV RXE^\~\~~19950306\~\~~PARTIAL^4005192~AMANTADINE HCL 100MG CAP~99VA \_52_6~0781-2048-01\~~NDC ^0^^20~MG~613_52_6^^^\~\~\~\~~WINDOW^^30^^^^2992~OPPROVIDER42~THREE~M\~\~\~~PHARMACIST^^^^19950307144822-0500^^^^D30^^^^^^^^^11135~ AMANTADINE HCL 100MG CAP ~613_50\_.01\|C0255\~~613_50_27

NTE^^^PT OUT RX ON SUSP FOR 24 MORE DAYS^RE~REMARKS~613_50_27

FT1^^^^19950306^^CG^620~AMANTADINE\~~613_52_39.2^^^^^0.009

FT1^2^^^19950306^^CG^1~PSO NSC RX COPAY NEW~500_52_105

### HL7 Outpatient Pharmacy VDEF Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some data values in the following table represent VistA data fields that have been assigned VUIDs (VHA Unique Identifiers). In these instances, when a VUID is available, the data value will be the VUID, along with the appropriate coding scheme. If for some reason the VUID is not available, the data value will be the VistA data value, along with the appropriate coding scheme.

The exception to this format would be the data value for the coded element for Give Code in the segment RXE 2. If a VUID is available, the first three pieces would be:

VUID from the VA PRODUCT file (#50.68)

VA PRODUCT Name from the VA PRODUCT file (#50.68)

99VA_52_6

If a VUID is not available, for example if the local drug from the DRUG file (#50) is not matched to the National Drug File, the first three pieces would be:

Null

DRUG Name from the DRUG file (#50)

(Station Number)\_52_6

Also in the following table, dosing information is sent in the RXE 1 segment. There are different formats for the dosing information, depending on the type of dosage. Here are examples, which include a possible dosage, a local possible dosage, and a possible dosage with complex dosing instructions.

Example 1: This example is for a possible dosage, which is a numeric dosage, with a numeric dispense units per dose. These types of dosages are limited to single ingredient drugs, with a numeric strength, usually with a dosage form of tablets or capsules.

> 2&200MG\~~10D~20050720~20060721\~~FILL/EXPIRATION

The dosage in this case is 2&200MG\~~10D, where 2 represents the dispense units per dose, 200MG represents the total dosage for the 2 tablets or capsules, and 10D represents the duration, which in this case is 10 days. (duration is optional)

Example 2: This example is for a local possible dosage, which is a text dosage, with no dispense units per dose. These types of dosages apply to items such as multi-ingredient drugs, creams, ointments, drops, etc.

> &1 DROP\~\~~20050720~20060721\~~FILL/EXPIRATION

The dosage in this case is &1 DROP\~\~~, where 1 DROP represents the dosage. Since it is a local possible dosage, there is no dispense units per dose, and in this case, there is no duration, though a duration can be applied to any type of dosage.

Example 3: This example is for a possible dosage, with complex dosing instructions.

> 1&100MG\~~10D~20050720~20060721\~~FILL/EXPIRATION\|2&200MG\~~5D

The first set of dosing instructions is 1&100MG\~~10D, where 1 represents the dispense units per dose, 100MG represents the total dosage, and 10D represents a duration of 10 Days. The next set of dosing instructions is 2&200MG\~~5D, where 2 represents the dispense units per dose, 200MG represents the total dosage, and 5D represents a duration of 5 Days.

31. The dosage will only appear in the RXE segment associated with the original fill, it will not appear in RXE segments associated with refills or partial fills.

<table>
<caption><p><span id="_Toc207089110" class="anchor"></span>Table 35: Pharmacy Header (PHA) 4.2A</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Segment</th>
<th>Piece /<br />
Sequence</th>
<th>Description / Field Name</th>
<th>Data Type</th>
<th>Data Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MSH</td>
<td>1</td>
<td>Field Separator</td>
<td>ST</td>
<td>^</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>2</td>
<td>Encoding Characters</td>
<td>ST</td>
<td>~|\&amp;</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>3</td>
<td>Sending Application</td>
<td>HD</td>
<td>HDRPREF</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>4</td>
<td>Sending Facility</td>
<td>HD</td>
<td>613~XXXX.XXXXXXXXXXXX.XXX.XX.XXX~DNS</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>5</td>
<td>Receiving Application</td>
<td>HD</td>
<td>PSO VDEF IE SIDE</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>6</td>
<td>Receiving Facility</td>
<td>HD</td>
<td>200HD~XXX.XXX.XX.XXX~DNS</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>7</td>
<td>Date/Time Of Message</td>
<td>TS</td>
<td>20041216192259-0500</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>8</td>
<td>Security</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>9</td>
<td>Message Type</td>
<td>CM</td>
<td>RDS~O13</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>10</td>
<td>Message Control ID</td>
<td>ST</td>
<td>61332594923</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>11</td>
<td>Processing ID</td>
<td>PT</td>
<td>T</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>12</td>
<td>Version ID</td>
<td>VID</td>
<td>2.4</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>13</td>
<td>Sequence Number</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>MSH</td>
<td>14</td>
<td>Continuation Pointer</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>15</td>
<td>Accept Acknowledgment Type</td>
<td>ID</td>
<td>AL</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>16</td>
<td>Application Acknowledgment Type</td>
<td>ID</td>
<td>NE</td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>17</td>
<td>Country Code</td>
<td>ID</td>
<td>US</td>
</tr>
<tr class="even">
<td>MSH</td>
<td>18</td>
<td>Character Set</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>19</td>
<td>Principal Language Of Message</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>MSH</td>
<td>20</td>
<td>Alternate Character Set Handling Scheme</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>MSH</td>
<td>21</td>
<td>Conformance Statement ID</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PID</td>
<td>1</td>
<td>Set ID - PID</td>
<td>SI</td>
<td>1</td>
</tr>
<tr class="even">
<td>PID</td>
<td>2</td>
<td>Patient ID</td>
<td>CX</td>
<td>1234567890V123456</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>3</td>
<td>Patient Identifier List</td>
<td>CX</td>
<td>1234567890V123456~~~USVHA&amp;&amp;0363~NI~VA FACILITY ID&amp;613&amp;L</td>
</tr>
<tr class="even">
<td>PID</td>
<td>3</td>
<td>Patient Identifier List_rep</td>
<td></td>
<td>000654321~~~USSSA&amp;&amp;0363~SS~VA FACILITY ID&amp;613&amp;L</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>3</td>
<td>Patient Identifier List_rep</td>
<td></td>
<td>1234~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;613&amp;L</td>
</tr>
<tr class="even">
<td>PID</td>
<td>3</td>
<td>Patient Identifier List_rep</td>
<td></td>
<td>000654321~~~USVBA&amp;&amp;0363~PN~VA FACILITY ID&amp;613&amp;L</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>4</td>
<td>Alternate Patient ID - PID</td>
<td>CX</td>
<td>654~~~USVHA&amp;&amp;0363~PI~VA FACILITY ID&amp;742V1&amp;L</td>
</tr>
<tr class="even">
<td>PID</td>
<td>5</td>
<td>Patient Name</td>
<td>XPN</td>
<td>LastName~FirstName~M~~~~L</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>6</td>
<td>Mother's Maiden Name</td>
<td>XPN</td>
<td>MotherMaidenLastName~~~~~~M</td>
</tr>
<tr class="even">
<td>PID</td>
<td>7</td>
<td>Date/Time Of Birth</td>
<td>TS</td>
<td>19150511</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>8</td>
<td>Administrative Sex</td>
<td>IS</td>
<td>M</td>
</tr>
<tr class="even">
<td>PID</td>
<td>9</td>
<td>Patient Alias</td>
<td>XPN</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>10</td>
<td>Race</td>
<td>CE</td>
<td>""</td>
</tr>
<tr class="even">
<td>PID</td>
<td>11</td>
<td>Patient Address</td>
<td>XAD</td>
<td>HC 11, BOX 22B~""~CAPON BRIDGE~WV~12345~~P~""</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>11</td>
<td>Patient Address_rep</td>
<td></td>
<td>~~BARNESVILLE~MD~~~N</td>
</tr>
<tr class="even">
<td>PID</td>
<td>12</td>
<td>County Code</td>
<td>IS</td>
<td>027</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>13</td>
<td>Phone Number - Home</td>
<td>XTN</td>
<td>(123)555-1212</td>
</tr>
<tr class="even">
<td>PID</td>
<td>14</td>
<td>Phone Number - Business</td>
<td>XTN</td>
<td>""</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>15</td>
<td>Primary Language</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>PID</td>
<td>16</td>
<td>Marital Status</td>
<td>CE</td>
<td>D</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>17</td>
<td>Religion</td>
<td>CE</td>
<td>0</td>
</tr>
<tr class="even">
<td>PID</td>
<td>18</td>
<td>Patient Account Number</td>
<td>CX</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>19</td>
<td>SSN Number - Patient</td>
<td>ST</td>
<td>654321</td>
</tr>
<tr class="even">
<td>PID</td>
<td>20</td>
<td>Driver's License Number - Patient</td>
<td>DLN</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>21</td>
<td>Mother's Identifier</td>
<td>CX</td>
<td> </td>
</tr>
<tr class="even">
<td>PID</td>
<td>22</td>
<td>Ethnic Group</td>
<td>CE</td>
<td>""</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>23</td>
<td>Birth Place</td>
<td>ST</td>
<td> BARNESVILLE MD</td>
</tr>
<tr class="even">
<td>PID</td>
<td>24</td>
<td>Multiple Birth Indicator</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>PID</td>
<td>25</td>
<td>Birth Order</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>PID</td>
<td>26</td>
<td>Citizenship</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>27</td>
<td>Veterans Military Status</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>PID</td>
<td>28</td>
<td>Nationality</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>29</td>
<td>Patient Death Date and Time</td>
<td>TS</td>
<td>20000301</td>
</tr>
<tr class="even">
<td>PID</td>
<td>30</td>
<td>Patient Death Indicator</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>PID</td>
<td>31</td>
<td>Identity Unknown Indicator</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>PID</td>
<td>32</td>
<td>Identity Reliability Code</td>
<td>IS</td>
<td></td>
</tr>
<tr class="odd">
<td>PID</td>
<td>33</td>
<td>Last Update Date/Time</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>PID</td>
<td>34</td>
<td>Last Update Facility</td>
<td>HD</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>35</td>
<td>Species Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>PID</td>
<td>36</td>
<td>Breed Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>PID</td>
<td>37</td>
<td>Strain</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>PID</td>
<td>38</td>
<td>Production Class Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ORC</td>
<td>1</td>
<td>Order Control</td>
<td>ID</td>
<td>RE</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>2</td>
<td>Placer Order Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>3</td>
<td>Filler Order Number</td>
<td>EI</td>
<td>1685567~613_52_.001</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>4</td>
<td>Placer Group Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>5</td>
<td>Order Status</td>
<td>ID</td>
<td>CM</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>6</td>
<td>Response Flag</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>ORC</td>
<td>7</td>
<td>Quantity/ Timing</td>
<td>TQ</td>
<td>~~~19950109~19960110~~FILL/EXPIRATION</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>7</td>
<td>Quantity/ Timing_rep</td>
<td></td>
<td>~~~~19950109~~ISSUED</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>7</td>
<td>Quantity/ Timing_rep</td>
<td></td>
<td>~~~19950109~19950330~~DISPENSED/LAST DISPENSED</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>7</td>
<td>Quantity/ Timing_rep</td>
<td></td>
<td>~~~~19950629~~CANCEL</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>8</td>
<td>Parent</td>
<td>CM</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>9</td>
<td>Date/Time of Transaction</td>
<td>TS</td>
<td>19950109123449-0500</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>10</td>
<td>Entered By</td>
<td>XCN</td>
<td>63~OPPROVIDER40~TWO~~~~~VistA200</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>11</td>
<td>Verified By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>12</td>
<td>Ordering Provider</td>
<td>XCN</td>
<td>947~OPPROVIDER41~TWO~A~MD~~MD~RE</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>13</td>
<td>Enterer's Location / Room (Hospital Location IEN~Clinic)</td>
<td>PL</td>
<td>CCS/HOME VISIT~2559</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>14</td>
<td>Call Back Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>15</td>
<td>Order Effective Date/Time</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>16</td>
<td>Order Control Code Reason</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>17</td>
<td>Entering Organization</td>
<td>CE</td>
<td>613~MARTINSBURG VAMC~613_52_20~5005423~MARTINSBURG VAMC~NCPDP</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>18</td>
<td>Entering Device</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>19</td>
<td>Action By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>20</td>
<td>Advanced Beneficiary Notice Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>21</td>
<td>Ordering Facility Name</td>
<td>XON</td>
<td> MARTINSBURG, WV</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>22</td>
<td>Ordering Facility Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>23</td>
<td>Ordering Facility Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>24</td>
<td>Ordering Provider Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>25</td>
<td>Order Status Modifier (If CMOP drug, send CMOP status)</td>
<td>CWE</td>
<td><p>4500704~DISCONTINUED~9</p>
<p>9VA_52_100</p>
<p>OR</p>
<p>12~DISCONTINUED~613_52_100</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>1</td>
<td>Quantity/Timing</td>
<td>TQ</td>
<td>1&amp;100MG~~~19950109~19950629~~FILL/CANCEL</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>2</td>
<td>Give Code</td>
<td>CE</td>
<td><p>4005192~AMANTADI</p>
<p>NE HCL 100MG CAP~99VA_52_6~0781-2048-01~~NDC OR</p>
<p>~AMANTADINE 100MG CAP~613_52_6~0781-2048-01~~NDC</p></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>3</td>
<td>Give Amount - Minimum</td>
<td>NM</td>
<td>0</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>4</td>
<td>Give Amount - Maximum</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>5</td>
<td>Give Units</td>
<td>CE</td>
<td>20~MG~613_52_6</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>6</td>
<td>Give Dosage Form</td>
<td>CE</td>
<td><p> 63~CAP~613_50.7_.02</p>
<p>OR if VUID exists</p>
<p>63~CAP~613_50.7_.02~11111~CAP~99VA__50.7_.02</p></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>7(n)</td>
<td>Verb, Noun, Schedule, Conjunction</td>
<td>CE</td>
<td>~TAKE~613_52.0113_8|~CAPSULE~613_52.0113_3|~Q8H~613_52.0113_7</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>7(n)</td>
<td>Patient Instructions</td>
<td>CE</td>
<td>~QAMHS~613_52_114</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>7(n)</td>
<td>Expanded Patient Instructions</td>
<td>CE</td>
<td>~IN THE MORNING AND AT BEDTIME~613_52_115</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>8</td>
<td>Deliver-To Location</td>
<td>CM</td>
<td>~~~~~WINDOW</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>9</td>
<td>Substitution Status</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>10</td>
<td>Dispense Amount</td>
<td>NM</td>
<td>90</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>11</td>
<td>Dispense Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>12</td>
<td>Number of Refills</td>
<td>NM</td>
<td>1</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>13</td>
<td>Ordering Provider's DEA Number</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>14</td>
<td>Pharmacist/Treatment Supplier's Verifier ID</td>
<td>XCN</td>
<td>2992~OPPROVIDER42~THREE~M~~~~PHARMACIST</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>15</td>
<td>Prescription Number</td>
<td>ST</td>
<td>5430744</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>16</td>
<td>Number of Refills Remaining</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>17</td>
<td>Number of Refills/Doses Dispensed</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>18</td>
<td>D/T of Most Recent Refill or Dose Dispensed</td>
<td>TS</td>
<td>19950111170823-0500</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>19</td>
<td>Total Daily Dose</td>
<td>CQ</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>20</td>
<td>Needs Human Review</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>21</td>
<td>Pharmacy/Treatment Supplier's Special Dispensing Instructions</td>
<td>CE</td>
<td>TAKE ONE CAPSULE BY MOUTH EVERY EIGHT HOURS IN THE MORNING AND AT BEDTIME~~613_52_10.2</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>22</td>
<td>Give Per (Time Unit)</td>
<td>ST</td>
<td>D90</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>23</td>
<td>Give Rate Amount</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>24</td>
<td>Give Rate Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>25</td>
<td>Give Strength</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>26</td>
<td>Give Strength Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>27</td>
<td>Give Indication</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>28</td>
<td>Dispense Package Size</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>29</td>
<td>Dispense Package Size Unit</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>30</td>
<td>Dispense Package Method</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: Local Drug</td>
<td>ST</td>
<td> 11135~AMANTADINE HCL 100MG CAP~613_50_.01</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: CMOP ID</td>
<td>ST</td>
<td> C0255~~613_50_27</td>
</tr>
<tr class="odd">
<td>RXR</td>
<td>1</td>
<td>Route</td>
<td>CE</td>
<td>1~ORAL (BY MOUTH)~613_52.0113_6</td>
</tr>
<tr class="even">
<td>RXR</td>
<td>2</td>
<td>Administration Site</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXR</td>
<td>3</td>
<td>Administration Device</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXR</td>
<td>4</td>
<td>Administration Method</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXR</td>
<td>5</td>
<td>Routing Instruction</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950109</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CG</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>7</td>
<td>Transaction Code</td>
<td>CE</td>
<td>620~AMANTADINE~~613_52_39.2</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>8</td>
<td>Transaction Description</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>9</td>
<td>Transaction Description - Alt</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>10</td>
<td>Transaction Quantity</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>11</td>
<td>Transaction Amount - Extended</td>
<td>CP</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>12</td>
<td>Transaction Amount - Unit</td>
<td>CP</td>
<td>0.009</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>13</td>
<td>Department Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>14</td>
<td>Insurance Plan ID</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>15</td>
<td>Insurance Amount</td>
<td>CP</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>16</td>
<td>Assigned Patient Location</td>
<td>PL</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>17</td>
<td>Fee Schedule</td>
<td>IS</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>18</td>
<td>Patient Type</td>
<td>IS</td>
<td>ONSC</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>19</td>
<td>Diagnosis Code - FT1</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>20</td>
<td>Performed By Code</td>
<td>XCN</td>
<td> 12345~FINISHING PHARM~613_52_38</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>21</td>
<td>Ordered By Code</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>22</td>
<td>Unit Cost</td>
<td>CP</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>23</td>
<td>Filler Order Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>24</td>
<td>Entered By Code</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>25</td>
<td>Procedure Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>26</td>
<td>Procedure Code Modifier</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950109</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CO</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>7</td>
<td>Transaction Code</td>
<td>CE</td>
<td>1~PSO NSC RX COPAY NEW~500_52_105</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBX</td>
<td>1</td>
<td>Set ID - OBX</td>
<td>SI</td>
<td>1</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>2</td>
<td>Value Type</td>
<td>ID</td>
<td>CE</td>
</tr>
<tr class="even">
<td>OBX</td>
<td>3</td>
<td>Observation Identifier</td>
<td>CE</td>
<td>WAS THE PATIENT COUNSELED</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>4</td>
<td>Observation Sub-Id</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>5</td>
<td>Observation Value</td>
<td>CE</td>
<td><p>4500633~YES~99VA_52_41</p>
<p>OR</p>
<p>1~YES~613_52_41</p></td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>6</td>
<td>Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>7</td>
<td>References Range</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>8</td>
<td>Abnormal Flags</td>
<td>IS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>9</td>
<td>Probability</td>
<td>NM</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>10</td>
<td>Nature of Abnormal Test</td>
<td>ID</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>11</td>
<td>Observation Result Status</td>
<td>ID</td>
<td>F</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>12</td>
<td>Date Last Observation Normal Value</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>13</td>
<td>User Defined Access Checks</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>14</td>
<td>Date/Time of the Observation</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>15</td>
<td>Producer's ID</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>16</td>
<td>Responsible Observer</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>17</td>
<td>Observation Method</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>18</td>
<td>Equipment Instance Identifier</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>19</td>
<td>Date/Time of the Analysis</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>1</td>
<td>Set ID - OBX</td>
<td>SI</td>
<td>2</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>2</td>
<td>Value Type</td>
<td>ID</td>
<td>CE</td>
</tr>
<tr class="even">
<td>OBX</td>
<td>3</td>
<td>Observation Identifier</td>
<td>CE</td>
<td>WAS COUNSELING UNDERSTOOD</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>4</td>
<td>Observation Sub-Id</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>5</td>
<td>Observation Value</td>
<td>CE</td>
<td><p>4500630~NO~99VA_52_42</p>
<p>OR</p>
<p>0~NO~613_52_42</p></td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>6</td>
<td>Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>7</td>
<td>References Range</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>8</td>
<td>Abnormal Flags</td>
<td>IS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>9</td>
<td>Probability</td>
<td>NM</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>10</td>
<td>Nature of Abnormal Test</td>
<td>ID</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>11</td>
<td>Observation Result Status</td>
<td>ID</td>
<td>F</td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>12</td>
<td>Date Last Observation Normal Value</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>13</td>
<td>User Defined Access Checks</td>
<td>ST</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>14</td>
<td>Date/Time of the Observation</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>15</td>
<td>Producer's ID</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>16</td>
<td>Responsible Observer</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>17</td>
<td>Observation Method</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>OBX</td>
<td>18</td>
<td>Equipment Instance Identifier</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="even">
<td>OBX</td>
<td>19</td>
<td>Date/Time of the Analysis</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td>NTE</td>
<td>1</td>
<td>Set ID - NTE</td>
<td>SI</td>
<td>1</td>
</tr>
<tr class="odd">
<td>NTE</td>
<td>2</td>
<td>Source of Comment</td>
<td>ID</td>
<td> </td>
</tr>
<tr class="even">
<td>NTE</td>
<td>3</td>
<td>Comment</td>
<td>FT</td>
<td>RENEWED FROM RX # 123456</td>
</tr>
<tr class="odd">
<td>NTE</td>
<td>4</td>
<td>Comment Type</td>
<td>CE</td>
<td>RE~REMARKS~613_52_12</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>1</td>
<td>Order Control</td>
<td>ID</td>
<td>RF</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>2</td>
<td>Placer Order Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>3</td>
<td>Filler Order Number</td>
<td>EI</td>
<td>1</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>4</td>
<td>Placer Group Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>5</td>
<td>Order Status</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>ORC</td>
<td>6</td>
<td>Response Flag</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>7</td>
<td>Quantity/Timing</td>
<td>TQ</td>
<td>~~~19950330~~~DISPENSED</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>8</td>
<td>Parent</td>
<td>CM</td>
<td>~1685567</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>9</td>
<td>Date/Time of Transaction</td>
<td>TS</td>
<td>19950306</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>10</td>
<td>Entered By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>11</td>
<td>Verified By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>12</td>
<td>Ordering Provider</td>
<td>XCN</td>
<td>947~OPPROVIDER41~TWO~A~MD~~MD~VistA200</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>13</td>
<td>Enterer's Location</td>
<td>PL</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>14</td>
<td>Call Back Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>15</td>
<td>Order Effective Date/Time</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>16</td>
<td>Order Control Code Reason</td>
<td>CE</td>
<td>REFILL</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>17</td>
<td>Entering Organization</td>
<td>CE</td>
<td>613~MARTINSBURG VAMC~613_52.1_8~5005423~MARTINSBURG VAMC~NCPDP</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>18</td>
<td>Entering Device</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>19</td>
<td>Action By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>20</td>
<td>Advanced Beneficiary Notice Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>21</td>
<td>Ordering Facility Name</td>
<td>XON</td>
<td> MARTINSBURG, WV</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>22</td>
<td>Ordering Facility Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>23</td>
<td>Ordering Facility Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>24</td>
<td>Ordering Provider Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>25</td>
<td>Order Status Modifier</td>
<td>CWE</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>1</td>
<td>Quantity/Timing</td>
<td>TQ</td>
<td>~~~19950330~~~REFILL</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>2</td>
<td>Give Code</td>
<td>CE</td>
<td><p>4005192~AMANTADI</p>
<p>NE HCL 100MG CAP~99VA_52_6~0781-2048-01~~NDC</p>
<p>OR</p>
<p>~AMANTADINE 100MG CAP~613_52_6~0781-2048-01~~NDC</p></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>3</td>
<td>Give Amount - Minimum</td>
<td>NM</td>
<td>0</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>4</td>
<td>Give Amount - Maximum</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>5</td>
<td>Give Units</td>
<td>CE</td>
<td>20~MG~613_52_6</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>6</td>
<td>Give Dosage Form</td>
<td>CE</td>
<td> 20~MG~613_52_6</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>7</td>
<td>Provider's Administration Instructions</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>8</td>
<td>Deliver-To Location</td>
<td>CM</td>
<td>~~~~~MAIL</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>9</td>
<td>Substitution Status</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>10</td>
<td>Dispense Amount</td>
<td>NM</td>
<td>90</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>11</td>
<td>Dispense Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>12</td>
<td>Number of Refills</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>13</td>
<td>Ordering Provider's DEA Number</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>14</td>
<td>Pharmacist/Treatment Supplier's Verifier ID</td>
<td>XCN</td>
<td>2992~OPPROVIDER42~THREE~M~~~~PHARMACIST</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>15</td>
<td>Prescription Number</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>16</td>
<td>Number of Refills Remaining</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>17</td>
<td>Number of Refills/Doses Dispensed</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>18</td>
<td>D/T of Most Recent Refill or Dose Dispensed</td>
<td>TS</td>
<td>199503290934-0500</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>19</td>
<td>Total Daily Dose</td>
<td>CQ</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>20</td>
<td>Needs Human Review</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>21</td>
<td>Pharmacy/Treatment Supplier's Special Dispensing Instructions</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>22</td>
<td>Give Per (Time Unit)</td>
<td>ST</td>
<td>D90</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>23</td>
<td>Give Rate Amount</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>24</td>
<td>Give Rate Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>25</td>
<td>Give Strength</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>26</td>
<td>Give Strength Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>27</td>
<td>Give Indication</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>28</td>
<td>Dispense Package Size</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>29</td>
<td>Dispense Package Size Unit</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>30</td>
<td>Dispense Package Method</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: Local Drug</td>
<td>ST</td>
<td> 11135~AMANTADINE HCL 100MG CAP~613_50_.01</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: CMOP ID</td>
<td>ST</td>
<td> C0255~~613_50_27</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950330</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CG</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>7</td>
<td>Transaction Code (Pharmacy Orderable Item/Name, Coding System)</td>
<td>CE</td>
<td>620~AMANTADINE~~613_52_39.2</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>8</td>
<td>Transaction Description</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>9</td>
<td>Transaction Description - Alt</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>10</td>
<td>Transaction Quantity</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>11</td>
<td>Transaction Amount - Extended</td>
<td>CP</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>12</td>
<td>Transaction Amount - Unit</td>
<td>CP</td>
<td>0.009</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950330</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CG</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>7</td>
<td>Transaction Code</td>
<td>CE</td>
<td>1~PSO NSC RX COPAY NEW~500_52_105</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>1</td>
<td>Order Control</td>
<td>ID</td>
<td>RF</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>2</td>
<td>Placer Order Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>3</td>
<td>Filler Order Number</td>
<td>EI</td>
<td>1</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>4</td>
<td>Placer Group Number</td>
<td>EI</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>5</td>
<td>Order Status</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>ORC</td>
<td>6</td>
<td>Response Flag</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>7</td>
<td>Quantity/Timing</td>
<td>TQ</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>8</td>
<td>Parent</td>
<td>CM</td>
<td>~1685567</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>9</td>
<td>Date/Time of Transaction</td>
<td>TS</td>
<td>199503061212-0500</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>10</td>
<td>Entered By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>11</td>
<td>Verified By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>12</td>
<td>Ordering Provider</td>
<td>XCN</td>
<td>947~OPPROVIDER41~TWO~A~MD~~MD~VistA200</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>13</td>
<td>Enterer's Location</td>
<td>PL</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>14</td>
<td>Call Back Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>15</td>
<td>Order Effective Date/Time</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>16</td>
<td>Order Control Code Reason</td>
<td>CE</td>
<td>PARTIAL</td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>17</td>
<td>Entering Organization</td>
<td>CE</td>
<td>613~MARTINSBURG VAMC~613_52.2_.09~5005423~MARTINSBURG VAMC~NCPDP</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>18</td>
<td>Entering Device</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>19</td>
<td>Action By</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>20</td>
<td>Advanced Beneficiary Notice Code</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>21</td>
<td>Ordering Facility Name</td>
<td>XON</td>
<td> MARTINSBURG, WV</td>
</tr>
<tr class="even">
<td>ORC</td>
<td>22</td>
<td>Ordering Facility Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>23</td>
<td>Ordering Facility Phone Number</td>
<td>XTN</td>
<td> </td>
</tr>
<tr class="even">
<td>ORC</td>
<td>24</td>
<td>Ordering Provider Address</td>
<td>XAD</td>
<td> </td>
</tr>
<tr class="odd">
<td>ORC</td>
<td>25</td>
<td>Order Status Modifier</td>
<td>CWE</td>
<td> </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>1</td>
<td>Quantity/Timing</td>
<td>TQ</td>
<td>~~~19950306~~~PARTIAL</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>2</td>
<td>Give Code</td>
<td>CE</td>
<td><p>4005192~AMANTADI</p>
<p>NE HCL 100MG CAP~99VA_52_6~0781-2048-01~~NDC</p>
<p>OR</p>
<p>~AMANTADINE 100MG CAP~613_52_6~0781-2048-01~~NDC</p></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>3</td>
<td>Give Amount - Minimum</td>
<td>NM</td>
<td>0</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>4</td>
<td>Give Amount - Maximum</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>5</td>
<td>Give Units</td>
<td>CE</td>
<td>20~MG~613_52_6</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>6</td>
<td>Give Dosage Form</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>7</td>
<td>Provider's Administration Instructions</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>8</td>
<td>Deliver-To Location</td>
<td>CM</td>
<td>~~~~~WINDOW</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>9</td>
<td>Substitution Status</td>
<td>ID</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>10</td>
<td>Dispense Amount</td>
<td>NM</td>
<td>30</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>11</td>
<td>Dispense Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>12</td>
<td>Number of Refills</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>13</td>
<td>Ordering Provider's DEA Number</td>
<td>XCN</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>14</td>
<td>Pharmacist/Treatment Supplier's Verifier ID</td>
<td>XCN</td>
<td>2992~OPPROVIDER42~THREE~M~~~~PHARMACIST</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>15</td>
<td>Prescription Number</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>16</td>
<td>Number of Refills Remaining</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>17</td>
<td>Number of Refills/Doses Dispensed</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>18</td>
<td>D/T of Most Recent Refill or Dose Dispensed</td>
<td>TS</td>
<td>19950307144822-0500</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>19</td>
<td>Total Daily Dose</td>
<td>CQ</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>20</td>
<td>Needs Human Review</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>21</td>
<td>Pharmacy/Treatment Supplier's Special Dispensing Instructions</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>22</td>
<td>Give Per (Time Unit)</td>
<td>ST</td>
<td>D30</td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>23</td>
<td>Give Rate Amount</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>24</td>
<td>Give Rate Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>25</td>
<td>Give Strength</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>RXE</td>
<td>26</td>
<td>Give Strength Units</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>27</td>
<td>Give Indication</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>28</td>
<td>Dispense Package Size</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>29</td>
<td>Dispense Package Size Unit</td>
<td>CE</td>
<td> </td>
</tr>
<tr class="even">
<td>RXE</td>
<td>30</td>
<td>Dispense Package Method</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: Local Drug</td>
<td>ST</td>
<td> 11135~AMANTADINE HCL 100MG CAP~613_50_.01</td>
</tr>
<tr class="even">
<td>RXE</td>
<td>31(n)</td>
<td>Supplementary Code: CMOP ID</td>
<td>ST</td>
<td> C0255~~613_50_27</td>
</tr>
<tr class="odd">
<td>NTE</td>
<td>1</td>
<td>Set ID - NTE</td>
<td>SI</td>
<td></td>
</tr>
<tr class="even">
<td>NTE</td>
<td>2</td>
<td>Source of Comment</td>
<td>ID</td>
<td></td>
</tr>
<tr class="odd">
<td>NTE</td>
<td>3</td>
<td>Comment</td>
<td>FT</td>
<td>PT OUT RX ON SUSP FOR 24 MORE DAYS</td>
</tr>
<tr class="even">
<td>NTE</td>
<td>4</td>
<td>Comment Type~Name of Coding System</td>
<td>CE</td>
<td>RE~REMARKS~613_50_27</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td> </td>
<td></td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950306</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CG</td>
</tr>
<tr class="even">
<td>FT1</td>
<td>7</td>
<td>Transaction Code (Pharmacy Orderable Item/Name, Coding System)</td>
<td>CE</td>
<td>620~AMANTADINE~~613_52_39.2</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>8</td>
<td>Transaction Description</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>9</td>
<td>Transaction Description - Alt</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>10</td>
<td>Transaction Quantity</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>11</td>
<td>Transaction Amount - Extended</td>
<td>CP</td>
<td> </td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>12</td>
<td>Transaction Amount - Unit</td>
<td>CP</td>
<td>0.009</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>1</td>
<td>Set ID - FT1</td>
<td>SI</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>2</td>
<td>Transaction ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>3</td>
<td>Transaction Batch ID</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td>FT1</td>
<td>4</td>
<td>Transaction Date</td>
<td>TS</td>
<td>19950306</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>5</td>
<td>Transaction Posting Date</td>
<td>TS</td>
<td> </td>
</tr>
<tr class="even">
<td>FT1</td>
<td>6</td>
<td>Transaction Type</td>
<td>IS</td>
<td>CG</td>
</tr>
<tr class="odd">
<td>FT1</td>
<td>7</td>
<td>Transaction Code</td>
<td>CE</td>
<td>1~PSO NSC RX COPAY NEW~500_52_105</td>
</tr>
</tbody>
</table>

<span id="_Toc207089110" class="anchor"></span>Table 35: Pharmacy Header (PHA) 4.2A

## Appendix E: Outpatient Pharmacy ASAP Standard for Prescription Monitoring Programs (PMP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data elements in this standard include those described in the Prescription Monitoring Program Model Act of October 2002 developed by the Alliance of States with Prescription Monitoring Programs and the National Association of State Controlled Substances Authorities.

Per the model act, the information submitted for each prescription, should include, but not be limited to:

- Dispenser identification number
- Date prescription filled
- Prescription number
- Prescription is new or is a refill
- NDC for drug dispensed
- Quantity dispensed
- Number of days supply of the drug
- Patient identification number
- Patient name
- Patient address
- Patient date of birth
- Prescriber identification number
- Date prescription issued by prescriber
- Person who received the prescription from the dispenser, if other than the patient
- Source of payment for prescription
- State issued serial number (If state chooses to establish a serialized prescription system)

### Safety Updates for Medication Prescription Management (SUMPM) Patch \*7\*408 – State Prescription Drug Monitoring Program 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The State Prescription Monitoring Program (SPMP) menu is used to identify prescriptions for controlled substance drugs, Schedule 2 through 5, dispensed by the VA Outpatient Pharmacy facilities, and to create and transmit an export file containing this information to the Prescription Drug Monitoring Programs (PDMP) of each state. This menu allows Veterans Health Administration (VA) Outpatient Pharmacies to comply with mandatory reporting to State Controlled Substance Rx databases as required by the Consolidated Appropriations Act, 2012, PL 112-74.

Each state has established its own PDMP to manage an electronic database that collects designated data on dispensed controlled substances. States distribute data from the database to individuals authorized under state law to receive the information for purposes of their profession. The information is reported to the state using the American Society for Automation in Pharmacy (ASAP) data format, which was developed by the Alliance of States with Prescription Monitoring Programs and the National Association of State Controlled Substances Authorities.

32. Prescription fills Administered in Clinic will not be sent to the states. Only outpatient prescriptions (new and updated) dispensed to patients will be submitted to the states.

### ASAP Segment Hierarchy Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TH — Transaction Header (one per file)

IS — Information Source (one per TH)

PHA — Pharmacy Header (one to 2,000 per IS)

PAT — Patient Information (one to 25,000 per PHA)

DSP — Dispensing Record (one to 300 per PAT)

PRE — Prescriber Information (one per DSP)

CDI — Compound Drug Ingredient Detail (zero to 25 per DSP)

AIR — Additional Information Reporting (zero to one per DSP)

PAT — Patient Information

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

PAT — Patient Information

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

TP — Pharmacy Trailer (one per PHA)

PHA — Pharmacy Header

PAT — Patient Information

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

PAT — Patient Information

DSP — Dispensing Record

PRE — Prescriber Information

CDI — Compound Drug Ingredient Detail

AIR — Additional Information Reporting

TP — Pharmacy Trailer

TT — Transaction Trailer (one per TH)

### SPMP Data Source (PSO\*7\*408) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc207089111" class="anchor"></span>Table 36: Patient Information (PAT) 4.2A</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Element</th>
<th>Name<br />
Description</th>
<th>Data<br />
Source</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">TH–Transaction Header</td>
</tr>
<tr class="even">
<td>TH01</td>
<td><p>Version/Release Number</p>
<p>Code uniquely identifying the transaction</p>
<p>Format = xx.x</p></td>
<td><p><strong>File</strong>: SPMP STATE PARAMETERS (#58.41)</p>
<p><strong>Field</strong>: ASAP VERSION field (#1)</p>
<p><strong>Option</strong>: View/Edit SPMP State Parameters [PSO SPMP STATE PARAMETERS]</p>
<p><strong>Example</strong>: 4.0, 4.1, 4.2</p></td>
</tr>
<tr class="odd">
<td>TH02</td>
<td><p>Transaction Control Number</p>
<p>Sender-assigned code uniquely identifying a transaction</p>
<p>This number must be used in TT01</p></td>
<td><p>ASAP 3.0 : Business Partner Implementation Version (Not Used)<br />
ASAP 4.0+: Transaction Control Number</p>
<p>VA Site Number – Export Batch Number</p>
<p><strong>Example</strong>: 500-3038</p></td>
</tr>
<tr class="even">
<td>TH03</td>
<td><p>Transaction Type</p>
<p>Identifies the purpose of initiating the transaction</p>
<p>01 Send/Request Transaction</p>
<p>02 Acknowledgment (Used in Response only)</p>
<p>03 Error Receiving (Used in Response only)</p>
<p>04 Void (Used to void a specific Rx in a real-time transmission, or an entire batch file that was transmitted)</p></td>
<td>ASAP 3.0 : Transaction Control Number<br />
ASAP 4.0+: Transaction Type (Always "01" - Send/Request Transaction)</td>
</tr>
<tr class="odd">
<td>TH04</td>
<td><p>Response ID</p>
<p>Contains the Transaction Control Number of a transaction that initiated the transaction</p>
<p>Required in response transaction only</p></td>
<td>ASAP 3.0 : Transaction Type (Not Used)<br />
ASAP 4.0+: Response ID (Not Used)</td>
</tr>
<tr class="even">
<td>TH05</td>
<td><p>Creation Date</p>
<p>Date the transaction was created</p>
<p>Format: CCYYMMDD</p></td>
<td><p>ASAP 3.0 : Message Type (Not Used)<br />
ASAP 4.0+: Creation Date (Format: YYYYMMDD)</p>
<p>Date the Export Batch was created</p>
<p><strong>Example</strong>: 20130115</p></td>
</tr>
<tr class="odd">
<td>TH06</td>
<td><p>Creation Time</p>
<p>Time the transaction was created</p>
<p>Format: HHMMSS or HHMM</p></td>
<td><p>ASAP 3.0 : Response ID (Not Used); ASAP 4.0+: Creation Time. Format: HHMMSS or HHMM</p>
<p>Time the Export Batch was created</p>
<p><strong>Example</strong>: 091522</p></td>
</tr>
<tr class="even">
<td>TH07</td>
<td><p>File Type</p>
<p>Code specifying the type of transaction</p>
<p>P Production</p>
<p>T Test</p></td>
<td><p>ASAP 3.0: Project ID (Not Used)<br />
ASAP 4.0+: File Type.</p>
<ul>
<li><p><strong>P</strong> is reported when running from a production account</p></li>
<li><p><strong>T</strong> is reported when running from a non-production account</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>TH08</td>
<td><p>Routing Number</p>
<p>This field is reserved for real-time transmissions that go through a network switch to indicate, if necessary, the specific state PMP to whom the transactions should be routed</p></td>
<td>ASAP 3.0: Creation Date (Format: YYYYMMDD)<br />
ASAP 4.0 : Composite Element Separator (:)<br />
ASAP 4.1+: Routing Number (Real-time transactions only) (Not Used)</td>
</tr>
<tr class="even">
<td>TH09</td>
<td><p>Segment Terminator Character</p>
<p>This terminates the TH segment and sets the actual value of the data segment terminator for the entire transaction</p></td>
<td><p>ASAP 3.0: Creation Time. Format: HHMMSS or HHMM<br />
ASAP 4.0+: Segment Terminator Character</p>
<ul>
<li><p>For ASAP version 4.0, the separator is set to “\” (backward slash)</p></li>
<li><p>For ASAP version 4.0, 4.1 and 4.2, the separator is set to “~” (tilde)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>TH10</td>
<td><p>File Type</p>
<p>Code specifying the type of transaction</p>
<p>P Production</p>
<p>T Test</p></td>
<td><p>ASAP 3.0 only</p>
<ul>
<li><p><strong>P</strong> is reported when running from a production account</p></li>
<li><p><strong>T</strong> is reported when running from a non-production account</p></li>
</ul></td>
</tr>
<tr class="even">
<td>TH11</td>
<td><p>Message</p>
<p>Free-form text message.</p></td>
<td>ASAP 3.0 only (not used)</td>
</tr>
<tr class="odd">
<td>TH12</td>
<td><p>Composite Element Separator</p>
<p>The delimiter used to separate component data elements within a composite data structure.</p></td>
<td>ASAP 3.0 only</td>
</tr>
<tr class="even">
<td>TH13</td>
<td><p>Data Segment Terminator Character</p>
<p>This terminates the TH segment and sets the actual value of the data segment terminator for the entire transaction set</p>
<ol start="33">
<li><p>This Data Element was released as NOT USED because ASAP 3.0 does not require the actual segment terminator value to be in the TH13 field.</p></li>
</ol></td>
<td>ASAP 3.0 only</td>
</tr>
<tr class="odd">
<td colspan="3">IS–Information Source</td>
</tr>
<tr class="even">
<td>IS01</td>
<td><p>Unique Information Source ID</p>
<p>Reference number or identification number as defined by the business partners</p>
<p>Example: Phone number</p></td>
<td><p>VA concatenated with the VA Site Number</p>
<p><strong>Example</strong>: VA500</p></td>
</tr>
<tr class="odd">
<td>IS02</td>
<td><p>Information Source Entity Name</p>
<p>Entity name of the Information Source</p></td>
<td><p><strong>File</strong>: INSTITUTION (#4)</p>
<p><strong>Field</strong>: OFFICIAL VA NAME (#100)</p>
<p><strong>Example</strong>: OKLAHOMA CITY VA MEDICAL CENTER</p></td>
</tr>
<tr class="even">
<td>IS03</td>
<td><p>Message</p>
<p>Free-form text for a message</p>
<p>Used for more detailed information if required by the PMP</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>IS04-IS10</td>
<td>ASAP 3.0 only</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td colspan="3">IR–Information Receiver (ASAP 3.0 Only)</td>
</tr>
<tr class="odd">
<td>IR01</td>
<td><p>Unique Information Receiver ID</p>
<p>Reference number or identification number as defined by the business partners</p>
<p>Example: Phone number</p></td>
<td><p>VA concatenated with the VA Site Number</p>
<p><strong>Example</strong>: VA500</p></td>
</tr>
<tr class="even">
<td>IR02</td>
<td><p>Information Receiver Entity Name</p>
<p>Entity name of the Information Receiver</p></td>
<td><p><strong>File</strong>: STATE (#5)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>Concatenated with “PMP PROGRAM”</p>
<p><strong>Example</strong>: OKLAHOMA PMP PROGRAM</p></td>
</tr>
<tr class="odd">
<td>IR03-IR10</td>
<td>ASAP 3.0 only</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td colspan="3">PHA–Pharmacy Header</td>
</tr>
<tr class="odd">
<td>PHA01</td>
<td><p>National Provider Identifier (NPI)</p>
<p>Identifier assigned to the pharmacy by Centers for Medicare and Medicaid Services (CMS)</p>
<p>Used if required by the PMP</p></td>
<td><p>Retrieved via the Registration API $$NPI^XUSNPI (ICR # 4532) using the NPI INSTITUTION field (#101) in the OUTPATIENT SITE file (#59)</p>
<p><strong>Example</strong>: 1043278211</p></td>
</tr>
<tr class="even">
<td>PHA02</td>
<td><p>NCPDP/NABP Provider ID</p>
<p>Identifier assigned to the pharmacy by the NCPDP/NABP.</p>
<p>Used if required by the PMP</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: NCPDP NUMBER (#1008)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: 3706972</p></td>
</tr>
<tr class="odd">
<td>PHA03</td>
<td><p>DEA Number</p>
<p>Identifier assigned to the pharmacy by the Drug Enforcement Administration (DEA)</p>
<p>Used if required by the PMP</p></td>
<td><p>Retrieved via the Registration API $$WHAT^XUAF4 (ICR # 2171) using the RELATED INSTITUTION field (#100) in the OUTPATIENT SITE file (#59)</p>
<p><strong>Example</strong>: AV4597211</p></td>
</tr>
<tr class="even">
<td>PHA04</td>
<td><p>Pharmacy Name or Dispensing Prescriber Name</p>
<p>Free-form text for the name of the pharmacy</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: OKLAHOMA CITY</p></td>
</tr>
<tr class="odd">
<td>PHA05</td>
<td><p>Address Information – 1</p>
<p>Free-form text for address information</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: MAILING FRANK STREET (#.02)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: 921 N.E. 13th. Street (119)</p></td>
</tr>
<tr class="even">
<td>PHA06</td>
<td><p>Address Information – 2</p>
<p>Free-form text for additional address information</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PHA07</td>
<td><p>City Address</p>
<p>Free-form text for city name</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: MAILING FRANK CITY (#.07)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: OKLAHOMA CITY</p></td>
</tr>
<tr class="even">
<td>PHA08</td>
<td><p>State Address</p>
<p>U.S. Postal Service state code</p></td>
<td><p><strong>File</strong>: STATE (#5)</p>
<p><strong>Field</strong>: ABBREVIATION (#1)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p>Example: OK</p>
<p><strong>Note</strong>: The pointer to STATE file (#5) is retrieved from OUTPATIENT SITE file (#59) MAILING FRANK STATE field (#.08).</p></td>
</tr>
<tr class="odd">
<td>PHA09</td>
<td><p>ZIP Code Address</p>
<p>U.S. Postal Service ZIP code<br />
Use if available</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: MAILING FRANK ZIP+4 CODE (#.05)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: 731045028 (no dash)</p></td>
</tr>
<tr class="even">
<td>PHA10</td>
<td><p>Phone Number</p>
<p>Complete phone number including area code</p></td>
<td><p><strong>File</strong>: OUTPATIENT SITE (#59)</p>
<p><strong>Field</strong>: PHONE NUMBER (#.04)</p>
<p><strong>Option</strong>: Site Parameter Enter/Edit [PSO SITE PARAMETERS]</p>
<p><strong>Example</strong>: 4056948387 (no dashes)</p></td>
</tr>
<tr class="odd">
<td>PHA11</td>
<td><p>Contact Name</p>
<p>Free-form text for contact name</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>PHA12</td>
<td><p>Chain Site ID</p>
<p>Store number assigned by the chain to the pharmacy location</p>
<p>Used when PMP needs to identify the specific pharmacy from which information is required</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PHA13</td>
<td><p>Message</p>
<p>Free-form text message</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td colspan="3">PAT–Patient Information</td>
</tr>
<tr class="odd">
<td>PAT01</td>
<td><p>ID Qualifier of Patient Identifier</p>
<p>Code identifying the jurisdiction that issues the ID in PAT03</p>
<p>Used if the PMP requires such identification</p></td>
<td>Always <strong>US</strong> (United States), except ASAP 3.0 (not used)</td>
</tr>
<tr class="even">
<td>PAT02</td>
<td><p>ID Qualifier</p>
<p>Code to identify the type of ID in PAT03. If PAT02 is used, PAT03 is required</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID)</p></td>
<td>Always <strong>07</strong> (Social Security Number)</td>
</tr>
<tr class="odd">
<td>PAT03</td>
<td><p>ID of Patient</p>
<p>Identification number for the patient as indicated in PAT02</p>
<p>An example would be the driver’s license number</p></td>
<td><p>ASAP 3.0 : Unique System ID - Patient (Not Used)<br />
ASAP 4.0+: ID of Patient (SSN)</p>
<p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(2)</p>
<p><strong>Example</strong>: 666554444 (no dashes)</p></td>
</tr>
<tr class="even">
<td>PAT04</td>
<td><p>ID Qualifier of Additional Patient Identifier</p>
<p>Code identifying the jurisdiction that issues the ID in PAT06</p>
<p>Used if the PMP requires such identification</p></td>
<td><p>ASAP 3.0 : SSN</p>
<p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(2)</p>
<p><strong>Example</strong>: 666554444 (no dashes)<br />
ASAP 4.0+: ID Qualifier of Additional Patient Identifier (Not Used)</p></td>
</tr>
<tr class="odd">
<td>PAT05</td>
<td><p>Additional Patient ID Qualifier</p>
<p>Code to identify the type of ID in PAT06 if the PMP requires a second identifier</p>
<p>If PAT05 is used, PAT06 is required</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID)</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>PAT06</td>
<td><p>Additional ID</p>
<p>Identification that might be required by the PMP to further identify the individual</p>
<p>An example: in PAT03, driver’s license is required and in PAT06, Social Security number is also required</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PAT07</td>
<td><p>Last Name</p>
<p>Patient’s last name</p></td>
<td><p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(1) – first value before the comma (e.g., SMITH, JOHN F)</p>
<p><strong>Example</strong>: SMITH</p></td>
</tr>
<tr class="even">
<td>PAT08</td>
<td><p>First Name</p>
<p>Patient’s first name</p></td>
<td><p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(1) – first value after the comma and before blank space (e.g., SMITH, JOHN F)</p>
<p>Example: JOHN</p></td>
</tr>
<tr class="odd">
<td>PAT09</td>
<td><p>Middle Name</p>
<p>Patient’s middle name or initial if available</p>
<p>Used if available in pharmacy system and required by the PMP</p></td>
<td><p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(1) –value following the first name (e.g., SMITH, JOHN F)</p>
<p>Example: F</p></td>
</tr>
<tr class="even">
<td>PAT10</td>
<td><p>Name Prefix</p>
<p>Patient’s name prefix such as Mr. or Dr.</p>
<p>Used if available in pharmacy system and required by the PMP</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PAT11</td>
<td><p>Name Suffix</p>
<p>Patient’s name prefix such as Jr. or the III</p>
<p>Used if available in pharmacy system and required by the PMP</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>PAT12</td>
<td><p>Address Information – 1</p>
<p>Free-form text for street address information</p></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(1)</p>
<p><strong>Example</strong>: 1235 STREET NAME ST</p></td>
</tr>
<tr class="odd">
<td>PAT13</td>
<td><p>Address Information – 2</p>
<p>Free-form text for additional address information, if required by the PMP and is available in the pharmacy system</p></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(2)</p>
<p><strong>Example</strong>: BLDG 101 APT #102</p></td>
</tr>
<tr class="even">
<td>PAT14</td>
<td><p>City Address</p>
<p>Free-form text for city name</p></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(4)</p>
<p><strong>Example</strong>: ARDMORE</p></td>
</tr>
<tr class="odd">
<td>PAT15</td>
<td><p>State Address</p>
<p>U.S. Postal Service state code if required by the PMP</p>
<ol start="34">
<li><p>Field was sized to handle international patients not residing in the U.S.</p></li>
</ol></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(5)</p>
<p>Example: OK</p></td>
</tr>
<tr class="even">
<td>PAT16</td>
<td><p>ZIP Code Address</p>
<p>U.S. Postal Service ZIP code</p>
<p>Populate with zeros if the patient address is outside the U.S.</p></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(6)</p>
<p><strong>Example</strong>: 723005500 (no dash)</p></td>
</tr>
<tr class="odd">
<td>PAT17</td>
<td><p>Phone Number</p>
<p>Complete phone number including the area code when the PMP requires and is available in the pharmacy system</p></td>
<td><p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(8)</p>
<p><strong>Example</strong>: 4245556666 (no dashes)</p></td>
</tr>
<tr class="even">
<td>PAT18</td>
<td><p>Date of Birth</p>
<p>Date patient was born</p>
<p>Format: CCYYMMDD</p></td>
<td><p>ASAP 3.0 : Email Address (Not Used)<br />
ASAP 4.0+: Patient DOB</p>
<p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(3)</p>
<p><strong>Example</strong>: 19661112</p></td>
</tr>
<tr class="odd">
<td>PAT19</td>
<td><p>Gender Code</p>
<p>Code indicating the sex of the patient if required by the PMP</p>
<p>F Female</p>
<p>M Male</p>
<p>U Unknown</p></td>
<td><p>ASAP 3.0 : Patient DOB<br />
Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(3)</p>
<p><strong>Example</strong>: 19661112</p>
<p>ASAP 4.0+: Patient Gender Code</p>
<p>Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(5).</p>
<p>If no value is found ,reports <strong>U</strong></p>
<p>Example: F</p></td>
</tr>
<tr class="even">
<td>PAT20</td>
<td><p>Species Code</p>
<p>Used if required by the PMP to differentiate a prescription for an individual from one prescribed for an animal</p>
<p>01 Human</p>
<p>02 Veterinary Patient</p></td>
<td><p>ASAP 3.0 : Patient Gender Code<br />
Retrieved via the Registration API $$DEM^VADPT (ICR #10061) return variable VADM(5).</p>
<p>If no value is found ,reports <strong>U</strong></p>
<p>ASAP 4.0+: Species Code</p>
<p>Always <strong>01</strong> (Human)</p></td>
</tr>
<tr class="odd">
<td>PAT21</td>
<td><p>Patient Location Code</p>
<p>Code indicating where the patient is located when receiving pharmacy services if required by the PMP</p>
<p>01 Home</p>
<p>02 Intermediary Care</p>
<p>03 Nursing Home</p>
<p>04 Long-Term/Extended Care</p>
<p>05 Rest Home</p>
<p>06 Boarding Home</p>
<p>07 Skilled-Care Facility</p>
<p>08 Sub-Acute Care Facility</p>
<p>09 Acute-Care Facility</p>
<p>10 Outpatient</p>
<p>11 Hospice</p>
<p>98 Unknown</p>
<p>99 Other</p></td>
<td>Always <strong>10</strong> (Outpatient)</td>
</tr>
<tr class="even">
<td>PAT22</td>
<td><p>Country of Non-U.S. Resident</p>
<p>Used when the patient’s address is a foreign country and PAT12 through PAT16 are left blank.</p>
<p>This is a free-form text field</p></td>
<td><p>ASAP 3.0 : Primary Prescription Coverage Type (Not Used)<br />
ASAP 4.0+:Country of Non-U.S. Resident</p>
<p>Retrieved via the Registration API $$ADD^VADPT (ICR #10061) return variable VAPA(25)</p>
<p>Example: MX</p></td>
</tr>
<tr class="odd">
<td>PAT23-PAT40</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">DSP–Dispensing Record</td>
</tr>
<tr class="odd">
<td>DSP01</td>
<td><p>Reporting Status</p>
<p>DSP01 requires one of the codes below. An empty or blank field no longer indicates a new prescription dispensing transaction. Individual PMPs may elect to require a subset of the codes below, specifically 00 and 02, but not 01.</p>
<p>00 New Record (indicates a new prescription dispensing transaction)</p>
<p>01 Revise (indicates that one or more data element values in a previously submitted transaction will be revised)</p>
<p>02 Void (message to the PMP to remove the original prescription transaction from its database, to mark the record as invalid, or to be ignored)</p></td>
<td><p>ASAP 4.0</p>
<ul>
<li><p>(Blank) New Record</p></li>
<li><p>01 Revise Record</p></li>
<li><p>02 Void Record</p></li>
<li><p>ASAP 4.1 and 4.2</p></li>
<li><p>00 New Record</p></li>
<li><p>01 Revise Record</p></li>
<li><p>02 Void Record</p></li>
</ul></td>
</tr>
<tr class="even">
<td>DSP02</td>
<td><p>Prescription Number</p>
<p>Serial number assigned to the prescription by the pharmacy</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: RX # (#.01)</p>
<p><strong>Example</strong>: 10930393</p></td>
</tr>
<tr class="odd">
<td>DSP03</td>
<td><p>Date Written</p>
<p>Date the prescription was written (authorized)</p>
<p>Format: CCYYMMDD</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: ISSUE DATE (#1)</p>
<p><strong>Example</strong>: 20130117</p></td>
</tr>
<tr class="even">
<td>DSP04</td>
<td><p>Refills Authorized</p>
<p>Number of refills authorized by the prescriber</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: # OF REFILLS (#9)</p>
<p>Example: 5</p></td>
</tr>
<tr class="odd">
<td>DSP05</td>
<td><p>Date Filled</p>
<p>Date prescription was filled</p>
<p>Format: CCYYMMDD</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: RELEASED DATE/TIME (#31)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: RELEASED DATE/TIME (#17)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>Sub-File</strong>: PARTIAL (#52.2)</p>
<p><strong>Field</strong>: RELEASED DATE/TIME (#8)</p>
<p><strong>Example</strong>: 20130118</p></td>
</tr>
<tr class="even">
<td>DSP06</td>
<td><p>Refill Number</p>
<p>Number of the fill of the prescription</p>
<p>0 indicates original dispensing</p>
<p>01-99 is the refill number</p></td>
<td><ul>
<li><p>Original</p></li>
</ul>
<p>0</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p>Refill # (e.g., 1, 2, …)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p>0</p></td>
</tr>
<tr class="odd">
<td>DSP07</td>
<td><p>Product ID Qualifier</p>
<p>Used to identify the type of product ID contained in DSP08</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 Compound (used to indicate it is a compound’ if used, the CDI segment then becomes a required segment)</p></td>
<td>Always <strong>01</strong> (NDC)</td>
</tr>
<tr class="even">
<td>DSP08</td>
<td><p>Product ID</p>
<p>Full product identification as indicated in DSP07, including leading zeros without punctuation</p>
<p>If the product is a compound, use 99999 for the first five characters of the product code. The remaining characters are assigned by the pharmacy. The CDI then becomes a required segment.</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: NDC (#27)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: NDC (#11)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: NDC (#27)</p>
<p><strong>Example</strong>: 55555444422 (no dashes)</p></td>
</tr>
<tr class="odd">
<td>DSP09</td>
<td><p>Quantity Dispensed</p>
<p>Number of metric units dispensed in metric decimal format</p>
<p>Example: 2.5</p>
<ol start="35">
<li><p>For compounds, show the first quantity in CDI04.</p></li>
</ol></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: QTY (#7)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: QTY (#1)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>Sub-File</strong>: PARTIAL (#52.2)</p>
<p><strong>Field</strong>: QTY (#.04)</p>
<p><strong>Example</strong>: 55555444422 (no dashes)</p></td>
</tr>
<tr class="even">
<td>DSP10</td>
<td><p>Days Supply</p>
<p>Estimated number of days the medication will cover</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: DAYS SUPPLY (#8)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: DAYS SUPPLY (#1.1)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>Sub-File</strong>: PARTIAL (#52.2)</p>
<p><strong>Field</strong>: QTY (#.041)</p>
<p>Example: 90</p></td>
</tr>
<tr class="odd">
<td>DSP11</td>
<td><p>Drug Dosage Units Code</p>
<p>Identifies the unit of measure for the quantity dispensed in DSP09, if required by the PMP</p>
<p>01 Each (used to report solid dosage units or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td><p><strong>File</strong>: DRUG (#50)</p>
<p><strong>Field</strong>: NCPDP DISPENSE UNIT (#82)</p>
<ul>
<li><p>01 EA</p></li>
<li><p>02 ML</p></li>
<li><p>03 GM</p></li>
<li><p>(Blank) Other</p></li>
</ul></td>
</tr>
<tr class="even">
<td>DSP12</td>
<td><p>Transmission Form of Rx Origin Code</p>
<p>Code indicating how the pharmacy received the prescription, if required by the PMP</p>
<p>01 Written Prescription</p>
<p>02 Telephone Prescription</p>
<p>03 Telephone Emergency Prescription</p>
<p>04 Fax Prescription</p>
<p>05 Electronic Prescription</p>
<p>99 Other</p></td>
<td><p>The CPRS API $$NATURE^ORUTL3 (IA# 5890) provides the Nature of Order, which is translated the following way:</p>
<ul>
<li><p>01 W</p></li>
<li><p>02 V or T</p></li>
<li><p>05 E</p></li>
<li><p>99 Other</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DSP13</td>
<td><p>Partial Fill Indicator</p>
<p>Used when the quantity in DSP09 is less than the met quantity per dispensing authorized by the prescriber. This dispensing activity is often referred to as a split filling.</p>
<p>00 Not a Partial Fill</p>
<p>01 First Partial Fill</p>
<ol start="36">
<li><p>For additional fills per prescription, increment by 1. The second partial fill is reported as 02, up to a maximum of 99.</p></li>
</ol></td>
<td><p>ASAP 4.0 and 4.1</p>
<ul>
<li><p>01 Partial Fill</p></li>
<li><p>02 Non-Partial Fill</p></li>
</ul>
<p>ASAP 4.2 and above</p>
<ul>
<li><p>00 Non-Partial Fill</p></li>
<li><p>01 Partial 1</p></li>
<li><p>02 Partial 2</p></li>
<li><p>03 Partial 3</p></li>
</ul></td>
</tr>
<tr class="even">
<td>DSP14</td>
<td><p>Pharmacist National Provider Identifier (NPI)</p>
<p>Identifier assigned to the pharmacist by CMS if the pharmacist applies for a number</p>
<p>This number can be used to identify the pharmacist dispensing the medication</p></td>
<td><p>Retrieved via the Registration API $$NPI^XUSNPI (ICR # 4532) using the prescription fill pharmacist.</p>
<p><strong>Example</strong>: 1043278211</p></td>
</tr>
<tr class="odd">
<td>DSP15</td>
<td><p>Pharmacist State License Number</p>
<p>This data element can be used to identify the pharmacist dispensing the medication</p>
<p>Assigned to the pharmacist by the State Licensing Board</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>DSP16</td>
<td><p>Classification Code for Payment Type</p>
<p>Code identifying the type of payment, i.e. how it was paid for, if required by the PMP</p>
<p>01 Private Pay (Cash, Charge, Credit Card)</p>
<p>02 Medicaid</p>
<p>03 Medicare</p>
<p>04 Commercial Insurance</p>
<p>05 Military Installations and VA</p>
<p>06 Workers’ Compensation</p>
<p>07 Indian Nations</p>
<p>99 Other</p></td>
<td>Always <strong>05</strong> (Military Installations and VA)</td>
</tr>
<tr class="odd">
<td>DSP17</td>
<td><p>Date Sold</p>
<p>Usage of this field depends on the pharmacy having a point-of-sale system that is integrated with the pharmacy management system to allow a bidirectional flow of information, and the PMP requires the capturing of the date received by the patient or the patient’s agent</p>
<p>This date may be different from DSP05</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>DSP18</td>
<td><p>RxNorm Product Qualifier</p>
<p>01 Semantic Clinical Drug (SCD)</p>
<p>02 Semantic Branded Drug (SBD)</p>
<p>03 Generic Package (GPCK)</p>
<p>04 Branded Package (BPCK)</p>
<ol start="37">
<li><p>DSP18 and DSP19 are placeholder fields pending RxNorm becoming an industry standard and should not be required until such time.</p></li>
</ol></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP19</td>
<td><p>RxNorm Code</p>
<p>Used for electronic prescriptions to capture the prescribed drug product identification, if required by the PMP.</p>
<ol start="38">
<li><p>DSP18 and DSP19 are placeholder fields pending RxNorm becoming an industry standard and should not be required until such time.</p></li>
</ol></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>DSP20</td>
<td><p>Electronic Prescription Reference Number</p>
<p>Used to provide an audit trail for electronic prescriptions, if required by the PMP</p>
<ol start="39">
<li><p>DSP20 and DSP21 should be reported as a pair to the prescription drug monitoring program, and each program decides which one, if not both, it decides to capture.</p></li>
</ol></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP21</td>
<td><p>Electronic Prescription Order Number</p>
<ol start="40">
<li><p>DSP20 and DSP21 should be reported as a pair to the prescription drug monitoring program, and each program decides which one, if not both, it decides to capture.</p></li>
</ol></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td colspan="3">RX – RX Prescription Order (ASAP 3.0 only)</td>
</tr>
<tr class="odd">
<td>RX01</td>
<td><p>Reporting Status</p>
<p>00 Add</p>
<p>01 Change</p>
<p>02 Delete</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>RX02</td>
<td><p><strong>Program Participation Status</strong></p>
<p>Code to reflect the current status of the prescription in relation to program participation (i.e., refill reminder or education enrollment).</p>
<blockquote>
<p>01 Rx is active and participation is current</p>
<p>02 Rx order has been discontinued by prescriber</p>
<p>03 Patient has refused participation for this Rx</p>
<p>04 Patient has requested disenrollment for this Rx</p>
</blockquote></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>RX03</td>
<td><p>Prescription Number</p>
<p>Serial number assigned to the prescription by the pharmacy</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: RX # (#.01)</p>
<p><strong>Example</strong>: 10930393</p></td>
</tr>
<tr class="even">
<td>RX04-RX07</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>RX08</td>
<td><p>Date Rx Written</p>
<p>Date the prescription was written (authorized)</p>
<p>Format: CCYYMMDD</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: ISSUE DATE (#1)</p>
<p><strong>Example</strong>: 20130117</p></td>
</tr>
<tr class="even">
<td>RX09-RX012</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>RX13</td>
<td><p>Product ID Qualifier</p>
<p>Used to identify the type of product ID contained in DSP08</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p></td>
<td>Always <strong>01</strong> (NDC)</td>
</tr>
<tr class="even">
<td>RX14</td>
<td><p>Product ID</p>
<p>Full product identification as indicated in RX13, including leading zeros without punctuation</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: NDC (#27)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: NDC (#11)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: NDC (#27)</p>
<p><strong>Example</strong>: 55555444422 (no dashes)</p></td>
</tr>
<tr class="odd">
<td>RX15-RX16</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="even">
<td>RX17</td>
<td><p>Quantity Prescribed</p>
<p>Number of metric units dispensed in metric decimal format.</p>
<p>Example: 2.5</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: QTY (#7)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: QTY (#1)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>Sub-File</strong>: PARTIAL (#52.2)</p>
<p><strong>Field</strong>: QTY (#.04)</p>
<p><strong>Example</strong>: 55555444422 (no dashes)</p></td>
</tr>
<tr class="odd">
<td>RX18</td>
<td><p>Days Supply</p>
<p>Estimated number of days the medication will cover</p></td>
<td><ul>
<li><p>Original Fill</p></li>
</ul>
<p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: DAYS SUPPLY (#8)</p>
<ul>
<li><p>Refill</p></li>
</ul>
<p><strong>Sub-File</strong>: REFILL (#52.1)</p>
<p><strong>Field</strong>: DAYS SUPPLY (#1.1)</p>
<ul>
<li><p>Partial</p></li>
</ul>
<p><strong>Sub-File</strong>: PARTIAL (#52.2)</p>
<p><strong>Field</strong>: QTY (#.041)</p>
<p>Example: 90</p></td>
</tr>
<tr class="even">
<td>RX19</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>RX20</td>
<td><p>Number Of Refills Authorized</p>
<p>Number of refills authorized by the prescriber</p></td>
<td><p><strong>File</strong>: PRESCRIPTION (#52)</p>
<p><strong>Field</strong>: # OF REFILLS (#9)</p>
<p>Example: 5</p></td>
</tr>
<tr class="even">
<td>RX21-RX29</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">PRE – Prescriber Information</td>
</tr>
<tr class="even">
<td>PRE01</td>
<td><p>National Provider Identifier (NPI)</p>
<p>Identifier assigned to the prescriber by CMS</p></td>
<td><p>ASAP 3.0 : Not Used<br />
ASAP 4.0+: Prescriber National Provider Identifier (NPI)</p>
<p>Retrieved via the Registration API $$NPI^XUSNPI (ICR # 4532) using the prescription fill provider</p>
<p><strong>Example</strong>: 1043278211</p></td>
</tr>
<tr class="odd">
<td>PRE02</td>
<td><p>DEA Number</p>
<p>Identifying number assigned to a prescriber or an institution by the Drug Enforcement Administration (DEA)</p></td>
<td><p>ASAP 3.0 : Not Used<br />
ASAP 4.0+: Prescriber DEA Number</p>
<p>First “-“ (dash) piece of the value returned by the Registration API $$DEA^XUSER (ICR # 2343) using the prescription fill provider</p>
<p><strong>Example</strong>: AV4598251</p></td>
</tr>
<tr class="even">
<td>PRE03</td>
<td><p>DEA Number Suffix</p>
<p>Identifying number assigned to a prescriber by an institution when the institution’s number is used as the DEA number, if required by the PMP</p></td>
<td><p>ASAP 3.0 : Prescriber NPI<br />
ASAP 4.0+: Prescriber DEA Number Suffix</p>
<p>Second “-“ (dash) piece of the value returned by the Registration API $$DEA^XUSER (ICR # 2343) using the prescription fill provider</p>
<p><strong>Example</strong>: 4598251PP</p></td>
</tr>
<tr class="odd">
<td>PRE04</td>
<td><p>Prescriber State License Number</p>
<p>Identification assigned to the Prescriber by the State Licensing Board</p>
<p>Used if required by the PMP</p></td>
<td>ASAP 3.0 : Prescriber DEA Number<br />
ASAP 4.0+: Prescriber State License Number (Not Used)</td>
</tr>
<tr class="even">
<td>PRE05</td>
<td><p>Last Name</p>
<p>Prescriber’s last name</p>
<p>Used if required by the PMP</p></td>
<td><p>ASAP 3.0 : Prescriber DEA Number Suffix<br />
ASAP 4.0+: Prescriber Last Name</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value before the comma (e.g., <strong>SMITH</strong>, JOHN F)</p>
<p><strong>Example</strong>: SMITH</p></td>
</tr>
<tr class="odd">
<td>PRE06</td>
<td><p>First Name</p>
<p>Prescriber’s first name</p>
<p>Used if required by the PMP</p></td>
<td><p>ASAP 3.0 : Prescriber State License Number (Not Used)<br />
ASAP 4.0+: Prescriber First Name</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and before blank space (e.g., SMITH, <strong>JOHN</strong> F)</p>
<p>Example: JOHN</p></td>
</tr>
<tr class="even">
<td>PRE07</td>
<td><p>Middle Name</p>
<p>Prescriber’s middle name or initial</p>
<p>Used if required by the PMP and is available in the pharmacy system</p></td>
<td><p>ASAP 3.0 : Prescriber Alternate ID (Not Used)<br />
ASAP 4.0+: Prescriber Middle Name</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and after the first blank space (e.g., SMITH, JOHN <strong>F</strong>)</p>
<p>Example: F</p></td>
</tr>
<tr class="odd">
<td>PRE08</td>
<td><p>Phone Number</p>
<p>Prescriber’s phone number</p></td>
<td><p>ASAP 3.0 : Prescriber's Last Name<br />
ASAP 4.0 &amp; 4.1: N/A (up to PRE07 only)<br />
ASAP 4.2: Prescriber's Phone Number</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: PHONE NUMBER # (#.132)</p>
<p><strong>Example</strong>: 5559998888 (no dashes)</p></td>
</tr>
<tr class="even">
<td>PRE09</td>
<td><p>Prescriber' First Name</p>
<p>Prescriber’s first name</p></td>
<td><p>ASAP 3.0 Only</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and before blank space (e.g., SMITH, <strong>JOHN</strong> F)</p>
<p>Example: JOHN</p></td>
</tr>
<tr class="odd">
<td>PRE10</td>
<td><p>Prescriber' Middle Name</p>
<p>Prescriber’s middle name</p></td>
<td><p>ASAP 3.0 Only</p>
<p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and after the first blank space (e.g., SMITH, JOHN <strong>F</strong>)</p>
<p>Example: F</p></td>
</tr>
<tr class="even">
<td>PRE11-PRE20</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">RPH – Pharmacist Information (ASAP 3.0 only)</td>
</tr>
<tr class="even">
<td>RPH01-RPH02</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>RPH03</td>
<td><p>National Provider Identification (NPI)</p>
<p>Identifier assigned to the pharmacist by CMS if the pharmacist applies for a number. This number is used to identify the pharmacist who dispensed the medication.</p></td>
<td><p>Retrieved via the Registration API $$NPI^XUSNPI (ICR # 4532) using the prescription fill pharmacist.</p>
<p><strong>Example</strong>: 1043278211</p></td>
</tr>
<tr class="even">
<td>RPH04-RPH05</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td>RPH06</td>
<td><p>Last Name</p>
<p>Pharmacist’s last name</p></td>
<td><p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value before the comma (e.g., <strong>SMITH</strong>, JOHN F)</p>
<p><strong>Example</strong>: SMITH</p></td>
</tr>
<tr class="even">
<td>RPH07</td>
<td><p>First Name</p>
<p>Pharmacist’s first name</p></td>
<td><p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and before blank space (e.g., SMITH, <strong>JOHN</strong> F)</p>
<p>Example: JOHN</p></td>
</tr>
<tr class="odd">
<td>RPH08</td>
<td><p>Middle Name</p>
<p>Pharmacist’s middle name or initial</p></td>
<td><p><strong>File</strong>: NEW PERSON (#200)</p>
<p><strong>Field</strong>: NAME (#.01)</p>
<p>First value after the comma and after the first blank space (e.g., SMITH, JOHN <strong>F</strong>)</p>
<p>Example: F</p></td>
</tr>
<tr class="even">
<td>RPH09-RPH11</td>
<td>Not Used</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">CDI – Compound Drug Ingredient Detail (Not Used)</td>
</tr>
<tr class="even">
<td colspan="3">CSR – Controlled Substance Reporting (ASAP 3.0 only – Not Used)</td>
</tr>
<tr class="odd">
<td colspan="3">AIR – Additional Information Reporting (Not Used)</td>
</tr>
<tr class="even">
<td colspan="3">PLN – Third-Party Plan (ASAP 3.0 Only – Not Used)</td>
</tr>
<tr class="odd">
<td colspan="3">TP–Pharmacy Trailer</td>
</tr>
<tr class="even">
<td>TP01</td>
<td><p>Detail Segment Count</p>
<p>Number of detail segments included for the pharmacy, including the Pharmacy Header (PHA) including the Pharmacy Trailer (TP) segments</p></td>
<td>Calculated for each transmission</td>
</tr>
<tr class="odd">
<td colspan="3">TT–Transaction Trailer</td>
</tr>
<tr class="even">
<td>TT01</td>
<td><p>Transaction Control Number</p>
<p>Identifying control number that must be unique</p>
<p>Assigned by the originator of the transaction</p>
<p>Must match the number in TH02</p></td>
<td>Same as TH02</td>
</tr>
<tr class="odd">
<td>TT02</td>
<td><p>Segment Count</p>
<p>Total number of segments included in the transaction including the header and trailer segments</p></td>
<td>Calculated for each transmission</td>
</tr>
</tbody>
</table>

<span id="_Toc207089111" class="anchor"></span>Table 36: Patient Information (PAT) 4.2A

| Segment                                                                            | Element ID | Element Name                                | Requirement |
|------------------------------------------------------------------------------------|------------|---------------------------------------------|-------------|
| TH: Transaction Header (required)                                                  |            |                                             |             |
|                                                                                    | TH01       | 4.2                                         | R           |
|                                                                                    | TH02       | 123456                                      | R           |
|                                                                                    | TH05       | 20150101                                    | R           |
|                                                                                    | TH06       | 223000                                      | R           |
|                                                                                    | TH07       | P                                           | R           |
|                                                                                    | TH09       | \\                                          | R           |
| IS: Information Source (required)                                                  |            |                                             |             |
|                                                                                    | IS01       | 7705555555                                  | R           |
|                                                                                    | IS02       | PHARMACY NAME                               | R           |
|                                                                                    | IS03       | Date Range of Report \#YYYYMMDD#-#YYYYMMDD# | R           |
| PHA: Pharmacy Header (required)                                                    |            |                                             |             |
|                                                                                    | PHA03      | ZZ1234567                                   | R           |
| PAT: Patient Information (required)                                                |            |                                             |             |
|                                                                                    | PAT07      | REPORT                                      | R           |
|                                                                                    | PAT08      | ZERO                                        | R           |
| DSP: Dispensing Record (required)                                                  |            |                                             |             |
|                                                                                    | DSP05      | 20150101                                    | R           |
| PRE: Prescriber Information (required; can be null as follows: PRE\*\*\*\*\*\*\*\\ |            |                                             |             |
| CDI: Compound Drug Ingredient Detail                                               |            |                                             |             |
| AIR: Additional Information Reporting                                              |            |                                             |             |
| TP: Pharmacy Trailer (required)                                                    |            |                                             |             |
|                                                                                    | TP01       | 7                                           | R           |
| TT: Transaction Trailer (required)                                                 |            |                                             |             |
|                                                                                    | TT01       | 123456                                      | R           |
|                                                                                    | TT02       | 10                                          | R           |

<span id="_Toc207089112" class="anchor"></span>Table 37: Dispensing Record (DSP) 4.2A

Sample Zero Report

The following example illustrates a zero report using the above values.

TH\*4.2\*123456\*01\*\*20150108\*223000\*P\*\*\\

IS\*7705555555\*PHARMACY NAME\*#20150101#-#20150107#\\

PHA\*\*\* ZZ1234567\\

PAT\*\*\*\*\*\*\*REPORT\*ZERO\*\*\*\*\*\*\*\*\*\*\*\*\\

DSP\*\*\*\*\*20150108\*\*\*\*\*\*\\

PRE\*\\

CDI\*\\

AIR\*\\

TP\*7\\

TT\*123456\*10\\

### SPMP Data Source (PSO\*7\*772)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ASAP Standard Version 4.2A Implementation

<table>
<caption><p><span id="_Toc207089113" class="anchor"></span>Table 38: Prescriber Information (PRE) 4.2A</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TH-Transaction Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To indicate the start of a transaction. It also assigns the segment terminator, data element separator, and control number.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TH01 - Version / Release Number</td>
<td><p>Code uniquely identifying the transaction. Format = x.x</p>
<p>4.2A ASAP Version 4 Release 2A</p></td>
<td>$$TH01^PSOASAP()</td>
<td>ASAP VERSION field (#1) retrieved from the SPMP STATE PARAMETERS file (#58.41)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH02 - Transaction Control Number</td>
<td><p>Sender assigned code uniquely identifying a transaction. This number must be used in TT01.</p>
<p>Recommendation: Use a Globally Unique Identifier (GUID) or other nonrepeating alphanumeric combination to populate this field.</p></td>
<td>$$TH02^PSOASAP()</td>
<td><p>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file.</p>
<p>(ex: 500-182)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH03 - Transaction Type</td>
<td><p>Identifies the purpose of initiating the transaction.</p>
<p>01 Send/Request Transaction</p>
<p>02 Acknowledgment (Used in Response only.)</p>
<p>03 Error Receiving (Used in Response only.)</p>
<p>04 Void (Used to void a specific Rx in a real-time transmission, or an entire batch file that has been transmitted.</p>
<p>When 04 is used the appropriate transaction control number in TH02 for the specific prescription or batch file must be included. When 04 is used only the TH Header Segment and the Transaction Trailer Segment are used.)</p></td>
<td>$$TH03^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>TH04 - Response ID</td>
<td>Contains the Transaction Control Number of a transaction that initiated the transaction. Required in response transaction only.</td>
<td>$$TH04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH05 - Creation Date</td>
<td><p>Date the transaction was created.</p>
<p>Format: CCYYMMDD.</p></td>
<td>$$TH05^PSOASAP()</td>
<td><p>Kernel API - $$FMTHL7^XLFDT($$HTFM^XLFDT($H)</p>
<p>Example: 20240904</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH06 - Creation Time</td>
<td>Time the transaction was created. Format: HHMMSS or HHMM. Do not use colons or other non-numeric characters.</td>
<td>$$TH06^PSOASAP()</td>
<td><ol type="1">
<li><p>Call Kernel API - $$HTFM^XLFDT($H)which returns back UTC date/time</p></li>
</ol>
<blockquote>
<p>Example: 091522</p>
</blockquote>
<ol start="2" type="1">
<li><p>Take the TIME value of the returned date/time stamp and set that data to be exactly 6 in length and append a ""Z"" to the end.</p></li>
</ol></td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH07 - File Type</td>
<td><p>Code specifying the type of transaction.</p>
<p>P Production</p>
<p>T Test</p></td>
<td>$$THO7^PSOASAP()</td>
<td>Retrieved via the Kernel API - $$PROD^XUPROD(1)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH08 - Routing Number/BIN</td>
<td>This field can be used for real-time transmissions that go through an intermediary or network switch to indicate, if necessary, the specific state that the transactions should be routed to.</td>
<td>$$TH08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH09 - Segment Terminator Character</td>
<td><p>This terminates the TH segment and sets the actual value of the data segment terminator for the entire transaction.</p>
<ol start="41">
<li><p>The ASAP 4.2a Standard document uses the “~” in all examples. See the “Data Element Separators and Segment Terminators” in the standard's introduction for more information.</p></li>
</ol></td>
<td>$$TH09^PSOASAP()</td>
<td>Retrieved from the SEGMENT TERMINATOR CHAR field (#58.4001,.03) of the SPMP ASAP RECORD DEFINITION file. Tilde character "~"</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089113" class="anchor"></span>Table 38: Prescriber Information (PRE) 4.2A

<table style="width:100%;">
<caption><p><span id="_Toc207089114" class="anchor"></span>Table 39: Compound Drug Ingredient Detail (CDI) 4.2A</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>IS – Information Source Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To convey the name and identification numbers of the entity supplying the information.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>IS01 - Unique Information Source ID</td>
<td>Reference number or identification number as defined by the business partners. (Example: Phone number. However, if a phone number is used to populate this field, do not include hyphens).</td>
<td>$$IS01^PSOASAP()</td>
<td><p>Hard-coded "VA"_facility code (via Registration API $$SITE^VASITE())</p>
<p>Example: VA500</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>IS02 - Information Source Entity Name</td>
<td>Entity name of the Information Source.</td>
<td>$$IS02^PSOASAP()</td>
<td><p>OFFICIAL VA NAME field (#100) retrieved from the INSTITUTION file (#4)</p>
<p>Example: OKLAHOMA CITY VA MEDICAL CENTER</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>IS03 - Message</td>
<td><p>Freeform text message. Use of this field is defined by the PDMP.</p>
<p>Many PDMPs may designate this field to hold the submission period date range of the file transmitted. When used to indicate the date range, it must be the first data text in the field and must be inserted with using the following layout (where ""#"" and ""-"" are those literal characters): #CCYYMMDD#-#CCYYMMDD#</p>
<p>For example, a pharmacy may be submitting records for the reporting period of March 1, 2012 through March 7, 2012 but only filled reportable prescriptions on March 3, and March 5. The full submission period date range would be reported in IS03 as #20120301#-#20120307#</p>
<p>It is up to the PDMP to further define how to enter the submission date range for exceptional cases, such as for late submission records.</p>
<ol start="42">
<li><p>IS03 can also be used to show the date range for Zero Reports.</p></li>
</ol></td>
<td>$$IS03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089114" class="anchor"></span>Table 39: Compound Drug Ingredient Detail (CDI) 4.2A

<table>
<caption><p><span id="_Toc207089115" class="anchor"></span>Table 40: Additional Information Reporting (AIR) 4.2A</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PHA – Pharmacy Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the pharmacy or the dispensing prescriber. It is required that information be provided in at least one of the following fields: PHA01, PHA02, or PH03.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PHA01 - National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacy by CMS. Used if required by the PDMP.</td>
<td>$$PHA01^PSOASAP()</td>
<td>NPI INSTITUTION field (#101) retrieved via the Kernel API $$NPI^XUSNPI (ICR# 4532) from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA02 - NCPDP/NABP Provider ID</td>
<td>Identifier assigned to pharmacy by the National Council for Prescription Drug Programs. Used if required by the PDMP.</td>
<td>$$PHA02^PSOASAP()</td>
<td>NCPDP NUMBER field (#1008) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA03 - DEA Number</td>
<td>Identifier assigned to the pharmacy by the Drug Enforcement Administration. Used if required by the PDMP.</td>
<td>$$PHA03^PSOASAP()</td>
<td>FACILITY DEA NUMBER (#4,52) retrieved via the Kernel API $$WHAT^XUAF4 (ICR# 2171) using the RELATED INSTITUTION field (#100) in the OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA04 - Pharmacy or Dispensing Prescriber Name</td>
<td><p>Freeform name of the pharmacy.</p>
<ol start="43">
<li><p>If a dispensing prescriber, the prescriber’s name and professional degree should be entered, such as John Doe MD.</p></li>
</ol></td>
<td>$$PHA04^PSOASAP()</td>
<td>NAME field (#.01) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA05 - Address Information - 1</td>
<td>Freeform text for address information.</td>
<td>$$PHA05^PSOASAP()</td>
<td>MAILING FRANK STREET ADDRESS field (#.02) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA06 - Address Information - 2</td>
<td>Freeform text for additional address information.</td>
<td>$$PHA06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA07 - City Address</td>
<td>Freeform text for city name.</td>
<td>$$PHA07^PSOASAP()</td>
<td>MAILING FRANK CITY field (#.07) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA08 - State Address</td>
<td>U.S. Postal Service state code.</td>
<td>$$PHA08^PSOASAP()</td>
<td><p>ABBREVIATION field (#1) retrieved from the STATE file (#5) via pointer MAILING FRANK STATE field (#.08) in the OUTPATIENT SITE file (#59)</p>
<p>Example: OK</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA09 - ZIP Code Address</td>
<td>U.S. Postal Service ZIP Code. Use if available.</td>
<td>$$PHA09^PSOASAP()</td>
<td><p>MAILING FRANK ZIP+4 CODE field (#.05) retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="44">
<li><p>hyphen excluded</p></li>
</ol>
<p>Example: 731045028</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA10 - Phone Number</td>
<td>Complete phone number including area code.</td>
<td>$$PHA10^PSOASAP()</td>
<td><p>AREA CODE (#.03) and PHONE NUMBER (#.04) fields retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="45">
<li><p>hyphens excluded</p></li>
</ol>
<p>Example: 4056948387</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA11 - Contact Name</td>
<td>Freeform name.</td>
<td>$$PHA11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA12 - Chain Site ID</td>
<td>Store number assigned by the chain to the pharmacy location. Used when PDMP needs to identify the specific pharmacy from which information is required.</td>
<td>$$PHA12^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA13 - Pharmacy's Permit Number / License Number</td>
<td>Used to help identify the sending pharmacy</td>
<td>$$PHA13^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089115" class="anchor"></span>Table 40: Additional Information Reporting (AIR) 4.2A

<table>
<caption><p><span id="_Toc207089116" class="anchor"></span>Table 41: Pharmacy Trailer (TP) 4.2A</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PAT – Patient Information Segment</strong></td>
<td colspan="4"><p><strong>Purpose: Used to report the patient’s name and basic information as contained in the pharmacy record.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PAT01 - ID Qualifier of Patient Identifier</td>
<td><p>Code identifying the jurisdiction that issues the ID in PAT03.</p>
<p>Used if the PDMP requires such identification.</p>
<p>ASAP version 4.2a Standard Appendix A lists jurisdictions</p></td>
<td>$$PAT01^PSOASAP()</td>
<td>VistA sends 'US'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT02 - ID Qualifier</td>
<td><p>Code to identify the type of ID in PAT03. If PAT02 is used, PAT03 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver's License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$PAT02^PSOASAP()</td>
<td>VistA sends '07'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT03 - ID of Patient</td>
<td>Identification number for the patient as indicated in PAT02. An example would be the driver's license number.</td>
<td>$$PAT03^PSOASAP()</td>
<td><p>Retrieved from the SOCIAL SECURITY NUMBER field (#2,.09) of the PATIENT file via the REGISTRATION DEM^VADPT API</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT04 - ID Qualifier of Additional Patient Identifier</td>
<td>Code identifying the jurisdiction that issues the ID in PAT06. Used if the PDMP requires such identification. ASAP version 4.2a Standard Appendix A lists jurisdictions.</td>
<td>$$PAT04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT05 - Additional Patient ID Qualifier</td>
<td><p>Code to identify the type of ID in PAT06 if the PDMP requires a second identifier. If PAT05 is used, PAT06 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver's License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$PAT05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT06 - Additional ID</td>
<td>Identification that might be required by the PDMP to further identify the individual. An example might be in that PAT03 driver's license is required and in PAT06 Social Security number is also required.</td>
<td>$$PAT06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT07 - Last Name</td>
<td>Patient's last name.</td>
<td>$$PAT07^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="a">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the FAMILY (LAST) NAME field (#1) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the first comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>PAT08 - First Name</td>
<td>Patient's first name.</td>
<td>$$PAT08^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the GIVEN (FIRST) NAME field (#2) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the first space delimited piece of the second comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT09 - Middle Name</td>
<td>Patient's middle name or initial if available. Used if available in pharmacy system and required by the PDMP.</td>
<td>$$PAT09^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the MIDDLE NAME field (#3) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the second space delimited piece of the second comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT10 - Name Prefix</td>
<td>Patient's name prefix such as Mr. or Dr. Used if available in pharmacy system and required by the PDMP.</td>
<td>$$PAT10^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><blockquote>
<p>If the patient DFN exists in the NAME COMPONENTS file (#20), the PREFIX field (#4) in the NAME COMPONENTS file (#20).</p>
</blockquote></li>
<li><blockquote>
<p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p>
</blockquote></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT11 - Name Suffix</td>
<td>Patient's name suffix such as Jr. or the III. Used if available in pharmacy system and if required by the PDMP.</td>
<td>$$PAT11^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the SUFFIX field (#5) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT12 - Address Information - 1</td>
<td>Field size has been increased to 35 bytes from 30 bytes in 4.1. However, in order to accommodate pharmacy management systems storing 30 bytes or less for the patient address, no programming change is necessary if that is the maximum length of the field in the pharmacy management system. If the address stored in the system is a P.O. box number, defer to the specifications of the PDMP as to whether this should be reported in PAT12 or PAT13.</td>
<td>$$PAT12^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 1] field (#.111) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT13 - Address Information - 2</td>
<td>Freeform text for additional address information, if required by the PDMP and is available in pharmacy system.</td>
<td>$$PAT13^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 2] field (#.112) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT14 - City Address</td>
<td>Freeform text for city name.</td>
<td>$$PAT14^PSOASAP()</td>
<td><p>Retrieved from the CITY field (#.114) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT15 - State Address</td>
<td><p>U.S. Postal Service state code if required by the PDMP.</p>
<ol start="46">
<li><p>Field has been sized to handle international patients not residing in the U.S.</p></li>
</ol></td>
<td>$$PAT15^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061). Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ABBREVATION field (#1) in the STATE file (#5) pointed to by the STATE field (#.115) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the PROVINCE field (#.1171) in the PATIENT file (#2).</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT16 - ZIP Code Address</td>
<td>U.S. Postal Service ZIP code. Postal code will be reported for non-U.S. addresses.</td>
<td>$$PAT16^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ZIP CODE field (#.116) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the POSTAL CODE (#.1172) in the PATIENT file (#2).</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT17 - Phone Number</td>
<td><p>Complete phone number including area code when a state PDMP requires and is available in the pharmacy system.</p>
<ol start="47">
<li><p>Do not include hyphens in the number.</p></li>
</ol></td>
<td>$$PAT17^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>Use PHONE NUMBER [RESIDENCE] field (#.131) in the PATIENT file (#2) if not null</p>
<p>Else use PHONE NUMBER [CELLULAR] field (#.134) in the PATIENT file (#2) if not null</p>
<p>Else PHONE NUMBER [WORK] field (#.132) in the PATIENT file (#2) if not null</p>
<p>Else use K-WORK PHONE NUMBER field (#.21011) in the PATIENT file (#2) if not null</p>
<p>Else use K2-WORK PHONE NUMBER field (#.2199) in the PATIENT file (#2) if not null</p>
<p>Else use E-WORK PHONE NUMBER field (#.33011) in the PATIENT file (#2) if not null</p>
<p>Else use E2-WORK PHONE NUMBER field (#.331011) in the PATIENT file (#2) if not null</p>
<p>Else use AREA CODE field (#.03) in the OUTPATIENT SITE file (#59) concatenated to the PHONE NUMBER field (#.04) in the OUTPATIENT SITE file (#59)</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT18 - Date of Birth</td>
<td>Date patient was born. Format: CCYYMMDD.</td>
<td>$$PAT18^PSOASAP()</td>
<td><p>Retrieved from the DATE OF BIRTH field (#.03) in the PATIENT file (#2)</p>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT19 - Gender Code</td>
<td><p>Code indicating the sex of the patient if required by the PDMP.</p>
<p>F Female</p>
<p>M Male</p>
<p>U Unknown</p></td>
<td>$$PAT19^PSOASAP()</td>
<td><p>Retrieved using the Registration API $$DEM^VADPT (ICR #10061) and return variable VADM(5).</p>
<p>If no value is found, VistA sends 'U'</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT20 - Species Code</td>
<td><p>Used if required by the PDMP to differentiate a prescription for an individual from one prescribed for an animal.</p>
<p>01 Human</p>
<p>02 Veterinary Patient</p></td>
<td>$$PAT20^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT21 - Patient Location Code</td>
<td><p>Code indicating where patient is located when receiving pharmacy services if required by the PDMP.</p>
<p>01 Home</p>
<p>02 Intermediary Care</p>
<p>03 Nursing Home</p>
<p>04 Long-Term/Extended Care</p>
<p>05 Rest Home</p>
<p>06 Boarding Home</p>
<p>07 Skilled-Care Facility</p>
<p>08 Sub-Acute Care Facility</p>
<p>09 Acute-Care Facility</p>
<p>10 Outpatient</p>
<p>11 Hospice</p>
<p>98 Unknown</p>
<p>99 Other</p></td>
<td>$$PAT21^PSOASAP()</td>
<td>VistA sends '10'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT22 - Country of Non-U.S. Resident</td>
<td>Used when the patient's address is a foreign country and PAT12 through PAT16 are left blank. This is a freeform text field. ASAP does not provide a list of countries for this field. PDMPs may permit some of the other address fields to not be used if this field is populated.</td>
<td>$$PAT22^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved If COUNTRY field (#.1173) in the PATIENT file (#2) points to the US in the COUNTRY CODE file (#779.004), VistA returns “” (null).</p>
<p>Else VistA returns the FIPS CODE field (#1.2) in the COUNTRY CODE file (#779.004) pointed to by the COUNTRY field (#.1173) in the PATIENT file (#2).</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT23 - Name of Animal</td>
<td>Used if required by the PDMP for prescriptions written by a veterinarian and the pharmacist has access to this information at the time of preparing the prescription.</td>
<td>$$PAT23^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td colspan="5"><p><strong>PAT07 – PAT09 Note:</strong> The NAME field is a delimited value in which the last name and first name are separated by a comma; the middle name and/or suffix are after the first name separated by a space "LAST,FIRST MIDDLE SUFFIX".</p>
<p><strong>PAT07 – PAT11 Note:</strong> The REGISTRATION package does not allow special characters in the PATIENT name during the registration process, with the exception of spaces, apostrophes, hyphens, and one comma. Since other characters are not permitted via end-user options, the probability of special characters in the PATIENT name fields that would cause a data transmission failure is unlikely.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207089116" class="anchor"></span>Table 41: Pharmacy Trailer (TP) 4.2A

<table>
<caption><p><span id="_Toc207089117" class="anchor"></span>Table 42: Transaction Trailer (TT) 4.2A</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 31%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DSP – Dispensing Record Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the basic components of the dispensing of a given prescription order including the date and quantity.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>DSP01 - Reporting Status</td>
<td><p>00 New Record</p>
<p>01 Revise</p>
<p>02 Void</p>
<p>DSP01 requires one of the codes below. An empty or blank field no longer indicates a new prescription dispensing transaction. A PDMP may elect to require a subset of the codes below, specifically 00 and 02, but not 01.</p>
<p>00 This code indicates a new prescription dispensing transaction.</p>
<p>01 This code indicates that one or more data element values in a previously submitted transaction are being revised.</p>
<p>Examples of when a revision may be necessary include corrections to typographical errors in original data submissions; or change occurred to the prescription between the time the record was submitted and the time the patient picked it up, such as dispensing a smaller metric quantity, adding or correcting patient information, correcting prescriber DEA number, or payment type. When receiving a transaction with a DSP01 value of 01, the PDMP will override all of the detail segments’ data of the original prescription transaction with all of the detail segments’ data from the revised prescription transaction. So it is essential to submit all of the data elements in all of the detail segments populated with the identical data as it appeared in the original record, with only the changed data element(s) content being different (and DSP01 with a value of 01). Do not use 01 in combination with a zero metric quantity to indicate that the prescription was not picked up. Use the value 02 instead as described below. If the PDMP receives a prescription transaction with DSP01 as 01 and a separate prescription transaction with DSP01 as 02, the PDMP will only void the original prescription transaction and will not attempt to apply a revision. Because the PAT segment loops at a higher level than the other detail segments, the only ways to submit revisions to PAT data elements are either: 1) to not loop the DSP segment within the PAT segment – or 2) to loop the DSP segment within PAT segment and have every DSP01 record element within the loop have a DSP01 of 01.</p>
<p>02 This code is a message to the PDMP to remove the original prescription transaction from its database (or to mark the record as invalid and to be ignored). There can be several reasons for sending a void transaction. One example would be when the prescription was never picked up and the medication was returned to stock. Another example would be when the prescription was reported in error. A DSP01 value of 02 can also be used as an alternative to the DSP01 value of 01 in order to send PDMP corrections. When submitting corrections in this manner; first submit a record with a DSP01 of 02 to indicate to the PDMP to void the original prescription transaction; then submit a brand-new prescription transaction with a DSP01 value of 00 with the correct information.</p>
<ol start="48">
<li><p>Examples of the correct use of codes in DSP01 are shown in Appendix D in the ASAP version 4.2a Standard, as well as the limited data set to void a prescription that PDMPs can elect to use.</p></li>
</ol></td>
<td>$$DSP01^PSOASAP()</td>
<td><p>Derived by retrieving the RECORD TYPE field (#2) in the PRESCRIPTIONS subfile (58.42001) of the SPMP EXPORT BATCH file (#58.42) for the prescription being exported and assigning a code based on the value where:</p>
<p>N = NEW Rx and VistA sends '00' for New Record</p>
<p>R = REFILL and VistA sends '01' for Revise</p>
<p>V = VOID and VistA sends '02' for Void</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP02 - Prescription Number</td>
<td>Serial number assigned to the prescription by the pharmacy.</td>
<td>$$DSP02^PSOASAP()</td>
<td>RX # field (.01) retrieved from the PRESCRIPTION file (#52)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP03 - Date Written</td>
<td>Date the prescription was written (authorized). Format: CCYYMMDD</td>
<td>$$DSP03^PSOASAP()</td>
<td>ISSUE DATE field (#1) retrieved from the PRESCRIPTION file (#52)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP04 - Refills Authorized</td>
<td>The number of refills authorized by the prescriber.</td>
<td>$$DSP04^PSOASAP()</td>
<td>Retrieved from the # OF REFILLS field (#52,9) of the PRESCRIPTION file</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP05 - Date Filled</td>
<td>Date prescription was prepared. Format: CCYYMMDD.</td>
<td>$$DSP05^PSOASAP()</td>
<td><p>Retrieved from one of three locations depending on the type of fill.</p>
<p>Original Fill: RELEASED DATE/TIME field (#31) of the PRESCRIPTION file (#52)</p>
<p>Refill: RELEASED DATE/TIME field (#17) of the REFILL subfile (#52.1)</p>
<p>Partial: RELEASED DATE/TIME field (#8) of the PARTIAL subfile (#52.2)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP06 - Refill Number</td>
<td><p>Number of the fill of the prescription.</p>
<p>0 indicates original dispensing, 01-99 is the refill number.</p></td>
<td>$$DSP06^PSOASAP()</td>
<td>Retrieved from the AL and AM cross-references of the PRESCRIPTION file (#52) and PARTIAL DATE subfile (#52.2) respectively.</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP07 - Product ID Qualifier</td>
<td><p>Used to identify the type of product ID contained in DSP08.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 Compound (Used to indicate it is a compound. The CDI segment then becomes a required segment. Also, see instructions for DSP08.)</p></td>
<td>$$DSP07^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP08 - Product ID</td>
<td><p>Full product identification as indicated in DSP07, including zeros without punctuation. If the product is a compound, use 99999 as the first five characters of the product code. The remaining characters are assigned by the pharmacy. The CDI then becomes a required segment.</p>
<ol start="49">
<li><p>If a controlled substance is part of a kit, the NDC of the kit should be reported if it is a legitimate manufacturer’s NDC. If not, the NDC of the controlled substance within the kit should be reported. Also, if multiple controlled substances are in the kit, use the CDI segment to report it as a compound.</p></li>
</ol></td>
<td>$$DSP08^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK subfile (52.07)</p>
<p>NDC field (#16)</p>
<p>If not at 52.07,16 then</p>
<p>DRUG file (#50)</p>
<p>NDC field (#31)</p>
<p>If not at 50,31 then</p>
<p>REFILL:</p>
<p>REFILL subfile (#52.1)</p>
<p>NDC field (#11)</p>
<p>ORIGINAL:</p>
<p>PRESCRIPTION file (#52)</p>
<p>NDC field (#27)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP09 - Quantity Dispensed</td>
<td><p>Number of metric units dispensed in metric decimal format.</p>
<p>Example: 2.5.</p>
<ol start="50">
<li><p>For compounds show the first quantity in CDI04. Appendix B in ASAP version 4.2a Standard contains specific instructions.</p></li>
</ol></td>
<td>$$DSP09^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>QTY field (#3)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>QTY field (#7)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>QTY field (#1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.04)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP10 - Days Supply</td>
<td>The calculated or estimated number of days the medication will cover.</td>
<td>$$DSP10^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>DAYS SUPPLY field (#4)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>DAYS SUPPLY field (#8)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>DAYS SUPPLY field (#1.1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.041)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP11 - Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in DSP09, if required by the PDMP.</p>
<p>Appendix B in ASAP version 4.2a Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$DSP11^PSOASAP()</td>
<td><p>Retrieved from the NCPDP DISPENSE UNIT field (#50,82) of the DRUG file.</p>
<p>Coded data:</p>
<p>01-EA</p>
<p>02-ML</p>
<p>03-GM</p>
<p>BLANK</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP12 - Transmission Form of Rx Origin Code</td>
<td><p>Code indicating how the pharmacy received the prescription, if required by the PDMP.</p>
<p>01 Written Prescription</p>
<p>02 Telephone Prescription</p>
<p>03 Telephone Emergency Prescription</p>
<p>04 Fax Prescription</p>
<p>05 Electronic Prescription</p>
<p>06 Transferred/Forwarded Rx</p>
<p>99 Other</p></td>
<td>$$DSP12^PSOASAP()</td>
<td><p>The ORDER ENTRY/RESULTS REPORTING API $$NATURE^ORUTL3 provides the Nature of Order, which is translated the following way:</p>
<p>01 W</p>
<p>02 V or T</p>
<p>05 E</p>
<p>99 Other</p>
<p>ICR# 5890</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP13 - Partial Fill Indicator</td>
<td><p>This field is used when the quantity in DSP09 is less than the metric quantity per dispensing authorized by the prescriber. This dispensing activity is often referred to as a split filling.</p>
<p>00 Not a Partial Fill</p>
<p>01 First Partial Fill</p>
<ol start="51">
<li><p>For additional fills per prescription, increment by 1. So the second partial fill would be reported as 02, up to a maximum of 99</p></li>
</ol></td>
<td>$$DSP13^PSOASAP()</td>
<td><p>Codes indicating partial or non-partial fill:</p>
<p>00 Non-Partial Fill</p>
<p>01 Partial 1</p>
<p>02 Partial 2</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP14 - Pharmacist National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacist by CMS if the pharmacist applies for a number. This number can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP14^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill pharmacist.</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP15 - Pharmacist State License Number</td>
<td>Assigned to the pharmacist by the State Licensing Board. This data element can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP15^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP16 - Classification Code for Payment Type</td>
<td><p>Code identifying the type of payment, i.e. how it was paid for, if required by the PDMP.</p>
<p>01 Private Pay (Cash, Charge, Credit Card)</p>
<p>02 Medicaid</p>
<p>03 Medicare</p>
<p>04 Commercial Insurance</p>
<p>05 Military Installations and VA</p>
<p>06 Workers’ Compensation</p>
<p>07 Indian Nations</p>
<p>99 Other</p></td>
<td>$$DSP16^PSOASAP()</td>
<td>VistA sends '05'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP17 - Date Sold</td>
<td><p>This field is used to determine the date the prescription was dispensed (sold to, picked up by, or otherwise left the pharmacy), not the date it was prepared.</p>
<p>This date could be captured from the point-of-sale (POS) system, if the pharmacy has a POS system, and there is a bidirectional flow with the pharmacy management system in order to capture and report this date. Or it could be captured and reported from a will-call management system, integrated with the pharmacy management system.</p></td>
<td>$$DSP17^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order via $$DSP05^PSOASAP():</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>RELEASED DATE/TIME field (#21)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>RELEASED DATE/TIME field (#31)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>RELEASED DATE/TIME field (#17)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>RELEASED DATE/TIME (#8)</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP18 - RxNorm Product Qualifier</td>
<td><p>01 Semantic Clinical Drug (SCD)</p>
<p>02 Semantic Branded Drug (SBD)</p>
<p>03 Generic Package (GPCK)</p>
<p>04 Branded Package (BPCK)</p>
<p>RxNorm code that is populated in the DRU-010-09 field in the SCRIPT transaction.</p>
<ol start="52">
<li><p>DSP18 and DSP19 are placeholder fields pending RxNorm becoming an industry standard. These fields should not be required until such time.</p></li>
</ol></td>
<td>$$DSP18^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP19 - RxNorm Code</td>
<td>Used for electronic prescriptions to capture the prescribed drug product identification, if required by the PDMP.</td>
<td>$$DSP19^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP20 - Electronic Prescription Reference Number</td>
<td>This field should be populated with the Initiator Reference Number from field UIB-030-01 in the SCRIPT transaction.</td>
<td>$$DSP20^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP21 - Electronic Prescription Order Number</td>
<td><p>This field will be populated with the Initiator Control Reference from field UIH-030-01 in the SCRIPT standard.</p>
<ol start="53">
<li><p>DSP20 and DSP21 should be reported as a pair to the PDMP and the PDMP will decide which one, if not both, it decides to capture. By requiring the reporting of both, this avoids specification variations that would require custom programming to accommodate a PDMP. Also, the information reported by the pharmacy management system will depend on the information received at the pharmacy with an electronic prescription.</p></li>
</ol></td>
<td>$$DSP21^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP22 - Quantity Prescribed</td>
<td>This field has been added in order to add clarity to the value reported in DSP13 Partial Fill Indicator</td>
<td>$$DSP22^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>DSP23 - Rx SIG</td>
<td>This field would capture the actual directions printed on the prescription vial label. If the directions exceed 200 characters, truncation would be allowed.</td>
<td>$$DSP23^PSOASAP()</td>
<td>Concatenate the SIG1 multiple (#52.04,.01) into a single string</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP24 - Treatment Type</td>
<td><p>While this field can be used to indicate that the prescription was for opioid dependency treatment when Code 02 is used, it can also be used to provide other reasons for the opioid prescription through use of the additional codes.</p>
<p>01 = Not Used for Opioid Dependency Treatment</p>
<p>02 = Used for Opioid Dependency Treatment</p>
<p>03 = Pain Associated with Active and Aftercare Cancer Treatment</p>
<p>04 = Palliative Care in Conjunction with a Serious Illness</p>
<p>05 = End-of-Life and Hospice Care</p>
<p>06 = A Pregnant Individual with a Pre-existing Prescription for Opioids</p>
<p>07 = Acute Pain for an Individual with an Existing Opioid Prescription for Chronic Pain</p>
<p>08 = Individuals Pursuing an Active Taper of Opioid Medications</p>
<p>09 = Patient is Participating in a Pain Management Contract</p>
<p>99 = Other (trading partner agreed upon reason)</p>
<p>*Codes 03 through 99 added 6/28/2017.</p>
<ol start="54">
<li><p>These new codes can only be reported if provided by the prescriber with the prescription.</p></li>
</ol></td>
<td>$$DSP24^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP25 - Diagnosis Code</td>
<td>This field is used to report the ICD-10 code. If required by a PDMP, this field would be populated only when the ICD-10 code is included with the prescription.</td>
<td>$$DSP25^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089117" class="anchor"></span>Table 42: Transaction Trailer (TT) 4.2A

<table>
<caption><p><span id="_Toc207089118" class="anchor"></span>Table 43: ASAP 4.2B Baseline Dataset - Transaction Header (TH) 4.2B</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PRE – Prescriber Information Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the prescriber of the prescription.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PRE01 - National Provider Identifier (NPI)</td>
<td><p>Identifier assigned to the prescriber by CMS.</p>
<ol start="55">
<li><p>If the prescriber does not have a DEA number and prescribed a noncontrolled substance that is a reportable drug to the PDMP, this field should be used as the identifier.</p></li>
</ol></td>
<td>$$PRE01^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill provider</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE02 - DEA Number</td>
<td>Identifying number assigned to a prescriber or an institution by the Drug Enforcement Administration (DEA).</td>
<td>$$PRE02^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The first piece by ""-"" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA#</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) of the NEW PERSON file. The first piece by ""-"" is returned.</p>
<p>ICR# 2343</p>
<p>Pharmacy DEA#</p>
<p>the Kernel API $$WHAT^XUAF4 is called to return the FACILITY DEA NUMBER field (#4,52) of the INSTITUTION file.</p>
<p>ICR# 2171</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PRE03 - DEA Number Suffix</td>
<td>Identifying number assigned to a prescriber by an institution when the institution's DEA number is used, if required by the PDMP.</td>
<td>$$PRE03^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# suffix associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The 2nd piece by ""-"" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA# suffix</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) from the NEW DEA #'S multiple of the NEW PERSON file. The 2nd piece by ""-"" is returned.</p>
<p>ICR# 2343</p>
<p>VA#</p>
<p>If DEA# from PHA03 is equal to the DEA# from PHA02, then The Kernel API $$DEA^XUSER retrieves the value at the VA# field (#200,53.3) of the NEW PERSON file.</p>
<p>ICR# 2171</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE04 - Prescriber State License Number</td>
<td>Identification assigned to the Prescriber by the State Licensing Board. Used if required by the PDMP.</td>
<td>$$PRE04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE05 - Last Name</td>
<td>Prescriber's last name. Used if required by the PDMP.</td>
<td>$$PRE05^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE06 - First Name</td>
<td>Prescriber's first name. Used if required by the PDMP.</td>
<td>$$PRE06^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE07 - Middle Name</td>
<td>Prescriber's middle name or initial. Used if required and is available in the pharmacy system.</td>
<td>$$PRE07^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE08 - Phone Number</td>
<td>The prescriber's primary phone number.</td>
<td>$$PRE08^PSOASAP()</td>
<td><p>Retrieved from the PHONE NUMBER # field (#200,.132) of the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE09 - XDEA Number</td>
<td>This field gives a PDMP the option of requiring the XDEA Number (NADEAN) in the PRE Segment when the prescription is for opioid dependency.</td>
<td>$$PRE09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
</tbody>
</table>

<span id="_Toc207089118" class="anchor"></span>Table 43: ASAP 4.2B Baseline Dataset - Transaction Header (TH) 4.2B

<table>
<caption><p><span id="_Toc207089119" class="anchor"></span>Table 44: Information Source (IS) 4.2B</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 41%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CDI – Compound Drug Ingredient Detail Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the individual ingredients that make up a compound.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Not Used</strong></p></td>
</tr>
<tr class="even">
<td>CDI01 - Compound Drug Ingredient Sequence Number</td>
<td>The first reportable ingredient is 1. Each additional reportable ingredient is incremented by 1.</td>
<td>$$CDI01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI02 - Product ID Qualifier</td>
<td><p>Code to identify the type of product ID contained in CDI03.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 CPD (This code is not used in this segment.)</p></td>
<td>$$CDI02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI03 - Product ID</td>
<td>Full product identification as indicated in CDI02, including leading zeros without punctuation.</td>
<td>$$CDI03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI04 - Component Ingredient Quantity</td>
<td><p>Metric decimal quantity of the ingredient identified in CDI03.</p>
<p>Example: 2.5. Appendix B in ASAP version 4.2a Standard contains specific instructions.</p></td>
<td>$$CDI04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI05 - Compound Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in CDI04, if required by the prescription-monitoring program.</p>
<p>Appendix B in ASAP version 4.2a Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage units or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$CDI05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089119" class="anchor"></span>Table 44: Information Source (IS) 4.2B

<table>
<caption><p><span id="_Toc207089120" class="anchor"></span>Table 45: Pharmacy Header (PHA) 4.2B</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 38%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AIR – Additional Information Reporting Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To report a prescription blank serial number, information on person dropping off or picking up the prescription, or information regarding the prescription not included in the other detail segments. Note: If this segment is used, at least one of the data elements (fields) will be required.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Optional</strong></p></td>
</tr>
<tr class="even">
<td>AIR01 - State Issuing Rx Serial Number</td>
<td><p>U.S.P.S. state code of state that issued serialized prescription blank. This is required if AIR02 is used.</p>
<p>ASAP version 4.2a Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR02 - State Issued Rx Serial Number</td>
<td>Number assigned to state issued serialized prescription blank. Required if state issues serialized prescription pads for prescribers to use.</td>
<td>$$AIR02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR03 - ID Issuing Jurisdiction</td>
<td><p>Code identifying the jurisdiction that issues the ID contained in AIR05.</p>
<p>Used if required by the PDMP.</p>
<p>ASAP version 4.2a Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR04 - ID Qualifier of Person Dropping Off or Picking Up Rx</td>
<td><p>Code indicating the type of ID in AIR05 if required by the PDMP.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver's License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>99 Other (Trading partner agreed upon ID)</p></td>
<td>$$AIR04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR05 - ID of Person Dropping Off or Picking Up Rx</td>
<td><p>ID number of the person dropping off or picking up the prescription, if required by the PDMP.</p>
<ol start="56">
<li><p>Because historically there has been a noticeable amount of extraneous information entered in this field, which has interfered with data analysis, it is important that every effort be made to ensure that only the unadorned customer ID and no additional information be entered into this field.</p></li>
</ol></td>
<td>$$AIR05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR06 - Relationship of Person Dropping Off or Picking Up Rx</td>
<td><p>Code indicating the relationship to the person dropping off or picking up Rx, if required by the PDMP.</p>
<p>01 Patient</p>
<p>02 Parent/Legal Guardian</p>
<p>03 Spouse</p>
<p>04 Caregiver</p>
<p>99 Other</p></td>
<td>$$AIR06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR07 - Last Name of Person Dropping Off or Picking Up Rx</td>
<td>Last name of the person dropping off or picking up Rx, if required by the PDMP.</td>
<td>$$AIR07^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR08 - First Name of Person Dropping Off or Picking Up Rx</td>
<td>First name of the person dropping off or picking up Rx, if required by the PDMP.</td>
<td>$$AIR08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR09 - Last Name or Initials of Pharmacist</td>
<td>Last name or initials of the pharmacist dispensing the medication, if required by the PDMP.</td>
<td>$$AIR09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR10 - First Name of Pharmacist</td>
<td>First name of the pharmacist dispensing the medication, if required by the PDMP.</td>
<td>$$AIR10^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR11 - Dropping Off/Picking Up Identifier Qualifier</td>
<td><p>Additional qualifier for the ID contained in AIR05.</p>
<p>01 Person Dropping Off</p>
<p>02 Person Picking Up</p>
<p>98 Unknown/Not Applicable (An example of Unknown: Where the pharmacist does not know which person it is. Or there is no ID to collect at drop-off, such as when a prescription is phoned in. An example of Not Applicable: When the prescription is delivered.)</p>
<ol start="57">
<li><p>Both 01 and 02 cannot be required by a PDMP. Usage of this field depends on whether a PDMP has interest in knowing whether the information supplied in fields AIR04–AIR08 is for the person dropping off or picking up the prescription.</p></li>
</ol></td>
<td>$$AIR11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089120" class="anchor"></span>Table 45: Pharmacy Header (PHA) 4.2B

<table>
<caption><p><span id="_Toc207089121" class="anchor"></span>Table 46: Patient Information (PAT) 4.2B</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TP – Pharmacy Trailer Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the end of data for a given pharmacy and provide the count of the total number of detail segments included for the pharmacy, including the pharmacy header (PHA) and the pharmacy trailer (TP) segments.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TP01 - Detail Segment Count</td>
<td>Number of detail segments included for the pharmacy including the pharmacy header (PHA) and the pharmacy trailer (TP) segments.</td>
<td>$$TP01^PSOASAP()</td>
<td>Calculates the number of detail segments included (PAT, DSP, PRE, CDI, AIR) in addition to the pharmacy header (PHA) and pharmacy trailer (TP)</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089121" class="anchor"></span>Table 46: Patient Information (PAT) 4.2B

<table>
<caption><p><span id="_Toc207089122" class="anchor"></span>Table 47: Dispensing Record (DSP) 4.2B</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TT – Transaction Trailer Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To indicate the end of the transaction and provide the count of the total number of segments included in the transaction.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TT01 - Transaction Control Number</td>
<td>Identifying control number that must be unique. Assigned by the originator of the transaction. Must match the number in TH02 sent by the pharmacy.</td>
<td>$$TT01^PSOASAP()</td>
<td>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file. (ex: 500-182)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TT02 - Segment Count</td>
<td>Total number of segments included in the transaction including the header (TH) and trailer (TT) segments.</td>
<td>$$TT02^PSOASAP()</td>
<td>Calculated for each transmission.</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089122" class="anchor"></span>Table 47: Dispensing Record (DSP) 4.2B

#### ASAP Standard Version 4.2B Implementation

<table>
<caption><p><span id="_Toc207089123" class="anchor"></span>Table 48: Prescriber Information (PRE) 4.2B</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TH – Transaction Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To indicate the start of a transaction. It also assigns the segment terminator, data element separator, and control number.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TH01 - Version / Release Number</td>
<td><p>Used to identify the transaction Version / Release.</p>
<p>Format = x.x 4.2B</p>
<p>ASAP Version 4 Release 2B</p></td>
<td>$$TH01^PSOASAP()</td>
<td>ASAP VERSION field (#1) retrieved from the SPMP STATE PARAMETERS file (#58.41)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH02 - Transaction Control Number</td>
<td><p>Sender assigned code uniquely identifying a transaction. This number must be used in TT01.</p>
<p>Recommendation: Use a Globally Unique Identifier (GUID) or other nonrepeating alphanumeric combination to populate this field.</p></td>
<td>$$TH02^PSOASAP()</td>
<td>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file. (ex: 500-182)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH03 - Transaction Type</td>
<td><p>Identifies the purpose of initiating the transaction.</p>
<p>01 Send/Request Transaction</p>
<p>02 Acknowledgment (Used in Response only.)</p>
<p>03 Error Receiving (Used in Response only.)</p>
<p>04 Void (Used to void a specific Rx in a real-time transmission, or an entire batch file that has been transmitted.</p>
<p>When 04 is used the appropriate transaction control number in TH02 for the specific prescription or batch file must be included. When 04 is used only the TH Header Segment and the Transaction Trailer Segment are used.)</p></td>
<td>$$TH03^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>TH04 - Response ID</td>
<td>Contains the Transaction Control Number of a transaction that initiated the transaction. Required in response transaction only.</td>
<td>$$TH04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH05 - Creation Date</td>
<td>Date the transaction was created. Format: CCYYMMDD.</td>
<td>$$TH05^PSOASAP()</td>
<td><p>Kernel API - $$FMTHL7^XLFDT($$HTFM^XLFDT($H)</p>
<p>Example: 20240904</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH06 - Creation Time</td>
<td>Time the transaction was created. Format: HHMMSS or HHMM. Do not use colons or other non-numeric characters.</td>
<td>$$TH06^PSOASAP()</td>
<td><ol type="1">
<li><blockquote>
<p>Call Kernel API - $$HTFM^XLFDT($H)which returns back UTC date/time</p>
</blockquote></li>
</ol>
<blockquote>
<p>Example: 091522</p>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Take the TIME value of the returned date/time stamp and set that data to be exactly 6 in length and append a "Z" to the end.</p>
</blockquote></li>
</ol></td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH07 - File Type</td>
<td><p>Code specifying the type of transaction.</p>
<p>P Production</p>
<p>T Test</p></td>
<td>$$THO7^PSOASAP()</td>
<td>Retrieved via the Kernel API - $$PROD^XUPROD(1)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH08 - Routing Number/BIN</td>
<td>This field can be used for real-time transmissions that go through an intermediary or network switch to indicate, if necessary, the specific state that the transactions should be routed to.</td>
<td>$$TH08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH09 - Segment Terminator Character</td>
<td><p>This terminates the TH segment and sets the actual value of the data segment terminator for the entire transaction.</p>
<ol start="58">
<li><p>The ASAP 4.2b Standard document uses the “~” in all examples. See the “Data Element Separators and Segment Terminators” in the standard's introduction for more information.</p></li>
</ol></td>
<td>$$TH09^PSOASAP()</td>
<td>Retrieved from the SEGMENT TERMINATOR CHAR field (#58.4001,.03) of the SPMP ASAP RECORD DEFINITION file. Tilde character "~"</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089123" class="anchor"></span>Table 48: Prescriber Information (PRE) 4.2B

<table>
<caption><p><span id="_Toc207089124" class="anchor"></span>Table 49: Compound Drug Ingredient (CDI) 4.2B</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>IS – Information Source Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To convey the name and identification numbers of the entity supplying the information.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>IS01 - Unique Information Source ID</td>
<td>Reference number or identification number as defined by the business partners. (Example: Phone number. However, if a phone number is used to populate this field, do not include hyphens.)</td>
<td>$$IS01^PSOASAP()</td>
<td><p>Hard-coded "VA"_facility code (via Registration API $$SITE^VASITE())</p>
<p>Example: VA500</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>IS02 - Information Source Entity Name</td>
<td>Entity name of the Information Source.</td>
<td>$$IS02^PSOASAP()</td>
<td><p>OFFICIAL VA NAME field (#100) retrieved from the INSTITUTION file (#4)</p>
<p>Example: OKLAHOMA CITY VA MEDICAL CENTER</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>IS03 - Message</td>
<td><p>Freeform text message. Use of this field is defined by the PDMP. Many PDMPs may designate this field to hold the submission period date range of the file transmitted. When used to indicate the date range, it must be the first data text in the field and must be inserted with using the following layout (where """"#"""" and """"-"""" are those literal characters): #CCYYMMDD#-#CCYYMMDD#</p>
<p>For example, a pharmacy may be submitting records for the reporting period of December 5, 2019 through December 11, 2019 but only filled reportable prescriptions on December 5 and December 7. The full submission period date range would be reported in IS03 as #20191205#-#20191211#</p>
<p>It is up to the PDMP to further define how to enter the submission date range for exceptional cases, such as for late submission records.</p>
<ol start="59">
<li><p>IS03 can also be used to show the date range for Zero Reports.</p></li>
</ol></td>
<td>$$IS03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089124" class="anchor"></span>Table 49: Compound Drug Ingredient (CDI) 4.2B

<table>
<caption><p><span id="_Toc207089125" class="anchor"></span>Table 50: Additional Information Reporting (AIR) 4.2B</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PHA – Pharmacy Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the pharmacy or the dispensing prescriber. It is required that information be provided in at least one of the following fields: PHA01, PHA02, or PH03. (Note: Situation for use of PHA04 through PHA13 is if needed by the state PDMP to further identify the sending pharmacy.)</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PHA01 - National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacy by CMS. Used if required by the PDMP.</td>
<td>$$PHA01^PSOASAP()</td>
<td>NPI INSTITUTION field (#101) retrieved via the Kernel API $$NPI^XUSNPI (ICR# 4532) from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA02 - NCPDP/NABP Provider ID</td>
<td>Identifier assigned to pharmacy by the National Council for Prescription Drug Programs. Used if required by the PDMP.</td>
<td>$$PHA02^PSOASAP()</td>
<td>NCPDP NUMBER field (#1008) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA03 - DEA Number</td>
<td>Identifier assigned to the pharmacy by the Drug Enforcement Administration. Used if required by the PDMP.</td>
<td>$$PHA03^PSOASAP()</td>
<td>FACILITY DEA NUMBER (#4,52) retrieved via the Kernel API $$WHAT^XUAF4 (ICR# 2171) using the RELATED INSTITUTION field (#100) in the OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA04 - Pharmacy or Dispensing Prescriber Name</td>
<td><p>Freeform name of the pharmacy.</p>
<ol start="60">
<li><p>If a dispensing prescriber, the prescriber’s name and professional degree should be entered, such as John Doe MD.</p></li>
</ol></td>
<td>$$PHA04^PSOASAP()</td>
<td>NAME field (#.01) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA05 - Address Information – 1</td>
<td>Freeform text for address information.</td>
<td>$$PHA05^PSOASAP()</td>
<td>MAILING FRANK STREET ADDRESS field (#.02) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA06 - Address Information - 2</td>
<td>Freeform text for additional address information.</td>
<td>$$PHA06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA07 - City Address</td>
<td>Free-form text for city name.</td>
<td>$$PHA07^PSOASAP()</td>
<td>MAILING FRANK CITY field (#.07) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA08 - State Address</td>
<td>U.S. Postal Service state code.</td>
<td>$$PHA08^PSOASAP()</td>
<td><p>ABBREVIATION field (#1) retrieved from the STATE file (#5) via pointer MAILING FRANK STATE field (#.08) in the OUTPATIENT SITE file (#59)</p>
<p>Example: OK</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA09 - ZIP Code Address</td>
<td>U.S. Postal Service ZIP Code. Use if available. Exclude hyphen.</td>
<td>$$PHA09^PSOASAP()</td>
<td><p>MAILING FRANK ZIP+4 CODE field (#.05) retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="61">
<li><p>hyphen excluded</p></li>
</ol>
<p>Example: 731045028</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA10 - Phone Number</td>
<td>Complete phone number including area code. Exclude hyphens.</td>
<td>$$PHA10^PSOASAP()</td>
<td><p>AREA CODE (#.03) and PHONE NUMBER (#.04) fields retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="62">
<li><p>hyphens excluded</p></li>
</ol>
<p>Example: 4056948387</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA11 - Contact Name</td>
<td>Freeform name.</td>
<td>$$PHA11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA12 - Chain Site ID</td>
<td>Store number assigned by the chain to the pharmacy location. Used when PDMP needs to identify the specific pharmacy from which information is required.</td>
<td>$$PHA12^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA13 - Pharmacy's Permit Number/License Number</td>
<td>Used to help identify the sending pharmacy</td>
<td>$$PHA13^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089125" class="anchor"></span>Table 50: Additional Information Reporting (AIR) 4.2B

<table>
<caption><p><span id="_Toc207089126" class="anchor"></span>Table 51: Pharmacy Trailer (TP) 4.2B</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PAT – Patient Information</strong></td>
<td colspan="4"><p><strong>Purpose: Used to report the patient’s name and basic information as contained in the<br />
pharmacy record</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PAT01 - ID Qualifier of Patient Identifier</td>
<td><p>Code identifying the jurisdiction that issues the ID in PAT03.</p>
<p>Used if the PDMP requires such identification.</p>
<p>ASAP version 4.2b Standard Appendix A lists jurisdictions.</p></td>
<td>$$PAT01^PSOASAP()</td>
<td>VistA sends 'US'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT02 - ID Qualifier</td>
<td><p>Code to identify the type of ID in PAT03. If PAT02 is used, PAT03 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Appriss Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$PAT02^PSOASAP()</td>
<td>VistA sends '07'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT03 - ID of Patient</td>
<td><blockquote>
<p>Identification number for the patient as indicated in PAT02. An example would be the driver’s license number.</p>
</blockquote>
<ol start="63">
<li><p>This field can only be populated with code 10 when provided on the prescription.</p></li>
</ol></td>
<td>$$PAT03^PSOASAP()</td>
<td><p>Retrieved from the SOCIAL SECURITY NUMBER field (#2,.09) of the PATIENT file via the REGISTRATION DEM^VADPT API</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT04 - ID Qualifier of Additional Patient Identifier</td>
<td><blockquote>
<p>Code identifying the jurisdiction that issues the ID in PAT06. Used if the PDMP requires such identification. ASAP version 4.2b Standard Appendix A lists jurisdictions.</p>
</blockquote></td>
<td>$$PAT04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT05 - Additional Patient ID Qualifier</td>
<td><p>Code to identify the type of ID in PAT06 if the PDMP requires a second identifier. If PAT05 is used, PAT06 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver's License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Appriss Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$PAT05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT06 - Additional ID</td>
<td>Identification that might be required by the PDMP to further identify the individual. An example might be in that PAT03 driver's license is required and in PAT06 Social Security number is also required.</td>
<td>$$PAT06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT07 - Last Name</td>
<td>Patient's last name.</td>
<td>$$PAT07^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the FAMILY (LAST) NAME field (#1) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the first comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>PAT08 - First Name</td>
<td>Patient's first name.</td>
<td>$$PAT08^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the GIVEN (FIRST) NAME field (#2) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the first space delimited piece of the second comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT09 - Middle Name</td>
<td>Patient's middle name or initial if available. Used if available in pharmacy system and required by the PDMP.</td>
<td>$$PAT09^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the MIDDLE NAME field (#3) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, the second space delimited piece of the second comma delimited piece of the NAME field (#.01) in the PATIENT file (#2).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT10 - Name Prefix</td>
<td>Patient's name prefix such as Mr. or Dr. Used if available in pharmacy system and required by the PDMP.</td>
<td>$$PAT10^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the PREFIX field (#4) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT11 - Name Suffix</td>
<td>Patient's name suffix such as Jr. or the III. Used if available in pharmacy system and if required by the PDMP.</td>
<td>$$PAT11^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the SUFFIX field (#5) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT12 - Address Information – 1</td>
<td>Field size has been increased to 55 bytes from 35 bytes. However, in order to accommodate pharmacy management systems storing 35 bytes or less for the patient address, no programming change is necessary if that is the maximum length of the field in the pharmacy management system. If the address stored in the system is a P.O. box number, defer to the specifications of the PDMP as to whether this should be reported in PAT12 or PAT13.</td>
<td>$$PAT12^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 1] field (#.111) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT13 - Address Information – 2</td>
<td>Freeform text for additional address information, if required by the PDMP and is available in pharmacy system.</td>
<td>$$PAT13^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 2] field (#.112) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT14 - City Address</td>
<td>Freeform text for city name.</td>
<td>$$PAT14^PSOASAP()</td>
<td><p>Retrieved from the CITY field (#.114) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT15 - State Address</td>
<td><p>U.S. Postal Service state code if required by the PDMP.</p>
<ol start="64">
<li><p>Field has been sized to handle international patients not residing in the U.S.</p></li>
</ol></td>
<td>$$PAT15^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061)”. Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ABBREVATION field (#1) in the STATE file (#5) pointed to by the STATE field (#.115) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the PROVINCE field (#.1171) in the PATIENT file (#2).</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT16 - ZIP Code Address</td>
<td>U.S. Postal Service ZIP code. Exclude hyphen. Postal code will be reported for non-U.S. addresses.</td>
<td>$$PAT16^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ZIP CODE field (#.116) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the POSTAL CODE (#.1172) in the PATIENT file (#2).</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT17 - Phone Number</td>
<td><p>Complete phone number including area code when a state PDMP requires and is available in the pharmacy system.</p>
<ol start="65">
<li><p>Exclude hyphens in the number.</p></li>
</ol></td>
<td>$$PAT17^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>Use PHONE NUMBER [RESIDENCE] field (#.131) in the PATIENT file (#2) if not null</p>
<p>Else use PHONE NUMBER [CELLULAR] field (#.134) in the PATIENT file (#2) if not null</p>
<p>Else PHONE NUMBER [WORK] field (#.132) in the PATIENT file (#2) if not null</p>
<p>Else use K-WORK PHONE NUMBER field (#.21011) in the PATIENT file (#2) if not null</p>
<p>Else use K2-WORK PHONE NUMBER field (#.2199) in the PATIENT file (#2) if not null</p>
<p>Else use E-WORK PHONE NUMBER field (#.33011) in the PATIENT file (#2) if not null</p>
<p>Else use E2-WORK PHONE NUMBER field (#.331011) in the PATIENT file (#2) if not null</p>
<p>Else use AREA CODE field (#.03) in the OUTPATIENT SITE file (#59) concatenated to the PHONE NUMBER field (#.04) in the OUTPATIENT SITE file (#59)</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT18 - Date of Birth</td>
<td>Date patient was born. Format: CCYYMMDD.</td>
<td>$$PAT18^PSOASAP()</td>
<td><p>Retrieved from the DATE OF BIRTH field (#.03) in the PATIENT file (#2)</p>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT19 - Gender Code</td>
<td><p>Code indicating the sex of the patient if required by the PDMP.</p>
<p>F Female</p>
<p>M Male</p>
<p>U Unknown</p></td>
<td>$$PAT19^PSOASAP()</td>
<td><p>Retrieved using the Registration API $$DEM^VADPT (ICR #10061) and return variable VADM(5).</p>
<p>If no value is found, VistA sends 'U'</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT20 - Species Code</td>
<td><p>Used if required by the PDMP to differentiate a prescription for an individual from one prescribed for an animal.</p>
<p>01 Human</p>
<p>02 Veterinary Patient</p></td>
<td>$$PAT20^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT21 - Patient Location Code</td>
<td><p>Code indicating where patient is located when receiving pharmacy services if required by the PDMP.</p>
<p>01 Home</p>
<p>02 Intermediary Care</p>
<p>03 Nursing Home</p>
<p>04 Long-Term/Extended Care</p>
<p>05 Rest Home</p>
<p>06 Boarding Home</p>
<p>07 Skilled-Care Facility</p>
<p>08 Sub-Acute Care Facility</p>
<p>09 Acute-Care Facility</p>
<p>10 Outpatient</p>
<p>11 Hospice</p>
<p>98 Unknown</p>
<p>99 Other</p></td>
<td>$$PAT21^PSOASAP()</td>
<td>VistA sends '10'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT22 - Country of Non-U.S. Resident</td>
<td>Used when the patient’s address is a foreign country. This is a freeform text field. ASAP does not provide a list of countries for this field. PDMPs may permit some of the other address fields to not be used if this field is populated.</td>
<td>$$PAT22^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved If COUNTRY field (#.1173) in the PATIENT file (#2) points to the US in the COUNTRY CODE file (#779.004), VistA returns “” (null).</p>
<p>Else VistA returns the FIPS CODE field (#1.2) in the COUNTRY CODE file (#779.004) pointed to by the COUNTRY field (#.1173) in the PATIENT file (#2).</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT23 - Name of Animal</td>
<td>Used if required by the PDMP for prescriptions written by a veterinarian and the pharmacist has access to this information at the time of preparing the prescription.</td>
<td>$$PAT23^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td colspan="5"><p><strong>PAT07 – PAT09 Note:</strong> The NAME field is a delimited value in which the last name and first name are separated by a comma; the middle name and/or suffix are after the first name separated by a space "LAST,FIRST MIDDLE SUFFIX".</p>
<p><strong>PAT07 – PAT11 Note:</strong> The REGISTRATION package does not allow special characters in the PATIENT name during the registration process, with the exception of spaces, apostrophes, hyphens, and one comma. Since other characters are not permitted via end-user options, the probability of special characters in the PATIENT name fields that would cause a data transmission failure is unlikely.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207089126" class="anchor"></span>Table 51: Pharmacy Trailer (TP) 4.2B

<table>
<caption><p><span id="_Toc207089127" class="anchor"></span>Table 52: Transaction Trailer (TT) 4.2B</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DSP – Dispensing Record Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the basic components of a dispensing a given prescription order including the date and quantity.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>DSP01 - Reporting Status</td>
<td><p>00 New Record</p>
<p>01 Revise</p>
<p>02 Void</p>
<p>DSP01 requires one of the codes below. An empty or blank field no longer indicates a new prescription dispensing transaction. A PDMP may elect to require a subset of the codes below, specifically 00 and 02, but not 01.</p>
<p>00 This code indicates a new prescription dispensing transaction.</p>
<p>01 This code indicates that one or more data element values in a previously submitted transaction are being revised. Examples of when a revision may be necessary include corrections to typographical errors in original data submissions; or change occurred to the prescription between the time the record was submitted and the time the patient picked it up, such as dispensing a smaller metric quantity, adding or correcting patient information, correcting prescriber DEA number, or payment type. When receiving a transaction with a DSP01 value of 01, the PDMP will override all of the detail segments’ data of the original prescription transaction with all of the detail segments’ data from the revised prescription transaction. So it is essential to submit all of the data elements in all of the detail segments populated with the identical data as it appeared in the original record, with only the changed data element(s) content being different (and DSP01 with a value of 01). Do not use 01 in combination with a zero metric quantity to indicate that the prescription was not picked up. Use the value 02 instead as described below. If the PDMP receives a prescription transaction with DSP01 as 01 and a separate prescription transaction with DSP01 as 02, the PDMP will only void the original prescription transaction and will not attempt to apply a revision. Because the PAT segment loops at a higher level than the other detail segments, the only ways to submit revisions to PAT data elements are either: 1) to not loop the DSP segment within the PAT segment – or 2) to loop the DSP segment within PAT segment and have every DSP01 record element within the loop have a DSP01 of 01.</p>
<p>02 This code is a message to the PDMP to remove the original prescription transaction from its database (or to mark the record as invalid and to be ignored). There can be several reasons for sending a void transaction. One example would be when the prescription was never picked up and the medication was returned to stock. Another example would be when the prescription was reported in error. A DSP01 value of 02 can also be used as an alternative to the DSP01 value of 01 in order to send PDMP corrections. When submitting corrections in this manner; first submit a record with a DSP01 of 02 to indicate to the PDMP to void the original prescription transaction; then submit a brand-new prescription transaction with a DSP01 value of 00 with the correct information.</p>
<ol start="66">
<li><p>Examples of the correct use of codes in DSP01 are shown in Appendix D in the ASAP version 4.2b Standard, as well as the limited dataset to void a prescription that PDMPs can elect to use.</p></li>
</ol></td>
<td>$$DSP01^PSOASAP()</td>
<td><p>Derived by retrieving the RECORD TYPE field (#2) in the PRESCRIPTIONS subfile (58.42001) of the SPMP EXPORT BATCH file (#58.42) for the prescription being exported and assigning a code based on the value where:</p>
<p>N = NEW Rx and VistA sends '00' for New Record</p>
<p>R = REFILL and VistA sends '01' for Revise</p>
<p>V = VOID and VistA sends '02' for Void</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP02 - Prescription Number</td>
<td>Serial number assigned to the prescription by the pharmacy.</td>
<td>$$DSP02^PSOASAP()</td>
<td>Retrieved from the RX # field (#52,.01) of the PRESCRIPTION file</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP03 - Date Written</td>
<td>Date the prescription was written (authorized). Format: CCYYMMDD</td>
<td>$$DSP03^PSOASAP()</td>
<td>ISSUE DATE field (#1) retrieved from the PRESCRIPTION file (#52)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP04 - Refills Authorized</td>
<td>The number of refills authorized by the prescriber.</td>
<td>$$DSP04^PSOASAP()</td>
<td>Retrieved from the # OF REFILLS field (#52,9) of the PRESCRIPTION file</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP05 - Date Filled</td>
<td>Date prescription was prepared. Format: CCYYMMDD.</td>
<td>$$DSP05^PSOASAP()</td>
<td><p>Retrieved from one of three locations depending on the type of fill.</p>
<p>Original Fill: RELEASED DATE/TIME field (#31) of the PRESCRIPTION file (#52)</p>
<p>Refill: RELEASED DATE/TIME field (#17) of the REFILL subfile (#52.1)</p>
<p>Partial: RELEASED DATE/TIME field (#8) of the PARTIAL subfile (#52.2)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP06 - Fill Number</td>
<td>Number of the fill of the prescription. 0 indicates original dispensing, 01-99 is the refill number.</td>
<td>$$DSP06^PSOASAP()</td>
<td>Retrieved from the AL and AM cross-references of the PRESCRIPTION file (#52) and PARTIAL DATE subfile (#52.2) respectively.</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP07 - Product ID Qualifier</td>
<td><p>Used to identify the type of product ID contained in DSP08.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 Compound (Used to indicate it is a compound. The CDI segment then becomes a required segment. Also, see instructions for DSP08.)</p></td>
<td>$$DSP07^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP08 - Product ID</td>
<td><p>Full product identification as indicated in DSP07, including leading zeros without punctuation. If the product is a compound, use 99999 as the first five characters of the product code. The remaining six characters are assigned by the pharmacy. The CDI then becomes a required segment.</p>
<ol start="67">
<li><p>If a controlled substance is part of a kit, the NDC of the kit should be reported as long as it is a legitimate manufacturer’s NDC. If not, the NDC of the controlled substance within the kit should be reported. Also, if multiple controlled substances are in the kit, use the CDI segment to report it as a compound.</p></li>
</ol></td>
<td>$$DSP08^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK subfile (52.07)</p>
<p>NDC field (#16)</p>
<p>If not at 52.07,16 then</p>
<p>DRUG file (#50)</p>
<p>NDC field (#31)</p>
<p>If not at 50,31 then</p>
<p>REFILL:</p>
<p>REFILL subfile (#52.1)</p>
<p>NDC field (#11)</p>
<p>ORIGINAL:</p>
<p>PRESCRIPTION file (#52)</p>
<p>NDC field (#27)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP09 - Quantity Dispensed</td>
<td><p>Number of metric units dispensed in metric decimal format.</p>
<p>Example: 2.5.</p>
<ol start="68">
<li><p>Note: For compounds show the first quantity in CDI04. Appendix B in ASAP version 4.2b Standard contains specific instructions.</p></li>
</ol></td>
<td>$$DSP09^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>QTY field (#3)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>QTY field (#7)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>QTY field (#1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.04)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP10 - Days Supply</td>
<td>The calculated or estimated number of days the medication will cover.</td>
<td>$$DSP10^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>DAYS SUPPLY field (#4)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>DAYS SUPPLY field (#8)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>DAYS SUPPLY field (#1.1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.041)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP11 - Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in DSP09, if required by the PDMP.</p>
<p>Appendix B in ASAP version 4.2b Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$DSP11^PSOASAP()</td>
<td><p>Retrieved from the NCPDP DISPENSE UNIT field (#50,82) of the DRUG file.</p>
<p>Coded data:</p>
<p>01-EA</p>
<p>02-ML</p>
<p>03-GM</p>
<p>BLANK</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP12 - Transmission Form of Rx Origin Code</td>
<td><p>Code indicating how the pharmacy received the prescription, if required by the PDMP.</p>
<p>01 Written Prescription</p>
<p>02 Telephone Prescription</p>
<p>03 Telephone Emergency Prescription</p>
<p>04 Fax Prescription</p>
<p>05 Electronic Prescription</p>
<p>06 Transferred/Forwarded Rx</p>
<p>99 Other</p></td>
<td>$$DSP12^PSOASAP()</td>
<td><p>The ORDER ENTRY/RESULTS REPORTING API $$NATURE^ORUTL3 provides the Nature of Order, which is translated the following way:</p>
<p>01 W</p>
<p>02 V or T</p>
<p>05 E</p>
<p>99 Other</p>
<p>ICR# 5890</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP13 - Partial Fill Indicator</td>
<td><p>This field is used when the quantity in DSP09 is less than the metric quantity per dispensing authorized by the prescriber. This dispensing activity is often referred to as a split filling.</p>
<p>00 Not a Partial Fill</p>
<p>01 First Partial Fill</p>
<ol start="69">
<li><p>For additional fills per prescription, increment by 1. So the second partial fill would be reported as 02, up to a maximum of 99</p></li>
</ol></td>
<td>$$DSP13^PSOASAP()</td>
<td><p>Codes indicating partial or non-partial fill:</p>
<p>00 Non-Partial Fill</p>
<p>01 Partial 1</p>
<p>02 Partial 2</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP14 - Pharmacist National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacist by CMS. This number can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP14^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill pharmacist.</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP15 - Pharmacist State License Number</td>
<td>Assigned to the pharmacist by the State Licensing Board. This data element can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP15^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP16 - Classification Code for Payment Type</td>
<td><p>Code identifying the type of payment, i.e. how it was paid for, if required by the PDMP.</p>
<p>01 Private Pay (Cash, Charge, Credit Card)</p>
<p>02 Medicaid</p>
<p>03 Medicare</p>
<p>04 Commercial Insurance</p>
<p>05 Military Installations and VA</p>
<p>06 Workers’ Compensation</p>
<p>07 Indian Nations</p>
<p>99 Other</p></td>
<td>$$DSP16^PSOASAP()</td>
<td>VistA sends '05'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP17 - Date Sold</td>
<td><p>This field is used to determine the date the prescription was dispensed (sold to, picked up by, or otherwise left the pharmacy), not the date it was prepared.</p>
<p>This date could be captured from the point-of-sale (POS) system, if the pharmacy has a POS system, and there is a bidirectional flow with the pharmacy management system in order to capture and report this date. Or it could be captured and reported from a will-call management system, integrated with the pharmacy management system.</p></td>
<td>$$DSP17^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order via $$DSP05^PSOASAP():</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>RELEASED DATE/TIME field (#21)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>RELEASED DATE/TIME field (#31)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>RELEASED DATE/TIME field (#17)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>RELEASED DATE/TIME (#8)</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP18 - RxNorm Product Qualifier</td>
<td><p>01 Semantic Clinical Drug (SCD)</p>
<p>02 Semantic Branded Drug (SBD)</p>
<p>03 Generic Package (GPCK)</p>
<p>04 Branded Package (BPCK)</p>
<p>RxNorm code that is populated in the DRU-010-09 field in the SCRIPT transaction.</p>
<ol start="70">
<li><p>DSP18 and DSP19 are placeholder fields pending RxNorm becoming an industry standard. These fields should not be required until such time.</p></li>
</ol></td>
<td>$$DSP18^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP19 - RxNorm Code</td>
<td>Used for electronic prescriptions to capture the prescribed drug product identification.</td>
<td>$$DSP19^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP20 - Electronic Prescription Reference Number</td>
<td>This field should be populated with the Initiator Reference Number from field UIB-030-01 in the SCRIPT transaction.</td>
<td>$$DSP20^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP21 - Electronic Prescription Order Number</td>
<td><p>This field will be populated with the Initiator Control Reference from field UIH-030-01 in the SCRIPT standard.</p>
<ol start="71">
<li><p>DSP20 and DSP21 should be reported as a pair to the PDMP and the PDMP will decide which one, if not both, it decides to capture. By requiring the reporting of both, this avoids specification variations that would require custom programming to accommodate a PDMP. Also, the information reported by the pharmacy management system will depend on the information received at the pharmacy with an electronic prescription.</p></li>
</ol></td>
<td>$$DSP21^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP22 - Quantity Prescribed</td>
<td>This field has been added in order to add clarity to the value reported in DSP13 Partial Fill Indicator. (Revised 08/17/2020)</td>
<td>$$DSP22^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>DSP23 - Rx SIG</td>
<td>This field would capture the actual directions printed on the prescription vial label. If the directions exceed 200 characters, truncation would be allowed.</td>
<td>$$DSP23^PSOASAP()</td>
<td>Concatenate the SIG1 multiple (#52.04,.01) into a single string</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP24 - Treatment Type</td>
<td><p>This field is used to explain the reason for an opioid prescription. If the prescription is not for an opioid, then this field would not be used.</p>
<p>01 = Not Used for Opioid Dependency Treatment</p>
<p>02 = Used for Opioid Dependency Treatment</p>
<p>03 = Pain Associated with Active and Aftercare Cancer Treatment</p>
<p>04 = Palliative Care in Conjunction with a Serious Illness</p>
<p>05 = End-of-Life and Hospice Care</p>
<p>06 = A Pregnant Individual with a Pre-existing Prescription for Opioids</p>
<p>07 = Acute Pain for an Individual with an Existing Opioid Prescription for Chronic Pain</p>
<p>08 = Individuals Pursuing an Active Taper of Opioid Medications</p>
<p>09 = Patient is Participating in a Pain Management Contract</p>
<p>10 = Acute Opioid Therapy</p>
<p>11 = Chronic Opioid Therapy</p>
<p>99 = Other (trading partner agreed upon reason or not indicated)</p>
<p>The definitions of Codes 03 to 11 can only be reported if mandated by the state to be provided by the prescriber on the prescription order.</p></td>
<td>$$DSP24^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP25 - Diagnosis Code</td>
<td>This field is used to report the ICD-10 code. If required by a PDMP, this field would be populated only when the ICD-10 code is included with the prescription. Exclude the decimal point.</td>
<td>$$DSP25^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089127" class="anchor"></span>Table 52: Transaction Trailer (TT) 4.2B

<table>
<caption><p><span id="_Toc207089128" class="anchor"></span>Table 53: ASAP 5.0 Baseline Dataset - Transaction Header (TH) 5.0</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PRE – Prescriber Information Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the prescriber of the prescription.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PRE01 - National Provider Identifier (NPI)</td>
<td><p>Identifier assigned to the prescriber by CMS.</p>
<ol start="72">
<li><p>If the prescriber does not have a DEA number, and prescribed a noncontrolled substance that is a reportable drug to the PDMP, this field should be used as the identifier.</p></li>
</ol></td>
<td>$$PRE01^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill provider</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE02 - DEA Number</td>
<td>Identifying number assigned to a prescriber or an institution by the Drug Enforcement Administration (DEA). Required when the prescription is for a DEA-defined controlled substance.</td>
<td>$$PRE02^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The first piece by "-" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA#</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) of the NEW PERSON file. The first piece by “-" is returned.</p>
<p>ICR# 2343</p>
<p>Pharmacy DEA#</p>
<p>The Kernel API $$WHAT^XUAF4 is called to return the FACILITY DEA NUMBER field (#4,52) of the INSTITUTION file.</p>
<p>ICR# 2171</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PRE03 - DEA Number Suffix</td>
<td>Identifying number assigned to a prescriber by an institution when the institution's DEA number is used, if required by the PDMP.</td>
<td>$$PRE03^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# suffix associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The 2nd piece by “-" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA# suffix</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) from the NEW DEA #'S multiple of the NEW PERSON file. The 2nd piece by “-" is returned.</p>
<p>ICR# 2343</p>
<p>VA#</p>
<p>If DEA# from PHA03 is equal to the DEA# from PHA02, then The Kernel API $$DEA^XUSER retrieves the value at the VA# field (#200,53.3) of the NEW PERSON file.</p>
<p>ICR# 2171</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE04 - Prescriber License Number</td>
<td>Identification assigned to the prescriber by the State Licensing Board of a state or jurisdiction. This field can be used for veterinarian prescriptions. Used if required by the PDMP.</td>
<td>$$PRE04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE05 - Last Name</td>
<td>Prescriber's last name. Used if required by the PDMP.</td>
<td>$$PRE05^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE06 - First Name</td>
<td>Prescriber's first name. Used if required by the PDMP.</td>
<td>$$PRE06^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE07 - Middle Name</td>
<td>Prescriber's middle name or initial. Used if required and is available in the pharmacy system.</td>
<td>$$PRE07^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE08 - Phone Number</td>
<td>The prescriber's primary phone number.</td>
<td>$$PRE08^PSOASAP()</td>
<td><p>Retrieved from the PHONE NUMBER # field (#200,.132) of the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE09 - XDEA Number</td>
<td>This field gives a PDMP the option of requiring the XDEA Number (NADEAN) in the PRE Segment when the prescription is for opioid dependency.</td>
<td>$$PRE09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PRE10 - Jurisdiction or State Issuing Prescriber License Number</td>
<td>This field can be used to further identify the information in PRE04 depending on PDMP’s need for this information.</td>
<td>$$PRE10^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089128" class="anchor"></span>Table 53: ASAP 5.0 Baseline Dataset - Transaction Header (TH) 5.0

<table>
<caption><p><span id="_Toc207089129" class="anchor"></span>Table 54: Information Source (IS) 5.0</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CDI – Compound Drug Ingredient Detail Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the individual ingredients that make up a compound. To identify the individual ingredients that make up a compound.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Not Used</strong></p></td>
</tr>
<tr class="even">
<td>CDI01 - Compound Drug Ingredient Sequence Number</td>
<td>The first reportable ingredient is 1. Each additional reportable ingredient is incremented by 1.</td>
<td>$$CDI01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI02 - Product ID Qualifier</td>
<td><p>Code to identify the type of product ID contained in CDI03.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 Compound (This code is not used in this segment.)</p></td>
<td>$$CDI02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI03 - Product ID</td>
<td>Full product identification as indicated in CDI02, including leading zeros without punctuation.</td>
<td>$$CDI03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI04 - Component Ingredient Quantity</td>
<td><p>Metric decimal quantity of the ingredient identified in CDI03.</p>
<p>Example: 2.5. Appendix B in ASAP version 4.2b Standard contains specific instructions.</p></td>
<td>$$CDI04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI05 - Compound Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in CDI04, if required by the prescription-monitoring program.</p>
<p>Appendix B in ASAP version 4.2b Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage units or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$CDI05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089129" class="anchor"></span>Table 54: Information Source (IS) 5.0

<table>
<caption><p><span id="_Toc207089130" class="anchor"></span>Table 55: Pharmacy Header (PHA) 5.0</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 15%" />
<col style="width: 27%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AIR – Additional Information Reporting Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To report a prescription blank serial number, information on person dropping off or picking up the prescription, or information regarding the prescription not included in the other detail segments. Note: If this segment is used, at least one of the data elements (fields) will be required.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Optional</strong></p></td>
</tr>
<tr class="even">
<td>AIR01 - State Issuing Rx Serial Number</td>
<td><p>U.S.P.S. state code of state that issued serialized prescription blank. This is required if AIR02 is used.</p>
<p>ASAP version 4.2b Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR02 - State Issued Rx Serial Number</td>
<td>Number assigned to state issued serialized prescription blank. Required if state issues serialized prescription pads for prescribers to use.</td>
<td>$$AIR02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR03 - ID Issuing Jurisdiction</td>
<td><p>Code identifying the jurisdiction that issues the ID contained in AIR05.</p>
<p>Used if required by the PDMP.</p>
<p>ASAP version 4.2b Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR04 - ID Qualifier of Person Dropping Off or Picking Up Rx</td>
<td><p>Code indicating the type of ID in AIR05 if required by the PDMP.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Appriss Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>99 Other (trading partner agreed upon ID such as cardholder ID)</p></td>
<td>$$AIR04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR05 - ID of Person Dropping Off or Picking Up Rx</td>
<td><p>ID number of the person dropping off or picking up the prescription, if required by the PDMP.</p>
<ol start="73">
<li><p>Because historically there has been a noticeable amount of extraneous information entered in this field, which has interfered with data analysis, it is important that every effort be made to ensure that only the unadorned customer ID and no additional information be entered into this field.</p></li>
</ol></td>
<td>$$AIR05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR06 - Relationship of Person Dropping Off or Picking Up Rx</td>
<td><p>Code indicating the relationship to the person, dropping off or picking up Rx, if required by the PDMP.</p>
<p>01 Patient</p>
<p>02 Parent/Legal Guardian</p>
<p>03 Spouse</p>
<p>04 Caregiver</p>
<p>99 Other</p></td>
<td>$$AIR06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR07 - Last Name of Person Dropping Off or Picking Up Rx</td>
<td>Last name of the person dropping off or picking up Rx, if required by the PDMP.</td>
<td>$$AIR07^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR08 - First Name of Person Dropping Off or Picking Up Rx</td>
<td>First name of the person dropping off or picking up the Rx, if required by the PDMP.</td>
<td>$$AIR08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR09 - Last Name or Initials of Pharmacist</td>
<td>Last name or initials of the pharmacist dispensing the medication, if required by the PDMP.</td>
<td>$$AIR09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR10 - First Name of Pharmacist</td>
<td>First name of the pharmacist dispensing the medication, if required by the PDMP.</td>
<td>$$AIR10^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR11 - Dropping Off/Picking Up Identifier Qualifier</td>
<td><p>Additional qualifier for the ID contained in AIR05.</p>
<p>01 Person Dropping Off</p>
<p>02 Person Picking Up</p>
<p>98 Unknown/Not Applicable (An example of Unknown: Where the pharmacist does not know which person it is. Or there is no ID to collect at drop-off, such as when a prescription is phoned in.</p>
<p>An example of Not Applicable: When the prescription is delivered.)</p>
<ol start="74">
<li><p>Both 01 and 02 cannot be required by a PDMP. Usage of this field depends on whether a PDMP has interest in knowing whether the information supplied in fields AIR04–AIR08 is for the person dropping off or picking up the prescription.</p></li>
</ol></td>
<td>$$AIR11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089130" class="anchor"></span>Table 55: Pharmacy Header (PHA) 5.0

<table>
<caption><p><span id="_Toc207089131" class="anchor"></span>Table 56: Patient Information (PAT) 5.0</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 32%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TP – Pharmacy Trailer Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the end of data for a given pharmacy and provide the count of the total number of detail segments included for the pharmacy, including the pharmacy header (PHA) and the pharmacy trailer (TP) segments.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TP01 - Detail Segment Count</td>
<td>Number of detail segments included for the pharmacy including the pharmacy header (PHA) and the pharmacy trailer (TP) segments.</td>
<td>$$TP01^PSOASAP()</td>
<td>Calculates the number of detail segments included (PAT, DSP, PRE, CDI, AIR) in addition to the pharmacy header (PHA) and pharmacy trailer (TP)</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089131" class="anchor"></span>Table 56: Patient Information (PAT) 5.0

<table>
<caption><p><span id="_Toc207089132" class="anchor"></span>Table 57: Dispensing Record (DSP) 5.0</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 32%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TT – Transaction Trailer Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To indicate the end of the transaction and provide the count of the total number of segments included in the transaction.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TT01 - Transaction Control Number</td>
<td>Identifying control number that must be unique. Assigned by the originator of the transaction. Must match the number in TH02 sent by the pharmacy.</td>
<td>$$TT01^PSOASAP()</td>
<td>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file. (ex: 500-182)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TT02 - Segment Count</td>
<td>Total number of segments included in the transaction including the header (TH) and trailer (TT) segments.</td>
<td>$$TT02^PSOASAP()</td>
<td>Calculated for each transmission.</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089132" class="anchor"></span>Table 57: Dispensing Record (DSP) 5.0

#### ASAP Standard Version 5.0 Implementation

<table>
<caption><p><span id="_Toc207089133" class="anchor"></span>Table 58: Prescriber Information (PRE) 5.0</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TH – Transaction Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To indicate the start of a transaction. It also assigns the segment terminator, data element separator, and control number.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TH01 - Version / Release Number</td>
<td><p>Used to identify the transaction Version/Release.</p>
<p>Format = x.x (5.0)</p>
<p>ASAP Version 5 Release 0</p></td>
<td>$$TH01^PSOASAP()</td>
<td>ASAP VERSION field (#1) retrieved from the SPMP STATE PARAMETERS file (#58.41)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH02 - Transaction Control Number</td>
<td><p>Sender assigned code uniquely identifying a transaction. This number must be used in TT01.</p>
<p>Recommendation: Use a Globally Unique Identifier (GUID) or other nonrepeating alphanumeric combination to populate this field.</p></td>
<td>$$TH02^PSOASAP()</td>
<td><p>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file.</p>
<p>(ex: 500-182)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH03 - Transaction Type</td>
<td><p>Identifies the purpose of initiating the transaction.</p>
<p>01 Send/Request Transaction</p>
<p>02 Acknowledgment (Used in Response only.)</p>
<p>03 Error Receiving (Used in Response only.)</p>
<p>04 Void (Used to void a specific Rx in a real-time transmission, or an entire batch file that has been transmitted.</p>
<p>When 04 is used the appropriate transaction control number in TH02 for the specific prescription or batch file must be included. When 04 is used only the TH Header Segment and the Transaction Trailer Segment are used.)</p></td>
<td>$$TH03^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>TH04 - Response ID</td>
<td>Contains the Transaction Control Number of a transaction that initiated the transaction. Required in response transaction only.</td>
<td>$$TH04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH05 - Creation Date</td>
<td>Date the file was created. Format: CCYYMMDD.</td>
<td>$$TH05^PSOASAP()</td>
<td><p>Kernel API - $$FMTHL7^XLFDT($$HTFM^XLFDT($H)</p>
<p>Example: 20240904</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH06 - Creation Time</td>
<td>Time expressed in 24-hour clock time HHMMSS or HHMM). Time range: 000000 through 235959. The time zone should be reported in Coordinated Universal Time (UTC) as HHMMSSZ (e.g., 235959Z). Do not include colons or non-numeric characters other than Z for Zulu time.</td>
<td>$$TH06^PSOASAP()</td>
<td><ol type="1">
<li><blockquote>
<p>Call Kernel API - $$HTFM^XLFDT($H)which returns back UTC date/time</p>
</blockquote></li>
</ol>
<blockquote>
<p>Example: 091522</p>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Take the TIME value of the returned date/time stamp and set that data to be exactly 6 in length and append a “Z" to the end.</p>
</blockquote></li>
</ol></td>
<td>Required</td>
</tr>
<tr class="even">
<td>TH07 - File Type</td>
<td><p>Code specifying the type of transaction.</p>
<p>P Production</p>
<p>T Test</p></td>
<td>$$THO7^PSOASAP()</td>
<td>Retrieved via the Kernel API - $$PROD^XUPROD(1)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TH08 - Routing Number/BIN</td>
<td>This field can be used for real-time transmissions that go through an intermediary or network switch to indicate, if necessary, the specific state that the transactions should be routed to.</td>
<td>$$TH08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>TH09 - Segment Terminator Character</td>
<td><p>This terminates the TH segment and sets the actual value of the data segment terminator for the entire transaction.</p>
<ol start="75">
<li><p>The ASAP 5.0 Standard document uses the “~” in all examples. See the “Data Element Separators and Segment Terminators” in the standard's introduction for more information.</p></li>
</ol></td>
<td>$$TH09^PSOASAP()</td>
<td>Retrieved from the SEGMENT TERMINATOR CHAR field (#58.4001,.03) of the SPMP ASAP RECORD DEFINITION file. Tilde character "~"</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089133" class="anchor"></span>Table 58: Prescriber Information (PRE) 5.0

<table style="width:100%;">
<caption><p><span id="_Toc207089134" class="anchor"></span>Table 59: Compound Drug Ingredient (CDI) 5.0</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>IS – Information Source Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To convey the name and identification number of the entity supplying the information.</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>IS01 - Unique Information Source ID</td>
<td>Reference number or identification number as defined by the business partners. (Example: Phone number. However, if a phone number is used to populate this field, do not include hyphens.)</td>
<td>$$IS01^PSOASAP()</td>
<td><ol type="1">
<li><p>Call REGISTRATION's $$SITE^VASITE to get the 3-digit VA SITE CODE (e.g.,500)</p></li>
<li><p>Use the VA SITE CODE to find the first valid OUTPATIENT SITE entry at the SITE NUMBER (59,.06) x-ref.</p></li>
<li><p>If there isn't a match at the SITE NUMBER x-ref then populate IS01 with the VA SITE CODE retrieved at step 1 concatenated with the ZIP (4, 1.04) W/0 any hyphen and quit</p></li>
<li><p>Call $$NPI^XUSNPI passing in file 59 ien retrieved at the SITE NUMBER x-ref and the “"Organizational_ID""</p></li>
<li><p>If the NPI is not returned at step 4, then populate IS01 with the VA SITE CODE retrieved at step 1 concatenated with the ZIP (4, 1.04) W/0 any hyphen and quit</p></li>
<li><p>Return NPI that was returned at step 4</p></li>
</ol></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>IS02 - Information Source Entity Name</td>
<td>Entity name of the Information Source.</td>
<td>$$IS02^PSOASAP()</td>
<td><p>OFFICIAL VA NAME field (#100) retrieved from the INSTITUTION file (#4)</p>
<p>Example: OKLAHOMA CITY VA MEDICAL CENTER</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>IS03 - Message</td>
<td><p>Freetext message. Use of this field is defined by the PDMP. PDMPs may designate this field to hold the submission period date range of the file transmitted. When used to indicate the date range, it must be the first data text in the field and must be inserted using the following layout (where "#" and "-" are those literal characters): #CCYYMMDD#-#CCYYMMDD#</p>
<p>For example, a pharmacy may be submitting records for the reporting period of February 5, 2023 through February 11, 2023 but only filled reportable prescriptions on February 5 and February 7. The full submission period date range would be reported in IS03 as #20230205#-#20230211#. It is up to the PDMP to further define how to enter the submission date range for exceptional cases, such as for late submission records.</p>
<ol start="76">
<li><p>IS03 can also be used to show the date range for Zero Reports.</p></li>
</ol></td>
<td>$$IS03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>IS04 - Pharmacy Dispensing Software Vendor</td>
<td>Name of software vendor the pharmacy is using.</td>
<td>$$IS04^PSOASAP()</td>
<td>VistA sends DEPT OF VET AFFAIRS - OFFICE OF INFORMATION AND TECHNOLOGY</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>IS05 - Phone Number of Software Vendor</td>
<td>No description provided in standard.</td>
<td>$$IS05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089134" class="anchor"></span>Table 59: Compound Drug Ingredient (CDI) 5.0

<table>
<caption><p><span id="_Toc207089135" class="anchor"></span>Table 60: Additional Information Reporting (AIR) 5.0</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PHA – Pharmacy Header Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the pharmacy or the dispensing prescriber. It is required that information be provided in at least one of the following fields: PHA01, PHA02, or PH03. (Note: PHA04 through PHA13 can be used if needed by the state to further identify the sending entity.)</strong></p>
<p><strong>Level: Header</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PHA01 - National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacy by CMS. Used if required by the PDMP.</td>
<td>$$PHA01^PSOASAP()</td>
<td>NPI INSTITUTION field (#101) retrieved via the Kernel API $$NPI^XUSNPI (ICR# 4532) from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA02 - NCPDP Provider ID</td>
<td>Identifier assigned to pharmacy by the National Council for Prescription Drug Programs. Used if required by the PDMP.</td>
<td>$$PHA02^PSOASAP()</td>
<td>NCPDP NUMBER field (#1008) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA03 - DEA Number</td>
<td>Identifier assigned to the pharmacy by the Drug Enforcement Administration. Used if required by the PDMP.</td>
<td>$$PHA03^PSOASAP()</td>
<td>FACILITY DEA NUMBER (#4,52) retrieved via the Kernel API $$WHAT^XUAF4 (ICR# 2171) using the RELATED INSTITUTION field (#100) in the OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA04 - Pharmacy or Dispensing Prescriber Name</td>
<td><p>Freetext name of the pharmacy.</p>
<ol start="77">
<li><p>If a dispensing prescriber, the prescriber’s name and professional degree should be entered, such as John Doe MD.</p></li>
</ol></td>
<td>$$PHA04^PSOASAP()</td>
<td>NAME field (#.01) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA05 - Address Information – 1</td>
<td><p>Freetext for address information.</p>
<p>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</p></td>
<td>$$PHA05^PSOASAP()</td>
<td>MAILING FRANK STREET ADDRESS field (#.02) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA06 - Address Information - 2</td>
<td><p>Freetext for address additional information.</p>
<p>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</p></td>
<td>$$PHA06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA07 - City Address</td>
<td>Freetext for city name.</td>
<td>$$PHA07^PSOASAP()</td>
<td>MAILING FRANK CITY field (#.07) retrieved from OUTPATIENT SITE file (#59)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA08 - State Address</td>
<td>Two-letter jurisdiction/state and possession abbreviation as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$PHA08^PSOASAP()</td>
<td><p>ABBREVIATION field (#1) retrieved from the STATE file (#5) via pointer MAILING FRANK STATE field (#.08) in the OUTPATIENT SITE file (#59)</p>
<p>Example: OK</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA09 - ZIP Code Address</td>
<td>United States Postal Service ZIP Code or ZIP+4 as described in United States Postal Service Publication 28 Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses. Do not include white spaces or special characters. Include hyphens in ZIP+4.</td>
<td>$$PHA09^PSOASAP()</td>
<td><p>MAILING FRANK ZIP+4 CODE field (#.05) retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="78">
<li><p>hyphen included</p></li>
</ol>
<p>Example: 73104-5028</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA10 - Phone Number</td>
<td>Complete phone number including area code. Exclude hyphens.</td>
<td>$$PHA10^PSOASAP()</td>
<td><p>AREA CODE (#.03) and PHONE NUMBER (#.04) fields retrieved from OUTPATIENT SITE file (#59)</p>
<ol start="79">
<li><p>hyphens excluded</p></li>
</ol>
<p>Example: 4056948387</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA11 - Contact Name</td>
<td>Freetext name of vendor contact.</td>
<td>$$PHA11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA12 - Chain Site ID</td>
<td>Store number assigned by the chain to the pharmacy location. Used when PDMP needs to identify the specific pharmacy from which information is required.</td>
<td>$$PHA12^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA13 - Pharmacy's Permit Number/License Number</td>
<td>Used to help identify the sending pharmacy.</td>
<td>$$PHA13^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PHA14 - Pharmacy/Dispenser Type</td>
<td><p>01 Independent Pharmacy</p>
<p>02 Chain Pharmacy</p>
<p>03 Long-term Care Pharmacy</p>
<p>04 Hospital Pharmacy</p>
<p>05 Opioid Treatment Program</p>
<p>06 Cannabis Dispensary</p>
<p>07 Veterinary/ Vet Patient Only Dispenser</p>
<p>08 Dispensing Prescriber</p>
<p>09 Specialty Pharmacy</p>
<p>10 Federal</p>
<p>11 Tribal</p>
<p>99 Other</p></td>
<td>$$PHA14^PSOASAP()</td>
<td>VistA sends '10'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PHA15 - Mail Order Pharmacy</td>
<td><p>01 Yes</p>
<p>02 No</p></td>
<td>$$PHA15^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089135" class="anchor"></span>Table 60: Additional Information Reporting (AIR) 5.0

<table>
<caption><p><span id="_Toc207089136" class="anchor"></span>Table 61: Pharmacy Trailer (TP) 5.0</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 27%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PAT – Patient Information Segment</strong></td>
<td colspan="4"><p><strong>Purpose: Used to report the patient’s name and basic information as contained in the pharmacy record.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PAT01 - ID Qualifier of Patient Identifier</td>
<td><p>Code identifying the jurisdiction that issues the ID in PAT03.</p>
<p>Used if the PDMP requires such identification.</p>
<p>If PAT01 is populated, then PAT02 and PAT03 must be populated as well.</p>
<p>ASAP version 5.0 Standard Appendix A lists jurisdictions.</p></td>
<td>$$PAT01^PSOASAP()</td>
<td>VistA sends 'US'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT02 - ID Qualifier</td>
<td><p>Code to identify the type of ID in PAT03. If PAT02 is used, PAT03 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Bamboo Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>11 Medicaid Recipient ID Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID)</p></td>
<td>$$PAT02^PSOASAP()</td>
<td>VistA sends '07'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT03 - ID of Patient</td>
<td><p>Identification number for the patient as indicated in PAT02. An example would be the driver’s license number.</p>
<ol start="80">
<li><p>This field can only be populated with code 10 when provided on the prescription.</p></li>
</ol></td>
<td>$$PAT03^PSOASAP()</td>
<td><p>Retrieved from the SOCIAL SECURITY NUMBER field (#2,.09) of the PATIENT file via the REGISTRATION DEM^VADPT API</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT04 - ID Qualifier of Additional Patient Identifier</td>
<td>Code identifying the jurisdiction that issues the ID in PAT06. Used if the PDMP requires such identification. ASAP version 5.0 Standard Appendix A lists jurisdictions.</td>
<td>$$PAT04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT05 - Additional Patient ID Qualifier</td>
<td><p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver's License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Bamboo Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>11 Medicaid Recipient ID Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$PAT05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT06 - Additional ID</td>
<td>Identification that might be required by the PDMP to further identify the individual. An example might be in that PAT03 driver’s license is required and in PAT06 Social Security number is also required.</td>
<td>$$PAT06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT07 - Last Name</td>
<td><p>Patient’s last name.</p>
<p>Recommended way to report:</p>
<p>Report the patient’s complete legal last name ONLY as listed on a government-issued identification</p>
<p>Do NOT report extraneous information or notes in this field</p>
<p>Do NOT enter Prefix or Suffix in Last Name field</p>
<p>Do NOT report special characters (e.g., parentheses, asterisk) other than a hyphen or apostrophe.</p>
<p>If for a veterinary patient, enter information of PERSON responsible for the care of the animal or who arranges for the animal’s veterinary care</p></td>
<td>$$PAT07^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><blockquote>
<p>If the patient DFN exists in the NAME COMPONENTS file (#20), PAT07 is assigned the value at the FAMILY (LAST) NAME field (#1) in the NAME COMPONENTS file (#20).</p>
</blockquote></li>
<li><blockquote>
<p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, PAT07 is assigned the value before the first comma of the NAME field (#.01) in the PATIENT file (#2).</p>
</blockquote></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>PAT08 - First Name</td>
<td><p>Patient’s first name.</p>
<p>Recommended way to report:</p>
<p>Report the patient’s complete legal first name ONLY as listed on a government-issued identification</p>
<p>Do NOT report extraneous information or notes in this field</p>
<p>Do NOT enter Prefix or Suffix in First Name field</p>
<p>Do NOT report special characters (e.g., parentheses, asterisk) other than a hyphen or apostrophe.</p>
<p>If for a veterinary patient, enter information of PERSON responsible for the care of the animal or who arranges for the animal’s veterinary care</p></td>
<td>$$PAT08^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), PAT08 is assigned the value at the GIVEN (FIRST) NAME field (#2) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, PAT08 is assigned the value before the first space and after the first comma of the NAME field (#.01) in the PATIENT file (#2). </p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT09 - Middle Name</td>
<td>Patient's middle name or initial if available. Used if available in pharmacy system and required by the PDMP.</td>
<td>$$PAT09^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), PAT09 is assigned to the value at the MIDDLE NAME field (#3) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, PAT09 is assigned the value after the first comma and after the first space of the NAME field (#.01) in the PATIENT file (#2). </p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT10 - Name Prefix</td>
<td>Patient’s name prefix such as Mr. or Dr. Used if available in pharmacy system and required by the PDMP. Do not report special characters other than a hyphen or a period.</td>
<td>$$PAT10^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the PREFIX field (#4) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT11 - Name Suffix</td>
<td><p>Patient’s name suffix such as Jr. or the III.</p>
<p>Used if available in pharmacy system and if required by the PDMP.</p>
<p>Do not report special characters other than a hyphen or a period.</p></td>
<td>$$PAT11^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<ol start="3" type="1">
<li><p>If the patient DFN exists in the NAME COMPONENTS file (#20), the SUFFIX field (#5) in the NAME COMPONENTS file (#20).</p></li>
<li><p>If no entry exists in the NAME COMPONENTS file (#20) for the patient DFN, VistA sends “” (null).</p></li>
</ol>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT12 - Address Information – 1</td>
<td><p>If the pharmacy management system stores 35 bytes or less for the address, no programming change is necessary. If the address stored in the system is a P.O. box number, defer to the specifications of the PDMP as to whether this should be</p>
<p>reported in PAT12 or PAT13.</p>
<p>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</p></td>
<td>$$PAT12^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 1] field (#.111) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT13 - Address Information – 2</td>
<td>Freetext for additional address information, if required by the PDMP and is available in pharmacy system. Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</td>
<td>$$PAT13^PSOASAP()</td>
<td><p>Retrieved from the STREET ADDRESS [LINE 2] field (#.112) in the PATIENT file (#2)</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT14 - City Address</td>
<td>Freetext for city name.</td>
<td>$$PAT14^PSOASAP()</td>
<td><p>Retrieved from the CITY field (#.114) in the PATIENT file (#2).</p>
<p>Retrieved using the REGISTRATION API, ADD^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT15 - Jurisdiction/State Address</td>
<td>Jurisdiction / state and possession abbreviation as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$PAT15^PSOASAP()</td>
<td><p>Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ABBREVATION field (#1) in the STATE file (#5) pointed to by the STATE field (#.115) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the PROVINCE field (#.1171) in the PATIENT file (#2).</p>
<p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>PAT16 - ZIP Code Address</td>
<td><p>United States Postal Service ZIP Code or ZIP+4 as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</p>
<p>Do not include white spaces or special characters. Include hyphens in ZIP+4. Postal code will be reported for non-U.S. addresses.</p></td>
<td>$$PAT16^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is the United States, retrieved from the ZIP CODE field (#.116) in the PATIENT file (#2).</p>
<p>If the COUNTRY field (#.1173) in the PATIENT file (#2) is not the United States, retrieved from the POSTAL CODE (#.1172) in the PATIENT file (#2).</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT17 - Phone Number</td>
<td><p>Complete phone number including area code when a state PDMP requires and is available in the pharmacy system.</p>
<ol start="81">
<li><p>Exclude hyphens.</p></li>
</ol></td>
<td>$$PAT17^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved using the following logic:</p>
<p>Use PHONE NUMBER [RESIDENCE] field (#.131) in the PATIENT file (#2) if not null</p>
<p>Else use PHONE NUMBER [CELLULAR] field (#.134) in the PATIENT file (#2) if not null</p>
<p>Else PHONE NUMBER [WORK] field (#.132) in the PATIENT file (#2) if not null</p>
<p>Else use K-WORK PHONE NUMBER field (#.21011) in the PATIENT file (#2) if not null</p>
<p>Else use K2-WORK PHONE NUMBER field (#.2199) in the PATIENT file (#2) if not null</p>
<p>Else use E-WORK PHONE NUMBER field (#.33011) in the PATIENT file (#2) if not null</p>
<p>Else use E2-WORK PHONE NUMBER field (#.331011) in the PATIENT file (#2) if not null</p>
<p>Else use AREA CODE field (#.03) in the OUTPATIENT SITE file (#59) concatenated to the PHONE NUMBER field (#.04) in the OUTPATIENT SITE file (#59)</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT18 - Date of Birth</td>
<td>Owner’s date of birth as listed on a government-issued identification. If for a veterinary patient Date of Birth should be listed as directed by applicable state/jurisdiction PDMP laws and regulations. Format: CCYYMMDD.</td>
<td>$$PAT18^PSOASAP()</td>
<td><p>Retrieved from the DATE OF BIRTH field (#.03) in the PATIENT file (#2)</p>
<p>Retrieved using the REGISTRATION API, DEM^VADPT</p>
<p>ICR #10061</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PAT19 - Gender Code</td>
<td><p>Codes indicating the sex of the patient if required by the PDMP.</p>
<p>F Female</p>
<p>M Male</p>
<p>N Non-Binary</p>
<p>U Unknown / Undisclosed</p>
<p>X Unspecified/Other</p></td>
<td>$$PAT19^PSOASAP()</td>
<td><p>Retrieved using the Registration API $$DEM^VADPT (ICR #10061) and return variable VADM(5).</p>
<p>If no value is found, VistA sends 'U'</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT20 - Species Code</td>
<td><p>Used if required by the PDMP to differentiate a prescription for an individual from one prescribed for an animal.</p>
<p>01 Human</p>
<p>02 Veterinary Patient</p></td>
<td>$$PAT20^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT21 - Patient Location Code</td>
<td><p>Code indicating where patient is located when receiving services, if required by PDMP.</p>
<p>01 Home</p>
<p>02 Intermediary Care</p>
<p>03 Nursing Home</p>
<p>04 Long-Term/Extended Care</p>
<p>05 Rest Home</p>
<p>06 Boarding Home</p>
<p>07 Skilled-Care Facility</p>
<p>08 Sub-Acute Care Facility</p>
<p>09 Acute-Care Facility</p>
<p>10 Outpatient</p>
<p>11 Hospice</p>
<p>12 Homeless/Unhoused</p>
<p>13 Transient Care</p>
<p>98 Unknown</p>
<p>99 Other</p></td>
<td>$$PAT21^PSOASAP()</td>
<td>VistA sends '10'</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT22 - Country of Non-U.S. Resident</td>
<td>Used when the patient’s address is a foreign country. This is a freetext field. ASAP does not provide a list of countries for this field. PDMPs may permit some of the other address fields to not be used if this field is populated.</td>
<td>$$PAT22^PSOASAP()</td>
<td><p>API ADD^VADPT is called and it is a supported reference to the REGISTRATION API. (ICR# 10061).</p>
<p>Retrieved If COUNTRY field (#.1173) in the PATIENT file (#2) points to the US in the COUNTRY CODE file (#779.004), VistA returns “” (null).</p>
<p>Else VistA returns the FIPS CODE field (#1.2) in the COUNTRY CODE file (#779.004) pointed to by the COUNTRY field (#.1173) in the PATIENT file (#2).</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT23 - Name of Animal</td>
<td>Used if required by the PDMP for prescriptions written by a veterinarian. An unnamed animal could be described as COWSmith or as COW1Smith.</td>
<td>$$PAT23^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PAT24 - Patient Preferred or Alias Last Name</td>
<td>May be used for a preferred name, previous name, nickname, alias, or name used on insurance card if different than legal last name.</td>
<td>$$PAT24^PSOASAP1()</td>
<td><p>If available, returns the value in the first piece by "," from the ALIAS field (#.01) of the PATIENT file (#2).</p>
<p>ICR# 5708</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT25 - Patient Preferred or Alias First Name</td>
<td>Maybe used for a preferred name, previous name, nickname, alias, or name used on insurance card if different than legal first name.</td>
<td>$$PAT25^PSOASAP1()</td>
<td><p>If available, returns the value in the second piece by "," from the ALIAS field (#.01) of the PATIENT file (#2).</p>
<p>ICR# 5708</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT26 - Patient Race Category</td>
<td><p>Code used for general race category.</p>
<p>01 American Indian or Alaskan Native</p>
<p>02 Asian</p>
<p>03 Black or African American</p>
<p>04 Native Hawaiian or Other Pacific Islander</p>
<p>05 White</p>
<p>06 Multiracial</p>
<p>99 Other/Unknown</p></td>
<td>$$PAT26^PSOASAP1()</td>
<td><p>Retrieved using the supported call to DEM^VADPT API including the array element for the RACE related field VADM(12). The RACE INFORMATION (#2.02,.01) is evaluated and the proper RACE category is applied. For multi-racial, if the PATIENT has more than one race then apply code 06.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PAT27 - Patient Ethnicity</td>
<td><p>Code used to describe general ethnicity group of the patient.</p>
<p>01 Hispanic or Latino</p>
<p>02 Not Hispanic or Latino</p>
<p>99 Undisclosed/Unknown</p></td>
<td>$$PAT27^PSOASAP1()</td>
<td><p>Retrieval of the ETHINICITY data from the DEM^VADPT call including the array element for ETHNICITY related field VADM(11).</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PAT28 - Veterinary Species Code</td>
<td><p>Code used to describe animal species.</p>
<p>01 Cat/Feline</p>
<p>02 Dog/Canine</p>
<p>03 Small Animal (Hamster, Rabbit, Other Rodent)</p>
<p>04 Reptile</p>
<p>05 Bird</p>
<p>06 Livestock, Large Animal</p>
<p>99 Other</p></td>
<td>$$PAT28^PSOASAP1()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>PAT29 - Animal Location Code</td>
<td><p>Animal Location Code.</p>
<p>01 Home</p>
<p>02 Animal Shelter</p>
<p>03 Foster</p>
<p>04 Farm</p>
<p>05 Zoo</p>
<p>06 Circus/Traveling Show</p>
<p>99 Other</p></td>
<td>$$PAT29^PSOASAP1()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td colspan="5"><p><strong>PAT07 – PAT09 Note:</strong> The NAME field is a delimited value in which the last name and first name are separated by a comma; the middle name and/or suffix are after the first name separated by a space "LAST,FIRST MIDDLE SUFFIX".</p>
<p><strong>PAT07 – PAT11 Note:</strong> The REGISTRATION package does not allow special characters in the PATIENT name during the registration process, with the exception of spaces, apostrophes, hyphens, and one comma. Since other characters are not permitted via end-user options, the probability of special characters in the PATIENT name fields that would cause a data transmission failure is unlikely.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc207089136" class="anchor"></span>Table 61: Pharmacy Trailer (TP) 5.0

<table style="width:100%;">
<caption><p><span id="_Toc207089137" class="anchor"></span>Table 62: Transaction Trailer (TT) 5.0</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DSP – Dispensing Record Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the basic components of a dispensing of a given prescription order including the date and quantity.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>DSP01 - Reporting Status</td>
<td><p>00 New Record</p>
<p>01 Revise</p>
<p>02 Void</p>
<p>DSP01 requires one of the codes below. An empty or blank field no longer indicates a new prescription dispensing transaction. A PDMP may elect to require a subset of the codes below, specifically 00 and 02, but not 01.</p>
<p>00 This code indicates a new prescription dispensing transaction.</p>
<p>01 This code indicates that one or more data element values in a previously submitted transaction are being revised. Examples of when a revision may be necessary include corrections to typographical errors in original data submissions; or change occurred to the prescription between the time the record was submitted and the time the patient picked it up, such as dispensing a smaller metric quantity, adding or correcting patient information, correcting prescriber DEA number, or payment type. When receiving a transaction with a DSP01 value of 01, the PDMP will override all of the detail segments’ data of the original prescription transaction with all of the detail segments’ data from the revised prescription transaction. It is essential to submit all of the data elements in all of the detail segments populated with the identical data as it appeared in the original record, with only the changed data element(s) content being different (and DSP01 with a value of 01). Do not use 01 in combination with a zero metric quantity to indicate that the prescription was not picked up. Use the value 02 instead as described below. If the PDMP receives a prescription transaction with DSP01 as 01 and a separate prescription transaction with DSP01 as 02, the PDMP will only void the original prescription transaction and will not attempt to apply a revision. Because the PAT segment loops at a higher level than the other detail segments, the only ways to submit revisions to PAT data elements are either: 1) to not loop the DSP segment within the PAT segment or 2) to loop the DSP segment within PAT segment and have every DSP01 record element within the loop have a DSP01 of 01.</p>
<p>02 This code is a message to the PDMP to remove the original prescription transaction from its database (or to mark the record as invalid and to be ignored). There can be several reasons for sending a void transaction. One example would be when the prescription was never picked up and the medication was returned to stock. Another example would be when the prescription was reported in error. A DSP01 value of 02 can also be used as an alternative to the DSP01 value of 01 in order to send PDMP corrections. When submitting corrections in this manner; first submit a record with a DSP01 of 02 to indicate to the PDMP to void the original prescription transaction; then submit a brand-new prescription transaction with a DSP01 value of 00 with the correct information.</p>
<ol start="82">
<li><p>Examples of the correct use of codes in DSP01 <strong>are</strong> shown in Appendix D <strong>in the ASAP version 5.0 Standard</strong>, as well as the limited data set to void a prescription that PDMPs can elect to use.</p></li>
</ol></td>
<td>$$DSP01^PSOASAP()</td>
<td><p>Derived by retrieving the RECORD TYPE field (#2) in the PRESCRIPTIONS subfile (58.42001) of the SPMP EXPORT BATCH file (#58.42) for the prescription being exported and assigning a code based on the value where:</p>
<p>N = NEW Rx and VistA sends '00' for New Record</p>
<p>R = REFILL and VistA sends '01' for Revise</p>
<p>V = VOID and VistA sends '02' for Void</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP02 - Prescription Number</td>
<td>Serial number assigned to the prescription by the pharmacy.</td>
<td>$$DSP02^PSOASAP()</td>
<td>Retrieved from the RX # field (#52,.01) of the PRESCRIPTION file</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP03 - Date Written</td>
<td>Date the prescription was written (authorized). Format: CCYYMMDD</td>
<td>$$DSP03^PSOASAP()</td>
<td>ISSUE DATE field (#1) retrieved from the PRESCRIPTION file (#52)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP04 - Refills Authorized</td>
<td>The number of refills authorized by the prescriber.</td>
<td>$$DSP04^PSOASAP()</td>
<td>Retrieved from the # OF REFILLS field (#52,9) of the PRESCRIPTION file</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP05 - Date Filled</td>
<td>Date prescription was prepared. Format: CCYYMMDD.</td>
<td>$$DSP05^PSOASAP()</td>
<td><p>Retrieved from one of three locations depending on the type of fill.</p>
<p>Original Fill: RELEASED DATE/TIME field (#31) of the PRESCRIPTION file (#52)</p>
<p>Refill: RELEASED DATE/TIME field (#17) of the REFILL subfile (#52.1)</p>
<p>Partial: RELEASED DATE/TIME field (#8) of the PARTIAL subfile (#52.2)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP06 - Fill Number</td>
<td>Number of the fill of the prescription. 0 indicates original dispensing, 01-99 is the refill number.</td>
<td>$$DSP06^PSOASAP()</td>
<td>Retrieved from the AL and AM cross-references of the PRESCRIPTION file (#52) and PARTIAL DATE subfile (#52.2) respectively.</td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP07 - Product ID Qualifier</td>
<td><p>Used to identify the type of product ID contained in DSP08.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 Compound (Used to indicate it is a compound. The CDI segment then becomes a required segment. Also, see instructions for DSP08.)</p>
<p>07 Cannabis</p></td>
<td>$$DSP07^PSOASAP()</td>
<td>VistA sends '01'</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP08 - Product ID</td>
<td><p>Full product identification as indicated in DSP07, including zeros without punctuation. If DSP07 = 01, then DSP08 should contain the 11-digit NDC code without hyphens. If the product is a compound, use 99999 as the first five characters of the product code. The remaining six characters are assigned by the pharmacy. The CDI then becomes a required segment.</p>
<ol start="83">
<li><p>If a controlled substance is part of a kit, the NDC of the kit should be reported if it is a legitimate manufacturer’s NDC. If not, the NDC of the controlled substance within the kit should be reported. Also, if multiple controlled substances are in the kit, use the CDI segment to report it as a compound.</p></li>
</ol></td>
<td>$$DSP08^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>VOID:</p>
<p>RETURN TO STOCK subfile (52.07)</p>
<p>NDC field (#16)</p>
<p>If not at 52.07,16 then</p>
<p>DRUG file (#50)</p>
<p>NDC field (#31)</p>
<p>If not at 50,31 then</p>
<p>REFILL:</p>
<p>REFILL subfile (#52.1)</p>
<p>NDC field (#11)</p>
<p>ORIGINAL:</p>
<p>PRESCRIPTION file (#52)</p>
<p>NDC field (#27)</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP09 - Quantity Dispensed</td>
<td><p>Number of metric units dispensed in metric decimal format.</p>
<p>Example: 2.5.</p>
<ol start="84">
<li><p>For compounds show the first quantity in CDI04. Appendix B in ASAP version 5.0 Standard contains specific instructions.</p></li>
</ol></td>
<td>$$DSP09^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>QTY field (#3)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>QTY field (#7)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>QTY field (#1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.04)</p></td>
<td>Required</td>
</tr>
<tr class="odd">
<td>DSP10 - Days Supply</td>
<td>The calculated or estimated number of days the medication will cover.</td>
<td>$$DSP10^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>DAYS SUPPLY field (#4)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>DAYS SUPPLY field (#8)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>DAYS SUPPLY field (#1.1)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>QTY field (#.041)</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>DSP11 - Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in DSP09, if required by the PDMP.</p>
<p>Appendix B in ASAP version 5.0 Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$DSP11^PSOASAP()</td>
<td><p>Retrieved from the NCPDP DISPENSE UNIT field (#50,82) of the DRUG file.</p>
<p>Coded data:</p>
<p>01-EA</p>
<p>02-ML</p>
<p>03-GM</p>
<p>BLANK</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP12 - Transmission Form of Rx Origin Code</td>
<td><p>Code indicating how the pharmacy received the prescription, if required by the PDMP.</p>
<p>01 Written Prescription</p>
<p>02 Telephone Prescription</p>
<p>03 Telephone Emergency Prescription</p>
<p>04 Fax Prescription</p>
<p>05 Electronic Prescription</p>
<p>06 Transferred/Forwarded Rx</p>
<p>07 Order (Administered at Prescriber Location)</p>
<p>08 Dispensed from a Prescriber Location</p>
<p>09 Standing Order/Protocol</p>
<p>99 Other</p></td>
<td>$$DSP12^PSOASAP()</td>
<td><p>The ORDER ENTRY/RESULTS REPORTING API $$NATURE^ORUTL3 provides the Nature of Order, which is translated the following way:</p>
<p>01 W</p>
<p>02 V or T</p>
<p>05 E</p>
<p>99 Other</p>
<p>ICR# 5890</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP13 - Partial Fill Indicator</td>
<td><p>This field is used when the quantity in DSP09 is less than the metric quantity per dispensing authorized by the prescriber. This dispensing activity is often referred to as a split filling.</p>
<p>00 Not a Partial Fill</p>
<p>01 First Partial Fill</p>
<ol start="85">
<li><p>For additional fills per prescription, increment by 1. The second partial fill would be reported as 02, up to a maximum of 99.</p></li>
</ol></td>
<td>$$DSP13^PSOASAP()</td>
<td><p>Codes indicating partial or non-partial fill:</p>
<p>00 Non-Partial Fill</p>
<p>01 Partial 1</p>
<p>02 Partial 2</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP14 - Pharmacist National Provider Identifier (NPI)</td>
<td>Identifier assigned to the pharmacist by CMS. This number can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP14^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill pharmacist.</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP15 - Pharmacist State License Number</td>
<td>Assigned to the pharmacist by the State Licensing Board. This data element can be used to identify the pharmacist dispensing the medication.</td>
<td>$$DSP15^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP16 - Classification Code for Payment Type</td>
<td><p>Code identifying the type of payment, i.e. how it was paid for, if required by the PDMP.</p>
<p>01 Private Pay (Cash, Charge, Credit Card)</p>
<p>02 Medicaid</p>
<p>03 Medicare</p>
<p>04 Commercial Insurance</p>
<p>05 Military Installations and VA</p>
<p>06 Workers’ Compensation</p>
<p>07 Indian Nations</p>
<p>99 Other</p></td>
<td>$$DSP16^PSOASAP()</td>
<td>VistA sends '05'</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP17 - Date Sold</td>
<td><p>This field is used to determine the date the prescription was dispensed (sold to, picked up by, or otherwise left the pharmacy), not the date it was prepared.</p>
<p>This date could be captured from the point-of-sale (POS) system, if the pharmacy has a POS system, and there is a bidirectional flow with the pharmacy management system in order to capture and report this date. Or it could be captured and reported from a will-call management system, integrated with the pharmacy management system.</p></td>
<td>$$DSP17^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order via $$DSP05^PSOASAP():</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>RELEASED DATE/TIME field (#21)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>RELEASED DATE/TIME field (#31)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>RELEASED DATE/TIME field (#17)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>RELEASED DATE/TIME (#8)</p></td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP18 - RxNorm Product Qualifier</td>
<td><p>01 Semantic Clinical Drug (SCD)</p>
<p>02 Semantic Branded Drug (SBD)</p>
<p>03 Generic Package (GPCK)</p>
<p>04 Branded Package (BPCK)</p>
<p>RxNorm code that is populated in the DRU-010-09 field in the SCRIPT transaction.</p>
<ol start="86">
<li><p>DSP18 and DSP19 are placeholder fields pending RxNorm becoming an industry standard. These fields should not be required until such time.</p></li>
</ol></td>
<td>$$DSP18^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP19 - RxNorm Code</td>
<td>Used for electronic prescriptions to capture the prescribed drug product identification, if required by the PDMP.</td>
<td>$$DSP19^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP20 - Electronic Prescription Reference Number</td>
<td>This field should be populated with the appropriate field in the SCRIPT transaction.</td>
<td>$$DSP20^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP21 - Electronic Prescription Order Number</td>
<td><p>This field will be populated with appropriate field in the SCRIPT standard.</p>
<ol start="87">
<li><p>DSP20 and DSP21 should be reported as a pair to the PDMP and the PDMP will decide which one, if not both, it decides to capture. By requiring the reporting of both, this avoids specification variations that would require custom programming to accommodate a PDMP. Also, the information reported by the pharmacy management system will depend on the information received at the pharmacy with an electronic prescription.</p></li>
</ol></td>
<td>$$DSP21^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP22 - Quantity Prescribed</td>
<td>This field can clarify the value reported in DSP13 Partial Fill Indicator.</td>
<td>$$DSP22^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP23 - Rx SIG</td>
<td>This field would capture the actual directions printed on the prescription vial label. If the directions exceed 200 characters, truncation would be allowed.</td>
<td>$$DSP23^PSOASAP()</td>
<td>Concatenate the SIG1 multiple (#52.04,.01) into a single string</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP24 - Opioid Treatment Type</td>
<td><p>This field is used to explain the reason for an opioid prescription. If the prescription is not for an opioid, then this field would not be used.</p>
<p>01 Not Used for Opioid Dependency Treatment</p>
<p>02 Used for Opioid Dependency Treatment</p>
<p>03 Pain Associated with Active and Aftercare Cancer Treatment</p>
<p>04 Palliative Care in Conjunction with a Serious Illness</p>
<p>05 End-of-Life and Hospice Care</p>
<p>06 A Pregnant Individual with a Pre-existing Prescription for Opioids</p>
<p>07 Acute Pain for an Individual with an Existing Opioid Prescription for Chronic Pain</p>
<p>08 Individuals Pursuing an Active Taper of Opioid Medications</p>
<p>09 Patient is Participating in a Pain Management Contract</p>
<p>10 Acute Opioid Therapy</p>
<p>11 Chronic Opioid Therapy</p>
<p>99 Other (trading partner agreed upon reason or not indicated)</p>
<p>The definitions of Codes 03 to 11 can only be reported if required by the state to be provided by the prescriber on the prescription order.</p></td>
<td>$$DSP24^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP25 - Diagnosis Code</td>
<td>This field is used to report the ICD-10 code. If required by a PDMP, this field would be populated only when the ICD-10 code is included with the prescription. Exclude the decimal point.</td>
<td>$$DSP25^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP26 - Time Written</td>
<td>Time expressed in 24-hour clock time HMMSS or HHMM). Time range: 000000 through 235959. The time zone should be reported in Coordinated Universal Time (UTC) as HHMMSSZ (e.g., 235959Z). Do not include colons or non-numeric characters other than Z for Zulu time.</td>
<td>$$DSP26^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP27 - Time Filled</td>
<td>The time the prescription record was prepared. Time expressed in 24-hour clock time HMMSS or HHMM). Time range: 000000 through 235959. The time zone should be reported in Coordinated Universal Time (UTC) as HHMMSSZ (e.g.,235959Z). Do not include colons or non-numeric characters other than Z for Zulu time.</td>
<td>$$DSP27^PSOASAP():</td>
<td><p>Retrieves from one of the following locations in respective order:</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>RELEASED DATE/TIME field (#21)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>RELEASED DATE/TIME field (#31)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>RELEASED DATE/TIME field (#17)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>RELEASED DATE/TIME (#8)</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP28 - Time Sold</td>
<td>The time the prescription record was sold to, picked up by, or otherwise left the pharmacy for the patient. Time expressed in 24-hour clock time HMMSS or HHMM). Time range: 000000 through 235959. The time zone should be reported in Coordinated Universal Time (UTC) as HHMMSSZ (e.g., 235959Z). Do not include colons or non-numeric characters other than Z for Zulu time.</td>
<td>$$DSP28^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order via $$DSP27^PSOASAP():</p>
<p>Void</p>
<p>RETURN TO STOCK LOG subfile (#52.07)</p>
<p>RELEASED DATE/TIME field (#21)</p>
<p>Original Fill</p>
<p>PRESCRIPTION file (#52)</p>
<p>RELEASED DATE/TIME field (#31)</p>
<p>Refill</p>
<p>REFILL subfile (#52.1)</p>
<p>RELEASED DATE/TIME field (#17)</p>
<p>Partial</p>
<p>PARTIAL subfile (#52.2)</p>
<p>RELEASED DATE/TIME (#8)</p></td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>DSP29 - Total Quantity Remaining on Prescription</td>
<td><p>Identifies the unit of measure for the total quantity remaining for the prescription after the current dispense in metric decimal format. Example: 2.5.</p>
<ol start="88">
<li><p>For compounding show the first quantity in CDI04.</p></li>
</ol>
<p>ASAP version 5.0 Standard Appendix B has specific instructions.</p></td>
<td>$$DSP29^PSOASAP():</td>
<td><ol type="1">
<li><blockquote>
<p>If TITRATION RX FLAG field (#52,45.3) is YES, send zero and quit</p>
</blockquote></li>
<li><blockquote>
<p>If TITRATION RX FLAG field (#52,45.3) is NO, then send {[DSP04 minus DSP06] multiplied by DSP09} where:</p>
</blockquote></li>
</ol>
<p>DSP04 = the # OF REFILLS field (#52,9) of the PRESCRIPTION file</p>
<p>DSP06 = the fill number which will be retrieved from the AL and AM cross-references of the PRESCRIPTION file (#52) and PARTIAL DATE subfile (#52.2) respectively</p>
<p>DSP09 = the data from one of the following locations in respective order:</p>
<p>Void: RETURN TO STOCK LOG subfile (#52.07), QTY field (#3)</p>
<p>Original Fill: PRESCRIPTION file (#52),QTY field (#7)</p>
<p>Refill: REFILL subfile (#52.1), QTY field (#1)</p>
<p>Partial: PARTIAL subfile (#52.2), QTY field (#.04)</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP30 - Total Quantity Remaining Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity remaining in DSP29. ASAP version 5.0 Standard has specific instructions.</p>
<p>01 Each (used to report solid dosage units or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$DSP30^PSOASAP()</td>
<td><p>Data is retrieved from the NCPDP DISPENSE UNIT field (#50,82) of the DRUG file.</p>
<p>Coded data:</p>
<p>01-EA</p>
<p>02-ML</p>
<p>03-GM</p>
<p>BLANK""</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP31 - Discount Card</td>
<td><p>Identifies whether the type of payment occurred using a local or national discount card if the PDMP requires payment DSP16. Required if classification payment code is 01 (Private Pay) or 04 (Commercial Insurance) used in DSP16.</p>
<p>01 Yes</p>
<p>02 No</p></td>
<td>$$DSP31^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP32 - Classification Code for Additional Payment Type</td>
<td><p>Code identifying the type of payment, i.e., how it was paid for, if required by the PDMP.</p>
<p>01 Private Pay (Cash, Charge, Credit Card)</p>
<p>02 Medicaid</p>
<p>03 Medicare</p>
<p>04 Commercial Insurance</p>
<p>05 Military Installations and VA</p>
<p>06 Workers’ Compensation</p>
<p>07 Indian Nations</p>
<p>99 Other</p></td>
<td>$$DSP32^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>DSP33 - Discount Card for Additional Payment Type</td>
<td><p>Required if classification payment code is 01 (Private Pay) or 04 (Commercial Insurance) used in DSP32.</p>
<p>01 Yes</p>
<p>02 No</p></td>
<td>$$DSP33^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>DSP34 - DEA Schedule/State Designation</td>
<td><p>State or Federal control Level or other reporting designation.</p>
<p>01 Cannabis and Cannabis Extract</p>
<p>02 State or DEA Schedule 2</p>
<p>03 State or DEA Schedule 3</p>
<p>04 State or DEA Schedule 4</p>
<p>05 State or DEA Schedule 5</p>
<p>06 State Designated Other Controlled Substance or Drug of Concern</p>
<p>07 CBD</p>
<p>99 Legend or Non-controlled Substances</p></td>
<td>$$DSP34^PSOASAP()</td>
<td>Assigns a zero to first character of the value that is populated at the DEA, SPECIAL HDLG field (#50,3) of the DRUG file. (example: 04)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>DSP35 - Last Name or Initials of Pharmacist Filling the Prescription</td>
<td>Last Name or Initials of the pharmacist dispensing the medication.</td>
<td>$$DSP35^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>DSP36 - First Name of Pharmacist Filling the Prescription</td>
<td>First Name of the pharmacist dispensing the medication.</td>
<td>$$DSP36^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089137" class="anchor"></span>Table 62: Transaction Trailer (TT) 5.0

<table style="width:100%;">
<caption><p><span id="_Toc207089138" class="anchor"></span>Table 63: ASAP 4.2AZ, 4.2BZ, 5.0 Zero Reports</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PRE – Prescriber information Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the prescriber of the prescription.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>PRE01 - National Provider Identifier (NPI)</td>
<td><p>Identifier assigned to the prescriber by CMS.</p>
<ol start="89">
<li><p>If the prescriber does not have a DEA number and prescribed a noncontrolled substance that is a reportable drug to the PDMP, this field should be used as the identifier.</p></li>
</ol></td>
<td>$$PRE01^PSOASAP()</td>
<td><p>Retrieved via the Kernel API $$NPI^XUSNPI using the prescription fill provider</p>
<p>ICR# 4532</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE02 - DEA Number</td>
<td>Identifying number assigned to a prescriber or an institution by the Drug Enforcement Administration (DEA). Required when the prescription is for a DEA-defined controlled substance.</td>
<td>$$PRE02^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The first piece by "-" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA#</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) of the NEW PERSON file. The first piece by "-" is returned.</p>
<p>ICR# 2343</p>
<p>Pharmacy DEA#</p>
<p>the Kernel API $$WHAT^XUAF4 is called to return the FACILITY DEA NUMBER field (#4,52) of the INSTITUTION file.</p>
<p>ICR# 2171</p></td>
<td>Required</td>
</tr>
<tr class="even">
<td>PRE03 - DEA Number Suffix</td>
<td>Identifying number assigned to a prescriber by an institution when the institution’s DEA number is used, if required by the PDMP.</td>
<td>$$PRE03^PSOASAP()</td>
<td><p>Retrieved from one of the following locations in respective order:</p>
<p>Provider DEA# suffix associated with the CPRS order</p>
<p>The ORDER ENTRY/RESULTS REPORTING procedure ARCHIVE^ORDEA retrieves the value at the DEA # field (#101.52,10) of the ORDER DEA ARCHIVE INFO file. The 2nd piece by “-" is returned.</p>
<p>ICR# 5709</p>
<p>Prescription fill provider or facility DEA# suffix</p>
<p>The Kernel API $$DEA^XUSER retrieves the value at the DEA NUMBER field (#200.5321,.01) from the NEW DEA #'S multiple of the NEW PERSON file. The 2nd piece by “-" is returned.</p>
<p>ICR# 2343</p>
<p>VA#</p>
<p>If DEA# from PHA03 is equal to the DEA# from PHA02, then The Kernel API $$DEA^XUSER retrieves the value at the VA# field (#200,53.3) of the NEW PERSON file.</p>
<p>ICR# 2171</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE04 - Prescriber License Number</td>
<td>Identification assigned to the prescriber by the Licensing Board of a state or jurisdiction. This field can be used for veterinarian prescriptions. Used if required by the PDMP.</td>
<td>$$PRE04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE05 - Last Name</td>
<td>Prescriber's last name. Used if required by the PDMP.</td>
<td>$$PRE05^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE06 - First Name</td>
<td>Prescriber's first name. Used if required by the PDMP.</td>
<td>$$PRE06^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE07 - Middle Name</td>
<td>Prescriber's middle name or initial. Used if required and is available in the pharmacy system.</td>
<td>$$PRE07^PSOASAP()</td>
<td><p>NAME field (#200,.01) from the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE08 - Phone Number</td>
<td>The prescriber's primary phone number.</td>
<td>$$PRE08^PSOASAP()</td>
<td><p>Retrieved from the PHONE NUMBER # field (#200,.132) of the NEW PERSON file.</p>
<p>ICR# 10061</p></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE09 - XDEA Number</td>
<td>This field has been decommissioned since DEA no longer issues XDEA numbers. This field is not to be used.</td>
<td>$$PRE09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>PRE10 - Jurisdiction or State of Issuing Prescriber License Number</td>
<td>This field can be used to further identify the information in PRE04, depending on the PDMP’s need for this information.</td>
<td>$$PRE10^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE11 - Prescriber Address Information – 1</td>
<td><p>Freetext for address information.</p>
<p>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Address.</p></td>
<td>PRE11^PSOASAP1()</td>
<td><ol type="1">
<li><p>Retrieve the PLACER ORDER NUMBER pointer at (#52, 39.3) using the available RX# IEN</p></li>
<li><p>Get the DEA# (#101.52,10) from the ORDER DEA ARCHIVE INFO file using PLACER ORDER NUMBER IEN</p></li>
<li><p>Get the STREET ADDRESS 1 (#8991.9,1.3) from the DEA NUMBERS file using the DEA#</p></li>
<li><p>If the address isn't populated at STREET ADDRESS 1 (#8991.9, 1.3) then retrieve the address from the ORDER DEA ARCHIVE INFO file (#101.52, 13)</p></li>
</ol></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE12 - Prescriber Address Information – 2</td>
<td>Freetext for additional address information. Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</td>
<td>PRE12^PSOASAP1()</td>
<td><ol type="1">
<li><p>Retrieve the PLACER ORDER NUMBER pointer at (#52, 39.3) using the available RX# IEN</p></li>
<li><p>Get the DEA# (#101.52,10) from the ORDER DEA ARCHIVE INFO file using PLACER ORDER NUMBER IEN</p></li>
<li><p>Get the STREET ADDRESS 2 (#8991.9,1.4) from the DEA NUMBERS file using the DEA#</p></li>
<li><p>If the address isn't populated at STREET ADDRESS 1 (#8991.9, 1.4) then retrieve the address from the ORDER DEA ARCHIVE INFO file (#101.52, 14)</p></li>
</ol></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE13 - Prescriber City Address</td>
<td>Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>PRE13^PSOASAP1()</td>
<td><ol type="1">
<li><p>Retrieve the PLACER ORDER NUMBER pointer at (#52, 39.3) using the available RX# IEN</p></li>
<li><p>Get the DEA# (#101.52,10) from the ORDER DEA ARCHIVE INFO file using PLACER ORDER NUMBER IEN</p></li>
<li><p>Get the CITY (#8991.9,1.5) from the DEA NUMBERS file using the DEA#</p></li>
<li><p>If there is no data at (#8991.9, 1.5) then retrieve the address data from the ORDER DEA ARCHIVE INFO file (#101.52, 16)</p></li>
</ol></td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>PRE14 - Prescriber State Address</td>
<td>Two-letter jurisdiction/state and possession abbreviation as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>PRE14^PSOASAP1()</td>
<td><ol type="1">
<li><p>Retrieve the PLACER ORDER NUMBER pointer at (#52, 39.3) using the available RX# IEN</p></li>
<li><p>Get the DEA# (#101.52,10) from the ORDER DEA ARCHIVE INFO file using PLACER ORDER NUMBER IEN</p></li>
<li><p>Get the STATE (#8991.9,1.6) from the DEA NUMBERS file using the DEA#</p></li>
<li><p>If the address isn't populated at (#8991.9, 1.6) then retrieve the address data from the ORDER DEA ARCHIVE INFO file (#101.52, 17)</p></li>
</ol></td>
<td>Optional</td>
</tr>
<tr class="even">
<td>PRE15 - Zip Code Address</td>
<td>United States Postal Service ZIP Code or ZIP+4 as described in United States Postal Service Publication 28 Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses. Do not include white spaces or special characters. Include hyphens in ZIP+4.</td>
<td>PRE15^PSOASAP1()</td>
<td><ol type="1">
<li><p>Retrieve the PLACER ORDER NUMBER pointer at (#52, 39.3) using the available RX# IEN</p></li>
<li><p>Get the DEA# (#101.52,10) from the ORDER DEA ARCHIVE INFO file using PLACER ORDER NUMBER IEN</p></li>
<li><p>Get the ZIP CODE (#8991.9,1.7) from the DEA NUMBERS file using the DEA#</p></li>
<li><p>If the address data isn't populated at (#8991.9, 1.7) then retrieve the address data from the ORDER DEA ARCHIVE INFO file (#101.52, 17.5)</p></li>
</ol></td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089138" class="anchor"></span>Table 63: ASAP 4.2AZ, 4.2BZ, 5.0 Zero Reports

<table>
<caption><p><span id="_Toc207089139" class="anchor"></span>Table 64: Segment</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 32%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CDI – Compound Drug Ingredient Detail Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the individual ingredients that make up a compound.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Not Used</strong></p></td>
</tr>
<tr class="even">
<td>CDI01 - Compound Drug Ingredient Sequence Number</td>
<td>The first reportable ingredient is 1. Each additional reportable ingredient is incremented by 1.</td>
<td>$$CDI01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI02 - Product ID Qualifier</td>
<td><p>Code to identify the type of product ID contained in CDI03.</p>
<p>01 NDC</p>
<p>02 UPC</p>
<p>03 HRI</p>
<p>04 UPN</p>
<p>05 DIN</p>
<p>06 CPD (This code is not used in this segment.)</p></td>
<td>$$CDI02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI03 - Product ID</td>
<td><p>Full product identification as indicated in CDI02, including leading zeros without punctuation.</p>
<p>If DSP07 = 01, then DSP08 should contain the 11-digit NDC code without hyphens.</p>
<p>If the product is a compound, use 99999 as the first five characters of the product code. The remaining six characters are assigned by the pharmacy. The CDI then becomes a required segment.</p></td>
<td>$$CDI03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>CDI04 - Component Ingredient Quantity</td>
<td><p>Metric decimal quantity of the ingredient identified in CDI03.</p>
<p>Example: 2.5. Appendix B in ASAP version 5.0 Standard contains specific instructions.</p></td>
<td>$$CDI04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>CDI05 - Compound Drug Dosage Units Code</td>
<td><p>Identifies the unit of measure for the quantity dispensed in CDI04, if required by the prescription-monitoring program.</p>
<p>Appendix B in ASAP version 5.0 Standard contains specific instructions.</p>
<p>01 Each (used to report solid dosage units or indivisible package)</p>
<p>02 Milliliters (ml) (for liters adjust to the decimal milliliter equivalent)</p>
<p>03 Grams (gm) (for milligrams adjust to the decimal gram equivalent)</p></td>
<td>$$CDI05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>CDI06 - DEA Schedule/State Designation of Each Ingredient</td>
<td><p>01 Cannabis and Cannabis Extract</p>
<p>02 State or DEA Schedule 2</p>
<p>03 State or DEA Schedule 3</p>
<p>04 State or DEA Schedule 4</p>
<p>05 State or DEA Schedule 5</p>
<p>06 State Designated Other Controlled Substance or Drug of Concern</p>
<p>07 CBD</p>
<p>99 Legend or Non-Controlled Substances</p></td>
<td>$$CDI06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Toc207089139" class="anchor"></span>Table 64: Segment

<table>
<caption><p><span id="_Ref161303409" class="anchor"></span>Table 65: Segment</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AIR – Additional Information Reporting Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To report a prescription blank serial number and information on person picking up or dropping off the prescription, if other than the patient. Note: If this segment is used, at least one of the data elements (fields) will be required.</strong></p>
<p><strong>Level: Detail</strong></p>
<p><strong>Requirement: Optional</strong></p></td>
</tr>
<tr class="even">
<td>AIR01 - Jurisdiction Issuing Rx Serial Number</td>
<td><p>U.S.P.S. code of jurisdiction that issued serialized prescription blank. This is required if AIR02 is used.</p>
<p>ASAP version 5.0 Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR01^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR02 - Jurisdiction Issued Rx Serial Number</td>
<td>Number assigned to state issued serialized prescription blank.</td>
<td>$$AIR02^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR03 - Jurisdiction Issuing ID of Person Picking Up Rx</td>
<td><p>Code identifying the jurisdiction that assigned the ID for the person picking up in AIR05.</p>
<p>ASAP version 5.0 Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR03^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR04 - ID Qualifier of Person Picking Up Rx</td>
<td><p>Code to identify the type of ID in AIR05. If AIR03 is used, AIR04 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Bamboo Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>11 Medicaid Recipient ID Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$AIR04^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR05 - ID of Person Picking Up Rx</td>
<td><p>Identification number for the person picking up the prescription as indicated in AIR 04.</p>
<p>An example would be the driver’s license number.</p>
<ol start="90">
<li><p>This field can only be populated with code 10 when provided on the prescription.</p></li>
</ol></td>
<td>$$AIR05^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR06 - Relationship of Person Picking Up Rx</td>
<td><p>Code indicating the relationship of the person picking up Rx to the patient, if required by the PDMP.</p>
<ol start="91">
<li><p>Code 01 is now Parent / Legal Guardian, not Patient.</p></li>
</ol>
<p>01 Parent/Legal Guardian</p>
<p>02 Spouse</p>
<p>03 Caregiver</p>
<p>99 Other</p></td>
<td>$$AIR06^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR07 - Last Name of Person Picking Up Rx</td>
<td>Person picking up last name. An apostrophe or period are acceptable characters to include.</td>
<td>$$AIR07^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>AIR08 - First Name of Person Picking Up Rx</td>
<td>Person picking up first name. An apostrophe or period are acceptable characters to include.</td>
<td>$$AIR08^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Required</td>
</tr>
<tr class="even">
<td>AIR09 - Last Name or Initials of Pharmacist</td>
<td>Field Decommissioned and Moved to DSP Segment.</td>
<td>$$AIR09^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>AIR10 - First Name of Pharmacist</td>
<td>Field Decommissioned and Moved to DSP Segment.</td>
<td>$$AIR10^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="even">
<td>AIR11 - Dropping Off/Picking Up Identifier Qualifier</td>
<td>(Field Decommissioned: Picking Up and Dropping Off now being handled separately.)</td>
<td>$$AIR11^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Not Used</td>
</tr>
<tr class="odd">
<td>AIR12 - Date of Birth of Person Picking Rx</td>
<td>Date person was born. Format: CCYYMMDD.</td>
<td>$$AIR12^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR13 - Address Information - 1 of Person Picking Up Rx</td>
<td>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</td>
<td>$$AIR13^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR14 - Address Information - 2 of Person Picking Up Rx</td>
<td>Recommendation: Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specifications for Patient Addresses.</td>
<td>$$AIR14^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR15 - Person Picking Up City Address</td>
<td>Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR15^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR16 - Person Picking Up State Address</td>
<td>Jurisdiction/state and possession abbreviation as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR16^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR17 - Person Picking Up Zip Code Address</td>
<td>United States Postal Service ZIP Code or ZIP+4 as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses. Do not include white spaces or special characters. Include hyphens in ZIP+4.</td>
<td>$$AIR17^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR18 - Phone Number of Person Picking Up Rx</td>
<td>Complete 10-digit phone number. Do not include hyphens or other special characters.</td>
<td>$$AIR18^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR19 - Picking Up Method of Delivery</td>
<td><p>01 Person Picked Up</p>
<p>02 Mailed/Shipped</p></td>
<td>$$AIR19^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR20 - Jurisdiction Issuing ID of Person Dropping Off Rx</td>
<td><p>Code identifying the jurisdiction that issues the ID contained in AIR22. Used if required by the PDMP.</p>
<p>ASAP version 5.0 Standard Appendix A lists jurisdictions.</p></td>
<td>$$AIR20^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR21 - ID Qualifier of Person Dropping Off Rx</td>
<td><p>Code to identify the type of ID in AIR22. If AIR20 is used, AIR21 is required.</p>
<p>01 Military ID</p>
<p>02 State Issued ID</p>
<p>03 Unique System ID</p>
<p>04 Permanent Resident Card (Green Card)</p>
<p>05 Passport ID</p>
<p>06 Driver’s License ID</p>
<p>07 Social Security Number</p>
<p>08 Tribal ID</p>
<p>09 Vendor Specific (such as Bamboo Health, Experian, LexisNexis)</p>
<p>10 Veterinary Patient Microchip Number</p>
<p>11 Medicaid Recipient ID Number</p>
<p>99 Other (Trading partner agreed upon ID, such as cardholder ID.)</p></td>
<td>$$AIR21^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR22 - ID of Person Dropping Off Rx</td>
<td><p>Identification number for the person dropping off the prescription as indicated in AIR 21.</p>
<p>An example would be the driver’s license number.</p>
<ol start="92">
<li><p>This field can only be populated with code 10 when provided on the prescription.</p></li>
</ol></td>
<td>$$AIR22^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR23 - Relationship of Person Dropping Off Rx</td>
<td><p>Code indicating the relationship of the person dropping off Rx to the patient, if required by the PDMP.</p>
<ol start="93">
<li><p>Code 01 is now Parent / Legal Guardian, not Patient.</p></li>
</ol>
<p>01 Parent/Legal Guardian</p>
<p>02 Spouse</p>
<p>03 Caregiver</p>
<p>04 Other</p></td>
<td>$$AIR23^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR24 - Last Name of Person Dropping Off Rx</td>
<td>Last name of the person dropping off Rx, if required by the PDMP.</td>
<td>$$AIR24^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR25 First Name of Person Dropping Off Rx</td>
<td>First name of the person dropping off Rx, if required by the PDMP.</td>
<td>$$AIR25^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR26 - Date of Birth of Person Dropping Off Rx</td>
<td>Date of birth of the person dropping off Rx the prescription as listed on a government-issued identification.</td>
<td>$$AIR26^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR27 - Address Information - 1 of Person Dropping Off Rx</td>
<td>Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR27^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR28 - Address Information - 2 of Person Dropping Off Rx</td>
<td>Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR28^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR29 - Person Dropping Off City Address</td>
<td>Information should be reported according to United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR29^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR30 - Person Dropping Off State Address</td>
<td>Jurisdiction/state and possession abbreviation as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses.</td>
<td>$$AIR30^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="even">
<td>AIR31 - Person Dropping Off ZIP Code Address</td>
<td>United States Postal Service ZIP Code or ZIP+4 as described in United States Postal Service Publication 28-Postal Addressing Standards or the most recently published version of the ONC Project US@ Technical Specification for Patient Addresses. Do not include white spaces or special characters. Include hyphens in ZIP+4.</td>
<td>$$AIR31^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
<tr class="odd">
<td>AIR32 - Phone Number of Person Dropping Off Rx</td>
<td>Complete 10-digit phone number. Do not include hyphens or other special characters.</td>
<td>$$AIR32^PSOASAP()</td>
<td>VistA sends "" (null)</td>
<td>Optional</td>
</tr>
</tbody>
</table>

<span id="_Ref161303409" class="anchor"></span>Table 65: Segment

<table>
<caption><p><span id="_Toc207089141" class="anchor"></span>Table 66: Segment</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 15%" />
<col style="width: 27%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>TP – Pharmacy Trailer Segment</strong></td>
<td colspan="4"><p><strong>Purpose: To identify the end of data for the entity submitting data and provide the count of the total number of detail segments, including the pharmacy header (PHA) and the pharmacy trailer (TP) segments.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TP01 - Detail Segment Count</td>
<td>Number of detail segments included for the pharmacy including the pharmacy header (PHA) including the pharmacy trailer (TP) segments.</td>
<td>$$TP01^PSOASAP()</td>
<td>Calculates the number of detail segments included (PAT, DSP, PRE, CDI, AIR) in addition to the pharmacy header (PHA) and pharmacy trailer (TP)</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089141" class="anchor"></span>Table 66: Segment

<table>
<caption><p><span id="_Toc207089142" class="anchor"></span>Table 67: Segment</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 45%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Data Element</strong></th>
<th><strong>Name Description</strong></th>
<th><strong>Data Source</strong></th>
<th><strong>Data Source Notes</strong></th>
<th><strong>Requirement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>TT – Transaction Trailer Segment</strong></td>
<td colspan="3"><p><strong>Purpose: To indicate the end of the transaction and provide the count of the total number of segments included in the transaction.</strong></p>
<p><strong>Level: Summary</strong></p>
<p><strong>Requirement: Required</strong></p></td>
</tr>
<tr class="even">
<td>TT01 - Transaction Control Number</td>
<td>Identifying control number that must be unique. Assigned by the originator of the transaction. Must match the number in TH02.</td>
<td>$$TT01^PSOASAP()</td>
<td>VA site number (via Registration API $$SITE^VASITE()) and BATCH NUMBER field (#58.42,.01) of the SPMP EXPORT BATCH file. (ex: 500-182)</td>
<td>Required</td>
</tr>
<tr class="odd">
<td>TT02 - Segment Count</td>
<td>Total number of segments included in the transaction including the header and trailer segments.</td>
<td>$$TT02^PSOASAP()</td>
<td>Calculated for each transmission.</td>
<td>Required</td>
</tr>
</tbody>
</table>

<span id="_Toc207089142" class="anchor"></span>Table 67: Segment

#### Zero Report Implementation for ASAP Standard versions 4.2A, 4.2B, 5.0

<table>
<caption><p><span id="_Toc173231222" class="anchor"></span>Table 68: Error Messages Returned by the PSO EPCS PSDRPH FILER RPC</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Segment / Element</strong></th>
<th><strong>Requirement</strong></th>
<th colspan="2"><strong>Value or Example if different from regular transmissions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><strong>TH: Transaction Header (Required)</strong></td>
</tr>
<tr class="even">
<td>TH01 – TH09</td>
<td>Variable*</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>IS: Information Source (Required)</strong></td>
</tr>
<tr class="even">
<td>IS01 – IS02</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>IS03</td>
<td>Optional</td>
<td colspan="2"><p>#20230205#-#220230228#</p>
<p>For Zero Reporting this element represents the Date Range of Report.</p></td>
</tr>
<tr class="even">
<td colspan="4"><strong>PHA: Pharmacy Header (Required)</strong></td>
</tr>
<tr class="odd">
<td>PHA01</td>
<td>Optional</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>PHA02</td>
<td>Not Used</td>
<td colspan="2">Null is sent by default because element is set to Not Used.  If changed to Required or Optional, the output generates from $$PHA02^PSOASAP().</td>
</tr>
<tr class="odd">
<td>PHA03</td>
<td>Optional</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><strong>PAT: Patient Information (Required)</strong></td>
</tr>
<tr class="odd">
<td>PAT01 – PAT06</td>
<td>Optional</td>
<td colspan="2">“”</td>
</tr>
<tr class="even">
<td>PAT07</td>
<td>Required</td>
<td colspan="2">REPORT</td>
</tr>
<tr class="odd">
<td>PAT08</td>
<td>Required</td>
<td colspan="2">ZERO</td>
</tr>
<tr class="even">
<td>PAT09 – PAT23</td>
<td>Variable*</td>
<td colspan="2"><p>“”</p>
<ol start="94">
<li><p>4.2AZ <strong>have</strong> the data elements up to and including PAT19.</p></li>
</ol>
<p>4.2BZ and 5.0z have the data elements up to and including PAT23.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>DSP: Dispensing Record (Required)</strong></td>
</tr>
<tr class="even">
<td>DSP01 – DSP04</td>
<td>Required</td>
<td colspan="2">“”</td>
</tr>
<tr class="odd">
<td>DSP05 – Date Filled</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>DSP06 – DSP25</td>
<td>Variable*</td>
<td colspan="2"><p>“”</p>
<ol start="95">
<li><p>4.2AZ <strong>have</strong> the data elements up to and including DSP17.</p></li>
</ol>
<p>4.2BZ and 5.0Z have the data elements up to and including DSP25.</p></td>
</tr>
<tr class="odd">
<td colspan="4"><strong>PRE: Prescriber Information (Required)</strong></td>
</tr>
<tr class="even">
<td>PRE01</td>
<td>Optional</td>
<td colspan="2">“”</td>
</tr>
<tr class="odd">
<td>PRE02</td>
<td>Required</td>
<td colspan="2">“”</td>
</tr>
<tr class="even">
<td colspan="4"><strong>CDI: Compound Drug Ingredient Detail (Required)</strong></td>
</tr>
<tr class="odd">
<td>CDI01 - CDI04</td>
<td>Required</td>
<td colspan="2">“”</td>
</tr>
<tr class="even">
<td colspan="4"><strong>AIR: Additional Information Reporting (Required)</strong></td>
</tr>
<tr class="odd">
<td>AIR01 - AIR02</td>
<td colspan="2">Optional</td>
<td>“”</td>
</tr>
<tr class="even">
<td colspan="4"><strong>TP: Pharmacy Trailer (Required)</strong></td>
</tr>
<tr class="odd">
<td>TP01</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><strong>TT: Transaction Trailer (Required)</strong></td>
</tr>
<tr class="odd">
<td>TT01 – TT02</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<span id="_Toc173231222" class="anchor"></span>Table 68: Error Messages Returned by the PSO EPCS PSDRPH FILER RPC

\*Variable denotes a mix of Required, Optional and Not used.

Sample Zero Report

> TH\*4.2B\*133-2961\*01\*\*20250501\*133200\*T\*\*\~~

> IS\*VA133\*PHARMACY NAME\*#20250501#-#20250501#~

> PHA\*1234567890\*\*ZZ1234567~

> PAT\*\*\*\*\*\*\*REPORT\*ZERO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*~

> DSP\*\*\*\*\*20250501\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*~

> PRE\*\*~

> CDI\*\*\*\*~

> AIR\*\*~

> TP\*7~

> TT\*133-2961\*10~

## Appendix F: OneVA Pharmacy HL7 Messaging using Middleware Application for External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OneVA Pharmacy General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall OneVA Pharmacy software design has several components; they are:

1.  Veterans Health Information Systems and Technology Architecture (VistA)
2.  Health Level 7 (HL7) Messaging
3.  National HL7 Health Connect (an Intersystems HealthShare service).
4.  Veterans Data Information Exchange (VDIF)

    Patch PSO\*7\*497 fixed the following OneVA Pharmacy critical defects:
1.  To fix the auto-suspend defect.
5.  To limit refill permissions to only those personnel who have the correct key(s).
6.  "Trade Name" prevented from being refilled/partial filled by a remote OneVA pharmacy location so that dispensing errors are reduced on prescriptions due to the lack of information.
7.  To identify titration prescriptions at the host site and to disallow refills of such titration prescriptions at the dispensing site.
8.  Update OneVA Pharmacy functionality to add menu item for turning OFF/ON Switch for OneVA Pharmacy ADPACs

VistA is the user interface where a pharmacist uses the “Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]” menu (found within the VistA Pharmacy Outpatient Pharmacy Manager package) to query for and refill patient’s active and refillable prescriptions from other VA Pharmacy VistA instances. The OneVA Pharmacy uses Health Level 7 (HL7) messaging to query and receive remote prescription details to and from VDIF.

The VistA instance the Veteran is refilling the prescription is considered the ‘dispensing’ VistA instance. This patch allows a pharmacist from a ‘dispensing’ VistA instance to refill a prescription that originated from another VA Pharmacy VistA instance and print a prescription label at the dispensing site. The VA Pharmacy VistA instance where the prescription originated and currently exits is the ‘host’ VistA instance. The host VistA instance is where the update to the prescription record is made after the fill is processed and the host label file is being extracted to return to the dispensing site via HL7.

The OneVA Pharmacy software sends an HL7 message to VDIF National Health Connect to an existing TCP Service to request patient medications.

96. The OneVA HL7 Listener Service is using an existing connection that all 130+ VistAs have with the National HL7 Health Connect.

The medications return to the dispensing site via HL7 messaging. Once the prescription reaches the dispensing site, they display below any 'local' prescriptions on the ‘Medication Profile’ screen. The prescriptions displayed to the Pharmacist by VA Pharmacy site. The dispensing Pharmacist can then view the ‘remote’ prescriptions and select one to refill or partially fill.

For label printing, VistA triggers the HL7 message stream that executes during the full or partial refill prescription processes. The event triggers the handling of the printing of the host label information at the dispensing printing device.

Using existing functionality detailed above, patch PSO\*7\*774 introduces the following enhancements:

1.  Prescriptions originating on the ‘host’ VistA instance which have been PARKED are designated as “AP” or “ACT/PK” (Active/Parked) on the ‘dispensing’ VistA instance’s ‘Medication Profile’ screen and upon selection of one of these prescriptions.
2.  For prescriptions originating on the ‘host’ VistA instance which have no original fill (e.g. PARKED prescriptions), an original fill will be done and the label printed on the ‘dispensing’ VistA instance as with refills.
3.  Original fills, refills, and partial fills PARKED on the ‘host’ VistA instance will be UNPARKED there as a result of fill requests on the ‘dispensing’ VistA instance.
4.  Original fills, refills, and partial fills going through OPAI automated dispensing device (ADD) on the ‘dispensing’ VistA instance will be auto-released on the ‘host’ VistA instance. Furthermore, if an original fill or refill is being auto-released, then ECME and copay transaction will be triggered, where applicable.

### OneVA Pharmacy New Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new option has been created to allow reporting regarding what 'remote' prescriptions have been filled by a particular facility, and what facilities have (re)filled prescriptions that belong to a target facility. This menu is OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT\].

### OneVA Pharmacy New Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new HL7 logical link, PSORRXSEND will facilitate the sending of the HL7 messages to middleware. The PSO VISTA PHARM and PSO EMI PHARM application parameters will control the message processing within VistA. The existing multi-threaded listener will be leveraged at each facility for receiving the HL7 messages into VistA.

### OneVA Pharmacy New Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/005.png)</th>
<th><p><strong>*Important*</strong></p>
<p>DO NOT turn on the OneVA Pharmacy Flag until directed to do so. The software will be released, deployed, and installed with the activation flag set to the “off” position. The Existing Product Intake Program (EPIP) Implementation Team will coordinate with the sites Pharmacy Automatic Data Processing Application Coordinator (ADPAC) on the specific date in which to activate the software.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To use OneVA Pharmacy, the user turns on the ‘ONEVA PHARMACY FLAG (#101)’. The 'ONEVA PHARMACY FLAG (#101)’ is located on the ‘PHARMACY SYSTEM FILE (#59.7)’ This field will allow sites to toggle the OneVA Pharmacy logic 'on' or 'off' depending on current needs. The user changes the field by using option, PSS SYS EDIT and editing the 'ONEVA PHARMACY FLAG (#101)’ field.

The patch PSS\*1\*212 delivers the ‘ONEVA PHARMACY FLAG (#101)’ in the 'off' state. When this flag is in the 'off' state, the VDIF National Health Connect is not queried for external prescriptions and other VistA instances will not be able to (re)fill prescriptions that belong to the VistA instance with the flag set to the 'off' state. When in the 'on' state, all prescription queries and actions may be taken for remote queries, original fills, refills, and partial fills. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘ONEVA PHARMACY FLAG (#101)’ set to the 'on' state.

To turn on the ‘ONEVA PHARMACY FLAG (#101)’

Select OPTION NAME: PSS SYS EDIT Pharmacy System Parameters Edit

Pharmacy System Parameters Edit

PMIS PRINTER: PP8//

PMIS LANGUAGE: English//

WARNING LABEL SOURCE: NEW//

CMOP WARNING LABEL SOURCE: NEW//

OPAI WARNING LABEL SOURCE: NEW//

AUTOMATE CPRS REFILL:

ONEVA PHARMACY FLAG: ON//

### OneVA Pharmacy Modified Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*497 modifies the following protocols to the PROTOCOL file (#101) to remediate critical defects found in PSO\*7\*454. They are:

1.  PSO LM REFILL REMOTE ORDER (Modified)
9.  PSO LM REMOTE ORDER MENU (Modified)
10. PSO LM REMOTE PARTIAL (Modified)

    Also, with the introduction of Patch PSO\*7\*774, the SCREEN field of Protocol PSO LM REMOTE PARTIAL was changed to call into PSORPH2 Tag of PSORRX2 Routine so that it could screen not to allow partial fills for remote mediations which are both Parked and never been filled.

### OneVA Pharmacy New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*454 adds new protocols to the PROTOCOL file (#101) to facilitate the OneVA Pharmacy messaging. They are:

1.  PSO LM MEDICATION PROFILE (Modified)
2.  PSO LM REFILL REMOTE ORDER (New)
3.  PSO LM REMOTE ORDER MENU (New)
4.  PSO LM REMOTE ORDER SELECTION (New)
5.  PSO LM REMOTE PARTIAL (New)
6.  PSO LM REMOTE REPORT DETAILS (New)
7.  PSO LM REMOTE RX REPORT (New)
8.  PSO LM REMOTE RX REPORT MENU (New)
9.  PSO LM SELECT REPORT ITEM (New)
10. PSO REMOTE RX QBP Q13 ESUBS (New)
11. PSO REMOTE RX QBP Q13 EVENT (New)
12. PSO REMOTE RX RDS O13 ESUBS (New)
13. PSO REMOTE RX RDS O13 EVENT (New)

### OneVA Pharmacy New Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*454 adds two new HL7 application parameters to the HL7 APPLICATION PARAMETER file (#771). They are:

PSO EMI PHARM

PSO VISTA PHARM

### New Fields on Existing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*454 adds new fields to the PRESCRIPTION (#52) REFILL file (#52.1). They are:

REMOTE FILL SITE (#52.1,91)

REMOTE PHARMACMIST (#52.1,92)

REMOTE PHARMACIST PHONE (#52.1,93)

Patch PSO\*7\*454 adds new fields to the PRESCRIPTION (#52) PARTIAL DATE file (#52.2). They are:

REMOTE FILL SITE (#52.2,91)

REMOTE PHARMACMIST (#52.2,92)

REMOTE PHARMACIST PHONE (#52.2,93)

Patch PSO\*7\*454 adds the new ONEVA PHARMACY FLAG field (#3001) to the OUTPATIENT SITE (#59) file).

Patch PSO\*7\*774 adds new fields to the PRESCRIPTION (#52) top-file level. They are:

REMOTE FILL SITE (#52,91)

REMOTE PHARMACMIST (#52,92)

REMOTE PHARMACIST PHONE (#52,93)

REMOTE FILLING PERSON (#52,96)

REMOTE CHECKING PHARMACIST (#52,97)

### OneVA Pharmacy New File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Remote Prescription Log File (#52.09) logs all activity related to OneVA Pharmacy ‘remote refills’ and ‘partial fills’. The log file will record all actions taken by the local or dispensing site as well as all actions taken by any external facility for any remote or host prescription. The log is input into the OneVA Pharmacy reports found on the OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT\] menu.

REMOTE PRESCRIPTION LOG file (#52.09)

PATIENT (.02)

RX NUMBER (.03)

SITE NUMBER (.04)

REQUEST TYPE (.05)

OUTGOING REQUEST PHARMACIST (.06)

REMOTE FILLING PHARMACIST (.061)

QUANTITY (.07)

DAYS SUPPLY (.08)

REFILL/PARTIAL DATE (.09)

DISPENSED DATE (.1)

RELEASED DATE/TIME (.16)

REMOTE DRUG NAME (1)

LOCAL (MATCHED) DRUG (1.1)

TOTAL REFILL/PARTIAL FILL COST (1.2

VA PRODUCT ID (1.3)

MESSAGE DETAILS (2)

LABEL DATA (3)

### OneVA Pharmacy Component Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 2.5.1 of the HL7 specification will be used for the message format. VDIF will accept HL7 messages on the National HL7 HealthConnect. This will use an existing HealthConnect Service that already has a connection to all 130+ VistAs.

<span id="_Toc207089144" class="anchor"></span>Figure 1: Dispensing VistA Instance to National HL7 Health Connect

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/006.png)

When the Pharmacist enters a request to display the Medication Profile screen from a dispensing VistA instance, the QBP^Q13 HL7 ‘Query By Parameter Request’ message is sent to VDIF National Health Connect to an existing TCP Service to request patient medications.

97. The OneVA HL7 Listener Service is using an existing connection that all 130+ VistAs have with the National HL7 Health Connect. The patient’s prescription data is returned to the dispensing VistA instance and displayed on the Medication Profile screen.

When a Pharmacist selects a prescription from the Medication Profile screen from a dispensing VistA instance, the RDS^O13 HL7 ‘Pharmacy/Treatment Dispense’ message is sent to a middleware application will receive the request, determine the destination facility, and then forward the message to the host VistA instance. The host VistA instance will process the message and return a response message containing the prescription label. The middleware will route the message back to the dispensing VistA, displaying the completion of the transaction to the Pharmacist on the screen.

### OneVA Pharmacy HL7 Message Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four HL7 message types created within the OneVA Pharmacy software. They are:

1.  QBP^Q13 Query by Parameter Request
11. RTB^K13 Prescription Query Service Request
12. RDS^O13 Pharmacy/Treatment Dispense Message Request
13. RRD^O14 Prescription (Re)fill/Partial Service Response

#### QBP^Q13 Query by Parameter Request

The following table defines the data elements required for each of the following segments of the QBP^Q13 Query by Parameter Request.

Message Header (MSH) segment

Query Parameter Definition (QPD) segment

Patient Identification (PID) segment

The MUMPS code is designed to use the ‘D BLDPID^PSOTPHL2(DFN,"",.PSORRDAT,.HL,.ERR)’ routine to create the Patient Identification (PID) segment.

Response Control Parameter (RCP) segment

| Segment | Piece | Description/Field Name         | Data Type |
|---------|-------|--------------------------------|-----------|
| MSH     | 1     | Field Separator                | ST        |
|         | 2     | Encoding Characters            | ST        |
|         | 3     | Sending Application            | HD        |
|         | 4     | Sending Facility               | HD        |
|         | 5     | Receiving Application          | HD        |
|         | 6     | Receiving Facility             | HD        |
|         | 7     | Date/Time of Message           | TS        |
|         | 8     | Security                       | ST        |
|         | 9     | Message Type                   | CM        |
|         | 10    | Message Control ID             | ST        |
|         | 11    | Processing ID                  | PT        |
|         | 12    | Version ID                     | ID        |
|         | 13    | Sequence Number                | NM        |
|         | 14    | Continuation Pointer           | ST        |
|         | 15    | Accept Acknowledgement         | ID        |
|         | 16    | Application Acknowledgement    | ID        |
|         | 17    | Country Code                   | ID        |
|         | 18    | Character Set                  | ID        |
|         | 19    | Principal Language of Messages | CE        |
| QDP     | 1     | Message Type                   | ST        |
|         | 2     | Message Query Name             | CE        |
|         | 3     | Query Tag                      | ST        |
|         | 4     | User Parameters                | Optional  |
| PID     | 1     | Set ID – Patient ID            | SI        |
|         | 2     | Patient ID (External ID)       | CK        |
|         | 3     | Patient ID (Internal ID)       | CK        |
|         | 4     | Alternate Patient ID           | CK        |
|         | 5     | Patient Name                   | PN        |
|         | 6     | Mother’s Maiden Name           | ST        |
|         | 7     | Date of Birth                  | TS        |
|         | 8     | Sex                            | ID        |
|         | 9     | Patient Alias                  | PN        |
|         | 10    | Race                           | ID        |
|         | 11    | Patient Address                | AD        |
|         | 12    | County Code                    | ID        |
|         | 13    | Phone Number – Home            | TN        |
|         | 14    | Phone Number – Business        | TN        |
|         | 15    | Language – Patient             | ST        |
|         | 16    | Marital Status                 | ID        |
|         | 17    | Religion                       | ID        |
|         | 18    | Patient Account Number         | CK        |
|         | 19    | SSN Number – Patient           | ST        |
|         | 20    | Driver’s Lic Num – Patient     | CM        |
|         | 21    | Mother’s Identifier            | CK        |
|         | 22    | Ethnic Group                   | ID        |
|         | 23    | Birth Place                    | ST        |
|         | 24    | Multiple Birth Indicator       | ID        |
|         | 25    | Birth Order                    | NM        |
|         | 26    | Citizenship                    | ID        |
|         | 27    | Veterans Military Status       | CE        |
| RCP     | 1     | Query Priority                 | ST        |
|         | N     | Ignored                        |           |

#### RTB^K13 Prescription Query Service Reponses

The following table defines the data elements required for each of the following segments of the RTB^K13 Prescription Query Service Response.

Message Header (MSH) segment

Message Acknowledgement (MSH) segment

Query Acknowledgement (QAK) segment

Query Parameter Definition (QPD) segment

Table Row Definition (RDF) segment

| Segment                                   | Piece | Description/Field Name         | Data Type/Description                                                                      |
|-------------------------------------------|-------|--------------------------------|--------------------------------------------------------------------------------------------|
| MSH                                       | 1     | Field Separator                | ST                                                                                         |
|                                           | 2     | Encoding Characters            | ST                                                                                         |
|                                           | 3     | Sending Application            | HD                                                                                         |
|                                           | 4     | Sending Facility               | HD                                                                                         |
|                                           | 5     | Receiving Application          | HD                                                                                         |
|                                           | 6     | Receiving Facility             | HD                                                                                         |
|                                           | 7     | Date/Time of Message           | TS                                                                                         |
|                                           | 8     | Security                       | ST                                                                                         |
|                                           | 9     | Message Type                   | CM                                                                                         |
|                                           | 10    | Message Control ID             | ST                                                                                         |
|                                           | 11    | Processing ID                  | PT                                                                                         |
|                                           | 12    | Version ID                     | ID                                                                                         |
|                                           | 13    | Sequence Number                | NM                                                                                         |
|                                           | 14    | Continuation Pointer           | ST                                                                                         |
|                                           | 15    | Accept Acknowledgement         | ID                                                                                         |
|                                           | 16    | Application Acknowledgement    | ID                                                                                         |
| appendi                                   | 17    | Country Code                   | ID                                                                                         |
|                                           | 18    | Character Set                  | ID                                                                                         |
|                                           | 19    | Principal Language of Messages | CE                                                                                         |
| MSA                                       | 1     | Acknowledge Code               | ID                                                                                         |
|                                           | 2     | Message Control ID             | ST                                                                                         |
|                                           | 3     | Text Message                   | W                                                                                          |
|                                           | 4     | Expected Sequence Number       | NM                                                                                         |
|                                           | 5     | Delayed Acknowledgement Type   | W                                                                                          |
|                                           | 6     | Error Condition                | W                                                                                          |
|                                           | 7     | Message Waiting Number         | NM                                                                                         |
|                                           | 8     | Message Waiting Priority       | ID                                                                                         |
| QAK                                       | 1     | Query Tag                      |                                                                                            |
|                                           | 2     | Query Response Status Code     |                                                                                            |
|                                           | 3     | Message Query Name             |                                                                                            |
|                                           | 4     | Count of RDT segments          |                                                                                            |
| QDP                                       | 1     | Message Query Name             | CE                                                                                         |
|                                           | 2     | Query Tag                      | ST                                                                                         |
|                                           | 3     | User Parameters                |                                                                                            |
| RDF                                       | 1     | Site Number                    | Site Number of the facility where the veteran has or had a prescription                    |
|                                           | 2     | Rx Number                      | The prescription number                                                                    |
|                                           | 3     | Drug Name (from the host site) | The name of the drug                                                                       |
|                                           | 4     | Quantity                       | The quantify of the prescription                                                           |
|                                           | 5     | Refills                        | The number of refills remaining                                                            |
|                                           | 6     | Days Supply                    | The number of days the prescription should be used                                         |
|                                           | 7     | Expiration Date                | The expiration date of the prescription                                                    |
|                                           | 8     | Issue Date                     | The issue date of the prescription                                                         |
|                                           | 9     | Stop Date                      | The end date for the prescription (same as expiration date)                                |
|                                           | 10    | Last Fill Date                 | The last date the prescription was refilled                                                |
|                                           | 11    | Sig                            |                                                                                            |
|                                           | 12    | Detail                         |                                                                                            |
|                                           | 13    | Status                         | The status of the prescription                                                             |
|                                           | 14    | VA Product IEN                 | The VA Product IEN of the drug                                                             |
|                                           | 15    | FQDN/Port (Unused)             | The fully qualified domain name of the host where the prescription originated and its port |
| <span id="Table37" class="anchor"></span> | 16    | PARKED Indicator               | Indicates if the prescription is PARKED on ‘host’                                          |
| RDT                                       | 1     | Site Number                    | Site Number of the facility where the veteran has or had a prescription                    |
|                                           | 2     | Rx Number                      | The prescription number                                                                    |
|                                           | 3     | Drug Name (from the host site) | The name of the drug                                                                       |
|                                           | 4     | Quantity                       | The quantify of the prescription                                                           |
|                                           | 5     | Refills                        | The number of refills remaining                                                            |
|                                           | 6     | Days Supply                    | The number of days the prescription should be used                                         |
|                                           | 7     | Expiration Date                | The expiration date of the prescription                                                    |
|                                           | 8     | Issue Date                     | The issue date of the prescription                                                         |
|                                           | 9     | Stop Date                      | The end date for the prescription (same as expiration date)                                |
|                                           | 10    | Last Fill Date                 | The last date the prescription was refilled                                                |
|                                           | 11    | Sig                            |                                                                                            |
|                                           | 12    | Detail                         |                                                                                            |
|                                           | 13    | Status                         | The status of the prescription                                                             |
|                                           | 14    | VA Product IEN                 | The VA Product IEN of the drug                                                             |
|                                           | 15    | FQDN/Port                      | The fully qualified domain name of the host where the prescription originated and its port |

<span id="Figure2" class="anchor"></span>Figure 2: Example RTB^K13 Prescription Query Service Response

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/007.png)

Example RTB^K13 HL7 RDF Segment

The Table Row Definition (RDF) segment defines the content for the Table Row Data (RDT) segment in the RTB^K13 HL7 message. The following is an example of the RDF segment created for the RTB^K13 HL7 message. The image displays the format to use for each prescription order.

<span id="_Toc155971190" class="anchor"></span>Figure 3: Example RTB^K13 HL7 RDF Segment

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/008.png)

#### RDS^O13 Pharmacy/Treatment Dispense Message Request

The ‘RDS^O13’ is a pass-through message that requires no transformation by a middleware application. The message can either be for a ‘Refill’ or ‘Partial Fill’ request. For a ‘Partial Fill’ request, the NTE segment will exist; it will not be there for a ‘Refill’ request.

98. With the introduction of patch PSO\*7\*774, a ‘Refill’ request on the ‘dispensing’ VistA instance can create an original fill on the ‘host’ VistA instance if a prescription was created there but never filled (e.g. PARKED prescription situation). Also, the ability to run a “Partial Fill Rx from Another VA Pharmacy” may not be selected for a remote medication that is both Parked and never been filled.

The following table defines the data elements required for each of the following segments of the RTB^K13 Prescription Query Service Response.

Message Header (MSH) segment

Patient Identification (PID) segment

The MUMPS code uses BLDPID^PSOTPHL2(DFN,"",.PSORRDAT,.HL,.ERR)’ to create the Patient Identification (PID) segment.

Common Order (ORC) segment

Pharmacy/Treatment Prescription Order (RXO)

Notes and Comments (NTE) segment

99. The Notes and Comments (NTE) segment will be present if the request is for a ‘Partial Fill’.

| Segment | Piece | Description / Field Name               | Data Type |
|---------|-------|----------------------------------------|-----------|
| MSH     | 1     | Field Separator                        | ST        |
|         | 2     | Encoding Characters                    | ST        |
|         | 3     | Sending Application                    | HD        |
|         | 4     | Sending Facility                       | HD        |
|         | 5     | Receiving Application                  | HD        |
|         | 6     | Receiving Facility                     | HD        |
|         | 7     | Date/Time of Message                   | TS        |
|         | 8     | Security                               | ST        |
|         | 9     | Message Type                           | CM        |
|         | 10    | Message Control ID                     | ST        |
|         | 11    | Processing ID                          | PT        |
|         | 12    | Version ID                             | ID        |
|         | 13    | Sequence Number                        | NM        |
|         | 14    | Continuation Pointer                   | ST        |
|         | 15    | Accept Acknowledgement                 | ID        |
|         | 16    | Application Acknowledgement            | ID        |
|         | 17    | Country Code                           | ID        |
|         | 18    | Character Set                          | ID        |
|         | 19    | Principal Language of Messages         | CE        |
| PID     | 1     | Set ID – Patient ID                    | SI        |
|         | 2     | Patient ID (External ID)               | CK        |
|         | 3     | Patient ID (Internal ID)               | CK        |
|         | 4     | Alternate Patient ID                   | CK        |
|         | 5     | Patient Name                           | PN        |
|         | 6     | Mother’s Maiden Name                   | ST        |
|         | 7     | Date of Birth                          | TS        |
|         | 8     | Sex                                    | ID        |
|         | 9     | Patient Alias                          | PN        |
|         | 10    | Race                                   | ID        |
|         | 11    | Patient Address                        | AD        |
|         | 12    | County Code                            | ID        |
|         | 13    | Phone Number – Home                    | TN        |
|         | 14    | Phone Number – Business                | TN        |
|         | 15    | Language – Patient                     | ST        |
|         | 16    | Marital Status                         | ID        |
|         | 17    | Religion                               | ID        |
|         | 18    | Patient Account Number                 | CK        |
|         | 19    | SSN Number – Patient                   | ST        |
|         | 20    | Driver’s Lic Num – Patient             | CM        |
|         | 21    | Mother’s Identifier                    | CK        |
|         | 22    | Ethnic Group                           | ID        |
|         | 23    | Birth Place                            | ST        |
|         | 24    | Multiple Birth Indicator               | ID        |
|         | 25    | Birth Order                            | NM        |
|         | 26    | Citizenship                            | ID        |
|         | 27    | Veterans Military Status               | CE        |
| ORC     | 1     | Order Control                          | ID        |
|         | 2     | Placer Order Number                    | CM        |
|         | 3     | Filler Order Number                    | CM        |
|         | 4     | Placer Group Number                    | CM        |
|         | 5     | Order Status                           | ID        |
|         | 6     | Response Flag                          | ID        |
|         | 7     | Quantity/Timing                        | TQ        |
|         | 8     | Parent                                 | CM        |
|         | 9     | Date/Time of Transaction               | TS        |
|         | 10    | Entered By                             | CN        |
|         | 11    | Verified By                            | CN        |
|         | 12    | Ordering Provider                      | CN        |
|         | 13    | Enterer’s Location                     | CM        |
|         | 14    | Call Back Phone Number                 | TN        |
|         | 15    | Order Effective Date/Time              | TS        |
|         | 16    | Order Control Code Reason              | CE        |
|         | 17    | Entering Organization                  | CE        |
|         | 18    | Entering Device                        | CE        |
|         | 19    | Action By                              | CN        |
| RXO     | 1     | Requested Give Code                    | CE        |
|         | 2     | Requested Give Amount – Minimum        | NM        |
|         | 3     | Requested Give Amount – Maximum        | NM        |
|         | 4     | Requested Give Units                   | CE        |
|         | 5     | Requested Dosage Form                  | CE        |
|         | 6     | Provider’s Pharmacy Instructions       | CE        |
|         | 7     | Provider’s Administration Instructions | CE        |
|         | 8     | Deliver to Location                    | CM        |
|         | 9     | Allow Substitutions                    | ID        |
|         | 10    | Requested Dispense Code                | CE        |
|         | 11    | Requested Dispense Amount              | NM        |
|         | 12    | Requested Dispense Units               | CE        |
|         | 13    | Number of Refills                      | NM        |
|         | 14    | Ordering Provider’s DEA Number         | CN        |
|         | 15    | Pharmacist Verifier ID                 | CN        |
|         | 16    | Needs Human Review                     | ID        |
|         | 17    | Requested Giver Per (Time Unit)        | ST        |
| NTE     | 1     | Set ID – NTE                           | SI        |
|         | 2     | Source of Comment                      | ID        |
|         | 3     | Comment                                | FT        |
|         | 4     | Comment Type                           | CE        |

<span id="_Toc155971191" class="anchor"></span>Figure 4: Example RDS^O13 Pharmacy/Treatment Dispense Message Request Refill

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/009.png)

<span id="_Toc155971192" class="anchor"></span>Figure 5: Example RDS^O13 Pharmacy/Treatment Dispense Message Request Partial Fill

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/010.png)

#### RRD^O14 Prescription Refill / Partial Services Response

The ‘RRD^O14’ message is the response to the ‘RDS^O13’ message.

The following table defines the data elements required for each of the following segments of the RRD^O14 Prescription Refill/Partial Services Response

Message Header (MSH) segment

Message Acknowledgement (MSH) segment

Patient Identification (PID) segment

100. The MUMPS code uses BLDPID^PSOTPHL2(DFN,"",.PSORRDAT,.HL,.ERR)’ to create the Patient Identification (PID) segment.

Common Order (ORC) segment

RXD Pharmacy/Treatment Dispense Segment

Notes and Comments (NTE) segment

101. The Notes and Comments (NTE) segment will be present if the request is for a ‘Partial Fill’.

| Segment | Piece | Description / Field Name       | Data Type |
|---------|-------|--------------------------------|-----------|
| MSH     | 1     | Field Separator                | ST        |
|         | 2     | Encoding Characters            | ST        |
|         | 3     | Sending Application            | HD        |
|         | 4     | Sending Facility               | HD        |
|         | 5     | Receiving Application          | HD        |
|         | 6     | Receiving Facility             | HD        |
|         | 7     | Date/Time of Message           | TS        |
|         | 8     | Security                       | ST        |
|         | 9     | Message Type                   | CM        |
|         | 10    | Message Control ID             | ST        |
|         | 11    | Processing ID                  | PT        |
|         | 12    | Version ID                     | ID        |
|         | 13    | Sequence Number                | NM        |
|         | 14    | Continuation Pointer           | ST        |
|         | 15    | Accept Acknowledgement         | ID        |
|         | 16    | Application Acknowledgement    | ID        |
|         | 17    | Country Code                   | ID        |
|         | 18    | Character Set                  | ID        |
|         | 19    | Principal Language of Messages | CE        |
| MSA     | 1     | Acknowledge Code               | ID        |
|         | 2     | Message Control ID             | ST        |
|         | 3     | Text Message                   | W         |
|         | 4     | Expected Sequence Number       | NM        |
|         | 5     | Delayed Acknowledgement Type   | W         |
|         | 6     | Error Condition                | W         |
|         | 7     | Message Waiting Number         | NM        |
|         | 8     | Message Waiting Priority       | ID        |
| PID     | 1     | Set ID – Patient ID            | SI        |
|         | 2     | Patient ID (External ID)       | CK        |
|         | 3     | Patient ID (Internal ID)       | CK        |
|         | 4     | Alternate Patient ID           | CK        |
|         | 5     | Patient Name                   | PN        |
|         | 6     | Mother’s Maiden Name           | ST        |
|         | 7     | Date of Birth                  | TS        |
|         | 8     | Sex                            | ID        |
|         | 9     | Patient Alias                  | PN        |
|         | 10    | Race                           | ID        |
|         | 11    | Patient Address                | AD        |
|         | 12    | County Code                    | ID        |
|         | 13    | Phone Number – Home            | TN        |
|         | 14    | Phone Number – Business        | TN        |
|         | 15    | Language – Patient             | ST        |
|         | 16    | Marital Status                 | ID        |
|         | 17    | Religion                       | ID        |
|         | 18    | Patient Account Number         | CK        |
|         | 19    | SSN Number – Patient           | ST        |
|         | 20    | Driver’s Lic Num – Patient     | CM        |
|         | 21    | Mother’s Identifier            | CK        |
|         | 22    | Ethnic Group                   | ID        |
|         | 23    | Birth Place                    | ST        |
|         | 24    | Multiple Birth Indicator       | ID        |
|         | 25    | Birth Order                    | NM        |
|         | 26    | Citizenship                    | ID        |
|         | 27    | Veterans Military Status       | CE        |
| ORC     | 1     | Order Control                  | ID        |
|         | 2     | Placer Order Number            | CM        |
|         | 3     | Filler Order Number            | CM        |
|         | 4     | Placer Group Number            | CM        |
|         | 5     | Order Status                   | ID        |
|         | 6     | Response Flag                  | ID        |
|         | 7     | Quantity/Timing                | TQ        |
|         | 8     | Parent                         | CM        |
|         | 9     | Date/Time of Transaction       | TS        |
|         | 10    | Entered By                     | CN        |
|         | 11    | Verified By                    | CN        |
|         | 12    | Ordering Provider              | CN        |
|         | 13    | Enterer’s Location             | CM        |
|         | 14    | Call Back Phone Number         | TN        |
|         | 15    | Order Effective Date/Time      | TS        |
|         | 16    | Order Control Code Reason      | CE        |
|         | 17    | Entering Organization          | CE        |
|         | 18    | Entering Device                | CE        |
|         | 19    | Action By                      | CN        |
| RXD     | 1     | Pharmacy/Treatment Dispense    |           |
|         | 2     | Dispense/Give Control          | CE        |
|         | 3     | Date/Time Dispensed            | TS        |
|         | 4     | Actual Dispense Units          | CE        |
|         | 5     | Ignored                        |           |
|         | 6     | Ignored                        |           |
|         | 7     | Prescription Number            | ST        |
|         | 8     | Number of Refills Remaining    | NM        |
|         | 9     | Ignored                        |           |
|         | 10    | Dispensing Provider            | XCN       |
|         | 11    | Ignored                        |           |
|         | 12    | Total Daily Dose               | CQ        |
| NTE     | 1     | Set ID – NTE                   | SI        |
|         | 2     | Source of Comment              | ID        |
|         | 3     | Comment                        | FT        |
|         | 4     | Comment Type                   | CE        |

### OneVA Pharmacy Messaging Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With this integrated VistA patch, several points of failure could occur. The systems design will allow the process to continue if any of the various integration points fail, however, remote prescriptions will not display to the Pharmacist on the Medication Profile view.

There are application error messages that will display during the search for the patient and the patient’s prescriptions. They are:

- No patient error message:  
  PATIENT IDENTIFIER NOT FOUND
- Multiple patients returned error messages:  
  MORE THAN ONE PATIENT RETURNED IN CALL TO HDR-CDS  
  MORE THAN ONE PATIENT FOUND ON RX DATABASE, CHECK ICN
- Patient returned, no prescription data returned error message:  
  PATIENT FOUND WITH NO PRESCRIPTION RECORDS
- Patient returned, no prescription data matching filters returned error message:  
  PATIENT FOUND WITH NO PRESCRIPTION RECORDS MATCHING SEARCH CRITERIA
- HL7 from VistA does not pass basic validation with a middleware application  
  Response Type: ACK  
  MSA-01: CR  
  MSA-03: {MESSAGE INDICATING INVALID DATA}

## Appendix G: Inbound ePrescribing (IEP) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Inbound ePrescribing Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A high-level overview of the Inbound ePrescribing (IEP) process flow for pharmacy data messages is outlined[\_Ref83216428](#_Ref83216428) below.

The IEP process flow depicts five (5) swim-lanes – one external to IEP (External Provider) and four (4) Inbound eR<sub>x</sub> processing tiers (Change Healthcare, Data Access Service (DAS), eR<sub>x</sub> Processing Hub and VistA Outpatient Pharmacy \[OP\]):

- External Provider:
  - External physicians (outside of the VA) who, with the use of a third party Electronic Medical Record (EMR) software, issue a prescription for a Veteran
  - The EMR system is registered with SureScripts, Change Healthcare, or both and is responsible for creating and sending the eR<sub>x</sub> in NCPDP 2017071 XML format
  - The External Provider is registered with SureScripts, Change Healthcare, or both and their provider information (e.g., National Provider Identification \[NPI\] number) is known and verified by Change Healthcare
- Change Healthcare:
  - Serves as proxy for all messages between the External Providers and the VA infrastructure (i.e., the DAS/eR<sub>x</sub> Processing Hub)
  - Supports and validates NCPDP 2017071 XML format and structure
- Data Access Services (DAS):
  - Serves as secured-layer gateway/proxy for all messages (in NCPDP 2017071 XML format) between Change Healthcare and the eR<sub>x</sub> Processing Hub
- eR<sub>x</sub> Processing Hub:
  - Receives, persists, validates, manipulates, and sends NCPDP 2017071 XML messages
  - Validates designated pharmacy from NCPDP XML message and match to VistA OP instance
  - Performs auto-validation and matching (including patient, enrollment / registration, provider, drug)
  - Sends prescription data to VistA eR<sub>x</sub> Holding Queue.
  - Maintains processing statuses and errors
  - Provides administrative user interface (UI) to track, enable/disable transmission, and run reports
- VistA Outpatient Pharmacy (OP)
  - Provides VistA UI for pharmacy users (manual steps, review and validate patient, provider, and drug/SIG)
  - Processes ePrescription (eR<sub>x</sub>) Holding Queue transactions. Once the eR<sub>x</sub> is validated, it is processed into the PENDING OUTPATIENT ORDERS (#52.41) file

<span id="_Ref83216428" class="anchor"></span>Figure 6: Inbound ePrescribing Process Flow (Version 4.0)

![](outpatient-pharmacy-version-7-technical-manual-security-guide-pso-7-766/011.png)

The Inbound eR<sub>x</sub> processing flow is sequential in nature as depicted in Figure 5 (above):

- Step 1: The Inbound eR<sub>x</sub> process flow begins with the External Provider, using their EMR system, creates and sends to Change Healthcare eR<sub>x</sub> message data in NCPDP 2017071 XML format. EMR Systems could also send via SureScripts, which are routed then through Change Healthcare.
- Step 2: In Change Healthcare, the eR<sub>x</sub> message is validated against the NCPDP 2017071 format to ensure that the message is in valid construct without any corruption.
- Step 3: If the message is valid, Change Healthcare routes the message to the VA infrastructure via DAS for further processing.
  - Step 3a: If the eR<sub>x</sub> message is invalid, an Error message is sent back to the External Provider (as per the NCPDP 2017071 specifications) without sending the message to VA.
- Step 4: DAS proxies the message to the eR<sub>x</sub> Processing Hub.
- Step 5: The eR<sub>x</sub> Processing Hub validates the NCPDP XML 2017071 format to ensure that the message is in a valid construct without any corruption and stores the message; the message is recorded in a transaction/processing table, which tracks the processing status of the message, as well as coordinates auto-validations and the synchronization with the VistA OP instance.
- Step 6: The eR<sub>x</sub> Processing Hub performs patient, provider, and drug/SIG auto-validations. The prescription record is updated to capture the auto-validation results – passed/failed.
- Step 7: The eR<sub>x</sub> Processing Hub constructs the eR<sub>x</sub> data into the format of the eRx Holding Queue and sends to the respective VistA OP. The eRx system utilizes the NPI Institution in the Outpatient site file (#59) to identify the eRx institution. The institution identified as the NPI Institution is a pointer to the Institution file (#4). The NPI value for this NPI Institution in the Institution file (#4) is used to map the eR<sub>x</sub>.
- Step 8: In the respective VistA OP instance, pharmacy personnel perform manual validation of the eR<sub>x</sub> (e.g., patient match, drug match, etc.).
- Step 9: Once all the validations are completed successfully, the prescription is fulfilled in VistA OP based on the existing fulfillment routines.
102. Change Healthcare validates all messages received back from eRx Processing Hub against the NCPDP 2017071 format to ensure that the message is in valid construct without any corruption and sends it to the External Provider. The Inbound eR<sub>x</sub> process flow ends with the External Provider receiving the message update from VA. In some cases, some of the EMR’s send Status messages back to the Hub upon successful receipt of messages from VA.

### Inbound ePrescribing Protocols 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound ePrescribing adds or modifies the following new protocols to facilitate the Inbound ePrescribing processing.

> PSO ERX ACCEPT ERX

> PSO ERX ACCEPT VALIDATION

> PSO ERX ACKNOWLEDGE

> PSO ERX ADD COMMENT

> PSO ERX ALL PATIENTS CR DEFAULT TEXT EDIT

> PSO ERX ALL PATIENTS QUEUE HIDDEN ACTIONS

> PSO ERX ALL RXS INCLUDE ALL STATUSES

> PSO ERX ALL RXS QUEUE HIDDEN ACTIONS MENU

> PSO ERX ALL RXS REMOVE FILTERS

> PSO ERX BATCH CHANGE REQUEST MENU

> PSO ERX BATCH CHANGE REQUEST SELECT

> PSO ERX BATCH CHANGE REQUEST SUBMISSION

> PSO ERX BATCH INCLUDE ALL STATUSES

> PSO ERX BATCH VISTA DRUG REPLACEMENT

> PSO ERX CHANGE REQUEST

> PSO ERX DISPLAY MENU

> PSO ERX DRUG EDIT FROM SINGLE ERX VIEW

> PSO ERX EDIT

> PSO ERX ENTER PROGRESS NOTES

> PSO ERX HIDDEN ACTIONS

> PSO ERX HOLD

> PSO ERX HQ MENU

> PSO ERX HQ SEARCH

> PSO ERX HQ SELECT

> PSO ERX HQ SORT

> PSO ERX JUMP TO ERX

> PSO ERX JUMP TO ERX PATIENT

> PSO ERX JUMP TO OP

> PSO ERX MESSAGE VIEW

> PSO ERX OP PRINT

> PSO ERX PATIENT ALLERGIES VIEW

> PSO ERX PCV MENU

> PSO ERX PCV MESSAGE VIEW

> PSO ERX PCV SEARCH QUEUE

> PSO ERX PCV SELECT BY NUMBER

> PSO ERX PCV SELECT PATIENT

> PSO ERX PCV SORT ENTRIES

> PSO ERX PRINT

> PSO ERX REFILL REQUEST

> PSO ERX REMOVE

> PSO ERX RESEND CHANGE REQUEST

> PSO ERX RX RENEWAL REQUEST

> PSO ERX SELECT BY NUMBER

> PSO ERX SINGLE PATIENT NEXT DRUG

> PSO ERX SINGLE PATIENT QUEUE HIDDEN

> PSO ERX SINGLE REFILL REQUEST

> PSO ERX SINGLE RXRENEWAL REQUEST

> PSO ERX STATUS HISTORY

> PSO ERX UN-ACCEPT

> PSO ERX UNHOLD

> PSO ERX UN-PROCESS

> PSO ERX UN-REMOVE

> PSO ERX VALIDATE ALL AND ACCEPT

> PSO ERX VALIDATE DRUG

> PSO ERX VALIDATE PATIENT

> PSO ERX VALIDATE PROVIDER

> PSO ERX VALIDATION MENU

> PSO ERX VIEW AUDIT LOG

> PSO ERX VIEW DRUG SUGGESTIONS

> PSO ERX VIEW HISTORY LOG

> PSO ERX VIEW ORIGINAL ERX

> PSO ERX VIEW PATIENT SUGGESTIONS

> PSO ERX VIEW PROVIDER SUGGESTIONS

> PSO ERX VIEW REQUEST ERX

> PSO ERX VIEW RESPONSE ERX

> PSO ERX VIEW SUGGESTED RX

> PSO HIDDEN ACTIONS

> PSO HIDDEN ACTIONS \#2

> PSO HIDDEN ACTIONS \#3

> PSO LM BACKDOOR PRTCL USRSCR VERIFY

> PSO LM EXIT2

> PSO LM HIDDEN OTHER

> PSO LM HIDDEN OTHER \#2

> PSO LMOE MOVE TO NEXT PATIENT

### Inbound ePrescribing Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inbound ePrescribing added the following new remote procedures to facilitate the Inbound ePrescribing messaging:

PSOERXA0 DRGMTCH: Drug matching logic

PSOERXA0 PRVMTCH: Provider match logic

PSOERXA1 INCERX: Read and file incoming eRx (XML message)

PSOERX1 INCERX: Read and file incoming eRx (XML message) in the 2017 script format, which replaces PSOERXA1 INCERX, which was the RPC used for the 10.6 script format

### Inbound ePrescribing Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new VistA option has been created that allows a pharmacist to view all inbound eRxs, validate patient, provider, and drug/SIG information, and ultimately, accept the eRx for sending to PENDING OUTPATIENT ORDERS file (#52.41). This menu is Complete Orders from eRx \[PSO ERX FINISH\]and is found on the Rx (Prescriptions) \[PSO RX\] menu.

### Inbound ePrescribing Holding Queue File (File \#52.49)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new VistA Inbound eRx Holding Queue (ERX HOLDING QUEUE FILE \#52.49) was created that holds all of the prescription information received on an eRx from an external provider. New Remote Procedures (RPC) were created within the OP package to accept the incoming HealtheVet Web Services Client (HWSC) messages (e.g., PSOERXA0 DRGMTCH, PSOERXA0 PRVMTCH, PSOERXA1 INCERX, etc.), which contains all of the needed elements for a prescription from a non-VA medical facility. Using the inbound HWSC message, a new entry is placed in the eRx Holding Queue file.

The Inbound eRx Holding Queue uses List Manager for user interaction. The Inbound eRx Holding Queue lists all eRxs received from external providers, with extended options available for users to view all the details about the prescriptions. Additional extended options were created to allow the pharmacist to validate patient, provider, and drug/SIG information.

ERX Holding Queue File \#52.49

.01 ERX HUB ID

.02 RELATED OR PARENT MESSAGE ID

.03 MESSAGE DATE/TIME

.04 EXTERNAL PATIENT IDENTIFIER

.05 VISTA PATIENT

.06 INSTITUTION

.07 PHARMACY SYSTEM

.08 MESSAGE TYPE

.09 EXTERNAL/PROVIDER ORDER NUMBER

.1 VISTA PENDING OUTPATIENT ORDER

.12 OE/RR ORDER NUMBER

.13 PHARMACY PRESCRIPTION NUMBER

.14 RELATES TO HUB ID

.15 SUGGESTED VISTA RX

1 ERX ORDER STATUS

1.11 DRUG VALIDATED BY

1.12 DRUG VALIDATED DATE/TIME

1.13 PATIENT VALIDATED BY

1.14 PATIENT VALIDATED DATE/TIME

1.2 PROV STAT (AUTO VALIDATION)

1.3 PROV STAT (MANUAL VALIDATION)

1.4 DRUG STAT (AUTO VALIDATION)

1.5 DRUG STAT (MANUAL VALIDATION)

1.6 PATIENT STATUS (AUTO VAL)

1.7 PATIENT STATUS (MANUAL VAL)

1.8 PROVIDER VALIDATED BY

1.9 PROVIDER VALIDATED DATE/TIME

2.1 EXTERNAL PROVIDER

2.2 EXTERNAL PHARMACIST

2.3 VA MATCHED PROVIDER

2.4 TO/FROM QUALIFIER

2.5 ERX EXTERNAL PHARMACY

2.6 ERX EXTERNAL SUPERVISOR

3.1 EXTERNAL DRUG/SUPPLY

3.2 MATCHED DRUG/SUPPLY

4.1 PRODUCT CODE

4.11 DRUG DB CODE QUALIFIER

4.2 PRODUCT CODE QUALIFIER

4.3 STRENGTH

4.4 DRUG DB CODE

4.5 FORM SOURCE CODE

4.6 FORM CODE

4.7 STRENGTH SOURCE CODE

4.8 STRENGTH CODE

4.9 DEA SCHEDULE

5.1 QUANTITY

5.2 CODE LIST QUALIFIER

5.3 UNIT SOURCE CODE

5.4 POTENCY UNIT CODE

5.5 DAYS SUPPLY

5.6 REFILLS

5.7 REFILL QUALIFIER

5.8 SUBSTITUTIONS

5.9 WRITTEN DATE

6.1 LAST FILL DATE

6.2 EXPIRATION DATE

6.3 EFFECTIVE DATE

6.4 PERIOD END

6.5 DELIVERED ON DATE

6.6 DATE VALIDATED

6.7 FUTURE FILL HOLD DATE

7 DIRECTIONS

8 NOTES

9 DIAGNOSIS

10.2 PRIOR AUTHORIZATION

10.3 PRIOR AUTHORIZATION QUALIFIER

10.4 PRIOR AUTHORIZATION STATUS

10.5 DO NOT FILL

10.6 NEEDED NO LATER THAN

10.7 TIMEZONE

10.8 TIME ZONE DIFFERENCE QUANTITY

10.9 NEEDED NO LATER THAN REASON

11 STRUCTURED SIG

12 ORDER CHECKS

13.1 PATIENT FACILITY UNIT

13.2 BED

13.3 ROOM

14 OBSERVATION

15 OBSERVATION NOTES

16 DRUG USE EVALUATION

17.1 EXTERNAL PHARMACY

17.2 EXTERNAL PHARMACIST

17.3 TRANSFERRED TO VA PHARMACY

17.4 XFER TO EXTERNAL PHARMACY

18 PAYER INFORMATION

19 STATUS HISTORY

20.1 VISTA QUANTITY

20.2 VISTA DAYS SUPPLY

20.3 VISTA VERB

20.4 VISTA ROUTING

20.5 VISTA REFILLS

20.6 VISTA CLINIC

21 QUANTITY/TIMING

22.1 FROM

22.2 FROM QUALIFIER

22.3 TO

22.4 TO QUALIFIER

22.5 CH SENT DATE/TIME

24.1 RELATED INSTITUTION

24.2 DIVISION

24.3 SENDER SECONDARY ID

24.4 SENDER TERTIARY ID

24.5 RECEIVER SECONDARY ID

24.6 RECEIVER TERTIARY ID

25 CH MESSAGE ID

25.2 PENDING OUTPATIENT ORDER#

26 VA DISPENSING INSTRUCTIONS

27 VA PATIENT INSTRUCTIONS

28 DRUG COVERAGE STATUS

29 INDICATION FOR USE

29.1 INDICATION FOR USE FLAG

29.2 OTHER LANG INDICATION FOR USE

30 VA PROVIDER COMMENTS

31 VA UNEXPANDED SIG

41 EXTERNAL FORM CODE

42 EXTERNAL POTENCY UNIT CODE

43 EXTERNAL STRENTH CODE

44 PAYER CARDHOLDER ID CONVERTED?

49 MEDICATION DISPENSED/REQUESTED

50 REQUEST/RESPONSE COMMENTS

50.1 NOTE ADDED BY

50.2 NOTE DATE/TIME

51.1 REFILL/CHANGE REQEUST PERSON

51.2 \# OF REFILLS REQUESTED

52.1 RESPONSE VALUE

52.2 RESPONSE NOTE

52.3 RESPONSE REFERENCE NUMBER

53 RESPONSE NOTE

55 RESPONSE CODES

60 REQUEST/RESPONSE ERROR TEXT

60.1 REQUEST/RESPONSE ERROR CODE

61 REQUEST/RESPONSE ERR DCODES

70.1 FACILITY NAME

70.2 FACILITY ADDRESS LINE 1

70.3 FACILITY ADDRESS LINE 2

70.4 FACILITY CITY

70.5 FACILITY STATE

70.6 FACILITY ZIP CODE

70.7 COUNTRY CODE

71 10.6 FACILITY ID

72 10.6 FACILITY COMM

73 2017 FACILITY COMMUNICATION

74.1 2017 FAC NCPDPID

74.2 2017 FAC STATE LIC NUMBER

74.3 2017 FAC MEDICARE NUMBER

74.4 2017 FAC MEDICAID NUMBER

74.5 2017 FAC UPIN

74.6 2017 FACILITY ID

75.1 2017 FAC DEA NUMBER

75.2 2017 FAC HIN

75.3 2017 FAC NPI

75.4 2017 FAC MUTUALLY DEFINED

75.5 2017 FAC REMS ENROLLMENT ID

76 2017 FACILITY DIRECT ADDRESS

80.1 CHANGE REQUEST TYPE

80.2 RETURN RECEIPT

80.3 REQUEST REFERENCE NUMBER

80.4 CHANGE RX STATUS FLAG

80.5 CHANGE/CANCEL DENIED BY HUB

100 PROCESSING ERRORS

201 MESSAGE HISTORY

301.1 2017 LTC LEVEL OF CHANGE

301.2 2017 URGENCY INDICATOR CODE

301.3 2017 PROHIBIT RENEWAL REQUEST

302 2017 NO KNOWN ALLERGIES

303 2017 ALLERGIES

304 2017 BENEFITS COORDINATION

305 2017 OBSERVATION NOTES

306 2017 OBSERVATION

307.1 2017 FOLLOW-UP PRESCRIBER

311 2017 MEDICATIONS

312.1 SCRIPT VERSION NUMBER

312.2 REQUEST REFERENCE NUMBER

312.3 RETURN RECEIPT

313.1 ECL VERSION

313.2 DATA TYPE VERSION

313.3 STRUCTURES VERSION

313.4 TRANSACTION DOMAIN

313.5 TRANSACTION VERSION

313.6 TRANSPORT VERSION

314.1 SENDER SOFTWARE DEVELOPER

314.2 SENDER SOFTWARE PRODUCT

314.3 SENDER SOFTWARE VERSION REL

315.1 CHANGE MES REQ CODE

316 CHANGE MES SUB CODE

317 CHANGE REQUEST REASON

318.1 CH RES STATE LICENSE NUM

318.2 CH RES MEDICARE NUMBER

318.3 CH RES MEDICAID NUMBER

319.1 CH RES UPIN

319.2 CH RES DEA NUMBER

319.3 CH RES HIN

319.4 CH RES SOCIAL SECURITY NUMBER

319.5 CH RES NPI

320.1 CH REQ PROGRESS NOTE REF \#

320.2 CH REQ PROGRESS NOTE COMMENT

321.1 CH RES CERT TO PRESCRIBE

321.2 CH RES DATA 2000 WAIVER ID

321.3 CH RES MUTUALLY DEFINED

322.1 CH RES REMS PROVIDER ID

322.2 CH RES STATE SUBSTANCE NUMBER

323 CH RES SUPERVISOR

324 VAL CH RES DATE

325 CH RES SPECIALTY

### Inbound ePrescribing External Patient File (File \#52.46)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERX External Patient File \#52.46 stores patient information from each incoming eRx.

ERX External Patient File \#52.46.01 NAME

.02 LAST NAME

.03 FIRST NAME

.04 MIDDLE NAME

.05 SUFFIX

.06 PREFIX

.07 GENDER

.08 DATE OF BIRTH

.09 ERX EXTERNAL PHARMACY

1.1 FILE ID

1.2 MEDICAL RECORD ID \#

1.3 ACCOUNT NUMBER

1.4 SSN

1.5 LINKED VISTA PATIENT

1.6 COUNTRY CODE

1.7 PATIENT RELATIONSHIP

2 COMMUNICATION

3.1 ADDRESS LINE 1

3.2 ADDRESS LINE 2

3.3 CITY

3.4 STATE/PROVINCE

3.5 POSTAL CODE

5 IDENTIFICATION

6 LAST LOCKED BY

7.1 FORMER LAST NAME

7.2 FORMER FIRST NAME

7.3 FORMER MIDDLE NAME

7.4 FORMER SUFFIX

7.5 FORMER PREFIX

8.1 PATIENT LOCATION FACILITY/UNIT

8.2 PATIENT LOCATION/ROOM

8.3 PATIENT LOCATION/BED

8.4 LANGUAGE NAME CODE

8.5 GESTATIONAL AGE

8.6 HOSPICE INDICATOR

9.1 ALTERNATE CONTACT LAST NAME

9.2 ALTERNATE CONTACT FIRST NAME

9.3 ALTERNATE CONTACT MIDDLE NAME

9.4 ALTERNATE CONTACT SUFFIX

9.5 ALTERNATE CONTACT PREFIX

9.6 ALT CONTACT RELATIONSHIP

10.1 ALT CONTACT FORMER LAST NAME

10.2 ALT CONTACT FORMER FIRST NAME

10.3 ALT CONTACT FORMER MIDDLE NAME

10.4 ALT CONTACT FORMER SUFFIX

10.5 ALT CONTACT FORMER PREFIX

11.1 ALT CONTACT ADDRESS LINE 1

11.2 ALT CONTACT ADDRESS LINE 2

11.3 ALT CONTACT CITY

11.4 ALT CONTACT STATE

11.5 ALT CONTACT POSTAL CODE

11.6 ALT CONTACT COUNTRY CODE

13 2017 COMMUNICATION

14 2017 DIRECT ADDRESS

15 2017 ALT COMMUNICATION

16 2017 ALT DIRECT ADDRESS

17.1 2017 MEDICARE NUMBER

17.2 2017 MEDICAID NUMBER

17.3 2017 MEDICAL RECORD ID \#

18.1 2017 ACCOUNT NUMBER

18.2 2017 SSN

18.3 2017 MUTUALLY DEFINED

18.4 2017 REMS PATIENT ID

19 2017 SUBSTANCES

### Inbound ePrescribing External Pharmacy File (#52.47)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERX External Pharmacy File \#52.47 is a sub-file that holds the identification elements passed in with the incoming eRx on pharmacy information.

Inbound ePrescribing External Pharmacy File (#52.47)

.01 NAME

.02 NCPDP ID

.03 NPI

.04 DEA NUMBER

.05 STORE NAME

1.1 ADDRESS LINE 1

1.2 ADDRESS LINE 2

1.3 CITY

1.4 STATE/PROVINCE

1.5 POSTAL CODE

1.6 TYPE

1.7 COUNTRY CODE

1.8 SPECIALTY

2 IDENTIFICATION

3 COMMUNICATION

4 ASSOCIATED ERX PERSON

5.1 FORMER LAST NAME

5.2 FORMER FIRST NAME

5.3 FORMER MIDDLE NAME

5.4 FORMER SUFFIX

5.5 FORMER PREFIX

7 2017 COMMUNICATION

8 2017 DIRECT ADDRESS

9.1 2017 STATE LICENSE NUMBER

9.2 2017 MEDICARE NUMBER

9.3 2017 MEDICAID NUMBER

9.4 2017 UPIN

9.5 2017 HIN

9.6 2017 MUTUALLY DEFINED

10.1 2017 NCPDP ID

10.2 2017 NPI

10.3 2017 DEA NUMBER

### Inbound ePrescribing External Person (File \#52.48)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERX External Person File \#52.48 stores external provider information from the incoming new eRx. Each provider record is unique based on a combination of parameters.

Inbound ePrescribing External Person (File \#52.48).01 NAME

.02 LAST NAME

.03 FIRST NAME

.04 MIDDLE NAME

.05 SUFFIX

.06 PREFIX

1.1 PERSON TYPE

1.2 SPECIALTY

1.3 ASSOCIATED ERX PHARMACY

1.4 NCPDP ID

1.5 NPI

1.6 DEA \#

1.7 HIN

1.8 STATE LICENSE NUMBER

2.1 BUSINESS NAME

2.2 COUNTRY CODE

2.3 PRESCRIBER PLACE OF SERVICE

2.4 FORMER LAST NAME

2.5 FORMER FIRST NAME

2.6 FORMER MIDDLE NAME

2.7 FORMER SUFFIX

2.8 FORMER PREFIX

3 COMMUNICATION

4.1 STREET ADDRESS LINE 1

4.2 ADDRESS LINE 2

4.3 CITY

4.4 STATE/PROVINCE

4.5 POSTAL CODE

5.1 AGENT LAST NAME

5.2 AGENT FIRST NAME

5.3 AGENT MIDDLE NAME

5.4 AGENT SUFFIX

5.5 AGENT PREFIX

6 IDENTIFICATION

7.1 AGENT FORMER LAST NAME

7.2 AGENT FORMER FIRST NAME

7.3 AGENT FORMER MIDDLE NAME

7.4 AGENT FORMER SUFFIX

7.5 AGENT FORMER PREFIX

11 2017 COMMUNICATION

12 2017 DIRECT ADDRESS

14.1 2017 STATE LICENCE \#

14.2 2017 MEDICARE NUMBER

14.3 2017 MEDICAID NUMBER

14.4 2017 UPIN

14.5 2017 DEA NUMBER

14.6 2017 HIN

14.7 2017 SOCIAL SECURITY

15.1 2017 NPI

15.2 2017 CERTIFICATE TO PRESCRIBE

15.3 2017 DATA 2000 WAIVER ID

15.4 2017 MUTUALLY DEFINED

15.5 2017 REMS ID

15.6 2017 STATE CS NUMBER

17.1 2017 PL NCPDP ID

17.2 2017 PL STATE LICENSE NUMBER

17.3 2017 PL MEDICARE NUMBER

17.4 2017 PL MEDICAID NUMBER

17.5 2017 PL UPIN

17.6 2017 PL FACILITY ID

18.1 2017 PL DEA NUMBER

18.2 2017 PL HIN

18.3 2017 PL NPI

18.4 2017 PL MUTUALLY DEFINED ID

18.5 2017 PL REMS HEALTHCARE ID

18.6 2017 PL BUSINESS NAME

19.1 VETERINARIAN

### Inbound ePrescribing External Person (File \#52.45)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERX Service Reason Codes File \#52.45 stores the Service Reason Codes and their corresponding translations.

ERX SERVICE REASON CODES (#52.45)

.001 NUMBER

.01 SERVICE REASON CODE

.02 BRIEF DESCRIPTION

.03 CODE TYPE

.04 CODE DESCRIPTION

1 FULL DESCRIPTION

2.1 NCIT SUBTYPE

20 CHANGE REQUEST REASON TEXT

21 CH REQ REASON TEXT BY DIVISION

    

[Outpatient Pharmacy PRESCRIPTION FILE (File \#52)](\l)

[PRESCRIPTION (#52) ACTIVITY LOG SUB-FILE (#52.3)](\l)

[REASON (#.02)](\l)

Outpatient Pharmacy OUTPATIENT SITE (File \#59)

OUTPATIENT SITE (#59) ERX DEFAULT LOOKBACK DAYS

(#10.2)

### Inbound ePrescribing New Field in Existing File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new field for a VA site’s default eRx clinic (ERX LOOKBACK DAYS \#10.2) was added to the Outpatient Site File \#59 and is also released as part of the VistA patch for Inbound ePrescribing.

<span id="_26_Appendix_H:" class="anchor"></span>

## Appendix H: DEA# Migration Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall design of Pharmacy Operations – DEA# Enhancements DOJ/DEA Migration has these components:

- Veterans Health Information Systems and Technology Architecture (VistA) (Patches PSO\*7.0\*529, PSO\*7.0\*667, and PSO\*7.0\*684)
- A VA Maintained DOJ/DEA web server with the names and DEA numbers of controlled substance prescribers.
- A web service client to be used during installation to retrieve the provider information from the VA Maintained DOJ/DEA web server.
- Filing the DOJ/DEA information into the DEA NUMBERS file (#8991.9) and linking the DEA NUMBERS file (#8991.9) to the NEW PERSON file (#200), NEW DEA \#'S (#53.21) multiple.
- New and modified menus and options containing DEA related functionality:
  - The Add New Providers \[PSO PROVIDER ADD\], Edit Provider \[PSO PROVIDER EDIT\], and View Provider \[PSO PROVIDER INQUIRE\] options have been updated to prompt for and display the DEA number information from the DEA NUMBERS file (#8991.9), and to allow an unlimited number of DEA numbers to be assigned to each provider.
  - Pharmacy Order Entry options have been updated to prompt the pharmacist to select the correct DEA number when there are multiple DEA numbers assigned to the ordering provider.

The initial DOJ/DEA migration process occurs as part of the patch installations of PSO\*7.0\*529. At installation, a search is made through the DEA \# field (#53.2) of the NEW PERSON file (#200). For each DEA \#, a call is made to the DOJ/DEA web server to retrieve the prescriber’s DEA information. If the call is successful, then the DEA information is filed in the DEA NUMBERS file (#8991.9) and the DEA NUMBERS file entry is linked to the prescriber in the NEW PERSON file (#200) and to the DEA BUSINESS ACTIVITY CODES file (#8991.8).

Patch PSO\*7.0\*684 performs a refresh “migration” of provider DEA information to new data dictionaries introduced by XU\*8\*688 and initially migrated by PSO\*7.0\*529. The DOJ/DEA migration process occurs as part of the patch installation. Prior to refreshing the DEA information, all old DEA information will be deleted. At installation, a search is made through the DEA \# field (#53.2) of the NEW PERSON file (#200). For each DEA \#, a call is made to the DOJ/DEA web server to retrieve the prescriber’s DEA information. If the call is successful, then the DEA information is filed in the DEA NUMBERS file (#8991.9) and the DEA NUMBERS file entry is linked to the prescriber in the NEW PERSON file (#200) and to the DEA BUSINESS ACTIVITY CODES file (#8991.8). Upon successful installation of this patch, an entry will be logged in the Kernel ^XTMP global for use by the environment check of the follow-on patch PSO\*7.0\*545 installation.

Patch PSO\*7.0\*684 also makes enhancements to the DEA Migration Report \[PSO DEA MIGRATION REPORT\] option to support the migration of DEA numbers from the NEW PERSON file (#200) to the DEA NUMBERS file (#8991.9).

### The Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSO DOJ/DEA WEB SERVER is a REST API web service that matches prescriber DEA numbers to the VA Maintained DOJ/DEA web server. If successful, the web service returns the valid DEA information for the prescriber.

- The web service is accessed at the following URL: https:// dev.deals.vaec.va.gov
- Protocol: The web service is a REST API and accepts and returns JSON request/ response objects.

HealtheVet Web Services Client (HWSC) - HWSC acts as an adjunct to the web services client functionality provided in Caché by leveraging Caché's platform-provided web services client capabilities. At the patch installation, entries are made in the WEB SERVER file (#18.12) for the entry PSO DOJ/DEA WEB SERVER and in the WEB SERVICES file (#18.02) for the entry PSO DOJ/DEA WEB SERVICE.

Consuming the Web Service - HWSC wrapper code is used to consume the web service, thereby making use of built-in error detection and error trap triggering.

Error response codes:

- 404 – Page Not Found (DEA Not Found)
- 6059 – Unable to establish a connection

HWSC Wrapper Calls:

- // gets client REST request object SET REQUEST=\$\$GETREST^XOBWLIB("MY REST SERVICE","MY SERVER")
- // executes HTTP GET method SET REQUEST=\$\$GET^XOBWLIB(REQUEST,XOBRSCE,XOBERR,XOBFERR)
- JSON Response - Response is stored in the REQUEST. HttpResponse.Data object in JSON format.

### Menu and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new menu option has been created to support VistA reports with PSO\*7\*667 and updated with PSO\*7\*545. This menu option is ePCS DEA Utility Functions \[PSO EPCS UTILITY FUNCTIONS\]. The Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option was also created. Both ePCS DEA Utility Functions \[PSO EPCS UTILITY FUNCTIONS\] and Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] are stand-alone menus, not attached to any class 1 menus.

The ePCS DEA Utility Functions \[PSO EPCS UTILITY FUNCTIONS\] menu has the following menu option items:

- DEA Expiration Date Report \[PSO EPCS EXPIRE DATE REPORT\]
- Changes to DEA Prescribing Privileges Report \[PSO EPCS LOGICAL ACCESS REPORT\]
- Allocation Audit of PSDRPH Key Report \[PSO EPCS PHARMACIST ACC REPORT\]
- Enter/Edit EPCS Access Reports Parameters \[PSO EPCS ACCESS REPORTS PARAM\]
- Print PSDRPH Key Holders \[PSO EPCS PSDRPH\]
- Set Pharmacy Operating Mode \[PSO VAMC MBM PHARMACY MODE\]
- Print Setting Parameters Privileges \[PSO EPCS SET PARMS\]
- Print Prescribers with Privileges \[PSO EPCS PRIVS\]
- Edit Facility DEA# and Expiration Date \[PSO EPCS EDIT DEA# AND XDATE\]
- Print Audits for Prescriber Editing \[PSO EPCS PRINT EDIT AUDIT\]
- Print DISUSER Prescribers with Privileges \[PSO EPCS DISUSER PRIVS\]
- Allow VA Number if DEA Number Expired \[PSO EPCS EXPIRED DEA FAILOVER\]
- Manual DEA Number Entry \[PSO EPCS DEA MANUAL ENTRY\]
- Manually Entered DEA Number Report \[PSO EPCS MANUAL DEA REPORT\]
- DEA Number Integrity Check \[PSO EPCS DEA INTEGRITY REPORT\]

#### DEA Expiration Date Report \[PSO EPCS EXPIRE DATE REPORT\]

This option can be used to print the DEA Expiration Date for all active users. It provides the following criteria to check the DEA expiration status:

Report requires 132 Columns

Select one of the following:

> A Active

> D DISUSERed

> B Both

Select one of the following:

> E EXPIRED

> N NO EXP DATE

> 3 \<30-DAYS

> 9 \<90-DAYS

#### Changes to DEA Prescribing Privileges Report \[PSO EPCS LOGICAL ACCESS REPORT\]

This is an on-demand report option that will print the setting or a change to DEA prescribing privileges related to issuance of controlled substance prescription. It will prompt for a date range and will print data that has been modified. The data is retrieved from the XUEPCS DATA file (#8991.6).

#### Allocation Audit of PSDRPH Key Report \[PSO EPCS PHARMACIST ACC REPORT\]

This is an on-demand report option that will print the allocation of the PSDRPH key. It will prompt for a date range and will print the allocation of the PSDRPH key data that has been modified. The data is retrieved from the XUEPCS PSDRPH AUDIT file (#8991.7).

#### Enter/Edit EPCS Access Reports Parameters \[PSO EPCS ACCESS REPORTS PARAM\]

This option will help the sites to set up the printer device and the email group related to the following parameters:

- Device for Pharmacist access report \[PSOEPCS PHARM ACC RPT DEVICE\]
- Email Group for Pharmacist Access Report \[PSOEPCS PHARM ACC REPORT EMAIL\]
- Device for Logical Access Report \[PSOEPCS LOGICAL ACC REPORT DEV\]
- Email Group for Logical Access Report \[PSOEPCS LOGICAL ACC RPT EMAIL\]

#### Print PSDRPH Key Holders \[PSO EPCS PSDRPH\]

This option will print all active users holding the PSDRPH key. This report will sort by division and within division it sorts by key holder name. This report will print the key holder name, key holder Designated User (DUZ), the person who assigned key, and the date that the key was assigned. A Non-licensed pharmacist (a user who is not a registered pharmacist - or a non-pharmacist) now can assign the PSDRPH key permissions when using PSO EPCS PSDRPH KEY Allocate/De-Allocate (Audited) option without personally having the authorizations.

#### Set Pharmacy Operating Mode \[PSO VAMC MBM PHARMACY MODE\]

This option will allow sites to turn off the warning message confirmation prompt associated with selecting a provider without a CPRS account for Meds by Mail sites running VistA as their pharmacy package.

#### Print Setting Parameters Privileges \[PSO EPCS SET PARMS\]

This option prints all active users holding the XUEPCSEDIT key. This report will identify individuals responsible for setting the parameters.

#### Print Prescribers with Privileges \[PSO EPCS PRIVS\]

This option prints all active users who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#. This option prints the NAME, SCHEDULES, VA#, DUZ, and DEA#.

#### Edit Facility DEA# and Expiration Date \[PSO EPCS EDIT DEA# AND XDATE\]

This option is for the DEA ePCS project and will allow users to edit the facility DEA# and Expiration Date in Institution file (#4).

### Print Audits for Prescriber Editing \[PSO EPCS PRINT EDIT AUDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the ability to print information related to the editing of prescriber information related to electronic Prescribing of Controlled Substances.

#### Print DISUSER Prescribers with Privileges \[PSO EPCS DISUSER PRIVS\]

This option is for the DEA ePCS project and will print all DISUSER users who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#. This option prints the NAME, SCHEDULESs, VA#, DUZ, TERMINATION DATE, and DEA#.

#### Allow VA Number if DEA Number Expired \[PSO EPCS EXPIRED DEA FAILOVER\]

This option will allow the sites to turn off the expired DEA number "fail over" functionality so that the renewal of a provider's expired DEA number can be enforced.

#### Manual DEA Number Entry \[PSO EPCS DEA MANUAL ENTRY\]

This option allows the manual addition and edit of DEA numbers in the DEA NUMBERS file (#8991.9) when a connection to the DEA Web Service cannot be established.

#### Manually Entered DEA Number Report \[PSO EPCS MANUAL DEA REPORT\]

This option prints all DEA numbers that were last entered, edited, or both using the Manual DEA Number Entry \[PSO EPCS DEA MANUAL ENTRY\]. DEA numbers entered or edited with this option are not retrieved from the PSO DOJ/DEA WEB SERVICE.

#### DEA Number Integrity Check \[PSO EPCS DEA INTEGRITY REPORT\]

This option can be used to print the DEA Number Integrity Check report. The report displays the following errors:

- A DEA number in the provider's profile does not exist in file 8991.9.
- Provider name associated with the DEA number does not match the provider name on the provider profile.
- Institutional DEA numbers without a suffix.
- Providers with at least one Individual DEA number, but no DEA numbers flagged for Inpatient.
- An individual DEA number that is associated with more than one provider.

### Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH Key Allocate/De-Allocate\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New option Allocate/De-Allocate of PSDRPH Key (Audited) \[PSO EPCS PSDRPH KEY\] option has been created and 'orphaned' (not attached to any class 1 menus). The option allows users to allocate or de-allocate the PSDRPH key while also logging an audit record of the transaction. This option was copied from existing option Allocate/De-Allocate of PSDRPH Key \[XU EPCS PSDRPH KEY\].

### Remote Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Remote Procedure has been created to support the Web Veteran's Health Information Systems and Technology Architecture (VistA) Remote Access Management (WebVRAM) application. The PSO EPCS PSDRPH FILER Remote Procedure Call (RPC) has been published to perform allocation and deallocation of the PSDRPH key, and logging of the event in the XUEPCS PSDRPH AUDIT file (#8991.7).

NAME: PSO EPCS PSDRPH FILER

TAG: PSDKEY ROUTINE: PSOEPUT2 RETURN VALUE TYPE: SINGLE VALUE AVAILABILITY: RESTRICTED

DESCRIPTION:

Allocates and deallocates the PSDRPH key to the specified user and logs the event in the XUEPCS PSDRPH AUDIT (#8991.7) file.

INPUT PARAMETER: PSOSUBJ PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

The NEW PERSON (#200) file Internal Entry Number (IEN) of the user to whom the PSDRPH key is being allocated or deallocated.

INPUT PARAMETER: PSOACTOR PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

The NEW PERSON (#200) file Internal Entry Number (IEN) of the user performing the allocation or deallocation of the PSDRPH key.

INPUT PARAMETER: PSOACTION PARAMETER TYPE: LITERAL MAXIMUM DATA LENGTH: 1 REQUIRED: YES

SEQUENCE NUMBER: 3

DESCRIPTION:

A flag indicating the type of action to be taken, either "1" to allocate the PSDRPH key, or "0" to deallocate the PSDRPH key.

RETURN PARAMETER DESCRIPTION:

The return value is 1 if the allocation or deallocation was successful.

The return value is 0^Error Message Text if the allocation or deallocation was unsuccessful.

| Error Message Text                                            | Description                                                                                                                                                                                                              |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invalid Action Code                                           | The PSOACTION input parameter is a value other than 0 (zero) or 1 (one).                                                                                                                                                 |
| PSDRPH key does not exist                                     | The PSDRPH key does not exist in the SECURITY KEY (#19.1) file.                                                                                                                                                          |
| Missing or invalid key recipient input parameter              | The PSOSUBJ input parameter is set to null or any non-numeric value. The PSOSUBJ input parameter represents the user to whom the PSDRPH key is being allocated.                                                          |
| Missing or invalid key allocator input parameter              | The PSOACTOR input parameter is set to null or any non-numeric value. The PSOACTOR input parameter represents the user allocating the PSDRPH key.                                                                        |
| Key recipient IEN \#### does not exist in the NEW PERSON file | The value of the PSOSUBJ input parameter passed validation but does not point to a record that exists in the NEW PERSON file. The PSOSUBJ input parameter represents the user to whom the PSDRPH key is being allocated. |
| Allocator IEN \#### does not exist in the NEW PERSON file     | The PSOACTOR input parameter passed validation but does not point to a record that exists in the NEW PERSON file. The PSOACTOR input parameter represents the user allocating the PSDRPH key.                            |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Outpatient Pharmacy Version 7 Technical Manual Security Guide (PSO*7*774)

### Steps for Startup/Shutdown of the External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens depict the steps necessary to startup and shutdown the external interface for Version 1.6 of the VistA Health Level Seven (HL7) application package. See Appendix A of this manual for more information on the Outpatient Pharmacy V. 7.0 HL7 Specification.

The following examples are options from the HL7 package. The top-level menu option being used is the HL MAIN MENU \[*HL7 Main Menu*\] option.

Example: Starting Up the Interface

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO DISP

The LLP was last shutdown on MAY 11, 2004 07:29:53.

This LLP has been enabled!

Example: Shutting Down the Interface

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO DISP

The LLP was last started on JUN 02, 2004 09:52:02.

Okay to shut down this job? YES

The job for the PSO DISP Lower Level Protocol will be shut down.
