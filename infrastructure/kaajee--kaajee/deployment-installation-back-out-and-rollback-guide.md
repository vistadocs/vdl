---
title: KAAJEE SSPI Rollback Instructions (WebLogic 12.2)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: KAAJEE
app_name: KAAJEE
section: INF
app_status: archive
pkg_ns: KAAJEE
patch_ver: 12.2
patch_id: null
group_key: KAAJEE::12.2
file_numbers: []
security_keys:
- PROVIDER
menu_options: 0
description: '- Revision History - # List of Tables - KAAJEE SSPI rollback Documentation Revisions The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to...'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 447
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 2021
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Infrastructure/KAAJEE_Archive/KAAJEE_SSPI_8_748_BCKOUT.docx
pdf_url: https://www.va.gov/vdl/documents/Infrastructure/KAAJEE_Archive/KAAJEE_SSPI_8_748_BCKOUT.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=298
audit_applied: '2026-05-31'
master_source: KAAJEE SSPI Rollback Instructions (WebLogic 12.2)
master_pub_date: December 2021
consolidated_from: 2 versions
prior_versions:
- KAAJEE SSPI 8.0.781 Rollback Instructions (WebLogic 12.2)
consolidated_title: kaajee sspi rollback instructions
---

![](kaajee-sspi-rollback-instructions-weblogic-12-2/001.png)

KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EE (KAAJEE)

SECURITY SERVICE PROVIDER INTERFACE (SSPI) VERSION 8.0.748

FOR WEBLOGIC (WL) VERSIONS 12.2 AND HIGHER

ROLLBACK GUIDE

December 2021

Office of Information and Technology

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [# List of Tables](#list-of-tables)
  - [KAAJEE SSPI rollback](#kaajee-sspi-rollback)
Documentation Revisions
The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.
<span id="_Toc44314849" class="anchor"></span>Table i. Documentation revision history
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 59%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2021</td>
<td><p>Updated software and the installation guide with relation to the KAAJEE SSPI.</p>
<p><strong>Kernel Patch: XU*8.0*748</strong>, makes changes the Technical Reference Model (TRM) compliance changes and upgrades/certifications of a KAAJEE SSPI component for the WebLogic 12.2/Java 1.8 and Oracle Relational Database Management System (RDMS), version 19c platform.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/2021</td>
<td>Second version of this document.</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# # List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Table i. Documentation revision history [3](#_Toc44314849)](#_Toc44314849)

## KAAJEE SSPI rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate and Run the setWLSEnv.sh script on the application server

![](kaajee-sspi-rollback-instructions-weblogic-12-2/002.png)

> The file is located under the server/bin directory by default (Ex: /u01/app/oracle/weblogic-server-12.2.1.4/wlserver/server/bin/setWLSEnv.sh)

#### Run the java weblogic.WLST and pass the required properties file to the deleteDSSSPI.py

> java weblogic.WLST deleteDSSSPI.py -p createDSSSPI.properties

#### The script will attempt to remove a datasource as well as the SQLAuthenticationProvider. It will use the same properties file. Upon successful script completion, you will be offered to shutdown an admin server. 

2.  Start the server; Log onto admin console.
3.  Navigate to the Authentication Directory:
    1.  Select Security Realms under Domain Structure.
    2.  Navigate to the Providers tab, as shown below:

\- Home \> Summary of Security Realms \> myrealm \> Providers \> Authentication tab

4.  Confirm absence of the KaajeeManageableAuthenticator.
    1.  When returned to the Authentication page, select and edit the DefaultAuthenticator Authentication Provider. Ensure that Control Flag is 'REQUIRED'.
5.  Restart the admin server, if any changes to the Authentication Providers has been made.
6.  Verify all Changes Have Taken Place:
    1.  Use the WebLogic console software (i.e., WebLogic Server 10.3.6 Console Login) to navigate to the following locations:
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Users tab)
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Groups tab)
    - Confirm absense of application-level users retrieved by the KaajeeManageableAuthenticator