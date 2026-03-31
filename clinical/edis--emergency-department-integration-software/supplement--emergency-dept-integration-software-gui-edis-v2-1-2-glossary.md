---
title: Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Glossary
doc_type: SUP
doc_label: Supplement
doc_layer: anchor
doc_subject: Glossary
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.2
patch_id: EDIS*2.1.2
group_key: "EDIS:EDIS:2.1.2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - class
  - even
  - health
  - java
  - veterans
  - patient
  - technology
page_count: 0
word_count: 7178
section_count: 79
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 6
revision_newest: 10/17/2014
revision_oldest: 05/12/2013
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_glossary.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_glossary.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

Department of Veterans AffairsEmergency Department Integration Software (EDIS)Glossary

![](emergency-dept-integration-software-gui-edis-version-2-1-2-glossary/001.png)

VistA EDP\*2.0\*2GUI EDIS Version 2.1.2November 2014Document Version 2.3

Office of Information and Technology (OI&T)

Product Development

Revision History

| Date       | Version | Description                                                                  | Author                                                               |
|------------|---------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 05/12/2013 | 2.0     | Updated header and footer and cover page                                     | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| 05/13/2013 | 2.0     | Final review prior to submission                                             | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| 06/19/2013 | 2.1     | Incorporate edits from Product Support                                       | Prod Dev                                                             |
| 06/20/2013 | 2.1     | Updated styles of text for 508 compliance, footer, and TOC                   | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |
| 07/17/2013 | 2.2     | Update Section 1.2 document listing                                          | ProdDev                                                              |
| 10/17/2014 | 2.3     | Updated cover page and footer to reflect EDIS version 2.1.2. Updated styles. | [<span class="mark">redacted</span>](ftp://ftp.fo-albany.med.va.gov) |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Summary](#summary)
  - [Scope](#scope)
- [Acronyms and Definitions](#acronyms-and-definitions)
- [Terms & Conditions](#terms-conditions)
  - [Approved Initial Requirements Analysis](#approved-initial-requirements-analysis)
  - [Application Structure and Integration Services (ASIS)](#application-structure-and-integration-services-asis)
  - [Asynchronous JavaScript and XML (Ajax)](#asynchronous-javascript-and-xml-ajax)
  - [Barcode Medication Administration (BCMA)](#barcode-medication-administration-bcma)
  - [Build](#build)
  - [Caché](#caché)
  - [Caché Server Pages](#caché-server-pages)
  - [Capability Maturity Model® Integration (CMMI)](#capability-maturity-model-integration-cmmi)
  - [Care Management](#care-management)
  - [Certification Commission for Healthcare Information Technology (CCHIT)](#certification-commission-for-healthcare-information-technology-cchit)
  - [Clinical Assistance Agent (CAA)](#clinical-assistance-agent-caa)
  - [Clinical Context Object Workgroup (CCOW)](#clinical-context-object-workgroup-ccow)
  - [Clinical Domain](#clinical-domain)
  - [Clinical Practice Environment (CPE)](#clinical-practice-environment-cpe)
  - [Commercial Off-the-Shelf (COTS)](#commercial-off-the-shelf-cots)
  - [Computerized Patient Record System (CPRS)](#computerized-patient-record-system-cprs)
  - [Computerized Patient Record System – Reengineering (CPRS-R)](#computerized-patient-record-system-reengineering-cprs-r)
  - [Decision Support Services (DSS)](#decision-support-services-dss)
  - [EAR (Enterprise ARchive)](#ear-enterprise-archive)
  - [Eclipse](#eclipse)
  - [Enterprise Reference Terminology/Data Standardization (ERT/DS)](#enterprise-reference-terminologydata-standardization-ertds)
  - [Extensible Markup Language (XML)](#extensible-markup-language-xml)
  - [Flash Player](#flash-player)
  - [Flex](#flex)
  - [Flex Player](#flex-player)
  - [Gap Analysis](#gap-analysis)
  - [Graphical User Interface (GUI)](#graphical-user-interface-gui)
  - [Health Data Repository (HDR)](#health-data-repository-hdr)
  - [Health<u>e</u>Vet Desktop (HeVD)](#healthueuvet-desktop-hevd)
  - [Health<u>e</u>Vet-VistA](#healthueuvet-vista)
  - [Health Level 7 (HL7)](#health-level-7-hl7)
  - [Hibernate](#hibernate)
  - [Hypertext Markup Language (HTML)](#hypertext-markup-language-html)
  - [Hypertext Transfer Protocol (HTTP)](#hypertext-transfer-protocol-http)
  - [Impact Analysis](#impact-analysis)
  - [Independent Verification and Validation (IV&V)](#independent-verification-and-validation-ivv)
  - [Information Technology Advisory Committee (ITAC)](#information-technology-advisory-committee-itac)
  - [Integrated Collaborative Environment (ICE)](#integrated-collaborative-environment-ice)
  - [Iterative Development Lifecycle (IDL)](#iterative-development-lifecycle-idl)
    - [Inception Phase](#inception-phase)
    - [Elaboration Phase](#elaboration-phase)
    - [Construction Phase](#construction-phase)
    - [Transition Phase](#transition-phase)
  - [Java](#java)
  - [Java Database Connectivity (JDBC)](#java-database-connectivity-jdbc)
  - [Java Platform, Enterprise Edition (Java EE—Formerly J2EE)](#java-platform-enterprise-edition-java-eeformerly-j2ee)
  - [JavaServer Pages (JSP)](#javaserver-pages-jsp)
  - [Java Servlet](#java-servlet)
  - [Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE)](#kernel-authentication-and-authorization-for-java-2-enterprise-edition-kaajee)
  - [Logical Observations, Identifiers, Names, and Codes (LOINC®)](#logical-observations-identifiers-names-and-codes-loinc)
  - [Massachusetts General Hospital Utility Multiprogramming System (MUMPS or M)](#massachusetts-general-hospital-utility-multiprogramming-system-mumps-or-m)
  - [Master Patient Index (MPI)](#master-patient-index-mpi)
  - [Medication Possession Ratio (MPR)](#medication-possession-ratio-mpr)
  - [Mockup](#mockup)
  - [Model View Controller (MVC)](#model-view-controller-mvc)
  - [MXML](#mxml)
  - [NetBeans](#netbeans)
  - [.NET Framework](#net-framework)
  - [Patient Information Management System (PIMS)](#patient-information-management-system-pims)
  - [Plain Old Java Object (POJO)](#plain-old-java-object-pojo)
  - [Primary Care Management Module (PCMM)](#primary-care-management-module-pcmm)
  - [Remote Data Views (RDV)](#remote-data-views-rdv)
  - [Representational State Transfer (REST or RESTful) Web Services](#representational-state-transfer-rest-or-restful-web-services)
  - [Scope Creep](#scope-creep)
  - [Service Oriented Architecture (SOA)](#service-oriented-architecture-soa)
  - [Spring Framework](#spring-framework)
  - [Stakeholder](#stakeholder)
  - [Structured Query Language (SQL)](#structured-query-language-sql)
  - [Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT)](#systematized-nomenclature-of-medicine-clinical-terms-snomed-ct)
  - [Text Integration Utilities (TIU)](#text-integration-utilities-tiu)
  - [Uniform Resource Identifier/ Uniform Resource Locator (URI/URL)](#uniform-resource-identifier-uniform-resource-locator-uriurl)
  - [Use Case](#use-case)
  - [Veterans Health Information Systems and Technology Architecture (VistA)](#veterans-health-information-systems-and-technology-architecture-vista)
  - [Virtual Patient Record (VPR)](#virtual-patient-record-vpr)
  - [VISN CIO Council (VCIOC)](#visn-cio-council-vcioc)
  - [VistA Blood Establishment Computer Software (VBECS)](#vista-blood-establishment-computer-software-vbecs)
  - [VistAWeb](#vistaweb)
  - [Wagner Chronic Care Model](#wagner-chronic-care-model)
  - [Widget](#widget)
  - [Wiki](#wiki)

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary supports formal and informal project documentation for Emergency Department Integration Software (EDIS). The glossary is a work in progress. As the project moves forward, the terms and acronyms contained herein will reflect additions to the project’s technical vocabulary while maintaining its historical vocabulary.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary contains terms, definitions, acronyms, and abbreviations included in the following documents:

- EDIS Installation Guide
- EDIS IRM Big Board Installation Guide
- EDIS User Manual
- EDIS Technical Manual

The number of documents on this list will grow as the project moves through the iterative development lifecycle (IDL).

# Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Acronyms</p>
</blockquote></th>
<th><blockquote>
<p>Definition</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADT</p>
</blockquote></td>
<td><blockquote>
<p>Admission, Discharge, and Transfer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AITC</p>
</blockquote></td>
<td><blockquote>
<p>Austin Information Technology Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AMS</p>
</blockquote></td>
<td><blockquote>
<p>Medical Automation Systems</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>API</p>
</blockquote></td>
<td><blockquote>
<p>Application Program Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ASIS</p>
</blockquote></td>
<td><blockquote>
<p>Application Structure and Integration Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BCMA</p>
</blockquote></td>
<td><blockquote>
<p>Barcode Medication Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CAA</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Assistance Agents</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CACs</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Applications Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Control</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCB</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Control Board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHIT</p>
</blockquote></td>
<td><blockquote>
<p>Certification Commission for Healthcare Information Technology</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCOW</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Context Object Workgroup</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CDS</p>
</blockquote></td>
<td><blockquote>
<p>Common Data Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHDR</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Data Repository/Health Data Repository (Interoperability Project)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CI</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Item</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CIO</p>
</blockquote></td>
<td><blockquote>
<p>Chief Information Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CMP</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Management Plan</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CMMI</p>
</blockquote></td>
<td><blockquote>
<p>Capability Maturity Model® Integration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COTS</p>
</blockquote></td>
<td><blockquote>
<p>Commercial Off-The-Shelf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPE</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Practice Environment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS-R</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System – Reengineering</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPT</p>
</blockquote></td>
<td><blockquote>
<p>Current Procedural Terminology</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CR</p>
</blockquote></td>
<td><blockquote>
<p>Change Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRDC</p>
</blockquote></td>
<td><blockquote>
<p>Capital Region Data Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CSA</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Status Accounting</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CSF</p>
</blockquote></td>
<td><blockquote>
<p>Critical Success Factor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CSP</p>
</blockquote></td>
<td><blockquote>
<p>Caché Server Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CVA</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Verification and Audit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DFN</p>
</blockquote></td>
<td><blockquote>
<p>Data File Number (field .001 in the VistA FileMan Patient file)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DoD</p>
</blockquote></td>
<td><blockquote>
<p>Department of Defense</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DSM-III</p>
</blockquote></td>
<td><blockquote>
<p>Diagnostic and Statistical Manual of Mental Disorders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DSS</p>
</blockquote></td>
<td><blockquote>
<p>Decision Support Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EAR</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Archives</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E3R</p>
</blockquote></td>
<td><blockquote>
<p>Electronic Error and Enhancement Request</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ECCB</p>
</blockquote></td>
<td><blockquote>
<p>Environment Change Control Board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ED</p>
</blockquote></td>
<td><blockquote>
<p>Emergency Department</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EIE</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Infrastructure Engineering</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMFAC</p>
</blockquote></td>
<td><blockquote>
<p>Emergency Medicine Field Advisory Committee</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EPS</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Product Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ERT/DS</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Reference Terminology/Data Standardization</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ESM</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Systems Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVEAH</p>
</blockquote></td>
<td><blockquote>
<p>Enhance the Veterans Experience Access to Healthcare</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVE</p>
</blockquote></td>
<td><blockquote>
<p>Client Server Program – System Manager</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVS</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise VistA Support (now Enterprise Product Support)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FCA</p>
</blockquote></td>
<td><blockquote>
<p>Functional Configuration Audit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GPO</p>
</blockquote></td>
<td><blockquote>
<p>Group Policy Objects</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GTS</p>
</blockquote></td>
<td><blockquote>
<p>Generic Traffic Shaping</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphical User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HDR</p>
</blockquote></td>
<td><blockquote>
<p>Health Data Repository</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HEC</p>
</blockquote></td>
<td><blockquote>
<p>Health Eligibility Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HeVD</p>
</blockquote></td>
<td><blockquote>
<p>HealtheVet Desktop</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIMS</p>
</blockquote></td>
<td><blockquote>
<p>Health Information Management Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HIPAA</p>
</blockquote></td>
<td><blockquote>
<p>Health Insurance Portability and Accountability Act</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIS</p>
</blockquote></td>
<td><blockquote>
<p>Indian Health Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HITC</p>
</blockquote></td>
<td><blockquote>
<p>Hines Information Technology Center</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIV</p>
</blockquote></td>
<td><blockquote>
<p>Human Immunodeficiency Virus</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>Health Level 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HPS</p>
</blockquote></td>
<td><blockquote>
<p>Health Provider Systems</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HSITES</p>
</blockquote></td>
<td><blockquote>
<p>Health Systems Implementation Training and Enterprise Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HTML</p>
</blockquote></td>
<td><blockquote>
<p>Hypertext Markup Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HTTP</p>
</blockquote></td>
<td><blockquote>
<p>Hypertext Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>iaw</p>
</blockquote></td>
<td><blockquote>
<p>In accordance with</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD</p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICE</p>
</blockquote></td>
<td><blockquote>
<p>Integrated Collaborative Environment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IDL</p>
</blockquote></td>
<td><blockquote>
<p>Iterative Development Lifecycle</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Internet Explorer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td><blockquote>
<p>Internal Entry Number (for VistA FileMan Files)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IOC</p>
</blockquote></td>
<td><blockquote>
<p>Independent Out-Patient Clinics</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>Internet Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRA</p>
</blockquote></td>
<td><blockquote>
<p>Initial Requirements Analysis</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resources Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ISP</p>
</blockquote></td>
<td><blockquote>
<p>Internet Service Provider</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ITAC</p>
</blockquote></td>
<td><blockquote>
<p>Information Technology Advisory Committee</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IV&amp;V</p>
</blockquote></td>
<td><blockquote>
<p>Independent Verification and Validation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Java EE (formerly J2EE)</p>
</blockquote></td>
<td><blockquote>
<p>Java Platform, Enterprise Edition—Formerly Java 2 Platform Enterprise Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAWS</p>
</blockquote></td>
<td><blockquote>
<p>Job Access with Speech</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JDBC</p>
</blockquote></td>
<td><blockquote>
<p>Java Database Connectivity</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JSF</p>
</blockquote></td>
<td><blockquote>
<p>JavaServer Faces</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JSP</p>
</blockquote></td>
<td><blockquote>
<p>JavaServer Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Authentication and Authorization for Java 2 Enterprise Edition</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KIDS</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Installation &amp; Distribution System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KPI</p>
</blockquote></td>
<td><blockquote>
<p>Key Performance Indicator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LCD</p>
</blockquote></td>
<td><blockquote>
<p>Liquid Crystal Display</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LOINC®</p>
</blockquote></td>
<td><blockquote>
<p>Logical Observations, Identifiers, Names, and Codes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LVN</p>
</blockquote></td>
<td><blockquote>
<p>Licensed Vocational Nurse</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MPI</p>
</blockquote></td>
<td><blockquote>
<p>Master Patient Index</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MPR</p>
</blockquote></td>
<td><blockquote>
<p>Medication Possession Ratio</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MRTG</p>
</blockquote></td>
<td><blockquote>
<p>Multi Router Traffic Grapher</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MTBF</p>
</blockquote></td>
<td><blockquote>
<p>Mean Time Before Failure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MTTR</p>
</blockquote></td>
<td><blockquote>
<p>Mean Time To Repair</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MUMPS (or M)</p>
</blockquote></td>
<td><blockquote>
<p>Massachusetts General Hospital Utility Multiprogramming System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MVC</p>
</blockquote></td>
<td><blockquote>
<p>Model View Controller</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MXML</p>
</blockquote></td>
<td><blockquote>
<p>Macromedia Flex Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NOIS</p>
</blockquote></td>
<td><blockquote>
<p>National Online Information Sharing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NSR</p>
</blockquote></td>
<td><blockquote>
<p>New Service Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NT&amp;EO</p>
</blockquote></td>
<td><blockquote>
<p>National Training and Education Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OED</p>
</blockquote></td>
<td><blockquote>
<p>Office of Enterprise Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OI&amp;T</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information and Technology</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OMB</p>
</blockquote></td>
<td><blockquote>
<p>Office of Management and Budget</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORT</p>
</blockquote></td>
<td><blockquote>
<p>Operational Readiness Testing</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PCMM</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Management Module</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PKI</p>
</blockquote></td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PITC</p>
</blockquote></td>
<td><blockquote>
<p>Philadelphia Information Technology Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PMAS</p>
</blockquote></td>
<td><blockquote>
<p>Performance Management Accountability System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>POC</p>
</blockquote></td>
<td><blockquote>
<p>Point-of-Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POJO</p>
</blockquote></td>
<td><blockquote>
<p>Plain Old Java Object</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PTF</p>
</blockquote></td>
<td><blockquote>
<p>Patient Treatment File</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PWS</p>
</blockquote></td>
<td><blockquote>
<p>Performance Work Statement</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QA</p>
</blockquote></td>
<td><blockquote>
<p>Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QOS</p>
</blockquote></td>
<td><blockquote>
<p>Quality of Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RALS</p>
</blockquote></td>
<td><blockquote>
<p>Point 0f Care IT Connectivity System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RAM</p>
</blockquote></td>
<td><blockquote>
<p>Random Access Memory</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RDV</p>
</blockquote></td>
<td><blockquote>
<p>Remote Data Views</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RDMS</p>
</blockquote></td>
<td><blockquote>
<p>Relational Database Management Systems</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REST or RESTful</p>
</blockquote></td>
<td><blockquote>
<p>Representational State Transfer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RIA</p>
</blockquote></td>
<td><blockquote>
<p>Rich Internet Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RPC</p>
</blockquote></td>
<td><blockquote>
<p>Remote Procedures Calls</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RQM</p>
</blockquote></td>
<td><blockquote>
<p>Rational Quality Manager</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RR</p>
</blockquote></td>
<td><blockquote>
<p>Risk Register</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCM</p>
</blockquote></td>
<td><blockquote>
<p>Software Configuration Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDD</p>
</blockquote></td>
<td><blockquote>
<p>System Design Document</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SD&amp;D</p>
</blockquote></td>
<td><blockquote>
<p>Systems Design and Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDS</p>
</blockquote></td>
<td><blockquote>
<p>Standard Data Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SLA</p>
</blockquote></td>
<td><blockquote>
<p>Service Level Agreement</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SNOMED CT</p>
</blockquote></td>
<td><blockquote>
<p>Systematized Nomenclature of Medicine Clinical Terms®</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOA</p>
</blockquote></td>
<td><blockquote>
<p>Service Oriented Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SQA</p>
</blockquote></td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQL</p>
</blockquote></td>
<td><blockquote>
<p>Structured Query Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SRS</p>
</blockquote></td>
<td><blockquote>
<p>Software Requirements Specification</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>To Be Determined</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td><blockquote>
<p>Text Integration Utilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TRRB</p>
</blockquote></td>
<td><blockquote>
<p>Team Risk Review Board</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TSPR</p>
</blockquote></td>
<td><blockquote>
<p>Technical Services Project Repository</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TWG</p>
</blockquote></td>
<td><blockquote>
<p>Technical Working Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UAT</p>
</blockquote></td>
<td><blockquote>
<p>User Acceptance Testing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UCM</p>
</blockquote></td>
<td><blockquote>
<p>Unified Change Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UFT</p>
</blockquote></td>
<td><blockquote>
<p>User Functional Testing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>URI/URL</p>
</blockquote></td>
<td><blockquote>
<p>Uniform Resource Identifier/Uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAMC</p>
</blockquote></td>
<td><blockquote>
<p>Veteran Affairs Medical Center</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VBECS</p>
</blockquote></td>
<td><blockquote>
<p>VistA Blood Establishment Computer Software</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VCIOC</p>
</blockquote></td>
<td><blockquote>
<p>VISN CIO Council</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VDL</p>
</blockquote></td>
<td><blockquote>
<p>VistA Documentation Library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VDSI</p>
</blockquote></td>
<td><blockquote>
<p>VistA Data Systems and Integration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VERA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Equitable Resource Allocation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Services Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VOB</p>
</blockquote></td>
<td><blockquote>
<p>Voice Object Base</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VPR</p>
</blockquote></td>
<td><blockquote>
<p>Virtual Patient Record</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WBS</p>
</blockquote></td>
<td><blockquote>
<p>Work Breakdown Structure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XML</p>
</blockquote></td>
<td><blockquote>
<p>Extensible Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XSLT</p>
</blockquote></td>
<td><blockquote>
<p>Extensible Stylesheet Language Transformation</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Terms & Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Approved Initial Requirements Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Information Technology Advisory Committee (ITAC)-approved document containing a project’s initial requirements.

## Application Structure and Integration Services (ASIS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An organization within the Veterans Administration (VA) Office of Information (OI) that is responsible for overseeing Health*<u>e</u>*Vet-VistA development efforts.

## Asynchronous JavaScript and XML (Ajax)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A technique for developing interactive Web applications. The technique uses a suite of technologies (extensible markup language, extensible hypertext markup language, cascading style sheets, HttpRequest, JavaScript and other scripting languages, etc.) to make Web pages feel more responsive.

## Barcode Medication Administration (BCMA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A national program to improve healthcare by using barcodes to track and monitor the dispensing and administration of medications; software that tracks medication dispensing and administration in inpatient settings by using barcodes and barcode readers.

## Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A test version of software, usually designated by a series of numbers. Developers usually increment the previous test version by one when they create a new test version.

## Caché

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An InterSystems multidimensional database that supports Java objects (plain old java objects \[POJOs\] and Enterprise Java Beans) and structured query language access.

## Caché Server Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An InterSystems architecture and toolset for building interactive Web applications.

## Capability Maturity Model® Integration (CMMI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Software Engineering Institute (of Carnegie Mellon University) process-improvement approach that provides essential elements for creating effective processes. CMMI guides process improvements for the Department of Defense (DoD), other federal agencies, and private enterprises.

## Care Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VHA) Java application that extends the current Computerized Patient Record System (CPRS) application by adding multi-patient views of order-related and other information. Care Management also includes alerting and tasking functionality.

## Certification Commission for Healthcare Information Technology (CCHIT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A private, non-profit certification program for electronic health records (EHRs). The U.S. Department of Health and Human Services officially designated this de facto authority for EHRs as a recognized certification body (RCB).

## Clinical Assistance Agent (CAA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A computer tool to help healthcare professionals make clinical decisions.

## Clinical Context Object Workgroup (CCOW)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A standards-based protocol that uses Health Level 7 (HL7) messages to enable disparate applications to synchronize on common data at the interface level.

## Clinical Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functions and information that are specific to a particular clinical context. For example, medication-ordering functions and medication-related data are specific to the pharmacy domain.

## Clinical Practice Environment (CPE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A team-based, multi-patient, multi-provider, knowledge- and workflow-driven clinical care environment.

## Commercial Off-the-Shelf (COTS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software that outside (non-Veterans Administration \[VA\]) vendors produce and make commercially available.

## Computerized Patient Record System (CPRS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single graphical user interface through which users can access multiple Veterans Health Information Systems and Technology Architecture (VistA) applications. CPRS is a Delphi application.

## Computerized Patient Record System – Reengineering (CPRS-R)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A terminated project to move Computerized Patient Record System to an updated platform that supports the Veterans Administration’s (VA’s) Health*<u>e</u>*Vet technology direction.

## Decision Support Services (DSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Health Administration (VHA) software that extracts information from Veterans Health Information Systems and Technology Architecture (VistA) systems. DSS software makes data extracts temporarily available for local reporting activities. For permanent report storage, DSS transmits the information to the Austin Automation Center for upload into a reporting database from Eclipsys, Transition System, Inc.

## EAR (Enterprise ARchive)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a file format used by Java EE for packaging one or more modules into a single archive so that the deployment of the various modules onto an application server happens simultaneously and coherently. It also contains XML files called deployment descriptors which describe how to deploy the modules.

## Eclipse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An open-source, platform-independent framework for developing rich-clients—as opposed to Web- or thin-client—applications.

## Enterprise Reference Terminology/Data Standardization (ERT/DS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VA) Office of Information (OI) project to implement a common set of data standards throughout the VHA healthcare system.

## Extensible Markup Language (XML)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A World Wide Web Consortium (W3C) standard. This markup language is widely used to facilitate Web-based information interchanges.

## Flash Player

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A multimedia and application player from Adobe Systems. Flash Player runs Flash and Flex applications.

## Flex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A collection of technologies from Adobe Systems for developing and deploying cross platform, rich Internet applications (RIAs) that run within the Adobe Flash platform.

## Flex Player

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application player for displaying Adobe Flash and Adobe Flex applications.

## Gap Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An analysis aimed at identifying necessary requirements that are missing from a project’s requirements documents. Gap analyses are important because omitted requirements can cause loss of needed end-user functionality, financial loss, non-compliance with federal regulations and laws, and an overall loss of confidence in a project.

## Graphical User Interface (GUI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application component that uses graphical images, text, and widgets. GUIs provide the interface through which users can interact with computers or computer applications.

## Health Data Repository (HDR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A national repository for Veterans Health Administration (VHA) clinical data.

## Health*<u>e</u>*Vet Desktop (HeVD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Java Swing framework that supports the Veterans Administration’s (VA’s) Care Management application.

## Health<u>e</u>Vet-VistA 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VHA) development effort to provide legacy VistA services on an updated technology platform.

## Health Level 7 (HL7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An American National Standards Institute (ANSI) standards-development organization; a standard for exchanging, integrating, and retrieving electronic health information. Many Veterans Health Administration (VHA) applications use HL7 messages to exchange data.

## Hibernate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An open-source technology for mapping Java classes to relational database tables and Java data types to structured query language (SQL) data types. Hibernate automates common data-handling tasks for Java developers.

## Hypertext Markup Language (HTML)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A markup language that enables Web designers to describe the structure of Web pages.

## Hypertext Transfer Protocol (HTTP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A World Wide Web Consortium (W3C) and Internet Engineering Task Force (IETF) standard response/request protocol for transferring or conveying information over the Internet.

## Impact Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A type of analysis in which analysts examine a project’s requirements to determine whether—and how—changes to these requirements would affect other project requirements.

## Independent Verification and Validation (IV&V)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VHA) organization that provides and manages Veterans Health Information Systems and Technology Architecture (VistA) components for systems development and software quality assurance (SQA) activities.

## Information Technology Advisory Committee (ITAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A committee that reviews initial-requirements-analysis documents and approves or rejects them.

## Integrated Collaborative Environment (ICE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A virtual environment that integrates collaboration, workflow, document-management, and social networking capabilities.

## Iterative Development Lifecycle (IDL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A software-development model in which developers proceed sequentially through each stage of development several times; each pass through a sequence of stages is called iteration.

### Inception Phase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The stage of software development in which a project team defines its preliminary vision of an application, including the application’s main features and architecture. The project team also clarifies the project’s overall scope during this stage of the iterative development lifecycle (IDL).

### Elaboration Phase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The stage of software development in which a project team refines its vision for—and the scope of—its development effort. The project team also defines and baselines the software’s architecture and formulates a more precise development and deployment plan. During this phase, developers also design prototypes to test areas of concern.

### Construction Phase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The stage of software development in which developers build software and deliver selected components to end users for feedback and testing.

### Transition Phase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The stage of software development in which developers deliver the software to end users. For the Veterans Administration (VA), this entails transitioning software to the field (that is, deploying and delivering software, training end users and technical support staffs, and supporting and maintaining the software).

## Java

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An open-source, object-oriented, platform-independent programming language. (Java’s proprietor, Sun Microsystems, released the Java source code to the open-source community.)

## Java Database Connectivity (JDBC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Java application program interface (API) that enables Java applications to access (read) and modify (add, delete, or change) data within a database.

## Java Platform, Enterprise Edition (Java EE—Formerly J2EE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An open-source platform for developing and running multi-tier, enterprise Java applications. Before the release of Java EE 1.5, this platform was known as Java 2 Platform Enterprise Edition (J2EE).

## JavaServer Pages (JSP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A technology for dynamically generating Web content (Hypertext Markup Language \[HTML\], Extensible Markup Language \[XML\], or other kinds of documents) in response to requests from Web-clients.

## Java Servlet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application program interface (API) through which software developers can add dynamic content to Web servers using the Java platform. Servlets receive requests from and generate responses to requesting applications.

## Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Health*<u>e</u>*Vet-VistA authentication and authorization application specifically for supporting applications running on Java Platform, Enterprise Edition (J2EE). KAAJEE is the only VA-approved security package for these applications.

## Logical Observations, Identifiers, Names, and Codes (LOINC®)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An American Clinical Laboratory Association-endorsed data system that provides a set of universal names and codes for identifying individual laboratory results. The committee responsible for introducing new codes includes representatives from the Veterans Health Administration (VHA).

## Massachusetts General Hospital Utility Multiprogramming System (MUMPS or M)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A late 1960s programming language. MUMPS (or M) was, and in some cases continues to be, the language of choice for many healthcare systems and databases—including the Veterans Health Information Systems and Technology Architecture (VistA) system.

## Master Patient Index (MPI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VHA) nation-wide index of unique patient identifiers. The VHA’s Remote Data Views (RDV) application relies on this index to retrieve clinical information from multiple sites.

## Medication Possession Ratio (MPR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The amount of a medication (number of pills or number of doses) that a patient currently possesses divided by the prescribed amount of the medication. This ratio is useful for determining when to refill prescriptions for chronic conditions or if patients are taking their medications as directed.

## Mockup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A graphical illustration of a software application, system, or system component. Mockups often form the basis for prototypes, which are usually working models of applications, systems, or system components.

## Model View Controller (MVC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An architectural pattern that many in the software-development community regard as a best-practices approach to software design. This pattern separates database actions from business-logic components that request the actions, and business logic from the user interface that calls the logic. The intermediate component that sits between each layer of this three-tier architectural pattern is called a controller.

## MXML

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Extensible Markup Language-based user-interface markup language that works with Adobe ActionScript in Adobe Flex applications.

## NetBeans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A platform for developing Java desktop applications and an integrated development environment (IDE) that is based on the NetBeans platform.

## .NET Framework

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Microsoft Windows software component that comprises a framework for developing applications that run on the Windows operating system.

## Patient Information Management System (PIMS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A modular system of Veterans Health Information Systems and Technology Architecture (VistA) applications that help medical-administration personnel complete hospital-operations tasks.

## Plain Old Java Object (POJO)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An ordinary—as opposed to special—Java object.

## Primary Care Management Module (PCMM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Information Systems and Technology Architecture (VistA) application that helps facilities implement and manage primary-care activities. Nationally, the Veterans Health Administration (VHA) uses this application for its national database of patients’ primary-care assignments.

## Remote Data Views (RDV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Information Systems and Technology Architecture (VistA) application that enables Computerized Patient Record System (CPRS) users to query and view data from all Veterans Health Administration (VHA) medical centers and from available Department of Defense (DoD) treating facilities.

## Representational State Transfer (REST or RESTful) Web Services 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A set of architectural principles for designing Web applications. The Web itself is a key example of existing REST design.

## Scope Creep

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The result of piggy backing unapproved requirements on approved requirements. Scope creep often creates significant development and implementation delays and cost overruns.

## Service Oriented Architecture (SOA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A software architecture that relies on independent, loosely coupled services to support application functionality. Because services are reusable, this architecture can significantly reduce development time and offer application-wide consistency that reduces user-training time.

## Spring Framework 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An open-source application framework for developing Java Web-based applications.

## Stakeholder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Anyone who could be materially affected by a system or application.

## Structured Query Language (SQL) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A popular computer language for adding, deleting, changing, and manipulating data that resides in relational database management systems.

## Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A College of American Pathologists system of standardized medical terms. SNOMED CT is a U.S. federal government data standard for electronic clinical data.

## Text Integration Utilities (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Information Systems and Technology Architecture (VistA) application that simplifies the management of clinical documents for clinical and administrative staff. TIU integrates with Computerized Patient Record System (CPRS), enabling authorized users to view and manage documents from within the CPRS system.

## Uniform Resource Identifier/ Uniform Resource Locator (URI/URL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Internet standard for identifying and locating Web content.

## Use Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A technique for capturing requirements for software systems or systems of systems.

## Veterans Health Information Systems and Technology Architecture (VistA) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A hospital information system that more than 1,300 Veterans Administration (VA) facilities use to maintain electronic health records for over five million veterans.

## Virtual Patient Record (VPR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A structured query language (SQL) database that can pull and organize information from any backend data source. It caches data for fast read access and automatically updates cached data via an event-based update module.

## VISN CIO Council (VCIOC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An action group aligned under the Veterans Health Administration (VHA) National Leadership Board (NLB) Informatics and Data Management Committee (IDMC). VCIOC formulates Veterans Integrated Services Network (VISN) requirements relating to the technology direction, policy, and products of Veterans Administration (VA) information-technology projects.

## VistA Blood Establishment Computer Software (VBECS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Veterans Health Administration (VHA) project that will create an improved blood-bank system for providing veterans with high-quality blood products and services. This standards-compliant software will, as its name suggests, integrate with the Veterans Health Information System and Technology Architecture (VistA).

## VistAWeb

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application that enables users to view remote data from within Computerized Patient Record System (CPRS). VistAWeb also includes a standalone interface for users who require special-user access (such as access for researchers or people who are working to mitigate national disasters).

## Wagner Chronic Care Model

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Improving Chronic Illness Care (ICIC) model that identifies essential elements for promoting high-quality chronic disease care. (ICIC is a national program that the Robert Wood Johnson Foundation supports with direction and technical assistance from Group Health Cooperative’s MacColl Institute for Healthcare Innovation.)

## Widget

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A reusable graphical user interface (GUI) component that provides a specific set of user interactions. For example, the grid widget displays information in customizable, sortable, relational tables that are called grids.

## Wiki

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A collaborative Web site that is capable of allowing visitors to add and edit site content.