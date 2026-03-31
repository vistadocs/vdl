---
title: InterSystems Health Connect - HL7 Messaging Product Operations Manual (POM) - Electronic Contract Management System (eCMS)
doc_type: POM
doc_label: Production Operations Manual
doc_layer: plain
doc_subject: 
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: - [Revision History](#revision-history) - [HC-HL7MessagingPOM-Master.docx](#hc-hl7messagingpom-masterdocx) - [Review eCMS System Default Settings](#review-ecms-system-default-settings) - [Management Portal  Ensemble  Configure  System Default Settings](#management-portal-ensemble-configure-system
audience: 
keywords: 
  - table
  - ecms
  - strong
  - contents
  - operation
  - class
  - settings
  - business
  - message
  - style
page_count: 0
word_count: 1341
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc-hl7_messaging_pom-ecms-signed.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc-hl7_messaging_pom-ecms-signed.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
  - [HC-HL7MessagingPOM-Master.docx](#hc-hl7messagingpom-masterdocx)
- [Review eCMS System Default Settings](#review-ecms-system-default-settings)
  - [Management Portal  Ensemble  Configure  System Default Settings](#management-portal-ensemble-configure-system-default-settings)
- [Review eCMS Router Lookup Settings](#review-ecms-router-lookup-settings)
  - [Management Portal  Ensemble  Configure  Data Lookup Tables](#management-portal-ensemble-configure-data-lookup-tables)
  - [Open  InboundRouter  eCMS](#open-inboundrouter-ecms)
- [eCMS Troubleshooting](#ecms-troubleshooting)
  - [eCMS Common Issues and Resolutions](#ecms-common-issues-and-resolutions)
- [eCMS Rollback Procedures](#ecms-rollback-procedures)
- [eCMS Enterprise Business Process Logic (BPL)](#ecms-enterprise-business-process-logic-bpl)
- [eCMS Regional Business Process Logic (BPL)](#ecms-regional-business-process-logic-bpl)
  - [eCMS Message Samples](#ecms-message-samples)
  - [eCMS Alerts](#ecms-alerts)
- [eCMS Approval Signatures](#ecms-approval-signatures)
<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/20/2018</td>
<td>0.2</td>
<td><p>VA Tech Edit Review:</p>
<ul>
<li><p>Renamed document file.</p></li>
<li><p>Added a Revision History section to track edits to this document.</p></li>
<li><p>Updated Introductory text to explain this document and how it will be incorporated in to the Master POM.</p></li>
<li><p>Updated styles and formatting to match the Master POM.</p></li>
<li><p>Modified content throughout to refer to figures and tables as appropriate.</p></li>
<li><p>Added alternate text to all images and verified document is Section 508 conformant.</p></li>
<li><blockquote>
<p>Some questions/comments remain, and Approval section is incomplete.</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>VA Tech Writer: REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/19/2018</td>
<td>0.1</td>
<td>Initial document.</td>
<td>Halfaker and Associates: REDACTED</td>
</tr>
</tbody>
</table>
> This document contains content specific to the Electronic Contract Management System (eCMS) application that is currently migrating messaging from the Vitria Interface Engine (VIE) to InterSystems HL7 Health Connect (HealthShare).
> Section [<u>6.3</u>](#6.3_Electronic_Contract_Management_Syste) in this document will be added as a sub-section entry to Section 6, “Appendix A— Products Migrating from VIE to HL7 Health Connect” in the FileMan 24 (FM24) project Master Production Operations Manual (POM):

## HC-HL7_Messaging_POM-Master.docx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *The “Pharmacy Automated Dispensing Equipment (PADE)” content is found in Section 6.1 in the FM24 project Master POM (HC-HL7_Messaging_POM-Master.docx).*

> *The Outpatient Pharmacy Automation Interface (OPAI) content is found in Section 6.2 in the FM24 project Master POM (HC-HL7_Messaging_POM-Master.docx).*

3.  <span id="6.3_Electronic_Contract_Management_Syste" class="anchor"></span>Electronic Contract Management System (eCMS)

> This section contains content specific to the Electronic Contract Management System (eCMS). It describes how to maintain the components of the Health Level Seven (HL7) Health Connect Production as well as how to troubleshoot problems that might occur with eCMS in production. The intended audience for this document is the Office of Information and Technology (OIT) teams responsible for hosting and maintaining the eCMS system after production release.

# Review eCMS System Default Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to access the eCMS system default settings and review the current settings. At the time of production deployment, these settings will be configured and should not change. Post-production, they should be used for possible troubleshooting. For example, if a Veterans Health Information Systems and Technology Architecture (VistA) site Internet Protocol (IP) address is changed for some reason, the setting in the table in [<u>Figure 2</u>](#_bookmark1) will need to be adjusted and reapplied to the settings for the outbound Operation.

> To access the “System Default Settings” page, do the following:

## Management Portal  Ensemble  Configure  System Default Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The System Default Settings maps an outbound business Operation to the domain name (FQDN) or IP address to which the message will be sent. These values are used to apply the default values to the IP address on the business Operation settings. On the Enterprise instance, there will be an entry for each Regional instance and the enterprise eCMS production instance. On a Regional instance, there will be a full list of VistA instances in the region, and one entry for the Enterprise HC instance labeled as eCMS Enterprise. The full mapping of outbound Operations to FQDNs or IP Addresses for each Health Connect instance are stored in a secure SharePoint location, accessible to production operations staff.

> Figure 1: System Default Settings—Enterprise HC

REDACTED

> <span id="_bookmark1" class="anchor"></span>Figure 2: System Default Settings—Regional HC

> REDACTED

# Review eCMS Router Lookup Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The eCMS router lookup settings map a destination facility identification from an HL7 message to an outbound business Operation. [<u>Figure 3</u>](#_bookmark2) and [<u>Figure 4</u>](#_bookmark3) are samples of appropriate entries used by eCMS routers on the Enterprise and Regional Health Connect instances, respectively. The full mapping of destination facilities to outbound Operations for each Health Connect instance are stored in a secure SharePoint location, accessible to production operations staff.

> To review the eCMS router lookup settings, do the following:

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/001.png)Use the Management Portal (MP) to navigate to the “Data Lookup Tables” page:

## Management Portal  Ensemble  Configure  Data Lookup Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/002.png)Select the following:

## Open  InboundRouter  eCMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/003.png)Select the OK button.

> On the Enterprise Health Connect instance, the router pulls the destination facility identifier (segment 6.2 in the message header) to determine the name of the outbound Operation. On the Enterprise instance, all possible destination facilities *must* be listed, and are routed to their assigned Regional Health Connect instance, see [<u>Figure 3</u>](#_bookmark2) for a sample for illustration.

> <span id="_bookmark2" class="anchor"></span>Figure 3: Lookup Tables—Enterprise

> REDACTED

> On the Regional Health Connect instance, a message received from the Enterprise Health Connect instance contains a destination facility identifier in segment MSH-6.2 of the message header. The router maps that identifier to the key in [<u>Figure 4</u>,](#_bookmark3) and uses the value to determine the outbound Operation that routes the message to the appropriate VistA instance.

> <span id="_bookmark3" class="anchor"></span>Figure 4: Lookup Tables—Regional

REDACTED

# eCMS Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For troubleshooting eCMS:

- Enter an Incident or Request ticket in ITSM ServiceNow system.
- Contact Tier 2 or the VA Enterprise Service Desk (ESD)
- Contact InterSystems Support

## eCMS Common Issues and Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table 1: eCMS—Common Issues and Resolutions

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 37%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Issue</strong></th>
<th><strong>Common Resolution</strong></th>
<th><strong>Support Contact</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VistA instances are <em>not</em> able to send messages to eCMS.</td>
<td>Check the ensure the Regional Health Connect instance for the VistA systems has the production started, and inbound services enabled.</td>
<td>HC Operations</td>
</tr>
<tr class="even">
<td>eCMS is <em>not</em> receiving messages.</td>
<td>Ensure the Enterprise Health Connect instance has the eCMS production started, and all services, operations, and processes are enabled.</td>
<td>HC Operations</td>
</tr>
<tr class="odd">
<td>VistA systems are <em>not</em> receiving messages from eCMS, but they are able to send messages.</td>
<td>Ensure all outbound Operations “ToVista*” are enabled in both the Enterprise and Regional Health Connect instances.</td>
<td>HC Operations</td>
</tr>
<tr class="even">
<td><p>Isolated VistA instances are <em>not</em></p>
<p>receiving messages from eCMS.</p></td>
<td><p>Ensure that the <strong>FQDN</strong> for the outbound Operation in the System Default settings for the subject VistA is correct</p>
<p>Ensure the outbound Operation for the subject VistA is enabled.</p>
<p>Ensure the Lookup Table entry for the subject destination facility is correct in both the Regional and Enterprise HC instances.</p></td>
<td>HC Operations</td>
</tr>
<tr class="odd">
<td>What is the contingency plan if Health Connect goes down?</td>
<td><p>For all of the applications that are supported by Health Connect (HC), if a site has an issue they think is related to HC, they can open a <u>YourIT (ServiceNow)</u> ticket.</p>
<p>In the case of eCMS, they should open a High Priority <u>YourIT</u> <u>(ServiceNow)</u> ticket by calling the VA <u>Enterprise Service Desk (ESD)</u>.</p>
<p>Request that the help desk get a member of the HC National Admin</p></td>
<td>Health Connect Support (<strong>HSH EO HealthShare Administration</strong>) — Submit <u>YourIT</u> <u>(ServiceNow)</u> Ticket</td>
</tr>
</tbody>
</table>

| Issue | Common Resolution                                              | Support Contact |
|-----------|--------------------------------------------------------------------|---------------------|
|           | team on the phone 24/7. eCMS is supported in the same way as OPAI. |                     |

# eCMS Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For back-out and rollback procedures, see the *eCMS Deployment, Installation, Back-Out, and Roll Back Guide* (HC_eCMS_DIBRG.docx) document.

# eCMS Enterprise Business Process Logic (BPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workflow logic to route HL7 messages from the Enterprise HC to the Regional HC based on Receiving Facility ID:

1.  Get Receiving Facility. Assign the MSH:ReceivingFacility.universalID, which is piece

> 6.2 from the MSH header, to receivingSystem.

2.  Look up Business Operation. A sql statement Lookup Business Operation gets the receivingBusinessOperation value from the InboundRouter table based on the receivingSystem value from the prior step (6.3.5 step 1). This will return the Business Operation of the Regional HC instance for the VistA to which the message is addressed.

> Figure 5: Sample SQL Statement

3.  If the condition to check receivingBusinessOperation value is empty:
    1.  If receivingBusinessOperation is NULL, send an alert to the support group (OIT EPMO TRS EPS HSH HealthConnect Administration).
    2.  Move the message to the BadMessageHandler.
    3.  The support group needs to check the MSH segment of the message and verify that an entry for the Universal Id in the MSH segment exists in the Outbound Router Table and maps to a corresponding Operation value (see [<u>Figure 3</u>](#_bookmark2)).

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/004.png)If condition to check the Operation value in Outbound Router is Enabled:

1.  If Operation is *not*Enabled send out an alert to the support group, to enable the Operation and continue to step 5.
2.  If Operation is Enabled continue to step 5.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/005.png)Send to Outbound Operator. Send the HL7 message to the Configured Business Operation.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/006.png)Figure 6: Business Process Logic—Enterprise

# eCMS Regional Business Process Logic (BPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/007.png)Workflow logic to route HL7 messages on a Regional HC server based on Receiving Facility ID: Get Receiving Facility. Assign the MSH:ReceivingFacility.universalID, which is piece

> 6.2 from the MSH header, to receivingSystem.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/008.png)Look up Business Operation. A sql statement Lookup Business Operation gets the receivingBusinessoperation value from the InboundRouter table based on the receivingSystem value from step 1. This returns the Business Operation of the VistA instance to which the message is addressed.

> Figure 7: Sample SQL Statement

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/009.png)If condition to check receivingBusinessOperation value is empty:

1.  If receivingBusinessOperation is NULL, send an alert to the support group (OIT EPMO TRS EPS HSH HealthConnect Administration) and move the message to the BadMessageHandler. The support group needs to check the MSH segment of the message and verify that an entry for the Universal Id in the MSH segment exists in the Outbound Router Table and maps to a corresponding Operation value (see [<u>Figure 4</u>](#_bookmark3)).
2.  If receivingBusinessOperation is *not* empty continue to step 4.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/010.png)If condition to check the Operation value in Outbound Router is Enabled:

1.  If Operation is *not*Enabled send out an alert to the support group, to enable the Operation and continue to step 5.
2.  If Operation is Enabled continue to step 5.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/011.png)Send to Outbound Operator. Send the HL7 message to the Configured Business Operation.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/012.png)Figure 8: Business Process Logic—Regional

## eCMS Message Samples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 9: eCMS—Message Sample to eCMS from VistA

> Figure 10: eCMS—Message Sample to VistA from eCMS

## eCMS Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table 2: eCMS—Alerts

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Alert</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Automatically Resend HL7 Message</td>
<td><p>Health Connect shall place the HL7 message in a queue and automatically resend the message for the system configured time period until an Accept Acknowledgment commit response is received:</p>
<ul>
<li><p><strong>CA</strong>—Commit Accept</p></li>
<li><p><strong>CE</strong>—Commit Error</p></li>
<li><p><strong>CR</strong>—Commit Reject</p></li>
</ul>
<p>This setting can be found on the business operation by going to</p>
<p><strong>Settings</strong> tab and updating <strong>Failure Timeout</strong>.</p>
<p>In this situation, the business operation should turn purple (see <a href="#_bookmark4">Figure 11</a>).</p></td>
</tr>
</tbody>
</table>

| Alert                                            | Description                                                                                                                                                                                                                                                                             |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Send Email Alert(s) that System or Device Offline    | Health Connect sends designated operations support personnel email alert(s) identifying the system or device that is offline based on the configured system parameter for frequency to send email alerts.                                                                                   |
| Send Email Alert Message Queue Size Exceeded         | Health Connect sends an email alert to designated Health Connect operations support personnel when the message send queue exceeds the configurable message queue limit. This setting can be found on the business operation by going to settings tab and updating Queue Count Alert.        |
| Send Email Alert When Commit Reject Message Received | Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit reject message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions. |
| Send Email Alert When Commit Error Message Received  | Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit error message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions.  |

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/013.png)<span id="_bookmark4" class="anchor"></span>Figure 11: HL7 Health Connect—Production Configuration Legend: Status Indicators

# eCMS Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The signatures in this section indicate the approval of the HL7 InterSystems Health Connect Production Operations Manual (POM) for the Electronic Contract Management System (eCMS) application.

> ![](intersystems-health-connect-hl7-messaging-product-operations-manual-pom-electron/014.png) NOTE: Digital signatures will only be added to the PDF version of the Microsoft<sup>®</sup> Word document (i.e., HC-HL7_Messaging_POM-eCMS-Signed.pdf).

REDACTED

REDACTED

REDACTED