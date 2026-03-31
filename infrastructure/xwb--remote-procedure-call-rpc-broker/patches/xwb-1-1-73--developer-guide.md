---
title: XWB*1.1*73 Developer's Guide
doc_type: DG
doc_label: Developer Guide
doc_layer: patch
doc_subject: Developer's Guide
app_code: XWB
app_name: Remote Procedure Call (RPC) Broker
section: INF
app_status: active
pkg_ns: XWB
patch_ver: 1.1
patch_id: XWB*1.1*73
group_key: "XWB:XWB:1.1"
file_numbers: []
security_keys: []
menu_options: 21
description: 
audience: 
keywords: 
  - table
  - property
  - contents
  - class
  - broker
  - server
  - component
  - strong
  - application
  - span
page_count: 0
word_count: 63779
section_count: 71
table_count: 48
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_dg_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_dg_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

---
title: |
  RPC Broker 1.1

  Developer’s Guide (REDACTED)
---

![](xwb-1-1-73-developer-s-guide/001.png)

September 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="revision_history" class="anchor"></span>Revision History

Documentation Revisions

<table>
<caption><p><span id="_Ref446337151" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/15/2021</td>
<td>6.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*73 (Client-Side only; no VistA M Server updates):</p>
<ul>
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Section <u>1.4.1</u>.</p></li>
<li><p>Corrects the following issues:</p></li>
</ul>
<ul>
<li><p>Ensures the data placed into the <strong>Brokerx.User.Division</strong> field is correctly formatted.</p></li>
<li><p>Redesigned the method of certificate processing; it automatically selects the user's Authentication certificate, eliminating the need for the user to select from a list of certificates.</p></li>
</ul>
<ul>
<li><p>Added the <strong>ShowCertDialog</strong> property. Updated the following:</p></li>
</ul>
<ul>
<li><p><u>Table 4: TCCOWRPCBroker Component—All Properties (listed alphabetically)</u>.</p></li>
<li><p>Section <u>2.6.50</u>.</p></li>
</ul>
<ul>
<li><p>Deleted Section 1.7, "Online Help," and references to <strong>.chm</strong>/online help, since the online help is <em>not</em> being released with RPC Broker Patch XWB*1.1*73.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*73 BDK</strong></p></li>
</ul></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>12/1/2020</td>
<td>5.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*72 (Client-Side only; no VistA M Server updates):</p>
<ul>
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Sections <u>1.3</u> and <u>1.4.2</u>.</p></li>
<li><p>Corrects the following issues:</p></li>
</ul>
<ul>
<li><p>Ensures the DIVISION field is properly set.</p></li>
<li><p>Addresses Hints and Warnings along with many of the memory leaks.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*72 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>05/06/2020</td>
<td>4.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*71 (Client-Side only; no VistA M Server updates):</p>
<ul>
<li><p>Added Section <u>1.4.1</u>, “<u>XWB*1.1*71</u>.”</p></li>
<li><p>Updated supported Delphi versions to: XE8, 10.0, 10.1, 10.2, and 10.3: Sections <u>1.3</u>, <u>1.4.3</u>.</p></li>
<li><p>Corrected broken links in Section <u>3.7.8</u>.</p></li>
<li><p>Updated “Caution” note for the reference <strong>PType</strong> in <u>Table 11</u>, <u>Table 14</u>, and <u>Table 61</u>.</p></li>
<li><p>Reformatted all references to file and field name numbers throughout.</p></li>
<li><p>Updated API formatting to synchronize with online APIs.</p></li>
<li><p>Updated document to follow current documentation standards and style guidelines.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*71 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>02/15/2017</td>
<td>3.0</td>
<td><p>Tech Edits based on release of RPC Broker Patch XWB*1.1*65:</p>
<ul>
<li><p>Reformatted document to follow current documentation standards and style formatting requirements.</p></li>
<li><p>Added Section <u>1.1.1</u>.</p></li>
<li><p>Updated Step 2 for 2-factor authentication (2FA) and BSE “GUI Developer Issues” in Section <u>1.1.2</u>.</p></li>
<li><p>Updated Section <u>1.3</u> for IPv4/IPv6 support, 2-factor authentication, renamed XWBHash Unit, and current Delphi software version support. Also, added “<strong>TXWBSSOiToken</strong>” to the list of components.</p></li>
<li><p>Restructured Section <u>1.4</u> to now list changes by BDK patch release. Updated the following content in those sections for Patch XWB*1.1*65:</p></li>
</ul>
<ul>
<li><p>Caution Note for 2-factor authentication.</p></li>
<li><p>New/Modified components.</p></li>
<li><p>Current Delphi software support and 2-factor authentication.</p></li>
<li><p>New library methods</p></li>
<li><p>New properties.</p></li>
<li><p>Modified type.</p></li>
</ul>
<ul>
<li><p>Updated Section <u>1.5.2</u> for currently supported Delphi software version.</p></li>
<li><p>Updated Section <u>1.6.5</u> for support of three types of silent login.</p></li>
<li><p>Updated Section <u>2.1.1.3</u>; clarified SSO/UC-aware and capable of CCOW single sign-on (SSO).</p></li>
<li><p>Updated Section <u>2.1.3.4</u>.</p></li>
<li><p>Updated patch reference in Section <u>2.1.3.5</u>.</p></li>
<li><p>Changed “Using clause” to “Uses clause” in Section <u>2.2.6.2</u>.</p></li>
<li><p>Added the “XWBSSOi Unit” and renamed “Hash Unit” to “XWBHash Unit” in Section <u>2.3</u> and moved “XWBHash Unit” to Section <u>2.3.10</u>.</p></li>
<li><p>Added Section <u>2.3.11</u>, “<u>XWBSSOi Unit</u>.”</p></li>
<li><p>Added the following properties to <u>Table 4</u>:</p></li>
</ul>
<ul>
<li><p><strong>SecurityPhrase</strong> Property</p></li>
<li><p><strong>SSHHide</strong> Property</p></li>
<li><p><strong>SSHport</strong> Property</p></li>
<li><p><strong>SSHpw</strong> Property</p></li>
<li><p><strong>SSHUser</strong> Property</p></li>
<li><p><strong>SSOiToken</strong> Property</p></li>
<li><p><strong>SSOiSECID</strong> Property</p></li>
<li><p><strong>SSOiADUPN</strong> Property</p></li>
<li><p><strong>SSOiLogonName</strong> Property</p></li>
<li><p><strong>UseSecureConnection</strong> Property</p></li>
</ul>
<ul>
<li><p>Added the following properties to <u>Table 6</u>:</p></li>
</ul>
<ul>
<li><p><strong>SSOiToken</strong> Property</p></li>
<li><p><strong>SSOiSECID</strong> Property</p></li>
<li><p><strong>SSOiADUPN</strong> Property</p></li>
<li><p><strong>SSOiLogonName</strong> Property</p></li>
</ul>
<ul>
<li><p>Added Section <u>2.1.5</u>, “<u>TXWBSSOiToken Component</u>.”</p></li>
<li><p>Added “Caution” note for the reference <strong>PType</strong> in <u>Table 11</u>, <u>Table 14</u>, and <u>Table 61</u>.</p></li>
<li><p>Added the following new properties:</p></li>
</ul>
<ul>
<li><p><u>SSOiADUPN Property (TRPCBroker Component)</u></p></li>
<li><p><u>SSOiADUPN Property (TXWBSSOiToken Component)</u></p></li>
<li><p><u>SSOiLogonName Property (TRPCBroker Component)</u></p></li>
<li><p><u>SSOiLogonName Property (TXWBSSOiToken Component)</u></p></li>
<li><p><u>SSOiSECID (TRPCBroker Component)</u></p></li>
<li><p><u>SSOiSECID Property (TXWBSSOiToken Component)</u></p></li>
<li><p><u>SSOiToken Property (TRPCBroker Component)</u></p></li>
<li><p><u>SSOiToken Property (TXWBSSOiToken Component)</u></p></li>
</ul>
<ul>
<li><p>Removed Note reference to the example in Sections <u>2.6.32.3</u>, <u>2.6.71.3</u>, <u>7.16.2.1</u>, and <u>7.16.2.2</u>; those sample files no longer distributed.</p></li>
<li><p>Modified/Renamed Section <u>4</u>.</p></li>
</ul>
<ul>
<li><p>Added new RPC Broker APIs Section <u>4.1</u>.</p></li>
<li><p>Moved content and added Section <u>4.2</u>.</p></li>
</ul>
<ul>
<li><p>Updated the option parameter description to clarify it is an “encrypted name” in Section <u>4.1.5</u>.</p></li>
<li><p>Added the following new RPCs to Section <u>4.2</u>:</p></li>
</ul>
<ul>
<li><p><u>XWB CREATE CONTEXT</u></p></li>
<li><p><u>XWB GET BROKER INFO</u></p></li>
<li><p><u>XWB IM HERE</u></p></li>
</ul>
<ul>
<li><p>Updated Section <u>4.2.9.1</u> regarding Windows registry entries.</p></li>
<li><p>Added Section <u>5</u>, “<u>Broker Security Enhancement (BSE)</u>.” Consolidating all developer-related content from the standalone <em>Broker Security Enhancement (BSE) Supplement to Patch: XWB*1.1*45 &amp; XU*8.0*404</em> document into the <em>RPC Broker Developer’s Guide</em>. Specifically, content taken from Sections 3-6.<br />
<br />
<strong>NOTE:</strong> Once all content is transferred from the BSE standalone document into the appropriate RPC Broker documents, the <em>Broker Security Enhancement (BSE) Supplement to Patch: XWB*1.1*45 &amp; XU*8.0*404</em> will be deleted and removed from the VDL.</p></li>
<li><p>Changed references from “Borland Delphi” to “Embarcadero Delphi,” removed Note referring to CAPRI, and updated Steps 1-2, removed old Step 3 (including RPC Broker login components) and old Step 8 (recompiling application), updated new Steps 3-7 in Section <u>5.3</u>.</p></li>
<li><p>Updated Section <u>6.2</u>.</p></li>
<li><p>Deleted “BAPI32.DLL not able to support SSH” Note from Section <u>8.1</u>.</p></li>
<li><p>Added the MySsoToken Function to <u>Table 40</u>.</p></li>
<li><p>Updated Section <u>8.3.2</u>. Also, deleted Section 8.7; it was a duplicate of Section <u>8.3.2</u>.</p></li>
<li><p>Added Section <u>8.7</u>, “<u>MySsoToken Function</u>.”</p></li>
<li><p>Added “SAML” and “XML” to the Glossary, <u>Table 66</u>.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*65 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>04/28/2016</td>
<td>2.0</td>
<td><p>Tech Edits based on release of RPC Broker Patch XWB*1.1*60 (released 06/11/2015):</p>
<ul>
<li><p>Reformatted document to follow current documentation standards and style formatting requirements.</p></li>
<li><p>Updated the “Orientation” section.</p></li>
<li><p>Updated Section 1.3.</p></li>
<li><p>Updated Section 1.4.2.1 for deprecated (removed) components.</p></li>
<li><p>Updated Section 1.4.2.2 for added or modified components.</p></li>
<li><p>Updated Section 1.4.4 for added functionality.</p></li>
<li><p>Updated Section 1.4.5.2 for modified methods.</p></li>
<li><p>Updated Section 1.4.6.1 for deprecated (removed) properties.</p></li>
<li><p>Added Figure 1 caption.</p></li>
<li><p>Removed deprecated properties from Table 4, Table 6, Table 7, and Table 9.</p></li>
<li><p>Modified command line parameter in Section 2.1.3.4.</p></li>
<li><p>Updated Sections 2.4.1.4.1 and 2.4.1.4.2.</p></li>
<li><p>Updated Section 2.6.52.4.</p></li>
<li><p>Modified property references in Sections 2.6.55.3 and 2.6.56.3.</p></li>
<li><p>Updated Figure 53.</p></li>
<li><p>Removed malfunction note in Section 4.2.7.1.</p></li>
<li><p>Updated Figure 59.</p></li>
<li><p>Removed Winsock reference note from Section 5.4.</p></li>
<li><p>Removed caution note regarding writing to Windows registry in Section 6.17.</p></li>
<li><p>Updated Section 7.1.</p></li>
<li><p>Removed references to “<strong>DSM</strong>” and <strong>ZDCEBUG</strong> throughout.<br />
<br />
Also, deleted Section 5.7, “Identifying the Listener Process on the Server” and Section 5.8, “Identifying the Handler Process on the Server,” since they referred to DSM commands and processes.</p></li>
<li><p>Updated help file references from “BROKER.HLP” to “<strong>Broker_1_1.chm</strong>” throughout.</p></li>
<li><p>Updated references to show RPC Broker Patch XWB*1.1*60 supports Delphi XE7, XE6, XE5, and XE4 throughout.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*60 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>04/16/2014</td>
<td>1.2</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Added links to new properties added with Patch XWB*1.1*50 in Section Properties—Added or Modified.</p></li>
<li><p>Corrected sort order of properties in Table 6.</p></li>
<li><p>Added the “RunTime only” icon to the <strong>Socket</strong> property (read-only) and <strong>User</strong> property throughout.</p></li>
<li><p>Corrected the <strong>Assign</strong> procedure link in Section 2.2.3.4.</p></li>
<li><p>Added bullet list of Units described in this document in Section 2.3.</p></li>
<li><p>Deleted <strong>TMult</strong> class from the list in Section 2.3.8.1.</p></li>
<li><p>Made other minor format and content updates.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>04/14/2014</td>
<td>1.1</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Updated the “Definitions” section for units, classes, components, and routines.</p></li>
<li><p>Updated the “About this Version of the RPC Broker” section.</p></li>
<li><p>Updated the order of the classes in the “Classes—Added” section.</p></li>
<li><p>Updated the “Components—Added or Modified” section.</p></li>
<li><p>Changed references from “TVCEdit Unit” to “VCEdit Unit” throughout.</p></li>
<li><p>Updated the “Properties—Added or Modified” section for properties added with XWB*1.1*50.</p></li>
<li><p>Updated Section 2.1.1.7 for reference to Sample directory.</p></li>
<li><p>Updated “TContextorControl Component” section. Added Parent class, Unit, and Description sub-sections.</p></li>
<li><p>Updated Table 6 with duplicate properties from TCCOWRPCBroker, because they have been made available within the TRPCBroker component.</p></li>
<li><p>Updated Section 2.1.3.8 for CCOW methods added to the TRPCBroker Component.</p></li>
<li><p>Changed references to correct Sample directory throughout:<br />
<br />
<strong>BDK32\Samples\BrokerEx</strong><br />
<br />
Also, changed references to the BDK32\Samples\SharedRPCBroker directory, since these were not included with XWB*1.1*50.</p></li>
<li><p>Updated Section 2.2.1.3.</p></li>
<li><p>Updated Section 2.2.1.4:</p></li>
</ul>
<ul>
<li><p>Changed <strong>Assign</strong> method (<strong>TMult Class</strong>) to <strong>Assign</strong> procedure (<strong>TMult Class</strong>).</p></li>
<li><p>Changed <strong>Order</strong> method to <strong>Order</strong> function throughout.</p></li>
<li><p>Changed <strong>Position</strong> method to <strong>Position</strong> function throughout.</p></li>
<li><p>Changed <strong>Subscript</strong> method to <strong>Subscript</strong> function throughout.</p></li>
</ul>
<ul>
<li><p>Updated Section 2.2.3.3 title and added the <strong>ParamArray</strong> property.</p></li>
<li><p>Updated Section 2.2.3.4 title and <strong>ParamArray</strong> property.</p></li>
<li><p>Updated Table 7; added the <strong>NTToken</strong> property.</p></li>
<li><p>Updated description in Section 2.2.6.2.</p></li>
<li><p>Added Caution note to Section 2.3.</p></li>
<li><p>Updated Encryption and Decryption Function links in Section 2.3.2.1.</p></li>
<li><p>Added description in Section 2.3.4.</p></li>
<li><p>Added description and Caution note in Section 2.3.5.</p></li>
<li><p>Added IsIPAddress Function to Section 2.3.5.1.</p></li>
<li><p>Added description to Section 2.3.6.</p></li>
<li><p>Added the following methods to Section 2.3.6.1: <strong>GetSessionInfo</strong> procedure, <strong>GetUserInfo</strong> procedure, <strong>SilentLogIn</strong> function, <strong>ValidAppHandle</strong> function, <strong>ValidAVCodes</strong> function, and <strong>ValidNTToken</strong> function.</p></li>
<li><p>Added description to Section 2.3.7.</p></li>
<li><p>Added “Procedure to library methods in Section 2.3.7.1.</p></li>
<li><p>Added the “Wsockc Unit” section.</p></li>
<li><p>Removed or modified references to the BDK32\Samples\SilentSignOn directory throughout.</p></li>
<li><p>Added the “SecurityPhrase Property” section.</p></li>
<li><p>Added the following properties/sections:</p></li>
</ul>
<ul>
<li><p><strong>SSHHide</strong> Property</p></li>
<li><p><strong>SSHport</strong> Property</p></li>
<li><p><strong>SSHpw</strong> Property</p></li>
<li><p><strong>SSHUser</strong> Property</p></li>
</ul>
<ul>
<li><p>Added the “UseSecureConnection Property” section.</p></li>
<li><p>Corrected sample app name in Section 3.7.8; added “.exe” and deleted the Note.</p></li>
<li><p>Added Caution and Note to Section 4.2.3.</p></li>
<li><p>As per Keith Cox, head of the ICR team, changed all XWB “public” RPCs to “Controlled Subscription throughout to improve VistA security. Added Notes where appropriate.</p></li>
<li><p>Updated Figure 53.</p></li>
<li><p>Added Windows 7 Note to Section 4.2.7.1.</p></li>
<li><p>Added Caution to Section 4.2.8.1.</p></li>
<li><p>Deleted first reference Note in Section 4.2.12.1, since repeated with the Example.</p></li>
<li><p>Updated Table 39: Added errors 20008 - 20112.</p></li>
<li><p>Updated Figure 74.</p></li>
<li><p>Updated example in Step 2 in the “Tutorial—Step 4: Routine to List Terminal Types” section.</p></li>
<li><p>Updated Figure 81.</p></li>
<li><p>Updated example in Step 3 in the “Tutorial—Step 8: Routine to Retrieve Terminal Types” section.</p></li>
<li><p>Updated Figure 90.</p></li>
<li><p>Updated Note in Section 6.16.4.1 and 6.16.4.2.</p></li>
<li><p>Added Caution note to Section 6.17.</p></li>
<li><p>Updated references to the VB5EGCHO sample application to have been distributed with an earlier BDK.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>04/10/2014</td>
<td>1.0</td>
<td><p>Initial document:</p>
<ul>
<li><p>Content derived from the RPC Broker 1.1 online HTML help topics using RoboHelp utility.</p></li>
<li><p>Reformatted document and made sure it conforms to the current OIT National Documentations Standards.</p></li>
<li><p>Made other minor grammar and punctuation corrections throughout.</p></li>
</ul>
<p><strong>RPC Broker 1.1</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref446337151" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc82593214" class="anchor"></span>List of Figures

<span id="_Toc82593215" class="anchor"></span>List of Tables

<span id="Orientation" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the Remote Procedure Call (RPC) Broker 1.1 Development Kit (BDK) and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA).

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](xwb-1-1-73-developer-s-guide/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimer

This manual provides an overall explanation of RPC Broker and the functionality contained in RPC Broker 1.1; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](xwb-1-1-73-developer-s-guide/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](xwb-1-1-73-developer-s-guide/004.png)                    | NOTE / REF: Used to inform the reader of general information including references to additional reading material |
| ![](xwb-1-1-73-developer-s-guide/005.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information |

<span id="_Ref446337152" class="anchor"></span>Table 2: Commonly Used RPC Broker Terms

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- *\[Application Name\]*PATIENT,*\[N\]*
- *\[Application Name\]*USER,*\[N\]*

Where “*\[Application Name\]*” is defined in the Approved Application Abbreviations document and “*\[N\]*” represents the first name as a number spelled out and incremented with each new entry.

For example, in RPC Broker (XWB) test patient names would be documented as follows:

XWBPATIENT,ONE; XWBPATIENT,TWO; XWBPATIENT,14, etc.

For example, in RPC Broker (XWB) test user names would be documented as follows:

XWBUSER,ONE; XWBUSER,TWO; XWBUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xwb-1-1-73-developer-s-guide/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- The following conventions are used with regards to APIs:
- The following API types are documented:
- Supported:

This applies where any VistA application may use the attributes/functions defined by the Integration Control Registration (ICR); these are also called “Public”. An example is an ICR that describes a standard API. The package that creates/maintains the Supported Reference *must* ensure it is recorded as a Supported Reference in the ICR database. There is no need for other VistA packages to request an ICR to use these references; they are open to all by default.

- Controlled Subscription:

Describes attributes/functions that *must* be controlled in their use. The decision to restrict the Integration Control Registration (ICR) is based on the maturity of the custodian package. Typically, these ICRs are created by the requesting package based on their independent examination of the custodian package's features. For the ICR to be approved the custodian grants permission to other VistA packages to use the attributes/functions of the ICR; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package.

![](xwb-1-1-73-developer-s-guide/007.png) Private APIs are *not* documented.

- Headings for developer API descriptions (e.g., supported for use in applications and on the Database Integration Committee \[DBIC\] list) include the routine tag (if any), the caret (^) used when calling the routine, and the routine name. The following is an example:

\$\$BROKER^XWBLIB

- For APIs that take input parameter, the input parameter is labeled “required” when it is a required input parameter and labeled “optional” when it is an optional input parameter.
- For APIs that take parameters, parameters are shown in lowercase and variables are shown in uppercase. This is to convey that the parameter name is merely a placeholder; M allows you to pass a variable of any name as the parameter or even a string literal (if the parameter is *not* being passed by reference). The following is an example of the formatting for input parameters:

XGLMSG^XGLMSG(msg_type,\[.\]var\[,timeout\])

- Rectangular brackets \[\] around a parameter are used to indicate that passing the parameter is optional. Rectangular brackets around a leading period \[.\] in front of a parameter indicate that you can optionally pass that parameter by reference.
- All APIs are categorized by function. This categorization is subjective and subject to change based on feedback from the development community. In addition, some APIs could fall under multiple categories; however, they are only listed once under a chosen category.  
    
  APIs within a category are first sorted alphabetically by Routine name and then within routine name are sorted alphabetically by Tag reference. The \$\$, ^, or ^% prefixes on APIs is ignored when alphabetizing.
- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the [XUPROGMODE](#_Toc384285598) security key).

![](xwb-1-1-73-developer-s-guide/008.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](xwb-1-1-73-developer-s-guide/009.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

Commonly Used Terms

<u>Table 2</u> is a list of terms and their descriptions that you may find helpful while reading the RPC Broker documentation:

<table>
<caption><p><span id="_Toc82593668" class="anchor"></span>Table 3: Broker Client-side and Server-side Overview</p></caption>
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
<td>Client</td>
<td>A single term used interchangeably to refer to a user, the workstation (i.e., PC), and the portion of the program that runs on the workstation.</td>
</tr>
<tr class="even">
<td>Component</td>
<td><p>A software object that contains data and code. A component may or may not be visible.</p>
<p>![](xwb-1-1-73-developer-s-guide/010.png) <strong>REF:</strong> For a more detailed description, see the <em>Embarcadero Delphi for Windows User Guide</em>.</p></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>The Graphical User Interface application that is developed for the client workstation.</td>
</tr>
<tr class="even">
<td>Host</td>
<td>The term Host is used interchangeably with the term Server.</td>
</tr>
<tr class="odd">
<td>Server</td>
<td>The computer where the data and the RPC Broker remote procedure calls (RPCs) reside.</td>
</tr>
</tbody>
</table>

<span id="_Toc82593668" class="anchor"></span>Table 3: Broker Client-side and Server-side Overview

![](xwb-1-1-73-developer-s-guide/011.png) REF: For additional terms and definitions, see the “Glossary” section in this manual and other RPC Broker manuals.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xwb-1-1-73-developer-s-guide/012.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.  
  
REF: For further information, see the *RPC Broker Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xwb-1-1-73-developer-s-guide/013.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- Remote Procedure Call (RPC) Broker—VistA Client/Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language
- Object Pascal programming language.
- Object Pascal programming language/Embarcadero Delphi Integrated Development Environment (IDE)—RPC Broker

References

Readers who wish to learn more about RPC Broker should consult the following:

- *RPC Broker Release Notes*
- *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *RPC Broker Systems Management Guide*
- *RPC Broker Technical Manual*
- *RPC Broker User Guide*
- *RPC Broker Developer’s Guide* (this manual)—This document provides an overview of development with the RPC Broker.
- RPC Broker VA Intranet website.  
    
  This site provides announcements, additional information (e.g., Frequently Asked Questions \[FAQs\], advisories), documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

The RPC Broker documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=23>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Broker Overview](#broker-overview)
    - [Broker Security Enhancement (BSE) Overview](#broker-security-enhancement-bse-overview)
    - [Broker Call Steps](#broker-call-steps)
  - [Definitions](#definitions)
    - [Units](#units)
    - [Classes](#classes)
    - [Objects](#objects)
    - [Components](#components)
    - [Types](#types)
    - [Methods](#methods)
    - [Routines: Functions and Procedures](#routines-functions-and-procedures)
  - [About this Version of the RPC Broker](#about-this-version-of-the-rpc-broker)
  - [What’s New in the BDK](#whats-new-in-the-bdk)
    - [XWB\1.1\73](#xwb1173)
    - [XWB\1.1\72](#xwb1172)
    - [XWB\1.1\71](#xwb1171)
    - [XWB\1.1\65](#xwb1165)
    - [XWB\1.1\60](#xwb1160)
    - [XWB\1.1\50](#xwb1150)
    - [XWB\1.1\40](#xwb1140)
    - [XWB\1.1\35](#xwb1135)
    - [XWB\1.1\26](#xwb1126)
    - [XWB\1.1\23](#xwb1123)
    - [XWB\1.1\14](#xwb1114)
    - [XWB\1.1\13](#xwb1113)
  - [Developer Considerations](#developer-considerations)
    - [Source Code](#source-code)
    - [DesignTime and RunTime Packages](#designtime-and-runtime-packages)
    - [Resource Reuse](#resource-reuse)
    - [Component Connect-Disconnect Behavior](#component-connect-disconnect-behavior)
  - [Application Considerations](#application-considerations)
    - [Application Version Numbers](#application-version-numbers)
    - [Deferred RPCs](#deferred-rpcs)
    - [Remote RPCs](#remote-rpcs)
    - [Blocking RPCs](#blocking-rpcs)
    - [Silent Login](#silent-login)
- [RPC Broker Components, Classes, Units, Methods, Types, and Properties](#rpc-broker-components-classes-units-methods-types-and-properties)
  - [Components](#components-1)
    - [TCCOWRPCBroker Component](#tccowrpcbroker-component)
    - [TContextorControl Component](#tcontextorcontrol-component)
    - [TRPCBroker Component](#trpcbroker-component)
    - [TXWBRichEdit Component](#txwbrichedit-component)
    - [TXWBSSOiToken Component](#txwbssoitoken-component)
  - [Classes](#classes-1)
    - [TMult Class](#tmult-class)
    - [TParamRecord Class](#tparamrecord-class)
    - [TParams Class](#tparams-class)
    - [TVistaLogin Class](#tvistalogin-class)
    - [TVistaUser Class](#tvistauser-class)
    - [TXWBWinsock Class](#txwbwinsock-class)
  - [Units](#units-1)
    - [CCOWRPCBroker Unit](#ccowrpcbroker-unit)
    - [LoginFrm Unit](#loginfrm-unit)
    - [MFunStr Unit](#mfunstr-unit)
    - [RPCConf1 Unit](#rpcconf1-unit)
    - [RpcSLogin Unit](#rpcslogin-unit)
    - [SplVista Unit](#splvista-unit)
    - [TRPCB Unit](#trpcb-unit)
    - [VCEdit Unit](#vcedit-unit)
    - [Wsockc Unit](#wsockc-unit)
    - [XWBHash Unit](#xwbhash-unit)
    - [XWBSSOi Unit](#xwbssoi-unit)
  - [Methods](#methods-1)
    - [Assign Method (TMult Class)](#assign-method-tmult-class)
    - [Assign Method (TParams Class)](#assign-method-tparams-class)
    - [Call Method](#call-method)
    - [CreateContext Method](#createcontext-method)
    - [GetCCOWtoken Method](#getccowtoken-method)
    - [IsUserCleared Method](#isusercleared-method)
    - [IsUserContextPending Method](#isusercontextpending-method)
    - [lstCall Method](#lstcall-method)
    - [pchCall Method](#pchcall-method)
    - [Order Method](#order-method)
    - [Position Method](#position-method)
    - [strCall Method](#strcall-method)
    - [Subscript Method](#subscript-method)
    - [WasUserDefined Method](#wasuserdefined-method)
  - [Types](#types-1)
    - [TLoginMode Type](#tloginmode-type)
    - [TParamType](#tparamtype)
  - [Properties](#properties)
    - [AccessCode Property](#accesscode-property)
    - [BrokerVersion Property (read-only)](#brokerversion-property-read-only)
    - [CCOWLogonIDName Property (read-only)](#ccowlogonidname-property-read-only)
    - [CCOWLogonIDValue Property (read-only)](#ccowlogonidvalue-property-read-only)
    - [CCOWLogonName Property (read-only)](#ccowlogonname-property-read-only)
    - [CCOWLogonNameValue Property (read-only)](#ccowlogonnamevalue-property-read-only)
    - [CCOWLogonVpid Property (read-only)](#ccowlogonvpid-property-read-only)
    - [CCOWLogonVpidValue Property (read-only)](#ccowlogonvpidvalue-property-read-only)
    - [ClearParameters Property](#clearparameters-property)
    - [ClearResults Property](#clearresults-property)
    - [Connected Property](#connected-property)
    - [Contextor Property](#contextor-property)
    - [Count Property (TMult Class)](#count-property-tmult-class)
    - [Count Property (TParams Class)](#count-property-tparams-class)
    - [CurrentContext Property (read-only)](#currentcontext-property-read-only)
    - [DebugMode Property](#debugmode-property)
    - [Division Property (TVistaLogin Class)](#division-property-tvistalogin-class)
    - [Division Property (TVistaUser Class)](#division-property-tvistauser-class)
    - [DivList Property (read-only)](#divlist-property-read-only)
    - [DomainName Property](#domainname-property)
    - [DTime Property](#dtime-property)
    - [DUZ Property (TVistaLogin Class)](#duz-property-tvistalogin-class)
    - [DUZ Property (TVistaUser Class)](#duz-property-tvistauser-class)
    - [ErrorText Property](#errortext-property)
    - [First Property](#first-property)
    - [IsProductionAccount Property](#isproductionaccount-property)
    - [KernelLogIn Property](#kernellogin-property)
    - [Language Property](#language-property)
    - [Last Property](#last-property)
    - [ListenerPort Property](#listenerport-property)
    - [LogIn Property](#login-property)
    - [LoginHandle Property](#loginhandle-property)
    - [Mode Property](#mode-property)
    - [Mult Property](#mult-property)
    - [MultiDivision Property](#multidivision-property)
    - [Name Property](#name-property)
    - [OnFailedLogin Property](#onfailedlogin-property)
    - [OnRPCBFailure Property](#onrpcbfailure-property)
    - [Param Property](#param-property)
    - [PromptDivision Property](#promptdivision-property)
    - [PType Property](#ptype-property)
    - [RemoteProcedure Property](#remoteprocedure-property)
    - [Results Property](#results-property)
    - [RPCBError Property (read-only)](#rpcberror-property-read-only)
    - [RPCTimeLimit Property](#rpctimelimit-property)
    - [RPCVersion Property](#rpcversion-property)
    - [SecurityPhrase Property](#securityphrase-property)
    - [Server Property](#server-property)
    - [ServiceSection Property](#servicesection-property)
    - [ShowCertDialog Property](#showcertdialog-property)
    - [ShowErrorMsgs Property](#showerrormsgs-property)
    - [Socket Property (read-only)](#socket-property-read-only)
    - [Sorted Property](#sorted-property)
    - [SSHHide Property](#sshhide-property)
    - [SSHport Property](#sshport-property)
    - [SSHpw Property](#sshpw-property)
    - [SSHUser Property](#sshuser-property)
    - [SSOiADUPN Property (TRPCBroker Component)](#ssoiadupn-property-trpcbroker-component)
    - [SSOiADUPN Property (TXWBSSOiToken Component)](#ssoiadupn-property-txwbssoitoken-component)
    - [SSOiLogonName Property (TRPCBroker Component)](#ssoilogonname-property-trpcbroker-component)
    - [SSOiLogonName Property (TXWBSSOiToken Component)](#ssoilogonname-property-txwbssoitoken-component)
    - [SSOiSECID (TRPCBroker Component)](#ssoisecid-trpcbroker-component)
    - [SSOiSECID Property (TXWBSSOiToken Component)](#ssoisecid-property-txwbssoitoken-component)
    - [SSOiToken Property (TRPCBroker Component)](#ssoitoken-property-trpcbroker-component)
    - [SSOiToken Property (TXWBSSOiToken Component)](#ssoitoken-property-txwbssoitoken-component)
    - [StandardName Property](#standardname-property)
    - [Title Property](#title-property)
    - [URLDetect Property](#urldetect-property)
    - [User Property](#user-property)
    - [UseSecureConnection Property](#usesecureconnection-property)
    - [Value Property](#value-property)
    - [VerifyCode Property](#verifycode-property)
    - [VerifyCodeChngd Property](#verifycodechngd-property)
    - [Vpid Property](#vpid-property)
- [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
  - [RPC Overview](#rpc-overview)
  - [What Makes a Good RPC?](#what-makes-a-good-rpc)
  - [Using an Existing M API](#using-an-existing-m-api)
  - [Creating RPCs](#creating-rpcs)
  - [M Entry Point for an RPC](#m-entry-point-for-an-rpc)
    - [Relationship between an M Entry Point and an RPC](#relationship-between-an-m-entry-point-and-an-rpc)
    - [First Input Parameter (Required)](#first-input-parameter-required)
    - [Return Value Types](#return-value-types)
    - [Input Parameters (Optional)](#input-parameters-optional)
    - [Examples](#examples)
  - [RPC Entry in the Remote Procedure File](#rpc-entry-in-the-remote-procedure-file)
    - [REMOTE PROCEDURE (#8994) File](#remote-procedure-8994-file)
    - [Key Fields for RPC Operation](#key-fields-for-rpc-operation)
    - [RPC Version](#rpc-version)
    - [Blocking an RPC](#blocking-an-rpc)
    - [Cleanup after RPC Execution](#cleanup-after-rpc-execution)
    - [Documenting RPCs](#documenting-rpcs)
  - [Executing RPCs from Clients](#executing-rpcs-from-clients)
    - [How to Execute an RPC from a Client](#how-to-execute-an-rpc-from-a-client)
    - [RPC Security: How to Register an RPC](#rpc-security-how-to-register-an-rpc)
    - [RPC Limits](#rpc-limits)
    - [RPC Time Limits](#rpc-time-limits)
    - [Maximum Size of Data](#maximum-size-of-data)
    - [Maximum Number of Parameters](#maximum-number-of-parameters)
    - [Maximum Size of Array](#maximum-size-of-array)
    - [RPC Broker Example (32-Bit)](#rpc-broker-example-32-bit)
- [RPC Broker: Developer Tools](#rpc-broker-developer-tools)
  - [Application Programming Interface (API)](#application-programming-interface-api)
    - [Overview](#overview)
    - [\$\$BROKER^XWBLIB: Test for Broker Context](#brokerxwblib-test-for-broker-context)
    - [\$\$RTRNFMT^XWBLIB(): Change RPC Return Type](#rtrnfmtxwblib-change-rpc-return-type)
    - [CHKPRMIT^XWBSEC(): Check Permissions](#chkprmitxwbsec-check-permissions)
    - [CRCONTXT^XWBSEC(): Create Context](#crcontxtxwbsec-create-context)
    - [SET^XWBSEC(): Set the State Variable](#setxwbsec-set-the-state-variable)
  - [Functions, Methods, and Procedures](#functions-methods-and-procedures)
    - [Overview](#overview-1)
    - [XWB CREATE CONTEXT](#xwb-create-context)
    - [XWB GET BROKER INFO](#xwb-get-broker-info)
    - [XWB GET VARIABLE VALUE](#xwb-get-variable-value)
    - [XWB IM HERE](#xwb-im-here)
    - [M Emulation Functions](#m-emulation-functions)
    - [Encryption Functions](#encryption-functions)
    - [CheckCmdLine Function](#checkcmdline-function)
    - [GetServerInfo Function](#getserverinfo-function)
    - [GetServerIP Function](#getserverip-function)
    - [ChangeVerify Function](#changeverify-function)
    - [SilentChangeVerify Function](#silentchangeverify-function)
    - [StartProgSLogin Method](#startprogslogin-method)
    - [VistA Splash Screen Procedures](#vista-splash-screen-procedures)
  - [Running RPCs on a Remote Server](#running-rpcs-on-a-remote-server)
    - [Overview](#overview-2)
    - [Using Direct RPCs](#using-direct-rpcs)
    - [Using Remote RPCs](#using-remote-rpcs)
    - [Checking RPC Availability on a Remote Server](#checking-rpc-availability-on-a-remote-server)
    - [XWB ARE RPCS AVAILABLE](#xwb-are-rpcs-available)
    - [XWB IS RPC AVAILABLE](#xwb-is-rpc-available)
    - [XWB DIRECT RPC](#xwb-direct-rpc)
    - [XWB REMOTE RPC](#xwb-remote-rpc)
    - [XWB REMOTE STATUS CHECK](#xwb-remote-status-check)
    - [XWB REMOTE GETDATA](#xwb-remote-getdata)
    - [XWB REMOTE CLEAR](#xwb-remote-clear)
  - [Deferred RPCs](#deferred-rpcs-1)
    - [Overview](#overview-3)
    - [XWB DEFERRED RPC](#xwb-deferred-rpc)
    - [XWB DEFERRED STATUS](#xwb-deferred-status)
    - [XWB DEFERRED GETDATA](#xwb-deferred-getdata)
    - [XWB DEFERRED CLEAR](#xwb-deferred-clear)
    - [XWB DEFERRED CLEARALL](#xwb-deferred-clearall)
- [Broker Security Enhancement (BSE)](#broker-security-enhancement-bse)
  - [Overview: Implementing Broker Security Enhancement (BSE)](#overview-implementing-broker-security-enhancement-bse)
  - [Assumptions When Implementing BSE](#assumptions-when-implementing-bse)
  - [Step-By-Step Procedures to Implement BSE](#step-by-step-procedures-to-implement-bse)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)
  - [Debugging and Troubleshooting Overview](#debugging-and-troubleshooting-overview)
  - [How to Debug the Application](#how-to-debug-the-application)
  - [RPC Error Trapping](#rpc-error-trapping)
  - [Broker Error Messages](#broker-error-messages)
  - [EBrokerError](#ebrokererror)
    - [Unit](#unit)
    - [Description](#description)
  - [Testing the RPC Broker Connection](#testing-the-rpc-broker-connection)
  - [Client Timeout and Buffer Clearing](#client-timeout-and-buffer-clearing)
  - [Memory Leaks](#memory-leaks)
- [Tutorial](#tutorial)
  - [Tutorial: Introduction](#tutorial-introduction)
    - [Tutorial Procedures](#tutorial-procedures)
  - [Tutorial: Advanced Preparation](#tutorial-advanced-preparation)
    - [Namespacing of Routines and RPCs](#namespacing-of-routines-and-rpcs)
    - [Tutorial Prerequisites](#tutorial-prerequisites)
  - [Tutorial—Step 1: RPC Broker Component](#tutorialstep-1-rpc-broker-component)
  - [Tutorial—Step 2: Get Server/Port](#tutorialstep-2-get-serverport)
  - [Tutorial—Step 3: Establish Broker Connection](#tutorialstep-3-establish-broker-connection)
  - [Tutorial—Step 4: Routine to List Terminal Types](#tutorialstep-4-routine-to-list-terminal-types)
  - [Tutorial—Step 5: RPC to List Terminal Types](#tutorialstep-5-rpc-to-list-terminal-types)
  - [Tutorial—Step 6: Call ZxxxTT LIST RPC](#tutorialstep-6-call-zxxxtt-list-rpc)
  - [Tutorial—Step 7: Associating IENs](#tutorialstep-7-associating-iens)
  - [Tutorial—Step 8: Routine to Retrieve Terminal Types](#tutorialstep-8-routine-to-retrieve-terminal-types)
  - [Tutorial—Step 9: RPC to Retrieve Terminal Types](#tutorialstep-9-rpc-to-retrieve-terminal-types)
  - [Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC](#tutorialstep-10-call-zxxxtt-retrieve-rpc)
  - [Tutorial—Step 11: Register RPCs](#tutorialstep-11-register-rpcs)
  - [Tutorial—Using VA FileMan Delphi Components (FMDC)](#tutorialusing-va-fileman-delphi-components-fmdc)
  - [Tutorial—Source Code (Sample)](#tutorialsource-code-sample)
  - [Silent Login](#silent-login-1)
    - [Handling Divisions during Silent Login](#handling-divisions-during-silent-login)
    - [Silent Login Examples](#silent-login-examples)
  - [Microsoft Windows Registry](#microsoft-windows-registry)
- [DLL Interfaces (C, C++, Visual Basic)](#dll-interfaces-c-c-visual-basic)
  - [DLL Interface Introduction](#dll-interface-introduction)
    - [Header Files](#header-files)
    - [Sample DLL Application](#sample-dll-application)
  - [DLL Exported Functions](#dll-exported-functions)
  - [DLL Special Issues](#dll-special-issues)
    - [RPC Results from DLL Calls](#rpc-results-from-dll-calls)
    - [GetServerInfo Function and the DLL](#getserverinfo-function-and-the-dll)
  - [C DLL Interface](#c-dll-interface)
    - [C: Guidelines Overview](#c-guidelines-overview)
    - [C: Initialize—LoadLibrary and GetProcAddress](#c-initializeloadlibrary-and-getprocaddress)
    - [C: Create Broker Components](#c-create-broker-components)
    - [C: Connect to the Server](#c-connect-to-the-server)
    - [C: Execute RPCs](#c-execute-rpcs)
    - [C: Destroy Broker Components](#c-destroy-broker-components)
  - [C++ DLL Interface](#c-dll-interface-1)
    - [C++: Guidelines Overview](#c-guidelines-overview-1)
    - [C++: Initialize the Class](#c-initialize-the-class)
    - [C++: Create Broker Instances](#c-create-broker-instances)
    - [C++: Connect to the Server](#c-connect-to-the-server-1)
    - [C++: Execute RPCs](#c-execute-rpcs-1)
    - [C++: Destroy Broker Instances](#c-destroy-broker-instances)
    - [C++: TRPCBroker C++ Class Methods](#c-trpcbroker-c-class-methods)
  - [Visual Basic DLL Interface](#visual-basic-dll-interface)
    - [Visual Basic: Guidelines Overview](#visual-basic-guidelines-overview)
    - [Visual Basic: Initialize](#visual-basic-initialize)
    - [Visual Basic: Create Broker Components](#visual-basic-create-broker-components)
    - [Visual Basic: Connect to the Server](#visual-basic-connect-to-the-server)
    - [Visual Basic: Execute RPCs](#visual-basic-execute-rpcs)
    - [Visual Basic: Destroy Broker Components](#visual-basic-destroy-broker-components)
  - [MySsoToken Function](#myssotoken-function)
    - [Declarations](#declarations)
    - [Return Value](#return-value)
    - [Examples](#examples-1)
  - [RPCBCall Function](#rpcbcall-function)
    - [Declarations](#declarations-1)
    - [Parameter Description](#parameter-description)
    - [Examples](#examples-2)
  - [RPCBCreate Function](#rpcbcreate-function)
    - [Declarations](#declarations-2)
    - [Return Value](#return-value-1)
    - [Examples](#examples-3)
  - [RPCBCreateContext Function](#rpcbcreatecontext-function)
    - [Declarations](#declarations-3)
    - [Return Value](#return-value-2)
    - [Parameter Description](#parameter-description-1)
    - [Examples](#examples-4)
  - [RPCBFree Function](#rpcbfree-function)
    - [Declarations](#declarations-4)
    - [Parameter Description](#parameter-description-2)
    - [Examples](#examples-5)
  - [RPCBMultItemGet Function](#rpcbmultitemget-function)
    - [Declarations](#declarations-5)
    - [Parameter Description](#parameter-description-3)
    - [Examples](#examples-6)
  - [RPCBMultPropGet Function](#rpcbmultpropget-function)
    - [Declarations](#declarations-6)
    - [Parameter Description](#parameter-description-4)
    - [Examples](#examples-7)
  - [RPCBMultSet Function](#rpcbmultset-function)
    - [Declarations](#declarations-7)
    - [Parameter Description](#parameter-description-5)
    - [Examples](#examples-8)
  - [RPCBMultSortedSet Function](#rpcbmultsortedset-function)
    - [Declarations](#declarations-8)
    - [Parameter Description](#parameter-description-6)
    - [Examples](#examples-9)
  - [RPCBParamGet Function](#rpcbparamget-function)
    - [Declarations](#declarations-9)
    - [Parameter Description](#parameter-description-7)
    - [Examples](#examples-10)
  - [RPCBParamSet Function](#rpcbparamset-function)
    - [Declarations](#declarations-10)
    - [Parameter Description](#parameter-description-8)
    - [Examples](#examples-11)
  - [RPCBPropGet Function](#rpcbpropget-function)
    - [Declarations](#declarations-11)
    - [Examples](#examples-12)
  - [RPCBPropSet Function](#rpcbpropset-function)
    - [Declarations](#declarations-12)
    - [Examples](#examples-13)
The RPC Broker is a client/server system within Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) environment. It enables client applications to communicate and exchange data with VistA M Servers.
This manual describes the development features of the RPC Broker. The emphasis is on using the RPC Broker in conjunction with Delphi software. However, the RPC Broker supports other development environments.
The manual provides a complete reference for development with the RPC Broker. For an overview of development with the RPC Broker components, see the *RPC Broker User Guide*.
This manual is intended for the VistA development community and system administrators. A wider audience of technical personnel engaged in operating and maintaining VA software might also find it useful as a reference.
The following topics are discussed in this section:
- <u>Broker Overview</u>
- <u>Broker Security Enhancement (BSE) Overview</u>
- <u>Broker Call Steps</u>
- <u>Definitions</u>
- <u>About this Version of the RPC Broker</u>
- <u>What’s New in the BDK</u>
- <u>Developer Considerations</u>
- <u>Application Considerations</u>
![](xwb-1-1-73-developer-s-guide/014.png) REF: For the latest RPC Broker product information, see the RPC Broker VA Intranet Website.

## Broker Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker is a bridge connecting the application front-end on the client workstation (e.g., Delphi-based GUI applications) to the M-based data and business rules on the VistA M Server.

<table>
<caption><p><span id="_Ref384102278" class="anchor"></span>Table 4: TCCOWRPCBroker Component—All Properties (listed alphabetically)</p></caption>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Client Workstation: RPC Broker</th>
<th>VistA M Server: RPC Broker</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Manages the connection to the client workstation.</p></li>
</ul>
<p>![](xwb-1-1-73-developer-s-guide/015.png) <strong>REF:</strong> For details, see the <em>RPC Broker Systems Management Guide</em>.</p>
<ul>
<li><p>The RPC Broker components allow Delphi-based applications to make RPCs to the server.</p></li>
<li><p>The Broker Dynamic Link Library (DLL) provides support for Commercial-Off-The-Shelf (COTS)/HOST client/server software.</p></li>
</ul></td>
<td><ul>
<li><p>Manages the connection to the client.</p></li>
</ul>
<p>![](xwb-1-1-73-developer-s-guide/016.png) <strong>REF:</strong> For details, see the <em>RPC Broker Systems Management Guide</em>.</p>
<ul>
<li><p>Authenticates client workstation.</p></li>
<li><p>Authenticates user.</p></li>
<li><p>Manages RPCs from the client, executes the M code, and passes back return values.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref384102278" class="anchor"></span>Table 4: TCCOWRPCBroker Component—All Properties (listed alphabetically)

The RPC Broker frees GUI developers from the details of the client-server connection and allows them to concentrate executing operations on the VistA M Server.

### Broker Security Enhancement (BSE) Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some VistA application users require access to data located at remote sites at which the users:

- Do *not* have assigned Access and Verify codes.
- Have *not* been entered into the NEW PERSON (#200) file by system administrators.
- Want to avoid having multiple Access/Verify code pairs.

Some applications use the Broker Security Enhancement (BSE) to obtain such access. BSE enters the user’s information into the NEW PERSON (#200) file as a visitor, but it does *not* require an Access or Verify code for the user at the remote site. This process accomplishes the following:

- Enables RPC Broker applications to access remote VistA M Servers with increased security.
- Ensures correct information for user access to prevent the mistaken identification of an incorrect or *non*-existent user (spoofing) via unauthorized applications.
- Provides the ability for RPC Broker applications that have implemented BSE to specify their own context option.

BSE adds a step to the RPC Broker signon process to authenticate the connecting application. This involves passing a secret encoded phrase that is established on the VistA M Server via a patch and KIDS build. BSE also adds a step to the RPC Broker signon context on the remote VistA M Server to authenticate the user by connecting back to the authenticating VistA M Server to validate a token established during the authentication process and retrieve the user’s information from the authenticating server.

### Broker Call Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps present a basic outline of the events that go into an RPC Broker call, starting with the initial client-server connection. Once the client machine and user are authenticated, any number of calls (Steps 3-5) can occur through the open connection.

GUI developer issues are noted for each step.

1.  Authentication of client workstation. When a client workstation initiates a session, the Broker Listener on the server spawns a new job. The server then calls the client back to ensure that the client’s address is accurate.

GUI Developer Issues:

None. This process is built into the RPC Broker.

![](xwb-1-1-73-developer-s-guide/017.png) REF: For more details, see the *RPC Broker Systems Management Guide* on the VDL at: <http://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_sm.pdf>

1.  Authentication of user. After the server connects back to the client workstation, the user is asked for user credentials, either 2-factor authentication (Public Key Infrastructure \[PKI\] certificate and Personal Identification Number \[PIN\]) or an Access and Verify code. User authentication and identification is done with calls to VistA Kernel RPCs, including:
- XUS SIGNON SETUP
- XUS ESSO VALIDATE
- XUS AV CODE

GUI Developer Issues:

Broker Security Enhancement (BSE)—BSE user authentication and identification on remote VistA M servers is performed by passing a token to the XUS SIGNON SETUP RPC, which the server then uses to validate the user’s credentials on the authenticating VistA M Server.

Creating user context—Applications *must* create a context for the user by calling the XWB CREATE CONTEXT RPC. This process checks the user’s access to individual RPCs associated with the application.

Enabling <u>Silent Login</u>—Developers *must* decide whether to enable <u>Silent Login</u>.

2.  Client makes a Remote Procedure Call.

GUI Developer Issues:

Connecting to VistA—Developers creating Delphi GUI applications can use the <u>TRPCBroker Component</u> to connect to VistA. For each transaction, the application *mus*t set parameters and execute a call. Issues include:

- Determining data types for input and return.
- Determining the kind of call to make.

In addition to the RPC Broker components, other components are available. The VA FileMan Delphi components (FMDC) encapsulate the details of retrieving, validating, and updating VA FileMan data within a Delphi-based application.

![](xwb-1-1-73-developer-s-guide/018.png) REF: For more information on the VA FileMan Delphi Components (FMDC), see the FMDC VA Intranet Website.

![](xwb-1-1-73-developer-s-guide/019.png) NOTE: In the future, components may become available to encapsulate other VistA functions.

3.  RPC execution on server.

GUI Developer Issues:

A Remote Procedure Call (RPC) is a defined call to M code that runs on a VistA M Server.

![](xwb-1-1-73-developer-s-guide/020.png) REF: For RPC information, see the “<u>RPC Overview</u>” section.

Issues include:

- Determining the best RPC—The BDK provides some RPC Broker APIs.

![](xwb-1-1-73-developer-s-guide/021.png) REF: For more information on RPC Broker APIs, see the “<u>Application Programming Interface (API)</u>” section.

- Creating RPCs from scratch—In many cases, an existing M API can be wrapped into an RPC.

![](xwb-1-1-73-developer-s-guide/022.png) REF: For more information, see the “<u>Creating RPCs</u>” and “<u>RPC Overview</u>” sections.

- Registering RPCs. RPCs *must* be registered on the server, so users of the GUI VistA application have access to them.

![](xwb-1-1-73-developer-s-guide/023.png) REF: For more information on registering RPCs, see the “<u>RPC Security: How to Register an RPC</u>” section.

4.  RPC returns information to the client.

GUI Developer Issues:

Handling the return values, including any error messages.

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker BDK includes:

- <u>Units</u>
- <u>Classes</u>
- <u>Objects</u>
- <u>Components</u>
- <u>Types</u>
- <u>Methods</u>
- <u>Routines: Functions and Procedures</u>

For each class, object, and component, this manual lists the unit, declaration, properties, methods, and a description of how to use the class, object, or component.

Some types and properties are public, some are private, and some are available only within the function or procedure in which they are defined:

Unit

Interface {specifies that this unit is an interface to a class}

Uses

{list of external units being referenced within this unit}

Type

{Class definition}

Private  
  
{private (available within this unit) variable, type, property, method, function, and procedure definitions}

Public  
  
{published (available to units using this unit) Variable, type, property, method, function, and procedure definitions}

Implementation

{Method, Function, and Procedure programming, which can contain their own Uses, Type, and property definitions within themselves}

### Units

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Unit is a Pascal source-code file or program composed of classes, objects, and components containing all of the other elements. The BDK includes a number of units (e.g., winsockc.pas). This manual documents some of the units provided, and details what parts of the BDK are declared in each unit.

Sometimes it is helpful to know in which unit a particular item, such as a type or routine, is declared in the BDK. This is because if you use the item in your own code, you may need to include the corresponding unit in your own Pascal unit’s Uses clause.

The BDK is *not* really a standalone program, but the units in the BDK are compiled with an application (e.g., Computerized Patient Record System \[CPRS\]) to make a program. The interfaces to those units are called components (well-defined and published to be used externally). For example, the wsockc unit in the BDK uses (references) other external units (i.e., BDK and Delphi Run Time Library: AnsiStrings, SysUtils, WinSock2, XWBBut1, WinProcs, WinTypes, Classes, Dialogs, Forms, Controls, StdCtrls, ClipBrd, TRPCB, RpcbErr) to make the functions and procedures in those units available to wsockc.

### Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A class, or class type, defines a structure consisting of fields, methods, and properties.

### Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An object is a specific instance of that class with associated values.

### Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A component as defined by this document is a self-contained object with a well-defined interface defined by properties, methods, and events that makes it suitable for specialized purposes. Embarcadero Delphi documentation uses a more generic definition of component to refer to the elements within a class.

![](xwb-1-1-73-developer-s-guide/024.png) REF: For a more detailed description, see the *Embarcadero Delphi for Windows User Guide*.

### Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A type defines the possible range of values for a property or a method. A number of types are declared in the BDK, which you may need to make use of in the code. Some types and properties are public, some are private, and some are available only within the function or procedure in which they are defined.

![](xwb-1-1-73-developer-s-guide/025.png) NOTE: For sections describing types in this manual, the unit and declaration for each type, as well as a description of the type is also provided.

### Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delphi’s definition: “A method uses the same calling conventions as ordinary procedures and functions, except that every method has an additional implicit parameter “Self”, which is a reference to the instance or class in which the method is called. For example, clicking on a button invokes a method which changes the properties of the button.”

### Routines: Functions and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Procedures and functions, referred to collectively as routines, are self-contained statement blocks that can be called from different locations in a program. Routines can either be functions or procedures. A function returns a value, and a procedure does not.

![](xwb-1-1-73-developer-s-guide/026.png) NOTE: For sections in this manual describing routines, the unit and declaration for each routine is listed, as well as a description of the routine is provided.

![](xwb-1-1-73-developer-s-guide/027.png) NOTE: In Delphi, routine is the generic term. It is *not* the same as a VistA M routine. In M, a routine is the file containing everything else, including functions and procedures. In Delphi, that would be called a Unit.

## About this Version of the RPC Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 provides developers with the capability to develop VistA Client/Server software using the following RPC Broker Delphi components in a 32-bit environment (listed alphabetically):

- <u>TCCOWRPCBroker Component</u>
- <u>TContextorControl Component</u>
- <u>TRPCBroker Component</u> (original component)
- <u>TXWBRichEdit Component</u>
- <u>TXWBSSOiToken Component</u>

![](xwb-1-1-73-developer-s-guide/028.png) REF: For a complete list of patches released with RPC Broker 1.1, see the National Patch Module (NPM) on FORUM.

RPC Broker 1.1 supports IPv4/IPv6 dual-stack network addressing. It also supports 2-factor authentication (2FA) using Identity and Access Management (IAM) Secure Token Service (STS) delegated authentication.

To develop Delphi client VistA applications in a 32-bit environment you *must* have Delphi XE8 or newer. This version of the RPC Broker supports Delphi versions XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4. This version of the RPC Broker does *not* allow you to develop new applications in older versions of Delphi or in a 16-bit environment. However, the RPC Broker routines on the VistA M Server continue to support VistA applications previously developed in the 16-bit environment.

![](xwb-1-1-73-developer-s-guide/029.png) NOTE: Applications developed using previous versions of the RPC Broker Development Kit (BDK) can be adapted to use Delphi XE8 or newer by renaming references to the “Hash” Unit to “XWBHash” to resolve a conflict with a new “Hash” Unit provided in Delphi XE8. Current versions of the BDK use the renamed <u>XWBHash Unit</u>.

The default installation of the RPC Broker creates a separate Broker Development Kit (BDK) directory (i.e., BDK32) that contains the required RPC Broker files for development.

![](xwb-1-1-73-developer-s-guide/030.png) CAUTION: This statement defines the extent of support relative to use of Delphi. The Office of Information and Technology (OIT) only supports the Broker Development Kit (BDK) running in the currently offered version of Delphi and the immediately previous version of Delphi. This level of support became effective 06/12/2000.  
  
Sites can continue to use outdated versions of the RPC Broker Development Kit but do so with the understanding that support is *not* available and that continued use of outdated versions do *not* afford features that can be essential to effective client/server operations in the VistA environment. An archive of old (no longer supported) Broker Development Kits is maintained in the VA Intranet Broker Archive.

## What’s New in the BDK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section highlights the major changes made to the Broker Development Kit (BDK) 1.1. Changes are listed by BDK patch release in reverse order (latest to earliest):

### XWB\*1.1\*73

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*73, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Bug Fixes and Enhancements:
- When a user assigned more than one division in VistA selects the division in which they will be working, the Brokerx.User.Division field is populated with the selected division. However, the division is only identified by its number; the correct return should be IEN^SITENAME^SITEID. This patch ensures the data placed into the Brokerx.User.Division field is correctly formatted.
- Users are reporting that the default certificate for connection to VistA is *not* correct. Patches XWB\*1.1\*71 and XWB\*1.1\*72 addressed certificate processing; however, the user would have to ensure they were selecting the correct certificate from the list presented. This causes confusion if the list presented does *not* default to the certificate used for authenticating to VistA. This patch redesigned the method of certificate processing; it automatically selects the user's Authentication certificate, eliminating the need for the user to select from a list of certificates.
- The <u>ShowCertDialog Property</u> (Published) was added to the TRPCBroker component.
- Support for Delphi Versions—BDK supports Delphi XE8, 10, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4.

### XWB\*1.1\*72

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*72, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Bug Fixes and Enhancements:
- A user having only one division set in the NEW PERSON (#200) file was causing the site's DEFAULT INSITUTION entry to be set in the DIVISION field of the RPCBrokerx.User class, *not* the entry from the NEW PERSON (#200) file. This patch ensures the DIVISION field is properly set.
- Before this patch, there were many compiler Hints and Warnings, as well as some memory leaks. The Hints and Warnings have been addressed along with many of the memory leaks.
- Support for Delphi Versions—BDK supports Delphi XE8, 10, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4.

### XWB\*1.1\*71

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*71, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Bug Fixes and Enhancements:
- Patient Safety Issue (HITPS-2387)—Mental Health providers are unable to renew medications in the Computerized Patient Record System (CPRS) when a patient has more than one medication used by Mental Health providers. The issue arises when more than one medication is being renewed. The data received from First DataBank for drug\<-\>drug interactions exceeds the allowable width of a string in the LPack function in the wsockc.pas code of the BDK. This patch widens the width from 999 characters to 99999 characters.
- Broker Security Enhancement (BSE) Issue—Applications compiled with the BDK provided with XWB\*1.1\*65 could no longer connect to a remote VistA instance using the BSE without the user having to enter his/her Access/Verify codes at the remote site. This patch corrects this issue.
- Hidden Dialogue—There was a hidden dialogue when a user entered incorrect Access/Verify codes; this only occurred after the first dialogue was presented. The first dialogue was visible to the user, but subsequent dialogues for invalid Access/Verify codes were hidden behind the application window. This patch remedies this issue by ensuring the dialogue is always in front of the main application.
- Inability to Restart Unattended Applications—There was an inability to restart an unattended application, like the VistA Imaging Background Processor. If an unattended application was suddenly stopped by a VistA error, the application's context with VistA was removed; this prevented the application from reconnecting to VistA in an unattended fashion. This patch corrects this issue by preserving the context option that was initially created by the execution of the application.
- Token Issues—The way in which Identity and Access Management (IAM) security (Security Assertion Markup Language \[SAML\]) tokens were being retrieved was altering the way the token was presented to VistA, the original token structure was not sound. This patch changes the way the token is requested and how it is received from the IAM sever.
- Active Directory (AD) Credentials—When a user is unable to log onto a workstation with their Personal Identity Verification (PIV) card, the user contacts the Enterprise Service Desk (ESD) to receive a PIV exemption to allow them to log on with their Active Directory (AD) credentials (username and password). This version of the BDK was enhanced to detect this condition and allow the user to use their AD credentials to secure a SAML token from IAM for logging onto VistA via applications compiled with this version of the BDK.
- Section 508 Issues—When applications connecting to VistA were presented with the security banner, the text of the banner was *not* accessible to screen reader software, such as JAWS. This was caused by a Tab Stop *not* being set on the component that contains the banner text. This patch adds that Tab Stop and the text is readable by the screen reader software.
- Support for Delphi Versions—BDK supports Delphi XE8, 10, 10.1, 10.2, and 10.3.

### XWB\*1.1\*65

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*65, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Support for 2-Factor Authentication (2FA)—The <u>TRPCBroker Component</u> provides Windows client support for 2-factor authentication using an IAM STS token. The user is authenticated into IAM with smart-card credentials:
- Public Key Infrastructure (PKI) Certificate  
    
  and
- Personal Identification Number (PIN)

The credentials are exchanged for a digitally signed token that is forwarded to VistA to authenticate and identify the user.

- Support for Delphi Versions—BDK supports Delphi 10.2, 10.1, 10.0, and XE8, XE7, XE6, XE5, and XE4.

Components Added or Modified:

- <u>TXWBSSOiToken Component</u>—Added this component to explicitly obtain an Identity and Access Management (IAM) Secure Token Service (STS) token for 2-factor user authentication and identification. It is used by the BAPI32.DLL to make the STS token available to *non*-RPC Broker applications. It is *not* needed for TRPCBroker or TCCOWRPCBroker applications, as the STS token is obtained and consumed internally for user authentication and identification.
- <u>TRPCBroker Component</u>—Modified to support 2-factor authentication by obtaining and using an IAM STS token.

Library Methods Modified:

<u>Silent Login</u> Function—Used to authenticate into a VistA server without user interaction. It was modified to accept a new lmSSOi login mode. A silent login is used to authenticate into VistA with STS token credentials obtained from an earlier 2-factor authentication into IAM.

Properties Added or Modified (listed by component/class):

- <u>TXWBSSOiToken Component</u> Properties:
- <u>SSOiADUPN Property (TXWBSSOiToken Component)</u> (Published)
- <u>SSOiLogonName Property (TXWBSSOiToken Component)</u> (Published)
- <u>SSOiSECID Property (TXWBSSOiToken Component)</u> (Published)
- <u>SSOiToken Property (TXWBSSOiToken Component)</u> (Published)
- <u>TRPCBroker Component</u> Properties:
- <u>SSOiADUPN Property (TRPCBroker Component)</u> (Public)
- <u>SSOiLogonName Property (TRPCBroker Component)</u> (Public)
- <u>SSOiSECID (TRPCBroker Component)</u> (Public)
- <u>SSOiToken Property (TRPCBroker Component)</u> (Public)
- <u>Connected Property</u> (Published)

Types Modified:

<u>TLoginMode Type</u>

### XWB\*1.1\*60

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*60, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Support for IPv4/IPv6 Dual-Stack—The <u>TRPCBroker Component</u> provides Windows client support for IPv4/IPv6 dual-stack environment using new Application Programming Interfaces (APIs). This patch also upgrades from WinSock 1.1 to WinSock 2.2. By using this BDK for development of a Delphi client application, the application will be protocol independent and will be able to connect to both IPv4 and IPv6 VistA servers.
- Support for Delphi Versions—BDK supports Delphi XE7, XE6, XE5, and XE4.

Components Deprecated (Removed):

- TSharedBroker component—Deprecated and removed the TSharedBroker component from RPC Broker 1.1. This component allowed applications to share a single Broker connection.
- TSharedRPCBroker component—Deprecated and removed the TSharedRPCBroker component from RPC Broker 1.1. This component allowed applications to share a single Broker connection.

![](xwb-1-1-73-developer-s-guide/031.png) CAUTION: The Shared Broker components have been deprecated and removed with RPC Broker Patch XWB\*1.1\*60. They were *not* widely used and had proven to be difficult to maintain. They will *not* be updated to support IPv6 functionality or 2-factor authentication. Application developers are encouraged to migrate their applications to the standard TRPCBroker component when adding support for IPv6 and 2-factor authentication.

Components Modified:

<u>TRPCBroker Component</u>:

- Modified to upgrade Windows Sockets (WinSock) from Version 1.1 to Version 2.2.
- Modified to support IPv4/IPv6 dual-stack addressing for connection to a VistA server. Applications compiled with this BDK will be protocol independent and will be able to connect to both IPv4 and IPv6 VistA servers.
- Modified to support lookup to the Windows Registry for Secure Shell (SSH) configuration for connection to a VistA server.
- Deprecated and removed the old-style Broker (where VistA calls back to a different port on the client workstation when making a connection). Applications compiled with this BDK will use the new-style Broker (where VistA calls back to the originating port on the client workstation).
- Deprecated and removed the old-style Broker (where VistA calls back to a different port on the client workstation when making a connection). Applications compiled with this BDK will use the new-style Broker (where VistA calls back to the originating port on the client workstation).

Library Methods Modified:

<u>GetServerInfo Function</u>—Used to select the desired Server name and ListenerPort (see <u>ListenerPort Property</u>). Added a new SSH Username field when adding a new Server/ListenerPort combination. This field can be used to identify the Attachmate<sup>®</sup> Reflection/Micro Focus<sup>®</sup> SSH Username for SSH connection to the specified server.

Properties Deprecated (Removed; listed by component/class):

- <u>TRPCBroker Component</u> Properties:

The following <u>TRPCBroker Component</u> properties were deprecated, as the old-style Broker connection is no longer supported:

- IsBackwardCompatibleConnection property (Deprecated)
- IsNewStyleConnection property (read-only) (Deprecated)
- OldConnectionOnly property (Deprecated)
- TSharedBroker component and TSharedRPCBroker component properties:

The following TSharedBroker component and TSharedRPCBroker component properties were deprecated, as the Shared Broker itself has been deprecated:

- OnConnectionDropped property (Deprecated)
- OnLogout property (Deprecated)

### XWB\*1.1\*50

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*50, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- <u>Support for Secure Shell (SSH) Tunneling</u>—The <u>TRPCBroker Component</u> enabled Secure Shell (SSH) Tunnels to be used for secure connections. This functionality is controlled by setting an internal property value (mandatory SSH) or command line option at run time. Support is provided for the Attachmate<sup>®</sup> Reflection/Micro Focus<sup>®</sup> terminal emulator software using SSH tunneling for clients within the VA, and support is provided for PuTTY Link (Plink) for secure channels for clients outside the VA.
- <u>Support for Broker Security Enhancement (BSE)</u>—The <u>TRPCBroker Component</u> enabled visitor access to remote sites using authentication established at a home site.
- Support for Delphi Versions—BDK supports Delphi XE5, XE4, XE3, and XE2.

Components Added or Modified:

<u>TRPCBroker Component</u>:

- Modified to include support for Secure Shell (SSH) tunneling using Attachmate<sup>®</sup> Reflection/Micro Focus<sup>®</sup> Reflection SSH or PuTTY Link (Plink).
- Modified to include support for Broker Security Enhancement (BSE) modifications introduced in patch XWB\*1.1\*45.
- Modified by wrapping CCOW User Context into the primary <u>TRPCBroker Component</u> so that if the <u>Contextor Property</u> is set, then CCOW User Context is used.

![](xwb-1-1-73-developer-s-guide/032.png) NOTE: All of the CCOW functionality used by and for the <u>TCCOWRPCBroker Component</u> is still present, but it is now part of the regular <u>TRPCBroker Component</u>.  
  
This means that there is no longer a need to have the separate <u>TCCOWRPCBroker Component</u>. The <u>TCCOWRPCBroker Component</u> is included separately in XWB\*1.1\*50 for backward compatibility.

Properties Added or Modified to the <u>TCCOWRPCBroker Component</u>:

- <u>SecurityPhrase Property</u> (Published)
- <u>SSHHide Property</u> (Published)
- <u>SSHport Property</u> (Public)
- <u>SSHpw Property</u> (Public)
- <u>SSHUser Property</u> (Public)
- <u>UseSecureConnection Property</u> (Published)

### XWB\*1.1\*40

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*40, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

Supports Single Sign-On/User Context (SSO/UC)—As of RPC Broker Patch XWB\*1.1\*40, the <u>TCCOWRPCBroker Component</u> enabled Single Sign-On/User Context (SSO/UC) in CCOW-enabled applications.

![](xwb-1-1-73-developer-s-guide/033.png) REF: For more information on SSO/UC, see the Single Sign-On/User Context (SSO/UC) Installation Guide and Single Sign-On/User Context (SSO/UC) Deployment Guide on the VA Software Document Library (VDL).

Class Added:

<u>TXWBWinsock Class</u>

Components Added or Modified:

- <u>TCCOWRPCBroker Component</u>—Allows applications to be CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware.
- <u>TContextorControl Component</u>—Communicates with the Vergence Locator service.

Library Methods Added to the <u>TCCOWRPCBroker Component</u>:

- <u>GetCCOWtoken Method</u>
- <u>IsUserCleared Method</u>
- <u>IsUserContextPending Method</u>
- <u>WasUserDefined Method</u>

Properties Added or Modified (listed by component/class):

- <u>TCCOWRPCBroker Component</u> Properties:
- <u>CCOWLogonIDName Property (read-only)</u> (Public)
- <u>CCOWLogonIDValue Property (read-only)</u> (Public)
- <u>CCOWLogonName Property (read-only)</u> (Public)
- <u>CCOWLogonNameValue Property (read-only)</u> (Public)
- <u>CCOWLogonVpid Property (read-only)</u> (Public)
- <u>CCOWLogonVpidValue Property (read-only)</u> (Public)
- <u>Contextor Property</u> (Public)
- <u>TVistaLogin Class</u> Properties:
- <u>DomainName Property</u> (Public)
- <u>IsProductionAccount Property</u> (Public)
- <u>TVistaUser Class</u> Property:

<u>Vpid Property</u> (Public)

Types Added or Modified:

- <u>TLoginMode Type</u>
- TShowErorMsgs (see <u>ShowErrorMsgs Property</u>)
- TOnLoginFailure (see <u>OnFailedLogin Property</u>)
- TOnRPCBFailure (see <u>OnRPCBFailure Property</u>)
- <u>TParamType</u>

### XWB\*1.1\*35

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*35, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

Supports Non-Callback Connections—The RPC Broker components are built with a UCX or *non*-callback Broker connection, so that it can be used from behind firewalls, routers, etc.

Properties Added or Modified in the <u>TRPCBroker Component</u>:

- <u>BrokerVersion Property (read-only)</u> (Public)
- <u>CurrentContext Property (read-only)</u> (Public)
- IsBackwardCompatibleConnection property (Published; deprecated with <u>XWB\*1.1\*60</u>)
- IsNewStyleConnection property (read-only) (Public; deprecated with <u>XWB\*1.1\*60</u>)
- <u>KernelLogIn Property</u> (Published)
- <u>LogIn Property</u> (Public)
- OldConnectionOnly property (Published; deprecated with <u>XWB\*1.1\*60</u>)
- <u>OnRPCBFailure Property</u> (Public)
- <u>RPCBError Property (read-only)</u> (Public)
- <u>ShowErrorMsgs Property</u> (Published)
- <u>User Property</u> (Public)

### XWB\*1.1\*26

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*26, the following changes were made to RPC Broker 1.1:

Components Added or Modified:

- TSharedBroker component (component deprecated with <u>XWB\*1.1\*60</u>)—Added the TSharedBroker component to RPC Broker 1.1. This component allows applications to share a single Broker connection.
- TSharedRPCBroker component (component deprecated with <u>XWB\*1.1\*60</u>)—Added the TSharedRPCBroker component to RPC Broker 1.1. This component allows applications to share a single Broker connection.

### XWB\*1.1\*23

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*23, the following changes were made to RPC Broker 1.1:

Properties Added or Modified (listed by component/class):

TSharedBroker component and TSharedRPCBroker component properties (components deprecated with <u>XWB\*1.1\*60</u>):

- AllowShared property (Public; deprecated with <u>XWB\*1.1\*60</u>)
- OnConnectionDropped property (Public; deprecated with <u>XWB\*1.1\*60</u>)
- OnLogout property (Published; deprecated with <u>XWB\*1.1\*60</u>)

### XWB\*1.1\*14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*14, the following changes were made to RPC Broker 1.1:

- Separate RunTime and DesignTime Packages:

![](xwb-1-1-73-developer-s-guide/034.png) REF: For details and compiling instructions, see the “<u>DesignTime and RunTime Packages</u>” section in the “<u>Developer Considerations</u>” section.

- Broker Source Code Released:

The source code is located in the following directory:

BDK32\Source

![](xwb-1-1-73-developer-s-guide/035.png) CAUTION: Modified BDK source code should *not* be used to create VistA GUI applications. For more details, see the “<u>Developer Considerations</u>” section.  
  
Not all methods and properties found in the source code are documented at this time. Only those documented methods and properties are guaranteed to be made backwards compatible in future versions of the BDK.

### XWB\*1.1\*13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of BDK Patch XWB\*1.1\*13, the following changes were made to RPC Broker 1.1:

Functionality Added or Modified:

- Supports <u>Silent Login</u>—Provides functionality associated with the ability to make logins to a VistA M Server without the RPC Broker asking for Access and Verify code information.
- Documented Deferred RPCs and Capability to Run RPCs on a Remote Server:
- <u>Running RPCs on a Remote Server</u>
- <u>Deferred RPCs</u>
- Multi-instances of the RPC Broker—RPC Broker code was modified to permit an application to open two separate Broker instances with the same Server/ListenerPort (see <u>Server Property</u> and <u>ListenerPort Property</u>) combination, resulting in two separate partitions on the server. Previously, an attempt to open a second Broker instance ended up using the same partition. For this capability to be useful for concurrent processing, an application would have to use threads to handle the separate Broker sessions.

![](xwb-1-1-73-developer-s-guide/036.png) CAUTION: Although there should be no problems, the RPC Broker is *not guaranteed to be thread safe*.

- Operates in a 32-bit Microsoft<sup>®</sup> Windows environment.

Classes Added:

- <u>TVistaLogin Class</u>
- <u>TVistaUser Class</u>

Component Added or Modified:

<u>TXWBRichEdit Component</u>—This component replaced the Introductory Text Memo component on the Login Form. It permits URLs to be identified and launched.

Library Methods Added to <u>VCEdit Unit</u>:

- <u>ChangeVerify Function</u>
- <u>SilentChangeVerify Function</u>
- <u>StartProgSLogin Method</u>

Library Methods Modified:

- <u>CheckCmdLine Function</u>—Changed from procedure to function with a Boolean return value.
- <u>GetServerInfo Function</u>—Used to select the desired Server name and ListenerPort (see <u>ListenerPort Property</u>). It was modified to allow users to add a new Server/ListenerPort combination to those available for selection. It also accepts and stores a valid [IP address](#IP_Address), if no name is known for the location. This permits those who have access to other Server/ListenerPort combinations that may not be available in the list on the current workstation to access them. However, they still need a valid Access and Verify code to log on to the added location.
- <u>TParams Class</u>—Clear procedure was moved from Private to Public.
- <u>TRPCB Unit</u>:
- TOnLoginFailure: Changed from Object: TObject, since this is what should be expected by the procedure if it is called.
- TOnRPCBFailure: Changed from Object: TObject, since this is what should be expected by the procedure if it is called.

Properties Added or Modified in <u>TRPCBroker Component</u>:

- <u>BrokerVersion Property (read-only)</u> (Public)
- <u>CurrentContext Property (read-only)</u> (Public)
- IsBackwardCompatibleConnection property (Published; deprecated with <u>XWB\*1.1\*60</u>)
- IsNewStyleConnection property (read-only) (Public; deprecated with <u>XWB\*1.1\*60</u>)
- <u>KernelLogIn Property</u> (Published)
- <u>LogIn Property</u> (Public)
- OldConnectionOnly property (Published; deprecated with <u>XWB\*1.1\*60</u>)
- <u>OnRPCBFailure Property</u> (Public)
- <u>RPCBError Property (read-only)</u> (Public)
- <u>ShowErrorMsgs Property</u> (Published)
- <u>User Property</u> (Public)

Types Added or Modified:

- <u>TLoginMode Type</u>
- TShowErorMsgs (see <u>ShowErrorMsgs Property</u>)
- TOnLoginFailure (see <u>OnFailedLogin Property</u>)
- TOnRPCBFailure (see <u>OnRPCBFailure Property</u>)
- <u>TParamType</u>

## Developer Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Source Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of RPC Broker Patch XWB\*1.1\*14, the RPC Broker source code was released. The release of the source code does *not* affect how a developer uses the Broker Components or other parts of the BDK.

![](xwb-1-1-73-developer-s-guide/037.png) CAUTION: Modified BDK source code should *not* be used to create VistA GUI applications.

Suggestions for changes, bugs, and enhancements to the BDK should be done via the Service Desk Manager (SDM) support system for review and possible inclusion in a future patch.

The source code is located in the following directory:

BDK32\Source

### DesignTime and RunTime Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of RPC Broker Patch XWB\*1.1\*14, the BDK has separate RunTime and DesignTime packages. There is no longer a VistA Broker package. The new packages are:

- XWB_DXE*n*
- XWB_R*XEn*

Where:

- “D”—DesignTime
- “R”—RunTime
- “*XEn*”—Delphi version with which it should be used

For example, XWB_D*XE8* is the DesignTime package for Delphi Version *XE8.*

Delphi 10.*n* uses the XWB_RunTime and XWB_DesignTime packages. The RunTime package should *not* be used to create executables that depend on a separate XWB_R*XEn*.bpl installed on client workstations. There is no procedure in place at this time to reliably install the correct version of the RunTimebpl on client workstations*.*

![](xwb-1-1-73-developer-s-guide/038.png) CAUTION: Do *not* compile your project so that it relies on dynamic linking with the BDK’s RunTime package; that is, do *not* check the “Build with runtime packages” box on the “Packages” tab of the “Project Options’ dialogue.

### Resource Reuse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Developers should be aware of existing resources that may be of use. These resources may be available nationally or through a particular project. Possibilities include:

- Delphi components, such as the VA FileMan Delphi components (FMDC).

![](xwb-1-1-73-developer-s-guide/039.png) REF: For more information on the VA FileMan Delphi components (FMDC), see the FMDC VA Intranet website.

- <u>RPC Broker: Developer Tools</u>
- <u>Using an Existing M API</u>

### Component Connect-Disconnect Behavior

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Connect

The first time one of the Broker components in your application connects, it establishes an actual connection with the server. The connection record is added to the list of all active connections for your application. This list is internal to the application and is completely under the control of the Broker component and is transparent to you. If another Broker component tries to connect to the same server/port, the existing connection record is found in the list and its socket is shared. The new connection is also added to this list. This process is repeated with each connection request.

#### Disconnect

When a Broker component disconnects, its connection record is removed from the internal list of active connections. If it happens to be the last record for the particular server/port combination, the connection is actually closed. This scheme provides the illusion of multiple connections without “clogging up” the server.

## Application Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Application Version Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be a need to set or pass application version numbers. The suggested format is as follows:

VersionNumber_PatchNumber (3 digits)

For example, Patch 22 of Version 8.2 would be formatted as follows:

8.2_022

### Deferred RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to increase efficiency, applications can run RPCs in the background.

![](xwb-1-1-73-developer-s-guide/040.png) REF: For more information on Deferred RPCs, see the “<u>Deferred RPCs</u>” section.

### Remote RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to work with patient data across sites, applications can run RPCs on a remote server.

![](xwb-1-1-73-developer-s-guide/041.png) REF: For more information on running RPCs on a remote server, see the “<u>Running RPCs on a Remote Server</u>” section.

### Blocking RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications can install RPCs that should be used only in certain contexts. It is possible to block access to an RPC.

![](xwb-1-1-73-developer-s-guide/042.png) REF: For more information on blocking access to an RPC, see the “<u>Blocking an RPC</u>” section.

### Silent Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In special cases, applications can use one of three types of <u>Silent Login</u> to log in users *without* the RPC Broker prompting for login information.

# RPC Broker Components, Classes, Units, Methods, Types, and Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TCCOWRPCBroker Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties (All)</u>
- <u>Methods</u>
- <u>Example</u>

#### Parent Class

TRPCBroker = class(TComponent)

#### Unit

CCOWRPCBroker.pas

#### Description

The TCCOWRPCBroker component (CCOWRPCBroker.pas) is derived from the existing <u>TRPCBroker Component</u>. The TCCOWRPCBroker component (Trpcb.pas) allows VistA application developers to make their applications CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware with all of the client/server-related functionality in one integrated component. Using the TCCOWRPCBroker component, an application can share User Context stored in the CCOW Context Vault.

When a VistA CCOW-enabled application is recompiled with the TCCOWRPCBroker component and other required code modifications are made, that application becomes SSO/UC-aware and capable of CCOW single sign-on (SSO).

![](xwb-1-1-73-developer-s-guide/043.png) REF: For more detailed information on the application developer procedures and code modifications needed to make CCOW-enabled RPC Broker-based applications SSO/UC aware, see the “RPC Broker-based Client/Server Applications” section in the “Making VistA Applications SSO/UC-aware” chapter in the *Single Sign-On User Context (SSO/UC) Deployment Guide*.

![](xwb-1-1-73-developer-s-guide/044.png) NOTE: Properties inherited from the parent component (i.e., TComponent) are *not* discussed in this manual (only those properties added to the parent component are described). For help on inherited properties, see Delphi’s documentation on the parent component (i.e., TComponent).

![](xwb-1-1-73-developer-s-guide/045.png) REF: For help on inherited properties, see the parent component (i.e., <u>TRPCBroker Component</u>).

#### Properties (All)

- <u>Properties (Unique)</u>

<u>Table 4</u> lists all properties available with the <u>TCCOWRPCBroker Component</u> (includes those properties inherited from the parent <u>TRPCBroker Component</u>):

| Read-only                                                                       | RunTime only                                                                   | Property                                             |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------|
| ![](xwb-1-1-73-developer-s-guide/046.png) | ![](xwb-1-1-73-developer-s-guide/047.png) | <u>BrokerVersion Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/048.png) | ![](xwb-1-1-73-developer-s-guide/049.png) | <u>CCOWLogonIDName Property (read-only)</u>          |
| ![](xwb-1-1-73-developer-s-guide/050.png) | ![](xwb-1-1-73-developer-s-guide/051.png) | <u>CCOWLogonIDValue Property (read-only)</u>         |
| ![](xwb-1-1-73-developer-s-guide/052.png) | ![](xwb-1-1-73-developer-s-guide/053.png) | <u>CCOWLogonName Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/054.png) | ![](xwb-1-1-73-developer-s-guide/055.png) | <u>CCOWLogonNameValue Property (read-only)</u>       |
| ![](xwb-1-1-73-developer-s-guide/056.png) | ![](xwb-1-1-73-developer-s-guide/057.png) | <u>CCOWLogonVpid Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/058.png) | ![](xwb-1-1-73-developer-s-guide/059.png) | <u>CCOWLogonVpidValue Property (read-only)</u>       |
|                                                                                 |                                                                                | <u>ClearParameters Property</u>                      |
|                                                                                 |                                                                                | <u>ClearResults Property</u>                         |
|                                                                                 |                                                                                | <u>Connected Property</u>                            |
| ![](xwb-1-1-73-developer-s-guide/060.png) |                                                                                | <u>Contextor Property</u>                            |
| ![](xwb-1-1-73-developer-s-guide/061.png) | ![](xwb-1-1-73-developer-s-guide/062.png) | <u>CurrentContext Property (read-only)</u>           |
|                                                                                 |                                                                                | <u>DebugMode Property</u>                            |
|                                                                                 |                                                                                | <u>KernelLogIn Property</u>                          |
|                                                                                 |                                                                                | <u>ListenerPort Property</u>                         |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/063.png) | <u>LogIn Property</u>                                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/064.png) | <u>OnRPCBFailure Property</u>                        |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/065.png) | <u>Param Property</u>                                |
|                                                                                 |                                                                                | <u>RemoteProcedure Property</u>                      |
|                                                                                 |                                                                                | <u>Results Property</u>                              |
| ![](xwb-1-1-73-developer-s-guide/066.png) | ![](xwb-1-1-73-developer-s-guide/067.png) | <u>RPCBError Property (read-only)</u>                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/068.png) | <u>RPCTimeLimit Property</u>                         |
|                                                                                 |                                                                                | <u>RPCVersion Property</u>                           |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/069.png) | <u>SecurityPhrase Property</u>                       |
|                                                                                 |                                                                                | <u>Server Property</u>                               |
|                                                                                 |                                                                                | <u>ShowCertDialog Property</u>                       |
|                                                                                 |                                                                                | <u>ShowErrorMsgs Property</u>                        |
| ![](xwb-1-1-73-developer-s-guide/070.png) | ![](xwb-1-1-73-developer-s-guide/071.png) | <u>Socket Property (read-only)</u>                   |
|                                                                                 |                                                                                | <u>SSHHide Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/072.png) | <u>SSHport Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/073.png) | <u>SSHpw Property</u>                                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/074.png) | <u>SSHUser Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/075.png) | <u>SSOiToken Property (TRPCBroker Component)</u>     |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/076.png) | <u>SSOiSECID (TRPCBroker Component)</u>              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/077.png) | <u>SSOiADUPN Property (TRPCBroker Component)</u>     |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/078.png) | <u>SSOiLogonName Property (TRPCBroker Component)</u> |
| ![](xwb-1-1-73-developer-s-guide/079.png) | ![](xwb-1-1-73-developer-s-guide/080.png) | <u>User Property</u>                                 |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/081.png) | <u>UseSecureConnection Property</u>                  |

<span id="_Ref384102554" class="anchor"></span>Table 5: TCCOWRPCBroker Component—Unique Properties (listed alphabetically)

#### Properties (Unique)

- <u>Properties (All)</u>

<u>Table 5</u> lists the unique properties available with the <u>TCCOWRPCBroker Component</u>:

| Read-only                                                                       | RunTime only                                                                   | Property                                       |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------|
| ![](xwb-1-1-73-developer-s-guide/082.png) | ![](xwb-1-1-73-developer-s-guide/083.png) | <u>CCOWLogonIDName Property (read-only)</u>    |
| ![](xwb-1-1-73-developer-s-guide/084.png) | ![](xwb-1-1-73-developer-s-guide/085.png) | <u>CCOWLogonIDValue Property (read-only)</u>   |
| ![](xwb-1-1-73-developer-s-guide/086.png) | ![](xwb-1-1-73-developer-s-guide/087.png) | <u>CCOWLogonName Property (read-only)</u>      |
| ![](xwb-1-1-73-developer-s-guide/088.png) | ![](xwb-1-1-73-developer-s-guide/089.png) | <u>CCOWLogonNameValue Property (read-only)</u> |
| ![](xwb-1-1-73-developer-s-guide/090.png) | ![](xwb-1-1-73-developer-s-guide/091.png) | <u>CCOWLogonVpid Property (read-only)</u>      |
| ![](xwb-1-1-73-developer-s-guide/092.png) | ![](xwb-1-1-73-developer-s-guide/093.png) | <u>CCOWLogonVpidValue Property (read-only)</u> |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/094.png) | <u>Contextor Property</u>                      |

<span id="_Ref384103151" class="anchor"></span>Table 6: TRPCBroker Component—All Properties (listed alphabetically)

![](xwb-1-1-73-developer-s-guide/095.png) NOTE: Since the <u>TCCOWRPCBroker Component</u> is a class derived from the <u>TRPCBroker Component</u>, it contains all of the <u>Properties (All)</u>, <u>Methods</u>, etc., of its parent.

#### Methods

- <u>GetCCOWtoken Method</u>
- <u>IsUserCleared Method</u>
- <u>IsUserContextPending Method</u>
- <u>WasUserDefined Method</u>

#### Example

For examples, see the Samples directory on the use of the <u>TCCOWRPCBroker Component</u>; located in the following directory:

BDK32\Samples\BrokerEx

### TContextorControl Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of RPC Broker Patch XWB\*1.1\*40, the TContextorControl component was added to RPC Broker 1.1.

#### Parent Class

TRPCBroker = class(TOleServer)

#### Unit

<u>TRPCB Unit</u>

#### Description

The TContextorControl component provides Delphi developers with access to the CCOW Vergence Locator service.

### TRPCBroker Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties (All)</u>
- <u>Methods</u>
- <u>Example</u>

#### Parent Class

TRPCBroker = class(TComponent)

#### Unit

<u>TRPCB Unit</u>

#### Description

The TRPCBroker component provides Delphi developers with an easy, object-based access to the Broker. It is compatible with the Delphi object oriented (OO) environment. This component, when placed on a Delphi form, allows applications to connect to the VistA M Server and reference M data within Delphi’s Integrated Development Environment (IDE). It makes a Delphi form and everything on it “data aware.”

The TRPCBroker component (Trpcb.pas) provides VistA application developers with all of the client/server-related functionality in one integrated component. Using the TRPCBroker component, an application can connect to the VistA M Server by simply setting the <u>Connected Property</u> to True. Remote procedures on the server can be executed by preparing the <u>Param Property</u> and <u>RemoteProcedure Property</u> and invoking any of the following methods:

- <u>Call Method</u>
- <u>strCall Method</u>
- <u>lstCall Method</u>

The TRPCBroker component can be found on the Kernel tab in the component palette.

![](xwb-1-1-73-developer-s-guide/096.png) NOTE: Properties inherited from the parent component (i.e., TComponent) are *not* discussed in this manual (only those properties added to the parent component are described). For help on inherited properties, see Delphi’s documentation on the parent component (i.e., TComponent).

#### Support for Secure Shell (SSH) Tunneling

As of RPC Broker Patch XWB\*1.1\*50 support was added for a Secure Shell (SSH) tunneling service to provide secure data transfer between the client and the VistA M Server.

The Attachmate<sup>®</sup> Reflection/Micro Focus<sup>®</sup> Reflection terminal emulator software with SSH tunneling is used inside the VA to provide secure data transfer between the client and the VistA M Server. SSH tunneling is also supported for PuTTY Link (Plink) for those using VistA outside of the VA.

For SSH tunneling using Reflection, either set a command line option or a property within the application. SSH is enabled if the <u>UseSecureConnection Property</u> is set to “secureAttachmate”. SSH is also enabled if either of the following command line parameters are set:

- SSHPort=portnumber (to specify a particular port number—If *not* specified, it uses the port number for the remote server).
- SSHUser=username (for the remote server, where username is of the form *xxx*vista, where the *xxx* is the station’s three letter abbreviation).

For SSH tunneling using Plink.exe, either set a command line option or a property within the application. SSH is enabled if the UseSecureConnection property is set to “securePlink”. SSH is also enabled if the following command line parameter is set:

SSHpw=password

#### Support for Broker Security Enhancement (BSE)

As of RPC Broker Patch XWB\*1.1\*45, the RPC Broker supports the Broker Security Enhancement (BSE). The TRPCBroker component was modified to enable visitor access to remote sites using authentication established at a home site.

#### CCOW User Context Wrapped into the Primary TRPCBroker Component

As of RPC Broker Patch XWB\*1.1\*50, the RPC Broker wraps CCOW User Context into the primary TRPCBroker component so that if the <u>Contextor Property</u> is set, then CCOW User Context is used. This means that there is no longer a need to have the separate <u>TCCOWRPCBroker Component</u>.

![](xwb-1-1-73-developer-s-guide/097.png) NOTE: All of the functionality used by and for the <u>TCCOWRPCBroker Component</u> is still present, but it is now part of the regular TRPCBroker component.

#### Properties (All)

<u>Table 6</u> lists all of the properties available with the <u>TRPCBroker Component:</u>

| Read-only                                                                       | RunTime only                                                                   | Property                                             |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------|
| ![](xwb-1-1-73-developer-s-guide/098.png) | ![](xwb-1-1-73-developer-s-guide/099.png) | <u>BrokerVersion Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/100.png) | ![](xwb-1-1-73-developer-s-guide/101.png) | <u>CCOWLogonIDName Property (read-only)</u>          |
| ![](xwb-1-1-73-developer-s-guide/102.png) | ![](xwb-1-1-73-developer-s-guide/103.png) | <u>CCOWLogonIDValue Property (read-only)</u>         |
| ![](xwb-1-1-73-developer-s-guide/104.png) | ![](xwb-1-1-73-developer-s-guide/105.png) | <u>CCOWLogonName Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/106.png) | ![](xwb-1-1-73-developer-s-guide/107.png) | <u>CCOWLogonNameValue Property (read-only)</u>       |
| ![](xwb-1-1-73-developer-s-guide/108.png) | ![](xwb-1-1-73-developer-s-guide/109.png) | <u>CCOWLogonVpid Property (read-only)</u>            |
| ![](xwb-1-1-73-developer-s-guide/110.png) | ![](xwb-1-1-73-developer-s-guide/111.png) | <u>CCOWLogonVpidValue Property (read-only)</u>       |
|                                                                                 |                                                                                | <u>ClearParameters Property</u>                      |
|                                                                                 |                                                                                | <u>ClearResults Property</u>                         |
|                                                                                 |                                                                                | <u>Connected Property</u>                            |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/112.png) | <u>Contextor Property</u>                            |
| ![](xwb-1-1-73-developer-s-guide/113.png) | ![](xwb-1-1-73-developer-s-guide/114.png) | <u>CurrentContext Property (read-only)</u>           |
|                                                                                 |                                                                                | <u>DebugMode Property</u>                            |
|                                                                                 |                                                                                | <u>KernelLogIn Property</u>                          |
|                                                                                 |                                                                                | <u>ListenerPort Property</u>                         |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/115.png) | <u>LogIn Property</u>                                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/116.png) | <u>OnRPCBFailure Property</u>                        |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/117.png) | <u>Param Property</u>                                |
|                                                                                 |                                                                                | <u>RemoteProcedure Property</u>                      |
|                                                                                 |                                                                                | <u>Results Property</u>                              |
| ![](xwb-1-1-73-developer-s-guide/118.png) | ![](xwb-1-1-73-developer-s-guide/119.png) | <u>RPCBError Property (read-only)</u>                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/120.png) | <u>RPCTimeLimit Property</u>                         |
|                                                                                 |                                                                                | <u>RPCVersion Property</u>                           |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/121.png) | <u>SecurityPhrase Property</u>                       |
|                                                                                 |                                                                                | <u>Server Property</u>                               |
|                                                                                 |                                                                                | <u>ShowErrorMsgs Property</u>                        |
| ![](xwb-1-1-73-developer-s-guide/122.png) | ![](xwb-1-1-73-developer-s-guide/123.png) | <u>Socket Property (read-only)</u>                   |
|                                                                                 |                                                                                | <u>SSHHide Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/124.png) | <u>SSHport Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/125.png) | <u>SSHpw Property</u>                                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/126.png) | <u>SSHUser Property</u>                              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/127.png) | <u>SSOiToken Property (TRPCBroker Component)</u>     |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/128.png) | <u>SSOiSECID (TRPCBroker Component)</u>              |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/129.png) | <u>SSOiADUPN Property (TRPCBroker Component)</u>     |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/130.png) | <u>SSOiLogonName Property (TRPCBroker Component)</u> |
| ![](xwb-1-1-73-developer-s-guide/131.png) | ![](xwb-1-1-73-developer-s-guide/132.png) | <u>User Property</u>                                 |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/133.png) | <u>UseSecureConnection Property</u>                  |

<span id="_Ref467579116" class="anchor"></span>Table 7: TXWBSSOi Component—All Properties (listed alphabetically)

#### Methods

- <u>Call Method</u>
- <u>CreateContext Method</u>
- <u>GetCCOWtoken Method</u>
- <u>IsUserCleared Method</u>
- <u>IsUserContextPending Method</u>
- <u>lstCall Method</u>
- <u>pchCall Method</u>
- <u>strCall Method</u>
- <u>WasUserDefined Method</u>

#### Example

The following example demonstrates how a <u>TRPCBroker Component</u> can be used to:

1.  Connect to the VistA M Server.
5.  Execute various remote procedures.
6.  Return the results.
7.  Disconnect from the server.

The example in <u>Figure 2</u> assumes that a <u>TRPCBroker Component</u> already exists on the form as brkrRPCBroker1:

<span id="_Ref446321628" class="anchor"></span>Figure 1: TRPCBroker Component—Example

procedure TForm1.Button1Click(Sender: TObject);

begintry

*{connect to the server}*

brkrRPCBroker1.Connected := True;

*//assign RPC name*

brkrRPCBroker1.RemoteProcedure := ‘SOME APPLICATION RPC’;

*{make the call}*

brkrRPCBroker1.Call;

*{display results}*

ListBox1.Items := brkrRPCBroker1.Results;

*{disconnect from the server}*

brkrRPCBroker1.Connected := False;

except

*//put error handling code here*end;

end;

![](xwb-1-1-73-developer-s-guide/134.png) REF: For more examples, see the Samples directory on the use of the <u>TRPCBroker Component</u>; located in the following directory:

BDK32\Samples\BrokerEx

### TXWBRichEdit Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Property</u>

#### Parent Class

TXWBRichEdit = class(TComponent)

#### Unit

XwbRich20

#### Description

The TXWBRichEdit component replaces the Introductory Text Memo component on the Login Form. TXWBRichEdit (XwbRich20.pas) is a version of the TRichEdit component that uses Version 2 of Microsoft’s RichEdit Control and adds the ability to detect and respond to a Uniform Resource Locator (URL) in the text. This component permits developers to provide some requested functionality on the login form. As an XWB namespaced component, it was required to be put on the Kernel tab of the component palette; however, it rightly belongs on the Win32 tab.

![](xwb-1-1-73-developer-s-guide/135.png) NOTE: Properties inherited from the parent component (i.e., TComponent) are *not* discussed in this manual (only those properties added to the parent component are described). For help on inherited properties, refer to Delphi’s documentation on the parent component (i.e., TComponent).

#### Property

The following is the <u>TXWBRichEdit Component</u> property:

<u>URLDetect Property</u>

### TXWBSSOiToken Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties (All)</u>
- <u>Example</u>

#### Parent Class

TXWBSSOiToken = class(TComponent)

#### Unit

<u>XWBSSOi Unit</u>

#### Description

The TXWBSSOiToken component provides Delphi developers with an easy, object-based access to an Identity and Access Management (IAM) Secure Token Service (STS) token. It is compatible with the Delphi object oriented (OO) environment. This component, when placed on a Delphi form, allows applications to authenticate a user with the IAM STS Server and exchange the user’s 2-factor authentication (Public Key Infrastructure \[PKI\] certificate and Personal Identification Number \[PIN\]) credentials for an STS token.

The TXWBSSOiToken component (XWBSSOi.pas) does *not* need to be explicitly added to RPC Broker applications for 2-factor authentication (2FA) into VistA but is available should authentication be required into another system that accepts the STS token.

The TXWBSSOi component can be found on the Kernel tab in the component palette.

![](xwb-1-1-73-developer-s-guide/136.png) NOTE: Properties inherited from the parent component (i.e., TComponent) are *not* discussed in this manual (only those properties added to the parent component are described). For help on inherited properties, see Delphi’s documentation on the parent component (i.e., TComponent).

#### Properties (All)

<u>Table 7</u> lists all of the properties available with the <u>TXWBSSOiToken Component</u>:

| Read-only | RunTime only                                                                   | Property                                                |
|-----------|--------------------------------------------------------------------------------|---------------------------------------------------------|
|           | ![](xwb-1-1-73-developer-s-guide/137.png) | <u>SSOiToken Property (TXWBSSOiToken Component)</u>     |
|           | ![](xwb-1-1-73-developer-s-guide/138.png) | <u>SSOiADUPN Property (TXWBSSOiToken Component)</u>     |
|           | ![](xwb-1-1-73-developer-s-guide/139.png) | <u>SSOiLogonName Property (TXWBSSOiToken Component)</u> |
|           | ![](xwb-1-1-73-developer-s-guide/140.png) | <u>SSOiSECID Property (TXWBSSOiToken Component</u>)     |

<span id="_Ref384108409" class="anchor"></span>Table 8: TVistaLogin Class—All Properties (listed alphabetically)

#### Example

The following example demonstrates how a <u>TXWBSSOiToken Component</u> can be used to:

1.  Create (obtain) an IAM STS token.
8.  Assign the token and user values to strings.
9.  Delete the token (free up memory).

The example in <u>Figure 3</u> assumes that a <u>TXWBSSOiToken Component</u> already exists on the form as mySSOiToken:

<span id="_Ref467578938" class="anchor"></span>Figure 2: TXWBSSOiToken Component—Example

procedure TForm1.Button1Click(Sender: TObject; myToken: String; myName: String);

begintry

*{authenticate to the server}*

mySSOiToken := TXWBSSOiToken.Create(nil);

*//assign token values to strings*

myToken := mySSOiToken.SSOiToken;

myName := mySSOiToken.SSOiLogonName;

*{release the memory used by the token}*

mySSOiToken.Free;

except

*//put error handling code here*end;

end;

## Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TMult Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties</u>
- <u>Methods</u>
- <u>Example</u>

#### Unit

<u>TRPCB Unit</u>

#### Description

The TMult class is used whenever a list of multiple values needs to be passed to a remote procedure call (RPC) in a single parameter. The <u>Mult Property</u> of a parameter is of TMult type. The information put in the TMult variable is really stored in a TStringList, but the access methods (used to read and write) take strings as subscripts and provide the illusion of a string-subscripted array.

It is important to note that items in a TMult class may or may not be sorted. If the <u>Sorted Property</u> is:

- False (default)—Items are stored in the order they are added.
- True—Items are stored in ascending alphabetical order by subscripts.

If you attempt to reference an element by a nonexistent subscript you get an error in the form of a Delphi exception. Do *not* forget that M syntax dictates that all strings *must* be surrounded by double quotes. So, if your goal is to pass a string subscripted array of strings using TMult as a parameter to an RPC on the VistA M Server, do *not* forget to surround each of the subscripts and their associated values with double quotes (“). Otherwise, M assumes that you are passing a list of variables and attempts to reference them, which is probably *not* what you want.

#### Properties

The following are the TMult Class properties:

- <u>Count Property (TMult Class)</u>
- <u>First Property</u>
- <u>Last Property</u>
- MultArray property
- <u>Sorted Property</u>

#### Methods

The following are the TMult Class methods:

- [Assign Procedure (TMult Class)](#assign-method-tmult-class)
- [Order Function](#order-method)
- [Position Function](#position-method)
- [Subscript Function](#subscript-method)

#### Example

The program code in <u>Figure 4</u> demonstrates how to store and retrieve elements from a TMult variable:

<span id="_Ref446321631" class="anchor"></span>Figure 3: TMult Class—Example

procedure TForm1.Button1Click(Sender: TObject);

var

Mult: TMult;

Subscript: string;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

*{Store element pairs one by one}*

Mult\[‘First’\] := ‘One’;

Mult\[‘Second’\] := ‘Two’;

*{Use double quotes for M strings}*

Mult\[‘“First”‘\] := ‘“One”’;

*{Label1.Caption gets “One”}*

Label1.Caption := Mult\[‘“First”’\];

*{Error! ‘Third’ subscripted element was never stored}*

Label1.Caption := Mult\[‘Third’\];

end;

### TParamRecord Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties</u>
- <u>Example</u>

#### Unit

<u>TRPCB Unit</u>

#### Description

The TParamRecord class is used to hold all of the information on a single RPC parameter. Depending on the type of the parameter needed, different properties are used. The <u>PType Property</u> is always used to let the Broker on the VistA M Server know how to interpret the parameter. For a single value parameter, the <u>Value Property</u> should be used. In the case of a list or a word-processing text, use the <u>Mult Property</u>.

The TParamRecord relationship to the <u>TRPCBroker Component</u> is as follows:

The <u>TRPCBroker Component</u> contains the <u>Param Property</u> (i.e., <u>TParams Class</u>).

The <u>TParams Class</u> contains the ParamArray property (array \[I:integer\]: <u>TParamRecord Class</u>).

The <u>TParamRecord Class</u> contains the <u>Mult Property</u> (i.e., <u>TMult Class</u>).

The <u>TMult Class</u> contains the MultArray property (array\[S: string\]: string).

The MultArray property internally uses a TStringList in which each element’s object is a TString.

![](xwb-1-1-73-developer-s-guide/141.png) CAUTION: Developers should *rarely* need to use TParamRecord by itself in their code. TParamRecord is the type of the elements in the ParamArray, default array property of the <u>TRPCBroker Component</u> <u>Param Property</u>. This means that when you are working with a Param\[x\] element, you are in reality working with an instance of TParamRecord.

![](xwb-1-1-73-developer-s-guide/142.png) REF: For more information on RPCs, see the “<u>RPC Overview</u>” section.

#### Properties

The following are the TParamRecord class properties:

- <u>Mult Property</u>
- <u>PType Property</u>
- <u>Value Property</u>

#### Example

The program code in <u>Figure 5</u> demonstrates how you can use a TParamRecord variable to save a copy of a single parameter of a <u>TRPCBroker Component</u>. This example assumes that prior to calling this procedure, a TRPCBroker variable has been created and some parameters have been set up. Pay close attention to how properties are copied one at a time. This is the only way that a separate copy could be created. If you try to simply assign one of the TRPCBroker parameters to the TParamRecord variable, you simply re-point the TParamRecord variable to that parameter:

<span id="_Ref446321623" class="anchor"></span>Figure 4: TParamRecord Class—Example

procedure TForm1.Button1Click(Sender: TObject);

var

ParamRecord: TParamRecord;

begin

*{Create ParamRecord. Make Form1 its owner}*

ParamRecord := TParamRecord.Create(Form1);

*{Store properties one at a time}*

ParamRecord.Value := RPCBroker.Param\[0\].Value;

ParamRecord.PType := RPCBroker.Param\[0\].PType;

*{This is how to copy a Mult}*

ParamRecord.Mult.Assign(RPCBroker.Param\[0\].Mult);

end;

### TParams Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Properties</u>
- <u>Methods</u>
- <u>Example</u>

#### Unit

<u>TRPCB Unit</u>

#### Description

The TParams class is used to hold parameters (i.e., array of TParamRecord) used in a remote procedure call (RPC). You do *not* need to know in advance how many parameters you need or allocate memory for them; a simple reference or an assignment to a parameter creates it.

The Clear procedure can be used to remove/clear data from TParams.

![](xwb-1-1-73-developer-s-guide/143.png) NOTE: Previously, this procedure was Private, but as of Patch XWB\*1.1\*13, it was made Public.

#### Properties

The following are the TParams Class properties:

- <u>Count Property (TParams Class)</u>
- ParamArray property

#### Methods

The following are the TParamsClass methods:

- [Assign Procedure (TParams Class)](#assign-method-tparams-class)
- Clear procedure

#### Example

The program code in <u>Figure 6</u> demonstrates how a <u>TParams Class</u> can be used to save off the <u>TRPCBroker Component</u> parameters and restore them later:

<span id="_Ref446321636" class="anchor"></span>Figure 5: TParams Class—Example

procedure TForm1.Button1Click(Sender: TObject);

var

SaveParams: TParams;

SaveRemoteProcedure: string;

begin

*{create holding variable with Form1 as owner}*

SaveParams := TParams.Create(self);

*{save parameters}*

SaveParams.Assign(brkrRPCBroker1.Param);

SaveRemoteProcedure := brkrRPCBroker1.RemoteProcedure;

brkrRPCBroker1.RemoteProcedure := ‘SOME OTHER PROCEDURE’;

brkrRPCBroker1.ClearParameters := True;

brkrRPCBroker1.Call;

*{restore parameters}*

brkrRPCBroker1.Param.Assign(SaveParams);

brkrRPCBroker1.RemoteProcedure := SaveRemoteProcedure;

*{release memory}*

SaveParams.Free;

end;

### TVistaLogin Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Properties</u>

#### Unit

<u>TRPCB Unit</u>

#### Description

The TVistaLogin class is used to hold login parameters for <u>Silent Login</u>.

![](xwb-1-1-73-developer-s-guide/144.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

#### Properties

<u>Table 8</u> lists all of the properties available with the <u>TVistaLogin Class</u>:

| Read-only                                                                       | RunTime only                                                                   | Property                                     |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------|
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/145.png) | <u>AccessCode Property</u>                   |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/146.png) | <u>Division Property (TVistaLogin Class)</u> |
| ![](xwb-1-1-73-developer-s-guide/147.png) | ![](xwb-1-1-73-developer-s-guide/148.png) | <u>DivList Property (read-only)</u>          |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/149.png) | <u>DomainName Property</u>                   |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/150.png) | <u>DUZ Property (TVistaLogin Class)</u>      |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/151.png) | <u>ErrorText Property</u>                    |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/152.png) | <u>IsProductionAccount Property</u>          |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/153.png) | <u>LoginHandle Property</u>                  |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/154.png) | <u>Mode Property</u>                         |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/155.png) | <u>MultiDivision Property</u>                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/156.png) | NTToken Property                             |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/157.png) | <u>OnFailedLogin Property</u>                |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/158.png) | <u>PromptDivision Property</u>               |
|                                                                                 | ![](xwb-1-1-73-developer-s-guide/159.png) | <u>VerifyCode Property</u>                   |

<span id="_Ref384108647" class="anchor"></span>Table 9: TVistaUser Class—All Properties (listed alphabetically)

### TVistaUser Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Properties</u>

#### Unit

<u>TRPCB Unit</u>

#### Description

The TVistaUser class is used to hold parameters related to the current user. These parameters are filled in as part of the login procedure.

![](xwb-1-1-73-developer-s-guide/160.png) NOTE: This class is used as a property by the TRPCBroker class. This property, with its associated data, is available to all applications, whether or not they are using a <u>Silent Login</u>.

#### Properties

<u>Table 9</u> lists all of the properties available with the <u>TVistaUser Class</u>:

| Read-only | RunTime only                                                                   | Property                                    |
|-----------|--------------------------------------------------------------------------------|---------------------------------------------|
|           | ![](xwb-1-1-73-developer-s-guide/161.png) | <u>Division Property (TVistaUser Class)</u> |
|           | ![](xwb-1-1-73-developer-s-guide/162.png) | <u>DTime Property</u>                       |
|           | ![](xwb-1-1-73-developer-s-guide/163.png) | <u>DUZ Property (TVistaUser Class)</u>      |
|           | ![](xwb-1-1-73-developer-s-guide/164.png) | <u>Language Property</u>                    |
|           | ![](xwb-1-1-73-developer-s-guide/165.png) | <u>Name Property</u>                        |
|           | ![](xwb-1-1-73-developer-s-guide/166.png) | <u>ServiceSection Property</u>              |
|           | ![](xwb-1-1-73-developer-s-guide/167.png) | <u>StandardName Property</u>                |
|           | ![](xwb-1-1-73-developer-s-guide/168.png) | <u>Title Property</u>                       |
|           | ![](xwb-1-1-73-developer-s-guide/169.png) | <u>VerifyCodeChngd Property</u>             |
|           | ![](xwb-1-1-73-developer-s-guide/170.png) | <u>Vpid Property</u>                        |

<span id="_Ref384098720" class="anchor"></span>Table 10: TLoginMode Type—Silent Login Values

### TXWBWinsock Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Unit

<u>TRPCB Unit</u>

#### Description

The code handling connections and transmission was moved into the TXWBWinsock class, which is defined in wsockc.pas. It facilitates the ability for making and maintaining multiple independent RPC Broker connections. To get around cyclic issues with the Uses clause, XWBWinsock within Trpcb.pas is defined as TObject and *must* be cast to TXWBWinsock when it is used.

The methods in the wsockc.pas unit were originally library methods or methods *not* associated with a class. To ensure that the <u>TCCOWRPCBroker Component</u> is thread-safe (i.e., thread safe operation of RPC Broker instances created in different threads), it became necessary for each instance of the TRPCBroker to have its own instance of these methods, values, etc. Thus, the TXWBWinsock class was created to encapsulate the Public members.

Methods within the TXWBWinsock class should *not* be referenced directly. Connections to VistA are made by setting the TVistaLogin <u>Connected Property</u> to “true” and ended by setting the <u>Connected Property</u> to “false”.

## Units

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-developer-s-guide/171.png) CAUTION: Not all units found in the source code are documented at this time. Only those documented methods and properties are guaranteed to be made backwards compatible in future versions of the BDK.

The following Units are described in this document (listed alphabetically):

- <u>CCOWRPCBroker Unit</u>
- <u>LoginFrm Unit</u>
- <u>MFunStr Unit</u>
- <u>RPCConf1 Unit</u>
- <u>RpcSLogin Unit</u>
- <u>SplVista Unit</u>
- <u>TRPCB Unit</u>
- <u>VCEdit Unit</u>
- <u>Wsockc Unit</u>
- <u>XWBHash Unit</u>
- <u>XWBSSOi Unit</u>

### CCOWRPCBroker Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCOWRPCBroker unit authenticates a user using CCOW user context.

#### Library Method

AuthenticateUser Procedure

![](xwb-1-1-73-developer-s-guide/172.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### LoginFrm Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch XWB\*1.1\*13, a “Change VC” check box was added to the to the login form. The user can use this check box to indicate that she/he wants to change their Verify code. If this box has been checked, after the user has completed logging in to the system, the Change Verify code dialogue is displayed.

![](xwb-1-1-73-developer-s-guide/173.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### MFunStr Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MFunStr unit contains Delphi functions that emulate MUMPS functions.

#### Library Methods

- <u>Piece Function</u>
- <u>Translate Function</u>

![](xwb-1-1-73-developer-s-guide/174.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### RPCConf1 Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCConf1 unit contains server selection dialogue.

![](xwb-1-1-73-developer-s-guide/175.png) CAUTION: This unit assumes that a single IP address is assigned to a host. That is no longer a reasonable assumption in a modern computing environment. These functions are expected to be deprecated and replaced in future versions of the BDK.

#### Library Methods

- <u>GetServerInfo Function</u>
- <u>GetServerIP Function</u>
- IsIPAddress function

![](xwb-1-1-73-developer-s-guide/176.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### RpcSLogin Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RpcSLogin unit contains silent login functionality.

#### Library Methods

- <u>CheckCmdLine Function</u>
- GetSessionInfo procedure
- GetUserInfo procedure
- SilentLogIn Ffunction
- [StartProgSLogin Procedure](#startprogslogin-method)
- ValidAppHandle function
- ValidAVCodes function
- ValidNTToken function

![](xwb-1-1-73-developer-s-guide/177.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

![](xwb-1-1-73-developer-s-guide/178.png) REF: For more information on silent login, see the “<u>Silent Login</u>” section.

### SplVista Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SplVista unit displays the VistA splash screen.

#### Library Methods

- SplashOpen procedure
- SplashClose procedure

![](xwb-1-1-73-developer-s-guide/179.png) REF: For more information on splash screens, see the “<u>VistA Splash Screen Procedures</u>” section.

![](xwb-1-1-73-developer-s-guide/180.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### TRPCB Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TRPCB unit contains the declarations for the various RPC Broker components.

When you add a component declared in this unit to a form, the unit is automatically added to the uses clause of that form’s unit.

The following items are automatically declared in the uses clause:

SysUtils, WinTypes, WinProcs, Messages, Classes, Graphics, Controls, Forms, Dialogs

#### Classes

- <u>TParamRecord Class</u>
- <u>TParams Class</u>
- <u>TVistaLogin Class</u>
- <u>TVistaUser Class</u>

#### Component

<u>TRPCBroker Component</u>

#### Library Methods

- GetAppHandle
- <u>TMult Class Methods</u>
- <u>TParams Class Method</u>
- <u>TRPCBroker Component</u> <u>Methods</u>

#### Types

- <u>EBrokerError</u>
- <u>TLoginMode Type</u>
- <u>TParamType</u>

![](xwb-1-1-73-developer-s-guide/181.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### VCEdit Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker calls the VCEdit unit at logon when users *must* change their Verify code (i.e., Verify code has expired). There is also a check box on the “VistA Sign-on” form that allows uses to change their Verify code at any time.

#### Library Methods

- <u>ChangeVerify Function</u>
- <u>SilentChangeVerify Function</u>

![](xwb-1-1-73-developer-s-guide/182.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### Wsockc Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Wsockc unit contains the interface to the Microsoft<sup>®</sup> Windows operating system TCP/IP network interface. It provides the communications between the RPC Broker GUI and the VistA M Server.

When a component declared in this unit is added to a form, the unit is automatically added to the uses clause of that form’s unit.

The following items are automatically declared in the uses clause:

AnsiStrings, SysUtils, Classes, Windows, WinTypes, WinProcs, Winsock2, Xwbut1, Trpcb, RpcbErr, Dialogs, Forms, Controls, StdCtrls, ClipBrd

#### Component

TXWBWinsock component

![](xwb-1-1-73-developer-s-guide/183.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### XWBHash Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Library Methods

- <u>Encrypt Function</u>
- <u>Decrypt Function</u>

![](xwb-1-1-73-developer-s-guide/184.png) REF: For more information on encryption/decryption functions, see the “<u>Encryption Functions</u>” section.

![](xwb-1-1-73-developer-s-guide/185.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

### XWBSSOi Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XWBSSOi unit contains the interface to the Identity and Access Management (IAM) Secure Token Service (STS) server.

When a component declared in this unit is added to a form, the unit is automatically added to the uses clause of that form’s unit.

The following items are automatically declared in the uses clause:

Messages, Windows, Classes, SysUtils, Variants, Controls, Dialogs, Forms, Graphics, OleCtrls, MSHTML, SHDocVw, MFunStr, XWBut1

#### Component

<u>TXWBSSOiToken Component</u>

![](xwb-1-1-73-developer-s-guide/186.png) REF: To see a listing of items declared in this unit including their declarations, use the ObjectBrowser.

## Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assign Method (TMult Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

procedure Assign(Source: TPersistent);

#### Description

The Assign method for a <u>TMult Class</u> takes Tstrings, a TStringList, or another TMult. In the case where the source is a TMult, the owner of the Assign method gets the exact copy of the source with all string subscripts and values. In the case where the source is a Tstrings or a TStringList, the items are copied such that the strings property of each item becomes the Value, while the index becomes the subscript in the string form.

![](xwb-1-1-73-developer-s-guide/187.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TMult Class</u>, see the “<u>RPC Limits</u>” section.

#### Example

#### TMult Assign Method—Assigning listbox Items to a TMULT

To assign listbox items to a TMult, do the following:

1.  Start a new VCL Forms application.
10. Drop one TListBox, one TMemo, and one TButton on the form. Arrange controls as in <u>Figure 8</u>.
11. Add Vcl.StdCtrls and TRPCB to the “uses” clause.
12. Copy the code in <u>Figure 7</u> to the Button1.OnClick event:

> <span id="_Ref446321639" class="anchor"></span>Figure 6: TMult Assign Method—Code Added to the Button1.OnClick Event

procedure TForm1.Button1Click(Sender: TObject);

var

Mult1: TMult;

Subscript: string;

begin

*//Create Mult1. Make Form1 its owner*

Mult1 := TMult.Create(Form1);

*//Fill listbox with some strings*

ListBox1.Items.Add(‘One’);

ListBox1.Items.Add(‘Two’);

ListBox1.Items.Add(‘Three’);

ListBox1.Items.Add(‘Four’);

ListBox1.Items.Add(‘Five’);

*//assign (copy) listbox strings to Mult*

Mult1.Assign(ListBox1.Items);

*//configure memo box for better display*

Memo1.Font.Name := ‘Courier’;

Memo1.Lines.Clear;

Memo1.Lines.Add(‘Tstrings assigned:’);

*//set a starting point*

Subscript := ‘’;

repeat

*//get next Mult element*

Subscript := Mult1.Order(Subscript, 1);

*//if not the end of list*

if Subscript \<\> ‘’ then

*//display subscript*

Memo1.Lines.Add(Format(‘%10s’, \[Subscript\]) + ‘ - ’ + Mult1\[Subscript\])

*//stop when reached the end*

until Subscript = ‘’;

end;

13. Run the project and click on the button.  
      
    The expected output is shown in <u>Figure 8</u>:

> <span id="_Ref385263278" class="anchor"></span>Figure 7: TMult Assign Method—Assigning listbox Items to a TMULT: Sample Form Output

> ![](xwb-1-1-73-developer-s-guide/188.png)

#### TMult Assign Method—Assigning One TMULT to Another

The program code in <u>Figure 9</u> demonstrates the use of the TMultAssign method to assign one TMult to another:

1.  Start a new VCL Forms application.
14. Drop one TMemo and one TButton on the form. Arrange controls as in <u>Figure 10</u>.
15. Add Vcl.StdCtrls and TRPCB to the “uses” clause.
16. Copy the code in <u>Figure 9</u> to the Button1.OnClick event:

> <span id="_Ref446321644" class="anchor"></span>Figure 8: TMult Assign Method—Code Added to the Button1.OnClick Event

procedure TForm1.Button1Click(Sender: TObject);

var

Mult1, Mult2: TMult;

Subscript: string;

begin

*//Create Mult1. Make Form1 its owner*

Mult1 := TMult.Create(Form1);

*//Create Mult2. Make Form1 its owner*

Mult2 := TMult.Create(Form1);

*//Fill Mult1 with some strings*

Mult1\[‘First’\] := ‘One’;

Mult1\[‘Second’\] := ‘Two’;

Mult1\[‘Third’\] := ‘Three’;

Mult1\[‘Fourth’\] := ‘Four’;

Mult1\[‘Fifth’\] := ‘Five’;

*//assign (copy) Mult1 strings to Mult2*

Mult2.Assign(Mult1);

*//configure memo box for better display*

Memo1.Font.Name := ‘Courier’;

Memo1.Lines.Clear;

Memo1.Lines.Add(‘TMult assigned:’);

*//set a starting point*

Subscript := ‘’;

repeat

*//get next Mult element*

Subscript := Mult2.Order(Subscript, 1);

*//if not the end of list*if Subscript \<\> ‘’ then

*//display subscript value*

Memo1.Lines.Add(Format(‘%10s’, \[Subscript\]) + ‘ - ’ + Mult2\[Subscript\])

*//stop when reached the end*until Subscript = ‘’;

end;

17. Run the project and click on the button.  
      
    The expected output is shown in <u>Figure 10</u>:

> <span id="_Ref445381534" class="anchor"></span>Figure 9: TMult Assign Method—Assigning One TMULT to another: Sample Form Output

> ![](xwb-1-1-73-developer-s-guide/189.png)

### Assign Method (TParams Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TParams Class</u>

#### Declaration

procedure Assign(Source: TParams);

#### Description

The Assign method for a <u>TParams Class</u> takes another <u>TParams Class</u> parameter. The Assign method is useful for copying one <u>TParams Class</u> to another. The entire contents of the passed in <u>TParams Class</u> are copied into the owner of the Assign method. The Assign method first deletes all of the parameters in the receiving class and then copies the parameters from the passed in class, creating a whole duplicate copy.

![](xwb-1-1-73-developer-s-guide/190.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TParams Class</u>, see the “<u>RPC Limits</u>” section.

#### Example

The program code in <u>Figure 11</u> demonstrates how a <u>TParams Class</u> Assign method can be used to save off the <u>TRPCBroker Component</u> parameters and restore them later:

<span id="_Ref446321649" class="anchor"></span>Figure 10: Assign Method (TParams Class)—Example

procedure TForm1.Button1Click(Sender: TObject);

var

SaveParams: TParams;

SaveRemoteProcedure: string;

begin

SaveParams := TParams.Create(self)  *{create holding variable with Form1 as owner}*

SaveParams.Assign(brkrRPCBroker1.Param);  *{save parameters}*

SaveRemoteProcedure := brkrRPCBroker1.RemoteProcedure;

brkrRPCBroker1.RemoteProcedure := ‘SOME OTHER PROCEDURE’;

brkrRPCBroker1.ClearParameters := True;

brkrRPCBroker1.Call;

brkrRPCBroker1.Param.Assign(SaveParams);  *{restore parameters}*

brkrRPCBroker1.RemoteProcedure := SaveRemoteProcedure;

SaveParams.Free;  *{release memory}*end;

### Call Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

procedure Call;

#### Description

The Call method executes a remote procedure on the VistA M Server and returns the results in the <u>Results Property</u>. Call expects the name of the remote procedure and its parameters to be set up in the <u>RemoteProcedure Property</u> and <u>Param Property</u> respectively. If the <u>ClearResults Property</u> is True, then the <u>Results Property</u> is cleared before the call. If the <u>ClearParameters Property</u> is True, then the <u>Param Property</u> is cleared after the call finishes.

![](xwb-1-1-73-developer-s-guide/191.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

![](xwb-1-1-73-developer-s-guide/192.png) NOTE: Whenever the Broker makes a call to the VistA M Server, if the cursor is crDefault, the cursor is automatically changed to the hourglass symbol as seen in other Microsoft-compliant software. If the application has already modified the cursor from crDefault to something else, the Broker does *not* change the cursor.

![](xwb-1-1-73-developer-s-guide/193.png) REF: For a demonstration using the Call method, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 12</u> demonstrates the use of the <u>Call Method</u> in a hypothetical example of bringing back demographic information for a patient and then displaying the results in a memo box:

<span id="_Ref446321652" class="anchor"></span>Figure 11: Call Method—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.RemoteProcedure := ‘GET PATIENT DEMOGRAPHICS’;

brkrRPCBroker1.Param\[0\].Value := ‘DFN’;

brkrRPCBroker1.Param\[0\].PType := reference;

brkrRPCBroker1.Call;

Memo1.Lines := brkrRPCBroker1.Results;

end;

![](xwb-1-1-73-developer-s-guide/194.png) REF: For a demonstration using the <u>Call Method</u>, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### CreateContext Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

function CreateContext(strContext: string): boolean;

Use the CreateContext method of the <u>TRPCBroker Component</u> to create a context for your application. To create context, pass an option name in the strContext parameter. If the function returns True, a context was created, and your application can use all RPCs entered in the option’s RPC multiple. If the <u>TRPCBroker Component</u> is *not* connected at the time context is created, a connection is established. If for some reason a context could *not* be created, the CreateContext method returns False.

Since context is nothing more than a client/server “B”-type option in the OPTION (#19) file, standard Kernel Menu Manager (MenuMan) security is applied in establishing a context. Therefore, a context option can be granted to users exactly the same way as regular options are done using MenuMan. Before any RPC can run, it *must* have a context established for it to on the VistA M Server. Thus, all RPCs *must* be registered to one or more “B”-type options. This plays a major role in Broker security.

![](xwb-1-1-73-developer-s-guide/195.png) REF: For information about registering RPCs, see the “<u>RPC Security: How to Register an RPC</u>” section.

A context *cannot* be established for the following reasons:

- The user has no access to that option.
- The option is temporarily out of order.

An application can switch from one context to another as often as it needs to. Each time a context is created the previous context is overwritten.

![](xwb-1-1-73-developer-s-guide/196.png) REF: For information about saving off the current context in order to temporarily create a different context and then restore the previous context, see the “<u>CurrentContext Property (read-only)</u>” section.

![](xwb-1-1-73-developer-s-guide/197.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

![](xwb-1-1-73-developer-s-guide/198.png) NOTE: Whenever the Broker makes a call to the VistA M Server, if the cursor is crDefault, the cursor is automatically changed to the hourglass symbol as seen in other Microsoft-compliant software. If the application has already modified the cursor from crDefault to something else, the Broker does *not* change the cursor.

![](xwb-1-1-73-developer-s-guide/199.png) REF: For a demonstration that creates an application context, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 13</u> demonstrates the use of the <u>CreateContext Method</u>:

<span id="_Ref446321655" class="anchor"></span>Figure 12: CreateContext Method—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.Connected := True;

if brkrRPCBroker1.CreateContext(‘MY APPLICATION’) then

Label1.Caption := ‘Context MY APPLICATION was successfully created.’

else

Label1.Caption := ‘Context MY APPLICATION could not be created.’;

end;

![](xwb-1-1-73-developer-s-guide/200.png) REF: For a demonstration that creates an application context, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### GetCCOWtoken Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

function GetCCOWtoken(Contextor: TContextorControl): string;

The GetCCOWtoken method returns the CCOW token as a string value. This value is passed in as authentication for the current user. The developer should *not* need access to this, since it is handled directly within the code for making the connection.

![](xwb-1-1-73-developer-s-guide/201.png) NOTE: The TContextorControl component is the interface for the Sentillion Vergence ContextorControl that communicates with the Context Vault. The component is created based on the type library for the DLL.

Since developers may want to use the TContextorControl component to initialize their own instances, the TContextorControl component is placed on the Kernel palette in Delphi; however, it is almost as easy to simply create it at run-time without using a component.

![](xwb-1-1-73-developer-s-guide/202.png) REF: For an example of the GetCCOWtoken method, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### IsUserCleared Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

function IsUserCleared: Boolean;

The IsUserCleared method returns a value of True if the user value in the Context Vault has been cleared. The value is only of interest if the <u>WasUserDefined Method</u> has a True value (since unless the user has been defined previously, it would *not* have a value). This method returns:

- True—CCOWUser Context is currently cleared.
- False—CCOWUser Context is currently *not* cleared

This method is used in response to an OnPending event to determine if the pending change is User Context related, and if so, whether the User value in the Context Vault has been cleared. If the value has been cleared, then the application should shut down. Switching User Context is *not* supported, since Office of Cyber and Information Security (OCIS) policy indicates that the current user *must* sign off the client workstation and the new user *must* sign on the client workstation.

#### Example

In the event handler for the Commit event of the TContextorControl, developers can check whether or not the user was previously defined and is now undefined or NULL. In this case, developers would want to do any necessary processing, and then halt.

<span id="_Toc82593574" class="anchor"></span>Figure 13: IsUserCleared Method—Example

Procedure TForm1.CommitHandler(Sender: TObject)

beginwith CCOWRPCBroker1 doif WasUserDefined and IsUserCleared thenbegin

*// do any necessary processing before halting*halt;

end;

end;

### IsUserContextPending Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

function IsUserContextPending(aContextItemCollection: IContextItemCollection): Boolean;

The IsUserContextPending method returns a value of True if the pending context change is related to User Context; if not, then it may be related to the Patient Context, etc. This method returns:

- True—CCOW pending context change is related to User Context.
- False—CCOW pending context change is *not* related to User Context (e.g., Patient Context change).

This method is used in response to an OnPending event to determine if the pending change is User Context related, and if so, whether the User value in the Context Vault has been cleared. If the value has been cleared, then the application should shut down. Switching User Context is *not* supported, since Office of Cyber and Information Security (OCIS) policy indicates that the current user *must* sign off the client workstation and the new user *must* sign on the client workstation.

![](xwb-1-1-73-developer-s-guide/203.png) REF: For an example of the IsUserContextPending method, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### lstCall Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

procedure lstCall(OutputBuffer: Tstrings;

The lstCall method executes a remote procedure on the VistA M Server and returns the results into the passed Tstrings- or TStringList-type variable, which you create outside of the call. It is important to free the [memory](#troubleshooting_memory_leaks_htm) later. lstCall expects the name of the remote procedure and its parameters to be set up in the <u>RemoteProcedure Property</u> and <u>Param Property</u> respectively. The <u>Results Property</u> is *not* affected by this call. If the <u>ClearParameters Property</u> is True, then the <u>Param Property</u> is cleared after the call finishes.

![](xwb-1-1-73-developer-s-guide/204.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

![](xwb-1-1-73-developer-s-guide/205.png) NOTE: Whenever the Broker makes a call to the VistA M Server, if the cursor is crDefault, the cursor is automatically changed to the hourglass symbol as seen in other Microsoft-compliant software. If the application has already modified the cursor from crDefault to something else, the Broker does not change the cursor.

![](xwb-1-1-73-developer-s-guide/206.png) REF: For a demonstration using the lstCall method, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 15</u> demonstrates the use of the <u>lstCall Method</u> in a hypothetical example of bringing back a list of user’s keys and automatically filling a list box with data:

<span id="_Ref446321660" class="anchor"></span>Figure 14: lstCall Method—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.RemoteProcedure := ‘GET MY KEYS’;

brkrRPCBroker1.lstCall(ListBox1.Items);

end;

![](xwb-1-1-73-developer-s-guide/207.png) REF: For a demonstration using the <u>lstCall Method</u>, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### pchCall Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Declaration

function pchCall: Pchar;

The pchCall function is the lowest level call used by the <u>TRPCBroker Component</u> and each of the other Call methods (i.e., <u>Call Method</u>, <u>strCall Method</u>, and <u>lstCall Method</u>), which are implemented via pchCall. The return value is a Pchar, which can contain anything from a NULL string, a single text string, or many strings each separated by Return and/or Line Feed characters. For converting multiple lines within the return value into a Tstrings, use the SetText method of the Tstrings.

### Order Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

function Order(const StartSubscript: string; Direction: integer): string;

#### Description

The Order method works very similar to the [\$ORDER](#_Toc384204759) function in M. Using the Order method, you can traverse through the list of elements in the <u>Mult Property</u> of an RPC parameter.

The StartSubscript parameter is the subscript of the element whose next or previous sibling is returned. If the Direction parameter is a positive number, then the subscript of the following element is returned, while if it is 0 or negative, then the predecessor’s subscript is returned. If the list is empty, or there are no more elements beyond the StartSubscript parameter, then empty string is returned. You can use the empty string as a StartSubscript parameter; then, depending on the Direction parameter, you get the subscript of the first or the last element in the list.

There are some important differences between this Order method and the M [\$ORDER](#_Toc384204759) function:

- The Order method requires both parameters to be passed in.
- If the StartSubscript parameter is *not* an empty string, it *must* be equal to one of the subscripts in the list; otherwise, an empty string is returned.
- It is case-sensitive.
- Unlike arrays in M, elements in TMult may or may not be in alphabetical order, depending on the <u>Sorted Property</u>; so, Order may not return the next or previous subscript in collating sequence.

![](xwb-1-1-73-developer-s-guide/208.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TMult Class</u>, see the “<u>RPC Limits</u>” section.

#### Example

The program code in <u>Figure 16</u> demonstrates how to get the next and previous elements in a TMult list:

<span id="_Ref445382486" class="anchor"></span>Figure 15: Order Method—Sample Code to Get the Next and Previous Elements in a TMult List

procedure TForm1.Button1Click(Sender: TObject);

var

Mult: TMult;

Subscript: string;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

Mult\[‘First’\] := ‘One’;

*{Store element pairs one by one}*

Mult\[‘Second’\] := ‘Two’;

Mult\[‘Third’\] := ‘Three’;

Mult\[‘Fourth’\] := ‘Four’;

*{Subscript is Fourth}*

Subscript := Mult.Order(‘Third’,1);

*{Subscript isnd}*

Subscript := Mult.Order(‘Third’,-1);

*{Subscript is* ‘’*. THIRD subscript does not exist}*

Subscript := Mult.Order(‘THIRD’,1);

*{Subscript is First}*

Subscript := Mult.Order(‘’,1);

*{Subscript is Fourth}*

Subscript := Mult.Order(‘’,-1);

end;

### Position Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

function Position(const Subscript: string): longint;

#### Description

The Position method takes the string subscript of an item in a TMult variable and returns its numeric index position, much like a TStringList’s IndexOf method. Because TMult uses a TStringList internally, the IndexOf method is used to implement the Position method. The first position in the TMult is 0. If TMult is empty, or the Subscript does *not* identify an existing item, Position returns -1.

The Position and Subscript methods are the reciprocals of each other.

![](xwb-1-1-73-developer-s-guide/209.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TMult Class</u>, see the “<u>RPC Limits</u>” section.

#### Example

The program code in <u>Figure 17</u> demonstrates how to get the position of an item in a TMult variable:

<span id="_Ref446321665" class="anchor"></span>Figure 16: Position Method—Sample Code that Shows How to Get the Position of an Item in a TMult Variable

procedure TForm1.Button1Click(Sender: TObject);

var

Mult: TMult;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

Label1.Caption := ‘The position of the ‘‘Third’’ element is ‘ +

*{is -1 since the list is empty}*

IntToStr(Mult.Postion(‘Third’));

Mult\[‘Second’\] := ‘Two’;

Label1.Caption := ‘The position of the ‘‘Third’’ element is ‘ +

*{is -1 since ‘Third’ item does not exit}*

IntToStr(Mult.Postion(‘Third’));

Label1.Caption := ‘The position of the ‘‘Second’’ element is ‘ +

*{is 0, TMult positions start with 0}*

IntToStr(Mult.Postion(‘Second’));

end;

### strCall Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

function strCall: string;

The strCall method executes a remote procedure on the VistA M Server and returns the results as a value of a function. The strCall method expects the name of the remote procedure and its parameters to be set up in the <u>RemoteProcedure Property</u> and <u>Param Property</u> respectively. The <u>Results Property</u> is not affected by this call. If the <u>ClearParameters Property</u> is True, then the <u>Param Property</u> is cleared after the call finishes.

![](xwb-1-1-73-developer-s-guide/210.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

![](xwb-1-1-73-developer-s-guide/211.png) NOTE: Whenever the Broker makes a call to the VistA M Server, if the cursor is crDefault, the cursor is automatically changed to the hourglass symbol as seen in other Microsoft-compliant software. If the application has already modified the cursor from crDefault to something else, the Broker does *not* change the cursor.

![](xwb-1-1-73-developer-s-guide/212.png) REF: For a demonstration using the strCall method, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 18</u> demonstrates the use of the <u>strCall Method</u> in a hypothetical example of bringing back the name of the user currently logged on and automatically displaying it in a label:

<span id="_Ref445382674" class="anchor"></span>Figure 17: strCall Method—Sample Code Showing the Use of the strCall Method

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.RemoteProcedure := ‘GET CURRENT USER NAME’;

Label1.Caption := brkrRPCBroker1.strCall;

end;

![](xwb-1-1-73-developer-s-guide/213.png) REF: For a demonstration using the <u>strCall Method</u>, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe) located in the following directory:

BDK32\Samples\BrokerEx

### Subscript Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

function Subscript(const Position: longint): string;

#### Description

The Subscript method takes the numeric position of an item in a TMult variable and returns its string subscript. If TMult is empty, or the Position is greater than the number of items in the list, an empty string is returned.

The Subscript method and <u>Position Method</u> are the reciprocals of each other.

![](xwb-1-1-73-developer-s-guide/214.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TMult Class</u>, see the “<u>RPC Limits</u>” section.

#### Example

The program code in <u>Figure 19</u> demonstrates how to get the subscript of an item in a TMult variable:

<span id="_Ref446321673" class="anchor"></span>Figure 18: Subscript Method—Example

procedure TForm1.Button1Click(Sender: TObject);

var

Mult: TMult;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

Label1.Caption := ‘The subscript of the item at position 1 is ’ +

*{is empty since the list is empty}*

Mult.Subscript(1);

Mult\[‘Second’\] := ‘Two’;

Label1.Caption := ‘The subscript of the item at position 1 is ’ +

*{is empty. Only one item in list so far at 0th position}*

Mult.Subscript(1);

Mult\[‘Third’\] := ‘Three’;

Label1.Caption := ‘The subscript of the item at position 1 is ’ +

*{is Third}*

Mult.Subscript(1);

end;

### WasUserDefined Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

function WasUserDefined: Boolean;

The WasUserDefined method is used to determine whether or not a User Context is currently or was previously defined in the Context Vault. It returns True any time after the initial establishment of User Context. This method returns:

- True—CCOW User Context established.
- False—CCOW User Context *not* established.

This method is used in response to an OnPending event to determine if the pending change is User Context related, and if so, whether the User value in the Context Vault has been cleared. If the value has been cleared, then the application should shut down. Switching User Context is *not* supported, since Office of Cyber and Information Security (OCIS) policy indicates that the current user *must* sign off the client workstation and the new user *must* sign on the client workstation.

#### Example

In the event handler for the Commit event of the TContextorControl, developers can check whether or not the user was previously defined and is now undefined or NULL. In this case, developers would want to do any necessary processing, and then halt.

<span id="_Toc82593580" class="anchor"></span>Figure 19: WasUserDefined Method—Example

Procedure TForm1.CommitHandler(Sender: TObject);

beginwith CCOWRPCBroker1 doif WasUserDefined and IsUserCleared thenbegin

*// do any necessary processing before halting*

halt;

end;

end;

## Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TLoginMode Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TLoginMode type is used with the <u>Mode Property</u> as part of the <u>TVistaLogin Class</u>.

#### Unit

<u>TRPCB Unit</u>

type TLoginMode = (lmAVCodes, lmAppHandle);

#### Description

The TLoginMode type includes the acceptable values that can be used during <u>Silent Login</u>. If the <u>KernelLogIn Property</u> is set to False, then it is a <u>Silent Login</u>. Thus, one of these mode types has to be set in the <u>TVistaLogin Class</u> <u>Mode Property</u>. The Broker uses the information to perform a <u>Silent Login</u>.

<u>Table 10</u> lists the possible values:

| Value           | Meaning                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lmAVCodes   | Used if the application is passing in the user’s Access and Verify codes during <u>Silent Login</u>.                                                                                                                                                                                                                                      |
| lmAppHandle | Used to pass in an application handle rather than a user’s Access and Verify codes during <u>Silent Login</u>. It sets the mode to lmAppHandle and the <u>KernelLogIn Property</u> to False. Indicates that an application handle is being passed to the application when it was being started as opposed to Access and Verify codes. |

<span id="_Ref384646557" class="anchor"></span>Table 11: PType Property—Values

### TParamType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Unit

<u>TRPCB Unit</u>

#### Declaration

TParamType = ([literal](#literal), [reference](#reference), [list](#list), [global](#global), [empty](#empty), [stream](#stream), [undefined)](#undefined);

#### Description

The TParamType type defines the possible values of the [RPC](#rpcs_rpc_overview_htm) parameter type (<u>PType Property</u> of <u>TParamRecord Class</u>).

The [global](#global), [empty](#empty), and [stream](#stream) values (added with RPC Broker Patch XU\*1.1\*40) can only be used if a new-style (i.e., *non-*callback) connection is present.

![](xwb-1-1-73-developer-s-guide/215.png) CAUTION: Use of the [undefined](#undefined) TParam Type in applications is *not* supported. It exists for the RPC Broker’s *internal use only*.

## Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### AccessCode Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property AccessCode: String;

#### Description

The AccessCode property (RunTime) holds the Access code for the lmAVCodes mode of <u>Silent Login</u>. The user’s Access code value should be set in as clear text. It is encrypted before it is transmitted to the VistA M Server.

![](xwb-1-1-73-developer-s-guide/216.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

![](xwb-1-1-73-developer-s-guide/217.png) REF: For more information on Access codes, see the “Part 1: Sign-On/Security” section in the *Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide*.

### BrokerVersion Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property BrokerVersion: String;

#### Description

The BrokerVersion property (RunTime) is a read-only property that indicates the RPC Broker version used in generating the application (currently, it returns the string “XWB\*1.1\*60”).

### CCOWLogonIDName Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonIDName: String;

#### Description

The CCOWLogonIDName property (RunTime) is a read-only property that is the name used within the CCOW Context Vault to store the LogonId.

It permits the user to identify the logon ID name associated with the <u>CCOWLogonIDValue Property (read-only)</u> logon ID name value used within the Context Vault related to User Context.

### CCOWLogonIDValue Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonIDValue: String;

#### Description

The CCOWLogonIDValue property (RunTime) is a read-only property that gives the value currently associated with the LogonId in the CCOW Context Vault.

It permits the user to identify the logon ID value associated with the <u>CCOWLogonIDName Property (read-only)</u> logon ID name used within the Context Vault related to User Context.

### CCOWLogonName Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonName: String;

#### Description

The CCOWLogonName property (RunTime) is a read-only property that gives the name used to store the LogonName of the currently active user.

It permits the user to identify the logon name associated with the <u>CCOWLogonNameValue Property (read-only)</u> logon name value used within the Context Vault related to User Context.

### CCOWLogonNameValue Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonNameValue: String;

#### Description

The CCOWLogonNameValue property (RunTime) is a read-only property that gives the value of the LogonName of the currently active user.

It permits the user to identify the logon name value associated with the <u>CCOWLogonName Property (read-only)</u> logon name used within the Context Vault related to User Context.

### CCOWLogonVpid Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonVpid: String;

#### Description

The CCOWLogonVpid property (RunTime) is a read-only property gthat ives the name used to store the LogonVpid value in the CCOW Context Vault.

It permits the user to identify the logon VA Person Identification (VPID) name associated with the <u>CCOWLogonVpidValue Property (read-only)</u> logon VPID value used within the Context Vault related to User Context.

### CCOWLogonVpidValue Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property CCOWLogonVpidValue: String;

#### Description

The CCOWLogonVpidValue property (RunTime) is a read-only property that gives the value of the VA Person Identification (VPID) value for the currently logged on user, if the facility has been enumerated; otherwise, the value returned is a NULL string.

It permits the user to identify the logon VPID value associated with the <u>CCOWLogonVpid Property (read-only)</u> logon VPID name used within the Context Vault related to User Context.

### ClearParameters Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property ClearParameters: Boolean;

#### Description

The ClearParameters property (DesignTime) gives the developer the option to clear the <u>Param Property</u> after every invocation of any of the following methods:

- <u>Call Method</u>
- <u>strCall Method</u>
- <u>lstCall Method</u>

Setting ClearParameters to True clears the <u>Param Property</u>.

Simple assignment of True to this property clears the <u>Param Property</u> *after* every invocation of the <u>Call Method</u>, <u>strCall Method</u>, and <u>lstCall Method</u>. Thus, the parameters need only be prepared for the *next* call *without* being concerned about what was remaining from the previous call.

By setting ClearParameters to False, the developer can make multiple calls with the same <u>Param Property</u>. It is also appropriate to set this property to False when a majority of the parameters in the <u>Param Property</u> should remain the same between calls. However, minor changes to the parameters can still be made.

#### Example

The program code in <u>Figure 21</u> sets the <u>ClearParameters Property</u> to True:

<span id="_Ref446321721" class="anchor"></span>Figure 20: ClearParameters Property—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.ClearParameters  := True;

end;

### ClearResults Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property ClearResults: Boolean;

#### Description

The ClearResults property (DesignTime) gives the developer the option to clear the <u>Results Property</u> prior to every invocation of the <u>Call Method</u>. The <u>strCall Method</u> and <u>lstCall Method</u> are unaffected by this property. Setting ClearResults to True clears the <u>Results Property</u>.

If this property is True, then the <u>Results Property</u> is cleared *before* every invocation of the <u>Call Method</u>; thus, assuring that only the results of the last call are returned. Conversely, a setting of False accumulates the results of multiple calls in the <u>Results Property</u>.

#### Example

The program code in <u>Figure 22</u> sets the <u>ClearResults Property</u> to True:

<span id="_Ref446321755" class="anchor"></span>Figure 21: ClearResults Property—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.ClearResults := True;

end;

### Connected Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

property Connected: Boolean;

#### Description

The Connected property (DesignTime) connects the application to the VistA M Server:

- Setting this property to True connects the application to the server.
- Setting it to False disconnects the application from the server.

It is *not* necessary for your application to manually establish a connection to the VistA M Server. RPC Broker 1.1 automatically connects and disconnects from the server. When you invoke an RPC, if a connection has *not* already been established, one is established for you. However, a user is *not* able to run the RPC unless a context has been created with the <u>CreateContext Method</u>.

The Connected property is also used to authenticate a user into a VistA M Server. After making the connection, it makes a call to Identity and Access Management (IAM) Secure Token Service (STS) for 2-factor authentication (2FA) of the user. The STS returns a token, which is used to authenticate the user into a VistA M Server. If a token *cannot* be obtained, VistA user authentication fails over to Access and Verify codes.

There are other advantages to establishing a connection manually. You can check if a connection is established, and branch accordingly depending on whether or not a connection was established. One good place to do this is in the application form’s OnCreate event. For that event, you could include code as shown in <u>Figure 23</u>:

<span id="_Ref446321810" class="anchor"></span>Figure 22: Connected Property—Example (1 of 2)

try

brkrRPCBroker1.Connected:= True;

excepton EBrokerError dobegin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

end;

end;

This code sets the <u>TRPCBroker Component</u>’s Connected property to True to establish a connection. If a Broker exception (i.e., <u>EBrokerError</u>) was raised (in which case the connection was *not* established), it provides a message to the user and calls the Terminate method to exit.

To verify that your application is connected to the VistA M Server, check the value of the Connected property.

If a connected <u>TRPCBroker Component</u> is destroyed (e.g., when the application is closed) that component first disconnects from the VistA M Server. However, for programming clarity, it is advisable to disconnect your application from the server manually by setting the Connected property to False.

If your application uses more than one Broker component, you should be aware of the component’s connect and disconnect behavior.

![](xwb-1-1-73-developer-s-guide/218.png) REF: For more information on connect-disconnect behavior, see the “<u>Component Connect-Disconnect Behavior</u>” section.

#### Example

The program code in <u>Figure 24</u> sets the <u>Connected Property</u> to True:

<span id="_Ref446321842" class="anchor"></span>Figure 23: Connected Property—Example (2 of 2)

procedure TForm1.btnConnectClick(Sender: TObject);

begin

brkrRPCBroker1.Server := edtServer.Text;

brkrRPCBroker1.ListenerPort := StrToInt(edtPort.Text);

brkrRPCBroker1.Connected := True;

end;

![](xwb-1-1-73-developer-s-guide/219.png) NOTE: The <u>Server Property</u> and <u>ListenerPort Property</u> *must* be set at design or run time before setting the <u>Connected Property</u> to True.

### Contextor Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TCCOWRPCBroker Component</u>

#### Declaration

property Contextor: TContextorControl;

read Fcontextor write FContextor; *//CCOW*

#### Description

The Contextor property (RunTime) *must* be set to an active instance of the TContextorControl component in order to initiate a login with CCOW User Context. If it is *not* set to an active instance, then the component basically reverts to an instance of a <u>TRPCBroker Component</u>, since none of the features of CCOW User Context is used.

![](xwb-1-1-73-developer-s-guide/220.png) NOTE: The TContextorControl component is the interface for the Sentillion Vergence ContextorControl that communicates with the Context Vault. The component is created based on the type library for the DLL.  
  
Since developers may want to use the TContextorControl component to initialize their own instances, the TContextorControl component is placed on the Kernel palette in Delphi; however, it is almost as easy to simply create it at run-time without using a component.

### Count Property (TMult Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

property Count: Word;

#### Description

The Count property (DesignTime) contains the number of items in a <u>TMult Class</u>. If <u>TMult Class</u> is empty, Count is zero.

#### Example

The program code in <u>Figure 25</u> displays the number of items in a Mult class in the caption of a label when the user clicks the CountItems button:

<span id="_Ref446321869" class="anchor"></span>Figure 24: Count Property (TMult Class)—Example

procedure TForm1.CountItemsClick(Sender: TObject);

begin

Label1.Caption := ‘There are ’ + IntToStr(Mult.Count) + ‘ items in the Mult.’

end;

### Count Property (TParams Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TParams Class</u>

#### Declaration

property Count: Word;

#### Description

The Count property contains the number of parameters in a <u>TParams Class</u>. If the <u>TParams Class</u> is empty, Count is zero.

#### Example

The program code in <u>Figure 26</u> displays the number of parameters in a TParams variable within the caption of a label when the user clicks the CountParameters button:

<span id="_Ref446321896" class="anchor"></span>Figure 25: Count Property (TParams Class)—Example

procedure TForm1.CountParametersClick(Sender: TObject);

begin

Label1.Caption := ‘There are ’ + IntToStr(brkrRPCBroker1.Param.Count) + ‘ parameters.’;

end;

### CurrentContext Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property CurrentContext: String;

#### Description

The CurrentContext property (RunTime) is a read-only property that provides the current context. Developers can:

- Save off the current context into a local variable.
- Set a new context.
- Restore the original context from the local variable before finishing.

This permits the application to use the <u>CreateContext Method</u> with an additional context when an initial context has already been established.

#### Example

The program code in <u>Figure 27</u> demonstrates the use of the <u>CurrentContext Property (read-only)</u> in a hypothetical example of saving and restoring the current context of an application:

<span id="_Ref446321924" class="anchor"></span>Figure 26: CurrentContext Property—Example

procedure TForm1.MyFantasticModule;

var

OldContext: String;

begin

OldContext := RPCB.CurrentContext;  *// save off old context*try

RPCB.SetContext(‘MyContext’);

...finally

RPCB.SetContext(OldContext);  *// restore context before leaving*end;

end;

### DebugMode Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property DebugMode: Boolean;

#### Description

The DebugMode property (DesignTime) formerly controlled how the VistA M Server process should be started. The default setting is False. Setting this property to True has no effect on the VistA M Server process. Control of debugging has been moved from the client to the server.

For debugging purposes, it can be very helpful to:

1.  Set break points.
18. Run the server process interactively.
19. Step through the execution.

![](xwb-1-1-73-developer-s-guide/221.png) REF: For more information, see the “<u>How to Debug the Application</u>” section.

### Division Property (TVistaLogin Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property Division: String;

#### Description

The Division property (RunTime) can be set to the desired division for a user for <u>Silent Login</u>.

![](xwb-1-1-73-developer-s-guide/222.png) REF: For information about handling multi-divisions during the <u>Silent Login</u> process, see the “<u>Handling Divisions during Silent Login</u>” section.

### Division Property (TVistaUser Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

property Division: String;

#### Description

The Division property (RunTime) is set to the division for a user when they are logged on.

### DivList Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property DivList: Tstrings;

#### Description

The DivList property (RunTime) is a read-only property that is a list of divisions that are available for selection by the user for the signon division. This list is filled in, if appropriate, during the <u>Silent Login</u> at the same time that the user is determined to have multiple divisions from which to select. The first entry in the list is the number of divisions present, followed by the names of the divisions that are available to the user.

![](xwb-1-1-73-developer-s-guide/223.png) REF: For information about handling multi-divisions during the <u>Silent Login</u> process, see the “<u>Handling Divisions during Silent Login</u>” section.

### DomainName Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property DomainName: String;

#### Description

The DomainName property (RunTime) can be used to obtain the domain name of the server to which the RPC Broker is currently connected.

### DTime Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property DTime: String;

#### Description

The DTime property (RunTime) holds the user’s DTime. DTime sets the time a user has to respond to timed read. It can be set from 1 to 99999 seconds.

### DUZ Property (TVistaLogin Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property DUZ: String;

#### Description

The DUZ property (RunTime) holds the user’s Internal Entry Number (IEN) from the NEW PERSON (#200) file for TVistaLogin.

### DUZ Property (TVistaUser Class)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property DUZ: String;

#### Description

The DUZ property (RunTime) holds the user’s Internal Entry Number (IEN) from the NEW PERSON (#200) file for TVistaUser.

### ErrorText Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property ErrorText: String;

#### Description

The ErrorText property (RunTime) holds text of any error message returned by the VistA M Server during the attempted <u>Silent Login</u>. It should be checked if the login fails. For example, it could indicate the following:

- Verify code needs to be changed.
- Invalid Access/Verify code pair.
- Invalid Division.

### First Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

property First: String;

#### Description

The First property (DesignTime) contains the subscript of the first item in a <u>TMult Class</u>. The first item is always in the 0<sup>th</sup> Position. You can think of the First property as a shortcut to executing the TMult.Order(‘’,1) method. If a TMult variable does *not* contain any items, the First property is empty.

![](xwb-1-1-73-developer-s-guide/224.png) REF: For more information, see the “<u>Order Method</u>” and “<u>Position Method</u>” sections.

#### Example

The program code in <u>Figure 28</u> displays the subscript and value of the first item in a Mult variable in the caption of a label when the user clicks the GetFirst button:

<span id="_Ref446321952" class="anchor"></span>Figure 27: First Property—Example

procedure TForm1.GetFirstClick(Sender: TObject);

var

Mult: TMult;

Subscript: string;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

Mult\[‘Fruit’\] := ‘Apple’;

*{Store element pairs one by one)*

Mult\[‘Vegetable’\] := ‘Potato’;

Label1.Caption := ‘The subscript of the first element: ’ + Mult.First + ‘, and its value: ’ + Mult\[Mult.First\];

end;

### IsProductionAccount Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property IsProductionAccount: Boolean;

#### Description

The IsProductionAccount property (RunTime) can be checked to determine if the current connection is to a Production account:

- True—If the account is a Production account.
- False—If the account is *not* a Production account.

While it is declared as a read-write property, it should be considered to be read-only, since changing its value does *not* change the nature of the server to which the RPC Broker is connected.

### KernelLogIn Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property KernelLogIn: Boolean;

#### Description

The KernelLogin property (DesignTime) is a Boolean property, which indicates the manner of signon:

- True—Presents the regular Kernel login security form.
- False—Broker uses the <u>TVistaLogin Class</u> for signon.

The <u>TVistaLogin Class</u> is referenced during <u>Silent Login</u>.

![](xwb-1-1-73-developer-s-guide/225.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### Language Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property Language: String;

#### Description

The Language property (RunTime) holds the user’s language from the NEW PERSON (#200) file.

### Last Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

property Last: String;

#### Description

The Last property (DesignTime) contains the subscript of the last item in a <u>TMult Class</u>. The last item is always in count-1 Position. You can think of the Last property as a shortcut to executing the TMult.Order(‘’,-1) method. If a TMult variable does *not* contain any items, the Last property is empty.

![](xwb-1-1-73-developer-s-guide/226.png) REF: For more information, see the “<u>Order Method</u>” and “<u>Position Method</u>” sections.

#### Example

The program code in <u>Figure 29</u> displays the subscript and value of the last item in a Mult variable in the caption of a label when the user clicks the GetLast button:

<span id="_Ref446321984" class="anchor"></span>Figure 28: Last Property—Example

procedure TForm1.GetLastClick(Sender: TObject);

var

Mult: TMult;

Subscript: string;

begin

*{Create Mult. Make Form1 its owner}*

Mult := TMult.Create(Form1);

Mult\[‘Fruit’\] := ‘Apple’;

*{Store element pairs one by one}*

Mult\[‘Vegetable’\] := ‘Potato’;

Label1.Caption := ‘The subscript of the last element: ’ + Mult.Last + ‘, and its value: ’ + Mult\[Mult.Last\];

end;

### ListenerPort Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property ListenerPort: Integer;

#### Description

The ListenerPort property (DesignTime) gives the developer the ability to select the Listener port on the VistA M Server. It *must always* be set *before* connecting to the server.

If one VistA M Server system has two or more environments (UCIs) that support client/server applications (e.g., Test and Production accounts), the Broker Listener processes *must* be listening on unique ports. Thus, you *must* specify which Listener port to use when you start the Listener on the VistA M Server. Consequently, if you have more than one Listener running on the same server, the application needs to specify the correct Listener for its connection request. This is accomplished using the ListenerPort property.

After the initial connection, the VistA M Server connection is moved to another port number \[i.e., <u>Socket Property (read-only)</u>\], which is used for the remainder of the session.

#### Example

The program code in <u>Figure 30</u> demonstrates using the <u>ListenerPort Property</u>:

<span id="_Ref446322021" class="anchor"></span>Figure 29: ListenerPort Property—Example

procedure TForm1.btnConnectClick(Sender: TObject);

begin

brkrRPCBroker1.ListenerPort := 9001;

brkrRPCBroker1.Connected := True;

end;

### LogIn Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property LogIn: TVistaLogin;

#### Description

The LogIn property (RunTime) holds parameters that the application needs to pass for <u>Silent Login</u>. The instance of the TVistaLogin used for this property is created automatically during the creation of the TRPCBroker object, and is therefore, available for reference as a TRPCBroker property *without* any user setup.

![](xwb-1-1-73-developer-s-guide/227.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### LoginHandle Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property LoginHandle: String;

#### Description

The LoginHandle property (RunTime) holds the Application Handle for the lmAppHandle mode of <u>Silent Login</u>. The Application Handle is obtained from the VistA M Server by a currently running application using the GetAppHandle function in the <u>TRPCB Unit</u>. The function returns a String value, which is then passed as a command line argument with an application that is being started. The new application *must* know to look for the handle, and if present, set up the <u>Silent Login</u>. The StartProgSLogin (see the “<u>StartProgSLogin Method</u>” section) procedure in the <u>RpcSLogin Unit</u> can be used directly or as an example of how the application would be started with a valid AppHandle as a command line argument. The CheckCmdLine procedure (see the “<u>CheckCmdLine Function</u>” section) in the <u>RpcSLogin Unit</u> can be used in an application to determine whether an AppHandle has been passed and to initiate the Broker connection or used as an example of how this could be done.

![](xwb-1-1-73-developer-s-guide/228.png) NOTE: The two procedures referenced here also pass the current values from the <u>Server Property</u>, <u>ListenerPort Property</u>, and <u>Division Property (TVistaLogin Class)</u> for the user so that the connection would be made to the same VistA M Server as the original application.  
  
The AppHandle that is obtained via the GetAppHandle function is only valid for approximately 20 seconds, after which the <u>Silent Login</u> would fail.

### Mode Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property Mode: TloginMode;

#### Description

The Mode property (RunTime) indicates the mode of <u>Silent Login</u>. The possible values include:

- lmAVCodes
- lmAppHandle

![](xwb-1-1-73-developer-s-guide/229.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### Mult Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TParamRecord Class</u>

#### Declaration

property Mult: TMult;

#### Description

(Mult is a property of the <u>TParamRecord Class</u> used in the <u>Param Property</u>.)

The Mult property (DesignTime) of a <u>TParamRecord Class</u>, which is the type of each <u>TRPCBroker Component</u>’s Param\[x\] element, can be used to pass a string-subscripted array of strings to the VistA M Server. For example, if you need to pass a patient’s name and Social Security Number (SSN) to a remote procedure, you could pass them as two separate parameters as PType literals, or you could pass them in one parameter using the Mult property as a PType list. If one is being sent, a Mult *must* be the last element in the Param array.

#### Example

The program code in <u>Figure 31</u> demonstrates how the <u>Mult Property</u> can be used to pass several data elements to the VistA M Server in one parameter:

<span id="_Ref446322059" class="anchor"></span>Figure 30: Mult Property—Example (1 of 2)

procedure TForm1.Button1Click(Sender: TObject);

beginwith brkrRPCBroker1 do begin

Param\[0\].PType :=list;

Param\[0\].Mult\[‘“NAME”’\] := ‘XWBBROKER,ONE’

Param\[0\].Mult\[‘“SSN”’\] := ‘000456789’;

RemoteProcedure := ‘SETUP PATIENT INFO’;

Call;

end;

end;

Assuming variable P1 is used on the VistA M Server to receive this array, it would look like <u>Figure 32</u>:

<span id="_Ref446322127" class="anchor"></span>Figure 31: Mult Property—Example (2 of 2)

P1(“NAME”)=XWBBROKER,ONE

P1(“SSN”)=000456789

### MultiDivision Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property MultiDivision: Boolean;

#### Description

The MultiDivision property (RunTime) indicates whether the user has multi-divisional access. It is set during the <u>Silent Login</u> process, if the user has more than one division that can be selected.

![](xwb-1-1-73-developer-s-guide/230.png) REF: For information about handling multi-divisions during the <u>Silent Login</u> process, see the “<u>Handling Divisions during Silent Login</u>” section.

### Name Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

TVistaUser Class

#### Declaration

property Name: String;

#### Description

The Name property (RunTime) holds the user’s name from the NEW PERSON (#200) file.

### OnFailedLogin Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property OnFailedLogin: TOnLoginFailure;

#### Description

The OnFailedLogin property (RunTime) holds a procedure to be invoked on a failed <u>Silent Login</u> that permits an application to handle errors as desired; where TOnLoginFailure is defined as:

TOnLoginFailure = procedure (VistaLogin: TVistaLogin) of object;

For example, an application could define:

Procedure HandleLoginError(Sender: TObject);

And then set:

OnFailedLogin := HandleLoginError;

![](xwb-1-1-73-developer-s-guide/231.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### OnRPCBFailure Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property OnRPCBFailure: TOnRPCBFailure;

#### Description

The OnRPCBFailure property (RunTime) holds a procedure to be invoked when the Broker generates an exception that permits an application to handle errors as desired, where TOnRPCBFailure is defined as:

TOnRPCBFailure = procedure (RPCBroker: TRPCBroker) of object;

The text associated with the error causing the exception is found in the <u>RPCBError Property (read-only)</u>.

![](xwb-1-1-73-developer-s-guide/232.png) NOTE: If the <u>OnFailedLogin Property</u> is also set, it handles any login errors and does *not* pass them up.

#### Example

For example, an application could define:

Procedure HandleBrokerError(Sender: TObject);

And then set:

OnRPCBFailure := HandleBrokerError;

![](xwb-1-1-73-developer-s-guide/233.png) NOTE: The initialization of the OnRPCBFailure property should be before the first call to the <u>TRPCBroker Component</u>.

<u>Figure 33</u> shows an instance of an error handler that takes the Message property of the exception and stores it with a time date stamp into a file named Error.Log in the same directory with the application exe:

<span id="_Ref446322260" class="anchor"></span>Figure 32: Error Handler—Example of Storing a Message with a Time Date Stamp

procedure TForm1.HandleBrokerError(Sender: TObject);

var

ErrorText: String;

Path: String;

StrLoc: TStringList;

NowVal: TDateTime;

begin

NowVal := Now;

ErrorText := TRPCBroker(Sender).RPCBError;

StrLoc := TStringList.Create;

try

Path := ExtractFilePath(Application.ExeName);

Path := Path + ‘Error.Log’;

if FileExists(Path) then

StrLoc.LoadFromFile(Path);

StrLoc.Add(FormatDateTime(‘mm/dd/yyyy hh:mm:ss ’,NowVal) + ErrorText);

StrLoc.SaveToFile(Path);

finally

StrLoc.Free;

end;

end;

### Param Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property Param: TParams;

#### Description

The Param property (RunTime) holds all of the parameters that the application needs to pass to the remote procedure using any of the following methods:

- <u>Call Method</u>
- <u>strCall Method</u>
- <u>lstCall Method</u>

Param is a zero-based array of the <u>TParamRecord Class</u>. You do *not* need to explicitly allocate any memory for the Param property. Simple reference to an element or a value assignment ( := ) dynamically allocates memory as needed. You should start with the 0<sup>th</sup> element and proceed in sequence. Do *not* skip elements.

Each element in the Param array has the following properties:

- <u>Mult Property</u>
- <u>PType Property</u>
- <u>Value Property</u>

![](xwb-1-1-73-developer-s-guide/234.png) CAUTION: Passing multiple parameters of PType list in one remote procedure call (RPC) is *not* supported at this time. Only one list parameter can be passed to an RPC, and it *must* be the last parameter in the actual list.

The Param relationship to the <u>TRPCBroker Component</u> is as follows:

The <u>TRPCBroker Component</u> contains the Param property (i.e., <u>TParams Class</u>).

The <u>TParams Class</u> contains the ParamArray property (array \[I:integer\]: <u>TParamRecord Class</u>).

The <u>TParamRecord Class</u> contains the <u>Mult Property</u> (i.e., <u>TMult Class</u>).

The <u>TMult Class</u> contains the MultArray property (array\[S: string\]: string).

The MultArray property internally uses a TStringList in which each element’s object is a TString.

If the remote procedure on the VistA M Server does *not* require any incoming parameters, applications can pass an empty Param property. The client application merely sets the <u>RemoteProcedure Property</u> and makes the call. If the Param property retains a value from a previous call, it can be cleared using the <u>ClearParameters Property</u>. Thus, it is possible to make a call without passing any parameters.

![](xwb-1-1-73-developer-s-guide/235.png) CAUTION: The following restrictions apply with the Param property:

> 1\. You are *not* allowed to “skip” passing parameters, such as TAG^ROUTINE(1,,3). If there are fewer elements in the Param array than exist as input parameters in the [RPC](#rpcs_rpc_overview_htm), the subsequent parameters are *not* passed to the RPC.

> 2\. Passing multiple array parameters in one remote procedure call is *not* supported at this time. Only one array parameter can be passed to an [RPC](#rpcs_rpc_overview_htm), and it *must* be the last parameter in the actual list.

![](xwb-1-1-73-developer-s-guide/236.png) REF: For a demonstration using the <u>Param Property</u>, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 34</u> demonstrates how the <u>Param Property</u> of a <u>TRPCBroker Component</u> is referenced and filled with two parameters that the remote procedure expects:

<span id="_Ref446322308" class="anchor"></span>Figure 33: Param Property—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

*{first parameter is a single string}*

brkrRPCBroker1.Param\[0\].Value := ‘02/27/14’;

brkrRPCBroker1.Param\[0\].PType := literal;

*{second parameter is a list}*

brkrRPCBroker1.Param\[1\].Mult\[‘“NAME”’\] := ‘XWBUSER,ONE’;

brkrRPCBroker1.Param\[1\].Mult\[‘“SSN”’\] := ‘000-45-6789’;

brkrRPCBroker1.Param\[1\].PType := list;

end;

![](xwb-1-1-73-developer-s-guide/237.png) REF: For a demonstration using the <u>Param Property</u>, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### PromptDivision Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property PromptDivison: Boolean;

#### Description

The PromptDivision property (RunTime) should be set to:

- True—If the user should be prompted for Division during <u>Silent Login</u>. The prompt only occurs if the user has multi-division access.
- False—If the prompt should *not* be displayed due to the manner in which the application is running.

However, if set to False and multi-division access is a possibility, then the application *must* handle it in another way. For example, the application developer would do the following:

1.  Set Login.PromptDivision to False.
20. Set the <u>Connected Property</u> to True to signon.
21. On return, check whether the <u>Connected Property</u> was set to True or check whether the Login.<u>ErrorText Property</u> was *non*-NULL (and especially “No Division Selected”).
22. If the connection was successful, there is no problem; otherwise, proceed to Steps 5 - 8.
23. Check the Login.<u>MultiDivision Property</u> and see if it was set to True, which is expected.
24. If the Login.<u>MultiDivision Property</u> is set to True, check the Login.<u>DivList Property (read-only)</u> for a list of the available divisions (remember the first entry is the number of entries that follow), and in whatever method was available to the application, have the user select the correct division.
25. Set the Login.<u>Division Property (TVistaLogin Class)</u> to the selected division.
26. Set the <u>Connected Property</u> to True, so the connection would be attempted to be established again.

![](xwb-1-1-73-developer-s-guide/238.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### PType Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TParamRecord Class</u>

#### Declaration

property PType: <u>TParamType</u>;

#### Description

PType is a property of the <u>TParamRecord Class</u> used in the <u>Param Property</u>.

The PType property (DesignTime) determines how the parameter is interpreted and handled by the Broker.

<table>
<caption><p><span id="_Ref384101411" class="anchor"></span>Table 12: ShowErrorMsgs Property—Values</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="literal" class="anchor"></span><strong>literal</strong></td>
<td>Delphi string value; passed as a string literal to the VistA M server. The VistA M Server receives the contents of the corresponding <u>Value Property</u> as one string or one number.</td>
</tr>
<tr class="even">
<td><span id="reference" class="anchor"></span><strong>reference</strong></td>
<td><p>Delphi string value; treated on the VistA M Server as an M variable name and resolved from the symbol table at the time the RPC executes. The VistA M Server receives the contents of the corresponding <u>Value Property</u> as a name of a variable defined on the server. Using indirection, the Broker on the server resolves this parameter before handing it off to the application.</p>
<p>![](xwb-1-1-73-developer-s-guide/239.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.</p></td>
</tr>
<tr class="odd">
<td><span id="list" class="anchor"></span><strong>list</strong></td>
<td>A single-dimensional array of strings in the <strong>Mult</strong> subproperty of the <u>Param Property</u>; passed to the VistA M Server where it is placed in an array. String subscripting can be used. This value is used whenever an application wants to send a list of values to the VistA M Server. Data is placed in a local array. In this case, the content of the corresponding <u>Mult Property</u> is sent, while the <u>Value Property</u> is ignored.</td>
</tr>
<tr class="even">
<td><span id="global" class="anchor"></span><strong>global</strong></td>
<td>This value is similar to list, but instead of data being placed in a local array, it is placed in a global array. Use of this value removes the potential problem of allocation errors when large quantities of data are transmitted.</td>
</tr>
<tr class="odd">
<td><span id="empty" class="anchor"></span><strong>empty</strong></td>
<td>This value indicates that no parameter value is to be passed; it simply passes an empty argument.</td>
</tr>
<tr class="even">
<td><span id="stream" class="anchor"></span><strong>stream</strong></td>
<td>This value indicates that the data should be passed as a single stream of data.</td>
</tr>
<tr class="odd">
<td><span id="undefined" class="anchor"></span><strong>undefined</strong></td>
<td>The Broker uses this value internally. It should <em>not</em> be used by an application.</td>
</tr>
</tbody>
</table>

<span id="_Ref384101411" class="anchor"></span>Table 12: ShowErrorMsgs Property—Values

For instance, if you need to pass an empty string to the remote procedure call (RPC), the <u>Value Property</u> should be set to ‘’ (i.e., NULL) and the PType to literal. Using reference, a developer can pass an M variable (e.g., DUZ) without even knowing its value. However, if the M variable being referenced is *not* defined on the VistA M Server, a run-time error occurs. When passing a list to an RPC:

1.  Set the PType to list.
27. Populate the <u>Mult Property</u>.
28. Do *not* put anything into the <u>Value Property</u> (in this case, Value is ignored).

![](xwb-1-1-73-developer-s-guide/240.png) REF: For a demonstration using PType, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

The program code in <u>Figure 35</u> demonstrates a couple of different uses of the <u>PType Property</u>. Remember, that each Param\[x\] element is really a <u>TParamRecord Class</u>.

<span id="_Ref446322523" class="anchor"></span>Figure 34: PType Property—Example

procedure TForm1.Button1Click(Sender: TObject);

beginwith brkrRPCBroker1 do begin

RemoteProcedure := ‘SET NICK NAME’;

Param\[0\].Value := ‘DUZ’;

Param\[0\].PType := reference;

Param\[1\].Value := edtNickName.Text;

Param\[1\].PType := literal;

Call;

end;

end;

![](xwb-1-1-73-developer-s-guide/241.png) REF: For a demonstration using PType, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### RemoteProcedure Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property RemoteProcedure: TRemoteProc;

#### Description

The RemoteProcedure property (DesignTime) should be set to the name of the remote procedure call entry in the <u>REMOTE PROCEDURE (#8994) File</u>.

#### Example

The program code in <u>Figure 36</u> demonstrates using the <u>RemoteProcedure Property</u>:

<span id="_Ref446322554" class="anchor"></span>Figure 35: RemoteProcedure Property—Example

procedure TForm1.Button1Click(Sender: TObject);

begin

brkrRPCBroker1.RemoteProcedure := ‘MY APPLICATION REMOTE PROCEDURE’;

brkrRPCBroker1.Call;

end;

### Results Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property Results: Tstrings;

#### Description

The Results property (DesignTime) contains the results of a <u>Call Method</u>. In the case where the RPC returns a single value, it is returned in Results\[0\]. If a call returns a list of values, the Results property is filled in the order the list collates on the VistA M Server. The Results property can only contain values of array elements—subscripts are *not* returned.

For example:

On the VistA M Server, the M routine constructs the list in the sequence shown in <u>Figure 37</u>:

<span id="_Ref446322587" class="anchor"></span>Figure 36: Results Property—Sample Array List Sequence

S LIST(“CCC”)=“First”

S LIST(1)=“Second”

S LIST(“AAA”)=“Third”

S LIST(2)=“Fourth”

Before Broker returns the list to the client, M re-sorts it in alphabetical order as shown in <u>Figure 38</u>:

<span id="_Ref446322631" class="anchor"></span>Figure 37: Results Property—Sample Array List Sequence Sorted Alphabetically

LIST(1)=“Second”

LIST(2)=“Fourth”

LIST(“AAA”)=“Third”

LIST(“CCC”)=“First”

On the client, the Results property content is shown in <u>Figure 39</u>:

<span id="_Ref446322690" class="anchor"></span>Figure 38: Results Property—Example

brkrRPCBroker1.Results\[0\]=Second

brkrRPCBroker1.Results\[1\]=Fourth

brkrRPCBroker1.Results\[2\]=Third

brkrRPCBroker1.Results\[3\]=First

#### Example

The program code in <u>Figure 40</u> demonstrates using the <u>Results Property</u>:

<span id="_Ref446322771" class="anchor"></span>Figure 39: Results Property—Sample Code Using the Results Property

procedure TForm1.btnSendClick(Sender: TObject);

begin

*{clears Results between calls}*

brkrRPCBroker1.ClearResults := True;

*{the following code returns a single value}*

brkrRPCBroker1.RemoteProcedure := ‘SEND BACK SOME SINGLE VALUE’;

brkrRPCBroker1.Call;

Label1.Caption := ‘Value returned is: ’ + brkrRPCBroker1.Results\[0\];

*{the following code returns several values}*

brkrRPCBroker1.RemoteProcedure := ‘SEND BACK LIST OF VALUES’;

brkrRPCBroker1.Call;

ListBox1.Items := RPCBroker.Results;

end;

### RPCBError Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property RPCBError: String;

#### Description

The RPCBError property (RunTime) is a read-only property that contains the Message property associated with the exception or error that was encountered by the instance of the <u>TRPCBroker Component</u>.

### RPCTimeLimit Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property RPCTimeLimit: Integer;

#### Description

The RPCTimeLimit property (RunTime) is a public integer property. It specifies the length of time a client waits for a response from an RPC. The default and minimum value of this property is 30 seconds. If an RPC is expected to take more than 30 seconds to complete, adjust the RPCTimeLimit property accordingly. However, it is *not* advisable to have an RPCTimeLimit that is too long; otherwise, the client-end of the application appears to “hang”, if the VistA M Server does *not* respond in a timely fashion.

#### Example

The program code in <u>Figure 41</u> demonstrates using the <u>RPCTimeLimit Property</u>:

<span id="_Ref446322803" class="anchor"></span>Figure 40: RPCTimeLimit Property—Example

procedure TForm1.Button1Click(Sender: TObject);

var

intSaveRPCTimeLimit: integer;

begin

brkrRPCBroker1.RemoteProcedure := ‘GET ALL LAB RESULTS’;

brkrRPCBroker1.Param\[0\].Value := ‘DFN’;

brkrRPCBroker1.Param\[0\].PType := reference;

*{save off current time limit}*

intSaveRPCTimeLimit := brkrRPCBroker1.RPCTimeLimit;

*{can take up to a minute to complete}*

brkrRPCBroker1.RPCTimeLimit := 60;

brkrRPCBroker1.Call;

*{restore previous time limit}*

brkrRPCBroker1.RPCTimeLimit := intSaveRPCTimeLimit;

end;

### RPCVersion Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property RPCVersion: String;

#### Description

The RPCVersion property (DesignTime) is a published string type property used to pass the version of the RPC. This can be useful for backward compatibility.

As you introduce new functionality into an existing RPC, your RPC can branch into different parts of the code based on the value of the RPCVersion property. The Broker sets the XWBAPVER variable on the VistA M Server to the contents of the RPCVersion property. This property *cannot* be empty and defaults to “0” (zero).

You can use the application version number in the RPCVersion property.

![](xwb-1-1-73-developer-s-guide/242.png) REF: For a suggested method for constructing version numbers, see the “<u>Application Considerations</u>” section.

#### Example

In the following examples (<u>Figure 42</u> and <u>Figure 43</u>), an RPC is first called with two parameters that are added together and the sum returned to the client. Again, this same RPC is called with the same parameters; however, this time it uses a different RPC version value. Thus, the two numbers are simply concatenated together, and the resulting string is returned:

#### On the Client

<span id="_Ref446322871" class="anchor"></span>Figure 41: RPCVersion Property—Example on the Client

procedure TForm1.Button1Click(Sender: TObject);

begin

*{make sure the results get cleared}*

brkrRPCBroker1.ClearResults := True;

*{just re-use the same parameters}*

brkrRPCBroker1.ClearParameters := False;

brkrRPCBroker1.RemoteProcedure := ‘MY APPLICATION REMOTE PROCEDURE’;

brkrRPCBroker1.Param\[0\].Value := ‘333’;

brkrRPCBroker1.Param\[0\].PType := literal;

brkrRPCBroker1.Param\[1\].Value := ‘444’;

brkrRPCBroker1.Param\[1\].PType := literal;

brkrRPCBroker1.Call;

*{the result is 777}*

Label1.Caption := ‘Result of the call: ’ + brkrRPCBroker1.Results\[0\];

brkrRPCBroker1.RPCVersion := ‘2’;

brkrRPCBroker1.Call;

*{the result is 333444}*

Label2.Caption := ‘Result of the call: ’ + brkrRPCBroker1.Results\[0\];

end;

#### On the Server

<span id="_Ref446322881" class="anchor"></span>Figure 42: RPCVersion Property—Example on the Server

TAG(RESULT,PARAM1,PARAM2) ;*Code for MY APPLICATION REMOTE PROCEDURE*

IF XWBAPVER\<2 SET RESULT=PARAM1+PARAM2

ELSE SET RESULT=PARAM1_PARAM2

QUIT RESULT

### SecurityPhrase Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SecurityPhrase: String;

#### Description

The SecurityPhrase property (RunTime) holds the unique security phrase for the application to be used with Broker Security Enhancement (BSE) logon. The security phrase identifies the application as an authorized user of BSE visitor access on the VistA M Server.

![](xwb-1-1-73-developer-s-guide/243.png) RECOMMENDATION: Since the Security Phrase is the applications identifier, a good security practice is to identify the Security Phrase as a const value in an include file when compiling any RPC Broker Delphi-based program implementing BSE. Add a substitute include file containing a generic Security Phrase (*not* the one used to compile the application) with the release of the source code.

![](xwb-1-1-73-developer-s-guide/244.png) REF: For more information on the application Security Phrase, see the “<u>Step-By-Step Procedures to Implement BSE</u>” section.

### Server Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property Server: String;

#### Description

The Server property (DesignTime) contains the name or [Internet Protocol (IP) address](#IP_Address) of the VistA M Server system. If the name is used instead of the [IP address](#IP_Address), Microsoft<sup>®</sup> Windows Winsock should be able to resolve it. Winsock can resolve a name to an [IP address](#IP_Address) either through the Domain Name Service ([DNS](#DNS)) or by looking it up in the [HOSTS](#HOSTS_File) file on the client workstation. In the case where the same name exists in the [DNS](#DNS) and in the HOSTS file, the HOSTS file entry takes precedence. Changing the name of the VistA M Server while the <u>TRPCBroker Component</u> is connected disconnects the <u>TRPCBroker Component</u> from the previous server.

![](xwb-1-1-73-developer-s-guide/245.png) REF: For common Winsock error messages, see the RPC Broker “FAQ: Common Winsock Error/Status Messages” at the RPC Broker VA Intranet website.

#### Example

The program code in <u>Figure 44</u> demonstrates using the <u>Server Property</u>:

<span id="_Ref446332444" class="anchor"></span>Figure 43: Server Property—Example

procedure TForm1.btnConnectClick(Sender: TObject);

begin

brkrRPCBroker1.ListenerPort := \<REDACTED\>;

brkrRPCBroker1.Server := ‘DHCPSERVER’;

brkrRPCBroker1.Connected := True;

end;

### ServiceSection Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property ServiceSection: String;

#### Description

The ServiceSection property (RunTime) holds the user’s service section from the NEW PERSON (#200) file.

### ShowCertDialog Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property ShowCertDialog

#### Description

The ShowCertDialog property was added to the TRPCBroker component with RPC Broker Patch XWB\*1.1\*73. It is of type Boolean and defaults to False. If set to True, either at design time or at run time, the user will be prompted to select a certificate rather than one being auto-selected. This was requested considering the auto-selection process; many applications have various components that require different user attributes to successfully test. The ShowCertDialog property affords the software developer with the ability to show the selection dialog to the user who can cancel it and be presented with the Access/Verify code dialog.

### ShowErrorMsgs Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property ShowErrorMsgs: TShowErrorMsgs;

#### Description

The ShowErrorMsgs property (DesignTime) gives the developer the ability to determine how an exception is handled, if an error handler has *not* been provided through the OnRpcbError property (i.e., a procedure property that is set to the name of a procedure that is called if an error is encountered). If the OnRpcbError property is assigned, then exception processing is delegated to that procedure; otherwise, exception handling is based on the value of ShowErrorMsgs property.

<u>Table 12</u> lists the possible values:

| Value                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| semRaise (default) | This is the default value. The Broker does *not* handle the error directly but passes it off to the application in general to process, which can result in a different message box display or some other type of error indication.                                                                                                                                                                         |
| semQuiet           | The error is *not* displayed or raised. This requires the application to check the value of the <u>RPCBError Property (read-only)</u> following calls to the Broker to determine whether an error has occurred, and if so, what the error was. This can be desirable, if the application requires that errors *not* result in display boxes, etc., as might be the case with an NT service or Web application. |

<span id="_Ref446337160" class="anchor"></span>Table 13: RPC Settings to Determine How Data is Returned

### Socket Property (read-only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property Socket: Integer;

#### Description

The Socket property (RunTime) contains the active port being used for the TCP/IP connection to the VistA M Server. This is the port that is currently in use on the server as opposed to the ListenerPort (see <u>ListenerPort Property</u>) that was used to make the initial connection. After the initial connection, the server connection is moved to another port number (i.e., Socket), which is used for the remainder of the session.

#### Example

The program code in <u>Figure 45</u> populates the <u>Socket Property (read-only)</u> with the active port on the VistA M Server:

<span id="_Ref446332733" class="anchor"></span>Figure 44: Socket Property—Example

function ExistingSocket(Broker: TRPCBroker): integer;

var

Index: integer;

begin

Result := 0;

if Assigned(BrokerConnections) and

BrokerConnections.Find(Broker.Server + ‘:’ + IntToStr(Broker.ListenerPort), Index) then

Result := TRPCBroker(BrokerConnections.Objects\[Index\]).Socket;

end;

### Sorted Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TMult Class</u>

#### Declaration

property Sorted: Boolean;

#### Description

The Sorted property (DesignTime) value determines the order of the items in a TMult variable. If Sorted is:

- True—Items are sorted in ascending order of their string subscripts.
- False (default)—Items are unsorted, and appear in the order they were added.

Keep in mind that changing Sorted from False to True irreversibly sorts the list so that changing Sorted back to False does *not* put the list back in its original order, unless the original order was already sorted of course.

#### Example

The program code in <u>Figure 46</u> demonstrates the effect the <u>Sorted Property</u> has on a TMult variable. Notice that by setting the <u>Sorted Property</u> back to False, the list does *not* revert to its unsorted order:

1.  Start a new VCL Forms application.
29. Drop one TMemo and one TButton on the form. Arrange controls as in <u>Figure 47</u>.
30. Add Vcl.StdCtrls and TRPCB to the “uses” clause.
31. Copy the code in <u>Figure 46</u> to the Button1.OnClick event:

<span id="_Ref446332772" class="anchor"></span>Figure 45: Sorted Property—Code Added to the Button1.OnClick Event

procedure TForm1.Button1Click(Sender: TObject);

var

Mult1: TMult;

Subscript: string;

begin

*//Create Mult1. Make Form1 its owner*

Mult1 := TMult.Create(Form1);

/*/Fill Mult1 with some strings*

Mult1\[‘First’\] := ‘One’;

Mult1\[‘Second’\] := ‘Two’;

Mult1\[‘Third’\] := ‘Three’;

Mult1\[‘Fourth’\] := ‘Four’;

Mult1\[‘Fifth’\] := ‘Five’;

*//configure memo box for better display*

Memo1.Font.Name := ‘Courier’;

Memo1.ScrollBars := ssVertical;

Memo1.Lines.Clear;

Memo1.Lines.Add(‘Natural order:’);

*//set a starting point*

Subscript := ‘’;

repeat

*//get next Mult element*

Subscript := Mult1.Order(Subscript, 1);

*//if not the end of list*if Subscript \<\> ‘’ then

*//display subscript value*

Memo1.Lines.Add(Format(‘%10s’, \[Subscript\]) + ‘ - ’ + Mult1\[Subscript\])

*//stop when reached the end*until Subscript = ‘’;

*//list is now sorted alphabetically*

Mult1.Sorted := True;

Memo1.Lines.Add(‘’);

Memo1.Lines.Add(‘Sorted order:’);

*//set a starting point*

Subscript := ‘’;

repeat

*//get next Mult elemen*t

Subscript := Mult1.Order(Subscript, 1);

*//if not the end of list*if Subscript \<\> ‘’ then

*//display subscript value*

Memo1.Lines.Add(Format(‘%10s’, \[Subscript\]) + ‘ = ’ + Mult1\[Subscript\])

*//stop when reached the end*until Subscript = ‘’;

*//existing entries remain in sorted order*

Mult1.Sorted := False;

Memo1.Lines.Add(‘’);

Memo1.Lines.Add(‘Unsorted order:’);

*//set a starting point*

Subscript := ‘’;

repeat

*//get next Mult element*

Subscript := Mult1.Order(Subscript, 1);

*//if not the end of list*if Subscript \<\> ‘’ then

*//display subscript value*

Memo1.Lines.Add(Format(‘%10s’, \[Subscript\]) + ‘ - ’ + Mult1\[Subscript\])

*//stop when reached the end*until Subscript = ‘’‘;

end;

32. Run project and select the button.

The expected output is shown in <u>Figure 47</u>:

> <span id="_Ref445382014" class="anchor"></span>Figure 46: Sorted Property—Sample Form Output

> ![](xwb-1-1-73-developer-s-guide/246.png)

You may have to scroll up and down to see all of the output.

### SSHHide Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSHHide: Boolean;

#### Description

The SSHhide property is used when making secured (Secure Shell \[SSH\]) broker connections. It determines whether the SSH Tunnel application control box is hidden (“true”) or minimized (“false”, default) at application run-time.

### SSHport Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSHport: String;

#### Description

The SSHport property (RunTime) holds a specific port number for SSH Tunneling if the <u>UseSecureConnection Property</u> is set to “SSH” or “PLINK” (either as a command line option or within the application). If *not* specified, the application uses the RPC Broker listener port for the remote server. This is useful if the server is running separate listeners for SSH and *non*-secured connections.

To set the SSHport property as a command line option, include the following:

SSHPort=portnumber

### SSHpw Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSHpw: String;

#### Description

The SSHpw property (RunTime) holds a password for SSH Tunneling if the <u>UseSecureConnection Property</u> is set to “PLINK” (either as a command line option or within the application). If *not* specified, the password is set to NULL.

To set the SSHpw property as a command line option, include the following:

SSHpw=password

### SSHUser Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSHUser: String;

#### Description

The SSHUser property (RunTime) holds a specific username for SSH Tunneling if the <u>UseSecureConnection Property</u> is set to “SSH” (either as a command line option or within the application). For VA VistA servers, the username is typically of the form *xxx*vista, where the *xxx* is the station’s three letter abbreviation.

To set the SSHUser property as a command line option, include the following:

SSHUser=username

### SSOiADUPN Property (TRPCBroker Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSOiADUPN: String;

#### Description

The SSOiADUPN property (RunTime) holds the authenticated user’s Active Directory (AD) User Principal Name (UPN) for the current connection. The value is obtained from the <u>SSOiADUPN Property (TXWBSSOiToken Component)</u>.

### SSOiADUPN Property (TXWBSSOiToken Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TXWBSSOiToken Component</u>

#### Declaration

property SSOiADUPN: String;

#### Description

The SSOiADUPN property (RunTime) holds the authenticated user’s Active Directory (AD) User Principal Name (UPN) for the current token. The value is extracted from the <u>SSOiToken Property (TXWBSSOiToken Component)</u>.

### SSOiLogonName Property (TRPCBroker Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSOiLogonName: String;

#### Description

The SSOiLogonName property (RunTime) holds the authenticated user’s Active Directory (AD) user name for the current connection. The value is obtained from the <u>SSOiLogonName Property (TXWBSSOiToken Component)</u>.

### SSOiLogonName Property (TXWBSSOiToken Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TXWBSSOiToken Component</u>

#### Declaration

property SSOiLogonName: String;

#### Description

The SSOiLogonName property (RunTime) holds the authenticated user’s Active Directory (AD) user name for the current token. The value is extracted from the <u>SSOiToken Property (TXWBSSOiToken Component)</u>.

### SSOiSECID (TRPCBroker Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSOiSECID: String;

#### Description

The SSOiSECID property (RunTime) holds the authenticated user’s Identity and Access Management Security ID (SecID) for the current connection. The value is obtained from the <u>SSOiSECID Property (TXWBSSOiToken Component)</u>.

### SSOiSECID Property (TXWBSSOiToken Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TXWBSSOiToken Component</u>

#### Declaration

property SSOiSECID: String;

#### Description

The SSOiSECID property (RunTime) holds the authenticated user’s Identity and Access Management Security ID (SecID) for the current token. The value is extracted from the TXWBSSOiToken component SSOiToken property.

### SSOiToken Property (TRPCBroker Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property SSOiToken: String;

#### Description

The SSOiToken property (RunTime) holds a digitally-signed XML document (stored as a string) containing user attributes needed to authenticate a user into VistA. The value is obtained from the <u>SSOiToken Property (TXWBSSOiToken Component)</u>.

### SSOiToken Property (TXWBSSOiToken Component)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TXWBSSOiToken Component</u>

#### Declaration

property SSOiToken: String;

#### Description

The SSOiToken property (RunTime) holds a digitally-signed XML document (stored as a string) containing user attributes needed to authenticate a user into VistA for the current connection. The value is obtained by authenticating the user into the Identity and Access Management (IAM) Secure Token Service (STS) server using mutual Transport Layer Security (TLS) 2-factor authentication.

### StandardName Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property StandardName: String;

#### Description

The StandardName property (RunTime) holds the user’s standard name from the NEW PERSON (#200) file.

### Title Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property Title: String;

#### Description

The Title property (RunTime) holds the user’s title from the NEW PERSON (#200) file.

### URLDetect Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TXWBRichEdit Component</u>

#### Declaration

property URLDetect: Boolean;

#### Description

The URLDetect property (DesignTime) is used to create active (“live”) links in an application. If this property is set to:

- True—URLs (http:, mailto:, file:, etc.) are shown in blue and underlined. If the user clicks on the URL, it opens the URL in the appropriate application.
- False (the default)—URLs appear as normal text and are *not* active.

### User Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property User: TVistaUser;

#### Description

The User property (RunTime) instance of the <u>TVistaUser Class</u> object is created during the Create process for the TRPCBroker instance. The object contains data on the current user and is updated as a part of the user authentication process.

![](xwb-1-1-73-developer-s-guide/247.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

### UseSecureConnection Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TRPCBroker Component</u>

#### Declaration

property UseSecureConnection: Constant;

#### Description

The UseSecureConnection property is used to specify whether SSH Tunneling is to be used when making the connection. It can be specified within an application or at run-time as a command line option.

To set the UseSecureConnection property within an application, use one of the following command lines:

- secureNone:

UseSecureConnection := 0; *//Do not use SSH tunneling (default)*

- secureAttachmate:

UseSecureConnection := 1; *//Use Attachmate/Micro Focus Reflection SSH*

- securePlink:

UseSecureConnection := 2; *//Use PuTTY Link (Plink) SSH*

To set the UseSecureConnection property as a command line option, include either of the following:

- “SSH”—Attachmate<sup>®</sup>/Micro Focus<sup>®</sup> Reflection.
- “PLINK”—PuTTY Link (Plink).

### Value Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TParamRecord Class</u>

#### Declaration

property Value: String;

#### Description

The Value property (DesignTime) is used to pass either a single string or a single variable reference to the VistA M Server, depending on the PType (see <u>Table 11</u>).

#### Example

The program code in <u>Figure 48</u> demonstrates a couple of different uses of the <u>Value Property</u>. Remember that each Param\[x\] element is really a <u>TParamRecord Class</u>.

<span id="_Ref446332843" class="anchor"></span>Figure 47: Value Property—Example

procedure TForm1.Button1Click(Sender: TObject);

beginwith brkrRPCBroker1 do begin

RemoteProcedure := ‘SET NICK NAME’;

*{A variable reference}*

Param\[0\].Value := ‘DUZ’;

Param\[0\].Ptype := reference;

*{A string}*

Param\[1\].Value := edtNickName.Text;

Param\[1\].Ptype := literal;

Call;

end;

end;

### VerifyCode Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaLogin Class</u>

#### Declaration

property VerifyCode: String;

#### Description

The VerifyCode property (RunTime) holds the Verify code for lmAVCodes mode of <u>Silent Login</u>. Like the <u>AccessCode Property</u>, the user’s Verify code is also encrypted before it is transmitted to the VistA M Server.

![](xwb-1-1-73-developer-s-guide/248.png) REF: For examples of silent logon by passing Access and Verify codes, see the “<u>Silent Login Examples</u>” section.

![](xwb-1-1-73-developer-s-guide/249.png) REF: For more information on Verify codes, see the “Part 1: Sign-On/Security” section in the *Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide*.

### VerifyCodeChngd Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property VerifyCodeChngd: Boolean;

#### Description

The VerifyCodeChngd property (RunTime) indicates whether or not the user’s Verify code has changed.

### Vpid Property

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Applies to

<u>TVistaUser Class</u>

#### Declaration

property Vpid: String;

#### Description

The Vpid property (RunTime) returns the Department of Veterans Affairs Person Identifier (VPID) value for the current user from the NEW PERSON (#200) file, if the facility has already been enumerated. If the facility has *not* been enumerated, the value returned is a NULL string.

# Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## RPC Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Remote Procedure Call (RPC) is a defined call to M code that runs on a VistA M Server. A client application, through the RPC Broker, can make a call to the VistA M Server and execute an RPC on the server. This is the mechanism through which a client application can:

- Send data to a VistA M Server.
- Execute code on a VistA M Server.
- Retrieve data from a VistA M Server.

An RPC can take optional parameters to do some task and then return either a single value or an array to the client application. RPCs are stored in the <u>REMOTE PROCEDURE (#8994) File</u>.

The following topics are covered:

- <u>What Makes a Good RPC?</u>
- <u>Using an Existing M API</u>
- <u>Creating RPCs</u>
- <u>M Entry Point for an RPC:</u>
- <u>Relationship between an M Entry Point and an RPC</u>
- <u>First Input Parameter (Required)</u>
- <u>Return Value Types</u>
- <u>Input Parameters (Optional)</u>
- <u>Examples</u>
- <u>RPC Entry in the Remote Procedure File:</u>
- <u>REMOTE PROCEDURE (</u>\#8994) File
- <u>Key Fields for RPC Operation</u>
- <u>RPC Version</u>
- <u>Blocking an RPC</u>
- <u>Cleanup after RPC Execution</u>
- <u>Documenting RPCs</u>
- <u>Executing RPCs from Clients:</u>
- <u>How to Execute an RPC from a Client</u>
- <u>RPC Security: How to Register an RPC</u>
- <u>RPC Limits</u>
- <u>RPC Time Limits</u>
- <u>Maximum Size of Data</u>
- <u>Maximum Number of Parameters</u>
- <u>Maximum Size of Array</u>
- <u>RPC Broker Example (32-Bit)</u>

## What Makes a Good RPC?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following characteristics help to make a good remote procedure call (RPC):

- Silent calls (no I/O to terminal or screen, no user intervention required).
- Minimal resources required (passes data in brief, controlled increments).
- Discrete calls (requiring as little information as possible from the process environment).
- Generic as possible (different parts of the same package as well as other packages could use the same RPC).

## Using an Existing M API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In some cases, an existing M API provides a useful M entry point for an RPC. As with any M entry point, you need to add the RPC entry that invokes the M entry point, in the <u>REMOTE PROCEDURE (#8994) File</u>.

![](xwb-1-1-73-developer-s-guide/250.png) REF: See also: “<u>Relationship between an M Entry Point and an RPC</u>” section.

## Creating RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create your own custom RPCs to perform actions on the VistA M Server and to retrieve data from the VistA M Server. Then you can call these RPCs from your client application. Creating an RPC requires you to perform the following:

- Write and test the M entry point that is called by the RPC.
- Add the RPC entry that invokes the M entry point, in the <u>REMOTE PROCEDURE (#8994) File</u>.

## M Entry Point for an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Relationship between an M Entry Point and an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An RPC can be thought of as a wrapper placed around an M entry point for use with client applications. Each RPC invokes a single M entry point.

An M entry point has defined input and output values/parameters that are passed via the standard M invoking methods. An RPC, however, needs to do the following:

- Accept input from the Broker (i.e., passing data/parameters from the client application).
- Pass data to the M entry point in a specified manner.
- Receive values back from the M code in a pre-determined format.
- Pass M code output back through the Broker to the client application.

You can use the <u>\$\$BROKER^XWBLIB</u> function in M code to determine whether the code is being run in an environment where it was invoked by the Broker. This can help you use M code simultaneously for Broker and *non*-Broker applications.

You can use the <u>RPCVersion Property</u> to support multiple versions of an RPC. The <u>RPCVersion Property</u> <u>Example</u> shows you how to do this on the client and server sides.

### First Input Parameter (Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker always passes a variable by reference in the first input parameter to your M routine. It expects results (one of five <u>Return Value Types</u>) to be returned in this parameter. You *must* always set some return value into that first parameter before your routine returns.

### Return Value Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are five RETURN VALUE TYPEs for RPCs as shown in <u>Table 13</u>. You should choose a return value type that is appropriate to the type of data your RPC needs to return. For example, to return the DUZ, a return value type of SINGLE VALUE would be appropriate.

The RETURN VALUE TYPE you choose determines what values you should set into the return value parameter of your M entry point.

You should always set *some* value into the Return Value parameter of the M entry point, even if your RPC encounters an error condition.

The RPC settings in <u>Table 13</u>, combined with your M entry point, determine how data is returned to your client application:

<table>
<caption><p><span id="_Ref446337161" class="anchor"></span>Table 14: Param PType Value Types</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 47%" />
<col style="width: 14%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC Return Value Type</th>
<th>How M Entry Point Should Set the Return Parameter</th>
<th>RPC Word Wrap On Setting</th>
<th>Values returned in Client Results</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Single Value</strong></td>
<td><p>Set the return parameter to a single value. For example:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT=“XWBUSER,ONE”</p>
<p>Q</p></td>
<td>No effect</td>
<td>Value of parameter, in Results[0].</td>
</tr>
<tr class="even">
<td><strong>Array</strong></td>
<td><p>Set an array of strings into the return parameter, each subscripted one level descendant. For example:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT(1)=“ONE”</p>
<p>S RESULT(2)=“TWO”</p>
<p>Q</p>
<p>If your array is large, consider using the GLOBAL ARRAY return value type, to avoid memory allocation errors.</p></td>
<td>No effect</td>
<td>Array values, each in a Results item.</td>
</tr>
<tr class="odd">
<td><strong>Word Processing</strong></td>
<td>Set the return parameter the same as you set it for the ARRAY type. The only difference is that the WORD WRAP ON setting affects the WORD PROCESSING return value type.</td>
<td>True<br />
<br />
<br />
False</td>
<td>Array values, each in a Results item.<br />
<br />
Array values, all concatenated into Results[0].</td>
</tr>
<tr class="even">
<td><strong>Global Array</strong></td>
<td><p>Set the return parameter to a closed global reference in <strong>^TMP</strong>. The global’s data nodes are traversed using <strong>$QUERY</strong>, and all data values on global nodes descendant from the global reference are returned.</p>
<p>This type is especially useful for returning data from VA FileMan WORD PROCESSING type fields, where each line is on a <strong>0</strong>-subscripted node.</p>
<p>![](xwb-1-1-73-developer-s-guide/251.png) CAUTION: The global reference you pass is killed by the Broker at the end of RPC Execution as part of <a href="#rpcs_rpc_cleanup_htm">RPC cleanup</a>. Do <em>not</em> pass a global reference that is <em>not</em> in ^TMP or that should <em>not</em> be killed.</p>
<p>This type is useful for returning large amounts of data to the client, where using the ARRAY type can exceed the symbol table limit and crash your RPC.</p>
<p>For example, to return signon introductory text you could do:</p>
<p>TAG(RESULT);</p>
<p>M ^TMP(“A6A”,$J)=</p>
<p>^XTV(8989.3,1,”INTRO”)</p>
<p>;this node not needed</p>
<p>K ^TMP(“A6A”,$J,0)</p>
<p>S RESULT=$NA(^TMP(“A6A”,$J))</p>
<p>Q</p></td>
<td>True<br />
<br />
<br />
False</td>
<td>Array values, each in a Results item.<br />
<br />
Array values, all concatenated into <a href="#components_results_property_htm">Results</a>[0].</td>
</tr>
<tr class="odd">
<td><strong>Global Instance</strong></td>
<td><p>Set the return parameter to a closed global reference.</p>
<p>For example, the following code returns the whole <strong>0th</strong> node from the NEW PERSON (#200) file for the current user:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT=$NA(^VA(200,DUZ,0))</p>
<p>Q</p></td>
<td>No effect</td>
<td>Value of global node, in Results[0].</td>
</tr>
</tbody>
</table>

<span id="_Ref446337161" class="anchor"></span>Table 14: Param PType Value Types

![](xwb-1-1-73-developer-s-guide/252.png) NOTE: In the M code called by an RPC, you can use the <u>\$\$RTRNFMT^XWBLIB</u> function to change the RETURN VALUE TYPE of an RPC on-the-fly.

### Input Parameters (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M entry point for an RPC can optionally have input parameters (i.e., beyond the first parameter, which is always used to return an output value). The client passes data to your M entry point through these parameters.

The client can send data to an RPC (and therefore the entry point) in one of the three <u>Param Property</u> types in <u>Table 14</u>:

<table>
<caption><p><span id="_Toc82593680" class="anchor"></span>Table 15: Remote Procedure File Information</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Param PType</th>
<th>Param Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>literal</strong></td>
<td>Delphi string value; passed as a string literal to the VistA M Server.</td>
</tr>
<tr class="even">
<td><strong>reference</strong></td>
<td><p>Delphi string value; treated on the VistA M Server as an M variable name and resolved from the symbol table at the time the RPC executes.</p>
<p>![](xwb-1-1-73-developer-s-guide/253.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.</p></td>
</tr>
<tr class="odd">
<td><strong>list</strong></td>
<td>A single-dimensional array of strings in the <u>Mult Property</u> of the <u>Param Property</u>; passed to the VistA M Server where it is placed in an array. String subscripting can be used.</td>
</tr>
</tbody>
</table>

<span id="_Toc82593680" class="anchor"></span>Table 15: Remote Procedure File Information

The type of the input parameters passed in the <u>Param Property</u> of the <u>TRPCBroker Component</u> determines the format of the data you *must* be prepared to receive in your M entry point.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The examples in <u>Figure 49</u> and <u>Figure 50</u> illustrate sample M code that could be used in simple RPCs:

1.  The example in <u>Figure 49</u> takes two numbers and returns their sum:

> <span id="_Ref446332879" class="anchor"></span>Figure 48: RPCs—Sample M Code to Add Two Numbers

SUM(RESULT,A,B) ;*add two numbers*

S RESULT=A+B

Q

33. The example in <u>Figure 50</u> receives an array of numbers and returns them as a sorted array to the client:

> <span id="_Ref446332906" class="anchor"></span>Figure 49: RPCs—Sample M Code that Receives an Array of Numbers and Returns them as a Sorted Array to the Client

SORT(RESULT,UNSORTED)  ;*sort numbers*

N I

S I=“”

F  S I=\$O(UNSORTED(I)) Q:I=”“  S RESULT(UNSORTED(I))=UNSORTED(I)

Q

## RPC Entry in the Remote Procedure File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### REMOTE PROCEDURE (#8994) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker consists of a single global that stores the REMOTE PROCEDURE (#8994) file:

| File \# | File Name        | Global Location |
|---------|------------------|-----------------|
| 8994    | REMOTE PROCEDURE | ^XWB(8994,      |

<span id="_Ref446337236" class="anchor"></span>Table 16: Remote Procedure File—Key Fields for RPC Operation

This is the common file used by all applications to store *all* remote procedure calls accessed via the Broker. All RPCs used by any site-specific client/server application software using the RPC Broker interface *must* be registered and stored in this file.

This file is used as a repository of server-based procedures in the context of the Client/Server architecture. By using the Remote Procedure Call (RPC) Broker, applications running on client workstations can invoke (call) the procedures in this file to be executed by the server and the results are returned to the client application.

![](xwb-1-1-73-developer-s-guide/254.png) NOTE: The RPC (#19.05) subfield of the OPTION (#19) file points to RPC (#.01) field of the <u>REMOTE PROCEDURE (#8994) File</u>.

### Key Fields for RPC Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the M code is complete, you need to add the RPC to the <u>REMOTE PROCEDURE (#8994) File</u>. <u>Table 16</u> lists the fields in the REMOTE PROCEDURE (#8994) file that are key to the correct operation of an RPC:

<table>
<caption><blockquote>
<p><span id="_Ref446337278" class="anchor"></span>Table 17: RPC Multiple Fields for “B”-Type Options</p>
</blockquote></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Required?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td>Yes</td>
<td>The name that identifies the RPC (this entry should be namespaced in the package namespace).</td>
</tr>
<tr class="even">
<td>TAG (#.02)</td>
<td>Yes</td>
<td>The tag at which the remote procedure call begins.</td>
</tr>
<tr class="odd">
<td>ROUTINE (#.03)</td>
<td>Yes</td>
<td>The name of the routine that should be invoked to start the RPC.</td>
</tr>
<tr class="even">
<td>WORD WRAP ON (#.08)</td>
<td>No</td>
<td>Affects GLOBAL ARRAY and WORD PROCESSING return value types only. If set to <strong>False</strong>, all data values are returned in a single concatenated string in Results[0]. If set to <strong>True</strong>, each array node on the M side is returned as a distinct array item in Results.</td>
</tr>
<tr class="odd">
<td>RETURN VALUE TYPE (#.04)</td>
<td>Yes</td>
<td><p>This can be one of five types:</p>
<ul>
<li><p>SINGLE VALUE</p></li>
<li><p>ARRAY</p></li>
<li><p>WORD PROCESSING</p></li>
<li><p>GLOBAL ARRAY</p></li>
<li><p>GLOBAL INSTANCE</p></li>
</ul>
<p>This setting controls how the Broker processes an RPC’s return parameter (see “<u>Return Value Types</u>“).</p></td>
</tr>
</tbody>
</table>

<span id="_Ref446337278" class="anchor"></span>Table 17: RPC Multiple Fields for “B”-Type Options

### RPC Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VERSION field of the <u>REMOTE PROCEDURE (#8994) File</u> indicates the version number of an RPC installed at a site. The field can be set either by an application developer and exported by KIDS or by a site manager using VA FileMan.

Applications can use <u>XWB IS RPC AVAILABLE</u> or <u>XWB ARE RPCS AVAILABLE</u> to check the availability of a version of an RPC on a server. This is especially useful for RPCs run remotely, as the remote server may not have the latest RPC installed.

### Blocking an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INACTIVE field of the <u>REMOTE PROCEDURE (#8994) File</u> allows blocking of RPCs. The blocking can apply to local access (users directly logged into the site) or remote access (users logged on to a different site) or both. The field can be set either by an application developer and exported by Kernel Installation & Distribution System (KIDS) or by a site manager using VA FileMan.

![](xwb-1-1-73-developer-s-guide/255.png) REF: For more information on remote access, see the “<u>Running RPCs on a Remote Server</u>” section.

#### Value in INACTIVE field

- 1 = Completely unusable
- 2 = Unusable locally
- 3 = Unusable remotely

### Cleanup after RPC Execution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Broker uses XUTL^XUSCLEAN to clean up globals upon application termination.

In addition, there is an RPC RETURN VALUE TYPE (see “<u>Return Value Types</u>“), GLOBAL ARRAY, where the application RPC returns a closed form global reference, for example:

^TMP(“EKG”,666333551)

The Broker kills the data for the global reference for this type of RPC at the end of RPC execution.

### Documenting RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each individual application development team is responsible for identifying and providing documentation for all object components, classes, and remote procedure calls they create. Other developers using these components need to know what RPCs are called, because they need to register them with their applications.

RPCs should be documented in the DESCRIPTION (#1) field in the <u>REMOTE PROCEDURE (#8994) File</u> for those RPCs installed on your system. This gives you the capability of generating a catalogue of RPCs from the REMOTE PROCEDURE (#8994) file.

#### Delphi Component Library and Sample RPCs

In the future, an Enterprise library of services, object components, classes, Application Programming Interfaces (APIs), Remote Procedure Calls (RPCs), etc. that are in use and available to the development community at large may be available. The essential benefit of this type of library is the promotion of object re-use; thereby, enhancing development productivity, application consistency, and quality assurance. Therefore, it could contain a wide variety of services, object components, APIs, classes, RPCs, etc. from many VistA software applications.

The immediate intent is to classify and catalogue all of the object classes in use (including the standard Delphi classes), and to make the catalogue available to all interested parties.

## Executing RPCs from Clients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How to Execute an RPC from a Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If your RPC has any input parameters beyond the mandatory <u>First Input Parameter (Required)</u>, set a Param node in the <u>TRPCBroker Component</u>’s <u>Param Property</u> for each. For each input parameter, set the following sub-properties:
- <u>Value Property</u>
- <u>PType Property</u> (literal, list, or reference)

If the parameter’s <u>PType Property</u> is list, instead of specifying a value, set a list of values in the <u>Mult Property</u>.

<u>Figure 51</u> is an example of some settings of the <u>Param Property</u>:

<span id="_Ref446332955" class="anchor"></span>Figure 50: RPCs—Param Property—Example Setting a List of Values

brkrRPCBroker1.Param\[0\].Value := ‘03/31/14’;

brkrRPCBroker1.Param\[0\].PType := literal;

brkrRPCBroker1.Param\[1\].Mult\[‘“NAME”‘\] := ‘XWBUSER, ONE’;

brkrrpcbroker1.param\[1\].mult\[‘“ssn”‘\] :=“000-45-6789” ;/pre=”“\>

brkrRPCBroker1.Param\[1\].PType := list;

2.  Set the <u>TRPCBroker Component</u>’s <u>RemoteProcedure Property</u> to the name of the RPC to execute:

> brkrRPCBroker1.RemoteProcedure:=‘A6A LIST’

34. Invoke the <u>TRPCBroker Component</u>’s [<u>Call Method</u>](#components_call_method_htm) to execute the RPC. All calls to the [<u>Call Method</u>](#components_call_method_htm) should be done within an exception handler try...except statement, so that all communication errors (which trigger the <u>EBrokerError</u> exception) can be trapped and handled. For example:

<span id="_Toc82593612" class="anchor"></span>Figure 51: Error Handling—Example of a “try...except” Statement

try

brkrRPCBroker1.Call;

except

On EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

end;

35. Any results returned by your RPC are returned in the <u>TRPCBroker Component</u>’s <u>Results Property</u>. Depending on how you set up your RPC, results are returned either in a single node of the <u>Results Property</u> (Results\[0\]), or in multiple nodes of the <u>Results Property</u>.

![](xwb-1-1-73-developer-s-guide/256.png) NOTE: You can also use the <u>lstCall Method</u> and <u>strCall Method</u> to execute an RPC. The main difference between these methods and the <u>Call Method</u> is that the <u>lstCall Method</u> and the <u>strCall Method</u> do *not* use the <u>Results Property</u>, instead returning results into a location you specify.

### RPC Security: How to Register an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security for RPCs is handled through the RPC registration process. Each client application *must* create a context for itself, which checks if the application user has access to a “B”-type option in the Kernel menu system. Only RPCs assigned to that option can be run by the client application.

To enable your application to create a context for itself:

1.  Create a “B”-type option in the OPTION (#19) file for your application.

![](xwb-1-1-73-developer-s-guide/257.png) NOTE: The OPTION TYPE “B” represents a Broker client/server type option.

36. In the RPC multiple for this option type, add an entry for each RPC that your application calls. The fields listed in <u>Table 17</u> can be set up for each RPC in your option:

| Field Name (#)  | Entry    | Description                                                                                                                                                                                      |
|-----------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPC (#.01)  | Required | This field is used to enter a pointer to the <u>REMOTE PROCEDURE (#8994) File</u>. This field links the remote procedure call in the <u>REMOTE PROCEDURE (#8994) File</u> to the package option. |
| RPCKEY (#1) | Optional | This field is used to restrict the use of a remote procedure call to a particular package option. The RPCKEY field is a free-text pointer to the SECURITY KEY (#19.1) file.                      |
| RULES (#2)  | Optional | This field is used to enter M code that is executed when an RPC request is made to verify whether the request should be honored.                                                                 |

<span id="_Toc82593683" class="anchor"></span>Table 18: \$\$RTRNFMT^XWBLIB: The type Input Parameter Values

37. When you export your package using Kernel Installation and Distribution System (KIDS), export both your RPCs and your package option. KIDS automatically associates the RPCs with the package option.
38. Your application *must* create a context for itself on the VistA M Server, which checks access to RPCs. In the initial code of your client application, make a call to the <u>CreateContext Method</u> of your <u>TRPCBroker Component</u>. Pass your application’s “B”-type option’s name as a parameter. For example:

if not brkrRPCBroker1.CreateContext(option_name) then

Application.Terminate;

39. If the <u>CreateContext Method</u> returns True, only those RPCs designated in the RPC multiple of your application option is permitted to run.
40. If the <u>CreateContext Method</u> returns False, you should terminate your application (if you do not, your application runs but you get errors every time you try to access an RPC).
41. End-users of your application *must* have the “B”-type option assigned to them on one of their menus, in order for the <u>CreateContext Method</u> to return True. This allows system managers to control access to client applications.

### RPC Limits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of various constants, maximum, and minimum parameters associated with the use of the RPC Broker:

- <u>Maximum Number of Parameters</u> that can be passed to the VistA M Server.
- <u>Maximum Size of Array</u> that can be passed to the VistA M Server.
- <u>Maximum Size of Data</u> that can be received in the VistA Graphical User Interface (GUI) application from the VistA M Server.
- <u>RPC Time Limits</u>.

### RPC Time Limits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A public READ/WRITE property (i.e., <u>RPCTimeLimit Property</u>) allows the application to change the network operation timeout prior to a call. This can be useful during times when it is known that a certain RPC, by its nature, can take a significant amount of time to execute. The value of this property is an integer that *cannot* be less than 30 seconds nor greater than 32767 seconds. Care should be taken when altering this value, since the network operation blocks the application until the operation finishes or the timeout is triggered.

There is also a server time limit for how long to stay connected when the client does *not* respond.

### Maximum Size of Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA M Server can transmit very large buffers of data back to the Microsoft<sup>®</sup> Windows client. The Windows client receives the returned data from an RPC into a 32-bit PASCAL string. RPCs can be written on the VistA M Server so that they store their results in an M GLOBAL structure, which can span RAM and disk storage media. This GLOBAL storage could be quite large depending on the assigned system quotas to the VistA M Server process. The return of the RPC can deliver this quantity to the Windows client. The actual limit depends on the capacity that the Microsoft<sup>®</sup> Windows operating system allows the client to process. Tests on a 32-megabyte RAM system have allowed buffers of several megabytes of data to be transmitted from the VistA M Server to the Microsoft<sup>®</sup> Windows client.

### Maximum Number of Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The remote procedure calls (RPCs) become M DO procedures on the VistA M Server. Since RPCs are communicated to the VistA M Server through a message mechanism, additional information is included with the message.

Parameters are processed as PASCAL short strings with a maximum of 255 characters. Each parameter is encoded with a three-character length plus a type character. Therefore, every parameter occupies length (parameter) +four. The maximum transmission at this time is 240 characters, since additional header information is present with every RPC.

A theoretical maximum, where every parameter was length 1 would give number of parameters = 240/5 or 48 parameters. A single parameter (e.g., a long string) could not exceed 240 - 4, or 236 characters. Future support will be based on the PASCAL 32-bit string, which can, theoretically, reach 2 GB. Limitations on the VistA M Server still limit this to far less, however.

### Maximum Size of Array

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although approximately only 240 characters can be sent to the VistA M Server as call parameters, a single array parameter can be passed in with greater capacity. The RPC can carry both literal and array parameters except that literal parameters are placed first and the single array last in order. Arrays are instantiated at the VistA M Server and are stored in a local array format. The maximum size is dependent on the symbol space available to the VistA M Server process. The index size and the value size are subject to limitations; the index and value each *cannot* exceed 255 - 3, or 252 characters approximately for each individual array elements.

At the time of this writing, 30 to 40 K arrays have easily been passed to the VistA M Server in a single RPC call.

### RPC Broker Example (32-Bit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker Example sample application provided with the BDK (i.e., BrokerExample.exe) demonstrates the basic features of developing RPC Broker applications, including:

- Connecting to a VistA M Server.
- Creating an application context (see <u>CreateContext Method</u>).
- Using the <u>GetServerInfo Function</u>.
- Displaying the VistA splash screen (see “<u>VistA Splash Screen Procedures</u>” section).
- Setting the TRPCBroker <u>Param Property</u> for each Param [Ptype](#ptype-property) (literal, reference, list).
- Calling RPCs with the <u>Call Method</u>.
- Calling RPCs with the <u>lstCall Method</u> and <u>strCall Method</u>.

![](xwb-1-1-73-developer-s-guide/258.png) REF: The BrokerExample.exe and client source code files for the BrokerExample.exe application are located in the following directory:

BDK32\Samples\BrokerEx

# RPC Broker: Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the RPC Broker components, the Broker Development Kit (BDK) provides other development tools, including:

- <u>Application Programming Interface (API)</u>
- <u>Functions, Methods, and Procedures</u>
- <u>Running RPCs on a Remote Server</u>
- <u>Deferred RPCs</u>

## Application Programming Interface (API)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker uses Kernel Application Programming Interfaces (APIs) and Remote Procedure Calls (RPCs) for most user authentication (Signon) and authorization (Security) actions. However, there are a few APIs and RPCs unique to Broker connections that are used by a variety of interfaces into VistA. For example, VistALink and VistA Services Assembler both use the CHKPRMIT^XWBSEC API to determine if a user has authorization to use a particular Remote Procedure.

The RPC Broker software provides the following APIs on the VistA M Server for use in RPC code:

- <u>\$\$BROKER^XWBLIB: Test for Broker Context</u>
- <u>\$\$RTRNFMT^XWBLIB(): Change RPC Return</u>
- <u>CHKPRMIT^XWBSEC(): Check Permissions</u>
- <u>CRCONTXT^XWBSEC(): Create Context</u>
- <u>SET^XWBSEC(): Set the State Variable</u>

### \$\$BROKER^XWBLIB: Test for Broker Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: RPC Broker

ICR \#: 2198

Description: Use the \$\$BROKER^XWBLIB extrinsic function in the M code called by an RPC to determine if the current process is being executed by the RPC Broker.

Format: \$\$BROKER^XWBLIB

Input Parameters: none.

Output: return value: Returns:

- 1—If the current process is being executed by the Broker.
- 0—If the current process is *not* being executed by the Broker.

#### Example

I \$\$BROKER^XWBLIB D .; broker-specific code

### \$\$RTRNFMT^XWBLIB(): Change RPC Return Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: RPC Broker

ICR \#: 2238

Description: Use the \$\$RTRNFMT^XWBLIB extrinsic function in the M code called by an RPC to change the return value type that the RPC returns on-the-fly.

Format: \$\$RTRNFMT^XWBLIB(type,wrap)

> Input Parameters: type: (required) Set this to the RETURN VALUE TYPE to which you want to change the RPC’s setting. Set it to one of the following numeric or free text values:

<table>
<caption><p><span id="_Toc82593684" class="anchor"></span>Table 19: CheckCmdLine Function—Argument</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Numeric</th>
<th><blockquote>
<p>Free Text</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>SINGLE VALUE</td>
</tr>
<tr class="even">
<td>2</td>
<td>ARRAY</td>
</tr>
<tr class="odd">
<td>3</td>
<td>WORD PROCESSING</td>
</tr>
<tr class="even">
<td>4</td>
<td>GLOBAL ARRAY</td>
</tr>
<tr class="odd">
<td>5</td>
<td>GLOBAL INSTANCE</td>
</tr>
</tbody>
</table>

<span id="_Toc82593684" class="anchor"></span>Table 19: CheckCmdLine Function—Argument

wrap: (required) Set value to:

- 1—Set RPC’s WORD WRAP ON setting to True.
- 0—Set RPC’s WORD WRAP ON setting to False.

Output: return value: Returns:

- 0—If the return value type could *not* be changed.
- numeric code—Representing the return value type to which the RPC is changed.

#### Example

I ‘\$\$RTRNFMT^XWBLIB(“ARRAY”,1) D .; branch to code if cannot change RPC type

### CHKPRMIT^XWBSEC(): Check Permissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4053

Description: The CHKPRMIT^XWBSEC API checks to see if the remote procedure is permitted to run. It checks for:

- User-held security keys
- User context (context option)
- Out-of-order settings
- RPC version

If the user is an Application Proxy, it checks to see if Application Proxy access to the remote procedure is permitted.

Some remote procedures are allowed in any context:

- XUS BSE TOKEN
- XUS CVC
- XUS GET USER INFO
- XUS GET TOKEN
- XUS IAM BIND USER
- XUS KAAJEE GET USER INFO
- XUS KAAJEE LOGOUT
- XUS KEY CHECK
- XUS SET VISITOR
- XWB CREATE CONTEXT
- XWB IM HERE
- XWB IS RPC AVAILABLE
- XWB RPC LIST

All Kernel “XUS” and RPC Broker “XWB” remote procedures are allowed in “XUS SIGNON” context.

Format: CHKPRMIT^XWBSEC(xwbrp)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
10. Set all input variables.
11. Call the API.

Input Parameters: xwbrp: (required) This is the name of the remote procedure to look up in the <u>REMOTE PROCEDURE (#8994) File</u>.

Output Variables: XWBSEC: Returns:

- “”—NULL in XWBSEC environment variable if the remote procedure is permitted to run.
- Error Message—If the remote procedure is *not* permitted. If an error is returned, then the XWBSEC environment variable is set to return the same error message.

![](xwb-1-1-73-developer-s-guide/259.png) NOTE:XWBSEC is an environment variable, so that the information is included in the error trap should a subsequent processing error occur.

### CRCONTXT^XWBSEC(): Create Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4053

Description: The CRCONTXT^XWBSEC API creates a valid RPC Broker user context.

Format: CRCONTXT^XWBSEC(result,option)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
12. Set all input variables.
13. Call the API.

Input Parameters: option: (required) This is the encrypted name of the B-type menu option to look up in the OPTION (#19) file. If the option has been assigned to the user as a SECONDARY MENU OPTION, then the context can be set.

![](xwb-1-1-73-developer-s-guide/260.png) REF: For more information on context options, see the “<u>RPC Security: How to Register an RPC</u>” section.

Output: result: Returns:

- 1—Successful: If the context is successfully created.
- 0 (and error message)—Unsuccessful: If the context could *not* be created.

Output Variables: XWBSEC: XWBSEC is an environment variable, so that the information is included in the error trap should a subsequent processing error occur. If an error is returned, then the XWBSEC environment variable is set to return the same error message.

### SET^XWBSEC(): Set the State Variable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Signon/Security

ICR \#: 4053

Description: The SET^XWBSEC API sets the XWBSTATE environment variable (array) to contain a passed in value. This is generally used to record the current status of a Broker connection for monitoring or testing.

![](xwb-1-1-73-developer-s-guide/261.png) NOTE:XWBSTATE is an environment variable, so that the information is included in the error trap should a subsequent processing error occur.

Format: SET^XWBSEC(%,value)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
14. Set all input variables.
15. Call the API.

Input Parameters: value: (required) This is FREE TEXT state value to be added to the XWBSTATE array.

Output Variables: %: Returns this variable equal to the value input parameter and also sets the XWBSTATE(%) environment variable equal to the value input parameter.

## Functions, Methods, and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional functions, methods, and procedures include:

- <u>XWB CREATE CONTEXT</u>
- <u>XWB GET BROKER INFO</u>
- <u>XWB GET VARIABLE VALUE</u>
- <u>XWB IM HERE</u>
- <u>M Emulation Functions</u>
- <u>Encryption Functions</u>
- <u>CheckCmdLine Function</u>
- <u>GetServerInfo Function</u>
- <u>GetServerIP Function</u>
- <u>ChangeVerify Function</u>
- <u>SilentChangeVerify Function</u>
- <u>StartProgSLogin Method</u>
- <u>VistA Splash Screen Procedures</u>

### XWB CREATE CONTEXT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XWB CREATE CONTEXT RPC (distributed with the RPC Broker) is used to establish the context on the VistA M Server, which is checked by the Broker Listener before executing any other remote procedure. Since context is nothing more than a client/server “B”-type option in the OPTION (#19) file, standard MenuMan security is applied in establishing a context. Therefore, a context option can be granted to users exactly the same way as regular options are done using MenuMan.

A context *cannot* be established for the following reasons:

- User has no access to that option
- Option is temporarily out of order

An application can switch from one context to another as often as it needs. Each time a context is created the previous context is overwritten.

Pass the encrypted (using the Encrypt function in the XWBHash unit) OPTION name in Param\[0\].Value, and the type (literal) in Param\[0\].PType. The TRPCBroker CreateContext method sets up these values and calls the RPC for you. Also, the current context of your user *must* give them permission to execute the XWB GET VARIABLE VALUE RPC (it *must* be included in the RPC multiple of the “B”-type option registered with the <u>CreateContext Method</u>).

![](xwb-1-1-73-developer-s-guide/262.png) NOTE:XWB CREATE CONTEXT is a Private RPC. If an application uses the TRPCBroker CreateContext method, a subscription is *not* needed as the RPC is owned by the RPC Broker package.

### XWB GET BROKER INFO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XWB GET BROKER INFO RPC (distributed with the RPC Broker) is used to return information regarding setup and parameters of the Broker Listener on the VistA M Server. The RPC currently returns only the timeout period for handler READs.

There are no input parameters.

![](xwb-1-1-73-developer-s-guide/263.png) NOTE:XWB GET BROKER INFO is currently used only within the RPC Broker package and has *not* been made available to other applications.

### XWB GET VARIABLE VALUE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the XWB GET VARIABLE VALUE RPC (distributed with the RPC Broker) to retrieve the value of any M variable in the VistA M Server environment. Pass the variable name in Param\[0\].Value, and the type (reference) in Param\[0\].PType. Also, the current context of your user *must* give them permission to execute the XWB GET VARIABLE VALUE RPC (it *must* be included in the RPC multiple of the “B”-type option registered with the <u>CreateContext Method</u>).

![](xwb-1-1-73-developer-s-guide/264.png) WARNING: The XWB GET VARIABLE VALUE RPC is intended to retrieve the value of an M variable (e.g., DUZ or DTIME). This is the only supported function of this RPC. If the RPC is used in an application in any other way than the way it was intended, results can be unpredictable, and the application could cease to function in future software patches.

![](xwb-1-1-73-developer-s-guide/265.png) NOTE:XWB GET VARIABLE VALUE is available only on a Controlled Subscription basis.

#### Example

<u>Figure 53</u> is an example of the XWB GET VARIABLE VALUE RPC:

<span id="_Ref446333001" class="anchor"></span>Figure 52: XWB GET VARIABLE VALUE RPC—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB GET VARIABLE VALUE’;

brkrRPCBroker1.Param\[0\].Value :=‘DUZ’;

brkrRPCBroker1.Param\[0\].PType := reference;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

ShowMessage(‘DUZ is ‘+brkrRPCBroker1.Results\[0\]);

### XWB IM HERE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XWB IM HERE RPC (distributed with the RPC Broker) is used to establish continued existence of the client connection to the VistA M Server (keepalive). It resets the server READ timeout. The RPC currently returns a meaningless value of “1”, which is *not* used on the client.

There are no input parameters.

![](xwb-1-1-73-developer-s-guide/266.png) NOTE:XWB IM HERE is a Private RPC. If an application uses the Delphi RPC Broker Development Kit (BDK), a subscription is *not* needed as the RPC is owned by the RPC Broker package.

### M Emulation Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Piece Function

The Piece function is a scaled down Pascal version of M’s \$PIECE function. It is declared in MFUNSTR.PAS.

function Piece(x: string; del: string; piece: integer) : string;

#### Translate Function

The Translate function is a scaled down Pascal version of M’s \$TRANSLATE function. It is declared in MFUNSTR.PAS.

function Translate(passedString, identifier, associator: string): string;

#### Examples

#### Piece Function

Piece3Str:=piece(‘123^456^789’,’^’,3);

#### Translate Function

hiStr:=translate(‘HI’,’ABCDEFGHI’,’abcdefghi’);

### Encryption Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and the RPC Broker provide encryption functions that can be used to encrypt messages sent between the client and the server.

#### In Delphi

Include XWBHash in the “uses” clause of the unit in which you are encrypting or decrypting.

Function prototypes are as follows:

function Decrypt(EncryptedText: string): string;

function Encrypt(NormalText: string): string;

#### On the VistA M Server

#### Encrypt Function

To encrypt a string, do the following:

\>S CIPHER=\$\$ENCRYP^XUSRB1(“Hello world!”) W CIPHER

/U’llTG~TVl&f-

#### Decrypt Function

To decrypt a string, do the following:

\>S PLAIN=\$\$DECRYP^XUSRB1(CIPHER) W PLAIN

Hello world!

These encryption functions can be used for any communication between the client and the server where encryption is desired.

### CheckCmdLine Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Patch XWB\*1.1\*13, the CheckCmdLine method was changed from a procedure to a function with a Boolean return value.

function CheckCmdLine(SLBroker: TRPCBroker): Boolean;

#### Argument

| Argument     | Description                                                                                                                                                    |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SLBroker | The instance of the Broker with which information on the command line should be used, and to be used for the connection, if a <u>Silent Login</u> is possible. |

<span id="_Toc82593685" class="anchor"></span>Table 20: ChangeVerify Function—Argument

#### Result

The return value indicates whether the information on the command line was sufficient to connect the RPCBroker instance to the specified Server/ListenerPort (see <u>Server Property</u> and <u>ListenerPort Property</u>).

- True—Broker is connected to the VistA M Server.
- False—Broker is *not* connected to the VistA M Server.

### GetServerInfo Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GetServerInfo function retrieves the end-user’s selection of server and port to which to connect. Use this function to set a <u>TRPCBroker Component</u>’s Server, and ListenerPort (see <u>Server Property</u> and <u>ListenerPort Property</u>) to reflect the end-user’s choice before connecting to the VistA M Server.

If there is more than one server/port from which to choose, GetServerInfo displays an application window that allows users to select a service to connect:

<span id="_Ref385263286" class="anchor"></span>Figure 53: GetServerInfo Function—Connect To Dialogue

![](xwb-1-1-73-developer-s-guide/267.png)

#### Syntax

function GetServerInfo(var Server, Port: string): integer;

![](xwb-1-1-73-developer-s-guide/268.png) NOTE: The unit is the <u>RPCConf1 Unit</u>.

The GetServerInfo function handles the following scenarios:

- If there are no values for server and port in the <u>Microsoft Windows Registry</u>, GetServerInfo does *not* display its dialogue window, and the automatic default values returned are BROKERSERVER/\<REDACTED\>. GetServerInfo returns mrOK.
- If exactly one server and port entry is defined in the <u>Microsoft Windows Registry</u>, GetServerInfo does *not* display its dialogue window. The values in the single <u>Microsoft Windows Registry</u> entry are returned to the calling application, with no user interaction. GetServerInfo returns mrOK.
- If more than one server and port entry exists in the <u>Microsoft Windows Registry</u>, the dialogue window is displayed. The only time that passed in server and port values are returned to the calling application is if the user selects Cancel. However, if a user selects an entry and presses OK, the server and port parameters are changed and returned to the calling application. GetServerInfo returns mrOK if the user selected OK, or mrCancel if the user selected Cancel.
- A typical Microsoft<sup>®</sup> Windows Registry entry for a VistA M Server contains the following characteristics:
- Located in either of the following registries:
- HKEY_LOCAL_MACHINE (HKLM)—Registry for accessibility to *all users* of a computer.
- HKEY_CURRENT_USER (HKCU)—Registry for accessibility to a *single user*.
- Located in the following registry subdirectory:

Software\Vista\Broker\Servers

- String-type registry entry, where Value name contains the IP address or Fully Qualified Domain Name (FQDN) of the server, followed by the port number of the RPC Broker listener on the server. The information should be separated by a comma. For example:

myserver.\<REDACTED\>.va.gov,\<REDACTED\>

- The optional Value data contains the SSHUsername to be used to establish an encrypted connection to the VistA M Server.

![](xwb-1-1-73-developer-s-guide/269.png) REF: For a demonstration using the Broker and GetServerInfo function, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

#### Example

<u>Figure 55</u> is an example of the GetServerInfo function:

<span id="_Ref446333055" class="anchor"></span>Figure 54: GetServerInfo Function—Example

procedure TForm1.btnConnectClick(Sender: TObject);

var

strServer, strPort, strSSHUsername: string;

begin

if GetServerInfo(strServer, strPort, strSSHUsername)\<\> mrCancel thenbegin

*{getsvrinfo begin}*

brkrRPCBroker1.Server := strServer;

brkrRPCBroker1.ListenerPort := StrToInt(strPort);

brkrRPCBroker1.SSHUser := strSSHUsername;

brkrRPCBroker1.Connected := True;

*{getsvrinfo end}*end;

end;

![](xwb-1-1-73-developer-s-guide/270.png) REF: For a demonstration using the Broker and GetServerInfo function, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

### GetServerIP Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GetServerIP function provides a means for determining the [Internet Protocol (IP) address](#IP_Address) for a specified VistA M Server address. The value returned is a string containing the [IP address](#IP_Address), or if it could *not* be resolved, the string “Unknown!”

function GetServerIP(ServerName: string): string;

#### Example

<u>Figure 56</u> is an example of the GetServerIP function:

<span id="_Ref446333089" class="anchor"></span>Figure 55: GetServerIP Function—Example

*// include the unit RpcConf1 in the Uses clause// An edit box on the form is assumed to be named edtIPAddress// Another edit box (edtInput) is used to input a desired server name*uses RpcConf1;

 

procedure Tform1.Button1Click(Sender: TObject);

var

ServerName: string;

begin

ServerName := ‘\<REDACTED\>.va.gov’;

edtIPAddress.Text := GetServerIP(edtInput.Text);

*// For \<REDACTED\>.va.gov returns ‘999.999.9.99’// For garbage returns ‘Unknown!’*end;

![](xwb-1-1-73-developer-s-guide/271.png) CAUTION: The GetServerIP function has limited use in a modern TCP/IP network, as multiple IP addresses can be assigned to a single server. It is expected to be deprecated and replaced in future releases with a function that returns a list of IP addresses.

### ChangeVerify Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ChangeVerify function can be used to provide the user with the ability to change his/her Verify code.

function ChangeVerify(RPCBroker: TRPCBroker): Boolean;

#### Argument

| Argument      | Description                                                                    |
|---------------|--------------------------------------------------------------------------------|
| RPCBroker | The Broker instance for the account on which the Verify code is to be changed. |

<span id="_Toc82593686" class="anchor"></span>Table 21: SilentChangeVerify Function—Arguments

#### Result

The return value indicates whether the user changed their Verify code or not.

- True—User changed their Verify code.
- False—User did *not* change their Verify code.

### SilentChangeVerify Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SilentChangeVerify function can be used to change the Verify code for a user without any dialogue windows being displayed.

function SilentChangeVerify(RPCBroker: TRPCBroker; OldVerify,

 NewVerify1, NewVerify2: String; var Reason: String): Boolean;

#### Arguments

| Argument       | Description                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| RPCBroker  | The current instance of the Broker for the account for which the Verify code is to be changed.                        |
| OldVerify  | The string representing the current Verify code for the user.                                                         |
| NewVerify1 | A string representing the new Verify code for the user.                                                               |
| NewVerify2 | A second independent entry for the string representing the new Verify code for the user.                              |
| Reason     | A string that on return contains the reason why the Verify code was *not* changed (if the result value is False). |

<span id="_Toc82593687" class="anchor"></span>Table 22: StartProgSLogin Method—Arguments

#### Result

The return value indicates whether the Verify code was successfully changed or not:

- True—Verify code was successfully changed.
- False—Verify code was *not* successfully changed. The reason for the failure is in the Reason argument.

### StartProgSLogin Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The StartProgSLogin method can be used to initiate another program with information sufficient for a <u>Silent Login</u>, or it can be used to launch a standalone program that does *not* use a <u>TRPCBroker Component</u> connection. If the program is being used to launch another executable with information for a <u>Silent Login</u>, it is *recommended* that the <u>CheckCmdLine Function</u> be used in the program being launched (since this function uses the command line information to make a <u>Silent Login</u> if possible).

procedure StartProgSLogin(const ProgLine: String; ConnectedBroker: TRPCBroker);

#### Arguments

<table>
<caption><p><span id="_Toc82593688" class="anchor"></span>Table 23: Direct RPCs</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ProgLine</strong></td>
<td><p>This is the command line that should be used as the basis for launching the executable. It contains the executable (and path, if not in the working directory or in the system path) and any command line arguments desired. If the ConnectedBroker argument is <em>not</em> nil, then the following are added to the command line and the application launched:</p>
<ul>
<li><p>VistA M Server address</p></li>
<li><p>ListenerPort</p></li>
<li><p>Division</p></li>
<li><p>ApplicationToken</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>ConnectedBroker</strong></td>
<td>This is the instance of the TRPCBroker that should be used to obtain an ApplicationToken for a <u>Silent Login</u>. The VistA M Server address and ListenerPort for this instance are used as command line arguments for launching the application, so that it makes a connection to the same Server/ListenerPort (see <u>Server Property</u> and <u>ListenerPort Property</u>) combination. If the application to be launched is <em>not</em> related to the TRPCBroker, then this argument should be set to nil.</td>
</tr>
</tbody>
</table>

<span id="_Toc82593688" class="anchor"></span>Table 23: Direct RPCs

#### Example 1

To launch a program, Sample1.exe, with command line arguments xval=MyData and yval=YourData, and connect with a <u>Silent Login</u> (which would be handled in Sample1.exe via the <u>CheckCmdLine Function</u>):

<span id="_Toc82593617" class="anchor"></span>Figure 56: SilentChangeVerify Function—Example

MyCommand := ‘C:\Program Files\VISTA\Test1\Sample1.exe xval=MyData yval=YourData’;

StartProgSLogin(MyCommand, RPCBroker1);

This results in the command line in <u>Figure 58</u> being used to launch the application:

<span id="_Ref449019516" class="anchor"></span>Figure 57: SilentChangeVerify Function—Example of Command Line Code to Launch the Application

C:\Program Files\VISTA\Test1\Sample1.exe xval=MyData yval=YourData s=ServerName p=\<REDACTED\> d=Division h=AppHandleValue

#### Example 2

To launch a program unrelated to TRPCBroker and VistA M Server connections (e.g., Microsoft<sup>®</sup> Notepad), the command line as desired is used as the first argument, and the value nil is used as the second argument:

<span id="_Toc82593619" class="anchor"></span>Figure 58: SilentChangeVerify Function—Example of Command Line Code to Launch Program Unrelated to TRPCBroker and VistA M Server Connections

MyCommand := ‘Notepad logtable.txt’;

StartProgSLogin(MyCommand, nil);

### VistA Splash Screen Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BDK provides two procedures in the SplVista.PAS unit to display a VistA Splash Screen when an application loads:

- procedure SplashOpen;
- procedure SplashClose(TimeOut: longint);

It is *recommended* that the VistA Splash Screen be opened and closed in the section of Pascal code in an application’s project file (i.e., .DPR).

#### Using a Splash Screen in an Application

To use the VistA Splash Screen in an application

1.  Open your application’s project file (i.e., .DPR). In Delphi:
1.  Select View.
2.  Select Project Source.
16. Include the SplVista in the uses clause of the project source.
17. Call SplashOpen *immediately after* the first form of your application is created and call SplashClose *just prior to* invoking the Application.Run method.
18. Use the TimeOut parameter to ensure a minimum display time. The TimeOut parameter is the minimum number of milliseconds the splash screen is displayed to the user.

The VistA Splash Screen is illustrated in <u>Figure 60</u>:

<span id="_Ref384050616" class="anchor"></span>Figure 59: Sample VistA Splash Screen

![](xwb-1-1-73-developer-s-guide/272.png)

#### Example

<u>Figure 61</u> is an example of code to display the VistA Splash Screen in an application:

<span id="_Ref446319507" class="anchor"></span>Figure 60: Sample Code to Display a VistA Splash Screen

uses

Forms, Unit1 in ‘Unit1.pas’, SplVista;

*{\$R \*.RES}*begin

Application.Initialize;

Application.CreateForm(TForm1, Form1);

SplashOpen;

SplashClose(2000);

Application.Run;

end.

![](xwb-1-1-73-developer-s-guide/273.png) REF: For a demonstration using the VistA Splash Screen, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

## Running RPCs on a Remote Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker can be used to facilitate invocation of Remote Procedure Calls on a remote VistA M Server. Applications can use either <u>XWB DIRECT RPC</u> or <u>XWB REMOTE RPC</u> to pass the following:

- Desired remote VistA M Server.
- Desired remote RPC.
- Any parameters for the remote RPC.

The RPC Broker on the local VistA M Server uses VistA Health Level Seven (HL7) as a vehicle to pass the remote RPC name and parameters to the remote VistA M Server. VistA HL7 is used to send any results from the remote server back to the local server. The RPC Broker on the local VistA M Server then passes the results back to the client application.

![](xwb-1-1-73-developer-s-guide/274.png) NOTE: The local VistA M Server is the server the user is logged into. The remote VistA M Server is any server the user is *not* logged into.

### Using Direct RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| RPC                   | Description                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>XWB DIRECT RPC</u> | This RPC blocks all other Broker calls until the results of the remote RPC are returned. The data is passed, and the user waits for the results to return from the remote system. |

<span id="_Toc82593689" class="anchor"></span>Table 24: Remote RPCs

### Using Remote RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| RPC                            | Description                                                                                                                                                                                                                                                                                               |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>XWB REMOTE RPC</u>          | This RPC allows other activity while the remote RPC is in process. In response to <u>XWB REMOTE RPC</u> the local VistA M Server returns a [HANDLE](#HANDLE) to the user application. At this point other Broker calls can commence while the server-to-server communication continues in the background. |
| <u>XWB REMOTE STATUS CHECK</u> | This RPC allows the application to check the local VistA M Server for the presence of results from the remote RPC. This RPC passes the [HANDLE](#HANDLE) to the local server and receives back the status of the remote RPC.                                                                              |
| <u>XWB REMOTE GETDATA</u>      | This RPC retrieves the results from the remote RPC after the status check indicates that the data has returned to the local VistA M Server. The RPC passes the [HANDLE](#HANDLE) and receives back an array with whatever data has been sent back from the remote site.                                   |
| <u>XWB REMOTE CLEAR</u>        | This RPC *must* be used to clear the data under the [HANDLE](#HANDLE) in the ^XTMP global.                                                                                                                                                                                                            |
| <u>XWB DEFERRED CLEARALL</u>   | Applications using <u>XWB REMOTE RPC</u> should use <u>XWB DEFERRED CLEARALL</u> on application close to clear all known data associated with the job on the VistA M Server.                                                                                                                              |

<span id="_Toc82593690" class="anchor"></span>Table 25: XWB ARE RPCS AVAILABLE—Parameters

![](xwb-1-1-73-developer-s-guide/275.png) NOTE: *All* XWB Remote Procedure Calls (RPCs) are available only on a Controlled Subscription basis.

### Checking RPC Availability on a Remote Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications can check the availability of RPCs on a remote VistA M Server. Use either of the following:

- <u>XWB DIRECT RPC</u>
- <u>XWB REMOTE RPC</u>

To pass either of the following:

- <u>XWB IS RPC AVAILABLE</u> (example)
- <u>XWB ARE RPCS AVAILABLE</u> (example)

To the remote server.

The RUN CONTEXT PARAMETER in <u>XWB IS RPC AVAILABLE</u> or <u>XWB ARE RPCS AVAILABLE</u> should be set to “R” or NULL to check that the remote VistA M Server allows RPCs to be run by users *not* logged into that remote server.

![](xwb-1-1-73-developer-s-guide/276.png) NOTE: *All* XWB Remote Procedure Calls (RPCs) are available only on a Controlled Subscription basis.

### XWB ARE RPCS AVAILABLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Checking RPC Availability on a Remote Server</u>

Use this RPC to determine if a set of RPCs is available on a VistA M Server. The RUN CONTEXT PARAMETER allows you to test availability on a local or remote VistA M Server. The RPC INPUT PARAMETER passes the names and (optionally) minimum version number of the RPCs to be checked.

<table>
<caption><p><span id="_Toc82593691" class="anchor"></span>Table 26: XWB IS RPC AVAILABLE—Parameters/Output</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RETURN VALUE</strong></td>
<td><p>A <strong>0-based</strong> array. The index corresponds to the index of the RPC in the RPC Input Parameter:</p>
<ul>
<li><p><strong>1—</strong>RPC Available.</p></li>
<li><p><strong>0—</strong>RPC Not available.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>RUN CONTEXT PARAMETER (Optional)</strong></td>
<td><p>Pass the run context (local or remote) of the RPC in Param[0].Value, and the type (<strong>literal</strong>) in <strong>Param[0].PType</strong>. Possible values:</p>
<ul>
<li><p><strong>L—</strong>Check if available to be run locally (by a user logged into the VistA M Server).</p></li>
<li><p><strong>R—</strong>Check if available to be run remotely (by a user logged in a different VistA M Server).</p></li>
</ul>
<p>If this parameter is <em>not</em> sent, the RPC is checked for both local and remote, and both run contexts <em>must</em> be available for the return to be “<strong>1</strong>” (RPC Available). The check is done against the INACTIVE field in the REMOTE PROCEDURE file (see the “<u>Blocking an RPC</u>” section).</p></td>
</tr>
<tr class="odd">
<td><strong>RPC INPUT PARAMETER</strong></td>
<td><p>Pass a <strong>0</strong>-based array of the names and (optionally) version numbers of RPCs to be tested in <strong>Param[1].Mult[]</strong>, and the type (<strong>List</strong>) in <strong>Param[1].PType</strong>. The format is:</p>
<p><strong>RPCName^RPCVersionNumber</strong></p>
<p>The RPCVersionNumber is used only if the Run Context parameter = “<strong>R</strong>”. If a numeric value is in the second ^-piece and Run Context = “<strong>R</strong>”, it is checked against the value in the VERSION field of the REMOTE PROCEDURE file (see the “<u>RPC Version</u>” section). If the version number passed is less than or equal to the number in the VERSION field, the RPC is marked available.</p>
<p>![](xwb-1-1-73-developer-s-guide/277.png) <strong>NOTE:</strong> If the VERSION field Is <strong>NULL</strong>, the check fails for a numeric value in this parameter.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc82593691" class="anchor"></span>Table 26: XWB IS RPC AVAILABLE—Parameters/Output

Also, the current context of your user *must* give them permission to execute the XWB ARE RPCS AVAILABLE (it *must* be included in the RPC multiple of the “B”-type option registered with the <u>CreateContext Method</u>).

![](xwb-1-1-73-developer-s-guide/278.png) NOTE:XWB ARE RPCS AVAILABLE is available only on a Controlled Subscription basis.

#### Example

<u>Figure 62</u> is an example of the <u>XWB ARE RPCS AVAILABLE</u> RPC:

<span id="_Ref446333172" class="anchor"></span>Figure 61: XWB ARE RPCS AVAILABLE—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB ARE RPCS AVAILABLE’;

brkrRPCBroker1.Param\[0\].Ptype:= Literal;

brkrRPCBroker1.Param\[0\].Value := ‘L’;

brkrRPCBroker1.Param\[1\].Ptype := List;

brkrRPCBroker1.Param\[1\].Mult\[‘0’\] = ‘MY FIRST RPC’;

brkrRPCBroker1.Param\[1\].Mult\[‘1’\] = ‘MY OTHER RPC^2’;

try

brkrRPCBroker1.Call;

except

On EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; branch code to handle availability of RPCs

### XWB IS RPC AVAILABLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Checking RPC Availability on a Remote Server</u>

Use this RPC to determine if a particular RPC is available on a VistA M Server. The RPC PARAMETER passes the name of the RPC to be checked. The RUN CONTEXT PARAMETER allows you to test availability to a local or a remote user. The VERSION NUMBER PARAMETER allows you to check for a minimum version of an RPC on a remote VistA M Server.

<table>
<caption><p><span id="_Toc82593692" class="anchor"></span>Table 27: XWB DIRECT RPC—Parameters/Output</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter/Output</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RETURN VALUE</strong></td>
<td><p>Boolean:</p>
<ul>
<li><p><strong>1—</strong>RPC Available</p></li>
<li><p><strong>0—</strong>RPC Not Available</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>RPC PARAMETER</strong></td>
<td>Pass the name of the RPC to be tested in <strong>Param[0].Value</strong>, and the type (<strong>literal</strong>) in <strong>Param[0].PType</strong>.</td>
</tr>
<tr class="odd">
<td><strong>RUN CONTEXT PARAMETER (Optional)</strong></td>
<td><p>Pass the run context (local or remote) of the RPC in <strong>Param[1].Value</strong>, and the type (<strong>literal</strong>) in <strong>Param[1].PType</strong>. Possible values:</p>
<ul>
<li><p><strong>L—</strong>Check if available to be run locally (by a user logged into the VistA M Server).</p></li>
<li><p><strong>R—</strong>Check if available to be run remotely (by a user logged in a different VistA M Server).</p></li>
</ul>
<p>If this parameter is <em>not</em> sent, the RPC is checked for both local and remote and both run contexts <em>must</em> be available for the return to be “<strong>1</strong>” (RPC Available). The check is done against the INACTIVE field in the REMOTE PROCEDURE file (see the “<u>Blocking an RPC</u>” section).</p></td>
</tr>
<tr class="even">
<td><strong>VERSION NUMBER PARAMETER (Optional)</strong></td>
<td><p>Pass the minimum acceptable version number of the RPC in <strong>Param[2].Value</strong>, and the type (<strong>literal</strong>) in <strong>Param[2].PType</strong>. This parameter is only used if the RUN CONTEXT parameter = “<strong>R</strong>”. If a numeric value is in this parameter, it is checked against the value in the VERSION field of the REMOTE PROCEDURE file (see the “<u>RPC Version</u>” section). If the version number passed is less than or equal to the number in the VERSION field, the RPC is marked available.</p>
<p>![](xwb-1-1-73-developer-s-guide/279.png) <strong>NOTE:</strong> If the VERSION field is <strong>NULL</strong>, the check fails for a numeric value in this parameter.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc82593692" class="anchor"></span>Table 27: XWB DIRECT RPC—Parameters/Output

Also, the current context of your user *must* give them permission to execute the XWB IS RPC AVAILABLE (it *must* be included in the RPC multiple of the “B”-type option registered with the <u>CreateContext Method</u>).

![](xwb-1-1-73-developer-s-guide/280.png) NOTE:XWB IS RPC AVAILABLE is available only on a Controlled Subscription basis.

#### Example

<u>Figure 63</u> is an example of the <u>XWB IS RPC AVAILABLE</u> RPC:

<span id="_Ref446333208" class="anchor"></span>Figure 62: XWB IS RPC AVAILABLE—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB IS RPC AVAILABLE’;

brkrRPCBroker1.Param\[0\].Value :=‘XWB GET VARIABLE VALUE’;

brkrRPCBroker1.Param\[0\].PType := literal;

brkrRPCBroker1.Param\[1\].Value := ‘R’;

brkrRPCBroker1.Param\[1\].PType := literal;

*{no version number passed in this example as XWB GET VARIABLE VALUE has only one version}*try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; branch code to handle RPC availability

### XWB DIRECT RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to request that an RPC be run on a remote system. This RPC blocks all other Broker calls until the results of the remote RPC are returned. Use <u>XWB REMOTE RPC</u> to allow other Broker activity while the remote RPC runs.

![](xwb-1-1-73-developer-s-guide/281.png) REF: For a comparison of the two methods, see the “<u>Running RPCs on a Remote Server</u>” section.

| Parameter/Output                     | Description                                                                                                                                                                                                                                                               |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCATION PARAMETER               | Pass the station number of the remote VistA M Server in Param\[0\].Value, and the type (literal) in Param\[0\].PType.                                                                                                                                         |
| RPC PARAMETER                    | Pass the name of the RPC to be run in Param\[1\].Value, and the type (literal) in Param\[1\].PType.                                                                                                                                                           |
| RPC VERSION PARAMETER (Optional) | Pass minimum version of RPC to be run in Param\[2\].Value, and the type (literal) in Param\[2\].PType. It is checked against the value in the VERSION field of the REMOTE PROCEDURE file (see the “<u>RPC Version</u>” section) on the remote VistA M Server. |
| PARAMETERS TO THE REMOTE RPC     | Pass up to seven parameters for the remote RPC in Param\[3\] through Param\[9\].                                                                                                                                                                                  |
| RETURN VALUE                     | An array with whatever data has been sent back from the remote site. In the case of an error condition, the first node of the array is equal to a string with the syntax “-1^error text”.                                                                             |

<span id="_Toc82593693" class="anchor"></span>Table 28: XWB REMOTE RPC—Parameters/Output

![](xwb-1-1-73-developer-s-guide/282.png) NOTE:XWB DIRECT RPC is available only on a Controlled Subscription basis.

#### Example

<u>Figure 64</u> is an example of the <u>XWB DIRECT RPC</u>:

<span id="_Ref446333239" class="anchor"></span>Figure 63: XWB DIRECT RPC—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DIRECT RPC’;

brkrRPCBroker1.Param\[0\].Ptype:= Literal;

brkrRPCBroker1.Param\[0\].Value := ‘Station Number’;

brkrRPCBroker1.Param\[1\].Ptype:= Literal;

brkrRPCBroker1.Param\[1\].Value := ‘XWB GET VARIABLE VALUE’;

*{no version numbers for remote RPC so NULL value in Param\[2\]}*

brkrRPCBroker1.Param\[2\].Ptype:= Literal;

brkrRPCBroker1.Param\[2\].Value := ‘’;

brkrRPCBroker1.Param\[3\].Ptype:= Reference;

brkrRPCBroker1.Param\[3\].Value := ‘DUZ’;

try

brkrRPCBroker1.Call;

except

On EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to handle brkrRPCBroker1.Results\[\]

### XWB REMOTE RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to request that an RPC be run on a remote system. This RPC allows other Broker activity while the remote RPC runs. Use <u>XWB DIRECT RPC</u> to block all other Broker activity while the remote RPC runs.

![](xwb-1-1-73-developer-s-guide/283.png) REF: For a comparison of the two methods, see the “<u>Running RPCs on a Remote Server</u>” section.

XWB REMOTE RPC requests the remote RPC. The return value is a [HANDLE](#HANDLE) that is used to check status and retrieve data. The following RPCs *must* be used to complete the transaction

- <u>XWB REMOTE STATUS CHECK</u>
- <u>XWB REMOTE GETDATA</u>
- <u>XWB REMOTE CLEAR</u>

| Parameter/Output                     | Description                                                                                                                                                                                                                                                                                                              |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCATION PARAMETER               | Pass the station number of the remote VistA M Server in Param\[0\].Value, and the type (literal) in Param\[0\].PType.                                                                                                                                                                                        |
| RPC PARAMETER                    | Pass the name of the RPC to be run in Param\[1\].Value, and the type (literal) in Param\[1\].PType.                                                                                                                                                                                                          |
| RPC VERSION PARAMETER (Optional) | Pass minimum version of RPC to be run in Param\[2\].Value, and the type (literal) in Param\[2\].PType. It is checked against the value in the VERSION field of the REMOTE PROCEDURE file (see the “<u>RPC Version</u>” section) on the remote VistA M Server.                                                |
| PARAMETERS TO THE REMOTE RPC     | Pass up to seven parameters for the remote RPC in Param\[3\] through Param\[9\].                                                                                                                                                                                                                                 |
| RETURN VALUE                     | An array. The first node is equal to a string that serves as a [HANDLE](#HANDLE). This [HANDLE](#HANDLE) should be stored by the application and used to check the status and retrieve the data. In the case of an error condition the first node of the array is equal to a string with the syntax “-1^error text”. |

<span id="_Toc82593694" class="anchor"></span>Table 29: XWB REMOTE STATUS CHECK—Output

![](xwb-1-1-73-developer-s-guide/284.png) NOTE:XWB REMOTE RPC is available only on a Controlled Subscription basis.

#### Example

<u>Figure 65</u> is an example of the XWB REMOTE RPC:

<span id="_Ref446333271" class="anchor"></span>Figure 64: XWB REMOTE RPC—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB REMOTE RPC’;

brkrRPCBroker1.Param\[0\].Ptype:= Literal;

brkrRPCBroker1.Param\[0\].Value := ‘Station Number’;

brkrRPCBroker1.Param\[1\].Ptype:= Literal;

brkrRPCBroker1.Param\[1\].Value := ‘MY RPC’;

brkrRPCBroker1.Param\[2\].Ptype:= Literal;

brkrRPCBroker1.Param\[2\].Value := ‘1’;

brkrRPCBroker1.Param\[3\].Ptype:= Reference;

brkrRPCBroker1.Param\[3\].Value := ‘MY RPC PARAMETER’;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to store HANDLE returned in brkrRPCBroker1.Results\[\]

The application needs to use <u>XWB REMOTE STATUS CHECK</u>, <u>XWB REMOTE GETDATA</u>, *and* <u>XWB REMOTE CLEAR</u> to complete the transaction.

### XWB REMOTE STATUS CHECK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to check for results of <u>XWB REMOTE RPC</u>. Periodically call this RPC and pass the [HANDLE](#HANDLE) returned by <u>XWB REMOTE RPC</u>.

<table>
<caption><p><span id="_Toc82593695" class="anchor"></span>Table 30: XWB REMOTE GETDATA—Output</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Output</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RETURN VALUE</strong></td>
<td><p>The return value is always an array. The first node of the array is equal to one of the following values:</p>
<ul>
<li><p><strong>“-1^Bad Handle—</strong>An invalid handle has been passed.</p></li>
<li><p><strong>“0^New”—</strong>The request has been sent via VistA HL7.</p></li>
<li><p><strong>“0^Running”—</strong>VistA HL7 indicates that the message is being processed.</p></li>
<li><p><strong>“1^Done”—</strong>RPC has completed, and the data has been returned to the local VistA M Server. The data is <em>not</em> returned by this RPC. Use <u>XWB REMOTE GETDATA</u> to retrieve the data.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc82593695" class="anchor"></span>Table 30: XWB REMOTE GETDATA—Output

The second node of the array is the status from the VistA HL7 software.

![](xwb-1-1-73-developer-s-guide/285.png) NOTE: XWB REMOTE STATUS CHECK is available only on a Controlled Subscription basis.

#### Example

<u>Figure 66</u> is an example of the <u>XWB REMOTE STATUS CHECK</u> RPC:

<span id="_Ref446334302" class="anchor"></span>Figure 65: XWB REMOTE STATUS CHECK—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB REMOTE STATUS CHECK’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to handle results of check

### XWB REMOTE GETDATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to retrieve the results of <u>XWB REMOTE RPC</u>. Before calling this RPC, use <u>XWB REMOTE STATUS CHECK</u> to ensure that the results have been returned to the local VistA M Server. When the results have arrived, call this RPC and pass the [HANDLE](#HANDLE) returned by <u>XWB REMOTE RPC</u>.

After the application is finished with the data on the VistA M Server, it should use <u>XWB REMOTE CLEAR</u> to clear the ^XTMP global.

| Output           | Description                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| RETURN VALUE | An array containing the data. In the case of an error condition the first node of the array is equal to a string with the syntax “-1^error text”. |

<span id="_Toc82593696" class="anchor"></span>Table 31: XWB REMOTE CLEAR—Output

![](xwb-1-1-73-developer-s-guide/286.png) NOTE: XWB REMOTE GETDATA is available only on a Controlled Subscription basis.

#### Example

<u>Figure 67</u> is an example of the <u>XWB REMOTE GETDATA</u> RPC:

<span id="_Ref446334331" class="anchor"></span>Figure 66: XWB REMOTE GETDATA—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB REMOTE GETDATA’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to handle data

### XWB REMOTE CLEAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC is used to clear the data created by a remote RPC under the [HANDLE](#HANDLE) in the ^XTMP global. Pass the [HANDLE](#HANDLE) returned by <u>XWB REMOTE RPC</u>.

| Output           | Description                                              |
|------------------|----------------------------------------------------------|
| RETURN VALUE | An array. The first node in the array is equal to 1. |

<span id="_Toc82593697" class="anchor"></span>Table 32: Deferred RPCs

![](xwb-1-1-73-developer-s-guide/287.png) NOTE: XWB REMOTE CLEAR is available only on a Controlled Subscription basis.

#### Example

<u>Figure 68</u> is an example of the <u>XWB REMOTE CLEAR</u> RPC:

<span id="_Ref446334367" class="anchor"></span>Figure 67: XWB REMOTE CLEAR—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB REMOTE CLEAR’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

## Deferred RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remote Procedure Calls can be run in the background with <u>XWB DEFERRED RPC</u>.

#### Using Deferred RPCs

| RPC                          | Description                                                                                                                                                                                                                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>XWB DEFERRED RPC</u>      | Use this RPC to pass the name of the RPC to be run in deferred mode and any parameters associated with the deferred RPC. In response to this RPC the VistA M Server returns a [HANDLE](#HANDLE) to the user application. At this point other Broker calls can commence while the job runs in the background. |
| <u>XWB DEFERRED STATUS</u>   | This RPC allows the application to check the local VistA M Server for the presence of results from the deferred RPC. This RPC passes the [HANDLE](#HANDLE) to the local server and receives back the status of the remote RPC.                                                                               |
| <u>XWB DEFERRED GETDATA</u>  | This RPC is the vehicle for retrieving the results from the remote RPC after the status check indicates that the data has returned to the local VistA M Server. The RPC passes the [HANDLE](#HANDLE) and receives back an array with whatever data has been returned by the deferred RPC.                    |
| <u>XWB DEFERRED CLEAR</u>    | This RPC *must* be used to clear the data under the [HANDLE](#HANDLE) in the ^XTMP global.                                                                                                                                                                                                               |
| <u>XWB DEFERRED CLEARALL</u> | Applications using <u>XWB DEFERRED RPC</u> should use <u>XWB DEFERRED CLEARALL</u> on application close to clear all known data associated with the job on the VistA M Server.                                                                                                                               |

<span id="_Toc82593698" class="anchor"></span>Table 33: XWB DEFERRED RPC—Parameters/Output

![](xwb-1-1-73-developer-s-guide/288.png) NOTE: *All* XWB Remote Procedure Calls (RPCs) are available only on a Controlled Subscription basis.

### XWB DEFERRED RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to request that an RPC be run in deferred mode. The return value is a [[HANDLE](#HANDLE)](#other_api_handle_htm) used to check status and retrieve data. The following RPCs *must* be used to complete the transaction:

- <u>XWB DEFERRED STATUS</u>
- <u>XWB DEFERRED GETDATA</u>
- <u>XWB DEFERRED CLEAR</u>

| Parameter/Output                     | Description                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPC PARAMETER                    | Pass the name of the RPC to be run in Param\[0\].Value, and the type (literal) in Param\[0\].PType.                                                                                                                                                                                                                                    |
| RPC VERSION PARAMETER (Optional) | Pass minimum version of RPC to be run in Param\[1\].Value, and the type (literal) in Param\[1\].PType. It is checked against the value in the VERSION field of the REMOTE PROCEDURE file (see the “<u>RPC Version</u>” section) on the remote VistA M Server.                                                                          |
| PARAMETERS TO THE REMOTE RPC     | Pass up to eight parameters for the remote RPC in Param\[2\] through Param\[9\].                                                                                                                                                                                                                                                           |
| RETURN VALUE                     | An array. The first node is equal to a string that serves as a [[HANDLE](#HANDLE)](#other_api_handle_htm). This [HANDLE](#HANDLE) should be stored by the application and used to check the status and retrieve the data. In the case of an error condition, the first node of the array is equal to a string with the syntax “-1^error text”. |

<span id="_Toc82593699" class="anchor"></span>Table 34: XWB DEFERRED STATUS—Output

#### Example

<u>Figure 69</u> is an example of the <u>XWB DEFERRED RPC</u>:

<span id="_Ref446334395" class="anchor"></span>Figure 68: XWB DEFERRED RPC—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DEFERRED RPC’;

brkrRPCBroker1.Param\[0\].Ptype:= Literal;

brkrRPCBroker1.Param\[0\].Value := ‘MY RPC’;

brkrRPCBroker1.Param\[1\].Ptype:= Literal;

brkrRPCBroker1.Param\[1\].Value := ‘1’;

brkrRPCBroker1.Param\[2\].Ptype:= Reference;

brkrRPCBroker1.Param\[2\].Value := ‘MY RPC PARAMETER’;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to store HANDLE returned in brkrRPCBroker1.Results\[0\]

The application needs to use <u>XWB DEFERRED STATUS</u>, <u>XWB DEFERRED GETDATA</u>, *and* <u>XWB DEFERRED CLEAR</u> to complete the transaction.

### XWB DEFERRED STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to check for results of <u>XWB DEFERRED RPC</u>. Periodically, call this RPC and pass the [[HANDLE](#HANDLE)](#other_api_handle_htm) returned by <u>XWB REMOTE RPC</u>.

<table>
<caption><p><span id="_Toc82593700" class="anchor"></span>Table 35: XWB DEFERRED GETDATA—Output</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Output</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RETURN VALUE</strong></td>
<td><p>The return value is always an array. The first node of the array is equal to one of the following values:</p>
<ul>
<li><p><strong>“-1^Bad Handle”—</strong>An invalid handle has been passed.</p></li>
<li><p>“<strong>0^New”—</strong>The request has been sent via VistA HL7.</p></li>
<li><p><strong>“0^Running”—</strong>VistA HL7 indicates that the message is being processed.</p></li>
<li><p><strong>“1^Done”—</strong>RPC has completed, and the data has been returned to the local VistA M Server. The data is <em>not</em> returned by this RPC. Use <u>XWB REMOTE GETDATA</u> to retrieve the data.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc82593700" class="anchor"></span>Table 35: XWB DEFERRED GETDATA—Output

![](xwb-1-1-73-developer-s-guide/289.png) NOTE: XWB DEFERRED STATUS is available only on a Controlled Subscription basis.

#### Example

<u>Figure 70</u> is an example of the <u>XWB DEFERRED STATUS</u> RPC:

<span id="_Ref446334423" class="anchor"></span>Figure 69: XWB DEFERRED STATUS—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DEFERRED STATUS’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

 .; code to handle results of check

### XWB DEFERRED GETDATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this RPC to retrieve the results of <u>XWB DEFERRED RPC</u>. Before calling this RPC, use <u>XWB DEFERRED STATUS</u> to ensure that the job has finished. When the results are available, call this RPC and pass the [[HANDLE](#HANDLE)](#other_api_handle_htm) returned by <u>XWB DEFERRED RPC</u>.

After the application is finished with the data on the VistA M Server, it should use <u>XWB DEFERRED CLEAR</u> to clear the ^XTMP global.

| Output           | Description                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| RETURN VALUE | An array containing the data. In the case of an error condition the first node of the array is equal to a string with the syntax “-1^error text”. |

<span id="_Toc82593701" class="anchor"></span>Table 36: XWB DEFERRED CLEAR—Output

![](xwb-1-1-73-developer-s-guide/290.png) NOTE:XWB DEFERRED GETDATA is available only on a Controlled Subscription basis.

#### Example

<u>Figure 71</u> is an example of the <u>XWB DEFERRED GETDATA</u> RPC:

<span id="_Ref446334591" class="anchor"></span>Figure 70: XWB DEFERRED GETDATA—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DEFERRED GETDATA’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

.; code to handle data

### XWB DEFERRED CLEAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC is used to clear the data created by a deferred RPC under the [[HANDLE](#HANDLE)](#other_api_handle_htm) in the ^XTMP global. Pass the [HANDLE](#HANDLE) returned by <u>XWB DEFERRED RPC</u>.

| Output           | Description                                              |
|------------------|----------------------------------------------------------|
| RETURN VALUE | An array. The first node in the array is equal to 1. |

<span id="_Toc82593702" class="anchor"></span>Table 37: XWB DEFERRED CLEARALL—Output

![](xwb-1-1-73-developer-s-guide/291.png) NOTE: XWB DEFERRED CLEAR is available only on a Controlled Subscription basis.

#### Example

<u>Figure 72</u> is an example of the <u>XWB DEFERRED CLEAR</u> RPC:

<span id="_Ref446334603" class="anchor"></span>Figure 71: XWB DEFERRED CLEAR—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DEFERRED CLEAR’;

brkrRPCBroker1.Param\[0\].Value :=‘MYHANDLE’;

brkrRPCBroker1.Param\[0\].PType := literal;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

### XWB DEFERRED CLEARALL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RPC is used to CLEAR ALL the data known to a remote RPC or deferred RPC job in the ^XTMP global. It makes use of the list in ^TMP(“XWBHDL”,\$J,handle). Applications using <u>XWB REMOTE RPC</u> or the <u>XWB DEFERRED RPC</u> should use this RPC on application close to clear all known data associated with the job on the VistA M Server.

| Output           | Description                                              |
|------------------|----------------------------------------------------------|
| RETURN VALUE | An array. The first node in the array is equal to 1. |

<span id="_Ref384053764" class="anchor"></span>Table 38: Broker Error Messages

![](xwb-1-1-73-developer-s-guide/292.png) NOTE:XWB DEFERRED CLEARALL is available only on a Controlled Subscription basis.

#### Example

<u>Figure 73</u> is an example of the <u>XWB DEFERRED CLEARALL</u> RPC:

<span id="_Ref446334643" class="anchor"></span>Figure 72: XWB DEFERRED CLEARALL—Example

brkrRPCBroker1.RemoteProcedure := ‘XWB DEFERRED CLEAR’;

try

brkrRPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

# Broker Security Enhancement (BSE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview: Implementing Broker Security Enhancement (BSE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how application developers can modify their Veterans Health Information Systems and Technology Architecture (VistA) RPC Broker Delphi-based client/server applications in order to implement the Broker Security Enhancement (BSE). The following topics are discussed:

- <u>Assumptions When Implementing BSE</u>
- <u>Step-By-Step Procedures to Implement BSE</u>

## Assumptions When Implementing BSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following assumptions are made regarding application developers and VistA software applications when implementing BSE:

- Developer Training—Application developers should already be knowledgeable/trained in creating RPC Broker Delphi-based applications.
- RPC Broker-based Applications—RPC Broker Delphi-based application already exists.
- Login at Startup—Applications automatically initiate login at application startup (i.e., users are presented with 2-factor authentication or an Access/Verify login dialogue).
- VistA M Server Patches—All BSE Project-related VistA M Server patches have been loaded on the appropriate servers.

## Step-By-Step Procedures to Implement BSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the procedures that VistA application developers *must* follow in order to implement the Broker Security Enhancement (BSE) in their RPC Broker Delphi-based applications (i.e., COM client applications developed in Embarcadero Delphi), so that the application can make remote user/visitor connections.

1.  Create a unique Application Security Phrase *(required).*

Use the \$\$SHAHASH^XUSHSH API to create a Base-64 Encoded SHA256 hashed Security Phrase (case sensitive) that is unique for your application.

For example, in M, go to Programmer Mode and enter the following command:

W \$\$SHAHASH^XUSHSH(256,"My Application Security Phrase",”B”)

The resulting sample value is:

TQu07MtTls83BGuWK/Kyb4naAUWHaVQjTzstCuDJKHw=

![](xwb-1-1-73-developer-s-guide/293.png) CAUTION: This is a sample value only; do *not* use this as your Application Security Phrase!

This is a one-way hash value for the Security Phrase that is only known to the application that creates it.

![](xwb-1-1-73-developer-s-guide/294.png) RECOMMENDATION: Since the Security Phrase is the application's identifier, VistA Infrastructure (VI) *recommends* developers identify the Security Phrase as a const value in an include file in any RPC Broker Delphi-based program implementing BSE. A substitute include file containing a phrase similar to that used above should then be included with release of the source code.

![](xwb-1-1-73-developer-s-guide/295.png) REF: For more information on the application Security Phrase, see the "Security Phrase" section in the *RPC Broker User Guide*.

1.  Create an entry in the REMOTE APPLICATION (#8994.5) file *(required).*

An application *must* send out a patch that creates an entry for their RPC Broker Delphi-based application that has implemented BSE in the REMOTE APPLICATION (#8994.5) file. Developers *must* add entries to the following fields in File \#8994.5:

- NAME (#.01)—Enter a descriptive name for your application.
- CONTEXTOPTION (#.02)—Enter the name of the "B"-Type context option that the users will need to run the application. This context option should be within your application’s namespace, or your application should have an Integration Control Registration (ICR) agreement in place documenting permission to use a context option owned by another application.
- APPLICATIONCODE (#.03)—Enter the hashed value of the Security Phrase you created in Step 1.
- CALLBACKTYPE Multiple (#1):
  - CALLBACKTYPE (#.01)—Current values for this field are:
- R—RPC Broker TCP/IP connection (*recommended* for *non*-medical centers).
- M—M-to-M Broker connection.
- H—HyperText Transport Protocol (HTTP) connection communication. You must also add an entry in the URLSTRING (#.04) field.
- S—Station-number callback (*recommended* for medical centers).
  - CALLBACKPORT (#.02)—Enter the Port number to be used for the callback connection. This required field should be set to “-1” for Station-number callback type, as the actual port number is passed to the remote VistA M Server as part of the process.
  - CALLBACKSERVER (#.03)—Enter the address of the server to be used for the callback connection. This should be a Domain Name Service (DNS) name-based address rather than an Internet Protocol (IP) address, because IP addresses can change. This field is *not* required for Station-number callback type, as the remote VistA M Server looks up the IP address of the authenticating VistA M Server based on the site number passed to the remote VistA M Server as part of the process.
  - URLSTRING (#.04)—Used only if the CALLBACKTYPE (#.01) field contains H for HyperText Transport Protocol (HTTP). Enter the Uniform Resource Locator (URL) string for the callback to the HTTP server. This field is *not* required for Station-number, RPC Broker, or M-to-M callback types.

![](xwb-1-1-73-developer-s-guide/296.png) NOTE: For more information on the REMOTE APPLICATION (#8994.5) file and specific field entries, see the "REMOTE APPLICATION (#8994.5) file" section in the *RPC Broker User Guide*.

![](xwb-1-1-73-developer-s-guide/297.png) REF: Use the sample code in the BseSample1.pas file as a basis for implementing BSE in your application. The BseSample1.pas file is located in the following directory:

BDK32\Samples\BSE

> <span id="_Toc303257698" class="anchor"></span>Figure 73: BseSample1.pas File—Sample Code Excerpt (#1)

procedure TForm1.DoConnection(Key: String);

var

TokenValue: String;

begin

RPCB.Server := AuthServer.Text;

RPCB.ListenerPort := StrToInt(AuthPort.Text);

RPCB.Connected := True;

if RPCB.Connected thenbegin

RPCB.RemoteProcedure := 'XUS SET VISITOR';

RPCB.Call;

TokenValue := RPCB.Results\[0\];

RPCB.Connected := False;

ShowMessage('Token: '+TokenValue);

ifnot (TokenValue = '') thenbegin

RPCB.Server := RemoteServer.Text;

RPCB.ListenerPort := StrToInt(RemotePort.Text);

RPCB.SecurityPhrase := Key + '^' + TokenValue;

RPCB.Connected := True;

if RPCB.Connected thenbegin

ShowMessage('Signed on to Remote Server');

RPCB.CreateContext('XWB BROKER EXAMPLE');

btnDisconnect.Enabled := True;

btnEcho.Enabled := True;

btnM2M.Enabled := False;

btnTCPIP.Enabled := False;

endelse

ShowMessage('Connection to Remote Server failed!');

end;

endelse

ShowMessage('Initial Sign-on Failed');

end;

2.  Get BSE Authentication Token *(required).*

After authenticating the user into the authenticating VistA M Server, the client application calls the XUS SET VISITOR RPC to get the BSE Authentication Token for the user. This token is then passed to the RPC Broker component and used to create an extended Security Pass Phrase (see Step 4). This token is eventually used to obtain the necessary user information for populating a user as a "visitor" entry in the remote site's NEW PERSON (#200) file.

VistA Kernel software on the authenticating VistA M Server creates the BSE Authentication Token. Kernel stores this token in the ^XTMP temporary global.

> <span id="_Toc303257699" class="anchor"></span>Figure 74: BseSample1.pas File—Sample Code Excerpt (#2)

RPCB.Server := AuthServer.Text;

RPCB.ListenerPort := StrToInt(AuthPort.Text);

RPCB.Connected := True;

if RPCB.Connected thenbegin

RPCB.RemoteProcedure := 'XUS SET VISITOR';

RPCB.Call;

TokenValue := RPCB.Results\[0\];

RPCB.Connected := False;

3.  Create and encode an extended Security Pass Phrase *(required).*

The application creates an extended Security Pass Phrase (string). The Security Pass Phrase consists of the unhashed application Security Phrase (Step 1) concatenated with the BSE Authentication Token (Step 4) delimited by a caret (^). For example:

My Application Security Phrase^XWBHDL977-124367_0

Station-number callback requires the authenticating VistA M Server’s station number as identified in the INSTITUTION (#4) file and the port number of the station’s RPC Broker listener, (Step 3) delimited by a caret (^). For example:

My Application Security Phrase^XWBHDL977-124367_0^518^19207

The Delphi RPC Broker software encodes the Security Pass Phrase, which is passed to the Remote VistA M Server XUS SIGNON SETUP RPC for authentication.

For *non*-Delphi applications (those that do *not* use the Broker Development Kit), the XUS BSE TOKEN RPC accepts the application Security Phrase on the authenticating server and creates a complete encoded extended Security Pass Phrase, which can be passed to the Remote VistA M Server XUS SIGNON SETUP RPC for authentication for Station-number based callback. This RPC does *not* work for Delphi applications, as the encoding is done within the Broker Development Kit.

In the source code excerpt that follows (see <u>Figure 76</u>), the value of Key (i.e., constant) was defined earlier by importing an include file that contained the following two lines:

const

Key = ' My Application Security Phrase';

![](xwb-1-1-73-developer-s-guide/298.png) NOTE:Key is a constant, which is a type of variable that has a fixed value that *cannot* be changed.

<u>Figure 76</u> shows the code after the RPCBroker login component connection to the Authenticating VistA M Server has been disconnected:

> <span id="_Ref137959689" class="anchor"></span>Figure 75: BseSample1.pas File—Sample Code Excerpt (#3)

ifnot (TokenValue = '') thenbegin

RPCB.Server := RemoteServer.Text;

RPCB.ListenerPort := StrToInt(RemotePort.Text);

RPCB.SecurityPhrase := Key + '^' + TokenValue;

RPCB.Connected := True;

if RPCB.Connected thenbegin

ShowMessage('Signed on to Remote Server');

RPCB.CreateContext('XWB BROKER EXAMPLE');

btnDisconnect.Enabled := True;

btnEcho.Enabled := True;

btnM2M.Enabled := False;

btnTCPIP.Enabled := False;

endelse

ShowMessage('Connection to Remote Server failed!');

end;

end

4.  Set RPCBroker login component properties *(required).*

The developer *must* set the following RPCBroker login component properties when calling the Remote VistA M Server:

- Server—Set to the Domain Name Service (DNS) or Internet Protocol (IP) address of the Remote VistA M Server.
- ListenerPort—Set to the Listener Port number of the Remote VistA M Server.
- SecurityPhrase—Set to the unhashed application's Security Phrase concatenated with the Kernel Authentication Token (See Step 4).
- Connected—Set to True.
5.  Process Remote User/Visitor Login on remote server *(required).*

After connecting to the Remote VistA M Server, software running on the Remote VistA M Server does the following:

1.  Identify the Security Pass Phrase. Kernel identifies the data passed in as a parameter, which contains the application's Security Phrase and Kernel Authentication Token for the user.
1.  Hash the Security Pass Phrase. Kernel hashes the Security Pass Phrase to parse out the application's Security Phrase and the Kernel Authentication Token.
2.  Get Authenticating VistA M Server Connection Mechanism. Kernel uses the Security Phrase to identify the application's entry in the REMOTE APPLICATION (#8994.5) file.

Included in that entry is the mechanisms for contacting the Authenticating VistA M Server:

- Connection type:
- R—RPC Broker TCP/IP connection
- M—M-to-M Broker
- H—HyperText Transport Protocol connection
- S—Station-number callback
- Port number
- Address (IP, DNS, or URL)

![](xwb-1-1-73-developer-s-guide/299.png) NOTE: The mechanisms for contacting the Authenticating VistA M Server allows you to use either the IP address or DNS; however, VistA Infrastructure (VI) *recommends* that you use a DNS Fully Qualified Domain Name (FQDN).

3.  Connect to Authenticating Server using Kernel Authentication Token. The Remote VistA M Server uses the appropriate mechanism to identify and connect to the Authenticating VistA M Server, passing in the BSE Authentication Token that identifies the user.
4.  Obtain user demographics. Kernel uses the XUS GET VISITOR RPC to request and obtain the user demographic information from the Authenticating VistA M Server.

The user demographic information that is returned is a string containing information that can be used to identify the visitor:

ssn^name^station name^station number^DUZ^phone^SecID^network username

- Social Security Number (SSN)
- Name
- Station Name
- Station Number
- DUZ
- Telephone
- Identity and Access Management (IAM) Security ID (SecID)
- Active Directory Network Username

This user demographic information is used to later establish the user as a remote user/visitor on the Remote VistA M Server.

5.  Disconnect from the Authenticating VistA M Server. The Remote VistA M Server disconnects from the Authenticating VistA M Server.
6.  Set up user as a visitor entry on the remote VistA M Server. Kernel uses the demographic information obtained from the Authenticating VistA M Server to set up the user as a visitor entry on the Remote VistA M Server.  
      
    Kernel creates or matches an entry in the NEW PERSON (#200) file and provides the visitor with the context option specified for the application in the REMOTE APPLICATION (#8994.5) file. The matching process uses the following precedence when matching an existing user:
1.  Identity and Access Management (IAM) Security ID (SecID)
2.  Social Security Number (SSN)
3.  Name (do *not* use if name has a different SSN)
6.  Test your application *(recommended).* Developers should test their RPC Broker Delphi-based applications to ensure they have successfully implemented BSE.

BSE Sample Test Applications

The Broker Development Kit (BDK) includes the BrokerSecurityEnhancement Sample1 application (i.e., BseSample1.exe, see <u>Figure 77</u>).

You can use this sample application to help test the sample entries in the REMOTE APPLICATION (#8994.5) file and to test the different connection types (i.e., TCP/IP, M2M, HTTP, and Station-number) to verify that the VistA M Server-side is set up correctly to implement BSE.

![](xwb-1-1-73-developer-s-guide/300.png) CAUTION: In order to implement BSE and use the RPC-Broker callback type, the central Authenticating VistA M server *must* run the RPC Broker as a TCPIP service.

BrokerSecurityEnhancement Sample1

<u>Figure 77</u> shows the sample application dialogue provided by the BrokerSecurityEnhancement Sample1 application (i.e., BseSample1.exe):

> <span id="_Ref136748615" class="anchor"></span>Figure 76: BSE Project—BrokerSecurityEnhancement Sample1 Application (i.e., BseSample1.exe)

> ![](xwb-1-1-73-developer-s-guide/301.png)

The sample application has the following controls:

- Server Edit Fields:
  - Authenticating Server IP—IP address for the Authenticating VistA M Server. This field is empty at initial startup; it is an editable field.
  - (Authenticating Server) Port—Port number for the Authenticating VistA M Server. This field is empty at initial startup; it is an editable field.
  - Remote Server IP—IP address for the Remote VistA M Server. This field is empty at initial startup; it is an editable field.
  - (Remote Server) Port—Port number for the Remote VistA M Server. This field is empty at initial startup; it is an editable field.
- Connection Buttons:
  - TCP/IP Connect
  - M2M Connect
  - HTTP Connect
  - Disconnect
- Phrase Echo Controls:
  - Phrase to Echo Edit Field—Enter an echo phrase.
  - Echo Button—Button used to submit the phrase to be echoed back form the Remote VistA M Server.
  - Echoed Field—Contains the phrase that gets echoed back once the user/visitor is signed onto the Remote VistA M Server.

To successfully run and test the BrokerSecurityEnhancement Sample1 application (i.e., BseSample1.exe), do the following:

1.  Edit entries for XUSBSE TEST1 and XUSBSE TEST2 in the following fields in the CALLBACKTYPE Multiple (#1) in the REMOTE APPLICATION (#8994.5) file. These entries are the Authenticating VistA M Servers that are used to authenticate the current user, and to which a callback is made to obtain information to eventually create the visitor entry in the Remote VistA M Server:
- CALLBACKPORT (#.02)
- CALLBACKSERVER (#.03)

The Broker Security Enhancement (BSE)-related code is dependent upon the use of appropriate and valid information for the Authenticating and Remote VistA M Servers. Therefore, running the BseSample1.exe program requires that you populate these fields on the Remote VistA M Server.

The Authenticating VistA M Server is the server on which the user already has a valid Kernel Access and Verify code established (i.e., entry in the NEW PERSON \[#200\] file). Both the Authenticating and Remote VistA M Servers *must* also have RPC Broker Patch XWB\*1.1\*45 and Kernel Patch XU\*8\*404 installed.

7.  Start the BseSample1.exe program.
8.  Enter a valid Authenticating VistA M Server IP address and Port number.

![](xwb-1-1-73-developer-s-guide/302.png) NOTE: This is the server against which the user first authenticates.

9.  Enter a valid Remote VistA M Server IP address and Port number.

![](xwb-1-1-73-developer-s-guide/303.png) NOTE: This is the server that the user signs onto as a visitor and already contains the updated information for the Authenticating VistA M Server in the REMOTE APPLICATION (#8994.5) file.

10. Press one of the connection buttons (e.g., TCP/IP Connect button).
11. Enter Access and Verify codes in the “VistA Sign-on” dialogue box when prompted.

![](xwb-1-1-73-developer-s-guide/304.png) NOTE: This authenticates the user against the Authenticating VistA M Server.

12. (optional) Choose your Division (i.e., Station Number) to log into, if prompted.
13. Press OK when presented with the dialogue in <u>Figure 78</u>:

> <span id="_Ref467597222" class="anchor"></span>Figure 77: Sample Kernel Authentication Token

> ![](xwb-1-1-73-developer-s-guide/305.png)

![](xwb-1-1-73-developer-s-guide/306.png) NOTE: <u>Figure 78</u> indicates that the Kernel Authentication Token was created, which means the user is now authenticated on the Authenticating VistA M Server.

14. After a few moments, you get the dialogue shown in <u>Figure 79</u> confirming the user is now also authenticated on the Remote VistA M Server as a visitor. Press OK when presented with the dialogue in <u>Figure 79</u>:

> <span id="_Ref467597265" class="anchor"></span>Figure 78: Sample Confirmation Message Indicating the User is Signed onto the Remote VistA M Server as a Visitor

> ![](xwb-1-1-73-developer-s-guide/307.png)

15. You can now enter an echo phrase to the Remote VistA M Server and get the string echoed back.

# Debugging and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Debugging and Troubleshooting Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Broker Development Kit (BDK) provides facilities for debugging and troubleshooting your VistA Graphical User Interface (GUI) applications.

- <u>How to Debug the Application</u>
- <u>RPC Error Trapping</u>
- <u>Broker Error Messages</u>
- <u>EBrokerError</u>
- <u>Testing the RPC Broker Connection</u>
- <u>Client Timeout and Buffer Clearing</u>
- <u>Memory Leaks</u>

![](xwb-1-1-73-developer-s-guide/308.png) REF: For commonly asked questions, see the RPC Broker FAQs on the RPC Broker VA Intranet site.

## How to Debug the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Control of debugging has been moved from the client to the server.

To start a debug session, do the following:

1.  On the VistA M Server, set initial breakpoints where desired.
42. On the client, follow instructions in the InterSystems Caché documentation on “Debugging with the Caché Debugger.” Set initial breakpoints where desired.
43. Start the following VistA M Server process:

\>D DEBUG^XWBTCPM

44. Enter a unique Listener port number (i.e., a port number *not* in general use).
45. Connect the client application to the server using the server’s IP address and the port number you entered in Step 4 and select OK.
46. You can now step through the code on your client, and simultaneously step through the code on the VistA M Server side for any RPCs that your client calls.

## RPC Error Trapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

M errors on the VistA M Server that occur during RPC execution are trapped by the use of M and Kernel error handling. In addition, the M error message is sent back to the Delphi client. Delphi raises an exception <u>EBrokerError</u> and a popup dialogue box displaying the error. At this point RPC execution terminates and the channel is closed.

In some instances, an application’s RPC could get a memory allocation error on the VistA M Server. Kernel does *not* trap these errors. However, these errors are trapped in the operating system’s error trap. For example, if an RPC receives or generates an abundance of data in local memory, the symbol table could be depleted resulting in a memory allocation error. To diagnose this problem, users should check the operating system’s error trap.

## Broker Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 38</u> list of errors/messages are Broker-specific and are *not* Winsock related:

<table>
<caption><blockquote>
<p><span id="_Toc82593704" class="anchor"></span>Table 39: Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC: Sample RPC Fields Returned and Label Information</p>
</blockquote></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 11%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>Error/Message</th>
<th>Name</th>
<th>Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Insufficient Heap</td>
<td>XWB_NO_HEAP</td>
<td>20001</td>
<td><p>This is a general error condition indicating insufficient memory. It can occur when an application allocates memory for a variable. This error occurs for some of the following reasons:</p>
<ul>
<li><p>Too many open applications.</p></li>
<li><p>Low physical memory.</p></li>
<li><p>Small virtual memory swap file (if dynamic, maybe low disk space).</p></li>
<li><p>User selecting too many records.</p></li>
</ul>
<p><strong>Resolution:</strong> Common solutions to this error include the following:</p>
<ul>
<li><p>Close some or all other applications.</p></li>
<li><p>Install more memory.</p></li>
<li><p>Increase the swap file size or, if dynamic, leave more free space on disk.</p></li>
<li><p>Try working with smaller data sets.</p></li>
<li><p>Reboot the workstation.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>M Error - Use ^XTER</td>
<td>XWB_M_REJECT</td>
<td>20002</td>
<td><p>The VistA M Server side of the application errored out. The Kernel error trap has recorded the error.</p>
<p><strong>Resolution:</strong> Examine the Kernel error trap for more information and specific corrective actions.</p></td>
</tr>
<tr class="odd">
<td>Signon was not completed</td>
<td>XWB_BadSignOn</td>
<td>20004</td>
<td><p>This error indicates the user did <em>not</em> successfully signon.</p>
<p><strong>Resolution:</strong> Either the Access and Verify codes were incorrect or the user clicked <strong>Cancel</strong> on the “VistA Sign-on” window.</p></td>
</tr>
<tr class="even">
<td>BrokerConnections list could not be created</td>
<td>XWB_BldConnectList</td>
<td>20005</td>
<td><p>This error is a specific symptom of a low memory condition.</p>
<p><strong>Resolution:</strong> For a detailed explanation and corrective measures, see the “Insufficient Heap” error message.</p></td>
</tr>
<tr class="odd">
<td>RpcVersion cannot be empty</td>
<td>XWB_NullRpcVer</td>
<td>20006</td>
<td><p>This error occurs when an RPC does <em>not</em> have an associated version number. Each RPC <em>must</em> have a version number.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>Server unable to read input data correctly</td>
<td>XWB_BadReads</td>
<td>20008</td>
<td><p>This error indicates that the format of the RPC input data was incorrect.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="odd">
<td>System was out of memory, executable file was corrupt, or relocations were invalid</td>
<td>XWB_ExeNoMem</td>
<td>20100</td>
<td><p>This error may indicate a low memory condition or may have errors in the application executable file.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>File was not found</td>
<td>XWB_ExeNoFile</td>
<td>20102</td>
<td><p>This error indicates that the referenced file could not be found.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="odd">
<td>Path was not found</td>
<td>XWB_ExeNoPath</td>
<td>20103</td>
<td><p>This error indicates that the referenced directory could not be found.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>Attempt was made to dynamically link to a task or there was a sharing or network-protection error</td>
<td>XWB_ExeShare</td>
<td>20105</td>
<td><p>This error most likely indicates network problems.</p>
<p><strong>Resolution:</strong> It may resolve itself over time. If not, contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="odd">
<td>Library required separate data segments for each task</td>
<td>XWB_ExeSepSeg</td>
<td>20106</td>
<td><p>This error indicates that the format of the RPC data was incorrect.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>There was insufficient memory to start the application</td>
<td>XWB_ExeLoMem</td>
<td>20108</td>
<td><p>This error is a specific symptom of a low memory condition.</p>
<p><strong>Resolution:</strong> For a detailed explanation and corrective measures, see the “Insufficient Heap” error message.</p></td>
</tr>
<tr class="odd">
<td>Windows version was incorrect</td>
<td>XWB_ExeWinVer</td>
<td>20110</td>
<td><p>This error indicates that the application was developed for a specific version of Windows and is not compatible with this system.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>Executable file was invalid. Either it was not a Windows application or there was an error in the EXE</td>
<td>XWB_ExeBadExe</td>
<td>20111</td>
<td><p>This error indicates a problem with the Windows executable application.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="odd">
<td>Application was designed for a different operating system</td>
<td>XWB_ExeDifOS</td>
<td>20112</td>
<td><p>This error indicates that the application is not compatible with this operating system.</p>
<p><strong>Resolution:</strong> Contact the developers responsible for the application software to take corrective action.</p></td>
</tr>
<tr class="even">
<td>Remote procedure not registered to application</td>
<td>XWB_RpcNotReg</td>
<td>20201</td>
<td><p>This error indicates the application attempted to execute an RPC that was <em>not</em> entered into the RPC Multiple field in the <u>REMOTE PROCEDURE (#8994) File</u> for this application.</p>
<p><strong>Resolution:</strong> The developers responsible for the application should be contacted.</p>
<p>As a “last resort” corrective measure, you can try to re-index the cross-reference on the RPC (#.01) field in the <u>REMOTE PROCEDURE (#8994) File</u> with the RPC (#320) field of the OPTION (#19) file. Ideally, this should only be attempted during off or low system usage.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc82593704" class="anchor"></span>Table 39: Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC: Sample RPC Fields Returned and Label Information

## EBrokerError

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>TRPCB Unit</u>

### Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EBrokerError is an exception raised by the <u>TRPCBroker Component</u>. This exception is raised when an error is encountered when communicating with the VistA M Server. You should use a try...except block around all server calls to handle any EbrokerError exceptions that may occur.

For example:

<span id="_Toc82593640" class="anchor"></span>Figure 79: Error Handling—EBrokerError Exception

try

brkrRPCBroker1.Connected:= True;

excepton EBrokerError dobegin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

end;

end;

![](xwb-1-1-73-developer-s-guide/309.png) REF: For descriptions/resolutions to specific error messages that can be displayed by EBrokerError, see the “<u>Broker Error Messages</u>” section.

## Testing the RPC Broker Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test the RPC Broker connection from your workstation to the VistA M Server, use the RPC Broker Diagnostic Program (i.e., RPCTEST.exe, distributed with patch XWB\*1.1\*47).

![](xwb-1-1-73-developer-s-guide/310.png) REF: For a complete description of the RPC Broker Diagnostic program, see Section 4, “Troubleshooting,” in the *RPC Broker Systems Management Guide*.

![](xwb-1-1-73-developer-s-guide/311.png) REF: For a demonstration/test using the Broker to connect to a VistA M Server, run the <u>RPC Broker Example (32-Bit)</u> (i.e., BrokerExample.exe); located in the following directory:

BDK32\Samples\BrokerEx

## Client Timeout and Buffer Clearing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a remote procedure call (RPC) fails to successfully complete due to a timeout on the client, the buffer on the VistA M Server contains data from the uncompleted call. Without special handling, this buffer on the server is returned whenever the next RPC is executed.

The solution to this problem is:

1.  The <u>RPCTimeLimit Property</u> on the <u>TRPCBroker Component</u> on the client helps avoid the problem in the first place.
47. In the event of a cancellation of a Network I/O operation, the Broker state on the client changes from NO FLUSH to FLUSH. When this state change occurs, the next RPC executed undergoes a READ operation prior to execution where any leftover incoming buffer is discarded. At the end of this operation, the Broker state on the client returns to NO FLUSH and the RPC executes normally. While the FLUSH state exists, users can experience a delay while the corrupted RPC data is discarded. The delay is proportional to the amount of data in the buffer.

## Memory Leaks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A good indication of a memory leak is when a running program is steadily decreasing the free pool of memory. As it runs or every time the program is started and stopped, free memory is steadily decreased.

Specifically, a program requests some bytes of memory from the Microsoft<sup>®</sup> Windows operating system (OS). When the OS provides it, it marks those bytes as taken. The free pool of memory (i.e., unmarked bytes) is decreased. When the program is finished with the memory, it should return the memory back to the OS by calling the FREE or DISPOSE functions. This allows the OS to clear the “taken” status of that memory; thereby, replenishing its free pool. When a developer forgets to free the memory after use or the program fails before it has a chance to execute the code that frees the memory, the memory is *not* reclaimed.

At all times, the program should keep track of which memory it is using. It does this by storing “Handles” (i.e., memory addresses of the beginning byte of each memory block). Later, when freeing memory, the Handle is used to indicate which memory address to free. If the variable that holds such a Handle is overwritten, there is no way to determine the Handle.

Nine out of ten times, memory leakage can be traced back to the application code that requests memory and then forgets to return it or *cannot* clean up after a crash.

As common with other professional-level languages (e.g., C/C++), Delphi has constructs that applications can use to:

1.  Request memory.
48. Type cast it.
49. Return it.

This requires developers to use their best judgement on how to best work with the system memory.

Avoiding memory leaks (and the often-subtle coding errors that lead to them) is a challenge for Delphi developers, especially for those whose main experience is working with M.

The insidious effect of these leaks (e.g., gobbling up 1K of memory each time that a certain event occurs) makes them difficult to detect with normal program testing. “Normal testing” means exercising all the possible paths through the code once, a difficult enough process in a Microsoft<sup>®</sup> Windows environment. Often, these leaks result in a symptom only under peculiar conditions (e.g., several other applications are running, reducing system resources), or only after extended use of the application (e.g., do you notice that Microsoft<sup>®</sup> Windows problems crop up in the afternoon, even though you were doing the same thing that morning?).

The most common symptom described is the following:

“The computer was working fine until the user installed the XYZ VistA software application on their PC. Now, it freezes up (gives an error message, says it is out of memory, etc.) all the time, even when the user is *not* using the XYZ package. No, the user *cannot* duplicate it, it just happens!”

One of the reasons that there is an extensive market for automated testing tools for Microsoft<sup>®</sup> Windows and client/server applications is that thorough testing is very difficult to do manually.

Fortunately, there are diagnostic products available for detecting code that cause memory leaks. It helps developers and code reviewers to find these leaks. Its use by people just starting out in Delphi development helps them identify the situations that cause memory leaks. This can serve as a good learning experience for new Delphi developers.

No application is immune from memory leaks, careful analysis of previous Broker code revealed some places where, under certain conditions, memory was *not* being released after it was used (i.e., memory leaks). These areas have been identified and corrected with RPC Broker 1.1.

# Tutorial

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Tutorial: Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The major functions of a <u>TRPCBroker Component</u> in a Delphi-based application are to:

- Connect to an RPC Broker VistA M Server system from a client.
- Execute remote procedure calls (RPCs) on that system.
- Return data results from RPC to the client.

This tutorial guides users through using a <u>TRPCBroker Component</u> to perform each of these tasks by having you create a Delphi-based application, step-by-step. This application retrieves a list of terminal types from the VistA M Server and displays information about each terminal type.

After you have completed this tutorial, you should be able to:

- Include a <u>TRPCBroker Component</u> in a Delphi-based application.
- Retrieve the end-user client workstation’s designated VistA M Server and port to connect.
- Establish a connection through the RPC Broker component to an RPC Broker VistA M Server.
- Create M routines that return data in the formats necessary to be called from RPCs.
- Create RPCs.
- Call RPCs from a Delphi-based application to retrieve data from VistA M database.
- Pass parameters from the Delphi-based application to RPCs.

### Tutorial Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Tutorial: Advanced Preparation</u>
- <u>Tutorial—Step 1: RPC Broker Component</u>
- <u>Tutorial—Step 2: Get Server/Port</u>
- <u>Tutorial—Step 3: Establish Broker Connection</u>
- <u>Tutorial—Step 4: Routine to List Terminal Types</u>
- <u>Tutorial—Step 5: RPC to List Terminal Types</u>
- <u>Tutorial—Step 6: Call ZxxxTT LIST RPC</u>
- <u>Tutorial—Step 7: Associating IENs</u>
- <u>Tutorial—Step 8: Routine to Retrieve Terminal Types</u>
- <u>Tutorial—Step 9: RPC to Retrieve Terminal Types</u>
- <u>Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC</u>
- <u>Tutorial—Step 11: Register RPCs</u>
- <u>Tutorial—Using VA FileMan Delphi Components (FMDC)</u>
- <u>Tutorial—Source Code (Sample)</u>

## Tutorial: Advanced Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Namespacing of Routines and RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each tutorial user should choose a unique namespace beginning with Z, concatenated with two or three other letters, for example ZYXU. Use this namespace as the beginning of the names for all routines and [RPCs](#rpcs_rpc_overview_htm) created during this tutorial. Using the unique namespace protects the system you are using from having existing routines and RPCs overwritten. This namespace is referred to as Z*xxx* during the tutorial.

### Tutorial Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use this tutorial:

- User should already have M programming skills, and some familiarity with Delphi and Object Pascal.
- User *must* have Delphi and the Broker Development Kit (BDK) installed on the workstation.
- The client workstation *must* have network access to an M account that is running a RPC Broker server process.
- Users *must* have programmer access in this M account, and it should be a Test account (*not* Production). Also, users need the [XUPROGMODE](#_Toc384285598) security key assigned to their user account.

## Tutorial—Step 1: RPC Broker Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step of this tutorial is to create a Delphi-based application that includes a <u>TRPCBroker Component</u>.

To create a Delphi-based application that includes a <u>TRPCBroker Component</u>, do the following:

1.  In Delphi, create a new application. Delphi creates a blank form, named Form1.
50. Set Form1’s Caption property to Terminal Type Display.
51. From the Kernel component palette tab, add a <u>TRPCBroker Component</u> to your form. The instance of the component is automatically named RPCBroker1. It should be renamed to brkrRPCBroker1.

![](xwb-1-1-73-developer-s-guide/312.png) NOTE: In general the name of the component can be any meaningful name that begins with “brkr” to indicate a <u>TRPCBroker Component</u>.

52. Leave the default values for Server and ListenerPort (see <u>Server Property</u> and <u>ListenerPort Property</u>) as is (they are retrieved from your workstation’s Registry). In Section <u>7.4</u> you will add code to retrieve these values at run-time from the workstation’s Registry.
53. Set the <u>ClearParameters Property</u> and <u>ClearResults Property</u> to True if they are not set to True already. This ensures that each time a call to an [RPC](#rpcs_rpc_overview_htm) is made, the <u>Results Property</u> is cleared beforehand, and the <u>Param Property</u> is cleared afterwards.
54. Your form should look like <u>Figure 81</u>:

> <span id="_Ref385267129" class="anchor"></span>Figure 80: Tutorial—Step 1: RPC Broker Component: Sample Form Output

![](xwb-1-1-73-developer-s-guide/313.png)

The next tasks are to use the <u>TRPCBroker Component</u> to retrieve the client workstation’s RPC Broker server and port information (<u>Tutorial—Step 2: Get Server/Port</u>), and then to establish a connection through the <u>TRPCBroker Component</u> to the VistA M Server (<u>Tutorial—Step 3: Establish Broker Connection</u>).

## Tutorial—Step 2: Get Server/Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>TRPCBroker Component</u> added to your form is hard-coded to access the Broker server and listener port that it picks up from the (developer) workstation (by default, BROKERSERVER and \<REDACTED\>). Naturally, you do *not* want this to be the only server and port to which your application can connect. To retrieve the end-user workstation’s designated Broker server and port to connect, as stored in their Registry, you can use the <u>GetServerInfo Function</u>.

To retrieve the end-user workstation’s designated server and port, do the following:

1.  Include the <u>RPCConf1 Unit</u> in the Pascal file’s uses clause. This is the unit of which [<u>GetServerInfo Function</u>](#other_api_otherapi_getserverinfo_4192) is a part.
55. Double-click on a blank region of the form. This creates an event handler procedure, TForm1.FormCreate, in the Pascal source code.
56. Add code to the FormCreate event handler that retrieves the correct server and port to connect, using the <u>GetServerInfo Function</u>. If mrCancel is returned, the code should quit. Otherwise, the code should then set brkrRPCBroker1’s <u>Server Property</u> and <u>ListenerPort Property</u> to the returned values.

The code should look like <u>Figure 82</u>:

<span id="_Ref446334711" class="anchor"></span>Figure 81: Tutorial—Step 2: Get Server/Port: Example

procedure TForm1.FormCreate(Sender: TObject);

var

ServerStr: String;

PortStr: String;

begin

*// Get the correct port and server from the Registry.*if GetServerInfo(ServerStr,PortStr)\<\> mrCancel thenbegin

brkrRPCBroker1.Server:=ServerStr;

brkrRPCBroker1.ListenerPort:=StrToInt(PortStr);

*{connectOK}*endelse

Application.Terminate;

end;

57. Now that you have code to retrieve the appropriate RPC Broker server and listener port, the next step of the tutorial (<u>Tutorial—Step 3: Establish Broker Connection</u>) is for the application to use the <u>TRPCBroker Component</u> to establish a connection to the VistA M Server.

## Tutorial—Step 3: Establish Broker Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that the application can determine the appropriate RPC Broker server and port to connect (<u>Tutorial—Step 2: Get Server/Port</u>), add code to establish a connection to the designated RPC Broker server from the application. The act of establishing a connection leads the user through signon. If signon succeeds, a connection is established.

To establish a connection from the application to a RPC Broker server, do the following:

1.  Add code to Form1’s OnCreate event handler. The code should:
1.  Set brkrRPCBroker1’s <u>Connected Property</u> to True (inside of an exception handler try...except block). This causes an attempt to connect to the RPC Broker server.
16. Check if an <u>EBrokerError</u> exception is raised. If this happens, connection failed, and the code should inform the user of this and terminate the application.

The OnCreate event handler should now look like <u>Figure 83</u>:

<span id="_Ref446334787" class="anchor"></span>Figure 82: Tutorial—Step 3: Establish Broker Connection: Example

procedure TForm1.FormCreate(Sender: TObject);

var

ServerStr: String;

PortStr: String;

begin

*// Get the correct port and server from the Registry.*if GetServerInfo(ServerStr,PortStr)\<\> mrCancel then

*{connectOK begin}*

begin

brkrRPCBroker1.Server:=ServerStr;

brkrRPCBroker1.ListenerPort:=StrToInt(PortStr);

*// Establish a connection to the RPC Broker server.*try

brkrRPCBroker1.Connected:=True;

exceptOn EBrokerError do

*{error begin}*begin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

*{error end}*end;

*{try end}*end;

*{connectOK end}*endelse

Application.Terminate;

end;

![](xwb-1-1-73-developer-s-guide/314.png) NOTE: Every call that invokes an RPC Broker server connection should be done in an “exception handler” try...except block, so that <u>EBrokerError</u> exceptions can be trapped.

58. Save, compile and run the application. It should connect to the VistA M Server returned by the <u>GetServerInfo Function</u>. You may be prompted to sign on with 2-factor authentication (2FA) or Access and Verify codes. If you can connect successfully, the application runs (at this point, it is just a blank form). Otherwise, troubleshoot the RPC Broker connection until the application connects.
59. If the server system defined in the Registry is *not* the development system (the one on which RPCs are created for this application), update the Registry using the ServerList.exe program so that the application connects to the proper VistA M Server.
60. Now that the application can establish a connection to the end-user’s server system, you can retrieve data from the VistA M Server.

The next steps of the tutorial create a custom RPC that retrieves a list of all of the terminal types on the VistA M Server and calls that RPC from the application.

## Tutorial—Step 4: Routine to List Terminal Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that the application uses an RPC Broker component to connect correctly to an RPC Broker server (<u>Tutorial—Step 3: Establish Broker Connection</u>), you are ready to create custom RPCs that the application can call. For the tutorial, you will create an RPC that retrieves the list of all terminal types from the RPC Broker server.

The first step in creating an RPC is to create the routine that the RPC executes. You *must* create its input and output in a defined format that is compatible with being executed as an RPC.

To create the routine that the RPC executes, do the following:

1.  Choose the data format that the RPC should return. The type of data needed to return to the client application determines the format of the routine that the RPC calls. There are five return value types for RPCs:
- SINGLE VALUE
- ARRAY
- WORD PROCESSING
- GLOBAL ARRAY
- GLOBAL INSTANCE

Since the type of data the tutorial application would like returned is a list of terminal types, and that list could be quite long, use a return value type GLOBAL ARRAY for the RPC. For the routine called by the RPC, this means that:

- The routine should return a list of terminal types in a global. Each terminal type should be on an individual data node, subscripted numerically.
- The return value of the routine (always returned in the routine’s first parameter) should be the global reference of the data global, in closed root form. The data nodes should be one level descendant from the global reference.
61. In the M account that the <u>TRPCBroker Component</u> connects to, create a routine that outputs a list of terminal types in the format determined above. The format for each data node that is returned for a terminal type could be anything; for the sake of this application, set each data node to “ien^.01 field” for the terminal type in question. Store each node in ^TMP(\$J,”ZxxxTT”,#), as shown in <u>Figure 84</u>.

> <span id="_Ref446334997" class="anchor"></span>Figure 83: Tutorial—Step 4: Routine to List Terminal Types: Example

ZxxxTT ;ISC-SF/KC TUTORIAL RTN, BRK 1.1; 7/22/97

 ;;1.0;;

TERMLIST(GLOBREF) ; *retrieve list of term types*

 ; *return list in ^TMP(\$J,”ZxxxTT”)*

 ; *format of returned results: ien^.01 field*

 N %                                         ;   *scratch variable*

 K ^TMP(\$J,”ZxxxTT”)              ;   *clear data return area *D LIST^DIC(3.2)                       ;   *retrieve list of termtype entries *; *now set termtype entries into data global*

 I ‘\$D(DIERR) D

 .S %=0 F S %=\$O(^TMP(“DILIST”,\$J,2,%)) Q:%=“” D

 ..S ^TMP(\$J,”ZxxxTT”,%)=\$G(^TMP(“DILIST”,\$J,2,%))\_“^”\_\$G(^TMP(“DILIST”,\$J,1,%))

 K ^TMP(“DILIST”,\$J)                              ; *clean up *S GLOBREF=\$NA(^TMP(\$J,“ZxxxTT”))  ; *set return value*

 Q

62. Test the routine. Call it like the Broker would:

\> D TERMLIST^ZxxxTT(.RESULT)

1.  Confirm that the return value is the correct global reference:

\> W RESULT

^TMP(566363396,”ZxxxTT”)

17. Confirm that the data set into the global is in the format shown in <u>Figure 85</u>:

> <span id="_Ref446334865" class="anchor"></span>Figure 84: Tutorial—Step 4: Routine to List Terminal Types: Example confirming global data format

^TMP(566347920,“ZxxxTT”,1) = 1^C-3101

^TMP(566347920,“ZxxxTT”,2) = 2^C-ADDS

^TMP(566347920,“ZxxxTT”,3) = 3^C-ADM3

^TMP(566347920,“ZxxxTT”,4) = 38^C-DATAMEDIA

^TMP(566347920,“ZxxxTT”,5) = 106^C-DATATREE

^TMP(566347920,“ZxxxTT”,6) = 4^C-DEC

^TMP(566347920,“ZxxxTT”,7) = 5^C-DEC132

^TMP(566347920,“ZxxxTT”,8) = 93^C-FALCO

^TMP(566347920,“ZxxxTT”,9) = 6^C-H1500

^TMP(566347920,“ZxxxTT”,10) = 103^C-HINQLINK

^TMP(566347920,“ZxxxTT”,11) = 132^C-HINQLINK

^TMP(566347920,“ZxxxTT”,12) = 63^C-HP110

^TMP(566347920,“ZxxxTT”,13) = 34^C-HP2621

63. Once you have tested the routine, and confirmed that it returns data correctly, the next step (<u>Tutorial—Step 5: RPC to List Terminal Types</u>) is to create the RPC that calls this routine.

## Tutorial—Step 5: RPC to List Terminal Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that you have created an RPC-compatible routine to list terminal types (<u>Tutorial—Step 4: Routine to List Terminal Types</u>), you can go ahead and create the RPC itself \[the entry in the <u>REMOTE PROCEDURE (#8994) File</u>\] that calls the routine.

To create an RPC that uses the TERMLIST^ZxxxTT routine, do the following:

1.  Using VA FileMan, create a new RPC entry in the <u>REMOTE PROCEDURE (#8994) File</u>. Set up the RPC as shown in <u>Figure 86</u>:

<span id="_Ref446335048" class="anchor"></span>Figure 85: Tutorial—Step 5: RPC to List Terminal Types: Example

> NAME: ZxxxTT LIST

> TAG: TERMLIST

> ROUTINE: ZxxxTT

> RETURN VALUE TYPE: GLOBAL ARRAY

> WORD WRAP ON: TRUE

> DESCRIPTION: Used in RPC Broker developer tutorial.

64. The RPC’s RETURN VALUE TYPE is set to GLOBAL ARRAY. This means that the RPC expects a return value that is a global reference (with data stored at that global reference).
65. Also, the RPC’s WORD WRAP ON is set to TRUE. This means each data node from the VistA M Server is returned as a single node in the <u>Results Property</u> of the <u>TRPCBroker Component</u> in Delphi. Otherwise, the data would be returned concatenated into a single node in the <u>Results Property</u>.
66. The next step of the tutorial (<u>Tutorial—Step 6: Call ZxxxTT LIST RPC</u>) is to call this RPC from the tutorial application, through its <u>TRPCBroker Component</u>.

## Tutorial—Step 6: Call ZxxxTT LIST RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have created and tested the ZxxxTT LIST RPC on the VistA M Server, use the Delphi-based application’s <u>TRPCBroker Component</u> to call that RPC.

To call the ZxxxTT LIST RPC from the Delphi-based application to populate a list box, do the following:

1.  Place a TListBox component on the form. It should be automatically named ListBox1.  
      
    Size it so that it uses the full width of the form, and half of the form’s height.
67. Place a button beneath ListBox1:
- Set its caption to “Retrieve Terminal Types”.
- Size the button so that it is larger than its caption.
68. Double-click on the button. This creates an event handler procedure, TForm1.Button1Click, in the Pascal source code.
69. In the TForm1.Button1Click event handler, add code to call the ZxxxTT LIST RPC and populate the list box with the retrieved list of terminal type entries. This code should:
1.  Set RCPBroker1’s <u>RemoteProcedure Property</u> to ZxxxTT LIST.
18. Call brkrRPCBroker1’s <u>Call Method</u> (in a try...except exception handler block) to invoke that RPC.
19. Retrieve results from brkrRPCBroker1’s <u>Results Property</u>, setting them one-by-one into the list box’s Items property.

This code should look like the code in <u>Figure 87</u>:

<span id="_Ref446335096" class="anchor"></span>Figure 86: Tutorial—Step 6: Call ZxxxTT LIST RPC: Example

Procedure TForm1.Button1Click(Sender: TObject);

var

i: integer;

begin

brkrRPCBroker1.RemoteProcedure:=‘ZxxxTT LIST’;

try

*{call begin}*begin

brkrRPCBroker1.Call;

ListBox1.Clear;

for i:=0 to (brkrRPCBroker1.Results.Count-1) do

ListBox1.Items.Add(piece(brkrRPCBroker1.Results\[i\],‘^’,2));

*{call end}*end;

exceptOn EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

*{try end}*end;

end;

70. Include the mfunstr unit in the Uses clause of the project’s Pascal source file. This enables the application to use the piece function included in mfunstr (see the “<u>XWB IM HERE</u>” section).
71. The user account *must* have [XUPROGMODE](#_Toc384285598) security key assigned. This allows the application to execute any RPC, without the RPC being registered. Later in the tutorial you will register your RPCs.
72. Run the application and click Retrieve Terminal Types. It should retrieve and display terminal type entries, and appear as shown in <u>Figure 88</u>:

<span id="_Ref385267423" class="anchor"></span>Figure 87: Tutorial—Step 6: Call ZxxxTT LIST RPC: Sample Output Form

![](xwb-1-1-73-developer-s-guide/315.png)

73. Now that you can retrieve a list of terminal type entries, the next logical task is to retrieve a particular entry when a user selects that entry in the list box.

## Tutorial—Step 7: Associating IENs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user selects a terminal type entry in the list box, a typical action is to retrieve the corresponding record and display its fields. The key to retrieving any VA FileMan record is knowing the IEN of the record. Thus, when a user selects an entry in the list box, you need to know the IEN of the corresponding VA FileMan entry. However, the list box items themselves only contain the name of each entry, not the IEN.

The subscripting of items in the list box still matches the original subscripting of items returned in brkrRPCBroker1’s <u>Results Property</u>, as performed by the following code in Button1Click event handler:

for i:=0 to (brkrRPCBroker1.Results.Count-1) do

ListBox1.Items.Add(piece(brkrRPCBroker1.Results\[i\],’^’,2));

If no further calls to brkrRPCBroker1 were made, you could simply refer back to brkrRPCBroker1’s Results\[x\] item to obtain the matching IEN of a list boxes’ Items\[x\] item. But, since brkrRPCBroker1 is used again, the <u>Results Property</u> is cleared. So, the results *must* be saved off in another location, if you want to be able to refer to them after other Broker calls are made.

To save off the Results to another location, do the following:

1.  Create a variable named TermTypeList, of type TStrings. This is where brkrRPCBroker1.Results is saved. Create the variable in the section of code where TForm1 is defined as a class:

> <span id="_Toc82593649" class="anchor"></span>Figure 88: Tutorial—Step 7: Associating IENs: Example of Creating a Variable to Save Results

type

TForm1 = class(TForm)

brkrRPCBroker1: TRPCBroker;

ListBox1: TListBox;

Button1: TButton;

procedure FormCreate(Sender: TObject);

procedure Button1Click(Sender: TObject);

private

*{Private declarations}*

public

*{Public declarations}// Added declaration of TermTypeList.*

TermTypeList: TStringList;

end;

74. In Form1’s OnCreate event handler, call the Create method to initialize the TermTypeList. Do this in the first line of code of the event handler:

TermTypeList:=TStringList.Create;

75. Create an event handler for Form1’s OnDestroy event (select Form1, go to the Events tab of the Object Inspector, and double-click on the right-hand column for the OnDestroy event). In that event handler, add one line of code to call the Free method for TermTypeList. This frees the memory used by the list:

> <span id="_Toc82593650" class="anchor"></span>Figure 89: Tutorial—Step 7: Associating IENs: Example of Creating an Event Handler to Free Memory

procedure TForm1.FormDestroy(Sender: TObject);

begin

TermTypeList.Free;

end;

76. In Button1’s OnClick event handler, add a line of code to populate TermTypeList with the list of terminal types returned in brkrRPCBroker1’s <u>Results Property</u>. This code uses the Add method of TStrings sequentially so that the subscripting of TermTypeList matches the subscripting of Results. The code for that event handler should then look like <u>Figure 91</u>:

> <span id="_Ref446337022" class="anchor"></span>Figure 90: Tutorial—Step 7: Associating IENs: Example of Creating an Event Handler to Populate a List of Terminal Types

procedure TForm1.Button1Click(Sender: TObject);

var

i: integer;

begin

brkrRPCBroker1.RemoteProcedure:=‘Zxxx LIST’;

try

*{call begin}*begin

brkrRPCBroker1.Call;

for i:=0 (brkrRPCBroker1.Results.Count-1) do begin *{copy begin}*

ListBox1.Items.Add(piece(brkrRPCBroker1.Results\[i\],‘^’,2));

*// Added line.*

TermTypeList.Add(brkrRPCBroker1.Results\[i\]);

*{copy end}*end;

{call end}

end;

exceptOn EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

*{try end}*end;

end;

77. Determine (and display) the IEN of the corresponding terminal type when a user selects an item in the list box:
1.  Create an OnClick event handler for ListBox1 by double-clicking on the list box.
20. Add code to the new event handler that checks if an item is selected. If an item is selected in the list box, display the first piece of the corresponding item saved off in the TermTypeList array (the index subscripts of TermTypeList and of the list box match each other). This is the IEN of the corresponding VA FileMan entry.

> <span id="_Toc82593652" class="anchor"></span>Figure 91: Tutorial—Step 7: Associating IENs: Example of Creating an Event Handler to Check if an Item is Selected

procedure TForm1.ListBox1Click(Sender: TObject);

var

ien: String;

beginif (ListBox1.ItemIndex \<\> -1) then

*{displayitem begin}*begin

ien:=piece(TermTypeList\[ListBox1.ItemIndex\],’^’,1);

ShowMessage(ien);

*{displayitem end}*end;

end;

78. Compile and run the application. When you click on an item in the list box, the IEN corresponding to that item should be displayed in a popup message window.
79. Now that you can determine the IEN of any entry the user selects in the list box, you can retrieve and display the corresponding VA FileMan record for any selected list box entry.

## Tutorial—Step 8: Routine to Retrieve Terminal Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that you have associated an IEN for each record displayed in the list box (<u>Tutorial—Step 7: Associating IENs</u>), you can use that IEN to display fields from any terminal type entry in the list box that a user selects. To retrieve the fields for any selected terminal type entry, create a second custom RPC. This RPC needs to take an input parameter, the record IEN, to know which record to retrieve.

To create an RPC routine to retrieve individual terminal type records, do the following:

1.  Choose the data format that the RPC should return. The type of data needed to return to the client application determines the format of the routine that the RPC calls. In this case, the RPC should, given an IEN, return fields .01, 1, 2, 3, 4, 6, and 7 (Name, Right Margin, Form Feed, Page Length, Back Space, Open Execute, and Close Execute).  
      
    Since this information is constrained and small, a return type of ARRAY would be suitable for this RPC. The return format of the array is arbitrary; for the sake of this application, the routine should return fields .01, 1, 2, 3, and 4 in node 0; field 6 (a 245-character field) in node 1; and field 7 (also a 245-character field) in node 2. This array *must* be returned in the first parameter to the routine.
80. The routine for this RPC also needs to be able to take an IEN as an input parameter. Any additional input parameters, such as one for the IEN, *must follow* the required input parameter in which results are returned.
81. Add a second subroutine to the ZxxxTT routine for the second RPC, similar to <u>Figure 93</u>. This subroutine uses an IEN to retrieve fields for a particular terminal type. It then sets three result nodes, each containing a specified set of fields for the record corresponding to the IEN parameter.

> <span id="_Ref446337027" class="anchor"></span>Figure 92: Tutorial—Step 8: Routine to Retrieve Terminal Types: Example of a Subroutine to Retrieve Fields for a Particular Terminal Type and Set Result Nodes

TERMENT(RESULT,IEN) ; retrieve a string of fields for a termtype

 ; format of results (by field number):

 ; RESULT(0)=.01^1^2^3^4

 ; RESULT(1)=6

 ; RESULT(2)=7

 ;

 N I,ARRAY S IEN=IEN\_“,”,RESULT(1)=“”

 D GETS^DIQ(3.2,IEN,“.01;1;2;3;4;6;7”,“”,“ARRAY”)

 S RESULT(0)=“”

I ‘\$D(DIERR) D

.F I=.01,1,2,3,4 D

 ..S RESULT(0)=RESULT(0)\_ARRAY(3.2,IEN,I)\_“^”

 .S RESULT(1)=ARRAY(3.2,IEN,6)

 .S RESULT(2)=ARRAY(3.2,IEN,7)

 Q

82. Test the routine. Call it like the Broker would:

\>D TERMENT^Z*xxx*TT(.ARRAY,103)

83. Confirm that the return array contains the specified fields in the nodes shown in <u>Figure 94</u>:

> <span id="_Ref446337030" class="anchor"></span>Figure 93: Tutorial—Step 8: Routine to Retrieve Terminal Types: Example Confirming Returned Array Contains the Specified Fields

ARRAY(0)=C-HINQLINK^80^#,\$C(27,91,50,74,27,91,72)^24^\$C(8)^

ARRAY(1)=U \$I:(0:255::255:512)

ARRAY(2)=U \$I:(:::::512) C \$I

84. Once you have tested the routine, and confirmed that it returns data correctly, the next step (<u>Tutorial—Step 9: RPC to Retrieve Terminal</u> Types) is to create the RPC that calls this routine.

## Tutorial—Step 9: RPC to Retrieve Terminal Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that you have created an RPC-compatible routine to retrieve fields from a terminal type record (<u>Tutorial—Step 8: Routine to Retrieve Terminal Types</u>), create the RPC itself.

To create an RPC that uses the TERMENT^ZxxxTT routine, do the following:

1.  Using VA FileMan, create a new RPC entry in the <u>REMOTE PROCEDURE (#8994) File</u>. Set up the RPC as shown in <u>Figure 95</u>:

> <span id="_Ref446337031" class="anchor"></span>Figure 94: Tutorial—Step 9: RPC to Retrieve Terminal Types: Example of an RPC Setup

NAME: ZxxxTT RETRIEVE

TAG: TERMENT

ROUTINE: ZxxxTT

RETURN VALUE TYPE: ARRAY

DESCRIPTION: Used in RPC Broker tutorial.

INPUT PARAMETER: IEN PARAMETER TYPE: LITERAL

85. The RPC’s RETURN VALUE TYPE is set to ARRAY. This means that the RPC expects a return value that contains results nodes, each subscripted only at the first subscript level.
86. The WORD WRAP ON setting does *not* affect RPCs whose RETURN VALUE TYPE is ARRAY.
87. The additional input parameter needed to pass in a record IEN is documented in the INPUT PARAMETER Multiple. Its parameter type is LITERAL, which is appropriate when being passed the numeric value of an IEN.
88. This RPC can now be called from a Delphi-based application, through the <u>TRPCBroker Component</u>.

## Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user selects a terminal type entry in the list box, the OnClick event is triggered. The ZxxxTT RETRIEVE RPC can be called from that OnClick event, as a replacement for the code there that simply displays the IEN of any selected record.

To use the ZxxxTT RETRIEVE RPC to display fields from a selected terminal type, do the following:

1.  Create labels and edit boxes for each of the fields the RPC returns from the Terminal type file:

| Terminal Type Field: | Add a TEdit component named: | Add a Label with the Caption: |
|----------------------|------------------------------|-------------------------------|
| .01                  | Name                         | Name                          |
| 1                    | RightMargin                  | Right Margin:                 |
| 2                    | FormFeed                     | Form Feed:                    |
| 3                    | PageLength                   | Page Length:                  |
| 4                    | BackSpace                    | Back Space:                   |
| 6                    | OpenExecute                  | Open Execute:                 |
| 7                    | CloseExecute                 | Close Execute:                |

<span id="_Ref384114351" class="anchor"></span>Table 40: DLL Exported Functions

89. Update ListBox1’s OnClick event handler. Add code so that when the user clicks on an entry in the list box, the application calls the ZxxxTT RETRIEVE RPC to retrieve fields for the corresponding terminal type and displays those fields in the set of TEdit controls on the form. This code should:
1.  Set RCPBroker1’s <u>RemoteProcedure Property</u> to ZxxxTT RETRIEVE.
21. Pass the IEN of the selected terminal type to the RPC, using the <u>TRPCBroker Component</u>’s RunTime <u>Param Property</u>. Pass the IEN in the <u>Value Property</u> (i.e., brkrRPCBroker1.Param\[0\].Value).
22. Pass the PType for the IEN parameter in the brkrRPCBroker1.Param\[0\].PType. Possible types are literal, reference, and list. In this case, to pass in an IEN, the appropriate PType is literal.
23. Call brkrRPCBroker1’s <u>Call Method</u> (in a try...except exception handler block) to invoke the ZxxxTT RETRIEVE RPC.
24. Set the appropriate pieces from each of the three Results nodes into each of the TEdit boxes corresponding to each returned field.

The code for the OnClick event handler should look like <u>Figure 96</u>:

> <span id="_Ref446337036" class="anchor"></span>Figure 95: Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC: Sample of an OnClick Event Handler

procedure TForm1.ListBox1Click(Sender: TObject);

var

ien: String;

beginif (ListBox1.ItemIndex \<\> -1) then

*{displayitem begin}*begin

ien:=piece(TermTypeList\[ListBox1.ItemIndex\],‘^’,1);

brkrRPCBroker1.RemoteProcedure:=‘ZxxxTT RETRIEVE’;

brkrRPCBroker1.Param\[0\].Value := ien;

brkrRPCBroker1.Param\[0\].PType := literal;

try

*{call code begin}*begin

brkrRPCBroker1.Call;

Name.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,1);

RightMargin.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,2);

FormFeed.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,3);

PageLength.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,4);

BackSpace.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,5);

OpenExecute.Text:=brkrRPCBroker1.Results\[1\];

CloseExecute.Text:=brkrRPCBroker1.Results\[2\];

*{call code end}*end;

exceptOn EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

*{try end}*end;

*{displayitem end}*end;

end;

90. Compile and run the application. When you click on an entry in the list box now, the corresponding fields should be retrieved and displayed in the set of edit boxes on your form, as shown in <u>Figure 97</u>:

> <span id="_Ref385267742" class="anchor"></span>Figure 96: Tutorial—Step 10: Call ZxxxTT RETRIEVE RPC: Testing the Application

> ![](xwb-1-1-73-developer-s-guide/316.png)

## Tutorial—Step 11: Register RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Up until now, it has been assumed that the only user of the application is you, and that you have programmer access and the [XUPROGMODE](#_Toc384285598) security key in the account where the RPCs are accessed.

Under any other circumstance, any RPCs that the application uses *must* be registered for use by the application on the host system. Registration authorizes the RPCs for use by the client based on user privileges.

To register the RPCs used by the tutorial application, do the following:

1.  Create an option of type “B” (Broker). For example, create an option called ZxxxTT TERMTYPE for the tutorial application.
91. In the “B”-type option’s RPC multiple, make one entry for each RPC the application calls. In the case of this tutorial, there should be two entries:
- ZxxxTT LIST
- ZxxxTT RETRIEVE
92. Follow the steps in the “<u>RPC Security: How to Register an RPC</u>” section to create an application context, using the ZxxxTT TERMTYPE option.

Essentially, add a line of code that calls the <u>CreateContext Method</u>, and terminates the application if False is returned. The code for Form1’s OnCreate event should now look like <u>Figure 98</u>:

<span id="_Ref446337041" class="anchor"></span>Figure 97: Tutorial—Step 11: Register RPCs: Example

procedure TForm1.FormCreate(Sender: TObject);

var

ServerStr: String;

PortStr: String;

begin

TermTypeList:=TStringList.Create;

*// Get the correct port and server from Registry.*if GetServerInfo(ServerStr,PortStr)\<\> mrCancel then

*{connectOK begin}*begin

brkrRPCBroker1.Server:=ServerStr;

brkrRPCBroker1.ListenerPort:=StrToInt(PortStr);

*// Establish a connection to the RPC Broker server.*try

brkrRPCBroker1.Connected:=True;

*// Check security.*if not brkrRPCBroker1.CreateContext(‘ZxxxTT TERMTYPE’) then

Application.Terminate;

exceptOn EBrokerError do

*{error begin}*begin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

*{error end}*end;

*{try end}*end;

*{connectOK end}*endelse

Application.Terminate;

end;

93. Compile and run the application. Try running it both with and without the [XUPROGMODE](#_Toc384285598) security key assigned to you. Without the [XUPROGMODE](#_Toc384285598) security key, you are *not* able to run the application unless the ZxxxTT TERMTYPE option is assigned to your menu tree.

## Tutorial—Using VA FileMan Delphi Components (FMDC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Congratulations! You have created a sample application that performs entry lookup and retrieves fields from any record selected by the end-user. You are now ready to create Delphi-based applications using the RPC Broker.

If the application needs to perform database tasks with VA FileMan on a VistA M Server, consider using the FileMan Delphi Components (FMDC). These components automate the major tasks of working with database records through Delphi. Among the functions they provide are:

- Automated entry retrieval into a set of controls.
- Automated online help for database fields.
- Automated validation of user data entry.
- Automated filing of changed data.
- IEN tracking in all controls.
- Automated DBS error tracking on the Delphi client.
- Generic lookup dialogue.
- Record locking.
- Record deletion.

If you need to do more than the most simple database tasks in your Delphi-based applications, the FileMan Delphi Components (FMDC) encapsulate most of the coding needed to retrieve, validate, and file VA FileMan data.

![](xwb-1-1-73-developer-s-guide/317.png) REF: For more information on the VA FileMan Delphi Components (FMDC), see the FMDC VA Intranet website.

## Tutorial—Source Code (Sample)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc82593659" class="anchor"></span>Figure 98: Tutorial Source Code

unit tut1;

interface

Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs, Trpcb, RPCConf1, StdCtrls, MFunStr;

type

TForm1 = class(TForm)

brkrRPCBroker1: TRPCBroker;

ListBox1: TListBox;

Button1: TButton;

Name: TEdit;

RightMargin: TEdit;

FormFeed: TEdit;

OpenExecute: TEdit;

CloseExecute: TEdit;

PageLength: TEdit;

BackSpace: TEdit;

Label1: TLabel;

Label2: TLabel;

Label3: TLabel;

Label4: TLabel;

Label5: TLabel;

Label6: TLabel;

Label7: TLabel;

procedure FormCreate(Sender: TObject);

procedure Button1Click(Sender: TObject);

procedure ListBox1Click(Sender: TObject);

procedure FormDestroy(Sender: TObject);

private

*{Private declarations}*public

*{Public declarations}// Added declaration of TermTypeList.*

TermTypeList: TStrings;

end;

var

Form1: TForm1;

implementation

*{\$R \*.DFM}*procedure TForm1.FormCreate(Sender: TObject);

var

ServerStr: String;

PortStr: String;

begin

TermTypeList:=TStringList.Create;

*// Get the correct port and server from the Registry*.

if GetServerInfo(ServerStr,PortStr)\<\> mrCancel then

*{connectOK begin}*begin

brkrRPCBroker1.Server:=ServerStr;

brkrRPCBroker1.ListenerPort:=StrToInt(PortStr);

*// Establish a connection to the RPC Broker server.*try

brkrRPCBroker1.Connected:=True;

if not brkrRPCBroker1.CreateContext(‘ZxxxTT TERMTYPE’) then

Application.Terminate;

exceptOn EBrokerError do

*{error begin}*begin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

*{error end}*end;

*{try end}*end;

*{connectOK end}*endelse

Application.Terminate;

end;

procedure TForm1.Button1Click(Sender: TObject);

var

i: integer

brkrRPCBroker1.RemoteProcedure:=‘ZxxxTT LIST’;

try

*{call begin}*begin

brkrRPCBroker1.Call;

for i:=0 to (brkrRPCBroker1.Results.Count-1) do begin  *{copy begin}*

ListBox1.Items.Add(piece(brkrRPCBroker1.Results\[i\],‘^’,2));

*// Added line.*

TermTypeList.Add(brkrRPCBroker1.Results\[i\]);

*{copy end}*end;

*{call end}*end;

exceptOn EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

{try end}beginend;

end;

procedure TForm1.ListBox1Click(Sender: TObject);

var

ien: String;

beginif (ListBox1.ItemIndex \<\> -1) then

*{displayitem begin}*begin

ien:=piece(TermTypeList\[ListBox1.ItemIndex\],‘^’,1);

brkrRPCBroker1.RemoteProcedure:=‘ZxxxTT RETRIEVE’;

brkrRPCBroker1.Param\[0\].Value := ien;

brkrRPCBroker1.Param\[0\].PType := literal;

try

*{call code begin}*begin

brkrRPCBroker1.Call;

Name.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,1);

RightMargin.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,2);

FormFeed.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,3);

PageLength.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,4);

BackSpace.Text:=piece(brkrRPCBroker1.Results\[0\],‘^’,5);

CloseExecute.Text:=brkrRPCBroker1.Results\[2\];

*{call code end}*end;

exceptOn EBrokerError do

ShowMessage(‘A problem was encountered communicating with the server.’);

*{try end}*end;

*{displayitem end}*end;

end;

procedure TForm1.FormDestroy(Sender: TObject);

begin

TermTypeList.Free;

end;end.

## Silent Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker provides “Silent Login” capability. Silent Login is a way to log in a user with known login information. Silent Login skips the step of asking the user for login information. It provides functionality associated with the ability to make logins to a VistA M Server without the RPC Broker asking for Access and Verify code information.

![](xwb-1-1-73-developer-s-guide/318.png) REF: For some examples, see the “<u>Silent Login Examples</u>” section.

There are three types of Silent Login provided with the RPC Broker 1.1 BDK:

- Access/Verify Code—Type of Silent Login that uses Access and Verify codes provided by the application. This type of Silent Login may be necessary for an application that runs as a background task and repeatedly signs on for short periods. Another case would be for applications that are interactive with the user but are running under conditions where they *cannot* provide a standard dialogue window, such as that used by the Broker to request Access and Verify codes. Examples might be applications running on handheld devices or within a browser window.
- CCOW Token—Type of Silent Login that uses a CCOW “User Context” token that is passed for authentication.
- Auto Sign-On (ASO) Token—Type of Silent Login that uses an ASO token obtained by one application that is passed along with other information as a command line argument to a second application that it is starting. The token is obtained from the VistA server and remains valid for about twenty (20) seconds. When the newly started application sends this token during login the server identifies the same user and completes the login.

Due to the various conditions under which Silent Logins might be used, it was also necessary to provide options to the applications on error handling and processing. Applications that run as system services crash if they attempt to show a dialogue box. Similarly, applications running within Web browsers are *not* permitted to show a dialogue box or to accept Windows messages. Properties have been provided to permit the application to handle errors in a number of ways.

As a part of the Silent Login functionality, the <u>TVistaUser Class</u> providing basic user information was added. This class is used as a property by the TRPCBroker class and is filled with data following completion of the login process. This property and its associated data are available to all applications, whether or not they are using a Silent Login.

![](xwb-1-1-73-developer-s-guide/319.png) REF: For more information on handling divisions during Silent Login, see the “<u>Handling Divisions during Silent Login</u>” section.

### Handling Divisions during Silent Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A login may be successful, but if the user has multiple divisions from which to choose and fails to select one, the connection is terminated, and a failed login message is generated. This becomes a potential problem in that a <u>Silent Login</u> can have problems if the user has multiple divisions from which to choose and the <u>PromptDivision Property</u> is *not* set to True.

If the application wishes to handle the user specification of the division, it can attempt to set the <u>TRPCBroker Component</u> <u>Connected Property</u> to True. If upon return, the <u>Connected Property</u> is still False, it can check the Login. <u>MultiDivision Property</u>. If the <u>MultiDivision Property</u> is True, the user has multiple divisions from which to choose. The application finds the possible values for selection in the Login. <u>DivList Property (read-only)</u> (i.e., Tstrings). The values that are present in the <u>DivList Property (read-only)</u> are similar to <u>Figure 100</u>:

<span id="_Ref446337046" class="anchor"></span>Figure 99: DivList Property—Sample List of Divisions

3

1^SAN FRANCISCO^66235

2^NEW YORK^630

3^SAN DIEGO^664^1

The first (index = 0) entry is the total number of divisions that can be selected (e.g., 3 in this example). This is followed by the different divisions comprised of the following pieces:

- The second ^-piece of each entry is the division name.
- The third ^-piece of each entry is the division number.
- The fourth ^-piece with the value of 1, if present in one of the entries, is the user’s default division.

The safest value to set as the Login.Division property might be the third ^-piece of the selected division.

If the desired division is known ahead of time, it can be set into the Login.Division property for the <u>TRPCBroker Component</u> prior to attempting the connection.

### Silent Login Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1: lmAVCodes

<u>Figure 101</u> is an example of how to use Silent Login by passing the Access and Verify codes to the <u>TVistaLogin Class</u>.

<span id="_Ref446337047" class="anchor"></span>Figure 100: Silent Login—Example of Passing the Access and Verify Codes

brkrRPCBroker1.KernelLogIn := False;

brkrRPCBroker1.LogIn.Mode := lmAVCodes;

brkrRPCBroker1.LogIn.AccessCode := \*\*\*\*\*\*\*\*;

brkrRPCBroker1.LogIn.VerifyCodeCode := \*\*\*\*\*\*\*\*;

brkrRPCBroker1.LogIn.PromptDivison := True;

brkrRPCBroker1.LogIn.OnFailedLogin := myevent;

Try

brkrRPCBroker1.Connected := True;

exceptexitend;

If brkrRPCBroker1.Connected is True, then Silent Login has worked.

#### Example 2: lmAppHandle

<u>Figure 102</u> is an example of how to use Silent Login by passing an Application Handle to the <u>TVistaLogin Class</u>.

The lmAppHandle mode of the Silent Login is used when an application starts up a second application. If the second application tests for arguments on the command line, it is possible for this application to be started and make a connection to the VistA M Server *without* user interaction.

An example of a procedure for starting a second application with data on the command line to permit a Silent Login using the LoginHandle provided by the first application is shown in <u>Figure 102</u>. This is followed by a procedure that can be called in the processing related to FormCreate to use this command line data to initialize the <u>TRPCBroker Component</u> for Silent Login (<u>Figure 103</u>).

![](xwb-1-1-73-developer-s-guide/320.png) CAUTION: The procedures shown here are included within the RpcSLogin unit and can be used directly from there.

If the value for ConnectedBroker is NIL, the application specified in ProgLine is started and any command line included in ProgLine is passed to the application.

In the second application, a call to the Broker should be made shortly after starting, since the LoginHandle passed in has a finite lifetime (approximately 20 seconds) during which it is valid for the Silent Login.

<span id="_Ref446337400" class="anchor"></span>Figure 101: Silent Login—Example of Passing in an Application Handle

procedure StartProgSLogin(const ProgLine: String ; ConnectedBroker: TRPCBroker);

var

StartupInfo: TStartupInfo;

ProcessInfo: TProcessInformation;

AppHandle: String;

CmndLine: String;

begin

FillChar(StartupInfo, SizeOf(TStartupInfo), 0);

with StartupInfo dobegin

cb := SizeOf(TStartupInfo);

dwFlags := STARTF_USESHOWWINDOW;

wShowWindow := SW_SHOWNORMAL;

end;

CmndLine := ProgLine;

if ConnectedBroker \<\> nil thenbegin

AppHandle := GetAppHandle(ConnectedBroker);

CmndLine := CmndLine + ‘ s=’+ConnectedBroker.Server + ‘ p=’

\+ IntToStr(ConnectedBroker.ListenerPort) + ‘ h=’

\+ AppHandle + ‘ d=’ + ConnectedBroker.User.Division;

end;

CreateProcess(nil, Pchar(CmndLine), nil, nil, False,

NORMAL_PRIORITY_CLASS, nil, nil, StartupInfo, ProcessInfo);

end;

*{btnStart is clicked to start the second application Test2.exe}*

procedure TForm1.btnStartClick(Sender: TObject);

var

CurDir: string;

begin

*{Use Test2.exe and expecting it to be in the startup directory for the current application}*

CurDir := ExtractFilePath(ParamStr(0)) + ‘Test2.exe’;

*{Now start application with Silent Login}*

StartProgSLogin(CurDir, brkrRPCB1);

end;

The following procedure (CheckCmdLine) would be called in the FormCreate code of the application being started to check for command line input, and if relevant to the Broker connection, to set it up.

This code assumes that the following commands are used in conjunction with the values shown:

- s= Server
- p= ListenerPort
- d= User.Division
- h= LoginHandle

The command line might look like:

ProgramName.exe s=DHCPSERVER p=\<REDACTED\> d=692 h=~1XM34XYYZZQQ_X

The <u>TRPCB Unit</u> and <u>RpcSLogin Unit</u> would need to be included in the USES clause.

<span id="_Ref446337500" class="anchor"></span>Figure 102: Silent Login—Calling the CheckCmdLine Procedure

procedure CheckCmdLine(brkrRPCB: TRPCBroker);

var

j: integer;

begin

*// Iterate through possible command line arguments*for j := 0 to 15 dobeginif ParamStr(j) \<\> ‘’ then

Form1.Memo1.Lines.Add(IntToStr(j) + ‘ ’ + ParamStr(j));

if Pos(‘p=’,ParamStr(j)) \> 0 then

brkrRPCB.ListenerPort := StrToInt(Copy(ParamStr(j),

(Pos(‘=’,ParamStr(j))+1),length(ParamStr(j))));

if Pos(‘s=’,ParamStr(j)) \> 0 then

brkrRPCB.Server := Copy(ParamStr(j),

(Pos(‘=’,ParamStr(j))+1),length(ParamStr(j)));

if Pos(‘h=’,ParamStr(j)) \> 0 thenbegin

brkrRPCB.Login.LoginHandle := Copy(ParamStr(j),

(Pos(‘=’,ParamStr(j))+1),length(ParamStr(j)));

if brkrRPCB.Login.LoginHandle \<\> ‘’ thenbegin

brkrRPCB.KernelLogIn := False;

brkrRPCB.Login.Mode := lmAppHandle;

end;

end;

if Pos(‘d=’,ParamStr(j)) \> 0 then

brkrRPCB.Login.Division := Copy(ParamStr(j),

(Pos(‘=’,ParamStr(j))+1),length(ParamStr(j)));

*// for end*end;

end;

## Microsoft Windows Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications built with RPC Broker 1.1 use the Microsoft<sup>®</sup> Windows Registry to store the available servers and ports accessed via the Broker.

The Windows Registry replaces the \[RPCBroker_Servers\] section of the VISTA.INI file. The VISTA.INI file is no longer used by applications built with Broker 1.1. However, this file continues to be used by applications built using RPC Broker 1.0. During the installation of the Broker, relevant data from the VISTA.INI file is moved to the Windows Registry. Subsequent reads and writes are done via the Registry.

![](xwb-1-1-73-developer-s-guide/321.png) CAUTION: The VISTA.INI file created with RPC Broker 1.0 *must not* be removed from the Windows directory on the client workstation. It is still required for 16-bit Broker-based applications created using RPC Broker 1.0.

# DLL Interfaces (C, C++, Visual Basic)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DLL Interface Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 provides Dynamic Link Library (DLL) functions that allow applications written in *any* Microsoft<sup>®</sup> Windows-based development environment (e.g., Embarcadero’s<sup>®</sup> Delphi, Embarcadero C++, Microsoft<sup>®</sup> Visual Basic, and other COTS products), to take advantage of all the features offered by the RPC Broker component. This reflects VistA’s continued movement toward open systems that support multiple GUI and client front-ends.

The Dynamic Link Library (DLL) functions act like a “shell” around the Delphi TRPCBroker component and provide developers with an easy function-based access to the Broker component. These functions allow GUI and client front-end applications written in Embarcadero’s Delphi and other COTS products to take advantage of all the features that the Broker offers. All of the communication to the server is handled by the TRPCBroker component accessed via the DLL interface.

The functionality of the <u>TRPCBroker Component</u> for Delphi is provided in a 32-bit Dynamic Link Library (DLL) interface, in BAPI32.DLL. This enables the use of any development product that can access Windows 32-bit DLLs to create applications that communicate with VistA M Servers through the RPC Broker.

![](xwb-1-1-73-developer-s-guide/322.png) NOTE: The BAPI32.DLL contains all of the 32-bit Broker DLL functions. It provides an interface to the Broker component.

In Delphi, you have direct access to the <u>TRPCBroker Component</u> itself, and its properties and methods. In other development environments, you can only access the properties and methods of the <u>TRPCBroker Component</u> through DLL functions. To understand the DLL interface, you should understand how the <u>TRPCBroker Component</u> is used in its native environment (Delphi).

The following special issues should be considered when accessing RPC Broker functionality through its DLL:

- <u>RPC Results from DLL Calls</u>
- <u>GetServerInfo Function and the DLL</u>

![](xwb-1-1-73-developer-s-guide/323.png) REF: For a list of DLL Exported Functions, see the “<u>DLL Exported Functions</u>” section.

### Header Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Header files for using the DLL are provided for C (BAPI32.H), C++ (BAPI32.HPP), and Visual Basic (BAPI32.BAS).

- <u>C: Guidelines Overview</u>
- <u>C++: Guidelines Overview</u>
- <u>Visual Basic: Guidelines Overview</u>

### Sample DLL Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VB5EGCHO sample application, distributed with an earlier Broker Development Kit (BDK), demonstrates use of the RPC Broker 32-bit DLL from Microsoft Visual Basic. The source code was located in the following directory:

BDK32\Samples\Vb5Egcho

## DLL Exported Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 40</u> lists the <u>TRPCBroker Component</u> functions that are exported in BAPI32.DLL:

| Function                          | Description                                                                                                           |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <u>MySsoToken Function</u>        | Get a Secure Token Service (STS) token from Identity and Access Management (IAM) using 2-factor authentication (2FA). |
| <u>RPCBCall Function</u>          | Execute an RPC.                                                                                                       |
| <u>RPCBCreate Function</u>        | Create a <u>TRPCBroker Component</u>.                                                                                 |
| <u>RPCBCreateContext Function</u> | Create context.                                                                                                       |
| <u>RPCBFree Function</u>          | Destroy a <u>TRPCBroker Component</u>.                                                                                |
| <u>RPCBMultItemGet Function</u>   | Get value of a Mult item in a Param.                                                                                  |
| <u>RPCBMultPropGet Function</u>   | Get value of a <u>Mult Property</u> in a Param.                                                                       |
| <u>RPCBMultSet Function</u>       | Set a Mult item in a Param to a value.                                                                                |
| <u>RPCBMultSortedSet Function</u> | Sorts a Mult <u>Param Property</u>.                                                                                   |
| <u>RPCBParamGet Function</u>      | Get the value of a Param.                                                                                             |
| <u>RPCBParamSet Function</u>      | Set the value of a Param.                                                                                             |
| <u>RPCBPropGet Function</u>       | Get the value of a <u>TRPCBroker Component</u> property.                                                              |
| <u>RPCBPropSet Function</u>       | Set the value of a <u>TRPCBroker Component</u> property.                                                              |

<span id="_Ref449019605" class="anchor"></span>Table 41: C++: TRPCBroker C++ Class Methods

## DLL Special Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RPC Results from DLL Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When executing an RPC on a VistA M Server, results from the RPC are returned as a text stream. This text stream may or may not have embedded \<CR\>\<LF\> character combinations.

In Delphi, when you call an RPC using the <u>TRPCBroker Component</u> directly, the text stream returned from an RPC is automatically parsed and returned in the <u>TRPCBroker Component</u>’s <u>Results Property</u>, either in Results\[0\] or in multiple Results nodes. If there are no embedded \<CR\>\<LF\> character combinations in the text stream, only Results\[0\] is used. If there are embedded \<CR\>\<LF\> character combinations, results are placed into separate Results nodes based on the \<CR\>\<LF\> delimiters.

When using the DLL interface, the return value is a text stream, but no processing of the text stream is performed for you. It is up to you to parse out what would have been individual Results nodes in Delphi, based on the presence of any \<CR\>\<LF\> character combinations in the text stream.

![](xwb-1-1-73-developer-s-guide/324.png) NOTE: You *must* create a character buffer large enough to receive the entire return value of an RPC.

### GetServerInfo Function and the DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you use the <u>TRPCBroker Component</u> for Delphi, you are able to call the <u>GetServerInfo Function</u> to retrieve the end-user workstation’s server and port settings.

The functionality provided by <u>GetServerInfo Function</u> is *not* currently available through the RPC Broker 32-bit DLL interface. To work around this limitation when using the RPC Broker 32-bit DLL, you should prompt the user directly for the server and port to connect.

## C DLL Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### C: Guidelines Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BAPI32.H header file defines the function prototypes for all functions exported in the RPC Broker 32-bit DLL.

![](xwb-1-1-73-developer-s-guide/325.png) REF: For a list of DLL Exported Functions, see the “<u>DLL Exported Functions</u>” section.

To use the DLL Broker functions, using C, exported in BAPI32.DLL, do the following:

1.  <u>C: Initialize—LoadLibrary and GetProcAddress</u>
94. <u>C: Create Broker Components</u>
95. <u>C: Connect to the Server</u>
96. <u>C: Execute RPCs</u>
97. <u>C: Destroy Broker Components</u>

### C: Initialize—LoadLibrary and GetProcAddress

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step to using the RPC Broker 32-bit DLL in a C program is to load the DLL and get the process addresses for the exported functions.

To initialize access to the Broker DLL functions, do the following:

1.  Use the Windows API LoadLibrary function to load the DLL.

> <span id="_Toc82593664" class="anchor"></span>Figure 103: C: Initialize—LoadLibrary and GetProcAddress: Using the Windows API LoadLibrary Function to Load the DLL

HINSTANCE hLib = LoadLibrary(“bapi32.dll”);

if((unsigned)hLib\<=HINSTANCE_ERROR)

{

*/\* Add your error handler for case where library fails to load. \*/*

return 1;

}

98. If you successfully load the DLL, map function pointers to the addresses of the functions in the DLL that you need for your application:

> <span id="_Ref473036139" class="anchor"></span>Figure 104: C: Initialize—LoadLibrary and GetProcAddress: Mapping Function Pointers to the Addresses of the Functions in the DLL

MySsoToken = (voic \*(\_\_stdcall\*)()) GetProcAddress(hLib, “MySsoToken”);

RPCBCreate = (void \*(\_\_stdcall\*)()) GetProcAddress(hLib, “RPCBCreate”);

RPCBFree = (void (\_\_stdcall\*)(void \*)) GetProcAddress(hLib, “RPCBFree”);

RPCBCall = (char \*(\_\_stdcall\*)(void \*, char \*)) GetProcAddress(hLib, “RPCBCall”);

RPCBCreateContext = (bool (\_\_stdcall\*)(void \*, char \*)) GetProcAddress(hLib, “RPCBCreateContext”);

RPCBMultSet = (void (\_\_stdcall\*)(void \*, int, char \*, char \*)) GetProcAddress(hLib, “RPCBMultSet”);

RPCBParamGet = (void (\_\_stdcall\*)(void \*, int, int, char \*)) GetProcAddress(hLib, “RPCBParamGet”);

RPCBParamSet = (void (\_\_stdcall\*)(void \*, int, int, char \*)) GetProcAddress(hLib, “RPCBParamSet”);

RPCBPropGet = (void (\_\_stdcall\*)(void \*, char \*, char \*)) GetProcAddress(hLib, “RPCBPropGet”);RPCBPropGet = (void (\_\_stdcall\*)(void \*, char \*, char \*)) GetProcAddress(hLib, “RPCBPropGet”);

RPCBPropSet =(void (\_\_stdcall\*)(void \*, char \*, char \*)) GetProcAddress(hLib, “RPCBPropSet”);

*//// GetProcAddress, returns null on failure.//*

if( RPCBCreate == NULL \|\| RPCBFree == NULL \|\| RPCBCall == NULL \|\| RPCBCreateContext == NULL

\|\| RPCBMultSet == NULL \|\| RPCBParamGet == NULL \|\| RPCBParamSet == NULL \|\| RPCBPropGet == NULL

\|\| RPCBPropSet == NULL)

{

*/\* Add your error handler for cases where functions are not found. \*/*

return 1;

}

Now you can use functions exported in the DLL.

### C: Create Broker Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create <u>TRPCBroker Component</u>s in your C program, do the following:

1.  Create a pointer for the <u>TRPCBroker Component</u>:

*// Generic pointer for the TRPCBroker component instance.*

void \* RPCBroker;

99. Call the <u>RPCBCreate Function</u> to create a <u>TRPCBroker Component</u> and return its address into the pointer you created:

// Create the TRPCBroker component instance.

RPCBroker = RPCBCreate();

Now you can use the pointer to the created Broker component to call its methods.

### C: Connect to the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To connect to the VistA M Server from the C program, do the following:

1.  Set the server and port to connect:

*// Set the Server and Port properties to determine where to connect.*

RPCBPropSet(RPCBroker,“Server”, “BROKERSERVER”);

RPCBPropSet(RPCBroker, “ListenerPort”, “\<REDACTED\>”);

100. Set the <u>Connected Property</u> to true; this attempts a connection to the VistA M Server:

*// Set the Connected property to True, to connect.*

RPCBPropSet(RPCBroker, “Connected”, “1”);

101. Check if you are still connected. If so, continue because the connection was made. If not, quit or branch accordingly:

*// If still connected, can continue.*

RPCBPropGet(RPCBroker, “Connected”, Value);

if (atoi(Value) != 1) return false;

102. Attempt to create context for your application’s “B”-type option. If you cannot create context, you should quit or branch accordingly. If <u>RPCBCreateContext Function</u> returns True, then you are ready to call all RPCs registered to your application’s “B”-type option:

*// Create Context for your application’s option (in this case, XWB EGCHO).*

result = RPCBCreateContext(RPCBroker, “XWB EGCHO”);

return result;

### C: Execute RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you can make a successful connection to the RPC Broker VistA M Server, and create an application context, you can execute any RPCs registered to your context.

To execute RPCs from your C program, do the following:

1.  Create a character buffer large enough to hold your RPC’s return value:

static char Value \[1024\];

103. Set the <u>RemoteProcedure Property</u> of the <u>TRPCBroker Component</u> to the RPC to execute:

RPCBPropSet(RPCBroker, “RemoteProcedure”,“XWB GET VARIABLE VALUE”);

104. Set the Param values for any parameters needed by the RPC. In the following example, one TRPCBrokerParam node is set (the equivalent of Param\[0\]):
1.  A value of 0 for parameter 2 denotes the integer index of the Param node being set (Param\[0\]).
25. A value of *reference* for parameter 3 denotes the setting for the equivalent of Param\[0\].PType. This uses the enumerated values for PType (see <u>Table 11</u>) declared in the header file.
26. A value of “DUZ” for parameter 4 denotes that the equivalent of Param\[0\].Value is “DUZ”:

RPCBParamSet(RPCBroker, 0, reference, “DUZ”);

105. Use the <u>RPCBCall Function</u> to execute the RPC:

RPCBCall(RPCBroker, Value);

The return value from the RPC is returned in the second parameter (in this case, the Value character buffer).

### C: Destroy Broker Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are done using any <u>TRPCBroker Component</u>, you should call its destroy method to free it from memory.

To destroy <u>TRPCBroker Components</u> from your C program, do the following:

1.  Make sure the <u>TRPCBroker Component</u> is *not* connected:

RPCBPropSet(RPCBroker, “Connected”, “0”);

106. Call the RPCBFree method to destroy the object:

*// Destroy the RPCBroker component instance.*

RPCBFree(RPCBroker);

107. When you have destroyed all <u>TRPCBroker Components</u>, but before your application terminates, you should call the Windows API FreeLibrary function to unload the DLL:

FreeLibrary(hLib);

## C++ DLL Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### C++: Guidelines Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BAPI32.HPP header file defines a class “wrapper” around the RPC Broker 32-bit DLL, defining a TRPCBroker C++ class. Objects of this class include all functions exported in the DLL, as methods of the TRPCBroker C++ class.

![](xwb-1-1-73-developer-s-guide/326.png) REF: For a list of C++ class methods, see the “<u>C++: TRPCBroker C++ Class Methods</u>” section.

One feature of wrapping a class around the RPC Broker 32-bit DLL is that all the ordinary details of working with a DLL (loading the DLL, getting the addresses of the functions in the DLL, and freeing the DLL) are done within the class definition. When you initialize the class, all of the details of loading and unloading the detail (LoadLibrary, GetProcAddress, and FreeLibrary) are done for you.

To use objects of the class, simply initialize the class, and then create and destroy objects of the class.

To use the TRPCBroker C++ class that encapsulates BAPI32.DLL, do the following:

1.  <u>C++: Initialize the Class</u>
108. <u>C++: Create Broker Instances</u>
109. <u>C++: Connect to the Server</u>
110. <u>C++: Execute RPCs</u>
111. <u>C++: Destroy Broker Instances</u>

### C++: Initialize the Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step to using the RPC Broker 32-bit DLL in a C++ program is to load the DLL and get the process addresses for the exported functions.

To initialize access to the Broker DLL functions, do the following:

1.  Include bapi32.hpp in the program:

\#include bapi32.hpp

This includes the TRPCBroker C++ class definition in the program.

112. Later, when you create a TRPCBroker C++ class object in the program, the class definition takes care of the following:
- Loading the DLL if *not* already loaded.
- Mapping the DLL functions if *not* already mapped.
- Creating the instance of the <u>TRPCBroker Component</u>.

### C++: Create Broker Instances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create instances of TRPCBroker C++ class objects in a C++ program, do the following:

1.  Create a variable of type TRPCBroker. This does the following:
- Initializes the TRPCBroker class.
- Creates a TRPCBroker C++ class object instance.
- Creates a <u>TRPCBroker Component</u>.

*// Initialize the TRPCBroker class.*

TRPCBroker RPCInst;

113. Access the properties and methods of the created <u>TRPCBroker Component</u> through the TRPCBroker C++ class object.

### C++: Connect to the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To connect to the VistA M Server from the C++ program, do the following:

1.  Set the server and port to connect:

*// Set the Server and Port properties to determine where to connect.*

RPCInst.RPCBPropSet(“Server”, server);

RPCInst.RPCBPropSet(“ListenerPort”, “\<REDACTED\>”);

114. Set the <u>Connected Property</u> to True; this attempts a connection to the VistA M Server:

*// Set the Connected property to True, to connect.*

RPCInst.RPCBPropSet(“Connected”, “1”);

115. Check if you are still connected. If so, continue because the connection was made. If not, quit or branch accordingly:

*// If still connected, can continue.*

RPCInst.RPCBPropGet(“Connected”, Value);

if (atoi(Value) != 1) return false;

116. Attempt to create context for the application’s “B”-type option. If you *cannot* create context, quit or branch accordingly. If <u>RPCBCreateContext Function</u> returns True, then you are ready to call all RPCs registered to the application’s “B”-type option:

*// Create Context for your application’s option (in this case, XWB EGCHO).*

result = RPCInst.RPCBCreateContext(“XWB EGCHO”);

return result;

### C++: Execute RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you can make a successful connection to the RPC Broker VistA M Server, and create an application context, you can execute any RPCs registered to your context.

To execute RPCs from a C++ program, do the following:

1.  Create a character buffer large enough to hold your RPC’s return value:

char Value \[1024\];

117. Set the <u>RemoteProcedure Property</u> of the <u>TRPCBroker Component</u> to the RPC to execute:

RPCInst.RPCBPropSet(“RemoteProcedure”,“XWB GET VARIABLE VALUE”);

118. Set the Param values for any parameters needed by the RPC. In the following example, one TRPCBrokerParam node is set (the equivalent of Param\[0\]):
1.  A value of 0 for parameter 1 denotes the integer index of the Param node being set (Param\[0\]).
27. A value of *reference* for parameter 2 denotes the setting for the equivalent of Param\[0\].PType. This uses the enumerated values for PType (see <u>Table 11</u>) declared in the header file.
28. A value of “DUZ” for parameter 3 denotes that the equivalent of Param\[0\].Value is “DUZ”:

RPCInst.RPCBParamSet(0, reference, “DUZ”);

119. Use the <u>RPCBCall Function</u> to execute the RPC:

RPCInst.RPCBCall(Value);

The return value from the RPC is returned in the first parameter (in this case, the Value character buffer).

### C++: Destroy Broker Instances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You do *not* need to do anything special to free up memory used by the <u>TRPCBroker Component</u> instances and their companion TRPCBroker C++ class objects. They are automatically destroyed when your program terminates, just as normal variables are automatically destroyed.

Also, when your program terminates, the FreeLibrary Windows API call is automatically executed to unload the RPC Broker 32-bit DLL, so there is no need to do this manually.

### C++: TRPCBroker C++ Class Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The functions in the RPC Broker 32-bit DLL are encapsulated in the TRPCBroker C++ class methods shown in <u>Table 41</u>:

| DLL Function                      | TRPCBroker C++ Class Method                                       |
|-----------------------------------|-------------------------------------------------------------------|
| <u>MySsoToken Function</u>        | char \* MySSOToken();                                             |
| <u>RPCBCall Function</u>          | char \* RPCBCall( char \* s);                                     |
| <u>RPCBCreateContext Function</u> | bool RPCBCreateContext ( char \* s);                              |
| <u>RPCBMultItemGet Function</u>   | void RPCBMultItemGet ( int i, char \* s, char \* t);              |
| <u>RPCBMultPropGet Function</u>   | void RPCBMultPropGet (void \* ptr, int i , char \* s, char \* t); |
| <u>RPCBMultSet Function</u>       | void RPCBMultSet ( int i, char \* s, char \* t);                  |
| <u>RPCBMultSortedSet Function</u> | void RPCBMultSortedSet (void \* ptr, int i, bool v);              |
| <u>RPCBParamGet Function</u>      | void RPCBParamGet ( int i, int j, char \* s);                     |
| <u>RPCBParamSet Function</u>      | void RPCBParamSet ( int i, int j, char \* s);                     |
| <u>RPCBPropGet Function</u>       | void RPCBPropGet ( char \* s, char \* t);                         |
| <u>RPCBPropSet Function</u>       | void RPCBPropSet ( char \* s, char \* t);                         |

<span id="_Toc82593707" class="anchor"></span>Table 42: MySsoToken Function—Declarations

## Visual Basic DLL Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Visual Basic: Guidelines Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BAPI32.BAS header file defines the function prototypes for all functions exported in the RPC Broker 32-bit DLL.

![](xwb-1-1-73-developer-s-guide/327.png) REF: For a list of DLL exported functions, see the “<u>DLL Exported Functions</u>” section.

To use the DLL Broker functions, using Visual Basic, exported in BAPI32.DLL, do the following:

1.  <u>Visual Basic: Initialize</u>
120. <u>Visual Basic: Create Broker Components</u>
121. <u>Visual Basic: Connect to the Server</u>
122. <u>Visual Basic: Execute RPCs</u>
123. <u>Visual Basic: Destroy Broker Components</u>

#### Sample DLL Application

The VB5EGCHO sample application, distributed with an earlier Broker Development Kit (BDK), demonstrates use of the RPC Broker 32-bit DLL from Microsoft Visual Basic. The source code was located in the following directory:

BDK32\Samples\Vb5Egcho

### Visual Basic: Initialize

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step to using the RPC Broker 32-bit DLL in a Visual Basic program is to load the DLL and get the process addresses for the exported functions.

To initialize access to the Broker DLL functions, do the following:

1.  Include BAPI32.BAS as a module in your Visual Basic program.
124. Visual Basic takes care of loading the DLL and mapping its functions.

### Visual Basic: Create Broker Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create <u>TRPCBroker Components</u> in your Visual Basic program, do the following:

1.  Create a variable to be a handle for the <u>TRPCBroker Component</u>:

Public intRPCBHandle As Long

125. Call the <u>RPCBCreate Function</u> to create a <u>TRPCBroker Component</u> and return its address into the variable you created:

intRPCBHandle = RPCBCreate()

Now, you can use the handle to the created Broker component to call its methods.

### Visual Basic: Connect to the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To connect to the VistA M Server from the Visual Basic program, do the following:

1.  Set the server and port to connect:

Call RPCBPropSet(intRPCBHandle, “Server”, “BROKERSERVER”)

Call RPCBPropSet(intRPCBHandle, “ListenerPort”, “\<REDACTED\>”)

126. Set the <u>Connected Property</u> to true; this attempts a connection to the VistA M Server:

Call RPCBPropSet(intRPCBHandle, “Connected”, “1”)

127. Check if you are still connected. If so, continue because the connection was made. If not, quit or branch accordingly:

RPCBPropGet(intRPCBHandle, “Connected”, strResult)

128. Attempt to create context for your application’s “B”-type option. If you *cannot* create context, quit or branch accordingly. If <u>RPCBCreateContext Function</u> returns True, then you are ready to call all RPCs registered to the application’s “B”-type option:

intResult = RPCBCreateContext(intRPCBHandle, “MY APPLICATION”)

### Visual Basic: Execute RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you can make a successful connection to the RPC Broker VistA M Server, and create an application context, you can execute any RPCs registered to your context.

To execute RPCs from your Visual Basic program, do the following:

1.  Create a character buffer large enough to hold your RPC’s return value:

Public strBuffer As String \* 40000

129. Set the <u>RemoteProcedure Property</u> of the <u>TRPCBroker Component</u> to the RPC to execute:

Call RPCBPropSet(intRPCBHandle, “RemoteProcedure”, “XWB GET VARIABLE VALUE”)

130. Set the Param values for any parameters needed by the RPC. In the following example, one TRPCBrokerParam node is set (the equivalent of Param\[0\]):
1.  A value of 0 for parameter 2 denotes the integer index of the Param node being set (Param\[0\]).
29. A value of *reference* for parameter 3 denotes the setting for the equivalent of Param\[0\].PType. This uses the enumerated values for PType (see <u>Table 11</u>) declared in the header file.
30. A value of “DUZ” for parameter 4 denotes that the equivalent of Param\[0\].Value is “DUZ”:

Call RPCBParamSet(intRPCBHandle, 0, reference, “DUZ”);

131. Use the <u>RPCBCall Function</u> to execute the RPC:

Call RPCBCall(intRPCBHandle, strBuffer

The return value from the RPC is returned in the second parameter (in this case, the Value character buffer).

### Visual Basic: Destroy Broker Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are done using any <u>TRPCBroker Component</u>, you should call its destroy method to free it from memory (see the “<u>Memory Leaks</u>”).

To destroy <u>TRPCBroker Components</u> from your Visual Basic program, do the following:

1.  Make sure the <u>TRPCBroker Component</u> is *not* connected:

Call RPCBPropSet(intRPCBHandle, “Connected”, “0”)

132. Call the <u>RPCBFree Function</u> to destroy the object:

RPCBFree(intRPCBHandle)

Visual Basic takes care of the details of unloading the DLL.

## MySsoToken Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Get a Secure Token Service (STS) token from Identity and Access Management (IAM) using 2-factor authentication. This encapsulates the following Broker Development Kit methods:

- TXWBSSOiToken Create
- SSOiToken
- Free

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                               |
|------------|-------------------------------------------|
| Delphi | function MySsoToken: PChar; stdcall;  |
| C      | void \*(\_\_stdcall \*MySsoToken) (void); |
| C++    | void \* MySsoToken(void);                 |
| VB     | Function MySsoToken () As String          |

<span id="_Toc82593708" class="anchor"></span>Table 43: RPCBCall Function—Declarations

### Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- String—Digitally signed XML (SAML) token containing authenticated user identity.
- Null string—If authentication failed or token could not be obtained.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

result = MySsoToken();

#### C++

Result = MySsoToken();

#### Visual Basic

StrResult = MySsoToken()

## RPCBCall Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Executes a remote procedure call and fills the passed buffer with the data resulting from the call. This is equivalent to the <u>TRPCBroker Component</u>’s <u>Call Method</u>.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                 |
|------------|-----------------------------------------------------------------------------|
| Delphi | procedure RPCBCall(const RPCBroker: TRPCBroker; CallResult: PChar); |
| C      | char \*(\_\_stdcall \*RPCBCall) (void \*, char \*);                         |
| C++    | char \* RPCBCall( char \* s);                                               |
| VB     | Sub RPCBCall (ByVal intRPCBHandle As Long, ByVal strCallResult As String)   |

<span id="_Toc82593709" class="anchor"></span>Table 44: RPCBCall Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter      | Description                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPCBroker  | Handle of the Broker component that contains the name of the remote procedure and all of the required parameters.                                                    |
| CallResult | An empty character buffer that the calling application must create (allocate memory for) before making this call. This buffer is filled with the result of the call. |

<span id="_Toc82593710" class="anchor"></span>Table 45: RPCBCreate Function—Declarations

![](xwb-1-1-73-developer-s-guide/328.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBCall(RPCBroker, Value);

#### C++

*// MyInstance is defined as an instance of the TRPCBroker.*

MyInstance.RPCBCall( strbuffer);

#### Visual Basic

Call RPCBCall(intRPCBHandle, strBuffer)

## RPCBCreate Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBCreate Function creates a new RPC Broker component for the application, which can then be used to connect to the VistA M Server and call remote procedures.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declarations                                      |
|------------|---------------------------------------------------|
| Delphi | function RPCBCreate: TRPCBroker;              |
| C      | void \* (\_\_stdcall \*RPCBCreate)(void);         |
| C++    | N/A (encapsulated in TRPCBroker class definition) |
| VB     | Function RPCBCreate () As Long                    |

<span id="_Toc82593711" class="anchor"></span>Table 46: RPCBCreateContext Function—Declarations

### Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A handle for the <u>TRPCBroker Component</u> created.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

*// Create the TRPCBroker component instance.*

RPCBroker = RPCBCreate();

#### Visual Basic

intRPCBHandle = RPCBCreate()

## RPCBCreateContext Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBCreateContext function calls the <u>TRPCBroker Component</u>’s <u>CreateContext Method</u> to set up the environment on the VistA M Server for subsequent RPCs.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declarations                                                                                            |
|------------|---------------------------------------------------------------------------------------------------------|
| Delphi | function RPCBCreateContext(const RPCBroker: TRPCBroker; const Context: PChar): boolean; |
| C      | bool (\_\_stdcall \*RPCBCreateContext) (void \*, char \*);                                              |
| C++    | bool RPCBCreateContext ( char \* s);                                                                    |
| VB     | Function RPCBCreateContext (ByVal intRPCBHandle As Long, ByVal strContext As String) As Integer         |

<span id="_Toc82593712" class="anchor"></span>Table 47: RPCBCreateContext Function—Parameters

### Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- True/1—If context could be created.
- False/0—If context could *not* be created.

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter     | Description                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| RPCBroker | Handle of the <u>TRPCBroker Component</u>.                                                                        |
| Context   | Null-terminated string identifying the option on the VistA M Server for which subsequent RPCs are registered. |

<span id="_Toc82593713" class="anchor"></span>Table 48: RPCBFree Function—Declarations

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

*// XWB EGCHO is a “B” (Broker) type option in the OPTION file.*

result = RPCBCreateContext(RPCBroker, “XWB EGCHO”);

#### C++

*// XWB EGCHO is a “B” (Broker) type option in the OPTION file.*

MyInstance.RPCBCreateContext(“XWB EGCHO”)

#### Visual Basic

intResult = RPCBCreateContext(intRPCBHandle, “MY APPLICATION”)

‘where MY APPLICATION is a “B” (Broker) type option in the Option file.

## RPCBFree Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBFree function destroys the RPC Broker component and releases associated memory (see “<u>Memory Leaks</u>” section).

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                       |
|------------|---------------------------------------------------|
| Delphi | procedure RPCBFree(RPCBroker: TRPCBroker);    |
| C      | void (\_\_stdcall \*RPCBFree)(void \*);           |
| C++    | N/A (encapsulated in TRPCBroker class definition) |
| VB     | Sub RPCBFree (ByVal intRPCBHandle As Long)        |

<span id="_Toc82593714" class="anchor"></span>Table 49: RPCBFree Function—Parameter

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter     | Description                                           |
|---------------|-------------------------------------------------------|
| RPCBroker | Handle of the <u>TRPCBroker Component</u> to destroy. |

<span id="_Toc82593715" class="anchor"></span>Table 50: RPCBMultItemGet Function—Declarations

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

*// Destroy the TRPCBroker component instance.*

RPCBFree(RPCBroker);

#### Visual Basic

RPCBFree (intRPCBHandle)

## RPCBMultItemGet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBMultItemGet function returns a requested item in a <u>TRPCBroker Component</u> <u>Param Property</u>’s <u>Mult Property</u>.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                                           |
|------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBMultItemGet (const RPCBroker: TRPCBroker; ParamIndex: integer; Subscript, Value: PChar);                    |
| C      | void (\_\_stdcall \*RPCBMultItemGet) (void \*, int, char \*, char \*);                                                                |
| C++    | void RPCBMultItemGet ( int i, char \* s, char \* t);                                                                                  |
| VB     | Sub RPCBMultItemGet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal strSubscript As String, ByVal strValue As String) |

<span id="_Toc82593716" class="anchor"></span>Table 51: RPCBMultItemGet Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter      | Description                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPCBroker  | Handle of the <u>TRPCBroker Component</u>.                                                                                                                                       |
| ParamIndex | Integer index of the parameter that contains the <u>Mult Property</u>.                                                                                                           |
| Subscript  | Null-terminated string identifying the Mult element to get.                                                                                                                  |
| Value      | An empty buffer that the calling application *must* create (allocate memory for) before making this call. This buffer is filled with the value of the <u>Mult Property</u> item. |

<span id="_Toc82593717" class="anchor"></span>Table 52: RPCBMultPropGet—Declarations

![](xwb-1-1-73-developer-s-guide/329.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

*// The following corresponds to getting the value of PARAM\[0\].Mult\[“0”\]*

RPCBMultItemGet(RPCBroker, 0 , “0”, Value);

#### C++

MyInstance.RPCBMultItemGet(0 , “0”, Value);

#### Visual Basic

Call RPCBMultItemGet(intRPCBHandle, 0, “0”, strResult)

## RPCBMultPropGet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBMultPropGet function returns a selected property value of a <u>TRPCBroker Component</u> <u>Param Property</u>’s <u>Mult Property</u>.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBMultPropGet(const RPCBroker: TRPCBroker; ParamIndex: integer; Prop,Value: PChar);                      |
| C      | void (\_\_stdcall \*RPCBMultPropGet) (void \*, int, char \*, char \*);                                                           |
| C++    | void RPCBMultPropGet (int i , char \* s, char \* t);                                                                             |
| VB     | Sub RPCBMultPropGet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal strProp As String, ByRef strValue As String) |

<span id="_Toc82593718" class="anchor"></span>Table 53: RPCBMultPropGet—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter      | Description                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPCBroker  | Handle of the <u>TRPCBroker Component</u>.                                                                                                                                                      |
| ParamIndex | Integer index of the parameter that contains the <u>Mult Property</u>.                                                                                                                          |
| Prop       | Null-terminated string identifying the name of the TMult property to get.                                                                                                               |
| Value      | An empty buffer that the calling application *must* create (allocate memory for) before making this call. This buffer is filled with value of the <u>Mult Property</u> that is in the Prop. |

<span id="_Toc82593719" class="anchor"></span>Table 54: RPCBMultSet Function—Declarations

![](xwb-1-1-73-developer-s-guide/330.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBMultPropGet(RPCBroker, 0, “Count”, Value);

#### C++

MyInstance.RPCBMultPropGet(0, “Count”, Value);

#### Visual Basic

Call RPCBMultPropGet(intRPCBHandle, 0, “Count”, strResult)

## RPCBMultSet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBMultSet function sets an item in a <u>TRPCBroker Component</u> <u>Param Property</u>’s <u>Mult Property</u> to a value.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBMultSet(const RPCBroker: TRPCBroker; ParamIndex: integer; Subscript, Value: PChar);                         |
| C      | void (\_\_stdcall \*RPCBMultSet) (void \*, int, char \*, char \*);                                                                |
| C++    | void RPCBMultSet ( int i, char \* s, char \* t);                                                                                  |
| VB     | Sub RPCBMultSet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal strSubscript As String, ByVal strValue As String) |

<span id="_Toc82593720" class="anchor"></span>Table 55: RPCBMultSet Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter      | Description                                                                              |
|----------------|------------------------------------------------------------------------------------------|
| RPCBroker  | Handle of the <u>TRPCBroker Component</u>.                                               |
| ParamIndex | Integer index of the parameter that contains the <u>Mult Property</u>.                   |
| Subscript  | Null-terminated string of the Mult item to set.                                      |
| Value      | Null-terminated string containing the value that the Mult item should be set to. |

<span id="_Toc82593721" class="anchor"></span>Table 56: RPCBMultSortedSet Function—Declarations

![](xwb-1-1-73-developer-s-guide/331.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBMultSet(RPCBroker, 0, “1”, “12/19/97”);

#### C++

MyInstance.RPCBMultSet(0, “1”, “12/19/97”);

#### Visual Basic

Call RPCBMultSet(intRPCBHandle, 0, “1”, “12/19/97”)

## RPCBMultSortedSet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBMultSortedSet function sets the <u>Sorted Property</u> of a <u>Mult Property</u>. In essence, sorts and keeps the <u>Mult Property</u> sorted or just leaves it in the order it is populated.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBMultSortedSet(const RPCBroker: TRPCBroker; ParamIndex: integer; Value: boolean); |
| C      | void (\_\_stdcall \*RPCBMultSortedSet) (void \*, int, bool);                                               |
| C++    | void RPCBMultSortedSet (int i, bool v);                                                                    |
| VB     | Sub RPCBMultSortedSet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal intValue As Integer) |

<span id="_Toc82593722" class="anchor"></span>Table 57: RPCBMultSortedSet Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc82593723" class="anchor"></span>Table 58: RPCBParamGet Function—Declarations</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPCBroker</strong></td>
<td>Handle of the <u>TRPCBroker Component</u>.</td>
</tr>
<tr class="even">
<td><strong>ParamIndex</strong></td>
<td>Integer index of the parameter that contains the <u>Mult Property</u>.</td>
</tr>
<tr class="odd">
<td><strong>Value</strong></td>
<td><p>Can be either a Boolean or, if the calling application language does <em>no</em>t support Boolean type, can be an integer:</p>
<ul>
<li><p><strong>True</strong> or <strong>1—</strong>Sorts the Mult and keeps it sorted thereafter when other elements are added.</p></li>
<li><p><strong>False</strong> or <strong>0—</strong>Does <em>not</em> sort the Mult and the elements are stored in the order they are added.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc82593723" class="anchor"></span>Table 58: RPCBParamGet Function—Declarations

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBMultSortedSet(RPCBroker, 0, 1);

#### C++

MyInstance.RPCBMultSortedSet(0, 1);

#### Visual Basic

Call RPCBMultPropGet(intRPCBHandle, 0, 1)

## RPCBParamGet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBParamGet function returns two values in two parameters: the value and the parameter type of a Param item.

You can compare the returned parameter type to the following enumerated values:

- literal
- reference
- list

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                                                |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBParamGet(const RPCBroker: TRPCBroker; ParamIndex: integer; var ParamType: <u>TParamType</u>; var ParamValue: PChar); |
| C      | void (\_\_stdcall \*RPCBParamGet) (void \*, int, int, char \*);                                                                            |
| C++    | void RPCBParamGet ( int i, int j, char \* s);                                                                                              |
| VB     | Sub RPCBParamGet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal intParTyp As Integer, ByVal intParVal As String)          |

<span id="_Toc82593724" class="anchor"></span>Table 59: RPCBParamGet Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter      | Description                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RPCBroker  | Handle of the <u>TRPCBroker Component</u>.                                                                                                                                                        |
| ParamIndex | Integer index of the parameter to get the value.                                                                                                                                                  |
| ParamType  | This variable, after making the RPCBParamGet call, is filled with <u>PType Property</u> of a Param\[ParamIndex\].                                                                                 |
| ParamValue | An empty buffer that you *must* create (allocate memory for) before making this call. This buffer, after making the RPCBParamGet call, is filled with Value of a Param\[ParamIndex\]. |

<span id="_Toc82593725" class="anchor"></span>Table 60: RPCBParamSet Function—Declarations

![](xwb-1-1-73-developer-s-guide/332.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

*// PType and Value are variables to retrieve values into.*

RPCBParamGet(RPCBroker, 0, PType, Value);

#### C++

*// PType and Value are variables to retrieve values into.*

MyInstance.RPCBParamGet(0, PType, Value);

#### Visual Basic

Call RPCBParamGet(intRPCBHandle, 0, PType, strResult)

‘ where PType and strResult are variables to retrieve values into

## RPCBParamSet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBParamSet function sets one Param item’s <u>Value Property</u> and <u>PType Property</u>, in a single call.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                                                                              |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBParamSet(const RPCBroker: TRPCBroker; const ParamIndex: integer; const ParamType: <u>TParamType</u>; const ParamValue: PChar); |
| C      | void (\_\_stdcall \*RPCBParamSet) (void \*, int, int, char \*);                                                                                          |
| C++    | void RPCBParamSet ( int i, int j, char \* s);                                                                                                            |
| VB     | Sub RPCBParamSet (ByVal intRPCBHandle As Long, ByVal intParIdx As Integer, ByVal intParTyp As Integer, ByVal intParVal As String)                        |

<span id="_Ref464709493" class="anchor"></span>Table 61: RPCBParamSet Function—Parameters

### Parameter Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc82593727" class="anchor"></span>Table 62: RPCBPropGet Function—Declarations</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPCBroker</strong></td>
<td>Handle of the <u>TRPCBroker Component</u>.</td>
</tr>
<tr class="even">
<td><strong>ParamIndex</strong></td>
<td>Integer index of the parameter.</td>
</tr>
<tr class="odd">
<td><strong>ParamType</strong></td>
<td><p>Set to the parameter type for the parameter you are setting. The value should be one of the integer values that are valid as a <strong>PType</strong>:</p>
<ul>
<li><p><strong>0</strong> (literal)</p></li>
<li><p><strong>1</strong> (reference)</p></li>
<li><p><strong>2</strong> (list)</p></li>
</ul>
<p>You can use the enumerated values literal, reference and list, as declared in the C, C++, or Visual Basic header file.</p>
<p>![](xwb-1-1-73-developer-s-guide/333.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.</p></td>
</tr>
<tr class="even">
<td><strong>ParamValue</strong></td>
<td><strong>Null-terminated</strong> string containing the Value to set.</td>
</tr>
</tbody>
</table>

<span id="_Toc82593727" class="anchor"></span>Table 62: RPCBPropGet Function—Declarations

![](xwb-1-1-73-developer-s-guide/334.png) REF: For information about the size of parameters and results that can be passed to and returned from the <u>TRPCBroker Component</u>, see the “<u>RPC Limits</u>” section.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBParamSet(RPCBroker, 0, reference, “DUZ”);

#### C++

MyInstance.RPCBParamSet(0, reference, “DUZ”);

#### Visual Basic

Call RPCBParamSet(intRPCBHandle, 0, literal, Text3.Text)

## RPCBPropGet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBPropGet function returns a requested property of a <u>TRPCBroker Component</u>.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBPropGet(const RPCBroker: TRPCBroker; const Prop: PChar; {var} Value: PChar); |
| C      | void (\_\_stdcall \*RPCBPropGet) (void \*, char \*, char \*);                                          |
| C++    | void RPCBPropGet ( char \* s, char \* t);                                                              |
| VB     | Sub RPCBPropGet (ByVal intRPCBHandle As Long, ByVal strProp As String, ByVal strValue As String)       |

<span id="_Toc82593728" class="anchor"></span>Table 63: RPCBPropGet Function—Parameters

<table>
<caption><p><span id="_Toc82593729" class="anchor"></span>Table 64: RPCBPropSet Function—Declarations</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPCBroker</strong></td>
<td>Handle of the <u>TRPCBroker Component</u>.</td>
</tr>
<tr class="even">
<td><strong>Prop</strong></td>
<td><p><strong>Null-terminated</strong> string of the property to get. <em>Not</em> case-sensitive. Valid properties to get are:</p>
<ul>
<li><p><u>ClearParameters Property</u></p></li>
<li><p><u>ClearResults Property</u></p></li>
<li><p><u>Connected Property</u></p></li>
<li><p><u>DebugMode Property</u></p></li>
<li><p><u>ListenerPort Property</u></p></li>
<li><p><u>RemoteProcedure Property</u></p></li>
<li><p><u>RPCTimeLimit Property</u></p></li>
<li><p><u>RPCVersion Property</u></p></li>
<li><p><u>Server Property<br />
</u></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Value</strong></td>
<td><p>An empty buffer that you <em>must</em> create (allocate memory for) before making this call. After this call, the buffer is filled with value of the property that is in the <strong>Prop</strong>. This procedure takes care of all the necessary type conversions. Boolean property values are returned as either of the following:</p>
<ul>
<li><p><strong>1</strong> (True)</p></li>
<li><p><strong>0</strong> (False)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc82593729" class="anchor"></span>Table 64: RPCBPropSet Function—Declarations

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBPropGet(RPCBroker, “Connected”, Value);

#### C++

MyInstance.RPCBPropGet(“Connected”, Value);

#### Visual Basic

Call RPCBPropGet(intRPCBHandle, “Server”, strResult)

## RPCBPropSet Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBPropSet function sets a <u>TRPCBroker Component</u> property to some value.

### Declarations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Software   | Declaration                                                                                      |
|------------|--------------------------------------------------------------------------------------------------|
| Delphi | procedure RPCBPropSet(const RPCBroker: TRPCBroker; Prop,Value: PChar);                   |
| C      | void (\_\_stdcall \*RPCBPropSet) (void \*, char \*, char \*);                                    |
| C++    | void RPCBPropSet ( char \* s, char \* t);                                                        |
| VB     | Sub RPCBPropSet (ByVal intRPCBHandle As Long, ByVal strProp As String, ByVal strValue As String) |

<span id="_Toc82593730" class="anchor"></span>Table 65: RPCBPropSet Function—Parameters

<table>
<caption><p><span id="_Ref467590751" class="anchor"></span>Table 66: Glossary of Terms and Acronyms</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPCBroker</strong></td>
<td>Handle of the <u>TRPCBroker Component</u>.</td>
</tr>
<tr class="even">
<td><strong>Prop</strong></td>
<td><p><strong>Null-terminated</strong> string of the property to set; <em>not</em> case-sensitive. Valid properties to set are:</p>
<ul>
<li><p><u>ClearParameters Property</u></p></li>
<li><p><u>ClearResults Property</u></p></li>
<li><p><u>Connected Property</u></p></li>
<li><p><u>DebugMode Property</u></p></li>
<li><p><u>ListenerPort Property</u></p></li>
<li><p><u>RemoteProcedure Property</u></p></li>
<li><p><u>RPCTimeLimit Property</u></p></li>
<li><p><u>RPCVersion Property</u></p></li>
<li><p><u>Server Property<br />
</u></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Value</strong></td>
<td><p><strong>Null-terminated</strong> string of the value to which the <strong>Prop</strong> property should be set. This procedure takes care of converting the passed in value to whatever type the property expects. For Boolean properties, pass in either of the following:</p>
<ul>
<li><p><strong>1</strong> (True)</p></li>
<li><p><strong>0</strong> (False)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref467590751" class="anchor"></span>Table 66: Glossary of Terms and Acronyms

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### C

RPCBPropSet(RPCBroker, “ListenerPort”, “\<REDACTED\>”);

#### C++

MyInstance.RPCBPropSet(“ListenerPort”, “\<REDACTED\>”);

#### Visual Basic

Call RPCBPropSet(intRPCBHandle, “Server”, cboServer.Text)

<span id="_Toc82593561" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Client</td>
<td>A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="even">
<td>Component</td>
<td>An object-oriented term used to describe the building blocks of GUI applications. A software object that contains data and code. A component may or may not be visible. These components interact with other components on a form to create the GUI user application interface.</td>
</tr>
<tr class="odd">
<td>DHCP</td>
<td><strong>D</strong>ynamic <strong>H</strong>ost <strong>C</strong>onfiguration <strong>P</strong>rotocol.</td>
</tr>
<tr class="even">
<td>DLL</td>
<td><p><strong>D</strong>ynamic <strong>L</strong>ink <strong>L</strong>ibrary. A DLL allows executable routines to be stored separately as files with a DLL extension. These routines are only loaded when a program calls for them. DLLs provide several advantages:</p>
<ol type="1">
<li><p>DLLs help save on computer memory, since memory is only consumed when a DLL is loaded. They also save disk space. With static libraries, your application absorbs all the library code into your application, so the size of your application is greater. Other applications using the same library also carry this code around. With the DLL, you do <em>not</em> carry the code itself; you have a pointer to the common library. All applications using it then share one image.</p></li>
<li><p>DLLs ease maintenance tasks. Because the DLL is a separate file, any modifications made to the DLL do <em>not</em> affect the operation of the calling program or any other DLL.</p></li>
<li><p>DLLs help avoid redundant routines. They provide generic functions that can be used by a variety of programs.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><span id="DNS" class="anchor"></span>DNS</td>
<td>The Domain Name Service (DNS) is a distributed database that maps names to their Internet Protocol (IP) addresses or IP addresses to their names. A query to this database is used to resolve names and IP addresses.</td>
</tr>
<tr class="even">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser Interface. A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.</td>
</tr>
<tr class="odd">
<td><span id="HANDLE" class="anchor"></span>HANDLE</td>
<td><p>A HANDLE is a string returned by <u>XWB REMOTE RPC</u> or <u>XWB DEFERRED RPC</u>. The application should store the HANDLE and use it to:</p>
<ol type="1">
<li><p>Check for the return of the data.</p></li>
</ol>
<ol start="4" type="1">
<li><p>Retrieve the data.</p></li>
<li><p>Clear the data from the VistA M Server.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><span id="HOSTS_File" class="anchor"></span>HOSTS File</td>
<td>The HOSTS file is an ASCII text file that contains a list of the servers and their Internet Protocol (IP) addresses. It is recommended that you put in a “<strong>DHCPSERVER</strong>” entry that points to the main server you intend using with the Broker the majority of the time. In your applications, you are able to specify any server you wish; however, if the <strong>Server</strong> property = “ (i.e., <strong>NULL</strong>), you get an error.</td>
</tr>
<tr class="odd">
<td>IAM</td>
<td>Identity and Access Management.</td>
</tr>
<tr class="even">
<td>Icon</td>
<td>A picture or symbol that graphically represents an object or a concept.</td>
</tr>
<tr class="odd">
<td><span id="IP_Address" class="anchor"></span>IP Address</td>
<td>The Internet Protocol (IP) address is the network interface address for a client workstation, server, or device.</td>
</tr>
<tr class="even">
<td>$JOB</td>
<td>Contains your operating system job number on the VistA M Server.</td>
</tr>
<tr class="odd">
<td><span id="_Toc384204759" class="anchor"></span>$ORDER</td>
<td><p>M code:</p>
<p>$ORDER(variable name{,integer code})</p>
<p>Returns the subscript of the previous or next sibling in collating sequence of a specified array node.</p>
<p>To obtain the first subscript of a level, specify a <strong>NULL</strong> subscript in the argument.</p></td>
</tr>
<tr class="even">
<td>Remote Procedure Call</td>
<td>A remote procedure call (RPC) is essentially M code that may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="odd">
<td>SAML</td>
<td>Security Assertion Markup Language. An XML-based industry standard for communicating identities over the Internet.</td>
</tr>
<tr class="even">
<td>Server</td>
<td>The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION (#19) file. An automated mail protocol that is activated by sending a message to a server at another location with the “<strong>S.server</strong>” syntax. A server’s activity is specified in the OPTION (#19) file and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td>User Access</td>
<td><p>This term is used to refer to a limited level of access to a computer system that is sufficient for using/operating software, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any of VistA’s options can be locked with a security key (e.g., XUPROGMODE, which means that invoking that option requires programmer access).</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="even">
<td>User Interface</td>
<td>The way the software is presented to the user, such as Graphical User Interfaces that display option prompts, help messages, and menu choices. A standard user interface can be achieved by using Embarcadero’s Delphi Graphical User Interface to display the various menu option choices, commands, etc.</td>
</tr>
<tr class="odd">
<td>Window</td>
<td>An object on the screen (dialogue) that presents information such as a document or message.</td>
</tr>
<tr class="even">
<td>XML</td>
<td>eXtensible Markup Language.</td>
</tr>
<tr class="odd">
<td><span id="_Toc384285598" class="anchor"></span>XUPROGMODE</td>
<td>A security key distributed by Kernel as part of its Menu Manager (MenuMan). This security key enables access to a number of developer-oriented options in Kernel.</td>
</tr>
</tbody>
</table>

![](xwb-1-1-73-developer-s-guide/335.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.